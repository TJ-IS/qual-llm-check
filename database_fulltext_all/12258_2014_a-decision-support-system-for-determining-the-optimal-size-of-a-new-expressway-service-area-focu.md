---
otero_id: 12258
otero_key: "YZEBY7MS"
title: "A decision support system for determining the optimal size of a new expressway service area: Focused on the profitability"
authors: "Choongwan Koo; Taehoon Hong; Jimin Kim"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.07.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A decision support system for determining the optimal size of a new expressway service area: Focused on the pro<sup>fi</sup>tability

Choongwan Koo, Taehoon Hong ⁎, Jimin Kim

Department of Architectural Engineering, Yonsei University, Seoul 120-749, Republic of Korea

## a r t i c l e i n f o

Article history: Received 4 November 2013 Received in revised form 3 June 2014 Accepted 22 July 2014 Available online xxxx

Keywords: Decision support systems Operations management Expressway service area Case-based reasoning Decision tree

## a b s t r a c t

Since the early 1990s, South Korea has been expanding its expressways. As of July 2013, a total of 173 expressway service areas (ESAs) have been established. Among these, 31 ESAs were closed due to <sup>fi</sup>nancial de<sup>fi</sup>cits. To address this challenge, this study aimed to develop a decision support system for determining the optimal size of a new ESA, focusing on the pro<sup>fi</sup>tability of the ESA. This study adopted a case-based reasoning approach as the main research method because it is necessary to provide the historical data as a reference in determining the optimal size of a new ESA, which is more suitable for the decision-making process from the practical perspective. This study used a total of 106 general ESAs to develop the proposed system. Compared to the conventional process (i.e., direction estimation), the prediction accuracy of the improved process (i.e., three-phase estimation process) was improved by 9.84%. The computational time required for the optimization of the proposed system was determined to be less than 10 min (from 1.75 min to 9.93 min). The proposed system could be useful for the <sup>fi</sup>nal decision-maker as the following purposes: (i) the probability estimation model for determining the optimal size of a new ESA during the planning stage; (ii) the approximate initial construction cost estimation model for a new ESA by using the estimated sales in the ESA; and (iii) the comparative assessment model for evaluating the sales per the building area of the existing ESA.

© 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

## 1.1. Research background and objective

Expressway Service Areas (ESAs) offer rest, convenience, and safety to drivers who make mid- to long-distance trips. According to the ‘Expressway design handbook (Section 9. Service facility) [1],’ the ESA relieves drivers from fatigue and stress due to continuous expressway driving, resolves the physiological needs of the drivers, and offers them opportunities to re<sup>fi</sup>ll their gas tanks and to check their cars for repairs. Recently, ESAs have likewise been required to provide additional amenities such as integrated IT services and eco-friendly resting places. From the four ESAs that were established in 1970, a total of 173 ESAs have been built in South Korea as of July 2013 [2,3].

Among these ESAs, however, 31 ESAs were closed due to <sup>fi</sup>nancial de<sup>fi</sup>cits. It means that there were some problems in the conventional process for determining the size of a new ESA, which caused the huge initial investment for several years before any income is returned. For example, about 43.2 million dollars was invested for the construction of ‘D’ ESA in South Korea, which was used to verify the feasibility of the developed system. To prevent these de<sup>fi</sup>cits in the operation of a new ESA in advance, this study aimed to develop a decision support system for determining the optimal size of a new ESA, focusing on the profitability of the ESA

## 1.2. Research scope and method

According to the current regulations [1,4,5], the functions of the ESA generally consist of three components: (i) convenient facilities (such as parking lots, restrooms, and green spaces); (ii) business facilities (such as restaurants, convenience stores, gas stations, and vending machines); and (iii) operation facilities (such as electric and communication facilities, water supply and sewage systems, and gas storage facilities). Among the three functions, the de<sup>fi</sup>cits in the operations of the ESAs are not directly related to the <sup>fi</sup>rst component (i.e., the convenient facilities), but to the other two components (i.e., the business facility and the operation facility). Therefore, the scope of this study is limited for determining the optimal size of the building area (including both the business facility and the operation facility) of a new ESA, which does not include the convenient facility.

To develop the decision support system, this study collected the project characteristics on a total of 106 general ESAs out of 142 ESAs which were operated by Korea Expressway Corporation (KEC) as of 2013. Namely, 36 ESAs were excluded based on the following criteria: (i) since this study focused on the optimal size of the general ESAs, 11 freight ESAs were excluded; (ii) since it is necessary to consider the ‘passing traffic volume’ as independent variable, 14 ESAs, whose passing traf<sup>fi</sup>c volume were not surveyed, were excluded; and (iii) since it is necessary to consider the ‘sales in the ESA’ as dependent variable, 11 ESAs, whose sales were not surveyed, were excluded.

This study was conducted largely in two steps: (i) this study conducted the statistical analysis to clearly identify the problems of the conventional process for determining the size of a new ESA; and (ii) based on the results of the statistical analysis, this study proposed the improved process for determining the optimal size of a new ESA, focusing on the pro<sup>fi</sup>tability of the ESA. Meanwhile, this study adopted a case-based reasoning (CBR) approach as the main research method because it is necessary to provide the historical data as a reference in determining the optimal size of a new ESA, which is more suitable for the decision-making process from the practical perspective.

## 1.3. Literature review

## 1.3.1. Parking space demand

Previous studies considered the parking space demand as the main impact factors. Regarding the parking space demand, various studies have been conducted worldwide [6–21]. First, international studies on the parking space demand of the ESA were conducted as follows. Especially, this study focused on the U.S. Department of Transportation (DOT) and its specialized division, the Federal Highway Administration (FHWA). The FHWA has mainly developed several handbooks for a commercial truck's parking space demand [6,7]. Several state DOT have developed prediction models to determine parking space requirements for the ESA. The Minnesota DOT (MnDOT) model was developed as a macroscopic-level parking space model for the ESA in 1979. This model was revised by the Virginia DOT (VDOT) based on the usage survey of the ESA in 1994. The MnDOT and VDOT's models only considered the passing traf<sup>fi</sup>c volume along the mainline to estimate the truck parking demand. Garber et al. [8] and Wang and Garber [9] considered the factors affecting the demand for commercial truck parking such as the percentage of trucks in the traf<sup>fi</sup>c stream, the distance from a truck stop to mainline, the distance from a truck stop to the nearest truck stop, and the facilities provided at the truck stop. In addition, several studies proposed the estimation models based on the law of supply and demand. FHWA [10] proposed two models: the capacity utilization model to evaluate the usage rate of the truck parking space in the operation stage of the ESA; and the truck parking demand model to evaluate the expansion size of the truck parking space. Gopi [11] developed recommendations that can provide parking facilities and the associated services based on the needs for commercial truck drivers in South Dakota DOT by using the truck parking demand model. FHWA [12] analyzed the commercial truck parking supply and demand balances, and then evaluated the adequacy of commercial truck parking facilities. Rodier and Shaheen [13] analyzed the expected truck parking shortages and illegal parking by considering the supply and demand for trucking parking within the study area. FHWA [14] analyzed the truck traf<sup>fi</sup>c volume and available parking space within the study area by using geographic information system, the results of which showed that the truck parking worked very well. Adams et al. [15] analyzed the supply and demand for trucking parking in Wisconsin DOT as follows: identi<sup>fi</sup>ed the parking issues for day-trip drivers; the operational issues causing the need for parking; where new or expanded facilities are needed; and low-cost solution to address trucking parking shortfalls. Based on the national research, other studies focused on the demand for truck parking space, the impact of the truck parking space on truck parking facilities, parking location, transportation infrastructure, safety, local economy, and environment. There were also sev eral studies related to parking space, location and pricing, and rest area facility design [16–21]. As such, international previous studies mainly dealt with the truck parking space demand, of which focus was different from the ESAs in South Korea in terms of the type of ESA. Moreover, they presented a linear model such as an equation that uses conversion factors such as the usage rate, congestion rate, and turnover rate of the ESAs, which may cause an issue on the reliability of the estimation model.

Second, domestic studies on the parking space demand of the ESA were conducted as follows [22–25]. Several studies focused on the parking space demand of the general ESA by taking into account the impact factors such as vehicle types, daytime and night-time traf<sup>fi</sup>c volume, and traf<sup>fi</sup>c routes. In these studies, the conversion factors were used to estimate the parking space demand of a new ESA, which were established by using regression and cluster analyses [22–24]. Another study developed a model through regression analysis in order to estimate the parking space demand for freight vehicles. In the study, independent variables were extracted through factor analysis and correlation analysis [25]. As such, domestic studies were mainly limited to the parking space demand, merely suggesting a conversion factor or a linear model. Namely, various characteristics of ESAs were not considered, and thus it is limited in establishing the optimal size of a new ESA.

In summary, there were two major limitations in the previous studies: (i) the parking space demand was considered as main impact factor to estimate the size of a new ESA. The parking space demand was directly related to the size of convenient facility, but it was not directly related to the building area (including both the business facility and the operation facility). Accordingly, these approaches cannot estimate the optimal size of a new ESA, resulting in the de<sup>fi</sup>cits in the operations of the ESAs; and (ii) the conversion factors for determining the size of a new ESA were established as a <sup>fi</sup>xed value based on limited survey results or a regression model based on limited historical data, which were not suf<sup>fi</sup>ciently validated. Accordingly, although the usage pattern of the ESA may be diverse depending on its characteristics, the previous studies cannot re<sup>fl</sup>ect enough characteristics to determine the optimal size of a new ESA.

## 1.3.2. Data mining technique

Various types of data mining techniques have been used for the purpose of prediction and classi<sup>fi</sup>cation (e.g., multiple regression analysis (MRA); arti<sup>fi</sup>cial neural network (ANN); decision tree (DT); and CBR). In addition, the optimization process has been adopted to solve the complicated high-dimensional problems.

• As a statistical method, MRA can be relatively simple to implement, and is easy to understand. However, MRA is not suitable for the complicated problems [26–30].

• While ANN can solve the complicated non-linearity among various variables, it is not able to explain the process from which the <sup>fi</sup>nal results are obtained, due to a hidden layer called the ‘black box [31–34].

• DT can form the clusters through the correlation analysis among the project's characteristics. Because the <sup>fi</sup>nal result is provided in the form of a tree, it is easy to understand and simple to implement. However, in case that the correlation among the independent variables is too complicated, the prediction accuracy of DT model can decrease [35,36].

• CBR cannot only provide the prediction value based on historical data, but also present the retrieved cases as a reference for the decisionmaking. Namely, CBR has higher explanatory power. As with the continuous accumulation of the database, the prediction accuracy of CBR model can be improved. However, the prediction accuracy of the basic CBR model is relatively inferior to that of MRA or ANN model [37–39]. Therefore, when the CBR method is adopted to estimate some value, the prediction accuracy of the basic CBR model can be improved by integrating itself with the other techniques (e.g., MRA, ANN, and DT) and by implementing the optimization process (e.g., genetic algorithm (GA)) to improve its prediction accuracy.

• GA is an adaptive heuristic algorithm based on the evolutionary concept of natural selection, in which a random search is conducted within a de<sup>fi</sup>ned range to address a given problem. GA is more suitable for <sup>fi</sup>nding the best solution to dif<sup>fi</sup>cult high-dimensional problems [40–44].

Based on the preliminary review on the various characteristics of the aforementioned data mining methodologies, this study aimed to develop a CBR-based decision support system for determining the optimal size of a new ESA. Also, this study aimed to solve the disadvantage of the basic CBR method (i.e., relatively lower prediction accuracy than the other data mining techniques) by developing an advanced CBR (A-CBR) model. Namely, this study can achieve this objective by integrating the basic CBR method with other data mining techniques (i.e., MRA, ANN, and DT) and by implementing the optimization algorithm (i.e., GA). Furthermore, by estimating the probability density function (PDF) through Monte Carlo simulation (MCS), the study hopes to offer various options for the <sup>fi</sup>nal decision-maker [45,46].

## 2. Preliminary review on the conventional process for determining the size of a new expressway service area

Fig. 1 shows the conventional process for determining the size of a new ESA in South Korea. It has been consistently revised. In 2004, ‘Improvement of the size of ESA [5]’ was established to prepare for the changes in the usage pattern of the ESA due to the expansion of the <sup>fi</sup>ve-day workweek system, resulting in the increases in operational ef<sup>fi</sup>ciency and customer service satisfaction. This guideline categorized the types of ESAs into general and freight ESAs. General ESAs were further divided into small-sized, mid-sized, and large-sized ones. Also, this guideline provided the detailed areas of the ESA (i.e., convenient facilities, business facilities, and operation facilities). While this guideline increased the previous standard for estimating the size of the ESA, there was no reasonable basis. In 2009, ‘Expressway design handbook (Section 9. Service facility) [1]’ was established to determine the size of a new ESA, in which the parking space demand was only considered. Moreover, the parking space demand was determined based on the three types of conversion factors. These conversion factors were established as a <sup>fi</sup>xed value based on limited survey results or a regression model based on limited historical data. Consequently, the conventional process was limited in determining the optimal size of a new ESA, resulting in the de<sup>fi</sup>cit operation of some ESAs.

This study conducted the statistical analysis to clearly identify the problems of the conventional process. Prior to the statistical analysis, based on interviews with ESA experts at KEC, this study focused on the following three relationships that should be considered to determine the optimal size of the ESA: (i) the ‘building area of the ESA’ should be established based on the ‘sales in the ESA’; (ii) the ‘sales in the ESA’ could be mainly affected by ‘the number of daily vehicles’; and (iii) ‘the number of daily vehicles’ could be mainly affected by the ‘passing traffic volume.’ Therefore, the following four factors were selected to conduct the statistical analysis: the ‘passing traffic volume’; ‘the number of daily vehicles’; the ‘sales in the ESA’; and the ‘building area of the ESA’.

Table 1 shows the descriptive statistics (i.e., minimum, maximum, mean, and standard deviation) on the four main factors that should be considered in determining the size of the ESA. They were distributed in a very wide range of the ‘passing traffic volume’ of 2767.0–95,667.0 (mean, 20,038.6; and standard deviation, 18,581.4); ‘the number of daily vehicles’ of 369.0–12,972.0 (mean, 3475.0; and standard deviation, 2291.0); the ‘sales in the ESA’ of 296.9–14,116.0 (mean, 4615.6; and standard deviation, 3066.1); and the ‘building area of the ESA’ of 341.0–6509.0 (mean, 2498.3; and standard deviation, 1245.8). Considering that these distributions were made based on the 106 ESAs, this study concluded that each of the 106 ESAs has very different characteristics from one another. Namely, it is very dif<sup>fi</sup>cult to estimate the optimal size of a new ESA, resulting in achieving the pro<sup>fi</sup>tability of the ESA.

Table 2 shows the correlation analysis among the aforementioned four main factors that should be considered in determining the size of the ESA. Based on the correlation analysis, this study concluded that while the convenient facility area can be estimated from the parking space demand (which can be estimated from the ‘passing traffic volume’ and ‘the number of daily vehicles’), the building area (including both the business facility and the operation facility) cannot be estimated from the parking space demand. The details of the analysis were as follows:

• The correlation coef<sup>fi</sup>cient between the ‘passing traffic volume’ and ‘the number of daily vehicles’ was 0.862, showing a very high correlation. It means that the parking space demand can be estimated by using ‘the number of daily vehicles’, which can be determined based on the ‘passing traffic volume’.

• The correlation coef<sup>fi</sup>cient between the ‘passing traffic volume’ and the ‘building area of the ESA’ was 0.383. Also, the correlation coef<sup>fi</sup>cient between ‘the number of daily vehicles’ and the ‘building area of the ESA’ was 0.435. These correlations were very low. It can be concluded

![](/api/attachments/YZEBY7MS/fulltext/images/19263fcbde80b2c406a655204036d50b942786a5ae9e4ac0f21481d83bb03a6e.jpg)  
Fig. 1. Conventional process for determining the size of a new expressway service area.

Please cite this article as: C. Koo, et al., A decision support system for determining the optimal size of a new expressway service area: Focused on the pro<sup>fi</sup>tability, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.07.005

Table 1  
Descriptive statistics on the four main factors in determining the size of the ESA.

<table><tr><td>Classification</td><td>N</td><td>Minimum</td><td>Maximum</td><td>Mean</td><td>Standard deviation</td></tr><tr><td>Passing traffic volume (Vehicles/day)</td><td>106</td><td>2767.0</td><td>95,667.0</td><td>20,038.6</td><td>18,581.4</td></tr><tr><td>The number of daily vehicles (Vehicles/day)</td><td>106</td><td>369.0</td><td>12,972.0</td><td>3475.0</td><td>2291.0</td></tr><tr><td>Sales in the ESA (Thousand $/year)</td><td>106</td><td>296.9</td><td>14,116.0</td><td>4615.6</td><td>3066.1</td></tr><tr><td>Building area of the ESA ( $m^2$ )</td><td>106</td><td>341.0</td><td>6509.0</td><td>2498.3</td><td>1245.8</td></tr></table>

that it was not appropriate to estimate the building area (including both the business facility and the operation facility) by using the ‘passing traffic volume’, ‘the number of daily vehicles’, and the parking space demand. Namely, it indicated that there were the problems in the conventional process for determining the size of a new ESA. It is because the conventional process did not only implement the excessive passing traf<sup>fi</sup>c volume but also used the conversion factors as a <sup>fi</sup>xed value based on limited survey results or a regression model based on limited historical data.

• The correlation coef<sup>fi</sup>cient between ‘the number of daily vehicles’ and ‘sales in the ESA’ was 0.873. Also, the correlation coef<sup>fi</sup>cient between ‘sales in the ESA’ and ‘building area of the ESA’ was 0.564. The correlations were very high. It means that the building area (including both the business facility and the operation facility) can be estimated by using ‘sales in the ESA’, based on ‘the number of daily vehicles’. Accordingly, it can be expected that the number of de<sup>fi</sup>cit ESAs will be considerably reduced if the ‘building area of the ESA’ can be estimated by using ‘sales in the ESA’ through the improved process.

Based on the above analysis, it was determined that the conventional process had two limitations, resulting in the de<sup>fi</sup>cit operation of the ESAs: (i) the conventional process did not propose the standards from the economic perspective. In the conventional process, the size of a new ESA was calculated by only considering the parking space demand. As can be founded in the statistical analysis, the parking space demand is suitable for estimating the size of convenient facility, but not for estimating the building area (including both the business facility and the operation facility), directly related to the sales in the ESA; and (ii) in the estimation process of the parking space demand, the conversion factors were not suf<sup>fi</sup>ciently validated. For these conversion factors, the conventional process used a <sup>fi</sup>xed value based on limited survey results or a regression model based on limited historical data. Consequently, the conventional process was limited in determining the optimal size of a new ESA, resulting in the de<sup>fi</sup>cit operation of some ESAs.

Based on the statistical analysis, this study proposed the improved process for determining the optimal size of a new ESA, focusing on the pro<sup>fi</sup>tability of the ESA. Fig. 2 shows the improved process, consisting of a three-phase estimation process. Namely, Phase 1 can be used in estimating the size of convenient facilities, and Phases 2 and 3 can be used in estimating the building area (including both the business facility and the operation facility) that generates the sales in the ESA.

• Phase 1, the estimation of the ‘usage rate of the ESA’ using DT and A-CBR: The ‘usage rate of the ESA’ can be used to estimate ‘the number of daily vehicles (refer to ‘(2)’ in Fig. 2)’, based on the ‘passing traffic volume (refer to ‘(1)’ in Fig. 2)’;

• Phase 2, the estimation of the ‘sales per vehicle’ using DT and A-CBR: The ‘sales per vehicle’ can be used to estimate the ‘sales in the ESA (refer to ‘(3)’ in Fig. 2)’, based on ‘the number of daily vehicles (refer to ‘(2)’ in Fig. 2)’; and,

• Phase 3, the estimation of the sales per the building area using PDF: The ‘sales per the building area’ can be used to estimate the ‘building area of the ESA (refer to ‘(4)’ in Fig. 2)’, based on the ‘sales in the ESA (refer to ‘(3)’ in Fig. 2)’.

## 3. A decision support system for determining the optimal size of a new expressway service area

This study aimed to develop a CBR-based decision support system for determining the optimal size of a new ESA, which was conducted in four steps: (i) setting the case-base; (ii) formation of a cluster using DT; (iii) development of an A-CBR model; and (iv) development of the PDF for the sales per the building area of ESAs.

## 3.1. Setting the case-base

Table 3 presents the factors affecting the ‘usage rate of the ESA’ and the ‘sales in the ESA’. Also, the detailed classi<sup>fi</sup>cation and the type of scale are explained by the factors. Through interviews with ESA experts at KEC, based on an extensive analysis of previous studies [6,8,12–14, 21–23], the following independent variables were categorized into largely two parts: (i) ‘Lane’ and (ii) ‘Service’.

First, the details of the seven independent variables included in ‘Lane’ are as follows:

• ‘Passing traffic volume’ stands for the number of daily vehicles passing the point where a new ESA is planned to be established. This factor can directly affect both the number of daily vehicles using the new ESA and the sales in the ESA.

Correlation analysis among the main factors in determining the size of the ESA. Note: Asterisk (\*\*) mean that the correlation coef<sup>fi</sup>cient is signi<sup>fi</sup>cant at 0.01 level (both sides)

<table><tr><td>Variable</td><td></td><td>Passing traffic volume</td><td>The number of daily vehicles</td><td>Sales in the ESA</td><td>Building area of the ESA</td></tr><tr><td rowspan="2">Passing traffic volume</td><td>Pearson correlation</td><td>1</td><td>.862**</td><td>.692**</td><td>.383**</td></tr><tr><td>Sig. (2-tailed)</td><td></td><td>.000</td><td>.000</td><td>.000</td></tr><tr><td rowspan="2">The number of daily vehicles</td><td>Pearson correlation</td><td>.862**</td><td>1</td><td>.873**</td><td>.435**</td></tr><tr><td>Sig. (2-tailed)</td><td>.000</td><td></td><td>.000</td><td>.000</td></tr><tr><td rowspan="2">Sales in the ESA</td><td>Pearson correlation</td><td>.692**</td><td>.873**</td><td>1</td><td>.564**</td></tr><tr><td>Sig. (2-tailed)</td><td>.000</td><td>.000</td><td></td><td>.000</td></tr><tr><td rowspan="2">Building area of the ESA</td><td>Pearson correlation</td><td>.383**</td><td>.435**</td><td>.564**</td><td>1</td></tr><tr><td>Sig. (2-tailed)</td><td>.000</td><td>.000</td><td>.000</td><td></td></tr></table>

Please cite this article as: C. Koo, et al., A decision support system for determining the optimal size of a new expressway service area: Focused on the pro<sup>fi</sup>tability, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.07.005

C. Koo et al. / Decision Support Systems xxx (2014) xxx–xxx

![](/api/attachments/YZEBY7MS/fulltext/images/eb98f1abf6309bbbe11f0f96dfeb0760b0248afbd92a54672f6edce77b6d97c5.jpg)  
Fig. 2. Proposed process for determining the optimal size of a new expressway service area.

• ‘Name of the expressway’ stands for the type of the expressway. There exist a total of 10 major expressways in South Korea. This factor can affect the scale of the expressway, the length of the expressway, and the relationship among one another.

• ‘Direction of the expressway’ stands for the direction of vehicles at the point where a new ESA is planned to be established. This factor is de<sup>fi</sup>ned as two types: southbound lane and northbound lane.

• ‘Location from the intersection/junction’ stands for the location of a new ESA from the nearest intersection/junction. This factor is de<sup>fi</sup>ned as two types: upstream and downstream.

• ‘Position ratio’ stands for the ratio dividing the distance from the downstream intersection/junction to the point where a new ESA is planned to be established by the total distance from the downstream intersection/junction to the upstream intersection/junction. This factor is categorized into four quartiles.

• ‘Distance from the upstream service area’ stands for the distance between a new ESA and its upstream service area. This factor is de<sup>fi</sup>ned as the unit of “km”. This factor can affect both the usage rate of the ESA and the sales in the ESA.

• ‘Distance from the downstream service area’ stands for the distance between a new ESA and its downstream service area. This factor is de<sup>fi</sup>ned as the unit of “km”. This factor can affect both the usage rate of the ESA and the sales in the ESA.

Second, the details of the three independent variables included in ‘Service’ are as follows:

• ‘Petrol station’ stands for the station where gasoline or diesel fuel is provided for vehicles.

• ‘LPG station’ stands for the station where lique<sup>fi</sup>ed petroleum gas is provided for vehicles.

• ‘Auto repair shop’ stands for the repair shop where automobiles are repaired by auto mechanics and electricians.

Meanwhile, based on the improved process for determining the optimal size of a new ESA (refer to Fig. 2), dependent variables were categorized into two factors: the ‘usage rate of the ESA’ and the ‘sales per vehicle’.

• The ‘usage rate of the ESA’ stands for the ratio of ‘the number of daily vehicles (refer to ‘(2)’ in Fig. 2)’ to the ‘passing traffic volume (refer to ‘(1)’ in Fig. 2)’. This factor can directly affect the ‘sales in the ESA (refer to ‘(3)’ in Fig. 2)’.

• The ‘sales per vehicle’ can be calculated by dividing the ‘sales in the ESA (refer to ‘(3)’ in Fig. 2)’ by ‘the number of daily vehicles (refer to ‘(2)’ in Fig. 2)’. This factor can directly affect the ‘building area of the ESA (refer to ‘(4)’ in Fig. 2)’.

## Table 3

Factors affecting the usage rate of the ESA and the sales in the ESA.

<table><tr><td>Variables</td><td>Attributes</td><td></td><td>Detailed classification</td><td>Type of scale</td></tr><tr><td rowspan="10">Independent variable</td><td rowspan="7">Lane</td><td>Passing traffic volume</td><td>( ) Vehicles/daily</td><td>Numerical</td></tr><tr><td>Name of the expressway</td><td>Gyeongbu, Namhae, 88Olympic, West-coast, Honam, Jungbu, Tongyeong-Daejeon, Jungbu-Naeryuk, Yeongdong, Jungang</td><td>Nominal</td></tr><tr><td>Direction of the expressway</td><td>Southbound lane, Northbound lane</td><td>Nominal</td></tr><tr><td>Location from the intersection/junction</td><td>Upstream, Downstream</td><td>Nominal</td></tr><tr><td>Position ratio</td><td>Quartile1, Quartile2, Quartile3, Quartile4</td><td>Nominal</td></tr><tr><td>Distance from the upstream service area</td><td>( ) km</td><td>Numerical</td></tr><tr><td>Distance from the downstream service area</td><td>( ) km</td><td>Numerical</td></tr><tr><td rowspan="3">Service</td><td>Petrol station (gasoline, diesel)</td><td>Yes (1), No (0)</td><td>Dummy</td></tr><tr><td>LPG station</td><td>Yes (1), No (0)</td><td>Dummy</td></tr><tr><td>Auto repair shop</td><td>Yes (1), No (0)</td><td>Dummy</td></tr><tr><td rowspan="2">Dependent variable</td><td rowspan="2"></td><td>Usage rate of the ESA</td><td>( ) %</td><td>Numerical</td></tr><tr><td>Sales per vehicle</td><td>( ) $/vehicle</td><td>Numerical</td></tr></table>

Please cite this article as: C. Koo, et al., A decision support system for determining the optimal size of a new expressway service area: Focused on the pro<sup>fi</sup>tability, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.07.005

Table 5  
Table 4  
Detailed description of the splitting criterion for the data classi<sup>fi</sup>cation in Phase 1.

<table><tr><td>Classification</td><td>Number of cases</td><td>Usage rate of the ESA (%)</td><td>Passing traffic volume (X1)</td></tr><tr><td>Leaf 1</td><td>61</td><td>0.246</td><td>≤ 16,521</td></tr><tr><td>Leaf 2</td><td>45</td><td>0.165</td><td>&gt; 16,521</td></tr></table>

## 3.2. Formation of a cluster using DT

As one of the data mining techniques, DT is very effective in the data classi<sup>fi</sup>cation. This study used DT for the data classi<sup>fi</sup>cation, where independent variables that were highly correlative to the dependent variable were selected as the splitting criteria. Since the dependent variables (i.e., the ‘usage rate of the ESA’ and the ‘sales per vehicle’) were de<sup>fi</sup>ned under the ratio scale, the Regression Tree of CART (Classi<sup>fi</sup>cation and Regression Trees) was adopted in this study. CART forms binary tree architecture, and its basic principle is to <sup>fi</sup>nd out the independent variable that classi<sup>fi</sup>es the dependent variable best [35,36].

This study proposed the improved process for determining the optimal size of a new ESA, which consists of a three-phase estimation process. Among these, DT was used in Phase 1 and Phase 2 (refer to Fig. 2): (i) Phase 1: Table 4 shows the detailed description of the splitting criteria for the data classi<sup>fi</sup>cation. The ‘passing traffic volume’ was used as the splitting criterion, and consequently, the dependent variable (i.e., the ‘usage rate of the ESA’) was classi<sup>fi</sup>ed into two leaves. Each of clusters was formed as a cluster of 61 data and a cluster of 45 data, respectively; and (ii) Phase 2: Table 5 shows the detailed description of the splitting criterion for the data classi<sup>fi</sup>cation. The ‘name of the expressway’ was used as the splitting criterion, and consequently, the dependent variable (i.e., the ‘sales per vehicle’) was classi<sup>fi</sup>ed into two leaves. Each of clusters was formed as a cluster of 57 data and a cluster of 49 data, respectively.

## 3.3. Development of an A-CBR model

## 3.3.1. Selection of similar expressway service areas using CBR

As a data mining technique, CBR can be generally applied to classi<sup>fi</sup>- cation tasks and synthesis tasks to <sup>fi</sup>nd a new solution by combining the existing solutions [47]. Based on this characteristic of CBR, this study used CBR to <sup>fi</sup>nd a new solution, i.e., for determining the optimal size of a new ESA. Toward this end, it is necessary to conduct a comparative analysis among similar ESAs. This study developed two CBR models for estimating the ‘usage rate of the ESA’ in Phase 1 and the ‘sales per vehicle’ in Phase 2, respectively.

CBR can retrieve several cases based on the case similarity score. The detailed process of CBR includes the attribute similarity, the attribute weight, and the case similarity. The research team has analyzed a variety of similarity metrics in the previous studies [48–50]. It was concluded that the prediction performance was the most excellent in applying the optimization process to the basic CBR process with the nearest-neighbor retrieval algorithm. Accordingly, this study adopted the nearest-neighbor retrieval algorithm as one of the similarity metrics because it is a very simple and common method. As shown in Eq. (1), it can be expressed as a simple determinant [51–57]

Detailed description of the splitting criterion for the data classi<sup>fi</sup>cation in Phase 2

<table><tr><td>Classification</td><td>Number of cases</td><td>Sales per vehicle ($/vehicle)</td><td>Name of expressway (X1)</td></tr><tr><td>Leaf 1</td><td>57</td><td>3.187</td><td>1(Gyeongbu), 2(Namhae), 3(88Olympic), 5(Honam), 7(Tongyeong-Daejeon), 8(Jungbu-Naeryuk)</td></tr><tr><td>Leaf 2</td><td>49</td><td>4.361</td><td>4(West-coast), 6(Jungbu), 9(Yeongdong), 10(Jungang)</td></tr></table>

$$
\left( \begin{array}{c c c} A S _ {1 1} & \dots & A S _ {1 n} \\ \vdots & \ddots & \vdots \\ A S _ {m 1} & \dots & A S _ {m n} \end{array} \right) \left( \begin{array}{c} A W _ {1} \\ \vdots \\ A W _ {n} \end{array} \right) = \left( \begin{array}{c} C S _ {1} \\ \vdots \\ C S _ {m} \end{array} \right)\tag{1}
$$

where AS is the attribute similarity, AW is the attribute weight, CS is the case similarity, m is the number of cases, and n is the number of attributes.

First, the attribute similarity score can be calculated based on the differences between the independent variables. In case that the attribute is under a nominal scale or dummy scale, the attribute similarity is given as 1 if its value is the same; otherwise, it is 0. Meanwhile, in case that the attribute is under a numerical scale, the attribute similarity can be calculated by using Eq. (2) if it is more than the minimum criterion for scoring the attribute similarity (MCAS); otherwise, it is 0. For example, for leaf 1 in Phase 1 (‘usage rate of the ESA’), in case of calculating the attribute similarity of the passing traf<sup>fi</sup>c volume (under a numerical scale), its attribute similarity is calculated at 0.5947 (59.47%) when the standardized value (1.000) of case No. 1 and that (0.595) of case No. 46 are applied to Eq. (2). If MCAS is set at 50%, the score of the attribute similarity becomes valid. However, if MCAS is set at 70%, the score of the attribute similarity is not recognized, and thus a score of 0 is given. The MCAS can be changed within a de<sup>fi</sup>ned range in GA. It is applied to the optimization process in Section 3.3.2 to <sup>fi</sup>nd its best value.

$$
f _ {A S} (x) = \left\{ \begin{array}{c l} 1 0 0 - \left(\frac {\left| A V _ {\text {Test\_Case}} - A V _ {\text {Retrieved\_Case}} \right|}{A V _ {\text {Test\_Case}}} \times 1 0 0\right) & \text {if} f _ {A S} (x) \geq \text {MCAS} \\ 0 & \text {if} f _ {A S} (x) <   \text {MCAS} \end{array} \right.\tag{2}
$$

where $f _ { A S }$ is the function for calculating the attribute similarity, $A V _ { t e s t - c a s e }$ is the attribute value of the test case, $A V _ { r e t r i e v e d - c a s e }$ is the attribute value of the retrieved case, and MCAS is the minimum criterion for scoring the attribute similarity.

Second, the case similarity score can be calculated using Eq. (3): (i) the weighted-attribute similarity can be derived by multiplying the attribute similarity with the attribute weight of all independent variables; and (ii) its accumulated sum was divided by the accumulated sum of the attribute weight. Meanwhile, in the previous studies [49, 50], it was concluded that GA was the best method of calculating the attribute weight in CBR method. Accordingly, GA is used to optimize the value of the attribute weight for the purpose of the maximization of the prediction accuracy. The attribute weights can be changed within a de<sup>fi</sup>ned range in GA. The range of attribute weight (RAW) is applied to the optimization process in Section 3.3.2 to <sup>fi</sup>nd the best value for the attribute weight.

$$
f _ {C S} (x) = \frac {\sum_ {i = 1} ^ {n} \left(f _ {A W _ {i}} \times f _ {A S _ {i}}\right)}{\sum_ {i = 1} ^ {n} \left(f _ {A W _ {i}}\right)}\tag{3}
$$

where $f _ { C S }$ is the function for calculating the case similarity, $f _ { A W }$ is the function for calculating the attribute weight, $f _ { A S }$ is the function for calculating the attribute similarity, and n is the number of attributes.

## 3.3.2. Improvement of the prediction accuracy using a genetic algorithm

Although the basic CBR method offers excellent explanatory power by presenting the historical data as a reference along with the prediction result, previous studies have shown that its prediction accuracy was relatively inferior to the other methodologies, like MRA or ANN. To address this challenge, this study proposed an A-CBR model that can be established by integrating MRA, ANN, and GA with the basic CBR method. The detailed explanation was discussed below [50–57].

The A-CBR model consists of three stages: (i) prediction accuracy calculation; (ii) <sup>fi</sup>ltering engine development; and (iii) GA application. First, predication accuracy can be calculated by considering the difference between the actual value and the predicted value of the dependent variable. This study used the mean absolute percentage error (MAPE), as shown in Eqs. (4) and (5).

$$
f _ {\text { MAPE }} (x) = \frac {1 0 0}{m} \times \sum_ {i = 1} ^ {m} \left| \frac {A V _ {i} - P V}{A V _ {i}} \right|,\tag{4}
$$

$$
f _ {P A} (x) = 1 0 0 - f _ {\mathrm{MAPE}} (x)\tag{5}
$$

where $f _ { \mathrm { M A P E } }$ is the function for calculating the mean absolute percentage error, AV is the actual value of the dependent variable, PV is the predicted value of the dependent variable, m is the number of cases, and $f _ { P A }$ is the function for calculating prediction accuracy.

Second, the <sup>fi</sup>ltering engine can be established by using the cross range between the predicted values of the MRA and ANN models (CRMA), as shown in Eqs. (6) to (9). In this process, the tolerance range of CRMA (TRCRMA) was used to give the buffer to the cross range (i.e., CRMA).

$$
P V _ {M R A} \times \left(1 - \frac {M A P E _ {M R A}}{1 0 0}\right) \leq P R _ {M R A} \leq P V _ {M R A} \times \left(1 + \frac {M A P E _ {M R A}}{1 0 0}\right),\tag{6}
$$

$$
P V _ {A N N} \times \left(1 - \frac {M A P E _ {A N N}}{1 0 0}\right) \leq P R _ {A N N} \leq P V _ {A N N} \times \left(1 + \frac {M A P E _ {A N N}}{1 0 0}\right)\tag{7}
$$

where $P R _ { M R A }$ is the predicted range of the MRA model, $P V _ { M R A }$ is the predicted value of the MRA model, $M A P E _ { M R A }$ is the mean absolute percentage error of the MRA model, $P R _ { \mathrm { A N N } }$ is the predicted range of the ANN model, $P V _ { A N N }$ is the predicted value of the ANN model, and $M A P E _ { \mathrm { A N N } }$ is the mean absolute percentage error of the ANN model.

$$
\operatorname{Max} \left(\operatorname{Min} \left(P R _ {M R A}\right), \operatorname{Min} \left(P R _ {\text {ANN}}\right)\right) \leq C R M A \leq \operatorname{Min} \left(\operatorname{Max} \left(P R _ {M R A}\right), \operatorname{Max} \left(P R _ {\text {ANN}}\right)\right),\tag{8}
$$

$$
\operatorname{Min} (\text { CRMA }) \times \left(1 - \frac {\text { TRCRMA }}{1 0 0}\right) \leq \text { CRMA } ^ {*} \leq \text { Max } (\text { CRMA }) \times \left(1 + \frac {\text { TRCRMA }}{1 0 0}\right)\tag{9}
$$

where CRMA is the cross-range between the predicted values of the MRA and ANN models, TRCRMA is the tolerance range of CRMA, and CRMA<sup>⁎</sup> is the <sup>fi</sup>ltering range in which TRCRMA was applied to CRMA.

Third, GA is a search algorithm to <sup>fi</sup>nd the optimal solution for the optimization objective (i.e., prediction accuracy). GA de<sup>fi</sup>nes a group of optimization parameters as a chromosome [40–44]. The genes were classi<sup>fi</sup>ed in four categories in this study: (i) MCAS; (ii) RAW; (iii) TRCRMA; and (iv) the range of case selection (RCS). As mentioned in Section 3.3.1, the MCAS and the RAW were used as key factors in calculating the case similarity. Also, the TRCRMA was used to establish the <sup>fi</sup>ltering range as mentioned in Eqs. (8) and (9). Furthermore, since this study presents the historical data as a reference along with the prediction result, it is the number of the retrieved cases that is important. Thus, the RCS was used as an optimization parameter. The software program ‘Evolver’ was used to conduct the optimization process using GA.

• Optimization parameter 1 (MCAS): To calculate the attribute similarity, MCAS was de<sup>fi</sup>ned as the optimization parameter within the range of 0–100% in GA.

• Optimization parameter 2 (RAW): To deduce the attribute weight, RAW was de<sup>fi</sup>ned as the optimization parameter within the range of 0.00–1.00 in GA.

• Optimization parameter 3 (TRCRMA): To determine a tolerance range which makes a <sup>fi</sup>ltering range to be effective, TRCRMA was de<sup>fi</sup>ned as the optimization parameter within the range of 0–100% in GA.

![](/api/attachments/YZEBY7MS/fulltext/images/58a7c6a3a27e2df4d01dc72ac28947cbae141984881170ec90fb12b2f2924792.jpg)  
Fig. 3. PDF for the sales per the building area of ESAs.

Please cite this article as: C. Koo, et al., A decision support system for determining the optimal size of a new expressway service area: Focused on the pro<sup>fi</sup>tability, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.07.005

• Optimization parameter 4 (RCS): To determine the number of similar cases that would be <sup>fi</sup>nally selected, RCS was de<sup>fi</sup>ned as the optimization parameter within the range of 0–100% in GA.

## 3.4. Development of the PDF for the sales per the building area of ESAs

Fig. 3 shows the PDF for the ‘sales per the building area of ESAs’, which can be established by using the ‘distribution fitting’ function of the software program ‘Crystal Ball’. Namely, as mentioned in Section 1, this study collected the project characteristics on a total of 106 general ESAs operated by KEC as of 2013, and then, this study calculated the ‘sales per the building area’ of 106 ESAs, which applied to the ‘distribution fitting’ function of the software program ‘Crystal Ball’.

The PDF can be used to estimate the ‘sales per the building area’ of a new ESA in Phase 3 (refer to Fig. 2). This study offered the percentile values (25%, 50%, and 75%) and the mean value as examples that can be used by the <sup>fi</sup>nal decision-maker. By applying the value selected from the PDF (i.e., the ‘sales per the building area’) to the estimated ‘sales of the ESA’ (which can be determined through Phase 1 and Phase 2), the building area of a new ESA can be <sup>fi</sup>nally determined as the optimal size, which can achieve the pro<sup>fi</sup>tability of the ESA.

## 4. Results and discussion

## 4.1. A comparison of the prediction performance by the methods

This study aimed to develop a decision support system for determining the optimal size of a new ESA, which consisted of three phases. Among the three phases, the A-CBR model was used to estimate the ‘usage rate of the ESA’ in Phase 1 and the ‘sales per vehicle’ in Phase 2. This study conducted a clustering analysis using DT, and then developed a hybrid model (i.e., A-CBR model) by integrating the various methodologies such as MRA, ANN, and GA with the basic CBR method.

First, Table 6 shows the prediction accuracy and the standard deviation of the proposed process (i.e., three-phase estimation), which were improved by 9.84% and 0.52%, respectively, compared to those of the conventional process (i.e., direct estimation). It can be concluded that the proposed process (i.e., three-phase estimation) is valid. Especially, the A-CBR model (77.62%) was superior to the other models such as CBR (51.51%), MRA (72.74%) and ANN (68.53%).

Second, according to the previous studies [48–57], although the basic CBR method has higher explanatory power, its prediction capacity is relatively lower than that of MRA or ANN model. However, the limitation can be overcome through the A-CBR model developed with DT. Namely, it was concluded that the A-CBR model developed with DT was improved in terms of not only the prediction accuracy but also the consistency of the predicted result.

• Phase 1: Table 7 shows the prediction performance by the methods that were used in Phase 1. The prediction accuracy and the standard deviation of the A-CBR model developed with DT (i.e., Tree & A-CBR model) were improved by 4.85% and 0.87%, respectively, compared to those without DT. Also, Tree & A-CBR model (85.96%) was superior

## Table 7

Comparison of the prediction performance by the methods used in Phase 1.

<table><tr><td>Phase</td><td colspan="2">Classification</td><td>Methodology</td><td> $APA^a$ </td><td> $SDPA^b$ </td></tr><tr><td rowspan="16">Phase 1(the usage rate of the ESA)</td><td rowspan="4">No tree</td><td rowspan="4">All data(106)</td><td>MRA</td><td>79.96</td><td>17.14</td></tr><tr><td>ANN</td><td>81.57</td><td>16.77</td></tr><tr><td>CBR</td><td>72.79</td><td>20.04</td></tr><tr><td>A-CBR</td><td>81.11</td><td>14.09</td></tr><tr><td rowspan="12">Use tree</td><td rowspan="4">Leaf 1(61)</td><td>Tree &amp; MRA</td><td>84.77</td><td>12.41</td></tr><tr><td>Tree &amp; ANN</td><td>81.69</td><td>17.49</td></tr><tr><td>Tree &amp; CBR</td><td>76.80</td><td>16.87</td></tr><tr><td>Tree &amp; A-CBR</td><td>86.96</td><td>12.78</td></tr><tr><td rowspan="4">Leaf 2(45)</td><td>Tree &amp; MRA</td><td>82.50</td><td>12.41</td></tr><tr><td>Tree &amp; ANN</td><td>83.35</td><td>11.28</td></tr><tr><td>Tree &amp; CBR</td><td>62.27</td><td>25.60</td></tr><tr><td>Tree &amp; A-CBR</td><td>84.65</td><td>13.81</td></tr><tr><td rowspan="4">Average</td><td>Tree &amp; MRA</td><td>83.80</td><td>12.40</td></tr><tr><td>Tree &amp; ANN</td><td>82.39</td><td>15.13</td></tr><tr><td>Tree &amp; CBR</td><td>70.63</td><td>22.12</td></tr><tr><td>Tree &amp; A-CBR</td><td>85.96</td><td>13.22</td></tr></table>

<sup>a</sup> APA stands for the average of the prediction accuracy.

<sup>b</sup> SDPA stands for the standard deviation of the prediction accuracy.

to the other methodologies (i.e., Tree & CBR (70.63%), Tree & MRA (83.80%) and Tree & ANN (82.39%)).

• Phase 2: Table 8 shows the prediction performance by the methods that were used in Phase 2. The prediction accuracy and the standard deviation of the A-CBR model developed with DT (i.e., Tree & A-CBR model) were improved by 3.42% and 4.95%, respectively, compared to those without DT. Also, Tree & A-CBR model (85.76%) was superior to the other methodologies (i.e., Tree & CBR (68.11%), Tree & MRA (80.71%) and Tree & ANN (80.26%)).

Third, Table 9 shows the detailed description of chromosome by the phases (i.e., four optimization parameters explained in Section 3.3.2) that were used in a GA. When a cluster was formed using DT and the four parameters (i.e., MCAS, RAW, RCS, and TRCRMA) were applied to the optimization process, the prediction accuracy was improved the most (i.e., Tree & A-CBR, 77.62%). The optimization parameters of the proposed A-CBR model were determined very differently. It indicates that it is necessary to determine the optimization parameters using a GA. The proposed A-CBR model was developed using 106 ESAs in South Korea. Thus, considering that the objective of this study was to develop a CBR-based decision support system, the prediction performance of the proposed A-CBR model will be improved further as additional data are accumulated in case base.

Meanwhile, the computational time required for the optimization of the proposed A-CBR model was determined to be less than 10 min (i.e., 9.93 min for Leaf 1 in Phase 1; 1.75 min for Leaf 2 in Phase 1; 2.6 min for Leaf 1 in Phase 2; and 7.9 min for Leaf 2 in Phase 2). Namely, the <sup>fi</sup>nal decision-maker requires the aforementioned computational time for the optimization process in case of updating the proposed A-CBR model.

## Table 6

Comparison of prediction performance between conventional and proposed process.

<table><tr><td>Classification</td><td>Dependent variables</td><td>Methodology</td><td>APA</td><td>SDPA</td></tr><tr><td rowspan="4">Conventional process (i.e., direct estimation)</td><td rowspan="4">The sales in the ESA</td><td>MRA</td><td>52.33</td><td>57.11</td></tr><tr><td>ANN</td><td>55.28</td><td>58.28</td></tr><tr><td>CBR</td><td>59.00</td><td>24.59</td></tr><tr><td>A-CBR</td><td>67.78</td><td>18.09</td></tr><tr><td rowspan="4">Proposed process (i.e., three-phase estimation)</td><td>Phase 1</td><td>MRA</td><td>72.74</td><td>24.47</td></tr><tr><td rowspan="2">(the usage rate of the ESA) &amp; Phase 2</td><td>ANN</td><td>68.53</td><td>28.99</td></tr><tr><td>CBR</td><td>51.51</td><td>52.46</td></tr><tr><td>(the sales per vehicle)</td><td>A-CBR</td><td>77.62</td><td>17.57</td></tr></table>

Note: APA stands for the average of the prediction accuracy; and SDPA stands for the standard deviation of the prediction accuracy.

Please cite this article as: C. Koo, et al., A decision support system for determining the optimal size of a new expressway service area: Focused on the pro<sup>fi</sup>tability, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.07.005

Table 9  
Table 8  
Comparison of the prediction performance by the methods used in Phase 2.

<table><tr><td>Phase</td><td colspan="2">Classification</td><td>Methodology</td><td> $APA^a$ </td><td> $SDPA^b$ </td></tr><tr><td rowspan="16">Phase 2(the sales per vehicle)</td><td rowspan="4">No tree</td><td rowspan="4">All data(106)</td><td>MRA</td><td>76.50</td><td>25.07</td></tr><tr><td>ANN</td><td>78.52</td><td>22.15</td></tr><tr><td>CBR</td><td>70.83</td><td>21.04</td></tr><tr><td>A-CBR</td><td>82.34</td><td>16.50</td></tr><tr><td rowspan="12">Use tree</td><td rowspan="4">Leaf 1(57)</td><td>Tree &amp; MRA</td><td>78.66</td><td>19.93</td></tr><tr><td>Tree &amp; ANN</td><td>78.98</td><td>21.93</td></tr><tr><td>Tree &amp; CBR</td><td>66.90</td><td>32.95</td></tr><tr><td>Tree &amp; A-CBR</td><td>85.65</td><td>12.57</td></tr><tr><td rowspan="4">Leaf 2(49)</td><td>Tree &amp; MRA</td><td>83.09</td><td>16.49</td></tr><tr><td>Tree &amp; ANN</td><td>81.75</td><td>17.64</td></tr><tr><td>Tree &amp; CBR</td><td>69.19</td><td>22.45</td></tr><tr><td>Tree &amp; A-CBR</td><td>85.88</td><td>10.36</td></tr><tr><td rowspan="4">Average</td><td>Tree &amp; MRA</td><td>80.71</td><td>18.47</td></tr><tr><td>Tree &amp; ANN</td><td>80.26</td><td>20.02</td></tr><tr><td>Tree &amp; CBR</td><td>68.11</td><td>28.73</td></tr><tr><td>Tree &amp; A-CBR</td><td>85.76</td><td>11.55</td></tr></table>

Note:  
<sup>a</sup> APA stands for the average of the prediction accuracy.  
<sup>b</sup> SDPA stands for the standard deviation of the prediction accuracy.

## 4.2. Model application

A case study was conducted to verify the reliability and applicability of the proposed system for determining the optimal size of a new ESA. Using the proposed system, the <sup>fi</sup>nal decision-maker can estimate the optimal size of a new ESA, resulting in achieving the pro<sup>fi</sup>tability of the ESA. Namely, the <sup>fi</sup>nal decision-maker can estimate the optimal size of the ESA, based on the estimated sales in a new ESA. The detailed process for the case study is as follows:

• Phase 1: The ‘usage rate of the ESA’ can be estimated by using the proposed A-CBR model. Using the estimated result, ‘the number of daily vehicles’ can be estimated, based on the ‘passing traffic volume’;

• Phase 2: The ‘sales per vehicle’ can be estimated using the proposed A-CBR model. Using the estimated result, the ‘sales in the ESA’ can be estimated, based on ‘the number of daily vehicles’; and,

• Phase 3: The <sup>fi</sup>nal decision-maker can use the PDF to establish the potential pro<sup>fi</sup>tability (e.g., percentile 25%, 50%, and 75%) of a new ESA. By applying the established value (i.e., for the ‘sales per the building area’) to the expected ‘sales in the ESA’, the study can estimate the optimal size of the building area (including both the business facility and the operation facility).

Table 10  
Detailed characteristics of ‘W’ ESA as the case study

<table><tr><td>Classification</td><td>Detailed description</td></tr><tr><td>Name of expressway service area</td><td>‘W’ ESA</td></tr><tr><td>Passing traffic volume</td><td>12,031</td></tr><tr><td>Name of expressway</td><td>Jungang expressway</td></tr><tr><td>Direction of expressway</td><td>Northbound lane</td></tr><tr><td>Location from IC/JC</td><td>Upstream</td></tr><tr><td>Position ratio (%)</td><td>42.65</td></tr><tr><td>Distance from downstream service area (km)</td><td>29.0</td></tr><tr><td>Distance from upstream service area (km)</td><td>39.0</td></tr><tr><td>Petrol station</td><td>Yes</td></tr><tr><td>LPG station</td><td>No</td></tr><tr><td>Auto repair shop</td><td>No</td></tr></table>

This study selected ‘W’ ESA as the case study, which was under de<sup>fi</sup>cit operation as of 2013. Table 10 shows the detailed characteristics of ‘W’ ESA as the case study. The detailed analysis results of the case study are as follows:

First, Table 11 shows the estimation of the ‘usage rate of the ESA’ of ‘W’ ESA by using the A-CBR model in Phase 1. The <sup>fi</sup>ve similar cases (i.e., case nos. 101, 25, 70, 53, and 100) were retrieved from the historical cases, and the average of the ‘usage rate of the ESA’ in these <sup>fi</sup>ve similar cases was determined to be at 20.40%. By applying the estimated ‘usage rate of the ESA’ (20.40%) to the ‘passing traffic volume’ (12,031 (vehicles/day)) of the zone at which ‘W’ ESA is located, the case study resulted in 2453.9 (vehicles/day) as ‘the number of daily vehicles’.

Second, Table 12 shows the estimation of the ‘sales per vehicle’ of ‘W’ ESA by using the A-CBR model in Phase 2. The three similar cases (i.e., case nos. 70, 45 and 64) were retrieved from the historical cases, and the average of the ‘sales per vehicle’ in these three similar cases was determined to be at 3.728 (\$/vehicle). By applying the estimated ‘sales per vehicle’ (3.728 (\$/vehicle)) to ‘the number of daily vehicles’ (2453.9 (vehicles/day)) which was estimated in Phase 1 (refer to Table 11), the case study resulted in 3339.3 (thousand \$/yr.) as the ‘sales in the ESA’.

Third, Table 13 shows the estimation of the optimal building area of ‘W’ ESA by using the PDF in Phase 3. Compared to the estimated building area, which was determined by using the improved process (i.e., threephase estimation process), it was determined that the actual building area (3663.0 m<sup>2</sup>) of ‘W’ ESA, which was determined by using the conventional process, was overestimated. If the ‘sales per the building

Detailed description of the optimization results in a genetic algorithm.

<table><tr><td rowspan="2" colspan="4">Classification</td><td colspan="2">Phase 1</td><td colspan="2">Phase 2</td></tr><tr><td>Leaf1</td><td>Leaf2</td><td>Leaf1</td><td>Leaf2</td></tr><tr><td rowspan="19">Chromosome</td><td>MCAS</td><td></td><td></td><td>0.831</td><td>0.261</td><td>0.132</td><td>0.269</td></tr><tr><td rowspan="16">RAW</td><td>Passing traffic volume</td><td></td><td>0.208</td><td>0.848</td><td>0.879</td><td>0.839</td></tr><tr><td>Name of the expressway</td><td></td><td>0.991</td><td>0.654</td><td>0.524</td><td>0.325</td></tr><tr><td rowspan="2">Direction of the expressway</td><td>Northbound lane</td><td>0.365</td><td>0.319</td><td>0.242</td><td>0.844</td></tr><tr><td>Southbound lane</td><td>0.084</td><td>0.401</td><td>0.107</td><td>0.676</td></tr><tr><td rowspan="3">Location from the intersection/junction</td><td>Upstream</td><td>0.052</td><td>0.557</td><td>0.082</td><td>0.715</td></tr><tr><td>Downstream</td><td>0.648</td><td>0.704</td><td>0.164</td><td>0.468</td></tr><tr><td>Normal</td><td>0.310</td><td>0.179</td><td>0.183</td><td>0.568</td></tr><tr><td>Distance from the upstream service area</td><td></td><td>0.415</td><td>0.863</td><td>0.193</td><td>0.157</td></tr><tr><td>Distance from the downstream service area</td><td></td><td>0.561</td><td>0.217</td><td>0.246</td><td>0.557</td></tr><tr><td rowspan="4">Position ratio</td><td>Quartile1</td><td>0.865</td><td>0.617</td><td>0.338</td><td>0.666</td></tr><tr><td>Quartile2</td><td>0.326</td><td>0.371</td><td>0.483</td><td>0.529</td></tr><tr><td>Quartile3</td><td>0.150</td><td>0.440</td><td>0.180</td><td>0.205</td></tr><tr><td>Quartile4</td><td>0.569</td><td>0.542</td><td>0.157</td><td>0.324</td></tr><tr><td>Petrol station</td><td></td><td>0.458</td><td>0.808</td><td>0.745</td><td>0.226</td></tr><tr><td>LPG station</td><td></td><td>0.481</td><td>0.513</td><td>0.484</td><td>0.535</td></tr><tr><td>Auto repair shop</td><td></td><td>0.222</td><td>0.317</td><td>0.575</td><td>0.915</td></tr><tr><td>TRCRMA</td><td></td><td></td><td>0.005</td><td>0.050</td><td>0.054</td><td>0.016</td></tr><tr><td>RCS</td><td></td><td></td><td>0.180</td><td>0.150</td><td>0.090</td><td>0.140</td></tr><tr><td colspan="4">Optimization time (minute)</td><td>9.93</td><td>1.75</td><td>2.6</td><td>7.9</td></tr></table>

Please cite this article as: C. Koo, et al., A decision support system for determining the optimal size of a new expressway service area: Focused on the pro<sup>fi</sup>tability, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.07.005

Estimation of the <sup>‘</sup>usa<sub>g</sub>e rate of the ESA<sup>’</sup> of <sup>‘</sup>W<sup>’</sup> ESA b<sub>y</sub> usin<sub>g</sub> the A-CBR model in Phase 1

<table><tr><td>Variable</td><td>Case No.</td><td>Passing traffic volume (vehicles/day)</td><td>Name of expressway</td><td>Direction of expressway</td><td>Location from IC/JC</td><td>Position ratio</td><td>Distance from downstream service area</td><td>Distance from upstream service area</td><td>Petrol station</td><td>LPG</td><td>Auto repair shop</td><td>Usage rate of the ESA (%)</td><td>The number of daily vehicles (vehicles/day)</td></tr><tr><td>Test case</td><td>-</td><td>12,031</td><td>Jungang expressway</td><td>Northbound lane</td><td>Upstream</td><td>42.65</td><td>29.0</td><td>39.0</td><td>1</td><td>0</td><td>0</td><td>20.40</td><td>2453.9</td></tr><tr><td>Retrieved case 1</td><td>101</td><td>6827</td><td>Jungang expressway</td><td>Northbound lane</td><td>Upstream</td><td>60.34</td><td>68.0</td><td>44.7</td><td>1</td><td>0</td><td>0</td><td>19.72</td><td></td></tr><tr><td>Retrieved case 2</td><td>25</td><td>13,103</td><td>Namhae expressway</td><td>Northbound lane</td><td>Downstream</td><td>40.63</td><td>26.0</td><td>38.0</td><td>1</td><td>1</td><td>0</td><td>18.98</td><td></td></tr><tr><td>Retrieved case 3</td><td>70</td><td>10,358</td><td>Jungbu expressway</td><td>Northbound lane</td><td>Upstream</td><td>36.11</td><td>26.0</td><td>46.0</td><td>1</td><td>1</td><td>0</td><td>19.34</td><td></td></tr><tr><td>Retrieved case 4</td><td>53</td><td>10,983</td><td>Honam expressway</td><td>Northbound lane</td><td>Downstream</td><td>30.95</td><td>26.0</td><td>58.0</td><td>1</td><td>0</td><td>0</td><td>21.32</td><td></td></tr><tr><td>Retrieved case 5</td><td>100</td><td>10,413</td><td>Jungang expressway</td><td>Northbound lane</td><td>Downstream</td><td>37.04</td><td>40.0</td><td>68.0</td><td>1</td><td>1</td><td>0</td><td>22.63</td><td></td></tr></table>

Estimation of the <sup>‘</sup>sales <sub>p</sub>er vehicle<sup>’</sup> of <sup>‘</sup>W<sup>’</sup> ESA b<sub>y</sub> usin<sub>g</sub> the A-CBR model in Phase 2

<table><tr><td>Variable</td><td>Case No.</td><td>Passing traffic volume (vehicles/day)</td><td>Name of expressway</td><td>Direction of expressway</td><td>Location from IC/JC</td><td>Position ratio</td><td>Distance from downstream service are</td><td>Distance from upstream service area</td><td>Petrol station</td><td>LPG</td><td>Auto repair shop</td><td>Sales per vehicle ($/vehicle)</td><td>Sales in the ESA (thousand $/year)</td></tr><tr><td>Test Case</td><td>-</td><td>12,031</td><td>Jungang expressway</td><td>Northbound lane</td><td>Upstream</td><td>42.65</td><td>29.0</td><td>39.0</td><td>1</td><td>0</td><td>0</td><td>3.728</td><td>3339.3</td></tr><tr><td>Retrieved case 1</td><td>70</td><td>10,358</td><td>Jungbu expressway</td><td>Northbound lane</td><td>Upstream</td><td>36.11</td><td>26.0</td><td>46.0</td><td>1</td><td>1</td><td>0</td><td>4.169</td><td></td></tr><tr><td>Retrieved case 2</td><td>45</td><td>58,417</td><td>West-coast expressway</td><td>Northbound lane</td><td>Upstream</td><td>39.39</td><td>26.0</td><td>40.0</td><td>1</td><td>1</td><td>0</td><td>3.209</td><td></td></tr><tr><td>Retrieved case 3</td><td>64</td><td>33,030</td><td>Jungbu expressway</td><td>Northbound lane</td><td>Upstream</td><td>50.00</td><td>33.0</td><td>33.0</td><td>1</td><td>1</td><td>0</td><td>3.807</td><td></td></tr></table>

Note : The exchange rate ( KRW/USD ) is 1 1 63 5 won to a U S dollar ( as of 24 June 201 3 )

Table 13  
Estimation of the optimal building area of ‘W’ ESA by using the PDF in Phase 3.

<table><tr><td>Class</td><td colspan="2">The sales per the building area (thousand $/year/m2)</td><td>Estimated building area (m2)</td><td>Actual building area (m2)</td><td>Deviation (m2)</td></tr><tr><td>Alt. 1</td><td>Percentile 25%</td><td>1.140</td><td>2929.2</td><td>3663.0</td><td>+733.8 (1.25)</td></tr><tr><td>Alt. 2</td><td>Percentile 50%</td><td>1.729</td><td>1931.4</td><td></td><td>+1731.6 (1.90)</td></tr><tr><td>Alt. 3</td><td>Mean</td><td>1.951</td><td>1711.6</td><td></td><td>+1951.4 (2.14)</td></tr><tr><td>Alt. 4</td><td>Percentile 75%</td><td>2.524</td><td>1323.0</td><td></td><td>+2340.0 (2.77)</td></tr></table>

area’ of the ESA is set higher to improve the operational ef<sup>fi</sup>ciency of the ESA, the difference between the actual building area (3663.0 m<sup>2</sup>) and the estimated building area is more increased. For example, in case of establishing the ‘sales per the building area’ of the ESA within the 75% level (refer to Alt. 4 in Table 13), the building area of ‘W’ ESA can be estimated at 1323.0 (m<sup>2</sup>). Accordingly, it was shown that the difference between the actual building area and the estimated building area was determined to be at 2340.0 (m<sup>2</sup>), and thus, the actual building area (3663.0 (m<sup>2</sup>)) was overestimated by 2.77 times than the estimated building area (1323.0 (m<sup>2</sup>)). Using the proposed system, it can be expected that the <sup>fi</sup>nal decision-maker can determine the optimal size of a new ESA, which can achieve the pro<sup>fi</sup>tability of the ESA.

## 5. Conclusions

This study aimed to develop a CBR-based decision support system for determining the optimal size of a new ESA, focusing on the pro<sup>fi</sup>tability of the ESA. To strengthen the advantage of the CBR approach (i.e., excellent explanatory power by presenting the historical data as a reference) and make up for the weakness (i.e., its prediction accuracy that is relatively inferior to the other methods, like MRA or ANN), this study developed the A-CBR model by integrating MRA, ANN, and GA with the basic CBR method. This study was conducted in four steps: (i) setting the case-base; (ii) formation of a cluster using DT; (iii) development of an A-CBR model; and (iv) development of the PDF for the sales per the building area of ESAs. The results of this study can be summarized as follows:

• First, compared to the conventional process (i.e., direction estimation), the prediction accuracy of the improved process (i.e., threephase estimation process) was improved by 9.84%. It means that the proposed three-phase estimation process is valid. In addition, it indicates that the impact factors (i.e., independent variables), which were established through the interviews with ESA experts and the extensive literature review, are well established enough to explain whether the size of the ESA is proper or not.

• Second, it was determined that the proposed A-CBR model was the most superior to the other methodologies such as the MRA and ANN, resulting in 85.96% of the prediction accuracy in Phase 1 and 85.76% of that in Phase 2. Namely, the proposed A-CBR model overcame the weakness of the basic CBR model, of which prediction accuracy is usually lower than that of the MRA or ANN model.

• Third, the optimization parameters of the proposed A-CBR model were determined very differently. It means that it is necessary to determine the optimization parameters using a GA. Also, the computational time required for the optimization of the proposed A-CBR model was determined to be less than 10 min (from 1.75 min to 9.93 min). The <sup>fi</sup>nal decision-maker requires the aforementioned computational time for the optimization process in case of updating of the proposed A-CBR model.

• Fourth, the case study showed that the actual building area of ‘W’ ESA by using the conventional process was overestimated, compared to the estimated building area by using the improved process (i.e., three-phase estimation process). In the case of establishing the ‘sales per the building area’ of the ESA within the 75% level, it was determined that the actual building area of ‘W’ ESA was overestimated by 2.77 times. As using the proposed system, it can be expected that the <sup>fi</sup>nal decision-maker can determine the optimal size of a new ESA, focusing on the pro<sup>fi</sup>tability of the ESA.

The proposed system can be used for the following purposes: (i) the probability estimation model for determining the optimal size of a new ESA during the planning stage; (ii) the approximate initial construction cost estimation model for a new ESA by using the estimated sales in the ESA; and (iii) the comparative assessment model for evaluating the sales per the building area of the existing ESA.

This study has limitations, and the research team hopes to solve them in future research: (i) the research team will present the stepby-step expansion strategies by conducting the time-series analysis on the usage pattern of ESAs. To achieve this, the research team should collect the time-series data on the sales of the speci<sup>fi</sup>c ESA as well as the change in the associated policy and the surrounding environment; and (ii) the research team will analyze the usage rates of the ESA by considering the esthetic aspects of the ESA, such as ESA design or surrounding natural scenery. To achieve this, the research team should establish the qualitative evaluation criteria on the esthetic aspects, and then conduct the qualitative evaluation by using the Delphi technique with the expert group.

## Acknowledgements

This research was supported by a Basic Science Research Program through the National Research Foundation of Korea (NRF) funded by the Korean Ministry of Education, Science and Technology (No. NRF-2012R1A2A1A01004376).

## References

[1] Ministry of Land, Infrastructure and Transportation (MOLIT), Expressway Design Handbook (Section 9. Service Facility), 2009. (Seoul, Korea).

[2] Korea Research Institute for Human Settlements (KRIHS), KRIHS Policy Brief (164): Consideration of the Installation of a Highway Rest Area for the Safety of Road Users, 2008. (Seoul, Korea).

[3] S. Seo, Preference Location Modeling of Freeway Rest Area Using Analytic Hierarchy Process, (M.S. thesis) Hanyang University, Seoul, Korea, 2002.

[4] Ministry of Land, Infrastructure and Transportation (MOLIT), Guideline for Calculating the Size of the Toll Road Service Area, 2004. (Seoul, Korea).

[5] Korea Expressway Corporation (KEC), Improvement of the Size of Expressway Service Areas, 2004. (Seoul, Korea).

[6] Federal Highway Administration (FHWA), Study of Rest Area Truck Parking, Technical Report, US Department of Transportation, Washington, DC, 1990.

[7] Federal Highway Administration (FHWA), Commercial Drivers Rest Area Requirements, Technical Report, US Department of Transportation, Washington, DC, 1996.

[8] N.J. Garber, H. Wang, D. Charoenphol, Estimating the Supply and Demand for Commercial Heavy Truck Parking on Interstate Highways: A Case Study of I-81 in Virginia, Center for Transportation Studies, University of Virginia, Virginia, 2002.

[9] H. Wang, N.J. Garber, Estimation of the Demand for Commercial Truck Parking on Interstate Highways in Virginia, Center for Transportation Studies, University of Virginia Virginia. 2003

[10] Federal Highway Administration (FHWA), Commercial Driver Rest and Parking Requirements: Making Space for Safety, Technical Report, US Department of Transportation, Washington, DC, 1996.

[11] U. Gopi, Assessment of Commercial Driver Rest Area Needs, South Dakota Department of Transportation Pierre, SD 2000

[12] Federal Highway Administration (FHWA), Study of Adequacy of Commercial Truck Parking Facilities, Technical Report, US Department of Transportation, Virginia, 2002.

[13] C.J. Rodier, S.A. Shaheen, Commercial vehicle parking in California: exploratory evaluation of the problem and possible technology-based solution. California PATH Research Report, Institute of Transportation Studies, University of California, Berkeley, 2007.

[14] Federal Highway Administration (FHWA), Truckers' Park/Rest Facility Study, Technical Report, Illinois Center for Transportation, Illinois, 2008.

[15] T. Adams, P. Srivastava, B. Wang, L. Ogard, Low Cost Strategies to Increase Truck Parking in Wisconsin, Wisconsin Department of Transportation Research and Library Unit, Wisconsin, 2009.

[16] M. Florian, M. Gaudry, A conceptual framework for the supply side in transportation systems, Transportation Research Part B: Methodology 14 (1980) 1–8.

[17] F.M. Heinitz, N. Hesse, Estimating time-dependent demand for truck parking facilities along a federal highway, Journal of the Transportation Research Board 2097 (2009) 26–34.

[18] M. Florian, M. Los, Impact of the supply of parking spaces on parking lot choice, Transportation Research Part B: Methodology 14 (1980) 155–163.

[19] N. Geroliminis, M.G. Karlaftis, A. Skabardonis, A spatial queuing model for the emergency vehicle districting and location problem, Transportation Research Part B: Methodology 43 (2009) 798–811.

[20] J.D. Hunt, S. Teply, A nested logit model of parking location choice, Transportation Research Part B: Methodological 27 (1993) 253–265.

[21] D. Tsamboulas, P. Evgenikos, M.A. Strogyloudis, The <sup>fi</sup>nancial viability of motorway rest areas, Public Works Management & Policy 11 (2006) 63–77.

[22] S. Baek, C. Kim, A research on parking demand of freeway service area, Proceedings of the 2006 Korean Society of Civil Engineers Conference, 2006, pp. 3573–3576.

[23] Y. Choi, S. Baek, A study on proper size of an expressway service area, Journal of Korean Society of Transportation 27 (2009) 7–18.

[24] T. Kim, J. Won, S. Lee, Estimating parking lot space for freeway service area, Proceedings of the 2003 Korea Planner Association Conference, 2003, pp. 609–620.

[25] T. Kim, J. Won, H. Kang, K. Kim, The development of parking space demand estimation models for freight vehicles in freeway rest areas, Journal of Korea Planner Association 41 (2006) 243–253.

[26] A.Z. Al-Garni, S.M. Zubair, J.S. Nizami, A regression model for electric energy consumption forecasting in Eastern Saudi Arabia, Energy 19 (1994) 1043–1049.

[27] F. Egelioglu, A.A. Mohamada, H. Guven, Economic variables and electricity consumption in Northern Cyprus, Energy 26 (2001) 355–362.

[28] M. Ranjan, V.K. Jain, Modeling of electric energy consumption in Delhi, Energy 24 (1999) 351–361.

[29] G.K.F. Tso, K.K.W. Yau, A study of domestic energy usage pattern in Hong Kong, Energy 28 (2003) 1671–1682.

[30] Y.Y. Yan, Climate and residential electricity consumption in Hong Kong, Energy 23 (1998) 17–20.

[31] K. Dahal, K. Almejalli, M.A. Hossain, Decision support for coordinated road traf<sup>fi</sup>c control actions, Decision Support Systems 54 (2013) 962–975.

[32] H.C.W. Lau, G.T.S. Ho, Y. Zhao, A demand forecast model using a combination of surrogate data analysis and optimal neural network approach, Decision Support Systems 54 (2013) 1404–1416.

[33] L. Ekonomou, Greek long-term energy consumption prediction using arti<sup>fi</sup>cial neural networks, Energy 35 (2010) 512–517.

[34] R.J. Kuo, K.C. Xue, A decision support system for sales forecasting through fuzzy neural networks with asymmetric fuzzy weights, Decision Support Systems 24 (1998) 105–126.

[35] M. Müller, E. Wiederhold, Applying decision tree methodology for rules extraction under cognitive constraints, European Journal of Operational Research 136 (2002) 282-289

[36] O.R.L. Sheng, C.P. Wei, P.J.H. Hu, N. Chang, Automated learning of patient image retrieval knowledge: neural networks versus inductive decision trees. Decision Support Systems 30 (2000) 105-124

[37] A. Pla, B. López, P. Gay, C. Pous, eXiT<sup>⁎</sup>CBR.v2: distributed case-based reasoning tool for medical prognosis, Decision Support Systems 54 (2013) 1499–1510.

[38] S.Z. Dogan, D. Arditi, H.M. Gunaydin, Determining attribute weights in a CBR model for early cost prediction of structural systems, Journal of Construction and Engineering Management 132 (2006) 1092–1098.

[39] P. Duverlie, J.M. Castelain, Cost estimation during design step: parametric method versus case based reasoning method, Journal of Advanced Manufacturing Technology 15 (1999) 895–906.

[40] R.L. Haupt, S.E. Haupt, Practical Genetic Algorithms, 2nd edition John Wiley & Sons Inc., Hoboken, New Jersey, 2004.

[41] M. Karlsson, The MIND method: a decision support for optimization of industrial energy systems — principles and case studies, Applied Energy 88 (2011) 577–589.

[42] P.C. Chang, C.Y. Lai, K.R. Lai, A hybrid system by evolving case-based reasoning with genetic algorithm in wholesaler's returning book forecasting, Decision Support Systems 42 (2006) 1715–1729.

[43] R. Balling, B. Powell, M. Saito, Generating future land-use and transportation plans for high-growth cities using a genetic algorithm, Computer-Aided Civil and Infrastructure Engineering 19 (2004) 213–222.

[44] T. Hsieh, H. Liu, Genetic algorithm for optimization of infrastructure investment under time-resource constraint, Computer-Aided Civil and Infrastructure Engineering 19 (2004) 203–212.

[45] S. Guericke, A. Koberstein, F. Schwartz, S. Voß, A stochastic model for the implementation of postponement strategies in global distribution networks, Decision Support Systems 53 (2012) 294–305.

[46] Z. Lounis, D.J. Vanier, A multiobjective and stochastic system for building maintenance management, Computer-Aided Civil and Infrastructure Engineering 15 (2000) 320–329.

[47] I. Watson, Applying Case-Based Reasoning: Techniques for Enterprise Systems, Morgan Kaufmann Publishers, Inc., San Francisco, California, 1997.

[48] C. Koo, T. Hong, C. Hyun, K. Koo, A CBR-based hybrid model for predicting a construction duration and cost based on project characteristics in multi-famil housing projects, Canadian Journal of Civil Engineering 37 (2010) 739–752

[49] C. Koo, T. Hong, C. Hyun, S. Park, J. Seo, A study on the development of a cost model based on the owner's decision-making at the early stages of a construction project, International Journal of Strategic Property Management 14 (2010) 121–137.

[50] C. Koo, T. Hong, C. Hyun, The development of a construction cost prediction model with improved prediction capacity using the advanced CBR approach. Expert Systems with Applications: An International Journal 38 (2011) 8597–8606.

[51] T. Hong, C. Koo, S. Park, A decision support model for improving a multi-family housing complex based on CO emission from gas energy consumption, Building and Environment 52 (2012) 142–151.

[52] T. Hong, C. Koo, H. Kim, A decision support model for improving a multi-family housing complex based on CO emission from electricity consumption, Journal of Environmental Management 112 (2012) 67–78.

[53] T. Hong, C. Koo, K. Jeong, A decision support model for reducing electric energy consumption in elementary school facilities, Applied Energy 95 (2012) 253–266.

[54] C. Koo, T. Hong, M. Lee, H. Park, Estimation of the monthly average daily solar radiation using geographical information system and advanced case-based reasoning, Environmental Science & Technology 47 (2013) 4829–4839

[55] T. Hong, C. Koo, H. Kim, H. Park, Decision support model for establishing the optimal energy retro<sup>fi</sup>t strategy for existing multi-family housing complexes, Energy Policy 66 (2014) 157–169.

[56] C. Koo, T. Hong, M. Lee, H. Park, Development of a new energy ef<sup>fi</sup>ciency rating system for the existing residential buildings, Energy Policy 68 (2014) 218–231.

[57] M. Lee, C. Koo, T. Hong, H. Park, Framework for the mapping of the monthly average daily solar radiation using an advanced case-based reasoning and a geostatistical technique, Environmental Science & Technology 48 (2014) 4604–4612.

Choongwan Koo is a Postdoctoral Fellow in the Department of Architectural Engineering at Yonsei University, Seoul, Republic of Korea. Before attending Yonsei University, he worked at a global construction management company called ‘HanmiGlobal Corporation as an associate researcher. His primary research areas include decision support systems, data mining, new renewable energy, solar photovoltaic system, energy policy, dynamic energy performance, carbon emissions reduction, life cycle cost, and life cycle assessment.

Taehoon Hong is an associate professor in the Department of Architectural Engineering at Yonsei University, Seoul, Republic of Korea. He is an Editor-in-Chief in the Journal of Construction Engineering and Project Management, KICEM and an associate editor in the Journal of Management in Engineering, ASCE. Also, he is also a member of academic or practical institutes such as AIK, KSCE, ASCE, and KICEM. His main research areas include life cycle cost analysis, life cycle assessment, decision support systems, infrastructure asset management, facility management, and construction project cost control.

Jimin Kim is a graduate research assistant and Ph.D. student in the Department of Architectural Engineering at Yonsei University, Seoul, Republic of Korea. His primary research areas include time and cost optimization for construction projects, decision support systems, carbon emission reduction, life cycle cost, and life cycle assessment.
