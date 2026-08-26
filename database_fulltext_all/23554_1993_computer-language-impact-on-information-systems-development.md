---
otero_id: 23554
otero_key: "BSEJSU2H"
title: "Computer language: impact on information systems development"
authors: "Peter Middleton"
year: "1993"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1993.22"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Computer language: impact on information systems development

PETER MIDDLETON

Information Management Division, The Queen's University of Belfast, Northern Ireland, UK

The impact of a particular computer language on the process of developing an information system is not well understood. This paper explores the issues through interviews with 16 software developers who changed, or considered changing, from a third to a fourth generation computer language. The conclusion is that there can be considerable costs in hardware, inflexibility and project planning errors incurred by changing to a fourth generation language. The benefits are unlikely to compensate for the costs of changing languages. The key factors influencing the productivity of software developers emerged as social, not technical.

## Introduction

The purpose of this article is to examine the impact of computer language on information systems development. Software development projects are prone to exceed planned cost, to be delivered late and to have low levels of user satisfaction. A computer language is used by definition to write a software system; it is therefore relevant to ask if the computer language is part of the reason for these problems. Computer languages currently in use can be classified broadly as either a third generation language (3GL) or a fourth generation language (4GL).

A 4GL, e.g. Ingres or Oracle, has a database as its foundation and provides a database query language, a report generator and a screen painter. By providing within the 4GL standard facilities to access the database and generate reports it seeks to improve programmer productivity. In contrast a 3GL, e.g. COBOL or Pascal, would not provide a database or the other features but it would be a smaller and cheaper language.

There are frequent advertisements in the computer trade press for 4GLs, e.g. Ingres, Informix, Oracle and Focus. These commercials feature slogans that relate development performance to the language used. This is not a new trend; the use of higher level languages has long been advocated as a route to higher productivity (Brooks, 1975; Martin, 1985).

Analytical evidence presented by Jones (1986) shows that a 4GL database requires 40% of the source statements needed by a 3GL such as COBOL. The main benefit of this is that programs will be shorter and therefore quicker to write. This implies that a 4GL will raise the productivity of developers.

There are many tasks required to construct an information system and programming is only one of them. For example the classic lifecycle includes the following which must be carried out in turn: analysis, specification, design, programming, testing and operation. This is known as the 'waterfall' approach and it is often criticized because it is said to be inherently slow. To speed up the development cycle Gane (1989) advocates the use of a 4GL combined with a structured prototyping approach. That is the use of a high level language, Oracle in this case, which allows increased productivity through the alteration of the system lifecycle. Crinnion (1991) argues for an evolutionary lifecycle based on the 4GL Focus. Again the language enables the adoption of a different approach to system development.

## What is a good computer language?

The change in software technology over the last 20 years means that the precise definition of high level and fourth generation languages is evolving. Brooks' (1975) recommendation for a high level language was "The only reasonable candidate today is PL/1". Boehm (1981, p. 661) selects Pascal and ADA as: "the strongest choice for enhancing productivity in the long run". Boddie (1987, p. 88) recommends "PASCAL, C, PL/1 or any of the ALGOL derivatives", and proceeds to note the importance of reuse that applies to all languages (p. 90).

"In terms of productivity, it doesn't appear that ADA will offer any gain over other block-structured languages until large libraries of common routines become available".

Crinnion (1991, p. 35) specifies tools for his evolutionary systems development method.

"It requires not only a fourth generation language (like FOCUS or NOMAD) but also a whole environment of software surrounding it. This provides what is often called a 'fourth generation environment' (4GE) or an 'analyst workbench'".

Holloway (1989, p. 188) quoted a 1986 report from the Institute of Data Processing Managers that suggested that organizations who had purchased 4GLs had not been as successful as they expected. He felt the reasons for this were that

“...the organizations had not thought about changing their methodology for developing systems, the new software and its associated techniques, as well as catering for the new problems that the software causes”.

Grindley (1991, p. 173) in his survey of 5000 IT executives concluded

"No IT director interviewed, however, claimed that the use of packages or of pure 4GLs would account for more than $30\%$ of his programming effort, or that they would solve the centralized systems development problem".

The point that 4GLs can have only a limited beneficial impact on the typical project life cycle is demonstrated by Jones (1986, p. 161). Only the coding and design phases are significantly affected by a 4GL. A similar point is made by Youett (1992). However, the changing of the language used can require alterations to estimating, project management and procurement procedures. This is necessary to work with the language, but does not bring any new advantages.

The evidence from the market place reported by Cane (1991) is that tools to improve productivity with COBOL are selling strongly. COBOL is cheaper to buy than a 4GL. It requires less hardware to run, it can tackle a wider range of tasks and has proven reliability. It is therefore a logical step to enhance this with low cost tools, rather than move to a 4GL.

Holway (1992) reports that there is more installed computer power now in the form of personal computers, than in mainframes and minicomputers combined. This trend towards the increasing personalization of computing and the move towards smaller computers is a powerful one. In contrast to this focus on the technology, Boehm (1981) reports an analysis of how programmers spend their time. This shows that they spend only 13% of their time writing programs.

This discussion indicates that while some computer languages are better than others a range of issues are important. Other factors such as the development cycle, reuse of software, the support environment, technology trends and work patterns were all parts of the equation. This research is to examine the experience of practitioners who switched, or considered switching, from a 3CL to a 4GL.

## Research methodology

The research took place in 1992 over a period of seven months. It involved two hour structured interviews with twelve public sector and four private sector organizations. The results were presented to the participants for comment. The public sector organizations were the Information Systems Units (ISU) of a range of government departments. The private sector representatives were the software development organization of a major multinational company, a systems software company that exports its products worldwide and two national bespoke software developers. These last two companies were accredited with the BS5750 quality standard.

Organizations that had recently changed computer languages were anticipated to be fertile sources of insight into the influence of language on systems development. Therefore of the 16 organizations examined, ten of them had changed to a 4GL within the last three years. This sample meant it was possible to ask ten developers why they had changed the language used and what happened when they did. The other six were questioned on why they had not changed languages.

The staff interviewed were systems analysts and project managers. These were selected because they would have first-hand experience of the result of using a particular computer language. They would also have a broad enough perspective to appreciate the total impact of the language. In 13 cases one specific project was discussed in depth. These interviews examined and discussed project documentation but it was not audited. In the other three cases the staff were concerned with numerous small projects, so their experiences on several of these projects were discussed in the interview.

The questions in the interview covered the complete lifecycle of the projects, rather than just focusing on the coding stage. The organization's total productivity was felt to be significant, rather than solely that of the programmers and programmer/analysts.

Research from Humphrey (1988) indicates that 86% of organizations collect no metrics on their software development process. The organizations studied were all found to be in this category. This meant that no empirical data were available to chart productivity against the language used. The significance of this is an indication that software production is still largely a craft skill, and that productivity is judged subjectively. It means that research has to tap practitioners' perceptions, rather than hard data.

The interviews were felt to give an accurate reflection of practitioners' experience of different computer languages for the following reasons. The interviewer was expecting different answers from ones received, and therefore interviewer bias is not distorting the replies. The structured interview was wide-ranging and loose enough to allow participants to raise issues they wanted to. The participants were guaranteed complete confidentiality, and consequently the replies were often given with great candour and conviction.

## Reasons for changing computer language

The first aim was to establish which problems the organizations were trying to solve by changing their computer language. The decision to change and the selection of language was always made by technical staff. In all 16 organizations, end users were not involved in the decision.

(1) Standardization: organizations had found a proliferation of languages in use. Each language had become established in an unpremeditated way. In one organization, 14 languages were found to be in use. This pattern is not unusual; Cane (1992) reports that the London Stock Exchange was using eight different programming languages. The result was inflexibility in the allocation of technical staff and higher support costs. Therefore a new language was sought which would be comprehensive enough to supersede all the existing languages.

(2) Range of hardware platforms: the key desire to standardize indicated that the language chosen should be available on a wide range of computers. This was necessary to avoid ‘proprietary lock-in’ which would raise prices on hardware purchase and maintenance.

(3) Industrial strength: the drive to standardize on one language to reduce costs meant that the language selected should be able to tackle all the tasks being handled by the existing languages. This indicated the need for a large general purpose language.

(4) Structured Query Language: SQL as a standard was expected to encourage end user computing and to allow computer staff to respond more easily to ad hoc requests for reports. This should reduce costs and improve user satisfaction.

(5) Bulk buying discounts: replacing the fragmented approach to the purchase of and training on assorted computer languages with a unified approach was anticipated to be cheaper.

What was unexpected about these replies was that organizations were not primarily looking for language performance. They were also not seeking to reduce hardware costs. Their objective was to reduce costs by increasing staff flexibility through language standardization. Their need was defined as a language that could undertake a wide range of tasks and which could run on a broad selection of computers.

## Reasons for not changing computer language

In contrast, the remaining six organizations had not changed their computer language in the last three years. All four private sector organizations were in this category. The decisions to remain with third generation languages such as COBOL and C were deliberate. The reasons given in order of priority were the following:

(1) Hardware cost: 4GLs were known to be heavy users of hardware. This would increase both the hardware capital and maintenance costs over the life of the system. This would increase the total cost of the system to the user, and easily outweigh any savings made during software development.

(2) 4GL capability: 4GLs were felt to have 'bugs' and therefore to be unreliable. It was also observed that 4GLs could not cope with really difficult code and therefore it would be necessary to use a 3GL anyway. This would increase costs because of the need to retain high order 3GL skills. This also introduced the added risk of possible interface problems with the 4GL. It was noted that COBOL and C are available on a wider range of hardware than any 4GL. This meant that there was more risk of not being able to support the users' hardware.

(3) Continuity: changing languages would mean altering the development methodology used. This would render their estimating experience invalid. Training costs would also be incurred.

(4) 4GL cost: the modern large general purpose languages were expensive to purchase when compared with COBOL or C. There were also costs for run time licences.

This group of developers perceived that using a 4GL would raise the total system cost. The private sector companies used time-sheets and had more accurate information on their costs. All this group were initially defensive when asked about their decision to stay with the older languages. This group was more sophisticated in their understanding of the importance of the system lifecycle. They understood that it would increase uncertainty in the development process, and therefore increase costs in many indirect ways.

## Results from changing computer language

The ten organizations which had moved to using a 4GL in the last three years had accumulated experience from this. The change had not been tracked or measured using metrics so collating the observations of practitioners was the only way to examine what had happened. The feelings were generally negative. The problems are grouped under

the following headings:

## (1) Hardware

(i) Hardware costs: the 4GLs required more powerful hardware to run and this had a series of knock-on effects, apart from the extra expense involved.

(ii) Slower procurement: the larger hardware raised the cost of the projects, and therefore required the use of more elaborate and lengthy procurement procedures. This increased the time needed for the projects. This made projects more vulnerable to changes in the environment that could require alterations to specifications.

(iii) Performance under MS DOS: 4GLs were found to run particularly slowly under the MS DOS microcomputer operating system. This caused problems for the several hundred small systems created by these organizations. It was not enough for a language to be available for a particular operating system; it also had to have adequate performance to be usable in practice, otherwise spending money on substantial equipment upgrades would be required.

(iv) Uninterruptable Power Supply (UPS): the larger hardware often required a larger UPS that added to cost.
(v) Air-conditioning: In one instance the larger hardware required would have needed an air-conditioned environment. This would have added considerably to cost, so for these and other reasons the standard 4GL was not used.

## (2) Operational

(i) Installation problems: several sites had great difficulty getting the software to load onto their machines. It was found to be complex to install and set up. This process took three weeks in one case. The depth of support required from the supplier was not forthcoming. There was a considerable time lag between new software being released and the field staff becoming skilled in its idiosyncrasies.

(ii) Development lifecycle: the Structured Systems Analysis and Design Methodology (SSADM) recommended for use needed substantial tailoring to work effectively with a 4GL. This had not been appreciated fully or prepared for at the time. Time wasting occurred while revising the development lifecycle.

(iii) Estimates: the strengths and weaknesses of the 4GL were not known; therefore the estimates for projects were inaccurate. The changes in methodology also hindered estimating. Project management was more difficult. This was because the experience of senior staff was not so applicable in the changed situation.

## (3) Staff

(i) Commitment: once a decision had been made to standardize on a particular language there was a sense that developers were to some extent 'let off the hook'. There was not the same responsibility for having to deliver cheap and effective systems. They could not be held accountable for high training costs, technical delays or higher hardware and accommodation costs.

(ii) Other changes: standardizing on a new language also occurred at times when there were other changes such as staff moves and new application areas being tackled. This added to the uncertainty of an already uncertain environment. This did damage to some projects and must be seen as an additional cost of changing languages.

(iii) Training costs: the training costs were higher than anticipated because courses were proprietary and subject to limited competition. The suppliers also released frequent upgrades and additions that required extra training. Apart from the direct cost of training this caused disruption.

(iv) Database design: the staff being interviewed did not mention database design as a problem, but the need to improve database design was shown by the project documents examined. Extensive training may be needed for people to be able to manipulate the relational database part of a 4GL competently. Sophisticated tools require a skill to handle them, which takes time to acquire.

The results from the ten organizations that had changed language recently points to the following. The language used is part of the fabric of the organization. Changing it is disruptive. The hardware costs that increased more than anticipated were those for initial purchase, maintenance and accommodation. The impacts on project management, development process and estimating were all underestimated. These organizations did not collect cost or any data in a coherent form. They were therefore vulnerable to advertisements and salesmen who promised productivity gains.

## Discussion

The results show that increasing staff flexibility was the objective of those organizations that changed language. They were prepared to increase their cost base to achieve this, but their decision was subjective because they had no data on their development performance.

The four organizations with time-sheets, all of whom did not change language, had information to show that their staff were productive for only 50% of the time. The other group without data assumed staff were productive 80% to 100% of the time. Probably the true figure for their productivity was 20% to 30%. The costs of changing language were therefore not fully appreciated because of their lack of data. They also did not know the critical factors affecting productivity. The following key themes have emerged from this research:

(1) Standardization: the findings illustrate that in this sample of organizations the key motivation for changing computer language was standardization. The use of only one language was expected to improve staff productivity when developing and maintaining software. While this is a reasonable assumption it is simplistic. Boehm et al. (1984) observed that three things would hamper the American Department of Defence's desire to standardize on the computer language ADA. These were the need to maintain existing systems written in other languages, the use of packages written in other languages and the need for specialized languages for certain applications. This is confirmed by these findings and they indicate that the goal of standardization may not be a practical one.

(2) Hardware costs: the need for more powerful hardware had been anticipated by the organizations that adopted 4GLs. What had been a surprise was the extent of the knock-on effects. The increased processing capacity required of the computers lengthened the procurement cycle, raised the accommodation costs for the machine and rendered large numbers of the microcomputers obsolete.

(3) People costs: the costs in staff time were high and often hidden because of the need to alter the development lifecycle. Until analysts were familiar with the new 4GL it was difficult for them to adopt a new lifecycle. By rendering their experience invalid, both estimating and project management were made more hazardous. The costs of this were considerable.

(4) Long term productivity: the key question remains – when the learning required by the change in language had taken place, would productivity rise? The analysis in Table 1 of how programmers spend their time shows that program writing takes just 13% of their time.

The data in Table 1 indicate that investment directed towards facilitating job communication (32%) and reading programs (16%) may well produce better returns. Improved motivation may well reduce the 33% of total time spent on miscellaneous (15%), personal (13%) and mail (5%). This indicates that changing the language is unlikely to produce significant productivity gains.

If 4GLs are to overcome the disadvantage of their rapacious appetite for computer processing power, there would need to be evidence of the productivity they could bring to the development process. Table 2 shows the approximate number of program statements required to code one Albrecht function point in selected languages.

Table 1 How programmers spend their time

<table><tr><td>Activity</td><td>% Time</td></tr><tr><td>Job communication</td><td>32</td></tr><tr><td>Read programs, manuals</td><td>16</td></tr><tr><td>Miscellaneous (walking . .)</td><td>15</td></tr><tr><td>Personal</td><td>13</td></tr><tr><td>Write programs</td><td>13</td></tr><tr><td>Training</td><td>6</td></tr><tr><td>Mail</td><td>5</td></tr><tr><td>Total</td><td>100</td></tr></table>

Source: Boehm (1981, p. 592).

The valuable insight here is that the reduction in source statements from Assembler (320) to Pascal (91) is 229. This illustrates the improvement from a second generation language (2GL) to a third generation language (3GL).

The reduction from Pascal (91) to Query language (16) is 75 source statements. This illustrates the improvement from a 3GL to a 4GL. It is only one third of the reduction between the 2GL and the 3GLs. Therefore, on this purely analytical basis, only small improvements should be expected from using a 4GL.

Spreadsheet languages are rated as requiring six source statements per function point. But, as languages become more specialized they become more inflexible. It is therefore apparent that a trade-off is necessary between the level of a language, its merits for assisting in the production of reliable programs and its general applicability.

## Alternative approaches

If this chosen route of setting a 4GL standard is so difficult, what other methods are available to raise productivity? From the references given and from the Japanese experience summarized in Matsumoto and Ohno (1989) the following have clear empirical data to show that they work:

Table 2 Lines of code per function point

<table><tr><td>Language</td><td>Source statements per function point</td></tr><tr><td>Assembler</td><td>320</td></tr><tr><td>COBOL</td><td>106</td></tr><tr><td>PASCAL</td><td>91</td></tr><tr><td>BASIC</td><td>64</td></tr><tr><td>Fourth-generation database</td><td>40</td></tr><tr><td>Query languages</td><td>16</td></tr><tr><td>Spreadsheet languages</td><td>6</td></tr></table>

Source: Jones (1987, p. 77).

(1) People: the estimates coverage around a 10–1 difference between programmers (DeMarco and Lister, 1987), so selecting and retaining good people would raise productivity. A graphic example of this is given by Wallace and Erickson (1992) when describing the successful software company Microsoft. They recruit only the best and then cull the bottom 5% of staff at six monthly intervals. By this Darwinian approach to their staff they have built a very capable organization.

(2) Organization: the estimates converge around a 10–1 difference between organizations. People of the same capability are only 10% as productive in some organizations as they are in others. This difference is due to physical layout, motivation and organization (DeMarco and Lister, 1987). Again Microsoft pays great attention to ensuring all software engineers have their own private office with a pleasant view. Young software specialists are motivated by deliberately creating an environment they would enjoy (Wallace and Erickson, 1992). They are reported to pay only average wage levels.

(3) Reuse: the Japanese and American companies such as Hewlett Packard report large gains from reuse of software. The problems are not technical but managerial. It is necessary to catalogue the software produced and to create a library that is easy to access.

(4) Measurement: the simple fact of measuring what is happening can provide valuable insights and raises productivity. It enables organizational learning and focuses attention on bottlenecks. Comprehensive measurement was absent in all the organizations visited, but no measurements were carried out by the ones that changed their language.

All of these four approaches require management skill rather than crudely attempting to buy productivity with a computer language. The technology-led approach is the equivalent of trying to improve a person's driving performance by buying them a new car.

## Conclusion

This research has examined the impact of computer language on the development of IS. The data presented indicate that productivity gains are problematic from simply replacing a 3GL with a 4GL. There are three main conclusions from this research.

Firstly, on a technical level, 4GLs have the following disadvantages. They are larger and more complex than 3GLs, which means that they are more difficult to install, are prone to bugs and are more expensive to purchase. They are also more expensive to use because they require more hardware, which increases capital, maintenance and (potentially) environment costs. They do not run well on a personal computer which is the dominant form of computer power. The increased cost of hardware and software can increase the time taken for procurement. This makes the proposed system vulnerable to changes in the user requirements.

Secondly, implementing a new language means that the organization's experience of estimating and project management needs revising. This was found to cause severe difficulties for organizations because by rendering their estimating experience obsolete it meant that mistakes were made when planning for projects using the new language.

Thirdly, the key drivers for organization performance are social not technical. Therefore the technocratic response of changing the computer language is not appropriate. Other methods for improving productivity are well documented and proven to produce results. These include policies for the selection and retention of staff, organization, reuse of software and measurement of projects. It is concluded that a new language adopted without addressing these other issues is unlikely to be a profitable investment.

## References

Boddie, J. (1987) Crunch Mode: Building Effective Systems on a Tight Schedule (Yourdon Press, Prentice-Hall, Englewood Cliffs, NJ).

Boehm, B.W. (1981) Software Engineering Economics (Prentice-Hall, Englewood Cliffs, NJ).

Boehm, B.W., Penedo, M.H., Stuckle, E.D., Williams, R.D. and Pyster, A.B. (1984) A software development environment for improving productivity. Computer, 17(6), 30–42.

Brooks, F.P. (1975) The Mythical Man-Month (Addison-Wesley, Reading, MA).

Cane, A. (1991) Speaking the right language. Financial Times, 6 June 1991.

Cane, A. (1992) Exchange grows heated over computers. Financial Times, 27 May 1992.

Crinnion, J. (1991) Evolutionary Systems Development (Pitman, London).

DeMarco, T. and Lister, T. (1987) Peopleware: Productive Projects and Teams (Dorset House, New York).

Gane, C. (1989) Rapid System Development (Prentice-Hall, Englewood Cliffs, NJ).

Grindley, K. (1991) Managing IT at Board Level (Pitman, London).

Holloway, S. (1989) Methodology Handbook for Information Managers (Gower Technical, Aldershot, Hants).

Holway, R. (1992) A Review of the Financial Performance of UK Computing Services Companies, in The Holway Report, 1, Richard Holway Ltd, Farnham, Surrey.

Humphrey, W.S. (1988) Characterising the software process: a maturity framework. IEEE Software, 5(2), 73–79.

Jones, C. (1986) Programming Productivity (McGraw-Hill, New York).

Martin, J. (1985) System Design from Provably Correct Constructs (Prentice-Hall, Englewood Cliffs, NJ).

Matsumoto, Y. and Ohno, Y. (eds) (1989) Japanese Perspectives in Software Engineering (Addison-Wesley, Singapore).

Wallace, J. and Erickson, J. (1992) Hard Drive: Bill Gates and the Making of the Microsoft Empire (John Wiley & Sons, New York).

Youett, C. (1992) Fourth generation languages – special report Computer Weekly, 4 June 1992.

## Biographical notes

Peter Middleton has been a lecturer in information management at The Queen's University of Belfast since September 1990. From 1985 to 1990 he was Head of Computer Services for an Education Authority. His research interests include Japanese management techniques, system dynamics and business process re-engineering.

Address for correspondence: Peter Middleton, Information Management Division, The Queen's University of Belfast, Belfast BT7 1NN, UK.
