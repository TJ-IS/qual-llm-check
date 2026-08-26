---
otero_id: 4082
otero_key: "3HGVK8HR"
title: "A Decision Support System for evaluating operations investments in high-technology business"
authors: "Adolfo Crespo Marquez; Carol Blanchar"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.08.012"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Decision Support System for evaluating operations investments in high-technology business

Adolfo Crespo Marquez <sup>a,\*</sup>, Carol Blanchar <sup>b,1</sup>

<sup>a</sup>Department of Industrial Management, School of Engineering. University of Seville.Camino de los Descubrimientos s/n. 41092 Sevilla, Spain <sup>b</sup>Analysis of Operational Investment Alternatives, Conexo, Inc., 1909 Magdalena Circle # 75, Santa Clara, CA. USA

Received 23 July 2003; received in revised form 12 August 2004; accepted 16 August 2004 Available online 17 September 2004

## Abstract

The evolution in the way that businesses approach markets has been a frequent literature topic in the last few years. In the high-tech industry, even the most successful companies have been mainly focused on the features of their products and processes, trying to develop their technology to gain a price/performance advantage, and thereby protect or increase market share. However, this approach is disconnected from their beliefs about what target customers really care about, nor does it is consider which of those underlying assumptions are most critical to business growth in share, revenue, and profit. This paper proposes a Decision Support System (DSS) to connect customer value to business targets, providing scenarios to show the customer responses and business results that will enable future funding, with optimization techniques to compare alternatives

The first step is for business planners to characterize their target market by formalizing what are often informal but deeply held beliefs about what drives their customers’ purchase decisions. They create a list of attributes that together define customer value, the basis on which customers in the target market compare and select from competing products. With that attribute list, planners sometimes are able to go further and segment their market by grouping customers together who put top priority on the same attributes. This system dynamics model connects planned investments to expected improvements in the customer’s perception of those critical attributes, (relative to the competition), and thus increase sales, revenue, and market share. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Decision Support Systems; System dynamics models; Investments evaluation; Product life cycle management; Supply chain management; Channel strategy; New product introduction; Solution selling; Solution integration; Product awareness; Pricing

## 1. Introduction

Decision Support Systems (DSSs) are tools that an organization uses to support and enhance decisionmaking activities [1]. Early use of decision support analysis was marketing Decision Support Systems (MDSS), defined [11] as a coordinated collection of data, system, tools and technology, with supporting software and hardware by which an organization gathers and interprets information from business and environment and turns it into a basis for marketing action.

Within the field of marketing, Higby and Farah [6] found that in the US, 32% of the companies have installed some form of marketing DSS (based on a survey among 212 executives.); In the Netherlands, Van Campen et al. [25] estimated the penetration of Decision Support Systems in marketing at 37% (based on a survey of 525 companies with over 10 employees and marketing manager present). The fact that current formal marketing plans incorporate information resources in 95.2% of the firms, compared to incorporation in 76.2% of the firms’ strategic business plans [10], illustrates about the importance of MDSS at present.

Companies and business planners have recognized the strategic importance of MDSS and are stepping up their investments in information technology for marketing [21] Adoption of MDSS is higher in companies with consumer products compared to industrial (business-to-business) products companies, and in companies with more market information available [27].

Their objective is to support a decision making process which is primarily a matter of reasoning (using the mental models of the manager) and analogizing (based on stories about similar events retained in mind). For instance, Van Bruggen et al. [24] found that managers who use a DSS are less inclined to anchor their decisions on earlier decisions compared with managers who do not use the system. Similarly, these authors found that the incorporation of model-based results into a DSS is especially beneficial. Prominence effects, overconfidence and other biases are reduced for managers who use modelbased DSSs relative to managers who do not. In the literature, we find that although the applicability of some marketing models to real-world problems has been questioned [22], there have been many examples of successful marketing model applications (see, for instance, Refs. [12,14]).

Beyond marketing, others of these model applications are within the new products area [9], trying to understand the dynamics between changing demand and the entry and exit behaviors of competitors in the market place. These works model demand and number of competitors simultaneously and empirically investigates some high-tech markets. Still other models try to bridge between new product introduction and marketing to understand the relationship between the number of competitors and the rate of technology diffusion [2], or to tie conceptual design in a new product introduction with cost modeling and marketing considerations [26].

In this paper, however, we go further to model product design and marketing innovations to anticipate and explain the way collaborative teams, both within firms and between partner businesses, may gain and retain customers in a very competitive hightech marketplace. The model also considers the expected response of a changing set of competitors. In this work, we pay special attention to the characterization of the customer behavior, and we use system dynamics to build our simulation model<sup>2</sup>. The simulation model confirms through team review that we have captured the behaviors that explain their customer segment response to changes in product attributes and price, creating collective understanding of the existing business environment, and able to be validated by historical data when available. This can be transformed into a DSS model by examining the impact on share, revenue, and profit from engineering and manufacturing changes made to product attributes and prices, as well as changes made to influence the customer’s perceptions, given what we believe to be true about the business dynamics. We show an example of the model used as a framework for a scenario (simulation) where business planners may explore specific product improvement strategies. The simulations calculate expected results in the context of current competitor investment and response, and planners can choose strategies to best meet business (financial and operational) targets and forecasts.

The rest of the paper is organized as follows: In Section 2, we characterize high-tech business planning today, with multiple dimensions of business organization, solution architecture, channel strategy, and changing segment needs, and with each dimension changing over time. In Section 3, we introduce a model using the System Dynamics methodology, proven effective for quickly simulating and understanding dynamic, non-linear behavior as a basis for collaborative decisions. Sections 4–6 are devoted to the explanation of the consumer purchasing behavior, financial and investments sub-models respectively. Example simulation results are presented in Section 7, generated from both quantitative and qualitative data inputs, a critical requirement in today’s fast-changing global marketplace, and we also suggest a generic scenario as a starting point. This section also explains how this model can rapidly be transformed into a Decision Support System for collaborative planning, along with some optimization capabilities to answer several possible questions with the purpose of improving business planning under different scenarios. In Section 8, we discuss our results to date and managerial implications of the high-tech Business Decision Support System. Finally, Section 9 concludes the paper with a summary of our findings and some useful directions for future research.

## 2. A characterization of high-tech business planning process complexity

Business planning within a high-tech environment is both dynamic and complex, with a critical need for nonlinear, relational input and mathematical rigor. This is especially the case where planners and decision-makers must rely on subjective and potentially biased data [7], and where data sources span across cultures and languages.

Relational input is important where projections of both market demand and competitive position are essential inputs to strategy [4,19]. There is simply not a large enough sample of good data to get statistically valid outcomes on the basis of projections from past trends and patterns, nor are there controlled representative data sources, to support correlations or regression analysis.

For all these reasons, planners increasingly turn to simulations to build confidence and consensus in selecting operational investments to improve or protect market share, revenue, and profit for global high-tech businesses. Adding the ability to analyze decisions in light of the impact on share, revenue and profits turns the simulation model into a decision support system.

The reader needs to understand that many hightech planners are more interested in share as a business metric than either revenue or profit (notice that market share may be widely used, but can be sometimes a very poor performance metric. Absolute sales volume could be preferable, since it is directly traceable to customer gains and losses. For instance, 90% of a tiny market could contribute less to earnings than 25% of a large market). This is closely tied to the fast pace of technology and product life cycles, and the increasing difficulty of trying to gain market share as the market matures. In addition, market share is tracked and reported in trade and investment publications and watched closely by investors and analysts looking for visible short-term results to publicized strategy.

As a first step in the introduction of a model that can meet these needs, let us summarize the unique characteristics of the high-tech marketplace:

– Volatile, uncertain markets with great pressure on managers for near-term market share and/or financial performance (In US, high-tech programs and product lines may be funded for a period of time in spite of poor financial results if they prove themselves, quarter by quarter, able to capture and hold share in strategic markets).

– Multiple planning dimensions, including technology path, product architecture, delivery chain, alliances, channels, and services.

– Little historical data, due to technology adoption rates, reorganizations, mergers and acquisitions, globalization, and new channels for order and distribution.

– Isolated groups of expert knowledge, each with their own language and systems.

– Absence of a single view of the possible impact of an investment, especially when results are scattered across space and time, well beyond the scope of any single enterprise planning system.

## 3. A general overview of a model for a high-tech business and marketplace

Fig. 1 is a representation of numerous planning team dialogues about the way business grows when it offers a valuable product to an existing market. The diagram links operational investment, conditioned by policy, to business revenue growth over a financial year. In this way, financial constraints are introduced into the model. Obviously, the higher the growth at a reasonable margin, the greater the level of investments that are available for the next year.

This simplified diagram does not show all the exogenous and endogenous factors that condition results over time, and that are included in this model for a valid simulation. For many reasons, business planners know that over time, it takes more dollars of investment to maintain the same level or to grow share the same amount (this, of course, does not apply to all cases, e.g. if a big rival has failed, the firm may be able to grow or sustain share with less expenditure), and the model indeed shows diminishing returns over time, depending on a number of factors. Most importantly, the model clearly shows why <sup>b</sup>doing nothing<sup>Q</sup> is almost never a good decision for a hightech business, and helps a business that has enjoyed great success in the past to act aggressively to protect its position for continued profit and growth.

Incremental investments are represented in this model as completely variable, even though volume ramps up or down would surely affect the return on fixed costs. We do not include a fixed costs component simply because none of the financial or strategic planners among the companies we worked with have done so. Industry practice is to build fixed costs into overhead rates as part of labor, material, and overhead in internal part costs, or priced into purchased parts, and are not visible to our clients nor used by them when they evaluate and compare business plans.

![](/api/attachments/3HGVK8HR/fulltext/images/65e73ce4b4de27e76c6e8692b2c3bbbe3b57e42704af857eab835a6bfb8e66c6.jpg)  
Fig. 1. General model overview (original team design).

The allowable change in spending level corresponds to an expected changed value of specific attributes. Note that the investment cycle is a consequence of corporate policy and regulated periods to report results and commit resources, where external economic cycles and market occur at their own pace. The model recognizes those delays between a change in spending and a resulting improvement in customer value and sales growth.

Business planners try to further group their customers in segments within the target market, according to the relative importance the buyers place on one or the other of the attributes that drive their market overall.

In a scenario, investing to improve product attributes drives positive change in customer perceptions, which are assumed by business planners to drive each competitor’s share in each segment of the overall market, and of course the related financial results.

In terms of confirmation and validation, the general model structure that we present in Fig. 1 was synthesized and refined with commercial and consumer business managers, systems analysts, critical part contract managers, financial executives, and experts in high-tech workforce collaboration. The results are represented by the three sub-models that we show in Fig. 2.

The financial model is set by reporting rules, the investment model by budget and targeting practices, and a value index computed from quality relative to price has gained wide acceptance and general industry use. In this paper, the authors compute the value index in a manner that takes advantage of the capabilities of system dynamics for the benefit of fast moving hightech industries.

## 4. Modeling customer purchasing decisions

<sup>b</sup>Purchasing<sup>Q</sup> here represents the customer’s decision to buy, and purchasing behavior is the customer response to perception of value relative to the competition. How does the customer perception of product quality and price attributes impact market share for this business and for its competitors? In this section, we will try to study this problem by formalizing the relationship among the variables involved. Before proceeding with the model development and discussion, we first describe the notations and definition of the main in the purchasing behavior model variables as follows:

![](/api/attachments/3HGVK8HR/fulltext/images/a2f07be00a425a7d9be48acb76c7657eed315151d4343c66942732439b8c1d7f.jpg)  
Fig. 2. Sub-models overview.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Subscripts:
$j=1,\ldots,N$ competitors, including this business
$s=1,\ldots,S$ segments grouped by the most important attributes
$i=1,\ldots,L$ quality attributes
$K=1,\ldots,M$ price attributes
Input: customer perception of each competitor
$Qac_{jt}^{i}$ perceived quality attribute $i$ of the competitor $j$ in $t$ $Pac_{jt}^{k}$ Perceived price attribute $k$ of the competitor $j$ in $t$ $Qab_{t}^{i}$ baseline perception of quality attribute $i$ for all competitors in $t$ $Pab_{t}^{k}$ baseline perception of price attribute $k$ for all competitors in $t$
Input: expected impact for each competitor in each segment
$Qa_{j,st}^{i}$ competitor $j$ impact on value for customers of the $s$ segment and through the quality attribute $i$ in $t$ $Pa_{jst}^{k}$ competitor $j$ impact on value for customers of the $s$ segment and through... the price attribute $k$ in $t$
Calculations: basis for comparison between competitors
$ICP_{jt}^{s}$ index of customer in segment $s$ perception of competitor $j$
Calculations: result of investment conditioned by share (reach)
$\Gamma q_{s}^{i}$ elasticity of the quality attribute $i$ for segment $s$ $\Gamma p_{s}^{k}$ elasticity of price attribute $k$ for segment $s$ $Pc_{st}^{j}$ presence of competitor $j$ in segment $s$ in $t$ $TCI_{t}^{s}$ total competitor index in segment $s$ in $t$
Output: market share change in units of solution product
$MSH_{jt}^{s}$ market-share of competitor $j$ in segment $s$ in $t$ $MST_{jt}$ market-share trend of competitor $j$ in $t$
</div>

The model can now be explained as follows: a purchaser (it could be a consumer, but also a technical or procurement manager) will most likely select a product according to widely-held perceptions about its quality $( \mathrm { Q a c } _ { j t } ^ { i } )$ and price $( \mathrm { P a c } _ { j t } ^ { \bar { k } } )$ attributes. Examples of quality attributes include reliability, ease of purchase, scalability, network friendliness, service availability, and connectivity. Examples of price attributes include rebates, promotional discounts, cost per instance of use, and channel discounts.

Once the purchaser establishes these preferences for the products of the different competitors, we can define the baseline perceptions as follows:

$$
\mathrm{Qab} _ {t} ^ {i} = \operatorname{MIN} _ {j} \left(\mathrm{Qac} _ {j t} ^ {i}\right), \text {   with   } j = 1, \dots , N\tag{1}
$$

$$
\mathrm{Pab} _ {t} ^ {k} = \mathrm{MIN} _ {j} \left(\mathrm{Pac} _ {j t} ^ {k}\right), \text {   with   } j = 1, \dots , N\tag{2}
$$

Next, we can formalize how much each attribute is able to impact on the value provided by the product to the purchaser, as follows,

$$
\mathrm{Qa} _ {j, s t} ^ {i} = \left(\mathrm{Qac} _ {j t} ^ {i} | \mathrm{Qab} _ {t} ^ {i}\right) ^ {\wedge} \Gamma q _ {s} ^ {i}\tag{3}
$$

$$
\mathrm{Pa} _ {j, s t} ^ {k} = \left(\mathrm{Pac} _ {j t} ^ {k} | \mathrm{Pab} _ {t} ^ {k}\right) ^ {\wedge} \Gamma p _ {s} ^ {k}\tag{4}
$$

In Eqs. (3) and (4), we assume that a purchaser in a segment will pay special attention to the attributes of the product most important to that segment. This concept is formalized through an index of elasticity for each price and quality attributes: $\Gamma { \mathfrak { p } } _ { s } ^ { k }$ and $\Gamma \mathbf { q } _ { s } ^ { \dot { i } } ,$ respectively (each elasticity value is calculated through the model calibration process, and then its value is maintained for the rest of the simulations). Switching costs and other factors may cause customers to be less responsive to changes in some attributes—this is represented in the model as the inherent elasticity of a quality or price attribute in a particular segment.

Once the impact on the value provided by each attribute of the product is calculated, we can formalize an index that compares the value provided by each competitor’s product, as follows:

$$
\mathrm{ICP} _ {j t} ^ {s} = \prod_ {t = 1} ^ {L} \mathrm{Qa} _ {j, s t} ^ {i} \prod_ {k = 1} ^ {M} \mathrm{Pa} _ {j, s t} ^ {k}\tag{5}
$$

Assessment of these indexes is not difficult since customer perception of their products is tracked somehow by most firms [18]. After that, the model simulates behavior for a given business by showing that the model generates correct changes in individual competitor market share for changes in value (relative to the competition), which can be validated by historical data. It is our main assumption that we can thereafter estimate the share by defined segment for each of the competitors by comparing their customer perception indices, and by assessing their presence in the marketplace $( \mathrm { P c } _ { s t } ^ { j } ) .$ , as follows:

$$
\mathrm{TCI} _ {t} ^ {s} = \sum_ {j = 1} ^ {N} \mathrm{Pc} _ {s t} ^ {j} \times \mathrm{ICP} _ {j t} ^ {s}\tag{6}
$$

$$
\mathrm{MSH} _ {j t} ^ {s} = \left(\mathrm{Pc} _ {s t} ^ {j} \times \mathrm{ICP} _ {j t} ^ {s}\right) / \mathrm{TCI} _ {t} ^ {s}\tag{7}
$$

Presence of the competitors in the market has to do with their reach in each segment. Market reach can vary from very monopolistic to very competitive, or even an almost non-existent reach in any segment.

Eqs. (6) and (7) are therefore introduced to model competitor market share in a market where competitive effects are differentially and asymmetrically distributed. Notice how this model can be considered as a simple attraction model [3] based on the hypothesis that a competitor market share is equal to its attraction relative to all others (Eq. (7)). In our case, competitor’s attraction in a segment is estimated by $( \mathrm { P c } _ { s } ^ { j } \times \mathrm { I C P } _ { j t } ^ { s } )$

The purchasing behavior model presented here was designed by modeling teams, as presented in Fig. 3, where three important competitors (or competitor proxies, where a proxy defines a competitive strategy) were considered.

Share here represents the percentage of target market segment sales that can be expected to flow to each competitor over a given time period, knowing that all the factors are continuously changing and influencing each other during that time. Overall market size remains exogenous to the model.

The leverage over time from successful product improvements is shown by the increasing slope of growth curves over time, typically in the shape of an <sup>b</sup>S<sup>Q</sup> curve, ramping from accumulating assets and then tapering off from the effects of diminishing returns.

## 5. Modeling financial implications of strategy

How does a product and market strategy impact business revenue? How is revenue over time linked to the product’s price attributes and profit? To answer these questions, we set out the variable equations formalization process, after first describing the notations and definition of the main financial model variables:

![](/api/attachments/3HGVK8HR/fulltext/images/c26b74566d0e7c7fd4e72555cc0df89c0d3dcccb775e5a6c3c44e74dae11d431.jpg)  
Fig. 3. Original team design of the purchasing behavior model for three competitors.

<table><tr><td colspan="2">Subscripts:</td></tr><tr><td> $j=1,\dots,N$ </td><td>competitors,</td></tr><tr><td> $s=1,\dots,S$ </td><td>segments by shared customer purchase priorities (as available)</td></tr><tr><td colspan="2">Input: segmented market data</td></tr><tr><td> $Tc_t$ </td><td>total potential unit sales in  $t$ </td></tr><tr><td> $Ss_t^s$ </td><td>size (% of the  $Tc_t$ ) of the segment  $s$  in  $t$ (Note that this is not a model of building and creating a market or individual segments, but of capturing and holding segment share within the strategic market as it grows or shrinks over time, by these exogenous values.)</td></tr><tr><td> $Tcs_t^s$ </td><td>total potential customers of the segment  $s$  in  $t$ </td></tr><tr><td> $S_{jt}^s$ </td><td>unit sales of competitor  $j$  per segment  $s$  in  $t$ </td></tr><tr><td colspan="2">Input: business financial targets/history allocated to this solution product</td></tr><tr><td> $Sd_{jt}$ </td><td>standard discount (% of list price) of competitor  $j$  in  $t$ </td></tr><tr><td> $Md_{jt}$ </td><td>margin discount (% of list price) of competitor  $j$  in  $t$ </td></tr><tr><td> $Mt_{jt}^s$ </td><td>market share (weighted by segment) trend of competitor  $j$  in period  $t$ </td></tr><tr><td> $LP_{jt}$ </td><td>competitor  $j$  list price in  $t$ </td></tr><tr><td> $Lpi_{jt}$ </td><td>competitor  $j$  list price increase in period  $t$ </td></tr><tr><td> $LPd_{jt}$ </td><td>competitor  $j$  list price decrease in period  $t$ </td></tr><tr><td colspan="2">Calculations: solution revenue</td></tr><tr><td> $R_t^j$ </td><td>revenue of competitor  $j$  in period  $t$ </td></tr><tr><td colspan="2">Input: cost ratios</td></tr><tr><td> $SGA_t^j$ </td><td>selling, general and administrative expenses of competitor  $j$  in period  $t$ </td></tr><tr><td> $C_t^j$ </td><td>cost of sales of competitor  $j$  in period  $t$ </td></tr><tr><td> $T_t^j$ </td><td>taxes of competitor  $j$  in period  $t$ </td></tr><tr><td colspan="2">Output: bottom-line for operations and product planners</td></tr><tr><td> $GP_t^j$ </td><td>gross profit of competitor  $j$  in period  $t$ </td></tr><tr><td colspan="2">Calculation and output: bottom line for financial planners</td></tr><tr><td> $NOP_t^j$ </td><td>net operating profit of competitor  $j$  in period  $t$ </td></tr><tr><td> $COS^j$ </td><td>cost of sales factor for competitor  $j$  as a percent of revenue</td></tr><tr><td>TAX</td><td>tax factor as a percent of net operating profit</td></tr></table>

We will now use nonfinancial measures as drivers of financial performance indicators, which is an assumption considered in many examples of current research in this area (for instance, Ittner and Larcker [8] have shown how for 2.491 customers of telecommunications firms, customer satisfaction indexes could be correlated to revenue levels, retention and revenue changes of the firms over time. They conclude that their results offer qualified support for recent moves to include customer satisfaction indicators in internal performance measurement systems and compensation plans).

The main equation links market share to revenue and profit by reproducing a pro-forma income statement of the business. (In the equations, we include the competitor and index ( j) to maintain the ability to track more than one competitor financials according to the model possibilities). All of the businesses we worked with require pro forma statements to also show associated market share, with as much back up information about target segments as possible—either as a %goal to be achieved over time that has been set by corporate, or as the assumed result of the planned operational targets tied to business projections.

In addition, working with business controllers led us to incorporate sales discounts for channel incentives $( \mathrm { S d } _ { j t }$ and $\mathrm { M d } _ { j t } )$ , cost of sales (COS<sup>j</sup>) and tax (TAX) factors, extending operations targets for individual programs to show front-end investments and contribution to shareholder metrics. To meet corporate planning guidelines, the business case usually has to project market share, revenue, and profit metrics, with details for the next 4 quarters and summary data over 3 years, Once the unit sales per segment is calculated in Eqs. (8) and (9), Eqs. (10–14) formalize the income statement.

$$
\mathrm{Tcs} _ {t} ^ {s} = \mathrm{Tc} _ {t} \times \mathrm{Ss} _ {t} ^ {s}\tag{8}
$$

$$
S _ {j} ^ {s} t = \operatorname{Tcs} _ {t} \times M S H _ {j} ^ {s} t\tag{9}
$$

$$
R _ {t} ^ {j} = \sum_ {s = 1} ^ {S} S _ {j} ^ {s} t \times \mathrm{LP} _ {j t} \times \left(1 - \left(\mathrm{Sd} _ {j t} + \mathrm{Md} _ {j t}\right)\right)\tag{10}
$$

$$
C _ {t} ^ {j} = R _ {t} ^ {j} \times \cos^ {j}\tag{11}
$$

$$
\mathrm{GP} _ {t} ^ {j} = R _ {t} ^ {j} - \left(C _ {t} ^ {j} + \mathrm{SGA} _ {t} ^ {j}\right)\tag{12}
$$

$$
T _ {t} ^ {j} = \mathrm{GP} _ {t} ^ {j} \times \mathrm{TAX}\tag{13}
$$

$$
\mathrm{NOP} _ {t} ^ {j} = \mathrm{GP} _ {t} ^ {j} - T _ {t} ^ {j}\tag{14}
$$

Share, Price, Revenue & Profit  
![](/api/attachments/3HGVK8HR/fulltext/images/91320524aa95f21ba15de3703ce941eb01ba39cf488e5b76fab8b17bf70bace6.jpg)  
Fig. 4. Original team design of the financial model.

In our experience, the financial model is conceived by business planners as shown in Fig. 4. The list price strategy is influenced by the market share trend of the business. For example, as a matter of pricing policy, a constraint was inserted in one scenario that raised or lowered the list price if market share projections fit defined gain or loss criteria.

## 6. Modeling allowable investments

Planning and tracking targets throughout the fiscal year means calculating the rate of investment that the business should direct toward a given market opportunity in order to reach its profit goals.

How do we set up a policy to determine the rate of spending we can accomplish? What variables should drive decisions about continuing or changing program investments? Again, in order to answer these questions, we first describe the notations and definition of the main financial model variables:

<table><tr><td colspan="2">Subscripts:</td></tr><tr><td> $j=1,\dots,N$ </td><td>competitors</td></tr><tr><td>Calculations: changes in financial variable values</td><td></td></tr><tr><td> $Rg^{j}$ </td><td>revenue growth of competitor  $j$  in period  $t$ </td></tr><tr><td> $SGAg^{j}$ </td><td>growth of selling and general administrative expenses of competitor  $j$  in period  $t$ </td></tr><tr><td> $Cg^{j}$ </td><td>cost of good sold growth of competitor  $j$  in period  $t$ </td></tr><tr><td> $Tg^{j}$ </td><td>taxes growth of competitor  $j$  in period  $t$ </td></tr><tr><td> $PC^{j}$ </td><td>profit contribution of competitor  $j$  in period  $t$ </td></tr><tr><td> $ICF^{j}$ </td><td>investments constraint factor in competitor  $j$ </td></tr></table>

Where channel strategy requires incentives in the form of discounts and payments, those costs are added to the computation of net sales as a deduction to compute revenue.

In the example scenario that follows, we represent an existing product, and therefore, we assume that conditions to increase investment map closely to changes in the financial variable values. We first define those value changes in Eqs. (15–18), where the growth in revenue, cost of sales, SGA expenses, and taxes are calculated.

$$
\mathrm{Rg} _ {t} ^ {j} = R _ {t} ^ {j} - R _ {t - 1} ^ {1}\tag{15}
$$

$$
\mathrm{Cg} _ {t} ^ {j} = C _ {t} ^ {j} - C _ {t - 1} ^ {1}\tag{16}
$$

$$
\mathrm{SGAg} _ {t} ^ {j} = \mathrm{SGA} _ {t} ^ {j} - \mathrm{SGA} _ {t - 1} ^ {j}\tag{17}
$$

$$
\mathrm{Tg} _ {t} = T _ {t} ^ {j} - T _ {t - 1} ^ {j}\tag{18}
$$

Profit contribution growth is defined as the difference between projected revenue growth, and the sum of the accumulated growth in the other three variables (see Eq. (19)).

$$
\mathrm{PCg} _ {t} ^ {j} = \mathrm{Rg} _ {t} ^ {j} - \left(\mathrm{Cg} _ {t} ^ {j} + \mathrm{SGAg} _ {t} ^ {j} + \mathrm{Tg} _ {t}\right)\tag{19}
$$

Finally, SGA expenses for the next year are calculated by considering the profit contribution, revenue growth and other factors. To illustrate how this is done, let us see the example, base in a real case, presented in Table 1.

Here we show how the model can be used to set target spending levels by mapping the pro-forma statement ratios, the proposed spending to increase specific attributes, and the expected returns from a strategy specifically engineered to influence a target segment. In the example in Table 1, profit contribution of Company X, in year 2, could be calculated as follows:

$$
\mathrm{PCg} _ {\mathrm{YR2}} = \mathrm{Rg} _ {\mathrm{YR2}} - \left(\mathrm{Cg} _ {\mathrm{YR2}} + \mathrm{SGAg} _ {\mathrm{YR2}} + \mathrm{Tg} _ {\mathrm{YR2}}\right) = 5 5 0 - (4 9 5 + 6 + 1 5) = 3 5 K 3 > 0
$$

In Company X, growth in profit contribution is therefore positive, and revenue growth (in %) is more than three times SGA growth (in %) during the last year (50%<sup>N</sup>14%). This seems to be an optimal proportion for Company X to increase its spending. Suppose, for instance, that when the above conditions are fulfilled, the company grows SGA expenses by half (ICF=1/2) of the revenue growth (in %), then $\operatorname { S G A } _ { \operatorname { Y R } 3 }$ would be calculated as follows:

Table 1  
Numerical example for the determination of investments in the model

<table><tr><td rowspan="3"></td><td colspan="6">Company X, profit and loss statement</td></tr><tr><td colspan="2">YR1</td><td colspan="4">YR2</td></tr><tr><td>K$</td><td>%Rev</td><td>K$</td><td>%Rev</td><td>Growth, $</td><td>Growth, %</td></tr><tr><td>Sales</td><td>2000.00</td><td></td><td>3000.00</td><td></td><td>1000.00</td><td></td></tr><tr><td>Standard Discount</td><td>840.00</td><td>42</td><td>1.260.00</td><td>42</td><td>420.00</td><td></td></tr><tr><td>Margin Discount</td><td>60.00</td><td>3</td><td>90.00</td><td>3</td><td>30.00</td><td></td></tr><tr><td>Revenue</td><td>1100.00</td><td>100</td><td>1650.00</td><td>100</td><td>550.00</td><td>50</td></tr><tr><td>Cost of Sales</td><td>825.00</td><td>75</td><td>1.320.00</td><td>80</td><td>495.00</td><td>60</td></tr><tr><td>Gross Profit</td><td>275.00</td><td>25</td><td>330.00</td><td>20</td><td>50.00</td><td>18</td></tr><tr><td>SGA</td><td>44.00</td><td>4</td><td>50.00</td><td>3</td><td>6.00</td><td>14</td></tr><tr><td>Net Operating Profit Before Taxes</td><td>231.00</td><td>21</td><td>280.00</td><td>17</td><td>50.00</td><td>22</td></tr><tr><td>Tax Factor</td><td>69.00</td><td>6</td><td>84.00</td><td>5</td><td>15.00</td><td>22</td></tr><tr><td>Net Operating Profit After Taxes</td><td>162.00</td><td>15</td><td>196.00</td><td>12</td><td>35.00</td><td>22</td></tr></table>

![](/api/attachments/3HGVK8HR/fulltext/images/6c5bda22047f6e520496c8ca0ed71baff60f76c171b493bdf0380c1eed84b5f6.jpg)  
Fig. 5. Original team design of the investments model.

$$
S G A _ {\mathrm{YR3}} = S G A _ {\mathrm{YR2}} ((1 + I C F (R g _ {\mathrm{YR2}} ^ {j} / R _ {\mathrm{YR1}} ^ {j})) = 5 0 (1 + 0. 5 (5 5 0 / 1 1 0 0)) = 5 0 (1. 2 5) = 7 5 K
$$

Then, this example would be formalized as a policy constraint in our model as shown in Eq. (20):

$$
S G A _ {t + 1} ^ {j} = \left\{ \begin{array}{l l} S G A _ {t} ^ {j} \big (1 + I C F ^ {j} \big (R g _ {t} ^ {j} / R _ {t - 1} ^ {j} \big) \big) & , \text {   if   } P C g _ {t} ^ {j} > 0 \text {   and   } \big (R g _ {t} ^ {j} / R _ {t - 1} ^ {j} \big) > 3 \times \big (S G A g _ {t} ^ {j} / S G A _ {t - 1} ^ {j} \big) \\ S G A _ {t} ^ {j} & , \text {   Otherwise   } \end{array} \right.\tag{20}
$$

Again, the investments model in our example, drawn from actual planning scenarios, was represented with the planning teams as shown in Fig. 5, where we find a balance loop that shows how the rate of growth in profit contribution conditions the growth of the SGA expenses, while ICF, $\mathrm { R g }$ and SGAg, limit that growth (again, policy could depend on other variables according to specific business and market conditions. See, for instance, comments about share in Section 2).

## 7. From an operational investment model to a decision support system

Sections 4–6 of this paper showed details within the three sub-models included in Fig. 2, containing our general model overview. With respect to system dynamics modeling, we note the importance of causal diagrams. They helped identify feedback mechanisms in the sub-models, to visualize how these could impact the way business grows. The possibility to shift from solely numerical data to a graphical representation provided the opportunity for dialog and eased mutual understanding, especially for people playing different roles within the business planning process.

The model as shown allows us to study many product and go-to-market scenarios, with enough rigor to quickly focus on key assumptions and to build confidence and consensus when changing business plans.

## 7.1. A sample of the decision support system applied to a business

We now present an example of the model’s use, based on a real instance where planners considered a possible strategy to improve three product attributes (see Fig. 6).

Given a stable organization and product architecture (rare in high-tech business), we first validated the model with history across 3 years, 1995–1998, for consumer products sold through resellers in a mature market in which the firm was dominant. In that ideal but unusually stable case, with the product attributes that customers hold most important, and the attribute elasticity in each segment, we were able to replicate the market response to attribute investments during those years with reasonable accuracy. Using the model for this scenario, planners wanted to know whether or not to continue the same rates of spending increase for the same three attributes over the next 3 years, as shown in Fig. 3, assuming that these would result in the same kind of increase in value perceptions for those three attributes. They wanted to know what kind of business results they could expect and why, in order to justify the rate of spending, they would fund to meet their growth objectives.

![](/api/attachments/3HGVK8HR/fulltext/images/c5267cb94babf3672c1d83aeaf9dcac13e2664fc2c5abf0c26769b5867c8fd90.jpg)

![](/api/attachments/3HGVK8HR/fulltext/images/64e66fb3c41347e1291d6beda3c05f1611452f0837f3585702038900d8ef76f7.jpg)  
Fig. 6. Base and best case of attribute improvement.

The scenario results shown below in Fig. 7 tell us that there is an incremental gain in market share in all three market segments we are considering, but that the gain is greatest in the segment called <sup>b</sup>small<sup>Q</sup>, where we may reach close to a 5% gain in market share. Segment <sup>b</sup>Soho<sup>Q</sup> responds very little, and there is only a small gain in segment <sup>b</sup>Medium<sup>Q</sup>. In calculating the profit impact, the model uses input from planners about segment growth, share size, competitor strategy, segment elasticity, and expected price or cost changes, all happening at the same time. The planning team, which includes marketing, engineering, finance, supply chain management, and division executives, reviews the scenario output to understand the results, confirm underlying assumptions, and agree where they would redirect spending.

In addition to being able to <sup>b</sup>drill down<sup>Q</sup> to underlying causes, the scenario shows the net operating profit the business could expect, if those investments are accomplished, given the corresponding yearly increase in SGA (see Fig. 8). The business planners used this outcome analysis to adjust their planned investment program.

## 7.2. From a simulation model to a decision support system

Now we give an example of how this model can take advantage of optimization techniques to compare alternative attributes investments, converting the model into a fast Decision Support System. A

Fig. 7. Base and best simulations for market share improvement (notice that last two graphs are in different scale than the first one).

![](/api/attachments/3HGVK8HR/fulltext/images/ba56345ebbefd7c25e09b2ecfb8d0b149e2b20cf3f24057d98c9caf3539ae4a7.jpg)

![](/api/attachments/3HGVK8HR/fulltext/images/3f1021fd3db43d185599eb3bc2441df8367e990f1f1e62c71e4a201c4eede323.jpg)  
Fig. 8. Base and best simulations, expected NOP (after taxes) and increase in SGA per year.

modified Powell method is used to carry out these optimizations properly. This is a direct-search numerical optimization technique which does need not to evaluate the gradient, and which is very suitable for the analysis of dynamics of complex nonlinear control systems. This technique is well known among direct-search methods, to derive a very fast convergence (the basic idea behind Powell’s method [15] is to break the N-dimensional minimization down into N separate 1D minimization problems. Then, for each 1D problem, a binary search is implemented to find the local minimum within a given range. Furthermore, on subsequent iterations an estimate is made of the best directions to use for the 1D searches. Some problems, however, are not always assured of optimal solutions because the direction vectors are not always linearly independent. To overcome this, the method was revised [16] by introducing new criteria for formation of linearly independent direction vectors; this revised method is called <sup>b</sup>The Modified Powell Method<sup>Q</sup>).

In this example, we use the model to select an investment focus for the next 3 years. From the list of attributes that represent the decision factors for solution customers, we compare the impact of improving each attribute by a planned percentage. Each column in Table 2 evaluates the choices according to a specific criteria. The table is used one column at a time, with each one representing a different planning scenario.

The table ranks the attributes according to each criteria, while in the last rows, the associated percentages tell us how much better the highest level of ranking is than each of the lower level ranks.

In order to optimize their investments, the planners first define the criteria for optimization to be used in each scenario, the calculation represented here by the column headings. Planners normally consider more than one criteria, and usually include both financial and market-based metrics, representing various business objectives for the planning period. They then define optimization variables for the ranking calculations (first column). Later, we can ask the model, by using multi-parametric optimization (considering cumulative evaluation of the payoff), which attributes should be the spending priority to best meet the business criteria shown in the column heading.

Table 2  
Example of output from the decision support system (not case described above)

<table><tr><td rowspan="2"></td><td colspan="6">Optimizing criteria (equivalent to a different planning scenario)</td></tr><tr><td>Revenue</td><td>Share</td><td>Net profit</td><td>Share in segment X</td><td>Share in product Y</td><td>Revenue and share</td></tr><tr><td colspan="7">Attributes</td></tr><tr><td>Reliability</td><td>1</td><td>2</td><td>6</td><td>4</td><td>2</td><td>1</td></tr><tr><td>Easy to purchase</td><td>1</td><td>2</td><td>6</td><td>3</td><td>2</td><td>2</td></tr><tr><td>Scalability</td><td>2</td><td>2</td><td>6</td><td>3</td><td>2</td><td>3</td></tr><tr><td>Network friendly</td><td>2</td><td>2</td><td>6</td><td>3</td><td>2</td><td>3</td></tr><tr><td>Service availability</td><td>2</td><td>2</td><td>5</td><td>3</td><td>1</td><td>3</td></tr><tr><td>Connectivity</td><td>3</td><td>2</td><td>1</td><td>2</td><td>3</td><td>3</td></tr><tr><td>Plug and play</td><td>4</td><td>3</td><td>2</td><td>4</td><td>4</td><td>4</td></tr><tr><td>...etc.</td><td>5</td><td>4</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td colspan="7">Relative level of importance</td></tr><tr><td>(1) more than (2)</td><td>7%</td><td>14%</td><td>20%</td><td>13%</td><td>12%</td><td>5%</td></tr><tr><td>(1) more than (3)</td><td>14%</td><td>20%</td><td>60%</td><td>15%</td><td>20%</td><td>16%</td></tr><tr><td>(1) more than (4)</td><td>78%</td><td>+%</td><td>260%</td><td>+%</td><td>+%</td><td>+%</td></tr><tr><td>(1) more than (5)</td><td>545%</td><td></td><td>340%</td><td></td><td></td><td></td></tr><tr><td>(1) more than (6)</td><td></td><td></td><td>400%</td><td></td><td></td><td></td></tr></table>

The way to read the table is as follows: if we pursue maximizing Revenue, first choice for attribute investment should be Reliability and Easy to Purchase, if you increase perception of either of those attributes by a targeted percent (which you assume you will do if you spend according to your plan), your results in terms of revenue will be 7% higher than in Scalability, Network Friendly, or Service Availability, and 14% higher than in any attribute with a 3, and so on.

The model here becomes a powerful and flexible planning tool. You may even explore multiple objectives (see last column that includes both Revenue and Share). The same planning team might go on to explore other investments goals, like increasing the presence in various segments. This constitutes a Decision Support System that adds clarity and rigor to targets and product/program strategy.

## 8. Managerial implications

As we mentioned and characterized in Section 2, managers in high-tech markets face unique challenges.

## 8.1. Respond to market-driven demand

Business planners represent the needs of engineering, marketing, sales, order, delivery, support, and service teams. They face changes driven by technological advances, volatile demand, global competition, emerging standards, and significant uncertainty about what drives their customer’s decisions to buy.

This decision support system views the business as a dynamic feedback system to:

1. sense an opportunity matched with an ability to respond with value;

2. create value—balancing features and price—and communicate that value to customers in a target segment;

3. grow with the market, faster than the competition;

4. create early barriers to entry for emerging markets;

5. confidently redirect resources based on changes in customer purchasing behavior, competitor investment, and the payback that can be expected from the required additional investment.

## 8.2. Segment according to customer purchase priorities

Wherever markets are segmented by customer value and buying behavior, decision makers may use this model to compare expected financial returns on alternative investments that appeal to some segments more than others. Investments that affect a specific attribute have different implications for each segment, with results for share, revenue, and profit that also reflect external changes in size of that targeted segment and of the market demand overall.

Specific investments considered by teams with whom we have done these analyses in the past include: reseller discounts, pricing strategy, one-toone relationship marketing programs, advertising to raise target customer awareness, new channel development, new product and technology introductions, introduction of non-branded offerings, forward contracts to secure critical part supply, and collaborative communication backbones for demand and fulfillment chains.

## 8.3. Focus on the vertical dimension of business planning

There is only one <sup>b</sup>product<sup>Q</sup> in our model, but in high-tech sectors like telecom infrastructure or medium business manufacturing, the end <sup>b</sup>product<sup>Q</sup> is a solution, i.e. multiple component products with different cost structures bundled for this market to meet this set of attributes.

Financial targets usually represent product businesses selling into numerous markets, where go-tomarket, sales, service, and channel investments are treated as programs, charged with achieving specific market objectives. Although current financial data usually comes to us as product business targets, most critical investment decisions must also consider the impact of changes in attributes and customer perception of value for a solution which will determine its success or failure.

## 8.4. Traction from precise go-to-market strategy

Initiatives to improve business performance are directed toward specific solution attributes:

Quality attributes are improved by investments to improve features, performance, power requirements, footprint size, integration, customization, delivery, localization, scalability, interoperability, quality, channels, and alliances.

Price attributes are improved by investments in aggressive sourcing, parts availability, risk management, order and forecast management, channel incentives, discounts, rebates, advertising, webbased collaborative infrastructure, and synchronized product upgrades.

The critical assumption, that your planned spending will indeed increase customer perception and impact sales as you expect, needs to be confirmed as quickly as possible. In addition to mining existing market research, our planners tended to gain confidence through immediate action guided by the decision support system, with a rapid <sup>b</sup>pilot<sup>Q</sup>, limited in scope and carefully observed to measure and confirm perception and response. Thus, for today’s high-tech businesses, strategy and tactics tend to merge, each informing the other in a rapid exchange between precise action and useful learning.

## 9. Conclusions and further research

In this paper, we have described how we have used simulation models to support product and marketing investment decisions. We have presented a high level model structure, and described formalization of three sub-models for purchasing behavior, financial results, and investments for growth. We have shown how the model is used in business planning to explore a specific problem, and given one example of the model’s value as an <sup>b</sup>engine<sup>Q</sup> of a Decision Support System.

The Decision Support System that we have defined takes into account the horizontal and vertical metrics that together define success for current high-tech businesses, matching each investment strategy to specific attributes of customer value and business results. At the same time, we incorporate within the model structure other important characteristics of high-tech markets that are just emerging but will soon be factors in business investments decisions.

System dynamics simulations greatly improve analysis of go-to-market strategies, integrating customer knowledge with simulations to analyze spending trade-offs in features, services, support, integration, channel incentives, pricing, and advertising. The payback over time is the shown in the output from this formal system dynamics model, a powerful DSS tool offering the opportunity to compare strategies for a segmented market, under different scenarios, with customized metrics.

## References

[1] G.D. Bhatt, J. Zaveri, The enabling role of Decision Support Systems in organizational learning, Decision Support Systems 32 (3) (2002) 297–309.

[2] E. Bridges, K.B. Ensor, J.R. Thomson, Marketplace competition in the personal computer industry, Decision Science 23 (2) (1992) 467– 477.

[3] G.S. Carpenter, L.G. Cooper, D.M. Hanssens, D.F. Midgley, Modeling asymmetric competition, Marketing Science 7 (4) (1998) 393– 412.

[4] G.S. Day, Market Driven Strategy: Processes for Creating Value, The Free Press, New York, 1990.

[5] J.W. Forrester, Collected Papers of Jay W. Forrester, Wright-Allen Press, Cambridge, Massachusetts, 1975.

[6] M.A. Higby, B.N. Farah, The status of marketing information systems, Decision Support Systems and expert systems in the marketing function of U.S. firms, Information and Management 20 (1991) 29– 35.

[7] R.M. Hogarth, S. Makridakis, Forecasting and planning: an evaluation, Management Science 27 (2) (1981) 115 – 138.

[8] C.D. Ittner, D.F. Larcker, Are nonfinancial measures leading indicators of financial performance? An analysis of customer satisfaction, Journal of Accounting Research 36 (1998) 1 – 31 (suppplement).

[9] N. Kim, E. Bridge, R.K. Srivastava, A simultaneous model for innovative product category sales diffusion and competitive

dynamics, International Journal of Research in Marketing 16 (1999) 95 – 112.

[10] E. Li, J.R. McLeod, J.C. Rogers, Marketing information systems in fortune 500 companies: a longitudinal analysis of 1980, 1990, and 2000, Information and Management 38 (2001) 307 – 322.

[11] J.D.C. Little, Decision Support Systems for marketing managers, Journal of Marketing 43 (1979) 9 – 26.

[12] J.D.C. Little, L.M. Lodish, J.R. Hauser, G.L. Urban, Commentary, in: G. Laurent, G.L. Lilien, B. Pras (Eds.), Research Traditions in Marketing, Kluwer Academic Publishing, Boston, 1994, pp. 44 – 51.

[13] J.D. Morecroft, P. Senge, J.W. Forrester, Modeling for Learning Organizations, Productivity Press, Portland, Oregon, 2000.

[14] L.J. Parsons, E. Gijsbrechts, P.S.H. Leeflang, D.R. Wittink, Commentary, in: G. Laurent, G.L. Lilien, B. Pras (Eds.), Research Traditions in Marketing, Kluwer Academic Publishing, Boston, MA, 1994, pp. 52–78.

[15] M.J.D. Powell, An efficient method for finding the minimum of a function of several variables without calculating derivatives, Computer Journal 7 (2) (1964) 155 – 162.

[16] M.J.D. Powell, On the calculation of orthogonal vectors, Computer Journal 11 (2) (1968) 302 – 304.

[17] E. Roberts (Ed.), Managerial Applications of System Dynamics, MIT Press, Cambridge, 1984.

[18] J. Ross, D. Georgoff, A survey of productive and quality issues in manufacturing. The state of the industry, Industrial Management 3 (5) (1991 (Jan–Feb.)) 22– 25.

[19] S.P. Schnaars, Marketing Strategy: a Customer-driven Approach, The Free Press, New York, 1991.

[20] P. Senge, The Fifth Discipline: the Art and Practice of the Learning Organization, Double Day, New York, 1991.

[21] J. Shaw, C. Subramaniam, G.W. Tan, M.E. Welge, Knowledge management and data mining for marketing, Decision Support Systems 31 (2001) 127– 137.

[22] H. Simon, Marketing science’s pilgrimage to the ivory tower, in: G. Laurent, G.L. Lilien, B.D. Pras (Eds.), Research Traditions in Marketing, Kluwer Academic Publishing, Boston, 1994.

[23] J. Sterman, Business Dynamics: Systems Thinking for a Complex World, McGraw-Hill, Irwin, 2000.

[24] G.H. Van Bruggen, A. Smidts, B. Wierenga, Improving decision making by means of marketing decision support system, Management Science 44 (1998) 645 – 658.

[25] P.A.F.M. Van Campen, K.R.E. Huizingh, P.A.M. Oude Ophuis, B. Wierenga, Marketing decision support systemen bij nedelandse bedrijven, Eburon, Delft, 1991.

[26] A. Vollerthun, Design-to-market: integrating conceptual design and marketing, Systems Engineering 5 (4) (2002) 315 – 326.

[27] B. Wierenga, P.A.M. Oude Ophuis, Marketing Decision Support Systems: adoption, use and satisfaction, International Journal of Research in Marketing 14 (1997) 275 – 290.

Adolfo Crespo Marquez is currently Associate Professor at the School of Engineering of the University of Seville, in the Department of Industrial Management. He holds a PhD in Industrial Engineering from that same University. He has been intensively involved in multinational projects related to supply chains, concerning front-end, back-end and integration issues. He has published or is about to publish his works in the International Journal of Production Research, International Journal of Production Economics, European Journal of Operational Research, Reliability Engineering and System Safety, Omega, Journal of Purchasing and Supply Management, International Journal of Agile Manufacturing, International Journal of Logistics Systems and Management, Journal of Quality and Maintenance Engineering, etc.

Carol Blanchar has decades of experience in delivering complex solutions for both IT and telephone needs. As independent consultant, she developed and executed investment and solution strategies to meet time-to-market, time-to-revenue, and profit objectives. She has proven effectiveness in translating the technology of complex telecom solutions and services into business value for vendors, delivery partners and customers alike. Today, she is managing partner of Conexo, a privately held California corporation offering deployment consulting to help clients better integrate IP Communication services and products, connect IP Communications solutions to results for the whole business, and manage operational risk during migration to the new products and technology.
