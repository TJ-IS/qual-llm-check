---
otero_id: 16916
otero_key: "WRS72EGW"
title: "A model management system to support policy analysis"
authors: "Louis W Miller; Norman Katz"
year: "1986"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(86)90121-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Model Management System to Support Policy Analysis

Louis W. MILLER and Norman KATZ
The Rand Corporation, 1700 Main Street, P.O. Box 2138, Santa Monica, CA 90406, USA

Model Management Systems are usually discussed in the context of DSS, focusing on the decision maker. But MMS is also useful in large scale policy analyses where there is no single individual decision maker and there are significant problems of communication, coordination, and learning. The use of MMS in support of policy analysis suggests a set of goals for design, and the paper describes a particular MMS that was built to operate with micro-analytic simulation models. The description is based on a framework of steps in using an MMS and gives brief overviews of the information with which the system deals and how users work with the system.

Keywords: Decision Support; Model Management; Policy Analysis; Simulation

![](/api/attachments/WRS72EGW/fulltext/images/0889aa2243594fc13b0fce353723141c637e98e88774e5036e1b0c279a8e647a.jpg)

Louis Miller heads the Rand Corporation's Information Sciences Department. The work reported here was done as a member of the faculty of the Decision Sciences Department at the Wharton School of the University of Pennsylvania. With interests in operations research and decision support systems, he has had extensive experience in policy analyses related to logistics systems and natural disasters. Dr. Miller is coauthor of Theory of Scheduling (Addison-Wesley, 1967)

and Disaster Insurance Protection: Public Policy Lessons (Wiley, 1978).  
![](/api/attachments/WRS72EGW/fulltext/images/fd1b8fe2f5d151d1d784cd6a37cd61e1a2c79f16157ebe7543799deb52b1f59f.jpg)

Norman Katz is an independent consultant, working in the areas of software systems design, data management, and human-machine interaction. Prior to that, he was a policy analyst in the information sciences department at the Rand Corporation. Mr. Katz has a M.S. in computer science from the University of Pennsylvania.

## Introduction

Sprague and Carlson [16] list a set of model management functions as the abilities (page 33):

(1) To create new models quickly and easily.

(2) To access and integrate model building blocks.

(3) To catalog and maintain a wide range of models.

(4) To interrelate models with appropriate linkages through the data base.

(5) To manage the model base with functions analogous to data base management (e.g., storing, cataloging, linking, and accessing models.)

Model Management Systems (MMS) is usually discussed in the context of DSS, but large-scale policy analyses are different from the scenarios usually associated with DSS. Yet meeting the needs of policy analysis presents challenges and opportunities for model management. Moreover, focusing on the MMS also serves to point out to the modeling community that there is much that could be done to make models more usable regardless of the decision making context. Modelers often devote their energies to the pure modeling aspect with the result that the models are difficult to set up, modify, and analyze.

Many of our thoughts were shaped by experience in building and using a particular model management system, and the paper describes aspects of that system to give a concrete example of an MMS that begins to address the abilities mentioned above. The system is called WHIMS (Wharton Interactive Modeling System) and was built to manage micro-analytic simulation models [14]. WHIMS does not utilize sophisticated concepts from data base management and artificial intelligence. Instead, if focuses on how models are described to the MMS and the architecture to achieve interactions between models. We believe that these are central issues that need more exploration in general, and without which discussions of data base models and AI are only abstract theory.

The paper is organized as follows. Section I describes typical organizational characteristics of modeling activities in support of policy analyses and discusses problems to be solved and goals for MMS. Section 2 is about the kinds of models with which WHIMS deals. Section 3 sets up a framework for dealing with MMS by enumerating steps in using models, and a number of design issues are raised. Sections 4 and 5 describe WHIMS in terms of the framework. Section 4 explains information that WHIMS deals with, and Section 5 shows how users work with the system.

## 1. The Modeling Environment in Policy Analysis

Policy analysis seeks to provide information for stakeholders dealing with a set of decisions involving the public welfare. The issues are often complicated and are viewed differently by different actors. Many aspects appear to lack structure, and there is not an identifiable decision maker; decisions are taken as the result of complex political processes. This contrasts with typical DSS scenarios that focus on the decision maker. For a brief summary of an exceedingly complex policy analysis project that employed many models see Goeller [6]. The books by Greenberger et al. [7], House and McLeod [10], and Brewer [3] provide valuable insights into the nature of relationships among modelers and policy makers.

MMS for policy analysis should seek to alleviate problems of:

(1) communication and interfaces among members of the analysis team,

(2) interfacing submodels,

(3) accommodation of learning and changing views of the problem,

(4) cumbersome models that inhibit effective utilization.

The problem of communication and interfaces among analysts arises because policy evaluations usually involve multidisciplinary teams to shorten the time required by the study and to bring to bear knowledge, modeling techniques, and points of view from a variety of disciplines.

Interfacing submodels is necessary because the multidisciplinary approach requires that the problem be decomposed and submodels created. Eventually a synthesis of models occurs in order to evaluate tradeoffs. Moreover, there is borrowing of submodels when one analyst develops a model of a particular process and other analysts need a model of the same phenomenon.

Learning occurs because new data and better theories about phenomena become available, new alternatives get invented, and views about what are important criteria change as the study progresses. In short, the model is a moving target. While the final report of a policy evaluation may give the impression that study progressed through a neat sequence of steps, it is likely that, as pointed out by Quade and Boucher [15], “to one degree or another [the steps] are all occurring simultaneously.” Both the analysts and the clients participate in learning processes, implying a need for flexibility of the modeling tools.

The book by House and McLeod [10] cites a variety of instances and includes several telling quotations to illustrate failures traced to models that were too cumbersome and inflexible.

In attempting to deal with these problems, WHIMS was designed to address the following goals and characteristics:

(1) Flexibility. We need the ability to change models without making extensive modifications to large programs and with minimum danger of introducing errors. Modularity and the ability to combine submodels are the means for achieving flexibility.

(2) Understanding and explaining models. Unless models are carefully organized and documented, they are confusing and assumptions get hidden. We wish to encourage the structuring of models in ways that make them easy to understand, but impose the discipline in a way that model builders will find comfortable. A good modularity scheme is the foundation for understandable models.

(3) Documentation. Users need easy access to information about models, data used by the models, and past results of running models. Users of MMSs create great amounts of information and computer files of various types over time. They need help in keeping track of all this.

(4) Handling users' data. Requiring the user to format inputs is an unnecessary distraction. Help should be available, errors easily corrected, data should be saved so that reentering information for successive model runs can be avoided, and changes should be easy. The user needs good visibility and control of what he is doing. Implementors of models should not bear the responsibility for coding user dialogues. Dialogues should be managed in a uniform fashion regardless of the particular model for which the user is supplying data.

(5) Separation of modeling and analysis. The designer of a model cannot foresee how outputs will be analyzed, so procedures to analyze and display results should be separate from the model. The user should be able to specify modes of analysis after the model has been run. This provides a useful separation of activities for the model user and it encourages exploratory analysis without overwhelming the user with data and paper. In WHIMS, goals 4 and 5 are met by having all input/output operations done by the MMS rather than the models themselves.

(6) Quality interface. The human-user interface should be built to high standards. Errors should be regarded as requests for help, not mistakes. Above all, the interface needs to make sense to users.

## 2. WHIMS Models

WHIMS is not a model, but an operating system-like shell for managing microanalytic simulation models [14]. Microanalytic simulations are used to model populations of individuals who interact with events and policies during their simulated life cycles. The models are disaggregated, with the unit of analysis being a single person or family, analogous to queuing simulations dealing with individual jobs or customers.

There are three reasons for not using more aggregated models. First, the policies under investigation apply to individuals, and aggregation would make faithful representation of the policies impossible. Second, there is usually a requirement to analyze the distributional effects of policies – how are various subgroups affected? Third, variances need to be analyzed and not lost through aggregation.

WHIMS was built to support models dealing with policies about mitigation and recovery from natural disasters, although there is nothing in the WHIMS system that specifically relates to the application. The modeling efforts grew out of an investigation of insurance buying behavior of homeowners in disaster-prone areas [13]. A nationwide survey produced a wealth of data about individuals' attitudes, behavior, experiences, and knowledge about mitigation and recovery programs. We wished to use the resulting data base together with information from other researchers, particularly in civil engineering and economics and finance, to develop models for studying implications of policy alternatives, since there is considerable governmental and public concern about natural hazards.

A typical model for comparing financial implications of various mitigation and recovery policies relating to flood disasters would proceed along the following lines. The simulation operates on a data base describing a sample of homeowners, with each homeowner represented by a record containing values of attributes relating to the physical characteristics of the house and socioeconomic descriptors of the family. For modeling purposes we usually think of three phases in the life cycles of the entities. During the pre-disaster phase there could be submodels that would do some or all of the following: locate the house in an area of the community and assign an elevation to the house, infer a variety of financial characteristics not in the original data base, and decide whether or not various mitigation measures had been taken (e.g., flood proofing, purchase of flood insurance). Locations of houses in the flood plain and adoption of mitigation measures are influenced by policies that would be experimental variables. The second stage is a simulated flood, where the severity of the flood is an experimental variable and dollar values of damage would be the result. The third, post-disaster, phase simulates the ways in which individuals attempt to recover losses through a variety of submodels relating losses, socioeconomic characteristics of the victims, and policies regarding insurance, loan, and grant programs.

This description shows both the opportunity for modularization and the need for coordination among modelers. Modularizing models is simplified because the entities do not interact and because the life cycles of the entities move in one direction with no cycling. For example, modeling damage phenomena was the job of civil engineers who relied upon the economics expert to supply the submodel that determines the pre-disaster values of properties. The team member responsible for modeling post-disaster policies depended on the economist's submodels for financial characteristics of homeowners and on the results of the engineers' damage models.

A good modularization scheme brings several benefits. The various modelers need communicate about the inputs and outputs of the submodels for which they are responsible, but they do not have to understand each other's submodels in detail. It is possible to change parts of the overall model without changing the rest. For example, we started with crude models of damage and substituting more sophisticated ones later did not affect other submodels. Also, it is easy to expand or contract the scope of a model, adding or removing modules dealing with particular policy components. WHIMS also allows models to be run in stages, which could be desirable in complicated studies.

A WHIMS model acts like a file processor. It cycles through an input file of entity records and produces an output file with the same number of records, but with more attributes. The results of the simulation are recorded by the additional attributes representing such things (in the disaster example) as the values of damage, insurance settlements, loans, and other financial aid. The job of a particular module is to calculate a few of the new attributes, which we call created attributes. In order to perform its computation, a module needs to be given the values of some other attributes. We call these the module's given attributes, which may be attributes whose values are in the input file, or they may be attributes that are created by some other module in the model. For each entity, every module in the model is called in turn. A central problem is setting up the control structure to insure that every module is provided with values for its given attributes and that the modules are called in a feasible order.

From this we see that the fundamental notion of WHIMS is linking together modules. But building on that notion allowed us to devise a MMS that addressed the six goals and characteristics mentioned in Section I. In so doing, a number of design issues of general interest to MMS were raised (which is a virtue of actually building systems). These are discussed in the next section with the help of a framework based on a view of what users of a MMS do with the system.

## 3. Steps in Using a Model Management System

Below are listed seven steps in using a MMS focused on the user's interactions with a computer. In addition to providing a framework for exploring issues in the design of an MMS, the steps create a basis for understanding WHIMS as a system rather than a collection of files, commands, and displays.

(1) Introduce new models (or modules) into the MMS.

(2) Select appropriate modules to comprise a model.

(3) Arrange for communication among modules and for controlling their execution.

(4) Locate data from a data base and arrange for its extraction and transmission to the modules that will use it.

(5) Specify the user's specific inputs and arrange for them to be transmitted to models.

(6) Run models and arrange for saving the outputs.

(7) Perform analysis of the inputs and outputs of the runs.

Designing a MMS to support these activities requires considering which aspects can be done automatically and how the system helps when the user must become involved. Examining the seven steps with these questions in mind raises the following points, which show that there are dependencies among the steps.

Step 1. Introducing new models into the MMS is often regarded as a low level, technical task since it involves programming. A MMS is stronger if, once a model is coded, the services of a systems programmer are not needed.

Step 2. Much discussion of MMS is directed at providing users with information about the contents of the model base with analogies drawn between data base management and model base management. This is obviously tied in with step 1 through the need to introduce information about models. WHIMS has a model documentation language that satisfies this need. Moreover, attention should be paid to the fact that in trying to solve some problems we may be creating additional information-processing problems for the user.

Step 3. Arranging for control and information transfers among several models can be confusing, and the user should be given help. This is particularly true with WHIMS because models are usually comprised of many building blocks. When one model supplies information for another, there are formatting and semantic problems in making sure that the receiving model interprets what it is getting properly. If one model produces a forecast and another model needs a prediction, the equivalence has to be established. If we want a system where the user never becomes involved with such semantic interpretations, there will have to be strict restrictions or conventions. If such restrictions are undesirable, the user may need to help. Then we must supply the user with information that will allow him to participate. WHIMS modules communicate only through attributes of entities, which are scalars. Thus there is no formatting problem. WHIMS can handle the semantic problem if the module designers have used consistent names in different modules. Otherwise, the user helps.

Step 4. Getting data from a data base to a model is similar to the information transfer problem of step 3; in WHIMS the problems are identical.

Step 5. Users' inputs means data that a model would obtain from prompting a user rather than from a data base. WHIMS modules do not converse directly with users. In fact, they do no I/O operations at all. Instead, the documentation language that goes with a module describes the needed data, and all conversations with the user are carried on by the MMS. There are several advantages. One is that the data can be saved by the MMS both as documentation of an execution of the model and to allow the model to be run several times without having to prompt for all the data again. (Users are prompted for data during the model building process in step 2. Requests that are deferred are repeated at step 6 when the model is run.) A second reason for letting the MMS do the prompting is that user interactions will be better and more uniform; errors and requests for help are handled in the same way regardless of whose module needs the data. Finally, it is folly to expect implementors of models to do a satisfactory job of programming user interactions.

Steps 6 and 7. In WHIMS, running models and analyzing the results are separate steps. In many cases this separation of activities is good for the user. Allowing the user to manipulate model outputs with something resembling an interactive statistical package encourages exploratory analysis without overwhelming the user with masses of uninteresting results. Separation of model execution and analysis also permits analyses that compare several model runs. If reporting of results is the responsibility of the modules in a model, we would have to rely on the modules' designers to guess what the analyst wants to see. WHIMS has an analysis subsystem that is similar to an interactive SPSS, but does not require the mass of boilerplate required by SPSS, and new, custom created analysis routines can be added in a manner similar to adding new modules to the model base. Interestingly, the user interface to the analysis system is almost identical to the interface to the model building and running interface.

The following two sections elaborate on how the issues raised in Section 3 were applied to the models discussed in Section 2 to achieve the goals set in Section 1.

## 4. The Information Base of WHIMS

We think of WHIMS as maintaining four categories of information, although there are many interrelationships:

(A) Modules available in the WHIMS libraries for building models are described by documentation language prepared when modules are coded. The same is true of analysis routines.

(B) Files of attributes used as model inputs and files created by executing models (output files can be used as inputs to other models) are described by descriptor files.

(C) Documentation about model runs is also contained in descriptor files.

(D) Template files describe models and are the means for saving models.

In explaining these information items, we shall examine the roles they play in conjunction with the steps outlined in Section III.

Information about modules (item A) originates as documentation statements prepared when modules are designed and coded. WHIMS modules are coded in FORTRAN, but the documentation is in a special language that is both easy to write and easy to read (and marked as comments so as not to upset the compiler). Most information handled by WHIMS and the processes carried out with the system depend one way or another on documentation language statements.

Documentation statements deal with three topics: (1) identification of the module, (2) specifications for user-supplied data, and (3) identification of given and created (input and output) attributes.

(1) Identification statements are used to establish meaningful names by which users can refer to modules (as opposed to FORTRAN names) and to supply generic categories for grouping modules by subject matter. This helps users to locate modules while building models. Descriptive text is included with the identification statements.

(2) The previous section discussed the benefits of having users supply data through the MMS rather than interact directly with modules. Statements in the documentation language tell WHIMS how to prompt for data including type (e.g., integer, real, file name, yes/no, dimensionality, etc.) and text for prompts, help, and annotating data in documenting model runs. WHIMS acts upon these statements during step 2 when a user specifies that a module be included in a model or in step 6 when the model is run if the user defers responding at step 2. Sometimes the need for a particular data item depends on the responses to earlier prompts. It is possible to establish such conditional prompting. User-supplied data for a module is accessed in the FORTRAN code of the module by means of special functions available to the programmer.

(3) Identification of given (input) and created (output) attributes provides an opportunity for supplying textual information to users and is the main clue that WHIMS uses in attempting to link modules without help from the user. Users building models may supply more meaningful aliases (called user names) for these short FORTRAN names.

Documentation language is intended to serve both the needs of WHIMS and its human users. The information contained in modules' documentation is easily accessible to users through flexible LIST and DESCRIBE commands.

Information about data files (item B). Files of attributes, which are the inputs and outputs of models, are simple flat files of data. Information about attribute files is maintained in matching descriptor files, which are produced by WHIMS as a byproduct of running a model, or they are prepared interactively with the help of WHIMS if a model is to be used with a foreign file as input. The most important information is the identification of fields in the records, which associates field numbers with user names for the attributes. For each attribute created by a model, the name of the module that created the attribute and the attribute's internal name is given. This serves to tie outputs of models back to documentation language statements should the need arise to recall such details.

Additional Information about runs (item C) contained in a descriptor file is identification of the model that produced the file and the name of the descriptor for the attribute file that was used for input. A descriptor file also contains all of the user's data for the run, annotated by comments originating in the documentation language statements belonging to the model's modules.

Information about Models (item D) is contained in template files. Template files, which are human-readable, are all that is saved from the model building process. A saved template may be loaded for examination and modification, and serves as a specification of the model when WHIMS runs the model. A template file contains a cleaned-up version of the user's end of an interactive session in which the model might have been built (steps 2–5), and contains four kinds of model building commands mentioned in the following section.

## 5. Using WHIMS

WHIMS contains three subsystems: LIBRARY to manage libraries of modules, MODEL to build and run models, and ANALYSIS to summarize and display the results from models. The MODEL and ANALYSIS interfaces are quite similar.

LIBRARY is used to introduce, remove, and modify modules in the WHIMS libraries. It processes documentation language statements and saves the information. LIBRARY also takes care of compiling the modules and saving the object code. A MMS that does not have a comparable subsystem would require an expert to perform these services.

Within MODEL, building a model produces a template file for the model. A template is like a high-level, nonprocedural program, but building a template is different from programming. First, the user may employ a variety of commands to access information at any time, even in the middle of another command. Second, WHIMS pays attention to what the user is doing and can provide considerable help, coaching, and error detection. Once a command has been accepted, the user can be assured that it is correct to the extent that it can be checked with the information currently available to WHIMS.

The CREATE command is the most frequently occurring of the four kinds appearing in template files. It calls for inclusion of a particular module and gives user names to the module's created attributes. An example is:

Command (M): create 'hgt h2o rel 1st flr' 'structure damage' using damage.flood

where the items in quotes are user names for created attributes and damage.flood is the module being selected. When the user types such a command to the MODEL interface, WHIMS will prompt the user for data as specified in the module's documentation language description, and the responses will be saved in the template. There are mechanisms for allowing the user to change the data later or nullify the CREATE command altogether. There is no reason why a particular module may not be used more than once in a model.

If the user wants to create attributes by direct computation, a COMPUTE command may be given:

Command(M): compute 'total damage' = 'contents damage' + 'structure damage' done

A compression list to remove unwanted attributes from the output file can be specified with a COMPRESS command such as:

Command(M): compress using 'house type' 'level 1st floor' done

In Section 2 we asserted that the most fundamental issue is linking modules, and this is likely to be true of any MMS that employs similar concepts of modularity. In WHIMS, this comes down to being able to identify every given attribute of a module as either the created attribute of some other module or an attribute being read from the input file. WHIMS attempts to establish linkages by matching internal names for attributes. If this fails (and there will certainly be ambiguities if a particular module is used more than once in a model), the user must help by issuing LINK commands such as:

Command(M): link value in module creating 'mod structure coverage' to 'structure value'

WHIMS has a CHECK command that shows how it would link the model given the information that it has along with indications of given attributes that it is unable to link. This is a powerful aid to achieving correct models and is valuable as documentation.

Running a model is rather simple for the user, if not for WHIMS. A typical RUN command is:

Command(M): run flood on philly making mess

In this command, FLOOD is the name of the template file, PHILLY is the descriptor file for the input, and MESS is the name of the descriptor file for the model's output. WHIMS will now ask the user to supply any deferred data and then get busy with a series of activities without further user involvement. WHIMS links the given attributes, works out a feasible sequence for calling the modules, writes a main routine in FORTRAN to run the model, writes the output descriptor file, and submits a job to the batch system which compiles the main routine and runs the program to produce the output attribute file.

The ANALYSIS subsystem (step 7) is used to make meaningful reports out of the files produced by running models. There were four objectives that led us to build our own rather than continue to use SPSS. We wanted to:

(1) make analysis interactive,

(2) have the analysis system extensible in the same way that MODEL is,

(3) have the analysis subsystem resemble as much as possible the modeling part of WHIMS, and

(4) have the ability to process several files simultaneously to facilitate comparisons of model runs.

ANALYSIS modules are a bit more complex technically than are MODEL modules because of the arrangements that have to be made to pass information to the modules and the need to build up data structures as records are processed. But these are problems for programmers implementing new modules, not ordinary users. WHIMS provides data structuring mechanisms that are useful in building tables and the like within the modules.

Users of ANALYSIS have all the information tools that are available in MODEL, and the specialized commands are analogous to MODEL commands. For example, to specify that an ANALYSIS procedure be applied to a set of attributes, the ANALYZE command is similar to CREATE:

Command(A): analyze 'structure damage' 'house value' 'hgt h20 rel 1st flr' using stat.multi.regression

In addition to ANALYZE statements, the COMPUTE statement is available to manufacture new attributes, and there are RECODE and SELECT commands similar to those in SPSS. Once an analysis template has been created, it can be executed with a RUN command like:

Command(A): run tellme on flood47 flood65 flood86

where TELLME is the name of an analysis template and FLOOD47, etc. are the names of descriptors for attribute files to be analyzed.

Complete details of working with WHIMS, including many examples showing user interactions may be found in Katz and Miller [11].

## 6. Conclusions

Efforts to enhance the usability of computers in modeling activities have been under way for many years. There currently is much discussion of accomplishing even more under the umbrella of DSS. MMS is recognized as an important component of DSS, but this paper argues that Model Management should be important to the field of policy analysis, even though policy analysts are not the intended clients for much of what is seen in the mainstream of DSS.

A specific, existing MMS has been described in order to enumerate some of the services that a MMS can provide and some design goals. The system does not employ any sophisticated ideas from the data base management or artificial intelligence fields that are popular topics in the literature of DSS. But the experience has raised some design issues and trade-offs that may not be apparent without actually building systems. We believe that the most important idea raised comes from the fact that most of the system depends on the rules for documenting modules and the conventions established for communication between modules. We expect that these aspects will be the critical features of any MMS, and it is not possible to build an effective MMS in which the models are treated as black boxes.

## Acknowledgements

This work was supported in part by grants NSF 76 12370 and PFR 77 26363 to the University of Pennsylvania.

## References

[1] J.L. Bennett, (ed.), Building Decision Support Systems. Addison Wesley, Reading (1982).

[2] R.H. Bonczeck, C.W. Holsapple and A.B. Whinston, Foundations of Decision Support Systems. Academic Press, New York (1981).

[3] G.D. Brewer, Politicians, Bureaucrats and the Consultant. Basic Books, New York (1973).

[4] F. Brooks, The Mythical Man-Month. Addison Wesley, Reading (1975).

[5] C.W. Churchman, R.L. Ackoff and E.L. Arnoff, Introduction to Operations Research. Wiley, New York (1957).

[6] B.F. Goeller and the PAWN TEAM, Planning the Netherlands' Water Resources. Interfaces, Vol. 15, No. 1 (Jan - Feb 1985).

[7] M. Greenberger, M.A. Crenson and B. Crissey., Models in the Policy Process. Russel Sage Foundation, New York (1976).

[8] H.R. Hamilton, S.E. Goldstone, J.W. Milliman, A.L. Pugh, III, E.B. Roberts and A. Zellner, The Management of a Multidisciplinary Research Project (Appendix A) in Sys-

tem Simulation for Regional Analysis - An Application to River Basin Planning. MIT Press, Cambridge (1969).

[9] B. Harris, Quantitative Models of Urban Development: Their Role in Metropolitan Policy Making in H.S. Perloff and L. Wingo, Jr. (eds.) Issues in Urban Economics. Johns Hopkins University Press, Baltimore (1968).

[10] P.W. House and J. McLeod, Large Scale Models for Policy Evaluation. Wiley, New York (1977).

[11] N. Katz and L. Miller, An Interactive Modeling System, Working Paper 77-09-02, Department of Decision Sciences, University of Pennsylvania, Philadelphia, PA. (1977).

[12] P.G.W. Keen and M.S. Scott-Morton, Decision Support Systems, An Organizational Perspective. Addison Wesley, Reading (1978).

[13] H. Kunreuther, R. Ginsberg, L. Miller, P. Sagi, B. Borkan and N. Katz, Disaster Insurance Protection. Wiley, New York (1978).

[14] G. Orcutt, M. Greenberger, J. Korbel and A. Rivlin. Microanalysis of Socioeconomic Systems: A Simulation Study. Harper (1961).

[15] E.S. Quade and W.I. Boucher (eds.), Systems Analysis and Policy Planning: Applications in Defense. American Elsevier, New York (1968).

[16] R.H. Sprague and E.D. Carlson, Building Effective Decision Support Systems. Prentice Hall, Englewood Cliffs (1982).

[17] H.M. Wagner, Principles of Operations Research. Prentice Hall, Englewood Cliffs (1969).

[18] A.H. Voelker, Some Pitfalls of Land-use Model Building. Oak Ridge National Laboratory, Oak Ridge (1975).
