---
otero_id: 22372
otero_key: "594ZBEFH"
title: "ISO 9000 versus CMM: Standardization and certification of IS development"
authors: "G.J. van der Pijl; G.J.P. Swinkels; J.G. Verrijdt"
year: "1997"
journal: "Information & Management"
doi: "10.1016/s0378-7206(97)00019-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# ISO 9000 versus CMM: Standardization and certification of IS development

G.J. van der Pijl $^{a,*}$ , G.J.P. Swinkels $^{1,b,c}$ , J.G. Verrijdt $^{c}$

$^{a}$ Tilburg University, POB 90153, 5000 LE Tilburg, The Netherlands $^{b}$ Rabobank Nederland, University of Amsterdam, Amsterdam, The Netherlands $^{c}$ Rabobank Nederland, Eindhoven, The Netherlands

## Abstract

A growing number of software developers use standards as a basis for their quality systems. Some of them go one step further and have their quality systems certified. In this paper, two well-known quality standards, ISO 9000 and the CMM, are compared. It is concluded that both standards are useful but there is a growing need for more specific standards. © 1997 Elsevier Science B.V.

Keywords: ISO-9000; Capability maturity model; Certification; Standardization; Information system development; Software quality; Software engineering; Quality standards; Quality systems

## 1. Introduction

Since serious software developers can no longer afford to deliver poor quality software, modern software development organizations are paying a great deal of attention to quality management $[1, 2]$ . In Europe, the ISO 9000 set of quality standards $[3]$ are widely used standards for quality management in software development. ISO 9000-3 $[4]$ was specifically designed for systems development. Today, a growing number of IS developers use standards as a control on implementing quality systems. There is, however, much discussion of these standards and the certificates that accompany their use; many companies are eager to obtain a certificate because of market pressure. This often means that a minimum set of procedures and quality handbooks are developed in the company without a quality system really being implemented or quality awareness being created among the employees. In such cases, the possession of certificates does not guarantee the quality of the software production process or a reasonable price/performance ratio for the products delivered to the client. Moreover, even when a company maintains a quality system that meets the ISO 9000 standards, the quality of the final product cannot be guaranteed. Worse still, adhering to strict software quality standards can, in some circumstances, be counterproductive, because the specific systems development environment in which the production takes place should be tailored for special circumstances and the software development process may need to be changed to accommodate the specific type of system to be produced [5].

In this paper, we discuss the use of standards in the control of the quality of the information systems development process. The ISO model, which is the most popular standard in Europe and Japan, is compared with the Capability Maturity Model (CMM) [6, 7, 8, 9], which is one of the common standards of the USA.

When looking at standards like these, we see that they serve two purposes. On the one hand, they can be used to provide guidance to organizations installing quality systems to produce goods and services of the desired quality. On the other hand, they are the basis for the certification of quality systems. Quality certificates are meant to give buyers of goods and services an impression of the quality of the suppliers and, indirectly, of the quality of their products and services [10]. Problems with standards can arise in either of these fields.

Although CMM solves some of the problems of the ISO model, it also has some shortcomings. In this paper we indicate the direction in which software quality assurance and software quality standards have to develop in order to improve the quality of delivered IS. Our conclusions are based on a literature study and experiences in applying both ISO 9000 and the CMM in systems development projects in a large bank and several organizations in the Netherlands.

## 2. The ISO 9000 standards

The international standards 9000–9004 describe how companies can implement quality systems. Once a system is in place, it may be certified by an independent institution. The certificates can then be used to show customers that the company adheres to externally verified quality standards. The philosophy of the standards is consistent with developments in the theory of quality management [11]. The focus is shifting from controlling the quality of the final product to controlling the quality of its production processes [12]. The essence of the ISO 9000 standard is that a company should visibly control all aspects of the business in order to guarantee a minimum quality level for its products. Visibility is realized by describing the quality system in a Quality Handbook. The standard does not define what is the most effective way of controlling business processes; it simply requires the organization to maintain sets of quality procedures and guidelines without specifying them. This is both the strength and the weakness of the standard. The openness makes it applicable to many different production processes, but it makes it hard for producers of goods and services to decide on the specific type of measures to be taken. For purchasers, it means that a quality certificate does not necessarily indicate that the quality system of the supplier is well attuned to the specific product and market situation. This is the main reason why more specific versions and interpretations of the standard are developed in different types of industries.

For systems development, there is the ISO 9000-3 standard: 'Guidelines for the development supply and maintenance of software.' In this, the life cycle of IS development is taken as the process to be controlled. However, the standard remains a very general description of the procedures and guidelines for quality management.

ISO 9000 is very popular in the United Kingdom and the Netherlands and the number of applications in Germany is rising. There is, however, much criticism, stemming partly from the fact that companies are trying to obtain ISO 9000 certificates for reasons of marketing rather than (total) quality management. But even if we assume that companies use standards to improve their production processes, it is possible to be critical of the contents and construction of the standards. The main criticisms of the use of ISO 9000-3 for systems development are:

\- The general nature of the standard.

\- The fact that it is specified for quality systems of systems development organizations and that little attention is given to quality measures on the level of specific development projects.

\- That ISO 9000 recognizes only one certifiable level of quality, while in practice different quality levels may be advisable for different situations.

\- The emphasis on strict procedures and their documentation in manuals leads to a bureaucratic type of behavior instead of a growing awareness of the importance of quality for the organization. Searching for new insights and methodologies in systems development may be hampered. A good example is Boehm's 'spiral model' [13] which copes with uncertainty in systems development but clashes with the rules of ISO 9000-3.

\- Though throughput time may be more important in some cases than superb quality and a somewhat ‘quick and dirty’ approach might then be advisable, quality standards leave very little room for the idea of end-user and rapid application development.

## 3. The Capability Maturity Model

The Software Engineering Institute's CMM builds on the work of Humphrey. The model presents a growth theory where the quality level of a systems development organization can grow along a given path. The essence of the model is that several quality levels can be recognized. An organization can go from one stage to another and thus grow from having no quality management to a mature situation with a very high level of quality control, as shown in Fig. 1.

Each level is determined by a set of key process areas, which, in turn consist of sets of key practices $[14]$ . By measuring the degree to which key practices are implemented, the maturity level of a systems development organization is measured. The structure for this measurement is given in Fig. 2, where each key process can be judged as being sufficiently (S), partly (P), or insufficiently (I) implemented. The total set of key practices is specifically aimed at the systems development organization, and is much more detailed than the prescriptions of ISO-9000. Therefore CMM leaves much less room for interpretation.

Each quality level can be seen as a well-defined stage on the way to mature organization. A set of well-defined small steps leads from each stage to the next higher quality level. Of course, the main idea behind the model is that a higher degree of maturity leads to better results in terms of defects, costs, throughput times, and quality of the systems delivered. Recent research $[15]$ shows that the CMM's quality levels are not always exactly equal to those in the real world. Possibly, a more gradual pattern of growth would be more realistic. This, however, does not fundamentally change the idea of CMM as an elaborate way to install quality management in systems development in a series of steps. It might, however, influence the idea that the quality of a software supplier's development process can be assessed by looking at a detailed set of key processes and practices, assessing the stage of the supplier. There may be other possible growth paths that enable suppliers to deliver software of the desired quality. This is especially true at the higher levels of the model, where the CMM rules exceed general engineering practices. The quality of these suppliers would not be recognized if their business processes are compared only to the levels of CMM.

## 4. Comparing ISO 9000-3 and CMM

In a project assessing the applicability of ISO 9000 and CMM in IS development environments in a large bank, we formulated a set of criteria for assessing the usefulness of guidelines for quality systems. In Fig. 3, the scores of ISO and CMM on these criteria are presented. From this, it is clear that:

<table><tr><td>level of CMM process</td><td>description</td></tr><tr><td>1. &quot;initial&quot;</td><td>ad hoc, sometimes chaoticproject success not guaranteed</td></tr><tr><td>2. &quot;repeatable&quot;</td><td>costs controlledproduct oriented reactive management system</td></tr><tr><td>3. &quot;defined&quot;</td><td>process documented and standardizedtailored standards for each project</td></tr><tr><td>4. &quot;managed&quot;</td><td>process understood, measured and controlled</td></tr><tr><td>5. &quot;optimizing&quot;</td><td>focus on process improvement and rapid technology updating</td></tr></table>

Fig. 1. The quality levels of CMM.

![](/api/attachments/594ZBEFH/fulltext/images/ab200c0dfdfda230e25ee966f40b208d5695092e6d945ef57a6f0e1c058f04ab.jpg)  
Fig. 2. Assessing the quality level of an organization.

\- Both approaches score high on stability (A.1) ISO 9000 is produced and maintained by the international standards organization, which guarantees that the standard will be available and adapted to developments in the field of quality systems. The SEI will maintain the CMM in its present form up to 1996. From then on, both approaches will probably be combined in a new international standard.

\- Neither standard completely covers the area of IS development. On the one hand, CMM is limited to IS development, while ISO 9000 also covers procurement. On the other hand, CMM covers a wider range of IS development organizations because it covers a wider range of quality levels. Our research [16] shows that there is much overlap between ISO

9000 and the first three levels of CMM. Almost all parts of the ISO standard can be translated into key practices at these two levels. Implementing CMM up to the third level and completing it with only a few additional items from ISO 9000-3 (5.2.2. 'contract items on quality'; 5.8 'acceptance'; 5.9 'replication, delivery and installation'; 6.2.4 'document changes'; 6.8 'included software') makes certification according to ISO 9000 possible. The higher levels of CMM, however, are not addressed in ISO 9000. These findings were recently confirmed by Paulk [17]. Therefore, we qualified the scope of both approaches as average (A.2).

\- CMM is specially aimed at software development. Although the key practices at the lower levels are like those of other ‘engineering’ organizations, at the higher levels, it models this software process in a much more detailed and specific way than ISO 9000. The quality characteristics are described in much more detail than the quality characteristics of

<table><tr><td>REQUIREMENT</td><td></td><td>score CMM</td><td>score ISO</td></tr><tr><td>A.</td><td>Requirements for the model</td><td></td><td></td></tr><tr><td>A.1</td><td>Stability</td><td>high</td><td>high</td></tr><tr><td>A.2</td><td>Scope of the model</td><td>average</td><td>average</td></tr><tr><td>A.3</td><td>Area of application</td><td>high</td><td>average</td></tr><tr><td>B.</td><td>Ease of application</td><td>average</td><td>high</td></tr><tr><td>B.1</td><td>Availability of tools</td><td>average</td><td>average</td></tr><tr><td>B.2</td><td>Availability of experience</td><td>average</td><td>high</td></tr><tr><td>C</td><td>Ease of gradual improvement</td><td>high</td><td>low</td></tr><tr><td>D</td><td>Ease of presenting results</td><td>high</td><td>average</td></tr><tr><td>E</td><td>Degree of acceptance</td><td>low</td><td>high</td></tr></table>

Fig. 3. Comparing ISO 9000 and CMM

ISO 9000-3. Because of this, we found it to be much easier to describe the quality of IS development groups in terms of CMM and to use CMM as a guideline for building quality systems. Therefore, the ease of application of ISO 9000 is scored as average and that of CMM as high (A.3). This explains why a central IS development group in the bank we studied is now switching from ISO 9000 to CMM as the basis for quality improvement, even though the aspiration level has not really changed. Formerly it was aimed at the ISO 9000 level; now the target is set as CMM level three. Our research showed that both approaches have to be adapted to the specific environment in which they are applied. Because of the great variety of software systems in a banking environment, a range of slightly differing quality standards for IS development has to be used throughout the organization.

\- There are no tools for either approach, other than the standards themselves and the CMM questionnaires to support the implementation of the quality system. Consequently, we scored them both as average (B.1).

\- At the time of our research ISO 9000-3 was much better known in the European organizations we visited than CMM. This meant that it was much easier to build on earlier experience with ISO-9000 than with CMM. Thus, we scored ISO as high and CMM as average in this respect (B.2). In the meantime, the use of CMM in the Netherlands has been increasing rapidly, which means that experience with CMM is also available now. An example can be found in, v.d. Genugten [18] who describes the use of CMM in the Philips organization. He shows that the number of faults in software development is drastically reduced by using CMM.

\- The stages of CMM describe a growth path to higher levels of quality. Following this path makes gradual improvement of quality easier in CMM than in ISO 9000. The ISO standards prescribe one fixed level of quality management. CMM points out that different ones are possible, but it does not prescribe which level has to be chosen: this choice is determined by the specific situation in which systems development takes place and by the demands of the software purchaser. Recent experiences in the banking environment have made it clear that it is much easier to discuss desirable and attainable quality levels on the basis of CMM (C).

\- Because of the more detailed character of CMM, it proved to be the better method for presenting the results of quality measurement. Therefore CMM scores high and ISO only average (D). There is, of course, a strong correlation between this conclusion and the one above.

\- CMM was still relatively unknown at the moment of our research, which made the acceptance of this standard rather difficult. ISO scored high for acceptance and CMM only low (E). At this point however, CMM is introduced as a philosophy for improving some important IS development departments in the bank.

It will be clear from this comparison that CMM solves some of the problems associated with ISO 9000. The more detailed specification of quality characteristics makes it much easier to use CMM as a blueprint. Due to the explicit attention to relevant aspects of development, it is also much easier to attune CMM to different circumstances. In the banking environment, where information systems of a very diverse nature are built by different IS groups in the organization, this is a very important distinction between the two approaches. IS development groups can choose the CMM quality level they want to attain. This also means that the software purchaser can choose a supplier with a quality system that meets his or her specific needs.

Since the growth path to quality indicated by CMM is not the only possible growth path, one should be careful not to use CMM exclusively. Organizations following a different growth path could also deliver good quality software [19].

## 5. Expected trends

Software projects have to be evaluated relative to the strengths and weakness of both the development organization and the user organization $[20]$ . This analysis determines the specific set of quality measures to be taken but makes it very difficult to use a standard quality assurance system. We must therefore strike a balance between specifying a set of minimum requirements for all projects and leaving enough room for the peculiarities of individual projects. A complete quality system takes into account all factors that explain the quality of the final product. A variety of aspects, such as the people involved, the methods and tools used, and the management commitment influence the result. Practical experience with the bank and other organizations shows, however, that we do not know all the factors and causal relationships involved $[21]$ .

Measures of improving quality are diverse (preventive, detective, corrective) and are partly exchangeable; for example, if some members of the project team have not learned the methods, they will have to pay more attention to testing the final product. Using several methods makes it possible to take care of the specifics of each project; however, differences in steps and deliverables make it difficult to compare projects and thus accumulate experience. There are some trends that support the development of more situation-specific norms, such as those for specific areas (e.g. detachment), development of quality metrics (e.g. using function points), and specifying software quality [22].

The more organizations that use quality systems, the more likely it is that parties participating in software contracts will use different quality systems. Even if those systems do not conflict, taking all these requirements into account will often be very complicated and costly. Current quality standards are mainly oriented towards standardizing activities and procedures. Innovative projects, however, require room for new ideas and creativity. Standardization may encourage creativity if it takes away the worries of basic quality issues. Standardization may hamper creativity if it limits the number of new solutions that can be taken into account. In this type of projects, relying on standardization too heavily may hamper creativity. Standardization is not the only way to guarantee quality. Other coordination mechanisms can also be used, for example, standardization of skills, standardization of outputs and communication among all concerned [23, 24].

Project- and organization-specific quality system improvements can be implemented and certified only if products and processes can be measured with a clear set of metrics. This is true for both ISO and CMM, although CMM stresses measurement more than ISO 9000. Interesting work in this direction is going on in the ESPRIT-AMI project [25] but so far there is no generally accepted set of metrics. Information technology and methods of information systems development are changing quickly. International standards generally develop at a much slower pace.

The specification of a quality system is a matter of weighing costs and benefits for organizations as a whole as well as specific projects. Some important questions are:

\- Are our clients obliging us to comply with standards (such as CMM for the military sector and nowadays even for all government in the USA or Llyods for the steel industry)?

\- Does a certified quality system really improve the bottom line because of its commercial importance?

\- Does such a formalized approach fit the culture of the organization?

\- Does a well-balanced quality system make it possible to offer our clients better, lower risk contracts (e.g. fixed date, fixed price, fixed quality)?

\- How sure are we that we can profit from our investment in quality production systems?

\- Does reduction of the number of errors reduce costs (e.g. because of a smaller number of modifications or lower insurance premiums)?

Advantages and disadvantages of improvements in the systems development process have to be weighed against each other and against the costs of implementation [26]. Results may differ for different parts of the organization. In the long run, efforts should be directed at formulating more specific standards for specific situations or else at developing standards that contain substandards that apply in different circumstances.

Finally, we want to draw attention to the fact that a quality system can only deliver good products if the specifications with which the systems development starts conform to the wishes of the users of the product.

This means that the phase of formulating the specifications has to be attended to in the quality systems itself. Fortunately, we see that in the oncoming new version of the ISO-9000-3 there is much more attention to this point than in the first edition of this standard. In more recent approaches to systems development like prototyping and RAD the specification of requirements is an integrated part of the development process. Quality systems for these approaches thus have to cover the specification part of the process.

## 6. Summary and conclusions

At present there is a conflict between the desire for better quality systems resulting in measurable improvements of the systems development process and the way in which this is implemented by means of standards. Quality certificates can give a wrong impression of the real capabilities of an organization, but this should not lead to the abolition of standards. The majority of organizations can improve their systems by making (sensible) use of the standards. In the short term, the quality of systems development can be improved by an approach that is specially constructed for assessing systems development environments, that support measurable improvement in the development process, and that support the choice and implementation of actions. Although not perfect, CMM offers more possibilities than ISO-9000-3.

In the longer term, standards and certificates will have to take into account the diversity that exists in the real world. Standards and certificates will have to accommodate this. We think this process will take some time and that, therefore, organizations will have to carefully assess the value of quality certificates in different situations.

## References

[1] D.d. Phan, J.F. George and D.R. Vogel, “Managing software quality in a very large development project,” Information and Management, 29 (1995), pp. 277–283.

[2] M.J. Pearson, C.S. McCahon and R.T. Hightower, "Total quality management: Are information systems managers ready?" Information and Management, 29 (1995), pp. 251-263.

[3] ISO 9000-9004 Quality Management and Quality Assurance Standards, 1987.

[4] ISO 9000-3, Quality management and quality assurance standards, part 3: Guidelines for the Application of ISO 9001 to the Development, Supply and Maintenance of Software, 1991.

[5] B. Fazlollahi and M.R. Tanniru, “Selecting a requirement determination methodology – Contingency approach revisited,” Information and Management, 21 (1991), pp. 291–303.

[6] W.S. Humphrey, Characterizing the software process, IEEE Software, March 1988.

[7] W.S. Humphrey, Managing the Software Process (Addison Wesley, 1989).

[8] M.C. Paulk, B. Curtis and M.B. Chrissis, Capability Maturity Model for Software, Software Engineering Institute, CMU/SEI-91-TR-24, DTIC Number AD24063, August, 1991.

[9] M.C. Paulk, B. Curtis, M.B. Chrissis and C.V. Weber, Capability Maturity Model for Software, Version 1.1. Software Engineering Institute, CMU/SEI-93-TR-24, August, 1993.

[10] D. Rugg, Using a capability evaluation to select a contractor, IEEE Software, July, 1993.

[11] J.M. Juran, Juran on Planning for Quality, McMillan, New York, 1988.

[12] G.J. van der Pijl, “Measuring the strategic dimensions of the quality of information,” The Journal of Strategic Information Systems, 3(3) (1994).

[13] B.W. Boehm, “A spiral model of software development and enhancement,” Computer, 21(5) (1988), pp. 61–72.

[14] C.V. Weber, M.C. Paulk, C.J. Wise and J.V. Withey, Key Practices of the Capability Maturity Model, Software Engineering Institute, CMU/SEI-91-TR-25, August, 1991.

[15] D. Drehmer, S. en Daklava, Measuring software engineering maturity: A Rash calibration, Proceedings of the Fourteenth International Conference on Information Systems, Orlando, December, 1993.

[16] J.G. Verrijdt, Het beheersen van kwaliteitsverbetering: groeien van Murphy naar Humphrey (Controlling quality improvements: Development from Murphy to Humphrey).

[17] M.C. Paulk, How ISO 9000 compares with the CMM, IEEE Software, January, 1995, pp. 74–82.

[18] J. Roooijmans, H. Aerts and M. van Genuchten, "Software quality in consumer electronic products," IEEE Software, January, 1996.

[19] T. Bollinger and C. McGowan, “A critical look at software capability evaluations,” IEEE Software, (1991), pp. 25–41.

[20] L.J.M.W. Gielen and G.J.P. Swinkels, Kwaliteitsbeheersing bij de ontwikkeling van informatiesystemen via knelpuntenanalyse (Analysing strengths and weaknesses as a means of quality assurance for the development of information systems), Handboek A.I.V., November, 1992.

[21] Capers Jones, Programming Productivity, McGraw-Hill, 1986.

[22] ISO 9126 Software Product Evaluation – Quality Characteristics and Guidelines for their Use, International Organization for Standardization, Geneva, 1991.

[23] H. Mintzberg, Structure in Fives; Designing Effective Organizations, Prentice Hall International, Englewood Cliffs, NJ, 1983.

[24] Pijl G.J. van der, P.L.M. Weterings, Standaardisatie in systeemontwikkeling (Standardization and systems development), Maandblad voor bedrijfsadministratie en organisatie, December, 1990.

[25] C. Debou, J. Lipták, H. J. en Schippers, “Decision making for software process improvement: A quantitative approach,” Journal of Systems Software, 26(1), pp. 43–52.

[26] R. Dion, Process improvement and the corporate balance sheet, IEEE Software, July 1993.

Frits Swinkels graduated from Tilburg University (Management Information Systems and Accountancy). He has several years of experience as consultant and EDP-auditor, working with a large audit and consultancy firm, specialized in information systems development and quality assurance. Currently he is with Rabobank Nederland, a large Dutch bank, as project manager. He is also working part-time with the University of Amsterdam as an assistant professor at the faculty of economics and econometrics. His research interests are systems development, quality, risk analysis and costs and benefits of information systems.

G. John van der Pijl is Assistant professor in information systems at Tilburg University, department of Information Systems and Director of studies of the post-graduate training programme in EDP-auditing at the Tilburg Institute of Advanced studies. Published a Ph.D. on “Quality of Information in theory and practice.” Teaches Systems Development and Management Information in the masters programme of the university and several ‘quality’-related topics in various postgraduate programmes. Research topics: quality of information, the application of groupware in systems development, IT applications in tourism, EDP-auditing.

Jeroen G. Verrijdt graduated from Tilburg University (Management Information Systems and Accountancy). Currently he is working with Rabobank Netherlands as project manager in the division Client Advise Affiliated Banks.
