---
otero_id: 23477
otero_key: "SM3SQY3G"
title: "Experiments with expert systems in management education"
authors: "Malcolm King; Laurie McAulay"
year: "1991"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1991.5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Experiments with expert systems in management education

MALCOLM KING\* and LAURIE MCAULAY†

\*Loughborough University of Technology and †University of Bath

Abstract: A simple system has been developed using expert systems technology to assist lecturers in teaching specific groups of professional and management students. To enable comparisons to be made, two versions of the system were built; one in prolog and one in an inexpensive expert system shell. The systems were designed to relieve lecturers by providing answers and explanations for examination questions in the area of standard costing. The experiments show that such simple systems can be developed by lecturers for their own use, although there are limitations, especially in the knowledge which can be captured. Testing of the system in practice has shown benefits in terms of reduced lecturer load and positive responses from students. The experiments show that integrating simple expert systems into the education process can be beneficial when the technology is adapted to match the educational requirements.

## Introduction

Duchastel and Imbeau (1988) note that 'contemporary education has the task of integrating ... new technology into the education process in order to profit from its promise of contributing to enhanced student learning'. One particular aspect of this promise may be the use of simple expert systems in supporting and relieving lecturers. To investigate this promise two simple systems using expert systems technology have been built and tested for use in professional accounting and general management education.

Simple expert systems appear to be worthy of investigation because of the opportunity for lecturers themselves to develop the teaching material. Harmon and King (1985) argue that it is possible for experts to develop their own simple expert systems and King (1989) has shown that suitably skilled experts can build useful systems using, commercially available expert system shells. In order to test the general applicability of the approach, the systems were developed by teaching staff from management science and accounting backgrounds within time constraints and the benefits achieved related to those time inputs. The following sections explain the choice of area, the planned use of the system and the resources used. Details of the systems are then provided. Subsequent sections describe the benefits achieved and the problems arising before providing an evaluation of the systems developed and forming conclusions about the approach based on the experiences.

## Scope and use of the systems

Selection of an appropriate specific area in which to experiment with expert systems technology would appear to be important to success (Connell, 1987). Previous experience of the researchers in developing software for student use has shown that there are differences in students' reactions to computers in courses depending on the type of course and type of student. It was decided to develop systems in the general area of Management Accounting rather than Management Science. This meant that systems could be tested on courses with different modes of attendance and levels of student maturity as well as contrasting courses aimed at professional qualifications with those providing a more general management education. Using criteria based on Wolfgram et al (1987) and Assad and Golden (1988), the area of standard costing was chosen for the following specific reasons:

(1) Text books have codified the knowledge area to the point at which there seems to be a good level of consensus;

(2) It is possible to define a useful and relatively small area from which initial development work could hope to succeed in a relatively short period of time. There is substantial opportunity for the system to grow out of its initial confines;

(3) Groups of students existed for whom the system could be expected to have utility. These groups included full and part-time students on post-graduate courses as well as full and part-time students studying for professional qualifications;

(4) A saving in lecturer's time was considered to be possible.

In designing a system for educational purposes, it is necessary to define the relevant expertise to be incorporated and consider the existing learning strategy. To assist this process a questionnaire was issued to 107 students and observations of lecturing practice were carried out. Analysis of the questionnaire suggested that the students valued most highly the lecturer who could answer examination question problems and provide good explanations. It was therefore decided to experiment with systems which provided answers and explanations for past examination questions. Observation of lecturers suggested that it was necessary for the module to enable students to check their own results and have access to the knowledge which created the answer.

At the research site, standard costing was taught routinely to a number of different groups, and three groups were identified as suitable for the experiments. Group A consisted of ten students on a part-time course and group B comprised twenty students undertaking day release studies towards the same professional examinations. Group C was a group of forty full-time students studying for examinations set by course lecturers.

The learning strategy used at the research site varied between groups, depending on the examinations to be taken and the mode of attendance. Group A was usually scheduled to have a lecture immediately followed by a session which allowed students to work through problems taken from past examination questions. After attempting the problems, students would look to lecturers to supply answers and explanations. During the experiments an attempt was made to try and provide answers at the appropriate stage of a class by displaying microcomputer output from the system via an overhead projector and invite students to ask questions about any of the answers provided. Explanations would then be projected from the system to cover the areas as requested. Finally, if further information was required, the lecturer would provide a verbal explanation and use the blackboard if necessary.

The same approach was selected for group B, but some of the problem material was set for students to complete in their own time, for review in the following class session.

Group C's schedule involved lectures to the whole group backed up by seminars with groups of around twenty students and tutorials for groups of a maximum of five students. In the experiments, it was planned to make the system available to students on a microcomputer in the library and students were given a sheet of instructions on how to use the system. Tutorials were cancelled and students were invited to use the system to check answers to problems issued in lectures. Students could still consult lecturers, could check answers with each other or could use a library stock of suggested answers. Lectures and seminars ran as normal in order to provide the required teaching input.

## Resources used

The first version of the system was written in prolog and the second in an inexpensive personal computer-based expert system shell. The total cost of this software was less than £250. Both systems were designed to run on a standard IBM compatible personal computer with a hard disk, running under MS-DOS. Prolog was selected as the initial development tool since the features it provides closely matched the requirements of the situation, including the ability to produce prototypes rapidly (Hammond, 1987). This was important to minimize development costs. In order to develop the systems, the lecturers had to gain expertise in prolog at the start of the exercise. Once a sufficient level of expertise had been achieved, the finished prolog prototype, referred to as STD1, was developed in one man-month. Further prolog expertise was gained during this development period mostly concerned with input and output protocols.

The second version of the system, referred to as STD2, was built using the expert system shell. The choice of an inexpensive shell was based partly on budget constraints and partly because of the trade-offs between complexity and simplicity discussed by Garson (1987). He suggested that 'less powerful software may be more effective for instruction with specific, limited objectives'. Again, the lecturers had to gain expertise in the use of this particular shell, but once this had been achieved, a version with similar functionality to STD1 was completed in 3 man-days. An extended version, with more explanation facilities and additional classification rules, took an additional week to develop.

## Description of the prototypes

STD1 combines knowledge of how to calculate variances with knowledge of types of examination questions. In one mode of usage, STD1 allows the entry of examination problems. Using knowledge of standard costing, a series of questions is asked in order to form a classification of the problem. Once a problem has been classified, questions are asked in order to extract data about the examination problem in accordance with a pre-determined formula approach to variance analysis. A database entry is created within the prolog program and saved with it. Problems may be entered by lecturers, in advance of sessions or may be entered by students prior to usage in the second mode.

In the second mode the user consults STD1 and specifies a problem to be solved. The database itself then fires prolog rules which contain knowledge of the appropriate formula for variance calculation. This largely procedural phase, with a substantial deterministic and calculative element, is not a customary use of expert systems (Wolfgram et al., 1987). Unusual as it seems, it was found that incorporating the calculations into the system itself appears to be an effective way of optimizing flexibility and efficiency for the system as a whole. The results of the variance analysis are then displayed and can be checked by students against their own calculations. If explanations are required, students can ask for further information related to any part of the results by means of a simple sequence of input key strokes.

It is felt that STD1 is better described as a knowledge base than an expert system. The way in which the explanation facility operates and the avoidance of probabilistic reasoning differs from most expert systems whilst embodying knowledge base and expert systems concepts.

STD2 adopts the same basic approach as STD1. It differs technically from STD1 because the rule-based expert system shell does not offer the same flexibility in data handling as prolog. Additionally, some of the features of STD1 have been extended. STD2 was built incrementally to test the ability to make changes easily and to accommodate new knowledge. A database file was maintained externally to the shell and rules were used to both update and retrieve data. The database was designed as simply as possible to minimize design time and has an inherently flat structure. Differences between examination questions require different types of loading of the database. Each database record was coded by the expert system shell based on the question classification. This code was then used to fire particular rules when the variance calculation was required. The explanation facility, which used rules rather than the shell's inherent explanation mechanism, was extended to provide a second level of explanation. The first level was comparable to STD1 and was partially driven by the classification in the database and partially driven by user input. The second level was built into the system as external files created by the lecturer using wordprocessing facilities and readable by the expert system shell when the student made the appropriate menu selection. These explanations were at a general level and not specific to individual problems.

Input was limited to yes/no responses and simple numerical keying for STD1 or menu responses and numerical keying STD2. Machine inferencing involved a mixture of backward and forward chaining for both systems. For output, control over numerical data was necessary, using product specific predicates or rules.

## Explanation facilities

Explanations in expert systems typically recall the chain of rules which are used to arrive at a particular conclusion. However, this was not considered sufficient in this case. Lecturers tended to use standard formats based on compiled knowledge into which data from problems could be slotted. Observation of lecturers' practice showed two types of formats commonly used at the research site. For the groups chosen for the exercise, different teaching would have been experienced by students who would be familiar with one but not both types of format. It would therefore be impossible to provide a single format to which all students in a group could readily relate. For this reason, the first level of explanation in both STD1 and STD2 comprised data descriptions and items of data in a generalized form.

The basic data values appearing within explanations could take one of two forms. First, the values could be directly available within the examination question. Alternatively, given the large variety of ways in which data could be presented in questions, the values in the explanations might be a combination of two or more figures given by a particular question. A calculation based on the figures in the question would have been necessary when the database was loaded. The latter kind posed a problem for the student in that there is a need for a greater degree of inferencing in order to reach an understanding of explanations provided. Values appearing in an explanation cannot be found directly in the examination question and the student would thus need to match an explanation value with two or more figures in the question. STD2 reduced the gap between figures in the examination question and values in the database. The less coarsified classification of STD2 required to close the gap is achieved at a cost in terms of extending the knowledge coding and increasing the testing and debugging time.

## Evaluation

Doubt was known to exist as to the feasibility of using an expert systems approach in the chosen domain. Quere (1985) found another area of accountancy difficult to codify for reasons which appeared to be applicable to standard costing. Establishing the feasibility of the basic idea of coding costing knowledge was therefore an important part of the experiment. From the educational point of view, qualitative evaluation was adopted due to the early stage of the testing. It is hoped to measure the differences between assessment results of research subjects and control groups in future trials of the systems.

To test the knowledge contained within STD1 and STD2, all the examination questions which could be construed as standard costing problems were taken from papers set in the previous 6 years. On these problems the system worked effectively. No redundant questions were asked when loading the problems, the calculated answers were in accord with manually produced answers and the explanation facility functioned as intended.

Table 1 Capacity and efficiency measures

<table><tr><td></td><td>STD1</td><td>STD2</td></tr><tr><td>Memory used by knowledge base text</td><td>12.2 Kb</td><td>51.1 Kb</td></tr><tr><td>Number of predicates/rules</td><td>68</td><td>124</td></tr><tr><td>Time to load Prolog/Shell</td><td>4 seconds</td><td>1 second</td></tr><tr><td>Time to load a knowledge base</td><td>6 seconds</td><td>7 seconds*</td></tr><tr><td>Time to ask lecturer a question</td><td>Instant</td><td>Instant</td></tr><tr><td>Time to provide result of a calculation</td><td>Instant</td><td>3 seconds</td></tr><tr><td>Time to provide explanation</td><td>Instant</td><td>1 second</td></tr><tr><td>Time to enter a problem</td><td>4.5 mins</td><td>3.5 mins</td></tr></table>

\*7 seconds are necessary each time one of the two modules is loaded. In normal use this 7 second wait is occasionally experienced by the user

Efficiency measures are included in Table 1, which provides comparable data for STD1 and STD2. In practice, efficiency did not appear as a problem in that all response times appeared to be reasonable, apart from the loading time for STD2 in its fully developed form. As STD2 was extended, machine memory capacity became a problem and it was necessary to break the system into two chained modules. Switching from one module to the other was necessary, in practice, and the time to load each knowledge-base detracts from the acceptability of STD2 from the point of view of the user. Whilst an initial loading time for the knowledge-base of around 7 seconds appears acceptable, a repeated waiting period of this duration is less than satisfactory. However, this only occurred when changing between different types of problems. Most responses from the computer were effectively instantaneous in the practical operation of the system.

In student use, the evaluation was encouraging. Group A received the presence of technology in the classroom with enthusiasm. A saving of 4 hours in teaching time was achieved by comparison with courses delivered in previous years, primarily because of a saving in time to write explanations on the board. The time saved was used for other teaching necessary to meet syllabus requirements. These benefits were not repeated for group B because the projection facilities proved to be unsuitable for the size of group and room characteristics. Group C was given a short attitudinal questionnaire in class. Of those using STD1, 78% felt that some benefit had been received. Informal feedback was enthusiastic with some students reporting that micro-computer use was stimulating and provided good experience.

In the case of one student from group C, who was particularly weak, substantial lecturer time was saved at no loss of benefit to the student. The student had severe learning difficulties and at the end of a session asked for further assistance. To resolve the problem, the lecturer spent ten minutes providing an introduction to STD1 and left the student to work on further problems. Four hours later, a jubilant student reported success and the lecturer was able to ascertain that the student had resolved the previous learning difficulties effectively. No problem in using STD1 had been experienced.

## Discussion

Evaluation of the experiments suggested that continued use of the product could show a direct payback of the relatively small inputs in a matter of 2 or 3 years. In hindsight, the time inputs would have been minimized by coding STD1 within a single module of the expert system shell. This would have minimized learning time from the point of view of the lecturer, taken an estimated 3 man-days for an experienced expert system shell user and cost £120 for the particular shell. Quantifiable benefits of approximately 1 man-day resulted from the limited testing of the product by one lecturer over one teaching cycle. Qualitative benefits such as the provision of individualized learning, especially for weaker students, and the fresh view of the subject area provided for the lecturer (by the need to code knowledge), would appear to be of importance. The key to the payback situation is the flexibility of the product. A number of different problems can be added to the system's database. Students can spend as much time as is necessary for them to gain proficiency in a particular problem area. As new questions are set by lecturers or the professional bodies, the basic program does not need to be re-written. The product should be relevant for several years and could be used by other lecturers at the same institution. Alternative approaches, such as providing spreadsheet answers or templates would seem to be less flexible since new problems would require new spreadsheets.

The experiments described here began with the aim of building systems using expert systems technology yet it was necessary to adapt the underlying technology, particularly in relation to the explanation facility, in order to create a knowledge base. The implication of this research to the debate on the value of such systems to education would appear to be that the technology needs to be carefully applied to meet specific educational requirements.

## Conclusions

The experiments involved systems which were tightly constrained in order to assess the feasibility of using small systems in the classroom and to provide the opportunity to balance costs and benefits within a short period of time. Students benefited from the availability of a backup for lectures and a substitute for tutorials. Lecturers benefited from a saving in teaching time, particularly with regards to providing explanations to weaker students. The flexibility provided by the expert systems approach, which permits a range of situations to be catered for, appeared to be advantageous in comparison with other approaches such as the use of spreadsheets.

Such systems can be developed quickly and easily in an expert system shell and relatively easily in prolog. Success relies on adapting the existing technology to meet particular educational requirements. Small expert systems appear to hold good prospects for the successful development of useful systems in general (King, 1989) and in education in particular, given careful selection of appropriate educational objectives.

## References

Assad, A.A. and Golden, B.L. (1988) Expert systems, microcomputers and operation research, Computer and Operations, Research, 63, 301–321.

Connell, N.A.D. (1987) Expert systems in accountancy: a review of some recent applications, Accountancy and Business Research, 17, 221–223.

Duchastel, P. and Imbeau, J. (1988) Intelligent computer assisted instruction (ICAI): flexible learning through better student-computer interaction, Journal of Information Technology, 3, 102–105.

Garson, G.D. (1987) Academic Microcomputing: a resource guide, Sage, London.

Hammond, P. (1987) Logic-based tools for building expert and knowledge-based systems: successes and failures in transferring the technology, in Knowledge-based Expert Systems in Industry, Kriz, J. (ed), Ellis Horwood, Chichester.

Harmon, P. and King, D. (1985) Expert Systems; Artificial Intelligence in Business, Wiley, New York.

King, M. (1989) Experiments with experts developing simple expert systems, Omega, 17, 123–134.

Quere, M. (1985) Expert systems: towards CAI of the future?, in Proceedings of the IFIP Fourth World Conference on Computers in Education, Duncan, K.A. and Harris, D.I. (eds), July 29-August 2, North Holland, New York.

Wolfgram, D.D., Dear, T.J. and Galbraith, C.S. (1987) Expert systems for the Technical Professional, Wiley, Chichester.

## Biographical Notes

Malcolm King is Professor of Management Sciences in the Loughborough University Business School. His initial training was in mathematics and throughout the 1970s and 1980s he taught the use of mathematics, statistics and computers in management to management students. Over the last 10 years his research interests have developed to include the impact of information technology on all areas of management, particularly accounting, including considering the organizational and political aspects as well as the technical. Recently, he has worked on several projects concerning the development of expert systems in different areas of management.

Laurie McAulay is currently a lecturer in Accountancy at the University of Bath. During the 1970s he qualified as a professional accountant and practiced as a Management Accountant in several large organizations. For the last 10 years he has taught on a variety of professional accounting, undergraduate and MBA programmes. His research interests are in the areas of the relationships between information technology and management accounting and the development of expert systems in accounting.

Address for correspondence: Professor Malcolm King, Loughborough University Business School, University of Technology, Loughborough, Leics., LE11 3TU
