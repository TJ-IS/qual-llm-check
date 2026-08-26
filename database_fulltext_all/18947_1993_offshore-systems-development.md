---
otero_id: 18947
otero_key: "UDGHJP2Y"
title: "Offshore systems development"
authors: "Ramrathnam Ravichandran; Nazim U. Ahmed"
year: "1993"
journal: "Information & Management"
doi: "10.1016/0378-7206(93)90045-u"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Offshore systems development

Ramrathnam Ravichandran and Nazim U. Ahmed

Ball State University, Muncie IN, USA

Many companies are increasingly shifting software development operations to offshore sites in countries like Ireland and India. This paper examines the offshore computing phenomenon in the context of a complex systems project. The extent to which offshore computing can be carried out in different phases of the system development is explored. The utilization of various telematic technologies to facilitate this is examined. A framework for offshore project and site selection is presented.

Keywords: Global software industry; Offshore computing; Offshore systems development; Software development; Software exports; Software imports; Systems analysis; Systems design; Systems development; Telecommunications technology

![](/api/attachments/UDGHJP2Y/fulltext/images/6c77c1e1244319db40a34357717b4e9b79ac8d41cacea703fecc491b62e16c81.jpg)

Ramarathnam Ravichandran ('Ravi') is an assistant professor of information systems at Ball State University, Indiana, USA. He received his Ph.D. in Management Information Systems from Indiana University, Bloomington. His articles have appeared in Decision Sciences and other journals. He is a member of Association for Computing Machinery, Decision Sciences Institute, The Institute of Management Sciences and American Association of Artificial Intelligence. His

current research interests include decision making, decision support system, database design, expert systems and systems development.

## 1. Introduction

Although rapid advances were made in computer technology in the past three decades, the demand for computer applications has generally outstripped the supply [2,17,21]. Currently the applications backlog is estimated to be about 29 months [8]. Recent developments that improve programming productivity, such as computer-aided software engineering (CASE) and fourth-generation programming languages (4GLs), are not expected to alleviate the ever-growing demand for more complex, functional, and application specific software systems [9,10,29]. The worldwide software market is expected to grow from \$120 billion in 1990 to \$1 trillion in 2000 [4,34].

While the cost of hardware has been dramatically declining, and the computing capacity has grown tremendously, the cost of developing systems is increasing. More than 50% of the organizational IS budgets is now spent on software. Software development is generally very labor intensive and is characterized by limited capital requirements.

Many US companies are increasingly shifting software development operations to offshore sites in countries like Ireland, India, Singapore, and Argentina. This paper examines the offshore computing phenomenon in the context of a complex systems development project. The paper examines the reasons for offshore computing, identifies special problems associated with it, addresses its applicability to various phases of systems development, explores the utilization of telematic technologies to support the process, and addresses issues in the selection of suitable offshore development projects and sites.

![](/api/attachments/UDGHJP2Y/fulltext/images/7f1671fd75d460303bdab456cfa668201d04b741a24c0ab8e4280cd9c7bc499e.jpg)  
and many other journals.

## 2. Advantages of offshore computing

## 2.1. Cost savings

Software development costs tend to be dominated by programmer salaries. The average annual salary for an entry-level programmer is \$26 000 in the US, \$17 000 in Ireland, and \$3600 in India [14]. In Japan good software programmers are paid about \$100 000 [33].

A survey by the Australian Department of Industry, Technology and Commerce [16] found that the main cost component of software development was the expertise of the software writer. Capital expenditure per employee in small firms with less than 20 employees was \$6300 in 1986–87. For larger firms it was \$4800. With the cost of the hardware dropping every year, the labor cost dominates the cost of software development. Since labor costs are lower in developing countries, they have a competitive cost advantage over industrialized nations.

This competitive advantage enjoyed by the developing countries may, however, be limited to certain software projects or some parts of a project. Recent developments in automated program generation and software engineering, such as CASE tools, can sometimes reduce the level of expertise required for software development $[5]$ . If end users can specify the requirements, automated tools can generate program code (in third generation languages such as PASCAL or C) or ready-to-run executables $[1]$ . However, CASE tools do not usually generate code in fourth generation languages (4GLs). Few large projects would consider the use of CASE code for their core.

## 2.2. Programmer availability

There is a shortage of skilled software programmers in the US [23] and Japan faces a similar situation [18]. According to the Ministry of International Trade and Industry (MITI), the shortfall will be 251 000 software engineers in 1990 and 512 000 in 1995. By the year 2000, the supply of software engineers is expected to be 1.175 million against a demand of 2.14 million. Due to the so called software crisis it is difficult to hire software engineers of reasonable quality; moreover, the current sales return is only \$70 000 per person in the Japanese software industry compared with the \$100 000 salary. As a result, offshore computing becomes an attractive option for meeting development demands.

## 2.3. Market entry advantages

Offshore sites can provide access points to markets. For instance, Boeing Computer Services has an established offshore development site in Ireland. When Europe becomes a single market after 1992, Boeing will be ahead of some competitors with its software development facility well in place. Boeing plans to use this facility as an entry point to the large market. It will export to the EEC its products developed in the US and other sites around the world. This strategy is similar to the Japanese acquisition of England's ICL.

As an another example, Texas Instruments has set up an offshore site in India. The Asian and Pacific Rim areas are expected to be among the major areas of growth over the next 20 years. Texas Instruments wants to have a strategic presence there and be part of that growth [24].

## 2.4. Improved quality

The quality of the systems development process is perceived to be higher in offshore sites. For example, while most systems development projects are completed successfully in offshore sites, about 25% of the projects in the US are aborted. The high turnover rate among software programmers further exacerbates the problem. A survey by Touche Ross & Co. found that the average turnover rate in 1988 was 9.5% and 11.9% in 1989, with an expected 12.8% in the years 1990–1995 [14]. When software programmers leave in the middle of the project, the development process is likely to be adversely affected.

## 3. Special problems

## 3.1. Language barriers

Most of the systems developed in the US, the EEC, and Japan are written in English. Offshore sites in countries with English as a major language, such as India and Ireland, have an edge. But even then, problems due to conventions arise. For instance, the format for date in the US (month/day/year) is different from that used in the UK or India (day/month/year). If a system developed offshore does not take such notational difference into account, errors may result. Another area is in spelling differences such as check vs. cheque.

Languages such as German, French, and Japanese are not as commonly known in the developing nations as English. As a result producing systems in these languages is not as easy as developing them in English. Languages such as English, German, Spanish and French employ the Roman alphabet and thus the need for specialized display hardware in offshore sites is not acute though accents and diacritical marks may be needed. For instance, many personal computers can display French, German, Spanish, and Russian Cyrillic using the set of DOS “KEYBxx” commands and “code page switching” [27]. For Arabic, Kanji, and Chinese, specialized hardware is generally needed, though increasing sophistication of video display systems in terms of their resolution, memory, and refresh speed rates may alleviate this problem.

## 3.2. Differences in laws and regulations

The second problem involves the difference between the laws and regulations of the onshore and offshore sites. Differences are important in areas such as commercial banking. Necessary controls mandated by the specific laws at the user site, e.g., French banking regulations for a French banking system, need to be built into the application code while it is being developed at the offshore site. Also changes to such systems must reflect new regulations. For example, the “funds availability” policy was changed by the US Federal Reserve Board several times during the past decade, and banking information systems developed offshore – such as those developed by Citicorp in India [22] – must accommodate such changes. The procedures to modify the system must be available at user sites, otherwise offshore developers need to be contacted for assistance or modifications.

## 3.3. Infrastructure problems

Offshore sites may lack infrastructure support usually taken for granted at user sites. For instance, the Texas Instruments facility in Bangalore, India has made provisions for a standby power supply because of frequent power outages. Automatic changeover in the case of a power failure is provided for by an uninterruptible power supply (UPS) system with storage batteries to supply the power until the generator is automatically started and up to speed.

## 4. Applicability to development phases

Under the life cycle development methodology (LCDM), the system development process consists of several phases $[13,3,31]$ ; e.g., Whitten, et al. consider eight activities $[32]$ : (a) survey the situation; (b) study the current system; (c) define user requirements; (d) evaluate alternative solutions; (e) select computer hardware and software; (f) design; (g) construct; and (h) deliver the new system. In this paper it is assumed that the system under consideration has successfully passed its initial feasibility phases. The systems development process can then be grouped into three phases for offshore development: (a) analysis and design; (b) implementation/coding; and (c) testing. Offshore systems development can be more useful in some of these phases than in others.

## 4.1. Design and analysis phase

During the analysis phase, it is essential to interact with users and this is not easy from the offshore facility. As the number of interested users increases, it becomes impossible to involve offshore systems development personnel. If the system to be developed is amenable to highly structured specifications $[11]$ , it is much easier to employ offshore facilities.

## 4.2. Implementation / coding phase

In the implementation phase, the need for interaction with users is minimal. While advances in the area of automated program generation and verification have been substantial in the past two decades, programmers are still needed to code complex applications, and expert programmers can be employed at the offshore centers to produce the system.

## 4.3. Testing phase

Initial testing is done by developers to debug the systems. If the offshore sites do not have the exact hardware platforms to be used at the user site, emulation software systems can aid in testing the application. Developers at the offshore sites can then concentrate on development rather than hardware platform setups. Similarly, emulation systems can be fruitfully employed while developing embedded systems applications in engineering, data collection, manufacturing and R&D activities.

With the advent of remote diagnostic capabilities, software systems can be installed at user sites and problems can be diagnosed and corrected using phone lines. As long as the communication lines are set up using high bandwidth channels, such as satellite links, the costs of such communication become minimal. However, final systems integration and validation tests can only be performed at the user sites.

Level of application of telematic technologies to offshore systems development

<table><tr><td>Telematics technology</td><td>Design and analysis phase</td><td>Implementation phase</td><td>Testing phase</td></tr><tr><td>Satellite links</td><td>High</td><td>Low</td><td>High</td></tr><tr><td>Electronic mail</td><td>Low</td><td>Low</td><td>Medium</td></tr><tr><td>Bulletin boards</td><td>None</td><td>Low</td><td>High</td></tr><tr><td>On-line links</td><td>Low</td><td>Low</td><td>High</td></tr><tr><td>FAX</td><td>High</td><td>Low</td><td>High</td></tr><tr><td>Audio teleconferencing</td><td>High</td><td>None</td><td>High</td></tr><tr><td>Video teleconferencing</td><td>High</td><td>None</td><td>Low</td></tr><tr><td>Remote diagnostics</td><td>None</td><td>None</td><td>High</td></tr><tr><td>Videotaping</td><td>High</td><td>None</td><td>Low</td></tr><tr><td>Telecasting</td><td>High</td><td>None</td><td>Medium</td></tr></table>

## 4.4. Applicability across phases

The development process is highly iterative; a high degree of support for interactive communication across the phases is essential throughout the systems development process. If the requirements and specifications are stated very well and are not prone to error, then the offshore development process can proceed at a much greater pace. Otherwise the need for interaction between the offshore facility and the user site is increased. Moreover, when changes are needed, sometimes during development, the need for approving and revising the specification increases.

## 5. Utility of telematic technologies

Many problems arise due to communication barriers between sites. Given the rapid evolution of global communication networks, telecommunication technology can be profitably employed to alleviate many problems. Table 1 summarizes the level at which different telematic technologies [28,6] can be applied to various phases. Based on a qualitative assessment of the potential of each, its usefulness is characterized as none, low, moderate, or high.

## 5.1. Satellite links

Captive satellite links are useful in offshore development: A large volume of data can be transmitted immediately. For example, Texas Instruments has a link between the corporate hub facility in Bedford, Britain and the offshore systems development facility in Bangalore, India [24]. Seventy Indian software engineers produce programming tools for TI, with their output transmitted via satellite link. But even a large company, such as TI, cannot exploit the full bandwidth available. The link has 30 channels for transmitting data and costs about \$180 000 US (4.5 million Indian Rupees) per year. In order to make the link viable, TI shares it with other international software developers in India, but still the bandwidth is not fully utilized. This suggests the economic viability of supporting large data transfer volumes between the sites.

## 5.2. Electronic mail and forums

Software vendors within the US are increasingly turning to electronic mail and forums to address software maintenance. Developers from offshore sites can communicate with the user population, especially in the beta-testing stages, by using electronic network systems. It is also possible to have a user located BBS system that can be accessed through dedicated lines (e.g., satellite links). International WATS lines accessible only to the offshore developers is also a useful approach. For example, Datamatic Consultants Ltd., an offshore UNIX systems developer located in Santa Cruz Electronics Export Processing Zone (SEEPZ), Bombay, India is linked online to the AT&T Bell Labs computers via a dedicated satellite link [19].

## 5.3. Fax machines

Fax machines are useful in transmitting visual images that are often used in the development process; the inputs and outputs can be either paper or scanned image files. Exact spacing requirements of legal forms (such as income tax returns) can be more easily developed using scanned images than input layout forms, printer spacing forms and display layout charts. In a similar vein, preprinted forms can be accommodated. Moreover, when non-Roman alphabets are involved, FAX machines help in the quick resolution of design questions. The use of FAX machines is facilitated by adherence to standards, such as Group III [28]. Widespread adoption of faster Group IV standards is expected to occur in the near future.

## 5.4. Teleconferencing

With teleconferencing technology, it is possible to carry out some part of the analysis phase from the offshore facility. If the system is developed for professional end users, such as engineers, it is likely that much of the analysis process can be carried out using teleconferencing, since professional communication is largely standardized across national borders. Professionals can be employed at the offshore sites. They can then interact with the professionals at the user sites and convey the requirements to the software engineer teams.

Understanding body language of the users is sometimes important in systems development $[20]$ . Video teleconferencing makes it possible to observe this and profit from its signals.

## 5.5. Telecasting

Often systems analysts visit the user site to watch the user work on the current information system. Observed activities may include the operation of a clerk at the ticket reservation desk of an airline company, the operation of a bank loan officer, etc. Such operations and related interviews can be captured using a video camcorder, and the resulting video images transmitted to the offshore site as part of the initial requirements. Transmittal of such video images will help in clarifying the initial specification. With satellite technology, it is even possible to go one step further and perform interviews using live telecasting.

## 6. A decision-making framework for offshore development

A decision framework for offshore systems development is now presented. Two issues are addressed under this framework: (a) the suitability of a project for offshore development; and (b) the selection of the specific offshore site in which to develop the project. If the final system to be developed is large, the development effort can be divided into several projects; each of these, in turn, can be evaluated for its suitability for offshore development. Given the specifications of the project, its feasibility needs to be ascertained. If the project is judged feasible, then its suitability for offshore development can be assessed. If it appears infeasible, then other projects can be considered, alternatively it may be possible to modify the project specifications so that the project becomes feasible while still meeting major user needs. If a project is deemed suitable, then a potential offshore site is sought, otherwise the project is developed at home or the user site.

Although a sequential decision-making process has been presented, interactions between phases can occur. For instance, a project which is initially deemed infeasible because of cost may be feasible if developed offshore.

Table 2  
Factors influencing adoption of offshore development

<table><tr><td>Factor</td><td>Favorable</td><td>Unfavorable</td></tr><tr><td colspan="3">User factors</td></tr><tr><td>Number of interactions of the proposed system with users</td><td>Low</td><td>High</td></tr><tr><td>Number of users involved in specifications at the user site</td><td>Low</td><td>High</td></tr><tr><td>Number of organizational units in which end users are located</td><td>Low</td><td>High</td></tr><tr><td>Level of involvement of professional users</td><td>High</td><td>Low</td></tr><tr><td colspan="3">Application factors</td></tr><tr><td>Level of complexity of application</td><td>High</td><td>Low</td></tr><tr><td>Size of the application</td><td>High</td><td>Low</td></tr><tr><td colspan="3">Specification factors</td></tr><tr><td>Level of structure in system specification</td><td>High</td><td>Low</td></tr><tr><td>Number of changes to system specifications over a period of time</td><td>Low</td><td>High</td></tr></table>

## 6.1. Suitability for offshore development

The various factors which affect the suitability of a project for offshore development are summarized in Table 2. For each, its impact on suitability is presented in terms of favorable or unfavorable levels.

Three types of factors are important here: User, application, and specification factors. The first deals with the extent of communication and coordination efforts. If a system is highly interactive, then the final users need to be involved more. Prototyping methodology may be preferred here $[12,15,26]$ , and this, in turn, necessitates increased communication and coordination between user and developer sites.

Application factors deal with complexity and size of the application. If the system is fairly simple and small (e.g., a simple forecasting model), the chances are that not much development effort is required. In this case the cost of setup time involved in communication and coordination may offset any advantages that might accrue from offshore development.

Specification factors deal with the complexity of structure and stability of the system specifications. The more structured a system specification, the easier it is to communicate. Also, the developers need to spend less time clarifying ambiguities. As the number of changes to system specification increases, the cost of communication and co-ordination increases, making it difficult for offshore development.

Table 3  
Factors for evaluating specific offshore sites

<table><tr><td>Factor</td><td>Favorable</td><td>Unfavorable</td></tr><tr><td colspan="3">Technological factors</td></tr><tr><td>Ability to network user and offshore sites using telematics</td><td>High</td><td>Low</td></tr><tr><td>Infrastructure support</td><td>High</td><td>Low</td></tr><tr><td colspan="3">Geopolitical factors</td></tr><tr><td>Tariff barriers</td><td>Low</td><td>High</td></tr><tr><td>Differences in laws and regulations between user and offshore sites</td><td>Low</td><td>High</td></tr><tr><td>Market entry advantages</td><td>High</td><td>Low</td></tr><tr><td>Short-term and long-term political stability</td><td>High</td><td>Low</td></tr><tr><td colspan="3">Managerial factors</td></tr><tr><td>Offshore analyst communication skills and expertise</td><td>High</td><td>Low</td></tr><tr><td>Development cost</td><td>Low</td><td>High</td></tr><tr><td>Commitment to staying within schedule and budget</td><td>High</td><td>Low</td></tr></table>

If most of the factor levels for a given development project are found to be unfavorable, then the system may have to be developed locally.

## 6.2. Offshore site evaluation

Table 3 presents the factors which are important for evaluating an offshore facility when determining if it will be suitable for system development.

It is important that the site under investigation has the necessary technologies to make offshore computing possible. Also, the offshore site should have compatible hardware and software to facilitate application development and portability. There may be several site-specific factors affecting the suitability of offshore development. Geopolitical factors determine which country is more suitable. Given that most of the countries aspiring to promote software development industries establish free trade zones, tariffs may not be important in final site selection. Managerial factors, such as development costs and commitment to work, also affect the final site selection; e.g., in Singapore the commitment to schedule and budget is high and workers are expected to finish up projects within the targeted time and budget resources, even if it means overtime without pay.

An offshore site that has many unfavorable levels for factors has to be dropped from further consideration and then the system may have to be developed at home.

## 6.3. A multicriteria approach

The decision framework, as discussed so far, deals with one project and one offshore site. It is straightforward to extend this to multiple projects and sites. The need for evaluation of multiple projects and sites can arise in different situations. A multicriteria approach can be fruitfully employed to make the final selections from a set of potential candidates $[35]$ . Using such an approach, based on past experience and expert judgment, each site is given a score on each factor. The IS manager should assign importance weights to each of the factors. For each site, its score is multiplied by the weight and summed. This score is then used to rank the sites. The rating scale can be a Likert-type scale ranging from 1–7, with 1 representing most unfavorable and 7 most favorable. Based on past experience, a cutoff score may be established to eliminate offshore sites from consideration. Following the elimination-by-aspects approach [30], it is also possible to establish a minimal cutoff score for each factor to eliminate some sites. Explicit consideration of important factors in project and site selection can help in avoiding pitfalls typically encountered in systems development [25].

## 7. Discussion and conclusion

Systems development has been traditionally viewed as a local operation. With better communication and economic benefits, such traditional assumptions are now being re-examined. Initially complex system development efforts have been moved to other locations; e.g., California's Silicon Valley and Boston's Route 128 in the US have provided major hardware and software development efforts for customers spread throughout the world. Environments congenial to these are now being established elsewhere.

The next logical step is offshore computing, wherein the software developers reside in another country. Globalization of the world through telecommunications and networking technology makes it possible to relocate users and designers. Many problems faced in systems development, such as ambiguous specifications, can arise in local as well as offshore development efforts. The pertinent issue is the quick resolution of such problems $[7]$ . Telematics technology makes it possible to clarify the ambiguities inexpensively and quickly.

Information systems practitioners have to be aware of the tradeoffs involved in offshore development. Cost savings from lower programmer salaries should be higher than the additional setup, communication and co-ordination costs. However, strategic considerations, such as market entry and paucity of programmers, may make such tradeoffs a moot issue in certain cases. Using the proposed decision framework, IS managers can use experience and judgment in the qualitative evaluation of important decision factors.

This paper explored various issues in the emerging area of offshore development. Future research can investigate specific aspects of offshore computing through empirical studies.

## Acknowledgments

The authors wish to thank the reviewers for their helpful comments in revising the manuscript. Special thanks go to Professor Edgar Sibley for his excellent editorial comments.

## References

[1] Matrix Layout. Matrix Inc., Boston, MA, 1990.

[2] Alloway, R.M. and J.A. Quillard, “User managers’ system needs”, MIS Quarterly, June 1983, pp. 27–41.

[3] Amadio, William, Systems Development: A Practical Approach, Mitchell Publishing, Santa Cruz, CA, 1989.

[4] Anonymous, “Software market will increase to \$1 trillion by year 2000 from about \$50 billion in 1988”, World Trade, 6, March 1989.

[5] Avgerou, Chrisanthi, “The applicability of software engineering in information systems development”, Information and Management, 13, 3, October 1987, pp. 135–142.

[6] Black, Uyless D., Data Networks: Concepts, Theory, and Practice. Prentice-Hall, Inc., Englewood Cliffs, NJ, 1989.

[7] Bostrom, Robert P., “Successful application of communication techniques to improve the systems development process”, Information and Management, 16, 5, May 1989, pp. 279–295.

[8] Bucken, Mike, “MIS backlog lives on”, Software Magazine, 10, 5, April 1990, pp. 28–29.

[9] Carlyle, R.E., “Where methodology falls short?”, Data-mation, 34, December 1988, 179–191.

[10] Case, A.F., “Computer-aided software engineering: technology for improving software development productivity”, DataBase, Fall 1985, pp. 35–43.

[11] Dijkstra, E.W., Structured Programming, Academic Press, London, 1972.

[12] Reed Doke, E., “An industry survey of emerging prototyping methodologies”, Information and Management, 18, 4, April 1990, pp. 169–176.

[13] Flaatten, P.O., D.J. McCubbrey, P.D. O'Riordan and K. Burgess, Foundations of Business Systems, The Dryden Press, Chicago, IL, 1989.

[14] Goff, Leslie, “U.S. programmer shortage spurs offshore software development”. MIS Week, 11, 4, January 1990, pp. 28–29.

[15] Guimaraes, Tor, and Jayant V. Saraph, “The role of prototyping in executive decision systems”, Information and Management, 21, 5, December 1991, pp. 257–267.

[16] Hughes, Gordon, “The software industry and the need for government assistance”, Australian Accountant, 57, September 1987, pp. 61–65.

[17] Jeffrey D.R. and M.J. Lawrence, “Some issues in the measurement and control of programming productivity”, Information and Management, 4, 4, November 1981, pp. 169–176.

[18] Kamata, Hiroki, “Software players tied to hardware”, Software Magazine, 9, 14, November 1989, pp. 74–76.

[19] Kanodia, L.S., “India’s growing software industry”, India Today, 44, April 30, 1990.

[20] Kendall, K.E. and J.E. Kendall, Systems Analysis and Design, Prentice-Hall, Inc., Englewood Cliffs, NJ, 1988.

[21] Martin, James and Carma McClure, Structured Techniques: The Basis for CASE, Prentice Hall, New Jersey, 1988.

[22] Premkumar, R.M., “The achievement zone”, India Today, 39, April 30, 1990.

[23] Richard, Ash, “Offshore development”, Journal of Systems Management, 41, 6, June 1990, p. 17.

[24] Rozeboom, Robert W., “Texas Instruments India Private Limited: A global informatics model”, Telematics and Informatics, 5, 4, 1988, pp. 415–420.

[25] Saarinen, Timo, “Systems development methodology and project success: An assessment of situational approaches”, Information and Management, 19, 3, October 1990, pp. 183–193.

[26] Shova, Peretz and Nava Pliskin, “Structured prototyping: Integrating prototyping into structured system development”, Information and Management, 14, 1, January 1988, pp. 19–30.

[27] Somerson, Paul, DOS Power Tools: Techniques, Tricks and Utilities, Bantam Books, Inc, New York, 1988.

[28] Stamper, David A., Business Data Communications, Benjamin/Cummings Publishing, Menlo Park, CA, 1986.

[29] Stamps, D., “Cranking out productivity”, Datamation, July 1, 1987, 55–58.

[30] Tversky, A., “Elimination by aspects: A theory of choice”, Psychological Review, 79, 4, 1972, pp. 281–299.

[31] Wetherbe, James C., “Systems Analysis and Design,” West Publishing, St. Paul, MN, 2nd edition, 1984.

[32] Whitten, J.L., L.D. Bentley and T.I.M. Ho, Systems Analysis and Design Methods, Times Mirror/Mosby College Publishing, St. Louis, 1986.

[33] Ed Yourdon, “U.S. has no monopoly on software”, Software Magazine, 9, 14, November 15, 1989, pp. 43–45.

[34] Edward Yourdon, Modern Structured Analysis, Prentice-Hall, Inc., Englewood Cliffs NJ, 1989.

[35] M. Zeleny, Multiple criteria decision making, McGraw-Hill, New York, 1982.
