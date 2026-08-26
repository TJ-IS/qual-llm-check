---
otero_id: 18304
otero_key: "AY9H5RYH"
title: "The applicability of software engineering in information systems development"
authors: "Chrisanthi Avgerou"
year: "1987"
journal: "Information & Management"
doi: "10.1016/0378-7206(87)90021-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Applicability of Software Engineering in Information Systems Development

Chrisanthi Avgerou

Information Systems Sub-department, London School of Economics, Houghton Street, London WC2A 2AE England

The development of computer-based information systems involves more than the building of a complicated software system because each information system is embedded in a social and organizational environment. Software Engineering, which relies mainly on engineering approaches and places emphasis on formal methods, is inadequate to steer information systems development projects. Particular advances in Software Engineering will be best utilized within a broad framework which is capable of dealing with both technical and social/organizational issues.

Keywords: Information systems development, Software engineering, Formal methods, Information systems methodologies, Socio-technical approach.

![](/api/attachments/AY9H5RYH/fulltext/images/c4073de19952761bf24d4a8c766a5fd8ea37d7ba234a5e7ee46ae1b62c40bc86.jpg)

Chrisanthi Avgerou is a lecturer in Information Systems at the London School of Economics. She obtained her first degree in Mathematics at the University of Athens and an M.Sc. in Computing at Loughborough University of Technology, UK. She started a career in computing in 1979 and worked first in a banking environment and later in a medical research computer centre. In 1984 she returned to the academic world to pursue research in information systems in social administration, their impact and the factors affecting their success. Her current research interests include also the utilization of information technology in developing countries.

## 1. Introduction

The development and use of information systems is recognized as a major research area and, within the International Federation of Information Processing (IFIP), technical committee TC8 was founded to deal specifically with aspects of information systems. However, there is no general agreement on what an information system is. The term ‘information system’ is used to mean a number of different notions. Hence it is necessary to specify our meaning before discussing issues concerning them. In this paper, an information system is defined as an open system capturing, contribute to the cognitive tasks in a social/organizational environment.

social/organizational environment.

Any organization fosters a variety of cognitive activities such as: operational, co-ordination and control tasks, decision taking, innovating, learning. Such activities are supported by formal and informal systems for communication and processing of information [10]. Formal means of communication, for example, written correspondence, are as important as informal conversation – one complementing the other in organizational activities. In the same way a formal, computer-based data-processing system is embedded in a complicated network of other formal and informal information handling procedures.

According to the perspective of the above definition the concept of information system is not equivalent to that of a computer system or to application software. Software isolated from the interaction with its environment cannot be regarded or studied as an information system. Social/organizational circumstances are crucially important because they determine the meaning of data and the usability of particular technical features. For example, the appropriateness of some data structure or the benefits gained from processes and time schedules that a computer application follows and imposes can only be considered in relation to organizational circumstances. In contrast to the software which can be assessed according to formal, technical factors, an information system can be assessed meaningfully only from its implications to the functioning of the organization in which it is imbedded.

Consequently, it is argued that the development of an information system cannot be reduced to a formal process for the production of a technological artefact. The possibility of application of formal techniques and tools for the development of information systems software needs to be considered within a broad framework that is capable of dealing with a multiplicity of technical and organizational issues, both formal and informal.

## 2. The Concept of Information System

Land and Hirschheim [9] describe the historical evolution of the meaning attached to information systems from their having for long been considered technical systems to their being recognized as technical systems with behavioural and social implications. The same authors argue that although this shift is a step forward, it is not good enough to avoid future information system development failures. They consider information systems to be: social systems which rely to an increasing extent on information technology for their function. Nevertheless the technology is never more than a component of the information system. Hence, the emphasis on social systems is of paramount importance.

However, the acceptance of such a definition for information systems is still far from universal. A great part of the scientific community conducting research in information systems does not consider behavioural and social issues as relevant aspects of its work. The proceedings of an international conference organized under the title: “The Theoretical and Formal Aspects of Information Systems 1985” [21] provides evidence of current research in information systems. Both panel sessions of the conference (“Foundations of information systems” and “Future of information systems”) almost exclusively addressed technical topics like logic, databases, structural growth of logical tools, the theory of Software Engineering and problem solution development using General Net Theory of Petri.

Mylopoulos offers an explanation to this variety of technical orientations to information systems research based on the observation that all information systems scientists focus on carefully narrowed research areas. Consequently, the question raised is “should there be a broader research area which covers and has broader goals than these areas and is concerned with the design of information systems?” (ibid.)

Different answers to this question lead to different ways of developing and treating computer-based information systems in organizations. Indeed there are methods which place emphasis on social/organizational aspects of the information system [8]. On the other hand, the design of information systems has, in many cases, been considered as a purely technical task, aiming at optimal (in terms of efficiency) computer technology applications. Software Engineering – the discipline of organizing and controlling the production of software – is such an example. It is, therefore, worth examining the relation of Software Engineering to the task of information systems development in the perspective of the above definition of information systems.

## 3. Software Engineering and Informatics

Software engineering, as defined by Lehman [14], is concerned primarily with the design, control and support of software development and evolution processes and it forms the basis of Software Technology.

The essence of software engineering is the formalization of software development and evolution. It aims to replace the ad hoc selection of tools and methods which is currently practised with a model for a systematic decomposition of the complicated process for developing software. Ideally it starts with an abstract model, which is the specification of the system to be developed and which can be validated with a formal theory. This is decomposed through a process of transformations towards more detailed specifications until a computer-executable system is produced. Each transformation step is formally verifiable for equivalence between the initial specification and the resulting refined specification. In addition the output specification of a transformation step is horizontally verified for consistency and completeness in relation to the features that were to have been added, or the problems that were to have been resolved in the current step [13].

The above model is meant to be an ideal in the sense that a number of practical problems restrict its applicability. For example, it is recognized that a creative aspect is involved in the transformation steps; also that for many applications formal theories providing a formal initial conceptual representation do not exist, and that this prohibits rigorous verification at the first step and increases the possibility of undetected errors carried through the transformation process. Despite these limitations, which have been recognized by software engineers [20], software engineering seeks the improvement of the reliability and productivity of software by formalizing its evolution process and is committed to the search for notations and methods with a sound mathematical basis.

Considerable research effort is directed towards this end. In the UK, a Software Engineering Strategy, part of the Alvey programme for collaborative research and development is aiming to the realization of the idea of Information Systems Factory – a highly productive environment for high quality products.

Current activities focus mainly on the development of Integrated Project Support Environments (IPSES) which are computer-based sets of facilities for the support of software production [15]. A great deal of research is concerned with formalisms and, in particular, the development of formal specification languages. More recent research efforts deal with activities for converting initial fuzzy requirements for a computer application to formal specifications of machine-executable functions [1].

Terminology such as Information Systems Factory and Information Engineering suggests the aim is to improve the production of information systems in order to support, for example, a project like the computerization of a hospital [1]. However, there is little empirical evidence of the application of facilities that have been developed so far from these efforts. Most publications reporting on the use of formal facilities refer to software types like compilers, operation systems and editors rather than information systems. For example, the Vienna Development Method (VDM) [7], which is probably the best-known formal specification language, has so far been applied mainly to the development of computer language compilers, although it is believed that in the nineties it will constitute a powerful method for a variety of software development projects.

The perspective of software engineering can be contrasted to that required for the study of information systems. The Scandinavian trade-union and user-participation-oriented school of information systems defines informatics as the science that has, as its domain, information processes and related phenomena in artefacts, society, and nature.

Nygaard [18] writes that informatics have the following four aspects:

1. Phenomenology: The empirical study of phenomena – their identification, observed behaviour, and properties.

2. Analysis: Comprehension and explanation of phenomena in terms of an underlying theory. Identification of important properties and concepts; relations between properties and concepts, description and anticipation of behaviour.

3. Synthesis, construction, technology: Knowledge organized for the purpose of interfering with, constructing, or generating phenomena.

4. Multiperspective reflection: The consideration and examination of concepts and phenomena at the same time – or alternatingly – from the perspectives of more than one science, or from more than one perspective within the same science. The study of how changes introduced according to one viewpoint affect properties of the phenomena when regarded from another viewpoint.

The multidisciplinary approach that informatics, as defined above, introduces, requires various methods – some of which can be formal – to support the development of information systems. The success of the construction of a computer-based information system, which is the core of the development process at the present time, depends significantly on organizational as well as technological factors. The development process often begins only with some vague expression of dissatisfaction from the functioning of the organization and this makes necessary an inquiry as to whether a formal information system can indeed alleviate it. Such investigation of so-called soft, ill-defined problem areas can be supported with scientific methods, but the specialist's main role is to intervene and assist the organization itself to reach feasible decisions for its problems [3]. As there are only rarely formal models on which to base the requirements specification (and often for only a few parts of an information system), the development process relies heavily on capturing the knowledge of the people in the organization, their habits and demands, through communication between developers and users. More than that, since computer applications are considered as components within a social environment, their development does not aim only at a technically efficient system but at satisfactory and acceptable working conditions as well [16].

Similarly, the nature of the implementation task requires a strategy to cover technical as well as organizational aspects; for example, where there is resistance to change, it is often the reaction to a new formal information system $[6]$ . Also, the maintenance (or evolution, depending on the model followed by the development process) of a computer-based information system involves both social/organizational and technical processes. It is a process of adaptation or rejection driven by needs for technical corrections and improvements and demands for alterations and enhancements.

## 4. Software Engineering for Information Systems Development

## 4.1 Limitations

Information systems as an area of scientific concern has emerged because of the enormous opportunities for handling organizational data that computer technology, hardware and software, have offered in the past three decades. Software reliability and productivity – issues which software engineering addresses – are important factors in the success of information systems. Reduction of software development and maintenance costs and decreases in the probability of software errors contribute to the cost-effectiveness of an information system as a whole.

Formal, mathematics-based theories have been the most significant ways of improving the efficiency of computers as instruments for data processing. It is reasonable to expect that the continuing efforts to build and integrate formal tools for software production and to develop theories for formal expression of application domains can further increase the efficient use of information technology.

Improvements in software reliability and productivity by introducing organization and discipline in development projects, the aim of software engineering, are very much needed in the case of information systems development. Most currently practised methods include guidelines on project discipline. For example they give advice for proper documentation update procedures and prompt for the correction of errors not only at the level of program code, where they are often discovered, but at the level of specification where they are first introduced. Nevertheless, such principles are cumbersome to follow within the ad hoc combination of techniques comprising the current methods and under the pressure of the organization's work-load, they are frequently violated. It can therefore be assumed that methodical organization of development projects with the support of automated tools can have a significant impact on the cost-effectiveness and the quality of the produced software.

However, the emphasis that current software engineering research gives to formalisms restricts the relevance and applicability of the methods developed to information systems. It is unlikely that a formal theory can describe organizational behaviour. Computer-based information systems are now a complex of components, some of which are mathematical models, some of which need to capture empirical knowledge, and others which need to support particular social/organizational creative habits. Only for some of these components can software engineering advances, which require a formal basis, provide their promised benefits.

Lehman [12] classifies software types according to the relation with their environment:

S, if they are determined by their specifications and once released operate unaffected by their environment.

P, if they have to meet the needs of an application; as the requirements of the application cannot be once and for ever specified they must be altered to follow the changes occurring in the application area.

E, if they are embedded in the environment of the problem they address, they have no intrinsic boundaries, their operation has an impact on the application area and, consequently, they evolve to meet the changed requirements.

Examining the evolution process of E type software Lehman writes that, because satisfaction in usage is the main criterion for such systems' acceptability and the requirements specifications are inherently incomplete, the development and evolution tend to divert from the linear ideal model and become iterative. It relies on user involvement for the specification of the requirements. In this case the assessment of the released system and its validation is more relevant than formal verification.

By the given definition, information systems belong to the E category. Some components may be S programs and others P programs, but, as subsystems of organizational activities, information systems interact and evolve with their environments. There is still a need to put discipline into the evolution process, perhaps more than in the cases of other types of software production, but formal methods are not the key elements in the information systems evolution process.

Downes [4] argues that fully a formal development process is neither practical nor desirable. She explains that apart from the lack of formal models capturing the richness of the application domains, there are two other reasons for non-formality: first, there is a need for interaction with the informal world of human behaviour, and second, formal methods are often too expensive – less rigorous techniques being more cost-effective.

It needs to be added that software reliability and productivity, which is the aim of formal methods, is not synonymous with the cost effectiveness of information systems. The reduction of the cost of producing and correcting software is only one factor of cost-effectiveness. It should be considered in parallel with the benefits gained from and the risks taken by the operation of the resulting information system. These benefits and risks can hardly be seen as a straightforward outcome of the computer application and are very difficult to measure. They depend on user behaviour and reactions which are not taken into account in software engineering. In fact such factors have no place within the rational framework of the sciences that contribute to formal models and engineering. For example, internal organizational, political or cultural circumstances, which can hardly be considered by formal techniques, may affect the performance of the social environment of a new information system and often counteract the benefits of the software built on the basis of optimizing models of organizational behaviour.

## 4.2 Undesirable Implications

There are, indeed, some undesirable implications from the emphasis on formalization in information system development. It discourages user participation in the development process and it causes overconfidence in the technology with neglect of social/organizational issues.

The participation of users in a formal development process becomes difficult. Formal notations in the descriptions of systems specifications are important in software engineering. Both ideas of executable specifications and formal verification are based on notations and methods with a mathematical basis. Many of the currently applied methods which follow the life cycle model use diagrams as description tools to express the structure of the application system. Such graphical representations are not meant to be used as the developers own work techniques, they provide a basis of communication between users and analysts. When user monitoring is the most significant validation process, such graphical models, although not the most rigorous possible, at present are effective means for designing reliable systems. Graphical notations are not considered adequate formal representations for software engineering because they do not provide the basis for verification; they are informal. However, replacing them with notations suitable for verification through the use of mathematical techniques will restrict the users' contribution – which is of major importance – to the validation process. Tse [22] has examined the currently applied development methods with regard to comprehensibility and verifiability. He suggested that the methods with greater verifiability are less comprehensible and vice versa.

Some formalists seem to suggest that it is in the users' best interests to master the notation to the degree necessary to understand the system specification [20]. This idea may be possible to realize with some users who are committed to the system under development but it certainly excludes many categories of end users. For example it has been indicated that trade unions are often, despite their willingness to get involved in the introduction of information systems in their work environment, unable to contribute genuinely to the development process because of their inadequate technical knowledge. Educating some shop stewards on technical design issues in order to be able to make feasible alternative proposals has been tried in Scandinavia but it did not solve the problem of genuine participation from all interested parts [5].

In many cases user training in formalisms may not be applicable. For example, it is probably unacceptable to demand managers to understand formal methods as a means to build cost-effective decision support systems. Building decision support systems often involves artificial intelligence techniques as well, in order to incorporate the decision-makers heuristics; it seems unreasonable to expect the users of such applications to have skills for understanding the variety of representations that a still immature discipline experiments with.

Another problem stemming from the application of software engineering in the development of information systems is that development projects which give emphasis to formal methods tend to neglect social/organizational issues because they rely on technical experts with little understanding of other aspects of information systems. Software engineering expertise requires long-lasting training in mathematical and technical issues. Contemporary curricula for computer science devote hardly any time to raising awareness on issues of organization theory and sociology. In fact many methods and approaches of the non-engineering disciplines involved in informatics are considered as non-scientific by people trained in the physical sciences' paradigm. Even scientists who appreciate the importance of social aspects of information systems are reluctant to depart from the traditional physical sciences' research and practice methods [17].

Without the ability to comprehend and tackle organizational aspects of information systems, developers often try to overcome the problems caused by reinforcing the immunity of their products with even more rigorous formalisms.

When reliance on technologically proved systems is overestimated, it is possible that the organizational ability to cope with unexpected events is weakened. Even in automated control systems whose correctness can be mathematically tested during development, confidence in rigorous design and fault-adjusting processes should not undermine organizational capability for problem solving. It is human endeavour that ultimately copes with unexpected errors; formalisms that prohibit or obscure human creativity can have catastrophic effects. In the case of information systems, reliance on additional formal methods as a remedy to their inherent imperfections is damaging if it underestimates the importance of the social/organizational system, and weakens its dynamic functioning. For example, in the case of computer-based information systems which support the operations of a social security organization, formal software engineering methods and tools for quick and robust fixes of software malfunctioning without disastrous effects on other parts of the software performance are obviously very important. However, it is more important to preserve the ability of the personnel to understand and control the service they are responsible to administer – for example to be able to recognize errors in the system's functioning and to continue functioning without the support of the system in case it is needed. In other words it is vital to create a work environment where responsibility lies on the human actors who should feel that information technology supports their functioning rather than obscures it.

## 4.3 Applicability

In order to advance the applicability of Software Engineering on information systems development and to avoid non-desirable effects, Downes suggests $[4]$ an evolutionary route from methods and languages without formal foundation (like SSADM and COBOL), to a formal paradigm which recognizes the need for human interaction. There are also efforts to build formal tools to assist such a transition. For example Tse $[22]$ proposes a category-theoretic approach for formal refinement of methods like DeMarco or Jackson. He suggests that a system developer can choose a method with consideration to the characteristics of a particular application and its environment. The application of such a formalism can then help him/her to visualize the internal structure of the system, assemble or refine subsystems, and verify the consistency and completeness of a design.

Many current IPSE projects follow this approach [2]. Logica, a major firm in the UK software production and consultancy industry, which is obviously very keen in ensuring the best use of advances in software development facilities, has adopted a similar policy [19]. Instead of searching for Software Engineering tools and methods capable of satisfying the requirements of the variety of their projects, they decided to establish a mechanism to keep their key staff aware of the major technological advances and to leave decisions concerning their application in particular projects to them. The company provides training and information on Software Engineering advances and is prepared to support their application in projects for which they seem suitable. More importantly, the new facilities adopted are integrated with established ones; in this way the methods used by the company evolve by taking into account the latest technology.

Land and Somogyi discuss the applicability of Software Engineering and suggest that there is a need for software engineering support systems which are very flexible and permissive in the way they are used, and which are designed as decision support systems rather than aiming at a software factory environment [11].

It is also reasonable to expect that in some cases the problem of limiting the ability for effective user participation that formal methods cause can be resolved by advances in this same area. If the application of formal processes and automated tools can result in the development of operational systems quickly and relatively inexpensively, user participation in the design process is not as important for a successful information system as it has been for development projects based on the life cycle model. The users do not need to monitor the design process in order to make sure that the resulting system will be satisfactory. They can express their requirements simply in terms of the desirable features of the computer based system in natural language or other ways appropriate to the application, and subsequently require modifications of the operational systems presented to them until a satisfactory system is built. Within such a model the development process becomes a series of changes, enhancements or even replacements of operational information systems, released for assessment. The design task for each release could be carried out solely by technical experts, but care will still be needed to ensure that users requirements are understood and appreciated to avoid wasting resources and frustration from misunderstanding.

While such approaches make possible the contribution of Software Engineering to the improvement of the information systems development process, it cannot be overemphasized that they do not make Software Engineering an adequate platform for information systems development. In order to deal with information systems in contemporary organizations it is necessary to search for knowledge in and adopt methods from social sciences as well. Consequently, a major task for those responsible for the development of information systems is the selection and integration of methods from different domains and diverse epistemological assumptions. Therefore the task of organizing and steering the development of information systems requires generalist skills rather than narrow technical expertise.

Developing such skills is by no means an easy task under present circumstances. It needs a long educational process with a careful balance between state of the art information technology, including its scientific and logic fundamentals, and topics from a variety of disciplines as indicated by Nygaard's definition of informatics. Specialization may be a powerful way to advance technology but it requires generalist skills to disseminate their benefits.

## 5. Conclusions

Because in most non-trivial information systems the technology complements social activities rather than substituting for them, their development involves both the construction of a complicated technical product and the planning and realization of organizational changes. Such an intervention process cannot be adequately guided by principles of engineering.

Consequently this paper has argued that:

a. Software Engineering, drawing mainly from engineering and formal sciences, focuses on the construction of software as a technical product and is therefore inadequate to steer the information systems development process.

b. The emphasis on formal methods in order to produce cost-effective and reliable software may have undesirable consequences on the resulting organizational performance; it discourages the involvement of users in the development process and tends to overestimate technical efficiency.

c. Advances in Software Engineering and other fields of information technology offer significant potential for improvements in the development of information systems of contemporary organizations. However, benefits can be realized only if methods and tools are selected, organized and applied within a framework broad enough to address social/organizational circumstances.

Indeed, the discipline of developing and using the information systems has still to develop such a framework by reconciling paradigms from both social sciences and technologies. It must recognize the importance of non-measurable, non-formalizable aspects of social activities and find ways to account for them. Software Engineering advances will be best utilized if they are placed within such a perspective.

## References

[1] Belady, L.A. (1986) Software Engineer, the System Designer, in Barnes D., Brown P., Software Engineering '86. Peter Peregrinus, London.

[2] Barnes, D., Brown, P. (1986) Software Engineering '86. Peter Peregrinus, London.

[3] Checkland, P. (1981) Systems Thinking, Systems Practice. John Wiley and Sons, London.

[4] Downes, V.A. (1986) Non-Formal Approaches to the Software Engineering Process. Proceeding of BCS, Software Engineering Specialist Group Conference on Complementary Approaches to the Software Engineering Process.

[5] Friedman, A., Cornford, D. (1985) Strategies for Meeting User Demands: An International Perspective. Proceedings from Working Conference on Development and Use of Computer-based Systems and Tools, Aarhus, Denmark, 19–23 August 1985.

[6] Hirschheim, R.A., Land, F.F., Smithson, S. (1984) Implementing Computer-based Information Systems in Organizations: Issues and Strategies. Proceedings of INTERACT '84, IFIP conference on Human-Computer Interaction, London 4–7 September. North-Holland Publishing Company.

[7] Jones, C.B. (1986) Systematic Software Development Using VDM. Prentice-Hall Intl. Englewood Cliffs NJ.

[8] Land, F.F., Mumford, E., Hawgood J. (1980) Training the Systems Analyst of the 1980s: Four Analytical Procedures to Assist the Design Process, in Lucas et al., The Information Systems Environment, North-Holland Publishing Company.

[9] Land, F.F., Hirschheim R.A. (1983) Participative Systems Design: Rationale, Tools and Techniques. Journal of Applied Systems Analysis, Vol. 10.

[10] Land, F.F. (1985) Is an Information Theory Enough? The Computer Journal, Vol. 28, No. 3.

[11] Land, F.F., Somogyi, E. (1986) Software Engineering: The Relationship Between a Formal System and its Environment. Journal of Information Technology, Vol. 1, Nr. 1.

[12] Lehman, M.M. (1981) The Environment of Program Development and Maintenance – Programs, Programming and Programming Support. Reprinted in Wasserman, A.J. (ed.) Software Development Environments. Computer Society Press, New York.

[13] Lehman, M.M. (1985) Program Evolution, in Teichroew D. et al. (ed.) System Description Methodologies, Elsevier Science Publishers B.V.

[14] Lehman, M.M. (1986) Advanced Software Technology - Development and Introduction to Practice, in Kugler, H.J. (ed.) Information Processing 86, IFIP Congress Proceedings, Elsevier Science Publishers B.V.

[15] McDermid, J. (1985) Integrated Project Support Environments. Peter Peregrinus, London.

[16] Mumford, E., Weir, M. (1979) Computer Systems in Work Design – the ETHICS Method. Associated Business Press, London.

[17] Mumford, E. et al. (1986) Research Methods in Information Systems, North-Holland, Amsterdam.

[18] Nygaard, K. (1986) Program Development as a Social Activity, in Kugler, H.J. (ed.) Information Processing 86, IFIP Congress proceedings, Elsevier Science Publishers B.V.

[19] Southwell, K. (1986) Introducing Software Technology: Project SESAME and its Lessons, in Barnes, D., Brown, P., Software Engineering '86. Peter Peregrinus, London.

[20] Stenning, V. (1986) Software Engineering: Present and Future. Proceedings of BCS, Software Engineering Specialist Group Conference on Complementary Approaches to the Software Engineering Process.

[21] TFAIS'85 Conference Proceedings, April 15–18, Sitges (Catalonia).

[22] Tse T.H. (1986) Integrating the Structured Analysis and Design Models: A Category-Theoretic Approach. Technical Report, Centre of Computer Studies and Applications, University of Hong Kong.
