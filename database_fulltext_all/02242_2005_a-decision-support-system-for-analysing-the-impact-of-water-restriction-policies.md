---
otero_id: 2242
otero_key: "JHU9SVZD"
title: "A decision support system for analysing the impact of water restriction policies"
authors: "B. Recio; J. Ibáñez; F. Rubio; J.A. Criado"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2003.11.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dsw

# A decision support system for analysing the impact of water restriction policies

B. Recio\*, J. Iba´n˜ez, F. Rubio, J.A. Criado

Departamento de Matema´tica Aplicada a la Ingenierı´a Agrono´mica, Escuela Te´cnica Superior de Ingenieros Agro´nomos, Universidad Polite´cnica de Madrid, Avenida de la Complutense s/n, Madrid 28040, Spain

Departamento de Estadı´stica y Me´todos de Gestio´n en Agricultura, Escuela Te´cnica Superior de Ingenieros Agro´nomos Universidad Polite´cnica de Madrid, Avenida de la Complutense s/n, Madrid 28040, Spain

Received 1 November 2001; accepted 1 November 2003 Available online 11 March 2004

## Abstract

The overall objective of the ‘‘Design of a Integrated Ground Water Management System. Application in the aquifer system 08.29 in Mancha Oriental, Spain’’ project (GESMO), financed by the Spanish government, is to research into new software tools for managing water resources in the agricultural environment. This paper presents a decision support system (DSS) developed within that project. The goal of the system is to assist Eastern Mancha Central Irrigation Board authorities to evaluate water use policies that combine the sustainability of natural resources with regional economic development, which is effectively based on irrigation farming. For this purpose, two different models were integrated within one and the same computer application. One is a hydrogeological model able to simulate the River Ju´car basin and its associated aquifer. The other is an econometric model capable of statistically predicting the evolution of the regional crops map, the crop yields and the associated prices, thus allowing for the determination of the regional gross product of crops. A combination of both models can be used to compare the reserve of ground water with the product generated using it as a resource, thus making easier to identify the policies that best combine both factors. The scope of this work is the whole river Ju´car aquifer (which is the second largest in surface in Spain) and the lands irrigated by it.

Functionally, the hydrogeological model is based on finite differences in accordance with the Modular Three-Dimensional Finite-Difference Ground Water Flow (MODFLOW) model developed by the US Geological Survey (USGS), whereas the econometric model is supported by statistical techniques. An important effort have been made in coupling both models as a feedback cycle allowing for a dynamic scenario assessment. Technically, the DSS is conceived as an integrated tool which has been implemented in Visual Basic with a database associated. Its architecture could be translated to other regions without significant programming changes, only introducing new particular parameters into the database. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Decision support system; Hydrogeological model; Econometric model; Water resources management

## 1. Introduction

In the early 20th century, traditional farming in the Mediterranean countries started to be gradually overtaken by an increase in irrigated farmland wherever water availability thus permitted. Such changeover is beneficial in more than one regard. Firstly, irrigated crops are much more profitable than dry land crops. Secondly, many of the irrigated crops (especially fruit and vegetables) are associated with agrofood industries which boost regional economic wealth: canning, vegetable freezing, sugar industries, etc. Finally, as a result of the change in the system of production and also of the increased profitability, a significant ancillary industry emerges, specialised in canalisation, drill testing, installing irrigation systems, etc.

However, the irrigation of hundreds of thousands of hectares of dry land upsets the water balance in the region at issue and may cause, in extreme cases, surface waters to dry up (rivers, lakes, etc.) or the depletion of ground water aquifers, with serious ecological and environmental implications.

The dramatic effects of this situation are being felt in regions of the interior of Spain (Albacete, Ciudad Real, etc.), where intensive agriculture has developed due to the exploitation of aquifers whose piezometric levels (the lift of the water table to the ground) have fallen rapidly. This has led to the continuous application of water restriction policies based on extraction quotas. These environmental policies have a major economic and social impact on the regions at issue, making necessary to develop suitable tools as an aid for predicting the agricultural and economic impact of their application.

The Eastern Mancha hydrogeological system 08.29 is the second largest aquifer in Spain and is plagued by these problems. It is located in the easternmost part of the Mancha plain, in southeastern central Spain. It has a surface area of 8500 km<sup>2</sup>, over half of which is situated in an immense plateau at an altitude of 700 m. The climate is warm continental with a marked variation between wet and dry months. Rainfall is low, around 350 mm/year.

Aquifer use has gradually increased over the last 15 years. Table 1 briefly outlines this trend.

The aquifer has been one of the drivers of economic development in the region. Now, it supports 90,000 ha of modern irrigated land whose output reaches 240 million o/year. In this way, the need to find a balance between economic advancement and the conservation of natural resources has brought water policy to the environmental, social and economical forefront in that region.

Table 1  
Trends of irrigated land and volume of water consumed in the 1972– 1990 period

<table><tr><td>Year</td><td>Irrigated area (ha)</td><td>Water volume (hm $^{3}$ /year)</td></tr><tr><td>1972</td><td>12,277</td><td>78</td></tr><tr><td>1979</td><td>29,686</td><td>165</td></tr><tr><td>1987</td><td>62,836</td><td>387</td></tr><tr><td>1990</td><td>71,519</td><td>407</td></tr></table>

The objective of the GESMO project, financed by the Spanish government, is to develop management tools that can harmonise resource exploitation with reserve sustainability in aquifer 08.29 in the Eastern Mancha region. GESMO was conceived to output two types of end products:

1. A decision support system (DSS) for defining water use policies by assessing the economic and environmental impacts within a single multicriteria/multipurpose decision-making simulator.

2. Measure monitoring and control systems, integrated in a Geographic Information System (GIS) and employing teledetection and simulation of crop water needs.

It is important to point that the software systems of those products are not currently related given that they have different orientations: The DSS is oriented to planning at aquifer level (in fact, a regional level) and the control systems are oriented to enforce the water restriction policies at farm level.

The content of this paper is restricted to describe the decision support system included in the GESMO project and to explain some of its possible applications.

## 2. Description and objectives of the water use policies evaluation system

The management of water resources in Spain is done by the Ministry of the Environment, which devolves the development of policies to the Hydrographic Confederations (HCs) of each basin. In practice, it is the HCs that exert the authority in this matter.

The sensitivity of the agricultural sector to water restriction measures is channelled through irrigation boards. These are irrigation co-operatives with a purpose of self-regulation, which is necessary for several reasons, the main one being the management of water availabilities during periods of scarcity. Other functions are the inspection of irrigation systems and the solving of conflicts between irrigation farmers. Some of these institutions are very old, dating back to the Middle Age.

The Eastern Mancha Central Irrigation Board is one of such associations in which the Hydrographic Confederation of the Ju´car has given the responsibility to design and control water use policies in aquifer 08.29.

There exist different instruments for water management. The most common, up until now, has been the allocation of irrigation quotas to the hectare. As knowledge of the aquifer increases, more sophisticated policies could be designed: seasonal and geographical modulations of the quota, suitable allocations between surface water (coming from the Ju´car river) and ground water, etc. All of these policies mainly need the flows extracted to the wells and the crop plans of the farmers to be controlled.

There are two opposite poles in the configuration of water policies:

1. Prioritise the maintenance of the aquifer over any other factor. This would mean to restrict the pumping to the average annual recharge of the aquifer and use groundwater mainly as a mean for smoothing climatic irregularities. In general, economic development of the region would find a severe constraint with this kind of measures.

2. Prioritise economic development over any other factor. This will cause a reduction of groundwater reserves, with the risk of its complete depletion.

Of course, the optimum policy should be somewhere between these two extremes. On these basis, the design of water use policies can be viewed as the problem of maximizing the revenues generated by the exploitation of water resources in such a way that those resources be suitable safeguarded for the long term.

The overall purpose of the DSS designed within the GESMO project is to provide a simulation tool for helping to solve that problem to the Eastern Mancha Irrigation Board, both with a short- and a long-term horizon, thus also helping them to better negotiate with the Ju´car’s Hydrographic Confederation the water restriction policies to be applied.

More detailed objectives are:

1. Adapt the general US Geological Survey (USGS) Modular Three-Dimensional Finite-Difference Ground Water Flow (MODFLOW) model to a broader architecture, substituting the input files for a global database and designing a simple Windows-based input – output interface.

2. Design a general aquifer recharge model based on the historical rainfall and the levels of water in the Ju´car river.

3. Use crop transpiration and irrigation models to calculate the demand of water for any crops map of the target area.

4. Design an econometric model to dynamically determine crops maps from input variables that specifically includes the water quota.

5. Design an econometric model to calculate crop yields from specific input variables.

6. Design an econometric model to forecast shortterm crop prices from its historical values.

7. Integrate all these elements in a global DSS able to evaluate complex climatic, regulatory and economic scenarios as a whole. Design different tools which can be used to evaluate these scenarios both for the short and the long term.

The global system architecture is shown in Fig. 1.

The database includes all the numerical information for models and scenarios and the information obtained when each one is executed.

The sectorial economic impact subsystem is composed of several models. Their goal is to dynamically determine, on the basis of water availability (quota), some agricultural policies (subsidies, setaside rates) and also of the average piezometric level (determined by means of the hydrogeological impact subsystem), the regional gross product of crops (gross output less gross input) every year up to a target year. Such models are built on the basis of econometric techniques.

![](/api/attachments/JHU9SVZD/fulltext/images/72db4304cfb3097dbff51e0269502f930dfa740b028baf8d8e3e54c9dfb749bb.jpg)  
Fig. 1. Global system architecture.

The hydrogeological impact subsystem simulates the evolution of the aquifer up to the target year depending on the meteorology specified in the scenarios and the crops map determined in the sectorial economic impact model. The result is, for each year, the map of the average water depth saturated layer (measured by the piezometric levels) of the aquifer in accordance with the grid specified when defining the system.

The auxiliary subsystem helps to integrate the results of both previous subsystems to configure scenarios and to automatically generate new ones. Additionally, the auxiliary subsystem allows automatica sensitivity analysis of selected parameters. It also enables the showing simulation results in different formats (tables and graphics).

The user interface serves to define and store scenarios and also to select the analysis tools of the system to be used.

The structures of the hydrogeological and the sectorial economic impact subsystems are very different.

The former is based on finite differences and is a geographic numerical model able to represent piezometric levels. The second is set of a statistical/econometric equations to model prices, yields and land allocation trends.

## 3. Hydrogeological impact subsystem

The global scheme of this subsystem is shown in Fig. 2. The hydrogeological model is based on the MODFLOW system, developed by the USGS (http:// www.water.usg.gob/software), which is widely used in the world of hydrogeology. This software is freely available.

The MODFLOW model calls for the definition of a grid with the physical characteristics of the aquifer and also the matrices that essentially represent the current water levels and any additions and removals that are to be made. The model returns a matrix with the updated water levels. The subsystem compute the flow matrices on the basis of the scenarios entered by the user. The results are transferred to the database and from there to the interface. All the numerical data are stored in the database.

![](/api/attachments/JHU9SVZD/fulltext/images/cec99bcbaf60a1a4aa86fd484020b882b24ec08f413fa500a826b271e92dc20f.jpg)  
Fig. 2. The hydrogeological impact subsystem.

There are two complementary submodels in the hydrogeological impact subsystem. The first one is the weather-based forecasting model, which assists in estimating annual recharges to the aquifer and expected evapotranspiration based on exogenous information referring to expected temperatures and rainfall, both supplied to the system as qualitative terms (low, medium or high). These options are associated to percentiles calculated from the historical series stored in the database. Another datum considered is the expected flow of the Ju´car river, which can also be configured for each year on the basis of similar options.

The second complementary model is the consumption model, which calculates the water consumed, during its vegetative cycle, by the crops included in a given crops map. It follows a model proposed by the FAO [6]. The total consumed calculated with the consumption model, less the water supplied by the precipitation and by the river, is the total demand to the aquifer.

## 4. Sectorial economic impact subsystem

This subsystem is built by means of the specification, empirical estimation and validation of relationships for the trends of those variables involved in the determination of the regional gross product of crops. For the subsystem to be used in short-term analysis, it will need the following main exogenous control variables:

1. The irrigation quota allocated to the region.

2. The main agricultural policy instruments being in force (subsidies and set-aside rates).

3. Local meteorology.

4. The cost of certain production inputs.

5. The average piezometric level of the aquifer (this variable is the nexus with the hydrogeological simulation model).

For the sectorial economic impact subsystem to be used in long-term analysis, crop prices must also be supplied exogenously.

The scheme of the sectorial economic impact submodel is shown in Fig. 3.

There are four submodels into this subsystem.

## 4.1. The land allocation model

The purpose of the land allocation model is to represent the impact of the implementation of a given irrigation quota $\mathcal { Q } _ { t }$ on the distribution of crops into the region at issue. The model acts as a dynamic simulation tool of the surface allocated to each crop and is based on scenarios which are defined by a set of control variables including $\mathcal { Q } _ { t }$ and the average piezometric level $\lambda ,$ which is used as a proxy variable of electricity costs. The model ensures that the total water consumption equals $\mathcal { Q } _ { t }$ for each and every t.

Appendix A gives a brief mathematical description of the land allocation model.

## 4.2. The yields model

This model represents crop yields and is mainly based on meteorological variables. These are provided by the scenario generation model which in its turn takes results from the weather-based forecasting model.

The yields model consists of a set of statistical equations which are briefly described in Appendix B. Given that these equations use a time trend as explanatory variable, the yields model is not used for simulations which try to reach stationary or equilibrium states of the system. In that case, average yields of the historic period, stored in the database, are taken as constant values.

![](/api/attachments/JHU9SVZD/fulltext/images/019cd027709c6f9a43dbad71e9ddd7a265acd3c2785736140d73b0ebe035765d.jpg)  
Fig. 3. Sectorial economic impact subsystem.

## 4.3. The prices model

The limited scope of the area to which this work is applied imposes certain restrictions concerning the methodology to be employed for modelling prices. Farmers do not limit themselves to selling in markets within their own province. Commonly, they will trade in surrounding markets as well, as long as the prices offered are appealing enough. Similarly, farmers of other regions may come to the local markets when it is advantageous for them to do so. Thus, the physical productions corresponding to the province of Albacete (those which exclusively can be reproduced by the DSS) are likely to provide only very limited information with regard to the prices perceived by the farmers of the region. This turns out to be an impediment for the estimation of prices by means of inverted demand models, in which prices are mainly dependent on physical productions. Hence, ARIMA models [3] were used instead, which allow for predictions based only on data series concerning the prices observed in the past.

The prices model is conceived to provide shortterm forecasts of the prices relevant to farmers. In this way, the prices model is not used when there is a need of long-term simulations of the system. In that case, prices are supplied exogenously. Anyway, both for the short- and the long-term horizon, there exist the option to use institutional prices as expected prices of those crops which have regulated markets.

## 4.4. The gross product model

The regional gross product of crops is estimated as

$$
\mathrm{GP} _ {t} = \sum_ {i} s _ {i t} y _ {i t} p _ {i t} - \mathrm{EI} _ {t} - \mathrm{OI} _ {t}
$$

where $s _ { i t }$ is the surface allocated to crop i in $t ; y _ { i t }$ is the yield of crop i in $t ; p _ { i t }$ is the price of crop i in $t ;$ EI is the regional electricity cost. OI are other regional input cost.

The regional cost of electricity has been statistical ly related to the average piezometric level. Other input costs are taken as fixed and equal to its average historic values.

The accumulated gross product along a period of time is also calculated in this model

$$
\mathrm{AGP} _ {T} = \sum_ {t = 1} ^ {T} \mathrm{GP} _ {t}
$$

All the quantities of this model are corrected for inflation.

## 5. The auxiliary subsystem

As can be seen in Fig. 4, this subsystem is formed by three modules.

## 5.1. The scenario configuration module

This module creates the files which constitutes the input for every simulation of the system. For instance:

it transforms those scenario directives specified by the user which needs to generate numerical parameters, as is the case for qualitative concepts as High/Medium/Low;

it calculates an average piezometric level of the aquifer from the output of the hydrogeological impact subsystem to serve as input for the sectorial economic impact subsystem;

it allocates the regional crops map which is calculated by the economic subsystem to each of the spatial units of the hydrologeological model.

The scenario configuration model also stores the scenario information in the database.

## 5.2. The sensitivity analysis module

This module interacts with the previous one and forces the iterative execution of the system changing the value of some critical parameter on every repetition according to the range and increments specified by the user.

## 5.3. The scenario analyser module

This module helps to present final results by means of synthetic tables and graphics. It also finds the steady states of the system when equilibrium simulations are invoked.

![](/api/attachments/JHU9SVZD/fulltext/images/c1c150a1b307fc103a109f55f8bc8b43c137ab32af0d5d842c1d14ef05d8b5bd.jpg)  
Fig. 4. The auxiliary subsystem structure.

## 6. System implementation and general insights of its application

The system has been implemented in Visual Basic. The associated Access database stores the persistent data of the models and the configuration parameters. Specific data of the scenarios are stored in external files.

The interface module have a tree structure which is shown in the left part of the screen in a Windows Explorer-like appearance. It is linked to a set of screens used to configure the scenarios, to execute a simulation or a sensitivity analysis and to show the obtained results. The system have a total of 18 windows and 5 kinds of printed reports.

The system is now in regular use by the technicians of the Eastern Mancha Central Irrigation Board, together with other GESMO products corresponding to 1999. Using it, they can determine, for different defined scenarios, the water quota which reports the maximum revenue also ensuring the sustainability of the aquifer. The results obtained are used to negotiate with the Jucar’s Hydrographic Confederation the final water quotas for each agricultural year to be applied.

The system has shown long-term steady states for all of the simulations aimed to find equilibrium. This is a very interesting result which means that both gross product and piezometric levels of the aquifer can find long-term stationary values. The reason is found in that as far as the aquifer exploitation increases up to some point, pumping becomes so expensive that gross product starts to fall thus making exploitation to go back.

The existence of the steady states must be taken carefully: The long-term equilibria of the system can be an overexploitation point, that is, a stationary empty aquifer. This result is effectively obtained with the system under certain intensive scenarios of exploitation.

In addition, the curve drawing the steady-state gross products obtained for different values of the quota shows a maximum. This way, the value of the quota corresponding to that maximum could be taken as the desirable long-term policy whenever the corresponding steady-state piezometric level be enough to ensure the sustainability of the aquifer.

An interesting additional analysis which can be performed with the system consists in comparing the mentioned long-term gross product curve with a similar one estimated for a short-term forecasting scenario in order to explore the differences between what would be desirable from short- and long-term points of view.

The application of more sophisticated water policies (stationary quotas, combinations of surface and underground endowments for irrigation, etc.) cannot be evaluated with the actual system and is an intended future developments.

Appendix C shows an example of utilisation of the system.

## 7. Conclusions

The system designed amounts to an innovation in the field of decision support systems for managing water resources. Its main feature is that it combines hydrogeological criteria with the economics of the agricultural sector, the biggest loser of the water restriction policies, in a joint tool that can be used to analyse those two important aspects under both short- and long-term scenarios.

The system has been validated by and delivered to the Eastern Mancha Central Irrigation Board, where it is used to plan the agricultural year and design irrigation policies, which are then submitted to the Hydrographic Confederation of the Ju´car.

The plan is to evolve the system in order for it to admit a wider range of water resource management measures (transfers, collection of surface water, recharging pools, etc.) and also to re-estimate the econometric model with recent data already corresponding to the post-quota period. A more accurately model for the trend in the costs of production, introducing advances in irrigation technology, is also desired.

The Spanish National Hydrologic Plan (2001) introduces deep changes in the water management at national level with a decisive influence in the Eastern Mancha aquifer. The main innovations include the transfer of water among different basins, a new use of superficial water, new government regulation of irrigation system, supporting the increment of the irrigation efficiency, etc. This new framework ask for a significant evolution of the system in order to support these new scenarios of water policies, far more complex than the old ones. The inclusion of multiple variables and concepts in that future version of the system would lead to the implementation of a multivariable–multicriteria meta-model to guide the choosing of alternatives in a single scenario, increasing the value added of the system.

## Acknowledgements

This research was funded by the Science and Technology Committee within the National Programme of Water Resources (CYCIT, HID 96- 1373).

## Appendix A. The land allocation submodel

The development of this tool was devised before the quota policy was put into effect. This posed a serious difficulty, because while the tool is intended to evaluate likely responses during the post-quota period, its parameters could only be estimated based on information from the pre-quota period. This way, the option finally adopted to solve this difficulty must be seen as a provisional one waiting for the availability of enough statistical data corresponding to the post-quota period.

For the pre-quota period, it is possible to estimate econometric relationships of the form

$$
\lambda_ {i t} = \frac {S _ {i t}}{\sum_ {1} ^ {n} S _ {i t}} = \varphi_ {i} (A _ {t}, S _ {t}) \quad i = 1, \dots , n\tag{1}
$$

where $s _ { i t }$ is the surface allocated to crop i in $t , A _ { t }$ is an n-dimensional vector in which each element $a _ { i t }$ measures the attractiveness of crop i in t and $S _ { t } = \sum _ { i } s _ { i t }$ This system of equations explains how the fractions $\lambda _ { i t }$ change over time in terms of relative changes in the attractiveness of each crop and the availability of cultivable land.

Multiplying each $s _ { i }$ in Eq. (1) by $\nu _ { i } ,$ the average unitary needs for each crop, yields

$$
f _ {i t} = \frac {v _ {i} S _ {i t}}{\sum_ {i} v _ {i} S _ {i t}} = \psi_ {i} (A _ {t}, Q _ {t} ^ {*}) \quad i = 1, \dots , n\tag{2}
$$

$q _ { i } = \nu _ { i } s _ { i t }$ is then an estimate of the annual water-need of the surface $s _ { i t }$ and $\begin{array} { r } { Q _ { t } ^ { * } = \sum _ { 1 } \nu _ { i } s _ { i t } } \end{array}$ is the estimate of total regional water-needs. Here, water-needs are used as proxies of water consumption assuming that farmers of the region supplied water to crops accordingly (before the application of quotas). Once each $\nu _ { \mathrm { i } }$ is known, the $\psi _ { i }$ functions can be estimated for the prequota period.

In this way, $\hat { f } _ { i j }$ is an estimate of the fraction that $q _ { i }$ represents over ${ { Q } _ { t } } ^ { * }$ and the $\psi _ { i }$ functions reflects decisions about the allocation of those (estimated) water consumption fractions which are related to the attractiveness of crops and ${ { Q } _ { t } } ^ { * }$ . For forecasting concerning the post-quota period, $\boldsymbol { \mathcal { Q } _ { t } ^ { * } }$ will be substituted by $\mathcal { Q } _ { t }$ and, given a scenario $\boldsymbol { A } _ { t } ^ { \mathrm { { o } } } ,$ the estimate of $s _ { i t }$ will be

$$
\hat {s} _ {i t} = \frac {Q _ {t} \hat {f} _ {i t} (A _ {i t} ^ {\mathrm{o}} , Q _ {t})}{v _ {i}} \qquad i = 1, \ldots , n
$$

The model uses functional forms which ensure, for every $t ,$ the additivity restrictions

$$
\sum_ {i} \hat {f} _ {i t} = 1 \quad \hat {f} _ {i t} \geq 0 \quad \forall i
$$

This is achieved with the multinomial extension of the logit model, [9], which is extensively employed in surface-allocation models [1,2,4,8,10]:

$$
f _ {i} = \frac {\exp (h _ {i} + \varepsilon_ {i})}{\sum_ {j} \exp (h _ {j} + \varepsilon_ {j})} \quad i, j = 1, \dots , n
$$

where

$$
h _ {i} = \alpha_ {i} + \sum_ {k} \beta_ {i k} \log x _ {k} \quad i = 1, \dots , n\tag{3}
$$

$x _ { k }$ represents explanatory variables, mainly returns (prices times yields), subsidies, set-aside rates and the average piezomatric level, $\varepsilon _ { i }$ represents random shocks and $\mathsf { \mathfrak { X } } _ { i }$ and $\beta _ { i k }$ are unknown parameters.

The model is completed by including lagged dependent variables:

Restricted dynamic specification: $n - 1$ dependent variables are included in every equation (3); each of them lagged one period. This specification is similar to that of the partial-adjustment generalized model [7].

n Unrestricted dynamic specification: the own dependent variable is included in every equation (3), but lagged one period. This specification is similar to the well-known simple partial-adjustment model, or Nerlove’s model.

The data employed to estimate this model are annual and correspond to the period 1973– 1998.

## Appendix B. The yields model

In order to estimate the yield by hectare for each crop $i ,$ a regression equation with the following specification has been estimated

$$
y _ {i t} = \mu_ {i} + \alpha_ {i} t + \beta_ {i} (h _ {t} / p _ {i t}) + \delta_ {i} s _ {i t} + \gamma d _ {i t} + \varepsilon_ {i t}
$$

where $y _ { i z } = \mathrm { y i e l d } , \ s _ { i t } = \mathrm { s u r f a c e }$ $h _ { t } { = } \mathrm { f e r t i l i z e r s } ^ { { \prime } }$ price index, $d _ { i t } \colon$ = meteorological dummy variable, $p _ { i t } \mathrm { = }$ = price and $\varepsilon _ { i t } =$ random shock.

The linear trend must capture the effect arising from the employment of new seeds and production technologies. The quotient between the fertilizer’s price index and the price obtained by farmers takes into account the relative profitability of that important production input. The cultivated surface should capture the effect due to the allocation of crops to soils of different qualities.

The meteorological dummy variables would capture the effect of climate and meteorological factors on yields. Usually, taking these important factors into account implies two difficulties:

n meteorological data loses statistical significance when aggregated over space and time;

n it is usually necessary to include a larger number of meteorological explanatory variables in the equations. This is due in part to the above consideration, but also because of the large number of meteorological factors to be considered and the different seasons of the year in which they can have an impact on the crops.

The approach which relies on dummy variables, also used by the CARD/FAPRI model [5], avoids both difficulties. The $d _ { i t }$ variables take on a value of 1 for those years in which observed yields are considerably high (assuming that this is due to very good meteorological conditions). Likewise, they take on a value of - 1 when yields are exceptionally low and a value of zero for normal years.

The classifications of yields as ‘‘high’’, ‘‘normal’’ and ‘‘low’’ are suitably related to the estimated standard deviation of regression equations of the type

$$
y _ {i t} = a _ {i} + b _ {i} t + v _ {i t}
$$

Thus, a single variable expresses both positive and negative meteorological effects. In this way, it is easy to project these variables for long-term simulations: If normal climate conditions are to be simulated, a value of zero must be projected; to simulate good or bad climate conditions, the values 1 or - 1, respectively, must be used.

Estimations have been done using annual average data series belonging to the province of Albacete and covering the period 1973 –1998.

## Appendix C. Sample of execution

The following sample shows a summary of the execution of an analysis with the system. Fig. 5 shows the main window of the system. The sub-windows are organised in a tree structure shown at the left side of the screen. At the right, the system presentation appears with the participants in the GESMO project.

In this example, the system will run a dynamic simulation starting in 1974 and ending when all the variables reach stationary values. In analysis not trying to reach equilibrium, simulations will end in the year specified on the screen of Fig. 6. All the input data provided exogenously to the system (which are shown in the following screens) are held constant from the last value stored in the database until the end of the simulation. If the staionary values of variables were not found, an error message is shown

Fig. 7 shows some of the hydrogeological input data:

n The qualitatively expected temperature and rainfall. With this information, the system calculates meteorological expected values taking into account the average and percentiles of the data stored in the database.

n Not agricultural water consumption (hm<sup>3</sup>/year) and average efficiency of the irrigation system (%) for each area of the hydrologic model. This information is used to calculate the total volume of water extracted in each subarea of the aquifer.

Fig. 8 shows the scenario for the economic submodel. For prices, it is possible to choose between the use of exogenous prices or the use of forecasting obtained with the prices model. It is also possible to use the institutional prices as estimations of those prices of crops whose market is regulated. Another inputs are compensatory payments, set-aside-rates, annual variations of the retail price index and irrigation quota.

In the screen of Fig. 9, the fenologic states (biological states) of each crop are introduced with the average dates of development of each state. Below, for the selected crop, the curve of water needs during the crop life is represented. This information is used to calculate the global agricultural water needs.

The screen of Fig. 10 allows the user to execute the scenario, showing the degree of advance.

![](/api/attachments/JHU9SVZD/fulltext/images/615d9aa774ea9f1aaba474f84321258b18868e7c054e1f183531041fb72287d9.jpg)  
Fig. 5. Main system window and introductory titles.

Fig. 11 shows the stimulated hydrogeological levels and compared it with those of the previous year.

Fig. 12 shows the estimated statistical crops map, the production expected for each crop and its gross value.

Fig. 13 shows the integrated results of the system corresponding to the simulated scenario and its variations to those of the last year of simulation. Given that the example corresponds to an equilibrium simulation, the variables remain stationary and all of those variations are zero.

![](/api/attachments/JHU9SVZD/fulltext/images/d473ca67ba8a39cf38b48305052921947037046e5d1975ed45cd69a34f10c3ad.jpg)  
Fig. 6. Input data: simulation year.

–Input data

Fig. 14 shows the screen for the configurations of a sensitivity analysis. The graphic shows the steadystate values of the regional gross product and piezometric level of the aquifer obtained for the specified values of the quota.

For the scenario established to get this graphic, the desired value of the quota would be around 3600 m<sup>3</sup>/ ha/year as average. That quota leads to the maximum gross product of crops also ensuring the sustainable conservations of the aquifer.

Of course, that curves would vary if the scenario were altered. The system let to explore the variations of the desired quota calculated under different situations. It is also possible to draw that kind of curves not for the equilibrium values, but for the expected nextyear scenario. The comparison of the long-term and short-term quotas is an interesting index in order to find suitable water management decisions.

Translation of texts in figures:

Fig. 5 left (also valid for the following figures):

–Run a simulation

–Results

– Sensitivity analysis

– Print reports

Fig. 5 main window:

‘‘The Integrated Model for the Assessment of Hydrological Politics has been developed by the Department of Mathematics Applied to Agricultural Engineering within the GESMO project, in collaboration with the University of Castilla-La Mancha, the Eastern Mancha Central Irrigation Board and the Provincial Technical Agronomic Institute of Albacete.’’

Fig. 6 left: The input data options are:

– Input data

<sub>o</sub> Hydrogeological data

<sub>o</sub> Economic data

<sub>o</sub> Fenological states (biological states)

Fig. 6 main window:

‘‘Configuring the year for the simulation. The year for the simulation is shown in the edition square. To change it simply type the new year and click on the ‘‘modifying period’’ button. Choose for a simulation to equilibrium: yes (.), no’’.

![](/api/attachments/JHU9SVZD/fulltext/images/1945015cfa7d0f675f3a0587401260fe35f63e1da4ca94f1aba4bb27c5d759e2.jpg)  
Fig. 7. Input data: hydrogeological data.

![](/api/attachments/JHU9SVZD/fulltext/images/e84fa4255ad85ffbc533d99587f7dfba7eb13a9576a8d76ec6e58da8fab5f83d.jpg)  
Fig. 8. Input data: economic data.

Fig. 7 main window:

‘‘Hydrological data. Temperature: High, Medium, Low. Precipitation: High, Medium, Low. Non agricultural volume consumed (hm<sup>3</sup>). Irrigation efficiency (%).’’

Fig. 8 main window:

‘‘Economic Data. Use the prices model ( ). Introduce prices (.). Use institutional prices ( ). Prices of the crops: sunflower, barley, etc. Compensatory payments of the CAP (European Common Agricultural Policy): set aside, sunflower, cereals. Set aside rate (10%). Annual rate of variation of the retail price index (2%). Irrigation quota (3415 m<sup>3</sup>/ha/an¯o).’’

![](/api/attachments/JHU9SVZD/fulltext/images/fc9ca6fbbfdb5d3e6cfe494e6e5b60a9f6fb040aa1075b2e9dd3172914f4191b.jpg)  
Fig. 9. Input data: crop fenologic states and calendar.

![](/api/attachments/JHU9SVZD/fulltext/images/4340cd5f0a08dd8d66010363b5897edc247ec11af748516e6b10f7bb7482f5fd.jpg)  
Fig. 10. Scenario execution window.

![](/api/attachments/JHU9SVZD/fulltext/images/d9d0a8feb321368fdf7c507166479321d63026fea4f36e81e28570ed5631818e.jpg)  
Fig. 11. Results obtained: hydrogeological simulated data.

![](/api/attachments/JHU9SVZD/fulltext/images/1dbf2b7b41f2d6baa405ced0bfb51077e8b90ad8e5e7cf36037c7fccdc6c7398.jpg)  
Fig. 12. Results obtained: economic data.

Fig. 9 main window:

‘‘Fenologic states. Barley 2000/2001. Insert. Vary. Delete. Period: initial, development, reproduction. Fenelogic state: initial little plant formation, etc. Date.’’

![](/api/attachments/JHU9SVZD/fulltext/images/162296a40b012429ae73a11032ef5291399bf37bb200155df37b4c16cb210e5b.jpg)  
Fig. 13. Results obtained: integrated results.

![](/api/attachments/JHU9SVZD/fulltext/images/b3fcc187cbd1644b487ab366d9f1d232791701d9f0ab2a812018b76cb8c1e5ba.jpg)  
Fig. 14. Sensitivity analysis.

Fig. 10 main window:

‘‘Run a simulation. Run the model. Cancel the simulation. Status of the execution.’’

Fig. 11 left: The results options are:

–Results <sub>o</sub> Hydrogeological results Economic results <sub>o</sub> Integrated results

Fig. 11 main window:

‘‘Hydrogeological results. Select hydrogeological area. Height of the piezometric level of the aquifer (meters over the sea level) and depth (meters). Zone. Height Depth of the previous year. Simulated depth. Variation (%)’’

Fig. 12 main window:

‘‘Economic results. The following table shows the surfaces in ha, the productions in kg/ha, the prices in o/kg and the monetary outputs in o of each crop. Crop: wheat, barley. . . Surface (ha): 1935. . . Production (kg/ha): 1986.084. . . Price (o/kg): 0.05. . . Output (o): 185009.62. . .’’

Fig. 13 main window:

‘‘Integrated results. The following table shows the general results of simulation. Height. Depth. Total output. Total gross product. Total area. (Value; % Variation to the last year)’’.

Fig. 14 main window:

‘‘Sensitivity analysis. Select the parameter for the sensitivity analysis (irrigation quota). Range of values (2500 – 4250). Increments (250). Target variables (Gross product; Piezometric level). Name of the simulation (Ejemplo). Get a graphic for the results. Results of the simulation ‘‘Ejemplo’’. Equilibrium values for different quotas’’.

## References

[1] P.F. Allanson, The Manchester Policy Simulation Model of U.K. Agriculture (Main Report), Department of Agricultural Economics, Faculty of Economic and Social Studies, University of Manchester, Manchester, 1988.

[2] R. Bewley, T. Young, D. Colman, A system approach to modelling supply equations in agriculture, Journal of Agricultural Economics, 38 (2) (1987) 151– 166.

[3] G.E. Box, G.M. Jenkins, Time Series Analysis: Forecasting and Control, Holden Day, San Francisco, 1976.

[4] M.P. Burton, An Agricultural Policy Model for the U.K., Avebury, Aldershot, 1992.

[5] CARD, Fapri modelling system documentation, Center for Agricultural and Rural Development. Iowa State University, Comunicacio´n al curso ‘‘Modelos Cuantitativos Econo´micos

en Agricultura’’. Instituto Agrono´mico Mediterra´neo de Zaragoza, May 8 to June 2 (1989).

[6] FAO, Irrigation and drainage paper no. 56: ‘‘Crop evapotranspiration’’, Drainage paper no. 24: ‘‘Crop water requirements’’, Drainage paper no. 33: ‘‘Yields response to water’ (1999).

[7] B.F. Hunt, M.R. Upcher, Generalized adjustment of asset equations, Australian Economic Papers, 18 (1979) 308 – 321.

[8] J. Iban˜ez, C. Pe´rez, Impactos de la reforma de la PAC de 1992 sobre el subsector agrı´cola espan˜ol, Revista Espan˜ola de Estudios Agrosociales y Pesqueros 185 (1999) 1 –9.

[9] A. Theil, A multinomial extension of the linear logit model, International Economic Review, 10 (3) (1969) 251–259.

[10] H. Wolfgarten, Supply component of SPEL model, in: S. Bauer, W. Henrichmeyer (Eds.), Agricultural Sector Modelling, Wissenschaftsverlag Vauk Kiel, Germany, 1989, pp. 385 – 390.

Beatriz Recio is a professor in the Department of Mathematics and Information Technology applied to Agricultural Engineering of the Polytechnic University of Madrid. His research interest include farm management, management information systems, and decision support systems.

Javier Iba´n˜ ez is s professor of the Department of Statistics and Management Methods in Agriculture of the Polytechnic University of Madrid (High Technical School of Agricultural Engineers). Since 1990 her main lines of research are the elaboration of dynamic simulation models. The main methodologies employed are econometrics and system dynamics. The main areas of application are the management of groundwater aquifers, the European Common Agricultural Politics and desertification.

Fernando Rubio is a PhD in Computer Science. He have been involved in all his proffesional career in advaced system implementations in areas as transportation, industry and bussiness. He have been working as manager for the EEC and firms as Texas Instruments and Andersen Consulting to provide advanced techonoly solutions. In the current he teachs bussiness and computing and maintain a fruitfull research line in the UPM. His research interest include e-commerce and decision support systems.

Jose Antonio Criado is now finishing his PhD in Intelligence Decision Support System for Farm Planning. His primary scientific interest lie in the application of Internet to support Decision Support Systems in agriculture.
