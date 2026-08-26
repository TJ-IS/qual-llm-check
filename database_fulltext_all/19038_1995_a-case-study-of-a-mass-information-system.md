---
otero_id: 19038
otero_key: "XP7RYW7B"
title: "A case study of a mass information system"
authors: "Hans Robert Hansen"
year: "1995"
journal: "Information & Management"
doi: "10.1016/0378-7206(94)00044-j"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A case study of a mass information system

Hans Robert Hansen

Vienna University of Economics and Business Administration, Vienna, Austria

## Abstract

Mass information systems (mass IS) support on-line information retrieval and routine tasks by way of self-service for a great number (thousands or millions) of occasional users. Delivered through public terminals, the services of mass IS are designed to cater to passer-by types of audiences, such as visitors of exhibitions, spectators at major sports events, travellers at airports and train stations, or users of automated teller machines (ATMs). In the last issue of Information and Management the author gave an overview of mass IS and outlined a conceptual framework for mass IS development. This paper presents a case study that summarizes the experiences of an Austrian university with such a videotex-based system.

Keywords: Adoption of IT; Austrian higher education; Data quality; End-user systems; Home information services; IS development; IS operations; Kiosks; Mass information system; On-line services; Self-service; Student information system; Telecommunications; University information system; User acceptance; User interface; Videotex

## 1. Introduction

This study describes the environment, the goals, the basic development decisions, and the results of a mass IS in higher education: the WU videotex system. The system was introduced in the early 1980s. It has undergone considerable changes, and is still in use today. As far as we know, it is one of the largest interactive videotex inhouse systems worldwide.

This case study is not one of the usual success stories. On the contrary, we try to point out the weaknesses of the system's design, and we concentrate on acceptance problems. We also derive ten lessons to help implement mass IS under similar conditions.

## 2. Environment of the WU videotex system

The environment of a mass IS consists of major determinants of the system's success that cannot be influenced by the IS developer, at least not in a short-range period. Significant environmental factors are related to the industry, the telecommunications infrastructure, and the particular organization.

## 2.1. Higher education in Austria

The population of Austria is 7.7 million. 31% of the age group (18 or 19 years) are completing higher secondary education. The “matura” qualification entitles to enter any university and to study any subject without tuition or fees. There are only 12 public universities with 204,900 enrollments (183,400 Austrian citizens), $^{1}$ regulated by the federal ministry of science. Students aged 18–25 represent 12% of their age group. Serious problems are the very high drop-out rate and the long duration of study. Only about 10,000 students graduate each year; about the same number of faculty is employed nationwide. Due to a recent change of federal policy and laws the very small non-university sector of higher education (14,000 students) will be extended.

Most universities are overcrowded in many areas. Therefore, they don't compete for students. Consequences of the seller's market situation are underdeveloped student services and poor students' guidance and counseling, especially at the undergraduate level.

## 2.2. Telecommunications

The telecommunications sector has always been strongly regulated by the Austrian government. The federal PTT has a nationwide monopoly on the telephone network and basic services $[1]$ . Telephone and data transmission rates are among the most expensive in the world, though the customer service is generally poor. The technical level of the infrastructure is high and corresponds to the leading industrial nations. But as far as new services are concerned, there is almost always a time-lag of two or three years compared to other providers.

An exception to this rule is interactive videotex. As in most nations of Western Europe the Austrian PTT introduced a public videotex service in the early eighties and called it – as in Germany – Bildschirmtext (BTX). Diebold and other market research companies predicted an overwhelming success for this low-cost telecommunications service: Over 100,000 participants, mostly private users at home, within the first three years in Austria, more than a million in Germany. In contrast to the German and most other national Telecom administrations the Austrian PTT did not push as standard terminals the existing TV sets linked up to telephone lines. It rather supported a much more advanced Austrian product: a dedicated BTX-PC, called Mupid, that offered high-resolution color graphics, downloading possibilities, and a growing number of special programs (utilities and applications). $^{2}$

More than a decade later the Austrian BTX service has still not more than 19,600 indefatigable subscribers. Almost all of them use standard PCs, the Mupid manufacturer went bankrupt several years ago. The number of information providers has dropped from 398 in 1991 to 266 in 1994. The postal BTX service has produced huge losses from the beginning. The telecommunications monopoly of the Austrian PTT will be broken soon, when Austria will become a member of the European Union.

## 2.3. Vienna University of Economics and Business Administration

Vienna University of Economics and Business Administration – also called “WU” for the German name “Wirtschaftsuniversität Wien” – is one of the leading business schools in Europe. The good reputation and the excellent job opportunities of their graduates have caused such a student boom that some years ago the administration tried to keep away less qualified or less motivated students by a nationwide advertising campaign. $^{3}$ The number of students rose sharply from 3,655 in 1970/71 to 8,968 in 1980/81 and 19,514 in 1990/91. Due to the WU strategy and supporting demographical trends the growth rate could be slowed down to 20,734 students in the winter semester 1993/94.

Seventy-six percent of the students are undergraduates. In every winter semester about 4,000 freshmen begin their studies at WU. Half of them are enrolled at other universities and take only selected courses at WU. Introductory lectures are attended by hundreds of students; practice courses have to be taught very often in 30 or 40 parallel classes. The undergraduate qualifications are honored by a first diploma certificate, but there is no bachelor's degree or other academic title. Almost all students are heading for the master's degree from the beginning, but only about one third are successful finally after an average study period of 13 semesters. 54% of the students are enrolled for Business Administration, 40% for World Trade, 4% for Business Education, and 2% for Economics. Last year about 1,100 MBA's and 80 Ph.D.'s graduated.

Because of the rapid growth of students' numbers and a comparably low increase of personnel the overall ratios between professors and administrative staff to students are worse than at most other schools worldwide. Due to the high drop-out rate however, this is only true for the undergraduate level. At the graduate level the conditions are comparable to leading U.S. business schools. The faculty has been doubled during the past decade to about 700 members, half of them are part-time adjunct professors (external lecturers). The administrative staff now has 255 employees.

Manpower shortage has been an important motivation for the intensive use of computers in administration, education, and research. This is also a reason why IS faculty – over 40 at present – has often been involved in the development of administrative IS. There was no other way to ease the burden of bureaucratic tasks. Another reason has always been that IS students can get practical experience in this way.

The first half of the eighties has been dominated by IBM and Siemens mainframes; the latter is still in use for administrative applications. Since 1984/85 an increasing number of PCs and workstations has been installed. Today's number of 1,200 PCs and workstations of all types, 70% networked, will probably not be increased, because a growing number of students has their own equipment. $^{4}$

## 3. Goals and architecture of the WU videotex system

Under these circumstances it is obvious that interactive videotex was seen then as a potential solution for many problems at WU [3,5]:

\- Elimination of bottlenecks in space and faculty through distance learning: by downloaded tele-software, to be developed and distributed by WU professors and others.

\- Relief of the endless stream of repeated inquiries concerning courses, events, etc. by self-service of students, giving them direct access to adequate “routine answer bases”.

\- Better communications with students and guidance of their homework by electronic message handling.

\- Prolongation of restrictive departmental opening hours by information retrieval around the clock in the library system, on-line guides, databases with questions of earlier tests, etc.

\- Improvement of the internal information by a permanently up-dated university-wide bulletin board with decentralized I/O.

\- Complete continuous documentation on the side of running announcements and database updates.

\- Remote access to WU computing resources from terminals in students' and faculty homes.

\- Public relations for the university as a whole, for departments, and for single faculty members (who is who?).

In 1982, the MIS Department of the WU offered a first very slim version of the WU videotex system in the public PTT videotex system. 1984, an expanded version was implemented on the WU Siemens host, linked ever since by a packet switched connection to the nationwide PTT videotex system. Access is possible by terminals (today: PCs) at home, by public videotex terminals in post offices, banks, $^{5}$ or around the campus, and, meanwhile, by all PCs and workstations of the WU local networks. (Figure 1.)

![](/api/attachments/XP7RYW7B/fulltext/images/e5caab9732adec91c6321542d8966ca31b05bc51f4f20ba9e2f57c40800c0ca6.jpg)  
Fig. 1. Architecture of the WU videotex system

Three to four MIS Department members worked for a total of seven years on research and development in connection with videotex. They supervised numerous seminar groups and students preparing for their diploma theses and involved them in the system development. By far more than ten thousand videotex pages (screens) were edited. Hundreds of beautiful pictures were drawn. A great number of smaller and larger interactive programs for the videotex host and the videotex-PCs (Mupids) were implemented.

The system was turned over to the university administration in 1989. The remains today are at most ten percent of the long-term development results, i.e. functions and files that have been implemented earlier. The WU videotex system currently contains some 1,700 seldom accessed information pages, but registration services are intensively used by about 20,000 students.

Though few of the development goals mentioned above have been achieved by the WU videotex system, it is hard to imagine day-to-day life at the WU without it. In the following we will describe why.

## 4. Basic decisions on the WU videotex system

This section summarizes basic decisions on the WU videotex system and their results. We also derive ten lessons to help implementing mass IS. $^{6}$

## 4.1. Offerings

Lesson 1:

Only those services should be implemented in mass IS which give the information providers as well as most of the users direct rationalization benefits (e.g., savings in time and costs, improvements of service). General information is not called up. Reservations or ordering by self-service are most attractive.

At present, the WU videotex system administers about 1,400 courses within one semester. Ninety percent of the approx. 55.000 registrations for exercises, proseminars, seminars, and examinations take place through the 27 public videotex terminals installed on the campus; the rest comes from the outside. The average time taken by an internal reservation process is 1.45 minutes (= time spent in the registration program).

What does that mean for the individual department? Four times a year the IS Institute offers a multiple-choice test, to check the prerequisites for the introductory course in the PC labs. Each time 1,500–2,000 students register through videotex. For the admitted participants (the system checks the enrollments) two different tests are set up from a database of multiple-choice questions that is not integrated in the videotex system. The 35 questions in ten different assortments and corresponding machine-readable answering forms are printed out for the participants. Immediately upon the examination follows the automatic evaluation of the test results, the transfer of the results to the WU videotex system, and the assignment of the successful participants to the approximately 40 parallel classes. The latter is a relatively complicated procedure, because on the one hand the preferences (up to four) given by the students when registering need to be considered, on the other hand because also students – with waiting-list priority – who had obtained their participation entitlement in a previous semester, need to be taken into account. Two days later, and thus just in time for the start of the semester, the examination results and the assignment to classes are published – again via videotex – and by printed lists on the traditional bulletin board. Although in 90% of the cases the first or second preference of the students could be assigned, immediately – as usual – an intensive exchange of places among the admitted participants sets in.

From the WU videotex system lists and data of participants are available to faculty upon call, which they can use as basis for their current PC-assisted class administration. At the end of the semester they enter the grades into the WU videotex system, so that they can be called up by the students. The protection through passwords prevents misuse – for instance, that a student wanting to register for a booked-out course just cancels another reservation. Of course, lists of grades with only the student ID numbers may be printed for the bulletin board and the files.

This example shows enormous time savings and better service for university departments and students as well. Therefore, all departments with a large number of students made use of the videotex registration at an early stage. Where this application was long under consideration, the pressure from the students contributed to its acceptance.

In the last of regularly carried out surveys among students during the summer semester 1992 (1,029 replies), only 3.9% stated that they had not used the WU videotex system during the previous semester. $^{7}$ Some 27.1% of those replying had used the system ten to twenty times during the winter semester 1991/92, 33.8% six to ten times, 29.9% two to five times.

Registration for courses and examinations was by far the most frequented application: 87.7% use it often, 11.9% occasionally. Videotex information on grades is called up by 22.4% often and by 58.8% occasionally. On the other hand this survey like all other preceding ones [4] showed insignificant usage of general information about the university, departments, faculty, courses, events etc. Only 1.3% of the students indicated that they often look for information in the offerings of specific information providers (academic and administrative departments, students' organizations etc.), 13.2% do so occasionally, but the great majority of 85.5% never do. Nearly the same answers were given to the question of browsing through the information offerings: 86.9% never do!

Though all information and services of the WU videotex system are free; neither the general public nor WU students or faculty have ever been charged for usage of the system. Everybody has anonymous access to most functions and data. Only for retrieval of personal data and registration an identification is required.

To summarize: The only successful products/processes of the WU videotex system are registrations and personal data retrieval. The offerings of university data, announcements, library and computing services have not been accepted and have therefore been eliminated over the years. The same happened with computer-assisted instruction, commercial telesoftware, and games (“WU-POLY”) – in central host versions as well as in versions for downloading to videotex PCs (Mupids). Communications services like e-mail and news groups still live in the shadows but have never been really important. $^{8}$

## 4.2. Target groups, points of usage, and supporting IT

At the beginning, the WU videotex system was addressed to “whom it may concern” or to many different anonymous public audiences. From today’s point of view this was a serious mistake.

Lesson 2:

Target groups of mass IS have to be clearly defined and specifically addressed. Only products and services planned for a tangible audience fulfil specific needs and make a great variety of useful features possible.

In our early dreams, we saw students, alpine farmers, and small business owners learning at home with our CAI courses. These hopes of an open university by means of the WU videotex system have never been fulfilled. Nor has the general public reached the system; so it could not support public relations' purposes. Only our students have become heavy users – but very slowly over many years.

## Lesson 3:

The most important target group of mass IS are the present customers. They should have system access both at home and at branch offices. To rely solely on the predicted success of a new telecommunications system is unwise. New delivery technologies mostly do not solve acceptance problems of offered products and services. Only widespread standard IT (carriers, terminals, software) can guarantee the necessary system stability and acceptance.

The enthusiasm that was there at the beginning of the new videotex technology was dampened from year to year. On the one hand, there were many technical problems because of the ongoing standardization process, poor development tools, and a limited market supply with rather expensive kiosks and Mupids. On the other hand, there was the stagnant user adoption of PTT videotex services in Austria, in Germany – another possible future market –, and of most of our services in-house, too.

Many time-consuming migrations had to be carried out: from early PRESTEL via MUPID to the final CEPT standard, from file organization (LEASY) to database administration (UDS), from one version of the videotex administration software on the host to the next, from one editor to the other. Most of these changes were not applications related – we simply had to keep track with the technological development of the postal services and our Siemens in-house software. Different videotex standards in different countries, the special Austrian approach with (at that time) high-tech “intelligent” home terminals, and resulting different software versions on all levels made development and operations rather complicated. Sometimes we had to operate different versions of the WU videotex system for the public PTT service and for the in-house service, just because the underlying administration software of different suppliers was not compatible for a while. Continuous adaptation was necessary for a great variety of terminals: ordinary TV sets with decoders, Mupids and later standard PCs at home, kiosks in post offices, banks and at the campus, workstations of the university staff. A large amount of time had to be spent to locate interface errors and to achieve stability in the quickly changing mixed hardware/software environment. During the first years the dependence on manufacturers of our videotex equipment (Siemens, Mupid, ITT) was strong. Their support was superior; the WU videotex system was an important pilot project for them.

Speculations on the reasons for the initial reluctant use of the WU videotex system concentrated on:

\- Many departments and student services were not integrated.

\- Complicated and slow information retrieval.

\- Bad image of the PTT videotex service.

\- Instability due to the many system changes.

\- Lack of knowledge on behalf of the users concerning the information services.

All these problems – with the exception of the bad PTT videotex image – have been eliminated over the years. All university institutions are integrated. The system availability is above 99% in a 24-hour operation. Through higher transmission speeds and an efficient database administration system, reply times are by far better than in the PTT videotex system. The students are well-acquainted with the WU videotex system; they know about the independence from the postal service. And in spite of this, the usage pattern has not changed very much.

The reward of costly offerings at different points of usage, i.e. terminal locations was in our case the one alternative that has finally turned out to be successful, at least.

Regarding the selection of carriers and terminals there was no other choice at the beginning of the system development. Meanwhile, the system can be accessed by any PC connected to the local WU networks and via Internet from home. Though the number of private student's PCs has grown over the years, the 10% share of external usage of the WU videotex system remained stable. The present usage pattern, however, suggests to make the system also accessible by touch-tone telephones.

## 4.3. Requirements analysis

## Lesson 4:

Information providers of mass IS very often have wrong perceptions of what the users really want. As a rule, “less is more” applies. User participation in the development process can be misleading. The necessary adaptation to individual needs can be achieved by continuous observation of user behavior.

During the first years, the information offerings of the individual departments were collected “without bridle” by seminar groups with concurrence of the respective staffs, edited with Mupids and stored in the WU videotex system. The result was a creative-chaotic “information cemetery” where everything was “buried” that ever before existed on paper. Up to 600 videotex pages per department were integrated in the search tree, among them 20-page formal instructions for preparing diploma theses, restaurant guides, literature lists, reports on research projects, layout maps, sample questions for tests, and the like.

We have already described the problems of user representation above. System developers, participating users, and information providers often forget that alternate sources of information exist, and that many users simply are disinterested, overburdened or lazy. Our “department store approach”, to offer nearly everything in the vague hope there might be at least something for somebody failed completely.

Along uniform design guidelines within the framework of a standard search tree, all WU departments offer only relatively little core information today. According to user behavior, these reduced offerings could be skipped too without negative consequences.

It is a truism that thorough requirements analysis is the basis for successful IS development. We have already outlined appropriate measures for mass IS above. In the case of the WU videotex system, trial and error, statistical analysis of usage data, and regular user surveys were most important for step-wise advances towards user needs.

## Lesson 5:

The danger should be seen but not overrated, that via self-service customer relationships become “depersonalized” and that the intensity and quality of communications suffer. This will hardly ever lead to a loss of customers.

In the representative survey mentioned above, many of the 1.029 replying students held the opinion that the communication between student and department suffers (full agreement: 11,2%, partial: 47,6%, no: 39,2%). However, a much larger number agrees with the statement “Videotex is for me an instrument of rationalization” (full: 57.4%, partial: 37.8%). An even higher percentage accepted the WU videotex system as a necessary efficiency measure for the university administration (64.2% fully, 29.7% partially).

4.4. User interface design and data quality management

Lesson 6:

Speed, i.e. fast access should be the most important goal of user interface design. In mass IS quick standard paths through interactive programs should be developed for guidance of users, containing relatively few explanations but offering clearly recognizable branching opportunities for the inexperienced user. Uniform interfaces for all programs are indispensable.

In the survey of the summer semester 1992, 70.7% of the replies considered the fast usability of programs as “very important”, another 23.3% as “important”. However, encompassing user instructions are important for only 35.8% – approximately the number of replying students who had taken up their studies in the academic year 1991/92. As a consequence of similar results in earlier polls all graphics of the WU videotex system have been eliminated as time went on.

## Lesson 7:

Reliability and currency of the offerings are crucial. Dialog programs with access to permanently up-dated operational databases are most suitable to achieve these requirements. The number of fixed information pages (screens with fixed contents) should be kept low.

According to the 1992 survey, reliability has overriding importance (78.9%) and currency of the information is very important (77.9%). The users were also concerned with brief and to-the-point information and a clearly structured offering, but already to a markedly lesser extent (very important: 48.8% and 40.7%). On the contrary, the all-embracing information supply was very important for only 22.9% of those replying. We have already mentioned that the actual use of general information is even far below this mark.

To ensure high data quality has always been a considerable problem of the WU “multi-vendor” system. An Austrian university is a loosely coupled system of rather autonomous departments, and there was no way to motivate some information providers to keep their offerings up-to-date.

Especially fixed videotex pages that need to be revised after textual changes require high efforts:

\- Downloading the pages to a local PC.

\- Editing the contents, directly on the screen or on print-outs.

\- Eventual data entry of the changes marked on print-outs.

\- Eventual change of the menu tree (structure of the offering).

\- Uploading the revised pages to the host.

All of this work has to be controlled by a central system administration, and most of it has to be done by this office itself. Different trials to decentralize and automate the up-date process failed. Today the WU departments get paper print-outs of their special offerings, hopefully correct them, and send them back to the system administration office that is responsible for the data entry. The number of fixed videotex pages is kept as low as possible and is restricted to truly long-term fixed contents.

Programs incorporated in the WU videotex system – either purely informative or for dialogue with the user – have these problems to a far lesser extent; especially if the announced information has in any case to be recorded for other purposes. At WU, the videotex programs access directly the operational databases where the administrative data are kept up-to-date. This is true for student programs and for faculty programs as well; many serve besides their main purposes as important sources for data collection. By this way, we avoid unnecessary data transfers, in earlier stages often leading to a lack of currency of the videotex data files and to inconsistencies.

## Lesson 8:

In order to avoid confusion and customer complaints, catalogs as well as other information sources used for business transactions in mass IS, must be consistent with the data used. An earlier printed catalog is always obsolete in parts; therefore, an additional permanently up-dated electronic version as supplement is recommended.

About 90% of all questions and complaints of students to the central videotex office at WU concern such data inconsistencies; an electronic version of the catalog is not available yet.

The importance of this issue also became evident in the 1992 survey regarding the WU videotex system. In 83.6% of the 1,029 replies the “correspondence with the catalog” was rated “very important”, in another 12.1% as “important”. Such peak values were not even nearly reached for any other requirement of the registration program.

The direct access to operational databases has never caused any security problems. Complaints about alleged data losses (“I-am-not-on-the-list”-problem) are refutable by protocols of all user transactions. The users’ knowledge about logging keeps the number of complaints without good reason down, and increases the confidence of users in the system.

## Lesson 9:

Many services of mass IS can be used anonymously. But when calling up personal data and in all business transactions (e.g., reservations, orders), the users must identify themselves. The user identification in a mass IS should be demanded as late as possible.

Adequate for the identification of mass IS users are already existing key terms like social security numbers, tax identification numbers, customer numbers, students IDs, etc., together with self assigned passwords. They have to be used for all personal transactions. At WU, the central videotex office is contacted two or three times a day because of forgotten passwords. That is not much, taking into account more than 20,000 users; in the earlier stages of the WU videotex system it has been many times the amount.

The user identification should be demanded as last interaction in the transaction process. With the verification of the ID by a strictly encapsulated step the actual reservation or other action takes place in the data file. Reason for this is that the access to a mass IS is often “public”, meaning, when the user leaves a public terminal, the next user is in an application exactly where the previous user has just left it. This opens the door for improper use, if there is no adequate protection.

## Lesson 10:

Adoption of mass IS on the basis of new IT or innovative mass IS development by “prototyping over the first years” are long-term processes. Therefore, a lot of staying power is needed. And luck – as usual when new consumer products are rolled out!

## 5. Conclusion

Characteristics of mass IS are the voluntary use and a high degree of uncertainty about the users and their requirements. The users must gain substantial benefits to accept the system. In the WU case, the most attractive applications are the on-line reservation in self-service and the retrieval of personal data. General information about faculty, courses, research projects, etc. is not called up. The most important design objectives are ease of use, fast access, reliability, and currency of data. Therefore, the offer of fixed information pages (screens) that have to be edited after changes should be kept low. Direct access to operational databases assures the current up-date. At WU, the standard database security features have always been sufficient. There is a slight danger of reduced personal communications. But the benefits, especially accessibility around the clock and time savings through the automation of routine inquiries, count more for both sides.

The only way to meet the demand may be the step-wise adaption of services by observing and analyzing the user behavior. This evolutionary development and the diffusion process can take some years. Accompanying marketing efforts are crucial. Nevertheless, the risk of failure is rather high. But, the potential benefits for the owner of a mass IS are high as well. The large number of users multiplies time and cost savings for the organization. Better knowledge by automated tracking of user behavior allows a differentiated management of individual customer relationships.

## References

[1] Bauer, J.M. and Latzer, M. (ed.) (1993), Nützliche Verbindungen. Österreichs Telekommunikationsdienste im internationalen Kontext, Oldenbourg, Wien.

[2] Bouwman, H. and Christoffersen, M. (ed.) (1992), Relaunching Videotex, Kluwer Academic Publishers, Dordrecht.

[3] Göpfrich, H.R. (1987), Bildschirmtext in der Ausbildung - dargestellt am Beispiel der Wirtschaftsuniversität Wien, Springer, Berlin.

[4] Göpfrich, H.R., Hansen, H.R., Hasenzagl, K. and Schindlauer, J. (1990), Bildschirmtext als Dienstleistungs- und Rationalisierungsinstrument an der Wirtschaftsuniversität Wien - Abschlußbericht zum Projekt "Entwicklung des WU-BTX-Systems", Arbeitsbericht Nr. 7 zum Tätigkeitsfeld Informationsverarbeitung und Informationswirtschaft der Wirtschaftsuniversität Wien.

[5] Hansen, H.R. (1984), “BTX macht Schule – BTX-Auskunftssystem zur Studentenbetreuung an der Wirtschaftsuniversität Wien”, Siemens data report, Vol. 19, No. 4, pp. 18–24.

[6] Hansen, H.R. and Prosser, A. (1993), “Masseninformationssysteme: Erfahrungen mit Selbstbedienungsinformationsdiensten für EDV-Laien, dargestellt am Beispiel des WU-BTX-Systems”, Proceedings of the WU-Jahrestagung 1993: Forschung für die Wirtschaft - Im Mittelpunkt der Mensch, Service, Wien.

[7] Hansen, H.R. and Prosser, A. (1994), “Entwicklung und Betrieb von Masseninformationssystemen. Schlußfolgerungen aus dem Studenteninformationssystem der Wirtschaftsuniversität Wien”, Wirtschaftsinformatik, Vol. 36, No. 3, pp. 233–242.

[8] Hansen, H.R. (1995), “Conceptual Framework and Guidelines for the Implementation of Mass Information Systems”, Information and Management, Vol. 28, No. 2, pp. 125–142.

[9] Noll, M.A. (1985), “Videotex: Anatomy of a Failure”, Information and Management, Vol. 9, No. 2, pp. 99–109.

![](/api/attachments/XP7RYW7B/fulltext/images/26a3e0d063f5014cb58fdac73b87c5dc3ea94364c41f1385bb7f672269e0aecd.jpg)

Hans Robert Hansen is Professor of Management Information Systems and Chairman of the MIS Department at Vienna University of Economics and Business Administration (Wirtschaftsuniversität Wien; WU in short). His current research interests focus on strategic planning, telecommunications, and applications in marketing and retailing. He is the author of the bestselling IS textbook in German language Wirtschaftsinformatik I,

UTB-Gustav Fischer, and has published numerous other textbooks, research monographs and articles. Prior to joining WU in 1978, he worked for IBM Germany and held faculty positions at Würzburg University and Duisburg University, Germany. He has had a variety of visiting appointments including stays at the Business Schools of New York University and University of California in Berkeley during the academic year 1993/94. His e-mail address: hansen@wu-wien.ac.at
