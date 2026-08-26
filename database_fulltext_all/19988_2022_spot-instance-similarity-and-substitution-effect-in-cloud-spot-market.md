---
otero_id: 19988
otero_key: "YRJB59C4"
title: "Spot instance similarity and substitution effect in cloud spot market"
authors: "Vivek Kumar Singh; Shivendu Shivendu; Kaushik Dutta"
year: "2022"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2022.113815"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Spot instance similarity and substitution effect in cloud spot market

![](/api/attachments/YRJB59C4/fulltext/images/0060c72aef6c381903ef0d99b87996346c2586c567b81959ddc13110948661b6.jpg)

Vivek Kumar Singh <sup>a,\*</sup>, Shivendu Shivendu <sup>b</sup>, Kaushik Dutta b

<sup>a</sup> IST, College of Business Administration, University of Missouri, St. Louis, MO, United States of America <sup>b</sup> MUMA College of Business, University of South Florida, Tampa, FL, United States of America

## A R T I C L E I N F O

Keywords: Cloud computing Similar spot instance Dimensions of spot instance similarity Substitution effect

## A B S T R A C T

Customers in cloud spot market choose from a set of computing resources (spot instances) some of which are same along one or more of the dimensions of hardware configuration, hardware capacity, software, and location (or zones within the same region). While prior research in IS has shown that cloud market consumers do not substitute identical spot instances across distant locations or regions due to costs associated with latency, there is a paucity of research examining spot price dynamics of similar instances which are same along only some of the dimensions (or characteristics) within a region. Using the economic theory of substitution in production and consumption as our theoretical lens, our empirical analysis finds evidence that consumers substitute similar computing resources in the spot market. Further, we find that while hardware configuration similarity between two instances is positively related to spot instance substitution, this substitution effect along hardware config uration is moderated by similarity along hardware capacity and location (zone). Our work contributes to the literature on cloud spot market by providing empirical evidence of the substitution effect among similar spot resources within a region, and thus help in understanding the choices of consumers in this market. We conclude by discussing how practitioners can leverage these findings in the procurement of computing resources from cloud spot market.

## 1. Introduction

The cloud computing market is transforming business in every in: dustry, and a large number of organizations are moving their core business to the cloud [1,2]. A high compounded annual growth rate of cloud computing<sup>1</sup> is driven by a low upfront investment in computing resources and enhanced operational flexibility leading to business resilience [2–7]. Moreover, recent economic ecosystem disruptions caused by COVID-19 pandemic are further driving the growth of cloud market because of enterprises’ need to support ‘work-from-home’, and increased demand for cloud-based business continuity tools and services. 2

Organizations migrating to cloud avail scalability and pay only for the use of computing resources. On the other hand, cloud vendors absorb the risk of oversupply of computing resources (leading to over invest ment) arising from demand uncertainties of organizations moving to their cloud platforms [8,9]. Understanding the cloud market dynamics is important for senior managers who are key decision makers of how organizations manage and procure these computing resources in the cloud market [10,11].

While cloud vendors offer different pricing models to sell the underutilized compute capacity, a leading vendor in this field – Amazon Web Services (AWS) offers a second-price auction model for spot pricing [12–14]. Unlike the traditional fixed pay-per-use pricing model, the price of a resource in this model, known as spot price, varies over time and is determined by the dynamics of the demand and supply of compute resource. The market using this pricing model is known as spot market, and the computing resources sold in this market are called spot instances (instance is another term for virtual machines).<sup>3</sup>

In this pricing model, customers specify a maximum price which they are willing to pay for a computing resource and get the resource at spot price if that is lower than the specified maximum price and the resource is available. To that extent the pricing model is akin to second-price auction [15]. The extant research on cloud spot market has primarily focused on selection of a maximum hourly price for a resource by developing predictive models to forecast the spot price for the next hour [16,17]. However, this stream of research does not consider relationship of spot price of focal instance with other instances, and to that extent, considers the spot prices of focal computing resources independent of spot prices of other resources or instances.

Cheng et al. [13] examined the relationships among the spot prices of identical computing resources and demonstrated that their prices differ based on the region<sup>4</sup> in which these resources are located. While Cheng et al. show that spot price differences of identical computing resources across data centers in two regions (which are distant from each other) are due to associated costs because of latency, they have not examined the price associations of computing resources in spot market within a region but across different zones (sub-geographies within a region). In other words, Cheng et al. [13] do not study spot price dynamics when associated data center are not distant and they are with in a region. Further, Mukherjee et al. [10] propose a new framework for spot price auction wherein customers bid for future time periods, but they also do not consider the relationships among the prices of spot instances. Some other studies in Information Systems have studied spot market pricing from the provider’s perspective [8,9,18] and lack consumers’ perspec tive. Therefore, to the best of our knowledge, this is a gap in the extant literature which we fill by studying the spot price dynamics of spot in stances based on their properties and explaining this dynamic through the theoretical lens of substitution of spot instances by consumers.

In this paper, we extend the prior research to examine the spot prices of similar computing resources located in data centers within a region. Similar to the expectation in Cheng et al. [13] of arbitrage among the identical computing resources across two regions due to the law of one price, one would expect customers to substitute between similar computing resources to take advantage of the price difference across data centers located in the same region though in different zones (a region consists of multiple zones) which are relatively geographically closer. The focus of this research is to understand the substitution among similar resources along one or more of the following four dimensions or attributes of spot instances – hardware configuration, hardware capac ity, software, and datacenter location within the same region. While hardware configuration represents the processor (CPU) characteristics, hardware capacity represents the capacity of hardware configuration in terms of number of CPU cores and memory size. Further, software rep resents the operating system running in the computing resource and location represents the data center location or zone where the computing resource that is being offered to the consumers is available.

More specifically, we address the following research question in this paper: Along which spot instance similarity dimensions do customers consider substituting spot resources? The research question is imperative for explaining the spot price dynamics in spot market. To study the above research question, we use the economic theory of substitution in production and consumption, which implies that if customers substitute similar computing resources in the spot market, then prices of these similar resources are likely to be positively associated with each other [19]. We measure the extent of substitution between two resources using their price association (covariance) over time. The findings of this research question are important for IT managers because these will help them to choose appropriate spot instances or computing resources to lower the computing resource costs when sourcing from spot market.

We consider four dimensions of spot instance similarity and to that extent also substitution of instances along these dimensions: hardware configuration, hardware capacity, software, and location. We study these dimensions because prior research finds that customers may choose resources from spot market based only on these dimensions [2,13].<sup>5</sup> Since these dimensions are same across various cloud providers, it helps in generalizability of findings to broader cloud market. We measure these dimensions of spot instance substitution as dichotomous variables indicating 1 if two spot instances are same on a specific dimension and 0 otherwise. Thereafter, we develop hypotheses to test the relationships between similarity of spot instances along four di mensions and their substitution. Moreover, we also hypothesize the interaction among the similarity dimensions of spot instances and thei substitution.

We hypothesize that consumers or buyers of spot instances are likely to substitute computing resources with similar hardware configuration because applications running on a particular type of hardware config uration can be relatively easily moved to another spot instance with same hardware configuration. On the other hand, moving an application to a computing resource with different configuration is likely to be hard and time consuming, and even infeasible. This in turn, is likely to lead to positive spot price association of resources with similar hardware configuration. Moreover, hardware capacity, software, and location similarities are likely to positively moderate the substitution of spot instances having hardware configuration similarity. This is so because of two reasons. First, if two spot instances have same hardware configu ration, then consumers may consider substituting between those in stances to take advantage of price difference. In other words, based on real-world computing environment considerations, hardware configu ration similarity is an important dimension of spot instance substitution. Second, if two resources are similar on dimension of hardware config uration along with other dimensions like hardware capacity or software or datacenter location, then it may be even easier for customers to move applications from a particular spot instance to another.

Further, we use one year Amazon AWS spot market data for the yea 2015 and employ ordinary least square method with robust standard errors to test our hypotheses. We find evidence that the hardware configuration similarity is positively related to the spot prices covari ance of similar instances which implies that consumers substitute spot instances which are similar on the dimension of hardware configuration similarity to take advantage of spot price differences. Moreover, spot instance similarity along hardware capacity and location dimensions positively moderate this relationship.

Our research makes following contributions to the literature. We extend the theoretical understanding of cloud spot market by demon strating that customers substitute computing resources located in the same zone (location) if two resources have similar hardware configu rations. Moreover, customers are more likely to substitute resources having similar hardware configurations, if the resources also have hardware capacity and location similarity. These findings extend the research by Cheng et al. [13], which does not examine the substitution among the similar spot instances within a region. While Cheng et al. show that consumers do not substitute computing resources across distant regions due to costs associated with latency, we show that within the same region customers substitute those resources which are similar along hardware configuration, and this substitution effect is positively moderated by spot instance similarity along dimensions of hardware capacity and location within the same region.

Our work also contributes to practice. The practitioners are likely to treat the spot instances as independent entities and assume that their prices are independent of each other. Further, the practitioner’s literature or trade articles do not provide any suggestions to managers on considering the relations between prices of spot instances on various dimensions when choosing such resources in cloud spot market. Our research findings help practitioners by providing guidance to take informed decision in choosing spot instances by considering the simi larity of these instances along the dimension of hardware configuration similarity and moderating dimensions of hardware capacity and data center location. Our findings are likely to help practitioners to take advantage of spot price relationships in sourcing decisions.

The rest of the paper is organized as follows. In §2, we present the related work followed by theory and hypothesis development in §3. In §4 and §5, we present variable construction and the empirical model, respectively. In §6, we present the data followed by hypotheses test re sults in §7. We discuss the findings in §8 and conclude in §9.

## 2. Related work

Yang and Tate [20] identified pricing as one of the key business is sues in cloud computing and highlight the scarcity of research addressing this issue. There are two types of pricing models in cloud computing: pay-per-use fixed price and spot or variable price [13]. Our paper contributes to the cloud pricing literature by examining the price dynamics of similar computing resources offered simultaneously in the cloud spot market.

Spot pricing in cloud computing has received recent attention in Information Systems research [13] and practice [21]. There are opera tional and managerial challenges in the adoption of this pricing model. The initial research addressing the operational challenges developed algorithms to forecast the next-hour spot price to help customers request for spot instances [16,17,22,23]. One of the key assumptions in this stream of research is that the prices of spot instances are independent of each other. However, the research by Cheng et al. [13] point towards the need for further research to understand the relationships among the prices of different computing resources offered simultaneously in this market.

Cheng et al. [13] examine the difference between spot prices of identical computing resources in two different regions – US-East and US-West – and demonstrate that the prices of computing resources are higher in US-West region compared to US-East region, and this differ ence in spot prices is explained through the difference in Internet latency across these two regions. While Cheng et al. demonstrate that customers do not substitute identical computing resources being offered in two different regions taking advantage of arbitrage opportunity due to associated Internet latency costs, we explore the relationships among spot prices of similar computing resources within a region. In other words, Cheng et al. examine the price relationships across two different regions; we extend that work by investigating relationships between spot prices at a relatively shorter geographical distances – that is across zones which is a sub-regional geography (there are multiple zones within a region).

Some of the research in IS have investigated the pricing challenges from the cloud vendor’s perspective [8,9]. While customers assume that cloud providers have unlimited resources, cloud vendors absorb much of the risk related to the uncertain demands of customers resulting in high underutilization of resources in off-peak hours. Du et al. [9] and Das et al. [8] propose dynamic forward contract mechanisms for efficient risk hedging for the cloud vendors. Unlike the above stream of research which focuses on cloud demand uncertainties faced by vendors, our study focuses on understanding the behavior of consumers or users or buyers of computing resources offered in the cloud spot market.

Digital infrastructure is an important category of IT artifact defined as “the basic information technologies and organizational structures, along with related services and facilities necessary for an enterprise or industry to function” [24](p.1). Cloud computing, especially its Infrastructure-as-a-Service (IaaS) delivery model is one of the contem porary topics in the area of digital infrastructure research [24].

Nevertheless, there is a paucity of research investigating digital in frastructures in Information Systems [20,24]. Our work also contributes to the research on digital infrastructure by extending our understanding of consumer behavior in the cloud spot market.

Understanding the issues affecting three key stakeholders in cloud computing, namely providers, consumers, and governmental agencies, has been one of the key research topics in the field of decision support systems research [25–27]. In addition to these key stakeholders, effects of cloud computing on economic and environmental performance have been examined for understanding the balance between economic per formance and sustainability of cloud computing in the decision support systems research [26]. Our paper contributes to understanding the economic performance of cloud computing for consumers who are one of the key stakeholders in the cloud computing ecosystem.

There are different methods used to study challenges in cloud computing: (1) empirical [13], and (2) analytical [5,9,28]. Further, relatively there are more studies in the IS literature on this topic applying analytical method compared to the empirical method. This may be due to challenges related to data access from cloud platforms. Moreover, analytical studies investigate fundamental properties of cloud computing, such as auto-scaling [28]; however, these studies lack focus on dynamic behaviors like resource substitution. The empirical studies on this topic complement analytical research by validating and extending existing theories using data. Our study applies substitution effect as the theoretical lens and uses empirical method to test the hy potheses relating to instance substitution in the spot market.

## 3. Theory and hypothesis development

## 3.1. Substitution in production and consumption

In economics, if two goods are substitutes in consumption, then an increase in the price of one good leads to an increase in demand for the substitute good [19]. In the cloud spot market, because the compute resources or instances overlap in some of their attributes or dimensions, it is feasible for a consumer to substitute one computing resource with another similar resource if the spot price of similar resource is lower. For example, consider two resources A and B, which are similar to each other along all or some of the dimensions of hardware configuration, hardware capacity, software, and data center location. If customers substitute resource A with B, then an increase in the spot price of A is likely to lead to customers substituting A with B, which in turn will lead to an increase in demand for B, leading to an increase in the spot price of B assuming that the supply of A and B are fixed. In other words, if consumers substitute resource A with B, then it is likely that increase in spot price of A will lead to increase in price of B due to increase in de mand for B resulting from substitution. This implies that, if customers substitute similar computing resources in the spot market, then spot prices of similar resources are likely to be positively associated with each other.

In a cloud computing data center, the resources are instantiated as virtual machines (or instances) using virtualization technology and share underlying hardware [29]. Since the capacity of a cloud data center is fixed in a short time period and computing resources share the underlying hardware, these resources are substitutes in production too [30]. In economics, two goods are substitutes in production if both goods are produced from the same resource; and if the price of one good increases, it decreases the supply for the other good because the pro ducer shifts the resources to increase the supply of the good whose price has increased, leading to decrease in resources for the production of the other good. Therefore, if computing resources A and B are substitutes in production, then an increase in the price of A will decrease the supply for B which would lead to increase in price of B. Thus, considering both substitutions in production and consumption, if resource A and B are substitutes, then the increase in the price of A will lead to increase in the price of B. To that extent, a measure of spot price association of price of

A and B, is a good measure of substitution of A and B in the spot market.

When the cloud provider either does not choose to or is unable to change the supply of underlying computing resources, the supply of different computing resources in cloud data centers remains constant over a short period of time, leading to no production side substitution [30]. Even in this case, due to substitution in consumption, an increase in the price of A will lead to increase in the price of B.

## 3.2. Similarity of spot instances

One of the key objectives of customers utilizing cloud computing is to reduce their operational cost. The problem of selecting appropriate re sources to address the operational requirements, at the same time reducing the cost, is an important challenge which has been highlighted in the recent IS research [2] which focuses on the resource selection problem in fixed-price cloud market where customers select a set of computing resources (to complete their computing task), minimizing the total cost. On the other hand, unlike the fixed-price cloud market in [2], we study the resource selection problem in spot market where prices of the resources are dynamic. In this market, customers select resources based on their dynamic price and operational requirements, wherein cloud provider offers a diverse set of resources (instances) in spot market along four dimensions – hardware configuration, hardware capacity, software, and location of the data center. These spot instances may be identical or similar along one or more of these four dimensions. In this setting, customers may substitute resources based on spot prices and their similarity on different dimensions.

The spot instances are offered with different hardware type specifi cations which are along two dimensions: hardware configuration and hardware capacity. For example, a computing resource having hardware-type ‘M3.2xlarge’ has hardware configuration ‘M3’ and hardware capacity ‘2xlarge’. The cloud provider offers computing re sources with different hardware configurations and capacities so that customers may choose appropriate resources based on their business requirements.

## 3.2.1. Hardware configuration similarity

A customer can migrate an application from one computing resource to another if both resources have similar hardware configurations to take advantage of their price difference. This is because the customers run their applications on resources whose hardware configurations (representing their processor architectures) support applications’ re quirements. For example, most deep learning-based applications require GPU hardware configuration for model training [31]. Therefore, cus tomers running deep learning-based applications are more likely to use resources of ‘G2’ category (see Table 2 for list of categories), which provide GPU processors. This implies that consumers will consider substituting spot instances having similar hardware configuration, which in turn would lead to positive spot price association of these in stances. This leads to the following hypothesis.

H1. Hardware configuration similarity of two spot instances will be posi tively associated with their substitution.

## 3.2.2. Hardware capacity similarity

The second sub-dimension of hardware type is hardware capacity. Computing resources are available in varying hardware capacities such as ‘small’, ‘medium’, ‘large’, etc. (see Table 2). The hardware capacity is determined based on the application’s load requirement (for example, the number of users that can be served by the computing resource) [2]. Thus, one would expect that customers are more likely to substitute when two instances have same hardware capacity given that instances are similar on hardware configuration. In light of above mechanism, we posit the following hypothesis:

H2a. Hardware capacity similarity of two spot instances will positively moderate the relationship between hardware configuration similarity of these

instances and their substitution

## 3.2.3. Software similarity

Computing resources are available with different software (or operating systems) such as Linux/UNIX, Windows, and SUSE Linux. Applications require specific software and deployment environment for execution. The software provides an abstraction from the underlying hardware and enables applications to run seamlessly on different hardware types. For example, an application developed for Windows operating system can run on different computing resources with similar operating systems. The customers may migrate their applications from one resource to another having same software to take advantage of their price difference when two resources have similar hardware configura tion. Thus, we have the following hypothesis.

H2b. Software similarity of two spot instances will positively moderate the relationship between hardware configuration similarity of these instances and their substitution

## 3.2.4. Location (zone) similarity

The cloud computing data centers are organized in a hierarchical order consisting of two levels – region and zone wherein each region consists of multiple zones. We focus on analyzing substitution between computing resources offered within a region but across different zones. Two resources have location similarity if both belong to the same zone. Prior research has investigated the price differences between identical computing resources in different regions (US-East and US-West) [13].

Customers may choose to migrate their applications from one resource to another within same zone because of two factors. First, the Internet latency difference to migrate an application within a zone is smaller due to proximity (located in the same data center) compared to migrating the same application from one region to another. Second, there is no cost of data transfer for migrating applications within the same zone. Thus, we posit the following hypothesis.

H2c. Location similarity of two spot instances will positively moderate the relationship between hardware configuration similarity of these instances and their substitution

## 4. Variable construction

## 4.1. Dependent variable

As discussed earlier, based on the economic theory of substitution in production and consumption, the increase (decrease) in price of one computing resource will increase (decrease) the price of other substi tutable resources. Therefore, we use price association measured using covariance of their prices over time as a measure of their substitution. Covariance has been used as a measure of similarity in the literature [32]. Moreover, we choose covariance instead of correlation because for resources with constant prices over time, the pairwise correlation is not defined. The covariance $Y _ { i , j }$ of prices of the two spot instances i and j is given in Eq. (1):

$$
Y _ {i, j} = \frac {1}{n - 1} \sum_ {k = 1} ^ {k = n} \left(x _ {i, k} - \overline {{x _ {i}}}\right) \left(x _ {j, k} - \overline {{x _ {j}}}\right)\tag{1}
$$

wherein n represents the number of price observations for each resource and $x _ { i , \ k }$ and $x _ { j , \ k }$ represent the spot prices of resources i and j at time (hour) k. Moreover, $\overline { { x _ { i } } }$ and $\overline { { x _ { j } } }$ represent the sample means of prices of spot instances i and j, respectively.

## 4.2. Independent variables

We define Hardware Configuration similarity (HCo) and Hardware Capacity similarity (HCa) as follows.

HCo = 1 If computing resources i and j have same hardware

configuration.

= 0 Otherwise.

H $\mathit { \Pi } _ { \mathit { \hat { \Pi } } } { } _ { a _ { i , \ j } } = 1 \ : \ : \ : \mathit { \Pi } _ { I f }$ computing resources i and j have same hardware capacity.

= 0 Otherwise.

Similarly, we define software (So) and location (L) similarity as follows.

So<sub>i,</sub> $\mathbf { \Phi } _ { j } ~ = ~ \mathbf { \Phi } _ { 1 }$ If computing resources i and j have same software or operating system.

= 0 Otherwise.

$L _ { i , j } \quad = 1$ If computing resources i and j have same location or zone. $= o$ Otherwise.

## 5. Empirical model

To test our hypotheses, we present the model specification in Eq. (2). The dependent variable is the price association between two resources which is the measure of their substitution. The independent variables include hardware configuration similarity, hardware capacity similar ity, software similarity, and location similarity. $\epsilon _ { i , j }$ represents the error term.

$$
\begin{array}{l} Y _ {i, j} = \beta_ {0} + \beta_ {1} H C o _ {i, j} + \beta_ {2} H C o _ {i, j} \times S o _ {i, j} + \beta_ {3} H C o _ {i, j} \times L _ {i, j} + \beta_ {4} H C o _ {i, j} \times H C a _ {i, j} \\ + \beta_ {5} H C a _ {i, j} + \beta_ {6} S o _ {i, j} + \beta_ {7} L _ {i, j} + \epsilon_ {i, j} \end{array} \tag {2}
$$

## 6. Data

We collected data for all 399 spot instances available in US-West region over a period of one year (January to December 2015) from Amazon Web Services (AWS). The AWS provides software development kit or SDK in Python programming (also known as Boto3) and other Additionally, AWS provides command line interface (CLI) which is a software that can be installed on a computer to communicate to the cloud infrastructure.<sup>7</sup> The AWS CLI uses the SDK underneath. We created an account on AWS platform and received access keys which we used with AWS CLI and SDK to collect the historic spot price data. The data collection and processing pipeline is shown in Fig. 1.

The data consists of dynamic prices of spot instances in real-time. At any time, AWS offers historical spot price data for past 90 days using an interactive web dashboard (website) for browsing and downloadable via programmable APIs discussed above. We developed a computing infrastructure to collect the spot price data for 90 days.<sup>8</sup> The details of different data attributes of the raw data collected are presented in Table 1. We follow data preparation steps similar to Cheng et al. [13] and aggregate the data at an hourly level by taking the last updated price within each hour. Since the data collected from AWS provides the updated price over time when there is a change, we keep the price of the previous hour for the current hour if there is no change in the price in the current hour. These steps are part of data processing as shown in Fig. 1. Finally, the processed data was stored in a MySQL database.

In our dataset, there are 28 different hardware types consisting of different hardware configurations and capacities, as shown in Table 2. The hardware configurations are further clustered under different hardware groups. These groups are compute-optimized, memory-opti mized, general-purpose, graphics processing, optimized for input/ output, and micro. A compute-optimized instance has high-performance processor suitable for jobs like batch processing, high-performance computing, etc. A Memory-optimized instance has high memory capacity, which is useful for analyzing large datasets in memory. A general-purpose instance has low-performance processor and low memory capacity and is useful for a variety of different generic work loads like web servers, code repositories, etc. Finally, the graphicsprocessing instance and input/output instance are specialized hard ware instances for multimedia processing and low latency database applications, respectively. Consumers can substitute spot instances with same hardware configuration.

In Table 3, we present the summary statistics of spot instances available over three different software: SUSE Linux, Windows, and Linux/UNIX. As we can see from the table, the number of instances offered is equally available in three different software. For example, for SUSE Linux software, there are 134 instances offered with different combinations of hardware configuration, hardware capacity, and zones. We present minimum, maximum, and average price per hour for these instances over time. The average price per hour for instances with Windows operating system is slightly higher compared to those with SUSE Linux and Linux/UNIX. Also, between SUSE Linux and Linux/ UNIX, the former has slightly higher average price than the latter. These price differences can be explained based on the cost of license associated with commercial software compared to its open source alternatives [33].

The hardware configuration represents the processor type, and hardware capacity represents the number of virtual cores of processors and memory size. For example, C1.xlarge configuration contains Xeon processor with eight virtual cores and 7GB of memory. A hardware configuration is available in different hardware capacities. For example, as shown in Table 2, the hardware configuration ‘C1’ is available in two hardware capacities: medium and xlarge. There are 13 different types of hardware capacities, namely nano, micro, small, medium, large, xlarge, 2xlarge, 4xlarge, 8xlarge, 10xlarge, 12xlarge, 16xlarge, 24xlarge, in the increasing order of their size. For example, 4xlarge is of higher capacity than 2xlarge, and so on. Hardware capacity is another dimension on which consumers can consider substituting spot instances if the in stances have similar hardware configurations. There are no such subcategories in the software attribute. Location attribute is divided into zones with in US-West region.

The cloud provider charges for the license cost using pay-per-use model and not a one-time cost. Further, the provider manages soft ware compliance and versions. The Windows operating system is a commercial software, SUSE Linux has both commercial and open source versions, and Linux/UNIX is available as an open source software. However, the maximum price per hour is influenced by the demand for resources of each software type. Although the average price per hour of compute resources with Linux/UNIX operating system is lower compared to other two software, the maximum price per hour of the former is higher than the latter two software.

Table 4 presents the descriptive statistics of spot prices for 28 different hardware types – combinations of hardware configurations and hardware capacities (jointly referred as hardware type) – available in the US-West region. For example, the computing resource C1.medium has hardware configuration ‘C1’ which is compute-optimized (see Table 2) and its capacity is ‘medium.’

The average price per hour of instances with certain hardware configuration increases with increase in their capacities. For example, for two instances C1.medium and C1.xlarge have the same hardware configuration; however, the average price per hour of C1.xlarge is higher than C1.medium because the capacity of the former is larger than the latter. The interesting aspect of spot price is that although the average price of C1.medium is lower compared to C1.xlarge due to lower capacity, the maximum price per hour observed is higher for the former instance indicating that there are durations of time when the demand for C1.medium is higher compare to C1.xlarge.

Finally, in Table $^ { 5 , }$ we present the availability of instances in five zones within US-West region. The minimum price per hour across in stances in different zones is identical (0.003 USD) which is the minimum price per hour of the instance T1.micro (see Table 3). Moreover, average and maximum price per hour of the instances across zones are similar. This indicates that the average price per hour of instances in different locations are homogeneous.

![](/api/attachments/YRJB59C4/fulltext/images/988d0317819915987152848a88a34a6d47ef4a47c99e51ea8f51daa2d17ec6f3.jpg)  
Fig. 1. Data collection and processing pipeline.

Table 1  
Details of attributes in raw data.

<table><tr><td>Variable</td><td>Details</td></tr><tr><td>Price</td><td>The price of a spot instance at a specific time. The price is not available at regular intervals and is only provided when there is a change in the current price. When there is no change in the current price, then the current price is same as the last updated price.</td></tr><tr><td>Date-time</td><td>Date and time</td></tr><tr><td>Hardware type</td><td>Hardware capacity and configuration of the spot instance</td></tr><tr><td>Software</td><td>Software (operating system) of the spot instance</td></tr><tr><td>Location</td><td>Location of the data center (or zone) where the spot instance is being offered</td></tr></table>

Table 2  
Hardware types description.

<table><tr><td>Hardware Group</td><td>Hardware Configuration</td><td>Hardware Capacity</td><td>Hardware Type</td></tr><tr><td rowspan="8">Compute Optimized</td><td rowspan="2">C1</td><td>Medium</td><td>C1.Medium</td></tr><tr><td>xlarge</td><td>C1.xlarge</td></tr><tr><td rowspan="5">C3</td><td>large</td><td>C3.large</td></tr><tr><td>xlarge</td><td>C3.xlarge</td></tr><tr><td>2xlarge</td><td>C3.2xlarge</td></tr><tr><td>4xlarge</td><td>C3.4xlarge</td></tr><tr><td>8xlarge</td><td>C3.8xlarge</td></tr><tr><td>CC2</td><td>8xlarge</td><td>CC2.8xlarge</td></tr><tr><td rowspan="8">General Purpose</td><td rowspan="4">M1</td><td>small</td><td>M1 small</td></tr><tr><td>medium</td><td>M1.medium</td></tr><tr><td>large</td><td>M1.large</td></tr><tr><td>xlarge</td><td>M1.xlarge</td></tr><tr><td rowspan="4">M3</td><td>medium</td><td>M3.medium</td></tr><tr><td>large</td><td>M3.large</td></tr><tr><td>xlarge</td><td>M3.xlarge</td></tr><tr><td>2xlarge</td><td>M3.2xlarge</td></tr><tr><td>Graphics Processing Unit</td><td>G2</td><td>2xlarge</td><td>G2.2xlarge</td></tr><tr><td rowspan="9">Memory Optimized</td><td rowspan="3">M2</td><td>xlarge</td><td>M2.xlarge</td></tr><tr><td>2xlarge</td><td>M2.2xlarge</td></tr><tr><td>4xlarge</td><td>M2.4xlarge</td></tr><tr><td>CR1</td><td>8xlarge</td><td>CR1.8xlarge</td></tr><tr><td rowspan="5">R3</td><td>large</td><td>R3.large</td></tr><tr><td>xlarge</td><td>R3.xlarge</td></tr><tr><td>2xlarge</td><td>R3.2xlarge</td></tr><tr><td>4xlarge</td><td>R3.4xlarge</td></tr><tr><td>8xlarge</td><td>R3.8xlarge</td></tr><tr><td>Micro</td><td>T1</td><td>micro</td><td>T1.micro</td></tr><tr><td>Optimized for Input/Output</td><td>Hi1</td><td>4xlarge</td><td>Hi1.4xlarge</td></tr></table>

## 7. Results

We present the summary statistics and correlation among the inde pendent variables – hardware configuration, hardware capacity, soft ware, and location, and the dependent variable in Tables 6a and 6b. We can observe that there are no high correlation values (>0.7), which implies that we do not have to be concerned about the issue of multi collinearity. We used ordinary least square (OLS) estimator with robust standard errors (Cameron and Trivedi 2010) to test our hypotheses and present the results in Models 1–4 in Table 7. Model 1 includes hardware configuration similarity along with other control variables to test the hypothesis H1. In Model 2, we have included the interaction term be tween hardware configuration similarity and hardware capacity simi larity to test the hypothesis H2a. To test the hypothesis H2b, we include the interaction term between hardware configuration similarity and software similarity in Model 3. In Model 4, to test the hypothesis H2c, we have included the interaction term between hardware configuration similarity and location similarity. Finally, in Model 5, we include all three interaction terms mentioned above together.

Table 3  
Spot price distribution of computing resources over software dimension.

<table><tr><td>Software</td><td>Number of instances offered $^{a}$ </td><td>Minimum price</td><td>Maximum price</td><td>Average price</td></tr><tr><td>SUSE Linux</td><td>134</td><td>0.007</td><td>1.402</td><td>0.282</td></tr><tr><td>Windows</td><td>131</td><td>0.006</td><td>10.848</td><td>0.374</td></tr><tr><td>Linux/ UNIX</td><td>134</td><td>0.003</td><td>20.831</td><td>0.219</td></tr></table>

<sup>a</sup> Instance is a unit of compute resource.

Table 4  
Spot price distribution of compute resources over hardware dimension.

<table><tr><td>Hardware type</td><td>Number of instances offered</td><td>Minimum price</td><td>Maximum price</td><td>Average price</td></tr><tr><td>C1.medium</td><td>15</td><td>0.016</td><td>20.000</td><td>0.058</td></tr><tr><td>C1.xlarge</td><td>15</td><td>0.064</td><td>2.640</td><td>0.174</td></tr><tr><td>M3.large</td><td>15</td><td>0.016</td><td>1.4</td><td>0.163</td></tr><tr><td>M3.medium</td><td>15</td><td>0.008</td><td>1.00</td><td>0.081</td></tr><tr><td>M3.xlarge</td><td>15</td><td>0.032</td><td>2.1</td><td>0.203</td></tr><tr><td>M3.2xlarge</td><td>15</td><td>0.064</td><td>5.6</td><td>0.381</td></tr><tr><td>C3.large</td><td>15</td><td>0.016</td><td>1.05</td><td>0.071</td></tr><tr><td>C3.8xlarge</td><td>15</td><td>0.256</td><td>19.120</td><td>1.443</td></tr><tr><td>C3.4xlarge</td><td>15</td><td>0.128</td><td>8.400</td><td>0.430</td></tr><tr><td>C3.xlarge</td><td>15</td><td>0.032</td><td>3.500</td><td>0.120</td></tr><tr><td>C3.2xlarge</td><td>15</td><td>0.064</td><td>4.780</td><td>0.226</td></tr><tr><td>CC2.8xlarge</td><td>9</td><td>0.253</td><td>2.000</td><td>0.388</td></tr><tr><td>M2.2xlarge</td><td>15</td><td>0.032</td><td>1.120</td><td>0.232</td></tr><tr><td>M2.4xlarge</td><td>15</td><td>0.064</td><td>7.360</td><td>0.364</td></tr><tr><td>M2.xlarge</td><td>15</td><td>0.016</td><td>3.450</td><td>0.093</td></tr><tr><td>G2.2xlarge</td><td>15</td><td>0.064</td><td>7.670</td><td>0.618</td></tr><tr><td>M1.large</td><td>15</td><td>0.016</td><td>0.500</td><td>0.058</td></tr><tr><td>M1.medium</td><td>15</td><td>0.008</td><td>0.210</td><td>0.029</td></tr><tr><td>M1.small</td><td>15</td><td>0.008</td><td>0.096</td><td>0.017</td></tr><tr><td>M1.xlarge</td><td>15</td><td>0.032</td><td>5.000</td><td>0.106</td></tr><tr><td>R3.2xlarge</td><td>15</td><td>0.064</td><td>7.000</td><td>0.296</td></tr><tr><td>R3.4xlarge</td><td>15</td><td>0.128</td><td>14.000</td><td>0.620</td></tr><tr><td>R3.8xlarge</td><td>15</td><td>0.256</td><td>15.000</td><td>0.976</td></tr><tr><td>R3.large</td><td>15</td><td>0.016</td><td>1.950</td><td>0.135</td></tr><tr><td>R3.xlarge</td><td>15</td><td>0.032</td><td>3.500</td><td>0.185</td></tr><tr><td>Hi1.4xlarge</td><td>9</td><td>0.135</td><td>0.726</td><td>0.293</td></tr><tr><td>T1.micro</td><td>15</td><td>0.003</td><td>1.000</td><td>0.006</td></tr><tr><td>CR1.8xlarge</td><td>6</td><td>0.258</td><td>3.500</td><td>0.619</td></tr></table>

Table 5  
Spot price distribution of compute resources over location dimension.

<table><tr><td>Location (Zones)</td><td>Number of instances offered</td><td>Minimum price</td><td>Maximum price</td><td>Average price</td></tr><tr><td>us-west-1b</td><td>75</td><td>0.003</td><td>20.000</td><td>0.356</td></tr><tr><td>us-west-1c</td><td>75</td><td>0.003</td><td>19.120</td><td>0.286</td></tr><tr><td>us-west-2a</td><td>83</td><td>0.003</td><td>15.000</td><td>0.264</td></tr><tr><td>us-west-2b</td><td>83</td><td>0.003</td><td>15.000</td><td>0.266</td></tr><tr><td>us-west-2c</td><td>83</td><td>0.003</td><td>16.800</td><td>0.289</td></tr></table>

Table 7 Regression results.  
Table 6 a: Summary statistics.

<table><tr><td>Variable</td><td>Obs</td><td>Mean</td><td>Std. Dev.</td><td>Min</td><td>Max</td></tr><tr><td>Price covariance</td><td>79,401</td><td>0.004</td><td>0.083</td><td>-9.414</td><td>8.942</td></tr><tr><td>Hardware configuration</td><td>79,401</td><td>0.136</td><td>0.343</td><td>0</td><td>1</td></tr><tr><td>Hardware capacity</td><td>79,401</td><td>0.153</td><td>0.360</td><td>0</td><td>1</td></tr><tr><td>Software</td><td>79,401</td><td>0.332</td><td>0.471</td><td>0</td><td>1</td></tr><tr><td>Location</td><td>79,401</td><td>0.198</td><td>0.399</td><td>0</td><td>1</td></tr></table>

<table><tr><td colspan="6">b: Summary statistics: correlations</td></tr><tr><td>Variable</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Price covariance</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>Hardware configuration</td><td>0.072***</td><td>1</td><td></td><td></td><td></td></tr><tr><td>Hardware capacity</td><td>0.044***</td><td>0.089***</td><td>1</td><td></td><td></td></tr><tr><td>Software</td><td>0.005</td><td>-0.009**</td><td>-0.008**</td><td>1</td><td></td></tr><tr><td>Location</td><td>0.008*</td><td>-0.012***</td><td>-0.011***</td><td>-0.007**</td><td>1</td></tr></table>

\*\*\*p < 0.01;\*\* < 0.05; $^ { \ast } p < 0 . 1$

We find support for hypothesis H1 which states that the similarity of spot instances based on hardware configuration is positively related to their substitution as shown in Model 1 in Table 7. We also find support for Hypotheses H2a and H2c which state the relationship in hypothesis H1 is moderated by similarity of two spot instances based on hardware capacity and location in Models 2 and $^ { 4 , }$ respectively, in Table 7.

<table><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Variables</td><td colspan="5">Dependent Variable: Price covariance</td></tr><tr><td rowspan="2">Hardware config. (HCo)</td><td>0.017***</td><td>0.010***</td><td>0.017***</td><td>0.014***</td><td>0.006***</td></tr><tr><td>(0.001)</td><td>(0.001)</td><td>(0.002)</td><td>(0.001)</td><td>(0.001)</td></tr><tr><td rowspan="2">Hardware Capacity (HCa)</td><td>0.009***</td><td>0.003***</td><td>0.009***</td><td>0.009***</td><td>0.003***</td></tr><tr><td>(0.001)</td><td>(0.001)</td><td>(0.001)</td><td>(0.001)</td><td>0.001</td></tr><tr><td rowspan="2">Software (So)</td><td>0.001*</td><td>0.001**</td><td>0.001**</td><td>0.001*</td><td>0.001*</td></tr><tr><td>(0.001)</td><td>(0.001)</td><td>(0.001)</td><td>(0.001)</td><td>(0.001)</td></tr><tr><td rowspan="2">Location (L)</td><td>0.002**</td><td>0.002**</td><td>0.002**</td><td>-0.000</td><td>-0.000</td></tr><tr><td>(0.001)</td><td>(0.001)</td><td>(0.001)</td><td>(0.000)</td><td>(0.001)</td></tr><tr><td rowspan="2">HCo × HCa</td><td></td><td>0.030***</td><td></td><td></td><td>0.031***</td></tr><tr><td></td><td>(0.006)</td><td></td><td></td><td>(0.002)</td></tr><tr><td rowspan="2">HCo × So</td><td></td><td></td><td>-0.001</td><td></td><td>0.000</td></tr><tr><td></td><td></td><td>(0.003)</td><td></td><td>(0.002)</td></tr><tr><td rowspan="2">HCo × L</td><td></td><td></td><td></td><td>0.015***</td><td>0.017***</td></tr><tr><td></td><td></td><td></td><td>(0.006)</td><td>(0.002)</td></tr><tr><td rowspan="2">Constant</td><td>-0.001</td><td>0.000</td><td>-0.001</td><td>-0.000</td><td>0.001</td></tr><tr><td>(0.000)</td><td>(0.000)</td><td>(0.000)</td><td>(0.000)</td><td>(0.000)</td></tr><tr><td>Observations</td><td>79,401</td><td>79,401</td><td>79,401</td><td>79,401</td><td>79,401</td></tr><tr><td>R-squared</td><td>0.007</td><td>0.009</td><td>0.007</td><td>0.007</td><td>0.010</td></tr></table>

Hco: Hardware configuration similarity; Hca: Hardware capacity similarity; So: Software similarity; L: Location similarity. Note: All values are rounded to three decimal places.  
\*\*\*p < 0.01;\*\* < 0.05; \*p < 0.1.

The visualization of moderating effects of hardware capacity simi larity, and location similarity are presented in Fig. 2(a) and 2(c). In Fig. 1(a), the blue line represents the condition when two instances have different hardware capacities, and the red line represents the condition when two instances have same hardware capacity. As you can observe from the figure that the likelihood of substitution when two instances have similar hardware configuration and hardware capacity is signifi cantly greater than the likelihood of substitution when two instances have only similar hardware configuration. Similarly, as shown in Fig. 2 (c), two spot instances having similar location and hardware configu ration similarity have significantly higher likelihood of substitution compared to two instances having only similar hardware configuration. Finally, as shown in Fig. 2 (b), we do not find significant difference in likelihood of substitution of two instances having similar hardware configuration and software similarity compared to the likelihood of substitution of two instances having only hardware configuration similarity.

We did not find support for H2b which hypothesized positive moderating effect of software similarity on the relationship between hardware configuration similarity of two instances and their substitu tion. One plausible explanation is that the software (or operating sys tem) provides an abstraction over the hardware configurations; and customer can use this abstraction to migrate their applications across spot instances with different hardware configurations. Therefore, unlike hardware capacity similarity and location similarity, the software dimension similarity is directly related to the spot instance substitution. This is also supported by significant coefficients of software similarity across models presented in Table 7. We present the summary of results of the hypotheses testing in Table 8.

## 8. Discussion

In this paper, we examined the substitution effect among the compute resources within a region in cloud spot market. Based on the economic theory of substitution in production and consumption, we use price association as a measure of substitution between similar compute resources. We show that the hardware configuration similarity is an important dimension of substitution and this substitution effect is positively moderated by similarity on other two dimensions – hardware capacity and location, while software similarity has no moderating effect.

The findings of our research are important, specifically in the domain of cloud computing, though are also relevant in e-commerce domain in certain aspects. First, we extend the understanding of relationships among the prices of spot instances in cloud computing. Understanding the cloud computing pricing and resource allocation mechanisms are important areas of research in Information Systems [13,28,34,35] due to rapid adoption of cloud computing [36]. Second, our findings are generalizable to e-commerce context where some e-retailers sell similar goods using second price auction mechanisms such as on eBay. Based on the empirical analysis of spot prices in cloud spot market, it is likely that the prices of similar products in these e-market platforms move together because consumers substitute among similar products, and to that extend these findings may help platform owners in designing appro priate pricing strategies. Moreover, understanding auction of multiple items is a contemporary research topic in Information Systems [37,38].

## 8.1. Contributions to literature

Recent research by Cheng et al. [13], one of the first studies on cloud spot market in IS research find that customers do not arbitrage compute resources across two different distant locations (regions) even when there is a significant price difference between identical resources in two locations. This absence of arbitrage has been explained by the differ ences in the Internet latency in these regions. While Cheng et al. [13] focus on compute resources across regions, we study these resources within a region (in different zones), and find that customers substitute similar instances across four similarity dimensions. Furthermore, in a framework where hardware similarity is an important dimension, cus tomers substitute computing resources only if they are similar along this dimension. The similarity along hardware capacity, software and loca tion positively moderates the substitution along hardware configuration dimension. This finding is new in this stream of literature.

![](/api/attachments/YRJB59C4/fulltext/images/6278156eece592848e375f79197aa9e7fb03fec62d8289499e324dd6c7b43095.jpg)

![](/api/attachments/YRJB59C4/fulltext/images/a3decb52a2ebcc9fa5cbec5768b1b795088349153d55c624ca37568bea32027b.jpg)

![](/api/attachments/YRJB59C4/fulltext/images/0c5dfb003254196ebf63553eebc5381df05b3a3a8a76502dd18ef863e5892f4d.jpg)

![](/api/attachments/YRJB59C4/fulltext/images/4577c706787f6eca37497cc0e6fdf03798b53f36e5a333d7506cf29704f60ccd.jpg)

Fig. 2. Moderation effect graphs.  
![](/api/attachments/YRJB59C4/fulltext/images/22c087a2018785ef07342c33aa7cc6e712e6d8a6072fb8916abd23d6fb8f1636.jpg)

Table 8  
Hypothesis test summary.

<table><tr><td>Hypothesis</td><td>Result</td></tr><tr><td>H1: Hardware configuration similarity of two spot instances will be positively associated to their substitution.</td><td>Supported</td></tr><tr><td>H2a: Hardware capacity similarity of two spot instances will positively moderate the relationship between hardware configuration similarity of these instances and their substitution.</td><td>Supported</td></tr><tr><td>H2b: Software similarity of two spot instances will positively moderate the relationship between hardware configuration similarity of these instances and their substitution.</td><td>Not Supported</td></tr><tr><td>H2c: Location similarity of two spot instances will positively moderate the relationship between hardware configuration similarity of these instances and their substitution.</td><td>Supported</td></tr></table>

Yang and Tate [20] highlight paucity of research dealing with business issues in cloud computing, including adoption, privacy, legal, cost, trust, pricing and ethical issues. Our paper contributes towards three of the key business issues: adoption, pricing, and cost of cloud computing.

Much of the literature on spot instances in computer science has focused on predicting the spot price for a brief duration such as a nexthour spot price [16,17]. Such predictions can help customers choose their bids prices appropriately. However, in a cloud computing resource auction model such as spot instances, customers pay the market price or clearing price instead of their bid price, similar to a Vickrey auction [15]. Therefore, if a customer bids a value higher than the market price, he or she will get the resource and the usefulness of forecasting the next hour’s price to appropriately choose bid price is limited. Therefore, in this paper, we contribute to understanding the relationship among the prices of spot instances instead of forecasting.

## 8.2. Contribution to practice

In addition to contribution to the literature, we also contribute to the practice. The practitioners treat the spot instances as independent en tities and assume that their prices are independent of each other. The practitioner’s literature does not provide any suggestions on considering the relations between prices of spot instances on various dimensions when choosing such resources. With findings from our study, practi tioners can take more informed decision in selecting spot instances by considering their price relationships.

Since spot pricing models are a new phenomenon in cloud computing, there exist multiple opportunities for practitioners to use these resources to lower operational costs. First, cloud vendors provide different types of compute resources with diverse set of configurations with varying prices [2]. It is very difficult for customers to select the optimal configuration of resources based on spot instance characteris tics, job completion deadline, and price. Practitioners can leverage the findings from our study to select a group of computing resources comprising of fixed price and spot instances. Moreover, practitioners can also use application resource usage data to identify applications where resources from the spot pricing model can be used.

Organizations allocate budgets to their sub-units based on their re quirements. The budget allocation process acts as an incentive tool to control costs within sub-units [39]. It is challenging to estimate the budget for spot instances due to their dynamic prices. To estimate the budget for a spot instance, understanding the factors which impact its price will help organizations in better estimation. Our findings imply that organizations should consider substitution effect as one of the fac tors impacting the price of spot instances while estimating their budget for these instances.

## 8.3. Limitation and future research

There may be differences across users who provision computing re sources through spot market; however, our analysis considers average effects. We face data limitation because we only observe the prices of spot instances and not the individual demands. The modeling of het erogeneity in substitution of similar compute resources across users may be a potentially interesting area of future research. Further, studies in literature have considered forecasting spot prices using machine learning techniques; however, these studies consider the prices inde pendent [16,17]. Another future research direction is to incorporate substitution effect and the relationships among the prices of spot in stances for short-term and long-term spot price and budget forecasting.

## 9. Conclusion

Spot pricing models in cloud computing, such as Amazon spot in stances, are emerging business models. In this paper, we demonstrate that the customer substitute compute resources based on hardware configuration similarity. Moreover, hardware capacity and location similarity between computing resources positively moderates the above relationship. We did not find moderating effect of software similarity on the above relationship.

Our study makes several contributions to literature and practice. We contribute to the understanding of relationships among the prices of similar computing resources based on resource characteristics in the cloud spot market. This contribution is important because majority of research examining spot prices consider the prices independent. Prac titioners can leverage the theoretical findings to inform their resource selection by considering the relationships between the prices of spot instances in this market. Further, organizations can consider substitu tion effect among the spot instances as one of the factors impacting spot price in determining the budget for their spot instance usage.

## Credit author statement

Vivek Kumar Singh: Conceptualization, Methodology, Data collec tion and analysis, Original draft preparation; Kaushik Dutta: Concep tualization, Supervision, Reviewing and Editing; Shivendu Shivendu: Conceptualization, Methodology, Supervision, Reviewing and Editing.

## References

[1] Z. Zhang, G. Nan, Y. Tan, Cloud services vs. on-premises software: competition under security risk and product customization, Inf. Syst. Res. 31 (2020) 848–864, https://doi.org/10.1287/isre.2019.0919

[2] L. Hosseini, S. Tang, V. Mookerjee, C. Sriskandarajah, A switch in time saves the dime: a model to reduce rental cost in cloud computing, Inf. Syst. Res. 31 (2020) 753–775, https://doi.org/10.1287/ISRE.2019.0912.

[3] L. Kappelman, V.L. Johnson, C. Maurer, K. Guerra, E. McLean, R. Torres, M. Snyder, K. Kim, The 2019 SIM IT issues and trends study, MIS Q. Exec. 19 (2020) 69–104. https://doi.org/10.17705/2msqe.00026

[4] A. Bhattacherjee, S.C. Park, Why end-users move to the cloud: a migrationtheoretic analysis, Eur. J. Inf. Syst. 23 (2014) 357–372, https://doi.org/10.1057/ ejis.2013.1.

[5] C. Borgs, O. Candogan, J. Chayes, I. Lobel, H. Nazerzadeh, Optimal multi-period pricing with service guarantees, Manag. Sci. 60 (2014).

[6] T. Erl, R. Puttini, Z. Mahmood, Cloud Computing: Concepts, Technology, & Architecture, Pearson Education. 2013.

[7] P. Yu Chen, S. Yi Wu, The impact and implications of on-demand services on market structure. Inf, Syst. Res. 24 (2013) 750–767, https://doi,org/10.1287 isre 1120.0451

[8] A.Y. Du, S. Das, R. Ramesh, Efficient risk hedging by dynamic forward pricing: a study in cloud computing, INFORMS J. Comput. 25 (2013) 625–642.

[9] S. Das, A.Y. Du, R.D. Gopal, R. Ramesh, Risk management and optimal pricing in online storage grids, Inf. Syst. Res. 22 (2011).

[10] A. Mukherjee, R.P. Sundarraj, K. Dutta, Time-preference-based on-spot bundled cloud-service provisioning, Decis. Support. Syst. 151 (2021), https://doi.org/ 10.1016/j.dss.2021.113607.

[11] J. Huang, R.J. Kauffman, D. Ma, Pricing strategy for cloud computing: a damaged services perspective, Decis. Support. Syst. 78 (2015) 80–92, https://doi.org 10.1016/i.dss.2014.11.001

[12] Z. Cai, X. Li, R. Ruiz, Q. Li, Price forecasting for spot instances in cloud computing, Futur. Gener. Comput. Syst. 79 (2018) 38–53, https://doi.org/10.1016/j. future.2017.09.038.

[13] H.K. Cheng, Z. Li, A. Naranjo, Cloud computing spot pricing dynamics: latency and limits to arbitrage, Inf. Syst. Res. 27 (2016) 145–165, https://doi.org/10.1287/ isre.2015.0608.

[14] D. Kumar, G. Baranwal, Z. Raza, D.P. Vidyarthi, A survey on spot pricing in cloud computing, J. Netw. Syst. Manag. 26 (2018) 809–856, https://doi.org/10.1007/ s10922-017-9444-x.

[15] V. Krishna, Auction Theory, Academic Press, 2009.

[16] V.K. Singh, K. Dutta, Dynamic price prediction for amazon spot instances, Proc. Annu. Hawaii Int. Conf. Syst. Sci. 2015-March, 2015, pp. 1513–1520, https://doi org/10.1109/HICSS.2015.184.

[17] Y. Song, M. Zafer, K.W. Lee, Optimal bidding in spot instance market, Proc. - IEEE INFOCOM. (2012) 190–198, https://doi.org/10.1109/INFCOM.2012.6195567.

[18] L. Dierks, S. Seuken, Cloud pricing: the spot market strikes back, Manag. Sci. 68 (2021).

[19] N.G. Mankiw, Brief Principles of Macroeconomics, Cengage Learning, 2020.

[20] H. Yang, M. Tate, A descriptive literature review and classification of cloud computing research, Commun. Assoc. Inf. Syst. 31 (2012) 35–60, https://doi.org 10.17705/1cais.03102

[21] Spotinst, The State of the Amazon EC2 Spot Market. https://spot.io/the-state-of-th e-amazon-ec2-spot-market, 2017 (date accessed May 22, 2022)

[22] B. Javadi, R.K. Thulasiram, R. Buyya, Characterizing spot price dynamics in public cloud environments, Futur. Gener. Comput. Syst. 29 (2013) 988–999, https://doi. org/10.1016/j.future.2012.06.012.

[23] O. Agmon Ben-Yehuda, M. Ben-Yehuda, A. Schuster, D. Tsafrir, Deconstructing amazon EC2 spot instance pricing, ACM Trans. Econ. Comput. 1 (2013) 1–20, https://doi.org/10.1145/2509413.2509416.

[24] D. Tilson, K. Lyytinen, C. Sørensen, Digital infrastructures: the missing IS research agenda, Inf. Syst. Res. 21 (2010) 748–759, https://doi.org/10.1287 isre.1100.0318.

[25] S. Marston, Z. Li, S. Bandyopadhyay, J. Zhang, A. Ghalsasi, Cloud computing - the business perspective, Decis. Support. Syst. 51 (2011) 176–189, https://doi.org/ 10.1016/j.dss.2010.12.006.

[26] D.G. Schniederjans, D.N. Hales, Cloud computing and its impact on economic and environmental performance: a transaction cost economics perspective. Decis Support. Syst. 86 (2016) 73–82, https://doi.org/10.1016/i.dss.2016.03.009.

[27] N. Wang, H. Liang, Y. Jia, S. Ge, Y. Xue, Z. Wang, Cloud computing research in the IS discipline: a citation/co-citation analysis, Decis. Support. Syst, 86 (2016) 35–47 https://doi.org/10.1016/i.dss.2016.03.006

[28] A. Fazli, A. Sayedi, J.D. Shulman, The effects of autoscaling in cloud computing, Manag. Sci. 64 (2018) 5149–5163, https://doi.org/10.1287/mnsc.2017.2891.

[29] L. Wang, G. Von Laszewski, A. Younge, X. He, M. Kunze, J. Tao, C. Fu, Cloud computing: a perspective study, New Gener. Comput. 28 (2010) 137–146, https:// doi.org/10.1007/s00354-008-0081-5.

[30] I. Iyoob, E. Zarifoglu, A.B. Dieker, Cloud computing operations research, Serv. Sci. 5 (2013) 88–101, https://doi.org/10.1287/sery,1120.0038.

[31] K. Lee, M. Son, DeepSpotCloud: leveraging cross-region GPU spot instances for deep learning, IEEE Int. Conf, Cloud Comput. CLOUD (2017) 98–105, https://doi. org/10.1109/CLQUD.2017.21.201Z-June

[32] J.R. Busemeyer, J.T. Townsend, Decision field theory: a dynamic-cognitive approach to decision making in an uncertain environment, Psychol. Rev. 100 (1993) 432–459, https://doi.org/10.1037/0033-295X.100.3.432.

[33] AWS, Microsoft Licensing on AWS. https://aws.amazon.com/windows/resources licensing, 2022 (date accessed May 22, 2022).

[34] R. Keller, H. Lukas, S. Thomas, G. Fridgen, Scheduling flexible demand in cloud computing spot markets, Bus. Inf. Syst. Eng. 62 (2020). https://aisel.aisnet.or g/bise/vol62/iss1/4.

[35] A. Gera, C.H. Xia, Learning curves and stochastic models for pricing and provisioning cloud computing services, Serv. Sci. 3 (2001) 99–109. http://www. sersci.com/ServiceScience/upload/12895882940.pdf.

[36] F. Wulf, M. Westner, S. Strahringer, Cloud computing adoption: a literature review on what is new and what still needs to be addressed. Commun. Assoc, Inf, Syst. 48 (2021) 523–561, https://doi.org/10.17705/1CAIS.04843.

[37] G. Adomavicius, A. Gupta, M. Yang, Bidder support in multi-item multi-unit continuous combinatorial auctions: a unifying theoretical framework, Inf. Syst. Res. (2022), https://doi.org/10.1287/isre.2021.1068.

[38] G. Adomavicius, A. Gupta, M. Yang, Designing real-time feedback for bidders in homogeneous-item continuous combinatorial auctions, MIS Q. Manag. Inf. Syst. 43 (2019) 721–743. https://doi.org/10.25300/MISQ/2019/14974

[39] H. Pollack, R. Zeckhauser, Budgets as dynamic gatekeepers, Manag, Sci, 42 (1996 642–658. https://doi.org/10.1287/mnsc.42.5.642

Vivek Kumar Singh is an Assistant Professor of Information Systems and Technology in College of Business Administration at University of Missouri – St. Louis. He received his Ph. D. from the University of South Florida, Tampa, USA. His research focuses on applications of data mining techniques in security of cloud computing, healthcare analytics, and online learning. He has published articles in Computers in Human Behavior, Journal of th American Medical Informatics Association, Psychology and Marketing, and Psychological

Studies, and in premier Information Systems conference outlets including ICIS, AMCIS, and HICSS.

Shivendu Shivendu is an associate professor of information systems in the School of Information Systems and Management. University of South Florida. Tampa. FIL. He has created and taught undergraduate and graduate courses in economics of information systems, blockchain technology, FinTech, and IT strategy. He is the principal investigator on the prestigious White House initiated Federal TechHire grant of \$600,000. He is the coorganizer of the annual “State of the Region” conference held Tampa, an event that draws hundreds to learn more about how the region compares to other metropolitan areas in key areas such an unemployment, income inequality, economic growth and educational attainment. Shivendu’s research focuses on the emerging business and policy issues at the intersection of technology, economics and public policy. He employs analytical, empirical and experimental methods to study technology mediated business models, economics of digitization of information, pricing of digital goods including content pricing in dual mediums, sourcing of IT services, security and privacy in big data, business challenges of cloud adoption, health IT and technology policy. His work has been published in infor mation systems journals including Management Science, Information Systems Research, Journal of Management Information Systems, and Information Technology Management.

His research papers have won many bestpaper awards in conferences. He earned a PhD and a master’s degree in economics from University of Southern California, Los Angeles, an MBA from the Indian Institute of Management, Ahmedabad; and a bachelor’s degree in electrical engineering from the Indian Institute of Technology, Kanpur.

Kaushik Dutta has 22 vears of professional and research experience in the field of en terprise IT infrastructure, data analytics and big data systems. He is professor and chair of the School of Information Systems and Management. His current research interest is big data analytics. Dutta’s primary expertise combines operations research and data mining techniques with computer science systems knowledge to efficiently handle big data and manage large IT infrastructure. He has been the mentor of two startups out of USF in the NSFiCorps program. Prior to joining USF, Dutta was a tenured associate professor at Na tional University of Singapore and Florida International University. Before starting out on his academic path, he pursued a career in engineering, most recently as the chief tech nology officer and vice president of engineering of Mobilewalla, a NUS-incubated and Madrona-funded company that developed big-data-based mobile advertisement platforms. Dutta earned a PhD in management information systems from the Georgia Institute of Technology and a master’s degree in computer science from the Indian Statistical Institute. He received a bachelor’s degree in electrical engineering from Jadavpur University.
