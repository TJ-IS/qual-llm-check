---
otero_id: 18835
otero_key: "YNRB7GDN"
title: "Software tasks"
authors: "Robert L Glass; Iris Vessey; Sue A Conger"
year: "1992"
journal: "Information & Management"
doi: "10.1016/0378-7206(92)90043-f"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Software tasks Intellectual or clerical?

Robert L. Glass

Computing Trends, State College PA, USA

Iris Vessey

Pennsylvania State University, University Park PA, USA

Sue A. Conger \*

City University of New York, New York NY, USA

There are two conflicting views of the complexity of software development: 'anyone can do it', or 'it is the most complex activity the human mind has ever undertaken'. We address this difference empirically in two exploratory studies that examined the intellectual (non-routine) and clerical (routine) nature of software tasks. The first study sought to determine the proportion of software tasks that can be regarded as intellectual or clerical in nature. Taxonomies of software tasks were classified based on the assessment of highly experienced raters. The second study examined the length of time novice systems analysts spent in carrying out tasks during the information requirements specification phase of the systems development life cycle. The experiment used protocol and videotape analysis. Results show that the numbers of intellectual tasks in software development, and the time spent on those tasks, both predominate over clerical tasks by 4 to 1. These initial results suggest that even simple tasks are more intellectual than the 'anyone can do it' or the 'software development can be automated' viewpoints frequently expressed in the literature.

Keywords: Software development; Software complexity; Management of software development; Information systems; Information requirements analysis; Structured analysis; Software tasks.

Correspondence to: I. Vessey, Department of Management Science and Information Systems, Pennsylvania State University, University Park, PA 16802, USA. Tel: (814) 865-5234. Bitnet: ixv1@psuvm.

## 1. Introduction

There are two divergent views of the complexity of developing software. In the first, software development is so mechanistic that it can be automated. In the second, software development is one of the most complex activities undertaken by humans. Clearly, these two views are in conflict.

Ever since the inception of computers, claims have been made that the need for software development would decline dramatically in response to the latest wave of innovation. In the 1960's, for

![](/api/attachments/YNRB7GDN/fulltext/images/af86f4481316c20f0978ec8e9f0e28206bc287c96e642b631df6e3cb433c4a8d.jpg)

Robert L. Glass has been active in the field of computing and software for over 35 years, largely in the Aerospace industry, but also as an academic. In industry, he has managed projects, built and maintained software, and engaged in research and development. In academe, he taught for five years in the software engineering graduate program at Seattle University, and spent a year at the Software Engineering Institute. He is the author of 16 books and 28 published

papers on computing and software, editor of the Journal of Systems and Software, publisher and editor of The Software Practitioner, and a Lecturer for the Association for Computing Machinery.

![](/api/attachments/YNRB7GDN/fulltext/images/65532e8f860eb6d3e41dbf6d63537d968d44c0573e183ad7283a8df8b6ea8c05.jpg)

Iris Vessey is Associate Professor of Management Information Systems at the Pennsylvania State University. She received the Ph.D. degree from the University of Queensland in 1984. Her research centers on the cognitive processes underlying the analysis and design of software. Current interests include the consequences of the application, structured methodologies, and the mode of information presentation for these activities, as well as the support provided by CASE tools for both individuals and for teams. She has published articles on related topics in Communications of the ACM, Decision Sciences, IEEE Transactions on Software Engineering, IEEE Transactions on Systems, Man, and Cybernetics, Information Systems Research, and the International Journal of Man–Machine Studies.

example, it was packaged software that was slated for replacing the software developer (see, for example, [8]). The 1970's was the era of the structured revolution [10,13,30,43] with its claims of error-free software [1]. The 1980's was the decade of the fourth-generation language and the debut of end-user computing. Martin [22] called it a “revolution in technology”, and the title of his book, ‘Application Development Without Programmers’, states the promise very clearly [21].

In the latter half of the 1980's and into the 1990's, the software industry is still searching for dramatic solutions, this time with automated software engineering (CASE) tools (see, for example, [23,26,29]). We see similar kinds of promises: In this instance, that automated tools will replace the software developer. For example, Souza [35] states that “CASE has been defined as the automation of software development” and McClure [25] elaborates: “A workbench has integrated tools that automate the entire development and maintenance of software systems and software project management. The output of one life-cycle phase is directly and automatically passed on to the next life-cycle phase; the final product is an executable software system and its documentation”.

The attitude that software development is easy is reflected in comments in the popular press. For example, we see [24]: “MIS should be managed by a business generalist rather than a technology specialist. I can teach my mother how to code. It is easier to teach a person about technology than it is to teach a techie how to manage.” Weinberg [38] lends further support to this ‘popular’ view when he sarcastically states: “The managers, after all, once took a ‘programming’ course. They know programming is unprofessional, shallow and

![](/api/attachments/YNRB7GDN/fulltext/images/5a3b5981658837fdd92fe1cb5ad88c13dc7ca825e90fdcc4b374fdb3816edd8b.jpg)

ment, information technology use for work, and management of the IS function. In addition to teaching and research, Dr. Conger has an extensive consulting practice which draws on her work experiences from 20 years in the information systems field.

unmanageable. They know that money spent on training is wasted and would be better invested in some new hardware or a software tool that promises to replace a few programmers.”

However, in the second view, software development is far from easy. Brooks [6] eloquently states: “Software entities are more complex for their size than perhaps any other human construct because no two parts are alike(...) In this respect, software systems differ profoundly from computers, buildings, or automobiles, where repeated elements abound.” This view is substantiated by a position statement of the computer science and technology board of the U.S. national research council [36], which asserts: “There are few human endeavors that are as difficult to grasp as a complex program”.

From an academic perspective, specialized software engineering programs are increasing in number, in addition to already existing university programs in computer science and information systems. Achieving the academic credentials necessary to pursue a career in software development requires several years of study.

It is clear, then, that, within the broader IS community, significantly different signals are frequently given regarding the scope and complexity of software development. These mixed signals challenge the credibility of software professionals, leaving the industry (and sometimes also the related academic disciplines) in the unenviable position of continually needing to justify its existence (see, for example, [7]).

This paper represents an initial attempt to improve our understanding of the complexity of the software development process by examining whether software tasks are predominantly intellectual (and thus “complex”), or clerical (and thus “easy”). By intellectual, we mean that the process requires non-routine thought processes; by clerical, we mean that the process can be accomplished using routine procedures. The paper presents the results of two exploratory studies that address the nature of software tasks from different perspectives.

## 2. Background

Perhaps rather surprisingly, few studies have explicitly sought to assess the complexity of the software development process. Hence, much of the available evidence is anecdotal or philosophical in nature.

Because so much has been said about the simplicity of software development, several leading software professionals have felt a need to refute the claims. For example, Parnas [31] in his “Star Wars” papers states: “I believe that the claims made for our automatic programming systems are greatly exaggerated(...) If the input specification is not a description of an algorithm, the result is woefully inefficient(...) there will be no substantial change from our present capability.” This statement is especially relevant to information systems where an algorithm is rarely available. Rich and Waters [33], active in the automatic programming field, felt the need to refute the “cocktail party myths” prevalent among those hoping that automatic programming would somehow eliminate the need for programmers. DeMarco and Lister [11], addressing the belief that methodology is the long-sought ‘silver bullet’ [6], state that “methodologies can do grievous harm” and that people are the key to software development.

The literature does provide certain empirical evidence of the complexity of software development. For example, Parnas's experience with the department of navy's software cost reduction project, which sought to demonstrate the effectiveness of modern development techniques in facilitating the development and maintenance of real-time software, presents evidence of the complexity of the software development process [32]. Fjelstad and Hamlen [12] showed that software maintainers spend 45% of their time seeking to understand the change to be made and the software to be changed, 35% of their time verifying the change once it is made, and only 20% of their time actually making the change. Hence they spend effectively 80% of their time thinking about the problem and its solution. Similarly, Gibson and Senn [14] in a study of professional maintenance programmers, report that to add 8 lines of code required on average 35 minutes to produce (mostly) erroneous code. They state: “Because so few lines were added, it might be inferred that more time was spent thinking than writing. Despite this, more than half (58%) of the implementations contained serious errors.” Further, Woodfield [40] suggests that for every 25% increase in the complexity of a problem to be solved, there is a 100% increase in the complexity of the software required to solve it. Hence, the complexity of software may be a problem of scale: Easy tasks are easy to solve, hard ones are very hard.

Finally, the question of the complexity of software development is begged in statements such as: “(…) testing comprises a planning part and an operative part. While the latter can take great advantage from the support of automated tools, the planning part is mostly based on human ingenuity and competence.” [2].

It appears, then, that a study examining the extent to which software personnel use human ingenuity versus routine procedures may be a fruitful way to investigate the complexity of software development. Support for these two types of activities can be found in the industrial psychology literature on job and task analysis. Singleton [34], for example, distinguishes between: “(...) two types of tasks which are not compatible because they require very different levels of skill. On the one hand [the problem solver] must cope with routines where the demand is for precise obedience to established instructions and on the other hand he might suddenly be faced with a need to respond in a creative manner totally outside any instructions.”

For the purposes of this research, we use the term ‘clerical’ to refer to routine tasks, those that can be completed using established routines or procedures, and “intellectual” to refer to tasks for which routine procedures are not available.

## 3. Studies conducted

To assess the nature of software tasks, we conducted two studies that assessed the issues under investigation from different perspectives. If the results of the studies supported each other, we could be more confident that we were, indeed, targeting the factors of interest. The first study involved classifying software tasks as either intellectual or clerical in nature. The second study involved recording the time people actually spent in carrying out intellectual versus clerical tasks when specifying information requirements using structured methods.

## 3.1. Software task analysis

The industrial psychology literature on job analysis documents a number of methods for evaluating jobs. McCormick and Ilgen [27], for example, report on “four rather traditional job evaluation methods [that] are based on individuals’ judgments of job characteristics”, together with a fifth method based on analysis of job components. The four traditional methods are the ranking, classification, point, and factor comparison methods. Our study of software tasks employed the classification method.

The tasks assessed were the most comprehensive lists or taxonomies of software tasks reported in the software literature. Table 1, for example, presents the detailed set of software tasks specified by Henderson and Cooprider [15]. Although developed to examine functionality in CASE tools, this task taxonomy provides a fairly detailed description of tasks in software development in general. Tables 2(a) and (b) present two task taxonomies taken from the general software development literature. The first of these, by Brackett [5], focuses on the initial stages of the software development life cycle, while the second, by Jones [20], focuses on the later stages of the life cycle. Since there is little overlap in the tasks represented in Brackett's and Jones' taxonomies, we investigated both.

Certain of the tasks in the taxonomies are technology-related. For example, Henderson and Cooprider list ‘simultaneously display several views’, ‘import/export data’, ‘magnify a model to see greater levels of detail’, and Jones lists ‘reusable design access’ and ‘reusable code access’. They clearly have relevance only in an automated environment. Hence, such tasks are asterisked in the tables and are not further considered here.

As stated in Section 2, “clerical” tasks were defined for the purposes of this study in terms of the availability of routine procedures for task accomplishment. “Intellectual” tasks were defined as those for which routine procedures were not available. Note that we made our judgments of the nature of tasks independent of whether the task was automated or not. Using this approach, we could judge a task to be clerical even if it were not currently automated. Two coders independently evaluated the lowest level tasks reported in the taxonomies according to whether they were intellectual, clerical, or indeterminate in nature. Following the job analysis literature we used coders with substantial experience in all aspects of software development. McCormick and Ilgen [27] report that the reliability of judgments is reasonably high when highly trained raters are used. One of the coders in this study had 30 years and the other 20 years of industrial and/or business software development experience.

To assess the reliability of the classification, coders' responses for each of the taxonomies were compiled into agreement matrices and the proportions of agreement and the Kappa coefficients were calculated [9]. For the CASE tool taxonomy of tasks (Table 1), the raw proportion of agreement was 0.83. The Kappa coefficient, which measures the proportion of agreement between coders after agreement that can be attributed to chance has been removed, was 0.73; the standard deviation of Kappa was 0.075. The proportion of agreement for Brackett's taxonomy, Table 2(a), was 0.92. The Kappa coefficient could not be calculated for this taxonomy, since there was only 1 disagreement in 13 tasks For Jones's taxonomy, Table 2(b), the raw proportion of agreement was 0.89, with Kappa of 0.60 and standard deviation of 0.27. These reliabilities are acceptable for an exploratory study (see, for example, [3,19]). Differences in the two coders' scoring were resolved by agreement between the two coders. The reconciled codings, which formed the basis for the analysis, are presented in Tables 1 and 2(a) and (b).

Table 3 shows that intellectual tasks predominate in the taxonomies. For Henderson and Cooprider's taxonomy, intellectual tasks predominate by a factor of almost 3 to 1(62/21). For the other taxonomies investigated, the breakdown is especially dramatic: Intellectual tasks make up 100% of Brackett's software tasks and 83% of Jones' tasks (a combined ratio of 9/1). Overall, intellectual tasks predominate over clerical tasks by a ratio of almost 4 to 1 (71/18). We see, using this rudimentary classification, that the predominant proportion of tasks in software development is intellectual in nature.

The limitation of this approach is that it assesses only the numbers of software development tasks that are intellectual or clerical in nature; it is also important to know the relative times (and therefore the resources) spent on those intellectual and clerical tasks. Hence, it is important to see the results as only one piece of evidence in the development of an accurate picture of the nature of software tasks.

Table 1
Tasks performed by CASE tools. $^{a}$

<table><tr><td>Software taskb</td><td>Code</td></tr><tr><td>Functionalities of representation</td><td>i</td></tr><tr><td>Represent a design</td><td>i</td></tr><tr><td>Construct models</td><td>i</td></tr><tr><td>Customize the language or conventions used for representation</td><td>i</td></tr><tr><td>Represent relationships</td><td>i</td></tr><tr><td>Combine entities or processes</td><td>id</td></tr><tr><td>* Show an object&#x27;s attributes</td><td></td></tr><tr><td>Maintain descriptions</td><td>c</td></tr><tr><td>Provide naming conventions</td><td>i</td></tr><tr><td>Maintain single definition</td><td>c</td></tr><tr><td>* Move between models</td><td></td></tr><tr><td>Redraw a diagram</td><td>c</td></tr><tr><td>Map onto functional description</td><td>id</td></tr><tr><td>Combine equivalent processes</td><td>id</td></tr><tr><td>* Simultaneously display several views</td><td></td></tr><tr><td>Choose a model</td><td>i</td></tr><tr><td>Functionalities of analysis</td><td></td></tr><tr><td>Test for model consistency</td><td>i</td></tr><tr><td>Check for structural equivalence</td><td>i</td></tr><tr><td>Check for unnecessary or redundant connections</td><td>id</td></tr><tr><td>Detect inconsistencies</td><td>id</td></tr><tr><td>Identify impact of design changes</td><td>i</td></tr><tr><td>Search the design for similar objects</td><td>i</td></tr><tr><td>Suggest resolutions</td><td>i</td></tr><tr><td>Estimate characteristics</td><td>i</td></tr><tr><td>Search design for specified characteristics</td><td>i</td></tr><tr><td>Simulate the production environment</td><td>i</td></tr><tr><td>Identify rules violations</td><td>c</td></tr><tr><td>Trace relationships</td><td>id</td></tr><tr><td>Identify differences</td><td>i</td></tr><tr><td>Recommend a general model</td><td>i</td></tr><tr><td>* Perform an operation on part of a design</td><td></td></tr><tr><td>Functionalities of transformation</td><td></td></tr><tr><td>Generate executable code</td><td>i</td></tr><tr><td>Convert specification</td><td>i</td></tr><tr><td>Transform a representation</td><td>i</td></tr><tr><td>Provide documentation</td><td>id</td></tr><tr><td>Perform reverse engineering</td><td>i</td></tr><tr><td>Generate screen mockups</td><td>i</td></tr><tr><td>* Import/export data</td><td></td></tr><tr><td>Create templates for tasks and deliverables</td><td>i</td></tr><tr><td>Propagate a change</td><td>c</td></tr><tr><td>Functionalities of control</td><td></td></tr><tr><td>Specify who can review work</td><td>id</td></tr><tr><td>Provide management information</td><td>id</td></tr><tr><td>Maintain a record of responsibility</td><td>c</td></tr><tr><td>Maintain a record of changes</td><td>c</td></tr><tr><td>Provide management information on more than one project</td><td>id</td></tr><tr><td>Specify who can modify</td><td>i</td></tr><tr><td>* Freeze a portion of a design</td><td></td></tr><tr><td>Manage quality assurance</td><td>i</td></tr><tr><td>Alter rules</td><td>i</td></tr><tr><td>Provide prioritizing assistance</td><td>i</td></tr><tr><td>Estimate tasks/projects</td><td>i</td></tr></table>

Table 1 (continued)

<table><tr><td>Software taskb</td><td>Code</td></tr><tr><td>Remind team about deadlines</td><td>c</td></tr><tr><td>Merge versions</td><td>c</td></tr><tr><td>Produce metrics</td><td>i</td></tr><tr><td>Maintain list of requirements and how satisfied</td><td>c</td></tr><tr><td colspan="2">* Temporarily ignore a problem so work can continue Functionalities of cooperative functionality</td></tr><tr><td colspan="2">* Maintain a dialogue with other tools users</td></tr><tr><td colspan="2">* Allow a group to work simultaneously on a task</td></tr><tr><td colspan="2">* Send message to others who use the tools</td></tr><tr><td colspan="2">* Allow concurrent use of dictionary/diagram/etc.</td></tr><tr><td colspan="2">* Provide group interaction support (brainstorming)</td></tr><tr><td colspan="2">* Attach electronic notes</td></tr><tr><td colspan="2">* Allow anonymous feedback</td></tr><tr><td>Notify designer of changes</td><td>c</td></tr><tr><td>Build a catalog of macros</td><td>c</td></tr><tr><td>Facilitate design alternatives</td><td>i</td></tr><tr><td colspan="2">Functionalities of support</td></tr><tr><td>Provide quick reference aids</td><td>i</td></tr><tr><td>Provide instructional materials</td><td>i</td></tr><tr><td>Identify external sources of information</td><td>i</td></tr><tr><td>Build templates/examples for tutorials/demos</td><td>i</td></tr><tr><td>Browse in other segments of the tool</td><td>i</td></tr><tr><td>Explain why part of a design is inconsistent</td><td>i</td></tr><tr><td>Anticipate user errors from past patterns</td><td>i</td></tr><tr><td>Allow undoing a series of commands</td><td>i</td></tr><tr><td>Generate outputs in a variety of media</td><td>id</td></tr><tr><td>Incorporate command macros</td><td>i</td></tr><tr><td>Generate reports and documents</td><td>c</td></tr><tr><td colspan="2">* Provide change pages</td></tr><tr><td colspan="2">* Magnify a model to see greater levels of detail</td></tr><tr><td>Build a library of customized models</td><td>i</td></tr><tr><td colspan="2">* Prepare, edit, store, send, and retrieve documents</td></tr><tr><td>Store versions of a design</td><td>c</td></tr><tr><td colspan="2">* Link a design to a library for testing</td></tr><tr><td colspan="2">* Develop, run and store customized reports</td></tr></table>

$^{a}$ [15] Henderson, J.C., and Coopridcr, J.G., “Dimensions of IS Planning and Design Technology,” Information Systems Research, Vol. 1, No. 3, 1990, 227–254.  
$^{b}$ technology-based tasks

## 3.2. Software time analysis

This part of the study was designed to address the relative times spent on intellectual and clerical tasks. To do this, we conducted a protocol analysis in which subjects spoke aloud as they solved a problem, thus providing a trace of their problem solving processes. The sessions were videotaped providing both visual and verbal

Table 2(a)
Software tasks performed. $^{a}$

<table><tr><td>Software tasks</td><td>Code</td></tr><tr><td>Software requirements tasks</td><td></td></tr><tr><td>Requirements identification</td><td></td></tr><tr><td>Context analysis</td><td>i</td></tr><tr><td>Elicitation from people</td><td>i</td></tr><tr><td>Deriving software requirements from system requirements</td><td>i</td></tr><tr><td>Task analysis to develop user interface requirements</td><td>i</td></tr><tr><td>Identification of constraints</td><td>i</td></tr><tr><td>Requirements analysis</td><td></td></tr><tr><td>Assessment of potential problems</td><td>i</td></tr><tr><td>Classification of requirements</td><td>i</td></tr><tr><td>Evaluation of fcasibility and risks</td><td>i</td></tr><tr><td>Requirements representation</td><td></td></tr><tr><td>Use of models</td><td>i</td></tr><tr><td>Roles for prototyping</td><td>i</td></tr><tr><td>Requirements communication</td><td>i</td></tr><tr><td>Preparation for validation (criteria, techniques)</td><td>i</td></tr><tr><td>Managing the requirements definition process</td><td>i</td></tr></table>

$^{a}$ [5] Brackett, J.W., “Software Requirements,” Software Engineering Institute, SEI-CMU-19-1.1, 1989.

records of problem solving behavior [28]. The visual record permitted us to observe how much time software developers spend thinking and how much time acting on that thought while engaged in specifying information requirements. Hence, for the purposes of this study, we operationalized time spent on intellectual and clerical tasks as time spent on thinking, and representing (drawing) the outcome of those thoughts.

<table><tr><td>Software  $tasks^b$ </td><td>Code</td></tr><tr><td colspan="2">Overall software tasks</td></tr><tr><td>Requirements analysis</td><td>i</td></tr><tr><td>Data flow analysis</td><td>i</td></tr><tr><td>Functional decomposition</td><td>i</td></tr><tr><td>Production of design and specification documents</td><td>i</td></tr><tr><td>Control of document updates</td><td>c</td></tr><tr><td colspan="2">* Reusable design access</td></tr><tr><td>New code development</td><td>i</td></tr><tr><td colspan="2">* Reusable code access</td></tr><tr><td>Analysis and modification of existing code</td><td>i</td></tr><tr><td>Restructuring of existing code</td><td>c</td></tr><tr><td>Removal of dead code</td><td>i</td></tr><tr><td>Design reviews</td><td>i</td></tr><tr><td>Code inspections</td><td>i</td></tr><tr><td>Personal debugging</td><td>i</td></tr><tr><td>Test case development</td><td>i</td></tr><tr><td>Test library control</td><td>c</td></tr><tr><td>Defect analysis</td><td>i</td></tr><tr><td>User documentation production</td><td>-i</td></tr><tr><td>On-line help and tutorial production</td><td>i</td></tr><tr><td>User training</td><td>i</td></tr></table>

$^{a}$ [20] Jones, T.C., “Why Choose CASE?” American Programmer, Vol. 3, No. 1 (Jan 1990), 14–21.

Table 3  
Categorization of CASE and non-CASE tasks.

<table><tr><td>Task categories</td><td>Clerical</td><td>Indeterminate</td><td>Intellectual</td></tr><tr><td colspan="4">CASE tool tasks</td></tr><tr><td>Henderson and Cooprider (1990)</td><td> $14^a$ (21)</td><td>11(17)</td><td>40(62)</td></tr><tr><td colspan="4">Non-CASE tasks</td></tr><tr><td>Brackett (1989)</td><td>0</td><td>0</td><td>13(100)</td></tr><tr><td>Jones (1990)</td><td>3(17)</td><td>0</td><td>15(83)</td></tr><tr><td>Overall</td><td>17(18)</td><td>11(11)</td><td>68(71)</td></tr></table>

$^{a}$ The table entries are numbers of tasks in each category; the figures in brackets are percentages.

Subjects in this experiment were six graduate students (novice systems analysts) completing a course in software engineering in the business school of a large university. The number of subjects participating in protocol studies is small due to the intensive nature of the subsequent analysis (see, for example, [3,19]). Subjects specified the information requirements for three problems (see, for example, [39]). The order of presentation of two of the problems was counter-balanced. The third problem was not investigated in the research and was always presented as the second problem. Hence, the thinking and drawing times were examined for a total of 12 problems.

The novice analysts received in-class instruction, completed in-class exercises, and a homework exercise using a structured methodology $[4,18,42]$ . Subjects then used these methods to specify the information requirements for the three problems. Subjects studied a problem statement (i.e., case), thought about how to represent the problem in the specification graphic of choice, and then developed the specification graphic and the associated data dictionary manually. (Vitalari $[37]$ and Yadav et al. $[41]$ report similar experimental treatments).

Table 4 presents the results of this study; they are remarkably consistent. Subjects spent, on average, 21% of their time drawing and the rest thinking, the range being 72–85%. The proportion of thinking to drawing time holds for the two problems examined. Drawing time was 20.7% of the total for problem 1 and 21.5% for problem 2. Our evidence suggests, therefore, that for a student population, time spent on the intellectual activities of specifying information requirements is approximately four times that spent on relatively clerical activities. Note, however, that these findings closely parallel those of Fjeldstad and Hamlen [12], who found that professional software maintainers also spent 80% of their time thinking (see Section 2).

Table 4  
Thinking time versus writing time during systems analysis.

<table><tr><td rowspan="2">Subject</td><td rowspan="2">Problem</td><td rowspan="2">Total time (mins.)</td><td rowspan="2">Writing time (mins.)</td><td colspan="2">% of total time</td></tr><tr><td>writing</td><td>thinking</td></tr><tr><td rowspan="2">S3</td><td>1</td><td>153</td><td>23.1</td><td>15</td><td>85</td></tr><tr><td>2</td><td>106</td><td>20.5</td><td>19</td><td>81</td></tr><tr><td rowspan="2">S4</td><td>1</td><td>117</td><td>24.2</td><td>21</td><td>79</td></tr><tr><td>2</td><td>26</td><td>6.8</td><td>26</td><td>74</td></tr><tr><td rowspan="2">S6</td><td>1</td><td>108</td><td>18.7</td><td>17</td><td>83</td></tr><tr><td>2</td><td>60</td><td>12.4</td><td>21</td><td>79</td></tr><tr><td rowspan="2">S10</td><td>1</td><td>51</td><td>11.0</td><td>22</td><td>78</td></tr><tr><td>2</td><td>41</td><td>10.0</td><td>24</td><td>76</td></tr><tr><td rowspan="2">S11</td><td>1</td><td>61</td><td>12.8</td><td>21</td><td>79</td></tr><tr><td>2</td><td>87</td><td>15.3</td><td>18</td><td>82</td></tr><tr><td rowspan="2">S12</td><td>1</td><td>61</td><td>16.9</td><td>28</td><td>72</td></tr><tr><td>2</td><td>67</td><td>14.3</td><td>21</td><td>79</td></tr></table>

There are a number of obvious limitations to this study. First, information requirements analysis is the initial step in the software development process. It might be expected that these types of tasks will be less clerical than those later in the process. Note, however, that there was little difference in the nature of the tasks associated with earlier and later stages of the software development life cycle, as evidenced by Brackett's [5] and Jones' [20] taxonomies (see section 3.1). Second, the subject pool consisted of graduate students with little practical experience in systems analysis. Perhaps experienced analysts would spend less time thinking and more time representing the requirements (writing) in the early phases of the life cycle. Third, the problems addressed in this experiment were, of necessity, fairly simple; they could be addressed within, say, a two-hour period. Note, however, that thinking time may be relatively longer than drawing time when real-world problems are addressed. Hence, the use of simpler tasks offsets the potential bias due to the use of inexperienced systems analysts. Fourth, we conducted an exploratory study that investigated the behavior of a small number of subjects as they specified the information requirements for each of two cases. The findings of this study should be replicated with practising systems analysts involved in developing software solutions to real-world problems.

## 4. Discussion

Our research investigated the nature of software tasks to assess whether software activities are predominantly intellectual or clerical in nature. The issue of the degree of intellectual effort spent in software activities is an important one, as well as being somewhat controversial.

## 4.1. Discussion of findings

The results of our studies, though exploratory, are consistent: Intellectual activities dominate clerical activities in software development.

The overall figures for the number of intellectual versus clerical software tasks and the amount of time spent on intellectual versus clerical activities in systems analysis are surprisingly similar (ratios of four to one), lending credence to our results.

## 4.2. Implications of the findings

From the broad viewpoint of the software development community, the results of this study suggest that software construction is predominantly intellectual in nature, providing evidence that the “anyone can write software” viewpoint is incorrect.

From the viewpoint of research, further studies on this topic are needed. For example, research involving professionals and downstream life cycle activities should be conducted to determine whether the results of the current study are generalizable. Further, research is needed toward developing a taxonomy of software tasks. The tables of tasks presented in this paper, although representative of the state of the practice, need improvement in the areas of completeness, uniqueness, and categorization.

Taxonomies of software tasks could potentially impact many aspects of software development. From the viewpoint of education, software task taxonomies would permit educators and textbooks to focus on the intellectual tasks of software. Educators could present diagram drawing, for example, as an exposure to representational techniques, leaving development of drawing skills to industrial training.

From the viewpoint of the software automation industry, tools vendors could use the intellectual nature of software tasks to identify where their products fit in the “software automation” process. Given that vendors often claim more than their tools can actually deliver, a tools taxonomy that distinguished between clerical and intellectual assistance could help clear the air for both purchasers and vendors.

Research into taxonomies could also pay off in the area of end-user computing. Problem-solving via software requires both application skills and software-specific skills. Better understanding of software tasks could lead to measures of the end-users' software knowledge to determine when sufficient skills are available to build software solutions, when additional skills or training are needed, and when software skills are not needed.

In the past, software developers have been hired with a wide variety of backgrounds, ranging from two year college degrees to master's degrees and higher. Although the application to be implemented will continue to be a determinant of the needed educational background, understanding the intellectual component of software tasks may play a larger role than some have previously thought, suggesting that developers may need a higher level of education.

Whether the IS function should be managed by a person with a technical or a managerial background has long been the subject of debate (see, for example, [17]). This study shows that there may be a significant and fundamental gap in management's understanding of software development. With the realization that software tasks are predominantly intellectual comes a strengthening of the case for managers who understand the technology and the tasks. Education for managers with little direct software experience might therefore include such topics as “managing for innovation” (see, for example, [16]).

## 5. Conclusions

Our research sought empirical evidence on the nature of software tasks to assess the claim that little expertise is required to perform them. Apparently even simple tasks are more intellectual than the “software development can be automated” or the “anyone can do it” viewpoints expressed in the introduction. Researchers interested in automating the software development life cycle and vendors engaged in developing automated products need to address the types of aid that automated tools can provide to different types of tasks in the software development process.

## References

[1] Baker, F.T. "System Quality Through Structured Programming", AFIPS Conference Proceedings FJCC, Part 1, 1972, pp. 339-343.

[2] Bertolino, A. "An Overview of Automated Software Testing". Journal of Systems and Software, Vol. 15, No. 2, May 1991, pp. 133–138.

[3] Biggs, S.F., Bedard, J.C., Gaber, B.G., and Linsmeier, T.J. “The Effects of Task Size and Similarity on the Decision Behavior of Bank Loan Officers”, Management Science, Vol. 31, No. 8, (August 1985, pp. 970–987.

[4] Booch, G. Software Engineering with Ada, 2nd edition, Benjamin/Cummings Publishing Company, Menlo Park, CA, 1987.

[5] Brackett, J.W. "Software Requirements", Software Engineering Institute, SEI-CM-19-1.1, 1989.

[6] Brooks, F.P. “No Silver Bullet: Essence and Accidents of Software Engineering”, IEEE Computer, Vol. 20, No. 4, April 1987, pp. 10–19.

[7] Caldwell, B. "CIO: Hype and Reality", Information Week, March 5, 1990, pp. 45–46.

[8] Canning, R.G., (ed.) “Application Packages Revisited”, EDP Analyzer, Vol. 9, No. 7, July 1971.

[9] Cohen, J. “A Coefficient of Agreement for Nominal Scales”, Educational and Psychological Measurement, Vol. 20, 1960, pp. 37–46.

[10] DeMarco, T. Structured Analysis and Design Specification, Prentice-Hall, Englewood Cliffs, NJ, 1979.

[11] DeMarco, T. and Lister, T. Peopleware, Dorset House, New York, NY, 1987, p. 118.

[12] Fjelstad, R.K. and Hamlen, W.T. “Application Maintenance Study: Report to Our Respondents”, Proceedings of GUIDE 48, The Guide Corporation, Philadelphia, PA, 1979.

## Research

[13] Gane, C. and Sarson, T. Structured Systems Analysis: Tools and Techniques, Prentice-Hall, Englewoods Cliffs, NJ, 1979.

[14] Gibson, V.R. and Senn, J.A. System Structure and Software Maintenance Performance, Communications of the ACM, Vol. 32, No. 3, 1989, pp. 347–358.

[15] Henderson, J.C. and Cooprider, J.G. "Dimensions of IS Planning and Design Technology", Information Systems Research, Vol. 1, No. 3, 1990, pp. 227–254.

[16] Humphrey, W.S. Managing for Innovation: Leading Technical People, Prentice-Hall, Englewood Cliffs, NJ, 1987.

[17] Ives, B. and Olson, M.H. "Manager or Technician?: The Nature of the Information Systems Manager's Job", MIS Quarterly, Vol. 5, No. 4, December 1981, pp. 49–63.

[18] Jackson, M. System Development, Prentice-Hall, Englewood Cliffs, NJ, 1983.

[19] Johnson, P., Duran, A., Hassebrock, F., Moller, J., Prietula, M., Feltovich, P. and Swanson, D. “Expertise and Error in Diagnostic Reasoning”, Cognitive Science, Vol. 5, 1981, pp. 235–283.

[20] Jones, T.C. "Why Choose CASE?", American Programmer, Vol. 3, No. 1, January 1990, pp. 14–21.

[21] Martin, J. Application Development Without Programmers, Prentice-Hall, Englewood Cliffs, NJ, 1982.

[22] Martin, J. In: Martin, J., Bernstein, P., Denning, P., Dertouzos, M., and Kleinrock, L., eds., “Computer Science Education Today: A Dialogue”, Communications of the ACM, Vol. 28, No. 3, 1985, pp. 251–262.

[23] Martin, J. and McClure, C. Structured Techniques: The Basis for CASE, 2nd edition, Prentice-Hall, New York, 1988.

[24] MBA. “More on MBAs in MIS”, Information Week, Fax Forum, March 19, 1990, p. 56.

[25] McClure, C. “The CASE for Structured Development”, PC Tech Journal, August 1988, pp. 51–67.

[26] McClure, C., CASE is Software Automation, Prentice-Hall, Englewood Cliffs, NJ, 1989.

[27] McCormick, E.J. and Ilgen, D.R., Industrial Psychology, 7th edition, Prentice-Hall, Englewood Cliffs, NJ, 1980.

[28] Newell, A. and Simon, H.A. Human Problem Solving, Prentice-Hall, Englewood Cliffs, NJ, 1972.

[29] Ng, P. and Yeh, R.T., eds. Modern Software Engineering:

Foundations and Current Perspectives, Van Nostrand Reinhold, New York, 1990.

[30] Page-Jones, M. The Practical Guide to Structured Systems Design, Prentice-Hall, Englewood Cliffs, NJ, 1980.

[31] Parnas, D.L. “Software Aspects of Strategic Defense Systems”, American Scientist, Vol. 73, No. 5, November 1985, pp. 432–440.

[32] Parnas, D.L., Clements, P.C. and Weiss, D.M. “The Modular Structure of Complex Systems”, IEEE Transactions on Software Engineering, Vol. 11, No. 3, March 1985, pp. 259–266.

[33] Rich, C. and Waters, R. “Automatic Programming: Myths and Prospects”, IEEE Computer, Vol. 21, No. 8, August 1988, pp. 40–51.

[34] Singleton, W.T. The Mind at Work: Psychological Ergonomics, Cambridge University Press, Cambridge, 1989.

[35] Souza, E. "The New CASE Development Life Cycle", Software Engineering: Tools. Techniques, Practice, Vol. 1, No. 3, September–October 1990, pp. 14–21.

[36] USNRC “Scaling Up: A Research Agenda for Software Engineering”, Computer Science and Technology Board, U.S. National Research Council, 1990.

[37] Vitalari, N.P. “Knowledge as a Basis for Expertise in Systems Analysis: An Empirical Study”, MIS Quarterly, Vol. 9, No. 3, 1985, pp. 221–241.

[38] Weinberg, G., Understanding the Professional Programmer, Dorset House, New York, NY, 1988.

[39] Whitten, J., Bentley, L. and Barlow, V.M. Systems Analysis and Design Methods, 2nd edition, Irwin, Homewood, IL, 1989.

[40] Woodfield, S. "An Experiment on Unit Increase in Program Complexity", IEEE Transactions on Software Engineering, March 1979.

[41] Yadav, S.B., Bravocco, R.R., Chatfield, A.T. and Rajkumar, T.M., “Comparison of Analysis Techniques for Information Requirement Determination”, Communications of the ACM, Vol. 31, No. 9, 1988, pp. 1090–1097.

[42] Yourdon, E. Modern Structured Analysis, Prentice-Hall, Englewood Cliffs, NJ, 1989.

[43] Yourdon, E. and Constantine, L.L. Structured Design, Prentice-Hall, Englewood Cliffs, NJ, 1979.
