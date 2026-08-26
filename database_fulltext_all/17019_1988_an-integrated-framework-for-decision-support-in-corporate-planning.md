---
otero_id: 17019
otero_key: "FVCCAPPA"
title: "An integrated framework for decision support in corporate planning"
authors: "R. Ramesh; G.Chandra Sekar"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90023-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Integrated Framework for Decision Support in Corporate Planning

R. RAMESH and G. CHANDRA SEKAR

Department of Management Science & Systems, School of Management, State University of New York at Buffalo, Buffalo, New York 14260, USA

Corporate planning and decision making is a complex but critical management process in multidivisional organizations. This process entails a determination of the objectives and operational constraints at various levels of management. The decision-making function in such large diversified corporations proceeds by assessing the decision alternatives at each level of management with reference to their mutual tradeoffs, and arriving at an equilibrium point. In this paper, we develop a conceptual framework for the design of an integrated DSS in hierarchical organizations. The proposed framework consists of five steps: Analysis of the corporate decision making process, building a model of the decision making process, configuring a DSS for this model, pilot study and implementation. We illustrate the proposed design principles by considering a three-level hierarchical organization and modeling the decision-making process within this organization. A case analysis of the proposed integrated framework is provided. The case study has been conducted with decision makers in a simulated business environment. This research has given rise to several new avenues of exploration and extensions of the proposed design. We present the conclusions from this study and directions for future research in this area. Our experience with this approach in the case analysis has been quite positive, and this suggests that similar results may be obtained in real world organizations as well. We are currently testing the proposed approach with a local organization.

Keywords: Decision Support Systems, Corporate Planning, Corporate Decision Making, Hierarchical Decision Systems, Corporate Information Systems.

## 1. Introduction

The essential components of the management process in a business environment are Analysis, Planning, Decision-making and Control, respectively. Corporate strategic planning is a central management process that integrates these components with regard to the different functional areas, as well as the business environment as a whole. In this process, the top management evaluates its strategies by identifying the opportunities and threats in the business environment, and by analyzing its resources to determine its own strengths and weaknesses. The management process consists of drawing up different courses of action, evaluating them against the company's long-term as well as short-term objectives, deciding on an appropriate course and implementing the decisions. This process can be considered within the hierarchy of an organization as follows. The corporate objectives, both long-term and short-term are defined at the top management level, which is the strategic level. In defining these objectives, the top management takes into account its resource restrictions, and the opportunities and threats in the business environment. Within the framework of the corporate objectives, the tactical goals are defined at the next level of management, which is the tactical level. The tactical goals are then translated into specific operational tasks at the bottom management level, which is the operational level. In this hierarchy, the functions of analysis, planning, decision-making and control are carried out at each level. This is accompanied

![](/api/attachments/FVCCAPPA/fulltext/images/672920d19a7f986051050d4361c5032e1423281351519240ba975fb62400b3e5.jpg)

R. Ramesh is an Assistant Professor in the Department of Management Science and Systems, School of Management at SUNYAB. He obtained his Ph.D. in Operations Research from the State University of New York at Buffalo. His areas of specialization include mathematical programming, combinatorial optimization, database theory and optimization. His publications appear in ACM Transactions on Database Systems, Naval Research Logistics, European Journal of Operations of Operations Research.

Research and Annals of Operations Research.

![](/api/attachments/FVCCAPPA/fulltext/images/259bfce2cfa00b3ba1c46ce3c96c504d1bdcde41b33ffc88005827dd847ebd40.jpg)  
G. Chandra Sekar is an Assistant Professor in the Department of Management Science and Systems, School of Management at SUNYAB. He holds a Ph.D. from State University of New York at Buffalo. He won the General Electric award for best dissertation in Strategic Planning for 1981. He is actively involved in consulting and research in planning and information systems. His publications appear in strategic planning and information systems journals.

by a vertical as well as horizontal flow of information in the hierarchy.

In this paper, we model the planning and decision-making process in a hierarchically structured organization as above, and develop the framework for a comprehensive decision support system to integrate the objectives, constraints and decisions at various levels of management, and to provide for a real-time base to facilitate efficient information transfer. To begin with, we present a review of relevant literature in this area, in the following discussion.

Literature on strategic planning and control is vast and extensive. Gershefski [6] surveys the set of corporate models used in strategic planning. He notes that the primary aim of these models is the generation of timely, accurate and economical planning information. Brown [1] develops a model for corporate planning at the Xerox Corporation to identify the financial implications of alternative marketing and production strategies under different environmental conditions. Dickson et al. [4] suggest the integration of optimization models in the corporate planning system to improve the quality of managerial decision-making. Hamilton and Moses [7] describe a computer-based corporate planning system which combines the analytical power of optimization with simulation capabilities and more specialized planning models. Seaberg and Seaberg [17] describe a corporate decision-aiding system incorporating a family of time-shared models developed for Xerox Corporation, in an effort to link the functional areas for communication, planning and control purposes. Srinivasan and Schoenfeld [19] discuss the implementation problems associated with corporate-wide information systems. Vancil and Lorange [21] analyze the strategic planning process in complex diversified companies and present a conceptual framework for modeling the decision process. Other important models in the strategic planning area include gargabe-can models (Mouzelis [14]), incremental logical input models (Quinn [16]) and multiobjective decision models (Chandrasekar and Ramesh [3]).

In all the above models, different facets of the corporate planning process are considered. Several schemes for the classification of these facets have been used (Hofer and Schendel [8], Keen and Scott Morton [11], and Srinivasan and Schoenfeld [19]). In this research, we broadly classify these facets according to the flows within an organization using the conventional practice for the design of management information systems (Tom De Marco [20]). These flows are the data flow, decision flow, control flow and communication flow, respectively. A comprehensive approach to the design of a corporate DSS should integrate these flows. In a hierarchical organization these flows are well defined and structured, thereby facilitating the design of efficient integrated support systems. On the other hand, in a matrix form of organization used typically in R&D units, these flows are not so well ordered due to its organizational dynamics. Several additional considerations arise in this case. Therefore, we focus on hierarchical, production-oriented organizations in this paper. We present below, the attributes of an effective DSS for corporate planning, which form the basis of the proposed design.

## 1.1. Data Flow

Information is critical to the planning and decision making functions in an organization. A comprehensive DSS should include the organizational information system and integrate the vertical and horizontal flow of data by providing timely, accurate and economical reports and control the flow through database security functions.

## 1.2. Decision Flow

Corporate decision-making situations usually involve multiple conflicting objectives, and in many cases, could also involve several decision makers. Furthermore, decisions at different levels and also within the same level could interact, resulting in tradeoff optimization situations. Therefore, an adequate DSS should provide appropriate modeling capabilities, systems for the accurate estimation of problem parameters, and efficient solution strategies for the decision models.

## 1.3. Control Flow

In a hierarchical organization, control flow is vertical. The control data flows downwards, and the feedback information flows upwards. An efficient DSS should integrate these flows and provide for accurate and timely reporting of control and feedback information at appropriate decision centers. Furthermore, it is important to ensure the security and privacy of the information transacted in this process.

## 1.4. Communication Flow

An efficient DSS should also incorporate appropriate communication systems to facilitate interaction between various corporate units, and thus enable the other flows discussed above. The communication system should be tailored to the structure and the needs of the organization.

## 2. An Integrated DSS Framework

Large diversified corporations that employ a product or area based divisional structure are usually hierarchically organized. In such organizations, decision making is decentralized, and is composed of responsibility centers. In highly structured organizations, the level of formal planning and decision making is usually high. Hence, it is possible in such organizations to use sophisticated DSS, which could encompass and integrate the organizational information system. The proposed design of a DSS for such organization consists of the following steps:

(1) Analyze the organizational structure and the decision making process. In this step, we identify the decision centers and the decisions made at these centers. The inputs, processing mechanisms and the outputs of each decision task are then identified. The interactions between the decision centers with regard to their respective decision processes are determined. Using an appropriate representation such as a decision/activity flowchart, the overall planning and decision making process is determined.

(2) Model the decision making process. In this step, we determine the objectives and the constraints on the decisions at each decision center. The corporate structure is then considered according to the levels of a hierarchy, and decision models for each level are developed. The inputs and outputs of these models are then linked and integrated according to the decision making process identified in Step 1.

(3) Configure and design the DSS. The DSS comprises of a modelbase, database and the supporting information system.

(4) Conduct a pilot study using the DSS. This study will reveal the strength and weaknesses of the DSS. Several approaches have been used to conduct the pilot study (see Cerveny et al. [2], Naumann and Jenkins [15], Sprague and Carlson [18]). Based on this study, repeat Steps (1), (2) and (3) until the design is satisfactory.

(5) Implement the DSS.

## 2.1. Analysis of Organizational Structure and Decision Making

This analysis is specific to the organization in consideration. We illustrate this step by considering a hierarchical organization composed of three levels: top management, divisions and departments within a division, respectively. The top management conducts corporate planning and makes decisions on corporate strategies. The corporate decisions include resource allocation to the divisions based on its expectations of divisional performance. The divisions are responsible for the business, and perform business planning subject to resources available and the corporate expectations. A division controls the departmental resources and lays down the departmental goals. The departments perform functional planning and execute their plans. For the sake of simplicity, we consider three departments in this analysis: production, marketing and finance, respectively. Addition of more departments will only expand the corporate structure laterally, and the analysis will still be applicable.

The planning and decision making functions at the various levels interact. This interaction takes place under both formal and informal circumstances. Fig. 1 presents a representation of the overall planning and decision making process under consideration.

Fig. 1 reveals the decision centers within the corporation, the nature of their planning and decision making processes and their interaction. A model of the decision making process is developed from a study of the characteristics of this system. The characteristics of the system under consideration are as follows:

![](/api/attachments/FVCCAPPA/fulltext/images/45c604c17e0c76ccd82af937c4ff88cffec4476c27793330e370caefa6e363d8.jpg)  
Fig. 1. Corporate Planning and Decision Making Process.

(i) The system has interacting decision making units within a hierarchical organizational structure.

(ii) Each subordinate level determines its optimal decisions subject to the decisions of the superior levels.

(iii) If a subordinate level determines that no feasible solution can be found for its decision problems subject to the decisions of its superior levels, or if the solutions are not acceptable with respect to its own expectations, then it negotiates with the immediate superior level.

(iv) Each unit maximizes net benefits independent of other units, but may be affected by the actions and reactions of those units.

(v) The effect of an unit's decisions on the other units in the system can be reflected in both their objectives and the set of feasible decision alternatives.

In the above scenario, a planner at a given level has his objectives and decision space influenced by those of others in the system, and in return, he influences theirs through the control instruments at his disposal.

## 2.2. A Model of Corporate Decision Making

We model the above decision process within the framework of a multilevel, multiobjective planning system. The model consists of three levels of optimization and two levels of negotiations, respectively. This is shown in fig. 2.

The optimization at each level usually involves multiple conflicting objectives. The optimization problems are solved by evaluating the tradeoffs among the objectives by the decision makers at each level. The negotiations between two levels result in modifications to the tradeoff structures among the objectives at the respective levels, leading to reoptimization at each level. This is an iterative process, and it terminates when a mutually acceptable plan is reached. The optimizations and the negotiations constitute the decision process illustrated in fig. 1.

The corporate optimization covers the entire range of operations in the company. The corporate objectives can be broadly specified in terms of its desired market share in the industry, level of production, return on assets, return on its total financial portfolio and its stock value. The corporate decisions represent their expectations on the divisional outputs in the respective functional areas. These decisions are constrained by the company's resources, the economics of the business environment, behavior of the industry and other legal and governmental factors. Appendix 1 provides a model of the corporate optimization problem.

The divisional optimization covers the operations within a division. The divisional goals are formulated from the corporate expectations. These goals include the level of production and sales in a given period, the production and selling costs, working capital usage and return on assets. The divisional decisions represent specific plans and strategies for the departments under its control. The departmental optimizations are based on the decisions made at the divisional level and result in specific operational plans. Several decision models may be used at this level.

![](/api/attachments/FVCCAPPA/fulltext/images/a0edfd3b4331ab514aecefec2399685fb686c698e59acd7ca20766cd11d93421.jpg)  
Fig. 2. A Multilevel Multiobjective Model of the corporate Planning and Decision Making Process.

![](/api/attachments/FVCCAPPA/fulltext/images/8c9ba6ff3c103e42935b5a240f6abb9b1baf18480170d1ba34985d25163d08a9.jpg)  
Fig. 3. DSS Architecture

In this model, the resources at a given level are controlled by its superior levels. The negotiations between levels lead to working strategies in terms of resources and expectations. Clearly, underlying these negotiations is the political reality of the organization (see Mouzelis [14] and Quinn [16]). A negotiated decision depends on several organizational and individual factors such as the resource restrictions, criticality of the business and the organizational power structure. Therefore, given the transient nature of business, reaching a negotiated agreement does not ensure an overall business optimization. Since this political reality is unavoidable, the role of an integrated DSS is only to facilitate an efficient analysis of the various decision alternatives and their consequences at different levels of management.

## 2.3. DSS Architecture

The proposed DSS architecture consists of five components. A modelbase, a database, a data-access component, an optimization component and an interactive component. The architecture is illustrated in fig. 3.

The modelbase is organized into three modules: Corporate module, Divisional module and Departmental module. The corporate module consists of the company-wide multicriteria decision model and is accessible to authorized corporate users only. The divisional module consists of the divisional multicriteria models and is accessible to the divisional heads. The departmental module consists of several models that are used to make decisions in the functional areas. These are general purpose optimization models and are accessible to all authorized company users. The database is organized into three levels: Corporate data, Divisional data and Departmental data. These levels represent various degrees of detail and consolidation. Access to the modelbase and the database is controlled through system security devices. The data-access component of the DSS provides a request-permission protocol for this purpose.

The optimization component is used to assemble the appropriate models from the modelbase and the relevant data from the database to solve a given decision problem. This component is also used to perform sensitivity analyses and consequence projections on various decision alternatives. The interactive component also serves two purposes. First, it enable a decision maker to interact with a model when it is solved interactively. The multiobjective decision problems are solved interactively by assessing the decision-maker's preference structure (see [12] [13] [23]). Second, it serves as a medium to present analyses and results to a group of decision makers during a negotiation session. The optimization and the interactive components together perform the functions of a facilitator in the negotiation process.

The above DSS configuration can be implemented using a central computer or in a distributed environment. In the distributed case, several additional considerations such as distribution the database and the modelbase, security and integrity issues, and establishing appropriate communication links arise. This is a promising area for future research.

## 3. A Case Analysis

In this section, we describe an organizational decision process in which the integrated DSS approach can profitably be employed. The simulated organization used in this study is contained in the management game described in Jensen and Cherrington [9]. The participants in the game are required to have sufficient knowledge of the management techniques needed to solve practical strategic planning problems. Accordingly in our study, the participants have been drawn from the final-year graduating M.B.A. students at the State University of New York at Buffalo. The management game consists of eight firms competing in an industry marketing two products in two geographic areas. Teams of three members manage each firm and are responsible for the entire operations – marketing, production, financial and materials planning. The teams run their firms for 1 to 2 years and make strategic operational decisions on a quarterly basis. The actual performance is obtained by executing all the decisions of all firms by the game administrator. The overall evaluation of the teams is based on how well they perform on market share of each product in each area, net income and share price. These performance measures constitute the multiple objectives in the decision making problems faced by the managers of the firms. The decisions in this situation include company strategies and short term plans and are based on a sales forecasting analysis, production planning analysis and financial analysis. Each team has to make 57 decisions in each quarter covering the marketing, finance and production functions. The industry environment is controlled by the game administrator, and the teams develop appropriate strategies in response to the industry reactions to their earlier decisions.

The members of each team are organized into three levels: Corporate level (president of the company), divisional level (divisional managers for each product-area combination) and the departmental level (marketing, production and finance). The planning at the corporate level is concerned with the determination of organizational objectives, business portfolio and resource availability. At the divisional level, planning is focussed on business development for each product-area segment. The detailed functional planning is carried out at the departmental level. At the corporate level, the teams attempt to optimize among the competing objectives of market shares, income and share price. Implicitly, this brings the competing requirements of the four divisions into the picture. A multicriteria decision model based on the framework given in appendix 1 is used for this purpose. Similarly, the divisions develop their plans by optimizing their competing marketing, finance and production objectives. The departmental managers use several planning and resource scheduling models.

The negotiations between a division and top management are conducted within the DSS environment. The two models provide the positions of the respective bargaining units with support analysis provided by the departmental projections and the consequence analysis component of the DSS. When mutual agreement is reached concerning the parameters of the corporate and divisional models, the models are reoptimized to determine the final corporate strategies and the divisional business plans. At the end of the game, a majority of the participants felt that the DSS environment was very helpful in analyzing the decision alternatives as well as facilitating their negotiations. This shows that the proposed approach is a promising avenue for designing DSS for real world situations.

## 4. Conclusions and Implications

Corporate strategic planning is a complex but critical management process for multidimensional organizations. This activity determines the objectives for the organization, portfolio decisions including resource allocations and sets the pattern for future development. In this process, there is a substantial conflict between corporate objectives themselves, between divisional interests and corporate objectives, and between departmental interests and divisional goals. Therefore, corporate decision making requires a deft integration of human inputs in the corporate structure, efficient analysis of various courses of action, and facilitation of the negotiation process. We have conceptualized a decision support system for corporate decision making with these objectives in view.

In this paper, we have developed a framework for an integrated DSS which supports organizational planning at various levels of management. The specific details of DSS design and implementation in real world organizations will be contingent upon the organizational and environmental factors. However, the framework proposed here can be followed with appropriate modifications according to these factors. We summarize the steps in designing a DSS using the proposed framework as follows:

(1) Determine the organizational structure. Identify the decision centers and the decisions made at these centers. Develop a decision/activity flowchart of the decision process which links the decision centers and shows the interactions between them.

(2) Determine the objectives and the constraints on the decisions at each decision center. In a hierarchical organization, this process is carried out using a top-down approach, starting from the top level decision center. Model the decision processes at each level, and integrate the models by linking the inputs and outputs between the models at different levels. Thus, a comprehensive model structure of the overall decision process is developed.

(3) Design a DSS for the above model structure. This DSS consists of five components: a modelbase, a database, a data access component, an optimization component and an interactive component.

(4) Conduct a pilot study and refine the design based on this experience.

(5) Implement the DSS.

In this research, we have developed a DSS based on the above framework for a corporate planning game and tested it using a simulated environment. We have experimented extensively with this system, and have refined our approach from our experience over the years. Our experience has been quite positive, and it shows that the proposed approach can be used as a basis for designing integrated DSS in real world hierarchical organizations that involve multilevel, multicriteria decision making. We intend testing this approach with a local organization. This implementation will help to validate the approach suggested.

There are several research issues that arise from this work. We address these issues from the perspective of the appropriateness of a DSS to a given decision process and its effectiveness. The appropriateness can be assessed in terms of the adaptability of a DSS to a decision process and the representativeness of the models that may be used in the DSS of the underlying real-world situation. The effectiveness can be assessed in terms of the improvement in the quality of decisions and the user satisfaction. The approach developed in this paper addresses structured organizations and the DSS is built from an initial development of mathematical models for various decision-making units and their integration within an overall framework. This approach gives rise to the following research questions:

(a) How flexible should the design be in order to accommodate changes in the organizational structure, the environmental factors and the decision making process itself? What critical factors affect the adaptability of the DSS to changing conditions? What are the cost/benefit tradeoffs between building a flexible, generalized DSS and a specialized DSS using this approach for an organization?

(b) Can we adopt some of the multilevel planning models discussed in the literature ([5][22])

within the DSS framework developed in this paper? Can we build mathematical models of the group decision making process so that the DSS can also direct, apart from facilitating the negotiations? What are the mathematical and organizational limitations of such an approach?

(c) How does user-involvement in the design of the proposed DSS affect its performance and user satisfaction? What should be the role and contribution of the user in the design process? How should the pilot study be conducted and what are the user's contributions at this stage? What issues must be considered in converting the current system to the DSS-environment? What are the hardware and software implications?

(d) Several approaches have been recommended in the literature for building a DSS (see Keen [10], Keen and Scott Morton [11] and Sprague and Carlson [18]). A cross-sectional study of these methods and the proposed method for a chosen organization will reveal their respective characteristics in terms of complexity of the analysis and design process, and the time and costs involved in designing a DSS under the given situation. This study could also provide an a priori assessment of the validity and performance of a DSS for the organization. We believe that an integrated approach as developed in this paper is essential to support complex group decision making processes in organizations. Conducting this study over several organizations could lead to generalizations concerning the characteristics of the various approaches. Furthermore, the organizational and environmental factors that affect the choice of a design approach can also be assessed from this study. This could lead to prescriptive models for a design approach for various types of organizations. Based on this, a taxonomy of DSS design methodologies according to the critical organizational and environmental parameters that affect the design can be developed.

We plan to investigate some of the above research questions in our study of a local organization.

## Appendix 1

A Model of the Corporate Optimization Problem

"Maximize"

1. Market share of each product in each area of operation

2. Net income

3. Stock value

## Subject to:

1. Marketing constraints

\- bounds on market shares

\- pricing constraints

\- budget constraints on product promotion

\- constraints on sales management costs
- others

2. Production constraints

\- production capacity constraints

\- inventory budget constraints

\- labor budget constraints

\- overhead restrictions

\- others

3. Financial constraints

\- limits on borrowings

\- limits on expenses

\- others

4. Industry environment constraints

\- overall demand constraints

\- constraints from the overall competitive market behavior

\- constraints on operational leverage
- others.

The term “maximize” is shown within quotes because it is a multiobjective optimization problem. The decision variables in this model can be broadly classified as production variables, marketing variables and finance variables pertaining to each division. The values of these variables represent the top-management’s expectations on the performance of the divisions. The parameters of this model are determined from industry data as well as broader environmental data using statistical and simulation techniques. Table 1 lists some of these parameters. Similarly, Table 2 lists some of the parameters used in divisional level optimiza-

Table 1  
Parameters in Corporate Level Optimization.

<table><tr><td colspan="3">Industry Parameters</td><td colspan="3">Environmental Parameters</td></tr><tr><td>Market</td><td>Industry Conditions</td><td>Supply</td><td>Economic Conditions</td><td>Demographic Trends</td><td>Socio-technological Trends</td></tr><tr><td>Size</td><td>Product differentiation</td><td>Raw material availability</td><td>GNP trends</td><td>Population growth rate</td><td>R&amp;D expenditure</td></tr><tr><td>Overall growth</td><td>Barriers to entry</td><td>Balance of supply and demand</td><td>Interest rates</td><td>Age distribution</td><td>Patent protection</td></tr><tr><td>Segmentation</td><td>Economies of scale</td><td>Supplier location</td><td>Money supply</td><td>Regional shifts</td><td>Lifestyle changes</td></tr><tr><td>Segment growth rates</td><td>Capacity utilization</td><td>Cost trends</td><td>Unemployment levels</td><td>Life expectancy</td><td>Tax laws</td></tr><tr><td>Distribution channels</td><td>Industry profitability</td><td>Import/export conditions</td><td>Energy availability</td><td>Birth rates</td><td>Other governmental regulations</td></tr></table>

## Table 2

Parameters in Divisional Level Optimization.

<table><tr><td>Production Parameters</td><td>Marketing Parameters</td><td>Finance Parameters</td><td>Division Environment Parameters</td></tr><tr><td>Number of Plants</td><td>Product types</td><td>Material Cost</td><td>Competing organizations</td></tr><tr><td>Average capacity</td><td>Pricing policies</td><td>Labor cost</td><td>Concentration of competitors</td></tr><tr><td>Capacity utilization</td><td>Distribution</td><td>Administrative expenses</td><td>Overall production strategy</td></tr><tr><td>Newness of plants</td><td>Marketing expenditure</td><td>Overall marketing expenses</td><td>Overall marketing strategy</td></tr><tr><td>Length of production cycle</td><td>Advertising expenditures</td><td>Expansion plans</td><td>Overall finance strategy</td></tr><tr><td>Capital intensity</td><td>Market share</td><td>Receivable/payables</td><td>Labor union parameters</td></tr><tr><td>Labor intensity</td><td></td><td>Audit/control parameters</td><td></td></tr><tr><td>R&amp;D expenditure</td><td></td><td></td><td></td></tr><tr><td>QC expenditure</td><td></td><td></td><td></td></tr></table>

tion. These parameters are also determined using statistical and simulation techniques.

## References

[1] Brown D.E., The Xerox Planning Model, presented to the American Management Association Seminar on Corporate Financial Models and Management Decision Making (December, 1968).

[2] Cerveny, R.P., Garrity, E.J. and Sanders, G.L., The Application of Prototyping to Systems Development: A rationale and Model, Journal of MIS, Vol. III (1986) pp. 52–62.

[3] Chandrasekar, G. and Ramesh, R., Microcomputer-Based Multiple Criteria Decision Support Systems for Strategic Planning, Information and Management, Vol. 12, No. 4 (1987) pp. 163–172.

[4] Dickson, G.W., Mauriel, J.J. and Anderson, J.C., Computer Assisted Planning Models: A Functional Analysis, in: A.N. Schrieber, ed., Corporate Simulation Models, University of Washington, Seattle, Washington (1970).

[5] Dirickx, Y.M.I. and Jennergren, L.P., Systems Analysis by Multilevel Methods: With Applications to Economics and Management, John Wiley, New York (1979).

[6] Gershefski, G., Corporate Models – The State of the Art, Management Science, Vol. 16, No. 6 (1970).

[7] Hamilton, W.F. and Moses M.A., A Computer-Based Corporate Planning System, Management Science, Vol. 21, No. 2 (1974).

[8] Hofer, C.W. Schendel, D., Strategic Formulation: Analytical Concepts, West Publishing Company, St. Paul, Minnesota (1978).

[9] Jensen, R.L. and Cherrington, D.J., Participant's manual: Business Management Laboratory, BPI (1977).

[10] Keen, P.G.W., Adaptive Design for Decision Support Systems, Database, Vol. 1, No. 1, pp. 15–25 (1980).

[11] Keen, P. and Scott Morton, M., Decision Support Systems: An Organizational Perspective, Addison-Wesley, Reading, MA (1978).

[12] Keeney, R.L. and Raiffa, H., Decision With multiple Objectives: Preferences and Value Tradeoffs, John Wiley, New York (1976).

[13] Lee, S.M., Goal Programming for Decision Analysis, Auerbach, Philadelphia (1972).

[14] Mouzelis, N.P., Organization and Bureaucracy: An Analysis of Modern Theories, Aldine Publishing, Chicago (1977).

[15] Nauann, J.D. and Jenkins, A.M., Prototyping: The New Paradigm for Systems Development, MIS Quarterly, Vol. 6, No. 3 (1982) pp. 29–44.

[16] Quinn, J.B., Strategic Goals: Process and Politics, Sloan Management Review, Fall (1977).

[17] Seaberg, R.A. and Seaberg, C., Computer Based DEcision Systems in Xerox Corporate Planning, Management Science, Vol. 20, No. 4 (1973).

[18] Sprague, R. and Carlson, E., Building Effective Decision Support Systems, Prentice-Hall, New Jersey (1982).

[19] Srinivasan, C.A. and Schoenfeld, H.M., Some Problems and Prospects in Design and Development of Corporate-wide Information Systems, Management International Review, Vol. 18, No. 2 (1978) pp. 15–31.

[20] Tom De marco, Structured Analysis and System Specification, Yourdon, Inc., New York (1978).

[21] Vancil, R.F. and Lorange, P., Strategic Planning in Diversified Companies, Harvard Business Review (January–February, 1975).

[22] Wendell, R.E., Multiple Objective mathematical Programming with Respect to Multiple decision Makers, Operations Research, Vol. 28, No. 5 (1980) pp. 1100–1111.

[23] Zionts, S. and Wallenius, J., An Interactive Multiple objective Linear Programming Method for a Class of Underlying Nonlinear Utility Functions, Management Science, Vol. 29, No. 5 (1983).
