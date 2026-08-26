---
otero_id: 19644
otero_key: "RYJAMXWW"
title: "Providing more regular road signs infrastructure updates for connected driving: A crowdsourced approach with clustering and confidence level"
authors: "Dieudonné Tchuente; Dominik Senninger; Holger Pietsch; Danilo Gasdzik"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113443"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Providing more regular road signs infrastructure updates for connected driving: A crowdsourced approach with clustering and confidence level

Dieudonn´e Tchuente <sup>a,\*</sup>, Dominik Senninger <sup>b</sup>, Holger Pietsch <sup>b</sup>, Danilo Gasdzik <sup>b</sup>

<sup>a</sup> Toulouse Business School, Dep. of Information, Operations and Management Sciences, 1 Place Alphonse Jourdain, 31068, Toulouse, France <sup>b</sup> Continental Automotive GmbH, Siemensstr. 12, 93055 Regensburg, Germany

## A R T I C L E I N F O

Keywords: Road signs Connected driving Crowdsourcing Big data Clustering Bayesian probabilities Intelligent transportation systems

## A B S T R A C T

Road signs, such as traffic signs, traffic lights or pavement markings, are essential elements for the regulation of driving. Sensors embedded in vehicles (e.g., cameras) are increasingly able to detect them to provide near realtime assistance to the driver, with features such as the current speed limitation at any moment. When sensors are not able to detect road signs (e.g., because of bad weather conditions or obstructions on the road), these features usually rely on in-vehicle digital map layers. However, in-vehicle digital maps are not often up-to-date because their update cycles from map providers are often lengthy (at the scale of several months). For example, a new speed limitation on a road can sometimes take months to be reflected in the vehicle’s digital map. To solve this problem, a crowdsourced process that can be used to provide more regular in-vehicle digital map updates (on an hourly or daily basis, for example) is proposed. In this paper, we focus on a crucial step in this process that consists of tracking road sign infrastructure changes by incrementally consolidating crowdsourced cameras detections of road signs and computing the real positions of the signs, while removing noise due to the impre cision of GPS positions in addition to false positive and false negative detections. This goal is achieved by using non-supervised geospatial clustering techniques and Bayesian probabilities to compute existence probabilities for road signs over time. Overall, this computation is performed in a big data context while also addressing security, privacy, safety and scalability issues. As a proof of concept, two experiments are conducted with true field data and they clearly demonstrate the relevance of the proposed approach. The method or the platform can be useful for many market players such as car manufacturers, map providers, or GPS providers (including navigation software providers) to provide more frequent map updates. to make connected driving easier and safer. It can also be useful for road infrastructure maintenance by helping to identify road signs that are poorly positioned or are not very visible.

## 1. Introduction

“Intelligent transportation systems” (ITS) refers to efforts that apply information, communication, and sensor technologies to vehicles and transportation infrastructure to provide real-time information for better decisions by road users and transportation system operators [1]. ITS operates in different fields of transportation systems, such as trans portation management, control, infrastructure, operations, policies, and control methods [2–4]. ITS can play a major role in reducing the risks, high accidents rates, traffic congestion, carbon emissions and air pollution, while increasing the safety and reliability, travel speeds and traffic flows, to the satisfaction of all-mode travelers. A road sign recognition system can technically be developed as part of an ITS. Road signs are an important part of road infrastructure in regard to providing information about the current state of the road, restrictions, pro hibitions, warnings, and other helpful information for navigation. This information is encoded in the visual traits of road signs, namely, the shapes, colors and pictograms. Examples for such road signs are traffic signs (e.g., a stop sign or speed limitation sign), traffic lights and pavement markings. Disregarding or failing to notice these road signs can directly or indirectly contribute to a traffic accident. In these cir cumstances, if there is an automatic detection and recognition system for road signs [5,6], it can compensate for a driver’s possible inattention, and it could decrease a driver’s tiredness by helping him to follow the road signs, which therefore make driving safer and easier.

In current vehicle navigation systems, road sign information for road stretches is usually provided to the driver by fusing data from multiple vehicle sensors. For example, to produce permanent reliable information on the current speed limit applicable to the vehicle, two sources of in formation are usually fused [7,8]:

• A digital map embedded in the vehicle: This map contains a speed limitation layer that can provide the current speed limitation for a road stretch when the vehicle is well localized and positioned on the relevant road link in the map by using map-matching methods [9].

• Road sign detection and recognition systems embedded in the vehicle: Such systems are usually embedded in a vehicle’s camera, and they can detect and recognize speed limitation traffic signs on the road.

In a simplified way, the fusion mechanism usually relies more on road sign detection and recognition systems because this approach provides more real-time information on the road infrastructure. On the other hand, the fusion mechanism relies more on the in-vehicle digital map when sensors are not able to provide suitable road sign detection on the current road stretch (e.g., occlusions by other vehicles or objects, shadows, light emitted by the headlamps of the incoming vehicles, weather-related factors such as rains, clouds, snow and fog) [6]. How ever, in-vehicle digital maps are very often outdated because of their longer update cycle, which is usually twice a year [10]. In such a long update period, there can be a large number of changes in the road infrastructure [11]. This can greatly increase the chances of relying on erroneous outdated information when using the in-vehicle digital map. The research objective in this paper is to improve the fusion mechanism by providing more frequent and relevant up-to-date road sign informa tion in the digital map. Thus, in the case of the camera detection prob lem, for example, the information from the digital map would be more up-to-date and relevant.

More precisely, the research question is the following: how can crowdsourced road camera detection be exploited to continuously deliver regular, relevant and updated road sign information to the drivers of vehicles? Of course, the aim is to propose updated frequencies at a scale of minutes or hours, for example, rather than the current up date cycles offered on a scale of months. As a rule, crowdsourcing in volves leveraging the combined intelligence, knowledge or experience of a group of people to answer a question, solve a problem or manage a process. In our case, the hypothesis is that if we can collect and centralize nearly real-time information about the localization of a road sign detected and recognized over time by many vehicles, then we can process in almost real time the localization of that road sign. This approach can be especially useful for tracking changes on the infra structure of road signs: the appearance of a new road sign, disappear ance of a road sign or modification of a road sign. However, to achieve this goal, several important issues must be considered, among which are the following:

• The imprecision of localization systems: conventional localization techniques, which mostly rely on GPS technology, are not able to provide reliable positioning accuracy in all situations [12]. To determine the real position of a road sign, several more or less precise localizations must be computed and aggregated efficiently.

• Road sign recognition system problems: this type of problem occurs when these systems are not able to recognize a road sign due to sensor errors or visibility issues [6]. False positive and false negative detections must be filtered efficiently.

• Big data and cloud issues: for more efficiency, the purpose of the crowdsourcing system here is to be able to operate with as many connected vehicles as possible, with worldwide coverage [13]. Such a system should be able to handle big data issues, such as high volume data collection with high velocity, while considering secu rity and privacy issues, a large variety of data sources and formats, the safety and the scalability issues.

In this paper, the specific focus is on addressing these three issues in a big data framework. We use a refined geospatial clustering technique to aggregate multiple and potentially noisy detection and recognition of road signs, and we provide a time-aware confidence level for each clustered road sign by using Bayesian probabilities.

The remainder of this paper is structured as follows: the Section 2 presents some related work. The Section 3 describes the proposed methodology and platform. The Section 4 presents processing steps for data analysis with clustering consolidation and confidence level calcu lations. The Section 5 presents the proof-of-concept results, with two experiments designed with true field data. The Section 6 provides a discussion of the results as well as the contributions, implications and limitations of this study, together with future research directions. The last Section 7 presents the conclusions.

## 2. Related work

For a few years, crowdsourcing approaches have been increasingly used in ITS [14–17]. According to the relevant available studies, crowdsourcing has an immense potential to replace or augment tradi tional methods of collecting data and feedback from a wider group of road users, at a very high speed and without creating an additional financial burden. Crowdsourcing in ITS is commonly used for moni toring traffic conditions, road hazards, road conditions and road infra structure [18]. In the current literature, the most common use cases concern the monitoring of road surface conditions for providing smooth and safe road infrastructure to road users [19–21]. It can be used, for example, to detect road surface anomalies such as potholes, bumps or cracks [22–24], or to compute the road roughness index [25,26]. The overall relevant literature relies on the data collected by using sensors on drivers’ smartphones, such as motion sensors (e.g., accelerometer, gy roscope) and position sensors (e.g., GPS, magnetometer). The data collected are then sent to the cloud, where their processing is usually performed using machine learning techniques [21]. All of the afore mentioned studies demonstrate the relevance of crowdsourcing ap proaches for accelerating the provision of up-to-date, useful information about the roads in ITSs. Some other studies that are based on crowd sourcing are interested in the detection and recognition of traffic regu lators, such as traffic lights (signals), stop-signs, yield-signs, prioritysigns, right of way priority rules and turning restrictions at in tersections [17]. However, the scope of the road signs that can be detected by these studies are limited (e.g., see previous list) because only crowdsourced vehicle position data (GPS) are used. For example, road signs, such as no entry signs or speed limit signs, cannot be detected by these approaches. To the best of our knowledge, we did not find a single research paper that addresses specifically the use of a crowdsourcing approach to provide accurate and up-to-date information about road signs that are detectable from vision-based detection and recognition systems [6].

In contrast, some recent web platforms, such as Mapillary [27], proposed a crowdsourced approach to provide an up-to-date road sign inventory for a specific area. They built a system on images or videos of driving sessions to provide a cloud-based algorithm that can detect up to 1500 visual road sign classes and position them on a map. This process could slightly accelerate and add some automation in the inventory of road signs for a specific area [28], by saving on time and budget. However, it would not be suitable to provide scalable regular updates of a road sign map for two major reasons. First, the process is not fully automated because street-level imagery and videos must first be captured by people before being manually uploaded for road sign recognition in the cloud. Second, even if someone wishes to fully auto mate this crowdsourcing process, sending images and videos from ve hicles to the cloud will cause a large bottleneck on the network because such visuals are too heavy for the current network transport protocol to be sent automatically from the vehicle to the cloud.

From an industrial point of view, some map providers, such as HERE [29], also consider the crowdsourcing approach to be a promising method for providing more frequent (daily basis) up-to-date road signs on maps. They indicate that they exploit the full path of the vehicle and the camera detections of the road signs with attributes such as the latitude and longitude of the detection, the heading of the vehicle, the detection timestamp, the road sign type and the road sign value, for making their daily cloud-based updates of the road sign map. However, little information is provided on the relevance (e.g., false positive and false negative rates) and the actual use of this service. In addition, the presented cloud-based technique for consolidating detections to deliver new updates is only a threshold setting: with at least three detections of a new sign in a day, a road sign map update is performed in the cloud. Obviously, this consolidation method could lack robustness when some sensor errors, traffic conditions or visibility-related events, such as bad weather, generate multiple false positive or false negative detections of a road sign in the course of a day. Furthermore, all of the individual camera detections are considered to be equal by this method, while in reality, a camera detection usually provides a confidence level (proba bility of the detection) that could be an interesting attribute for making distinctions in high-probable and low-probable detections. In this paper, we address the same problem that the HERE road sign service is attempting to solve. However, we propose a very robust and scalable platform for road sign consolidation in a big-data-based cloud. We also propose a quality indicator (time-aware confidence level) to measure at any moment the existence of any road sign and to eliminate noise due to false positive and false negative detections.

## 3. Methodology

Most of the current methods for updating road signs on digital maps are usually manual, and they involve teams driving around and filming the roads, as well as production teams who go through the video, making note of the signs before integrating them into the map [29]. This approach requires a very large investment in human and financial re sources and is especially time-consuming. This requirement explains why map updates are currently done at the scale of months or years. The Fig. 1 presents our methodology to improve the building and update frequencies (from months to a scale of minutes or hours) of maps by crowdsourcing.

This process can be divided into several successive steps: raw data collection, raw data feeding and storage, preprocessing of road sign observations, consolidation of road sign observations, mapping opera tions for new map layers, and distribution of updates to vehicles or other services. All of these steps, which require a large amount of computation or data storage, are performed in the cloud. Beyond technical issues, important issues related to privacy, security and safety are also considered in the platform as part of the global Continental AG eHorizon project [30]. The proposed methodology is applied to road signs; how ever, the same approach could be used for managing the lifecycle of other road objects (e.g., bumps, potholes, cracks) or road events (e.g., traffic conditions, road hazards). Moreover, the eHorizon project [30] also considers all of these other aspects. However, for each road object type or road event, there are some specificities that depend on their nature and the available raw data, which impact how these raw data will be consolidated in the cloud (along with the confidence levels). In this paper, we mainly focus on road signs.

## 3.1. Raw data collection

We consider using two different in-vehicle sensor signals: the road sign recognition output provided by in-vehicle cameras and the posi tioning data provided by the GPS. When a vehicle is directly connected to the provided cloud interface, these sensors act as IoT devices, and data are always sent with the driver’s consent to our cloud, using custom secured multifactor authentication mechanisms based on X509 certifi cates [31] and OIDC tokens [32]. These data can be sent as the vehicle is moving (“as you go”) or by batch, with no need for a complete GPS path of a single vehicle for privacy reasons. For example, the same vehicle is not expected to always have a single identifier in our cloud; only short driving sessions (e.g., each 100 m) with different identifiers would be sufficient for cloud-based processing.

## 3.2. Raw data feeding and storage

Raw data can be collected directly from vehicles (connections be tween vehicles and our cloud) or from vehicle data already stored in the car manufacturers’ cloud (with a connection between the cars manu facturers’ cloud and our cloud). The feeding and storage components are designed to be elastic and scalable to address data from many sources, which come at high rates and in greater volumes. We relied on a secured private cloud with big data infrastructure and services provided by Amazon Web Services (AWS). Before any processing, all of the incoming raw data are stored “as-is” with additional metadata, such as the received timestamp and the source. This approach gives the providers a subsequent access right to make adequate changes, while abiding by rules such as the GDPR (General Data Protection Regulation) rules. At this stage, no specific raw data format is required, even if we currently often rely on the SENSORIS (Sensor Interface format -https://sensor-is.org/) format, which is a global standardized interface for exchanging infor mation between in-vehicle sensors and dedicated clouds, as well as be tween clouds.

![](/api/attachments/RYJAMXWW/fulltext/images/e9a9f0995a572b3b231da219e2742fe49990ad3806fe82ff357502598123a880.jpg)  
Fig. 1. Global view of the crowdsourced-based processing framework.

## 3.3. Road sign observations

Road sign observations are a common representation of road sign recognition data and vehicle paths. With a common representation, the consolidation algorithm in the next step will be able to consolidate data from different sources as well as different raw data formats. For each raw data format, a dedicated preprocessing job is required to extract the road sign observations. For the sake of scalability, all of these preprocessing tasks are written within the distributed processing Spark framework [33], running on Hadoop clusters. The main attributes of the road sign observations that are needed for the consolidation are presented in Table 1.

For privacy issues, we consider road sign observations within driving sessions (e.g., each 100 m of driving or each 2 min of driving) with different identifiers (sessionId), even for the same vehicle. Within a session, road sign observations contain all of the recognized road signs and the successive GPS positions (paths) with the attributes described in Table 1. There are raw value attributes, such as the type, value, recog nition timestamp, recognition probability and detection timestamp. Usually, there are also computed attributes, such as the road sign ab solute position and heading. The reason is that vehicle sensor events are mostly sent as time series that contain only timestamps and associated

## Table 1

Mandatory road sign observation attributes.

<table><tr><td></td><td>Attributes</td><td>Description</td></tr><tr><td rowspan="6">Road sign</td><td>Type</td><td>Type of the road sign, as defined in SENSORIS format (e.g., “SPEED_LIMITATION”, “STOP”)</td></tr><tr><td>Value</td><td>Value of the road sign (e.g., “90” for a speed limitation road sign or empty for a stop sign)</td></tr><tr><td>Latitude, longitude, altitude</td><td>Computed absolute position of the road sign: the computation is performed by linear interpolation from the nearest GPS positions before and after the recognition timestamp.</td></tr><tr><td>Heading</td><td>Computed direction (at the time of detection) that the vehicle front is pointing in relative to the geographic true north: the computation is performed by linear interpolation from the heading of the nearest GPS positions before and after the recognition timestamp. This result will be useful to identify in which road direction a road sign applies.</td></tr><tr><td>Recognition timestamp</td><td>The timestamp at the recognition (detection) moment; This information will also be useful for aging considerations in the calculation of the road sign confidence level.</td></tr><tr><td>Recognition probability</td><td>The confidence level of the recognition provided by the camera (e.g., 0.95). If not provided, a parameterized default value can be used.</td></tr><tr><td rowspan="2">Path</td><td>Latitude, longitude, altitude</td><td>The absolute GPS position point as returned by the vehicle GPS</td></tr><tr><td>Position_timestamp</td><td>The timestamp for the GPS position</td></tr><tr><td>Common attribute</td><td>SessionId</td><td>Session identifier for the driving session that contains the vehicle path and all road signs recognized during this session.</td></tr></table>

events. Thus, for a road sign recognition event, the recognition time stamp and the raw value attributes are sent. However, to compute the absolute position and heading of the road sign, a linear interpolation from the closest GPS positions before and after the recognition time stamp is performed. We consider that systematic absolute position errors that could occur in the case of long-distance camera detections with low vehicle speed are marginal and will result in low confidence level values in subsequent steps of the consolidation algorithm. There are also optional road sign observation attributes that can be used during consolidation processing. They include road sign permanency (static or dynamic), GPS position accuracies (lateral, longitudinal, and vertical accuracies), or supplementary signs on a road sign (e.g., direction subsigns, weather sub-signs, time sub-signs); however, these are out of the scope of this paper.

## 3.4. Road sign consolidation with confidence levels

The research question on how can crowdsourced road camera detection be exploited to continuously deliver regular, relevant and updated road sign information to the drivers of vehicles is specifically addressed in this step.

The proposed technique for this consolidation exercise spans road sign observation clustering and road sign confidence level calculations. The clustering step uses the positions and heading of the observation to group multiple closed observations to a single potential road sign object. The confidence level calculation takes as input each potential road sign object from the previous step and computes its existence probability. The most important issues to consider for these two steps are the imprecision of the GPS positions and the filtering of false positive and false negative observations. The method for handling all of these issues is presented in detail in the Section 4 of this paper (data analysis process for consolidation).

## 3.5. Mapping operations

For each plausible road sign object (with a confidence level greater than a well-defined threshold), this step is about projecting each object onto a reference map with map-matching algorithms [9] and then applying constraints related to this object on a new map layer. For example, for a speed limitation road sign, applying constraints will help to obtain the construct for a new speed limitation map layer (e.g., by propagating a new speed limit on the concerned road links). More in formation on this step is unnecessary because it is out of the scope of this paper.

## 3.6. Providing map updates to vehicles

The goal here is to continuously provide updated portions of new map layers to connected vehicles when necessary. The distribution of the map updates depends on the position of the vehicle. Only map up dates around the position of a connected vehicle are sent to that vehicle. This strategy could be based, for example, on vehicle routing techniques [34,35], such as using the vehicle’s most probable path. Map updates or road sign updates could also be distributed not directly to vehicles, but to other services in our cloud or to partner clouds such as car manufacturers’ clouds. In the experiment section, a basic system that simu lates on-board fusion of camera detections and consolidated road signs that could help to provide more updated and reliable information to the driver is evaluated. However, on-board fusion mechanisms represent themselves broader topics that have rules that require further experi ments in partnership with car manufacturers, which is within a larger scope than the scope of this paper. The next section provides more de tails on the road sign consolidation with confidence level steps, which represents one of the main contributions of this paper.

## 4. Data analysis process for the consolidation

Road sign consolidation is a step of the global processing that con sists of taking continuous recent road sign observations in a common format and then processing them to obtain an up-to-date physical positioning of the road signs. To assess the relevance of each computed road sign, a confidence level is calculated and represents its existence probability. This processing operation is strongly parameterized for evaluation in multiple contexts (e.g., more or less driven areas, different countries or regions). The successive steps are presented in Fig. 2 and they are described in following subsections.

## 4.1. Sliding spatiotemporal query and reading of parameters

The consolidation steps start with the querying of road sign obser vation data and the reading of consolidation parameters. This step triggers the whole consolidation process and restarts at regular time intervals according to the desired update frequencies of the road signs (e.g., every hour or every day). The querying can be performed in a spatiotemporal way, and it returns all relevant road sign observation attributes with the vehicle paths for the driving sessions, as described in Table 1. The spatial component of the query is defined by the specifi cation of a geo-rectangle (bounding box), which delimits the geographical area in which the road sign observations will be retrieved. The temporal component is represented by a duration that indicates the time window in which the observations will be extracted. At each execution, this time window slides to also integrate the new observa tions that have occurred since the previous execution. For example, there could be daily executions for retrieving, at each execution of the rolling history of the past three months of observations $( \mathbf { e . g . }$ , three successive executions are shown in Fig. 3), for a specific geographic area delimited with a bounding box.

By using sliding windows, each execution performs on the same window size, but it also considers the freshest observation data since the last execution. In the confidence level computation step, we will see how the age of each observation is impacting the calculation of the existence probability of the road signs.

For flexibility purposes, spatial and temporal parameters are taken from a parameter file as well as from many other parameters, which are used in next steps.

## 4.2. Assigning road sign observations to tiles

We use geographic tiles (with configurable sizes) to make geographic partitions of the observation data, to enable further processing steps to be easily distributed for performance and scalability issues. Geographic tiles divide the world into grids of the same shapes and equal sizes [36]. The commonly used shapes for tiles are squares, which can be used at different size levels depending on the context [37]. For example, at zoom level $^ { 0 , }$ the entire world is rendered in a single tile. Each zoom level increases the magnification by a factor of two. Thus, at zoom level 1, the map will be rendered as a $2 \times 2$ grid of tiles. At zoom level 2, it is a $4 \times 4  \mathrm { g r i d }$ . At zoom level $^ { 3 , }$ it is an 8 × 8 grid, and so on (Fig. 4) [38]. For instance, if zoom level 1 is used, data can be partitioned in 4 tiles and processed in 4 parallel jobs for better scalability and performances.

In this step, each road sign observation is assigned to all of the tiles, which are touched by a circle with a configurable radius around the

detection.

Observations assigned to neighboring tiles avoid boundary effects that could occur by assigning different observations of the same road sign exclusively to different tiles. The same tile assignment process is performed for the paths, which are later used to find negative obser vations. For the paths’ case, the configurable radius for assigning a path to tiles considers the path’s starting point and the path’s length.

## 4.3. Clustering of road sign observations

The clustering step consists of bringing together road sign detections that potentially represent the same physical road sign object. First, the clustering is applied exclusively on the road sign detections that have the same type and the same value attributes. Thus, road signs for speed limitations will never be clustered with stop signs, for example. Second, the distance used to group the road sign detections considers the abso lute position of the detection (latitude and longitude) and the driving direction (heading) at the moment of the detection. The heading attri bute should be able to separate road sign detections of the same type and of the same value that are very close one to another, but they could be physically on different roads or have different directions. This distance $( d ) ,$ , which is indicated in Formula (1) below, uses the horizontal dis tance $d _ { h o r }$ (e.g., the geodesic distance between two absolute positions) and the heading angle difference $d _ { h e a d }$ between two detections. Each of these distances is normalized by its parameterized minimum values, to keep two observations in the same group (or cluster): $b _ { h o r }$ (horizontal bandwidth) and $b _ { h e a d }$ (heading bandwidth). For example, one can consider using $b _ { h o r } = 2 0$ m and $b _ { h e a d } = 4 5 ^ { \circ }$ to keep the detections within a 20-m radius with heading differences that are smaller than $4 5 ^ { \circ }$ into the same cluster.

$$
d = \sqrt {\left(\frac {d _ {h o r}}{b _ {h o r}}\right) ^ {2} + \left(\frac {d _ {h e a d}}{b _ {h e a d}}\right) ^ {2}}\tag{1}
$$

This distance is used as a parameter of the meanshift clustering al gorithm [39]. The meanshift algorithm is chosen because it is a nonparametric clustering technique that does not require prior knowl edge of the number of clusters and does not constrain the shape of the clusters. In our case, it is impossible to know in advance the number of clusters, and the shape of each cluster will be dependent on the physical position of each road sign, which will impact the visibility of the road sign from different visual angles.

However, as can be seen in Fig. 5, for example, the clustering step is not always sufficient to directly consolidate the road sign positions as they are in the real world. Fig. 5A shows an example of observations of road signs near Regensburg, in Germany (only 50 speed limit road signs). Fig. 5B shows how these observations have been clustered in this step. Observations with the same shape and the same color represent the same cluster (a potential road sign). Fig. 5C shows the locations of the real road signs (true field locations) with red points.

Normally, each cluster in Fig. 5B should represent a real road sign. Two main issues that concern the clusters are raised at this level:

• There are clusters that should normally be split into two clusters because there are really two road signs in the true field $( \boldsymbol { \mathrm { e . g . } }$ , blue cluster with plus shapes): this case is, for example, a case when the same road sign is repeated on both sides of a road. If the distance

![](/api/attachments/RYJAMXWW/fulltext/images/d2343383db1ff33148888c347192d5fa40424828be563ca276bf5f1f3262d588.jpg)  
Fig. 2. Road sign consolidation with confidence level steps.

![](/api/attachments/RYJAMXWW/fulltext/images/9c55842086b483dab5cc30beb283b9458a94f30aeaca172158b16ffb64764e9f.jpg)  
Fig. 3. Example of 3 successive daily window executions.

![](/api/attachments/RYJAMXWW/fulltext/images/69571f5e8b2bdaaa16918313704d3888d62ff1003717f3274fd4464e5ba36b1c.jpg)  
Fig. 4. Examples of three-level grid square tiles.

![](/api/attachments/RYJAMXWW/fulltext/images/15eea522eec6a4bc1e5ad0ec9dc75652a70cccecbfd84d67f70d39a85b0ea08d.jpg)  
A

![](/api/attachments/RYJAMXWW/fulltext/images/c6de99945e6f6f552c9cdac8e5710e563267788b6908d35d4d1b7593ba093b57.jpg)  
B

![](/api/attachments/RYJAMXWW/fulltext/images/441eca418d9957b9075ee7de2db6a5a7119b52b5cf97848aeb9208ea4d36c260.jpg)  
C  
Fig. 5. Output example of clustering and true field data near Regensburg.

between such road signs is smaller than the horizontal bandwidth and heading bandwidth parameters, then their observations will be grouped into only one cluster. The next step of the algorithm (clus tering refinement) is designed to solve this issue (splitting of clusters).

• There are clusters that do not correspond to any road sign in the true field (e.g., the cluster with two red triangles on the right): these are usually false positive detections or outliers. Some of these clusters could be removed by using parameters such as the minimum number of observations in a cluster, or the minimum age of the observations. However, this approach solves only a small part of the problem. In a more robust way, other information is required to solve this problem by calculating, for example, low existence probabilities for these types of clusters. This approach will be described in the confidence level calculation step.

## 4.4. Clustering refinement

As stated in the preceding section, the goal of the clustering refine ment step is to split clusters from the previous step that could physically contain several closed road signs of the same type and same value. Such road signs are frequently a replication of the same signs on both sides of the road, and they are also frequently geared toward the same direction. Therefore, for a single driving session, the vehicle’s camera is very likely to report not one, but two detections in a short time when crossing these road signs. Therefore, this step is about analyzing the vehicle paths around each cluster from the previous step and recording the number of detections at approximately the same time for each cluster. Clusters that regularly record a greater number of detections from single driving sessions are then split into as many clusters as there are different detections.

Fig. 6 complements Fig. 5 by adding the results obtained after applying the clustering refinement (Fig. 6D). Fig. 6D shows that each cluster from the previous step (Fig. 6B) that contains two road signs in the true field (Fig. 6C) is correctly split into two clusters by this refinement step (e.g., the blue cluster with the “+” shape in Fig. 6B is split into two clusters in Fig. 6D: blue and green).

At the end of the clustering steps, each cluster potentially represents a road sign. The position attributes (latitude, longitude, altitude and heading) of each road sign are simply computed as the weighted mean of all of the corresponding observation attributes in the cluster that rep resents the road sign. However, at this level, each cluster does not necessarily represent a physical road sign, most likely for two major reasons: (i) the cluster is an outlier cluster due to false positive de tections (e.g., the black and red triangles in Fig. 6D); or (ii) the cluster is consistent, but the physical road sign has been removed or updated recently. To remove these noisy clusters, the confidence level (existence probability) is computed for each cluster. However, first, it is necessary to compute the negative observations.

## 4.5. Computation of negative observations

A negative observation is generated for an existing sign that is not detected by the camera when the vehicle passes (a nondetection event). In general, negative observations are not directly evaluated in on-board systems during driving sessions. Thus, the proposed method consists of deriving negative observations from vehicle session paths in the cloud. This approach will entail having all driving session paths be available when the querying observations are made. Negative observations are estimated by identifying the previously clustered signs that can be detectable from a path. A road sign is said to be detectable from a path if that path harbors at least one GPS position that satisfies all of the following conditions:

• The GPS position is closer to the sign than a configurable distance. This approach could lead to problems when there is high speed. Interpolated positions are sometimes necessary.

• The absolute value of the angle between the heading of the GPS position and the direction of the road sign is below a configurable value (this criterion means that the camera cannot look backward).

• The absolute value of the angle between the heading of the road sign and the direction of the road sign, with respect to the GPS position, is below a configurable value (this criterion means that the camera cannot recognize a road sign from the side or the backside).

A road sign near the intersection between two consecutive session paths (the end of the previous session and the beginning of the next session) could be evaluated as a negative detection from one session, while it was detected in the other session. To avoid these side effects, all of the negative observations of a road sign that are closer in time to a positive detection (of the same sign) than a configurable value (e.g., 1 min) are omitted.

Finally, to evaluate the real existence of a clustered road sign at each moment, an existence confidence level value is calculated using both positive detection and negative detection events, as described in the following session.

## 4.6. Confidence level computation

## 4.6.1. Basic principle

The confidence level represents the probability that a potential road sign (a cluster) from the clustering steps exists physically. It is calculated incrementally for each potential road sign through Bayesian inference. The initial confidence level of each potential road sign is 50%, which implies the likeliness of existence and nonexistence at the beginning. After each event (detection or nondetection), a new confidence level i calculated from the previous calculation. The calculation after the last known event represents the current confidence level of the sign.

## 4.6.2. Description and illustration

Fig. 7 schematically represents the confidence level calculation process for a road sign.

First, all of the events (detections or negative detections) for the road sign are ordered in ascending order (from oldest to newest, T to $\mathrm { T _ { n } } )$ . In Fig. 7, we have the following:

• H represents the hypothesis that the road sign exists;

• E represents the event (detection or negative detection);

• P (E|H) represents the probability of the event at timestamp T . For a positive detection case, it is the recognition confidence provided by the camera (greater than 50%). For a negative detection case, it could be configured as a constant probability (lower than 50%) when negative detections are computed in the cloud, or a probability of nonexistence (lower than 50%) when negative detections are eval uated directly by a vehicle sensor. Probabilities that are lower than

![](/api/attachments/RYJAMXWW/fulltext/images/c84d504530a9ede32879d889bec64e1dba8f2dad68ef389f35773bb372077bde.jpg)  
A

![](/api/attachments/RYJAMXWW/fulltext/images/f9f16acb2024240c48bce6fdda1ae4d424480d175e50a5cf0b39022768eb83dd.jpg)  
B

![](/api/attachments/RYJAMXWW/fulltext/images/a9c753e522782c323965139333cda0eeb7ef7cf05b64138c4d2207944e815e7f.jpg)  
C

![](/api/attachments/RYJAMXWW/fulltext/images/7b0faf693873af078c630222234e39a1a335d4536dfa0c0fb71040109db41574.jpg)  
D  
Fig. 6. Output example of the clustering refinement step.

![](/api/attachments/RYJAMXWW/fulltext/images/47d61f19a1fd334c0b27cfc74ef48dc2b8a2f8f8566efda6fbed4a937e8c8be6.jpg)  
Fig. 7. Confidence level calculation process.

50% are used for negative detections because these will decrease the confidence level, while positive detections (probabilities greater than 50%) will increase the confidence level.

• P (H) represents the probability of the event at a timestamp T but with aging considerations. The reason is that recent events must be more important than old events in the confidence level calculation. In addition. the time interval between two successive events must also be considered (e.g., the most frequent detections should increase the confidence level faster than the less frequent detections). This aging probability is also very useful in the case of an empty time frame: when no event information is available (detection or non detection), as we will see later.

Second, the initial confidence level $P _ { O }$ is set to 50%, and after each event, the new confidence level is calculated from the previous level (e. g., $P _ { n }$ from $P _ { n - 1 } )$ . The confidence level (P) after the last event at time stamp $\mathrm { T } _ { \mathrm { n } }$ represents the current confidence level of the road sign.

Third, for aging considerations, an artificial neutral event (with the current consolidation timestamp) is added after the last event for calculating the current confidence level P. The purpose of this neutral event $( P _ { n e u t } = 5 0 \% )$ is only to apply aging in the confidence level calculation when the timeframe between the last event and the consol idation timestamp is relatively high. Obviously, between the last event and the consolidation timestamp, there is no event (empty timeframe). However, even in the case of an empty timeframe, the confidence level must be impacted by modeling the uncertainty due to the lack of in formation in this timeframe. Here, the uncertainty that is modeled consists of decreasing or increasing the last confidence level (from the last event before the empty timeframe) up to a maximum or minimum of 50% (highest level of uncertainty of the road sign’s existence).

Fig. 8 illustrates the behavior intuition for the confidence level, depending on the detections (pass & detect), negative detections (pass & no detect) and empty timeframes when no information is available (no pass & no detect).

The three major configurations for confidence level variations are presented in this figure:

![](/api/attachments/RYJAMXWW/fulltext/images/2dd814ba6ee090b42d2c805859bbb6d30cccf4e72d0c65a1d946e01daadef116.jpg)  
Fig. 8. Illustration of confidence level values from events or no events.

• Detections increase the confidence level (timeframes from $\mathrm { T } _ { 0 }$ to $\mathrm { T } _ { 5 }$ and T<sub>25</sub> to T<sub>30</sub>).

• Negative detections decrease the confidence level (timeframe from T<sub>15</sub> to T<sub>20</sub>).

• In the case of no information, only aging is used to model the un certainty. The confidence level decreases if the last known confi dence value is greater than 50% (timeframe from $\mathrm { T } _ { 5 } ~ \mathrm { t o } ~ \mathrm { T } _ { 1 0 } )$ . The confidence level increases if the last known confidence value is lower than 50% (timeframe from T to T ).

The parameters for controlling the increase or decrease due to aging are the time interval from the previous event and the road sign half-life parameter, as described below.

## 4.6.3. Algorithm

The algorithm is described in the following instructions:

a. Sort all detection events E (detections and negative detections) ascending by timestamp.

b. Add a neutral event E at the end with the consolidation timestamp

c. Initialize P with 50%

d. For each event E at position i, compute the confidence level $P _ { b }$ as follows:

$$
P _ {i} (H) = (P _ {i - 1} - P _ {n e u t}) ^ {*} 0. 5 ^ {\frac {T _ {i} - T _ {i - 1}}{T _ {1 / 2}}} + P _ {n e u t}\tag{2}
$$

$$
\begin{array}{r l} P _ {i} & = P _ {i} (H | E) = \frac {P _ {i} (H) ^ {*} P _ {i} (E | H)}{P _ {i} (E)} \\ & = \frac {P _ {i} (H) ^ {*} P _ {i} (E | H)}{P _ {i} (H) ^ {*} P _ {i} (E | H) + (1 - P _ {i} (H)) ^ {*} (1 - P _ {i} (E | H))} \end{array}\tag{3}
$$

## e. Return the last calculated $P _ { i } ( H | E )$

The confidence level is incrementally calculated with the return of the last calculated value by the ending neutral event, as described in the previous section. The formula for calculating the confidence level at each timestamp position is given by Eqs. (2) and (3).

First, Eq. (2) calculates the aging probability P (H) from the previous confidence level $P _ { i - 1 }$ by applying an exponential decay. The exponential decay is chosen because we assume that the value of the confidence level decreases (or increases) at a rate that is proportional to its current value, as in geophysics [40], radioactivity [41] or in user modeling systems [42]. In our case, the exponential decay depends on the time elapsed from the previous event $( T _ { i } - T _ { i - 1 } )$ and the road sign half-life parameter $( T _ { 1 / 2 } ) .$ The road sign half-life parameter gives an idea of the average life expectancy of road signs (time required for the confidence level to fall below 50%). This parameter can strongly depend on the geographical area (e.g., 60 days or 1 year for different areas), which therefore gives this parameter a configurable nature. The higher the half-life parameter is, the lower the decrease or increase in the confidence level due to aging. The higher the time elapsed from the previous event is, the higher the decrease or increase in the confidence level due to aging. In all cases, the aging probability is designed to converge to a maximum (if increasing) or a minimum (if decreasing) of $P _ { n e u t }$ (50%, maximum of uncertainty).

Second, $\operatorname { E q . }$ (3) calculates the current confidence level at timestamp i $P _ { i } ( H | E )$ by using the Bayes formula from the current aging probability $P _ { i } ( H )$ and from the probability of the current event P (E| H). P (E) is the normalizing factor, which is the sum of the probabilities of all possible outcomes. It is given by summing the following: the probability that the sign exists a priori; the supported event $\begin{array} { r } { ( P _ { i } ( H ) ^ { * } P _ { i } ( E | H ) ) ; } \end{array}$ ; the probability that the sign does not exist a priori; and the supported event $( 1 - P _ { i } ( H ) ) ^ { * }$ (1- P (E|H)).

The calculation is performed incrementally for successive positions of i, and the last calculated value is returned as the current confidence level. Table 2 shows a calculation example of the successive confidence

## Table 2

Example of the calculation of the confidence level from detections.

<table><tr><td rowspan="2">Event confidence</td><td colspan="6">Number of detections</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>10</td></tr><tr><td>60%</td><td>60%</td><td>69%</td><td>77,1%</td><td>83,5%</td><td>88,3%</td><td>98,21%</td></tr><tr><td>75%</td><td>75%</td><td>90%</td><td>96,4%</td><td>98,8%</td><td>99,6%</td><td>99,974%</td></tr><tr><td>85%</td><td>85%</td><td>97%</td><td>99,4%</td><td>99,89%</td><td>99,97%</td><td>99,9897%</td></tr></table>

level from successive detections. The event confidence is the confidence of the detection provided by the sensor (camera). In this case, a simple scenario is considered with a half-life $\left( T _ { 1 / 2 } \right)$ parameter of 30 days and a uniform time interval $( T _ { i } ~ - ~ T _ { i - 1 } )$ between detections of 1 h. This example shows that the confidence level increases quite fast with the number of detections. and in accordance with the event confidence.

Table 3 shows that the effect of a negative observation on the con fidence level depends on the last confidence level recorded just before the negative detection. The higher the last confidence is, the less important is the decay of the confidence due to the negative detection. Similar to the previous example, the half-life used here is 30 days, and the time interval from the last event is 1 h.

Table 4 shows that the effect of a negative detection also depends on the time interval to the last event before the negative detection. The higher the time interval ${ \mathrm { i } } s ,$ the more important is the decay due to the negative detection. Similar to the previous case, a half-life of 30 days is also used for this simulation.

## 5. Experiments

The experiments here are designed as proof-of-concept experiment to validate the relevance of the proposed crowdsourced-based approach to consolidating road signs with confidence levels. Two experiments are presented: the first experiment compares the results of the consolidation process to the actual positions of the road signs on the field, and the second experiment compares the relevance of a simulated system that aggregates in real time the road sign detections from a camera with consolidated road signs from the cloud, with a system that consider only the camera’s road sign detections.

## 5.1. Experiment 1: consolidated output versus real road sign positions

The goal of this experiment is to evaluate the relevance of the consolidation process compared to the true field data. The experimental design presented in Fig. 9 involves data collection, data analysis pa rameters and experiment output.

## 5.1.1. Data collection

True field data and road sign observations was collected for a wellknown reference track near the Continental location (Odessa ring) in Regensburg (Germany). This track is chosen for two main reasons. First, we had the true field data with real positions of all of the road signs for this track (collected manually). Second, some road signs on this track were sometimes naturally not visible from certain driving sections of the road; and thus, it was possible to obtain not only detection events but also nondetection events (negative observations), which is necessary for a better evaluation of the confidence level calculations in this proof-ofconcept experiment. This reference track is approximately 30 km long

## Table 3

Example of the confidence level calculation from a negative detection.

<table><tr><td rowspan="2"></td><td colspan="6">Confidence before the negative detection</td></tr><tr><td>60%</td><td>80%</td><td>95%</td><td>99%</td><td>99,9%</td><td>99,99%</td></tr><tr><td>Confidence after the negative detection</td><td>33%</td><td>57%</td><td>86%</td><td>97%</td><td>99,6%</td><td>99,83%</td></tr><tr><td>Decay</td><td>27%</td><td>23%</td><td>9%</td><td>2%</td><td>0,3%</td><td>0,17%</td></tr></table>

Table 4  
Table 5  
Example of the confidence level calculation from the different time interval before a negative detection.

<table><tr><td rowspan="2">Confidence before the negative detection: 89,7%</td><td colspan="5">Time interval from the last event</td></tr><tr><td>5 min</td><td>1 h</td><td>1 day</td><td>5 days</td><td>9 days</td></tr><tr><td>Confidence after the negative detection</td><td>89,68%</td><td>89,6%</td><td>87,9%</td><td>81,3%</td><td>75,7%</td></tr><tr><td>Decay</td><td>0,02%</td><td>0,09%</td><td>1,8%</td><td>8,3%</td><td>14%</td></tr></table>

and has been driven approximately 200 km in one day by two cars equipped with a Continental MFC I4.1.x camera. An embedded setup in each car was configured to send observations (vehicle path and detected road signs) every 100 m of driving in the cloud using the SENSORIS format. Similar to real traffic situations, some parts of the reference track were driven more frequently than others.

## 5.1.2. Data analysis parameters

The consolidation data processing step described in the previous sections was used to generate the clustered road sign positions with their confidence level. The consolidation process was conducted using all of the data collected during the experiment day. With regard to parti tioning the geographical data, tiles were used with an edge length of approximately 1 km. For the clustering step with the meanshift algo rithm, the optimal parameters found were 20 m for the horizontal bandwidth and 45<sup>◦</sup> for the heading bandwidth. The minimum number of observations to consider a cluster to be a potential road sign was fixed at 2. The maximum number of detections for one road sign in the reference track was 8. For each negative observation computed in the cloud, a constant probability parameter of 30% was assigned. To calculate the confidence level, the optimal half-life value found was 12 h, since the reference track was driven in only one day.

## 5.1.3. Experiment outputs

The road signs positions and their various confidence levels were compared with real road sign positions collected on the ground. A consolidated road sign was considered to exist if its confidence level was greater than 50%. Otherwise, it was considered nonexistent. The 50% existence threshold was used because the reference track was driven in only one day, with some sections in which only one or two passages occurred. This finding implies that some existing road signs were detected only once or twice during this experiment, because they were driven by only once or twice. Thus, the threshold was set to 50% to be able to consider the existence of such road signs (with a confidence level of slightly higher than 50%) in this specific context. However, in a general context with more usual driving conditions, the existence threshold should be, of course, set to a very high value (e.g., greater than

95%). For example, Table 2 shows how a confidence level of almost 99,99% can be reached after 10 detections for a given context with a half-life of 30 days and one hour between each detection. A consolidated road sign was considered to be equal to a reference sign on the ground if it was closer than 20 m and if their heading difference was smaller than 45<sup>◦</sup>. A consolidated sign can be assigned to only one reference sign, and one reference sign can have only one consolidated road sign assigned to it.

Table 5 shows the confusion matrix for camera observations versus real signs’ existences. A total of 807 camera detections was collected. They contained 733 real road sign detections (true positives) and 74 false road sign detections (false positives). A total of 297 nondetections (false negatives) was also noticed. As stated in the introduction of this paper, false detections are commonly due to specific situational prob lems, such as obstructions (e.g., other cars, physical objects such as trees), weather conditions or sensor errors [6]. These values give us a global camera detection precision of 90.8% with a recall of 71.1%. These values can be considered to be low because any loss of precision and recall represents an issue for any system or vehicle function that relies mostly on road sign detection in a single vehicle. This study is especially motivated by this result for complementing single camera detections for one vehicle with crowdsourced and consolidated road signs from the cloud.

Table 6 shows the consolidation output versus the existence of real signs. The experiment track contains a total of 76 road signs, 72 of which have been consolidated with a confidence level greater than 50% (true positives). This finding gives us a consolidation precision of 94.7%. When looking at the 4 nonconsolidated signs (or consolidated with a confidence value smaller than 50%) in relation to the false negatives, we noticed that all of them were replications of speed limitation signs that were already placed on the other side of the road, which are most frequently not visible from the vehicle’s camera. Zero false positive consolidated signs (from the previous 74 false positives detections) was also noticed. This finding gives us a consolidation recall of 100%. A total of 42 consolidated signs with confidence levels smaller than 50% (true negatives) was also noticed. These potential consolidated signs come from false positive detections, but their confidence level is very low, which lets us deduce that they do not exist.

Confusion matrix: Camera observations versus the existence of real road signs.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Camera observations</td></tr><tr><td>YES</td><td>NO</td></tr><tr><td rowspan="2">Existence</td><td>YES</td><td>733</td><td>297</td></tr><tr><td>NO</td><td>74</td><td>∞</td></tr></table>

![](/api/attachments/RYJAMXWW/fulltext/images/c5ece4241abae32ed03f4b3868e3f843d41bbd31a16bcdfefbccee473d421eae.jpg)  
Fig. 9. Comparison with true field data experimental design.

Table 6  
Confusion matrix: Consolidations versus the existence of real road signs.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Consolidations</td></tr><tr><td>YES</td><td>NO</td></tr><tr><td rowspan="2">Existence</td><td>YES</td><td>72</td><td>4</td></tr><tr><td>NO</td><td>0</td><td>42</td></tr></table>

To simulate the case of the possible disappearance of road signs, the consolidation process was simply relaunched with the same data 5 days after the data collection. In this configuration, this approach can simu late a lack of information (no event) about all of these road signs for 5 days. The aging modeling in the confidence level calculation (e.g., as in the timeframe $\mathrm { T } _ { 5 }$ to $\mathrm { T } _ { 1 0 }$ in Fig. 8) came into play (with a half-life of 12 h in this experiment), and almost all of the road signs’ confidence levels fell to approximately 50%. The effects would be the similar, but with a faster decay (even below 50%), in the case of multiple successive non detection events for a road sign (e.g., as in the timeframe $\mathrm { T } _ { 1 5 }$ to $\mathrm { T } _ { 2 0 }$ in Fig. 8).

Finally, this experiment shows that the consolidation process is relevant by reducing the false positive detection rate by 100% and increasing the true positive detections from 90.8% to 94.7%. All of the nonconsolidated signs are due to the nonvisibility of these signs by the vehicle’s camera. These marginal cases can help to detect the signs that drivers cannot see, which can contribute to improve the way that the signs are placed on the road’s infrastructure.

## 5.2. Experiment 2: simulated fusion of camera detections and consolidated road signs versus camera detections only

The goal of this experiment is to estimate the relevance of an in vehicle system that can use both road sign camera detections and consolidated road signs from the cloud to provide more relevant and up to-date information to the driver or to other embedded vehicle func tions. The design of this experiment is presented in Fig. 10. First, consolidated road signs from crowdsourced detections was considered up-to-date (as in the previous experiment). Second, two cars driving thi reference track in real time was used. Both cars were equipped with cameras that can detect road signs. However, one of the cars could also download from the cloud the up-to-date consolidated road signs that potentially apply to its driving area. The goal of the experiment was to evaluate the performance in terms of true positive, false positive and false negative detections for both systems.

## 5.2.1. Data collection

This experiment uses the same reference track that was used for the previous experiment, but both the cars drive only a portion of the 22.5 km of the track that concentrates most of the road signs. For the consolidated signs, only consolidated outputs from the previous exper iment were used. Both cars were equipped with the same Continental camera model MFC I4.1.x.

## 5.2.2. Data analysis parameters

With regard to the car with only the camera, all of the road signs that were detected by the camera during the driving session were considered. For the other car, which is also supposed to fuse the consolidated road signs, all of the detections of the camera merged with the consolidated road signs were considered. The merging operation prioritizes the consolidated road signs with the following rules (Fig. 11):

• If the confidence level of a consolidated sign was greater than 80%, the sign was considered to exist, even if the same sign was not visible by the camera in a driving session;

• If the confidence level of the consolidated sign was smaller than 50% or if there was no consolidated sign, the sign was considered nonexistent;

• If the confidence level of the sign was between 50% and 80%, two cases were relevant: (i) if the camera detects the sign, then the sign was considered to exist; and (ii) if the camera does not detect the sign, then the sign was considered nonexistent.

## 5.2.3. Experiment outputs

Table 7 compares both systems in terms of the true positives (TP), true positive rate (TPR), false negatives (FN), false negative rate (FNR), false positives (FP) and false positive rate (FPR). These results clearly show that the combined system that uses consolidated road signs along with camera detections can improve by 6.7% the true positive rate, while reducing by 33.5% the false negative rate and by 94.4% the false positive rate.

If we consider only the speed limitation road signs, which are detected more efficiently by the cameras used in this experiment, better results are obtained for the combined system (Table 8): improvement by 3.6% of the true positive rate, and reduction by 100% of the false negative rate and of the false positive rate.

![](/api/attachments/RYJAMXWW/fulltext/images/ea30159fe7a772469fb72b6dc373c5cd61cd06ed3d823465ec218c99e9fd51e7.jpg)  
Fig. 10. Comparison of an in-vehicle system with and without consolidated road signs.

![](/api/attachments/RYJAMXWW/fulltext/images/83fb51e2138fa8308f24ac66defb61dbbc5eb06164738ede4f2e3124f7ad93a2.jpg)  
Fig. 11. Merging strategy of a consolidated road sign with a camera road sign detection.

Table 7  
Results of the comparison between the two systems for all road signs.

<table><tr><td></td><td>TP</td><td>TPR</td><td>FN</td><td>FNR</td><td>FP</td><td>FPR</td></tr><tr><td>Camera only</td><td>649</td><td>80.1%</td><td>161</td><td>19.9%</td><td>17</td><td>2.6%</td></tr><tr><td>Consolidated signs + camera</td><td>702</td><td>86.8%</td><td>107</td><td>13.2%</td><td>1</td><td>0.1%</td></tr><tr><td>Improvement</td><td></td><td>6.7%</td><td></td><td>33.5%</td><td></td><td>94.4%</td></tr></table>

## Table 8

Results of the comparison between the two systems for only speed limitation signs.

<table><tr><td></td><td>TP</td><td>TPR</td><td>FN</td><td>FNR</td><td>FP</td><td>FPR</td></tr><tr><td>Camera only</td><td>265</td><td>96.4%</td><td>10</td><td>3.6%</td><td>7</td><td>2.6%</td></tr><tr><td>Consolidated signs + camera</td><td>275</td><td>100%</td><td>0</td><td>0%</td><td>0</td><td>0%</td></tr><tr><td>Improvement</td><td></td><td>3,6%</td><td></td><td>100%</td><td></td><td>100%</td></tr></table>

## 6. Discussion and implications

As part of a proof of concept, two experiments in real driving con ditions and with collected true field data was designed. The first experiment clearly shows a non-negligible proportion of false positives and false negatives when using only camera road sign detections (recall of 71.1%, precision of 90.4%). It also shows the relevance of the pro posed approach to correctly computing the real up-to-date positions of the road signs while eliminating almost totally the false positives and false negatives (recall of 100%, precision of 94.8%). The second experiment simulates a simple merging strategy of consolidated road signs along with camera detections in real driving situations. This experiment clearly demonstrates the relevance of the merged system compared to the sole usage of the camera: up to 100% improvement in the false positive rate and false negative rate depending on the type of road sign.

## 6.1. Contributions

The methodology in this paper provides more regular updates of road signs by using crowdsourced vehicle sensor data. This approach repre sents a significant contribution because, to the best of our knowledge, it might be quite new in the relevant research field—we could not find a single published research study on this specific topic. Even if some map providers, such as HERE [29], already have looked into this topic, their proposition is very lightly detailed and appears to be simplistic and not robust. Beyond the fact that the proposal of a platform aims at handling the technical and functional requirements related to this topic in a big data context, the other contribution in this paper resides in the proposed method to consolidate crowdsourced road sign observations to obtain up-to-date road signs with their associated confidence levels (existence probability). An adapted clustering technique (meanshift algorithm) is used with an appropriate distance and a refinement step for handling the specific case of sign detections. In addition, a confidence level calcula tion algorithm that is based on exponential decay (to model information aging) and on Bayesian probabilities is proposed. It iteratively computes a current event (detection or nondetection) probability based on the previous event. At each moment, this calculation can estimate the ex istence probability of a clustered sign. As we have seen in the experi ments, these probabilities are relevant to filtering the consolidated false positive and false negatives detections by applying a confidence threshold.

## 6.2. Implications

## 6.2.1. Practical implications

The proposal in this paper could have direct implications in improving connected driving and even autonomous driving in the future. First, it can help car manufacturers to improve their current strategy with regard to continuously providing the most up-to-date road restrictions information (e.g., speed limitations) to drivers. As shown in the second experiment, the use of near real-time crowdsourced and consolidated road signs can substantially improve the information ac curacy compared with a system that is mainly based on single vehicle camera detections. Therefore, driving will be found to be easier and safer for any car user.

Second, the proposal can help to market players such as map pro viders, GPS providers or GPS navigation software providers to improve the frequency with which the map can be updated in its layers, including road objects such as road sign information (e.g., speed limitation layers). The approach also allows an easy and automatic consolidation of changes in the road sign infrastructure, which can contribute to providing more frequent updates to the corresponding map layers. In addition, the short lifecycle of temporary road signs (e.g., in the case of road work) could also be easily managed by means of the time-aware and aging approach for the road sign confidence level calculation. These market players could also directly partner with car manufacturers to fuse these outputs with on-board cameras data.

Third, by comparing the consolidated result with the available true field data, the proposal can also help to quickly identify potentially misplaced road signs or those not visible to vehicles’ cameras (and potentially not visible to the driver). Thus, this approach can be used, for example, to identify and facilitate an efficient positioning of the mis placed road signs by the operators that control the maintenance of the road infrastructure.

## 6.2.2. Research implications

To the best of our knowledge, this study is the first research study on the automatic updating of road signs based on crowdsourced in-vehicle cameras’ detections. This paper focused especially on how to compute the clustering and the confidence level of road signs. Future research can rely on this study to extend or improve the proposal, replicating the method or combining it with others, to obtain more robust findings. In this regard, alternative relevant methods could also be studied and compared. Moreover, it appears that it is important to develop more indepth research on related issues (e.g., security, privacy, safety, scalability).

## 6.3. Limitations and directions for future research

Limitations or improvements to be made can be divided into three categories: at the experimental level, on the various research features, and on the algorithm.

The proposed platform is designed to be scalable and flexible for handling big data. As a proof of concept, the experiments presented in this paper primarily focus on demonstrating the functional relevance of the approach with a well-known driven track and true field data. Other proof-of-concepts are currently developed with car manufacturers to evaluate the functional and technical robustness of the proposal. For the technical robustness, large-scale simulations with artificial data to demonstrate the scalability and the resilience of the platform are plan ned. For the functional robustness, the experiments must be extended to explicitly address specific situations, such as road signs on more or less driven roads, while accounting for national specificities. Conceptually, some parameters, such as the half-life, the probability of negative de tections, the horizontal and heading bandwidth, the lengths of the tiles, or the confidence level threshold, must be evaluated for specific situations.

With regard to any improvements on the features, we are also working on handling other road sign elements, such as supplementary signs (e.g., direction subsigns, time subsigns) in the process when this information is available. As presented in the methodology, we also plan to work on the subsequent steps and especially on how to use the consolidation outputs to continuously update and distribute map ex tensions or layers. The confidence level provided by this study could also help in designing in-vehicle fusion strategies between crowdsourced digital maps’ information and on-board real-time cameras’ detections. In experiment 2, the fusion of the camera detections with consolidated signs provides a simulated use case that integrates the consolidated confidence level values. However, since this fusion mechanism is an on board car feature, the effective merging rules should also be studied by considering other parameters, such as the real update frequency of the digital map and the quality of the camera’s detections, which could also depend on the environment conditions where the car is located (e.g., weather or traffic conditions). These rules should consider cases of conflict (contradictory information) between the digital map informa tion and the camera output. Usually, the camera’s detections should prevail (as can be seen in most existing fusion systems), because they are expected to provide the most updated information for the current driving situation. However, false positive detections or detections that do not apply to the current road are some issues. To improve these systems, we believe that the camera’s detections should be contrasted by considering other parameters (e.g., the freshness and the confidence level of the information in the digital map, the driving environment conditions, the quality of the camera’s detections). Regardless of the origin of the information, the impacts of the false positives and false negatives are not the same in real driving situations and should also be considered. With regard to false positives, this consideration could definitely cause drivers to distrust the system, whereas false negatives tend to be more tolerated by drivers. Thus, only road signs with very high confidence levels (e.g., greater than 95%) should be used in onboard fusion mechanisms.

To improve the algorithms, other density-based clustering algo rithms that perform well in discovering clusters in large spatial data bases with noise [43] could also be evaluated in experiments. We could even consider making the clustering algorithm configurable. Moreover, there is a need to improve the computation of the negative observations in the algorithm through some characterization, with a specific proba bility feature. For example, by integrating weather-related data in cases of negative observations, such observations could be better explained and are more likely to impact the event. Finally, a large-scale deploy ment with cars equipped with different types of sensors (e.g., cameras) should consider the differences in terms of the detection qualities for each sensor type in the process.

The proposed methodology is also applicable to other contexts beyond road sign detection, such as, for instance personalized or recommender systems. Such systems generally require the modeling of the user profile (e.g. with weighted user interests) which evolves over time based on user interactions [44]. We believe that the confidence level calculation process that tracks the changes in the confidence level of a road sign over time could also be suitable in such systems to track the dynamic weights of user interests over time.

## 7. Conclusions

We presented a methodology for providing near real-time updates of road sign infrastructure for connected vehicles. This methodology relies on crowdsourced data from vehicle sensors that are aggregated and consolidated in the cloud. The platform that supports this methodology is designed to work in realistic contexts and considers not only func tional requirements but also requirements related to security and pri vacy as well as more requirements for managing big data. In this paper, the focus was on the functional aspect of consolidating crowdsourced sensor data to provide regular accurate and up-to-date positions of the road signs. The main challenge was related to how to filter noise that resulted from multiple imprecise positioning data and noise due to false positive and false negative detections, because they occur very often and are attributed to factors such as the weather, natural obstructions, traffic conditions, or sensor errors. As proof of concept, true field data was used to evaluate two experiments on a well-known reference track. These two experiments clearly demonstrated the relevance of the proposed approach, which could significantly contribute to making connected driving easier and safer. Therefore, entities such as car manufacturers, map providers, GPS providers or road network managers could take advantage of this approach. On the other hand, this study opens up several future research directions for improving the proposal in ITS or in other research fields.

## CRediT authorship contribution statement

Dieudonne ´ Tchuente: Conceptualization, Software, Validation, Writing - original draft, Writing - review & editing. Dominik Sen ninger: Conceptualization, Methodology, Software, Validation, Formal analysis, Writing - review & editing. Holger Pietsch: Supervision, Project administration, Conceptualization. Danilo Gasdzik: Software, Validation.

## Acknowledgments

This study has been done by the Continental AG company through the eHorizon project of the Vehicle Networking and Information business area. In France, this project was funded by the French “investment for the future program” (PIA) operated by the ADEME agency. The project is also supported by the Occitanie region and Toulouse Metropole.

## D. Tchuente et al.

## References

[1] D. Ni, Traffic Flow Theory: Characteristics, Experimental Methods, and Numerical Techniques, Butterworth-Heinemann, 2015, https://doi.org/10.1016/C2015-0- 01702-6.

[2] K.N. Qureshi, A.H. Abdullah, A survey on intelligent transportation systems, Middle-East J. Sci. Res. 15 (2013) 629–642, https://doi.org/10.5829/idosi. mejsr.2013.15.5.11215.

[3] K. Dahal, K. Almejalli, M.A. Hossain, Decision support for coordinated road traffic control actions, Decis. Support. Syst. 54 (2013) 962–975, https://doi.org/10.1016/ i.dss.2012.10.022.

[4] B. Ryder, B. Gahr, P. Egolf, A. Dahlinger, F. Wortmann, Preventing traffic accidents with in-vehicle decision support systems-the impact of accident hotspot warnings on driver behaviour, Decis. Support. Syst. 99 (2017) 64–74, https://doi.org/ 10.1016/j.dss.2017.05.004.

[5] K. Islam, R. Raj, Real-time (vision-based) road sign recognition using an artificial neural network, Sensors. 17 (2017) 853, https://doi.org/10.3390/s17040853.

[6] S.B. Wali, M.A. Abdullah, M.A. Hannan, A. Hussain, S.A. Samad, P.J. Ker, M. Bin Mansor, Vision-based traffic sign detection and recognition systems: current trends and challenges, Sensors. 19 (2019) 2093, https://doi.org/10.3390/s19092093.

[7] A.-S. Puthon, F. Nashashibi, B. Bradai, A complete system to determine the speed limit by fusing a GIS and a camera, in: 2011 14th Int. IEEE Conf. Intell. Transp. Syst, IEEE, 2011, pp. 1686–1691, https://doi.org/10.1109/ITSC.2011.6082951.

[8] J. Daniel, J.-P. Lauffenburger, Fusing navigation and vision information with the transferable belief model: application to an intelligent speed limit assistant, Inf. Fusion. 18 (2014) 62–77, https://doi.org/10.1016/j.inffus.2013.05.013.

[9] M.A. Quddus, W.Y. Ochieng, R.B. Noland, Current map-matching algorithms for transport applications: state-of-the art and future research directions, Transp. Res. Part C Emerg. Technol. 15 (2007) 312–328, https://doi.org/10.1016/j trc.2007.05.002.

[10] D. Zubach. How to Implement OTA Updates for Connected Cars. https://www,int ellias.com/how-to-realize-ota-updates-for-connected-cars/, 2018.

[11] Mapscape, Incremental Updating, 2020. http://www.mapscape.eu/telema tics/incrementalupdating.html (accessed July 19, 2020).

[12] A. Amini, R.M. Vaghefi, M. Jesus, R.M. Buehrer, Improving GPS-based vehicle positioning for intelligent transportation systems, in: 2014 IEEE Intell. Veh. Symp. Proc, IEEE, 2014, pp. 1023–1029, https://doi.org/10.1109/IVS.2014.6856592.

[13] L. Zhu, F.R. Yu, Y. Wang, B. Ning, T. Tang, Big data analytics in intelligent transportation systems: a survey, IEEE Trans. Intell. Transp. Syst. 20 (2018) 383–398, https://doi.org/10.1109/TITS.2018.2815678.

[14] K. Ali, D. Al-Yaseen, A. Ejaz, T. Javed, H.S. Hassanein, Crowdits: Crowdsourcing in intelligent transportation systems, in: 2012 IEEE Wirel. Commun. Netw. Conf, IEEE, 2012, pp. 3307–3311, https://doi.org/10.1109/WCNC.2012.6214379.

[15] A. Misra, A. Gooze, K. Watkins, M. Asad, C.A. Le Dantec, Crowdsourcing and its application to transportation data collection and management, Transp. Res. Rec. 2414 (2014) 1–8, https://doi.org/10.3141/2414-01.

[16] X. Wang, X. Zheng, Q. Zhang, T. Wang, D. Shen, Crowdsourcing in ITS: the state of the work and the networking, IEEE Trans. Intell. Transp. Syst. 17 (2016) 1596–1605. https://doi.org/10.1109/TITS.2015.2513086

[17] S. Zourlidou, M. Sester, Traffic regulator detection and identification from Crowdsourced data—a systematic literature review. ISPRS Int. J. Geo-Information 8 (2019) 491, https://doi.org/10.3390/ijgi8110491.

[18] E.P. Dennis, R. Wallace, B. Reed, Crowdsourcing transportation systems data, in: Michigan Dep. Transp. REQ, 2015.

[19] K. Chen, M. Lu, G. Tan, J. Wu, CRSM: Crowdsourcing based road surface monitoring, in: 2013 JEEE 10th Int. Conf, High Perform, Comput, Commun. 2013 IEEE Int. Conf. Embed. Ubiquitous Comput, IEEE, 2013, pp. 2151–2158, https:// doi.org/10.1109/HPCC.and.EUC.2013.308.

[20] A.S. El-Wakeel, J. Li, M.T. Rahman, A. Noureldin, H.S. Hassanein, Monitoring road surface anomalies towards dynamic road mapping for future smart cities. in: 2017 IEEE Glob. Conf. Signal Inf. Process, IEEE, 2017, pp. 828–832, https://doi.org/ 10.1109/GlobalSIP.2017.8309076.

[21] S. Sattar, S. Li, M. Chapman, Road surface monitoring using smartphone sensors: a review, Sensors. 18 (2018) 3845, https://doi.org/10.3390/s18113845.

[22] F. Carrera, S. Guerin, J.B. Thorp, By the people, for the people: the crowdsourcing of “streetbump”: an automatic pothole mapping app, Int. Arch. Photogramm. Remote. Sens. Spat. Inf. Sci. 40 (2013) 19–23, https://doi.org/10.5194 isprsarchives-XI-4-W1-19-2013

[23] V.S.F. Enigo, T.M.V. Kumar, S. Vijay, K.G. Prabu, CrowdSourcing based online petitioning system for pothole detection using android platform, Procedia Comput. Sci. 87 (2016) 316–321, https://doi.org/10.1016/j.procs.2016.05.167.

[24] A. Fox. B.V.K.V. Kumar. J. Chen. F. Bai. Multi-lane pothole detection from crowdsourced undersampled vehicle sensor data, IEEE Trans. Mob. Comput. 16 (2017) 3417–3430, https://doi.org/10.1109/TMC.2017.2690995.

[25] X. Li, R. Chen, T. Chu, A crowdsourcing solution for road surface roughness detection using smartphones, in: Proc. 27th Int. Tech. Meet. Satell. Div. Inst. Navig. GNSS, 2014, pp. 498–502.

[26] K. Zang, J. Shen, H. Huang, M. Wan, J. Shi, Assessing and mapping of road surface roughness based on GPS and accelerometer sensors on bicycle-mounted smartphones, Sensors. 18 (2018) 914. https://doi.org/10.3390/s18030914.

[27] Mappillary, Mapillary Automated Traffic Sign Inventory. https://www.mapillary. com/usecase/traffic-sign-inventory, 2020 (accessed July 17, 2020).

[28] M. Arnesdotter, Automating the Process: Collecting Traffic Sign Data in Clovis. https://blog.mapillary.com/update/2018/11/14/streamlining-traffic-sign-inven tory-in-clovis.html, 2018 (accessed October 19, 2019).

[29] J. Stevenson, HERE Road Signs Service Points Way to Autonomous Future. https ://360.here.com/2016/11/21/here-road-signs-service-points-way-to-autonomous -future/, 2016.

[30] Continental eHorizon Project. https://www.continental-automotive.com/en-gl/ Passenger-Cars/Vehicle-Networking/Software-Solutions-and-Services/eHorizon, 2020 (accessed July 17, 2020).

[31] M. Myers, C. Adams, D. Solo, D. Kemp, Internet X. 509 certificate request message format. Req, Comments. 2511 (1999)

[32] N. Sakimura, J. Bradley, M. Jones, B. de Medeiros, C. Mortimore, OpenID Connect Core 1.0 incorporating errata set 1. in: OpenID Found. Specif, 2014.

[33] M. Zaharia, M. Chowdhury, M.J. Franklin, S. Shenker, I. Stoica, Spark: cluster computing with working sets, HotCloud. 10 (2010) 95.

[34] P.B. Keenan, Spatial decision support systems for vehicle routing, Decis. Support. Syst. 22 (1998) 65–71, https://doi.org/10.1016/S0167-9236(97)00054-7.

[35] L. Santos, J. Coutinho-Rodrigues, C.H. Antunes, A web spatial decision support system for vehicle routing using Google maps, Decis. Support. Syst. 51 (2011) 1–9, https://doi.org/10.1016/j.dss.2010.11.008.

[36] G. McNeill, S.A. Hale, Generating tile maps, in: Comput. Graph. Forum, Wiley Online Library. 2017, pp. 435–445. https://doi.org/10.1111/cgf.13200.

[37] C. Willing, K. Klemmer, T. Brandt, D. Neumann, Moving in time and space–location intelligence for carsharing decision support. Decis, Support. Syst, 99 (2017) 75–85 https://doi.org/10.1016/i.dss.2017.05.005.

[38] J. Schwartz, Bing maps tile system, Microsoft Dey. Netw. Available Http//Msdn. Microsoft. Com/En-Us/Library/Bb259689. Aspx, 2009.

[39] Y. Cheng, Mean shift, mode seeking, and clustering, IEEE Trans. Pattern Anal. Mach. Intell. 17 (1995) 790–799, https://doi.org/10.1109/34.400568.

[40] X. Jiang, L. Wan, X. Wang, S. Ge, J. Liu, Effect of exponential decay in hydraulic conductivity with depth on regional groundwater flow, Geophys. Res. Lett. 36 (2009), https://doi.org/10.1029/2009GL041251.

[41] E.A. Hughes, A. Zalts, Radioactivity in the classroom, J. Chem. Educ. 77 (2000) 613, https://doi.org/10.1021/ed077p613.

[42] H. Bao, O. Li, S.S. Liao, S. Song, H. Gao, A new temporal and social PMF-based method to predict users’ interests in micro-blogging, Decis. Support. Syst. 55 (2013).698–709 https://doi org/10.1016/i dss 2013.02.007

[43] M. Ester, H.-P. Kriegel, J. Sander, X. Xu, A density-based algorithm for discovering clusters in large spatial databases with noise, in: Kdd, 1996, pp. 226–231.

[44] S. Ding, Y. Li, D. Wu, Y. Zhang, S. Yang, Time-aware cloud service recommendation using similarity-enhanced collaborative filtering and ARIMA model, Decis. Support. Syst. 107 (2018) 103–115, https://doi.org/10.1016/j.dss.2017.12.012
