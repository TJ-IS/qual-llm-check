---
otero_id: 26664
otero_key: "EURPGQ77"
title: "Formal Modeling of Complex Commands in Industrial Software Specifications"
authors: "Michael V. Mannino; Sukumar Rathnam; In Jun Choi; Veronica Tseng"
year: "1994"
journal: "Information Systems Research"
doi: "10.1287/isre.5.3.249"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

![](/api/attachments/EURPGQ77/fulltext/images/f24b66ff32d8d572094eac3064e7896893446eea0c0b5a7b83ab9ba354c2d668.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Formal Modeling of Complex Commands in Industrial Software Specifications

Michael V. Mannino, Sukumar Rathnam, In Jun Choi, Veronica Tseng,

## To cite this article:

Michael V. Mannino, Sukumar Rathnam, In Jun Choi, Veronica Tseng, (1994) Formal Modeling of Complex Commands in Industrial Software Specifications. Information Systems Research 5(3):249-274. https://doi.org/10.1287/isre.5.3.249

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1994 INFORMS

Please scroll down for article—it is on subsequent pages

## informs.

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Formal Modeling of Complex Commands in Industrial Software Specifications

Michael V. Mannino

Department of Management Science, DJ-10

University of Washington

Sukumar Rathnam

Seattle, Washington 98195

Scopus Technology

1900 Powell Drive

Suite 900

In Jun Choi

Emeryville, California 95608

Department of Industrial Engineering

Pohang Institute of Science and Technology

P.O. Box 125

Veronica Tseng

Pohang 790-600, Korea

IBM Corporation

472 Wheelers Farms Road

Mail Drop 61

Milford, Connecticut 06460

We present a formal approach for modeling complex commands characterized by heavy overloading of function, large numbers of parameters, dependencies among parameters, subtle side effects, and lack of abstraction. Complex commands arise in a variety of business settings such as requesting a brokerage order, enrolling in a course, and specifying a product order. In addition, complex commands are also prevalent where specification of commands is strictly separated from multiple, independent implementations as in open software standards.

Our approach is based on an inheritance structure known as a command lattice. Like other forms of inheritance, command lattices support incremental definition and abbreviation of specifications. Because a complete command lattice can have a large number of specifications, we develop another structure known as a minimal command tree in which a command lattice is derived from a much smaller number of independent specifications. To map from a minimal command tree to a command lattice, we present algorithms that materialize an arbitrary node of a command lattice and compactly generate the behavior of a command lattice. To demonstrate the potential of command lattices, we have implemented a set of tools that provide convenient specification and powerful reasoning capabilities. Our tool collection includes the Command Specification Language that supports a precise and rich specification of the structural and behavioral properties of commands, the

Mannino • Rathnam • Choi • Tseng

incremental definition tool that ensures consistency of command lattices, the browsing tool that displays a command's inheritance structure, the type checker that ensures structural consistency of commands in expressions, and the target system tracer that simulates a sequence of command executions. We discuss our experiences applying the tools to IBM's Distributed Data Management, a large scale specification of data access on remote and heterogeneous IBM systems.

Assertions—Inheritance—Formal methods—Abstraction

It is our position that a solid product consists of a triple: a program, a functional specification, and a proof.

Edsger Dijkstra Austin, Texas 09/04/89

## 1. Introduction

oftware specifications increasingly use formal methods due to economic factors Daffecting the software development process. Formal methods are mathematically based techniques for describing system properties and supporting the verification and testing of software (Wing 1990). They help in revealing ambiguities, exposing errors, and communicating complex ideas as well as in proving the correctness of system properties. There is a belief that proper application of formal methods can lower software development costs. The main reason for this belief is that the cost to find and correct an error increases more than linearly throughout the development process. Thus, the added effort to apply formal methods early in the development process can be offset by savings in programming, testing, and maintenance. Recent reports such as about IBM's CICS (Nix and Collins 1988), the CASE project of Praxis Systems (Hall 1990), and the Portable Common Tools Environment (Middleburg 1989) provide anecdotal evidence of the increasing role of formal methods.

In addition to formal methods, various forms of abstraction have been proposed to reduce software development costs. Control of the mass of details in large software projects motivates most abstraction techniques. Inheritance is an abstraction technique widely promoted to improve the reusability of software. Inheritance permits incremental definition and abbreviation of specifications. One defines general units of software (i.e., classes) and then systematically refines the general classes into more specific classes. Details of the more specific. classes need not be repeated but are included by the inheritance mechanism. Inheritance can be combined with formal methods so that their joint benefits can be realized to reduce software costs. For example, the Eiffel software development environment (Meyer 1988), tightly integrates inheritance and formal methods to improve the reusability and correctness of software.

In this paper, we propose an inheritance structure and formal methods for commands. A command is a procedure that receives input, produces output, and changes the state of a system. Some commands can be rather complex with many possible combinations of inputs, outputs, and side effects. One reason for complex commands is the tradeoff between the number of commands and their complexity. A small number of commands reduce the user's cost to find the appropriate command. One way to reduce the number of commands is to increase the complexity of some commands. However, complex commands can be difficult to specify and understand. Our concern here is primarily with architects who write command specifications and implementors who code the specifications rather than end users. Examples of complex commands are requesting a brokerage order, enrolling in a course, and specifying a product order. For example, the complex nature of a brokerage order derives from factors such as different kinds of securities, customer types, and actions. A good interface can hide the complicating factors from an end user, but architects and implementors need tools to manage the complexity. Complex commands are also common where specification of commands is strictly separated from multiple, independent implementations as in open software standards. In today's multi-vendor computing market, open standards are heavily emphasized.

Despite their importance and complexity, commands are often specified imprecisely. Informal text is typically the only description of a command's behavior and dependencies among parameters. The text can be long and complex without any abstractions to manage the details. (An examination of the text found in a large scale system—the help system in UNIX—also reveals all of these problems.) Since specifications are typically informal, there are no forms of automated reasoning to analyze their consistency and completeness.

To address the limitations of informal modeling of commands, we have developed a formal approach to modeling and reasoning about commands based upon an inheritance structure known as a command lattice. A command lattice represents a complex command as a collection of behaviors grouped into an inheritance network defined by inclusion among associated sets of parameters. Because a command lattice can contain many behavioral specifications, it is a virtual structure derived from another structure known as a minimal command tree. A minimal command tree is an inheritance structure where only independent behavioral specifications are provided. To map from a command tree to a command lattice, we have developed algorithms to materialize an arbitrary node of a command lattice and compactly generate the behavior of a command lattice.

To demonstrate the potential of command lattices, we have implemented a set of tools that provide convenient specification and powerful reasoning capabilities. The Command Specification Language supports a precise specification of the structural (input and output) and behavioral properties (state description, constraints, and changes) of commands. The incremental definition tool ensures that a consistent command lattice can be generated from a minimal command tree. The browsing tool materializes any node in a command lattice and displays its chain of inheritance. The type checker ensures that commands are structurally well formed when used in expressions. The target system tracer simulates command executions by checking the satisfiability of pre-conditions and asserting post-conditions. For both the type checker and target system tracer, a command's inputs can match any node in a command lattice.

The last two tools, the type checker and target system tracer, are examples of automated reasoning tools. Software tools based on automated reasoning contribute to increased quality, productivity, and understandability of a specification. The goal of automated reasoning is to derive inferences about a specification. These inferences can involve long and subtle chains of reasoning. Reasoning methods are deductive (from facts and axioms to conclusions), inductive (from examples to conclusions), and simulative (imitative representation of one function by another). Automated reasoning transforms the role of specification tools from merely representation to aiding problem solving.

The rest of this paper is organized as follows. Section 2 reviews related research on formal methods in software development. Section 3 discusses the nature of commands in large scale specifications and presents a representative example of a command using the Command Specification Language. Section 4 formally defines the command lattice and minimal command tree along with mapping algorithms. Section 5 presents our tool collection including the incremental definition and browsing tools, the type checker, and the target system tracer. Section 6 discusses our experience with implementing our tools and applying them to IBM's Distributed Data Management, a large scale industrial specification about data access on remote and heterogeneous IBM systems. Section 7 summarizes the work and discusses future research directions.

## 2. Background and Related Work

In this section, we review research on formal methods in software development. We begin with a general discussion of command modeling and then summarize research on formal methods used in command modeling including specification languages and type inference.

Command modeling is a part of process modeling (Curtis, Kellner, and Over 1992). Process modeling involves the functional (input-output flows), informational (entities manipulated), behavioral (when and how performed), and organizational (who and where performed) perspectives of both manual and automated procedures. Command modeling focuses on the functional and informational perspectives, and partially on the behavioral perspective of automated procedures. Jacob (1983) describes a number of properties for modeling automated procedures:

• The specification of the command should be easy to understand. In particular, it must be easier to understand and take less effort to produce than the software that implements it.

• The specification should be precise. It should leave no doubt as to the behavior of the system for each possible combination of parameters.

• It should be easy to check for consistency.

• The technique should be powerful enough to express nontrivial system behavior with a minimum of complexity.

• It should separate what the system does (function) from how it does it (implementation). The technique should support specification of the behavior of a command without constraining its implementation.

• The specification should directly yield a reasonable table of contents for a user manual. but not necessarily the material in the manual.

Floyd. Hoare, and Diikstra made the initial breakthrough in formal, declarative specifications by developing the concepts of Hoare triples and axiomatic semantics (Dijkstra 1976). The Floyd-Hoare-Dijkstra model (which we adapt for our study) formally describes the behavioral properties of commands in terms of a Hoare triplet P{S}O): if the pre-condition P holds in the current state of the system then the post-condition Q holds in the post state after command execution given successful command termination.¹ Hence, pre- and post-conditions can be described as wellformed formulae and commands as predicate transformers on pre- and post-conditions. Jacob (1983) describes the chief value of this formal specification methodology as:

It permits a designer of large and complex systems to describe the external behavior of the system without having to specify its internal implementation.

In practical terms, post-conditions declaratively describe assertions about the values that the relevant variables will take after execution of the command. These assertions will not ascribe particular values to each variable, but will rather specify certain general properties of the values and the relationships holding between them (Hoare 1969). Hence, formalizing command specifications emphasizes the expression and manipulation of the results of computational processes and the objects on which they are performed, rather than instructions for performing them (Winograd 1979). This allows an automated reasoning tool to infer properties about command descriptions (Hoare et al. 1987).

In practice, application of a formal method (like Hoare logic) requires a specification language and a collection of automated reasoning tools to define and analyze specifications. Wing (1990) classifies specification languages as model-oriented versus property-oriented. Model-oriented languages feature a small set of mathematical structures such as tuples, relations, and sets to directly describe a system's behavior. Property-oriented languages feature axioms to indirectly describe properties that a system must satisfy. Axioms can be used to describe both state dependent and state independent properties of a system. In practice, most specification languages feature both mathematical structures and axioms but emphasize only one. VDM (Jones 1986) and Z (Spivey 1988) are considered model-oriented languages because they emphasize sets and functions and do not support state independent axioms. Larch (Guttag, Horning, and Wing 1985) is considered a property-oriented language because it emphasizes state independent axioms. The Command Specification Language (CSL) described in §3 is a model-oriented language because it emphasizes the mathematical structures and does not support state independent axioms.

Software tools associated with a specification language include the usual syntactic analysis as well as simulation and proof checking tools. Simulation tools make a specification executable. Users can obtain immediate feedback about the meaning of a specification by executing and tracing its effects. Proof checking tools ensure that certain axioms hold in a specification and provide useful inferential information. Statemate (Harel 1988) is an example of a simulation tool for state transition diagrams, while the Larch prover (Garland and Guttag 1989) and the verifier for the Adaptable Database Programming Language (Sheard and Stemple 1989) are examples of proof checking tools. In §5, we describe the type checker (TC), a proof checking tool, and the target system tracer (TST) a simulation tool.

'Similarly, if a system or mechanism is denoted by S and the desired post-condition by R, then we denote the corresponding weakest pre-condition by wp(S, R). If the initial state satisfies wp(S, R), the mechanism is certain to establish the eventual truth of R. Because wp(S, R) is the weakest pre-condition, we also know that if the weakest pre-condition does not satisfy wp(S, R), this guarantee cannot be given (Dijkstra 1976). Hence, if (P{S}Q> can be proved then the familiar logical symbol for theoremhood -P{S}Q can be used (Hoare 1969).

Our work on command specification has also been heavily influenced by research on type inference and polymorphism in object-oriented systems (Cardelli and Wegner 1985). A type inference system ensures that expressions are “well-typed" before they are executed. "Well-typed" means that the sets of values (or types) used in expressions are guaranteed to be compatible. In other words, a type inference system will not permit illegal operations such as the addition of an integer and a string. Further, a type inference system can deduce the type of an expression, thus alleviating the user from specifying the type information. The use of type variables and subset conditions among type variables makes the type inference system flexible because only the most general type is determined at compile time. The actual type at execution time is guaranteed to be a substitution instance of the most general type. We have applied these general results on type inference in the design of the Command Specification Language and the type checker.

Polymorphism permits an operator to accept different kinds of arguments and respond based on the kinds of arguments received. Commands are polymorphic as they can accept different combinations of parameters. Object-oriented programming is characterized by universal polymorphism where there is one implementation of an operator for all objects and ad-hoc polymorphism where there are multiple implementations of an operator (Cardelli and Wegner 1985). Command lattices extend a form of ad-hoc polymorphism known as incremental overloading (Choi, Mannino, and Tseng 1991) that permits related implementations of an operator to be shared. However, in commands, behavioral specifications rather than implementations are shared.

Command lattices are also an extension of transaction specialization as described by Borgida, Mylopoulos, and Wong (1984). They permit transactions to be specialized by their arguments and pre-conditions. Command lattices extend their ideas through an explicit notion of a lattice, multiple inheritance of conditions, more general dependencies among parameters, and an executable model to simulate command execution.

## 3. Command Modeling Environment

In this section, we discuss the assumptions of our modeling environment and present the Command Specification Language (CSL) as a formalization of this environment. We begin with a discussion of command specification in an object-oriented environment, describe the components of the CSL with a simple example, and finish with a brief discussion of the benefits of our formal versus informal modeling approach.

## 3.1. Assumptions

We assume an object-oriented environment with classes and commands. A class is a collection of similarly structured objects. Using inheritance, classes can be organized by their similarities and differences. Commands are imperatives that change the state of one or more obiects. Commands are polymorphic because they can accept different combinations of parameters but not encapsulated. The last point means that a command is not necessarily associated with a single class. We do not preclude the existence of encapsulated methods as in traditional object-oriented environments but our approach emphasizes modeling of commands. In other work, commands are known as transactions (Borgida, Mylopolous, and Wong 1984) or activities (Yasdi 1991).

A command accepts arguments, causes state changes, and returns output. Thus, a command specification contains both behavioral and structural descriptions. The behavioral description expresses constraints on the pre- and post-states of the command's environment. The structural description expresses what kind of argument values a command can take and what kind of results it returns.

Complexity in commands is largely caused by overloaded behavior. Overloading means that the outputs and state changes of a command are dependent upon the combination of parameters and their values. A command may have a large number of parameters, but only a small number are always required. The other (optional) parameters are necessary depending upon the context of the command. At first, overloading may seem as a negative practice, but it reduces the number of command names that are visible to an end user. A good interface can hide the overloading complexities to users, but architects and implementors must understand the specifications of overloaded commands. As an example, consider a command to enroll a student in a course. The inputs, outputs, and logic of enrollment depend on the rank of a student (undergraduate versus graduate), type of course, status (full versus part time), and so on. Enrollment is presented to users as a single command, but its behavior is heavily overloaded.

Three groups require a shared understanding of commands. Architects provide the structural and behavioral specifications. Implementors code the commands to execute in a given environment. End users issue commands as part of an application. Our focus is to support architects and implementors. End users do not normally see the same specifications as architects and implementors. It is possible, however, that end user specifications could be at least partially generated from the specifications used by architects and implementors.

Informal specifications in such an environment have a number of limitations. First, behavioral properties are informally (and therefore imprecisely) specified in detailed text. Second, there are no abstraction techniques such as inheritance to aid in the comprehension of commands. Commands must be specified and browsed in entirety. Abstraction techniques should permit incremental specification and browsing, beginning with the most essential details and gradually adding nonessential details as desired. Third, there is no declarative, executable specification. A declarative specification expresses the relationships between the initial state, parameters, final state, and outputs in a process independent manner (Winograd 1979). Execution of a specification relates the state of a system to the details of command specification Fourth, the command specification should be strongly typed and support inference of type information. Strong typing and type inference are foundations of formal specification because they promote succinct, precise, and flexible specifications.

## 3.2. Command Specification Language

The Command Specification Language (CSL) is a formalism for the previously described command modeling environment. Sentences in the CSL² are divided into two categories: type expressions for the structural properties of commands and classes and pre- and post-conditions for the behavioral properties. Type expressions are formed from basic types, structured types, type variables, and Boolean conditions on type variables. The structured types include labeled records denoted by ‘’ to

Mannino • Rathnam • Choi • Tseng

```txt
enroll :: t1 → (success::t2 + failure::t3)
RESTRICTED_BY t1 ≤ (stdno::STRING * cno::STRING)
AND t1 ≥ (stdno::STRING * cno::STRING *
    gradelevel::STRING * credits::INT *
    permission::(ovrld::OVERLOAD + splstd::SPLSTUDENT))
AND t2 = (number_enrolled::INT)
AND t3 = (cause_of_failure::STRING)
```  
FIGURE 1. CSL Type Expression for enrol1.

represent classes, labeled unions denoted by ‘+’ to represent mutually exclusive types, function types denoted by →’ to represent commands, and lists denoted by f l’ to represent collections. Type variables and Boolean conditions on type variables specify relationships among required and optional command parameters. Commands are polymorphic because they can accept different combinations of parameters.

Figure 1 displays the CSL type expression for the command enrol1. In the first line, the type expression indicates that enro11 (adapted from Borgida, Mylopoulos, and Wong 1984) is a polymorphic function with type variables t1 through t3. In the second line, the subtype condition (≤)³ on type variable t1 indicates that the command input must contain the arguments stdno and cno. Note that the type of the output is a labeled union (denoted by the + symbol) indicating that either a successful execution or failure is generated. In the third line, the supertype condition on t1 (≥) indicates that the input can optionally contain other arguments for grade level (credit/nocredit or audit), credits, and permission for enrolling in overloaded courses and certain restricted courses. Note that permission is also a labeled union indicating that either an overload or a special student permission is required. Overloads are used for obtaining enrollment in a course whose size exceeds the limit, while special student permission is used for enrolling in courses restricted to a certain major.

The CSI, permits more dependencies among parameters than merely whether a parameter is required or optional. For example in the enrollment of a student, if the command contains a nationality parameter, then it must also contain a visa status parameter. This dependency is indicated in Figure 2 by the IF-THEN constraint where the type variable t1 must contain the parameter visa if it contains the parameter nationality.

The CSI, can also be used to model classes as labeled record types with a label for each instance variable of a class. For example, the type identifiers STuDENT and couRSE from Figure 1 along with other classes of interest are shown as labeled records in Figure 3. Note that the square brackets indicate a list of the enclosed type of objects. For example, the type of taking\_courses is a list of course numbers.

Behavioral properties of commands are modeled by pre- and post-conditions. A condition is a named Boolean formula with identifiers, comparison predicates, and simple functions to manipulate lists, labeled records, and labeled unions. List functions include construction denoted by ‘:’, tail denoted by ‘TL’, and head denoted by 'HD'. Identifiers differ by their scope of change: either local or global. Changes to global identifiers, denoted by NEw, persist to the execution of other commands, while changes to local identifiers do not persist after command execution.

![](/api/attachments/EURPGQ77/fulltext/images/5de93f64c8435aae4df52a59c699da3f1a6152d22f08c7b08071e290fe692275.jpg)  
FIGURE 2. Conditional Type Expression for enrol1.

Figure 4 lists pre- and post-conditions of the enro11 command. The list of global identifiers precedes the pre- and post-conditions. Here, there are three global identifiers for the student, course, and enrollment to update. A colon (:) separates a condition name from its associated expression. The first two pre-conditions state that there must exist a student and course with matching student and course numbers, respectively. The pre-condition NOT - FULL states that the course size must be less that the course limit. The pre-condition NOT - TAKEN - BEFORE states that the course taken by the student should not include the new course. The post-conditions assert new values for the global identifiers. The LRREPLACE function changes the value of a component of a labeled record. The UPDATE- REGISTRATION condition replaces the label taking\_course by prepending the course to the existing set of course numbers. UPDATE- ENROLLMENT operates similarly for the list of students associated with a course. The post-condition, INC-CouNT, increments the number of students enrolled for the course. The final post-condition (NEW- ENROLLMENT) creates a new enrollment record with values for the specified attributes.

An important aspect of modeling commands with a formal language is that dependencies among commands are stated declaratively through pre- and post-conditions. A dependency exists when a pre-condition can be satisfied by post-conditions of another command. For example, it is possible to express the constraint that a grade can be assigned if a student is enrolled or the constraint that a credit can be issued if a check has cleared. The target system tracer, discussed in §5, highlights this kind of dependency by demonstrating how sequences of commands interact.

![](/api/attachments/EURPGQ77/fulltext/images/a19803317b15dfb7c3479f13d02f6a061a40519303c403d493a02099cfa12ddb.jpg)  
FIGURE 3. Type Expressions for Some Enrollment Classes.

```lisp
Global Identifiers
c::COURSE
s::STUDENT
e::enrollment
Pre-Conditions
STUDENT-EXISTS: s.stdno = stdno
COURSE-EXISTS: c.cno = cno
NOT-FULL: c.size < c.limit
NOT-TAKEN-BEFORE: NOT(s.courses_taken CONTAINS cno.)
Post-Conditions
UPDATE-TAKING:
NEW s := LRREPLACE s taking_course (cno : s.taking_course)
UPDATE-ENROLLMENT:
NEW c := LRREPLACE c enrollment (stdno : course.enrollment)
INC-COUNT: NEW c := LRREPLACE c size (c.size + 1)
NEW-ENROLLMENT: NEW e :=
LRCREATE(student:=s * course:=c * credits:=c.credits)
```  
FIGURE 4. Some Pre- and Post-Conditions of enro11.

As depicted in this section, the CSL meets most of the criteria listed in §2. The CSL provides a declarative way to precisely describe structural and behavioral properties of commands without constraining implementation choices. We feel that CSL specifications are comprehensible for architects and implementors with training in formal methods. Pre- and post-conditions for large-scale specifications can be complex. This contrasts with most examples where formal specifications are rather simple such as push and pop for stacks or insert and delete for queues. Section 6 discusses our experiences applving the CSL to an industrial specification in which we encountered rather complex pre- and post-conditions.

So far we have not depicted overloading in the enrol1 command resulting from dependencies among parameters. Section 4 presents a formalism for managing this complexity. Section 5 describes some specification and automated reasoning tools that apply the formalism presented in §4.

## 4. An Abstraction Technique for Commands

In this section, we present command lattices, an abstraction technique that helps to manage the complexity of command specifications. We discuss the complexity of commands, present formal definitions of command lattices and minimal command trees, develop algorithms that map from a minimal command tree to a command lattice, and compare command lattices to incremental overloading in object-oriented programming.

The problem addressed here is the complexity of commands with a large number of interdependent parameters, each having possible side effects. For example, the enroll command has two required parameters (course, student) and three optional parameters. Further, the optional parameter, permission, is a union of OVERLOAD and SPLSTUDENT. This leads to 12 different enrol1 commands corresponding to combinations of the required and optional parameters. Note that any command containing the permission parameter represents two commands depending on whether an overload or special student permission is given. Similar complexity can be found in the commands of other large specifications such as the UNIX operating system. It is our conviction that complexity can be managed with proper abstraction.

A simple idea is to use incremental specification beginning with the smallest part of a command, the behavior of the command with only the required parameters. Complexity is introduced through the addition of optional parameters and their associated behavior. According to this approach, a command can be viewed as a collection of behaviors, one for each valid combination of parameters, controlled by a case statement to select the appropriate behavior based on the actual combination of parameters. In the CSL, a behavior corresponds to a collection of pre- and post-conditions for a combination of parameters. An obvious problem with this interpretation is the number of individual behaviors that must be defined. In the worst case, the number of behaviors is the size of the powerset (set of all subsets) of a command's parameters. However, the worst case or anything near the worst case is unacceptable because the command specifications would be too long to write and understand. A command should be completely described by a minimal set of behaviors from which all possible command behaviors can be derived. The burden of command specification can be reduced further by sharing behaviors among the set of minimal behaviors.

We formalize these notions by introducing the concepts of a command lattice and a minimal command tree. A command lattice is a set of parameter subsets partially ordered by set inclusion with a least upper bound and greatest lower bound.4 Each node of a command lattice is associated with a collection of pre- and post-conditions that describes its behavior. The root of the lattice is the set of required parameters, and the terminal node is the set of all parameters. It must be noted that à command lattice is a lattice of the structural properties of a command and that the behavioral properties do not constitute a lattice.

A minimal command tree is a subgraph of a command lattice with the same root node. It is minimal in the sense that it contains the smallest subset of behaviors from which the command lattice can be generated. The behavior of a node in a minimal tree is defined as the union of the behaviors of the node's parent, the unique pre- and post-conditions of the node, and the redefined pre- and post-conditions of the parent. Since the behavior of the parent node is inherited, only the unique and redefined behavior need be specified. As an example of a minimal command tree and an associated command lattice, consider Figure 5 that graphically depicts the parameters of the enrol1 command. There are three kinds of nodes depicted in Figure 5. Rectangular nodes are part of the minimal command tree, while ovals are part of the

Mannino • Rathnam • Choi · Tseng

![](/api/attachments/EURPGQ77/fulltext/images/61f0867cbf54e32707c81946b1b49bd005fcb580746e0398674fcf8cbd9bc57d.jpg)  
FiGuRE 5. Minimal Command Tree and Lattice for the enrol1 Command.

lattice but not the minimal command tree. Shaded nodes, representing choice nodes, contain one or more parameters with a union type. For example, the permission node represents a choice node for the OVERLOAD and SPLSTUDENT types, respectively. Thus. there are five nodes in the minimal command tree and 12 nodes in the command lattice because each choice node represents two nodes.

A minimal command tree is given by the user and checked to ensure that a consistent command lattice can be generated. Two important consistency properties are complete and disioint as defined below.

$$
\text { Complete: } \bigcup_ {1.. N} (\text { unique } (i)) = \text { Term }
$$

$$
\text { Disjoint: } \bigcap_ {\forall i, j \in \text { Tree }, i \neq j} (\text { unique } (i), \text { unique } (j)) \neq \emptyset
$$

where

Term is the terminal node in the command lattice,

Tree is the set of N nodes in the minimal command tree,

unique(i) is the unique parameters in node i = (Param(i) - Param(j)),

j = Parent(i)

Param(i) is the set of parameters of node i, and

Parent(i) is the parent of node i.

The complete property ensures that a minimal command tree contains the entire set of parameters of the command. The disjoint property ensures that each parameter is originally defined in exactly one node of the tree (i.e., the intersection of the unique parameters of any two nodes is empty). The disjoint property prevents conflicts in the command lattice. As a further guard against conflicts in the command lattice, the behavior associated with a parameter can be redefined along only one path of a minimal command tree. If a command tree is consistent, the disjoint property and the redefinition restriction are together sufficient but not necessary to prevent conflicts when a command lattice is generated from a command tree. To determine necessary conditions, one must test for conflicts among the behaviors associated with each node. It is well known that efficient algorithms for conflict testing (or subsumption testing as it is referred in object-oriented research) are known only for rather restricted languages. In the case of command modeling, it seems preferable to use simple sufficient conditions to prevent conflicts rather than restrict the expressiveness of the CSL. We further discuss this issue in §6.

The algorithm Generate Lattice provides a mapping from a minimal command tree to a command lattice. The resulting command lattice satisfies all constraints of the minimal command tree. The algorithm produces (rather naively) the closure of the minimal command tree by successively computing the union of nodes from the minimal command tree, the first level descendants of the minimal command tree, and so on. After computing the closure of the minimal command tree, nodes with union types are expanded into choice nodes. A pseudo code definition of Generate Lattice follows.

```vhdl
Algorithm Generate Lattice

Input:
    N: the set of parameter subsets of the minimal command tree
Output:
    L: the set of parameter subsets of the command lattice
Procedure:
1. Temp := N;
2. L := N;
3. Repeat until L does not grow
    3.1 NewTemp := U(Temp_i, Temp_j) ∀i, j such that i ≠ j AND AND (Temp_i ¬2 Temp_j) AND (Temp_j ¬2 Temp_i)
    3.2 L := L NewTemp;
    3.3 Temp := NewTemp;
4. Expand nodes containing union types into choice nodes;
5. Return L;
```

To support definition and browsing of commands, we have developed an algorithm to generate an arbitrary node of a command lattice. The algorithm Generate Lattice (or a more efficient version of it) is unnecessary because a user requests selected nodes, not the entire lattice. For an arbitrary subset of parameters, the algorithm Generate Node responds with the complete set of pre- and post-conditions for the given parameters. The algorithm labels pre- and post-conditions with the node of their origination and their status (new (NewPre) or redefined (OvrPre). The algorithm Generate Node implements inheritance as it determines the pre- and postconditions by descending a minimal command tree in a depth first manner.

```autohotkey
Algorithm Generate Node

Input:
    P: the set of parameters given by the user
    R: root node of the minimal command tree

Output: display the set of pre- and post-conditions of each node

Procedure

1. Pre := nil; Post := nil;
2. Visit(R, P, Pre, Post) "Visit is defined below"

Visit(N:Node, P:ParmList, Pre:CondList, Post:CondList)

1. NewPre := N.Pre - Pre; OvrPre := N.Pre - NewPre;
    " - is set difference"
2. NewPost := N.Post - Post; OvrPost := N.Post - NewPost;
3. Pre := Pre ∪ N.Pre; Post := N.Post ∪ Post;

4. Display NewPre, OvrPre, NewPost, OvrPost;

5. For each child node N.Ci;
    5.1 If P Contains N.Ci.ParmList
    Visit(N.Ci, P, Pre, Post);
6. Return;
```

To finish this section, we compare command lattices to method representation in object oriented programming. Command lattices can be considered an extension to incremental overloading in which a method is implemented in a class and then extended in a subclass. The extension to the code of a method in a parent class occurs by referencing the code of the parent and then adding additional code. For example, a class Date has a comparison method < that compares the year, month, and day attributes. The < method in a Time subclass invokes this code and then adds further comparisons for the hour and second attributes.⁵ Command lattices extend this style of incremental overloading in two ways. First, the code sharing in incremental overloading is between a subclass and the ancestor classes on one path, while code sharing in command lattices may involve multiple parents. Second, code sharing for incremental overloading is total and procedural. If there is any undesirable effect from an ancestor's code, the code in the subclass must override it. Overriding is difficult because the code is procedural, and the programming environment does not usually show the shared code. In contrast, sharing in command lattices is explicit through named pre- and post-conditions.

Command lattices are a technique to model individual commands, albeit heavily overloaded. Command lattices can be slightly extended to represent abstract commands, similar to abstract methods in object oriented programming. An abstract command can never be executed. Its purpose is simply to group commands that share specifications. Other than abstract commands, there is no need to model specification sharing among multiple commands. To model temporal dependencies and concurrency among commands, there are techniques based on notions of event and state (Wing 1990) that are complementary to command lattices.

Formal Modeling of Complex Commands

<table><tr><td></td><td colspan="2">Modify command browser for command: ENROLL</td></tr><tr><td>envirn</td><td>cno :: STRING</td><td rowspan="7">The rules are:OR arity -&gt; 3gradelevel :: STRINGcredits :: INTpermission :: PERMISSION-UNION</td></tr><tr><td>help</td><td>stdno :: STRING</td></tr><tr><td>localvars</td><td></td></tr><tr><td>post</td><td></td></tr><tr><td>pre</td><td></td></tr><tr><td>rules</td><td></td></tr><tr><td>type</td><td></td></tr><tr><td></td><td>List of Req Parameters</td><td></td></tr><tr><td></td><td>credits :: INI</td><td></td></tr><tr><td></td><td>gradelevel :: STRING</td><td></td></tr><tr><td></td><td>permission :: PERMISSION-UNION</td><td></td></tr><tr><td></td><td>List of Opt Parameters</td><td></td></tr></table>

FIGURE 6. Modify Command Browser

## 5. Prototype Tools for Command Lattices

In this section, we describe a collection of prototype tools that were developed to demonstrate the potential of command lattices. We begin with a discussion of the tools for defining and browsing commands followed by the automated reasoning tools, the type checker (TC), and the target system tracer (TST).

## 5.1. Browsing and Command Definition Tools

On the basis of the algorithm Generate Node, we have implemented a command definition tool featuring inheritance and overriding of pre- and post-conditions and a browser tool for command lattices. In addition, we have implemented a syntax directed editor for pre- and post-conditions. Figure 6 displays the command definition pane for the enrol1 command. The left subpane lists the command components that can be defined. Generally, a user proceeds by defining the minimal command tree in two steps. First, the parameter names and types are specified and divided into required parameters (root of the command tree) and optional parameters. Second, the user completes the minimal tree by defining rules among optional parameters using an AND/OR notation. The resulting minimal command tree is checked for disjointness and completeness.

Mannino • Rathnam • Choi • Tseng  
![](/api/attachments/EURPGQ77/fulltext/images/13f798b2fd76f7bf3820f8b4d5fc1efe8bbd496733666c33681c16a5b80815a7.jpg)  
FIGURE 7. Syntax Directed Editor.

Pre- and post-conditions are specified for nodes of the minimal command tree The user selects parameters from the middle panes and then pulls down a menu to define, delete, or browse pre- and post-conditions for the given combination of parameters. Only valid combinations of parameters as defined by the minimal command tree can be selected. Pre- and post-conditions from ancestor nodes are inherited. The user needs only to define new and overridden pre- and post-conditions. Overriding is indicated by defining a condition with an identical name as an inherited condition.

Pre- and post-conditions are defined with a syntax directed editor. Figure 7 displays the completed pre-condition NOT - FULL. To avoid precedence rules and parentheses, the editor supports prefix construction of expressions. The user selects tokens from a menu of term types. In Figure 7, note < with two required arguments. Depending on the term type chosen, the editor may prompt for another input or display another menu of options. For example, if PRoJECT is chosen and the user selects a variable, the editor prompts for a component in the corresponding labeled record type. When the user selects PROJECT from the term type menu and the variable course from which to project, the system presents a menu of the components of course.

A user may view the pre- and post-conditions for any node of a command lattice using the Command Browser tool. Figure 8 displays a command browser for the enrol1 command. The right pane contains a graphic representation of the command lattice. Initially the lattice is set to the root parameters. A user may add (remove) optional parameters by selecting the increment (decrement) buttons. Only valid combinations of parameters may be selected. For each parameter selected, an arc is added to the graph. After selecting a combination of parameters, the corresponding collection of pre- and post-conditions can be viewed by selecting a command attribute from the left pane.

![](/api/attachments/EURPGQ77/fulltext/images/cd0d32807e52f45f1799ab73de6c4765a5f1a466cd72e43736bfcbd2d421fc15.jpg)  
FIGURE 8. Command Browser.

## 5.2. The Type Checker

The Type Checker (TC) is a deductive reasoning tool that uses facts and axioms about set membership and inclusion (subset) to reason about expressions. Recall that types are sets constructed from basic domains such as integers and structured domains such as the set of all lists of integers. Facts about set membership and inclusion are represented by two constraint sets:

• The assignment set containing associations of an identifier with a type expression denoting that bindings of the identifier are members of the set denoted by the type expression.

• The restriction set containing inclusion relationships among type expressions. Using the conditional statement (IF) and subset and superset relations, the restriction set represents a command lattice.

Given a collection of type constraints, a type inference system can answer two kinds of questions using rules of inference. First, a type inference system can determine whether an expression is “well-typed." Second, a type inference system can deduce unknown type information such as identifiers with unspecified types and subexpressions. Both inferences can be performed for any node in a command lattice using the constraints of the restriction set. Furthermore, type inference systems are usually designed to deduce the principal or most general type.

![](/api/attachments/EURPGQ77/fulltext/images/4211f00174d15e050d22a1d552cee9f9c6607c516e0d9201c1067967c630b788.jpg)  
FIGURE 9. Type Inference Examples for Instantiations of enrol1

The TC can be used in two contexts for expressions in the CSL. First, when a user checks an instantiated command, the type inference system tells whether the command is “well-typed." For example, the type inference system gives the following replies for instantiations of enrol1 (Figure 9).

Since the first example in Figure 10 is "well-typed," the TC responds with the known result type of enro11. The type identifiers (for example, OVERLOAD) in the type expression can be expanded on demand. The second example is not “welltyped" because it is missing the course number parameter. The TC ascertained that the absence of this parameter did not satisfy the constraints given in Figure 1.

The second context for the TC is for pre- and post-conditions. Here, a user wants to check whether a condition is “well-typed" and determine the types of the identifiers used in the condition. For the pre-condition, NOT - TAKEN- BEFORE (repeated below in Figure 10), the TC infers the type of the entire condition and the types of the identifiers, s and cno. It is not necessary for the user to define explicitly the types of identifiers and subexpressions.

Further details of the TC are beyond the scope of this paper. For a detailed treatment of type inference including the rules of inference, complexity analysis, and formal semantics, consult Mannino, Choi, and Batory (1990) and Choi, Mannino, and Tseng (1990).

![](/api/attachments/EURPGQ77/fulltext/images/cef62897fa83fc1e6bdd0163695a888e072c6db3594ca5d81b3ba0de7bb0124e.jpg)  
FIGURE 10. The Pre-Condition NOT-TAKEN-BEFORE.

```python
Input to the Target System Tracer is
enroll(stdno:='S101' * cno:='IS320')

The outcome is...
    Testing Pre-Conditions: STUDENT-EXISTS, COURSE-EXISTS, NOT-FULL,
    NOT-TAKEN-BEFORE
    Asserting Post-Conditions: UPDATE-TAKING, UPDATE-ENROLLMENT,
    INC-COUNT, NEW-ENROLLMENT

Pre-conditions satisfied -- Post-conditions asserted.

State tracing for command: enroll
    Old value of c.enrollment:[]
    New value of c.enrollment:['S101']
    Old value of s.taking_course:[]
    New value of s.taking_course: ['IS320']
    Old value of c.size = 0
    New value of c.size = 1
    Old value of e = Nil
    New value of e =
    (student:=(ssn:='S101' * name:='Homer Wells' * age:=21 *
    college:='BUS' * status:=true * courses_taken:=[] *
    taking_courses:=['IS320'] * level:='JUN' * major:='IS') *
    course:=(cno:='IS320' * title:='Bus. Programming' *
    dept:='MS' * size:=1 * enrollment:=['S101'] * level:='JUN' *
    credits:=4 * instructor:=['F1']) * credits:=4)
```  
FIGURE 11. Command Tracing for enrol1

## 5.3. The Target System Tracer

The Target System Tracer (TST) complements the TC. The TC ensures that expressions have meaningful values, but it does not make inferences about pre- and post-conditions. The TST simulates the effects of pre- and post-conditions and lists the state of the target system. Because commands cannot be executed, the TST operationalizes the execution of commands by checking whether pre-conditions are satisfied and subsequently asserting post-conditions. The ability to simulate pre- and post-conditions can benefit both implementors and architects of any large scale specification. Implementors can compare the execution trace of their system against the abstract target system. Architects can increase their understanding of pre- and postconditions and discover subtle dependencies among commands.

Figure 11 illustrates tracing of an instantiation of enro11. The pre- and post-conditions are listed first followed by a trace of state changes in the abstract target system. In this case, there are changes to s.taking\_courses, c. enrollment, c. size, and e. The old values of the first two were empty lists and the new values are lists with a single value. The new value of size 1 reflects the addition of the first student. Because of the post-condition, the new value of e contains the values for student, course, and credits. In a similar manner, one can also use the Target System Tracer to investigate the cause of a failure by examining the pre-states of variables.

Internally, the TST relies on the inference engine of the Smalltalk/V286 (Digitalk 1988) Prolog class. Pre- and post-conditions are automatically translated into Prolog clauses, and Prolog's inference engine checks pre-conditions, binds variables, and asserts post-conditions. We augmented Smalltalk-V286 Prolog with some structures and predicate definitions that correspond to basic data types and operators of the CSL. Translation was complicated by dependencies between some of the Prolog predicates and the need to unbind variables. These complications resulted in the use of temporary variables and some context dependent translation.

Except for a few complications as briefly noted above, translation of CSL definitions into Prolog definitions is rather straightforward, but generating code for the complete lattice is difficult. The requirements of the TST were similar to the Command Browser. A user issues a command containing a subset of parameters, and the TST responds with a simulation of the command. We considered several alternatives ranging from static generation of the entire lattice, to static generation of the minimal command tree with dynamic composition, to dynamic generation of a given node. Static generation of Prolog definitions for every node in the lattice is too costly in terms of time and space. The alternative of generating Prolog code for the nodes of the minimal command tree and combining nodes at simulation time was too difficult to engineer. It would have been easier to write an interpreter in Smalltalk and bypass Prolog entirely. A second alternative is to generate dynamically the CSL definition using the algorithm Generate Node, convert the CSL definitions into Prolog, invoke the Logic Compiler of Smalltalk/V286, and then execute the compiled Prolog code. This approach has the unacceptable overhead of invoking the Logic Compiler for each simulated command.

Our solution was to rethink the problem in terms of pre- and post-conditions rather than the command tree or lattice. For purposes of code generation, we redefined a command as a collection of named pre- and post-conditions, each with an activation condition. The activation condition is simply the subset of parameters of the node in the minimal command tree. For an overridden condition, there is one activation condition for each node in which the condition appears. Since we restrict conditions to be overridden along only a single path of the minimal command tree, there is no ambiguity in the generated code. Thus for each condition, the generated code has the form:

condition i:

if parameter combination is . ..

then generated code is . ..

else if parameter combination is

then generated code is ...

The algorithm Generate Conditions formalizes this discussion. It collects preand post-conditions into two lists during a depth first descent of the minimal command tree. Each list contains the condition name and a list of pairs of parameter names (the activation condition) and condition contents. During the traversal, new conditions are appended to the tail of the list, while overridden conditions are updated in place. After the lists are constructed, the code generator translates the CSL conditions into Prolog definitions.

Formal Modeling of Complex Commands

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm Generate Conditions
Input:
    R: root node of the minimal command tree
Output: a pre-condition and a post-condition list each of the form
    [&lt;CondName, [&lt;Parameters, Condition&gt;]]
Procedure
1. Pre := nil; Post := nil;
2. GenNode (R, Pre, Post)
GenNode(N:node, Pre:CondList, Post:Condlist)
1. For each pre-condition in N do
    if N.Pre$_{i}$.Name ∈ Pre
    Update Pre with &lt;N.Pre$_{i}$.Parameters,N.Pre$_{i}$.Condition&gt;
    else
    Append &lt;N.Pre$_{i}$.Parameters,N.Pre$_{i}$.Condition&gt; to end of Pre
... -- An analogous loop for post-conditions
2. For each child node N.C$_{i}$;
    GenNode(N.C$_{i}$, Pre, Post);
3. Return;
</div>

For example, suppose that we have a minimal command tree with the following structure and conditions:

```txt
P1, P2 : C1, C2
|_P3 : C1, C3
|_P5 : C1, C5
|_P4 : C2, C4.
```

Note that P1, P2 are the parameters of the root node and C1 and c2 are its conditions. The algorithm Generate Conditions traverses the minimal command tree in a depth first manner and generates the following collections of /condition, parameter list> pairs.

```txt
C1 : {{P1, P2}, {P3}, {P5}}
C2 : {{P1, P2}, {P4}}
C3 : {{P3}}
C4 : {{P4}}
C5 : {{P5}}.
```

Using these lists, the code generator creates three activation conditions for C1, two for C2, and one each for C3, C4, and C5.

## 6. Experiences with Command Modeling and the Prototype Tools

The software tools described in §5 have been implemented in a mixture of Smalltalk/V286 and Smalltalk/V286 Prolog. The TC was implemented in Smalltalk/V286

Prolog; the other tools, including the TST code generator, syntax directed editors, command browser, and graphical user interface, were implemented in Smalltalk/ V286. Extensive context sensitive help is provided for most functions in the prototype. The prototype is in its third version, and the Smalltalk/V286 code is approximately 15.000 lines, 250.000 bytes, 35 classes, and 700 methods.

The prototype tools were applied to IBM's Distributed Data Management Architecture (DDM), a large specification of remote data access on multiple IBM operating environments (Demers 1988). The DDM provided a fertile ground for demonstrating our approach because it is a large, complex specification in which commands play an essential role. In addition, we had access to architects of the existing specification. The DDM specification consists of several upwardly compatible levels, each comprising more than 1,000 pages of printed documentation about classes and commands. The structural description of classes and commands was partly formalized, but their behavioral description was not formalized. Some commands have a large number parameters with heavy overloading of behavior. For example, the command to create a direct file has a dozen parameters with only two required parameters and the remainder being optional. In many cases, the text description of the behavior was long and complex. For example, the OPEN command has more than four pages of text explaining side effects related to open file lists, cursors, shadow files, and lock tables.

Our experience with the prototype tools, though limited to a subset of DDM commands, has been positive. We have defined six commands dealing with basic file handling capabilities comprising more than 70 conditions. Many of these conditions were complex and required careful analysis. In the process of modeling the commands, we discovered that a specification language has to be very expressive to be useful. Limiting the expressive power by removing disjunction, negation, or selected functions makes reasoning more efficient but renders many interesting conditions difficult or impossible to express.

Since our focus is on using our the CSL to specify large and complex information systems, we extended the syntax and expressive power of the CSL in a number of ways. For example, we extended incrementally the CSL with some (nonprimitive) functions including LRAPPEND (labeled record append), LRREPLACE (labeled record replace) and IF - TħEN - ELSE. We are now convinced, as eloquently argued by Doyle and Patil (1991), “general purpose representation services should provide fully expressive languages." They further argued that inferencing systems should be judged on broad notions of utility and rationality found in decision theory rather than by complexity theories of logical soundness, completeness, and worst case efficiency Thus, we have developed our formal methods based on the desired level of representation power rather than by the level of expressive power than can be processed efficiently in the worst case by certain forms of automated reasoning.

Our experience with the prototype has also revealed the problems of applying our approach to a large project and to transferring our technology. In the case of applying prototype to a large existing specification, it is difficult to justify retrofitting the current specification. More likely is a detailed pilot study to apply our tools to a new version of a specification or new projects. A second problem is the cost to apply our approach. There will be additional software development costs to improve the quality of our software tools. Architects and implementors will require significant training in formal methods. In addition, formal methods usually require more time in the analysis and design stages, even after training is completed. It is more difficult to be precise with our approach than imprecise with a text specification. Overcoming resistance to change and additional fixed costs pose a significant challenge, but we remain confident that the long term benefits outweigh these costs.

## 7. Conclusion

We described an approach to modeling commands in large scale information systems. The main contribution of the approach is an abstraction technique known as a command lattice that manages the complexity of specifying commands with many combinations of parameters and associated behaviors. Complex commands are common when there is a tradeoff between the number of commands and their complexity. Similar to other kinds ofinheritance, command lattices support abbreviation and incremental development of specifications. In addition, command lattices make dependencies among parameters explicit and enable precise, declarative specifications of command behavior. The economic value of command lattices combines the effects from investments in formal methods and abstraction techniques: reduction in software development cost due to more precise and correct specifications as well as improved control of the details of large software projects.

We presented a formal definition of command lattices and a related structure known as a minimal command tree along with algorithms that map from a minimal command tree to a command lattice. To demonstrate the potential of command lattices, we implemented a collection of prototype tools for syntax directed specification, incremental browsing, and automated reasoning through type checking and simulation of command execution. We applied the tools to a subset of classes and commands from IBM's Distributed Data Management Architecture, a large scale specification of remote data access across IBM environments.

This work is part of our long term interests in formal methods and object-oriented modeling and their application to large scale specifications. We are continuing to refine and extend the command lattice idea and prototype tools. Some important extensions are class constraints, proof checking tools for pre- and post-conditions, further consistency conditions for command lattices, test case generation, and version handling. With refinement and extension, we believe that our approach can contribute to improved productivity in the development of complex commands.\*

Acknowledgments. This research was supported in part by a grant from IBM Corporation. An earlier version of this paper appeared at the Twelfth International Conference on Information Systems, December 1991.

\* Steven O. Kimbrough, Associate Editor. This paper was received on June 9, 1992, and has been with the authors 5 months for 2 revisions.

```txt
Mannino • Rathnam • Choi • Tseng
```

## Appendix A. Syntax of the Command Specification Language

Notation: | denotes alternatives, capitalized or bolded items denote constant symbols, a name ending in ‘-list' such as ‘x-list', denotes a list of x's separated by spaces or newlines, square brackets denote optional items, braces denote zero or one of the enclosed items, parentheses (’ and ‘)' denote that exactly one alternative must be chosen, the plus symbol ‘+' denotes concatenation, and —' begins a comment.

```txt
command ::= comm-type local-vars preconds postconds
comm-type ::= type → type [type-restr]
Type ::= (type)
| type-constant
| type-id — global or local type identifier
| [type] — list type
| identifier :: type { * identifier :: type } — labeled record
| identifier :: type + identifier :: type { + identifier :: type } — union
| type → type — function type
type-restr ::= (type-restr)
| type type-pred type
| type-restr AND type-restr
| type-restr OR type-restr
| IF type-restr THEN type-restr
| NOT type-restr
type-pred ::= = | ≤ | ≥
local-vars ::= identifier :: type
| identifier :: type local-vars-list
preconds ::= cond-name : formula
| cond-name : formula preconds-list
postconds ::= cond-name : ( formula | state-change | if-stmt )
| cond-name: ( formula | state-change | if-stmt postconds-list )
formula ::= term comp-op term
| formula AND formula
| formula OR formula
| NOT formula
| (formula)
term ::= simple-term | function-term | (term )
simple-term ::= identifier | literal
comp-op ::= < | = | CONTAINS
function-term ::= term arith-op term
| list-term
| union-term
| record-term
arith-op ::= + | -
list-term ::= term : term — list constructor
| [ ] — empty list
| TL term — tail
| HD term — head of list
union-term ::= AS term label — adds label to make a union
| IS term label — returns value from union
| IN term label — returns TRUE if label in union term
record-term ::= [LRCREATE] label ::= term { * label ::= term }
| term LR-APPEND label term — extend existing LR
| term .label { .label } — extract value
| term LR-REPLACE label term — replace value in LR
state-change ::= NEW identifier term — global change
| identifier ::= term — local change
if-stmt ::= IF formula THEN (term | state-change) [ELSE (term | state-change)]
```

identifier ::= letter+{letterordigit} letterordigit ::= letter | digit literal := integer | string — surround in quotes boolean NIL integer ::= digit+{digit} string := character+{character}' — strings must be surrounded by quotes boolean ::= TRUE  FALSE letter ::= a |b | . . .  z | A |B | . . . | Z digit ::= 0|1|. . .|9 character ::= letter | digit | specialsymbol specialsymbol :=!  @ | . . . — any other printable ascii symbol

## References

Borgida, A., J. Mylopoulos, and H. Wong, "Generalization/Specialization as a Basis for Software Specification," On Conceptual Modeling, Springer Verlag, 1984, 87–117.

Cardelli, L. and P. Wegner, "On Understanding Types, Data Abstraction, and Polymorphism," ACM Computing Surveys 17, 4 (1985), 471–522

Choi, I., M. Mannino, and V. Tseng, "Type Restrictions and Method Interfaces in Object-Oriented Database Programming," IFIP TC2 Working Conf. on Database Semantics: Object Oriented Databases. Windermere, UK, July 1990.

-, and , “Graph Interpretation of Methods: A Unifying Framework for Polymorphism in Object-Oriented Programming," OOPS Messenger, ACM SIGPLAN, Spring 1991.

Canning, P., W. Cook, W. Hill, and W. Olthoff, "Interfaces for Strongly-Typed Object Oriented Programming," in Proc. OOPSLA Conference, New Orleans, October 1989, 457–467.

Curtis, B., M. Kellner, and J. Over, "Process Modeling," Communications of the ACM 35, 9 (September 1992), 75–90.

Demers, R., "Distributed Files for SAA,"IBM Systems Journal 27, 3 (1988), 348–361.

Digitalk Inc., "Smalltalk/V286 Reference Manual," Los Angeles, CA, 1988.

Dijsktra, E. W., “A Discipline of Programming," Prentice-Hall, Englewood Cliffs, NJ, 1976

Doyle, J. and R. Patil, "Two Theses of Knowledge Representation: Language Restrictions, Taxonomic Classification, and the Utility of Representation Services," Artificial Intelligence 48 (1991), 261-297.

Earl, A. et al. "Specifying a Semantic Model for Use in an Integrated Project Support Environment," in Software Engineering Environments, I. Sommerville (Ed.), Peregrinus, London, 1986, 202–219.

Garland, S. and J. Guttag, “An Overview of LP, The Larch Prover," in Proceedings of the Third International Conference on Rewriting Techniques and Applications, Chapel Hill, NC, 1989, 137–151.

Guttag, J., J. Horning, and J. Wing, "The Larch Family of Specification Languages," IEEE Software 2, 5 (September 1985), 24–36.

Hall, A. "Seven Myths of Formal Methods," IEEE Software 7, 5 (September 1990), 11–19.

Harel, D. "On Visual Formalisms," Communications of the ACM, 31, 5 (May 1988), 514–530.

Hoare, C. A. R., “An Axiomatic Basis for Computer Programming," Communications of the ACM, 12, 10 (October 1969), 576–580.

, I. Hayes, H. Jifeng, C. Morgan, A. Roscoe, J. Sanders, I. Sorensen, J. Spivey, and B. Sufrin, "Laws of Programming," Communications of the ACM, 30, 8 (August 1987), 672–686.

Jacob, R. J. K., "Using Formal Specifications in the Design of a Human-Computer Interface," Communications of the ACM, 26, 4 (April 1983), 259–264.

Jones, C. B., “Systematic Software Development Using VDM," Prentice-Hall, Englewood Cliffs, NJ, 1986

Mannino, M., I. J. Choi, and D. Batory, "The Object-Oriented Functional Data Language," IEEE Transactions on Software Engineering 16, 11 (November 1990), 1258–1272.

Meyer, B., "Object-Oriented Software Construction," Prentice-Hall, New York, 1988

Middleburg, C., "VVSL: A Language for Structured VDM Specifications," Formal Aspects of Computing, (Jan-March 1989) 115-135.

Nix, C. and B. Collins, “The Use of Software Engineering, Including the Z Notation, in the Development of CICS," Quality Assurance (September 1988), 103–110.

Sheard. T. and D. Stemple. “Automatic Verification of Database Safety," ACM Transactions on Database Systems 14. 3 (September 1989), 322–368.

Spivey, J., “The Z Notation: A Reference Manual." Prentice-Hall, Englewood Cliffs, NJ, 1989.

Wing, J.. “A Specifier's Introduction to Formal Methods," IEEE Computer 23, 9 (September 1990), 8-24

Winograd. T., “Bevond Programming Languages," Communications of the ACM 22, 17 (July 1979), 391-401.

Yasdi, R., “Learning Classification Rules from Database in the Context of Knowledge Acquisition and Representation," IEEE Transactions on Knowledge and Data Engineering 3, 3 (September 1991), 293-306.
