---
otero_id: 7178
otero_key: "MJUYK8EB"
title: "Assisting decision making in the event-driven enterprise using wavelets"
authors: "Stephen Russell; Aryya Gangopadhyay; Victoria Yoon"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2008.04.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Assisting decision making in the event-driven enterprise using wavelets

Stephen Russell ⁎, Aryya Gangopadhyay, Victoria Yoon

Department of Information Systems, University of Maryland Baltimore County, Maryland, USA

## a r t i c l e i n f o

Article history: Received 28 July 2006 Received in revised form 22 April 2008 Accepted 27 April 2008 Available online 10 May 2008

Keywords: Decision analysis Decision support systems Visualization Wavelets

## a b s t r a c t

This paper discusses issues related to data-driven decision support systems in event-driven enterprises and proposes Discrete Wavelet Transformation (DWT) as a method to improve these systems. DWT is proposed as a method of data reduction that reduces the effects of excessive data, enabling better visualization and scalability, while preserving patterns, trends, and surprises in the data. A procedural model for using a data-driven decision support system that integrates DWT is presented. Finally, the procedural model is evaluated in experiments based on real event-driven data from a large telecommunications company.

© 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

Business Activity Monitoring (BAM) has emerged as a dominant application solution for real-time, event-driven, measurement and monitoring. BAM extends enterprise system usage from strategic and tactical business decision making, to the management of day-to-day business operations [59]. BAM draws its information from multiple transaction processing systems and other internal and external (inter-enterprise) sources, enabling a broader and richer view of business activities [33]. The implementation of BAM technologies generates high volumes of data at a rapid pace that are closely linked with businesses' core operational processes. The richness and volume of this data provides a valuable asset to decisionmakers; however, it has caused decision making in this environment to be complicated and challenging.

The presence of massive data sets can cause serious problems in an organization's decision support systems [28]. A large volume of data obscures patterns, trends, surprises, and other important features. Visualizing data helps decisionmakers to discover patterns and trends, improving the ef<sup>fi</sup>ciency and effectiveness of the decision-maker [50].

However, visualizing the full range of large data is often infeasible. Moreover, common management software such as spreadsheets and word processors are limited in their ability to contend with excessive amounts of data, which forces decision-makers to learn and use specialized tools. Exploration, manipulation, and analysis become more complicated and resource consuming as data set sizes increase. Subsequently decision-makers' ability to <sup>fi</sup>lter, synthesize, and utilize data decreases [10]. In the event-driven enterprise, the speed that data arrives and in which decisions are expected exacerbates the problem of excessive data. Excessive data can cause decision-makers to sample data, or randomly select variables/values, negatively in<sup>fl</sup>uencing the decision making process and subsequently reducing decision quality [1].

Discrete wavelet transformation is a mathematically proven technique for data reduction [21]. Traditionally used in signal processing [29] and data compression [34] applications, wavelets effectively reduce the volume of data with minimal loss of resolution. The ability to compress data without loss of utility for analytical purposes provides direct improvements to the issues of scalability and visualization [24]. Despite the bene<sup>fi</sup>ts that wavelets have demonstrated in other domains, little research has been done in applying wavelet methodologies to management decision support applications.

The objective of this paper is to present wavelets as a viable alternative for dealing with a large volume of data and thereby improving decision-makers' ability to make highquality decisions in event-driven environments. We have developed a procedural model describing how discrete wavelet transformation (DWT) can provide data reduction, without loss of feature characteristics and subsequently improve exploratory visualizations of decision related data. This procedural model is implemented to aid a real world decision problem based on event-driven data, faced by a large telecommunications provider. The paper is organized as follows: Section 2 provides a brief background of BAM and event-driven enterprises. Section 3 presents prior research related to this work, and Section 4 presents the procedural model and experimental methodology. In Section 5, the empirical evaluation of the procedural model is presented, followed by a discussion of the results in Section 6. Finally, we conclude with a summary and future work.

## 2. Background

Fig. 1 shows a typical BAM system implementation. Data from a variety of enterprise sources is integrated in real-time for analysis and event-noti<sup>fi</sup>cation delivery to users. Because most BAM implementations are real-time systems, BAM must collect, store and manage large volumes of variant, mostly time-series data. For example, users de<sup>fi</sup>ne sophisticated events that occur within a production process; alerts are triggered when those events fall outside of prede<sup>fi</sup>ned parameters and are delivered to desktop or handheld devices, enabling rapid decision making and crisis management. Relevant data accompanies each alert (such as, historical trending data, test results, or data on path traveled), enabling users to proactively review the data, assess the issue, and make critical decisions to manage the event. The range of data at the bottom of Fig. 1 shows the increasing demand on managers to contend with high volumes of data in their decision making processes.

In event-driven environments processing and utilizing entire sets of data can be a challenge for decision making. Productivity may actually decline, as more data is made available to decision-makers. Large sums of data have a secondary effect on decision making: increased dif<sup>fi</sup>culty analyzing data across the breadth of the entire data set. Massive amounts of data encourage decision-makers to use cognitive simpli<sup>fi</sup>cation processes and heuristics that may lead them to ignore relevant data or process incorrect data. Alternatively, decision-makers may seek to reduce cognitive effort by relying on perceptual processes [5]. By examining discrete or sampled measures, potentially critical bits of data are obscured or decisions makers are mislead by the sampled selection. Speier and Morris [44] cite several empirical bodies of work that indicate excessive data results in decreased decision quality, increased decision time, and increased confusion for the decision-maker.

## 2.1. Wavelet transformations

Managing excessive data is a challenging problem. A common method of addressing this problem is the use of data reduction techniques. The problem of massive data and the need for automated data reduction or summarization are familiar to any user of large databases. What users want is the ability to rapidly scan through data looking just for the events or information of interest [60]. In domains outside of decision support, wavelets have been used for data reduction (compression) in image analysis, signal processing, GIS applications, and statistics, among other areas.

![](/api/attachments/MJUYK8EB/fulltext/images/35f0ed43f3ac1cd9aa09a44027fec818c01c1042a8a1a3953145c116c5425ae1.jpg)  
Fig. 1. Business Activity Monitoring (BAM) system diagram.

Discrete wavelet transformation (DWT) divides data, functions, or operators into different frequency components and then studies each component with a resolution matched to its scale [12]. A wavelet can have many desirable properties such as compact support, vanishing moments and dilating relation and other preferred properties such as smoothness and being a generator of an orthonormal basis of function spaces $L ^ { 2 } ( R ^ { n } ) [ 2 7 ] .$ The core idea behind discrete DWT is to progressively smooth the data using an iterative procedure and keep the detail along the way. The DWT of [X ] is an orthonormal transform such that $\mathrm { i f } \left[ W _ { n } ; n { = } 0 , { \ldots } N { - } 1 \right]$ represents the DWTcoef<sup>fi</sup>cients, then W=HX where W is a column vector of length 2<sup>i</sup>, whose nth element is the nth DWT coef<sup>fi</sup>cient of $W _ { n } ,$ H is a $N { \times } N$ real-valued matrix such that $H H ^ { T } { = } I ,$ where I is the N×N identity matrix, and X is a vector of values $X _ { 0 } , . . . , X _ { N - 1 } .$ Furthermore, orthonormality implies that $\pmb { X } \mathrm { = } H ^ { T } \mathbf { W } ,$ and $\| \mathbfcal { W } \| ^ { 2 } = \| \mathbf { X } \| ^ { 2 }$ . The nth wavelet coef<sup>fi</sup>cient $W _ { n }$ is associated with particular scale and a particular set of times. One of the simplest wavelets is the Haar wavelet. A Haar-based DWT produces an approximation coef<sup>fi</sup>cient and a difference or detail coef<sup>fi</sup>cient for each pair in the distribution being transformed as shown in Eq. (1).

$$
C _ {\text { appx } _ {i}} = \frac {x _ {i} + x _ {i + 1}}{\sqrt {2}}, C _ {\text { diff } _ {i}} = \frac {x _ {i} - x _ {i + 1}}{\sqrt {2}}\tag{1}
$$

DWT characteristics (data reduction, smoothing, and feature enhancement) indicate a potential to address aspects of the excessive data issue and subsequent scalability limitations of BAM systems. The data reduction provided by DWT may also facilitate better visualization, making patterns, trends, surprises, and relationships easier to identify. By utilizing the wavelet-transformed data for visualization, decision-makers should be able to explore larger amounts of data in a single view without sampling. This broader view of the data may also stimulate or trigger positive intuitive decision making behaviors; sometimes scanning all relevant data can help decision-makers extract similarities among events and hence inspire hypotheses [40].

## 3. Prior research

A signi<sup>fi</sup>cant amount of research has applied data reduction techniques to meet the challenge of very large data sets. Much of the work in the area of data reduction has been done in the database domain. Because the current state-of-the-art for event-driven systems is rooted in the evolution of data warehouses and data mining, it is appropriate to examine data reduction approaches from this perspective. In database research, data reduction is closely linked to approximation, aggregation, and sampling. The emphasis in this work has been on getting quick approximate answers from databases. Data reduction techniques can be divided into two distinct categories: parametric techniques that assume a model and non-parametric techniques that do not assume a model. Characteristics of parametric and non-parametric data reduction techniques have been examined thoroughly in the work of Barbara et al. [4]. Frequently in event-driven environments, an appropriate model does not exist that can aid the decisionmaker with an unstructured event-related decision opportunity. As a result, the focus of this section is on non-parametric data reduction methods.

There has been extensive work on data sampling [11,38,58] and it is one of the simplest, most common, data reduction techniques used in decision support. Most data sampling techniques are based on statistical methods, such as simple random sampling, strati<sup>fi</sup>ed sampling, cluster sampling or based on adaptive methods such as adaptive sampling [28]. Despite the many bene<sup>fi</sup>ts of sampling approaches, it has an intrinsic problem. The purpose of sampling is to obtain a reduced data set that represents the full population. In most cases, sampling will extract a subset of the full range of data. This is particularly problematic in environments where an appropriate model has yet to be de<sup>fi</sup>ned because it can lead a decision-maker to incorrect assumptions if the sample is not representative of the complete population. Fundamentally, the problem with sampling is that it may obscure a relevant pattern or feature. This is the same issue with traditional aggregation-based data reduction approaches such as averaging or clustering. Hidden patterns and features are of particular emphasis in the context of visualization. Visualizations should be designed so that they lead the viewer to make inferences consistent with those that would be reached by more thorough analysis of the underlying data [6,24,39,52].

Another data reduction method, factor analysis, is used to analyze interrelationships among a large number of variables and to explain these variables in terms of their common underlying dimensions or factors [15]. A basic method in factor analysis is Principal Components Analysis (PCA), which projects the vectors into a lower-dimension linear space, and treats the projection, called a principal component, as a method of data reduction. In the statistical domain, there has been a great deal of research utilizing PCA as a method of reducing data and explaining variance. Kargupta et al. [22] used PCA to aid feature selection, for data-mining activities in noisy mobile environments. Microsoft Research [51] has also investigated applications of PCA integrating a probabilistic model for the observed data. While popular, PCA suffers from two problems that wavelets may address. PCA is primarily used as a dimensionality (columnar) reduction approach. It is inappropriate to use PCA to reduce the number of rows of data. PCA also obtains its data reduction by eliminating columns. As a result, data potentially bene<sup>fi</sup>cial to the decision-maker may be removed. Secondly, PCA is computationally intensive, limiting its bene<sup>fi</sup>t with data containing large numbers of dimensions.

Compared to PCA, aggregation, and sampling, wavelets have several attractive characteristics that may make it appropriate for data reduction in decision support applications. Wavelets provide data reduction with minimal loss of features, can be used to create multi-resolution views [29], and can be reconstructed from its reduced wavelet coef<sup>fi</sup>cient form with few computational resources. Additionally DWT has been shown to be complimentary to other data reduction methods. Piovoso and Kosanovich's [37] work on process-monitoring has shown DWT to be complimentary to PCA. Guo et al. [14] integrated DWT with Fourier transformations to combine noise <sup>fi</sup>ltering and data reduction in the time domain for the prediction of stocks. Guo used Fourier transformations to reduce the data's dimensionality and wavelets were used to “denoise” the data.

It is important to note other prior applications of wavelet transformations. Wavelet transforms have been used in database optimization in various ways. These include selectivity estimation using wavelet-based histograms [31,32], approximate query processing in relational and multi-dimensional databases [53,54], clustering (WaveCluster) [42,43], similarity searches in time series databases [8,47,48], and similarity search in image databases [55–57]. The work on wavelet-based histograms and approximate query processing utilized thresholding to reduce the number of coef<sup>fi</sup>cients and hence achieve reduction in data size. In WaveCluster, the data is partitioned by a grid and wavelet transform is applied to the quantized feature space to obtain a multi-resolution data representation. Wavelets have also been used in fast computation of similarity measures in time series databases and been applied to image databases to extract compact feature vectors.

In addition to data reduction, wavelets have other characteristics that make them more desirable for event-driven data applications than other reduction techniques such as singular value decomposition (SVD), discrete Fourier transformations (DFT), Principal Component Analysis (PCA), and random projection. These characteristics consist of processing complexity (time ef<sup>fi</sup>ciency), retention of time-related characteristics (temporal semantics), multiple time resolutions (multi-scale time domain), and the ability to <sup>fi</sup>nd abrupt changes in data (bursts). Table 1 summarizes the results of research [3,7,30,35] comparing DWT with the other methods.

Despite this apparent potential, surprisingly the literature regarding wavelet-based methods in decision support is sparse. Excluding data compression, the literature on DWT has primarily focused on scienti<sup>fi</sup>c applications identifying subtle deviations and trends in radio frequency signals that are not otherwise visible. Data gathered in business applications are generally not considered comparable to signals from scienti<sup>fi</sup>c or engineering measurements. However, it is possible to draw some similarities. For example, in signal processing, data signals are treated as a mixture of high and low frequency components, where the high frequency component corresponds to noise and the low frequency component is taken as the general morphology of the signal. In decision support, there is no concept that corresponds to “noise” in signal processing. In this paper we use the high frequency components as short-term deviations and low frequency components as long-term trends. Decision makers can use these two components to determine both the general direction (trend) of business data as well as subtle changes occurring at speci<sup>fi</sup>c time periods. Moreover, such patterns can be traced at various temporal resolutions. These temporal resolutions can provide the basis for summary views of the data, reducing users' cognitive load to process the information. The literature surrounding DSS-related information overload concentrates on users' cognitive abilities and information <sup>fi</sup>ltering techniques. Advances in both areas have largely remained separate. Research integrating these two areas would enhance current approaches in data-driven DSS generally, and event-driven systems speci<sup>fi</sup>cally.

Comparison of transformation techniques

<table><tr><td></td><td>SVD</td><td>Random projection</td><td>PCA</td><td>DFT</td><td>DWT</td></tr><tr><td>Time efficiency</td><td>Slowest</td><td>Slow</td><td>Slow</td><td>Fast</td><td>Fastest</td></tr><tr><td>Temporal semantics</td><td>High</td><td>Low</td><td>High</td><td>Low</td><td>High</td></tr><tr><td>Multi-scale time domain</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr><tr><td>Handle bursts</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

The effects of information load, feature detection, and decision support have garnered a great deal of attention in the visualization domain and it is important to discuss relevant existing work in this area. Schkade and Kleinmuntz [41] found that information format had a signi<sup>fi</sup>cant effect on the decision process when used during information acquisition. Larkin and Simon [26] found that visualizations were superior representations to text-based ones. They concluded that if a user is capable of using visualizations to acquire information, visualizations seem to support more ef<sup>fi</sup>cient computational processes than their text-based counterparts. Cognitive information load research <sup>fi</sup>nds that volumes of data can inhibit assimilation of information in either format, visual or text-based [40].

Particularly in the analysis of business-related data, commonly used visualization methods such as two-dimensional charts have several shortcomings. Relationships can be obscured, hidden attributes may require extensive processing to be made available, and interpretation may cause ambiguity [20,50,52]. Kumar and Benbasat [25] have extended this research showing that both 2D and 3D visualizations can obscure relationships and make interrelation dif<sup>fi</sup>cult. All of these issues are compounded by large quantities of data. Large amounts of data are dif<sup>fi</sup>cult to visualize in a usable manner [18]. Prior research has demonstrated that visual representation of data is often oversimpli<sup>fi</sup>ed or data is too detailed to provide adequate visual representation [49]. The issue of using simple methods of visualization has resulted in the development of many innovative visualization methods such as the circle view method [23], multi-dimensional scaling [61], and visFlowConnect [62]. While innovative, these methods are often complex and deviate from commonly accepted data presentation methodologies. For example, some more complicated visualizations like the circle view [23] can require training on how to use the technique. Despite the limitations of simple 2D charts, they remain a staple of business analytics. In the next section, we discuss the DWT methods applied to traditional visualizations.

## 4. Procedural model

BAM ful<sup>fi</sup>lls a critical business need by providing real-time visibility into hot spots across an enterprise and access to related data that can potentially help managers make the right decisions [16]. Despite the bene<sup>fi</sup>ts of BAM systems, their very nature exacerbates the problem of excessive data, challenging common analytical and visualization techniques. Advanced information systems, with their increasing volume of data and complexity, can simply overwhelm the decision-maker.

More than ever, decision-makers have access to a larger range of relevant and potentially irrelevant data. BAM systems address the issue of application and information integration in the event-driven enterprise, but decision-makers must still investigate the details of any events that occur outside of the normal or expected range. In this regard, the decision opportunity is most often semi-structured and the decisionmakers' analysis is exploratory in nature. The data in the eventdriven environment is mostly temporal and naturally ordered, making it particularly suitable for discrete wavelet transformations [36]. To provide a solution to the excessive data problem in this context, it is necessary to de<sup>fi</sup>ne a method that supports traditional decision support analysis techniques such as On-

Line Analytical Processing (OLAP), visualization, and correlation. A successful solution should not preclude access to the original data and should integrate non-intrusively with the existing BAM processes and architecture. Our work proposes a new procedural model incorporating DWT into the decision making process. Fig. 2 illustrates this model.

The purpose of the procedural model is to integrate DWT as a method to improve managers' ability to explore data and help identify relevant decision variables and information. While not particularly highlighted by the model shown in Fig. 2, DWT data is the basis for the visualization and decision analysis inputs; the contributions of DWT are shown in steps 4, 5, 6, and 7. It is important to note that the DWT data is not a 100% replacement for the original data. The original data is still available to the decision-maker as shown in the data warehouse block. However, the DWT data is used to aid the formulation of the problem. The procedural model does not supersede traditional decision support approaches; instead, the intention is to augment it. To illustrate, the procedural model includes visualization and variable selection that allows users to interact visually with the wavelet coef<sup>fi</sup>cients at multiple levels of resolution in a manner similar to online analytical processing (OLAP) methods. Additional details on the implementation of the multi-resolution “OLAP-like” views will be provided below. Fig. 2 depicts a series of steps in the procedural model. The following describes the activities at each step/block of the procedural model.

(1) Operational activities trigger transactional events. The events are captured or tracked as operational data in online transaction processing systems.

(2) Operational data is transformed using DWT. Multiple transformations of the data at different resolutions may be generated.

(3) Transformed data is stored with the original data, in a data warehouse.

(4) The content of the data warehouse is used for event rules and analysis queries. Multi-resolution visualizations of large data sets are available to the user and can be used for data exploration.

(5)/(6) Decision support is provided by visual inspection of the wavelet coef<sup>fi</sup>cients as well as other analytical techniques such as seasonal <sup>fi</sup>ltering, identi<sup>fi</sup>cation of structural breaks, and multi-scale cross-correlation using the wavelet coef<sup>fi</sup>cients.

(7) From the multi-resolution view, a decision-maker can focus on a targeted area of interest, with the ability to return to the multi-resolution view. In this exploratory procedure, the DWT data is returned from queries of the data warehouse or through the event rule logic.

(8) Information gained from the data exploration and analysis can be used for decision opportunity identi<sup>fi</sup>cation or problem formulation.

Consider the following example. A BAM system collects events at one-minute intervals (1). Each day 1440 data points would be generated (2). An event occurs that presents a potential decision opportunity. For purposes of discussion, assume there is a cyclic, quarterly, seasonal pattern in the data that would occur naturally and there is no prede<sup>fi</sup>ned model to <sup>fi</sup>t this problem. That pattern would manifest in 172,800 data points. If there are inter-day <sup>fl</sup>uctuations, the cyclic pattern may be obscured by the local <sup>fl</sup>uctuations. The operational data is transformed and stored with the original data (3). Alerts and noti<sup>fi</sup>cations are generated (4). A decisionmaker who is tasked with addressing the decision opportunity could utilize both the original data and the transformed data for a variety of analysis (5, 6, and 7) leading to problem formulation or opportunity identi<sup>fi</sup>cation (8).

The wavelet-transformed data would allow the decision maker to explore a larger volume of data for analytical purposes. Given the data set in the example (1440 points per day), a decision-maker may have dif<sup>fi</sup>culty visualizing the full range of data with common of<sup>fi</sup>ce software such as Microsoft Excel, particularly if there are many local <sup>fl</sup>uctuations. As a result, the decision-maker would be forced to use specialized software tools, sample, or summarize in order to explore the data. These approaches have limiting effects. Specialized software requires a learning curve; sampling can create inappropriate judgment bias and summarization can obscure relevant details.

DWT-based multi-resolution views directly address these limiting effects. In the procedural model above, we employ visualizations (6) based on the DWT data rather than the raw data. From this, we expect to see two bene<sup>fi</sup>ts; the <sup>fi</sup>rst is a clearer picture of the trends in the data, due to the data reduction, without loss of features. This is due to the superior approximation properties of wavelets [46]. The second bene<sup>fi</sup>t can be found in the DWT's separation of signal/trend and noise/ <sup>fl</sup>uctuation and subsequent multi-resolution views, based on the separated coef<sup>fi</sup>cients. Prior research has shown that graphs mitigate the effects of interruptions on complex symbolic tasks [45], improve performance on dynamic decision making tasks in which earlier decisions affect subsequent ones [2], and help managers deal effectively with large data sets [9].

![](/api/attachments/MJUYK8EB/fulltext/images/06ae8de9acda97da05ab1fe7faee39bb29729e339c70d5880c39791c9741345f.jpg)  
Fig. 2. Procedural model.

Visualizations of the DWT data are simpli<sup>fi</sup>ed because of the data reduction. The time span would also be compressed, allowing views at different time resolutions; enabling drill down effects within a single presentation. In this context, the DWT approximation coef<sup>fi</sup>cient would show trends and the detail coef<sup>fi</sup>cient could be used to identify <sup>fl</sup>uctuations, surprises, or exceptions at different resolutions. Each resolution is based on one or more transformations. Consider events occurring on a single day interval over the course of a annual quarter (120 data points).

Fig. 3 represents a multi-resolution view of the detail/ <sup>fl</sup>uctuation data coef<sup>fi</sup>cients, as described in step 6 of the procedural model. This view shows surprises in the data series by utilizing the noise portion of the DWT at three different levels of decomposition. Different features of the data are captured at different levels of decomposition. For example, the level 1 decomposition (shown at the top of Fig. 3), shows the <sup>fl</sup>uctuations occurring over a period of two consecutive, nonoverlapping (CN) days, level 2 (middle plot) shows <sup>fl</sup>uctuations over four CN day periods, and level 3 (bottom plot in the <sup>fi</sup>gure shows <sup>fl</sup>uctuations over eight CN day periods — a weekly approximation. The multi-resolution view shown in Fig. 3 is similar to what would be achieved by a typical OLAP drill down analysis, where the decision-maker starts at the highest level of hierarchy and drills down to successively lower levels of detail. In our procedural model, the process of multi-resolution view is bottom up, where the highest resolution picture is shown <sup>fi</sup>rst and then successively rolled up to coarser levels of resolution. While this discussion emphasizes the improvements in visualization that wavelets can provide, the procedural model also includes other analysis techniques such as correlation, variance analysis, and statistical methods.

The procedural model is intended to augment an existing DSS architecture. To easily integrate with existing DSS, the introduction of wavelet data is done in a manner that is not intrusive to existing DSS functionality. BAM and other datadriven DSS have a database or data warehouse that supply decision related data to support the intelligence and design phases of decision making. Utilizing the procedural model, this data is transformed using DWT in a preprocessing step.

![](/api/attachments/MJUYK8EB/fulltext/images/eee37a63726b0eea5dfafd1e50e0356c11b35f0bd78ba42fa418842b9f9fa958.jpg)

![](/api/attachments/MJUYK8EB/fulltext/images/cdd7e7da525b229e599118a3178280d73922f164875cdda00487133443b0db49.jpg)

![](/api/attachments/MJUYK8EB/fulltext/images/feef6ef0e736fe04948505f3a16e48bf69b5fd9dc6a7a50823613de0280ab6e9.jpg)  
Fig. 3. Visualization of <sup>fl</sup>uctuation in quarterly data (3 levels of decomposition).

Both the transformed and the “original” data are stored and made available for analysis. In Fig. 2, the DSS and its functionality are shown in steps (3)–(8). The components of the DSS that support the intelligence and design phases would utilize the reduced wavelet data directly or present visualizations based on the wavelet data as described above. In the next section, an experiment implementing the procedural model with an existing BAM DSS in an event-driven enterprise is presented.

## 5. Experimentation

To evaluate the application of wavelets to event-driven decision support two experiments were conducted. The <sup>fi</sup>rst experiment was qualitative in nature and mirrored telecommunications managers' normal decision making process, but incorporated wavelet data and the procedural model. The second experiment performed a quantitative evaluation of DWT data used in a decision making context and its effects on user performance measured by three variables: decision outcome accuracy, timeliness/speed, and con<sup>fi</sup>dence.

## 5.1. Qualitative procedural model evaluation

To carry out this experiment, managers from a large telecommunications service provider who had recently implemented event-driven systems and utilized data from a BAM system were invited as subjects. Among the <sup>fi</sup>ve participants, two managers are males between the age of 46 and 55. The remaining three female managers are between the age of 26 and 45, and between the age of 46 and 55. It should be noted that all <sup>fi</sup>ve managers have more than 10 years of job experience. They all consider themselves advanced (as opposed to novice, intermediate, or expert), in terms of data analysis expertise. In this organization, managers are evaluated based on their monthly and annual performance. We spoke with <sup>fi</sup>ve managers who con<sup>fi</sup>rmed that many of their operationally oriented decisions are based on intuition or summarized historical data. The managers gave us a sample of Digital Subscriber Line (DSL) orders from their BAM system, which they said would typically be used to support staf<sup>fi</sup>ng decisions. This data consisted of details regarding orders placed and ful<sup>fi</sup>lled, such as the time the order was placed, the location of service delivery, the manager responsible for the order. The managers noted that they typically use this data to make decisions about where and when technicians were stationed to support the DSL delivery process. Speci<sup>fi</sup>cally, the managers asked us to evaluate this data and determine if there are patterns in the data that may be relevant to decisions regarding service delivery and staf<sup>fi</sup>ng. In this context, the managers posed a semi-structured decision opportunity for which we could apply the procedural model to aid data exploration.

The typical process managers followed when faced with this type of decision opportunity was to import the previous one-month's data into Microsoft Excel and plot the orderful<sup>fi</sup>llment delay measure against time, hoping to identify any trends. Based on this view of the data, the managers would make any staf<sup>fi</sup>ng adjustments deemed necessary; redistributing personnel or in some cases consolidating central of<sup>fi</sup>ces. Additionally, information gained from the managers' exploratory assessment would be used as feedback for organizational business development and sales teams to help manage new customers' expectations, in terms of service delivery.

Original Data  
![](/api/attachments/MJUYK8EB/fulltext/images/34b01d5a2e38c39d07ce482716d123018cb3c23a2e1087499ea63c5738590ba2.jpg)  
Fig. 4. Original data

The managers provided us with nearly four times as much data as they would typically use for their decision making process. From the perspective of the procedural model, this

Haar 5x Transform  
![](/api/attachments/MJUYK8EB/fulltext/images/255aa1f8da6fbca83d5ee1ed9cea86fe9cb530f545252e812baa22218109a0a8.jpg)  
Fig. 5. 5th level decomposition.

Fig. 7. 10th level decomposition.  
Haar 9x Tranform  
![](/api/attachments/MJUYK8EB/fulltext/images/0ea7405e59c8e7346d8760388e35dc7a0d0ac5778db1320c866d1c67478e54ff.jpg)

Haar 10x Tranform  
![](/api/attachments/MJUYK8EB/fulltext/images/be0df1b164bef5e170c1f43a054f0d711e8ad7e74d2353a49eac432460f32f1b.jpg)

Original Data  
![](/api/attachments/MJUYK8EB/fulltext/images/5cd6a6820aa8c82b2c8ab9faef3601345af2b6be18aa4d9ccaa97aa1df8d6cd0.jpg)  
Fig. 8. Original data scatter plot.

represents operational data as noted in step (1). This data was taken from their live BAM system and had the details for DSL orders completed in a particular geographical region, between June 5th and September 30th. This period covered 117 days and 82,963 records. The data contained several attributes: order start date/time, order completion date/time,

Haar 5x Tranform  
![](/api/attachments/MJUYK8EB/fulltext/images/5eaf0c038b0dcfedfdf4efae2453cd1891a4b050c81bafdbefd6b2a23f71470c.jpg)  
Fig. 9. 5th level decomposition scatter plot.

Haar 9x Tranform  
![](/api/attachments/MJUYK8EB/fulltext/images/e8a0c2a32bd30d2d4ba4a7b2172693b0c56eeb6b9e8f4ae047d2d72fac555b19.jpg)  
central of<sup>fi</sup>ce/location, and days to complete order (orderful<sup>fi</sup>llment delay). The number of orders-per-day was not linear across the time span. Each day had a variable number of  
orders each day, with a minimum of one and a maximum of 1701 on any given day. The average number of orders per day was 709 and the standard deviation 364.62.

Haar 10x Tranform  
![](/api/attachments/MJUYK8EB/fulltext/images/ed5eaf37037d9b5c1ef665668ee8c8992282d57310cd1db071121a0c646549b4.jpg)

Table 2  
Pearson's correlations

<table><tr><td></td><td>Original</td><td>5th level</td><td>9th level</td><td>10th level</td></tr><tr><td>Delay &amp; weekday</td><td>0.190</td><td>0.573</td><td>0.727</td><td>0.618</td></tr><tr><td>Delay &amp; quantity</td><td>-0.036</td><td>-0.144</td><td>-0.311</td><td>-0.196</td></tr></table>

We created a database using the original data and transformed the order-ful<sup>fi</sup>llment delay measure (days2Comp) using a Haar-based DWT to 10 individual levels of decomposition. This number of decompositions was chosen because nine transformations would result in 163 records. 163 records approximate a view similar to a daily average; the tenth-level decomposition results in 82 records. The original data was dense and odd numbers of records (not a multiple of two) for each transformation were padded with the last odd measure value, before transformation.

Initially, we attempted to visualize the data using standard Microsoft Of<sup>fi</sup>ce 2000 software (Access and Excel). This is what the managers said they did as their <sup>fi</sup>rst step in analyzing the data for this type of decision, so we followed a similar approach. Due to limitations in the software, neither of these tools was able to plot 82,963 records completely in sequence without cutting off records. Following steps (4) and (6) of the procedural model, we selected the days2Comp (delay) measure and used Systat's Sigmaplot to import and plot the data in a multiresolution view. The resulting plots can be seen in Figs. 4–7.

In Figs. 4–7, the X-axis represents order placement (orders) and the Y-axis is ful<sup>fi</sup>llment delay (days2Comp). Fig. 4 shows a plot of the data with no wavelet decomposition. This is what the decision-makers would see if they visualized the entire data set. The one-month visualization that the managers typically used was similar to Fig. 4's appearance; it is dif<sup>fi</sup>cult to see any pattern in the data. Figs. 5–7 show the DWT transformed (approximation coef<sup>fi</sup>cient) representation of this measure. Fig. 5 shows the same data after <sup>fi</sup>ve Haar-based DWT decompositions. Even at this level, a pattern is beginning to emerge. Fig. 6 is the data after nine transformations and Fig. 7 is the visualization of the tenth-level decomposition. For clarity and discussion purposes, we have superimposed a spline curve to highlight the pattern in the ninth and tenth-level decomposition plots.

The multi-resolution view based on the DWT data provided by step (6) of the procedural model, revealed a hidden pattern that was cyclic, seemingly based on day of the week. Using the hypothesis that there was a correlation between day of the week that the order was placed and the orderful<sup>fi</sup>llment delay, we decided to examine scatter plots of the day of the week and the days2Comp measure. Figs. 8–11 show the same data used for the previous analysis, graphed as scatter plots by day of the week (Monday=1) on the X-axis. As was the case in the <sup>fi</sup>rst analysis, the original data (Fig. 8) does not show a clear pattern as compared to the higher-level decompositions (Figs. 9–11). Visually examining the multiresolution DWT plots, a pattern is clearly visible.

The plots suggest that the pattern is seasonal in nature. With this information, we ran 2-tailed Pearson's correlations to determine if there was a direct relationship between day of the week and amount of time to complete the order. The correlations are shown in Table 2

The correlation between weekday and the delay (orderful<sup>fi</sup>llment delay) was positive and signi<sup>fi</sup>cant with a 99% con<sup>fi</sup>dence interval. Having identi<sup>fi</sup>ed a pattern that might present a decision opportunity about the staf<sup>fi</sup>ng utilization on certain days of the week, we examined the data further to determine if there were other causal relationships. Because the number of orders received each day was not linear, we felt it was relevant to attempt to determine if the quantity of orders received, (quantity) had a relationship with the time to complete (delay). The second row of Table 2 shows the results of Pearson's correlation using these attributes. This correlation was negative and signi<sup>fi</sup>cant with a 99% con<sup>fi</sup>dence interval (2-tailed) until the ninth level decomposition. In the ninth level decomposition, the correlation was still negative but only signi<sup>fi</sup>cant with a 95% con<sup>fi</sup>dence interval. Both correlation results strengthened, becoming more positive or negative respectively after each decomposition until the ninth level, after which it began to decline.

We presented our <sup>fi</sup>ndings to the <sup>fi</sup>ve managers of the telecommunications service provider who provided the data, explaining that there was a relationship between day of the week and the order-ful<sup>fi</sup>llment delay. While they explained that Saturdays usually had a higher order delay, they were a bit surprised by our <sup>fi</sup>ndings saying, “as a 24 hour a day, 7 days a week operation, they expected some delays but that those higher delays should have occurred on orders placed on Friday and Saturday.” Our data showed that the increasing delays began on Thursday. We also presented the multiresolution plots and the managers were able to quickly identify the same pattern we noted. The managers were also able to quickly explain the two peaks in the DWT plots (Figs. 4–7) that occurred on top of the cyclic daily pattern, noting “those peaks must be the 4th of July and Labor day holidays.” Upon exploring the original data for those time periods we con<sup>fi</sup>rmed that conclusion. The managers noted they felt intuitively, the delay should have a positive correlation with the number of orders for a given day. However, our <sup>fi</sup>ndings were the opposite of their intuition. Further exploration revealed that the reason for this was that most of their orders came on Tuesday and Wednesdays (days with the lowest delays), with the next highest day being Thursday. Saturday and Sunday had the fewest orders placed, less than a third of the orders received on any of the weekdays.

All <sup>fi</sup>ve managers felt that this analysis was extremely helpful to their staf<sup>fi</sup>ng decisions. Despite their initial surprise at the results, they felt that the visualizations led them to identify the variables in a manner that was more logical and ef<sup>fi</sup>cient, compared to their previous methods. All of the managers felt that the ability to visualize a much larger volume of data was a valuable tool and they stated they would use this analysis as the basis for current staf<sup>fi</sup>ng changes.

Summary of demographic information

<table><tr><td>Demographic</td><td>Class</td><td>Number of subjects</td></tr><tr><td rowspan="2">Gender</td><td>Female</td><td>23</td></tr><tr><td>Male</td><td>8</td></tr><tr><td rowspan="4">Age</td><td>26–35 years</td><td>4</td></tr><tr><td>36–45 years</td><td>8</td></tr><tr><td>46–55 years</td><td>10</td></tr><tr><td>&gt;55 years</td><td>9</td></tr><tr><td rowspan="2">Years of work experience</td><td>5–10 years</td><td>3</td></tr><tr><td>&gt;10 years</td><td>28</td></tr></table>

Table 4 Results of hypotheses testing

<table><tr><td></td><td>Non-transformed</td><td>Transformed</td><td>Hypothesis test</td><td>p value</td></tr><tr><td>Accuracy</td><td>31/124 (25%)</td><td>50/124 (40%)</td><td>Paired t-test</td><td>.016</td></tr><tr><td>Average time spent to analyze four visualizations</td><td>132.54 s</td><td>122.68 s</td><td>Paired t-test</td><td>.434</td></tr><tr><td>Average confidence</td><td>4.70</td><td>4.67</td><td>Mann-Whitney</td><td>.488</td></tr></table>

## 5.2. Quantitative experimental study of DWT data in a decision making context

To examine the effect of wavelet augmented decision support on user performance we conducted a quantitative experiment. The evaluation of the results examined the subjects' performance with and without wavelet transformed data. Many dependent variables have been proposed for measuring system impact on users' performance. Among them are time savings, decision quality, and con<sup>fi</sup>dence [13,17,19]. In this experiment, the dependent variables were speed (time savings), decision quality (measured by the number of patterns or anomalies correctly detected), and decision con<sup>fi</sup>dence. If the DWT technique was effective, we anticipated reduced time to make a decision, increased outcome accuracy (correct answers), and increased con<sup>fi</sup>- dence in decision choice. The independent variable was the use of wavelet-transformed data.

The experiment was laboratory-controlled and withinsubject. The subjects that participated in the experiment consisted of the <sup>fi</sup>ve managers from the qualitative study (as a pilot study) and an additional 31 non-managerial staff and technicians. The 5 managers were used to pilot the quantitative experiment and to con<sup>fi</sup>rm the qualitative <sup>fi</sup>ndings. Table 3 shows the demographic information of the 31 nonmanagerial subjects. Subjects were presented with visualizations of transformed and non-transformed data. Four data sets were utilized, one transformed and one non-transformed visualization for each data set, creating eight visualizations (4 pairs). All of the data sets and their visualizations had detectable features about which the subjects were asked. Each data set had a brief explanation describing its general characteristics and the subjects were not told which visualizations were transformed and which were not. The visualizations were randomly sequenced and each subject saw every visualization.

During the experiment, each subject was shown an explanation <sup>fi</sup>rst and then the data visualization. After seeing the brief explanation, the subjects were asked to identify the anomaly or pattern from a list of possible alternatives. The time subjects spent making each choice was measured. After making a decision regarding the data features, subjects were asked three Likert scale-based questions to measure the con<sup>fi</sup>dence they had in their response. The <sup>fi</sup>rst question was whether the subjects were con<sup>fi</sup>dent with their choice. The second question asked if the subjects felt they had chosen the best answer. The third question asked whether they would make the same choice again. This decision-survey sequence was repeated through the randomly selected visualizations.

The results of the pilot study with the 5 managers from the qualitative study were consistent with the feedback they provided. Of the 20 DWT-based visualizations shown the 5 managers (4 visualizations per manager), 8 were answered correctly, resulting in a hit rate of 40%. Only 4/20 (20%) visualizations based on the non-transformed data were answered correctly. On average, the managers took less time to evaluate and answer all four transformed visualizations: 82.4 s compared to 102.8 s for non-transformed visualizations (24.9% faster). The managers' mean con<sup>fi</sup>dence values between the transformed and non-transformed visualizations were similar: 5.09 and 4.97 respectively.

The data for the 31 non-managerial subjects in the expanded study was analyzed using SPSS to test three measures: speed, accuracy, and con<sup>fi</sup>dence. To evaluate accuracy, correct answers for each data set were coded as 1 and incorrect answers coded as 0. Then these results were evaluated using a paired t-test. Similarly, the time to answer each question was compared, also using a paired t-test. The questions measuring con<sup>fi</sup>dence were evaluated for internal reliability consistency and yielding a.897 value for Cronbach's alpha. Given this value, the three con<sup>fi</sup>dence questions were combined and then evaluated using a Mann–Whitney test.

The results of the two t-tests and the Mann–Whitney test are shown in Table 4. On average, subjects took less time to evaluate and answer all four transformed visualizations: 122.68 s compared to 132.54 s. Overall, the number of DWT transformed visualizations answered correctly is much higher than the non-transformed visualizations. Subjects correctly answered 50 out of 124 transformed visualizations, compared to 31 out of 124 non-transformed visualizations. The results demonstrate that the wavelet transformed visualizations enabled more accurate responses in a slightly lower average timeframe. The statistical signi<sup>fi</sup>cance of the accuracy t-test is below .05 supporting a rejection of the null hypothesis. The signi<sup>fi</sup>cance of the speed t-test is above .05, which indicates the results are not statistically different and the null hypothesis should be accepted. Examining Table 4, the two-tailed statistical signi<sup>fi</sup>cance is also above .05 for the con<sup>fi</sup>dence measure, accepting the null hypothesis for this measure.

## 6. Implications and discussion

The procedural model was successful in integrating the bene<sup>fi</sup>ts of DWT in terms of reducing the data set, providing a reasonable basis for visualization, and highlighting patterns, trends, and surprises. In the qualitative experiment, the visualization of the data, once transformed, revealed a cyclic pattern clearly. The plot of the original data was too cluttered to show a clear pattern and it could not be visualized using common of<sup>fi</sup>ce productivity software. It is interesting to note, that the visualizations of the transformed data also retained the “surprises” in the original data. Examining Fig. 4, the two points can be seen where the days to complete the order are nearly twice the average. These same features are evident in the transformed data at all decomposition levels and their approximate position in time is maintained. The DWT-based scatter plots showed the cyclic pattern much more clearly, compared to the visualizations of the original data.

The Pearson's correlations provided additional insight on the nature of the transformed data. The correlations were signi<sup>fi</sup>cantly stronger on the transformed data and may be useful in identifying an optimal number of transformations. The transformations also highlighted the relationships between the transformed measure and other non-transformed variables. A secondary bene<sup>fi</sup>t of the wavelet transformation is that the transformed data not only maintained and enhanced the pattern in the selected measure (time to complete orders), it also proportionally maintained other attribute characteristics, such as the relationship with the quantity of orders. This effect may be particularly useful in other event-driven applications and data mining such as classi<sup>fi</sup>cation or decision tree generation, because the detection of features and their relationships would be enhanced by the stronger correlations. In these types of applications, where subtle shifts in patterns and trends may foretell future events, being able to identify gentle, obscured, or minute changes is critical.

While it may be inferred that the strengthening of correlations may be the result of separating noise from the trend in the original data, the weakening in correlation after the 9th transformation warrants further investigation. This “turning point” that can be seen in the correlations based on the tenth decomposition, may be caused by the non-linear nature of the original data on the time scale. Once the transformations reduced the data beyond one measure per day, the correlation with day of the week would be weakened. This is because the data does not support the full range of days; the tenth-level decomposition approximates two consecutive days of the week. Identifying the “optimal” or best number of transformations also requires further investigation. It is not clear from this research how many transformations are necessary. Our work suggests the number of transformations may depend on the visualizations required or requested by the decision-maker. Therefore, an optimal transformation level may not exist.

Of the three measures (accuracy, speed, and con<sup>fi</sup>dence), only accuracy was statistically signi<sup>fi</sup>cant in the expected direction. For both con<sup>fi</sup>dence and speed, there was no statistical difference between the transformed and nontransformed samples (suggesting they were the same, i.e. not any better or worse). However, this may be explainable. The average speed, a quantitative measure, did decrease for the transformed data. However, the sample size may be too small for the t-test evaluation to attribute statistical signi<sup>fi</sup>cance to this deviation. The con<sup>fi</sup>dence variable is a qualitative measure; as such, the quantitative difference between the scale intervals is not necessarily equal from a purely statistical standpoint. This fact, coupled with the degree of difference between the average values (4.70 vs. 4.67) and the t-test showing the two populations are essentially the same, reduces the impact of its performance against our expectations. Another factor to consider is that much like the speed measure, evaluation with an increased sample size may clarify the true nature of the con<sup>fi</sup>dence measure.

For both the con<sup>fi</sup>dence and speed measures, the characteristics of the subjects may also play a role. These two measures may be in<sup>fl</sup>uenced by independent demographic factors such as computer expertise, physical condition, or experience with data analysis, which we did not capture. In light of these two measures not performing as expected, yet also not statistically going against the expected directions, further studies, then, should examine the sensitivity of the wavelet technique to the factors we describe above.

In contrast to the speed and con<sup>fi</sup>dence measures, the improvement in accuracy shown in the quantitative experiment is compelling. The combination of the qualitative evaluation and the quantitative results show the bene<sup>fi</sup>ts of this approach for event-driven, decision-focused, data analysis. It is clear that for event-driven data the DWT technique can provide bene<sup>fi</sup>t. Within this context, eventdriven data tends to have characteristics that make it suitable for DWT-based analysis. Event-driven data is naturally ordered, voluminous, and tends to be noisy, often with many local <sup>fl</sup>uctuations. In terms of generalizability, the procedural model and DWT technique should be applicable to any environment that has data with these types of characteristics.

## 7. Conclusion and future direction

Decision making in an event-driven environment is a dif<sup>fi</sup>cult and complex problem. The problem is compounded by the amount of data systems in that environment monitor and collect. Our experiment has empirically shown for decision support problems involving time series data, adapted in our procedural model, that wavelets provide the following bene<sup>fi</sup>ts: reducing the amount of data necessary to conduct analysis (increased scalability and usability of the data), multi-resolution data views (improved data visualization), and relationship enhancement between variables (better feature detection). DWT data, as applied in our procedural model, aided the decision-makers, showing its effectiveness to reduce data volume, preserve patterns, and strengthen relationships in a decision making context. In the qualitative study, all <sup>fi</sup>ve managers evaluating our results found that the DWT-based procedural model provided reduction of data and strengthening of relationships that dramatically improved visualization of complex, variant, and naturally ordered data. The quantitative evaluation of the DWT technique showed that analysis of DWT-based data improved decision accuracy without diminishing con<sup>fi</sup>dence and/or increasing the decision time.

This study used a Haar-based DWT. In the next phase of this research, we will examine the effects and suitability of other wavelets, such as Daubechies or Morlet. Related to the wavelet selection, the scaling of values in transformations presents an interesting challenge to the direct usefulness of the transformed values. The transformation can be very effective when applying statistical techniques, but extracting a value directly from the transformed data presents a unique challenge that may be mitigated by normalization techniques. We also intend to examine how the <sup>fl</sup>uctuation/noise portion of the DWT can be utilized for decision making purposes.

We will continue our engagement with the telecommunications service provider to evaluate the ultimate decision outcomes resulting from this exploratory effort and expand our laboratory-controlled experiment to include a larger number of users. In extending this research, a structured qualitative and quantitative study is planned to examine the issues this body of work identi<sup>fi</sup>ed and develop a system based on the procedural model proposed here. This planned research will develop a fully functional DSS to support the methods that we have de<sup>fi</sup>ned and implement the system in an event-driven production environment.

## References

[1] J. Ang, T.S.H. Teo, Management issues in data warehousing: insights from the Housing and Development Board, Decision Support Systems 29 (1) (2000) 11–20.

[2] P.W.B. Atkins, R.E. Wood, P.J. Rutgers, The effects of feedback format on dynamic decision making, Organizational Behavior and Human Decision Processes 88 (2) (2002) 587.

[3] S. Bapna, A. Gangopadhyay, A wavelet-based approach to preserve privacy for classi<sup>fi</sup>cation mining, Decision Sciences 37 (4) (2006) 623–642.

[4] D. Barbara, W. DuMouchel, C. Faloutsos, P.J. Haas, J.M. Hellerstein, Y.E. Ioannidis, H.V. Jagadish, T. Johnson, R.T. Ng, V. Poosala, K.A. Ross, K.C. Sevcik, The New Jersey data reduction report, IEEE Data Engineering Bulletin 20 (4) (1997) 3–45.

[5] L.R. Beach, T.R. Mitchell, A contingency model for the selection of decision strategies, Academy of Management Review 3 (1978) 439–449.

[6] J. Bertin, Semiology of Graphics, University of Wisconsin Press, Madison WI, 1983.

[7] M. Brenner, Non-stationary dynamics data analysis with wavelet-SVD <sup>fi</sup>ltering, Mechanical Systems and Signal processing 17 (4) (2003) 765–786.

[8] K.-P. Chan, A.W.-C. Fu, Ef<sup>fi</sup>cient time series matching by wavelets, Proceedings of the 15th International Conference on Data Engineering, Sydney, Austrialia, 1999, pp. 126–133.

[9] S.Y. Chan, The use of graphs as decision aids in relation to information overload and managerial decision quality, Journal of Information Science 27 (6) (2001) 417–425.

[10] E.C. Chewning Jr., A.M. Harrell, The effect of information load on decision makers' cue utilization levels and decision quality in a financial distress decision task, Accounting, Organizations and Society 15 (1990) 527–542.

[11] W.G. Cochran, Sampling Techniques, 3rd ed.John Wiley & Sons, New York, NY, 1977.

[12] I. Daubechies, Ten Lectures on Wavelets, Capital City Press, Montpelier, VT, 1992.

[13] H. Douglas, Requirements determination: an information systems specialist perspective of process quality, Requirements Engineering 6 (4) (2002) 220.

[14] G. Guo, H. Wang, D. Bell, Data reduction and noise <sup>fi</sup>ltering for predicting time series, in proceedings of WAIM'02, the 3rd International Conference on Web-Age Information Management, Beijing, China, 2002, pp. 421–429.

[15] J.F. Hair, R.L. Tatham, R.E. Anderson, W. Black, Multivariate Data Analysis, 3rd ed.Macmillan, New York, NY, 1992.

[16] M. Hellinger, S. Fingerhut, Business activity monitoring: EAI meets data warehousing, eAI Journal (2002) 18–22.

[17] C.W. Holsapple, M.P. Sena, ERP plans and decision-support bene<sup>fi</sup>ts, Decision Support Systems 38 (2005) 575–590.

[18] Z. Huanga, H. Chen, F. Guob, J.J. Xuc, S. Wu, W.-H. Chene, Expertise visualization: An implementation and study based on cognitive <sup>fi</sup>t theory, Decision Support Systems 42 (3) (2006) 1539–1557.

[19] H.K. Jain, K. Ramamurthy, S. Sundaram, Effectiveness of visual interactive modeling in the context of multiple-criteria Group decisions, IEEE Transactions on Systems, Man and Cybernetics 36 (2) (2006) 298–318.

[20] S.L. Jarvenpaa, G.W. Dickson, Graphics and managerial decision making: research-based guidelines, Commun. ACM 31 (6) (1988) 764–774.

[21] M.K. Jeong, J.-C. Lu, X. Huo, B. Vidakovic, D. Chen, Wavelet-based data reduction techniques for process fault detection, Technometrics 48 (1) (2006) 26–40.

[22] H. Kargupta, K. Sivakumar, S. Ghosh, A random matrix-based approach for dependency detection from data streams, Proceedings of the 7th Workshop on Research Issues in Data Mining and Knowledge Discovery, (ACM SIGMOD 2002), 2002, pp. 18–23.

[23] D.A. Keim, J. Schneidewind, Improving visualization, Working Conference on Advanced Visual Interfaces, Gallipoli, Italy, 2004, p. 179.

[24] S.M. Kosslyn, Understanding charts and graphs, Applied Cognitive Psychology 3 (3) (1989) 185-226.

[25] N. Kumar, I. Benbasat, The effect of relationship encoding, task type, and complexity on information representation: an empirical evaluation of 2D and 3D line graphs, MIS Quarterly 28 (2) (2004) 255–281.

[26] J.H. Larkin, H.A. Simon, Why a diagram is (sometimes) worth ten thousand words, Cognitive Science 11 (1987) 65–99.

[27] T. Li, Q. Li, S. Zhu, M. Ogihara, A survey on wavelet applications in data mining, SIGKDD Explorations 4 (2) (2003) 49–68.

[28] X.-B. Li, Data reduction via adaptive sampling, Communications In Information and Systems 2 (1) (2002) 53–68.

[29] S.G. Mallat, A wavelet tour of signal processing, Academic Press, San Diego, 1998.

[30] S.G. Mallat, W.L. Hwang, Singularity detection and processing with wavelets, IEEE Transactions on Information Theory 38 (1992) 617–643.

[31] Y. Matias, J.S. Vitter, M. Wang, Dynamic maintenance of wavelet-based histograms, Proceedings of 26nd International Conference on Very Large Databases (VLDB 2000), Cairo, Egypt, 2000.

[32] Y. Matias, J.S. Vitter, M. Wang, Wavelet-based histograms for selectivity estimation, Proceedings ACM SIGMOD International Conference on Management of Data, Seattle, WA, USA, 1998, pp. 448–459.

[33] D. McCoy, Business Activity Monitoring: Calm before the Storm Gartner Group, Stamford, CT, USA LE-15-9727, , 2002.

[34] M. Misiti, Y. Misiti, G. Oppenheim, J.M. Poggi, The MATH WORKS Inc. Wavelet Toolbox, The Math Works Inc., Natick, MA., USA, 1996.

[36] F. Murtagh, J.L. Starck, O. Renaud, On neuro-wavelet modeling, Decision Support Systems 37 (4) (2004) 475–484.

[37] M.J. Piovoso, K.A. Kosanovich, PCA of wavelet transformed process data for monitoring, Intelligent Data Analysis 1 (1) (1997) 85–99.

[38] D. Pyle, Data preparation for data mining, Morgan Kaufmann, San Mateo, CA, 1999.

[39] R. Raschke, P.J. Steinbart, Mitigating the effects of misleading graph designs on decisions, (Working Paper), Arizona State University, 2004, pp. 1–48.

[40] V.L. Sauter, Intuitive decision-making, Communications of the ACM 42 (6) (1999) 109–115.

[41] D.A. Schkade, D.N. Kleinmuntz, Information displays and choice processes: differential effects of organization, form and sequence, Organizational Behavior and Human Decision Processes 57 (1994) 319–337.

[42] G. Sheikholeslami, S. Chatterjee, A. Zhang, WaveCluster: a multiresolution clustering approach for very large spatial databases, Proceedings of 24th International Conference on Very Large Databases (VLDB'98) New York NY USA 1998 pp. 428–439

[43] G. Sheikholeslami, S. Chatterjee, A. Zhang, WaveCluster: a wavelet based clustering approach for spatial data in very large databases, VLDB Journal 8 (3–4) (2000) 289–304.

[44] C. Speier, M.G. Morris, Mitigating information overload: a comparison of perceptual and textual query interfaces in a decision support environment, Proceedings of the Americas Conference on Information Systems, Long Beach, CA, USA, 2000.

[45] C. Speier, I. Vessey, J.S. Valacich, The effects of interruptions, task complexity, and information presentation on computer-supported decision-making performance, Decision Sciences 34 (4) (2003) 771.

[46] G. Strang, Wavelets and dilation equations: a brief introduction, SIAM Review 31 (4) (1989) 614-627.

[47] Z.R. Struzik, A. Siebes, The Haar wavelet transform in the time series similarity paradigm, in lecture notes in computer science, Proceedings of the PKDD '99, Principles of Data Mining and Knowledge Discovery, Prague, Czech Republic, 1999, pp. 12–22.

[48] Z.R. Struzik, A. Siebes, Measuring time series' similarity through large singular features revealed with wavelet transformation, Proceedings of 10th International Workshop on Database & Expert Systems Applications, DEXA 1999, Florence, Italy, 1999, pp. 162–166.

[49] P. Subramanian, A. Songer, J. Diekmann, Visualizing process performance, ASCE International Conference on Computing in Civil and Building Construction, Stanford, CA, USA, 2000, pp. 1–6.

[50] D.P. Tegarden, Business information visualization, Communications of the AIS Archive 1 (1) (1999).

[51] M.E. Tipping, C.M. Bishop, Probabilistic principal component analysis, Journal of the Royal Statistical Society Series B61 (Part 3) (1997) 611-622

[52] E.R. Tufte, The Visual Display of Quantitative Information, Graphics Press, Cheshire, CN, 1983.

[53] J.S. Vitter, M. Wang, Approximate computation of multidimensional aggregates of sparse data using wavelets, Proceedings ACM SIGMOD International Conference on Management of Data (SIGMOD 1999) Philadelphia, PA, USA, 1999, pp. 193–204.

[54] J.S. Vitter, M. Wang, B.R. Iyer, Data cube approximation and histograms via wavelets, Proceedings of the 1998 ACM CIKM Bethesda MD USA 1998 pp.96-104

[55] J.Z. Wang, G. Wiederhold, O. Firschein, System for screening objectionable images using Daubechies' wavelets and color histograms, Lecture Notes in Computer Science, 1997, pp. 20–30.

[56] J.Z. Wang, G. Wiederhold, O. Firschein, S.X. Wei, Content-based image indexing and searching using Daubechies' wavelets, International Journal on Digital Libraries 1 (4) (1997) 311–328.

[57] J.Z. Wang, G. Wiederhold, O. Firschein, S.X. Wei, Wavelet-based image indexing techniques with partial sketch retrieval capability, Proceedings of the 4th Forum on Research and Technology Advances in Digital Libraries (ADL'97), Washington D.C., USA, 1997, pp. 13–24.

[58] S.M. Weiss, N. Indurkhya, Predictive Data Mining: A Practical Guide, Morgan Kaufmann, San Mateo, CA, 1997.

[59] C. White, BAM and business intelligence, DM Review Magazine, 2003.

[60] G.C.M. Wiederhold, M. Walker, R. Blum, S. Downs, Acquisition Of Knowledge From Data, in Proceedings of the ACM SIGART international symposium on Methodologies for intelligent systems Knoxville, ACM Press, Tennessee, United States, 1986.

[61] P.C. Wong, H. Foote, D. Adams, W. Cowley, J. Thomas, Dynamic visualization of transient data streams, IEEE Symposium on Information Visualization, (INFOVIS 2003), Seattle, WA, USA, 2003, pp. 97–104.

[62] X. Yin, W. Yurcik, M. Treaster, Y. Li, K. Lakkaraju, VisFlowConnect: net<sup>fl</sup>ow visualizations of link relationships for security situational awareness, 2004 ACM workshop on Visualization and data mining for computer security, Washington DC, USA, 2004.

Stephen Russell is currently an industry consultant and President of Agility Data Research, LLC. He has over 20 years of industry and entrepreneurial experience in such industries as telecommunications, healthcare, and manufacturing. He has authored or co-authored articles in Expert Systems with Applications, the Encyclopedia of Decision Making and Decision Support Technologies, and Frontiers in Bioscience. His primary research interests have been in the area of decision support systems and the application of intelligent systems to operations management. He is currently a Ph.D. Candidate in Information Systems at the University of Maryland Baltimore County and holds a M.S. in Information Systems Management and a B.Sc. in Computer Science also from the University of Maryland Baltimore County.

Aryya Gangopadhyay is an Associate Professor of Information Systems at the University of Maryland Baltimore County. He has more than 60 peer-reviewed articles in journals, conference proceedings, and book chapters. He also has edited and co-authored three books. His research has been published in journals such as Decision Support Systems, IEEE Transactions on Knowledge and Data Engineering, Journal of Management Information Systems, Very Large Database Journal, and Journal of Database Management. He is also the recipient of several grants from the Department of Education and Maryland Industrial partnerships program. His current research interests are in data warehousing, data mining, and in applications areas such as healthcare informatics and environmental sciences. He has a Ph.D. in Information Systems and an M.B.A from Rutgers University, an M.S. in Computer Science from New Jersey Institute of Technology, and a BTech from Indian Institute of Technology, Kharagpur.

Victoria Yoon is an Associate Professor in the Department of Information Systems at the University of Maryland Baltimore County. She received her M.S. from the University of Pittsburgh and her Ph.D. from the University of Texas at Arlington. Her primary research interests have been in the application of Arti<sup>fi</sup>cial Intelligence (AI) to business decision making in organizations and the managerial issues of such technology. She has published many articles in leading journals such as MIS Quarterly, Decision Support Systems, Communications of the ACM, Journal of Management Information Systems, Information Resources Management Journal, Information and Management, Journal of Operation Research Society, and others.
