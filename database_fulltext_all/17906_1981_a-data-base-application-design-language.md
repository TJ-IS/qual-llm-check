---
otero_id: 17906
otero_key: "Z895G9XR"
title: "A data-base application design language"
authors: "Donald A. Jardine; Barbara J. Davis"
year: "1981"
journal: "Information & Management"
doi: "10.1016/0378-7206(81)90004-5"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Data-Base Application Design Language

Donald A. Jardine and Barbara J. Davis

Department of Computing and Information Science, Queen's University at Kingston, Kingston, Ontario, Canada

High-level specification languages allow easy description of large application systems and encourage better designs with cleaner interfaces. Most such languages are concerned with system software development rather than business applications. A simple language called Pseudo-code, which incorporates concepts of module interconnection languages and application specification languages with specific features for data base and file-handling applications, is defined. The language is not executable, but a processor has been implemented to analyze Pseudo-code programs for syntactic correctness and to produce various reports to assist in the design and development of application software.

Keywords:

![](/api/attachments/Z895G9XR/fulltext/images/2bd874909b4df19268834482ce65732032c95af78abf3a16b0422e830ed79b33.jpg)  
Dr. D.A. Jardine is Professor of Computing and Information Science at Queen's University, Kingston, Ontario Canada. He received his Bachelors and Masters degrees at Queen's University and his Ph.D at the University of Delaware. His research interests are in data base definition and design.  
Ms. Barbara J. Davis is a systems Analyst at Maritime Computers Ltd. in Halifax, Nova Scotia, Canada. She received her B.Sc. degree at Acadia University, Nova Scotia and her M.Sc. at Queen's University.

## 1. Introduction

The high and increasing cost of developing software using existing methods has directed our attention to increasingly more powerful methods of analysis and design and in particular to the application of engineering discipline and the development of "software engineering principles" [4].

Software development involves analysis and specification of requirements, and design, implementation, and maintenance of programs. The most critical factor for successful production of software is the design stage. Errors in design not only account for the largest source of program errors, but are the most difficult to detect and correct [1]. The numerous advantages of structured programming [6] have led to an architecture for software design based on descriptions of modules and their interconnections [3,9,15,16]. With this approach, a system is decomposed into independent modules. Each module is characterized by its realization of one design decision, which is hidden from all other modules.

In order to implement such a design methodology, tools are required so that the designer can naturally manage, express, and document these concepts. A new program design language and supporting processor are proposed as such a tool. The potential advantages of this system include:

\- With the aid of a program design language, the initial algorithmic design of the system can be established early in the development process [21]. The formal design strategy enforces a structure which will promote program reliability.

\- The language can be used in all stages of system development, at all levels of detail, except the final coding phase. This simplifies and clarifies the design process – modular decomposition allows for division of the problem into manageable subproblems; abstraction reduces the complexity of the specification, thereby increasing comprehensibility [19]. Detailed design can point out potential areas of implementation difficulty.

\- A formal communication medium among designers and implementators insures both the implementor's understanding of the designer's intentions and the agreement of two implementators about the interface between the modules [13,14]. Likelihood of ambiguity or incompleteness decrease significantly.
- Modification of modules in accordance with a change in system specifications is easier if there is a formal specification of the effects of each module and the interfaces among modules.

\- An accurate and complete documentation of the system can be provided, eliminating the need for conventional flowcharts [8]. Listings give precise records of each stage of the design, at an appropriate level of detail.

\- The resulting design strategy is independent of any particular language in which individual modules are to be programmed. Implementation considerations are irrelevant. The design language is suitable for topdown or bottom-up programming.

## 2. Background

Although the need for good specification technique is becoming widely recognized, relatively few good techniques are available [10].

HIPO (Hierarchy plus Input-Process-Output) [23] is a diagrammatic approach to functional specification and documentation of programs for use in the top-down design of systems. The techniques for decomposing systems into functional modules in a HIPO environment is discussed in [24], where a number of criteria for module definition are suggested. All levels of the system are described by functions: each function is designed using a HIPO diagram, in which inputs and outputs are listed and the processing is specified. A hierarchy chart illustrates the relationships between a function and its subfunctions. The diagrams used at each stage of system development serve as documentation. HIPO is often used in conjunction with a pseudo-code, or metacode.

Metacodes [25] are program design languages which have the overall syntax of a structured programming language but enable the programmer to express ideas in natural English. The logical solution to a problem and the overall program design can then be expressed in a precise but readable format, without the constraints imposed by more formal programming languages. The programs themselves serve as documentation for the completed system.

Module interconnection languages (MIL) enable programmers of large systems to express the overall program structure in a concise, precise, machine-checkable form [5]. All module interconnections are explicitly specified, allowing analysis of the flow of resources and binding of resource names and of the modules providing them. Possible and initial values of functions may be specified, parameters and effects of functions stated [14]. Information-hiding independent development of modules is encouraged [18]. Each function is built with a single module with a limited and well-defined interface. Alphard [26,27] and CLU [11] both provide constructn (form and cluster) for implementing data abstractions. Similar concepts, specialised for real-time systems, are described in [7]. Type checking and separate compilation of modules are features of these systems.

Much work has been done on the use of abstract data types to provide high-level data manipulation primitives to improve program quality. A study [12] comparing MILs and data-type abstraction mechanism concludes that programming-in-the-large can be accomplished by augmenting programming languages with abstract data types. This approach, however, exposes the complexity of the programming language used, and binds the implementation to that (or a similar) language early in the design process. Another way to accomplish a combination of specification language and programming language is typified by EUCLID [20] which has constructs for including specifications and assertions. Yet another approach [22] uses a high-level pseudolanguage as a standard basis for programming, together with a pre-processor which translates the pseudolanguage into a conventional language, such as FORTRAN or COBOL.

Some automated aids for design verification have been developed. DECA (Design Expression and Confirmation Aid) [2], used in conjunction with a top-down design methodology, provides syntax checking of input and local consistency checks. Similarly, DACC (Design Assertion Consistency Checker) [1] performs module interface consistency checking, detects inconsistencies in assertions, and provides a checklist of potential interface problems.

The language described in this paper combines characteristics of metacodes, module interconnection and specification languages with specific capabilities to describe applications involving shared data bases. As such, it is capable of being used as part of a data-dictionary/program library system, thus permitting documentation and description of both data and programs in a uniform environment.

The language, called Pseudo-code, supports the program development methodology of modular decomposition and stepwise refinement, where problems of high complexity are successively decomposed into subproblems of lesser complexity and lower levels of abstraction until the problems are of manageable size for coding. Pseudo-code provides a notation for the definition and description of the units of abstraction into which a problem solution is divided. It is possible to describe not only the function carried out by the unit, but also the interconnections among units; hence a complete view of the system is maintained. Pseudo-code is similar to a programming language, but is not designed to be compilable or machine-translatable into a compilable language. It is therefore not, in detail, bound by rigid syntactical rules. Hence it is easier to use: logic of the solutions can be expressed without the distractions of programming language requirements.

A Pseudo-code program stands alone as documentation; however, it may be analyzed by a processor which produces a formatted listing of the code and various reports on modules and their relationships, both to each other and to shared data.

The language was designed with the following objectives in mind:

\- The syntax must be simple, unambiguous, and provide a basic structure, while permitting unanalyzed free text.

\- Module interfaces must be formally defined.

\- Program logic and function should be expressible in a clear but informal manner.

\- The language should handle successive levels of detail, so that, at the more detailed levels, hand-translation to a conventional language is relatively straightforward.

\- Design decisions and their scopes of influence must be clearly and simply expressable, so that Pseudo-code programs and their explicit realization in actual code can easily be modified.

\- The programs should be self-documenting, and provide technical communications at all levels, while allowing controlled distribution of design information [13].

\- The language should support top-down, outside-in, inside-out, or bottom-up [17] programming methods.

## 2. The Language

The basic unit of abstraction of Pseudo-code is the module that performs a well-defined task in terms of the probability be solved. Within a module definition, communication with the outside world is defined in terms of a parameter list, a returned value list, data base or file manipulation, and source/sink data (for terminal I/O). The language is structured such that module interaction and resource usage are declared entirely separately from the algorithmic aspects of the module. Thus it is possible to use Pseudo-code as an MIL in the early of design.

The basic philosophy of Pseudo-code is that inter-module communication, resource usage, and algorithm structure can be specified in a syntax which is capable of being analysed and checked by a processor, and that natural language text be permitted within the syntactic structure. This allows high-level definition and explication of a module without requiring precise definition of each and every action carried out in the module. Principles of 'successive refinement may be employed to reduce natural language text to more precise definitions in terms of the Pseudo-code syntax and more precise and detailed natural language text. By using a mathematical or other well-defined language, a Pseudo-code module may be reduced to a precise and formal definition. However, this to some extent violates the philosophy of Pseudo-code, which is to provide a high-level and succinct module description. In actual practice, it is sufficient to refine the Pseudo-code module to the point where a competent programmer can unambiguously hand-translate the module description to a conventional programming language.

Program readability generally improves as the size of program modules decreases. A practical rule is that a module not exceed one page of code (about 50 lines). Good decomposition of the program into modules generally results if the following are considered:

\- Modules should reflect the division of the program into pieces that relate to each other in a hierarchy. A well-designed module carries out a single function or several functions that are closely related; it is easier to understand and verify, and if modification is necessary, there is less chance of disturbing portions of the program that do not change.

\- A well-designed module communicates with other program modules only in carefully controlled ways (expressed in the declaration part).

Consistent identification enhances readability of the finished program. The relationships among the statements are then exhibited pictorally; understanding and verification of the program are facilitated. Indentation of the program is automatic, using the formatter (see the Processor description).

Properly written, Pseudo-code programs should provide a good source of documentation for the final executable code. To reduce the need for documentation of logic, the code should follow certain guidelines of good programming practice. Data names and labels should be as indicative as possible of the functions of the data items and program elements, even if this tends to lengthen the names.

The sections which follow contain an informal description of the language. A precise description is contained in Appendix A.

## 2.1. Reserved Words and Identifiers

Since Pseudo-code allows arbitrary text in most constructs, it is necessary to define reserved words for syntactic and semantic constructs of the language. In order to encourage simplicity and clarity of design, as well as to enhance ease of use, the number of keywords and language constructs have been kept to a minimum.

The reserved words are normally written in upper case in the hand-written programs to emphasize their interpretation as single symbols with fixed meaning. The programmer may not use these words in a context other than that explicit in the definition of Pseudo-code, unless otherwise stated. In particular, reserved words must not be used as identifiers.

Identifiers are names denoting modules, records and data elements. They must begin with a letter, which may be followed by any combination and number of letters, digits and underscore, to a maximum length of 80 characters (or the end of the line). Certain identifiers, those of data base elements, would normally be predefined in a data dictionary. For obvious reasons, use of such names in any other context should be avoided. Data element names also are written in upper case in the hand-written programs.

Comments, delimited by “%” symbols, may be inserted between any two words, identifiers, or special symbols.

Where $\langle simple text\rangle$ appears in a syntax description text may appear containing any combination of allowable symbols except reserved words. Where $\langle text\rangle$ appears, reserved words may appear in the text. If the keyword is part of a logic construct, then the entire construct must be included.

## 2.2. General Structure

The basic unit of abstraction in Pseudo-code is a module. An application program consists of a suite of related modules. A module consists of three parts:

\- The module heading, which specifies the module name and (optionally) parameter lists;

\- a declaration section, which defines the interaction between the module and other resources;

\- a module body, which describes the algorithm to be performed by this module.

Only part a) is necessary. Parts b) and c) may be added as design progresses. Thus, the overall modular structure of a application may be defined initially, followed by successive refinement to add declarations and the module body. While any description declared as such can be a module, it is intended that a module should describe a well-defined task in terms of the overall problem to be solved.

## 2.3. Module Definition

Each module definition consists of four parts:

1. a heading;

2. a declaration part;

3. a body;

4. an ending.

The heading and ending define and delimit the module description. The declaration part describes communication with other modules and external devices. The body describes the logical solution to the task in question.

## 2.3.1. The Module Heading

Every module must commence with a heading. Its purpose is to identify the module uniquely, and to specify parameter values which are passed to and from the module.

The module heading takes one of the following forms:

MODULE (module name)

MODULE <module name> (<parameter list>)

MODULE < module name> RETURNS (<parameter list>)

MODULE <module name>(<parameter list>) RETURNS (<parameter list>)

The module name must be a valid identifier. It must be unique for all modules defined within a single program. It must not be either a reserved word or the name of a data base element.

An optional parameter list follows the module name. If used, the parameters should specify values to be passed to the module for use in the module. Return parameters are those whose values are determined within the module and passed back to the calling module. If present, they should be specified using the RETURNS option of the statement. Parameters must be valid identifiers; neither reserved words nor module names are permitted. Parameters must be separated by commas and enclosed in parentheses. No additional punctuation is permitted.

## 2.3.2. The Declaration Part

The declaration part (if it exists) immediately follows the module heading and precedes the module body. Its purpose is to:

\- specify the data which the module uses and describe its manner of usage;

\- allow expression of authorization for another module or person to use that module;

\- specify communication with other modules and external devices.

The order and syntax of statements in the declaration part must be strictly followed. Declarations are optional, but if included, must follow the order and format specified. No extraneous text is allowed.

A. Declaration Delimiters The declaration part starts with the keyword BEGINDECLAR. It is concluded by ENDDECLAR. These are the only compulsory statements of the declaration part.

B. Record Declarations. If included, a record declaration must immediately follow the BEGINDE-CLAR statement. A module may have any number of consecutive record declarations. A record declaration defines a logical record (association among data elements) which the module will use. A record definition consists of a record heading, an ordering specification and a use clause.

A record declaration must commence with a record heading. It takes the form:

RECORD <record name> (<list of data names>)

The record name may be any legal identifier. It is internal to the module and need not be unique. The data names should be in the data dictionary. The user should ensure that the association of data names implied by the record definition is meaningful.

Ordering Specification. The ordering specification states the order expected by the module for sequenced data structures. An ordering specification is mandatory for each record declaration. It takes one of the forms:

ORDERED ON ( $\langle$ list of data names $\rangle$ )

or

## UNORDERED

Usage Specification. It is assumed that any field specified in a record declaration will be accessed in the module body. If, in addition, an individual field or record is to be created, modified, or deleted, then each such usage must be explicitly defined (in that order).

The CREATED clause is used to specify that the named data are created by this module. The clause takes one of two forms:

CREATED ( $\langle$ list of data names $\rangle$ )

or

CREATED ALL

The MODIFIED clause is used to specify the data items which are changed by the module. It has the form:

## MODIFIED (list of data names)

The DELETE clause is used to specify deletion of the record. It has the form:

## DELETED

This specifies deletion of all fields of the record. It is not possible to specify deletion of individual fields.

C. AUTHORIZATION clause. This optional statement is used to specify the authority of another module or use to access the module currently being defined. It has the form:

AUTHORIZATION < simple text>

D. PRODUCES clause. This optional statement is used to specify any external (i.e. non-data-base or non-file) output of the module. It has the form:

## PRODUCES <simple text>

E. CONSUMES clause. This optional statement is used to specify any external input to the module. It has the form:

CONSUMES (simple text)

F. INVOKES clause. This optional statement is used to specify the modules invoked by the module currently being defined. It has the form:

INVOKES ( $\langle$ list of module names $\rangle$ )

Each module name listed should be defined in its own right, although declaration of a module need not precede its mention in another module.

## 2.3.3. The Module Body

The module body describes the algorithm of the module. The module body may contain any number of statements, including zero.

A structured programming style is encouraged in formulating the solution. Pseudo-code provides the three control logic structures characteristic of structured programs:

1. simple sequence of statements;

2. selection of statements;

3. iteration;

In addition to these logic structures, assignment, input-output, data base manipulation, and assertions may be explicitly expressed. Each statement has a definite and simple syntax. Control logic structures have explicit entry and exit points to discourage ambiguity.

Free text may be included at the user's discretion, the only restriction being the use of reserved words. Thus the user may include notation appropriate to the application in describing the actions to be performed.

A. Assignment. The SET statement is used to specify assignment. It has the form:

SET <simple text>

<simple text> is the description of the assignment to be made.

B. Control Logic Structures. Conditional Statements. In conditional statements, a choice among actions is based on a predicate expressed in simple text. The IF and the CASE statement are available in Pseudo-code.

The two forms for an IF statement are:

IF <simple text> THEN <text> ENDIF

and

IF <simple text> THEN <text> ELSE <text> ENDIF

The CASE statement describes a multiway branch. It has the form:

## CASE <simple text> OF <text> ENDCASE

<simple text> represents a selector condition; <text> consists of a list of actions. Statement labels are contained in <simple text>. Upon completion of the selected statement, control is considered to proceed to the statement following the ENDCASE statement.

Iterative Statements. Iterative statements specify repeated execution of code depending on a condition. Iterative control structures provided by Pseudo-code are the FOR, WHILE, and UNTIL loops. These may be nested.

The FOR statement is used to specify definite iteration. It has the form:

## FOR EACH <simple text> DO <text> ENDFOR

This construct is used to describe iteration based on counting or an uenumerated list.

The WHILE statement specifies iteration in which the condition expressed in (simple text) is evaluated before each iteration. It has the form:

## WHILE <simple text> DO <text> ENDWHILE

The UNTIL statement specifies evaluation of the condition described by $\langle$ simple text $\rangle$ at the completion of each iteration. Thus the body of the iteration described by $\langle$ text $\rangle$ is considered to be performed at least once. The UNTIL statement has the form:

## UNTIL <simple text> DO <text> ENDUNTIL

The ESCAPE statement indicates an unconditional transfer of control to the end of the particular construct in which it appears. It has the single keyword:

## ESCAPE

C. Input and Output. Input and output are specified by GET and PUT respectively. The forms of these statements are:

GET (simple text)

and

PUT <simple text>

These describe external transfer of data. The specific I/O devices (e.g. terminals, card readers) and any necessary format specifications, if known, should be given.

D. Data base manipulation. Four commands are provided for data base manipulation. They are designed for use with the logical records declared in the declaration.

The FIND statement is used to specify the location and retrieval of the record defined in <simple text>, which should pspecify the record and its identifying characteristics. The FIND statement has the form:

## FIND (simple text)

The CREATE statement is used to specify creation

of a new record instance. It has the form:

CREATE <simple text>

The record specified in this statement should be declared with the CREATED attribute in the record declaration. If specific fields were designated as CREATED, then only these fields need be specified.

The MODIFY statement is used to specify changes to an already existing record. It has the form:

## MODIFY <simple text>

<simple text> should identify the record name. Any fields of the record to be changed should be specified as MODIFIED in the record declaration.

The DELETE statement is used to specify the deletion of a record. It has the form:

## DELETE <simple text>

<simple text> should identify the name and characteristics of the record to be deleted. The record name should be specified as DELETED in the record declaration.

E. The ASSERT statement. This is used to specify assertions about the module. It has the form:

## ASSERT〈text〉ENDASSERT

Assertions may contain any text, including keywords, which need not have their usual meaning. All assertions are recorded for later examination by the processor.

F. The NULL statement. The NULL statement has the form:

NULL

## 2.3.4. The Module Ending

The module ending follows the module body. It has the form:

## ENMODULE <module name>

〈module name〉 must be identical to that declared in the heading.

## 3. The Processor

To assist in the development of large application systems, an experimental Pseudo-code processor has been developed. Output from this processor includes:

A formatted listing of the Pseudo-code program.

\- Detection of errors which occur in the formal expression of the Pseudo-code or the use of variables in an incorrect fashion.

A control and data flow analysis.

## The processor

\- performs syntactic and semantic checks, and issues appropriate error messages;

\- derives and stores in a symbol table information concerning data and control flow within and between modules;

generates a formatted listing of the program code, with automatic indenting of declarations and module body logic, thus presenting a clear, explicit representation of the logical structure of the program;

produces from the symbol table various analytical reports on module and data interrelationships.

## 3.1. Structure of the Processor

The processor has the general structure of a language compiler. It differs from a compiler in that the symbol table records more information than is necessary for a conventional compiler, and in that no code generation routines exist. The processor has two sections. In the first section, the Pseudo-code is read and processed. A syntactic and semantic check is performed, the symbol table constructed, and a formatted listing of the program including error messages is produced. In the second section, the symbol table is analysed and various reports on program control and data flow are generated.

## 3.2. Scanner and Parser

The scanner and parser are of conventional design. The syntax is checked in accordance with the definition of Pseudo-code. Any deviation from the required syntax results in generation of an error message in the formatted program listing at the location of the error.

## 3.3. The Format

The formatter is responsible for producing a listing of the Pseudo-code. Formatting is applied according to the following rules:

\- Initial blanks of each input line are ignored; extra-neous blanks at the end of a line are ignored; internal blanks are preserved.

\- A new line is started for each new line of input text; therefore, every line of input text has at least one corresponding line of output text (except for blank lines)

\- Detection of certain reserved words forces start of a new line (unless part of a comment or assertion). This is to implement formatting of control structures.

Automatic indenting is accomplished by indenting each output line according to the current indentation value (indicated by current-indent and temp-indent). These values are modified during parsing of the pseudo-code, according to the construct being parsed.

The following conventions have been established for the use of identations:

\- The basic unit of indentation is 3 spaces.

\- Keywords delimiting the same construct are vertically aligned. Subordinate structures are indented a further 3 spaces. Statements controlled by a control logic structure are indented to make the scope of influence obvious.

\- Whenever an output line exceeds the space allowed by the indentation requirement, the excess text is printed on the next line.

## 3.4. The Symbol Table

The symbol table records all pertinent data flow as diagnosed in the processing of the Pseudo-code. An entry is made in the symbol table for each module or data element which appears in the module definitions. Internal to the processor, modules and data elements are given unique identification numbers which are assigned sequentially (commencing with 1).

The identifier represented by the entry is characterized by its type. Each identifier is classified as a data element, a declared module, or an undeclared module. An undeclared module is one which has appeared in an INVOKES clause during definition of another module, but which has not yet been defined.

Data declarations in Pseudo-code define data objects and declare an association between data objects and a module. In the symbol table, the data-use field of a module description entry contains an index into an array containing the identification numbers and data usage characteristics of the data objects declared in the module. Similarly, the data-use field of a data element description entry contains an index into the name array, the referenced element of which contains the numbers of the modules in which this data element is declared.

Module invocation relationships are recorded by reference to an array which contains the module numbers related by invocation to the module. The symbol table for each module contains a reference to an element of this array to record modules invoked by this module, and another reference to the array to record modules invoking it. Reserved word usage by modules is recorded similarly.

## 3.5. Error Detection and Recovery

An error message generation procedure is invoked whenever a systax error is detected, or on incorrect use of a variable.

Error recovery procedures vary according to the type and location of the error. Processing of the code always continues; an attempt is made to allow as little error propagation as possible. Generally the symbol in question is ignored, but parsing will usually continue correctly at the end of the logical construct in which the error occurs.

No attempt is made to correct errors.

## 3.6. Report Generator

The information stored in the symbol table is accessed and decoded (if necessary) and output for the user. Current features of the report generator include:

\- An alphabetical listing of all declared modules. A module that has been referenced but not defined is so indicated.

— An alphabetical listing of data elements.

\- A list of modules, and those that invoke them.

\- A list of data elements and, for each, the modules in which they were declared and their manner of usage.

\- A list of assertions in the program.

More information may be derived from the symbol table, including:

\- For each module, the module it calls.

\- For each module, the reserved words it uses.

\- For each module, the data elements it uses and the manner of usage.

\- For each reserved word, the modules that use it.

-- Modules and data elements could also be output in order of appearance.

## 4. Results

As a test of Pseudo-code, the Pseudo-code processor was designed using the language. A total of 41 modules (approximately 700 lines of Pseudo-code) was written. This was hand-translated into 3200 lines of PL/I (including about 600 lines of comments). The module definitions were then used to test the processor. Several results are of interest:

\- The Pseudo-code is much easier to read and understand than the equivalent PL/I code, because there are fewer lines and because all details of data structure and housekeeping are absent.

\- A Pseudo-code module is easily hand-translatable into PL/I.

\- There were few errors of design. Most errors were the result of PL/I peculiarities.

\- The processor is well documented by its Pseudo-code.

## 5. Programming Examples

Two examples of modules written in Pseudo-code are included to illustrate its use. These are in no way meant to relate to one another; each would only be a part of their respective programs. Two examples are given in Figs. 1 and 2.

The second example is one of the modules of the processor. It analyses the usage characteristics of declared data.

<table><tr><td>MODULE summarize_sales RETURNS (DEPT_TOTAL)BEGINDECLARRECORD sales_data (DISTRICT_NO,MAN_NO,MAN_TOTAL)ORDERED ON (DISTRICT_NO,MAN_NO)RECORD sales_total (DISTRICT_NO, TOTAL)ORDERED ON (DISTRICT_NO)MODIFIED (TOTAL)ENDDECLAROpen filesSET tot&gt;1 for all districts to zero.FOR EACH sales_data DOSET district_total to zero.FOR EACH sales_man DOAdd MAN_TOTAL to district_total.ENDFORMOIFY sales_total making TOTAL = district_total.Add district_total to total % for all districts %ENDFORSET dept_total = total % for all districts %Close filesENDMODULE summarize_sales</td><td>MODULE check_useBEGINDECLARINVOKES (get_a_symbol,generate_error)ENDECLAR% check for create %IF symbol is reserved word %CREATED%THENget_a_symbolIF symbol is % ALL %THEN% record all data created %get_&#x27;symbolELSEprocess_listFOR EACH data base element DO%check that it is in record declaration %IF soTHENSET use to %create%ENDIFENDIFENDIFIF symbol is %MODIFIED%THENprocess_listFOR EACH data base element DOcheck that its in %record% declarationIF soTHENSET use to % modify %ENDIFget_a_symbolENDIFENDIF symbol is %DELETED%THENFOR EACH data element DOSET use to %deleted%ENDIFFOR EACH data element declared DO%mark data usage%ENDIF Emeraldodule check_use</td></tr><tr><td colspan="2">Fig. 1. Example 1.</td></tr></table>

Fig. 2. Example 2.

```txt
<program specification> ::= 
    <module specification> {<module specification>}
<module specification> ::= <module heading>
    <module declaration>
    <module body>
    <module ending>

<module heading> ::= MODULE <module name>
    | MODULE <module name> (<param> {,<param>})
    | MODULE <module name> RETURNS (<param> {,<param>})
    | MODULE <module name> (<param> {,<param>})
    | MODULE <module name> (RETURNs (<param> {,<param>})

<module declaration> ::= BEGINDECLAR
    <record definitions>
    <authorization: part>
    <production part>
    <consumption part>
    <invocation part>
    ENDDECLAR

<record definitions> ::= <empty>
    | <record definition> {<record definition>}

<record definition> ::= <record heading>
    <ordering clause>
    <use specification>

<record heading> ::= RECORD <record name>
    (<data name> {,<data name>})

<ordering clause> ::= ORDERED ON (<data name> {,<data name>})
    | UNORDERED

<use specification> ::= <created clause> <modified clause>
    <deleted clause>

<created clause> ::= <empty>
    | CREATED (<data name> {,<data name>})
    | CREATED ALL

(modified clause> ::= <empty>
    | MODIFIED (<data name> {,<data name>})

<deleted clause> ::= <empty> | DELETED

<authorization part> ::= <empty> | AUTHORIZATION <simple text>

<production part> ::= <empty>
    | PRODUCES <simple text>

<consumption part> ::= <empty>
    | CONSUMES <simple text>

<invocation part> ::= <empty>
    | INVOKES (<module name> {,<module name>})
```

```txt
<module body> ::= <empty> | <statement> {<statement>}
<statement> ::= <conditional> | <iteration>
    <escape clause> | <case statement>
    <data-base manipulation> | <assignment>
    <I/O statement> | <assertion>
    <simple text>

<conditional> ::= IF <simple text> THEN <text> ENDIF
    | IF <simple text> THEN <text> ELSE <text> ENDIF
<iteration> ::= <for loop> | <while loop> | <until loop>
<for loop> ::= FOR EACH <simple text> DO <text> ENDFOR
<while loop> ::= WHILE <simple text> DO <text> ENDWHILE
<until loop> ::= UNTIL <simple text> DO <text> ENDUNTIL
<escape clause> ::= ESCAPE

<case statement> ::= CASE <simple text> OF <text> ENDCASE
<data-base manipulation> ::= FIND <simple text>
    CREATE <simple text>
    MODIFY <simple text>
    DELETE <simple text>

<assignment> ::= SET <simple text>

<I/O statement> ::= PUT <simple text> | GET <simple text>

<assertion> ::= ASSERT <text> ENDASSERT

<module ending> ::= ENDMODULE <module name>

<simple text> ::= <any sequence of symbols not containing a reserved word>

<text> ::= <any sequence of symbols>

<module name> ::= <identifier>

<record name> ::= <identifier>

<data name> ::= <identifier>

<param> ::= <identifier>

<empty> ::= NULL
```

## References

[1] B.W. Boehm, R.K. McClean, D.B. Urfrig, "Some Expe-

rience with Automated Aids to the Design of Large-Scale Reliable Software:. IEEE Transactions on Software Engineering, Vol SE-1, No 1 (March 27,5).

[2] L.C. Carpenter, L.L. Trip, "Software Design Validation Tool". Proceedings of International Conference on Reliable Software. SIGPLAN Notices, Vol. 10, No 6

(June 1975).

[3] J.L. Cheval, F. Cristian, S. Krakowiak, Montuelle, J., & Mossiere, J., "An Experiment in Modular Program Design". Information Processing 77 Proceedings of IFIP Congress 77. New York: North-Holland Publishing Company, 1977.

[4] Y. Chu, "A Methodology for Software Engineering". IEEE Transactions on Software Engineering", Vol. SE-1, No 3 (September 1975).

[5] F. DeRemer, H. Kron, "Programming-in-the-Large Versus Programming-in-the-Small". Proceedings of International Conference on Reliable Software, 1975. SIGPLAN Notices, Vol 10, No 6 (June 1975).

[6] E.W. Dijkstra, "Notes on Structured Programming", Structured Programming, Dahl, Dijkstra, and Hoare. London: Academic Press, 1972.

[7] K. Jackson, "Language Design for Modular Software Construction". Information Processing 77 Proceedings of IFIP Congress 77. New York: North Holland Publishing Company, 1977.

[8] E.A. Jordan, "A Support for Program Design With Abstract Machines". Information Processing 77 Proceedings of IFIP Congress 77. New York: North-Holland Publishing Company 1977.

[9] B.H. Liskov, "A Design Methodology for Reliable Software Systems". Proceedings of the AFIPS 1972 FJCC, Vol 41 (1972).

[10] B.H. Liskov, S. Zilles, "Specification Techniques for Data Abstractions". Proceedings of International Conferences on Reliable Software, 1975. SIGPLAN Notices, Vol 10, No 6 (June 1975).

[11] B. Liskov, A. Snyder, R. Atkinson, C. Schaffert, "Abstraction Mechanisms in CLU". CACM, Voc 20, No 8 (August 1977).

[12] T.P. Martin, "Programming-in-the-Large With Abstract Data Types. A Case Study and Comparison of Two Aids to the Design of Software Systems". M.Sc. Thesis, Department of Computing and Information Science, Queen's University, Kingston, Ontario, Canada. August 1977.

[13] D.L. Parnas, "Information Distribution Aspects of Design Methodology". Proceedings of the IFI $^{P}$ Congress. Booklet TA-3, 26–30, August 1971.

[14] D.L. Parnas, "A Technique for Software Module Speci-

fication With Examples" Comm. ACM, Vol 15, No 12 (May 1972).

[15] D.L. Parnas, "On the Criteria to be Used in Decomposing Systems Into Modules". Comm. ACM, Vol 15 No 12 (December 1972).

[16] D.L. Parnan, "The Influence of Software Structure on Reliability". Proceedings of International Conference on Reliability Software. SIGPLAN Notices, Vol 10, No 6 (June 1975).

[17] D.L. Parnas, "Use of Concept of Transparency in the Design of Hierarchically Structured Systems" Comm. ACM, Vol. 18, No 7 (July 1975).

[18] D.L. Parnas, "On the Design and Development of Program Families". IEEE Transactions on Software Engineering, Vol Se-2, No 1 (March 1976).

[19] D.L. Parnas, "The Use of Precise Specifications in the Development of Software". Information Processing 77 Proceedings of IFIP Congress 77. New York: North-Holland Publishing Company, 1977.

[20] G.J. Popek, J.J. Horning, B.W. Lampson, J.G. Mitchell, London, R.1. "Notes on the Design of Euclid". SIGPLAN Notices, Vol 9 No 4 (April 1974).

[21] D.J. Reifer, "Automated Aids for Reliable Software". Proceedings of International Conference on Reliable Software. SIGPLAN Notices, Vol 10, No 6 (June 1975).

[22] S. Shinozawa, H. Ikeda, A. Nakashima, and M. Watanabe, "Pseudo-Languages and Their Pre-Processors". Information Processing 77 Proceedings of II-IP Congress 77. New York: North-Holland Publishing Company, 1977.

[23] J.F. Stay, "HIPO and Integrated Program Design". IBM Systems Journal Vol 15, No 2 (1976).

[24] W.P. Stevens, G.J. Myers, L.L. Constantine, "Structured Design". IBM Systems Journal Vol 13 No 2 (1974).

[25] P. Van Leer, "Top-down Development Using a Program Design Language". IBM Systems Journal Vol 15 No 2 (1976).

[26] W.A. Wulf, R.L. London, M. Shaw, "An Introduction to the Construction and Verification of Alphard Programs". IEEE Transactions on Software Engineering, Vol SE-2, No 4 (December: 1976).

[27] W.A. Wulf, R.L. London, M. Shaw, "Abstraction and Verification in Alphard: A Symbol Table Example". Department of Computer Science, Carnegie-Mellon University. December 1976.
