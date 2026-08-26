---
otero_id: 23438
otero_key: "XETWVU9J"
title: "A survey of requirements verification techniques"
authors: "Sachidanandam Sakthivel"
year: "1991"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1991.12"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A survey of requirements verification techniques

SACHIDANANDAM SAKTHIVEL

College of Business Administration, Bowling Green State University, OH, USA

Abstract: Requirements verification is a set of procedures used to detect errors in requirement specifications. This paper discusses various types of requirement errors and illustrates each error with an example. It also examines several techniques used for requirements verification and the capability of each technique to identify various requirement errors. In addition, it reviews the use of each technique in various requirements analysis approaches and indicates the drawbacks of these techniques. This paper can help systems analysts to be aware of possible errors in requirement specifications and the limitations in requirements verification while using a requirements analysis approach.

## Introduction

The increasing size and complexity of organizations warrant large and complex information systems. As a result, the development of such information systems is also complex. Developing information systems in stages such as requirements analysis, design, and implementation helps to manage this complexity. The requirements analysis is the initial stage that should encompass everything necessary to lay the groundwork for later stages. The requirements analysis includes various tasks to analyse vague user needs and translate them into information system requirement specifications. These specifications include the functional requirements (content of the information system, i.e. inputs, outputs, processes, and the relationships among these) and performance requirements (response time, resources required, etc.).

Since the requirement specifications become inputs to the design stage, the successful design of an information system depends on the accuracy of its requirement specifications. The uncorrected requirement errors may propagate and magnify during the design stage. This eventually leads to an inappropriate design. Such a system may not meet user needs and face possible rejection by the users.

Though testing a system is useful to detect errors, it is performed after the design is completed. To detect errors successfully, the procedures and data used for testing should be comprehensive. Even a comprehensive testing may indicate the presence but not the absence of errors (Dijkstra, 1972). It is a costly mistake to defer the activity of detecting and correcting errors until late in the development process (Boehm, 1977). The cost of fixing errors at a later stage is high (Boehm, 1984; Martin, 1985) due to design revision, code revision, retesting, and maintenance (Alford, 1977). Identifying the requirement errors avoids reworking and improves the productivity of systems development (Boehm, 1987; Case, 1985). It also improves the quality of the developed systems (Buckley and Poston, 1984).

The process of identifying the errors in system specifications is defined as verification (Federal Information Processing Standard 101, 1983; IEEE Standard Glossary of Software Engineering Terminology, 1983). Verification should not be confined to a single stage of the life cycle but should be incorporated into every stage of systems development (Adrion et al., 1982; Howden, 1982; Wallace, 1985). A comprehensive discussion of verification during the later stages of systems development is available (Adrion et al., 1982; Miller and Howden, 1981). The objective of this paper is to provide a detailed discussion of verification during requirements analysis.

The following section identifies various errors that are commonplace in requirement specifications and illustrates each error with an example. A system analyst can use this list to look for possible errors in requirement specifications. The third section examines various techniques used for requirements verification and the capability of each technique to identify requirement errors. It also reviews the use of each technique in various requirements analysis approaches and discusses the inadequacy of these techniques in providing a comprehensive verification. This section can help a systems analyst to be aware of the limitations in requirements verification while using a requirements analysis approach. The last section concludes this paper and suggests future research directions.

## Requirement errors

Several studies have classified requirement errors as incomplete, inconsistent, infeasible, untestable, redundant, and incorrect requirements (Bell and Thayer, 1976; Boehm, 1984; Howden, 1982; Miyamoto and Yeh, 1981; Sakthivel and Tanniru, 1988–89). Using the same classification scheme, this section lists these errors. Two case studies showed that these are the commonly occurring requirement errors (Bell and Thayer, 1976; Scheffer et al., 1985). This section also illustrates each error with an example.

(1) Incomplete: the requirements are incomplete when all parts in the specifications are not present or each part is not fully developed. Various types of incomplete requirements are as follows:

(i) TBDs (To Be Determined) are incompletely specified requirements, e.g. the system should provide the output frequently, the frequency to be determined.

(ii) Nonexistent references are the references made to undefined processes, inputs, or outputs in the specifications, e.g. the process uses the credit file and the sale order to authorize credit to the customer, where the credit file is undefined.

(iii) Missing specifications refer to the undefined specifications such as boundary, interfaces, performance, resource constraints, and recovery.

(iv) No minimal completeness occurs when a process does not have at least one input and one output, e.g. the process uses the credit file and the sales order, where the process does not have an output.

(v) Process insufficiency is a process defined insufficiently such that its specified inputs cannot be translated into specified outputs, e.g. the process compares the credit available and the order value to authorize credit to the customer, where how they are compared is not specified.

(vi) Missing Relationships occur when a process relationship such as order dependency, order independency, mutually exclusiveness, or concurrency is not specified. In a data model, a relationship such as implication, equivalence, or precedence among information sets may be missing.

(vii) Data insufficiency refers to the nonavailability of all the data required for performing a process, e.g. the process calculates the order value by multiplying the order quantity and the item price, where the item price is not available.

(viii) Conceptual omissions pertain to omitted user requirements, e.g. a manager needs a sales analysis report which is not included in the requirements.

(2) Inconsistent: the requirements are inconsistent when the specifications are conflicting with each other or with the system goals and objectives. Various types of inconsistent requirements are as follows:

(i) Convention inconsistency refers to the specifications that are not consistent with the modelling conventions, e.g. the modelling formalism requires the specification of only the information flow but the material flow is also specified.

(ii) The names and terms in specifications may be homonyms or synonyms. These could lead to requirement errors when they are not identified, e.g. homonym — the data name 'date' where, it may refer to order receipt date, shipping date, or billing date. Synonym — the data names 'amount owed' and 'credit' that may refer to the balance due from a customer.

(iii) Internal inconsistency is the conflict of the specifications with each other, e.g. process 2.4 — outputs the customer name, item name, price, quantity, and order value. Process 2.5 — accepts the inputs, customer number, item number, price, quantity, and order value from process 2.4.

(iv) External inconsistency is the conflict of the specifications with the system goals and objectives, e.g. system goal — to provide a real-time soft copy output to managers for decision-making. Specification — the query will be processed and a report will be printed immediately.

(v) Untraceable specifications are the items in the specifications that do not have clear antecedents in earlier specifications or a statement of system objectives, e.g. system objective — the system interface should be user friendly. Specification — the data input interface will have a natural language processor and function as follows ...

(vi) Hierarchical inconsistency refers to the inconsistency between the main system and the subsystem specifications in hierarchically developed systems, e.g. in a system, a process is receiving two inputs and producing two outputs. The refinement of this process into a subsystem is inconsistent if the subsystem receives two inputs and produces three outputs.

(3) Infeasible: the requirements are infeasible when the system cannot meet those requirements. The process of checking the feasibility of requirements at the end of the systems development process is called validation (Federal Information Processing Standard 101, 1983; IEEE Standard Glossary of

Software Engineering Terminology, 1983). Since the feasibility may be checked at the requirements analysis stage, the term validation is not used here. Various types of infeasibility are as follows:

(i) Infeasible system objectives are those system objectives that may not be realizable, e.g. the objective to cut inventory holding by 10 % may not be realizable.

(ii) Infeasible user needs refer to the user needs such as response-time and ease of use that may not be satisfiable, e.g. a user requirement of 2 seconds response-time may not be satisfiable.

(iii) Infeasible functional needs are the system needs, such as maintainability that may not be achievable, e.g. a functional need to produce a maintainable system may not be achievable.

(iv) Infeasible resource usage occurs when the system cannot meet the system objectives, user needs, and functional needs at an acceptable resource cost, e.g. the estimated cost of developing the system under \$100 000 may not be feasible.

(4) Untestable: the requirements are untestable when the specifications lack clarity and precision.

(i) Unclear and ambiguous specifications refer to the specifications that lack clarity, e.g. the credit worthiness of a customer will be evaluated in accordance with the company procedures.

(ii) Imprecise specifications are the requirements that are not quantitative or measurable, e.g. the query system will produce a fast turn around. Instead, it should specify the turn around time (say, $4 \pm 2$ seconds).

(5) Redundant: the requirements are redundant when the specifications show the following traits:

(i) Redundant requirements are unnecessary requirements, e.g. the system will produce a list of customers whose credit requests were not approved, where such a report is not required by the users.

(ii) Redundant functions include unnecessary processes or processes that use the same input and produce the same output, e.g. process A — use picking ticket and customer master to produce the packing slip; process B — produce the packing slip by using the customer master and picking ticket as inputs.

(iii) Redundant data are unused data, e.g. the credit file includes the data items, spouse's name, occupation, and salary, that are never used.

(6) Incorrect: the specifications are incorrect when they have the following traits:

(i) Incorrect processes refer to wrong procedures used in data manipulation, e.g. calculate the amount owed by the customer:

item value = item price \* quantity

new amount = item value - discount

tax = new amount \* 0.05

amount owed = new amount + tax

Since the tax should be a percentage of the item value instead of the new amount, this processing is incorrect.

Inefficient processes refer to inefficient procedures used in data manipulation, e.g. a process calculates the amount owed by a customer; another process that succeeds this immediately recalculates the amount. The second process is inefficient.

(iii) Wrong precedence relationships involve the sequence of processes in a system. A wrong sequence of processes will not lead to the required system outputs, e.g. to prepare a picking ticket, the processes 'prepare internal order', 'check credit', and 'prepare picking ticket' need to be performed in that order. Instead, if the sequence is given as 'check credit', 'prepare internal order', and 'prepare picking ticket', then the precedence relationships are wrong.

(iv) Unperformable processes are those processes that may not be performed at all, e.g. the process 'B' or the process 'C' needs to be performed after the process 'A'. The performing of the process 'B' or the process 'C' depends on the outcome of the process 'A'. The outcome of the process 'A' is such that the process 'B' is never performed.

(v) Two processes producing the same output for a transaction may be an incorrect specification, e.g. either a process called 'process back order' or a process called 'process accepted order' should produce a picking ticket. If both the processes produce the picking ticket for the same transaction, then one of them is incorrect.

(vi) System properties violation occurs when the specifications violate or contradict the expected system properties, e.g. an order processing system may produce either an accepted order or a rejected order. If the specifications are such that both the accepted order and the rejected order are produced for a transaction, then the specifications violate the system properties.

(vii) Incorrect timing refers to the nonavailability of the required inputs for a process in time, e.g. a process called 'process material receipt' requires the inputs 'bill of lading' and 'purchase order'. Both the inputs are available but not in time.

## Requirements verification techniques

This section examines various requirements verification techniques. Several requirements analysis approaches advocate verification but some of these (Aschim and Mostue, 1982; Knuth et al., 1982; PRIDE, 1986; Solvberg, 1982) have not documented their verification techniques. This section discusses the documented verification techniques. In addition, it examines the capability of each technique and shows that each technique identifies only a few of the errors.

This section also reviews the use of these techniques in various requirements analysis approaches. The approaches such as Higher Order Software (USE. IT, 1982), Jackson System Development (Jackson, 1983), and Structured Design (Yourdon and Constantine, 1979) do not have a well defined requirements analysis stage, and hence, are not reviewed here. The approaches such as Bluementhal's approach (1969), Business System Planning (IBM, 1978), Critical Success Factors approach (Rockart, 1979), Information Analysis (King and Cleland, 1975), and Office Analysis Methodology (OAM) (Sirbu et al., 1981) that do not discuss verification are also not reviewed here. Table 2 shown at the end of this section, lists the requirements analysis approaches that are reviewed here.

## Formal foundations

Several software products used in systems development employ formal languages for stating requirements. These artificial languages are not standard and their degree of formality varies. Verification techniques in these languages include cross referencing tables, diagrams such as state transition graphs, and compiler-type checking. Generally, they can identify TBDs, nonexistent references, missing specifications, no minimal completeness, process insufficiency, and convention inconsistency. Highly formalized languages such as Problem Statement Language of Problem Statement Language / Problem Statement Analyzer (PSL/PSA) (Teichroew and Hershey, 1977) can identify internal consistency, redundant functions, and redundant data. In addition, languages such as Requirements Statements Language (RSL) of Software Requirements Engineering Methodology (SREM) (Bell et al., 1977) can identify untraceable specifications, lack of clarity, and lack of precision. The formalized structure of these languages prevents ambiguities and generalities.

The formalized structure of these languages also enables the automation of the verification procedures. Several requirements analysis approaches that use formal languages have automated verification techniques. These approaches are: Conceptual

Information Modeling (CIM) (Gustafsson et al., 1982), Data Oriented Design (DADES) (Olive, 1982), Interpretive Structural Modelling Software (ISMS) (Hansen et al., 1979), PSL/PSA (Teichroew and Hershey, 1977), Structured Systems Analysis and Design Method (SSADM) (Downs et al., 1988), SREM (Bell et al., 1977), Systematic Activity Modeling Method (SAMM) (Stephens and Tripp, 1978), the Technology for the Automated Generation of Systems (TAGS) (Sievert and Mizell, 1985).

## Derivability analysis

Derivability analysis helps to check the logical consistency of requirements specifications (Olive, 1983). In using the derivability analysis, one defines the information sets and precedence rules (a rule applied to a given information set gives its direct precedents) first. Additional precedences are inferred from a set of inference rules. The information sets and the precedence rules are used to check whether or not a given information set is derivable from others. In doing this, it can also check missing relationships, data insufficiency, untraceable specifications, redundant functions, redundant data, and wrong precedence relationships. Since the derivability analysis uses the predicate logic, it is automatable. The Data Oriented Design (DADES) (Olive, 1982) uses this technique for verification. Conceptual Information Modelling (CIM) (Gustafsson et al., 1982) and Sakthivel's approach (Sakthivel and Agarwal, 1987) employ similar techniques.

## Precedence analysis

In an information system, various processes and their precedence relations can be described as a process precedence matrix. Similarly, various information sets and their precedence relations can be described as a data set precedence matrix (Langefors, 1963). Marimont's (1959) procedure can check the consistency of these matrices by detecting contradictions such as the process 'A' precedes the process 'B' and the process 'B' precedes the process 'A'. In addition to such explicit contradictions, it can detect implicit contradictions that are possible in large precedence relationships. The correctness of precedence relationships of processes leading to information system outputs from the inputs can be checked using the Langefors theory. Precedence analysis is useful to detect internal consistency and wrong precedence relationships. Since both Marimont's procedure and Langefors' theory have a mathematical basis, the precedence analysis is automatable. The following requirement analysis approaches use this technique: Briggs' (1966) approach, Information Systems work and Analysis of

Changes (ISAC) (Lundeberg, 1982), PSL/PSA (Teichroew and Hershey, 1977), SODA/PSL (Nunamaker, 1971).

## Simulation

Simulation is an experiment of a real system using its model. Simulation is the most widely used technique for checking feasibility. Be executing a simulation model of an information system, one can check the feasibility of performance requirements before design and implementation (Bell et al., 1977). A dynamic analysis using simulation can check the behaviour of a system in order to detect timing problems. The simulation also helps to check the efficiency of a system within a specific resource environment (Estrin et al., 1986; Sakthivel and Tanniru, 1988–89).

In using simulation, one needs to ensure that the simulation model reflects the behaviour of the system (Shannon, 1975). Without such checks, the inferences drawn from the simulation results may be incorrect. Since the cost of producing an accurate simulation model can be high, automatic simulation generators are essential to obtain the simulation model from the requirement specifications. The simulation of a system needs certain design parameters such as processing assumptions (on-line, real-time, or batch), transaction volumes, their frequency distribution, process times, and their frequency distribution. In this regard, the use of simulation to verify feasibility causes intermingling of design and requirements analysis stages. The requirements analysis approaches that use simulation are: Bodard et al's, (1979; 1985) approach, REMORA (Rolland and Richard, 1982), Sakthivel's (1988–89) approach, SREM (Bell et al., 1977), Systems Architects Apprentice (SARA) (Estrin et al., 1986), TAGS (Sievert and Mizell, 1985). These approaches, however, do not mention any checking to ensure the accuracy of the simulation models.

## Prototyping

Prototyping is a method for developing information systems in which a tentative version of the system is rapidly developed and then iteratively refined based on user feedback. Prototyping compresses various life-cycle stages into one process and repeats this process several times until the system is accepted by the users. Though Naumann and Jenkins (1982) advocate prototyping as an alternate paradigm for systems development, it is more useful when integrated into the life-cycle approach (Dearnley and Mayhew, 1983; Janson and Smith, 1985). Prototyping has the following uses in the life-cycle approach:

(1) To elicit and establish user requirements.

(2) To ascertain the feasibility and acceptability of the

proposed solutions to a problem.

(3) To assess the feasibility of the target system in handling the anticipated workload.

(4) To estimate the organizational resources for supporting the system.

(5) To develop evolving systems (Law, 1985; Mayhew and Dearnley, 1987).

Since prototyping involves the construction of a system, it enables the identification of the following errors: process insufficiency, data insufficiency, missing relationships, internal inconsistency, external inconsistency, redundant functions, redundant data, wrong precedence relationships. Operating a prototyped system by the users enables the detection of the following errors: conceptual omissions, untraceable specifications, redundant requirements, incorrect processes, system properties violation. However, a successful detection of these errors is contingent upon devising a full fledged prototype that is operated under real conditions.

Prototyping is an iterative process. The use of the fourth generation languages and micro computers simplifies prototyping. Several requirements analysis that employ the prototyping technique are: Active and Passive Component Modelling (ACM/PCM) (Brodie and Silva, 1982), Bodart et al's approach (1985), ISAC (Lundeberg, 1982), MERISE (Rochfield and Tardieu, 1983), User Software Engineering (USE) (Wasserman, 1982).

## Petri Nets

Petri Nets are bipartite graphs that have modelling and analytical power. They are useful during the requirements analysis and design stages (Richter and Durchholz, 1982; Sakthivel and Tanniru, 1988–89). Petri Nets have several mathematical properties that are useful in verification. The modelling and verification power of Petri Nets are superior to those of the available formal foundations (Sakthivel and Tanniru, 1988–89). The Petri Nets enable the identification of the following errors: TBDs, nonexistent references, no minimal completeness, process insufficiency, missing relationships, convention consistency, internal consistency, hierarchical inconsistency, unclear and ambiguous specifications, redundant functions, wrong precedence relationships, unperformable processes, two processes that produce the same output, systems properties violation (Sakthivel and Tanniru, 1988–89). Petri Net theory has several extensions and timed Petri Net is one of them (IEEE International Workshop on Timed Petri Nets, 1985). The timed Petri Nets can measure the performance and identify incorrect timing. Since using Petri Nets in verification involves the construction of matrices and manipulation of them, computer support is essential. Since Petri Nets have mathematical properties, the automation of this technique is possible.

## Dual specifications

Dual specifications involve introducing redundancy in specifications in order to facilitate a comparison of them. Such comparison can pinpoint ambiguities and misinterpretations; viewing the same system from several points helps to identify omissions and contradictions. If multiple views of a system do not agree, then at least one of them should be incorrect. An approach in dual specifications is to develop the specifications by two teams (Ramomoorthy et al., 1978). Another approach is to obtain several viewpoints by the same team and then cross reference these specifications (An Introduction to SADT™, 1976; Downs et al., 1988). Dual specifications can detect the following requirement errors: conceptual omissions, internal consistency, unclear and ambiguous specifications, redundant requirements, and redundant functions. Wasserman (1982) advocates a reconciliation between the user views and developer views for checking the traceability. To automate verification by dual specifications, formalized languages are essential.

## Data flow diagram algebra

Several approaches emphasize the need for hierarchical decomposition to manage the complexity of large projects. They suggest presenting an overview of the information system requirements and then decomposing complex processes in a top-down manner. These approaches, however, do not explain any technique to check the consistency of such decomposition. Since data flow diagrams are commonly used for specifying requirements (DeMarco, 1979; Gane and Sarson, 1979), Adler (1988) has provided a technique for consistent hierarchical decomposition of data flow diagrams. In this technique, an analyst identifies a process for decomposition, he/she then defines an input/output matrix that shows what inputs are used to produce various outputs of the process. Next, he/she produces a directed acyclic graph from the matrix. Using certain decomposition rules and operators described by Adler (1988), the analyst can produce a decomposition graph and transform it into a decomposed data flow diagram. Adler (1988) has also provided metrics to test the quality of the decomposition and has implemented this technique as a PROLOG model to provide an automated tool.

In hierarchical decomposition, Adler's method is also inadequate because the analyst has to choose a process for decomposition. Ewusi-Mensah (1984) has provided a method for identifying subsystems of an information system. The use of these two techniques will help to ensure the hierarchical consistency. No requirement analysis approach uses these techniques for hierarchical decomposition. However, Structured Analysis (DeMarco, 1979) and Structured Analysis Design and Implementation of Information Systems (STRADIS, 1983) approaches are good candidates for employing this technique.

## Reviews

Reviews are manual techniques that may detect most types of errors except infeasible performance requirements. Though they are the best among the available techniques, they do not guarantee complete verification. Since review techniques are manual and informal, their capability is contingent upon the efficiency, knowledge, and skills of the reviewers. These techniques are ad hoc and time consuming with automated support for reviews available only for documentation. A review can be a walkthrough or an inspection; Yourdon (1977) and Freedman and Weinberg (1982) have discussed various review techniques in detail.

## Walkthroughs

The objective of a walkthrough is to review the system requirements by a group of people involved in the system. A walkthrough enables an exchange of diverse viewpoints of a system and can be informal or formal. An informal walkthrough can be an interview of the user. Formal walkthroughs involve meetings of other analysts and the users. In a formal walkthrough, the developing analyst explains the system requirements. The participants may ask clarifications; identify incomplete, incorrect, redundant, and inconsistent specifications; and also suggest improvements. Several walkthroughs may be necessary until the acceptance of the system requirement specifications.

The following approaches suggest walkthroughs for verification: Development of Data Sharing Systems 2 (D2S2) (MacDonald and Palmer, 1982), ISAC (Lundeberg, 1982), MERISE (Rochfield and Tardieu, 1983), Nijssens Information Analysis Method (NIAM) (Verheijen and VanBekkum, 1982), Structured Analysis Design and Implementation of Information Systems (STRADIS, 1983), Structured Analysis (SA) (DeMarco, 1979), Structured Requirements Definition (SRD) (Orr, 1981), TAGS (Sievert and Mizell, 1985). The Structured Analysis and Design Technique (SADT) (Ross, 1977; 1985) and ACM/PCM (Brodie and Silva, 1982) use a variation of the walkthrough technique called author/reader cycle. This technique involves a review of the requirement specifications between the user and the developer in cycles.

## Inspections

An inspection basically involves an examination of the requirement specifications. The inspection may involve reading of the specifications, cross-referencing, or a check-list. The inspector may use simple scenarios which assess the requirements. To be successful, he/she should know what to look for in the specifications, these can be in the form of a check list. These checklists contain a list of 'do's and 'don't's based on the analyst's experience (Miyamoto and Yeh, 1981). The following approaches suggest inspection: D2S2 (MacDonald and Palmer, 1982), Information Engineering (IE) (Martin and Finkelstein, 1981), ISAC (Lundeberg, 1982), MERISE (Rochfield and Tardieu, 1983), NIAM (Verheijen and VanBekkum, 1982), Rzevski et al's (1982) approach, SA (DeMarco, 1979), STRADIS (1983).

## Summary

This section has reviewed several verification techniques and the capability of each technique to detect various requirement errors (see Table 1). Table 1 shows the capabilities attributable to a technique per se. Each technique has a specific orientation and is useful to verify only a few errors. No technique can detect homonyms and synonyms, infeasible system objectives, infeasible functional needs, and inefficient processes. Though reviews provide good verification (Fagan, 1976), they are manual, ad hoc, and time consuming. Furthermore, the success in using review techniques depends to a great extent on the reviewers. All the verification techniques except reviews are automatable. Computer-Aided Systems Engineering (CASE) tools which assist in systems development (Benyon and Skidmore, 1987; McClure, 1989; Schneider and Wasserman, 1982) are good for documentation, project management, and graphics (Peters, 1987). Their use in verification, however, is limited to identifying nonexistent references, no minimal completeness, convention inconsistency, and internal inconsistency. Two studies have shown that SREM and PSL/PSA have good CASE tools but they are weak in providing an adequate verification (Salwin, 1977; Stainer, 1976).

This section also reviewed several requirements analysis approaches which use various verification techniques. These are summarized in Table 2. Though most approaches employ several verification techniques, the do not provide an adequate verification. For example, SREM is a widely used approach in the development of weapon systems (Salwin, 1977; Stainer, 1976). SREM uses formal foundations and simulation techniques but is not effective in verification (Scheffer et al., 1985).

## Future research and conclusions

This paper has shown that available verification techniques are weak and various requirements analysis approaches using these techniques do not provide a comprehensive verification. An approach may integrate more techniques to provide an adequate verification. However, the nature of specification languages used in most approaches prohibits a gainful integration of several techniques. For example, Structured Analysis may use reviews (manual) and data flow algebra technique for verification. Since the specifications in Structured Analysis are verbal and the data flow diagrams are abstract, the use of simulation or formal foundations is impractical. Knowledge-based techniques integrated into a knowledge-based requirements analysis approach may provide an adequate verification.

Several studies have suggested a knowledge-based approach for requirements analysis (Blackburn, 1989; Borgida et al., 1985; Tanik and Yu, 1988). The knowledge-based approach satisfies the following requirement specifications criteria: abstraction, decomposition, a facility for handling time, exceptions, and uncertainty, automation, a basis for design. Whereas, the available requirements analysis approaches use artificial languages with strict syntax to specify the requirements, the knowledge-based approach can represent the requirements in a natural and convenient fashion.

To understand and use the requirements, the specifications should include information not only about the system (concrete knowledge) but also about its environment (abstract knowledge) (Bubenko, 1980; Loucopoulos and Champion, 1988). Most requirements analysis approaches focus only on specifying the computer-oriented requirements and use the available techniques to verify these requirements. Certain approaches such as Office Analysis Methodology (OAM) (Sirbu et al., 1981) which include information about the system and its environment do not use any verification techniques. The knowledge-based approach can unify the concrete and abstract knowledge to capture, model, and analyze the requirements effectively. Such a requirements analysis approach is superior to available approaches (Borgida et al., 1985; Bubenko, 1980; Roman, 1985; Zave, 1982). Knowledge-based techniques, such as deduction and inference integrated into the knowledge-based approach can aid in verification. The specifications can include time dimensions to simulate the system in order to identify the feasibility of user needs and resource usage. In addition, the system can be prototyped for further verification. The deductive and logic power of the knowledge-based approach can be supplemented by the formal foundations, simulation, and prototyping to provide an adequate verification. Furthermore, the entire verification process is automatable.

Table 1 Requirement errors identifiable by various techniques

<table><tr><td rowspan="5"></td><td>F</td><td>D</td><td>P</td><td>S</td><td>P</td><td>P</td><td>D</td><td>D</td><td>R</td><td>K**</td></tr><tr><td>o</td><td>e</td><td>r</td><td>i</td><td>r</td><td>e</td><td>u</td><td>a</td><td>e</td><td>n</td></tr><tr><td>r</td><td>r</td><td>e</td><td>m</td><td>o</td><td>t</td><td>a</td><td>t</td><td>v</td><td>o</td></tr><tr><td>m</td><td>i</td><td>c</td><td>u</td><td>t</td><td>r</td><td>l</td><td>a</td><td>i</td><td>w</td></tr><tr><td>a</td><td>v</td><td>e</td><td>l</td><td>o</td><td>i</td><td>S</td><td>F</td><td>e</td><td>l</td></tr><tr><td rowspan="6">Verification techniques</td><td>l</td><td>a</td><td>d</td><td>a</td><td>t</td><td>N</td><td>p</td><td>l</td><td>w</td><td>e</td></tr><tr><td>F</td><td>b</td><td>e</td><td>t</td><td>y</td><td>e</td><td>e</td><td>o</td><td>s</td><td>d</td></tr><tr><td>o</td><td>i</td><td>n</td><td>i</td><td>p</td><td>t</td><td>c</td><td>w</td><td></td><td>g</td></tr><tr><td>u</td><td>l</td><td>c</td><td>o</td><td>i</td><td>s</td><td>i</td><td>A</td><td></td><td>e</td></tr><tr><td>n</td><td>i</td><td>e</td><td>n</td><td>n</td><td></td><td>f</td><td>l</td><td></td><td>b</td></tr><tr><td>d</td><td>t</td><td>A</td><td></td><td>g</td><td></td><td>i</td><td>g</td><td></td><td>a</td></tr><tr><td rowspan="6">Requirement errors</td><td>a</td><td>y</td><td>n</td><td></td><td></td><td></td><td>c</td><td>e</td><td></td><td>s</td></tr><tr><td>t</td><td>A</td><td>a</td><td></td><td></td><td></td><td>a</td><td>b</td><td></td><td>e</td></tr><tr><td>i</td><td>n</td><td>l</td><td></td><td></td><td></td><td>t</td><td>r</td><td></td><td>d</td></tr><tr><td>o</td><td>a</td><td>y</td><td></td><td></td><td></td><td>i</td><td>a</td><td></td><td>a</td></tr><tr><td>n</td><td>l</td><td>s</td><td></td><td></td><td></td><td>o</td><td></td><td></td><td>p</td></tr><tr><td>s</td><td>y</td><td>i</td><td></td><td></td><td></td><td>n</td><td></td><td></td><td>p</td></tr><tr><td rowspan="5">v</td><td></td><td>s</td><td>s</td><td></td><td></td><td></td><td>s</td><td></td><td></td><td>r</td></tr><tr><td></td><td>i</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>o</td></tr><tr><td></td><td>s</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>a</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>c</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>h</td></tr><tr><td colspan="11">1. Incomplete</td></tr><tr><td>1.1 TBDs</td><td>x</td><td></td><td></td><td></td><td></td><td>x</td><td></td><td></td><td>x</td><td>l</td></tr><tr><td>1.2 Nonexistent references</td><td>x</td><td></td><td></td><td></td><td></td><td>x</td><td></td><td></td><td>x</td><td>l</td></tr><tr><td>1.3 Missing specifications</td><td>x</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>x</td><td>l</td></tr><tr><td>1.4 No minimal completeness</td><td>x</td><td></td><td></td><td></td><td></td><td>x</td><td></td><td></td><td>x</td><td>l</td></tr><tr><td>1.5 Process insufficiency</td><td>x</td><td></td><td></td><td></td><td>x</td><td>x</td><td></td><td></td><td>x</td><td>l</td></tr><tr><td>1.6 Missing relationships</td><td></td><td>x</td><td></td><td></td><td>x</td><td>x</td><td></td><td></td><td>x</td><td>l</td></tr><tr><td>1.7 Data insufficiency</td><td></td><td>x</td><td></td><td></td><td>x</td><td></td><td></td><td></td><td>x</td><td>l</td></tr><tr><td>1.8 Conceptual omissions</td><td></td><td></td><td></td><td></td><td>x</td><td></td><td>x</td><td></td><td>x</td><td>l</td></tr><tr><td colspan="11">2. Inconsistent</td></tr><tr><td>2.1 Convention inconsistency</td><td>x</td><td></td><td></td><td></td><td></td><td>x</td><td></td><td></td><td>x</td><td>l</td></tr><tr><td>2.2 Homonyms or synonyms</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>x</td><td>l</td></tr><tr><td>2.3 Internal consistency</td><td>x</td><td></td><td>x</td><td></td><td>x</td><td>x</td><td>x</td><td></td><td>x</td><td>l</td></tr><tr><td>2.4 External consistency</td><td></td><td></td><td></td><td></td><td>x</td><td></td><td></td><td></td><td>x</td><td>l</td></tr><tr><td>2.5 Untraceable specifications</td><td>x</td><td>x</td><td></td><td></td><td>x</td><td></td><td>x</td><td></td><td>x</td><td>l</td></tr><tr><td>2.6 Hierarchical consistency</td><td></td><td></td><td></td><td></td><td></td><td>x</td><td></td><td>x</td><td></td><td>l</td></tr><tr><td colspan="11">3. Infeasible</td></tr><tr><td>3.1 Infeasible system objectives</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>?</td></tr><tr><td>3.2 Infeasible user needs</td><td></td><td></td><td></td><td>x</td><td>x</td><td></td><td></td><td></td><td></td><td>2</td></tr><tr><td>3.3 Infeasible functional needs</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>?</td></tr><tr><td>3.4 Infeasible resource usage</td><td></td><td></td><td></td><td>x</td><td></td><td></td><td></td><td></td><td></td><td>2</td></tr><tr><td colspan="11">4. Untestable</td></tr><tr><td>4.1 Unclear and ambiguous</td><td>x</td><td></td><td></td><td></td><td></td><td>x</td><td>x</td><td></td><td>x</td><td>l</td></tr><tr><td>4.2 Imprecise</td><td>x</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>x</td><td>l</td></tr><tr><td colspan="11">5. Redundant</td></tr><tr><td>5.1 Redundant requirements</td><td></td><td></td><td></td><td></td><td>x</td><td></td><td>x</td><td></td><td>x</td><td>l</td></tr><tr><td>5.2 Redundant functions</td><td>x</td><td>x</td><td></td><td></td><td>x</td><td>x</td><td>x</td><td></td><td>x</td><td>l</td></tr><tr><td>5.3 Redundant data</td><td>x</td><td>x</td><td></td><td></td><td>x</td><td></td><td></td><td></td><td>x</td><td>l</td></tr><tr><td colspan="11">6. Incorrect</td></tr><tr><td>6.1 Incorrect processes</td><td></td><td></td><td></td><td></td><td>x</td><td></td><td>x</td><td></td><td>x</td><td>l</td></tr><tr><td>6.2 Inefficient processes</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>x</td><td>l</td></tr><tr><td>6.3 Wrong precedence relationships</td><td></td><td>x</td><td>x</td><td></td><td>x</td><td>x</td><td></td><td></td><td></td><td>l</td></tr><tr><td>6.4 Unperformable processes</td><td></td><td></td><td></td><td></td><td></td><td>x</td><td></td><td></td><td></td><td>l</td></tr><tr><td>6.5 Two processes produce the same output</td><td></td><td></td><td></td><td></td><td></td><td>x</td><td></td><td></td><td></td><td>l</td></tr><tr><td>6.6 System properties violation</td><td></td><td></td><td></td><td></td><td>x</td><td>x</td><td></td><td></td><td></td><td>l</td></tr><tr><td>6.7 Incorrect timing</td><td></td><td></td><td></td><td>x</td><td></td><td>x</td><td></td><td></td><td></td><td>l</td></tr></table>

\*\* - Knowledge-based approach is proposed in the last section  
1 - Errors identifiable by the knowledge-based technique  
2 - Errors identifiable by using simulation in the knowledge-based approach  
? - Errors not identifiable by any technique

Table 2 Requirements analysis approaches using various verification techniques

<table><tr><td rowspan="20">Verification techniques</td><td>F</td><td>D</td><td>P</td><td>S</td><td>P</td><td>P</td><td>D</td><td>D</td><td>R</td></tr><tr><td>o</td><td>c</td><td>r</td><td>i</td><td>r</td><td>c</td><td>u</td><td>a</td><td>e</td></tr><tr><td>r</td><td>r</td><td>e</td><td>m</td><td>o</td><td>t</td><td>a</td><td>t</td><td>v</td></tr><tr><td>m</td><td>i</td><td>c</td><td>u</td><td>t</td><td>r</td><td>l</td><td>a</td><td>i</td></tr><tr><td>a</td><td>v</td><td>e</td><td>l</td><td>o</td><td>i</td><td>S</td><td>F</td><td>e</td></tr><tr><td>l</td><td>a</td><td>d</td><td>a</td><td>t</td><td>N</td><td>p</td><td>l</td><td>w</td></tr><tr><td>F</td><td>b</td><td>e</td><td>t</td><td>y</td><td>e</td><td>e</td><td>o</td><td>s</td></tr><tr><td>o</td><td>i</td><td>n</td><td>i</td><td>p</td><td>t</td><td>c</td><td>w</td><td></td></tr><tr><td>u</td><td>l</td><td>c</td><td>o</td><td>i</td><td>s</td><td>i</td><td>A</td><td></td></tr><tr><td>n</td><td>i</td><td>e</td><td>n</td><td>n</td><td></td><td>f</td><td>l</td><td></td></tr><tr><td>d</td><td>t</td><td>A</td><td></td><td>g</td><td></td><td>i</td><td>g</td><td></td></tr><tr><td>a</td><td>y</td><td>n</td><td></td><td></td><td></td><td>c</td><td>e</td><td></td></tr><tr><td>t</td><td>A</td><td>a</td><td></td><td></td><td></td><td>a</td><td>b</td><td></td></tr><tr><td>i</td><td>n</td><td>l</td><td></td><td></td><td></td><td>t</td><td>r</td><td></td></tr><tr><td>o</td><td>a</td><td>y</td><td></td><td></td><td></td><td>i</td><td>a</td><td></td></tr><tr><td>n</td><td>l</td><td>s</td><td></td><td></td><td></td><td>o</td><td></td><td></td></tr><tr><td>s</td><td>y</td><td>i</td><td></td><td></td><td></td><td>n</td><td></td><td></td></tr><tr><td></td><td>s</td><td>s</td><td></td><td></td><td></td><td>s</td><td></td><td></td></tr><tr><td></td><td>i</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>s</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Active component modeling/passive component modeling (Brodie and Silva, 1982)</td><td></td><td></td><td></td><td></td><td>x</td><td></td><td></td><td></td><td>x</td></tr><tr><td>Bodart&#x27;s approach (Bodart et al., 1985)</td><td></td><td></td><td></td><td>x</td><td>x</td><td></td><td></td><td></td><td></td></tr><tr><td>Conceptual information modeling (Gusatfsson et al., 1982)</td><td>x</td><td>x</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Data oriented design (Olive, 1982)</td><td>x</td><td>x</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Development of Data Sharing Systems (Macdonald and Palmer, 1982)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>x</td></tr><tr><td>Information engineering (Martin and Finkelstein, 1981)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>x</td></tr><tr><td>Information systems work and analysis of change (Lundeberg, 1982)</td><td></td><td></td><td>x</td><td></td><td>x</td><td></td><td></td><td></td><td>x</td></tr><tr><td>Interpretive structural modeling software (Hansen et al., 1979)</td><td>x</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>MERISE (Rochfield and Tardieu, 1983)</td><td></td><td></td><td></td><td></td><td>x</td><td></td><td></td><td></td><td>x</td></tr><tr><td>Nijssens information analysis method (Verheijen and VanBekkum, 1982)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>x</td></tr><tr><td>Problem Statement language / problem statement analyzer (Teichroew and Hershey, 1977)</td><td>x</td><td></td><td>x</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>REMORA (Rolland and Richard, 1982)</td><td></td><td></td><td></td><td>x</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Rzevski&#x27;s approach (Rzevski et al., 1982)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>x</td></tr><tr><td>Sakthivel&#x27;s approach (Sakthivel and Tanniru, 1988–89)</td><td></td><td>x</td><td></td><td>x</td><td></td><td>x</td><td></td><td></td><td></td></tr><tr><td>Software requirements engineering methodology (Bell et al., 1977)</td><td>x</td><td></td><td></td><td>x</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Structured analysis (DeMarco, 1979)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>x</td><td>x</td></tr><tr><td>Structured analysis and design technique (Ross, 1977)</td><td></td><td></td><td></td><td></td><td></td><td></td><td>x</td><td></td><td>x</td></tr><tr><td>Structured analysis, design, and implementation of information systems (STRADIS, 1983)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>x</td><td>x</td></tr><tr><td>Structured requirements definition (Orr, 1981)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>x</td></tr><tr><td>Structured systems analysis and design method (Downs et al., 1988)</td><td>x</td><td></td><td></td><td></td><td></td><td></td><td>x</td><td></td><td></td></tr><tr><td>Systematic activity modeling method (Stephens and Tripp, 1978)</td><td>x</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Systems architects apprentice (Estrin et al., 1986)</td><td></td><td></td><td></td><td>x</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Technology for automated generation of system (Sievert and Mizell, 1985)</td><td>x</td><td></td><td></td><td>x</td><td></td><td></td><td></td><td></td><td>x</td></tr><tr><td>User software engineering (Wasserman, 1981)</td><td></td><td></td><td></td><td></td><td>x</td><td></td><td>x</td><td></td><td></td></tr><tr><td>**Knowledge-based approach</td><td></td><td></td><td></td><td>x</td><td>x</td><td></td><td></td><td></td><td></td></tr></table>

\*\* - Knowledge-based approach is proposed in the next section. The major technique in this approach is knowledge-based. In addition, the system can be simulated and prototyped.

Though over fifty requirements analysis approaches have been developed in the past two decades, only five papers addressed the issue of requirements verification adequately (Bell and Thayer, 1976; Boehm, 1984; Howden, 1982; Miyamoto and Yeh, 1981; Sakthivel and Tanniru, 1988–89). Due to the importance of requirements verification in terms of system cost, development productivity, and system quality, more research is needed in this area. An integrated knowledge-based approach for requirements specification, analysis, and verification may provide solutions to requirements verification problems.

Abdel-Hamid (1988) used a simulation-based case study to show the existence of an optimal verification effort for a system development project. He showed that the system development cost decreases with structured walkthrough effort but increases after a certain point. Similar studies to find the cost effectiveness of various verification techniques can be conducted. The selection of a verification technique should be guided by its appropriateness for use in a requirements analysis approach, the efficiency of the technique, and the cost effectiveness of the technique.

## References

Abdel-Hamid, T.K. (1988) The economics of software quality: a simulation based case study. MIS Quarterly, 12, 395–411.

Adler, M. (1988) An algebra for data flow diagram process decomposition. IEEE Transactions on Software Engineering, 14, 169–183.

Adrion, W.R., Branstad, M.A. and Cherniavsky, J.C. (1982) Validation, verification, and testing of computer software. Computing Surveys, 14, 159–192.

Alford, M.W. (1977) A requirements engineering methodology for real-time processing requirements. IEEE Transactions on Software Engineering, SE-3, 60–69. An Introduction to SADT $^{TM}$ (1976) Document 9022-78, Waltham, MA, USA.

Aschim, F. and Mostue, B.M. (1982) IFIP WG 8.1 case solved using SYSDOC and SYSTEMATOR, in Information Systems Design Methodologies: A Comparative Review, Olle, T.W., Sol, H.G. and Verrijn-Stuart, A.A. (eds.). (North-Holland, New York, NY) 15–40.

Bell, T.E., Bixler, D.C. and Dyer, M.E. (1977) An extendable approach to computer-aided software requirements engineering. IEEE Transactions on Software Engineering, SE-3, 49–59.

Bell, T.E. and Thayer, T.A. (1976) Software requirements: are they really a problem?, in Proceedings of the 2nd International Conference on Software Engineering. (IEEE Computer Society Press, Los Alamitos, CA, USA).

Benyon, D. and Skidmore, S. (1987) (eds.). Automating Systems Development. (Plenum, New York, NY).

Blackburn, M.R. (1989) Using expert systems to construct formal specifications. IEEE Expert, 4, 62–74.

Bluementhal, S.C. (1969) Management Information Systems - A Framework for Planning and Development. (Prentice-Hall, Englewood Cliffs, NJ).

Bodart, F. and Pigneur, Y. (1979) A model and a language for functional specifications and evaluation of information systems dynamics, in Formal Models and Practical Tools for Information Systems Design, Schneider, H.J. (ed) North-Holland, (New York, NY), pp. 257–279.

Bodart, F., Hennebert, A.M., Leheureux, J.M. and Pigneur, Y. (1985) Computer-aided specification, evaluation, and monitoring of information systems, in Proceedings of 1985 International Conference on Information Systems, 27–44.

Boehm, B.W. (1977) Software Engineering Techniques,

seven basic principles of software engineering, in Infotech state of the art report, Infotech, London.

Boehm, B.W. (1984) Validating and verifying software requirements and design specifications. IEEE Software, 1, 75–88.

Boehm, B.W. (1987) Improving software productivity. Computer, 20, 43–57.

Borgida, A., Greenspan, S. and Mylopoulos, J. (1985) Knowledge representation as the basis for requirements specifications. Computer, 18, 82–91.

Briggs, R.B. (1966) A mathematical model for the design of information management systems, MS thesis, Division of Natural Science, University of Pittsburgh, Pittsburg, PA, USA.

Brodie, M.L. and Silva E. (1982) Active and passive component modelling: ACM/PCM in Information Systems Design Methodologies: A Comparative Review Olle,

T.W., Sol, H.G. and Verrijn-Stuart, A.A. (eds) (North-Holland, New York, NY). pp. 41–92.

Bubenko, Jr. J.A. (1980) Information modeling in the context of system development, in Information Processing 80, Proceedings of the IFIP Congress, (North-Holland, Amsterdam), pp. 395–411.

Buckley, F.J. and Poston, R. (1984) Software quality assurance. IEEE Transactions on Software Engineering, SE-10, 36–41.

Case, Jr. A.F. (1985) Computer-Aided Software Engineering (CASE): technology for improving productivity. Data base, 17, 35–43.

Dearley, P.A. and Mayhew, P.J. (1983) In favor of system prototypes and their integration into the systems development cycle. The Computer Journal, 26, 36–42.

DeMarco, T. (1979) Structured Analysis and System Specification. (Yourdon Engledwood Cliffs, NJ).

Dijkstra, E.W. (1972) Notes on structured programming, in Structured Programming, Dahl, O.J. et al. (eds) (Academic, New York, NY).

Downs, E., Clare, P. and Coe, I. (1988) Structured Systems Analysis and Design Method, (Prentice-Hall, Hertfordshire, UK).

Estrin, G., Fenchel, R.S., Razouk, R.R. and Vernon, M.K. (1986) SARA (System Architects Apprentice): modeling analysis, and simulation support for design of concurrent systems. IEEE Transactions on Software Engineering, SE-12, 293–311.

Ewusi-Mensah, K. (1984) Identifying subsystems in information systems analysis. Information Systems, 9, 181–190.

Fagan, M.E. (1976) Design and code inspections to reduce errors in program development. IBM Systems Journal, 15, 182–211.

Freedman, D.P. and Weinberg, G.M. (1982) Handbook

of Walkthroughs, Inspections, and Technical Reviews: Evaluating Programs, Projects, and Products. (Little, Brown and Company, Boston, MA).

Gane, C. and Sarson, T. (1979) Structured Systems Analysis: Tools and Techniques. Prentice-Hall, Englewood Cliffs, NJ.

Gustafsson, M.R., Karlsson, T. and Bubenko, J.A. (1982) A declarative approach to conceptual in information modeling, in Information Systems Design Methodologies: A Comparative Review, Olle, T.W., Sol,

H.G. and Verrijn-Stuart, A.A. (eds) (North-Holland, New York, NY) pp. 93–141.

Hansen, J.V., McKell, L.J. and Meitzer, L.E. (1979) ISMS: computer-aided analysis for design of decision support systems. Management Science, 25, 1069–1081.

Howden, W.E. (1982) Life-cycle software validation. Computer, 15, 71–78.

IBM (1978) Business Systems Planning-Information Systems Planning Guide. Manual GE20-0527-2.

IEEE International Workshop on Timed Petri Nets. (1985) Torino, Italy. IEEE Catalog No. 85CH2 187-3, IEEE Computer Society Press.

IEEE Standard Glossary of Software Engineering Terminology. (1983) IEEE Std. 729-1983, IEEE-CS order No. 729, Los Alamitos, CA: IEEE Computer Society.

Jackson, M.A. (1983) System Development, (Prentice-Hall International, London).

Janson, M.A. and Smith, L.D. (1985) Prototyping for systems development: a critical appraisal. MIS Quarterly, 9, 305–316.

King, W.R. and Cleland, D.J. (1975) The design of management information systems, an information analysis approach. Management Science, 22, 286–297.

Knuth, E., Halaz, F. and Rado, P. (1982) SDLA: system descriptor and logical analyzer, in Information Systems Design Methodologies: A Comparative Review. Olle,

T.W., Sol, H.G. and Verrijn-Stuart, A.A. (eds) (North-Holland, New York, NY) pp. 143–171.

Langefors, B. (1963) Some approaches to the theory of information systems. BIT, 3, 229–254.

Law, D. (1985) Prototyping: a state-of-the-art report, in Proceedings of the 1985 National Computer Conference.

Loucopoulos, P. and Champion, R. (1988) Knowledge-based approach to requirements engineering using method and domain knowledge. Knowledge Based Systems, 1, 179–187.

Lundeberg, M. (1982) The ISAC approach to specification of information systems and its application to the organization of an IFIP working conference, in Information Systems Design Methodologies: A Comparative Review. Olle, T.W., Sol, H.G. and Verrijn-Stuart, A.A. (eds) (North-Holland, New York, NY) pp. 173–234.

MacDonald, I.G. and Palmer, I.R. (1982) System development in a shared data environment, in Information Systems Design Methodologies: A Comparative

Review. Olle, T.W., Sol, H.G. and Verrijn-Stuart, A.A. (eds) (North-Holland, New York, NY) pp. 235–283.

Marimont, R.B. (1959) A new method of checking the consistency of precedence matrices. Journal of the ACM, 6, 164–171.

Martin, J. (1985) Program Design Which is Provably Correct. (Prentice-Hall, Englewood Cliffs, NJ).

Martin, J. and Finkelstein, C. (1981) Information Engineering. (Savant Research Studies, Lancashire, England).

Mayhew, P.J. and Dearnley, P.A. (1987) An alternative prototyping classification. The Computer Journal, 30, 481–484.

McClure, C. (1989) A CASE workshop. BYTE, 14, 246.

Miller, E. and Howden, W.E. (eds) (1981) Tutorial: Software Testing and Validation Techniques. IEEE-CS order No. 365, Los Alamitos, CA: IEEE Computer Society.

Miyamoto, I. and Yeh, R.T. (1981) A Software Requirements Analysis and Definition Methodology for Business Data Processing, in Proceedings of the 1981 National Computer Conference, pp. 571–581.

Naumann, J.D. and Jenkins, A.M. (1982) Prototyping: the new paradigm for systems development. MIS Quarterly, 6, 29–44.

Nunamaker, J.F. (1971) A methodology for the design and optimization of information systems, in AFIPS Conference Proceedings, 38, pp. 283–293.

Olive, A.R. (1982) DADES: A methodology for specification and design of information systems, in Information Systems Design Methodologies: A Comparative Review Olle, T.W., Sol, H.G. and Verrijn-Stuart, A.A. (eds) (North-Holland, New York, NY) pp. 285–333.

Olive, A.R. (1983) Information derivability analysis in local information systems. Communications of the ACM, 26, pp. 933–938.

Orr, K.T. (1981) Structured Requirements Definition. Ken Orr and Associates, Topeka, KS).

Peters, L. (1987) Advanced Structured Analysis and Design. (Prentice-Hall, Englewood Cliffs, NJ).

PRIDE, M. Bryce and Associates, Cincinatti, OH.

Ramamoorthy, C.V., Ho, S.F. and So, H.H. (1978) The role of software tools in a methodology for the development and validation of critical software for nuclear plants, in Tutorial: Software Methodology. Ramamoorthy, C.V. and Yeh, R.T. (eds) IEEE Catalog No. EHO 142-0, CA: IEEE Computer Society, pp. 397–415.

Richter, G. and Durchholz, R. (1982) IML-inscribed high-level Petri Nets, in Information Systems Design Methodologies: A Comparative Review. Olle, T.W., Sol, H.G. and Verrijn-Stuart, A.A. (eds). (North-Holland, New York, NY) pp. 335–368.

Rockart, J.F. (1979) Chief executives define their own data needs. Harvard Business Review, 57, 81–93.

Rochfield, A. and Tardieu, H. (1983) MERISE: An

information system design and development methodology. Information and Management, 6, 143–159.

Rolland, C. and Richard, C. (1982) The REMORA methodology for information systems design and management, in Information Systems Design Methodologies: A Comparative Review. Olle, T.W., Sol, H.G. and Verrijn-Stuart, A.A. (eds). (North-Holland, New York, NY) pp. 369–426.

Roman, G-C. (1985) A taxonomy of current issues in requirement engineering. Computer, 18, 14–24.

Ross, D.T. (1977) Structured analysis (SA): a language for communicating ideas. IEEE Transactions on Software Engineering. SE-3, 16–34.

Ross, D.T. (1985) Applications and extensions of SADT. Computer, 18, 25–34.

Rzevski, G., Trafford, D.B. and Wells, M. (1982) The evolutionary design methodology applied to information systems, in Information Systems Design Methodologies: A Comparative Review. Olle, T.W., Sol, H.G. and Verrijn-Stuart, A.A. (eds). (North-Holland, New York, NY) pp. 427–473.

Sakthivel, S. and Agarwal, R. (1987) Verifying the correctness of information systems using PROLOG interpreted Petri nets, in Proceedings of the 1987 Decision Science Institute Conference, 369–371, Decision Sciences Institute, Atlanta, GA, USA.

Sakthivel, S. and Tanniru, M.R. (1988–89) Information system verification and validation during requirements analysis using Petri Nets. Journal of MIS, 33–52.

Salwin, A.E. (1977) A Test Case Comparison of URL/URA and RSL/REVS. Tech. Report FS-77-161, Fleet Systems Department, The John Hopkins University, Laurel, MD.

Scheffer, P.A., Stone, A.H. and Rzepka, W.E. (1985) A case study of SREM. Computer, 18, 47–54.

Schneider, H.J. and Wasserman, A.I. (1982) (eds). Automated Tools for Information Systems Design. (North-Holland, New York, NY).

Shannon, R.E. (1975) Systems Simulation, The Art of Science, (Prentice-Hall, Englewood Cliffs, NJ).

Sirbu, M., Schoichet, S., Kunin, J. and Hammer, M. (1981) OAM: an office analysis methodology. Memo OAM-106, MIT.

Sievert, G.E. and Mizell, T.A. (1985) Specification-based software engineering with TAGS. Computer, 18, 56–65.

Solvberg, A. (1982) A draft proposal for integrating system specification models, in Information Systems Design Methodologies: A Comparative Review. Olle, T.W.,

Sol, H.G. and Verrijn-Stuart, A.A. (eds). (North-Holland, New York, NY) pp. 475–535.

Stainer, H.M. (1976) An Evaluation of PSL/PSA and RSL/REVS, Two Computer Assisted Software Requirements/

Specification/Description Tools. Tech. Report FS-76-205, Fleet Systems department, The John Hopkins University, Laurel, MD.

Stephens, S.A. and Tripp, L.L. (1978) Requirements expression and verification aid, in Proceedings of the 2nd International Conference on Software Engineering, IEEE Computer Society Press, Los Alamitos, CA, USA, 101–108.

STRADIS. (1983) McAuto (UK), Surrey, U.K.

Tanik, M.M. and Yun, D.Y.Y. (eds) (1988) AI/software engineering (Special Issue). IEEE Expert, 3.

Teichroew, D. and Hershey, E.A. (1977) PSL/PSA: A computer-aided technique for structured documentation and analysis of information processing systems. IEEE Transactions on Software Engineering, SE-3, 41–48.

USE.IT Reference Manual. (1982) Higher-Order Software, Cambridge, MA.

Verheijen, G.M.A. and VanBekkum, J. (1982) NIAM: an information analysis method, in Information Systems Design Methodologies: A Comparative Review. Olle, T.W., Sol, H.G. and Verrijn-Stuart, A.A. (eds). (North-Holland, New York, NY) pp. 537–589.

Wallace, D.R. (1985) The validation, verification and testing of software: an enhancement to software maintainability, in 1985 Conference on Software Engineering Proceedings, pp. 69–77. IEEE Computer Society Press, Los Alamitos, CA, USA.

Wasserman, A.I. (1982) The user software engineering methodology: an overview, in Information Systems Design Methodology: A Comparative Review. Olle,

T.W., Sol, H.G. and Verrijn-Stuart, A.A. (eds). (North-Holland, New York, NY) pp. 591–628.

Yourdon, E. (1977) Structured Walkthroughs. (Yourdon, New York, NY).

Yourdon, Y. and Constantine, L.L. (1979) Structured Design, (Prentice-Hall, Englewood Cliffs, NJ).

Zave, P. (1982) An operational approach to requirements specification for embedded systems, IEEE Transactions on Software Engineering, SE-8, 250–269.

## Biographical notes

Dr S. Sakthivel is an Assistant Professor of MIS at Bowling Green State University. He completed his Ph.D. in August 1989 from Syracuse University, U.S.A. His research interests are in systems analysis and software engineering. He has published in the Journal of MIS and in several conferences.

Address for correspondence: Dr. S. Sakthivel, Dept of Accounting, MIS Bowling Green State University, Bowling Green, Ohio 43403, USA.
