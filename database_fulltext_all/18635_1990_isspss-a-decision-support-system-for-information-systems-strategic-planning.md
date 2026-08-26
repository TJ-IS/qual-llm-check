---
otero_id: 18635
otero_key: "GGKE253K"
title: "ISSPSS: A decision support system for information systems strategic planning"
authors: "Moshe Zviran"
year: "1990"
journal: "Information & Management"
doi: "10.1016/0378-7206(90)90048-m"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Applications

# ISSPSS: A decision support system for information systems strategic planning

Moshe Zviran \*

Department of Administrative Sciences, Naval Postgraduate School, Monterey, CA 93943, USA

This paper describes a Decision Support System (DSS) for strategic planning of Information Systems (IS) named ISSPSS (Information Systems Strategic Planning Support System) and the experience of its implementation. The system addresses three core issues of the IS strategic planning process: identifying the importance and role of information systems in the organization, defining IS objectives based on organizational objectives and critical success factors and formulating hardware distribution policy. The system's output is designed to guide an organization in formulating a policy for organizational information resource.

Keywords: Decision Support Systems (DSS), IS Planning, Strategic Planning, IS Objectives, Organizational Objectives, Hardware Policy.

![](/api/attachments/GGKE253K/fulltext/images/78bd15d61cc3a4b5cc9de9799802dfd4cb5093f49416f1d23591f4d32ff342c1.jpg)

Moshe Zviran is an assistant professor of Information Systems at the Naval Postgraduate School. He received his B.Sc in Mathematics and Computer Science and M.Sc and Ph.D in Information Systems in 1979, 1982 and 1988, respectively, from Tel Aviv University. His research interests include information systems planning, development and management of information systems, information systems security, decision support systems, and information systems in health care and

medicine. His published works have appeared in MIS Quarterly, Journal of MIS, Information & Management, Computers & Security, Journal of Medical Systems and other journals. Dr. Zviran served as a consultant in these areas for a number of organizations. He has also a number of years of experience in various positions in information systems in private and public organizations.

\* The author wishes to acknowledge Niv Ahituv and Seev Neumann of Tel Aviv University and William J. Haga of the Naval Postgraduate School for their many valuable comments and suggestions. The constructive comments provided by the Editor on an earlier version of this paper are also acknowledged with thanks.

1. Introduction

The importance of IS strategic planning and its alignment with corporate planning has been identified as a vital issue to continuing organizational success and IS performance and, therefore, a subject of interest to IS managers $[6,10,12]$ . Additional attention was drawn to this area by various information systems that have been employed to achieve competitive advantage in the marketplace rather than merely being operational service systems $[7,27,30,31]$ .

Strategic planning methodologies and models suggested by IS researchers recommend that IS strategies should emanate from organizational strategies to ensure compatibility between organizational and IS plans. However, most research work in this area has been normative, focusing upon the issue of “what should be done” rather than “how to do it” [26,33].

This paper reports on a DSS developed to assist managers in carrying out key activities of IS strategic planning. The objectives were to examine the characteristics of the IS strategic planning process, identify key activities, and formulate a DSS to support these activities.

## 2. The IS Strategic Planning Process

Information systems planning is a hierarchic process generally considered to consist of three phases: strategic, tactical and operational $[1,20,28]$ . Strategic IS planning focuses on linking organizational needs with information resources. Tactical IS planning seeks to establish an IS master plan with a planning horizon of five years. Operational planning is the lowest level in the planning hierarchy and is concerned with developing a detailed annual IS plan.

<table><tr><td>Activity</td><td>Related operations</td><td>References</td></tr><tr><td rowspan="3">Assess organizational characteristics</td><td>- Review organizational strategic plan</td><td>[4, 9, 16, 21, 28]</td></tr><tr><td>- Identify organizational objectives and strategy</td><td>[1, 2, 4, 9, 16, 21, 28]</td></tr><tr><td>- Assess organizational environment</td><td>[1, 4, 9, 21, 26, 28]</td></tr><tr><td rowspan="3">Assess IS environment</td><td>- Assess current IS capabilities</td><td>[1, 21, 28]</td></tr><tr><td>- Assess current application portfolio</td><td>[4, 6, 7, 19, 21, 28]</td></tr><tr><td>- Evaluate stage of IS maturity</td><td>[4, 11, 28]</td></tr><tr><td rowspan="2">Identify IS strategic opportunities</td><td>- Identify role and impact of IS</td><td>[6, 7, 19]</td></tr><tr><td>- Identify applications with strategic relevance</td><td>[7, 16, 23]</td></tr><tr><td rowspan="4">Set IS strategy</td><td>- Set IS objectives</td><td>[1, 4, 9, 16, 20, 26, 28]</td></tr><tr><td>- Set IS mission and strategy</td><td>[1, 4, 9, 16, 20, 26, 28]</td></tr><tr><td>- Define architecture policy</td><td>[1,4, 15, 19, 24, 32]</td></tr><tr><td>- Formulate IS charter</td><td>[1, 4, 20, 29]</td></tr></table>

Fig. 1. Major activities in IS strategic planning.

IS planning begins with establishing the IS strategic plan. This process evaluates environmental and organizational factors, choosing objectives for the information systems and formulating policies to govern the architecture, acquisition, use and disposition of the IS resources $[1,20]$ . Figure 1 outlines the major activities of IS strategic planning with a set of related operations for each activity.

1. Strategy Set Transformation (SST)

2. The Strategic Grid

3. Strategic Fit with Organizational Culture

4. Derivation from Organizational Plan

5. Portfolio Management

6. Value Chain Analysis

7. Nolan Stage Model

8. Customer Resource Life Cycle (CRLC)

Fig. 2. IS strategic planning methodologies.

Acknowledging the importance of strategic planning in the process of managing an organization's information resource, a collection of methodologies that serve in carrying out this process has been proposed. Figure 2 portrays methodologies for the IS strategic planning phase. Each, however, relates only to a partial set of IS strategic planning activities; none provides a comprehensive solution. Moreover, since the existing planning methodologies are normative, they do not address managerial problems that arise as to how strategic planning is to be done and how to make the best use of current methodologies [28,32].

As many IS researchers point out, a major theme in IS strategic planning is how to integrate the characteristics and objectives of the information systems with those of the organization they are to serve. Since it seems that IS strategy should derive from the overall organizational strategy $[7,16,19,25]$ , the basic IS strategic planning effort should concentrate on revealing the organization's strategy and setting the basic guidelines for the organizational information systems to support this strategy.

## 3. Design objectives for ISSPSS

Design objectives for a DSS to support IS strategic planning include:

Flexibility - due to differences among organizations, the DSS should have an ability to deal with various environments and organizational settings [16].

Prescriptiveness - the system should provide a clear understanding of the role and importance of the organizational information systems [6,21].

Ease of use - since typical users will be top managers rather than computer experts, an IS strategic planning support system should be easy to use, producing output that can be trusted and easy to learn [17].

Responsiveness - many organizations avoid performing IS strategic planning since it is considered to be a lengthy process. A DSS that can respond quickly will enhance the chances that organizations will perform this planning activity [5,21].

Reliability - because of the nature of the IS strategic planning process, any system designed to support its activities must rely on well accepted and validated models [8].

Based on these requirements and the key activities of the IS strategic planning process that are common to all organizations, our proposed DSS aims to help strategic planners in identifying the role and importance of IS to the organization and the dependence of IS objectives and architecture upon organizational characteristics and objectives.

## 4. ISSPSS - System Characteristics and Components

ISSPSS is an interactive DSS that was developed to assist IS managers in carrying out key activities of IS strategic planning. The system was designed and developed for an IBM PC and can, therefore, be easily implemented on any IBM PC or compatibles.

Following Alter's classification of DSS [3], this system is a model-oriented Suggestion DSS. It generates suggested guidelines for an IS strategic plan with empirically-based formulae and decision rules, documenting the process, and producing a draft of an IS strategic plan.

The main component of ISSPSS is its model base. It is comprised of three independent modules, each of which is devoted to a specific issue of the IS strategic planning process. Figure 3 outlines the planning activities supported by ISSPSS's model base.

The first module deals with assessing the importance and role of the organizational information systems through McFarlan and McKenney's strategic grid $[7,18]$ . This is a contingency approach to deciding on the IS planning effort. It defines four levels of the importance of information systems to an organization, depending on the strategic impact of its existing application portfolio and the application portfolio planned for development. The position of an actual organization on the grid reflects the relative importance of these portfolios. The strategic grid can be used as a diagnostic tool to understand the role of information systems in an organization. It also explains the level of top management involvement needed and the relationship of the information systems plan to the organizational plan.

The location of an organization on the grid is determined by a model that was developed and empirically validated [22,32]. The model consists of seven measurable variables, dedicated to the following issues:

![](/api/attachments/GGKE253K/fulltext/images/ceeece276ccb8174a0a7f961b7e4276a2f425ba6ce08c1e0381e3a8ed0e60bed.jpg)  
Fig. 3. Planning activities supported by ISSPSS.

\- degree of IS support of organizational strategy;
- degree of IS support of operational management;

\- degree of IS contribution to profitability;

\- degree of criticality of IS.

Putting this model to work, a user answers a set of seven questions. The output is an organization's position on the strategic grid.

The second building block explores organizational objectives and Critical Success Factors (CSF), to derive IS objectives. The model consists of a mapping scheme between organizational and IS objectives, described and empirically validated [32]. It helps to carry out the ideas of the Strategy Set Transformation methodology [16] by relating specific IS objectives to corresponding organizational objectives.

The main steps in this process are to:

1. define organizational CSFs (as a background to setting organizational objectives);

2. define organizational objectives (based on a pre-defined set of possible objectives proposed by the system, plus additional user-defined organizational objectives);

3. select IS objectives from those proposed by the system (corresponding to the selected organizational objectives resulting from the previous step) and add other, user defined, IS objectives.

The mapping scheme serves as a communicating mechanism between steps 2 and 3, resulting in a proposed set of IS objectives for the organizational objectives selected in step 2.

The third module in ISSPSS deals with IS architecture. The model leans on the findings of an empirical study $[2,32]$ , suggesting a fit between organizational geographical structure and IS architecture. Since organizational structure is superimposed on its information systems, the model seeks the IS architecture – centralization, distribution or decentralization – that best matches the organizational geographical structure. It proposes that architecture to a decision maker along with an explanation for this recommendation.

There is no database per se in ISSPSS. Necessary data are input during the system's operation for use by its various models. Data can be saved in interim storage for further elaboration and sensitivity analysis. They can also be organized in external files if further processing is desired.

The user interface is a combination of menus and question/answer dialogues. While menus guide users through specific activities of ISSPSS, the question/answer mode is used to inquire of a users' knowledge base for answers needed as input for the DSS's models. In addition, ISSPSS has a built-in help feature to assist users in understanding the system and accomplishing the planning task.

As previously mentioned, the system produces a preliminary draft for the IS strategic plan. The presentation capacity includes four optional output modes:

a. A user can view the output on the screen;

b. A hard copy can be printed (illustrated in Appendix A);

c. A system file can be saved, for future processing and analysis;

d. An ASCII output file can be produced and transferred as input to other systems (e.g. a word processor).

## 5. System Organization and Function

The work flow within the system consists of three generic activities: input session; review of system's output and sensitivity analysis; and output production - a draft of an IS strategic plan.

Figure 4 outlines the steps involved in generating a decision by ISSPSS. Blocks 1–6 represent activities included in the input session. A typical dialogue of the input session consists of the following steps:

![](/api/attachments/GGKE253K/fulltext/images/699087eef4b89fb3804142302ba1463896dba63c10a105d3f58714b1c3bd824c.jpg)  
Fig. 4. Steps involved in generating ISSPSS decision.

a. Input of organization characteristics (name, size, structure, sectoral affiliation and geographical dispersion of organizational units).

b. Formulation of organizational CSFs (in free format).

c. Analysis and assessment of key issues regarding the role and importance of IS in the organization. These questions refer to the present situation and future expectations of the following issues:

\- the extent of IS application to advance organizational CSFs;

\- the extent to which IS aid the organization to compete in the market;

\- the extent to which IS serve the middle management echelon;

\- the extent of IS use for administrative and operational applications;

\- the extent of aid provided by IS to increase organizational profitability;

\- the extent to which IS improve operational areas (such as reduction of manufacturing costs and minimizing inventory);

\- the extent to which IS are critical to the functioning of the organization.

d. Selection of organizational objectives from a pre-defined set of common organizational objectives presented to the system. The list is presented in Figure 5, a subset of which is proposed by the system according to an organization's sectoral affiliation (from step a).

e. Setting of user-defined organizational objectives, in addition to those mentioned in step d.

f. Selection of IS specific objectives from a subset of possible IS objectives that correspond to the organizational objectives selected in step d.

4. Improve service quality

5. Supply products and services on time

6. Gain competitive advantage

7. Improve product quality

8. Improve productivity

Fig. 5. Organizational objectives.

Figure 6 outlines the list of possible IS specific objectives.

g. Setting of additional, user-defined, IS specific objectives that relate to organizational objectives set in steps d through e.

h. Selection of general IS objectives from a predefined, literature-based, set of general IS objectives, and setting additional, user-defined, general IS objectives. Figure 7 lists the proposed set of general IS objectives.

Step 7 in Figure 4 creates a preliminary output that can be refined at the review and sensitivity analysis session (step 8). Figure 8 illustrates the review and update menu, which guides a user to desired activities of the review process. Users can perform changes or sensitivity analysis for each data item through repetition of input steps, and examine the full consequences of these changes on the resulting output. The final step in ISSPSS operation is output production – hard copy, file, or both.

## 6. Implementation Experience with ISSPSS - Three Case Studies

The outcomes and advantages of using ISSPSS are demonstrated by three real-life implementation experiences. The system was implemented in three different organizations in Israel During the Summer of 1988. Each of these had its unique characteristics and environmental setting. All three organizations had planned for their information systems and had a written IS plan that was up to two years old. This enabled a comparison of the existing IS plan and the outputs of ISSPSS.

## 6.1. Case study I

The first case study was performed in a large manufacturing firm which had originally produced its IS plan two years earlier and was reevaluating it. The firm is one of the 50 largest companies in Israel, has some 1,000 employees and annual revenues of approximately 100 million dollars. Its organizational structure is functional and strategic decisions are made by general management. Headquarter offices are located in Tel aviv and all manufacturing activities are performed in five plants located within a 40-mile radius of headquarters.

<table><tr><td>1.</td><td>Provide timely information on customer orders</td></tr><tr><td>2.</td><td>Provide sales information for sales Forecasting</td></tr><tr><td>3.</td><td>Incorporate information systems in customer account control</td></tr><tr><td>4.</td><td>Provide reliable information on the organization&#x27;s financial situation</td></tr><tr><td>5.</td><td>Provide information for raw material inventory control</td></tr><tr><td>6.</td><td>Provide information on logistic control and spare-parts management</td></tr><tr><td>7.</td><td>Provide information for human resource management</td></tr><tr><td>8.</td><td>Provide timely information for cost control</td></tr><tr><td>9.</td><td>Provide information for investments management and control</td></tr><tr><td>10.</td><td>Provide information to improve the allocation of scarce resources</td></tr><tr><td>11.</td><td>Provide information on competitive products and services</td></tr><tr><td>12.</td><td>Provide information for marketing forecast</td></tr><tr><td>13.</td><td>Integrate information systems in production planning and control</td></tr><tr><td>14.</td><td>Provide information on finished goods inventory</td></tr><tr><td>15.</td><td>Provide information for quality control</td></tr><tr><td>16.</td><td>Incorporate information systems in service systems to improve service quality</td></tr></table>

Fig. 6. Specific IS objectives.

ISSPSS was implemented and used at the company's headquarters during a special meeting of its IS steering committee, devoted to reevaluating the IS strategic plan. The committee consisted of the company's president; three senior vice presidents heading finance, manufacturing and marketing; and the Chief Information Officer (CIO). Since ISSPSS is designed for a single-user operation mode, the CIO acted as a facilitator to link the system with all decision makers.

After reviewing current IS status and the existing IS plan, input data were entered to the system and a preliminary draft was produced. Based on this draft, a discussion concerning the role and objectives of IS was developed. This process resulted in five iterations of sensitivity analysis through data modifications and reviews of its impact on outputs.

The concluding output is portrayed in Appendix A. It first indicates that the company is located in the "FACTORY" cell on the strategic grid. It provides an explanation regarding the implica-

1. Facilitate the attainment of organizational objectives

2. Develop and operate control systems

3. Improve the flow and availability of information for management

4. Develop applications in light of the systems approach principle

5. Ease the transferability of data among applications

6. Develop system using most advanced technologies

7. Create corporate data base, common to the entire organization

8. Provide accessibility to organizational data base

9. Assure data security and confidentiality

10. Initiate and develop local applications for departmental units

Fig. 7. General IS objectives.

tions of this location as well as guidelines for organizing and managing the company's information systems. After listing the CSFs and selected organizational objectives, IS objectives were outlined. These objectives aimed at supporting the organizational objectives, and include:

\- Provide timely information for customer orders;

\- Provide information on sales for forecasting;

(size, structure and geographical dispersion), IS-SPSS proposed CENTRALIZATION as the appropriate IS architecture, with further supportive information about the meaning of this recommendation.

\- Integrate IS in production planning and control;

and others. Based on organizational characteristics

Evaluation of ISSPSS's output and the two-year-old IS plan reveals a similarity in organizational and IS objectives and the proposed IS architecture. While the strategic grid approach was not used during the planning exercise two years ago, there was an overall consensus among the steering committee members that the location of the firm on the grid helped them to understand the role of their information systems. ISSPSS's concluding document was approved as the new guideline for managing the organization's information systems.

```batch
REVIEW & UPDATE MENU
Review & Update - General Information
Update Organizational Characteristics
Update Critical Success Factors
Update I.S. Importance Parameters
Update Organizational Objectives
Update I.S. Objectives
Update I.S. General Objectives
End Update Session, Back to Main Menu
```

```txt
Use arrow keys (↑↓) to select your choice.
Press 'ENTER' (←) to operate
```  
Fig. 8. ISSPSS review and update menu.

## 6.2. Case study II

The second implementation took place in a medium-size insurance company. The company specializes in casualty and life insurance and is considered to be technology-oriented. It has approximately 550 employees and is one of the most profitable firms in the insurance sector.

The company is functionally organized. In addition to its Tel Aviv headquarters, the company has four branches, each of which controls insurance agents in its region. Strategic decisions are made at the headquarters level while tactical decisions are made at the branches. Operational decisions are made either at the branch level or by insurance agents.

About six months prior to implementing IS-SPSS, the company had gone through a comprehensive process of IS planning that resulted in its IS plan. In this planning process, the company made use of the BSP methodology [13]. Since this methodology is not directed to the strategic planning phase, ISSPSS was implemented to examine and reevaluate the strategic guidelines for the information systems.

As in the previous example, the system was implemented by the CIO. Input data were based on three sources: the company's business plan, its existing IS plan, and the CIO's familiarity with the organization. Based on these data, a draft was produced by ISSPSS. The CIO performed sensitivity analyses on some of the variables in the model base which led him to the final version of the system's output.

Based on the input data, the company was positioned in the “STRATEGIC” cell on the grid, meaning that its information systems are critical to the current strategy and future strategic directions of the firm. Its critical success factors were:

– High quality marketing;

– High administrative efficiency;

\- Efficient financial management; and

\- Effective management and development of human resources.

The list of organizational objectives included:

\- Reduce costs;

\- Increase revenues;

\- Gain competitive advantage;

\- Improve administrative efficiency;

\- Improve services quality;

\- Supply services on time.

\- Increase productivity.

Based on these objectives, a list of 15 corresponding IS objectives was selected, focusing on maximum support of the organizational objectives. Organizational characteristics of this company resulted in DISTRIBUTION as ISSPSS's recommendation for its IS architecture.

A comparison of ISSPSS strategic plan draft with the existing IS plan reveals that both recognized the strategic importance of the information systems and both suggested hardware distribution. Nevertheless, the CIO admitted immediately that the use of ISSPSS was a benefit for the following reasons:

\- It helped in elaborating the IS strategic plan using well known methodologies;

\- It helped in understanding IS importance through using the strategic grid approach;

\- It helped in establishing the link between organizational objectives and IS objectives;

\- It provided further justification to the organization's decision of adapting hardware distribution as its future architecture.

The CIO further indicated that ISSPSS's output can be adapted as an integral part of the company's IS plan. Moreover, the board of directors claimed that the ISSPSS planning document helped them to understand the role of the information systems and the expected extent to which IS will support organizational activities.

## 6.3 Case study III

The third case study focuses on ISSPSS's implementation in a local municipality of some 150,000 residents. Its 1988 annual budget was 50 million dollars and it employed 1,500 people.

Until end-1988, all IS activities of this organization were performed by a service bureau, with an annual expense (1987 prices) of about one million dollars. In early 1988 the city council decided to develop its own IS facility. A steering committee consisted of three top executives and an outside IS consultant performed the IS planning and established a comprehensive IS plan approved by the city council.

The implementation of ISSPSS in this organization came after the 1988 IS planning process. It served as an additional planning exercise and aimed at examining the IS strategic plan. All steering committee members took part in this planning exercise with the IS consultant serving as the system's facilitator. After entering input data, the preliminary output was reviewed by the committee, resulting in some changes during the review and update process.

ISSPSS's concluding document mapped the organization into the “SUPPORT” cell on the strategic grid, suggesting that IS applications are useful but not vital to the organization. The fact that this is a service-oriented, not-for-profit organization was reflected in its CSFs (“Provide best quality services” and “Effective management and operation of the organization”), its organizational objectives and corresponding IS objectives. Since the organization is centralized, both in its decision making process and geographically, CENTRALIZATION was proposed by ISSPSS as the appropriate IS architecture.

Although the guidelines in ISSPSS's concluding document were very similar to the existing IS plan, the steering committee indicated its satisfaction with the planning exercise. They found that, unlike the lengthy and costly manual planning process, ISSPSS was easy to use and produced a clear and easy-to-understand output. Secondly, although both the manual process and ISSPSS led to the same location on the strategic grid, the committee felt more confident with ISSPSS's results since their manual process was based only on their feelings about the organization's strategy. Third, they pointed out that the explicit linkage between organizational and IS objectives contributed to their understanding how the information systems can help achieve organizational goals.

From these three case studies, the following advantages were seen in using ISSPSS for initiating the IS strategic planning process:

a. ISSPSS proved to be easy to use and produce an easy to understand output.

b. In all three cases, ISSPSS's output matched the guidelines from the manuallyprepared IS plans.

c. Locating an organization on the strategic grid using ISSPSS's model base was helpful in clarifying the IS role in an organization.

d. An explicit linking of IS objectives with organizational objectives clarified the expected contribution of the information systems to achieving organizational goals.

e. All users expressed their confidence in the architecture recommendations provided by the system, indicating that such a DSS is bias free.

f. The sensitivity analysis capability helped users to feel comfortable and confident in using the system, mainly due to the ability to investigate the impact of changes in input data on ISSPSS output.

## 7. Summary

Strategic planning of information systems is a major challenge facing IS executives today. Effective planning is essential to understanding the role and importance of the organizational information systems and realizing their potential strategic impact. Nevertheless, since the existing planning methodologies are normative and descriptive, the managerial problems that arise are how the IS strategic planning is carried out and how to make the best use of current planning methodologies.

The DSS described here focuses on three key issues of the IS strategic planning process:

– identifying IS role and importance;

\- defining IS objectives based on organizational objectives and critical success factors; and
- formulating hardware distribution policy.

The system addresses these issues using relevant organizational data for its empirically-validated models.

The implementation experience gained in using the system in three real-life case studies confirmed that the system is capable of helping an organization perform the key activities of the IS strategic planning process. It proved to be easy to use, flexible and understandable. Moreover, all three case studies indicated that the ISSPSS's planning output matched the existing perceptions about the role of the organizational information systems and led to the approval of its output as strategic guidelines for the IS plan.

The implementation experience also revealed some practical limits in applying the system to real-life planning scenarios. First, the system addresses the conceptual level of IS strategic planning. Thus, its output provides neither practical mission statements nor guidelines for the subsequent planning processes. Second, ISSPSS is not easily applicable to large and complex business situations (e.g., conglomerates or multinational organizations). It seems to better suit small and medium-size organizations. It can also be applied to particular strategic business unit in large organizations.

## References

[1] Ahituv, N. and Neumann, S., Principles of Information Systems for Management, Dubuque, Iowa, Wm. C. Brown, Third Edition, 1990.

[2] Ahituv; N., Neumann, S. and Zviran, M., “Factors Affecting the Policy for Distributing Computing Resources”, MIS Quarterly, Vol. 13, No. 4, (December 1989), pp. 389–401.

[3] Alter, S.L., Decision Support Systems: Current Practice and Continuing Challenges, Reading, MA, Addison Wesley, 1980.

[4] Bowman, B., Davis, G.B. and Wetherbe, J.C., “Three Stage Model of MIS Planning”, Information & Management, Vol. 6, No. 1, (February 1983), pp. 11–25.

[5] Boynton, A.C. and Zmud, R.W., “Information Technology Planning in the 1990’s: Directions for Practice and Research”, MIS Quarterly, Vol. 11, No. 1, (March 1987), pp. 59–71.

[6] Brancheau, J.C. and Wetherbe, J.C., “Key Issues in Information Systems”, MIS Quarterly, Vol. 11, No. 1, (March 1987), pp. 23–45.

[7] Cash, J.I. Jr., McFarlan, F.W., McKenney, J.L. and Vitale, M.R., Corporate Information Systems Management: Text and Cases, Homewood, IL, Irwin, Second edition, 1988.

[8] Davis, G.B., “Conclusion of Part IV, IS Resource Management”, in: The Information Systems Research Challenge, McFarlan F.W. (ed.), Boston, MA, Harvard Business School Press, (1984), pp. 251–254.

[9] Davis, G.B. and Olson, M.H., Management Information Systems: Conceptual Foundations, Structure and Development, Singapore, McGraw-Hill, Second edition, 1985.

[10] Dickson, G.W., Leitheiser, R.L., Neches, M., and Wetherbe, J.C., “Key Information Systems Issues for the 1980’s”, MIS Quarterly, Vol. 8, No. 3, (September 1984), pp. 135–148.

[11] Gibson, C.F. and Nolan, R.L., “Managing the Four Stages of EDP Growth”, Harvard Business Review, Vol. 52, No. 1, (January–February 1974), pp. 76–88.

[12] Hartog, H.C. and Herbert, M., “1985 Opinion Survey of MIS Managers: Key Issues”, MIS Quarterly, Vol. 10, No. 4, (December 1986), pp. 351–361.

[13] IBM Corporation, Business Systems Planning: Information Systems Planning Guide, Application Manual GE20-0527-4, Fourth Edition, July 1984.

[14] Ives, B. and Learmonth, G.P., “The Information System as a Competitive Weapon”, Communications of the ACM, Vol. 27, No. 12, (December 1984), pp. 97–103.

[15] Johnson, J.R., “Enterprise Analysis”, Datamation, Vol. 30, No. 21, (December 1984), pp. 97–103.

[16] King, W.R., “Strategic Planning for Management Information Systems”, MIS Quarterly, Vol. 2, No. 1, (March 1978), pp. 27–37.

[17] Lederer, A.L. and Sethi, V., “The Implementation of Strategic Information Systems Methodologies”, MIS Quarterly, Vol. 12, No. 3, (September 1988), pp. 445–461.

[18] McFarlan, F.W., McKenney, J.L. and Pyburn, P.J., “The Information Archipelago – Plotting a Course”, Harvard Business Review, Vol. 61, No. 1, (January–February 1983), pp. 145–156.

[19] McKenney, J.L. and McFarlan, F.W., "The Information Archipelago - Maps and Roads", Harvard Business Review, Vol. 60, No. 5, (September–October 1982), pp. 109–119.

[20] McLean, E.R. and Soden, J.V., eds., Strategic Planning for MIS, New York, NY, Wiley-Interscience, 1977.

[21] Moskowitz, R., “Strategic Systems Planning Shifts to Data Oriented Approach”, Computerworld, Vol. 20, No. 19, (May 12, 1986), pp. 109–119.

[22] Neumann, S., Ahituv, N. and Zviran, M., “A Model for Determining The Strategic Relevance of IS to The Organization”, Naval Postgraduate School, Department of Administrative Sciences, WP 89-01, 1989.

[23] Porter, M.E. and Millar, V.I., “How Information Gives You Competitive Advantage”, Harvard Business Review, Vol. 63, No. 4, (July–August 1985), pp. 149–160.

[24] Pyburn, P.J., “Linking the MIS Plan With Corporate Strategy: An Exploratory Study”, MIS Quarterly, Vol. 7, No. 2, (June 1983), pp. 1–14.

[25] Siegel, P., Strategic Planning for Management Information Systems, New York, NY, Petrocelli Books, 1985.

[26] Shrivastava, P., “Strategic Planning for MIS”, Long Range Planning, Vol. 16, No. 5, (October 1983), pp. 19–28.

[27] Sprague, R.H. and McNurlin, B.C., Information Systems Management in Practice, Englewood cliffs, NJ, Prentice-Hall, 1982.

[28] Wetherbe, J.C., Systems Analysis and Design, St. Paul, MN, West Publishing, 1988.

[29] Whieldon, D., “MIS/DP Needs a Charter”, Computer Decisions, Vol. 12, No. 11, (November 1980), pp. 94–112.

[30] Wiseman, C., Strategy and Computers, Homewood, IL, Dow Jones-Irwin, 1985.

[31] Wiseman, C., Strategic Information Systems, Homewood, IL, Irwin, 1988.

[32] Zviran, M., A Methodology and a Decision Support System for Strategic Planning of the Organizational Information Systems, Unpublished Ph.D. Dissertation, Tel Aviv University, Israel, April 1988 (in Hebrew).

[33] Zviran, M., “Relationship Between Organizational and IS Objectives: Some Empirical Evidence”, Journal of Management Information Systems, Vol. 7, No. 1, (Summer 1990), pp. 65–84.

## Appendix A

Sample Output of ISSPSS for Case-Study 1

## A. General Information

Strategic planning for information systems (IS) is the highest level of planning. It is intended to define the overall mission and objectives for the organizational IS. ISSPSS is an interactive decision support system (DSS) for this phase of the organizational IS planning. The major purpose of the system is to help top management and the Chief Information Officer (CIO) in the formulation of guidelines for the IS strategic plan. This is done by defining the role, importance and objectives of the organizational IS, as well as the hardware deployment and distribution. The system attempts to achieve these goals by processing the input data, using a series of empirically validated models.

This appendix contains the final printout of ISSPSS results for CASE-STUDY-1. Its first two sections define the Strategic Grid approach and the organization's location on this grid. The following three sections consist of the organizational and IS objectives, followed by guidelines for hardware distribution policy and a conclusion. The printout may, therefore, be used as a preliminary draft for the IS strategic planning process.

## B. The Strategic Grid Approach

The Strategic Grid provides a contingency approach to deciding on the IS planning effort. It defines four levels of IS importance to the organization, depending on the strategic impact of existing information systems and those planned for development.

The layout of the strategic grid is as follows:

![](/api/attachments/GGKE253K/fulltext/images/a566ae38429493bd94a67b2f3e6093d3317a3746b712cfebb6292efd986e7c54.jpg)

The cells in the grid define the position of the IS activity relative to the organization:

STRATEGIC - IS activities are critical to the current strategy and/or to future strategic directions of the enterprise. IS applications are part of these directions.

FACTORY - IS applications are vital to the successful functioning of well-defined, well-accepted activities. However, they are not part of future strategic operations.

SUPPORT - IS applications are useful in supporting the activities of the organization. Locating an organization in this cell suggests that the major emphasis is on traditional data processing systems and that IS activities are not vital to critical operations and are not included as part of future strategic directions.

TURNAROUND - This is a transition state between ‘support’ and ‘strategic’. The organization has had support-type applications but is now planning for applications vital to strategic organizational success.

The strategic grid for IS is, therefore, a diagnostic tool for understanding the role, importance, and mission of the IS in the organization. The position on the grid explains the desired level of top management involvement and the relationship between the IS plan and organizational plan.

## C. Information Systems Importance and Role

The importance and role of IS to the organization were analyzed on the basis of the Strategic Grid approach.

The input data were processed using an empirically validated model to determine the organization's location on the grid. The analysis of the input data suggests that the organization is located in the lower level of the FACTORY cell in the grid. The exact location is denoted by ‘■’ in the following illustration:

![](/api/attachments/GGKE253K/fulltext/images/e0e9536ff3ed85c067c119f5aab73d0d585cf16e44e708ee6f18258f2897cf9e.jpg)

The location of the organization in the FACTORY cell means that IS applications are vital to the successful functioning of well-defined, well-accepted activities. However, IS are not part of future strategic operations.

This location can also be used to suggest the following guidelines for the organization and management of the IS planning effort:

\- Top management involvement and guidance are not critical.

– Guidance from corporate plan to maintain IS alignment.

\- Need for smooth functioning of IS is critical.

\- Attention should be given to detailed operational and capacity planning by the IS function.

## D. Organizational Objectives and Critical Success

Factors

Organizational objectives are general statements about what is to be accomplished. The following organizational objectives were selected for CASE-STUDY-1.

\- Reduce costs.

\- Improve services.

\- Supply products and services on time.

\- Increase productivity.

Furthermore, the following list of factors which were defined critical for this organization's success:

\- Maximal exploitation of financial reserves.

\- Production at required capacity.

\- High quality production.

\- Positive cash flow.

## E. Information Systems Objectives

IS objectives are general statements about what is to be achieved by the organizational information systems, and provide guidelines for the direction of the IS effort. The following information systems objectives were derived from the organizational objectives:

\- Provide timely information on customer orders.

\- Provide information on sales for forecasting.

\- Provide information for raw material inventory control.

\- Provide information for logistic control and spare-parts management.

\- Provide information for human resource management.

\- Provide information for cost control.

\- Provide information for investments management and control.

\- Provide information to improve the allocation of scarce resources.

\- Integrate IS in production planning and control.

\- Provide information on inventory and finished goods.

\- Incorporate IS in service systems to improve service quality.

## F. General Information Systems Objectives

General IS objectives are additional to those objectives listed in the previous section, and provide further guidelines for the characteristics and contribution expected from the organizational IS. The following general information systems objectives were indicated for CASE-STUDY-1:

\- Facilitate the attainment of organizational objectives.

\- Develop and operate control systems.

\- Improve the flow and availability of information for management.

\- Ease the transferability of data among various applications.

\- Develop systems using the most advanced technologies.

## G. Hardware Distribution Policy

The last set of guidelines deriving from ISSPSS refers to hardware deployment and distribution. As suggested by many, it is the role of top management to determine the organizational policy for hardware distribution.

Such decision is, of course, specific to each organization and takes into account many parameters. Some research in the IS field showed, however, that hardware distribution is mainly based on the geographical distribution of the decision making process within an organization. Based on this theory (which was also empirically validated), and the characteristics of CASE-STUDY-1, it is suggested for the organization to adopt CENTRALIZATION for hardware deployment policy.

Centralized hardware deployment defines a policy where all computer facilities (processors, peripheral equipment, etc.) are centralized in one geographical location and thus provide all computing needs for the entire organization.

## H. Summary

As it seems, the organizational IS are profitable and important in their own right. CASE-STUDY-1 is heavily dependent on cost-effective, totally reliable IS operational support for smooth operation. However, the organizational IS are not fundamental to the ability to compete and/or survive. This conclusion is mainly derived from the location of the organization on the strategic grid, as well as from the IS objectives.

The results and conclusions presented in this draft should guide the organization and its IS department in formulating the policy for the organizational IS, as a preliminary stage to preparing the IS master plan.
