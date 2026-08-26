---
otero_id: 27283
otero_key: "EAUBN2U3"
title: "Prototyping For Systems Development: A Critical Appraisal"
authors: "Marius A. Janson; L. Douglas Smith"
year: "1985"
journal: "MIS Quarterly"
doi: "10.2307/249231"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Prototyping for Systems Development: A Critical Appraisal
Author(s): Marius A. Janson and L. Douglas Smith
Source: MIS Quarterly, Vol. 9, No. 4 (Dec., 1985), pp. 305-316
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/249231

Accessed: 09/05/2014 00:31

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# Prototyping For Systems Development: A Critical Appraisal

By: Marius A. Janson
L. Douglas Smith
University of Missouri — St. Louis
School of Business Administration
Department of Management Science
and Information Systems
St. Louis, Missouri

## Abstract

Although relatively recent in information systems design, the prototyping technique has a long tradition in developing engineering systems. An engineering system is defined as any artificial system that performs actions to achieve a desired transformation of objects undergoing a change of state. We will review the application of and experience with prototyping in engineering systems design and relate these to the development of information systems.

Drawing on the strong similarities between the design processes of engineering systems and information systems results in the identification of a number of different types of prototypes that can be used for a variety of purposes and integrated into the various stages of the systems development life cycle. The experience gained from applying the prototyping method in the design of engineering systems permits us to exploit its advantages and to avoid its misapplications when it is used in information systems development.

Keywords: Information systems, system analysis, system design, prototype.

ACM Categories: D.2.1, D.2.9, D.3.2

## Introduction

Prototyping as a method for systems development has received a great deal of attention in recent literature. Some authors view it as a “revolutionary” method that will replace the traditional life cycle method of systems development $[10,11]$ .

Major differences between prototyping and the traditional systems development life cycle are the lack of tightly written systems design specifications and the short time period required to provide the user with an initial system for actual “hands-on” experience. Prototyping addresses the inability of many users to specify their information needs, and the difficulty of systems analysts to understand the user’s environment, by providing the user with a tentative system for experimental purposes at the earliest possible time. The user’s experiences with this experimental system indicate modifications to incorporate into the prototype, leading to a new series of user experimentation.

As in many situations it is possible to oversell a new method. Studies reporting successful information systems developed using the prototype method do not necessarily demonstrate that the traditional life cycle method is obsolete. Rather, a better understanding of prototyping, the different types of prototypes, and their advantages and disadvantages are needed to decide where, when, and for which purposes this method should be used.

Dodd [2] examined prototyping, using architectural concepts to structure the prototyping process of information systems design, without much success. A more fruitful approach would be to identify a design discipline that has substantial experience with prototypes and would apply them under situations similar to those encountered in information systems design.

Although prototyping is a relatively recent development in information systems design, it has been used extensively and over a long period of time for electrical and mechanical engineering systems design. For our purposes an engineering system may be defined as any artificial system that performs the necessary actions to achieve a desired transformation of the object(s) undergoing a change of state [8]. The objects can be material, energy, or information signals. A standard television set is an example of an engineering system. It is an artificial system that accepts as input an electromagnetic signal containing audio and video information. The signal is processed and, after separating the audio and video components, appears as system outputs in the form of sound and light.

Information systems are similar to engineering systems because they too perform transformations on (data) objects that are undergoing a change of state. Therefore, adding the term “information” to the definition of an engineering system extends it to include information systems as well.

Prototyping in engineering systems design is the process of building and testing models of the target system. These models, constructed at different points during the design effort, serve a wide variety of purposes including, but not limited to, system requirements specification, initial design concept testing, and verification that the final systems design performs as intended. These divergent tasks determine the method of prototype construction, which may vary from simulating the system to actually building it using completed design documents.

The study of prototypes used in engineering systems design is motivated here by the expectation that it will provide insights that can be transferred to information systems design. The notion of transferability of prototype experiences from one discipline to the other is based on the similarity of the design task.

This article (1) discusses the application of the prototyping method in engineering, (2) compares the similarities between engineering and information systems design processes, (3) relates the prototyping experience in engineering to information systems design, and (4) identifies different types of prototypes that are applicable to a variety of tasks, not limited to information requirements specification. The comparative study shows that the prototype method does not render the life cycle method obsolete; rather, prototyping can be effectively used in combination with it. This article concludes with a discussion of an actual information systems design where prototypes were used for user information needs identification, systems design and verification, and systems implementation. It should be of interest to those generally concerned with developing and using management information and decision support systems.

## The Nature of Prototyping

Recent articles recommending prototyping as a method for systems design emphasize situations where users have difficulty in specifying, or are unable to specify their information needs. The prototyping practice in mechanical and electrical engineering reveals, however, that prototyping is useful within the traditional life cycle as a method for:

1. verifying that the needs of the user(s) are met,

2. verifying that a design meets its specifications,

3. selecting the “best” design from among a number of alternative design solutions,

4. testing and developing a conceptual understanding of novel problem solutions,

5. testing a chosen design under varying environmental conditions,

6. demonstrating a new product to upper management to gain approval for a full-scale development effort, or

7. implementing a new system in the user environment.

The divergent nature of these tasks calls for prototypes with task specific characteristics, and therefore a definition and categorization of prototypes based on their characteristics is needed. Although the ensuing discussion will be in terms of mechanical and electrical engineering concepts, much of it has direct implications for information systems design.

Glegg [4] defines a prototype as the “first embodiment of an idea.” It is tentative and its purpose is to validate or test the idea in question. Neither the prototype’s form nor the materials used in its construction have to be those of the final design, as long as the basic idea or concept can be tested. This parallels the definition given by Naumann and Jenkins [11], who describe an information system's prototype as being a system that captures the essentials of a later system. We shall return to these definitions at a later point to assess how well they describe the prototyping process. For our purposes it is important to note that these definitions permit prototypes of different kinds, constructed for different purposes.

## Categories of prototypes

Table 1 identifies three prototype categories: real life, simulated, and real life/simulated. The table further illustrates the nature of the design information provided by each prototype category. The different categories are described in the discussion below.

## Real Life Prototype

A “real-life” prototype is a full-scale representation of the basic design idea employing materials intended to be used for the final design. It is then tested under a variety of conditions. The primary purpose of this type of prototype is to verify the soundness of the design idea and to ensure that design specifications are met by comparing test results against stated specifications. In terms of Table 1, the real-life prototype reveals if the design is successful, but not the reasons for its success. Experiments involving changes in the prototype are needed to learn why a design works. Real-life prototypes, because of their size, cost, and the time required for their construction and modification, are usually too inflexible for much experimentation.

## Simulated prototype

A second possibility is to construct a “simulated” prototype using a different medium for construction than the final intended design. This substitute medium operates according to the same physical laws as the original medium. An example is the representation of building heat losses by electrical components, such as resistors, capacitors, and voltages; in short, an analog computer. A prototype of this kind can be changed rapidly to reflect equivalent building modifications. Experimentation with a simulated prototype does not show how the design works in real life because it is not constructed in its intended medium. Rather, the simulated prototype can provide an understanding of the proposed design concept(s). This understanding comes about through repeated testing and prototype modification.

## Real-life/simulated prototype

A final possibility is a prototype that is a combination of the two just discussed; some parts are real-life, constructed using final design materials, and other parts are simulated. This prototype shows how parts of the final design work in real life and also provides insights into why the design works.

A prototype is applied within the context of a design process, and thus its purpose and characteristics are contingent on that process. That is to say, the nature of the design and the degree of design completion at the time of prototype application determines both its purpose and its characteristics. For example, constructing a real-life prototype requires a significant amount of design completion and should thus be used at a later stage in the system development life cycle. A simulation prototype demands a smaller degree of design completion and can be used at practically any phase in the life cycle. We shall show that the design processes in engineering and information systems design are similar, resulting in the transferability of prototype experience from one discipline to the other.

Table 1. The Nature of Prototypes

<table><tr><td rowspan="2">Design Information Provided by Prototype</td><td colspan="3">Prototype Nature</td></tr><tr><td>Real-life</td><td>Simulated</td><td>Real-life/Simulated</td></tr><tr><td>What happens, what works</td><td>Y</td><td>N</td><td>Y</td></tr><tr><td>Conceptual understanding</td><td>N</td><td>Y</td><td>Y</td></tr></table>

## The Design Process

A simplified version of the mechanical engineering design process, proposed by Hubka [8], is illustrated in Figure 1. The individual phases of this process map into three main stages: (1) intelligence, (2) design, and (3) implementation.

The intelligence stage begins with a set of requirements that are usually minimally defined, often unrealistic, and contradictory. They form the input to the phase that elaborates the problem assignment. The objective of this part of the design process is to specify what the engineering system has to accomplish so that the outcome is a solution-neutral formulation of requirements expressed as design specifications.

The second step uses the design specifications to establish functional structures that underlie the engineering system. The function the system is to perform can often be broken down into subfunctions that need to be combined optimally by selecting the best solution from among a set of alternatives.

![](/api/attachments/EAUBN2U3/fulltext/images/15dd38a01c3c6166c53924f3363ee5a55954d09fe0994bd3b47002bb7fec1b7c.jpg)  
Figure 1. The Systems Development Life Cycle

During stage 2 the functional structure is transformed into a semifinal representation during the conceptual design, preliminary layout, and dimensional layout phases. The subfunctions can often be realized using different anatomic structures, where the objective is to select one structure that is optimal given all of the design situation constraints. The selection of materials, components, and their arrangements, which were vague in previous phases, are completed in the dimensional layout phase. Furthermore, a thorough evaluation and verification process is conducted by means of dimensional checking, strength calculations, and systems testing. The design stage is completed by final design detailing and engineering systems production. The third and final stage involves implementing the engineering system in its working environment.

## Prototype function in engineering

Prototype characteristics and the design process illustrated previously form the basis for a method of dealing with two major problem categories occurring in engineering system design: (1) incomplete and contradictory user need and design specifications, and (2) uncertainty regarding possible design solutions.

Incomplete design specifications are an example of category 1. They result from the user's inability to state his needs, to foresee how those needs may evolve over time, or to appreciate the limitations of a particular technology. The primary purpose of a prototype in this context is to determine a set of desirable design features for a given user environment, rather than to foster an understanding about the design concepts underlying the engineering system. In terms of Table 1, the focus is on what works rather than on conceptual understanding. The prototype should then be either real-life or a combination of real-life/simulation. Such a prototype requires a fair amount of design completion and occurs, at a later phase in the system development life cycle.

Using prototyping for user needs specification cannot then be equally applied in all situations, rather, it is contingent on the nature of the design environment. Certain design environments allow for more flexibility for design changes than others. If an engineering system is entirely mechanical, a major design change implies a major cost in both time and money to change the prototype. On the other hand, if the design has mainly electronic components, a design change may mean a different arrangement of standard high-level electronic functional blocks which can be accomplished comparatively inexpensively. To keep the number of prototype iterations to a minimum, especially when modifications are costly, prototyping cannot substitute for careful user needs specifications.

In the second problem category a situation may arise when the design environment or task are so complex that it is not feasible to predict systems behavior by analytical means. In this case the designer is interested in learning how the underlying design concepts operate in an actual design. Table 1 indicates that a simulation or real-life/simulation prototype is appropriate. Prototyping for design selection can occur at any phase in the life cycle up to engineering systems production. The cost of prototyping depends on the degree to which system functions can be simulated. The use of sophisticated functional building blocks (i.e., functions realized in off-the-shelf electronic components) make it possible to realize flexible, low-cost prototypes.

Another example of problem category 2 deals with the testing of a completed engineering design against specifications. The testing takes place before systems implementation and is typically conducted at the request of the systems designer. A prototype constructed for this purpose is real-life, and design failures are expensive to correct because the intelligence and design stages have been completed. Any design changes at this point may mean having to duplicate the complete design life cycle.

A last problem in category 2 involves a situation in which users have an application with well-defined specifications and decide to avoid system design by acquiring an existing system. The purpose of a prototype here, sometimes called a pilot system [12], is to verify that the system's specifications match the user's needs. The prototype system is real-life, and failure to meet user needs results either in minor systems modifications or system rejection.

The initial definitions of a prototype as a “first embodiment of an idea” [4], or as a “system that captures the essential features of a later system” [11], when compared to these examples, do not adequately describe the prototyping process. The issue here is that distinctions between prototype and final system are ambiguous; nonexistent in cases where standard systems are acquired and tested. It is, therefore, most useful in practical situations to consider prototyping in a functional context.

The integration of the prototype into the development life cycle is illustrated in Table 2. The conclusions drawn in this table are that: (1) the applicability of a particular type of prototype is contingent on the task it is asked to perform, (2) both the nature of the prototype and its task determine where in the life cycle it can be used, and (3) prototype cost depends on prototype nature and task.

Prototype testing and evaluation is a recurring theme. It is the primary purpose of prototype construction. This, in turn, requires that a well-defined test plan be developed before starting prototype construction. The plan ensures that the prototyping activity has focus and avoids needless prototype versions. Prototyping, by itself, is not a method of systems design; rather, it augments and is integrated into the standard development life cycle. The prototype increases the likelihood that the final design meets the user's needs and that it will be successfully implemented. Thus, cost savings in the design process is not a major motivation for prototype use here.

## Information systems vs. engineering systems

The similarities of the design process provide the rationale for transferring prototype experiences in engineering to information systems design. Information and engineering systems development life cycle similarities are illustrated in Figure 1. The figure depicts the information systems development life cycle defined by Davis [1] and an engineering life cycle based on Hubka [8]. The correspondence between the two development life cycles is indicated by dashed lines connecting the design phases with similar functions. The individual design phases are grouped into the three main stages of intelligence, design, and implementation, and show the close correspondence between information systems and engineering systems design disciplines.

A second aspect of similarity is the type of prototype. The three kinds of prototypes used in engineering systems design, real-life, simulation, and real-life/simulation, depicted in Table 1, are also relevant to information systems design and are illustrated in Table 2. A real-life prototype is constructed such that its individual parts are as close as possible to their final form; i.e., the system's model base, database, and report generator are represented in their final structure. The purpose of the real-life prototype is to test an information system against its design specifications.

A simulation prototype can provide knowledge about the reality the information system is to model and the functions it is to perform. An information system for inventory control is an example of the simulated approach. In this case, the inventory system would be modeled and information gathered on its behavior (e.g., stock levels on a per item basis, aging, spoilage, and shortages). This information can be gathered for different physical layouts of the inventory system and for different replenishment schedules. The management information system would be embedded into the model of the inventory system. The simulation prototype provides design information on the behavior of the inventory system itself and about the information needs required to keep the system under control.

A real-life/simulation prototype may be written in a language, operate on data, and employ a database structure that are all different from the final system. In our example, the inventory system can be simulation or real-life, with the information system operating on part or all of the simulated or real-world data. The purpose of the prototype is to define user information requirements and to gain insights into systems behavior.

Table 2. The Application of Prototyping in the Design Process

<table><tr><td rowspan="2">Prototype Use</td><td colspan="5">Prototype Nature</td></tr><tr><td>Where Used in Life Cycle Stage</td><td>Real-life</td><td>Simulation</td><td>Real-life/ Simulated</td><td>Relative Cost</td></tr><tr><td>Requirement Specification</td><td>Intelligence (at end) or Design (at start)</td><td>+</td><td>++</td><td>+++</td><td>Low to Medium</td></tr><tr><td>Design Selection Understanding Test System Components</td><td>Intelligence or Design</td><td>+</td><td>+++</td><td>++</td><td>Low</td></tr><tr><td>Test, Evaluation Completed System</td><td>Design (at end) or Implementation (at start)</td><td>+++</td><td></td><td></td><td>High</td></tr><tr><td colspan="6">Blank; not applicable + Least Applicable + + Applicable + + + Most Applicable</td></tr></table>

The previous discussion focused on the application and nature of prototypes and their place in the system development life cycle. Experience with prototyping in engineering systems design reveals that this method has serious disadvantages when applied incorrectly. Reasons for its misapplication are varied. The designer often labors under severe time constraints that are a motivation for proceeding with prototype construction quickly, without the benefit of indepth user needs analyses or a prototype testing and evaluation plan. The designer may also fail to consider the more general set of needs that the engineering system has to meet, either presently or at some future time. The resulting design may be inflexible, not easily adaptable to additional applications, and may suffer from a narrowness of focus.

A prototype does not provide a strong motivation for careful documentation because it is constructured for the purpose of iterating through a number of design cycles, and as a result is temporary in nature. This, in turn, can result in a final design that cannot be defended because it lacks justification about why it was selected over other design alternatives.

A more serious problem of the prototyping method can be the designer himself, who may be lacking general design skills or the expertise required for a specific design situation. Faced with a system development task for which this person is ill-equipped, the overwhelming urge is to build a prototype without a clearly defined design concept or a plan for prototype testing and evaluation. Analysis is replaced by prototyping and systems design is in the form of a series of “cut-and-try” modifications.

This situation has been noticed by the researchers at a number of different companies where it was customary to promote electronic technicians to design engineers. This coincided with the development of low cost, sophisticated electronic functional building blocks. These two events led to designers who were ill-equipped for the task, facing an almost infinite set of possibilities in constructing prototypes using the newly available functional building blocks. The results were design releases lacking both a sound theoretical design basis and adequate documentation, displaying unstable design properties, and unable to operate in the face of varying functional block and environmental tolerances. This necessitated patch-ups to get individual production units to work at all, resulting in units at the customer's site that were all slightly different. The difficulty of servicing products, all different and lacking in adequate documentation, can well be imagined.

Because of the similarities of the design process one may argue that the problems experienced in engineering systems design find a parallel in information systems design. Time pressures are great, qualified systems designers are scarce, and the use of very high level languages allow for prototyping based on scant user needs definitions and systems analysis. This, in turn, may result in systems that are: (1) narrow in design focus, (2) lacking in adaptability to changing needs, (3) lacking in adequate design documentation, and (4) not operating as intended.

The well established and long term use of prototypes in engineering systems design suggests that ways exist to avoid the misapplication of this method. Narrowness of design focus (i.e., lack of appreciation for future user information needs, not considering alternative system designs) can be avoided through using scaled down simulation prototypes or real-life/simulation prototypes. The former assures an understanding of the system, whereas the latter provides the user with hands-on experience that enables him better to specify his information system needs.

Peer group design evaluation represents an additional tool for preventing the problem of narrow design focus [7]. Substituting prototyping for sound design methods occurs when the complexity of systems design and the designer's abilities are ill-matched. Peer group evaluation and a reasonably well-defined prototype purpose, test, and evaluation plan before commencing with prototype construction can prevent this problem.

## Prototyping Applied to Systems Design

Established practices in engineering systems design show that prototypes are used for a variety of tasks that fall into three categories: systems specification, design selection and testing, and systems testing and implementation. The nature of the prototype is either real-life, simulation, or real-life/simulation. The nature of the prototype, and its place in the development life cycle, is task-specific.

These findings will be illustrated with the analysis of the prototyping method applied in the development of an information system that supports marketing research and planning. The reader may consider for what purposes the prototypes were used, what their nature was, and in what ways prototyping misapplication was prevented.

## Case study

A regional insurance firm approached several university faculty members about a joint effort to develop a decision support system for marketing research and corporate planning. The primary goal was to produce reports and geographic maps to show summary statistics based on the company's past performance. This information would enable management to compare the company's performance relative to its competitors.

A secondary goal, contingent on the first, was to construct productive models that were based on exploratory variables of past performance to facilitate planning for future business activities. Modeling results needed to be presented in tabular form or superimposed on geographic maps of corporate operating areas displayed on a VDT with the option of hard copy output. It was felt that the user's information requirements dictated a very responsive and interactive system. The design support system, although intended to be multi-user, primarily served two company officials, the vice president of marketing and the director of planning and research.

## Strategy for Systems Development

The design of the decision support system started with funding and developing an information system that summarized and graphically displayed past company performance by geographic area. Successful demonstration of the system led to funding and developing the predictive models. The framework of the decision support system resulting from this staged approach is illustrated in Figure 2.

The database consisted of several files: (1) information summarized from U.S. census files, (2) coordinates for the geographic areas of interest to the company, and (3) policyholder information—one for the current year, another for the previous year. The report and display generator presented information in either tabular or graphic format, both on a VDT and as hard copy. The model base formed the third component of the information system. It contained a set of regression models that predicted exploratory company performance as a function of operational variables.

The primary information system user, the director of planning and research, specified SAS as the programming language because he and his staff members were familiar with it. The planning group would perform ongoing systems maintenance. The SAS language was thought to be particularly applicable in light of stated systems requirements. SAS features excellent mapping and report generating capabilities, a wide range of modeling capabilities, a file management system, and the possibility of combining all of these in programming macros. The system illustrated in Figure 2 has all of the resources identified by Naumann and Jenkins [11] as required for prototyping: (1) a database, (2) a modeling facility, (3) generalized input and output, and (4) a high level programming language.

## Roles of Prototypes

The report and display generator and model base were each designed concurrently but separately by two designers. This required constructing several independent prototypes. These prototypes were different in nature because they performed different functions. As illustrated in Table 3, the report and display generator fulfilled multiple functions: user need specification, systems specification, systems demonstration, and securing continued systems funding.

![](/api/attachments/EAUBN2U3/fulltext/images/814d30820a62b6d587daa4276b38ca0fe55742e0e052b6143ec54d092de9a97a.jpg)  
Figure 2. A DSS for Marketing Research and Planning

Table 3. Prototype Use in DSS Development

<table><tr><td>System Component</td><td>Prototype Purpose</td><td>Prototype Characteristics</td><td>Where Used in Life Cycle</td></tr><tr><td>Report and Display Generator</td><td>user need specificationdesign specificationsystem demonstrationcontinued project funding</td><td>real-life</td><td>intelligence stage</td></tr><tr><td>Predictive Models</td><td>modeling technique selectionmodel development exploratory</td><td>simulatedreal-life/simulatedsimulated</td><td>design stage</td></tr><tr><td>Completed DSS</td><td>implementation</td><td>real-life</td><td>implementation stage</td></tr></table>

Several factors motivated the construction of a real-life prototype. First, the primary system user insisted that the prototype operate on the entire database. Second, it was expected that a real-life prototype would improve the chances of obtaining ongoing project funding.

The development of predictive models was supported by several prototypes. One prototype facilitated the selection of the appropriate modeling technique and its purpose was exploratory. It operated on a small subset of the corporate data with a file structure that differed from that of the corporate database. This insulated the modeling technique selection from modifications of and additions to the corporate database, thus simplifying prototype testing and evaluation. These characteristics of use and structure were best served by a simulation prototype.

A second prototype aided variable selection and parameter estimation of the predictive model after the appropriate modeling technique had been defined. It used a database similar to that of the previous model. An additional prototype function consisted of demonstrating the input, output, and operating features of this part of the system. These characteristics resulted in a real-life/simulation prototype.

A final prototype consisted of the completed decision support system, operating under conditions similar to those of the corporate computing environment. The main function of this prototype was to demonstrate the system to the user in an effort to achieve successful systems implementation at the corporate facilities. This prototype, alternatively called a pilot system $[12]$ , was a real-life prototype.

The development method just described facilitated the design and construction of the information system within 100 man-hours. Narrowness of the design concept, a possible result of prototyping misapplication, was prevented by the intimate involvement of the system user in specifying the system's features. The task of design documentation was simplified because of the self-documenting nature of SAS and because the user was familiar with this programming language. The chances of successful systems design were enhanced by regular peer group meetings between the individual designers. Careful prototype construction planning, testing, and evaluation kept the design effort on course and allowed system completion within budget and on time.

It is evident from this narrative that prototypes can be used to develop a larger and more complete information system than required for this particular application. As a system becomes larger and more complex, involving more designers, it is expected that one will need a higher degree of design formalization. This can be achieved by integrating the prototype in the standard systems development life cycle or some derivative thereof.

## Conclusion

This article presents a view of prototyping based on the analysis of design processes similar to those used in the development of information systems, and on the personal experience of the researchers in designing electronic systems. As with so many seemingly new developments in MIS, prototyping for the design of management information systems is part of a more general design method that has been widely used in other disciplines, notably mechanical and electrical engineering.

The more novel contribution of this article is in identifying a variety of prototypes that serve different design purposes and are integrated into the systems development life cycle. The analogy between engineering and information systems design provides guidelines for prototype applications and is suggestive of ways in which possible prototype misapplications may be avoided.

The comparative study of engineering and information systems results in a view of prototyping that shifts from the strict definitional position advanced by Naumann and Jenkins to considering the prototype in terms of its intended function.

## References

[1] Davis, G.B. Management Information Systems: Conceptual Foundations, Structure, and Development, McGraw-Hill, New York, New York, 1974.

[2] Dodd, W. P. “Prototype Programs,” Computer, Volume 13, Number 2, February 1980, p. 81.

[3] Freeman, P. “Why Johnny Can’t Analyze,” in System Analysis and Design: A Foundation for the 1980’s, W. Cotterman, J.D. Couger, N.L. Enger, and F. Haroki, (eds.), Elsevier North-Holland, Amsterdam, Holland, 1981, pp. 321-329.

[4] Glegg, G.L. The Development of Design, Cambridge University Press, Cambridge, England, 1981.

[5] Gooma, H. and Scott, B.H. “Prototyping as a Tool in the Specification of User Requirements,” Proceedings of the Fifth International Conference on Software Engineering, Institute of Electrical and Electronic Engineers, New York, New York, 1981, pp. 333-339.

[6] Groner, G.F., Hopwood, M.D., Palley, N.A. and Sibley, W.L. “Requirements Analysis in Clinical Research Information Processing — A Case Study,” Computer, Volume 12, Number 9, September 1979, pp. 100-108.

[7] Henderson, J.C. and Ingraham, R.S. “Prototyping For DSS: A Critical Appraisal,” in Decision Support Systems, M.J. Ginzberg, W.R. Reitman, and E.A. Stohr, (eds.) Elsevier North-Holland, Amsterdam, Holland, 1982, pp. 79-96.

[8] Hubka, V. Principles of Engineering Design, Butterworth Scientific, Boston, Massachusetts, 1982.

[9] Mason, R.E.A. and Carey, T.T. “Prototyping Interactive Information Systems,” Communications of the ACM, Volume 26, Number 5, May 1983, pp. 347-354.

[10] McCracken, D.D. and Jackson, M.A. “A Minority Dissenting Position,” in Systems Analysis and Design, W.W. Cotterman, J.D. Couger, N.L. Enger and F. Haroki, (eds.) Elsevier North-Holland, Amsterdam, Holland, 1981, pp. 551-553.

[11] Naumann, J.D. and Jenkins, A.M. “Prototyping: The New Paradigm for Systems Development,” MIS Quarterly, Volume 6, Number 3, September 1982, pp. 29-44.

[12] Rzevski, G. “Prototypes versus Pilot Systems: Strategies for Evolutionary Information System Development,” in Approaches to Prototyping, R. Buddy, K. Kuhlenkamp, L. Mathiassen, and H. Zullighoven, (eds.), Springer-Verlag, Berlin, Germany, 1984, pp. 356-367.

## About the Authors

Marius A. Janson received his Ph.D. from the University of Minnesota. He is an Assistant Professor of Management Information Systems at the University of Missouri-St. Louis. Dr. Janson has worked for N.V. Philips Gloeilampenfabrieken, The Netherlands, Honeywell, and Research, Inc. His publications have appeared in various journals including Decision Sciences, Information and Management, and Systems, Objectives, Solutions.

L. Douglas Smith (Ph.D., University of Minnesota) is an Associate Professor of Management Science and Director of the Center for Business and Industrial Studies at the University of Missouri-St. Louis. Dr. Smith has served as a consultant to a variety of organizations, including the Williams Pipe Line Company, Interprovidential Pipeline Co., Northwest Energy Co., Southwestern Bell Telephone Company, and Shelter Insurance Companies. He is author or co-author of more than 20 papers appearing in national and international professional journals.
