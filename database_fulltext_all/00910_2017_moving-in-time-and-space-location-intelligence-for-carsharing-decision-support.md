---
otero_id: 910
otero_key: "ZVYHT3M5"
title: "Moving in time and space – Location intelligence for carsharing decision support"
authors: "Christoph Willing; Konstantin Klemmer; Tobias Brandt; Dirk Neumann"
year: "2017"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.05.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Moving in time and space – Location intelligence for carsharing decision support

Christoph Willing <sup>a</sup>, Konstantin Klemmer <sup>b</sup>, Tobias Brandt <sup>c,</sup>⁎, Dirk Neumann

<sup>a</sup> University of Freiburg, Germany

<sup>b</sup> Imperial College London, United Kingdom

<sup>c</sup> Rotterdam School of Management, Erasmus University, Netherlands

## a r t i c l e i n f o

Article history: Received 5 October 2016 Received in revised form 12 April 2017 Accepted 4 May 2017 Available online xxxx

Keywords: Carsharing Spatial analytics Location-based services Spatial decision support system

## a b s t r a c t

In this paper we develop a spatial decision support system that assists free-floating carsharing providers in countering imbalances between vehicle supply and customer demand in existing business areas and reduces the risk of imbalance when expanding the carsharing business to a new city. For this purpose, we analyze rental data of a major carsharing provider in the city of Amsterdam in combination with points of interest (POIs). The spatiotemporal demand variations are used to develop pricing zones for existing business areas. We then apply the influence of POIs derived from carsharing usage in Amsterdam in order to predict carsharing demand in the city of Berlin. The results indicate that predicted and actual usage patterns are very similar. Hence, our approach can be used to define new business areas when expanding to new cities to include high demand areas and exclude low demand areas, thereby reducing the risk of supply-demand imbalance.

© 2017 Elsevier B.V. All rights reserved.

## 1. Introduction

Over the coming years, urban mobility challenges, such as traffic jams, parking shortage, noise pollution and harmful emissions, are only expected to worsen due to cities growing in size and an increase in the urban population [36]. Over the last two decades, carsharing has established itself as a novel mode of transportation [33] and the more recent introduction of station-less free-floating carsharing (FFCS) has been deemed particularly promising in addressing the above-mentioned issues by providing a more sustainable and more environmentally friendly form of urban mobility [3,14].

Due to the relatively recent emergence of FFCS, providers are still in an experimental stage, operating under uncertainty and constantly adapting their customer offering. Thus, they can particularly benefit from decision support systems (DSS) to assist in strategic decision making and to advance their business model. Moreover, the transportation sector, with its complex modelling problems and large amounts of data being generated, is ideally situated to take advantage of analyticsenabled DSS [12,17,21]. Therefore, in this paper we introduce a spatial decision support system (SDSS), which we also test with real-world carsharing rental data, to aid in two specific areas of FFCS, namely demand-supply balancing and expansion planning.

The practice of carsharing dates back to as early as 1948 in Switzerland [34]. Recent advancements in information technology (IT), along with the widespread adoption of smartphones and mobile internet, have enabled the most flexible form of carsharing yet: free-floating carsharing. In contrast to traditional station-based carsharing, this system allows customers to start and end a rental anywhere within a predefined operating area, the border of which will often be similar to the boundaries of the city. Smartphones are used to locate and unlock vehicles, and drivers are subsequently charged on a per-minute and/ or per-mile (per-kilometer) basis.

The increased flexibility of the free-floating model however, comes at the cost of greater complexity. Because users are free to leave their rental vehicles wherever they please, cars are not necessarily always located where they are needed most. As a consequence, providers are required to conduct costly relocations of vehicles to rebalance supply and demand, which continues to be the main challenge they are facing [38– 40]. In order to understand how these supply-demand imbalances develop, it is necessary to first understand the dynamics behind FFCS activity. Hence, the first research question we address in this paper is:

RQ 1: How does carsharing usage vary over time and space, and what drives these variations?

To answer this question, we employ a geographic information system (GIS) to analyze historical FFCS rentals in the city of Amsterdam and are able to show that variations in carsharing usage are driven by different categories of points of interest (POIs).<sup>1</sup> The influence of these POIs, however, varies depending on the hour of the day. The results of

C. Willing et al. / Decision Support Systems xxx (2017) xxx–xxx

this analysis can then be used in our proposed SDSS prototype to derive pricing strategies aimed at reducing the supply-demand imbalance, thereby also reducing the need for vehicle relocation.

Another way of reducing the need for relocation is to define an operating area with limited dead spots – areas of low demand where parked vehicles ‘get stuck’ and from which they require relocation. Carefully choosing the boundaries of an operating area is especially challenging for providers when moving into a new city. Usually, there is no historical rental information available from which customer demand can be inferred. Therefore, the second research question we aim to answer is:

RQ 2: How can FFCS operators decide on the operating area when entering a new city?

Our proposed SDSS again makes use of POI data. Based on the POIs' estimated influence on FFCS dynamics in the city of Amsterdam, we predict carsharing demand for the city of Berlin. Our results show that predicted demand is, in fact, very similar to actual historical carsharing demand and that this approach can thus be used to define operating areas when expanding into new cities.

The measures derived from the two research questions have the potential to reduce the need for costly provider-based relocation. Thus, our proposed SDSS reduces operational costs while also helping in strategic decision-making with regard to business expansion.

In the next section, we motivate our approach by reviewing prior related research. Thereafter, we present the structure of our SDSS prototype. In Section 4, we describe the dataset, and subsequently present the methodology to evaluate the proposed SDSS approach in Section 5. We then continue by discussing the performance of the SDSS prototype in Section 6 and provide concluding remarks in Section 7.

## 2. Related work

Carsharing provides users with the flexibility of personal car travel without the fixed costs associated with personal cars – such as the purchase price, maintenance and insurance cost –thereby increasing personal mobility [11,34]. In consequence, the usage of carsharing (and other alternative forms of transportation such as bikesharing, ride-sharing, and e-hailing) has expanded significantly over the past several years [33]. Naturally, academia has also developed a considerable interest in carsharing. There have been multiple studies addressing a number of topics including, for example, its role as a prime example of the sharing economy [4], studying user behavior [24], estimating its environmental impact [14], evaluating its integration with other modes of transport [26,41], assessing its potential to provide relief to overburdened urban mobility systems [25], and finding solutions to operational challenges – most notably the relocation problem [39,40]. An answer to the relocation issue is especially crucial to ensure more widespread adoption, since a persistent supply-demand imbalance might cause users to become frustrated and unwilling to regard carsharing as a viable and reliable transportation alternative.

Geographic information systems play an important role in solving these challenges. Since they are employed to aid decision-making, the term is used interchangeably with spatial decision support system and spatial business intelligence (SBI) [13].

## 2.1. Carsharing demand estimation

Understanding carsharing demand is a prerequisite for solving the relocation problem, as it enables one to predict when and where demand-supply imbalances are likely to occur, so that providers can implement countermeasures. Multiple authors have studied carsharing demand over the past several years and publications up to 2012 have been summarized by Jorge and Correia [19]. The authors conclude that most studies do not, or only insufficiently, consider the supply side of carsharing, which directly impacts demand, and how to find the right balance between the two. Furthermore, demand models are too context-specific and not widely applicable to other providers and locations.

Thus, they call for more realistic models, especially for one-way carsharing, which are then also tested in a real-world environment.

Since then, Ciari, Bock, and Balmer [9] and Balac, Ciari, and Axhausen [2] have employed the MATSim software, a multi-agent simulation tool, to model carsharing demand as part of the daily activities of relevant customer groups in Zurich. In doing so, they considered both the spatial and temporal variations in demand during a workday. Schmöller, Weikl, Müller, and Bogenberger [31] analyze actual FFCS dynamics in Munich and Berlin and show that demand concentrates around temporal peaks and spatial ‘hot spots’. Additionally, they found that demographic factors influence long-term demand patterns while weather conditions influence short-term demand dynamics.

There are two sides to carsharing demand: firstly, when and where people are in need of carsharing and, secondly, how and for what purpose they use carsharing. Surveying current and potential customers revealed that the purpose of a carsharing trip, and thus a major influence on carsharing demand, is often associated with specific locations, or points of interest (POIs), which drivers want to reach [7]. Wagner et al. [37] have investigated this relationship empirically and were able to show that FFCS demand is indeed driven by POIs within the provider's operating area. They applied a geographic information system, which uses rental data of a leading FFCS provider in Berlin in conjunction with POIs extracted from Google Maps. Running a zero-inflated regression revealed that the proximity of certain POI categories, such as nightclubs or shopping malls, is associated with higher carsharing demand. They subsequently applied their model to predict demand in areas just outside the operating area, which were later included by the provider. This allowed them to demonstrate that their predicted demand was in fact a good indicator of what turned out to be the observed rental density after these areas were incorporated into the provider's service area.

In this paper, we extend their approach in two ways. First, we add the temporal dimension to the estimation of demand and test whether and in what way POI influence changes over the course of the day. Additionally, we then examine whether their approach can also be used to predict demand in a different city, for which the provider does not yet have any information about carsharing dynamics.

## 2.2. Carsharing relocation problem

The carsharing relocation problem has arisen with the introduction of one-way, station-based carsharing and as such has been extensively discussed in academic literature (see [8,19] for an overview of these studies). FFCS can be regarded as a form of one-way carsharing with an infinite number of stations and, more recently, researchers have also begun investigating the FFCS relocation problem from an information systems (IS) perspective [6,39]. In general, relocation strategies can be divided into two approaches: operator-based relocation and userbased relocation. We next provide an overview of the most relevant studies.

## 2.2.1. Operator-based relocation

Based on historical trip patterns, Kek, Cheu, Meng, and Fung [22] develop a DSS for station-based carsharing operators, which enables proactive relocation instead of reactive relocation. Based on an Optimization-Trend-Simulation they minimize the cost of staff-based relocation, i.e. staff time, and the cost of unfulfilled customer demand. For FFCS the optimization becomes more complex. Weikl and Bogenberger [39] conceptualize a dual approach, which consists of an offline module that predicts longer-term demand variations and which is enhanced by an online module to track real-time demand, thereby enabling proactive relocation by providers. In a subsequent paper they extend their approach of profit-maximizing relocations and evaluate its implementation in real-world test cases in Munich [40]. To do so, they divide the operating area into zones to mimic stations and consequently distinguish inter- and intra-zone relocations. Using optimization and rule-

Please cite this article as: C. Willing, et al., Moving in time and space – Location intelligence for carsharing decision support, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.05.005

![](/api/attachments/ZVYHT3M5/fulltext/images/c2e9586c8e7704235e4fb381b4418f46a1d410380a222c3fad924ef942426f13.jpg)  
Fig. 1. Schematic visualization of SDSS part 1 – pricing design to reduce supply-demand imbalance.

based methods, they minimize the cost of staff-based relocation and the field tests have yielded a profit increase of 5.8% and a decrease in mean idle times of vehicles of up to 4%.

## 2.2.2. User-based relocation

A user-based approach to relocation is desirable because in most cases it is more cost-efficient than operator-based relocation and contributes to the self-regulation of the balance between supply and demand. In these approaches, customers are offered financial incentives to relocate vehicles. Early strategies in station-based systems included trip-joining to oversupply stations and trip-splitting to undersupply stations [5]. Clemente, Fanti, Mangini, and Ukovich [10] use timed petri nets to model user willingness to relocate electric vehicles in a station-based carsharing system in such a way that supply at the different stations is balanced. In a similar manner, but in an FFCS environment, Wagner et al. [38] simulate user-based relocation by predicting idle times at the rental's destination and offering users an incentive to park at a nearby spot with lower expected idle time. This approach however requires users to communicate their destination at the beginning of their trip.

Schulte and Voß [32] propose another DSS for FFCS relocation. Akin to Weikl and Bogenberger [39], they use regression analysis to estimate long-term demand patterns over time, which are then used to develop relocation strategies. These are enhanced by the application of neural networks to incorporate short-term forecasts based on current vehicle locations, thus enabling real-time adjustment of the long-term relocation strategies. This model can be used to achieve either the most cost-efficient or the most environmentally friendly (CO2-efficient) results. Based on the provider's primary goal, one of four relocation strategies is offered to users: (1) incentives to book a more distant vehicle, (2) incentives to opt for a more distant drop-off location, (3) paid relocation, and (4) demand pooling.

While all of these studies require either a change in user or operator behavior to achieve relocation, there have also been several studies which aim to implement implied user-based relocation by designing the system in such a way that the need for active relocation is reduced. This includes optimal shaping of the operational area by including ‘hot spots’ and excluding ‘cold spots’ [37], optimal placement of stations [35], or variable trip pricing [20]. The latter was evaluated for a station-based, one-way carsharing system, which demands higher prices for trips that increase imbalance and lower prices for trips that reduce imbalance [20]. To the best of our knowledge, however, trip-based pricing has not yet been considered as a means of rebalancing FFCS systems.

## 3. SDSS outline

Reducing the need for relocation is the most cost-efficient approach to achieving a more balanced FFCS system. In our own analyses, therefore, we consider two cases suggesting how this might be achieved – first, for existing operations, by introducing pricing zones, and second, for expanding operations, by choosing the appropriate operating area for new cities. In this section, we outline our approach before describing the data and methodology behind it.

## 3.1. Location intelligence for existing areas

In FFCS systems there are not stations, but rather areas of higher demand, which exhibit a higher density of trips, and areas of lower demand, which are less frequented by customers. In this paper we use end points as a proxy for carsharing demand for two reasons. First, we are interested in carsharing usage in general and, as shown by Celsor and Millard-Ball [7], the destination of a carsharing trip is a strong determinant of one of the two types of carsharing demand – especially in a free-floating, one-way carsharing system. The second reason is that in a free-floating system, the destinations of the trips are independent observations, but trip origins are not. In other words, carsharing users can freely choose where to end their trip but not necessarily where to start it, because this depends on the availability, or supply, of cars at a certain location and point in time. It is thus challenging to determine starting point demand in a free-floating carsharing system based on rental data, as there might be unobserved demand in areas without any data points. Nevertheless, in FFCS every trip destination is the origin of the subsequent trip, unless operator-based relocation occurs. If an area has a lot of trip end points, it must therefore also exhibit a large number of starting points, which is why end point densities can also approximate origin demand. Thus, we assume that areas with a lot of carsharing activity are areas of high carsharing demand and that providers would benefit from bringing more vehicles into these areas to increase the utilization of their fleet and, as a consequence, increase their profits.

![](/api/attachments/ZVYHT3M5/fulltext/images/5cdc055e1c2135181af221a20bf6a9e5346e9ba0ee7506506725894f8bb17c4b.jpg)

Fig. 2. Schematic visualization of SDSS part 2 – carsharing expansion into new city.

<table><tr><td>Please cite this article as: C. Willing, et al., Moving in time and space – Location intelligence for carsharing decision support, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.05.005</td></tr></table>

Table 1 Dataset characteristics.

<table><tr><td rowspan="2">Observation period</td><td>Amsterdam</td><td>Berlin</td></tr><tr><td>70 days(11 Feb 15–20 Apr 15)</td><td>70 days(11 Feb 15–20 Apr 15)</td></tr><tr><td>Number of trips</td><td>282,587</td><td>355,318</td></tr><tr><td>Number of POIs</td><td>61,442</td><td>178,311</td></tr><tr><td>Number of tiles (kernels)</td><td>6664</td><td>26,425</td></tr></table>

Applying the station-based balancing approach by Jorge et al. [20] to a FFCS system, trips to low-demand destination areas could be discouraged by charging a higher price for such journeys, while trips to highdemand destination areas should be encouraged with a discount. As previously mentioned, these areas can be determined by analyzing historical rental densities. However, as Weikl and Bogenberger [40] show, spatial demand varies over time.

In our approach, which is conceptualized in Fig. 1, we therefore use a GIS to convert historical rental data into spatial heatmaps of demand, which display rental densities per area. By creating multiple heatmaps for different times of day we are able to capture and easily visualize the temporal variations in carsharing usage. When clustering the rental densities into quantiles – for example low, medium and high demand – polygons for each quantile emerge. In order to encourage customers to end their rides in high demand areas and discourage them from low demand areas, providers can use the demand polygons as pricing zones, commanding a lower price for rentals ending in high demand zones and a higher price for those ending in low demand zones. In Section 6.1 we elaborate further on how such a system could be implemented.

In the logic of our proposed SDSS, after implementing the new pricing design, the effects can be measured by calculating average idle times of vehicles, which should decrease in a system where demand and supply are more balanced. In a final step, the approach should be validated by analyzing spatio-temporal demand variations under the new trip pricing design. Ideally, demand variations will have stayed the same. If not, the pricing zones should be adjusted to incorporate the change in demand patterns.

## 3.2. Location intelligence for expansions

The second part of our proposed SDSS assists FFCS providers in choosing an appropriate operating area when entering a new city. The approach, visualized in Fig. 2, is based on Wagner et al. [37], who have demonstrated that their SDSS can successfully optimize existing operating areas. We enhance this system to accommodate expansion into a new city.

Broadly speaking, in this process FFCS providers calculate the determinants of carsharing activity for a city in which they are already active and, subsequently, apply them to a new city for which they do not yet have any indication of carsharing demand. More specifically, an existing operating area is subdivided into more manageable, smaller areas of equal size, in our case tiles of 100 m in edge length. Subsequently, Google Maps points of interest, which are categorized into 94 distinct types, are analyzed for that training city. The POIs are mapped onto the tiles and then converted into POI densities for each of the 94 categories and each of the tiles. Simultaneously, historical carsharing data is converted into rental densities for each tile in that same area. Again, trip end points, which are usually also the starting points of the subsequent rentals, are representative of carsharing activity in each tile and are therefore used to approximate demand. Combining these two datasets and regressing the trip dataset on the POI dataset produces regression coefficients, which represent the influence of each POI category on carsharing demand.

In a second step, POIs are analyzed for the desired target city, which is also subdivided into smaller tiles, and converted into densities. Multiplying POI densities with the previously obtained regression coefficients yields the predicted carsharing demand for each tile. Naturally, this approach can also be computed for different time intervals to capture spatial demand variations.

## 4. Dataset

In order to test the performance of the proposed SDSS, we collected carsharing rental data for Amsterdam and Berlin from a major FFCS provider. The provider has been offering its service for several years in both cities with the same types of vehicles and under similar contract conditions. We can thus assume that the decision-making process of carsharing customers in both cities is quite similar. It was, however, also important to us that the chosen cities not be too similar in their characteristics and be located in different countries, so that we could assess the general applicability of our expansion SDSS.

Overall, we collected individual trip data over a period of more than three months, from February to April 2015. Our dataset consists of N 280,000 trips for Amsterdam and over 350,000 for Berlin. The difference in the number of trips can be attributed to a more extensive operational area, more operating vehicles, and a larger customer base in Berlin.

Just as we require comparable carsharing data from our sample cities, we need suitable POI data. The Google Maps API provides us with datasets from both cities incorporating standardized characteristics. We analyze a total of N60,000 POIs for Amsterdam and N170,000 POIs

![](/api/attachments/ZVYHT3M5/fulltext/images/13e4b0f87e3b804920cf2210fc08818c08ca3758324346b97f8a61539357a2e4.jpg)

![](/api/attachments/ZVYHT3M5/fulltext/images/79c39995625a881bf64123d68e04327e42e70ca3b1fb29eba46bc4d17ac52646.jpg)

![](/api/attachments/ZVYHT3M5/fulltext/images/d6e0f717b25a259bd0cd72bdffbf9634dbee7ced48fed5dfe77f5e80e7e95c41.jpg)  
Fig. 3. Distribution of Amsterdam carsharing trips per day across time windows

Please cite this article as: C. Willing, et al., Moving in time and space – Location intelligence for carsharing decision support, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.05.005

b) Adding POI food

(d) 8:00 − 12:00

(b) 0:00 − 4:00

(c) 4:00 − 8:00

C. Willing et al. / Decision Support Systems xxx (2017) xxx–xxx

(a) All trips

![](/api/attachments/ZVYHT3M5/fulltext/images/765370c57269f92d5e53103b922ea0750c76b17f7c90846d8f7587de274a5f69.jpg)  
Fig. 4. Densities of trip ending points on weekdays (Mo–Fr) in the city of Amsterdam

for Berlin, which are processed online and stored as density values. Again, the difference in geographic size between the two cities shows clearly. The characteristics of our dataset are summarized in Table 1.

In order to gain insight into the temporal dynamics of carsharing trips, we assign each trip to its respective predefined time interval. Rental behavior on weekdays has been found to differ significantly from rental behavior on Saturdays and Sundays [31], and it is easy to imagine that desired destinations on the weekend are different from those on working days. Therefore, we first divide the trip dataset into these three groups,

$$
T = \sum T _ {i} w i t h i = \{W D, S A, S U \}\tag{1}
$$

and then create further subsamples of four-hour intervals within each group to represent night time (0–4 h and 4–8 h), morning (8– 12 h), afternoon (12–16 h) early evening (16–20 h), and late evening (20–24 h).

$$
T _ {i} = \sum I ^ {j} w i t h j = \{0 - 4, 4 - 8, 8 - 1 2, 1 2 - 1 6, 1 6 - 2 0, 2 0 - 2 4 \}\tag{2}
$$

We thus generate a total of 18 subsamples, each representing particular day(s)-of-week and times-of-day. Looking at the descriptive statistics from the day(s)-of-week samples T in Fig. 3, one can already identify temporal variations in carsharing activity over the course of a day, with most rentals happening during early and late evening hours. Yet, although the histograms for weekdays and weekend days appear similar, the reasons for carsharing usage on the different days might still differ significantly. Fig. 4 shows the spatial variations in demand on weekdays, on which rentals end more towards the center of the operating area during evening hours, and are more dispersed during the other time periods.

The subsets also enable us to compare POI influence across the six intervals. The POI data comes with a broad classification of 94 POI types. These types are used to distinguish between the various POIs' characteristics and include attributes such as restaurant, ATM, or subway station. An individual POI may be tagged with one or more of these attributes, for instance restaurant, bar and café. For further data processing, we create 94 POI subsamples, one for each attribute.

## 5. Approach

## 5.1. Kernel density estimation

By combining the vehicle dataset with the POI dataset, we are able to explain carsharing activity by proximity of carsharing destinations to POI categories. In order to merge the two datasets we apply a kernel density estimation (KDE). Using predefined kernels, the distance to reference points can be measured and density values can be computed accordingly. The number of trip end points within a particular distance of the kernel define its rental density, which is a direct indicator of how strongly a specific geographical point attracts carsharing activity. Likewise, a KDE for different POI types represents the concentration of those points across geographical areas. The KDE approach thus enables us to relate density values from the trip sample to density values from

a) Creating a grid of regularly distributed points  
![](/api/attachments/ZVYHT3M5/fulltext/images/33fffc7622b8e808eb4812602bf06b3cd25ed9dbe4352028f145b7e6c17220c9.jpg)

![](/api/attachments/ZVYHT3M5/fulltext/images/2cf9134e14bffcffb0693408170393310d57019e7c6b5ed6c48d94a1aa649ca7.jpg)

![](/api/attachments/ZVYHT3M5/fulltext/images/a6b23efef0d93312b8ccd0110e36bd7a0eb27a38a55b93966dfa0a3f208a979e.jpg)  
Fig. 5. Example of kernel density estimation in spatial context in the city of Amsterdam.

Please cite this article as: C. Willing, et al., Moving in time and space – Location intelligence for carsharing decision support, Decision Support Sys tems (2017), http://dx.doi.org/10.1016/j.dss.2017.05.005

the POI sample and find patterns. For instance, if a kernel has a high trip density value and also a high density value for the POI type ‘bar’, this may indicate that in this particular area, carsharing is used to visit bars.

Another significant advantage of the KDE approach is that it drastically reduces zero values, which would otherwise be predominant in spatial data [18,28] and limit the explanatory power of our results. KDE is hence represented in geospatial research across several academic fields: Gerber [16] uses KDE to predict crime using predictive analytics driven by Twitter data. Kenchington et al. [23] apply KDE to the task of identifying significant concentrations of biomass and relating them to vulnerable marine ecosystems. Our own approach, as mentioned previously, aims to make trip and POI data relatable and suitable for further statistical analysis.

In our case, we generate a grid of evenly distributed points, which are located at the center of the aforementioned tiles. These points, or kernels, are thus separated from their nearest neighbor by 100 m. The generated point grids span the entire operational areas of both cities, resulting in a grid of 6664 points for Amsterdam and a grid of 26,425 points for Berlin (Table 1).

In a second step, we add the layer of reference points from the trip sample and the POI sample. Each kernel is now assigned all POIs and rental destinations within a predefined bandwidth h. The number of points assigned to the kernel, as well as the distance to these points, define the kernel's density value. For our purpose, we choose a bandwidth of h = 1000 m with a linear decreasing influence and, following an established approach from urban economics [27,30], a quartic (biweight) kernel, which can be formulated as follows:

$$
K (u) = \frac {1 5}{1 6} (1 - u 2) ^ {2} 1 _ {\{| u | \leq 1 \}}\tag{3}
$$

Eventually, we compute density values for each kernel in the regular grid based on a corresponding point sample and rescale these densities within their respective range to the interval [0,1] to ensure a better match between the different cities. Fig. 5 once again illustrates the KDE process.

We repeat these steps for each of the 18 rental subsets (each representing a particular time-of-day and day-of-week subsample) and the 94 POI datasets in order to obtain corresponding density sets.

The KDE approach also allows us to effectively deal with spatial autocorrelation among POIs, which naturally occurs in our dataset, as well. Shopping streets, for instance, comprise a multitude of different POIs, all very close together. However, by clustering POIs, assigning them to kernels, and calculating POI densities, we make spatial autocorrelation explicit for all variables and analyze POI patterns instead of single points. We are then able to regress the spatial patterns of carsharing use on the spatial pattern of POI occurrence and, by using a regular grid, analyze how changes in POI patterns relate to changes in carsharing patterns.

## 5.2. Gradient boosting

Before investigating how the density of the different POI groups (explanatory variables) influences the density of trip ending points (dependent variable), we need to reduce the number of predictors, since our model faces the risk of overfitting with 94 POI types. Hence, we opt for a method of variable selection to find the most statistically relevant explanatory variables. We approach the selection process using a Gradient Boosting Machine (GBM), a machine learning technique which offers high flexibility and may be adjusted according to our particular requirements [29]. Originally developed by Friedman [15], gradient boosting builds stage-wise prediction models by optimizing arbitrary differentiable loss functions. We use the statistical programming language R, along with the h2o.ai engine and R package, to compute our models [1]. GBM allows us to rank the predictor variables in accordance with their respective influence on the response variable. Fig. 6 shows the ten most important predictor variables for the distribution of carsharing trips in Amsterdam across all days and time slots, as computed by the GBM. Because the influence of the different POI categories is expected to change over the course of the day, we compute the GBM for each of our 18 time intervals and indeed obtain a different ranking for each time period.

![](/api/attachments/ZVYHT3M5/fulltext/images/efcdd608866ff4d84f4dac6540fe6a2bbb4db11030ae4cc018db127d9b97f0c7.jpg)  
Fig. 6. Most important predictor variables for carsharing activity (all time slots) in the cit of Amsterdam.

To validate our model and conduct sensitivity analyses, we also ran calculations with the 5, 15, and 20 most important explanatory variables. For comparison, Table 4, which is discussed in detail in Section 6.2, provides an overview of the 20 most influential POI categories for all days, including their relative importance for demand explanation in percent.

## 5.3. Regression

Finally, in order to investigate how the densities of the different POI groups (explanatory variables) influence the density of trip ending points (dependent variable), we apply a generalized linear model (GLM) with normally distributed values to every trip ending point dataset. As mentioned before, we test different models with different numbers of POI categories. As can be expected, the R-squared increases when more independent variables are added. However, we also calculate the adjusted R-squared to account for the number of variables in our model and still the model with N = 20 POI categories has the highest explanatory power with an adjusted R-squared of 67.9%, although the improvement over N = 15 is only marginal. As another measure of model comparison, we computed the Akaike Information Criterion (AIC). The AIC is a measure to assess the relative quality of a model. It balances the fit of the model with the complexity of the model by penalizing the inclusion of additional explanatory variables. Again the model with 20 POI categories outperforms the other models, as it exhibits the lowest AIC score. The results for the different models are presented in Table 2.

Model performance characteristics from GLM for all weekday trips in Amsterdam

<table><tr><td></td><td>N = 5</td><td>N = 10</td><td>N = 15</td><td>N = 20</td></tr><tr><td> $R^2$ </td><td>54.8%</td><td>59.1%</td><td>67.8%</td><td>68.0%</td></tr><tr><td> $R^2$ adj.</td><td>54.8%</td><td>59.0%</td><td>67.7%</td><td>67.9%</td></tr><tr><td>AIC</td><td>-7715</td><td>-8366</td><td>-9945</td><td>-9991</td></tr></table>

N = number of explanatory variables (POI categories).

(a) All trips  
Table 3  
POI influence on Amsterdam carsharing demand on weekdays (N = 20).

<table><tr><td>Variable</td><td>0-4 h</td><td>Variable</td><td>4-8 h</td><td>Variable</td><td>8-12 h</td><td>Variable</td><td>12-16 h</td><td>Variable</td><td>16-20 h</td><td>Variable</td><td>20-24 h</td><td>Variable</td><td>All</td></tr><tr><td>Intercept</td><td>0.01</td><td>Intercept</td><td>0.04</td><td>Intercept</td><td>0.06</td><td>Intercept</td><td>0.10</td><td>Intercept</td><td>0.08</td><td>Intercept</td><td>0.04</td><td>Intercept</td><td>0.04</td></tr><tr><td>Atm</td><td>0.03</td><td>Accounting</td><td>0.00</td><td>Accounting</td><td>0.04</td><td>Atm</td><td>0.12</td><td>Accounting</td><td>-0.08</td><td>Bank</td><td>0.26</td><td>Bank</td><td>0.66</td></tr><tr><td>Bank</td><td>0.39</td><td>Bank</td><td>0.59</td><td>Bank</td><td>0.59</td><td>Bank</td><td>0.47</td><td>Bank</td><td>0.75</td><td>Book store</td><td>-0.08</td><td>Book store</td><td>0.06</td></tr><tr><td>Bus station</td><td>-0.21</td><td>Book store</td><td>0.24</td><td>Book store</td><td>-0.17</td><td>Bicycle</td><td>0.09</td><td>Book store</td><td>-0.35</td><td>Bus station</td><td>-0.22</td><td>Bus station</td><td>-0.21</td></tr><tr><td>Cafe</td><td>0.64</td><td>Bus station</td><td>-0.12</td><td>Bus station</td><td>-0.10</td><td>Book store</td><td>-0.34</td><td>Bus station</td><td>-0.28</td><td>Cafe</td><td>0.16</td><td>Car dealer</td><td>0.30</td></tr><tr><td>Car repair</td><td>0.05</td><td>Car dealer</td><td>0.17</td><td>Car dealer</td><td>0.17</td><td>Bus station</td><td>-0.19</td><td>Car dealer</td><td>0.25</td><td>Car dealer</td><td>0.08</td><td>Car repair</td><td>0.03</td></tr><tr><td>Dentist</td><td>-0.08</td><td>Establ.</td><td>0.34</td><td>Car repair</td><td>0.03</td><td>Car dealer</td><td>0.26</td><td>Dentist</td><td>0.00</td><td>Car repair</td><td>0.08</td><td>Electronic</td><td>0.20</td></tr><tr><td>Doctor</td><td>0.13</td><td>Finance</td><td>-0.29</td><td>Clothing</td><td>-0.19</td><td>Electronic</td><td>0.04</td><td>Electronic</td><td>0.26</td><td>Clothing</td><td>-0.10</td><td>Establ.</td><td>0.34</td></tr><tr><td>Establ.</td><td>0.28</td><td>Food</td><td>-0.43</td><td>Electronic</td><td>0.06</td><td>Finance</td><td>-0.07</td><td>Establ.</td><td>0.41</td><td>Doctor</td><td>0.05</td><td>Finance</td><td>-0.10</td></tr><tr><td>Furniture</td><td>-0.14</td><td>Gas station</td><td>0.02</td><td>Finance</td><td>0.07</td><td>Furniture</td><td>-0.05</td><td>Gen. con.</td><td>-0.26</td><td>Electronic</td><td>0.02</td><td>Food</td><td>0.60</td></tr><tr><td>Health</td><td>0.00</td><td>Hospital</td><td>0.09</td><td>Gas station</td><td>0.02</td><td>Gas station</td><td>0.05</td><td>Health</td><td>0.39</td><td>Establ.</td><td>0.33</td><td>Furniture</td><td>-0.10</td></tr><tr><td>Hospital</td><td>0.08</td><td>Jewelry</td><td>-0.55</td><td>Gen. con.</td><td>-0.11</td><td>Gen. con.</td><td>-0.19</td><td>Home goods</td><td>0.07</td><td>Food</td><td>-0.17</td><td>Gas station</td><td>0.02</td></tr><tr><td>Lawyer</td><td>0.02</td><td>Laundry</td><td>0.26</td><td>Hospital</td><td>0.15</td><td>Hospital</td><td>0.14</td><td>Hospital</td><td>0.16</td><td>Furniture</td><td>-0.10</td><td>Health</td><td>0.30</td></tr><tr><td>Meal ta.</td><td>0.19</td><td>Lawyer</td><td>0.15</td><td>Jewelry</td><td>-0.28</td><td>Lawyer</td><td>0.06</td><td>Lawyer</td><td>-0.16</td><td>Health</td><td>0.18</td><td>Hospital</td><td>0.19</td></tr><tr><td>Museum</td><td>0.13</td><td>Library</td><td>-0.05</td><td>Lawyer</td><td>0.01</td><td>Lodging</td><td>0.36</td><td>Painter</td><td>-0.01</td><td>Home goods</td><td>-0.04</td><td>Laundry</td><td>0.13</td></tr><tr><td>Physio</td><td>0.03</td><td>Lodging</td><td>-0.03</td><td>Liquor</td><td>-0.11</td><td>Museum</td><td>0.05</td><td>Parking</td><td>-0.26</td><td>Laundry</td><td>0.10</td><td>Lawyer</td><td>-0.01</td></tr><tr><td>Post office</td><td>0.07</td><td>Moving</td><td>-0.02</td><td>Lodging</td><td>0.22</td><td>Physio</td><td>0.02</td><td>Restaurant</td><td>0.26</td><td>Meal ta.</td><td>0.14</td><td>Museum</td><td>-0.03</td></tr><tr><td>Restaurant</td><td>-0.70</td><td>Painter</td><td>-0.29</td><td>Museum</td><td>0.14</td><td>Restaurant</td><td>-0.23</td><td>School</td><td>0.01</td><td>Post offic</td><td>0.00</td><td>Restaurant</td><td>0.05</td></tr><tr><td>School</td><td>0.19</td><td>Park</td><td>-0.15</td><td>Painter</td><td>0.00</td><td>Subway</td><td>-0.43</td><td>Store</td><td>-0.48</td><td>Restaurant</td><td>0.14</td><td>Store</td><td>-0.99</td></tr><tr><td>Shoe store</td><td>-0.52</td><td>Physio</td><td>0.22</td><td>Restaurant</td><td>0.10</td><td>Train st.</td><td>0.56</td><td>Train st.</td><td>0.08</td><td>School</td><td>0.07</td><td>Train st.</td><td>0.05</td></tr><tr><td>Train st.</td><td>0.01</td><td>Post office</td><td>0.02</td><td>Train st.</td><td>0.13</td><td>Travel</td><td>0.25</td><td>Travel</td><td>0.13</td><td>Travel</td><td>0.01</td><td>Travel</td><td>0.05</td></tr><tr><td> $R^2$ </td><td>52.4%</td><td> $R^2$ </td><td>36.1%</td><td> $R^2$ </td><td>52.9%</td><td> $R^2$ </td><td>59.8%</td><td> $R^2$ </td><td>70.4%</td><td> $R^2$ </td><td>70.7%</td><td> $R^2$ </td><td>68.0%</td></tr><tr><td> $R^2$ adj.</td><td>52.2%</td><td> $R^2$ adj.</td><td>35.9%</td><td> $R^2$ adj.</td><td>52.7%</td><td> $R^2$ adj.</td><td>59.7%</td><td> $R^2$ adj.</td><td>70.3%</td><td> $R^2$ adj.</td><td>70.6%</td><td> $R^2$ adj.</td><td>67.9%</td></tr></table>

bicycle = bicycle store establ. = establishment clothing = clothing store electronic = electronics store  
furniture = furniture store gen. con. = general contractor jewelry = jewelry store liquor = liquor store  
meal ta. = meal takeaway moving = moving company physio = physiotherapist subway = subway station  
train st. = train station travel = travel agency.

## 6. Performance evaluation

## 6.1. Location intelligence for existing areas

Wagner et al. [37] have shown that POI densities have a significant influence on carsharing demand. However, our regression results, which can be found in Table 3, show that their influence is not static but changes over the course of the day. The table displays the results of the generalized linear model, regressing the 20 most important POI category densities onto trip densities. The results shown are for the six different timeslots during weekdays, as well as the regression results for carsharing rentals during weekdays in general. The sample size is equal to the number of grid tiles (6664) for all regressions. It should be noted that POI categories need to be considered relative to each other, since the same POI may be tagged with various categories. For instance, in the first column, the coefficient of ‘health’ includes all POIs that are tagged as health-related. This coefficient is further refined by the categories ‘dentist’ (negative) and ‘hospital’ (positive). The coefficients of these sub-categories allow a further discrimination within the ‘health’-category and are similar to interaction terms in their effects.

For each timeslot during weekdays, the order of influence of the most influential POI categories is different and some changes are quite significant. For instance, there are categories, such as ‘restaurant’, which change from having a negative influence in the 12-16 h slot to strongly positive in the subsequent two timeslots and again to negative between 0 and 4 h. ‘Meal takeaway’, on the other hand, has a positive influence during the late evening (20–24 h) and subsequent night slot, but does not appear otherwise. Both phenomena reflect temporal variation in dining behavior. Other categories are more constant in their influence: ‘bank’, for example, always has a positive influence, as does ‘train station’ whenever it is in the top 20. ‘Bus station’, on the other hand, has a negative influence on trip densities in all periods. These are interesting results in the broader context of urban mobility, as they suggest that carsharing and public transport are used complementarily [41]. While transport via train is used in direct combination with carsharing, carsharing activity also seems to be greater in areas with a lower density of bus stops, i.e. areas that offer less access to urban public transportation.

When trying to interpret the results it becomes apparent that some variations are intuitive while others are more difficult to explain, such as the positive influence of the ‘school’ POI category during night intervals. These categories may serve as proxies for other variables not under consideration – for instance, schools may be more prevalent in, or close to, residential areas and the positive impact may represent people returning home.

Overall, the results were similar for carsharing activity on weekend days and for different numbers of explanatory variables. Together with the descriptive statistics in Fig. 3 and Fig. 4, we can summarize with respect to the first research question that carsharing demand increases over the course of the day and decreases again during nighttime. These variations are accompanied by a change in spatial demand which, in Amsterdam, seems to be more centrally located during the evening hours and more dispersed otherwise. These demand variations can, to a certain degree, be explained by the varying influence of differ ent POI categories.

![](/api/attachments/ZVYHT3M5/fulltext/images/5d322c8c7ab2ea6c6a660fe7f9728942da1455f9a8138dd4a1de790430e4b270.jpg)

![](/api/attachments/ZVYHT3M5/fulltext/images/06beaedfdb60127274ccb11ead6a9281068279efe11ef73a558b0c2b0006a25c.jpg)  
Fig. 7. Demand quantiles (Mo.–Fr.) to shape pricing zones

Table 4  
POI category selection from Gradient Boosting Machine; bold categories are the same in both cities (all rentals).

<table><tr><td colspan="3">Amsterdam</td><td colspan="3">Berlin</td></tr><tr><td>Variable</td><td>Scaled importance</td><td>Percentage</td><td>Variable</td><td>Scaled importance</td><td>Percentage</td></tr><tr><td>Health</td><td>1.00</td><td>37.65%</td><td>Restaurant</td><td>1.00</td><td>35.20%</td></tr><tr><td>Restaurant</td><td>0.20</td><td>7.41%</td><td>Food</td><td>0.74</td><td>26.02%</td></tr><tr><td>Book store</td><td>0.19</td><td>7.12%</td><td>Bar</td><td>0.56</td><td>19.54%</td></tr><tr><td>Bank</td><td>0.16</td><td>6.16%</td><td>Art gallery</td><td>0.10</td><td>3.40%</td></tr><tr><td>Bus station</td><td>0.12</td><td>4.44%</td><td>Lodging</td><td>0.06</td><td>2.08%</td></tr><tr><td>Car dealer</td><td>0.08</td><td>3.01%</td><td>School</td><td>0.05</td><td>1.77%</td></tr><tr><td>Food</td><td>0.07</td><td>2.63%</td><td>Car rental</td><td>0.03</td><td>0.98%</td></tr><tr><td>Train station</td><td>0.07</td><td>2.49%</td><td>Bus station</td><td>0.03</td><td>0.91%</td></tr><tr><td>Electronic</td><td>0.06</td><td>2.25%</td><td>Establishment</td><td>0.02</td><td>0.83%</td></tr><tr><td>Finance</td><td>0.05</td><td>1.90%</td><td>Real estate</td><td>0.02</td><td>0.73%</td></tr><tr><td>Travel agency</td><td>0.05</td><td>1.79%</td><td>Plumber</td><td>0.02</td><td>0.71%</td></tr><tr><td>Store</td><td>0.05</td><td>1.70%</td><td>Health</td><td>0.01</td><td>0.50%</td></tr><tr><td>Establishment</td><td>0.04</td><td>1.46%</td><td>Electronics</td><td>0.01</td><td>0.44%</td></tr><tr><td>Hospital</td><td>0.03</td><td>1.27%</td><td>Clothing store</td><td>0.01</td><td>0.44%</td></tr><tr><td>Laundry</td><td>0.03</td><td>1.08%</td><td>Liquor store</td><td>0.01</td><td>0.42%</td></tr><tr><td>Furniture</td><td>0.03</td><td>1.08%</td><td>Park</td><td>0.01</td><td>0.42%</td></tr><tr><td>Museum</td><td>0.03</td><td>1.04%</td><td>Bakery</td><td>0.01</td><td>0.38%</td></tr><tr><td>Lawyer</td><td>0.03</td><td>0.99%</td><td>Accounting</td><td>0.01</td><td>0.35%</td></tr><tr><td>Car repair</td><td>0.02</td><td>0.91%</td><td>Store</td><td>0.01</td><td>0.28%</td></tr><tr><td>Gas station</td><td>0.02</td><td>0.82%</td><td>Home goods</td><td>0.01</td><td>0.26%</td></tr></table>

This approach certainly helps in understanding the drivers behind spatio-temporal demand variations, but it is not a prerequisite for developing pricing zones. To follow the SDSS approach sketched out in Fig. 1, we use the rental densities for Amsterdam's operating area and divide them into three quantiles representing areas of relatively low demand in light blue, areas of medium demand in medium blue, and high trip densities in dark blue (Fig. 7a). As previously mentioned, providers may want to charge higher prices for rentals ending in the light blue area, and lower prices for rentals ending in high-demand areas.

Currently, the dominant FFCS providers charge their customers purely on a per-minute basis and award bonuses (e.g. free minutes) when customers provide a service, such as refueling or getting the car washed. In seeking to implement a pricing scheme that encourages balancing of supply and demand, carsharing operators have multiple strategies to choose from: They could apply the aforementioned bonus method, and give customers free minutes for ending their rentals in high-demand zones, or impose a penalty – a fixed extra charge – for ending the rental in a low-demand zone. Alternatively, providers could adjust the per-minute rental price, i.e. give a percentage discount at the end of a rental, depending on the zone in which the destination is located – for instance, a lower per-minute price for rentals ending in high-demand polygons and a higher per-minute price for low-demand destinations.

Although the zones in Fig. 7(a) do not spread evenly from the city center to the outskirts of the operating area, technical implementation of the different price zones could be easily achieved since FFCS vehicles are all equipped with GPS systems, which could simply inform users about the price should they choose to leave their rental vehicle at its current location. From a user perspective, however, more coherent zones would be much easier to explain to customers. Educating the customer becomes even more difficult when adding temporal demand dynamics into the mix. As shown in Fig. 7(b) and (c) the zones shift and become more fragmented. In any case, the pricing system would have to be totally transparent so that users know what price to expect before initiating a rental. These considerations show that it is necessary to further investigate the different pricing designs and test them in realworld pilots. This would allow carsharing operators to determine the extent to which customers understand and accept the different approaches and how effective the approaches are in balancing supply and demand.

## 6.2. Location intelligence for expansion

To answer the second research question of how FFCS operators can decide on the operating area when entering a new city, we follow the

![](/api/attachments/ZVYHT3M5/fulltext/images/832a48c0930b5114e49a9a8eba1b3c3aa30833c72b50cbf59236d4a75aa457eb.jpg)  
(a) Predicted rental densities

![](/api/attachments/ZVYHT3M5/fulltext/images/2712d761c6531506fee0365bd08e022cde9fb2b121c70dd940976ae1877c9961.jpg)  
(b) Actual rental densities  
Fig. 8. Comparison of predicted and actual demand patterns for weekdays in Berlin (based on N = 20 POIs). (For interpretation of the references to color in this gure, the reader is referred to the web version of this article.)

Please cite this article as: C. Willing, et al., Moving in time and space – Location intelligence for carsharing decision support, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.05.005

Table 5  
![](/api/attachments/ZVYHT3M5/fulltext/images/5a84e7afbeecb36f95d2ad99e8c4ad110113807223ea9074d58eba5d3f2e19b1.jpg)  
(a) N = 5 POI categories

![](/api/attachments/ZVYHT3M5/fulltext/images/e2ac71b9f4aa3a594c62ecce4668cf2a2c58c35d601c4e2ee5f098bc91389d98.jpg)  
(b) N = 20 POI categories  
Fig. 9. Visualization of ranked trip densities (predicted and actual) for each kernel in Berlin.

approach outlined in Fig. 2 and apply the POI regression coefficients from our Amsterdam sample to normalized POI densities in Berlin. Just as we did for Amsterdam, we have created a point grid for Berlin with the same distance between points. Using the aforementioned KDE approach, and with the same parameters as in Amsterdam, each point is assigned its respective POI densities for each of the 94 POI categories. Carsharing demand is then computed for every kernel by simply multiplying the POI densities with their respective regression coefficients that resulted from the Amsterdam estimation.

Because we also collected rental data in Berlin over the same time period as for our Amsterdam trip dataset, we can easily verify our approach and test its validity. As a first indication of the suitability of our approach, we compute the GBM to determine the POI categories that have the greatest influence on Berlin's actual rental density. Indeed, for 7 of the 20 most influential POI categories, the types overlap and are the same in both cities. The relevant categories are marked in bold in Table 4.

For the subsequent comparison of predicted and actual demand, we divided the trip density subsets into two quantiles, one above the median rental density (blue) and one below the median density (grey). A visual comparison of predicted demand (based on N = 20 most influencing POI categories) and actual rental densities in Fig. 8 shows clearly that, overall, the spatial demand patterns are very similar. Our prediction, however, seems to underestimate demand in the city center where, it is more fragmented than actual rental densities, and overestimate demand for kernels which are closer to the operating areas' boundaries.

For a more quantitative comparison of predicted and actual demand, we rank the actual and predicted rental datasets by kernel, according to rental densities. For each kernel, we can thus easily compare whether its predicted and actual demand both rank in the same quantile.

This comparison is visualized in Fig. 9, where each mark represents one kernel within the operating area of Berlin. Plot (a) clearly shows that there is a strong correlation between the ranked predicted trip densities and ranked actual demand densities. Plot (b) shows that this correlation improves even more when more POI categories are used to predict carsharing usage in Berlin.

To confirm the visual impression and to further investigate the sensitivity of the accuracy of our predictions, we have also calculated confusion matrices (Table 5), which provide an overview of the respective quality of each prediction. The true positive rate (TPR) indicates how many kernels were correctly predicted to be in the higher demand quantile, while the true negative rate (TNR) reflects how many were correctly predicted to be in the lower demand quantile. The results show that the highest accuracy is achieved for N = 20 explanatory POI categories, where almost 80% of the areas with high demand have been correctly identified. Without the POI approach, the naïve prediction would have yielded a 50% hit rate. Our approach, thus, signifies a substantial improvement over naïve prediction and helps decisionmakers correctly identify high-demand areas. Interestingly, the quality of prediction is not significantly reduced when fewer POI categories are used in the model. When only five categories are utilized, the prediction improvement still exceeds 26 percentage points, compared to 29 percentage points for 20 categories.

We also assess the ability of our SDSS to identify particularly highdemand areas by dividing the rental density datasets into a quantile of the highest 25% demand kernels and another quantile including the bottom 75% demand densities. The prediction accuracy for this approach is still quite high, with a TPR of 72.2% and a TNR of 90.7% for 20 POI categories.

For a final assessment we calculated receiver operator characteristic (ROC) curves for the different models. Again, we classified the actual trip densities into two demand quantiles – above-median demand equal to 1 and below median demand equal to 0 – and assessed the model performance for different cut-off points for our predicted demand. Fig. 10b for the N = 20 model shows high model accuracy, with an area under the curve (AUC) of 86.5%; however, the N = 5 also performs well, with an AUC of 82%.

Confusion matrix of predicted and actual demand in Berlin.

<table><tr><td rowspan="2"></td><td colspan="2">N = 5</td><td colspan="2">N = 10</td><td colspan="2">N = 15</td><td colspan="2">N = 20</td></tr><tr><td>Predicted: above</td><td>Predicted: below</td><td>Predicted: above</td><td>Predicted: below</td><td>Predicted: above</td><td>Predicted: below</td><td>Predicted: above</td><td>Predicted: below</td></tr><tr><td>Actual: above</td><td>10,141</td><td>3072</td><td>10,109</td><td>3104</td><td>10,424</td><td>2789</td><td>10,476</td><td>2737</td></tr><tr><td>Actual: below</td><td>3072</td><td>10,140</td><td>3104</td><td>10,108</td><td>2789</td><td>10,423</td><td>2737</td><td>10,475</td></tr><tr><td>TPR</td><td>76.8%</td><td></td><td>76.5%</td><td></td><td>78.9%</td><td></td><td>79.3%</td><td></td></tr><tr><td>TNR</td><td>76.7%</td><td></td><td>76.5%</td><td></td><td>78.9%</td><td></td><td>79.3%</td><td></td></tr></table>

Please cite this article as: C. Willing, et al., Moving in time and space – Location intelligence for carsharing decision support, Decision Support Systems (2017), http://dx.doi.org/10.1016/j.dss.2017.05.005

![](/api/attachments/ZVYHT3M5/fulltext/images/3d248fab249f21db0a29037ffd25d70fec9efb7009619d84444f86125a47a9d1.jpg)  
(a) N = 5 POI categories

![](/api/attachments/ZVYHT3M5/fulltext/images/c48bb3490e782eb5bf2fa9f4d0f221e9c0420ff913831f83915b41d7e05bb9c4.jpg)  
(b) N = 20 POI categories  
Fig. 10. ROC curves for carsharing activity prediction models.

## 7. Conclusions

Carsharing is growing rapidly in metropolitan areas all over the world and the need for methods to improve its efficiency and userfriendliness has increased accordingly. Information systems have emerged as a powerful instrument to connect service providers and customers. This also applies to carsharing, whose customers are offered a considerably degree of flexibility and self-determination. This flexibility, though, comes at the price of growing complexity and optimization challenges, most notably the rising imbalance of supply and demand with regard to vehicles. In our research, we therefore investigate carsharing customer behavior by connecting trip activity with points of interest (POIs) and propose a spatial decision support system which contributes to more balanced supply and demand in two ways. First, we introduce a method for creating variable trip pricing in existing operating areas and, second, our system provides decision support to carsharing operators wishing to enter a new city, such that they can correctly shape the operating area to include areas of high-demand, and exclude those with low-demand. For this purpose we have compiled a dataset of carsharing rentals from a major carsharing provider in Amsterdam and examine how trip destinations are connected to different POI categories. We use kernel density estimation and apply a Gradient Boosting Machine (GBM) to select the POI categories with the greatest explanatory power. Subsequently, employing a generalized linear model, we can show that different POIs impact trip destinations and that their influence varies over time. We thus confirm the results of a recent study by Wagner et al. [37] and extend it by providing new insight into the temporal variability of POI influence.

Our work contributes to current research in two ways: First, we aid in understanding customer behavior by investigating when and for what purpose carsharing is used. Our findings suggest that in this respect, the temporal and spatial dimensions are not independent. Rather, different POI categories have a different influence on trip destinations depending on the time of day and the day of the week. We draw the conclusion that the spatio-temporal dynamics of carsharing utilization can, to some extent, be explained by POIs. This knowledge not only enables managers to better understand their customers' behavior, but also equips them with a valuable tool for demand prediction in previously unserved areas. Second, by providing new insights into shared vehicle demand, we are able to predict the development of ‘hot spot’ and ‘cold spot’ regions. Applying this knowledge when shaping the business area of a new city can once again reduce the initial need for relocation.

While the relocation question in carsharing is steadily gaining more academic attention, it is still not resolved. The approaches laid out in this paper provide a starting point to rebalance carsharing supply and demand and, in effect, reduce the need for relocation. Future research will, however, need to further test and validate both approaches – zone-based trip pricing and POI-based expansion planning – in realworld test cases to determine the effectiveness and evaluate customer understanding and acceptance of a more flexible pricing design.

From a carsharing provider's point of view, directing more vehicles to high-demand areas is desirable, as it would be expected to lead to higher vehicle utilization, which translates directly into higher profits. From a societal standpoint, however, directing vehicles away from low-demand areas might be less desirable, as it deprives residents living in those areas of equal mobility access. Hence, with carsharing becoming a more established part of the urban modal mix, we see another promising line of research in evaluating carsharing demand in the context of other transport modes from a more holistic urban mobility point of view, which could support urban planning decision-making at a municipal level and include both environmental and social considerations.

## References

[1] S. Aiello, T. Kraljevic, P. Maj, R Interface for H ORetrieved from https://cran.r-project. org/web/packages/h2o/h2o.pdf 2016.

[2] M. Balac, F. Ciari, K.W. Axhausen, Carsharing demand estimation. Transportation research record, J. Transp. Res. Board 2536 (2015) 10–18 (https://doi.org/10.3141/ 2536-02).

[3] P. Baptista, S. Melo, C. Rolim, Energy, environmental and mobility impacts of carsharing systems. Empirical results from Lisbon, Portugal, Procedia. Soc. Behav. Sci. 111 (2014) 28–37 (https://doi.org/10.1016/j.sbspro.2014.01.035).

[4] F. Bardhi, G.M. Eckhardt, Access-based consumption: the case of car sharing, J. Consum. Res. 39 (4) (2012) 881–898 (https://doi.org/10.1086/666376).

[5] M. Barth, M. Todd, L. Xue, User-based vehicle relocation techniques for multiple-station shared-use vehicle systems, Transportation Research Board 80th Annual Meeting, 2004.

[6] G. Brandstätter, C. Gambella, M. Leitner, E. Malaguti, F. Masini, J. Puchinger, ... D. Vigo, Overview of optimization problems in electric car-sharing system design and management, in: H. Dawid, K.F. Doerner, G. Feichtinger, P.M. Kort, A. Seidl (Eds.), Dynamic Modeling and Econometrics in Economics and Finance. Dynamic Perspectives on Managerial Decision Making. Essays in Honor of Richard F. Hartl vol. 22, Springer Berlin Heidelberg, New York NY 2016, pp. 441–471 (https://doi. org/10.1007/978-3-319-39120-5\_24).

[7] C. Celsor, A. Millard-Ball, Where does carsharing work?: using geographic information systems to assess market potential. Transportation research record, J. Transp Res. Board (2007) 61–69 1992. (https://doi.org/10.3141/1992-08).

[8] E.M. Cepolina, A. Farina, A new shared vehicle system for urban areas, Transp. Res. C Emerg. Technol. 21 (1) (2012) 230–243 (https://doi.org/10.1016/j.trc.2011.10.005).

[9] F. Ciari, B. Bock, M. Balmer, Modeling station-based and free-floating carsharing demand. Transportation research record, J. Transp. Res. Board 2416 (2014) 37–47 (https://doi.org/10.3141/2416-05).

[10] M. Clemente, M.P. Fanti, A.M. Mangini, W. Ukovich, The vehicle relocation problem in car sharing systems: modeling and simulation in a petri net framework in: D. Hutchison T. Kanade I. Kittler LM. Kleinberg, E. Mattern LC. Mitchell I. Desel (Eds.), Lecture Notes in Computer Science/Theoretical Computer Science and General Issues: Vol. 7927. Application and Theory of Petri Nets and Concurrency: 34th International Conference, vol. 7927, Springer, Berlin 2013, pp. 250–269 (https://doi org/10.1007/978-3-642-38697-8\_14).

[11] C. Costain, C. Ardron, K.N. Habib, Synopsis of users' behaviour of a carsharing program: a case study in Toronto, Transp. Res. A Policy Pract. 46 (3) (2012) 421–434 (https://doi.org/10.1016/j.tra.2011.11.005).

[12] M.D. Crossland. B.E. Wynne, W.C. Perkins, Spatial decision support systems: an overview of technology and a test of efficacy, Decis. Support. Syst. 14 (3) (1995) 219-235 (https://doi.org/10.1016/0167-9236(94)00018-N)

[13] D. Farkas, B. Hilton, J. Pick, H. Ramakrishna, A. Sarkar, N. Shin, A tutorial on geographic information systems: a ten-year update, Commun. Assoc. Inf. Syst. 38 (1) (2016) Retrieved from http://aisel.aisnet.org/cais/vol38/iss1/9.

[14] J. Firnkorn, M. Müller, What will be the environmental effects of new free floating car-sharing systems? The case of car2go in Ulm, Ecol. Econ. 70 (8) (2011) 1519–1528.

[15] J.H. Friedman, Greedy function approximation: a gradient boosting machine, Ann. Stat. 29 (5) (2001) 1189–1232 (https://doi.org/10.1214/aos/1013203451).

[16] M.S. Gerber, Predicting crime using twitter and kernel density estimation, Decis. Support. Syst. 61 (2014) 115–125 (https://doi.org/10.1016/j.dss.2014.02.003).

[17] G.M. Giaglis, I. Minis, A. Tatarakis, V. Zeimpekis, Minimizing logistics risk through real-time vehicle routing and mobile technologies, Int. J. Phys. Distrib. Logist Manag. 34 (9) (2004) 749–764 (https://doi.org/10.1108/09600030410567504).

[18] M. Hallin, Z. Lu, L.T. Tran, Kernel density estimation for spatial processes: the L1 theory, J. Multivar. Anal. 88 (1) (2004) 61–75 (https://doi.org/10.1016/S0047- 259X(03)00060-5).

[19] D. Jorge, G. Correia, Carsharing systems demand estimation and defined operations: a literature review, Eur. J. Transp. Infrastruct. Res. 13 (3) (2013) 201–220 Retrieved from http://www.tbm.tudelft.nl/fileadmin/Faculteit/TBM/Onderzoek/EJTIR/Back\_issues/13.3/2013\_03\_02.pdf.

[20] D. Jorge, G. Molnar, G.H. de Almeida Correia, Trip pricing of one-way station-based carsharing networks with zone and time of day price variations, Transp. Res. B Methodol. 81 (2015) 461–482 (https://doi.org/10.1016/j.trb.2015.06.003).

[21] P.B. Keenan, Spatial decision support systems for vehicle routing, Decis. Support Syst. 22 (1) (1998) 65–71 (https://doi.org/10.1016/S0167-9236(97)00054-7).

[22] A.G. Kek, R.L. Cheu, Q. Meng, C.H. Fung, A decision support system for vehicle relocation operations in carsharing systems, Transp. Res. E Logist. Transp. Rev. 45 (1) (2009) 149–158 (https://doi.org/10.1016/j.tre.2008.02.008).

[23] E. Kenchington, F.J. Murillo, C. Lirette, M. Sacau, M. Koen-Alonso, A. Kenny, ... L. Beazley, Kernel density surface modelling as a means to identify significant concentrations of vulnerable marine ecosystem indicators, PLoS One 9 (10) (2014), e109365. (https://doi.org/10.1371/journal.pone.0109365).

[24] J. Kopp, R. Gerike, K.W. Axhausen, Do sharing people behave differently?: an empirical evaluation of the distinctive mobility patterns of free-floating car-sharing members, Transportation 42 (3) (2015) 449–469 (https://doi.org/10.1007/s11116-015- 9606-1).

[25] E.W. Martin, S.A. Shaheen, Greenhouse gas emission impacts of carsharing in North America, IEEE Trans. Intell. Transp. Syst. 12 (4) (2011) 1074–1086 (https://doi.org/ 10.1109/TITS.2011.2158539)

[26] A. Millard-Ball, G. Murray, J. ter Schure, C. Fox, J. Burkhardt, Car-sharing: where and how it succeeds TCRP Report: Vol, 108 Washington. D C: Transportation Research Board, 2005.

[27] P. Monkkonen, X. Zhang, Innovative measurement of spatial segregation: comparative evidence from Hong Kong and San Francisco, SI: Tribute to John Quigley, 47, 2014, pp. 99–111 (https://doi.org/10.1016/j.regsciurbeco.2013.09.016).

[28] T. Nakaya, K. Yano, Visualising crime clusters in a space-time cube: an exploratory data-analysis approach using space-time kernel density estimation and scan statistics, Trans. GIS 14 (3) (2010) 223–239 (https://doi.org/10.1111/j.1467-9671.2010. 01194.x).

[29] A. Natekin, A. Knoll, Gradient boosting machines, a tutorial, Front. Neurorobot. 7 (2013) 21 (https://doiorg/10.3389/fnbot.2013.00021).

[30] S.F. Reardon, S.A. Matthews, D. O'Sullivan, B.A. Lee, G. Firebaugh, C.R. Farrell, K. Bischoff, The geographic scale of metropolitan racial segregation, Demography 45 (3) (2008) 489–514 (https://doi.org/10.1353/dem.0.0019).

[31] S. Schmöller, S. Weikl, J. Müller, K. Bogenberger, Empirical analysis of free-floating carsharing usage: the Munich and Berlin case, Transp. Res. C Emerg. Technol. 56 (2015) 34 51 (https://doi.org/10.1016/j.trc.2015.03.008).

[32] F. Schulte, S. Voß, Decision support for environmental-friendly vehicle relocations in free- floating car sharing systems: the case of Car2go, Procedia CIRP 30 (2015) 275–280 (https://doi.org/10.1016/j.procir.2015.02.090).

[33] S.A. Shaheen, A.P. Cohen, Carsharing and personal vehicle services: worldwide market developments and emerging trends, Int. J. Sustain. Transp. 7 (1) (2013) 5–34 (https://doi.org/10.1080/15568318.2012.660103).

[34] S.A. Shaheen, D. Sperling, C. Wagner, Carsharing in Europe and North America: past, present, and future, Transp. Q. 52 (3) (1998) 35–52.

[35] M. Sonneberg, K. Kuehne, M. Breitner, A decision support system for the optimization of electric car sharing stations, Proceedings of the 36th International Conference on Information Systems, 2015 Retrieved from http://aisel.aisnet.org/icis2015/proceedings/DecisionAnalytics/7

[36] United Nations Department of Economic and Social Affairs, World Urbanization Prospects: The 2014 Revision, Highlights, 2014 (New York).

[37] S. Wagner, T. Brandt, D. Neumann, In free float: developing business analytics support for carsharing providers, Omega 59 (2016) 4–14 (https://doi.org/10.1016/j. omega.2015.02.011).

[38] S. Wagner, C. Willing, T. Brandt, D. Neumann, Data analytics for location-based services: enabling user-based relocation of carsharing vehicles Proceedings of the 36th International Conference on Information Systems, 2015 (https://doi.org/10.13140/ RG.2.1.1595.6966).

[39] S. Weikl, K. Bogenberger, Relocation strategies and algorithms for free-floating car sharing systems, IEEE Intell. Transp. Syst. Mag. 5 (4) (2013) 100–111 (https://doi. org/10.1109/MITS.2013.2267810)

[40] S. Weikl, K. Bogenberger, A practice-ready relocation model for free-floating carsharing systems with electric vehicles – mesoscopic approach and field trial results, Trans. Res. C Emerg. Technol. 57 (2015) 206–223 (https://doi.org/10.1016/j. trc.2015.06.024).

[41] C. Willing, G. Gust, G. Brandt, S. Schmidt, D. Neumann, Enhancing municipal analytics capabilities to enable sustainable urban transportation, Proceedings of the 24th European Conference on Information Systems (ECIS), 2016 (https://doi.org/10. 13140/RG.2.1.1509.6727).

Christoph Willing is a Ph.D. candidate at the University of Freiburg investigating innovative mobility solutions with a particular focus on carsharing. Before his Ph.D. studies, he has worked for several years in strategy consulting, advising clients in transformation pro grams. His work has appeared in the proceedings of ICIS, ECIS, and AMCIS.

Konstantin Klemmer is a graduate student at Imperial College London. He received his B·Sc. in economics from the University of Freiburg in 2016. Konstantin has contributed to various research projects on location intelligence and sustainable transportation.

Tobias Brandt is assistant professor of business information management at Rotterdam School of Management, Erasmus University. He received his Ph.D. from the University of Freiburg, Germany, in 2015. His research focuses on the digital transformation of society and economy, with a particular focus on smart cities and urban data analytics. His work has received best paper awards at ICIS and HICSS and his papers have been published or are forthcoming in the Journal of Management Information Systems, the European Journal of Information Systems, the European Journal of Operational Research, Information & Management, and Omega.

Dirk Neumann is full professor for information systems at the University of Freiburg, Germany. He holds degrees in economics from the University of Giessen, Germany, and the University of Wisconsin-Milwaukee, as well as a Ph.D. in economic and business sciences from the Karlsruhe Institute of Technology, Germany. His research centers on digitization and novel uses of information systems in industry and society. His articles have been published in the Journal of Management Information Systems, the ACM Transactions in Internet Technology, the Communications of the ACM, Decision Support Systems, and others.
