---
otero_id: 17107
otero_key: "DNDYZHFB"
title: "Knowledge-based GDSS to support reciprocally interdependent decisions"
authors: "Mohan R. Tanniru; Hemant K. Jain"
year: "1989"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(89)90036-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Knowledge-Based GDSS to Support Reciprocally Interdependent Decisions

Mohan R. TANNIRU

School of Management, Syracuse University, Syracuse, NY 13210, USA

Hemant K. JAIN

School of Business Administration, University of Wisconsin-Milwaukee, Milwaukee, WI 53201, USA

Many organizational decisions require a consensus among a group of individuals representing different units or functions of an organization. The group members may disagree because they have incomplete information (uncertainty) and conflicting interests. The integration of tools and procedures for sharing of information (among individuals) in a Group Decision Support System (GDSS) can solve most of the disagreement caused by incomplete information and can set the stage for useful discussion and negotiation. The design of such a GDSS requires the establishment of a group decision making procedure which can assist in the negotiation and conflict resolution. This paper identifies the characteristics of a communication support facility that can enhance communication among group members based on the degree of their dependency. The role of a knowledge based approach to facilitate communication support when the group is reciprocally interdependent is illustrated using a financial budgeting example.

Keywords: Decision Support Systems, Group DSS, Expert System, Knowledge-based Systems, Information System.

## 1. Introduction

In an organization many important decisions such as strategic planning, financial budgeting and formulating marketing and production strategy are made essentially by groups of individuals. In such an environment people responsible for various organizational functions who possess different facts, expertise and points of view need to share information in order to arrive at a consensus-decision. Various approaches have been suggested to make this group decision making activity more effective and efficient. But, in general, the group decision process is not yet well understood in both descriptive theory (how groups make decisions) and prescriptive theory (rules for making rational group decisions) [14,15]. This situation contrasts with the state of a well developed theory of decision analysis within which rational individual decisions can be defined. In spite of the lack of a comprehensive theory, important research findings have gained acceptance by academics and practitioners of group decision making.

Organizations are said to achieve bounded rationality, i.e., arrive at satisfactory or locally optimal solutions, by defining a structure that identifies various individual member components and assigns each one distinct responsibilities to control resources, achieve local objectives, etc. [23]. In addition to providing bounded rationality, organizational structure must also facilitate coordinated

![](/api/attachments/DNDYZHFB/fulltext/images/1cbd2aa3566710ad1f6dff87ce3190d53da452530ee266298c044c904ddf7b9e.jpg)  
Mohan R. Tanniru is an Associate Professor of MIS at Syracuse University. He received his Ph.D. in 1978 from Northwestern University. He has published in a number of journals and presented papers at various meetings. His research interests are in systems analysis, decision support systems, and expert systems.

![](/api/attachments/DNDYZHFB/fulltext/images/42542dc90191e75da03ade7e26fe60dd814f806f1d00877e73c9bf2b3ae9b110.jpg)

anical Engineering from the University of Indore (India), a M. Tech in Industrial Engineering from I.I.T. Kharagpur, and Ph.D. from Lehigh University. He is a member of ACM, IEEE Computer Society and TIMS.

action among these interdependent components. However, the extent to which these components need coordination depends to a large degree on their relative interdependence.

Much of the research in DSS has addressed the need to support individual decision making styles and processes $[3,24]$ . Only recently has there been an interest in looking at support for decisions that are made by groups of individuals $[9,20]$ . Goncalves $[16]$ argues that the major difficulty in attempting to extend the notions of individual decision analysis to group decisions is the existence of disagreement caused by incomplete information (uncertainty) and conflicting interests among group members. The greater the interdependence among various organizational components, the more significant the need for effective communication among these components. Structured Management Techniques such as nominal group technique $[8]$ , the Delphi technique $[5]$ , and social judgment analysis $[7]$ provide communication protocols among participants in a decision making process.

The communication support has been identified as the first level of support, with modeling and decision coordination being the other two, that is necessary in the building of a Group Decision Support System (GDSS) [11]. However, the type of communication that is needed beyond a simple display of individual actions/preferences, requires an understanding of the type of interdependency that exists among various participating decision units. Thompson [28] identifies three levels of such dependency: pooled interdependency, sequential interdependency, and reciprocal interdependency; each requires different levels of communication support.

The objective of this paper is to illustrate how a knowledge based GDSS can support decision situations that exhibit reciprocal interdependency and to illustrate an implementation of this support within a financial budgeting environment. Section 2 will formulate some general characteristics of communication support for situations under reciprocal interdependency. The third section will introduce the reader to the financial budgeting environment as a group decision making process exhibiting reciprocal interdependency. The fourth section will show how a PROLOG based knowledge base can provide communication support in such group decision making situations, and the last section will illustrate an implementation of a knowledge based GDSS for financial budgeting.

## 2. A Communication Support Framework for Group Decision Making

A widely accepted view of the group decision making process in the literature posits two dimensions of decision making: task and social dimensions [14]. While the task dimension focuses on the work being performed by the group and how it is being done, the social dimension focuses on the relationship between the group members, and how they feel toward each other and about their membership in the group. One of the earlier attempts at supporting communication among group members electronically was the formation of decision rooms [17,18]. Several electronic based communication architectures were also proposed to support distinct types of group decision making [9]. Most of the models, linear as well as multiple sequence, that are discussed in the literature to explain group decision making emphasize the role of communication to collect, disseminate, and synthesize group preference information [14,19,22,29].

Thompson [28], in his study of organizations in action, describes three basic levels of interdependencies that may exist among various components of an organization and discusses how these dependencies require different levels of communication support. Table 1 briefly describes each of these interdependencies, the degree of coordination needed to support group decision making when such dependencies exist, and the appropriate communication support. Note that the sequential dependencies are characteristics of linear models, while multiple sequence models feature reciprocal interdependency.

Since reciprocal interdependency assumes the existence of sequential and pooled interdependencies, a communication facility to support reciprocal interdependency will also meet the needs of the other two. Based on the discussion in Table 1, the types of communication needed to support reciprocal interdependency are identified. Table 2 describes the communication support required for reciprocal interdependency.

While the actual implementation of this communication facility is problem dependent, one can generalize the characteristics of any system that

## Table 1

Characteristics of Interdependencies in Decision Making.

## Pooled Interdependence:

\- Each unit can perform its activities without regard to the other units and yet makes a contribution towards the organizational objective. Each unit is, in turn, supported by the organization.

\- Coordination among these units is standardized by establishing rules and routines. These rules have to be internally consistent and are applicable when the situation is stable and repetitive.

\- System that supports such coordination has to allow for communication of rules and routines that are applicable, and check for any internal inconsistency among the information that is being communicated.

Sequential Interdependence:

\- Each unit, while maintaining pooled interdependency to achieve overall organizational objectives, may also depend on other units to complete their normal operations. The degree of one unit's dependency on other units can vary significantly among units.

\- Coordination among these units is achieved with a plan, i.e., establishment of schedules for the sharing of information that governs each of their actions. The plan itself may be dynamic, i.e., changes with a change in the task composition of the organizational units.

\- System support here requires the establishment of individual unit's responsibilities, identification of their internal dependency based on these responsibilities, and communication of appropriate information to meet each of their operational objectives.

Reciprocal Interdependence:

\- Each unit, while remaining pooled and sequentially dependent, may be recursively dependent, i.e., output of a unit X become input of another unit, Y, and the output of unit Y may become input of another unit, Z, and, finally, output of unit Z may become input of unit X. In this case, each unit has to constantly adjust to the other units' activities, thus making the dependency relatively complex and dynamic.

\- Coordination is accomplished under these conditions through mutual adjustment. The more variable and unpredictable the situation, the greater the reliance on coordination by mutual adjustment.

\- A system that supports this type of dependency has to continually evaluate the significance of any new information with regard to its impact on various units and direct these units to take appropriate action.

## Table 2

Communication Support for Reciprocal Interdependency.

(a) facilitate sharing of rules/routines that guide the operations of each unit and ensure their consistent usage:

\- Is the individual unit information lexically correct, i.e., are the variables used known to the organization and do they convey same meaning to all involved? For example, variable “sales” may mean “until sales” for production and “dollar sales” to accounting.

\- Is the individual unit information logically correct, i.e., does it make sense to use certain information by a given unit in the context of a decision making process? For example, does it make sense to use “detailed sales data” when developing long term financial plans?

\- Is the use of certain relationships such as accounting identities consistent with normal practice? For example, did a unit use both earnings before tax and tax to derive earnings after tax?

\- Is there a consistency between the functional and organizational policies, i.e., if an organization has made certain decisions on goals, strategies, and priorities, is this information available to all concerned? For example, if an organization's strategy is to increase market share by cutting prices, then this information has to be conveyed to all units to allow them to synchronize their decisions with that of the corporation, i.e., marketing may use mass media advertising rather than selective magazine advertising, production unit may produce more items for stock rather than tighten inventories, and accounting unit may plan for an increase in cash outflow in the short run.

(b) dynamically plan, monitor, and control the communication support among units based on their operational interdependency.

\- Is there an internal dependency among various organizational units and, if so, is this dependency sequential and consistent? Here sequential dependency refers to the sharing between one unit's output and another unit's input and consistency refers to the nongeneration of output information by more than one unit.

\- Is the system capable of providing the dependency information when the dependency is not direct, i.e., output of unit "k" is needed as input to unit "m" via the input/output of unit "l". This dependency is referred to as the "control path" and is needed to study the impact of changes in policies associated with unit k on the outcome of unit m even though they don't share any information directly.

(c) dynamically plan and adjust the operations of each individual unit that participates in reciprocal interdependency.

\- Is there a reciprocal dependency among units, i.e., is there a sharing of both inputs and outputs of units, with or without any intervening units? If there are units in between the two units that are reciprocally interdependent, then what is the path that controls this dependency?

\- What type of communication mechanism is needed to manage the reciprocal dependency, i.e., what information is needed to decide on the acceptable convergence value of a parameter?

supports such a communication as follows. Let there be “n” units that, together, represent the organization. Each unit “i” has the responsibility to transform certain input information, I(i), to output information, O(i). In doing so, the unit may need access to certain organizational policies, procedures, protocols, etc., E(i), to ensure the internal consistency of the individual unit’s operations. The relative dependency of a unit on other units is a function of the overlap between the input information needs of one unit and the output information produced by another unit. The generic information set that is needed to support the reciprocal interdependency can be described as:

<table><tr><td>/* Established Organization-Wide Information */</td></tr><tr><td>established policies and guidelines variable relationships that are accepted organization wide synonym and reference information</td></tr><tr><td>/* Input and Output Information of Organizational Units */</td></tr><tr><td>input information of each unit output information of each unit</td></tr></table>

To support pooled interdependencies the global information that each unit has to know to perform its mission is provided. The input and output information of each unit is provided to identify any sequential as well as reciprocal interdependency. Next section discusses the financial budgeting problem and shows how it features reciprocal interdependency characteristics.

## 3. Interdependency Features in Financial Budgeting Decisions

Financial budgeting is the third stage of a three stage process used for corporate financial planning, the other two being the long-term and the short-term planning. The budgeting stage requires the estimation of revenues and expenditures for the upcoming period and these estimates are often used to monitor and control the performance of an organization. The estimation of the revenue and expenditure items and the resulting balance sheet and income statement items can be made in two different ways. One approach allows the corporate planner to relate the revenue and expenditure items with other revenue and expenditure items or some exogenous variables using past data. Once these relationships are established, projection of these can be made for a relatively short period of time and can be used as guidelines for operations during that period. This often is referred to as a top-down planning procedure.

Another approach to budgeting requires that each functional area determine the values of the revenue and expenditure items that are related to its operations. These are then consolidated to estimate various balance sheet ratios and income statement items. This approach is often referred to as a bottom-up approach to planning. It is, however, recognized that planning and budgeting processes are iterative in nature and require continual interactions between functional managers and the top management. Ackoff [1] refers to this as “interactive planning” and defines such an environment as one whereby both the corporate and functional area representatives are able to make decisions based on a reasonable understanding of the dynamics of the organization. For this interactive planning process to be effective, it has to be adaptive, future-oriented, participative, learning-oriented, integrated and coordinated [21].

The budgeting process, independent of which approach is used, needs such an interactive planning environment to arrive at a consensus that is acceptable to all the members (functional and corporate representatives) in the decision making process. In general, the financial budgeting process estimates the resources needed to move the financial state of an organization from its current state to the desired state during the next budget period, while remaining consistent with both short and long-term plans. Budget requirements are estimated by the functional units and tested against the corporate goals and objectives iteratively until a consensus is reached.

The corporate goals/objectives are communicated to all functional area units. They use these corporate objectives, outputs of related functional area units, and locally defined input parameters to determine their decision strategy. For example, the output of the sales unit (e.g., projected sales)

![](/api/attachments/DNDYZHFB/fulltext/images/0543f138ee21f1097e20aad9031393edbf4d809eb3a4612bb72cd68f08f0b4c2.jpg)  
Fig. 1. Functional and Corporate Decision Linkages.

will serve as an input to the production unit, and the output of the production unit (e.g., material and equipment needed) will be needed by the purchase unit. This is an illustration of sequential interdependency. In addition, the input of the sales unit may be “standard cost” which may be an output of the administrative unit, and the input variables of the administrative unit come from the production, purchase and sales units. This is an illustrative case of reciprocal interdependency.

Each functional unit, upon reaching a decision, transmits its output to the corporate unit and other related units. The corporate unit integrates the functional decisions and evaluates their impact on corporate goals/objectives. If this impact is not favorable, new information is sent to the functional units to modify their strategy, thus creating recursive dependency between functional units and the corporate unit. See Fig. 1 for an illustration of this dependency.

The long-term and short-term corporate goals and/or objectives, while expressed at times in terms of nonmonetary variables, i.e., 10% growth in sales or market share, expansion into some new production line, etc., eventually have to be expressed in financial terms (as functions of balance sheet and/or income statement items) for financial budgeting. Following are some critical ratios organizations use for strategy evaluation.

return on investment: (earnings before tax/ assets) $> = \mathrm{k}1$ ;

debt ratio: (long term debt/ assets) <= k2;

These critical ratios are often expressed as functions of balance sheet and income statement accounts.

The items of balance sheet, income statement and other accounting statements can be represented as a tree structure. The leaf nodes of this tree represent nonaggregate items such as cash, accounts receivable, and advertising expense, while nonleaf nodes such as current assets and liabilities represent aggregate items. Let S represent the financial state of the organization expressed in terms of critical ratios, L the set of leaf nodes and NL is the set of nonleaf nodes of the financial statement. Then the corporate model that aggregates the values of leaf nodes in set L to derive the values of nonleaf nodes in set NL and the financial state S of the organization is defined as a State Aggregation Model (SAM).

To see the impact of business decisions (set D) on financial states (S), one needs to convert the decision set D to a financial transaction set T which, in turn, will affect the leaf nodes in L. For example, “purchasing of equipment” results in a financial transaction “machinery cost” and this financial transaction affects the nodes “plant and equipment” and “long-term debt” if one acquires this equipment on loan. Similarly, selling of a product for cash results in a “cash sale” transaction which affects both “cash” and “sales revenue.”

The model that computes the values of the leaf nodes in L from the values of financial transactions in T is called the Transaction to Leaf Node Model (TLM) and the model that translates the values of the decision variables in D to the financial transactions in T is called the Decision is Transaction Model (DTM). Note that some of the business decisions are financial transactions themselves, in which case the functional mapping is one-to-one. For further information on these mappings, see Stohr and Tanniru [25] and Tanniru [26].

The next step is to define the exogenous and endogenous inputs needed by each functional area to arrive at the business decisions in set D. For example, the marketing area may obtain “standard cost” exogenously and define the demand function endogenously in order to estimate decision variables: unit sales, price, and credit factors. Each functional area represented in the group will define a Functional Area Model (FAM) to estimate the values of decision variables associated with that area. The definition of each FAM (transformation of the input variables into the output variables) will remain under the control of the functional area with its output information made available to other area members and the corporate unit as and when needed.

![](/api/attachments/DNDYZHFB/fulltext/images/e0d1053028a28b457ab9aceb1ab80017d68383882188927e0a349c6e9531bfce.jpg)  
Fig. 2. Mapping of Functional Decisions to Corporate States.

Fig. 2 shows the value mapping between functional area models and the financial states in S. In the implementation discussed in the last section, the modeling computation is performed in the IFPS environment, and the modeling relationships are stored in a PROLOG-based knowledge base. The next section will show how the knowledge base provides the communication support needed to assist in this group decision making process.

## 4. Knowledge Based Communication Support

As discussed in section 2, two types of generic information sets (established organization-wide information and input-output information of organization units) are required to provide communication support for reciprocal interdependency. This information can be stored in a knowledge based system to provide intelligent support to the group. In the financial budgeting example, many of the above relationships are a priori defined by the organization and are available for use by the functional units as they build their model(s). This also holds true in other decision environments where dependency exists. The functional unit representatives define the input data required and the output information produced by the functional unit. Table 3 shows how this a priori defined organization-wide information can be stored as a part of the knowledge base in PROLOG. This knowledge base will be used to support the communication needs. Financial budgeting application has been used here as an example to illustrate the use of the knowledge base.

Support of pooled interdependency: When individual functional areas identify input and output variables associated with the model(s) used in reaching their decisions, the knowledge base can be used to check whether all these variable definitions are lexically correct, i.e., known to the organization and part of the organizational directory of variables. The following rule represented in PROLOG is used to perform this check.

lexically\_correct: -input(Model, Model\_inputs), check(Model\_inputs), output(Model, Model\_outputs), check(Model\_outputs).

check([ ]).

check([Head | Tail]): -organizational\_directory
(List), member(Head, List).
check(Tail).
check([Head | Tail]): -write(H), write("Not properly defined"), check(Tail).

If all the variables are found to be lexically correct, it is necessary to see whether their use in the model(s) is appropriate, i.e., logically correct. This logical correctness checking is critical in the context of model validation.

Detailed discussion of model validation is outside the scope of this paper and can be found in [27]. The present implementation of the system performs a simple test to advise the area users of any established input that is considered necessary to generate the output variables of their models. For example, an organization may have considered it appropriate to use “unit sales forecasts” in estimating the “unit production levels.” This can be stored in the knowledge base and used to test the reasonability of production models’ input variables. This test can be represented in PROLOG as:

established\_input(production,[unit\_sales]).

established\_guideline\_check:-
    input(Model,Model\_inputs),established\_input(Model,Est\_inputs),check\_est(Model\_inputs,Est\_inputs).

check\_est(\_,[ ]).

check\_est(MI,[Head | Tail]): -member(Head,MI), check\_est(MI,Tail).

check\_est(MI,[Head | Tail]):-write(Head),write
('should be included as input'),
check(MI,Tail).

In financial budgeting example, accounting identities are quite often used in relating functional area decisions with financial variables such as balance sheet and income statement accounts. For example, if a model is estimating earnings after tax, then it has to use variables earnings before tax and tax in its derivation. These variables can be either derived from other inputs or entered explicitly. By viewing the financial accounts as a hierarchical tree structure, undefined branches of the tree that span over a user's decision scope can be determined systematically [26]. In this paper, only the identities associated

Table 3
Part of Knowledge Base for Financial Budgeting.

Organization-wide, a priori defined, relationships

leaf node(non-aggregate balance sheet and income statement account).

ex leaf\_node(cash).
leaf\_node(dividends).

non\_leaf\_node(aggregate balance sheet and income statement account. [financial accounts that make up this aggregate balance]).

ex: non\_leaf\_node(gross\_income,[sales\_revenue.
cost\_of\_goods\_sold]).
non\_leaf\_node(assets,[current\_assets.fixed\_assets]).

effects(financial transaction.[accounts this financial transactions affects in the order of debit and credit]).

ex: effects(cash\_sale,[cash,sales\_revenue]).  
effects(cost\_of\_goods\_sold,[finished\_inventory, cost\_of\_goods\_sold]).

function\_of(financial transaction,[functional decision variables that affect this transaction]).

ex function\_of(cash\_sale,[unit\_sales,price,credit\_factor]). function\_of(sales\_tax,[unit\_sales,price]).

financial ratio([financial variables]).

ex: current\_ratio(current\_assets, current\_liabilities).
return\_on\_assets(earnings\_after\_tax, assets).

above\_target(financial ratio,[plausible reasons]).

ex: above\_target(current\_ratio,[excess cash, too much inventory,too much of investment tied up in inventory]).

below target(financial ratio,[plausible reasons]).

ex: below\_target(current\_ratio,[too many account payables, not enough liquidity, in-sufficient inventory]).

User defined modeling relationship

input(model,[input variables]).
output(model,[output variables]).

ex: input(sales,[standard\_cost]).
output(sales,[unit\_sales,price,credit\_factor, advertising\_expense]).
input(production,[unit\_sales,std\_cost,std\_material\_cost, std\_labor\_cost,std\_supply\_cost]).
output(production,[unit\_production,labor\_hrs\_spent, mat\_qty\_used,supplies\_used]).

with a user's output variables, if known to the system, are presented. The user is then allowed to assess their relevance.

accounting\_identities: -output(Model, Model\_outputs), get\_relationships (Model\_outputs).

get\_relationships([ ]).

get\_relationships([H | T]: -non\_leaf\_node(H, list), write(List), write('you need to estimate these variables'), get\_relationships(T).

get\_relationships([H | T]: -get\_relationships(T).

The synchronization of strategies between the corporate and functional areas can be accomplished through a group consensus or by providing information on any relevant established goals/policies. This type of synchronization can be accomplished using model scope: breadth vs. depth (product planning, sales planning, promotion planning), time horizon): long-term vs. short-term (5 years, 1 year, monthly), etc. [27]. In this paper, only information on relevant goals, policies, etc. are displayed for the functional area's perusal.

goals(marketing,[increase market share by 20 percent,penetrate into other neighboring regions]) policies(production,[maintain stable labor force,

relevant\_information(purchasing,[purchase of equipment over 3,000 dollar value should be made by Finance and will be treated as an investment]).

relevant\_organization\_information(Area):-

goals(Area, Area\_related\_goals);

policies(Area,Area\_related\_policies);

relevant\_information

(Area, Area\_related\_information).

Support for sequential interdependency: The interdependency among units is determined in two stages: first, any overlapping output definition of decision variables is investigated. Then the sequential dependency among functional areas is established. Any dependency between models, once identified, can be corrected through a redefinition or left as is. Some of the dependencies are immediately not apparent, i.e. the dependency is observable only through other models. In such cases, the dependency is shown by a control path and is determined by the knowledge base. This control path relates one model with all others that precede it in their proper sequence. This type of control path information is useful for performing sensitivity analysis across variables that span multiple functional areas.

overlapping\_definition:-

output(Model, Model\_outputs),

other\_definitions (Model, Model\_outputs),

other\_definitions(\_,[]).

other\_definitions(M,[Head | Tail]):-

output(M1, outputs), not(M1 = M),

member(Head,Outputs),write

('overlapping definition'), write(Head),

other\_definitions(M,Tail).

other\_definitions(M,[Head | Tail]):-other\_definitions(M,Tail).

precede(X,Y):-precede(X,Z),precede(Z,Y).   
precede(X,Y): output(X,Outputlist), input(Y,Inputlist),not(X=Y), share(Outputlist,Inputlist)

Table 4 describes the ‘control path’ for a few case examples based on model dependencies shown in Fig. 4. The model and target variable column of Table 4 defines the testing strategy a decision maker would like to investigate. Columns 3 through 6 simply identify the transactions, decision variables, and models of interest, using the logical relationships in the knowledge base. Column 7 will identify the relevant models to be run. The control path in column 8 identifies the sequence to be used in running these models. This issue is being actively investigated by the researchers in the area of model management systems [2,12,13]. A more sophisticated system for model management based on [6] is currently being implemented in the example system.

Support for reciprocal interdependency: The reciprocal interdependency among functional units and the path that controls this dependency can be established from the input and output information of these models using the rule below.

model(sales)

model(production)

recursively\_interdependent: -model(M1), model(M2), not(M1 = M2), precede(M1, M2), precede(M2, M1)

Some of the paths shown in Table 4 are reciprocally interdependent. A resolution of this reciprocal interdependency, if desired, has to be established by the group a priori in terms of the number of iterations needed before terminating the recursion among these models, or by the specification of an acceptable convergence value of the parameter. In the example discussed here, the knowledge base merely provides information on the interdependency among the functional units and asks them to agree on a method to terminate such dependency. Two such recursive interdependencies, one involving sales, production, purchase, and administrative units (see Fig. 3) and the other involving all the functional area units and the corporate unit (see Fig. 1), are discussed in this paper. An acceptable convergence value on the “standard cost” is used to terminate the first recursion and group consensus is used to terminate the other.

Table 4
Control Path Determination for a set of special cases.

<table><tr><td>Case</td><td>Model &amp; target variables</td><td>Nodes of interest (Bi)</td><td>Transactions of interest (Ti)</td><td>Decision variables of interest (Di)</td><td>Model of interest (Mi)</td><td>Relevant models (to be run)</td></tr><tr><td>1</td><td>Impact of “Credit policy” (of M1) on ‘earnings before tax’</td><td>Sales revenue, cost of goods sold, other revenue, depreciation expense, interest expense, office expense</td><td>Cash sale, credit sale, cost of goods sold, depreciation, interest, net salary, interest on short term debt</td><td>Unit sale, price, credit factor, depreciation, interest, net salary, other revenue, interest on short term debt</td><td>Sales (M1), depreciation (M5) interest (M6) payroll (M8) cash management (M11)</td><td>M2 thru M11 of model hierarchy except M8</td></tr><tr><td>2</td><td>Impact of reorder point changes (of M3) on ‘Accounts Payable’</td><td>accounts payable</td><td>material cost accounts paid</td><td>material qty. purchased, material price, accounts paid</td><td>purchase (M3) funds flow (M10)</td><td>M6, M4, M9 and M10</td></tr><tr><td>3</td><td>Impact of depreciation policy changes (of M5) on ‘earnings before tax’</td><td>Same as in Case 1</td><td>Same as in Case 1</td><td>Same as in Case 1</td><td>Same as in Case 1</td><td>-none-</td></tr><tr><td>4</td><td>Impact of ‘inventory policy changes’ (of M2) on the ratio of ‘sales revenue to inventory’</td><td>Sales revenue, raw material inventory, supplies inventory, finished goods inventory, work in process</td><td>Cash sale, credit sale, cost of goods sold, labor cost, material used, supplies used, transfer to finished goods inventory, material cost, supply cost, insurance per month</td><td>Unit sale, price, credit factor, labor hours spent, material qty. used, unit production, material qty. purchased, material price, supply qty., supply price, insurance per month, supplies used</td><td>Sales (M1) production (M2) purchase (M3)</td><td>M3</td></tr><tr><td>5</td><td>Impact of ‘equipment’ units purchased’ (of M3) on long term debt and equity</td><td>long term debt, equity</td><td>long term debt repaid, equity raised, machinery cost</td><td>equipment units purchased, equipment cost, long term debt repaid, equity raised</td><td>M12 and M3</td><td>M4 thru M12 except M7 and M8</td></tr></table>

![](/api/attachments/DNDYZHFB/fulltext/images/5b001b8ccbe5c976b4bce6e63aee5beff46ec15ee684f133ad838494ff6688c3.jpg)  
Fig. 3. Sales, Production, Purchasing, and Administration Looping.

## 5. Implementation of a GDSS for Budgeting

The purpose of a GDSS is to increase the effectiveness of decision groups by facilitating the interactive sharing and use of information among group members and also between the group and the computer [20]. The development of such a GDSS needs an identification of its major components: hardware, software, people, and procedures, and their active engagement in a particular group decision making environment. In this section, we will identify these major components as they are used to aid the budgeting process.

Group decision making environment: Four types of environments (decision room, local decision network, teleconferencing, and remote decision making) are discussed in the literature [10]. We will use a combination of “local decision network" and "decision room" type environments in the financial budgeting case. Some preliminary decision making occurs at the functional level based on long and short-term plans of an organization and this is supported by individual DSS and a local decision network. These preliminary estimates are then reconciled, integrated, and revised in an interactive manner at a single location until a consensus is reached. This process is aided by a decision room type environment [17].

The hardware component: The hardware configuration used is somewhat different from those suggested for a typical decision room. It consists of a mainframe IBM system with a VM/CMS operating system and several terminals or personal computers linked directly to the mainframe. Note, however, that the same can be accomplished with the assistance of a set of personal computers and a file server that allows access to large modeling software and data files. (The system has also been implemented on a network of IBM PS-2 computers.)

The software component: The component includes modeling, data, knowledge, and dialog management software. The software is designed to support both the development of individual DSS by functional users as well as to support the development of GDSS. This dual use of a similar software environment increases the usage frequency, reduces relearning caused by infrequent use, and makes the decision environment less threatening. These factors are considered to be important for the use and survival of GDSS [20]. Specifically, the software components used for developing individual as well as GDSS are IFPS (for modeling support), PROLOG (for knowledge support), SAS (for data management support), and REXX (for dialog support).

The people component: In the budgeting application, this component includes the functional and corporate representatives (group members), and a group coordinator or facilitator. The functions of the group facilitator/coordinator are similar to those discussed in the literature $[9,20]$ . The primary mission of the group coordinator is to make the GDSS technology easy to use in retrieving, manipulating, and disseminating relevant information.

The procedural component: This includes procedures that will support not only the hardware and software use, but also the decision making process. The individual decision making process can be supported with the aid of data, model, and dialog management tools. Extensive literature is available on how such support can be provided effectively $[3,4,23]$ . The group decision making process, however, requires the identification of a procedure that can provide a mapping for integrating the individual and group decisions. The procedure used for this integration has been discussed in the third section and will be illustrated in the following section.

## 6. Use of the GDSS to Reach Consensus Decision

In this section the use of the GDSS to reach a consensus decision will be illustrated with the help of the financial budgeting example. The situation considered has six functional area representatives; Sales, Production, Purchasing, Administrative, Accounting, and Funds Acquisition, and a corporate representative. The responsibilities of each functional unit, the financial transactions they help estimate in the budgeting process, and the major policies they help establish to reach the desired group objectives are shown in Table 5. The models used by various functional areas and their dependencies are shown in Fig. 4.

An analysis of input and output variables defined for each FAM indicates that there is a recursive interdependency between Sales (which uses standard unit cost), Production (uses unit sales), Purchasing (uses unit production, and materials and equipment required), and Administration (uses materials and equipment along with overhead expenses to determine standard unit cost). This is shown in Figure 3. Each functional area involved in such a situation then engages in an iterative group interaction process supported by the GDSS. This process starts with an initial standard unit cost value that allows each functional area to estimate their decision variables using their FAM. Upon a recalculation of the loop control variable (standard cost unit) the above process is repeated until an acceptable consensus is reached. The consensus is reached here when the difference between the values of loop control variable(s) (standard cost unit) during two successive iterations is relatively small. Table 6 shows how the control variable (standard unit cost) and some of the input and output variables change between different iterations in an example situation.

After reaching consensus on these functional decisions, the estimated values of transaction variables from each FAM are sent to the corporate model for aggregation and analysis. Several financial ratios (liquidity, profitability, leverage and activity) are computed for this projected pro forma balance sheet and income statement data. These are then compared with either industry standards or company targets. Table 7 shows the type of ratios computed for the example problem, along with the target values assigned.

The values of these ratios obtained by integrating transaction values from FAMs are then displayed on the main screen. The group then compares the ratios with target values. discusses alternative strategies for reaching the target and selects a particular strategy to see its effect on the financial state represented by these ratios. The FAMs affected by the selected strategy are executed by respective members and new values for these ratios are obtained. The above process is repeated until a group consensus is reached. This iterative process is in itself an illustration of recursive interdependency among various functional and corporate units. Traditional group methods like Nominal Group Techniques can be used for generating ideas on alternative strategies and a voting procedure can also be used for selecting a strategy. These features are currently being built into the system. The main purpose of the modeling and knowledge base mechanism is to provide real time information regarding the effect of alternative strategies on each functional area and financial state of the corporation. This will help minimize disagreement in the group caused due to incomplete information. Table 8 summarizes the results of three alternative strategies. Column 1 of the table represents the initial solution. The three strategies considered are:

![](/api/attachments/DNDYZHFB/fulltext/images/760d655c6d09564d54fe05f5c5e742358a538be580cc8d6065543cf82b73331f.jpg)  
Fig. 4. Model Hierarchy Based on Decision Variable Dependencies.

Table 5
Model/Variable Interrelationships.
Functional Area Model Variables

<table><tr><td rowspan="3">Functional Area</td><td colspan="4">Model Variables</td><td rowspan="3">Policies Established</td></tr><tr><td colspan="2">Input</td><td colspan="2">Decision Variables</td></tr><tr><td>Exogenous</td><td>Endogenous</td><td>Operational</td><td>Transactional</td></tr><tr><td>Sales</td><td>Standard unit cost</td><td>Credit factor; Advertising expense</td><td>Unit sales; price</td><td>Credit sales; Cash sales; Advertising expense; Cost of goods sold</td><td>Pricing; Promotion; Credit;</td></tr><tr><td>Production</td><td>Unit sales</td><td>Capacity, material and labor needs; finished goods inventory levels</td><td>Unit production; Materials; equipment</td><td>Labor expended; Material consumed; Supplies used; Finished goods inventoried</td><td>Inventory; Capacity, labor and material utilization</td></tr><tr><td>Purchasing</td><td>Unit production; materials; equipment</td><td>Material cost and inventory levels</td><td>-</td><td>Material costs; equipment costs; supply costs</td><td>Material inventory; pur chasing</td></tr><tr><td>Administrative</td><td>Unit production; price; unit sales; Equipment costs</td><td>Office personnel; tax withholding; depreciation</td><td>Standard unit cost</td><td>Depreciation expense; interest expense; salary payments; insurance costs (pre-paid and adjusted); tax (sales and employee withholdings).</td><td>Depreciation; tax; insurance</td></tr><tr><td>Accounting</td><td>Credit sales; material costs; interest and tax expenses</td><td>Collection and vendor payment profiles</td><td></td><td>Receivable collections; accounts paid; interest paid; and taxes paid</td><td>Collection; discount taking and giving</td></tr><tr><td>Funds</td><td>levels of cash, equity, marketable securities, and short term debt; debt payments</td><td>divident payouts; liquidity decisions</td><td></td><td>marketable securities (bought &amp; sold); short term debt (raised and paid); equity raised; dividends paid; long term debt repaid; revenues from securities and interest on short term debt.</td><td>debt/equity; sales/cash; short term liquidity</td></tr></table>

Table 6  
Iterations to Resolve Reciprocal Interdependency.

<table><tr><td>Iteration Number</td><td>Standard Unit Cost</td><td>Price</td><td>Unit Sales</td><td>Unit Production</td><td>Materials &amp; Equipment Cost</td><td>New Unit Cost</td></tr><tr><td>1</td><td>$40.00</td><td>72.22</td><td>8056</td><td>9667</td><td>108,469</td><td>47.43</td></tr><tr><td>2</td><td>$47.43</td><td>75.93</td><td>7124</td><td>8552</td><td>114,780</td><td>50.09</td></tr><tr><td>3</td><td>$50.09</td><td>77.27</td><td>6795</td><td>8154</td><td>109,426</td><td>50.36</td></tr><tr><td>4</td><td>$50.36</td><td>77.40</td><td>6761</td><td>8113</td><td>108,882</td><td>50.38</td></tr></table>

Table 7  
Ratios Calculated in Corporate Model.

<table><tr><td colspan="3"></td><td>Target values</td></tr><tr><td rowspan="2">Liquidity</td><td>1. Current Ratio</td><td>current assets/current liabilities</td><td>2.4</td></tr><tr><td>2. Quick Ratio</td><td>(current assets - inventory)/current liabilities</td><td>1.2</td></tr><tr><td rowspan="4">Leverage</td><td>3. Debt to total assets</td><td>long term debt/total assets</td><td>0.45</td></tr><tr><td>4. Debt to equity</td><td>long term debt/equity</td><td>0.81</td></tr><tr><td>5. Times interest earned</td><td>(earnings before tax + interest expense)/interest expense</td><td>6.0</td></tr><tr><td>6. Fixed charge coverage</td><td>income before meeting fixed charges/fixed charges</td><td>3.2</td></tr><tr><td rowspan="4">Activity</td><td>7. Inventory turnover</td><td>cost of goods sold/(average inventory)</td><td>5.0</td></tr><tr><td>8. Average collections</td><td>average accounts receivables/average credit sales per day</td><td>60.0</td></tr><tr><td>9. Fixed asset turnover</td><td>sales/fixed assets</td><td>11.0</td></tr><tr><td>10. Total asset turnover</td><td>sales/total assets</td><td>7.0</td></tr><tr><td rowspan="4">Profitability</td><td>11. Gross profit margin</td><td>(sales - cost of goods sold)/sales</td><td>12%</td></tr><tr><td>12. Net profit margin</td><td>operating income/sales</td><td>5%</td></tr><tr><td>13. Return on total assets</td><td>(net income + interest)/total assets</td><td>8%</td></tr><tr><td>14. Return on equity</td><td>net income/common equity</td><td>9.5%</td></tr></table>

Table 8  
Effect of Alternative Strategies on Pro-Forma Balance Sheet and Income Statement Data.

<table><tr><td colspan="2"></td><td>Initial Solution</td><td>Strategy 1</td><td>Strategy 2</td><td>Strategy 3</td></tr><tr><td rowspan="2">Liquidity</td><td>1. Current Ratio</td><td>3.08</td><td>3.8</td><td>2.1</td><td>2.6</td></tr><tr><td>2. Quick Ratio</td><td>2.52</td><td>3.2</td><td>1.5</td><td>1.8</td></tr><tr><td rowspan="4">Leverage</td><td>3. Debt to total assets</td><td>0.53</td><td>0.44</td><td>0.28</td><td>0.29</td></tr><tr><td>4. Debt to equity</td><td>1.60</td><td>1.10</td><td>0.51</td><td>0.50</td></tr><tr><td>5. Times interest earned</td><td>0.96</td><td>1.02</td><td>1.80</td><td>3.60</td></tr><tr><td>6. Fixed charge coverage</td><td>1.40</td><td>1.40</td><td>1.50</td><td>1.80</td></tr><tr><td rowspan="4">Activity</td><td>7. Inventory turnover</td><td>2.9</td><td>3.1</td><td>3.1</td><td>3.0</td></tr><tr><td>8. Average collections</td><td>182.0</td><td>150.0</td><td>150.0</td><td>150.0</td></tr><tr><td>9. Fixed asset turnover</td><td>0.74</td><td>0.90</td><td>0.86</td><td>0.76</td></tr><tr><td>10. Total asset turnover</td><td>0.42</td><td>0.43</td><td>0.54</td><td>0.50</td></tr><tr><td rowspan="4">Profit-</td><td>11. Gross profit margin</td><td>1.54</td><td>1.61</td><td>1.6</td><td>3.0</td></tr><tr><td>12. Net profit margin</td><td>0.14</td><td>0.51</td><td>0.14</td><td>0.7</td></tr><tr><td>13. Return on total assets</td><td>18%</td><td>12%</td><td>14%</td><td>15%</td></tr><tr><td>14. Return on equity</td><td>6%</td><td>5%</td><td>7%</td><td>9%</td></tr></table>

Strategy 1: Try to reduce the average accounts receivable by tightening the credit. All other parameters were unchanged except price elasticity was increased (by changing slope of equation) to allow price fluctuations because of tighter credit.

Effect: Because of tighter credit, there was loss in sales; hence the overall effect of above strategy was low profitability. Also this strategy did not significantly improve the average collection and turnover ratios.

Strategy 2: Since the current and quick ratios are quite high, the next strategy tried was to reduce long-term debt by cash purchases.

Effect: This strategy did reduce the long-term debt and also improved profitability to a certain extent.

Strategy 3: Since turnover ratios were still quite low, it was decided to try to increase sales by promotion. The amount spent on advertising was increased from \$15,000 to \$35,000.

Effect: This strategy did improve the “times interest” earned and profits but did not improve the turnover significantly.

The process is continued until a consensus is reached on an appropriate strategy.

## 7. Conclusions and Extensions

This paper illustrates how knowledge based decision support tools have a potential to be used in the design of a GDSS to facilitate communication support. The knowledge base (1) links the individual decisions with group decisions, (2) provides information to support communication among group members, (3) helps iterate over the individual and group decisions until a consensus is reached. The knowledge base is implemented in PROLOG and the modeling support is provided by IFPS. A financial budgeting example is used to illustrate the use of the knowledge base.

This application demonstrates clearly that system support required for group decision making is different from the system support for individual decision making as there are conflicts among the group members which need resolution before a final decision can be reached. The impact of such a GDSS on group decision making needs further study. (The system is currently being tested in a live setting.) The impact may be measured in terms of quality of decision making (alternatives considered, confidence associated with the final decision, etc.), time to reach a final decision, its effect from a historical perspective (how a recording of past decisions influences current decision making), etc.

The procedure used here to link individual and group decisions is based on the premise that all functional decisions eventually have to be translated into financial terms at the corporate level. The knowledge base is primarily used here to facilitate communication support under conditions of reciprocal interdependency. The content of the knowledge base is application dependent, and needs to be changed to suit the application under development. However, the concept and the method of using the knowledge base and the model base to support communication presented in this paper is general and can be used in developing any GDSS.

## References

[1] Ackoff, Russel A., A Concept of Corporate Planning, Wiley-Inter., New York, 1970.

[2] Applegate, L.M., G. Klein, B.R. Konsynski, and J.F. Nunamaker, Model Management Systems: Proposed Model Representations and Future Designs, Proceedings of Sixth International Conference on Information Systems, December 1985.

[3] Bonczak, Robert H., C.W. Holsapple, and A.B. Whinston, Foundations of Decision Support Systems, Academic Press, New York, 1981.

[4] Brennan, J.J., and Joyce Elam, Enhanced Capabilities for Model Based Decision Support Systems, Decision Support Systems - Putting Theory into Practice, Edited by Sprague, R.H. and H.J. Watson, Prentice Hall, New Jersey, 1986.

[5] Brown, Bernice, Delphi Process: A Methodology Used for the Elicitation of Opinions of Experts, Rand Report No. P-3925, 1968. The RAND Corporation, Santa Monica, California.

[6] Bu-Hulaiga, M., Model-Manipulation in Decision Support Systems: A Plan-Based Approach, Ph.D. Dissertation, September 1987, University of Wisconsin-Milwaukee.

[7] Cook, R.L. and K.R. Hammond, Interpersonal Learning and Interpersonal Conflict Reduction in Decision Making Groups, in R.A. Guzzo (Ed.), Improving Group Decision Making, Academic Press, N.Y., 1982, pp. 13–72.

[8] Delbecq, A.L., A.H. Van de Ven, and D.H. Gustafson, Group Techniques for Program Planning: A Guide to Nominal Group and Delphi Processes, Scott-Foresman & Company, Glenview, Illinois, 1975.

[9] DeSanctis, G. and B. Gallupe, Group Decision Support Systems: A New Frontier, Data Base, Vol. 16, No. 2, Winter 1985.

[10] DeSanctis, G. and B. Gallupe, GDSS: A Brief Look at a New Concept in Decision Support, ACM Proceedings of the 21st Annual SIGCPR and SIGBDP Conference, pp. 24–28, 1985.

[11] DeSanctis, G. and B. Gallupe, A Foundation for the Study of Group Decision Support Systems, Management Science, Vol. 33, No. 5, May 1987, pp. 589–609.

[12] Dutta, Amitava, and A. Basu, An Artificial Intelligence Approach to Model Management in Decision Support Systems, Computer, September 1984, pp. 89–97.

[13] Elam, Joyce, J., J. Henderson, and L.W. Miller, Model Management Systems: An Approach to Decision Support in Complex Organizations, Hawaii International Conference on Systems Sciences, University of Hawaii, 1981.

[14] Fisher, B.A., Small Group Decision Making, 2nd Ed., McGraw-Hill, New York, New York, 1980.

[15] Gallupe, B., The Impact of Task Difficulty on the Use of a Group Decision Support System, Ph.D. Dissertation, University of Minnesota, December 1985.

[16] Goncalves, A.S., Group Decision Methodology and Group Decision Support Systems, Transactions on the Third International Conference on Decision Support Systems, 1983.

[17] Gray, P., The SMU Decision Room Project, Transactions of the First International Conference on Decision Support Systems, Atlanta, Georgia, June 1981.

[18] Gray, P., Initial Observations From the Decision Room Project, Transactions of the Third International Conference on Decision Support Systems, Boston, Massachusetts, June 1983.

[19] Hoffman, R.L., The Group Problem Solving Process, Praeger, 1979.

[20] Huber, G.P., Issues in the Design of Group Decision Support Systems, MIS Quarterly, September, 1984.

[21] Lahr, M.L., Interactive Planning – The Way to Develop Commitment, Long Range Planning, Vol. 16, No. 4, pp. 31–38, 1983.

[22] Mintzberg, H., D. Raisinghani, and A. Theoret, The Structure of Unstructured Decision Processes, Administrative Science Quarterly, Vol. 21, 1976.

[23] Simon, Herbert A., Models of Man, Social and Rational, John Wiley & Sons, New York, 1957.

[24] Sprague, R.H., A Framework for the Development of Decision Support Systems, MIS Quarterly, 1980, 4(4), 1–26.

[25] Stohr, E.A., and M.R. Tanniru, A Data Base for Operations Research Models, Policy Analysis and Information Systems, Vol. 4, No. 2, December 1980.

[26] Tanniru, Mohan R., A Decision Support Systems for Planning, Ph.D. Dissertation, Northwestern University, 1978.

[27] Tanniru, M.R. and T.J. Murray, Model Validation in an DSS Environment, Hawaii International Conference on Systems Sciences, University of Hawaii, 1987.

[28] Thompson, James D., Organizations in Action, McGraw Hill, New York, 1967.

[29] Tuckman, B.W., Development Sequence in Small Groups, Psychological Bulletin, Vol. 63, 1965, pp. 384.
