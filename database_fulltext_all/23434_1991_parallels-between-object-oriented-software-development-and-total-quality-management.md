---
otero_id: 23434
otero_key: "K3JB4E6W"
title: "Parallels between object-oriented software development and total quality management"
authors: "B Henderson-Sellers"
year: "1991"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1991.11"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Parallels between object-oriented software development and total quality management

B. HENDERSON-SELLERS

School of Information Systems, University of New South Wales, New South Wales

Abstract: The object-oriented (OO) approach to building information systems, if applied correctly, can greatly enhance the quality of the finished software product. This emphasis on greater quality is paralleled by the management philosophy known as Total Quality Management (TQM). Based on the common theme of 'quality', parallels are drawn between the OO and TQM philosophies in order to optimize on the benefits to quality software engineering offered by the object-oriented approach.

## Introduction

Total quality management is a modern management philosophy, developed essentially in industrial and commercial environments. It focusses on the concept of quality which it identifies as arising from the process central to the particular project/industry. A quantitative (statistical) study of this central process can highlight improvements which management (but not workers) can make to the system itself. The application of object-oriented ideas to the management of software development is also aimed at improving the quality of the finished product. The aim of this paper is to explore parallels between these two new philosophies and to identify possible synergistic elements.

## The object-oriented philosophy

The object-oriented approach to information systems is not new, dating back some 20 years. However, over the last few years its applicability to modern MIS problems, together with contemporary announcements in terms of new language support, have begun to be realized over a wide range of industries and commercial organizations (Howard, 1988). Application areas such as MIS and DSS are likely to see a rapid growth in the use of object-oriented techniques. Meyer (1989a) is ‘particularly excited by the applications to the MIS/EDP world. I think the business data processing community desperately needs object-oriented techniques.’

The basic ideas of object-oriented information systems extend the old ideas and introduce several new ideas. These are focussed upon

(1) Encapsulation or information hiding.

(2) Inheritance (by which code can be reused and commonality factored out based on ideas of subsets and supersets).

(3) Data abstraction (by which classes of like objects can be described by a template of common code) see Figure 1.

![](/api/attachments/K3JB4E6W/fulltext/images/d7c1e78d911ddc561bcf01d804cbbafedc985d9ae27880dd01f538ba9fd3ddaf.jpg)  
Figure 1 Object-oriented triangle emphasizing the links between the three apexes representing the three basic concepts embodied in an object-oriented approach: inheritance, encapsulation and classification.

Together these new language capabilities are able to provide an easy environment in which to implement these concepts. This has led directly to the likelihood that some of the software engineering goals of the last few decades may become a step nearer. Code and design reusability, a high level of correctness and integrity (i.e. prevention of unauthorized 'meddling'), and lower maintenance costs all combine to offer the software engineer a means of producing higher quality software products (Table 1).

It is important to note, however, that the object-oriented (OO) philosophy is not simply a new set of rules by which today's analysts, designers and programmers can accomplish better standards overnight. In order for the full power of object-orientation to be realized, it is necessary to acquire a new mindset. Problems must no longer be viewed as functional or procedural (here used as synonyms, i.e. functional will not be used in the sense of functional programming languages such as Miranda\*). Instead of asking what the system does, analysts must ask the following questions: (1) what objects comprise the system? and (2) what are their characteristics (attributes) and behaviour (functionality)?

Table 1 Attributes of software quality

<table><tr><td colspan="2">(after Thomsett, 1990)</td></tr><tr><td>Conformity</td><td>Portability</td></tr><tr><td>Reliability</td><td>Usability</td></tr><tr><td>Maintainability</td><td>Auditability</td></tr><tr><td>Reusability</td><td>Security</td></tr><tr><td>Efficiency</td><td>Flexibility</td></tr></table>

It has already been noted that many of the object-oriented (OO) ideas can be found in older writings. For example, the ideas of information hiding date back to a paper by Parnas (1972). In this instance the twist of viewpoint is to add to the (old) ideas of a high degree of encapsulation the requirement that in an OO software system each encapsulated module is identified with an abstract data type (ADT). This is simply a formal way of saying that each module is written to represent a class of similar objects and can thus be described as an abstraction. Similar variables are now grouped together and common features factored out into a class (a coded template of all such objects) which is the implementation of the ADT.

An object-oriented information system therefore consists of a number of coded classes which represent the sets of objects identified at the analysis and design stages of the software lifecycle. These classes can also be understood as user-defined types (Stroustrup, 1988). As such they can be manipulated in the same range of ways that standard and immediately recognizable types such as INTEGER, REAL, and CHARACTER can be manipulated in the current procedural framework. At program execution time, individual instantiations of these classes provide the runtime objects (equivalent at one level to variables in the procedural language sense) which represent specific examples of the classes. These are created as and when required by the system and when no longer required the memory space they occupy should be automatically reallocated (Meyer, 1988).

Coded classes and runtime objects thus share the characteristics of data plus functionality plus encapsulation - basic characteristics of an object-oriented approach to software development.

## Total quality management

Total quality management (TQM) has its origins in seminars presented to the Japanese by American experts after the Second World War. Although seen to be applicable in the Japanese environment, it was doubted for many years whether the Western culture was amenable for the support of the ideas originally proposed by Deming and his colleagues (Deming, 1981). However, the success of Japanese industry has caused industries in the USA, Europe, Australia etc. to reconsider and to investigate actively the possible adoption of, for instance, Deming's '14 points'.

Zultner (1988) examines the interpretation of these 14 points to software quality engineering. The 14 points (see Table 2) are accomplished, in part, by

## Table 2 Deming's fourteen points

1. Create constancy of purpose
2. Adopt the new TQM philosophy
3. Evaluate the system objectively and quantitatively
4. Don't award business on price tag, rather on quality
5. Aim for constant improvement
6. Institute on-the-job training
7. Institute leadership rather than control
8. Drive out fear (of punishment)
9. Break down inter-departmental barriers (and rivalries)
10. Eliminate slogans (which are usually not achievable)
11. Eliminate numerical goals and objectives (including MBO)
12. Give workers pride in their work
13. Institute programmes of self-improvement
14. Involve everyone

diagrammatic tools such as Pareto charts, control charts, histograms and scattergrams. The use of quantitative and statistical tools underlines not only point 3, but provide a rationale on which several of the other points are based (e.g. points 2, 4, 5, 6). Education and training are also major factors as are leadership and constancy of purpose, which should be obvious to all employees. Enhanced interaction between departments and between workers and management assist in accomplishing a continuous improvement in quality engendered to a significant degree by the pride which all workers can have in their accomplishments. Total quality management, as practised in commercial organizations, can thus easily be translated to MIS/DP departments and to software development houses (Zultner, 1988).

TQM embodies many of the best parts of old management philosophies but seen from a different angle. For example, although Deming stresses that management by objectives (MBO) must be eliminated, the idea of goal setting is retained in the TQM philosophy with the twist that says that once attained, new goals must be set in order to accomplish gradual and continuous improvement.

In the software industry, plagued by overruns and poor quality, the TQM approach would seem to be a godsend. Indeed Software Quality Assurance professional groups around the world are rapidly gaining both strength and visibility within the community. In Australia, the Software Quality Association, itself a Special Interest Group of the Australian Computer Society, is running certification courses designed to meet both Australian and international quality standards.

The new quality emphasis is epitomized by 'Joiners Triangle' (Figure 2) (Joiner and Scholtes, 1986) in

![](/api/attachments/K3JB4E6W/fulltext/images/3d9dfcec26d1e47346da5d025e6176c0ecc2e2db1c18fe1083ae5ef58826cd9e.jpg)  
Figure 2 Joiner's Triangle emphasizing the links between the three apexes of quality, the scientific (data-driven) approach and teamwork. The labels in square brackets reflect the associated attitudes of commitment, practice and culture which synergistically combine to support the ethos of continual improvement

which quality is at the top apex of a triangle with supporting vertices of 'scientific approach' or 'data-driven decision-making' and 'implementation by teamwork'. Both these supporting concepts provide a solid support for the attainment of quality. This new quality-focussed culture can also be seen as striving for continual improvement, in which frame of reference the vertices of the triangle can be relabelled, more abstractly perhaps, as 'practice' and 'corporate culture' supporting a 'commitment' to the central goal of continual quality improvement.

## Direct parallels

As noted above, both the TQM and OO philosophies require a different mindset for the full utilization of their essentially holistic design. Both are evolutionary rather than revolutionary with pedigrees dating back over 20 years. As with all new developments there is a synergistic combination of established ideas together with some new ideas.

Some of the 14 points in Table 2 can usefully be examined directly in terms of parallels in the object-oriented philosophy. As with any new ideas, there may be a tendency to 'jump on the band wagon'. However, a corporation with such a tendency is just as likely to jump off the wagon when a newer one appears around the corner. Such a migratory perspective leads to a multitude of abandoned practices, abandoned projects, disillusioned professionals, etc. With the increasing emergence of the object-oriented philosophy into the corporate consciousness, it is important that a leadership decision is made to adopt the new ideas (point 2) and embody them within a strategic planning framework (point 1). With both TQM and object-oriented software development, there is bound to be an initial drop in productivity as the new tools are learned. However, both are essentially long term investments and the ultimate goal is that a higher quality product (Table 1) will ensue which will take less time and cost less. This is seen particularly in the additional time (cf. normal one-off software projects) which is needed to build up the software libraries vital for the feasibility of the reusability aspects of the object-oriented technology. Indeed it is in the development of the library classes that quality can be built in.

Current software development practices essentially have a 'build fast, test later' attitude in which the calling routine checks the validity of the answers derived by the subroutine (at least if the programmer remembers to code in adequate checks!). This means that even with subroutines designed to be archived and reused in a later project, there is no quality assurance that they will perform adequately (and safely) in the new environment which will inevitably be slightly different to that for which the subroutine module was originally designed and used.

In developing object-oriented library classes (e.g. Meyer, 1990), it is vital (and indeed perfectly feasible) that correctness, robustness, integrity etc. (in other words, quality) (Meyer, 1989b) be built into each class module before acceptance into the reuse library. Continuous monitoring of these classes during the development process, using safety mechanisms such as assertions (Meyer, 1989b) permits a continuous assessment (point 3) to be made. In addition, the highly iterative nature of this generalization process (e.g. Henderson-Sellers and Edwards, 1990) permits classes destined for generic libraries to be both closed (in the sense of being reliable classes available to the general software developer) and open (in the sense of being easily improved (Meyer, 1988)) (point 5). The ability for such built-in quality must mean that modules of code carefully developed in such a quality managed environment will be purchased on an evaluation based on this stated quality, rather than on price (point 4); although appropriate software metrics, in the strict sense, have yet to be developed. Additionally, it might be anticipated that software developers of truly generic and useful classes will indeed take pride in a job well done (point 12).

Deming's points 8–11 are less easily paralleled in the object-oriented approach. Cooperation between objects is clearly evident in any object-oriented software system. However, in one sense this is only achieved by building tight barriers around each module (the idea of tight encapsulation). Nor have slogans ever had any place in this approach. These four points could, no doubt, be addressed within the context of the management structure of a software developer, but in the context of the management philosophy utilized, rather than within the context of the object-oriented philosophy per se.

The arguments on the best method of introduction of both TQM and OO also have strong similarities. Although top commitment is necessary (point 7), it is also important that the practitioners understand and sympathize with these new approaches (point 14). Consequently, education and training programmes throughout the company are necessary (points 6, 13) (Wybolt, 1990). However, it is debatable whether a total commitment should be made immediately; or whether it is more realistic to replace the management philosophy incrementally. TQM experiences show that successful implementation can occur in one of two ways: either management itself learns the philosophy before disseminating, via leadership, the new management methodologies to the workers or else small groups of enthusiasts are given the resources to try out the ideas at a lower level (but with management's blessing). In an object-oriented framework the ideas may be tried out in a prototyping environment or in a non-critical software development project.

Further, more trivial parallels can be drawn. In TQM there is more equality insofar as management participation is enhanced, especially in quality audits (Shimoyamada, 1987). Using an object-oriented approach, there is no longer a main program driving all its subroutines, but the program (renamed a system to reflect the new thinking) is now composed of a number of autonomous modules (coded classes) all with equal rights.

## OO and TQM in practice

One of the promises of OO is greater safety, quality and reliability in large and very large projects. However, there is, as yet, little empirical data to support this promise. It has become clear that initially small projects should be initiated using OO techniques (Goldberg and Rubin, 1990). When the first OO project attempted is of a large scale, problems have been encountered with project management in the new environment, sometimes worsened by technical hitches (Leathers, 1990). However, there is a growing number of reports of highly successful use of OO techniques. In the cash management arena, McCullough and Deshler (1990) report that 'prospective users were amazed' by the WyCASH+ system; and on-the-fly modifications/extendibility was proven in a short time in response to an initial customer query. In other words, the product was seen, both by customers and developers, to be of high quality. Here, as elsewhere, a prototyping development environment was chosen for the OO implementation. Other successful projects are reported by Hopkins (1990) in telecommunications, by Winston (1990) in a wide range of applications areas, by Wybolt (1990) in the development of CASE tools and by Berman and Gur (1988) and Nurick (1990).

As noted above, not all projects are successful immediately. Many of the barriers to successful implementation of both OO and TQM arise from the current organizational culture. For example, Thomsett (1990) evaluated the potential conflicts between two program development teams within the same organization who might be in competition in some way. Thomsett recommends the institution of a linking-pin role between the two teams: someone who is responsible to both team leaders. This shared human resource will enhance the production and generalization of reusable library classes as well as providing central support to both teams. Such a reporting structure is necessary if the quality of software is to be enhanced by use of this new approach to software engineering: an approach for which traditional management structures are ill-suited. Thomsett (1990) stresses that we should regard the object-oriented development paradigm as an organizational paradigm first, and a technical development paradigm second. A similar question (of corporate culture) is asked by Linkow (1989) in a review of 20 companies implementing TQM. He proposes the use of a total quality culture matrix to help an organization identify its strengths and weaknesses in successfully adopting a quality culture; whilst Gibson (1990) sees the role of strong leadership as vital to the success of TQM. He also urges the opening of channels of communication between top management and the quality professionals in this changing organizational culture. Hopkins and Warboys (1990) stress the need for management to reassess how productivity, effort and success are measured in a high quality, object-oriented software development environment where the software itself should come to be regarded as a corporate asset.

## Conclusions

Quality is the focus of the new paradigms of object-oriented software engineering and total quality management. Whilst TQM rests on concepts proposed by Deming (1981), and Joiner and Scholtes (1986), the realization that quality is a central feature of object-oriented systems development is more recent (Meyer, 1989b). Parallels have been explored between these two philosophies in the context of the management of the software development process — a process for which models have only recently been proposed (Henderson-Sellers and Edwards, 1990). Both philosophies can benefit greatly from further mutual interaction.

## References

Berman, C. and Gur, R. (1988) NAPS — a C++ project case study, in Proceedings of the USENIX C++ Conference, 137–149.

Deming, W.E. (1981) Improvement of quality and productivity through action by management, National Productivity Review, 12–22.

Gibson, T.C. (1990) Helping leaders accept leadership of total quality management, Quality Progress, 23(11), 45–47.

Goldberg, A. and Rubin, K. (1990) Talking to project managers: organizing for reuse, Hotline on Object-Oriented Technology, 1, 7–11.

Henderson-Sellers, B. and Edwards, J.M. (1990) The object-oriented systems lifecycle, Comms. ACM, 33, 142–151.

Hopkins, D. (1990) An Eiffel experience, ACS Bulletin (Victoria Branch), 29(5), 5–8.

Hopkins, T. and Warboys, B. (1990) Asset management and object-oriented technology, Hotline on Object-Oriented Technology, 1, 12–13.

Howard, G.S. (1988) Object oriented programming explained, J. Systems Management, 39, 13–19.

Joiner, B.L. and Scholtes, P.R. (1986) The quality manager's new job, Quality Progress, 19(10), 52–56.

Leathers, B. (1990) Cognos and Eiffel: a cautionary tale, Hotline on Object-Oriented Technology, 1, 1, 3, 6–8.

Linkow, P. (1989) Is your culture ready for total quality?, Quality Progress, 22(11), 69–71.

McCullough, P. and Deshler, N. (1990) WyCASH+: an application built within an OOP environment, Hotline on Object-Oriented Technology, 1, 1, 3–4.

Meyer, B. (1988) Object-oriented Software Construction (Prentice-Hall, Hemel Hempstead) p. 534.

Meyer, B. (1989a) From structured programming to object-oriented design: the road to Eiffel, Structured Programming, 1, 19–39.

Meyer, B. (1989b) Writing correct software, Dr Dobb's Journal, 14(12), 48–63.

Meyer, B. (1990) Tools for the new culture: lessons from the design of the Eiffel libraries, Comms. ACM, 33, 68–88.

Nurick, A. (1990) An OOP developer's success story, Programmer's Update, 41–51.

Parnas, D. (1972) On the criteria to be used in decomposing systems into modules, Comm. ACM, 15, 1053–1058.

Shimoyamada, K. (1987) The president's audit: QC audits at Komatsu, Quality Progress, 20(1), 44–49.

Stroustrup, B. (1988) What is object-oriented programming?, IEEE Software, 5(5), 10–20.

Thomsett, R. (1990) Management implications of object-oriented development, ACS Newsletter, 26(9), 5–7, 10–12.

Winston, A. (1990) Objective reality, Unixworld, 7(4), 72–75.

Wybolt, N. (1990) Experiences with C++ and object-oriented software development, in Proceedings of the USENIX C++ Conference, 1–9.

Zultner, R. (1988) The Deming approach to software quality engineering, Quality Progress, 21(11), 58–64.

## Biographical notes

Brian Henderson-Sellers is Associate Professor in the School of Information Systems at the University of New South Wales. His current research interests include object-oriented systems development methodologies and notation; implementations of the object-oriented paradigm in the commercial environment; environmental decision support and simulation modelling. He is Convenor of the Object-Oriented Special Interest Group of the Australian Computer Society (NSW Branch).

Address for correspondence: Associate Professor B. Henderson-Sellers, School of Information Systems, University of New South Wales, P.O. Box 1, Kensington, New South Wales 2033.
