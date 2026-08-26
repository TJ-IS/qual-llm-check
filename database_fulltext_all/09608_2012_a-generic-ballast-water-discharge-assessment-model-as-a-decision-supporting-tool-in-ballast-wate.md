---
otero_id: 9608
otero_key: "QCEEU2EK"
title: "A generic ballast water discharge assessment model as a decision supporting tool in ballast water management"
authors: "Matej David; Marko Perkovič; Valter Suban; Stephan Gollasch"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.01.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A generic ballast water discharge assessment model as a decision supporting tool in ballast water management

Matej David <sup>a,</sup>⁎, Marko Perkovič <sup>a,b</sup>, Valter Suban <sup>a</sup>, Stephan Gollasch <sup>c</sup>

<sup>a</sup> University of Ljubljana, Faculty of Maritime Studies and Transport, Pot pomorščakov 4, SI 6320 Portorož, Slovenia

<sup>b</sup> European Commission, Joint Research Centre, Ispra, Italy

<sup>c</sup> GoConsult, Grosse Brunnenstr. 61, 22763 Hamburg, Germany

## a r t i c l e i n f o

Article history: Received 28 June 2011 Received in revised form 15 December 2011 Accepted 2 January 2012 Available online 9 January 2012

Keywords: Maritime transport Ballast water management Discharge assessment Risk assessment Decision support tool

## a b s t r a c t

One of the critical issues in species invasion ecology is the need to understand and evaluate the dimensions and processes of aquatic organisms transfer with vessels ballast water. The assessment of the quantity of ballast water discharged as the medium of transfer is one of the basic elements of the decision making process in ballast water risk assessment and management. The possibility to assess this in advance of the vessel's arrival to a port enhances the management process and gives port authorities a decision supporting tool to respond in time with adequate measures. A new generic ballast water discharge assessment model has been prepared. The model is based on vessel cargo operation and vessel dimensions. The model was tested on real shipping traf<sup>fi</sup>c and ballast water discharge data for the Port of Koper, Slovenia. The results show high con<sup>fi</sup>dence in predicting whether a vessel will discharge ballast water, as well in assessing the quantity of ballast water (to be) discharged.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

The transfer of aquatic alien organisms occurs unintentionally, e.g., with vessels, or intentionally, e.g., with aquaculture, aquarium trade. In shipping, aquatic organisms are predominantly transferred across natural boundaries with ballast water and related sediments [5,13,23,24,27,28,35,36,38,43] and attached to the vessels' hull or in sea chests [8,20,22,25,30,32,39]. The transfer of harmful aquatic organisms with vessels has already resulted in harmful impacts on natural environments and human health, and has also caused substantial economic losses [6,25,34,47].

Understanding the transfer process of aquatic organisms, i.e., organisms entering ballast tanks, surviving a voyage and the ballast water discharge, is critical for an effective ballast water management [9,31]. Risk assessment plays a crucial role as it enables the identi<sup>fi</sup>cation of appropriate management measures according to the risk level assessed, e.g., high risk — possible additional control and management requirements, low risk — no need for ballast water management [9,11,21,30,31]. As the quantity of ballast water discharged is one of the basic elements for an evaluation of the risk posed, i.e., in general, the bigger the quantity discharged, the more organisms are discharged, different studies around the world included the quanti<sup>fi</sup>cation of ballast water discharged in ports [4,23,33,41,44].

A port state may introduce the requirement for vessels to report ballast water operations when sailing to their port to collect data about, e.g., the source and quantity of ballast water, as well as other information depending on the purpose of the data collection and regulations in place [10]. On the other side, the quantities of ballast water discharges, e.g., for a single vessel or for discharges in a period of time for a terminal, port, or port state waters, may also be assessed with a model. This enables also the assessment of ballast water discharges in the past, as well as the assessment of future discharges. All this information is crucial to assess the related threats posed to the environment, human health and economy, and based on this the decision making process to support effective ballast water management is enabled [9,11,14].

A Decision Support System (DSS) can be de<sup>fi</sup>ned as a supporting tool enhancing the decision-making process [3]. DSSs today are widely supporting decision-making processes in business, social sciences, medicine, politics, games, information technologies, and transport [37], and they are major building blocks in environmental management and science today [16]. Decision-makers are frequently faced with the need to take decisions on very complex issues, requiring a large data input, and in a timely manner. DSSs help decision-makers to reduce uncertainties [26], as well as to ease and speed-up the decision process. DSSs also avoid emotional driven decision making, hence reduce subjectiveness [40].

The possibility to have a decision support model to assess ballast water discharges in advance of the vessel's arrival in a port would support the management process and provide the port state with a tool to respond through different management options according to, e.g., the level of the risk posed, the veri<sup>fi</sup>cation of the vessel's reporting quality, and the selection of vessels for Port State Control inspection. These options aim at the most effective prevention measures for certain vessels, i.e., selective approach, and at the same time will lower the costs of unnecessary management procedures and burden in case measures will be applied on all vessels, i.e., blanket approach [9,11,14].

## 2. Material and methods

## 2.1. Study purpose

Two research studies on ballast water issues and management in the Slovenian Sea were conducted between July 2001 and June 2007. To achieve the aims of these studies it was required to:

1. Assess the ballast water discharges for the past period in the Port of Koper, Slovenia, to identify quantities and trends;

2. Identify in advance vessels which will discharge ballast water to enable a selection of representative vessels to be studied, i.e., those representing the source ports or areas and quantities of ballast waters being discharged in the Port of Koper, as part of the ballast water sampling program;

3. Verify the exactness of ballast water reporting that was introduced for vessels calling to the Port of Koper;

4. Predict future ballast water discharges for risk assessment and ballast water management needs.

## 2.2. Previous studies

Previous studies conducted elsewhere were reviewed to locate any quantitative assessment approaches/models to assess ballast water discharge volumes. Most authors [1,2,4,7,17,19,29,46,48,49] based their estimations on the relation, i.e., percentage, between vessel's deadweight (DWT) and ballast water capacity, some of these being more detailed and using different relations for different vessel types (see Table 1). In a more recent study [44], information from vessel reporting systems of Canada and the USA was used to assess ballast water operations in the Great Lakes, but we were not able to identify clear information on how the ballast water volumes were assessed or calculated in cases these were not reported.

Further, three discharge models were identi<sup>fi</sup>ed, i.e., the “European” [23], the “Australian” Brisbane [33] and Victoria [18], and the “North American” Great Lakes Model [42]. The “European” model prepared during the EU Concerted Action study on Testing Monitoring Systems for Risk Assessment of Harmful Introductions by Ships to European Waters [23] is based on the assessment of the quantity of ballast water discharged in relation to the total quantity of cargo transhipped in a port by vessel type. The model used in Australian studies is based on average percentage of the relation between ballast capacity and DWT. This initial model has been used in the Brisbane area [33] and it was slightly modi<sup>fi</sup>ed and applied for Victoria [18]. The model used in the North American Great Lakes studies is based on the number of vessels and average ballast water carried [42].

Comparison of assessed ballast water discharged quantities in the Port of Koper as result of applying different existing and modi<sup>fi</sup>ed models [23,33,42].

<table><tr><td rowspan="4">Year</td><td colspan="6">Estimated ballast water discharge (ton)</td></tr><tr><td colspan="6">Models</td></tr><tr><td colspan="2">Great Lakes</td><td colspan="2">European</td><td colspan="2">Brisbane</td></tr><tr><td>Original</td><td>Modified</td><td>Original</td><td>Modified</td><td>Original</td><td>Modified</td></tr><tr><td>2002</td><td>10,304,576</td><td>335,212</td><td>2,492,883</td><td>794,646</td><td>7,393,302</td><td>953,850</td></tr><tr><td>2001</td><td>10,495,714</td><td>331,830</td><td>2,395,673</td><td>722,246</td><td>8,340,648</td><td>806,579</td></tr><tr><td>2000</td><td>10,827,394</td><td>359,873</td><td>1,348,433</td><td>647,894</td><td>7,644,733</td><td>853,067</td></tr><tr><td>1999</td><td>11,322,104</td><td>370,160</td><td>2,285,337</td><td>737,999</td><td>7,100,306</td><td>802,599</td></tr><tr><td>1998</td><td>10,866,746</td><td>348,072</td><td>2,728,990</td><td>800,631</td><td>7,172,106</td><td>840,314</td></tr></table>

All models were applied in Slovenia for a <sup>fi</sup>ve years period (1998 to 2002, study 1). The data about vessel calls and cargo operations in the Port of Koper were obtained from the Slovenian maritime authorities and the Port of Koper operator. Results showed relatively high variation among different approaches. The models were reviewed and some modi<sup>fi</sup>cation has been made to adjust the models for shipping characteristics in Slovenia [41,46] (Table 2).

The previously developed models were believed not to be reliable enough and accurate for the purposes of our studies. Further, even more important for the scope of our studies, none of the approaches and models were found appropriate to assess/predict ballast water discharge at the level of an individual vessel.

## 2.3. The model development

The authors decided to develop a new model, which would enable the assessment of ballast water operations for each vessel arrival to the port, and with this an overall assessment for the past, as well as future ballast water discharges could also be conducted. The goal was to obtain as much as possible reliable results (assessments) that would be possibly based on easily available data, i.e., data regularly collected from a port or maritime authority on each vessel arrival. Ballast water processes onboard vessels, i.e., vessel operation and decision making of responsible of<sup>fi</sup>cers regarding ballast water operations, were studied to identify possible correlations among ballast water operations and basic vessel operations and dimensions. The experience of the authors in the <sup>fi</sup>eld of vessel operation triggered the idea on the possible correlation between the cargo and ballast operation, and vessel's DWT. The cargo operation of a vessel in relation to her DWT was found as the key component for assessing the amount of ballast water discharged in a port.

Assessed percentage of vessel ballast water capacity in relation to the vessel DWT, based on different vessel types (GC = General Cargo; BC = Bulk Carrier, C = Container, T = Tanker, Pas = Passenger, RR = Roll on Roll off).

<table><tr><td>Type (DWT)</td><td>AQIS [1]</td><td>Walters [48]</td><td>Wiley [49]</td><td>Carlton et al. [4]</td><td>Farley [19]</td><td>Cohen [7]</td><td>Dobes [17]</td><td>Hay and Tanis [29]</td><td>Behrens et al. [2]</td><td>Suban [45]</td></tr><tr><td>All vessels</td><td></td><td></td><td>30</td><td>38</td><td>40</td><td>36</td><td>33</td><td></td><td>36</td><td>33</td></tr><tr><td>BC</td><td></td><td>41</td><td></td><td>43</td><td></td><td></td><td></td><td>60</td><td></td><td>33</td></tr><tr><td>BC (250,000)</td><td>30/45</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>BC (150,000)</td><td>30/45</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>30/45</td></tr><tr><td>BC (70,000)</td><td>36/57</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>30/45</td></tr><tr><td>BC (35,000)</td><td>30/49</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>33/57</td></tr><tr><td>T</td><td></td><td>26</td><td></td><td>38</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>T (100,000)</td><td>40/45</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>T (40,000)</td><td>30/38</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>43</td></tr><tr><td>C</td><td></td><td>30</td><td></td><td>32</td><td></td><td></td><td></td><td>30-60</td><td></td><td>35</td></tr><tr><td>C (40,000)</td><td>30/38</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>28/40</td></tr><tr><td>C (15,000)</td><td>30</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>30</td></tr><tr><td>GC</td><td></td><td>35</td><td></td><td></td><td></td><td></td><td></td><td>30-60</td><td></td><td>29</td></tr><tr><td>GC (17,000)</td><td>35</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>GC (8000)</td><td>38</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Pas/RR</td><td>33</td><td>38</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>43</td></tr></table>

Overall model assessment results compared to ballast water discharges in the Port of Koper (2004 to 2006) documented by BWRF, indicating correct, as well as false negative and positive ballast water discharges assessed by the model.

<table><tr><td rowspan="2"></td><td colspan="2">BWDA model assessment</td><td colspan="2">BWRF declaration</td></tr><tr><td>Quantities&#x27; [ton]</td><td>Vessels [number]</td><td>Quantities&#x27; [ton]</td><td>Vessels [number]</td></tr><tr><td colspan="5">All vessels (3451)</td></tr><tr><td>Overall estimated BW discharge</td><td>1,198,996</td><td>1211</td><td>1,011,762</td><td>644</td></tr><tr><td>No BW discharge</td><td>0</td><td>2240</td><td>0</td><td>2897</td></tr><tr><td>BW discharge - identical vessels</td><td>857,331</td><td>470</td><td>958,824</td><td>470</td></tr><tr><td>No BW discharge - identical vessels</td><td>0</td><td>2159</td><td>0</td><td>2159</td></tr><tr><td>False negative BW discharge</td><td>-</td><td>-</td><td>52,938</td><td>81</td></tr><tr><td>False positive BW discharge</td><td>341,663</td><td>738</td><td>-</td><td>-</td></tr></table>

For such an assessment, the following input data were needed:

• vessel's cargo operation, i.e., cargo loading, unloading or both, for each vessel call to the port;

• type of cargo;

• quantity of cargo in tons; and

• vessel's DWT in tons.

The Ballast Water Discharge Assessment (BWDA) model was developed in the form of a <sup>fl</sup>owchart. To calibrate the model the correlations among the cargo and ballast operation and vessels DWT, i.e., percentage of the ballast water discharged as a result of the percentage of the cargo loaded in relation to the vessels DWT, were analyzed as approximately 10,500 ballast water relevant vessel calls in Slovenian waters in a <sup>fi</sup>ve year period (2002 to 2006, study 2). Further, about 50 vessels of different types and dimensions were boarded in the Port of Koper to study their ballast water operations in detail, i.e., responsible of<sup>fi</sup>cers were interviewed, log books were checked and vessels stability books were used to do detailed calculations.

For the purpose of this study different cargo types were grouped in two main groups, i.e., very light cargoes and all other cargoes. Very light cargoes were identi<sup>fi</sup>ed as cargoes with the stowage factor<sup>1</sup> above 2.5 m<sup>3</sup>/ton. In the Port of Koper study these were only timber and livestock (for more explanations see Discussion).

## 2.3. Model application and results verification

In fall 2001 voluntary ballast water reporting with ballast water reporting forms (BWRF) was introduced for the Port of Koper to collect data on ballast water discharges. The model presented in this publication was used to assess ballast water discharges in the Port of Koper during 1990–2006. The results of the BWDA model were compared with the data collected with BWRF for the period from January 2004 to December 2006.

The reliability/accuracy, i.e., veri<sup>fi</sup>cation, of the model was studied based on the comparison of model results with the veri<sup>fi</sup>ed data collected with BWRFs. BWRFs of 3618 vessels were checked if all necessary data were reported. Obvious reporting errors resulted in the exclusion of a further 167 reports (4.6%). As the correct data on vessels' DWT is essential for the model, these were veri<sup>fi</sup>ed<sup>2</sup> for the remaining BWRFs of 3451 vessel calls, and 67 vessels were corrected accordingly. The <sup>fi</sup>nal data were deemed reliable and therefore used for the model veri<sup>fi</sup>cation analyses (see Table 3). This study is also unique compared to others, where models or reporting forms were applied alone, but the reliability/accuracy of the model or the data reported was not “cross-checked”.

## 2.4. Port of Koper profile

Port of Koper is a multi-purpose port, where many different types of vessels discharge or load (or do both) many different types of cargo. In the period from January 2004 to December 2006 6934 vessel calls were registered. 3879 of these vessels discharged 27.8 million tons of cargo, and 4237 vessels loaded 12.2 million tons of cargo, so that 1867 vessels, i.e., container vessels, Ro-Ro car carriers and general cargo vessels, conducted cargo loading and unloading operations during one call (see Figs. 1 and 2). This pro<sup>fi</sup>le adds complexity to the assessment of ballast water discharges, especially if this is to be conducted on the level of an individual vessel.

## 3. The BWDA model

## 3.1. BWDA model basic principles

The cargo operation of a vessel in relation to her DWT was identi<sup>fi</sup>ed as the key component in assessing the quantity of ballast water discharged in a port on a single vessel call basis. Based on studies and calibrations conducted, the following basic principles and relations were identi<sup>fi</sup>ed to best represent relations between cargo and ballast water operations:

• A vessel that unloads cargo does not discharge ballast water.

![](/api/attachments/QCEEU2EK/fulltext/images/c4641e7b84c20632f4db3f958ca225a26b86d88420b1e4bd201a7e41ee0cac3c.jpg)  
Fig. 1. Number of vessels calling for the Port of Koper according to cargo operation (2004 to 2006).

![](/api/attachments/QCEEU2EK/fulltext/images/fe4f12970891ce42c69c82275693a9148133745bc2b6d0fda8182e45be7d6c3f.jpg)  
Fig. 2. Loaded and unloaded cargo type and quantities (ton, t) according to number (n) of vessels in the Port of Koper (2004 to 2006).

• A vessel that loads cargo in general discharges ballast water, but: a vessel that loads very light cargo will not discharge ballast water; and

a vessel that loads less than 10% of cargo in relation to vessel's DWT will not discharge ballast water.

• A vessel that conducts loading and unloading of cargo in a port will discharge ballast if the loaded quantity of cargo is bigger than the unloaded quantity, and that this difference is bigger than 10% of the vessel's DWT.

• The quantity of ballast water discharge will on average amount to 20% of the cargo loaded, if this represents more than 10% and less than 50% of the vessel's DWT.

• The quantity of ballast water discharge will on average amount to 25% of the cargo loaded, if this represents more than 50% and less than 80% of the vessel's DWT.

• The quantity of ballast water discharge will in average amount to 33% of the cargo loaded, if this represents more than 80% of the vessel's DWT.

## 3.2. Generic BWDA model

The basic principles and relations are arranged in the <sup>fl</sup>ow-chart model (Fig. 3). The model's <sup>fi</sup>rst criterion to determine whether a ballast water discharge will occur is the qualitative cargo operation, i.e., cargo loading vs. unloading. If the vessel is identi<sup>fi</sup>ed that will discharge ballast water, the process continues with the assessment of the quantity of discharged ballast water based on the quantity of loaded cargo in relation to the vessels DWT as the second criterion.

## 4. Results

4.1. Ballast water discharge quantities in the Port of Koper calculated by the model

An overview of calculated ballast water discharges in correlation to loaded cargo for the period 1990 to 2006 is presented as yearly quotas in Fig. 4. A correlation between the volume of loaded cargo and discharged ballast is clearly visible, i.e., the more cargo was loaded the more ballast water was discharged.

## 4.2. BWDA model verification

Veri<sup>fi</sup>ed information for 3451 vessel calls was deemed reliable, and was therefore used for the model veri<sup>fi</sup>cation analyses (see Table 3). The declared ballast water discharges of these vessels amount to 1,011,762 tons, while the model assessment resulted in 1,198,996 tons, 17% more than the declared quantity. However, when analyzing the vessels itself it was noted that out of the total 3451 vessel calls just 644 vessels (19%) declared a ballast water discharge compared to the 1211 (35%) vessels for which the model had foreseen a ballast water discharge.

When comparing the amount of ballast water discharged only for the 470 (14%) vessels, which declared ballast water discharge and at the same time were recognized by the model as vessels to discharge ballast water, i.e., correctly assessed, the total amount of ballast water discharge was 958,824 tons compared to 857,331 tons assessed by the model. Further, the model did correct assessments for 2159 (63%) vessels that have declared not to discharge ballast water. In 738 (21%) cases the model assessed ballast water discharges which was not declared by vessels, and this is a “false positive” assessment. This is equal in total to 341,663 tons of undeclared ballast water discharges. In 81 (2%) cases the model did not predict ballast water discharges while this was declared, resulting in a model underestimation of 52,938 (5%)tons of released ballast, and this is a “false negative” assessment (see Table 3).

For the purpose of a more detailed analysis, and to possibly identify model weaknesses in 81 cases of false negative assessment, the model results and declared information were grouped according to the relation between the loaded cargo quantity and vessels' DWT. Four groups were obtained, i.e., (1) the loaded cargoes represent two thirds or more of the vessels' DWT; (2) the loaded cargoes represent between one third and two thirds of the vessels' DWT; (3) the loaded cargoes represent one third or less of the vessels' DWT. Some vessels that have loaded more cargo than discharged have also declared to have discharged ballast water, and these were analyzed in group (4) (see Table 4).

![](/api/attachments/QCEEU2EK/fulltext/images/2b3b9b948e6c2ee81a7da4e8cba5feb336a26d85c83b344a965921cd7f876f24.jpg)  
Fig. 3. The BWDA model

For vessels in the <sup>fi</sup>rst group it can be expected that ballast water discharge will most probably occur, as there is a very low possibility that a vessel would load close to her full DWT capacity and would not discharge some ballast water. Table 4 shows that 644 vessel calls (18.5% of all analyzed vessels) fell into in this group and according to the model results they discharged 984,979 tons of ballast water. In contrast, according to the BWRF only 386 vessel calls appear in this group with 894,278 tons of ballast water discharged. When checking the data of 258 vessel calls in this group that did not declare the discharge of ballast water it was recognized that these were mainly very small vessels calling to the Port of Koper almost without ballast water and they arrived from nearby northern Adriatic ports, i.e., Monfalcone, Trieste, Grado and Venice. In this group the model performance was 100% for the group of vessels that declared no ballast water discharges.

Table 4  
![](/api/attachments/QCEEU2EK/fulltext/images/f482f029fa44421072dbd8d5982d3409c86859f61e642a27034ba44ed7564617.jpg)  
Fig. 4. Assessed ballast water discharges in correlation to the loaded cargo for the period 1990 to 2006 in the Port of Koper.

537 (15.5%) vessel calls were identi<sup>fi</sup>ed in the second group and, according to the model, they have discharged in total 149,066 tons of ballast water while having declared only 38,848 tons of ballast water discharged. Similar is the relation when looking at the number of vessels that have declared ballast water discharge (61) compared to the numbers foreseen by the model for discharge (398). According to the model, among the 61 vessels that declared discharge only 4 with a total of 876 tons would not discharge ballast water. The ballast water discharge quantities assessed for the remaining 57 vessels were almost equal to the declared ones, and the model also very accurately identi<sup>fi</sup>ed 135 vessel calls with no ballast water discharge. For this group the model failed in 4 cases mismatching only 876 tons of discharged ballast, consequently the model performance was 93% correct in vessels identi-<sup>fi</sup>cation and 98% in assessing the quantities of ballast water discharged.

Model assessment results compared to ballast water discharges in the Port of Koper (2004 to 2006) documented by BWRF according to the relation of vessels cargo operations and DWT, indicating correct, as well as false negative and positive ballast water discharges assessed by the model.

<table><tr><td rowspan="2"></td><td colspan="2">BWDA model assessment</td><td colspan="2">BWRF declaration</td></tr><tr><td>Quantities&#x27; [ton]</td><td>Vessels [number]</td><td>Quantities&#x27; [ton]</td><td>Vessels [number]</td></tr><tr><td colspan="5">Cargo operation and ballast onboard exceeded 66% of DWT (644 vessels)</td></tr><tr><td>Estimated BW discharge</td><td>984,979</td><td>644</td><td>894,278</td><td>386</td></tr><tr><td>Without BW discharge</td><td>-</td><td>0</td><td>-</td><td>258</td></tr><tr><td>BW discharge - identical vessels</td><td>806,847</td><td>386</td><td>894,278</td><td>386</td></tr><tr><td>No BW discharge - identical vessels</td><td>-</td><td>0</td><td>-</td><td>0</td></tr><tr><td>False negative BW discharge</td><td>-</td><td>-</td><td>0</td><td>0</td></tr><tr><td>False positive BW discharge</td><td>178,132</td><td>258</td><td>-</td><td>-</td></tr><tr><td colspan="5">Cargo manipulation and ballast onboard 34%-66% of DWT (537 vessels)</td></tr><tr><td>Estimated BW discharge</td><td>149,066</td><td>398</td><td>38,848</td><td>61</td></tr><tr><td>Without BW discharge</td><td>-</td><td>139</td><td>-</td><td>476</td></tr><tr><td>BW discharge - identical vessels</td><td>38,342</td><td>57</td><td>38,848</td><td>57</td></tr><tr><td>No BW discharge - identical vessels</td><td>-</td><td>135</td><td>-</td><td>135</td></tr><tr><td>False negative BW discharge</td><td>-</td><td>-</td><td>876</td><td>4</td></tr><tr><td>False positive BW discharge</td><td>110,724</td><td>339</td><td>-</td><td>-</td></tr><tr><td colspan="5">Cargo manipulation and ballast onboard 0%-33% of DWT (722 vessels)</td></tr><tr><td>Estimated BW discharge</td><td>64,950</td><td>171</td><td>28,229</td><td>41</td></tr><tr><td>Without BW discharge</td><td>-</td><td>551</td><td>-</td><td>681</td></tr><tr><td>BW discharge - identical vessels</td><td>12,142</td><td>30</td><td>26,574</td><td>30</td></tr><tr><td>No BW discharge - identical vessels</td><td>-</td><td>539</td><td>-</td><td>539</td></tr><tr><td>False negative BW discharge</td><td>-</td><td>-</td><td>1665</td><td>11</td></tr><tr><td>False positive BW discharge</td><td>1780</td><td>141</td><td>-</td><td>-</td></tr><tr><td colspan="5">Cargo manipulation and ballast onboard towards lightering DWT (1548 vessels)</td></tr><tr><td>Estimated BW discharge</td><td>0</td><td>0</td><td>50,407</td><td>65</td></tr><tr><td>Without BW discharge</td><td>-</td><td>1548</td><td>-</td><td>1483</td></tr><tr><td>BW discharge - identical vessels</td><td>0</td><td>-</td><td>0</td><td>-</td></tr><tr><td>No BW discharge - identical vessels</td><td>-</td><td>0</td><td>-</td><td>0</td></tr><tr><td>False negative BW discharge</td><td>-</td><td>-</td><td>50,407</td><td>65</td></tr><tr><td>False positive BW discharge</td><td>-</td><td>-</td><td>-</td><td>-</td></tr></table>

722 (21%) vessel calls were recognized to be in the group where the loaded cargoes represent one third or less of the vessels DWT, from which 551 vessel calls were assessed by the model as not discharging ballast water, while 171 vessel calls were assessed to have discharged ballast water in the total quantity of 64,950 tons. In this group vessels reported 41 discharges totalling to 28,229 tons of ballast water. The model did not predict discharge in 11 cases of the 41 declared at a total declared quantity of 1665 tons of ballast water. When analyzing this discrepancy in more detail we noted that in all 11 cases added cargo weight was only 4% of the vessel's DWT and that all vessels were container type vessels that performed both loading and unloading cargo operations. The model performance for this group of cargo operation is 73% for vessel identi<sup>fi</sup>cation and 94% for discharged quantities. Additionally, the model predicted 141 discharges of ballast water totalling to 1780 tons which were not declared. In 539 vessel calls the model predicted no discharge, which was in line with the vessel declarations.

Vessel calls where more cargo was unloaded than loaded were also analyzed to cover all vessel calls studied. 1548 (45%) vessel calls were identi<sup>fi</sup>ed with this pro<sup>fi</sup>le. Total cargo unloaded amounted to 14,323,010 tons, and total cargo loaded to 959,238 tons. The model by default does not predict discharges of ballast water in such cases, while 65 vessels declared ballast water discharges that amounted to 50,407 tons. These were mainly container vessels that have on average unloaded 7094 tons and loaded 1796 tons of cargo. Vessel calls with this pro<sup>fi</sup>le were identi<sup>fi</sup>ed as critical for the model.

Further, a detailed analysis on a vessel-by-vessel study has shown that there was also a relatively high number of vessels for which the model resulted in an overestimation of very small quantities of ballast water discharges, i.e., less than 1000 tons (Fig. 5). However, a false assessment of such small quantities per vessel does not vary much.

![](/api/attachments/QCEEU2EK/fulltext/images/f51d38a91d1cb31295238cb72a27ec67bca9bff1cfba3ed75c1ad4bbb6c8806d.jpg)  
Fig. 5. Correlation between the assessed and declared quantities of ballast water discharges in the Port of Koper (2004 to 2006) declared by BWRF (diagonal dark gray line) and estimated by the BWDA model (diamonds) for selected vessels; the white area surrounding the dark gray line means the area of 50% discrepancy, and the light gray shaded is the area of up to 100% discrepancy of the BWDA model result regarding the declared discharged quantity in BWRE

Some deviations on the negative side, i.e., underestimation, were also recognized in cases where vessels loaded timber to their full capacity, and those that, at arrival, were loaded more than 50% of their DWT.

## 5. Discussion

Previous studies conducted elsewhere developed different approaches and models for the assessment of ballast water discharges. Most authors based their estimations on the correlation between vessel's deadweight (DWT) and ballast water on board for different vessel types (Table 1). Different authors used different ratios, i.e., percentage, between vessels ballast water capacity and vessels DWT, what unavoidably generated different ballast water discharge estimations among models. Available statistics on ballast tank capacities expressed as the ratio with vessels DWT either generally for all vessels or in some cases for particular vessel size and type is shown in Table 1. Here as an example; the Det Norske Veritas [2] statistical analysis has been undertaken for 100 cargo vessels with dedicated ballast tanks, built after 1990. The average ballast water capacity was found to be 36% of the DWT. For bulk carriers, tankers and container vessels, these results correspond with the statistical relation of vessels reported by Carlton et al. [4]. The correlation coef<sup>fi</sup>cient varied from 0.90 to 0.97 for the different vessel types as documented in Behrens et al. [2]. Research on those relations has been conducted also for vessels arrived in the Port of Koper in 2000 in which 1209 different vessel were analyzed and the average ballast water capacity was found to be 33% of the DWT.

Further, when applying the existing discharge models to the Port of Koper vessel traf<sup>fi</sup>c data, the results have shown high difference among them (Table 2, left columns). The average assessed quantities of the Great Lakes model were 5 times higher than those of the European model, because according to the North American model it is assumed that all vessels calling to a port will discharge ballast; the Brisbane model was believed to overestimate assessed discharges because it simply multiples tons of cargo imported with average ballast water capacities. The European model calculates discharges according to the manipulated cargo quantities divided into domestic and international trade and furthermore applies different ballast water capacities for different vessel types, what generates more precise results, but was still felt to overestimate discharges. After having reviewed and adapted the models, i.e., generally exclude vessels that only unload cargo, and for vessels that simultaneously unload and load cargo, the ballast water discharge was assessed with application of a reduction factor to suit better the pro<sup>fi</sup>le to the Port of Koper, the estimated ballast water discharges were much lower (Table 2, right columns), but still a relatively high difference occurred among them, and also showed different patterns than before, i.e., average assessed quantities of the Brisbane modi<sup>fi</sup>ed model were more than 2.4 times higher than those of the Great Lakes modi<sup>fi</sup>ed model, and in maximum were also more than 2.8 times higher.

Considering all this and more in depth studies of ballast water discharge pro<sup>fi</sup>les and vessel operations, it was recognized that the differences among obtained ballast water discharge assessment results do not derive only from the differences among the assessments of the ballast water capacity, but mainly from the interpretation of the relation between ballast water discharges and cargo operations.

For instance, when a vessel is not fully laden, i.e., when her carrying capacity in terms of weight (DWT) is not fully exploited, additional weight is required to compensate for the increased buoyancy that can result in the lack of propeller immersion, inadequate transversal and longitudinal inclination, static and dynamic stresses on the vessel's hull including shear forces and bending moments, and static and dynamic transversal and longitudinal stabilities, in order to provide for the vessel's seaworthiness.

Cargo vessels, such as, general cargo, Ro-Ro, e.g., ferries and car carriers, use only small quantities of ballast water, i.e., some 20% of their DWT. On the other hand, vessels for the transport of liquid and dry bulk cargoes, e.g., tankers, dry-bulk carriers, require signi<sup>fi</sup>cantly larger quantities of ballast water, i.e., mostly between 30 and 50% of their DWT, what means also up to more than 100,000 tons of ballast water per vessel. When calculating ballast water discharges in relation to a vessel's DWT, it is necessary to consider the fact that a vessel is not loading the full DWT capacity but a deduction of the weight of stores, fuel, fresh water and other weights needs to be taken into account. This weight usually represents about 5–10% of the vessel's DWT [15,41,45].

As stated in most studies related to ballast water, a vessel discharges ballast when she loads cargo, and the reverse. Logically, it appears that all vessels that load cargo in a port consequently discharge ballast. But in reality the situation is not so simple. Vessels load different types of cargoes, which could be divided into speci<sup>fi</sup>cally heavy, e.g., metal rolls, steel, iron, ore, carbon, oils, and light, e.g., grain, timber, paper as pulp, vehicles, and containers.

In the case of heavy cargo, a vessel will be immersed to the maximum load line<sup>3</sup> and must discharge all ballast to load as much cargo as possible. This means that the vessel will discharge all ballast except the quantity unable to be discharged, and the quantity needed for compensating longitudinal, i.e., trimming, and transversal inclination, i.e., heeling. However, vessels carrying light cargoes usually load these in the cargo hold and some also above the main deck, e.g., typical example is in the case of loading timber cargo on the main deck. This negatively impacts ships stability, consequently it is necessary to retain some ballast in lower tanks, e.g., double bottom tanks, or in some cases to load additional ballast to provide for vessels stability. After having studied different types of ships and cargoes, it was recognized that in general cargoes with the stowage factor above 2.5 m<sup>3</sup>/ton can be considered as very light cargoes for these purposes.

Some vessels usually discharge and load cargo during one port call, e.g., containers and vehicles. In these cases the ballast water operations depend on the quantity of unloaded and loaded cargoes. If the quantity of unloaded cargo is greater than that of the loaded, it is supposed that the vessel will not discharge ballast and vice versa. After having studied vessel operation patterns it was recognized that in general vessels that were loading less than 10% of vessels DWT were not discharging ballast water.

The quantity of ballast water may also depend on weather conditions. When expecting to sail through bad weather conditions and heavy seas vessels would be in heavy ballast condition to improve the safety of navigation.

Tanker vessels carrying heavy oil and bulk carriers mostly conduct full cargo operation in a port, i.e., arrive empty in the port of loading and load cargo to their full capacity, and unloaded it in another. On the other hand, general cargo, container vessels and car carriers will mostly carry some cargo, i.e., some will be unloaded and some loaded at the next port of call. These vessels can thus carry ballast water taken up in different ports. The quantity of ballast water carried, however, primarily depends on the cargo handling operations carried out. Therefore, if a signi<sup>fi</sup>cantly greater quantity of cargo is discharged than loaded, it may be assumed that ballast water will be required on board, and vice versa [15,41,45].

All these different situations are related to different vessel types, vessel construction, cargo operation and weather conditions, which makes the process of ballast water discharge assessment complex. There are also no clear limits among all these factors, but the decision on ballast water operation is under the discretion of the chief of<sup>fi</sup>cer or captain, who is responsible for the vessels stability and safety. It is clear that all these parameters and conditions in general make the ballast water discharge assessment dif<sup>fi</sup>cult. But to be accurate in an assessment for vessels that conduct only partial cargo operations, or partially load and unload cargo at the same port, is even much more dif<sup>fi</sup>cult; almost impossible.

One of the critical aspects in such assessments is also the data availability to run the model. All-around the world vessels need to report to the responsible maritime authorities before (or when) entering a port. Different data are required to obtain the permit, i.e., “Free pratique”, to start operations in a port. There are some differences in reporting requirements by different port states, but the information required to run the BWDA model is required in all ports as this is basic information to conduct cargo operations in a port.

In our study, data from BWRFs were used for the model validation. The key issue identi<sup>fi</sup>ed was the reliability of the reported data. The identi<sup>fi</sup>cation of errors was found important to exclude the false/ non-accurate information. The errors identi<sup>fi</sup>ed were mainly related to exceeding the maximum DWT for selected vessels that loaded cargo and at the same time did not declare a discharge of ballast water. When analyzing the data it was recognized that most of these vessels spent some time at the anchorage before entering the port, and hence it was assumed that they discharged ballast water at anchorage and this was later reported as zero or as lower in quantity discharge in the port. There were also cases when the vessels from ports in the vicinity, mostly Trieste, Italy, which is just 5 nautical miles away from Koper, already discharged ballast on the way or they arrived without ballast, which is not according to the safe practice. This was also con<sup>fi</sup>rmed by port authorities, but as they were sailing short distances this was of no consequence. Some different types of errors are shown in Table 5.

For instance, the <sup>fi</sup>rst vessel listed in Table 5 declared “0” ballast water discharge, but at the same time declared to load 24,150 tons of cargo, what represents 86% of her maximum DWT. By adding the initially declared ballast on board (7589 tons) this sums up to 112% of the vessel's DWT, which is impossible (see Table 5 under “Remarks”, cases like this are shown as “exceed DWT”). Further there were many similar cases when cargo was declared to be loaded to the vessel's maximum DWT, but the vessel still did not declare de-ballasting (see Table 5 under “Remarks”, cases like this are marked with “max. DWT”) which is possible, but in normal vessel operation ballast water not needed is discharged to carry less weight and consequently consume less fuel in navigation.

The analysis of the BWDA model accuracy identi<sup>fi</sup>ed that the mode performance decreases when the ratio of cargo loaded against cargo unloaded is lower. The model performance regarding the ballast water discharge assessment was excellent (100%) for those vessels where loading against unloading exceeded 66% of the vessel maximum DWT. The performance was still high (93%) for the vessels where the ratio between loading and discharging was in the range of 34–66% of the vessel maximum DWT. For the vessels where loading was greater than discharging for approximately 33% of the vessel maximum DWT the model still showed a good accuracy level (73%).

For the last group where the quantity of cargo unloaded is bigger than the loaded the model failed in 65 (4%) cases out of 1548 vessels in the group, i.e., the model always recognizes vessels in this group with “0” discharge. It can also be assumed that some of these 65 vessels declared de-ballasting by mistake. To try to solve this inaccuracy, further work would be necessary to analyze in more detail the ballast water discharge patterns of vessels that load more cargo than they unload. For instance, additional data, e.g., exact vessel's drought at entering and leaving the port as well as hydrostatic particulars of these vessels could be helpful for such calculations.

## 6. Conclusions

Given that the quantities of ballast water discharges are one of the most important input details for ballast water risk assessment and management decision support, clearly a reliable assessment model is of high demand. As existing models have not yielded satisfactory accuracy levels, this study was conducted to develop a more accurate model.

Table 5  
Vessel particulars and identi<sup>fi</sup>cation of errors comparing the documented ballast water situation of selected vessels calling for the Port of Koper (2004 to 2006) with the ballast water discharges calculated by the model.

<table><tr><td>Vessel name</td><td>Ancho rage [days]</td><td>Last port of call</td><td>Ship type</td><td>Loaded-unloaded [t]</td><td>Cargo/DWT</td><td>Model - ballast discharge [t]</td><td>BWRF - ballast discharge [t]</td><td>Difference [t]</td><td>DWT (BWRF)</td><td>Ballast on board [t]</td><td>Tanks in ballast [no.]</td><td>Total ballast capacity  $\left\lbrack {\mathrm{m}}^{3}\right\rbrack$ </td><td>All ballast tanks [no.]</td><td>Remarks</td></tr><tr><td>ELI***</td><td>0.44</td><td>LA GOLETE</td><td>GC</td><td>24,150</td><td>86%</td><td>8050</td><td>0</td><td>8050</td><td>112%</td><td>7589</td><td>18</td><td>8650</td><td>20</td><td>Exceed DWT</td></tr><tr><td>HUN***</td><td>1.42</td><td>RAVENNA</td><td>GC</td><td>10,513</td><td>83%</td><td>3504</td><td>0</td><td>3504</td><td>96%</td><td>1597</td><td>7</td><td>3830</td><td>14</td><td>Max. DWT</td></tr><tr><td>TRO***</td><td>0.85</td><td>VENEZIA</td><td>GC</td><td>7675</td><td>90%</td><td>2558</td><td>0</td><td>2558</td><td>100%</td><td>859</td><td>9</td><td>859</td><td>9</td><td>Max. DWT</td></tr><tr><td>ABU***</td><td>0.28</td><td>P. MARGHERA</td><td>RR</td><td>8149</td><td>64%</td><td>2037</td><td>0</td><td>2037</td><td>82%</td><td>2290</td><td>8</td><td>3180</td><td>11</td><td>Anchorage</td></tr><tr><td>ELG***</td><td>2.32</td><td>RIJEKA</td><td>GC</td><td>9913</td><td>42%</td><td>1983</td><td>0</td><td>1983</td><td>57%</td><td>3598</td><td>16</td><td>4373</td><td></td><td>Anchorage</td></tr><tr><td>ABU***</td><td>0.91</td><td>P. NOGHARO</td><td>RR</td><td>7774</td><td>61%</td><td>1944</td><td>0</td><td>1944</td><td>80%</td><td>2473</td><td></td><td>3180</td><td>11</td><td>Anchorage</td></tr><tr><td>PRO***</td><td>0.04</td><td>PORTO NOGHARO</td><td>GC</td><td>5379</td><td>96%</td><td>1793</td><td>0</td><td>1793</td><td>96%</td><td>0</td><td>0</td><td>1200</td><td>8</td><td>Full loading</td></tr><tr><td>ELD***</td><td>0.38</td><td>CHIOGGIA</td><td>GC</td><td>6974</td><td>73%</td><td>1744</td><td>0</td><td>1744</td><td>83%</td><td>1010</td><td>2</td><td>4064</td><td>8</td><td>Anchorage</td></tr><tr><td>JAR***</td><td>2.55</td><td>TRIESTE</td><td>GC</td><td>6668</td><td>70%</td><td>1667</td><td>0</td><td>1667</td><td>103%</td><td>3200</td><td>6</td><td>4064</td><td>7</td><td>Exceed DWT</td></tr><tr><td>ELD***</td><td>0.20</td><td>TRIESTE</td><td>GC</td><td>6516</td><td>68%</td><td>1629</td><td>0</td><td>1629</td><td>88%</td><td>1900</td><td>4</td><td>4000</td><td>8</td><td>Anchorage</td></tr><tr><td>ELD***</td><td>2.04</td><td>MISURATA</td><td>GC</td><td>6491</td><td>68%</td><td>1623</td><td>0</td><td>1623</td><td>97%</td><td>2846</td><td>6</td><td>3834</td><td>8</td><td>Max. DWT</td></tr><tr><td>LAD***</td><td>6.79</td><td>RAVENNA</td><td>GC</td><td>4805</td><td>94%</td><td>1602</td><td>0</td><td>1602</td><td>94%</td><td></td><td>6</td><td></td><td>6</td><td>Full loading</td></tr><tr><td>TAB***</td><td>1.13</td><td>BIZERTA</td><td>RR</td><td>2800</td><td>89%</td><td>933</td><td>0</td><td>933</td><td>99%</td><td>315</td><td>1</td><td>1352</td><td>10</td><td>Full loading</td></tr><tr><td>TAB***</td><td>0.72</td><td>MISURATA</td><td>RR</td><td>2791</td><td>89%</td><td>930</td><td>0</td><td>930</td><td>109%</td><td>612</td><td>4</td><td>1491</td><td>10</td><td>Exceed DWT</td></tr><tr><td>GIN***</td><td>0.61</td><td>MONFALCONE</td><td>GC</td><td>2103</td><td>140%</td><td>701</td><td>0</td><td>701</td><td>179%</td><td>585</td><td></td><td>585</td><td></td><td>Exceed DWT</td></tr><tr><td>EME***</td><td>1.23</td><td>P. LEVANTE</td><td>GC</td><td>2624</td><td>70%</td><td>656</td><td>0</td><td>656</td><td>113%</td><td>1600</td><td>8</td><td>1600</td><td>8</td><td>Exceed DWT</td></tr><tr><td>KAI***</td><td>1.07</td><td>ALGER</td><td>GC</td><td>1800</td><td>81%</td><td>600</td><td>0</td><td>600</td><td>98%</td><td>391</td><td>7</td><td>401</td><td>7</td><td>Max. DWT</td></tr><tr><td>GIN***</td><td>0.59</td><td>MONFALCONE</td><td>GC</td><td>1758</td><td>117%</td><td>586</td><td>0</td><td>586</td><td>117%</td><td>0</td><td>0</td><td></td><td></td><td>Exceed DWT</td></tr><tr><td>YAV***</td><td>0.56</td><td>TRIPOLI</td><td>GC</td><td>1751</td><td>81%</td><td>584</td><td>0</td><td>584</td><td>104%</td><td>500</td><td>8</td><td>506</td><td>8</td><td>Exceed DWT</td></tr><tr><td>IRM***</td><td>0.91</td><td>P. MAREGHERA</td><td>GC</td><td>1497</td><td>94%</td><td>499</td><td>0</td><td>499</td><td>106%</td><td>190</td><td>4</td><td>555</td><td>14</td><td>Exceed DWT</td></tr><tr><td>GIN***</td><td>7.98</td><td>MONFALCONE</td><td>GC</td><td>1460</td><td>97%</td><td>487</td><td>0</td><td>487</td><td>131%</td><td>509</td><td>12</td><td>586</td><td>12</td><td>Exceed DWT</td></tr></table>

The asterisks were used not to show the full vessel names.

In this study, the vessels operational and ballast water discharge “behavior” have shown best correlation between the vessel's cargo operation and DWT, therefore the model was prepared on this basis. The data required to run the model are basic vessel data, i.e., DWT, and her cargo operation, which should be easy to obtain from port or maritime authorities.

The model veri<sup>fi</sup>cation process conducted on the maritime traf<sup>fi</sup>c in the Port of Koper, a multi-purpose port, showed an overestimation of 17% in the total ballast water discharge quantity. When other models were tested, the results before adaptation of the models, showed up to 5 times higher values, while after adaptation these ranged from an underestimation of 35% (the Great Lakes model) to 100% overestimation (the Brisbane model).

When considering the model's applicability for assessing ballast water discharges in advance and on a vessel-by-vessel basis, the veri<sup>fi</sup>- cation process has shown that the model failed to assess (predict) ballast water discharges from vessels in only 81 cases (2%) of the 3451 cases. Out of those 81 cases, 65 were related to the vessels calling for the Port of Koper mainly to load cargo. It is almost impossible to develop a model which enables ballast water discharge calculations for cases when more cargo is unloaded then loaded, as this would require speci<sup>fi</sup>c calculations including vessels stability for each such vessel call. Vessels that declared deballasting but the model did not assess those vessels as to have discharged ballast, were mainly container vessels that have on average discharged 775 tons of ballast, while on average unloaded 7094 tons of cargo and loaded 1796 tons of cargo.

The comparison of model results with BWRF data has also shown that vessels may for different reasons, e.g., scared of possible problems with port state authorities, do not declare ballast water discharges; however, if they declare a discharge and there are no obvious mistakes, the declared quantity may be deemed to be the real quantity of ballast water discharged.

During research studies the model was also used for targeting vessels for ballast water sampling in 2003. 15 vessels were accurately identi<sup>fi</sup>ed that will discharge ballast water, which was con<sup>fi</sup>rmed when the vessels arrived in the port and were boarded for sampling [12]. The sampling methods used and the biological results of this study are published elsewhere [12,13].

The authors believe that the presented BWDA model is accurate enough for a reliable assessment of ballast water discharges in a port as the decision supporting tool in ballast water management. The model can be used for both, the assessment of ballast water discharges in the past, and the assessment of the ballast water discharges in the future; and this can be done at the level of a single vessel, as well as cumulative for a port or an area.

The model was successfully applied also to assess ballast water discharges in some other ports and areas, i.e., Albanian ports Durres, Valore, Sarande and Shengjin; and the Polish Port of Gdynia, but the results could not be veri<sup>fi</sup>ed in terms of accuracy, as we had no other reliable data for comparison, e.g., veri<sup>fi</sup>ed ballast water reporting forms. Therefore we suggest that for further use of the model to assess ballast water discharges in other ports and areas, it may be advisable to consider also model veri<sup>fi</sup>cation tests, especially when applying it in ports (or terminals) with fundamentally different cargo pattern. In case this cannot be done, the errors presented here may be a good guidance to the errors expected.

The model can further be used as a decision supporting tool for different purposes in ballast water management. Historical data of ballast water discharges may be helpful when studying vessel and ballast water patterns through time and relating these to known introduced species. It may also be used to assess the suitability and dimensions of land-based ballast water reception facilities. Further, ballast water discharge estimations may enable an environmental impact assessment of ballast water treatment systems which make use of active substances, e.g., chemical treatment. For this purpose a worst case scenario may be developed, i.e., all ballast water discharged in a port was treated with the same active substance, to determine whether the remaining toxicity of the ballast water at discharge is environmentally acceptable. This is especially valid for possible long-term accumulation of such substances in the port environment. The assessment of ballast water discharges in advance on the level of single vessels calling to a port may also support ballast water management measures based on the level of the risk assessed. This would enable port state authorities to identify vessels that pose a higher risk and hence may introduce more stringent requirements, or at least trigger inspections to verify compliance. In case a low (acceptable) risk is identi<sup>fi</sup>ed, authorities could allow some relaxation in requirements and hence lower the unnecessary costs and burden on vessels, e.g., if a vessel would be found not compliant she may still be allowed to discharge ballast water in the port. In case a port state requires ballast water reporting from vessels, the model can be used also to verify the reported data.

Additional model improvements could be achieved when considering statistically obtained hydrostatic ballast water related parameters for different vessel sizes and types. This work is still under investigation. However, the authors believe that absolute accuracy is unattainable by using models. It may remain impossible to predict with absolute certainty the ballast water discharges, especially when vessels manipulate only minor cargo quantities and when they are performing simultaneous cargo loading and unloading operations. In some rare cases vessels may also discharge ballast water even when they unloaded a cargo, e.g., to quickly trim the vessel and when sailing between ports that are close to each other. All these operations are actually not simple mechanical operations, and there are no clear limits among these. Further, the decision on ballast water operations remains with the chief of-<sup>fi</sup>cer or captain to provide for most effective vessel operation and the safety within permissible limits.

## Acknowledgments

This study was carried out in the framework of the Slovenian research projects Harmful Introductions and Ballast Water Management in the Slovenian Sea, <sup>fi</sup>nancially supported by the Ministry of Education, Science and Sports of the Republic of Slovenia and the Port of Koper (Luka Koper d.d.), and Decision Model and Control of Ballast Water Management in the Slovenian Sea, <sup>fi</sup>nancially supported by the Slovenian Research Agency and the Port of Koper (Luka Koper d.d.). This contribution was also developed to support the project Vectors of Change in Oceans and Seas Marine Life, Impact on Economic Sectors (VECTORS), which has received funding from the European Community's Seventh Framework Programme (FP7/2007-2013) under Grant Agreement No. 266445.

## References

[1] AQIS, Ballast Water Management, Ballast Water Research Series Report No. 4, Australian Quarantine and Inspection Service, AGPS, Canberra, 1993.

[2] H.L. Behrens, Ø. Endresen, A. Mjelde, C. Garmann, Environmental Accounting System for Norwegian Shipping — EASNoS Phase 1 DNV Rep. No. 2002-1645, Høvik, Oslo, 2003.

[3] G.D. Bhatt, J. Zaveri, The enabling role of decision support systems in organizational learning, Decision Support Systems 32 (2002) 297–309.

[4] J.T. Carlton, Transoceanic and interoceanic dispersal of coastal marine organisms: the biology of ballast water, Oceanography and Marine Biology Annual Review 23 (1985) 313-374

[5] J.T. Carlton, D. Reid, H. Van Leeuwen, The Role of Shipping in the Introduction of Nonindigenous Aquatic Organisms to the Coastal Waters of the United States (other than the Great Lakes) and an Analysis of Control Options, Shipping Study I USCG Report No. CG-D-11-95, National Technical Information Service, Spring<sup>fi</sup>eld, VA, 1995.

[6] G.A. Casale, Ballast water — a public health issue? GloBallast Programme, IMO London, Ballast Water News 8 (2002) 4–5.

[7] A.N. Cohen, Ships' Ballast Water and the Introduction of Exotic Organisms into the San Francisco Estuary, Current Status of the Problem and Options for Management, San Francisco Estuary Institute, Richmond, CA, A report for the CALFED Category III Steering Committee, 1998.

[8] A.D.M. Coutts, T.J. Dodgshun, The nature and extent of organisms in vessel sea-chests: a protected mechanism for marine bioinvasions, Marine Pollution Bulletin 54 (2007) 876–886

[9] M. David, A Decision Support System Model for Ballast Water Management of Vessels Doctoral dissertation Uniy, Liubliana Portorož 2007.

[10] M. David, S. Gollasch, EU shipping in the dawn of managing the ballast water issue, Marine Pollution Bulletin 56 (2008) 1966–1972

[11] M. David, S. Gollasch, Risk assessment as a decision supporting tool in ballast water management, International Conference on Traf<sup>fi</sup>c Science — ICTS 2011, Portorož, Conference Proceedings, 2011, p. 6.

[12] M. David, M. Perkovič, Ballast water sampling as a critical component of biological invasions risk management, Marine Pollution Bulletin 49 (2004) 313–318.

[13] M. David, S. Gollasch, M. Cabrini, M. Perkovič, D. Bošnjak, D. Virgilio, Results from the <sup>fi</sup>rst ballast water sampling study in the Mediterranean Sea — the Port of Koper study, Marine Pollution Bulletin 54 (2007) 53–65.

[14] M. David, S. Gollasch, C. Hewitt, L. Jakomin, Ballast Water Management for European Seas — is There a Need for a Decision Support System? Conference Proceedings, Aberdeen, IEEE, 2007, p. 6.

[15] M. David, S. Gollasch, C. Hewitt, Global Maritime Transport and Ballast Wate Management, Springer Science, in preparation.

[16] R. Denzer, Generic integration of environmental decision support systems — stateof-the-art, Environmental Modelling and Software 20 (2005) 1217–1223.

[17] J.C. Dobes, Ballast Water Management — a Glimpse of the Future, ASNE Environmental Symposium — Technical Papers, 1997 http://www.pwsrcac.org/NIS/Tech0021.pdf.

[18] ENRC, Ballast Water and Hull Fouling in Victoria, Environment and Natural Resources Committee, Parliament of Victoria, No. 60 Session 1996/97, Victorian Government Printer, October 1997 Chapter 7, 1997.

[19] R. Farley, Analysis of Overseas Vessel Transits into the Great Lakes through Commercial Shipping and Resultant Distribution of Ballast Water, University of Michigan, College of Engineering, Department of Naval Architecture and Marine Engineering paper No. 331, University of Michigan, Ann Arbor, MI, 1996, pp. 12–19.

[20] P.W. Fofonoff, G.M. Ruiz, B. Steves, J.T. Carlton, In Ships or on Ships? Mechanisms of Transfer and Invasion for Non-native Species to the Coasts of North America, in: G.M. Ruiz, J.T. Carlton (Eds.), Invasive Species: Vectors and Management Strategies, Island Press, Washington, 2003, pp. 152–182.

[21] S. Gollasch, E. Leppäkoski, Risk assessment and management scenarios for ballast water mediated species introductions into the Baltic Sea, Aquatic Invasions 2 (2007) 313–340.

[22] S. Gollasch, K. Riemann-Zürneck, Transoceanic dispersal of benthic macrofauna: Haliplanella luciae (Verrill, 1898) (Anthozoa, Actinaria) found on a ship's hull in a shipyard dock in Hamburg harbour, Germany, Helgoländer Meeresunters 50 (1996) 253–258.

[23] S. Gollasch, Untersuchungen des Arteintrages durch den internationalen Schiffsverkehr unter besonderer Berücksichtigung nichtheimischer Arten, Doctoral Dissertation (in German), Univ. Hamburg, Verlag Dr. Kovac, Hamburg, 1996

[24] S. Gollasch, H. Rosenthal, H. Botnen, I. Laing, E. Leppäkoski, E. Macdonald, D. Minchin, M. Nauke, S. Olenin, S. Utting, M. Voigt, I. Wallentinus, Survival Rates of Zooplankton Taxa in Ballast Water during Short-term and Long-term Ocean-going Voyages, Report of the European Concerted Action Study “Testing Monitoring Systems for Risk Assessment of Harmful Introductions by Ships to European Waters”, 1996.

[25] S. Gollasch, E. Macdonald, S. Belson, H. Botnen, J. Christensen, J. Hamer, G. Houvenaghel, A. Jelmert, I. Lucas, D. Masson, T. McCollin, S. Olenin, A. Persson, I. Wallentinus, B. Wetsteyn, T. Wittling, Life in Ballast Tanks, in: E. Leppäkoski, S. Gollasch, S. Olenin (Eds.), Invasive Aquatic Species of Europe: Distribution, Impacts and Management, Kluwer Academic Publishers, Dordrecht, 2002, pp. 217–231.

[26] I. Graham, P.L. Jones, Expert Systems: Knowledge, Uncertainty, and Decision, Chapman and Hall, New York, 1988.

[27] G.M. Hallegraeff, C.J. Bolch, Transport of toxic dino<sup>fl</sup>agellate cysts via ship's ballast water, Marine Pollution Bulletin 22 (1991) 27–30.

[28] J.P. Hamer, I.A.N. Lucas, T.A. McCollin, Harmful dino<sup>fl</sup>agellate resting cysts in ships' ballast tank sediments; potential for introduction into English and Welsh waters, Phycologia 40 (2001) 246–255.

[29] C. Hay, D. Tanis, Mid Ocean Ballast Water Exchange: Procedures, Effectiveness and Verification. Cawthron Report No. 468, Wellington, 1998.

[30] C.L. Hewitt, M.L. Campbell, Mechanisms for the prevention of marine bioinvasions for better biosecurity, Marine Pollution Bulletin 55 (2007) 395-401.

[31] C.L. Hewitt, K.R. Hayes, Risk Assessment of Marine Biological Invasions, in: Leppäkoski, E. Gollasch, S. Olenin (Eds.), Invasive Aquatic Species of Europe — Distribution, Impact and Management, Kluwer Academic Publishers, Dordrecht, 2002, pp. 456–466

[32] C.L. Hewitt, M.L. Campbell, R.E. Thresher, R.E. Martin, S. Boyd, B.F. Cohen, D.R. Currie, M.F. Gomon, M.J. Keogh, J.A. Lewis, M.M. Lockett, N. Mays, M.A. McArthur, T.D. O'Hara, G.C.B. Poore, D.J. Ross, M.J. Storey, J.E. Watson, R.S. Wilson, Introduced and cryptogenic species in Port Phillip Bay, Victoria, Australia, Marine Biology 144 (2004) 183–202.

[33] S. Kerr, Ballast Water Ports and Shipping Study, Australian Quarantine and Inspection Service Ballast Water Research Series Report No. 5, AQIS, Canberra, 1994.

[34] M. Kettunen, P. Genovesi, S. Gollasch, S. Pagad, U. Star<sup>fi</sup>nger, P. ten Brink, C. Shine, Technical Support to EU Strategy on Invasive Alien Species (IAS) — Assessment of the Impacts of IAS in Europe and the EU, Final Module Report for the European Commission, Institute for European Environmental Policy (IEEP), Brussels, 2009.

[35] E. Leppäkoski, Introduced species — resource or threat in brackish-water seas? Examples from the Baltic and the Black Sea, Marine Pollution Bulletin 23 (1991) 219–223.

[36] A. Locke, D.M. Reid, H.C. van Leeuwen, W.G. Sprules, J.T. Carlton, Ballast water exchange as a means of controlling dispersal of freshwater organisms by ships, Canadian Journal of Fisheries and Aquatic Sciences 50 (1993) 2086–2093.

[37] A.C. Marquez, C. Blanchar, A Decision Support System for evaluating operations investments in high-technology business, Decision Support Systems 41 (2006) 472-487

[38] T. McCollin, A.M. Shanks, J. Dunn, Changes in zooplankton abundance and diversity after ballast water exchange in regional seas, Marine Pollution Bulletin 56 (2008) 834–844.

[39] M. Otani, Important Vectors for Marine Organisms Unintentionally Introduced to Japanese Waters, in: F. Koike, M.N. Clout, M. Kawamichi, M. De Poorter, K. Iwatsuki (Eds.), Assessment and Control of Biological Invasion Risks, Shoukadoh Book Sellers, Kyoto, Japan and IUCN, Gland, 2006, pp. 92–103.

[40] D. Paradice, Expanding the boundaries of DSS, Decision Support Systems 43 (2007) 1549–1552.

[41] M. Perkovič, V. Suban, M. David, Ballast Water Discharges in the Slovenian Sea, 8th International Conference on Traf<sup>fi</sup>c Science — ICTS 2004, Nova Gorica, Conference Proceedings, 2004, p. 12.

[42] E. Reeves, I.J.C. An, White Paper on Policies for the Prevention of the Invasion of the Great Lakes by Exotic Organisms, Milwaukee, 1999.

[43] G.M. Ruiz, T.K. Rawlings, F.C. Dobbs, L.A. Drake, T. Mullady, A. Huq, R.R. Colwell Global spread of microorganisms by ships: ballast water discharged from vessels harbors a cocktail of potential pathogens, Nature 408 (2000) 49–50.

[44] M.I.P. Rup, S.A. Bailey, C.J. Wiley, M.S. Minton, A.W. Miller, G.M. Ruiz, H.J. MacIsaac, Domestic ballast operations on the Great Lakes: potential importance of Lakers as a vector for introduction and spread of nonindigenous species, Canadian Journal of Fisheries and Aquatic Sciences 67 (2010) 256–268.

[45] V. Suban, Model določanja količine izpuščenega balasta za preteklo obdobje s pomočjo izvedenih podatkov, Master thesis, University of Ljubljana, Portorož, (In Slovenian language), 2006.

[46] V. Suban, M. David, M. Perkovič, Model for the Assessment of the Quantity of Ballast Water Discharges Using Ships' Traffic Data. 8. International Conference Maritime Transport and Infrastructure, Riga, Conference Proceedings, 2006, pp. 69–75.

[47] M. Vila, C. Basnou, P. Pyšek, M. Josefsson, P. Genovesi, S. Gollasch, W. Nentwig, S. Olenin, A. Roques, D. Roy, P.E. Hulme, DAISIE partners, How well do we understand the impacts of alien species on ecosystem services? A pan-European cross-taxa assessment, Frontiers in Ecology and the Environment 8 (2010) 135–144.

[48] S. Walters, Ballast Water, Hull Fouling and Exotic Marine Organism Introductions via Ships — a Victorian Study, Publication 494, Environment Protection Authority, Victoria, 1996.

[49] C. Wiley, Aquatic Nuisance Species: Nature Transport and Regulation, in: F.M. D'Itri (Ed.), Zebra Mussels and Aquatic Nuisance Species, Ann Arbor. Press, Chelsea, MI, 1997, pp. 55–63.

![](/api/attachments/QCEEU2EK/fulltext/images/094d7ce8b477555effe1f3b4617c3ef80e2f3fc6e55b48e901cac46da73c40db.jpg)

Matej David <sup>fi</sup>nished navigation studies (Maritime Transport), sailed on merchant vessels and is a Ship's Mate (deck of<sup>fi</sup>cer). He got his doctoral degree in the <sup>fi</sup>eld of maritime transport with a focus on ballast water management decision support based on risk assessment. He is professor at the University of Ljubljana, Faculty of Maritime Studies and Transport. He conducts researches predominately in the <sup>fi</sup>eld of ballast water management (ballast water sampling, risk assessment and management, decision support systems), and oil and HNS pollution from vessels and in ports (contingency planning, illicit spills monitoring, port sustainable development). From 2002 to 2009 he was head or member of the Slovenian Delegation in the International

Maritime Organisation (IMO) Marine Environment Protection Committee (MEPC), Bulk Liquids and Gasses (BLG) Sub Committee and the Ballast Water Working Group (BWWG), and he was head of Slovenian delegation at the Diplomatic Conference in 2004 in London when the BWM Convention was adopted. He is contributing to the development of ballast water management approaches in the Mediterranean, North and Baltic Seas. He is also an invited expert for ballast water management issues at the European Maritime Safety Agency (EMSA).

![](/api/attachments/QCEEU2EK/fulltext/images/9c4585aaddb65dad5fd4dbd63947ef6b0bc106c0918d6653de117b1d9ca1c5ae.jpg)

Marko Perkovič attended maritime high school and become a nautical technician. He continued his education aboard ship and at the Faculty of Maritime and Transport, University of Ljubljana, where he completed three undergraduate programs, in nautical science and marine engineering, and transport technology. At the same time, working aboard merchant ships, he became both a deck of-<sup>fi</sup>cer and marine engineer. Offered the position of young researcher at the Faculty for Maritime Studies in 1998, he continued his academic career as an assistant and received his Master's degree. Marko quickly became a senior lecturer and a department head as well as a senate member. Today his main occupation as a lecturer is teaching ships theory, directing ships' engines practices and cargo handling training. Understanding the necessity of modern approaches in education, he has a vital role in introducing simulators to Faculty. A strong concern in environmental issues lately led him to participate in projects researching ballast water, oil spill problematic and navigational risk assessment. He is also a member of European Commission Group of Experts on Satellite Monitoring of sea-based Oil Pollution.

![](/api/attachments/QCEEU2EK/fulltext/images/d730ab538d9576cf7f80a535299ab16702816ca867585dd933465eb328f64954.jpg)

Valter Suban is lecturer at the University of Ljubljana, Faculty of Maritime Studies and Transport. He has BSc in Nautical Science (1986), BSc in Transportation Technology (1996), and MSc in Transportation Technology (2005). His Master thesis was “Determination model for quantifying past discharged ballast”. He has a master mariner certi<sup>fi</sup>cate of competency, and served on 17 different ships of different size and types on positions from cadet to master to stay in continuous touch with ships; works part time as a surveyor and a magnetic compass adjuster. He is lecturing different subjects related to cargo handling, basic seamanship, stability and sea communications, and he is an instructor on short courses related to GMDSS. safety and security. His main

<sup>fi</sup>elds of research are: cargo handling, ballast water issues, maritime communications and maritime safety. He was involved in more than 10 national and international projects.

![](/api/attachments/QCEEU2EK/fulltext/images/667ca9e40c31a399a190aec906c8995fcacab21b3ea371c96648d065c87e5f59.jpg)

Stephan Gollasch was involved in the <sup>fi</sup>rst European ship sampling program on ballast water, tank sediments and ship hull fouling (1992–1996). His PhD is world-wide the <sup>fi</sup>rst thesis based on ballast water sampling. Due to the international aspect of biological invasions he became a member of several working groups, e.g. International Council for the Exploration of the Sea (ICES); International Maritime Organization (IMO), and the Baltic Marine Biologists (BMB). In addition to laboratory and desk studies he spent more than 250 days at sea during several biological sampling surveys and sampled ballast water of more than 200 vessels. As an independent consultant he is today involved in projects related to biological invasions (e.g. ballast water treatment,

ship sampling, risk assessment). He was also involved in the development of ballast water management scenarios for the European Atlantic coast, North, Baltic, Caspian and Mediterranean Seas. Ongoing contracts include onboard ef<sup>fi</sup>cacy tests of ballast water treatment systems according to IMO guidelines and also the evaluation of active substances used to treat ballast water as a member of the GESAMP Ballast Water Working Group.
