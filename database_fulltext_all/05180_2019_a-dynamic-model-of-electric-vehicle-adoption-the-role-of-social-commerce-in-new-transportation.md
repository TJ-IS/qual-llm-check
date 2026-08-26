---
otero_id: 5180
otero_key: "DZWBSWCY"
title: "A dynamic model of electric vehicle adoption: The role of social commerce in new transportation"
authors: "Bo Feng; Qiwen Ye; Brian J. Collins"
year: "2019"
journal: "Information & Management"
doi: "10.1016/j.im.2018.05.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A dynamic model of electric vehicle adoption: The role of social commerce in new transportation

Bo Feng<sup>a,b</sup>, Qiwen Ye<sup>a,⁎</sup>, Brian J. Collins<sup>c</sup>

<sup>a</sup> School of Business Administration, South China University of Technology, #381 Wushan Road, Guangzhou, 510640, China

<sup>b</sup> Business School, Soochow University, #50 East Ring Road, Suzhou, 215021, China

<sup>c</sup> Department of Management, College of Business, University of Southern Mississippi, Box #5077, Hattiesburg, MS 39406, USA

## A R T I C L E I N F O

Keywords: System dynamics (SD) Electric vehicle Adoption Fuzzy logic Social commerce

## A B S T R A C T

This research explores the adoption of electric vehicles (EVs) as a substitute for internal combustion engine vehicles (ICVs) and examines its emergence as a mobile intelligent terminal of social commerce. We present a system dynamics (SD) model incorporating fuzzy logic to simulate the adoption process. The results suggest that consumers’ vague perceptions and the dispersion of pilot EV projects have caused EV adoption to be delayed; nevertheless, the introduction of social commerce to EVs can help relieve this problem and promote EV adoption. However, the timing of introducing social commerce is critical for enhancing its positive e<sup>f</sup>ect on EV adoption.

## 1. Introduction

Electric vehicles (EVs) increasingly function as mobile intelligent terminals for social commerce. Baidu, Alibaba, and Tencent (BAT), three Chinese Internet giants, have invested more than \$200 million to develop an ecosystem of “Internet-connected cars”. Tencent and Guangzhou Automobile Group Co., Ltd. joined forces to introduce the EV iSPACE concept, which features the “AI in car” system that integrates new technologies (e.g., mobile networks, GIS, arti<sup>fi</sup>cial intelligence, and social media). Equipped with state-of-the-art technologies and a growing vehicle network, EVs have the potential to be a rich source of user-generated input, real-time information, location-based data, and contextual information, all of which are features of social commerce (e.g., [1,36]). Social commerce plays a key role in EV adoption. First, incorporating social commerce into EV endows a new function to conventional vehicles and then improves the perceived usefulness in EVs adoption. Second, it is very attractive to the young people and increase the social identi<sup>fi</sup>cation among the drivers who pursue the high-tech and fashion product. Last, social commerce enhances the network externality through a two-sided market and may lead to a “massive adoption” of EVs.

Although the future holds promise for EVs as a social commerce hub, that is, an integrated and moving carrier of transportation, shop ping, o<sup>fi</sup>cial business, and entertainment [2], currently, EVs are primarily a transportation alternative to internal combustion engine vehicles (ICVs). As political winds dictate, many governments have heavily subsidized e<sup>f</sup>orts to expand EV acceptance and build the necessary infrastructure [3]. In response, individual vehicle manufacturers are working to obtain a “<sup>fi</sup>rst mover” position [4] in what they view as a potentially expanding market. However, is this the right time to emphasize the Internet usage in EVs and is this a feature that customers highly value? Speci<sup>fi</sup>cally, will positioning EVs as social commerce terminals accelerate their adoption?

The extant research on EV adoption mainly focuses on empirical analyses to identify in<sup>fl</sup>uencing factors such as cost, contextual, and technical factors (e.g., [5–7]. In these studies, economic utility [8] is emphasized, whereas its potential for social utility [8] (i.e., an emerging hub of commerce) is seldom mentioned. In isolation, these factors are salient, but their interactions may more fully inform the dynamic process of EV adoption. The higher costs that are associated with EVs tend to dampen demand [9]; however, consumers may be willing to absorb higher purchase costs in exchange for increased charging convenience [10–13]. Furthermore, the cost to develop the embryonic network and solve the inevitable technical di<sup>fi</sup>culties may hinder EVs acceptance [14]. In addition, some potential customers will remain skeptical until the network reaches maturity [15]. These issues need to be more fully understood, and they prompt the need for additional research.

In this paper, we capture the process of adopting EVs, and we attempt to interpret how consumers perceive the economic utility and social utility of EVs. By incorporating data from Chinese consumers, we model the reciprocal (i.e., circular) and temporal (i.e., time variant) relations that in<sup>fl</sup>uence EV adoption. Consistent with the extant research [16], we model the bene<sup>fi</sup>ts that consumers can receive by substituting EVs for ICVs. EVs will be adopted only when a cost–bene<sup>fi</sup>t analysis favors them [17]. Moreover, we suggest that consumers’ decision-making processes are neither linear nor precise because they are subject to individual preferences and personal biases. Previous linear, elemental views of cognitive processing cannot re<sup>fl</sup>ect the complex comparative evaluations in the real world, which more closely approximate “fuzzy logic” [18]. Therefore, we apply fuzzy logic to replicate the comparative processes that consumers use to decide among alternatives.

This paper makes the following contributions to the Information Systems literature. First, this study explicates the complex process of adopting the new technology that speci<sup>fi</sup>cally relates to EVs and social commerce. Second, we use system dynamics (SD) modeling to evaluate how feedback and interactions in<sup>fl</sup>uence EV adoption. Third, we in corporate fuzzy logic to replicate the more realistic cognitive processes of individuals when they make comparisons. Finally, we examine an array of potential in<sup>fl</sup>uences through a “what if” analysis to provide constructive implications for practitioners.

The remainder of this paper is structured as follows. In Section 2, we review the literature regarding EVs and social commerce. We present an SD model of EV adoption and the related casual analyses in Section 3. In Section 4, fuzzy logic is applied to characterize consumers’ complex cognitive processes in the SD model, and the results of the simulation are shown in Section 5. The <sup>fi</sup>nal section provides conclusions from the simulation results and some important practical implications.

## 2. Literature review

## 2.1. EV adoption

EV adoption has attracted research attention from scholars across the academic spectrum such as transportation (e.g., [19], management (e.g., [20], energy (e.g., [21], and environmental studies (e.g., [22]. Most of this literature (see Table 1) empirically examines in<sup>fl</sup>uences such as cost, context, and technology (e.g., [23].

As an emerging technology, the price of an EV is signi<sup>fi</sup>cantly higher than that of an ICV, which creates an obstacle to the broad adoption of EVs. More than 50% of the people surveyed in [19] cited price as the major shortcoming of EVs. Krause et al. [24] found signi<sup>fi</sup>cantly higher adoption rates of EVs when the prices of EVs and ICVs were comparable. The cost to charge EVs is another consideration, particularly in relation to the cost to fuel ICVs (e.g., [25]. Substantial empirical evi dence indicates that reduced charging costs has a positive e<sup>f</sup>ect on EV adoption (e.g., [7,19]). As the price of gasoline increases, the operating cost of EVs becomes more competitive. With the signi<sup>fi</sup>cant e<sup>f</sup>ects of these cost factors on EV adoption, there is a research stream that compares the life cycle costs of an ICV and EV [26,27] because it is believed that more accurate comparisons will help accelerate the adoption process [6,28]. However, additional research that explores dynamic and complex cost analyses is needed. What is the in<sup>fl</sup>uence of the charging cost in relation to the unpredictable <sup>fl</sup>uctuations in the price of gasoline? What is the long-term behavior pattern of EV adop tion considering the cost reduction that is caused by economies of scale? These discussions have not been addressed in prior research.

Table 1  
Studies on in<sup>fl</sup>uencing factors of EV adoption.

<table><tr><td>Factor</td><td>Example</td><td>Scholarship</td></tr><tr><td rowspan="3">Cost</td><td>Purchase price</td><td>[5,19,21]</td></tr><tr><td>Charging fee</td><td>[7,63]</td></tr><tr><td>Maintenance expense</td><td>[29,64]</td></tr><tr><td rowspan="2">Context</td><td>Charging infrastructure</td><td>[19,29,30]</td></tr><tr><td>Policy incentives</td><td>[3,33,32]</td></tr><tr><td rowspan="3">Technology</td><td>Driving range</td><td>[65–67]</td></tr><tr><td>Safety</td><td>[7,68]</td></tr><tr><td>Performance</td><td>[64,66]</td></tr></table>

Infrastructure convenience, a key contextual factor, is positively related to purchase intention [19,29,30] because it impacts consumers driving patterns [31]. Increased infrastructure convenience may improve the driving experience and further increase consumers’ cost tolerance [13]. However, range anxiety is a legitimate concern, and it is likely that only access to a broader infrastructure system will alleviate these fears. Public policy is another contextual factor that in<sup>fl</sup>uences EV adoption [23], where incentives (e.g., monetary subsidies and emission taxes) can alter the decision-making calculus [32]. Bakker & Trip [33] assessed the feasibility of nonmonetary incentives such as special lane access and found that infrastructure factors were salient. All these policy incentives seek to increase EV adoption by reducing costs or improving convenience. However, previous research has not studied how these incentives a<sup>f</sup>ect EV adoption by varying the related factors from a dynamic perspective.

ICVs are an accepted part of modern society, whereas EVs require consumers to adapt to new transportation patterns. Consumers have had perceived range anxiety and safety as potential issues since the introduction of EVs [21,22]. However, EV technology is maturing, and EV quality has been improving. Currently, certain EV models have driving ranges and safety records that are comparable to those of ICVs. As these functional issues have been resolved, the emphasis is moving from performance to cost factors.

Thus, the previous literature has examined the potential drawback to the adoption of new modes of transportation. However, as EV technology and its charging infrastructure make EVs more comparable to ICVs, more complex analyses are needed. Although some researchers have compared the costs of using EVs and ICVs, their results have been unable to reveal their dynamic substitution on the adoption process. In addition, the SD modeling approach more realistically predicts the future buying behaviors of consumers because survey data are not wellsuited to this dynamic environment. In this paper, we attempt to bridge these gaps by developing an SD model to explore how the in<sup>fl</sup>uencing factors on EV adoption dynamically interact.

## 2.2. Social commerce adoption

Social commerce is an emerging business mode in which buyers and sellers transact through online social networks [34,35]. Social com merce has the following distinguishing features.

(1) User-generated content is the primary information source for consumers [2]. Content (e.g., product reviews and peer recommendations) informs consumer research because social networks enable widespread word-of-month feedback [36].

(2) Mobile intelligent terminal is increasingly important for social commerce [78]. With the mobile Internet, mobile intelligent terminals (e.g., smart phones) perform a better job than traditional methods in providing location-based services, real-time information publishing, and intelligent push, which ensure the diversity and timeliness of information for consumers.

(3) Social relationships play a critical role in consumer purchasing decisions [37]. Strong social network ties increase the trust and credibility of feedback [2], which consumers <sup>fi</sup>nd persuasive.

Thus, there are three main streams of the scholarly research on social commerce adoption. One stream closely follows consumers’ virtual experience (e.g., [38,14]. Unlike e-commerce, social commerce emphasizes social sharing and networking rather than traditional shopping behaviors [2]. Table 2 summarizes the aspects of the social commerce experience. Drawing from previous theories on social networks and psychology [38], indicated that support—social, informational, and emotional—is important in measuring the consumer’s social commerce experience. Zhang et al. [14] noted that social support, social presence, and <sup>fl</sup>ow are all positively related to consumers’ adoption of social commerce. Increased social support facilitates presence and builds a warm and harmonious social environment that leads to higher satisfaction (<sup>fl</sup>ow).

Table 2  
Constructs of consumers’ virtual experience in social commerce.

<table><tr><td>Construct</td><td>Definition</td><td>Scholarship</td></tr><tr><td>Social support</td><td>Degree of being supported in the social environment</td><td>[38,14]</td></tr><tr><td>Social presence</td><td>Degree to which consumers perceived the social environment to be sociable, warm, and intimate</td><td>[69,70]</td></tr><tr><td>Flow</td><td>Perceived satisfaction of curiosity, interest, and control in social interactions</td><td>[69,70,14]</td></tr><tr><td>Information support</td><td>Perceived support of receiving information aids from friends in social commerce</td><td>[71,38]</td></tr><tr><td>Emotional support</td><td>Perceived support of receiving emotional concerns from friends in social commerce</td><td>[71,38]</td></tr></table>

Technology is another focus of social commerce research. Some scholars consider social commerce to be a new technology, and they apply the typical technology acceptance model (TAM: [39]). Consistent with the previous TAM literature, the perceived usefulness of social commerce sites has a positive e<sup>f</sup>ect on intent adoption. However, perceived ease of use (e.g., [40,41]) is replaced with perceived enjoy ment and has a positive e<sup>f</sup>ect on social commerce adoption. Moreover, system security, information quality, and technical reliability also contribute to intent adoption by enhancing the perceived trustworthi ness of the system [37,40].

The extant research presents a clear view of the in<sup>fl</sup>uencing factors of social commerce adoption [42,38,43]. A pleasant experience and technical support are critical to earn the trust of consumers. Undoubtedly, social relations are also important to adoption, but this factor is di<sup>fi</sup>cult to quantify and is uncontrollable for managers in the EV industry. Therefore, only consumers’ virtual experience and the technical features of social commerce are considered in this study.

## 3. System dynamics model of EV adoption

## 3.1. System dynamics modeling

EV adoption is a dynamic and complex process with feedback and causal loops. In this paper, we adopt SD modeling to capture the process of EV adoption.

First, our SD model is developed based on the related theories and internal mechanisms of EV adoption. The application of reinforced and balancing feedback loops of SD models helps researchers to better understand the system structures and circular causality between components [44,45]. This feature renders SD modeling a suitable methodology for us to better describe the complex interactions among the mentioned in<sup>fl</sup>uencing factors in EV adoption. Second, in SD modeling, stocks and <sup>fl</sup>ows are applied to record the accumulation and transformation of the critical components, which provide us a clearer view of the adoption behaviors of EV users [45,46]. In our study, the number of di<sup>f</sup>erent vehicle owners is central to observe the adoption process. Stocks and <sup>fl</sup>ows enable us to capture the changes among these pivotal variables through the dynamic process and o<sup>f</sup>er us the essential information for decision-making. Third, SD modeling is an appropriate methodology to model EV adoption with delayed causality and is e<sup>fi</sup>- cient at capturing the delay e<sup>f</sup>ect of structures on the system behaviors [45]. By exploiting this feature, we can determine the delay e<sup>f</sup>ect of infrastructure construction and the network externality on EV price and social commerce. Finally, SD modeling furnishes us with a “what if” analysis of the simulation [46], which assists us in exploring how the adoption behavior of EV users responds to various in<sup>fl</sup>uencing factors.

## 3.2. Model description

Considering the multiple functions of an EV as both a form of transportation and a mobile intelligent terminal, two utilities are included in our model, as shown as Fig. 1.

## 3.2.1. Economic utility

In our model, we assume that the economic utility of EVs is based on comparisons with ICVs in the dimensions of cost, infrastructure con venience, and vehicle technology because of the nature of consumers to make comparisons between alternatives during the purchase decisionmaking process [47].

First, the price-perceived utility theory [48,49] is applied to illustrate the process of cost comparison by using the costs of ICVs as the “reference price” [50,51] and the cost di<sup>f</sup>erence between ICVs and EVs as the consumers’ perceived economic utility of EVs [49]. The costs in our model comprise (1) the purchase cost, which includes the price of the vehicle and the purchase tax (which is proportional to the vehicle price), and (2) the operation cost, where only the cost of energy consumption is included because the maintenance cost is unpredictable and depends on the use. For the use of an ICV with a displacement of 1.4–1.6 L and BYD E6 as examples, their estimated charging costs are presented in Table 3, which shows a considerable savings of more than 7000 RMB per year.

The EV infrastructure brings convenience to vehicle users. To in crease the infrastructure convenience of EVs, the UK government requires all gasoline stations and motorway service centers to build charging stations. Major oil companies such as Shell and BP are planning to install EV charging stations at their gasoline stations to catch up with the vehicle revolution. Potential consumers of EVs compare the convenience of the infrastructure by comparing the number/coverage of EV charging stations to the number/coverage of ICV gas stations. In our SD model, the number of existing gasoline stations is used as a reference, and the time di<sup>f</sup>erence between ICV re<sup>fi</sup>lling and EV recharging is also considered (the detailed calculation is presented in section 4.1).

![](/api/attachments/DZWBSWCY/fulltext/images/d33996be4cf15a1ddeed975d5963a6591a15d36b265f86818e619c1a0f7b86b6.jpg)  
Fig. 1. Research framework.

Table 3  
Estimated charging costs of ICV and EV.

<table><tr><td>Vehicle</td><td>Energy consumption per 100 km</td><td>Price of energy</td><td>Travel distance per year</td><td>Charging cost per year</td></tr><tr><td>ICV</td><td>8 L (gasoline) $^{a}$ </td><td>7.79 RMB/L $^{b}$ </td><td>15,000  $km^{c}$ </td><td>9348 RMB</td></tr><tr><td>EV</td><td>19.5 kWh (electricity) $^{d}$ </td><td>0.73 RMB/  $kWh^{e}$ </td><td>15,000 km</td><td>2,135.25 RMB</td></tr></table>

<sup>a</sup> Average energy consumption of ten popular ICVs with a displacement of 1.4–1.6 L; data are obtained from http://auto.163.com/.  
<sup>b</sup> 7.79 Is the <sup>fi</sup>nal price of 93# of gasoline in 2013 in China.  
<sup>c</sup> The average driving distance is from the experimental data in the research of Feng et al. [72].  
<sup>d</sup> Data are from the o<sup>fi</sup>cial website of BYD (http://www.byd.com/hk/e6. html).  
<sup>e</sup> The second degree of electricity price in Guangzhou, China.

Regarding technology, EVs are becoming comparable to ICVs in terms of safety and vehicle performance. There are various regulations on EV safety that have been issued by di<sup>f</sup>erent countries; for example, the EU uses Economic Commission of Europe (ECE) regulations, the US uses Federal Motor Vehicle Safety Standards (FMVSS), and China adopts GB/T (National Recommendatory Standards) 18384. These regulations cover the requirements from the components to the entire electric drivetrain, which is formed after hundreds of safety tests of charging, collisions, etc. EVs can access the market only if they have passed all the tests. For vehicle performance, Tesla Model S is the representative of advanced EV technology, and the equipped features include over a 400-km driving range, a 2.7-s acceleration time from 0 to 100 km/h, and autopilot capabilities. However, it is undeniable that EVs are more expensive than ICVs yet have only comparable performance. Therefore, we show the e<sup>f</sup>ect of vehicle technology on decreasing the production cost of EVs in our model by using the “Learning Curve” [52].

## 3.2.2. Social utility

In the ecosystem of “Internet-connected cars,” the EV network is becoming the next social network, which is accompanied by various social activities and conceals a signi<sup>fi</sup>cant business opportunity. To provide consumers with good virtual experiences (such as social support, social presence, and emotional and information support) in EV social commerce, innovations on commercial activities in the EV network are indispensable [35]. We employed the construct of “commer cial activity innovations to re<sup>fl</sup>ect the integration between social commerce and the EV network, as well as the virtual experiences that it provides to consumers [38,14]. In our model, the four life cycle stages of the business model that was proposed by Wirtz [53] are employed to describe the level of commercial innovation and network externality that are involved.

An EV, as an intelligent mobile terminal, increases the high demand of information and communication technology (ICT). The advanced Internet of Things contributes to real-time data collection, information sharing, and services, which are provided in EV social commerce. These types of technologies and the related software should be user friendly, which improves the perceived ease of use for consumers. The maturity of the Internet of Things in the Gartner Hype Cycle [54] is applied to measure the level of ICT in EV social commerce.

## 3.3. Interactions and casual loops analysis

As mentioned, many interactions exist among the variables that are used to measure economic utility and social utility. Concerning economic utility, infrastructure convenience, as part of the perceived ease of use, may lead to a higher tolerance of costs by increasing consumers’ satisfaction [11,13]. Regarding social utility, ICT is the foundation of social interactions and commercial activity innovation [35]. Moreover, social utility also interacts with economic utility from two aspects: (1) commercial activity innovation may facilitate the infrastructure convenience of EVs by exploiting real-time data sharing on location and at the charging stations and (2) advanced ICT for social commerce increases the cost of technology and slows the reduction of EV production costs [14], which is measured by the “Learning Curve” [52]. With these interactions, we simulate the adoption process with both ICV and EV owners. The di<sup>f</sup>erent EV adoption rates will decide how many <sup>fi</sup>rsttime vehicle buyers and vehicle repurchase buyers will become EV owners per year.

![](/api/attachments/DZWBSWCY/fulltext/images/e6a8b281dfc8f2bb4d2f9c290d31b1fd18c4204c53d67de2f5c26f7455554474.jpg)  
Fig. 2. Full causal loop diagram.

Fig. 2 presents the causal loops among the critical variables in our model. The variables that have a positive/negative e<sup>f</sup>ect on the variables indicated by an arrow are noted by ± . The reinforced loop is the feedback loop with a variable that is ultimately changing in the same direction as its initial variation. Similarly, if a variable changes to the opposite direction in the feedback loop, we identify this loop as a balancing loop.

## 3.3.1. Reinforced loop (Learning Curve+)

This loop captures the positive e<sup>f</sup>ect of the “Learning Curve” regarding the number of EV owners. When there are more EV owners, the cumulative production of EVs is greater, which leads to the lower price of EVs. With the decreasing cost between EVs and ICVs, vehicle buyers are more willing to adopt EVs, which ultimately increases the number of EV owners.

## 3.3.2. Reinforced loop (NE+)

This loop describes the e<sup>f</sup>ects of network externality on the EV adoption process. When the EV network reaches a certain scale, there is a positive externality e<sup>f</sup>ect on commercial activity innovation, which accelerates EV adoption directly. Moreover, network externality also enhances the loop by reinforcing the positive e<sup>f</sup>ect of infrastructure convenience. However, a small network size may in<sup>fl</sup>uence the extension of commercial activities and disappoint the early adopters, which slows the growth of EV adoption [15].

## 3.4. Formal model with stocks and flows

Fig. 3 depicts the formal model, which is extended from the research framework and causal loops.

![](/api/attachments/DZWBSWCY/fulltext/images/7fe0e863ddade45b5785c63f602119924c3192e0d13dcd60872225000a6965a8.jpg)

(a) Economic Utility  
![](/api/attachments/DZWBSWCY/fulltext/images/c330a0c4017c0ddbc8429d4caead009d3f543be15b5704bd69363e8c29885fb2.jpg)  
(b) Social Utility

![](/api/attachments/DZWBSWCY/fulltext/images/f122ec59c210b3ec27982de0f5db6394470ad971127e49082e980a9a541a0cea.jpg)  
(c) Adoption Process of EV  
Fig. 3. Formal model with stocks and <sup>fl</sup>ows.

In Fig. 3(c), the box of “First Time Vehicle Buyers” refers to vehicle buyers who have never owned a vehicle before. The <sup>fl</sup>ow that goes to this box is “New Buyers per year,” which represents the people with the ability and willingness to purchase their <sup>fi</sup>rst vehicles. The <sup>fl</sup>ows from “First Time Vehicle Buyers” are “Buying ICVs” and “Buying EVs,” which indicate the people who purchase ICVs or EVs as their <sup>fi</sup>rst vehicles. The temporal accumulation of “First-Time Vehicle Buyers,” FB(t), is calcu lated using Eq. (1), where FB(0) is 5.2863e + 06, which is 6% (the <sup>fi</sup>xed growth rate) of the total number of vehicles owners in 2013.

$$
F B (t) = \int_ {0} ^ {t} \begin{array}{l} \text { New   Buyers   per   year } (t) d t - \text { Buying   ICVs } (t) d t - \\ \text { Buying   EVs } (t) d t + F B (0) \end{array}\tag{1}
$$

The box “Vehicle Repurchase Buyers” is the number of buyers who need to change their vehicles after the average lifetime of the vehicle. They come from the <sup>fl</sup>ows of “Change Vehicles 1” and “Change Vehicles $2 , \ "$ the buyers who owned ICVs and EVs before but need to change vehicles now. The <sup>fl</sup>ows that come from “Vehicle Repurchase Buyers” are “Change to $\scriptstyle { \mathrm { I C V s } } ^ { \prime \prime }$ and “Change to $\mathrm { E V } s , { } ^ { \dag }$ which are buyers who change their vehicles to ICVs and EVs. The temporal accumulation of “Vehicle Repurchase Buyers,” VRB(t), is calculated using Eq. (2), where $V R B ( 0 ) = 0 .$

$$
V R B (t) = \int_ {0} ^ {t} \begin{array}{l l} \text { Change } & \text { Vehicles } 1 (t) d t + \text { Change } \\ \text { Change } & \text { to } I C V s (t) d t - \text { Change } \text { to } E V s (t) d t + V R B (0) \end{array}\tag{2}
$$

The box of “ICV Owners” is the number of ICV owners. It is an accumulated stock that includes the <sup>fl</sup>ows of “Buying $\mathrm { I C V } s , ^ { \prime \prime } { } ^ { \cdots }$ Change to $\mathrm { I C V } { \mathsfit { s } } , \mathrm { \Delta } ^ { \mathrm { \Delta } \mathrm { \omega } }$ and “Change Vehicles 1”. “ICV Owners,” IO(t), is calculated using Eq. (3), where $I O ( 0 ) = 8 . 8 1 0 5 \mathrm { e } + 0 7 , ^ { 1 }$ which is the number of small private ICV owners in 2013 in China.

$$
I O (t) = \int_ {0} ^ {t} \begin{array}{l} B u y i n g I C V s (t) d t + C h a n g e t o I C V s (t) d t - \\ C h a n g e V e h i c l e s 1 (t) d t + I O (0) \end{array}\tag{3}
$$

Similarly, the box of “EV Owners” is the number of EV owners and can be calculated using Eq. (4), where $E O ( 0 ) = 3 8 , 5 9 2 , ^ { 2 }$ which is the number of private EVs in 2013 in China.

$$
E O (t) = \int_ {0} ^ {t} \begin{array}{l} B u y i n g E V s (t) d t + C h a n g e t o E V s (t) d t - \\ C h a n g e V e h i c l e s 2 (t) d t + E O (0) \end{array}\tag{4}
$$

The stock of “The Number of Infrastructures” and the <sup>fl</sup>ow of “Infrastructures per year” represent the total number of available charging infrastructures and the number of new infrastructures per year, respectively. “The Number of Infrastructures,” I(t), is presented in $\mathbf { E q . \ ( 5 ) b } ,$ , where $I ( 0 ) = 2 7 , 7 0 8 , ^ { 3 }$ which is the number of charging in frastructures in 2013 in China.

$$
I (t) = \int_ {0} ^ {t} I n f r a s t r u c t u r e s p e r y e a r (t) d t + I (0)\tag{5}
$$

The variables that describe the components of cost, infrastructure convenience, and vehicle technology are shown in Appendix A.

## 4. Consumer’s comparison process with fuzzy logic

The previous literature has used rigorous quantitative models to determine the life cycle costs of ICVs and EVs (e.g., [26]). In a realworld case, however, consumers may compare the alternatives from various dimensions with varying degrees of perception [55]. Thus, we describe the comparison process of consumers as a vague perception by using fuzzy logic. Fuzzy logic was introduced by Lot<sup>fi</sup> Zadeh [56] and is commonly employed in the area of social science [55]. In the case of EV adoption, for example, consumers may perceive di<sup>f</sup>erent degrees of “convenience” with a <sup>fi</sup>xed number of charging infrastructures. Fuzzy logic permits the memberships of the variables in the interval of [0,1] by transforming the conventional binary variables into continuous variables [55]. This feature makes it e<sup>fi</sup>cient to characterize consumers’ vague perceptions with varying memberships. Furthermore, consumers commonly express their degrees of perception with lin guistic terms such as “very high” or “very low” rather than an exact value. Fuzzy logic can match the linguistic variables to a certain range of membership degrees and can compute the quantitative results that are needed in the SD model by using the logic rules [18].

In our model, we use di<sup>f</sup>erent fuzzy logic rules to measure economic utility and social utility. Because economic utility is the most important factor for consumers to purchase vehicles and social utility is an added value of EVs, we use direct fuzzy logic to measure economic utility. We assume that social utility may amplify the e<sup>f</sup>ect of economic utility in EV adoption. Therefore, we measure social utility by using indirect fuzzy logic with the interval of [0,1], where 0 means no commercial activity innovation and 1 means extreme development of commercial activity innovation.

## 4.1. Description of consumers’ fuzzy logic

Customers’ subjective perceptions on cost, infrastructure convenience, and vehicle technology (measured by added purchase cost) are expressed in linguistic terms to obtain consumers’ fuzzy utilities.

We use seven-scale linguistic terms to describe the fuzzy utilities in our model. Linguistic term set U represents the di<sup>f</sup>erent scales of cost di<sup>f</sup>erence that correspond to speci<sup>fi</sup>c crisp values, V represents the di<sup>f</sup>erent scales of consumers’ perception on infrastructure convenience with di<sup>f</sup>erent numbers of charging infrastuctures, and W represents the scale of perceived economic utility. Tables 4–6 list all the scales and semantics of sets $U , V ,$ and W.

## 4.2. Inference process in fuzzy logic

In this process, IF…THEN rules are presented to depict the perceived economic utility. As shown in section 4.1, there are seven scales of the perceived economic utility of EVs $( w _ { k } , k = 0 , 1 , 2 , 3 , 4 , 5 , 6 ) ,$ which could be inferred from 49 rules combined with seven scales of cost di<sup>f</sup>erence $( u _ { i } , i = 0 , 1 , 2 , 3 , 4 , 5 , 6 )$ and seven scales of infrastructure convenience (v , j = 0, 1, 2, 3, 4, 5, 6). All the rules are presented in Eq. (6).

$$
R (u _ {i}, v _ {j}) = \left\{ \begin{array}{c c} w _ {0}, & i \leq 3 - j \\ w _ {1}, & 3 - j <   i \leq 6 - j \\ w _ {M i n (i + j - 5, 0)}, & i > 6 - j \end{array} \right.\tag{6).}
$$

According to Larsen’s inference method [57],

$$
w (z) = u (x) v (y),\tag{7}
$$

where x, y, and z are the crisp values of the cost di<sup>f</sup>erence, infrastructure convenience, and perceived economic utility, respectively.

To advance the calculation, defuzzi<sup>fi</sup>cation is conducted to transform the membership degree to the crisp value of the perceived economic utility of EVs. In this paper, we adopt the defuzzi<sup>fi</sup>cation method that was proposed by [58], which can better restore the crisp value and distinguish the triangle fuzzy values with the same means. The equation is as follows.

$$
C _ {i} ^ {d e f} = L + \frac {\varDelta [ (f _ {i} ^ {M} - L) (\varDelta + f _ {i} ^ {R} - f _ {i} ^ {M}) ^ {2} (R - f _ {i} ^ {L}) + (f _ {i} ^ {R} - L) ^ {2} (\varDelta + f _ {i} ^ {M} - f _ {i} ^ {L}) ^ {2} ]}{(\varDelta + f _ {i} ^ {M} - f _ {i} ^ {L}) (\varDelta + f _ {i} ^ {R} - f _ {i} ^ {M}) ^ {2} (R - f _ {i} ^ {L}) + (f _ {i} ^ {R} - L) (\varDelta + f _ {i} ^ {M} - f _ {i} ^ {L}) ^ {2} (\varDelta + f _ {i} ^ {R} - f _ {i} ^ {M})}\tag{8),}
$$

where $C ^ { d e f } \mathrm { i } s$ the crisp value that is transformed from the triangular fuzzy number, $\hat { F _ { i } } = ( f _ { i } ^ { L } , f _ { i } ^ { M } , f _ { i } ^ { R } ) , \quad i = 1 , \quad 2 ; \quad L = \operatorname * { m i n } \{ f _ { 1 } ^ { L } , f _ { 2 } ^ { L } \} .$ $R = \operatorname* { m a x } \{ f _ { 1 } ^ { R } , f _ { 2 } ^ { R } \}$ , and $\Delta = R - L .$

Linguistic scales of set V.  
Table 5  
Table 4  
Linguistic scales of set U.

<table><tr><td>Linguistic variable and semantic</td><td>Triangular fuzzy numbera</td><td>Figure of membership function</td></tr><tr><td> $u_0$ = definitely low (DL)</td><td> $(-\infty,-1.5,-1)$ </td><td rowspan="7"></td></tr><tr><td> $u_1$ = very low (VL)</td><td> $(-1.5,-1,-0.5)$ </td></tr><tr><td> $u_2$ = low (L)</td><td> $(-1,-0.5,0)$ </td></tr><tr><td> $u_3$ = medium (M)</td><td> $(-0.5,0,0.5)$ </td></tr><tr><td> $u_4$ = high (H)</td><td> $(0,0.5,1)$ </td></tr><tr><td> $u_5$ = very high (VH)</td><td> $(0.5,1,1.5)$ </td></tr><tr><td> $u_6$ = definitely high (DH)</td><td> $(1,1.5,\infty)$ </td></tr></table>

<sup>a</sup>The average cost of using an ICV per year is 15,000 RMB in our model, and we assume that if the cost of using an EV is 15,000 RMB or higher, there is de<sup>fi</sup>nitely a low cost di<sup>f</sup>erence for consumers; otherwise, there is a de<sup>fi</sup>nitely a high cost di<sup>f</sup>erence if the cost of an EV is 15,000 RMB or lower. For the convenience of calculation, we set the intervals of the membership function as 0.5 (5000 RMB/10,000 RMB). <sup>b</sup>x: the crisp value of the cost di<sup>f</sup>erence/10,000 RMB.

<table><tr><td>Linguistic variable and semantic</td><td>Triangular fuzzy numbera</td><td>Figure of membership function</td></tr><tr><td> $v_0$ = definitely low (DL)</td><td>(0,0,0.2)</td><td rowspan="7">v(y)1v0v1v2v3v4v5v6y b</td></tr><tr><td> $v_1$ = very low (VL)</td><td>(0,0.2,0.4)</td></tr><tr><td> $v_2$ = low (L)</td><td>(0.2,0.4,0.6)</td></tr><tr><td> $v_3$ = medium (M)</td><td>(0.4,0.6,0.8)</td></tr><tr><td> $v_4$ = high (H)</td><td>(0.6,0.8,1)</td></tr><tr><td> $v_5$ = very high (VH)</td><td>(0.8,1,1.2)</td></tr><tr><td> $v_6$ = definitely high (DH)</td><td>(1,1.2,∞)</td></tr></table>

<sup>a</sup>For the convenience of calculation, we assume that the perception of consumers on infrastructure convenience is de<sup>fi</sup>nitely high when the coverage of the charging infrastructure is 1.2 times the coverage of refueling equipment in gasoline stations. <sup>b</sup>y: the crisp value of infrastructure convenience.

<table><tr><td>Linguistic variable and semantic</td><td>Triangular fuzzy number</td><td>Figure of membership function</td></tr><tr><td> $w_0$ = definitely low (DL)</td><td>(0,0,1/6)</td><td rowspan="7"></td></tr><tr><td> $w_1$ = very low (VL)</td><td>(0,1/6,1/3)</td></tr><tr><td> $w_2$ = low (L)</td><td>(1/6,1/3,1/2)</td></tr><tr><td> $w_3$ = medium (M)</td><td>(1/3,1/2,2/3)</td></tr><tr><td> $w_4$ = high (H)</td><td>(1/2,2/3,5/6)</td></tr><tr><td> $w_5$ = very high (VH)</td><td>(2/3,5/6,1)</td></tr><tr><td> $w_6$ = definitely high (DH)</td><td>(5/6,1,1)</td></tr></table>

<sup>a</sup>z: The crisp value of the perceived economic utility.

## 5. Model validation and simulation

In this section, the SD model is validated and simulated with Vensim PLE 6.3 software, which is an e<sup>fi</sup>cient tool that provides a user-friendly interface and clear charts for us to conduct the simulation and result analyses [45].

## 5.1. Key assumptions

We assume that only two types of vehicles exist on the market, i.e., ICVs and EVs. Potential adopters consist of <sup>fi</sup>rst-time vehicle buyers and vehicle repurchase buyers. The model is simulated under the baseline scenario with a <sup>fi</sup>xed rate of purchase tax and gasoline price with linear growth. All the stock variables that relate to the numbers of vehicle owners and infrastructures are initially valued by using the 2013 statistical data in China.

## 5.2. Model validation

## 5.2.1. Direct structure tests

The direct structure tests include a structure assessment, paramete assessment, boundary adequacy test, and dimension test [59].

First, in our model, all the variables and their relations are developed on the basis of the previous literature on EV adoption and real cases and data. Therefore, our model has passed the structure assessment, with all the structures and casual loops in our model theoretically and empirically matching the real world. Second, in the parameter assessment, two experts in the area of EV and SD modeling were invited to assess and adjust all the constant variables in our model to ensure that these critical variables are reasonable and conceptually match the real world. Third, all the important model variables are endogenous (which is shown in Appendix A), which means that our model passed the boundary adequacy test. Finally, the dimensions of all variables were checked using the “Unit Check” function in Vensim, and our model also passed the dimension consistency test.

## 5.2.2. Structure-oriented behavior tests

Structure-oriented behavior tests focus on the validation of the patterns of model-generated behavior [60].

5.2.2.1. Extreme-condition test. We conduct the extreme-condition test by assigning extreme values to the critical constant variables to determine whether the model-generated behaviors are reasonable. The parameter settings are shown in Table B1, and our model passed this test.

Table 7  
Parameter settings of the model with both precise perception and vague perception.

<table><tr><td>No.</td><td>Scenario</td><td>Equation of “Adoption Rate of EV”a</td></tr><tr><td>S1-1</td><td>consumers are extremely sensitive to the cost difference and the number of infrastructures and have a precise perception of them</td><td>IF THEN ELSE((0.025 + (1-((1-(Cost Difference between ICV and EV/(Life Cycle Cost of ICV + ABS (Cost Difference between ICV and EV)) + 0.5))* (1-(Infrastructure Convenience/1.2))^(1/2)))*(1 + Perceived Social Utility) &lt; 1, (0.025 + (1-((1-(Cost Difference between ICV and EV/(Life Cycle Cost of ICV + ABS(Cost Difference between ICV and EV)) + 0.5))* (1-(Infrastructure Convenience/1.2))^(1/2)))*(1 + Perceived Social Utility), 1)</td></tr><tr><td>S1-2</td><td>consumers have a vague perception of the cost difference and number of infrastructures</td><td>Perceived Economic Utility*(1 + Perceived Social Utility)</td></tr></table>

<sup>a</sup> “Adoption rate of EV”: The range of “Adoption Rate of EV” is [0.025, 1], where 0.025 is the rate of innovators [73]. It increases with an increase in the economic utility and social utility of using an EV.

![](/api/attachments/DZWBSWCY/fulltext/images/d9ae440889728b8035301c7c23efabb96be15abd6865bb70b6388743dc694fb6.jpg)

![](/api/attachments/DZWBSWCY/fulltext/images/cecc03f1eb2db5ce93652bf8090fcddcbbe23319e49cbd7b68536aa91aa8e515.jpg)  
Fig. 4. Simulation results under the scenarios with a precise perception and vague perception.

Table 8  
Parameter settings of the model with di<sup>f</sup>erent EV technology levels.

<table><tr><td>No.</td><td>Scenario</td><td>Progress ratio</td></tr><tr><td>S2-1</td><td>The cost of producing an EV is reduced to 90% when the cumulative production volume of EVs is doubled.</td><td>90%</td></tr><tr><td>S2-2 (Baseline)</td><td>The cost of producing an EV is reduced to 85% when the cumulative production volume of EVs is doubled.</td><td>85%</td></tr><tr><td>S2-3</td><td>The cost of producing an EV is reduced to 80% when the cumulative production volume of EVs is doubled.</td><td>80%</td></tr><tr><td>S2-4</td><td>The cost of producing an EV is reduced to 75% when the cumulative production volume of EVs is doubled.</td><td>75%</td></tr><tr><td>S2-5</td><td>The cost of producing an EV is reduced to  $70\%^a$  when the cumulative production volume of EVs is doubled.</td><td>70%</td></tr></table>

<sup>a</sup> 70% Is the minimum possible progress ratio, which means that the production cost will decrease by 30% when the cumulative production is double [74].

![](/api/attachments/DZWBSWCY/fulltext/images/e63d2695beb1be938c835c48b2d0adb2089003e48d83f7b7b2d94e1f0c66a25f.jpg)

![](/api/attachments/DZWBSWCY/fulltext/images/2d4c5cbaf5a469ee69201d7f4a201f7c8de7cfe6c1c41fce595aa257904d828e.jpg)  
Fig. 5. Simulation results under the scenarios with di<sup>f</sup>erent progress ratios.

5.2.2.2. Sensitivity test. We conduct a sensitivity test on six critical parameters to con<sup>fi</sup>rm that the model is sensitive to these parameters similar to the real world. First, we assign di<sup>f</sup>erent values to the variable of “Increasing Rate of Gasoline Price,” which $\mathrm { a r e } - 8 2 \% , - 4 1 \% , - 2 1 \% , 2 1 \% ,$

41%, and 82%. The result of this test is shown in Fig. B1 (a), and we <sup>fi</sup>nd that the adoption rate of EVs increases as the gasoline price increases. Second, we run the model with the di<sup>f</sup>erent progress ratios of 70%, 75%, 80%, 85%, 90%, and 95%, which represents the technology levels of EV. As shown in Fig. B1(b), the EV adoption rate is higher when the progress ratio

Table 9  
Parameter settings of model with di<sup>f</sup>erent increasing rates of the gasoline price.

<table><tr><td>No.</td><td>Scenario</td><td>Value of “Increasing Rate of Gasoline Price”</td><td>Equation of Price of Gasoline</td></tr><tr><td>S3-1 (Baseline)</td><td>The price of gasoline changes with linear growth.</td><td> $0.4129^a$ </td><td>Increase Rate of the Gasoline Price*Time + 7.79b</td></tr><tr><td>S3-2</td><td>The price of gasoline changes with logarithmic growth.</td><td> $2.2^c$ </td><td>Increase Rate of the Gasoline Price*LN (Time + 16) + 1.5414</td></tr><tr><td>S3-3</td><td>The price of gasoline is fixed.</td><td>0</td><td>Increase Rate of the Gasoline Price* Time + 7.79</td></tr><tr><td>S3-4</td><td>The price of gasoline changes with linear decrease.</td><td> $-0.4129^d$ </td><td>MAX (Increase Rate of the Gasoline Price* Time + 7.79, 0)</td></tr></table>

<sup>a</sup> 0.4129: Calculated with the historical price of 93# gasoline from 1998 to 2013.  
<sup>b</sup> 7.79: The price of 93# gasoline in December 2013 in China.  
<sup>c</sup> 2.2: Calculated with the historical price of 93# gasoline from 1998 to 2013.  
<sup>d</sup> −0.4129: We set the opposite increasing rate in S3-1 as the decreasing rate of gasoline price.

![](/api/attachments/DZWBSWCY/fulltext/images/d1b51d9ea321c4d737797f4f9f1513c60e1387b7e7a3f3342f7db4f0b02b572f.jpg)  
(a) Cost difference between ICV and EV

![](/api/attachments/DZWBSWCY/fulltext/images/276569682d0fd908e2755f4145817c8f2fd4128309b65c88f9c12075760a7eaf.jpg)  
(b)Adoption rate of EV

![](/api/attachments/DZWBSWCY/fulltext/images/7b3c03a5c36ee9139ae2098c8c320c7196ec1a3e77432fb8fa36edb6d66a20a0.jpg)  
(c) Market share of EV  
Fig. 6. Simulation results under the scenarios with di<sup>f</sup>erent variations in gasoline price.

Table 10  
Parameter settings for di<sup>f</sup>erent investments in infrastructure.

<table><tr><td>No.</td><td>Scenario</td><td>Total Investment</td><td>Equation of “Infrastructure per year”</td></tr><tr><td>S4-1</td><td>40% less infrastructure investment than the government plan</td><td>60 billion RMB</td><td>IF THEN ELSE (Time = 0, 0, IF THEN ELSE (Time &lt; = 15, 240000, IF THEN ELSE (Amount of Infrastructure &lt; = 2.16913e + 007, Amount of Infrastructure* 0.009, 0)))</td></tr><tr><td>S4-2</td><td>20% less infrastructure investment than the government plan</td><td>80 billion RMB</td><td>IF THEN ELSE (Time = 0, 0, IF THEN ELSE (Time &lt; = 15, 320000, IF THEN ELSE (Amount of Infrastructure &lt; = 2.16913e + 007, Amount of Infrastructure* 0.009, 0)))</td></tr><tr><td>S4-3(Baseline)</td><td>Infrastructure investment of the government plan</td><td>100 billion RMB</td><td>IF THEN ELSE (Time = 0, 0, IF THEN ELSE (Time &lt; = 15, 400000, IF THEN ELSE (Amount of Infrastructure &lt; = 2.16913e + 007, Amount of Infrastructure* 0.009, 0)))</td></tr><tr><td>S4-4</td><td>20% more infrastructure investment than the government plan</td><td>120 billion RMB</td><td>IF THEN ELSE (Time = 0, 0, IF THEN ELSE (Time &lt; = 15, 480000, IF THEN ELSE (Amount of Infrastructure &lt; = 2.16913e + 007, Amount of Infrastructure*0.009, 0)))</td></tr><tr><td>S4-5</td><td>40% more infrastructure investment than the government plan</td><td>140 billion RMB</td><td>IF THEN ELSE (Time = 0, 0, IF THEN ELSE (Time &lt; = 15, 560000, IF THEN ELSE (Amount of Infrastructure &lt; = 2.16913e + 007, Amount of Infrastructure*0.009, 0)))</td></tr></table>

is lower (higher technology level). Third, the sensitivity to infrastructure is veri<sup>fi</sup>ed. Di<sup>f</sup>erent amounts of infrastructure investment, i.e., 40 billion, 60 billion, 80 billion, 100 billion (baseline), 120 billion, 140 billion, and 180 billion, are assigned, which leads to di<sup>f</sup>erent numbers of charging infrastructures that are under construction per year. Fig. B1(c) shows that when infrastructure investment is higher, the adoption rate of EVs is higher. Finally, the values of 0.2, 04, 0.6, 0.8, and 1 are assigned to “ICT” and the “Sensitivity of Social Service.” In addition, four di<sup>f</sup>erent stages are assigned to the “Life Cycle Stage of the Business Model” [53]. As presented in Fig. B1(d)–(f), the adoption rate of EVs increases as we increase the level of ICT and the life cycle stage of the business model. Although there is no signi<sup>fi</sup>cant di<sup>f</sup>erence on EV adoption in the early stage, the sensitivity of social service plays its role when the EV network expands. All the results that are mentioned above are reasonable compared to the real-world cases, which demonstrates that our model passed the sensitivity test.

![](/api/attachments/DZWBSWCY/fulltext/images/e325faa377b976c5874ae9b0a4957dd4ad28196d7c4c4a9bf68d9e79e45cb12f.jpg)

![](/api/attachments/DZWBSWCY/fulltext/images/3ad57be9688fe6a96683dc27f8250434ce36493e72750c424df372d3c77a936c.jpg)  
Fig. 7. Simulation results under the scenarios with di<sup>f</sup>erent infrastructure investments.

Table 11  
Parameter settings with di<sup>f</sup>erent stages in the Gartner Hype Cycle.

<table><tr><td>No.</td><td>Scenario</td><td>Value of “ICT”</td></tr><tr><td>S5-1 (Baseline) $^a$ </td><td>At the first stage: innovation trigger</td><td>0.2</td></tr><tr><td>S5-2</td><td>At the second stage: peak of inflated expectation</td><td>0.4</td></tr><tr><td>S5-3</td><td>At the third stage: trough of disillusionment</td><td>0.6</td></tr><tr><td>S5-4</td><td>At the fourth stage: slope of enlightenment</td><td>0.8</td></tr><tr><td>S5-5</td><td>At the fifth stage: plateau of productivity</td><td>1</td></tr></table>

Table 12  
<sup>a</sup> In the Gartner Hype Cycle [54], technologies such as the Internet of Things, autonomous vehicles, and big data are near the transition between the <sup>fi</sup>rst and second stages.

Parameter settings with di<sup>f</sup>erent business model life cycle stages.

<table><tr><td>No.</td><td>Scenario</td><td>Value of “The Life Cycle Stage of the Business Model”</td></tr><tr><td>S6-1 (Baseline)</td><td>At the first stage: introduction</td><td>0.25</td></tr><tr><td>S6-2</td><td>At the second stage: growth</td><td>0.5</td></tr><tr><td>S6-3</td><td>At the third stage: maturity</td><td>0.75</td></tr><tr><td>S6-4</td><td>At the fourth stage: stagnation</td><td>1</td></tr></table>

![](/api/attachments/DZWBSWCY/fulltext/images/8e7d339526313afff48d00627757b4faf063d68019bc1ec7fda2d9d917e674d7.jpg)  
(a) Perceived social utility

![](/api/attachments/DZWBSWCY/fulltext/images/dd0f67087d72c3cf500edc8d930863669fedc247b198be20ca77daff8693d347.jpg)  
(b) Commercial activity innovation

![](/api/attachments/DZWBSWCY/fulltext/images/e6455ce7edb6958b4844fb72d2601994ef61181f8e834f138a5a4c35dede4784.jpg)

![](/api/attachments/DZWBSWCY/fulltext/images/2926f3b304175103486c7b05b77e0a2dad6962a1e158d5f3787d667dd2ebbb90.jpg)  
(d) Market share of EV  
Fig. 8. Simulation results in the scenarios with di<sup>f</sup>erent stages in the Gartner Hype Cycle.

5.2.2.3. Integration error test. In this model, the integration interval and the numerical integration method are changed to perform this test [46]. First, we adjust the integration interval to 1, 0.5, and 0.25 to <sup>fi</sup>nd the accordant model-generated patterns. Second, the Euler’s integration method and the Runge–Kutta integration method are separately applied in our model, thus generating two consistent model behaviors. All these running results indicate that our model passed the test.

![](/api/attachments/DZWBSWCY/fulltext/images/18b6294370d86cd774ac3d2dd9da415a1354698fb64e688bbd51f9cc685b2dc4.jpg)

![](/api/attachments/DZWBSWCY/fulltext/images/0bf55c02df75b35db056e45c96ab2dad072558070b431eb80882939253d58063.jpg)  
(b) Infrastructure convenience

![](/api/attachments/DZWBSWCY/fulltext/images/d9cf65e6ed556e51bf96474afc4d432eda4d4868148de377fb852452818e88c7.jpg)  
Fig. 9. Simulation results in the scenarios with di<sup>f</sup>erent business model life cycle stages.

## 5.2.3. Behavior pattern test

This test aims at assessing whether the generated behavior pattern of our model is in accord with the pattern in a real situation [60]. We compare the simulation result with the historical data<sup>4</sup> of EV ownership from 2013 to 2016. As shown in Fig. B2, the two patterns are similar, and we can conclude that our model passed this test.

## 5.3. Model simulation and running results

Model simulations are conducted in two steps to address our research questions. First, we compare the adoption behaviors of the model with both the precise and vague perceptions. Then, we perform the simulations by varying the values of the variables that relate to the economic utility and social utility to test their e<sup>f</sup>ects on EV adoption.

## 5.3.1. Simulation on vague perception

In this section, we simulate the adoption process of EVs with both a precise perception and vague perception. All the parameter settings are shown in Table 7.

The simulation results are presented in Fig. 4. Although the simu lation with precise perception presents a vigorous increase in the adoption rate and market share of EVs, the number of EV owners under the scenario with a vague perception is consistent with the historical data, as the result of the behavior test shows. The step increase in the EV adoption, which is shown in curve S1-2 in Fig. 4(a), re<sup>fl</sup>ects the delay e<sup>f</sup>ect that is caused by consumers’ vague perception, which leads to a much slower growth of the market share for EVs. According to

Weber’s law [61], a consumer could perceive the variations of cost di<sup>f</sup>erence and infrastructure convenience only when the variations reach a certain amount. This delay e<sup>f</sup>ect from a vague perception provides us with the reason for the low adoption rate of EVs even with the current strong promotion. For example, it is di<sup>fi</sup>cult for consumers to clearly perceive the growth of EV infrastructure in the early promotion stage when the pilot projects are scattered and distributed across many cities.

## 5.3.2. Simulations on cost and infrastructure convenience

We perform the remaining simulations by considering consumers’ vague perception because the results of this type of simulation approximate the real case and observed data.

5.3.2.1. Simulation on purchase cost. The purchase cost is one of the most important cost factors that in<sup>fl</sup>uences EV adoption (e.g., [5]). We assume that the price of a vehicle is a<sup>f</sup>ected by the vehicle technology level, which follows the “Learning Curve” [52]. However, ICV technology is relatively mature with limited space for price reduction. We provide <sup>fi</sup>ve scenarios to represent the <sup>fi</sup>ve levels of vehicle technology, as shown in Table 8.

The adoption process appears to be more aggressive when the progress ratio of an EV decreases from 90% to 85%, which means that the e<sup>f</sup>ect of technology development on EV price reduction decreases. We can explain this phenomenon with the diminishing marginal e<sup>f</sup>ect of the “Learning Curve” [52]. Moreover, although a higher technology level brings a substantial increase in EV adoption at the initial stage, most of the scenarios with other technology levels will <sup>fi</sup>nally reach the same EV adoption rate (Fig. 5(b)). Therefore, reducing the price of EVs through vehicle technology improvement may have a remarkable e<sup>f</sup>ect on promoting EV adoption, but it is not an e<sup>fi</sup>cient method when EV technology becomes mature.

5.3.2.2. Simulation on operation cost. Compared to electricity price, the price of gasoline presents frequent <sup>fl</sup>uctuations. Moreover, the worry of the rapid increase in gasoline price is one of the reasons why consumers intend to adopt EVs. Thus, we decided to conduct the simulation focusing on the price of gasoline to explore its e<sup>f</sup>ect on the adoption process of EV. There are two scenarios with di<sup>f</sup>erent growth tendencies <sup>fi</sup>tted with the historical data of gasoline price. Furthermore, simulations with <sup>fi</sup>xed and decreasing gasoline prices are also conducted, shown in Table 9.

The simulation results are shown in Fig. 6. With a lower operation cost, EV becomes more comparable to ICV in cost and wins more of the market share. In the cases of S3-2 and S3-3, however, a small cost di<sup>f</sup>erence between ICVs and EVs does not make much di<sup>f</sup>erence to consumers. For this reason, the positive e<sup>f</sup>ect of an increasing gasoline price on EV adoption is diminishing over time.

In addition, there is an asymmetric e<sup>f</sup>ect of gasoline price on EV adoption. Intriguingly, this asymmetric e<sup>f</sup>ect appears to be more remarkable around the 6th year, when the EV cost is lower than the ICV cost (see Fig. 6(b)). This asymmetric e<sup>f</sup>ect is a type of S-shaped utility function [62].

5.3.2.3. Simulation on infrastructure convenience. Improving infrastructure convenience is one focus of the Chinese government to promote EVs. In China, the government has increased the investment in infrastructure construction to 100 billion RMB. To capture the e<sup>f</sup>ect of infrastructure convenience on EV adoption, we simulate the model with di<sup>f</sup>erent infrastructure investments (Table 10). For the baseline, 400,000 charging stations are built per year by considering the government plan.

All the investment in infrastructure will be exhausted in the <sup>fi</sup>rst 15 years according to the government plan. However, from Fig. 7, we <sup>fi</sup>nd that there exists little di<sup>f</sup>erence between the growth patterns in the adoption rate and the market share of EVs before the 10th year. We attribute this result to the network externality. As the potential vehicle buyers increase, the delay and ampli<sup>fi</sup>cation e<sup>f</sup>ect of infrastructure convenience on EV adoption is more remarkable.

Furthermore, the same variation in infrastructure investment leads to di<sup>f</sup>erent increasing patterns of the adoption rate (Fig. 7(a)). For example, compared to scenario S4-5, increasing the investment by 20% in scenario S4-4 does not lead to a signi<sup>fi</sup>cant increase in the adoption rate. However, there is a remarkable increase in the adoption rate in scenario S4-3 in the later running period if 20% more is invested than in scenario S4-4. Similar situations also exist in the other scenarios. These simulation results suggest that if the government wants a higher adoption rate in the short term, it should invest more in infrastructure at the early stage.

## 5.3.3. Simulations on social utility

5.3.3.1. Simulation on ICT. ICT in our model is speci<sup>fi</sup>ed as senior technology, mobile networks, and related software. The Gartner Hype Cycle [54], which predicts the mega-trends of popular emerging technologies, is employed as the evaluation tool in our model. We assess the maturity of ICT from 0 to 1 according to the <sup>fi</sup>ve stages in the Gartner Hype Cycle, as shown in Table 11.

In Fig. 8, ICT presents distinct e<sup>f</sup>ects on the di<sup>f</sup>erent variables. ICT has positive e<sup>f</sup>ects on enhancing the perceived social utility and commercial activity innovation. However, ICT has a diminishing marginal e<sup>f</sup>ect on decreasing the EV price, which implies that premature in troduction or emphasis of ICT to EV may lead to an adverse e<sup>f</sup>ect with stronger hinder of EV price reduction. In other words, development of ICT is bene<sup>fi</sup>cial to EV adoption only when the EV technology is mature and the EV network reaches a certain scale.

5.3.3.2. Simulation on commercial activity innovation. Commercial activities include the activities of marketing, information collection, recommendations, and transactions in social commerce [35], whose innovation and presence depend heavily on the business model. In each stage, model adaption and activity innovation are necessary for companies to survive and develop [53]. We conduct simulations on commercial activity innovation by establishing four scenarios with di<sup>f</sup>erent business model life cycle stages (refer to [53], and the results are given in Table 12.

By observing the results in Fig. 9(a), we <sup>fi</sup>nd that the positive e<sup>f</sup>ect of social commercial innovation on EV adoption becomes more remarkable in the later running period, around the 15th year, because of network externality. The catalytic role of network externality on the relation between social commercial innovation and infrastructure convenience is more discernable from the 10th year (see Fig. 9(b)). We can thus conclude that social commercial innovation may not be as e<sup>f</sup>ective as other factors in accelerating EV adoption in the beginning, whereas social commercial innovation should be valued more in the later stages to increase the EV market continuously.

## 6. Conclusion

This study was driven by real cases from the EV and Internet in dustries. EV adoption is a complex dynamic process in which the government is dedicated to substituting ICVs with EVs, and the Internet industry has an overwhelming urge to forge EVs as the new mobile terminal of social commerce. By taking advantage of intelligent technology and innovative business models of social commerce, EVs have the potential to rapidly replace ICVs and rewrite the history of the automobile by acting in a manner similar to that of the <sup>fi</sup>rst smart iPhone. A better understanding of why and how EVs are adopted (or not) can help us to make more realistic business plans and public policies. This study o<sup>f</sup>ers a useful SD model to explain and predict the dynamic process of EV adoption by capturing the impact from the causal feedbacks with the factors of social commerce and vehicle attributes. This study reinforces the internal consistency of the EV adoption theories by ensuring that the adoption behavior that it purports to explain can in fact be generated by its underlying empirical evidence. In addition, varying parameter and treatment provides a laboratory to discover the practical implications that are not intuitively obvious.

Illustrated by the simulation results, the utility from incorporating social commerce in EVs is an alternative impetus to promote EV adoption. However, we <sup>fi</sup>nd that this strategy can play a more e<sup>f</sup>ective role if it appropriately coordinates with the primary positioning of EVs as a substitute for ICVs. Generally, in the early stage of EV development, the focus should be placed on the vehicle attributes of EVs, such as vehicle performance, price reduction, and convenient charging, which are the major concerns of consumers and have signi<sup>fi</sup>cant impacts on EV adoption. The premature introduction of social commerce to EVs may generate another obstacle to adoption by creating new technical di<sup>fi</sup>culties and slowing EV price reductions. Additionally, a low user base of EVs may lead to a negative network externality that weakens the e<sup>f</sup>ect of social commerce in EV adoption. Accordingly, the cooperation of the vehicle and Internet industries is a prospective strategy for EV adoption in which the Internet companies bring together sophisticated ICT and potential adopters who are interested in social commerce. The practical implications for the speci<sup>fi</sup>c in<sup>fl</sup>uencing factors are also provided.

(1) Consumers’ vague perception enforces the delay e<sup>f</sup>ect of the substitution between ICV and EV. Because of consumers’ torpid perception of the gradual cost reduction and improvement of convenient charging, EVs become a less attractive substitute for ICVs (scenarios 1-1 and 1–2). Thus, some measures should be taken by the governors and managers to conquer this challenge. On the one hand, an infrastructure that is built on arterial roads and business districts is more e<sup>f</sup>ective in providing convenience to drivers and attracting more attention from potential adopters. Developing business models of social commerce, such as charging and parking sharing, also improves the convenience for drivers. On the other hand, it is important to emphasize the economy of EVs with subsidies and charging cost savings to promote EVs.

(2) Consumers are more sensitive to increases in gasoline prices (the results that are shown in scenarios 3-1 to 3–4). Thus, the promotional focus should be transferred to operation cost savings when the EV price becomes comparable to the price of ICVs. In the early stage, governors and managers should focus the same attention on the gasoline price reduction scenario because it may create a greater obstacle to EV adoption. With the reduction in gasoline prices, intervention by the government is suggested to guarantee price stability. The EV industry should prepare with some appropriate countermeasures such as improving the vehicle performance and battery e<sup>fi</sup>ciency.

(3) The “Learning Curve” e<sup>f</sup>ect of technology development is more signi<sup>fi</sup>cant to EV adoption in the early stage. Inspired by the marginal e<sup>f</sup>ect of the “Learning Curve” that is presented in scenarios 2- 1 to 2–6, we suggest that it is more e<sup>fi</sup>cient for governors to support EV industries with incentives or R&D investment at the initial stage. A price advantage is critical to consumers’ adoption decision; thus, companies should increase their investment in technology development to reduce the price of EVs when there is a large cost di<sup>f</sup>erence between ICVs and EVs.

(4) “Few is not better than nothing” for the charging infrastructures in EV adoption. The simulation results on infrastructure convenience indicate that EV infrastructure must reach a certain amount before it can signi<sup>fi</sup>cantly facilitate the adoption of EVs. Therefore, in tensive infrastructure construction in one or two areas will better reinforce EV adoption with the apparent increase in charging infrastructures rather than distributing them in many scattered pilot cities or residential areas.

(5) The results from simulation scenarios S5-1 to S5-5 show that ICT could increase the cost of EVs and cannot facilitate EV adoption until EV prices are acceptable to consumers. Considering this concern, consociation with the Internet companies is suggested for the vehicle industry, which will help the vehicle industry to ease the burden of R&D. In addition, to make the development of ICT more visible to consumers, user-friendly designs should be adopted in related technical applications, and relevant software may be preinstalled in the electronic systems of EVs.

(6) Commercial activity innovation helps the integration of the com mercial purpose with social activities. By utilizing real-time information sharing and location technology, sharing economy can be realized in the EV network. For example, charging sharing not only advances the infrastructure convenience of EV drivers but also at tracts business investment in the charging infrastructure. Nonetheless, the success of commercial activity innovation depends heavily on mature technology and network externality. Without su<sup>fi</sup>cient preparation, an overemphasis on the form of commercial activity may disappoint consumers with unsatisfactory performance.

Future research may focus on the e<sup>f</sup>ect of policies on EV adoption by considering di<sup>f</sup>erent combinations of various incentives. In addition, EV adoption is related to <sup>fi</sup>rst-time buyers and repeat purchasers. The previous driving experience of repurchase buyers may have an e<sup>f</sup>ect on their purchase decisions. Future research may conduct surveys or experiments to test this e<sup>f</sup>ect and study EV adoption in the markets of developed and developing countries with di<sup>f</sup>erent proportions of repurchase buyers.

## Acknowledgments

The work described in this article was partially supported by the National Science Foundation of China [Projects 71522002 and 71371076] and Guangdong National Science Funds for Distinguished Young Scholars [Project 2014A030306006].

## Appendix A. Model variables, equations (descriptions), dimensions, and explanations

See Tables A1–A3.

Table A1  
Flows, equations, dimensions, and explanations.

<table><tr><td>Flow (Endogenous)</td><td>Equation</td><td>Dimensiona</td><td>Explanation</td></tr><tr><td>New Buyers per year</td><td>=5.2863e + 06*(1 + Growth Rate of Vehicle Owners)^(Time)</td><td>Con/Year</td><td>We assume that the number of new vehicle buyers increases with a fixed growth rate. 5.2863e + 06 is 6% (fixed growth rate) of the total number of vehicle owners in 2013.</td></tr><tr><td>Buying ICVs</td><td>=First Time Vehicle Buyers/TIME STEP-Buying EVs</td><td>Con/Year</td><td>The number of new vehicle buyers who buy ICVs.</td></tr><tr><td>Buying EVs</td><td>=IF THEN ELSE (Time = 0, MIN (First Time Vehicle Buyers/TIME STEP *Adoption Rate of EV, 78499), First Time Vehicle Buyers* Adoption Rate of EV)</td><td>Con/Year</td><td>The number of new vehicle buyers who buy EVs. 78,499 is the production of EVs in 2014 (data from the China Association of Automobile Manufacturers &lt; http://www.caam.org.cn/xiehuidongtai/20150112/1805144355.html &gt;), which ensures that the sales volume is smaller than the production.</td></tr><tr><td>Change Vehicle1</td><td>=ICV Owners/Average Life</td><td>Con/Year</td><td>The number of people who change their ICVs per year.</td></tr><tr><td>Change Vehicles2</td><td>=EV Owners/Average Life</td><td>Con/Year</td><td>The number of people who change their EVs per year.</td></tr><tr><td>Change to ICVs</td><td>=Vehicle Repurchase Buyers/TIME STEP-Change to EVs</td><td>Con/Year</td><td>The number of vehicle repurchase buyers who buy an ICV per year.</td></tr><tr><td>Change to EVs</td><td>=Vehicle Repurchase Buyers/TIME STEP* Adoption Rate of EV</td><td>Con/Year</td><td>The number of vehicle repurchase buyers who buy an EV per year.</td></tr><tr><td>Infrastructures per year</td><td>=IF THEN ELSE (Time = 0, 0, IF THEN ELSE (Time &lt;= 15, 400000, IF THEN ELSE (The Number of Infrastructure &lt;= 2.16913e + 07, The Number of Infrastructure/TIME STEP*0.009, 0)))</td><td>Inf/Year</td><td>According to “The 12th Five Year Plan of Electric Vehicle Technology Development” (&lt;https://policy.asiapacificenergy.org/node/3033 &gt;), 100 billion RMB will be invested in infrastructure construction (400,000 new charging infrastructures per year). After the investment is completely used, the infrastructure will increase at the rate of 0.9%, until the distribution level of the infrastructure reaches the same level as gasoline stations.0.9% is the increasing rate of Chinese gasoline stations in 2012, according to the industrial report (Research in China &lt;http://www.pday.com.cn/htmls/Report/201401/24511729.html &gt;).</td></tr></table>

Table A2  
Auxiliaries, equations, dimensions, and explanations.

<table><tr><td>Auxiliary (Endogenous)</td><td>Equation</td><td>Dimensiona</td><td>Explanation</td></tr><tr><td>Purchase Tax of ICV</td><td>=Price of ICV*0.1</td><td>RMB</td><td>The purchase tax on a vehicle in China is 10% of the vehicle price.</td></tr><tr><td>Purchase Cost of ICV (Convert to Every Year)</td><td>=(Price of ICV + Tax of ICV)/10</td><td>RMB/Year</td><td>The purchase cost of a vehicle consists of the vehicle price and the purchase tax. The average life of a vehicle is 10 years.</td></tr><tr><td>Price of Gasoline</td><td>=Increase Rate of Gasoline Price*Time + Initial Price of Gasoline</td><td>RMB/L</td><td>The price per liter of gasoline.</td></tr><tr><td>Cost of Gasoline</td><td>=Price of Gasoline* Efficiency of ICV*Travel Distance of ICV</td><td>RMB</td><td>The cost of gasoline consumption per year.</td></tr><tr><td>Operation Cost of ICV (Convert to Every Year)</td><td>=Cost of Gasoline</td><td>RMB/Year</td><td>Only the operation costs with significant differences between ICVs and EVs are considered.</td></tr><tr><td>Life Cycle Cost of ICV</td><td>=“Operation Cost of ICV (Convert to Every Year)” + “Purchase Cost of ICV (Convert to Every Year)”</td><td>RMB/Year</td><td>The life cycle cost of a vehicle consists of the purchase cost and operation cost [26]; [27]; [75].</td></tr><tr><td>Life Cycle Cost of EV</td><td>=“Operation Cost of EV (Convert to Every Year)” + “Purchase Cost of EV (Convert to Every Year)”</td><td>RMB/Year</td><td>The life cycle cost of a vehicle consists of the purchase cost and operation cost [26]; [27]; [75].</td></tr><tr><td>Cost of Charging</td><td>=Price of Electricity* Efficiency of EV*Travel Distance of EV</td><td>RMB</td><td>The cost of electricity consumption per year.</td></tr><tr><td>Operation Cost of EV (Convert to Every Year)</td><td>=Cost of Charging</td><td>RMB/Year</td><td>Only the operation costs with significant differences between ICVs and EVs are considered.</td></tr><tr><td>Cumulative Volume of EV</td><td>=EV Owners*Vehicle per Owner</td><td>Vehicle</td><td>The total production of EVs.</td></tr><tr><td>Price of EV</td><td>=DELAY1I (Price of EV, 1, Price of First Unit) * ((Cumulative Volume of EV/DELAY1I (Cumulative Volume of EV, 1, 68939)) ^ Vehicle Technology)</td><td>RMB</td><td>We assume that the price of an EV is the production cost of an EV, which is calculated through the Learning Curve.</td></tr><tr><td>Purchase Tax of EV</td><td>=Price of EV*0.1</td><td>RMB</td><td>The purchase tax on a vehicle in China is 10% of the vehicle price.</td></tr><tr><td>Purchase Cost of EV (Convert to Every Year)</td><td>=(Price of EV + Tax of EV)/10</td><td>RMB/Year</td><td>The purchase cost of a vehicle consists of the vehicle price and the purchase tax. The average life of a vehicle is 10 years.</td></tr><tr><td>Vehicle Technology</td><td>=WITH LOOKUP (Progress Ratio, [(0.7, 1) - (-0.514, 0)], (0.7, -0.514), (0.75, -0.415), (0.8, -0.321), (0.85, -0.2345), (0.9, -0.151), (0.95, -0.074), (0.99, -0.0124)))</td><td>Dmnl</td><td>According to the definition of the progress ratio, we can acquire the corresponding parameter of the Learning Curve [74].</td></tr><tr><td>Progress Ratio</td><td>=MIN (0.85*(Network Technology Support^-0.047), 1)</td><td>Dmnl</td><td>The percentage that the production cost of EVs will be reduced to if the cumulative output of EVs is double. The progress ratio of mechanical assembly products is 80% to 90% [74].</td></tr><tr><td>Cost Difference Between ICV and EV</td><td>=Life Cycle Cost of ICV-Life Cycle Cost of EV</td><td>RMB/Year</td><td>The cost difference between using an ICV and using an EV per year.</td></tr><tr><td>Infrastructure Convenience</td><td>=(5.532e-08*Amount of Infrastructure) *(1 + Commercial Activity Innovation)</td><td>Dmnl</td><td>Generally, the number and the distribution of gasoline stations in China are considered to be very convenient for charging. Considering that the charging time (quick charge) of EVs is 12 times greater than refueling, we obtain this function to transform the number of charging infrastructures to the level of infrastructure convenience. Additionally, we assume that it is affected by commercial activity innovation through economic sharing.</td></tr><tr><td>Fuzzy Cost Difference</td><td>=fuz (Cost Difference between ICV and EV)</td><td>Dmnl</td><td>We can acquire the corresponding fuzzy cost difference with the triangle membership function.</td></tr><tr><td>Fuzzy Infrastructure Convenience</td><td>=fuz (Infrastructure Convenience)</td><td>Dmnl</td><td>We can acquire the fuzzy value of infrastructure convenience with the triangle membership function.</td></tr><tr><td>Perceived Economic Utility</td><td>=fdef (Fuzzy Cost Difference, Fuzzy Infrastructure Convenience)</td><td>Dmnl</td><td>We can infer the perceived economic utility of consumers with the IF...THEN rules.</td></tr><tr><td>Network Scale</td><td>=EXP (Sensitivity of Social Service*(1-1.5*(1-Market Share of EVs)))</td><td>Dmnl</td><td>A modified function of the network effect, referring to [46].</td></tr><tr><td>Commercial Activity Innovation</td><td>=(1 + 0.55*Network Technology Support) *Life Cycle Stage of Business Model*Network Scale</td><td>Dmnl</td><td>We assume that commercial activity innovation is influenced by ICT, which is the foundation and provides the perceived ease of use [76]. It is also affected by the network scale through externality.</td></tr><tr><td>Perceived Social Utility</td><td>=(0.4*Commercial Activity Innovation + 0.25*Network Technology Support)</td><td>Dmnl</td><td>We assume that ICT brings ease of use and that commercial activity innovation helps to increase the perceived usefulness for consumers [76].</td></tr><tr><td>Adoption Rate of EV</td><td>=Perceived Economic Utility*(1 + Perceived Social Utility)</td><td>Dmnl</td><td>We assume that social utility may amplify the effect of economic utility in EV adoption</td></tr><tr><td>Market Share of EV</td><td>=EV Owners/(EV Owners + ICV Owners)</td><td>Dmnl</td><td>The market share of EVs in the vehicle market.</td></tr></table>

<sup>a</sup> Dimension: Con (Consumer), Dmnl (Dimensionless).

Constants, descriptions, dimensions, and explanations.

<table><tr><td>Constant (Exogenous)</td><td>Description</td><td>Dimensiona</td><td>Explanation</td></tr><tr><td>Average Life</td><td>10</td><td>Year</td><td>The average life of a vehicle. Consulted with the marketing panel</td></tr><tr><td>Growth Rate of Vehicle Owners</td><td>0.06</td><td>Dmnl</td><td>The average value of two predicted growth rates of new vehicle buyers, according to Wang et al. [77]&#x27;s report and predictions from the China Automotive Technology &amp; Research Center (&lt; http://mt.sohu.com/20151021/n423799839.html &gt;).</td></tr><tr><td>Price of ICV</td><td>150000</td><td>RMB</td><td>We assume the price of a best seller (Volkswagen LAVIDA) in 2013 to be the price of the ICV.</td></tr><tr><td>Initial Price of Gasoline</td><td>7.79</td><td>RMB/L</td><td>7.79 is the final price of 93# of gasoline in 2013 in China.</td></tr><tr><td>Increase Rate of Gasoline Price</td><td>0.4129</td><td>RMB/Year/L</td><td>We acquire the increasing rate of 93# of gasoline price with the historical prices from 1998 to 2013.</td></tr><tr><td>Efficiency of ICV</td><td>0.08</td><td>L/km</td><td>There will be 8 L of gasoline consumption per 100 km.</td></tr><tr><td>Travel Distance of ICV</td><td>15000</td><td>km</td><td>The average driving distance is from experimental data in the research of Feng et al. [72].</td></tr><tr><td>Travel Distance of EV</td><td>15000</td><td>km</td><td>The average driving distance is from experimental data in the research of Feng et al. [72].</td></tr></table>

(continued on next page)

Table A3 (continued)

<table><tr><td>Constant (Exogenous)</td><td>Description</td><td>Dimensiona</td><td>Explanation</td></tr><tr><td>Efficiency of EV</td><td>0.195</td><td>kWh/km</td><td>There will be 19.5 kWh of electricity consumption per 100 kilometers for an EV.We take the performance of BYD E6 as the performance of an EV in our research, which has a comparable driving range as an ICV.</td></tr><tr><td>Price of Electricity</td><td>0.73</td><td>RMB/kWh</td><td>The second degree of electricity price in Guangzhou, China.</td></tr><tr><td>Price of First Unit</td><td>400000</td><td>RMB</td><td>The price of BYD E6 in 2013.</td></tr><tr><td>Vehicle per Owner</td><td>1</td><td>Vehicle/Con</td><td>We assume that each EV owner has only one EV.</td></tr><tr><td>The Number of Gasoline Stations</td><td>113593</td><td>Inf</td><td>The number of gasoline stations in China before May 2014, from the industrial report of Tian Yang Consulting &lt;http://bjtyzx.com.cn/news/936&gt;.</td></tr><tr><td>ICT</td><td>0.2</td><td>Dmnl</td><td>In the Gartner Hype Cycle [54], technologies such as the Internet of Things, autonomous vehicles, and big data are near the transition between the first and second stages.</td></tr><tr><td>Life Cycle Stage of Business Model</td><td>0.25</td><td>Dmnl</td><td>Because social commerce in EVs is a new concept, we assume that it is in the first stage.</td></tr><tr><td>Sensitivity of Social Service</td><td>0.5</td><td>Dmnl</td><td>The penetration of social media in China, acquired from KANTAR Consulting &lt;https://cn.kantar.com&gt;.</td></tr></table>

<sup>a</sup> Dimension: Con (Consumer), Dmnl (Dimensionless).

## Appendix B. Model validation

![](/api/attachments/DZWBSWCY/fulltext/images/3d2f92b06943febaecf56e5f6face481595d2d05e3e6ce1e88ef01a22d94997c.jpg)

![](/api/attachments/DZWBSWCY/fulltext/images/405cf0007a7ed677114d4d4228175da9ee4cd4019e60e6c6baba21fcf7e7cb07.jpg)

<table><tr><td colspan="3">Adoption Rate of EV</td></tr><tr><td>(1) Adoption Rate of EV: Increasing rate of GP 80%</td><td>(2) Adoption Rate of EV: Progress ratio is 95%</td><td>(3) Adoption Rate of EV: Progress ratio is 90%</td></tr><tr><td>(4) Adoption Rate of EV: Progress ratio is 85%</td><td>(5) Adoption Rate of EV: Progress ratio is 80%</td><td>(6) Adoption Rate of EV: Progress ratio is 75%</td></tr><tr><td>(7) Adoption Rate of EV: Progress ratio is 70%</td><td>(8) Adoption Rate of EV: Progress ratio is 65%</td><td>(9) Adoption Rate of EV: Progress ratio is 60%</td></tr><tr><td colspan="3">(c) Infrastructure (IF)</td></tr><tr><td>(1) Adoption Rate of EV: IF investment-160 billion</td><td>(2) Adoption Rate of EV: Level of ICT-100%</td><td>(3) Adoption Rate of EV: Level of ICT-80%</td></tr><tr><td>(3) Adoption Rate of EV: IF investment-140 billion</td><td>(4) Adoption Rate of EV: Level of ICT-60%</td><td>(5) Adoption Rate of EV: Level of ICT-40%</td></tr><tr><td>(5) Adoption Rate of EV: IF investment-120 billion</td><td>(6) Adoption Rate of EV: Level of ICT-20%</td><td>(7) Adoption Rate of EV: Level of ICT-5%</td></tr><tr><td>(8) Adoption Rate of EV: IF investment-100 billion</td><td>(9) Adoption Rate of EV: Level of ICT-20%</td><td>(10) Adoption Rate of EV: Level of ICT-5%</td></tr><tr><td>(11) Adoption Rate of EV: IF investment-80 billion</td><td>(12) Adoption Rate of EV: Level of ICT-20%</td><td>(13) Adoption Rate of EV: Level of ICT-5%</td></tr><tr><td>(14) Adoption Rate of EV: IF investment-60 billion</td><td>(15) Adoption Rate of EV: Level of ICT-20%</td><td>(16) Adoption Rate of EV: Level of ICT-5%</td></tr><tr><td>(17) Adoption Rate of EV: IF investment-40 billion</td><td>(18) Adoption Rate of EV: Level of ICT-20%</td><td>(19) Adoption Rate of EV: Level of ICT-5%</td></tr></table>

![](/api/attachments/DZWBSWCY/fulltext/images/91d6a9bc11fd0c3517582cad8f43734a17124a57faa147cb21136de05ccdceb4.jpg)

![](/api/attachments/DZWBSWCY/fulltext/images/d88e206b3b45b8e1fa7c64a588a64dfceb2f1399af51c8cd676d38f240936bbb.jpg)

![](/api/attachments/DZWBSWCY/fulltext/images/d2ab1a3f16cc4351967665d12d146a0755710b97ea44e7e89996b9956bc3b2fa.jpg)

![](/api/attachments/DZWBSWCY/fulltext/images/4b336b0403d7139a1f12bcd7c5b67201dd144d190d1e55dd9caf49f9be4f7d62.jpg)  
Fig. B1. Sensitive tests of model behavior.

![](/api/attachments/DZWBSWCY/fulltext/images/078de8a59178226e68e08f22e4ec799ced109a88c0fa83a22b48bc852cc13647.jpg)  
Fig. B2. Behavior test.

Table B1  
Parameter settings and results of extreme-condition test.

<table><tr><td>No.</td><td>Extreme test</td><td>Parameter setting</td><td>Result</td></tr><tr><td>1</td><td>Extremely high growth rate of vehicle owners</td><td>Growth Rate of Vehicle Owners = 50%</td><td>Passed</td></tr><tr><td>2</td><td>Extremely low growth rate of vehicle owners</td><td>Growth Rate of Vehicle Owners = 0%</td><td>Passed</td></tr><tr><td>3</td><td>Extremely long average life of vehicle</td><td>Average Life = 30</td><td>Passed</td></tr><tr><td>4</td><td>Extremely short average life of vehicle</td><td>Average Life = 1</td><td>Passed</td></tr><tr><td>5</td><td>Extremely high efficiency of ICV</td><td>Efficiency of ICV = 1</td><td>Passed</td></tr><tr><td>6</td><td>Extremely low efficiency of ICV</td><td>Efficiency of ICV = 16</td><td>Passed</td></tr><tr><td>7</td><td>Extremely high efficiency of EV</td><td>Efficiency of EV = 1</td><td>Passed</td></tr><tr><td>8</td><td>Extremely low efficiency of EV</td><td>Efficiency of EV = 39</td><td>Passed</td></tr><tr><td>9</td><td>Extremely high price of electricity</td><td>Price of Electricity = 1.46</td><td>Passed</td></tr><tr><td>10</td><td>Extremely low price of electricity</td><td>Price of Electricity = 0</td><td>Passed</td></tr><tr><td>11</td><td>Extremely long travel distance</td><td>Travel Distance of ICV = 30000Travel Distance of EV = 30000</td><td>Passed</td></tr><tr><td>12</td><td>Extremely long travel distance</td><td>Travel Distance of ICV = 0Travel Distance of EV = 0</td><td>Passed</td></tr><tr><td>13</td><td>Extremely high price of the first unit of EV</td><td>Price of First Unit = 800000</td><td>Passed</td></tr><tr><td>14</td><td>Extremely low price of the first unit of EV</td><td>Price of First Unit = 100000</td><td>Passed</td></tr><tr><td>15</td><td>Extremely high technology level of EV</td><td>Progress Ratio = -0.7</td><td>Passed</td></tr><tr><td>16</td><td>Extremely low technology level of EV</td><td>Progress Ratio = -0.95</td><td>Passed</td></tr><tr><td>17</td><td>Extremely high level of ICT</td><td>ICT = 1</td><td>Passed</td></tr><tr><td>18</td><td>Extremely low level of ICT</td><td>ICT = 0.1</td><td>Passed</td></tr><tr><td>19</td><td>Extremely mature stage of business model</td><td>Life Cycle Stage of Business Model = 1</td><td>Passed</td></tr><tr><td>20</td><td>Extremely early stage of business model</td><td>Life Cycle Stage of Business Model = 0.1</td><td>Passed</td></tr><tr><td>21</td><td>Extremely high sensitivity of social service</td><td>Sensitivity of Social Service = 1</td><td>Passed</td></tr><tr><td>22</td><td>Extremely low sensitivity of social service</td><td>Sensitivity of Social Service = 0.1</td><td>Passed</td></tr></table>

## References

[1] P.E. Kourouthanassis, G.M. Giaglis, Introduction to the special issue mobile commerce: the past, present, and future of mobile commerce research. Int. J. Electron Commerce 16 (4) (2012) 5–18.

[2] C. Wang, P. Zhang, The evolution of social commerce: the people, management, technology, and information dimensions, CAIS 31 (5) (2012).

[3] F. Hacker, R. Harthan, F. Matthes, W. Zimmer, Environmental impacts and impact on the electricity market of a large scale introduction of electric cars in Europe-Critical Review of Literature, ETC/ACC Techn. Pap. 4 (2009) 56–90.

[4] M.B. Lieberman, D.B. Montgomery, First-mover advantages, Strat. Manage. J. 9 (S1) (1988) 41–58.

[5] M. Burgess, N. King, M. Harris, E. Lewis, Electric vehicle drivers' reported interactions with the public: driving stereotype change? Transp. Res, Part F-Traff. Psychol. Behav. 17 (2013) 33 44.

[6] N.D. Caperello, K.S. Kurani, Households' stories of their encounters with a plug-in hybrid electric vehicle, Environ, Behav, 44 (4) (2012) 493–508.

[7] E. Graham-Rowe, B. Gardner, C. Abraham, S. Skippon, H. Dittmar, R. Hutchins J. Stannard, Mainstream consumers driving plug-in battery-electric and plug-in hybrid electric cars: a qualitative analysis of responses and evaluations, Transp. Res. A: Policy Pract, 46 (1) (2012) 140–153

[8] J.K. Frenzen, H.L. Davis, Purchasing behavior in embedded markets, J. Consum. Res. 17 (1) (1990) 1 12.

[9] B. Knutson, S. Rick, G.E. Wirnmer, D. Prelec, G. Loewenstein, Neural predictors of purchases, Neuron 53 (1) (2007) 147 156.

[10] E.W. Anderson, Customer satisfaction and price tolerance, Market. Lett. 7 (3) (1996) 265 274.

[11] F. Calisir. E. Calisir, The relation of interface usability characteristics, perceived usefulness, and perceived ease of use to end-user satisfaction with enterprise resource planning (ERP) systems, Comput. Human Behav. 20 (4) (2004) 505 515.

[12] X.M. Luo, C. Homburg, J. Wieseke, Customer satisfaction, analyst stock recommendations, and firm value J Market Bes 47 (6) (2010) 1041–1058

[13] P. Mohseni, R.G. Stevie, Electric vehicles: holy grail or fool's gold, Paper Presented at the Power & Energy Society General Meeting, 2009. PES'09. IEEE (2009).

[14] H. Zhang, Y.B. Lu, S. Gupta, L. Zhao, What motivates customers to participate in social commerce? The impact of technological environments and virtual customer experiences, Inf. Manage. 51 (8) (2014) 1017 1030.

[15] J. Song, E. Walden, How consumer perceptions of network size and social interactions in<sup>fl</sup>uence the intention to adopt peer-to-peer technologies, J. E-Bus. Res. 3 (4) (2007) 49.

[16] J.C. Fisher, R.H. Pry, A simple substitution model of technological change, Technol. Forecast, Soc, Change 3 (1971) 75–88

[17] S.M. Shugan, The cost of thinking, J. Consum. Res. 7 (2) (1980) 99–111.

[18] L.A. Zadeh, Fuzzy logic = computing with words, IEEE Trans. Fuzzy Syst. 4 (2) (1996)103–111

[19] S. Carley, R.M. Krause, B.W. Lane, J.D. Graham, Intent to purchase a plug-in electric vehicle: a survey of early impressions in large US cites, Transp. Res. D-Transp. Environ. 18 (2013) 39–45

[20] B. Avci, K. Girotra, S. Netessine, Electric vehicles with a battery switching station: adoption and environmental impact, Manage. Sci. 61 (4) (2014) 772–794.

[21] O. Egbue, S. Long, Barriers to widespread adoption of electric vehicles: an analysis of consumer attitudes and perceptions, Energy Policy 48 (2012) 717–729.

[22] D. Browne, M. O'Mahony, B. Caul<sup>fi</sup>eld, How should barriers to alternative fuels and vehicles be classified and potential policies to promote innovative technologies be evaluated? J. Clean. Prod. 35 (2012) 140–151.

[23] Z. Rezvani, J. Jansson, J. Bodin, Advances in consumer electric vehicle adoption research: a review and research agenda, Transp. Res. D-Transp. Environ. 34 (2015) 122 136.

[24] R.M. Krause, B.W. Lane, S. Carley, J.D. Graham, Assessing demand by urban con sumers for plug-in electric vehicles under future cost and technological scenarios, Int. J. Sustain. Transp. 10 (8) (2016) 742–751.

[25] R. Sioshansi, OR forum—modeling the impacts of electricity tari<sup>f</sup>s on plug-in hy brid electric vehicle charging, costs, and emissions, Oper. Res. 60 (3) (2012) 506–516.

[26] P. Cicconi, M. Germani, D. Landi, M. Mengarelli, Life cycle cost from consumer side: a comparison between traditional and ecological vehicles, in: I. Kuzle, T. Capuder, H. Pandzic (Eds.), 2014 IEEE International Energy Conference (2014) 1440–1445.

[27] C.T. Lin, T. Wu, X.M. Ou, Q. Zhang, X. Zhang, X.L. Zhang, Life-cycle private costs of hybrid electric vehicles in the current Chinese market, Energy Policy 55 (2013) 501–510.

[28] T.S. Turrentine, K.S. Kurani, Car buyers and fuel economy? Energy Policy 35 (2) (2007)1213-1223.

[29] W. Sierzchula, Factors in<sup>fl</sup>uencing <sup>fl</sup>eet manager adoption of electric vehicles, Transp. Res, D-Transp. Environ. 31 (2014) 126–134.

[30] S. Skippon, M. Garwood, Responses to battery electric vehicles: UK consumer attitudes and attributions of symbolic meaning following direct experience to reduc psychological distance, Transp. Res. D-Transp. Environ. 16 (7) (2011) 525–531.

[31] M. Petschnig, S. Heidenreich, P. Spieth, Innovative alternatives take action – investigating determinants of alternative fuel vehicle adoption, Transp. Res. a-Policy Pract. 61 (2014) 68 83.

[32] W. Sierzchula, S. Bakker, K. Maat, B. van Wee, The influence of financial incentives and other socio-economic factors on electric vehicle adoption, Energy Policy 68 (2014) 183 194.

[33] S. Bakker, J.J. Trip, Policy options to support the adoption of electric vehicles in the urban environment, Transp. Res. D: Transp. Environ. 25 (2013) 18–23.

[34] A.T. Stephen, O. Toubia, Deriving value from social commerce networks, J. Market. Res. 47 (2) (2010) 215 228.

[35] T.-P. Liang, E. Turban, Introduction to the special issue social commerce: a research framework for social commerce, Int. J. Electron. Commerce 16 (2) (2011) 5–14.

[36] K.-Y. Goh, C.-S. Heng, Z. Lin, Social media brand community and consumer beha vior: quantifying the relative impact of user- and marketer-generated content, Inf. Syst. Res. 24 (1) (2013) 88 107.

[37] S. Kim, H. Park, E<sup>f</sup>ects of various characteristics of social commerce (s-commerce) on consumers' trust and trust performance. Int. J. Inf. Manag. 33 (2) (2013 318-332.

[38] M.N. Hajli, The role of social support on relationship quality and social commerce, Technol. Forecast. Soc. Change 87 (2014) 17 27.

[39] F.D. Davis, A Technology Acceptance Model for Empirically Testing New End-user Information Systems: Theory and Results. (Doctoral Dissertation). Massachusetts Institute of Technology, 1985.

[40] P.L. Teh, P.K. Ahmed, Understanding social commerce adoption: an extension of the Technology Acceptance Model, Paper Presented at the 2012 IEEE International Conference on Management of Innovation & Technology (ICMIT) (2012)

[41] D.-H. Shin, User experience in social commerce: in friends we trust, Behav. Inf. Technol, 32 (1) (2013) 52–67

[42] C.S.-P. Ng, Intention to purchase on social commerce websites across cultures: a cross-regional study, Inf, Manage, 50 (8) (2013) 609–620.

[43] P. Van Baalen, J. Bloemhof-Ruwaard, E. Van Heck, Knowledge sharing in an emerging network of practice: the role of a knowledge portal. Eur. Manag, J. 23 (3 (2005) 300–314.

[44] J. Randers, Elements of the System Dynamics Method, MIT press, Cambridge, MA, 1980.

[45] J.D. Sterman, System dynamics modeling: tools for learning in a complex world. Calif. Manage. Rev. 43 (4) (2001) 8 25.

[46] J.D. Sterman, Business Dynamics: Systems Thinking and Modeling for a Complex World vol. 19, Irwin/McGraw-Hill, Boston, 2000

[47] J.F. Engel, D.T. Kollat, R.D. Blackwell, Consumer Behavior, 1st ed., Holt, Rinehart and Winston, New York, 1968.

[48] D. Grewal, K.B. Monroe, R. Krishnan, The e<sup>f</sup>ects of price-Comparison advertising on buyers' perceptions of acquisition value, transaction value, and behavioral intentions, J. Market. 62 (2) (1998) 46 59.

[49] R. Thaler, Mental accounting and consumer choice, Market. Sci. 4 (3) (1985) 199 214.

[50] R.A. Briesch, L. Krishnamurthi, T. Mazumdar, S.P. Raj, A comparative analysis of reference price models, J. Consum. Res. 24 (2) (1997) 202 214.

[51] S.J. Mezias, Y.R. Chen, P.R. Murphy, Aspiration-level adaptation in an American <sup>fi</sup>nancial services organization: a <sup>fi</sup>eld study, Manage. Sci. 48 (10) (2002) 1285 1300.

[52] T.P. Wright, Factors a<sup>f</sup>ecting the cost of airplanes, J. Aeronautical Sci. 3 (4) (1936) 122 128.

[53] B.W. Wirtz. Business Model Management. Design. (2011) Retrieved from

Instrumente–Erfolgsfaktoren von Geschäftsmodellen

[54] J. Fenn, M. Raskino, Gartner's Hype Cycle Special Report for 2011, Gartner, Stamford, CT, 2013 (Retrieved from).

[55] C.C. Ragin, Fuzzy-set Social Science, University of Chicago Press, 2000.

[56] L.A. Zadeh, Outline of a new approach to the analysis of complex systems and decision processes, IEEE Trans. Syst. Man Cybern. SMC-3 (1) (1973) 28–44.

[57] P.M. Larsen, Industrial applications of fuzzy logic control, Int. J. Man Mach. Stud. 12 (1) (1980) 3–10.

[58] S. Opricovic, G.H. Tzeng, Defuzzi<sup>fi</sup>cation within a multicriteria decision model, Int. J. Uncertain. Fuzziness Knowl.-Based Syst. 11 (5) (2003) 635–652

[59] P.M. Senge, J.W. Forrester, Tests for building con<sup>fi</sup>dence in system dynamics models, Syste. Dyn. TIMS Stud. Manag. Sci. 14 (1980) 209–228.

[60] Y. Barlas, Tests of model behavior that can detect structural <sup>fl</sup>aws: demonstration with simulation experiments, Computer-Based Management of Complex Systems, Springer, 1989, pp. 246–254.

[61] E.H. Weber, EH Weber on the Tactile Senses, Psychology Press, 1996.

[62] D. Kahneman, A. Tversky, Prospect theory: an analysis of decision under risk, Econometrica: J. Econ. Soc. (1979) 263–291.

[63] L. Noel, R. McCormack, A cost bene<sup>fi</sup>t analysis of a V2G-capable electric school bus compared to a traditional diesel school bus, Appl. Energy 126 (2014) 246–255.

[64] Y. Zhang, Y.F. Yu, B. Zou, Analyzing public awareness and acceptance of alternative fuel vehicles in China: the case of EV, Energy Policy 39 (11) (2011) 7015–7024.

[65] A.F. Jensen, E. Cherchi, S.L. Mabit, On the stability of preferences and attitude before and after experiencing an electric vehicle, Transp. Res. D: Transp. Environ. 25 (2013) 24 32.

[66] T. Lieven, S. Muehlmeier, S. Henkel, J.F. Waller, Who will buy electric cars? An empirical study in Germany, Transp. Res. D-Transp. Environ. 16 (3) (2011) 236 243.

[67] I. Moons, P. De Pelsmacker, Emotions as determinants of electric car usage inten tion, J. Market. Manag. 28 (3–4) (2012) 195–237.

[68] B. Lane, S. Potter, The adoption of cleaner vehicles in the UK: Exploring the con sumer attitude-action gap, J. Clean. Prod. 15 (11 12) (2007) 1085 1092.

[69] L. Qiu, I. Benbasat, An investigation into the e<sup>f</sup>ects of Text-To-Speech voice and 3D avatars on the perception of presence and <sup>fl</sup>ow of live help in electronic commerce, ACM Trans. Comput.-Hum. Interact. (TOCHI) 12 (4) (2005) 329 355.

[70] A. Animesh, A. Pinsonneault, S.B. Yang, W. Oh, An odyssey into virtual worlds: exploring the impacts of technological and spatial environments on intention to purchase virtual products, MIS Q. (2011) 789 810.

[71] T.-P. Liang, Y.-T. Ho, Y.-W. Li, E. Turban, What drives social commerce: the role of social support and relationship quality, Int. J. Electron. Commerce 16 (2) (2011) 69–90.

[72] B. Feng, F.J. Lai, Q.W. Ye, Government incentive polices for the electric vehicle adoption: behavioral modeling, Work. Pap. (2015).

[73] E.M. Rogers, Di<sup>f</sup>usion of Innovations, 5th ed., Free Press, New York, 2003.

[74] H. Tsuchiya, O. Kobayashi, Mass production cost of PEM fuel cell by learning curve, Int. J. Hydrogen Energy 29 (10) (2004) 985–990.

[75] Z.H. Sui, Z.P. Wang, Technical and economic analysis of pure-electric vehicles based on the life-cycle cost theory, Paper Presented at the Business Management and Electronic Information (BMEI), 2011 International Conference on (2011).

[76] D. Gefen, E. Karahanna, D.W. Straub, Trust and TAM in online shopping: an integrated model, MIS 0. 27 (1) (2003) 51–90.

[77] A. Wang, W. Liao, A.P. Hein, Bigger, Better, Broader: A Perspective on China’s Auto Market in 2020. McKinsey & Company: Automotive & Assembly Practice. 2013.

[78] N. Smith, Still in style, New Media Age (Oct. (29)) (2009) 19.

Dr. Bo Feng obtained her Bachelor. Master and PhD degrees in Management Science from Northeastern University. She is a chair professor and dean at Business School, Soochow University. Dr. Feng visited the City University of Hong Kong as a research fellow from 2009 to 2011, the University of California-Berkeley as a visiting scholar from 2011 to 2012, and Purdue University as a visiting professor in 2014. Her research interests include solving practice-triggered challenging problems with analytics and optimization, parti cularly for interfaces between Operations and IS/Marketing.

Qiwen Ye is a Ph.D. student in the South China University of Technology, majoring in Management Science and Engineering. She received her Bachelor degree in Information Security from the same university. She currently conducts her research at the University of Illinois at Urbana-Champaign as a visiting student. Her research interests cover consumers behavior in Social Commerce and big data analysis in Information System.

Dr. Brian J. Collins obtained his B.S. degree in Purdue University, M.B.A. degree in UNC Charlotte and Ph.D. degree in the University of Alabama. He is the Business Advisory Council Research Fellow and an Associate Professor of Management in the College of Business, University of Southern Mississippi. His research has published in such journal as Journal of Applied Psychology, Journal of Management, and Organizational Research Methods.
