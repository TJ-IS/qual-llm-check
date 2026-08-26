---
otero_id: 21039
otero_key: "CPPBBU8U"
title: "DSSALM: A decision support system for asset and liability management"
authors: "Gary P. Moynihan; Prasad Purushothaman; Robert W. McLeod; William G. Nichols"
year: "2002"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(01)00131-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# DSSALM: A decision support system for asset and liability management

Gary P. Moynihan <sup>a,</sup>\*, Prasad Purushothaman <sup>a</sup>, Robert W. McLeod <sup>b</sup>, William G. Nichols <sup>a</sup>

<sup>a</sup>Department of Industrial Engineering, The University of Alabama, Box 870228, Tuscaloosa, AL 35487-0288, USA <sup>b</sup>Department of Economics, Finance and Legal Studies, The University of Alabama, Box 870224, Tuscaloosa, AL 35487-0224, USA

Received 1 June 2000; received in revised form 1 December 2000; accepted 1 June 2001

## Abstract

The following paper discusses the development of a decision support system for asset and liability management (ALM) in financial institutions. The system utilizes historical data to develop algorithms that can forecast the amounts of these assets and liabilities. Simulation models are used to identify the crests and troughs of the primary interest rate, and to forecast interest rates for future cycles of interest. The outputs of the algorithms are utilized to calculate the gap position and interest rate risk of the institution. ‘‘What-if’’ analysis features are incorporated into the system to determine the favorable alternatives in changing market environments. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Finance; Banking; Risk Analysis; Asset and liability management

## 1. Introduction

Asset and liability management (ALM) is defined as ‘‘managing both assets and liabilities simultaneously for the purpose of mitigating interest rate risk, providing liquidity and to enhance the value of the bank’’ [7]. It is the process of planning, organizing and controlling asset and liability mixes, volumes, yields, and rates in order to achieve a target interest margin [19]. Asset and liability management views the financial institution as a set of interrelationships that must be identified, coordinated and managed as an integrated system. The primary management goal is the control of interest income and expenses and the resulting net interest margins on an ongoing basis. There is an increase in the number of transactions between various organizations both in terms of value and volume, as well as a rising trend and market for large-scale mergers and acquisitions. These developments have given a new and important role to the financial division of the organization. In general, the assets and liabilities of the organization have become very complex, so that it is no longer possible to use the traditional methods for asset and liability management. Institutions who wish to actively manage their assets and liabilities are faced with the problem of making the best choice among the available methods to provide them with the most efficient management tools.

## 1.1. Background

Asset and liability management is heavily dependent of the movement of interest rates in the market. The market rates include short-term Treasury bill rates, long-term Treasury rates, LIBOR, and commercial paper rates. The values of an organization’s rate-sensitive assets and liabilities are indirectly proportional to the current interest rate risk. These relationships make the management of interest rate risk a very important and prominent function of the organization.

The history of asset and liability management suggests that it is very important for a financial institution to measure, manage and control interest rate risk. One of the most important reasons for the rapid development in tools for asset and liability management is the increase in the involvement of regulatory bodies. Regulators are becoming concerned about financial institutions that either have no ALM procedures or use an outdated one [2]. New laws require financial institutions to declare their maximum interest rate risk exposure; form an asset and liability management committee to monitor the various risks; and install a modeling system to identify and measure the various risks [25].

Other environmental changes have increased the need for a formal and specialized asset and liability management system. Deregulation of the financial industry and the influence of free market forces in the economy are the major factors in financial institutions changing their approach. Other factors include the entrance of new players in investment banking, creation of innovative new products, monetary involvement and the overall increase in competition [17]. The important effect of deregulation is the increased focus on risk management. The margin squeeze resulting from increased competition has allowed financial institutions to maintain profitability by adopting more risk, increasing attention on fee income, and increasing use of off-balance sheet-type activities like derivatives.

## 1.2. Nature of the problem

Interest rate risk must be measured in order to be controlled. Many models have been developed to measure interest rate risk but the most common are gap analysis and duration. Gap analysis is a technique that compares ‘‘the difference in speed at which a financial institution’s assets and liabilities mature, when external interest rate changes’’ [14]. Duration is a ‘‘measure of time weighted average maturity resulting from the cash flows of a financial instrument’’ [15]. However, there are certain limitations in both of these models. Gap analysis is a static measure of interest rate risk and is a short-term measure of interest rate risk [6,26]. Duration considers the time value of money but is difficult to comprehend and apply [26,21]. Recently, computer simulations have been developed to generate interest rate scenarios and determine the interest rate risk [26,3].

The identification of a base case for simulation plays an important role in the accuracy of future gaps and market values. There are a number of simulation techniques available in the market, which can be used for asset and liability management. Simulation is considered to be an expensive tool to measure interest rate risk. The measurement of the current risk exposure fails to consider many factors, which gives an inaccurate indication to the institution.

Another model being researched for its applicability in calculating interest rate risk is stochastic optimization [11]. These models can properly capture the dynamic structure of the decision problem, including the stochastic evolution of the uncertain parameters and the flexibility of the decision-maker to take corrective action as new information becomes available. A key characteristic of stochastic optimization is the ability to consider both asset and liability aspects of a financial problem in an integrated framework. The accuracy of the stochastic optimization and its applicability of interest rate risk are being debated by researchers in this field. Stochastic models suffer from increased computational complexity due to the need to incorporate a large number of scenarios in order to properly account for the uncertainty in model parameters. The size of the optimization program grows exponentially with the length of the time horizon in the planning problem [11].

The literature suggests that no single asset and liability management model would be able to address all forms of interest rate risk [8,10,11,23]. A blend of duration and simulation dominates exclusive reliance on one of the risk measurement technique. It is suggested that a blend of gap analysis and simulation would be able to meet most of the requirements as the disadvantages of one tool could be offset by the advantages of the other tool [8,24]. The cost of the system would be within reasonable limit and the complexity of the system would be reduced. This approach would be a relatively new concept in asset and liability management and the results of such a model could be used to develop more hybrid models.

## 2. Computer-based asset and liability management

The importance of asset and liability management has been recognized in recent years with the development of various strategies and systems. In the early 1980s, the trend was on the development of systems that could perform specific tasks such as the calculation of assets and liabilities. This led to the development of systems, which could calculate the gap of an institution for the current cycle. It soon became apparent that gap analysis was not an accurate measure of interest rate risk. Duration and simulation were being considered as tools for asset and liability management. As the complexity of the tools increased, there was an increased focus on the development of systems that could incorporate the additional features and provide management with an accurate view of the interest rate risk of the institution.

Young et al. [27] developed the Asset/Liability and Profit Planning System to help banks with projecting profit for 2 years in differing interest rate environments. This system determines the amount of interest rate risk and how the risk is distributed within different areas of the bank. It also determines that the risk is cumulative, and if there is significant risk in some other part of the bank, then limited interest rate risk should be recommended [27].

Banks such as the former First Interstate Bancorp have used gap analysis for the calculation of interest rate risk [6]. The gap of the bank included effects of both the balance sheet mix of assets and liabilities and of off-balance sheet commitments such as swaps or futures. This gap takes into account the expected repricing or maturity of its assets and liabilities as contrasted with the contractual maturity of its assets and liabilities [6].

ALMIS uses the time value method, which quantifies the effect of interest rate changes on both net interest income and market value [1]. The time value technique combines the features of the gap analysis and duration techniques. The main features include timely and detailed information relating to the existing balance sheet and profitability, and a comprehensive series of market risk reports analyzing the risks to changing interest rates and currency exchange rates [1].

## 2.1. Application of decision support systems

It became increasingly apparent that traditional information systems could not meet all requirements of an asset and liability management system. Institutions started recognizing the applicability of decision support systems and began their development in specific areas. For example, General Motors developed such a decision support system for asset and liability management. The system established a rate view, provided ‘‘what if’’ capabilities and gave the management feedback on selecting the best method under the circumstances [18].

A more sophisticated approach is represented by RADAR, which is a fully integrated financial risk management and decision support system based an open client/server architecture designed to help financial institutions manage interest rate risk and maximize profits within management-imposed risk limits [9]. The logic behind the model is to provide the capability of handling hundreds of computer simulations on the effect of random interest rate movements. The system begins with the current position and models its evolution, potential behavior in both positive and negative directions in future environments. The distinguishing factor is the interactive exploration of analytical results rather than static reporting. Reports include gap, duration, convexity, a wide range of income forecasts and valuation-oriented reports [9]. The main disadvantage of RADAR is its inability to accommodate risk factors in the calculation of interest rate risk. Historical data could be used to determine trends in the movement of interest rate risks with the amounts of assets and liabilities, which could indicate the risk factor to accommodate in the calculation of interest rate risk.

ALMAN is an integrated system, which addresses interest rate risk, liquidity risk, capital risk, foreign exchange risk and cash flow analysis [22]. The use of a multi-currency system, use of random interest rate scenarios to measure the risk, and forecasting capabilities are some of the important features of the system. It uses simulation and decision support tools for the potential impact of various risk scenarios on the balance sheet, income statements, and cash flow reports [22]. The variance analysis model of ALMAN is used to compare and measure the various strategies in terms of currency, instrument, volume, rate, and tenure. The interest rate forecasting system provides various rate scenarios within which management can position the institution to address different situations [22]. However, the uses of historical data in forecasting the amount of assets and liabilities for a future cycle is absent in ALMAN. The system does not provide many options for ‘‘what if’’ analysis, nor does it include the risk factor in the calculation of interest rate risk, or the reporting features of RADAR. The advantage of ALMAN is that it is a multi-currency system and with the addition of these relevant features, it could become a global asset and liability management system [22].

Strategic Asset/liability Management tool (SAM) is a PC-based simulation tool used for measuring and managing interest rate risk. SAM simulates the reinvestment of maturing and amortizing funds, producing forecast balance sheets, income statement, and ratio analysis [4]. The data input process is also automated increasing the operational efficiency and accuracy. Up to 60 months of historical data can be stored and used for trend analysis, budgeting and comparative reporting. Discounted cash flow analysis and ‘‘what if’’ capabilities give SAM a high modeling power as a financial instrument. However, it fails to address issues like the relationship between different kinds of risk, distribution of assets and liabilities and strategies for different interest rate scenarios [4].

Logica, a systems integration and software company, has developed an asset and liability management system and financial planning software [16]. Bank-Master Plus enables banks to manage interest rate risks in changing environments, accurately forecast future performances, gain widespread access to interest rate risk data, calculate market valuations and duration analyses, and meet regulatory requirements for reporting. The system also lacks ‘‘what if’’ capabilities and does not use historical data to capture trends in interest rates and the amounts of assets and liabilities. The data for the base case simulation of interest rate risk should be calculated on existing data [16].

## 2.2. Selection of the approach

One of the essential features of an asset and liability management system is the use of historical data to model future cycles. Traditionally, historical data have not been effectively used in the calculation of interest rate risk. The various trends in data could be identified using statistical models like forecasting and regression, and the outputs of these models could be simulated to populate the baseline data for the future cycles. The various systems for asset and liability management including the systems discussed earlier in this paper have identified the importance of historical data and are contemplating the development of appropriate models. The selection of the model to calculate interest rate risk is the most important requirement of a true asset and liability management system. The research has indicated that no single model can be used to accurately measure the interest rate risk. Each model has its advantages and limitations. A combination of models, termed a hybrid model, would be an improvement from earlier tools to measure the risk. Gap analysis is a cheap and easily interpretable measure of risk, whereas simulation adds the dynamic capabilities to effectively measure risk. Simulating the interest rate could rectify the static nature of gap analysis, and the inaccurate measure of current risk by simulation could be rectified by gap analysis of existing cycles.

Another important requirement of the system would be its ability to provide different scenarios for the institution. This functionality would be provided by ‘‘what if’’ analysis. Existing systems provide ‘‘what if’’ analysis for a variety of interest rates that are randomly generated. The scenarios could be further normalized, by simulating the amounts of assets and liabilities and providing different gap options of a future cycle. This would increase the number of scenarios for the institution, and trends from historical data could be incorporated in the ‘‘what if’’ analysis resulting in the development of a dynamic functionality of the system.

Similarly, the calculation of interest rate risk would be further normalized with the introduction of risk factors and the error in the calculation of risk for existing cycles. In existing systems, the nature of interest rates has been duly recognized, but their effect on interest rate risk has not been emphasized. The volatility of the interest rate should be recognized while predicting the risk of the institution for a future cycle. The risk factor could be a figure forecasted from existing cycles or could be introduced by the management based on their experience.

With the increase in the sophistication of the data and the frequent fluctuations of the market rates, it is very important for all organizations to have an asset/ liability management system, which can give the organization an accurate representation of its current position and the favorable scenarios for the future. The purpose of the research is to develop a decision support system for asset and liability management. The system will consist of various management science and operations research models to assist in decision-making capabilities. The system developed should meet all requirements of an asset and liability management model discussed previously.

## 3. Data considerations

The decision support system requires inputs from different sources to calculate the interest rate risk. The data from 20 cycles prior to the current cycle of interest have been obtained from a local financial institution, and the data on the movement of the primary interest rate have been obtained from the Federal Reserve Bank of St. Louis. The data from the financial institution contained information about the assets, liabilities, incomes and expenditures of the institution. The objective was to identify the key assets and liabilities, differentiate them as rate sensitive and non-rate sensitive, and store them in a relational database management system. The management of the credit union assisted in the identification of assets and liabilities, and provided information to differentiate the assets and liabilities.

The data contained information about the amounts and interest rates of rate-sensitive assets and liabilities, and amounts of other assets and liabilities. The objective was to store the data in a format that would provide an easy retrieval mechanism to the application-programming interface. The structure of the tables, the description of the columns, and the identification of the primary key were the main processes involved in the storage of the data. There are four files in the system for the four quarters in a year, specifically those ending in March, June, September, and December. Each file has individual tables for the year for which the financial institution has the available data. There are three columns in a table, specifically the type of the asset or liability, amount of asset or liability, and the interest rate on the asset or liability.

The data were downloaded from the web site of the credit union as text files and stored in a local directory. The data were then imported into the Microsoft Access using the data import wizards, and making the necessary corrections at different points in the process. The irregular nature of the data and the lack of uniformity among different cycles caused the main problems in the data import process. The objective was to create a script in the decision support system that would allow the users to upload new cycles of data directly into the database. This required a drastic change in the manner in which the data are currently stored in the database of the financial institutions. The solution was to fine-tune the data import process according to the type of the institution. The information on the primary interest rate was obtained from the web site of the Federal Reserve Bank of St. Louis [5].

## 4. DSS functionality and design

The resulting decision support system is referred to as Decision Support System for Asset and Liability Management (DSSALM). It has three important components that are built separately to ensure that the required features are presented to the management. These three features are a graphical user interface, an application-programming interface, and a database management system. The primary functions of the three features and the general framework of the decision support system are described in Fig. 1.

The simulation of the primary interest rate is one of the primary functions of the decision support system. The objective of simulation is to effectively capture the historical trends in the movement of the primary interest rate in order to generate the interest rate for the future cycle of interest. This requires the identification of a function that will randomly generate the primary interest rate. The first step in this process is to provide the existing data as inputs to a simulation tool of the decision support system. The

![](/api/attachments/CPPBBU8U/fulltext/images/e2eed932635ede2e7f066edb6a08d189792836fa9d9bc81ebaacab805c452597.jpg)  
Fig. 1. System architecture.

simulation tool then generates the function to utilize in the calculation of random interest rates. The decision support system uses the ARENA simulation package to identify the function to use for simulation. This is a critical step in the process as the accuracy of the primary interest rate generated has a bearing effect on the interest rate risk.

The selected function is used by another package to generate the daily interest rates for the selected cycle of interest. The average of these values provides the system with the primary interest rate for the selected cycle. The decision support system utilizes Microsoft Excel to randomly generate the daily values of interest rates. The purpose of using Microsoft Excel is that it can be efficiently integrated with the user interfaces and database management systems.

The input data from the local financial institution contain information about the amounts of assets and liabilities for current cycles. These data are used as input to a tool that identifies the historical trends, and forecast the corresponding amounts of assets and liabilities for a future cycle of interest. The calculation of interest rate risk for a future cycle of interest is based on the amounts and interest rates of various assets and liabilities, an inherently generated risk factor, and the desired gap position of the management. The risk factor is estimated after comparing the actual results of the existing cycle with the results from the decision support system. The management is given several alternatives to select the desired gap position for the selected cycle. The amounts and interest rates of existing cycles are calculated using the methodology discussed earlier in the chapter. These values provide the input to the equation that calculates the interest rate risk of the institution for a future cycle of interest.

## 4.1. Processing considerations

The assets and liabilities of a future cycle of interest are forecast by utilizing historical trends and seasonal variations. The graphical tools provided by Microsoft Excel are utilized to identify the forecasting function, which accurately calculate the amounts of assets and liabilities. This analysis indicated that the TREND function, of Microsoft Excel, could calculate the amount of each individual asset and liability for the selected cycle of interest. The TREND function has the following syntax:

$$
\text { new\_value\_of\_y } = \text { TREND } (\text { known\_value\_of\_y },
$$

$$
\text { known\_value\_of\_ } x, \text { new\_value\_of\_ } x, \text { const })\tag{1}
$$

The function retrieves the existing values of the amounts of assets and liabilities from the database by using structured query language (SQL). The retrieved data provide the input to the TREND function. This function develops a trend line between the cycle, and the amounts of assets and liabilities in the cycle. The application-programming interface is connected to Microsoft Excel using Active X objects. The purpose of this object is to create an Excel sheet, populate the cells with the input values from the database, and trigger the TREND function. The results of the TREND function are stored in several variables, and are used on the screens displaying to the amounts of assets and liabilities.

The primary interest rate for the current cycle of interest is simulated using existing values of the primary interest rate in the database. The list of interest rates is then input to the ARENA input analyzer, which reviews different distributions and identifies the distributions with the least error in calculation. The system selected the normal distribution to generate the random interest rate for the selected cycle of interest. The function distributes the input data into a bell-shaped curve with the input values on either side of the mean of the distribution. The thickness of curve is determined by the standard deviation of the distribution. The normal distribution is widely used, as in this case, when the data appear to be symmetrical in nature. The system generates random interest rates for each day of the selected cycle of interest, and calculates the average of the interest rates to generate the primary interest rate for the cycle. The interest rates (IR) for the rate-sensitive assets and liabilities have to be calculated in order to estimate the gap position of the cycle of interest. The interest rates are related to the movement of the primary interest rate, and are calculated based on the value of the primary interest rate for the cycle of interest. Interviews with the management of the financial institution indicated that the following interest rates are calculated using these equations:

IR of unsecured credit card loans ¼ ðaverage of

$$
\text { the   primary   interest   rate   for   the   cycle) } + 7\tag{2}
$$

$$
\text { IR   of   other   real   estate   loans } = (\text { average   of   the }
$$

$$
\text { primary   interest   rate   for   the   cycle) } + 3. 4\tag{3}
$$

The interest rates on the remaining rate-sensitive assets and liabilities are calculated using the TREND function discussed earlier in this section. The primary interest rates for the existing cycle provide the known value of x array, while the values of the interest rates for the existing cycle provide the known value $\mathrm { o f \_ y }$ array. The primary interest rate for the selected cycle of interest is the new value of x. The result of the TREND function is the interest rate for the rate-sensitive asset or liability for the cycle.

The gap position of an institution is calculated using the amounts and interest rates of rate-sensitive assets and liabilities. The rate-sensitive asset gap and the ratesensitive liability gap are calculated, and the difference in the two gaps defines the gap position for the cycle of interest. The classification of assets and liabilities as rate sensitive and non-rate sensitive is a precursor to this process. The sum of interest earned on the ratesensitive assets is defined as the rate-sensitive asset gap. The following equation is used to calculate the interest earned on rate-sensitive assets [20]:

$$
\mathrm{IE} = (A I) / 1 0 0\tag{4}
$$

where: IE: interest earned on the rate-sensitive asset; A: amount of the rate-sensitive asset at the end of the requested cycle; $I ;$ interest rate on the rate-sensitive asset at the end of the requested cycle.

The value of IE is calculated for each of the ratesensitive asset of the institution. The sum of all the IE provides the system with the rate-sensitive asset gap for the institution for the selected cycle of interest. In a similar manner, the rate-sensitive liability gap of the institution is calculated. The gap position of the institution for the selected cycle of interest is calculated by using the following equation [20]:

$$
\text { Gap   position } = \text { rate   sensitive   asset   gap }
$$

$$
- \text { rate   sensitive   liability   gap }\tag{5}
$$

The risk factor of the institution is generated to determine the accuracy of the decision support system in estimating the interest rate risk. This factor is calculated when the management selects the option of comparing the results of N existing cycle. The results of an existing cycle are compared with the results of the decision support system, by reviewing the sums of assets and liabilities, the gap position, and the gap as a percentage of total assets. As discussed by Olson et al. [20], the error in each of these calculations is estimated by:

$$
\operatorname{Error} = (A - D) / A\tag{6}
$$

where: A: actual result from the database; $D \colon$ result from the decision support system.

The product of these individual errors provides the system with the risk factor to utilize in the calculation of interest rate risk. This calculation is based on the values of the desired gap position of the institution, actual gap position, and the risk factory of the institution, as noted in the following equation [20]:

$$
\mathrm{IRR} = ((D - A) / A) - \mathrm{RF}\tag{7}
$$

where: IRR: interest rate risk; A: actual gap position; $D \colon$ desired gap position; RF: risk factor.

Management’s objective is to maintain a positive interest rate risk, which would indicate that the institution would be able to achieve its desired gap position. The interest rate risk would thus be able to handle the fluctuations of the primary interest rate, and support the policies, procedures, and goals of the institution.

## 4.2. Simulation under different conditions

The objective of ‘‘what-if’’ analysis is to provide the management with different strategies to reduce or increase the interest rate risk. If the interest rate risk of the institution is negative, then the management would prefer to analyze strategies in order to obtain a positive interest rate risk. This would involve diluting the desired gap position by selecting different options for the baseline amounts of assets and liabilities, baseline interest rates, and the desired gap position. The system calculates the interest rate risk and generates a summary report for the management to assist in the selection the favorable alternative. The strategy suggested by the system would assist the management in redefining their goals for the selected cycle, and maintain the corresponding amounts of assets and liabilities.

The decision support system allows the management to analyze an existing cycle to compare the decision support system results with the actual results. These include comparison of amounts of rate-sensitive assets and liabilities, gap position, and the gap as a percentage of total assets. These allow the management to effectively plan the different strategies to utilize in the analysis of a new cycle of interest. The comparison of these values defines the risk factor to utilize in the calculation the interest rate risk of the institution.

The amounts and interest rates of various assets and liabilities are calculated using the baseline data for the cycle of interest. The gap position and the gap as a percentage of total assets are calculated using these values. The risk factor, desired gap position of the institution, and the actual gap position are utilized to calculate the interest rate risk of the institution. A sequence of these operations is depicted in Fig. 2.

![](/api/attachments/CPPBBU8U/fulltext/images/d10e0ee05ce949901bd2cc9675c4af661bd1a487113a9eec7aeff8c83a21f54a.jpg)  
Fig. 2. Sequence of system displays and operations.

## 5. Use of the system

The system stores the list of the valid usernames and passwords in the database management system. The application-programming interface transmits a query to the database and retrieves the username and password of the current user. This transaction ensures that only users authorized by the management of the financial institution are eligible to utilize the decision support system. In the next screen of the system, the user is provided with the option of either comparing the results of an existing cycle, or analyzing the interest rate risk for a future cycle of interest.

## 5.1. Comparison of existing cycle

The management of the financial institution is provided with the option of analyzing the results of existing cycles with the results from the decision support system. In the selection screen of the system, there is an option to analyze the results of an existing cycle. The list of cycles is provided in a single select list. The selection of the cycle by the management triggers a series of processes, which simultaneously calculate the amounts and interest rates on rate-sensitive assets and liabilities. The amounts of rate-sensitive assets and liabilities are forecasted with the data from the existing cycles using the TREND function of Microsoft Excel. The primary interest rate is randomly generated and the various interest rates on rate-sensitive assets and liabilities are calculated utilizing the existing relationships.

![](/api/attachments/CPPBBU8U/fulltext/images/92385079575f1d8ccd8661bbda24e50572b329c039cce8c9915be60f5efea49f.jpg)  
Fig. 3. Comparison of existing cycle results.

The gap position is calculated using the amounts and interest rates on rate-sensitive assets and liabilities. The system generates a summary report that compares the results of the decision support system with the actual results. The objective of this report is to assist the management in evaluating the accuracy of the decision support system in effectively calculating the interest rate risk. The summary report screen is displayed in Fig. 3.

## 5.2. Evaluation of a new cycle

The evaluation of a new cycle is the primary feature of the decision support system. The user selects a cycle of interest and the mechanism to generate the baseline amounts and interest rates on assets and liabilities. The various options provided in the selection of baseline amounts of assets and liabilities, and the baseline interest rates are displayed in Fig. 4.

The baseline amounts of assets and liabilities can be generated by three different mechanisms in the system. The historical data are used to develop a function that can forecast the amounts of asset and liabilities for a selected cycle of interest. In addition, the user is provided with the option of selecting the baseline amounts from an existing cycle or selecting the latest available data. The interest rates on the ratesensitive assets and liabilities are generated by one of the three mechanisms selected by the user. The user can select a randomly generated interest rate, interest rate from an existing cycle, or the latest available interest rate.

![](/api/attachments/CPPBBU8U/fulltext/images/bc4248f2856cc90c8de63d651756764287310ab457253c659acb6dc716db7248.jpg)  
Fig. 4. Baseline data options.

For example, assume that the user has selected a randomly generated primary interest rate for the cycle June 2000. The baseline interest rates of the ratesensitive assets for the selected cycle are displayed in Table 1. The baseline interest rates of the rate-sensitive liabilities for the selected cycle are displayed in Table 2. The user is then provided with the option of selecting a desired gap position for the cycle June 2000. The desired gap position can be forecast from existing values of gap positions, derived from the gap position of any cycle, or the user can specify the desired gap position by inputting the value to the system. In the current example, the user has selected US\$7,000,000 as the desired gap position for the cycle June 2000. The decision support system uses the various inputs to calculate the actual gap position for the cycle of interest and calculates the interest rate risk based on the values of the desired gap position, actual gap position, and the risk factor in the system. The various outputs of the system for the selected cycle of interest are displayed in Table 3.

The difference between the desired and actual gap position is the reflection of the changing market environments and the volatile nature of the primary interest rate. The interest rate risk is calculated on the basis of this difference and the addition of a risk factor, which is inherently calculated by the system. The results of the analysis of the cycle June 2000 are displayed in Fig. 5.

Table 1  
Baseline interest rates of rate-sensitive assets

<table><tr><td></td><td>Decision support system</td><td>User override amount</td></tr><tr><td>Unsecured credit card loans</td><td>12.8</td><td>12.75</td></tr><tr><td>All other unsecured credit loans</td><td>12.64</td><td>-</td></tr><tr><td>New vehicle loans</td><td>8.72</td><td>-</td></tr><tr><td>Used vehicle loans</td><td>10.12</td><td>-</td></tr><tr><td>Total first mortgage real estate loans</td><td>9.36</td><td>-</td></tr><tr><td>Total other real estate loans</td><td>9.58</td><td>9.59</td></tr><tr><td>Total all other loans to members</td><td>8.56</td><td>-</td></tr><tr><td>Total other loans</td><td>0</td><td>-</td></tr></table>

Table 2  
Baseline interest rates of rate-sensitive liabilities

<table><tr><td></td><td>Decision support system</td><td>User override amount</td></tr><tr><td>Share drafts</td><td>0</td><td>-</td></tr><tr><td>Regular shares</td><td>3.97</td><td>4</td></tr><tr><td>Money market shares</td><td>4.87</td><td>-</td></tr><tr><td>Share certificates with 1 year maturity</td><td>6.29</td><td>-</td></tr><tr><td>IRA/KEOGH and retirement accounts</td><td>6.48</td><td>6.5</td></tr><tr><td>Non-member deposits</td><td>0</td><td>-</td></tr></table>

A positive value of interest rate risk reflects that the management will be able to meet the desired gap position in the current environment. A negative value reflects that the management would not be able to achieve the desired gap position. Typically, the objective would be to have a large value of positive interest rate risk in order to accommodate for the various trends in the market. The inputs and outputs for the analysis of a new cycle generate a report similar to the one displayed in Table 4.

The ‘‘what-if’’ analysis feature of the decision support system may then be applied. The management can analyze different alternatives that will give them a high value of interest rate risk. If the current interest rate risk is negative, then the minimum objective will be to reduce the risk and obtain a non-negative value of risk. Alternatives that may be considered, include:

1. Change the mechanism to generate the baseline amounts of assets and liabilities

2. Change the mechanism to generate the baseline interest rate of rate-sensitive assets and liabilities

Table 3

<table><tr><td colspan="2">Outputs for the cycle June 2000</td></tr><tr><td>Desired gap position</td><td>7,000,000</td></tr><tr><td>Actual gap position</td><td>8,148,317</td></tr><tr><td>Gap as a percentage of total assets</td><td>2.08</td></tr><tr><td>Interest rate risk</td><td>0.16</td></tr></table>

![](/api/attachments/CPPBBU8U/fulltext/images/5465c28d824863bc072a5ba80b22a126c4d3027200491d6f32172507cf2e676f.jpg)  
Fig. 5. Outputs for the cycle June 2000.

3. Define a different desired gap position for the cycle of interest

4. Select any combination of the above options.

## 6. Verification and validation

According to Laudon and Laudon [13], two approaches can be distinguished for the verification of any expert system. The first approach considers the system as a whole, while the second focuses on separate verification of each component. Since DS-SALM is modular in design, it requires a combination of the two approaches. This architecture implies that the performance of each separate module be verified individually, with subsequent verification of the integrated whole.

Traditional software engineering techniques, that is, using a set of predetermined tests, were used to verify the integrity of the individual modules. Variations on these structured tests, as identified by Kroenke and Hatch [12], were applied. A series of unit, module, and system tests was successfully completed using both actual and contrived data. The verification process ensured that the system performed the functions identified in the design specifications. Expected functionality was usually observed through the predetermined set of test cases. Upon detection of any errors, a structured problem resolution procedure was conducted. This included a methodical process for problem description, evaluation, resolution, and retest [13].

The validation process established that the system’s functionality would address the original business problem and the financial analyst’s needs. Face validation by three domain experts, as well as a predictive validation using case studies from the literature, were conducted successfully in accordance with the procedures described by Laudon and Laudon [13].

## 7. Planned integration of the prototype system

The prototype DSS is viewed as an initial iteration in solving bank’s requirements for asset and liability management. The prototype was developed as a stand-alone system. Further benefit would be derived by integrating the DSS with the bank’s other existing files and external systems. For example, the system currently stores input data in the user’s local directories. It is recommended to run the database management system on a server in the local area network of the institution. This would broaden the user base. The decision support system currently does not support the automatic uploading of data from new cycle into the database management system. The irregular format of the existing data was the primary reason for the rejection of the feature. Integration of the DSS into the bank’s information architecture would standardize the format of data for the future cycles, and allow upload of the most current data.

Table 4  
New cycle analysis report

<table><tr><td>Name of asset/liability</td><td>Amount (US$)</td><td>Interest rate (%)</td></tr><tr><td colspan="3">Rate-sensitive assets</td></tr><tr><td>Unsecured credit card loans</td><td>5,000,000</td><td>12.64</td></tr><tr><td>All other unsecured loans</td><td>15,978,997</td><td>8.72</td></tr><tr><td>New vehicle loans</td><td>3,718,622</td><td>10.12</td></tr><tr><td>Used vehicle loans</td><td>10,000,000</td><td>9.36</td></tr><tr><td>Total first mortgage real estate loans</td><td>14,447,420</td><td>9.59</td></tr><tr><td>Total other real estate loans</td><td>1,498,900</td><td>8.56</td></tr><tr><td>Total all other loans to members</td><td>10,000</td><td>0</td></tr><tr><td>Total other loans (purchased/non-members)</td><td>0</td><td>0</td></tr><tr><td colspan="3">Rate-sensitive liabilities</td></tr><tr><td>Share drafts</td><td>17,726,875</td><td>4</td></tr><tr><td>Regular shares</td><td>20,964,732</td><td>4.87</td></tr><tr><td>Money market shares with minimum balance requirement, withdrawal limitations, and no fixed maturity</td><td>13,419,894</td><td>6.29</td></tr><tr><td>Share certificates with 1 year maturity</td><td>5,316,662</td><td>6.5</td></tr><tr><td>IRA/KEOGH and retirement accounts</td><td>1000</td><td>0</td></tr><tr><td>Non-member deposits</td><td>0</td><td>0</td></tr><tr><td colspan="3">Other assets</td></tr><tr><td>U.S. government obligations</td><td>18,896,457</td><td></td></tr><tr><td>Federal agency securities</td><td>0</td><td></td></tr><tr><td>Mutual funds and common trust investments</td><td>10,000</td><td></td></tr><tr><td>Credit unions—deposits in and loans to</td><td>50,000</td><td></td></tr><tr><td>Other investments</td><td>3,171,024</td><td></td></tr><tr><td>Cash and cash equivalents</td><td>5,876,605</td><td></td></tr><tr><td>Corporate credit unions</td><td>10,000</td><td></td></tr><tr><td>Commercial banks, S&amp;Ls, mutual saving banks</td><td>703,256</td><td></td></tr><tr><td>NCUA share insurance capitalization deposit</td><td>698,857</td><td></td></tr><tr><td>Land and building</td><td>300,000</td><td></td></tr><tr><td>Other fixed assets</td><td>200,000</td><td></td></tr><tr><td>Other real estate owned</td><td>945,735</td><td></td></tr><tr><td>Other assets</td><td>0</td><td></td></tr><tr><td colspan="3">Other liabilities</td></tr><tr><td>Total borrowings</td><td>19,307</td><td></td></tr><tr><td>Accrued dividends/interest payable on shares/deposits</td><td>441,835</td><td></td></tr><tr><td>Accounts payable and other liabilities</td><td>5,425,798</td><td></td></tr><tr><td>Share certificates</td><td>0</td><td></td></tr><tr><td>All other shares</td><td>3,386,480</td><td></td></tr></table>

Table 4 (continued )

<table><tr><td>Name of asset/liability</td><td>Amount (US$)</td><td>Interest rate (%)</td></tr><tr><td>Regular reserves</td><td>0</td><td></td></tr><tr><td>Uninsured secondary capital(low-income designated credit unions only)</td><td>0</td><td></td></tr><tr><td>Investment valuation reserve</td><td>-181,047</td><td></td></tr><tr><td>Accumulated unrealized gains(losses) on for sale securities</td><td>0</td><td></td></tr><tr><td>Other reserves</td><td>7,778,091</td><td></td></tr><tr><td>Undivided earnings</td><td>0</td><td></td></tr><tr><td>Net income</td><td>0</td><td></td></tr><tr><td>Gap position</td><td>2,456,452</td><td></td></tr><tr><td>Gap as a percentageof total assets</td><td>2.885037</td><td></td></tr><tr><td>Interest rate risk</td><td>-0.64</td><td></td></tr></table>

The system could also be converted from a standalone application to a web-based application using HTML-software. The application could be incorporated in the institution’s website allowing the management to access the system from different locations. The maintenance of such an application then could be conducted from a single source, which would reduce the software problems and increase the speed and reliability of the system. With the increase in Internet technology and number of users, the conversion to a web-based application would be beneficial to the institution.

## 8. Conclusions

Current trends in the management of financial institutions emphasize the need for an improved means of decision support. As noted in the literature, a fundamental limitation of earlier asset and liability management systems was an inadequate use of historical data for forecasting purposes. The resulting gap position was a static measure, not reflecting the volatile nature of the primary interest rate as well as its impact on the calculation of interest rate risk.

The DSS discussed in this paper provides an improved proof-of-concept approach to asset and liability management that would meet the desired requirements. The scope of the research was limited into developing a comprehensive prototype of the system, which was validated by experts in the area of financial management. DSSALM will calculate the interest rate risk for 20 cycles from the current cycle. This risk is calculated on the basis of historical data available from a relational database. The data provide the input to the forecasting functions, and project the levels of assets and liabilities. DSSALM also calculates a dynamic gap position based on a random value of interest rates. The system will neither determine the effects of hedging, nor the effects of manipulation of financial instruments like derivatives.

The system is currently useful for credit unions, and the capabilities of the system could be extended to other financial institutions. The alternatives provided in the ‘‘what-if’’ analysis are sufficient to generate different scenarios in changing market environments. DSSALM introduces a relatively new concept referred to as the risk factor of the institution. This factor is an estimate of the accuracy of the system in generating the gap position and interest rate risk for a future cycle. DSSALM provides the option of comparing the results of existing cycles with the system’s calculations. The difference between the two values is used to calculate the risk factor of the system. The risk factor is then adjusted in the calculation of the interest risk for a future cycle.

Further research is necessary to enhance the capabilities of DSSALM. The system currently forecasts the amount of assets and liabilities based on a TREND function. The input data strongly suggested a seasonal trend in the amounts of assets and liabilities. The system should periodically analyze the input data to determine if there is a change in the trend. The DSSALM could also provide the user with the option of changing the forecasting function for different assets and liabilities. The feedback from the validators also suggested that the addition of a feature to replicate similar environments as past cycles would improve the performance of the system. The assumption in this feature is that the management frequently encounters familiar situations, and the solutions utilized in the past could be used effectively for the present situation.

## References

[1] ALMIS, Balance Sheet Management: A Structured Solution, http://www.almis.co.uk/home.htm (04/05/98).

[2] J.W. Bitner, R.A. Goddard, Successful Bank Asset/Liability Management, Wiley, New York, 1992.

[3] F.J. Fabozzi, K. Atsuo, Asset/Liability Management, Probus Publishing, Chicago, 1991.

[4] Farin and Associates, SAM—A Planning Tool, http://www. farin.com/sam<sub></sub>cpt.htm (02/05/98).

[5] Federal Reserve Bank of St. Louis, FRED: Federal Reserve Economic Data, http://www.stls.frb.org/fred/index.html (12/ 20/97).

[6] D.R. Fraser, B.E. Gup, J.W. Kolari, Commercial Banking: The Management of Risk, West Publishing, Minneapolis/St. Paul, 1996.

[7] B.E. Gup, R. Brooks, Interest Rate Risk Management, Irwin Professional Publishing, Burr Ridge, 1993.

[8] J. Haynes, The use and abuse of simulation models, in: J. Whitley (Ed.), The ALCO. Strategic Issues in Asset/Liability Management, Macmillan, New York, 1992.

[9] IBM and RADAR RiskManager, What makes the RADAR System special? http://www.rmtech.com/prodinfo/ibm-uk/ ibm-main2.htm (02/06/98).

[10] W. Joubert, Duration Analysis, RiskFlow Technologies, http:// www.riskflow.com/Refs/AlUp01.htm (10/22/98).

[11] R. Kouwenberg, Asset and liability management for pension funds: elements of Dert’s model, in: C. Zopoundis (Ed.), New Operational Approaches for Financial Modelling, Physica Verlag: New York, pp. 37–48.

[12] D. Kroenke, R. Hatch, Management Information Systems, 3rd edn., McGraw-Hill, New York, 1994.

[13] K. Laudon, J. Laudon, Management Information Systems: New Approaches to Organization and Technology, 5th edn., Prentice Hall, Englewood Cliffs, NJ, 1998.

[14] Liberty Advisors, ALM Guide: Gap Analysis, http://www.libertyadvisors.com/almgap.htm (02/08/98).

[15] Liberty Advisors, Duration Analysis, http://www.libertyadvisors.com/almdurat.htm (02/08/98).

[16] Logica News, Press Release: Logica Asset/Liability Management and Financial Planning Software draws 25 new clients in Spain, http://www.logica.com/news/press/pr163.html (02/05/ 98).

[17] D. Mare, J. Vong, Systematic Risk, Systematic Solutions, Nanyang Business School, Singapore; SPL WorldGroup Banking Division, Singapore, http://aseanbusiness.com/ibjm<sub></sub>rs.htm (04/05/98).

[18] J. Mason, Financial Management of Commercial Banks, Warren, Gorham, and Lamont, Boston, 1979.

[19] R.L. Olson, H.M. Sollenberger, W.E. O’Connell Jr., Financial Planning for Credit Unions, Ivy Press, Greenbelt, 1990.

[20] R.L. Olson, H. Sollendberger, W. O’Connell, Financial Planning for Credit Unions, Ivy Press, Greenbelt, 1990.

[21] R.W. Payant, Maximizing Bank Value: Asset/Liability Management in the 1990’s, Bankers Publishing, Rolling Meadows, 1989.

[22] RiskFlow Technologies, ALMAN: RiskFlow’s Asset and Liability Manager, http://www.riskflow.com/Alman.htm (06/22/ 98).

[23] J. Sagerstrom, G. Meadows, Why gap doesn’t work, ABA Banking Journal, 44–50 (October).

[24] D. Simonson, G. Hempel, Improving gap management as a technique for controlling interest rate risk, Journal of Bank Research (Summer), pp. 109–115.

[25] P. Styger, What should the Board of Directors know about Asset and Liability Management? http://www.riskflow.com/ Refs/AlUp11.htm (03/07/98).

[26] D.G. Uyemura, D.R. Van Deventer, Financial Risk Management in Banking, Bankers Publishing; Probus Publishing (Chicago, 1993).

[27] Young and Associates, Beyond Gap — Asset/Liability Management in the 1990s, http://www.younginc.com/90dn<sub></sub>8<sub></sub>96<sub></sub> alm.html (10/12/97).

![](/api/attachments/CPPBBU8U/fulltext/images/59f53ab2055777ab1159252b1ddfa695c574821c93a9eb64cca507f6976f0d99.jpg)

Gary P. Moynihan is a professor in the Department of Industrial Engineering, the University of Alabama. He received BS and MBA degrees from Rensselaer Polytechnic Institute, and a PhD from the University of Central Florida. His primary area of specialization is the development of expert systems and decision support systems. Prior to joining the faculty of the University of Alabama, Dr. Moynihan held positions in the aero-

space, computer, and chemical processing industries.

![](/api/attachments/CPPBBU8U/fulltext/images/a504d3ff2b21f21fc5eaee5fc0444037e7a6318f53903ffda87984bc1a6e9b89.jpg)  
Prasad Purushothaman obtained his MSIE degree from the University of Alabama in 1999. He is currently employed by KPMG Consulting, Inc. He received his BS degree from the University of Delhi, India.

![](/api/attachments/CPPBBU8U/fulltext/images/ef6e9dce7eebff2222e200bd937cad60209782aa9f20deb372ea494266261202.jpg)

Robert W. McLeod is a professor of finance and Executive Director of MBA Programs at the University of Alabama. He received BSBA and MBA degrees from the University of Southern Mississippi, and a PhD from the University of Texas-Austin. Dr. McLeod holds the professional designations of Chartered Financial Analyst (CFA), Certified Financial Planner (CFP), and Chartered Life Underwriter (CLU). His specialty

areas include financial institutions and markets, personal financial planning and investing, valuation analysis, and company analysis. He is a past president of the Academy of Financial Services.

![](/api/attachments/CPPBBU8U/fulltext/images/73d8773cf548623e34e96927c6550e88fc90622caa96e4d858918a456d8dac07.jpg)

The late William G. Nichols was an associate professor and interim head of the Department of Industrial Engineering, the University of Alabama. He received BA and MS degrees in Mathematics from the University of Rhode Island, and MS and PhD degrees in Statistics from Virginia Polytechnic Institute and State University. His main areas of research included stochastic theory and computer applications.
