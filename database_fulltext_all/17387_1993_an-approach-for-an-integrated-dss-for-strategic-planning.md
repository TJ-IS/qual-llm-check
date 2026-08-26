---
otero_id: 17387
otero_key: "4NQB2DA6"
title: "An approach for an integrated DSS for strategic planning"
authors: "Jürgen Moormann; Martin Lochte-Holtgreven"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90070-j"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# An approach for an integrated DSS for strategic planning \*

Jürgen Moormann

Diebold Deutschland GmbH, Eschborn, Germany

Martin Lochte-Holtgreven

Krupp MaK Maschinenbau GmbH, Kiel, Germany

Although Decision Support Systems (DSS) have become widespread in recent years for operational control their use in strategic decision-making has only rarely been seen. This study investigates how DSS technology can be applied in the process of strategic planning. The requirements of Strategic Decision Support Systems (SDSS) are discussed and a conceptual frame for the construction of SDSS is developed. The authors emphasize the integration of both the planning instruments and the corresponding data flows. They present the StratConsult system – a PC-based prototype for supporting strategic sessions. Benefits and drawbacks of SDSS are explored and relevant trends for integrated computer-aided strategic DSS are outlined.

Keywords: Strategic planning; Decision support system; DSS generator; Financial modelling language

![](/api/attachments/4NQB2DA6/fulltext/images/350d82166aa4c492a08e7dd963885074de98f418a53bec0ae3f7214acd4bde4f.jpg)

Jürgen Moormann is a management consultant in the financial industry. He has been in banking for three years before he studied business administration at the universities of Kiel, Germany, and Zurich, Switzerland. Prior to his consultant activities he was a scientific assistant at the Institute of Business Administration, University of Kiel, where he received a Ph.D. in Economics and Social Sciences. His current research interests include various aspects of decision

## 1. Introduction

The competition at the markets is getting ever harder. Political and social changes, the common European market, and the rapid advance of new technologies require new approaches to corporate planning. As top management has to develop comprehensive corporate strategies to cope with the increasing instability and complexity of the environment, strategic planning becomes most important.

For operational control, Decision Support Systems (DSS) have become widely used. They represent computer-based applications for the decision-making process. Yet DSS have hardly been used in the important field of strategic planning. How can DSS technology be applied in the process of strategy planning?

This paper starts with a brief discussion of the most important terms as well as an overview of some representative software tools for DSS. On this basis a conceptual frame for the construction of DSS for strategic purposes is developed with an emphasis on overall system integration. We concentrate on technological aspects rather than methodological aspects of strategic planning where we follow the implementation school of DSS research [34]. Furthermore, we present the StratConsult system, a prototype of a PC-based planning system supporting strategic decisions. We then discuss the benefits and shortcomings of computer-based strategic DSS in general. In ad-

![](/api/attachments/4NQB2DA6/fulltext/images/c06c1d04c098f799acd5a57ed11af7f3689919bb0df02cfc30b50b975ad33d13.jpg)

1989, he is working as a consultant for strategic IT applications.

support systems, strategic management and strategic IT planning. Dr. Moormann also lectures at the Department of Business Informatics of the European Business School, Oestrich-Winkel, Germany.

dition, ideas for future developments of strategic DSS are presented. Finally, we shall draw some conclusions on the integration of strategic planning and DSS technology.

## 2. Definitions

## 2.1. Strategic planning

Strategic planning focuses on the development of an organization's overall goals and the required policies for achieving them [16,22,25]. In trying to cope with an ever-changing and challenging environment the area of strategic planning has gained wide acceptance and interest among both managers and academics.

In long-term business planning, the radical changes in the markets have passed the limits of conventional extrapolation methods. Today, this approach is less suitable for strategic planning since turbulent and complex environments require a sophisticated, comprehensive concept to design the long-range future of companies and other organizations.

This concept has to be a continuing process to prepare the organization for rapidly evolving threats and opportunities. Strategic planning involves the influences of all relevant environmental issues as well as the internal capabilities and resources. Permanent adjustments to the changing environment are essential for lasting success (“change management”). Strategic decisions give input to subsequent systems of both management control and operational control.

The cycle of strategic planning consists of three basic phases: information, design, and evaluation. This concept corresponds to the decision process theory of Simon [31] who identifies intelligence, design, and choice as the central steps of each decision process. The functions of information, design, and evaluation are highly interconnected. According to this concept the strategic planning process can be viewed as shown in Figure 1.

The strategic planning cycle begins with the analysis of the organization's internal and environmental situation. The information phase also includes the definition of strategic business units (SBUs). In the second step, the design phase, the overall goals are defined and alternative strategies to achieve these goals are outlined. The planning process is completed by the evaluation phase where the final strategy is selected and described in detail, giving policies for SBUs and functional sectors (e.g. personnel, production and operations, logistics).

![](/api/attachments/4NQB2DA6/fulltext/images/4166c439ce39a740162c3ca5df516514cf00c03e882c1fccf8a5e6863570982d.jpg)  
Fig. 1. Process model of strategic planning.

Following the planning period, the strategic management process also includes the implementation of the selected strategy and subsequently the implementation control.

## 2.2. Decision support system (DSS)

The classical definition of Sprague [32] describes a DSS as an interactive computer-based system that utilizes decision models, gives users easy and efficient access to a powerful data base, and provides various display possibilities.

Thus, the basic software elements of an interactive DSS are

\- Data Base Management Software (DBMS),

\- Model Base Management Software (MBMS), and

\- Dialogue Generation Management Software (DGMS) [2,33,39].

A decision component has been added by several authors to construct a knowledge-based DSS [4,18,37].

Yoo and Digman define DSS “...as general purpose systems which support decision makers in their planning, problem solving, and decision tasks that are relatively unstructured and which try to permit ease of use and flexibility of the system" [40, p.117]. According to Keen and Scott-Morton [20] decisions are unstructured when we cannot precisely identify the significant parameters of the problem. A more recent, generalized understanding of DSS might be stated as follows: A DSS is a highly flexible and easy-to-use computer-based system that helps decision makers utilize data and models to analyze unstructured problems.

Sprague and Carlson distinguish between specific DSS, a DSS generator, and DSS tools $[33]$ . According to this widely accepted view a specific DSS is a DSS “application”. A DSS generator is defined as a package of related software which provides a set of capabilities to build a specific DSS quickly and easily. The third and most fundamental level of DSS technology is called DSS tools. These are hardware and software components which facilitate the development of specific DSS or DSS generators.

## 2.3. Strategic decision support systems (SDSS)

In recent years, we have seen a growing interest in combining strategic planning with the DSS approach [e.g. 1,5,7,28,40]. DSS technology is obviously applicable to strategic planning as strategic decisions are complex and unstructured and DSS are intended for just such underspecified decision problems [21]. But top management is still reluctant to apply decision support systems [17].

We agree with King when he defines SDSS “...as the variety of DSS that is specifically designed to support top management and planners in their strategic management functions” [21, p.74].

SDSS are characterized by certain features. They

\- contain one or more specific DSS,

\- address a class of problems that are strategic in nature,

\- concentrate on the ‘information’ and the ‘design’ phases rather than the ‘evaluation’ step,

\- integrate all relevant data resources and planning techniques, and

\- cover both the conceptual planning process and the corresponding tools including the software configuration.

These requirements provide an excellent foundation for a SDSS architecture.

## 3. Software tools for strategic DSS

A range of authors has been working on computer-based strategic decision-making $[8,11,13,15,23,24,29,38]$ . However, the SDSS software market has so far not seen an integrated system that could be used as an overall standard tool. On the other hand there is a wide selection of software packages available that are suited to cover some parts of the strategic planning process.

DSS software tools can be classified in the following groups:

\- Prestructured DSS applications

\- DSS generators

\- Spreadsheet packages

\- Financial modelling languages

\- Other software tools suitable for special applications.

There are several pre-structured applications available (e.g. Ansplan, PIMS/PC, Strad, Stratpac), developed using general-purpose programming languages or other standard PC software packages. Most commonly they are designed for stand-alone personal computers. These applications do not support the whole planning process but they can be used in specific situations of the strategic process. Most of them are applied to what-if planning or the popular portfolio analysis. It should be noted, however, that they are often isolated from other PC-based planning tools and therefore create interface problems, while SDSS demand an integrated toolbox approach.

Therefore, our approach to the SDSS design focusses on the more flexible DSS generators and other supporting tools.

DSS generators are software packages which include predefined microalgorithms, specific data elements, and a more simplified syntax for business planning purposes. These packages have become widespread during recent years. Tools for generating DSS include spreadsheet packages and financial modelling languages $[12,36]$ . Table 1 shows representative software tools for building DSS.

In the following we shall take a closer look at DSS generators, especially to financial modelling languages. This class of computer software is specifically designed for planning, financial analysis, and decision support [3,28,30].

<table><tr><td>Table 1DSS software tools.</td></tr><tr><td>DSS Generators* Financial Modelling Languages(for use on- mainframes : e.g. FCS, IFPS, System W,- PCs : e.g. Micro-Control, Compete!. Micro-FCS)* Spreadsheet Packages(e.g. Excel, Lotus 1-2-3, Open Access)Other kinds of software packages that can be used for DSS environments include* Report Generators(e.g. Focus, Mapper, Ramis)* Statistical Analysis Packages(e.g. SAS, SPSS, Statpro)* Business Graphic Software(e.g. Freelance, Harvard Graphics)* Information Management Software(e.g. AskSam, IZE)* Database Software(e.g. Adabas, dBase, Oracle)* Communication Software(e.g. Aremos, Genesys)* Word Processing Software(e.g. Word, Wordperfect)</td></tr></table>

The main difference of financial modelling languages with respect to spreadsheet packages is given by the separation of logic and data components. In financial modelling languages the logic can be used for several data sets resp. data can be used for various experiments with different model logics while spreadsheets do not offer this flexibility. Modelling languages require more training than spreadsheet products but they are more powerful.

## 4. Construction of strategic decision support systems

Up to now there is a lack of systems which fit to the characteristics of strategic planning. Only a few real world applications are known.

Interesting concepts for strategic DSS have been shown e.g. in [7] and [40]. But these frameworks have not been implemented. Another approach has been presented and implemented by Applegate et al. [1]. They introduce a model management system for strategic planning which is based on the decision process model of Simon.

The system contains planning instruments for three phases: formulation, solution/action modelling, and implementation.

## 4.1. Requirements for SDSS

To provide adequate DP support several requirements of SDSS must be fulfilled. Computer-assisted systems for strategic planning have to take into account the characteristics of the strategic decision process [7]. SDSS should

\- support the unstructured type of strategic decisions. Strategic decisions are characterized by an enormous complexity and quantity of internal and external data. Nevertheless planners have to cope with insufficient data material and missing knowledge because of uncountable interdependencies. Strategic decisions are highly unstructured decisions. Human intuition and judgement, management experience, and creativity are generally needed to reach a decision.

\- provide instruments for each of the three basic phases. A SDSS has to support the whole strategic planning process including information, design, and evaluation.

\- integrate a variety of planning instruments or techniques [e.g. see 16,26]. The conceptual frame of a SDSS should reflect a toolbox of various instruments. The variety of planning techniques or instruments is typical for concepts of strategic planning. At present, a strategy cannot be developed by using a single instrument but the integrated use of various instruments. The aim of all these instruments is to provoke new ideas and a better methodological background. The instruments can be viewed as modules of the strategic planning process.

\- be highly flexible for model changes, adaptations, and enhancements at any time.

\- allow quantitative and qualitative data input. The system must provide heuristic and analytical instruments to cope with both qualitative and quantitative data.

\- facilitate the access to internal and external data bases.

\- offer pre-defined graphics and reports but also allow individual outputs.

\- be easy to use so that top managers can easily work with the system. It must be accepted that strategy planning is a top management's responsibility. As far as top managers get involved in using PC-based planning systems DSS applications must be completely user-oriented (turn-key applications).

![](/api/attachments/4NQB2DA6/fulltext/images/891a97ca96e0623ddf491ae5f49a41e2f361399a91191207582ea5cf7ed0b1c4.jpg)  
Fig. 2. Architecture for an integrated strategic decision support system.

\- allow group decision-making. Because of the fundamental importance of strategic decisions for the organization usually a group of persons is involved in the planning process. Therefore strategic decisions can be classified as multi-personal decisions.

## 4.2. Conceptual frame for an integrated SDSS

How to design an appropriate architecture for SDSS?

Each single instrument of strategic planning can be implemented as an isolated DSS. This approach corresponds to the idea of specific DSS [33]. In the context of strategic planning this means that we have to implement a variety of specific DSS. These DSS should be integrated in a conceptual frame for strategic planning. Because of this architecture the resulting system will support all phases of the strategic planning process. The whole set of all specific DSS for strategic planning we call SDSS. A concept of an integrated strategic DSS is shown in Figure 2.

The dots symbolize various instruments of strategic planning whereas arrows symbolize the integration of instruments resp. the corresponding flows of data.

There are two aspects we want to point out concerning the integration of specific DSS:

\- All components of the toolbox must be integrated by a homogeneous user interface.

\- Connections are necessary between the specific DSS. Especially the integration of instruments and the internal/external data interchange must be paid attention to. We make a distinction between horizontal and vertical integration:

\- Horizontal integration of instruments. That means that there are connections between the stand-alone instruments within each basic phase. Thus the workthrough in a logical sequence will be ensured.

\- Vertical integration of instruments. By this way the strategic phases of information, design, and evaluation are interconnected. So the planning team will be guided to the next phase. Additionally, some instruments might be used in several phases (e.g. the Relevance Tree Technique).

\- Horizontal data integration. Results of a specific DSS can be used by another DSS of the same phase. Therefore quantitative and qualitative data have to be transferred into the current specific DSS. Furthermore, the access to external online databases and the integration into client-server architectures within the organization must be ensured.

\- Vertical data integration. Results of a finished phase are used in the following phase. Thus, the system must allow the transfer of these data (e.g. data from the internal strategic database are necessary for constructing a SBU graph).

The design of a SDSS therefore requires a profound background knowledge of the individual strategic planning process, the existing specific IT environment, and the DSS tool market.

## 4.3. Implementation and control of SDSS

Though the common success factors for introducing information technology applications are well known, the implementation of SDSS requires extremely careful work.

The profound support SDSS can provide has to be reflected by the consequences that might be evoked by a computer-driven misjudgement concerning a strategic decision situation.

Thus users, i.e. top managers, will benefit from a SDSS only if they can trust the correctness of the underlying information processes. This, however, depends both on the logical correctness of the models and data used and on the psychological trust to the system. Managers should be guided to positively accept the SDSS as a useful tool but never lose a slight mistrust in the computer's output.

Very close cooperation of the management with the system designers and extensive testing is needed. Testing and a constant checking for consistent system behaviour should not be restricted to the system development phase but continue through the whole SDSS lifecycle. Quality checks by independent system experts should also be included on a regular basis to ensure unbiased decision support.

![](/api/attachments/4NQB2DA6/fulltext/images/a3327610bdfe0072442415a67a8305676c97ad887996c402b94cc215dc8f9fdf.jpg)  
Fig. 3. Structure of StratConsult.

## 5. StratConsult

StratConsult is a prototype for a real world application to improve strategic decisions. It runs on IBM-compatible PCs under DOS and is produced with the financial modelling language Micro-FCS (vendor: Pilot Executive Software, Inc.). This is the PC version of the DSS generator FCS (Financial and Corporate Planning System) which is a well known product on mainframes and workstations.

Micro-FCS enables system development techniques including menu programming, sub programming, and compilation of the model logic. So even complex black-box applications can be built. Micro-FCS has been used as a programming tool to build ready-to-use applications.

The idea of StratConsult is to provide the essential spectrum of strategic planning instruments under a menu-driven user interface. It provides a variety of qualitative and quantitative methods. It covers all phases of the strategic planning process. The system is designed to support planning teams directly in strategic planning sessions.

## 5.1. The structure of the system

Each strategic instrument has been implemented as a stand-alone application. All these applications have been integrated in a common frame. For us, the logical grouping of the instruments and their interaction is most important. Figure 3 presents an overview of the system's components.

<table><tr><td>Table 2Instruments implemented in StratConsult.</td></tr><tr><td>Information phaseWork Programs and Planning CalendarInternal Strategic DatabaseAccess to External Online DatabasesSWOT AnalysisRelevance Tree Technique</td></tr><tr><td>Design phaseCorporate Culture AnalysisMorphological MethodCross Impact AnalysisPortfolio AnalysisStrategic Business Unit Graph</td></tr><tr><td>Evaluation phaseWhat-if ModelDecision Tree Technique</td></tr></table>

The integration of the strategic instruments was achieved by an integrating menu system which covers the three basic phases of information, design, and evaluation. The main menu branches into sub menus for the basic phases. From here the desired application can be started. For example, the application of the relevance tree technique allows the users to ask information on the technique, to start the procedure, and finally to receive a report on the results. Of course the findings are saved in a data file, too.

Today, the system consists of 12 strategic instruments (Table 2).

## 5.2. Benefits and shortcomings

An integrated SDSS is a powerful tool to improve the effectiveness of strategic planning under complex environmental conditions.

Systems like StratConsult

\- allow direct use of the system within strategic planning conferences (e.g. system installed on a PC or laptop, with video-transmission). Thus, the planning process becomes more systematic and goal-oriented.

\- allow actual calculations and rapid graphical representation. The direct access resp. input of data from actual calculations ensure instant discussions. Therefore the planning process becomes faster and far more efficient. Because of the possibility of rapid graphical representation complex interdependencies can be visualized directly.

\- create participation by top management, the planning team, and the consultant because of the system's ease of use.

\- support cooperative work within the planning team. Although StratConsult is not really a multipersonal system it enhances group decision-making.

\- allow the enhancement by other instruments and methods of management science at any time.

Still there are some drawbacks of computer-based SDSS to take into account.

Technical constraints put several limits to the

applications that can be developed today:

\- DSS generators are designed on the base of the software tool market. Thus there is always a time lag in DSS development before latest techniques get incorporated, resulting i.e. in uncomfortable user interfaces.

\- Modern relational data bases have only rarely been used as a basis for DSS though they provide an excellent and flexible way to use the company-wide data pool. Direct interfaces to such databases, e.g. SQL-statements, should become standard within each DSS tool.

\- The use of distributed databases, data access in heterogenous networks, and support of the client-server concept are still not satisfying. Non-technical drawbacks are also found, as

\- verbal information becomes more and more important in strategic planning but up to now this is not incorporated in DSS generators;

\- very commonly just planning techniques get incorporated rather than knowledge on strategic actions;

\- advances in DP-based collaborative systems are still slow.

## 6. Future developments

In the following three trends are emphasized which we assume are essential for future SDSS development: (1) further improvements of DSS generators, (2) incorporation of knowledge-based approaches, and (3) orientation towards group decision-making.

## 6.1. Improvements of DSS generators

The existing tools for generating computer-based planning systems must be further improved $[23]$ . The development of menu-driven applications and the use of all facilities still require an extensive training for SDSS developers.

DSS generators are designed for input and manipulation of quantitative data. They incorporate functions for operational control rather than for strategic planning. Up to now DSS generators do not support problem formulation and problem structuring. Also, graphical and natural language techniques are to be integrated. The access to data bases, especially to external data bases, must become much easier.

The long-term perspectives, however, are promising. The trends in information technology include an increasing interconnectivity on various technical levels, easy-to-use user interfaces, and simplified programming techniques such as object orientation and card technology.

## 6.2. Enhancements of SDSS by knowledge-bases

Another promising approach for enhancing the capabilities of SDSS is the combination of conventional DSS with knowledge-based systems $[14]$ . A knowledge-based SDSS might support the strategic planning process in different ways, such as the choice and explanation of

\- adequate planning instruments for certain strategic decision situations,

\- internal and external databases, or

\- appropriate software packages to be used for specific planning tasks.

However, most knowledge processing systems still require substantial programming skills.

## 6.3. Group decision support in strategic planning

The strategy development process needs the coordination and agreement of several persons $[19,27]$ . Furthermore presentations and discussions take place in conferences. Therefore computerized systems are relevant which support the decision process of groups. These Group Decision Support Systems (GDSS) will become more and more important in the near future because of the boom of networking and the necessity for sophisticated communication/discussion software.

Strategic planning is group decision-making. In a GDSS environment typically a group of executive planners work interactively using a network of hardware and software to cover various aspects of the planning process. GDSS can be used for a variety of planning tasks, e.g. idea generation and evaluation, setting goals and objectives, evaluation of alternative strategies, stakeholder analysis, identifying assumptions and voting [10].

In the literature a couple of running GDSS and experiments in collaborative systems are described [e.g. 9,35]. These systems have to be developed towards communication support systems [6].

## 7. Conclusions

Success factors of strategic decision-making are human intuition and judgement, management experience, and creativity. In this paper we investigated how DSS technology can be helpful within the strategic planning process.

A central requirement for SDSS implementation is a truly integrated architecture. The variety of planning instruments has to be integrated as well as the corresponding data flows.

It has been demonstrated that financial modelling languages are useful for implementing strategic stand-alone applications and for integrating these applications. As an example, we presented StratConsult - a prototype of a computer-based planning system for strategic decision support. By use of SDSS the process of strategy development becomes far more transparent and efficient.

The combination of strategic planning with DSS technology is a relatively new approach. It can substantially increase the strategic sessions' effectiveness. Careful design is essential to ensure the full benefits of SDSS applications. Further advances in DSS research and information technology will give new impulses for successful SDSS developments.

## References

[1] L.M. Applegate, B.R. Konsynski, and J.F. Nunamaker, Model Management Systems: Design for Decision Support, in: Decision Support Systems 2, 1986, pp. 81–91.

[2] G. Ariav and M.J. Ginzberg, DSS Design: A Systematic View of Decision Support, Communications of the ACM 28, 1985, No. 10, pp. 1045–1052.

[3] S.E. Bodily, Modern Decision Making, New York: McGraw Hill, 1985.

[4] R.H. Bonczek, C.W. Holsapple, and A.B. Whinston, Foundations of Decision Support Systems, New York: Academic Press, 1981.

[5] G.M. Brooke and N.M. Duffy, The Use of Financial Modelling in Strategic Planning, Information and Management 11, 1986, pp. 13–24.

[6] L.C. Charalambides, Designing Communication Support Systems for Strategic Planning, Long Range Planning 21, 1988, No. 6, pp. 93–101.

[7] C.H. Chung, J.R. Lang, and K.N. Shaw, An Approach for Developing Support Systems for Strategic Decision Making in Business, Omega 17, 1989, No. 2, pp. 135–146.

[8] F.R. David, Computer assisted strategic planning in small

business, Journal of Systems Management 36, 1985, pp. 24–34.

[9] A.R. Dennis, A.R. Heminger, J.F. Nunamaker, Jr., and D.R. Vogel, Bringing Automated Support to Large Groups: The Burr-Brown Experience, Information & Management 18, 1990, pp. 111–121.

[10] A.R. Dennis, J.F. Nunamaker, Jr., D. Paranka, and D.R. Vogel, A New Role for Computers in Strategic Management, Journal of Business Strategy, II, 1990, No. 5, pp. 38–43.

[11] C. Eden, Strategic Thinking with Computers, Long Range Planning 23, 1990, No. 6, pp. 35–43.

[12] P. Finlay, Computer Packages in Financial Modelling, in W. Bryant (ed.), Financial Modelling in Corporate Management, 2nd edition, Chichester: John Wiley, 1987, pp. 59–70.

[13] P. Fredericks and N. Venkatraman, The Rise of Strategy Support Systems, Sloan Management Review 29, 1988, No. 3, pp. 47–54.

[14] M. Goul, On Building Expert Systems for Strategic Planners: A Knowledge Engineer's Experience, Information and Management 12, 1987, pp. 131–141.

[15] F. Hanssmann and D. Meyersiek, EDV-Einsatz im strategischen Management, in H.A. Henzler (ed.), Handbuch Strategische Führung, Wiesbaden: Gabler, 1988, pp. 717–741.

[16] A.C. Hax and N.S. Majluf, Strategic Management: An Integrative Perspective, Englewood Cliffs/N.J.: Prentice-Hall, 1984.

[17] P.K. Hough and N.M. Duffy, Top Management Perspectives on Decision Support Systems, Information and Management 12, 1987, pp. 21–31.

[18] M.T. Jelassi, K.A. Williams, and C.S. Fidler, The Emerging Role of DSS: From Passive to Active, Decision Support Systems 3, 1987, pp. 299–307.

[19] L.M. Jessup and S. Kukalis, Better Planning Using Group Support Systems, Long Range Planning 23, 1990, No. 3, pp. 100–105.

[20] P.G.W. Keen and M.S. Scott Morton, Decision Support Systems: An Organizational Perspective, Reading/Mass.: Addison Wesley, 1978.

[21] W.R. King, Planning for Strategic Decision Support Systems, Long Range Planning 16, 1983, No. 5, pp. 73–78.

[22] S.K. Marrus, Building the Strategic Plan: Find, Analyze, and Present the Right Information, New York: John Wiley, 1984.

[23] J. Moormann, Strategische Planung mit DSS-Generatoren, Munich: Florentz, 1989.

[24] E. Plattfaut, DV-Unterstützung strategischer Unternehmensplanung, Berlin: Springer, 1987.

[25] M.E. Porter, Competitive Strategy, New York: Free Press, 1980.

[26] J.E. Prescott and J.H. Grant, A Manager's Guide for Evaluating Competitive Analysis Techniques, Interfaces 18, 1988, No. 3, pp. 10–22.

[27] M.A. Rathwell and A. Burn 'Information Systems Support for Group Planning and Decision-Making Activities, MIS Quarterly 9, 1985, pp. 255–271.

[28] B.C. Reimann, Decision Support Systems: Strategic Management Tools for the Eighties, Business Horizons 28, 1985, No. 5, pp. 71–77.

[29] R. Sabherwal and V. Grover, Computer Support for Strategic Decision-Making Processes: Review and Analysis, Decision Sciences 20, 1989, pp. 54–76.

[30] K.B.C. Saxena and M. Kaul, A Conceptual Architecture for DSS Generators, Information & Management 10, 1986, pp. 149–157.

[31] H. Simon, The New Science of Management Decision, New York: Harper and Rowe, 1960.

[32] R.H. Sprague, A Framework for the Development of Decision Support Systems, MIS Quarterly 4, 1980, No. 4, pp. 1–26.

[33] R.H. Sprague, Jr. and E.D. Carlson, Building Effective Decision Support Systems, Englewood Cliffs/N.J.: Prentice-Hall, 1982.

[34] C.B. Stabell, Decision Support Systems: Alternative Perspectives and Schools, in E.R. McLean and H.G. Sol (eds.), Decision Support Systems: A Decade in Perspective, Amsterdam: Elsevier Science, 1986, pp. 173–182.

[35] M. Stefik, G. Foster, D.G. Bobrow, K. Kahn, S. Lanning,

and L. Suchman, Beyond the Chalkboard: Computer Support for Collaboration and Problem Solving in Meetings, Communications of the ACM 30, 1987, No. 1, pp. 32–47.

[36] R.J. Thierauf, User-Oriented Decision Support Systems, Englewood Cliffs/N.J.: Prentice-Hall, 1988.

[37] E. Turban and P.R. Watkins, Integrating Expert Systems and Decision Support Systems, MJ's Quarterly 10, 1986, pp. 91–98.

[38] P. Waalewijn and R. Boulan, Strategic Planning on a Personal Computer, Long Range Planning 23, 1990, No. 4, pp. 97–103.

[39] M.S. Wang and K. Yu, An Investigation on the Nature of Decision Support System Software, Decision Support Systems 3, 1987, pp. 277–288.

[40] S. Yoo and L.A. Digman, Decision Support System: A New Tool for Strategic Management, Long Range Planning 20, 1987, No. 2, pp. 114–124.
