---
otero_id: 18816
otero_key: "T7CVQN8M"
title: "Organizational hurdles to distributed database management systems (DDBMS) adoption"
authors: "Steven R Gordon; Judith R Gordon"
year: "1992"
journal: "Information & Management"
doi: "10.1016/0378-7206(92)90029-f"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# Organizational hurdles to distributed database management systems (DDBMS) adoption \*

Steven R. Gordon

Babson College, Babson Park, MA, USA

Judith R. Gordon

Boston College, Chestnut Hill, MA, USA

Organizations adopt new technologies, ultimately, to enhance their competitive position and profitability. A distributed database management system (DDBMS) is an example of a technology that may enhance a company's profitability but is also likely to change the way it does business. Specifically, DDBMS adoption may disturb the locus of power, alter the organizational structure, and change the culture of a company. This exploratory study examines the organizational factors that influence the likelihood of DDBMS adoption. It identifies organizational hurdles to adoption, offers an agenda for research validation, and proposes strategies for overcoming the identified hurdles.

Keywords: Distributed database management systems, Organizational structure and culture, Adoption of new technology.

![](/api/attachments/T7CVQN8M/fulltext/images/08dbba40ecd564f5be7c5b01b3f7f861aa6ffb6fe4031a9dcf8e501215b43d00.jpg)

Steven R. Gordon is Assistant Professor of Information Systems at Babson College. He received his B.S., M.S., and Ph.D. from the Massachusetts Institute of Technology. Prior to joining Babson he founded the consulting and software development firm of Beta Principles, Inc., where he remains president. Dr. Gordon's research interests include data structures, DBMS internals and applications, particularly as regards distributed DBMS, international issues in IS, senior management's perspectives on IS, and techniques for teaching about computers.

## Introduction

Distributed database management systems (DDBMSs) are an evolutionary outgrowth of database management systems (DBMSs), a technology at the very heart of most companies' information processing. The difference between the two systems is that a DDBMS allows users and computer programs to access a database that is divided into parts (which may be distributed and/or duplicated among a set of connected computers) as if the data were at a single site. The Business Research Group [5] recently predicted that distributed databases will constitute a multibillion dollar market by 1993. We have investigated the progress being made by organizations in this direction. Technological issues addressing the reliability and feasibility of DDBMS adoption are central to their eventual implementation; the cost of DDBMS software and of the hardware and communication facilities required for DDBMS is also a critical issue, but the technical and cost issues are not the only ones that affect DDBMS adoption. In this study we examine the organizational factors that accompany the technical and cost issues and that could facilitate

![](/api/attachments/T7CVQN8M/fulltext/images/d3d8fd9b2ef45f640ccea8bb6b670d76a18a49ce918628d277d9f2cfb272b50c.jpg)  
and the midlife issues of professional women.

\* The authors thank Dr. Jerome Kanter and Dr. Ed Cale of Babson College for their comments on earlier drafts of this paper. We also wish to acknowledge the financial support of the Babson Center for Information Management Studies.

or impede an organization's progress in adopting new technology. The results of this study are intended to alert organizations and software vendors to possible impediments to successful DDBMS adoption, so that early remedies can be sought.

The definition of DDBMS above, however, describes an ideal that is currently infeasible. Most DDBMS vendors impose some restrictions on the way that data may be divided and distributed, and none claims the ability to hide the distribution of data fully from users and programs. For example, many DDBMS products will not allow data to be updated at remote sites. Nevertheless, progress toward the ideal has been rapid, and the features provided by today's products make distribution and collection of data relatively easy. Most vendors differentiate between DDBMS and networked DBMS products. Networked DBMS products following a client/server architecture distribute their database processing but are not called DDBMS in our terms unless they allow the data to be distributed as well.

Prior to DDBMS, since it was difficult to gather disbursed data, most companies maintained a single, central data repository kept under tight control by information systems (IS) managers. Those that followed a less centralized approach, allowing local managers to keep their own data bases, needed to develop specialized programs whenever it was necessary to combine data for management decision making or operational needs. The institution of distributed systems increases the accessibility of either centralized or decentralized data and decreases the power of those who previously claimed “ownership” of the data.

The adoption of any new technology inevitably stresses an organization. Even if the technology simply reduces costs, its introduction has consequences for budgets and personnel, forcing organizations to cope with change. DDBMS technology also alters the flow of information, the location of data, and the locus of power that flows from control of data. As a result, it is more likely that changes in technology conflict with forces seeking to maintain the status quo.

The widespread introduction of personal computers into organizations in the 1980s had significant organizational consequences. These included shifting the locus of decision making, changing the balance of power, and introducing new control strategies in organizations. Since then, the change in organizations has been incremental rather than abrupt. But the introduction of DDBMS has the possibility of dramatically altering these aspects of the organization once more – and the impact may be equally significant.

Although some companies might avoid adopting DDBMS for technical reasons, and some claim that DDBMS do not help them accomplish their business objectives, in this study we are interested solely in the organizational factors that influence the adoption decision. Accordingly, we spoke with a sample of information systems executives at large, multi-site companies – those who have the most to gain (or lose) from adopting DDBMS. Our objective was to learn as much as possible about the organization, including its culture, structure, and management, whether and how the decision about DDBMS adoption was or is being made, and how organizational factors are affecting the adoption decision. In this paper we address three questions: (1) What organizational factors influence the likelihood of DDBMS adoption? (2) How can these factors be further validated? (3) How can the identified organizational hurdles be overcome to facilitate DDBMS adoption?

## The adoption of new technologies

What characteristics of an organization contribute to its propensity to adopt new technology? Research has shown that culture and structure are among the most important. In addition, the attitude of corporate leaders, particularly the chief executive officer or president, is key.

Culture is a set of beliefs, basic assumptions, key values, and understandings shared by most members of an organization about how people should behave at work and what tasks and goals are important $[3,30,32]$ . Well-defined cultures act to reduce uncertainty because employees know what is important to their associates, can predict how they will respond to change, and can more easily achieve consensus $[24]$ . But this does not necessarily lead to innovation for two reasons $[21]$ . First, by reinforcing existing beliefs, culture can blind management to the need for change. Second, even when the need for change is recognized, managers may view their options within the context of the existing culture, inhibiting them from adopting true innovation.

Adoption is less likely in cultures that are more bureaucratic and relatively stable than in those geared toward competing $[14]$ . Also, the cultural attitude toward technology in general and information systems in particular is likely to affect adoption. Resistance to change in organizations (conservatism) also has significant consequences for the successful adoption of new technologies $[9]$ .

Addressing the relationship between organizational structure and technology adoption, Gattiker [14] has shown that the U form or, unitary organizational structure, is slower to adopt new technology than the M form, or multidivisional organizational structure. Correspondingly, adoption of new technology is slower the more hierarchical the organization, the more clearly defined its jobs, and the more centralized decision making, because of the absence of lateral communication [7].

Lind, Zmud and Fischer [20] have stated that the adoption of microcomputer technology depends positively on both organization size and structure. In the context of their study, structure refers to “linking mechanisms that facilitate lateral relations among an organization’s units.” It was operationalized by counting links (such as newsletters, user questionnaires, information centers, steering committees, and task forces). The authors express their belief that size affects adoption by giving the organization more slack and a greater diversity of potential applications, but this too may be a manifestation of structure.

Finally, top management's commitment to any change has been shown to be critical to its success [4,16,31]. If the chief executive officer becomes personally committed to a particular change, then the corporate management team usually follows, and the change becomes easier to implement throughout the organization. Not surprisingly, then, we would expect that such commitment greatly influences the adoption of new technology – a major change in an organization.

Adoption of a new technology is a complex process. Rogers [28] describes it as involving five steps: (1) acquisition of knowledge about the technology; (2) persuasion of relevant parties to adopt it; (3) decision about the adoption; (4) implementation of the new technology; and (5)

confirmation of its appropriateness and institutional longevity. Because of the relative novelty of DDBMS, the companies we spoke to are currently in one of the first three stages – few decisions about the ultimate adoption of DDBMS had firmly been made. This represents an ideal setting for our research because we could examine the decision process in current and prospective modes rather than in a retrospective mode. This increases the likelihood of observing conflicts before institutional memory is clouded by acceptance of the ultimate decision.

## The adoption of information technologies

The impact of the computer and other information technologies on management and organizations has been an active area of research and conjecture since computers became an important business tool. As early as 1958, Leavitt and Whistler [18] proposed that computers would reverse the trend of decentralization of management functions, which they viewed as caused by management's inability to process and organize increasingly large and complex sets of information. Dearden [11] countered that there should be little impact on division control even though data processing and logistics systems might become more centralized; decentralization, where necessary, was not due to lack of information but rather to management's inability to become expert in a sufficiently broad realm (i.e., management's inability to use information) and to the fixed time available for managers to make a limited number of decisions.

Numerous studies before and since [e.g., 2,8,13,17,25,27] have chronicled researchers' thinking about the impact of computer systems on organizations. However, the effects of organizational characteristics on the adoption of information systems has received relatively scant attention [10]. Yet, if information systems change organizations, it is reasonable to assume that the organization's readiness for change in terms of the fit between the organization's changes and its structure and culture will be important in an organization's decision about when and how to adopt the new technology [19]. Failure to account for these factors will lead ultimately to failure of implementation [22].

Leifer [19] contends that the “successful implementation of [computer-based information systems] architectures requires that system users match the style and process by which jobs in the organization are performed.” He develops a taxonomy in which the organizational context is a modified version of Mintzberg’s [23] organizational structure typology and the information systems architecture is similar to Burch’s [6] typology of information systems network topologies. Within this framework, he hypothesizes that systems such as DDBMS, which he would classify as decentralized systems, fit best with two types of companies: (1) the adhocracy, which calls for a flexible structure that uses a variety of ad hoc or temporary liaison devices to encourage mutual adjustment among members and a rapid response to changing environmental conditions, and (2) divisionalized companies that create units by market or product but also have a strong culture that tightly couples the divisions to corporate management. He believes that more centralized systems, including those where dumb terminals are linked to a mainframe or smart terminals are linked to a central host, are required for three types of companies: (1) machine bureaucracies; (2) professional bureaucracies; and (3) divisionalized companies having a weak culture and autonomy among its divisions. He believes that standalone systems are best for simple structures found in small, young organizations. These hypotheses are based on theoretical arguments rather than on a study of adoption.

Others believe that adoption of new information systems structures is more affected by economics than organizational structure. Clearly, the economics of the microcomputer has affected the way companies process information. The increasing popularity, capability, and economic attractiveness of networking has further moved processing power away from the central information systems (IS) divisions toward the end user. Dearden [12] has predicted the withering away of the IS division of most companies with the dispersion of its function to end users. Nevertheless, dispersion of the IS function is not easy, and mainframes have not disappeared, even among companies showing the highest rate of dispersion [26]. Possibly, the new economics are simply making distributed systems more feasible when they fit with the organization's structure.

## Are companies adopting DDBMS?

At the time of our interviews, Oracle, Ingres, and Sybase were the leading vendors of DDBMS products. While their products ran on a wide variety of platforms, including IBM mainframes, they were well known only among VAX and UNIX-workstation users. IBM had recently announced distributed capabilities for DB2, but these capabilities did not match those of the leading DDBMS vendors, and they did not extend to the popular IBM mini-computer Systems 36, 38, or AS400.

Since this was an exploratory study designed to identify the key obstacles and facilitators to DDBMS adoption, we used a qualitative research methodology, namely the interview format. We interviewed either the most senior information systems executive or the person who might be responsible for the decision to adopt DDBMS in nine companies, selected according to the following criteria: (1) size – companies with at least \$1.0 billion in sales or the equivalent were deemed to have a strong potential to use DDBMS, specifically a need to collect information at multiple sites and the ability to use it; (2) diversification – for an exploratory study, a diverse set of industries is necessary to maximize the likelihood of identifying significant organizational factors relevant to DDBMS adoption; (3) lack of bias – DBMS and hardware vendors (e.g., DEC and Wang) are likely to be biased towards the their own products for internal applications, and thus are not representative; and (4) location – for practical reasons, headquarter location was restricted to New England. Table 1 provides properties of the interview subjects.

Table 1  
Description of interview subjects

<table><tr><td>Company</td><td>Industry group</td><td>Title of interviewee</td></tr><tr><td>A</td><td>Financial Services</td><td>Director of Technology and Data Architecture</td></tr><tr><td>B</td><td>Financial Services</td><td>Director of Database Administration</td></tr><tr><td>C</td><td>Financial Services</td><td>Director of Information Systems Development and Maintenance</td></tr><tr><td>D</td><td>Industrial Products</td><td>General Manager of Information Systems</td></tr><tr><td>E</td><td>Consumer Goods</td><td>Director of Systems Planning and Research</td></tr><tr><td>F</td><td>Consumer Goods</td><td>Senior Director of MIS</td></tr><tr><td>G</td><td>Consumer Services</td><td>Vice President of MIS</td></tr><tr><td>H</td><td>Utility</td><td>Manager of Computer Planning for Information Systems</td></tr><tr><td>I</td><td>Retail</td><td>Manager of Database Support Group</td></tr></table>

We used a semi-structured interview format (see Appendix A for the interview protocol); this allowed us to focus the interview on the major organizational issues for each company. Each interview began with questions about the scope and organization of the MIS function; this typically led to additional discussion about the structure and organization of the company. We next asked about the company's current use of or plans for using DDBMS. The interview concluded with questions about organizational factors such as culture, power, and organization structure. All respondents were assured confidentiality for themselves and their company. The interviews lasted from one to two hours, and our impression was that the interviewees were candid in their comments on their organization and its adoption of DDBMS. Although the comments reflected only a single person's perspective, they also reflected the opinions of individuals who would be the likely champions for DDBMS in their organization.

## Plans for Adoption

None of the companies we studied employs DDBMS for any application, even for experimental purposes. Given the industry publicity about the value of DDBMS and the widespread adoption of new computer technologies by American corporations, we were surprised that no company in our sample had adopted it. Of course, the small size of our sample may have caused us to miss companies using DDBMS. Our interviews did indicate, however, that several companies would probably adopt it within the next few years, suggesting that they view it as a feasible option. The likelihood of adoption by other companies was lower; it ranged from possible to unlikely.

Companies were thereafter classified as (1) unlikely, (2) possible, or (3) likely to adopt DDBMS based on their comments during the interview, as shown in Figure 1. The two authors independently placed each company into one of the three categories based on an analysis of the interview data; they concurred in all cases.

Those organizations that are unlikely to introduce DDBMS typically have highly centralized, mainframe processing with a common platform. In addition, they perceive no need for simultaneous updating of data or for real-time consolidation. They did not believe that DDBMS would help them accomplish their business objectives.

Companies classified as possible to adopt DDBMS currently had no distributed applications in place. However, they did not rule out adopting DDBMS because of existing hardware or software configurations. Two of the companies classified in this category had decentralized MIS, but relatively new top management – in one case, the corporate CEO, and in the other, the VP of MIS – who wished to coordinate and centralize information processing.

Companies classified as likely to adopt described specific applications that would most appropriately be served with DDBMS technology. These companies also felt that their employees needed DDBMS technology to obtain and integrate information from various sources and thus to improve decision making. Furthermore, the companies most likely to adopt DDBMS already used some types of distributed applications, although they had not implemented DDBMS software; various business units or user groups had “home-grown” applications and solutions that were supported either locally or by the MIS department. These companies attributed the absence of DDBMS in their organization to its newness and the untested quality of the technology. Although our interviewees tended to see their companies near the forefront of technology adoption in their industry, they preferred to wait until the technology had been better tested, typically by a competitor. In this way they could evaluate the DDBMS more carefully and ensure its reliability.

<table><tr><td>Unlikely</td><td>Possible</td><td>Likely</td></tr><tr><td>Consumer Goods (F)</td><td>Financial Services (C)</td><td>Financial Services (A)</td></tr><tr><td>Consumer Services (G)</td><td>Industrial Products (D)</td><td>Financial Services (B)</td></tr><tr><td>Retail (I)</td><td>Consumer Goods (E)</td><td>Utility (H)</td></tr></table>

Fig. 1. Likelihood of adoption.

In the rest of this section we look at three of the companies in our sample, one from each category, in more detail.

An unlikely adopter: The case of a consumer services company

Our conversation with the Vice President of MIS suggested that this company was unlikely to adopt DDBMS in the near future. We focused on one division that has five regional offices, five or six divisional offices in each region, and more than 300 outlets across the country. Other than end-user PCs, the only computing equipment is at the home office. Regional managers connect to the corporate computer with dumb terminals; a few have PCs which they also use as dumb terminals. Division managers have no computers. Each outlet tabulates its sales information locally. After midnight the main office uploads all sales information and, once a week, deals with payroll.

Management of this company does not believe that their business requires the use of a DDBMS. As distributors, they see no business reason to put DDBMS into regional or district offices. Top management's style is very centralized and entrepreneurial, with power residing solely in the president. In addition, technology is not part of the organizational culture. Top management wants field managers to adopt a hands-on approach, taking care of their divisions rather than analyzing data. Top management is averse to increasing technology: the president has stated that “there are too many G.D. computers in this company.”

A possible adopter: The case of a consumer goods manufacturer

Our interview with the Director of System Planning and Research suggested that adoption of DDBMS was possible, although not likely at present. He noted that the company is always experimenting with new technologies and new concepts. Since the Vice President of Corporate MIS had only been with the company for nine months, the function was changing.

The company is decentralized with autonomous business units and facilities in thirty to fifty countries. MIS is also fairly decentralized, but corporate MIS serves in an oversight function. The major business units have acted independently in providing their own information technology (IT). The company has not purchased any DDBMS products and has no active plans for introducing them, although there has been some limited discussion about them. The new vice president, however, is looking at coordinating and centralizing some information systems functions to reduce costs.

The corporate culture emphasizes decentralized decision making and functioning. At some business unit level, people are running their own business, though the locus of decision making has shifted over the last few years. Individual countries or small groups of countries in Europe have similar applications. The United States divisions run shared IDMS data bases. While there is some belief that corporate financial consolidation would be advantageous, the corporate culture is against it. Rather than introducing DDBMS, a much more practical model is Electronic Data Interchange. The Director of Systems Planning and Research expressed the need for a level of commonality and definition, but no need for immediate or concurrent data update capability. This manager also did not feel that the business called for DDBMS; perhaps, he noted, if the technology eventually works easily, they might find applications for it.

A likely adopter: The case of the financial services organization

This company is the most likely of those we interviewed to adopt DDBMS. The organization is a holding company with several separate companies as subsidiaries. Up to three years ago, the information systems organization was centralized as one of those companies. However, since then each individual business unit has had its own MIS staff, although three small companies – operations and technical support, telecommunications, and a software development company – still centralize some MIS functions. We interviewed the Director of Database Administration.

The organization has extensive experience with distributed systems, but not with real DDBMS since their systems are not managed by central software and lack location independence. They have many distributed applications: programmers can request prepackaged views of data from different computers in the company. They have made progress toward transparency of location in these applications, but still lack a distributed database as the foundation of their information technology.

The organization introduced distributed applications for several reasons. First, it is better economically to have them reside on midsize computers or LANS than on mainframes. Second, it is easier to develop them locally. Third, the organization has traditionally valued local control of applications. The MIS group was distributed, for example, because the business units found it very difficult to deal with a totally centralized MIS function. Even though some data reside on the mainframe, and some reside locally, a good exchange mechanism does not yet exist. The move has been driven by the business units and they will probably drive a move to DDBMS. The company is very market-oriented and distributing the information allows units to acquire the information they uniquely need. In addition, planning is very difficult, as it supports the local rather than corporate development of systems. Of course, this may also ultimately hinder the introduction of DDBMS.

Internally, the company has experienced competition between business units; while they previously competed for the same customers, now they try to present a coherent public face. This supports the sharing of information offered by a DDBMS. For a new technology to be introduced, one of the business units must champion it. To date, no one has championed DDBMS, although corporate MIS believes that if the technology were sufficiently developed, there would be a cautious move to it. At the same time, however, they are not clear about how they would use the technology, since they cannot properly control data that reside in a single data center, and DDBMS would call for control of data spread across the world. Still, the organization “says they want it, need it, but haven’t been able to articulate what we mean by it or what we would use it for.” Although they are currently experimenting with some implementations of DDBMS, they do not yet understand (from a business sense) what they would do with data distributed across nodes.

## Organizational influences on DDBMS adoption

What organizational factors differentiate these three organizations? What factors help explain the differences in attitudes toward the adoption of DDBMS? Our analysis focuses on three areas: (1) organization culture, (2) organization structure, and (3) top management's attitude toward the new technology.

## Organizational culture

The culture of the organization can be reflected in several dimensions, including its structure, which is discussed in the next section. Given the nature of DDBMS, we are particularly interested in its fit with the nature of decision making and with power and control in the organization.

<table><tr><td>Unlikely</td><td>Possible</td><td>Likely</td></tr><tr><td>MIS Driven (F)</td><td>Top Management Driven (C)</td><td>User Driven (A)</td></tr><tr><td>MIS Driven (G)</td><td>MIS Driven (D)</td><td>User Driven (B)</td></tr><tr><td>MIS Driven (I)</td><td>MIS Driven (E)</td><td>User Driven (H)</td></tr></table>

Fig. 2. Selection of information technology and likelihood of adoption.

Although decision making can be characterized in a variety of ways $[15]$ , we were primarily interested in how much it was centralized or decentralized, since DDBMS affects the location and processing of data. One indicator of centralization of decision making is the extent to which users (as opposed to top management) were involved in the adoption of new IT. As shown in Figure 2, companies unlikely to adopt and those that might possibly adopt DDBMS were MIS driven (and in one case top management driven) in their selection of IT; those companies likely to adopt DDBMS were user driven in selecting their IT. Although all the individuals we interviewed acknowledged that selection of IT was based on business needs, in those companies most likely to adopt DDBMS technology, the push for additional information came from the business units. In these companies, users lobbied for additional information and championed the introduction of new technology. In one large financial institution likely to adopt DDBMS, the person we interviewed felt that “distributing mainframe data down to the analyst is most important... The problem is that the data is now on networks of PCs or in individual computers.” She looked to the potential of DDBMS to “transparently distribute the data across platforms.” Although she stated that there is no “long-term player” in the market that now offers such a product, her company will use one when it becomes available.

The selection of new information technology was also related to the extent to which decision making was centralized. As shown in Figure 3, two of the companies least likely to adopt the new technology have strongly centralized decision making; both companies were lead by strong owner-founders, who wanted to retain control of information at the top of the organization, rather than allowing it to flow down through the organization. In one of these organizations, the culture is summarized in the statement: “the manager should be out managing, not playing with PCs.” The third company unlikely to adopt DDBMS was a relatively new corporation: major business decisions were made by corporate and divisional management and decision making was centralized. In these centralized and highly centralized organizations, DDBMS did not seem to be viewed as beneficial, probably because DDBMS could be seen as threatening the central power base by encouraging the eventual growth and independence of remote data sites.

In contrast, decision making among the companies most likely to adopt DDBMS tended to be more decentralized. These companies focused on providing users the information they needed to do business. Each was market-driven. Autonomous business units were encouraged and supported in building independent applications. Two of these companies, however, were feeling the need for integration and control of information. This tug between centralization and decentralization seemed to provide the backdrop for the potential adoption of DDBMS. In such decentralized organizations, DDBMS increases the ability of users to access information, no matter where it is stored, thereby retaining power among the local users while simultaneously empowering central users who might wish to collect information for comparison and control. As a hybrid, it may threaten individual sites and run counter to decentralized decision making, since the need for sharing and consolidation among independent divisions is increasing. DDBMS, however, can be seen as a tool for improving data communication, and thus can eliminate one of the greatest drawbacks of decentralization.

The issues of control and power are central to the adoption of DDBMS. Often reflected in the nature of decision making, as well as in the structure of the organization, the likelihood of adopting DDBMS seems tied to a willingness to relinquish some power and authority. Interestingly, such loss of power can be required from either top management or lower level workers, depending on the extent to which the DDBMS will increase centralization or decentralization of data processing. In the companies we examined, adoption of DDBMS was more associated with the ability of top management to recapture some of its power previously delegated to lower-level managers. In one of the companies that might adopt DDBMS, for example, the major resistance to adoption seems to be the unwillingness of local sites to relinquish power and control over information. However, this same company has a new CEO who wishes to centralize more decision making and reduce some of the autonomy of the various units. Ultimately, once the power struggle is resolved, the likelihood of adopting DDBMS may increase.

<table><tr><td>Highly Unlikely</td><td>Possible</td><td>Highly Likely</td></tr><tr><td>Strongly Centralized (F)</td><td>Decentralized (C)</td><td>Decentralized (A)</td></tr><tr><td>Centralized (G)</td><td>Decentralized (D)</td><td>Decentralized (B)</td></tr><tr><td>Centralized (I)</td><td>Decentralized (E)</td><td>Decentralized (H)</td></tr></table>

Fig. 3. Decision making and likelihood of adoption.

## Organization structure

Because of their large size, each of the organizations has either multiple locations, divisions, or subsidiaries. According to Leifer's hypotheses, each parent company but one (industrial products) is a candidate for DDBMS because it is divisionalized with market or product-based units. The appropriateness of DDBMS for individual divisions may vary with their structure (which may be the same or different from the corporate structure). Two additional structural issues seem to affect the expectation of DDBMS adoption: (1) the location of the MIS staff and (2) the nature of the corporate infrastructure.

First, the location of MIS varied. Looking again at the three adoption categories, we see differences in the nature of the MIS organization (see

Figure 4). We note that companies that are unlikely to adopt DDBMS tend to have a centralized MIS organization. Then, MIS often operated as a “bought” service, maintained directly through transfer payments or (indirectly) as part of company overhead. When possible, MIS used much of the same software for each operating entity, even consolidating some common data, such as customer lists. Usually a single mainframe was used as the repository for all company data. Satellite or direct-line communication links were used to process incoming data from remote locations at the central mainframe. MIS groups that operated centrally were very pessimistic about the possibility of DDBMS being able to meet their need for data integrity, database recovery after system failures, and network reliability.

In companies where DDBMS adoption is either possible or likely, organizations are more likely to have a decentralized MIS function or to have tried to provide one recently. For example, in two of the organizations most likely to adopt DDBMS, each business unit has its own MIS unit. Even in the organization where a previously decentralized MIS had recently been centralized after the hiring of a new corporate vice president for information systems, some processes are still distributed and supported by local staff at remote locations. A number of the decentralized groups were evaluating or planning to evaluate DDBMS technology for transaction processing.

As the likelihood of adoption increases, it is more likely that an infrastructure exists to support the combination of centralized-decentralized processing that characterizes DDBMS. This type of infrastructure may consist of IS people at remote locations or a totally decentralized MIS department. For example, in one company unlikely to adopt DDBMS, no expert support staff is placed at remote locations; they are currently on-line, with remote switching and support from corporate MIS. In one of the companies that may adopt DDBMS, the MIS function is decentralized, with approximately twice the staff outside corporate MIS as inside it. Among the companies most likely to adopt DDBMS, the infrastructure to support DDBMS exists. Either they already have distributed systems, are currently planning the integration of diverse sites already staffed by MIS professionals, or have dealt with distributed data but have had to exert control from central MIS by directive of top management.

<table><tr><td>Unlikely</td><td>Possible</td><td>Likely</td></tr><tr><td>Centralized (F)</td><td>Centralized (C)</td><td>Newly Centralized (A)</td></tr><tr><td>Centralized (G)</td><td>Decentralized (D)</td><td>Decentralized (B)</td></tr><tr><td>Centralized (I)</td><td>Decentralized (E)</td><td>Decentralized (H)</td></tr></table>

Fig. 4. MIS structure and likelihood of adoption.

## Top management's attitude toward technology

The literature on overcoming resistance to change indicates that the support of top management is critical. As shown in Figure 5, when adoption is considered likely or even possible, the attitude of top management toward new technology is in general more favorable. Those companies least likely to adopt DDBMS have top managers who do not advocate the introduction of new technology. The case of the consumer services provider is a prime example. Because top management opposed computing and ad hoc data analysis by local managers, acquisition of a personal computer was almost impossible. An advanced technology such as DDBMS had no place within the company.

The companies shown as having a top management ambivalent to new technology are dependent on transaction-processing, operations-oriented systems. Although they are not generally averse to new technology, they are extremely cautious about adopting any new systems that might compromise their existing mode of operation. In this environment, the need for DDBMS is tempered by conservatism and fear of change. Both organizations might consider DDBMS for operational reasons, though they have not yet seen the need.

In companies more likely to adopt DDBMS, top management tended to be more favorable toward the introduction of new technology. In one of the financial services companies considered a possible adopter, the president thinks that there are economic reasons to distribute product information to independent sales agents. However, neither top management nor MIS has yet quantified the extent of this need nor are they sure who would pay for the development and maintenance of the shared databases. Thus, the technological capabilities of DDBMS and the desirability of change have both been recognized, but political and economic considerations have delayed implementation.

## Validating the hurdles to DDBMS adoption

What can those who see the value in DDBMS do to plan for their introduction? What are the hurdles they must overcome to encourage and ultimately ensure DDBMS adoption?

In this study we have begun to identify potential factors that must be acknowledged and addressed. The first step towards an increase in DDBMS adoption, and perhaps improved effectiveness after adoption, is more extensive research on the correlation between specific organizational characteristics and DDBMS adoption. Based on our qualitative research findings, we propose that studies should test the following hypotheses:

1. Organizations whose users are driving the selection of information technology are more likely to adopt DDBMS.

<table><tr><td>Unlikely</td><td>Possible</td><td>Likely</td></tr><tr><td>Ambivalent (F)</td><td>Supportive (C)</td><td>Supportive (A)</td></tr><tr><td>Non-supportive (G)</td><td>Supportive (D)</td><td>Supportive (B)</td></tr><tr><td>Ambivalent (I)</td><td>Supportive (E)</td><td>Supportive (H)</td></tr></table>

Fig. 5. Management's attitude and likelihood of adoption.

2. Organizations with decentralized decision making are more likely to adopt DDBMS.

3. Organizations with a decentralized MIS structure are more likely to adopt DDBMS.

4. Organizations with an infrastructure that supports DDBMS functioning are more likely to adopt DDBMS.

5. Organizations whose top management supports information technology are more likely to adopt DDBMS.

## Strategies for facilitating DDBMS adoption

Champions of DDBMS must overcome the following problems for successful DDBMS implementation: first, the organization whose culture only supports centralized decision making and no user input into software decisions; second, the nonexistent or inadequate infrastructure for support of DDBMS use and absence of decentralized MIS staff support; and third, top management's lack of support for new technology in general and DDBMS in particular.

The solution for each of these is straightforward, but not simple. First, organizations can use one of three strategies to address mismatches between an organizational culture and use of new technology such as DDBMS: (1) an agent for change can ignore the culture; (2) a company can manage around the culture; or (3) the culture can be changed to fit the strategy of adopting new technology [29]. While ignoring the culture may have worked for microcomputer introduction in some companies, it requires a strong agent for change in a senior position within the IS department to make DDBMS succeed. A DDBMS is not a personal product, and it cannot be implemented without alliances among data users throughout the organization. Managing around the culture can involve highlighting ways the new technology supports the existing culture, such as how it facilitates and legitimizes current decision-making processes. It can also supplement and improve current work processes, showing its value through increased individual and organizational effectiveness. Still, compatibility with existing values and norms should be assessed; where misfits exist, review of the adoption decision may be appropriate. Changing the organizational culture is not easy. In the cases of the entrepreneur-ori ented organizations, the ultimate growth and development of the organizations may result in shifts in the culture. Until they occur, increasing the autonomy of units in decision making and empowering large groups of employees is a major hurdle to overcome. Also, the philosophy of senior management toward power and control must be changed.

Second, introducing an infrastructure to support DDBMS use requires a clear willingness to both centralize and decentralize MIS control and influence. Spreading resources throughout the organization to provide local support is a prerequisite; then a smaller corporate MIS can facilitate the centralization facility of DDBMS.

Finally, top management must be educated about the value of introducing new technology. For example, one MIS executive noted that his CEO saw technology as a competitive advantage. In the companies least likely to adopt DDBMS, changing the attitude of senior management through education is essential.

Although the adoption of PCs in industry provides a model for successful technology adoption, we cannot necessarily expect the adoption of DDBMS to follow a similar pattern. One significant difference is the incremental investment cost. PC investment can, at least initially, be on a very small scale and for individual users. DDBMS requires a major commitment of financial and human resources. In the early stages of technology adoption, the motivation to adopt typically derives from potential users who are intimately familiar with their application and with the possible ways of addressing it $[1]$ . With PCs, the early users often become internal advocates for wider adoption within the organization. This pattern is inapplicable to DDBMS. Instead, if pressure is to come from end users, there will need to be more consensus building: resulting changes will have company-wide impact.

The adoption of new technologies is also likely to affect the distribution of power within the organization. Certainly the widespread introduction of PCs spread information and resulted in greater equalization of power. Concerns about such effects may facilitate or hinder the adoption of a new technology.

If DDBMS is to become a multibillion dollar industry in 1993, significant changes may need to be made in the organizations. A culture, structure, and top management that support the introduction of DDBMS is essential.

## Appendix A

## Interview protocol

Background of the MIS Function:

1. How is the MIS function organized? Will you provide an organizational chart?

2. How many people report directly or indirectly to the MIS director?

3. Are there other employees who primarily have MIS roles?

4. How large is the MIS budget? What percentage of organizational expenses does it comprise? What is included in the budget?

Use of and Plans for DDBMS:

1. For what applications do you use DBMS?

2. For what applications do you use DDBMS?

3. For what additional applications would you like to use DBMS or DDBMS?

4. Which of these applications would be more appropriate to DDBMS?

5. Do you have any plans to convert any of your existing applications to DDBMS? Which ones?

6. Do you have any plans for any new applications in DDBMS?

7. How does introduction of DDBMS differ from (or is the same as) the introduction of other new technologies?

Organizational Factors that Affect DDBMS Use:

1. What factors do you think have affected the use of DDBMSs in your organization?

2. How would you describe the culture of your organization? What effects does it have on DDBMS use?

3. How would you describe the formal structure of your organization? What effects does it have on DDBMS use?

4. What types of links exist between different departments (e.g. hierarchy, plans, integrating manager, project team, matrix)? What relationship do these links have to DDBMS use?

5. How are decisions made in your organization? What effects does this approach have on DDBMS use?

6. How willing is your top management to taking risks? What effect does this have on DDBMS use?

7. What individuals and which departments have the most power in your organization? What are the sources of this power? How does this power relate to the use of DDBMS in your organization?

8. What are top management's, middle management's, and other employees' attitudes toward adding new technologies?

9. How would you describe the environment faced by your organization? What effect does it have on the use of DDBMS?

## References

[1] Abernathy, W.J. and Townsend, P.L. “Technology, Productivity and Process Change”, Technological Forecasting and Social Change, Vol. 7, 1975, pp. 379–396.

[2] Attewell, P. and Rule, J. “Computing and Organizations: What We Know and What We Don’t Know”, Communications of the ACM, Vol. 27, No. 12, December 1984, pp. 1184–1217.

[3] Baker, E.L. “Managing Organizational Culture”, Management Review, Vol. 69, No. 7, July 1980.

[4] Bice, M.O. “CEO Commitment Key to Organizational Change”, Hospitals, Vol. 62, No. 2, January 1990, p. 76.

[5] Burch, J. “Network Topologies: The Ties that Bind Information Systems”, Data Management, Vol. 23, No. 12, December 1985, pp. 34–37.

[6] Burns, R. and Stalker, G.M. The Management of Innovation, Tavistock, London, 1961.

[7] Business Research Group. BRG Information Industry Review, Vol. 3, No. 1, January 1990.

[8] Carter, N.M. “Computerization as a Predominate Technology: Its Influence on the Structure of Newspaper Organizations”, Academy of Management Journal, Vol. 23, No. 2, 1984, pp. 274–270.

[9] Child, J., Ganter, H. and Kieser, A. “Technological Innovation and Organizational Conservatism”, In: Pennings J.M. and Buitentam, A., eds., New Technology as Organizational Innovation, Ballinger, Cambridge, MA, 1987.

[10] Davis, J.G., Dahr, V., King, W.R. and Teng, J. “The Impact of the Organization on the Computer”, Business Forum, Vol. 9, No. 4, Fall 1984, pp. 40–43.

[11] Dearden, J. “Computers: No Impact on Divisional Control”, Harvard Business Review, Vol. 45, January–February, 1967.

[12] Dearden, J. “The Withering away of the IS Organization”, Sloan Management Review, Vol. 28, Summer 1987, pp. 87–91.

[13] Foster L.W. and Flynn D.M., “Management Information Technology: Its Effects on Organizational Form and Function”, MIS Quarterly Vol. 8, No. 4, December 1984, pp. 229–236.

[14] Gattiker, U.E. Technology Management in Organizations, Sage, Newbury Park, CA, 1990.

[15] Huber, G. Managerial Decision Making, Scott, Foresman, Glenview, IL, 1980.

[16] Hunsucker, J.D. and Loos, D. “Transition Management: An Analysis of Strategic Considerations for Effective Implementation”, Engineering Management International, Vol. 5, No. 3, February 1989, pp. 167–178.

[17] P. Keen, “Information Systems and Organizational Change”, Communications of the ACM, Vol. 24, No. 1, January 1981, pp. 24–33.

[18] Leavitt, H.J. and Whistler, T.L. "Management in the 1980's", Harvard Business Review, Vol. 36, November–December 1958, p. 43.

[19] Leifer, R. "Matching Computer-Based Information Systems with Organizational Structures", MIS Quarterly, Vol. 12, No. 1, March 1988, pp. 63–73.

[20] Lind, M.R., Zmud, R.W. and Fischer W.A., “Microcomputer Adoption – The Impact of Organizational Size and Structure”, Information & Management, Vol. 16, 1989, pp. 157–162.

[21] Lorsch, J. Managing Culture: “The Invisible Barrier to Strategic Change”, California Management Review, Vol. 28, 1986.

[22] Miller, J.A. "The Hidden Dimension in Information Systems Technology", Computers in Healthcare, Vol. 8, No. 4 April 1987, pp. 16–18.

[23] Mintzberg, H. The Structuring of Organizations, Prentice-Hall, Englewood Cliffs, NJ, 1979.

[24] Ogilvie, J.R., Pohlen, M.F. and Jones, L.H. "Organiza-

tional Information Processing and Productivity Improvement", National Productivity Review, Summer, 1988, pp. 229–237.

[25] Olsen, M.H. and Lucas, H.C. Jr., “The Impact of Office Automation on the Organization: Some Implications for Research and Practice”, Communications of the ACM, Vol. 25, No. 11, November 1982, pp. 838–847.

[26] Redditt, K.L. and Lodahl, T.M. "Leaving the IS Mothership", CIO Magazine, October 1988, pp. 54–60.

[27] Robey, D. “Computers and Management Structure: Some Empirical Findings Re-examined”, Human Relations, Vol. 30, No. 11, November 1977, pp. 963–976.

[28] Rogers, E.M. Diffusion of Innovation, 3rd edition, Free Press, New York, 1983.

[29] Sankar, Y. “Organizational Culture and New Technologies”, Journal of Systems Management, April 1988, pp. 10–17.

[30] Schein, E.H., Organizational culture and Leadership. Jossey-Bass, San Francisco, CA, 1985.

[31] Schwartz, H. and Davis, S. "Matching Corporate Culture and Business Strategy", Organizational Dynamics, Vol. 10, No. 1, Summer 1981, pp. 30–48.

[32] Smircich, L. "Concepts of Culture and Organizational Analysis", Administrative Science Quarterly, Vol. 28, No. 3, 1983.
