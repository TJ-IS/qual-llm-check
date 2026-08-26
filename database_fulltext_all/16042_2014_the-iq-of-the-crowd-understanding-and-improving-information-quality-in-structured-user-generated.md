---
otero_id: 16042
otero_key: "RFFB23MC"
title: "The IQ of the Crowd: Understanding and Improving Information Quality in Structured User-Generated Content"
authors: "Roman Lukyanenko; Jeffrey Parsons; Yolanda F. Wiersma"
year: "2014"
journal: "Information Systems Research"
doi: "10.1287/isre.2014.0537"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/RFFB23MC/fulltext/images/8000d843d6b240613af6c9a4d4661b3961e64e54884634c9abda97820d038cfd.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# The IQ of the Crowd: Understanding and Improving Information Quality in Structured User-Generated Content

Roman Lukyanenko, Jeffrey Parsons, Yolanda F. Wiersma

Roman Lukyanenko, Jeffrey Parsons, Yolanda F. Wiersma (2014) The IQ of the Crowd: Understanding and Improving Information Quality in Structured User-Generated Content. Information Systems Research 25(4):669-689. http:// dx.doi.org/10.1287/isre.2014.0537

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2014, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/RFFB23MC/fulltext/images/742181e1d67e0e1e22cf4007dc2417868ddf99e384958ff087eb2e1a6b415c4a.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# The IQ of the Crowd: Understanding and Improving Information Quality in Structured User-Generated Content

Roman Lukyanenko College of Business, Florida International University, Miami, Florida 33199, roman.lukyanenko@fiu.edu

Jeffrey Parsons

Faculty of Business Administration, Memorial University of Newfoundland, St. John’s, Newfoundland A1B 3X5 Canada, jeffreyp@mun.ca

Yolanda F. Wiersma

Department of Biology, Memorial University of Newfoundland, St. John’s, Newfoundland A1B 3X5 Canada, ywiersma@mun.ca

ser-generated content (UGC) is becoming a valuable organizational resource, as it is seen in many cases as a way to make more information available for analysis. To make effective use of UGC, it is necessary to understand information quality (IQ) in this setting. Traditional IQ research focuses on corporate data and views users as data consumers. However, as users with varying levels of expertise contribute information in an open setting, current conceptualizations of IQ break down. In particular, the practice of modeling information requirements in terms of fixed classes, such as an Entity-Relationship diagram or relational database tables, unnecessarily restricts the IQ of user-generated data sets. This paper defines crowd information quality (crowd IQ), empirically examines implications of class-based modeling approaches for crowd IQ, and offers a path for improving crowd IQ using instance-and-attribute based modeling. To evaluate the impact of modeling decisions on IQ, we conducted three experiments. Results demonstrate that information accuracy depends on the classes used to model domains, with participants providing more accurate information when classifying phenomena at a more general level. In addition, we found greater overall accuracy when participants could provide freeform data compared to a condition in which they selected from constrained choices. We further demonstrate that, relative to attribute-based data collection, information loss occurs when class-based models are used. Our findings have significant implications for information quality, information modeling, and UGC research and practice.

Keywords: systems design and implementation; laboratory experiments; information quality; conceptual modeling; crowdsourcing; social media; citizen science; user-generated content

History: Joey George, Senior Editor; Andrew Burton-Jones, Associate Editor. This paper was received May 4, 2012, and was with the authors 14 months for 4 revisions. Published online in Articles in Advance October 13, 2014.

## Introduction

Information systems (IS) were traditionally considered as conceived, designed, implemented, and used primarily within an organization for well defined purposes determined during systems development (e.g., Mason and Mitroff 1973). This organizational focus enabled control over mechanisms to collect, store, and use data. The growth of interorganizational systems challenged this view to some degree, as it became necessary to standardize methods for information exchange between independent systems in different organizations (Choudhury 1997, Markus et al. 2006, Vitale and Johnson 1988, Zhu and Wu 2011). Recently, the proliferation of social media (Susarla et al. 2012) and crowdsourcing (engaging online users to work on specific tasks, see Doan et al. 2011) has further changed the IS landscape. There is growing interest in user-generated content (UGC) (Cha et al. 2007, Daugherty et al. 2008, Krumm et al. 2008), defined here as various forms of digital information (e.g., comments, forum posts, tags, product reviews, videos, maps) produced by members of the general public. These are often casual content contributors (i.e., the crowd) rather than employees or others closely associated with an organization. UGC increasingly supports decision making and analysis in many contexts, including business applications (Gallaugher and Ransbotham 2010, Gangi et al. 2010), e-commerce (Zwass 2010), stock markets (Hill and Ready-Campbell 2011), navigation and mapping systems (Goodchild 2007, Haklay 2010), emergency management (Majchrzak and More 2011), scientific research (Hand 2010), healthcare (Gao et al. 2010), and politics (Wattal et al. 2010). Significantly, in these settings information collected for one purpose may be used for other purposes not recognized at the time a system was developed. For example, many projects that harness UGC for scientific purposes are initiated without prespecified hypotheses (Wiersma 2010). In general, there is a growing trend to mine UGC for unanticipated insights (Crooks et al. 2013, Nelson and Fijn 2013).

Despite its pervasiveness, UGC holds potential risks. First, by opening participation to the crowd, it is more difficult to control the content or form of data supplied. Casual users often lack domain expertise, have little stake in the success of projects, and cannot be held accountable for the quality of data they contribute (Coleman et al. 2009). Second, in a crowd environment casual participants may lack incentives to contribute and may be dissuaded if the process of making contributions is difficult. For example, if an interface requires that data be recorded at a level of specificity that a casual contributor cannot easily provide, potential contributions might be lost. Third, different contributors have different perceptions of what is relevant and interesting for a particular observation. If the system is not flexible enough to allow unanticipated data to be systematically captured, potentially useful information might be lost. Thus, an important challenge in making effective use of UGC is crowd information quality<sup>1</sup> or (crowd IQ), i.e., the quality of information contributed by Internet users (Arazy et al. 2011, Flanagin and Metzger 2008, Hochachka et al. 2012, Mackechnie et al. 2011, Rowland 2012, Wiggins et al. 2011). Perceived or actual low quality UGC can severely curtail its value in decision making.

In response to the growing interest in UGC, two perspectives on how to better understand and improve crowd IQ have emerged. Consistent with broader IQ research, the prevailing approach is fitness for use, which focuses on the organization, qualifications, and expertise of contributors so as to better align information capture with needs of data consumers. This approach assumes that potential uses of information are known and stable. In contrast, some authors (e.g., Parsons et al. 2011) recently advocate a contributor-oriented perspective that examines ways to design IS to better capture observations of information providers. Such an approach makes limited assumptions about how the information will be used in evaluating IQ, thus allowing for emerging unanticipated uses.

In this research, we examine the effect of a largely ignored, but important, factor influencing IQ in UGC: conceptual modeling. Conceptual modeling and IQ management have traditionally been seen as distinct activities. Conceptual modeling represents knowledge about a domain, often deliberately abstracting from implementation concerns (Mylopoulos 1998, Olivé 2007, Wand and Weber 2002). By comparison, IQ research has emphasized the needs of data consumers and their experiences with IQ. These experiences can be characterized using dimensions such as consistency, timeliness, believability, accessibility, security, completeness, value-added, ease of manipulation, and freedom from error (accuracy) (Wang and Strong 1996). IQ research also addresses issues of definition, measurement, analysis, and IQ improvement that arise during the collection, storage, and use of information, as experienced by various stakeholders, each with their own purposes and information requirements (Lee et al. 2006, Pipino et al. 2002, Tayi and Ballou 1998, Wang and Strong 1996).

Some recent studies suggest that the intersection of modeling and crowd IQ warrants attention. Girres and Touya (2010) note the importance of the data model used by the OpenStreetMap project, and argue for a better balance between contributor freedom and compliance with specifications. Parsons et al. (2011) identify an inverse relationship between IQ and level of participation in crowdsourcing projects, and suggest that this trade-off can be avoided by changing the way information is collected and stored.

Our research aims to increase understanding of the impact of conceptual modeling on IQ in the context of UGC. We argue that the IQ of structured user contributions can be influenced positively or negatively by conceptual modeling decisions. In particular, we show that the dominant approach, in which data are conceived and recorded in terms of classes (e.g., phenomena are assigned to classes such as product type, biological species, or landscape form), can have a significant negative impact on IQ when the classes provided by a system based on the needs of data consumers are not familiar to data contributors (or when unanticipated uses of information arise after a system has been developed). Once defined, classes constrain the degree to which an information system reflects users’ views of reality. Relaxing the rigid constraints of class-based models can help capture user input more objectively and completely, leading to higher quality of stored data while simultaneously mitigating the constraints on participation arising from insufficient expertise and differences in domain conceptualizations among online users. It can also fuel scientific discovery by creating an environment that facilitates the identification of previously unknown classes of phenomena.

The remainder of the paper is organized as follows. The next section provides a theoretical foundation for crowd IQ and derives propositions about the impact of conceptual modeling on important IQ dimensions. We then present three experiments that test hypotheses derived from these propositions. The paper concludes by outlining an approach to resolving IQ problems arising from the use of traditional class-based conceptual models and discussing implications of our work for future research and practice.

## Theoretical Foundations and Research Propositions

## Defining Crowd IQ

A core principle of IS analysis and design is userdriven development, according to which user requirements are captured during systems analysis and reflected to the extent possible in the design of the resulting information system (Checkland and Holwell 1997, Hirschheim et al. 1995). This user-oriented view is reflected in seminal definitions of information quality: the prevailing conceptualization of IQ is fitness for use of data by information consumers for specific purposes (Lee 2003, Lee et al. 2004, Wang and Strong 1996, Zhu and Wu 2011). This focus underlies another popular IQ definition, i.e., “conformance to specification and as exceeding consumer expectations” (Kahn et al. 2002, p. 184). Both definitions focus IQ improvement on ways to shape the “information product” (Ballou and Pazer 1985, Wang 1998) to better satisfy data consumers’ needs and are concomitant with conceptions of quality in marketing and management science (Juran and Gryna 1988, Reeves and Bednar 1994).

However, important differences between traditional organizational settings and crowdsourcing applications require extending the prevailing data consumer focus of IQ definitions. Consumer-centric definitions ignore the characteristics of crowd (volitional) information creation and do not reflect the information contributor’s perspective. Crowdsourcing projects are often designed at the request of project sponsors, i.e., those who allocate resources (e.g., financial, management, and technical) to the project and evaluate its success in serving the needs of (potential) data consumers. However, ordinary people are the key information contributors and the main drivers of success in these projects. The abilities, motivation, and domain knowledge of contributors in crowdsourcing can have a strong impact on the level of engagement and quality of contributions (Coleman et al. 2009, Hand 2010, Nov et al. 2011, Parsons et al. 2011). Furthermore, contributors to crowdsourcing projects may be neither aware of the intended use of contributed data nor motivated to fully satisfy (or exceed) expectations of data consumers. Overemphasizing the data consumer’s perspective in systems designed to harness UGC may preclude contributors from accurately and fully describing the phenomena about which they are contributing data. In cases where the data consumer’s information needs are incongruent with what a user can provide, potential contributors may simply abandon data entry. Often contributors provide what they can (or are willing to), not necessarily what is required. Such information, if properly captured, could be useful for purposes not anticipated when a project was designed. To be effective, information systems in crowdsourcing settings should be sensitive to information contributors’ capabilities, as well as to data consumers’ requirements.

We therefore propose a definition of crowd IQ that amends the traditional definition of information quality to account for the issues and challenges of the emerging area of UGC. Specifically, we define crowd Information Quality 4crowd IQ5 as the extent to which stored information represents the phenomena of interest to data consumers 4and project sponsors5, as perceived by information contributors. This definition explicitly excludes fitness for use. Rather, it is use-agnostic, recognizing that “the phenomena 0 0 0 as perceived by information contributors” accommodates both known uses and future, unanticipated uses. With this definition we hope to guide research aimed at improving the quality of crowdsourced data. By addressing consumer needs, we advocate making IQ improvements that lead to desirable and useful outcomes for consumers. At the same time, the definition recognizes the pivotal role of information contributors and motivates an effort to design systems sensitive to their points of view.

## Approaches to Improving Crowd IQ

Fitness for use underlies a number of approaches to improving crowd IQ that work with contributors to improve adherence of contributions to predefined standards. These include collaborative or peer review, role-based constraints on contribution, and user training. Collaboration is the basis for iSpot (http://www .ispotnature.org), a project that uses social networking for collaborative identification of species of plants and animals (Silvertown 2010), and is also at the heart of Wikipedia (Arazy et al. 2011). While collaborative review is promising, it is appropriate only for popular content in projects with many users; even in larger projects, less popular content may escape peer scrutiny (Cha et al. 2007).

Organizational structures to manage IQ constrain contributions by the organizational roles of their authors. The basic assumption underlying this approach is that users in different roles (e.g., moderator versus rookie member) tend to produce information that differs in quality. For example, to edit certain content of Wikipedia, one needs to have moderating or administrative privileges. However, this approach creates what Kittur et al. (2007) call the online “elite” or “bourgeoisie,” a few privileged users who control the collaborative enterprise. In extreme cases, this may lead to information censorship.

Project sponsors use training to improve IQ when there are established standards to which contributions should adhere (Dickinson et al. 2010, Foster-Smith and Evans 2003). For example, in Galaxy Zoo (http://www.galaxyzoo.org) data contributors are required to take a tutorial and pass a test before they are allowed to classify galaxies (Fortson et al. 2012). However, training can sometimes introduce biases (Galloway et al. 2006), and may not be realistic for casual contributors.

To our knowledge, unlike IQ management based on fitness for use, contributor-focused IQ management, emphasizing information capture and storage, has been neglected. We next examine a novel contributororiented perspective on IQ by considering how conceptual modeling decisions can affect the quality of UGC.

## Conceptual Modeling Foundations

Conceptual modeling has been defined as “the activity of formally describing some aspects of the physical and social world around us for the purposes of understanding and communication” (Mylopoulos 1992, p. 51). As conceptual modeling involves representing the world as understood by humans (Hirschheim et al. 1995, Wand et al. 1995), at least two theoretical foundations have been shown to be appropriate for understanding conceptual modeling: ontology and cognition.

Ontology, the philosophical study of what exists, has been used as a theoretical foundation of conceptual modeling to prescribe modeling constructs and evaluate the fidelity with which models represent reality (Guizzardi 2010, Wand et al. 1995, Wand and Weber 2002). Bunge’s (1977) ontology has been popular in conceptual modeling research as it maps well to IS constructs (Wand and Weber 1990) and explains and predicts a variety of information systems phenomena (Burton-Jones and Meso 2006, Gemino and Wand 2005, Recker et al. 2011, Shanks et al. 2008, Weber 1996).<sup>2</sup> It has also been used to theoretically derive data quality dimensions (Wand and Wang 1996).

As human understanding of the real world is moderated by cognitive processes, we augment ontology with theories of cognition. In particular, classification theory “attempts to explain the nature of concepts (categories/classes) and why humans classify” phenomena (Parsons 1996, p. 1438). Significantly, prominent conceptual modeling grammars, such as the Entity-Relationship (ER) model and Unified Modeling Language (UML) Class Diagrams, rely on class constructs (e.g., ER entity types, UML classes). Based on these foundations, we evaluate prevailing approaches to conceptual modeling and examine the potential impact of conceptual modeling on IQ.

According to Bunge, the world is made of “things” (individuals or entities). Every thing possesses properties; properties do not exist independent of things. People are unable to directly observe properties, and see them instead as attributes. Properties of things may change over time.

Things possessing common properties can be grouped together to form kinds (which are similar to classes). Unlike material things, classes (kinds) are derived constructs existing only in human minds (Parsons and Wand 2008). According to cognitive theories, classes provide cognitive economy and inference, enabling humans to efficiently store and retrieve information about phenomena of interest (instances) (Parsons 1996, Posner 1993, Rosch 1978). Cognitive economy is achieved by focusing on common attributes, ignoring differences among instances deemed irrelevant in a particular situation.

The notion of class is a core conceptual modeling construct (Parsons and Wand 2008). Indeed, the prevailing method of representing information in an IS is recording an instance in terms of usually one a priori defined class (see Parsons and Wand 2000). This means instance information in a database derived from a class-based conceptual model is constrained by the properties of the classes to which the instance belongs. For example, Tsichritzis and Lochovsky (1982) define datum (data item) in a strictly-typed data model as members of an a priori class. Therefore “data that do not fall into a [class] 0 0 0 have either to be subverted to fall into one, or they cannot be handled in the data model” (Tsichritzis and Lochovsky 1982, p. 8). Information about an instance that is not captured in any classes to which it belongs cannot be captured in a class-based conceptual model or in a database designed from it (Parsons and Wand 1997).

## The Theoretical Link Between Conceptual Modeling and Information Quality

We examine the potential impact of storing instances in classes on the two most heavily studied (Redman 1996, Wand and Wang 1996) IQ dimensions: accuracy and completeness.

First, there is a potential mismatch between the classes familiar to a contributor and those defined in the IS designed to handle user-generated data. A class is a mental model of perceived reality learned or derived from prior experience (Murphy 2004). Thus, a contributor may reasonably see an instance as a member of a different class than those defined for an IS. When required to conform to the class structure imposed by an IS, a contributor may classify an observed phenomenon incorrectly (from the sponsors perspective), leading to lower data accuracy (i.e., whether a statement $\bar { C ( \boldsymbol { x } ) }$ about an instance, x’s, membership in class C is true or false). For example, a system may provide classes $C _ { 1 } , \dots , C _ { N } ,$ , while a contributor may see an observation as a member of class Y (Y may be more general than any of $C _ { 1 } , \dots , C _ { N } ,$ or orthogonal to that structure). If the contributor is forced to guess (C ), the statement C 4x5 may be false, but if the contributor can classify the observation confidently as an instance of Y , the statement Y 4x5 may be true.

Second, class-based models may have a negative effect on data completeness (i.e., the degree to which observed information about an instance is captured). Class-based models inevitably result in property loss, as no class can capture all potentially observable properties of an instance. Ontologically, every “thing” is unique by the virtue of having unique properties: “what makes a thing what it is, i.e., a distinct individual, is the totality of its properties: different individuals fail to share some of their properties” (Bunge 1977, p. 111). Classification is based on similarity (common properties) of instances and ignores properties deemed irrelevant for the purpose of classification. Therefore, IQ is necessarily reduced whenever a class is used to store instances. Below we elaborate on this analysis and develop two theoretical propositions on accuracy and completeness.

## Impact of Class-Based Information Models on Data Accuracy

Accuracy is frequently suggested as the closest proxy for IQ (Ballou and Pazer 1995, Wand and Wang 1996, Wang and Strong 1996). Accuracy is typically defined as degree of conformity of a stored value to the actual (reference) value (Ballou and Pazer 1995, Pipino et al. 2002, Redman 1996, Wand and Wang 1996), or to some accepted fact in a domain (e.g., Barack Obama was born August 4, 1961).

As classes are observer-dependent, differences in prior experience, domain expertise, or ad hoc utility may result in the same thing being classified differently by different people and by the same person over time (Barsalou 1983, McCloskey and Glucksberg 1978, Murphy 2004). For example a passport can be an identity document, a thing to take on a trip abroad and an item to take from a burning house (see Barsalou 1983). Naturally, humans use only those classes with which they are familiar. People also attempt to match candidate classes to the situation at hand (Winograd and Flores 1986). Thus, the process of classification is a fluid interplay of context, purpose, and prior knowledge. In contrast, class-based models require information contributors to conform to a particular classification. If the classes presented by the system are unfamiliar to an information contributor (i.e., the contributor lacks the domain knowledge to identify phenomena as belonging to any of the available classes), the result is a forced choice that does not reflect reality as perceived by the contributor and may be inaccurate with respect to a reference value (e.g., the species of bird selected by a nonexpert contributor to a system that classifies bird sightings may be incorrect).

Proposition 1 (Classification Accuracy). <sub>Class-</sub> based information models result in lower information accuracy (more classification errors) when the classes defined in an information system are unfamiliar to the information contributor.

## Impact of Class-Based Information Models on Information Loss

Support for the classification accuracy proposition suggests the potential benefit of implementing IS that use classes expected to be familiar to potential contributors. While this can increase classification accuracy, it will fail to prevent a second problem, namely, information (property) loss.

Using classes to store information about instances will always result in a failure to fully capture reality, no matter how good the chosen classes are. According to Bunge, any complex instance has a large number of attributes. No one class can encompass them all. This is a key difference between human and computerized representation. When humans classify, they focus on some equivalence among instances, but remain aware of individual differences. In contrast, when instances are stored only as members of classes derived from class-based information models, attributes not captured by class definitions are lost. For example, if we define a class student (assuming it has no subclasses) in an IS, every stored instance of that class will have only those attributes that are part of the class definition. All other potentially useful attributes will be lost. However, a human encountering a particular student may easily notice additional attributes of the individual (e.g., works part-time) that are not implied by the fact that the person is a student, even if student is the class the person initially associates with that instance. As (ontologically) classes are unable to capture all instance attributes that might be observed, class-based information models will result in information loss as long as contributors can observe attributes of an instance that cannot be inferred from the classes they can provide. Consequently we propose:

Table 1 Major Citizen Science Projects That Harness UGC

<table><tr><td>Project</td><td>Scope</td><td>Collection focus1</td><td>No. of records2</td></tr><tr><td>eBirdhttp://www.ebird.org</td><td>Birds, globally</td><td>Species-level</td><td>Over 100 million</td></tr><tr><td>The atlas of living Australiahttp://www.ala.org.au/</td><td>All taxa, Australia</td><td>Species-level</td><td>Over 35 million</td></tr><tr><td>iSpothttp://www.ispotnature.org/</td><td>All taxa, globally (UK primarily)</td><td>Species-level</td><td>Over 250,000</td></tr><tr><td>South Asia birdshttp://www.worldbirds.org/</td><td>Birds, India primarily</td><td>Species-level</td><td>Over 50,000</td></tr><tr><td>Treezillahttp://www.treezilla.org/</td><td>Trees, UK</td><td>Species-level</td><td>48,000</td></tr></table>

<sup>1</sup>Projects may allow other levels, but species is the principal level at which data collection is expected.  
<sup>2</sup>As of May 2014; records come from various sources (e.g., citizens, experts, and existing collections).

Proposition 2 (Information Loss). <sub>Class-based</sub> <sub>in-</sub> formation models result in information loss when the classes a contributor uses to record an instance do not imply some attributes of the instance observed by the contributor.

## Mitigating the Negative Impact of Class-Based Models on Information Quality

Parsons et al. (2011) suggest relaxing the requirement to classify observed instances and, instead, permitting recording contributions in terms of instances and attributes.<sup>3</sup> Instance-based data collection does not require contributors to classify instances and permits storing any attribute associated with the observed instance, thus removing constraints on information capture (Lukyanenko et al. 2011). Contributors can supply attributes and classes based on their domain knowledge.

Next, we describe three experiments that examine the impact of class-based versus instance-based information models on accuracy and completeness in the context of UGC.

## Experiments

We conducted three experiments based on a citizen science project in the natural history domain. Citizen science epitomizes the concept of UGC (Hamel et al. 2009, Hochachka et al. 2012, Kim et al. 2011, Wiersma 2010, Wiggins and Crowston 2011). Major citizen science projects, such as eBird (Table 1), advocate Entity Relationship Diagrams as “best practice,” and are implemented in relational databases (Wiggins et al. 2013). Therefore, evaluating the impact of classbased models on the quality of contributions in these projects is of great practical importance.

## Experiment 1

First, we investigate the impact of class-based models on accuracy and information loss in a free-form data reporting task. While users typically select from predefined classes, a free-form task makes it possible to investigate the impact of modeling on IQ in the absence of potential confounds arising from guiding participants to particular classes (e.g., priming, cuing effects). The unprompted setting enables exploration of the kinds of classes and attributes contributors naturally choose when describing familiar and unfamiliar phenomena (in Experiments 2 and 3, we guide participants to predefined classes).

Information models supporting many natural history citizen science projects are class-based and involve positive identification (i.e., classification) of genera or species (Parsons et al. 2011, Silvertown 2010), as this information is demonstrably useful for scientific research (Bonter and Cooper 2012). Therefore, data collection involves classifying observations at the species-genus level and contributors are presented with options based on this conceptual model (see Table 1).

However, citizen scientists generally are not biology experts.<sup>4</sup> In general, we expect those with low expertise to have limited skill in identifying species, and to correctly identify relatively few, widely known (familiar) species. Here, familiarity refers to knowledge of the attributes that enable correct identification at a particular level (in this case, the species level). Requiring contributors to classify observations at the species-genus level may lead to guessing and, thereby, result in inaccurate data. As an alternative, the basic level is widely accepted in cognitive psychology as the generally preferred classification level for nonexperts (Rosch et al. 1976). In biology, the basic level is an intermediate taxonomic level (e.g., “bird” is a level higher than “American Robin,” and lower than “animal”). Jolicoeur et al. (1984) suggest the basic level is typically the first class people think about when they encounter an instance. Children appear to learn basic level classes ahead of other classes. People use them most frequently in daily speech (Cruse 1977, Wisniewski and Murphy 1989). Experimental studies have shown that people can generally classify objects more quickly (e.g., Murphy and Smith 1982) and more accurately (e.g., Rosch et al. 1976) at the basic level than at subordinate or superordinate levels. We expect those with low species identification skill to nevertheless have a well-developed classification structure consisting of basic level categories and their identifying characteristics and, therefore, high skill in identifying organisms at the basic level. In other words, they will be familiar with relevant basic level categories and can correctly identify at the basic level.

The contrast between basic and species-genus levels clearly illustrates the potential mismatch between the classification structure of a contributor and that defined in an IS, resulting in a potential deterioration of data quality (Proposition 1). As the expected preferred level for nonexperts is the basic level, we therefore hypothesize that, in an unprompted setting (i.e., participants do not choose from a predetermined set of classes), nonexperts will classify more often and more accurately at the basic level than at the species-genus level. That is:

Hypothesis H-1.1 (Classification Accuracy). <sub>In</sub> a free-form data entry task, contributors will classify instances more often and with fewer errors at the basic level than at the species-genus level, when classes at the species-genus level are unfamiliar to the contributors.

Although basic level classes are expected to increase crowd IQ by producing higher (classification) accuracy from nonexpert contributors (by matching classification levels familiar to contributors), the question also arises: To what extent does basic level classification result in information loss? Following Bunge (1977) and cognitive principles (and consistent with Proposition 2), we expect that contributors will tend to report attributes that describe particular instances, rather than attributes associated with a specific class (including a basic level). For example, when describing a bird (e.g., American Robin, Caspian Tern), we expect nonexperts to focus on observable attributes of the instance, such as “standing on the ground” and “orange beak,” as opposed to those associated with its basic level, bird (i.e., “can fly,” “has feathers”). This can be generalized to the claim that a conceptual model based on a particular class level (however useful or intuitive it may be) can preclude potentially useful instance-level properties from being recorded, thereby contributing to lower crowd IQ by failing to accommodate the phenomena of interest as perceived by information contributors. Thus, we hypothesize:

Hypothesis H-1.2 (Information Loss). <sub>In</sub> <sub>a</sub> <sub>free-</sub> form data entry task, contributors will describe instances using terms that include attributes subordinate to the level of the class at which they identify instances.

## Method.

Participants. To test these hypotheses, we conducted a study with 247 undergraduate business students (141 female, 106 male) in eight experimental sessions at a mid-sized Canadian university. Participants in each session were shown the same set of stimuli, with the sequence randomized between sessions to mitigate any order effect. Business students were chosen to ensure a low overall level of biology expertise, reflecting the intended context where information contributors are nonexperts with respect to the intended information uses of project sponsors (in this case, biologists). Low domain expertise was verified using self-reported expertise measures: Most participants (83%) either strongly or somewhat disagreed (on a 5-point scale) with the statement that they are “experts” in local wildlife (mean = 1090; s.d. = 00886). Most participants (77%) had never taken any postsecondary biology courses.<sup>5</sup> Participants indicated that they spend an average of 10 hours per week outdoors (s.d. = 90038). Finally, the low proportion of species-level responses (discussed below) is further evidence of low expertise.

Participation was voluntary and anonymous. Participants were selected from senior business courses and were told the purpose of the study only at the beginning of the session to ensure that no one could prepare in advance and to prevent bias that might arise from attracting students with specific interest in the subject, and vice versa. No incentives (e.g., to encourage correct answers) were provided.

While students are a relatively homogeneous group and unrepresentative of the broader citizen science population, we believe the use of this group as study participants is appropriate. The hypotheses tested are assumed to be universally applicable, as they are derived from fundamental principles of human cognition. We selected participants with low biology expertise because, based on the participation-data quality trade-off (Parsons et al. 2011), those with little domain knowledge may be most disenfranchised in citizen science projects. Furthermore, students can be good predictors of the direction in which the rest of the society is moving vis-à-vis information technology adoption (Gallagher et al. 2001).

Materials. The stimuli were 24 full-color images of plants and animals native to the geographic region in which the study was conducted. The plants and animals were selected by one of the authors, an ecology professor well versed in local flora and fauna. Species were chosen to include primarily organisms believed to be unfamiliar (e.g., false morel) and a few believed to be familiar (e.g., American Robin) to those living in the area. In each image, the organism of interest was in focus and occupied most of the image area.

Participants were randomly assigned into one of two study conditions. Those in the first condition (Categories and Attributes; 122 participants) were given a printed form with two columns. One asked participants to name the object on the image (using one or more words). The second asked them to list features that best describe the object on the image. In the second condition (Attributes only; 125 participants), there was only one column asking participants to list features that best describe the object.

Procedure. Images were displayed to participants in a random sequence on a large screen. Each image was shown for 50 seconds. This time was deemed reasonable as observers often have only short encounters with fauna in the wild. Also, in a pre-test this time was determined sufficient to elicit several attributes and classes. The transition between images was a blank screen shown for one second, accompanied by a beep.

Data Entry. Responses were transcribed by one of the authors to ensure consistency. We recorded verbatim the categories and attributes provided by participants, following practices used in similar studies (Jones and Rosenberg 1974, Lambert et al. 2009). When faced with illegible handwriting we attempted to decipher it but avoided making interpretations and skipped unreadable entries. Obvious spelling errors were corrected (e.g., coyotaie was recorded as coyote); redundant words (e.g., its antlers look heavy was recorded as heavy antlers) and symbols (e.g., brackets, tilde) that did not carry additional meaning were removed. Complex attributes were broken down into individual components (e.g., “long yellow beak” was recorded as “long beak” and “yellow beak”), based on considerations suggested by Rosenberg and

Jones (1972). Following psychology research (e.g., Tanaka and Taylor 1991), attributes for the same species with clearly similar meanings were grouped together (e.g., “horns” and “antlers”).

Coding. Categories provided by participants were coded as “basic level,” “species-genus level,” or “other.” Attributes were coded as “basic level,” “superordinate to basic,” “subordinate to basic,” or “other.” The species-genus level was determined based on biological convention, while the basic level was adopted from prior studies in cognitive psychology. All categorical responses at other biological levels (e.g., subordinate) were coded as “other.” Because a thorough survey of cognitive literature failed to reveal an agreed-upon basic-level for six of the 24 species used (lung lichen, Old Man’s beard, coyote, chipmunk, moose, and caribou), these were excluded from further analysis. The final data set contained 3,737 categories and 7,330 attributes.

For internal consistency, the first author coded the data. To assess coding accuracy, the second author independently recoded category responses, resulting in 94.8% agreement with the original coding (Cohen’s Kappa = 00913). This agreement is considered “almost perfect” (Landis and Koch 1977). The third author independently recoded the attributes, with 76.3% agreement<sup>6</sup> with the original coding.<sup>7</sup>

## Results.

Information Accuracy: Free-Form Data Entry (Hypothesis H-1.1). To assess accuracy, we focused on the “Categories and Attributes” study condition, in which 122 participants were explicitly asked to classify observed stimuli. Participants provided a total of 3,737 categories (on average 1.28 per image per participant). We analyzed data for each image separately. The categories for each species were grouped into basic and combined species-genus levels (categories at other levels were not relevant to this analysis). The basic level (e.g., bird) was expected to be preferred by participants, while species (e.g., American Robin, Turdus migratorius) and genus (e.g., “true thrush,” Turdus) levels are useful to data consumers (e.g., biologists) and are the levels at which many citizen science projects expect contributors to report sightings.

Table 2 Total Responses at Basic and Species-Genus Levels in Experiment 1, with Chi-Square (<sup>2</sup>) Goodness-of-Fit for the Number of Basic vs. Species-Genus Level Categories

<table><tr><td>Species</td><td>Basic and species-genus</td><td>Basic</td><td>Species-genus</td><td>Ratio of basic to species-genus</td><td> $\chi^2$ </td><td>p-value</td></tr><tr><td>American Robin</td><td>164</td><td>86</td><td>78</td><td>1.10</td><td>0.39</td><td>0.532</td></tr><tr><td>Atlantic salmon</td><td>125</td><td>100</td><td>25</td><td>4.00</td><td>45.00</td><td>0.000</td></tr><tr><td>Blue Jay</td><td>168</td><td>69</td><td>99</td><td>0.70</td><td>5.36</td><td>0.021</td></tr><tr><td>Blue Winged Teal</td><td>149</td><td>144</td><td>5</td><td>28.80</td><td>129.67</td><td>0.000</td></tr><tr><td>Bog Labrador tea</td><td>112</td><td>108</td><td>4</td><td>27.00</td><td>96.57</td><td>0.000</td></tr><tr><td>Calypso orchid</td><td>104</td><td>92</td><td>12</td><td>7.67</td><td>61.54</td><td>0.000</td></tr><tr><td>Caspian Tern</td><td>113</td><td>111</td><td>2</td><td>55.50</td><td>105.14</td><td>0.000</td></tr><tr><td>Common Tern</td><td>110</td><td>107</td><td>3</td><td>35.67</td><td>98.33</td><td>0.000</td></tr><tr><td>False morel</td><td>34</td><td>34</td><td>0</td><td>N/A</td><td>34.00</td><td>0.000</td></tr><tr><td>Fireweed</td><td>120</td><td>94</td><td>26</td><td>3.62</td><td>38.53</td><td>0.000</td></tr><tr><td>Greater Yellowlegs</td><td>109</td><td>108</td><td>1</td><td>108.00</td><td>105.04</td><td>0.000</td></tr><tr><td>Indian pipe</td><td>96</td><td>89</td><td>7</td><td>12.71</td><td>70.04</td><td>0.000</td></tr><tr><td>Killer whale</td><td>142</td><td>54</td><td>88</td><td>0.61</td><td>8.14</td><td>0.004</td></tr><tr><td>Mallard Duck</td><td>153</td><td>133</td><td>20</td><td>6.65</td><td>83.46</td><td>0.000</td></tr><tr><td>Red fox</td><td>124</td><td>110</td><td>14</td><td>7.86</td><td>74.32</td><td>0.000</td></tr><tr><td>Red squirrel</td><td>123</td><td>105</td><td>18</td><td>5.83</td><td>61.54</td><td>0.000</td></tr><tr><td>Sheep laurel</td><td>105</td><td>103</td><td>2</td><td>51.50</td><td>97.15</td><td>0.000</td></tr><tr><td>Spotted Sandpiper</td><td>114</td><td>112</td><td>2</td><td>56.00</td><td>106.14</td><td>0.000</td></tr></table>

As expected, basic-level categories were most frequent. To compare the frequency of basic- and species-genus level responses, we used the Chi-square goodness of fit statistic. The observed frequencies of basic and species-genus labels were compared with the null model assuming equal proportions of basic- and species-genus level categories (aggregating species and genus categories into one group increased the test’s conservativeness). For example, when observing Common Tern, participants provided 107 basic level (e.g., bird) and three species-genus level responses. The expected frequency for each group is 55 $\stackrel { \cdot } { ( } \chi ^ { 2 } = 9 8 . 3 3 , \mathrm { d . f . } = 1 , p < 0 . \dot { 0 } 0 1 ,$ ). This shows a strong tendency to report basic-level categories, consistent with prior research in cognitive psychology. Table 2 summarizes the results. In 15 of 18 cases, there was a significant (p < 00001) preference for basic-level categories.<sup>8</sup> Only in the case of American Robin, killer whale, and Blue Jay did basic-level classification not dominate. In the case of killer whale and Blue Jay, participants favored the species, rather than the basic, level (whale or bird). The prevalence of basic-level category responses across most of the stimuli is further evidence of the low level of domain expertise in the sample.

To test accuracy (Hypothesis H-1.1), we assigned a binary variable for each response indicating whether it was correct for the stimulus it described. For example, in descriptions of Common Tern, all labels bird were coded as correct (at the basic level); Common Tern was coded as correct at the species-genus level, while Arctic Tern, Kittiwake, and Osprey were coded as incorrect. We performed Fisher’s exact test of independence to determine whether information accuracy was contingent on level of classification. As Table 2 shows, for half of the images very few species-genus level categories were provided.<sup>9</sup>

The results are significant (using a threshold of p = 0005) for 15 of 17 species (excluding false morel, for which a p value could not be calculated due to a complete absence of species-genus level responses, while 22 participants correctly provided its basic level, mushroom), indicating a strong relationship between level of classification and accuracy (see Table 3).<sup>10</sup> In all significant cases, the number of correct basic level responses was higher than the number of correct species-genus level responses. The cases for which accuracy was not significantly higher for basiclevel categories (i.e., Blue Jay and killer whale) can be explained by high awareness of these organisms and exposure (either in nature or in popular media) to their distinct identifying characteristics, meaning they were familiar with these organisms at the species level. It is not surprising, therefore, that these species resulted in high accuracy at the species level, and that these two species accounted for a high proportion of all correct species-genus level responses. Notwithstanding these charismatic cases, the remainder of the data demonstrates that, as the level of classification changes from basic to species-genus, accuracy declines. Overall, the results provide strong support for Hypothesis H-1.1.

Table 3 Accuracy of Species-Genus vs. Basic-Level Classes in Categories and Attributes Condition in Experiment 1

<table><tr><td>Species</td><td>Correct basic</td><td>Incorrect basic</td><td>Correct species-genus</td><td>Incorrect species-genus</td><td>Fisher&#x27;s exact (p-value)</td></tr><tr><td>American Robin</td><td>86</td><td>0</td><td>74</td><td>4</td><td>0.049</td></tr><tr><td>Atlantic salmon</td><td>100</td><td>0</td><td>0</td><td>24</td><td>0.000</td></tr><tr><td>Blue Jay</td><td>69</td><td>0</td><td>98</td><td>1</td><td>1.000</td></tr><tr><td>Blue Winged Teal</td><td>143</td><td>1</td><td>0</td><td>5</td><td>0.000</td></tr><tr><td>Bog Labrador tea</td><td>108</td><td>0</td><td>0</td><td>4</td><td>0.000</td></tr><tr><td>Calypso orchid</td><td>91</td><td>1</td><td>0</td><td>12</td><td>0.000</td></tr><tr><td>Caspian Tern</td><td>111</td><td>0</td><td>0</td><td>2</td><td>0.000</td></tr><tr><td>Common Tern</td><td>107</td><td>0</td><td>0</td><td>3</td><td>0.000</td></tr><tr><td>False morel</td><td>22</td><td>12</td><td>0</td><td>0</td><td>N/A</td></tr><tr><td>Fireweed</td><td>94</td><td>0</td><td>1</td><td>25</td><td>0.000</td></tr><tr><td>Greater Yellowlegs</td><td>107</td><td>1</td><td>0</td><td>1</td><td>0.018</td></tr><tr><td>Indian pipe</td><td>88</td><td>1</td><td>0</td><td>7</td><td>0.000</td></tr><tr><td>Killer whale</td><td>48</td><td>6</td><td>86</td><td>2</td><td>0.054</td></tr><tr><td>Mallard Duck</td><td>133</td><td>0</td><td>15</td><td>5</td><td>0.000</td></tr><tr><td>Red fox</td><td>104</td><td>6</td><td>10</td><td>4</td><td>0.015</td></tr><tr><td>Red squirrel</td><td>100</td><td>5</td><td>1</td><td>17</td><td>0.000</td></tr><tr><td>Sheep laurel</td><td>103</td><td>0</td><td>0</td><td>2</td><td>0.000</td></tr><tr><td>Spotted Sandpiper</td><td>112</td><td>0</td><td>0</td><td>2</td><td>0.000</td></tr></table>

Note. Fisher’s exact test is applied to test whether information accuracy was contingent on level of classification.

Information Loss (Hypothesis H-1.2). We measured information loss in terms of the number of attributes reported by participants that could not be inferred from the classes provided by those participants for an image. The results from the accuracy test above demonstrate the dominance of basic-level classes over species-genus level classes. This finding is critical in testing the degree of information loss, as the question can now be asked: To what extent do participants use basic-level attributes (e.g., can fly, has feathers for bird) versus lower-level attributes (e.g., red breast for American Robin) when they are not required to classify observations? The greater the number of subbasic level attributes reported, the greater the degree of potential information loss if the basic-level is the one at which information is collected and stored.

To investigate information loss, all attributes (7,330) in the Attributes-only condition for the 18 plants and animals with an agreed-on basic-level category were classified into: sub-basic, basic (and superordinate) or other, resulting in 6,429 sub-basic, 824 basic, and 77 other attributes.<sup>11</sup>

We tested for differences using the Chi-square goodness of fit test, where the observed frequencies of sub-basic and basic level attributes were compared with expected frequencies (assuming equal probabilities of obtaining basic and sub-basic attributes). In contrast with the prevalence of basic-level categorization, there were 9.38 times more sub-basic than basic-level attributes, with an average p-value approaching zero. Table 4 summarizes the results across the 18 species used in this analysis. The data strongly support Hypothesis H-1.2 and indicate that, despite the salience of a particular classification level, the basic-level does not capture all information available to and easily reported by contributors.

## Experiment 2

In Experiment 1, the classes that would be of interest to project sponsors did not, in most cases, match contributor classifications of phenomena in the domain. However, we did not direct participants to a particular level of classification. In practice, data collection (whether for UGC or traditional applications)

Note. Significance testing is based on Chi-square test of observed vs. expected frequencies of sub-basic and basic-level attributes <sup>1</sup>Some attributes provided could not be associated with biological classes of organisms. For example, some participants used adjectives such as “beautiful” and “standing on rock” to describe organisms.

Table 4 Number of Sub-Basic, Basic, Super-Basic, and Other Attributes in Attributes-Only Condition of Experiment 1

<table><tr><td>Species</td><td>Total</td><td>Sub-basic</td><td>Basic</td><td>Sub-basic to basic ratio</td><td>Super-basic</td><td>Other1</td><td> $\chi^2 p-value (basic and super vs. sub-basic)$ </td></tr><tr><td>American Robin</td><td>400</td><td>362</td><td>35</td><td>10.3</td><td>1</td><td>2</td><td>0.000</td></tr><tr><td>Atlantic salmon</td><td>337</td><td>273</td><td>45</td><td>6.1</td><td>4</td><td>15</td><td>0.000</td></tr><tr><td>Blue Jay</td><td>453</td><td>397</td><td>51</td><td>7.8</td><td>1</td><td>4</td><td>0.000</td></tr><tr><td>Blue Winged Teal</td><td>439</td><td>350</td><td>76</td><td>4.6</td><td>2</td><td>11</td><td>0.000</td></tr><tr><td>Bog Labrador tea</td><td>274</td><td>266</td><td>3</td><td>88.7</td><td>2</td><td>3</td><td>0.000</td></tr><tr><td>Calypso orchid</td><td>364</td><td>358</td><td>3</td><td>119.3</td><td>0</td><td>3</td><td>0.000</td></tr><tr><td>Caspian Tern</td><td>511</td><td>460</td><td>47</td><td>9.8</td><td>1</td><td>3</td><td>0.000</td></tr><tr><td>Common Tern</td><td>479</td><td>435</td><td>41</td><td>10.6</td><td>0</td><td>3</td><td>0.000</td></tr><tr><td>False morel</td><td>248</td><td>238</td><td>9</td><td>26.4</td><td>0</td><td>1</td><td>0.000</td></tr><tr><td>Fireweed</td><td>312</td><td>302</td><td>3</td><td>100.7</td><td>0</td><td>7</td><td>0.000</td></tr><tr><td>Greater Yellowlegs</td><td>534</td><td>486</td><td>39</td><td>12.5</td><td>4</td><td>5</td><td>0.000</td></tr><tr><td>Indian pipe</td><td>351</td><td>342</td><td>6</td><td>57.0</td><td>0</td><td>3</td><td>0.000</td></tr><tr><td>Killer whale</td><td>388</td><td>325</td><td>54</td><td>6.0</td><td>0</td><td>9</td><td>0.000</td></tr><tr><td>Mallard Duck</td><td>497</td><td>421</td><td>74</td><td>5.7</td><td>0</td><td>2</td><td>0.000</td></tr><tr><td>Red fox</td><td>476</td><td>340</td><td>46</td><td>7.4</td><td>88</td><td>2</td><td>0.000</td></tr><tr><td>Red squirrel</td><td>503</td><td>362</td><td>105</td><td>3.4</td><td>35</td><td>1</td><td>0.000</td></tr><tr><td>Sheep laurel</td><td>326</td><td>319</td><td>4</td><td>79.8</td><td>0</td><td>3</td><td>0.000</td></tr><tr><td>Spotted Sandpiper</td><td>438</td><td>393</td><td>44</td><td>8.9</td><td>1</td><td>0</td><td>0.000</td></tr></table>

typically involves populating pre-existing class structures. Experiment 1 demonstrated that class-based models can impair accuracy and result in information loss, but it does not provide direct evidence of the impact of a predefined schema on accuracy. Hence, we conducted a second experiment to assess whether our findings with respect to the relative accuracy of basic-level versus species-level classification continue to hold when a predefined class-based schema is imposed.

In Experiment 2, we asked participants to classify each stimulus by selecting one option from prespecified options. Based on the results of Experiment 1, we manipulated the classification choices (levels) available to participants. In the first condition, we simulated a class-based model at a single level, typical of existing projects (i.e., select one species from a set of potential species). As an alternative to species-based collection, in the second condition we focused on basic-level categories. For each organism, we explicitly included the most frequent (and always correct) basic-level response from Experiment 1, e.g., bird, duck, fish, flower, and mushroom. To make the task more conservative (and also realistic), in addition to these basic-level categories we included multiple correct and incorrect options at different classification levels. For example, the options for Common Tern (Sterna hirundo) were: bird (predicted response, correct, basic), animal (correct, superordinate to basic), Common Tern (correct, species-level), Iceland Gull (incorrect, species-level), loon (incorrect, subordinate to basic), shorebird (incorrect, subordinate), tern (correct, subordinate), warm-blooded organism (correct, superordinate), waterfowl (incorrect, subordinate).<sup>12</sup> For some organisms, we added an option considered to be basic-level in the psychology literature that was not however the salient basic-level category based on Experiment 1 (e.g., “bird” for Mallard Duck in addition to the predicted “duck”). These served as distractors. The presence of multiple correct options (included at levels deemed basic) offered a strong test of the predicted basic level by evaluating the extent to which preference for the basic level persists in the presence of other viable (including correct) choices. Finally, the hierarchical class-based model in the second condition also offered a plausible practical approach to collecting UGC. Experiment 1 demonstrated that participants provide classes at different levels (basic being the most frequent). In open UGC settings, modelers cannot be confident about which classification level will be the most appropriate for a given contributor; therefore, an IS may present multiple levels in a taxonomy simultaneously. For the same reason, in each condition we included “I don’t know” and “Other” (with space for an alternate response) options to allow participants to avoid classifying (typical to volitional IS use) or respond using classes that were not among the predefined choices.

Experiment 1 showed that nonexperts favor basiclevel classes. We therefore expect participants to classify more often and more accurately at the predicted basic level in the multilevel condition than at the species-level in the single-level condition. Consistent with Proposition 1, we hypothesize:

Table 5 Proportion of Correct Species-Level Responses (in the Single-Level Condition, E2SL) vs. Predicted Basic-Level Responses (in the Multilevel Condition, E2ML) of Experiment 2

<table><tr><td rowspan="2">Species-level</td><td colspan="2">E2SL</td><td colspan="3">E2ML</td><td colspan="2">E2ML vs. E2SL</td></tr><tr><td>Correct species</td><td>% correct species</td><td>Predicted basic</td><td>Predicted basic responses</td><td>% predicted basic</td><td>% diff.</td><td> $\chi^2$ p-value</td></tr><tr><td>Atlantic salmon</td><td>9</td><td>23.7</td><td>fish</td><td>12</td><td>30.8</td><td>7.1</td><td>0.485</td></tr><tr><td>Blue Winged Teal</td><td>3</td><td>7.9</td><td>duck</td><td>26</td><td>66.7</td><td>58.8</td><td>0.000</td></tr><tr><td>Calypso orchid</td><td>6</td><td>15.8</td><td>flower</td><td>14</td><td>35.9</td><td>20.1</td><td>0.044</td></tr><tr><td>Caspian Tern</td><td>2</td><td>5.3</td><td>bird</td><td>21</td><td>53.8</td><td>48.6</td><td>0.000</td></tr><tr><td>Common Tern</td><td>4</td><td>10.5</td><td>bird</td><td>13</td><td>33.3</td><td>22.8</td><td>0.019</td></tr><tr><td>False morel</td><td>0</td><td>0.00</td><td>mushroom</td><td>1</td><td>2.6</td><td>2.6</td><td>0.320</td></tr><tr><td>Fireweed</td><td>5</td><td>13.2</td><td>flower</td><td>16</td><td>41.0</td><td>27.9</td><td>0.006</td></tr><tr><td>Indian pipe</td><td>3</td><td>7.9</td><td>flower</td><td>10</td><td>25.6</td><td>17.7</td><td>0.038</td></tr><tr><td>Mallard Duck</td><td>25</td><td>65.8</td><td>duck</td><td>11</td><td>28.2</td><td>-37.6</td><td>0.001</td></tr><tr><td>Sheep laurel</td><td>3</td><td>7.9</td><td>flower</td><td>23</td><td>59.0</td><td>51.1</td><td>0.000</td></tr><tr><td>Total</td><td>60 of 379</td><td>15.8</td><td></td><td>147 of 390</td><td>37.7</td><td>21.9</td><td>0.000</td></tr></table>

Note. Significance testing is based on Chi-square test of frequencies of correct basic vs. species responses.

Hypothesis H-2 (Classification Accuracy). <sub>In</sub> <sub>a</sub> constrained (class-based) data entry task, contributors will classify instances more often and with fewer errors at the basic level in the multilevel condition than at the species level in the single-level condition, when classes at the species level are unfamiliar to the contributors.

## Method.

Participants. Seventy-seven undergraduate students (24 female, 53 male) participated in the study. Almost all (94.8%) strongly or somewhat disagreed (on a 5- point Likert scale) with the statement that they are “experts” in local wildlife, and most (68.8%) had never taken a post-secondary course in biology.

Materials and Procedure. The materials used were a subset of those in Experiment 1.<sup>13</sup> The procedure for presenting the images was the same as in Experiment 1. Participants were randomly assigned to one of two conditions. In the single-level condition (38 participants), participants chose from a list of possible species-level responses; in the multilevel condition (39 participants), participants chose from options that included the basic level and levels above and below the basic (including species).

In the single-level condition, of the nine species provided as options, only one was correct. In the multilevel condition, of the nine classes provided as options, only one was the predicted basic-level class. The options were printed on paper with each set of options on its own page. In both conditions, the order of options was randomized for each participant and participants were asked to select one option.

Results. To evaluate Hypothesis H-2, we compared the proportion of correct species-level responses given by participants in the single-level condition with the proportion of predicted basic-level responses in the multilevel condition. In total, we obtained 379 responses in the single-level condition including 60 correct species-level responses. Other responses in this condition included 108 “I don’t know,” 13 correct responses at the basic-level provided in the “Other” field, and 198 incorrect species-level responses. In the multilevel condition we obtained 390 responses, of which 147 were at the predicted basic level. Other responses in this condition included 15 “I don’t know,” 130 correct responses at other levels, and 98 incorrect responses at different levels.

We compared predicted basic-level responses in the multilevel condition with correct species-level responses in the single-level condition. Consistent with Experiment 1, the proportion of responses at the predicted basic level in the multilevel condition was significantly greater than the correct responses at the species level in the single-level condition (37.7% versus 15.8%, $p = 0 . 0 0 0 , \chi ^ { 2 } = 4 6 . 7 , 1 \mathrm { d . f . ) }$ . The basic level was significantly more frequent for 7 of 10 organisms (see Table 5).<sup>14</sup>

The findings provide strong evidence of the strength of basic-level categorization compared with species-level categorization. To be selected, participants had to prefer this level to a number of plausible options, including alternative options at the basic-level. Indeed, of 148 responses at the basic-level given, 147 (the exception was goose instead of duck by one participant) were the basic-level categories we predicted based on psychological theory.

In addition to testing Hypothesis H-2, we analyzed the results within the two conditions. Among the 375 categorical responses in the multilevel condition (excluding 15 “I don’t know” responses), basic was the most frequent level: there were more basic-level responses (148 or 39.5%), than specieslevel (103 responses, 27.5%) responses $( p = 0 . 0 0 5 ,$ $\chi ^ { 2 } = 8 . 0 7 ,$ , 1 d.f.). Accuracy of basic-level responses was 99.3% compared with 53.4% for species-level responses. Basic-level responses accounted for 53.1% of correct responses in the multilevel condition while only 20.2% of correct responses were at the specieslevel $( p = 0 . 0 0 0 ,$ $\chi ^ { 2 } = 4 1 . { \overset { \cdot } { 9 } } 0 ,$ , 1 d.f.). Of other correct responses, 7.6% were at the subordinate level and 19.1% at the superordinate level. Finally, basic-level responses were also provided in the single-level condition where, of 13 correct responses provided in the “Other” field, all were the predicted basic-level classes.

Overall, the results from Experiment 2 demonstrate that in the constrained-choice task participants select more predicted basic-level classes in a multilevel condition than correct species-level classes in a singlelevel condition. Notably, the prevalence and accuracy of the basic-level was generally not affected by the presence of other correct or plausible classes. The results are consistent with theoretical predictions and the free-form responses of Experiment 1 and provide strong support for Hypothesis H-2 and Proposition 1.

## Experiment 3

Experiments 1 and 2 demonstrate that accuracy declines if the classes specified in a conceptual model do not match the classes contributors can competently provide. In Experiment 3, we sought to rule out possible alternative explanations for the findings in Experiments 1 and 2. First, we ensured that participants in the species-level condition were not drawn to incorrect options merely due to greater awareness of such options than of the correct one. Therefore, we examined the results of Experiment 2 and removed and replaced all incorrect classes that received a larger than average number of responses (a possible indicator of participant awareness of these terms, if not familiarity with the identifying characteristics). For example, jelly leaf fungus was removed as an option for false morel because it was incorrectly chosen 13 times in Experiment 2, whereas the next most frequent incorrect response was selected five times. All frequent incorrect responses were replaced with new classes deemed by the team’s biologist to be unfamiliar to nonexperts.<sup>15</sup>

<sup>15</sup> A complete listing of options provided to participants for all species used is provided in the online supplement.

Second, we increased the number of “distractor” basic-level classes to provide for a more conservative evaluation and kept the number of incorrect options constant across organisms. We also replaced duck with bird as the predicted basic-level class for Mallard Duck and Blue Winged Teal. Removing duck from the predefined set of classes allowed evaluation of the salience of a more established (e.g., Rosch et al. 1976) basic-level class bird; however, this was a conservative decision as Experiments 1 and 2 demonstrated a strong preference for duck.

Third, to better delineate the boundary of our theory as applying to unfamiliar classes, we included in Experiment 3 the species from Experiment 1 that were removed in Experiment 2 (i.e., American Robin, killer whale, and Blue Jay). By including these, we created a small set of familiar stimuli based on the finding from Experiment 1 that participants identified these organisms at the species level. This enables an informal comparison with the unfamiliar group, i.e., the 10 organisms from Experiment 2 for which accuracy was greater in the multilevel condition.

Consistent with Proposition 1 and Hypothesis H-2, we hypothesize:

<sup>Hypothesis</sup> <sup>H-3.1.</sup> In a constrained (class-based) data entry task, contributors will classify instances more often and with fewer errors at the basic level in the multilevel condition than at the species level in the single-level condition, when classes at the species level are unfamiliar to the contributors.

Finally, to further evaluate our claim that requiring nonexperts to conform to a predetermined classbased schema results in negative consequences on IQ, we compare classification accuracy in free-form versus constrained data entry tasks. While constrained data entry provides participants with cues and may help in recalling applicable classifications, it may also bias participants to choices they might not otherwise make, leading to wrong classification decisions (Parsons et al. 2011). For example, whereas nonexperts can provide accurate responses in a free-form data task (as seen in Experiment 1 where the overall accuracy of categories provided was 86.7%), the presence of different options may influence data contributors to select incorrect classes. Consistent with Proposition 1, we hypothesize:

<sup>Hypothesis</sup> <sup>H-3.2.</sup> In a free-form data entry task, contributors will classify instances with fewer errors than in a class-based data entry task, whether the latter uses singlelevel or multilevel classification.

## Method.

Participants. Sixty-six undergraduate business students (36 female, 30 male) participated, drawn from the same population of biology nonexperts as in Experiments 1 and 2. Almost all participants (89.4%) strongly or somewhat disagreed (on a 5-point Likert scale) with the statement that they were “experts” in local wildlife, and most (83.3%) had never taken a post-secondary course in biology.

Table 6 Proportion of Correct Species-Level Responses (in the Single-Level Condition, E3SL) vs. Predicted Basic-Level Responses (in the Multilevel Condition, E3ML) of Experiment 3

<table><tr><td rowspan="2">Species-level</td><td colspan="2">E3SL</td><td colspan="3">E3ML</td><td colspan="2">E3ML vs. E3SL</td></tr><tr><td>Correct species</td><td>% correct species</td><td>Predicted basic label</td><td>Predicted basic responses</td><td>% predicted basic</td><td>% diff.</td><td> $\chi^2$ p-value</td></tr><tr><td>Atlantic salmon</td><td>4</td><td>17.4</td><td>fish</td><td>6</td><td>28.6</td><td>11.2</td><td>0.377</td></tr><tr><td>Blue Winged Teal</td><td>11</td><td>47.8</td><td>bird</td><td>4</td><td>19.0</td><td>-28.8</td><td>0.044</td></tr><tr><td>Calypso orchid</td><td>3</td><td>13.0</td><td>flower</td><td>10</td><td>47.6</td><td>34.6</td><td>0.012</td></tr><tr><td>Caspian Tern</td><td>1</td><td>4.3</td><td>bird</td><td>9</td><td>42.9</td><td>38.5</td><td>0.002</td></tr><tr><td>Common Tern</td><td>2</td><td>8.7</td><td>bird</td><td>7</td><td>33.3</td><td>24.6</td><td>0.043</td></tr><tr><td>False morel</td><td>0</td><td>0.0</td><td>mushroom</td><td>2</td><td>9.5</td><td>9.5</td><td>0.130</td></tr><tr><td>Fireweed</td><td>7</td><td>30.4</td><td>flower</td><td>7</td><td>33.3</td><td>2.9</td><td>0.837</td></tr><tr><td>Indian pipe</td><td>1</td><td>4.3</td><td>flower</td><td>3</td><td>14.3</td><td>9.9</td><td>0.252</td></tr><tr><td>Mallard Duck</td><td>18</td><td>78.3</td><td>bird</td><td>1</td><td>4.8</td><td>-73.5</td><td>0.000</td></tr><tr><td>Sheep laurel</td><td>0</td><td>0.0</td><td>flower</td><td>12</td><td>57.1</td><td>57.1</td><td>0.000</td></tr><tr><td>Total</td><td>47 of 230</td><td>20.4</td><td></td><td>61 of 210</td><td>29.0</td><td>8.6</td><td>0.036</td></tr></table>

Note. Significance testing is based on Chi-square test of frequencies of correct basic vs. species responses.

Materials and Procedure. The materials used were the same as in Experiment 2, with the addition of the three familiar species used in Experiment 1. The procedure for presenting the images was the same as in Experiments 1 and 2. Participants were randomly assigned to one of three conditions. In the first condition (single-level, 23 participants), participants chose one option from a list of possible specieslevel responses. In the second condition (multilevel, 21 participants), participants chose one option from classes at the basic-level and at levels above and below the basic (including species). In both conditions, we included “I don’t know” and “Other” (with space for an alternate response) options to allow participants to avoid classifying or respond using classes that were not included in the predefined lists. In the third condition (free form, 22 participants), participants were presented with an empty sheet and asked to name the object using one class or to write “I don’t know.”

In the single-level condition, of the nine species provided as options, only one was correct. In the multilevel condition, of the nine classes provided as options, only one was the predicted basic. The options were printed on paper, with each set of options on its own page. In both conditions, the order of options was randomized for each participant and participants were asked to select one option for each stimulus.

Results. To evaluate Hypothesis H-3.1, we followed the procedure used to test Hypothesis H-2, but analyzed the familiar and unfamiliar groups separately as we do not formally hypothesize about the effects of familiarity given that contributors are in general unfamiliar with species level classification. We obtained 299 responses in the single-level condition, including 105 correct species-level responses (58 for the three familiar and 47 for the 10 unfamiliar species). Other responses in this condition included 86 “I don’t know” (93.0% of which were given for the unfamiliar species), one correct response at the predicted basic-level provided in the “Other” field, and 107 incorrect species-level responses (95.3% of which were for the unfamiliar species). In the multilevel condition, we obtained 273 responses, including 70 at the predicted basic level (61 in the unfamiliar and nine in the familiar group). Other responses in this condition include 21 other basic-level classes, 19 “I don’t know” (94.7% in the unfamiliar group), and 94 correct and 69 incorrect responses at different levels.

We compared the predicted basic-level responses in the multilevel condition with the correct responses at the species level in the single-level condition. As expected, participants provided a greater number of correct species-level responses than predicted basic-level responses for species in the familiar group (84.1% versus 14.3%, $p = 0 . 0 0 0 , \ \chi ^ { 2 } = 6 4 . 1 4 , \ 1$ d.f.). The differences were significant for all three familiar species $( p < 0 . 0 1$ for each). In contrast, in the unfamiliar group, the proportion of responses at the predicted basic-level in the multilevel condition was significantly greater than the proportion of correct responses at the species level in the single-level condition (29.0% versus 20.4%, $p = 0 . 0 3 6 , \ x ^ { \bar { 2 } } = 4 . 4 0 ,$ 1 d.f.). At the same time, the proportion of basiclevel responses in the multilevel condition was significantly larger than the proportion of correct species in the single-level condition for only three of the 10 species (see Table 6). The low proportion by species may be the result of a lower effect size due to the increased conservativeness of Experiment 3 compared with Experiment 2. For example, the substitution of the basic level “duck” with a more established, but less salient “bird” potentially dissuaded participants from selecting “bird” as an option. Notably, participants provided 14 responses “duck” in the “Other” fields for Mallard and Blue Winged Teal. Furthermore, the purposeful exclusion of the incorrect options that were frequently chosen in Experiment 2 resulted in a slight increase in the percentage of correct species-level responses in Experiment 3 (compare Table 5 versus Table 6). This shows that the salience of basic-level categories can be somewhat undermined, but at the expense of realism and ecological validity. Overall, the results remain consistent with those in Experiments 1 and 2.

Table 7 Categorical Responses and Percent Accurate Responses for Experiment 3 in Single-Level (E3SL) and Multilevel Condition (E3ML) for “Familiar” Species

<table><tr><td rowspan="2">Species</td><td colspan="3">E3SL</td><td colspan="3">E3ML</td></tr><tr><td>Correct</td><td>Total</td><td>% accuracy</td><td>Correct</td><td>Total</td><td>% accuracy</td></tr><tr><td>American Robin</td><td>16</td><td>19</td><td>84.2</td><td>16</td><td>21</td><td>76.2</td></tr><tr><td>Species-level</td><td>16</td><td>19</td><td>84.2</td><td>12</td><td>17</td><td>70.6</td></tr><tr><td>Other levels</td><td>0</td><td>0</td><td></td><td>4</td><td>4</td><td>100.0</td></tr><tr><td>Blue Jay</td><td>23</td><td>23</td><td>100.0</td><td>20</td><td>20</td><td>100.0</td></tr><tr><td>Species-level</td><td>23</td><td>23</td><td>100.0</td><td>16</td><td>16</td><td>100.0</td></tr><tr><td>Other levels</td><td>0</td><td>0</td><td></td><td>4</td><td>4</td><td>100.0</td></tr><tr><td>Killer whale</td><td>19</td><td>21</td><td>90.5</td><td>21</td><td>21</td><td>100.0</td></tr><tr><td>Species-level</td><td>19</td><td>21</td><td>90.5</td><td>19</td><td>19</td><td>100.0</td></tr><tr><td>Other levels</td><td>0</td><td>0</td><td></td><td>2</td><td>2</td><td>100.0</td></tr><tr><td>Total</td><td></td><td></td><td>92.1</td><td></td><td></td><td>91.9</td></tr><tr><td>Species-level</td><td></td><td></td><td>92.1</td><td></td><td></td><td>90.6</td></tr><tr><td> $Other\ levels^1$ </td><td></td><td></td><td>—</td><td></td><td></td><td>100.0</td></tr></table>

<sup>1</sup>Consisting of nine basic-level responses (bird, whale) and one superordinate (mammal).

In addition to testing Hypothesis H-3.1, we analyzed the results within the two conditions. As expected, for the “familiar” group, the species level accounted for all 63 categorical responses in singlelevel condition (the remaining six were “I don’t know”) and for 82.5% (52 of 63) of the categorical responses in the multilevel condition. Most specieslevel responses for the familiar group were correct (see Table 7). As in Experiment 1, in the constrained-choice task, participants were comfortable classifying American Robin, Blue Jay, and killer whale at the species level, suggesting that the species level was congruent with their mental schema for these organisms.

For the “unfamiliar” group in the multilevel condition, basic-level responses were the most common. Among the 192 categorical responses in the “unfamiliar” group (excluding 18 “I don’t know” responses), 82 responses or 42.5% were at the basic level and 61 or 31.6% were at the species level $( p = 0 . 0 7 9 ,$ $\chi ^ { 2 } = 3 . 0 8 , \ 1 \ \mathrm { d . f . } )$ . Accuracy of basic-level responses was 96.3% compared to 42.6% at the species-level. Basic level accounted for 63.2% of correct responses while only 20.8% of correct responses were at the species-level $( p = 0 . 0 0 0 , \ \chi ^ { 2 } = 2 6 . \mathcal { \bar { I } } 5 , \ 1 \ \mathrm { d . f . } )$ . Of other correct responses, 3.2% were at the subordinate level and 12.8% at the superordinate level. Finally, the sole nonspecies-level response in the single-level condition was a basic level “duck” provided in the “Other” field.

These results support Hypothesis H-3.1 and are consistent with Hypothesis H-1.1 (free-form class elicitation) and Hypothesis H-2, providing additional evidence that accuracy is contingent on providing users with classification structures more congruent with preferred user classification models. The lack of difference among the familiar group is consistent with Hypothesis H-3.1 as it suggests that, for these species, most contributors are comfortable classifying at the species-genus level.

Impact of Schema on Accuracy: Free-Form vs. Class-Based Models (Hypothesis H-3.2). In assessing the accuracy of free-form versus class-based data collection, we followed the procedure used in Hypothesis H-1.1. In total 286 responses in the free-form condition were compared with 299 responses in the single-level and 273 responses in the multilevel condition.

Overall accuracy in the free-form condition was 77.3% compared to 35.5% in the single-level condition and 66.7% in the multilevel condition (both percentages are significantly different from the free-form condition based on Fisher’s exact, $p < 0 . 0 5 )$ . We then investigated the differences for each organism separately. As shown in Table 8, in nine of 13 cases participants in the free-form condition provided a significantly higher percentage of accurate responses compared to those in the single-level condition.

In addition, as Table 8 shows, in two of 13 cases accuracy in the free-form condition was significantly higher than in the multilevel condition. In part, the increase in accuracy in the free-form condition is due to the greater accuracy when classifying at the basiclevel (which was close to 100% correct regardless of condition). There were significantly more basiclevel responses in the free-form condition than in the multilevel condition; 158 of 286 (55.2%) compared to 91 of 273 (33.3%) (p = 00000, <sup>2</sup> = 27015, 1 d.f.). There was only one basic-level response (duck) in the species-only condition (provided in the “Other” field). Considering that overall accuracy in the freeform condition was significantly higher than in both of the constrained-choice conditions, the results support Hypothesis H-3.2.

## General Discussion

The results demonstrate that accuracy is contingent on the classes used to model a domain. In free-form data collection, in most cases we found higher accuracy when using basic-level classification. Similarly, in schema-mediated data collection, we found higher accuracy when data collection was guided by basiclevel classes. Confirmation of the findings from the free-form data collection in the constrained-choice task is further notable. While the multilevel conditions in Experiments 2 and 3 included other plausible correct options, participants generally avoided them, favoring basic-level classes.

Table 8 Accuracy in Experiment 3, Single-Level Condition (E3SL), Multilevel Condition (E3ML), and Free-Form Condition (E3FF)

<table><tr><td rowspan="2">Species</td><td colspan="2">E3SL</td><td colspan="2">E3ML</td><td colspan="2">E3FF</td><td colspan="2">Δ % correct</td></tr><tr><td>Correct/incorrect</td><td>% correct</td><td>Correct/incorrect</td><td>% correct</td><td>Correct/incorrect</td><td>% correct</td><td>E3FF vs. E3SL</td><td>E3FF vs. E3ML</td></tr><tr><td>American Robin</td><td>16/7</td><td>69.6</td><td>16/5</td><td>76.2</td><td>20/2</td><td>90.9</td><td>21.3**</td><td>14.7*</td></tr><tr><td>Atlantic salmon</td><td>4/19</td><td>17.4</td><td>13/8</td><td>61.9</td><td>17/5</td><td>77.3</td><td>59.9**</td><td>15.4*</td></tr><tr><td>Blue Jay</td><td>23/0</td><td>100.0</td><td>20/1</td><td>95.2</td><td>20/2</td><td>90.9</td><td>-9.1**</td><td>-4.3*</td></tr><tr><td>Blue Winged Teal</td><td>11/12</td><td>47.8</td><td>16/5</td><td>76.2</td><td>22/0</td><td>100.0</td><td>52.2**</td><td>23.8*</td></tr><tr><td>Calypso orchid</td><td>3/20</td><td>13.0</td><td>12/9</td><td>57.1</td><td>17/5</td><td>77.3</td><td>64.2**</td><td>20.1*</td></tr><tr><td>Caspian Tern</td><td>1/22</td><td>4.3</td><td>10/11</td><td>47.6</td><td>18/4</td><td>81.8</td><td>77.5**</td><td>34.2*</td></tr><tr><td>Common Tern</td><td>2/21</td><td>8.7</td><td>8/13</td><td>38.1</td><td>12/10</td><td>54.5</td><td>45.8**</td><td>16.5*</td></tr><tr><td>False morel</td><td>0/23</td><td>0.0</td><td>14/7</td><td>66.7</td><td>8/14</td><td>36.4</td><td>36.4**</td><td>-30.3*</td></tr><tr><td>Fireweed</td><td>7/16</td><td>30.4</td><td>10/11</td><td>47.6</td><td>14/8</td><td>63.6</td><td>33.2**</td><td>16.0*</td></tr><tr><td>Indian pipe</td><td>1/22</td><td>4.3</td><td>6/15</td><td>28.6</td><td>12/10</td><td>54.5</td><td>50.2**</td><td>26.0*</td></tr><tr><td>Killer whale</td><td>19/4</td><td>82.6</td><td>21/0</td><td>100.0</td><td>20/2</td><td>90.9</td><td>8.3**</td><td>-9.1*</td></tr><tr><td>Mallard Duck</td><td>19/4</td><td>82.6</td><td>19/2</td><td>90.5</td><td>22/0</td><td>100.0</td><td>17.4**</td><td>9.5*</td></tr><tr><td>Sheep laurel</td><td>0/23</td><td>0.0</td><td>17/4</td><td>81.0</td><td>19/3</td><td>86.4</td><td>86.4**</td><td>5.4*</td></tr><tr><td>Average</td><td></td><td>35.5</td><td></td><td>66.7</td><td></td><td>77.3</td><td>41.8**</td><td>10.6*</td></tr></table>

<sup>∗</sup>Significant at 0.05; <sup>∗∗</sup>significant at 0.01 level (using Fisher’s exact test).

In addition, the comparison between unconstrained and schema-mediated data collection shows that accuracy does not necessarily improve when intuitive and accurate options are provided for users. Indeed, the overall classification accuracy in the free-form condition of Experiment 3 was significantly greater than in single or multilevel conditions. This is particularly notable because the most frequent correct options from the free-form task in Experiment 1 (the basic-level categories bird, fish, mushroom) were available as options in the multilevel condition of Experiment 3, making the comparison more conservative. This further indicates the potential IQ implications of using a predefined schema in UGC settings: while predefined classes provide nonexpert data contributors with cues that may guide them to correct choices, they may also bias nonexperts to wrong classification decisions.

Our experiments point to a data quality dilemma in using class-based models to capture UGC. The classes nonexperts are comfortable using, that is, the ones for which they know the identifying characteristics of instances, tend to be basic-level classes. However, for many applications, more specific classes are required. Experiment 1 shows that when contributors attempt to classify observations at a lower level accuracy generally declines. Thus, there is the potential for low accuracy in real-world UGC data sets that require specialized classification choices. However, our results also show that participants can contribute substantial amounts of information (attributes) beyond what is implied by the high-level classes to which they can assign an observed phenomenon.

While the support for Hypotheses H-1.1, H-2, and H-3.1 demonstrates the merits of using more familiar classes (e.g., basic-level categories) in designing information systems to harness UGC, in this paper we also examine an alternative to the class-based approach to harnessing collective intelligence. Based on ontology and cognition, we argue that representing instances in terms of classes results in the loss of potentially valuable properties. The test of Hypothesis H-1.2 demonstrated that a significant number of low-level attributes can be generated by nonexpert contributors. These attributes cannot be inferred from the classes that can be accurately identified by nonexperts. All three experiments show that basic-level categories are generally the most frequently provided and typically most accurate of the classification levels, whether in free-form or schema-mediated data collection tasks. Notwithstanding this, the results also show that modeling using basic-level classes can be expected to lead to a significant loss of properties.

Implications for Research and Practice Our findings have important implications for theory and practice in harnessing UGC. Currently, many projects (e.g., various active citizen science initiatives) focus data collection on classifying phenomena. Our research suggests that such approaches not only can lead to data accuracy problems, but can also preclude collection of valuable information (leading to information loss). Our results highlight an opportunity to extract additional data from the crowd that is routinely neglected in applications with fixed classification structure. Thus, we contend the potential of

UGC is not being fully realized. By identifying specific ways in which modeling decisions affect resulting information quality, we hope to catalyze research on mechanisms to address the described negative consequences and design better systems.

The Future of User-Generated Content. We have identified some novel IQ challenges in UGC, and shown how they can be addressed by applying fundamental principles of ontology and human cognition. We have demonstrated empirically that, unless data are collected in a way that accommodates unanticipated user input, it may be deficient. In short, to the extent possible, conceptual modeling for applications harnessing UGC (e.g., crowdsourcing, social media) should be both expertise- and use-agnostic.

To implement expertise- and use-agnostic information systems (and thus to increase the quality of data generated from social media and crowdsourcing activities), traditional assumptions of class-based conceptual models need to be reconsidered. Our research demonstrates the potential negative impact of constrained data collection on the accuracy of nonexpert classifications. The preference for, and accuracy of, basic-level (compared to more specialized) classification from data contributors demonstrates the inherent trade-off between accuracy and usefulness in UGC. For information to be useful to sponsors, a greater level of classification specificity is often expected from the crowd. However, nonexperts cannot classify accurately at that level; they can perform much better at basic-level classification. As we show, there is a greater tendency in both free-form and constrained tasks to respond at the basic level, and basic-level responses are significantly more accurate than those at more specific levels.

To mitigate this usefulness-accuracy trade-off, it is of course possible to design a system using userpreferred (e.g., basic-level or some other equivalent category) classes only. In fact, some IS research has considered notions of “preferred class” and basiclevel categories before (see Bertino and Guerrini 1995, Raccoon and Puppydog 1998). We have shown empirically some IQ benefits of modeling information using basic-level categories. This can inform the theory and practice of conceptual modeling, in which choosing appropriate classes is considered essential (Parsons and Wand 2008). At the same time, our results identify a shortcoming of this approach: striving for classes that are more natural to nonexpert contributors increases information loss.

Our research suggests that contributors classify better at the basic level than at more specific levels due to higher familiarity with the identifying characteristics of basic-level classes. However, we did not explicitly assess whether and how contributors were familiar with a particular classification level. Indeed, we dealt with a context (nonexperts participating in citizen science) in which the operating assumption was that contributors were, in general, unfamiliar with the domain. Further research is needed to explicitly examine the relationship between familiarity and classification accuracy in domains in which a higher level of familiarity can be expected.

Implications for Crowd IQ. Our research also points to the potential of an alternative data structure, based on attributes and instances, to improve crowd IQ. By allowing instances to be stored independent of any classification, an application does not a priori constrain the potential information that can be stored. Thus, contributors can supply attributes based on their levels of domain expertise without having to pass a (potentially incorrect) classification judgment. Such an approach assumes neither a particular use of the data nor a minimal level of domain expertise and is, in that sense, use- and expertise-agnostic.

Once several attributes are recorded, a system can match them with pre-existing sets of identifying attributes for a phenomenon (such as biological species or an e-commerce product category), and infer a class or ask for additional attributes that can be deduced from those previously supplied. The final attribute set could match a class or simply be recorded independent of any class. This approach avoids inherent IQ deficiencies of class-based information models.

This research demonstrates a context in which instance-and-attribute based data collection and storage can lead to higher quality information for those who benefit from UGC. The approach is clearly useful when contributors lack domain knowledge or do not share the conceptual models (class structures) of information consumers. Additionally, where there is the opportunity to capture a diverse range of instance information (attributes that would not be expressed in a shared conceptual model), an instance-and-attribute approach offers flexibility that cannot be achieved using a predetermined class structure. Such flexibility is likely to be valuable when there is a reasonable prospect of using information for purposes other than those envisioned when a system was designed. It can be combined with a traditional class-based approach (which might also include basic-level classes) when there is a range from novice to expert contributors, who can be identified when contributions are reported. In addition, experts who classify at a fine level can also be given opportunities to report additional attribute information.

Future Research: Addressing Challenges to Instance-and-Attribute Approaches. Notwithstanding the advantages suggested above, the instance-andattribute approach to crowd IQ has limitations. One challenge is managing a large number of attributes.

As with classes, attributes of interest may not all be known at the time a system is designed. With a potentially very large set of attributes, it is necessary to devise mechanisms to guide contributors to select from available attributes. This may necessitate grouping attributes in some way, thus negating some of the potential benefits of an attribute-based model.

Another issue when allowing contributors to report attributes in a relatively unconstrained manner is standardizing data to make it amenable to analysis. In particular, when users are free to specify attributes, heterogeneity in reporting is likely to result in observations with (slightly) different names for semantically equivalent attributes (synonymy). This limitation can be addressed at the input and postprocessing levels. On input, it is possible to guide contributors to attributes by displaying potential matches for partially specified attributes and allowing contributors to select from them (without constraining users to these options). Alternatively, similar attributes can be compared after being collected using techniques such as word stemming to find matches (Porter 1980). One area for future research is to examine the effectiveness of techniques for standardizing attributebased data.

A further challenge lies in developing tools to make effective use of attribute-based data, beginning with simple query tools. Currently, relational databases are queried with class-based languages (such as SQL). However, because attribute data might not be stored in class-based structures, attribute-oriented querying is required. A query algebra for instance-attribute data, such as that proposed by Parsons and Wand (2000) and implemented in the instance-based Query Language (iQL) (Parsons and Su 2004), may be useful in supporting instance-and-attribute oriented queries.

Implications for Traditional Organizational Applications. Although we have framed this work in terms of UGC, it can also be applied to traditional corporate systems when information about entities might be used for purposes not anticipated when a system was designed. For example, if the sole purpose of an asset management system is to keep track of accounting information about assets, a traditional class-based structure might be adequate. If, however, it is discovered that the performance of assets depends on the conditions under which they are used, but this relationship was not anticipated when the (class-based) asset management system was designed, the system would need to be redesigned to capture additional attributes of assets reflecting the conditions of use (entailing a detailed analysis of the kinds of conditions that matter and the specific impact on attributes of assets). In contrast, an instance-and-attribute based system would capture additional attributes of specific assets independent of any classification. Such an approach could foster new ways of conceptualizing phenomena in a seemingly familiar and well understood domain.

While the present study assumed a particular context, namely an online environment and UGC, we believe the arguments and findings apply more generally. Many enterprise-wide and interorganizational IS integrate large and often heterogeneous views of data (Vitale and Johnson 1988, Zhu and Wu 2011). Much like the UGC setting explored in this paper, such integration creates the possibility of underrepresenting the perspectives of many individual data contributors. As Kent (1978, p. 203) noted: “we can share a common enough view of [reality] for most of our working purposes, so that reality does appear to be objective and stable 0 0 0 0 But the chances of achieving such a shared view become poorer when we try to encompass broader purposes, and to involve more people.”

Our research demonstrates a connection between conceptual modeling grammars and IQ. Traditionally, conceptual modeling and IQ have been considered quite different domains. Conceptual modeling research explored effective domain representations (Mylopoulos 1998, Olivé 2007, Parsons and Wand 2008, Wand and Weber 2002), while IQ research examined data accuracy, completeness, and fitness for use in already designed systems (Lee et al. 2006, Pipino et al. 2002, Tayi and Ballou 1998, Wang and Strong 1996). Novel IQ challenges in user-generated data sets (e.g., information loss) illustrate a critical role for conceptual modeling in information quality, which is likely to be applicable in internal corporate settings as well as in the UGC environment. This paper provides further support for grounding conceptual modeling and IQ in fundamental theories of ontology and cognition. Furthermore, by demonstrating the importance of conducting conceptual modeling and IQ research in tandem, we call for greater consideration of information quality in future conceptual modeling research.

## Conclusions

UGC enables organizations to draw on the collective intelligence of online crowds to support analysis and decision making. Among other uses, contributions of ordinary people expand an organization’s sensor network, making it possible to collect large amounts of data from diverse audiences. Despite the ongoing effort to harness the “wisdom of crowds,” concerns about crowd IQ may significantly curtail the usefulness of user-generated data.

The online environment in which user contributions are being made is different from the traditional internal corporate environment of data management in three important ways that affect information quality. First, in a controlled environment it is possible to ensure a high level of data input quality (via training, input controls, and other measures). By contrast, in projects harnessing user input the organization often has little control over the domain expertise and motivation of potential contributors. Second, in a corporate environment, databases are generally initially designed with specific applications and uses in mind, making it possible to tailor the database design using a set of domain classes that are well understood within the organization. By contrast, the potential uses of user-generated data may not be fully known when the system is designed and deployed. Finally, traditional design assumes that the success of information systems is contingent on how well such systems capture and implement user requirements (Appan and Browne 2010). Users’ views of reality are central to seminal IQ conceptualizations (Wand and Wang 1996, Wang and Strong 1996). In crowdsourcing projects (such as those in citizen science) with a distributed, diverse, and potentially uncommitted user base, the traditional process of information requirements determination is practically unachievable.

With this research we focus on the black box of crowd IQ. By evaluating existing practices against theories of philosophy and human cognition, we hope to draw attention to a number of critical questions and provide insight on how crowd IQ can be conceptualized and improved.

## Supplemental Material

Supplemental material to this paper is available at http://dx .doi.org/10.1287/isre.2014.0537.

## Acknowledgments

This research was supported by the Alexander Graham Bell Canada Graduate Scholarship from the Natural Sciences and Engineering Research Council of Canada to the first author, a grant from the Natural Sciences and Engineering Research Council of Canada to the second author, and funding from a GEOIDE grant and the Natural Sciences and Engineering Research Council of Canada to the third author. The authors are grateful to the associate editor and three anonymous reviewers for highly constructive guidance during the review process.

## References

Agresti A (1992) A survey of exact inference for contingency tables. Statist. Sci. 7(1):131–153.

Allen G, March S (2012) A research note on representing part-whole relations in conceptual modeling. MIS Quart. 36(3):945–964.

Angles R, Gutierrez C (2008) Survey of graph database models. Comput. Surveys 40(1):1–39.

Appan R, Browne GJ (2010) Investigating retrieval-induced forgetting during information requirements determination. J. Assoc. Inform. Systems 11(5):250–275.

Arazy O, Nov O, Patterson R, Yeo L (2011) Information quality in Wikipedia: The effects of group composition and task conflict. J. Management Inform. Systems 27(4):71–98.

Ballou DP, Pazer HL (1985) Modeling data and process quality in multi-input, multi-output information systems. Management Sci. 31(2):150–162.

Ballou DP, Pazer HL (1995) Designing information systems to optimize the accuracy-timeliness tradeoff. Inform. Systems Res. 6(1):51–72.

Barsalou LW (1983) Ad hoc categories. Memory Cognition 11(3): 211–227.

Bertino E, Guerrini G (1995) Objects with multiple most specific classes. Olthoff W, ed. Proc. 9th Eur. Conf. Object-Oriented Programming (Springer, Berlin Heidelberg), 102–126.

Bonter DN, Cooper CB (2012) Data validation in citizen science: A case study from project feederwatch. Frontiers Ecology Environ. 10(6):305–307.

Brennan P, Silman A (1992) Statistical methods for assessing observer variability in clinical measures. BMJ: British Medical J. 304(6840):1491–1494.

Bunge M (1977) Treatise on Basic Philosophy: Ontology I: The Furniture of the World (Reidel, Boston).

Burton-Jones A, Meso PN (2006) Conceptualizing systems for understanding: An empirical test of decomposition principles in object-oriented analysis. Inform. Systems Res. 17(1):38–60.

Cha M, Kwak H, Rodriguez P, Ahn Y-Y, Moon S (2007) I tube, you tube, everybody tubes: Analyzing the world’s largest user generated content video system. Dovrolis C, Roughan M, eds. Proc. 7th ACM SIGCOMM Conf. Internet Measurement (ACM, New York), 1–13.

Checkland P, Holwell S (1997) Information, Systems and Information Systems: Making Sense of the Field (John Wiley & Sons, New York).

Choudhury V (1997) Strategic choices in the development of interorganizational information systems. Inform. Systems Res. 8(1):1–24.

Coleman DJ, Georgiadou Y, Labonte J (2009) Volunteered geographic information: The nature and motivation of producers. Internat. J. Spatial Data Infrastructures Res. 4:332–358.

Collins H, Evans R (2007) Rethinking Expertise (University of Chicago Press, Chicago).

Crooks A, Croitoru AA, Stefanidis A, Radzikowski J (2013) #Earthquake: Twitter as a distributed sensor system. Trans. GIS 17(1): 124–147.

Cruse DA (1977) The pragmatics of lexical specificity. J. Linguistics 13(2):153–164.

Daugherty T, Eastin M, Bright L (2008) Exploring consumer motivations for creating user-generated content. J. Interactive Advertising 8(2):16–25.

Dickinson JL, Zuckerberg B, Bonter DN (2010) Citizen science as an ecological research tool: Challenges and benefits. Ann. Rev. Ecology, Evolution, Systematics 41:112–149.

Doan A, Ramakrishnan R, Halevy AY (2011) Crowdsourcing systems on the World-Wide Web. Comm. ACM 54(4):86–96.

Flanagin A, Metzger M (2008) The credibility of volunteered geographic information. GeoJournal 72(3):137–148.

Fortson L, Masters K, Nichol R, Borne K, Edmondson E, Lintott C, Raddick J, Schawinski K, Wallin J (2012) Galaxy zoo: Morphological classification and citizen science. Way MJ, Scargle JD, Ali KM, Srivastava AN, eds. Advances in Machine Learning and Data Mining for Astronomy (CRC Press, Boca Raton, FL), 213–236.

Foster-Smith J, Evans SM (2003) The value of marine ecological data collected by volunteers. Biol. Conservation 113(2):199–213.

Gallagher K, Parsons J, Foster KD (2001) A tale of two studies: Replicating advertising effectiveness and content evaluation in print and on the Web. J. Advertising Res. 41(4):71–81.

Gallaugher J, Ransbotham S (2010) Social media and customer dialog management at Starbucks. MIS Quart. Executive 9(4): 197–212.

Galloway AWE, Tudor MT, Haegen WMV (2006) The reliability of citizen science: A case study of Oregon white oak stand surveys. Wildlife Soc. Bull. 34(5):1425–1429.

Gangi PMD, Wasko M, Hooker R (2010) Getting customers’ ideas to work for you: Learning from Dell how to succeed with online user innovation communities. MIS Quart. Executive 9(4): 163–178.

Gao G, McCullough JS, Agarwal R, Jha AK (2010) Are doctors created equal? An investigation of online ratings by patients Proc. Workshop Inform. Systems Econom. St. Louis, 1–6.

Gemino A, Wand Y (2005) Complexity and clarity in conceptual modeling: Comparison of mandatory and optional properties. Data Knowledge Engrg. 55(3):301–326.

Girres J-F, Touya G (2010) Quality assessment of the French openstreetmap data set. Trans. GIS 14(4):435–459.

Goodchild M (2007) Citizens as sensors: The world of volunteered geography. GeoJournal 69(4):211–221.

Guizzardi G (2010) Theoretical foundations and engineering tools for building ontologies as reference conceptual models. Semantic Web 1(1):3–10.

Haklay M (2010) How good is volunteered geographical information? A comparative study of openstreetmap and ordnance survey data sets. Environ. Planning B 37(4):682–703.

Hamel NJ, Burger AE, Charleton K, Davidson P, Lee S, Bertram DF, Parrish JK (2009) Bycatch and beached birds: Assessing mortality impacts in coastal net fisheries using marine bird strandings. Marine Ornithology 37(1):41–60.

Hand E (2010) People power. Nature 466(7307):685–687.

Hill S, Ready-Campbell N (2011) Expert stock picker: The wisdom of (the experts in) crowds. Internat. J. Electronic Commerce 15(3):73–101.

Hirschheim R, Klein HK, Lyytinen K (1995) Information Systems Development and Data Modeling: Conceptual and Philosophical Foundations (Cambridge University Press, New York).

Hochachka WM, Fink D, Hutchinson RA, Sheldon D, Wong W-K, Kelling S (2012) Data-intensive science applied to broad-scale citizen science. Trends Ecology Evolution 27(2):130–137.

Jolicoeur P, Gluck MA, Kosslyn SM (1984) Pictures and names: Making the connection. Cognitive Psych. 16(2):243–275.

Jones RA, Rosenberg S (1974) Structural representations of naturalistic descriptions of personality. Multivariate Behav. Res. 9(2): 217–230.

Juran JM, Gryna FM (1988) Juran’s Quality Control Handbook (McGraw-Hill, New York).

Kahn BK, Strong DM, Wang RY (2002) Information quality benchmarks: Product and service performance. Comm. ACM 45(4): 184–192.

Kent W (2000) Data and Reality, 2nd ed. (1st Books, Bloomington, IN).

Kim S, Robson C, Zimmerman T, Pierce J, Haber EM (2011) Creek watch: Pairing usefulness and usability for successful citizen science. Tan D, ed. Proc. 2011 Ann. Conf. Human Factors Comput. Systems (ACM, New York), 2125–2134.

Kittur A, Chi E, Pendleton B, Sun B, Mytkowicz T (2007) Power of the few vs. wisdom of the crowd: Wikipedia and the rise of the bourgeoisie. Rosson MB, ed. Proc. CHI 2007 (ACM, New York), 1–9.

Krumm J, Davies N, Narayanaswami C (2008) User-generated content. IEEE Pervasive Comput. 7(4):10–11.

Lambert NM, Graham SM, Fincham FD (2009) A prototype analysis of gratitude: Varieties of gratitude experiences. Personality Soc. Psych. Bull. 3(9):1193–1207.

Landis R, Koch G (1977) The measurement of observer agreement for categorical data. Biometrics 33(1):159–174.

Lee YW (2003) Crafting rules: Context-reflective data quality problem solving. J. Management Inform. Systems 20(3):93–119.

Lee YW, Pipino L, Strong DM, Wang RY (2004) Process-embedded data integrity. J. Database Management 15(1):87–103.

Lee YW, Pipino LL, Funk JD, Wang RY (2006) Journey to Data Quality (MIT Press, Cambridge, MA).

Lukyanenko R, Parsons J, Wiersma Y (2011) Citizen science 2.0: Data management principles to harness the power of the crowd. Jain H, Sinha A, Vitharana P, eds. Service-Oriented Perspectives in Design Science Research, Vol. 6629 (Springer, Berlin Heidelberg), 465–473.

Mackechnie C, Maskell L, Norton L, Roy D (2011) The role of “Big Society” in monitoring the state of the natural environment. J. Environ. Monitoring 13(10):2687–2691.

Majchrzak A, More P (2011) Emergency! Web 2.0 to the rescue! Comm. ACM 54(4):125–132

Markus M, Steinfield CW, Wigand RT (2006) Industry-wide information systems standardization as collective action: The case of the US residential mortgage industry. MIS Quart. 30(Special Issue):439–465.

Mason R, Mitroff I (1973) A program for research on management information systems. Management Sci. 19(5):475–487.

McCloskey M, Glucksberg S (1978) Natural categories: Well defined or fuzzy sets? Memory Cognition 6(4):462–472.

Murphy G, Smith E (1982) Basic-level superiority in picture categorization. J. Verbal Learn. Verbal Behav. 21(1):1–20.

Murphy GL (2004) The Big Book of Concepts (MIT Press, Cambridge, MA).

Mylopoulos J (1992) Conceptual modeling and telos. Loucopoulos P, Zicari R, eds. Conceptual Modeling, Databases, and CASE: An Integrated View of Information Systems Development (John Wiley & Sons, Inc., New York), 49–68.

Mylopoulos J (1998) Information modeling in the time of the revolution. Inform. Systems 23(3–4):127–155.

Nelson XJ, Fijn N (2013) The use of visual media as a tool for investigating animal behaviour. Animal Behav. 85(3):525–536.

Nov O, Arazy O, Anderson D (2011) Technology-mediated citizen science participation: A motivational model. Proc. Fifth Internat. AAAI Conf. Weblogs Soc. Media, Barcelona, Spain, 249–256.

Olivé A (2007) Conceptual Modeling of Information Systems (Springer, Berlin Heidelberg).

Parsons J (1996) An information model based on classification theory. Management Sci. 42(10):1437–1453.

Parsons J, Su J (2004) Exploiting instance-based data structures with iQL. Proc. Workshop Inform. Tech. Systems, 206–211.

Parsons J, Wand Y (1997) Choosing classes in conceptual modeling. Comm. ACM 40(6):63–69.

Parsons J, Wand Y (2000) Emancipating instances from the tyranny of classes in information modeling. ACM Trans. Database Systems 25(2):228–268.

Parsons J, Wand Y (2008) Using cognitive principles to guide classification in information systems modeling. MIS Quart. 32(4): 839–868.

Parsons J, Lukyanenko R, Wiersma Y (2011) Easier citizen science is better. Nature 471(7336):37.

Pipino LL, Lee YW, Wang RY (2002) Data quality assessment. Comm. ACM 45(4):211–218.

Porter F (1980) An algorithm for suffix stripping. Program: Electronic Library Inform. Systems 14(3):130–137.

Posner MI (1993) Foundations of Cognitive Science (MIT Press, Cambridge, MA).

Raccoon LSB, Puppydog POP (1998) A middle-out concept of hierarchy (or the problem of feeding the animals). ACM SIGSOFT Software Engrg. Notes 23(3):111–119.

Recker J, Rosemann M, Green P, Indulska M (2011) Do ontological deficiencies in modeling grammars matter? MIS Quart. 35(1):57–79.

Redman TC (1996) Data Quality for the Information Age (Artech House, Norwood, MA).

Reeves CA, Bednar DA (1994) Defining quality: Alternatives and implications. Acad. Management Rev. 19(3):419–445.

Rosch E (1978) Principles of categorization. Rosch E, Lloyd B, eds. Cognition and Categorization (John Wiley & Sons Inc., Hoboken, NJ), 27–48.

Rosch E, Mervis CB, Gray WD, Johnson DM, Boyesbraem P (1976) Basic objects in natural categories. Cognitive Psych. 8(3): 382–439.

Rosenberg S, Jones R (1972) A method for investigating and representing a person’s implicit theory of personality: Theodore Dreiser’s view of people. J. Personality Soc. Psych. 22(3):372–386.

Rowland K (2012) Citizen science goes “extreme.” Nature News, Retrieved December 9, 2013, http://www.nature.com/news/ citizen-science-goes-extreme-1.10054.

Shanks G, Tansley E, Nuredini J, Tobin D, Weber R (2008) Representing part-whole relations in conceptual modeling: An empirical evaluation. MIS Quart. 32(3):553–573.

Silvertown J (2010) Taxonomy: Include social networking. Nature 467(7317):788.

Sim J, Wright CC (2005) The kappa statistic in reliability studies: Use, interpretation, and sample size requirements. Physical Therapy 85(3):257–268.

Stonebraker M, Abadi DJ, Batkin A, Chen X, Cherniack M, Ferreira M, Lau E, Lin A, Madden S, O’Neil E, O’Neil P, et al. (2005) C-store: A column-oriented DBMS. Böhm K, Jensen CS, Haas LM, Kersten ML, Larson P-Å, Ooi BC, eds. Proc. 31st Internat. Conf. Very Large Data Bases (ACM, New York), 553–564.

Susarla A, Oh J-H, Tan Y (2012) Social networks and the diffusion of user-generated content: Evidence from YouTube. Inform. Systems Res. 23(1):23–41.

Tanaka JW, Taylor M (1991) Object categories and expertise: Is the basic level in the eye of the beholder? Cognitive Psych. 23(3):457–482.

Tayi GK, Ballou DP (1998) Examining data quality. Comm. ACM 41(2):54–57.

Tsichritzis DC, Lochovsky FH (1982) Data Models (Prentice-Hall, Englewood Cliffs, NJ).

Vitale MR, Johnson H (1988) Creating competitive advantage with interorganizational information systems. MIS Quart. 12(2): 152–165.

Wand Y, Wang RY (1996) Anchoring data quality dimensions in ontological foundations. Comm. ACM 39(11):86–95.

Wand Y, Weber R (1990) An ontological model of an information system. IEEE Trans. Software Engrg. 16(11):1282–1292.

Wand Y, Weber R (2002) Research commentary: Information systems and conceptual modeling—A research agenda. Inform. Systems Res. 13(4):363–376.

Wand Y, Monarchi DE, Parsons J, Woo CC (1995) Theoretical foundations for conceptual modelling in information systems development. Decision Support Systems 15(4):285–304.

Wang RY (1998) A product perspective on total data quality management. Comm. ACM 41(2):58–65.

Wang RY, Strong DM (1996) Beyond accuracy: What data quality means to data consumers. J. Management Inform. Systems 12(4): 5–33.

Wattal S, Schuff D, Mandviwalla M, Williams CB (2010) Web 2.0 and politics: The 2008 U.S. presidential election and an e-politics research agenda. MIS Quart. 34(4):669–688.

Weber R (1996) Are attributes entities? A study of database designers’ memory structures. Inform. Systems Res. 7(2):137–162.

Wiersma YF (2010) Birding 2.0: Citizen science and effective monitoring in the Web 2.0 world. Avian Conservation Ecology 5(2):1–9.

Wiggins A, Crowston K (2011) From conservation to crowdsourcing: A typology of citizen science. Sprague RH Jr, ed. Proc. 44th Hawaii Internat. Conf. System Sci. (IEEE, Piscataway, NJ).

Wiggins A, Newman G, Stevenson RD, Crowston K (2011) Mechanisms for data quality and validation in citizen science. Proc. “Comput. Citizen Sci.” Workshop, Stockholm, 1–6.

Wiggins A, Bonney R, Graham E, Henderson S, Kelling S, LeBuhn G, Litauer R, Lots K, Michener W, Newman G (2013) Data management guide for public participation in scientific research. DataOne Working Group 1–41. Retrieved December 5, http://www.dataone.org/sites/all/documents/DataONE-PPSR -DataManagementGuide.pdf.

Winograd T, Flores F (1986) Understanding Computers and Cognition: A New Foundation for Design (Ablex Pub, Norwood, NJ).

Wisniewski EJ, Murphy G (1989) Superordinate and basic category names in discourse: A textual analysis. Discourse Processes 12(2):245–261.

Wyssusek B (2006) On ontological foundations of conceptual modelling. Scandinavian J. Inform. Systems 18(1):63–80.

Zhu H, Wu H (2011) Quality of data standards: Framework and illustration using XBRL taxonomy and instances. Electronic Markets 21(2):129–139.

Zwass V (2010) Co-creation: Toward a taxonomy and an integrated research perspective. Internat. J. Electronic Commerce 15(1):11–48.
