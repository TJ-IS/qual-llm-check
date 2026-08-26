---
otero_id: 15616
otero_key: "3DY5G5RR"
title: "Quality of data model for supporting mobile decision making"
authors: "Julie Cowie; Frada Burstein"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.09.010"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Quality of data model for supporting mobile decision making

Julie Cowie <sup>a,1</sup>, Frada Burstein <sup>b,⁎</sup>

a Department of Computing Science and Mathematics, University of Stirling, FK9 4LA, UK b School of Information Management and Systems, Monash University, Melbourne, Australia

Available online 20 October 2006

## Abstract

This paper describes research towards implementation of a mobile decision support system. Our view is that the mobile decision maker will benefit if provided with a measure of the Quality of the Data (QoD) used in deriving a decision, and how QoD improves or deteriorates while he/she is on the move. We propose a QoD model taking into account static and dynamic properties of the mobile decision context, and use multicriteria decision analysis to represent decision model and derive a QoD measure. A prototype mobile decision support system has been developed to investigate the usefulness of the proposed QoD model. © 2006 Elsevier B.V. All rights reserved.

Keywords: Mobile decision support; Multicriteria decision analysis; Quality of data

## 1. Introduction

The last decade has seen significant advances in the way humans interact with technology. Users of computers are no longer constrained to the office desktop, but can have much more flexible access to technology almost anywhere, anytime. The spread of e-services and wireless devices has facilitated a new way of using computers, increased accessibility to data, and in turn, influenced the way in which users make decisions while on the move.

Consider for example tourists who are looking for the nearest parking space in a city. Having access to a mobile device that can locate available parking spaces nearby can save them from wasting time driving around searching for a spot. In this situation, the mobile device provides decision support to the tourists by giving them instant access to data (i.e., available parking spaces). However, if the tourist is not quick enough, someone else might take such parking spot. Wouldn't she be better supported if the mobile device could also advise her that the parking spot she found is expected to be taken within the next 5 min? In this case, we are raising the level of decision support by providing the tourist with added information indicating the validity of data relative to time.

The scenario discussed above is an example of mobile decision making in which the decision maker is faced with the task of choosing the best option from a set of available options while being on the move. In mobile decision making, the alternatives will be compared on the basis of their evaluations (or scores) against multiple criteria, however, such evaluations may vary due to context changes. For example, as the tourist moves from one city to another, the availability of parking spots, security of parking spaces, or waiting time until a space becomes available will vary accordingly.

Our research is concerned with the changing paradigm of decision support. We focus on changes in the way in which decisions are often made, and the impact this has on the type of systems developed to support decision making. The quality of data (QoD) becomes extremely important as the focus of decision support moves from strategic long term decision analysis to justin-time operational decision support [8,10]. Also, with shifting to mobile decision support, data timeliness, completeness, reliability, and relevance have to be considered as contributing factors of QoD metrics. For example, in the area of contingency management a “good enough” feasible decision achievable “on the spot”, anytime, anywhere is often preferable to a perfect solution that may require extensive additional computational resources as well as time.

In this paper, we propose a QoD model that takes into account static and dynamic properties of mobile decision making. We discuss a prototype mobile decision support system (MDSS) which provides a ranking of options and a QoD indicator. Our view is that the mobile decision maker will be better supported in his choice making if he is aware of the QoD used in deriving the decision, and how QoD improves or deteriorates while he is on the move. The paper concludes with proposed future work and conclusions drawn.

## 2. Mobile decision making

To date, much of our work has adopted multicriteria decision analysis (MCDA) to provide static decision support [1]. Here we can assume that the evaluation of alternatives with respect to criteria is constant (over a given period of time), and evaluations will not fluctuate according to some external factor. For example, in assessing a suitable location to conduct a conference, criteria such as size of rooms, facilities available, and accommodation costs will have scores that are unlikely to change from 1 min, or even one day, to the next [7].

In a mobile environment, the decision being made is a dynamic process. We cannot assume that the score we give for a particular alternative for a particular criterion will remain constant over time. For example, suppose the decision maker is deciding on a mode of transport for travel to work. During rush hour, the quickest mode of transport could be the train. Outside peak hours, the quickest mode of transport could be the car. In this scenario, external factors (here, time of day) can cause the scores we would give to an alternative for a particular criterion to fluctuate. In such situations, it is important to have some indication of how static or dynamic the decision situation is, and some estimation of the time period over which the stability of the data is likely to be maintained. In this circumstances there is the need to not only provide decision support in the traditional sense as seen with static decisions, but take into consideration a possibility of some changes in data over time and to give some indication of the quality of the decision or QoD being received because of these changes.

## 3. Qod framework for mobile decision support

The idea of informing the mobile user of the changing parameters in their context has been adopted in most mobile devices. They use icons and alerts to indicate different measures which can potentially contribute to QoD and are important in supporting the decision-making task. The available battery energy, for example, is usually represented in mobile phones by a battery icon with four bars, where 4 bars indicate full energy while 1 bar indicates low energy (see Fig. 1a). When there is not enough energy, the user receives an alert indicating a low battery. The user then becomes aware that he should not finalise a business transaction over the phone, as the business call might be cut off anytime. Network connection is usually represented by an antenna (Fig. 1b). When the network connection is weak, the mobile user is aware that it will take long to download a website from the device. Network security, on the other hand, is usually indicated by a padlock as shown in Fig. 1c. When the network is safe, the padlock is locked, when not safe, the padlock is unlocked. When the mobile user wishes to access confidential data from his mobile device he will ensure that the padlock is locked, reflecting a secure environment.

Fig. 1a–c relates only to technical aspects of the mobile environment. Each technical parameter is represented individually, and addresses specific technical support (energy, connectivity, security). We propose the notion of overall QoD as an aggregate measure of technical parameters as well as other factors depending on the user and the context of decision making. We visually represent the overall QoD using a single icon as shown in Fig. 1d and depict how it improves or deteriorates over time while connected or disconnected from the network (Fig. 1e). As shown in Fig. 1e, the overall QoD may deteriorate 5, 10, or 20 min from when the mobile is disconnected from the network; or 5, 10, 20 min away from the current location of the user; or 5, 10, 20 min from when data was last updated. If such visual representation is adopted in a mobile device, the user is made aware of the parameters that have been considered in the calculation of QoD. Thus, specific to the user, the decision-making context, and the mobile device used, the overall QoD will vary from user to user, from one decision context to another, from one location to another, or from one mobile device to another.

![](/api/attachments/3DY5G5RR/fulltext/images/b647a130ef9a663b27bc840f2ea9f775ce3c132c283b7bbfdf7618630b812787.jpg)  
Fig. 1. Some QoD indicators in mobile device (adapted from [8]).

Recent work on mobile decision support focuses on implementation of knowledge-based services on handheld computers [2,14]. Work on mobile clinical support systems, for example, addresses different intelligent decision support such as knowledge delivery on demand, medication consultant, therapy reminder [18], preliminary clinical assessment for classifying treatment categories [2,11], and providing alerts of potential drugs interactions and active linking to relevant medical conditions [3]. These systems also address mobility by providing intelligent assistance on demand, at the patient's bedside or on-site. Research on location-based mobile support systems uses search, matching and retrieval algorithms to identify resources that are in proximity to the location of the mobile users and that satisfy multi-attribute preferences of the users and the e-service providers. Examples of such location-based systems are those that recommend best dining options to mobile users [19], locate automatic teller machines nearby [14], and locate nearest speed cameras and intersections from GPS-enabled mobile devices. Most of these mobile support systems use intelligent technologies and soft computing methodologies (e.g., rule-based reasoning, rough sets theory, fuzzy sets theory, multi-attribute utility theory) as background frameworks for intelligent decision support. However, none of these systems address the issue of quality of data or quality of decision support while connected or disconnected from the network. In the sense that no aggregate measure of QoD has yet been proposed to support mobile decision making, our QoD framework can be regarded as novel and unique.

Outwith the area of mobile decision making, the importance of indicating the quality of information is a concept that has been explored in other areas of decision support. One area in particular where information quality is regarded as paramount is in the accuracy of database information [12]. Hill [5] provides a comprehensive review of the measurement of information quality and suggests that although recognised as significant in assessing the usefulness of any information provided, much of the existing research fails to capture a complete measure of quality. Hill proposes an information quality model that combines classifier effectiveness (overall classifier performance compared to real-world), pragmatic information quality effectiveness (performance independent of decision-making effect), semantic information quality effectiveness (quality of information in relation to the real-world), and actionability (which defines the extent to which an attribute influences decisions). To some extent, our QoD model depicted in Fig. 2 follows his strategy in explicitly recognising different contributing factors to the quality of information and applies it to the mobile decision support environment. In Fig. 2 we illustrate how QoD can be represented as an aggregate measure of technology-related parameters (e.g., energy, security, connectivity), user-related parameters (e.g., stability of scores or weights in user's decision model), and data quality parameters that are related to historical context (e.g., completeness, currency, accuracy of historical data). Some of these metrics can be calculated by comparing current data with standard data. For example, completeness of historical data can be considered as a fraction of complete, standard data needed to perform a triage preliminary assessment [16] Currency can be calculated based on current time and frequency of updates [2].

For example, when buying foreign currencies, the user can be better supported if he knows the current foreign exchange rates. In this case, currency of data may be considered as QoD parameter. In our search for parking example, validity of the data is another QoD parameter. We can also include the accuracy of predicted data, if such prediction can support the decision-making task at hand.

This view of overall QoD being influenced by different context changes on the mobile environment was first investigated by the authors in [15,16]. In these papers, we identified that user-related and technologyrelated contexts, as well as historical context should be addressed when representing the QoD for using data to support mobile decision making. By providing this multi-focused view of the decision we aim to provide our decision maker with a more complete picture of the factors influencing the outcome of the decision to be made.

![](/api/attachments/3DY5G5RR/fulltext/images/c6e8d955d5e4b36c13e3bcc7631523eca237f1f1c4b29c733cbf1cc54fb015a9.jpg)  
Fig. 2. A sample multi-context representation of QoD.

In the following section, we focus on user-related contexts influencing the overall QoD. In particular, we address the stability of the data provided. Stability refers to how constant score values and weight values remain over a given time period. We consider a choice problem while the user is on the move. We represent the user's choice problem as a MCDA model, and then consider stability of data as one QoD parameter. We discuss how stability of data may be measured and incorporated in the overall QoD.

## 3.1. User-related context

Fig. 3 depicts an example value tree used in Multiattribute Value Theory (MAVT) which is the MCDA approach the authors are most familiar with. The model represents a decision of which investment strategy to follow. In this decision model, the scores of alternatives against the given criteria can be static or dynamic.

## 3.1.1. Static scores

By static score, we refer to a score that does not change despite changes in the time, weather, network connection, or other context changes. For example, the company's profile (earnings, reputation, trader's reviews) is unlikely to change from 1 min to the next and can therefore be regarded as static. Obviously it is important to determine the likely time frame in which the decision will be made in order to categorise the score as being static or dynamic.

## 3.1.2. Dynamic scores

A dynamic score relates to an evaluation score that varies with changes in the mobile environment. Thus, a score that is not static is described as either unstable or dynamic. In our example, dividend yields is highly dependent on the current market situation, and therefore can change from 1 min to the next.

![](/api/attachments/3DY5G5RR/fulltext/images/51e7932a321dd85334c4d72748f032448ee8171c6832f811f891a7d77e80bcf0.jpg)  
Fig. 3. Model used to decide on where to invest money.

## 3.1.3. Stability of scores

When using a MCDA model to represent a choice problem in a mobile decision-making environment, it is important to indicate how static or dynamic score values are. Thus we provide a measure of stability referred to as the stability of scores.

One way to measure the stability of a score is to use a simple scale from 0 to 100, where 0 represents a dynamic value, 100 denotes a static value. For example, as shown in Fig. 4, the shaded bars on the left correspond to the evaluation scores of the alternatives against the “short term risk” criterion. Associated with each score, is a measure of stability of the score for the given time frame (e.g., 60 min). In Fig. 4, the stability of each score is represented by the bar on the right of the evaluation score. Thus, the “short term risk” of putting our money in a bank account (option D) is almost non-existent given the high-score it receives (100 being the best, 0 being the worst). In addition, this score is fairly static, meaning it is unlikely to change within a 60-min time frame. However, investing in option B: penny investments, is deemed to be quite risky, and the corresponding stability score indicates that this risk is relatively constant over time.

An overall stability of scores can be taken as a weighted sum of all stability scores after considering all criteria. The overall stability can reflect the stability or sensitivity of the decision outcome to fluctuations in the evaluation scores. For example, in the investment strategy decision, we would assess how the scores for each of the criteria in the model (depicted in Fig. 3) have fluctuated over a given time period and over a given number of criteria value updates. Supposing that the example shown in Fig. 4 reflects stability of scores for the criteria in a two hour time period, accessing updates every half hour. It is clear from Fig. 4, that option D has scores for each criteria that remain static over this time period. Option C however, clearly has criteria with fluctuating scores over this time period. By clicking on the stability bar associated with Option C, we can determine which criteria have fluctuating scores contributing to the instability of the option.

![](/api/attachments/3DY5G5RR/fulltext/images/b2a37a997d283f01a6c2eecf7d3e4c9b1cbc0fabdb9a9c20ee87fdcb54f86ee9.jpg)  
Fig. 4. Modelling stability of scores of alternatives with respect to “short term risk” criterion.

## 3.2. Overall Qod

Using the proposed multi-faceted representation of QoD, we can use the overall stability of scores and overall stability of weights as user-related QoD parameters. Depending on the context of decision making, some of the technical parameters may not be considered in the overall calculation of QoD, but can remain as separate considerations. Decision-making tasks requiring secured network connection, for example, can put upmost importance to security. The mobile user in this case might prefer checking the status of padlock icon before the decision-making task is initiated. This idea of QoD parameters is discussed further at the start of Section 3, and depicted in Fig. 2. As stated earlier, to reflect the importance of different QoD parameters, the system allows the user to weight the various parameters accordingly. So for example, if user-related QoD parameters are highly-significant in the investment strategy model, then a higher weight will be given to this parameter. Similarly, the weights given to the remaining parameters described in the model will be assigned to reflect the importance of each parameter.

Other application areas we have examined the use of a mobile DSS include mobile accounts management [2] and triage management [4]. The necessity and importance of the QoD measure, and the weightings assigned for each parameter of the model are very model dependent. For example, in the field of triage management, the need for access to up-to-date, accurate information while attending to an emergency scene is of paramount importance. In such a scenario, options that might be being considered may include the most appropriate means of transporting patients to hospital, or indeed, which hospital patients should be sent to. Here, the historical context criteria of completeness, currency, and accuracy can be seen to play an important role whereas factors such as the stability of weights may be less crucial, as the weights for the model are likely to remain constant.

## 3.3. Predicted overall Qod

By using some simple forecasting techniques, or more complex data-mining techniques, we can calculate a measure of how the QoD will fluctuate over time. For example, we can use simple moving average forecasting model to automatically calculate the validity of the data relating to parking space at the city, or predict the stability of short term and long term risk using time-series data of the stock price over the past year. Using moving averages, the average score for QoD of each alternative over a given number of updates is calculated. By assessing how these average values change over time, it is possible to predict the likely behaviour of values in the future. For example, the average values may appear cyclical in nature, linearly increase/decrease over time, remain fairly constant, or reflect an erratic system. Knowing the behaviour of previous values allows us to predict behaviour in the future.

## 4. Prototype mobile decision support system (MDSS)

The prototype was developed using an Object Oriented (OO) methodology, where unified modelling language (UML) was used to assist in conceptualising the design of the prototype. Although the DSS proposed is designed to operate on a number of mobile devices, this initial design is for use on a Personal Digital Assistant (PDA). The technologies used comprised of SuperWaba, Java, Excel, and Java Servlets.

The phases the mobile decision maker must complete are depicted in Fig. 5. Initially, the Decision Maker (DM) must create a MCDA value tree depicting the scenario being considered. Having developed this value tree (as shown in Fig. 3), the user then proceeds to enter their weights, which represent preferences in significance for each criteria. Thus far, the procedure replicates that performed when a static MCDA model is created. The next stage of the process however requires the user to stipulate the data source for the score values for alternatives for each criterion. Two options are currently provided:

## (i) Manual entry

If for a given criterion, the user chooses “manual entry” then for each alternative a score must be provided for the criterion. Such scores are regarded as “static” as they remain constant and are not updated over time.

(ii) Retrieved from website

If for a given criterion, the user chooses “Retrieve from website” then the user must:

• Provide the address of the website where the scores will be retrieved from

• Specify how the values on the website should be translated to a scale between 0–100 thus normalising all values attained

• Specify how frequently the website should be accessed to retrieve data

• Provide an initial evaluation of how static/ dynamic they expect the scores for a criterion to be. This static/dynamic grade will be re-evaluated over time as the system monitors how score values fluctuate.

The MCDA model created by the decision maker is saved onto a server machine. In addition, details are saved relating to the websites to be parsed for update information, and how often this information should be retrieved. Server side software then dissects the model and parses the information and refresh frequency details and saves this information into database tables. A threaded server-side process then checks at regular intervals to ascertain if any of the database dynamic criteria needs refreshing, and if so, the relevant website is contacted and the pertinent data values retrieved. The value retrieved and success of connectivity/retrieval of the data is recorded and contributes to the calculation of the QoD score.

![](/api/attachments/3DY5G5RR/fulltext/images/c1c133fdc85169549a2a52f54f27ba468b168a5c5f3d71ed38d2d40659e9296e.jpg)  
Fig. 5. Phases involved in setting up mobile decision model.

Having completed the MCDA model and data retrieval information, the MCDA model can then be loaded onto the PDA and is ready for use by our mobile DM. It is feasible that the person designing the overall MCDA model may be a different person to the mobile DM. Thus it is conceivable that pre-existing models designed by MCDA specialists can be downloaded by a mobile DM and tailored to their requirements. This would allow base MCDA models to be available to mobile DMs to access and adjust as required, thus alleviating the need for new models to be created for a given scenario from scratch.

The interface that has currently been adopted for the prototype is shown in Fig. 6(a–c). The interface developed is undergoing constant revision, however, the current version is seen to provide sufficient functionality to potentially aid a mobile DM. The lower part of the screen provides the overall ranking of the alternatives, A–D that are being considered. It is clear to see from this that alternative A (Blue Chip Co.) is currently the best option. However, it is also crucial that the DM takes into account the QoD score (top left Fig. 6a) and the predicted QoD score over time (top right Fig. 6a). The current QoD indicates that the quality of the data is relatively good. However the QoD score over time shows that the quality of the data will deteriorate.

Should the DM wish to find out more about the QoD score, by clicking on the QoD info button they are taken to the screen depicted in Fig. 6b. This screen allows the DM to analyse the quality of the data concerning the main three criteria used in constructing the QoD score (as shown in Fig. 2). From Fig. 6b we can clearly see that it is the technology-related issues that have poor quality (so for example, perhaps we are unable to connect to the specified URLs as frequently as requested due to poor network connection). The user also has the ability to drill down further and analyse the factors contributing to the QOD scores for user-related, technology-related, and historical contexts.

Returning to the main DM screen, the user can also click on the weights button and review current weights applied at the top-level of their tree. Fig. 6c shows the current weights applied to the top-level criteria in our model. By manipulating the weight bars, the DM can interactively see the effect this has on the ranking of alternatives.

## 5. Future work

In our ongoing research, we are investigating different graphical methods for representing the suitability and ranking of alternatives. Recent work [6] on static decision making has addressed the issue of visual interactive displays and proposed the use of a triangleplot. This approach, although not completely new to

![](/api/attachments/3DY5G5RR/fulltext/images/41eb1d4fb5f32a745e32331ad965f337779dfa859d012dffb93a3dbecbabbb4d.jpg)  
Fig. 6.

![](/api/attachments/3DY5G5RR/fulltext/images/3db0b3796d138420089fae2cea090550a38ea73aa1050362907814ec719419d3.jpg)  
Fig. 7. Visual interface for the “investment strategy” problem.

MCDA [9], is novel in terms of development of the interface to support the MAVT approach, and evaluation through use of case studies. Results from such studies have suggested that the plot is useful in investigating model robustness, and providing holistic data concerning the decision model. The triangle-plot depicted in Fig. 7 shows the robustness of the decision under different weight choices.

Such a display could possibly alleviate the need to investigate weight changes further (as shown in Fig. 6b). The model focuses on the top 3-criteria of our ‘investment strategy’ model as shown in Fig. 3. Depending on the importance placed on each of the three criteria, the shaded triangle in Fig. 7 indicates which alternative is the “best” one to go with. So for example, a high weight placed on “Ethical Stance” indicates that option D: bank account is our best option, while a high weight on “Company Profile” (where we are not duly concerned about ethical investing and return potential) indicates option A: Blue Chip is the best option.

## 6. Conclusions

Our recent work on mobile decision support is based on our view that the mobile decision maker will be better supported if our decision maker is aware of the QoD used in deriving the decision and how it improves or deteriorates over time. In this paper, we represented the user's decision problem as a multicriteria decision analysis model with dynamic as well as static attributes. Static attributes are those attributes that do not vary with context changes (e.g., changes in time, weather, network connectivity, network security, location, etc.), while dynamic attributes are those that are prone to change over a given time period. We considered the overall stability of evaluation scores and overall stability of criteria weights to capture these static and dynamic attributes of the decision model, and considered them as user-related QoD parameters. We also suggested providing a predicted measure of overall QoD over time to further inform the user of likely changes in QoD and their impact on the decision outcome. We briefly touched on the area of sensitivity of decision outcome to changes in evaluation scores or changes in criteria weights. When presented simultaneously to the mobile decision maker, we believe a triangle-plot that displays the user's decision model and a QoD indicator (such as QoD bar or QoD graph) can inform the user of the sensitivity of the decision to changes in evaluation scores or criteria weights, and may indicate robustness of the decision.

In the ongoing research we plan to investigate further the potential benefits in providing QoD models for supporting mobile decision making. QoD models for specific decision-making scenarios will be considered. We are currently exploring how the proposed QoD framework may be implemented to support triage in emergency departments [17]. Case studies will also be conducted to determine if our visual displays of the user's decision model and QoD model have an impact on the user's decision-making capability, and how they may be best implemented to achieve the desired level of decision support. The other issue to be addressed is a possibility of populating some of the dynamic parameters automatically using context-aware applications [13].

## Acknowledgement

This research is partly funded by Monash University, Stirling University, The Carnegie Trust for Scotland and The Nuffield Foundation. The authors would like to acknowledge contribution from Dr Jocelyn San Pedro in her capacity as a Research Postdoctoral Fellow at the Monash University Knowledge Management Research Program to the earlier draft of this paper.

## References

[1] V. Belton, Multiple criteria decision analysis, practically the only way to choose, in: L. Hendry, R. Eglese (Eds.), Operational Research Tutorial Papers, 1990, pp. 53–101.

[2] F. Burstein, J. San Pedro, A. Zaslavsky, J. Hodgkin, Pay by cash, credit or EFTPOS? Supporting the user with mobile accounts Manager, Proceedings of the 3rd Mobile Business Conference, M>Business Conference, New York, USA, 12th – 13th July, 2004.

[3] A. Chan, WWW+ smart card: towards a mobile health care management system, International Journal of Medical Informatics 57 (2000) 127–137.

[4] J. Cowie, P. Godley, Decision support on the move: mobile decision making for triage management, 8th International Conference on Enterprise Information Systems, 23rd–27th May, 2006.

[5] G. Hill, An information-theoretic model of customer information quality, Proceedings of the Decision Support Systems Conference, Prato, Italy, July 1–3, 2004, CD ROM.

[6] J. Hodgkin, V. Belton, Development and evaluation of two decision support systems to provide intelligent user support for multicriteria decision making, in: T. Bui, H. Sroka, S. Stanek, J. Goluchowski (Eds.), Proceedings of the 7th International Conference of the International Society for Decision Support Systems: DSS in the Uncertainty of the Internet Age, The Karol Adamiecki University of Economics, Katowice Poland, Ustron, Poland, 2003, pp. 201–204.

[7] J. Hodgkin, B. Malyon, A. Morton, An introduction to two group decision support systems, Keynote/Tutorial paper of 10th Young Operational Research Conference, University of Surrey, Guildford, 1998.

[8] J. Hodgkin, J. San Pedro, F. Burstein, Quality of data model for supporting real-time decision-making, Proceedings of the 2004 IFIP International Conference on Decision Support Systems (DSS2004), July 1–3, 2004, Monash University, Melbourne VIC Australia, 2004, pp. 372–380, Prato, Italy (CD ROM).

[9] J. Hodgkin, V. Belton, K. Koulouri, Supporting the intelligent MCDA user: a case study in multi-person multicriteria decision support, European Journal of Operational Research 160 (1) (2005) 172–189.

[10] E.G. Malah, Decision Support and Datawarehouse Systems, McGraeHill, 2000.

[11] W. Michalowski, S. Rubin, R. Slowinski, S. Wilk, Mobile clinical support system for pediatric emergencies, Decision Support Systems 36 (2003) 161–176.

[12] F. Naumann, C. Rolker, Assessment methods for information quality criteria, Proceedings of the 2000 Conference on Information Quality, Cambridge, MA, 2000.

[13] A. Padovitz, A. Zaslavsky, S.W. Loke, B. Burg, Maintaining Continuous Dependability in Sensor-Based Context-Aware Pervasive Computing Systems, Hawaii International Conference on System Sciences (HICSS38), IEEE Computer Society, Los Alamitos, CA USA, 2005.

[14] V. Roto, Search on Mobile Phones, 2003 [on line] URL http://home. earthlink.net/∼searchworkshop/docs/RotoSearchPositionPaper. pdf, Accessed 11 Nov 2003.

[15] J. San Pedro, F. Burstein, A. Zaslavsky, An approach to sensitivity analysis for data quality assessment in mobile decision-making,

in: T. Bui, H. Sroka, S. Stanek, J. Goluchowski (Eds.), Proceedings of the 7th International Conference of the International Society for Decision Support Systems: DSS in the Uncertainty of the Internet Age, The Karol Adamiecki University of Economics, Katowice Poland, 2003, pp. 323–332.

[16] J. San Pedro, F. Burstein, L. Churilov, J. Wassertheil, P. Cao, Intelligent Multiattribute Decision Support Model for Triage, Information Processing and Management of Uncertainty in Knowledge-Based Systems, Perugia, Italy, Information Processing and Management of Uncertainty in Knowledge-Based Systems (IPMU2004), Editrice Universita La Sapienza, Rome, Italy, 2004, pp. 1559–1566.

[17] J. San Pedro, F. Burstein, J. Wassertheil, N. Arora, L. Churilov, A. Zaslavsky, On development and initial evaluation of prototype mobile decision support for hospital triage, Proceedings of the 38th Annual Hawaii International Conference on System Sciences (HICSS'38), IEEE Publication, 2005, CD ROM.

[18] C. Spreckelsen, C. Lethen, I. Heeskens, K. Pfeil, K. Spitzer, The Roles Of An Intelligent Mobile Decision Support System In The Clinical Workflow, 2000 [on line] URL citeseer.nj.nec.com spreckelsen00roles.html, Accessed 11 Nov 2003.

[19] G. Tewari, J. Youll, P. Maes, Personalized location-based brokering using an agent-based intermediary architecture, Proceedings of the International Conference on E-wCommerce, Seoul, Korea, 2000.

![](/api/attachments/3DY5G5RR/fulltext/images/82e89793fb0d41c3b463597d08aeaaa2247c8aaa8de855f2d23f217bd0774319.jpg)

Julie Cowie is a lecturer in the Department of Computing and Maths at Stirling University, UK. She holds a BSc. (Hons 1st class) from Stirling University in Computing Science with Maths and Ph.D. in Operational Research from Strathclyde University, Glasgow, UK. She has been an active researcher in the area of decision support systems

and the provision of intelligent decision support for the past 10 years. Currently, she supervisors 2 Ph.D. students and 1 research fellow who are involved in research in the use of such systems in diverse application areas. Dr Cowie's current research interests include the use of evolutionary techniques in decision support and the use of support systems in the healthcare domain.

![](/api/attachments/3DY5G5RR/fulltext/images/b1bb0ab27db7b8c2b47099517b2e5fea0373fce8d3d42d7e41b0c94a7328b837.jpg)

Frada Burstein is an Associate Professor in the School of IT at Monash University in Melbourne, Australia. She holds a Masters of Sci (applied Math) from Tbilisi State University from Georgia, USSR (1978) and PhD in Technical Cybernetics and Information Theory from the Soviet Academy of Sciences (1984). She researches and teaches in the areas of knowledge management and decision support systems

at Monash University since 1992. At Monash University she has established and leads a Knowledge Management Research Program including an industry sponsored virtual laboratory for studying modern technologies for supporting knowledge creation, storage, communication and application. Her current research interests include knowledge management technologies, intelligent decision support, cognitive aspects of information systems development and use, organisational knowledge and memory, systems development research.
