---
otero_id: 25923
otero_key: "NMUREM5B"
title: "Formal specification – an analytic tool for (management) information systems"
authors: "PA Swatman; PMC Swatman"
year: "1992"
journal: "Information Systems Journal"
doi: "10.1111/j.1365-2575.1992.tb00071.x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Formal specification — an analytic tool for (management) information systems

PA Swatman and PMC Swatman

Curtin University of Technology, Department of Computer Science, GPO Box U1987, Perth 6001, Australia

Abstract. There appears to be a general consensus within the information systems literature that formal specification of software systems is an inappropriate response to the perceived general failure of information systems to meet user requirements. Such views would seem to be based primarily on the difficulty of constructing formal specifications — and on the difficulty of understanding such specifications once constructed. Research into the applicability of formal methods has therefore tended to concentrate on the needs and the context of software developers specializing in critical and extremely complex software such as operating systems, transaction processing monitors, or nuclear reactor protection. More recently, however, formal methods have been applied successfully in more conventional and commercial areas, such as the development of a CASE tool, indicating that many of the perceived disadvantages of formal methods are merely myths.

This paper discusses the differing research directions of the information systems and software engineering disciplines and suggests that significant benefits may result from a synthesis of the two approaches. We further suggest that there is a serious danger that approaches which have been shown to have value in one of the two domains are automatically being ignored in the other as being 'irrelevant'. While each of the two areas ignores the contribution of the other, software systems will continue to be sub-optimal (in terms of relevance, as well as quality). We argue the relevance of formal specifications to the information systems discipline, illustrating the argument with a case study based within the IS domain.

Keywords: analysis, formal, information, specification, systems.

## INTRODUCTION

The term 'Software Crisis', initially coined in the mid-1960s, is a descriptor for the pervasive state of affairs in which computer software:

(a) frequently fails to meet user requirements,

(b) frequently crashes (and fails completely under certain circumstances),

(c) is excessively expensive (and difficult to cost),

(d) is difficult to alter (maintain, enhance),

(e) takes too long to build,

(f) is difficult to schedule and thus is often delivered late,

(g) is not portable (and tends not to be ported),

(h) uses resources (processing power, storage space) in a non-optimal manner (Booch, 1987; Schneider, 1987; Sommerville, 1989).

In this paper we examine perhaps the most important of the many approaches (for a review, see Swatman & Swatman, 1990) which have been taken in an attempt to contribute to the resolution of this crisis — the improvement of the requirements determination and specification processes.

Studies indicate that the cost of correcting system errors increases exponentially as the life cycle proceeds from phase to phase; and further, that up to 60% of system faults are due to specification errors, omissions or ambiguities (studies conducted by IBM and TRW, cited in Boehm, 1976 $^{1}$ ). Although there is general agreement on the importance of requirements definition, there are clearly two schools of thought on how best to attack the problem — one based in information systems and one in software engineering research.

This paper has the following structure:

(a) a description of the alternative research philosophies and their foci,

(b) an examination of the limitations of each approach taken in isolation; together with a suggested synthesized strategy,

(c) a case study drawn from the world of information systems which demonstrates the practical applicability of the strategy,

(d) in conclusion, a discussion of our experience of presenting this strategy to the professional information systems community and an overview of the co-operative research currently underway.

## SYSTEMS DEVELOPMENT PHILOSOPHIES

Within most academic institutions, research relevant to the development of computer-based systems is found in two quite separate academic areas. Typically, one of these areas is located within the business (commerce) faculty and may be called information systems, management information systems, business computing, or information (data) processing.

The other focus of teaching and research into the development of computer-based systems is most frequently found within the science or engineering faculty, where it is normally known as computer (computing) science.

These two academic disciplines view the systems development process from differing philosophical perspectives:

(a) the predominantly socio-organizational perspective — which we shall refer to as the 'information systems' perspective; and

(b) the predominantly scientific/engineering-based perspective — which we shall call the 'software engineering' perspective.

## Information Systems

A succinct and relevant definition of information systems poses some difficulties, due to the discipline's rapidly changing nature (which itself follows from the relative infancy of the discipline). There are, however, many definitions of information systems themselves and of information systems methodologies, some of which include a wider explanation of the discipline:

'The information systems designer . . . is concerned with the application of information technology in organisations and society and with the design, development and use of information systems which add effectively to their welfare and successful activity'. (Buckingham et al., 1987).

'The IS discipline provides the analytical framework and the methodology to analyze, design, implement and manage complex information/decision systems. An IS is defined as 'a set of personnel, computer hardware, software packages, computerprograms, data files, communication systems, decision models, organizational procedures and practices, so structured and assembled as to ensure data quality, transmission, processing and storage in accordance with a given performance criterion to assist decision-making'. An IS integrates systems analysis, statistics, management, management science, accounting, economics, finance, marketing, production, and computer and communications technology to accomplish these tasks'. (Nunamaker, 1981).

'An information systems methodology, in attempting to make effective use of information technology, will also attempt to make effective use of the techniques and tools available. But information systems are about balancing these technical specialisms with behavioural (people-oriented) specialisms'. (Avison & Fitzgerald, 1988)

'The mission of Information Systems Research is to study the effective design, delivery, use and impact of information technology in organizations and society'. (Keen, 1987)

The common theme within these various definitions, and the factor which most clearly distinguishes this philosophy from that of software engineering, is the emphasis on the human, organizational and societal issues associated with information systems.

## Software engineering

Software engineering, like information systems, is a young and rapidly changing discipline though it is, perhaps, easier to define:

'Software Engineering is the establishment and use of sound engineering principles and good management practice, and the evolution of applicable tools and methods, and their use as appropriate, in order to obtain — within known but adequate resource limitations — software that is of high quality in an explicitly defined sense'. (Macro & Buxton, 1987)

'Software Engineering is the disciplined utilization of a systematic, coherent set of principles, tools and techniques within a planned organizational framework, the objective of which is to achieve the on-schedule, cost-effective development of quality software for a diverse range of non-trivial applications and environments' (Ratcliff, 1987)

'Software Engineering is the management of expectations, computer technologies, people and their skills, time, cost, and other resources to create a product that meets the expectations of the client with a process that meets the expectations of the producer'. (Steward, 1987)

Mary Shaw of the Software Engineering Institute at Carnegie Mellon University offers the following definition 'Software Engineering is promoting the development of cost-effective solutions to practical problems of increasing scale (size, complexity) applying scientific knowledge in order to build things in the service of humanity' (cited in Bamberger, 1990)

Sommerville suggests that the common factors in the various definitions include:

(a) a concern with software systems built by teams rather by individuals (real-world systems as opposed to simple computer programs),

(b) the use of engineering principles,

(c) concern with both technical and non-technical aspects (Sommerville, 1989).

Jones adds: 'the recommended techniques draw from a foundation of Computer Science, Mathematics, Management Science, and Systems Science . . .' (Jones, 1990).

We shall define software engineering as:

The application of scientific, mathematical, engineering and managerial principles to the software development process.

It is worth noting that the context in which the eventual software system will exist is not specified in any of the above definitions. Software engineering is concerned with the development of software for both technical/scientific and information systems purposes. It is our view that software engineering is as important within information systems as it is within the computer science domain.

## Two research foci compared

Although both information systems and software engineering are concerned with the development of computerized information systems and, in particular, with requirements determination, we could conclude that:

(a) when the information systems community considers the process of requirements definition, it is primarily concerned with contextual analysis,

(b) when the software engineering community considers the process of requirements definition, it is primarily concerned to specify, completely and unambiguously, the artefact (that is the software system and supporting documentation and procedures) to be built.

An informal survey of well-known text books in the areas of both information systems development (Wilson, 1984; Eliason, 1990; Senn, 1990) and software engineering (Steward, 1987; Macro & Buxton, 1987; Sommerville, 1989; Jones, 1990; Macro, 1990), provides evidence of a general consensus on this categorization.

As the main thrust of our argument is concerned with synthesizing an approach to the development of systems which draws from both domains, it is interesting to compare the approach taken by Avison & Fikgerald (1988) from the information systems domain with that of Birrell & Ould (1985) from the software engineering domain, who review systems development methodologies from their respective viewpoints.

These two perspectives overlap significantly — for example both groups consider the structured techniques, Jackson's techniques and the data-oriented techniques to be appropriate methodologies for software development within their own domain — although there are significant differences.

1 Birrell & Ould suggest a model of the systems development process in which the first phase is called 'project inception'. This stage includes aspects such as market research, cost/benefit analysis, operations research and tender analysis and aims to produce a requirements specification defining the system in such a way as to meet user needs within the constraints of the resources available. By contrast, Avison & Fitzgerald consider that one of the most important aspects of the history of IS methodological development is the extension of the scope of the systems development life cycle into the area of strategy and planning. The first phase of the software development process is therefore concerned with the organization's overall strategy and the place of the proposed system within the strategy.

2 Avison & Fitzgerald take a fairly orthodox but relatively narrow view of software engineering, regarding it 'as a skill which improves program design and thereby makes software, an important element of computer information systems, more effective once implemented, and easier to maintain . . . Areas such as:

(a) understanding the problem area,

(b) understanding the needs of the user,

(c) looking at alternatives,

(d) deciding whether a computer system is needed.

lie outside the scope of software engineering' (Avison & Fitzgerald, 1988).

3 Birrell & Ould spend a considerable portion of their comparison of methodologies on mathematically-oriented methods including VDM, HDM, FDM and Higher-Order Software. Avison & Fitzgerald mention the area only so that they may explain their reasons for excluding it: 'Where formal methods are particularly applicable is in process-control applications, such as missile systems or factory production systems. They are less applicable in the information systems arena, because of its people-orientation. We have chosen, therefore, not to discuss formal methods further' (Avison & Fitzgerald, 1988).

There is a danger that the information systems community, having decided that software engineering forms only a small part of the systems development domain, may ignore software engineering techniques as being irrelevant or (at best) extremely limited. The tools and techniques being developed as part of software engineering (such as mathematical modelling, verification, information hiding and abstract data types, for example) are particularly seen as being limited in applicability to the domain in which they are currently being used. We shall, however, demonstrate in this paper that the domain of use is often much wider. In the final section, we shall make use of the techniques of object-orientation and mathematical modelling in the analysis of an information systems problem at the organization — rather than at the systems development — level.

## A SYNTHESIZED STRATEGY

The information systems community has long recognized the importance of computer science as a reference discipline (Anon., 1987) but has sought to differentiate itself by stressing its sociological and organizational focus, looking to additional reference disciplines such as cognitive psychology and political science (Keen, 1980), organizational theory, organizational behaviour, systems theory, management science and sociology (Anon., 1987).

There has been a clear feeling within the IS community that the influence of computer science and, more generally, the physical sciences and scientific method, has been too strong (Mumford et al., 1985; Boland & Hirschheim, 1987). Recent research in information systems has focused much more strongly on the organizational and sociological issues $^{2}$ . Similarly, considerable efforts have been made in transferring from academe to industry the impetus to view information systems from this socio-organizational perspective. These efforts have been successful — not only have we seen a change in nomenclature from data processing departments to information systems departments, but there is evidence that the change is more than simply nominal. As an example, the conference shaping organizations shaping technology 1989 (SOST/89) held in NSW, Australia, attracted almost equal numbers of delegates from the academic and professional IS sectors to discuss social, organizational and managerial aspects of information systems. SOST was sufficiently successful to become a biennial event.

![](/api/attachments/NMUREM5B/fulltext/images/f60c2b06798a205b249be51a776e6df81d3a085151a4f3b7eab9a2ab65d233b0.jpg)  
Figure 1. The information systems problem — current practice.

We have seen thesis (a reference discipline of computer science) and are currently seeing antithesis (reference disciplines in the social and organizational arena). Both information systems and computer science are relatively young disciplines and we believe that there is much to be gained by completing this cycle of the philosophical progression and achieving a synthesis of the contributions possible from both perspectives.

In Figure 1 we identify a model of the 'information systems problem', representing common current practice. This diagram shows a problem context which is first informally and then systematically specified. The informal specification is (of course) ambiguous, imprecise and contradictory. The various systematic specification techniques (amongst which we may consider prototyping) are designed to reduce this ambiguity, imprecision and contradiction. Unfortunately, while the systematic techniques assist in this process, only formal specification languages have a well-defined syntax and semantics — and are thus capable of precise analysis.

Once the solution design and implementation have occurred, the formalized $^{3}$ information system which results has a well-defined behaviour (that is, a precise behaviour free of ambiguity). This applies whether or not we are dealing with a computer-based system although it is, perhaps, easier to identify the problem in this case. Programming languages are, in a sense, mathematical specification languages (albeit, unconventional ones). There can be no doubt that a program is an unambiguous, precise and complete specification of its behaviour (that is, all programs do something — whether or not that something was the task envisaged by its specifier).

The crucial question, therefore, is that of the point at which we resolve the ambiguities, imprecisions and contradictions of our specification. Checkland, in introducing the concept of Weltanschauung says 'whether we realize it or not, we view raw data via a particular mental framework, or world-view . . . we attribute meaning to the observed activity by relating it to a larger image we supply from our minds. The observed activity is only meaningful to us, in fact, in terms of a particular image of the world or Weltanschauung, which in general we take for granted' (Checkland, 1981). Clearly, we would prefer to have our ambiguities, imprecisions and contradictions resolved by those whose world-view is organizational in nature, rather than by those whose world-view is technical. The present method of information systems development ensures that many specification problems remain unresolved until solution implementation — in computer-based information systems this means the coding phase, where the actor has an exclusively technical world-view.

This is particularly important since, as we have already stated, approximately 60% of the errors eventually found in a typical software product arise from ambiguities, omissions, contradictions and lack of precision in the specification (Boehm, 1981). These specification problems arise from:

(a) a misunderstanding of the societal and organizational context in which the software will be used (Wilson, 1984; Avgerou, 1987),

(b) inconsistent interpretations of the specification: by the client and the specifier, within the development team.

Figure 2 presents a model of an alternative development strategy — highlighting the issue of requirements determination and specification — in which there is an iterative process of:

(a) information analysis based upon the organizational context under review and, in general, statements of the conflict which exists within our understanding of the problem,

(b) formal modelling of the various informal and semi-formal perspectives on the problem area under review, resulting in a collection of formal and analysable problem statements,

(c) integration and analysis of the formal problem statements in the light of a general understanding of the organizational context and the informally and semi-formally expressed problem statements. Conflict between the world-views will be highlighted by this analysis, thus providing an opportunity for its resolution by means of further information analysis.

This development approach caters for both functional and non-functional requirements. In the authors' current application of this strategy, we use formal mathematical modelling purely for functional requirements and recommend that non-functional requirements be reviewed informally during the information analysis and validation phases, using whatever techniques seem appropriate. We take the view that it is vital to the development of high-quality information systems that conflict in requirements be identified and resolved. This is true whether the term 'high-quality' is taken to mean fitness for purpose, optimal organizational fit, actual efficiency of the system, or cost effectiveness (that is, an economic view of quality) — or, indeed, any other definition of quality which may seem relevant.

![](/api/attachments/NMUREM5B/fulltext/images/51a9ca9bb43e2602f0a1db4dea968362196ec66d768494680d153a6643ca4e8d.jpg)  
Figure 2. The information system problem — an alternative approach.

Work in formal specifications within the software engineering domain initially arose from the desire to verify mathematically the match between computer programs and their specifications. It has since been argued (Sommerville, 1989; Hall, 1990; Swatman et al., 1991) that formal specifications may, in fact, be valuable independently of their use in program verification. Major contributions which these specifications can make to the quality of the software developed with their assistance include:

(a) the provision of a deeper insight into the system being specified — a formal specification prevents the creation of inherent contradictions caused by redefining the 'meaning' of portions of the specification without corresponding changes to the specification itself,

(b) a mechanism allowing study and analysis of the specification, thus offering reliable predictions of behaviour; and leading to,

(c) a basis for system acceptance testing.

It is the ability to reason reliably about the formally specified systems which makes formal specifications an ideal means of validating informal functional requirement statements.

The model shown in Figure 2 describes an approach which is compatible with any of the commonly-used development 'life cycles':

(a) a conventional waterfall life cycle approach to development (Royce, 1970),

(b) a Soft Systems approach (Checkland, 1981),

(c) a prototypical approach (Birrell & Ould, 1985),

(d) Boehm's "spiral" model of development (Boehm, 1988).

The use of formal specifications of functional requirements does not, therefore, preclude the selection of any development life cycle. Formation specifications are simply a tool which can be used for precise analysis — enabling the identification of conflict within and between statements of requirements.

## Benefits and costs

The benefits of using formal specification techniques (in conjunction with techniques appropriate to socio-organizational analysis) include the following.

1 More relevant systems. The use of formal methods as an analytic tool assists in identifying (and thus in resolving) conflicts amongst the various Weltanschauungen which exist within the organizational context, in terms of the system's functional goals.

2 Higher-quality systems. The use of formal methods as a specification tool will contribute to precise communications amongst the members of the development team, thus helping to ensure that the system which is developed corresponds to the system which was originally specified. The precise nature of the specification also provides objectivity in the form of a base-line from which all explanations and demonstrations of the system's intended function will be derived.

3 A more manageable development process. It is very easy to compare progress which has been made in implementing a system with its formal requirements specification — and thus to identify the implementation tasks which still remain. 'The application of formal methods can also make you more confident in the development process, because at each stage it is clear what has and has not been done. Monitoring is more reliable and thus development is less risky' (Hall, 1990).

4 Cheaper, faster systems development. Although we expect a longer specification phase in the development of formally specified systems, there are some indications that the overall implementation time and cost are, if anything, reduced — due to fewer specification ambiguities, imprecisions and contradictions to be resolved and to the more precise communication possible between specifiers and developers.

The evidence to support these asserted benefits comes from a series of case studies conducted by the author in January 1991 at Praxis, IBM and Rolls Royce and Associates; and from a variety of published material including Cunningham et al. (1985), Oakley (1985), Cohen et al. (1986), Norris (1986), Hayes (1987), Hall (1990). Further case research is underway in Australia in collaboration with OTC, the Western Australian Department of State Services and Telecom Plus.

There are potential benefits to be gained from the adoption of formal methods beyond those relating purely to the software development process. The ordering and purchasing of packaged software involves liability on both sides — the purchaser must clearly and unambiguously define his/her requirements; and the developer must produce a system which demonstrably meets the specified requirements. Until recently it has been difficult, if not impossible, to specify liability in disputes between the parties to a software development contract. This problem is increasing in importance as the trend towards third-party software development (Swatman et al., 1990) and facilities management (Dearden, 1987) continues.

Professional liability for the software industry is, however, becoming a reality — the legal implications of software developers' actions were highlighted in the U.S. case of Diversified Graphics v. Groves (Bloombecker, 1989). Formal specifications provide a factual basis for litigation, by defining the developer's responsibilities (and success in meeting specified criteria) clearly and provably.

The costs of adopting formal specification methods include the following.

1 Training in mathematics and the formal specification techniques. Many authors have pointed to the need for training (Jones et al., 1986; Norris, 1986; Wordsworth, 1986; Wordsworth, 1987; Youll & Simms, 1988). Estimates of the amount of education and training effort required vary, but the consensus is that the level of mathematical sophistication required for specification $^{4}$ is rather shallow. 'At Praxis, we have found that the mathematics of specification, at least, is easily learned and used' (Hall, 1990). 'The mathematical notations and concepts are not a stumbling block to the vast majority of students. The essential mathematics for writers of specifications is a little set theory, including the notions of ordered pair, binary relations and sequence, and a little predicate calculus necessary to write set-theoretic predicates including quantified statements' (Wordsworth, 1986).

The authors are currently supervising a PhD and a Master degree student researching the use of formal specifications in a commercial environment. The research students' only academic qualifications are in information systems and neither has studied discrete mathematics (or, indeed, any mathematics beyond High School level other than statistics). The training programme, taken over a period of 5 weeks, comprises 15 hours of seminar, together with some practical exercises to be undertaken in the students' own time. These students appear to be progressing at a rate equivalent to that of the computer science honours students who are undertaking the same programme. it is clear that the key to a successful use of formal methods is more strongly related to the ability to abstract and model problem situations that it is to a flair for (or experience in) mathematics.

The need for consultancy. Before an organization can commit to the use of formal specification as a part of the development process for information systems (other than systems whose primary purpose is the evaluation of the development method), it must possess some level of confidence in its ability to use the tool effectively. Until the organization is able to train a 'critical mass' of experts in the use of the tool, it must have access to experts on a consultative basis. In view of the comparatively early stage of the process of transferring formal techniques to industry, this will most often mean collaboration with tertiary institutions — although there are now a small number of commercial organizations able to provide these services.

3 The need to reorganize the development team. Differing levels of expertise in formal specification (and other) techniques are required by the various actors participating in the development process. It is unreasonable to anticipate that the majority of people who are concerned with the context in which the proposed information system will exist should possess skills in the formal (mathematical) specification of software. Similarly it is unreasonable to expect to find expertise in socio-organizational skills amongst the more technically-oriented actors. We therefore believe that a strongly interactive multi-disciplinary team is necessary for the successful elicitation, analysis, synthesis and definition of information system requirements. We do not believe that it is effective either:

(a) to consider the socio-organizational perspective in isolation during the development of information systems requirements; or

(b) to consider the technical perspective in isolation thereafter.

## Overcoming the perceived difficulties

Cunningham et al. (1985) argue that formal methods promise to be cost-effective ways of overcoming the difficulties of constructing large scale software systems, although they point out that there are obstacles to be overcome in transferring formal specification technology to industry, pointing to:

(a) widespread suspicion amongst potential recipients that formal methods are of little value,

(b) unrealistic expectations by the transferor of the mathematical capabilities of the recipients,

(c) immaturity of the techniques,

(d) fear of intellectual inadequacy on the part of the potential recipients (Cunningham et al., 1985).

We will address each of these issues in turn.

## The value of formal methods in information systems

A perception exists that formal methods are applicable only to 'toy systems' and that formal methods will not scale up for use in realistically sized development. This view derives, in part, from the tutorial literature and, in part, from the comparative specification technique literature where the examples given tend to be simple to the point of commercial irrelevancy. In fact, formal techniques are today being used in commercial systems developments including the CICS project at IBM, Hursley.

Research into formal methods was driven by the problems of developing safety-critical and extremely complex software, such as military systems (Ince, 1989; McKenzie Sibbett, 1989); nuclear reactor monitoring systems (Bloomfield & Froome, 1986); operating systems (Morgan & Sufrin, 1984); and transaction processing monitors (Hayes, 1985). The vast majority of experience in the commercial use of formal methods is in connection with critical systems — which leads to a perception within the IS community that formal methods are only economically viable where the consequences of failure are extreme.

While the relative numbers of systems which have been developed using formal methods are still small, they are no longer confined to the 'critical' domain. Hall (1990) describes the cost-effective development of a computer aided software engineering (CASE) tool. Here the formal specification language Z is used as a tool in the analysis and specification of system requirements. In the following section and the Appendix of this paper, we show how formal specification can be used in the analysis of a problem situation which clearly lies within the information systems domain. We believe that this case study is small enough to be appreciated, while being sufficiently realistic and relevant to demonstrate the utility of formal specifications in an IS environment.

## The mathematical capability of the IS community

Avison & Fitzgerald present the conventional wisdom of the IS community when they suggest that information systems professionals have largely ignored the potential of formal methods because the required level of mathematical sophistication is not generally achievable (Avison & Fitzgerald, 1988). While we accept that this statement reflects present reality, we believe that the decision to ignore formal methods is based on a misconception within the IS community of the level of mathematical sophistication required for the effective use of formal specification techniques within IS. It is useful to stress again that, at the current level of maturity of formal methods, we do not recommend the use of a fully formal development process which includes proof of program correctness, but merely the use of formal specification techniques as analysis and communication tools. The level of mathematical sophistication required for specification is far less than that required for fully formal development.

We have already argued for a multi-disciplinary information systems team. In such a team, varying levels of mathematical capability would be required.

1 Those members of the team who write formal specifications — the systems (as opposed to business) analysts and the systems designers — clearly require the greatest level of sophistication. We have already indicated during our discussion of training that the consensus of opinion, supported by our own experience, is that an ability to abstract, analyse and conceptually model problem situations is considerably more important to the successful use of formal specification techniques than is any mathematical training or level of sophistication.

2 Those members of the team who are more user-oriented need a far lesser level of mathematical sophistication. Olle et al. have stated:

'Feedback from the user acceptor [the representative of the users or the executive responsible or both] and from other users is important, especially during the analysis stage. Users should not be expected to react to specifications expressed in some highly mathematical form, however rigid and complete this may be' (Olle et al., 1988).

If we are to accept that view, we need members of our team who are skilled readers of formal specifications (but who need not have the additional skills necessary for specification writing) and who can translate the formal specification into a form acceptable for communication with users unfamiliar with the notation. Such a form may be wholly or partly textual, diagrammatic, or in the form of an animated prototype. $^{5}$ Although, under this arrangement, the user does not have the chance to examine a precise, formally analysable specification, enormous benefits of increased understanding obtained in the process of specification writing and translation may still be gained.

3 Those members of the team responsible for implementing the formal information system again require only the skills necessary for specification reading.

Only key members of the information systems team will, therefore, require the skill to write formal specifications — a skill which is roughly as difficult to learn as is one's first computer programming language. We suggest that such an expectation of information systems professionals is no greater than the expectation that such professionals gain the socio-organizational skills whose necessity has been promoted widely within the IS community.

## Immaturity of formal methods

Formal methods have been in transition from the academic to the commercial sector for some years now (e.g. Rolls Royce and Associates have been using formal methods for 10 years). Formal specification techniques are relatively well understood, though the problems of fully formal development (including refinement to proven code) and tools to support such a process remain areas of active research.

The British Ministry of Defence have produced an interim draft standard DefStan 00-55 (Ministry of Defence, 1989) requiring inter alia the use of formal methods in the development of safety-critical systems. MoD acknowledges, however, that considerable technology transfer must take place before the standard which will eventually evolve from the interim draft may be enforced. As an initial step, the MoD commissioned Cranfield Information Technology Institute (CITI) to conduct a study into the training and education necessary to support the proposed standard (Youll & Simms, 1988; Ministry of Defence, 1989).

Before formal specification techniques can be widely applied within the world of commercial information systems, a critical mass of professionals trained in the techniques must be achieved.

In Britain, professional re-training courses in formal methods are offered by both commercial organizations and tertiary institutions. Many computer science departments at tertiary institutions in Britain and overseas are already offering undergraduate level courses in formal methods. Graduates from these courses will help to swell the numbers of re-trained professionals.

## Fear of intellectual inadequacy

Any new technique is likely to threaten those members of a profession who do not already possess the requisite skills (as an extreme example, one could consider the Luddite response to the Industrial Revolution). It is perfectly reasonable for a senior member of a profession to fear the introduction of techniques which will require competition on even terms with the junior members of the profession.

Many people appear to dislike (or even fear) mathematics. In our current training programme, we are achieving some success by drawing examples from the commercial world inhabited by the trainees, rather than by using contrived and scientific exercises. The case study included in the Appendix to this paper was successfully used by the authors to encourage senior members of a state government department to engage in a collaborative research project in the application of formal specification methods within a commercial environment.

## A CASE STUDY IN FORMAL METHODS AND INFORMATION SYTEM

## Aims and scope

In this section, and in the Appendix, we present a case study which illustrates many of the issues which we have discussed above. Our principal aim is to illustrate that we can formally specify an information system of realistic size and present the results in a manner approachable by members of the IS community.

The object of our specification (Electronic Data Interchange or EDI) was chosen, not 'artificially' because it was a particularly suitable candidate for formal specification but, in a sense, arbitrarily — the authors were conducting a research programme in the area. The problem context which we investigate is: How does an organization use Electronic Data Interchange to gain strategic advantage? From here, we apply firstly informal, contextual analysis — we could have used any one (or even a combination) of a range of techniques here from the socio-organizational to the systematic.

As we proceed with the case study, we focus on a sub-problem: Should the organization approach EDI primarily from a technical or socio-organizational perspective? This is, in the author's experience, an example of a recurrent problem within the IS domain.

We review the EDI literature which suggests a socio-organizational and holistic approach to the problem is required; and the practice, particularly in Australia, which suggests that a technical approach is often adopted. We analyse the dichotomy and synthesize an informal model of the problem, in which those issues which are clearly technical in nature (in this case, the provision of a value-added telecommunications network) are clearly separated from the organizational concerns. We then specify this section formally, using Object-Z, thus creating a model with well-defined behaviour which is readily and reliably analysable using the tools of formal logic.

Although we do not take the process further in this paper, the next stage would be to verify that the externally observable behaviour of the formal model which we have created can be incorporated, without conflict, within the broader organizational model. The conflict statement resulting from this validation step which is not, of course, limited to issues directly connected with the new formal specification, would drive the next analysis/modelling/validation cycle.

On the assumption that the specification survives the validation process, we obtain the following benefits:

(a) a precise and unambiguous requirements specification which can form the basis of the development contract and the acceptance criteria for a software system — relevant whether the solution is to be implemented in-house, or by an external contractor,

(b) the safe application of reductionism to this aspect of the problem context.

The case study, then, illustrates the use of a formal approach to information systems modelling.

## Overview

Electronic Data Interchange (EDI), 'the computer-to-computer transmission of standard business data' (Emmelhainz, 1990), has shown remarkable growth over recent years. Early applications were intended simply as replacements for paper document flows by the U.S. transportation industry during the late 1960s, and to improve the efficiency of product ordering and delivery systems between companies. Subsequently, the benefits obtainable from integrating EDI with existing business practices and application systems have encouraged the conception and development of multi-organizational systems (of which Europe's automotive industry system ODETTE and Australia's trading community system, Tradegate are examples).

It has now become almost an article of faith within the international EDI community to claim that 'EDI is 90% business and 10% technology'. A wide variety of writers within both the 'trade' and academic sectors have provided support for the view that EDI should be regarded as a strategic issue, rather than as a technical problem (see, for example, Emmelhainz, 1988, 1990; Hardy, 1988; Patrick, 1988; Wilmot, 1988; Skagen, 1989; Swatman & Swatman, 1989a, b, 1991; Benjamin et al., 1990; Swatman & Clarke, 1990; and many others). Despite this strategic view, many organizations (particularly within Australia) perceive EDI as a technical issue (Swatman & Swatman, 1991). In practice, this means that the control of EDI implementation tends to be ceded to the information systems department.

As the most significant long-term benefits of EDI are gained from the revision of (and integration with) existing information systems and organizational structure, this technocentric attitude leads to a lack of organization-level control and a failure to gain the maximum potential available from the implementation. This situation has meant a much slower 'ramp-up' of EDI in Australia than that seen in North America and (in expectation of the imminent completion of the single unified market) within the European Community. It appears likely that, if Australian organizations wish to continue doing business in the North American and European markets, they will increasingly need to trade using EDI. If they hope to remain competitive in those markets, they must also integrate EDI internally. The EDI problem in Australia, then, is clearly within the information systems domain.

## The EDI problem analysed

A factor contributing to the perception of EDI as a technical issue within Australian industry may actually be the presentation of EDI as a purely organizational issue. An organization presented with such a simplified view may argue that embracing EDI involves inter alia:

(a) computerization of the mechanism by which the organization currently communicates with its customers, its suppliers, and other organizations with which it deals (e.g. the Customs, Port Authorities, etc),

(b) connection to a national (possibly, international) computer network.

These technical difficulties are often the first issues to be tackled when implementing EDI.

We took a rather different approach to the question of whether EDI was a technical or an organizational concern suggesting that the technical aspects of EDI are not absent (or even less important than the organizational and managerial considerations), but rather, that the technical and organizational aspects can be dealt with in isolation and, indeed, largely in parallel. In order to demonstrate that this contention was valid, we decided to model the technical part of the EDI system as an Abstract Data Type (after Liskov & Zilles, 1974). In this way, we could describe what an EDI system can be relied on to do, without concerning ourselves with how this behaviour would be achieved. Clearly, organizational concerns revolve around:

(a) whether the proposed behaviour of the EDI system was useful (and, if not, whether a useful behaviour could be specified); and

(b) whether (and how) the organization can be remodelled so as to make effective use of the services offered by the EDI system

The technical issues, by contrast, revolve purely around ensuring that the EDI system does indeed behave in the specified manner.

Figure 3 shows how an organization which has adopted EDI may be divided into three essentially independent parts:

(a) within the organization, internal information systems generate information for transmission to other organizations,

(b) an interface system collects the information which is to be transmitted, formats and collates it appropriately, then transmits it to its recipient,

(c) a communications network through which standard documents will flow from sender to recipient.

There are few essential differences between the system which we have just described and a conventional mail system. In an EDI system:

(a) the communications network will be electronic rather than manual,

(b) the messages are standard rather than free form.

The benefits of this are:

Organizational EDI responsibilities  
![](/api/attachments/NMUREM5B/fulltext/images/a27eefd2fa99f636f52bdb62bf30871d84791cdb4796ea7e7ef7b8b5b4991bfc.jpg)  
EDI systems responsibilities  
Figure 3. EDI System architecture.

(a) the (two-way) interface between internal information systems and outside organizations may be automated,

(b) communication speed may be increased,

(c) communication may be directly from the information systems in one organization to the information systems in another BUT each organization is only responsible for getting the information from its own information systems to its own 'electronic door' and vice-versa.

In this case study, we will concentrate on defining the behaviour of the electronic communications network which forms the part of EDI external to the organization. While there is still much refinement required before all the problems of in-house EDI software integration are solved, the essential principles of the technology are already in place. It is in the domain of the third-party provider that a generic model of EDI system structure is urgently needed.

![](/api/attachments/NMUREM5B/fulltext/images/e01d38155fa18d0ba738cb8d22fdf0d334bcc77837ca4a0424e7b6819a3fc7d4.jpg)  
Figure 4. A generic model of an EDI communications system.

## An informal model of EDI communications systems

The EDI document transmission process can take place in one of two ways — either by linking the two trading partners directly (point-to-point) via modem, or by means of third-party value-added networks: 'in essence, what a third-party network provides is the EDI communication skills, expertise and equipment necessary to communicate electronically. In addition, [it] can also provide value added services such as translation to standard, international connections, connection to other third party networks and training' (Emmelhainz, 1990).

Organizations contemplating the implementation of EDI tend to see each scheme as unique, largely because each company involved in a particular market segment transacts its business slightly differently from its competitors. It was this perception that a company's methods of doing business were unique (and thus that software to meet those needs must also be unique) which led to the development of so many software variations on universal requirements such as payroll or general ledger. In much the same way, despite the perception of EDI as an ever-new technical problem, EDI communications systems conform to a relatively simple model illustrated in Figure 4 (Swatman & Swatman, 1991). Figure 4 provides a generalization of the three-part classification of EDI systems suggested by Akerman & Cafiero (1985):

1 One-to-many systems. These systems typically arise when a (large) organization wishes to streamline its interactions with suppliers (or customers). The initiating organization is the hub of the system, while its trading partners form the satellites.

2 Many-to-many or 'clearing house' systems. A more general form in which there is no single hub but, apparently, many buyers and sellers interacting with each other. Notionally, the system itself forms the hub and all parties are satellites. The development of a system of this type is usually driven by two organizations, each representing an industry group. In a sense, these systems can be considered as one-to-one systems connecting the buyer industry group with the supplier industry group. Although Akerman & Cafiero do not carry this idea further, it is a simple task to extend the concept to allow for the participation of any number of industry groups — each of which may be either supplier or customer.

3 'Incremental paper trail' systems, where documents are amended by a series of participants with additional information being added to the document at each stage in the process, are particularly relevant to the domestic and international trading community. Schemes of this type allow the progress of a shipment from exporter to importer to be covered by a single electronic document, to which each party merely adds the appropriate information, obviating the need for bulky and unmanageable documents such as bills of lading or ships' manifests (Akerman & Cafiero, 1985).

Our general model of an EDI communications system, incorporates the concept of persistent memory, necessary for incremental paper-trail documents. Although this diagram shows a single data store for the entire EDI system, we do not imply that the data store could not be implemented as a distributed database. In fact, the current European development of an electronic Bill of Lading (EDI Monthly Report, September 1990) with its consequent need for multiple third-party network providers, seems to indicate that distributed document storage will be the method of choice (if not actually that of necessity). It is now clear that we can redefine EDI at a systems level in the following manner.

EDI communications systems are that sub-class of distributed information systems where the users of the system are organizations rather than individuals and where messages must conform to some standard.

The rapid growth of third-party EDI network service providers (Takac & Swatman, 1989) offers further support for the proposition that the provision of EDI services is, at worst, a solvable and comparatively standard technical issue. From the systems developer's perspective, therefore, it can be said that EDI is not a new problem, although such a statement does not imply that the development of EDI systems is a simple issue. The successful development of large organizationally effective systems continues to be an area in which we achieve only limited success. The most significant consequence of defining EDI in terms of a single system type is not the fact that this eliminates the difficulty of implementing EDI schemes, but that it debunks the myth of

EDI's technical complexity. Clearly, from a technical point of view, the fact that the users of a system are organizations (rather than individuals) is largely irrelevant. EDI per se offers few unique technical problems — despite its organizational challenges.

## CONCLUSION

In this paper we have argued that formal specification methods may be used in conjunction with socio-organizational analysis techniques to identify and develop more relevant and higher quality information systems. Although mathematical techniques are generally unfamiliar to most members of the information systems profession (and certainly to the end-user members of the development team), we have argued that the difficulties of the technology transfer are not nearly so great as is commonly supposed. Even were this not so, provided that the difficulties are not insuperable, if the techniques can be shown to be essential to the development of relevant and high-quality systems, the information systems community cannot afford to ignore them.

The difficulties of arriving at a precise specification of an appropriate system are equally great in information systems and in technical computing systems. In both cases, we need tools which help us to think constructively and perceptively about problem situations. Although we believe that there are enormous benefits to be gained from a synthesis of research within information systems and software engineering generally, in this paper we have confined ourselves to the enhancement which formal system specification can provide to the traditional information analysis process.

The case study described in the final section (and which leads to the formal specification contained in the Appendix to this paper) is the seminal core of a series of collaborative research projects currently being undertaken by Curtin University's School of Computing Science and the Western Australian Department of State Services. We have used the specification as a means of demonstrating the relevance of formal specifications to the identification and analysis of commercial problems. We have been pleasantly surprised by the level of acceptance with which this approach has met. It is clear that there is wide agreement within the information systems community that problem identification and requirements analysis and specification are seen as both critical and as inadequately handled by currently available techniques.

It can be argued that the academic information systems community has a duty to consider all possible solutions to the presently inadequate practice of information analysis and system specification. We believe that tools developed within the software engineering discipline — in particular, formal methods of system specification — have the potential to improve this practice, offering the analyst an analysable contextual modelling tool.

## REFERENCES

Akerman, G. & Cafiero, W. (1985) Introduction to Electronic Data Interchange: A Primer. GE Information Services.

Anon. (1987) Information systems research methods — summary of a questionnaire investigation carried out by IFIP WG 8.2 TG. Information Age, 4, 238–241.

Avgerou, C. (1987) The applicability of software engineering in information systems development. Information & Management, 3, 135-142.

Avison, D.E. & Fitzgerald, G.(1988) Information Systems Development: Methodologies, Techniques and Tools. Blackwell Scientific Publications, Oxford.

Bamberger, J. (1990) Keynote Address: SEI Overview. ASWEC '90, 5th Australian Software Engineering Conference, Sydney, Australia, May.

Benjamin, R., De Long, D. & Scott Morton, M. (1990) Electronic data interchange: how much competitive advantage? Long Range Planning (UK), 1, 29-40.

Birrell, N.D. & Ould, M.A. (1985) A Practical Handbook for Software Development, Cambridge University Press, Cambridge.

Bloombecker, J. (1989) Malpractice in IS? Datamation, Oct 15, 85–86.

Bloomfield, R. & Froome, P. (1986) The application of formal methods to the assessment of high integrity software. IEEE Transactions on Software Engineering, 9, 988–993.

Boehm, B.W. (1976) Software engineering. IEEE Transactions on Computers, 12, 1226–1241.

Boehm, B.W. (1981) Software Engineering Economics. Prentice Hall, Englewood Cliffs.

Boehm, B. (1988) A spiral model of software development and enhancement. IEEE Computer, 5, 61–72.

Boland, R. & Hirschheim, R. (1987) Critical Issues in Information Systems Research. Wiley, Chichester.

Booch, G. (1987) Software Engineering with Ada, 2nd edn. Benjamin Cummings, Menlo Park.

Buckingham, R., Hirschheim, R., Land, F.F. & Tully, C.J. (eds) (1987) Information Systems Education: Recommendations and Implementation. Cambridge University Press, Cambridge.

Checkland, P. (1981) Systems Thinking, Systems Practice. pp. 3–98, 245–285. Wiley, Chichester.

Cohen, B., Harwood, W. & Jackson, M. (1986) Specification of Complex Systems. Addison Wesley, Wokingham.

Cunningham, R., Finkelstein, A., Goldsack, S., Maibaum, T. & Potts, C. (1985) Formal requirements specification — the forest project. In: Proceedings of the International Workshop on Software Specification and Design, pp. 186–191.

Dearden, J. (1987) The withering away of the IS organization. Sloan Management Review, Summer, 87–91.

Diller, A. (1990) Z: An Introduction to Formal Methods. Wiley, Chichester, UK.

Downes, E., Clare, P. & Coe, I. (1988) Structured Systems Analysis and Design Method. Prentice Hall, Englewood Cliffs.

Duke, R., King, P., Rose, G. & Smith, G. (1991) The OBJECT-Z specification language. Version 1 Technical Report 91–1 Software Verification Research Centre, Department of Computer Science, University of Queensland, Australia.

Eliason, A. (1990) Systems Development: Analysis, Design, and Implementation, 2nd edn Scott, Foresman/Little, Brown Higher Education, Glenview, Illinois.

Emmelhainz, M. (1988) Strategic issues of implementation. Journal of Business Logistics, 2, 55–70.

Emmelhainz, M. (1990) Electronic Data Interchange: A Total Management Guide. Van Nostrand Reinhold, New York.

Galliers, R. (ed.) (1987) Information Analysis: Selected Headings. Addison Wesley, Sydney, Australia.

Hall, A. (1990) Seven myths of formal methods. IEEE Software, 5,11–19.

Hardy, M. (1988) Opening up European telecommunications — the commission perspective. Proceedings of the Conference EDI '88, London.

Hayes, I. (1985) Applying formal specification to software development in industry. IEEE Transactions on Software Engineering, 2, 169–178.

Hayes, I. (ed.) (1987) Specification Case Studies. Prentice Hall International (UK), London.

Ince, D.C. (1989) A standard for formal education. Computing, (UK), May 25.

Jackson, M.A. (1983) System Development. Prentice Hall, Englewood Cliffs.

Jones, J., Loomes, M. & Shaw, R. (1986) An Education Programme for Practising Software Engineers. In: Software Engineering '86, Barnes, D. and Brown, P. (eds), pp. 66-87, Peter Peregrinus, London.

Jones, G. (1990) Software Engineering, John Wiley and Sons, New York.

Keen, P. (1980) MIS research: reference disciplines and a cumulative tradition. In: Proceedings of the 1st International Conference on Information Systems, Philadelphia, PA 8–10 December.

Keen, P. (1987) MIS research: current status, trends and needs. In: Information Systems Education: Recommendations and Implementation. Cambridge University Press, Cambridge.

Liskov, B. & Zilles, S. (1974) Programming with abstract data types. ACM SIGPLAN Notices, 4, 50–59.

Macro, A. & Buxton, J. (1987) The Craft of Software Engineering, Addison Wesley, Reading.

Macro, A. (1990) Software Engineering: Concepts and Management, Prentice Hall International (UK) Ltd, Hemel Hempstead, Herls.

McKenzie Sibbitt, H. (1989) Software quality: a formal introduction to def stan. Systems International, April.

Ministry of Defence (UK) (1989) Critical software steering group. Interim Defence Standard 00–55 (Draft). May.

Morgan, C. & Sufrin, B. (1984) Specification of the UNIX filing system. IEEE Transactions on Software Engineering, 2, 128–142.

Mumford, E., Hirschheim, R., Fitzgerald, G. & Wood-Harper, A. (eds) (1985) Research Methods in Information Systems. Elsevier Science Publishers, B.V., Amsterdam.

Norris, M. (1986) Z: A formal specification method STARTS: software tools for application to large real-time systems. Debrief report National Computing Centre Ltd, Manchester.

Nunamaker, J. (1981) Educational programs in information systems: a report of the ACM curriculum committee on information systems. Communications of the ACM, 3, 124–133,

Oakley, B. (1985) The Alvey Programme: Progress Report — 1985 (Poster Supplement). Technical report Alvey Directorate.

Olle, T., Hagelstein, J., Macdonald, I., Roland, C., Sol. H., Assche, F.V. & Verrijn-Stuart, A. (1988) Information Systems Methodologies: A Framework for Understanding. Addison Wesley, Wokingham.

Patrick, G. (1988) The challenges of EDI decision making. In: The EDI Handbook, Gifkins, M. and Hitchcock, D. (eds). Blenheim Online Publications, London.

Ratcliff, B. (1987) Software Engineering: Principles and Methods. Blackwell Scientific Publications, Oxford.

Royce, W. (1970) Managing the development of large software systems. Proceedings of WESTCON, California.

Schneider, R. (1987) Prototyping toolsets and methodologies: user/developer sociology. Proceedings of IEEE International Conference on Systems, Man, and Cybernetics. October.

Senn, J. (1990) Information Systems in Management, 4th edn. Wadsworth Publishing Co., Belmont, California.

Skagen, A. (1989) Nurturing relationships, enhancing quality with electronic data interchange. Management Review, February, 28–32.

Sommerville, I. (1989) Software Engineering, 3rd edn. Addison Wesley, Wokingham.

Spivey, J.M. (1989) The Z Notation: A Reference Manual. International Series in Computer Science Prentice Hall, Hemel Hempstead, Hertfordshire HP2 4RG, UK.

Steward, D. (1987) Software Engineering with Systems Analysis and Design. Brooks/Cole Publishing Co., Monteray, California.

Swatman, P. & Clarke, R. (1990) Organisational, sectoral and international implications of electronic data interchange. In: Proceedings IFIP Conf HCC4 (4th International Conference on Human Choice and Computers) Dublin, July.

Swatman, P. & Swatman, P. (1989a) Electronic data interchange — implications for industry. Proceedings Conference SOST '89, Terrigal, NSW, April.

Swatman, P. & Swatman, P. (1989b) Europe's single unified market — 1992 — a spur to the development of Electronic Data Interchange? Proceedings Conference ACC '89 Perth, Western Australia, September.

Swatman, P. & Sweatman, P. (1990) The software reusability issue: perspectives from software engineering and infor-

mation systems. Proceedings of the 1st Australian Conference on Information Systems, February 1990, Melbourne, Australia.

Swatman, P. & Swatman, P. (1991) Electronic data interchange: organisational opportunity, not technical problem. Proceedings Conference DBIS '91—2nd Australian Conference on Information Systems and Database, Sydney University of New South Wales, February.

Swatman, P., Swatman, P. & Everett, J. (1990) Stages of growth of an innovative software house: an additional criterion for software package selection. Australian Computer Journal, 3, 81–91.

Swatman, P., Swatman, P. & Duke, R. (1991) Electronic data interchange: a high-level formal specification in OBJECT-Z. Proceedings of ASWEC '91—The 6th Australian Software Engineering Conference, Sydney, NSW, July.

Takac, P. & Swatman, P. (1989) A discussion of third party networks. Proceedings IDC Conference: EDI — The Key to Profitability in the 1990's, Sydney, NSW, December.

Wilmot, R. (1988) International trends and developments in EDI. Proceedings Conference EDI '88, pp. 15–21, London, November.

Wilson, B. (1984) Systems: Concepts, Methodologies, and Applications. John Wiley & Sons, Chichester.

Wordsworth, J. (1986) Teaching formal specification methods in an industrial environment. Software Engineering '86, pp. 43–51. Peter Perigrinus, London.

Wordsorth, J. (1987) Formal methods in the development of CICS. Computer Bulletin, 4, 6–7.

Youll, D. & Simms, P. (1988) Study of the training and education needed in support of def stan 00-55. Report issued to the Ministry of Defence by Cranfield Information Technology Institute Limited.

## Biographies

Paul Swatman spent 12 years in information systems in the private and public sectors before moving into academe at Curtin University in Perth where he is Lecturer in Software Engineering in the Department of Computer Science. His research interests are in the development of information systems, technology transfer and particularly the use of formal techniques within the IS domain.

Paula Swatman spent 10 years in information systems in the private sector. She subsequently moved into academe in Perth where she is Lecturer in the Department of Computer Science at Curtin University, specializing in the fields of IS management and implementation. Her current research interests are in the integration of Electronic Data Interchange systems into wider organizational applications.

# Appendix - A Formal Model of EDI

## A Brief Introduction to Object-Z

The specification language Z (Spivey, 1989) developed at the Oxford University has been extended at the University of Queensland (Duke et al., 1991) with the object-oriented concepts of Class and Instance. Here, we will introduce the features of the language which are used in the EDI Communications System specification. A number of textbooks introducing Z are available, including (Diller, 1990), though there are, as yet, no textbooks concerned with Object-Z.

When specifying using Object-Z, one must first identify the components (or objects) which, together with their interactions, comprise the system. The behaviour of each class of object identified is then specified by means of a Class Schema:

## StaffMember

We begin by defining constants which apply to each instance of this class. In this case, any members of the class StaffMember will have maxYears associated with them. maxYears will be constant for any particular StaffMember but may vary from StaffMember to StaffMember. maxYears has been declared to be of type N, that is, maxYears is a natural number – in the set $\{0,1,2,3,\ldots\}$ .

```txt
maxYears : N
```

The following (unnamed) box is called the State schema and, above the line, contains variables which will represent the internal state of each instance of the class. As each instance of the class passes through its "life" the values of these variables and, thus the internal state of the instance, will change. Below the line in the State schema, we describe constraints on what we consider to be valid StaffMembers – in this case that no staff member may be on staff for longer than the period maxYears which was set when s/he joined.

```txt
name : NAME
department : DeptName
yearsService : N
yearsService ≤ maxYears
```

In the following box, INIT, we describe the condition which must hold for a StaffMember to be in his/her initial state – in this case, that initially s/he has completed no service.

```txt
INIT yearsService = 0
```

Each schema below represents an operation which objects of this class may perform. In each Operation schema variables are declared above the line and predicates, which constrain the relationships between the variables, are set out below the line. The object may only be manipulated by means of its operations – its state should not be altered directly, though interrogation of the state variables is allowed.

It is sometimes useful to declare operations which are used by other operations within the object, but which may not be invoked directly by other objects within the system. These auxiliary operations, called Framing schemas are distinguished from ordinary operations by the initial letter $\Phi$ . An example of the use of a Framing schema can be found in the specification of the class EDICommsSystem in the case study.

Join

The first line lists those state variables which this operation may alter – in this case, name and department. State variables which have not been named in the delta list remain unchanged.

We include the initial condition schema INIT here which adds any variables which were declared in INIT (none in this case) to those which we declare here and also adds the condition which was defined in INIT to the condition which we define here – in this case we strengthen the precondition for this operation (only people who have no years of service can join).

Information which is passed in from the outside world when the operation is called have the suffix "?".

Information which is to be passed out of the object when the operation is called is given the suffix "!".

$\Delta$ (name, department)

INIT

newPerson? : NAME

newDepartment! : DeptName

We define the state of the StaffMember object after undergoing the join operation to have the input name and to have been assigned to some department. Variables after the operation are distinguished from those before the operation by the decoration ' - for example, name'. Operations may be more or less deterministic as desired. In this example we set name' deterministically, but allow department to take any (valid) value, then report the value set in newDepartment!, the output variable.

name' = newPerson?

department' = newDepartment!

and newDepartment! of type DeptName. Only a limited number of types are predeclared in Object-Z - typically, the well known mathematical sets such as N, the Natural Numbers. We can, however, define new types. In the case of Name and DeptName our interest is not in the form which these types may take but, simply, in the existence of a set of things which can be considered to be NAMEs and a set of things which can be considered to be DeptNamess. Object-Z allows us to declare the existence of such types in the following way (though, strictly, such type declarations should be made before they are used):

## [NAME,DeptName]

In addition to its use of schema boxes, Object-Z makes use of many symbols drawn from the world of formal logic and mathematics. The symbols which are used in the case study specification are set out below:

Typically, we build up system specifications by combining schemas. For example, we can model a very simple personnel system as follows:

<table><tr><td>==</td><td>is defined to be</td></tr><tr><td>×</td><td>cartesian product</td></tr><tr><td>∨</td><td>for all...</td></tr><tr><td>∃</td><td>there exists...</td></tr><tr><td>|</td><td>a delimiter - can often be read as where...</td></tr><tr><td>●</td><td>another delimiter - can often be read as such that...</td></tr><tr><td>∧</td><td>logical and</td></tr><tr><td>∨</td><td>logical or</td></tr><tr><td>¬</td><td>logical not</td></tr><tr><td>⇒</td><td>implies</td></tr><tr><td>{}</td><td>bracket a set</td></tr><tr><td>∅</td><td>the empty set</td></tr><tr><td>A : FB</td><td>A is of type powerset of B i.e. A is some set of B</td></tr><tr><td>a ∈ A</td><td>a is a member of the set A</td></tr><tr><td>∪</td><td>set union</td></tr><tr><td>∩</td><td>set intersection</td></tr><tr><td>⊆</td><td>subset</td></tr><tr><td>⊂</td><td>proper subset</td></tr><tr><td>\</td><td>set subtraction</td></tr><tr><td>↔</td><td>relation</td></tr><tr><td>↔</td><td>partial function</td></tr><tr><td>→</td><td>total function</td></tr><tr><td>↔</td><td>maplet - links the two items in an ordered pair</td></tr><tr><td>(a,b)</td><td>an alternative representation of an ordered pair</td></tr><tr><td>dom</td><td>domain of a relation</td></tr><tr><td>ran</td><td>range of a relation</td></tr><tr><td>seq</td><td>sequence</td></tr><tr><td>Φ</td><td>as initial letter indicates a framing schema</td></tr><tr><td>Δ</td><td>introduces a list of variables which may be changed by an operation</td></tr><tr><td>a.op</td><td>the operation op on variable a</td></tr><tr><td>&#x27;</td><td>as suffix, indicates a variable name after the operation</td></tr><tr><td>!</td><td>as suffix, indicates an output variable</td></tr><tr><td>?</td><td>as suffix, indicates an input variable</td></tr></table>

```txt
PersonnelSystem ____
No constants this time.
The personnel system is just a set of StaffMembers – initially an empty set.
```

```txt
employees : P StaffMember
```

```ini
INIT
employees = ∅
```

We can now specify an operation which allows a person to join the company. We have declared input variable newPerson? and output variable newDepartment!. These variables are identified with the variables of the same name in the StaffMemeber's Join operation when we make the statement s.Join. As a consequence, a Join operation occurring at the system level means that the Join operation occurs to the StaffMember called NewPerson (who is not already an employee) and the newly Joined StaffMember becomes a member of the set which comprises the employees recorded in the system.

```python
Join
△(employees)
newPerson? : NAME
newDepartment! : DeptName
∃s, s' : StaffMember • s∉ employees
    s'∉ employees
    s.Join
    employees' = employees ∪ {s'}
```

To complete our rather trivial system, we define an operation which allows employees to leave the company. This operation illustrates one of the advantages of a formal specification language over a programming language. We do not need to do any housekeeping. When an employee leaves service, we don't care about him/her any more and this is mirrored in our specification. The employee leaves service when s/he is removed from our set of employees – and that's all we need to say.

```ini
Leave
Δ(employees)
leaver? : NAME
leaver? ∈ employees
employees' = employees \ {leaver?}
```

## Introduction to the Object-Z Specification

The formal specification which follows was written by the authors in collaboration with Roger Duke $^{6}$ in the specification language Object-Z.

An understanding of Z and Object-Z is, of course, necessary for a full understanding of the specification. Since the specification is embedded within explanatory text, however, we believe that it is sufficiently self-explanatory to allow the interested reader to gain a flavour of the approach.

We begin by defining some basic types which will be used within the specification without description of their structure:

[Code, MessId, Message]

We now describe the "standard document" philosophy of EDI:

\- each item of data will be associated with a field identifier - there will be no "free" items of data. Formally then:

Info : MessId ↔ Message

describes all the allowable combinations of field names (MessIds) and field contents (Messages) within the system. There will, of course, be infinitely many members of this relation but, importantly, this modelling approach allows us to effectively "type" the fields independently of the Object-Z typing mechanism. That is, to exclude from the Info relation invalid (MessId, Message) combinations, while still considering all Messages to be of the same "type" in all other respects. Sub-typing within Message will be important at more detailed abstraction levels while, at the current level, sub-typing would merely obscure important detail.

\- each document type, which for the sake of convenience we identify by means of a unique document code (Code), is associated with a set of MessIds which define its form:

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
form: Code $\rightarrow$ P MessId
</div>

It is useful to specify an abbreviation for the set of Codes which identify defined documents:

DocCode == dom form

DocumentType
code : DocCode

On receipt of a document, the form in which the subscriber must respond is fixed. This response may be “no response”, or it may be the issue of some other EDI document. In the case of the majority of EDI documents, we expect either the issue of a simple confirmation of receipt document or no response at all to be the defined action. In the case of incremental paper trail documents, however, we anticipate that many documents will be received by intermediate subscribers which require reaction in some fixed form.

## Example

In the process of "transmitting" an electronic Bill of Lading, we expect to send inter alia:

\- a Request for Insurance Cover document to the nominated insurer—the expected response being an Insurance Certificate: a document which may contain either acceptance or rejection. Throughout this specification, we will consider both acceptance and rejection documents to be instances of the same DocumentType

\- a Request for Letter of Credit document to a subscriber—the expected response being a Letter of Credit document which may be either an acceptance of rejection of the request

\- a Request for Customs Clearance document—the expected response being a customs clearance document which, as in the case of the Letter of Credit document, may be an acceptance or rejection of the request

We describe this idea in the form of a partial function:

| reply : DocCode $\rightarrow$ DocCode

We would choose a partial function, even if all DocCodes had been pre-allocated, since some (probably most) document types for example, Invoices, Purchase Orders—will not require a reply.

## Document Life Histories

DocumentTypes can be characterised by more than just their form. Each DocumentType has a characteristic "life history" $^{7}$ . The "life history" concept is probably best explained by means of our (simplified) example Bill of Lading.

## Example

The life of a Bill of Lading begins when a shipping agent sends a Bill of Lading document into the system. At this stage the document will be partially completed—details of the shipment will be present but the Insurance Certificate, the Letter of Credit and the Customs Clearance associated with the shipment will not, normally, have been obtained. Although those details will not be present, the subscribers who will provide the information (the chosen insurance company and bank and so on) will be identified. The process which must be followed to complete the document and forward information (always in the form of standard DocumentTypes) forms the life history of the DocumentType in question.

In our case, when we have sufficient information, we will place a Request for Insurance Cover document in the mailbox belonging to the nominated insurer and await a reply in the form of an Insurance Certificate. Similarly, when we have sufficient information, we will place a Request for Letter of Credit in the chosen bank's mailbox. The process of passing the information to the shipper, the bank and customs agents in the importing country is similar. As soon as the necessary information has been collected, the appropriate standard documents will be placed in the relevant mailboxes.

Of course, not all Bills of Lading will follow exactly the same life history. For example, the chosen insurer may refuse to insure the shipment in which case there will be no point in applying for a Letter of Credit or for Customs clearance.

We need a way to describe the range of permitted life histories for a given document type. Let us consider a fragment of the form of a Bill of Lading. The document may have fields (MessIds) such as InsuranceCertificateNumber and InsuranceRejectionReason. The presence or absence of these completed fields within the document may be used to drive the particular life history model to be followed, i.e. if InsuranceCertificateNumber (possibly inter alia) is present then the criteria for the issue of a Letter of Credit Request is met and the request document is placed in the bank's mailbox. If, however, InsuranceRejectionReason is present a Bill of Lading Rejection document may be issued to the originator of the document.

We can, then, control the path through the potential life history models by describing the criteria for each piece of behaviour (which must always be characterised by the placing of a standard EDI document in the mailbox of some subscriber) in terms of its prerequisite fields within the document.

We will formalise this by defining a relation subdocs which describes the prerequisites for the issue of a given DocumentType from an existing document of given type. At this high level of abstraction, we do not define this relation deterministically, but content ourselves with placing generally applicable constraints on the relation. This constraint is that a document cannot generate the "issue" of a document unless the information within the issued document is present within the issuing document; and the issuing document also contains the address to which the issued document is to be sent (data cannot simply appear out of thin air). As an example of this, Letter of Credit Request is wholly contained within Bill of Lading and it would not be unreasonable to assume that one of the actions which may occur in the life of a Bill of Lading is the issue of a Letter of Credit Request.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$\begin{array}{l}\text{subdocs: DocCode} \leftrightarrow (\text{DocCode} \times \text{MessId})\\ \hline \forall c, d: \text{DocCode}; mid: \text{MessId} \bullet \\ c \underline{\text{subdocs}}(d, mid) \Rightarrow (form(d) \cup \{mid\}) \subseteq form(c) \end{array}$
</div>

In this specification, the MessId on the right of the relation simply represents the field within the document which contains the identifier of the subscriber to whom the message should be sent.

For document types which are simply passed from the sender to the recipient, such as Invoices and Orders, the only subdocument defined will be the document itself-of course, the intended recipient's address will be contained within some field within the document. The life history associated with such documents is clearly very straightforward. For more complex documents such as the Bill of Lading discussed above, there may be many subdocuments and, consequently, more complex life histories.

It is important to realise that just because two document types fulfil the requirements to be included in the relation subdocs, one is not entitled to deduce that that relationship is documented within subdocs. Definition of permitted life histories is a matter to be addressed in defining document standards. The implementor of the specification is, however, entitled to deduce that no member of the relation subdocs will exist which does not fulfil the predicate.

## The Objects within the System

We can now begin to describe the major objects in the EDI system. Firstly, we consider the subscribers to the system. In essence, we have chosen to model a one to one relationship between subscribers and mailboxes. That is, each subscriber has a mailbox, each mailbox is owned by a single subscriber. Each Subscriber will be an object in our system.

It is convenient to model a document as passing between the system and a subscriber. We model the case of a simple document passed from subscriber A to subscriber B as two transfers:

\- subscriber A to the system

\- system to subscriber B

Each document within the system will contain data which identifies the Subscriber with whom it is associated. In this specification we will use UmbrellaIds as a means of linking associated documents within an object which we call Umbrella. We will not need to worry about the characteristics of UmbrellaIds except to know that there is a special UmbrellaId NULL which we can use whenever we wish to introduce a new document instance into the system. In some circumstances, it may be necessary for one document to refer to other documents within the system. A good example of this is the document type Ship's Manifest which will, inter alia, contain references to a number of Bills of Lading.

Similarly, we will use the type SubscriberId to identify subscribers and, thus, mailboxes uniquely. In some document types, it is necessary to hold information about a number of subscribers. For example, an electronic Bill of Lading will contain details of the subscribers who will provide the Letter of Credit, Certificate of Insurance and so on. It is useful, at this high level of abstraction, to relax the strong typing available within Object-Z by allowing UmbrellaIds and SubscriberIds to appear as Messages. Formally, we say:

UmbrellaId : P Message

SubscriberId : P Message

NULL: UmbrellaId

We can model our system as messages in the form of standard EDI documents (instances of one of the defined DocumentTypes) being passed from Subscribers to Umbrellas and vice versa. We can define what we mean by a standard EDI document in the following way:

```txt
Document ____

Document Type
ref : UmbrellaId
info : P Info
sub : SubscriberId

dom info ⊆ form(code)
∀(f₁, m₁), (f₂, m₂) : info • (f₁ = f₂) ⇒ (m₁ = m₂)
```

By including the schema DocumentType in this way, Document inherits all its characteristics—it contains a DocCode for which a form is defined. The declarations ref and sub identify the Subscriber and Umbrella between which the document is being passed and info defines the data within the Document in the form of (MessId, Message) pairs.

The predicates place some constraints on what may be considered as an EDI document:

\- only fields which have been defined for documents of this DocumentType may be included within the info

\- no field may be duplicated within the document

In essence then, a document within our system will be associated with a Subscriber and an Umbrella, will contain a subset of the fields which have been defined for the standard DocumentType of which it is an instance and the contents of the fields will be valid within our definition of Info.

The first of our major active objects is the subscriber. Each subscriber may interact with the system in three ways:

\- the subscriber may send standard documents to other subscribers

\- the subscriber may take action resulting from standard documents which he receives:

\- if the document is not in the domain of reply, that is, "no action" is the only possible action, then the subscriber may Read the document and, thus, remove it from the mailbox

\- if the document is in the domain of reply, that is, the prescribed action is the sending of a specific standard document, then the subscriber may ReplyToMail. This results in the removal of the document from the mailbox and the issuing of the reply to the system

\- The subscriber may also interact with the system in a more passive way—the system may add documents to the associated mailbox at any time

So far, our formal specification has followed standard Z syntax. Although Document is an object, it is essentially inanimate. Subscribers, modelled as Subscriber objects are, however, active-and Object-Z offers constructs which allow us to specify such objects in an intuitively clear manner. Each Subscriber has a constant identifier sid (we will include a system level constraint later which ensures that these identifiers are unique) and a variable state which is composed of a mailbox (mbox) which may contain Documents. The only constraint on this state is that no Document may appear in the mailbox unless it is associated with the particular Subscriber. The special initialisation operation states that initially, the mailbox will be empty.

The state of the Subscriber may only be affected by means of the operations defined upon it:

\- the specification of the ReceiveMail operation defines the way in which a Document may be added to the Subscriber's mailbox. In line with our expectations, only mail for the particular Subscriber will appear in his/her mailbox.

\- the SendMail operation initiates each independent document transmission. The specification constrains the output document to be any valid Document, to be associated with the issuing Subscriber and to be associated with no existing Umbrella. Since this document transmission is independent, there are no associated alterations to the state of the Subscriber—the mailbox remains unaltered.

\- two mutually exclusive operations ReadMail and ReplyToMail are defined which remove Documents from the mailbox.

\- ReadMail affects documents within the mailbox whose DocCode does not appear in the domain of the function reply those Documents which, from the point of view of the communications system, do not require any further associated action. An Invoice is a good example of such a document type since the communications system will treat the Invoice and the Payment as independent transactions—indeed, either the Invoice or the Payment may be handled via some non-EDI mechanism. The result of the ReadMail operation is that a message is removed from the EDI Communications system.

\- ReplyToMail affects documents within the mailbox whose DocCode appears in the domain of the function reply-those Documents which, from the point of view of the communications system, require consequent associated action. A Request for Letter of Credit is a good example of such a document. Such a document cannot simply be removed from the system since doing so would leave another document in "limbo". The DocumentType associated through the reply function in this case would be a Letter of Credit. A ReplyToMail operation will issue to the Umbrella which initiated the incoming Document, a Document of the type of the required reply and remove the incoming Document from the mailbox (and, hence, from the system).

Subscriber

```txt
sid : SubscriberId

mbox : P Document

∀ d : mbox • d.sub = sid

INIT

mbox = ∅

ReceiveMail

Δ(mbox)
d? : Document

d?.sub = sid
mbox' = mbox ∪ {d?}

SendMail

d! : Document

d!.sub = sid
d!.ref = NULL

ReadMail

Δ(mbox)

∃ d : mbox • d.code∉ dom reply
    mbox' = mbox \ {d}
```

```python
ReplyToMail
Δ(mbox)
d! : Document
∃ d : mbox • d.code ∈ dom reply
    d!.code = reply(d.code) ∧ d!.ref = d.ref
    d!.subs = sid ∧ dom d!.info = form(d!.code)
    mbox' = mbox \ {d}
```

The other major active object within our system is the umbrella. An Umbrella will be created within the system every time an independent Document is issued by a Subscriber—that is, as a consequence of the SendMail operation (this idea will be formalised when we define the EDI Communication System object). The Umbrella will be “active” in that operations taking place within the Umbrella will guide a Document through its life history.

Informally, the Umbrella will, from time to time, examine the information held within it and the life history of the DocumentType which it represents. When sufficient information is available to issue a Document defined within the subdocs relation it may do so. Some of the issued Documents will generate replies (that is, their DocCode will be in the domain of the function reply) and the information contained in the reply Documents will be used to update the information held within the Umbrella, thus restarting the cycle. Eventually, no further documents may be legally issued by the Umbrella and no replies will be outstanding. At that point the life cycle of the document is complete. In the simplest cases such as those of Invoices and Orders, the Umbrella will be created with exactly sufficient information to issue a Document of its own type, a DocumentType whose DocCode is not within the domain of the function reply. Since no reply is expected and no further document may be issued, the Umbrella has reached the end of its life history and, effectively, the Document has been transmitted from its sender to its recipient.

Examining the formal specification below, we see two constants associated with each Umbrella-its ref which is a unique identifier (its uniqueness will be defined at the systems level) and its code. An Umbrella will have the same code as the Document which brings it into existence. We can model the internal state of the Umbrella as follows:

\- info (a set of valid (MessId, Message) pairs for the DocumentType in question

\- three sets of (DocCode, SubscriberId) pairs:

\- posted defines all Documents and their recipients which have been sent by the Umbrella in progressing through the life history

\- forposting defines all Documents and their intended recipients which may validly be issued at the current time by the Umbrella, but which have not yet been issued.

\- expected defines all Documents and their senders which are expected to be received as replies to Documents which have been posted

## There are some constraints on the state of the Umbrella:

\- No (DocCode, SubscriberID) pair may both have been posted and be available for posting; nor may we expect to receive any such pair which we either have posted or could legitimately post ourselves

\- Between them, forposting and posted contain details of all documents which could legitimately be issued on the basis of the information held within the Umbrella and the life history defined in the subdocs relation

\- We cannot expect a document which contains information which is not within the scope of the DocumentType represented by the Umbrella

\- The Umbrella may not contain information which is not within the scope of the DocumentType which it represents

The special condition INIT defines constraints on a new Umbrella. At this time no Documents have been posted by the Umbrella, nor are any expected. Only two operations can affect an Umbrella:

\- it may Receive a Document which must be associated by means of its ref and which must be expected (as documented in the set expected). The effect of the operation is to update the information held within the Umbrella and remove the expectation of the received document. Note that posted is not made available to be changed by this operation so, as with initialisation, forposting may be altered to reflect any additional Documents which may now be legitimately issued in line with the state invariant.

\- it may Post a Document which is documented within the set forposting. In doing so, it will transfer the reference to the Document from forposting to posted, determine whether a reply is expected and, if so, document that expectation.

Umbrella

```txt
ref : UmbrellaId
code : DocCode

info : P Info
posted, forposting, expected : P(DocCode × SubscriberId)

disjoint(posted, forposting, expected)
(posted ∪ forposting) = {(c, s) : (DocCode × SubscriberId) |
    ∃ m : dom info • (m, s) ∈ info
    code subdocs (c, m)
    form(c) ⊆ dom info}

∀(c, s) : expected •
    ∃ m : dom info • (m, s) ∈ info
    code subdocs (c, m)
dom info ⊆ form(code)

INIT

posted ∪ expected = ∅
ref ≠ NULL

Receive ____

Δ(info, expected, forposting)
d? : Document

∃(c, s) : expected • d?.sub = s
    d?.code = c
    d?.ref = ref
    expected' = expected \ {(c, s)}
info' = info ∪ d?.info
```

```txt
Post
Δ(posted, forposting, expected)
d! : Document
∃(c, s) : forposting; m : dom info •
    (m, s) ∈ info
    (d!.subs = s) ∧ (d!.code = c)
    (d!.ref = ref) ∧ (d!.info ⊆ info)
    ∀ m₁ ∈ form(c) • m₁ ∈ dom info ⇒ m₁ ∈ dom d!.info
    posted' = posted ∪ {(c, s)}
    forposting' = forposting \ {(c, s)}
    c ∈ dom reply ⇒ expected' = expected ∪ {(reply(c), s)}
    c∉ dom reply ⇒ expected' = expected
```

Finally, we define an object which represents the EDI Communications System as a whole and which describes the way in which the various active objects communicate with each other. The state of the system is described in terms of a set of Subscribers and a set of Umbrellas. The fields ref and sid uniquely identify Umbrellas and Subscribers respectively. Initially, there are no Subscribers and no Umbrellas. Initialised Subscribers can be added by means of the operation AddSubscriber provided that they are not already recorded in subscribers.

Four operations are defined which, together with AddSubscriber represent the only operations which may be observed from outside the system. The framing schema $\Phi$ Create Umbrella represents a hidden operation which can only occur as a part of another (unhidden) operation.

\- the Send operation is seen when a Subscriber sends an independent Document by means of the operation SendMail and, in parallel, an occurrence of Umbrella is created which makes use of the sent Document as input to its initialisation. The newly created Umbrella is now part of the system state.

\- in the Reply operation a Subscriber outputs a Document as part of its ReplyToMail operation and the Document forms the input to a Receive operation executed by an Umbrella

\- in the Receive operation an Umbrella outputs a Document as part of its Post operation and that Document forms the input to a Subscriber's ReceiveMail operation

\- RemoveMail operations may be observed whenever a Subscriber executes a Read operation

```txt
subscribers : P Subscriber
umbrellas : P Umbrella

∀ u, v : umbrellas • u.ref ≠ NULL ∧ u.code ∈ DocCode
    u.ref = v.ref ⇒ u = v
∀ s, t : subscribers • s.sid = t.sid ⇒ s = t

INIT ____

subscribers = ∅ ∧ umbrellas = ∅

AddSubscriber ____

Δ(subscribers)
s? : Subscriber

s?∉ subscribers ∧ s?.Init ∧ subscribers' = subscribers ∪ {s?}

Φ Create Umbrella ____

Δ(umbrellas)
d? : Document

∃ u : Umbrella • u∉ umbrellas
    u.init
    u.code = d?.code
    u.info = d?.info
    umbrellas' = umbrellas ∪ {u}

Send ≜ (s : subscribers • s.SendMail) || Φ Create Umbrella
Reply ≜ s : subscribers; u : umbrellas • s.ReplyToMail || u.Receive
Receive ≜ s : subscribers; u : umbrellas • s.ReceiveMail || u.Post
RemoveMail ≜ s : subscribers • s.Read
```

The examples and illustrations contained within our presentation of the formal specification have shown that incremental paper trail documents may be transmitted through the EDI system in the required manner. We have also endeavoured to include the very much simpler special case of documents which are intended for direct transmission from subscriber to subscriber. Clearly, our formal specification of the generic EDI communications system illustrated in Figure 4 would subsume the specifications of each of the simpler systems in Akerman and Cariero's classification.
