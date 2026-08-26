---
otero_id: 19183
otero_key: "BHD46RGK"
title: "Expert systems reliability: A life cycle approach"
authors: "N. Ashrafi; J.-P. Kuilboer; J.M. Wagner"
year: "1995"
journal: "Information & Management"
doi: "10.1016/0378-7206(95)00004-g"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Techniques

# Expert systems reliability: A life cycle approach

N. Ashrafi \*, J.-P. Kuilboer, J.M. Wagner

Dept. of Management Science and Information Systems, College of Management, University of Massachusetts, 100 Morrisey Boulevard, Boston, MA 02125, USA

## Abstract

Over the past few years, the application of expert systems has moved from the domain of toy systems and menial tasks to areas where complex systems perform critical tasks. However, the acceptance of expert systems for practical use has been slow. This paper argues that one of the reasons for this is that insufficient attention has been directed at ensuring the correctness and reliability of expert systems in the early phases of development. This article then discusses a life cycle approach to identify and reduce the different types of reliability problems inherent in developing expert systems.

Keywords: Expert system reliability; Expert system development; Life-cycle; Software engineering

## 1. Introduction and background

As the field has matured, expert systems have moved away from specific academically-oriented efforts toward more complex managerially-oriented corporate issues $[19]$ . Expert systems (ES) have now improved to a point where they can be used in complicated, realistic, and serious tasks. ES have been or are being developed in such varied fields as medical diagnosis, equipment repair, computer configuration, chemical data interpretation and structure elucidation, speech and image understanding, financial decision making, process control, mineral exploration, and military intelligence and planning $[13]$ . In all of these applications ES are intended to solve complex and ill-structured problems quickly by imitating the decisions of an expert.

One of the often stated advantages of ES is the reliability of their decisions. They are, after all, computer programs. Hence, when presented with the same evidence, the same decision should result regardless of time or any external factors. ES are intended to provide feasible solutions to problems that require human expertise and skill plus the consistency, speed and infallibility of artificial reasoning. They are supposed to guard against the errors and biases to which humans are prone to, due to fatigue, lack of attention, emotions, and other sources of bias.

However, as ES move from the laboratory into real-world applications, concerns have grown about their reliability. Coats $[6,7]$ discusses a number of problems, including reliability, that have been encountered with the application of ES in the area of financial management and concludes that: “... an objective look at the accumulating disillusionment of users, developers, and investors who have firsthand experience with trying to launch financial expert systems for commercial use (shows) there are serious problems with methodology, code, knowledge acquisition, and validation". Vinze et al. [28] states that the need for validation (one part of ensuring the reliability of ES) "explain(s) the relatively small number of documented successful knowledge-based system implementations". Hollnagel [14-16] argues that ES are unlikely to become an integral part of the decision making mechanism in any organization until they are proven to be highly reliable, so that they can be used with "reasonable confidence".

The field of (conventional) software engineering has developed formal methods to be used throughout the life cycle of system development to enhance (though not guarantee) system reliability. O'Keefe et al. [20] state “the purpose of the life cycle is to allow the production process to be carried out in a rational, disciplined, effective, controlled, and uniform way, going beyond the peculiarities of individual skill and proficiency.... The definition of the life cycle is a key point differentiating craftsmanship from engineering [20]”. As is increasingly recognized in the literature, reliability management efforts must extend throughout the life cycle. For the purposes of this paper, the life cycle will consist of the stages of (1) requirements specifications, (2) design, (3) coding, (4) testing, and (5) maintenance.

Most of the work addressing ES reliability focuses on verification and validation (V and V), which are done only in the testing phase and occur only after the system has been developed. Even then O'Keefe et al. [20] report that validations of ES, at their best, "have been ad hoc, informal, and of dubious value". The narrowness of the work on ES reliability is evidenced by a search of the UNCOVER database (for the years 1988 to the present). Over thirty citations were found dealing with verification or validation (V and V) of expert systems. On the other hand, only eight citations were found in response to the keywords "reliability" and "expert systems", and half of these were about ES that had been constructed to examine the reliability of other systems.

This paper argues that the field of ES development can profit from a wider view of reliability efforts, one that extends beyond only V and V. Guida and Tasso [12] also allude to problems of reliability by saying the development of ES is “more like handicraft than engineering, and it lacks several of the desirable features of an industrial process such as reliability and quality assurance”. To move beyond “handicraft”, system developers must be concerned with reliability issues throughout the development process. By taking a wider life cycle approach, we see that each stage will have its own reliability issues, and that producing a sufficiently reliable product will require recognizing and confronting the reliability issues at each stage. With its focus on reliability issues throughout the development process, this paper is primarily intended for the audience of ES developers. However, since reliability is a major concern of those who employ ES, this paper should be of interest to ES users as well and should help these users to become more educated “consumers”.

As traditionally presented, the life cycle consists of a nicely ordered sequence of activities. Obviously it has been recognized that software development does not proceed linearly through these stages, and that much “looping” is required. Nonetheless, by separating development activities into these general categories, reliability issues that may previously have been ignored now become obvious and strategies for ensuring these often overlooked reliability issues can be identified.

## 2. Software reliability

As software applications become more complex, the issue of their reliability is taking on a greater importance. In recent years, there has been considerable efforts to define, measure and manage software reliability. For software systems, reliability is defined as the probability that a software system will perform in the user environment without failure for a period of time $[18]$ . Failure, can be defined as observable departure from the required function, when the system is in operation. Reliability is a subset of a broader concept: quality. Quality software is also correct, efficient, portable, reusable, and maintainable. Some would also add that it can be produced on schedule and within budget [18].

Unreliable software systems are not commercially viable. However, no piece of software can be 100% error free. Programmers and others make errors at all phases of development. These lead to faults that can cause failures. Quantitative models have been developed to measure software reliability, but these by themselves cannot improve software reliability. However, these models allow the determination of reliability levels during testing and better management of project resources [18].

High development costs have intensified the pressure for managing and controlling software reliability. In recent years, reliability has been recognized as a source of market advantage. There are three approaches to the management and control of software reliability: fault correction, fault tolerance and fault prevention. A focus on only V and V leads to a fault correction approach. This paper advocates that the best approach to managing reliability is fault prevention, and that examining reliability issues throughout the life cycle approach provides a good start at fault prevention.

Fault correction is mainly addressed by software testing: that is “the symbolic or physical execution of a set of test cases with the intent of exposing embedded faults in the program $[9]$ ”. For any system, testing must be performed. However, this testing is performed only after software development is completed, and at this point even once we know that software contains faults, we generally don’t know their cause, their severity, nor how difficult it will be to correct the problem. Also, exhaustive testing of a large software system is so time consuming and so expensive that it is rarely practical (for more refer to Beizer $[3]$ ).

Fault tolerance methods use redundant programs to enable the software to bypass and thus “tolerate” any faults that are identified when the system is in use. In such techniques, there is still the need to develop methods to detect faults, and the cost and time required to develop redundant programs is often prohibitive. This approach is rarely implemented [25].

Practitioners and researchers agree that fault prevention during the software development process is the most powerful means of constructing reliable software. Efforts expended in building the system “right” the first time, will usually avoid much more extensive efforts than searching for and fixing faults. Fault prevention, however, requires a shift from the assessment of the reliability of software products to that of providing methods and techniques to enhance reliability throughout the development process. Since reliability cannot be achieved by testing alone, the development process itself must be seen as an error prevention activity, with testing and evaluation providing continual feedback on subsequent activities. This requires methodologies that permit the diagnosis of problems as early in the life cycle as possible.

Many fault prevention techniques are part of the larger field of software engineering. These techniques (first developed for conventional software development) prescribe a process that involves the careful design and thorough documentation at each stage of development. One of the primary goals of software engineering techniques is to increase software reliability by monitoring and minimizing the number of errors through all phases.

The life cycle model makes the process of software development more visible and thus enhances the ability of developers to manage the process as well as estimate and control its costs $[26]$ . The model has also served to enhance reliability by focusing on the differing possibilities and sources of error. By breaking down the development process, measures can be taken at each phase to prevent introducing errors.

Errors in later stages of the life cycle often require revisiting the earlier stages. Design limitations may force revision of the requirements specification. Errors uncovered in testing require, at a minimum, changes in implementation and may require reworking of the requirement specifications and design. One of the objectives of implementing a life cycle approach is to minimize the “backtracking” by expending careful thought and analysis at early stages to avoid major problems and changes at the later ones. Although only a model, the life cycle concept has proved of great value in the production of timely, affordable, and reliable software systems.

Rapid prototyping has been the prominent method for developing ES. Prototyping can be an important tool and the work expended in developing and refining prototypes does enhance the reliability of the final system. However, prototyping development tends to involve a somewhat ad hoc process lacking the discipline and the principles necessary for any effective and efficient production system. Prototypes are, after all, software systems themselves, and so – although perhaps on a smaller scale – they also have their life cycle stages. Thus, it is essential that they should be developed in a way that adheres to good business practices, with a production schedule, formal quality assurance plans, documentation, and attention paid to whatever maintenance the prototype system may require. Problems faced in development of ES are basically the same as those encountered in developing conventional software systems and thus the life cycle approach should also be useful when developing ES.

## 3. Reliability throughout the ES development life cycle

Throughout the life cycle of ES development, there are three special qualities that impact their reliability. First, by definition, ES are used for complex problems and so result in complex software systems. Thus, there are more opportunities for errors and ES will always present formidable reliability challenges. Second, they are used on ill-structured problems. Thus their development will require more iterations than conventional software development, since the specifications and design will need iterative improvement. Third, the distinctions between the phases may not be as clear cut for ES as for conventional software. In ES, the developer is likely to interact with the expert and the user – each of whom may require changes in the requirements specifications and the design. This is another reason why the reliability of an expert systems application is so difficult to manage.

## 3.1. Requirement specifications

Requirements are the needs of the user. Specification is the description of what the system is supposed to do in order to meet its requirements. Misunderstandings in the requirement specification stage are very common and stem from communication gaps between the user and the developer. Because the cost of fixing an error rises dramatically as the software progresses through the life cycle, best practice is to prevent errors in the early stages. Formal specifications and algebraic specifications have been proposed to help software engineers overcome these problems.

Precisely because of the ill-structured nature of the problems, the possibility of solving the wrong problem is of greater concern for ES than for conventional software systems. A specification for a conventional application such as “calculate interest payments accurately” is more precise than an expert specification such as “make decisions about loan applications as well as the current loan manager does”.

Many researchers (e.g. Green and Keyes [10]) contend that the requirement specifications of expert systems are often nonexistent, imprecise, or changeable. Somerville says that “setting out a detailed specification for software to imitate humans is impossible [26]”. Parnas [22] states that software systems developed heuristically (as ES often are) are by their nature less reliable. Obtaining a complete formal specification for an ES may – for some projects – be impossible; however, some requirements documentation will reduce the ambiguity and should lead to better systems.

Giarratano and Riley [8] suggest production of a preliminary functional layout that defines “what the system should accomplish by specifying the high level functions of the system”. As the ES goes through iterations and changes, modifications that are broad enough to affect the high level functions and the general purpose of the system should be documented. The resources spent on the modification of the documents will be paid off by savings during the maintenance phase.

## 3.2. Design

In the design stage, decisions are made about how the system is to be implemented. Designing is a creative process and, in many cases, is mainly ad hoc. As with designing any product, errors are often introduced at this stage. Good design is the key to reliable software, but unfortunately it is not possible to formalize the design process completely.

One useful technique is a progressive design documentation approach that starts with an overall view of the software and progressively refines the system with more detail. Methods of refining (decomposing) the design include structured design and stepwise refinement. Cohesion, abstraction, coupling, and adaptability are the criteria used to identify a good design; see Pressman [24] and Somerville [26].

The increase in complexity of an expert system will lead to increased chances for design errors. For ES, design errors can occur in any of the three components: the knowledge base, the inference engine, and the user interface and can also occur from the interactions of these three.

The knowledge base of an expert system contains information relevant to a particular task. The amount and quality of the information in the knowledge base is crucial to the performance of the ES. In the design phase, the amount, quality, and structuring of the information are determined. Decisions are also made in this stage about the choice of an expert, how information is to be elicited, and the paradigm to use in representing this information.

The inference engine provides the control system and uses the interface mechanisms for applying the knowledge stored in the knowledge base. Inference engines use heuristic techniques to search the knowledge base, determine which rules and facts are to be utilized, execute the rules, interact with the user to obtain an additional needed information, and make decisions or recommendations when a satisfactory solution has been found. Inference engine design problems can include using the wrong search heuristic, using the wrong stopping mechanism, and using incorrect or inconsistent logic processing techniques.

The user interface is the mechanism by which the user and the expert system communicate. For ES there is at least a triangle of users: the expert, the knowledge engineer, and the ultimate user. The knowledge engineer, who is trying to elicit the information from the expert, not only has to communicate with the expert but also has to be able to translate the knowledge into a form useable by the inference engine and into a form that meets the user requirements. Abdul-Gader [1] describes this process as moving from technical feasibility to user feasibility. In addition, ES will frequently require a knowledge base maintainer to update and modify the knowledge base as new information is obtained. This maintainer may not be part of the original development team. Differences in communication styles between experts, knowledge engineers, maintainers, and users can lead to considerable design difficulties.

The parties may also have different communication requirements. ES requirements often call for interfaces that not only report the results of the analysis but can also explain and justify them. Thus ES interfaces often must provide powerful interactive graphics and language processing. In addition, the user's interface requirements may change over time. As the user gains familiarity with the system the needs may switch to a leaner explanation facility and greater efficiency. These multiple interfaces may lead to errors being introduced in the interface design.

To the extent that they can be applied to the less structured ES design, techniques of structured design and stepwise refinement should help to increase reliability “designed into” these systems. The design process can be divided into two phases: the logical design and the physical design. The logical design is based on the structure of the knowledge elicited. The physical design (developing any hardware and writing software) follows the logical design.

## 3.3. Implementation

The process of programming and implementing ES shares all of the possibilities for the introduction of errors as the process of implementing conventional software. Programming errors are unavoidable. They are very frequent in artificial intelligence applications due to the complexity of programming tools and the fact that few programmers have much experience with implementing ES.

The major difference in ES occurs in the implementation of the knowledge base that encodes human knowledge in modules that can be activated by patterns [17]. This design process consists of two steps: knowledge acquisition and knowledge representation.

Knowledge acquisition is the process of eliciting information from the domain expert and structuring it for the ES. The knowledge elicited from the expert includes factual knowledge and heuristic knowledge, which may be uncertain, judgmental, and only partially valid $[14]$ . Knowledge elicitation is usually accomplished by a series of lengthy and intensive interviews with the domain expert, who tries to articulate the needed expertise. However, all experts are, to some degree subjective, biased, and prone to error. Problems due to the knowledge acquisition phase may arise due to the complexity of the domain, communication gaps between expert and knowledge engineer, errors in reported knowledge due to experts' being distracted, tired or tempted to provide the wrong information to ensure continued employment or status.

Some authors have defined the reliability of an ES solely in terms of reliability of the acquired knowledge. O'Leary [21] indicated that reliability may be measured by the strength of the relationship between the knowledge reported to the system designer and the actual knowledge of the expert: he would say that if the actual and reported knowledge are the same we have perfect reliability. There are, however, other issues. An expert system may provide the same results as the expert, but both may be wrong. Any definition and measurement of reliability for expert systems must examine this issue of agreement with the expert against agreement with the outcome. In addition, an expert system may provide the “correct” result, but it may be misinterpreted by the user. With most expert systems, the user has to answer a set of questions which lead him/her to a solution. The end user, however, may not interpret and answer the questions as the expert intended, and also has only a limited ability to judge the validity of a given answer.

Knowledge representation is the process of formalizing the domain knowledge obtained during knowledge acquisition. It is not simply encoding. Representation mainly implies organization; knowledge representation is concerned with the way in which large bodies of knowledge can be formally described. By its nature, knowledge is hard to formalize, being derived from experience rather than mathematical theory $[17]$ . Any set of rules may be incomplete and inconsistent or the behavior of the system may not be reliably predicted by its designer. This complexity of knowledge leads to different forms of representation, such as symbolic systems and numeric information including uncertainty measures. Different schemes need to be developed to ensure the reliability of these different forms of information.

The field of ES itself, and knowledge representation in particular, is a relatively new area and thus the implementation tools available to developers are not extensive. The low level symbolic languages like Prolog and LISP often fail to offer the high level programming constructs and utilities that could greatly increase the productivity of developers and the reliability of final products. Knowledge engineers also need tools to facilitate the development and encoding of the knowledge base; e.g. explanation facilities, tracing mechanisms, rules/facts editors, and spelling checkers and graphical representation facilities. Much work remains to be done in the development of full featured and robust tools.

Yoon and Guimaraes [29] discuss the use of several development tools and techniques that can be used to overcome the limitations of attempting to extract knowledge from human experts by allowing the ES themselves to “learn” from a knowledge base of examples or cases or a model of the system. These tools may help to increase reliability by providing documented objective method to generate new knowledge, that do not rely on the vagaries of interacting with human experts. On the other hand, if there are errors in the original knowledge base, such tools may serve to propagate these errors in ways that may prove difficult to detect.

In addition, these (and other available) implementation tools themselves may be unreliable and a contributing factor to the failure of the final product. Many of the products are not fully developed, and they do not all have the robustness necessary for the development of expert systems intended to perform tasks of critical nature.

## 3.4. Testing

As part of the testing phase, V and V procedures are employed. Verification in conventional software engineering is a method of determining whether an implemented software system completely satisfies its specifications [2]. Validation tests determine if software functions properly in a total system environment. Boehm [4] distinguishes between them by asking two questions: 1. “Validation: are we building the right product?”,

2. “Verification: are building the product right?” Much of the published work on reliability of ES can be classified as efforts expended primarily in the testing phase, including the less specific “evaluation” of expert systems $[5,23]$ .

The link between reliability of an expert system and verification and validation is best described by Grunwald [11]. “An artificial system is reliable to the extent to which it can be expected that it functions according to its specifications... In the case of knowledge-based systems, it can be said that the system is reliable, if the conclusion that the knowledge-based system reaches is the same as the conclusion that this system was expected to reach”.

Tepandi [27] reports that verification tests are intended to uncover errors in a knowledge base, such as “redundancy”, “circularity in rules”, “subsuming rules”, “incompleteness”, etc. Verification problems should be designed to test all sections as thoroughly and comprehensively as possible. An ES that is formally verified has a better chance of producing correct answers.

The validation process is intended to test that the ES works correctly in its final user environment. These tests should be performed after the system is completely developed and verified by running test cases and comparing the results against known results or expert opinions. The reliability of the final system depends both upon the choice of test cases (complexity and comprehensiveness) and on the number of test cases.

Testing is likely to be more arduous for ES than for conventional systems. It is likely that ES will require almost continual testing of the system and frequent expansion of its test data base to try to keep the system from exhibiting important gaps in knowledge.

## 3.5. Maintenance

Maintenance of ES has not been widely addressed. However, as they move away from being academic projects and towards becoming commercial, increased concern must be given to maintaining them.

A maintenance problem specific to ES is that maintainers usually have less expertise than the original engineers. Maintainers need tools for editing and updating rules, variable definitions, and cases. These tools should be able to show the links and implications of new rules and the existing knowledge base. The knowledge maintainer has often limited access to the original domain expert, thus ambiguities can easily occur.

Another source of failure is coding errors. Those expert systems built “from scratch”, make use of AI or knowledge engineering languages that are relatively difficult to learn and use without error. Implementations written using these languages can be difficult to follow, leading to a high likelihood of errors introduced when making changes.

Decisions pertaining to reliable maintenance of an ES should be made in the design phase. A long term maintenance group should be trained. They will be responsible for revising data and knowledge that has changed. Two alternatives are available: centralized maintenance or distributed maintenance. The former relies heavily on the original expert and a small maintenance group. Distributed maintenance may involve a including new sources of expertise to respond to problems and needs that occur as the ES evolves; it may involve a number of maintenance teams working in different areas. Distributed maintenance can allow the customization of the system for different user groups, however the proliferation of different versions of the ES increases maintenance difficulties.

Table 1  
Summary of reliability issues and possible techniques throughout the life cycle

<table><tr><td>Stage</td><td>Reliability issues specific to expert systems</td><td>Useful techniques</td></tr><tr><td>Requirements specification</td><td>ES used on ill-structured problems, so requirements are difficult to specify precisely.</td><td>Develop high-level functional layouts.</td></tr><tr><td>Design</td><td>ES involve complex systems; require design of knowledge base, inference engine, and user interface. Each component has unique reliability issues. Reliability problems can also occur in the interfaces between components.</td><td>Use stepwise refinement, decomposition, and structured design.</td></tr><tr><td>Implementation</td><td>Problems will occur in both knowledge acquisition and representation. Finding a structure to truly represent the full knowledge of the expert is difficult. Developers must think through the issue of whether what the expert says is always, in fact, “correct”. Implementation languages and tools are new, may be difficult to use correctly, and may themselves have errors.</td><td>Develop (and use) full-featured and robust languages and development tools. Develop tools to let the systems themselves “learn”.</td></tr><tr><td>Testing</td><td>ES are complex and difficult to fully test. ES evolve continuously with use, so testing is never finished.</td><td>Expend effort on carefully planned, ongoing, verification and validation programs.</td></tr><tr><td>Maintenance</td><td>Knowledge continually changes. Maintenance must involve the users as well as developers. Systems using new and unfamiliar AI languages can be difficult to change without introducing new errors.</td><td>Develop a balance between centralized and decentralized efforts.</td></tr></table>

help increase the quality and reliability of these systems. In addition, by formalizing the processes performed at early stages the number of problems introduced early but identified late should be reduced.

Following the process used in production engineering, developing an ES should involve specifications of general engineering quality standards, which are then used as a guideline for the assessment of the system's performance. Sound software engineering principles should lead to faster, more reliable, and safer ES.

## 4. Summary and conclusions

The increasing application of ES for both routine and critical tasks has lead to a considerable commercial interest. Since ES are no longer the output only of advanced research laboratories and are becoming commercial products, there must be formal process of quality assurance. Table 1 summarizes the specific reliability issues often encountered during each stage in the life cycle and suggests some techniques that might be used to address these issues. Organization of ES development by using the life cycle paradigm should

## References

[1] Abdul-Gader, A.H. “Usability of Knowledge-Based Systems”, Information and Management, North-Holland, Vol. 21, 1991, pp. 1–6.

[2] Adrion, W.R., Branstad, M.A. and Chernavsky, J.C. "Validation, Verification and Testing of Computer software", ACM Computing Surveys, Vol. 14, No. 2, June 1982.

[3] Beizer, B. Software System Testing and Quality Assurance, Van Nostrand Reinhold Company, USA, 1984.

[4] Boehm, B.W. Software Engineering Economics, Englewood Cliffs, NJ: Prentice Hall, 1981.

[5] Botten, N., Kusiak, A. and Raz, T. “Knowledge Bases: Integration, Verification and Partitioning”, European

Journal of Operational Research, Vol. 2, 1989, pp. 111-128.

[6] Coats, P.K. “Why Expert Systems Fail”, Financial Management, Vol. 17, No. 3, 1988, pp. 396–405.

[7] Feigenbaum, E.A. Knowledge Engineering in the 1980's, Technical Report, Department of Computer Science, Stanford University, Stanford, CA, 1982.

[8] Giarrantano, J. and Riley, G. Expert Systems: Principles and Programming, Boston: PWS-KENT, 1989.

[9] Goel, A.L. “Software Reliability Models: Assumptions, Limitations, and Applicability”, IEEE Transactions on Software Engineering, Vol. SE-11, No. 12, 1985, pp. 1411–1423.

[10] Green, C.J.R. and Keyes, M.M. “Verification and Validation of Expert Systems” in WESTEX-87 – Western Conference on Expert Systems, IEEE, 1987, pp. 38–43.

[11] Grunwald, S. "Estimation of Failure Potential in Knowledge Bases", in Proceedings of the 9th European Conference on Artificial Intelligence, M. Ayel and J-P. Laurent, eds., ECAI 90, Stockholm, Pitman, 1990, pp. 163–175.

[12] Guida, G. and Tasso, C. “Building Expert Systems: A Structured Bibliography”, in Topics in Expert System Design: Methodologies and Tools, G. Guida and C. Tasso, eds., New York: North-Holland, 1989, pp. 419–435.

[13] Hayes-Roth, F. “The Knowledge-based Expert System: A Tutorial”, in Developing Expert Systems for Business Applications, J.S. Chandler and T-P. Liang, eds., Columbus, OH: Merrill, 1989, pp. 3–24.

[14] Hollnagel, E. “Evaluation of Expert Systems”, in Topics in Expert System Design: Methodologies and Tools, G. Guida and C. Tasso, eds., New York: North-Holland, 1989, pp. 377–416.

[15] Hoppe, T. “Aspects of Incremental Knowledge Validation” in Proceedings of the 9th European Conference on Artificial Intelligence, M. Ayel and J-P. Laurent, eds., ECAI 90, Stockholm, Pitman, 1990, pp. 34-45.

[16] Ignizio, J.P. Introduction to Expert Systems: the Development and Implementation of Rule-Based Expert Systems, McGraw-Hill, 1991.

[17] Jackson, P. Introduction to Expert Systems, 2nd edn., Reading, MA: Addison-Wesely, 1990.

[18] Musa, D.J., Iannino, A. and Okumoto, K. Software Reliability: Measurement, Prediction, Application, New York: McGraw-Hill, 1988.

[19] Mykytyn, K., Mykytyn, P. and Slinkman, G. “Expert Systems: A Question of Liability?”, MIS Quarterly, Vol. 27, No. 1, March 1990, pp. 26–41.

[20] O'Keefe, R.M., Balci, O. and Smith, E.P. Validation Expert System Performance, IEEE Expert, Winter 1987, pp. 81–89.

[21] O'Leary, D.E. "Validation of Expert Systems - With Applications to Auditing and Accounting Expert Systems", Decision Sciences, Vol. 18, Summer 1987, pp. 468-485.

[22] Parnas, D.L. “Software Aspects of Strategic Defense Systems”, American Scientist, Vol. 17, No. 5, May 1985.

[23] Preece, A.D. “Verification of Rule-based Systems in Wide Domains”, in Research and Development in Expert

Systems VI: Proceedings of Expert Systems 89, Ninth Annual Technical Conference British Computer Society Specialist Group on Expert Systems, London, September 20–22, 1989, pp. 66–77.

[24] Pressman, R.S. Software Engineering - A Practitioner's Approach, 2nd Edn., New York: McGraw-Hill, 1987.

[25] Shimeall, T.J. and Leveson N. "An Empirical Comparison of Software Fault Tolerance and Fault Elimination", IEEE Transactions on Software Engineering, Vol. 17, No. 2, 1991, pp. 173–182.

[26] Somerville, I. Software Engineering, 3rd Edn., Reading, MA: Addison-Wesley, 1989.

[27] Tepandi, J. “Comparison of Expert System Verification Criteria: Redundancy” in Proceedings of the 9th European Conference on Artificial Intelligence, M. Ayel and J-P. Laurent, eds., ECAI 90, Stockholm, Pitman, 1990, pp. 42–61.

[28] Vinze, A.S. and Vogel, D.R. “Performance Evaluation of a Knowledge-based System”, Information and Management, North-Holland, Vol. 21, 1991, pp. 225–235.

[29] Yoon, Y. and Guimaraes, T. "Selecting Expert System Development Techniques", Information and Management, North-Holland, Vol. 24, 1993, pp. 209–223.

![](/api/attachments/BHD46RGK/fulltext/images/e93d7c58d16ce6159fc8ca2e39cd1ba8e78bb7400ad9270664bd12c03410f40c.jpg)

Noushin Ashrafi is an Assistant Professor of Management Science and Information Systems at University of Massachusetts at Boston. She received her PhD. degree in Management Sciences and Information Systems from the University of Texas at Arlington in 1989. Her current areas of research include software reliability, fault-tolerant software, expert system reliability, and Bayesian methods for estimating and predicting software

reliability. She has published several papers on these topics in the leading journals. She was the Vice President and President of TIMS Boston Chapter for 1990–1991 and 1991–1992 respectively.

![](/api/attachments/BHD46RGK/fulltext/images/c091025b019eabab630741645dc3a77811d9ffa76cbe97948ed4cf39fb27d091.jpg)

Jean-Pierre Kuilboer is an assistant professor of Management Science and Information Systems at the University of Massachusetts at Boston. He received a PhD. in Information Systems from the University of Texas at Arlington in 1992. His research interests include quality and performance measurements in information systems, object-oriented systems design, and enterprise-wide data models. He is a member of the Decision Sciences In-

stitute and AIS. He has recently published articles in Information and Software Technology, Journal of Data and Computer Communications, and Database.

![](/api/attachments/BHD46RGK/fulltext/images/978289c399cee2f568255896b55bcacbedc669d1c36f23d5c3e70495b9b196e4.jpg)

Janet M. Wagner is a Assistant Professor of Management Science and Information Systems at the University of Massachusetts at Boston. She received her PhD. in Operations Research from the Massachusetts Institute of Technology in 1998. Her research interests involve examining the effects of uncertainty on various management areas, including software reliability, reliability of water distribution systems, capacity expansion in

operations management, and stochastic optimization. Her work has published in journals including the European Journal of Operational Research and Naval Research Logistics.
