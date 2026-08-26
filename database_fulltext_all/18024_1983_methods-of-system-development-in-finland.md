---
otero_id: 18024
otero_key: "XR5Z3RG9"
title: "Methods of system development in Finland"
authors: "Eija Korpela"
year: "1983"
journal: "Information & Management"
doi: "10.1016/0378-7206(83)90002-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Methods of System Development in Finland \*

Eija Korpela \*\*

University of Helsinki, Department of Computer Science, Tukholmankatu 2, 00250 Helsinki 25, Finland

Interest in the use of different methodologies, methods and tools for information systems analysis and design has been increasing for the last decade in Finland. This has resulted in the founding of a special interest group in systems analysis and design within the Finnish Data Processing Association and in its making a survey of the methods and tools in use in Finland in 1980. This survey was in the form of a questionnaire mailed to the company members of the association. The results of the survey show a wide use of different tools in the design and implementation of information systems. In the analysis phase, there seems to be a need for more and better methods and tools. In 1980 several companies began to use new methodologies, methods and tools in the field; the most common are: the Swedish ISAC, Jackson's JSP, and the data dictionary.

Keywords: method, methodology, technique, administration of information systems, systems analysis and design, implementation, testing.

## 1. Introduction

In the past two or three years there has been considerable increase in interest in Finland in methodology to aid in the early phases of the system development process. The reason for this interest lies in the outcome of the process: the system itself. Maintenance seems to require an increasing share of the ADP-department's time, leaving less for development of new systems. The most effective cure for this seems to be found in the early phases; by paying more attention to the requirements of the user and the modifiability of the system, the maintenance load should be kept under control.

For the purpose of sharing ideas and spreading knowledge in this area, a special interest group, the Systems Analysis and Design Club (SYTYKE), was founded in 1979 within the Finnish Data Processing Association. In order to provide a solid basis for its work, the club formed a working group to survey the methods and tools in use in Finland.

The results of the survey, presented here, were not too surprising. In the early life cycle phases (feasibility analysis and systems analysis) only a few companies use formal methods and techniques. This was felt to be a problem; formal methods and techniques are needed. New systematic methods could be expected to help in the communication between the user and the ADP personnel.

![](/api/attachments/XR5Z3RG9/fulltext/images/7a75afc8be5e0ca1988159ff5517a03212b5fa524bc87cc139ab6d2bc200f7a1.jpg)  
tion and the Systems Analysis and Design Club (SYTYKE) and the Office Automation Club within the same association.

The club decided to have the results published and a report was written in the winter 1980–81. Also the club decided that a similar survey should be made in five years time.

## 2. The Survey

The working group consisted both of doers and of thinkers – including representatives from a major bank, an insurance company, a governmental technical research center, a college-level ADP institute, and the department of computer science at the University of Helsinki.

The survey was made by mailing a questionnaire to the 485 company members of the Finnish Data Processing Association. Questionnaires were returned by 167 (34%) of the companies. This can be considered satisfactory, since several of the members have no systems development or commercial data processing operations. The timing may have reduced the response, since the questionnaires were mailed in May; also the extensiveness of the questionnaire (61 questions) may have had a negative effect. In general, the respondents returned the forms in time and had a favourable attitude to the survey.

The companies that took part in the survey were mostly large (large in the Finnish scale: over 1000 employees or the annual turnover over 100 million dollars in 1979). The main areas of business were industry and commerce.

The applications made in these companies are mostly conventional business or engineering applications. The top five mainframe manufacturers are IBM, Digital Equipment Corporation, Hewlett-Packard, Honeywell and Data General, in this order.

## 3. Controlling Information Systems Development

In most of the companies, users are participating more and more in the systems development. In two thirds of the companies, the systems development effort is distributed throughout the user departments. One quarter of the companies still believe in concentrating the job in the ADP department. Cooperation between users and ADP appears to be a problem and it is probably one of the major factors to be considered when developing and choosing methods for systems development.

Most of the companies (83%) use a model to structure the work. Most of the respondents stay with domestic thinking, and use either the “Building Model” of the ADP-Institute and Finnish Data Processing Association or the “Phasing Model” of the State Computer Center, VTKK. The Phasing Model is an ordinary five-phase model, which has its equivalents in most countries. The Building Model, published in 1975, is a four-sector model (the sectors are activity content, information content, manual solution and ADP solution), each sector containing certain tasks to be performed. There is a precedence order between the tasks that bind the model together. The reason for the wide use of these two models lies in their being taught at both the college-level ADP-Institute and computer science departments in most Finnish universities.

In order to determine the number of phases and the amount of work in different phases, the companies were asked to state which phases were used and the relative amount of work in each phase. The answers were then fitted into a six-phase model, which also includes maintenance. The outcome of this appears similar to the results in other countries. The amount of maintenance does not depend on the amount of systems work in the company and is generally 36% to 45%, with an average of 41%. In some companies, it was stated to be more than 90%.

![](/api/attachments/XR5Z3RG9/fulltext/images/06a4d3efe00a0adc5dd894fc2d77b560b4986b75c881599ae6cac1c994dcb16a.jpg)  
Fig. 1. The distribution of effort in the various phases of the system life cycle.

The quality of the data processing systems is controlled during the systems development by checking the documents produced between the phases (60%). Structured walk-throughs are used in 34% of the companies. The quality of the data processing systems is controlled during production generally by collecting user comments and complaints (87%), following the amount of maintenance (50%), collecting error statistics (47%), making time measurements (45%) and following costs (44%). If the quality is being controlled, several methods are normally used. The quality is not controlled in 4% of the cases.

## 4. Feasibility Study

The initiative to develop a data processing system is mostly made by the users (58%). Half of the companies make long range studies to define which systems should be developed in the long term. These studies are usually made every 3 to 5 years. Among the methodologies are: Change Analysis of ISAC, METO (a Finnish methodology) and BSP (Business System Planning of IBM). In general companies use no specific methodology for making this overall study (67%).

The feasibility study is made either according to the company's own instructions (41%) or there are none at all (48%).

## 5. Systems Analysis

The questionnaire mentioned three methodologies for analysis, HIPO, ISAC, and SADT. HIPO is an IBM description technique mainly used for program design, but also for systems analysis and design. It has been tried in seven companies, but it is generally not preferred. SADT is a U.S. methodology, developed by D. Ross in the SofTech Inc.. It is considered good especially in engineering applications. Its use is emitted by the expense of the licence and the high initial threshold in learning the language. By now, SAAT might be being accepted; it has been widely discussed and referenced and is probably more widely used than in 1980.

![](/api/attachments/XR5Z3RG9/fulltext/images/97c63106d4a0c46feec0af0c924bc89edeac3d4943dfad27bf9aca9c8bfa775f.jpg)  
Fig. 2. Usage of different methodologies in systems analysis.

The Swedish ISAC is the most common of the structured methodologies. Its wide use is probably due to its availability. Lundeberg's precedence analysis technique has been taught for several years and now presumably all educational institutions in the field give some kind of training in the whole methodology. Written material is also ample. A major ADP service company started using a modified version of ISAC in 1977–78 and has also organized courses in it.

The use of ISAC has not been without controversy. It is considered better than nothing but also criticized; for example, the maintenance of its graphs is cumbersome and there are no automatic tools to assist in it; the methodology is not algorithmic, so it gives no guarantee of the quality of the result. People involved in the project are not always willing and committed to using the methodology. There are still problems in the communication between the ADP personnel and the users and there is no smooth transition to structured programming built into the methodology.

A tool that was ignored in our survey, but has a wide-spread use, is the wall-chart. A favorite approach nowadays seems to be to have a “war-room” with charts of the requirements analysis and the conceptual analysis on the walls, completed with photos, forms and other objects of the system to be analysed.

In general, 10% are satisfied, 50% are fairly satisfied, and 40% are not satisfied with their analysis and design methods. The greatest deficiencies and problems are the absence of systematic methods (36%), the cooperation between users and ADP personnel (20%) and deficiencies in the documentation system (9%).

## 6. Systems Design

In systems design, the manual tasks have received much less attention than the computerised ones. This situation will very likely change as more attention is now paid to the man-machine interface and work design in general. At present, only 20% of the companies have a guide for designing manual tasks.

In describing the terminal dialogouses, there is a documentation standard in 31% of the companies. But seldom is one documentation technique (design technique) enough. On different levels of detail a different technique is needed. A program tool for designing terminal dialogues is used in 30% of the companies.

Centralised data management is becoming more and more common in the companies. A database management system is used in 54% and a data dictionary in 25% of the companies. In several companies, the data dictionary will be the next tool to be taken into use. For designing a database, 18% of the companies use a systematic method.

The most common database management systems are IBM's DL/1, Cullinane's IDMS, Honeywell's IDS, Hewlett-Packard's IMAGE, IBM's IMS and Cincom's TOTAL. The most common data dictionaries are Cullinane's IDD, a self-made data dictionary, and MSP's Datamanager.

When inquiring about program design methods used. IPO (Constantine et al.), JSP (Jackson's

![](/api/attachments/XR5Z3RG9/fulltext/images/e6ef5dc5ea3a6b640d612542896255b1d391fa076646729d3bc73b4d96d927a8.jpg)  
Fig. 3. Usage of different methods in the program design.

Structured Programming of Michael Jackson), and LCP (Logical Construction of Programs of Warnier and Orr) were mentioned. JSP is by far the most common, although many companies have only used it by way of experiment and do not use it as a standard. LCP is the least known method: one quarter of the respondents do not know it by name. Methods developed by the companies themselves and other methods mentioned were: modular programming, HIPO, decision tables, program skeletons, pseudocoding, and flow charts.

Among the problems and deficiencies mentioned were: a lack of a systematic method (26%); problems with maintenance (26%); applying the methods used (20%); and the variations in the tasks to be designed (17%). The users of IPO are unsure whether it can be applied for interactive programs. The users of JSP have problems in applying the method and maintaining the descriptions; they feel a need for automated tools.

On the average, 20% of the systems consist of commercial packages. Every tenth company uses more than 75% bought software in their systems. Only three percent of the companies rely on their own systems designers for all their software.

## 7. Programming

In programming, Finnish programmers aim at modularity, good structure, and top-down development. Tools most frequently mentioned were generalized (parametrised) modules and program skeletons combined with terminal programming. Only 9% of the companies do not use any tools in programming. Among the products mentioned were ROSCOE (ADR), CICS (IBM), TI-Cobol (a Finnish Cobol-preprocessor), Vollie (ADR), Easytrieve (Pansophic Systems Inc.), and TSO (IBM). For documenting the programs, one third of the companies use an automated tool.

![](/api/attachments/XR5Z3RG9/fulltext/images/6aa8092409fe8835b88ed1b8ab070b9e6aeedacfd22ec05567f9a84e38f558e7.jpg)  
Fig. 4. Usage of programming languages.

Cobol is the most common of the programming languages. Usually companies use more than one programming language – three is the most common number. This number is clearly correlated to the amount of system development. Other languages not mentioned in the chart are Cobol-related Databus, RPG-related CPG and other very high level languages. The interest in ADA has been considerable and the Finnish computer manufacturer Nokia will soon introduce a model based on ADA.

![](/api/attachments/XR5Z3RG9/fulltext/images/170be99b38059fdcd6c1e427b5cba69132cf4ccb0299faac49f1414629edeb8d.jpg)  
Fig. 5. Calculation of the index of usage.

For program and module testing, the most common tools are test data generators, test result comparators, bug tracing programs, and the traditional program dumps. Optimizer III (Capex Corp.) is the most common tool. Despite the tools, testing is still felt to be “hit and miss”. The effort that seems to be needed most is in improved planning of the testing procedures and the test material.

## 8. Developing and Choosing and the Methods

At the time of the survey, most companies were introducing a new method or tool. The most frequent ones were ISAC, JSP, and the data dictionary. The amount of work needed in modifying the methods for the needs of the company was not surveyed.

In choosing and developing a new method, the aim is to develop better quality systems. The costs and the end-user participation are also important. In choosing a method, the decisive factor is the experience of other companies.

## 8. Conclusion

The peak of enthusiasm seems to have passed by now in the systems analysis area. Companies have gained valuable information and experience in the methods. The large companies that were installing new methods in 1980 may still be doing that due to organisational inertia. Smaller companies seem to be faster in adapting and are perhaps using more developed tools.

According to ms. Terttu Pulkkinen, head of the research department of the ADP-Institute, the main questions are now:

\- What is the relationship between the traditional phase-oriented systems development methods and the new prototype approach?

\- How do we manage information and data? Who is responsible for the data resource? Who is allowed to use the information?

\- In what ways can the design of the end users'

work be better considered?

How can responsibility for the project be transferred to the end-users and how can the end-users become more involved in the system development process?

How can traditional data processing be efficiently combined with text processing and the other fields of office automation?

The results of the survey in 1985 will give insight into how these have been treated in Finnish companies.
