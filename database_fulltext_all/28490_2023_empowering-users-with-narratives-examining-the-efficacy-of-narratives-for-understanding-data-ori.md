---
otero_id: 28490
otero_key: "EQFDNQ79"
title: "Empowering Users with Narratives: Examining the Efficacy of Narratives for Understanding Data-Oriented Conceptual Models"
authors: "Merete Hvalshagen; Roman Lukyanenko; Binny M. Samuel"
year: "2023"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.1141"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Empowering Users with Narratives: Examining the Efficacy of Narratives for Understanding Data-Oriented Conceptual Models

Merete Hvalshagen,<sup>a</sup> Roman Lukyanenko,<sup>b</sup> Binny M. Samuel<sup>c,</sup>\*

<sup>a</sup> University of Dayton, Dayton, Ohio 45469; <sup>b</sup> University of Virginia, Charlottesville, Virginia 22903; <sup>c</sup> University of Cincinnati, Cincinnati, Ohio 45221

Contact: mhvalshagen1@udayton.edu (MH); romanl@virginia.edu (RL); samuelby@uc.edu, https://orcid.org/0000-0002-3223-4616 (BMS)

Received: Revised: August 14, 2021;<sub>Accepted:</sub> <sup>March 28, 2022</sup>Published Online in Articles in Advance: August 31, 2022

https://doi.org/10.1287/isre.2022.1141

Copyright:

Abstract. With the ongoing digitalization of human society, regular employees (e.g., noninformation technology experts) become increasingly autonomous and proactive in using organizational data and information technologies to facilitate data-driven actions and insights. This growing autonomy of regular employees (dubbed here, empowered users) in using information technologies creates new challenges. As most empowered users lack sophisticated information technology skills, they struggle to <sup>fi</sup>nd and access relevant data, understand their meaning, and extract and adapt them to meet their needs. We propose a powerful way to support empowered users with a combination of conceptual models and narratives. A data narrative is a descriptive and textual representation of one or more aspects of data in a domain that is organized and presented as a connected sequence of sentences in a natural language. We assess the ef<sup>fi</sup>cacy of narrative representations for conceptual modeling cardinality constraints, which are an essential part of understanding data. We conducted two laboratory experiments and found a positive and strong effect for narratives: cardinality constraints that were described in the narratives were better understood than constraints only represented in the model (i.e., script). This effect was robust across cardinalities, meas ures, script complexities, and familiarity levels with the conceptual modeling grammar.

![](/api/attachments/EQFDNQ79/fulltext/images/fd34b30b76343df4b65232a0609fb37e929f1f0dcc0d75c839ac1e92960e2a67.jpg)

History: Manju Ahuja, Senior Editor; Choon-Ling Sia, Associate Editor.

Open Access Statement: This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License. You are free to download this work and share with others, but cannot change in any way or use commercially without permission, and you must attribute thi work as “Information Systems Research. Copyright © 2022 The Author(s). https://doi.org/10.1287/ isre.2022.1141, used under a Creative Commons Attribution License: https://creativecommons.org licenses/bv-nc-nd/4.0/.

Supplemental Material: The online appendices are available at https://doi.org/10.1287/isre.2022.1141.

Keywords: empowered users conceptual modeling data management data analytics narratives laboratory experiment

## 1. Introduction

The <sup>fi</sup>rst users of computers were technical experts— thoroughly knowledgeable in both hardware and software (Aspray and Campbell-Kelly 1996, Hirschheim and Klein 2012). As computers began to be widely introduced in organizations, the cohort of users expanded and increasingly encompassed nontechnical organizational employees who lacked specialized expertise or training in computing (Gibson and Nolan 1973, Zuboff 1988). Concomitantly, a challenge emerged to effectively support nontechnical users.

Dating back to the 1970s, organizations began to rely on conceptual modeling (CM) to create scripts,<sup>1</sup> namely, (semi)formal, and mainly graphical, representations of application domains, to capture data to be stored and managed by an information system (IS), along with the rules for manipulating these data (Chen 1976, Bachman and Daya 1977, Bubenko 1979,

Roussopoulos and Mylopoulos 1989). Conceptual modeling emerged among the primary tools to support IS development. It proved indispensable in facilitating a wide range of activities, including representation of user requirements, database design, structuring data collection activities and processes, supporting information retrieval, interpretation and use of data, as well as interaction and communication among developers and nontechnical users (Hirschheim et al. 1995, Wand and Weber 2002).

Although conceptual modeling scripts were generally designed to be intuitive (Chen 1976, Gemino and Wand 2005, Moody 2009), their creation and interpretation continued to require some specialized knowledge. Speci<sup>fi</sup>cally, to ensure consistency of interpretation and implementation, conceptual modeling scripts conformed to grammars (syntax and rules for using and interpreting elements of a given type of script) that were sometimes arcane and dif<sup>fi</sup>cult to grasp. Consequently, research began to investigate the ability of users to interpret domain semantics conveyed in conceptual modeling scripts. Decades of research has generally concluded that nontechnical users continue to face dif<sup>fi</sup>- culties when learning and understanding conceptual modeling scripts (Topi and Ramesh 2002, Recker et al. 2011, Samuel et al. 2018).

The increasing digitalization in human society has both magni<sup>fi</sup>ed existing challenges and also brought about novel challenges. First, organizational reliance on IS has broadened and deepened (Legner et al. 2017). This has expanded the range and overall tech savviness of IS users for nearly every organization (e.g., business) function and role. Second, in the age of arti<sup>fi</sup>cial intelligence and data analytics, employees across every facet of business are hungry to be datadriven in their decision making (Khatri and Samuel 2019). These and other processes precipitated by the accelerating digitalization of society create a new cohort of users—empowered users—de<sup>fi</sup>ned here as non-IT professionals who are motivated to take autonomous initiative and action to implement a desired change using information technology.

As empowered users are frequently autonomous and not always as technically savvy as traditional programmers or database analysts, the demand for better data management support for these users continuously increases. We, therefore, seek to answer the following research questions: (1) How can we better understand the nature of data management needs of empowered users? (2) What methods, tools, and techniques can be developed to better support the data management activities of empowered users?

To our knowledge, no research to date explicitly thought to address these questions. At the same time, increasing calls from industry suggest that everyone needs to become familiar with data, databases, and data management (e.g., learn SQL,<sup>2</sup> implement business intelligence solutions; Meulen and Pettey 2018). Further, some industry estimates suggest as much as 80% of the time spent on data analytics is associated with data management activities<sup>3</sup> (e.g., identifying relevant data, exploring and understanding data). Hence, it is paramount for empowered users to understand data and their structure, and this could be facilitated with training on conceptual modeling scripts, which have traditionally served as the basis of data management. However, as empowered users are a diverse and heterogeneous group with different experiences and skills (Meulen and Pettey 2018), many may lack the ability (or motivation) to understand traditional conceptual modeling grammars in support of their data management and analytics activities; thus, it is unreasonable to expect every empowered user to become a conceptual modeling expert.

Emerging scholarship in conceptual modeling has sug gested making grammars simpler (e.g., based on general, commonly familiar classes) to support the data management needs of heterogeneous users (Lukyanenko et al. 2019a, Castellanos et al. 2020). However, these grammars are also less expressive. In this research, we seek to retain the richness and expressivity of traditional conceptual modeling while ensuring that empowered users can understand the scripts without having to undergo extensive training. We do so by using an auxiliary representation—a data narrative—to support conceptual modeling scripts. We de<sup>fi</sup>ne data narrative (hereafter, narrative) as a descriptive and textual representation of one or more aspects of the substance and form of a domain that is organized and presented as a connected sequence of sentences in a natural language. As multiple representations are increasingly used in the practice of conceptual modeling (Jabbari Sabegh et al. 2019, Recker and Green 2019), we use narratives to enable empowered users to unlock the utility of traditional conceptual modeling scripts for the analysis, design, development, implementation, and maintenance of IS, as well as for analyzing data.

Whereas narratives appear to be suitable for supporting empowered users, little is currently known about the advantages and limitations of using narratives in sup port of conceptual modeling activities (Malinova and Mendling 2021), especially by empowered users. In this paper, we begin to close this gap. Speci<sup>fi</sup>cally, we conceptualize the essential components (van den Broek 2010) for the design of narratives to help understand data-oriented conceptual modeling scripts. These scripts are typically diagrams that capture the substance and form of a domain (Burton-Jones and Weber 2014), such as entities and their roles, relationships, and/or attributes. Further, they are among the most widely used types of conceptual modeling scripts, with prominent examples being entity-relationship diagrams, Uni<sup>fi</sup>ed Modeling Language (UML) class diagrams, and object-role diagrams (Pilone and Pitman 2005, Khatri et al. 2006, Allen and March 2012, Bera et al. 2014). We consider how to maximize the potential of narratives as a supplement to scripts by exploring their effectiveness in various conditions (Lee and Baskerville 2012): (1) different levels of conceptual modeling grammar familiarity, thereby re<sup>fl</sup>ecting diverse levels of technical acumen among modern empowered users; and (2) different script complexities.

## 2. Conceptual Background

We begin by describing empowered users and their data management needs. We then outline why traditional con ceptual modeling scripts may not be a suf<sup>fi</sup>cient (or certainly a sole) solution to support empowered users. We conclude this section by turning to narratives as an auxiliary representation to help empowered users.

## 2.1. Empowered Users and Conceptual Modeling Scripts

A new cohort of IS users has emerged. In general, these users, who we refer to as empowered users, are different than prior users of IS. These users are more tech-savvy and data-driven in their decision making compared with the initial nontechnical organizational employees who lacked much training in computing (see Online Appendix A for more details on these users). As a result of the ongoing digitalization in society, users are increasingly autonomous, competent, and empowered (Newman and Vidler 2006, Niehaves et al. 2012, Junglas et al. 2014). Technology and the change that is made possible with its use, allows these people to explore new possibilities, learn new skills, and contribute their knowledge, curiosity, and creativity to the betterment of the organizations and society around them (Buhler¨ 2001, Gustavsson and Sta˚hl 2010, Sharma and Patil 2017, The Economist 2022).

Within organizations, empowered users rely on organizational data to conduct data analytics—that is, use data to facilitate informed actions and insight (Davenport et al. 2010). However, there could be a wide diversity of data literacy skills of empowered users. For example, one study found that 42% of organizational users of data identi<sup>fi</sup>ed themselves as nonexperts in technology (Graves and Hendler 2013). Whereas empowered users might have some familiarity with the domain of a data source, they may not have the intimate knowledge of databases and data models that store these data (Møller et al. 2020, Sagha<sup>fi</sup> et al. 2021). At the same time, understanding where to <sup>fi</sup>nd (e.g., in which database) and how to interpret and use the relevant data are prerequisites for data analytics (Davenport et al. 2010).

Conceptual modeling scripts are one prominent tool that can further promote user empowerment with respect to understanding data (Topi and Ramesh 2002, Recker et al. 2021). These scripts can be used to help users become more data literate and aware of how data are organized and <sup>fl</sup>ow through the organization (De Simoni 2021). They can also aid in interpreting and retrieving relevant data to support analytics activities by empowered users (Howson 2013, Edjlali and Sicular 2017, De Simoni 2021).

To appreciate the opportunities for conceptual modeling script use by empowered users, Online Appendix B contains a scenario that is becoming increasingly common in organizations. Organizations persistently encourage their users to acquire skills to perform their own data management and analytics tasks. The trend of automated machine learning (or AutoML), which promises to make AI solutions even more accessible to nonexperts by streamlining many tasks related to the training of machine learning models, also requires solid understanding of input data (He et al. 2021, Larsen and Becker 2021). It is clear that one of the critical skills needed is the ability to understand the semantics of data (Møller et al. 2020), which can be done with the use of conceptual modeling scripts.

The need to support empowered users signals a major shift for conceptual modeling, as it opens mod eling for the masses. However, the challenge is that empowered users in organizations are a vast and heterogeneous group. We cannot expect every user to have the same technical expertise and abilities. Thus, the focus of our research is to better support these diverse empowered users in understanding and using conceptual modeling scripts.

Figure 1 uses a two-by-two matrix to illustrate who we focus on in this research by categorizing empowered users along two dimensions—dependency on organizational data for their work and data literacy. Regarding dependency on organizational data (the vertical axis), empowered users in today’s workforce are expected to be data-driven. Thus, we believe the empowered users who would need to understand data would have a medium to high dependence on data to do their work. Regarding data literacy (the horizontal axis), users vary widely in their data literacy skills. Most users have some basic data literacy skills, whereas those with extremely high data literacy are less likely to need help understanding data and are also more likely to be pro<sup>fi</sup>cient in using conceptual modeling scripts. Yet, even these users may <sup>fi</sup>nd narratives helpful for communicating with less techsavvy colleagues.

Figure 1. (Color online) Empowered Users in Organizations High  
![](/api/attachments/EQFDNQ79/fulltext/images/5a67fb4bf0f03e732566910adbf45ae03b6ea65d4f5d5f0409a0f7c2a22702aa.jpg)

## 2.2. Difficulty Understanding Conceptual Modeling Scripts

One key reason why conceptual modeling scripts are dif<sup>fi</sup>cult to understand for empowered users is because these scripts are abstract (i.e., class-based) and are communicated via arti<sup>fi</sup>cially created grammars (Lukyanenko et al. 2019a, Eriksson and Agerfalk 2021, Mayr and Thalheim 2021). Although abstract scripts convey information in an ef<sup>fi</sup>cient and precise manner, this is often done at the expense of comprehensibility (Day and Goldstone 2012, Nathan 2012). To use scripts, one must be able to relate the abstract elements of the script with real-world instances in the domain (e.g., transforming the abstract representation into a more concrete one). Prior research has acknowledged this tension in understanding conceptual modeling scripts (Samuel et al. 2018, Eriksson et al. 2019). Narratives can include instances and are one potential solution to help empowered users cognitively relate the abstract to instances.

Second, conceptual modeling scripts are typically graphical in nature. Graphical representations (e.g., diagrams, models, schemas) are bene<sup>fi</sup>cial for many cognitive activities (Dansereau and Simpson 2009), including understanding. However, some aspects of information and meaning are dif<sup>fi</sup>cult to encode graphically (Bergen 2012). Instead, a multimedia approach, (i.e., graphics and text) is often advocated to facilitate understanding (Angwin et al. 2019). Narratives can serve as a text representation written in a natural language to enhance understanding of conceptual modeling scripts.

Studying every aspect of using narratives to improve conceptual modeling script understanding by empowered users is intractable in a single paper. Our work focuses on the relationship construct, which has been noted as the most dif<sup>fi</sup>cult, but also very important aspect of scripts (Bodart et al. 2001, Shanks et al. 2008, Samuel et al. 2018). Speci<sup>fi</sup>cally, the cardinality constraints of relationship constructs re<sup>fl</sup>ect important aspects of data and their domain (Ram and Khatri 2005, Olive´ 2007, Currim and Ram 2012), such as “every account must be tied to a customer,” and these semantics are often challenging to understand (Batra et al. 1990, Bodart et al. 2001, Dunn et al. 2011, Samuel et al. 2018). Recent research has suggested that misunderstanding cardinalities may degrade data analytics (Lukyanenko et al. 2019b), for example, machine learning performance, a core technology of predictive analytics. Using Chen’s (1976) entity-relationship (ER) model (see Online Appendix C), we distinguish between two main types of relationship cardinality constraints—participation constraints and connectivity constraints (Thalheim 1992). It is critical for empowered users to grasp such semantics if they want to fully understand their data (De Simoni et al. 2015).

In line with prior research (Bodart et al. 2001, Khatri et al. 2006), our study looks at surface-level understanding with semantic tasks, which is consonant with the understanding empowered users would need from conceptual modeling scripts to know important aspects of the realworld domain from which the data were captured. We next turn to why narratives might help empowered users understand scripts.

## 2.3. Creating Narratives for Conceptual ModelingScripts

The use of narratives as text representations can be seen throughout the IS lifecycle (see (Alexander and Maiden 2004a, b) and are often used in combination with graphical representations such as use case diagrams (Cockburn 2000). Whereas the use of narratives with graphical representations has helped nontechnical individuals improve domain understanding (Arlow et al. 1998, Burton-Jones and Meso 2008), there are cognitive theories suggesting that narratives might not be useful. “More information” is not always better, and too much information can cause information overload (O’Reilly 1980, Eppler and Mengis 2004), leading to confusion instead of enlightenment. For example, Burton-Jones and Meso (2008) found that unde certain circumstances, individuals did signi<sup>fi</sup>cantly worse on understanding tasks when a narrative was provided compared with when no narrative was provided.

Stories are an essential part of humanity and are deeply embedded into human culture and cognition (e.g., the way we remember experiences; Damasio 2010, Kahneman 2011). Cognitive psychology has suggested that information conveyed in the form of narratives as a genuine story is understandable to a wide audience (Schank and Abelson 1995). Ryan (2007) proposes that narratives as genuine stories use speci<sup>fi</sup>c properties to convey information from four dimensions: spatial, temporal, mental, and formal and pragmatic. The spatial dimension suggests that narratives should be populated with real (reallike) persons interacting with concrete objects, preferably situated in a speci<sup>fi</sup>c place (Abbott 2008). Regarding the temporal dimension, narratives include actions and events occurring in a speci<sup>fi</sup>c time frame. The mental dimension suggests that characters in the narrative respond and make decisions to the events in the narrative with intention and purposefulness, and their responses are motivated by goals. In other words, the characters are not inanimate bystanders; rather, they make a conscious effort to re<sup>fl</sup>ect on and interact with the world around them. Last, the formal and pragmatic dimension suggests that the actions are usually causally linked, forming a chain of events. The chain of events should communicate something meaningful to the reader, like progress toward a goal. Collectively, the properties in these dimensions form a “sliding scale” that expresses the degree to which a text is a narrative, as opposed to a dichotomous classi<sup>fi</sup>cation (Abbott 2008).

IS narratives traditionally only included properties from one or two of the dimensions mentioned above. Alexander and Maiden (2004b) provide a best-practices perspective of narratives during the IS lifecycle with dozens of examples, albeit no data narratives. To our knowledge, no IS study has fully considered how to make information in narratives understandable to a wide audience of empowered users with empirical support. Furthermore, prior use of IS narratives has typically relied on abstraction instead of using instances. Thus, less is known about the explicit use of data narratives to support the semantics of conceptual modeling scripts.

Our current study operationalizes properties of narratives from all four dimensions (see Table 1) to create a narrative supplement to accompany conceptual modeling scripts. The narrative supplement explains aspects of the substance and form of a domain depicted in the script. We note that we use the formal and pragmatic dimension consistent with our de<sup>fi</sup>nition of a data narrative as a descriptive and textual representation of one or more aspects of data in a domain that is organized and presented as a connected sequence of sentences in a natural language (Benyon and Macaulay 2004, Hvalshagen 2011).

## 3. Theory and Hypotheses

We use cognitive load theory (henceforth, CLT) (Sweller 1994, van Merrienboer and Sweller¨ 2005, Sweller 2010) to hypothesize the ef<sup>fi</sup>cacy of narratives to help empowered users understand conceptual modeling scripts. CLT has gained popularity as a theoretical foundation for IS research (Browne and Parsons 2012), in particular when studying the understanding of IS representations (Gemino 2004, Burton-Jones and Meso 2008, Gemino and Parker 2009, Bera et al. 2019).

## 3.1. Narratives Supplementing Conceptual Data Models

According to CLT, an individual’s working memory is essential for cognitive tasks, including understanding information in representations. However, individuals have limited cognitive capacity (Eysenck 1991, McNamara and Scott 2001), and if a cognitive task pla ces too high demand (i.e., cognitive load) on an individual’s working memory, cognitive overload occurs and inhibits successful completion of the task (Paas et al. 2003, Sweller 2010). The amount of cognitive load is in<sup>fl</sup>uenced by three factors (Paas and Van Merrienboer¨ 1994): (1) the characteristics of the task (e.g., the inherent complexity of understanding a representation); (2) the characteristics of the individual (e.g., IQ, skills); and (3) the interaction between the task and the individual (i.e., some abilities amplify or inhibit challenges related to different tasks).

Table 1. Properties of Narratives Operationalized to Supplement Data-Oriented Conceptual Modeling Scripts, Adapted from Abbott (2008) and Ryan (2007)

<table><tr><td>Narrative dimension</td><td>Property label</td><td>Narrative property definition and an example for data-oriented conceptual modeling scripts</td></tr><tr><td>Spatial</td><td>Real(-like) people</td><td>The narrative is about particular named characters. Example: “Veronica is a 36-year-old woman living in Mason, OH.”</td></tr><tr><td>Spatial</td><td>Specific places</td><td>The narrative takes place at specific places. Example: “When Veronica started, she was assigned to Central Ohio.”</td></tr><tr><td>Spatial</td><td>Concrete objects</td><td>The narrative refers to instances of objects or examples of objects. Example: “Most products like the ‘Organic Kitchen Cleaner’ are available through several subscription plans.”</td></tr><tr><td>Temporal</td><td>Timeframe</td><td>Events are arranged in a timeframe. Example: “However, before Veronica became region manager for the Central Ohio region, Central Ohio did not have a region manager.”</td></tr><tr><td>Mental</td><td>Evidence of consciousness</td><td>The characters in the narrative act in ways that imply thinking and deciding. Example: “Veronica left her full-time job after becoming a mother to a set of twins, but when the twins started preschool, she was looking for something to do part-time.”</td></tr><tr><td>Formal and pragmatic</td><td>Causally linked events</td><td>All actions (initiated by people or not) in the narrative are usually causally linked, forming a chain of events. We operationalized this with the premise that the narrative is a connected sequence of activity. The narrative is not just one sentence.</td></tr><tr><td>Formal and pragmatic</td><td>Meaningful facts</td><td>The narrative must communicate facts and something of meaning to the reader. We operationalized this with the premise that the narrative is a descriptive and textual representation of one or more aspects of data in a domain. The text communicates meaningful facts of the domain semantics to the reader.</td></tr></table>

We apply CLT to our work to examine empowered users as people who generally do not have very high data literacy skills (see Section 2.1) and are nonexperts in the cognitive task of understanding conceptual modeling scripts. We focus on reducing the inherent complexity of understanding scripts by providing helpful additional information (i.e., germane load according to CLT) as a narrative supplement. For example, to explain that an ANTIQUE CAR can be owned by multiple MEMBERs of a club chapter together (see Figure 2), a portion of the narrative can state: “Martha is married to John, and the two of them own a 1956 Audi together. They are therefore both registered as owners of that antique car.”

Narratives will be helpful for two principal reasons. First, a narrative conveys information in a manner that is easy to understand, thereby lessening the cognitive load of understanding it while using a conceptual modeling script. Encoding information in text using natural everyday language is consistent with the way individuals make sense of the world around them (Bergen 2012); natural language is accessible and essential to conveying meaning. Further, humans have cognitive capacities dedicated to processing language. Providing empowered users additional information in the form of explanations in a narrative supplement will allow them to use both their cognitive visual information processing resources (i.e., using the graphical script), as well as their cognitive verbal processing resources that interact in their working memory (Mayer 2005, Mayer 2014).

Second, CLT suggests that a representation should pair abstract concepts with their referents (i.e., individual objects or instances) to improve understanding of information (Paas and van Gog 2006, Sweller 2006, Renkl et al. 2009, Renkl and Atkinson 2010). Abstract and instance information together helps individuals create knowledge schemas (Sweller 2006, Kalyuga 2010), which are vital to complex cognitive tasks (Ericsson et al. 2006). Knowledge schemas reside in an individual’s long-term memory as the synthesis of their understanding and help alleviate working memory. Indeed, a goal of effective representations is to aid the creation and activation of knowledge schemas. In our work, a conceptual modeling script serves as the abstract representation of the domain (Wand et al. 1995), while the narrative serves as the instance representation. Instances help facilitate knowledge schemas because they provide repeated exposure and analogy to the abstract information (Renkl 2005), ready-made examples that can be copied (Atkinson et al. 2000), and encourage knowledge elaboration where new knowledge is intertwined with one’s prior knowledge (Kalyuga 2009).

Instances are helpful to individuals for many cognitive activities (Allen and Brooks 1991), including understand ing conceptual modeling scripts. Providing instances to individuals via narratives is especially potent because it supports a naturally occurring cognitive process of simulation in which individuals imagine or create mental scenes or pictures of the information presented in sentences (Bergen 2012). This simulation allows individuals to visualize the sentences as if they can observe the events unfolding in their minds, and thereby better understand the information. Individuals attempt to simulate with even abstract concepts (e.g., the text labels on a conceptual modeling script) during understanding; however, simulation is facilitated with instances. Furthermore, the narrative ordering of the sentences provides individuals with an incremental guide to their simulation. Empowered users will be able to create better mental simulations with instances in narratives to understand the details represented by the script.

In summary, empowered users with both a conceptual modeling script and narrative supplement should have a better understanding of the substance and form of a domain. This additional information in a narrative will reduce the demand on their working memory by allowing them to use their cognitive verbal processing resources, create and activate knowledge schemas, and facilitate simulation. This leads to our <sup>fi</sup>rst hypothesis (see Figure 3).

Hypothesis 1 (H1). Providing a conceptual modeling script with a narrative supplement will improve domain understanding of both connectivity and participation car dinality constraints.

Prior research has suggested that people struggle more with understanding participation constraints compared with connectivity constraints (Wand et al. 1999, Bodart et al. 2001, Burton-Jones et al. 2012, Samuel et al. 2018). We, therefore, assume that if cardinality constraints are not accompanied by a narrative, then connectivity constraints would be better understood than participation constraints. Furthermore, if participation constraints are more challenging to grasp than connectivity constraints, then we expect that narratives will aid understanding of participation constraints more than connectivity constraints. If there is more confusion without a narrative supplement, then there is more opportunity for understanding to be facilitated. This leads us to our second hypothesis (see Figure 3).

Figure 2. Excerpt from an Entity-Relationship Diagram  
![](/api/attachments/EQFDNQ79/fulltext/images/90cfbc2477a0a232034574105257750d4f014a076966beba2e23b0da3a4bb3a9.jpg)

Hypothesis 2 (H2). Narrative supplements will have a greater positive effect on the domain understanding of participation constraints compared with connectivity constraints.

## 3.2. Boundary Conditions

For the above hypotheses, we consider two important boundary conditions: (1) familiarity level with a conceptual modeling grammar (Khatri et al. 2006); and (2) script complexity (Moody 2009). We examine the heterogeneity of data literacy backgrounds of empowered users with respect to the usefulness of narratives by considering individuals with different levels of familiarity with conceptual modeling grammars. We assess the effect of narratives (Hypothesis 1) across two separate groups: one with lower familiarity and one with higher familiarity with a conceptual modeling grammar. We also consider the bene<sup>fi</sup>t of narratives for different script complexities. In one experiment, we use a conceptual modeling script with four entity types and three relationships, and the other uses a conceptual modeling script with 10 entity types and 10 relationships.

## 4. Experiments and Results

To test our hypotheses, we conducted one pilot study and two experiments. We used the ER model to create ER diagrams with cardinality constraints to operationalize conceptual modeling scripts. We also created a narrative supplement for each ER diagram using all the dimensions and properties from Section 2.3. Experiment 1 assessed the effect of a narrative supplement on the understanding of cardinality constraints (Hypothesis 1), checking for differences in connectivity versus participation constraints (Hypothesis 2). We cultivated participants with different levels of conceptual modeling grammar familiarity. Experiment 2 reassessed Hypothesis 1 using a more complex conceptual modeling script and added novel measures of understanding.

## 4.1. Experiment 1—The Effect of Narrative Supplements

4.1.1. Experiment 1 Design. We used three factors in a mixed design for Experiment 1. In crafting this design, we wanted to balance the advantages of statistical power and internal validity from within-subject factors while avoiding confounds that would leave us unable to isolate the treatment effects we wanted to assess. The <sup>fi</sup>rst factor was a within-subjects use of connectivity and participation cardinality constraints in the ER diagrams ( cardinality type). We used a balanced number of each cardinality type (i.e., connectivity vs. participation) in each ER diagram in order to assess the effect of narratives for the different types.

The second factor was the within-subjects use of explained versus unexplained ER diagram cardinality constraints using a narrative supplement ( narrativ explanation). We chose to explain only some of the ER diagram cardinality constraints. If participants could better understand cardinality constraints explained in the narrative supplement compared with those unexplained, then this would provide support for the ef<sup>fi</sup>cacy of narratives. The narrative explanations were balanced across the type of cardinality con straints so that an equal number of connectivity and participation constraints were described for each ER diagram.

Last, a randomized block-design between-subjects factor of training ( training) provided a mechanism for us to operationalize our boundary condition of different levels of conceptual modeling grammar familiarity (see Section 3.2). Participants received one of two training videos described in the next section. Some of the participants would be trained in the speci<sup>fi</sup>c grammar used in our experimental material, whereas the rest would be trained in another grammar. Both videos focused on cardinality constraints in conceptual modeling grammars and scripts; they outlined the different types of cardinality constraints and showed how they could be represented using a particular conceptual modeling grammar. No training was provided for the narrative supplement.

4.1.2. Experiment 1 Materials. We developed three sets of materials to support our design. First, pertaining to the cardinality type and narrative explanation factors (see Section 4.1.1), we used two moderately familiar domains (Bera et al. 2014) (“Antique Car Club” and “High School Tutoring”) to create two ER diagrams and two narrative supplements. The two diagrams were similar in design and had relatively low complexity (four entity types and three relationships). The narrative supplements were similar with respect to their length and explanations of 4 of the 12 cardinality constraints (e.g., two participation and two connectivity) in their respective ER diagram. See Online Appendix D.1 for the ER diagrams and their narratives, as well as the rationale for our domain choices.

Figure 3. Research Model for Hypothesis 1 and Hypothesis 2  
![](/api/attachments/EQFDNQ79/fulltext/images/4e6df73b372e3d1951c130981a9f2956fc987540ec0714b4be263a6eddf4e290.jpg)

Second, pertaining to the training factor (see Section 4.1.1), we developed two training videos. One video taught the ER model using ER diagrams with crow’s feet notation ( ER-trained), whereas the other taught the set notation using set diagrams ( set-trained) (Elmasri and Navathe 2010). The ER model (Chen 1976) encodes data semantics in classes in ER diagrams, and the combination of ER diagrams with crow’s feet notation is well known and widely used (Davies et al. 2006, Fettke 2009, Moody 2009). Set diagrams encode cardinality constraint semantics of a domain with an emphasis on instances, as opposed to symbols or numbers, and have been used in prior research on the understanding of conceptual modeling scripts and cardinality constraints (Samuel et al. 2018). ER-trained individuals would have high familiarity with the grammar used for the experiment, whereas set-trained would have low familiarity.

Last, the dependent variable of this study was domain understanding of the cardinality constraint semantics depicted in the ER diagrams. Understanding was measured as the “percentage correct” score on a semantic task with true/false questions. All cardinality constraints in the ER diagrams had a corresponding question and could be answered with the diagram alone. See Online Appendix D.1 for the task questions.

Figure 4 illustrates our intended interplay between the experimental material. It depicts a portion of the narrative supplement that explains a cardinality constraint in the corresponding portion of the ER diagram and an associated true/false question to measure understanding.

Figure 4. (Color online) Illustration of Experiment 1 Material Interplay  
![](/api/attachments/EQFDNQ79/fulltext/images/6c1d164aabc09c8ae4a3d886a9fbf4490a5c6f2f58c84f0dcdd3526572ac9da3.jpg)

4.1.3. Pilot of Materials and Procedures for Experiment 1. We ran a pilot study to assess the potential of narrative supplements for conceptual modeling scripts and to get feedback on the understandability of our materials and inform our procedures. Key results from our pilot indicated that participants performed signi<sup>fi</sup>cantly better on questions when cardinality constraints were explained in a narrative compared with when they were left unexplained (p < 0.001, Cohen’s d <sub>-</sub> 1.97;<sup>4</sup> see Online Appendix E).

4.1.4. Experiment 1 Procedures. Experiment 1 had <sup>fi</sup>ve stages (see Figure 5). First, participants completed a background survey so that we could characterize their age, work experience, conceptual modeling experience, and database experience. Next, the partici pants watched a short training video based on random assignment to one of the conceptual modeling grammar familiarity conditions (i.e., “ER-trained” vs. “set-trained”). After the training, in stage 3 the participants completed a practice task to ensure they understood the concepts in their training (e.g., syntax). Last, participants received the ER diagrams and narrative supplements and completed the task for the two domains in a randomized order (stages 4 and 5). The participants were instructed to use both the diagram and the narrative when answering the questions.

4.1.5. Experiment 1 Participants. A total of 223 undergraduate students drawn from two courses offered in the business school of a university in the United States participated in Experiment 1. Participation was voluntary and resulted in a small amount of extra credit for the course. Average conceptual modeling experience and database experience were low (see Online Appendix F.1 for details). Our participants were good proxies for empowered users in general (Tarca et al. 2008, Romero et al. 2014) and, in particular, those who do not have extensive experience in conceptual modeling (Ottensooser et al. 2012, Samuel et al. 2018). Further, students are often asked to learn a concept in an academic setting while paying close attention to the topic, and then demonstrate their understanding of the topic on an academic assessment akin to the questions in our task. This is consistent with the expectations of empowered users being asked to interpret or learn about data in novel domains (see Online Appendix B). We veri<sup>fi</sup>ed that our participants would understand the task and domain because we used a moderately familiar domain and gave them a practice task to ensure that they understood the concepts in the training (questions about the syntax). Also, the previously mentioned pilot study helped assure us that participants understood our materials and procedures.

Figure 5. (Color online) The Five Stages of the Experimental Procedure  
![](/api/attachments/EQFDNQ79/fulltext/images/a50edc29492a5f0a8890716f146f28777ba22eef83c1cdbc768f3a851a7d9fae.jpg)

## 4.2. Experiment 1 Analysis and Results

Understanding was assessed by awarding one point for each correct true/false response. The performance for all 24 questions across the two domains was combined. Manipulation checks with one-way randomizedgroups analysis of variance (ANOVA) and one-way repeated-measures ANOVA tests (see Online Appendix G.1) suggested three conclusions. First, our training had a desirable effect on performance and resulted in two groups with different levels of ER model familiarity $( p < 0 . 0 0 1 , \ d = 1 . 6 5 )$ . Second, consistent with our pilot study, narrative explanations had a positive effect on performance (ER-trained: $p < 0 . 0 0 1 , d = 0 . 2 3 ;$ set-trained: $p < 0 . 0 0 1 , d = 1 . 0 7 )$ . Third, without a narrative explanation, connectivity constraints were better understood than participation constraints (ER-trained: $p { < } 0 . 0 0 1$ $d = 0 . 5 6 ;$ set-trained: $p < 0 . 0 0 1 , d = 1 . 6 7 )$

A three-way mixed ANOVA (Tabachnick and Fidell 2000) was carried out on the complete set of independent variables (see Table 2): cardinality type (connectivity vs. participation), narrative explanations (explained vs. unexplained by the narrative), and training (ER-trained vs. set-trained). The three-way mixed ANOVA showed an interaction effect, indicating that the effect of narrative explanations on the understanding of cardinality constraints was different for the ER-trained group compared with the set-trained group. Thus, we analyzed these two groups separately in the rest of our analysis.

To assess Hypothesis 1, we performed a pairedsample t-test<sup>5</sup> comparing the score for explained cardinality constraints with the score for unexplained cardinality constraints. For connectivity constraints, neither ER-trained nor set-trained participants showed a signi<sup>fi</sup>cant improvement in understanding with narrative explanations; see the solid lines in the Figure 6 panels (ER-trained: $p = 0 . 4 7 , d = 0 . 0 0 ;$ set-trained: $p = 1 . 0 , d = 0 . 1 7 )$ and Table 10 in Online Appendix H.1 for more details. For participation constraints, both ER-trained and set-trained participants showed a signi<sup>fi</sup>- cant improvement in understanding with narrative explanations; see the dashed lines in Figure 6 (ER-trained: $p { < } 0 . 0 0 1$ , d 0.39; set-trained: $p { < } 0 . 0 0 1$ , d 1.98) and Table 11 in Online Appendix H.1. Overall, Hypothesis 1 was conditionally supported among the constraint types.

We assessed Hypothesis 2 by testing for a difference in the magnitude of improvement for participation constraints versus the magnitude of improvement for connectivity constraints using a paired-sample t-test. ER-trained participants showed no improvement in their performance with narrative explanations of connectivity constraints but had an 8.6 percentage point improvement in their score for participation constraints. This was a signi<sup>fi</sup>cant difference $( p < 0 . 0 0 1 , d = 0 . 3 8 )$ ; see Figure 7 and Table 12 in Online Appendix H.1. Set-trained participants had a 3.9 percentage point improvement for explained connectivity constraints compared with a 35 percentage point improvement for participation constraints; this was also a signi<sup>fi</sup>cant difference (p < 0.001, d 1.06). Hypothesis 2 was therefore supported.

## 4.3. Experiment 2: The Effect of Narrative

Supplement for Increased Script Complexity 4.3.1. Experiment 2 Design. For Experiment 2, we reused two factors from Experiment 1 in a withinsubject design: (1) cardinality type; and (2) narrative explanation. These factors were operationalized in an ER diagram and a narrative supplement for a home selling domain. The ER diagram was more complex than Experiment 1 to examine the boundary condition of increased script complexity (see Section 3.2). We wrote one narrative for the ER diagram but split it into two versions to reduce idiosyncrasies with respect to which cardinality constraints were explained by the narrative supplement and our results. We also incorporated different measures of domain understanding to further af<sup>fi</sup>rm the positive effect of narratives.

Table 2. Results of Three-Way Mixed ANOVA (Experiment 1)

<table><tr><td rowspan="2" colspan="2">Effect</td><td colspan="6">Multivariate testsa</td></tr><tr><td>Value</td><td>F</td><td>Hypothesis degrees of freedom</td><td>Error degrees of freedom</td><td>p-value</td><td>Partial η2</td></tr><tr><td rowspan="4">Narrative explanations</td><td>Pillai&#x27;s trace</td><td>0.216</td><td>61.000b</td><td>1.000</td><td>221.000</td><td>0.000</td><td>0.216</td></tr><tr><td>Wilks&#x27;s lambda</td><td>0.784</td><td>61.000b</td><td>1.000</td><td>221.000</td><td>0.000</td><td>0.216</td></tr><tr><td>Hotelling&#x27;s trace</td><td>0.276</td><td>61.000b</td><td>1.000</td><td>221.000</td><td>0.000</td><td>0.216</td></tr><tr><td>Roy&#x27;s largest root</td><td>0.276</td><td>61.000b</td><td>1.000</td><td>221.000</td><td>0.000</td><td>0.216</td></tr><tr><td rowspan="4">Narrative explanations × training</td><td>Pillai&#x27;s trace</td><td>0.101</td><td>24.900b</td><td>1.000</td><td>221.000</td><td>0.000</td><td>0.101</td></tr><tr><td>Wilks&#x27;s lambda</td><td>0.899</td><td>24.900b</td><td>1.000</td><td>221.000</td><td>0.000</td><td>0.101</td></tr><tr><td>Hotelling&#x27;s trace</td><td>0.113</td><td>24.900b</td><td>1.000</td><td>221.000</td><td>0.000</td><td>0.101</td></tr><tr><td>Roy&#x27;s largest root</td><td>0.113</td><td>24.900b</td><td>1.000</td><td>221.000</td><td>0.000</td><td>0.101</td></tr><tr><td rowspan="4">Cardinality type</td><td>Pillai&#x27;s trace</td><td>0.002</td><td>0.431b</td><td>1.000</td><td>221.000</td><td>0.512</td><td>0.002</td></tr><tr><td>Wilks&#x27;s lambda</td><td>0.998</td><td>0.431b</td><td>1.000</td><td>221.000</td><td>0.512</td><td>0.002</td></tr><tr><td>Hotelling&#x27;s trace</td><td>0.002</td><td>0.431b</td><td>1.000</td><td>221.000</td><td>0.512</td><td>0.002</td></tr><tr><td>Roy&#x27;s largest root</td><td>0.002</td><td>0.431b</td><td>1.000</td><td>221.000</td><td>0.512</td><td>0.002</td></tr><tr><td rowspan="4">Cardinality type × training</td><td>Pillai&#x27;s trace</td><td>0.003</td><td>0.566b</td><td>1.000</td><td>221.000</td><td>0.453</td><td>0.003</td></tr><tr><td>Wilks&#x27;s lambda</td><td>0.997</td><td>0.566b</td><td>1.000</td><td>221.000</td><td>0.453</td><td>0.003</td></tr><tr><td>Hotelling&#x27;s trace</td><td>0.003</td><td>0.566b</td><td>1.000</td><td>221.000</td><td>0.453</td><td>0.003</td></tr><tr><td>Roy&#x27;s largest root</td><td>0.003</td><td>0.566b</td><td>1.000</td><td>221.000</td><td>0.453</td><td>0.003</td></tr><tr><td rowspan="4">Cardinality type × narrative explanations</td><td>Pillai&#x27;s trace</td><td>0.352</td><td>120.246b</td><td>1.000</td><td>221.000</td><td>0.000</td><td>0.352</td></tr><tr><td>Wilks&#x27;s lambda</td><td>0.648</td><td>120.246b</td><td>1.000</td><td>221.000</td><td>0.000</td><td>0.352</td></tr><tr><td>Hotelling&#x27;s trace</td><td>0.544</td><td>120.246b</td><td>1.000</td><td>221.000</td><td>0.000</td><td>0.352</td></tr><tr><td>Roy&#x27;s largest root</td><td>0.544</td><td>120.246b</td><td>1.000</td><td>221.000</td><td>0.000</td><td>0.352</td></tr><tr><td rowspan="4">Cardinality type × narrative explanations × training</td><td>Pillai&#x27;s trace</td><td>0.142</td><td>36.566b</td><td>1.000</td><td>221.000</td><td>0.000</td><td>0.142</td></tr><tr><td>Wilks&#x27;s lambda</td><td>0.858</td><td>36.566b</td><td>1.000</td><td>221.000</td><td>0.000</td><td>0.142</td></tr><tr><td>Hotelling&#x27;s trace</td><td>0.165</td><td>36.566b</td><td>1.000</td><td>221.000</td><td>0.000</td><td>0.142</td></tr><tr><td>Roy&#x27;s largest root</td><td>0.165</td><td>36.566b</td><td>1.000</td><td>221.000</td><td>0.000</td><td>0.142</td></tr></table>

<sup>a</sup>Design: Intercept training  
Within Subjects Design: narrative explanations cardinality type narrative explanations cardinality type <sup>b</sup>Exact statistic.

Figure 6. (Color online) Hypothesis 1 Results (Experiment 1)  
![](/api/attachments/EQFDNQ79/fulltext/images/1d50c3296c6c7287ceb78d3eab8a3d476c13dcac40a2b52e5073ecfa2b4c5255.jpg)

4.3.2. Experiment 2 Materials. We developed two new sets of materials to support our design. First, we used another moderately familiar domain (home selling) to create an ER diagram and two versions of a narrative supplement. The ER diagram had 10 entity types and 10 relationships; thus, it was more complex than the diagrams in Experiment 1. We created one narrative supplement that explained 32 ER diagram cardinality constraints corresponding to each task question (described in the next paragraph). However, to support our within-subject design, we split the narrative into two similar versions (e.g., V1 and V2), such that each narrative version would only explain 16 of the cardinality constraints in our task questions, leaving the other half unexplained. There was no overlap for explained cardinality constraints in the versions with respect to the task questions.<sup>6</sup> See Online Appendix D.2 for the ER diagram and narrative supplement.

Figure 7. (Color online) Hypothesis 2 Results (Experiment 1)  
![](/api/attachments/EQFDNQ79/fulltext/images/af5c1748cb430684b329f104d76456a07def0888d92c31de1b1cd763fb81186e.jpg)

We used understanding (“percentage correct”) on a semantic task again as our dependent variable (see Experiment 1) but measured it in two different ways. We created 16 statement questions and 16 yes/no scenario questions that each covered an equal number of participation and connectivity constraints in the ER diagram. Each statement question included a correct and an incorrect statement regarding the same cardinality constraint in the ER diagram and instructed participants to choose the correct one. The scenario questions used some narrative properties (see Table 1) and were instantiated with values from the home selling domain as opposed to the narrative supplement. All questions could be answered with the ER diagram alone. See Online Appendix D.2 for representative task questions.

4.3.3. Experiment 2 Procedures. We essentially followed the same procedure as Experiment 1 (see Figure 5). Differences include stage 2, where participants were only ER-trained, and we only had one stage for the task where participants answered all 32 questions. The distribution of the narrative supplement versions was randomized; thus, only half of the ER diagram cardinality constraint task questions were explained for each participant.

4.3.4. Experiment 2 Participants. We recruited 60 undergraduate students drawn from a mandatory course offered in the business school of a university in the United States. Participation was voluntary, and participants could earn a small amount of course credit for participation. Average conceptual modeling experience and database experience were low; see Online Appendix F.2.

## 4.4. Experiment 2—Analysis and Results

Understanding was assessed by awarding one point for each correct response. Percentage correct performance scores for the 16 statement questions and the 16 scenario questions were tallied separately. Manipula tion checks conducted with paired-sample t-tests (see Tables 6–9 in Online Appendix G.2) found similar results as Experiment 1 across the question types. Narrative explanations had a positive effect on performance (statement questions: p < 0.001, d 0.85; scenario questions: p < 0.001, d 0.73), and that connectivity constraints were better understood than participation without a narrative explanation on statement questions (statement questions: p < 0.001, d 0.62; scenario questions: p 0.441, d 0.12).

The overall model was assessed with two-way repeated-measures ANOVA tests, including the complete set of independent variables for this study: cardinality type (connectivity vs. participation) and narrative explanations (explained vs. unexplained by the narrative). We ran an ANOVA once for statement questions and once for scenario questions (see Tables 3 and 4). The ANOVAs showed a signi<sup>fi</sup>cant positive effect for narrative explanations on the understanding of cardinality constraints for both question types. There was no signi<sup>fi</sup>- cant interaction between cardinality type and narrative explanations, indicating that narratives had an equally positive effect on both types of constraints. Hence our analysis proceeded by examining simple main effects.

Table 3. Results of Two-Way Repeated-Measures ANOVA, Statement Questions (Experiment 2)

<table><tr><td colspan="8">Statement questions percentage correct</td></tr><tr><td rowspan="2">Effect</td><td></td><td colspan="6">Multivariate testsa</td></tr><tr><td></td><td>Value</td><td>F</td><td>Hypothesis degrees of freedom</td><td>Error degrees of freedom</td><td>p-value</td><td>Partial η2</td></tr><tr><td rowspan="4">Cardinality type</td><td>Pillai&#x27;s trace</td><td>0.440</td><td>46.402b</td><td>1.000</td><td>59.000</td><td>0.000</td><td>0.440</td></tr><tr><td>Wilks&#x27;s lambda</td><td>0.560</td><td>46.402b</td><td>1.000</td><td>59.000</td><td>0.000</td><td>0.440</td></tr><tr><td>Hotelling&#x27;s trace</td><td>0.786</td><td>46.402b</td><td>1.000</td><td>59.000</td><td>0.000</td><td>0.440</td></tr><tr><td>Roy&#x27;s largest root</td><td>0.786</td><td>46.402b</td><td>1.000</td><td>59.000</td><td>0.000</td><td>0.440</td></tr><tr><td rowspan="4">Narrative explanation</td><td>Pillai&#x27;s trace</td><td>0.333</td><td>29.417b</td><td>1.000</td><td>59.000</td><td>0.000</td><td>0.333</td></tr><tr><td>Wilks&#x27;s lambda</td><td>0.667</td><td>29.417b</td><td>1.000</td><td>59.000</td><td>0.000</td><td>0.333</td></tr><tr><td>Hotelling&#x27;s trace</td><td>0.499</td><td>29.417b</td><td>1.000</td><td>59.000</td><td>0.000</td><td>0.333</td></tr><tr><td>Roy&#x27;s largest root</td><td>0.499</td><td>29.417b</td><td>1.000</td><td>59.000</td><td>0.000</td><td>0.333</td></tr><tr><td rowspan="4">Cardinality type × narrative explanation</td><td>Pillai&#x27;s trace</td><td>0.000</td><td>0.019b</td><td>1.000</td><td>59.000</td><td>0.890</td><td>0.000</td></tr><tr><td>Wilks&#x27;s lambda</td><td>1.000</td><td>0.019b</td><td>1.000</td><td>59.000</td><td>0.890</td><td>0.000</td></tr><tr><td>Hotelling&#x27;s trace</td><td>0.000</td><td>0.019b</td><td>1.000</td><td>59.000</td><td>0.890</td><td>0.000</td></tr><tr><td>Roy&#x27;s largest root</td><td>0.000</td><td>0.019b</td><td>1.000</td><td>59.000</td><td>0.890</td><td>0.000</td></tr></table>

Table 4. Results of Two-Way Repeated-Measures ANOVA, Scenario Questions (Experiment 2)

<table><tr><td colspan="8">Scenario questions percentage correct</td></tr><tr><td rowspan="2">Effect</td><td></td><td colspan="6">Multivariate testsa</td></tr><tr><td></td><td>Value</td><td>F</td><td>Hypothesis degrees of freedom</td><td>Error degrees of freedom</td><td>p-value</td><td>Partial η2</td></tr><tr><td rowspan="4">Cardinality type</td><td>Pillai&#x27;s trace</td><td>0.034</td><td> $2.087^b$ </td><td>1.000</td><td>59.000</td><td>0.154</td><td>0.034</td></tr><tr><td>Wilks&#x27;s lambda</td><td>0.966</td><td> $2.087^b$ </td><td>1.000</td><td>59.000</td><td>0.154</td><td>0.034</td></tr><tr><td>Hotelling&#x27;s trace</td><td>0.035</td><td> $2.087^b$ </td><td>1.000</td><td>59.000</td><td>0.154</td><td>0.034</td></tr><tr><td>Roy&#x27;s largest root</td><td>0.035</td><td> $2.087^b$ </td><td>1.000</td><td>59.000</td><td>0.154</td><td>0.034</td></tr><tr><td rowspan="4">Narrative explanation</td><td>Pillai&#x27;s trace</td><td>0.345</td><td> $31.046^b$ </td><td>1.000</td><td>59.000</td><td>0.000</td><td>0.345</td></tr><tr><td>Wilks&#x27;s lambda</td><td>0.655</td><td> $31.046^b$ </td><td>1.000</td><td>59.000</td><td>0.000</td><td>0.345</td></tr><tr><td>Hotelling&#x27;s trace</td><td>0.526</td><td> $31.046^b$ </td><td>1.000</td><td>59.000</td><td>0.000</td><td>0.345</td></tr><tr><td>Roy&#x27;s largest root</td><td>0.526</td><td> $31.046^b$ </td><td>1.000</td><td>59.000</td><td>0.000</td><td>0.345</td></tr><tr><td rowspan="4">Cardinality type × narrative explanation</td><td>Pillai&#x27;s trace</td><td>0.001</td><td> $0.071^b$ </td><td>1.000</td><td>59.000</td><td>0.791</td><td>0.001</td></tr><tr><td>Wilks&#x27;s lambda</td><td>0.999</td><td> $0.071^b$ </td><td>1.000</td><td>59.000</td><td>0.791</td><td>0.001</td></tr><tr><td>Hotelling&#x27;s trace</td><td>0.001</td><td> $0.071^b$ </td><td>1.000</td><td>59.000</td><td>0.791</td><td>0.001</td></tr><tr><td>Roy&#x27;s largest root</td><td>0.001</td><td> $0.071^b$ </td><td>1.000</td><td>59.000</td><td>0.791</td><td>0.001</td></tr></table>

<sup>a</sup>Design: Intercept  
Within Subjects Design: cardinality type <sub>+</sub> narrative explanations <sub>+</sub> cardinality type <sub>×</sub> narrative explanations <sup>b</sup>Exact statistic.

We carried out paired-sample t-tests comparing the performance on explained cardinality constraints to the performance on unexplained cardinality constraints (see Tables 13 and 14 in Online Appendix H.2). The results showed that narrative explanations had an overall positive effect on understanding of both connectivity (p < 0.001, d 0.78) and participation (p 0.01, d 0.64) constraints assessed using statement questions; see Figure 8. In addition, Hypothesis 1 also held true for scenario questions (connectivity: $p < 0 . 0 0 1 , d = 0 . 6 3 ;$ participation: $p < 0 . 0 0 1 , \ d = 0 . 5 8 )$ . These results support Hypothesis 1 for more complex conceptual modeling scripts and with different measures than Experiment 1, thus adding to the overall robustness of our <sup>fi</sup>ndings.

Figure 8. (Color online) Hypothesis 1 Results (Experiment 2)  
![](/api/attachments/EQFDNQ79/fulltext/images/1697dd156c2e2c988591825f996b70f10ebc0039e45adee9e32e88bc7b424051.jpg)

## 5. Discussion

We set out to help empowered users better understand data-oriented conceptual modeling scripts with a data narrative. Whereas the use of narratives is well established in IS (see, e.g., use cases, user stories, agile personas), they are not generally used for describing the semantics of the substance and form of a domain. Further, IS narrative design has traditionally relied on a higher level of abstraction via classes/roles and has not been instantiated with the dimensions/properties known to make narratives useful for human cognition. Prior to this research, less was known about how narratives should be designed for understanding conceptual modeling scripts, as well as how understanding would be impacted by different levels of familiarity with the conceptual modeling grammar and script complexities. Table 5 summarizes the <sup>fi</sup>ndings for Experiments 1 and 2.

In general, we found that narrative supplements bene<sup>fi</sup>ted participation constraints more but were useful for both types of cardinality constraints in more complex conceptual modeling scripts (the ER diagram used in Experiment 2 had 40 individual cardinality constraints compared with the 12 in each of the ER diagrams used in Experiment 1). Further, narratives did not seem to negatively interfere with the interpretation of the conceptual modeling scripts, even for the individuals more familiar with the grammar.

Table 5. Summary of Results for Experiments 1 and 2

<table><tr><td colspan="2"></td><td>Description</td><td>Result</td></tr><tr><td rowspan="2">Experiment 1</td><td>H1</td><td>Narrative supplements improve understanding of cardinality constraints in conceptual modeling scripts.</td><td>Supported for participation constraints (regardless of grammar familiarity)</td></tr><tr><td>H2</td><td>Narrative supplements improve understanding of participation constraints more than connectivity constraints.</td><td>Supported (regardless of grammar familiarity)</td></tr><tr><td>Experiment 2</td><td>H1</td><td>Narrative supplements improve understanding of cardinality constraints in conceptual modeling scripts.</td><td>Supported (more complex script and two different measures than Experiment 1)</td></tr></table>

## 5.1. Applicability Check

We conducted an applicability check with semistructured interviews to assess the external validity of our <sup>fi</sup>ndings and overall narrative usefulness (Rosemann and Vessey 2008). Interviewees were recruited from a graduate-level course on business intelligence from the business school at a university in the United States. All students in the course were given Experiment 2 as a class exercise, and <sup>fi</sup>ve students voluntarily agreed to participate in a follow-up discussion about the exercise. The <sup>fi</sup>ve participants had at least seven years of full-time work experience, and most were actively employed in a business role. Table 6 provides a summary of their backgrounds. The interviewees were also sked to indicate where they belonged on a modi-<sup>fi</sup>ed version of Figure 1 (without the shape overlay). Figure 9 visualizes their self-reported data.<sup>7</sup> In consideration of their demographics, experience, and skills/ abilities, our interviewees were representative of empowered users.

Interviews were conducted using virtual conferencing software in 30-minute sessions that included one interviewee and two authors of this study. One research member was the primary interviewer, while the other took notes and asked follow-up questions to understand key ideas and concepts. The sessions were recorded for transcription and subsequent analysis.

The session entailed the primary interviewer sharing the session goals and other instructions with the participant. Then, the participants were given statements to guide their placement on the matrix (see Figure 9 and Online Appendix I). Then the participants were asked to candidly answer the interview questions. We highlight two important questions discussed during the interviews:

1. Why (or why not) was the narrative helpful for answering questions about the ER diagram?

2. Would individuals in all quadrants <sup>fi</sup>nd narratives helpful to understand data?

Question 1 was asked to assess the theoretical rationale of this current study, and question 2 was asked to learn about the potential boundaries for the usefulness of narratives. We list key quotes from the interviews in Tables 7 and 8 (full quotes in Online Appendix J) and brie<sup>fl</sup>y discuss their conclusions.

The interviewees indicated that the narrative helped them better understand the conceptual modeling script and complete the exercise (see Table 7). They suggested that the narrative was helpful because it was written in an easy-to-understand manner, and it contained instances. Further, they also recognized the bene<sup>fi</sup>t of providing instances in a natural language format. One participant highlighted the ability to visualize the narrative in their mind. Broadly, these reasons aligned with our theoretical rationale.

Figure 9. Interviewee Self-Reported Empowered User Rating  
![](/api/attachments/EQFDNQ79/fulltext/images/e5d7f8b7a5387a1471f42695e1f9dfb8f989d1a89e486513df290746f3fb5a43.jpg)

Table 6. Background of Interviewees

<table><tr><td>Participant</td><td>Current role</td><td>Industry</td><td>Full-time work experience (years)</td><td>Gender</td></tr><tr><td>P1</td><td>Analyst</td><td>Manufacturing</td><td>15</td><td>Male</td></tr><tr><td>P2</td><td>Software tester</td><td>Genomics</td><td>12</td><td>Male</td></tr><tr><td>P3</td><td>Operations manager</td><td>Distribution operations</td><td>7</td><td>Male</td></tr><tr><td>P4</td><td>Buyer/planner</td><td>Manufacturing</td><td>39</td><td>Female</td></tr><tr><td>P5</td><td>Manager, joint venture and customer analytics</td><td>Aerospace</td><td>20</td><td>Female</td></tr></table>

Interviewees also commented that narratives would be helpful for many individuals in organizations (see Table 8). With narratives, empowered users could save time and effort from having to recall conceptual modeling syntax, and this would make data understanding more effortless. However, they suggested that those with extremely high data literacy might <sup>fi</sup>nd a narrative distracting. For those with low data literacy, narratives can help foster the understanding of data in the organization and keep different teams and individuals aligned in their interpretation and understanding of it. This would allow more consistency in behavior and improved outcomes for the organization, as more individuals would “be on the same page” and act in a more coordinated manner. Formally making narratives available could also inspire and help those with low data literacy to accelerate their journey to becoming more data-literate.

Based on our <sup>fi</sup>ndings, we conclude that more research on narratives for data is imperative, as they appear to hold so much potential.

## 5.2. Limitations

This study suffers from limitations of laboratory experiments with respect to the generalizability of our <sup>fi</sup>ndings (Roger and Kirk 1968, Tabachnick and Fidell 2000, Com peau et al. 2012). Although our participants representing empowered users were undergraduate students, they had a general familiarity with the domains, limited knowledge of conceptual modeling scripts, and matched the pro<sup>fi</sup>le of empowered users.<sup>8</sup> Hence, we judged that these students would be an acceptable proxy for organizational empowered users. We also conducted an applicability check with empowered users to con<sup>fi</sup>rm the generalizability of our ideas and <sup>fi</sup>ndings.

Second, similar to other studies in this area, we used surface-level tasks assessing one’s basic understanding of cardinality constraints (Shoval and Frumermann 1994,

Table 8. Selected Question 2 Quotes from the Application Check Interview

<table><tr><td>Question 2: Would individuals from all quadrants find narratives helpful to understand data?P1I mean, I want to say well it [a narrative] is useful for everyone at some point, but who is it the most useful for? I kind of lean toward if you have low data literacy [because] it&#x27;s going to be hard for you to extract these things [from the ER diagram alone].</td></tr><tr><td>P2I could imagine instances where all four [quadrants] would need data. Narratives would help a lot. For someone in my quadrant [top right], understanding data I would have to maybe go back to a textbook and reference it, and read it. Now [with the narrative], I can just off the top of my head understand what I&#x27;m seeing. The narrative was helpful in that situation. I know in terms of people with low dependence, low data literacy, nowadays, becoming data literate is almost required even on like some place like a floor of a warehouse or manufacturing, and it&#x27;s being required now I noticed.</td></tr><tr><td>P3I think if you get to the high data literacy those people might think it&#x27;s [narratives] a little bit tedious because maybe they&#x27;re able to analyze the data faster than having to read through a narrative.I&#x27;m an operations manager so I work with hourly associates that don&#x27;t necessarily need the data to perform their job, but it&#x27;s something that we want them to know is going on and where our overall operation is, how we&#x27;re servicing the customer, how their performances is, and those things. I think they would be in the bottom left quadrant, but the narratives would be something that can help them through like our preshifts when we talk with everybody about what&#x27;s going on in the business. To have a narrative that really explains the data in a way they understand would help keep the team on the same page.Maybe in the high dependence, but maybe low data literacy, if you&#x27;re trying to present something to a customer to help them understand why they might need to invest money in some sort of automation or piece of equipment, you don&#x27;t really necessarily know their data literacy. So having narratives to go along with whatever data or information you&#x27;re presenting them on how you&#x27;re going to improve the operation, lower costs, or those things would probably be beneficial to them. I think that the data are like the most important thing, is it [the investment] going to be beneficial to costs and efficiency, but also will they understand it [the data]?</td></tr><tr><td>P4The people that don&#x27;t rely on information [organizational data], or in the bottom half, a narrative might help them understand why it&#x27;s [data] is important. And then the people that already understand it&#x27;s important might not know what&#x27;s available as far as tools and education and learning, to get them into the upper right quadrant [data literate].</td></tr><tr><td>P5A narrative would help people [with low data literacy] understand the data, and move up on the literacy side. I got IMs [instant messages] from somebody who just doesn&#x27;t understand our data, and I was just talking her through it for her purposes. Now that I think back on it, I was kind of providing the narrative for her. She was trying to figure out how to do something, and I told her that, &quot;We only do business with these customers, but our service center might do business with these customers.&quot; So I was kind of giving her that narrative.The narrative is helpful if they [leadership] want to understand what&#x27;s being told to them. For example, &quot;These are these are our sales, but it doesn&#x27;t include something anyone would not include . . .,&quot; you know, &quot;something that would not normally be included in sales.&quot; I think that if I was presenting data to leadership who aren&#x27;t solely dependent on the data the way I am, I would probably explain the data. There&#x27;s always a reason we&#x27;re showing things the way we do. I&#x27;m imagining like I would show a graph, and then the next slide would be almost my disclaimer, &quot;What you&#x27;re seeing includes this, doesn&#x27;t include that for this reason, etc.&quot;</td></tr></table>

Kim and March 1995). Since mastering basic tasks is usually a prerequisite for mastering more complex tasks (Bloom 1956, Anderson and Krathwohl 2000), it seems logical to <sup>fi</sup>rst thoroughly study the effect of narratives on more basic tasks before considering more complex tasks. We were pleased to <sup>fi</sup>nd that narratives did have a substantial effect on surface-level tasks, especially since many prior studies have had to include more complex tasks to <sup>fi</sup>nd differences for their treatment conditions (see, e.g., Khatri et al. 2006).

## 5.3. Implications for Research

Our work fosters a stream of research to assess the bene<sup>fi</sup>ts and limitations of narratives in understanding organizational data to support data management and analytics. We describe several implications for research below. Whereas most of these are described in the context of empowered users, narratives could also be explored for other roles (e.g., IS professionals) and purposes beyond understanding conceptual modeling scripts.

First, helping empowered users to better understand conceptual modeling scripts by providing an additional representation (like narratives) is uncharted terri tory. Prior research has emphasized improving scripts themselves and has scrutinized them through many theoretical lenses and contexts. The typical result was to alter such scripts to make them easier to use and understand. In contrast, our approach was to provide an auxiliary representation. Our approach answers a call for research on multiple representations suggested by Wand and Weber (2002), which has largely been ignored by prior research (Recker et al. 2021). Whereas narratives are used in some IS contexts (e.g., process models; Kuechler and Vaishnavi 2006), they have rarely been used together with data-oriented scripts.

Based on our encouraging results on the use of narratives, we believe that the effectiveness of narratives for scripts warrants further investigation. We scoped our work to the understanding of the relationship construct for empowered users. Moving beyond this scope, one next step for future research would be to explore how narratives should be designed to support the understanding of other conceptual modeling constructs such as entities and their attributes, or even other concepts (e.g., supertype-subtype, aggregation), similar to what was done in Batra et al. (1990). Another next step could be to examine the use of narratives among those with higher levels of IS knowledge or with other task types (Khatri et al. 2006).

Second, additional improvements might be gained through our use of narratives by offering multiple explanations of cardinality constraints. Research has suggested that multiple explanations are usually more effective than one (Sweller and Cooper 1985, Cooper and Sweller 1987, Renkl and Atkinson 2010). Our narrative supplements offered at most one explanation per constraint. Future studies could consider how to use multiple explanations (e.g., three or more) and examine their effect on understanding cardinality constraints. From a design science perspective, an artifact sampling methodology would be apt to test and evaluate multiple design possibilities suggested by this implication or any of the design implications mentioned in this section (Lukyanenko et al. 2016, Lukyanenko et al. 2018).

Third, more research is needed to gain a better understanding of how to optimally combine narratives with conceptual modeling scripts. One concern would be to avoid information overload. In our work, we explained half of the cardinality constraints to avoid confounds with our treatment effect (i.e., narrative explanation). However, as script complexity increases and narratives grow longer, there will most likely be a point where the cognitive burden of narratives might outweigh the cognitive gains; see the <sup>fi</sup>ndings of Burton-Jones et al. (2012). A question that needs to be addressed is, how much content in a narrative is too much? Would a stand-alone one-page ER diagram be superior to a three-page narrative? Another concern would be to facilitate optimal information integration. Prior studies within multimedia learning (Mayer 2005, Mayer 2014) and scripts (Kim et al. 2000, Gemino 2004) have shown that piecing together information from multiple representations is not a straightforward cognitive task. We provided narratives as a separate representation to pair with a script.<sup>9</sup> However, future research should explore optimal ways of combining narratives with scripts in a hybrid representation to avoid information overload and facilitate information integration. The notion of hybrid representations is being explored in some IS research contexts (Jiang and Benbasat 2007, Xiaoyu and Jiang 2018), and methodologies such as eye tracking (Bera et al. 2019) could yield insight into how to integrate different representations.

Last, with the advent of arti<sup>fi</sup>cial intelligence, tools that can automatically generate narratives or conceptual modeling scripts should be explored as well. Some research has already begun to explore how to generate scripts from users taught to write user stories (Gupta et al. 2019b). These tools automatically generate a script to support the underlying technology and respond to the needs of IS professionals (Gupta et al. 2018, Gupta et al. 2019a). However, if these tools would incorporate narratives, then it would allow empowered users to focus on implementing their desired change. Empowered users could write a narrative to describe their domain of interest and allow the software to automatically implement a solution for immediate work. Alternatively, tools could be created to automatically generate narratives from conceptual modeling scripts to explain them for those wanting to use them. In the case of analytics, some tools can generate text from reports or dashboards,<sup>10</sup> and similar initiatives can be undertaken for conceptual modeling scripts based on the dimensions and properties that make narratives understandable.

## 5.4. Implications for Practice

In this paper, we bring attention to the major societal trend whereby “nearly everyone” in the organization is dealing with data management issues. This study has shown how to support empowered users to better understand conceptual modeling scripts. Using narratives allowed empowered users to gain a better understanding of the cardinality constraints depicted in a script without extensive training and practice. These constraints are an important aspect of understanding organizational data (De Simoni et al. 2015) and thereby can support empowered users in data exploration, data understanding, and software development and codevelopment initiatives. We encourage IS professionals to use our research as a guide to create narratives for empowered users in their organizations (recall our illustrative case in Online Appendix B). Based on our research results, we contend that more empowered users would be able to take autonomous initiatives in data management and data analytics with narratives.

There are a variety of means by which narratives can be created. In general, we believe that the task of creating narratives should be the responsibility of IS professionals, such as systems analysts. As the results of our work indicate, the greatest advantage of narratives comes when they are combined with graphical scripts. Therefore, it is reasonable to posit that people with expertise in conceptual modeling should be the ones writing narratives. However, we also suggest for this process to be participatory and completed with the users who can, for example, indicate which parts of scripts are more dif<sup>fi</sup>cult for them and where adding narratives can yield the most effect. Indeed, many organizations realize the critical importance of ensuring that meaningful data are available to decision makers for various purposes and have given this oftenunappreciated charge to administrative and clerical workers (Møller et al. 2020). This process could also be partially automated, as narratives can be inferred from other sources (e.g., requirements speci<sup>fi</sup>cations) using natural language processing and machine learning techniques (Sutskever et al. 2011, Radford et al. 2019). Narratives, however, are different from requirements speci<sup>fi</sup>cations and other common artifacts of systems analysis and design. As we show in our work, narratives typically have four key dimensions that explain their approachability. Creating narratives using properties from the four dimensions of genuine stories (spatial, temporal, mental, and formal and pragmatic) seems to be an especially effective approach to increase understanding of conceptual modeling scripts.

## 6. Conclusion

The aim of this research was to help empowered users gain a better understanding of data-oriented conceptual modeling scripts, and we took the approach of pairing them with narratives (textual representations) designed as a genuine story. We found that narratives complemented conceptual modeling scripts and signi<sup>fi</sup>cantly improved the understanding of the semantics of their cardinality constraints. This effect was robust across a range of conditions, including conceptual modeling grammar familiarity, conceptual modeling script complexity, and multiple measures of understanding. While we call for more research on the use of narratives in IS, we also encourage organizations to begin using this powerful new tool to unlock even more potential in data-driven analyses and actions.

## Acknowledgments

The authors thank the senior editor, associate editor, and the anonymous reviewers for providing very helpful com ments that improved the quality of the paper. The authors are grateful for the feedback provided during an AIS SIG-SAND Symposium and a University of Cincinnati Lindner College of Business Information Systems Research Forum. Last, the authors thank the University of Cincinnati Press for its generosity in supporting our publication via the Open Access Article Fund.

## Endnotes

<sup>1</sup> In this paper, a conceptual modeling script is the representation created as a result of using a conceptual modeling grammar. An example of a conceptual modeling script and a conceptual modeling grammar is an ER diagram created by using the ER model. Prior research has also referred to the script as a model or schema.

<sup>2</sup> See https://www.linkedin.com/pulse/why-you-should-learn-sqlbrewster-knowlton.

<sup>3</sup> See https://www.ibm.com/cloud/blog/ibm-data-catalog-datascientists-productivity.

<sup>4</sup> Cohen (1988) suggests <sub>≥</sub>0.2 <sub>-</sub> small, <sub>≥</sub>0.5 <sub>-</sub> medium, and >0.8 <sub>-</sub> large for effect size interpretation.

<sup>5</sup> For an independent variable with only two levels, a repeatedmeasures ANOVA (comparing all levels) and a paired-sample t-test (comparing two specific levels) are equivalent.

<sup>6</sup> Post hoc analysis suggested no significant difference in performance between the versions of the narrative participants used.

<sup>7</sup> Participants may over-characterize their data literacy (Atir et al. 2015); however, after conversing with the participants, we were able to ensure that they generally align with our empowered user research focus.

<sup>8</sup> See, for example, https://www.pewresearch.org/fact-tank/2018/ 05/02/millennials-stand-out-for-their-technology-use-but-oldergenerations-also-embrace-digital-life/.

<sup>9</sup> Online Appendix K suggests that our participants attempted to use both representations to interpret cardinality constraints and that this combined usage led to a better performance than using either the ER diagram or narrative supplement alone.

<sup>10</sup> Examples include salesforce “Einstein Discovery” stories, and “Quill” or “Lexico” from narrative science.

## References

Abbott HP (2008) The Cambridge Introduction to Narrative, 2nd ed. (Cambridge University Press, Cambridge, UK).

Alexander I, Maiden N (2004a) Scenarios, stories, and use cases: The modern basis for system development. IEEE Comput. Control Engrg. 15(5):24–29.

Alexander I, Maiden N (2004b) Scenarios, Stories, Use Cases: Through the Systems Development Life-Cycle (Wiley, New York).

Allen GN, March ST (2012) A research note on representing partwhole relations in conceptual modeling. MIS Quart. 36(3): 945–964.

Allen SW, Brooks LR (1991) Specializing the operation of an explicit rule. J. Experiment. Psych. General 120(1):3–19.

Anderson LW, Krathwohl DR (2000) A Taxonomy for Learning, Teach ing, and Assessing: A Revision of Bloom’s Taxonomy of Educational Objectives, abridged 2nd ed. (Allyn & Bacon, Boston).

Angwin DN, Cummings S, Daellenbach U (2019) How the multimedia communication of strategy can enable more effective recall and learning. Acad. Management Learning Ed. 18(4):527–546.

Arlow J, Emmerich W, Quinn J (1998) Literate modelling—capturing business knowledge with the UML. Bezivin J, Muller P-A,´ eds. The Unified Modeling Language. UML ’98: Beyond the Nota tion (Springer, Berlin), 189–199.

Aspray W, Campbell-Kelly M (1996) Computer: A History of the Infor mation Machine, 1st ed. (Basic Books, New York).

Atir S, Rosenzweig E, Dunning D (2015) When knowledge knows no bounds: Self-perceived expertise predicts claims of impossible knowledge. Psych. Sci. 26(8):1295–1303.

Atkinson RK, Derry SJ, Renkl A, Wortham D (2000) Learning from examples: Instructional principles from the worked examples research. Rev. Educ. Res. 70(2):181–214.

Bachman CW, Daya M (1977) The role concept in data models Housel BC, Merten AG, eds. Proc. Third Internat. Conf. Ver Large Data Bases, vol. 3 (VLDB Endowment), 464–476.

Batra D, Hoffer JA, Bostrom RP (1990) Comparing representations with relational and EER models. Comm. ACM 33(2):126–139.

Benyon D, Macaulay C (2004) A scenario-based design method for human-centred interaction design. Alexander I, Maiden N, eds. Scenarios, Stories, Use Cases: Through the Systems Development Life-Cycle (Wiley, New York), 211–235.

Bera P, Burton-Jones A, Wand Y (2014) How semantics and pragmatics interact in understanding conceptual models. Inform Systems Res. 25(2):401–419.

Bera P, Soffer P, Parsons J (2019) Using eye tracking to expose cognitive processes in understanding conceptual models. MIS Quart. 43(4):1105–1126.

Bergen BK (2012) Louder Than Words: The New Science of How the Mind Makes Meaning (Basic Books, New York).

Bloom BS (1956) Taxonomy of Educational Objectives. Handbook 1: The Cognitive Domain (McKay, New York).

Bodart F, Patel A, Sim M, Weber R (2001) Should optional properties be used in conceptual modeling? A theory and three empir ical tests. Inform. Systems Res. 12(4):384–405.

Browne GJ, Parsons J (2012) More enduring questions in cognitive IS research. J. Assoc. Inform. Systems 13(12):1000–1011.

Bubenko JA (1979) On the role of ‘understanding models’ in conceptual schema design. Furtado AL, Morgan HL, eds. Proc. Fifth Internat. Conf. Very Large Data Bases (VLDB Endowment), 129–139.

Buhler C (2001) Empowered participation of users with disabil-¨ ities in R&D projects. Internat. J. Human Comput. Stud. 55(4): 645–659.

Burton-Jones A, Meso PN (2008) The effects of decomposition qual ity and multiple forms of information on users’ understanding of a domain. J. Assoc. Inform. Systems 9(12):2.

Burton-Jones A, Weber R (2014) Building conceptual modeling on the foundation of ontology. Topi H, Tucker A, eds. Computing Handbook: Information Systems and Information Technology (CRC Press, Boca Raton, FL), 316–339.

Burton-Jones A, Clarke R, Lazarenko K, Weber R (2012) Is use of optional attributes and associations in conceptual modeling always problematic? Theory and empirical tests. ICIS 2012 Proc., vol. 4. https://aisel.aisnet.org/icis2012/proceedings/ HumanComputerInteractions/4.

Castellanos A, Tremblay MC, Lukyanenko R, Samuel B (2020) Basic classes in conceptual modeling: Theory and practical guidelines. J. Assoc. Inform. Systems 21(4):1001–1044.

Chen PP-S (1976) The entity-relationship model—Toward a uni<sup>fi</sup>ed view of data. ACM Trans. Database Systems 1(1):9–36.

Cockburn A (2000) Writing Effective Use Cases, 1st ed. (Addison-Wesley, Boston).

Cohen J (1988) Statistical Power Analysis for the Behavioral Sciences, 2nd ed. (Erlbaum Associates, Hillsdale, NJ).

Compeau D, Marcolin B, Kelley H, Higgins C (2012) Generalizability of information systems research using student subjects— A re<sup>fl</sup>ection on our practices and recommendations for future research. Inform. Systems Res. 23(4):1093–1109.

Cooper G, Sweller J (1987) Effects of schema acquisition and rule automation on mathematical problem-solving transfer. J. Ed. Psych. 79(4):347–362.

Currim F, Ram S (2012) Modeling spatial and temporal set-based constraints during conceptual database design. Inform. Systems Res. 23(1):109–128.

Damasio AR (2010) Self Comes to Mind: Constructing the Conscious Brain (Pantheon, New York).

Dansereau DF, Simpson DD (2009) A picture is worth a thousand words: The case for graphic representations. Professional Psych. Res. Practice 40(1):104–110.

Davenport TH, Harris JG, Morison R (2010) Analytics at Work: Smarter Decisions, Better Results (Harvard Business Press, Boston).

Davies I, Green P, Rosemann M, Indulska M, Gallo S (2006) How do practitioners use conceptual modeling in practice? Data Knowledge Engrg. 58(3):358–380.

Day SB, Goldstone RL (2012) The import of knowledge export: Connecting <sup>fi</sup>ndings and theories of transfer of learning. Ed. Psych. 47(3):153–176.

De Simoni G (2021) Metadata is the <sup>fi</sup>sh <sup>fi</sup>nder in data lakes. Report, Gartner Research, https://www.gartner.com/en/documents/ 3996684.

De Simoni G, Judah S, Zaidi E (2015) Market guide for metadata management solutions. Gartner Research, https://www.gartner. com/en/documents/3092921.

Dunn CL, Gerard GJ, Grabski SV (2011) Diagrammatic attention management and the effect of conceptual model structure on cardinality validation. J. Assoc. Inform. Systems 12(8):585–605.

Edjlali R, Sicular S (2017) Four data management best practices for AI. Report, Gartner Research, https://www.gartner.com/en/ documents/3787064.

Elmasri R, Navathe S (2010) Fundamentals of Database Systems, 6th ed. (Addison-Wesley, Boston).

Eppler MJ, Mengis J (2004) The concept of information overload: A review of literature from organization science, accounting, marketing, MIS, and related disciplines. Inform. Soc. 20(5):325–344.

Ericsson KA, Charness N, Feltovich PJ, Hoffman DL (2006) The Cambridge Handbook of Expertise and Expert Performance (Cambridg University Press, New York).

Eriksson O, Agerfalk PJ (2021) Speaking things into existence: Ontological foundations of identity representation and management. Inform. Systems J. 32(1):33–60.

Eriksson O, Johannesson P, Bergholtz M (2019) The case for classes and instances—A response to representing instances: The case for reengineering conceptual modelling grammars. Eur. J. Inform. Systems 28(6):681–693.

Eysenck MW (1991) Working memory. Eysenck MW, ed. The Blackwell Dictionary of Cognitive Psychology (Blackwell, Malden, MA), 372–375.

Fettke P (2009) How conceptual modeling is used. Comm. Assoc. Inform. Syst. 25:43.

Gemino A (2004) Empirical comparisons of animation and narration in requirements validation. Requirements Engrg. 9(3):153–168.

Gemino A, Parker D (2009) Use case diagrams in support of use case modeling: Deriving understanding from the picture. J. Database Management 20(1):1–24.

Gemino A, Wand Y (2005) Complexity and clarity in conceptual modeling: Comparison of mandatory and optional properties. Data Knowledge Engrg. 55(3):301–326.

Gibson CF, Nolan RL (1973) Organizing and managing computer personnel: Conceptual approaches for the MIS manager. Proc. 11th Annual SIGCPS Comput. Personnel Res. Conf. (ACM, New York), 19–45.

Graves A, Hendler J (2013) Visualization tools for open government data. Proc. 14th Annual Internat. Conf. Digital Governmen Res. (ACM, New York), 136–145.

Gupta A, Poels G, Bera P (2018) A proposal of using conceptual models for user story development and maintenance. 17th AIS SIGSAND Sympos., Syracuse, NY, May 24–25.

Gupta A, Poels G, Bera P (2019a) An algorithm to create multiple conceptual models from user stories. 18th AIS SIGSAND Sympos., New York, June 1–2.

Gupta A, Poels G, Bera P (2019b) Creation of Multiple Conceptual Models from User Stories—a Natural Language Processing Approach (Springer, Cham, Switzerland), 47–57.

Gustavsson R, Sta˚hl B (2010) The empowered user—The critical interface to critical infrastructures. 2010 Fifth Internat. Conf. Crit ical Infrastructure (CRIS) (IEEE, Piscataway, NJ), 1–3.

He X, Zhao K, Chu X (2021) AutoML: A survey of the state-of-the art. Knowledge-Based Systems 212:106622.

Hirschheim R, Klein HK (2012) A glorious and not-so-short history of the information systems <sup>fi</sup>eld. J. Assoc. Inform. Systems 13(4): 188–235.

Hirschheim R, Klein HK, Lyytinen K (1995) Information Systems Development and Data Modeling: Conceptual and Philosophical Foundations (Cambridge University Press, Cambridge, UK).

Howson C (2013) Successful Business Intelligence: Unlock the Value of BI and Big Data (McGraw-Hill, New York).

Hvalshagen M (2011) Harnessing the power of narratives to understand user requirements. Unpublished doctoral dissertation, Kelley School of Business, Indiana University.

Jabbari Sabegh MA, Recker J, Green P, Werder K (2019) How do individuals understand multiple conceptual modeling scripts? J. Assoc. Inform. Systems 20(8):2.

Jiang Z, Benbasat I (2007) The effects of presentation formats and task complexity on online consumers’ product understanding. MIS Quart. 31(3):475–500.

Junglas I, Goel L, Ives B, Harris J (2014) Consumer IT at work: Development and test of an IT empowerment model. Proc. 35th Internat. Conf. Inform. Systems, Auckland, New Zealand, December 14–17.

Kahneman D (2011) Thinking, Fast and Slow (Farrar, Straus and Giroux, New York).

Kalyuga S (2009) Knowledge elaboration: A cognitive load perspective. Learning Instruction 19(5):402–410.

Kalyuga S (2010) Schema acquisition and sources of cognitive load. Plass JL, Moreno R, Brunken R, eds.¨ Cognitive Load Theory (Cam bridge University Press, Cambridge, UK), 48–64.

Khatri V, Ramesh V, Vessey I, Clay P (2006) Comprehension of conceptual schemas: Exploring the role of application and is domain knowledge. Inform. Systems Res. 17(1):81–99.

Khatri V, Samuel BM (2019) Analytics for managerial work. Comm. ACM 62(4):100–100.

Kim Y-G, March ST (1995) Comparing data modeling formalism. Comm. ACM 38(6):103–115.

Kim J, Hahn J, Hahn H (2000) How do we understand a system with (so) many diagrams? Cognitive integration processes in diagrammatic reasoning. Inform. Systems Res. 11(3):284–303.

Kuechler WL, Vaishnavi V (2006) So, talk to me: The effect of explicit goals on the comprehension of business process narratives. MIS Quart. 30(4):961–979.

Larsen KR, Becker DS (2021) Automated Machine Learning for Business (Oxford University Press, New York).

Lee AS, Baskerville RL (2012) Conceptualizing generalizability: New contributions and a reply. MIS Quart. 36(3):749–761.

Legner C, Eymann T, Hess T, Matt C, Bohmann T, Drews P,¨ Madche A, Urbach N, Ahlemann F (2017) Digitalization:¨ Opportunity and challenge for the business and information systems engineering community. Bus. Inform. Systems Engrg. 59(4):301–308.

Lukyanenko R, Parsons J, Samuel B (2018) Artifact sampling: Using multiple information technology artifacts to increase research rigor. Proc. 51st Hawaii Internat. Conf. System Sci., Big Island, HI, January 2–6, 235–244.

Lukyanenko R, Parsons J, Samuel B (2019a) Representing instances: The case for reengineering conceptual modelling grammars. Eur. J. Inform. Systems 28(1):68–90.

Lukyanenko R, Samuel BM, Evermann J, Parsons J (2016) Toward artifact sampling in IS design research. Workshop Inform. Tech. Systems, Dublin, Ireland, December 15–16.

Lukyanenko R, Castellanos A, Parsons J, Chiarini Tremblay M, Storey VC (2019b) Using conceptual modeling to support machine learning. Cappiello C, Ruiz M, eds. Information Systems Engineering in Responsible Information Systems (Springer, Cham, Switzerland), 170–181.

Malinova M, Mendling J (2021) Cognitive diagram understanding and task performance in systems analysis and design. MIS Quart. 45(4):2101–2158.

Mayer RE, ed. (2005) The Cambridge Handbook of Multimedia Learning, 1st ed. (Cambridge University Press, Cambridge, UK).

Mayer RE (2014) Cognitive theory of multimedia learning. Mayer RE, ed. The Cambridge Handbook of Multimedia Learning, 2nd ed. (Cambridge University Press, Cambridge, UK), 43–71.

Mayr HC, Thalheim B (2021) The triptych of conceptual modeling. Software Systems Modeling 20(1):7–24.

McNamara DS, Scott JL (2001) Working memory capacity and strat egy use. Memory Cognition 29(1):10–17.

Meulen Rd, Pettey C (2018) Gartner says self-service analytics and BI users will produce more analysis than data scientists will by 2019. Press release, Gartner Research, January 25, https://www. gartner.com/en/newsroom/press-releases/2018-01-25-gartnersays-self-service-analytics-and-bi-users-will-produce-moreanalysis-than-data-scientists-will-by-2019.

Møller NH, Bossen C, Pine KH, Nielsen TR, Neff G (2020) Who does the work of data? Interaction 27(3):52–55.

Moody D (2009) The “physics” of notations: Toward a scienti<sup>fi</sup>c basis for constructing visual notations in software engineering. IEEE Trans. Software Engrg. 35(6):756–779.

Nathan MJ (2012) Rethinking formalisms in formal education. Ed Psych. 47(2):125–148.

Newman J, Vidler E (2006) Discriminating customers, responsible patients, empowered users: Consumerism and the modernisation of health care. J. Soc. Policy 35(2):193–209.

Niehaves B, Koffer S, Ortbach K (2012) IT consumerization¨ —A theory and practice review. Proc. AMCIS 2012, Seattle, August 9–12.

O’Reilly CA (1980) Individuals and information overload in organizations: Is more necessarily better? Acad. Management J. 23(4): 684–696.

Olive A (2007)´ Conceptual Modeling of Information Systems (Springer, Berlin).

Ottensooser A, Fekete A, Reijers HA, Mendling J, Menictas C (2012) Making sense of business process descriptions: An experimental comparison of graphical and textual notations. J. Systems Software 85(3):596–606.

Paas F, van Gog T (2006) Optimizing worked example instruction: Different ways to increase germane cognitive load. Learning Instruction 16(2):87–91.

Paas F, Van Merrienboer JJ (1994) Instructional control of cognitive¨ load in the training of complex cognitive tasks. Ed. Psych. Rev. 6(4):351–371.

Paas F, Renkl A, Sweller J (2003) Cognitive load theory and instructional design: Recent developments. Ed. Psych. 38(1):1–4.

Pilone D, Pitman N (2005) UML 2.0 in a Nutshell, 2nd ed. (O'Reilly, Sebastopol, CA).

Radford A, Wu J, Child R, Luan D, Amodei D, Sutskever I (2019) Language models are unsupervised multitask learners. OpenAI Blog (February 14), https://openai.com/blog/better-languagemodels/.

Ram S, Khatri V (2005) A comprehensive framework for modeling set-based business rules during conceptual database design. Inform. Systems 30(2):89–118.

Recker J, Green P (2019) How do individuals interpret multiple conceptual models? A theory of combined ontological complete ness and overlap. J. Assoc. Inform. Systems 20(8):1.

Recker J, Rosemann M, Green P, Indulska M (2011) Do ontological de<sup>fi</sup>ciencies in modeling grammars matter? MIS Quart. 35(1): 57–79.

Recker J, Lukyanenko R, Jabbari M, Samuel BM, Castellanos A (2021) From representation to mediation: A new agenda for conceptual modeling research in a digital world. MIS Quart. 45(1):269–300.

Renkl A (2005) The worked-out-example principle in multimedia learning. Mayer RE, ed. The Cambridge Handbook of Multimedia Learning, 1st ed. (Cambridge University Press, Cambridge, UK), 229–245.

Renkl A, Atkinson RK (2010) Learning from worked-out examples and problem solving. Plass JL, Moreno R, Brunken R, eds.¨ Cognitive Load Theory (Cambridge University Press, Cambridge, UK), 91–108.

Renkl A, Hilbertm T, Schworm S (2009) Example-based learning in heuristic domains: A cognitive load theory account. Ed. Psych. Rev. 21(1):67–78.

Roger EK, Kirk A (1968) Experimental Design: Procedures for the Behavioral Sciences (Brooks/Cole, Belmont, CA).

Romero S, Fernandez-Feijoo B, Ruiz S (2014) Perceptions of quality of assurance statements for sustainability reports. Soc. Responsibility J. 10(3):480–499.

Rosemann M, Vessey I (2008) Toward improving the relevance of information systems research to practice: The role of applicabil ity checks. MIS Quart. 32(1):1–22.

Roussopoulos N, Mylopoulos J (1989) Using semantic networks for data base management. Mylopolous J, Brodie M, eds. Readings in Artificial Intelligence and Databases (Elsevier, Amsterdam), 112–137.

Ryan M-L (2007) Toward a de<sup>fi</sup>nition of narrative. Herman D, ed. The Cambridge Companion to Narrative (Cambridge University Press, Cambridge, UK), 22–35.

Sagha<sup>fi</sup> A, Wand Y, Parsons J (2021) Skipping class: Improving human-driven data exploration and querying through instances. Eur. J. Inform. Systems, ePub ahead of print January 29, https://doi.org/10.1080/0960085X.2020.1869507.

Samuel BM, Khatri V, Ramesh V (2018) Exploring the effects of extensional versus intentional representations on domain understand ing. MIS Quart. 42(4):1187–1209.

Schank RC, Abelson RP (1995) Knowledge and memory: The real story. Wyer RS, ed. Knowledge and Memory: The Real Story (Lawrence Erlbaum Associates, Hillsdale, NJ), 1–85.

Shanks G, Tansley E, Nuredini J, Tobin D, Weber R (2008) Represent ing part–whole relations in conceptual modeling: An empirical evaluation. MIS Quart. 32(3):553–573.

Sharma S, Patil K (2017) Past, Present and Future of Collaborative Design: From User Centric to User Driven Design (Springer, Singapore), 1025–1036.

Shoval P, Frumermann I (1994) OO and EER conceptual schemas: A comparison of user comprehension. J. Database Management 5(4):28–38.

Sutskever I, Martens J, Hinton GE (2011) Generating text with recurrent neural networks. Proc. 28th Internat. Conf. Machine Learning (ICML-11), Bellevue, Washington, June 28–July 2, 1017–1024.

Sweller J (1994) Cognitive load theory, learning dif<sup>fi</sup>culty, and instructional design. Learning Instruction 4(4):295–312.

Sweller J (2006) The worked example effect and human cognition Learning Instruction 16(2):165–169.

Sweller J (2010) Cognitive load theory: Recent theoretical advances. Plass JL, Moreno R, Brunken R, eds. ¨ Cognitive Load Theor (Cambridge University Press, Cambridge, UK), 29–47.

Sweller J, Cooper GA (1985) The use of worked examples as a substitute for problem solving in learning algebra. Cognition Instruction 2(1):59–89.

Tabachnick B, Fidell L (2000) Computer-Assisted Research Design and Analysis, 1st ed. (Pearson, New York).

Tarca A, Hancock P, Woodliff D, Brown P, Bradbury M, Van Zijl T (2008) Identifying decision useful information with the matrix format income statement. J. Internat. Financial Management Accounting 19(2):184–217.

Thalheim B (1992) Fundamentals of Cardinality Constraints. Pernu G, Tjoa AM, eds. Entity-Relationship Approach—ER ’92 (Springer, Berlin), 7–23

The Economist (2022) What if all workers wrote software, not just th geek elite? (January 29), https://www.economist.com/business/ 2022/01/29/what-if-all-workers-wrote-software-not-just-the geek-elite.

Topi H, Ramesh V (2002) Human factors research on data modeling: A review of prior research, an extended framework and future research directions. J. Database Manage ment 13(2):3–19.

van den Broek P (2010) Using texts in science education: Cognitive processes and knowledge representation. Science 328(5977): 453–456.

van Merrienboer JJG, Sweller J (2005) Cognitive load theory and¨ complex learning: Recent developments and future directions. Ed. Psych. Rev. 17(2):147–177.

Wand Y, Weber R (2002) Information systems and conceptual modeling—A research agenda. Inform. Systems Res. 13(4): 363–376.

Wand Y, Storey VC, Weber R (1999) An ontology analysis of th relationship construct in conceptual modeling. ACM Trans Database Systems 24(4):494–528.

Wand Y, Monarchi DE, Parson J, Woo CC (1995) Theoretical foundations for conceptual modeling in information systems devel opment. Decision Support Systems 15(4):285–304.

Xiaoyu M, Jiang Z (2018) The magic of cinemagraphs: Investigation of different image formats in online product presentation. Proc. 39th Internat. Conf. Inform. Systems, San Francisco, December 13–16, 1–9.

Zuboff S (1988) In the Age of the Smart Machine: The Future of Work and Power (Basic, New York).

C<sub>opy</sub>ri<sub>g</sub>ht 2023 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
