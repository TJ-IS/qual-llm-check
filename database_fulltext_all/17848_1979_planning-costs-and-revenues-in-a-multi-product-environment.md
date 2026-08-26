---
otero_id: 17848
otero_key: "DGSAMXTA"
title: "Planning costs and revenues in a multi-product environment"
authors: "C.Warren Axelrod"
year: "1979"
journal: "Information & Management"
doi: "10.1016/0378-7206(79)90017-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Planning Costs and Revenues in a Multi-Product Environment

C. Warren Axelrod \*

Director, Strategy Planning, Securities Industry Automation Corp.

Each year companies commit to development budgets which include funds for new and ongoing projects. Since the initial funding of a project implies future costs for continuing work and revenues (or other benefits) from the product, it is clear that new project funding for the coming year will continue to affect profit and loss into the future.

If the distributions over time of the costs and the resulting revenues can be estimated, a planning model can be built which will facilitate decision-making under criteria such as steady growth in annual costs or specified revenue-to-cost ratio for particular years. The tedious manual application of this model can be greatly assisted by means of an interactive computer program. A long-range development budget can then be quickly prepared.

This paper shows in non-mathematical terms how such a model can be developed and applied. The appendix contains the mathematical derivation of the model.

Keywords: Multi-product planning, interactive decision-making, computer-aided system, product life cycle.

## 1. Introduction

The development and implementation of a system (e.g., computer, weapons, ...) or the development, production and sale of a product or service (e.g., consumer, industrial ...) is phased over time. For a system, Rosove [3] and Seiler [4] propose five phases of development: research, design, fabrication, installation, and operation. Fisher [1] combines these into three major cost categories, namely, research and development (i.e., research, design), investment (i.e., fabrication, installation), and operating costs. Goggin [2] describes seven stages of the product life cycle: conception, feasibility, product development, commercialization, market expansion, product maturity, and obsolescence. A similar life cycle holds true for a service, although the emphasis on the various stages will differ.

Each of the above phases involve costs, which are illustrated in figs. 1, 2, and 3 for a typical system, product, and service respectively. The implementation of a system or the sale of a product or service will result in benefits to the developer which may be represented in terms of effectiveness (for a system) or revenues (for a product or service). We term these benefits “returns” for the general case, and indicate that these returns are also phased over time in some fashion, perhaps as shown in figs. 1, 2 and 3. A great body of analysis exists on the evaluation of individual projects in terms of their cost-effectiveness of their return on investment. The problem addressed here is this: Suppose we have many projects in which to invest for which the development/implementation cost patterns, as well as the distribution of returns over time, are known. What annual investment level should be funded to fulfil some predetermined criteria such as a steady growth in profits or investment, or minimization of year-to-year fluctuations in expenses? Since the range of feasible choices is very great and each choice requires considerable calculation, the use of computer assistance immediately comes to mind. However, since the criteria are highly subjective, it would be valuable for the decision-maker to have a “feel” for the behavior and sensitivity of the cost-return system due to changes in input, which suggests an interactive computer-aided system such as that described in this paper.

![](/api/attachments/DGSAMXTA/fulltext/images/7878d04d8ea5b75df9469843a857760c2ee5761a8ee9e0869b6aa73f05cfe595.jpg)

![](/api/attachments/DGSAMXTA/fulltext/images/0eacf533346fdb48d49741b061acbd2ea69bee9d6ec6838a6a6ca33f5513e5fc.jpg)  
Fig. 1. Time distribution of costs and benefits for a system life cycle.

![](/api/attachments/DGSAMXTA/fulltext/images/5a30c0ad16d082241eeabc7bd78f4b1eea1736cdb8574941c2c931bcbd106157.jpg)  
Fig. 2. Time distribution of costs and revenues for a product life cycle.

![](/api/attachments/DGSAMXTA/fulltext/images/8c71b116f5690785019d229a3aff49420efced07a5ff9ac1a1919568cf30c72f.jpg)  
Fig. 3. Time distribution of costs and revenues for a service life cycle.

## 2. Assumptions

We consider an environment in which there are many projects, each of small size relative to the overall budget level. Each project is assumed to have the same cost and return phasing, the parameters of which have been determined empirically from historical data. Examples of such distributions are shown in table 1.

Table 1 shows the cost and return coefficients for a succession of periods. The periods may be years, quarters, months, etc. The interpretation of the coefficients is as follows: Each dollar spent in period 1 will result in related expenditures of \$1.25, 20 cents and 5 cents in the successive three periods. If there is a one-period “displacement” between costs and returns, then for each dollar spent in period 1 the expected returns will be 37.5 cents, 83.3 cents, \$1.167, \$1.04 and 75 cents for periods 2 through 6 respectively. If the displacement is two periods the return coefficients are moved down one further period as shown in column 3 of table 1. Overall, it is anticipated that \$1.666 will be returned for each dollar spent on the development and implementation stages. The 66.6 cents per dollar margin may go towards overhead and selling costs, the remainder being profit (if the return is revenue).

Table 1
Examples of cost and return distributions

<table><tr><td rowspan="2">Period</td><td rowspan="2">Cost Coefficients</td><td colspan="2">Return Coefficients</td></tr><tr><td>One-Period Displacement</td><td>Two-Period Displacement</td></tr><tr><td>1</td><td>1.00</td><td></td><td></td></tr><tr><td>2</td><td>1.25</td><td>0.375</td><td></td></tr><tr><td>3</td><td>0.20</td><td>0.833</td><td>0.375</td></tr><tr><td>4</td><td>0.05</td><td>1.167</td><td>0.833</td></tr><tr><td>5</td><td></td><td>1.040</td><td>1.167</td></tr><tr><td>6</td><td></td><td>0.750</td><td>1.040</td></tr><tr><td>7</td><td></td><td></td><td>0.750</td></tr><tr><td>Totals</td><td>2.50</td><td>4.165</td><td>4.165</td></tr><tr><td colspan="4"> $\frac{\text{Total return}}{\text{Total cost}} = 1.666$ </td></tr></table>

As will be seen later, the return-to-cost ratio per period may never actually coincide with the total-return-to-total-cost ratio of table 1 due to fluctuations in periodic expenditures.

## 3. The decision model

Each period the organization must determine its level of spending. If we agree with the above assumptions, all future cost and revenue flows follow a pattern based on expenditures on new projects; the decision thus reduces to determining the funds to be spent on new projects. The decision model takes these initial project costs and extends them to show their cost-return impact. A second version of the model derives the initial cost requirement for some specified total annual return. The derivation of the model is shown in the appendix.

## 4. Illustrative examples

The following two examples demonstrate the computer model in both its modes, namely, the decision variable for each period may be (1) the initial cost, or (2) the total return. Thus the decision-maker may examine the effects of different initial costs on periodic costs and returns, or may see how much should be spent to realize a specific total return.

```txt
INITIAL
ENTER FIRST PERIOD FOR WHICH INITIAL COST TO BE DETERMINED
□ 1977
ENTER COST COEFFICIENTS (PERIOD 1, PERIOD 2, ...)
□ 1 1.25 .2 .05
ENTER RETURN COEFFICIENTS (PERIOD 1, PERIOD 2, ...)
□ .375 .833 1.167 1.04 .75
WHAT IS THE DISPLACEMENT (NO. OF PERIODS) BETWEEN RETURNS AND COSTS?
□ 1
ENTER INITIAL COSTS OF PERIODS 1972 1973 1974 1975 1976
□ 900 800 950 1100 1000

TOTAL RETURN FOR PERIOD 1977 IS 3907.0

TOTAL COST FOR PERIOD 1976 IS 2605.0

IS DECISION VARIABLE INITIAL COST (ENTER '1') OR TOTAL RETURN (ENTER '2')?
□ 1

ENTER INITIAL COST FOR PERIOD 1977
□ 1200

TOTAL RETURN FOR PERIOD 1978 IS 4154.7

TOTAL COST FOR PERIOD 1977 IS 2717.5

DO YOU WISH TO SEE COMPLETE TABLE (YES OR NO)?
NO
DO YOU WISH TO CALCULATE ANOTHER YEAR (YES OR NO)?
YES

ENTER INITIAL COST FOR PERIOD 1978
□ 1250

TOTAL RETURN FOR PERIOD 1979 IS 4491.9

TOTAL COST FOR PERIOD 1978 IS 3005

DO YOU WISH TO SEE COMPLETE TABLE (YES OR NO)?
NO
DO YOU WISH TO CALCULATE ANOTHER YEAR (YES OR NO)?
YES

ENTER INITIAL COST FOR PERIOD 1979
□ 1:00

TOTAL RETURN FOR PERIOD 1980 IS 4719.2

TOTAL COST FOR PERIOD 1979 IS 2952.5

DO YOU WISH TO SEE COMPLETE TABLE (YES OR NO)?
YES
(SEE TABLE BELOW)
DO YOU WISH TO CALCULATE ANOTHER YEAR (YES OR NO)?
NO
```  
Fig. 4A. Procedure when decision variable is initial cost.

COSTS (THOUSANDS OF DOLLARS)

<table><tr><td>PERIODS</td><td>1972</td><td>1973</td><td>1974</td><td>1975</td><td>1976</td><td>1977</td><td>1978</td><td>1979</td><td>1980</td><td>1981</td><td>1982</td><td>1983</td><td>1984</td></tr><tr><td></td><td>900.0</td><td>1125.0</td><td>180.0</td><td>45.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>800.0</td><td>1000.0</td><td>160.0</td><td>40.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>950.0</td><td>1187.5</td><td>190.0</td><td>47.5</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>1100.0</td><td>1375.0</td><td>220.0</td><td>55.0</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>1000.0</td><td>1250.0</td><td>200.0</td><td>50.0</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>1200.0</td><td>1500.0</td><td>240.0</td><td>60.0</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1250.0</td><td>1562.5</td><td>250.0</td><td>62.5</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1100.0</td><td>1375.0</td><td>220.0</td><td>55.0</td><td></td><td></td></tr><tr><td>TOTALS</td><td>900.0</td><td>1925.0</td><td>2130.0</td><td>2492.5</td><td>2605.0</td><td>2717.5</td><td>3005.0</td><td>2952.5</td><td>1685.0</td><td>282.5</td><td>55.0</td><td></td><td></td></tr><tr><td colspan="14">RETURNS (THOUSANDS OF DOLLARS)</td></tr><tr><td>PERIODS</td><td>1972</td><td>1973</td><td>1974</td><td>1975</td><td>1976</td><td>1977</td><td>1978</td><td>1979</td><td>1980</td><td>1981</td><td>1982</td><td>1983</td><td>1984</td></tr><tr><td></td><td></td><td>337.5</td><td>749.7</td><td>1050.3</td><td>936.0</td><td>675.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>300.0</td><td>666.4</td><td>933.6</td><td>832.0</td><td>600.0</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>356.3</td><td>791.4</td><td>1108.7</td><td>988.0</td><td>712.5</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>412.5</td><td>916.3</td><td>1283.7</td><td>1144.0</td><td>825.0</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>375.0</td><td>833.0</td><td>1167.0</td><td>1040.0</td><td>750.0</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>450.0</td><td>999.6</td><td>1400.4</td><td>1248.0</td><td>900.0</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>468.8</td><td>1041.3</td><td>1458.8</td><td>1300.0</td><td>937.5</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>412.5</td><td>916.3</td><td>1283.7</td><td>1144.0</td><td>825.0</td></tr><tr><td>TOTALS</td><td></td><td>337.5</td><td>1049.7</td><td>2073.0</td><td>3073.5</td><td>3907.0</td><td>4154.7</td><td>4491.9</td><td>4719.2</td><td>4373.1</td><td>3483.7</td><td>2081.5</td><td>825.0</td></tr><tr><td>RET/COST</td><td></td><td>0.18</td><td>0.49</td><td>0.83</td><td>1.18</td><td>1.44</td><td>1.38</td><td>1.52</td><td>2.80</td><td>15.48</td><td>63.34</td><td></td><td></td></tr><tr><td colspan="14">Fig. 4B. Table produced by initial cost procedure.</td></tr></table>

![](/api/attachments/DGSAMXTA/fulltext/images/8a4b735f527b803d6980ef902bf19d03641bf1b0d07f9d376510a18fc5d8e635.jpg)  
Fig. 5A. Procedure when decision variable is total return.

Fig. 5B. Table produced by total return procedure.

<table><tr><td>PERIODS</td><td>1972</td><td>1973</td><td>1974</td><td>1975</td><td>1976</td><td>1977</td><td>1978</td><td>1979</td><td>1980</td><td>1981</td><td>1982</td><td>1983</td><td>1984</td><td>1985</td></tr><tr><td></td><td>900.0</td><td>1125.0</td><td>160.0</td><td>45.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>800.0</td><td>1000.0</td><td>160.0</td><td>40.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>950.0</td><td>1187.5</td><td>190.0</td><td>47.5</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>1100.0</td><td>1375.0</td><td>220.0</td><td>55.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>1000.0</td><td>1250.0</td><td>200.0</td><td>50.0</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>787.5</td><td>984.3</td><td>157.5</td><td>39.4</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1388.1</td><td>1735.1</td><td>277.6</td><td>69.4</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>1226.0</td><td>1532.4</td><td>245.2</td><td>61.3</td><td></td><td></td><td></td></tr><tr><td>TOTALS</td><td>900.0</td><td>1925.0</td><td>2130.0</td><td>2492.5</td><td>2605.0</td><td>2305.0</td><td>2627.4</td><td>3168.6</td><td>1849.4</td><td>314.6</td><td>61.3</td><td></td><td></td><td></td></tr><tr><td colspan="15">RETURNS (THOUSANDS OF DOLLARS)</td></tr><tr><td>PERIODS</td><td>1972</td><td>1973</td><td>1974</td><td>1975</td><td>1976</td><td>1977</td><td>1978</td><td>1979</td><td>1980</td><td>1981</td><td>1982</td><td>1983</td><td>1984</td><td>1985</td></tr><tr><td></td><td></td><td></td><td>337.5</td><td>749.7</td><td>1050.3</td><td>936.0</td><td>675.0</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>300.0</td><td>666.4</td><td>933.6</td><td>832.0</td><td>600.0</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>356.3</td><td>791.4</td><td>1108.7</td><td>988.0</td><td>712.5</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td>412.5</td><td>916.3</td><td>1283.7</td><td>1144.0</td><td>825.0</td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>375.0</td><td>833.0</td><td>1167.0</td><td>1040.0</td><td>750.0</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>295.3</td><td>656.0</td><td>919.0</td><td>819.0</td><td>590.6</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>520.5</td><td>1156.3</td><td>1619.9</td><td>1443.6</td><td>1041.1</td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>459.7</td><td>1021.2</td><td>1430.7</td><td>1275.0</td><td>919.5</td></tr><tr><td>TOTALS</td><td></td><td></td><td>337.5</td><td>1049.7</td><td>2073.0</td><td>3073.5</td><td>3907.0</td><td>4000.0</td><td>4200.0</td><td>4400.0</td><td>4210.1</td><td>3464.9</td><td>2316.1</td><td>919.5</td></tr><tr><td>RET/COST</td><td></td><td></td><td>0.16</td><td>0.42</td><td>0.80</td><td>1.33</td><td>1.49</td><td>1.26</td><td>2.27</td><td>13.99</td><td>68.68</td><td></td><td></td><td></td></tr></table>

Fig. 4A shows the interactive procedure for the case in which the decision variable is initial cost. The user is asked to provide the starting point, which in this case is 1977. The cost and return coefficients are then entered. Note that no displacement is shown here, i.e., the return coefficient for year 1 is given as 0.375. The displacement is given in answer to the next question. The user is then requested to enter the initial costs for the number of prior years which will allow the 1977 return to be obtained if the displacement is one year. If all the required data are not available, zeros can be entered – however, this will invalidate the 1977 total return and total cost, and perhaps other years' total returns and total costs (unless of course the entries are really zero). In general, total costs and returns will not be meaningful prior to the first decision year (here 1977) if there was relevant business activity prior to the earliest year (here 1972).

At this point, the decision-maker may choose which decision variable is to be used, initial cost or total return. In fig. 4A the initial cost option is selected. An example of the total return option is shown in fig. 5A. Continuing with fig. 4A, the program asks for the first initial cost, and in response gives the total cost for the same period and the total revenue for the period which is advanced by the amount of the displacement. These can be compared with the numbers given for the corresponding immediately-prior periods to see if the progression is satisfactory. At this point, the user is asked whether a complete table of the calculations to date is wanted, to which a negative response is given in the example. The succeeding decision period is then accessed by responding affirmatively to the next question. The next initial cost is entered and the above sequence is repeated. At each stage the user is provided with the corresponding total cost and return to aid in determining the magnitude of the next initial cost. If the complete picture is needed (as, for example, at the end of a run) the table printing option can be activated. This will produce tables such as that shown in fig. 4B. The upper table indicates the initial costs, the succeeding costs resulting from the initial costs, and the total costs per period. The lower table shows the corresponding returns. The bottom line gives the total-return-to-total-cost ratio. It should be noted that, if there had been costs prior to 1972 for this example, some or all the total costs for 1972–1974, the 1972–1976 returns, and the 1973–1976 ratios could be invalid for comparison or projection purposes. Furthermore, total costs after 1979 and total return after 1980 will be masked by any further projects initiated after 1979. It is interesting to observe that the periodic return-cost ratio is below the 1.666 value mentioned previously for 1977–1979. This is to be expected in a situation where the costs are increasing each year and the corresponding returns are displaced. When the initial costs are terminated, the ratio rises rapidly, even though the 1.666 value still holds. Consequently care must be taken in interpreting this ratio in terms of performance, since it is so strongly related to the dynamics of the system.

The example of fig. 5A is similar to the previous example except that the displacement is now two years, and the total return option is selected. With this option, the user provides the total return and the program generates the initial cost that would produce that return. The user is informed of the minimum return to be entered, namely, that which would require zero initial cost. Fig. 5B shows the results of this run in the same format as fig. 4B.

## 5. Extensions of the model

Two options for the decision variable are presented here, namely, the initial cost and total return. Additional options that could be readily incorporated into the program are: total cost per period yielding initial cost per period (i.e. resource-constrained project-environments), return-cost ratio yielding initial cost, or changes in the total-return-to-total-cost ratio of table 1 giving different return coefficients which could be used with any of the other options. More sophisticated adaptations of the model could include the dynamic modification of the cost or return coefficients or both, or even modification of the displacement. These latter enhancements are useful in reflecting changes in technological complexity or in the size of the organization, since, typically, as complexity and size increase so do the lead times in development, production and marketing.

Further enhancements might include risk analysis and cash flow discounting.

## 6. Other uses

Besides the cost-return formulation, models of this type can be adapted for such diverse applications as credit charges and inventories. For the credit example, single period charges or receivables result in a distribution of subsequent payments. The model could be used to investigate the payment patterns produced by a seasonally fluctuating charging pattern assuming that the payment distribution remains fixed. Conversely, the effect of a changing payment distribution could be examined.

In the inventory case, the costs are replaced by production initiation and returns by the distribution of product completion. Here the displacement is the lead time between initiating production and the first products coming off the line. The model would be used in the total return mode, whereby the decision-maker would provide the anticipated sales levels and the model would generate the level of production to be initiated to meet that sales level. In a slightly different formulation, the “initial return” could represent sales direct from production and the subsequent returns from that production run would be the sales from inventory.

## Conclusions

Corporate planners need easy and quick ways to compute the relationships between inflows and outflows for a relatively stable planning model. The use of an interactive computerized tool, such as that described in this paper, facilitates the examination of a large number of scenarios with minimum effort.

## Appendix. The mathematical derivation of the model

## Cost relationships

Let $C_{p}^{k}$ ( $k = 1, 2, ..., m$ ), where $m$ is the number of years in the cost distribution, be the expenditure in year p on programs in their kth year of development/implementation, e.g.

$C_{1968}^{l} =$ expenditure on new programs in 1968,

$C_9^2 =$ expenditure on 2-period-old programs in period 9

The total expenditure in year p, $K_{p}$ , is made up of the expenditure on new programs, $C_{p}^{1}$ , together with expenditures generated by programs initiated up to $(m - 1)$ years previously, that is:

$$
K _ {p} = C _ {p} ^ {1} + C _ {p} ^ {2} + \dots + C _ {p} ^ {m}.
$$

For example, total expenditure in 1977, for $m = 4$ , is:

$$
K _ {1 9 7 7} = C _ {1 9 7 7} ^ {1} + C _ {1 9 7 7} ^ {2} + C _ {1 9 7 7} ^ {3} + C _ {1 9 7 7} ^ {4}.
$$

$K_{p}$ may be expressed in compact form as:

$$
K _ {p} = \sum_ {i = 1} ^ {m} C _ {p} ^ {i} \text {   for   any   } p.
$$

For example, from table 1, each dollar spent of new programs in year $p$ generates an expenditure of \$ 1.25 in year $(p + 1)$ , 20 cents in $(p + 2)$ , and 5 cents in $(p + 3)$ , i.e., expenditure in 1978 on programs in their second year of development, $C_{1978}^{2}$ , is equal to 1.25 times the 1977 expenditure on new programs, that is $C_{1978}^{2} = 1.25$ $C_{1977}^{1}$ .

The general relationships are:

$$
\begin{array}{l} C _ {p} ^ {2} = 1. 2 5 C _ {p - 1} ^ {1}, \\ C _ {p} ^ {3} = 0. 2 0 C _ {p - 2} ^ {1}, \\ C _ {p} ^ {4} = 0. 0 5 C _ {p - 3} ^ {1}. \end{array}
$$

Now, it was shown previously that

$$
K _ {p} = C _ {p} ^ {1} + C _ {p} ^ {2} + C _ {p} ^ {3} + C _ {p} ^ {4} \text {   for   any   } p, \text {   and   } m = 4,
$$

therefore

$$
K _ {p} = C _ {p} ^ {1} + 1. 2 5 C _ {p - 1} ^ {1} + 0. 2 0 C _ {p - 2} ^ {1} + 0. 0 5 C _ {p - 3} ^ {1}.
$$

Thus $K_{p}$ is expressed in terms of expenditures on new programs, for example, for 1977

$$
K _ {1 9 7 7} = C _ {1 9 7 7} ^ {1} + 1. 2 5 C _ {1 9 7 6} ^ {1} + 0. 2 0 C _ {1 9 7 5} ^ {1} + 0. 0 5 C _ {1 9 7 4} ^ {1}.
$$

Substituting $a_{1}$ for 1, $a_{2}$ for 1.25, $a_{3}$ for 0.2, $a_{4}$ for 0.05, we get

$$
K _ {p} = a _ {1} C _ {p} ^ {1} + a _ {2} C _ {p - 1} ^ {1} + a _ {3} C _ {p - 2} ^ {1} + a _ {4} C _ {p - 3} ^ {1}.
$$

For the general case,

$$
K _ {p} = \sum_ {j = 1} ^ {m} a _ {j} C _ {p - (j - 1)} ^ {1}.\tag{1}
$$

Return relationships

Let $U_{p}^{k}$ ( $k = 1, 2, ..., n$ ), where $n$ is the number of years in the return distribution, be the return on programs in their $k$ th year of returns, e.g.,

$U_{1070}^{2}=$ return in 1970 on programis in their second year of returns.

The total return in year $p$ , $W_p$ , is the summation of the returns of programs initiated from one to $(n - 1)$ years previously, that is

$$
W _ {p} = U _ {p} ^ {1} + U _ {p} ^ {2} + \dots + U _ {p} ^ {n}.
$$

For example, total return in 1977, for n = 5, is:

$$
W _ {1 9 7 7} = U _ {1 9 7 7} ^ {1} + U _ {1 9 7 7} ^ {2} + U _ {1 9 7 7} ^ {3} + U _ {1 9 7 7} ^ {4} + U _ {1 9 7 7} ^ {5}.
$$

$W_{p}$ may be expressed as

$$
W _ {p} = \sum_ {q = 1} ^ {n} U _ {p} ^ {q} \text {   for   any   } p .
$$

Following the same logic as for costs, and using the numbers in table 1, the total return in 1977, with a displacement (d) of one year, is given by

$$
\begin{array}{r l} W _ {1 9 7 7} & = 0. 3 7 5 C _ {1 9 7 6} ^ {1} + 0. 8 3 3 C _ {1 9 7 5} ^ {1} + 1. 1 6 7 C _ {1 9 7 4} ^ {1} \\ & + 1. 0 4 C _ {1 9 7 3} ^ {1} + 0. 7 5 C _ {1 9 7 2} ^ {1}. \end{array}
$$

Substituting $b_{1}$ for 0.375, etc., we get

$$
W _ {p} ^ {\prime} = b _ {1} C _ {p - d} ^ {1} + b _ {2} C _ {p - d - 1} ^ {1} + \dots + b _ {5} C _ {p - d - 4} ^ {1}.
$$

For the general case,

$$
W _ {p} = \sum_ {r = 1} ^ {n} b _ {r} C _ {p - d - (r - 1)} ^ {1}
$$

which can be rewritten:

$$
W _ {p + d} = \sum_ {r = 1} ^ {n} b _ {r} C _ {p - (r - 1)} ^ {1},\tag{2}
$$

which has the same form as equation (1) except for the displacement and the number of terms.

Method

In the computer program, for the initial cost option, the initial cost is substituted in equation (1) to yield the total cost for the same period and in equation (2) to give the total return d periods into the future.

For the total return option, equation (2) is solved for the initial cost of d periods earlier, the latter being substituted in equation (1) to give the total cost.

## References

[1] Gene H. Fisher, Cost Considerations in Systems Analysis, American Elsevier Publishing Company, Inc., (New York, 1971).

[2] William C. Goggin, "How the Multidimensional Structure Works at Dow Corning", in Harvard Business Review -- On Management, Harper and Row (New York, 1975), pp. 650-668.

[3] Perry E. Rosove, Developing Computer-Based Information System, John Wiley and Sons, Inc. (New York, 1968).

[4] Karl Seiler, II, Introduction to Systems Cost-Effectiveness, John Wiley and Sons, Inc. (New York, 1969).
