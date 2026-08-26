---
otero_id: 1260
otero_key: "FB26FCQ6"
title: "Assessing the impacts of South-to-North Water Transfer Project with decision support systems"
authors: "Shan Feng; Ling Xia Li; Zhi Gang Duan; Jin Long Zhang"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.11.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Assessing the impacts of South-to-North Water Transfer Project with decision support systems

Shan Feng <sup>a,\*</sup>, Ling Xia Li <sup>b</sup>, Zhi Gang Duan <sup>a</sup>, Jin Long Zhang <sup>c</sup>

<sup>a</sup> Institute of Systems Engineering, Huazhong University of Science and Technology, Wuhan 430074, China <sup>b</sup> Department of Information Technology and Decision Sciences, Old Dominion University, Norfolk, VA 23529, USA <sup>c</sup> School of Management, Huazhong University of Science and Technology, Wuhan 430074, China

Available online 1 January 2005

## Abstract

The South to North Water Transfer Project is one of the four largest trans-century projects in China, which is expected to be completed by 2008. The project seeks to promote Northern China’s economic growth by relaxing water constraints in a region now facing severe water shortage. In this paper, a decision support system (DSS) for assessing the social–economic impact of China’s South-to-North (S2N) Water Transfer project is presented. The DSS provides decision support through simulation with an embedded water computable general equilibrium model (WCGE). The system is able to perform qualitative analysis on regional water resource vulnerability with mathematical modeling. In addition, the system is also able to examine a region’s water demand–supply balance dynamics through forecasting with the WCGE model on the basis of various scenarios for the time horizon up to the year 2020. The what-if analysis performed by the DSS shows that the incremental water supply from the project helps the recipient region to catch up with the development pace of the country as a whole. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: DSS; Modeling; Simulation; Forecasting; Water resource management; Sustainable development

## 1. Introduction

## 1.1. Background

Among all the natural resources available to mankind, water is the most essential resource for the sustainable development of human society. When people enjoy increasingly prosperous life based on industrialization, they pay a price related to environmental and ecological losses, particularly in developing countries with fast-growing populations [19]. These countries may find dilemmas facing them. Water resources may be constrained due to direct demand by masses of people, and due to the growing water needs of various industries. China, with a population of 1.27 billion in year 2000, is a typical country that needs to carry out proper water management policies in order to attain its national economic development goal of <sup>b</sup>Xiaokang<sup>Q</sup> or <sup>b</sup>moderate prosperity society<sup>Q</sup> by the year 2020.

Table 2

China is a large continental country with large water resource endowments of 2800 billion $\mathrm { m } ^ { 3 }$ and per unit continent water resource of $2 9 1 . 7 ~ \mathrm { k m } ^ { 3 }$ per $\mathrm { k m } ^ { 2 }$ , the level is only slightly lower than the global average water resource level of 315.1 km<sup>3</sup> per km<sup>2</sup>. However, due to China’s population of $1 2 . 6 5 \times 1 0 ^ { 8 }$ in the year 2000, this has led to a water occupation of $2 1 9 \dot { 6 } \mathrm { ~ m } ^ { 3 }$ per capita, approximately only about 1/4 of the global average level 8618 $\mathrm { i n } ^ { 3 }$ per capita [5]. Therefore, on a per capita basis, China has been grouped as 1 of the 13 countries with the most severe water scarcity like Kuwait, Saudi Arabia, Israel, and so on. If the factor of geographical distribution of water is further considered, there is another picture of heterogeneity. See Table 1 for basic information.

The position of lowest water occupation per capita is not to suggest that there are no regions within China with a relative water surplus. From Table 1 which collects some interesting statistics related to water resources of the world and China, one can see that the southern China region—south to Yangtse River, is relatively abundant with water resources. It shows that the availability of water resources for every Chinese inhabitant is quite different based upon their residential location, $\mathrm { e . g . , }$ in northern China, water availability is about 900 $\mathrm { m } ^ { 3 }$ per capita, which is lower than the water stress or severe scarcity criterion of less than $1 0 0 0 ~ \mathrm { m } ^ { 3 }$ per capita, given by United Nations (refer to Table 2).

In China, population growth has been at a fast pace, and the progress of industrialization has also been very fast. These changes have put water resources both in quantity and quality under direct or indirect stress and strain. The water supply–demand balance has come under constant pressure. Some of these trends are under way. In addition, regional acidification from industrial activity, water pollution (indirectly through air pollution and directly through discharge of pollutants from industrial activity and sewage disposal), desertification, and soil erosion are also major threats to water resources. All of the described changes come together to force an assessment of the carrying capacity of the biosphere of China, and limits may be reached in terms of sustainable level of development.

UN criterion for water resource scarcity degree (Unit: $\mathrm { m } ^ { 3 } /$ person)

<table><tr><td>Slightly scarce</td><td>Middle scarce</td><td>Severe scarce</td><td>Most severe scarce</td></tr><tr><td>1700–3000</td><td>1000–1700</td><td>500–1000</td><td>&lt;500</td></tr></table>

## 1.2. South-to-North water transfer project

South-to-North (S2N) Water Transfer Project is one of the four China’s largest trans-century projects aimed at transferring water from southern China to northern China to meet the increasing demand for water resources in northern China, where the storage of water has been a serious constraint to the regional economic development, and consequently, the resultant slower development has become an obstacle to the implementation of the country’s harmonic and sustainable development plan [13,27]. How will the water storage constraint be relaxed through the S2N project? Will water transferring improve the water shortage in northern China? These are major questions that need to be answered.

Table 1  
Water resource distribution and socioeconomic situation in China (year 2000)

<table><tr><td rowspan="2"></td><td rowspan="2">Typical city</td><td rowspan="2">Area $(10^{4} \text{km}^{2})$ </td><td colspan="2">Population index</td><td colspan="2">Economic index</td><td colspan="3">Water resource index</td></tr><tr><td>Population $(10^{8} \text{person})$ </td><td>Density $(\text{person/km}^{2})$ </td><td>GDP $(10^{8} \text{Yuan})$ </td><td>Average GDP(Yuan/Person)</td><td>Total waterresource $(10^{12} \text{m}^{3})$ </td><td>Water resourceper capita $(\text{m}^{3}/\text{person})$ </td><td>Exploitationrate in 1997(%)</td></tr><tr><td>China</td><td></td><td>960</td><td>12.65</td><td>131.8</td><td>97,209</td><td>7684.5</td><td>2.800</td><td>2196</td><td>25.8</td></tr><tr><td>NorthernChina</td><td>Beijing, Tianjin,Shenyang, Xian,Lanzhou, Taiyuan</td><td>609.6</td><td>5.82</td><td>95.5</td><td>40,213</td><td>6909.5</td><td>0.532</td><td>914</td><td>62.5</td></tr><tr><td>SouthernChina</td><td>Shanghai,Guangzhou,Nanjing, Wuhan,Chengdu</td><td>350.4</td><td>6.83</td><td>194.9</td><td>56,996</td><td>8344.9</td><td>2.268</td><td>3321</td><td>17.2</td></tr><tr><td>Globe</td><td></td><td>14,865</td><td>60.36</td><td>40.6</td><td></td><td></td><td>46.85</td><td>8618</td><td></td></tr></table>

Source: [5,17].

## 1.3. DSS solution

DSS have been developed since the 1970s to help tackle semi-structured and unstructured decision problems. DSS are considered an effective approach for water systems management and are increasingly used for unstructured decision- and policy-making [10,12,16,25,18,19]. DSS has also been successfully implemented to assess the overall sustainability in compliance with the EU water framework directive as the issue can no longer be resolved by means of intuitive reasoning [3]. A DSS for analyzing the impact of water restriction policies has recently been implemented in which an econometric model was employed [20]. This study was designed to provide a preliminary investigation of China’s water resources with a decision support system (DSS). In Section 2, as the main model of the system, a conceptual model of various linkages in social economic and ecological subsystems related to the problem of regional vulnerability is presented. Based on qualitative analysis using the conceptual model, then in Section 3, a water-embedded CGE model (WCGE) has been constructed to obtain a complete picture of economy with special consideration given to water resources. Through the DSS model WCGE, water linked problems, their causes and consequences can be found and examined. Section 4 discusses model verification and validation. In Section 5, several what-if analyses have been conducted which show the possible impacts of the project under different scenarios. Finally, in Section 6, implications for water strategic management from DSS are discussed.

## 2. Conceptual modeling

## 2.1. Concept of regional vulnerability

Refer to the pioneer study on world water resources [14] and the strategic economic development plan of China, in this study, a region becomes vulnerable to a certain natural resource’s availability if it cannot pursue its targeted goals at a desirable level. Thus, the vulnerability of a region due to a water resource shortage is interpreted as the inability of a region to sustain economic and social development in commensuration with the stated goals of socioeconomic policy.

## 2.2. Contributors to regional vulnerability to water resources

Fig. 1 shows that four aspects of water resources are important in an examination of a region’s vulnerability: water quantity, inter-temporal distribution, water quality, and water use/requirements. The first three factors interact with each other to make a region vulnerable. However, the origins of this vulnerability may lie in various socioeconomic– physical characteristics identified as population growth. Economic development and the relevant environmental and ecological factors are shown in the top three blocks in Fig. 1. Dotted lines in the figure denote a relatively weaker effect.

![](/api/attachments/FB26FCQ6/fulltext/images/52a5ea390f063ae9c01460bfa5138885207005e5db3cc6d120117bd7dbb4c399.jpg)  
Fig. 1. Interrelationships among water supply and use leading to regional vulnerability.

![](/api/attachments/FB26FCQ6/fulltext/images/096407ebe3f0afac665c7cf068c5f14dfbad362f771d6cd83ba5faa8b0a8e894.jpg)  
Fig. 2. Processes determining a region’s vulnerability to water resources.

As a further step in the analysis of determining a region’s vulnerability to water resources, Fig. 2 shows that if a country’s desire to achieve a higher level of industrial development is a means to improve the quality of life for its citizens, then such aspirations can be translated into higher income levels and increases in the demand for food and non-food products. These demands can be translated into an increased water use level. Fig. 2 also shows that environmental changes may impact both water supply and water demand/use level. Note that water-quality effects are excluded here.

![](/api/attachments/FB26FCQ6/fulltext/images/b3289221c1a3d8c1c7c0b8a0e4c872a72c922a011f20418e5ab3db0146da27e0.jpg)  
Fig. 3. D–S water balance and the deficit criterion.

## 2.3. Regional water supply level

The degree of regional vulnerability to water resources shown in Fig. 2 can be assessed quantitatively by using the quantity of water shortage as the criterion shown in Fig. 3. With this criterion, water availability (supply) and its use (demand) are studied over a period of time. Assuming that water supply remains at a constant level but water use increases as a direct result of economic activities in the region, indicated by the demand curve D. It is not difficult to see that the region may change its state from not vulnerable to extremely vulnerable, if the region’s water demand moves along the D curve from $E _ { 0 } \left( t _ { 0 } \right)$ cross balance point $E _ { 1 } \left( t _ { 1 } \right)$ to $E _ { 2 } \left( t _ { 2 } \right) ;$ ; however, if the water deficit can be compensated by additional quantities of water, for instance, gained from a water transfer project, then the planned economic development target may well be reached without any water deficit cost, e.g., underground water over withdrawal or reducing domestic water uses. $\Delta S _ { \mathrm { w } }$ in Fig. 3 shows an additional quantity of water supply gained from a project, it raises the total water supply level from S to $S { + } \Delta S _ { \mathrm { w } }$ then $E _ { 2 } \ \left( t _ { 2 } \right)$ becomes a new balance point rather than a water deficit of quantity DS that would exist without the water transfer project.

## 3. WCGE model

To investigate the water effects reflected in a multidimensional social–economic system, a computable general equilibrium model is selected for the DSS. This model is one of the best economic quantitative analysis models and has been successfully employed in many countries around the world [2,4,8,9,21]. The key problem now faced is how to put water resources into CGE’s mechanism. It is a rational decision to treat water resource as equivalent to land resources, due to the fact that both are natural resources limited in supply/availability. While water can be considered as a factor input in various domestic and productive uses, it is necessary to describe the degrees of various sectoral demand for water in different production and consumption processes. Accordingly, economic sectors by water usage intensity should be distinguished, which can be indicated by elasticity of substitution in production functions. Thus, water as an elementary input factor can be observed both on the input side by its price and the output side by its elasticity of substitution in various production functions of an economy.

## 3.1. Representative regional WCGE model

The water embedded CGE model WCGE stemmed from the Dynamic Recursive Chinese CGE model (DRC-CGE<sup>1</sup>), which was developed by the Development Research Center of Chinese State Council [28]. WCGE includes a complete set of 36 production sectors of neoclassical structure, with three groups (high, middle and low income) of representative households and four primary factors such as labor, capital, land, and water. To cope with regional vulnerability to the water resource problem, among those primary factors, water resource has been specially considered beyond standard CGE modeling. For the purpose of investigating the macro impact of the S2N project, China’s Capital city—Beijing has been chosen as the main water recipient region and the rest of China ROC has been treated as Beijing’s interactive trade partners, while the rest of the world, ROW, is used to specify international trade relationships between China and other parts of the world. Fig. 4 gives a brief description of water resource impacts from a macro economic point of view. In the diagram, CES and CET denote the constant elasticity of substitution and transformation.

3.2. Production, consumption, macro closure and dynamic features of the WCGE

## 3.2.1. Production structure

Fig. 5 shows the multiple nested structure of the production function. At the top level, sectoral output is a linear function of real value added and aggregate intermediate inputs. Aggregate intermediate inputs are demands with fixed input–output coefficients. Real value added is a constant elasticity of substitution

![](/api/attachments/FB26FCQ6/fulltext/images/28dd70ba08040e305b23a91c44a7098095a5702383bf7c54b0572baa22952128.jpg)  
Fig. 4. Diagram of water resource impact in macro economy.

(CES) function of aggregate labor, capital, water and land (in the agriculture sectors) aggregate. The aggregate labor and aggregate capital are also CES function of different types of labor and capital. The aggregate of water and land, in turn, is a linear aggregation of water and land individually. The model assumes that every sector has only one producer. Each producer maximizes their profit, under the constraint of certain production factors, by altering each factor employed in response to the relative price change between factors [26].

## 3.2.2. Consumption

The households in each region, grouped by income level, maximize a Stone–Geary utility function over the composite goods and savings, which lead to the Extended Linear Expenditure System (ELES) of household demand. Government spending and investment decisions in each region are based on the Cobb–Douglas utility function, which generates constant expenditure shares for each composite commodity. In each region, intermediate inputs, household consumption, government expenditure and investment demand constitute total demand for the same Armington composite of domestic and imported goods from different sources. A two-level nested CES aggregation function is specified for each composite commodity in each region. Total demand is first divided between domestic and imported goods; then the expenditure on imports is further divided according to geographical origin under the assumption of cost minimization.

![](/api/attachments/FB26FCQ6/fulltext/images/95ae85c862a422e3aed644f8c80aa091de1d20ba130f376efe23676dfcba8b40.jpg)  
Fig. 5. Production structure of water CGE.

## 3.2.3. Output allocation

As a part of China, the recipient regions have frequently participated in interregional trade with ROC. In order to capture regional trade characteristics, a two-level nested CET aggregation function has been employed. The distinction between international and interregional trade is specified for each sectoral output in each region. Fig. 6 shows the regional output allocation and demand structure. Sectoral output is assumed to be a composite commodity that can be transformed according to a constant elasticity of transformation (CET) function between a good sold on the domestic market and a good sold out of the region. While the aggregate commodity sold out of the region will be further transformed to export to the ROW and outflow to the ROC. The outflow of one region will constitute the corresponding ROC inflow. Each will equally match and will be cleared by the relative price of tradable commodities. Exports from two regions together will make up China’s total export by CES function.

## 3.2.4. Macro closure

For each region, the model includes three macro balances: trade balance, government expenditurereceipts balance, and saving-investment balance. The government balance is obtained through governmental saving endogenously determined. The regional capital inflow (or outflow) and foreign exchange surplus (or deficits) are determined endogenously as the residue to keep the balance of regional and international trade payments. The WCGE model uses neoclassical closure rules, also called saving-driving rules, to balance savings and investment.

## 3.2.5. Dynamic feature

The following three aspects drive the model’s dynamic features: (1) Factors accumulation and their efficiency improvement. Accumulation of capital stock in the model depends upon depreciation and gross real investment rates, and the latter is set exogenously based on forecasts from regression models. (2) Total Factor Productivity (TFP) growth. The economy-wide TFP variable is solved endogenously in the baseline calibration to match a prespecified path of real GDP growth in each region [15]. Then the economy-wide TFP variable is fixed when

![](/api/attachments/FB26FCQ6/fulltext/images/1fe32c2741c426c0398e3a10b6eb53f5a30beaa71ec97a51550ffdb1ed5d3428.jpg)  
Fig. 6. Regional output allocation structure.

alternative scenarios are simulated, in such a case, the growth rate of GDP and the sector-specific TFP variables that link productivity growth and imports are solved endogenously; (3) Population growth. Total population in each region is fixed exogenously according to the related forecast.

Table 3  
Sectoral water use, output and efficiency

<table><tr><td></td><td>Sectoral classification by water use style</td><td>Elasticity value</td><td>A, Water use (106m3)</td><td>B, Output (109Yuan)</td><td>B/A, Output/m3(Yuan/m3)</td></tr><tr><td>1</td><td>Agriculture</td><td>0.1</td><td>2036</td><td>17.1</td><td>8.4</td></tr><tr><td>2</td><td>High-water-intensive industry</td><td>0.3</td><td></td><td></td><td></td></tr><tr><td>2.1</td><td>Processed food, Beverage and Tobacco</td><td></td><td>96.1</td><td>26.3</td><td>274.1</td></tr><tr><td>2.2</td><td>Textile</td><td></td><td>40.0</td><td>6.7</td><td>168.2</td></tr><tr><td>2.3</td><td>Paper, printing</td><td></td><td>129.6</td><td>8.1</td><td>62.7</td></tr><tr><td>2.4</td><td>Chemical</td><td></td><td>139.3</td><td>29.2</td><td>209.5</td></tr><tr><td>2.5</td><td>Non-ferrous metal</td><td></td><td>34.2</td><td>11.2</td><td>327.1</td></tr><tr><td>2.6</td><td>Metal smelting and yielding</td><td></td><td>54.9</td><td>24.9</td><td>454.3</td></tr><tr><td>2.7</td><td>Machinery</td><td></td><td>42.9</td><td>16.4</td><td>382.1</td></tr><tr><td>2.8</td><td>Electricity Generation and Hot water</td><td></td><td>287.3</td><td>8.5</td><td>29.6</td></tr><tr><td></td><td>Total/Average</td><td></td><td>824.3</td><td>131.3</td><td>159.3</td></tr><tr><td>3</td><td>Middle-water-intensive industry</td><td>0.5</td><td></td><td></td><td></td></tr><tr><td>3.1</td><td>Ferrous ore mining</td><td></td><td>8.2</td><td>0.4</td><td>52.0</td></tr><tr><td>3.2</td><td>Non-ferrous ore mining</td><td></td><td>9.7</td><td>0.5</td><td>49.4</td></tr><tr><td>3.3</td><td>Petroleum refining</td><td></td><td>15.1</td><td>9.0</td><td>595.5</td></tr><tr><td>3.4</td><td>Metal Product</td><td></td><td>19.7</td><td>9.3</td><td>472.9</td></tr><tr><td>3.5</td><td>Transportation Equipment Manufacturing</td><td></td><td>15.9</td><td>14.3</td><td>896.7</td></tr><tr><td>3.6</td><td>Electric machinery</td><td></td><td>16.7</td><td>6.8</td><td>408.3</td></tr><tr><td>3.7</td><td>Construction</td><td></td><td>13.0</td><td>54.8</td><td>4216.4</td></tr><tr><td></td><td>Total/Average</td><td></td><td>98.3</td><td>95.1</td><td>967.4</td></tr><tr><td>4</td><td>Low-water-intensive industry</td><td>0.8</td><td></td><td></td><td></td></tr><tr><td>4.1</td><td>Crude oil and Natural gas</td><td></td><td>-</td><td>-</td><td>-</td></tr><tr><td>4.2</td><td>Coal mining</td><td></td><td>7.5</td><td>1.6</td><td>214.3</td></tr><tr><td>4.3</td><td>Apparel, Leather and other fibre Product</td><td></td><td>22.4</td><td>7.7</td><td>344.5</td></tr><tr><td>4.4</td><td>Sawmills and Furniture</td><td></td><td>7.2</td><td>2.9</td><td>407.1</td></tr><tr><td>4.5</td><td>Electronics and Telecommunication Equipment</td><td></td><td>7.2</td><td>32.9</td><td>4589.8</td></tr><tr><td>4.6</td><td>Social article manufacturing</td><td></td><td>2.1</td><td>2.2</td><td>1071.0</td></tr><tr><td>4.7</td><td>Machine Repair</td><td></td><td>1.2</td><td>2.6</td><td>2225.4</td></tr><tr><td>4.8</td><td>Other Manufacturing</td><td></td><td>4.2</td><td>6.8</td><td>1611.6</td></tr><tr><td>4.9</td><td>Production and Supply of Gas</td><td></td><td>1.2</td><td>0.8</td><td>673.6</td></tr><tr><td>4.10</td><td>Production and Supply of Tap water</td><td></td><td>1.1</td><td>0.6</td><td>565.8</td></tr><tr><td></td><td>Total/Average</td><td></td><td>54.1</td><td>58.1</td><td>1073.9</td></tr><tr><td>5</td><td>Service</td><td>0.75</td><td></td><td></td><td></td></tr><tr><td>5.1</td><td>Store Warehouse</td><td></td><td>57.6</td><td>20.0</td><td>347.4</td></tr><tr><td>5.2</td><td>Post</td><td></td><td>14.5</td><td>10.1</td><td>697.1</td></tr><tr><td>5.3</td><td>Sales</td><td></td><td>150.9</td><td>27.5</td><td>182.4</td></tr><tr><td>5.4</td><td>Catering</td><td></td><td>178.9</td><td>7.1</td><td>39.8</td></tr><tr><td>5.5</td><td>Passenger transportation</td><td></td><td>7.5</td><td>7.5</td><td>993.3</td></tr><tr><td>5.6</td><td>Financial and Insurance</td><td></td><td>15.5</td><td>85.4</td><td>5507.2</td></tr><tr><td>5.7</td><td>Real Estate</td><td></td><td>5.7</td><td>8.3</td><td>1460.7</td></tr><tr><td>5.8</td><td>Social Service</td><td></td><td>74.5</td><td>47.4</td><td>635.8</td></tr><tr><td>5.9</td><td>Education</td><td></td><td>17.9</td><td>22.7</td><td>1268.7</td></tr><tr><td>5.10</td><td>Others</td><td></td><td>39.9</td><td>62.3</td><td>1561.8</td></tr><tr><td></td><td>Total/Average</td><td></td><td>505.3</td><td>278.3</td><td>550.8</td></tr><tr><td></td><td>Total/Average</td><td></td><td>3518</td><td>579.9</td><td>164.8</td></tr></table>

Source: Water Input–Occupation–Output Table in Haihe River basin and Beijing 1997 Input–Output Table [6,7].

## 4. Water resource factor in WCGE

## 4.1. Sectoral water use

To characterize the different water intensive degrees in various production sectors by elasticity of substitution, the second column in Table 3 lists 36 production sectors of the WCGE, they are grouped into five categories by style of water use and elasticity of substitution in production functions, namely: agriculture, high-intensive sector, middle-intensive sector, low-intensive sector and service, with the elasticity value of 0.1, 0.3, 0.5, 0.8 and 0.75, respectively [24]. The 4th–6th columns show sectoral water use, output, and efficiency correspondingly.

## 4.2. Water use and reuse classified by quality

The model distinguishes three types of water resources by their quality: high quality water, middle quality water, and low quality water. Water with different quality will be used for different purposes. The model assumes water with high quality for service and domestic use, middle quality for industry use, and low quality for agriculture. The model also assumes that after proper sewage treatment, the service and household effluent can be reused for industrial purposes. A fixed proportion of industrial sewage can be reused in agriculture sectors after proper treatment. Fig. 7 portrays the water recycling in the model. In the model, it is assumed that the S2N transferred water is high quality, and will first be used to meet increasing domestic demand, and then the rest will be allocated for the industrial use, while the water available for agriculture use will be increased indirectly due to an industrial sewage increase.

Table 4  
Water shadow price by types

<table><tr><td></td><td>Sectoral classification by water use style</td><td>Volume of water use ( $10^{8}$  m $^{3}$ )</td><td>Shadow price (Yuan/m $^{3}$ )</td></tr><tr><td rowspan="2">1</td><td>Agriculture</td><td>20.36</td><td>1.17</td></tr><tr><td>Industry</td><td>9.76</td><td>15.32</td></tr><tr><td>2</td><td>High-intensive</td><td>8.24</td><td>10.6</td></tr><tr><td>3</td><td>Middle-intensive</td><td>0.98</td><td>18.5</td></tr><tr><td>4</td><td>Low-intensive</td><td>0.54</td><td>81.5</td></tr><tr><td rowspan="2">5</td><td>Service</td><td>5.05</td><td>52.7</td></tr><tr><td>Average</td><td></td><td>4.7</td></tr></table>

## 4.3. Water price formation

In this study, the water shadow price in the base year is adopted to represent the water equilibrium price. The following programming problem derived from an input–output framework is used to identify the shadow price of water resource [6]:

$$
\max z = \sum a _ {n j} X _ {j}   \text { s.t. } \left\{ \begin{array}{l} A X + Y + U - V \leq X \\ X ^ {l} \leq X \leq X ^ {h} \\ \sum a _ {\mathrm{wj}} X _ {j} \leq W \\ 0 \leq U \leq U ^ {h} \\ 0 \leq V \leq V ^ {h} \\ Y ^ {l} \leq Y \\ \sum U _ {j} - \sum V _ {j} \geq c \\ X \geq 0, U \geq 0, V \geq 0 \end{array} \right.
$$

In the above equations, X, Y, U, V are variables. X is the total output vector in the Input–Output table; Y is sector final consumption volume, U is export vector; V is import vector; A is sector direct consumption coefficient; $a _ { \mathrm { v } j }$ are sectoral value-added coefficients; $a _ { \mathrm { w } j }$ are sector water usage coefficients; W is sectoral water usage vector; $X _ { l } , X _ { h }$ are sectoral constraint boundary vector for total output; $V _ { h } , U _ { h }$ are the constraint vector for sectors import; c is sectoral net export bottom boundary. The loose variable corresponding to W is the shadow price of water resource. The solution of the above maximization problem is given in Table 4.

![](/api/attachments/FB26FCQ6/fulltext/images/50418ab5481a70d1adb1cc7ed83e845b2951a8e73a212000cd904c4c33bb6967.jpg)  
Fig. 7. Water use hierarchy recycling in CGE model.

T<sub>a</sub>bl<sub>e</sub> 5  
Th<sub>e s</sub>t<sub>ruc</sub>t<sub>ure o</sub>f SAM <sub>em</sub>b<sub>e</sub>dd<sub>e</sub>d <sub>w</sub>ith <sub>wa</sub>t<sub>er resource</sub>

<table><tr><td></td><td>Activity</td><td>Commodity</td><td>Capital</td><td>Labor</td><td>Water</td><td>Land</td><td>Enterprise</td><td>Household</td><td>Central Government</td><td>Local Government</td><td>Investment</td><td>ROW</td><td>ROC</td><td>Total</td></tr><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td></td></tr><tr><td>Activity 1</td><td></td><td>Total Sales</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Total Output</td></tr><tr><td>Commodity 2</td><td>Intermediate Input</td><td></td><td></td><td></td><td></td><td></td><td></td><td>Household Consumptions</td><td>Government Consumption</td><td></td><td>Investment</td><td>Export</td><td>ROC Outflow</td><td>Total Demand</td></tr><tr><td>Capital 3</td><td>Capital Revenue</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Capital Rewards</td></tr><tr><td>Labor 4</td><td>Labor Remuneration</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Labor Income</td></tr><tr><td>Water Resource 5</td><td>Water Resource Fee</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Water Resource Fee</td></tr><tr><td>Land 6 Enterprise 7</td><td>Land Rent</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Land Rent Enterprise Revenue</td></tr><tr><td>Household 8</td><td></td><td></td><td>Capital Reward</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Household Income</td></tr><tr><td>Central Government 9</td><td>Indirect Taxes</td><td></td><td></td><td>Labor Wage</td><td>Water Resource Tax and Fee</td><td>Land Reward Land Tax</td><td>Retained Earnings Enterprise Taxes</td><td>Household Income Taxes</td><td>Government Transfer</td><td>Household Subsidy</td><td></td><td></td><td></td><td>Government Revenue</td></tr><tr><td>Local Government 10 Savings 11</td><td>Production Taxes</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Production Subsidy</td><td></td><td></td><td></td><td></td><td>Total Subsidy</td></tr><tr><td>ROC 12 ROW 13</td><td></td><td>Outflow Import</td><td></td><td></td><td></td><td></td><td>Enterprise Savings</td><td>Household Savings</td><td>Government Savings</td><td></td><td></td><td>Exchange Savings</td><td>ROC Surplus</td><td>Total Savings</td></tr><tr><td>Total</td><td>Total Cost</td><td>Total Supply</td><td>Capital Reward</td><td>Labor Reward</td><td>Total Water Fee</td><td>Total Land Fee</td><td>Enterprise Fee</td><td>Household Expenditure</td><td>Government Expense</td><td>Subsidy</td><td>Total Investment</td><td>Exchange Surplus</td><td>Net Inflow</td><td></td></tr></table>

Actually, the water shadow price represents the extra unit of value added resulting from giving an additional unit of water to the macro economy. In the model, the water shadow price means the GDP generated by the last unit water input. In a complete competitive market, as the marginal cost equals marginal revenue, the water shadow price equals the market equilibrium price.

## 4.4. Water SAM—WSAM

The base year equilibrium of a CGE model is the starting point of the equilibrium time series created by the CGE model forecasting [22]. It is a fundamental part of a CGE model system. In the case study, a Social Accounting Matrix SAM [23] embedded with water resources was established to provide a consistent macroeconomic database for the calibration of various parameters in the WCGE model. Table 5 provides a description of WSAM.

The essence in constructing such WSAM is to capture the links, water resource fee (or water economic value), between the water accounts, which is originally measured in cubic meters $( \mathbf { m } ^ { 3 } )$ , and the rest of economy, which is denominated in money [11]. In WSAM, the water resource fee actually is the transaction cost that the activities should pay to the water resource account for their water usage. In WSAM, water resource fees are calculated as:

Water Resource Fee

ðor Water Economic ValueÞ

$$
= \text {   Water   Use   Volume   } * \text {   Water   Shadow   Price   }
$$

In WSAM, it is assumed that the central government is the water resource possessor, and the payment by activity for their water resource usage will be collected by the central government as water resource taxes or fees [22]. The amount of such income will finally constitute part of central government revenue. The gap between the shadow price and the current executive price is treated as the government <sup>d</sup>implicit subsidy<sup>T</sup> and this amount of value will be deducted from net production taxes.

<table><tr><td colspan="3">Table 6Scenario description</td></tr><tr><td>Without S2N project</td><td>B1</td><td>B2</td></tr><tr><td>Group 1: Business as usual</td><td>· Without sustainable development strategy; · Keep water use pattern as 1990s; · With excessive pumping groundwater; · Keep surface water utilization rate as high as 80%; · Ecological water use keep zero; · Household per capita water use increase 2% annually.</td><td>· Adopt sustainable development policy; · Stop the excessive pumping of groundwater which causes regional total water supply decreased by 0.426 billion  $m^{3}$  consequently; · Lower surface water utilization rate below 60%; · Increase the regional ecological water use from 0 in 1997 to 0.92 billion  $m^{3}$  in 2020 by a linear increment; · Household per capita water use increase 2% annually.</td></tr><tr><td>With S2N project</td><td>S1</td><td>S2</td></tr><tr><td>Group 2: Support the regional water supply by S2N project</td><td>· All the assumption similar to B1, except · From 2008, the transferred water  $\Delta S_{w}=1.021\times 10^{8} \text{m}^{3}$  is added to the regional water supply. · The transferred water will be first for household use, then allocated for industrial use.</td><td>· All the assumption similar to B2, except · From 2008, the transferred water  $\Delta S_{w}=1.021\times 10^{8} \text{m}^{3}$  is added to the regional water supply. · The transferred water will be first for household use, then allocated for industrial use.</td></tr></table>

Table 7  
Water supply level in different scenarios 1997, 2010 and 2020

<table><tr><td rowspan="2">Sectoral water use style</td><td rowspan="2">Base year 1997 (108 m3)</td><td colspan="4">2010 ( $10^{8}$  m3)</td><td colspan="4">2020 ( $10^{8}$  m3)</td></tr><tr><td>B1</td><td>B2</td><td>S1</td><td>S2</td><td>B1</td><td>B2</td><td>S1</td><td>S2</td></tr><tr><td>Agriculture</td><td>20.36</td><td>19.72</td><td>16.89</td><td>26.00</td><td>22.47</td><td>19.91</td><td>12.55</td><td>25.56</td><td>18.19</td></tr><tr><td>Industry</td><td>11.36</td><td>11.00</td><td>9.75</td><td>15.02</td><td>12.98</td><td>11.5</td><td>7.25</td><td>14.76</td><td>10.5</td></tr><tr><td>Service</td><td>6.64</td><td>6.43</td><td>4.19</td><td>6.45</td><td>5.57</td><td>4.94</td><td>3.11</td><td>6.34</td><td>4.51</td></tr><tr><td>Household</td><td>1.77</td><td>2.97</td><td>2.97</td><td>2.97</td><td>2.97</td><td>3.78</td><td>3.78</td><td>3.78</td><td>3.78</td></tr><tr><td>Ecological</td><td></td><td>0.00</td><td>2.10</td><td>0.00</td><td>2.10</td><td>0.00</td><td>9.20</td><td>0.00</td><td>9.20</td></tr><tr><td>Total</td><td>40.13</td><td>40.12</td><td>35.90</td><td>50.44</td><td>46.09</td><td>40.13</td><td>35.89</td><td>50.44</td><td>46.18</td></tr></table>

Source: Recalculated based on report of Beijing water resource planning, 2001.

## 5. What-if analysis and outcome

## 5.1. Scenario setting

Two scenario groups are designed to compare the regional economic performance under the assumption of with and without the S2N project. The first group designed is without the S2N project. In this group, two scenarios B1 and B2 were devised, which can be granted as an unsustainable and a sustainable scenario without S2N. The second group designed is with the S2N scenario. In this group, two scenarios, S1 and S2, are introduced for the comparison of the first group. The S2N project is expected to be accomplished by 2008. From then on, the scheduled water of $1 . 0 2 1 \times 1 0 8 ~ \mathrm { ~ m ~ } ^ { 3 }$ will be replenished to the regional total water supply annually. Table 6 presents the general assumption of each scenario while Table 7 lists the water supply discrepancy in scenarios.

## 5.2. Simulation outcome

The WCGE model contains 96 groups of equations and a total number of 8732 endogenous variables. The trajectory of GDP growth rate of each scenario and relevant selected outcome data groups are shown in Fig. 8 and Table 8. Fig. 8 plots Beijing’s GDP growth rate curves from 2006 to 2020 under different scenarios. In water unsustainable utilization pattern B1 scenario, Beijing’s GDP growth rate will be around 7.5% from 2010 to 2020. While in the water

![](/api/attachments/FB26FCQ6/fulltext/images/ed0f928c4a2db30bec90490a24be900ca6e49cc772e69c393b097a9f9a9b200d.jpg)  
Fig. 8. GDP growth rate in scenarios.

Table 8 Main simulation macro economy index

<table><tr><td rowspan="2">Without S2N project</td><td rowspan="2">Base year (1997)</td><td colspan="2">2010</td><td colspan="2">2020</td></tr><tr><td>B1</td><td>B2</td><td>B1</td><td>B2</td></tr><tr><td>Annual GDP growth rate, %</td><td></td><td>9.21</td><td>5.52</td><td>7.2</td><td>4.52</td></tr><tr><td>Real GDP ( $10^{8}$  Yuan)</td><td>2291</td><td>7202</td><td>4606</td><td>14,434</td><td>7167</td></tr><tr><td>Total Output ( $10^{8}$  Yuan)</td><td>6002</td><td>19,576</td><td>13,168</td><td>40,159</td><td>20,984</td></tr><tr><td>Investment ( $10^{8}$  Yuan)</td><td>1197</td><td>3675</td><td>2349</td><td>7283</td><td>4655</td></tr><tr><td>Household Consumption ( $10^{8}$  Yuan)</td><td>1417</td><td>4569</td><td>2907</td><td>9225</td><td>4562</td></tr><tr><td>Domestic commodity inflow ( $10^{8}$  Yuan)</td><td>1166</td><td>3772</td><td>2421</td><td>7802</td><td>3887</td></tr><tr><td>Domestic commodity outflow ( $10^{8}$  Yuan)</td><td>1091</td><td>3368</td><td>2153</td><td>6657</td><td>3302</td></tr><tr><td>Import ( $10^{8}$  Yuan)</td><td>257</td><td>793</td><td>507</td><td>1568</td><td>778</td></tr><tr><td>Export ( $10^{8}$  Yuan)</td><td>127</td><td>392</td><td>251</td><td>951</td><td>385</td></tr><tr><td>Employment ( $10^{4}$  person)</td><td>661</td><td>672</td><td>554</td><td>706</td><td>575</td></tr><tr><td>Household income per person (Yuan)</td><td>11,431</td><td>20,780</td><td>13,308</td><td>41,649</td><td>20,707</td></tr><tr><td>Government Revenue ( $10^{8}$  Yuan)</td><td>594.0</td><td>1006</td><td>589</td><td>2016</td><td>917</td></tr></table>

<table><tr><td rowspan="2" colspan="2">With SEN project</td><td colspan="2">2016</td><td colspan="2">2020</td></tr><tr><td>S1</td><td>S2</td><td>S1</td><td>S2</td></tr><tr><td>Annual GDP growth rate, %</td><td></td><td>10.2</td><td>6.98</td><td>9.3</td><td>7.05</td></tr><tr><td>Real GDP ( $10^{8}$  Yuan)</td><td>2291</td><td>8098</td><td>5507</td><td>19,705</td><td>10,885</td></tr><tr><td>Total Output ( $10^{8}$  Yuan)</td><td>6002</td><td>21,979</td><td>14,837</td><td>53,483</td><td>29,821</td></tr><tr><td>Investment ( $10^{8}$  Yuan)</td><td>1197</td><td>4046</td><td>2795</td><td>12,598</td><td>6647</td></tr><tr><td>Household Consumption ( $10^{8}$  Yuan)</td><td>1417</td><td>5070</td><td>3458</td><td>12,450</td><td>6878</td></tr><tr><td>Domestic commodity inflow ( $10^{8}$  Yuan)</td><td>1166</td><td>4220</td><td>2851</td><td>10,382</td><td>5731</td></tr><tr><td>Domestic commodity outflow ( $10^{8}$  Yuan)</td><td>1091</td><td>3721</td><td>2581</td><td>8891</td><td>5073</td></tr><tr><td>Import ( $10^{8}$  Yuan)</td><td>257</td><td>941</td><td>638</td><td>2332</td><td>1284</td></tr><tr><td>Export ( $10^{8}$  Yuan)</td><td>127</td><td>428</td><td>297</td><td>1023</td><td>585</td></tr><tr><td>Employment ( $10^{4}$  person)</td><td>661</td><td>745</td><td>600</td><td>803</td><td>667</td></tr><tr><td>Household income per person (Yuan)</td><td>11,431</td><td>21,357</td><td>13,868</td><td>51,968</td><td>27,408</td></tr><tr><td>Government Revenue ( $10^{8}$  Yuan)</td><td>594.02</td><td>1186</td><td>770</td><td>2885</td><td>1594</td></tr></table>

<table><tr><td rowspan="2">Project benefit/increment (S-B)</td><td colspan="2">2010</td><td colspan="2">2020</td></tr><tr><td>S1-B1</td><td>S2-B2</td><td>S1-B1</td><td>S2-B2</td></tr><tr><td>Annual GDP growth rate, %</td><td>0.99</td><td>1.46</td><td>2.1</td><td>2.3</td></tr><tr><td>Real GDP ( $10^{8}$  Yuan)</td><td>896</td><td>901</td><td>5271</td><td>3717</td></tr><tr><td>Total Output ( $10^{8}$  Yuan)</td><td>2404</td><td>1670</td><td>13,324</td><td>8837</td></tr><tr><td>Investment ( $10^{8}$  Yuan)</td><td>371</td><td>447</td><td>5315</td><td>1992</td></tr><tr><td>Household Consumption ( $10^{8}$  Yuan)</td><td>501</td><td>551</td><td>3225</td><td>2316</td></tr><tr><td>Domestic commodity inflow ( $10^{8}$  Yuan)</td><td>448</td><td>430</td><td>2580</td><td>1843</td></tr><tr><td>Domestic commodity outflow ( $10^{8}$  Yuan)</td><td>353</td><td>428</td><td>2234</td><td>1770</td></tr><tr><td>Import ( $10^{8}$  Yuan)</td><td>148</td><td>131</td><td>764</td><td>506</td></tr><tr><td>Export ( $10^{8}$  Yuan)</td><td>36</td><td>47</td><td>72</td><td>200</td></tr><tr><td>Employment ( $10^{4}$  person)</td><td>73</td><td>46</td><td>97</td><td>92</td></tr><tr><td>Household income per person (Yuan)</td><td>577</td><td>560</td><td>10,319</td><td>6701</td></tr><tr><td>Government Revenue ( $10^{8}$  Yuan)</td><td>180</td><td>181</td><td>869</td><td>677</td></tr></table>

Source: Model simulation results.

sustainable B2 scenario, the regional GDP growth rates would sharply decrease to 5.5%. The data indicate that there is a conflict between regional economic growth speed and ecological preservation within the existing natural water resource supply volume. The high growth rate is done at the cost of environmental deterioration that would bring the regional ecological system into the marginal or extremely vulnerable state. While in the S1 and S2 with the project’s water increment, Beijing’s growth rate will increase to 8.5%. The above results imply that the S2N project will benefit not only the regional sustainable development but also preserve the ecological vulnerability.

Table 8 lists the comparison of the main macro index of each simulation. Compared to the scenarios without the S2N project, increment of water will contribute to 1–2.3% increase in the GDP growth rate, that will equal a GDP increase of 89 billion Yuan or almost US\$10 billion annually. The ripple effect will result in production expansion, 700,000 employment opportunities and a 577 Yuan increase to the household income per capita in the year 2010, which will account for 2.5–4.1% of the total household annual income. The project will indirectly increase government revenue by 18 billion Yuan in 2010. The projected benefits maybe even larger in the long term as the usage efficiency of regional water would improve. By 2020, the project will create almost 527 billion Yuan GDP annually and create about 1.0 million employment opportunities. It will increase household income per capita by 7825 Yuan and result in 87 billion Yuan in governmental revenue.

## 6. Conclusion

This paper describes a model based DSS for assessing the impact of the South-to-North Water Transfer Project in China and how the system has been implemented to address real-world water resource issues associated with strategic initiatives as they can no longer be resolved by means of intuitive reasoning. The goal of the system is to assist authorities in evaluating water usage policies that combine the sustainability of natural resources with economic growth. Implications of the results shown in Table 8 and Fig. 8 can be summarized as follows:

1. In the absence of the S2N Water Transfer Project, Beijing would face serious water shortage problems. DSS simulation for scenario B1 shows that extracting all of its ground water on an over-use basis could support a long-term accelerated industrialization process, but it may cause the city’s natural environment to become unmanageable.

DSS simulation for scenario B2 shows that if a proper environment and resource protection policy had been adopted, then the goal of high-speed industrialization may be curtailed.

2. DSS simulation outcomes for scenarios B2 and S2 show that in any case, a holistic consideration of harmonic social–economic–environmental development strategy is valuable. The opposites are the B1 and S1 scenarios. The results shown in Fig. 8 are obviously true.

3. DSS simulation outcomes for scenario S1 and S2 show that with the S2N Project, an incremental quantity of additional water supply is definitely beneficial to the recipient region.

4. Although there is a trade-off between the cost of implementing the S2N Water Transfer Project and the benefits derived from optimized water resource allocation, DSS simulation outcomes show that through an increment of water supply by the S2N Project and proper policy-making, if a city such as Beijing pursues a sustainable development strategy, the gap between water demand and supply can eventually be closed. The simulation outcome from scenario S2 is a proof.

## Areas of future research include the following:

(1) Water use efficiency. Different types of production technology result in different levels of water use efficiency. There is considerable space available to design a water conservation style for use in China, which is worthy of research efforts.

(2) New topic. Based on the current WCGE model, a further study of the dynamics of the interrelationship between water, food and energy systems under a changing environment (economic and non-economic) is a topic that should be given a high priority in future research.

## Acknowledgement

The research has been supported by Natural Science Foundation of China NSFC 60174039 and 79990580. Authors take the opportunity to express their sincere appreciation of help from the Development Research Center of the State Council PRC and from their own team members particularly Dr. Zhou Kai-bo and Ms. Guo Shi-hai.

## References

[1] J. Beghin, S. Dessus, D. Roland-Holst, D. Mensbrugghe, Proto-type CGE Model for the Trade and the Environment Programme—Technical Specification, OECD Development Centre, Paris, 1994.

[2] A. Brooke, D. Kendrick, A. Meeraus, GAMS: A User’s Guide, The Scientific Press, New York, 1998.

[3] N. Brunner, M. Starkl, Decision aid systems for evaluating sustainability: a critical survey, Environmental Impact Assessment Review 24 (4) (2004) 441– 469.

[4] K. Chang, T. Seung, R. Harris, Impact of water reallocation: a combined computable general equilibrium and recreation demand model approach, Annals of Regional Science 34 (2000) 473–487.

[5] J. Chen, H. Wang, Water Resource, Science Press, Beijing, 2002.

[6] X. Chen, C. Yang, Research on Water Input–Occupancy– Output model and its Application, Academy of Mathematics and Systems Science, Chinese Academy of Sciences, Beijing, 2002.

[7] Committee of Beijing Water Resource, Beijing Water Resource Planning for South to North Water Transfer.

[8] S. Feng, L. Xu, H. Zhou, L. Li, Dynamic simulation of demographic economic systems in developing countries, Information and Decision Technologies 18 (1992) 363– 374.

[9] S. Feng, L. Xu, H. Zhou, L. Li, V. Yen, Simulating large complex societal systems, International Journal in Computer Simulation 3 (1993) 97– 105.

[10] M. Holmes, A. Young, T. Goodwin, R. Grew, A catchmentbased water resource decision support tool for the United Kingdom, Environmental Modeling and Software 20 (2) (2005) 197 – 202.

[11] B. Hynd, Water in the Macro Economy: Integrating Economics and Engineering into an Analytical Model, Ashgate Publishing Limited, London, England, 2001.

[12] A. Karbowski, K. Malinowski, E. Niewiadomska-Szynkiewicz, A hybrid analytic/rule-based approach to reservoir system management during flood, Decision Support Systems (2003) (in press).

[13] H.S. Kim, Sustainable Development and the South-to-North Water Transfer Project in China. Master thesis, Central Connecticut State University, 2003.

[14] S.N. Kulshreshtha, World water resources and the regional vulnerability: Impacts of future changes. Research Report, IIASA93-10, 1993.

[15] S. Li, F. Zhai, China still have the capacity of growing fast in the long-term, Journal of Chinese Industrial Economy (6) (2000) 15 – 19.

[16] D. Liu, T. Stewart, Object-oriented decision support systems modeling for multicriteria decision making in natural resource management, Computers and Operations Research 31 (7) (2004) 985– 999.

[17] Ministry of Water Resource of the People’s Republic of China, China Water Resource Gazette. http://www.water.com/gazzette/ 2000.html.

[18] J. Mysiak, C. Giupponi, P. Rosato, Towards the development of a decision support system for water resource management, Environmental Modeling and Software 20 (2) (2005) 203– 214.

[19] T. Nauta, A. Bongco, A. Santos-Borja, Set-up of a decision support system to support sustainable development of the Laguna de Bay, Philippines, Marine Pollution Bulletin 47 (1–6) (2003) 211– 218.

[20] B. Recio, J. Ibanez, F. Rubio, J. Criado, A decision support system for analyzing the impact of water restriction policies, Decision Support Systems (in press).

[21] S. Robinson, C. Gehlhar, Land, water and agriculture in Egypt: the economy wide impact of policy reform, TMD Working Paper No.227, International Food Policy Research Institute, Washington, 2000.

[22] P. Rogers, R. de Silva, R. Bhatia, Water is an economic good: how to use price to promote equity, efficiency and sustainability, Water Policy (4) (2002) 1 – 17.

[23] P. Round, Social Accounting Matrix: A Basis for Planning, World Bank, 1985.

[24] D. Shen, H. Wang, The econometric analysis of industrial water use, Journal of Water Conservancy 8 (2000) 27 – 31.

[25] U. Simon, R. Bruggemann, S. Pudenz, Aspects of decision support in water management—example Berlin and Potsdam (Germany): II. Improvement of management strategies, Water Research (in press).

[26] Z. Wang, The impact of China’s WTO accession on patterns of world trade, Journal of Policy Modeling (25) (2003) 1 –41.

[27] Yangtse River Water Resource Commission of Ministry of Water Resource, PRC, No. 5 of Series Reports on South-to-North Water Transfer: Comprehensive economic analysis, Beijing, 2001.

[28] F. Zhai, S. Li, S. Feng, Chinese economy and structural change in long run-dynamic recursive CGE model, System Engineering Theory and Application (2) (1999) 88–95.
