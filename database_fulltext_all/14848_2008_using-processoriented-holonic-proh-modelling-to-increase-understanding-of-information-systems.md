---
otero_id: 14848
otero_key: "6R8GT9JT"
title: "Using process‐oriented holonic (PrOH) modelling to increase understanding of information systems"
authors: "Ben Clegg; Duncan Shaw"
year: "2008"
journal: "Information Systems Journal"
doi: "10.1111/j.1365-2575.2008.00308.x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using process-oriented holonic (PrOH) modelling to increase understanding of information systems

Ben Clegg\* & Duncan Shaw<sup>†</sup>

Information and Operations Management Group, Aston Business School, Aston University Birmingham, B4 7ET, UK, \* email: b.t.clegg@aston.ac.uk, and <sup>†</sup>email: d.a.shaw@aston.ac.uk

Abstract. Methodologies for understanding business processes and their information systems (IS) are often criticized, either for being too imprecise and philosophical (a criticism often levied at softer methodologies) or too hierarchical and mechanistic (levied at harder methodologies). The process-oriented holonic modelling methodology combines aspects of softer and harder approaches to aid modellers in designing business processes and associated IS. The methodology uses holistic thinking and a construct known as the holon to build process descriptions into a set of models known as a holarchy. This paper describes the methodology through an action research case study based in a large design and manufacturing organization. The scientific contribution is a methodology for analysing business processes in environments that are characterized by high complexity, low volume and high variety where there are minimal repeated learning opportunities, such as large IS development projects. The practical deliverables from the project gave IS and business process improvements for the case study company.

Keywords: systems thinking, business process, modelling, IS development projects, problem structuring methods

## INTRODUCTION

In information systems (IS) design, softer approaches such as participatory design (Bodker, 1996), joint application design (Davidson, 1999) and soft systems methodology (SSM) (Checkland, 1996) are often used to engage stakeholders. For example, by modelling stakeholders viewpoints, SSM can aim to build an accommodating solution which will have the desired impact when implemented (Checkland & Poulter, 2006). However, a main criticism of SSM [and of the broader field of problem structuring methods (Rosenhead, 1989)] is that it is difficult for the novice modeller to apply because the subtle craft skills underpinning the methodology are accessible to only a few who already have experience of their application (Keys. 2006;

Westcombe et al., 2006; Morrill, 2007). In contrast, the modelling principles of harder design methodologies (e.g. data flow diagrams, entity-relationship diagrams) view the world as being more straightforward in that the problem is unitary and they also take the nature of the organization for granted (Pidd, 1996). Pidd explains that the outcome from a harder model is a ‘correct’ answer and not necessarily learning about the context in which issues exist. Consequently, solutions may be technically appropriate but culturally/organizationally infeasible or fail to meet user needs.

This paper presents a new approach called the process-oriented holonic (PrOH) modelling methodology, which bridges these softer and harder paradigms. Earlier versions of the methodology from previous related projects (that lacked the sophistication and rigour to join individual models within a set) have focused on managing information about new product design (Cole, 1997; Cole & Boardman, 1995), concurrent engineering (Boardman & Cole, 1996; Clegg & Boardman, 1997), computing service provision (Ramsey et al., 1995), export processes (Al-Kalifa, 2000), systems engineering (Sherman et al., 1996) and project management (Boardman, 1994). These have taken place in the aerospace, pharmaceutical and industrial engineering sectors which were chosen because they all design complex products that are initially made in low volumes and rely on IS to capture design information and transfer it to production departments. This paper discusses the latest developments of the methodology that have evolved from an action research project in the capital goods sector. Such discussion is important for educating reflective developers and encouraging iterative development (Mathiassen & Purao, 2002; Iverson & Mathiassen, 2004).

This project’s theoretical challenge was to integrate harder and softer modelling approaches. This is a topic which has received academic attention, for example, Mingers & Gill (1997) cal this ‘multi-methodology’, Pidd (2004) promotes further thinking about the ‘complementarity’ of harder/softer methods, while Fitzgerald and Howcroft (1998) go further to suggest ‘integrationism’ where alternative approaches are integrated into a single coherent mode of analysis. The theoretical challenge was also to overcome the narrowness of many existing approaches and their rigidity in use [highlighted by Avison et al. (1998)].

The practical challenge behind the development of The PrOH modelling methodology was to satisfy the need of managers in organizations to better understand their organization’s processes and IS. This particular paper focuses on one major case study from the capita goods sector (which was conducted along with other complementary ones from the aerospace, pharmaceutical and industrial engineering sectors which are not explicitly discussed in this paper for reasons of brevity). These industries were all chosen because they all involve designing and developing complex new products that are initially made in low volumes and rely heavily on IS to capture their design information and transfer it to their production departments. One particular dilemma for these managers when aiming to understand their organization’s systems was whether to use soft or hard approaches. As Fitzgerald (2000) states, ‘. . . practitioners have in many cases assimilated good practices and techniques and may be rejecting methodologies for pragmatic reasons . . .’ In this case study, what the company ideally required was an integration of both: an easily accessible methodology that provided structured and explicit modelling guidance that accommodated stakeholder perspectives that could deliver a coherent set of models (Avison et al., 2001b; Rosenhead & Mingers, 2001). Through action research, a new methodology took shape and evolved into that reported here. The purpose of this paper is to establish the new PrOH modelling approach in the context of business process and IS design.

PrOH modelling aims to help novice modellers to build defensible process models while resolving complexities, for example, where processes are difficult to define perhaps because of low throughput volumes or high variation; involve a lengthy time to complete; or provide few repeated learning opportunities. Such properties make the PrOH modelling methodology less akin to a systems analysis method (e.g. data flow diagrams or entity-relationship diagrams) which assumes that most specifics of the situation are known, and more like a problem structuring method (e.g. SSM) where different people can view the problem differently. This paper gives a literature review for PrOH modelling, the action research approach used to deliver it, a case study from Marconi Electronic Systems (MES) focusing on IS issues in materials requirements planning (MRP) and the implications for IS design.

## FOUNDATIONS TO PROH MODELLING

To establish a sound conceptual foundation to such work (Fitzgerald, 1996; 1997), we intro duce key terms to explain how business process modellers can use models to think about systems. ‘Holistic’ is a lay term that means to consider the whole and its emergent properties that are greater than the sum of its parts, and in PrOH, it is used in this way. When trying to embody holistic thinking into analytical models, general language is often not sufficiently accurate and specific constructs need to be used which has led to the term ‘holon’ being offered to describe a model that represents one part of a system (Koestler, 1967; Beer, 1985). For PrOH, a holon is a model of a human activity system (e.g. a business process) that contains all the fundamental systems thinking principles such as a system boundary, entities, entity relationships, control loops, a name and an environment (Flood & Jackson, 1991). A holon is also considered to be part of a larger system and may itself contain other systems (Jackson & Keys, 1984). PrOH models use this construct more explicitly than any other before as it uses it to explore hidden as well as emergent properties to build set of models known as ‘holarchies’ (explained in detail using the case study later in the paper). Therefore, as the modelling methodology uses holons, it follows that the modelling technique is ‘holonic’. To say that the methodology is ‘holonic’ is more precise and is more meaningful for expert practitioners and theorists working in the area. The authors believe that precise terminology is necessary to advance theoretical developments. This and other closely related concepts are now introduced using via a ‘concept-centric’ literature review (Webster & Watson, 2002) that draws upon general systems thinking (Jackson & Keys, 1984) and problem structuring methodologies (PSMs), in particular SSM. This work has been called on by authors such as Senge (1990), Mitroff and Linstone (1993), Wastell (1996), Avison et al. (1998) and Ulleru et al. (2002).

## Scope the granularity

Some modellers use the notions of scope (i.e. the range of activities modelled) and/or level (the detail/depth of that modelling) to frame a model’s content (Robinson, 2003; Greasley, 2004; Valacich et al., 2006). For PrOH, this is an oversimplification and so it uses a more sophisticated notion of granularity which, in simple terms, means deciding what goes in and what stays out of the process model (Gardiner & Gregory, 1996). In this, one must decide on the size of each piece of the model (whether that piece is an entity within a model, an entire model or a set of models). This is a recursive concept (Jackson & Keys, 1984) that can be applied at any level of modelling and guides thinking at the initial scoping stage when the level of detail of the exercise is being considered. Granularity should be revisited throughout the modelling process to ensure consistency and appropriateness for the purpose of achieving project objectives. In PrOH modelling, granularity has the three dimensions (pitch, length and width); for each of these dimensions, a validation question is used to assess potential inclusion in the model. This is shown in Figure 1.

Pitch relates to the organizational level(s) at which the modelling exercise is conducted. The validation question in Figure 1 guides whether to include a factor in the model given the pitch of the model. Processes often extend beyond the boundary (Flood & Jackson, 1991) of a model, so the modeller must decide where to start and finish modelling a process, which is

![](/api/attachments/6R8GT9JT/fulltext/images/bbc5c411422660bdd028f383423dcc7813fa46f829397dd492ffe335fe7b0690.jpg)  
Figure 1. Scoping the granularity of a business process model.

## VALIDATION QUESTION:

Does the inclusion of any particula elements, relationships, inputs, outputs or feedback loops in the model, help to describe the behaviour of the core business process and its critical success factors within these dimensions?

referred to as the length of the model. Specific model inclusions/exclusions because of length are also determined using the Figure 1 validation question.

A PrOH modeller must also decide on model width; that is, how much supporting activity description does a model require to support the core business process? For example, if a software design process is being modelled and the main process output is to produce prototype designs, then most of the model could focus on activities of designers and engineers, which can be directly linked to the main output. However, some modellers may wish to include Finance or Marketing activities which could give an indirect contribution to the main output, and hence make the model wider. Again, the inclusion/exclusion in the model based on width is informed by the validation question in Figure 1.

Pitch, width and length are closely related and collectively define the model’s scope and number of levels. Each level can be described in terms of its granularity; if a model depicts a design process in a very non-specific manner, such as Corporate Management<sup>1</sup> or Turnover Targets, it will have a coarse granularity in comparison to that which depicts the same design process in terms of Shop Floor Operatives sort out any Estimate Queries. The coarser the granularity of the model, the more strategic in nature it is. A robust set of models will ensure that consistent granularity exists within models at the same level and a clear contrast between models at different levels. A practical example for how these dimensions are used is given later, via the MES case study.

## Systems models should have objectives – not just names

An important facet of some process modelling approaches is to ensure that the objective of the system is explicitly articulated as a fundamental part of the approach: For example, SSM achieves this through the root definition, which is a sentence that articulates, in part, the objective of the transformation process taking place and the worldview which informs that transformation (Wilson, 1990). However, for many methodologies, this is not the case and without well-defined naming rules, some designers may name a system very loosely which is unhelpful but does not break the rules of the methodology.

PrOH modelling requires not only a meaningful name for a model but also a statement about the process objective which becomes an explicit part of a model’s core process description, defining who does what for whom. A PrOH model about manufacturing could have the objective defined as the, The SBU must manage delivery of the Assembled Units to End Customers (as in Figure 2). This would have to appear in the core process description to be a verifiable model (i.e. true to the methodology and techniques by which the model was constructed – explained in more detail later) and the title of the model would be concordant (e.g. The SBU must manage delivery of the Assembled Units). While this is an option with most methodologies, it is fundamental to the PrOH modelling methodol ogy because it becomes part of the template for every model.

![](/api/attachments/6R8GT9JT/fulltext/images/68b1f05144fe3d11dcfd90510a6b898d01ac8de259b8f6298602dfb2592a0d2a.jpg)  
Figure 2. A PrOH model for MES – the SBU (strategic business unit) must manage delivery of the assembled units

## Minimize codification, maximize normal language

Most approaches to business process modelling rely on a mix of graphics, language and codification which can bring confusion if not carefully designed. For many PSMs, the aim is for participants to perceive that the models have been informed by them and belongs to them (Rosenhead & Mingers, 2001) – so their commitment to the outcome is partly built through their own self belief. From certain PSMs, we can take the following lessons for model building:

1 using normal language (English) in models is important to reduce communication barriers between modeller and stakeholder, and to support two-way sense making (Eden, 1988); Conklin, 2005);

2 models should rely as heavily as possible on terminology which originates from the stakeholders (either through capturing that wording during individual interviews, or group workshops), and not that which originated from a facilitator (Ackermann, 1996); and

3 through the concept of procedural rationality (Simon, 1976), the modelling process should be as transparent and user-friendly as possible (e.g. designing out complex codification o entries or numerous obscure modelling rules) (Johnson & Johnson, 2002). This includes explaining relationships and behaviour of the process in normal language within the models.

PSMs do not suggest that codification in the process is unhelpful; indeed, it is often essential when managing complex data, but the coding schema needs to be easily understandable, usable and effective (Davison et al., 2004). This has been proven to be possible by othe problem structuring methods e.g. strategic options development and analysis relies heavily on cognitive maps of ideas linked by arrows (Eden, 1995) and participants can design the coding schemas themselves to help them make better use of the concepts; Dialog Mapping relies on a handful of coding schema (questions, ideas, arguments all linked by arrows signifying dialogue) which helpfully structure the model’s content (Conklin, 2005).

In alignment with these principles, PrOH modelling uses graphics to reach an appropriate balance between the use of normal language and codification within a model. The models contain a simple set of symbols (bubbles and arrows) to represent different types of words (nouns and verbs, respectively) to represent the business process. All noun phrases (i.e. resources) are placed in bubbles while verb phrases are placed on arrows. Together, the noun phrases in the bubbles and the verb phrases on the arrows form readable sentences that describe the process in normal language. Additionally, to contain more helpful information in the model, graphics highlight the difference between the core business process and the wide supporting activities (and provide a helpful presentation medium).

## ‘Enrich and abstract’, do not ‘reduce and aggregate’

Some hard methodological approaches to systems modelling can lead modellers to produce models that are pitched at more than one level [e.g. data flow diagrams explicitly take modellers through various levels from high/overview to low/detailed levels (Valacich et al., 2006)]. This may lead modellers to define a task and then starting to break it down to sub-tasks, sub-sub-tasks and so on. Reductionism may be suitable for analysing data needs for certain IS (e.g. using data flow diagrams or entity-relationship diagrams) or producing product routings around a factory (e.g. using a simple flow chart). The usefulness of reducing tasks in this manner is suited to low variation, high volume and relatively short lead-time processes where repeated learning opportunities are possible (e.g. mass produced cars); common reasons for doing this might be for an audit or a quality control exercise (Nookabadi & Middle, 1996).

Like SSM, PrOH modelling recognizes that business processes and IS involve more than just a list of tasks to perform (Checkland & Scholes, 1996). Business processes require people to make decisions about complex issues involving the use of tangible and intangible transfor mational resources (e.g. computer hardware and information from an MRP database) that are used to transform a huge range of inputs (e.g. people, information, material) to outputs that fulfil process objectives (e.g. finished products) (Johnson & Scholes, 2002).

To understand complex processes and IS, The PrOH modelling methodology proposes the concept of holarchical enrichment, i.e. building understanding of a process and its IS by constructing a set of models that recognize that systems properties exist and need be modelling and managed; this is demonstrated later using the case study. When the core process for The SBU must manage delivery of the Assembled Units model (Figure 2) is considered, an initial core process description (and objective) could be defined as follows (tracing the bold arrows): the Customer supplies Potential Order Intake which becomes the responsibility of the SBU Management Team. The SBU Management Team must manage the delivery of the Assembled Units delivered to the respective End Customer. The core business process description can then be widened by adding supporting activity descriptions within the same model, or by building a lower set of models to enrich specific aspects. For example, new lower level core process descriptions and objectives might focus specifically on Order Intake, Set-up and Planning, Manufacture or Order Completion. Taking the Manufacture aspect, the new core process description (and objective) about this could be based upon (tracing the bottom right of Figure 2): the Programmes (Bid) Department Project Manager solicits contracted documents to produce the Manufacturing Control Documents (Master Manufacturing Requisition (MMR) and trial Material Resource Plan (MRP)) which were required by the Operations Department. The Operations Department has the responsibility to ensure the First MRP run and continue to complete the Assembled Units which requires action to be taken by the Project Manager. Reinterpretation may be necessary to make it more relevant to the new pitch and supporting activities are used to widen lower level models. Consequently, more sentence descriptions and understanding about causal relationships in process models could be included in successively lower levels. In contrast, the reductionism of task-breakdown would only produce increasing amounts of fragmented smaller tasks which does not build understanding of complex issues to the same extent. Therefore, enrichment is an essential property of The PrOH modelling methodology.

The reverse of enrichment is abstraction (see Figure 3). If a modelling exercise begins with the detail and an overview is required, then thought must be given to how a more concise account can be re-pitched in a higher level model (e.g. going from operational to tactical or tactical to strategic). The importance of abstraction is that new descriptions about the higher level system representing more than one lower level system can be added, which may contain ‘emergent properties’, i.e. those which are realized through the modelling process (Checkland, 1996, pp. 74–82). Together, abstraction and enrichment is used in PrOH modelling to build sets of models about complex and difficultly codified processes in a holistic manner (Clegg & Boardman, 1996).

The contrast with abstraction is aggregation (Figure 3). Aggregation occurs when smaller tasks are progressively lumped together into larger tasks and merely collectively relabelled. For example the sub-tasks involved in Order Intake, Set-up and Planning, Manufacture and Order Completion would simply be aggregated further and collectively labelled at the strategic level as ‘SBU Manage Delivery’. Aggregation is the reverse of reduction. Information richness can be lost by aggregation and little new context is gained because the flexibility to reinterpret lower level activities within the context of a more highly pitched model does not exist.

![](/api/attachments/6R8GT9JT/fulltext/images/b7613bda38c644308aed7886ef125bc91451dfafe6a9cf3a337e62cc62a26264.jpg)  
Figure 3. Contrasts in thinking: holistic and hierarchic.

Aggregation assumes that the truthfulness of activity relationships in the lower pitched models is absolute. In contrast, abstraction does not assume this but builds upon the premise that through developing higher level models, one can identify new properties which reshape existing process descriptions and lower level models. In reverse, enrichment is built upon the premise that lower level models can also possess new properties requiring new process descriptions. The PrOH modelling methodology calls these hidden properties (a new concept for systems thinking literature) and these can only be depicted in models if the principle of enrichment rather than reduction is practiced.

There is a common grounding to holistic thinking and hierarchic thinking because both are guided by the systems model and both have, as a general foundation, the idea that systems are comprised of sub-systems within a boundary and exist in an environment (Jackson & Keys, 1984). However, there are differences that become apparent when you begin to model. PrOH treats the contrast as:

1 holistic thinking (abstraction and enrichment of process descriptions) should use holonic based modelling principles leading to holarchies. Models explicitly aim to show properties tha occur relative to the pitch of the model.

2 hierarchic thinking (aggregation and reduction of tasks) should use methodologies and techniques leading to hierarchies. Models aim to define systems in absolute terms.

The former is found more commonly in softer systems methodologies, while the latter is more commonly found in harder systems methodologies. Neither approach should allow key entities or relationships to be omitted from any pitch model of a model, as omissions should be resolved through validation of the model during its construction. However, the verification of a hierarchical model could remove emergent and hidden properties (relationships that may be specific to only one pitch of the model) as a unique occurrence of a relationship at only one pitch is considered to be a methodological mistake in hierarchical thinking. In contrast, PrOH modelling uses sets of

![](/api/attachments/6R8GT9JT/fulltext/images/a56f3163e89da6a2903c93ee611c8aa47452087f2fc62b9e83e5469072bdb43b.jpg)  
holons that are composed into holarchies which actively try and preserve such properties (hidden and emergent) so that nuances of the real world can be reflected.

Modelling World

## Reflect, do not re-create

A process model is often constructed partly to provide insight into the behaviour of the rea world process; it should not aim to recreate it. It is an axiom of approaches such as SSM (Checkland & Scholes, 1996) that models should artfully represent rather than faithfully recreate that which they seek to model; this is an important distinction for PrOH modellers. Morecroft (2004, p. 101) suggests that if careful discipline is not exercised while constructing a model that ‘the model can become so large that no-one really understands it or has confidence in it’. These issues can be addressed more easily if hidden and emergent properties are recognized to exist in the real world and need not be verified out of a model.

The PrOH modelling methodology recognizes that a useful process model should accurately represent all important issues and yet still be parsimonious (Pidd, 1996; Melão & Pidd, 2000): saying something important with enough contextual background to make it meaningful. Figure 4 shows the PrOH modelling methodology stance – that there is a ‘real world’ with actual business processes in it from which data is collected and models are built. Also, tha there is the ‘modelling world’ that uses constructed models as defensible representations of real processes and their important issues. This is a simplified view of that taken by SSM (Wilson, 1990; Checkland, 1999, p. 163).

## Validate and build agreement

The process of building a business process model is as important as the final model itself; in colloquial terms ‘the journey is as important as the destination’. From the initial data gathering through to the model creation and implementation of findings, it is crucial to keep as many stakeholders engaged with the activity as possible. Just as for PSMs, engagement of stakeholders aims to build collective learning about: the system and issues; the consequences of inaction to encourage some action to be taken; and the consequences of action to allow the right action to be taken (Eden & Ackermann, 1998). This learning can build commitment to the right actions because stakeholders believe that the actions are legitimate, in part, because they have been developed using an appropriate, transparent process (Shaw & Edwards, 2005). Also, this allows stakeholders to address issues of concern so as to reduce their impact when final recommendations are made and when implementation is being rolled out (Ackermann & Eden, 1996).

PrOH modelling has its own technique to support the building of agreement in preparation for implementation known as process storyboarding, where one part of the process is pre sented at a time starting with the basic core process statement. Storyboarding aims to make the model easier for readers to mentally digest and allow them to critique the story being presented. This is demonstrated later using the MES case study.

## Summary of the PrOH modelling methodology foundations

As discussed above, the foundations of PrOH help to decide the right granularity for the models (accounting for pitch, length and width), build models with explicit objectives and which reflect the situation accurately while maximizing the use of normal language to encourage stakeholder engagement. As models are being built, details are added to enrich them and enhance their usability for analysing the process. The models aim to be a device through which stakeholders can come to learn more about the processes and so collectively agree their (re)design. Abstraction-and-enrichment of holons builds a holarchy of business process models.

## ACTION RESEARCH METHODOLOGY

The case study reports on an action research case study project based at the MES manufacturing unit in the East Midlands (UK) with 500 employees which gives ‘empirical evidence of usability’ (Fitzgerald, 1996, p. 12). This unit manufactures radar systems for external customers as well as its parent company. The action researchers were approached by the company to help improve the efficacy of their IS supporting their manufacturing process. The overall project had two primary goals:

1 improve how the company’s manufacturing process and their IS operated and interacted (i.e. intervene in a social system and organizational change)

2 develop a suitable approach for doing so. The company gave the academic team complete freedom in this respect and claimed no ownership of it and were happy entertain new and insightful approaches (i.e. contribute to scientific knowledge).

This is in line with the characteristics of action research as given by Baskerville & Wood Harper (1998).

The company had already attempted to address their problems using tools such as Integrated computer aided manufacture DEFinition – version 0 (IDEF0) (IEEE, 1998) and standard Data Flow Diagrams and Flow Charting approaches with limited success, as vast amounts of undisciplined output had been produced without creating any valuable insight. The research motivation was to see whether the ideas of SSM could address some of the shortcomings of the approaches that had already been tried within the context of IS and process improvement. The outcomes of the project were unpredictable, and so action research was used as ‘. . . its strength [action research] lies in its ability to deal with the emergent nature of human systems (Grant & Ngwenyama, 2003, p. 32). The project also operated within the action research definition given by Baskerville (1999) which states that it should, ‘. . . increase the understanding of an immediate social situation, . . . simultaneously assist in practical problem solving and expand scientific knowledge, . . . be performed collaboratively, . . . and is primarily applicable for the understanding of change in social systems’.

The action research methodology aligned with Susman and Everard’s (1978) canonica action research cycle:

1 diagnosing – the project aimed to (1) clarify why there was an inconsistency of purpose between their manufacturing process and their supporting IS (i.e. understanding the social system); and (2) develop a new hybrid process modelling methodology that would be somewhere between those they had already used and those of softer methodologies (i.e. expanding scientific knowledge).

2 action planning – consisted of 32-hour interviews with directors (focusing on strategy), middle management (focusing on tactical planning) and shop floor workers (focusing on daily operations). Through each interview, the researchers built insight (and later a PrOH model) on the manufacturing process and interactions of the supporting IS

3 action taking – it was then necessary to conjoin the separate PrOH models to produce a model of the entire end-to-end customer facing process. The team jointly decided that three levels of the model would adequately represent the issues; strategic, tactical and operational levels. Each level reflected the issues relevant to people working at that level, and simultaneously linked to issues at the other levels represented by a different level of modelling.

4 evaluating – in true action research spirit to the models and improvement points that were developed were extensively reviewed in workshops involving MES employees and academics. The models were validated to see if they represented the real world accurately, they were also verified to make sure that they were adhering to their own rules and guidelines and these experiences built ‘empirical evidence of [their] usability’ (Fitzgerald, 1996, p. 12). Extensive iteration was necessary in what Argyis & Schon (1978) describe as ‘double loop learning’.

5 specifying learning – outcomes of this research were the new PrOH methodology (new methodology and scientific theory) which was fully documented and the changed processes for MES (practical intervention in a social system) that were implemented.

The action researchers worked in a shop-floor office on one day a week for 18 months along with three MES staff, headed by their IS Manager. It was important to be on site and actively collaborating in changes taking place as Pettigrew (1990, pp. 269–270) states ‘the need to explore context, and action where context is a product of action, and action where it is a product of context’ is important.

The PrOH modelling methodology in its current iteration is detailed in the next section. The practical (e.g. process improvements) and theoretical deliverables (e.g. holarchy development) are given together as they are hard to present separately. This is common in presenting action research results as Mansell (1991, pp. 29–30) states an action researcher, ‘acts and simultaneously observes himself acting’.

## A CASE STUDY USING PROH MODELLING

The PrOH modelling methodology is structured around Deming’s (1986) Plan-Do-Check-Act cycle (see Figure 5). Specifically for PrOH modelling, this involves: scoping the granularity (e.g. Plan); gathering of data (e.g. Do); building, enriching and abstracting the model (e.g Check); implementing new process (e.g. Act). These stages are described below for MES through how an individual holon is created and how a holarchy (set of models) is constructed

## Constructing an individual PrOH model: a holon

Methodological stage 1 (in Figure 5) scopes the necessary granularity of the model using the dimensions of pitch, width and length. During data collection (methodological stage 2), the process data and associated issues from which holons are built are collected. The logical input–output relationships between entities within the core process statement and the supporting activities are defined using a tabular format – the PrOH Logic Table (see Table 1). The table can also be used as an aid in defining links between previous and successive holons

![](/api/attachments/6R8GT9JT/fulltext/images/d7e7f0cbd49a28edd1d4390657c78c7696599a8992d3810103a9ad727253f26d.jpg)  
Figure 5. The process orientated holonic (PrOH) modelling methodology.

Table 1. The PrOH logic table showing different paths through Figure 6

<table><tr><td></td><td>Previous key human resource and activity</td><td>Input</td><td>Key human resource</td><td>Performs an activity</td><td>Output</td><td>Next key human resource and activity</td></tr><tr><td>A</td><td>Input from previous process phase: key human resource of previous phase produced core inputs</td><td>Core inputs to be transformed</td><td>Key human resource of current process phase</td><td>Produces core transformed output</td><td>Core transformed output</td><td>Output to next process phase: key human resource of next phase manages next phase</td></tr><tr><td>B</td><td>Input from previous process phase: key human resource of previous phase produced core inputs</td><td>Core inputs to be transformed</td><td>Key human resource of current process phase oversee resources</td><td>Oversee processing of resources for micro operations</td><td>Resources for micro operations</td><td>Output to next process phase: key human resource of next phase manages next phase</td></tr><tr><td>C</td><td>Input from previous process phase: key human resource of previous phase produced core inputs</td><td>Core inputs to be transformed</td><td>Supporting human resource</td><td>Uses resources in essential for producing core transformed output</td><td>Resources for micro operations</td><td>Output to next process phase: key human resource of next phase manages next phase</td></tr></table>

![](/api/attachments/6R8GT9JT/fulltext/images/6675f4896d7ef9a1b40268948b7c06e908fbad3b583c182e7111af6935caea5a.jpg)  
Figure 6. The PrOH model template – key human resource of current process phase produce core transformed output.

within the same pitch of modelling – as well as between different pitches. The structured dataset within the PrOH Logic Table also captures the normal language used by stakeholders. In Table 1, the headers define the entity type for the column, Row A defines the core process statement which is read from left to right; Rows B and C define alternative supporting activities (note: the grey shading denotes a repeating structure to the above row).

The logical structure between the entities and the input–transformation–output information (Juran, 1987) is then converted to the graphical PrOH model and aims to support presentation, understanding, validation and agreement building (methodological stage 3). Table 1 and Figure 6 are templates for all holon models, including the case study models.

In the template (Figure 6), resource entities are placed within bubbles and text on the links between the bubbles contains verbs (i.e. activity descriptions) to describe activities being conducted. For simplicity, the template here only distinguishes between human resource, shown in black bubbles, and non-human resource (tangible or intangible such as financial or design information) shown in white bubbles. This template serves a similar purpose to Checkland’s SSM ‘root definition’ (Checkland & Scholes, 1996) as it defines the essentia parts of each individual model

The bold arrows of the template running from top left to bottom right show the core business process and should be included in all models (‘Row A’ in Table 1). The remaining paths of the model (with greyed cells in Table 1) show examples of supporting activity descriptions that become adapted to create instantiations of specific case studies. How much supporting description to include is decided by the width and pitch validation. The core business process can be read by tracing the bold arrows and annotations of Figure 6 and should define the objective of the process which, generically is to have . . . the key human resource of the previous phase produce the core transformed input to service the key human resource of the current process phase who produces a core transformed output essential for the key human resource of the next process phase. Process knowledge is read from the diagram using everyday language. The words and number of supporting activity branches are adapted from this generic template to produce specific holon models.

Using the PrOH Logic Table from MES (in Appendix), a single top-level PrOH model is given in Figure 2. It contains an instantiation of the core process statement on the arrows which runs from top left to bottom right, it is read from Figure 2 as, the Customer supplies potential Order Intake which becomes the responsibility of the SBU Management Team. The SBU Management Team must manage the delivery of the Assembled Units delivered to the respective End Customer. A wider supporting activity is described as, the SBU Management Team periodically produce Status Reports to inform the Corporate Management. Corporate Management define Corporate Policy which directs the SBU Management Team is also included within the width of the model; this serves as a control loop – making sure that the operational strategy of the SBU is concordant with the parent company’s overall strategic vision. In systems thinking terms, this keeps the process from becoming chaotic.

Other wider activities in the strategic level model in Figure 2 include the:

1 Internal Customers supply Works Requisitions which are allocated to either the Spares or Repairs Cell Project Manager who can directly set-up the Manufacturing Control Documents (MMR – Master Manufacturing Requisition and the MRP – Manufacturing Requirements Planning)

2 External Customers supply an RFQ (Request for Quotation) and a Data Pack allocated to the Programmes Bid Department Project Manager who must aim to solicit Contractual Documents and then manage the set-up of the Manufacturing Control Documents.

These activities were modelled in this way because the dual path through this production process minimizes information handling risk for external work, but fast-tracks internal work tha is undertaken with lower perceived risk. In a similar fashion, other descriptive sentences tha explain the process can be read, such as the

```txt
- Trial MRP run allocates work to the Operations Department. The Operations Department ensures the first MRP run and continues to complete the manufactured Assembled Units.
```

If the model became overloaded with description, it could be presented scene-by-scene in the notion of a storyboard (described above), along with its annotated critical success factors fo information handling (methodological steps 3 and 4).

By adhering to the basic PrOH model template, a modeller can then develop further application specific modelling guidelines, such as grouping alike resources (e.g. Customers: Internal and External, and Manufacturing Control Documents: MMR and MRP) and colour bubbles to further differentiate the resource type. Colouring or patterning links can also highlight different sentence descriptions that explain the logic of the non-core activi ties, for example (reading along the foot of Figure 2) the Assembled Units require action to be taken by the Programmes (Bid) Department Project Manager who must declare a Completed Order to inform the SBU Management Team (shown in dotted line) simultaneously to the Assembled Units being delivered to the respective End Customer.

Another rule is having alternative human resource (black bubbles) and non-human resource such as information (white bubbles) in a description; this forces the modeller to think in terms of input–output, internal customers and suppliers and to always assign responsibility for activities. This discipline can also be used to give an indication of temporality: the past tense of verbs can be used to indicate what has been, the present tense what currently is and the future tense of verbs for what will be. Simply by using normal language and little codification, the focus of the process logic can be shown based upon the structure of the PrOH Logic Table.

Any number of models based on the PrOH model template can be sequentially linked together within any one particular holarchy pitch. For example, the model previous to the SBU must manages delivery of the Assembled Units in Figure 2 would be the Customer Requirement Definition Process which has the output Potential Order Intake that is also the input to the model shown. Similarly, the output of Figure 2, Assembled Units is the input to the next model, Customer Installation.

## Building a set of PrOH models: a holarchy

Figure 2 is a single PrOH model of a strategic business process. Models built on the PrOH model template can be built into a non-reductionistic and non-aggregational set of models – a holarchy (Valckenaers et al., 1997). PrOH responds to Van de Ven’s (1986) calls for guidelines for how a holarchy could practically be depicted. For instance, if more description about a specific process is required, then enriched models can be produced by pitching them at a lower level by using a 3-step technique. This 3-step technique is now explained using Figure 7 to represent a single PrOH model.

## Enriching models

Enrichment is achieved though the following steps, by defining:

![](/api/attachments/6R8GT9JT/fulltext/images/0f7993ca035a1d478e18825fb48874c5067c82f0a6328d6995347b4d3a339790.jpg)  
Figure 7. Representing a single PrOH model.

1 chains of entities (sentence descriptions contained in resource bubbles and on activity links) from the strategic level needing to be enriched. As more than one model will be produced, the new core process statements (including objectives) will be linked serially by their inputs, outputs and shared human resources. A name will also be given to each new model derived directly from the core process statement, such as; The SBU must manage delivery of the Assembled Units.

2 a new core business process for each newly pitched tactical (lower-level) model composed from any of the resource bubbles already defined in the strategic level model (again using a PrOH Logic Table to define activity dependencies). Do not introduce new resource bubbles into the core process descriptions as this would compromise ‘holarchiness’.

3 new resources (bubbles) and new relationships (links) to add to and widen the description of the new model. Go back to Step 1 for further enrichment to produce models at a lower level.

These steps help to avoid reductionism through structuring the modelling of the complexity without having to overly simplify this just to understand the situation. Enrichment enables important details (hidden properties) to be captured in lower level models rather than clouding higher level thinking. These steps are depicted in Figure 8.

To demonstrate the enrichment technique (depicted in Figure 8), the model in Figure 2 is used. Step 1 could define new lower level models about order intake, set-up and planning, manufacture and order completion activities.

Step 2 defines the new core process statement (and objective) for the tactical level mode about potential order intake. Developing this anew here using the knowledge represented by Figure 2, its definition might be: External Customers will supply RFQ and Data Pack which becomes the responsibility of the Programmes Bid Department Project Manager who must aim to solicit Contractual Documents. Furthermore, for the tactical model about set-up and planning the core process might be: the Programmes Bid Department Project Manager is allocated the solicited

![](/api/attachments/6R8GT9JT/fulltext/images/da743257a16e6bedcbddf896a9a5a742f88481f5b5e6ffc4a0f334085c6db6ff.jpg)  
Figure 8. Enriching to build a modelling holarchy.

Contractual Documents. The Programmes Bid Department Project Manager then manages set up of the Manufacturing Control Documents (MMR and trial MRP) which are required by the Operations Department. In a similar manner, the core process for the tactical model about manufacturing could be: the Programmes Bid Department Project Manager produced the Manufacturing Control Documents (MMR and trial MRP) which were required by the Operations Department. The Operations Department has the responsibility to ensure the First MRP run and continue to complete the Assembled Units which requires action to be taken by the Project Manager. Finally, the tactical model about order completion could have the core process statement: the Operations Department had the responsibility to ensure the first MRP run and continues to complete the Assembled Units which requires action to be taken by the Project Manager. The Project Manager must then declare a Completed Order required by the SBU Management Team. In this step, the selected resources (bubbles) used in either core or wider descriptions of the strategic level model have been raised in relative significance by making them all part of core process descriptions of tactical models. Text on links are also reinterpreted to better reflect the new relationships that now exist around the new core business process statements. Again, all new core business process statements are constructed by adapting the same PrOH model template (given in Figure 6) to specific processes applying the validation questions above.

Critical Success Factors - Tactics for Handling Manufacturing Information:

1. The volume of missed planning reports needs to be reduced

2. The ‘Spares’ and ‘repairs’ cells is needed to deal with low risk manufacturing independently from mainstream operations to increase efficiency

![](/api/attachments/6R8GT9JT/fulltext/images/bacea7a2f81a8c2e45e053229c06af5b60c0079dbee99a73b4e71a30b6a1775d.jpg)

3. Manufacturing problems can be reduced by addressing obsolescence and improving the management of changing customer requirements

4. The number of retrospectively refits given to new kits should be reduced

5. The control of build standards using engineering change requests (ECR’s) must have better IS support.

Figure 9. Tactical level model – scene 2 from a 7 scene storyboarded PrOH model – operations dept has the responsibility to deliver the assembled units.

To show how Methodological Step 3 can further widen the new core process description, the tactical Operations Dept has the responsibility to deliver the Assembled Units model (in Figure 9) is selected as an example. This has been produced through enrichment from its higher level model shown in Figure 2.

In Figure 9, the new core business process description has been refreshed to show the new tactical pitch of the model. For example, the resource bubble First MRP Run (from bottom-right of Figure 2) has now been widened in Figure 9 to include Purchasing Demands and Missed Planning Reports. The Operations Department from Figure 2 is also explained more fully in Figure 9. These embellishments match with the granularity of new wider descriptions in Figure 9 such as Purchasing Demands are sent to the Purchasing Department. The Purchasing Department raises Orders that are sent to the Suppliers.

In PrOH modelling terms, these new wider descriptions help to uncover the hidden properties of the process. Figure 9 is the second of seven storyboarded scenes based on the complete Operations Dept has the responsibility to deliver the Assembled Units model. The first scene (according to PrOH convention) just gives the core business process statement, while further scenes incrementally add wider descriptions until the full model is shown. The PrOH modelling methodology allows so much description (through enrichment and widening) that it is often useful to serialize its delivery by storyboarding.

The re-contextualized core process statement for Figure 9 would read as the, Set-up and Planning Phase was managed by the Project Manager. The Project Manager was responsible for the First MRP Run (Purchasing Demands and Missed Planning Reports) required by the Operations Department (Team Leader, Shop Floor Operatives, Production Engineer, and Materials Planning Manager). The Operations Department has responsibility to deliver the Assembled Units (with completed Route Cards) to the Quality Manager. The Quality Manager will then manage the Order Completion Phase. The temporal nature of the language is demonstrated here to show what has happened, what is happening and what should happen. Storyboarding allows critical success factors (Rockart, 1979) to be highlighted at suitable scenes of the process. Figure 9 shows five critical success factors about production IS considered germane to this particular scene of the model, these are explained more fully in the Discussion section.

An important point when enriching is that all the resource bubbles used in the new core process descriptions of an immediate lower level model are selected from those that already exist in the higher level model; this helps maintain ‘holarchiness’. New resource bubbles can only be included in the wider activity descriptions. Enrichment can be used to produce as many levels of modelling as required, however, experience shows that three levels should be parsimonious.

## Abstracting models

In addition to building a holarchy of models in a top-down enrichment manner, PrOH facilitates bottom-up construction (Sheard & Kakadabse, 2004) by applying the same 3-step technique in reverse, called abstraction. It is achieved by:

1 selecting all the resources (bubbles) from all the core process statements from all the models at the same lower pitch (removing duplications).

2 forming a new higher level core process statement using a combination of the extracted resources as well as new ones more relevant to the new models of higher pitch.

3 adding new wider relevant resources and activity descriptions to contextualize the new core process description. All extracted resources from all lower-level core process statements are used within the new model of higher pitch.

The abstraction technique is shown in Figure 10 by using the PrOH model as represented in Figure 7. Abstraction enables important details (emergent properties) to be captured in highe level models rather than confusing lower level thinking.

When abstracting, new resources and relationships that are salient to the new higher pitch are included in the core process statement; this preserves ‘holarchiness’. Fundamentally, a new model has then been created using issues and resources more relevant to the re-pitched model. For example, Figure 2 introduced the SBU Management Team into the core process statement and Corporate Management and Corporate Policy into the wider descriptions, as these are relevant at a more highly pitched level.

![](/api/attachments/6R8GT9JT/fulltext/images/f2b0d5ffc2f05ae70e16877c000ccd13e259c72b035b8d9ceff2195f004d4e17.jpg)  
Figure 10. Abstracting to build a modelling holarchy.

## RETHINKING THE PURPOSE OF AN IS

Through producing 3 levels of PrOH models for MES, several IS and production process conflicts were highlighted, primarily because of discord between the different levels of knowledge and thinking within MES. For instance, using Figure 2 (the strategic level model) and the numbered points 1–5 in Figure 9 (the tactical level model) an enriched discussion is now given:

1 the SBU management team’s primary concerns were to get assembled units delivered to the end customer. Additionally, they had to interface with the parent company and adhere to their strategic goals and working practices, meet profit, order intake and turnover targets as well as constantly improve their performance (see Figure 2). This allowed them limited time to understand the complex issues surrounding the production process and its IS. However, a newly installed MRP system had been imposed by the management team to try to meet the demanding targets of the parent company. At a tactical level, this was a source of much acrimony. Figure 9 refers to core process statements reflecting the same strategic intent of the management team, but much of the supporting activity description is about doing extra activities in order to deal with the poor match between the imposed MRP IS and the process that it is supposed to support. In other words, the manufacturing process was increasing in complexity and becoming increasingly demanding for employees’ time in order to make the new IS work. Obviously, this is the opposite of the desired impact. For instance, in Figure 9, there is a chain of activities described as the Project Manager was responsible for the First MRP run. The Missed Planning Reports are sent to the Operations Department. The Operations Department sort out any Planning Problems (e.g. estimating queries, test specification queries, modifications or DSIs (Design Standard Instructions) with the help of the. If the MRP system had been well matched to the production process, there would have not been any missed items in the first place and therefore, no missed planning reports. This demonstrates the extra work and problems that the installation of the new MRP IS caused. The rectification of these problems often involved consulting the customer and amending contractual documents in the form of Engineering Change Requests.

2 the Operations Department came up with a new tactical process for dealing with low risk changes because the official process had become too time-consuming and too complex. Such low risk changes were mainly for customers that were other SBUs of the same parent company. As a somewhat controversial solution, this had to be reported to a higher level in the organization and so summarized in the higher strategic level model (Figure 2).

3 the new MRP IS had no links to other legacy systems. For instance, the MRP IS and the engineering drawing database were separate, meaning that obsolete components could only be sorted out manually. The MRP Manager had to keep a stand-alone spreadsheet with these cross references on. The Management Team were not concerned with this detailed level of problem. Without a complete Bill of Materials, the MRP would not run and production could not begin. Often ‘dummy numbers’ were used as a ‘work around’ to keep production going despite having a new MRP IS.

4 the new MRP IS automatically defaulted to the latest build standard for each unit. As the MES manufacturing plant performed many refits for equipment that had been in service for decades, often it was the case that older build standards should have been used. This was another problem requiring manual reworking by tactical planners in the Operations Departmen that the strategic management team were blind to.

5 the changing of build standards (i.e. upgrading an old piece of kit to a newer version) was not supported by the new MRP IS. This was troublesome as much of the manufacturing unit’s turnover was this type of work. Again, this was not visible by the Management Team.

These five issues are found from just one scene of one model by comparing it to the next level up of modelling. In all, the exercise produced 15 PrOH models with an average of 5 scenes in each, which together raised hundreds of well-contextualized salient issues. The project showed a mismatch between the MRP IS imposed on the manufacturing unit and the type of processes operated (i.e. low volume. high variety). The MRP system would have been better suited to a mass production environment (i.e. high volume and low variation). The parent company took some radical restructuring as a result of these results; the modelling results were regarded as highly informative and demonstrated some very politically sensitive issues by presenting a meaningful context for different people at different organizational levels.

## SUMMARY

Starting from the basic tenants of SSM, this paper has offered a new methodology to help modellers to analyse business processes with IS rather than only defining the IS. From SSM, PrOH retains the critical features of:

1 the philosophical approach to modelling;

2 using systems models to build a defensible representation of a situation and not necessarily to faithfully and exhaustively recreate it;

3 using models to stimulate debate and select ‘feasible and desirable changes’; and

4 the realization that the performance of a complex human activity system (e.g. a production process and its supporting IS) is not able to be optimized in the same way as a physica system, but is only capable of becoming better through improved understanding of it.

However, the gap in SSM (that PrOH addresses) is that it does not explicitly explain how a model of a sub-system relates to a higher system of which it is part of and vice versa. While this may be sufficient for defining general problems, it is insufficient when talking about business processes as managers seek to ensure that day-to-day operations are concordant with strategic vision (Mintzberg & Quinn, 1991). To show this in a set of models requires inheritance between levels; as in harder systems methodologies. However, harder systems methodologies are also not entirely appropriate because of their over reliance on mechanistic hierarchical decomposition. In response to this dilemma, the PrOH Methodology was developed. In a spectrum of approaches with SSM at the softer end, and approaches such as IDEF0 and Data Flow Diagrams at the harder end; PrOH modelling is positioned between these but towards the softer end.

The principles of PrOH modelling methodology include: minimal codification; maximum utilization of normal language; graphical representation of processes; and a reversible 3-step technique to build a holarchy rather than a hierarchy. PrOH uses abstraction as the process o maintaining holonic descriptions when going from lower level models to higher level models. In reverse, it uses enrichment as the process of maintaining holonic descriptions when going from a higher level model to lower level models. This is possible because models are built from inter-linking sentence descriptions that can be re-interpreted, re-related and re-contextualized for different pitches. This enables individual holon models to be built into a set of models known as a holarchy.

This project delivered the “double challenge” (Avison et al., 2001a) of action research by delivering (1) the industrial requirement to facilitate discourse between levels of managemen about production processes and their supporting IS; and (2) the academic theoretical requirement which was a new hybrid technique which consisted of a complete holarchy of models to describe the business processes (Clegg, 1999). All the models were storyboarded and pre sented to directors of the collaborating company. The directors agreed this had been a revealing exercise that had effectively dealt with some long standing complex issues. This is in accordance with Baskerville’s (1999, p. 12) view on action research when he points out that, ‘. . . a newly invented technique is impossible without intervening in some way to inject the new technique into the practitioner environment’.

Future research called for in this area plans to compare the PrOH modelling with othe systems thinking techniques to test its efficacy. Training courses for higher education students and practitioners are currently being developed to transfer the methodology to others.

## ACKNOWLEDGEMENTS

The primary author gratefully acknowledges the action research collaboration from MES; for providing time, data and validating theoretical debate. Also to the EPSRC (grant reference GR/K24567) for supporting this action research.

## REFERENCES

Ackermann, F. (1996) Participants perception on the role of facilitators using GDSSs. Group Decision and Negotiation, 5, 93–112.

Ackermann E & Eden C (1996) Stakeholders matter how can we identify and manage them? In: Proceedings of Group Decision and Negotiation. La Rochelle, France Delft: Technische, Ackermann, F. & de Vreede, G.-J. (eds), pp. 225–226. Bestuurskunde, Delft University of Technology, The Netherlands.

Al-Kalifa, A. (2000) The design of an export process from Roval Ordnance (UK) to the Bahrain Defence Force. MPhil Dissertation, De Montfort University, Leicester, UK.

Argyis, C. & Schon, D. (1978) Organisational Learning: A Theory of Action Perspective. Addison Wesley, Reading, MA, USA.

Avison, D. Bakerville, R. & Myers, M. (2001a) Controlling action research projects. Information Technology and People, 14, 28–45.

Avison, D., Fitzgerald, G. & Powell, P. (2001b) Reflections on information systems practice, education and research: 10 vears of the Information Systems Journal. Information Systems Journal, 11, 3–22.

Avison, D.E., Wood-Harper, A.T., Vidgen, R.T. & Wood, J.R.G. (1998) A further exploration into information

systems development: the evolution of Multiview2. Information Technology and People, 11, 124– 139.

Baskerville, R. & Wood-Harper, A.T. (1998) Diversity in information systems action research methods. Euro pean Journal of Information Systems, 7, 90–107.

Baskerville, R.L. (1999) Investigating information systems with action research. Communications of the Associa tion for Information Systems. 2. Article 19. [WWW docu ment]. URL http://cais.aisnet.org/articles/default.asp? vol=2&art=19

Beer, S. (1985) Diagnosing the Systems for Organisations. Wiley, Chichester, UK.

Boardman, J.T. (1994) A process model for unifying systems engineering and project management. Engi neering Management Journal, 4, 25–35.

Boardman, J.T. & Cole, A.J. (1996) Integrated process improvement in design and manufacturing using a systems approach. IEE Proceedings – Control Theory and Application, 143, 171–185.

Bodker, S. (1996) Creating conditions for participation: conflicts and resources in systems development. Human–Computer Interaction, 11, 215–236.

Checkland, P.B. (1996) Systems Thinking, Systems Practice. Wiley, Chichester, UK.

Checkland, P.B. (1999) Systems Thinking, Systems Practice: Includes a 30 Year Retrospective. Wiley, Chichester, UK.

Checkland, P.B. & Poulter, J. (2006) Learning for Action: A Short Definitive Account of Soft Systems Methodology and its Use for Practitioner, Teachers, and Students. Wiley, Chichester, UK.

Checkland, P.B. & Scholes, J. (1996) Soft Systems Meth odology in Action. Wiley, Chichester, UK.

Clegg, B.T. (1999) A systems approach to re-engineering business processes towards concurrent engineering principles. PhD Thesis, De Montfort University, Leicester, UK.

Clegg, B.T. & Boardman, J.T. (1996) Process integration and improvement using systemic diagrams and a human-centred approach. Concurrent Engineering: Research and Applications, 4, 119–136.

Clegg, B.T. & Boardman, J.T. (1997) Systemic analysis of concurrent engineering practice. In: IEE Internationa Conference ‘Factory 2000’, Gregory, M. (ed.), pp. 464– 470. Cambridge University, Cambridge, UK. IEE publication No 435 2-4

Cole, A.J. (1997) An agent-centred method for systemic improvement of business processes. PhD Thesis, Portsmouth University, Portsmouth, UK.

Cole, A.J. & Boardman, J.T. (1995) Modelling product development processes using a soft systems methodology. 1st World Conference on Integrated Design and Process Technologies, Austin, TX

Conklin, J. (2005) Dialogue Mapping: Building Shared Understanding of Wicked Problems. John Wiley & Sons, Chichester, UK.

Davidson, E.J. (1999) Joint application design ( JAD) in practice. Journal of Systems and Software, 45, 215– 223.

Davison, R.M., Martinsons, M.G. & Kock, N. (2004) Principles of canonical action research. Information Systems Journal, 14, 65–86.

Deming, W.E. (1986) Out of the Crises. MIT Centre for Advanced Engineering Study, Cambridge, MA, USA.

Eden, C. (1988) Cognitive mapping. European Journal of Operational Research, 36, 1–13.

Eden, C. (1995) Using cognitive mapping for strategic options development and analysis (SODA). In: Rationa Analysis for a Problematic World, Rosenhead, J. (ed.), pp. 21–42. Wiley, Chichester, UK.

Eden, C. & Ackermann, F. (1998) Making Strategy: The Journey of Strategic Management. Sage Publications, London, UK.

Fitzgerald, B. (1996) Formalised systems developmen methodologies: a critical perspective. Information Systems Journal, 6, 3–23.

Fitzgerald, B. (1997) The use of systems developmen methodologies in practice: a field study. Information Systems Journal, 7, 201–212.

Fitzgerald, B. (2000) Systems development methodolo gies; the problem of tenses. Information Technology and People, 13, 174–185.

Fitzgerald, B. & Howcroft, D. (1998) Towards dissolution o the IS debate: from polarisation to polarity. Journal of Information Technology, 13, 313–326.

Flood, R.L. & Jackson, M.C. (1991) Creative Problem Solving: Total Systems Intervention. Wiley, Chichester, UK.

Gardiner, G.S. & Gregory, M.J. (1996) An audit based approach to the analysis, redesign and continuing assessment of a new product introduction system. Integrated Manufacturing Systems, 7, 52–59.

Grant, D. & Ngwenyama, O. (2003) A report on the use of action research to evaluate a manufacturing systems development methodology in a company. Information Systems Journal. 13. 21–35

Greasley, A. (2004) Simulation Modelling for Business. Ashgate Press, London, UK

IEEE. (1998) IEEE Standard for Functional Modelling Language – Syntax and Semantics for IDEF0. IEEE Computer Society, Washington, DC, USA.

Iverson, J.H. & Mathiassen, L. (2004) Managing risk in software process improvement: an action research approach. MIS Quarterly, 28, 395–433.

Jackson, M.C. & Keys, P. (1984) Towards a system o system methodologies. Journal of Operations Research 35, 473–486.

Johnson, G. & Scholes, K. (2002) Exploring Corporate Strategy, 6th edn. FT Prentice Hall, Harlow, UK.

Johnson, P. & Johnson, G. (2002) Facilitating group cog nitive mapping of core competencies. In: Mapping Strategic Knowledge, Huff, A.S. & Jenkins, M. (eds), pp. 220–236. Sage, London, UK.

Juran, J.M. (1987) Juran on Planning for Quality. Mac millan Free Press, New York. NY. USA

Keys, P. (2006) On becoming expert in the use of problem structuring methods. Journal of the Operational Research Society, 57, 822–829.

Koestler, A. (1967) The Ghost in the Machine. Hutchinson, London, UK.

Mansell, G. (1991) Action research in information systems development. Journal of Information Systems Develop ment, 1, 29–30.

Mathiassen, L. & Purao, S. (2002) Educating reflective systems developers. Information Systems Journal, 12, 81–102.

Melão, N. & Pidd, M. (2000) A conceptual framework for understanding business process and business process modelling. Information Systems Journal, 10, 105–130.

Mingers, J. & Gill, A. (1997) Multi-methodology: Theory and Practice of Combining Management Science Methodologies. John Wiley & Sons, Chichester, UK.

Mintzberg, H. & Quinn, J.B. (1991) The Strategy Process Concepts, Contexts and Cases, 2nd edn. Prentice Hall, Harlow, UK.

Mitroff, I. & Linstone, H. (1993) The Unbounded Mind, Breaking Chains of Traditional Business Thinking. Oxford University Press, New York, NY, USA.

Morecroft, J. (2004) Mental models and learning in systems dynamics practice. In: Systems Modelling: Theory and Practice, Pidd, M. (ed.), pp. 101–126. Wiley, Chichester, UK.

Morrill, N. (2007) Are the benefits of PSMs being sold sufficiently? Practitioner view on the present and future of PSMs. Journal of the Operational Research Society, 58, 533–549.

Nookabadi, A.S. & Middle, J.E. (1996) A generic IDEF0 model of quality assurance information systems for design-to-order manufacturing environment. IEEE Transactions on Components, Packaging and Manufacturing Technology: Part C, 19, 78–84.

Pettigrew, A.M. (1990) Longitudinal field research on change theory and practice. Organisational Science, 1, 267–292.

Pidd, M. (1996) Tools for Thinking: Modelling in Management Science, John Wiley & Sons, Chichester, UK

Pidd, M. (2004) Systems Modelling: Theory and Practice. John Wiley & Sons, Chichester, UK.

Ramsey, D.A., Clegg, B.T. & Cole, A.J., (1995) Developing learning frameworks using soft systems theory. In: 3rd International Workshop on Managerial and Organisational Cognition, pp. 12–18, Glasgow, UK

Robinson, S. (2003) Simulation: The Practice of Model Development and Use. John Wiley and Sons, Chichester, UK.

Rockart, J.F. (1979) Chief executives define their own data needs. Harvard Business Review, 57, 81–93.

Rosenhead, J. (1989) Rational Analysis for a Problematic World. John Wiley & Sons, Chichester, UK.

Rosenhead, J. & Mingers, J. (2001) Rational Analysis for a Problematic World Revisited. John Wiley & Sons, Chichester. UK.

Senge, P. (1990) The Fifth Discipline. Doubleday, New York, NY, USA.

Shaw, D. & Edwards, J.S. (2005) Building user commit ment to knowledge management strategy. Information & Management, 4, 977–988.

Sheard, A.G. & Kakadabse, A.P. (2004) A process per spective on leadership and team development. Journa of Management Development, 21, 7–106.

Sherman, D.G., Cole, A.J. & Boardman, J.T. (1996) Assist ing cultural reform in a projects-based company using systemigrams. International Journal of Project Manage ment, 14, 23–30.

Simon, H.A. (1976) From substantive to procedural ratio nality. In: Method and Appraisals in Economics, Latsis, S.J. (ed.), pp. 424–443. Cambridge University Press, Cambridge, UK.

Susman, G.L. & Everard, R.D. (1978) An assessment o the scientific merits of action research. Administrativ Science Quarterly, 23, 582–603.

Ulleru, M., Brennan, R.W. & Walker, S.S. (2002) The holonic enterprise: a model for internet-enabled globa manufacturing supply chain and workflow management. Integrated Manufacturing Systems, 13, 538–550.

Valacich, J.S., George, J.F. & Hoffer, J.A. (2006) Essen tials of Systems Analysis and Design, 3rd edn. Prentice Hall, Upper Saddle River, NJ, USA.

Valckenaers, P., van Brussel, H., Bongaerts, L. & Wyns, J. (1997) Holonic manufacturing systems. Integrated Computer-Aided Engineering, 4, 191–201.

Van de Ven, A.H. (1986) Central problems in the manage ment of innovation. Management Science, 32, 590–607.

Wastell, D.G. (1996) The fetish of technique: methodology as a social defence. Information Systems Journal, 6 25–40.

Webster, J. & Watson, R.T. (2002) Analysing the past to prepare for the future: writing a literature review. MIS Quarterley, 26, 13–23.

Westcombe, M., Franco, L.A. & Shaw, D. (2006) New directions for PSMs – a grass-roots revolution? Journal of the Operational Research Society, 57, 776–779.

Wilson, B. (1990) Systems: Concepts, Methodologies and Applications, 2nd edn. John Wiley & Sons, Chichester, UK.

## Biographies

Ben Clegg has a degree in Management Science and a diploma in Industrial Studies from Loughborough Univer sity. Simultaneously, he completed a diploma in Strategic

Marketing from the Chartered Institute of Marketing and a sponsored business studentship with GEC. He has worked as a project manager for several years in the capital goods sector. He has a PhD from De Montfort University in Systems Engineering funded by the EPSRC in conjunction with Rolls-Royce Aerospace, BAE Systems and their respective suppliers. He spent a year (2000–2001) as a Visiting Scholar at Stanford University’s Center for Integrated Facilities Engineering (USA) continuing research into business simulation tools, organizational theory, and systems thinking, as well as working for a university spinout company. He is a Fellow of the Higher Education Academy, a Chartered Engineer, and a Member of the Institute of Engineering and Technology. He is a reviewer for many international journals, publishers and the EPRSC. Ben joined Aston Business School in 2003 to teach in and research into improving operations management; he also consults and trains widely in a variety of companies in the area of business process modelling, improvement and simulation.

Duncan Shaw is a Senior Lecturer in Aston Business School, Birmingham, UK. He also has a BA and a PhD in Management Science from Strathclyde University. His research interests include the application of systems thinking methodologies, problem structuring and using operational research models to support effective decision-making. He works extensively with public and private companies, large and small, in a range o research and consulting activities. He has used systems thinking to support groups on a variety of topics including knowledge management, strategic planning, implement ing strategy and has recently developed a systems think ing methodology for the management of radioactive waste.

APPENDIX: THE PROH LOGIC TABLE FOR FIGURE 2.

<table><tr><td>Pervious key humanresource and activity</td><td>Input</td><td>Key human resource</td><td>Performs an activity</td><td>Output</td><td>Next key humanresource and activity</td></tr><tr><td>Holon input from environment: customer (internal customer), (external customer) supply potential order intake (works requisitions), (RFQ and data packs)</td><td>potential orders (works requisitions, RFQ and data pack)</td><td>SRL management team (materials, accounts, quality, operations, programmes, personnel, purchasing)</td><td>must manage delivery of the assembled units</td><td>assembled units</td><td>Holon output to environment: delivered to the respective end customer which should fulfil customer installation</td></tr><tr><td>Holon input from environment: customer (external customer) supplies potential order intake (RFQ and data pack)</td><td>potential order intake (RFQ and data pack)</td><td>project manager (programmes/bid dept)</td><td>must aim to solicit contractual documents</td><td>contractual documents</td><td>project manager (programmes/bid dept) can manage set-up of manufacturing control documents (MRP), (MMR)</td></tr><tr><td>project manager (programmes/bid dept) must aim to solicit contractual documents</td><td>contractual documents</td><td>project manager (programmes/bid dept)</td><td>can manage set-up of manufacturing control documents (MRP), (MMR)</td><td>manufacturing control documents (MRP trial run), (MMR)</td><td>operations department ensure the first MRP run for loading</td></tr><tr><td>Holon input from environment: customer (chelmsford BU) defines manufacturing requirement</td><td>potential orders intake (work requisitions)</td><td>project manager (spares cell), (repairs cell)</td><td>can directly manage set-up of manufacturing control documents (MRP trial run), (MMR)</td><td>manufacturing control documents (MRP trial run), (MMR)</td><td>operations department ensure the first MRP run for loading</td></tr><tr><td>project manager (programmes/bid dept) can manage set-up of manufacturing control documents (MRP), (MMR)</td><td>manufacturing control documents (MRP trial run), (MMR)</td><td>operations department</td><td>ensure the first MRP run for loading</td><td>first MRP run</td><td>operations department must complete manufacturing with assembled units</td></tr></table>

APPENDIX: cont.

<table><tr><td>Pervious key human resource and activity</td><td>Input</td><td>Key human resource</td><td>Performs an activity</td><td>Output</td><td>Next key human resource and activity</td></tr><tr><td>project manager (spares cell), (repairs cell) can directly manage set-up of manufacturing control documents (MRP trial run), (MMR)</td><td>manufacturing control documents (MRP trial run), (MMR)</td><td>operations department</td><td>ensure the first MRP run for loading</td><td>first MRP run</td><td>operations department must complete manufacturing with assembled units</td></tr><tr><td>operations department ensure the first MRP run for loading</td><td>first MRP run</td><td>operations department</td><td>must complete manufacturing with assembled units</td><td>assembled units</td><td>Holon output to environment: delivered to the respective end customer which should fulfil customer installation</td></tr><tr><td>operations department ensure the first MRP run for loading</td><td>first MRP run</td><td>operations department</td><td>must complete manufacturing with assembled units</td><td>assembled units</td><td>project manager (programmes/bid dept) takes action in order to close the order</td></tr><tr><td>operations department must complete manufacturing with assembled units</td><td>assembled units</td><td>project manager (programmes/bid dept)</td><td>takes action in order to close the order</td><td>completed orders</td><td>SBU management team (materials, accounts, quality, operations, programmes, personnel, purchasing) periodically review and produce status reports as directed by corporate policy</td></tr></table>

<table><tr><td>Holon input from environment: corporate management define corporate policy: policy (profit targets, strategic goals and working practices, turnover targets, constant change for improvement, order intake targets)</td><td>corporate policy (profit targets, strategic goals and working practices, turnover targets, constant change for improvement, order intake targets)</td><td>SBU management team (material, accounts, quality, operations, programmes, personnel, purchasing)</td><td>periodically review and produce status reports as directed by corporate policy</td><td>status reports (SBU pack)</td><td>Holon output to environment: corporate management kept informed of SBU progress</td></tr><tr><td>Holon input from environment: customer (internal BU), (External customer), supply potential order intake</td><td>potential orders (RFQ and data pack), (works requisitions)</td><td>SBU management team (materials, accounts, quality, operations, programmes, personnel, purchasing)</td><td>periodically review and produce status reports as directed by corporate policy</td><td>status reports (SBU pack)</td><td>Holon output to environment: corporate management kept informed of SBU progress</td></tr><tr><td>project manager (programmes/bid dept) takes action in order to close the order</td><td>completed orders</td><td>SBU management team (materials, accounts, quality, operations, programmes, personnel, purchasing)</td><td>periodically review and produce status reports as directed by corporate policy</td><td>status reports (SBU pack)</td><td>Holon output to environment: corporate management kept informed of SBU progress</td></tr></table>
