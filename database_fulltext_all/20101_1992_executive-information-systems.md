---
otero_id: 20101
otero_key: "9N2HSGG9"
title: "Executive information systems"
authors: "Ido Millet; Charles H. Mawhinney"
year: "1992"
journal: "Information & Management"
doi: "10.1016/0378-7206(92)90011-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Applications

# Executive information systems A critical perspective

Ido Millet

Bentley College, Waltham, MA 02154-4705, USA

Charles H. Mawhinney

Metropolitan State College of Denver, Denver, CO 80217-3362, USA

The purpose of this paper is to clarify what EIS are, why they are developed, and what should be considered when such systems are proposed. Although EIS can be very valuable, there is a need for a critical perspective and careful review of proposed investments in such systems. Various organizational conditions might lead to a premature development of EIS when the required MIS sub-structure is not yet well formed, and when investment in MIS would be more beneficial. Furthermore, for some situations, the periodic distribution of focused and integrated MIS reports may be better than the online EIS reporting mode.

Keywords: EIS, MIS, DSS, Periodic reporting

![](/api/attachments/9N2HSGG9/fulltext/images/e1450f02da678369ed6f39d6564eed077369c5c345da2d1146dba52bbcc23b89.jpg)

Ido Millet is an Assistant Professor of Computer Information Systems at Bentley College. He received a B.S. in Industrial Engineering and Management from the Technion - Israel Institute of Technology, an M.B.A. from Tel-Aviv University, and a Ph.D. in Information Systems from the Wharton School, University of Pennsylvania. He has 12 years of industrial experience including systems analysis and project management for large-scale information systems, consulting,

and development of PC-based management information systems. He is the author of articles in Systems, Objectives, Solutions, and the European Journal of Operations Research. His research interests include EIS, DSS, MIS, the Analytic Hierarchy Process, and issue management information systems.

## Introduction

It was recently claimed that executive information systems (EIS) have been installed on the desks of senior executives in nearly 25% of the largest U.S. companies [5]. Saks [12] cites a recent study indicating that vendor sales of EIS packages totaled \$22 million in 1987 and are expected to grow tenfold to \$230 million by 1992. However, some sources wonder if the claims made and expectations held for EIS may be exaggerated [15]. The purpose of this paper is to clarify what EIS are, why they are developed, and what should be considered when such systems are proposed.

During 1989, we conducted structured telephone interviews with four executives at four of the major EIS vendor companies. We refer to the interviewees as experts since they averaged eleven years of experience in the EIS arena and were personally familiar with a combined total of 361 EIS cases. Due to the obvious limitation of such a small sample size, we use the results from the interviews only as interesting indications rather than as basic arguments. Also, the numeric results are delegated to the Appendix, and in the

![](/api/attachments/9N2HSGG9/fulltext/images/4bffdc9bc4822174d76c2c88bf18d6661cfc12e9a05355e7de83894604963169.jpg)

of MIS, Information and Management, Journal of CIS, Journal of Research on Computer Education, and Computer Personnel. His research interests include MIS, DSS, EIS, the management of end-user computing, and information systems curriculum.

body of the text we refer to these results only through verbal approximations. The Appendix presents both the interview questions as well as the average responses, weighted by the number of EIS cases known to each expert.

EIS are risky and expensive projects $[17]$ . The experts estimated that almost a quarter of the EIS installations with which they were familiar were failures. This indicates a need for a critical perspective and careful review of proposed investments in EIS.

## Mapping the MIS, DSS, EIS ground

The terms MIS, DSS, and EIS are not uniformly defined, and often are used synonymously $[10]$ . In the following sections we develop operational definitions for these terms to provide a foundation for the discussion in later sections.

## The MIS concept

In a manner consistent with Sprague, we define an MIS to be a system that allows managers at various organizational levels to get detailed and summarized information from operational databases. The operational databases are typically created by “transaction processing systems” (TPS) which have been developed to support business functions. Thus the MIS is a layer on top of the TPS.

TPS are relatively inflexible, and use predominantly internal data sources. This tends to result in MIS whose primary purpose is the internal monitoring of past activities through pre-defined periodic reports or simple queries. TPS are often developed in a piecemeal fashion to support individual functions, resulting in MIS which lack integration. Since MIS serve many managers at all organizational levels, they typically lack the degree of customization and focus required by top executives. Table 1 compares and contrasts the characteristics of MIS with those of DSS and EIS.

## The DSS concept

We define a DSS to be a system which uses models of the relationships between decisions and outcomes to support problem solving. The focus of a DSS is a specific decision problem or a collection of related problems. Sprague and Carlson proposed two types of DSS: (1) data based and (2) model based. In contrast, we would classify the data based group as MIS, and reserve the use of the term DSS to model based systems.

Previous literature emphasizes semi-structured or unstructured decisions as the domain of DSS. This view emphasizes the active role played by the human as the ultimate decision maker. Yet, once a repetitive decision making problem (e.g., maintaining inventory) has been well understood and modeled, the DSS may take over the actual decision making process. Table 1 emphasizes this broadening of the DSS domain by listing two types of DSS. Type I DSS support structured decisions at the clerical level and in many instances automate them. Type II DSS address semi-structured and unstructured problems: they are typically used by staff professionals and middle managers rather than by executives [16].

Table 1  
MIS, EIS, and DSS: A comparison

<table><tr><td></td><td>Primary Purpose</td><td>Primary Users</td><td>Primary Output</td><td>Primary Operations</td><td>Time Orientation</td><td>Example</td></tr><tr><td>MIS</td><td>Internal Monitoring</td><td>All Levels Managers</td><td>Pre-defined Periodic Reports</td><td>Summarize Information</td><td>Past</td><td>Sales Report</td></tr><tr><td>EIS</td><td>Internal and External Monitoring</td><td>Executives</td><td>Pre-defined Customized Presentation</td><td>Integrate, Present, Track CSF</td><td>Past-Present</td><td>Market Share Tracking</td></tr><tr><td>DSS I</td><td>Support Structured Decisions</td><td>Clerical or Automated</td><td>Decisions</td><td>Solve, Model Automate, Suggest</td><td>Present-Future</td><td>EOQ</td></tr><tr><td>DSS II</td><td>Semi/Un-Structured Decisions</td><td>Staff and Managers</td><td>Suggestions, Analytic Reports</td><td>Model, Solve, Suggest, Analyze</td><td>Future-Present</td><td>Pricing Model</td></tr></table>

## The EIS concept

Although early researchers [1] discussed the need for and characteristics of information systems supporting executive decision making, the term EIS was coined by Rockart and Treacy [11]. We define an EIS to be a system that integrates information from internal and external data sources enabling executives to monitor and request information of key importance to them via customized presentation formats. Typically, EIS allow executives to interact directly with the system via a user-friendly interface.

Literature indicates that executives use computers for reporting rather than analysis purposes $[10]$ . This tends to support the view of EIS as a monitoring oriented system. The experts we interviewed indicated that indeed most EIS are used predominantly for monitoring purposes.

EIS provide information focused on indicators or dimensions of interest to the executive. Much of this information is potentially available from the TPS and MIS, but not in a meaningful, integrated, customized, and needs-oriented fashion.

Figure 1 clarifies the relationship between EIS and other subsystems. The EIS is a monitoring system that draws information from MIS data bases and from external data sources for use by executives. We would expect the bulk of the data needs to be met through the underlying MIS. The experts indicated that indeed most of the EIS data is internal. The EIS provides a data base extraction capability, and, in instances where the underlying MIS does not provide integrated access to underlying data files, the EIS also provides the missing integration. Additionally, EIS provides a user-friendly interface and highly customized report formats for effective executive use. While EIS help executives find problems, DSS help managers solve problems:

![](/api/attachments/9N2HSGG9/fulltext/images/69aa7a8f3cdc3232e029acb1bfb157314a52b04e166d55725bf92a0cef0c5813.jpg)  
Fig. 1. The EIS role.

Executive information systems are specifically designed to help executives gain insights and track critical success factors. The focus of an EIS is to aid a decision maker in assimilating information quickly and identifying problems or opportunities, not as an aid in problem analysis or resolution. In many corporations, well-developed EIS have replaced the traditional periodic executive summary reports $[6]$ .

We submit that EIS are in many respects very similar to the MIS concept. As indicated in Table 1, both MIS and EIS are primarily oriented toward monitoring performance, and both make extensive use of pre-defined reports. This is also indicated by the experts who estimated that, in the cases with which they were familiar, the vast majority of EIS functionality could have been delivered via MIS capabilities.

These definitions of MIS, DSS, and EIS do not provide for mutually exclusive domains, but rather focus on key distinguishing features. Actual systems may not always map neatly into this framework, and may exhibit a mixture of two or even three of the pure categories. For example, EIS with many users may take on more of the characteristics of MIS and/or DSS. The experts estimated that installed EIS average 41 users, only a quarter of which are actually executives. Larger systems would naturally reduce the percentage of executive users. One might expect that in these larger EIS cases, the number of users reduces the ability to customize reports and increases the instances of report distribution, thus lending the system an MIS flavor. Furthermore, since staff analysts would typically demand analysis and modeling capabilities, the system may also acquire a DSS flavor. One of the experts mentioned a case where a system that was called an EIS was in reality an MIS/DSS with 2,000 users.

## Limitations of EIS

EIS are subject to several technical and organizational limitations. These, along with the similarity to MIS and dependence on MIS capabilities, serve as the rationale for the proposed critical perspective of EIS.

## Technical limitations

We structure the discussion of EIS technical limitations along the generic system dimensions of input, processing, and output. We aim to show that in the case of EIS, each of these dimensions might suffer from inflexibility and other limitations.

Input related limitations. Since EIS aim to provide executives with their specific information needs, we would expect a substantial portion of the EIS database to be drawn from external data [3]. However, a review of literature reports on EIS implementations seem to suggest that most of the information supplied by EIS is internal. Indeed, as discussed earlier, the experts estimated that only a small portion of the data used by EIS is external. This observation shouldn't surprise us since the same limitations that apply to acquiring external information in a form amenable to MIS processing should apply also to EIS.

Another data related limitation of EIS involves data-source inflexibilities. On the one hand, the EIS imposes inflexibility on information systems that serve as information sources to the EIS. Necessary modifications to operational and managerial information systems might be curbed to ensure the supply of data in the format and content required by the EIS. On the other hand, the data sources impose inflexibility on the EIS, since the EIS set of presentation options is tailored to the available EIS database at the time of development. Therefore, if other data sources are required, an equally elaborate process is required to develop the necessary procedures for extracting, loading and presenting the data. The necessary changes in data might also interact with previous design of the system (e.g. adding quarterly data to a system that is designed on a monthly basis) and demand further re-work and re-training. This type of inflexibility is to a large extent an outcome of the elaborate structure and design behind EIS.

The difficulty to obtain external data and the data inflexibility issues can be viewed as only sub-issues of the general data availability problem. EIS are highly dependent on capabilities of the MIS from which they draw data:

...the technical, physical, and political barriers to providing executives with the data they need can be a major roadblock in the evolution of an EIS. ...An EIS can be a catalyst for rebuilding a firm's data infrastructure, which can be a costly and time-consuming project [10].

Processing related limitations. EIS usage tends to be limited to the MIS mode of pre-specified options for data retrieval, status and exception reporting, and graphical presentations [10]. These systems typically have limited statistical and analytical capabilities. The experts estimated that most of EIS utilization is provided via pre-defined reports.

A recent study [17] found that annual personnel, operating and maintenance costs of EIS (\$117,000) are higher than personnel development costs (\$90,000). While this may indicate a healthy appetite for more EIS options, it might also indicate that the systems lack flexibility and that changes or additions to processing capabilities may require substantial work. For example, if an executive requests financial modeling capabilities, multiple regression functionality, or new types of divisional comparisons, the changes may require substantial skills, time, and resources. Even when changes can be made relatively easily, some executives might resent the need to keep learning new functions and adapting to these changes.

The cost of making changes to the system might increase when the EIS vendor is a major source of expertise in developing and maintaining the EIS. The use of external expertise appears to be fairly extensive. According to the experts, the majority of successful EIS were developed with external help and one third of successful EIS are maintained with external help.

Even if more advanced analysis features were provided by the EIS, executives typically lack the skills, time or inclination to perform data analysis. One may even argue that supplying executives with detailed data without analysis and without recommendations might lead to hasty decisions and to deterioration of decision making quality.

Output related limitations. EIS may suffer from inflexibility and limitations in relation to output presentation and distribution options. Output is limited to those options and formats that were designed into the system. For example, if the system tracks the performance of four sales regions through four graphs on one screen, a restructuring of sales into five regions might require a substantial re-design and re-work effort.

Since EIS make use of on-screen mixed graphics and text color presentations it might be difficult to distribute the output to other managers. This might limit the ability of the executive to share and to discuss the information. While this limitation may be alleviated in organizations with sophisticated communication networks and output devices, it remains a limitation in many of the current business environments.

Due to these limitations, an EIS might actually become a delivery mechanism for standard reports. As Friend [5] indicated, “...many EIS users have not gone beyond the delivery of standard reports to the use of their system to pursue corporate goals and objectives.” Still, as we discuss below, beyond the price and technical considerations, there are also organizational arguments in favor of periodic reporting.

## Organizational liabilities

The technical concerns may be addressed by better EIS development tools, increased availability of external data for sale, better MIS infrastructure, and by improved technical and analytic skills of executives. However, under certain circumstances, the organizational liabilities of EIS may prove to be more profound and more difficult to circumvent. Possible negative organizational impacts of EIS include: (a) detrimental effects on managerial agenda and on managerial time orientation, (b) loss of synchronization in managerial processes, and (c) the generation of oscillatory or destabilizing organizational adjustments.

Biased agendas and time orientation. The introduction of EIS into the executive suite might bias the executive's agenda and time orientation. EIS might focus too much attention on the measurable dimensions of the business (e.g., sales rather than customer satisfaction). Executives might spend too much of their time, as well as the time of their subordinates, on information and issues presented by the EIS. Since the EIS profile of emphasis might differ significantly from the ideal profile of executive attention, the organizational agenda might be biased.

Due to the increased frequency and depth of the information supplied by the EIS, the executive time horizon might be unduly shortened. It may be anticipated that such feedback will increase the executive involvement with short-term, low-level concerns. Most advanced EIS allow the user to “drill-down” through layers of aggregation to get at underlying data and sources of problems. For example, the executive may view sales performance at any level of detail from total sales to sales by individual agents. Such a system may induce the executive to react prematurely to small short-term fluctuations or to request action in relation to small organizational units or even specific individuals. Too much executive involvement with “micro-management” might prove disruptive to staff and line work.

When considering claims that managerial agendas are already biased toward short-run measurable and structured issues, the potential negative effects of EIS seem clear. Beyond the biasing of the organizational agenda and shortening of the time horizon, the pre-defined presentation formats and topics might lead to trivialization of managerial agenda and thought patterns. This may be compared to claimed effects of the television medium on our society. The presentation of a limited repertoire of themes in a preprocessed suggestive mode can reduce active high-level intellectual exploration:

Programmed and immediate tasks tend to be handled before more ambiguous and longer-run matters... The real challenges of managing are so difficult and anxiety-provoking that managers allow their days to be filled with detail and trivia [19].

A more subtle source of agenda and time horizon bias might be found in defensive chain reactions throughout the organization. Since lower echelons in the organization know that certain dimensions of their performance are monitored by the executive via the EIS, they may shift their agenda and shorten their time horizon to improve those dimensions at the expense of others or to the detriment of long-term performance.

This phenomenon might occur at lower management levels, even if the executive agenda and time horizon remain unchanged.

Consider, for example, a case mentioned by Rockart and De Long where a system was developed for the Chairman of a firm to track the response time of departments to his correspondence. The system is credited with reducing the average response time from 15 to less than 5 days. Such “achievement” might have hidden but dire consequences by generating disruptive work patterns throughout the organization.

Loss of managerial synchronization. While ad hoc reporting and query capabilities are a boon to many managerial processes, there are also advantages to periodic reporting. Periodic reporting actually synchronizes management processes into alternating phases of sensing and acting. The periodic and shared review of all performance indicators by all managers allows decisions and actions to be prioritized and orchestrated with a global perspective. This has the added benefit of clearly communicating priorities to subordinates and reducing confusion.

In contrast, the introduction of EIS might disrupt such reporting cycles and cause a loss of synchronization. The executive might neglect to review some of the performance dimensions and might be tempted to react to information in an isolated myopic manner.

The periodic distribution of hard copy reports on key performance indicators to various levels of management has additional benefits. The hard copy format facilitates hand written annotation, distribution, and communication with peers as well as with subordinates. The distribution of the report to various levels of management increases motivation due to increased performance feedback.

The positive effects of periodic paper-based reporting were personally observed by the first author who has developed performance tracking systems for military logistics and for a large commercial bank. The bank system is in its fifth year of operation, and is currently tracking more than 300 key performance indicators on a monthly and quarterly basis, serving five management levels in the organization. Both systems are PC-based and rely almost exclusively on standard paper reports.

In fact, contemporary EIS still make extensive use of periodic reporting. The experts estimated that most of EIS usage was via standard reports, and that most of these standard reports are run periodically. This may be the result of the periodic nature of updates to the information database feeding the EIS. However, further research may indicate that the periodicity is at least partially motivated by the above considerations.

Organizational oscillations and destabilization. The literature shows that managerial systems may demonstrate oscillations or even chaotic behavior under certain conditions of external disturbance and internal feedback and adjustment $[4,8,7]$ . Similar concerns were recently expressed in relation to distributed database technology:

Information feedback that is too rapid and not controlled properly is very destabilizing for a system, causing its behavior to oscillate wildly ...we may inadvertently destabilize large organizations by forcing them to react too quickly to changes [2].

While some organizational oscillations may play a self-regulating role $[7]$ , one must consider the effect that EIS might have on organizational stability. The issue is perhaps not so much the availability of frequent feedback and information to top-executives, but the type and magnitude of adjustments that the executive will generate as a reaction to the information. EIS might destabilize organizations in those cases where executives over-react to the supplied information by imposing too frequent and too strong adjustments.

## Political conditions leading to EIS

We believe that in some cases investments in EIS may be attributed to political rather than normative considerations. These conditions can usually be traced to the relationships between the executive body, middle management, and the MIS department.

## Technological push

The MIS department professionals might be attracted to the EIS concept as an opportunity to learn and experiment with advanced software and hardware technology, expand and secure larger budgets, and gain direct access to top executives. We label these cases as “technology push”. The experts estimated that “technology push” from the MIS department plays a significant role in some EIS investment propositions. Similarly, a recent survey of 50 firms having EIS reports that in 28% of the firms the EIS was initiated by information system personnel [17]. While most of these cases are probably driven by perfectly proper motives, it seems reasonable to assume that the IS staff is not blind to the potential rewards associated with an EIS project.

In some cases the technology push may come from an EIS vendor or a consulting firm willing to develop the EIS or a prototype at a loss in order to gain entry into the organization or the industry. We are aware of at least one case in which an EIS prototype was developed by a consulting company as a free service to a client. The experts estimated that special introductory offers from EIS vendors play a significant role in a quarter of vendor supported EIS applications.

## Closet MIS

Middle management or the MIS department might find that the executive body fails to recognize the need for improvements in MIS capabilities and is not willing to authorize budgets for such activities. By presenting the project as an EIS, the budget may be approved and necessary MIS capabilities (e.g. data and file management, networking, and hardware resources) may be secured in the process of developing the EIS. The experts indicated that this scenario is not a significant motivation for EIS investment propositions.

## Middle management bypassing

The executive body might be frustrated by the lack of integrated and focused reporting across divisional or functional borders. While a good MIS could provide much of the needed information, functional and divisional management may resist the development of these capabilities $[17,18]$ . Such integrated MIS threaten these managers with increased corporate monitoring and control as well as loss of ownership over what used to be “their” data. Since the MIS is important for operational as well as corporate reporting needs, the local managers might block the necessary modifications to the MIS by claiming unacceptable operational consequences.

In such a case the executives might elect to by-pass the current reporting system and the opposition of middle management by requesting an EIS from the MIS department. The creation of the EIS provides the momentum to collect the necessary information while leaving the MIS intact. The experts indicated that this scenario is not a significant motivation for EIS investment propositions.

## Normative conditions for EIS

The discussion above should be balanced with the recognition that EIS have several advantages over MIS and that in many cases EIS should be considered as a viable investment. EIS can deliver highly effective presentations of information that can highlight trends and exceptions and provide fresh insights. While such capabilities can be delivered via MIS, EIS are specialized and dedicated to this domain and are tailored to the needs and tastes of the executive. This can increase the effectiveness and shorten the time spent by the executive in reviewing reports and generating decisions. Indeed, the experts estimated that the vast majority of EIS investments are significantly motivated by the need to provide executives with information in better format and via better interface.

EIS may also serve to integrate, standardize and summarize information that would otherwise be served to the executive in a bewildering variety of reports, formats and conventions. Since commercial EIS packages have good capabilities for extracting information from diverse file structures, an EIS may prove to be a technical solution to necessary integration of information from diverse internal and external data sources. These capabilities can prove especially useful for organizations, such as holding companies, that need to control business units with diverse information systems. The EIS can serve in such cases to mask different information systems, file structures, and conventions by creating a unified reporting system. Even if an MIS can or should serve the same purpose, the political clout of the executives may be required to bring about the necessary standardization and discipline. The experts estimated that the vast majority of EIS investments are significantly motivated by the need to provide executives with integrated, combined, or unified MIS information.

Once the executive is given a first dose of useful information he may progress to higher levels of sophistication in terms of analysis, conceptualization, and consumption of information. An EIS may prove valuable in garnering the executive support and good will towards MIS, DSS and information technology in general. Once an executive becomes a user of one computer system, synergies are created for the adoption of other systems. Executive Support Systems (ESS), as discussed by Rockart and De Long, are geared to take advantage of this synergy by combining EIS with electronic mail and other executive work station services.

EIS may be more beneficial to organizations in a dynamic business environment where top executives need to exercise frequent involvement and monitoring of operations. EIS are also effective at supporting extensive use of backup detail for analysis and decision making. In addition, the cost/benefit ratio and value of EIS improves as the number and sophistication of users increase.

Beyond the support for executive decision making, EIS may be used to project an image of advanced technology and organizational control. Such an image can be valuable in dealing with customers, investors, suppliers, and competitors. Such an image can also be very valuable for internal purposes such as attracting, retaining, and motivating high quality managerial and DP personnel.

## A critical perspective

Notwithstanding the discussion above, EIS motivated by normative reasons may still be non-normative in cases where the necessary MIS substructure is missing. In such situations, the EIS may supply executives with information that might be better supplied via an MIS. Without a well developed MIS, data collection for the EIS may be difficult or impossible. We believe that in some cases an investment in improved MIS capabilities and increased integration and focus in periodic reporting may yield better results. We suspect the lack of MIS infrastructure may even lead to failure of EIS.

If the MIS infrastructure is not well developed, management should consider postponing investment in EIS until the MIS can adequately support the EIS. Premature investments in EIS may produce long lasting bad impressions in the minds of the executives. Perhaps even more significant are the possible dysfunctional effects on the MIS. If the MIS capabilities are adjusted or re-designed after the EIS has been launched, the design choices might be constrained and influenced unduly by the demands exerted by the EIS.

The consideration of investment in MIS as a necessary precursor or as a preferred alternative to investment in EIS can also be supported by the similarity in form and function between the two. In the seemingly common case where the main objective of the EIS is to provide monitoring of organizational performance, periodic MIS reports may provide a better alternative in terms of efficiency, effectiveness, and organizational impact. However, rather than providing the usual garden variety of MIS reports in the push mode, these reports should be customized in content and in format to the needs of the executives.

As discussed earlier, the experts indicated that most of EIS are predominantly monitoring oriented and that almost all of EIS functionality in practice could theoretically have been delivered via MIS capabilities. While the experts estimated that an MIS investment would have been more beneficial than the investment in EIS in only a small fraction of the cases, it does support our claim that the problem exists.

Organizations need to recognize that the request for an EIS is a special moment. Not only does it signal executive dissatisfaction with the information currently being provided, but it also affords the opportunity to consider broader issues. The full value of EIS will be realized only when they help executives focus on strategic issues. As suggested by our preliminary findings, today's EIS generally do not do that. We think an organization should consider two lines of inquiry when a request for EIS surfaces. One approach would be to consider MIS as an alternative, as we have already suggested. The other would be to force consideration of the strategic perspective to see if a more valuable solution could be found. Such a strategic perspective would include flexibility and external data as critical elements in the EIS. This second line of inquiry also offers an opportunity for the MIS executive to build the kind of partnership with the general and functional executives that is needed for realizing the strategic value of the information resource.

## Conclusions and future research

The purpose of this paper was to clarify what EIS are, why they are developed, and what should be considered when such systems are proposed. We have provided a definitional framework for the concepts of MIS, DSS, and EIS which emphasizes the overlap and dependencies between EIS and MIS capabilities. A variety of technical and organizational considerations and relevant estimates from interviews with four EIS vendor experts were used to provide insights into normative and non-normative aspects of EIS investment and utilization.

The emerging critical perspective suggests that since EIS need a good MIS basis, and since both types of systems serve similar objectives, proposed investments in EIS should be reviewed against the explicit alternative of investments in MIS. Management should be aware of non-normative conditions that may lead to premature development of EIS, and the advantages that periodic reporting cycles may provide. In some cases, management should postpone proposed investments in EIS and dedicate resources to building the MIS infrastructure.

This article raises several issues for future research. In particular, the possible organizational liabilities of EIS (biased agendas and time orientation, loss of managerial synchronization, and organizational oscillations and destabilization) seem like an intriguing domain for empirical studies. At this stage, these ideas are speculative in that although other researchers have proposed their existence, the evidence tends to be anecdotal rather than rigorous empirical validation. For example, one could compare the efficacy and side effects of periodic versus ad hoc reporting of key performance indicators in different organizations. A related question is the appropriate mode, periodic versus ad hoc, of various types of information for various organizational contingencies. Future research should also clarify the causes for EIS failure and correlate such failures to the development stage of the MIS and to the initiation scenario of the EIS.

## References

[1] Anthony, R.N., Planning and Control Systems: A Framework for Analysis, Cambridge, MA: Harvard University Graduate School of Business (1965).

[2] Chapnic, Philip, “Editor’s Buffer,” Database, Programming and Design, 2, 4 (April 1989) 7–8.

[3] El Sawy, Omar E., “Personal Information Systems for Strategic Scanning in Turbulent Environments: Can the CEO Go On-Line?” MIS Quarterly (March 1985).

[4] Forrester, J.W., Industrial Dynamics, Cambridge, MA: MIT-Press (1968).

[5] Friend, David, “EIS: Straight to the Point,” Information Strategy: The Executive's Journal 4, 4 (Summer 1988) 25–30.

[6] Martin, James, “DSS applications should shed new light on a problem,” PC Week 6, 17 (May 1, 1989) p. 50.

[7] Rasmussen, Dan Rene and Eric Mosekilde, “Bifurcations and Chaos in a Generic Management Model,” European Journal of Operations Research, 35 (1988) 80–88.

[8] Roberts, E.B., Managerial Applications of System Dynamics, Cambridge, MA: MIT-Press (1978).

[9] Rockart, J.F., “Chief executives define their own data needs,” Harvard Business Review (March–April 1979) 81–93.

[10] Rockart, F. John and David W. De Long, Executive Support Systems, The Emergence of Top Management Computer Use, Homewood, Illinois: Dow Jones-Irwin (1988).

[11] Rockart, J.F. and Treacy Michael E., “The CEO Goes On-Line,” Harvard Business Review (January–February 1982).

[12] Saks, S.. “Decision support tools expected to boom in '90s,” Management Information Systems Week 26 (May 8, 1989) p. 8.

[13] Sprague, R.H. Jr., “A framework for the development of decision support systems,” MIS Quarterly 4 (December 1980), 1–26.

[14] Sprague, R.H. Jr. and Carlson, E.D., Building Effective Decision Support Systems, Englewood Cliffs, NJ: Prentice-Hall (1982).

[15] Tobias, A.J., “Today’s executives in a state of readiness,” Software Magazine 8, 13 (November 1988) 55–60, 62–66.

[16] Watson, J. Hugh, Astrid Lipp, Pamela Z. Jackson, Abdelhafid Dahmani and William B. Fredenberger, "Organizational Support for Decision Support Systems," Journal of Management Information Systems 5, 4 (Spring 1989) 87–109.

[17] Watson, J. Hugh, Kelly R. Rainer Jr., and Chang E. Koh, "Executive Information Systems: A Framework for Development and a Survey of Current Practices," MIS Quarterly (March 1991), 13–30.

[18] Wetherbe, C. James, “Executive Information Requirements: Getting It Right,” MIS Quarterly (March 1991) 51–65.

[19] Webber, Ross A., A Guide to Getting Things Done, New York: Free Press (1980).

## Appendix: Interview questions and response summary

Based on your experience with EIS, please estimate:

○ Avg nr. of users 41, % who are executives: 41%

○ % of usage via predefined reports vs. interactively designed 83% - of standard reports being run periodically: 84%
- % of internal (i.e. MIS) data content: 90%
- % of EISs that are predominantly “monitoring” (vs. modeling): 81%
- % of EIS functionality in practice that could have been delivered via MIS capabilities: 98%
- % of EIS cases where investment in MIS instead would have been more beneficial: 5%
- % of EIS cases that are failures (not used or worse): 23%
- % successful EISs developed w/o external help: 30%
- % successful EISs w/o external maintenance: 64%

Estimate % of EIS significantly motivated by:
○ Technology Push from the DP/MIS group: 17%
○ Executive bypassing poor MIS (via vendor help): 69%
○ Execs by-passing functional/divisional mgrs (via IS): 0%
○ Getting budget for better MIS by disguising it as EIS: 5%
○ Giving execs MIS info with better format/interface: 94%
○ Giving executives external information: 40%
○ Providing integrated/combined/unified MIS info: 90%
○ EIS vendors introductory/prototyping special offers: 26%
○ Other: 0%
