---
otero_id: 11376
otero_key: "FMDFFW5N"
title: "The Application Software Factory: Applying Total Quality Techniques to Systems Development"
authors: "Kent Swanson; David McComb"
year: "2000"
journal: "MIS Quarterly"
doi: "10.2307/249460"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Application Software Factory: Applying Total Quality Techniques to Systems Development

By: Kent Swanson
Andersen Consulting
717 17th St., Suite 2000
Denver, Colorado 80202

Dave McComb
Micro Planning International
950 So. Cherry St., Suite 912
Denver, Colorado 80222

Jill Smith
College of Business Administration
University of Denver
2020 So. Race St.
Denver, Colorado 80208

Don McCubbrey
College of Business
Administration
University of Denver
2020 So. Race St.
Denver, Colorado 80208

## Abstract

This paper describes an approach to application software development (the Application Software Factory) that enables over 90 percent reuse of code, produces application code where quality is measured in defects per million lines of code, and generates productivity exceeding that of interpretative 4GL environments. The environment is built on top of a commercial CASE tool and does not rely on exotic technology. The delivered systems are COBOL transaction processing systems using relational database technology and are predominantly online. Two applications of approximately 200,000 lines of code have each been developed by teams at two different sites. A third application of over 2 million lines of code is nearing completion. The paper depicts the important relationships between technology, management, methods, and design approaches that comprise the Application Software Factory.

Keywords: Software factory, software reuse, software development productivity

ACM Categories: D.2.1, D.2.2, D.2.3, D.2.5, D.2.6, D.2.7

Burgeoning system size and complexity lead to larger teams and increasing communication difficulties. These problems interact and continue to grow through system component and integration testing and linger throughout the entire systems development life cycle. In the 1990s, system size and complexity are driving major corporations to develop solutions such as the Application Software Factory (ASF). ASF approaches substitute well-managed, design-driven reusability for the “wheel reinvention” of custom code.

Recently, Software Maintenance News (1991) confirmed the trend toward large system size by reporting a survey comparing the average size of systems in 1980 (23,000 LOC) and in 1990 (1,246,000 LOC). Fred Brooks (1987) points out two sources of complexity in software development: those that relate to the inherent complexity of the problem being solved (the essence) and those that are by-products of the myriad of architectures and approaches for solving these problems (the accidents). Accidental code appears through combining tools, languages, and design approaches, which in turn, emphatically increase software complexity. Brooks suggests that the two complexities interact to compound each other. The environment of the ASF simplifies the development process, partitions the complexities, and eliminates the accidents. This allows the analysts to concentrate on organizing the essence into reusable architectures.

Celite Sales Corporation has had exceptional success with a group of technologies and approaches collectively termed the Application Software Factory or ASF. Not simply a code generation exercise, the ASF integrates a number of techniques. Cumulatively, these techniques generate an order of magnitude improvement in both software development productivity and in the quality of delivered code. Celite CIO, Steve McMillan, states, “Estimates made prior to development of the Software Factory suggested that most features would take from 10 to 30 work days to implement. Actual development for these same features took 1 to 2 days.”

Celite is a multi-national company with operations throughout the U.S. and overseas. In 1988, following a strategic information planning effort, the company formalized a new IS policy to move as rapidly as possible to a distributed IS architecture. While application software could facilitate some of the anticipated systems development, management recognized the necessity for a considerable amount of custom development and authorized building the ASF. Celite's McMillan adds “Several more projects remain in the plan which will use this approach and the ASF tools built to date. The expectation is to roll projects out to other larger Celite organizations and to try the ASF on different types of systems.”

This paper is organized into five sections. The first section is a synopsis of systems and architectures that are currently billed as “software factories.” In particular, Japanese software factory concepts are compared to contemporary U.S. software engineering practices. The second section develops the underlying total quality concepts that make the factory work. The third section describes the actual components and the relationships between components that make up the Application Software Factory. The fourth section portrays both statistical and narrative descriptions of projects completed to date. Finally, the last section describes the future steps in ASF development.

## Software Factories: A Synopsis

The bulk of relevant literature does not use the term “software factory” per se but concentrates on a key software-factory attribute, reusability. Not limited to merely code reusability, reuse concepts apply to each life cycle phase: analysis, design, construction, testing, maintenance, and revision (Apte, et al., 1990; Bassett, 1987).

Typically, reusability will not occur spontaneously from “as-is” code. Attempts to treat software as standard inventory items fail. As Bersoff and Davis (1991) avow, such attempts “do not appreciate the fine grain of software, its inherent complexity, its degree of volatility, or the subtle and complex relationships that must be understood and recorded prior to making any change to it” (p. 105).

Software developers (including those involved in the ASF) tend to agree that the greatest reusability benefits stem from designing flexible components (Apte et al., 1990; Bassett, 1987; Kaiser and Garlan, 1987; Karimi, 1990). Such components are subsequently tailorable through application-specific parameters prior to code generation. In this manner, software development is similar to the legal profession in the way law and software development meld reusability from experience with evolution of circumstance (Gibbs, et al., 1990).

For business applications, several writers point out that reusability may be most successful with transaction processing systems analogous to the two ASF systems described in this article (Apte, et al., 1990). Such systems share sufficient commonality to make reuse practical (e.g., a deposit transaction is similar in both savings and money market applications).

Reuse of flexible design components may be counterproductive in some circumstances. Bollinger and McGowan (1991) critique the Software Engineering Institute's (SEI) process maturity model for assessing software productivity among defense contractors. The primary criticism is the model's emphasis on design-based code replication. For software development in the defense industry, Bollinger and McGowan believe that replication is more feasible for maintenance than design. Design activities have too many uncertain and novel factors to replicate between projects.

Some evidence exists that the U.S. lags behind Japan in the adoption of reuse-support tools (Cusumano and Kemerer, 1990) although competitive pressures are likely to thrust U.S. firms to adopt more reuse practices (Kolodziej, 1988). The lag may be attributed in part to programmer resistance. Apte, et al. (1990) found that programmer resistance was difficult to overcome, and Kolodziej (1988) describes the concept of programmer individuality in the U.S. as a cult-like norm. Moad (1990) attributes the problem to the lack of appropriate software management practices and standard development methodologies. As described later, the ASF approach concentrates as much on disciplined practices and standard methods as on reusability.

Concern exists on how the U.S. is faring compared to its international competition (particularly Japan) in the arena of software development. Cusumano and Kemerer (1990) pioneer in a quantitative comparison of U.S. and Japanese practices and performance in software development. Overall, the comparative study found more equivalence than difference. Sample Japanese and U.S. firms developed similar products, used similar languages, tools, and hardware platforms, employed personnel with similar experience, and achieved equivalent levels of code reuse, productivity, and equality. However, Cusumano and Kemerer caution that Japanese productivity statistics may be understated in this study because the U.S. had proportionately more transaction processing projects in the sample (the Japanese had more systems software projects).

Software factories are prevalent in large Japanese firms such as Toshiba, Hitachi, and NEC. Cusumano recently published extensive research on Japanese software factories (Business Week, 1991; Cusumano, 1989; 1991). He describes Japanese software factory components and compares them to American counterparts.

Cusumano points out that the term “software factory” has been used since the late 1960s in the U.S. and since the mid 1970s in Japan. Although the precise meaning of the term differs from country to country and between different organizations in the same country, a software factory generally connotes most of the tools and techniques shown in the five phases of Figure 1.

The central thought in Phase 5 is that there is value in approaching software development efforts with the engineering discipline usually associated with manufacturing. In changing software development from an art to a science, software engineering approaches generally entail (1) standardized methods and tools, (2) appropriate automated support, (3) disciplined planning, analysis and control processes, and (4) reusable, interchangeable code.

Returning to the Cusumano and Kemerer study (1990), data analysis found no significant difference in the amount of software reuse in Japan compared to the U.S. However, the Japanese reported more extensive use of coding utilities, automated flow charting, and reuse-support tools than did the U.S. firms. Thus, at least in the realm of reuse-support tools and design-automation tools, the Japanese appear to be further into the flexible automation phase of software-factory evolution (Phase 5 in Figure 1).

Cusumano (1991) notes that reliance on reusable code is probably a Japanese response to a shortage of programmers and a high demand for custom software. An emphasis on total quality techniques that support reuse of predefined and well-structured code yields a substantial proportion of the impressive productivity gains in the Celite systems projects, which are the subject of this paper. This reuse has been restricted to a limited set of functionally rich, generic shells that the ASF modifies to create unique and function-specific programs.

## Total Quality Approach

The ASF works through a combination of process flexibility and team discipline gained from a thorough team understanding of ASF principles and approaches. The process is self-constrained in that developers have very little latitude to make changes in one program that makes it arbitrarily different from other programs. The overriding philosophical stance on discipline is to first eliminate any unnecessary variation from program to program and then to reduce the necessary variation to its minimal expression. This is in contrast to traditional, artistic software engineering approaches that attempt to empower the programmer or analyst by making available all the capabilities that he or she might want to use.

Contrasting commonly used fourth generation languages and application generators demonstrates ASF flexibility. These tools impose similar discipline but are rigid about their constraints. If the overall requirements of the problem to be solved do not fit the preconceived notions of the tool builder, then the project becomes one of determining clever “work-arounds” to the tool. This phenomenon led Hallmark Corporation,

<table><tr><td>Phase 1: Basic Organization and Management Structure (mid-1960s to early 1970s)</td></tr><tr><td>Factory objectives establishedProduct focus determinedProcess data collection and analysis begun</td></tr><tr><td>Phase 2: Technology Tailoring and Standardization (early 1970s to early 1980s)</td></tr><tr><td>Control systems and objectives establishedStandard methods adopted for design, coding, testing, documentation, and maintenanceOnline development through terminalsEmployee training program to standardize skillsProgram libraries introducedIntegrated methodology and tool development begun</td></tr><tr><td>Phase 3: Process Mechanization and Support (late 1970s to present)Introduction of tools supporting project controlIntroduction of tools to generate code, test cases, and documentationIntegration of tools with online databases and engineering workbenches begun</td></tr><tr><td>Phase 4: Process Refinement and ExtensionRevision of StandardsIntroduction of new methods and toolsEstablishment of quality-control and quality-circle programsTransfer of methods and tools to subsidiaries, subcontractors, and hardware customers</td></tr><tr><td>Phase 5: Flexible AutomationIncrease in capabilities of existing toolsIntroduction of reuse-support toolsIntroduction of design automation toolsIntroduction of requirements-analysis toolsFurther integration of tools through engineering workbenches</td></tr></table>

## Figure 1. Software-Factory Process Evolution

© 1989 IEEE; reprinted with permission (see Cusumano, 1989).

which also uses a software factory approach, to totally exclude 4GLs from their factory (Johnson, 1991). Hallmark perceives 4GLs to be best suited for simple, non-integrated systems. To be fair, the above criticism applies to interpretative 4GLs geared toward report writing. Current 4GLs associated with ICASE products feature compilers and may be more flexible and adaptive to ASF requirements.

In contrast to 4GL tool work-arounds, the ASF builds architectures from the shells in concert with a predefined execution architecture. Essentially, the overall ASF architecture has enough flexibility to incorporate most, if not all, of the requirements in a disciplined subset of the target execution architecture.

Approaching system development in this manner required a significant paradigm shift on the part of the Celite team. Trusting that a module can be generated from a shell of reusable code changes the analyst's approach to the design of his or her modules. Steve McMillan recalls, "One of the biggest problems we had was getting our team leaders to become comfortable estimating programming effort in modules per day rather than days per module." As confidence grew, analysts found ways to improve and expand their use of the ASF, pushing it well beyond the expectations of the original ASF design team. By empowering the work team, members significantly improved their own work environment and productivity. Where it was not practical to generate unique or highly specialized code, analysts over-emphasized their effort in design checks, system tests, etc. If anything, the built-in quality of the ASF induced a sense of complacency regarding the program unit testing process.

Developing the Celite ASF was not solely a technological exercise. The technology of generating and reusing code is not enough to gain the productivity improvements that were achieved on the first two test projects. Through the application of total quality management (TQM) concepts to the entire development process, far greater gains were achieved than would be typically suggested by the technologies employed. The discipline, direction, and approaches that allow effective code reuse are the more central concern of the ASF.

The design team began building the ASF by deciding exactly what functionality would be supported and parameterized in the common generic COBOL shells. This was an iterative process beginning with postulation of a new shell function and a review of the functional requirements. Focus groups of analysts, programmers, and users then assessed how many of the requirements would be covered by the newly postulated shell's functions. They then determined what additional functionality the shells would require to accommodate most functional requirements. They also approached each "problem" requirement in reverse by asking how the expression of a given functional requirement could be resolved using standardized shells as defined.

The process of assigning functionality to a shell, called application packaging, was actually quite simple. There were only a few shells originally postulated so the shell builders could quickly assign the newly proposed functionality to an appropriate shell. Following this, the proposed assignment was reviewed with the appropriate focus group for confirmation and process impact assessment.

Following the use of total quality concepts in developing the ASF, Celite concentrated on building quality into the design and programming processes rather than on removing defects from the product through system testing. In the systems development context, process quality improvements included:

1. Eliminating any design or code that does not add real value to the final system functions.

2. Eliminating, simplifying, and then automating processes that could otherwise create flaws in testing or bugs in the finished system.

3. Testing and improving the process rather than the product (system). This not only eliminates errors (bugs) but also eliminates the opportunities to make those errors.

4. Emphasizing training, discipline, and consistent application of standards.

5. Empowering the entire team to build and improve the ASF rather than relying on a separate technical group of architecture builders.

6. Fostering a positive team approach to forestall perceptions of "bad" ideas or failures.

The ultimate goal of TQM applied to systems is “zero defect” programs. While no one believes that all defects will be eliminated, a quality orientation strives to get closer and closer to that zero defect point. Focus sharpens on continual improvements that will remove those last few defects in the process. This has become more important to the team than figuring out how to live with the defects.

Many typical business application programs need not be designed in the traditional form (with data flow diagrams or structure charts, etc). The truly unique aspects of an entire program can be defined by a small number of parameters. If any of those parameters change, the program can be redeveloped from those changes. Acknowledging this key requirement, Coad and Yourdon (1989) quote Gerhand Fisher, “We have to accept changing requirements as a fact of life, and not as a product of sloppy thinking” (p. 11). The advantage of designing modules by parameter is that unrelated design changes do not affect the subject module. A parametrically designed module can be redesigned and rebuilt easily; in most cases, automatically. In contrast, a conventional design approach mandates that each affected module must be redesigned or at least re-examined and retested. Steve McMillan attests, “The most profound change has been in maintenance effort. Enhancements that had been budgeted prior to the ASF are now completed within 10-20 percent of their original budget." Many more changes never make it to the IS department because the data driven architecture has turned what would have been coding tasks into user data maintenance.

The TQM principles “simultaneous engineering” and “concurrent engineering” suggest two things in the systems development environment. First, a function, subsystem, or module should not be designed in isolation from the process in which it will be created. Second, the process chosen to develop the system will influence its characteristics. In simultaneous or concurrent software engineering, the systems development process is defined simultaneously with the system design.

At Celite the execution architecture and the ASF shells were defined concurrently with the pilot application design phase. Once the process became solidified and consensus was formed that a particular shell was suitable for a large family of applications, additional applications were examined to determine if they could use ASF shells in an identical fashion without re-engineering. In building the shells, the goal was to remove excess code and excess processes without removing those that contribute value. The outcome was a simplified process for producing the product.

It is a difficult but necessary exercise in discipline to consolidate the design to a reduced number of generic modules, reusing as many as possible to create unique systems and subsystems. From a pure design standpoint, these reused parts may “suboptimize” the design. However, experience demonstrates that by reducing the total number of unique modules to be designed, coded, tested, and maintained, overall costs go down and quality goes up. In fact, in the TQM approach, code is probably the ultimate standardized “part” in that its reuse is virtually free.

Traditional approaches to automating software development attempt to empower the programmer by allowing many possible design combinations. In contrast, the Celite ASF development team rigorously examined the design and removed unnecessary unique options, features, and capabilities. What remained was a very small subset of required unique characteristics, which were then defined through standardized parameters. This small subset, in turn, easily defined potential problems in unit, system, and integration testing. Regarding the standardized approach, Bob Blewis, manager of distribution at Celite, comments, "Using the ASF gives us systems with consistency in look and feel without the usual design review and coordination effort. The ASF approach works because it is almost like designing one's own fourth generation language." The productivity gains are comparable to those possible in traditional 4GLs without the two common shortcomings to 4GLs—run-time performance and tool inflexibility.

In a traditional development environment, much of the detail design precedes programming because the act of detail design usually uncovers items that may affect programs already coded. Also, due to the time intensity of programming and testing, analysts usually establish a large backlog of work for programmers.

In the ASF environment business requirements continue to drive the development process. However, based on the Celite experience, it is counterproductive to draft screens and reports too early in the design process. Following ASF standards, Celite analysts can now reduce technical design, module packaging, and detail design to a simple one-step cognitive process. The analyst builds on the functional information needs as described in the business requirement, uses data normalization and abstraction to properly structure the data, and then easily identifies the shell type and parameters to be used.

## Components

At Celite, the current implementation of the ASF is a combination of (1) technical and application architectures, (2) tools to automate and/or integrate the development environment, (3) reusable code, and (4) methods and approaches. Application shells rest on top of the underlying hardware architecture for this specific installation, which is Digital Equipment Corporation's VAX hardware platform combined with Digital's relational database Rdb. On top of that is the Andersen Consulting CASE product, FOUNDATION, which includes the PC-based design tools called Design/1 and development and run-time architectures referred to as Install/1 (Foundation I/1 VAX) (see Figure 2).

A small technical architecture team at Celite quickly defined the initial hardware and technical software architecture, which included the selection of the DBMS, CASE tools, and approved languages. The task of building the Application Software Factory and formalizing the methods described in this article was assigned to the first major custom application project to ensure that it met developers needs and was not driven primarily by technical considerations.

Self-imposed constraints are needed to properly define the effective use of the architectural components. By using the conversation context-management features found in Install/1, ASF operates in a more standardized manner than a typical custom online system. In the ASF, one overall context map is sufficient for an entire application rather than a unique map created by programmers (or analysts), for each module or subsystem. All conversations share this map, which contains references to all the primary key accesses to all the tables in the application. Because of this common agreement on the standard linkage between all conversations and all online programs within an application, key features in the reusable code are available to all conversations.

For example, one feature is automatic, user-directed, context-sensitive navigation. From any of the scrollable or selectable screens, a user can select a field or a line and strike a function key to go to another screen. The reusable code grabs the keys of the related line, carries them through the context area, and restarts the next program using that context information. This facility automatically provides a built-in “drill down” capability not commonly found in many transaction systems. More importantly, it allows reuse of entire programs in multiple conversations without custom definition or coding of the interface between the modules. The external interface of every program looks the same to all other programs, making it possible to reuse unique function modules anywhere in the system without modification.

In reverse, this same facility serves as a simplified form of “sticky” cursor cut and paste. A user can easily navigate through several screens, select an item, return to a maintenance screen, and apply the selected key into the field from which he or she exited. The consistency of the application impressed the users at Celite. Bob Blewis recalls, “The users’ initial reaction to the QC [quality control] system was amazement that there was so little variation in the look and feel of the system from one end to the other. This undoubtedly reduced training costs and accelerated absorption of the system.”

![](/api/attachments/FMDFFW5N/fulltext/images/1bb3fadbb432b7ee9798fb11047ea1aac3f01271f7bbae353bae90580bece761.jpg)  
Figure 2. ASF Hardware Configuration

A design standard of one program per screen allows reuse of programs several times throughout the system. However, while this type of reuse can significantly reduce the total lines of code (LOC) required, it does not actually show up in the productivity statistics. The productivity gain from this type of code reuse is not counted since a program is compiled only once, and productivity statistics are based on LOC generated. In function point analysis this form of reuse clearly shows up in productivity statistics.

Other major architectural elements are modularization and heavy reliance on database trigger and constraint procedures. “Triggers and constraints” is a relatively new relational database facility that allows designers to attach procedures to the database in such a way that they are guaranteed to be executed with a particular type of access to a given table. This facility moves the most complex data navigation and data checking code, traditionally coded into applications, to the database. This simple movement significantly reduces program complexity and also contributes to the reduction in system test time.

Using these features has the effect of standardizing and automating data integrity rules, relieving the application code from needing to ensure integrity. Among other things, a traditional system test creates conditions that attempt to prove that certain combinations of events will not give rise to data integrity problems. Using triggers and constraints, the ASF integrity mechanisms are not spread across many separate programs operating on the same data, but rather are contained in a single procedure that controls that data. Thus, the possible combination of many data integrity events has been reduced to one atomic event and consequently is very easy to test. A later section of this paper describes the next generation of tools that are possible now that the development processes have been simplified and standardized.

Additionally, trigger and constraint code is reused but not recounted. Every program that accesses the table uses the same routines. Again, there is no easy way to count the degree to which that reuse comes into play. Project experience suggests there is a 10 to 30 percent reduction in total code size using the following techniques.

\- Common routines are brought into application programs automatically through the use of the field name as a parameter.

\- The macro substitution process brings in common copybook logic without the programmer being aware of it.

\- The five generic shell programs represent the greatest level of reusability. They consist of 3,000 to 12,000 lines of COBOL code.

Developing a program is a process of applying each of the parameters in the functional specification to the generic shell program using the appropriate predefined edit macro. This process changes the generic shell into a custom application program with very specific and rich behavior. Another macro then removes any predefined code that was not necessary to achieve those specific functions. In most cases little or no extra work is needed to successfully compile the program.

Install/1 provides a number of design and programming tools as well as a well-architected runtime environment. At Celite the design team created additional tools tailored to its own self-imposed constraints. One of the simplest and most useful tools is a set of edit macros designed to replicate input parameters repeatedly through reusable generic shell code. Thus, the ASF uses a generic shell program to produce a specific application module. Additional tools aid in the process of building conversations out of individual modules and assist in configuration management and change control for the project. Celite has intentions of applying the tools and concepts to other environments. McMillan says, "In the future, we expect the ASF's layered architecture to ease cross-platform migration, including possible movement to a Unix environment."

## Project Description

Experience to date with Celite's ASF includes two medium-sized systems implemented at two different geographical sites. The ASF was piloted on these applications to test and refine the concepts. The first project completed under this approach was a quality control (QC) application for a process manufacturing operation. The other was a warranty system for tracking activity on the warranties of a product that has a very long field life. The QC system consists of approximately 250,000 lines of COBOL code in 60 modules, and the warranty system has 210,000 lines of COBOL code implemented in 50 modules. Both systems incorporate a relational database.

Table 1 shows the productivity statistics from these two projects. Table 2 compares project statistics with current norms for this type of transaction-based business application.

Of the 250,000 lines of delivered code in the QC system, 248,000 were generated from pretested shell modules. Thus, 99 percent of this system is “untouched by human hands.” Statistics are not available for the warranty system, although that system had more custom code, which promulgated more post-conversion errors. The actual code-generation mechanism is quite straightforward.

Overall, while the results from the pilot projects indicate dramatic reductions in development time, unit test time and especially system test time generated even greater reductions. Reusable parts are very predictable once programs pass their initial tests. Unless analysts circumvent the ASF and include additional custom code, there is very little that can go wrong in a system test. If the process is followed, problems usually found in a system test will be avoided and can only be reintroduced by deliberate actions of the team.

The high percentage of generated code has had a predictable beneficial effect on overall system quality. As Table 3 shows, emphasis on the quality of the process resulted in no bugs in the system test and only one bug uncovered during the first 90 days of operation. A bug, in TQM terminology, has a broad definition and involves more than just an abnormal program termination or a violation of a particular functional specification condition. Rather, a bug is any occurrence where the output of the system does not match the user's functional specification or the designer's intention.

Table 1. Productivity Statistics for Completed Projects

<table><tr><td></td><td>QC</td><td>Warranty</td></tr><tr><td>Number of modules</td><td>60</td><td>50</td></tr><tr><td>Lines of code</td><td>250,000</td><td>210,000</td></tr><tr><td>Days detail design</td><td>114</td><td>74</td></tr><tr><td>Days Programming</td><td>87</td><td>248</td></tr><tr><td>System test days</td><td>20</td><td>44</td></tr><tr><td>Days technical support and architecture building</td><td>150</td><td>81</td></tr><tr><td>Errors found in system test or post conversion</td><td>1</td><td>53</td></tr></table>

Table 2. Comparison of Software Factory Statistics to Traditional Norms

<table><tr><td></td><td>SW Factory (Range)</td><td>Traditional</td></tr><tr><td>Lines of code per day</td><td>862–2,873</td><td>200</td></tr><tr><td>Days per module (programming)</td><td>1.5–5.0</td><td>20</td></tr><tr><td>Lines of code per day (all dev)</td><td>478–673</td><td>50</td></tr><tr><td>Errors per 1,000 LOC</td><td>.01–.25</td><td>4.4</td></tr></table>

Table 3. Change Requests Since System Implementation (QC Project)

<table><tr><td>Program “bug” (original system)</td><td>1</td></tr><tr><td>Program “bug” (maintenance)</td><td>1</td></tr><tr><td>New features</td><td>4</td></tr><tr><td>Usability</td><td>12</td></tr><tr><td>Performance</td><td>2</td></tr><tr><td>Dropped requests</td><td>4</td></tr></table>

This particular system test bug occurred in a combination of conditions that the analysts had not considered and was in one of the very few custom-coded subroutines added into a program generated from reusable code. The lesson in the ASF environment is that custom code should be avoided wherever possible. If design and ASF capabilities do not eliminate the need for custom code, then the ASF capabilities and processes should be re-examined. It may be necessary to modify the factory (the process) to ensure that it meets the needs of the design team. This happened numerous times during the initial projects, but as the ASF grew it became possible to continually hit a standardized code reuse level in excess of 90 percent.

A marked improvement in the consistency and quality of delivered code produced an unexpected side benefit for users. Screens and user navigation behave identically from conversation to conversation throughout the entire system because they are implemented only once in the generic shells and reused. Additionally, this approach enhances maintainability of the system. Steve McMillan comments, “Every system generated by the ASF has the same technical architecture making it easier to implement technical upgrades across all systems. Since almost any program can be created in a day, very few maintenance tasks take longer than one day per affected program. Most take far less.”

By drastically reducing the elapsed time to produce modules, many other problems just "go away." For example, design changes in a traditional development environment are deadly because they can affect so many modules that are in partial states of completion. If the programming cycle time is reduced to a day or less, there is very little “work in process” and thus very little work is exposed to design change.

Through simplification of data design (triggers and constraints) and over 90 percent reuse of code, the ASF reduced complexity and increased programmer communication. As Coad and Yourdon (1989) explain, “the analysis challenge requires effective communication” (pp. 10-11). Software methods are effective only to the extent that they help people communicate with one another. Five shells covered all the functionality, and no one shell had much functional complexity. This allowed team members to internalize most of the commonly used design options. Internalization created a very effective shorthand communication vehicle.

This approach prompted a cultural change. The team turned away from solving system problems by designing and implementing unique and complex code to using an approach that rewarded the reduction of a design problem to a simple, standardized, and reproducible solution. In turn, simplification was encouraged as a design goal.

The ASF approach has changed the mix and timing of skills on a project. There is very little in the design process where a design change can affect modules already completed. The act of performing detail design is not likely to turn up additional change requests because there is so little involved in the process of detail design. Also, the process of coding generally takes no longer than the design process. It is quite feasible to have a team of only programmer/analysts who develop their own specifications and then code them. The similarity of the modules naturally leads to a standard approach to unit testing. Because programmers have very little latitude in changing code, there is very little they can or should test that was not already thoroughly tested when the generic shells were originally developed.

Perhaps one of the biggest changes in approach and methodology has been a paradigm shift in terms of the effort required to manage a project of this size. Steve McMillan points out, “Unless project managers fully understand the implications of this, there is a tendency to overburden the project with more control mechanisms, status, supervision, documentation, etc., than is necessary. The level of control needed to manage a project is not a function of the size of the system, but the size of the team.” A project that typically would take 50 or 60 people can now be concluded in approximately the same timeframe with a team fewer than a dozen.

At Celite another large-scale application is under development and targeted for 1992 completion. This system will be used to manage process manufacturing operations, and encompasses production scheduling, inventory control, warehousing, shipping, traffic, customer service, order entry, and billing. Current expectations forecast about 2 million lines of COBOL source code. Several other projects are in the planning stages as the ASF is extended to meet the majority of Celite's remaining non-packaged transaction systems needs. The productivity gains of the ASF have actually increased the number of systems that can be implemented on a custom basis versus a packaged solution, which may be far less than a perfect fit to defined requirements.

## Next Steps

Specific plans are in place to begin formalizing the approach, methods, and training materials. These steps are some of the most important for the large-scale roll out. Up to now, projects unfolded through interpersonal communication and placement of trained personnel on multiple projects using the technology described earlier in this article. Currently, the functional specification development process and programmer processes are documented in great detail. However, it is the more general and abstract elements of the approach that present the greatest challenge in replicating the ASF. To address this issue, training sessions describing the techniques of data normalization and abstraction, disciplined application design using application shells, and concepts of standardization and reuse are being created to solidify the approach and methodology.

Subsequent projects will expand the ASF to encompass additional system development processes. Current strategy includes additional plans for tools to aid version, migration, and configuration management. Also included in beta implementation is an AI-based functional specification composer and compiler. AI technology may also be applied to the problem of creating representation test data values and volumes. In addition, there are plans to enhance the performance and functionality of the existing application shells. From there, work will move “backwards” into the system planning requirements gathering and data design aspects of system development using Andersen’s Plan/1 system planning tool. The ASF has attacked and solved a large part of the problem. Yet, that merely makes other aspects of the problem larger now by comparison, and therefore targets of future development.

## Conclusion

Successful Application Software Factories to date have included a high degree of code reuse, improvements in quality, and increased flexibility. Reusable code furnished 99 percent of the total code for the QC project. Quality improvements mandated a new metric, since the ASF approach now allows defects to be measured in “parts” per million rather than “parts” per thousand. Further, project teams have achieved these levels of productivity in a CASE and COBOL, transaction-oriented environment.

Two aspects of the ASF have significantly increased development flexibility. First, through the use of an intelligence database with triggers and constraints (objects), programs have far fewer internal data integrity references. Thus, data maintenance is easier and users can change data management and integrity rules without IS involvement. Second, because the ASF is an approach rather than a rigid tool, the methods and development tools readily transfer to other application environments.

Currently much interest continues in Japanese software factory developments (Business Week,

1991; Cusumano, 1991). The ASF projects, developed and in progress, demonstrate that the Japanese productivity gains can be eclipsed by the adoption of these methods. Simplification, conceptual integrity, adherence to standards, and selective automation in the development process generate impressive results.

## References

Apte, U., Sankar, C.S., Thakur, M., and Turner, J.E. "Reusability-Based Strategy for Development of Information Systems: Implementation Experience of a Bank," MIS Quarterly (14:4), December 1990, pp. 421-433.

Bassett, P.G. "Frame-Based Software Engineering," IEEE Software, July 1987, pp. 9-24.

Bersoff, E.H. and Davis, A.M. "Impacts of Life Cycle Models on Software Configuration Management," Communications of the ACM, August 1991, pp. 104-117.

Bollinger, T.B. and McGowan, C.M. "A Critical Look at Software Capability Evaluations," IEEE Software, July 1991, pp. 25-40.

Brooks, F.P. "No Silver Bullet," IEEE Computing (20:4), April 1987, pp. 10-19.

Business Week. "Now Software Isn't Safe From Japan," February 11, 1991, p. 84.

Coad, P. and Yourdon, E., Object Oriented Analysis, Yourdon Press, Englewood Cliffs, NJ, 1989.

Cusumano, M.A. "The Application Software Factory: A Historical Interpretation," IEEE Software, March 1989, pp. 23-30.

Cusumano, M. A. Japan's Software Factories: A Challenge to U.S. Management, Oxford University Press, New York, NY, 1991.

Cusumano, M. A. and Kemerer, C.F. "A Quantitative Analysis of U.S. and Japanese Practice and Performance in Software Development," Management Science (36:11), November 1990, pp. 1384-1406.

Gibbs, S., Tsichritzis, D., Casais, E., Nierstrasz, O., and Pintado, X. "Class Management for Software Communities," Communications of the ACM, September 1990, pp. 90-103.

Johnson, J. The Software Factory: Managing Software Development and Maintenance, 2nd Edition, QED Information Sciences, Inc., Wellesley, MA, 1991.

Kaiser, G.E. and Garlan, D. "Melding Software Systems from Reusable Building Blocks," IEEE Software, July 1987, pp. 17-24.

Karimi, J. "An Asset-Based Systems Development Approach to Software Reusability," MIS Quarterly (14:2), June 1990, pp. 179-200.

Kolodziej, S. "Software's driving force," Computerworld, October 5, 1988, pp. 31-37.

Moad, J. "The Software Revolution," Datamation, February 15, 1990, pp. 22-30.

Software Maintenance News, February 2, 1991.

## About the Authors

Kent Swanson is a partner at Andersen Consulting in Denver. He received a B.S. from the University of Minnesota in 1967 and an M.B.A. from the University of Chicago in 1969. In the same year he joined the firm of Arthur Andersen & Co. Since then he has worked exclusively in Andersen's Products Industry Group. Mr. Swanson has been primarily engaged in the design and installation of systems covering the manufacturing, materials management, distribution, logistics, and customer support functions. He has also supervised numerous total quality productivity projects for the firm's manufacturing and distribution clients. The Application Software Factory was developed for one of those clients and accorded him the opportunity to apply the quality and productivity techniques normally associated with the production environment to software development.

Dave McComb is vice president of research and development for Micro Planning International, Denver, CO. Prior to joining MPI, he was a consultant for 14 years, first with Arthur Andersen Consulting and then with First Principles. Dave was the chief architect of the Application Software Factory.

Jill Smith is an assistant professor of MIS in the College of Business Administration at the University of Denver. She obtained her Ph.D. in business computer information systems at the University of North Texas. She is also a research associate in UNT's Information Systems Research Center. Dr. Smith's research interests include information systems productivity issues and organizational change issues accompanying

IS implementation. She has published previously in the Journal of Management Information Systems, Information and Management, and the Journal of Information Systems Management.

Dan McCubbrey is chair of the MIS Department at the University of Denver. He is also director of the Colorado Advanced Software Institute, a technology transfer program of the Colorado Advanced Technology Institute. Prior to joining the University of Denver faculty in 1984, he served as a partner with Andersen Consulting, Arthur Andersen & Co. He is co-author of Foundations of Business Systems and department editor for cross-cultural issues of International Information Systems.

## Subject Index for Volume 15

## APPLICATION

Executive Information Systems: A Framework for Development and a Survey of Current Practices
Hugh J. Watson, R. Kelly Rainer, Jr., and Chang E. Koh ..... No. 1, pg. 13
Applications of Global Information Technology: Key Issues for Management
Blake Ives and Sirkka L. Jarvenpaa ..... No. 1, pg. 33
Executive Information Requirements: Getting It Right
James C. Wetherbe ..... No. 1, pg. 51
On Information Systems Project Abandonment: An Exploratory Study of Organizational Practices
Kewku Ewusi-Mensah and Zbigniew H. Przasnyski ..... No. 1, pg. 67
Identification of Strategic Information Systems Opportunities:
Applying and Comparing Two Methodologies
Francois Bergeron, Chantal Buteau, and Louis Raymond ..... No. 1, pg. 89
Career Orientations of MIS Employees: An Empirical Analysis
Magid Igbaria, Jeffrey H. Greenhaus, and Saroj Parasuraman ..... No. 2, pg. 151
Key Information Systems Management Issues for the Public Sector
Sharon L. Caudle, Wilpen L. Gorr, and Kathryn E. Newcomer ..... No. 2, pg. 171
An Applied Framework for Classifying the Complexity of Knowledge-Based Systems
Marc H. Meyer and Kathleen Foley Curley ..... No. 4, pg. 455
Information Systems Management Issues in the 1990s
Fred Niederman, James C. Brancheau, and James C. Wetherbe ..... No. 4, pg. 475
Educational Needs as Perceived by IS and End-User Personnel:
A Survey of Knowledge and Skill Requirements
R. Ryan Nelson ..... No. 4, pg. 503

THEORY AND RESEARCH
Decisional Guidance for Computer-Based Decision Support
Mark S. Silver ..... No. 1, pg. 105
Personal Computing: Toward a Conceptual Model of Utilization
Ronald L. Thompson, Christopher A. Higgins, and Jane M. Howell ..... No. 1, pg. 125
Is Office Productivity Stagnant?
Raymond R. Panko ..... No. 2, pg. 191
Executive Involvement and Participation in the Management of Information Technology
Sirkka L. Jarvenpaa and Blake Ives ..... No. 2, pg. 205
A Model of Users' Perspective on Change:
The Case of Information Systems Technology Implementation
Kailash Joshi ..... No. 2, pg. 229
A Model for Measuring Information System Size
Clive D. Wrigley and Albert S. Dexter ..... No. 2, pg. 245
