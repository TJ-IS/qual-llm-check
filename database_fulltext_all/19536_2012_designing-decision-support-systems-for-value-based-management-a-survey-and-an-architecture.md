---
otero_id: 19536
otero_key: "YXDKTXPB"
title: "Designing decision support systems for value-based management: A survey and an architecture"
authors: "G.J. Hahn; H. Kuhn"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.02.016"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Designing decision support systems for value-based management: A survey and an architecture

G.J. Hahn, H. Kuhn ⁎

Department of Supply Chain Management & Operations, Catholic University of Eichstaett-Ingolstadt, Germany

a r t i c l e i n f o

Article history: Received 29 July 2010 Received in revised form 11 February 2012 Accepted 28 February 2012 Available online 7 March 2012

Keywords: Value-based management Integrated business planning Supply chain management Financial management Robust optimization

## a b s t r a c t

Value-based Management (VBM) concepts are prevalent in theory and practice since shareholder value creation is commonly considered the paramount business goal. However, VBM mainly applies data-driven concepts to support decision-making, disregarding model-driven approaches. This paper develops a comprehensive approach to designing model-driven DSS for VBM. First, we derive a conceptual architecture for Integrated Business Planning (IBP) as the foundation for a model-driven approach to VBM. Second, we present a uni<sup>fi</sup>ed modeling approach for value-based performance and risk optimization that implements Value Added (xVA) performance metrics and applies robust optimization methods to mitigate risk impact.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction and scope

Creating shareholder value is commonly considered the paramount business goal [120], and requires an integrated approach to performance [21] and risk management [98]. Value-based Management (VBM) provides a corresponding framework using value driver trees and risk-adjusted performance metrics as major concepts for performance and risk management [58]. Value driver trees drill down a toplevel metric into operational levers for performance management [95] and risk implications are considered via risk-adjusted cost of capital [120]. However, there are two major drawbacks to this common approach from an OR perspective. First, value driver trees are explanatory frameworks and do not provide support on balancing con<sup>fl</sup>icting value drivers. Second, the in<sup>fl</sup>uence of uncertainty is covered indirectly via risk-adjusted parameters instead of managing risk impact based on scenario information. From a decision support perspective (see [90]), VBM mainly resorts to data-driven concepts, disregarding modeldriven approaches.

Decision support models for VBM are receiving increasing attention in OR-related publications (e.g., [44,45,63,92]). These articles implement conceptual approaches [25,64,115] and build upon previous decision support models for integrated supply chain and <sup>fi</sup>nancial management (e.g., [41,65,81,109]). They use prevalent value-based performance metrics to do this, such as discounted Free Cash Flow (FCF) and Economic Value Added (EVA), and apply robust optimization methods to deal with risk impact. A few conceptual papers discuss approaches to corporate planning and optimization advocating a comprehensive decision-oriented approach that integrates operations, <sup>fi</sup>nancial, and risk considerations within the supply chain context [40,91,114]. However, a uni<sup>fi</sup>ed modeling approach for model-driven decision support in VBM has not yet been presented.

A comprehensive architecture for Integrated Business Planning (IBP) bridging the gap between Supply Chain Management (SCM) and Financial Management (FM) [103] constitutes the foundation for model-driven decision support in VBM. Conceptual architectures have been developed separately for SCM [34] and FM [4] summarizing a large body of literature on decision-oriented approaches in both domains [73,111]. Long-term capital budgeting/structuring and shortterm working capital management constitute the two planning levels of FM [4]. SCM distinguishes three planning levels [34]: long-term strategic network planning, mid-term sales and operations planning, and short-term order ful<sup>fi</sup>llment planning. Although modeling frameworks in SCM underline the relevance of <sup>fi</sup>nancial aspects and risk implications [15,75], uni<sup>fi</sup>ed frameworks and approaches to IBP are mainly discussed outside the academic literature [10,103].

A diverse body of literature deals with Enterprise Resource Planning (ERP) [77,104], including discussions on future trends and research perspectives [55,72]. The scope of ERP expands beyond classical data and process integration to provide enhanced modeling and analytical capabilities for complex business problems [76,105]. Corresponding DSS for advanced business planning have emerged as stand-alone systems ‘bolt on’ ERP covering different functional aspects and methodological approaches [76,97]. Advanced Planning and Scheduling (APS) systems in SCM focus on material <sup>fl</sup>ows and pursue a model-driven approach using optimization methods [90,111]. In contrast, Business Planning and Simulation (BPS) systems in FM mainly cover <sup>fi</sup>nancial <sup>fl</sup>ows and apply data-driven concepts [32,97]. Although the OR discipline could contribute substantially to the conceptual and methodological advancement of ERP [55], a comprehensive conceptual architecture for model-driven IBP has not yet been developed.

In summary, a large body of literature deals with concepts and decision support models in VBM and IBP. However, two main gaps in the literature can be determined. First, a comprehensive conceptual architecture for model-driven IBP deserves further research since corresponding approaches are con<sup>fi</sup>ned to their respective domains. Second, various decision-oriented approaches to VBM exist, but a uni<sup>fi</sup>ed modeling approach has not yet been presented. This paper therefore develops a comprehensive approach to designing model-driven DSS for VBM. The remainder of the paper is structured as follows: a conceptual architecture for IBP following the hierarchical planning paradigm is derived in Section 2 from a literature survey. Section 3 develops a corresponding uni<sup>fi</sup>ed modeling approach for value-based performance and risk management using Value Added (xVA) performance concepts and robust optimization methods. We conclude the paper in Section 4 summarizing major research perspectives.

## 2. A conceptual architecture for Integrated Business Planning

## 2.1. Overview

In the following, we derive the Integrated Business Planning (IBP) matrix as a comprehensive conceptual architecture for model-driven DSS at the corporate level (see Fig. 1). The IBP matrix is structured along the two dimensions time horizon and corporate perspective, and follows the hierarchical planning paradigm [101]. The architecture distinguishes three different levels from long- to short-term [34], and provides an integrated perspective on pro<sup>fi</sup>t, cash <sup>fl</sup>ow, and risk considerations [114]. The real-time execution level is positioned below the planning domains and covers the management of operations/<sup>fi</sup>nancial transactions as well as risk monitoring [52,74,83].

The IBP matrix is predominantly targeted at companies in supply chain-oriented manufacturing industries, but can easily be adapted to retail and service industries. De<sup>fi</sup>nitions and detailed descriptions for the 8 domains, 14 subdomains, and 23 decision-relevant aspects of the IBP matrix are developed from a literature survey (see Table 1). In a hybrid top-down and bottom-up approach, we consolidate relevant conceptual and architectural frameworks for decision support in IBP, and investigate decision-oriented aspects from selective in<sup>fl</sup>uential papers. Surveying the literature on decision-oriented approaches, we focus on mixed-integer linear programming models due to their prevalence in model-driven DSS for corporate planning [111].

Pro<sup>fi</sup>t and cash <sup>fl</sup>ow perspective constitute the two pillars of corporate performance [58]. The pro<sup>fi</sup>t perspective covers the physical dimension of business, and thus includes all (dis-)investment and operational decisions in SCM [34] as well as Supplier and Customer Relationship Management (SRM and CRM), Product Lifecycle Management (PLM), and Human Resource Management (HRM) [76]. Since the physical and <sup>fi</sup>nancial dimensions are inextricably interlinked [103], the cash <sup>fl</sup>ow perspective covers decisions on capital budgeting and working capital management to <sup>fi</sup>nance decisions of the physical domains and to ensure fundamental liquidity [4]. A separate risk perspective [98,114] is introduced to complete the model-driven approach to integrated performance and risk management.

Two types of risk can be distinguished according to their severity [112]: operational risks result from the uncertainty of future events in the ordinary course of business, as opposed to disruption risks from natural or man-made disasters. Decision-oriented approaches can address both types of risk [45,60] and implement the four common risk management responses [116]: risk avoidance and adoption either completely eliminate or accept risks and thus correspond to con<sup>fi</sup>guration decisions at the long-term level. Coordination decisions at the midto short-term level result in risk mitigation or transfer, reducing or sharing risk impact [98].

A company creates value if earnings exceed total costs of invested capital [95]. Although a multitude of value-based performance metrics exists [95,120], model-driven approaches mainly focus on Value Added (xVA) concepts such as Economic Value Added (EVA) or metrics based on Free Cash Flow (FCF) such as Corporate Value (CV) or Shareholder Value (SV). Hahn and Kuhn [44] implement the EVA concept in mid-term corporate planning and compare the integrated value-based approach to a common approach where the physical and <sup>fi</sup>nancial perspectives are optimized sequentially. The numerical analyses outline a substantial improvement potential in EVA of between 9% and 32%. Majumdar and Chattopadhyay [70] conduct a similar analysis for their integrated approach to investment and <sup>fi</sup>nancial planning in power systems. They evaluate the incremental net worth of the <sup>fi</sup>rm and obtain an improvement potential of 22% for the integrated approach. Incremental net worth of the <sup>fi</sup>rm is comparable to Market Value Added (MVA) which is the multi-annual extension of the EVA concept [120]. Lainez et al. [62] investigate optimal supply chain design in chemical process industries, and compare an integrated approach to a common pro<sup>fi</sup>t-based approach increasing Corporate Value by 32%.

![](/api/attachments/YXDKTXPB/fulltext/images/1776085fee77b0b7bf59066befeb7faba2e0e32d49425ac57daa6b6ae53b8fa3.jpg)  
Fig. 1. The Integrated Business Planning (IBP) matrix

Domain map of integrated business planning

<table><tr><td>Level</td><td>Domain</td><td>Subdomain</td><td>Decision-relevant aspects</td><td>Value-based metrics</td></tr><tr><td rowspan="3">Long-term</td><td rowspan="3">Strategic Performance &amp; Risk Management</td><td>Strategic Business Development</td><td>(Dis-)Investments in research and product development Determination of suppliers and procurement program (Dis-)Investments in operations/support infrastructure Determination of market portfolio and sales program (Dis-)Investments in customer service and aftersales</td><td rowspan="3">MVA, CV/SV</td></tr><tr><td>Capital Budgeting Management</td><td>Determination of equity/debt funding, financial leverage Dividend policy and cost of capital management</td></tr><tr><td>Risk Portfolio Management</td><td>Management of risk exposure</td></tr><tr><td rowspan="6">Mid-term</td><td rowspan="2">Profit Calculation</td><td>Sales and Operations Management</td><td>Demand and master planning Capacity adjustment timing</td><td rowspan="6">EVA, FCF</td></tr><tr><td>Project Portfolio Management</td><td>Project selection and resource allocation</td></tr><tr><td>Balance Sheet Calculation</td><td>Creative Accounting Management</td><td>Capitalization and valuation Transfer pricing</td></tr><tr><td rowspan="2">Cash Flow Calculation</td><td>Debt Management</td><td>Mid-term debt creation and repayment</td></tr><tr><td>Working Capital Management</td><td>Cash-to-cash cycle management</td></tr><tr><td>Operational Risk Management</td><td>Risk Reduction</td><td>Risk mitigation and transfer</td></tr><tr><td rowspan="5">Short-term</td><td rowspan="2">Earnings Calculation</td><td>Revenue Management</td><td rowspan="2">Profitable-to-promise demand fulfillment Material requirements planning and purchasing Planning/scheduling of production and distribution Scheduling of project activities and resources</td><td rowspan="5">EVA, FCF</td></tr><tr><td>Cost Management</td></tr><tr><td rowspan="2">Liquidity Calculation</td><td>Open Items Management</td><td>Management of accounts receivable and payable</td></tr><tr><td>Cash Management</td><td>Short-term borrowing and lending</td></tr><tr><td>Risk Assessment</td><td>Risk Evaluation</td><td>Risk profile analysis</td></tr></table>

## 2.2. Long-term level

Strategic performance and risk management constitutes one comprehensive domain at the long-term level, integrating the highly interdependent subdomains of strategic business development [25], capital budgeting management [4], and risk portfolio management [114]. Decision-oriented approaches at the long-term level focus on the entire supply chain, the aggregated portfolio of further business activities [114], and aggregated balance sheet positions [4] covering a planning period of more than two years in quarterly or (semi-)annual time buckets [34].

Strategic business development considers value-creating (dis-) investment and con<sup>fi</sup>guration decisions with respect to (in-)tangible assets supporting the value chain [25,72,95]. Strategic business development thus integrates PLM and SCM [7,38], determining an optimal portfolio of product development activities [61] and the corresponding optimal closed-loop supply chain footprint [30,35,63]. Decisions on the supply chain footprint include determination of suppliers and the procurement program, (dis-)investments in operations/support infrastructure, determination of the market portfolio and the sales program, and (dis-)investments in customer service and aftersales [34]. Since SRM/CRM, and HRM support integrated value chain management [72,76,111], strategic business development should also consider further planning-relevant aspects regarding supplier, customer, and employee lifecycle management. Selective aspects have already been integrated into the literature on supply chain design [38], but could be further extended to develop a comprehensive approach.

Capital budgeting management determines decisions on volume and structure of equity and debt capital to <sup>fi</sup>nance (dis-)investment activities in strategic business development, and deals with dividend policy and cost of capital management [17,115]. Two major streams of research can be distinguished within this <sup>fi</sup>eld. Joint investment and <sup>fi</sup>nancial planning models cover both decisions simultaneously for capital budgeting [12,43,47,79], while singular <sup>fi</sup>nancial planning models optimize capital structure/volume and <sup>fi</sup>nancial <sup>fl</sup>ows for a given (dis-)investment plan [18,22].

Risk portfolio management deals with risk exposure due to strategic con<sup>fi</sup>guration decisions and aims at determining a robust business portfolio [60,108]. Two different approaches to risk portfolio management can be distinguished. Financial market-oriented models only focus on non-diversi<sup>fi</sup>able risk factors [48,50] as opposed to more prevalent total risk approaches [51]. Applequist et al. [3] present a combination of both approaches considering the risk premium for a physical investment compared to an alternative investment. Decision-oriented approaches for operational (e.g., [85,87,89]) and disruption [93,107] risk planning have emerged corresponding to the distinction between both types of risk.

Decision-oriented approaches to VBM at the long-term level are discussed in several papers. However, they only focus on performance management [62,70] and/or apply an expected value approach within stochastic programming [68,92,117] to deal with uncertainty. Only Lainez et al. [63] consider aspects of risk management using contracts for risk hedging in supplier–customer relationships. An integrated approach to strategic performance and risk optimization implementing a valuebased performance metric thus provides opportunities for further research.

## 2.3. Mid-term Level

Strategic performance and risk management determines the frame for the mid-term level; simulation results for different con<sup>fi</sup>gurations in mid-term corporate management serve as input for the long-term level [97]. Pro<sup>fi</sup>t, balance sheet, and cash <sup>fl</sup>ow calculation as well as operational risk management constitute the domains of mid-term corporate planning [45,58]. Decision-oriented approaches at the midterm level cover supply chain segments, major activities and resources in the project portfolio [37], and balance sheet positions [58] for a planning period of 6 to 18 months [34].

Profit calculation covers sales and operations management [31,57] as well as project portfolio management [37], constituting major buckets of the income statement [58]. Sales and operations management coordinates demand and master planning [34] in a closed-loop supply chain [35] as well as capacity adjustment timing [16,46]. Project portfolio management deals with project selection and resource allocation [37] for business activities in PLM, SRM/CRM, and HRM [72,114]. Although various interdependencies exist between both subdomains, an integrated approach has not yet been developed and thus deserves further research.

Balance sheet calculation is concerned with creative accounting to optimize the tax burden within the legal framework, including decisions on capitalization and valuation of assets as well as transfer pricing within multinational corporations [82]. Corresponding decision models for <sup>fi</sup>nancial statement planning [5,96] and optimal transfer pricing [80,86] are rarely discussed in the literature and provide opportunities for further research.

Cash flow calculation deals with balancing mid-term cash in- and out<sup>fl</sup>ows due to debt and working capital management [17]. Working capital management covers decisions on current assets and liabilities [4], including short-term borrowing and lending, handling of accounts receivable and payable, cash management, and inventory management. Since inventories are also determined as part of sales and operations management, an integrated approach to working capital management is required [20,71,80,99]. Debt management covers various means of mid-term debt funding, such as bonds or bank loans [17].

Operational risk management is concerned with risks in material and <sup>fi</sup>nancial <sup>fl</sup>ows due to uncertainty in supply, operations, and demand as well as incoming payments, exchange rates, and interest rates [113,116]. Project activities and resources are also subject to uncertainty [49] and should be considered in the risk management approach. Robust optimization methods [66,119,121] and sample average approximation approaches [9,88] are used for risk optimization in the context of stochastic programming.

Different decision-oriented approaches to integrated pro<sup>fi</sup>t and cash <sup>fl</sup>ow calculation are discussed in the early literature [8,27,33,54,59], and basically combine existing models for sales and operations management and working capital management. More recent papers extend the scope towards the supply chain [26,41] and integrate risk considerations [109]. A comprehensive approach for value-based performance and risk optimization in supply chains at the mid-term level can be found in Hahn and Kuhn [45].

## 2.4. Short-term level

Coordination decisions from mid-term corporate management determine instructions for the short-term level [97]. Short-term corporate management correspondingly provides feedback to the mid-term level either ex ante in the event of infeasible/suboptimal results or ex post via a rolling horizons approach [101]. Earnings and liquidity calculation, and risk assessment constitute the domains of short-term corporate management [17,83]. Decision-oriented approaches at the short-term level cover single supply chain items, detailed activities and resources [19] in projects, and individual <sup>fi</sup>nancial items [4] for a planning period of several weeks [34].

Earnings calculation is concerned with short-term revenue and cost management [1,24,42]. Short-term revenue management provides decision support for pro<sup>fi</sup>table-to-promise demand ful<sup>fi</sup>llment, integrating order promising and dynamic pricing considerations [94]. Cost management deals with short-term procurement, production, and distribution planning [34] in a closed-loop supply chain [35], and involves lot-sizing/scheduling considerations [29]. Project scheduling [19,49] provides the required framework to plan detailed project activities and resources in PLM, SRM/CRM, and HRM [72,76]. Since the decision-relevant aspects are less closely interlinked as opposed to the mid-term level [97], further research should be devoted to coordination mechanisms and distributed decision-making approaches [101].

Short-term open items and cash management constitute the domain of liquidity calculation [36,39,106]. Open items management covers handling of accounts receivable and payable regarding factoring and early payment [67,84]. Cash management considers short-term borrowing and lending using securities or a bank line of credit [17,56,69,110].

Although operational risk management approaches (see Section 2.3) can also be applied to the short-term level [102], indirect methods of risk assessment such as sensitivity and risk analysis [2] are more prevalent in short-term corporate management [83]. Especially risk pro<sup>fi</sup>les are a common tool for visualizing and analyzing the risk impact of different scenarios [9].

Charnes et al. [23] established the discussion on integrated approaches to short-term operations and <sup>fi</sup>nancial planning by investigating a simpli<sup>fi</sup>ed warehousing problem with a <sup>fi</sup>nancial constraint. More sophisticated models with respect to production and supply chain management are provided in recent papers [6,13,100,118]. Approaches to value-based performance optimization at the shortterm level considering risk implications have not yet been discussed, and provide opportunities for further research.

## 3. Modeling Value-based Management

## 3.1. Value-based performance metrics

Since a multitude of value-based performance metrics exists, we focus on Economic Value Added (EVA) in the following due to the high practicability and intelligibility of the concept [120]. EVA determines economic profit, i.e., operating pro<sup>fi</sup>t minus total costs of invested capital [95]. In (1), EVA in period t equals net operating pro<sup>fi</sup>t NOP in period t after tax (tax rate z) minus the capital charge derived from net operating assets NOA at the end of the previous period t−1 and weighted average cost of capital i<sup>wacc</sup> [120].

$$
E V A _ {t} = N O P _ {t} \cdot (1 - z) - N O A _ {t - 1} \cdot i ^ {w a c c}\tag{1}
$$

$$
M V A = \sum_ {t = 1} ^ {T} \frac {\mathrm{EVA} _ {t}}{(1 + i ^ {\mathrm{wacc}}) ^ {t}}\tag{2}
$$

Market Value Added (MVA) represents the multi-annual extension of the EVA concept and is calculated in (2) as the sum of discounted EVA values up to the planning horizon T, applying WACC i<sup>wacc</sup> [120]. Consequently, the EVA concept can be consistently applied across the three hierarchical planning levels of the IBP matrix. While EVA is directly suited for IBP at the mid-/short-term level, MVA can be applied to the long-term level. Performance metrics such as EVA cannot be in<sup>fl</sup>uenced at the top level and are thus drilled down into separate value drivers [95]. Value drivers and corresponding subdomains of IBP are summarized in Fig. 2.

$$
N O P _ {t} = N P _ {t} - E x p _ {t}\tag{3}
$$

In (3), NOP in period t results from net pro<sup>fi</sup>ts NP and expenses Exp in period t. Net pro<sup>fi</sup>ts are derived from mid-term sales and operations management and short-term revenue and cost management covering sales revenues and variable costs of operations from procurement, production, and distribution [44]. Model-driven approaches to long-term strategic performance and risk management require an embedded model for sales and operations management to evaluate con<sup>fi</sup>guration decisions in strategic business development with respect to net pro<sup>fi</sup>t impact [38]. Expenses are partially <sup>fi</sup>xed costs at the mid-/short-term level and cover depreciations, non-capitalizable investments, and other overhead costs [62]. They result from (dis-)investment and con<sup>fi</sup>guration decisions in long-term strategic business development and decisions in mid-term project portfolio management.

$$
N O A _ {t} = F A _ {t} + I _ {t} + C E _ {t}\tag{4}
$$

Net operating assets NOA at the end of period t in (4) cover <sup>fi</sup>xed assets FA, inventories I, and the position in net current <sup>fi</sup>nancial assets CE [120]. (Dis-)investment activities in strategic business development and mid-term creative accounting management de<sup>fi</sup>ne the balance of <sup>fi</sup>xed assets [62,96]. Several factors in<sup>fl</sup>uence the balance of inventories: inventory (re-)allocation due to strategic business development and seasonal stocking in sales and operations management (in case of time buckets of less than a year) determine inventories at the longterm level [38]. Inventory management is mainly performed as an integral part of mid-term sales, operations, and working capital management [44] and short-term cost management [34]. Creative accounting management can be used to in<sup>fl</sup>uence inventory valuation [96].

![](/api/attachments/YXDKTXPB/fulltext/images/b75be51710678b59289cf8eca5529c947e436dd9fffb1507e7a73a4b100a9a3d.jpg)  
Fig. 2. Value driver tree for the EVA concept with corresponding IBP subdomains.

Net current <sup>fi</sup>nancial assets include short-term <sup>fi</sup>nancial investments, accounts receivable, and cash deducting accounts payable since they are non-interest-bearing debt capital [58]. Endogenous and exogenous cash <sup>fl</sup>ows determine the position in net current <sup>fi</sup>nancial assets CE at the end of period t [44,62]: activities in strategic business development as well as pro<sup>fi</sup>t and earnings calculation de<sup>fi</sup>ne endogenous cash <sup>fl</sup>ow; exogenous cash <sup>fl</sup>ow results from long-term capital budgeting, mid-term debt and working capital management, and short-term open items and cash management.

## 3.2. Integrated performance and risk optimization

VBM predominantly pursues an indirect approach to risk management using expected values and risk-adjusted cost of capital [95,120]. Corresponding OR-based approaches for VBM consider different discrete scenarios to account for uncertainty directly, but also apply an expected value approach (e.g., [63,68,92,117]). In contrast, we use robust optimization methods to develop an integrated approach for performance and risk management based on the EVA concept. A prede-<sup>fi</sup>ned hurdle rate is thus applied instead of WACC to avoid misinterpretations with respect to risk considerations [120].

Robust optimization represents a generalization of stochastic programming explicitly considering the risk-averse preference of the decision-maker, and thus aims at deriving plans that are suf<sup>fi</sup>ciently insensitive to the in<sup>fl</sup>uence of imperfect information [78,102]. Robust optimization methods are suited for both long-term risk portfolio management and mid-term operational risk management [113]. We consider three different robustness criteria [102]: model, solution, and objective robustness. A totally model robust ‘fat solution’ design is applied to ensure decisive and feasible solutions for each scenario. While solution robustness represents a risk-neutral preference seeking for optimal results, a risk-averse decision-maker aims at objective robustness to attain a prede<sup>fi</sup>ned aspiration level [102].

With respect to the internal benchmark of the xVA concepts, i.e., that total costs of capital are covered, a decision-maker balances the upside potential (UP) of creating value (xVA>0) with the downside risk (DR) of destroying value (xVAb0), depending on the individual risk preference (risk-seeking vs. risk-averse). UP and DR correspond to <sup>fi</sup>rst-order partial moments with the internal benchmark of 0 and thus complement one another to the expected value (EV) of the entire distribution. Since corporate decision-makers are typically risk-averse [78], we focus on the weakly risk-averse spectrum of risk preferences and derive the objective function Φ in (5). pr denotes the probability of scenario s in the discrete scenario set S; Z contains the scenario-speci<sup>fi</sup>c xVA value.

$$
\begin{array}{l} \Phi (\gamma) = \gamma \cdot E V - (1 - \gamma) \cdot D R \\ = \gamma \cdot \underbrace {\sum_ {s \in S} p r _ {s} \cdot Z _ {s}} _ {\text { Expected   Value } (E V)} - (1 - \gamma) \cdot \underbrace {\sum_ {s \in S} p r _ {s} \cdot m a x \{0 ; - Z _ {s} \}} _ {\text { Downside   Risk } (D R)} \end{array}\tag{5}
$$

A linear implementation of (5) is provided in (6); (7) and (8) are required to linearize the calculation of DR. D denotes the downward deviation of the performance metric Z for scenario s from the internal benchmark of 0.

$$
\max \quad \gamma \cdot \sum_ {s \in S} p r _ {s} \cdot Z _ {s} - (1 - \gamma) \cdot \sum_ {s \in S} p r _ {s} \cdot D _ {s}\tag{6}
$$

$$
Z _ {s} + D _ {s} \geq 0 \quad \forall s \in S\tag{7}
$$

$$
D _ {s} \geq 0 \quad \forall s \in S\tag{8}
$$

In two-stage stochastic programming, the results of the deterministic wait-and-see (WS) approach can be compared against the stochastic here-and-now (HN) approach [14]. The gap between both approaches equals the economic impact of incomplete information (Expected Value of Perfect Information, EVPI) [14]. In (6), we obtain relative solution robustness for a risk-neutral decision-maker (γ=1) with a minimal EVPI [102]. For γ → 0, a risk-averse decision-maker focuses on objective robustness and reduces DR at the cost of a substantial loss in UP (see Fig. 3). The risk preference of the decision-maker should be determined in retrospect by balancing upside potential against downside risk for different parameter values of γ.

Besides the three robustness criteria introduced above, we consider information robustness [102] and require decisions to be suf<sup>fi</sup>ciently independent of the level of information applied in the decision model [11]. Since the level of information increases with the size of the scenario set [28], the decision-maker has to determine a relatively information robust size of the scenario set that is still manageable with respect to the resulting contingency plans. Hahn and Kuhn [45] examine different sizes of the scenario set, and conclude that a scenario set of size of 5 to 7 can be considered relatively information robust depending on the underlying probability distribution.

![](/api/attachments/YXDKTXPB/fulltext/images/43b641c21d7b7ee513d49d2361e4aa0196213bdb12f813e7c52fed022c81613e.jpg)  
Fig. 3. Upside potential vs. downside risk depending on risk preference.

Furthermore, robustness involves the trade-off between decision stability and <sup>fl</sup>exibility [102]. In two-stage stochastic programming, structural <sup>fi</sup>rst-stage decisions are determined here-and-now to obtain stability irrespective of the realized scenario [14]. Second-stage control variables allow for <sup>fl</sup>exibility since decisions can be postponed until the actual scenario is realized (wait-and-see) [102]. In a multiperiod approach, <sup>fi</sup>rst-stage decisions are determined for the entire planning period omitting <sup>fl</sup>exibility potential due to the postponement and revision of decisions beyond the frozen horizon. Multistage stochastic programming approaches are therefore advocated [53], but require a relatively high amount of accurate and detailed information compared to a two-stage approach [102].

Sequential two-stage approaches with rolling horizons are therefore discussed [102] applying a postponement approach to consider the shorter frozen period for structural decisions, as opposed to the entire planning period in common approaches [46]. In the postponement (PP) approach, structural variables are modeled as scenario-speci<sup>fi</sup>c decision variables, but identical values for all scenarios are required in the frozen period [46]. WS and HN approaches evolve as limiting cases of the PP approach for frozen horizons before and at the end of the planning period. The <sup>fl</sup>exibility introduced with the PP approach improves expected value creation and mitigates risk impact as the gap versus the WS approach is reduced (see Fig. 3).

## 4. Conclusions and research perspectives

This paper presents a comprehensive approach to designing modeldriven DSS in Value-based Management (VBM). A conceptual architecture for integrated business planning is derived from a literature survey providing the foundation for a model-driven approach to VBM. In contrast to common explanatory frameworks and data-driven concepts such as value driver trees and risk-adjusted parameters, we develop a model-driven approach for integrated performance and risk optimization. Opportunities for further research are identi<sup>fi</sup>ed as part of the literature survey.

The Integrated Business Planning (IBP) matrix is derived from a literature survey as a comprehensive conceptual architecture for model-driven DSS in corporate planning. The IBP matrix follows the hierarchical planning paradigm distinguishing three different planning levels and provides an integrated perspective on pro<sup>fi</sup>t, cash <sup>fl</sup>ow, and risk considerations. The IBP matrix de<sup>fi</sup>nes major domains covering related subdomains and decision-relevant aspects that can serve as a blueprint to con<sup>fi</sup>gure and coordinate corresponding modular DSS for value-based corporate planning. Summarizing various decisionoriented approaches in the literature, we outline the bene<sup>fi</sup>ts of a value-based approach compared to a common approach that optimizes the physical and <sup>fi</sup>nancial dimension of business sequentially.

A uni<sup>fi</sup>ed modeling approach for integrated value-based performance and risk optimization is developed using Value Added (xVA) concepts for performance management and robust optimization methods for risk management. A risk-based adaptation of the xVA concept is used to develop a decision-oriented approach to risk management explicitly taking into account the risk(-averse) preference of the decision-maker. Multiple aspects of robust planning and different criteria for robust decisions are examined to outline their bene<sup>fi</sup>ts in a two-stage stochastic programming approach.

The literature survey identi<sup>fi</sup>es several perspectives for further research at the different levels of the IBP matrix. At the long-term level of strategic performance and risk management, decisionoriented aspects of further business domains such as supplier, customer, and employee lifecycle management should be integrated into decision models for strategic supply chain design. Since an integrated approach to value-based performance and risk management has not yet been implemented at the long-term level, a corresponding approach using the Market Value Added (MVA) concept should be investigated using a case-oriented application. Coordination with mid-term corporate management should also be further examined to analyze the bene<sup>fi</sup>ts of using coherent xVA concepts at both levels.

Although sales and operations management and project portfolio management cover two different perspectives on business (run vs. change) at the mid-term level, they are closely interlinked since change initiatives in<sup>fl</sup>uence run parameters and both domains partially compete for the same resources. Consequently, integrated approaches to sales, operations, and project portfolio management should be investigated. Alternatively, a hierarchical coordination approach via longterm strategic business development could be considered. Furthermore, integrated/distributed decision-making concepts should be analogously developed for the level of short-term corporate management taking value-based considerations into account.

## Acknowledgments

We thank the anonymous referee for the valuable feedback, which has helped to improve the paper substantially.

## References

[1] H. Ahn, M. Gumus, P. Kaminsky, Pricing and manufacturing decisions when demand is a function of prices in multiple periods, Operations Research 55 (2007) 1039–1057.

[2] D.R. Anderson, D.J. Sweeney, T.A. Williams, R.K. Martin, An introduction to management science: quantitative approaches to decision making, South-Western, Mason, twelfth ed., 2008.

[3] G.E. Applequist, J.F. Pekny, G.V. Reklaitis, Risk and uncertainty in managing chemical manufacturing supply chains, Computers and Chemical Engineering 24 (2000) 2211–2222.

[4] R.W. Ashford, R.H. Berry, R.G. Dyson, Operational research and <sup>fi</sup>nancial management, European Journal of Operational Research 36 (1988) 143–152.

[5] B. Back, R.J.R. Back, Financial statement planning in the presence of tax constraints, European Journal of Operational Research 85 (1995) 66–81.

[6] M. Badell, E. Fernandeza, G. Guillen, L. Puigjaner, Empowering <sup>fi</sup>nancial tradeoff with joint <sup>fi</sup>nancial and supply chain planning models, Mathematical and Computer Modelling 46 (2007) 12–23.

[7] M.J. Bagajewicz, On the role of microeconomics, planning, and <sup>fi</sup>nances in product design, AICHE Journal 53 (2007) 3155–3170.

[8] K.R. Baker, W.W. Damon, A simultaneous planning model for production and working capital, Decision Sciences 8 (1977) 95–108.

[9] A. Barbaro, M.J. Bagajewicz, Managing <sup>fi</sup>nancial risk in planning under uncertainty, AICHE Journal 50 (2004) 963–989.

[10] R. Baseman, W. Grey, Method for integrated supply chain and <sup>fi</sup>nancial management, Patent, US 6671673, 2003.

[11] G. Bayraksan, D.P. Morton, Assessing solution quality in stochastic programs, Mathematical Programming 108 (2006) 495–514.

[12] R. Bernhard, Mathematical programming models for capital budgeting: a survey, generalization, and critique, Journal of Financial and Quantitative Analysis 4 (1969) 111–158.

[13] S. Bertel, P. Fenies, O. Roux, Optimal cash <sup>fl</sup>ow and operational planning in a company supply chain, International Journal of Computer Integrated Manufacturing 21 (2008) 440–454

[14] J.R. Birge, F. Louveaux, Introduction to stochastic programming, Springer, New York 1997.

[15] S. Biswas, Y. Narahari, Object oriented modeling and decision support for supply chains, European Journal of Operational Research 153 (2004) 704–726.

[16] J.R. Bradley, B.C. Arntzen, The simultaneous planning of production, capacity, and inventory in seasonal demand environments, Operations Research 47 (1999) 795–806.

[17] R.A. Brealey, S.C. Myers, A.J. Marcus, Fundamentals of corporate <sup>fi</sup>nance, sixth ed McGraw-Hill/Irwin, Boston, 2009.

[18] I.E. Brick, W.G. Mellon, J. Surkis, M. Mohl, Optimal capital structure: a multiperiod programming model for use in <sup>fi</sup>nancial planning, Journal of Banking & Finance 7 (1983) 45–67.

[19] P. Brucker, A. Drexl, R. Mohring, K. Neumann, E. Pesch, Resource-constrained project scheduling: notation, classi<sup>fi</sup>cation, models, and methods, European Journal of Operational Research 112 (1999) 3–41.

[20] W. Bühler, H. Gehring, Short-term <sup>fi</sup>nancial planning with uncertain receipts and disbursements, European Journal of Operational Research 2 (1978) 313–326.

[21] J. Cai, X. Liu, Z. Xiao, J. Liu, Improving supply chain performance management: a systematic approach to analyzing iterative KPI accomplishment, Decision Support Systems 46 (2009) 512–521.

[22] W.T. Carleton, An analytical model for long-range <sup>fi</sup>nancial planning, Journal of Finance 25 (1970) 291–315.

[23] A. Charnes, W.W. Cooper, M.H. Miller, Application of linear programming to <sup>fi</sup>nancial budgeting and the costing of funds, Journal of Business 32 (1959) 20–46.

[24] Z.L. Chen, N.G. Hall, The coordination of pricing and scheduling decisions, Manufacturing & Service Operations Management 12 (2010) 77–92.

[25] M. Christopher, L. Ryals, Supply chain strategy: its impact on shareholder value, International Journal of Logistics Management 10 (1999) 1–10.

[26] M. Comelli, P. Fenies, N. Tcherneva, A combined <sup>fi</sup>nancial and physical <sup>fl</sup>ows evaluation for logistic process and tactical production planning: application in a company supply chain, International Journal of Production Economics 112 (2008) 77–95.

[27] W.W. Damon, R. Schramm, A simultaneous decision model for production, marketing and <sup>fi</sup>nance, Management Science 19 (1972) 161–172.

[28] N.D. Domenica, G. Mitra, P. Valente, G. Birbilis, Stochastic programming and scenario generation within a simulation framework: an information system perspective, Decision Support Systems 42 (2007) 2197–2218.

[29] A. Drexl, A. Kimms, Lot sizing and scheduling: survey and extensions, European Journal of Operational Research 99 (1997) 221–235.

[30] G. Fandel, M. Stammen, A general model for extended strategic supply chain management with emphasis on product life cycles including development and recycling, International Journal of Production Economics 89 (2004) 293–308.

[31] Y. Feng, S.D. Amours, R. Beauregard, The value of sales and operations planning in oriented strand board industry with make-to-order manufacturing system: cross functional integration under deterministic demand and spot market recourse, International Journal of Production Economics 115 (2008) 189–209.

[32] R. Fischer, Business planning with SAP SEM, Galileo Press, Bonn, 2004.

[33] J. Fisk, An interactive game for production and <sup>fi</sup>nancial planning, Computers and Operations Research 7 (1980) 157–168.

[34] M. Fleischmann, J.M. Bloemhof-Ruwaard, R. Dekker, E. van der Laan, J.A.E.E. van Nunen, L.N. van Wassenhove, Quantitative models for reverse logistics: a review, European Journal of Operational Research 103 (1997) 1–17.

[35] B. Fleischmann, H. Meyr, M. Wagner, Advanced planning, in: H. Stadtler, C. Kilger (Eds.), Supply chain management and advanced planning, Springer, Berlin, 2008, pp. 81–106.

[36] J.A. Gentry, State of the art of short-run <sup>fi</sup>nancial management, Financial Management 17 (1988) 41–57.

[37] F. Ghasemzadeh, N.P. Archer, Project portfolio selection through decision support, Decision Support Systems 29 (2000) 73–88

[38] M. Goetschalckx, B. Fleischmann, Strategic network design, in: H. Stadtler, C. Kilger (Eds.), Supply chain management and advanced planning, Springer, Berlin, 2008, pp. 117–132.

[39] G. Gregory, Cash <sup>fl</sup>ow models: a review, Omega 4 (1976) 643–656.

[40] I.E. Grossmann, Enterprise-wide optimization: a new frontier in process system engineering, AICHE Journal 51 (2005) 1846–1857.

[41] G. Guillen, M.J. Bagajewicz, S.E. Sequeira, A. Espuna, L. Puigjaner, Management of pricing policies and <sup>fi</sup>nancial risk as a key element for short term scheduling optimization, Industrial and Engineering Chemistry Research 44 (2005) 557–575.

[42] G. Guillen, M. Badell, L. Puigjaner, A holistic framework for short-term supply chain management integrating production and corporate <sup>fi</sup>nancial planning International Journal of Production Economics 106 (2007) 288–306.

[43] S. Güven, A. Kaynarca, An integrated investment and <sup>fi</sup>nancial planning model International Transactions in Operational Research 5 (1998) 123–136.

[44] G.J. Hahn, H. Kuhn, Optimising a value-based performance indicator in mid-term sales and operations planning, Journal of the Operational Research Society 62 (2011) 515–525.

[45] G.J. Hahn, H. Kuhn, Value-based performance and risk management: a robust optimization approach International Journal of Production Economics (2011) doi:10.1016/ijipe 2011.04.002

[46] G.J. Hahn, H. Kuhn, Simultaneous investment, operations, and <sup>fi</sup>nancial planning in supply chains: a value-based optimization approach, International Journal of Production Economics (2012) doi:10.1016/i.jipe 2012.02.018.

[47] W.F. Hamilton, M.A. Moses, An optimization model for corporate <sup>fi</sup>nancial planning, Operations Research 21 (1973) 677–692.

[48] D.M. Hanink, A mean-variance model of MNF location strategy, Journal of International Business Studies 16 (1985) 165–170.

[49] W. Herroelen, R. Leus, Project scheduling under uncertainty: survey and research potentials, European Journal of Operational Research 165 (2005) 289–306.

[50] J.E. Hodder, Financial market approaches to facility location under uncertainty, Operations Research 32 (1984) 1374–1380.

[51] J.E. Hodder, M.C. Dincer, A multifactor model for international plant location and <sup>fi</sup>nancing under uncertainty, Computers and Operations Research 13 (1986) 601–609.

[52] C.W. Holsapple, M.P. Sena, ERP plans and decision-support bene<sup>fi</sup>ts, Decision Support Systems 38 (2005) 575–590.

[53] K. Huang, S. Ahmed, The value of multistage stochastic programming in capacity planning under uncertainty, Operations Research 57 (2009) 893–904.

[54] Y. Ijiri, F.K. Levy, R.C. Lyon, A linear programming model for budgeting and <sup>fi</sup>- nancial planning, Journal of Accounting Research 1 (1963) 198–212.

[55] F.R. Jacobs, E. Bendoly, Enterprise resource planning: developments and directions for operations management research, European Journal of Operational Re search 146 (2003).233-240

[56] J.G. Kallberg, R.W. White, W.T. Ziemba, Short term <sup>fi</sup>nancial planning under uncertainty, Management Science 28 (1982) 670–682

[57] M. Kannegiesser, H.O. Günther, P. van Beek, M. Grunow, C. Habla, Value chain management for commodities: a case study from the chemical industry, OR Spectrum 31 (2009) 63–93.

[58] R.S. Kaplan, A.A. Atkinson, Advanced management accounting, third ed. Prentice-Hall, Upper Saddle River, 1998.

[59] Ö. Kirca, M.M. Köksalan, An integrated production and <sup>fi</sup>nancial planning model: an application, IIE Transactions 28 (1996) 677–686.

[60] W. Klibi, A. Martel, A. Guitouni, The design of robust value-creating supply chain networks: a critical review, European Journal of Operational Research 203 (2010) 283–293.

[61] V. Krishnan, K.T. Ulrich, Product development decisions: a review of the literature, Management Science 47 (2001) 1–21.

[62] J.M. Lainez, G. Guillen-Gosalbez, M. Badell, A. Espuna, L. Puigjaner, Enhancing corporate value in the optimal design of chemical supply chains, Industrial and Engineering Chemistry Research 46 (2007) 7739–7757.

[63] J.M. Lainez, L. Puigjaner, G.V. Reklaitis, Financial and <sup>fi</sup>nancial engineering considerations in supply chain and product development pipeline management, Computers and Chemical Engineering 33 (2009) 1999–2011.

[64] D.M. Lambert, T.L. Pohlen, Supply chain metrics, International Journal of Logistics Management 12 (2001) 1–20

[65] J. Lavaja, A. Adler, J. Jones, T. Pham, K. Smart, D. Splinter, M. Steele, M.J. Bagajewicz, Financial risk management for investment planning of new commodities considering plant location and budgeting, Industrial and Engineering Chemistry Research 45 (2006) 7582–7591.

[66] S.C.H. Leung, S.O.S. Tsang, W.L. Ng, Y. Wu, A robust optimization model for multi-site production planning problem in an uncertain environment, European Journal of Operational Research 181 (2007) 224–238

[67] Z. Lieber, Y.E. Orgler, An integrated model for accounts receivable management, Management Science 22 (1975) 212–219.

[68] P. Longinidis, M.C. Georgiadis, Integration of <sup>fi</sup>nancial statement analysis in the optimal design of supply chain networks under demand uncertainty, International Journal of Production Economics 129 (2011) 262–276

[69] S.F. Maier, J.H. Vander Weide, A practical approach to short-run <sup>fi</sup>nancial planning, Financial Management 7 (1978) 10–16.

[70] S. Majumdar, D. Chattopadhyay, A model for integrated analysis of generation capacity expansion and <sup>fi</sup>nancial planning, IEEE Transactions on Power Systems 14 (1999) 466–471.

[71] J.C.T. Mao, Application of linear programming to short-term <sup>fi</sup>nancing decision, The Engineering Economist 13 (1968) 221–241.

[72] R.E. McGaughey, A. Gunasekaran, Enterprise resource planning (ERP): past, present and future, International Journal of Enterprise Information Systems 3 (2007) 23–35.

[73] J.M. McInnes, W.J. Carleton, Theory, models and implementation in <sup>fi</sup>nancial management, Management Science 28 (1982) 957–978.

[74] H. Meyr, M. Wagner, J. Rohde, Structure of advanced planning systems, in: H. Stadtler, C. Kilger (Eds.), Supply chain management and advanced planning, Springer, Berlin, 2008, pp. 109–115.

[75] H. Min, G. Zhou, Supply chain modeling: past, present and future, Computers and Industrial Engineering 43 (2002) 231–249.

[76] C. Møller, ERP II: a conceptual framework for next-generation enterprise systems? Journal of Enterprise Information Management 18 (2005) 483–497.

[77] Y. Moon, Enterprise resource planning (ERP): a review of the literature, International Journal of Management and Enterprise Development 4 (2007) 235–264.

[78] J.M. Mulvey, R.J. Vanderbei, S.J. Zenios, Robust optimization of large-scale systems, Operations Research 43 (1995) 264–281.

[79] S.C. Myers, G.A. Pogue, A programming approach to corporate <sup>fi</sup>nancial management, Journal of Finance 29 (1974) 579–599.

[80] W.L.J. Ness, A linear programming approach to <sup>fi</sup>nancing the multinational corporation, Financial Management 1 (1972) 88–100.

[81] S. Nickel, F. Saldanha-da Gama, H.P. Ziegler, A multi-stage stochastic supply network design problem with <sup>fi</sup>nancial decisions and risk management, Omega 40 (2012) 511-524

[82] C. Nobes, R.B. Parker, Comparative international accounting, tenth ed. Prentice-Hall, Harlow, 2008.

[83] D.L. Olson, D.D. Wu, Enterprise risk management, World Scienti<sup>fi</sup>c, Singapore, 2008.

[84] Y.E. Orgler, An unequal-period model for cash management decisions, Management Science 16 (1969) B77–B92

[85] F. Pan, R. Nagi, Robust supply chain design under uncertain demand in agile manufacturing, Computers and Operations Research 37 (2010) 668–683.

[86] J.W. Petty II, E.W. Walker, Optimal transfer pricing for the multinational <sup>fi</sup>rm, Financial Management 1 (1972) 74–87.

[87] M.S. Pishvaee, M. Rabbani, S.A. Torabi, A robust optimization approach to closedloop supply chain network design under uncertainty, Applied Mathematical Modelling 35 (2011) 637–649.

[88] A. Pongsakdi, P. Rangsunvigit, K. Siemanond, M.J. Bagajewicz, Financial risk management in the planning of re<sup>fi</sup>nery operations, International Journal of Production Economics 103 (2006) 64–86.

[89] C.A. Poojari, C. Lucas, G. Mitra, Robust solutions and risk measures for a supply chain planning problem under uncertainty, Journal of the Operational Research Society 59 (2008) 2–12.

[90] D.J. Power, R. Sharda, Model-driven decision support systems: concepts and research directions, Decision Support Systems 43 (2007) 1044–1061.

[91] L. Puigjaner, G. Guillen, Towards an integrated framework for supply chain management in the batch chemical process industry, Computers and Chemical Engineering 32 (2008) 650–670.

[92] L. Puigjaner, J.M. Lainez, Capturing dynamics in integrated supply chain management, Computers and Chemical Engineering 32 (2008) 2582–2605.

[93] L. Qi, Z.J.M. Shen, L.V. Snyder, The effect of supply disruptions on supply chain design decisions, Transportation Science 44 (2010) 274–289.

[94] R. Quante, H. Meyr, M. Fleischmann, Revenue management and demand ful<sup>fi</sup>llment: matching applications, models, and software, OR Spectrum 31 (2009) 31–62.

[95] A. Rappaport, Creating shareholder value: a guide for managers and investors, second ed. Free Press, New York, 1998.

[96] C. Reibis, Zieloptimale Jahresabschlussplanung durch Einsatz mehrperiodiger bilanzpolitischer Entscheidungsmodelle, Zeitschrift für Planung & Unternehmenssteuerung 17 (2006) 99–122.

[97] B. Reuter, J. Rohde, Coordination and integration, in: H. Stadtler, C. Kilger (Eds.), Supply chain management and advanced planning, Springer, Berlin, 2008, pp. 247–261.

[98] B. Ritchie, C. Brindley, Supply chain risk management and performance, International Journal of Physical Distribution and Logistics Management 27 (2007) 303–322.

[99] A.A. Robichek, D. Teichroew, J.M. Jones, Optimal short term <sup>fi</sup>nancing decision, Management Science 12 (1965) 1–36.

[100] J. Romero, M. Badell, M. Bagajewicz, L. Puigjaner, Integrating budgeting models into scheduling and planning models for the chemical batch industry, Industrial and Engineering Chemistry Research 42 (2003) 6125–6134

[101] C. Schneeweiss, Distributed decision making, second ed. Springer, Berlin, 2003.

[102] A. Scholl, Robuste Planung und Optimierung: Grundlagen, Konzepte und Methoden, experimentelle Untersuchungen, Physica, Heidelberg, 2001.

[103] J.F. Shapiro, Modeling the supply chain, second ed. Thomson-Brooks/Cole, Belmont, 2007.

[104] E.M. Shehab, M.W. Sharp, L. Supramaniam, T. Spedding, Enterprise resource planning: an integrative review, Business Process Management Journal 10 (2004) 359–386.

[105] J.P. Shim, M. Warkentin, J.F. Courtney, D.J. Power, R. Sharda, C. Carlsson, Past present, and future of decision support technology, Decision Support Systems 33 (2002) 111–126.

[106] K.V. Smith, State of the art of working capital management, Financial Management 2 (1973) 50–55.

[107] L.V. Snyder, M.P. Scaparra, M.S. Daskin, R.L. Church, Planning for disruptions in supply chain networks, TutORials in Operations Research, 2006.

[108] M.S. Sodhi LP modeling for asset-liability management: a survey of choices and simpli<sup>fi</sup>cations, Operations Research 53 (2005) 181–196.

[109] M.S. Sodhi, C.S. Tang, Modeling supply-chain planning under demand uncertainty using stochastic programming: a survey motivated by asset–liability management, International Journal of Production Economics 121 (2009) 728–738.

[110] V. Srinivasan, Y.H. Kim, Decision support for integrated cash management, Decision Support Systems 2 (1986) 347–363.

[111] H. Stadtler, Supply chain management and advanced planning: basics, overview and challenges, European Journal of Operational Research 163 (2005) 575–588.

[112] C.S. Tang, Perspectives in supply chain risk management, International Journal of Production Economics 103 (2006) 451–488.

[113] O. Tang, S.N. Musa, Identifying risk issues and research advancements in supply chain risk management, International Journal of Production Economics 133 (2010) 25–34.

[114] V.A. Varma, G.V. Reklaitis, G.E. Blau, J.F. Pekny, Enterprise-wide modeling & optimization: an overview of emerging research challenges and opportunities, Computers and Chemical Engineering 31 (2007) 692–711.

[115] D. Walters, The implications of shareholder value planning and management for logistics decision making, International Journal of Physical Distribution and Logistics Management 29 (1999) 240–258.

[116] C.D.J. Waters, Supply chain risk management: vulnerability and resilience in logistics, Kogan Page, London, 2007.

[117] X. Xu, J.R. Birge, Equity valuation, production, and <sup>fi</sup>nancial planning: a stochastic programming approach, Naval Research Logistics 53 (2006) 641–655.

[118] G. Yi, G.V. Reklaitis, Optimal design of batch-storage network with <sup>fi</sup>nancial transactions and cash <sup>fl</sup>ows, AICHE Journal 50 (2004) 2849–2865.

[119] F. You, J.M. Wassick, I.E. Grossmann, Risk management for a global supply chain planning under uncertainty: models and algorithms, AICHE Journal 55 (2009) 931–946.

[120] S.D. Young, S.F. O'Byrne, EVA and value-based management: a practical guide to implementation, McGraw-Hill, New York, 2001.

[121] C.S. Yu, H.L. Li, A robust optimization model for stochastic logistic problems, International Journal of Production Economics 64 (2000) 385–397.

![](/api/attachments/YXDKTXPB/fulltext/images/ed7b01a5b9d4b8ede9a3231dbd3472bb2feeca2f4660a2cea7731fe6f13ae7e2.jpg)

Heinrich Kuhn is a Full Professor for Supply Chain Management & Operations at the Catholic University of Eichstaett-Ingolstadt, Germany and a Guest Professor at the Free University of Bozen, Italy. Before that, he was an Assistant Professor at the University of Cologne, Germany (1994– 1997) and a Teaching and Research Assistant at the Technical University of Brunswick, Germany (1990–1994). He received his Ph.D. (1990) in Industrial Engineering from the Technical University of Darmstadt, Germany, and the degree of Habilitation (1997) in Business Administration from the Universit of Cologne, Germany. He is a co-author of the textbook Flexible Manufacturing Systems–Decision Support for Design and Operation, published by Wiley, New York, 1993.

In addition to that, he is author and co-author of numerous articles published in Naval Research Logistics, IIE Transactions, International Journal of Production Research, International Journal of Production Economics, European Journal of Operational Research, OR Spectrum, and International Journal of Flexible Manufacturing Systems. Heinrich Kuhn is an Associate Editor for Omega, the International Journal of Management Science. His research interests focus on performance analysis of production systems, lot-sizing and resource scheduling and inventory management with an industry focus on automotive and semiconductor industry as well as consumer goods and retail.

![](/api/attachments/YXDKTXPB/fulltext/images/5c4d6c88dacd2ed6d45c661ea72652eef61fa0b1ac6d544dcbea4c993fac2ec7.jpg)

Gerd I. Hahn is a Proiect Manager with a management consultancy and an external Postdoctoral Research Associate in Supply Chain Management & Operations at the Catholic University of Eichstaett-Ingolstadt, Germany. He holds a Diploma in Business Administration, and received his Ph.D. in Management Science from Catholic University of Eichstaett-Ingolstadt in 2011. His research has been published in the Journal of the Operational Research Society, the International Journal of Production Economics. and several conference proceedings. Gerd J. Hahn has presented his work at the European Conference on Operational Research, the International Working Seminar on Production Economics, and the INFORMS Annual Meeting. His research interests focus on decision support systems in supply chain management, supply chain performance and risk management, and robust optimization methods.
