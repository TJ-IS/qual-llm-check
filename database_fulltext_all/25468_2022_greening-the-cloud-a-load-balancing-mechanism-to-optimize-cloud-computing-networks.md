---
otero_id: 25468
otero_key: "NDTNC8EH"
title: "Greening the Cloud: A Load Balancing Mechanism to Optimize Cloud Computing Networks"
authors: "Chetan Kumar; Sean Marston; Ravi Sen; Amar Narisetty"
year: "2022"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2022.2063551"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Greening the Cloud: A Load Balancing Mechanism to Optimize Cloud Computing Networks

Chetan Kumar, Sean Marston, Ravi Sen & Amar Narisetty

To cite this article: Chetan Kumar, Sean Marston, Ravi Sen & Amar Narisetty (2022) Greening the Cloud: A Load Balancing Mechanism to Optimize Cloud Computing Networks, Journal of Management Information Systems, 39:2, 513-541, DOI: 10.1080/07421222.2022.2063551

To link to this article: https://doi.org/10.1080/07421222.2022.2063551

![](/api/attachments/NDTNC8EH/fulltext/images/8beaa611885a8515db29194080f59567acbfc31f55cf49ba1479cec6961705ab.jpg)

Published online: 07 Jun 2022.

![](/api/attachments/NDTNC8EH/fulltext/images/11895d6f23fce8da5a78b45a59061b880caafd1b4a56cfe54c6ae52fda64e0e9.jpg)

Submit your article to this journal

![](/api/attachments/NDTNC8EH/fulltext/images/5bcada342989c79ccf670e640c2aed5ae94af338189800162f671a6a4c53d585.jpg)

Article views: 175

![](/api/attachments/NDTNC8EH/fulltext/images/9593b8a9826f4196b3a510043563c3626a81f83aa2eabfaad9ffa14d33677c1f.jpg)

View related articles

![](/api/attachments/NDTNC8EH/fulltext/images/c9f62c6987014174c83b210b243705ed2fd0b7877641269013bf6fa8cb285e4d.jpg)

View Crossmark data

Check for updates

# Greening the Cloud: A Load Balancing Mechanism to Optimize Cloud Computing Networks

Chetan Kumar<sup>a</sup>, Sean Marston<sup>b</sup>, Ravi Sen<sup>c</sup>, and Amar Narisetty<sup>d</sup>

<sup>a</sup>Information Systems, College of Business Administration, California State University San Marcos, San Marcos, CA, USA; <sup>b</sup>Gordon Ford College of Business, Western Kentucky University, Bowling Green, KY, USA; <sup>c</sup>Mays Business School, Texas A&M University, College Station, TX, USA; <sup>d</sup>SAS Instititute Inc., Cary, NC, USA

## ABSTRACT

Approximately 55 percent of the world’s 7.3 billion people access the Internet, creating a significant demand in information technology (IT) services for both organizations and consumers. The number of data centers continue to increase to meet this demand, consuming 2 percent of the energy produced worldwide. Many organizations moving towards cloud computing due to its ability to meet users’ needs on demand. Greening cloud computing technology has become an important aspect of an organization’s design and use of cloud computing. One aspect of greening the cloud is through eficiently using cloud-based resources. In this study, we focus on the resource allocation applications of cloud computing technologies to green an organizations cloud. We design a pricing and allocation mechanism for a private cloud computing service that allows the firm to efectively load balance their cloud computing resources. Our optimal pricing mechanism is a dynamic pricing model, which maximizes the net value of users in a private cloud computing service. Additionally, we create a job allocation algorithm based on our dynamic pricing model to load balance the cloud. We show that balancing the job allocation such that the number of jobs at individual resource servers as close to equal as possible is optimal. Furthermore, simulations were run on the allocation mechanism to examine the efects on the cloud resources while gaining insight to efectively distribution resources to public clouds. Our model can help organizations to eficiently distribute their cloudbased resources, which allows for a greener cloud computing system.

Cloud computing; Green IT; load balancing; optimal allocation

## Introduction

The pervasiveness of computing technology and internet usage by stakeholders has created pressure on organizations to provide reliable Information Systems (IS). To meet these stakeholder needs, organizations have implemented the use of cloud computing in their Information Technology (IT) architecture. Cloud computing uses the capabilities of the Internet to permit access to remote resources, allowing information technology services, applications, and infrastructure to be scaled in an on-demand fashion. The capability of cloud computing architecture allows companies to eficiently use their own IT services and the IT services they deliver to their consumers [16, 24, 39].

The reliability and speed of the Internet has also led to an increased demand for Internet-based services. Video on demand, social networking, collaboration applications, and other Internet based services have exploded during the past few years. Most of these Internet based services are delivered using cloud computing services. In North America, real time entertainment accounts for 59 percent of the Internet trafic during the peak period, Netflix alone accounts for 31 percent of this trafic. Netflix provides its services to its consumers through the Amazon Web Services, which is one of the largest public cloud computing companies. Other large corporations are providing a significant number of services through the cloud. Microsoft provides its Xbox services through its Azure cloud, and Khan Academy’s educational services are provided using Googles cloud. Many companies are using private clouds to meet the needs of the organization while using public clouds to supplement their IS when required. Corporations have been moving several traditional applications to cloud based applications and transitioning their traditional data centers to a cloud paradigm [10, 26]. The Covid-19 pandemic has impacted this significantly. It has increased internet usage by 40 to 100 percent, video conference call technology usage increasing tenfold, and content delivery services having an increase in content usage of 30 percent [5]. This in turn has driven a need to have flexible information and scalable information systems, driving organizations to use cloud computing in there IT architecture. One issue that many companies are dealing with while transitioning is managing their private clouds in conjunction with the use of public clouds to manage their workloads to meet the needs of the company [12].

One important aspect of IT today is the attempt to make it more environmentally friendly, which is the basis for green computing. Green computing is the use of IT and IS to help firms reduce their environmental impact and increase overall sustainability. There are two aspects of green Computing: green IS encompasses “the design and implementation of information systems that contribute to sustainable business processes” [59] and green IT, which focuses on the eficient use of energy and equipment. Cloud computing can be used to improve each of these green computing aspects. Hugh et al. [22] examine the factors that positively influence a company’s adoption of Green IT, one of which is environmental awareness. 52. Subramanian et al. [52] has shown that small to medium size Chinese logistic service providers would benefit from green IS through the integration of cloud computing to optimize their business processes.

It is readily seen that a significant number of companies are moving toward cloud-based services. Walmart in 2018 created a strategic partnership with Microsoft to leverage the use of cloud solutions for enterprise-wide use [58]. This transition to cloud-based services has impacted both internal facing operations, such as supply chain management and in store refrigeration management, and external facing operations, such as online consumer shopping. Best Buy has entered a similar partnership with the Google cloud platform while Kroger has split its cloud usage between Azure and the Google cloud platform. Some companies have elected to use private clouds services. These include Hyatt Hotels Corporations and CBS Interactive which use the Amazon Virtual Private Cloud services that allow them to have an isolated instance of a private cloud with complete control over the instance allowing them to meet their needs [11]. Other companies have elected to have a hybrid cloud, using their own private cloud while expanded its use to a publicly accessible cloud when needed. Smithfield Foods is one such company, which partnered with Azure to implement a hybrid cloud. This allows Smithfield to keep all its sensitive data and applications on premise while giving them the flexibility to access the public cloud to handle any overflow when processing demands increase beyond the private cloud capacity [43].

Cloud computing has grown significantly in market size over the past decade, as of 2012 it was \$26 billion [7] and by the end of 2020 its expected value is \$371.4 billion. It is predicted to grow to \$832.1 billion by 2025 with a 17.5 percent compounded annual growth rate [9]. This growth has led to a significant increase in the global data center market. The increased investment in cloud computing is expected to grow the global data center market at compounded annual growth rate of 2 percent over the period of 2019-2025 [55]. While a significant number of data centers are in North America, the growth is expected to be worldwide.

In 2018, the United States data centers consumed 90 billion kilowatt hours of energy [12], creating approximately 97 million metric tons of carbon dioxide (CO2) emissions. By 2030 the data centers which power the internet are expected to consume 8 percent of the world’s electricity, a 15-fold increase from 2010 [2]. This increase in consumption is due, in large part, to the expanded use of cloud computing services. Cloud computing services help contribute to green IS through improving the usage of servers and resource allocations which improves system performance. The overall improvements of a cloud through increasing resource eficiencies reduce the cloud’s overall energy usage and CO2 footprint. Most cloud services fall into the category of being energy ineficient, consuming a significant amount of energy due to the low deployment level of virtualization and idle servers. While large public facing cloud computing services, such as the Amazon EC2 and the Microsoft Azure, have made moves to become relatively energy eficient, there is still room for improvement. The efective management of cloud resources will lead to a greener, more environmentally friendly cloud for all cloud sizes [28, 49].

This study focuses on the resource allocation applications of cloud computing technologies. The objective is to design a pricing and allocation mechanism for a private cloud computing service that allows the firm to efectively load balance their cloud computing resources. Our mechanism allows resource requests to be eficiently distributed to the available cloud resources in a decentralized manner. The mechanism being presented maybe be considered under diferent objective functions. Based on the need of an organization, the mechanism can be designed to maximize the net value of the private cloud services or minimize the delay cost of end users.

On the one hand, public cloud services are provided by third parties that own, operate, and manage the cloud infrastructure (e.g., Microsoft Azure). On the other hand, private cloud services are provided in-house by an organization and all related cloud infrastructure is owned, operated, and managed by the organization. Hybrid cloud services include a combination of public and private cloud services, that is some cloud services are take care of in-house while others are outsourced to a third-party cloud service provider. In this study, we modelled a private cloud service that can access a public cloud when the resources are fully allocated, in essence a hybrid cloud. Specifically, we look at the private cloud side of the hybrid, which is owned and operated by the customer, and not at the public cloud side, which will be used when the private clouds resources are fully allocated. This is similar to Smithfield foods’ hybrid cloud, controlling its own private cloud while using Microsoft Azure public cloud services to expand its resources when needed [43]. Our model would be beneficial to Smithfield food when setting their resource allocation policy for their private cloud. However, the results obtained in the study would apply to a public cloud service. In the public case, the third-party cloud service provider can use the insights obtained to price its services and optimize resource allocation. The limitation would be when the public cloud’s resources are fully allocated, the only option that they would have would be to expand their resources since the do not have access to a separate public cloud.

The case we characterize is an organization maximizing the load balancing of resources in their private cloud to optimize the resource usage. Our cloud balancing mechanism model builds on Kumar and Bandyopadhyay [31] and Kumar et al. [32] models for resource sharing in a peer-to-peer network environment. The model’s objective is appropriate for an organizational setting where the firm is interested in eficiently using the available resources, which will increase the eficiency of the cloud’s energy usage. The private cloud consists of multiple resource servers with the ability to create various virtualized environments; each resource server will have the capability of receiving multiple jobs. Figure 1 shows an example of a basic private cloud consisting of ten resource servers that can share computer resources.

Any cloud resource server can communicate with any other resource server in the cloud. When one resource server receives a job requesting resources, there is a possibility another resource server receives the allocation of the job allowing the cloud to pool its resources efectively. The firm owns and controls its private cloud, and its objective is to maximize the usage of the available resources. In addition to maximizing the usage of resources, we extend our mechanism to account for a maximum permissible queue length for each resource server. The queue length ensures a quality of service (QoS) for the firm’s private cloud by limiting the end users’ delay. We can then study the case, in which any resource server in the private cloud can outsource a job to a third party based on its own utilization level. The mechanism that we present is advantageous to organizations by allowing them to more efectively allocate their cloud resources.

![](/api/attachments/NDTNC8EH/fulltext/images/a82cd0759a1e108d872df7c13a1851ebe08311a58cea19fccd0cca17e70e9901.jpg)  
Figure 1. A private cloud network for sharing computing resources.

Our proposed cloud pricing mechanism is an implementation of dynamic pricing for a private cloud network. It should be noted that while there are alternative cloud pricing mechanisms, some form of dynamic pricing is widely incorporated by the major cloud providers such as Amazon AWS and Microsoft Azure [22]. Amazon, Walmart, and AliExpress are all known to use some form of dynamic pricing in their retail business. Popular models of dynamic pricing include:

● Cost-based model, which merge the profit with the level of Cost [19]

● Value-Based, which take into consideration the basis of user perceiving value [14]

● Competition-based, which take into consideration the competitor price of services [19]

● Customer-Based, which consider what the customer is prepared to pay [60]

● Location-Based, where price is set according to the customer location.

We posit that given the nature of cloud services; dynamic pricing is the way to go to make cloud computing more “green.” Our optimal pricing mechanism which maximizes the net value of users in a private cloud computing service is one such approach. Dynamic pricing model such ours can be considered an innovation of the cost-based model as it considers the expected delay cost of executing jobs for determining optimal pricing.

Our dynamic cloud pricing model in this study builds on extensive literature on dynamic pricing. The classic Mendelson [41] study was among the pioneering research to model a computer network as a congestible resource. Mendelson [41] derived the optimal pricing strategy for maximizing net value of users of a single computer network. Kumar and Bandyopadhyay [31] and Kumar et al. [30] generalized this model to formulate the pricing strategy for a network of computer servers where each node behaved as a peer to form a multi-server peer-to-peer network. MacKie-Mason and Varian [37] were among the first to propose a dynamic pricing model for the Internet. In this study we extend the ideas of Kumar et al. [30], MacKie and Varian [37], and Mendelson [41], among other studies [6, 19, 23, 34, 60] to formulate a dynamic pricing and allocation mechanism for a private cloud computing service that allows the firm to load balance their cloud computing resources efectively. While our model is a first cut attempt at this dynamic pricing approach for cloud computing, there are many interesting avenues for future research. For example, spot pricing for jobs on public clouds such as Amazon AWS, may be examined for pricing impact on cloud-based services. Alternative dynamic pricing models, such as cost-based, valuebased, and location-based, may also be compared versus our net value maximization approach [1, 19, 34, 60]. These topics are interesting areas to pursue for future research.

The rest of this paper is presented as follows. We first discuss the literature related to our study, followed by the formulation and analysis of the model. We then discuss our findings from numerical simulations. Finally, we present our conclusions and discuss diferent directions for future research.

## Related Literature

The greening of IT has become an important aspect in our data-centric world due to the increasingly large environmental impact of the Internet typically unseen by traditional users. Cloud computing plays an important role in reducing this impact due to its ability to scale and make resources available as needed. Organizations are moving toward the use of their own private clouds to run the IT services they require and those that they provide to consumers. Additionally, many organizations are attempting to green these services through the reduction of energy consumption, use of renewable energy resources, recycling equipment at the end of their lives, and recycling disposable waste. Examples include Google<sup>1</sup> and Microsoft’s,<sup>2</sup> two of the biggest cloud service provider sustainability initiatives. Two important ways companies are reducing energy consumption is through the decrease in the total amount of resources needed and the eficient utilization of the available resources. Reducing the number of resources needed decreases the overall energy consumption of the cloud while improving the allocation of cloud resources, which in turn improves the cloud’s energy eficiency.

The purpose of Green Cloud Computing is to reduce the power consumption of the data center while ensuring the QoS from the customer point of view [40]. With a cloud computing resource planning policy, providers can improve the allocation of resources in a cloud computing environment such that it will reduce processing cost and time, energy usage and overall environmental impact [35]. The purpose of our model is to eficiently allocate resources throughout the cloud, minimizing the need for excess processing usage and allowing for the eficient design of the cloud. By optimal we mean our model develops a mechanism that aims to reduce overall waiting times for all users in the network by utilizing a net value maximization approach. Our load balancing mechanism has important benefits as related to green IT because (1) it allows us to optimize the size and requirements of the cloud so we do not have excess unutilized capacity (2) we can optimize machines usage which would in turn we minimize energy costs. [47] shows that the more eficient use of equipment reduces the overall infrastructure needed while reducing the overall use of energy usage. Additionally, the optimization of machines will lower the amount of e-waste produced in the cloud environment. These two aspects of a green cloud will reduce the company’s carbon footprint.

It has been shown that approximately 90 percent of a data center’s energy expenditures come from the use of its equipment [53]. One stream of research has been the creation of eficient processors. Processors are being designed to reduce power usage through reducing clock speed, dynamic voltage scaling (DVS), or shutting of portions of the processor that are not in use. The use of DVS can lead to the reduction in the cost of power used by the processor at the cost of the speed of a program’s execution [4]. The scheduling of tasks on multiple cores processors has been examined to reduce energy consumed by processors. Zhu et al. [62] discusses a technique that reduces processor power usage through throttling the execution speed of tasks with slack time.

Green computing and the increasing cost of electricity has led to the importance of power management in data centers, and it is shown that eficient allocation of resources play a role in energy eficiency of a cloud [36]. Hameed et al. [20] survey studies on improving energy eficiency in allocating cloud resources, and Gawali and Shinde [17] provide a good summary of recent works on task scheduling and resource allocation in the context of cloud computing. While varied degrees of success have been reported in subsequent studies, energy eficient resource allocation in cloud networks has many open challenges [8, 38, 54]. Kumar et al. [33] review various resource scheduling for better resource management in clouds while also touting the need for the further development of scheduling techniques.

Our proposed optimal cloud load balancing mechanism addresses the key issues of allocation method and resource adoption policy in cloud computing research. While there is a large body of work on task scheduling and resource allocation in a networked environment and specifically in the context of cloud services, all these studies tend focus on the eficiency [40], performance, and resource optimization [20, 36]. Our work builds upon this foundation by bringing in pricing of cloud services and how they can be used to optimize resource allocation to minimize any adverse impact that cloud infrastructure has on the environment. It is estimated that almost 1 percent of all energy demand in 2021 is used by cloud computing and it is expected to grow at an exponential rate [45], contributing to 0.3 percent of all global carbon emissions [15]. Optimizing resources allocation to minimize energy consumption will play a key role in helping reduce cloud computing overall environmental impact.

Virtualization plays a key role in managing the workload of cloud resources, helping make the cloud more efective, eficient, and scalable [46]. One area of virtualization research examines virtualization’s role to reduce energy consumption by data centers and cloud computing [29]. Deploying virtual machines can lead to energy savings; however, if done in a poor manner it can lead to increased energy consumption. The reconfiguration of virtual machines to self-allocate the resources needed for each job, as it is being handled in combination with controlling the power state of the CPS, can be used to increase energy eficiency [44]. Blind consolidation of virtual machines leads to energy ineficiency but using workload aware consolidation techniques to manage virtual machines also reduces energy consumption [27]. Beloglazov and Buyya [3] proposed a resource management policy of virtualized data centers and showed it provided a substantial energy saving. Sharifi et al. [50] examines how the combination of multicore architecture in conjunction with virtualization can improve a clouds energy eficiency and help overcome the clouds energy wastage.

Data transportation across networks within a data center plays a role in the energy consumption of data centers. In the past, researchers have suggested that the impact of energy usage of networks is not relevant since components use the same amount of energy regardless of the amount of data transported [21]. However, energy eficient components with networks that can adapt bandwidth based on need and the ability to switch of components when not needed allow for energy savings in data centers [57]. It has been shown that the data transport during the migrating virtual machines does play an important role in energy consumption [51].

Managing the workload of a cloud through load balancing has become an important issue in cloud computing [48]. Efective load balancing allows for the eficient allocation of the workload across the cloud helps in QoS enhancements such as reliability, productivity, resources utilization, and energy consumption [42]. This in turn allows for the cloud to scale up and meet the demands of its consumers [1]. When load balancing is done in an appropriate manner, it can reduce the overall resource consumption of the cloud, which in turn can help make the cloud greener [56]. Honeybee forging behavior and biased random sampling and active clustering are two of many load balancing techniques that have been proposed to efectively allocate recourses. Kumar and Marston [32] review various data driven approaches to efectively manage computer proxy networks’ load thereby reducing energy consumption. Each of the proposed algorithms come with a diferent set of advantages and disadvantages but each does create a greener system [25, 26, 27, 61]. A summary of this relevant literature is provided in Table 1.

Table 1. Existing research on managing resource consumption by cloud services.

<table><tr><td>Focus</td><td>Research</td><td>Example</td></tr><tr><td rowspan="3">Hardware and Equipment used to provide cloud services</td><td>Design and creation of energy efficient processors</td><td>[31]</td></tr><tr><td>Task Scheduling among multiple processors to reduce power consumption</td><td>[30]</td></tr><tr><td>Power management</td><td>[33]</td></tr><tr><td rowspan="2">Virtualization</td><td>Virtualization plays a key role in managing the workload of cloud resources</td><td>[39]</td></tr><tr><td>One area of virtualization research examines virtualization&#x27;s role to reduce energy consumption by data centers and cloud computing</td><td>[40-44]</td></tr><tr><td rowspan="2">Network Traffic</td><td>Data transportation across networks within a data center plays a role in the energy consumption of data centers.</td><td>[45-47]</td></tr><tr><td>Review of algorithms to reducing energy consumption by networks.</td><td>[52-54]</td></tr><tr><td rowspan="5">Task scheduling and resource allocation</td><td>Importance of load balancing in cloud computing</td><td>[48]</td></tr><tr><td>Effective load balancing for efficient allocation of the workload across the cloud</td><td>[49, 50]</td></tr><tr><td>Load balancing to reduce the overall resource consumption of the cloud, which in turn can help make the cloud greener</td><td>[51]</td></tr><tr><td>Survey of literature on task scheduling and resource allocation</td><td>[38, 57]</td></tr><tr><td>Survey of studies on improving energy efficiency in allocating cloud resources</td><td>[34-37]</td></tr></table>

Our model builds on the classical dynamic network pricing models first utilized by Mendelson [41] for a single server environment and then applied by Kumar and Bandyopadhyay [31] and Kumar et al. [30] for pricing in a multi-server peer to peer computer network. We combined multi-server dynamic pricing in a new cloud computing setting extending Kumar and Bandyopadhyay [31] and Kumar et al. [30], creating a decentralized dynamic pricing model for a large-scale cloud computing environment. Through this extension we examine large scale network interaction efects, pricing, and congestion pricing, and QoS guarantees/private public cloud outsourcing issues for cloud computing. Therefore, our model is a large-scale multi-server generalization of the simpler Kumar and Bandyopadhyay [31] and Kumar et al. [30] peer-to-peer pricing model. In addition, we demonstrate the practical efects of pricing and congestion in a cloud computing environment by building a load balancing algorithm based on our analytical model. Our simulation results provide insights into the real world efects of pricing and congestion in a large scale cloud computing environment.

## Model

Our proposed cloud computing load balancing mechanism models the steady state behavior of a cloud. Our model expands on the Kumar and Bandyopadhyay [31] and Kumar et al. [30] models, in which a pricing and allocation mechanism was developed for a multi-server peer-to-peer (P2P) network where the users in a firm may share their computing resources. This model demonstrated that the net value of users in a peer-to-peer computer network is maximized when jobs are equally allocated. We apply this model to a private cloud environment. Building on this model, we examine the impact of job allocation in queue length constrained cloud environment on the cloud’s eficiency. The following two sub sections details the application of our multi-server dynamic pricing model for cloud computing. In the first section, we extend Kumar and Bandyopadhyay [31] and Kumar et al. [30] creating a decentralized dynamic pricing model for a large-scale cloud computing environment. In the next section, we demonstrate the practical efects of pricing and congestion in a cloud computing environment by building a load balancing mechanism based on our analytical model. Finally, we construct a job balancing algorithm for cloud computing, which is later used to perform large scale simulations.

## Model Review

We review and apply the Kumar et al. [30] model to our proposed cloud computing mechanism as follows. The cloud computing system we model contains resource servers that receive jobs requesting the use of resources that arrive at a fixed exogenous rate. The pricing scheme is based on an individual user deciding to use the resource of the cloud based on the transfer price posted. When a job arrives at a resource server, it will either receive access to the resources or be assigned to another cloud resource server in the network. The model is designed as follows: A resource server is represented by j and i is a directly connected resource servers. Any job arriving at resource server j has an efective arrival rate of $\lambda _ { i j }$ , this is also the total allocation of jobs at resource server j in the cloud. A job originating at i with an arrival rate of $\varGamma _ { i j }$ that is executed at resource server j has an expected arrival rate of $\begin{array} { r } { T _ { j } = \sum _ { i } \lambda _ { i j } } \end{array}$ , it is assumed that this total allocation follows a Poison process. The efective arrival rate of resource sever j includes the jobs which have originally arrived and are executed at resource server j. The resource server at which a job is executed is decided by the number of jobs within the cloud computing system regardless of where the job originates. All notations used in the model and their definitions can be seen in Table 2.

Figure 2 demonstrates a simple lay out of five resource servers with resources to allocate in a cloud environment. The five resource servers located at $i , j , k , l ,$ and m are neighbors to each other. The solid lines with arrows represent jobs that arrive exogenously at each resource servers: $\lambda _ { i } \ : , \ : \lambda _ { j } \ : , \ : \lambda _ { k } \ : , \ : \lambda _ { l }$ , and $\lambda _ { m }$ . The dashed lines with arrows represent the jobs that are redistributed to resource server j and $\begin{array} { r } { T _ { j } = \sum _ { i } \lambda _ { i j } : \lambda _ { j i } , \lambda _ { k i } , \lambda _ { l i } } \end{array}$ , and $\lambda _ { m i }$ . The model’s objective is to obtain the optimal $\begin{array} { r } { T _ { j } = \sum _ { i } \lambda _ { i j } ^ { * } } \end{array}$

For simplicity, as a first cut of our cloud balancing mechanism we assume the individual jobs are of the same size. However, it is to be noted in our model the optimal transfer price is based on every resource server in the cloud maximizing its expected net value. The net value is characterized as the diference between the expected gross value of (all) the jobs and the expected delay cost. Therefore, even if each job is of diferent amount, the expected gross value already takes these into account. Another way to look at this approach is that our unit of analysis is all jobs assigned to resources instead of each separate job assigned to it. Additionally, our equal allocation optimal pricing scheme is applicable to a fully connected network structure as seen in Figure 1 and Figure 2. Future extensions to our model may also consider diferent job sizes in addition to difering unit job arrival rates to capture this practical cloud computing scenario. Furthermore, an investigation into optimal pricing for a network structure that is that is not directly connected which include resource servers that have one or more hops to connect to resource services.

Table 2. Notations.

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $j$ </td><td>server location</td></tr><tr><td> $i, k$ </td><td>&#x27;direct neighbor&#x27; locations of  $j$ </td></tr><tr><td> $\lambda_j$ </td><td>exogenous arrival rate of a jobs at  $j$ </td></tr><tr><td> $\lambda_{ij}$ </td><td>arrival rate of a job originating at  $i$  to be executed at  $j$ </td></tr><tr><td> $\Gamma_j = \sum_i \lambda_{ij}/\Gamma_j^* = \sum_i \lambda_{ij}^*$ </td><td>total/optimal total arrival rate of jobs at server  $j$ </td></tr><tr><td> $\Lambda(\Gamma_j)$ </td><td>gross value gained by system users at  $j$  when the arrival rate is  $\Gamma_j$ </td></tr><tr><td> $W_j(\Gamma_j)$  or  $W_j$ </td><td>expected time a job spends at  $j$  when the arrival rate is  $\Gamma_j$ </td></tr><tr><td> $L_j(\Gamma_j)$  or  $L_j$ </td><td>expected job queue length at  $j$  when the arrival rate is  $\Gamma_j$ </td></tr><tr><td> $v$ </td><td>delay cost per-unit time for any job</td></tr><tr><td> $p_j/p_j^*$ </td><td>price/optimal price for executing a job at node  $j$ </td></tr><tr><td> $\partial W_j/\partial \Gamma_j/\partial W_j/\partial \Gamma_j^*$ </td><td>incremental delay added to  $W_j$  due to an incremental arrival  $\Gamma_j / \Gamma_j^*$ </td></tr><tr><td> $\partial L_j/\partial \Gamma_j$ </td><td>incremental increase in queue length  $L_j$  due to an incremental arrival  $\Gamma_j$ </td></tr><tr><td> $\mu_j$ </td><td>job processing capacity at  $j$ </td></tr><tr><td> $\partial p_j^*/\partial \lambda_{ij}$ </td><td>first order effect, marginal change in price at  $j$  due to marginal arrival  $\lambda_{ij}$  from  $i \neq j$ </td></tr><tr><td> $\partial^2 p_j^*/\partial \lambda_{ij} \partial \lambda_{kj}$ </td><td>second order interaction effect, change in marginal price at  $j$  due to marginal arrivals  $\lambda_{kj}$  and  $\lambda_{ij}$  from neighbor locations  $k \neq i \neq j$ </td></tr><tr><td> $q$ </td><td>maximum permissible queue length</td></tr><tr><td> $\beta_j$ </td><td>Lagrange multiplier</td></tr><tr><td> $M = \sum_j \lambda_j/N$ </td><td>number of jobs executed at any node $j$ </td></tr><tr><td> $N$ </td><td>total number of direct neighbors in the P2P network</td></tr><tr><td> $j'$ </td><td>a node that has job allocations  $\Gamma_{j'} >M$  jobs</td></tr><tr><td> $j''$ </td><td>another node that has job allocations  $\Gamma_{j''} < M$  jobs</td></tr><tr><td> $p_{j'} = v\Gamma_j' (\partial W_{j'}/\partial \Gamma_{j'})$ </td><td>job execution price at  $j'$ </td></tr><tr><td> $p_{j''} = v\Gamma_{j''} (\partial W_{j''}/\partial \Gamma_{j''})$ </td><td>job execution price at  $j''$ </td></tr><tr><td> $\Delta_j'$ </td><td>increased job allocations at  $j'$  where  $\Gamma_{j'} = M + \Delta_{j'}$ </td></tr><tr><td> $\Delta_{j''}$ </td><td>reduced job allocations at  $j''$  where  $\Gamma_{j''} = M - \Delta_{j''}$ </td></tr><tr><td> $\Lambda(\Gamma_{j'})$  and  $W_{j'}$ </td><td>gross value of executing jobs and expected waiting time at  $j'$ </td></tr><tr><td> $\Lambda(\Gamma_{j''})$  and  $W_{j''}$ </td><td>gross value of executing jobs and expected waiting time at  $j''$ </td></tr><tr><td> $\Lambda(\Gamma_j^*)$  and  $W_j^*$ </td><td>gross value of executing jobs and expected waiting time when jobs are equally allocated at  $\Gamma_j^* = M$  jobs per node  $j$  and the nodes have an identical execution price  $p_j^* = v\Gamma_j^*(\partial W_j/\partial \Gamma_j^*)$ </td></tr></table>

Note: Adapted from Hameed et al. [20].

The optimal transfer price is based on every resource server in the cloud maximizing its expected net value. The net value is characterized as the diference between the expected gross value of the jobs and the expected delay cost. A user’s job can be executed at every resource server i that originated at resource server $j .$ The net value maximization given a fixed capacity is:

$\left\{ \boldsymbol { A } \left( \boldsymbol { I } _ { j } \right) - \nu \boldsymbol { L } _ { j } \left( \boldsymbol { I } _ { j } \right) \right\}$ The Net-Value Maximization Problem.

This leads to the optimal job execution price:

(1)

$$
p _ {j} ^ {*} = \nu \Gamma_ {j} ^ {*} \left(\frac {\partial W _ {j}}{\partial \Gamma_ {j} ^ {*}}\right).\tag{2}
$$

![](/api/attachments/NDTNC8EH/fulltext/images/7965bbdc59b1b46a9b5e9cb3111c97b0bf323fd3dce2d87bbf006182ddc20a11.jpg)  
Figure 2. A simple example of a Cloud environment with five server locations.

as seen in Kumar et al. [30]. The optimal price is equal to the expected delay cost per unit time inflicted on the Cloud by a minuscule increase in job flow. Thus, the optimal job execution price is equivalent to the marginal delay cost imposed on the all the jobs in the cloud by the job, which allows every resource server j has its own optimal job execution price.

For any given resource server $j ,$ the capacity $\mu _ { j }$ and the job arrival rate $T _ { j }$ can be used to express the optimal price. The waiting time is for a job at resource server j given by:

$$
W _ {j} = \frac {1}{\left(\mu_ {j} - \Gamma_ {j}\right)}.\tag{3}
$$

It should be noted that as the job arrival rate $T _ { j }$ approaches the capacity $\mu _ { j }$ , the waiting time $W _ { j }$ tends to infinity. Note that there is a non-linear efect on the waiting time $W _ { j }$ as job arrival rate $T _ { j }$ approaches capacity $\mu _ { j }$ . Given this non-linear relationship, we would expect to see any pricing function for executing jobs at a given cloud server to also have a nonlinear or exponential relationship to job arrival rate as it approaches server capacity. We explore this point in the Simulation section later in this study. To avoid an infinite delay for jobs in the cloud, $\mu _ { j } > T _ { j }$ . Diferentiating the waiting time $W _ { j }$ with respect to $T _ { j }$ gives:

$$
\frac {\partial W _ {j}}{\partial \Gamma_ {j}} = \frac {1}{\left(\mu_ {j} - \Gamma_ {j}\right) ^ {2}}.\tag{4}
$$

The expression for the optimal price can be rewritten by substituting Equation (4) in Equation (2) and replacing $T _ { j }$ with ${ \cal T } _ { j } = \sum _ { i } \lambda _ { i j } ^ { * }$ giving us:

$$
P _ {j} ^ {*} = \nu \left(\sum_ {i} \lambda_ {i j} ^ {*}\right) \left[ \frac {1}{\left(\mu_ {j} - \sum_ {i} \lambda_ {i j} ^ {*}\right) ^ {2}} \right]\tag{5}
$$

Based on the optimal price expression, we infer that price $\boldsymbol { p } _ { j } ^ { * }$ approaches infinity since the efective arrival rate $\sum _ { i } \lambda _ { i j } ^ { * }$ at j approaches the capacity $\mu _ { j }$ , the denominator in $\boldsymbol { p } _ { j } ^ { * }$ approaches zero. The non-linear nature of $\frac { \partial W _ { j } } { \partial T _ { j } }$ in Equation (2) is captured by $\displaystyle \frac { 1 } { \left( \mu _ { j } { - } T _ { j } \right) ^ { 2 } }$ in Equation (5). For any $i { \neq } j$ the aggregate efect on price due to the efective arrival rate is $\sum _ { i } \lambda _ { i j } ^ { * } , j$ , it may be compared to that of the marginal efect on price due to a marginal arrival $\lambda _ { i j } ^ { * }$ from any i. Our cloud resource allocation queues consist of job arrivals from multiple sources, thus the interaction efects of job arrivals from diferent sources impact the price of executing a job at any neighbor location. A maximum permissible queue length constraint is imposed on resource servers within the cloud in our model. Imposing a queue length creates a minimum QoS guarantee through limiting job delays. This in turn gives us the ability to model a cloud that can “outsource” a job to a separate cloud when the clouds resource utilization level reaches a specified point. One key reason to model the QoS is that a business operating a cloud can guarantee a minimum level of service to is users. It is very common for cloud service providers such as Amazon or Google to ofer access to a cloud with a specified limit on the wait time of a customer. The same can hold true for private cloud providers that may need to access a public cloud to ensure a minimum level of service.

In a cloud, the resource servers’ objective is to maximize its net value while constrained by the maximum queue length. The queue length is set to a value no more than a specific exogenous value, $q$ . The optimization problem subject to the queue constraint is:

$\left\{ { \cal { A } } \left( { { T } _ { j } } \right) - \nu { { L } _ { j } } \left( { { T } _ { j } } \right) \right\}$ The Constrained Queue Length Problem

(6)

$$
s. t. q - L _ {j} \geq 0.\tag{7}
$$

The constraint (7) is a binding constraint if the queue length, $q$ , is no more than the optimal solution of equation (1). To solve the constrained queue length problem, we can relax the constraint (7) using the Lagrangean relaxation. We add a relaxed constraint to the objective function while setting the Lagrange multiplier asn o $\beta _ { j }$ . The Legrangean relaxed problem is: $\left\{ \Lambda \big ( T _ { j } \big ) - \nu L _ { j } \big ( T _ { j } \big ) + \beta _ { j } \big ( q - L _ { j } \big ( T _ { j } \big ) \big ) \right\}$ The Lagrangean Relaxation Restated Problem (8)

$$
s. t. \beta_ {j} \geq 0.\tag{9}
$$

The restated relaxed problem is solved analytically through observing queue lengths constraints on the optimal service price as shown in Hameed et al. [20].

$$
\begin{array}{l}p _ {j} ^ {*} = \left\{ \right.\left(\nu + \beta_ {j}\right)\left[ \Gamma_ {j} ^ {*} \left(\frac {1}{\left(\mu_ {j} - \Gamma_ {j} ^ {*}\right) ^ {2}}\right)\right] + \beta_ {j} \left[ \frac {1}{\left(\mu_ {j} - \Gamma_ {j} ^ {*}\right)} \right] \text {   if   } \Gamma_ {j} W _ {j} (\Gamma_ {j})\\\leq q, a n d \infty i f \Gamma_ {j} W _ {j} (\Gamma_ {j}) > q\end{array}\tag{10}
$$

where

$$
\Gamma_ {j} ^ {*} \leq \left[ \frac {q}{(q + 1)} \right] \mu_ {j}.\tag{11}
$$

It is shown that when an exogenous constraint is imposed on the maximum permissible queue length ðqÞ on the cloud resource servers that it improves the overall QoS through a decrease in the overall waiting time. The queue length constraint increases the waiting time penalty for jobs, which decreases waiting times and allows managers to set the level of QoS through varying q .

## Cloud Load Balancing Mechanism

Building on the aforementioned model characterization adapted from Hameed et al. [20], we now prove that the total waiting time in a cloud with multiple resource servers is minimized when jobs are equally allocated, as shown in the following equal allocations proof.

Proposition 1 (The equal allocation waiting time minimization proposition.): When there is an equal allocation of jobs between all cloud resource servers the overall total waiting time is minimized.

## Proof

Expanding upon the Globe News Wire [55] and Andrae and Edler [2] models, we first look at the case where there are two nodes, j<sup>0</sup> andj<sup>0</sup>, in the cloud with unequal job allocations. The capacity of resource server j is j with $\mu _ { j } = \mu$ being randomly generate such that $\mu > T _ { j }$ . When jobs are allocated equally, we let $\begin{array} { r } { M = \sum \frac { \lambda _ { j } } { N } } \end{array}$ , the number of jobs allocated to node j . At node $j ^ { \prime }$ when the job arrival rate is greater than M, $T _ { j ^ { \prime } } { > } M$ , the price $\mathbf { \nabla } ^ { p _ { j ^ { \prime } } }$ is:

$$
p _ {j ^ {\prime}} = \nu \Gamma_ {j} \left(\frac {\partial W _ {j ^ {\prime}}}{\partial \Gamma_ {j ^ {\prime}}}\right).\tag{12}
$$

Diferentiating the waiting time with respect to $T _ { j ^ { \prime } }$ gives us:

$$
\frac {\partial W _ {j ^ {\prime}}}{\partial \Gamma_ {j ^ {\prime}}} = \frac {1}{(\mu - \Gamma_ {j ^ {\prime}}) ^ {2}}.\tag{13}
$$

We substitute equation (13) into Equation (12) and show that.<sup>.</sup>

$$
p _ {j ^ {\prime}} = \nu \Gamma_ {j} \left(\frac {1}{\left(\mu - \Gamma_ {j ^ {\prime}}\right) ^ {2}}\right).\tag{14}
$$

Additionally, the total allocation of jobs at node $j ^ { \prime }$ , $T _ { j ^ { \prime } }$ , is equal to job allocation during equal allocations, M , plus the increased allocations at node $j ^ { \prime } , \varDelta _ { j ^ { \prime } }$ :

$$
\Gamma_ {j ^ {\prime}} = M + \Delta_ {j ^ {\prime}}.\tag{15}
$$

We now solve for the diference in marginal waiting at node $j ^ { \prime }$ when compared to the marginal waiting during optimal job allocations.

$$
\frac {\partial W _ {j ^ {\prime}}}{\partial \Gamma_ {j ^ {\prime}}} - \frac {\partial W _ {j}}{\partial \Gamma_ {j ^ {*}}} = \frac {1}{(\mu - (M + \Delta_ {j ^ {\prime}})) ^ {2} -} \frac {1}{(\mu - M) ^ {2}}.\tag{16}
$$

While at node $j ^ { \prime \prime }$ , the arrival rate is less than M, $I _ { j ^ { \prime \prime } } < M$

In a similar fashion, we solve node $j ^ { \prime \prime }$ when the job arrival rate is less than M, $I _ { j ^ { \prime \prime } } < M$ , the price $\mathit { p } _ { j ^ { \prime \prime } }$ is:

$$
p _ {j ^ {\prime \prime}} = \nu \Gamma_ {j} \left(\frac {\partial W _ {j ^ {\prime \prime}}}{\partial \Gamma_ {j ^ {\prime \prime}}}\right).\tag{17}
$$

The total allocations at node $j ^ { \prime \prime }$ with the decrease in allocation, $\varDelta { { _ { j ^ { \prime \prime } } } }$ , is:

$$
\Gamma_ {j ^ {\prime \prime}} = M - \Delta_ {j ^ {\prime \prime}}\tag{18}
$$

Solving for the diference in marginal waiting time gives us:

$$
\frac {\partial W _ {j}}{\partial \Gamma_ {j ^ {*}}} - \frac {\partial W _ {j ^ {\prime \prime}}}{\partial \Gamma_ {j ^ {\prime \prime}}} = \frac {1}{(\mu - M) ^ {2} -} \frac {1}{\left(\mu - \left(M + \Delta_ {j ^ {\prime \prime}}\right)\right) ^ {2}}.\tag{19}
$$

We now examine the diference in marginal waiting time for unequal allocation compared to equal allocation by subtracting Equation (16) from Equation (19).

$$
\frac {1}{\left(\mu - \left(M + \Delta_ {j ^ {\prime}}\right)\right) ^ {2} + \frac {1}{\left(\mu - \left(M - \Delta_ {j ^ {\prime \prime}}\right)\right) ^ {2}} - \frac {2}{(\mu - M) ^ {2}}}.\tag{20}
$$

This leads to three following cases to be examined: Case $1 ; \varDelta _ { j ^ { \prime } } > \varDelta _ { j ^ { \prime \prime } }$ , Case 2: $\varDelta _ { j ^ { \prime } } < \varDelta _ { j ^ { \prime \prime } }$ , and Case 3: $\varDelta _ { j ^ { \prime } } = \varDelta _ { j ^ { \prime \prime } } = \varDelta _ { j }$ . However, since Case1: $\varDelta _ { j ^ { \prime } } > \varDelta _ { j ^ { \prime \prime } }$ and Case2: $\varDelta _ { j ^ { \prime } } < \varDelta _ { j ^ { \prime \prime } }$ are the same with $j ^ { \prime }$ and $j ^ { \prime \prime }$ in reverse order, only Case 1 and Case 3 needs to be examined.

Case 1: $\varDelta _ { j ^ { \prime } } > \varDelta _ { j ^ { \prime \prime } }$

Substituting in Equation (20), we arrive at

$$
\frac {1}{\left(\mu - \left(M + \Delta_ {j ^ {\prime}}\right)\right) ^ {2} - \frac {1}{(\mu - M) ^ {2}} -} \left[ \frac {1}{(\mu - M) ^ {2}} - \frac {1}{\left(\mu - \left(M - \Delta_ {j ^ {\prime \prime}}\right)\right) ^ {2}} \right].\tag{21}
$$

We know $\frac { 1 } { \left( \mu { - } \left( M { + } { \varDelta } _ { j ^ { \prime } } \right) \right) ^ { 2 } > } \frac { 1 } { \left( \mu { - } \left( M { - } { \varDelta } _ { j ^ { \prime \prime } } \right) \right) ^ { 2 } }$ , since $\frac { 1 } { \left( \mu - \left( M + \Delta _ { j ^ { \prime } } \right) \right) ^ { 2 } }$ is an exponential function where $\frac { 1 } { \left( \mu - \left( M + \Delta _ { j ^ { \prime } } \right) \right) ^ { 2 } } \longrightarrow \infty$ as $\mu - ( M + \Delta _ { j ^ { \prime } } )  0$ with increasing $\mu - ( M + \Delta _ { j ^ { \prime } } )  0$

Substituting this into Equation (21), we confirm $( 2 1 ) > 0$

Therefore, we demonstrate there in a net increase in waiting times for this case where $\varDelta _ { j ^ { \prime } } > \varDelta _ { j ^ { \prime \prime } }$

Case 3: $\varDelta _ { j ^ { \prime } } = \varDelta _ { j ^ { \prime \prime } } = \varDelta _ { j }$

Substituting in Equation (20), we arrive at

$$
\frac {1}{(\mu - (M + \Delta_ {j})) ^ {2} - \frac {1}{(\mu - M) ^ {2}} -} \left[ \frac {1}{(\mu - M) ^ {2}} - \frac {1}{(\mu - (M - \Delta_ {j})) ^ {2}} \right].\tag{22}
$$

We know $\frac { 1 } { \left( \mu - \left( M + \Delta _ { j } \right) \right) ^ { 2 } > } \frac { 1 } { \left( \mu - \left( M - \Delta _ { j } \right) \right) ^ { 2 } }$ , since $\frac { 1 } { \left( \mu - \left( M + \Delta _ { j } \right) \right) ^ { 2 } }$ is an exponential function where ${ \frac { 1 } { \left( \mu - \left( M + \Delta _ { j } \right) \right) ^ { 2 } } } \longrightarrow \infty \mathrm { ~ a s ~ } \mu - \left( M + \Delta _ { j } \right) \longrightarrow 0$ with increasing $\varDelta _ { j }$ . Substituting for this in to Equation (22), we confirm $\varDelta _ { j }$ . Therefore, we demonstrate there in a net increase in waiting times for this case where $\varDelta _ { j ^ { \prime } } = \varDelta _ { j ^ { \prime \prime } } = \varDelta _ { j }$

For both Cases 1 and 3, we confirm that there is a net increase in waiting times as Equations (21) and (22) are >0, respectively.

Consequently, the net diference in marginal waiting time in Equation (20) for unequal allocation $T _ { j ^ { \prime } } = M + \varDelta _ { j ^ { \prime \prime } }$ and $T _ { j ^ { \prime \prime } } = M + \varDelta _ { j ^ { \prime \prime } }$ versus equal allocation $T _ { j ^ { * } } = M$ is always positiv ${ \mathrm { : } } > 0 ,$ as $\frac { \partial W _ { j ^ { \prime } } } { \partial T _ { j ^ { \prime } } } - \frac { \partial W _ { j } } { \partial T _ { j ^ { * } } } > \frac { \partial W _ { j } } { \partial T _ { j ^ { * } } } - \frac { \partial W _ { j ^ { \prime \prime } } } { \partial T _ { j ^ { \prime \prime } } }$ .Therefore, we prove that there is a net increase in waiting times due to unequal allocations, ${ \cal T } _ { j ^ { \prime } } > { \cal M }$ and ${ T _ { j ^ { \prime \prime } } } < M$ ; compared to equal allocations $\begin{array} { r } { T _ { j ^ { * } } = M = \sum _ { N } ^ { \lambda _ { j } } } \end{array}$ . Thus, waiting times due to equal allocations $\begin{array} { r } { T _ { j ^ { * } } = M = \sum \frac { \lambda _ { j } } { N } } \end{array}$ is minimized when compared to unequal allocations, ${ \cal T } _ { j ^ { \prime } } > { \cal M }$ and $I _ { j ^ { \prime \prime } } < M$

## Job Allocation Algorithm

Based on the findings in Proposition 1, we created a job allocation algorithm that is used to simulate the optimal cloud load balancing mechanism. The job allocation algorithm is as follows:

Steps:

(1) Each cloud resource server receives INT (total jobs/N) (INT refers to the Integer function) number of jobs, where N is the total number of cloud resource servers, ensuring queue length constraints are not violated at each resource server

(2) Check if (total jobs MOD N = 0) (MOD refers to the Modulo function)

(3) If (total jobs MOD N = 0), then every cloud resource receives total jobs/ N allocated jobs or their individual queue length constraint q number of jobs, whichever is less

(4) If (total jobs MOD $N \neq O )$ , then resource servers are randomly allocated excess jobs in cyclical order of the resource servers, while not violating their individual queue length constraints q

(5) Calculate job allocations $\begin{array} { r } { T _ { i } = \sum _ { i } \lambda _ { i j } } \end{array}$ for any resource serverj, where i is a neighbor location toj, using Steps 1 through 4.

## Simulations

We performed simulations for our optimal cloud load balancing mechanism to illustrate the impact of job arrivals on prices and load allocations at the individual cloud resource servers. We consider a simple cloud network structure of ten resource server locations as seen in Figure 1, with the resource servers referred to as 1 through 10. We simulate the job arrival rates at each of the resource server locations using a Poisson process and randomly generate the mean Poisson arrival rates for each resource server in the range of 5 to 15. The unit delay cost, v, for each job is set as 5 and is consistent for all users. Each resource server has fixed capacities of 20 and a queue length randomly generated within a range of 15 to 20. The range of values utilized for generating these parameters are summarized in Table 3 and the final generated numbers are summarized in Table 4. This framework models the case of a cloud network that is receiving jobs at resource servers requesting virtualized machines with queue length capacity constraints.

Table 3. Simulation parameters.

<table><tr><td>Number of resource servers</td><td>10</td></tr><tr><td>Unit cost for waiting</td><td>5</td></tr><tr><td>Queue length minimum and maximum bounds</td><td>15, 20</td></tr><tr><td>Resource server capacity minimum and maximum bounds</td><td>20, 20</td></tr><tr><td>LaGrange Multiplier</td><td>0.5</td></tr><tr><td>Total Number of Data Points to be Generated</td><td>1000</td></tr><tr><td>Range for mean values of each server</td><td>5, 15</td></tr></table>

The model characterizes a cloud environment where jobs are arriving exogenously to access resources at the individual resource servers. The total arrivals in the cloud environment at any given time are the sum of the exogenous arrivals at individual resource servers. Table 5 shows 10 instances of the simulated individual arrivals $\lambda _ { 1 }$ at resource server 1 and the corresponding total job arrivals in the cloud environment. Figure 3 is a histogram representation of the total cloud environment arrivals for 1000 generated instances for all individual resource server location. It demonstrates that total arrivals in the cloud environment also follows a Poisson process with a mean arrival rate of 116, which is the sum of the individual resource servers mean arrival rates shown in Table 3.

At equilibrium, the jobs are allocated to cloud resource servers such that their loads are as close to equal as possible, utilizing the Job Allocation Algorithm illustrated earlier in Model Section 3.2. The detailed proof shown in Proposition 1, demonstrates this allocation is indeed optimal for the cloud environment since it minimizes total overall wait times in the cloud network. This means that if there are 100 total jobs in the cloud with 10 resource servers, then 10 jobs are allocated to each of the resource servers. In this case, the unit price of executing jobs at each resource server location is identical. However, if total jobs are not a perfect multiple of the number of resource servers, then the extra jobs are randomly allocated to resource servers creating an imbalance in the prices at the diferent resource server locations. As excess jobs are allocated in a cyclic order to resource servers, the diferences in prices for jobs allocated to resources servers balance out to equally priced tiers for all resource servers with an equal number of job allocations. This is demonstrated in the following illustrations.

Table 4. Resource server queue length and capacity.

<table><tr><td>Resource Server</td><td>Mean Poisson Arrival Rates</td><td>Queue Length</td><td>Capacity</td></tr><tr><td>1</td><td>15</td><td>15</td><td>20</td></tr><tr><td>2</td><td>9</td><td>16</td><td>20</td></tr><tr><td>3</td><td>14</td><td>15</td><td>20</td></tr><tr><td>4</td><td>14</td><td>20</td><td>20</td></tr><tr><td>5</td><td>15</td><td>16</td><td>20</td></tr><tr><td>6</td><td>7</td><td>17</td><td>20</td></tr><tr><td>7</td><td>9</td><td>15</td><td>20</td></tr><tr><td>8</td><td>14</td><td>15</td><td>20</td></tr><tr><td>9</td><td>8</td><td>20</td><td>20</td></tr><tr><td>10</td><td>11</td><td>16</td><td>20</td></tr></table>

Table 5. Arrival rate and total jobs over 10 periods at resource server (RS) 1.

<table><tr><td>Arrival Rate RS 1</td><td>Total Jobs</td></tr><tr><td>10</td><td>137</td></tr><tr><td>11</td><td>150</td></tr><tr><td>11</td><td>68</td></tr><tr><td>4</td><td>142</td></tr><tr><td>11</td><td>137</td></tr><tr><td>17</td><td>131</td></tr><tr><td>47</td><td>183</td></tr><tr><td>9</td><td>130</td></tr><tr><td>23</td><td>83</td></tr><tr><td>1</td><td>144</td></tr></table>

We previously derived the optimal price expression (11) in terms of the capacity $\mu _ { j }$ and job allocation $T _ { j }$ at any $j$ . Using expression (11), we can now calculate numerical values for the price $\hbar _ { j }$ for executing jobs at each resource server $\hbar _ { j }$ . Let resource server capacity $\mu _ { j } = 2 0$ for all $\mu _ { j } = 2 0$ and unit waiting time cost $\nu = 5$ . Note that resource server capacities are kept constant to demonstrate the efect of job arrivals alone to allocations and pricing. Using these values, we calculate the price $\mathit { p } _ { j }$ for executing jobs corresponding to $T _ { j }$ in a simulation with 1000 instances.

Histogram - Total Job Arrivals in Cloud System  
![](/api/attachments/NDTNC8EH/fulltext/images/91334af2e754b0bff4367f74c64e1fa5778badb214b13979594e6866bce1388e.jpg)  
Figure 3. Total Job arrivals in Cloud System for 1000 generated instances of jobs arriving at individual resource server locations.

Tables 6 to 8 shows three separated instances of the price per job at each individual resource server and the corresponding total jobs at that specific instance. Figures 4, 5, and 6 all have a very similar look, and this occurs based on how the job allocation algorithm allocates job to each resource server. Since the algorithm fills the resource servers evenly, Figures 4, 5, and 6 show that the increase in a job price is evenly distributed as the total number of jobs increase. These figures demonstrate that filling the capacity for each of the resource servers steadily increases the price to access each resource server. The similar patterns of increasing prices with increasing total jobs at each cloud server is reinforced by Figures 4, 5, and 6. Comparing the three figures indicates that the price per job at each resource server increases at a higher rate as the resource server total jobs tend toward capacity. Note that we can tie this non-linear increase in prices $\boldsymbol { p _ { j } }$ with increasing number of jobs in our simulation back to the expected non-linear efect on waiting times $W _ { j }$ with arrival rates $T _ { j }$ approaching capacity $\mu _ { j }$ , as previously discussed in the Model section. The increase in price per job from Figure 4 to Figure 6 is substantial. However, when each of the resource servers reach capacity, there is a significant jump in price per job at the resource server. This is clear in Figure 7, which shows the change in price per job as total allocations increases from 1 to 185 as well as in Table 9 which shows the significant change in price per server between jobs 179 to 188. When the total job arrivals are greater than the server capacity and the excess jobs are placed in queue of a resource server, the price per job significantly increases for the resource server. This is readily shown in Figures 8, 9, and 10, where the price per job versus total allocation is shown for resource server 1.

In Figure 8, the total allocations increase from 2 to capacity at 20; however, there is a significant increase as the total allocations reach capacity, specifically in the range of 15-20. Figure 8 is broken into two figures to show the diference in the size of price increases. Figure 9 is set to a job allocation range of 2-14 and a steady, smooth increase in price per job as the total allocations increase is shown over a range of 0.028 to 0.084. Whereas Figure 10 shows a job allocation range of 15-19 with an increase in price over a range of 0.1 to 100. The increase is to 1.0E10; however, for the sake of the graph, 100 was chosen. This indicates that submitting a job to a resource server that has reached capacity is a lot more expensive than submitting a job when resource servers are readily available process jobs.

Figure 11 demonstrates the impact of the increase in total jobs on the corresponding allocations to the resource servers. When there is an increase in total jobs, there is a corresponding increase in job allocations to any given resource server. By regulating prices according to the level of job congestion, the resource server loads will balance out in the long term.

The simulation also clearly indicates the waiting time per resource server increased as the total jobs in the queue increased, which is what is expected.

Figure 12 demonstrates that job waiting time versus total jobs in the queue are identical for similar queue lengths 15, 16, 17, and 20, respectively. The smaller queue length constraint resource server’s job waiting time was longer versus the higher queue length constraints. Additionally, resource servers with shorter queue lengths job waiting times increased at a faster rate than those of a resource server with higher queue length constraints. The reduced queue length provides additional QoS due to reduced waiting times by incenting jobs to be priced higher as we approach capacity. Furthermore, managers can examine this optimal price per job with respect to job waiting time in their organizations private cloud to determine when excess jobs should be ofloaded to a public cloud to ensure a minimum QoS.

Table 6. Price per job at each resource server (RS) over a10 periods as total jobs increase.

<table><tr><td>Total Jobs</td><td>Price RS 1</td><td>Price RS 2</td><td>Price RS 3</td><td>Price RS 4</td><td>Price RS 5</td><td>Price RS 6</td><td>Price RS 7</td><td>Price RS 8</td><td>Price RS 9</td><td>Price RS 10</td></tr><tr><td>17</td><td>0.0277778</td><td>0.0277778</td><td>0.0277778</td><td>0.0277778</td><td>0.0277778</td><td>0.0277778</td><td>0.0277778</td><td>0.0263158</td><td>0.0263158</td><td>0.0263158</td></tr><tr><td>25</td><td>0.0294118</td><td>0.0294118</td><td>0.0294118</td><td>0.0294118</td><td>0.0294118</td><td>0.0277778</td><td>0.0277778</td><td>0.0277778</td><td>0.0277778</td><td>0.0277778</td></tr><tr><td>28</td><td>0.0294118</td><td>0.0294118</td><td>0.0294118</td><td>0.0294118</td><td>0.0294118</td><td>0.0294118</td><td>0.0294118</td><td>0.0294118</td><td>0.0277778</td><td>0.0277778</td></tr><tr><td>32</td><td>0.03125</td><td>0.03125</td><td>0.0294118</td><td>0.0294118</td><td>0.0294118</td><td>0.0294118</td><td>0.0294118</td><td>0.0294118</td><td>0.0294118</td><td>0.0294118</td></tr><tr><td>33</td><td>0.03125</td><td>0.03125</td><td>0.03125</td><td>0.0294118</td><td>0.0294118</td><td>0.0294118</td><td>0.0294118</td><td>0.0294118</td><td>0.0294118</td><td>0.0294118</td></tr><tr><td>34</td><td>0.03125</td><td>0.03125</td><td>0.03125</td><td>0.03125</td><td>0.0294118</td><td>0.0294118</td><td>0.0294118</td><td>0.0294118</td><td>0.0294118</td><td>0.0294118</td></tr><tr><td>35</td><td>0.03125</td><td>0.03125</td><td>0.03125</td><td>0.03125</td><td>0.03125</td><td>0.0294118</td><td>0.0294118</td><td>0.0294118</td><td>0.0294118</td><td>0.0294118</td></tr><tr><td>36</td><td>0.03125</td><td>0.03125</td><td>0.03125</td><td>0.03125</td><td>0.03125</td><td>0.03125</td><td>0.0294118</td><td>0.0294118</td><td>0.0294118</td><td>0.0294118</td></tr><tr><td>38</td><td>0.03125</td><td>0.03125</td><td>0.03125</td><td>0.03125</td><td>0.03125</td><td>0.03125</td><td>0.03125</td><td>0.03125</td><td>0.0294118</td><td>0.0294118</td></tr><tr><td>39</td><td>0.03125</td><td>0.03125</td><td>0.03125</td><td>0.03125</td><td>0.03125</td><td>0.03125</td><td>0.03125</td><td>0.03125</td><td>0.03125</td><td>0.0294118</td></tr></table>

Table 7. Price per job at each resource server (RS) over a 10 periods as total jobs increase.

<table><tr><td>Total Jobs</td><td>Price RS 1</td><td>Price RS 2</td><td>Price RS 3</td><td>Price RS 4</td><td>Price RS 5</td><td>Price RS 6</td><td>Price RS 7</td><td>Price RS 8</td><td>Price RS 9</td><td>Price RS 10</td></tr><tr><td>149</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.0833333</td></tr><tr><td>150</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.1000000</td></tr><tr><td>151</td><td>5.625</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.1000000</td></tr><tr><td>152</td><td>5.625</td><td>5.625</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.1000000</td></tr><tr><td>153</td><td>5.625</td><td>5.625</td><td>5.625</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.1000000</td></tr><tr><td>154</td><td>5.625</td><td>5.625</td><td>5.625</td><td>5.625</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.1000000</td></tr><tr><td>155</td><td>5.625</td><td>5.625</td><td>5.625</td><td>5.625</td><td>5.625</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.100</td><td>0.1000000</td></tr><tr><td>157</td><td>5.625</td><td>5.625</td><td>5.625</td><td>5.625</td><td>5.625</td><td>5.625</td><td>5.625</td><td>0.100</td><td>0.100</td><td>0.1000000</td></tr><tr><td>158</td><td>5.625</td><td>5.625</td><td>5.625</td><td>5.625</td><td>5.625</td><td>5.625</td><td>5.625</td><td>5.625</td><td>0.100</td><td>0.1000000</td></tr><tr><td>159</td><td>5.625</td><td>5.625</td><td>5.625</td><td>5.625</td><td>5.625</td><td>5.625</td><td>5.625</td><td>5.625</td><td>5.625</td><td>0.1000000</td></tr><tr><td>160</td><td>5.625</td><td>5.625</td><td>5.625</td><td>5.625</td><td>5.625</td><td>5.625</td><td>5.625</td><td>5.625</td><td>5.625</td><td>5.6250000</td></tr></table>

Table 8. Price per job at each resource server (RS) over a 10 periods as total jobs increase.

<table><tr><td>Total Jobs</td><td>Price RS 1</td><td>Price RS 2</td><td>Price RS 3</td><td>Price RS 4</td><td>Price RS 5</td><td>Price RS 6</td><td>Price RS 7</td><td>Price RS 8</td><td>Price RS 9</td><td>Price RS 10</td></tr><tr><td>169</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.625</td></tr><tr><td>170</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td></tr><tr><td>171</td><td>22.25</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td></tr><tr><td>172</td><td>22.25</td><td>22.25</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td></tr><tr><td>173</td><td>22.25</td><td>22.25</td><td>22.25</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td></tr><tr><td>174</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td></tr><tr><td>175</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td><td>5.66667</td></tr><tr><td>177</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>5.66667</td><td>5.66667</td><td>5.66667</td></tr><tr><td>178</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>5.66667</td><td>5.66667</td></tr><tr><td>179</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>5.66667</td></tr><tr><td>180</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td></tr></table>

Price per Job vs Total Jobs 17-39  
![](/api/attachments/NDTNC8EH/fulltext/images/246b21b34cc909701808fd411ac414a2ddff072ef42eb7dcdeb4269560f49230.jpg)  
Figure 4. Price per job at each resource server (RS) over a 10 periods as total jobs increase.

Price per Job vs Total Jobs 149-160  
![](/api/attachments/NDTNC8EH/fulltext/images/27ba0efcfc7744624eb922f1248bfb3de03517fb90edb908fb6b8dc8901ac5b1.jpg)  
Figure 5. Price per job at each resource server (RS) over a 10 periods as total jobs increase.

Price per Job vs Total Jobs 169-180  
![](/api/attachments/NDTNC8EH/fulltext/images/540c9e68cb29b8334adeaaa9cc39351b1e11c58a015c3583f8e8e07894d7decd.jpg)  
Figure 6. Price per job at each resource server (RS) over a 10 periods as total jobs increase.

Pserver vs Total Job 1-180  
![](/api/attachments/NDTNC8EH/fulltext/images/e93dcc428736371cf51efd75e805799eae2449733c80102483c335dfe08c7312.jpg)  
Figure 7. Price per job at each resource server (RS) as total jobs increase from 1 to 180.

Price per Job vs Job Allocation for Resource Server 1  
![](/api/attachments/NDTNC8EH/fulltext/images/f751d5939c6d90b71cf8d0640940fc0baae9efe7e07f34943fe7dc042380a096.jpg)  
Figure 8. Price per job at resource server (RS) 1 as job allocations increases.

Table 9. Price per job at each resource server (RS) as total jobs increase from 1 to 180.

<table><tr><td>Total Jobs</td><td>Price RS 1</td><td>Price RS 2</td><td>Price RS 3</td><td>Price RS 4</td><td>Price RS 5</td><td>Price RS 6</td><td>Price RS 7</td><td>Price RS 8</td><td>Price RS 9</td><td>Price RS 10</td></tr><tr><td>179</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>5.66667</td></tr><tr><td>180</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td></tr><tr><td>182</td><td>1.00E+10</td><td>1.00E+10</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td></tr><tr><td>183</td><td>1.00E+10</td><td>1.00E+10</td><td>1.00E+10</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td></tr><tr><td>185</td><td>1.00E+10</td><td>1.00E+10</td><td>1.00E+10</td><td>105</td><td>1.00E+10</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td></tr><tr><td>186</td><td>1.00E+10</td><td>1.00E+10</td><td>1.00E+10</td><td>105</td><td>1.00E+10</td><td>1.00E+10</td><td>22.25</td><td>22.25</td><td>22.25</td><td>22.25</td></tr><tr><td>187</td><td>1.00E+10</td><td>1.00E+10</td><td>1.00E+10</td><td>105</td><td>1.00E+10</td><td>1.00E+10</td><td>1.00E+10</td><td>22.25</td><td>22.25</td><td>22.25</td></tr><tr><td>188</td><td>1.00E+10</td><td>1.00E+10</td><td>1.00E+10</td><td>105</td><td>1.00E+10</td><td>1.00E+10</td><td>1.00E+10</td><td>1.00E+10</td><td>22.25</td><td>22.25</td></tr></table>

Price per Job vs Job Allocation for Resource Server 1  
![](/api/attachments/NDTNC8EH/fulltext/images/11add5cba401ef79c136a9b563ff023d0425b58d2e7c8693ed3a348da4b8a1ea.jpg)  
Figure 9. Price per job at resource server (RS) 1 as job allocation increases from 0 to 15.

Price per Job vs Job allocation for Resource Server 1  
![](/api/attachments/NDTNC8EH/fulltext/images/0e5010725e81750254ec9d5ad036a472098b74aae8bb38034e2ee9c6ec869ebe.jpg)  
Figure 10. Price per job at resource server (RS) 1 as job allocation increases from 0 to 15.

Comparison of Jobs at RS 1 vs Total Job Allocations in Cloud  
![](/api/attachments/NDTNC8EH/fulltext/images/10766850cdbe97f8bc69d2565959df45ae8d345c1f005dd53ff94798745353aa.jpg)  
Figure 11. Job arrival rate and Jobs allocated to resource server 1 as the total number of jobs allocated to servers in Cloud increase.

Wait Time vs Jobs in Queue  
![](/api/attachments/NDTNC8EH/fulltext/images/f8ec23ff60a92e64733948c78f826dc1b364c534a5a537a98d3847c61108d9ba.jpg)  
Figure 12. Wait time at each resource server (RS) with corresponding queue length (QL) as the number of jobs in the queue increases.

## Discussion and Conclusions

The pervasiveness of computing technology and Internet access has led to an increase in the reliance on Internet based services for both consumers and organizations, which in turn increased the number of computing-based resources needed by organizations. The cost to implement and maintain traditional computer-based systems to meet the needs of an organization has become expensive, leading to an increased use in-cloud based systems. Organizations can use clouds to deploy their technology resources more eficiently at a lower cost when compared to a traditional IT system. This combined with the prevalence of computing technology and high-speed internet access has led organizations to shift to the use of private clouds in combination of public clouds to help meet the organization’s needs.

The increase in overall demand for IT resources and the implementation of cloud based systems by organizations has significantly increased the number of data centers throughout the world, this trend has caused a significant increase in the overall CO2 output. One way to help decrease the overall CO2 output by cloud computing is through eficient utilization of the cloud resources. The purpose of this research study is to create an eficient load balancing mechanism to help organizations optimize the usage of the available cloudbased resources. We examine the case where an organization maximizes the load balancing of resources in its own private cloud to optimize the usage of cloud resources. The private cloud consists of multiple resource servers with the ability to create various virtualized environments; each resource server has the capability of receiving multiple jobs. In addition to maximizing the usage of resources, we extend our mechanism to account for a maximum permissible queue length for each resource server. The queue length ensures a QoS for the firm’s private cloud by limiting the end users’ delay. We study the case where any resource server in the private cloud can outsource a job to a third party based on its own utilization level. The mechanism that we present is advantageous to organization by allowing them to better allocate their cloud resources.

We prove that balancing the job allocation, such that the number of jobs at individual resource servers are as close to equal as possible, is optimal in a cloud-computing environment. Based on our model, a cloud computing load balancing algorithm was developed, which can minimize overall wait time in the cloud while also ensuring a minimum QoS. We create a simulation using the job allocation algorithm and analytically derive result to numerically evaluate the behavior of the cloud mechanism. The simulation results give insight to managers, showing that understanding the optimal price per job with respect to job waiting time of the cloud computing system will help determine when to transfer excess jobs to a public cloud for execution. Companies such as Smithfield Foods, Airbus, and UBS, that use hybrid clouds that allow them the flexibility to access public clouds when demand calls for it, would be able to use this model to help them optimize their eficiency. This optimization in turn would help impact the company’s energy use and help green their IT systems.

The demand for computing resources by consumers and organizations increased the amount of physical data centers in the world today. Approximately 2 percent of the electricity is used in the world today is consumed by data center usage [13]; in other words, data centers produce approximately .625 gigatons of carbon emissions on a yearly basis [18]. The number of data centers and the amount of electricity used to power the data centers will increase as more consumers and organization access services over the Internet. One benefits of the eficient resource allocation in a cloud environment leads to a reduction in overall energy usage of the cloud, as stated in the literature. Our model will help organizations provide a more eficient allocation of resources in a cloud environment, which will also help contribute to greening the organization IT infrastructure.

While our research intent is to optimize clouds to help create a greener IT infrastructure, there are still ways to extend our work. First, our model examines spinning of virtualized machines that all have the same resource usage. The model can be expanded to examine the impact of varying the amount of resources allocated to each virtualized machine based on the job submitted to more realistically examine optimal pricing and the minimization of wait times. The focus of the model is based on minimizing overall wait times within the cloud while organization may prioritize diferent objectives. Examining the profit or revenue maximization can be an interesting approach to better understand how public clouds are currently designed and used. Our model is an initial attempt at this type of dynamic pricing approach, which allows for many interesting avenues for future research. For example, spot pricing for jobs on public clouds such as Amazon AWS, may be examined for pricing impact on cloud-based services. Alternative dynamic pricing models, such as value-based, and location-based, may also be compared versus our net value maximization approach [6, 19, 34, 40, 60]. These topics are interesting areas to pursue for future research. Another area of future research is to compare the diferent types of dynamic cloud pricing strategies, as well as to examine alternative non dynamic pricing strategies that may be provided to private cloud users and evaluate the overall benefit of each approach to the cloud network. Finally, it would be interesting to examine a cloud computing environment composed of individual users, not part of an organization, who are behaving strategically. This would allow us to gain insight into how public clouds are currently used.

## Notes

1. https://cloud.google.com/sustainability/

2. https://www.microsoft.com/en-us/corporate-responsibility/sustainability?activetab=pivot\_1% 3aprimaryr3

## Disclosure Statement

No potential conflict of interest was reported by the authors.

## Notes on contributors

Chetan Kumar (ckumar@csusm.edu) is an Associate Professor of Information Systems at California State University San Marcos. He received his Ph.D. from Purdue University. His research interests include cybersecurity, big data, cloud computing, electronic commerce, web analytics, and green IT.

Dr. Kumar has published a number of papers in such journals as Decision Support Systems, Electronic Commerce Research and Applications, and Journal of Information Systems and Technology Management, among others. He has presented his research at such conferences as the Institute for Operations Research and Management Sciences Annual Meeting, Workshop on E-Business, Workshop on Information Systems and Economics, and International Conference on Information Systems Doctoral Consortium.

Sean Marston (sean.marston@wku.edu) is an Associate Professor of Information Systems at Gordon Ford College of Business Staf, Western Kentucky University. His research focuses the analysis of digital distribution of information, the economic analysis of information systems policies, cloud computing security policy, and the use of technology in higher education. He has presented his research at several academic conferences including Pacific Asia Conference on Information Systems, Hawaii International Conference on System Sciences, Decision Sciences Institute annual meeting, and the INFORMS annual meeting.

Ravi Sen (rsen@mays.tamu.edu; corresponding author) is an Associate Professor at Mays Business School, Texas A&M. He received his Ph.D. from the University of Illinois at Urbana-Champaign. His research interests include cybersecurity, open source software, and economics of electronic commerce. He has published in the Journal of Management Information Systems, Production and Operations Management, Decision Support Systems, Decision Sciences, International Journal of Electronic Commerce, Communications of AIS and other journals.

Amar Narisetty (amar.narisetty@gmail.com) is a Principal Operations Research Specialist at SAS Institute Inc. He received his Ph.D. in Industrial Engineering from Purdue University.

## References

1. Alakeel, A.M. A Guide to dynamic load balancing in distributed computer systems. International Journal of Computer Science and Network Security (IJCSNS), 10(6), (2010),153–160.

2. Andrae, A.; and Edler, T. On global electricity usage of communication technology: trends to 2030. Challenges, 6(1), (2015),117–157.

3. Beloglazov, A.; and Buyya, R. Energy eficient allocation of virtual machines in cloud data centers. In Proceedings of the 2010 10th IEEE/ACM International Conference on Cluster, Cloud and Grid Computing (CCGRID’10), (2010), 577–578.

4. Benini L.; Bogliolo A.; and Micheli G.D. A survey of design techniques for system-level dynamic power management. IEEE Trans Very Large Scale Integr (VLSI), 8(3), (2000), 299–316.

5. Branscombe M. The network impact of the global COVID-19 pandemic. The New Stack, (2020). https://thenewstack.io/the-network-impact-of-the-global-covid-19-pandemic/ April 14. (accessed on June 6, 2020).

6. Chen, S.; Lee, H.; and Moinzadeh, K. Pricing schemes in cloud computing: Utilization-based vs. reservation-based. Production and Operations Management, 28(1), (2019), 82–102.

7. Choudhary, V.; and Vithayathil, J. The impact of cloud computing: Should the IT department be organized as a cost center or a profit center? Journal of Management Information Systems, 30 (2), (2013), 67–100.

8. Chunxia, Y.; and Shunfu, J. An energy-saving strategy based on multi-server vacation queuing theory in cloud data center. The Journal of Supercomputing, 74(12), (2018), 6766–6784.

9. Cloud Computing Market by Service Model (Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS)), Deployment Model (Public and Private), Organization Size, Vertical, and Region - Global Forecast to 2025 (2020) https://www.marketsandmarkets.com/ Market-Reports/cloud-computing-market-234.html (accessed on November 21, 2021)

10. Columbus, L. 83% Of Enterprise Workloads Will Be in The Cloud By 2020. Forbes, (2018). https://www.forbes.com/sites/louiscolumbus/2018/01/07/83-of-enterprise-workloads-will-bein-the-cloud-by-2020/#1c2b2b06261a (accessed on November 21, 2021)

11. Companies using Amazon Virtual Private Cloud (VPC) (2020), https://enlyft.com/tech/pro ducts/amazon-virtual-private-cloud-vpc (accessed on November 21, 2021)

12. Cooney, M. IBM wants to manage your cloud services no matter which ones you run. Network World, (2018). https://www.networkworld.com/article/3313332/cloud-computing/ibm-wantsto-manage-your-cloud-services-no-matter-which-one-you-run.html. (accessed on November 21, 2021).

13. Data Center Renewable Energy. Google. (2018), https://www.google.com/about/datacenters/ renewable/index.html (accessed on November 21, 2021).

14. Dimitri, N. Pricing cloud IaaS computing services. Journal of Cloud Computing, 9(1), (2020), 1–11.

15. Ezra, A. Renewable Energy Alone Can’t Address Data Centers’ Adverse Environmental Impact. Forbes, May 3, (2021). https://www.forbes.com/sites/forbestechcounsil/2021/05/03/renewableenergy-alone-cant-address-data-centers-adverse-environmental-impact/?sh= 6897D1DB5DDC. (accessed on November 21, 2021)

16. Fox, A.; Grifith, R.; Joseph, A.; Katz, R.; Konwinski, A.; Lee, G.; Patterson, D.; Rabkin, A.; and Stoica, I. Above the Clouds: A Berkeley View of cloud computing. Dept. Electrical Eng. and Computer. Sciences, University of California, Berkeley, Rep. UCB/EECS, 28(13), 2009.

17. Gawali, M.B.; and Shinde, S.K. Task scheduling and resource allocation in cloud computing using a heuristic approach. Journal of Cloud Computing, 7(4), (2018), 1–16.

18. Global energy demand grew by 2.1% in 2017, and carbon emissions rose for the first time since 2014. International Energy Agency, March 22, (2018). https://www.iea.org/news/global-energydemand-grew-by-21-in-2017-and-carbon-emissions-rose-for-the-first-time-since-2014 (accessed on November 21 2021).

19. Greenberg, A.; Hamilton, J.; Maltz, D. A.; and Patel, P. The cost of a cloud: research problems in data center networks. ACM SIGCOMM Computer Communication Review, 39(1), (2009), 68–73.

20. Hameed, A.; Khoshkbarforoushha, A.; Ranjan, R. et al. A survey and taxonomy on energy eficient resource allocation techniques for cloud computing systems. Computing, 98(7), (2016), 751–774.

21. Hlavacs, H.; Da Costa, G.; and Pierson, J. Energy consumption of residential and professional switches (regular paper). In Computational Science and Engineering 2009. CSE’09. International Conference, 1, (2009), pp. 240–246. IEEE.

22. Hu, P.J. H.; Hu, H.F.; Wei, C.P.; and Hsu, P.F. Examining firms’ green information technology practices: A hierarchical view of key drivers and their efects. Journal of Management Information Systems, 33(4), (2016), 1149–1179.

23. Huang, J.; Kaufman, R.; and Ma, D. Pricing strategy for cloud computing: A damaged services perspective. Decision Support Systems, 78, (2015), 80–92.

24. Joe-Wong, C.; and Sen, S. Harnessing the power of the cloud: Revenue, fairness, and cloud neutrality. Journal of Management Information Systems, 35(3), (2018), 813–836.

25. Kansal, N.; and Chana, I. Cloud load balancing techniques: A step towards green computing. IJCSI International Journal of Computer Science Issues, 9(1), (2012), 238–246.

26. Kathuria, A.; Mann, A.; Khuntia, J.; Saldanha, T. J.; and Kaufman, R.J. A strategic value appropriation path for cloud computing. Journal of Management Information Systems, 35(3), (2018), 740–775.

27. Kaur, T. Energy Eficiency Trends in Cloud Computing. Journal of the Gujarat Research Society, 21(6), (2019), 542–553.

28. Kaushal, S.; Gogia, D.; and Kumar, B. Recent Trends in Green Cloud Computing. In Proceedings of 2nd International Conference on Communication, Computing and Networking, (2019), pp. 947–956. Springer: Singapore.

29. Kothari, M. Green Computing: Approach to Green IT. Tech Tonics, 17, (2019).

30. Kumar, C.; Altinkemer, K.; and De, P. A Mechanism for pricing and resource allocation in peer‒to‒peer networks. Electronic Commerce Research and Applications, 10(1), (2011), 26–37.

31. Kumar, C., and Bandyopadhyay, S. Computer networks, the Internet, and Green IT: Managing computer networks efectively. In The Eleventh Workshop on e-Business, Orlando, FL, December 15, (2012).

32. Kumar, C., and Marston, S. Accelerating the Internet in the presence of big data: Reducing user delays by leveraging historical user request patterns for web caching. Journal of Information Systems and Technology Management, 16, (2019), 72-82.

33. Kumar, M.; Sharma, S.; Goel, A.; and Singh, S. A comprehensive survey for scheduling techniques in cloud computing. Journal of Network and Computer Applications, 143, (2019), 1–33.

34. Lee, I. Pricing schemes and profit-maximizing pricing for cloud services. Journal of Revenue and Pricing Management, 18(2),(2019), 112–122.

35. Liu, Z.; Qu, W.; Liu, W.; Li, Z.; and Xu, Y. Resource preprocessing and optimal task scheduling in cloud computing environments. Concurrency and Computation: Practice and Experience, 27 (13), (2015), 3461–3482.

36. Lu, Y.; and Sun, N. An efective task scheduling algorithm based on dynamic energy management and eficient resource utilization in green cloud computing environment. Cluster Computing, 22(1), (2019), 513–520.

37. MacKie-Mason, J. K.; and Varian, H. R. Pricing the internet. Public access to the Internet, (1995), 269-273.

38. Madni, S. H.H.; Latif, M. S. A.; and Coulibaly, Y. Recent advancements in resource allocation techniques for cloud computing environment: a systematic review. Cluster Computing, 20(3), (2017), 2489–2533.

39. Marston, S.; Li, Z.; Bandyopadhyay, S.; Zhang, J.; and Ghalsasi, A. Cloud computing — The business perspective, Decision Support Systems, 51(1), (2011), 176–189.

40. Meenal, A.; and Ankita, J. Study on green cloud computing—A review. Machine Learning Approach for Cloud Data Analytics in IoT, (2021), 307-322.

41. Mendelson, H. Pricing computer services: Queueing efects. Communications of the ACM, 28 (3), (1985), 312–321.

42. Mishra, S.; Sahoo, B.; and Parida, P. Load balancing in cloud computing: A big picture. Journal of King Saud University-Computer and Information Sciences, 32(2), (2020), 149–158.

43. Mixed grill: Smithfield Foods runs its \$15 billion pork business using a hybrid cloud (2018) https:// customers.microsoft.com/en-us/story/smithfield-azure-us-en. (accessed on November 21, 2021)

44. Nathuji, R.; and Schwan, K. VirtualPower: Coordinated power management in virtualized enterprise systems. ACM SIGOPS Symposium Operating Systems Review, 41(6), (2007), 265–278.

45. Pesce, M. Cloud Computing’s Coming Energy Crisis. IEEE Spectrum, July 21 (2021). https:// www.bloombergquint.com/business/microsoft-teams-up-with-accenture-goldman-ongreener-software. (accessed on November 21, 2021)

46. Prakash, S. Role of virtualization techniques in cloud computing environment. In Bhatia, S.K., Tiwari, S., Mishra, K.K., Trivedi, M.C. (eds.), Advances in Computer Communication and Computational Sciences, Singapore: Springer, 2019, pp. 439–450.

47. Radu, L.D. (2017). Green cloud computing: A literature survey. Symmetry, 9(12), 295.

48. Rima, B.P.; Choi, E., and Lumb, I. A Taxonomy and survey of cloud computing systems. In Proceedings of 5th IEEE International Joint Conference on INC, IMS and IDC, NCM, Seoul, Korea, (2009), pp. 44–51.

49. Shakeel, F., and Sharma S. Green cloud computing: A review on eficiency of data centres and virtualization of servers. In 2017 International Conference on Computing, Communication and Automation (ICCCA), Greater Noida, India. IEEE, 2017, pp. 1264–1267.

50. Sharifi, M.; Salimi, H.; and Najafzadeh, M. Power-eficient distributed scheduling of virtual machines using workload-aware consolidation techniques. The Journal of Supercomputing. 61 (1), (2012), 46–66.

51. Strunk, A., and Waltenegus, D. Does live migration of virtual machines cost energy? In Proceedings of 2013 Advanced Information Networking and Applications (AINA), Barcelona, Spain. IEEE, 2013, pp. 514–521.

52. Subramanian, N.; Abdulrahman, M.; and Zhou, X. Integration of logistics and cloud computing service providers: Cost and green benefits in the Chinese context. Transportation Research Part E: Logistics and Transportation Review 70, (2014), 86–98.

53. Sweeney, J.; and Bradfield, J. Reducing data center’s power and energy consumption: saving money and go “Green.” Saving Money and “Going Green” White paper. (2018) https://shop. unicomgov.com/cms/documents/white-papers/green-it.pdf. (accessed on November 21, 2021)

54. Telenyk S.; Zharikov E.; and Rolik O. Architecture and conceptual bases of cloud IT infrastructure management. In Advances in Intelligent Systems and Computing, Springer, Cham., 2017, pp. 41–62.

55. The global data center market is expected to grow at a CAGR of over 2% during the period 2019–2025 (2020). https://www.globenewswire.com/news-release/2020/02/14/1985327/0/en/ the-global-data-center-market-is-expected-to-grow-at-a-cagr-of-over-2-during-the-period -2019-2025.html. (accessed on November 21, 2021)

56. Uddin, M.; Darabidarabkhani, Y.; Shah, A.; and Memon, J. Evaluating power eficient algorithms for eficiency and carbon emissions in cloud data centers: A review. Renewable and Sustainable Energy Reviews, 51, (2015), 1553–1563.

57. Vasic, N., and Kostic, D. Energy-aware trafic engineering. In Proceedings of the 1st International Conference on Energy-Eficient Computing and Networking, Passau, Germany. ACM, 2010, pp. 169–178.

58. Walmart establishes strategic partnership with Microsoft to further accelerate digital innovation in retail. (2018). https://corporate.walmart.com/newsroom/2018/07/17/walmartestablishes-strategic-partnership-with-microsoft-to-further-accelerate-digital-innovation-inretail. (accessed on November 21, 2021)

59. Watson, R.; Boudreau, M.; Chen, A.; and Huber, M. Green IS: Building sustainable business practices. Information Systems: A Global Text, (2008), 1–17.

60. Wu, C.; Toosi, A.N.; Buyya, R.; and Ramamohanarao, K. Hedonic pricing of cloud computing services. IEEE Transactions on Cloud Computing, 9 (1),Jan-March (2021), 182–196.

61. Xu, M.; Tian, W.; and Buyya, R. A survey on load balancing algorithms for virtual machines placement in cloud computing. Concurrency and Computation: Practice and Experience, 29 (12), (2017), 1–22.

62. Zhu, D.; Melhem, R.; and Childers, B.R. Scheduling with dynamic voltage/speed adjustment using slack reclamation in multiprocessor real time systems. IEEE Transactions on Parallel and Distributed Systems, 14(7), (2003), 686–699.
