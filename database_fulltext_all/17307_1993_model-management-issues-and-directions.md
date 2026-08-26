---
otero_id: 17307
otero_key: "SXXFQCVM"
title: "Model management issues and directions"
authors: "Ai-Mei Chang; Clyde W. Holsapple; Andrew B. Whinston"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90020-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Model management issues and directions

Ai-Mei Chang

University of Arizona, Tucson, AZ, USA

Clyde W. Holsapple

University of Kentucky, Lexington, KY, USA

Andrew B. Whinston

University of Texas, Austin, TX, USA

This paper examines two fundamental issues of model management: What is it that is being managed and what is the DSS context in which model management occurs. How a researcher answers these questions will shape ensuing research efforts. We then consider research directions that have been pursued in terms of the issues of developer tools, analysis dynamics, and usage settings. We conclude with a new direction for model management research, which involves a hyperknowledge paradigm.

Keywords: Analysis dynamics, Concepts, Development tools, DSS frameworks, Environment, Hyperknowledge, Knowledge management, Knowledge system, Language system, Messages, model, Model management, Presentation system, Problem processor.

![](/api/attachments/SXXFQCVM/fulltext/images/32bc3d812250802ab99802af81d5c39008a8b2f17845b2409441abffbd98416c.jpg)

Ai-Mei Chang is Assistant Professor of Management Information Systems in the College of Business and Public Administration, University of Arizona. She holds a Bachelor's degree in Computer Science and Mathematics and a PhD. in Management Information Systems, from Purdue University. Her research interests include decision support systems—theory, design and development, computer supported collaborative systems, distributed artificial intelligence and expert systems.
Correspondence to: Ai-Mei Chang, Management Information Systems, University of Arizona, Tucson, AZ 85721, USA.

## 1. Introduction

Within the decision support system (DSS) field, there is a growing body of work focusing on the topic of model management. It is concerned with computer-based means for representing and processing models. It aims to increase the productivities of decision makers, DSS developers, and modeling experts. Our dual purpose here is to offer a useful perspective on progress that has been made and to sketch out a unifying paradigm for stimulating further advances. This paradigm involves the notion of a hyperknowledge environment furnished with diverse, yet synergistically integrated, knowledge management techniques.

In examining what has been published about model management, it quickly becomes apparent

![](/api/attachments/SXXFQCVM/fulltext/images/98f2475a2c0a5db6d12586786c0ce311b3a241ebcf4217c9a5ea324c04b7b4b5.jpg)

Clyde W. Holsapple is Professor of Decision Science and Information Systems and holds the Endowed Chair in Management Information Systems at the University of Kentucky. In addition to this books in the decision support system, data base management, and expert system areas, he has many research articles published in such journals as Decision Support Systems, Operations Research, The Computer Journal, Organization Science, Decision Sciences, IEEE Expert, Fi nancial Management, Policy Sciences and Recherche Operationnelle. Dr. Holsapple is the DSS Area Editor for ORSA Journal on Computing and Associate Editor for Organizational Computing.

![](/api/attachments/SXXFQCVM/fulltext/images/aeef504acf02c1812b2435665403c5c11922db1a8c13760a3ce49ddbedf6d05e.jpg)

Andrew B. Whinston is Professor of Information Systems on the faculty of the College and Graduate School of Business, Department of Management Science and Information Systems at the University of Texas at Austin. His primary teaching interest is management information systems. His current research interests include data base management and applications of artificial intelligence to economics and management. He has also studied applied economics, regulatory

economics, and accounting theory. Among his numerous publications, he has co-authored two books (with C. Holsapple and R. Bonczek), Foundations of Decision Support Systems (Academic Press, 1981), and Micro Database Management – Practical Techniques for Application Development (Academic Press, 1985). He has been a consultant to various companies, governmental agencies, and international organizations on data processing questions.

that there are two key questions that need to be answered. First, what does the author mean by the term ‘model’? Although its meaning is usually taken for granted, there are distinct alternatives that strongly color different researchers’ approaches to the model management topic. Second, what is the DSS context in which model management occurs? A researcher’s response to this question about DSS constitution strongly influences the limits and direction of subsequent investigation into model management possibilities. Section 2 discusses the various answers to these two key questions and their impacts on model management research.

Against this background, Section 3 surveys major streams of model management research. The survey is organized in terms of three issues: Developer tools, analysis dynamics, and settings for usage. Section 4 describes the environment paradigm and comments on its relevance to model management research. We conclude with a summary of pertinent research issues and directions.

## 2. Models and their contexts

Interest in computer-based modeling predates emergence of the DSS field (e.g., [19,33]). Algorithms developed by management scientists, econometricians, and statisticians for analyzing data were formally specified as computer programs. The user of such a program would specify some set of data to be analyzed and, as a result of program execution, receive some new data. This derived data might be viewed as being forecasts, summaries, facts, or beliefs. Libraries composed of commonly-used analytic programs appeared as a natural step beyond the function libraries that accompanied programming languages in the 1960s.

Formative work in the DSS field argued that both data and analytic programs can help support decision makers $[35]$ . Moreover, they should be made available to decision makers through interactive computer-based systems that help solve semi-structured or unstructured problems. Such systems came to be known as decision support systems and their analytic programs were often called models (e.g., $[44,64,73]$ ). However, by the end of the 1970s it had become clear that a DSS could involve other types of knowledge aside from data and models. In addition, DSS researchers began to use the term ‘model’ to refer to something other than an analytic procedure.

## 2.1. What is a model?

Obviously, a grasp of model management depends on an understanding of what it is that is being managed. Precisely, what is a model? Often, this question is not answered explicitly or clearly in model management literature. Authors may take it for granted that readers share their own conceptions about models. Yet an examination of the literature reveals that very different notions about models underlie work that has been done in the model management area. Awareness of these distinctions can help organize a consideration of what has been and remains to be accomplished with respect to the topic of managing models.

The earliest, and perhaps predominant, DSS view of models is that they are procedures, automated algorithms whereby data can be analyzed in response to stated problems. In discussing the notion of a model bank, Will [78] speaks of models being executed. As one DSS design criterion, Sprague and Watson [72] suggest the need for a command language to accomplish both data access and model execution. Early publications describing actual DSS implementations also viewed models as programs whose execution by a DSS would satisfy user requests (e.g., [44,56,64]). In [44] for instance, the DSS had a bank of models (i.e., library of executable routines) that could process queries for both data retrieval and model execution.

Standard books in the DSS field also treat models as computerized procedures that need to be managed [16,71]. Much subsequent research has echoed this treatment. For instance, Blanning [5,6] views a model as a virtual relation whose structure consists of input attributes and output attributes. Underlying this logical view is a procedure which, when run with a tuple's input attribute values, will generate values of that tuple's output attributes. In a similar spirit, the notion of virtual records for procedures has been explored with a network architecture [17]. In their discussion of representing modeling knowledge, Fedorowicz and Williams [31] consider a model base to be a set of procedures. In his functional architecture for detecting and eliminating computational redundancies, Orman [62] views models as computational units. Ghiaseddin's model management language [34] is concerned with the manipulation of procedural modules. As a final example, the use of machine learning to automate aspects of model management is concerned with the manipulation of programs [66].

A different view of models treats them as data that are to be analyzed by a procedure. For instance, the objective function and constraints that describe (i.e., 'model') some situation are inputs to a math programming procedure. This is consistent with terminology employed for some kinds of problems in the operations research field, where models are input to solvers. On the other hand, within that same field reference to an EOQ model usually denotes a procedure that calculates economic order quantities for varying inputs. Thus, the DSS field is not alone in allowing multiple meaning for the term. But in the DSS case, such distinctions have significant implications for what constitutes model management.

Regardless of nomenclature, it should be clear that the management of both procedures and their data inputs are important topics for DSS research and practice. Early efforts in the latter area showed how data base management techniques could be used to manage inputs to math programming procedures $[8,9]$ . The resultant 'model' schema allowed matrices to share common data, treatment of functional coefficients, efficient storage of sparse matrices, accommodation of non-numeric data, and direct ad hoc query access. The notion of program record types was also introduced as a way for organizing similar and related procedures via data base management techniques. Similarly, Konsynski $[57]$ put forth the notion of a 'model database' encompassing both solution procedures and their inputs. He characterized the latter in terms of equations and elements such as time-series descriptions. Along the same lines, Stohr and Tanniru $[74]$ discuss the management of both programs and their inputs via a CODASYL-network data base management system.

When an analytic procedure is executed with some data inputs, a problem is being solved. The nature of that problem statement is an interesting issue. A taxonomy devised to characterize languages for directing retrieval and computation indicates there are many possibilities [13]. These range from entirely procedural specifications (i.e., the problem statement is a model, in the procedural sense) to entirely non-procedural statements that simply request some information (i.e., causing procedures to be executed with appropriate inputs). There is a middle ground, where the problem statement identifies a procedure that is to be executed and specifies what inputs it is to use. Such a specification may take the form of a query, designating that some inputs (e.g., a constraint matrix and objective function) stored in the DSS should be used by the procedure [9]. Alternatively, the specification may include a full expression of the inputs. For instance, the user's problem statement would include an explicit and complete specification of the constraints and objective function that are to govern a math programming procedure's execution.

This gives rise to a third interpretation of the model notion. Rather than regarding a model as a procedure or as data, a model is considered to be a problem. Although related to the model-as-data view, this perspective casts a different light on what it means to manage models. Rather than focusing on the representation and processing of procedures or data, the central concern of this brand of model management revolves around the facilitation of problem statements of the particular kind noted above. Model building is considered to consist of developing a set of equations that are to be ‘solved’ [57]. That is, the equations are a model and are regarded as specifying a problem that the DSS is to solve. Dolk [27] also writes of ‘solving models’, which suggests that models should be seen as problem statements.

Users of packages such as SPSS [61] are quite familiar with such detailed problem statements. But such packages do little to facilitate the activity of stating problems. Research into aids for developing math programming equations and objective functions is quite relevant to this brand of model management [3,60]. Also relevant is Geoffrion's structured modeling work [32]. He presents an approach to stating problems in terms of acyclic, attributed graphs that show variable dependencies. It is claimed that these graphical conventions, together with a corresponding textual language, “provides a framework for modeling within which various problems and tasks can be posed precisely and naturally” [32].

The three streams of model management research outlined above are reflective of Sprague and Carlson's contention that models can be viewed as data, statements, or subroutines [71]. All three views are relevant to the DSS field and no one of them is sufficient to fully account for the use of analytic procedures in a DSS context. But just what is that context? The answer to this question impacts model management investigation just as strongly as one's conception of a model.

## 2.2. What is the nature of the entity providing decision support?

The activity of specifying problems, thereby causing the execution of procedures that analyze data, implies the existence of some entity that reacts to the problem statements. A model management researcher's assumptions about the nature and capabilities of that entity will circumscribe the investigation. If the entity is regarded as incapable of certain knowledge management behaviors, then the model management research results will overlook or ignore those behaviors. It follows that model management research should be concerned with characterizations of the decision support entity that are both accurate and expansive.

Some decision support entities are human $[14,53]$ . They may be individuals, groups, or organizations. Understanding the nature of these may offer valuable insights into what traits would be desirable to incorporate into a computer-based decision support entity (i.e., a DSS) $[28,48,51,53]$ . How do humans respond to problems that necessitate the analysis of data and reporting of results? A DSS framework may well be applicable to both computers and humans, although not fully capable of explaining the latter. This connection is important not only with respect to efforts at emulating successful human decision support entities, but also with respect to capturing user-specific knowledge in a DSS $[28]$ .

Here, we focus on two DSS frameworks that are widely referenced and have had major impacts on shaping DSS (including model management) research over the past decade. Each framework is concerned with characterizing the constitution and possible abilities of a decision support system. Each offers a basis for thinking about and designing both DSSs and software tools that can be used to build DSSs. They are examined here with particular attention to their model management implications. The framework of Sprague and Carlson [7] is considered first. For brevity, it is referred to as the SC framework. The framework of Bonczek, Holsapple, and Whinston [14] is then surveyed. It is referred to as the BHW framework.

Even though some in the DSS field seem to regard the two frameworks as dissimilar or even somehow competitive, we do not. The fact of the matter is that they are quite consistent and compatible. This compatibility is not so much complementary as it is supplementary. The SC framework is a special case of the BHW framework that provides supplemental details about problem processor constitution and allowable knowledge system contents. A considerable amount of model management research and development has occurred within its confines. Alternative realizations of the BHW framework are not only possible, but have served as the basis for implementing DSS development tools (e.g., [49,52]) that are inadmissible within the SC framework.

The SC framework holds that a DSS has three components: A data base, a model base, and a software system $[70]$ . The data base is a storage repository holding data of direct or indirect interest to the DSS user (i.e., the decision maker). These data are organized according to a schema designed with the conventions of some data model. The notion of data models in the data base management field $[41]$ should not be confused with any of the three model notions discussed earlier. In the SC framework, a model base is a storage repository, holding models (i.e., procedures) of relevance to the user's problem domain. These may be organized into modules (i.e., subroutines) which, when combined in various ways, yield various models for execution. Specific organization methods are not prescribed by the SC framework, leaving the issue open to model management researchers. According to the SC framework, a DSS's software system has three constituents: Data base management software (DBMS), model base management software (MBMS), and dialog generation/management software (DGMS).

The DGMS defines what requests a user can make to the DSS and what kinds of responses the DSS can make to the user. It is designed to accommodate one or another style of interaction, accept requests via appropriate input devices, display responses in appropriate ways, and help the user use the system. The DBMS is software that permits the data base to be defined schematically, loaded with data, modified to remain current, and interrogated for retrieval. Presumably, this interrogation can satisfy the ad hoc data needs of users and the input needs of executing models. The MBMS should provide facilities for the creation, maintenance, and use of model base contents. This is largely analogous to the role of a DBMS relative to a data base, except the MBMS deals with procedures rather than data (e.g., procedures are more likely to be executed than retrieved).

All aspects of the SC framework are allowed in the BHW framework and it, too, has three major components. But its three major components for characterizing a DSS are different than those of the SG framework. They are a language system (LS), a knowledge system (KS), and a problem processing system (PPS) [14]. The first two are systems of representation, while the PPS (often called the problem processor) is a software system. The LS and KS fuel the activities of the PPS. The LS is comprised of all requests that the PPS can act on with respect to the current contents of DSS's knowledge system. The KS is comprised of knowledge that the PPS can use in generating responses to user requests.

The PPS is able to process a problem statement (i.e., an element of LS) and in so doing, work with relevant pieces of knowledge (i.e., elements of KS) until a solution is achieved. The solution is perhaps an extraction from KS and reported to the user. Alternatively, the solution may be now knowledge that the PPS manufactures from present KS contents. For instance, a particular request may cause the PPS to select some procedural knowledge from KS and execute it to analyze some of the descriptive knowledge (i.e., data) held in the KS. This produces some new knowledge that is either presented to the user or used to modify the KS.

What is the nature of such a presentation? This may be determined by the PPS based on presentation knowledge held in the KS. How did the PPS recognize the meaning of the original request? The PPS may ascertain the meaning of an LS element by drawing on linguistic knowledge existing in the KS. How did the PPS go about selecting appropriate procedural and descriptive knowledge? The PPS may have an ability to reason and exercise that ability with some reasoning knowledge residing in the KS. Knowledge is not monolithic. It comes in distinctly different types [40,47,52]. Some knowledge is neither procedural nor descriptive, but is meta knowledge that can be used to govern the use of programs and data [16]. Reasoning knowledge (e.g., in the form of rules) is a good example of this.

From the BHW framework's perspective, the SC framework refers to a particular class of DSSs characterized as follows. The KS consists exclusively of a data base representing descriptive knowledge and a model base representing procedural knowledge. Alternative means for representing these two kinds of knowledge are not considered. For instance, text management or rule management techniques for representing knowledge are not included. The problem processor of a DSS adhering to the SC framework is restricted to managing a data base and a base of procedures. The DSS's language system is defined solely in terms of the PPS's dialog software. Similarly, it is the dialog software alone that governs the presentation of analysis results. There is no notion of linguistic knowledge (e.g., grammars, vocabularies, menus) and presentation knowledge (e.g., forms, templates, images) being held in the KS where it can be drawn on by the PPS in handling requests and responses.

By relaxing restrictions on what kinds of knowledge can exist in a KS, how it can be represented, what knowledge management capabilities a PPS can possess, and dialog adaptability, more powerful and flexible DSS possibilities emerge. Consider a conventional expert system (ES) built with a programming language (e.g., LISP) or an expert system shell. Some commentators treat an ES as something quite different than a DSS (e.g., [75]), even though the advice offered by the ES could be very important for supporting decisions. This treatment is understandable within the context of the SC framework. A conventional ES does not employ data base or model base management. On the other hand, the BHW framework easily accommodates expert systems as valid decision support entities [14]. An expert system is a special kind of DSS whose KS is comprised of rule sets and state variables, whose LS consists of requests for advice and explanation, and whose PPS is an inference engine capable of dealing with such requests and carrying out deductions based on KS contents.

Consider another example. Does 1-2-3, and a group of spreadsheets it can process, constitute a decision support system? Few would argue that decision makers do not base decisions on the results of spreadsheet analysis. However, the 1-2-3 software does not include the DBMS component prescribed by the SC framework. Moreover, spreadsheets are not data bases in any technical or rigorous sense of the term. Nor are spreadsheets exclusively concerned with procedures. Rather a spreadsheet is a convenient amalgam of data and procedural knowledge. In a BHW context, 1-2-3 is a PPS able to draw on a KS composed of spreadsheets that hold both descriptive knowledge (cell constants) and procedural knowledge (cell formulas). The PPS supports a very rigid LS and has fixed response-presentation capabilities.

Whether a model management researcher adopts the SC framework, an ES viewpoint, a spreadsheet perspective, or some other conception of decision support entities, it is important to be cognizant of the resultant limitations on what is produced. Because all of these are meritorious and have valuable contributions to make to a full exploration of model management capabilities, we believe a generic framework that embraces them all can offer a unifying context for research and study. The BHW framework is an effort in this direction and is certainly subject to extension and enhancement. For instance, a variant of this generic framework formalizes its notion of responses as a fourth DSS component: A presentation system (PS) composed of all responses the PPS can make to a user $[28]$ . To remain generic in the face of technological advances, it is necessary that a framework does not enforce some preconceptions about what the KS can contain, what knowledge management capabilities the PPS can exercise, or what the elements of LS and PS can be. The possibilities for a decision support entity can then be ground out in the crucible of research.

## 3. Model management research

This section offers a survey of representative research impinging on various aspects of model management. It is intended as a complement to Blanning's survey [7], which examines the literature from two angles: Use of relational concepts for model management and applications of artificial intelligence to model management. Here, the survey is organized differently. We first look at the issue of software tools that aim to address a developer's need for building DSSs that facilitate the analysis of data via procedure execution. Second, there is the issue of analysis dynamics. That is, what can happen within a DSS when a user needs data that necessitate an analysis? Third, some researchers have focused on the settings for analytical DSS usage.

In the interest of precision and clarity, we tend to avoid using the term ‘model’ in this survey. When it appears that an author is using ‘model’ in the sense of a procedure, we simply substitute the term ‘procedure.’ Similarly, when it is used in the sense of data that can be analyzed by a procedure, we substitute the term ‘data’ for ‘model.’ When a researcher is concerned with problem statements posed to a DSS, we use the term ‘problem’ instead of ‘model.’ The discussion employs the BHW framework and the more specialized SC framework as appropriate. In the latter case, the term ‘model base’ should be understood in the spirit of the SC framework: as a collection of procedures that can be executed to analyze data.

## 3.1. Tools

For purposes of this discussion, a tool is a piece of software that aids in the construction or administration of a DSS. It is intended to increase the productivity of DSS developers and administrators. There are various ways to distinguish among types of tools. Some tools are extrinsic. They are external to the DSSs built or administered with them. Other tools are intrinsic. They supply the developer with software that becomes a part of the DSS being constructed, thereby saving programming effort. The 1-2-3 software or an inference engine are examples of intrinsic tools, while a text editor or induction mechanism used to specify an ES's rule set are examples of extrinsic tools. Another distinction lies in the knowledge management technique a tool employs (e.g., spreadsheet vs. data base). Yet another distinction is proposed by Sprague and Carlson [71] who refer to tools that cannot be used to produce other tools as generators, while those that could be used to develop generators are called tools. In other words, some tools (e.g., IFPS) are higher-level than others (e.g. FORTRAN compiler).

DSS research has been much more concerned with the high end of the tool spectrum, in the interest of mitigating development and maintenance difficulties that result from using low-level tools. Moreover, the trend in high-level tools has been from special-purpose toward general-purpose features. A specialized tool is one that is useful for building only a certain class of DSSs. For instance, there are limitations on the kinds of procedures it can handle, on how the procedures can be used, on the style or substance of problem statements and presentations, on means for data representation, or on means for representing and integrating other types of knowledge.

The notion of a generalized problem processing system (GPPS) was advanced to overcome such limitations $[14,39]$ . A GPPS is a single piece of software that can be used to develop DSSs across a wide range of problem domains, having diverse dialog styles and contents, requiring very different analytical procedures and data, and accommodating multiple knowledge management techniques. A GPPS is an invariant, high-level, intrinsic tool. It can serve as the PPSs of drastically different DSSs because of its ability to work with divergent LSs, PSs, and KSs devised by developers for providing support in assorted decision settings.

In spirit, the GPPS notion follows Simon's idea of a Generalized Problem Solver [67]. Along these same lines, the importance of incorporating intelligence into a GPPS has also been recognized [12,39], allowing it to emulate aspects of behavior that would be regarded as intelligent if observed in a human decision support entity. Scott Morton [63] has pointed out that it is no small undertaking to translate the notion of a generalized intelligent problem processor into implementations available to DSS developers. Yet, great strides have been made in this direction. Not only is a very substantial GPPS implementation available today [52], a GPPS implementation embodying extensive artificial intelligence is also being used by some professional developers. The theoretical developments that led to this progress are quite relevant to model management.

In abstract terms, it was shown that data, procedures, and rules (in the form of Horn clauses) could beneficently coexist in a KS [15]. A PPS with data retrieval, procedure execution, and deductive capabilities could successfully use such a KS in responding to problem statements asking for either new or existing data. Through its deductive capability the PPS used rules to ultimately produce a proper response. The rules, in turn, referred to KS data and procedures. Thus, in the midst of deduction, the PPS would exercise its data retrieval and procedure execution capabilities as required by the rules being processed. The net effect was that the PPS could use the KS's rules to reason about solving a posed problem, where that reasoning was intertwined with appropriate sequencing of data retrievals and multiple procedure executions.

A key recognition of this work was that several distinct types of knowledge are candidates for inclusion in a KS and are subject to involvement in a particular decision support episode. Efforts at identifying and delineating knowledge types relevant to decision support resulted in a taxonomy differentiating among descriptive knowledge (i.e., data), procedural knowledge, reasoning knowledge, linguistic knowledge, presentation knowledge, and assimilative knowledge [40,52]. All of these are related to the varying views of model management and collectively they are the subject matter of what is more broadly called knowledge management. But understanding basic knowledge types is not enough. What are the alternatives for managing (i.e., representing and processing) each type of knowledge?

Empirically, it is obvious that there are a number of highly practical computer-based techniques for managing knowledge: programming, spreadsheet methods, file management, data base management, text management, rule management, and so forth. Each is exemplified by a class of knowledge management tools. These techniques are not the same as knowledge types. Rather, each technique can be studied with respect to its value in handling each of the knowledge types. That is, a technique may be applicable to multiple types and a knowledge type may be subject to management via multiple techniques. In general, it cannot be assumed that one technique is 'best' for all pieces of a given type of knowledge [47]. Furthermore, in the interest of generality, it becomes imperative that a GPPS not only address every major type of knowledge, but also embrace multiple knowledge management techniques [45]. Failure to do so impairs its generality. Clearly, an inference engine, the 1-2-3 software, or a data base manager falls far short of the GPPS ideal.

What was needed to make meaningful progress in the direction of a general tool for development? The specialized knowledge management capabilities conventionally packaged into separate tools needed to be integrated into a single tool. A resultant GPPS could then do data base management, support programming and execute program library contents, make rule-based inferences, carry out spreadsheet analyses, produce graphical and form-oriented presentations, comprehend customized problem statements, and so forth. With such a GPPS the developer could populate a DSS's knowledge system with data bases, programs, rule sets, spreadsheets, graphs, forms, vocabularies, menus, and so on, depending on DSS user needs.

Although it is often overlooked, there are very distinct strategies for accomplishing the integration of traditionally separate capabilities $[46]$ . With respect to GPPS design, the synergistic strategy dominates the others $[52,76]$ . In breaking down the traditional and arbitrary barriers between knowledge management techniques, it gives us a tool in which no technique dominates the other, any technique can be ignored, several techniques can be exercised in a single operation, and the cumbersome 'cut and paste' mentality is absent. For instance, with a modern GPPS implementation, the developer can let a KS procedure directly reference cells in a KS spreadsheet or consult a KS rule set. Any cell in a KS spreadsheet can be defined to be the execution of a program held in the KS or the consultation of a KS rule set. The premise of any rule in a KS rule set can be conditioned on KS spreadsheet cell values or KS program variable values. The rule's conclusion could involve such actions as spreadsheet analysis, execution of KS programs, retrieval from a KS data base, and consultation of another rule set.

The foregoing trends toward tools that address more types of knowledge and more knowledge management techniques can also be seen in recent writings that take the SC framework as their starting point. Fedorowicz and Williams [31] stress that knowledge representation is an important DSS issue and “no single representation scheme can hope to be universally most powerful across all applications.” While preserving the notion of a model base consisting of canned and custom-built procedures, they replace the SC framework’s data base with a ‘knowledge base.’ Their knowledge base includes non-procedural knowledge represented with conventional data base techniques, plus nonprocedural knowledge represented with artificial intelligence techniques such as formal logic clauses, production rules, semantic nets, and frames. To permit this implies that the DSS’s software system (i.e., PPS) must have the wherewithal to process such added representations. They point out that such a tool allows the concentration of intelligent DSSs, capable of using the added knowledge for determining appropriate model selection strategies.

Konsynski and Sprague [58] also suggest extending the SC framework by giving it a fourth component, which they call a 'knowledge base,' and enlarging the software system component to include a 'knowledge base management system.' Beyond a hint that artificial intelligence would be involved, no details are given about the nature of the proposed knowledge base. But presumably it has knowledge that somehow augments the descriptive knowledge held in a data base and the procedural knowledge held in a model base. Tools to build DSSs based on this extension would need to be equipped in a corresponding manner. Like a GPPS, such tools might be capable of developing DSSs that employ reasoning knowledge to govern the sequencing and interfacing of procedures and data (e.g., [15]).

Some researchers have focussed on the idea of a model management system (MMS). Dolk [27] characterizes a MMS as “an operating system for models” whose purpose it is to “support the general description, manipulation (analysis, solution and presentation) and control (access authorization, integrity, security, and privacy) of models.” At a more specific level, Konsynski [57] has posed a set of objectives that a generalized MMS should aim to satisfy. Applegate, Konsynski, and Nunamaker [1] suggest a MMS design that would give DSS developers semantic network and frame techniques for representing “decision and modeling knowledge.” A different MMS view has been offered by Ghiaseddin [34], who shows how data base management techniques can be used to implement a module directory holding extensive descriptive knowledge about procedural modules that is important for their administration.

To summarize, tools are necessary for the development of computer-based decision support entities that can execute analytic procedures with particular data sets in reaction to problem statements. Conventional tools are typically designed to furnish one knowledge management technique. Decision support systems involve multiple knowledge types and no one knowledge management technique is ideal (or even feasible) for handling all types of knowledge. Conventional tools are, therefore, individually insufficient or unwieldy for general-purpose DSS construction. From both the BHW and SC vantage points, as well as in the MMS area, the need for tools that provide more and new knowledge management techniques is recognized and being addressed to varying degrees.

## 3.2. Analysis dynamics

A large part of DSS research has been concerned with what can or should happen when a user wants to make a request that may involve analysis. This work might be broken down into the issues of what happens when:

(1) a problem is being stated;

(b) data need to be selected or produced;

(c) procedural modules need to be selected, sequenced, or interfaced;

(d) an executing module needs some data input;

(e) problem solution results are to be presented as a response to the user.

Although there are other dynamics that can be involved in a DSS, these are the ones that seem to have the most direct bearing on the various conceptions of model management. In considering tools, our focus was on knowledge representation possibilities, since they define the boundaries of what a DSS can do. Here, we focus more on knowledge processing possibilities which determine what a DSS does with the knowledge available to it.

(a) What happens as a problem is being stated? The answer depends on the nature of the language being used (i.e., LS) and on whether any linguistic knowledge is held in the KS, as opposed to being hardwired into the PPS (e.g., as required by the SC framework). The DSS language taxonomy mentioned earlier identifies languages that range from those with explicit or procedural statements of what is desired to those where the user simply characterizes desired results $[13]$ . Although all of today's DSS's have their own language system traits within this taxonomy, no universal or standard DSS LS has emerged. That is, the DSS field has no counterpart to SQL in the relational data management field. The structured modeling conventions $[32]$ might be regarded as an attempt toward a standard language for DSSs that are devoted to executing math programming procedures.

It may be that no broad standard will emerge. The approach of customizing DSS languages to reflect different user needs, tastes, and stages has considerable merit. How to accomplish this customization is an important issue. There seem to be two extremes with many variations between them. One is to program or otherwise instill the dynamics of a DSS's language-handling behavior into a DGMS. Different DGMSs would be constructed for different customized languages. At the other end of the spectrum is a GPPS, which is invariant software that can handle a wide range of customized languages. Linguistic differences among DSSs are reflected in different linguistic knowledge stored in their respective KSs $[47]$ . As a result, the dynamics of understanding a user's request can involve considerable use of the KS. Because a DSS's KS contents can change over time, there is the opportunity for its customized problem statement language to evolve in accordance with user desires $[28]$ . Interestingly, this extreme suggests the possibility of standardized dynamics for dealing with customized problem statement languages.

Another issue in the dynamics of processing a request is the extent to which a user can be actively aided in the act of problem specification. Artificial intelligence techniques that bring reasoning knowledge (e.g., held in the KS) to bear on the formulation of a problem would seem to have considerable potential. Trail-blazing investigations in this direction have focused on the domain of math programming problems $[3,4,60]$ . They have proposed problem formulation dynamics at quite detailed levels and allude to implementations of those dynamics. A module directory data base (e.g., $[34]$ ) would also seem very pertinent to a PPS that aims to actively aid a user's problem formulation efforts.

(b) What happens when data need to be selected during the course of processing a problem that has been stated? The answer depends on the knowledge management technique used to represent the data in a KS. If the technique is some variant of data base management, the dynamics are well understood and considerable flexibility exists. If the data are represented in a spreadsheet, selection possibilities are typically less flexible, but do exist. When data are represented in a text file, the facilities of ordinary text processing allow selection, but it may be cumbersome. Hypertext techniques promise to offer more flexible means for accomplishing data selection.

The dynamics of data selection are not so ordinary when the needed data do not explicitly exist in a KS. For instance, it has been pointed out that conventional means (e.g., data base management) for representing descriptive knowledge are very inefficient and open to integrity problems for certain data collections $[10]$ . It was shown how a large group of records could be replaced by a single logic clause, which could be used to infer the data in those records. Because a piece of reasoning knowledge is substituted for chunks of descriptive knowledge, the dynamics of data selection become very different, involving a mix of inference and traditional retrieval mechanisms. In this way, a KS can hold virtual data in addition to actual data. Subsequent analysis or presentation of the data is unaffected by whether it is virtual or actual.

Not only can the storage of reasoning knowledge be a means for effecting virtual data, storage of procedural knowledge can have a comparable effect. Blanning $[5,6]$ has shown this very clearly in his series of papers on relational model management. A model relation is virtual and the selection of data from it entails the execution of a corresponding model (i.e., procedure). An excellent summary of this work appears in $[7]$ . Other work that involves procedure execution as the dynamic for selecting virtual data includes [15,17].

(c) What happens when procedural modules need to be selected and combined in the course of processing a stated problem? As with data, the technique used to represent the procedural knowledge in the KS influences the processing dynamics. It makes a difference to the PPS whether a procedure is represented in the KS as a FORTRAN program, a C program, a spreadsheet, a piece of text, or in some other way. A procedure may be virtual, in the sense of not existing as an identifiable entity in the KS. It may need to be formulated from component modules. This has been recognized from the early days of the DSS field [72]. In the SC framework, the MBMS, in and of itself, is responsible for procedure formulation. In the BHW framework, the KS can contain reasoning knowledge about procedure formulation. The PPS is responsible for procedure formulation and can draw on KS contents (e.g., a set of rules) in dispensing with this duty.

The formulation of a procedure from procedural modules (sometimes called model formulation) has drawn the attention of many DSS researchers. Bonczek, Holsapple, and Whinston [11] suggested a general scheme for procedure formulation involving the modification and combination of known program modules. Based on KS rules for permissible modifications and combinations, problem reduction was adapted to derive an AND/OR graph of modules for a stated problem. Formal logic resolution has been applied to the issue of determining the selection and proper sequencing of module execution [15,29,30]. Sivasankaran and Jarke [68] impose a hierarchical control structure on logic resolution to manage the sequencing and combination of formulas. The use of expert system technology as a means for governing procedure formulation suggests yet another mechanism [49,65]. Blanning [6,7] has shown how the activity of procedure formulation can be characterized in terms of relational operators on model relations.

The mechanics of interfacing modules in a planned sequence is an important practical issue. Module compatibility of some nature is mandatory. That is, in the absence of procedure synthesis yielding a single executable entity, the outputs of one module execution must be viable as inputs to one or more subsequent modules in the formulated procedure. In general, this has been characterized as an information mapping activity in which data organized according to an output schema of one module needs to be mapped into the input schema of another module [42]. Such a transferral may be accomplished with a single command specified in a generalized mapping language such as the one described in [18]. This is unnecessary if modules can be designed to employ a common intermediate file format or a common data based schema for storage of and access to intermediate execution results.

(d) What happens when an executing module needs some data input? This is related to the two prior questions. It can be answered in much the same way as the one about data selection. But there are a couple of added issues here. They involve the timing of a module's need for data and the delivery of that data in a form suitable for the module's use. Before considering them, we should point out that an appreciation of the distinct styles of software integration may also be helpful in researching data-model interface possibilities [76].

One strategy proposes that a module's data requirements be determined, those data be selected, and they be reorganized as required by the module prior to the module's execution [38]. An alternative proposes that the module be devised to contain requests for data selection that the PPS acts on during the module's execution [44]. It was explained that these requests might be in the guise of DML commands either embedded in the module by its creator or automatically edited into the module. In contrast, they might be in the guise of invocations of extraction routines that map selected data into formats that the module can use.

(e) What happens when a response is to be presented? It has long been well known that the manner in which a response is presented to a user is very significant. In many respects, this is a mirror image of the first question. Presentation dynamics may be hardwired into a PPS (e.g., as in the DGMS of the SC framework) or they may feed off of KS contents. The latter, of course, gives greater flexibility for allowing a DSS to adapt to changing user needs or tastes. All that is needed is to add to or modify presentation knowledge in its KS. The PPS itself does not need to be reprogrammed.

Just as some researchers have been interested in how to assist in problem formulation, others have been concerned with providing assistance for solution presentation. This goes beyond generic ergonomic considerations, to actively assist the user in interpreting results. Greenberg's tableau solution analyzer [36] and natural language discourse approach [37] are good representatives of steps in this direction. Brennan and Elam [21] discuss limitations of current decision support systems, particularly with respect to the user-model interface. They identify capabilities that a 'smart' modeling system should possess for helping users understand and validate results of procedure execution.

The assistance in interpreting results can be turned in a very different direction. By providing feedback on the system's performance, a user can give assistance to the DSS in interpreting how well it has done. Such an interpretation can allow the DSS to learn from experience [66]. A PPS can change KS contents in the interest of better performance in the future.

## 3.3. Settings for analysis

In what setting do analysis dynamics implemented with some tool or tools occur? In much of the DSS literature, the setting is that of an individual person who needs to solve various knowledge management problems in the course of reaching a decision. It is a person who instigates the execution of a procedure to analyze data. But there are other interesting possibilities. The instigator could be a person's work station [50]. That is, the work station would formulate problem statements to decision support entities of computer-based or human varieties. The instigator could be an event (other than a user request) that triggers some analysis [31,62]. This suggests that demon management could be a worthwhile technique for inclusion in a GPPS [42].

Sometimes a group is the decision maker. Instead of each group member having a personal DSS, the members might share a common DSS [22,54]. Event-triggered procedural analysis may be particularly relevant to such a setting. Jarke [55] points out that a multiperson DSS is not necessarily a group DSS. That is, the latter is a special case of the former. Others have also looked at possible connections between distributed (non-group) decision making and decision support systems $[23,25]$ . Multiperson or distributed DSS research not only raises interesting questions about cooperative or coordinated formulation of problems, it may also shed light on the coordination of modules.

## 4. Hyperknowledge environment

This section summarizes some of the main features of an emerging theory of decision support systems which regards a DSS as a hyper-knowledge environment [48]. Based on a cognitive metaphor, the theory may stimulate new ways of thinking about decision support in general and model management in particular. As a starting point, we assert that a decision maker cognitively possesses many diverse and interrelated pieces of knowledge (i.e., concepts). Some are descriptive, others are procedural in nature, yet others are concerned with reasoning, and so forth. The mind is able to deal with these in a fluid and inclusive manner via controlled focusing of attention. In effect, the decision maker actively acquires (i.e., recalls, focuses on) desired pieces of knowledge by cognitively navigating among the universe of available concepts. To the extent that a DSS can be conceived and devised as a natural extension of such activity, interacting with it should be relatively ‘easy,’ natural, or comfortable for the user. That is, the DSS can be regarded as an extension of the decision maker’s innate knowledge management capabilities.

Treating the foregoing cognitive basics as a guiding metaphor, we might conceive of an ideal DSS as a knowledge-rich environment in which a decision maker is immersed. In this environment, the decision maker is allowed to contact and manipulate knowledge embodied in any of a wide range of interrelated concepts. The decision maker is able to navigate spontaneously through the DSS's concepts in either a direct or associative fashion, pausing at a concept currently in focus to interact with it or an image of it. The type of interaction that is possible depends on the nature of the concept or its image. A decision support environment ideally is an extension of the user's private cognitive world, pushing back cognitive limits on knowledge representation. Its knowledge processing capabilities augment the user's mental skills, overcoming cognitive limits on the speed and capacity of strictly human knowledge processing. Because of this extensive nature, we refer to the consequent decision support system ideal as a hyperknowledge environment.

Current decision support systems are pragmatic, varied responses to needs sensed by diverse decision makers. For the most part they can be viewed as narrow, very specialized, inflexible, and partial renderings of the environment idea. Typically, they manage only one or two types of knowledge (e.g., descriptive and procedural), offer noncustomizable interfaces, and do little to facilitate navigation through concepts. Yet if we were to imagine the domain independent functionalities of all current decision support systems accessible via the metaphorical interface of a single DSS, then the environment ideal begins to be approached. Problem processor generality and intelligence are essential for faithfully adhering to the cognitive metaphor in devising hyperknowledge environments.

In a hyperknowledge environment, a user freely navigates through and works with diverse concepts. Moreover, the concepts can work with and play upon each other. The conventional view of narrowly specialized software tools (e.g., data base managers, spreadsheet systems, expert system shells) vanishes, although each can be regarded as a very constrained rendition of the environment view. Just as the human navigates via a cognitive map of the mental landscape and visits various concepts to bring them into the focal point of attention, so too should a user be able to navigate through a DSS's KS via a concept map that shows the environment's content. Having brought some KS concept into focus, the user should be able to direct the environment's PPS to manipulate that concept in desired ways. For each kind of concept allowed to exist in the KS, the PPS must possess relevant processing abilities.

The environment theory recognizes the possibility of a knowledge system that holds interrelated concepts of many epistemological shapes and sizes. It admits concept relationships that are structured, in the sense of associations and definitions [14,20,69] and relationships that are dynamic, in the sense of active interconcept communication [47]. Such a knowledge system might be regarded as a generalization of the notion of hypertext wherein multiple pieces of text are related by semantic associations rather than physical linearity [26]. Instead of being restricted to paths connecting textual nodes, a hyperknowledge user is able to navigate through a KS that can represent paths through arbitrary (i.e., textual or non-textual) concepts and allows concepts to actively interact with other concepts.

The theory identifies interface possibilities which may or may not be exploited in this or that DSS. What happens when a hyperknowledge problem processor receives a request for the recall or manufacture of knowledge? The PPS must recognize exactly what problem it is that the user wants to have solved. This is accomplished by exercising its innate linguistic processing knowledge and drawing on domain-specific or user-specific linguistic knowledge held in the KS. In this way, the PPS translates the request into a series of one or more elements on which it can directly act for the purpose of satisfying the request. Conversely, what happens when the PPS has completed its recall or manufacture for a recognized problem? It may simply retain the knowledge in the KS for later use. Alternatively or in addition, the solution may be presented to the user by exercising innate presentation processing knowledge and drawing on domain-specific or user-specific presentation knowledge existing in the KS. Thus, the theory distinguishes between surface requests/responses understood by users and deep requests/responses that a PPS understands quite apart from user interface considerations.

Having briefly introduced the theory's central idea of a hyperknowledge environment, we now turn to an overview of its features, undertaken from two essential and complementary angles. The first angle involves an examination of the interface and functionality duality. The second involves formulation of traits and behaviors that need to be considered in devising a hyperknowledge environment [24].

## 4.1. Interface versus functionality

Both requests to and responses from the environment can be regarded as messages. Both will be referred to as surface messages, indicating that they lie at the surface which joins a user to the environment. Let $M_{SI}$ denote the subset of LS, consisting of all surface input messages that a user knows how to send an environment. A particular $m_{SI}$ in $M_{SI}$ is physically realized as a series of keystrokes, a mouse movement, touching the screen, speaking, or via some other overt user action [2]. Let $M_{SO}$ denote the subset of PS, consisting of all surface output messages that an environment's PPS knows how to send to a user. A particular $m_{SO}$ in $M_{SO}$ is physically realized as an image on a console display screen, a printed pattern, an audio image, or some other overt computer action. The set $M_{SO}$ will be regarded as a subset of the user's language system. It is thereby symmetric with $M_{SI}$ , which is a subset of the environment's language system.

Each $m_{SI}$ maps into exactly one deep input message $m_{DI}$ , which specifies what the PPS is to do in order to satisfy the request expressed in $m_{SI}$ . Taken together, the set of all deep input messages ( $M_{DI}$ ) and the KS contents (e.g., data, rules, procedures) define what decision support functionality a user can cause a PPS to perform. The surface to deep mapping of input messages can be represented as

$$
t \left(m _ {\mathrm{SI}}, K _ {\text {ling}}\right) = m _ {\mathrm{DI}},
$$

where t denotes the translation part of the PPS's user interface capability and $K_{ling}$ refers to the KS's linguistic knowledge available to the PPS.

It may happen that $t(m, K_{\mathrm{ling}})$ is null, meaning that m is not in the LS. In such a case, the PPS's functional processing capabilities cannot be exercised to provide decision support. Instead, another part of its user interface capability is employed to assist the user. This assistance manifests as a message $m_{SO}$ to the user, reflecting the degree of success achieved in interpreting m. Results of applying this assistance function to m, together with presentation knowledge ( $K_{pres}$ ), are arguments for a presentation function that yields some $m_{SO}$ . This is expressed as

$$
p \big (a (m, K _ {\mathrm{ling}}), K _ {\mathrm{pres}} \big) = m _ {\mathrm{SO}},
$$

where p is the presentation function and a is the assistance function. It should be clear that several iterations may be followed before the user succeeds in completely and correctly stating some $m_{SI}$ . Even when or as a particular $m_{SI}$ is specified, this mechanism may be used to provide the user with a record of that $m_{SI}$ .

Once the PPS has identified an element of $M_{DI}$ , the instructions embodied in that $m_{DI}$ are carried out. In general, these instructions can activate any mix of the PPS's knowledge processing capabilities with respect to corresponding knowledge representations held in the KS. For instance, some $m_{DI}$ might cause the PPS to use its inference engine capability to formulate a procedural model and identify appropriate data for analysis, retrieve or derive the data, and then execute the procedure with that data to yield some derived data. The PPS's exercise of such functionalities can be expressed as

$$
f (m _ {\mathrm{DI}}, K S) = m _ {\mathrm{DO}},
$$

where $m_{DO}$ is the deep output (derived knowledge) produced by the PPS. Knowledge derived by f from $m_{DI}$ and KS forms a message that can be used in either or both of two ways, depending on the user's intent specified in $m_{DI}$ . The PPS can store $m_{DO}$ in the KS or present it in a manner conforming to the user's request. This is accomplished by the p function portion of the PPS's user interface.

$$
p \left(m _ {\mathrm{DO}}, K _ {\text {pres}}\right) = m _ {\mathrm{SO}},
$$

possibly drawing on presentation knowledge held in the Ks.

Effectively tapping an environment's knowledge resources depends on the phenomena of contact and impact [24]. In a cognitive environment, the decision maker must contact a concept of interest before impact can occur. Impact refers to situations wherein the decision maker is affected by the concept or affects the concept. Similarly, in a hyperknowledge environment, a concept must be contacted before it can be impacted by or have an impact on the user. It follows that $M_{\mathrm{SI}}$ includes both contact and impact messages. Similarly, some elements of $M_{\mathrm{SO}}$ are concerned with presenting the results of contact activities, while others involve presentation of impact results.

Either implicitly or explicitly, the user must be provided with a concept map as the basis for establishing contacts. This implies the existence of a concept map, indicating what concepts are in the environment and what their interrelationships are. An implicit map is one that is viewed external to the DSS. For instance, it may reside in the user's cognitive environment, akin to Bennett's notion of a 'knowledge base' [2]. However, due to cognitive limits, maintaining and using such an implicit map becomes burdensome or even infeasible for ambitious environments whose KSs are large, varied, and frequently changing. Alternatively, we propose that an explicit map be provided by the DSS itself. A significant portion of $M_{\mathrm{SO}}$ would be concerned with portraying available concepts and relationships. In addition, corresponding elements of $M_{\mathrm{SI}}$ should be devoted to manipulating the map. Possible notational conventions for concept maps are introduced in [24].

When a user has established contact with some concept (e.g., a procedure) pertinent to a decision process, the DSS must facilitate interaction with that concept. The nature of the desired interaction is indicated with some $m_{SI}$ submitted by the user. Via $M_{SI}$ elements, the user is able to impact the concept's state and behavior. Conversely, via $M_{SO}$ elements, the concept is able to impact the user's consciousness by conveying some recalled or manufactured knowledge. It may also impact (i.e., interact with) other concepts as a byproduct or chain reaction. General terms of impact are discussed in [24].

## 4.2. The fabric of hyperknowledge

The foregoing characterization of dynamics fits the BHW framework. These dynamics involve transformations of messages from the environment's LS to the user's LS (i.e., the environment's PS). The transformations are carried out by the PPS (subject to KS contents) which embodies $t$ , $a$ , $f$ , and $p$ functions. From a user's perspective, the DSS augments personal cognitive concepts with an environment of diverse and interrelated concepts that can be contacted for impacts. An explicit concept map is available to assist the user in navigating through this hyperknowledge space. But, what is the nature of this space? What laws govern its constitutions? What primitives must exist as a basis for devising a PPS to handle such a KS?

Various propositions have been advanced to begin to formally answer such questions [24]. Some central ones are briefly reprised here. Such formalisms can be valuable in several respects. To the extent they are general and reasonably comprehensive, they give DSS researchers a common ground for detailed study, discourse, and evaluation. They can also offer a stimulative language for uncovering new DSS possibilities (e.g., in the area of model management).

Proposition 1. There exists a function $\chi$ such that $\chi(\mathrm{KS}) = \{c_1, c_2, \ldots, c_n\}$ ,

where $c_{i}$ is a concept tag and $c_{i} \neq c_{j}$ $\forall i, j \in \{1, \ldots, n\}$ . A KS is composed of concepts, each of which can be referenced by a unique tag or identifier. As part of its functionality f, a PPS is able to apply $\chi$ .

Proposition 2. There exists a function $\delta$ such that $\delta(c_{i}) = \mathrm{DC}_{i} \subset \xi(\mathrm{KS})$

where $DC_{i}$ is the set of all defining concepts for $c_{i}$ . They are the concepts that can serve as definitions (i.e., instantiations) of $c_{i}$ . A concept map of KS must be able to portray the definitional relationship existing between the $C_{i}$ node and the node for each element of $\delta(c_{i})$ .

Proposition 3. There exists a function $\tau$ such that $\tau(S_i) = S_j$ ,

where $S_{i}$ and $S_{j}$ are sets of concepts and $\forall c_{j} \in S_{j}$ , $S_{i} \subset \delta(c_{j})$ . Together, $\delta$ and $\tau$ allow the PPS (and therefore a user) to recognize and navigate through an arbitrary KS's definitional relationships.

Proposition 4. There exists a function $\alpha$ such that $\alpha(c_i) = AC_i \subset \chi(KS)$ ,

where $AC_{i}$ is the set of all associated concepts of $c_{i}$ . To be faithful to the cognitive metaphor, a DSS should have an ability to identify every concept associated with a given concept. The concept map must make such associations clear. The $AC_{i}$ elements can be viewed as qualifying $c_{i}$ . Conversely, $c_{i}$ can be viewed as qualifying $AC_{i}$ elements. Considering an association of two concepts conveys more about each than considering the same two concepts in isolation from each other. In any associative relationships there is at least one concept that participates as the agent and at least one concept that participates as the object.

Proposition 5. Each associative relationship has a tag, differentiating it from other associations in KS. There exists a function $\alpha_{A}$ such that

$$
\alpha_ {A} (c _ {i}) = \mathrm{AT} _ {i},
$$

where $AT_{i}$ is the set $\{A_{1},\ldots,A_{k}\}$ of tags for all associations in which $c_{i}$ participates. In a concept map, these association tags connect nodes formed by concept tags.

Proposition 6. In allowing associative relationships in its KS, an environment possesses functions $\alpha_{a}$ and $\alpha_{o}$ such that

$$
\alpha_ {a} (c _ {i}) \cup \alpha_ {o} (c _ {i}) = \mathrm{AT} _ {i}
$$

where $\alpha_{a}(c_{i})$ is that subset of $AT_{i}$ for which $c_{i}$ is an agent of each of its elements and $\alpha_{o}(c_{i})\subset AT_{i}$ for which $c_{i}$ is an object of each of its elements.

Proposition 7. If $A_{l} \in \alpha_{a}(c_{i})$ and $c_{j} \in (c_{i})$ , then $A_{l} \in \alpha_{a}(c_{j})$ . Similarly, if $A_{l} \in \alpha_{0}(c_{i})$ and $c_{j} \in \delta(c_{i})$ , then $A_{l} \in \alpha_{o}(c_{j})$ . This proposition maintains that associations are inherited.

Proposition 8. Each association belongs to a specific cardinality class. Such a partitioning of associations is useful for purposes of referential integrity and semantic clarity in a concept map.

Definitions. A selection set S is the result of applying a function (e.g., $\chi$ , $\delta$ , $\tau$ , $\alpha$ , $A_{1}$ ) that yields a collection of concepts. Very often there is a need to select a particular concept from S. A selection criterion C is a specification that differentiates all elements of S.

Proposition 9. There is a function $\sigma$ such that $\sigma(S, C) = c_i$ ,

where $c_{i} \in S$ and $c_{i}$ satisfies C. Such a function is the mechanism for focusing on a particular concept from a set of concepts to satisfy a user's contact needs. Variants of the primitive $\sigma$ , which produce sets of concepts, are of course possible.

The set $\chi(\mathrm{KS})$ is sufficient to characterize what concepts exist in a concept map. The functions $\delta$ , $\tau$ , $\alpha_{a}$ , and $\alpha_{o}$ are sufficient to characterize structural relationships existing among concepts in the map. These same functions, together with $\sigma$ and the elements of $\alpha_{A}(c_{i})$ $\forall i \in \{1, \ldots, n\}$ , are suffi-

To navigate through the concept map for the use of contacting any concept in KS. They use to reach any or all concepts related directly or indirectly, either definitionally inciatively, to an arbitrarily chosen concept.

dition 10. There must be a function $\mu$ such

$$
= \mathbf {M I} _ {i} \subset M _ {\mathrm{DI}},
$$

$\mathbf{MI}_{i}=\{M_{1},\ldots,M_{p}\}$ consists of all messages in be sent to a contacted concept $c_{i}$ . Each message designates a valid kind of impact. Innt concepts can be subject to different im-

ition 11. If $M_l \in \mu(c_i)$ , then $M_l(c_i) \in M_{\text{DO}}$ uivalent to an element of $M_{\text{DO}}$ . The result of 'ing a concept is ultimately a deep output e. It can happen that $M_l(c_i)$ causes contact compact with other concepts as intermediate stations of its behavior.

ition 12. For a full-fledged decision support element, the function $f$ must minimally have blem processing capabilities inherent in $\chi$ , $\delta$ , $_A$ , $\alpha_a$ , $\alpha_o$ , $A_l \in \alpha_A(c_i) \forall i \in \{1, \ldots, n\}$ , $\sigma$ , $\mu$ , $_l \in \mu(c_i) \forall i \in \{1, \ldots, n\}$ . In principle, each some composite of these function invoca-

ition 13. In the interest of PPS invariance, ions taken to realize dynamic relationships corresponding to elements of $\mathrm{MI}_i$ ) may not exist within the PPS $f$ function. Instead they possible to it. This is made possible by allow-se prescribed actions to exist as concepts in . They may or may not appear in the surface t map presented to the user, but do exist in p concept map available to the PPS.

foregoing propositions deal with the repetition of knowledge in an environment for an support. Regardless of whether a model used as a procedure, data, or a problem, these representation protocols are rel. The propositions also deal with the basics cessing hyperknowledge, identifying funda-

functionality that must exist in a full-l environment. As such, they offer a set of ves for devising alternative model management dynamics and establishing an interplay with non-model concepts.

## 5. Research directions

Scott Morton [63] has argued that the DSS field can benefit from each of nine types of research: Prototype construction, methodology construction, theory development, concept development, laboratory experimentation, field testing, survey work, case study, and assertion. We believe this typology works as a useful classification of approaches for future investigations of model management topics. Some may be of more immediate value for one topic than for others. But what are those topics? Konsynski and Sprague [58] organize research topics into six categories: Model elicitation, model specification, operations on models, administration of models, model manipulation, and policies on model use. Although they view model management from within the confines of the SC framework, they do suggest that extensions to permit the use of artificial intelligence techniques would be a worthy research direction.

In his discussion of research directions, Blanning [7] stresses the need to go beyond the dualism of model base and data base. He suggests a more pluralistic KS, capable of holding images, text, and a ‘knowledge base’ (i.e., rule sets). He emphasizes the need for more research in the direction of intelligent DSSs and speculates that progress along this track may lead to new ways of viewing organizations (beyond those drawn from economics and behavioral science). Blanning concludes by posing a number of interesting discussion questions which are suggestive of various research topics.

To the views of others, we offer some additional observations about model management research directions. These are framed along the lines of issues examined in Sections 2–4. We begin by recognizing that an investigator's conception of model management research is strongly colored by the conception of 'model' that is adopted and by the conception of a context in which models exist. For clarity, it is advisable to be precise and explicit about the meaning of 'model' and the nature of the chosen contextual framework. As to the former point, it might be best to refer to a problem statement as a problem statement (i.e., an element of LS), data as data (i.e., descriptive knowledge in a KS), and a procedure as a procedure (i.e., procedural knowledge in a KS). All three could be regarded as facets of modeling. As to the latter point, limitations (if any) imposed by a framework should be carefully scrutinized as potential causes of research blind spots. One research direction of relevance to model management is the investigations or invention of DSS frameworks in the interest of understanding or overcoming limitations.

Some research directions are a continuation of past research. Thus, the review in Section 3 suggests three lines of investigation. First, there will be endeavors to invent new tools that are more powerful, flexible, efficient, or accessible than today's tools. In a related vein, research is needed into the activity of DSS development. This is concerned with strategies for tool usage in the design, implementation, and evolution of DSSs. Second, there will be research aimed at uncovering new possibilities for analysis dynamics in terms of each of the five activities identified in Section 3.2. Progress in this direction will open the way for tool improvements. Third, there is a need to better understand the settings in which analysis is relevant. This includes an appreciation of the implications that different multiperson structures of decision making have for support systems (e.g., [77]). It also includes the topics of DSS valuation [59].

An alternative way of looking for model management research opportunities can occur from the platform of a DSS theory. For instance, consider the emerging hyperknowledge theory of decision support described in Section 4. The constructs and principles that it embodies flow from the strong knowledge-orientation of the BHW framework. It shifts the focus away from isolated consideration of model management to the more all encompassing realm of knowledge management. It asks a host of descriptive, normative, and speculative questions that slice across model management boundaries.

What distinct types of knowledge are germane to a decision-making process? Which of these are amenable to computerized management (i.e., representation and processing)? What existing or new techniques for knowledge management are applicable to each type of knowledge? How should concepts of the same or diverse types be definitionally and associatively related to each other in a hyperknowledge KS? What is the mechanism whereby one concept (e.g., a rule set) contacts and impacts another concept (e.g., a procedural module), which in turn contacts and impacts yet another concept (e.g., a piece of data, another procedure, or another rule set)? Can standard $M_{SI}$ and $M_{SO}$ be devised? How can customized $M_{SI}$ and $M_{SO}$ be devised? How can customized $M_{SI}$ and $M_{SO}$ be rapidly developed? Can they evolve based on experiences with users? In what other ways can the environment be self-adapting to better conform to user traits? To what extent can an environment's interface be independent of its functionality? What roles can interactors, constraint maintainers, and event handlers [43] play in accomplishing such independence? How general can implementations of the t, a, f, and p functions be? Should the same f implementation be able to handle multiple $M_{DI}$ and $M_{DO}$ ?

The foregoing are representative of research issues raised by the hyperknowledge theory. They are by no means exhaustive. Such questions furnish an unconventional vantage point for model management researchers. As such, they may stimulate new insights or investigations that are beneficial to decision makers who state problems and expect to receive presentations based on the procedural analysis of data. The environment's ability to manufacture new knowledge from existing knowledge may be enhanced by imbuing it with its own intelligence.

Acknowledgement: Research support in part by the NSF, Grant IRI-8921603.

## References

[1] L.M. Applegate, B.R. Konsynski and J.R. Nunamaker, Model Management Systems: Design for Decision Support, Decision Support Systems 2, No. 1 (1986).

[2] J. Bennett, User-Oriented Graphics, Systems for Decision Support in Unstructured Tasks, in User-Oriented Design of Interactive Graphics Systems, ed., Treu (ACM, New York, 1977).

[3] M. Binbiasioglu and M. Jarke, Domain Specific DSS Tools for Knowledge-Based Model Building, Decision Support Systems 2, No. 3 (1986).

[4] M. Binbiasioglu and M. Jarke, Knowledge-Based Formulation of Linear Programming Models, in Expert Systems

and Artificial Intelligence in Decision Support Systems, eds. H. Sol, et al. (Reidel, Dordrecht, 1987).

[5] R.W. Blanning, Issues in the Design of Relational Model Management Systems, Proceedings of the National Computer Conference (June, 1983).

[6] R.W. Blanning, A Relational Theory of Model Management, in Decision Support Systems: Theory and Applications, eds. Holsapple and Whinston (Springer-Verlag, Berlin, 1987).

[7] R.W. Blanning, Model Management Systems: An Overview, Decision Support Systems, this issue, 1992.

[8] R.H. Bonczek, c.W. Holsapple and A.B. Whinston, Data Base Management Techniques for Mathematical Programming, Proceedings of the SIGMAP Bicentennial Conference on Mathematical Programming, Washington, DC (November, 1976).

[9] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Mathematical Programming Within the Context of a Generalized Data Base Planning System, Recherche Operationnelle (May, 1978).

[10] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, The Integration of Data Base Management and Problem Resolution, International Journal of Information Systems 4, No. 2 (1979a).

[11] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Model Management via Problem Reduction, Proceedings of Hawaiian International Conference on Systems Sciences, Honolulu (January 1979b).

[12] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Computer-Based Support of Organizational Decision Making, Decision Sciences (April, 1979c).

[13] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, The Evolving Roles of Models Within Decision Support Systems, Decision Sciences (April 1980a).

[14] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Future Directions for Developing Decision Support Systems, Decision Sciences October (1980b).

[15] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, A Generalized Decision Support System Using Predicate Calculus and Network Data Base Management, Operations Research 29, No. 2 (1981a).

[16] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Foundations of Decision Support Systems (Academic Press, New York, 1981b).

[17] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Specifications of Modeling Knowledge in Decision Support Systems, in Processes and Tools for Decision Support, ed. H.G. Sol (North-Holland, Amsterdam, 1983).

[18] R.H. Bonczek and A.B. Whinston, A Generalized Mapping Language for Network Data Structures, Information Systems 2, No. 2 (1977).

[19] J.B. Boulden and E.S. Buffa, Corporate Models: On-line, Realtime systems, Harvard Business Review (July–August, 1970).

[20] P.J. Brachman and J.G. Schmolze, An Overview of the KL-ONE Knowledge Representation System, Cognitive Science 9, No. 2 (1985).

[21] J.J. Brennan and J.J. Elam, Understanding and Validating Results in Model-Based Decision Support Systems, Decision Support Systems 2, No. 1 (1986).

[22] T.X. Bui and M. Jarke, Communications Design for CO-OP: A Group Decision Support System, ACM

Transactions on Office Information Systems 2, No. 4 (1986).

[23] A. Burns, M.A. Rathwell and R.C. Thomas, A Distributed System for Decision Making, Decision Support Systems 3, No. 2 (1987).

[24] A. Chang, C.W. Holsapple and A.B. Whinston, A Decision Support System Theory, Kentucky Institute for Knowledge Management, Paper No. 5 (1988).

[25] C. Ching, C.W. Holsapple and A.B. Whinston, Reputation, Learning, and Organizational Coordination, Kentucky Institute for Knowledge Management, Paper No. 6 (1988).

[26] J. Conklin, Hypertext: An Introduction and Survey, IEEE Computer (September, 1987).

[27] D.R. Dolk, Data as Models: An Approach to Implementing Model Management, Decision Support Systems 2, No. 1 (1986).

[28] B. Dos Santos and C.W. Holsapple, A Framework for Designing Adaptive DSS Interfaces, Decision Support Systems 5, No. 1 (1989).

[29] A. Dutta and A. Basu, An Artificial Intelligence Approach to Model Management in Decision Support Systems, IEEE Computer 17, No. 9 (1984).

[30] J.J. Elam, J.C. Henderson and L.W. Miller, Model Management Systems: An Approach to Decision Support in Complex Organizations, Proceedings of First Conference on Information Systems, Philadelphia (December, 1980).

[31] J. Fedorowicz and G.D. Williams, Representing Modeling Knowledge in an Intelligent Decision Support System, Decision Support Systems 2, No. 1 (1986).

[32] A.M. Geoffrion, An Introduction to Structured Modeling, Management Science 33, No. 5 (1987).

[33] G.W. Gershefski, Corporate Models—The State of the Art, Management Science 16, No. 6 (1970).

[34] N. Ghiaseddin, An Environment for Development of Decision Support Systems, Decision Support Systems 2, No. 3 (1986).

[35] G.M. Gorry and M.S. Scott Morton, A Framework for Management Information Systems, Sloan Management Review (Fall, 1971).

[36] H.J. Greenberg, A Functional Description of ANALYZE: A Computer-Assisted Analysis System for Linear Programming Models, ACM Transactions on Mathematical Software 9, No. 1 (1983).

[37] H.J. Greenberg, A Natural Language Discourse Model to Explain Linear Programming Models and Solutions, Decision Support Systems 3, No. 4 (1987).

[38] W.D. Haseman, C.W. Holsapple and A.B. Whinston, Implementation of a Large-Scale Water Quality Data Management System, Socio-Economic Planning Sciences 10, No. 1 (1976).

[39] C.W. Holsapple, Framework for a Generalized Intelligent Decision Support System, doctoral dissertation, Purdue University (1977).

[40] C.W. Holsapple, The Knowledge System for a Generalized Problem Processor, Krannert Institute Paper, No. 827, Purdue University (1983).

[41] C.W. Holsapple, A Perspective on Data Models, PC Tech Journal 2, No. 1 (1984).

[42] C.W. Holsapple, Adapting Demons to Knowledge Management Environments, Decision Support Systems 3, No. 4 (1987).

[43] C.W. Holsapple, S. Park and A.B. Whinston, Developing User Interfaces for Decision Support Systems, Proceedings of First Asian Federation of Operations Research Society Conference, Seoul (1988).

[44] C.W. Holsapple and A.B. Whinston, A Decision Support System for Area Wide Water Quality Planning, Socio-Economic Planning Sciences 10, No. 6 (1976).

[45] C.W. Holsapple and A.B. Whinston, Software Tools for Knowledge Fusion, Computerworld (In Depth) 17, No. 15 (1983).

[46] C.W. Holsapple and A.B. Whinston, Aspects of Integrated Software, Proceedings of the National Computer Conference, Las Vegas (July 1984).

[47] C.W. Holsapple and A.B. Whinston, Knowledge Representation and Processing in Economics and Management, Proceedings of Conference on Integrated Modeling Systems, Austin (October, 1986).

[48] C.W. Holsapple and A.B. Whinston, Toward an Environment Theory of Decision Support, Proceedings of Conference on Integrated Modeling Systems, Austin (October 1987a).

[49] C.W. Holsapple and A.B. Whinston, Business Expert Systems (Irwin, Homewood, IL, 1987b).

[50] C.W. Holsapple and A.B. Whinston, Knowledge-Based Organizations, Information Society 5, No. 2 (1987c).

[51] C.W. Holsapple and A.B. Whinston, Distributed Decision Making: A Research Agenda, ACM SIGOIS Bulletin 9, No. 1 (1988a).

[52] C.W. Holsapple and A.B. Whinston, The Information Jungle (Dow Jones-Irwin, Homewood, IL, 1988b).

[53] G.P. Huber, Organizational Science Contributions to the Design of Decision Support Systems, in Decision Support Systems: Issues and Challenges, eds. Fick and Sprague (Pergamon Press, London, 1980).

[54] G.P. Huber, Issues in the Design of Group Decision Support Systems, MIS Quarterly (September, 1984).

[55] M. Jarke, Knowledge Sharing and Negotiation Support in Multiperson Decision Support Systems, Decision Support Systems 2, No. 1 (1986).

[56] R.L. Klass, A DSS for Airline Management, Data Base (Winter, 1977).

[57] B.R. Konsynski, Model Management in Decision Support Systems, in Data Base Management Theory and Applications, eds., C.W. Holsapple and A.B. Whinston (Reidel, Boston, 1982).

[58] B.R. Konsynski and R.H. Sprague, Jr., Future Research Directions in Model Management, Decision Support Systems 2, No. 1 (1986).

[59] J. Marsden and D.E. Pingry, A Theory of Decision Support Systems Design Evaluation, working paper, University of Kentucky (1988).

[60] F.H. Murphy and E.A. Stohr, An Intelligent System for Formulating Linear Programs, Decision Support Systems 2, No. 1 (1986).

[61] N.H. Nie et al., Statistical Packages for the Social Sciences, 2nd ed. (McGraw Hill, New York, 1975).

[62] L. Orman, Flexible Management of Computational Models, Decision Support Systems 2, No. 3 (1986).

[63] M.S. Scott Morton, State of the Art of Research in Management Support Systems, Colloquium on Information Systems, Harvard (July, 1983).

[64] R.A. Seaberg and C. Seaberg, Computer Based Decision Systems in Xerox Corporate Planning, Management Science 20, No. 4 (1973).

[65] A. Sen and G. Biswas, Decision Support Systems: An Expert System Approach, Decision Support Systems 1, No. 3 (1985).

[66] M.J. Shaw, P. Tu, and P. De, Applying Machine Learning to Model Management in Decision Support Systems, Decision Support Systems 4, No. 3 (1988).

[67] H.A. Simon, The Heuristic Compiler, in Representation and Meaning, eds. Simon and Siklossy (Prentice-Hall, Englewood Cliffs, NJ, 1972).

[68] T. Sivasankaran and M. Jarke, Logic-Based Formula Management Strategies, Decision Support Systems 1, No. 3 (1985).

[69] J.F. Sowa, Conceptual Structures: Information Structures in Mind and Machine (Addison–Wesley, Reading, MA, 1984).

[70] R.H. Sprague, Jr., A Framework for the Development of Decision Support Systems, MIS Quarterly (December, 1980).

[71] R.H. Sprague, Jr. and E.D. Carlson, Building Effective Decision Support Systems (Prentice-Hall, Englewood Cliffs, N.J. 1982).

[72] R.H. Sprague, Jr. and H.J. Watson, MIS Concepts-Part II, Journal of Systems Management 26, No. 2 (1975).

[73] R.H. Sprague, Jr. and H.J. Watson, A Decision Support System for Banks, OMEGA 4, No. 6 (1976).

[74] E.A. Stohr and M.R. Tanniru, A Database for Operations Research Models, International Journal of Policy Analysis and Information Systems 4, No. 1 (1980).

[75] E. Turban, Decision Support and Expert Systems (Macmillian, New York, 1988).

[76] K. Watabe, C.W. Holsapple and A.B. Whinston, Solving Complex Problems Via Software Integration, Kentucky Institute for Knowledge Management, Paper No. 2 (1988a).

[77] K. Watabe, C.W. Holsapple and A.B. Whinston, Coordinator Support in a Newawashi Decision Process, Kentucky institute for Knowledge Management, Paper No. 4 (1988b).

[78] H.J. Will, Model Management Systems, in Information Systems and Organization Structure, eds., Grochla and Szyperski, (Gruyter, Berlin, 1975).
