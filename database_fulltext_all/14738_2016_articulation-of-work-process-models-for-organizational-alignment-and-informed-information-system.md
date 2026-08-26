---
otero_id: 14738
otero_key: "8AEU7ZHB"
title: "Articulation of work process models for organizational alignment and informed information system design"
authors: "Stefan Oppl"
year: "2016"
journal: "Information & Management"
doi: "10.1016/j.im.2016.01.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Articulation of work process models for organizational alignment and informed information system design

Stefan Oppl \*

Johannes Kepler University of Linz, Department of Business Information Systems – Communications Engineering, Altenberger Strasse 69, 4040 Linz, Austri

## A R T I C L E I N F O

Article history: Received 4 March 2015 Received in revised form 23 November 2015 Accepted 17 January 2016 Available online xxx

Keywords: Collaborative articulation of work Conceptual modeling of communication and work processes Domain expert-driven modeling Bottom-up organizational development

## A B S T R A C T

Articulating and representing procedural aspects of work in conceptual models is a prerequisite for informed information system (IS) design. Instruments supporting articulation need to establish common ground about the interaction of the collaborating actors. This article proposes a methodology for the articulation of work processes by inexperienced modelers. It consists of phases of articulation and consolidation of case-based models and interactive elaboration toward comprehensive representation of the process via virtual enactment. The resulting models can be directly interpreted by IS. A case study confirms that the methodology meets the identified requirements and identifies areas of improvement. - 2016 Elsevier B.V. All rights reserved.

## 1. Introduction

Changes to business processes have an impact on how people work and collaborate within organizations. Being able to quickly adapt business processes to external or internal influencing factors is crucial in the present ever-changing business environment. Remaining competitive in such environments, which are characterized by highly dynamic market requirements and increased employee mobility, is dependent on being able to acquire knowledge about work processes and their context from experienced workers [1] and represent it in a way that makes it accessible for and adaptable to future work situations and new employees [62]. Representing work processes through conceptual modeling is a recognized means of making them visible and adaptable to changing organizational or business requirements, particularly by using them to design and configure information systems (IS) [6]. Failing to involve operative personnel in projects affecting work processes and IS results in ignorance [33] and ultimately leads to ineffectiveness and unclear responsibilities [61].

The existing literature (e.g., [24,50]) shows that this challenge can be met by involving operative staff in conceptual modeling activities, but also indicates that such an approach introduces challenges in the process of modeling that have to be addressed methodologically. People operatively involved in work processes (referred to as ‘‘actors’’ in the following) are domain experts with extensive knowledge about their respective roles in a work process, but normally have little methodological knowledge about modeling [51]. Their role in traditional IS-oriented modeling approaches is thus widely reduced to providers of domain knowledge for expert modelers [46]. An expert-mediated approach of representing work process knowledge in conceptual models bears the risk of introducing the expert modeler’s own bias regarding which information should be represented in the model and the interpretation of vague or conflicting statements provided by the actors [20]. This not only negatively affects actors’ ability to interpret the information represented in a model [33], but also leaves unresolved potential misconceptions or conflicting understanding of work among the involved actors [24,47]. The aim of this article is to introduce a model elicitation approach, which is driven by actors and allows them to articulate and align their views on a work process, and still leads to a syntactically correct and semantically sound process model for further processing in IS.

From a practical perspective, organizations would benefit from such an approach as it supports operative staff to align conflicting understandings and resolve misconceptions about their work. This reduces the effects of unforeseen contingencies [65] and allows to identify potential for improvement in the overall work process [15]. As the work process usually is shaped and supported by IS, these aligned views should be reflected in the models used to design these systems to appropriately support the work process [42].

S. Oppl / Information & Management xxx (2016) xxx–xxx

Involving actors in modeling activities has been addressed in several fields of research. In the field of system dynamics, approaches such as those of Vennix et al. [68] or Franco and Rouwette [17] focus on involving actors and resolving conflicting viewpoints as noted above. The resulting models, however, are not intended for the development of socio-technical support in IS. Research in the area of business process modeling shows that established formal modeling languages such as Business Process Modeling and Notation (BPMN) [70] are used for modeling driven by actors (e.g., [40]), but lead to the sacrifice of formal correctness and semantic completeness for usability [48], which makes them of limited use for further processing. A third strain of research in the area of socio-technical system design focuses on collaboratively capturing information about work processes from actors by providing notations explicitly tailored for understandability and easy use (e.g., [2,25,29]), while still maintaining a link toward technical interpretability of the created models. The task of transforming these models to representations that can be processed in IS, however, is left to expert modelers (e.g., [58]). Margaria et al. [41] argue in favor of a simple modeling approach that allows actors to create directly executable role-based workflow models and present a framework on how this aim can be achieved with modeling support tools. Fahland and Weidlich [10] and Kabicher and Rinderle-Ma [35] argue in favor of approaching actors with a case- or scenario-based approach to modeling, respectively, in which elicitation focused on capturing case-based process fragments, which are later (semi-)automatically aggregated to form a complete model of the process.

All of the aforementioned approaches aim at facilitating work modeling by actors without formal process modeling experiences. They either focus on supporting actors’ needs in a collaborative modeling process or aim at producing executable models that can be processed directly in IS. The challenges addressed in both areas are of high relevance for the aim of involving actors in IS design, but have not yet been addressed in an integrated approach. This article addresses this issue and introduces a methodology to facilitate actors’ collaborative articulating of their work processes. It furthermore presents a support tool for conflict resolution and model elaboration, leading to formally correct models that are necessary for technical processing in IS.

Collaborative articulation of work process models should lead to common ground [5] for all involved actors and serve as an agreedupon basis for further use. This is necessary, because actors’ mental models of how they contribute to a work process and how they interact with each other can be assumed to be inconsistent [65]. This eventually leads to problems in collaboration [68]. Existing work on collaborative conceptual modeling hardly addresses explicitly the differences in how people perceive collaborative work processes [52]. Also, no account is given on how to resolve these differences to an extent that allows reaching common ground on how to collaborate [57]. The methodology presented in this article contributes to this area of research by introducing a modeling method that makes visible differences in understanding and requires resolving them to be able to finish the modeling process.

The research reported on in this article methodologically follows a design science approach [26]. The modeling approach and the proposed tools are to be considered the designed artifacts. Although involving operatively active people in the work process modeling for the sake of IS design has been recognized as a relevant field of study, the rationale of this study is that no approach so far has addressed how to support the process of articulating and aligning potentially conflicting views on work processes while still maintaining a model representation that can be directly processed in IS. The contribution of this study is a methodology that enables nonexpert modelers to collaboratively create conceptual models of a shared work process by articulating and aligning their individual views on the work process. The resulting models are technically interpretable in IS. The method ology is supported by a set of tools that facilitate articulation, alignment, and conceptual modeling to achieve these ends. Research rigor is ensured by deriving the designed artifacts requirements from the relevant literature in the fields of articulation support in collaborative settings and conceptual modeling support for inexperienced modelers. This brings together the research domains that are relevant as indicated in the design rationale. The artifact design process solely is based on these requirements. Consequently, evaluation in this article focuses on assessing whether these requirements have been met. A case study has been conducted to evaluate the designed artifacts in the intended field of application, and to identify the potential advantages and areas of improvement for the results presented.

The remainder of this article is organized as follows. In Section 2, we elaborate on the question of how conceptual modeling can be adopted for articulation support. In Section 3, the methodology designed to meet these requirements is introduced and described in detail. A brief description of the tools that have been developed to support the different methodological phases closes Section 3. In Section 4, the case study used to examine if the proposed modeling approach meets the identified requirements is presented. The article concludes with an account of the limitations of the presented research and a discussion on the potential for future methodological and technical developments.

## 2. Conceptual modeling for articulation support

Representing the procedural aspects of work in conceptual models is one prerequisite for informed IS design [6]. Commonly adopted modeling languages such as BPMN [70] and event-driven process chain (EPC) [44] provide constructs to describe the activities that constitute a work process and their causal relationships. Most of these modeling languages aim at representing models for further processing by means of technology (such as simulation or workflow execution; see [6]). Conceptualizing work in a technically interpretable manner, however, is not always feasible when capturing information about work processes from inexperienced modelers. People’s mental models about their work processes are likely to be incomplete and inconsistent [60]. When using a modeling language oriented toward technical interpretability [38], its semantically exact specified constructs might be too limiting to fully capture the information that people articulate based on their mental models [11].

This challenge has been recognized for years in the area of socio-technical systems design [24]. One approach to overcome modeling constraints imposed by model semantics is to explicitly allow for vagueness in the models, deliberately leaving aside information that is incomplete or inconsistent at the time of modeling. This approach is implemented in modeling languages such as SeeMe [23], which explicitly introduces a construct to express vagueness, but also BPMN [70], which allows the use of a reduced set of model constructs with relaxed semantics when creating models with the involvement of inexperienced modelers [70]. This approach allows models that are syntactically correct and do not contain any semantically incorrect information to be quickly captured. However, it potentially omits information that is considered inconsistent or nonconsensual in the modeling situation.

The approach presented in this article explicitly targets such inconsistencies and focuses on their resolution in the course of modeling. Information is provided by the actors and directly represented by them in the model. They follow a multistep approach through the modeling process, which is described later. Modeling is initially carried out on an individual level to collect

Please cite this article in press as: S. Oppl, Articulation of work process models for organizational alignment and informed information system design, Inf. Manage. (2016), http://dx.doi.org/10.1016/j.im.2016.01.004

S. Oppl / Information & Management xxx (2016) xxx–xxx

individual viewpoints on the work process followed by a collaborative consolidation phase and subsequent elaboration of the resulting model. It can then be interpreted and processed further in IS.

## 2.1. Requirements

Collaborative modeling is the goal-driven joint effort of several people to create a representation of those parts of the real world they consider relevant for the modeling goal (referred to as ‘‘topic of modeling’’ in the following – cf. model theory of Stachowiak [64]). Collaborative modeling is successful if every involved person considers the model to depict appropriately his/her perception of the topic of modeling [38] and considers the model to be useful with regard to the modeling goal [38].

In collaborative modeling, the topic of modeling is a collaborative work process. The aim of this research is to enable the articulation of a collaborative work process by the people operatively involved in it (‘‘actors’’). Consequently, actors are the participants of a collaborative modeling session. Everybody involved in a collaborative work process contributes to the overall aim by performing activities guided by individual mental models of the work process [60]. The mental model of an operatively inexperienced actor is refined only to the extent that it allows the next activities to be chosen based on the perceptions of the work situation [32]. Performing work based on such incomplete mental models might lead to problems in work situations where two or more people need to collaborate and therefore need to have a shared understanding of how to appropriately perform activities as a group. Although mental models are refined over time with increasing experience, unobservable contributions of others cannot be incorporated in one’s mental model. Limiting one’s mental models to individual contribution prevents identification of the potential for improvement, which could be gained by extending collaboration beyond the currently established way of working.

Thus, the goal of a collaborative modeling session aiming at improving a collaborative work process is to facilitate common ground of the work process as a whole and the collaborative aspects in particular. ‘‘Common ground’’ is reached when the actors ‘‘mutually believe that the partners have understood what the contributor meant to a criterion sufficient for current purposes’’ ([5], p. 129). It can be facilitated by providing a communication setting (‘‘medium’’), in which all contributors can articulate how they perceive their work and can negotiate the aspects that are not agreed upon in an argumentative way [54,66]. Such grounding activities are more likely to be necessary in the collaborative aspects of the work process than in those parts that a single contributor performs autonomously [66].

A modeling approach that serves this purpose thus needs to lead to a comprehensive representation of the overall work process. It needs to consider all individual contributions and facilitate identifying and making visible different mental models of how the collaborative aspects are performed [42]. The requirements of articulation support (ARs) of such an approach are derived in the following based on the existing literature.

## 2.1.1. Articulation requirement 1

In order to identify different perceptions of how collaborative work is carried out, the individual mental models of the collaborating contributors need to be made accessible for alignment [9,43]. Externalization of mental models (i.e., creating explicit representations of mental models) is a recognized means to serve this purpose. Conceptual models are a form of representation that has been shown to be suitable for mental model externalization [32]. The act of representation leads to elaboration of the mental model of the externalizing individual, creating a result that serves as an artifact for making the mental model understandable for others [7,53,66]. Consequently, a collaborative modeling approach to work should profit from a phase during which the participants individually externalize their mental model of the work process in the form of a conceptual model (AR 1).

## 2.1.2. Articulation requirement 2

A common vocabulary used by all participants to describe their mental models is a prerequisite for alignment on content level [56,59]. The existence of common ground here cannot be taken for granted, particularly when people with a diverse professional background are involved [59]. The relationship between the vocabulary used to describe concepts in the real-world and the actual real-world phenomena is not unique, because different notions can be used by different people to refer to the same concept [56,69]. Explicitly aligning the notions used to describe the aspects of a work process in a model therefore contributes to creating common ground [13] (AR 2).

## 2.1.3. Articulation requirement 3

Furthermore, the scope of the work process might not be obvious for all participants or even might be perceived differently by the participants [69]. Facilitating a convergence of the understandings of the scope of the work (e.g., what triggers the start of the work process and how its end is recognized) and how the work environment is set up (e.g., identifying the relevant actors, necessary infrastructure, utilized resources, and location of the process and/or its parts) is necessary before externalizing the individual contributions to the work model (AR 3).

The modeling approach to be developed in this study thus should facilitate the following activities: (1) creating individual models of the work process before creating a common model, (2) agreeing on a common description of the work process elements, and (3) creating common ground about the scope of the work process.

## 2.1.4. Articulation requirement 4

The results of these activities provide a foundation for reaching common ground about the work process. This can be facilitated by conceptual models that serve as a shared artifact [13]. Weinberger et al. [69] show that common ground develops through argumentative alignment of individual claims made by the participating actors. A conceptual modeling approach supporting this process should allow for the expression of individual claims and place them in the context of other claims for reviewability in the argumentative chain. This allows conflicting claims to be expressed and monitored, which is important as they need to be resolved to ultimately create a commonly agreed-upon model (AR 4).

Approaches toward collaborative work modeling have already been discussed in the Introduction. Previous research works have identified additional supportive factors that have to be considered when designing a collaborative modeling method to support articulation and alignment. These modeling support factors (MSF) are described as follows:

## 2.1.5. Modeling support factor 1

Majority of the existing research on collaborative modeling targets inexperienced modelers. Requirements originating from this target group are relevant for this research, as operative work staff cannot be expected to have modeling experiences. Research on facilitating lay modeling focuses on measures to guide inexperienced modelers through the process of creating a model without overwhelming them with syntactic formalism and complex modeling constructs. Existing research (e.g., [10,35,39,58]) suggests that starting modeling based on a concrete work case makes it easier for inexperienced modelers to develop an understanding of the necessary concepts to describe a work process in an abstract conceptual model (MSF 1).

## 2.1.6. Modeling support factor 2

The use of a case-based approach for modeling also reduces the number of language elements necessary to depict the work process. For example, case-based models do not require decision constructs or elements for exception handling. While the number of modeling elements alone appears not to have an appreciable impact on the understanding of a modeling language for inexperienced modelers [49], empirical evidence shows that the number of elements actually used during modeling is limited and highly dependent on the modeling objective [73]. When involving inexperienced modelers, it seems to be appropriate to limit the number of available modeling elements a priori to those appropriate for the intended modeling perspective and targeted outcome [3,20] (MSF 2). In this study, the modeling perspective is oriented toward the work of actors and their interactions within an organization. The targeted outcome is reaching common ground on the work process for nonexpert modelers.

## 2.1.7. Modeling support factors 3 and 4

Furthermore, Herrmann and Nolte [23] and Santoro et al. [58] provide evidence that nonformalized information and annotations to model elements can aid the externalization process. However, they do not force the modelers to express all information using the constructs of the modeling language (MSF 3). Some results also indicate the importance of (manual or automatic) facilitation and scaffolding during the model creation process [27] and the model alignment process [53], particularly for inexperienced modelers [8] (MSF 4). Current research indicates that procedural and structural scaffolds provided by a facilitator or automated system may support the elaboration of incomplete models [21,29]. The effectiveness of these approaches, however, still needs to be validated empirically.

## 2.1.8. Summary

The following properties of a modeling approach support collaborative modeling by inexperienced modelers: (1) starting with case-based development of process models, (2) offering a constrained set of modeling constructs with semantics focused on the modeling objective, (3) enabling informal annotations of model elements (i.e., not adhering to formal modeling syntax), and (4) offering procedural and structural scaffolds for model creation and alignment.

Fig. 1 shows ARs and MSFs. Implementing ARs 1 and 2 is at the core of supporting the transition from potentially divergent individual mental models about work to a commonly agreedupon externalized representation of a work process that provides a sound foundation for IS design. ARs 3 and 4 support this transition by clarifying the scope of work and keeping track of the articulation and alignment process, respectively. The implementation of the ARs by means of conceptual modeling is facilitated if MSFs 1–4 are considered during method design. MSFs 1 and 2 are relevant, in particular, for implementing AR 3, whereas MSFs 3 and 4 enable the implementation of AR 4. All four MSFs are finally relevant for ARs 1 and 2 (Section 3).

## 2.2. Modeling language

Models of work processes that should express the collaborative aspects of work need to provide semantic constructs to represent who is involved in the work process, which activities are performed by the involved entities, and what information or artifacts are exchanged by them. These elements describe the coordinative and operative aspects of work, and thus can be considered the minimal set of conceptual elements necessary to describe collaborative work [15]. This assumption has been backed by the development of business process modeling languages over the last few years, where the focus has shifted from functional approaches (e.g., EPCs; [44]) to approaches that structure process descriptions along the involved entities and explicitly allow them to express their interaction (e.g., BPMN [70] or S-BPM [16]).

The aforementioned interaction-oriented modeling languages are designed to describe complex business processes, covering all their variants and potential exceptions. The modeling constructs introduced to handle this complexity, however, are not required for the articulation approach proposed in this article. Starting articulation with a case-based narrative approach (MSF 1) avoids the need for control flow constructs beyond describing sequences of activities and interaction with others. This reduces the number of modeling elements (MSF 2) to make modeling easier for nonexpert modelers. On the basis of empirical data collected on practitioners’ use of BPMN 2.0, zur Muehlen and Recker [73] show that for interaction-oriented modeling for organizational work processes, at most the following constructs are used: Task and sequence flow to indicate what is to be done in which sequence, pools to indicate who is doing what, message flows to couple the process parts in the pools and events indicating the start and end of the process. Abstracting from BPMN, the modeling language proposed in this study consequently consists of the following three modeling elements: WHO element: representing actors, roles, or organizational entities (exact semantics depending on the level of

![](/api/attachments/8AEU7ZHB/fulltext/images/431b4c9481e15e33a7356b544e7a6b2dd3fa19fb64aa9a99d3f9a072e8d4537b.jpg)  
Fig. 1. Articulation requirements and modeling support factors

Please cite this article in press as: S. Oppl, Articulation of work process models for organizational alignment and informed information system design, Inf. Manage. (2016), http://dx.doi.org/10.1016/j.im.2016.01.004

abstraction individually chosen for modeling – cf. MSF 2) (! ‘‘pools’’); WHAT element: representing activities (! ‘‘tasks’’); and EXCHANGE element: describing exchange of information or artifacts among WHO elements (exact semantics depending on designator for element – cf. MSF 3) (! ‘‘message flow’’).

These elements are put into mutual relationship by spatially arranging them as follows: Each WHAT element is assigned to a WHO element by placing it on an imaginative straight line originating from the WHO element (! assignment of ‘‘tasks’’ to ‘‘pools’’). Causality between WHAT elements is expressed by their order on the line starting with the one that is placed nearest to the WHO element (! ‘‘sequence flow,’’ ‘‘start event,’’ ‘‘end event’’). EXCHANGE elements are placed between the lines of the communicating WHO elements and are causally related in the stream of WHAT elements by spatial arrangement, explicitly adding connecting arrows from the activity in which or after which the exchange is triggered and to the activity that receives or is triggered by the exchange (! ‘‘message flow’’).

As shown by the above explanation, the proposed language covers the elements used for interaction-oriented modeling for organizational work processes as identified by zur Muehlen and Recker [73] and can be mapped to formal business process modeling languages such as BPMN. The number of elements has to be reduced and assigned clearly distinguishable semantics to meet the articulation needs of inexperienced modelers [19].

## 3. Articulation support

The proposed modeling procedure comprises three phases to address the aforementioned ARs. These phases involve multiple steps that are shown in Fig. 2. The articulation process starts with a ‘‘setting-the-stage’’ phase, in which a concept map of the work context is created collaboratively. This is to achieve a common understanding of the relevant concepts and the scope of the process. This map serves as a peripheral artifact during the following phases, acting as a point of reference whenever ambiguities arise.

‘‘Articulation and alignment’’ of the work process starts with a set of concurrent individual articulation sessions, in which all participants create models of their work contributions and interactions with others. Individual articulation is followed by collaborative consolidation, in which the individual models are brought together and aligned to form a coherent and agreed-upon model of the overall work process. Both individual articulation and collaborative consolidation are designed to facilitate the creation of case-based models (cf. MSF 1). The ‘‘articulation and alignment’’ phase can optionally be instantiated sequentially for different cases to provide a more comprehensive foundation for the next phase.

The case-based model serves as the foundation for the ‘‘elaboration through virtual enactment’’ phase, during which the model is revisited by going through the articulated process sequentially and altering or extending the model whenever it represents the real work process in an incorrect or incomplete way.

This step can optionally be repeated several times to thoroughly validate the model. Virtual enactment requires IT support. The articulated case-based model thus needs to be transformed in a computer-interpretable model that can be loaded by the business process management system (BPMS) used for virtual enactment. If transformation fails due to missing or ambiguous model information, interactive resolution of these issues is supported. The result of virtual enactment is an elaborated and validated model of the work process, which then can be processed further during IS design. Further validation can be achieved by involving nonoperative stakeholders in the consolidation and elaboration phases. They can contribute their perspectives on the work process and so add aspects that might not have been visible initially to the actors involved in individual articulation.

In the following, the steps of the process are described in more detail, including information on technical tool support for model transformation and elaboration through virtual enactment in the final subsection. A simplified organizational work process of an employee applying for a vacation is used for illustrative purposes consistently across all stages. It is distributed across three organizational roles: employee applying for vacation, secretary processing the application, and manager deciding upon the outcome.

## 3.1. Setting the stage

Not all involved contributors necessarily have a common understanding of the concepts used to describe the different aspects of the collaborative work process (i.e., the WHO, WHAT, and EXCHANGE aspects) and the organizational setting in which the process is embedded [59] (AR 3). In an effort to ‘‘set the stage’’ for creating the collaborative work model, the modeling approach presented in this article incorporates a phase that aims at reaching common ground on the scope of the work process and concepts to be used for describing its relevant aspects.

The modeling method used for setting the stage is based on the research on collaborative concept mapping as a means to create common ground [18,67]. Concept mapping is a method for externalizing and reflecting upon real-world phenomena, which in turn reflects the cognitive structures of the creator [12].

Concept maps allow arbitrary model element types, which prevent misrepresentation or loss of information about individual work perceptions due to a lack of support regarding what people want to express [59]. Creating concept maps without any semantic restrictions supports actors not used to thinking about distinct concepts and helps them to verbalize their work perception. Further, it guides them toward conceptual thinking and sets a common frame of reference for all members of the group. This frame of reference supports a consolidation of the different individual views on collaboration later on.

The actors are asked to describe their work environment by collecting items they consider relevant in the context of their work. Concepts are related by two means: spatial clustering of items and explicit associations by connecting two items and naming the

![](/api/attachments/8AEU7ZHB/fulltext/images/1226a6ebf60eb1611a5059a664247835e3957f0dcfedd8e79f5bc650e47530d9.jpg)  
Fig. 2. Articulation process steps and generated artifacts.

Please cite this article in press as: S. Oppl, Articulation of work process models for organizational alignment and informed information system design, Inf. Manage. (2016), http://dx.doi.org/10.1016/j.im.2016.01.004

S. Oppl / Information & Management xxx (2016) xxx–xxx

connection. The aim of the initial phase is to make explicit the notions participants use to refer to their work and the perceived relationships among the concept considered relevant. This provokes discursive clarification of the scope of the work process and avoids fundamental misunderstandings in the subsequent phases, in which the work process itself is described.

## 3.2. Individual articulation

The modeling approach has to comprise a phase where models of the actors’ own perceived work contributions are articulated individually (AR 1). These models can then be consolidated in a common model in a third phase (AR 2). Individual modeling and the ability to consolidate to a common model are thus inherent properties of the proposed modeling approach. Models are structured along the entities that are involved in collaborative work. Therefore, actors can independently describe (1) WHAT they do to contribute to the work process (their own activities) and (2) with WHOM they EXCHANGE information or artifacts (the actors or organizational entities they are interacting with and how this interaction manifests in information or artifact exchange).

The following spatial layout is used for the different elements to create a consistent form of model representation:

\- WHO items are placed on the upper border of the modeling surface, and they indicate the role represented by the actor and those roles with which the modeler is perceived to interact directly.

\- WHAT items are placed below the WHO item representing the role of the actor, and they describe the actor’s own activities. Their sequence indicates causal and/or temporal relationship.

\- EXCHANGE items are placed below the WHO items of the other roles. They indicate expected exchange of information or artifacts. Their spatial arrangement indicates the causal and/or temporal relationship with the stream of WHAT items:

 EXCHANGE items placed slightly above a WHAT item indicate expected incoming information or artifacts. In case of ambiguity, this relationship can be made explicit by drawing an arrow connecting the EXCHANGE item with the WHAT item requiring this input.

 EXCHANGE items placed slightly below a WHAT item indicate offered outgoing information or artifacts. In case of ambiguity, this relationship can be made explicit by drawing an arrow connecting the WHAT item producing this output with the EXCHANGE item.

Fig. 4 shows the three individually articulated models for the sample process. WHO items are represented in blue, WHAT items red, and EXCHANGE items in yellow. As an example, the model of actor 2 is described in narrative form in the following: the secretary perceives that he has to interact with his colleague and his boss to complete his role in the process. He expects to receive a completed application from the colleague to be able to start his contribution. He checks for conflicts with other submitted or already confirmed applications. The checked application is then forwarded to the boss. The secretary proceeds, as soon as he receives the confirmed application back from the boss. He then files the application and forwards the confirmation to his colleague.

Fig. 3 also shows the semantic differences between the models on the levels of WHO elements (e.g., ‘‘boss’’ vs. ‘‘manager’’) and EXCHANGE elements (e.g., ‘‘form’’ vs. ‘‘completed application’’ or ‘‘decision’’ vs. ‘‘confirmed application’’). These differences reflect different perceptions of the work process. They are addressed in the next phase, where the individual models are consolidated into a commonly agreed-upon model.

## 3.3. Collaborative consolidation

Consolidation has to explicitly make visible and keep track of different perceptions of how to implement the collaborative work process (AR 4). The individual models are thus merged and aligned according to the following scheme for consolidation in the phase of collaborative consolidation:

\- One of the actors starts by placing the WHO items on the upper border of the shared modeling surface. The actor responsible for starting the real-world work process (if known a priori) consequently should start modeling.

\- The same actor continues by describing his/her own contribution to the work process by placing WHAT items below his/her own WHO item. Others do not intervene during this stage.

\- As soon as the actor encounters the first EXCHANGE or shared WHAT item, the targeted communication partner (acting as the source or the sink of the exchange) steps in and starts by matching his/her own perception of the work process with the already externalized model. The following cases can occur:

 A matching EXCHANGE item exists (i.e., an expected exchange that matches an offered exchange, or vice versa). In this case, the matching elements are merged and modeling continues.

 There is no WHO item for the original communication partner available (i.e., the partner has not perceived any collaboration with the original actor at all). In this case, a fundamental

![](/api/attachments/8AEU7ZHB/fulltext/images/fb12013816c43d695a3a26fa8237f80fbb0c95eed636be0c2af5aea4f22f0abf.jpg)  
Fig. 3. Sample result of individual articulation.

Please cite this article in press as: S. Oppl, Articulation of work process models for organizational alignment and informed information system design, Inf. Manage. (2016), http://dx.doi.org/10.1016/j.im.2016.01.004

difference in work perception has been identified, which needs to be resolved by the participants.

 There is no matching EXCHANGE item available (i.e., the perception of collaboration was not shared or considered relevant). In this case, a difference in work perception has been identified, which needs to be resolved by the participants.

 A matching EXCHANGE items exists, but is perceived to represent content or nature that is different from the exchanged information or artifact (i.e., share the perception of the need for collaboration, but do not share common ground on how it is implemented, or alternatively choose different levels of granularity to describe exchanges). In this case, a difference in collaboration perception has been identified, which needs to be resolved by the participants.

\- If a match has been identified or different understandings have been resolved to ultimately form a match, the modeler responsible for the targeted entity continues to complete the model with the elements describing how he/she contributed to the work process until the agreed-upon point of collaboration (i.e., the EXCHANGE element). This includes adding his/her own WHO elements.

\- Consolidation continues in this way until all points of collaboration are agreed upon. If one actor has completed his/ her contribution, others with remaining elements not yet incorporated in the common model take over and provide further input to the consolidation process. If missing elements are discovered by an actor during consolidation, they are added by the responsible actor immediately, even if they had not been created during individual articulation.

\- Any elements created during individual articulation which are not part of the collaborative model after the former steps (e.g., because at this point they are considered irrelevant by the contributing actor) need to be revisited explicitly and discussed in the group regarding their potential to be integrated in the model.

Fig. 4 shows the consolidated model for the sample process. The matching WHO and EXCHANGE items are placed on top of each other. The final model depicts the vacation application process in case of no conflicts identified by the secretary and a confirmation by the manager. The semantic differences existing in the individual models have been resolved in the agreed-upon model. The resolution is an integral part of the consolidation process carried out in this phase.

The whole process of consolidation aims at facilitating the creation of common ground on the collaborative work process. The matching of WHO and EXCHANGE elements, where mismatches in the individual models are explicitly made visible, triggers explicit alignment activities (AR 4). The involved people need to refine or alter their mental models to converge to an extent that allows reaching common ground on how to collaborate [56].

Building upon Clark and Brennan’s [5] notions of ‘‘common ground’’ and ‘‘consensus,’’ Weinberger et al. [69] describe which behavior to expect from people involved in these processes and list the following resolution strategies to deal with views that do not match.

Quick consensus building occurs when participants accept the contributions of others not because they are convinced, but to be able to continue discussion. This is a nondesirable behavior in the aforementioned cases that requires explicit resolution. It is, however, acceptable when models created on different levels of granularity are matched (i.e., one model being more detailed than the other while not representing different perceptions of the actual work process) or only different naming has been used to describe the same concept (e.g., for WHO elements ‘‘boss’’ and ‘‘manager’’ in the sample process depicted in Fig. 3).

Integration-oriented consensus building is characterized by an adoption of the perspectives of other participants. Individuals may give up or modify their viewpoints and eventually their models based on others’ contributions. This behavior is to be expected in case of necessary clarification of the specific form or content of EXCHANGE items. In the sample process, ‘‘form’’ (offered by actor 1) and ‘‘completed application’’ (expected by actor 2) of the EXCHANGE items represent such a case, where actor 2 has more specific expectations on the exchanged information than actor 1, while their fundamental intentions do not differ.

Conflict-oriented consensus building requires participants to face critique of their own models and views. They need to assess

![](/api/attachments/8AEU7ZHB/fulltext/images/0844d7297ee3064b0ade1ea692e509f9d793a053eff5a7a6ac43c21bae7ffb35.jpg)  
Fig. 4. Result of collaborative consolidation.

Please cite this article in press as: S. Oppl, Articulation of work process models for organizational alignment and informed information system design, Inf. Manage. (2016), http://dx.doi.org/10.1016/j.im.2016.01.004

S. Oppl / Information & Management xxx (2016) xxx–xxx

multiple perspectives to find better arguments for their positions. Creating consensus in a conflict-oriented manner requires participants to identify the specific conflicting aspects of the others’ contributions. This might also be a desirable behavior, as an understanding of other people’s viewpoints is required to present acceptable alternatives. The models in this case act as externalized artifacts of those viewpoints, which ease the process of understanding and facilitate the making of proposals [30]. In the sample case, this could be triggered by the EXCHANGE items ‘‘decision’’ offered by actor 3 and the ‘‘confirmed application’’ expected by actor 2. Those items are of fundamentally different nature, as ‘‘decision’’ implies an open-ended outcome, while ‘‘confirmed application’’ indicates an expected positive decision. In the process leading to the model in Fig. 4, the conflict could have been resolved if actor 3 agreed to remain with the case of a positive decision for the initial agreedupon model and come back to the other variants in the next phase, where the process is elaborated through virtual enactment.

The model evolution supports reaching common ground as the current state of the model continuously serves as a shared artifact for reviewability and clarification purposes [14,67]. The immediate visibility of fundamentally different viewpoints in the model should prevent a quick consensus building where necessary, and it requires actors to use more elaborate strategies such as integration- or conflict-oriented consensus building. After reaching common ground and reflecting upon changes in the model, it represents an agreed-upon representation of the respective parts of the collaborative work.

## 3.4. Elaboration through virtual enactment

Completing the modeling phases described so far leads to models that are semantically incomplete representations of a work process. It is important to note that these models do not account for different variants of a work process that are represented using decision elements in other business process modeling languages (e.g., in the sample process, negative outcomes are not yet represented). This study deliberately follows a case-based approach to reduce model complexity for the targeted inexperienced modelers (cf. MSF 1). A comprehensive model of the business process, however, is still required for further processing during IS design. For this reason, the case-based models are elaborated interactively using process enactment tools, which play through the work process step by step and alter and extend the model whenever the enactment is incorrect or incomplete with regard to the perceived real-world work process. It should be stressed at this point that participants during the virtual enactment do not perform modeling. At this stage, they interact with a BPMS implemented for this purpose within our research [37]. This BPMS presents Web-based dialog forms to the participants, allowing them to describe the deviations from the currently enacted process. The BPMS supports the description of the new or altered process steps by providing the current process context (i.e., what was done before the deviation was started), as well as information about potential interaction partners.

Completing collaborative alignment leads to models that are transformable to models created with role-centric, communication-oriented business process modeling languages such as S-BPM [16] or BPMN [70]. Mapping from the case-based model to the target business process model fully represents the structure of the former in the target model. By applying a set of transformation rules, a source model adhering to the aforementioned layout rules can be mapped to a syntactically correct target business process model. Syntactic correctness enables further processing of the model and uses it for execution in a BPMS as described above. Elaboration during execution requires altering the model while an instance of it is currently being executed. This is not a common feature of BPMS. For this study, a system processing S-BPM models has been extended to provide this functionality within our research [37], which is described in more detail in Section 3.6. While not being a part of the methodology, S-BPM offers close conceptual similarity to the modeling language introduced for the first part of the methodology. A subset of BPMN, being the source for language design in Section 2.2, conceptually would also be a valid choice, but has not yet been examined more closely in this study because of limited engineering resources. The following descriptions focus on S-BPM, but are equally applicable to BPMS based on other languages.

## 3.4.1. Transformation

S-BPM models consist of behavioral models, which describe the activities (‘‘action states’’) and communication acts (‘‘send state’’ and ‘‘receive state’’) of each step involved in a process. These behavioral models are encapsulated in ‘‘subjects,’’ with each representing one process role and used in an interaction model, which provides a bird’s-eye view on the communication occurring among subjects in the process. The WHO items of the source model are mapped to ‘‘subjects,’’ the WHAT items are mapped to ‘‘action states,’’ and the EXCHANGE elements are transformed to the corresponding ‘‘send state’’ and ‘‘receive state.’’ The detailed transformation and mapping process is beyond the scope of this study; however, it has been described in detail in Oppl [45], in which, the method used to resolve issues arising from incomplete source models or ambiguous source model layouts has also been addressed.

Fig. 5 (left-hand side) shows the result of the transformation process for the sample model, depicting the interaction model and the behavioral diagrams of the subjects. The interaction model shows the subjects and messages exchanged between them, which can be directly derived from the spatial arrangement of the WHO and EXCHANGE items in the consolidated model. The behavior diagrams show the activities and communication acts of the involved subjects. They are derived from the spatial arrangement of the WHAT items assigned to the WHO element representing the subjects and the incoming and outgoing EXCHANGE items. Each outgoing and incoming EXCHANGE items are mapped to send state and receive state, respectively.

## 3.4.2. Virtual enactment

Models without syntactic errors can be directly used for virtual enactment in the BPMS. For this purpose, a process derived from the original model is started. As mentioned earlier, this model initially reflects only one variant of the process, omitting more sophisticated control flow constructs such as decisions or loops. The aim of elaboration through virtual enactment is creating a semantically correct representation of the work process in all its variations as perceived by the involved actors.

The actors enact the process step by step. For each step, the responsible actor assesses whether the step is correct and described in sufficient detail and whether the next step is the only possible way to progress or if there are alternative ways of continuing with the work process. This can refer to alternative options of progressing, optional activities, or activities that have been omitted in the original model. The model is altered if any of these assessments lead to the need for changes in the process. The BPMS directly accesses the modified model representations and continues with the execution (cf. Section 3.6 for a more detailed description of tool support in these steps).

## 3.4.3. Refinement

Changes can have different effects that might trigger the need for further changes in the overall process. Increasing potential changes with respect to their impact on the overall process are

S. Oppl / Information & Management xxx (2016) xxx–xxx

![](/api/attachments/8AEU7ZHB/fulltext/images/6498e6cf3e522dd506dde935dfd8f64b12160cdc42b6e1122d2f4ab23fe0fa80.jpg)  
Fig. 5. Results of model transformation (left) and elaboration through virtual enactment (right).

described in the following. The nomenclature of the modeling language described in Section 2.2 is used for consistency: (1) adding, altering, or removing WHAT items to a WHO item, (2) shifting responsibilities for WHAT items between WHO items, (3) altering the sequence of EXCHANGE items between WHO items, (4) adding or removing EXCHANGE items required from or provided to other WHO items, and (5) involving a new WHO item in the process.

Case 1 refers to situations where only the behavior of a WHO item is altered without affecting its interfaces to other WHO items. Content, form, and sequence of EXCHANGE items remains unchanged. In this case, the changes only affect one WHO item and do not require further changes. Case 2 refers to situations where the content, form, and sequence of EXCHANGE items remain unchanged, but responsibilities are shifted from one WHO item to another. In this case, the affected WHAT items must be incorporated in the behavior of the target WHO item. Case 3 refers to situations where the sequence of EXCHANGE items is altered, but both content and form remain unchanged. In this case, the WHO item collaborating in the communication needs to adapt its behavior to fit the new expectations. This might trigger subsequent changes for this WHO item, which again potentially causes cascaded changes elsewhere in the process. Case 4 refers to situations where the EXCHANGE items are fundamentally altered in a way that adds or removes communication acts to or from the behavior of the involved WHO items. This necessarily causes changes in the targeted WHO item, as it needs to react to new information or provide information that was not expected before the change. This again potentially causes cascaded changes elsewhere in the process. Case 5 finally refers to situations where a new WHO item is added to the process. This requires specifying the communication interface (i.e., the EXCHANGE items) with this new WHO item as well as its WHAT items, if they are known and relevant to the work process. Adding a new WHO item might have implications on the behavior of the other involved WHO items, as additional EXCHANGE items might be required.

If a change to the model triggers the need for further changes (i.e., in cases 2–5), those cascaded changes do not necessarily need to be made immediately. The elaboration of the overall process, however, can only be finished if all open change requests have been resolved.

Fig. 5 (right-hand side) shows an elaboration in the secretary’s behavior, which reflects the potentially negative outcome of the decision of the manager. The shown elaboration has been triggered by a change in the manager’s behavior, altering the message from ‘‘confirmed application’’ to ‘‘decision’’ (case 4). The change in the secretary’s behavior is important to assess the decision during filing and accordingly to communicate the different outcomes to the employee (case 4). Consequently, the employee also would have to adapt his/her behavior to reflect the altered incoming messages.

Elaboration through virtual enactment is a means to generate a process description without the need to manually create comprehensive formal process models by traditional conceptual modeling. Separation of models and model changes together with the different involved subjects reduces complexity and allows a focus on one subject’s behavior at a time. The use of the execution engine allows modeling of complex decision processes by incrementally adding process variants to the model as the enactment continues. Complex models of collaborative work processes are developed in this way without the need to ever translate one’s perceptions of a work process to abstract process descriptions.

It is important to note that the resulting model is not necessarily complete or valid in terms of representing organizational reality. The completeness and objective validity of the resulting model are constrained by the limited views of the involved actors on the overall organization. Nonoperatively involved internal or external stakeholders – because of their position – might be able to articulate further relevant aspects about the work process. Involving them in the consolidation and elaboration process or having them validate the results of either phase can address this issue, if a more comprehensive process representation is required from an organizational perspective.

## 3.5. Summary of methodology and comparison to related work

Table 1 summarizes the steps involved in articulation and alignment. They are described regarding the actor involvement, generated artifacts, and addressed ARs and MSFs.

The identified ARs and MSFs provide the necessary framework to compare the presented approach with related work. Reviewing the existing literature for approaches that propose a methodology, which uses conceptual modeling for collaborative articulation of work to produce models that serve the purpose of designing IS and that are empirically validated, suggests the following approaches for further analysis: socio-technical walkthrough (STWT) [25], collaborative modeling architecture (COMA) [55], and Plural [66]. These approaches are discussed with respect to the ARs and MSFs.

## 3.5.1. Socio-technical walkthrough

STWT workshops [25] target domain experts who do not necessarily need to have modeling experience. The STWT uses SeeMe [23] as a modeling language, which comprises three coremodeling elements with context-sensitive semantics (!MSF2+), and is designed to represent models of socio-technical systems. It represents vague information, which explicitly captures disputed or unclear parts of a work process (!AR4+). Informal annotations can be added to the model (!MSF3+), and the resulting models are intended for use in IS design, but are not executable in BPMS. The STWT does not explicitly collect individual work contributions in models, but strives to consolidate divergent views through moderation techniques directly in the workshop setting (!AR2+). No explicit scaffolds for model creation or alignment, however, are embedded in the methodology or the modeling language. Reaching a common understanding about the scope of work and the work environment is an integral part of the methodology (!AR3+). The STWT is usually implemented as a series of workshops, allowing iterative elaboration of the model, but does not explicitly focus on case-based modeling (!MSF1?).

## 3.5.2. Collaborative modeling architecture

COMA [55] focuses on providing support for articulating (!AR1+) and consolidating (!AR2+) models during collaborative modeling with a language-agnostic negotiation approach. The COMA tool provides support for unified modeling language (UMA) and enables actors to communicate via the software in a structured way specified by the COMA methodology. Support of informal annotations is not mentioned (!MSF3?). Following its negotiation-oriented approach, COMA does not make any explicit claim on whether clarifying the scope of the process is suggested as a dedicated activity (!AR3?) or whether model creation should start following a case-based approach (!MSF1?). COMA does not explicitly address inexperienced modelers. It provides scaffolds for model consolidation (i.e., the negotiation process) (!MSF4+). These scaffolds make explicit divergent views and suggestions for a common view, which is ultimately agreed upon with the support of a human facilitator (!AR4+).

## 3.5.3. Plural

Plural [66] is a method based on a multiperspective modeling paradigm [42], which focuses on representation of individual work contributions in models (!AR1+) and subsequently merges them into a common model by agreeing upon the interfaces among the individual models (!AR2+). It uses enhanced EPC (eEPC) [44] as a modeling language and assumes that actors are familiar with this language. Plural uses tool support built upon a commercial modeling environment, which identifies inconsistencies between individual models (!AR4+). Clarifying the scope of the work process is not explicitly mentioned to be a part of the method (!AR3?). Informal annotations are supported as far as eEPCs can comprise them; they are not mentioned as a part of the method (!MSF3?). The same holds true when following a case-based modeling approach (!MSF1?). Tu¨ retken and Demiro¨rs [66] mention tool support for resolution of inconsistencies between models, but do not elaborate further on how scaffolding is implemented (!MSF4?).

## 3.5.4. Summary

Existing approaches to supporting collaborative articulation and modeling either target inexperienced modelers (such as the STWT + SeeMe) or aim at producing a formally correct model that can be directly processed in IS (such as COMA or Plural). This is a reasonable approach given the conflicting requirements in those areas [72]. From an IS design perspective, however, it remains desirable to satisfy requirements in both areas with a single methodological approach [33]. Reviewing the results presented in Table 2, it seems possible to adapt the existing approaches to reach similar objectives as the proposed approach in its different phases. This article still extends beyond the state of the art by proposing a

Table 1  
Summary of methodology.

<table><tr><td>Phase</td><td>Interactive step</td><td>Actor involvement</td><td>Generated artifacts</td><td>Addressed AR and MSF</td></tr><tr><td>1</td><td>Setting the stage</td><td>Collaborative</td><td>Concept map of work context</td><td>AR: 3MSF: 2, 3</td></tr><tr><td rowspan="2">2</td><td>Individual articulation</td><td>n individuals</td><td>n individual models of perceived contribution to work</td><td>AR: 1MSF: 1, 2, 4</td></tr><tr><td>Collaborative consolidation</td><td>Collaborative</td><td>Agreed-upon model of overall work process, case-based</td><td>AR: 2, 4MSF: 1, 2, 3,4</td></tr><tr><td>3</td><td>Elaboration through virtual enactment</td><td>Collaborative</td><td>Elaborated, executable model of work process</td><td>AR: 1, 2MSF: 3, 4</td></tr></table>

Please cite this article in press as: S. Oppl, Articulation of work process models for organizational alignment and informed information system design, Inf. Manage. (2016), http://dx.doi.org/10.1016/j.im.2016.01.004

Comparison with related work (‘‘+’’ indicates fulfilled criteria, ‘‘?’’ indicates ambivalence of the approach to the respective criterion, and empty cells indicate not explicitly supported criteria.

<table><tr><td></td><td>Targeted actors</td><td>Resulting model</td><td>AR 1</td><td>AR 2</td><td>AR 3</td><td>AR 4</td><td>MSF 1</td><td>MSF 2</td><td>MSF 3</td><td>MSF 4</td></tr><tr><td>STWT+SeeMe</td><td>Domain experts</td><td>SeeMe, not executable</td><td></td><td>+</td><td>+</td><td>+</td><td>?</td><td>+</td><td>+</td><td></td></tr><tr><td>COMA+Tool</td><td>Need to know UML</td><td>UML, executable</td><td>+</td><td>+</td><td>?</td><td>+</td><td>?</td><td></td><td>?</td><td>+</td></tr><tr><td>Plural</td><td>Need to know EPCs</td><td>EPC, executable</td><td>+</td><td>+</td><td>?</td><td>+</td><td>?</td><td></td><td>?</td><td>?</td></tr></table>

methodology that combines two modeling languages to transition from articulation-oriented modeling toward elaboration of formal models. In order to enable this transition, the formal modeling language used for the latter phase is syntactically and semantically compatible to the representation used for articulation and alignment support in the first phase. The necessary transition between representations affects the design of the support tools, which are described in the following.

## 3.6. Tool support

The above-described modeling procedure requires technical support to enable transition between the articulation and elaboration phases. The tools designed to provide this support are described in the following. Phases 1 and 2 are methodologically based on collaborative conceptual modeling. Carrying out such collaborative conceptual modeling activities does not necessarily require support by IT-enabled tools and can benefit from tangible representation of the modeling elements [7,40]. Phase 3, however, relies on IT to support elaboration through virtual enactment. Thus, a tool prototype has been designed that allows for tangible modeling of the work process and context in phases 1 and 2. It allows (semi-)automatic transformation to a digital model representation that can be processed further in phase 3.

## 3.6.1. (Semi-)automatic model transformation

Modeling of phases 1 and 2 is carried out using physical cards (cf. Fig. 6), which are used to create models according to the structuring guidelines described in Sections 3.2 and 3.3. After completing phase 2, the resulting card-based model should represent an agreed-upon perception of the collaborative work process. The card-based models need to be converted into digital model representations for further processing in phase 3. Manual transformation is time-consuming and error-prone. An IT-supported tool has thus been developed to transform the card-based model to a digital model representation, which can directly be processed in a BPMS. The operative design goal for this tool is to avoid the need to split an articulation workshop into two parts because of the need for manual model transformation.

The bridge between the card-based model and the digital model is designed to work as transparently for the user as possible. User interaction should only be necessary if syntactical model information derived from the card-based model is ambivalent or incomplete and requires elaboration. The card-based model is initially captured as a pixel-based image in the first step via taking a picture, for example, with a mobile phone. The modeling cards hold visual markers that can be recognized and uniquely identified in the picture (cf. Fig. 6, Source image).

The optical marker recognition engine is based on the reacTIVision system [36], and identifies the coordinates of each marker. On the basis of this information, the cards contained in the image can be identified and extracted (cf. Fig. 6, yellow bounding boxes in the second image). The extracted information is also used for identification of potential connections that are drawn between cards (cf. Fig. 6, red arrows in the second image). The model layout is analyzed in the next step regarding its adherence to the model layout rules described in Section 3.3. Those parts of the model that adhere to these rules can be transformed to S-BPM automatically and are stored as an XML-representation (cf. Fig. 6, S-BPM model). If modeling rules are violated, missing, or ambiguous, then the information needed for the transformation can be added interactively (cf. Fig. 6, third image). IT-based guidance through the interactive parts of the transformation process is currently implemented prototypically and described by Oppl [45]. Once the transformation process is complete, the resulting model can be used for elaboration through virtual enactment.

## 3.6.2. Elaboration through virtual enactment

Elaboration through virtual enactment is performed using a BPMS that allows process descriptions to be altered during runtime. It is a means to generate a process description without the need to manually create comprehensive formal process models. Using the BPMS described in Kannengiesser et al. [37], playing through complex decision processes is enabled by incrementally adding process variants to the model as virtual enactment continues. In order to avoid losing the context of the enacted work process (i.e., losing all entered data or information about earlier decisions), these model changes must not require a restart of the virtual enactment. The need to restart workflow execution in the case of model changes is a technical constraint of most currently available BPMS [37]. The BPMS has been functionally extended as a prerequisite for the present research and supports deviations from a currently executed process model during runtime [37].

![](/api/attachments/8AEU7ZHB/fulltext/images/8344f3f429cfd5642a552e093458964a5f3c093455e7dd61dd804a1f49a20b41.jpg)  
Fig. 6. Transformation from card-based model to formal S-BPM model. (For interpretation of the references to colour in the citation of this figure, the reader is referred to the web version of this article.)

Please cite this article in press as: S. Oppl, Articulation of work process models for organizational alignment and informed information system design, Inf. Manage. (2016), http://dx.doi.org/10.1016/j.im.2016.01.004

S. Oppl / Information & Management xxx (2016) xxx–xxx

Elaboration of process models is carried out in plenary sessions, where all involved actors play through the model collaboratively, guided by the BPMS, and make appropriate changes to the process. Changing the model of the process is not a trivial task for nonexpert modelers in this phase, as a formal business process specification language is used in this study. The tool allows for extending process descriptions via dialog forms and without directly manipulating the model. While this enables elaboration through virtual enactment, it does not provide sufficient support in terms of MSF4 and is currently being extended toward interactive prompting to elicit the missing model information during execution as proposed by Herrmann and Loser [21]. In the current prototypical implementation of the tool, a facilitator carries out prompting and model modifications. While this poses a limitation to this study, the overall methodology – being the core design artifact presented in this study – is not affected, as the facilitator does not intervene content-wise, but only acts as an interface to the modeling environment. The prompting interventions of the facilitator, however, need to be examined more closely in future research to enable an appropriate design of scaffolds (cf. MSF4).

## 4. Organizational alignment – a case study

Section 3 introduced a methodology to support the process of collaboratively articulating knowledge about work in organizations as a design artifact. The evaluation of this artifact with respect to the requirements identified in Section 2 is described in this section. The primary aim is to contribute to articulating different views on a work process and facilitate the alignment of different views. This implies the existence of a shared work context in which different views in collaborative work can emerge. This shared work context, however, cannot be controlled or artificially created, as would be necessary for an experimental evaluation setup. Case study research [71] thus remains as a suitable validation strategy. The research questions to be addressed here are twofold. Regarding articulation, evaluation needs to address how the identified ARs and MSFs are met by the methodology. Regarding the articulation results, evaluation needs to address whether the resulting models are syntactically valid and semantically sound. Underlying these research questions and concretizing them are the following two propositions: (1) the proposed methodology as a whole (i.e., comprising all its phases) enables domain experts without modeling experiences (‘‘actors’’) to articulate and align their views on a collaborative work process and create a common artifact representing this aligned view; and (2) this common artifact is a model of the work process as perceived by the actors, where the model is considered to be complete when all actors involved in the model creation process consider their views to be fully represented by the model. This model can be interpreted by and processed in an IS without further transformation.

## 4.1. Case study design

The unit of analysis for proposition 1 is a group of actors working together in the course of one modeling workshop. For proposition 2, the modeling result needs to be assessed. Consequently, the data collection methodology for proposition 1 needs to generate data about the acts of articulation and alignment happening during the application of the methodology, also capturing which behavior can be observed during the different methodological phases. Data interpretation needs to identify whether the phases meet their design criteria as described in Table 1. Data collection for proposition 2 needs to document those modeling results generated during the application of the methodology, which represent common artifacts that serve as the foundation for further processing: the model generated as an outcome of collaborative consolidation (acting as the baseline for elaboration), the result of the transformation process to an executable modeling language (as the first IT-interpretable model), and the model generated by elaboration through virtual enactment (as the final result). Data interpretation needs to assess the syntactic correctness of these models with respect to the use of modeling language and their usefulness for the indented articulation objective.

Following this research design, the case study has been designed to test the propositions. The ARs and MSFs are the fundamental criteria for designing the methodology. Consequently, the properties of the methodology meeting these criteria should be observable in any of its applications. This objective justifies a revelatory single case design [71], where a case needs to be selected in which the data collection requirements can be satisfied. In particular, this means that the outcome of the methodology needs to be applied in a practical work context (cf. data collection requirement for proposition 2: generate data on the usefulness for the intended articulation objective). Data to assess proposition 1 also can only be generated in situ during a real-world application of the methodology. Thus, data for the presented case were collected following a participant observation approach [34]. In the following, the case setting is described after a summary of the observations is provided with respect to research questions 1 and 2. Section 4.3 discusses the findings of the research proposition formulated above.

## 4.2. Case description

The case is situated in the administration department of a university, and addresses the procedures necessary to come to a funding decision for research materials or infrastructure. Research departments can apply to receive additional funding from the global university budget, if they are not able to cover the costs of materials or infrastructure for conducting their research.

The process of assessment and decision making for such applications historically was never formally established. This led to a lack of transparency in the decision process regarding both the decision criteria and status of an application at a given point in time. In this case study, when a new CFO took office, he/she set out to establish this process. The aim of this initiative was to make the progress and outcome of applications transparent to the applicants, and ultimately to have the whole process supported by the already existing workflow management system of the university. This methodology was used in a series of workshops to achieve these goals.

Following the procedural model described in Section 3, the methodology initially was applied to reach common ground across all involved organizational entities of the not yet formally established process. The methodology was used to elaborate the model of the application process so that it provided a foundation for setting up process guidelines, forms, and workflow support. Four people from the university administration and one person representing the research departments were involved throughout the whole process. Modeling consisted of setting the stage, individual articulation, and collaborative consolidation in the initial workshop and elaboration by virtual enactment in a second workshop. A facilitator guided the whole process methodological ly, but did not carry out content-wise intervention.

Representatives of the following organizational roles were involved throughout the whole articulation and elaboration process (names given in brackets are used as abbreviations when referring to them below). The list of activities refer to the anticipated tasks during the application process that led to the invitation of the respective person to participate in the workshops: technician of a research department (technician): filing application for funding and providing additional information as needed;

representative of university IT department (IT dept.): providing domain expertise for decisions about IT-oriented applications; CFO of university (CFO): making final funding decisions and acting as the link to the executive board of the university for decisions on applications exceeding a given financial threshold; head of controlling (controller): preparing funding decisions for the CFO, assessing financial feasibility, and communicating with the applicant; head of financial administration (head of finance): managing the ordering and inventory of material or infrastructure from approved applications.

Of these five actors, only the representative of the IT department had prior knowledge of business process modeling. The other actors only had operative experiences with the university workflow management system, without being explicitly confronted with the underlying process models. The group consisted of four female actors and one male actor aged between 32 and 45 years. The following subsection reports on the observations made during the implementation of the methodology.

## 4.3. Documentation of articulation process and outcomes

## 4.3.1. Setting the stage

The actors started with the ‘‘setting-the-stage’’ phase. The facilitator gave them the task to identify ‘‘everything that they considered relevant for the funding application process,’’ without imposing any further restrictions. The actors identified 14 concepts that were considered important in the context of the work process. After clustering these concepts, three main classes of concepts were identified. One cluster comprised the involved organizational roles, the second cluster covered the relevant information and documents that were required, and in the third cluster, the actors identified the major global steps that were necessary to complete the work process. As the actors were selected based on their anticipated involvement in the process, no major conflicting views were uncovered. Some wording issues were resolved, mainly between the members of the administrative departments and the technician, as different notions used by administrative staff to refer to information required during the application assessment were initially unclear to the technician. ‘‘Setting the stage’’ was also used to clarify the scope of the process. There were different viewpoints on whether the activities that happen in administration after a positive funding decision should still be included in the work process. As the technician and the representative of the IT department already identified potentially redundant activities occurring in this later phase, the actors decided to include it in the articulation activities. The created model was filed electronically and printed for each actor to be used as a reference for consistent wording during individual articulation.

## 4.3.2. Individual articulation

The steps of the ‘‘articulation and alignment’’ phase were also performed using the card-based tool. In the initial step, all actors were asked to describe their activities within the process from their viewpoint following the approach described in Section 3.2. This phase required clarification on the meaning and use of EXCHANGE elements for two actors. Referring the cluster including the relevant information items from the first modeling phase as an example for potential EXCHANGE elements helped to resolve these issues. The step of ‘‘individual articulation’’ was completed in approximately 15 min without any further issues.

## 4.3.3. Collaborative consolidation

Collaborative model consolidation was performed using the cards created during individual articulation. The result of this part of the workshop is depicted in Fig. 7, which shows the original model and a transcribed, anonymized version used for description (coding scheme for numbers used in transcribed version: x denotes WHO elements; x.y denotes WHAT elements, where x is the responsible WHO element; and x1–x2.z denotes EXCHANGE elements, where x1 is the sending and x2 is the receiving WHO element). Numbers in brackets refer to Fig. 7 following the described coding scheme.

The technician (1) started with adding his elements, as he also triggered the process in reality by preparing the funding application at the research department (1.1). The controller (2) was involved as the second actor when the technician modeled the interaction of submitting the funding application form (1–2.1). The subsequent activities required further discussion, as the controller potentially needs to collect further information from the technician. This was not included in the latter’s individually articulated model. After resolving these issues, the CFO (3) became involved. When the controller passed on the prepared documents for the funding decision (2–3.1), the CFO immediately involved the IT department requesting a comment on the funding application to make a decision. At this point, the first major change for the process was proposed. The controller recognized that he/she could request the IT department’s comment in the preparation phase, making the actual decision process more efficient. All affected actors accepted this change, and the model was adapted accordingly (2–5.1 and 5–2.1).

From this point on, modeling continued without any major changes to the process as the actors originally envisioned it during individual articulation. One major change to the content of the application form was proposed when discussing the activities to be performed after a positive funding decision. As already anticipated during the setting-the-stage phase, the representative of the IT department (responsible for placing an order to external suppliers) and the technician (responsible for collecting initial quotes) discovered that both of them requested offers from potential suppliers. In order to avoid inefficiencies and double quotes, they agreed that the initial offers collected by the technician should be included with the application, so that this information could be passed on in the case of a positive funding decision. The controller, being responsible for handling those applications, agreed to this change on the condition that the processing of applications in the future was supported electronically. The representative of the IT department, responsible for the workflow management system, agreed to implement this functionality in the operative system. This change did not immediately affect the process model, as the steps remained unchanged. Still, the information to change both the content and representation of the application form was documented as an annotation to the respective EXCHANGE element. The first workshop ended with an initial version of the work process to which all participants could agree.

## 4.3.4. Model transformation

For the second workshop, the model was transformed to an S-BPM process model (cf. Fig. 9) using the transformation tool described in Section 3.4.1. Missing information and ambiguities (e.g., EXCHANGE items 7–1.1 and 5–1.2 lack a target WHAT item in the lane of WHO item 1) were identified and resolved during transformation. The facilitator guided this step, as interactive guidance was technically in an embryonic stage and thus could not be operatively deployed. The result was deployed to the BPMS used for the ‘‘elaboration through virtual enactment’’ phase. The same actors as in the first workshop gathered in a colocated setting with the facilitator and an additional modeler responsible for making changes to the model as required during enactment. The latter was necessary due to the limitations of the current tool prototype used for virtual enactment (cf. Section 3.6) and consequently was instructed not to intervene regarding the content.

![](/api/attachments/8AEU7ZHB/fulltext/images/074ec1cb18d188799e81e98556d5910ef157aa7979695b13e4518a377705d378.jpg)  
Fig. 7. Card-based model resulting from collaborative consolidation.

## 4.3.5. Elaboration through virtual enactment

Enacting the process contributions of the technician and the controller did not reveal any need for changes or extensions. Major changes to the process, however, were required for the CFO’s part, reflected in Fig. 8 and described in the following (numbers in brackets refer to elements shown in Fig. 8). The CFO wanted to reflect the criteria for funding decisions in the process model, and he/she consequently extended the model with a decision element (3.n1) that reflected the different options of coming to a decision for a funding application. These changes to the process model were included immediately during execution and were validated in the same step by executing them iteratively. These changes to the behavior of the CFO triggered cascaded changes as described in Section 3.4.2. An example of such cascaded changes is the addition of the executive board of the university as an additional instance for decision making if the funding application exceeds a certain amount of money (cf. case 5 in Section 3.4.2). In the subject interaction diagram, the existing subject 4 in phase 2 originally referred to the university chief operating officer (COO), who had to be informed in certain cases. However, this was changed to represent the executive board (4c). The behavior of the CFO affects communication with the executive board (cf. case 4 in Section 3.4.2, reflected in 3–4.1 and 4–3.n in Fig. 8). In addition, the behavior of the controller requires changes, as decisions need to be made differently in such cases (cf. case 3 in Section 3.4.2, reflected by the altered incoming communication 2–3.1c in Fig. 9). In addition, the communication with the IT dept. (5) was changed back to be carried out by the CFO (3), as the latter argued that making informed decisions was easier for him/her if he/she could interact with the domain experts directly (reflected in 3–5.1 and 3–5.2, which substitute 2–5.1 and 2–5.2 from the result of phase 2). In addition, the CFO insisted that he/she should be the one to inform the technician (1) about decisions made by the executive board (reflected in 3–1.n in Fig. 8). The remaining process was again enacted without any major changes, and is not described in more detail in this study.

After ‘‘elaboration through virtual enactment’’ was completed, the process was transferred to an operative instance of the BPMS. The participants were granted access to this platform to experimentally implement the new process in real-world cases. After a testing phase of 3 months, a brief reflection meeting was held to allow for mutual feedback and collect ideas for further improvements to the process. In this step, only minor modifications to the sequences of activities of the controller were made, and thus the remainder of the process was not altered. The process was then exported in its final version and provided to the IT department for implementation in the university’s global workflow management system.

## 4.4. Discussion

The case study so far described has made visible different aspects of the proposed methodology and tools that are discussed in this study with respect to its original aim.

The primary goal of this research is to facilitate the development of common ground on a work process across all involved

Please cite this article in press as: S. Oppl, Articulation of work process models for organizational alignment and informed information system design, Inf. Manage. (2016), http://dx.doi.org/10.1016/j.im.2016.01.004

S. Oppl / Information & Management xxx (2016) xxx–xxx

![](/api/attachments/8AEU7ZHB/fulltext/images/8233b34ddec3d2a47ef231a76356b472e9e85fbd4c50282ecf358dc75710e612.jpg)  
Fig. 8. Excerpt of S-BPM model representation (already elaborated) – left: part of subject interaction diagram showing CFO’s (3) modified interaction (changes printed in bold); right: extended behavior diagram of CFO (changes printed in bold).

actors. This aim is supported by fulfilling the ARs and MSFs described in Section 2.1 (cf. proposition 1 as described in the introduction to Section 4).

ARs 1 and 2 (individual articulation, collaborative consolidation, clarification on scope, and setup of work environment) are implemented via the design of the methodology and are reflected in phases 2 and 3 of the procedural model (‘‘articulation and alignment’’ and ‘‘elaboration through virtual enactment’’) by different methodological approaches. In phase 2, alignment was provoked by explicitly articulating individual models in a first step and consolidating them in a second step. The layout guidelines for model consolidation were successfully deployed as a structural scaffold in this case (cf. MSF 4). In phase 3, individual articulation was facilitated by virtual enactment of the activities of each involved actor. The communication-centric modeling approach used in this phase also triggered collaborative alignment, where necessary. Virtual enactment acted as a procedural scaffold, guiding the elaboration process (cf. MFS 4).

AR 3 (convergence of the understanding of a scope of work) was appropriately supported by the concept map-based collaborative modeling approach used in phase 1 (‘‘setting the stage’’). The incremental rise in modeling language complexity throughout the phases, in particular, helped the inexperienced modelers become familiar with reading and understanding models, and using them as a form of expression for their own viewpoint. Progressing from semantically open concept mapping in settingthe-stage phase over single-perspective flow-oriented modeling in individual articulation to multiperspective communicationoriented modeling during collaborative consolidation thus appropriately implemented MSF 2 while still maintaining the goal of creating a model representation that adheres to a formal syntax, allowing for further processing in an IS. This goal is also supported by the implementation of MSF 4 via the enactment component that enables selective generalization to case-independent models until a common model of the full work process is created (MSF 1).

A drawback of the reduced set of modeling elements became apparent during collaborative consolidation. The lack of a structured approach to specify the content of EXCHANGE elements seems to lead to ‘‘vague’’ definitions [24] that neither reflect nor facilitate reaching common ground on the transferred information or artifacts. The opportunity to annotate informally information about these aspects (cf. MSF 3) was hardly used in the case study and does not seem to replace appropriately a structured modeling approach in terms of articulation and alignment support.

AR 4 (identifying and keeping track of conflicting issues) was implemented in the case study by using the card-based tool for collaborative consolidation. The representation of conflicting issues is imminent to the modeling approach, as it requires matching associated or equivalent cards. Conflicts are made explicit whenever this matching fails. This approach has worked well in this case study, with respect to both process support and results. The lack of matching cards was hardly ever accepted without further discussion, thus avoiding the undesirable quick consensus building approach mentioned in Section 3.3. Identified issues, however, rarely led to extensive discussions, but were resolved rather quickly. In the feedback session, participants attributed this to the fact that they did not have conflicting viewpoints, but rather suffered from a lack of transparency. Still, according to immediate feedback after the workshop, uncovering different perceptions and resolving them worked well, and everybody was satisfied with the resulting model. This is backed by the observation that no changes to the operative instance of the work process were requested during the pilot phase.

Please cite this article in press as: S. Oppl, Articulation of work process models for organizational alignment and informed information system design, Inf. Manage. (2016), http://dx.doi.org/10.1016/j.im.2016.01.004

S. Oppl / Information & Management xxx (2016) xxx–xxx

While resolution of conflicting issues was facilitated well in phase 2, observations were different in phase 3. The switch between different model visualizations from card-based consolidation to computer-based elaboration initially made it hard for participants to recognize the semantic equivalence of both models. This issue was resolved when virtual enactment was started and tracked simultaneously in both model versions. The setting in which the elaboration workshop was held, however, reduced the involvement of the actors in modeling. They took no active role in modeling anymore, and left finding appropriate model representations to the expert modeler, who was perceived to be responsible for making the model elaborations, although his/her passive role was clearly articulated. Although none of the actors has claimed this to have a negative impact on the modeling outcome, the validity of their perception is questionable. Observations have shown at least two cases where the actors accepted content-wise changes proposed by only one actor and made by the expert modeler without questioning them. First, experiments with enabling model elaborations done by the actors themselves during virtual enactment using an interactive elaboration component based on prompting embedded in the enactment environment were made since then. Initial results with this setup were promising, but require further evaluation before they can be used in real-world settings.

The aim of generating a model that is a syntactically valid and semantically sound (cf. proposition 2) was reached. Analyzing the process of model creation, however, reveals some limitations of the current tool support, which were resolved in the case study by interventions of the facilitator. Future work will have to address these limitations and extend tool support toward providing better procedural scaffolds for model transformation and elaboration.

## 5. Conclusions

This article has proposed a methodology that enables people, who are not expert modelers, to articulate and negotiate their use of work processes in the form of collaboratively created conceptual models. The design of the methodology prioritizes ease of use and understandability over semantic completeness during articulation. Elaborating these models toward a representation of the process in all its variations is done in a separate phase. The methodology builds upon two compatible modeling languages, of which the first supports case-based articulation and alignment of collaborative work models, and the second is executable in IT systems, representing work processes in all their variants. Using different forms of representations is necessary, as different requirements must be met for human actor interpretation and technical actor interpretation [38,72].

The methodology is backed by a set of tools that provide scaffolds for the methodological steps. Most prominently, a nontechnology-enhanced, card-based tool for performing individual articulation and collaborative consolidation is presented. The result of articulation and consolidation is processed in a transformation step, in which a tool generates an executable version of the articulated model. The virtual enactment BPMS processes this model and allows to generate a description of the work process in all its variants.

## 5.1. Contributions

The proposed methodology, backed with the current tool prototypes, has been validated by the case study described in Section 4, which confirmed that the methodology meets the requirements set up in Section 2.1. The major contributions of the present work consequently are, first, the integrated chain of modeling steps, which is a novel way of guiding actors with no prior modeling experiences through articulating, aligning, and refining their views on collaborative work processes, and results in syntactically valid and semantically correct business process models. The second is the card-based modeling language designed for collaborative articulation and alignment of work process knowledge while maintaining syntactic and semantic compatibility to formal, executable process modeling languages such as S-BPM, together with the toolset that allows for transforming and elaborating these models interactively. This is novel, as it meets the requirement of modeling objectives pursued in both natural modeling and formal modeling [72]. From a practical perspective, the results of the case study show that organizations can expect the identification of inefficiencies that arise from the division of labor in collaborative work (such as the duplication of requesting offers from potential suppliers) and the development of process models that better reflect the requirements of the operative staff (such as the request of the CFO to consult with domain experts him/herself).

## 5.2. Limitations

The present research has some limitations. In terms of research design, its empirical validation is rather limited, as this article only reports on a single case study. However, it still shows that the design objectives of the methodology have been reached and provided valuable first insights for potential areas of improvement. Following a design science approach, this provides the foundation for the next iteration of the designed artifacts. Technically, the implementation of the interfaces between the used tools was not sufficiently stable for unattended actor-driven operations. Several manual interventions in the transformation process between the card-based model and the S-BPM model have been necessary due to limitations of the interactive model transformation algorithms. This, however, has not affected the application of the methodology and thus has no impact on the outcome of the case study. Methodologically, the resolution of conflicting viewpoints during collaborative consolidation has not yet been sufficiently researched. While the descriptive analysis of the identifiable behavior during consolidation provides a starting point for choosing appropriate interventions, further research in this area should lead to improvement of the methodology. In general, the focus of research has been put on single work processes. Dependencies between different work processes, which are common from an organizational perspective, are not explicitly addressed methodologically, but are only considered indirectly via the involved actors, if they chose to justify their arguments during consolidations based on such dependencies. Whether and how a more comprehensive perspective considering collections of interdependent process can be considered in the methodology remains an open issue to be addressed in future research. Validation by or involvement of stakeholders, who are not operatively participating in the work process, but are responsible for or affected by them, could be a potential approach to address this issue.

## 5.3. Future work

In future work, further experimental and practical evaluation of the methodology is planned. This includes deploying it in more diverse organizational settings and evaluating the effects of its components in more detail. This will require evaluation setups that go beyond participatory observation and enable a structured review of the collaborative articulation and alignment processes of the actors in the different phases and how they interact with the designed artifacts. Approaches for an empirical evaluation of the addressed phenomena can be found in the field of collaborative modeling support. Rittgen [53] provided an insight into the evaluation of the collaborative modeling part of the methodology based on the semiotic qualities observable during modeling. Claes et al. [4] focused on analyzing process modeling and anchored their metrics on dynamic aspects observable during model creation. Hoppenbrouwers and Rouwette [28] used the concept of ‘‘focused conceptualizations’’ to separate the collaborative model building process together with its different conversational topics and analyzed them regarding different aspects of modeling (e.g., required input, desired outcome, participants, guidance measures, and type of abstraction activity). Ssebuggwawo et al. [63] proposed a framework for selecting and combining evaluation methods to address different aspects of collaborative modeling processes. Instantiating this framework would allow to comprehensively describe the effects caused by the phases of the proposed methodology. The findings from these evaluations will further refine both the methodology and toolset. Future iterations of the design will focus on improving technical support for elaboration through virtual enactment (e.g., providing interactive scaffolds for potential modifications of the model) and for the model transformation process (e.g., interactively merging several casebased models to provide a more comprehensive foundation for elaboration through virtual enactment). Finally, the results of this article will be embedded in an IS, supporting organizational learning processes as a front end for articulation, reflection, and distribution of knowledge about organizational work.

## Acknowledgments

The author would like to thank Mr Simon Vogl for his contributions to the technical developments reported in this article, and the participants of the case study for their contributions to the workshops. Special thanks go to the anonymous reviewers for their valuable comments. This study was financially supported by the European Commission within the PEOPLE IAPP program under grant agreement No. 286083 (IANES).

## References

[1] M.I. Aguirre-Urreta, G.M. Marakas, Comparing conceptual modeling techniques ACM SIGMIS Database 39 (2), 2008, p. 9.

[2] P. Antunes, D. Simo˜es, L. Carrico, J.A. Pino, An end-user approach to business process modeling, J. Netw. Comput. Appl. 36, 2013, pp. 1466–1479.

[3] C. Britton, S. Jones, The untrained eye: how languages for software specification support understanding in untrained users, Hum.–Comput. Interact. 14 (1–2), 1999, pp. 191–244.

[4] J. Claes, I. Vanderfeesten, J. Pinggera, H.A. Reijers, B. Weber, G. Poels, A visual analysis of the process of process modeling, Inf. Syst. e-Bus. Manag. 13 (1), 2013, pp. 147–190.

[5] H.H. Clark, S.E. Brennan, Grounding in communication, Perspect. Soc. Shared Cogn. 13, 1991, pp. 127–149.

[6] B. Curtis, M.I. Kellner, J. Over, Process modeling, CACM 35 (9), 1992, pp. 75–90.

[7] H.D. Dann, Variation von Lege-Strukturen zur Wissensrepra¨sentation, in: B. Scheele (Ed.), Struktur-Lege-Verfahren als Dialog-Konsens-Methodik, (vol. 25), Aschendorff 1992, pp. 2-41

[8] I. Davies, P. Green, M. Rosemann, M. Indulska, S. Gallo, How do practitioners use conceptual modeling in practice? Data Knowl. Eng, 58 (3), 2006, pp, 358–380.

[9] T. Engelmann, F.W. Hesse, How digital concept maps about the collaborators’ knowledge and information influence computer-supported collaborative problem solving Int. L. Comput,-Support, Collab. Learn. 5 (3) 2010 pp. 299–319

[10] D. Fahland, M. Weidlich, Scenario-based Process Modeling with Greta, BPM Demos. 2010 pp. 52–57.

[11] E.D. Falkenberg, W. Hesse, P. Lindgreen, B.E. Nilsson, J.L.H. Oei, C. Rolland, et al., A Framework of Information System Concepts, The FRISCO Report IFIP WG 8.1, 1998.

[12] F.G. Feltham, Do the blocks rock: a tangible interface for play and exploration, in: Proceedings of OZCHI ’08, ACM, New York, NY, 2008, pp. 188–194.

[13] F. Fischer, H. Mandl, Knowledge convergence in computer-supported collaborative learning: the role of external representation tools, J. Learn. Sci. 14 (3), 2005, pp. 405–441.

[14] F. Fischer, J. Bruhn, C. Gra¨sel, H. Mandl, Fostering collaborative knowledge construction with visualization tools, Learn. Instr. 12 (2), 2002, pp. 213–232.

[15] A. Fjuk, M. Nurminen, O. und Smørdal, Taking Articulation Work Seriously: An Activity Theoretical Approach, TUCS TR 120, Turku Centre for Computer Science 1997.

[16] A. Fleischmann, W. Schmidt, C. Stary, S. Obermeier, E. Bo¨rger, Subject-Oriented Business Process Management, Springer, 2012.

[17] L.A. Franco, E.A.J.A. Rouwette, Decision development in facilitated modelling workshops, Eur. J. Oper. Res. 212 (1), 2011, pp. 164–178.

[18] H. Gao, E. Shen, S. Losh, J. Turner, A review of studies on collaborative concept mapping, J. Interact. Learn. Res. 18 (4), 2007, pp. 479–492.

[19] N. Genon, P. Heymans, D. Amyot, Analysing the cognitive effectiveness of the BPMN 2.0 visual notation, Software Language Engineering, (vol. 6563), Springer, Berlin, Heidelberg, 2011 pp. 377–396.

[20] J. Goncalves, F.M. Santoro, F.A. Baiao, Business process mining from group stories, in: Proceedings of CSCWD, 2009, pp. 161–166.

[21] T. Herrmann, K.U. Loser, Facilitating and prompting of collaborative reflection of process models, in: Proceedings of MoRoCo 2013. ceur-ws, 2013.

[22] T. Herrmann, A. Nolte, Combining collaborative modeling with collaborative creativity for process design, Proceedings of Coop 2014, pp. 1–16.

[23] T. Herrmann, M. Hoffmann, K.U. Loser, K. Moysich, Semistructured models are surprisingly useful for user-centered design, Proceeding of COOP, IOS Press, 2000, pp. 159–174.

[24] T. Herrmann, M. Hoffmann, G. Kunau, K.U. Loser, Modelling cooperative work: chances and risks of structuring, Presented at the Cooperative Systems Design A Challenge of the Mobility Age. Proceedings of COOP, IOS Press, 2002 , pp. 53–70.

[25] T. Herrmann, K.U. Loser, I. Jahnke, Sociotechnical walkthrough: a means for knowledge integration, Learn. Organ. 14 (5), 2007, pp. 450–464.

[26] A.R. Hevner, S.T. March, J. Park, S. Ram, Design science in information systems research, MIS Q. 28 (1), 2004, pp. 75–105.

[27] A. Hjalmarsson, J.C. Recker, M. Rosemann, M. Lind, Understanding the behavior of workshop facilitators in systems analysis and design projects: developing theory from process modeling projects, Commun. Assoc. Inf. Syst. 36 (22), 2015, pp. 421–447.

[28] S. Hoppenbrouwers, E. Rouwette, A dialogue game for analysing group model building: framing collaborative modelling and its facilitation, Int. J. Organ. Des. Eng. 2 (1). 2012. pp. 19–40.

[29] S. Hoppenbrouwers, R. Thijssen, J. Vogels, Operationalizing dialogue games for collaborative modeling, in: Proceedings of MoRoCo 2013. ceur-ws, 2013.

[30] E. Hornecker, Understanding the benefits of graspable interfaces for cooperative use, Presented at the Proceedings of Coop, 2002, pp. 4–7.

[31] D. Ifenthaler, Diagnose lernabha¨ngiger Vera¨nderung mentaler Modelle, University of Freiburg, 2006.

[32] D. Ifenthaler, P.N. Pirnay-Dummer, N.M. Seel, The role of cognitive learning strategies and intellectual abilities in mental model building processes, Technol ogy, Instruction, Cognition and Learning 5. 2007, pp. 353–366.

[33] S.M.M. Joosten, Why modellers wreck workflow innovations, Business Process Management: Models, Techniques, and Empirical Studies, Springer, 2000.

[34] D.L. Jorgensen, Participant Observation, John Wiley & Sons, Inc, Hoboken, NJ, USA, 1989http://dx.doi.org/10.1002/9781118900772.etrds0247.

[35] S. Kabicher, S. Rinderle-Ma, Human-centered process engineering based on content analysis and process view aggregation, Proceedings of Caise 2011, pp. 467–481.

[36] M. Kaltenbrunner, R. Bencina, reacTIVision: a computer-vision framework for table-based tangible interaction, in: Proceedings of TEI ’07, 2007, pp. 69–74.

[37] U. Kannengiesser, M. Radmayr, R. Heininger, N. Meyer, Generating subjectoriented process models from ad-hoc interactions of cognitive agents, in: Proceedings of Web Intelligence (WI) and Intelligent Agent Technologies (IAT), vol. 3, 2014, pp. 440–446.

[38] J. Krogstie, G. Sindre, H.D. Jørgensen, Process models representing knowledge for action: a revised quality framework, Eur. J. Inf. Syst. 15 (1), 2006, pp. 91–102.

[39] H. Lai, R. Peng, Y. Ni, A collaborative method for business process oriented requirements acquisition and refining, in: Proceedings of ICSSP, 2014, pp. 84–93.

[40] A. Luebbe, M. Weske, Bringing design thinking to business process modeling, Design Thinking, Springer, Berlin, Heidelberg, 2011 pp. 181–195.

[41] T. Margaria, S. Boßelmann, B. Kujath, Simple modeling of executable role-based workflows: an application in the healthcare domain, J. Integr. Des. Process Sci. 17 (3), 2013.

[42] G.P. Mullery, CORE – a method for controlled requirement specification, ICSE ’79 Proceedings of the 4th International Conference on Software Engineering, 1979, pp. 126–135.

[43] J.D. Novak, A.J. Canas, The Theory Underlying Concept Maps and How to Construct Them. Florida Institute for Human and Machine Cognition, 2006

[44] M. Nu¨ ttgens, F.J. Rump, Syntax und Semantik Ereignisgesteuerter Prozessketten (EPK), in: Proceedings of Promise, Potsdam, Germany, 2002, pp. 64–77.

[45] S. Oppl, Articulation of subject-oriented business process models, in: Proceedings of the 7th International Conference on Subiect-Oriented Business Process Management, 2015, pp. 1–11.

[46] J.A. Pino, F.M. Santoro, M.R.S. Borges, CEPE: cooperative editor for processe elicitation, in: Proceedings of HICSS, 2000.

[47] M. Prilla, A. Nolte, Integrating Ordinary Users into Process Management. Enterprise Business-Process and Information Systems Modeling, 2012 pp. 182–194.

[48] i. Recker, Opportunities and constraints: the current struggle with BPMN, Bus. Process Manag. J. 16 (1), 2010, pp. 181–201.

[49] J.C. Recker, A. Dreiling, Does it matter which process modelling language we teach or use? in: Proceedings of The Australasian Conference on Information Systems 2007.

[50] J. Recker, A. Dreiling, The effects of content presentation format and user characteristics on novice developers’ understanding of process models, Commun Assoc. Inf. Syst. 28 (6), 2011, pp. 65–84.

Please cite this article in press as: S. Oppl, Articulation of work process models for organizational alignment and informed information system design, Inf. Manage. (2016), http://dx.doi.org/10.1016/j.im.2016.01.004

S. Oppl / Information & Management xxx (2016) xxx–xxx

[51] J. Recker, N. Safrudin, M. Rosemann, How novices design business processes, Inf Syst. 37 (6), 2012, pp. 557–573.

[52] M. Renger, G.L. Kolfschoten, G.J.D. Vreede, Challenges in collaborative modelling: a literature review and research agenda, Int. J. Simul. Process Model. 4 (3/4), 2008, p. 248.

[53] P. Rittgen, Negotiating models, in: J. Krogstie, A. Opdahl (Eds.), Advanced Information Systems Engineering, (vol. 4495), Springer, Berlin, Heidelberg, 2007 , pp. 561–573.

[54] P. Rittgen, Collaborative modeling of business processes: a comparative case study, in: Proceedings of the 2009 ACM symposium on Applied Computing, 2009.

[55] P. Rittgen, Collaborative modeling – a design science approach, in: Proceedings of HICSS, 2009, pp. 1–10.

[56] J. Roschelle, Designing for cognitive communication: epistemic fidelity or mediating collaborative inquiry? in: D. Day, D.K. Kovacs (Eds.), Computer, Communication and Mental Models, Taylor & Francis, 1996, pp. 15–27.

[57] E. Rouwette, J. Vennix, T. van Mullekom, Group model building effectiveness: a review of assessment studies, Syst. Dyn. Rev. 18 (1), 2002, pp. 5–45.

[58] F.M. Santoro, M.R.S. Borges, J.A. Pino, Acquiring knowledge on business processes from stakeholders’ stories, Adv. Eng. Inf. 24 (2), 2010, pp. 138–148.

[59] M. Sarini, C. Simone, Recursive articulation work in Ariadne: the alignment of meanings, in: Proceedings of COOP, 2002, pp. 191–206.

[60] N.M. Seel, Model-centered learning and instruction, Technol. Instr. Cognit. Learn. 1 (1), 2003, pp. 59–85.

[61] H. Shen, B. Wall, M. Zaremba, Y. Chen, J. Browne, Integration of business modelling methods for enterprise information system analysis and user requirements gathering, Comput. Ind. 54 (3), 2004, pp. 307–323.

[62] M. S<sup>ˇ</sup>kerlavaj, M.I. S<sup>ˇ</sup>temberger, R. S<sup>ˇ</sup>krinjar, V. Dimovski, Organizational learning culture—the missing link between business process change and organizational performance, Int. J. Prod. Econ. 106 (2), 2007, pp. 346–367.

[63] D. Ssebuggwawo, S. Hoppenbrouwers, H.A. Proper, Applying AHP for collaborative modeling evaluation, Int. J. Inf. Syst. Model. Des. 4 (1), 2013, pp. 1–24.

[64] H. Stachowiak, Allgemeine Modelltheorie, Springer, Wien, 1973.

[65] A. Strauss, Continual Permutations of Action, Aldine de Gruyter, New York, 1993.

[66] O. Tu¨ retken, O. Demiro¨ rs, Plural: a decentralized business process modeling method. Inf, Manag, 48 (6), 2011, pp. 235–247

[67] C. van Boxtel, A. Veerman, Diagram-mediated collaborative learning: diagrams as tools to provoke and support elaboration and argumentation, CSCL, 2001

[68] J. Vennix, H.A. Akkermans, E. Rouwette, Group model-building to facilitate organizational change: an exploratory study, Syst. Dyn. Rev. 12 (1), 1996.

[69] A. Weinberger, K. Stegmann, F. Fischer, Knowledge convergence in collaborative learning: concepts and assessment, Learn. Instr. 17 (4), 2007, pp. 416–426.

[70] S.A. White, D. Miers, BPMN Modeling and Reference Guide: Understanding and Using BPMN, Future Strategies Inc., 2008.

[71] R.K. Yin, Case Study Research: Design and Methods, 4th ed., Sage, Los Angeles, 2009.

[72] Z. Zarwin, M. Bjekovic´ , J.-M. Favre, J.-S. Sottet, H.A. Proper, Natural modelling, J Object Technol. 13 (3), 2014, 4:1.

[73] M. zur Muehlen, J.C. Recker, How much language is enough? Theoretical and practical use of the BPMN Advanced Information Systems Engineering, 2008pp. 465–479.

Stefan Oppl is an assistant professor at the Department of Business Information Systems – Communications Engineering, Johannes Kepler University of Linz, Austria. He holds an MSc degree in computer science and an MBA. He received his PhD in computer science from the Technical University of Vienna in 2010. He has been working as a researcher at the Kepler University of Linz since 2003. During the early years of his career, he worked in the area of context-aware group support and mobile learning support systems. Stefan Oppl has been developing means to support collaborative work and knowledge externalization and alignment processes in organizational settings since 2006. He has been involved in several national and EUfounded research projects, and is currently the coordinator and lead scientist of the EU FP7-founded research project IANES (www.ianes.eu). He has also coordinated the Leonardo-da-Vinci Transfer-of-Innovation project FARAW (www.faraw.eu) and the Erasmus Intensive Programme SURGEOM (www.surgeom.eu).
