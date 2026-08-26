---
otero_id: 22072
otero_key: "7JE8AYNZ"
title: "Modelling policies and decisions"
authors: "Bernadette O’Regan; Richard Moles"
year: "2003"
journal: "Information & Management"
doi: "10.1016/s0378-7206(01)00139-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Modelling policies and decisions A case study in mineral extraction

Bernadette O’Regan<sup>\*</sup>, Richard Moles

Department of Chemical and Environmental Sciences, Lonsdale Building, University of Limerick, Limerick, Ireland

Received 9 July 2000; received in revised form 8 August 2001; accepted 21 November 2001

## Abstract

This paper describes the application of the tools and techniques of the system dynamics method within the context of factors which impact the flow of international mineral investment funds.<sup>1</sup> Emphasis is placed on methodology rather than context. The simulation model, which provides the theoretical underpinning for the paper, is developed in the system dynamics tradition and provides a means of examining the effectiveness of varied environmental, fiscal, and corporate policies on the operating decisions of international mining firms and the flow of investment funds. The model acts as an integrated decision support tool through the projection of future changes in a mining firms key performance indicators. <sup>#</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Modelling; Simulation; Decision support; Complexity; Feedback

## 1. Introduction

The aim of this paper is to describe the system dynamics simulation methodology within the context of the complexity and interdependence of the factors impacting the relative attractiveness of a country as a location for minerals exploration and development. The model comprises a number of tightly coupled system dynamics sub-models.

The mining firm is viewed as a particular case of a typical business entity, which is assumed to have a major objective of maximising profits. The mining firm sub-model attempts to capture the essential decision making structures that determine how (and where) profits are re-invested through further exploration and development activity.

Individual countries compete for mineral investment funds, either directly through specific minerals policies, or indirectly through prevailing government and economic conditions. Domestic environmental policies may have a large impact on the relative attractiveness of a country to the mining industry. The objective of this sub-model is to expose those factors that directly impact the investment decisions of mining firms.

Base metals are traded on the international commodity markets. These can be considered exogenous to both individual firm behaviour and government policy and are subject to fluctuations that impact on the performance of mining firms and the relative attractiveness of mineral producing countries.

A hypothetical mining firm might decide to invest a proportion of its exploration budget in a particular country on the basis of the prevailing investment climate there. It is likely that the firm will spread its investment among a number of countries as a function of their relative attractiveness; thus, the decision making process considers environmental regulation as an important factor. Furthermore, the firm’s decision mechanisms do not exist in isolation but are dependent on the activities of its competitors, as reflected in the behaviour of the international minerals market.

## 2. Modelling complexity

A computer simulation model provides a powerful means of exposing system complexity and, thus, increasing understanding. The model described here shows how exploration spending is a function of the relative attractiveness of individual deposits in competing countries. This, defined by the expected net value of exploration, changes over time, as deter mined by the interrelationships between many factors, such as the host government’s environmental regulatory and planning requirements, the level of taxation, and the availability of accurate geological information. The exact nature of these complex interrelationships is made explicit through the variable definitions. These assumptions (definitions) can be modified and the resulting changes in behaviour patterns examined.

The greatest advantage in adopting system dynamics as an analytical tool is that it exposes the many interrelationships (structure) that influence the behaviour of a complex system, e.g. for the flow of mineral investment funds, the same change to environmental or fiscal policy does not always have the same effect because the effect is dependent on the ‘state’ of the system at a particular point in time. Through its effectiveness at capturing and exposing the state of the system, this model improves on more conventional methods for evaluating policy effectiveness.

## 3. Modelling policies and decisions

System dynamics fosters a feedback view of management as a process that converts information into action. This process is a decision process and success depends on selecting the right information and using it effectively. From this perspective, a policy is a guiding rule: an aid to decision making. This process is complicated by the fact that information about the outcome of actions taken is never immediately available.

Through a quantitative analysis of existing data, the model exposes, within the context of the problem area, the underlying assumptions used as a basis for policy formulation and corporate decisions. Furthermore, through compression of time, the model provides a means of taking these assumptions to their logical conclusion. Exposing assumptions in this way leaves less room for misinterpretation and provides a solid basis for enhancing the understanding of system structure.

## 4. Model variables and relationships

Our model contains over 8000 individual model objects (array elements and scalars). Almost all of them are dependent variables: their value at any particular time is determined by the current ‘state’ of the system. System state is defined by the collective values of the level variables in the system, of which there are 31. These, together with the 24 model constants, act as initial conditions for the model and can be changed at the start or during the run to reflect particular circumstances, such as changes in corporate or government policy. Many of the levels are derived variables, in that their values are directly dependent on the values of other levels. Some of the most significant level variables and constants are Table 1.

As zinc is the most commonly mined mineral in Ireland, it was chosen as a basis for parameter values in the construction of the model. The structure is captured through the relationships between the variables. Many of them are simple (linear) in nature and, therefore, easy to define. Non-proportional relationships are modelled through the use of multipliers or graph functions. The main use of a multiplier in a system dynamics model is to act as a changing (dynamic) pressure on decision making. This is in contrast to the static, normal, value, which takes effect when the system is in equilibrium. For example, the decision of how much to invest in exploration, the

Table 1 Selection of key model parameters

<table><tr><td>Actual_Geology</td><td>Available_Resources</td></tr><tr><td>Average_Ore_Grade</td><td>Book_Value_of_Mine</td></tr><tr><td>Cash</td><td>Cumulative_Income_Reserves</td></tr><tr><td>Debt</td><td>Discovery_Delay</td></tr><tr><td>E_Cost_of_Exploration_Effort</td><td>Equity</td></tr><tr><td>Expected_Demand</td><td>Expected_Price</td></tr><tr><td>Exploration_Spending_by_Country</td><td>Explored_Resources</td></tr><tr><td>Extracted_Ore</td><td>LME_Inventory</td></tr><tr><td>Metal_Recovery</td><td>Mineable_Reserves</td></tr><tr><td>Paid_in_Capital</td><td>Perceived_Geological_Potential</td></tr><tr><td>Perceived_Ore_Grade</td><td>Proven_Reserves</td></tr><tr><td>Refined_Mineral</td><td>Regulatory_and_Planning_Requirements</td></tr><tr><td>Retained_Earnings</td><td>Waste</td></tr><tr><td>Exploration_Budget_Allocation</td><td>Construction_Delay_Normal</td></tr><tr><td>Costs_of_Local_Inputs</td><td>Interest_Rate</td></tr><tr><td>Perceived_Political_Stability</td><td>Perceived_Security_of_Tenure</td></tr><tr><td>Percentage_of_Profits_Reinvested_in_New_Mines</td><td>Planning_Delay_Normal</td></tr><tr><td>Pollution_Tax_Rate</td><td>Price_Normal</td></tr><tr><td>Profits_Reinvisted_in_Exploration</td><td>Taxation_Percentage</td></tr></table>

Exploration\_Budget, is defined as the product of static and dynamic pressures as follows:

Exploration Budget

¼ Exploration Budget Normal

 Expected Price to Exploration Budget Multiplier

 Market Share to Exploration Budget Multiplier

ð1Þ

Exploration\_Budget\_Normal is the typical exploration budget. The size of this is affected by changes in expected price. This pressure, which cannot be ignored, is modelled through the use of an Expected\_- Price\_ to\_Exploration\_Budget\_Multiplier. When the presumed future price equates to the long-term median price (US\$ 1235/tonne), then expected price neither has a positive or negative pressure on the size of the exploration budget; this provides point 1 on the y-axis. However, when the expected price of a tonne of the mineral exceeds US\$ 1235/tonne, then there is an incentive (pressure) to increase the size of the exploration budget to maximise gains from expected improvements in market conditions. Similarly, when price is expected to fall, there is an incentive to reduce the exploration budget. The graph function for the Expected\_Price\_to\_Exploration\_Budget\_Multiplier is shown in Fig. 1.

![](/api/attachments/7JE8AYNZ/fulltext/images/ecfeac097d9e2846c7fcbad51c00ada7609a6af0657f25cca242f36a9fd8c6f0.jpg)  
Fig. 1. Modelling the effect of expected price on a firms exploration budget.

## 5. Modelling methodology

It is beyond the scope of this paper to present a detailed context for the model. Instead, emphasis is placed on modelling methodology and the reader is referred to a paper by O’Regan and Moles [3] for a detailed discussion of the dynamics of the minerals industry.

![](/api/attachments/7JE8AYNZ/fulltext/images/e6e1da4e9f9c576bbe95a8a3bf860f0354642fe2c422d0be0190595a0ac01544.jpg)  
Fig. 2. Decisions are based on perceived (not actual) information.

The system dynamics development process is iterative in nature. There is no initial template upon which to base the model structure. Instead it evolves over time, as more accurate information becomes available about the relative importance of the various information flows that feed the critical decision points in the system. In a system dynamics model, the state of the system (as defined by the collective values of all level variables) is changed over time as a result of actions carried out to implement management decisions. These management decisions are in turn driven by the current system state, as well as any guiding polices.

Developing a system dynamics model to expose the dynamics of management behaviour involves identifying the key decision points. These form the basis of system sub-models, in that they may be developed and tested in relative isolation. However, once each of the decision sub-models is sufficiently complex to capture the real-world decision processes, and at a level of abstraction deemed suitable to meet the objectives of the model, then the next main task is to capture the feedback between the various decision points or subsystems. Much of the significant dynamics in a complex system arises from delayed feedback between decision points, particularly when the feedback crosses organisational boundaries, e.g. the decision on where to explore is significantly affected by the success or otherwise of previous explorations. This information is captured in our model through the difference between perceived and Actual\_Geology, which is a component of the main mining process model and specific to the individual country (and deposit). Perceived\_Geological\_Potential, on the other hand, is specific to the individual firm and the difference between the two values is determined by the particular firm’s prior exploration activity in the particular country, other firms’ exploration activity, and, most importantly, the delays involved in making the results of the exploration activity available (accuracy of the geological information). It is very important for the model to distinguish between perceived and actual information as actual information is almost never available immediately, and so decisions must be made on perceived values Fig. 2.

## 6. Overview of causal feedback structure

There are two critical reinforcing feedback loops that are primarily responsible for changes in this system. At the micro level, the price/unit operating cost ratio is a fundamental determinant of the extraction decision of the individual mine. At the macro level, cumulative retained earnings drive the flow of exploration funds in, and between, countries. These loops interact through the effect of unit operating costs on mine profitability. Fig. 3 shows a highly aggregated causal-loop diagram depicting this feedback structure. The main determinant of the nature of the feedback, be it positive or negative, is the demand for the mineral and, consequently, price. In times of favourable market conditions, there is an excess of investment funds, and these are allocated primarily according to the principle of relative attractiveness. However, when market conditions become unfavourable, economic viability is determined on a per mine basis and is significantly impacted by the individual policies, including environmental policies, of the host governments.

![](/api/attachments/7JE8AYNZ/fulltext/images/63143fc90710f48a24addf95039b5728d044094d525754890e467d70caa6ed2b.jpg)  
Fig. 3. Critical feedback loops in the system.

## 7. Sample model output

The model is the present state of an iterative evolutionary process. Initial plans were modified and the model’s scope redefined on a number of occasions as a result of an increased understanding of the systems methodology. This only comes with prolonged experience in the model development process and as a result of changing expectations in relation to the availability of critical data.

The model represents a microcosm of the international zinc industry, in which four multi-national mining firms have explored and developed up to 20, each in four different countries, over a 100 years period. Model behaviour is a complex function of initial conditions and changing policy over the simulation period. To increase variety and better simulate reality, countries are assigned different initial conditions of geology, environmental regulatory and planning requirements, exploration costs, and the cost of local inputs. Firms vary according to their growth goals, risk aversion, and the price sensitivity of their extraction policies.

As an example of model output, consider the generation of waste at an individual mine. As minerals are recovered, solid waste is generated. The quantity of this waste is directly dependent on the average ore grade of the deposit, as well as the metal recovered. On the assumption that higher grade ore is extracted first, the decreasing average ore grade over the life of the mine results in an increase in the quantity of waste generated per tonne of recovered mineral (Fig. 4). With a constant metal recovery rate, the waste generated increases over the short-term time horizon of an individual mine, as well as over the longer term on a global scale, due to decreasing ore grade. Fig. 5 shows the ratio of the total amount of waste generated to mineral recovered with a constant metal recovery of 80% (lines 1 and 3) and with a step-wise improvement in metal recovery (lines 2 and 4).

The improvements to metal recovery result in a downward shift of the waste generation to recovered mineral ratio over the period of the simulation. However, the trend continues to increase over time, because the improvement in metal recovery facilitates the development (or reopening) of lower grade deposits that were not previously economically viable.

![](/api/attachments/7JE8AYNZ/fulltext/images/4d359dd6acdc0366daeeee197df03a5420acc988d295537e1e31e9c8780be952.jpg)  
Fig. 4. Waste generation for simulated deposit.

The model can be used to examine the effects of command and control environmental policies. However, apart from direct environmental regulation, governments also have the option of imposing fiscal penalties or using market based instruments to protect the environment. These may take the form of pollution taxes on a per unit of waste produced basis Fig. 5.

If the host government imposes a pollution tax on an operating mine, this will increase its unit operating costs. As the tax is on a per unit of waste basis, the ore grade will affect the total amount of tax payable, as the waste generated per tonne of metal recovered is dependent on the ore grade.

Fig. 6 presents output from a simulation run where a pollution tax of US\$ 10/tonne of waste is imposed on mining operations in Country4. From this figure, it can be seen that while refining rate declines over time due to decreasing ore grade, the waste generation rate remains relatively constant over the life of the mine, because the same quantity of ore (and resultant waste) is required to recover an ever decreasing quantity of mineral. Similarly, unit pollution tax (pollution tax/ tonne of recovered mineral) increases as average ore grade declines. This results in an increase in both unit

![](/api/attachments/7JE8AYNZ/fulltext/images/3469144c9ace8890abb6c2eed9ad00757cf63a2d6fee21f2dcce700c519348b7.jpg)  
Fig. 5. Metal recovery and waste generation.

![](/api/attachments/7JE8AYNZ/fulltext/images/f45ab40e08adf709186dde672e97ed9d50209df17bc93fbd4a20fab79ab262c8.jpg)

![](/api/attachments/7JE8AYNZ/fulltext/images/57db4d57698adf6f4c45ee764249a4019cc6469bc76924b5c132d782486180d1.jpg)  
Fig. 6. Pollution tax and waste generation.

and actual operating costs and has a negative effect on mine profitability. Thus, as a pollution tax affects the profitability of a mine, it affects the ore grade that can be economically recovered, and as marginal mines with lower ore grades generate more waste/tonne of mineral, a pollution tax may be seen by some governments as an effective means of discouraging development.

As a further example of model output, consider the effect of increased planning delays on retained earnings. It is well documented that the period from the initiation of exploration to the beginning of commercial production, the gestation period, may take upwards of 10 years Table 2 [1,2,4].

For example, in the case of the Tara mine in Ireland, the gestation period was 8 years see note at the top and with the Lisheen mine (also in Ireland) the gestation period was 13 years (exploration of approximately 4 years and time between discovery and production 9 years).

The gestation period includes the discovery delay, the construction delay, and any delays caused by planning requirements. Increased planning delays are often the result of meeting environmental planning and EIA requirements, as well as objections to the mining development on environmental and other grounds by the public or other interested bodies: these are captured by the model using Discovery\_Delay, Construction\_Delay\_Normal, and Planning\_Delay\_- Normal, respectively. The construction delay is modulated as a function of mine life (size) and the planning delay is modulated as a function of the stringency of the regulatory and planning requirements. Changes to the duration of these delays may have a significant effect on the profitability of a mining operation.

<table><tr><td>Period from initiation of exploration to commercial production (years)</td><td>Number of mining projects</td></tr><tr><td>5 or less</td><td>2</td></tr><tr><td>6–10</td><td>14</td></tr><tr><td>11–15</td><td>17</td></tr><tr><td>16–20</td><td>6</td></tr><tr><td>&gt;20</td><td>13</td></tr></table>

Tables 3–5 present selected output pertaining to the profitability of mining Deposit221, for the purpose of illustrating the time-scales involved in the development process.

Firm2 begins funding a 5 years exploration effort in 2029. A discovery delay of 5 years, modelled as a third-order material delay, results in 50% of the available resources (13.35 million tonnes) being discovered by 2036. Under the very favourable market conditions of 2036, when price exceeds US\$ 1200/tonne (not shown here), 6.67 million tonnes of ore is sufficient to justify development (NPV > US\$ 20million).

Construction is funded through borrowing 75% (determined by Percentage\_of\_Profits\_Reinvisted \_in\_New\_Mines) of the estimated cost of construction (US\$ 52.32 million). The remainder is taken from retained earnings.

However, a 2 years planning delay and a 3 years construction delay means that mine operation does not start until 2041, at which time extraction starts at maximum productivity (1.5 times normal extraction rate) to avail of the upturn in the market. By this time, price has fallen by more than US\$ 150/tonne since the original cost estimates were made, but still remains above the unit operating cost. However, by 2050, price begins a rapid fall to under US\$ 1000/tonne and, thus, any major increase in the planning delay will have significant impact on mine profitability.

This is an important point, because increased planning (and construction) delays may cause individual mines to miss upturns in the market and the resulting negative impact on Retained\_Earnings will feed back to influence Prior\_Company\_Experience in the country in question and, consequently, future exploration investment. Increased delays also affect the time value of money as projected profits are discounted further into the future. Costs (such as interest on borrowings) have to be incurred for longer without any turnover to meet repayments (see Table 5).

Table 4 Construction commences  
Table 3  
The exploration phase

<table><tr><td>Time period</td><td>2029</td><td>2030</td><td>2031</td><td>2032</td><td>2033</td><td>2034</td><td>2035</td><td>2036</td></tr><tr><td>Available_Resources(2,2,1)</td><td>1.335e7</td><td>6.676e6</td><td>6.676e6</td><td>6.676e6</td><td>6.676e6</td><td>6.676e6</td><td>6.676e6</td><td>6.676e6</td></tr><tr><td>Average_Ore_Grade(2,2,1)</td><td>0.168</td><td>0.168</td><td>0.168</td><td>0.168</td><td>0.168</td><td>0.168</td><td>0.168</td><td>0.168</td></tr><tr><td>Wxploration_Budget_Allocation</td><td>827073</td><td>827073</td><td>827073</td><td>827073</td><td>827073</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>Discovery_Delay(2,2,1)</td><td>5.00</td><td>5.00</td><td>5.00</td><td>5.00</td><td>5.00</td><td>5.00</td><td>5.00</td><td>5.00</td></tr><tr><td>Discovery_Rate(2,2,1)</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.442e6</td><td>3.172e6</td><td>2.031e6</td><td>0.00</td></tr><tr><td>Proven_Reserves(2,2,1)</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.442e6</td><td>4.614e6</td><td>6.676e6</td></tr><tr><td>Net_Present_Value(2,2,1)</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>-1.1e7</td><td>1.653e7</td><td>3.762e7</td></tr></table>

<table><tr><td>Time</td><td>2036</td><td>2037</td><td>2038</td><td>2039</td><td>2040</td><td>2041</td></tr><tr><td>Proven_Reserves(2,2,1)</td><td>6.676e6</td><td>6.676e6</td><td>6.676e6</td><td>6.676e6</td><td>6.676e6</td><td>6.676e6</td></tr><tr><td>Net_Present_Value(2,2,1)</td><td>3.762e7</td><td>3.8e7</td><td>3.639e7</td><td>3.515e7</td><td>3.392e7</td><td>3.292e7</td></tr><tr><td>E_Planning_Delay(2)</td><td>2.00</td><td>2.00</td><td>2.00</td><td>2.00</td><td>2.00</td><td>2.00</td></tr><tr><td>E_Planning_Costs(2,2,1)</td><td>3.19e6</td><td>3.19e6</td><td>3.19e6</td><td>3.19e6</td><td>3.19e6</td><td>3.19e6</td></tr><tr><td>E_Construction_Delay(2,2,1)</td><td>2.97</td><td>2.97</td><td>2.97</td><td>2.97</td><td>2.97</td><td>2.97</td></tr><tr><td>E_Mine_Life(2,2,1)</td><td>10.00</td><td>10.00</td><td>10.00</td><td>10.00</td><td>10.00</td><td>10.00</td></tr><tr><td>Mineable_Reserves(2,2,1)</td><td>0.00</td><td>0.00</td><td>0.00</td><td>2.225e6</td><td>5.934e6</td><td>6.676e6</td></tr><tr><td>Extraction_Rate_Normal(2,2,1)</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>667552</td></tr><tr><td>Extraction_Rate(2,2,1)</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.001e6</td></tr><tr><td>Average_Ore_Grade_Remaining(2,2,1)</td><td>0.168</td><td>0.168</td><td>0.168</td><td>0.168</td><td>0.168</td><td>0.168</td></tr><tr><td>E_Cost_of_Construction(2,2,1)</td><td>5.232e7</td><td>5.232e7</td><td>5.232e7</td><td>5.232e7</td><td>5.232e7</td><td>5.232e7</td></tr><tr><td>Borrowings(2,2,1)</td><td>3.924e7</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr></table>

Table 5 Borrowings and interest

<table><tr><td>Time Period</td><td>2036</td><td>2037</td><td>2038</td><td>2039</td><td>2040</td></tr><tr><td>Borrowings(2,2,1)</td><td>3.924e7</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>Turnover(2,2,1)</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>Operating_Costs(2,2,1)</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>Operating_Profit(2,2,1)</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>Depreciation(2,2,1)</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>R_and_D(2,2,1)</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>Profit_on_Ordinary_Activities_b</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>Interest(2,2,1)</td><td>212043</td><td>2.839e6</td><td>2.981e6</td><td>3.13e6</td><td>3.286e6</td></tr></table>

Fig. 7 shows the balance sheet for the simulated mine in 2042, the first year of operation. Normal extraction rate is calculated using an estimated mine life of 10 years and, although the normal rate of extraction is exceeded in the early years of operation, the mine actually operates for 14 years as a result of additional reserves discovered during the proving-up phase. In the final year of operation, 2056, the mine operates at a loss as market conditions start to become unfavourable. However, overall this particular mine is very profitable; Fig. 8 presents the balance sheet for the mine in 2056.

Fig. 9 presents a similar balance sheet for a separate simulation run where all parameters are identical, with the exception of a once-off 3 years increase in the planning delay.

An increased planning delay of 3 years results in a reduced retained earning of almost US\$ 40million over the life of the mine. This is primarily because the mine would be unable to exploit the favourable market conditions of the 2050s, and operates into the downturn in demand for zinc.

The degradation of profitability in this simulation example is much greater than the percentage increase in ‘actual’ planning costs resulting from the planning delay. This is an example of counterintuitive system behaviour and is due to the complexity of the system, coupled with its inherent delays that results in changes in one part of the system (planning regulations) having an amplified effect elsewhere (mine profitability).

For such reasons, it is not sufficient to consider the effect of increased planning delays and/or changes to environmental regulatory and planning requirements in isolation. Every situation is different and the prevailing market conditions are particularly important.

<table><tr><td colspan="4">Balance Sheet : 2042</td></tr><tr><td>ASSETS</td><td></td><td>LIABILITIES</td><td></td></tr><tr><td>Cash</td><td>-$16,620,978</td><td>Debt</td><td>$55,841,557</td></tr><tr><td>Book Value</td><td>$47,091,044</td><td></td><td></td></tr><tr><td></td><td></td><td>EQUITY</td><td></td></tr><tr><td></td><td></td><td>Equity Issue</td><td>$595,233</td></tr><tr><td></td><td></td><td>Retained Earnings</td><td>-$25,966,724</td></tr><tr><td></td><td>$30,470,066</td><td></td><td>$30,470,066</td></tr><tr><td colspan="4">Balance Sheet : 2060</td></tr><tr><td>ASSETS</td><td></td><td>LIABILITIES</td><td></td></tr><tr><td>Cash</td><td>$94,257,005</td><td>Debt</td><td>$7,462,329</td></tr><tr><td>Book Value</td><td>$9,695,628</td><td></td><td></td></tr><tr><td></td><td></td><td>EQUITY</td><td></td></tr><tr><td></td><td></td><td>Equity Issue</td><td>$582,121</td></tr><tr><td></td><td></td><td>Retained Earnings</td><td>$95,908,183</td></tr><tr><td></td><td>$103,952,633</td><td></td><td>$103,952,633</td></tr></table>

Fig. 7. Balance sheet for mine in 2042.

Fig. 8. Balance sheet for the same mine with increased planning delay.

<table><tr><td colspan="4">Balance Sheet : 2056</td></tr><tr><td>ASSETS</td><td></td><td>LIABILITIES</td><td></td></tr><tr><td>Cash</td><td>$130,031,855</td><td>Debt</td><td>$7,189,607</td></tr><tr><td>Book Value</td><td>$10,772,920</td><td></td><td></td></tr><tr><td></td><td></td><td>EQUITY</td><td></td></tr><tr><td></td><td></td><td>Equity Issue</td><td>$595,233</td></tr><tr><td></td><td></td><td>Retained Earnings</td><td>$133,019,935</td></tr><tr><td></td><td>$140,804,775</td><td></td><td>$140,804,775</td></tr></table>

Fig. 9. Balance sheet for mine in 2056.

## 8. Conclusions

In a simple system or mental model, cause-andeffect are closely related in space and time. From such a perspective, increased planning delays would simply result in increased planning costs. However, increased planning delays may, under adverse market conditions, have a significant impact on profitability that is much more than the original increase in planning costs. Not only does the model provide a means of evaluating the effects of alternative policies but it provides a very powerful means of evaluating the effects of the same policy under different conditions.

Furthermore, the multi-dimensional aspects of this model allows the user to test different sets of assumptions and policies by setting different parameter values for each of the mining firms and countries. In this way, the dynamics of relative attractiveness may be exposed through the flow of exploration funds between countries.

The model is the present state of an iterative evolutionary process. Initial plans have been modified and the project’s scope redefined on a number of occasions as a result of increased understanding, which only comes with prolonged experience. Many of the important dynamics presented in verbal models have been exposed. As a result, the numerous interrelating factors that impact the effects of governmental policies may be examined afresh.

Simulation models in the system dynamics tradition may be used once off to analyse a particular investment opportunity or may be incorporated as part of a distributed, integrated management system. They help reduce the risk of new strategic initiatives by allowing managers to experiment with alternative decisions in a simulated business environment. In this way simulations enhance and complement spreadsheets, database tools, and risk analysis software by combining both historical data and ‘‘cause-and-effect’’ assumptions about future performance.

## References

[1] G. Caraghiaur, Financing of the small, independent mining enterprise, in: C.R. Tinsley, M.E. Emerson, W.D. Eppler (Eds.), Finance for the Minerals Industry, Society of Mining Engineers, USA, 1985, pp. 65–70.

[2] M.E. Emerson, Independent engineering information for project financing, in: C.R. Tinsley, M.E. Emerson, W.D. Eppler (Eds.), Finance for the Minerals Industry, Society of Mining Engineers, USA, 1985, pp. 483–487.

[3] B. O’Regan, R. Moles, A system dynamics model of mining industry investment decisions within the context of environmental policy, Journal of Environmental Planning and Management (UK) 44 (2), 2001, pp. 245–262.

[4] J. Otto, The Exploration and Mine Development Regulatory Time Dilemma, Professional Paper PP15, Centre for Petroleum and Mineral Law and Policy, University of Dundee, Scotland, 1995.

Bernadette O’Regan has a degree in Production Management and her PhD is in the field of Environmental Science. She is working as a lecturer and senior researcher in Environmental Management at the University of Limerick. Her research interests include modelling complex systems and environmental policy.

Richard Moles is a senior lecturer and the director of the Centre for Environmental Research at the University of Limerick.
