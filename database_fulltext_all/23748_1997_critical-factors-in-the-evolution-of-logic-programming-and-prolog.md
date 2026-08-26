---
otero_id: 23748
otero_key: "FG3R6N2G"
title: "Critical factors in the evolution of logic programming and Prolog"
authors: "K Darby-Dowman; J Little"
year: "1997"
journal: "European Journal of Information Systems"
doi: "10.1057/palgrave.ejis.3000255"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Criticalfactorsintheevolutionoflogicprogrammingand Prolog

K Darby-Dowman and J Little

Department of Mathematics and Statistics, Brunel University, Uxbridge, Middlesex UB8 3PH, UK

Logic programming has received much critical attention over the past two decades from both a language perspective and as a methodology for practical problem solving. This paper presents a historical foundation of the approach and examines the development of Prolog since its firs implementation. An analysis of the use of Prolog in commercial, research and teaching environments shows that there is an established base of users and that, after a period of rapid growth, the language currently enjoys continuing activity. The key to its success so far is due to its continuing evolution by including features that were not seen as being within the original concept as a pure logic language. Significan features which have contributed to the success of Prolog include integration with other languages, object oriented extensions, constraint representation, parallel execution as well as improved speed and robustness. Applications databases are analysed with respect to type of application, system status, type of developer, hardware platform, country of origin and the Prolog implementation used. Factors contributing to the success of Prolog are identifie and likely future developments are explored.

## Introduction

Logic programming may be define as a representation of a ‘form of logic’ in a computer language. In particular, the logic is made up of logical statements and a deductive mechanism to operate on them. A computer language can represent these aspects by having a syntax similar to the logical statements and an execution process simulating the deductive mechanism. Many real life problems, particularly combinatorial problems, can be expressed in a logical framework. Logic programming, with its ability to apply the principles of logic on a computer, provides an opportunity to efficientl solve these hard problems.

The three main streams leading to the evolution of a logic programming language are the representation of the logic, the deduction mechanism and computing technology to implement it. Taken together, these influence contributed to the creation of a language which was sufficientl expressive to allow deductions to be made over large sets of axioms in acceptable execution times on available hardware platforms. Prolog is the most common and widely accepted implementation of a logic programming language and exhibits many unique characteristics over other languages.

Prolog differs from existing languages by having a declarative logic-based syntax and an in-built inference engine that performs searches to evaluate the validity of a logical proposition. This level of abstraction allows the program developer to concentrate on what the problem is in terms of its logical representation, rather than how the problem is to be processed in the program. For example, memory management and argument typing, both part of many lower level languages to improve the efficienc of compilation and execution, are absent from the Prolog language. Prolog has achieved greatest success on problems which are difficul to formulate in a way suitable for processing by known algorithms, or where the size of the problem makes such an approach impractical. For example, problems arising in planning, scheduling and expert systems (AALPS, 1993; ACAPS, 1993; CAPS, 1993) are among those in which Prolog has been used with success. In general, the problems on which Prolog has most success are those that are difficul to model using traditional approaches, yet can be modelled declaratively in a logic framework. Prolog also has, in practical terms, a capability to add and remove dynamically extra code in the development cycle without having to re-compile or re-link as with conventional languages. As a result, the development cycle is shorter, and therefore Prolog is considered to be an excellent rapid prototyping language.

Prolog is not only suitable for specifi types of problems; its syntax contains general programming features such as formatted input/output and mathematical functions. For this reason, Prolog can be used for all aspects of an application.

In summary, Prolog is considered to be a good language for rapid prototyping and in representing ideas symbolically with the logical aspect being useful for specifi cation and verification The advantages of Prolog have been gained by adopting a programming paradigm different to that followed by the vast majority of professional programmers. The transition from a procedural paradigm to a declarative paradigm can be a difficul one. Prolog code written in procedural style is possible, but is usually inefficient difficul to understand and loses many of the benefit of the language. To overcome the required paradigm shift and for Prolog to gain widespread use as either a general application building language or an application specifi language, evidence of considerable advantage over the existing commonly used languages is needed.

Prolog has introduced many features together within one language, some of which have been incorporated into more recent languages in constraint logic programming, parallel programming and deductive databases. At the moment, Prolog plays an important role in providing a better alternative to other languages in acting as an exploratory leading edge software development language. Pereira’s (1994) suggestion of using logic programming, along with functional programming as the coordination language, as the basis of ‘coordinated computing is a good example of how Prolog can continue to position itself at the centre of evolving computer systems. Similarly, the availability of interfaces from Java to Prolog indicates that the language is still able to fulfi a role alongside current computing developments. Both of these examples illustrate how logic programming is currently viewed as a part of an overall solution and not the total solution.

This paper reviews the historical development of logic programming from the idea of logical deductions as the basis of problem solving, to the firs commercial implementation of Prolog and analyses the extent of its use up to the present time. The development of Prolog is then examined and its impact is evaluated from commercial, research and teaching perspectives. The paper concludes by discussing those aspects of Prolog’s success that are likely to influenc the future of logic programming languages.

## Logicprogrammingasageneralproblem solvingmechanism

Given a logical representation and algorithmic proof mechanism for a logic programming language, there was a requirement to implement one on a computer and to show the applicability of this combination, outside theorem proving, to general problem solving. Green (1969) has shown that theorem proving could be adapted to act as the basis for general problem solving. He developed a computer language called QA3 in LISP which realised the power of a general, formal, deductive question– answer system. This system was based on first-orde logic in classical form with a resolution type problem solver to deduce solutions. Green foresaw some of the characteristics that such a logic programming language would display. These characteristics, which are still important today are listed below.

(1) The descriptive nature by which domain objects, relations, questions and answers can be presented.

(2) The built-in search mechanism which is logically complete in the way it searches for the relevant piece of information with which to answer the proposed question, or take the process nearer to an answer.

(3) The process by which answers can be deduced from the problem description. It is in this respect that theorem proving equates to answering general questions.

(4) Different domains can be represented in the same language, i.e. the language is not specific in its representation or solving mechanism, to a particular type of problem.

(5) The dynamic nature of the language, i.e. how new axioms can be added and others removed.

By developing an actual system, Green highlighted the importance of the search strategy to the execution time. The process could be speeded up by choosing the best pairs of axioms for reduction, removing subsumed axioms, deciding what depth to stop searching and looking for direct contradictions. He also saw that in the future it would be important to have flexible easily modifiabl search strategies for particular subject areas. QA3 performed well on relatively small logic puzzles at that time (e.g. Monkeys and Bananas), both in its ability to model and to solve problems that other systems could not.

Although a theorem proving approach is suitable for many application areas, there are caveats about wholesale adoption of this approach. Problems may not be able to be described as a set of crisp logical axioms and therefore rules of deduction cannot be applied. Often the rules and facts are not known and if they are, then they may be vague. In addition, the resolution approach can take a long time to fin proof through searching via resolving pairs of axioms. It may often result in a combinatorial explosion of searching required and hence effectively not produce a solution in an acceptable time period. Other techniques such as integer programming may prove more successful for such problems, but they also may suffer from the combinatorial effect.

## ThedevelopmentofProlog-Alanguagefor logicprogramming

Around the beginning of the 1970’s several people began to formalise a language for logic programming in a way that was implementable on a computer in an efficien manner (Nilsson, 1971; Kowalski & Hayes, 1972; Roussel, 1972). Some of its characteristics meant that it was viewed as an artificia intelligence (AI) language: its symbolic nature, its reasoning through logic and also because much work took place at AI laboratories. Classic AI application areas such as natural language processing, diagnosis and planning were shown to be amenable to a logic programming approach, hence reinforcing this impression.

The use of the clausal form of first-orde logic represented as horn clauses was proposed by Kowalski (1979) as the basis for a logic programming computer language. Horn clauses are first-orde predicate clauses, but with only one conclusion. This form had the advantage of being closer to existing data processing models and other computer languages, but it also simplifie resolution significantl to make it fast enough to solve large problems. Selection, linear and definit (SLD) resolution (Kowalski & Hayes, 1972; Kowalski, 1973) was also proposed as the basis of the deduction algorithm in the logic programming language. It define a particular way of choosing and reducing two clauses. At each inference or deductive step the left-most sub-goal of each goal (as they have been input) is selected to be unifie with an appropriate head of another clause. On unification the resolvent is then made the new goal. Once this has been proved, the next left-most sub-goal is chosen and the process repeated.

The power of a possible language was also shown through its unique approach in representing and solving problems from areas such as relational databases, semantic network parsing, path finding plan formation and representing search strategies.

For Autumn 1972 to Summer 1973, Colmeraur et al (1973) and Colmeraur and Roussel (1992) developed a preliminary question–answer system written initially in ALGOL-W and followed by a more successful fina version in FORTRAN. The system was called Prolog (PROgrammation en LOGique) based on the same Horn clause logic and SLD resolution Kowalski defined but with different syntax to the current standard (Deransart et al, 1996).

The language established itself quickly as the firs commercial logic programming language. Early copies of this Prolog interpreter were taken to countries such as Hungary, Poland, Canada, France, Belgium and the UK where further development took place. One of these developments enabled the efficien compilation of Prolog and several implementations (DEC10 Prolog from University of Edinburgh, Prolog from Prologia, Marseilles) were capable of solving large problems in reasonable time (Warren, 1974). However, the language had to incorporate several non-logical features in the syntax and execution to satisfy the requirements of a general computer language. These non-logical features included, for example, axioms for input/output and control of the execution. This led to partially destroying a pure logical interpretation.

## Prologtoitscurrentstate

The development of Prolog from the early Colmeraur interpreter to the present day has been one of technical improvements to overcome perceived limitations. Prolog by the time of its firs compiler (Warren, 1977) had addressed one of the main initial limitations, that of speed. This enabled more programs which had hitherto been computationally too expensive, to be run in an acceptable amount of time. The Prolog compiler and inference engine continued to evolve, making it more robust and faster by offering improved compiler optimisation, memory usage, global analysis, simpler instruction sets and garbage collection. Generally, the logic part of Prolog, based on Horn clauses and SLD resolution, has remained unchanged. However, the syntax of the language was different between the two main initial implementations at Marseilles and Edinburgh. The current standard (Deransart et al, 1996) is based on DEC-10 Edinburgh Prolog. A debugger model was developed by Byrd (1979) and remains the model for debugging on most implementations of Prolog. Other developments to address the limitations have been in the areas of integration with foreign code or other applications, better programming environments, additional data structures and direct access to graphics.

In order to avoid the need to rewrite existing software in Prolog or just to make use of other programs, foreign function interfaces were developed to allow other language codes to be called directly from Prolog. This is a standard facility of inter-callability available between conventional languages. Fully callability was also designed to allow Prolog applications to be callable from other languages (e.g. FORTRAN or C). A major use of this inter-calling feature in Prolog concerns the interface to relational databases. Here, there is a high degree of similarity between a Prolog clause and a data entry in a relational database. Another common use of the foreign function interface is for highly numerical routines, say in FORTRAN, which can perform computationally intensive tasks faster than an equivalent piece of Prolog code.

One limitation of the syntax was in providing constructs for ‘programming in the large’ (i.e. large applications require structuring because of their size that smaller ones do not). Consequently, systems which allow the representation of modules have been introduced to allow predicates to be encapsulated and accessed in different file without the requirement of always having unique predicate names. Similarly, object orientation can be added to extend the encapsulation to within individual objects as well as giving inheritance and polymorphism (McCabe, 1992) as additional programming features to Prolog.

Some implementations of Prolog environments have provided graphical interfaces to the debugging process and to the general loading/editing/running cycle, but there are still no commercial CASE tools available as with other languages such as C++ or Smalltalk.

It is often desirable to remain within Prolog to develop the graphics interface for an application or to reason over graphical objects. For each type of windowing system on a given machine there is usually a set of Prolog predicates which interface to it. Although no standard has emerged, the implementation is usually a straight predicate to foreign language function one. However, this introduces a very procedural interpretation to the resulting code. Other representations such as declarative or object-oriented have found a better fit

## ThestatusofProlog–howsuccessfulisit?

The success of a programming language may be measured with reference to a number of different criteria. Gabriel (1993) proposed a set of criteria for a general purpose language which included its social acceptability (meaning its local support, similarity to existing languages and benefit in moving to it), amount of resources it required, its performance model and level of aptitude required to use it. The weight attached to each criterion is to some extent subjective and depends on the domain in which the language is used. Generally, Prolog scores well in requiring a low resource base in terms of memory and disk space, its availability on a large number of hardware platforms (although not necessarily the same implementation of Prolog), a good infrastructure of user help (especially in Europe), and features which are useful for certain types of application. Against this, however, users need a high degree of mathematical aptitude to fully understand aspects of Prolog such as backtracking and unification In addition, Prolog when introduced, was radically different in approach to all other successful languages at that time and could not be considered as an extension to already established languages. Its performance is also difficul to predict on the basis of the code itself. The application of Gabriel’s criteria suggests that Prolog would be unlikely to become a successful general purpose language. In this section the success of Prolog, as a special purpose language, in commercial, research and teaching environments is examined. These three domains are not exclusive since many research teams have a strong commercial focus.

## CommercialstatusofProlog–measuring success

The adoption and success of a language in commercial terms depends on factors such as speed, robustness, compatibility and the level of use, in terms of the number of reference applications built. The language must be perceived to be significantl better for a particular application area than existing established languages in order to persuade people to change.

Although slower than some other languages, Prolog’s speed of execution is acceptable in many cases. However Prolog has considerably fewer commercial applications compared to other languages such as C and C++. Questions of robustness and compatibility have now been answered, although for many years Prolog was primarily considered as the ‘master’ of a multi-language application. Taking these factors into account, it may be concluded that Prolog has enjoyed only limited commercial success. Although there is evidence that Prolog is a recognised teaching language in universities in the UK, many companies are not persuaded to invest in sustaining this level of expertise as evidenced by the lack of commercial applications. The relatively small number of professional Prolog programmers creates worries over maintenance and system developments. Therefore, even though Prolog may have been used to produce prototypes, they are likely to be deployed as full commercial systems only after they have been re-written in a language for which there is not such a skill shortage.

The data to verify the extent of Prolog’s commercial success is however not readily available. Data from software vendors is naturally commercially sensitive and so only public domain data can be used. The sources of this data are often incomplete and selective. For example, the presence of an application in a public domain database, may be dependent on the type of application, the interest of the developers/users in ‘publicising’ their application or some form of pre-selection. The two sources of public domain data used here are the Prolog1000 Database (Moss, 1993) and the Proceedings of the Practical Application of Prolog Conferences (1992, 1994, 1995, 1996), both of which exhibit the incompleteness and selectivity mentioned above.

The Prolog1000 Database initiated by the Association of Logic Programming (ALP) and The Prolog Vendors Group (PVG) is a database in which developers and users record details of Prolog applications. Most of the entries were included during 1993 and provide a snapshot of the applications at that time. The applications in the database have been analysed to provide insight into the characteristics of commercial Prolog applications. Unfortunately, full data is not available for all 502 reported applications and therefore the analysis is restricted to those cases where the relevant data is known. The subsequent analysis has been carried out with respect to system status, type of developer, hardware platform, country of origin, the Prolog implementation used and the type of application.

## Status

Table 1 shows the status of applications from the Prolog 1000 Database. The release of a piece of software, having passed quality assurance procedures, is a good indication of its commercial viability. It is diffi cult to tell from the data whether the number of evaluation or prototype systems were on their way to becoming released products, or whether the application had been stopped at that stage either for re-coding or that no further work was to be done on it. Certainly, there is a high proportion of applications taken only to this firs stage. The academic applications had a higher proportion of evaluation and prototype systems in relation to released systems, which reflect academic objectives with respect to software development. The total number of released applications was taken as the basis for further analysis of the commercial applications of Prolog.

Table1 Status of Prolog applications by type of developer

<table><tr><td rowspan="2">Type of developer</td><td colspan="3">Number of systems</td></tr><tr><td>Prototype and evaluation</td><td>Released</td><td>Total</td></tr><tr><td>Academic developer</td><td>31</td><td>23</td><td>54</td></tr><tr><td>Commercial developer</td><td>101</td><td>153</td><td>254</td></tr><tr><td>Total</td><td>132</td><td>176</td><td>308</td></tr></table>

## Platform

Table 2 shows the main hardware platforms used by the released applications. The porting of applications between DOS and other operating systems such as UNIX or VMS has traditionally been difficul since nonstandard features such as graphics and integration with foreign code in most Prolog applications have not been readily portable. In addition, few of the more popular implementations of Prolog at that time were implemented on the full range of platforms. However, porting between workstations on which the same Prolog runs is common and relatively easy as the graphics and foreign interface will be handled within the implementation and the syntax should be the same. Therefore, for a single application, there may be several workstations on which it runs.

Table2 Number of applications by hardware platform

<table><tr><td>Platform</td><td>Number of applications</td></tr><tr><td>PC</td><td>56</td></tr><tr><td>SUN</td><td>40</td></tr><tr><td>IBM mainframe, PS/2 and RS6000</td><td>11</td></tr><tr><td>DECstation VAX</td><td>6</td></tr><tr><td>Hewlett Packard</td><td>9</td></tr><tr><td>Total</td><td>122</td></tr></table>

Table3 Number of commercial applications by country of origin

<table><tr><td>Country</td><td>Number</td><td>Country</td><td>Number</td></tr><tr><td>USA</td><td>40</td><td>UK</td><td>36</td></tr><tr><td>France</td><td>13</td><td>Germany</td><td>13</td></tr><tr><td>Spain</td><td>12</td><td>Canada</td><td>12</td></tr><tr><td>Japan</td><td>9</td><td>Denmark</td><td>9</td></tr><tr><td>Holland</td><td>8</td><td>Sweden</td><td>8</td></tr><tr><td>Italy</td><td>7</td><td>Norway</td><td>6</td></tr><tr><td>Australia</td><td>6</td><td>Belgium</td><td>4</td></tr></table>

Analysis shows that there are more applications associated with PC’s than any other single platform. Taken together, the number of applications on workstations is similar to the number on PC’s. The reasons for two distinct types of platforms running applications are unclear, but may be to do with the organizational environment of the developers: systems developed in sectors with a significan research presence (aerospace, engineering, financ and medicine) and powerful computing facilities in contrast to those developed for a market whose only delivery platform is the PC (commercial, individual consultants).

## Countries

Table 3 shows the countries of origin of the commercial applications built in Prolog. Most of the applications built came from the countries associated with early developments and implementations of Prolog. The USA, which was not involved in the early developments of Prolog, is responsible for a relatively small number of applications considering its large computer base. It is likely that all active countries were aware of the survey through Internet News and ALP newsletters.

## Implementation

Table 4 shows the chosen implementation of Prolog for the commercial applications. It suggests that the majority of applications are running on PC’s since they are using PDC Prolog. It is interesting to note that this implementation is a low cost, cut-down version of Prolog. However, its reduced functionality does not mean that it has overcome Prolog’s problems in requiring significan mathematical aptitude. The differences are small for the programmer, the main one being that arguments have to be typed, which for most applications should be known anyway. On workstations, Quintus Prolog is the most commonly used implementation of the applications analysed. Quintus Prolog was recognised as the de-facto Prolog standard (until the ISO standard appeared) with which most other vendors claim compatibility.

Table4 Number of commercial applications using a particular implementation

<table><tr><td>Prolog implementation</td><td>Number</td></tr><tr><td>PDC</td><td>79</td></tr><tr><td>Quintus</td><td>28</td></tr><tr><td>LPA</td><td>17</td></tr><tr><td>Arity</td><td>12</td></tr><tr><td>Interface</td><td>8</td></tr><tr><td>Prolog-2</td><td>7</td></tr><tr><td>BIM</td><td>5</td></tr><tr><td>K-Prolog</td><td>4</td></tr><tr><td>Delphia</td><td>3</td></tr><tr><td>Sicstus</td><td>2</td></tr><tr><td>Total</td><td>165</td></tr></table>

## Characteristic types of applications

Analysis of the Prolog1000 database on the types of applications for which Prolog has been used gives an insight into the important features of Prolog which has led to its use. A large number of applications fall into the AI category, confirmin Prolog’s position as one of the main AI languages. Within this area of AI most examples are ‘expert systems’ applications. The characteristic types of systems here are those for advising (especially financial policy or legal), configuring monitoring, diagnosis/repair, learning and reasoning. Among the reasons for Prolog’s use as an AI language are its high level, symbolic nature combined with its ability to represent knowledge and reason over it.

A second type of application category is that of translation, program generation and natural language. Again this is really in the AI area and is a result of Prolog’s ability in parsing and manipulating data. Many of these applications may make use of the in-built definitiv clause grammar (DCG) rules available within Prolog. The DCG’s are used as a processor to verify, correct and understand language or to develop an interface language to a relational database or management information system.

A third category is that of data or program analysis which is based on Prolog’s pattern matching capabilities. Commonly, Prolog is used as the back-end of an application which generates data, i.e. statistical, text or structured reports which are then interpreted and presented in an alternative format.

A fourth category consists of design and layout applications. For reasons of Prolog’s easy and flexibl representation of layouts and design rules, applications were successfully built in Prolog for domains such as telecommunications, electronics, architecture and chemicals.

A fift category is in the area of scheduling and planning where again it is Prolog’s representational abilities in definin the scheduling configuration and rules that has led to success.

These last two categories concern decisions of a what, where and when nature, leading to a possible combinatorial explosion of possibilities in the search for a solution. Given the capability to develop specialised search strategies within Prolog for individual applications, there is great potential for a logic-based approach to attack problems that hitherto have been computationally too expensive.

A minority of applications exist for which Prolog appears to offer no distinct advantage over other languages. The developer’s familiarity with Prolog and a convenient environment are likely to have influence the choice in these cases of it being used as a general purpose language.

The practical applications of Prolog conferences have been held annually between 1992 and 1996. Their proceedings describe Prolog applications which have been chosen to be good examples in the fiel and cover a wide range of application areas. Therefore, it must be assumed that the proceedings are selective in the applications which are presented. However, the range of papers should indicate the nature of the application areas in which Prolog is used. The commercial applications were observed as being from the following industrial sectors: engineering, telecommunications, natural resources, transport, computing, agriculture, hospitals, financ and chemical. Although covering a wide area, all the applications were of a specialised one-off nature and few could be considered as examples of Prolog being used as a general purpose programming language. There were also many instances of Prolog being used to build other tools such as parsers or analysers.

The papers are categorised in Table 5 according to whether the paper was an academic application or commercial application. The balance seemed to be roughly equal between commercial and academic application papers, although the conference may have been designed that way. Alternatively, if the conference is seen as promoting the commercial use of Prolog, then the figure illustrate a weak presence commercially but strong academic representation. The rise in papers devoted to constraint logic programming (CLP) resulted in a separate conference called the practical application of constraint programming (PACT) being introduced. The set of CLP papers showed, however, a greater number coming from industry, remarkably so at such an early stage in the history of this logic-based technology.

Table5 Number and types of papers presented at the four practical application of Prolog conferences

<table><tr><td rowspan="2">Applications*</td><td colspan="4">Years</td><td rowspan="2">Total</td></tr><tr><td>1992</td><td>1994</td><td>1995</td><td>1996</td></tr><tr><td>Prolog Academic</td><td>17</td><td>18</td><td>20</td><td>19</td><td>74</td></tr><tr><td>Prolog Commercial</td><td>22</td><td>17</td><td>23</td><td>16</td><td>78</td></tr><tr><td>Total</td><td>39</td><td>35</td><td>43</td><td>35</td><td>152</td></tr></table>

\*These do not include CLP papers.

The absence of parallel applications of Prolog was notable, perhaps because the parallel community is very much a separate application area, while CLP is seen much more as an extension to Prolog.

## ResearchstatusofProlog–measuring success

In research environments, the criteria for success of a language are different to those commercially. In research, it is the ability to represent ideas and evaluate new or different approaches easily that has resulted in Prolog being so successful in the research area. Although many research projects involve building applications, the commercial realisation is likely to take place outside the research environment. To judge the extent to which Prolog is used in research, a survey of the published research literature with the word Prolog in the title, abstract or keyword was undertaken. The Science Citation Index provides bibliographic references from over 4400 journals containing over 200 000 papers each year. The type of usage to which Prolog is put in research can be categorised into the following three areas:

(1) Using Prolog for building applications or modelling (e.g. A fitnes analysis system with an intelligent interface (Parisi & Allen, 1992)). These are typically ‘expert’ systems where a particular problem in a company is addressed.

(2) Using Prolog as a language or concept as the basis for building other technologies or tools (e.g. The CLP(R) language and system (Jaffar et al, 1992)).

(3) Developing Prolog technology through improving aspects of it such as the compiler, unificatio or environment (e.g. A verifie Prolog compiler for the Warren Abstract Machine (Russinoff, 1992)), without developing a new language. It also covers papers which are about Prolog as a computer language.

Table 6 shows the number of papers published in each area in the years 1991 to 1996. Certainly there are a large number of papers written for which Prolog is considered an important constituent. Even in 1996, over 20 years since Prolog was invented, enhancements are still being proposed to the basic model. The emphasis over the past 6 years seems to have switched from the core Prolog technology to developing higher level technologies based on Prolog. There also appears to be an increasing use of Prolog in applications as the language matures. The areas of these applications are analysed in Table 7 for the years 1994, 1995 and 1996. It can be seen that there is a wide range of application areas for which Prolog has been found suitable.

Table6 Number of research papers by type and year

<table><tr><td rowspan="2">Type of paper</td><td colspan="6">Year</td></tr><tr><td>1991</td><td>1992</td><td>1993</td><td>1994</td><td>1995</td><td>1996 (9 months)</td></tr><tr><td>Applications</td><td>15</td><td>11</td><td>10</td><td>37</td><td>23</td><td>20</td></tr><tr><td>Other technologies</td><td>30</td><td>18</td><td>45</td><td>42</td><td>44</td><td>44</td></tr><tr><td>Prolog technology</td><td>41</td><td>29</td><td>61</td><td>35</td><td>28</td><td>20</td></tr><tr><td>Total</td><td>86</td><td>58</td><td>116</td><td>114</td><td>95</td><td>84</td></tr></table>

In the other technologies category of Table 6, most of the papers related to using Prolog as the basis for parallel processing, constraint programming and other language synthesis. Prolog lends itself to parallel processing with AND-parallelism relating to each sub-goal as a separate process and OR-parallelism relating to each clause being searched in parallel. The reasoning and in-built search mechanism encouraged the use of Prolog as the basis of constraint programming.

## AcademicteachingstatusofProlog– measuringsuccess

As an academic teaching language, Prolog is frequently used at universities and colleges, not just as an AI language but one in which the student is exposed to problem solving as opposed to concentrating solely on execution. A recent survey entitled ‘A survey of the teaching of programming to computing undergraduates in UK universities and polytechnics’ (Furber, 1992), gives an indication of Prolog usage in the UK around July/August of

Table7 Number of published applications in 1994 –1996 by type

<table><tr><td rowspan="2">Application type</td><td colspan="3">Year</td></tr><tr><td>1994</td><td>1995</td><td>1996 (9 months)</td></tr><tr><td>Manufacturing/Production/Engineering</td><td>11</td><td>6</td><td>9</td></tr><tr><td>Robotics/Vision</td><td>3</td><td>1</td><td>1</td></tr><tr><td>CAD</td><td>3</td><td>2</td><td>1</td></tr><tr><td>Medicine</td><td>3</td><td>3</td><td>2</td></tr><tr><td>Biology</td><td>3</td><td>0</td><td>0</td></tr><tr><td>Mathematics</td><td>3</td><td>0</td><td>1</td></tr><tr><td>Physics</td><td>2</td><td>0</td><td>0</td></tr><tr><td>Languages</td><td>2</td><td>1</td><td>0</td></tr><tr><td>Chemistry</td><td>3</td><td>4</td><td>2</td></tr><tr><td>Computing</td><td>1</td><td>0</td><td>1</td></tr><tr><td>Nuclear Power</td><td>1</td><td>1</td><td>0</td></tr><tr><td>Meteorology</td><td>1</td><td>0</td><td>0</td></tr><tr><td>Geology</td><td>0</td><td>2</td><td>0</td></tr><tr><td>Archaeology</td><td>0</td><td>1</td><td>0</td></tr><tr><td>Forestry</td><td>0</td><td>1</td><td>0</td></tr><tr><td>Transport</td><td>0</td><td>1</td><td>0</td></tr><tr><td>Music</td><td>0</td><td>1</td><td>1</td></tr><tr><td>Financial</td><td>0</td><td>0</td><td>1</td></tr></table>

1989. A total number of 60 UK universities and polytechnics responded by giving details of which languages were used in Computer Science or IT courses. Prolog came highest among all languages with 38 of the 60 establishments using it on courses. The author concluded that the use of Prolog was high because it was the only readily available language within the declarative programming paradigm. The most popular firs language was Pascal, and in order to complement this with a second taught language, one from another paradigm such as logic programming or object oriented programming would be recommended.

## Conclusions

After 20 years, Prolog is being used successfully in commercial, research and teaching environments. It has overcome many hurdles of acceptability that any new programming language must clear. It has gone through a period of expansive growth, but at the moment is on a plateau. There is though, a growing base of commercial applications, a growing use of it as a research language, and it is being taught extensively at universities. It is however a minority language and as such needs to keep evolving in order to continue to survive and keep its position as a language for leading edge and AI applications. As a mainstream general application language, it can at least hope not to provide the reasons for rewriting after the prototype has been developed, by providing the necessary speed, robustness and integration. However, the choice of a language is often a social phenomenon rather than technical (Gabriel, 1993), and the perceived image of Prolog is frequently still of its state 20 years ago when it firs emerged. This was also the view of Van Roy (1994) as one of the factors influencin the widespread acceptance of Prolog. He suggested that the public perception could only be solved by marketing and application development.

It is perhaps also important to try to extract Prolog’s main features and use these to augment existing popular languages. In this way, the existing programmer base is more likely to make the modest jump to using logic programming features.

The factors which have influence the current position of Prolog, may be summarised as follows.

(1) The language itself – it is sufficientl different in its modelling and solving capabilities over other languages to make a logic programming approach more suitable for certain application areas.

(2) Academic teaching base – this is strong especially in Europe because of its origins and the way it provides a contrast to procedural languages.

(3) Commercial applications – there have been few, but a sufficien number in important companies to give the language credibility.

(4) Research – perhaps the most important factor. Prolog has shown itself to be an excellent research tool, often forming the basis of other languages in CLP and parallel programming.

Programming languages are continually evolving and as Friedman (1991) observed, each step in the evolution so far has been away from machine oriented languages to user oriented ones. Prolog fit well into the latter category, but its success may be limited in the way in which it has given rise to more successful languages within the areas of CLP or parallel programming. It is still too early to predict which more successful language will supersede Prolog, but the pattern has already been set by a pioneer language in one paradigm giving rise to a more successful language in the same area. The examples here are of how ALGOL gave rise to Pascal in the area of structured programming, and of Smalltalk providing the model for object orientation and the C++ language.

## References

<sup>AALPS</sup> (1993) Load Planning System for Aircraft Cargo, Prolog 1000 Database. Available through anonymous ftp from src.doc.ic.ac.uk in packages/prolog-progs-db/prolog1000.v1.

<sup>ACAPS</sup> (1993) Expert System to Create Loan Documentation, Prolog 1000 Database. Available through anonymous ftp from src.doc.ic.ac.uk in packages/prolog-progs-db/prolog1000.v1.

<sup>Byrd</sup> <sup>L</sup> (1979) Understanding the control flo of Prolog programs. DAI Research paper No 151, Department of Artificia Intelligence, University of Edinburgh.

<sup>CAPS</sup> (1993) Computer Aided Process Scheduling, Prolog 1000 Database. Available through anonymous ftp from src.doc.ic.ac.uk in packages/prolog-progs-db/prolog1000.v1.

Colmerauer A, Kanoui H, Roussel P <sub>et al (1973) System de Com-</sub> munication Homme-Machine en Francaise, Research Report, Groupe Intelligence Artificielle Faculte des Sciences de Luminy, Universite Aix-Marseilles, Luminy, France.

<sup>Colmerauer</sup> <sup>A</sup> and <sup>Roussel</sup> <sup>P</sup> (1992) The Birth of Prolog. SIGPLAN Notices 28(3), 37–52.

Deransart P, Ed-Dbali A <sub>and</sub> Cervoni L <sub>(1996) Prolog: The Stan-</sub> dard Reference Manual. Springer-Verlag.

<sup>Friedman</sup> <sup>LW</sup> (1991) Comparative Programming Languages. Prentice Hall.

<sup>Furber</sup> <sup>D</sup> (1992) A survey of the teaching of programming to computing undergraduates in UK universities and polytechnics. The Computer Journal 35(5), 530–533.

<sup>Gabriel</sup> <sup>RP</sup> (1993) The end of history and the last programming language. Journal of Object Oriented Programming 6(4), 90–94.

<sup>Green</sup> <sup>C</sup> (1969) Theorem-proving by resolution as a basis for question-answering systems. In Machine Intelligence Vol 4, (<sup>Meltzer</sup> <sup>B,</sup> <sup>Michie</sup> <sup>D</sup> and <sup>Swann</sup> <sup>M</sup>, Eds). pp 183–205.

Jaffar J, Michaylov S, Stuchry PJ <sub>et al (1992) The CLP(R) langu-</sub> age and system. ACM Transactions on Programming Languages and Systems 4(3), 339–395.

<sup>Kowalski</sup> <sup>RA</sup> and <sup>Hayes</sup> <sup>PJ</sup> (1972) Lecture Notes on Automatic Theorem Proving, Memo 40, Department of Computational Logic, Edinburgh University.

<sup>Kowalski</sup> <sup>RA</sup> (1973) Predicate Logic as Programming Language, Memo 70, Department of Artificia Intelligence, Edinburgh University.

<sup>Kowalski</sup> <sup>RA</sup> (1979) Logic for Problem Solving. North-Holland.

<sup>McCabe</sup> <sup>FG</sup> (1992) Logic and Objects. Prentice Hall.

<sup>Moss</sup> <sup>CDS</sup> (1993) Halfway to the Prolog Thousand. Logic Programming: The Newsletter of the Association for Logic Programming 6(2), 3–7.

<sup>Nilsson</sup> <sup>NJ</sup> (1971) Problem Solving Methods in Artificial Intelligence. McGraw-Hill.

<sup>Parisi</sup> <sup>AV</sup> and <sup>Allen</sup> <sup>GD</sup> (1992) A fitnes analysis system with an intelligent interface. Computers in Biology and Medicine 22(6), 437– 441.

<sup>Pereira</sup> <sup>F</sup> (1994) Mailnote on comp.lang.prolog. 13th June.

Proceedings of the Practical Application of Prolog (1992) London, Alinmead Software Ltd.

Proceedings of the Second International Conference on the Practical Application of Prolog (1994) London, Alinmead Software Ltd.

Proceedings of the Third International Conference on the Practical Application of Prolog (1995) Paris, Alinmead Software Ltd.

Proceedings of the Fourth International Conference on the Practical

## Abouttheauthors

KenDarby-Dowman , PhD is Senior Lecturer in Operational Research at Brunel University. His research interests lie in linear and integer programming algorithms and applications, stochastic programming and the integration of constraint logic programming and mathematical programming approaches for solving combinatorial optimisation problems. He has published over 40 refereed papers in leading international journals and has led several funded research projects, particularly in the area of transport scheduling.

Application of Prolog (1996) London, The Practical Application Company Ltd.

Prolog 1000 Database (1993) is available through anonymous ftp from src.doc.ic.ac.uk in packages/prolog-progs-db/prolog1000.v1.

<sup>Roussel</sup> <sup>P</sup> (1972) Definition et Traitement de L’egalite Formelle en Demonstration Automatique, These de 3ieme Cycle, Groupe Intelligence Artificielle Faculte des Sciences de Luminy, Universite Aix-Marseilles.

<sup>Russinoff</sup> <sup>DM</sup> (1992) A verifie Prolog compiler for the Warren abstract machine. Journal of Logic Programming 13(4), 367–412.

<sup>Van</sup> <sup>Roy</sup> <sup>P</sup> (1994) The wonder years of sequential prolog implementations. Journal of Logic Programming 19, 385–441.

<sup>Warren</sup> <sup>DHD</sup> (1974) A System for Generating Plans. Memo 76, Department of Computational Logic, Edinburgh University.

<sup>Warren</sup> <sup>DHD</sup> (1977) Implementing Prolog – Compiling Logic Programs, DAI Research Report 39 & 40, Department of Artificia Intelligence, University of Edinburgh.

JamesLittle is a teaching and research fellow in the Department of Mathematics and Statistics, Brunel University. He is working towards a PhD in the effective collaboration of Integer Programming and Constraint Logic Programming to solve large-scale scheduling problems. Prior to his academic appointment, he worked as technical director with an Artificia Intelligence company. He also has research interests in the application of machine learning techniques to social work.
