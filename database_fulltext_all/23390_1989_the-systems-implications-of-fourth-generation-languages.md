---
otero_id: 23390
otero_key: "ZP9YHB2U"
title: "The Systems Implications of Fourth Generation Languages"
authors: "John Crinnion"
year: "1989"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1989.9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Systems Implications of Fourth Generation Languages

John Crinnion, Department of Business Computing, The City University, London

Abstract: This paper discusses the need for changes in the generally accepted systems development methodologies in the light of the increased use of fourth generation languages and their associated techniques. It puts forward the opinion that an evolutionary development approach is the best way of obtaining the advantages of prototyping techniques, while at the same time retaining the benefits of a structured systems analysis and design methodology. The paper goes on to describe what is meant by an evolutionary development methodology, and identifies seven essential ingredients which must be present in such a methodology if the full potential of fourth generation advances are to be realized.

## Introduction

The purpose of this paper is to examine the changes that can be made to the way in which systems analysis and design is carried out, in order to take full advantage of the opportunities provided by the use of fourth generation languages and software.

The paper begins with a brief discussion of fourth generation language concepts, including the use of prototyping techniques. It then examines the traditional systems development life cycle, and considers the problems of using a prototyping approach within such a straightjacket. From this it concludes that a different method of systems development must be used if the benefits of both structured analysis and prototyping are to be realized.

One such approach is that of evolutionary systems development. The paper explains what an evolutionary development method implies, and lists what are considered to be the essential characteristics of this approach.

Finally, the place of an evolutionary development methodology within an organization's overall systems development environment is considered, and a migration path is suggested.

## Fourth generation languages

The term ‘fourth generation language’ (4GL), thought to have been coined originally by James Martin (Martin, 1982), has been in common use now for something like six years, but still remains somewhat difficult to define. One of the main reasons for this is that the impetus behind the development of 4GLs has come from the user and the software services industry, rather than as a result of some unified academic theoretical breakthrough. The drive has been towards the simplification and acceleration of the programming stage of the systems development process, and the solutions arrived at by different factions are known collectively by the generic name. These solutions vary considerably depending on the view of the problem taken by the different 4GL suppliers.

Figure 1 illustrates the three main directions from  
![](/api/attachments/ZP9YHB2U/fulltext/images/980baf79d23349a93ca04d906f3f4c4a54ff7dac153548aa532e8f904741b63e.jpg)  
Figure 1. Sources of fourth generation concepts.

which 4GL developments have come. The oldest source is the traditional 3GL (third generation language) environment, where specialist program generators and pre-processors have been in use for some time. Even in the late 1960s sort/merge generators were common in most systems development organizations, and by the mid-1970s simple screen formatters and report generators were becoming available (usually in the form of Cobol pre-processors). The next major contribution to the development of 4GLs came as a result of advances in the provision of database management facilities, in particular the increased availability of relational database management systems. This led to user demands for easy access to databases, for example for management information and decision support, and the resultant end-user query languages and data dictionary-centred facilities have become essential components in modern fourth generation environments.

The third area of origin is that of microcomputer software. During the early 1980s the increasing popularity of personal computers and the trend towards end-user computing were made possible by the existence of simple user-friendly computer software such as wordprocessors and spreadsheets. These packages, and more particularly the philosophy behind their production, played a major role in the continuing development of the fourth generation.

In all three cases the facilities being provided have been gradually expanded to create an environment in which the development of most common types of business software can take place.

Recently there have been more formal attempts to define the terms ‘fourth generation language’ and ‘fourth generation environment’. Grindley (1987), for example, has made the distinction between ‘pure 4GLs’, which he describes as ‘specification’ languages made up of non-procedural instruction sets, and ‘hybrid 4GLs’, which can consist of a number of pure 4GLs combined with and held together by a more procedural language.

The clear advantage of a pure 4GL is that because it is a specification language, in theory at least there is no need for a programming task; the systems analyst will create the specification and the necessary software can be generated directly from that. The disadvantage is that such a language can only address a small and very highly specialized area of development. For example, a screen painter may be considered to be a pure 4GL, a report generator would be another, and an end-user query language yet another. This means that in order to provide an environment in which a complex business system can be developed, a number of different types of pure 4GL must be integrated, and further procedural programming facilities must be provided. Such a package (Grindley's hybrid 4GL) is now more commonly referred to as a 'fourth generation environment' or 4GE (Martland et al., 1986).

Figure 2 illustrates a typical set of components comprising a modern fourth generation environment. At the centre is some form of data dictionary which maintains details of all data and program definitions. The environment usually includes a database management system (DBMS) which will be used as the filehandler for the business systems developed using the environment. The DBMS is, of course, also the software which holds and maintains the data dictionary. The three pure 4GLs are highlighted in the diagram, and the procedural supporting language is also shown. The box marked 'graphical design tool' represents a component which allows the capture of graphical models (for example data flow diagrams and entity models), built as part of the analysis and design process and incorporated automatically in the data dictionary. Modern data dictionaries of this type are able to provide more than a simple repository function: they can, for instance, provide checks on the completeness of the data definitions and on the correctness of program statements. They can even provide data validation checks on information being input to the database of a business system developed using the 4GE.

Perhaps the most significant difference between a suite of programs developed using a 3GL and one created using a 4GE is that whereas a 3GL program is compiled into executable code and can be run in the absence of the compiler, in most cases a 4GE program can be run only in the presence of the full environment. While such a program is running, the statements are individually interpreted before they are obeyed, and the data dictionary is consulted to ensure database integrity. This approach, while being one of the main strengths of the fourth generation concept, can also be considered as one of its main weaknesses. It means that at their current stage of evolution, most 4GEs are unable to handle the development of systems with critical response time constraints. In general (though there are a number of notable exceptions), 4GEs tend also to be restricted to the development of small and medium-sized systems, and are not considered suitable for use in major systems development projects. With the continuing improvements and extra facilities being introduced by 4GE suppliers, these 'weaknesses' are gradually being overcome.

![](/api/attachments/ZP9YHB2U/fulltext/images/0c863376e5fccdca0c118af8a604b49c229a28eddb03d8070a53d8779a5341f0.jpg)  
Figure 2. The fourth generation environment.

In summary, fourth generation environments provide a number of important facilities to the systems developer. Firstly they provide simple language statements which can be learnt easily and written quickly. Many of these statements are non-procedural, allowing the analyst to specify what is required rather than how it should be carried out. Each statement written may generate a substantial amount of code, thereby providing a great deal of functionality and a high level of productivity. One of the main reasons why 4GEs are so much more powerful that their predecessors is that in most circumstances they assume sensible defaults. For example, in a report generator one default assumption is likely to be that each page of the report is to be numbered; it is not necessary for the analyst to specify the fact. On the contrary the facility to override defaults and provide a highly customized product is a measure of the power of a 4GE

The compatibility of systems produced using the same 4GE on different types of hardware is also an important benefit; not only can databases on other machines be accessed and updated (perhaps via a data communications network), but also systems can be developed on one type of machine (say a PC), to be run on another. This is quite a common approach taken, particularly by users of FOCUS and ORACLE 4GEs.

Finally, many of the more advanced environments provide the facility to interface with DBMSs from a number of different manufacturers. This allows information to be extracted from a large corporate database, to be worked on using the 4GE in its own database and then transferred back. Again this approach is becoming common practice.

## Prototyping

It is, however, recognized by most authorities, (Martin, 1985; Ince and Hekmatpur, 1988; Watts,

1987), that the most important advantage of using a 4GE is that it changes the way in which we view the whole process of systems development. It does this by making possible the use of the technique of prototyping. Prototyping can be defined as:

building A PHYSICAL WORKING MODEL of all or part of the proposed system, and using it to help identify weaknesses in our understanding of the system requirements (Crinnion, 1989).

The major benefit from such an approach is that the user is able to see a version of the proposed system long before it has been fully developed, and is therefore able to correct any misunderstandings at an early stage. This picture of the system that the user gets is much clearer than can be obtained by examining the abstract graphical models provided by even the most modern form of structured systems analysis (Olle et al., 1988).

A number of attempts have been made to classify the different forms of prototyping (Floyd, 1984; Dearnley and Mayhew, 1988), but the two most important forms in common use are known as 'Rapid' and 'Evolutionary'. Rapid prototyping consists of building a very early prototype of parts of the system with the emphasis on speed of production. The quality of the coding is unimportant, because this version of the system will eventually be discarded and the real system will be built using structured methods; the sole purpose of the rapid prototype is to get user feedback on requirements and proposals.

On the other hand, the Evolutionary prototyping approach involves building a carefully structured working model of the core of the proposed system, with a view to revising and extending it rather than throwing it away. Obviously such prototypes takes longer to build than their 'rapid' counterparts, but because a 4GE is used they can still be assembled and adjusted relatively quickly. In fact, it is the facility to write quick and throw-away code, provided by the use of fourth generation software, that makes the technique of prototyping feasible (Grindley, 1987).

There are, however, at least two major problems associated with the use of prototypes within systems development. The most obvious of these relates to the rapid prototyping approach. This occurs when the user has been shown an acceptable working version of the system at a very early stage, and then must somehow be convinced that a proper implementation version will require a great deal of further development and will not be ready for several months.

The second problem relates to evolutionary development, and is concerned with the tendency shown by some prototypers to build their systems in an ad hoc way, allowing the reactions and suggestions of the users to supplant a properly structured analysis of requirements. Such an approach makes project management and control almost impossible, renders the success or failure of the project very much a matter of chance, and causes many data-processing professionals to doubt seriously the wisdom of evolutionary development. Evolutionary prototyping can take place successfully only within a strictly managed project environment.

## The traditional systems development approach

Even the most forward-looking of the structured systems development methodologies now in common use (e.g. SSADM, JSD, Information Engineering etc.), while making use of modern effective modelling tools and techniques, base their frameworks on the traditional systems development cycle. Each of the stages of this cycle — investigation, analysis, design, construction and implementation — are broken down into easily measurable units, and as a general rule each stage must be completed and signed off before the next stage can begin. This provides a clear demarcation between different processes, and allows for the use of specialist staff (e.g. programmers, analysts) for different stages. The reasoning behind the use of such a formal separation and ordering of tasks is that some of the later activities (in particular, programming) are complex, expensive and time-consuming, and the specification for these must be extremely accurate to avoid the need to write-off or re-work major pieces of code when errors are found.

There are a number of major benefits that structured systems methods have brought to the systems development process (Olle et al., 1986), but perhaps the most important of these is the introduction of 'logical' or 'conceptual' modelling techniques. For the first time the analyst had formal tools to help him to strip away the constraints of the existing physical system, and to enable him to analyse the user's business requirements before having to consider how they were to be carried out in the new system. Logical modelling techniques such as data flow diagramming, entity modelling and the construction of entity life history diagrams (Cutts, 1987), have revolutionized the analysis stage of system development. They have, however, also highlighted the need for a separate integral analysis stage, so their adoption has reinforced strict adherence to the traditional systems development life cycle (SDLC).

Many of the leading writers on systems development during the last few years have severely criticized this dependence on the SDLC, pointing out the restrictions it places on the flexibility of the development process (Martin, 1985; Sprague and McNurlin 1986). Grindley (1987) for example has shown how the different stages of the cycle were defined in the early history of data processing to overcome problems which to a large extent no longer exist. McCracken and Jackson (1982) warn us against treating the SDLC as an inevitable fact of life! These writers are particularly concerned about the attempt to treat prototyping as just another technique in the structured systems toolbox, and at the efforts of methodology suppliers to incorporate 4GE concepts without considering their implications.

As Figure 3 illustrates, the concept of prototyping cuts across the traditional approach of sequential stages; each individual prototype includes elements of investigation, analysis, design and construction. The definition of prototyping given earlier in the paper stresses that the purpose is to help in analysing the requirements of the system. However, as has just been pointed out, the analysis stage in structured development consists of a logical examination of requirements; no physical design has been considered, so the building of a physical model should not be possible! On the other hand, if prototyping is delayed until early in the design stage, much of the potential benefit is lost.

The use of prototyping for systems development has led in many situations to a change in the user's view of what is required; users are now able to go for a more advanced system with greater functionality and a higher level of user interaction. Fourth generation environments lend themselves particularly to the development of on-line systems, specializing as they do in dialogue design facilities. Also, many fourth generation systems, once they are built, become part of the prototypers' library of example systems, from which they can select an appropriate candidate to be tailored to fit any new system's basic requirements. This means that users are able, at a very early stage of the development, to view a number of options in prototype form and make decisions accordingly.

On the other hand, the use of a structured systems methodology can provide a much more controlled approach to a large development, and the logical modelling techniques lead to a much deeper understanding of the business, opening up a larger range of design and implementation options, and giving users a wider choice.

The problem remains: how do we take advantage of the mature, controlled, risk-minimizing approach of a structured systems methodology, and at the same time reap the benefits of a more quickly produced and more user-oriented system as provided using a prototyping approach?

![](/api/attachments/ZP9YHB2U/fulltext/images/9b655863d408ec068067be9055f2053a9c5e296900ae5b0575ab08c4d50bd754.jpg)

![](/api/attachments/ZP9YHB2U/fulltext/images/18d685b5f925eae1155a4329eb2d3882d143107f89b2e176ba6d8b02c7e2e254.jpg)  
Figure 3. Comparison of traditional and evolutionary development cycles.

## The evolutionary systems development approach

During the last five years many data processing organizations have attempted to resolve the conflict between structured systems analysis and design and prototyping, and a number of these organizations have written about their findings (Hyldon, 1985; Aitken, 1985; Travis, 1987); these references are only a small selection. Other more research-oriented organizations have tried by means of survey and interview to pull together the lessons learned from these attempts (Ince and Hekmatpur, 1988; Dearnley and Mayhew, 1988; London HCI Centre, 1988). The Department of Business Computing at the City University, London is one such organization, and the rest of this paper is a description of our conclusions on the future of systems development methodologies. Although almost half of the company methodologies examined could be described as 'Rapid' prototyping approaches, it seemed that the best aspects of both structured systems development and prototyping could be achieved only through the use of an evolutionary development methodology (EDM). The following discussion identifies what we consider to be the most important aspects of such a methodology.

## The overlap of the analysis, design and construction stages

One of the most important ideas in the evolutionary development concept is that prototypes must be delivered at a very early stage to the users. In the definition of prototyping examined earlier, it was stressed that the purpose of a prototype was to 'help identify the user requirements', and this identification of requirements is part of the analysis stage of the development. However, in many structured systems methodologies, the analysis stage involves identifying the complete 'logical' requirements before considering how they are to be physically implemented. This means that no prototype (which is by definition a 'physical' model) can be built until the start of the formal design stage. If analysis must be complete before design starts, then clearly the prototyping technique cannot be used to assist in the analysis.

In fact, a good prototype not only should check the validity and completeness of the analysis carried out earlier, but also can identify new logical requirements and implications.

Obviously some logical analysis must be carried out before the prototype can be built; it is after all a physical implementation of the logical requirements!

The argument is that the revisions to the prototype are likely to affect both the physical and logical elements, so if the full logical specification has been formalized and agreed, some of the benefits of using a prototype are wasted.

One approach put forward to facilitate this is the use of a hierarchical Business Function analysis to identify separate functional components of the system (Crinnion, 1989). This can enable the staggered development of the further analysis models, allowing one functional area of the system to be progressed into the design stage while others are still under analysis. This means that the first prototype of a small part of the system can be with the user often within a few days of the start of the systems analysis.

## Limited modelling of the existing system

A large number of structured systems methodologies incorporate a stage for the modelling of the existing physical system (usually in data flow diagram form). This can be quite popular with users, who can recognize their current working practices and can clarify any misunderstandings in the detail. However, it is often questionable as to how valuable much of this information is. For example, if the new system is to be very different from the old then many of the existing processes will be completely changed, rendering their detailed analysis almost worthless. (There is of course still a need to create a ‘logical’ model of the existing system.)

The argument in favour of retaining the modelling of the existing physical system is that the analyst can use it as the starting point for his analysis of the ‘logical’ requirements. There is clearly some justification in this, in that many of the users’ requirements are likely to be implicit in the existing system, and some may easily be overlooked should that system be ignored. However, the overhead involved in finding these few (albeit important) oversights can be excessive, and the suggestion is that by using an evolutionary development approach these facts can be obtained in another way.

The assumed necessity of modelling the existing physical system is part of the traditional view of the systems analysis process, where analysts are required to identify and record everything that the user knows about the system, then use that information for their analysis. It has long been realized that it is almost impossible to glean every piece of information about how users carry out particular tasks; some of that knowledge is the result of the combined experience of 20 years, and it would be arrogance to assume that an analyst could pick this

## up in a half-hour interview!

The traditional view suggests that analysts transfer all the knowledge about the existing system from the mind of the user into a specification to be used by themselves and their colleagues. They then continue with their analysis and design, and record the completed design in a specification for transfer to the mind of the programmer (see Figure 4). This transfer of information involves a massive overhead in specification, and opens up possibilities for misunderstanding and error.

analyst, with each bringing to the task a specialist knowledge and expertise, is an axiom of the evolutionary development creed. The approach has been formalized in a number of different ways, one of the most important being in the writings of Milton Jenkins (Neumann and Jenkins, 1982).

This much greater level of involvement for the user in the development process must be accompanied by an acceptance of some of the responsibility for its progress. The role of the user, for example in the testing and reporting back on prototype iterations,

![](/api/attachments/ZP9YHB2U/fulltext/images/d114827ec3ad1b89902a7ce4923bf3da8dff0c355594774f90ce15ca22a8b469.jpg)  
Figure 4. The transfer of information during the traditional systems development approach.

In the case of an evolutionary development approach there is no need for this complete transfer; the prototyper and the user are working in partnership on the analysis and design, so that the repository of detailed knowledge about the existing system can remain in the mind (and the documentation) of the user. When these details are needed they can be summoned at will, and only those pieces of information that are relevant need be put forward for examination.

It is easy to overstate this point of view; there must obviously still be ‘specifications’ produced as part of the analysis and design, but they require to be much less detailed and their purpose is to formalize the decisions and agreements on the scope and direction of the project. Nevertheless, if the detailed specialist knowledge of the users is not put to effective use throughout the analysis and design stages of the project, then many of the benefits of an evolutionary approach will be lost.

## Partnership and user responsibility

This idea of the analysis and design of the system being carried out in partnership between user and must be formalized, standards must be devised, and the adherence to rules and deadlines must be made to apply equally to both partners.

This inevitably means that the contribution required from the user must be planned for, estimated, costed and monitored in the same way as any other project resource. In the past, it has been common practice not to include user activity as a component in the development cost analysis or in the resource planning; in an evolutionary development such an approach would be unrealistic. As a result it may appear that the resource requirements for an EDM project are greater than those for a more traditional structured systems project. However, from many of the points already made, it can be seen that the opposite is likely to be true in most cases.

The major advantage of this extra user involvement during the development process is the very high level of commitment that it instils. Because the user is ‘responsible’ for the design, the system is much more likely to be implemented and accepted wholeheartedly. Again, this is a benefit that should spring from a well-structured evolutionary development approach, and failure to establish the user partnership concept could place it in jeopardy.

## Formalizing prototype boundaries

It is important that when a piece of the proposed system is identified as a unit of work to be prototyped, it should be marked and documented in terms of its scope and boundary. In an uncontrolled prototyping environment there are great dangers, both of duplication of effort and of uneven coverage of the system requirements.

For example, during the iteration of a particular prototype new ideas may surface, and before deciding to implement them prototypers must be sure that they are not being incorporated elsewhere in the development. In order to make the decision, the prototypers must have a very clear idea of the functions required from the unit on which they are working, and must have an appreciation of the rest of the system, in particular the parts of the system that interface with their unit. In a well-structured development methodology the availability of these two essential areas of information would be guaranteed by the methodology framework.

The methodologies examined seemed to provide little to support this requirement. In a methodology developed within the City University (Crinnion, 1989), the problem was tackled using a version of the data flow diagram (DFD) which separates the human and computer parts of the proposed system. Candidate prototypes are identified from this DFD, and marked accordingly (see Figure 5). The outline of each prototype is supported by the process descriptions of all the DFD processes involved, and similarly by the data definitions of the entity types mentioned within the prototype boundary. The analyst may also have details of early interviews conducted with the user, and is able to supplement these with further interviews before building the prototype. During the building process the analyst may be further constrained by the organization's standards on dialogue design.

The analyst will also be in constant contact with the project manager, and will be required to be involved in the walkthroughs for all other related parts of the system.

## Evolving levels of functionality

For a project to be managed successfully, control must be exercised over the stages within the project, and the progress of each stage and sub-stage must be carefully monitored. In the standard structured methodology approach, these stages are based firmly on those defined in the systems development life cycle, and the fact that the analysis and design stages of an evolutionary development project overlap can add to the complexity of the control problem.

The use of evolutionary prototyping techniques can also present problems in terms of estimation and monitoring: as yet, analysts have only limited experience of the use of these methods, and this is bound to be reflected in their forecasts and estimates. Also, so much depends on the understanding, the abilities and the attitude of the user. In theory, such a prototype can be set up quite early during the analysis stage, and still be undergoing revision by iteration almost until the release date. As suggested earlier, the fact that a prototype involves some investigation, some analysis, some design and some implementation, means that a form of concept other than a life-cycle stage must be used to split the prototype into measurable and therefore controllable components.

![](/api/attachments/ZP9YHB2U/fulltext/images/dd9932104c7456dd3376bafc4a50ad103551fd73895b46c371124027a3b58a59.jpg)  
Figure 5. Marking the boundaries of prototypes.

One approach put forward (Crinnion, 1989) is to make use of the concept of a 'level of functionality' within each prototype. Not only are there iterations, where corrections and users' suggestions may be incorporated, but there are versions, where these extra levels of functionality can be included in the prototype. Briefly, these levels can be considered to consist of:

\- an initial prototype (incorporating the human-computer dialogue and the basic functionality);

\- a completeness prototype (including the result of extra analysis for completeness, e.g. ELHs);

\- a controls prototype (incorporating the design decisions resulting from a controls audit);

\- a combination prototype (where the separate modules and prototypes are combined into programs, suites and sub-systems);

\- a performance prototype (where the data-accessing aspects of the programs are tuned to take advantage of the optimized database design).

Obviously, in small systems some of these levels can be grouped together, and in some particular instances all the factors relating to a later level may have been identified intuitively and included in an earlier version. The fact remains that the approach provides a vehicle for the rigorous estimation, monitoring and control of an evolutionary development process.

This is clearly not the only way in which evolutionary design components can be separated and classified. However, unless some such approach is taken, the project control benefits which should be inherited from the structured systems methodologies of the last decade will not be realized.

## Early implementation

In an evolutionary development approach, all opportunities for early delivery of all or part of the system must be explored. For example, the possible 'phasing' of the system delivery should be considered when the first discussions on the project are taking place. It may be that some parts of the overall system are almost integral, and can be implemented earlier than the rest of the project, with minimum overheads incurred. Alternatively, perhaps in a system to be introduced into a number of similar locations, some of the locations require only part of the complete system; again this sub-set of system functions could be completed and delivered early.

There is also another way in which the early delivery of a system can be brought about using an evolutionary development method. In some special circumstances, an early prototype with somewhat limited functionality can be released for use as a real system, and the later 'versions' can be treated as groups of amendments which may be issued as new releases. An example of the kind of situation in which this approach might be viable is one where there is no existing system, and where any information from a reduced form of the required system is better than no information at all. Nevertheless, such an approach should be treated with extreme caution.

## Flexibility and scalability

An evolutionary development methodology must be able to handle the development of a variety of different types of system, some heavily data-oriented, some with very complex processing, some with critical response-time problems, some with rigorous control requirements etc. It must also be able to tackle systems of different sizes, ranging from the relatively trivial two-person-day project through to the several-person-year major development.

This means that the various tools and techniques used within the methodology must have several levels of complexity, and the analyst is required to make decisions as to the level needed for each particular case. It must also be possible to leave out some of the stages in the full methodology framework when the system to be developed is small and relatively straightforward.

One of the key requirements of an evolutionary methodology is that it can be easily tailored. First, it may need to be adjusted to suit the type of organization or department in which it is to be used. Second, there will almost certainly have to be slightly different versions of the methodology for each of the 4GL environments of which the organization is making use. Third it must be adapted to suit each of the systems development projects to which it is to be applied.

## Conclusion

The problem faced by data processing managers responsible for providing systems development facilities for their organization is what kind and level of methodology to adopt. Should they opt for a large structured ‘cookbook’ methodology like SSADM or JSD? If so, how should the smaller and medium-sized systems be developed? And what about end-user development?

Evidence (Sprague and McNurlin, 1986) shows that many data processing departments are now providing three alternative types of systems development approach:

\- A structured systems methodology of the 'cookbook' variety for building large and complex systems.

\- A much simpler ‘toolbox’ type methodology for small and medium-sized systems (to be developed using 4GLs).

\- An Information Centre facility for end-user support.

The argument put forward in this paper is that in order to take full advantage of the potential of the fourth generation of software development tools, the approach adopted for small and medium-sized systems should be some form of Evolutionary Development Methodology. Furthermore, this smaller methodology cannot be the result of a series of simplifying adjustments to the larger one; the inherent concept of the traditional systems development life cycle must be jettisoned!

Eventually, as a result of improvements in 4GEs and CASE tools, the proportion of the number of projects being developed using such methodologies is expected to increase to the point at which an evolutionary prototyping approach becomes the most common form of systems development (IDPM Survey of Organizations, 1985).

## References

Aitkin, I. (1985) Tools to clean up a tarnished image. Computing Magazine (July).

Crinnion, J. (1989) A role for prototyping in information systems design methodology. Design Studies Magazine (July).

Cutts, G. (1987) Structured Systems Analysis and Design Methodology Paradigm.

Dearnley, P. and Mayhew, P. (1988) An alternative prototyping classification. BCS Computer Journal.

Floyd, C. (1984) A systematic look at prototyping. In Budde et al. Approaches to Prototyping Springer Verlag.

Grindley, K. (1987) Fourth Generation Languages, A Survey of Best Practice IDPM Publications.

Hyldon, M. (1985) Feeling the effect of a new life cycle. Computing Magazine (March).

IDPM (1985) Survey of DP organizations. In Fourth Generation Languages: A Survey of Best Practice Grindley, K. IDPM Publications.

Ince, D.C. and Hekmatpur, S. (1988) Software Prototyping in the Eighties: Information Technology Briefing Open University.

London HCI Centre (1988) Alvey Project MMI 151. Report of Prototyping Stream Queen Mary College, London.

Martin, J. (1982) Applications Development without Programmers Prentice Hall.

Martin, J. (1985) Fourth Generation Languages Prentice Hall.

Martland, D. et al. (1986) Fourth Generation Languages and Application Generators UNICOM Technical Press.

McCracken, D. and Jackson, M.A. (1982) Life cycle concept considered harmful. ACM SIGSOFT Systems Engineering Notes.

Neumann, J.D. and Jenkins, M.A. (1982) Prototyping, the new paradigm for systems development. MIS Quarterly (Sept).

Olle, T.W. et al. (1986) Information Systems Design Methodologies, A Feature Analysis IFIP North Holland.

Olle, T.W. et al. (1988) Information Systems Design Methodologies Addison Wesley.

Sprague, R. and McNurlin, B. (1986) Information Systems Management in Practice Prentice Hall.

Travis, B.J. (1987) Auditing the Development of Computer Systems Butterworths.

Watts, R. (1987) Application Generators using Fourth Generation Languages NCC Publications.

## Biographical notes

John Crinnion is currently a lecturer in the Department of Business Systems Analysis at the City University. Prior to this he worked for 15 years in various areas of data processing ranging from computer operations to systems development management, mostly within the public sector. He also taught systems analysis and design at the Civil Service College for a period of four years, and has carried out consultancy and training assignments in his specialist field of systems methodologies for a number of multi-national organizations.

Address for correspondence: John Crinnion, Department of Business Systems Analysis, City University, Northampton Square, London EC1V 0HB.
