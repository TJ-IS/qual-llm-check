---
otero_id: 10584
otero_key: "AJ36DJG4"
title: "Design and implementation of a decision support system for competitive electricity markets"
authors: "Julia Sancho; Joaquín Sánchez-Soriano; Juan Antonio Chazarra; Juan Aparicio"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.09.008"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Design and implementation of a decision support system for competitive electricity markets ☆

Julia Sancho, Joaquín Sánchez-Soriano, Juan Antonio Chazarra, Juan Aparicio

Operations Research Center, University Miguel Hernández of Elche, Av. universidad s/n, Elche 03202, Spain

Received 21 December 2006; received in revised form 20 September 2007; accepted 30 September 2007 Available online 12 October 2007

## Abstract

In this paper we describe software which could be used as a decision support tool for decision makers in competitive electricity markets. The tool is based on the behavior of the competitors in the market, thus many different parameters around them are considered and, additionally, many different scenarios can be used. The possible results are obtained by simulation. Two modes are implemented; one to simulate the functioning of a competitive electricity market and the other, called manual, to evaluate the success of particular strategies by a user. Finally, some computational experience is reported to validate the simulation model. © 2007 Elsevier B.V. All rights reserved.

Keywords: Competitive electricity markets; Simulation model; Spot prices

## 1. Introduction

The organization of the electricity industry at international level has undergone significant changes since the beginning of the 1990's at a pace unprecedented during its history. Coinciding with this process, the researchers interest in the development of models adapted to these new circumstances, has given rise to numerous publications [8], [19] and [27], and more recently [13], [18] and [23].

Our interest focuses on the strategic behavior of the companies which compete in the electricity market. One of the main lines of research open in this field, consists of what kind of tender is more advisable in the electricity markets: uniform or discriminatory. In the literature there are several works which tackle this problem. In the general context, it cannot be guaranteed that one bid may be preferred to another (see [2] and [7]). In multiple objective tenders the comparison between both tenders is complex and there is no clear evidence to show that the discriminatory is better than the uniform tender.

Another of the debates which are latent in the electricity market environment is whether to use a discrete model of multiple objectives tender or a continuous offer model (this subject is dealt with in depth in [16]). In this article, the discrete model is considered to be more appropriate to reflect the reality of the electricity markets, whereas in other works such as [3–5], [15] and [20] it is argued that the most appropriate way of describing the strategic behavior of companies, which are part of electricity market, is the continuous tender model. The two approaches take the costs of known competitor companies, that is the electricity market tenders are modelled by juggling with complete information. In fact, this supposition is too restrictive, although electricity generating companies know each other very well and when the production costs of other competitors have to be decided, many factors which cannot be known exactly come into play. For example, a company may have purchased oil reserves years ago and not applied them directly to present tenders.

The main aim of our work is to simulate how the competitive electricity market functions by means of simple offers in the daily market. We offer a computer application which models the short term behavior of energy sales agents which are present in the markets and submit information on the main interest variables, as for example: the market price exercised by the different power stations, the spot price for energy, the generated output of each station, the profits obtained and the probability that each type of technology could fix the spot price.

In any case, the majority of theoretical models are based on the formal definition of equilibrium (see [6] and [12]), which is expressed mathematically in the form of algebraic equation systems and/or differentials difficult to solve, and to this is added a further complication, which is the representation of the competition between the participants in the electricity markets. These two factors on many occasions distance the models from reality and the solution of the same leads to equations, where if there is a solution, is very difficult to find. Simulation models are an alternative to models based on equilibrium, when the resulting problem is very difficult to solve and does not have an analytical solution. On many occasions simulation models are closely related to theoretical model families [4], [14] and [17]. For example, the simulation models where the participants base their strategies on the quantity of energy make a clear reference to the Cournot model [27], [28]. Some authors have simulated the energy market following the theoretical models of market equilibrium according to continuous supply [14], which have the advantage of being less restrictive than the theoretical models. In [28] the authors show an extensive revision of the models, both theoretical and applied, and simulation models which have been applied to the electricity energy markets. In all these models there are limitations, such as the competitors being symmetrical, the marginal cost functions are known and identical for all the players, the supply functions are continuous and the same and the production capacity of each generator is unlimited. Not all the restrictions occur at the same time in existing models, but there is no model which resolves all these matters at the same time.

Given that there are limitations which we find in a field as complex as the electricity markets and the great difficulty involved in analytically resolving a model with numerous competitors, unknown and asymmetrical costs, discrete and different functions for the offer of the sale of energy for each generator, we think that to be able to solve this problem, the best solution was to provide a computer tool capable of reproducing the supply which energy generators produce every day in the energy market and reproduce the steps which the Market Operator takes on receipt of these offers. We can find an example of this approach in [26], where an opensource agent-based framework is designed to analyze the Wholesale Power Market Platform (WPMP) in USA. We can find another example of this approach in [25]. In our paper, the application developed allows the simulation of any electricity energy market, but the Spanish daily electricity energy market has been used as a reference, as it is the operator which offers most information to the public on its web [11]. OMEL publishes daily information on the spot price and hourly demand, the power stations which fix the spot price, the curves of aggregated supply and demand, the offers made by each power station with a delay of three months, the market quotations for each company etc. All this information (see so [1,9,10,21,22,24]) helped to define the input of information into the system, to check in the adjustment phase that the simulator reflects accurately the behavior of the electricity energy markets.

The rest of the paper is structured as follows. In Section 2 we present a brief description of the Spanish electricity market. Section 3 deals with the fundamentals and development of the Decision Support System (DSS) for competitive electricity markets. In Section 4 we report the results provided by the DSS-tool. In Section 5 we present some computational experience to check functioning at the DSS-tool. Finally, in Section 6 we provide some conclusions.

## 2. Brief description of the Spanish electricity market

Since the 1990's many countries (Argentina, Australia, Canada, Chile, Columbia, the United States, Spain, Peru, Sweden, and the United Kingdom, among others) have made changes in their electricity sectors with the aim of improving their efficiency by means of deregulation. In Spain, the electricity market came into being on 1st January 1998. The main objective of the deregulation of the electricity market in Spain was to increase the efficiency of the sector by introducing competition into the activities of generating and marketing electricity. The electricity generating production market comprises both the marketing transactions of the buying and selling of energy and other complementary services related to the supply of electric energy, essential to ensure the right conditions of safety and quality. The operation of the national electricity system is entrusted to two independent but interactive bodies, which are the market operator and the (transmission) system operator. The financial management of the electricity system is handled by the Operating Company of the Spanish Electricity Market, S.A. OMEL, which is responsible for the management of the daily markets.

## 2.1. The daily electricity energy market

The daily market, as an integral part of the electricity energy production market, has the objective of carrying out the transactions of electric energy for the day following the presentation of the offers to sell and purchase energy by the market agents. The contracting sessions of the daily markets are organized into programming periods equivalent to one hour, taking the programming limit as being 24 periods (hours) of the following day. The basic elements which form part of the daily market transactions of electricity energy are: the agents who wish to buy or sell energy, the offers made by these agents, the process of matching the offers and the price of electricity for each period, called the spot price. As follows, each of these elements is described in detail.

## 2.1.1. The market agents

The market agents are the companies authorized to intervene directly in the electricity market as buyers and sellers of electricity. The electricity generators (producers, special category, external seller) make their offers to sell into the market, while the buyers (distributors, marketing organizations, consumers, external buyer) make their offers to purchase in the market. The market operating company intervenes in the matching of the offer with the demand.

The electric energy production plants are each thermal group, each pumping station and each hydraulic or wind-powered plant. As a result of the liberalization of the electricity sector, there has been a growth in production plants, especially in combined cycle stations where the raw material is gas. Another technology undergoing rapid development is wind-powered energy.

## 2.1.2. The offers to buy and sell energy in the daily market

The offers to buy and sell energy can be made considering from 1 to 25 energy blocks in each hour, in each one of which a pair energy-price is offered. In the case where it is an offer to sell, the energy and the price are non-decreasing in each block, and will be decreasing in each block of the offers to buy. The offers to sell can be simple or complex. The simple offers are those where the sellers present their offers without any kind of constraint, either economic or technical. The offers which include complex sales conditions are those which, whilst fulfilling the requirements demanded for the simple offers, include in addition some technical or economic constraint.

## 2.1.3. The matching process of sales and purchase offers in the daily market

OMEL carries out the matching of the offers for sale and purchase of electric energy received before 10 o'clock the day prior to the supply and the procedure is a closed method (i.e. does not permit more than one turn). First a simple valid solution is obtained and then OMEL proceeds to explore the combination of complex offers which improve it, finally determining the marginal price for each hour, the quantities adjudicated for each offer for sale and acquisition and the order of economic preference.

The price of each hourly period will be equal to the price of the last block of the sale offer of the last production unit whose acceptance has been necessary to meet the demand that has been matched. This is usually referred to as ‘spot’ or ‘marginal’ price. That is, it is the point where the aggregated offer curve (the sum of the demands of all the sellers of electric energy) and the aggregated demand curve (the sum of the offers of all the buyers of electric energy) cross.

## 3. Fundamentals and development of the Decisions Support System for competitive electricity markets

Based on the description of the electric energy markets, we have tried to reflect the reality of the generators' offers and carry out the matching of these offers. In most electricity markets, the demand is inelastic with regard to the price. In addition, as it is an essential commodity, it makes the consumption of energy relatively simple to estimate, which is why an approximation of the problem directed at the offers of the sale of energy has been carried out. It should be noted that in the application which has been implemented, it is possible to introduce a module similar to the offers of the sale of energy for the offers of purchase of energy, so that it is possible to simulate in the same way an electric energy market with offers to sell and to buy. But owing to the large amount of information which needs to be added to the system and as at the present time the offers to buy do not influence directly the final price of energy, we have opted to consider the demand as a known parameter and inelastic to the price.

Below, the main fundamentals are described and the flow chart of the computer application SIMEL 1.5 (SIMULATOR OF ELECTRICITY MARKETS).

## 3.1. General outline of application

Taking into account the technology used by the power stations which participate in the electricity markets, the variability in price and hourly demand over a period of time and climatic factors, a series of scenarios which will establish the input of information into the system, have been defined. Once all the input necessary to start off has been introduced, which constitutes the initial working conditions, the implementation cycle is the following:

1. Warm-up period. If the market operator publishes the offers which the power stations bring to the markets with a certain delay (three months in Spain), the system allows us to use this information to estimate the offers which the generators make during that delay. In another case, if the market operator does not publish the offers, the valuations which each competitor has for the rest of the power stations will be taken. The objective of this warm-up period is to update the system with the information which the market operator does not publish from the delay to the period which we wish to simulate, given that the spot price for this period of time is known.

![](/api/attachments/AJ36DJG4/fulltext/images/6e01c982fc4e6bcdac6695bf0bdea7b9b2ed943c0c5d226931432b9f037b38fb.jpg)  
Fig. 1. the flow chart which represents the operating model of the application described.

2. Updating. The offers which each power station submits to the market for each hour of the day, are discrete functions of quantity/price of energy, where the price is defined according to certain parameters. These are updated in the system both in the warm-up period and during the period simulated daily, that is, once the prices are simulated in each function of hourly offer for one day, before simulating the following day, all the parameters are updated.

3. Calculation of the offers to sell. When the parameters which define the prices in each stage of an offer have been updated, a price for each stage is obtained by means of simulation and a quantity of energy is assigned to each price. Each price in a particular stage is directly related to the price of the stage immediately before. And the maximum price of an offer is directly related to the spot price of the previous period. In this way, for each one of the power stations which participate in the electricity energy market, an offer of sale of energy (pricequantity) for every hour is obtained.

4. Calculation of the spot price (matching). By means of this process the spot price for each hour is obtained and which power stations are selling energy, through the matching of the supply and demand. This process is regulated in the markets by the market operator.

5. The first 4 steps (warm-up period, updating, calculation of the offers to sell and matching) are repeated ns times for the first day, as pointed out at the beginning of the operation, according to the number of simulations.

6. The average values of all the parameters associated with the simulated day, random variables (r.v.), spot prices, offers, profits, etc. are calculated.

7. Once the first day of the simulation has been calculated and the estimated spot price obtained, it is possible to calculate the following day and so on and so forth. That is why all the previous steps (except the warm-up period) are repeated as many times as may be required in the number of days to be simulated.

8. Presentation of the results.

Fig. 1 shows the flow chart which represents the operating model of the application described.

We should also like to describe the aspect of the software developed. The main advantage is the clarity with which the different parameters which intervene in the development of the electricity markets are dealt with, and also its easy use. The software consists of a graphic interface through which the user can introduce all the types of parameters and scenarios necessary to carry out a simulation of the behavior of the Electricity Market.

This consists of a compact window in which the following fundamental parts with very different characteristics appear (they will be gone into in detail later): simulation scenarios, power station profiles and warmup period. The main application window is shown in Fig. 2.

## 3.2. Scenario definition

In general, the different situations (or scenarios) will be defined, representing the various conditions of competence which can appear in an electric energy market.

• Wet, dry or very dry period. In some electricity markets there is a heavy dependence on hydroelectric power stations, this situation is shown by the quantity of water in reservoirs and therefore, in the offers made by generating companies to the market. A good example of this situation is the Spanish market. On analysis of the hourly spot price in this market, we find that the average price during a very dry period is double that of a wet period. That is why with regard to the water in reservoirs, the three periods of wet, dry and very dry have been taken. Note that in markets which are not affected in this way, one single period is always defined.

• Working days and public holidays. Another important factor at the time of defining the various electricity market scenario, is the kind of day to be simulated. As can be expected, on working days more energy is needed than on holidays, this change in energy consumption makes the average spot price in the energy market different in each situation.

Time changes. Over the 24 h in a day, variations occur in the demand for energy in the market which also causes changes in the average spot price per hour. Therefore, the following hourly phases are taken: peak hours are those when the greatest demand for electric energy takes place. Off-peak hours are those when least demand for electric energy occurs. Transition hours are the times of transition between an off-peak and a peak or vice versa. This structure occurs in most of the electricity markets (see [29]). We will take here 7 phases, aggregating the 24 h of the day. Based on the information from OMEL for the Spanish electricity market we consider 2 peak phases, 2 off-peak phases and 3 transition phases.

In general, 42 different scenarios are described (3 (weather conditions) × 2 (working days and public holidays) × 7 (time changes)), denoted by $J { = } 1 , { \ldots } , 4 2$

![](/api/attachments/AJ36DJG4/fulltext/images/f78af590295e15dfd2f787084822a20cf69b4608993de3334bb08bdab7a74e4d.jpg)  
Fig. 2. The main application window.

The reduction in the hourly variation is made for the convenience of the user, and also to reduce the simulation time, but the software can simulate the 24 h in a day independently (Time changes = 24) and in this case 144 (3 × 2 × 24) possible scenarios are obtained.

In the computer application (simulation scenarios) in the first module the scenarios are specified and it is where the user specifies: the period of time to be simulated; the demand for electric energy for each one of the periods to be simulated (the application allows the demand data to be introduced manually into a template which is provided with the software, or if there is already a file with this information, to include it); the climatic conditions, whether they are very dry, dry or wet, according to the water held in reservoirs during the period of simulation; bid options, the programme allows us to choose between a uniform or discriminatory bid, and finally, the number of simulations to be carried out.

## 3.3. Demand for electric energy

The main objective of the electricity market simulator is to provide a tool to the electricity generating companies for them to be able to make their offers for sale on the actual day for each one of the 24 h of the following day. To do this, another entry which we should provide in the system is the demand for energy required for each hour of the day to be simulated. Because electric energy is an essential commodity and, in addition, at the present time in some markets the consumers can acquire their energy with tariffs fixed by the State without need to go to the market to make offers to buy, the demand is practically inelastic with regard to the price (see the transmission system operator web [24]). Nowadays, the existing methods used to estimate the demand are powerful enough to be able to predict very reliably what may happen the following day. A large variety of methods are used for demand forecasting. They may be classified into two broad categories (see [29]): statistical approaches (exponential smoothing, regression and time series methods) and artificial intelligence-based techniques (neural networks and fuzzy logic). That is why in our system it is assumed that the market demand for each hour is a known parameter, where the electric energy generators compete through offers of quantity/price to supply this demand.

## 3.4. Definition of the power station profiles

One of the most potent factors of the simulator is the fact of being able to consider the different technologies for electric energy generating with different cost functions (asymmetric competitors). In addition to the cost functions, the idea of incomplete information is introduced. As stated previously, the companies which compete in the market have only approximate information about their competitors' production costs. It can be said that this information is vague or at least not very accurate. For this situation to be reflected in the system, uncertainty is introduced into the parameters which define each of the production cost functions by means of fuzzy numbers. These are entries into the system which the system user has to specify.

At present, there are basically three types of different technologies which compete in the competitive electricity markets, usually all the companies possess the three kinds of technologies which are the following:

1. Conventional thermal. In general, this kind of technology has square-root production costs. When they begin to produce, for small increases in the production units, large variations in cost are produced, while as they approach their maximum capacity, the cost eases off and stays constant when maximum production is reached. The production cost function is the sum of the fixed costs (CFT) plus the variable costs, these being considered as the form $\mathbf { C V T } = \alpha { \sqrt { e } }$ where α is a fuzzy number and e is the quantity of energy produced.

2. Hydroelectric. In general, these generation plants do not have production costs, but their maintenance costs are fixed (CFH) whether they produce energy or not, but depend on the raw material available to produce energy, the accumulated and future water in the reservoirs.

3. Combined cycle. At present, this kind of technology is in a stage of full development and has as the main advantages that it is not dependent on nature as is hydroelectric and is more flexible at the time of production than thermal, its production costs are linear. That is, the marginal cost is constant, i.e., independently of the quantity produced, the costs increase in the same way, whether we are close to the maximum generation or not. The production cost function is the sum of the fixed costs (CFCC) plus the variable costs, these being in the form CVCC be where β and $\gamma$ are fuzzy numbers and e is the quantity of energy produced.

![](/api/attachments/AJ36DJG4/fulltext/images/c394a781b667b5d7907363996e5d271ae2655d67a8a672d230399327e49392e3.jpg)  
Fig. 3. The main screen of SIMEL is shown to define the power station profiles.

On the other hand, nowadays the use of technologies which take advantage of natural resources is increasing, giving rise to a boom in the introduction of windpowered stations. In general, as with hydroelectricity, these power stations do not have production costs, but their costs are decided by maintenance, whether they produce energy or not, but depend on the raw material available to produce energy, in this case the wind and the future weather forecast.

All the participants in the daily electricity markets are obliged to offer all the units of electric energy which they have available every hour. This condition implies that the offer of each generator has to be everything that is available at that time. We call this: CGD = Available Generating Capability. It is the maximum amount of energy which a power station can produce at a particular time of day. It is another entry which we have to specify into the system, this information being in the public domain.

In the second part of the application (power station profiles) it is where the power stations which form part of the market that is to be simulated and all its features are specified. Among others features we can specify the kind of power station, cost functions, maximum available generating capacity for each hour, profit strategy, number of blocks in each one of the offer to sell functions for each period, the size of the sample used to estimate the random variable (r.v.) which define the differences in price between blocks and the parameters which define these r.v. The software allows us to add new power stations and also it is possible to store the information in a data base and introduce it when simulation is required. In Fig. 3 the main screen of SIMEL is shown to define the power station profiles.

For its part, the software allows two kinds of simulation to be carried out. One which simulates the behavior of a series of power stations which compete to enter and become part of the electricity market, estimating the average behavior of them all, and another in which a power station evaluates what the result in the market would be if a fixed strategy is applied. That is, given that a power station fixes the offer functions for each hour of a day, it simulates the market with all the power stations which participate in it, and observes the result expected from this strategy. If this process is repeated with the different strategies which the power station has, it can evaluate the result of all its possibilities and choose the one which maximizes its benefit, that is to say, the optimal strategy. To carry out this kind of simulation, it is necessary to activate the Manual Competitor option, the corresponding screen is shown in Fig. 4.

## 3.5. The warm-up phase

A market with n power stations is considered, where each one generates electricity by means of one of the different technologies. The objective is to simulate the offer blocks of a collection of power stations for 24 h of a day for a period of time, less than or equal to a full month. The choice of this simulation period is determined by this initial or warm-up phase. The electricity market regulator (OMEL) publishes every day the result of the supply and demand matching, thereby obtaining the energy selling price (spot price) for every hour of the day. On the other hand, it also publishes the offers which all the power stations carried out in the market with a delay of three months, the interval chosen by OMEL to update this information related to the offers being one month. As a result, both sets of information are used for the electricity market simulation algorithm. So four months before the month in which it is intended to simulate, complete information (spot price and selling offer functions) is available. In the three months prior to the month when it is intended to simulate, incomplete information is available (spot price). Given that we have an imbalance of three months between the two kinds of information, complete and incomplete, the idea is to carry out a first phase where advantage is taken both of the exact spot price information for three months and the complete information on the power station offers, by means of a warmup phase, thereby obtaining a stationary state of the model. The following sections describe in detail how all this information is processed and the way in which this is put together to achieve this objective.

## 3.5.1. Distribution functions of the price for each block of the energy sales offers

Since the electric energy market began until month-4, information on the spot price for every hour of the day is available, as are the offers made by power stations to the market; this period is called Complete Information. With this data, we estimate the random variables which characterize the behavior followed by the power stations during this period, for each one of the 42 scenarios defined previously.

![](/api/attachments/AJ36DJG4/fulltext/images/f15d5fd606f736afaaca4bb30752fe3e742cfac537c9e17ace1c38fcadfa3499.jpg)  
Fig. 4. The manual competitor.

The energy sales offers are discrete functions, where price-energy pairs are given, increasing in price and quantity (to the number of pairs of an offer function the term ‘blocks’ is used). The rules for each market establish the maximum number of energy blocks for the same offer. These rules can vary between 3 blocks as in the case of the English market and 25 as for example in the Spanish market. In the application, from 0 to 10 blocks have been taken, since the power station offers usually have from 3 to 6 energy blocks. The number of blocks is data which should be introduced into the system, for each power station in each of the different scenarios, as they may be different. Given the number of energy blocks of the offer function, it is defined as:

$N { = } \left\{ 1 , \ 2 , . . . , n \right\}$ the number of power stations which make sales offers to the daily market and an element of the set N is denoted by k.

$J = \left\{ 1 , 2 , . . . , 4 2 \right\}$ the number of scenarios and an element of the set J is denoted by j.

$L = \{ 1 , 2 , . . . , l \}$ is the temporary horizon of the warm-up phase, each day being $t \in L$ , then t = 1 is the first day of the warm-up phase.

$H = \{ 0 , 1 , . . . , 2 3 \}$ the 24 h in the day. We denote by h an element of the set H.

$F _ { k , j } { = } \{ 1 , 2 , . . . , f _ { n , j } \}$ the number of price-energy blocks in an offer, the maximum being 10 pairs, for each power station k ∈ N in the scenario $j \in J .$ We denote by i an element of the collection $F _ { k , j } .$

Now $P _ { i , j , h } ^ { k , t }$ is the price for the i-th block of the offer function of the power station k, in the scenario j, for the day t at the hour h.

The idea of the algorithm is to estimate the prices in each block, binding the prices of one block with the following by means of random continuous variables independently distributed. To do this, the difference between one block and the following is modelled by means of two different types of random variables which the system allows us to choose:

• Gaussian: the difference in price between (i + 1)-th block and the i-th block of the offer function of the power station k in the scenario j for the day t has a Gaussian distribution of average $\mu _ { ( i + 1 ) , i } ^ { 0 }$ <sub>i</sub> and standard deviation $\sigma _ { ( i + 1 ) , i } ^ { 0 } ,$ i.e., $\bar { P _ { ( i + 1 ) , j } } ^ { k , t } - \bar { P _ { i , j } } ^ { k , t } \approx$ $N ( \mu _ { ( i + I ) , i } ^ { o } , \sigma _ { ( i + 1 ) , i } ^ { 0 } )$ . The superindex 0 shows that it is the information which the user introduces into the system in the period $t = 0$ , that is at the moment immediately prior to when the warm-up phase begins. The users of the simulator are advised to use this when on calculating these differences, it leads to a symmetric variable.

• Beta: the difference in prices between the (i + 1)-th block and the i-th block of the offer function of the power station k in the scenario j for the day t has a Beta distribution with parameters $\boldsymbol { \alpha } _ { ( i + 1 ) , i } ^ { 0 }$ and $\beta _ { ( i + 1 ) , i } ^ { 0 } ,$ i.e. $P _ { i + I , j } ^ { k , t } - P _ { i , j } ^ { k , t } \approx \mathrm { B e t a } ( \alpha _ { ( i + 1 ) , i } ^ { 0 } , \beta _ { ( i + 1 ) , i } ^ { 0 } ) .$ . The superindex 0 indicates that it is the information which the user introduces into the system for the period t = 0. On many occasions the differences in prices between the blocks of the same offer are not symmetric, that is, they have greater density to the right or to the left in the variable range, in these cases the modelling through the Beta distribution is recommended.

It should be pointed out that each power station makes its offers for each time. In the system an offer function is also made for each time, but, as already described in the definition of the scenarios, information is shared for each of the seven groups of hours in each day, so that the subindex h corresponding to the times does not appear. In the same way, these variables are defined for each scenario.

<sup>Example 1.</sup> If we are faced with the scenario of a very dry period, a holiday and in the peak 1 timetable phase, this means that for the peak 1 times, we define a same random variable with the information available up to the moment before beginning the warm-up phase with the times that make up this scenario, and when we simulate a price for each one of these times, they are different simulations of the same random variable.

It should be emphasized that in this work we have used the information on the offers made by the power stations to the market to estimate the parameters which define these variables, with the purpose of developing later a computational experiment with real data which comes from the Spanish electricity market. But the main use of SIMEL is to give the companies a tool whereby they can introduce their experts' information and thereby be able to be more competitive in the market. This information can be introduced as a function of valuations and interpretations which each company has of its market rivals, through the distribution functions of the price for each block of the energy sales offers.

The software has a template to introduce the price distribution parameters for each kind of scenario and also allows the data to be downloaded from a spreadsheet file when these are being stored.

## 3.5.2. Incomplete information

Until now the prices of each block have been related to the following, according to the kind of distribution function. It remains to define how we tie the spot price of each hour to the offers. To this end, a continuous random variable is defined to express the difference between the maximum price of an offer for the present day for each of the 24 h in a day less the spot price for that same time in the previous day, taking for each scenario $j \in J$ the average of the times which it comprises.

Let $P _ { s , j } ^ { t - 1 }$ be the average spot price $j \in J$ of the energy market from the day prior to the present one which we wish to simulate $( t - 1 ) \in L$ . The spot price is common to all the power stations, since they all have this information available in an exact form.

As with the difference in prices between blocks, there are also two modelling options by means of a Beta or Normal distribution, this is for each $j \in J$ and for each $k { \in } N .$ , we define:

$P _ { f _ { k , j } ; j } ^ { k , t } - P _ { s , j } ^ { t - 1 } \approx N ( \mu _ { f _ { k , j } , s } ^ { 0 } , \sigma _ { f _ { k , j } , s } ^ { 0 } )$ being the pair corresponding to the maximum capacity of generating energy for each sales offer, as the function is increasing it is reached in the last block. It can also be taken as $P _ { f _ { k , j } j } ^ { k , t } { - }$ $P _ { s , j } ^ { t - l } { \approx } B e t a ( \alpha _ { f _ { k , j } , s } ^ { \theta } , \beta _ { f _ { k , j } , s } ^ { \theta } )$ .

In the third and final part of the application (Warm-up phase), the number of warm-up months required should be shown, so that the corresponding boxes and buttons to be able to download from a disk are activated, all the values of the spot prices which result from the real matching of the previous months indicated, as shown in Fig. 5.

Process of updating the random variables during the warm-up period: Once all the distribution parameters have been defined, every time a day (the 24 h) is simulated, a further item of information is obtained to update the form of the variables. This new information is introduced not only for the case of the Beta distribution but also for the Normal distribution, by means of the corresponding updating of the parameters which define each random variable.

![](/api/attachments/AJ36DJG4/fulltext/images/d3d1ea9077e656862b2dab381f54a39b4b1abb39b2a0d22513a330b11b8532a6.jpg)  
Fig. 5. Warm-up period.

3.5.3. Calculation of the prices in each block of the energy sales offers

Previously, we have defined the parameters which bring together the prices of a power station offer and the relationship with the spot price. It remains to be seen how the prices of each block in the warm-up phase are obtained starting from the variables which have been defined in the previous section.

3.5.3.1. Obtaining the maximum price in each offer function. For the first hour of the day $( h { = } 0 )$ of the first day (t = 1), we begin simulating an execution of the chosen distribution function, Gaussian or Beta, defined for the scenario $j \in J$ such that the hour h belongs to this scenario $j .$ If the difference between $P _ { f _ { k , j } , j } ^ { k , 1 }$ (maximum price) and the $P _ { s _ { k , i } } ^ { 0 }$ (spot price of the previous period) has been modelled by means of:

• One Gaussian distribution of average $\mu _ { f _ { k , j } s } ^ { 0 }$ and standard deviation $\sigma _ { f _ { k , j } , s } ^ { 0 } .$ . We begin simulating a value of a standard Gaussian distribution, denoting this as $z _ { i , j , h } ^ { k , l } .$ Then $x _ { f _ { k , j } , s , h } ^ { k , 1 } { = } z _ { i , j , h } ^ { k , I } \sigma _ { f _ { k , j } , s + } ^ { 0 } \mu _ { f _ { k , j } , s } ^ { 0 }$ provides a simulation of the difference between the maximum price of the offer function and the spot price of the previous period.

• One Beta distribution of average $\mu _ { f _ { k , j } , s } ^ { 0 }$ and standard deviation $\mathrm { ~ \bf ~ { ~ \sigma ~ } ~ } _ { f _ { k , j } , s } ^ { 0 } ,$ with range $\theta \in [ \theta _ { 1 } , \stackrel {  } { \theta } _ { 2 } ]$ , these being the minimum and maximum values respectively. In the case of the Beta distribution, a value $\mathbf { z } _ { i , j , h } ^ { \bar { k } , I }$ is simulated in the range [0,1] (because the process to simulate a value is simpler), therefore it is necessary to introduce the values of the average and the standard deviation which define the Beta distribution parameters, normalized between zero and one, together with the maximum and minimum values $( \theta _ { 1 , } \ \theta _ { 2 } )$ of the range. Later, this normalization is broken down to find out the difference between the maximum price and the spot price for the previous period as follows: $x _ { f _ { k , j } , s } ^ { k , 1 } { = } \bar { \theta _ { 1 } } { + } ( \bar { \theta } _ { 2 } { - } \theta _ { 1 } ) z _ { i , j , h } ^ { k , I }$ .

Then $x _ { f _ { k , j } , s } ^ { k , 1 }$ is an execution of the difference in prices between $P _ { f _ { k , j } , j } ^ { k , 1 }$ and $P _ { s , j } ^ { 0 }$ . In addition the spot price for the previous day is known, then the maximum price is obtained in the form: $P _ { f _ { k , j } , j } ^ { k , 1 } = x _ { f _ { k , j } , s } ^ { k , 1 } + P _ { s , j } ^ { 0 }$

The value of the maximum price of an offer for an hour $h \in H$ in the scenario $j \in J$ for the first day of the warm-up phase has already been simulated. This value being known, the following price of the offer function can now be simulated.

3.5.3.2. Obtaining the rest of the prices in each block for each offer function. Once again we simulate an execution of a standard Gaussian or a Beta of a range [0,1] we denote $z _ { i , j , h } ^ { k , I }$ the simulated value, according to each case we have:

• One Gaussian distribution of average $\mu _ { ( i + 1 ) , } ^ { 0 }$ i and standard deviation $\boldsymbol { \sigma } _ { ( i + 1 ) , i } ^ { 0 } ,$ then $x _ { ( i + 1 ) , i , j , h } ^ { \ k , 1 } =$ $z _ { i , j , h } ^ { k , I } \sigma _ { ( i + I ) , i } ^ { o } + \mu _ { ( i + I ) , i } ^ { o }$ . Then the simulated value of the difference between the maximum price (i + 1) and the price of the present block i is obtained.

• Given the Beta(α,β) distribution of average $\mu _ { ( i + 1 ) , i } ^ { 0 }$ and standard deviation $\sigma _ { ( i + 1 ) , i } ^ { 0 }$ with range $( \theta _ { 1 } , \theta _ { 2 } )$ then $x _ { ( i + 1 ) , i , j , h } ^ { k , 1 } { = } \theta _ { 1 } { + } ( \theta _ { 2 } { - } \tilde { \theta } _ { 1 } ) z _ { i , j , h } ^ { k , I }$

Once the value $x _ { ( i + 1 ) , i , j , h } ^ { k , 1 }$ has been simulated and the value $P _ { ( i + 1 ) , j , h } ^ { k , 1 }$ is known, $\bar { P } _ { i , j , h } ^ { k , l }$ can be obtained as follows $P _ { i , j , h } ^ { k , l } { = } P _ { ( i + l ) , j , h } ^ { k , l } { - } x _ { ( i + l ) , i , j , h } ^ { k , l } .$

In this way, the price in the i-th block of the sales offer function for the time h for a day t is obtained. The algorithm is completed as follows:

1. It is carried out for all the times h ∈ H for the period t.

2. The average prices are calculated of the times which make up the same scenario in each block of the offer, for each power station.

3. The averages and variances of the random variables are updated.

4. The algorithm is repeated for all days of the warm-up time horizon.

This process can be seen illustrated in the flow chart in Fig. 6, for each power station with $i \in [ 1$ , I] offer blocks, 24 h of the day $h \in [ 0 , \ 2 3 ]$ and a warm-up horizon $t { \in } [ 1 , T ]$

![](/api/attachments/AJ36DJG4/fulltext/images/1d2a4a8d32fa063438cd0d6ffc53a03378f44ef3b6a71016d80962359e3a2fa4.jpg)  
Fig. 6. The flow chart for warm-up phase.

## 3.6. Simulation phase

Once the last day t of the warm-up phase has been reached, the prices for each block of the offers for the first day to be simulated are found, having the r.v. of the difference of the price updated for that day. The algorithm will consist then in assigning in each block of the offer function to each price, a quantity of energy which takes into account the price offered. The idea is that the sales price of a unit of energy according to a mark-up (B) can be equal to the mark-up times the unit cost, that is to say, energy is offered at the price it costs us to produce it (no profit is obtained), expressed by $B { = } 1 ;$ ; the energy is offered at a price below cost, expressed by $B < 1$ ; and the energy is offered at a price greater than the production cost, expressed by $B > 1$ . The price and the energy are related to each other according to the general expression $\begin{array} { r } { p = B \cdot \left( \frac { \mathrm { C F } + \mathrm { C V } ( e ) } { e } \right) } \end{array}$ , where CF and CV are fix and variable costs respectively. Then clearing from the last equation related to the kind of power station (thermal, hydro-electric power, combined cycle or wind powered) by means of CF and CV (see Section 3.4) the quantity of energy offered is obtained.

In this way, the price-energy pairs of each offer are given expressing the energy according to the price in each block and the mark-up $B _ { i } .$ . The regulations of the market establish that each power station has to offer its available generation capacity (CGD) in the last block of each offer, $f _ { k , j } .$ . Then clearing from the equation $\begin{array} { r } { p = B \cdot \left( \frac { \mathrm { C F } + \mathrm { C V } ( e ) } { e } \right) } \end{array}$ according to the functions CF and CV for each kind of technology (see Section 3.4) we obtain the maximum mark-up of the offer function, called $B _ { f _ { k } }$ or, equivalently, $B _ { \mathrm { M A X } }$ . In the paper the mark-up $B _ { i }$ will be characterized as a trapezoidal fuzzy number $( b _ { 1 } , b _ { 2 } , b _ { 3 } ,$ $b _ { 4 } )$ . Below we show in detail how the parameters are which define the fuzzy numbers of the mark-up in each offer function.

The minimum value $b _ { 1 }$ is fixed which defines the fuzzy number of the mark-up B according to three criteria on the mark-up expected by the power station.

• Price 0. To offer in the first block of the offer function a quantity of energy at zero cost, that is, $b _ { 1 } = 0$ , to ensure the sale of energy. This behavior is usual among companies which take the price in uniform tenders. To emphasize that in the algorithm when energy is assigned at zero cost, a minimum energy sales quantity is taken. This can be interpreted as when in the case of being less than that quantity of energy, a power station will not start up its machines.

• Mark-up 0. The behavior of the power station consists of not having losses in any block of its function of bets, trying to ensure that it enters the system so that its most competitive bid does not lose. Therefore, the lowest limit is $b _ { 1 } = 1$

• Marginal costs. As in the previous case, in the first block the minimum energy is assigned to the marginal price of producing that energy and from this relationship we obtain the minimum value of the fuzzy number of the mark-up $b _ { 1 }$

The minimum value does not vary for the different blocks in each offer, but the maximum value $b _ { 4 }$ does vary since in the highest block it is the maximum markup and in the following blocks the mark-up gradually reduces as a consequence of the same reduction in price and energy. For this reason according to the kind of competitive company $b _ { 4 }$ will be in each block:

1. Hydro-electric power or wind-powered: the maximum value of the mark-up in the i-th block of an offer function is less than the value of the maximum mark-up of the previous block (i + 1) so we can ensure that this is fulfilled if $\begin{array} { r } { b _ { 4 } ^ { i } = \frac { p _ { i } } { p _ { i + 1 } } B _ { i + 1 } } \end{array}$ . This condition is the direct consequence of the form of the offer functions of the power stations which establish that $e _ { i + 1 } { \geq } e _ { i }$

2. Thermal: to find an analytical condition for the thermal stations which satisfy that $e _ { i + 1 } \geq e _ { i }$ and to be able to express it in simple terms is difficult, which is why we have designed a small algorithm:

a. $b _ { 4 } ^ { i } { \le } B _ { i + 1 }$ is taken.

b. A value of the fuzzy number of the mark-up is simulated, $B _ { i }$

c. $\mathrm { I f } e _ { i + 1 } \geq e _ { i } \longrightarrow$ is fulfilled we are left with that value.

d. If it is not fulfilled the extreme maximum ${ b _ { 4 } } ^ { i }$ is taken to be the same as the simulated value → we simulate again a value for the mark-up (step 2).

3. Combined cycle: for the combined cycle stations imposing the condition $e _ { i + 1 } { \geq } e _ { i }$ it remains that $b _ { 4 } ^ { i }$ has to be less than or equal to the minimum between:

$$
b _ {4} ^ {i} = \frac {p _ {i}}{p _ {i + 1}} B _ {i + 1} \text { and } b _ {4} ^ {i} = \frac {p _ {i}}{\beta}
$$

The problem is how to fix the central points $b _ { 2 }$ and $b _ { 3 }$ of the mark-up. Given a trapezoidal fuzzy number $( b _ { 1 } ,$ $b _ { 2 } , b _ { 3 } , b _ { 4 } )$ , we denote by $R _ { 1 }$ the area between $b _ { 1 }$ and $b _ { 2 } ,$ by $R _ { 2 }$ the area between $b _ { 2 }$ and $b _ { 3 }$ and, finally, $R _ { 3 }$ the area between $b _ { 3 }$ and $b _ { 4 } .$ . Then to obtain the central points we use a small algorithm which fixes the value of the areas $R _ { 1 } , R _ { 2 }$ and $R _ { 3 }$ at 0.05, 0.90 and 0.05 respectively, being able to calculate the value of $b _ { 2 }$ and $b _ { 3 }$ .

## 3.7. Matching of the sales offer functions with the demand

It is the algorithm which is charged with the task of calculating the spot prices and the mark-ups obtained in accordance with this, for each one of the power stations and for each hour of the day in which they join in the bidding. For this reason, the offer price vectors for each of the power stations are arranged from lesser to greater, for each time of the day. This allows us to go over the price vector in ascending order, so that the total energy offered is the sum of the energy offered by each of the individual companies whose respective price is less than or equal to that of the selected element of the said vector. In the event that the total energy offered is greater or equal to the demand for that time of the day, it will be before the spot price.

Therefore, this same algorithm permits us to know simultaneously, what the set spot price is, as well as which company or technology sets it. Likewise, it lets us know how many times a company sets the price a particular time, making it possible to calculate what the associated probability is. A flow chart of the matching phase is shown in Fig. 7.

![](/api/attachments/AJ36DJG4/fulltext/images/ada4141c3ccbc0e5ee639a74bd379d893d5b7750cd44468288d9603acd5d5986.jpg)  
Fig. 7. The flow chart for matching

The process described below, should be carried out for each of the 24 h in a day. To be able to understand this, we will consider one hour $h \in H ;$

• The vectors of the pairs of price-energy offers for each one of the power stations are ordered from lesser to greater taking into account the price.

• The number of possible blocks is 10. Therefore, to carry out a correct matching, the vectors are completed with 10-i identical blocks to the block of lowest value in price for each power station, where i is the number of blocks of the power station.

• All the offers in price are ordered jointly in one single vector in ascending order of price.

• The vector is covered element by element (price to price) until it is true that:

1. Given an element $p _ { i }$ of the joint vector, we look for which price is greater or equal to each one of the vectors of the power stations.

2. The energy associated with each one of these prices is added. That is the energy offered to the market at that price:

If this satisfies the demand → spot price.

We return to step 3.

• Calculation of the energy sold at that price matched for each on of the power stations. This lets us know what the mark-up obtained for each particular station is, according to the estimated production costs for the said company.

A situation worthy of analysis is what should happen when a ‘draw’ situation occurs, that is, when two or more power stations offer energy at the same price when that price has been the result of matching, that is, the spot price. To solve this situation, an auxiliary algorithm has been designed which reveals this fact. In reality, it is the Market Operator who is in charge of regulating situations of this kind, assigning the sale of energy to that or those power stations whose technical conditions are more favorable for the distribution of the energy (distance from the power station to the consumption point, economic,….). This algorithm would act before calculating the energy sold by each station, in the case where it is found that more than one of the same spot price exists, in the other case the matching algorithm would follow the process described in the previous diagram. The operating method for one hour h is the following:

1. It is checked to see if there is more than one offer price which is the same as the spot price resulting from the matching of that time.

2. The stations whose offer price is less than the spot price, are the first to sell energy, so that, once that energy has been shared, the quota of energy left over to cover the demand is shared equally between the number of stations which have the same price as the spot price.

## 4. Report of the results

Once the simulation has been completed, all the data obtained are presented in a practical format such as spreadsheets, which allows us to store on the hard disk the result of all the simulations carried out. The format of the book of results shows the following composition divided into the different pages:

1. Simulation report: general data on the simulation appear in this, as for example, the period of time simulated, the simulation time, the name, the technology and kind of mark-up used by each one of the power stations and the kind of climatic scenario.

2. Demand: sample of the quantity of energy requested in MW per hour for each hour of the day and for the number of days simulated.

3. Spot price: presents both the spot price resulting from the matching for each time and day simulated. Two spot prices are found to be represented: the first of these is the result of the matching with the average values of the Price/Energy offers for a number of simulations ns. The second of these is the average spot price resulting from each one of the ns simulations in particular, with the Price/Energy pairs of those ns simulations. In the following section a computational experiment is carried out where the spot price results obtained with SIMEL are outlined. Here it is intended to emphasize that although the main objective of the simulator is to provide a tool for decision-making by the companies which generate electricity, as a result of simulating a competitive electricity market, an estimation of the market spot price is obtained for each hour of the day, for a temporary short-term horizon (from one to three days) until medium-term (one month), using for this estimation an approach which is based on the strategic behavior of the companies at the time of making their sales offers. This estimation solves a complex problem from the point of view of other disciplines used in the estimation of the spot price, such as temporary series, since as the spot price cannot be expressed solely according to its own past, it involves more than just the seasonal factor (by hours, weeks, months) and the changes in weather conditions over a period of time are very abrupt, so exact estimations cannot be given for each time, neither short nor medium-term.

![](/api/attachments/AJ36DJG4/fulltext/images/72acc0869bbb4f83b7c675838fa4c41ef0e3b745485a253bebd33d53b18b2f09.jpg)  
Fig. 8. The average spot prices per hour on the working days.

4. Probabilities: specifies the technology and power station which gives the spot price for each time and day simulated, as well.

5. n sheets defined as the name of the Power Station which is involved in the simulation in which the set of Price/Energy offers for each one of the days and times of the selected simulation period; the quantity of energy sold for each time of the day according to the spot price; the expected and the final mark-up, according to that quantity of energy sold, the selling price and the specific power station costs, on average, resulting from the calculations during ns simulations, all appear.

## 5. Computational experiment: simulation of a very dry period in the Spanish electricity market

To show how the application works, the results obtained are shown below for a simulation with the following characteristics:

Number of competitive power stations: 5. Kind of competitive stations<sup>1</sup>: 2 thermal, 2 hydraulic, and 1 combined cycle. Number of simulations: 100; simulation time: approximately 30 min/day. Period of simulation: 1/04/2005 to 17/04/05. Actual climatic period: very dry. Mark-up strategy: Mark-up 0 (for all the stations). Simulation type: uniform. Distribution function of the difference in price: type beta (for all the stations).

## 5.1. Comparison of the spot price

The main objective of this application is not to give an exact estimate of the spot price in the short term. But it is a good indicator to control the reliability of the system. In Fig. 8 the average spot prices per hour on the working days simulated, and the values obtained in the Spanish electric energy daily market are shown. As can be seen, the simulator has detected perfectly the hourly variation in the spot price, this means that the system is able to simulate the behavior of the daily electric energy market, since the spot price is the final result of the matching of selling offers with the demand and so the energy sales functions which the simulator provides, are a good reflection of the behavior of all the power stations, and therefore we can use this tool to advise the companies generating electricity what bids they should make to increase their mark-up.

Note that the price estimated with the simulator is greater than that which really occurred in the market, this is normal as a simulation has been made with five power stations (by way of an academic example) while more than 300 power stations take part in the daily market.

If the same figure is made comparing the average spot price per hour for holidays, it is also seen that the simulator detects perfectly the variations in the spot price (see Fig. 9). In this case the competition between the power stations increases, as during the weekends less energy is required and the companies have the same generating capacity at their disposal to satisfy the demand, and then compete more aggressively, so that the hourly spot price goes down.

![](/api/attachments/AJ36DJG4/fulltext/images/9023e692dd0054dedac9d1aa646e98bed29dfa171d400f937713f6edb22bedfe.jpg)  
Fig. 9. The average spot prices per hour for holidays.

## 5.2. Power stations which fix the spot price

Another of the interesting results provided by the simulator is the technology which fixed the spot price for each time, as well as the probability of a power station fixing the spot price for each hour. On examining the table in Fig. 10 that shows which technology fixed the spot price, it can be seen that there is a big difference between working and non-working days. As previously mentioned on working days there is more demand for electric energy; this causes the most competitive companies (which in a very dry period like the present, are the power stations of the combined cycle type and then the thermal) to make their offers to fix the spot price and the least competitive (in this scenario, the hydraulic)

![](/api/attachments/AJ36DJG4/fulltext/images/0c566d223bb67dda504ee41fe51e813e1b9568bdd661a78222ff65a46a929e76.jpg)

```txt
TE = POWER STATION: CONVENTIONAL THERMAL
CC = POWER STATION: COMBINED CYCLE
HI = POWER STATION: HYDROELECTRC
```  
Fig. 10. Technology fixed the spot price.

![](/api/attachments/AJ36DJG4/fulltext/images/f454544c19a99027095336839a127486cb9c374ad2831e59ad4cbde929e9dcfc.jpg)  
Fig. 11. The probability has been that each one of the companies fixes the spot price at each time of the day.

are those which accept the spot price and make their offers, offering the first energy block at zero cost. In the second block they offer energy at a price which they believe to be higher than the spot price. This results in, that during the hours of greatest demand (as there is not much competition in the model), the energy which the hydraulic stations have offered is needed and therefore more often fixes the spot price. In the real market where there is more competition, this behavior also occurs, but at fewer times of the day, usually at peak hours, as the hydraulic power stations do not have the raw material at their disposal in dry periods to be competitive 24 h a day, they keep their most aggressive bids for the hours of greatest demand.

At weekends, as the demand for electric energy is less, the stations which fix the spot price are the most competitive, that is, combined cycle and thermal, since as the demand decreases the energy for the second block of the hydraulic stations is not needed. The Fig. 11 shows what the probability has been that each one of the companies fixes the spot price at each time of the day, for each one of the simulations carried out each day, with which these results have been obtained.

## 5.3. Results obtained for a power station

Due to the large amount of data obtained with the simulation, only the results of the sales offer functions are given in detail for a peak and off-peak time for one of the power stations, both for a non-working and working day. The time of greatest and least demand has been chosen, on account of the fact that the competitors offers are much more competitive, making it possible to show the comparison of the most varied scenarios.

![](/api/attachments/AJ36DJG4/fulltext/images/dc2fc7a9644582bfba82de0e9e4c94ac95cc9da0fccf57be5600f979055821ef.jpg)  
Fig. 12. The average offer functions are shown for the CC1 power station at 21.00 which is that of greatest demand, on a working day.

![](/api/attachments/AJ36DJG4/fulltext/images/32937fcee9cf86bdbc88146c510eae1d5adb44eab4a4547c3ca9e8abf2880991.jpg)  
Fig. 13. The average offer functions are shown for the CC1 power station at 03.00 which is that of least demand, on a working day.

Power station: CC1 a power station of the combined cycle kind has been selected because in a very dry scenario, this kind of station is the most aggressive in making its offers of the sale of energy to the market.

## 5.3.1. Offer function

In the Figs. 12 and 13, the average offer functions are shown for the CC1 power station at 21.00 which is that of greatest demand and at 03.00 which is that of least demand on a working day. The average offer function for each hour obtained with the simulator are the points which appear on the figures, in addition an approximation with a continuous function has been drawn; it is intended to emphasize graphically the great difference which exists between the two ways of modelling the energy sales offer functions of the power stations. To emphasize that in scenarios like this (very dry) the offer functions usually have very few blocks and as can be seen in the figures, the continuous form does not reflect the real behavior of the power station strategies.

To emphasize that for working days this power station gave the market and energy sales function with four blocks, in both functions, in the first block it offers energy at zero cost, this block is interpreted as the manner the companies use to ensure that they are going to sell energy, in the two following blocks the intention is to fix the spot price, in the second block the price which gives the energy is less than what it is estimated the spot price will be, but in the case of fixing the spot price in this block, it ensures that there will not be losses. The third block is where it is believed the spot price will really be and the last block is the price at which all its energy would be sold at a very high mark-up. To emphasize that the behavior for a peak or off-peak time is very similar, nevertheless, there is a clear difference in the price in the second block, which where it is estimated the spot price will be, at the peak time that price is 4.82 euro cents/kwh, whereas at an off-peak time the price is 3.21 euro cents/kwh and the energy offered at those prices is the same. That is, the greater the demand the higher the spot price is estimated.

![](/api/attachments/AJ36DJG4/fulltext/images/0a4db87b49a867c2bd767e91f55d4ca8cf7360b8e7657608d2a14c788fc3b442.jpg)  
Fig. 14. The average profit obtained, for working days in the period simulated.

## 5.4. Profits obtained

In Fig. 14 the average profit obtained is shown for the same power station, for working days in the period simulated. To emphasize that the average profit has the same form as average price per hour. As can be expected, the average profit on working days is greater than on public holidays, since both the demand and the spot price which results is greater in the former case.

## 6. Conclusions

As the years go by, companies live in an ever more competitive market and need to become more productive, relying on information received. Companies handle an enormous amount of information, and in addition, in such a changing world as the present, decisions have to be taken and changed for each variation in the market. When data is analyzed in such a way that it is possible to obtain a competitive advantage, advantages can indeed be gained and above all decisions will be taken based on real and current data in such a way that decision-making time is reduced and this in turn allows us to generate actions to generate advantages. This is why the main objective of this work has been to develop a simple software tool in the form of a Decision Support System (DSS). This makes it possible to simulate in a clear and simple way how an electricity market functions (it does not have to be Spanish) based on a system of simple matching.

Although the application is able to carry out the simulation of a full month, the optimum operation of this DSS is day to day, for several reasons: (1) the Spanish Transmission System Operator provides the best estimation of the demand for the day following the present one in an open manner; (2) the spot prices are updated and published on the OMEL website daily, so that it is better to warm up the system with true values than with estimated parameters, since estimations imply an error which accumulates with the passing of time; and (3) the appearance of wind-powered stations whose behavior can be estimated for a short period of time (of about three days).

Apart from the academic interest, the commercial use of this tool would be interesting for the different power stations which compete in the market, once it has been developed more extensively, allowing strategic decisions to be taken depending on the behavior of the competing stations and the given conditions, providing, for example, advantages such as:

• Reduction in decision-making time.

• Generating reliable information to be able to make the right decisions.

• Reduction in decision-making costs.

• Increase in productivity.

• It leads to an analysis of: what happens if? Each power station can fix a strategy (manual competitor option) and analyze the result it would obtain in the market.

It should be emphasized that the tool we have developed will fulfil its main objective, which is to provide the companies, which sell energy in the electricity market, a DSS to make its offers to the market for each time of the day. But in addition, we provide an estimation of the spot price in the short term; to give an estimation is very important, as with theoretical models this is not achieved, these are more focused on being studied when changes in the spot price are produced.

## References

[1] Asociación Española de la Industria Eléctrica. http://www.unesa.es.

[2] L. Ausubel, P. Cramton, (1998). Demand Reduction and Inefficiency in Multi-unit Auctions. Working Paper. Economics Department, University of Maryland, 98wpdr

[3] R. Baldick, W.W. Hogan (2002). Capacity Constrained Supply Function Equilibrium Models of Electricity Markets: Stability, Non-decreasing constraints, and Function Space Iterations. Working paper. Energy Institute (University of California, PWP-089).

[4] R. Baldick, W.W. Hogan (2004). Polynomial Approximations and Supply Function Equilibrium Stability. Working paper. Center for Business and Government (Harvard University).

[9] Centro de Estudios Hidrográficos, (2006). http://www.cedex.es. [10] Comisión Nacional de Energía, (2006). http://www.cne.es.

[5] R. Baldick, R. Grant, E. Kahn, Theory and application of linear supply function equilibrium in electricity markets, Journal of Regulatory Economics 25 (2) (2004) 143–167.

[6] K. Binmore, Teoría de Juegos, Editorial McGraw-Hill, 1994.

[7] K. Binmore, J. Swierzbinski, Treasury auctions: uniform or discriminatory? Review of Economic Design 5 (4) (2000) 387–410.

[8] C.E. Bazán (2004). Análisis de la competencia en un mercado mayorista de electricidad: el caso de España. Working paper. Departamento de Análisis Económico Aplicado (Universidad de Las Palmas de Gran Canaria).

[11] Compañía Operadora del Mercado Español de Electricidad. http://www.omel.es.

[12] A. Cournot, Recherches sur les principes mathématiques de la théorie des richesses, Libraire des sciences politiques et sociales, Paris, 1838.

[13] J.B. Cruz, X. Tan, Price strategies in dynamic duopolistic markets with deregulated electricity supplies using mixed strategies, Decision Support Systems 40 (3–4) (2005) 439–447.

[14] C. Day, D. Bunn, Divestiture of generation assets in the electricity pool of England and Wales: a computational approach to analyzing market power, Journal of Regulatory Economics 19 (2) (2001) 123–141.

[15] C. Day, B.F. Hobbs, J.S. Pang, Oligopolistic competition in power networks: a conjectured supply function approach, IEEE Transactions on Power Systems 17 (3) (2002) 597–607.

[16] N. Fabra, N.H. Von der Fehr, D. Harbord, Modelling electricity auctions, Electricity Journal 15 (7) (2002) 72–81.

[17] E. Kahn, Numerical techniques for analyzing market power in electricity, Electricity Journal 11 (6) (1998) 34–43.

[18] A.R. Kian, J.B. Cruz, Bidding strategies in dynamic electricity markets, Decision Support Systems 40 (3–4) (2005) 543–551.

[19] P. Klemperer, Why economist should learn some auction theory, www.nuff.ox.uk/economics/people/klemperer 2000.

[20] P. Klemperer, M. Meyer, Supply function equilibria in oligopoly under uncertainty, Econometrica 57 (1989) 1243–1277.

[21] Ministerio de Economía. http://www.mineco.es.

[22] Ministerio de Medio Ambiente, (2006). http://www.mma.es.

[23] E. Pettersen, A.B. Philpott, S.W. Wallace, An electricity market game between consumers, retailers and network operators, Decision Support Systems 40 (3–4) (2005) 427–438.

[24] Red Eléctrica de España, (2005). http://www.ree.es.

[25] T. Sueyoshi and G.R. Tadiparthi, in press. An agent-based decision support system for wholesale electricity market. Decision Support Systems, In Press, Corrected Proof, Available online 18 May 2007.

[26] J. Sun and L. Tesfatsion (2007). Dynamic Testing of Wholesale Power Market Designs: An Open-Source Agent-Based Framework. ISU Economics Working Paper, 06025, revised March.

[27] M. Ventosa, M. Rivier and A. Ramos (2000). Revisión de las tendencias de modelado de la explotación de la generación en mercados de generación eléctrica. Instituto de Investigación Tecnológica (Universidad Pontificia de Comillas).

[28] M. Ventosa, A. Baillo, A. Ramos, M. Rivier, Electricity market modeling trends, Energy Policy 33 (7) (2005) 897–913.

[29] R. Weron (2006). Modeling and forecasting electricity loads and prices. A Statistical Approach. Ed. John Wiley & Sons.

<sup>Julia Sancho</sup> was born in October 1974 in Avellaneda (Spain). She received a Statistics Degree from the University Miguel Hernández of Elche (Spain) and a DEA in Financial Statistics from the same university. She was part of several research projects related to the electricity markets in Spain. Julia Sancho is currently a PhD student at the Operations Research Center of the University Miguel Hernández. Her research interests are: energy markets, game theory and power systems operation and control.

<sup>Joaquín</sup> <sup>Sánchez-Soriano</sup> received a Mathematics Sciences Degree from Murcia University (Spain), obtaining an award for the best academic records, a DEA in Quantitative Economics from Alicante University (Spain), a DEA in Operations Research, Statistics and Applied Mathematics from Murcia University and a PhD in Mathematics Sciences from Murcia University. In 1998, he received the ‘Ramiro Melendreras’ Award for young researchers in Statistics and Operations Research. At present, he is a Lecturer in the Department of Statistics, Mathematics and Computer Science, and the Director of the Operations Research Center of the University Miguel Hernández. His current research interests include: game theory and its applications, in particular to radio resource management, transportation problems and market design.

<sup>Juan Antonio Chazarra</sup> received a Telecommunication Engineer Degree from the University Miguel Hernández in 2005. He is currently a PhD student at the Operations Research Center of the University Miguel Hernández.

<sup>Juan Aparicio</sup> was born in January 1978 in Alicante (Spain). He received a Statistics Degree and a DEA in Financial Statistics from the University Miguel Hernández of Elche (Spain). He is currently a Lecturer in the Department of Statistics, Mathematics and Computer Science of the University Miguel Hernández. His current research interests include: game theory, auctions, efficiency and productivity analysis.
