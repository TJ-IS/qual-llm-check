---
otero_id: 9774
otero_key: "XVHWZTMN"
title: "Modelling decision support and uncertainty for large transport infrastructure projects: The CLG-DSS model of the Øresund Fixed Link"
authors: "Kim Bang Salling; Steen Leleur; Anders Vestergaard Jensen"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.06.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Systems 43 (2007) 1539– 1547

www.elsevier.com/locate/dss

# Modelling decision support and uncertainty for large transport infrastructure projects: The CLG-DSS model of the Øresund Fixed Link

Kim Bang Salling <sup>⁎</sup>, Steen Leleur, Anders Vestergaard Jensen

Centre for Traffic and Transport, CTT-DTU, Build. 115, Technical University of Denmark, DK-2800 Lyngby, Denmark

Accepted 9 June 2006 Available online 28 July 2006

## Abstract

This paper presents a decision support system, named the CLG-DSS model, which makes it possible for decision makers to assess various uncertainties in project appraisal in a systematic and explicit way. This model, a decision support system (DSS) developed within the Danish Centre for Logistics and Freight Transport (CLG) is based on cost-benefit analysis (CBA) embedded in a wider multi-criteria analysis (MCA) by the use of some principles for composite modelling assessment (COSIMA). The CLG-DSS model is set up to make use of scenario analysis (SA) and Monte Carlo simulation (MCS). A particular concern in the model is the handling of varying information across the assessment criteria and the application of SA to inform the MCS parameter setting. After the presentation of the modelling principles some ex-post case calculations for the Øresund Fixed Link are illuminating different aspects of appraisal uncertainty and thereby, at the same time, demonstrate the features of the CLG-DSS model as a useful decision support tool. It is finally concluded that appraisal of large infrastructure projects can be effectively supported by dealing with uncertainty issues in accordance with the principles described. © 2006 Elsevier B.V. All rights reserved

Keywords: Cost-Benefit Analysis; Multi-Criteria Analysis; Scenario Analysis; Risk Analysis; Monte Carlo Simulation; Decision Support System

## 1. Introduction

The purpose of this paper is to present the CLG-DSS model with emphasis on its potential for dealing with uncertainty issues relating to the appraisal of major transport infrastructure projects. The model is developed as a decision support system (DSS) and as one of several research tasks in the Danish Centre for Logistics and

Freight Transport (CLG). It has been used to make an ex-post appraisal study of the Øresund Fixed Link which opened in July 2000. The Øresund Fixed Link is a 20 km long bridge connecting Copenhagen with the southern part of Sweden–Skåne. It is, however, foreseen that the CLG-DSS modelling principles can be used for other purposes such as, for example, up-coming ex-ante appraisal studies for other European major transport infrastructure projects and even for assessment tasks in other societal sectors due to the generality and flexibility of the model.

The paper is organized as follows: After this introduction Section 2 presents some principles for composite modelling assessment (COSIMA) while Section 3 gives an overall description of the CLG-DSS model together with a presentation and discussion of the different model components and the methodological principles and theories that underpin them. The model basically consists of a cost-benefit analysis (CBA) embedded in a multicriteria analysis (MCA) where the latter is calibrated by making use of weights made up similar to the standard prices of the CBA. A computable general equilibrium (CGE) model for the Øresund Region is applied to calibrate the MCA model.

An important feature described in Section 4 is the linking of scenario analysis (SA) with Monte Carlo simulation (MCS). A particular concern has been to apply available assessment information in the best possible way, as collection of extra data and estimation of more precise parameters in many cases turn out to be relatively expensive study costs. By approaching the uncertainty issues involved in transport infrastructure appraisal, it becomes possible for the decision-makers assisted by the model to follow in an explicit and straightforward way how uncertainty issues can be dealt with. This is demonstrated in Section 5 by a number of different model runs. The results are discussed and interpreted to give an indication of how decision-makers can be supported by making use of the different aspects of uncertainty handling.

Finally, Section 6 presents some conclusions and gives a perspective on the further work on the development of the model.

## 2. Principles for composite modelling assessment (COSIMA)

The idea behind COSIMA is to extend conventional CBA into a more comprehensive type of analysis — as often demanded by decision-makers — by including “missing” decision criteria of relevance for the actual assessment task. The missing criteria often address issues that have been difficult to assess by the conventional CBA but hold a potential of improving actual decision support from the assessment if treated properly. This is the purpose of COSIMA where the added criteria will be referred to as the MCA part of the COSIMA analysis.

In brief, COSIMA consists of a CBA part and a MCA part and the result of a COSIMA examination is expressed as a total value (TV) based on both parts. This model set-up emphasizes that the MCA part should be truly additive to the CBA part for which reason an activity, project or initiative $A _ { k } ,$ is better represented for a decision support purpose by $\mathrm { T V } ( A _ { k } )$ than by the net present value of benefits (NPV) from the CBA, here referred to as $\mathrm { C B A } ( A _ { k } )$ . Thus the basic principle behind COSIMA can be set out by Eq. (1) below:

$$
\operatorname{TV} \left(A _ {k}\right) = \operatorname{CBA} \left(A _ {k}\right) + \operatorname{MCA} \left(A _ {k}\right)\tag{1}
$$

The formulation of COSIMA introduced by Eq. (1) thus resembles cost-benefit analysis but the assessment principles made use of in the MCA part — generally based on decision-maker involvement which is not made use of in CBA — justifies the denomination as multi-criteria analysis. It can be noted on the basis of Eq. (1) that in a situation where the investment in $A _ { k }$ equal to the investment cost $C _ { k }$ is not feasible seen from CBA, i.e. $\mathrm { C B A } ( A _ { k } ) { < } C _ { k } ,$ , then the investment can be justified by the wider COSIMA examination if $\mathrm { T V } ( A _ { k } ) { > } C _ { k }$ . If examined as a total rate of return (TRR), the latter can be expressed as $\mathrm { T R R } ( A _ { k } ) { > } 1$

In a COSIMA analysis applied in the CLG-DSS model, where $A _ { k }$ denominates the implemented infrastructure alternative k for the Øresund Fixed Link, it has in fact been convenient to express the feasibility by the total rate of return $\mathrm { T R R } ( A _ { k } )$ from the investment $C _ { k }$ which leads to Eq. (2) below:

$$
\begin{array}{l} \operatorname{TRR} (A _ {k}) \cdot C _ {k} = \operatorname{TV} (A _ {k}) = \sum_ {i = 1} ^ {I} V _ {\mathrm{CBA}} (X _ {i k}) \\ \quad + \alpha \cdot [ \sum_ {j = 1} ^ {J} w (\mathbf {j}) \cdot V _ {\mathrm{MCA}} (X _ {j k}) ] \end{array}\tag{2}
$$

where

$V _ { \mathrm { C B A } } \left( X _ { i k } \right)$ Value in monetary units for the CBA effect i for alternative k for altogether I CBA effects.

$V _ { \mathrm { M C A } } ~ ( X _ { \mathrm { j k } } )$ Value function for MCA criterion j for alternative k for altogether J MCA criteria.

α Calibration factor that expresses the specific model set-up's trade-off between the CBA and the MCA part.

$w ( j )$ A weight expressing the importance of criterion j.

The general COSIMA principles are presented by Eqs. (1) and (2). It can be realized that with sufficient information about the MCA part, Eq. (2) can be specified into a CBA. This will be the situation when, for example, a conventional CBA is carried out and is afterwards supplemented with some extra criteria. This can be specified fully by impact models that lead to net effects which can be given satisfactory unit prices similar to the assessment in the CBA part. Most often this will, however, not be possible as in general the MCA part will be “less known” than the CBA part. In fact the purpose of

COSIMA is to handle such a situation. In modelling terms this is done by the determination of appropriate values for α and $w ( j )$ for the J MCA criteria and by the determination of appropriate value functions $V _ { \mathrm { M C A } } \left( X _ { j k } \right)$ The latter supplement the determination of $V _ { \mathrm { C B A } } ~ ( X _ { i k } )$ that, however, can be derived from a CBA manual relevant for the actual assessment case.

In the CLG-DSS model — one specific application of COSIMA—the following specifications are applied for the CBA part [6]:

$$
V _ {\mathrm{CBA}} (X _ {i k}) = \sum_ {t = 0} ^ {T} D (t) \cdot \mathrm{UP} _ {i} (t) \cdot e _ {i k} (t)\tag{3}
$$

where

$e _ { i k } ( t )$ Net change for CBA effect i in year t with $t { = } 0 , 1 , . . . , T .$

$\mathrm { U P } _ { i } ( t )$ Unit price in year t (estimated growth in fixed price level can be accounted for).

D(t) Discounting factor $\left( 1 + r \right) ^ { - t }$ with r as discount rate.

Due to the availability of suitable effect models for strategic impacts, it has been chosen to formulate the MCA part of the CLG-DSS model in a way similar to Eq. (3) so the following specifications are applied:

$$
\alpha \cdot w (j) \cdot V _ {\mathrm{MCA}} (X _ {j k}) = \sum_ {t = 0} ^ {T} D (t) \cdot \mathrm{WP} _ {j} (t) \cdot e _ {j k} (t)\tag{4}
$$

where

$e _ { j k } ( t )$ Net change for MCA effect j in year t with $t { = } 0 , 1 , . . . , T .$

$\mathrm { W P } _ { j } ( t )$ Weight price in year t (estimated growth in fixed price level can be accounted for).

D(t) As in Eq. (3)

α and w( j) As in Eq. (2)

It should be noted that in the CLG-DSS application of COSIMA, Eqs. (3) and (4) differs principally by the prices they adopt, namely the standard unit prices and the weight prices. The latter are dependent on the actual values of α and $w ( j ) ,$ , see Eq. (2), and the idea of the CLG-DSS model is that appropriate weight prices can be determined by making use of computable general equilibrium (CGE) modelling for the actual examination case. Technically the set of weight prices in the CLG-DSS model is determined by the CGE–CBA difference treated by making use of different runs of the CGE calculation model [6].

## 3. Description of the CLG-DSS model

The Danish Centre for Logistics and Freight Transport's-Decision Support System (CLG-DSS) model concerns the development of a new evaluation methodology to be applicable within the area of logistics and transport. Given the complexity of this particular research task it has been decided to concentrate the model study on the Øresund Fixed Link as base case, i.e. as a kind of evaluation research laboratory.

The CLG-DSS model consists of two modules, a COSIMA-module [5] which is a module combining a CBA and a MCA, and a GAMS-module (General Algebraic Modelling System) using a CGE model. The interaction between the two modules shown in Fig. 1 makes it possible to combine a conventional CBA and CGE models which proves to be particularly useful to study the overall effects of transport projects (covering both the direct and indirect effects). Among other things, this makes it possible to provide assessment information for decision-makers in a straightforward and comprehensible manner. First, the decision-maker will get information about the impacts usually included in a CBA such as time savings, accidents, and vehicle operating costs together with the construction and operating costs. Second, CGE model results will identify the changes in welfare at an aggregated level and for the individual groups involved. This will identify the welfare changes for consumers and producers (from different economic sectors). In particular, the structure of CGE models is well-suited to address the impacts associated with enlargement of markets (effects on competition and productivity) and relocation of firms. It should be noted that the CBA outcome is likely to be different from the CGE outcome (unless perfect competition in the economy can be assumed).

The basic structure of the CGE model used for the specific Øresund Region is as follows. The economy is divided into four regions: The Greater Copenhagen area, the rest of Denmark, the Skåne region and the rest of Sweden. In addition, there is an external region to describe the trade between the four regions and the rest of the world. Each region includes a set of households, a bundle of labour, and capital used by regional firms for producing goods and services. Apart from production factor services, the firms are using intermediate goods in the production process. The firms can belong to one of three tradable goods sectors or to one non-tradable (local) goods sector. Furthermore, the sectors can be described via a number of different product types and services: agriculture, forestry and fishery products; manufactured products; market services and non-market services. Firms are free to compete in the market for a tradable product which already exists or to sell a new one not yet in the market. The optimal choice for the firm is to choose the latter option which means that only one firm will monopolistically supply each product. In this context the firm will set the price as a mark-up on costs. If the firm has a positive profit, new firms are attracted to the industry supplying new variants of the product such that the demand for each single product declines until profits are driven back to zero. Households are assumed to be utility maximizing in the spending of their total disposable income. Disposable income is assumed to come from returns on regional production factors (all production factors are assumed to be owned by regional households) and a net transfer payment from the rest of the world. Households can spend their income on goods (local and tradable) as well as on travel. Households gain utility from a set of activities connected with travel and suffer from disutility for spending travel time. This model setup allows calculation of the welfare changes as a result of the Øresund Fixed Link. The welfare changes can be calculated at an aggregated level as well as at disaggregated levels for Denmark and Sweden respectively.

![](/api/attachments/XVHWZTMN/fulltext/images/12af56ff21a69d29ebba16375738b548c39fd2e6f8f80577e9bcd6590fd07332.jpg)  
Fig. 1. The CLG-DSS model.

The CGE model work is in line with the research findings within the SACTRA work [1,8]. In particular, the model focuses on effects on the product market taking into account the possibility of imperfect competition within a multiregional economic system. In the COSIMA module, CBA is supplemented with MCA so that the MCA basically “interprets” the overall CGE–CBA difference. Due to the theoretical difference between CBA and CGE the decomposition of the CGE–CBA difference at this stage of the work is sometimes referred to as “pedagogical”. The further work will seek to illuminate these aspects more closely. Wider economic effects are included as the following MCA criteria: (I) Network and mobility, (II) Global emissions (CO ), (III) Employment, and (IV) Logistics and goods effects [1]. In this way it becomes possible to obtain an estimate of the socio-economic value of the wider economic effects as part of the modelling results. The general structure of the model work carried out in the CLG has been split into six different stages combining the various research results.

First, the principles behind the composite CBA and MCA modelling were determined. In the CLG-DSS model this is addressed by the COSIMA module. Some specifications were discussed in Section 2.

The second stage was a determination of the planning principles for the appraisal of large infrastructure projects such as the previously mentioned case for the Øresund Fixed Link and the Øresund Region.

In the third stage a determination of the so-called logistics and goods (LG) effects was treated on an aggregated level by consideration of four defined effects (frequency of shipments, changes in regularity, enlargement of the market, and relocation of production and/or warehouses). The LG-effects differ from the traditional CBA effects due to their nature as defined on company level. It is maintained that the CBA is well-determined both in literature and in practice whilst the wider economic impacts concerning companies are not similarly well-defined [5].

In the fourth stage the scenario work was developed. This stage is described more explicitly in the following Section 4.

The fifth stage concerns the model results based on both deterministic and stochastic model runs. The results are also discussed in the following sections with some illustrating examples.

The last stage of the CLG-DSS model work concerns the growth effects giving the interlinking of the COSIMA and the GAMS module for the Øresund Fixed Link case. Available theoretical and empirical findings support the hypothesis that wider economic impacts can be rather substantial, e.g. the English SACTRA work [8] has suggested that the true benefits (with inclusion of direct and indirect impacts) could be between 30% and 50% greater than the benefits calculated in a standard cost benefit analysis [9]. The problem, however, is that the magnitude of these (potentially) additional impacts can be determined only on a case-by-case basis. The modelling and the case relations give valuable information as concerns the level and composition of the socio-economic project value.

Aiming at working more closely with alternative development patterns, it has proven relevant to create a number of framework scenarios to interpret the economic growth in the region as well as at a European level.

## 4. Scenario analysis and Monte Carlo simulation

The technical modelling work carried out in the CLG-DSS model aims also at demonstrating that scenarios — in addition to their basic function showing alternative development patterns — can be made use of to influence the parameter settings in related model simulations.

The CLG-DSS model consists of 10 scenarios divided into 9 framework scenarios and 1 trend scenario.

All of the produced scenarios in the CLG-DSS work can be categorized as exploratory. Within these there are two sub-types of scenarios: framework and trend scenarios. The framework scenarios expand the possible range of outcome and try to elaborate various (extreme) scenarios while the trend scenarios try to elaborate a scenario which is affected by some particular development trend [3].

The scenarios in the study have been elaborated with respect to two regimes: A Regional/Local regime and a National/European regime. The Regional/Local regime describes how the integration within the Øresund Region is progressing and varies with high, middle and low integration, while the National/European regime deals with the more overall development in the remaining part of Denmark and elsewhere in Europe. This regime varies between a situation with deregulation, with regulation and sustainable development and a situation with stagnation and crisis. By combining these two regimes a total of 9 different framework scenarios can be produced as shown in Table 1.

The Deregulation regime (Scenarios 1, 2 and 3) is a situation where the market mechanism is in control. The European Union is here expanding with new member nations. Consequently, Europe has developed into a flexible and competitive region without trade barriers. The transport area has traditionally been a much regulated area but has through the 1990's undergone a shift towards more deregulation, e.g. road haulage, airlines, railways, and inland waterways. This trend is assumed to continue. The successful economy allows substantial investment in the European infrastructure. Furthermore, the development of technology is also making progress, which means that a possible lack of fossil fuels can gradually be remedied by new technology that allows the use of fuel cells and electrically driven cars.

The Regulation regime (Scenarios 4, 5 and 6) also implies an expansion of the European Union, but the market is more regulated and moves towards a more sustainable direction. In Europe agreements have been made regarding standards for speed limits, noise, emissions and land use planning. Road tax, fuel duties and road pricing contribute to a sustainable development. However, the introduction of new agreements is not achieved without problems and makes only slow progress. The environmental agreements imply that infrastructure investment has not been made to the same extent as is the case in the Deregulation regime. Furthermore, an adjustment of the tax system from taxing the income to taxing the use of natural resources, results also in more sustainable development.

Table 1  
The 9 different framework scenarios

<table><tr><td>∅resund region integration</td><td>Deregulation</td><td>Regulation and sustainable dev.</td><td>Stagnation and crisis</td></tr><tr><td>High</td><td>1</td><td>4</td><td>7</td></tr><tr><td>Middle</td><td>2</td><td>5</td><td>8</td></tr><tr><td>Low</td><td>3</td><td>6</td><td>9</td></tr></table>

The Stagnation regime (Scenarios 7, 8 and 9) assumes that the previous years' tendency of a weak economy will continue. The enlargement of the European Union is not working out in a smooth way. Unemployment continues to grow implying increased pressure on public resources. In general Europe experiences stagnation and therefore few infrastructure investments are made. The high demand on public expenditures implies that there are few resources left to deal with environmental problems. This is reflected in environmental policies that continue mainly based on already existing agreements, etc.

An additional scenario — Scenario 10 — is produced to make possible the modelling of an oil crisis. The tenth Scenario is referred to as a trend scenario based on Scenario 7, in which an oil crisis is modelled to take place around year 2015.

To incorporate the different scenarios in the CLG-DSS model it is necessary to estimate a scenario modelling parameter (the scenario factor S) for each effect. These Sestimates are made on the basis of the different development patterns that are embedded in each scenario. The scenario factor used in the COSIMA module varies around 1.00 where a value of 1.00 implies that the effect is not affected by the actual scenario. A value below 1.00 corresponds to the S-factor reduces the impact on the effect and a value above 1.00 increases the impact. Values varying from 0.67 to 1.15 have been used in the calculations presented in this paper. However, most of the effects vary from 0.85 to 1.15 with regard to the S-factor.

One of the main influences of the Regional/Local regime is the growth in traffic. Different growth rates have been estimated for both the car and train traffic. The growth in car traffic is illustrated on Fig. 2. In this case the growth has a big effect on the total evaluation of the project because the main benefits stem from the reduction in travel time. However, other impacts are also affected by the difference in the two regimes and these are explained in the following description of Scenario 1.

Scenario 1 is the most optimistic one. The economy in Europe and Denmark is generally in a good state. Within the Øresund Region the economy has developed towards a very strong economy. The integration between The Greater Copenhagen Region in Denmark and Skåne in Sweden has undergone a progressive development. This has resulted in the creation of an integrated region where people move across the border between Denmark and Sweden daily without noticing the differences. The region is highly competitive compared with other regions within the European Union.

![](/api/attachments/XVHWZTMN/fulltext/images/f78fc5aefe4c2e787d49426578ec8e4a41744533e042b3898cf912e64f1d9ce7.jpg)  
Fig. 2. The traffic growth on the Øresund Fixed Link for car traffic for the three regional/local regimes.

The effect is a perceived higher value of time for the travellers (both car and train travellers). This is due to the level of activity in the region. The value will increase after 2004 with a steady rate until year 2020 where the scenario factor (S) ends up with a value of 1.15. After 2020 the value of S is constant at 1.15. A progressive technology development results in a reduction of the number of accidents on the Øresund Fixed Link. This reduction is modelled with a fall in the scenario factor after 2004 until 2020 to a value of 0.95. Then the factor is set to 0.95 throughout the evaluation period.

The value of carbon dioxide (CO ) is reduced due to the expectation towards emissions which fail to appear and the technological development has also reduced the emission of $\mathrm { C O } _ { 2 }$ . The price per ton $\mathrm { C O } _ { 2 }$ emission is reduced rapidly after 2004 until a value of 200 DKK per tonne is reached in 2007. This is modelled with a scenario factor that takes on the value of 0.67 in 2007. The $\mathrm { C O } _ { 2 }$ price reflects USA and UK estimates, where $\mathrm { C O } _ { 2 }$ emissions are not considered as important as in continental European countries today.

Employment issues are affected such that the value of a new workplace is reduced. A new workplace value is based on a report from the former West Germany calculating the resources associated with creating a new workplace for the government [2]. The value is reduced because the economy produces many new workplaces and therefore the expenses associated with forming a new workplace are reduced. The value is reduced with the scenario factor that takes on the value of 0.95 in 2020. The high integration between Denmark and Sweden results in

3300 new workplaces. Because of the progressive development in the rest of Denmark and Europe there are created 100 new workplaces because of the Øresund Fixed Link. This gives a total of 3400 new work places [6].

The number of scenarios reflects the overall uncertainty. To handle the uncertainty involved within each scenario in the CLG-DSS model, Monte Carlo simulation (MCS) has been used including software @RISK applied as an add-on to the Excel-based CLG-DSS software [7,10].

The CLG-DSS model in its present version categorises information about study data and parameters into three levels of knowledge:

1. A relatively high level of knowledge is modelled by a normal distribution leaving the decision maker with the determination of a mean value and a standard deviation. An example is the use of this distribution for the travel time savings based on traffic flow modelling.

2. The middle level of knowledge is modelled by a triangular probability distribution leaving the user to determine a minimum, a most likely and a maximum value. The triangular distribution is furthermore characterised by higher flexibility as it is possible to work with open distribution tails defined by appropriate fractiles stating that some values exceed the previously defined range with a chosen probability. An example here is the employment effect based on regional economics studies.

3. The low level of knowledge is related to the uniform distribution, which as input only needs a minimum and a maximum value defining an overall range for the parameter value. An example here is the amount of local pollutants.

## 5. Model results

The CLG-DSS model results are divided into 2 groups based on the deterministic runs and on the stochastic runs. The results concerning the deterministic runs are presented as single value return rates representing the nine different framework scenarios. As an example Table 2 shows the result of framework scenario 1 representing a high integration in the Øresund Region combined with deregulation from the National/European regime.

The “Travel time etc.” result stems from the basic cost-benefit analysis stating that a benefit-cost rate above 1 is an indication of a socio-economically feasible project. This is, however, not the case in the given study from the Øresund Fixed Link. However, if the employment effect, one of the added MCA-effects is taken into account, a combined CBA and MCA rate is

Table 2

<table><tr><td>Travel time etc.</td><td>0.85</td></tr><tr><td>Network and mobility</td><td>0.11</td></tr><tr><td>Global emissions (CO2)</td><td>0.02</td></tr><tr><td>Employment</td><td>0.32</td></tr><tr><td>Logistics and goods effects</td><td>0.05</td></tr><tr><td>Total rate</td><td>1.35</td></tr></table>

found equal to 1.17, which then makes the project feasible seen from a societal point of view. The conclusion to be drawn from the deterministic runs is therefore that when making a socio-economic analysis it is important not only to look upon the traditional, narrow effects from a CBA but also include wider impacts made up by network and mobility, global emissions (CO<sub>2</sub>), employment and logistics and goods effects modelled by the applied MCA in the COSIMA module [6,5].

The total level of the allocative externalities — the MCA impacts above — is determined by a CGE sketch model developed for the Øresund Region [1,8], see also Fig. 1 indicating the iterative procedure applied [4]. The CGE modelling approach is relevant to assess the wider economic impacts generated from transport projects, i.e. those impacts which are caused by the interaction between the transport sector and the overall economy. One problem, however, is that the magnitude of these (potentially) additional impacts can only be determined on a case-by-case basis [8,4].

The results from the deterministic runs are further examined in the CLG-DSS model by setting probability distributions for some of the variables. In this respect it can be mentioned that travel time savings, based on flow estimates from traffic models, are modelled by a normal distribution whereas, for example, employment is modelled by a triangular distribution for the value of one job created and $\mathrm { C O } _ { 2 }$ emissions by a uniform distribution for the value of one tonne of $\mathrm { C O } _ { 2 } .$ Furthermore, there will appear across the scenarios an increasing uncertainty, reflected in the particular distribution parameters. This uncertainty are modelled so moving from low via medium to high integration and from deregulation via regulation and sustainability to crisis and stagnation is associated with higher uncertainty along each regime axis. Fig. 3 gives an overview of the settings and the obtained results.

<table><tr><td></td><td>Deregulation</td><td>Regulation - sustainable development</td><td>Stagnation - crisis</td></tr><tr><td>High Integration in the region</td><td>Scenario 1CBA-I Normal (1;0.14)CBA-I Trigen (0.2;1;1.25;9%;91%)CBA-II Uniform (1;0.14)CBA-III Uniform (0.75;1.25)MCA-II Uniform (0.75;1.25)MCA-III Trigen (100;300;1000;9%;91%)MCA-IV Trigen (2900;3400;3900;9%;91%)MCA-V Uniform (0.75;1.25)Results [1.04;1.40;1.82]</td><td>Scenario 4CBA-I Normal (1;0.16)CBA-I Trigen (0.2;1;1.25;13%;87%)CBA-II Normal (1;0.16)CBA-III Uniform (0.75;1.25)MCA-II Uniform (0.75;1.25)MCA-III Trigen (100;300;1000;13%;87%)MCA-IV Trigen (2800;3300;3800;13%;87%)MCA-V Uniform (0.75;1.25)Results [0.94;1.23;1.55]</td><td>Scenario 7CBA-I Normal (1;0.20)CBA-I Trigen (0.2;1;1.25;15%;85%)CBA-II Normal (1;0.20)CBA-III Uniform (0.75;1.25)MCA-II Uniform (0.75;1.25)MCA-III Trigen (100;300;1000;15%;85%)MCA-IV Trigen (2700;3200;3700;15%;85%)MCA-V Uniform (0.75;1.25)Results [0.69;1.09;1.47]</td></tr><tr><td>Middle Integration in the region</td><td>Scenario 2CBA-I Normal (1;0.13)CBA-I Trigen (0.2;1;1.25;8%;92%)CBA-II Normal (1;0.13)CBA-III Uniform (0.75;1.25)MCA-II Uniform (0.75;1.25)MCA-III Trigen (100;300;1000;8%;92%)MCA-IV Trigen (2500;3000;3500;8%;92%)MCA-V Uniform (0.75;1.25)Results [0.80;1.08;1.30]</td><td>Scenario 5 – Reference scenarioCBA-I Normal (1;0.15)CBA-I Trigen (0.2;1;1.25;10%;90%)CBA-II Normal (1;0.15)CBA-III Uniform (0.75;1.25)MCA-II Uniform (0.75;1.25)MCA-III Trigen (100;300;1000;10%;90%)MCA-IV Trigen (2400;2900;3400;10%;90%)MCA-V Uniform (0.75;1.25)Results [0.73;1.01;1.30]</td><td>Scenario 8CBA-I Normal (1;0.17)CBA-I Trigen (0.2;1;1.25;12%;88%)CBA-II Normal (1;0.17)CBA-III Uniform (0.75;1.25)MCA-II Uniform (0.75;1.25)MCA-III Trigen (100;300;1000;12%;88%)MCA-IV Trigen (2300;2800;3300;12%;88%)MCA-V Uniform (0.75;1.25)Results [0.62;0.87;1.14]</td></tr><tr><td>Low Integration in the region</td><td>Scenario 3CBA-I Normal (1;0.10)CBA-I Trigen (0.2;1;1.25;5%;95%)CBA-II Normal (1;0.10)CBA-III Uniform (0.75;1.25)MCA-II Uniform (0.75;1.25)MCA-III Trigen (100;300;1000;5%;95%)MCA-IV Trigen (2100;2600;3100;5%;95%)MCA-V Uniform (0.75;1.25)Results [0.76;0.93;1.12]</td><td>Scenario 6CBA-I Normal (1;0.12)CBA-I Trigen (0.2;1;1.25;7%;93%)CBA-II Normal (1;0.12)CBA-III Uniform (0.75;1.25)MCA-II Uniform (0.75;1.25)MCA-III Trigen (100;300;1000;7%;93%)MCA-IV Trigen (2000;2500;3000;7%;93%)MCA-V Uniform (0.75;1.25)Results [0.68;0.87;1.10]</td><td>Scenario 9CBA-I Normal (1;0.16)CBA-I Trigen (0.2;1;1.25;11%;89%)CBA-II Normal (1;0.16)CBA-III Uniform (0.75;1.25)MCA-II Uniform (0.75;1.25)MCA-III Trigen (100;300;1000;11%;89%)MCA-IV Trigen (1900;2400;2900;11%;89%)MCA-V Uniform (0.75;1.25)Results [0.57;0.79;1.02]</td></tr></table>

Fig. 3. Overview of results for the stochastic runs. Note that the most likely value in Scenario 1 is 1.40 which deviates from the 1.35 shown in Table 2 due to asymmetric probability distributions.

The results from the stochastic runs are presented in Fig. 4 by descending cumulative graphs indicating the probability that the overall rate of return will be equalled or exceeded. To exemplify, the Scenario 1 result is the SC 1-curve at the right, showing a total return rate equal to 1.03 at 100% probability and a rate equal to 1.85 at a 1% probability level.

Note that for the descending cumulative curves with the probability on the y-axis and the rate of return on the x-axis more reliable data will lead to steeper curves. Note also for Scenarios 2 and 7 results, and to some extent for Scenarios 6 and 8 results, that the curves cross each other. This is to be paid special attention to by the decision-makers with regard to the desired level of rate and their actual risk aversion.

The influence on practical decision-making can be illustrated as follows. Scenario 7 has a total return rate equal to 1.09 at the 50 percentile indicating a feasible project. Most decision makers, however, are not pleased $ { \mathrm { \^ { 6 } o n l y ^ { , 3 } } }$ with a 50% level but would prefer, for example, a 90% level here giving a rate below 1 equal to 0.94 indicating that the project is not feasible at this level of probability. The feasibility risk to be adopted in the actual case is of course up to the decision-makers to debate but the features to deal with uncertainty in the CLG-DSS model may help support their considerations. Some of these will be to get acquainted with the various assumptions behind the scenarios, probability distributions, and the way the latter have been assessed/ estimated and related to the different scenarios.

## 6. Conclusions and perspective

This paper has presented a new model to appraise large transport infrastructure projects stemming from research carried out in the Danish Centre for Logistics and Freight Transport (CLG). The model development uses the Øresund Fixed Link and the Øresund region as an evaluation methodology laboratory. One major outcome is that narrow CBA-based impacts — in many European countries described in a national manual — need to be supplemented with wider impacts to appraise whether the project is feasible or not feasible from a socio-economic viewpoint. Due to the comprehensive and complex project information it will be relevant to deal with uncertainty issues as part of the decision support established by the appraisal study. The approach taken in the CLG-DSS model is to combine scenarios and Monte Carlo simulation to establish a range of results.

The Øresund Fixed Link: All Scenarios  
![](/api/attachments/XVHWZTMN/fulltext/images/dc68bd32737721fb914db2bbb61751a8f8f7f7e4d25811a97164dfebb7e37c37.jpg)  
Fig. 4. Combination of descending graphs concerning the nine framework scenarios.

Although the total set of model results — here also considering subdivisions of the total rate into CBA and MCA contributions and further into single impact return contributions — may seem quite comprehensive it is the opinion of the team behind the CLG-DSS model that it is possible to communicate the essence to decision-makers. This also includes the extension of deterministic single value results into stochastic result curves and their association with different scenarios.

A current research perspective is to refine the CGE approach and continue the iteration indicated in Fig. 1. This will allow better calibration of the impact models applied for the four allocative externalities made use of in the model. Another research perspective is to continue the work on linking scenarios with the Monte Carlo simulation [5].

At its current stage of development it can be concluded that the CLG-DSS model contains model features that are relevant and effective for the provision of decision support for large transport infrastructure projects with emphasis on assessment of uncertainty. There is, however, ample room for further development when applying it on other case studies.

## References

[1] D. Banister, J. Berechman, Transport Investment and Economic Development, UCL Press Taylor & Francis Group, United Kingdom, London, 2000.

[2] P. Goodwin, S. Persson, Assessing the Benefits of Transport, ECMT Report, OECD, 2001.

[3] P. Hall, Europe 2000, Columbia University Press, London, United Kingdom, 1977.

[4] T. Holvad, S. Leleur, Assessment of wider economic benefits: the case of the øresund fixed link with a special emphasis on regional economic development, Proceeding the 10th World Conference on Transport Research Istanbul, Turkey, 2004.

[5] S. Leleur, Road Infrastructure Planning — A Decision-Oriented Approach, 2nd Edition, Polytechnical Press, Denmark, Lyngby, 2000.

[6] S. Leleur, T. Holvad, K.B. Salling, A.V. Jensen, Development of the CLG-DSS Evaluation Model, CLG-Report 1, Feb 2004.

[7] Palisade Corporation, @RISK — Risk Analysis and Simulation Add-In for Microsoft Excel, Vers. 4.5 (USA, Newfield, 2002).

[8] SACTRA, Transport and the Economy, Final Report, SACTRA, 1999.

[9] A.J. Venables, M. Gasiorek, The Welfare Implications of Transport Improvements in the Presence of Market Failure, Report to SACTRA, 1999.

[10] D. Vose, Risk Analysis — A Quantitative Guide, 2nd Edition, John Wiley & Sons Ltd, Chichester, United Kingdom, 2000.

![](/api/attachments/XVHWZTMN/fulltext/images/be0f8da614299bc5fe7d9192a76a550330bedb820bf56bc0261eb9a58f6983df.jpg)

Kim Bang Salling is currently a Ph.D. Student in the Decision Modelling Group at the Centre for Traffic and Transport in the Technical University of Denmark. He holds a Master's degree in Engineering. He specialises in socio-economic evaluation methodologies with special emphasis on cost-benefit analysis and multi-criteria analysis. His Ph.D. study is entitled: Optimization of Decision Support concerning Large Infrastructure Projects. The study is partly funded by the Danish

Centre for Logistics and Freight transport (CLG). The main purpose of the Ph.D. project is to formulate and define a method/model towards optimization of project appraisal. By use of the so-called COSIMA– VEJ software, which is a basic evaluation software of large-scale infrastructure appraisal, a new methodology for assessment is made.

![](/api/attachments/XVHWZTMN/fulltext/images/c0b3748aa2ebcc19332c5ce84e4b8a2862950f10f0a5553e6887ca98ccb0a3d8.jpg)

Steen Leleur is a professor of decision support systems and planning at the Centre for Traffic and Transport—CTT at the Technical University of Denmark–DTU and the head of the Decision Modelling Group. He is an experienced transport planner, who has participated in numerous activities especially in the fields of national and international strategic transport planning studies, transport investment planning, road project appraisals and road project priority scheme studies.

Steen Leleur has worked out, among other things, three textbooks of which the most recent are “Road Infrastructure Planning—A Decision Oriented Approach” published in 2000, Second Edition and “Systemic Planning” published in 2005. Steen Leleur has participated in the EU research projects EURET 1.1, APAS/ROAD3, EUNET, TEN– ASSESS, CODE–TEN, TRANS–TALK and TEN–INVEST. Currently he is involved in TRANS–TOOLS and TRANSFORUM.

![](/api/attachments/XVHWZTMN/fulltext/images/ee45e8b722f846decb32b694dbc53af74b23786d7808f04b7bccc47e7aa95e57.jpg)

Anders Vestergaard Jensen is currently employed as a research assistant in the Decision Modelling Group at the Centre for Traffic and Transport in the Technical University of Denmark. He holds a Master's degree in Engineering. He has participated in the Centre for Logistics and Freight transport (CLG) where he is the co-author of a report describing decision support. Furthermore he has participated in the elaboration of the COSIMA–VEJ software developed for the Danish Road

Directorate. Currently he participates in a project for the Greenland Home rule, which elaborates a transport model and appraisal tool for new infrastructure projects in Greenland. He is also a part of the Strategic Transport Management in the Øresund region project.
