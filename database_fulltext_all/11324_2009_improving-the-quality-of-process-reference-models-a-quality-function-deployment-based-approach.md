---
otero_id: 11324
otero_key: "WRCK6TNG"
title: "Improving the quality of process reference models: A quality function deployment-based approach"
authors: "Sabine Matook; Marta Indulska"
year: "2009"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.12.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Improving the quality of process reference models: A quality function deployment-based approach

Sabine Matook ⁎, Marta Indulska

The University of Queensland, UQ Business School, Qld 4072, Australia

## a r t i c l e i n f o

Article history: Received 6 January 2008 Received in revised form 22 December 2008 Accepted 30 December 2008 Available online 7 January 2009

Keywords: Reference model Reference model quality Reference model characteristics Quality function deployment

## a b s t r a c t

Little academic work exists on managing reference model development and measuring reference mode quality, yet there is a clear need for higher quality reference models. We address this gap by developing a quality management and measurement instrument. The foundation for the instrument is the well-known Quality Function Deployment (QFD) approach. The QFD-based approach incorporates prior research on reference model requirements and development approaches. Initial evaluation of the instrument is carried out with a case study of a logistic reference process. The case study reveals that the instrument is a valuable tool for the management and estimation of reference model quality.

© 2009 Elsevier B.V. All rights reserved

## 1. Introduction

Today's hyper-competitive and increasingly regulated markets see organizations place signi<sup>fi</sup>cant focus, and thus resources, on managing and improving their business processes [42]. Such improvements and innovations are considered to be an important factor in creating organizational wealth [49]. Indeed, recent Gartner studies show that CIOs now consider Business Process Management (BPM) to be the top priority in the coming years [41–43]. The high prioritization of process management in the recent years is also due to today's regulatory climate, which is forcing organizations to document processes and ensure their compliance. Many recent regulations (e.g. Anti Money Laundering Act [4]), however, are principle-based, as opposed to being prescriptive in nature, and require signi<sup>fi</sup>cant interpretation on account of the regulatee [36]. Anecdotal evidence from the Australian <sup>fi</sup>nance sector suggests that organizations are seeking reference models (RM) to help ease their compliance management pain and reduce the signi<sup>fi</sup>cant spending brought on by compliance requirements.

RM are blueprints of recommended practice and, thus, are sources of reusable and ef<sup>fi</sup>cient business processes on which organizations can model their own [58]. Their main purpose is to streamline the design of enterprise models and enable organizations to apply ‘best practice’ knowledge. The use of high quality RM can result in cost and risk reductions, as well as an improvement of the organization's business processes [58]. It is estimated that the use of RM in projects can reduce the project duration and required <sup>fi</sup>nancial resources by 30% [60]. Clearly, while there is much potential for savings with the use of RM, using a low quality RM can be damaging to the performance of the organization and to the quality of its decision making. Business processes, and therefore also RM, contain decision making components, such as policies or business rules for example [54], hence a high quality speci<sup>fi</sup>cation of the RM is important to ensure compliance with various requirements. In other words, an organization should ensure that the considered RM is complete, accurate, and easily con<sup>fi</sup>gurable (i.e. <sup>fl</sup>exible) for their purpose. To date, however, little work has been carried out that might provide guidance for the selection of high quality RM, let alone guidance for the development process that leads to high quality RM [45]. Only a few studies have focused on the quality of RM, despite reference modeling being an established <sup>fi</sup>eld in Information Systems research. This situation is despite the fact that prior research has explicitly identi<sup>fi</sup>ed the need to close this gap [70]. For example, according to Fettke and Loos [20], the selection of models is increasingly complicated while being ‘a crucial task for the project’. Frank [24] concludes that “… the evaluation of reference models is a challenging, yet important task”. Accordingly, the organizations that develop RM (e.g. standardization or regulation bodies), and also those that are potential RM users, would value an instrument that aims to increase the quality of RM, through guiding its development, and also provides an easy measure of model quality that can be used in communication between the RM provider and RM user organizations. Indeed, the research presented in this paper was incepted by a request from a German standardization body that required such an instrument despite already having a quality control process in place. The organization was interested in obtaining an RM quality management and measurement instrument that would incorporate a best practice RM development process while also taking into consideration RM user requirements.

In response to the clear gap in RM quality research, and in response to the request of the aforementioned standardization organization, we present an interrelationship matrix-based artifact for increasing and measuring the quality of RM. The measurement evaluates the steps that are taken to develop an RM with respect to a set of required model characteristics and also considers the ‘voice of the customer’. We adapt the <sup>fi</sup>rst phase of the Quality Function Deployment (QFD) approach (also referred to as ‘narrow QFD’) for this purpose and derive an artifact that not only helps organizations develop high quality RM but also measures the achieved quality level. QFD, which originates from Japan, is an approach aimed at satisfying the users through the provision of high quality products that <sup>fi</sup>t the users' requirements. The approach involves collecting user demands and converting them into design targets and major quality assurance points to be used throughout the development phases [3]. We see a QFD-based approach as most suitable here due to QFD's user-centric nature that captures the mapping of user requirements into product design [26].

The paper is structured as follows. Section 2 discusses related work — its main contribution is the extensive literature analysis and synthesis of academic literature related to RM quality and RM development, much of which is published in various German publication outlets and, hence, not easy accessible by international researchers. Research methodology is presented in Section 3. Section 4 describes the proposed instrument and Section 5 presents its application in a case study. Section 6 discusses <sup>fi</sup>ndings related to the development process and RM characteristics. Last, Section 7 summarizes contributions, limitations and outlines future research.

## 2. Reference model development and characteristics

The general aspect of model re-use dates back to the 1930s [70] but was revitalized in the early 90s by Scheer [59–61], Österle et al. [50– 52], and Hammel [28] for the process modeling domain. At the time, as Business Process Reengineering (BPR) was gaining popularity, organizations began to realize the cost advantages of RM on their process redesign projects. Since then, BPR has given way to BPM, with organizations taking an increasing interest in continually and holistically managing and improving their processes. Today, organizations spend signi<sup>fi</sup>cant amounts of money on BPM initiatives [75]. Recent BPM market analysis indicates that improvement of processes for productivity gains will be the main driver of the market in the coming years [74].

The redesign of processes for the purpose of increasing productivity is one example of a potentially fruitful opportunity for the application of RM. It is not the only opportunity however — RM have been used for a wide variety of purposes [20]. For example, they have been applied throughout the Enterprise Resource Planning Lifecycle [56], used for standardization of organizational software [73], curriculum design ([38,44]), knowledge and supply chain management [23], and decision support (e.g. selection of ERP packages or validating enterprise-speci<sup>fi</sup>c models) [22]. Fettke et al.'s [23] survey and classi<sup>fi</sup>cation of RM indeed shows a very broad application of RM and classi<sup>fi</sup>es the models into speci<sup>fi</sup>c orientation categories (viz. business function, Information Systems function, industry).

Regardless of the <sup>fi</sup>eld or categorization, there is no doubt that “there is currently a remarkable renaissance in using reference models” [34]. Despite the increased popularity, there is a lack of understanding of the characteristics required of RM and also of their development process. In the next two sections, we consolidate various works on RM characteristics and development strategies in order to present a consistent and cohesive body of knowledge in this domain.

## 2.1. Process reference model development

While literature emphasizes the advantages of having access to high quality RM, this emphasis is not balanced with much published academic work that guides quality RM development [71]. Prior studies have shown, however, that a de<sup>fi</sup>ned and structured development process contributes positively to the validity and quality of a RM [73]. In the development of a quality management and measurement instrument for the RM domain, we were also motivated to consolidate existing (and often only published in German) contributions towards RM development. There is a clear need for such consolidation in this domain [22]. This need is strengthened by the fact that RM research is predominantly conducted in Germany [22] and sometimes also only locally published.

A literature analysis of RM publications shows a strong German in<sup>fl</sup>uence (e.g. [2,24,73]) with many of the publications available only in German language (e.g. [7,21,28,29]). Some of these publications contain guidance for RM development and, hence, are included in our consolidation so that their contributions can be available to the larger research community. In the remainder of this section we present an overview of both English and German published research on RM development and then present the seven phase RM development process.

RM development models have a sequential and sometimes cyclic structure of their overall construction processes in analogy with systems engineering [2]. The majority of the mentioned development stages have commonalities with software development approaches. Our aim in this section is to consolidate these works to arrive at a synthesized model that builds on the systems development life cycle (SDLC) ([1,15,25,40]). Orienting the RM development process on the SDLC provides the bene<sup>fi</sup>t of manageable, well separated phases that clearly de<sup>fi</sup>ne required inputs and outputs [5]. The RM development process embraces seven phases, which emerge out of the synthesis of prior RM development research outlined below, which are based on prior research and practical experiences.

Schütte [63] proposes a process model for the development of industry-speci<sup>fi</sup>c RM. The model allows con<sup>fi</sup>guration and consists of <sup>fi</sup>ve phases that emphasize the importance of model based planning. Building on Schütte's work [63], Schlagheck [62] considers RM development as an iterative process that focuses not only on the development aspect but also on the application aspect of the RM. The RM development phases are those of problem de<sup>fi</sup>nition, analysis of the problem domain, construction, evaluation, and evolution [62]. Becker et al. [7] use in their RM development process different perspectives for considering various RM user groups. While their suggested RM development process is similar to that proposed by [62], it consists of an additional phase dedicated explicitly to marketing of the RM.

The process presented by Ahlemann and Gastl [2] emphasizes the use of empirical evidence in the RM development. The development phases are adopted from prior research (speci<sup>fi</sup>cally, that of Schütte [63] and Schlagheck [62]) but the work presents speci<sup>fi</sup>c instructions and hence, offers guidance on documentation and user involvement in the development process.

Thomas and Scheer [71] describe the development process as a chain of activities, which involves the planning, information search, documentation of user organizational knowledge and model construction. Fettke and Loos [20], on the other hand, describe the development process at the high level as a cycle that consists of problem de<sup>fi</sup>nition, construction, assessment, and maintenance. Even the well recognized work of Schütte and Rotthowe [64], which introduced the Guidelines of Modeling (GoM), only at the high level describes that the principles of construction adequacy, language adequacy, economic ef<sup>fi</sup>ciency, systematic design, comparability and clarity need to be observed in RM development initiatives.

In addition to the academic contributions, there is also a number of RM design philosophies known in practice. However, these philosophies are very high level approaches that do not provide any guidance for RM development [68] and, hence, are not incorporated in our consolidated RM development process below.

The <sup>fi</sup>rst phase of the RM development process is problem definition. Relevant activities in this early stage include outlining the purpose of the model, selecting model characteristics (e.g. model audience), and developing model conventions ([63,68]). We argue that, in addition, other aspects must also be considered in this phase before model characteristics are de<sup>fi</sup>ned and modeling conventions are set. For example, the scope of the RM must be agreed upon and an understanding of the domain area must be achieved [9]. This phase should be done in collaboration with a domain expert [63].

The second phase – requirement analysis – incorporates the main activities of analysis of the most appropriate modeling language, determination of existing models, and setting the level of granularity [55]. It builds on the information gained in the problem de<sup>fi</sup>nition phase and usually ends with effort estimation [7].

The third phase – information gathering – incorporates mainly identi<sup>fi</sup>cation, as well as relation and rating of information sources. Schwegman [65] emphasizes the importance of explicitly stating the common sources of information in process design initiatives.

Phase four deals with the need for the setting of conventions and rules within the development project [62]. Further, the development of glossaries is bene<sup>fi</sup>cial for a common terminology and understanding of, in particular, multi-disciplinary teams ([7,24)].

Given the required reusability of RM by a large number of organizations, we see a strong need for the explicit incorporation of a documentation phase as phase <sup>fi</sup>ve. While documentation also has to occur throughout the development process, there needs to be a stage at which the documentation is updated and guaranteed to be consistent with the implemented RM [63]. This stage preferably comes before construction ensuring that RM implementation is based on complete information [2].

The <sup>fi</sup>nal two phases – construction and evaluation – are the actual creation of the RM and its subsequent evaluation. The construction phase refers to the act of creating the RM, which also includes activities that consider existing RM [62]. During the construction phase, a close working relationship between the developers ensures that more of the available information is used to create the RM [7]. The evaluation phase is the last phase in the development process [68]. It assesses the consistency and usefulness of the RM [62] and allows identi<sup>fi</sup>cation of improvements and changes. The evaluation should be ongoing and continue beyond the completion of the RM development project. It should also involve both the users and developers.

The full list of activities involved in each of the development phases is shown in the Appendix. Each set of activities was derived through literature analysis of prior reference modeling research.

## 2.2. Process reference model characteristics

Every model can be described by a set of desired characteristics that can also be used to assess model quality. Previous research in the domain of reference modeling has identi<sup>fi</sup>ed a number of characteristics that are considered to be required of models. However, as suggested by Moody [46], the number of disjoint and sometimes inconsistent contributions on model quality is counter-productive to an objective assessment of model quality. Accordingly, the aim of this section is to consolidate prior research on RM characteristics, and also practical experiences, to derive a set of desired characteristics that indicate a model of high quality.

According to Rosemann and Schütte [57], model quality can be measured by evaluating the model's syntactic and semantic completeness and correctness, as well as its adaptability and applicability. Mišic and Zhao [45] propose their set of quality evaluation criteria also as syntactic and semantic, but additionally pragmatic as well. Within these criteria, Mišic and Zhao [45] further articulate level of abstraction, level of detail, strati<sup>fi</sup>cation, consistency, coherence, completeness, orientation, scope, extensibility, openness and technology dependence. Lindland et al. [39] and Taylor and Sedera [69], identify a number of factors, viz., clear de<sup>fi</sup>nition of the language, consistency of use of language, clarity of scope de<sup>fi</sup>nition, extended documentation, and training, which are among the highest perceived quality indicators. In the related area of conceptual modeling, Moody and Shanks [48,47] provide empirical validation for quality factors of conceptual models in general: completeness, simplicity, <sup>fl</sup>exibility, correctness, integration, understandability and implementability. Frank [24] presents a multiperspective framework that takes into consideration an economic, deployment, engineering, and epistemological perspective and de<sup>fi</sup>nes thirty-three aspects with multiple criteria.

Table 1  
Reference model characteristics de<sup>fi</sup>ned in prior research.

<table><tr><td>Reference model characteristics</td><td>Meaning and definition</td><td>Relevant studies</td></tr><tr><td>Generality</td><td>Degree to which the reference model performs a broad range of functions and is usable in different cases</td><td>Hars [29], Schlagheck [62], Schwegman [65]</td></tr><tr><td>Flexibility</td><td>Ease with which a reference model adapts and accommodates to changes of the requirements other than for those for which it was specifically designed</td><td>Hars [29], Mišic and Zhao [45], Moody and Shanks [48], Scheer [61], Schwegman [65], Schlagheck [62]</td></tr><tr><td>Completeness</td><td>Degree to which all the components of the reference model are present under a predefined scope</td><td>Frank [24], Hars [29], Lindland et al. [39], Mišic and Zhao [45], Moody and Shanks [48], Taylor and Sedera [69]</td></tr><tr><td>Usability</td><td>Ease with which a user or user firm can operate, implement, and apply the reference model</td><td>Fettke and Loos [20], Hars [29], Scheer [61],</td></tr><tr><td>Understandability</td><td>Degree to which the purpose, concepts, and structure of the reference model is clear to the users</td><td>Frank[24], Moody and Shanks [48], Schwegman [65], Taylor and Sedera [69]</td></tr></table>

We explicate <sup>fi</sup>ve RM characteristics through the consolidation of previous literature and industry experience on quality criteria of reference and data models. We select these characteristics because they represent a comprehensive set of criteria that incorporates the previous research in this area. In this selection process we exclude any characteristics from previous research that can be subordinated under the <sup>fi</sup>ve general characteristics. Table 1 de<sup>fi</sup>nes the characteristics together with their literature source. In the following, we present the characteristics in more detail.

## 2.2.1. Understandability

Moody and Shanks [47] identify understandability as one of the key requirements for high quality data models. The same requirement holds for RM, as models that are not easily understood are not likely to be adopted or perceived as high quality by the model users. This need for understandability is further supported by the empirical work of Taylor and Sedera [69]. They identify attributes in the syntactic and pragmatic model quality dimensions that can increase the understandability of RM, for example providing documentation, educating the users, and using simple and consistent language within the RM. Moreover, GoM [64] name clarity, which impacts understandability, as one of the additional principles required for modeling, hence also applicable to RM.

## 2.2.2. Generality

A certain level of abstraction is required for RM to be useful since RM must have the potential to create more speci<sup>fi</sup>c models and facilitate re-use [29]. When a RM is speci<sup>fi</sup>ed in too much detail, there is a risk that the model will not be seen as semantically correct or relevant to potential users [65]. In other words, users must be able to identify their organizational situation in the RM to consider adopting the model — this is more dif<sup>fi</sup>cult when the model is over-speci<sup>fi</sup>ed. Generality, however, is only possible for a certain scope and no model is applicable to all situations. Within that scope, the RM is made for a broad user group and is valid for a large number of cases. Hence, overall, generality can be seen as a measure of the RM's potential use in various use cases with similar structure and process characteristics.

![](/api/attachments/WRCK6TNG/fulltext/images/5ffa76ca9efd3371656c591e7bb298a31e409eb075b08f73787465e87b1decc4.jpg)  
Fig. 1. Major interactions between the reference model characteristics.

## 2.2.3. Flexibility

One of the main bene<sup>fi</sup>ts of having a repository of RM in an organization is that these general models are ready to be deployed with some con<sup>fi</sup>guration, as called for by different situations. This adaptation or extension is necessary since the RM cannot contain all individual requirements of all potential users (see Generality). Indeed, Schwegman [65] argues that this requirement is also necessary to ensure that the resulting RM align with GoM [64], in particular, with relevance and semantic correctness from the user's perspective. Scheer [61] further articulates this need for adaptability, underlining the importance of general models being adaptable to the changing organizational needs.

## 2.2.4. Completeness

Completeness refers to the RM being correct and having all required components (within a prede<sup>fi</sup>ned scope) present. This characteristic is one of the core user requirements [24]. When an RM is developed, all necessary structures, processes, data, policies, etc., should be taken into consideration to create a complete model. The RM must still adhere with the generality requirement but it should be correct and complete so that it is, in theory, possible to use the model without variation in some given situation ([29,61]).

## 2.2.5. Usability

The required characteristic of usability refers to the need for RM to be detailed enough and aligned with the organizational situation so that the model can be implemented [48,47]. Models that are vague in nature may be seen as having some value in overall guidance, but are not useful to organizations from an implementation perspective. Thus, RM are distinguished from meta-models, which guide organizations at a much higher level of abstraction [29].

Although each of the characteristics focuses on a distinct facet of an RM, they are interrelated as depicted in Fig. 1. The understanding of the interactions between the different characteristics implies the trade-off among them.

For example, understandability impacts usability directly, because, if model users do not understand the RM, it is dif<sup>fi</sup>cult, if not impossible, for the model to be implemented. In turn, completeness impacts understandability, because incomplete vague models are harder to understand. Using the approach of Moody and Shanks [47], we present below the interactions expected between the <sup>fi</sup>ve RM characteristics and outline the positive and negative interactions in Table 2. It is expected that there are additional interactions but these are dependent on the context of the RM and its potential user, and are, hence, omitted from the interactions diagram and table. For instance, generality can positively impact understandability because overly speci<sup>fi</sup>c models make it harder for an organization to see their situation in the RM. However, overly general RM can be too high level to result in any meaningful understanding in the potential model user.

## 3. Research methodology

Having motivated the need for an instrument that allows the improvement and management of RM quality, in our study we follow, as closely as possible, the guidelines set out within Design Science (DS) [33]. DS is a research methodology that can be adopted when the goal of the research is the development of an artifact. An artifact in this context can be a system, a set of constructs, or a measurement instrument for instance. While DS is published predominantly in the Information Systems discipline, by its very nature, it applies to many development domains such as Computer Science and Engineering for instance. Indeed, DS stems from these development-focused disciplines and explicitly articulates the seven guidelines [33] that should be followed to ensure the development of a complete and useful artifact.

According to Winter and Schelp [73], Hevner et al.'s [33] de<sup>fi</sup>nition of constructs, models and methods as “the most important results of DS research” extends to not just speci<sup>fi</sup>c models but also to RM. We agree, and further argue that any instrument for the management and measurement of RM development and quality also falls in this category. Accordingly, to ensure the development of a useful artifact for the process RM domain, we follow each of the guidelines set out in [33].

In relation to the <sup>fi</sup>rst guideline – Design as an Artifact – the main aim of this research is the development of a quality assessment instrument, which falls under the artifact de<sup>fi</sup>nition of the DS methodology. The earlier presented sections demonstrate our adherence to the second guideline viz., Problem Relevance, together with the fact that this research was incepted as a result of an organization's request for help in this area. Our research makes a direct contribution to the design artifact and the design foundations (guideline four). This contribution is evident through the adaptation of the QFD approach to the reference modeling domain, and through the investigation of characteristics and development phases of RM. We employ thorough literature searches to motivate the work, identify existing approaches and other relevant areas that can help in the design of the artifact, hence, considering guidelines <sup>fi</sup>ve (Research Rigor) and six (Design as a Search Process). We endeavor to satisfy guideline seven – Communication of Research – through presenting this work at an academic seminar (as well as a conference and workshop in the initial stages of the work ([19,78]).

## Table 2

<table><tr><td>Positive interactions</td><td>Negative interactions</td></tr><tr><td>Flexibility → generality</td><td>Flexibility → understandability</td></tr><tr><td>Flexibility can increase the potential set of users for whom the model is relevant, through the provision of a variety of configurable options</td><td>Providing too many options for variation impacts the ease with which a model is readily understood</td></tr><tr><td>Flexibility → usability</td><td>Generality → usability</td></tr><tr><td>Model flexibility, as in configurable reference models, allows for quicker implementation options</td><td>General models tend to lack specificity that allows quick implementation</td></tr><tr><td>Completeness → understandability</td><td></td></tr><tr><td>A complete model requires less expertise and analysisfor it to be understood</td><td></td></tr><tr><td>Completeness → usability</td><td></td></tr><tr><td>A complete models can be implemented faster since missing elements do not need to be considered</td><td></td></tr><tr><td>Understandability → usability</td><td></td></tr><tr><td>An understanding of an RM facilitates its implementation</td><td></td></tr></table>

Major interactions between the reference model characteristics.

We also initiate steps for guideline three — Design Evaluation. Evaluation of reference model related work is generally a very time consuming and resource intensive task [24]. While an extensive evaluation based on multiple case studies remains a next step in this research, as a means towards this goal, we present an initial case study that details the evaluation of the developed artifact with the organization that requested its development. We choose to adopt the method of an exploratory case study, because it allows the examination of phenomena in their natural settings [8]. The case study research strategy focuses on the understanding and capturing of the dynamic of the practitioner's knowledge within a single setting ([8,18]), and typically applies a combination of data collection methods such as interviews, questionnaires, observations, and company documents [18]. While we only conduct one case study at the present point in time, Yin [77] suggests that a single case study is appropriate if the case is unique. We argue that, while RM are not unique, the adaptation of the QFD approach for this purpose is unique and that evaluation of such an artifact is further impacted by longrunning RM development projects and intellectual property considerations. Furthermore, Yin suggests that a single-case study used for exploratory work can be followed by multiple case studies [77], and we encourage other researchers to use the artifact in other RM development projects to build on our initial evaluation.

## 4. Reference model quality measurement

Prior research considers the quality of a process model in general and emphasizes quality as one of the core success factors of process modeling [6]. However, only little work on the improvement and assessment of RM quality appears in the literature. Among the few, Rosemann and Schütte [57], as well as Mišic and Zhao [45], investigate approaches for assessing the quality of RM. These contributions, however, are high level approaches that do not provide a means to objectively assess model quality, let alone compare the quality of different models. Mišic and Zhao [45] base their evaluation on a linguistic framework that evaluates the syntax, semantics, and pragmatics of the RM. In its present conceptualization, the framework is still missing the de<sup>fi</sup>nition of quality attributes for the three assessment criteria. Taylor and Sedera [69] and Taylor [68] address this gap by de<sup>fi</sup>ning attributes pertaining to RM quality speci<sup>fi</sup>cally. While the compilation is detailed, it lacks theoretical foundation and leaves the application of the framework and the assessment of RM quality for future research. Similar research has been carried out in the broader area of conceptual modeling [46–48], where a six factor framework was developed. We borrow heavily from this framework (see Section 2.2) since RMs are unarguably conceptual models [22]. However, not all conceptual models are reference models [21], hence, we deviate from the framework where deemed necessary.

## 4.1. Quality function deployment

QFD, which originated in Japan in 1972 at the Kobe shipyard of Mitsubishi Heavy Industries, is a customer-oriented approach that facilitates the translation of customer requirements into technical engineering characteristics [67]. It is often used by manufacturing organizations to assist in obtaining a balance between customer requirements and the organizations' actual ability to ful<sup>fi</sup>ll the requirements [26]. In such applications, QFD guides the design and development teams through each stage of the product development process and, in doing so, assures that products closely match customer demand [26]. Thus, QFD can also serve as a decision-making methodology that helps to master the dif<sup>fi</sup>cult and complex decisions during the process of, for example, resource allocation [9]. Moreover, QFD, when applied successfully, can lead to a signi<sup>fi</sup>cant reduction in system development costs [76].

The QFD approach involves developing one or more matrices, the <sup>fi</sup>rst (and most important) of which is referred to as “The House of Quality” (HoQ) [31], as illustrated in Fig. 2.

HoQ provides a conceptual map that enables the improvement of planning and control of the product development process ([26,30]). To achieve this goal, HoQ incorporates six parts ([16,35]); viz., (1) customers requirements and assessment (horizontal dimension), (2) engineering requirements (vertical dimension), (3) the center of the house assessing the impact of the engineering requirements on the customer requirements, (4) the technical correlations (roof), (5) customer perceptions, and (6) objectives and targets. The HoQ can be expanded beyond these components or some components can be eliminated depending on the time available for the assessment and the focus of the analysis [16]. In our work, we utilize parts of the HoQ due to its fundamental and strategic importance in the QFD system [11]. We do not employ the full HoQ, rather, we select and adapt certain elements that are relevant to our study, viz., customer requirements and assessment, engineering requirements, impact of engineering requirements on customer requirements, customer perceptions, and objectives and targets. In the following, we present the six steps taken to create the QFD-based measurement approach.

## 4.1.1. Step 1

Identify and translate the ‘voice of the customer’ into a set of product requirements, which are then populated into the left hand side of the HoQ matrix. The customer here is de<sup>fi</sup>ned as any entity likely to be a consumer of the product. The careful analysis of the requirements spans various sources, such as, for example, surveying, interviewing and pro<sup>fi</sup>ling potential customers [26]. These requirements are usually short statements about customer needs and expectations [27] — we refer to them as customer requirements CR(i).

## 4.1.2. Step 2

Derive product engineering requirements that address customer product requirements. These engineering requirements are technical and measurable statements of the product [26], which are populated into the top row of the HoQ. The traditional application of QFD assumes the engineering requirements to be a set of attributes that express <sup>fi</sup>nal product characteristics [67] (e.g. ‘color screen’, ‘climate control’, etc.). In other words, they represent solutions to how to implement the ‘voice of the customer’, which are independent of the customer requirements and more stable over time [32]. We refer to them as engineering requirements ER(j).

## 4.1.3. Step 3

Collect information about the customers' perception of the importance of each of the product requirements (ICR). This step is akin to asking: “How important is this product requirement to you?“ [13]. The importance is rated using a 5-point scale from 1 (not very important) to 5 (very important). The information regarding the importance of each identi<sup>fi</sup>ed product requirement enables the developing organization to <sup>fi</sup>nd a well-informed trade-off between different requirements [30]. The importance ratings also enable prioritization of the various requirements [53].

## 4.1.4. Step 4

Complete the correlation matrix (REM) by indicating the extent to which each engineering requirement addresses each individual product requirement [30]. This judgment is generally made by the organization in charge of the product development process. Customarily different sets of numbers can be used to represent the relationships between the customer requirements and engineering requirements in the HoQ [13]. In cases where visual representation is preferred, symbols, such as triangles, or circles, can be used. When QFD is applied as a mathematical means, the most commonly used numbers are {0, 1, 3, 9}, however, the use of other number sets is also possible [53]. The {0, 1, 3, 9} set is preferred, however, as it is seen most suitable due to its higher weighting for strong relationships that are much more important in the development process [11]. These numerical values are indicative of different levels of in<sup>fl</sup>uence: $9 =$ strong relationship, 3 = medium/moderate relationship, 1 = weak/ possible relationship and 0 = no relationship [11]. They illustrate the level of correlation between the customer requirements CR(i) and the engineering requirements ER(j) [32]. Whichever set of numbers is chosen, the distribution of the numbers within that set ensures a clear distinction between a weak and a strong correlation.

![](/api/attachments/WRCK6TNG/fulltext/images/071c56e89e8c5b9ac55449a66f3749800755afda1dd39ca0434853eb228e6711.jpg)  
Fig. 2. The house of quality

## 4.1.5. Step 5

Calculate the absolute $\left( I _ { \mathrm { a b s } } \right)$ and relative $\left( I _ { \mathrm { r e l } } \right)$ importance of each engineering requirement on the entire set of customer product requirements. This step identi<sup>fi</sup>es the in<sup>fl</sup>uence of each engineering requirement on the product requirements, thereby populating the two bottom rows of the HoQ [12]. The calculation is performed by taking into consideration the customers' prioritization of their own needs and multiplying these values by the correlation values in the matrix. The resulting values of the absolute and relative importance are a valuable input to the product development process because they express how (non-)signi<sup>fi</sup>cantly a particular engineering requirement can ful<sup>fi</sup>ll the customers' requirements [26].

$$
I _ {\mathrm{abs} E R _ {j}} = \sum_ {i = 1} ^ {n} \left(I C R _ {C R _ {i}} * R E M _ {E R _ {j} C R _ {i}}\right)\tag{1}
$$

$$
I _ {\text { rel } E R _ {j}} = \frac {I _ {\text { abs } E R _ {j}}}{\sum_ {j = 1} ^ {n} I _ {\text { abs } E R _ {j}}} \quad (j \in N; 1 \leq j \leq 7).\tag{2}
$$

## 4.1.6. Step 6

Collect customers' perception of the ful<sup>fi</sup>llment of each of the product requirements (FuCr). This step is akin to asking: “How closely does the product meet each of the requirements?” [13]. In other words, customers' perception of ful<sup>fi</sup>llment of the requirements indicates their opinion of how closely the product meets their requirements [12]. Much like the importance ratings, the ful<sup>fi</sup>llment is rated using a 5-point scale from 1 (not at all ful<sup>fi</sup>lled) to 5 (completely ful<sup>fi</sup>lled).

While the QFD approach has been widely applied (Chan and Wu [10] classify over 650 QFD publications), the approach is not a panacea that solves all design problems and allows the development of perfect products. However, this approach does provide a systematic method for transferring the needs of the customer into concrete product design. While the in<sup>fl</sup>uence and strength ratings require careful interpretation, the HoQ is considered to be a powerful approach for quality management [26].

## 4.2. Quality function deployment-based approach for reference models

While the original aim of QFD was to provide guidance on how to design products that meet customer needs [14], this aim is abstract enough and can be adapted to other domains [9]. Although a QFD-based approach, as far as we are aware, has not been used in the past for the purpose of managing and assessing the quality of conceptual models, applications of it exist outside of the manufacturing domain that demonstrate its <sup>fl</sup>exibility in various situations. For example, QFD has been shown to be a useful approach for decision processes on IT investments [37], electronic marketplaces [35], and in software engineering projects [32]. Such applications require that the original QFD approach be adapted to <sup>fi</sup>t the context of the situations. The required adaptations are generally carried out by changing the focus of the user requirements and engineering requirements. In order to adapt the traditional QFD to the <sup>fi</sup>nancial domain, Kim et al. [37] substitute user requirements with the organization's critical success factors and the engineering requirements with ef<sup>fi</sup>ciency and <sup>fl</sup>exibility factors in relation to IT investment strategies. Similarly, Hopkins and Kehoe [35] apply QFD to determine the quality of electronic marketplaces. They achieve this application by considering the customer requirements of an electronic marketplace as the QFD user requirements and considering the electronic marketplace features as the QFD engineering requirements. Similarly, in our work, we consider the RM users to be the customers, RM model characteristics to be the user requirements, RM developers to be the engineers and the RM development process to be the engineering requirements.

<table><tr><td colspan="3"></td><td colspan="7">RM Development Phases</td></tr><tr><td rowspan="6">RM Characteristics</td><td></td><td>Customer Importance Ratings</td><td>Problem Definition</td><td>Requirement Analysis</td><td>Information Gathering</td><td>Setting Conv.&amp; Rules</td><td>Documentation</td><td>Construction &amp; Design</td><td>Evaluation</td></tr><tr><td>Generality</td><td></td><td rowspan="5" colspan="7"></td></tr><tr><td>Completeness</td><td></td></tr><tr><td>Flexibility</td><td></td></tr><tr><td>Understandability</td><td></td></tr><tr><td>Usability</td><td></td></tr><tr><td colspan="3">Absolute importance</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="3">Relative importance</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Fig. 3. A QFD-based approach for reference models.

In the following, we present the adaptation of the QFD approach to the domain of reference modelling (see Fig. 3). In the initial step, we adapt selected HoQ elements to the <sup>fi</sup>eld of RM. Accordingly, <sup>fi</sup>rst, the customer requirements are identi<sup>fi</sup>ed and we use the <sup>fi</sup>ve RM characteristics (see Section 2.2), which have been consolidated from prior research, as the customer RM requirements. Then, the engineering requirements are related to the various RM development phases (see Section 2.1), which are also consolidated from prior research and further enhanced. These phases lead to the creation of the <sup>fi</sup>nal RM product, with each phase consisting of a number of required activities (see Section 2.1 and Appendix). The ful<sup>fi</sup>llment of all activities within a single development phase ensures that the development phase is complete.

Accordingly, the proportion of the actually performed activities within a development phase to the set of all activities required within a development phase provides a good indication of the degree of phase completion.

The user assessment of the importance of and, later, ful<sup>fi</sup>llment of the RM characteristics follows the HoQ guidelines. Despite academic literature largely treating the <sup>fi</sup>ve RM characteristics as equally important, we argue that organizations might be motivated to prioritize the characteristics (user requirements) based on their needs and their resource availability. Accordingly, the QFD-based approach for RM allows organizations to communicate such preferences. The correlation matrix measures the impact of each development phase on each of the <sup>fi</sup>ve requirements. The {0–1–3–9} weightings are assigned by the RM development project manager, and later used to calculate the absolute and relative importance of each phase on the set of all RM characteristics. These numbers indicate the extent to which a certain development phase impacts the RM characteristics and, thus, can be a valuable communication and planning instrument for the RM developers and related stakeholders.

Having adapted parts of the QFD approach to the reference modelling domain, we now can use the data to measure the overall RM quality. The quality measure is represented by a quality ratio (Eq. (3)) calculated based on user assessment of the importance of the requirements $\left( I _ { \mathrm { r e l } } \right)$ as well as the completeness of the development phases (evidenced by the completed activities and as reported by the RM development project manager).

$$
\text { RMQuality } = \sum_ {j = 1} ^ {7} \left(\text { Performed\_Activities } _ {j} * I _ {\text { rel...Dev\_Phase } _ {j}}\right).\tag{3}
$$

Unlike the customers' requirement ful<sup>fi</sup>llment ratings, which represent a subjective opinion of the quality of the model, the RM quality measure provides an assessment based on the quality of the development process and the user speci<sup>fi</sup>ed importance of the RM characteristics. The ratio provides a single summary measure of the model quality and allows an organization to compare competing RM. Much like <sup>fi</sup>nancial ratios, the quality ratio is limited in the way that it reduces the level of detail to one single number [72]. Considering the pros and cons of using the quality measurement, we calculate the ratio as a means to provide a <sup>fi</sup>nal outcome of the evaluation process that is simple enough to assist in further improvement processes.

## 5. Artifact evaluation approach

This section presents the case study used to evaluate the developed artifact and, thus, describes the case study company, the RM under investigation, and the data collection stages.

## 5.1. Research setting

The initial evaluation of the proposed QFD-based artifact is carried out in a real world setting through a case study at the organization that approached us to develop the artifact. The research team was approached by the German-based Central for Co-Organisation (CCG) and asked to develop a quality management and measurement instrument for CCG's RM development projects. The CCG was founded in 1974 by a German industry consortium and functions as the service and competence centre for cross-company business processes in the German consumer industry (i.e. the organization has substantial expertise and knowledge in RM development). The aim of the organization is to simplify business processes by integrating the <sup>fl</sup>ow of information in supply chains into the <sup>fl</sup>ow of goods. CCG is internationally active and aware of global process standardization activities. Accordingly, we consider it a good candidate for evaluating the QFD-based approach since the organization's focus is not limited to Germany and hence, allows for some generalization of results. For example, the CCG participated in the European Article Number (EAN) organization on the development of the EANCOM standard, which is used worldwide to optimize the electronic exchange of business information [17]. The CCG develops standards that have legal validity and thus, already commits to a high quality development process. It is an accredited body responsible for, among others, the “Data and Movement of Goods in the Consumer Industry” committee within the German International Organization for Standardization (ISO).

Together with the CCG, we selected a new project that focused on developing an Information Flow Logistic RM, which describes the supply chain processes in the consumer industry and speci<sup>fi</sup>cally prescribes the integration of logistic service providers into the supply chain. The project was led by the Efficient Consumer Response initiative, which is an association of European logistic-related companies (German, Austrian, and Swiss) and chaired by the CCG. The developed RM is a textual description of logistic processes, supported by <sup>fl</sup>ow charts and enriched by XML code to ensure the integration into the IT landscape of the companies. It describes modules that de<sup>fi</sup>ne the responsibilities between the industry, the retailers and the service providers. The three basic modules are purchase order processing, transport activities, and warehouse activities. The combination of these modules creates numerous advanced supply processes.

Following the development of the Information Flow Logistic RM with the use of the QFD-based approach, the RM was implemented by a number of CCG customers. These customers were from the European consumer goods industry; retailers, and logistic providers in Germany, Austria, and Switzerland, e.g. Nestle Deutschland AG and the Milupa GmbH [66].

## 5.2. Data collection

The research team was involved throughout the development process. The evaluation of the QFD-based approach required collection of data from the Information Flow Logistic RM users and from the RM developers as well. This data collection incorporated interviews, questionnaires, and the examination of secondary company data and RM development documents. The time frame for the data collection was as follows. The research team was approached by the CCG in January 2004 and observed the model development process from

Table 3  
Descriptive statistics for the model users.

<table><tr><td>Model user</td><td>Department</td><td>Industry</td><td>Headquarters</td></tr><tr><td>A</td><td>Sales management</td><td>Logistic provider</td><td>Austria</td></tr><tr><td>B</td><td>IT integration</td><td>Logistic provider</td><td>Germany</td></tr><tr><td>C</td><td>IT – Division Electronic DataExChange</td><td>Consumer industry</td><td>Germany</td></tr><tr><td>D</td><td>Business development</td><td>Logistic provider</td><td>Germany</td></tr></table>

February 2004 until April 2004. CCG customers implemented the Information Flow Logistic RM in early 2005. The <sup>fi</sup>nal interviews with the RM users were not carried out until December 2006, providing adequate time for the users to develop opinions about ful<sup>fi</sup>llment of the required RM characteristics and a reliable perception, based on their experience with the RM, of the overall RM quality.

## 5.3. Collection of data from model users

The CCG met with the participating organizations of the Efficient Consumer Response initiative (future Information Flow Logistic RM users) twice a year to discuss the development of the Information Flow Logistic RM. The research team attended one of these meetings (March, 2004) and introduced the QFD-based approach. At this time the prioritization of RM characteristics was collected from the users via a questionnaire. A glossary of RM characteristics was provided to the users to increase the consistency and validity of responses. The same group of users implemented the RM after its launch in 2005 and was contacted again in December 2006 to share their experiences. To this end, we again distributed to the model users a questionnaire and a glossary providing de<sup>fi</sup>nitions of the requirements<sup>1</sup>. We then conducted follow-up interviews to gain a deeper understanding and further feedback from the users.

The questionnaire measured the degree of ful<sup>fi</sup>llment of RM characteristics on a 7-point Likert scale. In addition, the overall perception of quality of the RM was captured and users were asked to provide justi<sup>fi</sup>cations for their overall quality assessment. The questionnaire was then followed up by interviews that further probed the reasons for the users' assessment of the degree of RM characteristics ful<sup>fi</sup>llment and the reason for their overall assessment of the RM quality.

The overall assessment of the RM quality was an important aspect of data collection in this evaluation, since it allowed us to then compare the RM quality measure calculated by QFD-based approach with the RM quality perceptions of users who have had the opportunity to interact with the developed RM over an extended period of time. In other words, it was a critical component that allowed us to judge the accuracy of the QFD-based approach quality measure.

We received data from four companies (see Table 3), each represented by their company representative. These representatives were responsible for the introduction, implementation, and the compliance of the RM within their respective organizations, hence, were the best candidates to answer questions relating to RM quality and RM characteristics.

## 5.4. Collection of data from model developers

The research team had access to the Efficient Consumer Response group and their RM developers for the purposes of this project. The CCG and Efficient Consumer Response welcomed the involvement of the research team; hence, we do not foresee issues with collection of false data from the team or its team leader. We interviewed the team leader, as the representative of the RM development team, using a semi-structured interview in order to gain feedback on the RM development phases. The interview protocol was based on the RM development phases, as derived from previous research. The interviewer also used secondary data from company's brochures, white papers, customer information materials, and company's website. Thus, we ensured the consideration of such materials when asking the team leader to articulate and justify the impact of each development phase on the RM characteristics, and, further, also assess which development activities (please see Appendix) were undertaken within the development phases.

The semi-structured interview protocol consisted of two parts. The <sup>fi</sup>rst part investigated the in<sup>fl</sup>uence of each development phase of the <sup>fi</sup>ve customer requirements. The team leader was asked to indicate the extent to which each development phase affects user requirements (using the HoQ {0–1–3–9} classi<sup>fi</sup>cation). To increase the developer's understanding of the meaning of the RM characteristics, a glossary of terms was provided. The result of the <sup>fi</sup>rst step was the complete relationship matrix.

The second part of the interview focused on capturing information about the activities that make up each of the RM development phases. For each activity in the seven development phases, we discussed with the team leader, and also an additional member of the team, which activities were carried out. The agreement on the carried out activities was only recorded when both the team leader and team member indicated in their discussion that the activity was performed and what the activity involved.

Based on the data collected from the RM users and the RM developers, we are now able to demonstrate the application of the QFD-based approach, and also evaluate its RM quality measurement potential.

## 6. Evaluation of the QFD-based approach for reference models

The determination of the Information Flow Logistic RM quality, using the QFD-based approach, delivers a quality ratio based on the quality of development phases and prioritization of RM characteristics. This measure can then be compared to the users' perception of RM quality, which is established after the users have time to interact with the RM, in order to evaluate the usefulness of the quality measurement provided by QFD-based approach.

In this section, we describe the steps required to calculate the RM quality measure. Based on the data collected throughout the evaluation case study, we also provide explanations for reasons why users assess the importance and the degree of ful<sup>fi</sup>llment of RM characteristics at a relatively high level. Further, based on such data, we also <sup>fi</sup>nd that RM developers can in<sup>fl</sup>uence the degree of ful<sup>fi</sup>llment, particularly within the construction and design phases of RM development.

## 6.1. User perspectives on reference model characteristics

The users assessed the importance of the RM characteristics and, later, their degree of ful<sup>fi</sup>llment (see Figs. 4 and 5). Overall, each of the <sup>fi</sup>ve characteristics appears to be important to the RM users. Although the importance ratings are grouped around the values of 6 (on a scale of 7), the completeness RM characteristic seems to be less important. The developed RM model contains process recommendations for an entire industry; hence, it provides a large degree of generality but does not include speci<sup>fi</sup>c logistic processes for a single organization. It became apparent in the study that the users considered a complete RM to be dif<sup>fi</sup>cult to understand because they believed that it would be overloaded and, in certain parts, not relevant. The users agreed that understandability is the most important RM characteristic (importance rating of 7) because it governs the use and implementation of the model in the organization. It also shows that, without understanding, it would be impossible for users to assess the RM. RM that are too dif<sup>fi</sup>cult to understand are unlikely to be implemented. Hence, understandability is an early and important criterion for RM success in an organization, because without RM implementation the model cannot provide its bene<sup>fi</sup>ts.

![](/api/attachments/WRCK6TNG/fulltext/images/c16b6328e7490ada8f6b265d20b29156a0e40fd5280a67f9a69d0bce56099389.jpg)  
Fig. 4. Comparison between importance and ful<sup>fi</sup>llment of the user requirements

Besides being complete and understandable, an RM should also be flexible and usable — both requirements are important for the user because <sup>fl</sup>exibility and usability allow integration of the RM into the organization. The users consider the RM to be a recommendation based on which processes still can be designed <sup>fl</sup>exibly. The generality of the model was also important to the users. They recognize that a lack of generality might impact the ability to reuse the model.

After implementation of the RM, and after an extended period of use, the users evaluated all requirements on a high ful<sup>fi</sup>llment level. Consequently, the users perceived the RM as being bene<sup>fi</sup>cial for their organization and also being of high quality. The generality (with a value of 5.75) and completeness characteristics (5.75) were found to be assessed 0.5 points lower than the other three characteristics (6.26). Follow-up interviews revealed that the difference appears to exist because generality and completeness are to some extent mutually exclusive (see Section 2.2) and neither can be ful<sup>fi</sup>lled when the other is. Therefore, users evaluate both with a slightly lower rating.

## 6.2. Developer perspectives on development phases

The developer perspective is the developer's re<sup>fl</sup>ection on the steps taken to develop the RM. Each phase in the seven-phase development process may have a different level of in<sup>fl</sup>uence on RM characteristics. In addition, each development phase is characterized by a <sup>fi</sup>nite number of activities, the ful<sup>fi</sup>llment of which re<sup>fl</sup>ects the extent to which the developers completed each of the development phases. Table 4 compares the calculated relative importance of each development phase and the extent of activities conducted in each of the development phases.

The data shows that the construction and design phase has the highest perceived in<sup>fl</sup>uence on all RM characteristics, followed by the problem de<sup>fi</sup>nition phase. The lowest perceived in<sup>fl</sup>uence on the characteristics is exhibited by the phases of setting conventions and rules and evaluation. Not surprisingly, the design and construction phase exerts the most in<sup>fl</sup>uence because this is the phase in which the RM emerges. The developers reached an activity rating of 0.8 for this phase because they did not consider competing RM and included only organization-owned RM. This decision was motivated by the need to keep the RM neutral and open. The missing framework orientation is another weakness in this phase, however, the collaboration among the developers, users, and experts ensured that a high level of activities was ful<sup>fi</sup>lled. In the <sup>fi</sup>rst phase, the developers achieved only an average activity level of 0.67 because the description of views on the target market did not take place. However, the developers included in the de<sup>fi</sup>nition phase the identi<sup>fi</sup>cation of the target group, the de<sup>fi</sup>nition of the project goals, and the achievement of consensus among the participants. The documentation of the development process was comprehensive and included information about project meetings and outcomes, the various versions of the RM, and changes of the model during development. Therefore, the activity level in this phase was ranked at 1.0, hence, the phase is considered to be fully completed.

In contrast, the phase of information gathering achieved the lowest assessment level because activities such as surveys with broader user involvement, use of academic literature, etc., were not carried out.

## 6.3. Development of the quality function deployment-based matrix

Fig. 5 presents the HoQ adaptation with correlations, RM characteristic prioritization, and RM characteristics ful<sup>fi</sup>llment assessments.

The data shows that RM characteristics of generality and completeness can be in<sup>fl</sup>uenced by the <sup>fi</sup>rst three development phases. The completeness of the RM, in particular, is achieved in these three development phases and the developers do not expect that later phases can enhance ful<sup>fi</sup>llment of this requirement. In contrast, generality can also be impacted during the construction phase because elements and processes that are too detailed can be left out.

<table><tr><td colspan="3"></td><td colspan="7">RM Development Phases {0-1-3-9}</td><td></td></tr><tr><td rowspan="6">RM Characteristics</td><td></td><td>Customer Importance Ratings {1-2-3-4-5}</td><td>Problem Definition</td><td>Requirement Analysis</td><td>Info Gathering</td><td>Setting Rules</td><td>Documentation</td><td>Design</td><td>Evaluation</td><td>Customer Fulfillment Rating {1-2-3-4-5}</td></tr><tr><td>Generality</td><td>6.5</td><td>9</td><td>9</td><td>9</td><td>1</td><td>3</td><td>9</td><td>3</td><td>5.75</td></tr><tr><td>Completeness</td><td>5.5</td><td>9</td><td>9</td><td>9</td><td>1</td><td>3</td><td>3</td><td>3</td><td>5.75</td></tr><tr><td>Fexibility</td><td>6.5</td><td>3</td><td>3</td><td>1</td><td>1</td><td>3</td><td>9</td><td>0</td><td>6.25</td></tr><tr><td>Understand- ability</td><td>7.0</td><td>9</td><td>3</td><td>3</td><td>9</td><td>9</td><td>9</td><td>0</td><td>6.25</td></tr><tr><td>Usability</td><td>6.5</td><td>3</td><td>3</td><td>3</td><td>1</td><td>3</td><td>9</td><td>9</td><td>6.25</td></tr><tr><td colspan="3">Absolute importance</td><td>210</td><td>168</td><td>155</td><td>88</td><td>138</td><td>255</td><td>94.5</td><td rowspan="2"></td></tr><tr><td colspan="3">Relative importance</td><td>0.1894</td><td>0.1516</td><td>0.14398</td><td>0.0794</td><td>0.1245</td><td>0.23</td><td>0.0853</td></tr></table>

Fig. 5. QFD-based approach for the reference model information flow logistic.

Table 4  
Importance of the development phases and the activities.

<table><tr><td>Development phases</td><td>Relative importance</td><td>Activity fulfillment {0...1}</td></tr><tr><td>Problem definition</td><td>18.94%</td><td>0.67</td></tr><tr><td>Requirement analysis</td><td>15.16%</td><td>0.75</td></tr><tr><td>Information gathering</td><td>13.98%</td><td>0.50</td></tr><tr><td>Setting conventions and rules</td><td>7.94%</td><td>0.80</td></tr><tr><td>Documentation</td><td>12.45%</td><td>1.00</td></tr><tr><td>Construction and design</td><td>23.00%</td><td>0.80</td></tr><tr><td>Evaluation</td><td>8.53%</td><td>0.83</td></tr></table>

The most important (as speci<sup>fi</sup>ed by the users) RM characteristic, the understandability of the RM, is affected by latter development phases as well as problem de<sup>fi</sup>nition. Reaching agreement among the users about the RM goals, processes covered, and target market in the <sup>fi</sup>rst development phase supports the ease of understanding of the RM. The guidelines for the development, the documentation and the modeling mainly in<sup>fl</sup>uence how the RM customers understand the model.

## 6.4. Determination of the quality of the RM

During the second round of questionnaires and interviews, the four organizations who implemented the RM, following its development, were asked to estimate (on a scale of 1–7) the overall quality of the RM and further provide a justi<sup>fi</sup>cation for this estimate (this additional step was used to encourage critical re<sup>fl</sup>ection rather than a quick assessment). Two of the four organizations (A and D in Table 4) perceived the RM quality as very good (6), and two organizations (B and C in Table 4) perceived the quality as good (5). With these perceived quality assessments we calculated an estimated overall quality of 78.57% [(2⁎6+2⁎5)/(4⁎7)].

The QFD-based approach, on the other hand, calculates the quality ratio for the RM “Information Flow Logistic” to be 0.7533 (Eq. (3), Section 4.2). This quality measurement corresponds with a quality level of 75.33%. Hence, the difference between the quality measurement by the QFD-based approach and the quality perception by the users is only 3.24%. While more case studies are required in order to create a large data set of consistent relationships between the measured quality and the perceived quality, the initial evaluation case study points to a reliable and accurate measurement instrument.

## 6.5. Comparing the quality of reference models

While we show that the outcome of the QFD-based measures correlates with the users' estimations, due to lack of other data we cannot determine the quality of the RM in comparison to other models. This assessment requires the existence of a benchmark. In the absence of this benchmark we can, however, perform simulations of RM quality. RM quality depends on the degree of the activities carried out in the development phases by the developers. In RM development projects these activities can vary based on which activities are conducted. We perform the simulation using Crystal Ball 7 Professional Edition (by Decisioneering, Denver, CO). Running a brute-force simulation that calculates the RM quality within 10,000 trials indicates that the RM quality can be generally expected to be between 0.2307 and 0.8694 when different levels of activities are considered. In our simulation an RM can never achieve a quality of 1.00 because, while the performed activities are varied, the values of the second factor in the multiplication (importance of the phases) are not at their optimum. In the simulation, the mean quality is 0.5845, which indicates that the RM quality (0.7533) for Information Flow Logistic is relatively high in relation to this benchmark.

The sensitivity chart in Fig. 6 shows the extent to which each phase can impact the RM quality and, thus, which phase drives the uncertainty in the forecast for the RM quality. Consistent with our <sup>fi</sup>ndings from the case study, the construction and design phase has the biggest impact and emphasizes the need to carry out all activities in this development phase. The evaluation and setting conventions and rules phases have a lesser impact and the development activities contribute only partly to the overall RM quality.

## 7. Conclusions

This study is the <sup>fi</sup>rst to recognize the usefulness of a QFD-based approach for conceptual models, in particular RM. The study provides three main contributions. First, the proposed QFD-based approach incorporates the voice of the RM users and presents a compressed measure for the quality of such models as well as a means for the management of quality RM development. Thus, it allows for better communication between the users and the developers, an easier means of comparing quality of different RM versions, as well as development of higher quality RM. Second, our research consolidates disparate literature on RM characteristics and identi<sup>fi</sup>es <sup>fi</sup>ve required characteristics of such models, viz. generality, <sup>fl</sup>exibility, usability, completeness, and understandability. Third, our research contributes to the creation of a cumulative tradition in RM development. We consolidate guidelines for RM development from various works into a seven-phase development approach, in which each phase is characterized by different activities that need to be carried out in order for the phase to be successfully completed.

![](/api/attachments/WRCK6TNG/fulltext/images/757cab8fc53885ab8075b2410aaeab2645d1dc666da9b7ee699fb9f38cbb0deb.jpg)  
Fig. 6. Variation of the degree of development activities.

In this paper, we also present the initial evaluation of the proposed QFD-based artifact in one in-depth case study. Through the empirical component of this study, we are able to not only show the accuracy of the measurement instrument, but also discuss the user and developer assessments of different aspects of the RM development. Moreover, due to lack of data at this stage, we run a simulation to determine benchmarks for RM quality and compare the chosen RM to these values.

We see our work as relevant to the research and practice communities. The contributions are two-fold. First, through the innovative adaptation of the QFD approach, hence, adding to the QFD body of research. Second, through the consolidation of existing English and German literature on RM characteristics and development approaches, and the development of the measurement instrument that incorporates both these factors. The contribution to industry is also twofold. First, for users, the QFD-based approach is an instrument that enables easy comparison of quality of RM versions, and, hence, helps guide the RM selection and revision process. Second, the identi<sup>fi</sup>cation of how to develop RM may assist development organizations in increasing the maturity of their work, consequently, positively in<sup>fl</sup>uencing the quality of the RM they develop. Finally, the activities de<sup>fi</sup>ned in the various development phases can guide the developers in the development phases and hence, contribute to the overall RM quality.

The limitations of the study are related to data collection and analysis. While every effort was taken to eliminate bias, it is possible that the focus on organizations from one region and from one industry is a source of bias. Also, the data collection carried out by the research team with the developer organization may have been in<sup>fl</sup>uenced by the researchers' background. One might perceive the subjectivity of the QFD-based approach as another limitation because non-objective measures are used to determine the quality.

Future research can proceed in a number of directions. The QFDbased approach is a Design Science artifact that should be applied in further case studies to evaluate its usefulness. Further research can also focus on the application of the instrument for in-depth longitudinal case studies. Also, while the QFD-based approach assesses the quality of an RM developed for German speaking organizations of the consumer goods industry, it would be interesting to see the differences of the user importance and ful<sup>fi</sup>llment assessments in other industries and regions with the same RM.

## Acknowledgments

The authors are thankful to Nicole Sunke for her assistance with the data collection for this study and to Werner Esswein for his valuable comments and feedback during the early stage of the research. The authors would like to extend their thanks to the participants of a University of New South Wales workshop, and at the International Conference on Electronic Commerce (2004), as well as two anonymous reviewers and the editor for comments, ideas, and suggestions.

## Appendix

Development phases and phase activities.

<table><tr><td>Development phase</td><td>Activity in each of the development phases</td></tr><tr><td>Problem definition</td><td>1.1 Identify boundary of the relevant scope1.2 Describe the target market1.3 Determine RM users1.4 Achieve consensus on the participants1.5 Define the purpose of the project and model1.6 Identify the target process</td></tr></table>

(continued)Appendix (continued)

<table><tr><td>Development phase</td><td>Activity in each of the development phases</td></tr><tr><td>Requirement analysis</td><td>2.1 Determine alternatives2.2 Analyse for suitable modelling techniques2.3 Select the level of detail2.4 Analyse visualization preferences2.5 Investigate the market for existing models for the domain2.6 Industry analysis (trends and developments)2.7 Analysis of suitable technologies (e.g. XML)2.8 Effort estimation</td></tr><tr><td>Information gathering</td><td>3.1 Interview domain experts and users3.2 Use of published materials3.3 Use of research publications3.4 Conduct a survey with potential RM customers3.5 Consider existing processes or reference models3.6 Identify further sources of information and their quality</td></tr><tr><td>Setting conventions and rules</td><td>4.1 Develop a glossary4.2 Define name conventions for the RM components4.3 Define conventions for the working environment (e.g. systems and available resources)4.4 Select a modelling technique4.5 Carry out a detailed specification of the layout</td></tr><tr><td>Documentation</td><td>5.1 Document the subjective problems of the parties (participants)5.2 Document the agreement process and reached consensus5.3 Document the development steps5.4 Document the modelling and configuration options</td></tr><tr><td>Construction and design</td><td>6.1 Ensure adherence to a framework and modeling from top down6.2 Ensure intensive exchange between model developers6.3 Ensure use of existing RM6.4 Consider interlinks/interconnections with other models6.5 Follow the set conventions</td></tr><tr><td>Evaluation</td><td>7.1 Continually evaluate the construction7.2 Perform a final internal evaluation by developer7.3 Carry out RM user evaluation7.4 Evaluate graphical attributes (e.g., user understanding of constructs)7.5 Ensure continual RM improvement (with close contacts to model users)7.6 Update the RM in line with emerging technologies</td></tr></table>

## References

[1] N. Ahituv, M. Hadass, S. Neumann, A <sup>fl</sup>exible approach to information system development, MIS Quarterly 8 (2) (1984)

[2] F. Ahlemann, H. Gastl, Process model for an empirically grounded reference model construction, in: P. Fettke, P. Loos (Eds.), Reference Modeling for Business Systems Analysis, Idea Group Hershey, 2007.

[3] Y. Akao, Quality Function Deployment: Integrating Customer Requirements into Product Design, Productivity Press, Cambridge, 1990 Translated by Mazur, G.

[4] AML, Anti-Money Laundering and Counter-Terrorism Financing Amendment Act 2007, Act — C2007A00052, 18/04/2007.

[5] D. Avison, G. Fitzgerald, Information systems development, in: W. Currie, B. Galliers (Eds.), Rethinking Management Information Systems: an Interdisciplin ary, Oxford University Press, 1999.

[6] W. Bandara, G. Gable, M. Rosemann, Factors and measures of business process modelling: model building through a multiple case study, European Journal of Information Systems 14 (4) (2005).

[7] J. Becker, P. Delfmann, R. Knackstedt, D. Kuropka, Kon<sup>fi</sup>gurative Referenzmodellierung, in: Becker Knackstedt (Ed.), Wissensmanagement mit Referenz­modellen: Konzepte für die Anwendungssystem- und Organisationsgestaltung, Heidelberg Physica, 2002.

[8] I. Benbasat, D. Goldstein, M. Mead, The case research strategy in studies of information systems, MIS Quarterly 11 (3) (1987).

[9] E. Burke, J. Kloeber, R. Deckro, Using and abusing QFD scores, Quality Engineering 15 (1) (2002).

[10] L. Chan, M. Wu, Quality function deployment: a literature review, European Journal of Operational Research 143 (3) (2002)

[11] L. Chan, M. Wu, Quality function deployment: a comprehensive review of its concepts and methods, Quality Engineering 15 (1) (2002).

[12] D. Clausing, Total Quality Development: A Step-By-Step Guide to World Class Concurrent Engineering, American Society of Mechanical Engineers, Cambridge Massachusetts, 1994.

[13] L. Cohen, Quality Function Deployment: How to Make QFD Work For You, Addison-Wesley, Massachusetts, 1995.

[14] J. Cristiano, J.K. Liker, C. White, Customer-driven product development through quality function deployment in the U.S. and Japan, Journal of Product Innovation Management 17 (4)(2000).

[15] A. Daniels, D. Yeates, Basic Training in Systems Analysis, Pitman, London, 1971.

[16] G. Delano, G.S. Parnell, C. Smith, M. Vance, Quality function deployment and decision analysis: a R&D case study, International Journal of Operations and Production Management 20 (5) (2000).

[17] EANCOM, EANCOM<sup>®</sup> 2002 Syntax 4 User Manual (based on UN/EDIFACT Syntax 4), EAN International, Brussels Belgium, 2002

[18] K. Eisenhardt, Building theories from case study research, Academy of Manage ment Review 14 (4) (1989).

[19] W. Esswein, S. Zumpe, N. Sunke, Identifying the quality of e-commerce reference models, Proceedings of the Sixth International Conference on Electronic Commerce 2004, Delft, Netherlands, ACM Press, New York NY, 2004.

[20] P. Fettke, P. Loos, Classi<sup>fi</sup>cation of reference models — a methodology and its application, Information Systems and e-Business Management 1 (1) (2003).

[21] P. Fettke, P. Loos, Der Beitrag der Referenzmodellierung zum Business Engineering, HMD — Praxis der Wirtschaftsinformatik 241 (2005).

[22] P. Fettke, P. Loos, in: P. Fettke, P. Loos (Eds.), Perspectives on Reference Modeling, Reference Modeling for Business Systems Analysis, Idea Group Hershey, 2007.

[23] P. Fettke, P. Loos, J. Zwicker, Business process reference models: survey and classi<sup>fi</sup>cation, Proceedings of Workshop on Business Process Reference Models (BPM 2005 Workshops), 2005.

[24] U. Frank, Evaluation of reference models, in: P. Fettke, P. Loos (Eds.), Reference Modeling for Business Systems Analysis, Idea Group Hershey, 2007.

[25] C. Ghezzi, M. Jazayeri, D. Mandrioli, Fundamentals of Software Engineering Prentice Hall, Upper Saddle River NJ, 2002.

[26] C. Grovers, What and how about quality function deployment (QFD), International Journal of Production Economics 46-47 (December 1996)

[27] S. Haag, M. Raja, L. Schkade, Quality function deployment usage in software development, Communication of the ACM 39 (1) (1996).

[28] C. Hammel, Generische Spezi<sup>fi</sup>kation betrieblicher Anwendungssysteme, Shaker, Aachen, 1999.

[29] A. Hars, Referenzdatenmodelle: Grundlagen ef<sup>fi</sup>zienter Datenmodellierung Gabler, Wiesbaden, 1994.

[30] J. Hauser, D. Clausing, The house of quality, Harvard Business Review 66 (3) (1988)

[31] G. Herzwurm, QFD, in: K. Landau (Ed.), Lexikon Arbeitsgestaltung, Gentner Stuttgart, 2007, & ergonomia.

[32] G. Herzwurm, S. Schockert, The leading edge in QFD for software and electronic business, International Journal of Quality & Reliability Management 20 (1) (2003).

[33] A. Hevner, S. March, J. Park, S. Ram, Design science in information systems research, MIS Quarterly, 28 (1) (2004).

[34] W. Höhnel, D. Krahl, D. Schreiber, Lessons learned in reference modeling, in: P. Fettke, P. Loos (Eds.), Reference Modeling for Business Systems Analysis, Idea Group Hershey, 2007.

[35] J. Hopkins, D. Kehoe, The theory and development of a relationship matrix-based approach to evaluating e-marketplaces, Electronic Markets 16 (3) (2006).

[36] M. Hopper, J. Stainsby, Principles-based regulation? Better regulation? Journal of International banking law and regulation 21 (7) (2006).

[37] S.H. Kim, D.H. Jang, D.H. Lee, S.H. Cho, A methodology of constructing a decision path for IT investment, Journal of Strategic Information Systems 9 (1) (2000).

[38] M. Krishnan, A. Houshman, QFD in academic: addressing customer requirements in the design of engineering curricula, Proceedings of the 5th Symposium on Quality Function Deployment, June 1993, Novi Michigan, 1993.

[39] O.I. Lindland, G. Sindre, A. Solvberg, Understanding quality in conceptual modeling, IEEE Software 11 (2) (1994).

[40] M. Mahmood, System development methods—a comparative investigation, MIS Quarterly 11 (3) (1987).

[41] M. McDonald, T. Nunno, Creating enterprise leverage, The 2007 CIO Agenda, Gartner, January 2007.

[42] M. McDonald, T. Nunno, D. Aron, Making the difference, The 2008 CIO Agenda, Gartner, January 2008.

[43] M. McDonald, M. Blosch, T. Jaffarian, L. Mok, S. Stevens, Growing IT's contribution, The 2006 CIO Agenda, Gartner, January 2006.

[44] D. Menasce, A reference model for designing an e-commerce curriculum, IEEE Concurrency 8 (1) (2000).

[45] V. Mišic, J. Zhao, Evaluating the quality of reference models. In Proceedings of 19th International Conference on Conceptual Modeling. A. Laender, S. Liddle, V. Storey (eds.), Salt Lake City, Utah, USA, 9–12 October 2000. Lecture Notes in Computer Science 1920, Springer, (2000).

[46] D. Moody, Theoretical and practical issues in evaluating the quality of conceptual models: current state and future directions, Data & Knowledge Engineering 55 (3) (2005).

[47] D. Moody, G. Shanks, What makes a good data model? Evaluating the quality of entity relationship models, in: P. Loucopolous (Ed.), Proceedings of the 13th International Conference on the Entity Relationship Approach, England, Manchester, December 14–17 1994.

[48] D. Moody, G. Shanks, Improving the quality of data models: empirical validation of a quality management framework, Information Systems 28 (6) (2003).

[49] E. Mustonen-Ollila, K. Lyytinen, How organizations adopt information system process innovations: a longitudinal analysis, European Journal of Information Systems 13 (1) (2004).

[50] H. Österle, Business Engineering: Prozess- und Systementwicklung, Springer, Berlin. 1995.

[51] H. Österle, Business in the Information Age, Springer, Berlin, 1995

[52] H. Österle, W. Brenner, K. Hilbers, Total Information Systems Management — An European Approach, John Wiley & Sons, Chichester, 1993.

[53] B. Prasad, Review of QFD and related deployment techniques, Journal of Manufacturing Systems 17 (3) (1998).

[54] T.S. Raghu, A. Vinzea, A business process context for knowledge management, Decision Support Systems 43 (3) (2007).

[55] J. Remmert, Referenzmodellierung von Prozessketten als Instrument des Supply Chain Manangements, in: W. Dangelmaier, A. Ammrich, D. Kaschula (Eds.), Modelle im E-Business, 2000, Paderborner Frühjahrstagung, Fraunhofer ALB, Paderborn.

[56] M. Rosemann, Using reference models within the enterprise resource planning lifecycle, Australian Accounting Review 3 (22) (2000).

[57] M. Rosemann, R. Schütte, Multiperspektivische Referenzmodellierung, in: J. Becker, M. Rosemann, R. Schütte (Eds.), Referenzmodellierung: State-of-the-Art und Entwicklungsper-spektiven, 1999, Physica Heidelberg.

[58] M. Rosemann, W.M.P. van der Aalst, A con<sup>fi</sup>gurable reference modelling language, Information Systems 32 (1) (2007).

[59] A.W. Scheer, Architecture of Integrated Information Systems: Foundations of Enterprise Modeling, Springer, Berlin, 1992.

[60] A.W. Scheer, Business Process Engineering: Reference Models for Industrial Enterprises, Springer, Berlin, 1994.

[61] A.W. Scheer, ARIS House of Business Engineering — Konzept zur Beschreibung und Ausführung von Referenzmodellen. Proceedings of the workshops, in: J. Becker, M. Rosemann, R. Schütte (Eds.), Entwicklungsstand und Entwicklungsperspektiven der Referenzmodellierung, Münster, Germany, 1997.

[62] B. Schlagheck, Objektorientiere Referenzmodelle für das Prozeß- und Projektcontrolling Grundlagen – Konstruktion – Anwendungsmöglichkeiten, Gabler, Wiesbaden, 2000.

[63] R. Schütte, Referenzmodellierung: Anforderungen der Praxis und methodische Konzepte, in: M. Maicher, H.-J. Scheruhn (Eds.), Informationsmodellierung: Referenzmodelle und Werkzeuge, Gabler, Wiesbaden, 1998.

[64] R. Schütte, T. Rotthowe, The guidelines of modeling — an approach to enhance the quality in information models, Proceedings of 17th International Conference on Conceptual Modeling (ER), Springer, 1998.

[65] A. Schwegman, Objektorientiere Referenzmodellierung: theoretische Grundlagen und praktische Anwendung, Gabler, Wiesbaden, 1999.

[66] R. Strand, An einem Strang ziehen, GS1 Magazin 25 (4) (2006).

[67] L. Sullivan, Quality function deployment, Quality Progress 19 (6) (1986).

[68] C. Taylor, Reference Process Model for Enterprise Systems Administration. Master Thesis, QUT Australia (2003).

[69] C. Taylor, W. Sedera, De<sup>fi</sup>ning the quality of business process reference models, Proceedings of the 14th Australasian Conference on Information Systems, Australia, 2003.

[70] O. Thomas, Understanding the term reference model in information systems research: history, literature analysis and explanation, Proceedings of the Workshop on Business Process Reference Models (BPRM 2005), Nancy, France, September 5, 2005.

[71] O. Thomas, A.W. Scheer, Tool support for the collaborative design of reference models—a business engineering perspective, Proceedings of the 39th Annual Hawaii International Conference on System Sciences Hawaii, 2006.

[72] G. White, A. Sondhi, D. Fried, The Analysis and Use of Financial Statements, Wiley Hoboken, New Jersey, 2003.

[73] R. Winter, J. Schelp, Reference modeling and method construction: a design science perspective, Proceedings of the 2006 ACM Symposium on Applied Computing (SAC), France, Dijon, 2006.

[74] WinterGreen Research, Business Process Management (BPM) — Market Opportunities, Strategies, and Forecasts, 2006 to 2012, Report # SH29821474 (2006)

[75] C. Wolf, P. Harmon, The State of Business Process Management—2006, 2006 www. BPTrends.com.

[76] M. Wolfe, Developmentof the city of quality: a hypertext-based group decision support system for quality function deployment, Decision Support Systems 11 (3) (1994)

[77] R. Yin, Case Study Research, Sage, Beverly Hills CA, 1984.

[78] S. Zumpe, W. Esswein, N. Sunke, M. Thiele, Die Qualität von Referenzmodellen im E-Commerce Dresdner Beiträge zur Wirtschaftsinformatik N. 47 Technica University of Dresden, Dresden, 2005.

![](/api/attachments/WRCK6TNG/fulltext/images/8cc252ec27c98f7b50203952c3dc652d15901acefd69493c39eb5823a9014a19.jpg)

![](/api/attachments/WRCK6TNG/fulltext/images/7733b07f9e11ed7987fb9ab6e2717bd09b4008ac6f1a5cf8de726dd69852f290.jpg)  
Sabine Matook is a Senior Lecturer in Information Systems at the UO Business School The University of Oueensland She received her doctoral degree from the Technical University of Dresden, Germany. Her research interests are in the area of IT strategy, IS use and adoption, and electronic business. Her work has appeared or is forthcoming in The Journal of Strategic Information Systems, Journal of Electronic Commerce Research, International Journal of Operations & Production Management and Informatikspektrum. Dr. Matook has presented research papers at a variety of international conferences, including the International Conference on Information Systems and the International Conference on Electronic Commerce.

Marta Indulska is a Lecturer at the UO Business School. The University of Queensland. She obtained her PhD in Computer Science, in the research area of Information Systems, at the University of Queensland, in 2004. Marta's main research interests are conceptual modeling and Business Process Management. She has published and presented her work at numerous international conferences. Her work has also been published by journals such as IEEE Transactions on Knowledge & Data Engineering, and Data & Knowledge Engineering. Her teaching focuses on topics in Information Systems and globalization.
