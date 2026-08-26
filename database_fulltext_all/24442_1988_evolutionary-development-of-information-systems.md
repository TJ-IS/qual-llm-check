---
otero_id: 24442
otero_key: "VE34B9H6"
title: "Evolutionary Development of Information Systems"
authors: "Levent Orman"
year: "1988"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1988.11517830"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Evolutionary Development of Information Systems

## Levent Orman

To cite this article: Levent Orman (1988) Evolutionary Development of Information Systems, Journal of Management Information Systems, 5:3, 19-32, DOI: 10.1080/07421222.1988.11517830

To link to this article: http://dx.doi.org/10.1080/07421222.1988.11517830

![](/api/attachments/VE34B9H6/fulltext/images/b4c18e41e5bc5a75c0bc9b3cdb19011b5a4ceb9a76b827b7fa4f2d19d17b520b.jpg)

Published online: 23 Dec 2015.

![](/api/attachments/VE34B9H6/fulltext/images/399f769134832d27427ecb0f7feb42ffcebc0e7eec969c285a3794d07ceeb41f.jpg)

Submit your article to this journal ↗

![](/api/attachments/VE34B9H6/fulltext/images/319ef956bbc8c99c2ce5aad8f9bb4f0264c97450e18b67013e932dfc0d9d9df0.jpg)

View related articles ↗

# Evolutionary Development of Information Systems

LEVENT ORMAN

LEVENT ORMAN is Associate Professor of Information Systems at Cornell University, Graduate School of Management. He received M.M. and Ph.D. degrees from Northwestern University Graduate School of Management. His research interests are in design, specification, and evaluation of information systems, with recent publications in information systems, information and management, and computer languages.

ABSTRACT: Arguments are presented in support of the evolutionary development of information systems. The traditional analysis and design tools are shown to be inappropriate for the evolutionary development, and the requirements for such a development environment are determined. Three major tools are borrowed from the fields of artificial intelligence, programming languages, and database management, and combined to create an environment that meets these requirements. The resulting novel system architecture is described by using a university registration system.

KEY WORDS: Evolutionary development, system architecture, system life cycle, system design, development tools.

## 1. Evolutionary Development

EVOLUTIONARY SYSTEMS ARE CHARACTERIZED by their ability to adapt to their environment. These systems are not in their final form once designed, but the design process stretches over their entire lifetime, constantly providing a better approximation to the ideal product. The evolutionary nature of a system refers not only to its maintenance but also to the original creation. Consequently, the evolutionary systems are not developed from an overall design, but from bits and pieces of information that have been captured at different times by different people, and evolved through time by extensive use, testing, and modification by a variety of users.

The major argument for an evolutionary strategy is the contention that it may be the only feasible strategy for the development of highly unstructured and unstable systems where the traditional requirements and analysis techniques frequently fail [9]. Most strategic management applications and decision support systems fall into this category, since their requirements are generally vague, and the objectives are fluid even in the minds of end users [34]. Even when the organization is stable and the objectives are clear, the end users may not be able to determine their requirements because they may have no consistent model of their decision processes, whether descriptive or prescriptive [9], and even where they could determine the requirements they may fail to communicate them properly to the designers [8, 19, 21].

Evolutionary design may also be the only feasible strategy for end-user development of large shared systems. End-user development has been advanced as the ultimate solution to software crisis by bypassing the computing professionals $[20, 24]$ . Since the end users presumably understand their requirements better than any analyst ever can, they are in the best position to formalize their requirements. Moreover, all the political and privacy-related problems associated with the information (and power) transfer to the computing staff (due to their intermediation between the end users and the system) are automatically resolved $[32]$ . Although promising, end-user computing has not achieved its full potential, since to date it has been restricted to the development of small and private systems, and mere retrieval from shared resources $[4]$ . The development of shared organizational information systems by end users is not feasible with the traditional design tools, since it would either require a tremendous commitment of time from the end users to reconcile their requirements with those of others, or it would lead to large-scale redundancy and inconsistency in the system if they fail to make such a commitment. Consequently, an evolutionary strategy and a corresponding architecture appear to be essential to accommodate end-user development of organizational information systems where each user contributes a small piece of the system at a time, without a major commitment to the development process and without duplicating or contradicting the contributions of other users.

The current enthusiasm for prototyping is mainly due to its approximately evolutionary nature during the initial stages of development $[3, 5]$ . By far the most commonly cited advantage of prototypes is their evolvability, since they can be modified quickly in response to changing user needs. Evolvability of the prototypes is instrumental not only in eliciting the user requirements and validating them by providing a concrete but flexible basis for exchange of ideas, but also in creating an environment of cooperation and communication between the users and the designers, which is so critical for a successful development $[15, 18, 22]$ .

Unfortunately, a truly evolutionary development is not feasible with the traditional design tools. It requires a significantly different system architecture and a variety of new tools. The different requirements of an evolutionary strategy will be discussed in the next section. The tools necessary to implement an evolutionary strategy will be introduced in section 3, and an evolutionary architecture will be sketched in section 4. Section 5 will provide an example of the new architecture using a university registration system.

## 2. Requirements

EVOLUTIONARY DESIGN REQUIRES a significantly different architecture from the traditional system structures. The first and the most obvious difference is the need for very small and highly independent modules, since evolution implies many small and quick modifications $[14]$ . The need is especially obvious if the end-user development is to be supported. The end users cannot be expected to develop large software modules requiring major time commitments. After all, the end users are not in the business of full-time system development. They need to contribute simple ideas, facts, and relationships as individual modules—one at a time—with no major commitment to organize those modules and their relationships into a software system. Popular programming languages do not lend themselves to such extensive modularization, since as the module size is reduced the interaction among modules increases. For modules small enough to be created by the end users, the interaction among the modules is usually too complex to permit end-user development without a major coordination and communication effort $[30]$ . A system specification and programming environment based on very small and highly independent constructs is essential for evolutionary development.

## Example 2.1

Every university registrar's information system contains procedures to compute and report the GPA's of students at the end of each semester. These procedures involve retrieval from student and course files, partitioning course records with respect to students, computation of GPA for each student, and finally report design. To achieve small enough components to be appropriate for end-user development, these components would have to be separated from each other and possibly further divided into smaller independent components. It is not reasonable to expect the totality of GPA computation from one end user.

Not all development effort goes into the creation of modules. Combining modules into meaningful programs is also a major task. With a large number of very small modules this task is even more complex $[37]$ . As the module size is reduced, the increasing complexity of forming meaningful programs may hinder the evolvability of the systems, since evolvability implies quick and small modifications not only to the individual modules but also to the way they are combined. It is again useful to think in terms of end-user development, and the appropriate level of complexity for combining modules into meaningful programs by the end users. To minimize the effort by an individual user to create meaningful programs from existing modules, the combining task may have to be divided into many small and highly independent steps, and this requires the ability to provide many levels of abstraction. System design with multiple levels of abstraction involves modules that can be combined in a variety of ways to produce new, higher-level modules, which are themselves available as individual units for further combination [27]. The independence of these multiple steps of abstraction is necessary to distribute these steps among many users. It is also necessary that the abstraction mechanism remains the same from small-module level to large-program level for uniformity of user tasks and to minimize learning. More preferably, the abstraction mechanism should remain the same for the complete development effort—ranging from primitive operations to the complete system—to extend the uniformity beyond the boundaries of the design process, to the analysis on the one hand and to the implementation on the other. Data also need to belong to many levels of abstractions in order to facilitate sharing without redundancy and without complex conversion procedures. Abstraction by functional composition is commonly used in the early stages of system design when handling large modules [10]. However, it fails with smaller modules because of strong interaction among smaller modules preventing pure functional decomposition. Data abstraction is generally acknowledged as useful in literature [33], but very few database management systems provide even the three levels of abstraction adopted by ANSI [1]. Multiple levels of data and procedure abstraction are essential for evolutionary development.

## Example 2.2

The user of the registration system who merely needs to retrieve the GPA value for a particular student needs to link and execute all relevant modules with appropriate restrictive parameters. If a single end user is expected to accomplish this task without customized front-end procedures, he must be protected from both the data and procedural details. He must be protected from the requirement to know the type of student in question, since GPA computation may be different for graduate students, transfers, and honors students. Data abstraction facilities that generalize all those types and their attributes to a generic STUDENT type and generic attributes are essential. He must also be protected from the requirement of explicitly calling and linking all necessary procedures, since GPA computation will involve many data-retrieval and formatting procedures, in addition to fairly complex computations with a number of exceptions for seminars, colloquia, and non-credit or PASS/FAIL courses. Procedural abstraction of multiple independent levels restricting the top level to a simple procedure call with few parameters, and consecutive levels to simple functional decomposition, is essential.

Given a large number of small modules and the ability to combine them in various levels of abstraction, the final requirement is an effective mechanism to describe those modules extensively to facilitate sharing and combining by end users. Popular programming environments do not provide formal tools for the description of modules, but rely on separate documentation, and comments in the code, neither of which utilizes a formal and unambiguous language $[16, 17]$ . Formal semantics of programming languages are complex and the tools provided are not easily usable in practice $[13]$ . The description of data used by a module is also an integral part of the description of that module. Data description also received much attention in the literature, and the field of data semantics has expanded into a major field of study $[35]$ . For practical purposes, data semantics met with more success than procedural semantics. Not only a variety of practical tools for data description have been devised $[11]$ , but many commercial database management systems provide facilities for the description of data and the enforcement of integrity. The same type of practical success is also needed with procedures, since extensive description of modules is essential for evolutionary design where a large number of end users may create, use, share, and modify a large number of modules for a variety of purposes.

## Example 2.3

When the users are given the power to elicit information such as the GPA of a student by a mere function call and with no other knowledge about the system, then they must be protected from misusing the system through extensive description. The data item GPA has to be associated with an extensive description in addition to the integrity constraints that protect the system. The description has to contain the relationship of this data item to others in the form of a data model. The GPA has to be described in terms of its relationship to the student's standing and probationary status. A GPA of under 2.00/4.00 should be related to “poor” standing in the student record. Moreover, a derived data item such as GPA cannot be fully described without some reference to the formulas that compute it. A concise procedural semantics devoid of algorithmic details is essential for a complete description.

## 3. Tools

THREE MAJOR TOOLS FROM THE FIELDS of programming languages, artificial intelligence, and database management will be borrowed and combined to produce an architecture appropriate for evolutionary design [6].

The functional style of programming will be borrowed from the field of programming languages to achieve the abstraction capability required for evolutionary development. A functional programming language consists of a collection of primitive functions and a small number of operators $[12]$ . Each function is a mapping from its domain to its range where the domain and range are usually expressed as lists of data items $[2, 23]$ , and each operator is a mapping from functions to functions. A functional programming environment contains both primitive functions and user-defined functions created by applying the operators to the existing functions. The environment is characterized by the application of functions to data to derive new data solely by a sequence of mappings. No side effects are allowed, and no global variables exist to influence the execution of a function by setting the values of those variables from outside the function. Consequently, a function applied to the same data always returns the same result, and programs are collections of functions that do not depend on state variables or the state of the system except through their formal arguments. The composition operator is the major operator common to all functional languages. It involves the consecutive application of two functions, defined as a new function, and provides a uniform abstraction mechanism ranging from the primitive functions level to the complete system level. Consequently, the functional programming languages provide an excellent tool to meet the abstraction need of an evolutionary development strategy.

Production systems will be borrowed from the field of artificial intelligence to meet the modularity requirement of evolutionary development. Production systems are widely used in artificial intelligence applications where a large number of loosely coupled procedures may have to be combined in various ways to respond to a variety of situations $[31]$ . A production system provides a highly modular programming environment with very small and highly independent modules. Each module is called a production rule and consists of a procedure (called the “body”), and a set of conditions (called the “pattern”) that must be satisfied to activate the procedure. Ordinarily, the rules are highly independent; they do not call or refer to each other, and they are activated only when their pattern is matched by a global database that provides the only means of communication among the rules $[36]$ . Consequently, the production systems provide an excellent tool to meet the requirement for very small and highly independent modules in evolutionary systems.

Data models from the field of database management will be borrowed to meet the data description requirements of evolutionary development. Data models provide formal description of data by using data structures and integrity constraints. Data structures are used to formalize the relationships among data items into standard forms so that they can be treated uniformly, and generic procedures can be designed to apply to all data items in a particular collection. The same data may be structured in a variety of ways to serve different needs efficiently where efficiency may be measured in terms of machine utilization or user effort. More appropriately the same data, with a unique physical structure, can be viewed as having a variety of virtual structures through run-time conversion. This approach has the advantage of nonredundancy by avoiding the storage of multiple copies of the same data where each possesses a different structure. The run-time conversion of data by a database management system into three levels of structures, each designed for a broad category of users (such as implementors, designers, and end users), has been proposed as an industry standard $[1]$ . The structure rarely provides adequate description of data and it has to be augmented with integrity constraints. An integrity constraint is a logical predicate to be satisfied by the data at all times. A variety of languages to express the integrity constraints and many methods to enforce them efficiently have been developed, and some are provided by the commercial systems $[7, 35]$ .

## 4. Evolutionary Architecture

THE THREE MAJOR TOOLS DESCRIBED in section 3 will be combined in a unique fashion to provide an evolutionary architecture. A production rule environment is employed to provide for the maximum independence of the modules. Each rule is viewed as a small and simple module. Modules are highly independent since the production rules are activated independently whenever their conditions are satisfied, and they do not explicitly call or refer to each other but interact only through the highly structured global database. Such a high degree of independence is crucial in facilitating development by multiple end users on a piecemeal basis and with minimal coordination and communication. The major shortcomings of the production system are the lack of parameter passing, procedure and data abstraction, and data sharing. These shortcomings are remedied by utilizing functional programming languages and data models within a production system environment.

## Example 4.1

Using the notation $C|A$ for a production rule requiring that if the conditions $C$ hold then the actions $A$ should be taken, the GPA computation within the registrar's information system can be accomplished as follows using three independent production rules communicating through central data buffers:

Buffer $B_{1}$ is empty. Retrieve a student record $s$ into $B_{1}$ .  
Buffer $B_{2}$ is empty. Retrieve a course $c$ taken by student $s$ into $B_{2}$ . Mark $s$ and $c$ to prevent repeated retrieval.

$$
B _ {1}
$$

$$
B _ {2}
$$

$$
B _ {2}
$$

$$
B _ {2}
$$

A record s is in $B_{1}$ . Compute GPA=TPOINT/TCREDIT.
Buffer $B_{2}$ is empty. Format and print GPA.
Eliminate s from $B_{1}$ .

To add abstraction power to the production system, all rules are expressed in a purely functional language. Functional languages provide multiple levels of abstraction through functional composition. The abstraction mechanism is uniform, and ranges from the primitive functions to the system level. The side-effect-free nature of functional languages makes it possible to combine a large number of functions to create a meaningful program in multiple, highly independent steps, where at each step only a small number of functions is combined to generate a slightly higher-level function. This capability is crucial in dividing into many steps the formidable task of forming a meaningful program from a large number of very small modules, and keeping the steps uniform and independent so that they can be accomplished by a variety of minimally cooperating end users on a piecemeal basis. Consequently, although the production rules do not provide an abstraction mechanism where multiple production rules can be combined into a single higher-level production rule, it is possible to achieve the same effect by using functions at different levels of abstraction in forming the production rules. Each production rule is viewed as computing a function from more elementary functions under given conditions. All three components—the function to be computed, the procedure, and the conditions—are expressed using a functional language for uniformity. The resulting environment allows production rules to call each other, but only when the function computed by a production rule is needed by another production rule computing a higher-level function. In effect, the production rules are stratified into multiple levels of abstraction in terms of the functions they compute. The shortcomings of the functional languages are the lack of facilities for the management of shared data, data abstraction, and data description. These shortcomings are remedied by utilizing a semantic data model compatible with the functional programming principles and the production system.

## Example 4.2

A functional language utilizing the predicates “contained in” $\epsilon$ , and “equal” =, the aggregate arithmetic operator “sum over i” $\Sigma_{i}$ , in addition to the regular arithmetic operators can be used to express the GPA computation problem:

$$
\begin{array}{l l} s \in \text {STUDENT} \mid \text {GPA} (s) = \text {TPOINT} (s) / \text {TCREDIT} (s) \\ s \in \text {STUDENT} & \text {TPOINT} (s) = \sum_ {c} g \\ c \in \text {COURSE} \\ c \text {is taken by} s \\ g \text {is grade of} s \text {in} c \\ s \in \text {STUDENT} & \text {TCREDIT} (s) = \sum_ {c} r \\ c \in \text {COURSE} \\ c \text {is taken by} s \\ r \text {is the number of credits of} c \end{array}
$$

The functional data model concept is employed to meet the data description and data abstraction requirements in an evolutionary environment $[26, 28]$ . The concept will be expanded to also include extensive description of procedures to complete all the requirements listed in section 2. A data model provides facilities for data description, data abstraction, and data sharing. The functional data model is a semantically rich data model that is also highly compatible with the functional programming environment. A functional data model consists of functions defined on data sets, where each function captures a relationship between the set of data items comprising the domain of the function and the set of data items constituting the range. A function is a general structure, and sets, sequences, trees, and many other data structures can be expressed in terms of functions. In conformity with the production environment, each function is described by a set of conditions that must be satisfied by the function at all times. These conditions are also expressed using a functional language. Moreover, the use of functions as a unit of data as well as a unit of procedure allows a single set of facilities to manage both the data and the procedures in the uniform environment of production systems. Data abstraction facilities are based on functional decomposition and functional specialization and they are exactly the same as procedure abstraction facilities. Similarly, procedure description reduces to mere data description since all procedures are expressed functionally and each function is described using the production rule format. Within this architecture, an information system is a collection of functions corresponding to data and procedures. Each function has a collection of constraints attached to it, and the derived functions also have procedures associated with them to compute their values. Both the constraints and the procedures are expressed functionally. The constraints associated with the observed data functions can be interpreted as integrity constraints, and the constraints associated with the derived functions establish the conditions under which the associated procedure can be used to compute the function. Since all constraints and procedures are sequences of function applications, all of their components are described similarly in the uniform environment of the production system. In summary, the functional data model provides the data description and data abstraction capabilities essential for an evolutionary environment where the activities of many users have to be coordinated over long periods of time. The data model also meets the need for extensive procedure description due to its choice of the function as a unit and the resulting uniform treatment of data and procedures. The general shortcomings of data models are the lack of facilities to manage the procedures to create and maintain data, and they have already been remedied by the other components of the evolutionary system.

## Example 4.3

A functional data model containing the functions STUDENT, COURSE(STUDENT), CREDIT(COURSE), GRADE(STUDENT, COURSE) can be used to express data retrieval directly with no intermediate data structures (such as lists used in most logic programming):

$$
s \in \text { STUDENT }
$$

$$
\operatorname{GPA} (s) = \text { TPOINT } (s) / \text { TCREDIT } (s)
$$

$$
s \in \mathrm{STUDENT}
$$

$$
\operatorname{TCREDIT} (s) = \sum_ {c} \operatorname{CREDIT} (c)
$$

$$
c \in \operatorname{COURSE} (s)
$$

$$
s \in \mathbf {S T U D E N T}
$$

$$
\operatorname{TPOINT} (s) = \sum_ {c} \operatorname{GRADE} (s, c)
$$

$$
c \in \mathbf {C O U R S E} (s)
$$

## Example 4.4

Additional functions such as STANDING(STUDENT) can be used to describe the data item GPA, and specializations such as GRAD of STUDENT can be used for abstracting descriptions so that a user who is interested in the standing of a student does not have to know if the student is grad or not, or how the GPA is computed:

$$
s \in \mathrm{STUDENT}
$$

$$
\operatorname{GPA} (s) \geq 3. 0 0
$$

$$
\text { STANDING } (s) = \text { 'GOOD' }
$$

$$
\begin{array}{l} s \in \text { STUDENT } \\ s \notin \text { GRAD } \\ \text { GPA } (s) \geq 2. 0 0 \end{array}
$$

$$
\text { STANDING } (s) = ^ {\prime} \text { GOOD } ^ {\prime}
$$

$$
\begin{array}{l} s \in \text { STUDENT } \\ \text { STANDING } (s) \neq \text { `GOOD' } \end{array}
$$

$$
\text { STANDING } (s) = \text { 'POOR' }
$$

## 5. Design Experiment

THE EVOLUTIONARY ARCHITECTURE described in section 4 has been used in designing an experimental registration system for the Graduate School of Management in a major university. In a series of small-scale mock registrations run in parallel with the regular university registration, the following major differences between the life-cycle and evolutionary approaches to development were observed: a. In the evolutionary approach a large portion of the development effort is taken away from the computing professionals and delegated to and distributed among many users. The contribution of each end user is minimal due to the extreme modularity of the architecture and the large number of end users. Consequently, the evolutionary approach appears to be more appropriate for more complex and less structured systems where a single algorithmic solution is not readily available. A registration system, generally considered to be a well-structured and straightforward application, became a good candidate when expanded into a less structured and more complex system of multiple conflicting goals set by the students, faculty, and the administration.

b. The evolutionary approach largely bypasses the requirements analysis phase and consequently is more appropriate for less structured systems where this phase is the most complex. It is also appropriate for the systems where the requirements analysis is complicated by the sheer number of nonhomogeneous end users with personal and distinct requirements. The registration system does exhibit this property due to a large number of students with widely varied interests in terms of the courses they want to take, the instructors, the lecture rooms and the lecture hours they prefer, the size of the classes they attend, and the nature of students attending each class.

c. Even with a small number of homogeneous end users, the requirements analysis may be complicated by the reluctance of end users to divulge their personal and private requirements to computing professionals. The evolutionary approach and the end-user development it affords appear to be more appropriate for systems with a considerable amount of private information. Unfortunately, the extent or even the existence of relevant private information is not known to the analysts until a commitment is made to end-user development and appropriate security measures are taken to protect the privacy of individual end users. The registration system revealed an amazing array of private student requirements ranging from the grading behavior of the instructors and teaching assistants to the background, personality, and the competitiveness of classmates. It is unlikely that these types of requirements would be revealed to systems analysts, especially when they expose the embarrassing weaknesses and the selfish concerns of end users.

d. Soon after the decision to develop the system, the evolutionary approach delivers a skeleton with which the users can interact, make modifications, corrections, and additions. This capability is extremely important in getting the users involved early in the process, which is commonly advocated as a critical success factor. On the other hand, the development of the system is very gradual and may take longer than it would with a traditional approach. With less structured requirements the system may never cease evolving. The lack of a point in time at which the system is complete, correct, and reliable may be a major disadvantage for some users; and for some applications it may be necessary to establish a deadline to halt artificially the evolution of the system and deliver it as complete. The registration application is a typical example of this. At some point in time it is necessary to stop the registration process and to declare the current state of the system as final for administrative and grading purposes.

e. The system is completely modular. No metarules are needed to assign priorities or to control the execution sequence of rules. The restriction of certain types of rules to certain users is accomplished solely through the data security system. For example, students cannot modify the class size limits because they do not have write access to the SIZE function. Similarly, faculty members cannot enter rules to print the conflict resolution procedures used by the administration because they do not have read access to those functions.

The registration experiment that was designed to test the evolutionary concepts involved a stylized functional language based on the three tools described in section 4. All components of the system were expressed by the end users as small and independent production rules written in this functional language. An interpreter for the language is the only professionally developed software required to automate the end-user development process. The end users, as developers, are classified into the administration, faculty, and the students. The administration is required to specify the requirements with respect to the courses to be offered, the available classrooms and their capacity limits, the time periods acceptable for classroom instruction, the instructors eligible to teach in each department of the school, and the minimum load requirements for each student and faculty member. The administration is also expected to provide the criteria to resolve the possible conflicts among faculty, and between the faculty and students. Simple criteria based on faculty seniority and the dominance of faculty preferences over student preferences are easy to specify and efficient in terms of computing resources; however, more complex criteria may sometimes be preferable. The faculty provides the system with its preferences for courses to teach and the time and classroom assignments preferred for each course. The students complete the system by entering their preferences for the same. These roles are typical of the administrators, faculty, and students in a university environment although they are played differently in traditional and evolutionary approaches.

Another crucial difference in the evolutionary approach is that none of the participants are restricted to the strict roles prescribed for them. The major advantage of the evolutionary approach is its personalized nature for each end user. Since the end user is not just a user but also a developer of the system, there are no theoretical or practical limits to what each user can enter into the system. This is possible because the role of an individual end user is not predetermined and fixed by the developers of the software, but the end user (as a developer) is given a language through which he expresses his requirements freely and with no prior constraints. In the registration application, for example, there is nothing to prevent a student from requesting classes where the average GPA of all registered students for that class is less than 2.50, unless another rule by the administration overrules that type of criteria. Some typical (and some not so typical) rules entered by the students into the registration system are shown in the Appendix to demonstrate the user interface without going into the syntactic details of the languages used.

## 6. Conclusions

An evolutionary approach appears to be essential to the development of highly unstructured and unstable systems such as those designed to support strategic decisions. Moreover, the much heralded end-user development cannot be expected to go much beyond the development of small and private systems unless an evolutionary strategy is adopted. Unfortunately, the traditional analysis and design tools do not lend themselves to evolutionary development because of the rigidly defined stages in the life cycle, and the independence and incompatibility of the tools used in different stages. An evolutionary environment is characterized by the integration and the concurrency of the developmental stages, and the need for comprehensive tools supporting the complete life cycle. Such an environment has significantly different requirements, such as very small module size, procedure and data abstraction capabilities in multiple levels, and extensive description of data and procedures. Three major tools have been borrowed from the fields of artificial intelligence, programming languages and database management to meet each of these three requirements. The resulting novel architecture is highly evolutionary since each module is minimal in that it represents a single fact or a relationship, and a large number of modules can be easily combined in a variety of ways to form meaningful procedures due to the extensive and formal description of the modules and the abstraction capacity that divides the task into multiple independent steps. A complete set of tools to support the evolutionary development has been designed; the technical details have been reported elsewhere [29].

## APPENDIX

SAMPLE STUDENT INTERACTION WITH THE REGISTRATION SYSTEM:

SIZE(CS101) ≤ 100
INSTRUCTOR(CS101) ∈ {Doe, Thomas}

CS101 ε
COURSE('J. M. Smith')

ROOM(MIS507) $\epsilon$ {101,108,204} TIME(MIS507) $\leq 1100$

MIS507 ε
COURSE('J. M. Smith')

A. T. Clarke $\notin$ STUDENT(MIS600)  
AVERAGE(GPA(STUDENT(MIS600))) $\leq 2.50$

MIS600 ε
COURSE('L. L. Rowe')

The three production rules shown above demonstrate the bulk of the entries made by the students into the registration system. The first rule indicates that J. M. Smith would like to take the course CS101 if the size of the course is less than 100 and the instructor is either DOE or THOMAS. The second rule states that J. M. Smith is interested in taking MIS507 if it meets in room 101, 108, or 204 and it meets before 11:00 AM. The third rule indicates that L. L. Rowe would register for MIS600 if another student A. T. Clark is not in that class, and the average GPA of all students in that class is less than 2.50! “Average” and “GPA” are functions defined elsewhere in the system using the same notation. The syntax of a complete functional language based on production rules has been reported elsewhere [29].

## REFERENCES

1. ANSI/X3/SPARC Study Group on Database Management Systems. DBMS Framework, D. Tsichritzis and A. Klug eds., AFIPS Press, Montvale, NJ, 1977.

2. Backus, J. Can programming be liberated from the Von Neumann style? A function style and its algebra of programs. Communications of ACM, 21, 8 (1978), 613–641.

3. Bally, L.; Brittan, J.; Wagner, K. H. A prototype approach to information system design and development. Information and Management, 1, 1 (1977), 21–26.

4. Benson, D.H. A field study of end user computing: Findings and issues. MIS Quarterly, 7, 6 (1983), 35–45.

5. Berrisford T., and Wetherbe, J. Heuristic development: A redesign of systems design. MIS Quarterly, 3, 1 (1979), 11–19.

6. Brodie, M. L.; Mylopoulos, J.; Schmidt, J. W. Conceptual Modeling: Perspectives From Artificial Intelligence, Databases and Programming Languages. New York: Springer Verlag, 1984.

7. Buneman, D. P., and Clemons, E. K. Efficiently monitoring relational databases. Transactions on Database Systems, 4, 3 (1979), 368–382.

8. Couger, J. D.; Cotler, M. A.; and Knapp, R. W. Advanced System Development/Feasibility Techniques. New York: Wiley, 1982.

9. Davis, G. B. Strategies for information requirements determination. IBM Systems Journal, 21, 1 (1982), 4–30.

10. Gane, C., and Sarson, T. Structured Systems Analysis: Tools and Techniques. Englewood Cliffs, NJ: Prentice Hall, 1979.

11. Hammer, M., and McLeod, D. Database description with SDM: A semantic database model. Transactions on Database Systems, 6, 3 (1981).

12. Henderson, P. Functional Programming: Applications and Implementation. Englewood Cliffs, NJ: Prentice Hall, 1980.

13. Hoare, C. A. R., and Lauer, P. E. Consistent and complementary formal theories of the semantics of programming languages. Acta Informatica, 3, 1 (1974).

14. Keen, P. G. W. Adaptive design for decision support systems. Data Base, 12, 1 (1980), 15–25.

15. Kraushaar, J. K., and Shirland, L. A. A prototyping method for applications development by end users and information system specialists. MIS Quarterly, 9, 3 (1985), 189–198.

16. Krieg-Brueckner, B., and Luckham, D. C. Anna: Towards a language for annotating Ada programs. SIGPLAN Notices, 15, 11 (1980), 128–138.

17. Lampson, B. W., et al. Report on the programming language Euclid. SIGPLAN Notices, 12, 2 (1977), 1–79.

18. Lucas, H. C. Why Information Systems Fail. New York: Columbia Press, 1975.

19. Lucas, H. C. The evolution of an information system: From key-man to every person. Sloan Management Review (Winter 1978).

20. Martin, J. Application Development Without Programmers. Englewood Cliffs, NJ: Prentice Hall, 1982.

21. Martin, J., and McClure, C. Structured Techniques for Computing. Englewood Cliffs, NJ: Prentice Hall, 1985.

22. Mason, R. E. A., and Carey, T. T. Prototyping interactive information systems. Communications of ACM, 26, 5 (1983), 347–354.

23. McCarthy, J. Recursive functions of symbolic expressions and their computation by machine. Communications of ACM, 3, 3 (1960).

24. McLean E. R. End users as application developers. MIS Quarterly, 3, 4 (1979), 37-46.

25. Orman, L. A familial specification language for database applications. Computer Languages, 8, 3 (1983), 113–124.

26. Orman, L. Familial model of data. Computer and Information Sciences, 13, 3 (1984), 149–175.

27. Orman, L. A multilevel design architecture for decision support systems. Data Base, 15, 3 (1984), 3–10.

28. Orman L. Design criteria for functional databases. Information Systems, 10, 2 (1985), 207–217.

29. Orman, L. Functional development of database applications. IEEE Transactions on Software Engineering 14, 9 (1988), 1280–92.

30. Parnas, D. L. On the criteria to be used in decomposing systems into modules. Communications of ACM, 15, 12 (1972), 1053–1059.

31. Rich, E. Artificial Intelligence. New York: McGraw Hill, 1983.

32. Rockart, J. F., and Flannery, L. S. The management of end user computing. Communications of ACM, 26, 10 (1983), 776–784.

33. Smith, J. M., and Smith, D. C. P. Database abstractions: Aggregation and generalization. Transactions on Database Systems, 2, 2 (1977), 105–133.

34. Sprague, R. H., and Carlson, E. D. Building Effective Decision Support Systems. Englewood Cliffs, NJ: Prentice Hall, 1982.

35. Tsichritzis, D. Data Models. Englewood Cliffs, NJ: Prentice Hall, 1982.

36. Waterman, D. A., and Hayes-Roth, F. eds. Pattern Directed Inference Systems. New York: Academic Press, 1978.

37. Zelkowitz, M. V.; Shaw, A. C.; and Gannon, J. D. Principles of Software Engineering and Design. Englewood Cliffs, NJ: Prentice Hall, 1978.
