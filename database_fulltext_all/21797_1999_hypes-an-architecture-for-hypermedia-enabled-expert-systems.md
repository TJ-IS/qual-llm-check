---
otero_id: 21797
otero_key: "CJZ89GYF"
title: "HypEs: an architecture for hypermedia-enabled expert systems"
authors: "Y.Alex Tung; Ram D Gopal; James R Marsden"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00057-3"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# HypEs: an architecture for hypermedia-enabled expert systems

Y. Alex Tung <sup>a,1</sup>, Ram D. Gopal <sup>b,)</sup>, James R. Marsden <sup>b,2</sup>

<sup>a</sup> Department of Management<sup>r</sup>MIS, UniÕersity of NeÕada Las Vegas, Las Vegas, NV 89154, USA <sup>b</sup> Department of Operations and Information Management, UniÕersity of Connecticut, Storrs, CT 06269, USA

Accepted 9 September 1999

## Abstract

Expert systems and hypermedia constitute two important technologies for organizations to create, store, and manage information products. The purpose of our research is to develop an architectural blueprint for the construction of hypermedia-enabled expert systems. We propose an architecture termed HypEs HypŽ . ermedia-enabled Expert System for the development of media-rich expert systems. The integration of hypermedia technologies and expert systems can provide significant potential benefits by enabling the storage and manipulation of non-textual knowledge, enhancing the effectiveness of both knowledge acquisition from the sources of expertise and knowledge transfer to non-expert users. An experimental analysis that contrasts the hypermedia-enabled and text-restricted expert systems provides results that underscore the usefulness of hypermedia techniques in enhancing the effectiveness of expert systems in practical applications. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Expert system; Hypermedia; System architecture; Knowledge-based system

## 1. Introduction

Traditional expert systems require that information input and output be in textual form 28 . While<sup>w</sup> <sup>x</sup> this remains the rule, there are several applications that rely on expertise that is non-textual in nature. Examples of such applications include ones based on visual reasoning 5 , on acoustic analysis 26 , and on <sup>w x</sup> <sup>w</sup> <sup>x</sup> temporal and spatial reasoning involving complex interactions among related components 8 . Current<sup>w</sup> <sup>x</sup> expert systems approximate such inherently nontextual knowledge by a conversion or ‘‘translation’’ process, that is, converting knowledge from nontextual to textual for system input. System output is commonly left in textual form with any required translation process left to the system user. Since the mapping from non-textual to textual is most certainly not one-to-one, each such translation is inherently subject to inconsistencies, knowledge confusion, and<sup>r</sup>or knowledge loss 18,29 .<sup>w</sup> <sup>x</sup>

During the period in which expert system developers have increasingly recognized the importance of non-textual knowledge, there have been numerous investigations into possible uses of hypermedia technologies. Examples of application areas include education and training 3 , computer problem diagnosis<sup>w</sup> <sup>x</sup> <sup>w x</sup> <sup>w x</sup> <sup>w x</sup> 10 , market trading 21 , conferencing 13 , and health management 7 . The question we address in<sup>w</sup> <sup>x</sup> our work is the potential use of hypermedia in the development of next generation expert systems. That is, can hypermedia knowledge representations be the vehicle for direct knowledge input<sup>r</sup>output that enables expert systems to operate seamlessly and avoid the pitfalls of contrived textual<sup>r</sup>non-textual translation schemes?

While possible uses of hypermedia technology within the framework of expert systems have recently been suggested by several researchers 23 , <sup>w</sup> <sup>x</sup> none has taken an integrated or comprehensive approach. A related stream of research investigates the use of expert systems in improving hypermedia technologies. The focus of our work is on how hypermedia technologies can aid in the functionality of an expert system. Ragusa 27 suggested, but did not <sup>w</sup> <sup>x</sup> demonstrate, that the use of hypermedia can offer significant benefits in certain expert system applications. Bielawski and Lewand 2 utilized multimedia<sup>w</sup> <sup>x</sup> technologies for the presentation of expertise to the users. Mao et al.’s 24 Hyper-FINALYZER expert<sup>w</sup> <sup>x</sup> system allowed for the representation of the relationships and structures in the knowledge domain using multimedia graphical browsers. Gaines and Linster <sup>w x</sup> <sup>w x</sup> 11 and Lee et al. 17 proposed the use of multimedia to aid in the knowledge acquisition process. Fuerst et al. 10 and Tung et al. 31 suggested that<sup>w x</sup> <sup>w x</sup> the potential exists for the use of hypermedia technology in major facets of expert systems, including user interface, knowledge acquisition, and explanation of expertise. The inherent appeal of hypermedia is that it permits the management of expertise in its native or near-native format, without the need to resort to conversion to text-based formats.

In this paper, we develop an architectural blueprint for the construction of hypermedia-enabled expert systems. We propose an architecture termed HypEs Ž . Hypermedia-enabled Expert System for the development of media-rich expert systems. A key component of the architecture is the Knowledge Manager that enables the media objects to directly manipulate knowledge in native or near-native formats. Knowledge Manager provides services that can be employed to enable the hypermedia objects to perform a variety of tasks, ranging from enhanced communication with end users to embedding knowledge directly into the media objects.

An experimental study is utilized to demonstrate potential performance differentials of text-restricted and hypermedia-based expert systems. The experimentation illustrates the potential benefits of the use of hypermedia technologies within the expert system framework. This initial experimental analysis provides a critical first step in empirically testing our argument for the HypEs approach. Though our arguments may appear reasonable, it is crucial that we seek empirical verification see examples of suchŽ experimental analysis in Refs. 16,22 . Our argu-<sup>w</sup> <sup>x</sup>. ment follows basic philosophy of science principles. Arguments other than tautologies must be subjected to empirical verification. Without rigorous testing, verbal arguments remain as untested assumptions. Our initial experiments provide only the first step in rigorous empirical testing.

The HypEs approach is presented as a blueprint that has general application in ES development. We refrain from explicitly constructing an ES development shell because this would impose restrictions and run counter to a general and flexible blueprint. A shell requires details on object types and restricts the breadth of application. Our general blueprint HypEs can serve as the basis to generate a class of development shells. This generation of a class of shells is a subsequent step that is beyond the scope of this presentation.

The remainder of the paper is organized as follows. Section 2 motivates the importance of hypermedia technologies for expert system development. The section includes two experimental illustrations of translation errors inherent in moving from nontextual to textual representations. Section 3 is the key section of the paper, providing the development and explanation of our HypEs architecture. Section 4 provides a prototype expert system and an empirical study that underscores the potential practical benefits of our HypEs architecture. Section 5 offers brief concluding remarks.

## 2. Motivation

We use two initial experimental studies to help motivate an understanding of the need for hypermedia in expert system development. The experiments highlight the inherent problems that arise in the human translation between textual and multimedia data representations. This situation often arises in knowledge assimilation and dissemination activities in traditional expert system applications. Reliance on experts and users to create textual equivalents may result in an inconsistent, incomplete, or false knowledge base and may lead to misleading advice to expert system end-users. Our two experiments evaluate human processing of image data where the primary task is to create a textual representation of certain aspects of the image. One experiment focused on the ensuing inaccuracies. The other experiment included the capability to identify inconsistencies.

In the first experiment, 16 subjects were provided a campus map non-textual information of a majorŽ . university and a brief questionnaire with 18 questions relating to the map. The questions posed were related to major landmarks depicted in the map and their relative proximity. The subjects’ task was to examine the map and provide answers to the 18 specific questions within a 10-min time period. That is, the subjects were required to utilize non-textual information as a basis for providing text-based responses. The subjects were carefully screened to ensure that they were not familiar with the university campus. A financial incentive, based on the number of correct answers, was used to improve the effort expended by the subjects in answering the questions.

Fig. 1 illustrates the percentage of incorrect answers across all subjects for each question.

The overall average inaccuracy rate of 20.5% underscores errors in the human translation process. The individual performance of subjects varied from 0% to 40% inaccuracy rates, indicating significant inconsistencies in the performance. As Fig. 1 illustrates, the errors were not concentrated on a few of the questions but were present in a significant majority of them. This points to the subjects’ difficulties in image-to-text translations rather than a lack of clear exposition in framing a few of the questions.

The design of the second experiment was structured to include capabilities to investigate possible inconsistencies, as well as inaccuracies in imageto-text translations. Disparities that arise during repetitive translations of the same data by an individual subject and those that arise across the subjects were examined. The design of the experiment is as follows.

Each experimental image consisted of three distinct identifiable zones. The zones were color coded to ensure that each zone was clearly identifiable and all zones were distinguishable from each other. Six different images were created and each was duplicated once unknown to the subjects to provide a Ž . total of 12 images for the experimental analysis. An image processing program was developed to process each image and accurately record the proportion of each zone in the image. This formed the benchmark to evaluate the accuracy of the responses from the human subjects.

![](/api/attachments/CJZ89GYF/fulltext/images/4709c99e7dba666977629e4bc7e3f90e486def877308d8b6c6436a888278d2ed.jpg)  
Fig. 1. Inaccuracies in textual interpretation.

![](/api/attachments/CJZ89GYF/fulltext/images/5854874ef5636b01e42d4c7f83bc540673c0ee725ccd4c43ef02e8ba7a6d3b22.jpg)  
Fig. 2. Deviation across subjects.

Twenty-eight subjects participated in this experiment. None of the subjects in this experiment participated in the earlier experiment. The 12 images were presented to each subject in a random order. For each image, the subjects’ task was to provide their best estimate of the proportion of each identifiable zone upon a visual examination of the image. Note that each subject’s session involves six distinct images, each of which is inspected twice by the subject. Interestingly, no subject noted the replication of the images. As in the first experiment, a financial incentive based on performance provided the necessary motivation for the subjects. No time constraints were imposed for the completion of the tasks.

The accuracy rate or percent deviation for eachŽ . identifiable zone is defined as: actual <sup><</sup>Ž <sup>y</sup> estimated proportion.<sup><</sup>)100<sup>r</sup>Ž . actual proportion . The overall average deviation across all estimations performed by each subject is illustrated in Fig. 2. The results vary from about 10% deviation to over 85% deviation, suggesting significant discrepancies in how individuals process and translation visual information. Besides variations across individuals, significant discrepancies are observed even when an individual re-analyzes the same visual data. As each individual was asked to provide estimates for the same image twice, an analysis of identical pairs of images highlights such discrepancies. The metric utilized to capture these discrepancies is: first estimate of a zone<sup><</sup>Ž <sup>y</sup>second estimate of the same zone.<sup><</sup>)100<sup>r</sup>Žfirst estimate of the zone . The overall average discrep-.

![](/api/attachments/CJZ89GYF/fulltext/images/fece6d9c685d843c69990c34ebfc2b3c1cd7a8fb20be4e7cdc301c7a731e6b58.jpg)  
Fig. 3. Inconsistencies within subjects.

ancy for each of the six distinct images is illustrated in Fig. 3. Variations of up to 25% suggest a lack of consistency by individuals while performing identical image processing and translation activities.

Together the two experiments help illustrate the inadequacies in image-to-text translations that are performed by human subjects. Reliance on humans, both experts and users, to perform these activities has rendered the traditional text-restricted expert systems less useful. Incorporation of hypermedia technologies offers the potential to overcome these problems and enhance the effectiveness of expert systems. The architectural details that arise in the integration of the two technologies are the focus of Section 3.

## 3. HypEs architecture

In this section, we develop the architectural foundations for the development of hypermedia-enabled expert systems. HypEs is designed to employ multiple media for knowledge acquisition, storage, and user interface activities. We begin our discussion with a description of media taxonomy.

## 3.1. Media taxonomy

The media objects can be classified along two dimensions, reality and complexity. The media objects on the reality dimension are real and<sup>r</sup>or abstract. The distinction is based on a mapping of the media object with the external world. If every element of the media object corresponds to an element on the representative object in the external world, the media object is termed real. Otherwise, it is termed abstract. Complexity of a media object is determined based on the effort expended in the computer storage and manipulation for knowledge activities.

The commonly used media types are text, sound, image, graphics, animation, and motion video, briefly described as follows:

Text: Most commonly used data type; exhibits the least levels of complexity for computer manipulation. Text can be real or abstract depending on the context. For example, the textual representation of height of individuals is real and musical talent is abstract.

Sound: Consumes more computer resources than the text object. Sound can also be real or abstract depending on the context. Noise from an automobile engine and heartbeat heard through a stethoscope are examples of real sound; computer simulated voice is an example of abstract sound.

Image: Pictures which result from a mechanical mapping of the external world into two dimensions <sup>w</sup> <sup>x</sup>6 . This data object is real and consumes more computer resources than the text object.

Graphics: Pictures that are not images 6 . By<sup>w</sup> <sup>x</sup> definition, they are abstract. Two forms of graphics, charts and diagrams, are of particular interest in the expert system context. Charts are based on numerical data for example, a bar chart and diagrams for Ž . Ž example, data flow diagrams are graphics con- . structed based on a limited set of two dimensional shapes that prescribe to preset diagrammatic conventions 9 . The general graphic data type assumes a <sup>w</sup> <sup>x</sup> complexity level similar to an image. Some elements of charts and diagrams can be represented textually and thus they require lesser computing resources.

Animation: Brings static objects to life; can be used to add realism to artificial objects or surrealism to images of real objects 14 . We adopt the defini- <sup>w</sup> <sup>x</sup> tion that animation is a collection images, graphics and sound where at least one object is abstract. Therefore, animation is abstract and more complex than its individual constituents; and

Motion Õideo: Pictures of an event captured and recorded over a period of time 14 ; can be viewed as<sup>w</sup> <sup>x</sup> a collection of images and real sound that is temporally sequenced. Therefore, motion video is real and complex as it consumes significant computing resources.

Fig. 4 provides a graphical illustration of the media objects on the two classification dimensions and the interrelationships among the objects. These media objects are employed by the hypermedia-enabled expert system and the details are described in the following.

## 3.2. Expert system

Turban 32 identified four components of an <sup>w</sup> <sup>x</sup> expert system — knowledge source, knowledge base, user interface and explanation facility. Fig. 5 illustrates the component view of the HypEs architecture.

![](/api/attachments/CJZ89GYF/fulltext/images/012124cda1301c5cfbd9fbc331da200153f19125afa609269938d44dec6ca2f3.jpg)  
Fig. 4. A knowledge taxonomy of media objects.

The expert system components interface with the media objects via the Knowledge Manager.

## 3.2.1. Knowledge source

The typical knowledge sources for expertise are experts and documentation. In a number of applications, the knowledge sources reside on documents, which in their natural formats are available as multimedia objects. Examples include angiograms and aerial views of locations that are image-based 29 ,<sup>w</sup> <sup>x</sup> sounds from malfunctioning high-pressure air supply system 26 , system diagrams of complex engine <sup>w</sup> <sup>x</sup> parts, and time-based animated views of complex, inter-related systems such as automobiles and manufacturing systems 8 . In the case of expert system<sup>w</sup> <sup>x</sup> that performs diagnostic analysis of angiograms, the typical experts are radiologists and cardiologists 20 .<sup>w</sup> <sup>x</sup> Angiograms are X-ray photographs of the heart taken by a rapid-exposure cine cinema immediately after radiographic contrast is injected into the coronary arteries. These experts use perceptual reasoning and are often unable to give unambiguous verbal descriptions or to explain reasoning involved in the interpretation of the angiogram 29 .<sup>w</sup> <sup>x</sup>

![](/api/attachments/CJZ89GYF/fulltext/images/170167694f97e3b5c61e9f6e7523aab0b31e750bef58d2fc0c678a295ac23006.jpg)  
Fig. 5. HypEs architecture — a component view.

An expert system that permits knowledge acquisition directly through the angiograms should significantly enhance the effectiveness of the diagnosis.

When documentation is naturally available in multiple media formats, HypEs can directly access these sources and provide an interface to the experts to manipulate these objects for knowledge extraction. This allows experts to function in their natural environments and utilize their perceptual, visual, acoustic reasoning abilities and thus overcome ambiguities and inaccuracies associated with verbalizing such knowledge to create text-restricted systems. The experts interact with HypEs through the Knowledge Manager that incorporates pattern recognition and segmentation, feature extraction, object description and comparison, and other algorithms that are embedded in the object operators. This permits the expert to focus explicitly on the knowledge domain and ignore the algorithmic details on how efficiently and effectively to translate the domain knowledge into computer-understandable formats.

## 3.2.2. Knowledge base

The knowledge base stores the knowledge that is acquired from the knowledge source. The acquired knowledge is typically stored in a rule-based or frame-based format. HypEs can incorporate media objects in the knowledge base and embed knowledge directly in the stored media objects. The media-rich knowledge base incorporates expert heuristics. For example, production rules might operate on the existence of certain patterns in the media objects, or characteristics of a media object, or a comparison of an object under study with a reference object. An example of a possible production rule that features image analysis is provided in Fig. 6.

## 3.2.3. User interface

The user interface in most traditional expert systems is centered on the keyboard and the computer screen. The consulting session typically involves text-restricted dialogue between the system and the user. Input information that naturally exists in nontextual formats has to be processed and translated to textual format by the user. As a result the advice or the results provided by the expert system are critically dependent on the efficacy with which the user can process and translate non-textual information. Inaccuracies, ambiguities and inconsistencies that tend to arise in such translations potentially hinder the practicality of expert systems in some application domains. Leonard-Barton and Sviokla 18 describe a<sup>w</sup> <sup>x</sup> failed prototype expert system to diagnose problems in soldering of computer components. The crucial deficiency of the prototype was that the operators who consulted with the expert system often missed the subtle irregularities in the components and thus failed to provide correct information to the expert system.

![](/api/attachments/CJZ89GYF/fulltext/images/a9c36e3514fc910853c5530310fc6d72bec467f408b4ac6eee7d3707689e5945.jpg)  
Fig. 6. A sample production rule in HypEs’s knowledge base.

HypEs is designed to provide input facilities in a variety of media formats. For example, an image of an external object or audio recording can be directly read and processed by the system. Furthermore, HypEs allows for multimodal input and preprocessing of information. Examples of multimodal inputs include multiple images of the same object from different viewpoints and augmentation of images by the addition of associated acoustic properties or explanatory textual descriptions. While possibly redundant, multimodal input can take advantage of the unique features of individual media objects in that eachŽ media object can better capture certain types of information than others . Examples of preprocessing. of information include data error checks, identification and elimination of ‘‘noise’’ and other extraneous data. Thus, HypEs provides features that work to ensure the completeness and accuracy of the information communication between the user and the system.

## 3.2.4. Explanation facility

Explanation of the expert advice can be more effective if conducted in multimodal formats 10 .<sup>w</sup> <sup>x</sup> Media such as graphics, animation and sound are more effective at conveying information that involves two or three dimensional spatial relationships, and behavior and evolution of complex systems 9 . <sup>w</sup> <sup>x</sup> Awad 1 describes an expert system that utilizes <sup>w</sup> <sup>x</sup> virtual reality to help the user experience the advice or solution in a realistic environment via visualization and sensing. One example is the explanation of statistical information through graphs. A second example is the use of computer animation to demonstrate temporal patterns such as tumor growth or developing weather conditions. HypEs provides a media-rich environment within which a plethora of multisensory capabilities can be augmented to the solutions offered by the expert system.

Fig. 7 provides a process view of HypEs. As illustrated in this figure, the proposed architecture provides valuable services to both the experts and the users in their interactions with the expert system. HypEs is designed to work with multiple media objects to garner the advantages they offer to increase the effectiveness of expert systems and the scope of the application domain. This is accomplished through the Knowledge Management component that manages the media objects and is specifically tailored for expert system development. Knowledge Manager provides services to both the experts and the non-expert users.

## 3.3. Knowledge Manager

A significant body of research in the areas of pattern recognition 4 and content-based retrieval in <sup>w</sup> <sup>x</sup> multimedia databases 25 addresses processing of<sup>w</sup> <sup>x</sup> various media objects. The technology that drives the functionality of the Knowledge Manager is derived from the techniques developed in these related bodies of research. Media analysis by Knowledge Manager involves structured processes that are employed in typical media-based applications in pattern recognition 19 .<sup>w</sup> <sup>x</sup>

These processes are the following.

Acquisition: Capture of the media object in a digital form.

Enhancement: Improvements to the quality of the media object to eliminate degradations that occur in the digitization of the object and increase the detectability of features of interest to the application. This, for example, could involve reduction of blur in an image or elimination of background noise in an audio object.

Segmentation: A typical media object contains representations of multiple items or features. This processing step involves the partitioning of media object in order to isolate items or features that are relevant for the application.

![](/api/attachments/CJZ89GYF/fulltext/images/f8ad244232576d61f13aaa752a5fcb862154a9ee49053391e7997dd8cecdf4b3.jpg)  
Fig. 7. HypEs architecture — a process view.

Analysis: Further examination of the segmented media object to obtain qualitative or quantitative information of interest.

The above guidelines are adopted by the Knowledge Manager and are specifically tailored for knowledge-related purposes. The Knowledge Manager provides services both to the expert and the user community. The components that comprise the Knowledge Manager, their significance, and the interactions with expert system functions are discussed below.

The Knowledge Manager exhibits a two-layered architecture, termed object layer and control layer, depicted in Fig. 8. The object layer houses the media objects, their associated properties and methods to manipulate these objects. The control layer provides for the management of media objects and serves as the bridge between the expert system and the object layer. As illustrated in Fig. 8, each of the layers has three components.

We explain the layers and component elements as follows.

## 3.3.1. Object layer

The object layer is the central repository of the objects employed in the expert system. The property base identifies the attributes of the media objects. These attributes constitute the basic ingredients for the analysis of the media objects. Examples include frequency and amplitude of a sound object and colors and brightness of an image object. The methods base provides the set of operators that function on the objects for feature extraction, pattern identification, object comparison and object conversion. Conversion methods act on the objects to produce another object. The resultant object can be the same object with different properties, or a different object of the same data type, or a completely different data type. Conversion methods that produce more complex objects are typically utilized for meta-knowledge creation and dissemination. Mechanisms for conversion to simpler formats are invoked during information input from the users when data is not available in its native format. Thus, the object layer provides the media toolkit that is manipulated by the control layer for expert system purposes.

![](/api/attachments/CJZ89GYF/fulltext/images/00f914a23b326ecba6ae25bef3bdf8dfc49472723e1485668c69fb412b1534db.jpg)  
Fig. 8. Knowledge manager.

## 3.3.2. Control layer

The control layer serves as a bridge between knowledge manager and expert system. It is comprised of three knowledge creation<sup>r</sup>dissemination components, each with subcomponents as follows.

Knowledge creation facility: The key purpose of this control layer component is to assist the experts in the construction of the knowledge base that relies on the object layer for knowledge storage. Its support feature permits the experts to work at higher visual and acoustic levels to derive their expertise. Thus, it obviates the need for the experts to consider the algorithmic details in transforming high level expertise to system level specifics. The knowledge base creation process follows the standard media processing stages and is outlined below.

Media acquisition for knowledge base: This stage involves digitization of the media objects that are analyzed in their native format to derive the knowledge base.

Media preprocessing: This processing stage invokes noise reduction and media enhancement algorithms to account for the discrepancies that arise in the digitization of the data. The consultation session with the experts provides the basis that drives the selection of the appropriate algorithms. The methods base from the object layer provides these algorithms that are appropriate for the application scenario.

Object specification and creation of lower complexity equiÕalents: At this processing stage, the creation facility triggers the object layer and, in conjunction with the experts, isolates features in the media objects that form the basis on which the knowledge base is created. The resulting features provide the key ingredients of the domain knowledge and thus their analysis constitutes the knowledge base. When the objects are available in their native formats, the features of interest can be automatically detected during the consultation with non-expert users by HypEs. While this is clearly preferred, there may be instances when the native objects are not available in the digital format. The onus of eliciting the features would partly shift to the non-expert users as the input information would only be available in lower level object formats. Identification of and feature extraction from lower complexity equivalent objects is also conducted in this processing stage to accommodate for such occurrences.

Knowledge base creation: This final processing stage results in the creation of the media-enabled knowledge base. The knowledge creation facility assists the experts during the knowledge base construction by providing higher level expert reasoning through the objects. The key objective is to make the system level details transparent to the experts who can then focus primarily on the domain knowledge to create the knowledge base. Several versions of the knowledge base can be created, either through automated routines or expert assistance, to accommodate information input in its native format or its less complex equivalents.

Meta-knowledge creation facility: Meta-knowledge represents the how’s and why’s regarding the knowledge embedded in the knowledge base and this is communicated to the user through the explanation facility. Communication modes that rely on more complex and abstract media objects are typically more intuitive and comprehensible to non-expert users. For example, a pictorial simulation of a tumor growth under various medical conditions or an animation of complex machinery conveys the mechanisms that drive the knowledge base more effectively than mere textual, verbal or static image descriptions. This control layer subcomponent assists in the creation of the explanation facility by providing techniques to convert media objects to more abstract and more complex versions to enhance user comprehension of the embedded knowledge.

Knowledge dissemination facility: The knowledge dissemination facility is activated during the user consultation with the expert system. It provides facilities to acquire user input in native format or alternately in a less complex format. It operates the media preprocessing algorithms designed during the knowledge creation stage to error check and enhance the input object. The preprocessed input information is conveyed to the knowledge base. Media processing algorithms that are invoked by the knowledge base are handled by the knowledge dissemination facility and are transferred to the inference engine. Further requests for user input by the inference engine are conveyed through the dissemination facility and the user interface. User queries during the consultation session are conveyed to the explanation facility. The requisite meta-knowledge objects and algorithms are activated as per the designated object routines by the dissemination facility and presented to the user via the user interface. This control layer subcomponent is designed to handle media processing and act as an intermediary between the object layer and the expert system during user interaction with the system.

## 3.4. Implementation issues

HypEs architecture is generic in that it is amenable to a spectrum of different implementation environments. This is due to the modularity in the design of the Knowledge Manager that results in logical independence between its components. New media objects, properties and processing methods of the objects can be iteratively added to the object layer to improve its functionality without triggering system wide alterations. Similarly, the implementation of the control layer can be conducted through various degrees of automation. A low-end system might simply provide a few automated routines to the experts orŽ knowledge engineers to provide access to the object. layer for knowledge and meta-knowledge creation and to the user interface for knowledge dissemination. A high-end system may reduce the cognitive burden on the human participants by automating media analysis and retrieval operations. This can be achieved by designing expertise into the control layer to incorporate deductive capabilities, efficient selection of properties, feature and pattern identification algorithms, and object conversion techniques. From an organizational perspective, the Knowledge Manager can be implemented as a central repository of media objects that provides services to various expert system applications across the organization. Such an architecture can transcend departmental boundaries by enabling knowledge sharing between distinct, but related functional areas. A unified, organization-wide implementation serves to significantly enhance the visibility and can potentially foster increased acceptance and usage of expert system technologies.

Traditional expert systems have provided non-expert users access to expertise, albeit in text-restricted environments. The complexities involved in textual translations by the experts and the users have severely hampered their widespread use. The significance of HypEs stems from the fact that it transfers these complex tasks from human participants to the system, through the utilization of hypermedia technologies. In Section 4, we provide a limited validation of the HypEs architecture through an experimental evaluation.

## 4. Experimental analysis

In this section, we provide an initial validation of the proposed architecture. The validation is conducted through a comparative analysis of an expert system application, implemented both in a hypermedia and in a text-restricted environment. As noted in the introduction, initiating empirical testing is crucial to validation of our HypEs architecture argument. While our experimentation is limited, the results provide important initial support for our arguments.

The experimental prototype expert system was not based on a real world problem, but it incorporated key image analysis characteristics inherent in several practical applications. This approach permitted us to retain control and broaden the scope of analysis while maintaining realism. The expert system was developed to analyze patterns within paths and regions present in a series of image objects. The characteristics studied include length, area, growth and movement of these patterns in the image objects. Such patterns are examined by human experts in a number of application domains 12,15,30 .<sup>w</sup> <sup>x</sup>

Table 1  
Variables in the experimental system

<table><tr><td>Input variables</td><td>Pattern analysis</td><td>Measurement items</td></tr><tr><td>Var1</td><td>Path length</td><td>Len1, Len2</td></tr><tr><td>Var2</td><td>Path length</td><td>Len3, Len4</td></tr><tr><td>Var3</td><td>Region area</td><td>Area1, Area2</td></tr><tr><td>Var4</td><td>Region growth</td><td>GArea</td></tr><tr><td>Var5</td><td>Pattern movement</td><td>L-Move, R-Move</td></tr><tr><td colspan="3">Intermediate goal variables</td></tr><tr><td>IVar1</td><td>Boolean</td><td>True, false</td></tr><tr><td>IVar2</td><td>Categorical</td><td>High, medium, low</td></tr><tr><td colspan="3">Goal variable</td></tr><tr><td>GVar</td><td>Boolean</td><td>True, false</td></tr></table>

```txt
Table 2
Rule set for the experimental system

R1: IF (Len2 > Len1) OR (Area2 ≤ 1.7 * Area1)
AND (Len3 ≤ Len4)
THEN IVar1 = True
R2: IF (GArea > 30%) AND (L-Move > R-Move)
OR (GArea ≤ 30%) AND (L-Move ≤ R-Move)
THEN IVar2 = Low
R3: IF (GArea > 30%)
AND (L-Move ≤ R-Move)
THEN IVar2 = Medium
R4: IF (GArea ≤ 30%)
AND (L-Move > R-Move)
THEN IVar2 = High
R5: IF (IVar1 = True)
OR ~ (IVar2 = Low)
THEN GVar = True
```

A rule-based expert system was created and used for experimental evaluation. The variables, their attributes and measurements are described in Table 1. The rule base consists of five rules shown in Table 2.

The inference mechanism was operationalized through a simple forward chaining process. The initial data set provided to the expert system consisted of the values for all the five input variables: Var1 through Var5. While inefficient from an implementation perspective, utilizing data on all the input variables permitted us to simultaneously analyze and correlate the conclusions from expert system consultation with the data input errors. The rule set was constructed to ensure that no combination of input data values translate to inconsistent results in the goal variable.

The input data analyzed by the expert system was created in an image format. The patterns in each image object were distinguished by their color values in relation to the surrounding areas. The values for each of the variables Var1, Var2, and Var3 result from pattern analysis of two image objects. Two animation objects, one depicting growth in a pattern and other a movement in a series of patterns, constituted the input data for variables Var4 and Var5. Each animation object was operationalized through a series of image objects. The correct values of the input data result in the following outcomes: IVar1<sup>s</sup> True, IVar2<sup>s</sup>High, and GVar<sup>s</sup>True.

In the hypermedia-enabled prototype, a front-end was designed to process the image objects and then directly transfer the input data in a textual format to the expert system. The length, area and growth values were obtained by analyzing the proportion of various color values in the image objects. The color values, along with their location on the image object were analyzed to detect moÕement patterns. In the text-restricted expert system, the user bore the responsibility to translate the image objects into textual format. The final conclusions in both prototypes were generated by the system not the human sub- Ž jects ..

The hypermedia-enabled prototype worked — the image analysis algorithms generated accurate input data values and the expert system provided the correct conclusion. This is due to the fact that this prototype did not rely on image-to-text translations by the human participants. This provided the benchmark to evaluate the performance of the text-restricted expert system.

In the text-restricted implementation, human subjects were given the task of analyzing the input image objects and translating this information to the expert system in a textual format. The expert system provided the final conclusion based on the textual data provided by the subjects. Sixty-three subjects participated in the experiment. The subjects represented faculty, staff and students from a major U.S. university. None of the subjects participated in the earlier experiments.

The overall experiment consisted of two experimental sessions. The second experimental session was a repetition of the first experimental session, in that the participants re-analyzed the same image objects during the second session. This repetition of the tasks allowed us to track learning effects and inconsistencies in human image processing. A financial incentive based on the accuracy of the media translation tasks was provided to improve the effort expended by the participants. No time constraint was imposed for the completion of the tasks.

Table 3  
Conclusion accuracy

<table><tr><td>Experimental session 1</td><td>Experimental session 2</td><td>Percentage</td></tr><tr><td>Correct conclusion</td><td>Correct conclusion</td><td>39.7%</td></tr><tr><td>Correct conclusion</td><td>Incorrect conclusion</td><td>14.3%</td></tr><tr><td>Incorrect conclusion</td><td>Correct conclusion</td><td>23.8%</td></tr><tr><td>Incorrect conclusion</td><td>Incorrect conclusion</td><td>22.2%</td></tr></table>

Table 4  
Answer accuracy

<table><tr><td>Average no. of correct answers (of five questions)</td><td>Experimental session 1</td><td>Experimental session 2</td></tr><tr><td>Correct conclusion reached</td><td>2.12</td><td>2.33</td></tr><tr><td>Incorrect conclusion reached</td><td>1.76</td><td>1.91</td></tr></table>

Our initial analysis focused on the comparison of the final conclusions reached by the text-restricted expert system with the correct conclusions derived from the hypermedia-enabled expert system. Note that the errors in the final conclusion arrived by the text-restricted expert system arise due to errors in the input textual data provided by the human participants. The results from the experiment on the accuracy of the final conclusions obtained from the textrestricted expert system are depicted in Table 3. Less than 40% of the participants were able to successfully translate image data to textual data and obtain the correct conclusion from the expert system in both sessions. In at least one experimental session, over 60% of the participants made errors that resulted in incorrect conclusions drawn by the text-restricted expert system. Around 38% of the participants obtained differing conclusions in the two sessions, highlighting inconsistencies in human analysis of image objects. The percentage of participants who reached the right conclusion jumped from 54% in the first session to 63.5% in the second session, indicating the existence of some learning effects.

Note that even when a participant obtains the correct final conclusion from the text-restricted expert system, this does not necessarily imply that every image object was accurately translated by that subject. Table 4 reports the average number of correct answers to the five input variables provided by Ž . the participants to the expert system, tabulated by the experimental session and the final conclusion reached. As the results indicate, even when the textrestricted expert system provided the correct final conclusion, less than 50% of the image-to-text translation tasks were accurately conducted. Overall, the participants who were able to obtain the correct conclusion performed better in the translation tasks. While participants who reached the right conclusion performed better in the number of questions answered correctly, their responses were not error-free. Table 4 also provides some evidence for the existence of learning effects as the accuracy of the translation tasks increased in the second experimental session.

## 5. Concluding remarks

This research addresses the incorporation of hypermedia technologies into expert systems. Hypermedia technologies extend the functionality of expert systems beyond the realm of text-restricted environments and thus improve the effectiveness and widen the domain of expert system applications. We proposed an architecture termed HypEs that is designed to employ multiple media for knowledge acquisition, storage and user interface activities of expert systems. A key component of the architecture is the Knowledge Manager that enables these objects to directly manipulate knowledge in native or near-native formats. An initial experimental study provided evidence of the superiority of hypermedia-enabled expert systems over their textual counterparts. Next steps include the following:

1. more rigorous tests of the general HypEs architecture;

2. using HypEs architecture to construct a class of development shells followed by appropriate validation testing;

3. field application and study of the value-added by use of HypEs in key expert system arenas.

Our efforts are now being directed at these tasks in order to move HypEs farther along the path from a logical construct to a useful application method.

## Acknowledgements

This research was partially supported by the Treibick Electronic Commerce Initiative at the Department of Operations and Information Management, School of Business Administration, University of Connecticut.

## References

<sup>w</sup> <sup>x</sup> 1 E.M. Awad, Building Expert Systems, St. Paul, West Minnesota, 1996.

<sup>w</sup> <sup>x</sup> 2 L. Bielawski, R. Lewand, Intelligent Systems Design: Integrating Expert Systems, Hypermedia and Database Technologies, Wiley, New York, 1991.

<sup>w</sup> <sup>x</sup> 3 K. Bland, J. Liebowitz, KARTT: a multimedia tool to help students learn knowledge acquisition, Journal of End User Computing 5 1 1993 5–16.Ž . Ž .

<sup>w</sup> <sup>x</sup> 4 L.G. Brown, A survey of image registration techniques, Computing Surveys 24 1 1992 325–376.Ž . Ž .

<sup>w</sup> <sup>x</sup> 5 N. Carbonell, D. Fohr, J. Haton, Aphodex: an acousticphonetic decoding expert system, in: C.H. Chen Ed. , Pro- Ž . ceedings of IEEE Workshop on Expert Systems and Pattern Analysis, Paris, France, World Scientific, 1987, pp. 31–44.

<sup>w</sup> <sup>x</sup> 6 D.R. Clark, in: R.A. Earnshaw, J.A. Vince Eds. , DefiningŽ . the Multimedia Engine, Multimedia Systems and Applications, Academic Press, San Diego, 1995, pp. 3–20.

<sup>w</sup> <sup>x</sup> 7 P. Courtway, Hospital saves thousands using multimedia tutorial, Health Management Technology 16 12 1994Ž . Ž . 30–32.

<sup>w</sup> <sup>x</sup> 8 D. Fischer, C. Richards, in: R.A. Earnshaw, J.A. Vince Ž . Eds. , The Presentation of Time in Interactive Animated Systems Diagrams, Multimedia Systems and Applications, Academic Press, San Diego, 1995, pp. 141–159.

<sup>w</sup> <sup>x</sup> 9 G. Fisher, J. Grudin, A. Lemke, R. McCall, J. Ostwald, B. Reeves, F. Shipman, Supporting indirect collaborative design with integrated knowledge-based design environment, Human-Computer Interaction 7 1 1992 281–314.Ž . Ž .

<sup>w</sup> <sup>x</sup> 10 W.L. Fuerst, J.M. Ragusa, E. Turban, Expert systems and multimedia: examining the potential for integration, Journal of Management Information Systems 11 3 1995 155–179.Ž . Ž .

<sup>w</sup> <sup>x</sup> 11 B.R. Gaines, M. Linster, Integrating a knowledge acquisition tool, expert system shell and a hypermedia system, International Journal of Expert Systems 3 2 1990 105–129.Ž . Ž .

<sup>w</sup> <sup>x</sup> 12 F. Golshani, N. Dimitrova, Retrieval and delivery of information in multimedia database systems, Information and Software Technology 36 4 1994 235–242.Ž . Ž .

<sup>w</sup> <sup>x</sup> 13 M.J. Handley, P.T. Kirstein, M.A. Sasse, Multimedia integrated conferencing for European researchers MICE : pilot-Ž . ing activities and the conference management and multiplexing centre, Computer Networks and ISDN Systems 26 1Ž . Ž .1993 275–290.

<sup>w</sup> <sup>x</sup> 14 M.A. Harrison, in: R.A. Earnshaw, J.A. Vince Eds. , TheŽ . Essential Elements of Hypermedia, Multimedia Systems and Applications, Academic Press, San Diego, 1995, pp. 79–99.

<sup>w</sup> <sup>x</sup> 15 B. Kartikeyan, K.L. Majumder, A.R. Dasgupta, An expert system for land cover classification, IEEE Transactions on Geoscience and Remote Sensing 33 1 1995 58–66.Ž . Ž .

<sup>w</sup> <sup>x</sup> 16 S. Kung, J.R. Marsden, A methodology and experimenta shell for formally addressing centralized<sup>r</sup>distributed decision making choices, Decision Support Systems 15 1 1995 Ž . Ž . 45–63.

<sup>w</sup> <sup>x</sup> 17 J.K. Lee, I.K. Lee, H.R. Choi, S.M. Ahn, Automatic rule generation by the transformation of expert’s diagram: LIFT, International Journal of the Man–Machine Studies 1990Ž . 275–292.

<sup>w</sup> <sup>x</sup> 18 D. Leonard-Barton, J.J. Sviokla, Putting expert systems to work, Harvard Business Review, March–April 1998 91–98.Ž .

<sup>w</sup> <sup>x</sup> 19 R. Lewis, Practical Digital Image Processing, Ellis Horwood, London, 1990.

<sup>w</sup> <sup>x</sup> 20 J.M. Long, J.R. Slagle, E.A. Irani, M.R. Wick, J.W. Johnson, J.P. Matts, in: J. Liebowitz Ed. , Two Expert SystemsŽ . Applied to Clinical Trails, Operational Expert System Applications in the United States, Pergamon, New York, 1991, pp. 52–66.

<sup>w</sup> <sup>x</sup> 21 A.J. Macartney, G.S. Blair, Flexible trading in distributed multimedia systems, Computer Networks and ISDN Systems 25 1 1992 145–157.Ž . Ž .

<sup>w</sup> <sup>x</sup>22 J.R. Marsden, Y.A. Tung, The use of information technology to develop tests on insider trading and asymmetric information, Management Science, forthcoming.

<sup>w</sup> <sup>x</sup> 23 R. Minch, Application and research areas for hypertext in decision support systems, Journal of Management Information Systems 6 3 1990 119–138.Ž . Ž .

<sup>w</sup> <sup>x</sup> 24 J. Mao, J.S. Dhaliwal, I. Benbasat, The use of hypertext to provide explanations in knowledge-based systems: a conceptual model and implementation, Proceedings of the 27th Hawaii International Conference on Systems Sciences 4 1Ž . Ž .1994 210–223.

<sup>w</sup> <sup>x</sup> 25 A. Moffat, J. Zobel, Index organization for multimedia database systems, ACM Computing Surveys 27 4 1995 Ž . Ž . 607–609.

<sup>w</sup> <sup>x</sup> 26 S.W. Oxman, in: J. Liebowitz Ed. , The Development of the Ž . AIRAID Expert System: A Case Study, Operational Expert System Applications in the United States, Pergamon, New York, 1991, pp. 130–143.

<sup>w</sup> <sup>x</sup> 27 J.M. Ragusa, Models and applications of multimedia, hypermedia and intellimedia integration with expert systems, Expert Systems with Applications 7 1 1994 7–13.Ž . Ž .

<sup>w</sup> <sup>x</sup> 28 J.C. Sipior, E.J. Garrity, Merging expert systems with multimedia technology, Data Base 21 4 1992 45–49.Ž . Ž .

<sup>w</sup> <sup>x</sup> 29 P. Suetens, A. Oosterlinck, Using expert systems for image understanding, in: C.H. Chen Ed. , Proceedings of IEEEŽ . Workshop on Expert Systems and Pattern Analysis, Paris, France, World Scientific, 1987, pp. 61–74.

<sup>w</sup> <sup>x</sup> 30 S. Tsao, N. Kehtarnavaz, P. Chan, R. Lytton, Image-based expert-system approach to distress detection on CRC pavement, Journal of Transportation Engineering 120 1 1994 Ž . Ž . 52–64.

<sup>w</sup> <sup>x</sup> 31 Y.A. Tung, R.D. Gopal, J.R. Marsden, in: W.S. Chow Ed. ,Ž . Architectural Foundations of Hypermedia-Enabled Expert Systems, Multimedia Technology and Applications, Springer-Verlag, Singapore, 1997, pp. 34–44.

<sup>w</sup> <sup>x</sup> 32 E. Turban, Decision Support and Expert Systems, 2nd edn., Macmillan, New York, 1993.

Y. Alex Tung is Assistant Professor of MIS at the University of Nevada Las Vegas. He received his BS from National Sun Yat-Sen University Taiwan 1988 and PhD from the UniversityŽ . of Kentucky 1994 . His research interests include end-user com-Ž . puting, emerging information technologies, and business applications of the Internet. He has published papers in various journals such as Management Science, European Journal of Operational Research, Journal of Business Research, Journal of Multi-Criteria Decision Analysis, and Journal of Computer Information Systems.

Ram D. Gopal is Associate Professor of Operations and Information Management in the School of Business, University of Connecticut. His current research interests include economics of information systems management, data security, economic and ethical issues relating to intellectual property rights, and multimedia applications. His research has appeared in INFORMS Journal on Computing, Information Systems Research, Communications of the ACM, IEEE Transactions on Knowledge and Data Engineering, Journal of Management Information Systems, Decision Support Systems, and other journals and conference proceedings.

James R. Marsden is Professor and Head of the Department of Operations and Information Management, School of Business Administration, University of Connecticut. He was formerly the Philip Morris Professor and Founding Chair of the Department of Decision Sciences and Information Systems, University of Kentucky. He has held visiting positions at the University of North Carolina, University of Arizona, Purdue University, and University of York U.K. . His research interests include informationŽ . valuation, controlled laboratory experimentation, electronic markets, dynamic database restricting, and intelligent systems. His research has appeared in Management Science, IEEE Transactions on Systems, Man and Cybernetics, American Economic Review, Journal of Economic Theory, Journal of Political Economy, and numerous other outlets.
