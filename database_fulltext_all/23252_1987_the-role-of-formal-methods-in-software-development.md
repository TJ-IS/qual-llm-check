---
otero_id: 23252
otero_key: "WBCBP3AC"
title: "The Role of Formal Methods in Software Development"
authors: "John McDermid"
year: "1987"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1987.25"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Role of Formal Methods in Software Development

John McDermid, Department of Computer Science, University of York

## 1. Introduction

## 1.1 Background

This paper summarizes the content of an invited presentation at a meeting on 'Formal Methods' organized by the Association for Information Technology. The presentation was made while the author was with Systems Designers plc (SD) and is based both on experience within SD and observations which the author has made concerning the use of formal methods in other organizations.

The term formal method is used widely but with differing meanings. In this paper the term is used to refer to methods with a sound basis in mathematics. The term structured method is used to refer to methods which are well defined but which do not have a sound basis in mathematics. Technically the most significant difference between the two classes of technique is that formal methods permit functionality to be specified precisely whereas structured methods allow only system structure to be specified precisely. The term informal method is used to describe those methods which have no formal basis, e.g. those using natural language system descriptions. Structured methods are used fairly widely in industry. Formal methods are used much less widely, but their use is on the increase.

The paper is based on the premise that formal methods are valuable to industry and that their introduction represents a significant step in the evolution of software development towards a true engineering discipline. However, formal methods are still a nascent discipline so there are a number of ways in which they need to develop before they can be widely applicable in industry. This paper sets out what the author sees as problem areas with formal methods given their current state of development, and thus the paper might appear negative with respect to formal methods. However, it is not intended to be so: it is simply easier to describe perceived problems than to present a eulogy with caveats!

## 1.2 Content of the paper

The main body of the paper starts with a brief description of a model of the software life cycle in order to define terms and to form a basis for the discussion of the perceived problems with existing formal methods. The bulk of the paper considers use of formal methods at different stages in the development process. Much of what is said would apply even if formal methods were not used. The author believes that this is appropriate: one weakness of formal methods today is that there is too much emphasis on the notation and too little on the methodological aspects of their use. The paper concludes by considering issues to do with tool support for formal methods, training and education.

The paper is broad in scope — consequently full technical arguments cannot be given in support of all the views presented within the space available. Further, the paper contains some subjective, and probably contentious, comments. Where possible arguments supporting the comments are presented. Some of the comments are based on value judgements, however, and for this and other reasons some of the comments are presented without supporting evidence. The author would welcome correspondence on any of the points covered, including those which are presented without justification.

The paper was written on the assumption that the primary audience would be professional software developers who are not au fait with formal methods. Consequently it contains definitions of some basic terms and gives references to a number of introductory papers. Some of the references are of a more advanced nature and these are identified in the References (section 15).

## 2. The software life cycle

## 2.1 Generic model

The software 'life cycle' is concerned with the development of software from initial concepts through delivery, use, and so-called maintenance.

![](/api/attachments/WBCBP3AC/fulltext/images/20ecbd287ab6698d95c667faaca8de2a4d0b4ea78cbcfec8f0799259a8e59027.jpg)  
Figure 1. Generic model of system life cycle

It is helpful to produce a generic model of the life cycle in order to have a basis for discussing different software development paradigms. Therefore we base our model on an abstract view of the activities carried out in software development and maintenance. The model is summarized in graphical form in Figure 1.

The first observation which we make is that, except for trivial systems, it is not possible to proceed directly from the initial concepts to executable software. Instead a number of intermediate system descriptions are produced, e.g. requirements specifications and design descriptions. We call these descriptions representations.

In general, development proceeds from concepts, through requirements etc., and one representation is developed by some intellectual or automated process from the preceding representation or representations. We refer to this process as a transformation although there is no implication that this is a purely automatable process.

In an ideal world the transformations would yield a sequence of representations, resulting in executable programs which satisfied their requirements, and the initial concepts. In practice errors and infelicities are discovered during the development and maintenance which cause iteration, i.e. repetition of the current transformation or rework of earlier representations. We use the term verification and validation (V&V) for the checking activities which can lead to iteration. We distinguish between verification and validation below.

It is worth pointing out that this model can encompass a number of different development paradigms. In a contractual model each representation would be completed before the next is started. With incremental enhancement all the representations (with the possible exception of the requirements) may be evolving simultaneously. Further 'maintenance' is encompassed in the model – we simply observe that maintenance involves iteration, updating various representations, once the system has been delivered.

The model can therefore be used as the basis for comparing different development methodologies. On a smaller scale it is helpful as a basis for discussing methods, as it identifies the three major components of a method, namely:

1. the notation used for the representation;

2. the rules for V&V;

3. the guidelines for the transformation.

We use the term ‘rules’ for V&V as there should be a precise correspondence between representations. However, we use the term ‘guidelines’ for transformations recognizing that this may be an intellectual process guided by general principles such as ‘information hiding’ (Parnas, 1972) and ‘delaying design commitment’ (Thimbleby, 1987).

More strictly we use the term 'verification' to mean answering the question 'Are we building it right?', which implies checking the correspondence between representations. Similarly we associate 'validation' with the question 'Are we building the right thing?', which implies determining whether the representations are still consistent with the initial concepts. Thus we should talk about verification rules and guidelines for validation.

![](/api/attachments/WBCBP3AC/fulltext/images/4164ccd5c850b5e6d6dfe402f81eeab1fefc32f378a7e56abcbb7999eb2516d7.jpg)  
Figure 2. 'Typical' development stages

It is interesting to note that many so-called methods are deficient in terms of the model presented. This is usually where the method defines a notation but no transformation guidelines, or rules for V&V. The absence of guidelines for transformation is a limitation of many current formal methods.

It is possible to produce many different instances of this generic model representing particular development methodologies. We give one (still fairly abstract) instance in the next section as a basis for the main part of our discussion. Management activities are not captured in the model as presented. This important topic is discussed in some detail by McDermid and Ripken (1984) together with a much fuller discussion of the above life cycle model.

## 2.2 Typical development stages

As indicated above there are many different approaches to software development adopted in industry. The following 'typical' model is intended to encapsulate the differing nature of the information being worked with at different stages in software development, without making commitment to any particular development methodology. It is hoped that the model encompasses most 'real developments'.

Five stages are identified in addition to the concepts stage (see Figure 2). The first two, requirements analysis and system specification, are in the domain of requirements, i.e. what the customer or user wants. The remaining three are in the design domain, i.e. how the system developer intends to satisfy the requirements. The reasons why we stress this distinction should become clear in section 5. In practice there may well be multiple stages of detailed design. We leave more detailed descriptions of the life cycle stages to the subsequent sections.

Many industrialists may think that the model incorporates activities which they do not undertake, or information which they do not use. It is asserted that this is either a misconception, or an omission, on their part! Some evidence for this view is presented below.

## 3. Requirements analysis

Requirements analysis is the first stage of the development process concerned with documenting the user's or customer's perceived needs by 'transformation' from the (by definition undocumented) initial concepts. The distinguishing characteristic of requirements analysis is that it is primarily an information gathering exercise which can only be validated, not verified.

The results of requirements analysis should describe both the system and the environment in which it operates. This is the case for two reasons:

1. the environment may change, impacting the functionality required of the system;

2. the boundary of the system is not known a priori.

It is hard to outline precisely that part of the environment which should be considered in requirements analysis, but it should cover at least those systems, individuals, etc. which interact directly with the system to be developed. The need to represent the environment means that requirements descriptions must be able to represent concurrency explicitly (because the system and processes in the environment operate concurrently).

In requirements analysis it must be possible to describe non-computable systems. This is both because users may ask for unrealizable systems and it is desirable to be able to record their requests exactly, and because it must be possible to record partial requirements, or requirements based on the assumption of infinite resources, which may arise as part of the information gathering process.

The results of requirements analysis are the primary basis for communication with the user and customer. For this reason it is desirable that the representation should be as precise as possible, e.g. formal. However, it is rare for users to be educated to understand the necessary formalisms. Consequently it seems that either formal techniques cannot be used at this stage or, if they are used, some interpretation of the formalism is required for communication with the customer. For example it would be possible to use techniques of animation, as opposed to specification execution, in validation of requirements.

Technically requirements analysis methods need to deal with causality, e.g. 'when this event occurs in the environment the system must perform the following actions', and other properties such as behaviour of the system under hardware failure conditions. Currently most requirements are specified informally. Structured methods such as CORE (Mullery, 1979) do address some of the technical problems alluded to above and are used in requirements analysis. There are few formal methods oriented towards requirements although the work of the Alvey FOREST project (Maibaum, Khosla and Jeremaes, 1986; Potts and Finkelstein, 1986) is noteworthy as it deals with issues such as formally representing causality and giving guidelines for requirements capture.

There are a number of research problems which have to be overcome before formal techniques can be used widely for requirements analysis. Perhaps the most crucial of these is the development of a notation (or notations) which is (are) rich enough to specify functional, causal and non-functional requirements but which can be presented to a user in an acceptable manner without (substantial) loss of precision.

## 4. System specification

System specification is still in the requirements domain, i.e. it is concerned with what the system should do, not how it does it, although this is not always an easy distinction to make in practice (see below). The primary distinction between this and the previous stage is that it describes only the system, not the environment, and it gives precise definitions of the system interfaces. In practice the system specification may be an enriched subset of the requirement specification and it should encompass both the system interfaces and its functionality.

In the contractual model of the life cycle the system specification would be the basis of the contract for the development team. The implicit requirement for precision suggests that the specifications produced should be formal. Further, the need to specify what, not how, suggests that it would be desirable to use algebraic specification techniques, that is, techniques where the behaviour of a system is specified implicitly by equations relating inputs to outputs (Zilles, 1974).

Algebraic specification techniques have been widely applied to small examples but there is little evidence, as yet, that they are suitable for specifying large systems. It is worth trying to amplify on the problems of using algebraic specifications by means of a small example. Imagine a system containing a database which we wish to update. If we model the database directly we can simply specify validity (the object to be updated exists, the type is correct, etc.). In an algebraic approach we would have to establish existence of an object by reasoning about the sequence of inputs to the system and determining whether the object had been created (successfully) since it was last deleted. This would make the specification obscure and cumbersome. In the author's experience, problems of this nature arise with the algebraic approach and such specifications tend to obfuscate rather than elucidate the problem being specified. Thus we have a conflict between the theoretical attractiveness of algebraic approaches and their apparent practical limitations.

As far as possible, concurrency should be specified implicitly, not explicitly, so that the system developers are free to choose what level of concurrency to use in implementing the system. This is certainly a contentious point and other authors, e.g. Zave (1982), would argue in favour of explicitly modelling concurrency. The primary argument in favour of the implicit approach is that it does not involve making premature design decisions (see also section 5).

There is another important issue related to system specification which can be illustrated by example. It is possible in an avionics system that some interfaces (e.g. to radar subsystems) would be specified very precisely during requirements, for example down to the level of the meanings of bits at the interface. However, interfaces to other devices, such as a head-up display, may be known in terms of the information to be displayed but not in terms of the data formats, etc. Defining these formats is a design exercise which should involve human factors experts. In producing a system specification the interface definition would have to be made precisely so it will inevitably contain design information. The extent to which the system specification will (implicitly) contain design information will depend on the nature of the system being built.

It might be thought that this ‘problem’ of mingling requirements and design can be avoided by using different development paradigms, for example prototyping. In fact this does not avoid the need to produce a complete system specification. Instead it simply (and possibly desirably) defers the point at which the specification is made precise until after validation of the proposed system specification by means of prototyping. It is desirable to avoid ‘premature design’ (see section 5) but it is clear that it is difficult to determine what is necessary design information and what is superfluous.

The system specification should be informally verified against the requirements. Since design information may have been added it is also desirable that it is validated against the initial concepts. It is possible that techniques of animation or specification execution (Coleman and Gallimore, 1987) can be used in validation although, as pointed out above, system specification may not initially contain enough information to allow execution of all aspects of the specification.

There seem to be two possible ways in which formal techniques can evolve to become more applicable for this stage in the software development process. First, algebraic techniques can be developed so that they are applicable to large-scale systems — this will almost inevitably involve schemes for modularizing specifications; second, it may be possible to find ways of applying the more operational techniques so that they do not unduly compromise design.

## 5. Architectural design

The architectural design describes the system interfaces, functionality and structure as we intend to implement it. The architecture is distinct from the previous stage in that it discusses system structure and how the functionality will be achieved as well as what functionality is required. The level of detail contained in such a specification will vary from project to project. However, it is not the level of detail which characterizes the architectural design, but the fact that this is the first description of the system from the developer's rather than the user's point of view.

Many different ways of producing formal specifications have been proposed. However, the concept of architecture outlined above seems to match closely the ideas of model-oriented specifications, i.e. producing a model of the system state and specifying the behaviour of operations by saying how they change the state. There are many other possible approaches to formally specifying architecture but space does not permit us to survey them here, nor to argue their relative merits and demerits.

A primary characteristic of the transformation from system specification to architecture is that it may not be structure preserving. In other words the structure of the design may have to be different from that of the requirement. This change in structure may be necessitated so that the system performs sufficiently quickly, or so that the customer can afford it. The author has been surprised to find that even experienced software designers can find it difficult to accept this point, so we will give a simple example by way of illustration.

Imagine a telephone exchange intended to handle 10,000 lines. The 'natural' way to specify this from the customer's point of view would be as 10,000 parallel processes each carrying out the appropriate functions for their respective lines. (In practice there would be additional functions for producing customers' bills, fault-finding, etc.) If the exchange were built with 10,000 processes then it would be prohibitively expensive. Instead exchanges are built with a smaller number of specialized processes each of which handles a part of the processing associated with handling each line. The number of processes is determined by a number of factors including the expected density of call set-up requests, and reliability of the processors to be used. Thus cost and the limitations of current hardware technology are a primary factor in determining the design. We can draw a number of points from this observation.

First, we have given non-functional reasons for the change in structure. In other words non-functional requirements such as performance, cost and reliability drive the design process. This is significant because formal specifications do not, in general, enable this non-functional information to be recorded.

Second, many formal methods support a concept known as refinement — see, for example, Jones (1986) — which enables us to define and verify the correctness of the relationships between two formal representations of the same system. However, the published refinement techniques are usually too restrictive to admit the sort of structural change identified above, although recent work in Oxford (He, Hoare and Sanders, 1986) is addressing this problem.

Third, we need quite a permissive interpretation of equivalence between the levels of representation. It must be possible to take into account non-determinism, asynchrony, etc. which would mean, inter alia, that the order of the outputs would not be determined entirely by the order of the inputs. The notion of behavioural equivalence introduced in algebraic specification — see, for example, Sanella and Tarlecki (1984) — admits at least some of the requisite laxity in the meaning of equivalence.

As will be apparent from the example above it is also necessary to be able to represent concurrency within the architectural design. The primary problem associated with applying formal methods at this stage in the life cycle is that there is no method, or notation, which encompasses all the requirements identified above. At present the would-be user of formal methods must choose the technique which best supports the characteristics which are most critical in his or her application area.

## 6. Detailed design

It is the author's view that detailed design should proceed from the architecture by the conventional process of (structure preserving) refinement. This is not a universally held view: indeed the phrase 'one man's design is another man's requirement' is often used in the software industry when discussing hierarchical specifications of systems. Given the interpretation of the relationship between requirements and design given above, this would mean that the structure of the design could be changed in each representation. In the author's opinion this is an unhealthy attitude from at least two points of view.

1. Technically it implies that the architect did not have a complete (adequate) understanding of the system. This is particularly critical if the proposed changes involve modifying the process structure and hence impacting timing, etc. possibly to the extent that the system no longer meets its (non-functional) requirements. Clearly problems with the architecture may be found in detailed design: these should be resolved by updating the architecture, not making low-level changes to the overall design.

2. Managerially it implies that the project is not under adequate control. For example modules common to several subsystems may have been identified for separate implementation, and the basis on which this decision was made could be invalidated by allowing changes at this level.

Thus even if the restructuring preserves sub-system interfaces it could have 'knock-on' effects on the rest of the project and invalidate project plans, project resourcing, etc.

This is a complex topic and there are other arguments in favour of (and against) the structure preserving view. We will not prolong the argument here but we do note two technical points related to the argument. First, the structure preserving view is consistent with (capable of being supported by) current refinement techniques — see, for example, Jones (1986). If this view is not accepted then we have the same requirements for refinement as for the transformation between system specification and architecture, so no more technical problems are introduced.

The classical refinement techniques apply for sequential systems. Some techniques for dealing with concurrent systems, e.g. CCS (Milner, 1980), support hierarchical decomposition of systems which is akin to refinement. So far as the author is aware, there is no satisfactory formalism for dealing with the simultaneous refinement of both the concurrent and sequential aspects of a system and this remains an active research area.

## 7. Implementation

There has been considerable work on formal treatment of the final stage of development, i.e. formally relating a program to a low-level specification. Techniques include the so-called 'constructive' approach (e.g. Backhouse, 1986) and program verification environments (e.g. Gypsy – Good, 1984). The constructive techniques are methods based on the idea of deriving the program from low-level specifications, and are intended to be applied manually. The verification environments are based on similar mathematical bases (Hoare, 1969) to the constructive techniques but typically are more concerned with giving automated assistance to proof of correspondence between a program and a specification. Techniques for formal implementation are most well developed for sequential programs, but some work has been carried out for concurrent programs. The techniques are expensive to use and most of their uses to date have been in highly critical systems where the cost of failure justified the expense of applying the techniques in development. A considerable improvement in productivity using these techniques will be necessary before they can become more widely used.

The majority of these techniques are suited to the development of sequential programs, or at least programs which terminate. However, many critical applications where the use of these formal verification techniques would be justified on economic grounds are continuously running programs, monitoring the state of some (physical) process and taking the necessary remedial actions if the process is becoming dangerous (for example, monitoring and controlling the flow of steel through a steel mill). Improvements in techniques for handling concurrency and continuously running programs will be necessary to handle this class of programs in a satisfactory manner.

Weaker forms of verification may be valuable under some circumstances. For example, tools such as Malpas (Bramson, 1984) can carry out various analyses on programs, and these can be used to validate or verify the program. Capabilities of the tools include analysing control and data flow for undesirable features and establishment of the information flow in the program so that it can be compared with the specification.

## 8. Representations

We have already discussed aspects of the notations used for the representations at each stage of the life cycle. There are, however, a number of issues which apply to all the representations which warrant discussion, although we will not elaborate on such well-understood topics as re-usability.

First, it is necessary to be able to modularize specifications in order to be able to divide specification and implementation tasks among the members of a development team. Z (Hayes, 1986) has a form of modularization known as 'the schema calculus'. This is analogous to the procedure in a programming language but, to the author's knowledge, no formal method supports modularity in the sense of Ada packages.\* This is a constraint on the application of formal methods.

Second, the different notations used throughout the life cycle need to relate to one another. This means that they should not be wantonly different in linguistic form and, more significantly, that they should be based on compatible models of the system. It is perhaps easiest to define compatibility by means of a counter-example! A representation based on synchronous communication by message passing would not, in general, be compatible with one based on asynchronous communication via shared store. This is not to say that the two representations could not describe the same system, but rather that there is a considerable conceptual change between the two representations which would impede understanding, especially of the way in which one representation was meant to implement the other. Note that this is weaker than saying that refinement should be structure preserving.

\* Ada is a registered trademark of the US DoD, Ada Joint Program Office.

Third, there is benefit to be gained from having languages tailored to particular application areas. This may be achieved either through the design of a special purpose language or by means of a 'library' used with a conventional formal specification language such as Z. The primary motivation behind this suggestion is the achievement of greater efficiency in the development of specifications (c.f. 4GLs).

Fourth, it is necessary to be able to specify non-functional requirements and facets of the design. This is not possible within current formalisms. For this and other reasons it seems desirable that multiple (related) notations should be used for each representation. This is analogous to other engineering disciplines where different notations are used to describe different aspects of the same artefacts, or different notations are used under different circumstances — high frequency and low frequency models of transistor behaviour, for example.

## 9. Transformations

As explained above, transformation is primarily an intellectual process driven by non-functional requirements as much as by the functional requirements for a system. Guidelines for the transformations are as important for formal methods as they are for structured methods, although currently this is an area where formal methods are weak.

Some transformations can be automated. The most obvious example is the compilation of statements in a high-level language into assembly or machine code. It is, however, possible to carry out transformations from higher-level specifications (Partsch and Steinbruggen, 1981) to produce executable programs. Formal methods are particularly amenable to transformation techniques because of the precise semantics of the notations used. It seems probable that these automated transformation tools will become more widely available in support of formal methods, although progress is likely to be slow as there are significant technical problems to be overcome in producing efficient and effective tools.

## 10. Verification and validation

Verification is concerned with demonstrating consistency and completeness within a representation, and that one representation bears the correct relationship to another. Validation is concerned with demonstrating that the representations are consistent with the initial system concepts.

The term formal verification is used to mean verification based on the concepts of mathematical proof. More strictly it means proofs where all the details of the mathematical argument are presented. In other words, the statement:

$$
(a + b) + c = (b + c) + a
$$

would not be accepted in a formal proof without explicit statement of the order of which rules of commutativity, etc. were applied to reduce the two halves of the equality to the same (textual) form. We can have extreme confidence in the correctness (with respect to the specification) of a formally verified system, but the cost of gaining this confidence is very high. Consequently formal verification tends to be used only where the cost of system failure is very high, as in safety critical systems. The successful use of formal verification is contingent on proper tool support (see below).

An alternative style of verification known as the rigorous approach (Jones, 1986) is entering use in industry. With the rigorous approach it is acceptable to present much less detailed proofs, or arguments, and 'obvious' truths (such as the equality above) will be accepted without any requirement to present an explicit argument. With the rigorous approach much of the benefit of formal proofs is gained at a much lower cost. It is probable that future, large-scale, software development projects will be based on the rigorous approach.

Verification of consistency requires us to demonstrate that there are no contradictions in a particular representation. Completeness is a more subtle concept. Ideally we would like completeness to mean that a representation covers every facet of the system. However, this implies perfect validation: hence it is not attainable. More practically we might seek to achieve 'analytical completeness' where all facets of those objects and operations specified were covered, but this prevents us from delaying design commitments and has a number of other adverse characteristics. We are reduced to saying that the concept of completeness is subjective!

The detailed rules for demonstrating proper correspondence between representations depends on the refinement technique employed. In general refinement will be concerned both with the data structures at two levels of representation and with the operations at two levels of representation. In general we are concerned that the lower-level (nearer to implementation) data structures are adequate for holding all the information which can be held by the higher-level data structures. Similarly we are concerned that the low-level operations satisfy the constraints placed on the high-level operations (with suitable interpretation of the meaning of the data structures). These concepts are set out for the refinement paradigm supported by VDM by Jones (1986).

As we explained above, validation can be carried out by a number of techniques including specification animation and execution. At least one system has been developed for executing a subset of a formal specification (Henderson, 1986). This may be used for both validation and rapid prototyping. A limitation of this sort of validation technique is that it does not enable us to validate negative properties, e.g. 'the system shall not deadlock', although the proof techniques described above can be used in this way. In practice much validation is in the form of (peer) review.

In V&V we are also concerned with quality. Thus a representation may satisfy the V&V rules to do with refinement, but be unsatisfactory from the quality point of view. From this and the above it should be clear that the verification and validation activities are partially automatable, and partially the subject of human judgement.

Finally, we recall that we expect to modify representations both during development and during maintenance. Most verification techniques tend to be 'monolithic', i.e. a change in a representation requires the whole V&V activity to be repeated. Considerable advantage would be gained from techniques which enabled re-verification to be carried out incrementally.

## 11. Metrics

Clearly it is desirable to be able to measure facets of a system under development and to measure and estimate productivity in order to be able to control a project. The requirement for metrics applies to all facets of software development, not just the use of formal methods. The development of metrics is quite a controversial topic and a number of elaborate theories have been produced only to be discredited. However, the lack of good metrics does not remove the requirement for metrics!

Particular needs are for complexity metrics for formal specifications and for productivity metrics. There is very little work in this area; one notable exception, however, is some recent work at the Polytechnic of the South Bank (Fenton and Whitty, 1986) on graph-theoretic measures of complexity.

Even if soundly based complexity measures cannot be produced it will be necessary for empirical measures to be developed in order that projects using formal methods can be planned and controlled.

## 12. Tool support

It has long been recognized that neither structured nor formal methods can be applied cost effectively in large-scale projects without adequate tool support. In line with our factorization of methods into three components we can divide tools into three classes:

1. clerical support;

2. verification support;

3. transformation support.

The availability of tools in each of these three classes varies considerably.

There are many formal notations for which syntax checking tools, and in some cases type checking tools, are available. Verification support essentially means tools for producing, or checking the validity of, formal proofs. Many 'stand alone' theorem provers have been produced and there is a more limited number of proof systems integrated with specification and programming tools — e.g. Gypsy (Good, 1984). There is a small number of experimental transformation tools in existence but, so far as the author is aware, only one transformation tool is commercially available (REFINE from Reasoning Systems Inc.).

There are substantial technical problems associated with producing verification and transformation tools. These include both theoretical problems in computer science, and pragmatic problems due to the computational complexity of some of the algorithms which have to be used in the tools. A discussion of these problems is outside the scope of this paper.

Clerical support tools are comparatively straightforward to design. It should be possible to produce clerical tools for a wide class of formal methods, and these tools should be adequate for supporting the use of formal notations in the rigorous approach to software development. However, there are still problems of finding appropriate 'modules' for formal specifications so that they can be broken down into manageable units and placed under configuration control. Thus the use of the methods is limited to comparatively small projects with currently available tools.

It should be clear that there are substantial problems to be overcome before adequate tool support can be provided to enable formal methods to be used widely in industry.

## 13. Training and education

While tool support for formal methods is important, the real stumbling blocks in introducing formal methods into industry are the lack of adequately trained staff and industry's lack of belief in the value of the techniques. Most undergraduate courses now teach the necessary mathematics underlying the formal methods, and many teach particular methods (e.g. VDM), but most of the practitioners in industry have not had the benefit of such an education. Consequently there is a need for training and continuing education in the mathematical basics of formal methods, and in particular methods.

There is a considerable amount of material that could usefully be taught, but it is possible to learn to use a particular formal method with comparatively little effort. For example the Programming Research Group at the University of Oxford teach a two-week course on Z, after which attendees are able to read Z specifications and most can write Z specifications given a little assistance or consultancy. Fluency in producing formal specifications is then dependent on further practice, but will typically be achieved within a few months.

There is some scepticism in the industry about the value of formal methods and, unfortunately, some of the limitations pointed out above may serve to mask the benefits of using the methods. This attitude can be changed but there are a number of prerequisites. First, some more major projects need to be carried out using formal methods and the benefits (or at least the practicality) of the methods demonstrated. Second, management level information on formal methods needs to be made available — this includes information on productivity, etc. alluded to above.

There is also a reluctance in the industry to adopt formal techniques, perhaps based on the view that software development is an 'art' or at any rate is not an engineering discipline. This is a cultural problem and it will not be solved merely by making available training courses on particular formal methods. It is hard to see how to change this view within the industry, although the fact that some companies are encouraging their employees to undertake continuing education programmes in basic computer science and software engineering is encouraging. It is to be hoped that this trend continues.

## 14. Conclusions

This paper is based on the premise that the introduction of formal methods will be of benefit to the software industry. Although the benefits of formal methods have not been discussed here, the author believes that they are part of the scientific and mathematical basis which will enable software development to be treated as a true engineering discipline. Perhaps the greatest pragmatic benefits of formal techniques are the precision, and hence the clarity, which they introduce in specifications, and in the communication within the development team, and potentially between the development team and the customer for a system. However, there are still limitations on the capabilities of formal methods.

This paper has given the author's personal view of the nature of the software development process, and the role of formal methods within that process. Further, it sets out perceived limitations of formal methods in terms of their role within that process. Some of these views are subjective and, presumably, contentious. The author would welcome correspondence on these issues.

Many of the perceived limitations are in the area of making the methods applicable for use in an industrial context by a team, rather than use by a small number of people in a research context. Particular problems discussed are modularizing formal specifications, and provision of adequate refinement techniques. Overcoming these problems requires both academic research work and development based on industrial experience.

Problems of education and training are at least as important as technical issues in the introduction of formal methods. Some progress can be made by training in particular methods but a wider education programme is needed before these methods can be used widely. The author strongly believes that these changes should, and will, come about as part of the evolution of software development to a true engineering discipline.

## 15. References

Backhouse, R. (1986) Program Construction and Verification. Prentice Hall International.

Bramson, B.D. (1984) Malvern's program analysers. RSRE Research Review.

Coleman, D. and Gallimore, R.M. (1987) Software Engineering Using Executable Specifications. Macmillan Computer Science Series.

Fenton, N.E. and Whitty, R.W. (1986) Axiomatic approach to software metrication through program decomposition. The Computer Journal, 29, 4.

Good, D. (1984) Mechanical proofs about computer programs. Report No. 41, Institute for Computing Science, The University of Texas at Austin.

Hayes, I. (ed.) (1986) Specification Case Studies. Prentice Hall International.

He, J., Hoare, C.A.R. and Sanders, J.W. (1986) Data Refinement Refined. Programming Research Group, University of Oxford.

Henderson, P. (1986) Functional programming, formal specification and rapid prototyping. Transactions on Software Engineering, 12, IEEE.

Hoare, C.A.R. (1969) An axiomatic basis for computer programming. CACM, 12, 10.

Jones, C.B. (1986) Systematic Software Development Using VDM. Prentice Hall International.

Maibaum, T.S.E., Khosla, S. and Jeremaes, P. (1986) A modal (action) logic for requirements specification. In Brown, P.J. and Barnes, D.J. (eds.) Software Engineering 86. Peter Peregrinus.

McDermid, J.A. and Ripken, K. (1984) Life Cycle Support in the Ada Environment. Cambridge University Press.

Milner, A.J.R.G. (1980) Calculus of communicating systems. In Goos, G. and Hartmanis, J. (eds.) Lecture Notes in Computer Science No. 92. Springer Verlag.

Mullery, G.P. (1979) CORE – a method for controlled requirements specification. In Proceedings of 4th International Conference on Software Engineering. IEEE Computer Society Press.

Parnas, D.L. (1972) On the criteria to be used in decomposing systems into modules. CACM, 15, 12.

Partsch, H. and Steinbruggen, R. (1981) A comprehensive survey of program transformation systems. Report No. 18108. Institut für Informatik, Technical University of Munich.

Potts, C.J. and Finkelstein, A. (1986) Structured common sense. In Brown, P.J. and Barnes, D.J. (eds.) Software Engineering 86. Peter Peregrinus.

Sanella, D. and Tarlecki, A. (1984) On Observational Equivalence and Algebraic Specification. Department of Computer Science, University of Edinburgh.

Thimbleby, H.W. (1987) Delaying commitment: a general design heuristic. (Forthcoming.)

Zave, P. (1982) An operational approach to requirements expression for embedded systems. Transactions on Software Engineering, 8, 3. IEEE.

Zilles, S. (1974) Algebraic specification of data types. Report No. 11, Project MAC, Massachusetts Institute of Technology.

## Biographical notes

John McDermid joined the Ministry of Defence as a student engineer in 1971, then went to Cambridge to read engineering and electrical sciences. On graduating in 1975 he joined RSRE undertaking research in fault-tolerant distributed computer systems, which included design and implementation of a fault-tolerant, packet switching LAN, and development of software fault recovery techniques. This latter work was submitted for an external Ph.D. at the University of Birmingham.

![](/api/attachments/WBCBP3AC/fulltext/images/df1a3571c2461132ea4f6b86cd9211099d1859d707149823d6c9354bda7468de.jpg)

In 1982 Dr McDermid joined Systems Designers plc and worked on a number of facets of software engineering including integrated project support environments, formal design methods and structured methods for requirements analysis. He also carried out work in computer security, particularly advising on the software engineering techniques to be used for producing highly secure systems.

In 1987 Dr McDermid took up a Professorship in the Department of Computer Science at the University of York where his primary research interests are formal and structured methods and high integrity systems.

Professor McDermid has been active in the IEEE promoting the cause of software engineering. He has served on numerous committees and working parties and is now an Honorary Editor of the joint IEEE/BCS Software Engineering Journal. He has published over 30 papers and articles, and has produced two books.

Address for correspondence: Department of Computer Science, University of York, Heslington, York YO1 5DD. (Tel. 0904 430000 ext. 5570 in the UK; +44 904 430000 ext. 5570 outside the UK).
