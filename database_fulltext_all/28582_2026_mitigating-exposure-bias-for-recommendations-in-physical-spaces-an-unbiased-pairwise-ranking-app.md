---
otero_id: 28582
otero_key: "64TQ7628"
title: "Mitigating Exposure Bias for Recommendations in Physical Spaces: An Unbiased Pairwise Ranking Approach Using Spatial Movement"
authors: "Jiangning He; Weikun Wu; Fan Zhang; Zhepeng (Lionel) Li"
year: "2026"
journal: "Information Systems Research"
doi: "10.1287/isre.2023.0100"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Mitigating Exposure Bias for Recommendations in Physical Spaces: An Unbiased Pairwise Ranking Approach Using Spatial Movement

Jiangning He,<sup>a</sup> Weikun Wu,<sup>a</sup> Fan Zhang,<sup>a</sup> Zhepeng (Lionel) Li<sup>b,</sup>\*

<sup>a</sup> School of Information Management and Engineering, Shanghai University of Finance and Economics, Shanghai 200433, China; <sup>b</sup> Faculty of Business and Economics, The University of Hong Kong, Hong Kong, China \*Corresponding author

Contact: he.jiangning@mail.shufe.edu.cn, https://orcid.org/0000-0002-6313-5266 (JH); wu.weikun@stu.sufe.edu.cn, https://orcid.org/0009-0004-6735-5989 (WW); vivifansh@163.sufe.edu.cn, https://orcid.org/0000-0003-0343-3648 (FZ); zpli@hku.hk, https://orcid.org/0000-0002-7988-0412 (Z(L)L)

Received: February 20, 2023 Revised: March 14, 2024; March 29, 2025 Accepted: May 31, 2025 Published Online in Articles in Advance: July 14, 2025

https://doi.org/10.1287/isre.2023.0100

Copyright: © 2025 INFORMS

Abstract. The remarkable success in personalized recommendations on digital platforms has sparked interest in extending this advancement to physical spaces. In response, our study introduces a generalized recommendation problem, named point-of-interest (POI) recommen dations in physical spaces with pedestrian movement (P3M). A critical yet under-investigated impediment in addressing P3M is exposure bias: When the exposure likelihood of items to users is unevenly distributed, indiscriminately treating all unobserved user–item interaction as negative feedback introduces bias to the learning of recommender systems. Unlike existing debiasing literature on digital platforms, we focus on the unique source of uneven exposure in physical spaces, arising from the dynamic interaction between pedestrian movement and spa tial layout. To address this issue, we propose a novel recommendation method, unbiased movement-aware pairwise ranking (UMPR), which considers dynamic pedestrian movement to achieve unbiased POI recommendations. Specifically, we formulate an unbiased pairwise learning framework, propose a movement-aware recommendation model, and devise an alternating learning algorithm to optimize model parameters. Using real-world mall data, we demonstrate that our method outperforms state-of-the-art benchmarks in delivering store recommendations for pedestrian shoppers. Further investigations confirm that the improved recommendation performance translates into added monetary value while maintaining humanistic fairness across customers and store tenants. Overall, this study underscores the significance of addressing exposure bias through adequate spatial movement modeling, paving the way for effective recommendations in the physical landscape.

History: Ahmed Abbasi, Senior Editor; Dokyun Lee, Associate Editor. Funding: This work was supported by the National Natural Science Foundation of China [Grant 72001128] the University Research Committee, University of Hong Kong [Grant 104006434.115746.07030.301.01], and the Research Grants Council, University Grants Committee [Grant 17500122] Supplemental Material: The online appendices are available at https://doi.org/10.1287/isre.2023.0100.

Keywords: recommender systems • physical recommendations • exposure bias • spatial movement • pairwise learning

## 1. Introduction

Personalized recommendations have achieved remarkable success on online platforms by integrating artificial intelligence (AI) technology into business operations, such as product and service provision, yielding significant economic value including increased sales (Li et al. 2022) and improved conversion rates (Lee and Hosanagar 2021). Brick-and-mortar businesses are now proactively seeking viable solutions to transfer the success of personalized services from online to offline scenarios. A salient example is Cheetah Mobile (New York Stock Exchange (NYSE): CMCM), which has launched its AI-powered mall robots in more than 962 shopping malls across 33 cities in China (Synced 2020). These robots, equipped with AI, sensor technologies, and an embedded indoor navigation system, can actively interact with customers and intelligently recommend stores, brands, and coupons, thereby attracting foot traffic, boosting coupon redemption rates, and increasing sales. Another notable example is Amazon’s Dash Cart, a smart shopping cart that combines computer vision and sensor fusion to identify items added to the cart. This cart serves as a shopping companion that travels through a store with a pedestrian customer, helping them locate items and providing personalized recommendations through an on-cart screen. This innovation not only enhances personalization and convenience for pedestrian customers but also demonstrates a 10% increase in per-cart sales (Kumar 2024). Thus, making effective recommendations in physical spaces presents a promising avenue for enhancing customer experience, delivering targeted marketing, and boosting revenues (Walter et al. 2012, Ghose et al. 2019).

Recommending in physical spaces for pedestrian customers warrants a common setting across various applications, referred to as point-of-interest (POI) recommendations in physical spaces with pedestrian movement (P3M). This setting is characterized by three key features. First, we consider a physical space encompassing a diverse set of POIs. Each POI corresponds to a location (e.g., a store) or a facility (e.g., a shelf) that is frequently visited by customers. Second, the arrangement of the POIs follows a specific spatial layout that may encompass walls, corridors, and stairs. This spatial structure not only affects customer movement but also determines the likelihood of each POI being visited and exposed (Hui et al. 2009). Third, individuals adopt the mode of pedestrian movement (i.e., walking) to explore the space and interact with the POIs. The sequence of POIs visited in succession, termed the visitation sequence, reflects customers’ preferences and decision paths. In this setting, the goal of recommender systems is to suggest the next POI that a customer is most likely to visit based on their visitation sequence. This P3M setting can cover various recommendation problems in physical environments, including but not limited to store recommendations in shopping malls (Ghose et al. 2019), product shelf recommendations in hypermarkets (Shin et al. 2022) and grocery stores (Zeng et al. 2021), and exhibit recommendations in world expos and museums. Given the significant role of recommender systems in alleviating the choice overload problem, such personalized recommendation services are particularly valuable in medium- to large-scale physical environments, featuring a broad spectrum of POIs and a heterogeneous customer base (Walter et al. 2012).

A critical yet under-investigated impediment to solving the P3M problem is exposure bias. This bias prevails in implicit–feedback recommendations, where observed interactions (e.g., visited POIs) reflect positive preferences, whereas unobserved interactions (e.g., unvisited POIs) do not necessarily represent negative preferences (Saito et al. 2020). Thus, accurate identification of negative feedback from unobserved interactions is essential for the effective learning of recommender systems with implicit feedback. Exposure bias arises when the exposure likelihood of items to users is unevenly distributed, so indiscriminately treating all unobserved user–item interactions as negative feedback introduces a bias to the learning of recommender systems (Chen et al. 2023, Krause et al. 2024). This uneven exposure is particularly pronounced in the context of P3M, influenced by factors such as popularity, spatial layout, and movement paths. For instance, in shopping malls, popular stores receive a greater exposure chance than unpopular ones. Besides, stores that are located along customers’ movement paths and with greater visibility are more likely to be exposed and visited compared with those that are distant or less visible (Mowrey et al. 2019). Therefore, the dynamic interaction between pedestrian movement and spatial layout constitutes a primary source of exposure bias in physical spaces, which remains an underexplored aspect of existing research.

Using the mall context as an example, we illustrate the unique mechanism of exposure bias arising from pedestrian movement and its impact on the identification of negative feedback and recommender learning. During a customer’s movement process, the exposure likelihood of POIs is not uniformly distributed, but spa tially biased toward the space that is being explored. Figure 1 shows a pedestrian customer outside store D currently, with a gray sector indicating the customer’s visual scope. At this moment, stores D, E, and O are more likely to be exposed to the customer than those stores (e.g., F and G) that are out of scope. As the customer moves forward, stores F and G tend to catch the customer’s visual attention. Therefore, stores’ exposure likelihood depends on customers’ movement status (e.g., position, moving direction, and visual scope) and dynamically changes with pedestrian movement. Sup pose that the customer next patronizes store F. During the movement process from store D to F, it is very likely that the exposed but unvisited stores (e.g., E and O) represent negative preferences. Nevertheless, it is uncertain whether store H is negative or potentially positive because the store has not been exposed and considered by the customer. If we indiscriminately treat all unvis ited stores as negative feedback, the learned recom mender system would be severely biased, leading to suboptimal recommendation results (Saito et al. 2020), amplifying the Matthew effect (i.e., the rich stores get richer; Wan et al. 2022), and diminishing customers exploratory shopping experience. Therefore, to correct exposure bias, it is necessary to dynamically mode pedestrian movement in the physical space and incorporate this into the development of unbiased recommendations.

Methodologically, our study is closely related to two research streams: unbiased recommendations on exposure bias and spatially aware recommendations. A thorough review of the literature reveals two research gaps. First, existing debiasing approaches can be grouped into heuristic based and model based. Heuristic-based debiasing approaches employ particular metrics such as item popularity (Saito et al. 2020) and user activeness (Pan et al. 2008) to heuristically determine the confidence of an unobserved user–item pair being negative. Despite their simplicity, these heuristics often lead to suboptimal results because the debiasing stage is disconnected from the learning process of a recommendation model. To overcome this limitation, model-based debiasing approaches are proposed by integrating a debiasing component into a recommendation model and optimizing both parts in a unified learning objective (Liang et al. 2016). However, existing model-based debiasing approaches are mainly designed for pointwise learning, but lack a viable debiasing framework based on pairwise learning. Given the widely recognized superiority of pairwise learning over pointwise learning in handling implicit feedback (Rendle et al. 2009, Wan et al. 2022), developing an unbiased pairwise learning framework is imminent.

Figure 1. Mall Floor Plans and a Customer’s Visual Scope  
![](/api/attachments/64TQ7628/fulltext/images/2fe9b57ed93b817a84ccb482e3319f2bf087fad0b821004509441f9f71620ae5.jpg)

Second, extant research concentrates primarily on digital platforms, where exposure occurs in the form of page-centric impressions (by displaying or loading items on a web page). Given the choice overload problem, the exposure likelihood of items is largely determined by the algorithmic designs of information filtering tools (particularly search engines and recommender systems), which dictate which items are featured and at what position in search or recommendation lists. However, scant attention has been paid to addressing exposure bias in physical spaces, where customers adopt the mode of pedestrian movement to explore the space and make patronage decisions. The exposure likelihood of POIs is largely determined by dynamic interactions between pedestrian movement and spatial layout. Although the role of spatial distance in recommendation effectiveness has been widely confirmed in the extant literature (Liu et al. 2013, Zhao et al. 2020), the issue of how to dynamically model pedestrian movement (in terms of position, moving direction, and visual scope) and incorporate this to reduce exposure bias remains underexplored.

To address the aforementioned research gaps, we are among the first to tackle exposure bias arising from pedestrian movement in physical recommendations. Specifically, we formulate a generalized recommendation problem, named P3M, and highlight a critical impediment—exposure bias—that hinders effective and unbiased recommendations in this setting. To address this challenge, we propose a novel recommendation approach, named unbiased movement-aware pairwise ranking (UMPR), to deliver recommendations for pedestrian customers. As illustrated in Figure 2, the proposed approach utilizes the input of floor plans and visitation sequences, and the generated recommendations can be delivered to customers through various channels, such as mobile apps, digital screens (Haynes 2021), and AI robots (Deamer 2020). The core novelties of our approach lie in integrating pedestrian movement modeling with unbiased pairwise learning. Specifically, the pedestrian movement modeling allows us to model customer movement between consecutive visits in the physical space, thus facilitating the dynamic estimation of exposure and relevance scores during the movement process. The unbiased pairwise learning framework combines classic pairwise learning with a learnable debiasing component, which is parameterized as a function of the exposure and relevance scores to gauge the probability that an unvisited POI is indeed negative. Learning model parameters in such a model-based debiasing framework is challenging, for which we develop a new alternating learning algo rithm based on stochastic gradient ascent. We theoretically analyze the effectiveness guarantees of the proposed debiasing framework for reducing training errors. Using real-world shopping mall data, we empiri cally demonstrate and analyze the superior recommendation performances of our method over classic and state of-the-art benchmark methods. In addition, we investigate how the enhanced performance translates into added monetary value and promotes recommendation fairness for multiple stakeholders.

## 2. Related Work

In this section, we first review the literature that under pins the conceptualization of exposure bias and illustrate the distinct exposure mechanism in physical spaces compared with digital platforms. Then, we summarize the two primary streams of methodological research: (1) unbiased recommendations on exposure bias and (2) spatially aware recommendations. For each stream, we review the literature, analyze key research gaps, and discuss how our method fills these gaps.

Figure 2. Our Solution Framework: From Data Source to Delivery System  
![](/api/attachments/64TQ7628/fulltext/images/c5750a8527c3a1b792ff454b7aa489ad52344042e0bb27ecceb36d763d1c34d8.jpg)

## 2.1. Conceptualization of Exposure Bias

Exposure bias refers to the systematic distortion in recommender systems resulting from nonuniform exposure distributions (Krause et al. 2024). Typically, exposure is defined as the random event of presenting an item i to an individual u in a particular context. This event raises individuals’ awareness of the item’s relevant characteristics that may impact subsequent preference assessment and interaction behaviors. Exposure bias occurs when the exposure probability P(Expose i|u, context) across all items i is nonuniformly distributed. To effectively address exposure bias, it is essential to understand the phases during which exposure occurs (i.e., exposure phases) and the underlying mechanisms that impact exposure likelihood (i.e., exposure mechanisms).

Drawing on insights in the marketing literature (Cox and Cox 2002, Bell et al. 2011), we divide the exposure of items into two main phases: prior exposure and on-spot exposure. Specifically, prior exposure occurs when individuals acquire information on a particular item before entering a platform or space. This information can be obtained from various channels, such as merchandise advertisements and peer recommendations. Generally, the more popular an item is, the more likely individuals are to become aware of the item in advance. Thus, item popularity is a widely recognized factor for measuring exposure likelihood (Pan et al. 2008, Saito et al. 2020, Damak et al. 2022). In addition, several studies have utilized online social network data to capture exposure from peer recommendations (Wang et al. 2018, Chen et al. 2019). Because individuals often share knowledge and experiences on items through social connections, items that are consumed by more social friends tend to gain greater exposure chance. Despite varying measurements and information utilized, the impact of prior exposure is generally consistent between digital platforms and physical spaces, and the methodologies for addressing this remain similar.

On-spot exposure occurs during real-time interactions within a platform or space, and it plays a significant role in affecting consumer choices and decisions (Hui et al. 2009, 2013). For instance, impulse buying, which is often triggered by on-spot exposure, constitutes a common shopping behavior, accounting for 60%–70% of purchases in physical retail (Underhill 2008). Notably, the underlying exposure mechanisms differ significantly between digital platforms and physical spaces. On digital platforms, users navigate swiftly between different webpages through pointing devices (e.g., mice, touchscreens, or joysticks). When an item is displayed or loaded on a user’s web page (referred to as an impression), this leads to potential exposure (Braun and Moe 2013). The exposure likelihood of an item varies with the viewability of its placement, such as being featured on the homepage, in frequently browsed category pages, or with a high ranking in recommendation or search lists. Given the choice overload problem on digital platforms, which items are displayed and at what positions are largely determined by the algorithmic designs of information filtering tools, particularly search engines and recommender systems. Therefore, to address exposure bias arising from system algorithms, extant research concentrates on proposing unbiased algorithms by taking specific algorithmic designs into account. For example, Damak et al. (2022) correct exposure bias in sequential recommendation approaches to avoid overly exposing items that are sequentially correlated with previous item sequences, and Kim et al. (2022) propose an unbiased graph neural network to correct exposure bias in their neighborhood aggregation process. In summary, on-spot exposure on digital platforms occurs in the form of page-centric impressions, and the likelihood of exposure largely depends on the algorithmic designs of their information filtering tools.

In contrast, customers in physical spaces adopt a unique interaction mode—pedestrian movement—to explore the space and make patronage decisions. Unlike the instantaneous transfers between webpages through pointing devices, pedestrian movements between locations in physical spaces require explicit time and physical effort. The resulting movement paths delineate how customers interact with the physical space and what they may visually observe along the path (Ghose et al. 2019, Mowrey et al. 2019). For example, POIs located along a path tend to be physically accessed, leading to potential exposure. Moreover, the exposure likelihood largely depends on the extent to which a POI can be visually observed along the path, influenced by pedestrian customers’ moving status including relative position, moving direction, and visual scope. Therefore, on-spot exposure in physical spaces occurs in the form of path-centric visual contact, and the exposure likelihood is largely influenced by the dynamic interactions between pedestrian movement and spatial layout. Table 1 compares on-spot exposure between digital platforms and physical spaces.

In this research, we focus on addressing exposure bias arising from pedestrian movement to achieve effective and unbiased recommendations in physical spaces. To this end, our methodological contributions include (1) introducing a pedestrian movement system that represents floor plans as a spatial network and reconstructs movement paths between successive visits and (2) proposing a novel set of exposure factors, including access and visibility, to characterize the likelihood of passing or seeing a POI along a path. These proposed artifacts and factors enable us to dynamically capture pedestrian movements in physical spaces and effectively quantify the exposure likelihood of POIs to pedestrian customers.

## 2.2. Unbiased Recommendations on Exposure Bias

Recommendation biases have attracted extensive research from two primary perspectives. One stream of research delves into investigating and confirming the existence of specific biases in recommender systems, such as rating bias (Lin et al. 2019), judgmental bias (Adomavicius et al. 2022), and decoy effect (Mousavi et al. 2023). The other stream involves counteracting such bias through algorithms and mechanism designs, such as graphical rating displays (Adomavicius et al. 2019) and warning messages (Xiao and Benbasat 2015). In particular, our study focuses on mitigating exposure bias in physical spaces through the development of unbiased recommendation methods. To address exposure bias, existing debiasing approaches can be grouped into heuristic based and model based.

2.2.1. Heuristic-Based Debiasing Techniques. Heuristic-Heuristic-based approaches can be further categorized as heuristic-based weighting and heuristic-based sampling, depending on whether the learning objective for a recommendation model is pointwise or pairwise. For pointwise learning, heuristic-based weighting heuristically determines the confidence that an unobserved user–item interaction is negative (Chen et al. 2023). Concretely, the more likely an item has been exposed to the user, the higher the confidence that an unobserved user–item interaction should be considered as negative feedback. To measure exposure likelihood, several factors such as item popularity (Pan et al. 2008, Saito et al. 2020, Damak et al. 2022) and user activeness (Pan et al. 2008) are employed. Although heuristic-based weighting is easy to implement, it is inefficient to include all unobserved user–item interactions in pointwise learning, given the large number of users and items in a recommendation task (Chen et al. 2019). Heuristic-based sampling for pairwise learning, discussed next, can significantly mitigate the efficiency issue.

Heuristic-based sampling randomly draws a subset of unobserved user–item interactions as negative feedback according to their probabilities of being negative (Chen et al. 2023). Given a positive item, heuristicbased sampling draws several negative items to form item pairs, and then a pairwise learning model is fitted to prioritize the positive item over the negative items. Consequently, it is crucial to identify truly negative items from the unobserved interactions to constitute informative pairs (Lian et al. 2020). Several heuristicbased sampling strategies have been developed to address this issue. For instance, Pan et al. (2008) design a popularity-based sampler to conduct the oversampling of popular items compared with less popular ones. For location recommendations, Cheng et al. (2013) and Lian et al. (2020) employ a distance-based sampler to emphasize the sampling of nearby locations, based on the assumption that nearby locations have greater exposure chance and therefore higher probabilities of being negative than distant places. Instead of assuming a specific exposure mechanism, Wan et al.

Table 1. Comparison of On-Spot Exposure Between Digital Platforms and Physical Spaces

<table><tr><td></td><td>Digital platforms</td><td>Physical spaces</td></tr><tr><td>Application domains</td><td>E-commerce platforms, content delivery platforms, social media, etc.</td><td>Shopping malls, hypermarkets, grocery stores, world expos and museums, etc.</td></tr><tr><td>Exposure mode</td><td>Page-centric impressions through pointing devices</td><td>Path-centric visual contact during pedestrian movement</td></tr><tr><td>Exposure factors</td><td>Impression: If an item is displayed or loaded on a user&#x27;s webpage, this indicates a potential exposure.Viewability: The placement of an item on a webpage greatly affects its exposure likelihood. Items featured on the homepage, in frequently browsed category pages, or with a high ranking in recommendation or search lists have greater exposure likelihood.</td><td>Access: If customers can physically reach a POI along a movement path, this indicates a potential exposure.Visibility: The extent to which a POI can be visually noticed through a path greatly affects its exposure likelihood. POIs located in more prominent locations, with larger sizes, and greater visual angles are more likely to be exposed.</td></tr><tr><td>Exposure mechanism</td><td>The exposure likelihood of items depends on the impression and viewability of item placement on a webpage, which is largely determined by algorithmic designs of information filtering tools.</td><td>The exposure likelihood of POIs is largely influenced by pedestrian movements in the physical spaces, characterized by dynamic position, moving direction, and visual scope.</td></tr><tr><td>Debiasing approaches</td><td>Extant literature has proposed various unbiased algorithms by considering specific algorithmic designs, such as sequential relevance (Damak et al. 2022) and neighborhood aggregation mechanisms (Kim et al. 2022).</td><td>This study proposes an unbiased movement-aware recommendation approach, featured with a pedestrian movement system and a novel set of exposure factors to characterize exposure likelihood.</td></tr></table>

(2022) propose a cross pairwise sampler that selectively constructs comparison pairs between several positive and negative user–item interactions to offset exposure bias in pairwise learning. In summary, regardless of the weighting or sampling strategy employed, it is hard to guarantee the effectiveness of a heuristic-based debiasing approach because the debiasing stage is disconnected from the learning process of a recommendation model.

2.2.2. Model-Based Debiasing Approaches. Unlike heuristic-based techniques, model-based debiasing approaches integrate a learnable debiasing component into the learning objective of a recommendation model to mitigate exposure bias. This debiasing component is designed to estimate the likelihood of an item being exposed to a customer, thus enabling the learning objective to treat those exposed but unobserved user–item interactions as true negative feedback. To accurately capture exposure likelihood, prior works have exploited different types of auxiliary information. For instance, Liang et al. (2016) incorporate textual information to describe user interests and characterize those items that are similar to a user’s interests as having a higher exposure likelihood. In addition, Chen et al. (2019) assume that item exposure is inevitably affected by social influence and design a personalized random walk on a social network to capture the propagation of social influence. Despite the utilization of different types of auxiliary information, existing model-based debiasing approaches are mainly designed for pointwise learning. Nevertheless, how to integrate model-based debiasing with pairwise learning remains under-investigated.

2.2.3. Key Novelties of Our Method. Our literature review, as summarized in Table 2, reveals a research gap between model-based debiasing and pairwise learning. To bridge this gap, we propose a novel debiasing framework, named unbiased pairwise learning, which deviates from existing literature in three key aspects. First, our debiasing component, which characterizes the probability that a pairwise preference relation in the training data holds true, features a unique probabilistic interpretation and offers theoretical guarantees (Propo sition 2). Second, to accurately model the debiasing component, our approach incorporates the interplay between spatial structures and pedestrian movement from multiple perspectives, including position, moving direction, and visual scope. This study pioneers in examining the mechanism of exposure bias arising from pedestrian movement and correcting this bias through a novel unbiased, movement-aware pairwise ranking approach. Third, to overcome the complexity of parameter learning associated with the model-based debiasing framework, we devise a new alternating learning algorithm based on stochastic gradient ascent to achieve effective parameter learning.

## 2.3. Spatially Aware Recommendations

Our study also relates to the stream of spatially aware recommendations, which utilize spatial information to boost recommendation effectiveness. In the following, we review representative works in two major domains, physical recommendations with pedestrian movement data and POI recommendations with check-in data, and then discuss how our study differs from existing research.

Table 2. Summary of Unbiased Recommendation Literature on Exposure Bias

<table><tr><td></td><td>Pointwise learning</td><td>Pairwise learning</td></tr><tr><td>Heuristic-based debiasing</td><td>Heuristic-based weightingItem popularity (Pan et al. 2008, Saito et al. 2020, Damak et al. 2022)User activeness (Pan et al. 2008)</td><td>Heuristic-based samplingPopularity-based sampler (Pan et al. 2008)Distance-based sampler (Cheng et al. 2013, Lian et al. 2020)Cross pairwise sampler (Wan et al. 2022)</td></tr><tr><td>Model-based debiasing</td><td>Exposure-based debiasing modelTextual information (Liang et al. 2016)Social influence (Chen et al. 2019)</td><td>Our method</td></tr></table>

2.3.1. Physical Recommendations with Pedestrian Movement Data. In contrast to the extensive recommendation research on digital platforms, physical recommendations are recently emerging within the information systems (IS) discipline, yielding various studies focusing on store recommendations in shopping malls (Ghose et al. 2019, Guo et al. 2024) and product recommendations in retail stores (Zeng et al. 2021, Shin et al. 2022). All these studies rely on the effective utilization of pedestrian movement data, such as finegrained pedestrian trajectories and discrete purchase data recorded by shopping carts, to uncover customers shopping preferences and movement patterns. A widely employed framework in existing studies is neighborhood-based collaborative filtering, which heuristically recommends items to a user based on similar users (Herlocker et al. 2002). To enhance the performance of physical recommendations, spatial features are exploited to enrich the representation of user profiles and enhance the identification of similar users. For instance, Li et al. (2017) describe a customer’s preference for an area according to the number of visits and the duration of the shopping time in that area. Ghose et al. (2019) consider spatial features such as floor levels, movement directions, and velocities to derive customer similarities. Zeng et al. (2021) develop a novel similarity measure based on shopping paths to capture the effects of temporal and spatial patterns. Despite the emphasis on spatial features, the heuristic-based collaborative filtering framework makes it hard to guarantee recommendation effectiveness due to the lack of learning objectives for parameter learning.

2.3.2. POI Recommendations with Check-in Data. Our study also relates to the popular field of POI recommendations, which focuses on exploiting users’ check-in data on location-based social networks (e.g., Foursquare and Gowalla) to predict their future check-in behaviors.

Existing research on POI recommendations can be grouped into two branches, depending on whether they capture spatial effects explicitly. Specifically, one branch of the literature adopts learning-based models (e.g., matrix factorization) to implicitly capture user preference and sequential patterns among locations. For example, Cheng et al. (2013) and Zhao et al. (2016) develop POI recommendation approaches based on the factorizing personalized Markov chains (FPMC; Rendle et al. 2010), a well-known matrix factorization technique that captures the first-order Markov transition patterns between successive check-ins. With the recent advancement of deep neural networks, various deep sequential models are proposed and applied to POI recommendations, such as gated recurrent units for recommendations (GRU4Rec; Hidasi et al. 2016) and stochastic shared embeddings with personalized transformer (SSE-PT; Wu et al. 2020). These deep sequential models are advantageous in capturing high-order nonlinear sequential dependencies but lack the ability to explicitly characterize the spatial effects that influence users’ check-in behaviors.

An alternative branch of POI recommendations explicitly captures the impact of spatial effects on users’ checkin behaviors. According to the first-law of geography that “everything is related to everything else, but near things are more related than distant things” (Tobler 1970, p. 236), the role of geographic distance has been well docu mented in the literature. For example, Ye et al. (2011) and Liu et al. (2013) find that a user’s check-in probability for a location is inversely proportional to the user’s geographical distance to that location and model this pattern with power law distributions based on matrix factorization. In addition, Zhao et al. (2020) replace the standard vanilla attention mechanism with a power-law attention mechanism in order to characterize the influence of geographic proximity on users’ check-in behaviors. Despite the various modeling architectures, existing studies generally focus on exploiting the effect of geographic distance, but are inadequate in delineating more diverse, dynamic patterns of spatial interaction.

2.3.3. Key Novelties of Our Method. Our study differs from extant research on spatially aware recommendations in two key respects. First, our study models the dynamic interactions between pedestrian customers and physical spaces from multiple aspects: position, moving direction, and visual scope. This goes beyond extant POI recommendation literature, which predominantly focuses on the single dimension of geographic distance. Second, compared with existing research on physical recommendations, our study presents a novel perspective of addressing exposure bias and making unbiased recommendations by integrating pedestrian movement. This demonstrates a stark contrast with the prior research in terms of both research objectives and methodologies for utilizing spatial information. Specifically, we introduce a network representation of the physical space, devise representative operationalizations of exposure and movement factors, and integrate these factors into a novel unbiased movement-aware recommendation approach, leading to accurate recommendation results.

## 3. Preliminaries

In this section, we define essential concepts and formulate the P3M problem. As a preliminary, we introduce a classic pairwise ranking approach for implicit-feedback recommendations and highlight two methodological gaps that should be addressed to make effective recommendations for pedestrian customers.

## 3.1. Problem Formulation

Consider a multistorey physical space I comprising the set of n POIs. Each POI i ∈ I represents a location (e.g., a store) or a facility (e.g., a shelf) that is frequently visited by customers, associated with specific spatial information (including xy coordinates and level). In this paper, we use “POI” and “location” interchangeably for convenience. The set of m customers, denoted by $U ,$ explores the space and makes patronage decisions through pedestrian movement, resulting in a collection of visitation sequences (Definition 1).

Definition 1. A customer’s visitation sequence is the sequence of temporally ordered POIs visited by the customer. Formally, let $S _ { u } = < i _ { u , 1 } , . . . , i _ { u , k } , . . . , i _ { u , | S _ { u } | } >$ represent the visitation sequence for customer $u \in U ,$ where $i _ { u , k } \in I$ represents the k-th POI visited by customer u, and $\lvert S _ { u } \rvert$ is the length of the sequence.<sup>1</sup>

In addition to individual preferences, customers patronage decisions are also influenced by the spatial layout of the POIs. Hence, we introduce floor plans (Definition 2) to capture the spatial structure of the physical spaces, which is subsequently used to delineate movement paths and spatial interactions.

Definition 2. Floor plans refer to the two-dimensional layout diagrams of physical spaces, which describe specific positions, shapes, and sizes of individual POIs, as well as the physical barriers (e.g., walls) and walkable passages (e.g., corridors and stairs) that affect pedestrian movement, as illustrated in Figure 1.

We are now ready to formulate the P3M problem in this study.

Definition 3 (P3M). Given the set of POIs I distributed in a physical space according to floor plans F, the set of customers U, and observed visitation sequences $S = \{ S _ { u } | u \in U \}$ , the objective of P3M is to recommend the most relevant POI $i ^ { * } \in I$ for each customer $u \in U$ to visit next, based on their previous visitation sequence.

## 3.2. Classic Pairwise Ranking

The P3M problem belongs to implicit-feedback recommendations (Hu et al. 2008), as the patronage behaviors are naturally generated during the movement processes rather than being explicitly labeled. For implicit-feedback recommendations, two types of learning objectives are extensively employed to learn model parameters, includ ing pointwise learning and pairwise learning. Specifi cally, pointwise learning (e.g., binary cross entropy (BCE)) captures a user’s preference for a single item by minimizing the discrepancy between the targeted and predicted relevance scores, whereas pairwise learning (e.g., Bayesian personalized ranking (BPR)) learns a user’s preference over item pairs by maximizing the difference in predicted relevance scores between positive and negative items. Unlike pointwise learning, which treats recommendations as binary classification tasks, pairwise learning is specifically designed for ranking optimization, rendering it well suited for implicit-feedback recommendations (Rendle et al. 2009, Wan et al. 2022). Furthermore, existing research has confirmed that pairwise learning shows great flexibility and effectiveness in handling rec ommendation tasks of different scales (ranging from hundreds to millions of items) and across diverse domains (both online and offline; Zhao et al. 2017, Damak et al. 2021). Therefore, we choose pairwise learning as the methodological framework of this study.

When applied to the P3M context, pairwise learning selects two locations at a time, one with positive and the other with negative feedback, and then learns a recommendation model to differentiate the relevance scores between the two locations. Given the observed patronage behaviors, where only positive feedback is recorded, a commonly adopted approach to identify negative feedback is to follow the negativity assumption by treating those unvisited locations by a customer as being negative (Pan et al. 2008, Bekker and Davis 2020). Accordingly, for each customer $u ,$ each visited location $i \in S _ { u }$ is paired with an unvisited location $j \in I \backslash S _ { u }$ to form a training data set $D _ { 0 } ,$ , defined as

$$
D _ {0} = \{(u, i, j) \in U \times I \times I | i \in S _ {u}, j \in I \setminus S _ {u} \}.\tag{1}
$$

According to the negativity assumption, each $( u , i , j ) \in$ $D _ { 0 }$ corresponds to a preference relation $i { \succ } _ { u } j$ that indicates location i is preferred over location j by customer u.

Suppose that the learned recommendation model is configured by a vector of parameters and that the estimated relevance scores for customer u regarding a pair of positive and negative locations are denoted as $r _ { u i } ( \pmb { \theta } )$ and $r _ { u j } ( \pmb { \theta } )$ , respectively. The pairwise learning problem is to find the optimal configuration of to maximize the difference between $r _ { u i } ( \pmb { \theta } )$ and $r _ { u j } ( \pmb { \theta } )$ for all $( u , i , j ) \in D _ { 0 } .$ formulated as follows:

$$
\max _ {\boldsymbol {\theta}} \sum_ {(u, i, j) \in D _ {0}} \ln \sigma (r _ {u i} (\boldsymbol {\theta}) - r _ {u j} (\boldsymbol {\theta})),\tag{2}
$$

where $\sigma ( \cdot )$ denotes the sigmoid function, that is, $\sigma ( z ) = 1 / 1 + e ^ { - z }$

The relevance scores $( \mathrm { e . g . , } r _ { u i }$ and $r _ { u j } )$ in Equation (2) can be instantiated in various forms, yielding a series of well-known recommendation models, such as BPR with matrix factorization (BPR-MF; Rendle et al. 2009), FPMC (Rendle et al. 2010), and GRU4Rec (Hidas et al. 2016). Here, we introduce the details of BPR-MF, which lays the foundation for current unbiased recommendation models (Saito et al. 2020, Damak et al. 2021). Concretely, BPR-MF employs matrix factorization techniques to map both customers and locations into a lowdimensional latent factor space and decomposes each relevance score $r _ { u i }$ using a dot product of the customer’s and location’s latent factors:

$$
r _ {u i} = \mathbf {p} _ {u} ^ {T} \cdot \mathbf {q} _ {i}, \quad \forall i \in I,\tag{3}
$$

where $ { \mathbf { p } } _ { u } \in \mathbb { R } ^ { d }$ is a vector of d-dimensional latent factors for customer $u ,$ and $\mathbf { q } _ { i } \in \mathbb { R } ^ { d }$ is a vector of d-dimensional latent factors for location i. Combining Equations (2) and (3), we obtain the BRP-MF model, which generates location recommendations for pedestrian customers based on estimated relevance scores.

Despite its wide adoption, the classic pairwise ranking approach would suffer from two limitations if directly applied to our P3M problem. First, the negativity assumption in the pairwise learning objective (Equation (2)) may lead to severe learning bias for recommender systems due to the existence of exposure bias. Because unvisited POIs are indeed a mixture of negative ones $( \mathrm { i . e . , }$ exposed but irrelevant POIs) and potentially positive ones (i.e., unexposed but relevant POIs), indiscriminately treating them as negative feedback will bias the learning of recommender systems. Second, the classic pairwise ranking approach only considers preference matching in modeling relevance scores. For example, BPR-MF models a relevance score as the dot product of user interests $( \pmb { \mathrm { p } } _ { u } )$ and item characteristics $( \mathbf { q } _ { i } ) .$ , as shown in Equation (3). However, pedestrian customers find interesting POIs on foot, thus requiring physical time and efforts. Therefore, in addition to preference matching, it is essential to capture the impact of movement costs in assessing relevance scores to make effective recommendations for pedestrian customers.

## 4. UMPR Method

In this section, we propose the UMPR method for addressing the P3M problem. First, we propose an unbiased pairwise learning objective and provide theoretical proofs of the effectiveness guarantees of the proposed learning objective. Then, we introduce a movement-aware recommendation model that incorporates the impact of pedestrian movement in modeling relevance scores. Finally, we design an alternating learning algorithm based on stochastic gradient ascent to optimize the model parameters.

## 4.1. UMPR’s Learning Objective

As follows, we first propose the framework of unbiased pairwise learning, specify the probabilistic form of the debiasing component, and provide theoretical insights for the effectiveness of the proposed framework.

4.1.1. Unbiased Pairwise Learning. On the basis of pairwise learning, we introduce two unique strategies to formulate the unbiased pairwise learning objective. The first strategy is stage segmentation by treating each visitation sequence as comprised of several stages. Concretely, we segment each visitation sequence $S _ { u }$ into $\lvert S _ { u } \rvert$ stages, with each stage $\textit { k } ( k = 1 , 2 , \ldots , \left| S _ { u } \right| )$ delineating the movement process between two succes sive visits $i _ { u , k - 1 }$ and ${ i _ { u , k } } . ^ { 2 }$ This strategy of segmenting between consecutive patronages has several desirable properties: (1) it aligns with our sequential recommendation task, which aims to predict the next POI that a customer is interested in visiting given their current position $( \mathrm { i . e . , }$ predict $i _ { u , k }$ after visiting $i _ { u , k - 1 } ) ;$ (2) it allows us to simulate customer movement in each stage and capture the dynamics of customer preferences across stages, thus facilitating more accurate estimation of exposure and relevance scores and enhanced recommendation results; and (3) this strategy is simple to implement without additional computational resources or auxiliary information. Consequently, given customer u at stage k, we represent the customer’s patronage deci sion regarding any location $i \in I$ with a binary variable $Y _ { u k i } \in \{ \bar { 0 } , 1 \}$ , where $Y _ { u k i } = 1$ if customer u visits location i at stage k and $Y _ { u k i } = 0$ otherwise. Then the condition $^ { \prime \prime } Y _ { u k i } = 1 , Y _ { u k j } = 0 ^ { \prime \prime }$ defines the pairwise relation between a visited location i and an unvisited location j for customer u at stage k. Thereby, the stage-specific training data D can be constructed as

$$
D = \{(u, k, i, j) \in U \times \mathbb {N} _ {+} \times I \times I | Y _ {u k i} = 1, Y _ {u k j} = 0, k \leq | S _ {u} | \},\tag{4}
$$

where $\mathbb { N } _ { + }$ denotes the set of positive integers. If the negativity assumption is followed, then for any $( u , k , i , j ) \in \bar { D } _ { \cdot }$ we would have the preference relation $i \succ _ { u , k } j ,$ , indicating that customer u prefers location i over location j at stage k.

The second strategy is the inclusion of the debiasing component to address the exposure bias resulting from the negativity assumption. Let $P ( i \mathord { \left. \right|} _ { u , k } j  D )$ denote the debiasing component that characterizes the probability that the preference relation $i { > } _ { u , k } j$ is true, namely, location i is preferred over location j by customer u at stage k. By integrating $P ( i \mathord { > } _ { u , k } j | D )$ into the classic pairwise learning, we formulate the unbiased pairwise learning objective L as

$$
\mathcal {L} = \sum_ {(u, k, i, j) \in D} P (i \succ_ {u, k} j | D) \ln \sigma (r _ {u k i} (\boldsymbol {\theta}) - r _ {u k j} (\boldsymbol {\theta})),\tag{5}
$$

where $r _ { u k i } ( \pmb { \theta } )$ and $r _ { u k j } ( \pmb { \theta } )$ stand for the relevance scores for customer u at stage k regarding locations i and $j ,$ respectively. The debiasing component $P ( i \mathord { \left. \right.} _ { u , k }  | \mathbf { D } )$ is used to reweight the importance of the preference relation $i \succ _ { u , k } j$ to be considered in the learning objective. When $P ( i \mathord { > } _ { u , k } j | D )$ is close to one, the underlying preference relation tends to be correct. Thus, the learning model will emphasize differentiating between the relevance scores $r _ { u k i } ( \pmb { \theta } )$ and $r _ { u k j } ( \pmb { \theta } )$ . Conversely, when the probability $P ( i \mathord { \left. \right.} _ { u , k }  | \ r { D } )$ approaches zero, the underlying preference relation is inclined to be erroneous. As a result, the learning model tends to ignore this relation in the learning objective, preventing exposure bias.

4.1.2. Debiasing Component. We next specify the probabilistic form of the debiasing component based on the data generation process. Drawing on the unbiased recommendation literature (Saito et al. 2020, Damak et al. 2021), the generation of each patronage behavior $Y _ { u k i }$ can be decomposed into two processes: exposure and relevance assessment. Specifically, we represent the outcome of exposure using the binary variable $O _ { u k i } \in \{ 0 , 1 \}$ , where $O _ { u k i } = 1$ if customer u has been exposed to location i at stage k and $O _ { u k i } = 0$ otherwise. Similarly, we describe the result of relevance assessment with the binary variable $R _ { u k i } \in \{ 0 , 1 \}$ , where $R _ { u k i } =$ 1 if customer u considers location i as being relevant to their preference at stage k and $R _ { u k i } = \dot { 0 }$ otherwise. Hence, the data generation process for a patronage behavior $Y _ { u k i }$ is

$$
\begin{array}{c} {P (Y _ {u k i} = 1) = P (O _ {u k i} = 1) \times P (R _ {u k i} = 1),} \\ {Y _ {u k i} = O _ {u k i} \times R _ {u k i}.} \end{array}\tag{6}
$$

Accordingly, an observed patronage behavior $( \mathrm { i . e . , }$ $Y _ { u k i } = 1 )$ indicates that the location is exposed $( \mathrm { i . e . , }$ $O _ { u k i } = 1 )$ and relevant $( \mathrm { i . e . , ~ } R _ { u k i } = 1 )$ to customer u at stage k, whereas an unobserved patronage behavior $( \mathrm { i . e . , ~ } Y _ { u k i } = 0 )$ could be the result of nonexposure (i.e., $O _ { u k i } = 0 )$ or irrelevance $( \mathrm { i . e . , } R _ { u k i } = 0 )$

Based on the data generation process, we define $P ( i \mathord { \left. \right|} _ { u , k } j  D )$ as the probability that the relation $i \succ _ { u , k } j$ holds in D, which is equivalent to the fact that location i is relevant and location j is irrelevant, as given by

$$
\begin{array}{r l} & P (i > _ {u, k} j | D) := P (R _ {u k i} = 1 \land R _ {u k j} = 0 | D) \\ & \qquad = P (R _ {u k i} = 1 | Y _ {u k i} = 1) \times P (R _ {u k j} = 0 | Y _ {u k j} = 0). \end{array}\tag{7}
$$

Derivation of the second step in Equation (7) is provided in Online Appendix A. Based on the commonly adopted assumption in implicit-feedback recommendations that observed user–item interactions reflect positive preferences (Pan et al. 2008, Rendle et al. 2009, Saito et al. 2020), we can establish $P ( R _ { u k i } = 1 | Y _ { u k i } = 1 ) =$ 1 and $P ( Y _ { u k j } = 0 | R _ { u k j } = 0 ) = 1$ . By incorporating this into Equation (7), we can further derive that

$$
\begin{array}{r l} & P (i > _ {u, k} j | D) = P (R _ {u k j} = 0 | Y _ {u k j} = 0) \\ & \qquad = \frac {P (R _ {u k j} = 0) \times P (Y _ {u k j} = 0 | R _ {u k j} = 0)}{P (Y _ {u k j} = 0)} \\ & \qquad = \frac {1 - P (R _ {u k j} = 1)}{1 - P (O _ {u k j} = 1) \times P (R _ {u k j} = 1)}. \end{array}\tag{8}
$$

From Equation (8), we know that the debiasing component $P ( i \mathord { > } _ { u , k } j | D )$ characterizes the probability that an unvisited POI is negative $( \mathrm { i . e . , ~ } \ \hat { P } ( R _ { u k j } = 0 | \ \dot { Y } _ { u k j } = 0 ) ) .$ which involves two extreme cases. On the one hand, if $P ( O _ { u k j } = 1 ) = 1$ , we have $P ( R _ { u k j } = 0 | Y _ { u k j } = 0 ) = 1$ , which suggests that exposed but unvisited POIs are definitely negative. On the other hand, if $P ( O _ { u k j } = 1 ) = 0 .$ , then $P ( \bar { R } _ { u k j } = 0 | Y _ { u k j } = 0 ) = 1 - P ( R _ { u k j } = 1 )$ ), which indicates that unexposed POIs could be negative or potentially positive, depending on their relevance probabilities. By integrating the relevance term, our method can accurately identify negative feedback even in circumstances with incomplete knowledge of exposure. For instance, prior exposure through marketing channels and pee recommendations may be unobservable, resulting in an inaccurate estimation of $P ( O _ { u k j } = 1 ) = 0$ . In such a situation, the efficacy of our debiasing approach still sustains if the relevance term is correctly estimated based on visi tation data.<sup>3</sup> In summary, the proposed debiasing component benefits from the integration of exposure and relevance probabilities, facilitating accurate identification of true negative feedback from unobserved interactions to achieve unbiased pairwise learning.

4.1.3. Theoretical Insights. We show theoretical guarantees regarding the effectiveness of the two strategies in the unbiased pairwise learning. First, the stage segmentation strategy allows us to build preference relations within each stage, as shown in Equation (4). Because of the prominent feature of preference dynamics $( \mathrm { e . g . } )$ , multipurpose shopping in a single trip; Leszczyc et al. 2004), customers may switch to a different purpose when proceeding to a new stage (see details in Online Appendix B). Thus, without stage segmentation, building preference relations across stages may lead to overclaimed errors (Definition 4).

Definition 4. When two stages k and $k ^ { \prime }$ are associated with different purposes, the preference relation $i \succ _ { u , k } j$ is defined as an overclaimed error for customer u at stage $k { \mathrm { ~ i f ~ } } i = i _ { u , k ^ { \prime } }$ is the visited POI at stage $k ^ { \prime } \left( k ^ { \prime } \neq k \right)$ and $j \in I \backslash S _ { u }$ is a POI that is unvisited by the customer over the sequence $S _ { u }$

Second, the debiasing component $P ( i \mathord { \left. \right|} _ { u , k } j  D )$ is integrated into the classic pairwise learning objective to address exposure bias. Without the debiasing strategy, building the preference relations based on the negativity assumption would cause biased errors (Definition 5).

Definition 5. For customer u at stage $k ,$ the preference relation $i \succ _ { u , k } j$ is defined as a biased error if $\bar { Y _ { u k j } } = 0$ and $R _ { u k j } = 1$ , which indicates that the unvisited POI j is potentially positive but considered negative in the preference relation.

Based on the above definitions, we next provide theoretical results regarding the effectiveness guarantees of the two strategies in reducing training errors. Specifically, Proposition 1 quantifies the effectiveness of the stage segmentation strategy in mitigating overclaimed errors, and Proposition 2 measures the extent to which the debiasing strategy decreases biased errors.

Proposition 1. For customer $u \in U ,$ the stage segmentation strategy eliminates at least a proportion of $\frac { - ( \mid S _ { u } \mid - 1 ) ( \mid S _ { u } \mid - 2 ) \tau _ { u } ^ { 2 } + 2 ( \mid S _ { u } \mid - 1 ) ^ { 2 } \tau _ { u } } { \mid S _ { u } \mid ^ { 2 } }$ overclaimed errors from $D _ { 0 } ^ { + } =$ $\{ ( u , k , i , j ) \in U \times \mathbb { N } _ { + } \times I \times I | i \in S _ { u } , j \in I \setminus S _ { u } , k \le | S _ { u } | \}$ , where $D _ { 0 } ^ { + }$ is a stage-specific extension of $D _ { 0 }$ defined by Equation (1) and $\tau _ { u }$ stands for the probability that customer u changes purposes between adjacent stages over the sequence $S _ { u }$

Proof. See Online Appendix B for derivation details. w

Proposition 1 provides a theoretical guarantee of overclaimed error reduction by stage segmentation. To illustrate the proportion of overclaimed error reduction in Proposition 1, we plot how this proportion changes with $\tau _ { u } \in [ 0 , 1 ]$ by considering the different cases of $| S _ { u } | = 5 , 1 5 , + \infty ,$ as shown in Figure $3 ( \mathrm { a } ) . ^ { 4 }$ From this figure and our monotonic analysis in Online Appendix B, we highlight two findings. First, given $\lvert S _ { u } \rvert$ , the proportion of overclaimed error reduction increases with $\tau _ { u } ,$ which suggests that stage segmentation is more effective for customers with dynamic preferences. Second, given $\tau _ { u } ,$ , the proportion of overclaimed error reduction increases as the length $\lvert S _ { u } \rvert$ grows, indicating that the proposed unbiased pairwise learning objective better addresses learning bias for active customers with longer visitation sequences.

Proposition 2. For customer $u \in U$ at stage k, the proposed debiasing component in the learning objective eliminates a proportion $\begin{array} { r } { o f \frac { ( n - 1 - b _ { u k } ) } { ( 1 + b _ { u k } ) ( n - 1 ) } } \end{array}$ biased errors from D as defined in Equation (4), where n is the total number of POIs in the physical space and $b _ { u k }$ is the number of POIs that are exposed to but assessed irrelevant by customer u at stage k.

Proof. See Online Appendix C for derivation details. w

Proposition 2 suggests that the proposed debiasing strategy is effective in reducing biased errors. To illustrate, we plot the proportion of biased error reduction in relation to $b _ { u k }$ by considering n � 50, 100, and 500, as shown in Figure 3(b). Our findings shed theoretical light in three key respects. First, the proportion is equal $\begin{array} { r } { \mathrm { t o } \frac { 1 } { n - 1 } ( \frac { n } { 1 + b _ { u k } } - 1 ) } \end{array}$ . Given $n ,$ the proportion increases as $b _ { u k }$ decreases. By definition, $b _ { u k }$ is the number of POIs that are exposed between two successive visits but considered irrelevant by the customer. A lower $b _ { u k }$ indicates fewer irrelevant POIs at stage $k ,$ indicating a higher likelihood of more frequent visits. Thus, the debiasing strategy can better address the learning bias for active customers. Second, the proportion of biased error reduction can also be transformed to $\begin{array} { r } { \frac { 1 } { 1 + b _ { u k } } ( 1 - \frac { b _ { u k } } { n - 1 } ) } \end{array}$ Given $b _ { u k } ,$ , we can see that the proportion increases with $n ,$ which suggests that the debiasing strategy is more effective for physical spaces with a larger number of POIs. Third, it is worth noting that the proportion of biased errors is more sensitive to $b _ { u k }$ but remains relatively stable to n. For example, when fixing $b _ { u k }$ at 10, the proportion slightly decreases from 9.09% to 8.17% when n sharply decreases from 1,000,000 to 100. Therefore, even in physical spaces (e.g., malls) with fewer options (n) compared with digital platforms, addressing exposure bias is still critical to achieving effective and unbiased recommendations.

## 4.2. UMPR’s Recommendation Model

We next develop the movement-aware recommendation model based on the unbiased pairwise learning objective. As a foundation, we first build a pedestrian movement system to characterize how pedestrian customers move in the physical space. We then introduce the framework of the recommendation model and detail the factor operationalizations.

4.2.1. Pedestrian Movement System. The pedestrian movement system serves as the basis for modeling customer movement in the physical space. Within this system, we first establish a spatial network based on floor plans, then construct movement paths between successive visits based on the spatial structure, and finally delineate movement status for customer agents accordingly.

Based on the floor plans, we build a spatial network that specifies the set of accessible positions and allowable movements given each position (Afyouni et al. 2012). Formally, we represent the spatial network as an undirected graph $G = ( V , E )$ , where the nodes V denote a collection of turning points that are accessible to customer agents, and the edges E stand for walkable passages between pairs of nodes. Specifically, we define the nodes ${ \hat { V } } { \stackrel { } { = } } I \cup A ,$ , where I indicates the set of POI nodes and A denotes the set of anchor nodes that characterize the contours of obstacle areas.<sup>5</sup> The nondirectional edges are defined as $E = E ^ { S } \cup E ^ { C }$ , where $E ^ { S }$ is the set of same-level edges and $E ^ { C }$ is the set of cross-level edges. Given a threedimensional coordinate system, the spatial position for node $v \in V$ is recorded as coordinates $( \delta _ { x } , \delta _ { y } , \delta _ { z } )$ , in which $\delta _ { x } ( v )$ and $\delta _ { y } ( v )$ denote the x and y coordinates of node v on level number $\delta _ { z } ( v )$ . Details about the spatial network construction are given in Online Appendix D.

Figure 3. (Color online) Overclaimed and Biased Error Reduction  
![](/api/attachments/64TQ7628/fulltext/images/b95dfd37ec28153811eb861270a0e1bc73ae2e0b398be0b3e73c0b5cb3d8dfea.jpg)

Given the structure of the spatial network, we connect movement paths between successive visits to characterize the trajectory along which a customer agent moves in the spatial network. Given a source node $v _ { s }$ and a target node $v _ { t }$ from $V ,$ the movement path $\mathcal { P } ( v _ { s } , v _ { t } )$ is a sequence of adjacent nodes that are joined by edges in the spatial network. Formally, we define a movement path as $\mathcal { P } ( v _ { s } , v _ { t } ) = ( v _ { 1 } , v _ { 2 } , \ldots , v _ { \mid \mathcal { P } \mid } ) ,$ where $v _ { s } = v _ { 1 } , \quad v _ { t } = v _ { \left| \mathcal { P } \right| } ,$ and there are edges $( v _ { h } , v _ { h + 1 } ) \in E$ for $h = 1 , 2 , \ldots , | \mathcal { P } | - 1$ . Movement paths provide viable information for analyzing the spatial context in which customers compare POIs, assess movement costs, and ultimately make patronage decisions (Hui et al. 2009). In this research, we adopt the widely recognized shortest path assumption, described below, to simulate movement paths between successive visits.

Assumption 1 (Shortest Path Assumption). Pedestrian agents are assumed to take the shortest path between two successive visits to minimize movement costs, as suggested by the pedestrian movement literature (Farley and Ring 1966, Zhu and Timmermans 2008).

![](/api/attachments/64TQ7628/fulltext/images/5abf53618ef086bbb7d6afab940e8d694ff24254f9abec549f788201449e7abc.jpg)

For customer agents moving along a movement path, we delineate their movement status with three elements, namely position, moving direction, and visual scope. To illustrate, Figure 4 shows a customer agent at position v with moving direction $\vec { d }$ and visual scope ϑ. We extract the movement status following the agentbased movement assumption outlined below.

Assumption 2 (Agent-Based Movement Assumption). We assume that pedestrians move along the edges of the spatia network, with their moving direction $\vec { d }$ aligned with the edge and a visual scope of $\vartheta / 2$ on each side of ${ \vec { d } } . ^ { 6 }$ The assumption aligns with the literature on space syntax–based agent simulation (Penn and Turner 2002, Afyouni et al. 2012).

Based on the steps described above, we construct movement paths between successive visits and obtain multidimensional movement status for customer agents. This enriched movement information facilitates effective training of our movement-aware recommendation model, introduced below.

Figure 4. Customer Agent  
![](/api/attachments/64TQ7628/fulltext/images/44fccf8995d801358ea814692fd19b8e5b5ab6fdf4780e96694a2dd510848902.jpg)

4.2.2. Model Framework. Having established the pedestrian movement system, we next propose the movement-aware recommendation model. According to Equations (5) and (8), achieving the unbiased pairwise learning necessitates effective modeling of exposure and relevance probabilities. By leveraging the sigmoid function $\sigma ( \cdot )$ , we establish their proportional relationships with the corresponding exposure and relevance scores $( \mathrm { i . e . , } o _ { u k i }$ and $r _ { u k i } )$ as follows:

$$
\begin{array}{r l} & P (O _ {u k i} = 1) = \sigma (o _ {u k i}), \\ & P (R _ {u k i} = 1) = \sigma (r _ {u k i}), \quad \forall i \in I. \end{array}\tag{9}
$$

The exposure score $o _ { u k i }$ captures the propensity that a physical location i has been exposed to customer u at stage k. The likelihood of exposure depends on the location’s spatial relationships in relative to the customer’s movement process. Given the movement path $\mathcal { P } ( i _ { u , k - 1 } ,$ $i _ { u , k } )$ at stage $k ,$ we model the exposure score $o _ { u k i }$ as a linear weighted sum of its exposure factors $\mathbf { x } _ { u k i }$ , as given by

$$
o _ {u k i} = \pmb {\rho} ^ {T} [ 1; \mathbf {x} _ {u k i} ], \quad \forall i \in I,\tag{10}
$$

where $\mathbf { x } _ { u k i } = [ A C _ { u k i } , V S _ { u k i } , P O _ { i } ] ^ { T }$ is the vector of exposure factors. The details on extracting $\mathbf { x } _ { u k i }$ are provided in Section 4.2.3. The real-valued parameter vector $\pmb { \rho } ^ { T } =$ $[ \rho _ { 0 } , \rho _ { 1 } , \rho _ { 2 } , \rho _ { 3 } ]$ is learned from the data.

The relevance score $r _ { u k i }$ reflects the extent to which location i is relevant to customer u at stage k. A pedestrian customer evaluates the relevance score by considering the degree to which the location satisfies their interests and the pedestrian cost of moving to that location (Hoogendoorn and Bovy 2004). In this light, we model the relevance score $r _ { u k i }$ as a tradeoff between the benefits of preference matching $( b _ { u k i } )$ and the costs of pedestrian movement $\left( c _ { u k i } \right)$ , as given by

$$
r _ {u k i} = b _ {u k i} - c _ {u k i}, \quad \forall i \in I.\tag{11}
$$

For the benefit term $b _ { u k i }$ , we consider customer u’s global preferences as well as their local interests. Global preferences are associated with individual customers and remain relatively stable across trips, whereas local interests reflect current purposes and dynamically change during a trip. Inspired by Rendle et al. (2010), we represent the local interests as reflected by the customer’s last patronage, that is, $l = i _ { u , k - 1 } \in I$ . Hence, the benefit term $b _ { u k i }$ can be formulated as

$$
b _ {u k i} = \mathbf {p} _ {u} ^ {T} \cdot \mathbf {q} _ {i} + \mathbf {z} _ {l} ^ {T} \cdot \mathbf {q} _ {i}, \quad \forall i \in I,\tag{12}
$$

where $\boldsymbol { \mathsf { p } } _ { u } \in \mathbb { R } ^ { d }$ is the global preference vector for customer $u \in U , \mathbf { q } _ { i } \in \mathbb { R } ^ { d }$ is the latent feature vector for location $i \in I ,$ and $\mathbf { z } _ { l } \in \mathbb { R } ^ { d }$ is the local interest vector represented by customer u’s last patronage l. Hence, the first term $( \mathbf { \dot { p } } _ { u } ^ { T } \cdot \mathbf { q } _ { i } )$ measures the impact of global preferences, whereas the second term $( \mathbf { z } _ { l } ^ { T } \cdot \mathbf { q } _ { i } )$ captures the effect of the local interests. All the latent factors $\mathbf { P } = [ \mathbf { p } _ { u } ] _ { u \in U } \in \mathbb { R } ^ { m \times d } , \ \mathbf { Q } = [ \mathbf { q } _ { i } ] _ { i \in I } \in \mathbb { R } ^ { n \times d }$ , and ${ \mathbf Z } = [ { \mathbf z } _ { l } ] _ { l \in I } \in$ R<sup>n×d</sup> are learned from the data.

In addition to preference matching, we innovatively model the movement cost $c _ { u k i }$ , which is crucial for pedestrian customers’ relevance assessment. For different patronage decisions, the associated movement cost may vary with the walking distance, the number of directional changes, and/or the degree of uncertainty and risk in the movement process (Antonini et al. 2006, Robin et al. 2009). Accordingly, we formulate the movement cost $c _ { u k i }$ as a linear weighted sum of movement factors $\mathbf { m } _ { u k i }$ , as given by

$$
c _ {u k i} = \pmb {\omega} ^ {T} \cdot \mathbf {m} _ {u k i}, \quad \forall i \in I,\tag{13}
$$

where $\mathbf { m } _ { u k i } = [ D S _ { u k i } , L D _ { u k i } , D D _ { u k i } , I V _ { u k i } , D T _ { u k i } ] ^ { T }$ is the vector of movement factors. The details on extracting $\mathbf { m } _ { u k i }$ are presented in Section 4.2.4. The real-valued parameter vector $\pmb { \omega } ^ { T } = [ \omega _ { 1 } , \omega _ { 2 } , \omega _ { 3 } , \omega _ { 4 } , \omega _ { 5 } ]$ is learned from the data.<sup>7</sup>

4.2.3. Exposure Factors. The exposure factors $\mathbf { x } _ { u k i }$ in Equation (10) are used to characterize the possibility to which a pedestrian customer becomes aware of a target POI at a particular stage. As illustrated in Section 2.1, exposure occurs in two primary phases, including on-spot exposure (determined by pedestrian movement) and prior exposure (correlated with popularity). Accordingly, we identify three representative exposure factors, including Access (AC), Visibility (VS), and Popularity (PO).

Exposure can occur if a target POI is physically accessed along a customer’s movement path. We use the binary variable Access (AC) to indicate whether it is located on the movement path. Given the movement path $\mathcal { P } ( i _ { u , k - 1 } , i _ { u , k } )$ for customer u at stage $k ,$ we set $A C _ { u k i } = 1$ if location i is included in $\mathcal { P } ( i _ { u , k - 1 } , i _ { u , k } ) .$ , and $A C _ { u k i } = 0$ otherwise. Physical access $( \mathrm { i . e . , ~ } A C _ { u k i } = 1 )$ indicates that the customer comes into close proximity with the POI along the path and is thus very likely aware of this location.

Besides physical access, a POI may catch a customer’s attention through visual contact. Thus, we propose a measure Visibility (VS) to quantify how well a customer agent can see the POI in their visual scope. As illustrated in Figure 5, the visual angle α to which a POI extends into a human’s visual scope is an effective measurement of visibility (Lu and Seo 2015). Using the maximal value of α over the path $\mathcal { P } ( i _ { u , k - 1 } , i _ { u , k } )$ , we calculate the visibility of location i to customer u at stage k as

$$
V S _ {u k i} = \max _ {(v _ {h}, v _ {h + 1}) \in \mathcal {P} (i _ {u, k - 1}, i _ {u, k})} \frac {\alpha (v _ {h} , \vec {d} (v _ {h} , v _ {h + 1}) , i)}{\vartheta}.
$$

When customer u moves along the edge $( v _ { h } , v _ { h + 1 } )$ $\in \mathcal { P } ( i _ { u , k - 1 } , i _ { u , k } )$ , we denote the visual angle of location i as $\alpha ( v _ { h } , \dot { d } ( v _ { h } , v _ { h + 1 } ) , i )$ , where $v _ { h }$ is the starting node of this edge and $\vec { d } ( v _ { h } , v _ { h + 1 } )$ is the moving direction from $v _ { h }$ to $v _ { h + 1 }$ . The maximal visual scope ϑ is used to normalize visibility in the range [0, 1]. Specifically, $V S _ { u k i }$ equals one when the visual angle reaches $\vartheta$ for at least one node of $\mathcal { P } ( i _ { u , k - 1 } , i _ { u , k } )$ , and it equals zero if the target POI is totally outside the visual scope along the path. We set the visual angle $\alpha = 0 \mathrm { i f } v _ { h }$ and i are located on different levels.

Figure 5. Visual Angle for a Target POI  
![](/api/attachments/64TQ7628/fulltext/images/96773bf70da3e45177b7872d07884af37deea03b33da4960c3d74ee8fdb97539.jpg)

In addition to on-spot exposure, customers may also become aware of a POI through prior knowledge, such as merchandise advertisements and peer recommendations (Bell et al. 2011, Chen et al. 2019). To capture this effect, we adopt the widely used factor, Popularity $( P O ) ,$ as a proxy because popular POIs are more likely to be noticed than less popular ones (Damak et al. 2022). The measure $P O _ { i }$ is calculated as the average number of visits for POI i in a given period (e.g., a month).<sup>8</sup>

4.2.4. Movement Factors. The movement factors $\mathbf { m } _ { u k i }$ in Equation (13) are used to characterize the cost of walking to a target POI along a movement path. We identify a representative set of movement factors from the three aspects: position, moving direction, and visual scope.

Regarding position, it is widely acknowledged that, all else being equal, customers are less likely to visit distant locations because of higher movement costs (Raghubir and Krishna 1996, Timmermans 2004). Therefore, we propose the measure Distance (DS) to account for how far a pedestrian customer is from a target POI. Formally, we calculate $D S _ { u k i }$ using the Euclidean distance of the movement path $\mathcal { P } ( i _ { u , k - 1 } , i ) ;$

$$
D S _ {u k i} = \sum_ {(v _ {h}, v _ {h + 1}) \in \mathcal {P} (i _ {u, k - 1}, i)} d i s t (v _ {h}, v _ {h + 1}),\tag{14}
$$

where $d i s t ( v _ { h } , v _ { h + 1 } )$ is the Euclidean distance of edge $( v _ { h } , v _ { h + 1 } )$ in the movement path, computed as dist $( v _ { h } , v _ { h + 1 } ) = \sqrt { ( \delta _ { x } ( v _ { h + 1 } ) - \delta _ { x } ( v _ { h } ) ) ^ { 2 } + ( \delta _ { y } ( v _ { h + 1 } ) - \delta _ { y } ( v _ { h } ) ) ^ { 2 } } .$ . In addition to the distance on the same level, we adopt a measure Level Difference (LD), calculated as $L D _ { u k i } =$ $| \delta _ { z } ( i ) - \delta _ { z } ( i _ { u , k - 1 } ) |$ , to account for the cross-level transition efforts between different levels.

Regarding moving direction, it has been widely confirmed that pedestrians tend to maintain their moving direction, instead of making frequent directional changes (Antonini et al. 2006, Robin et al. 2009). Hence, a patronage decision that requires a larger directional change incurs higher movement costs and is thus less preferred by pedestrian customers. Accordingly, we propose a measure Directional Difference (DD) to gauge how much a target moving direction $( \mathrm { i . e . } ,$ , the moving direction to a target POI) deviates from a customer’s current moving direction. Given customer u at stage k and the target POI $i ,$ we compute the Directional Differ ence $D D _ { u k i }$ <sub>i</sub> as

$$
D D _ {u k i} = \arccos (\vec {d} (i _ {u, k - 1}, i), \vec {d} (v _ {u, k - 1} ^ {-}, i _ {u, k - 1})),\tag{15}
$$

where $\vec { d } ( i _ { u , k - 1 } , i )$ is the target moving direction from the current position $i _ { u , k - 1 }$ to the target POI $i ,$ and $d ( v _ { u , k - 1 } ^ { - } ,$ $i _ { u , k - 1 } )$ ) is the current moving direction from $v _ { u , k - 1 } ^ { - }$ to $i _ { u , k - 1 }$ . Here, $v _ { u , k - 1 } ^ { - }$ denotes the node that lies before $i _ { u , k - 1 }$ on the movement path $\mathcal { P } ( i _ { u , k - 2 } , i _ { u , k - 1 } )$ , and thus $( v _ { u , k - 1 } ^ { - } , i _ { u , k - 1 } )$ is the last edge in the movement path $\mathcal { P } ( i _ { u , k - 2 } , i _ { u , k - 1 } )$ . According to Equation (15), a larger angle indicates that more effort needs to be exerted to change the current moving direction to visit a target location.

Regarding visual scope, pedestrian customers can assess the style and offerings of a target POI based on visual judgments (e.g., based on window designs). However, for a target POI outside of a customer’s visual scope, the patronage decision tends to incur higher uncertainty and risk, thus increasing the movement cost. Therefore, we propose Invisibility (IV) to capture the extent to which a target POI is invisible to a pedestrian customer. Given the movement path $\mathcal { P } ( i _ { u , k - 1 } , i ) .$ we compute invisibility $I V _ { u k i }$ using the average of the invisibilities along the path, as given by

$$
\begin{array}{c} I V _ {u k i} = \frac {1}{| \mathcal {P} (i _ {u , k - 1} , i) | - 1} \sum_ {(v _ {h}, v _ {h + 1}) \in \mathcal {P} (i _ {u, k - 1}, i)} \\ \left(1 - \frac {\alpha (v _ {h} , \vec {d} (v _ {h} , v _ {h + 1}) , i)}{\vartheta}\right). \end{array}\tag{16}
$$

When customer u moves along edge $( v _ { h } , v _ { h + 1 } ) \in$ $\mathcal { P } ( i _ { u , k - 1 } , i )$ , we measure the invisibility of POI i as $1 - \alpha ( v _ { h } , \vec { d } ( v _ { h } , v _ { h + 1 } ) , i ) / \vartheta$ . According to Equation (16), $I V _ { u k i }$ ranges over [0, 1]; it equals zero if the target POI always has the maximal visual angle along the entire movement path $( \mathrm { i . e . , ~ } \ \alpha ( \boldsymbol { v } _ { h } , \vec { d } ( \boldsymbol { v } _ { h } , \boldsymbol { v } _ { h + 1 } ) , i ) = \vartheta )$ , and it reaches one if the target POI is located totally outside of the customer’s visual scope $( \mathrm { i . e . , } \alpha ( v _ { h } , \vec { d } ( v _ { h } , v _ { h + 1 } ) , i ) = 0 )$

In addition to the impact of the target POI, we further account for the disturbing effect cast by other visible

POIs along the movement path. Customers may be attracted by those POIs and give up their planned route (Kłeczek and Wa˛s 2014). Therefore, we propose Distraction (DT) to quantify such dropout risk as a movement cost. In analogy to the force of gravity, we calculate the attraction of a given POI as positively proportional to its popularity and negatively proportional to the square of its distance to the customer’s current position (Gibson and Pullen 1972). Hence, the distraction $D T _ { u k i }$ for customer u who is moving along the path $\mathcal { P } ( i _ { u , k - 1 } , i )$ is computed as

$$
D T _ {u k i} = \sum_ {v _ {h} \in \mathcal {P} (i _ {u, k - 1}, i) \backslash i} \max _ {j \in J (v _ {h}) \backslash i} \frac {P O _ {j}}{d i s t (v _ {h} , j) ^ {2}},\tag{17}
$$

where $J ( v _ { h } )$ denotes the set of POIs that are visible to customer u at node $v _ { h } \in \mathcal { P } ( i _ { u , k - 1 } , i ) \setminus i .$ . The attraction power of a visible POI $j \in J ( v _ { h } ) \setminus i$ is measured as $P O _ { j } / d i s t ( v _ { h } , j ) ^ { 2 }$ , in accordance with the force of gravity. In Equation (17), we consider that a customer is likely to be distracted at each node $v _ { h }$ along the path $\mathcal { P } ( i _ { u , k - 1 } , i )$ , and such distraction can be attributed to the most attractive POI in the visible set $J ( v _ { h } )$

## 4.3. UMPR’s Model Learning

In this section, we introduce how to find the optimal configuration of model parameters for UMPR. Based on the unbiased learning objective (Equation (5)) and the modeling of relevance scores (Equations (11)–(13)), the learning problem we need to solve is formulated as

$$
\max _ {\boldsymbol {\theta}} \mathcal {L} (\boldsymbol {\theta}) = \max _ {\boldsymbol {\theta}} \sum_ {(u, k, i, j) \in D} P (i \succ_ {u, k} j) \ln \sigma \left(r _ {u k i} (\boldsymbol {\theta}) - r _ {u k j} (\boldsymbol {\theta})\right),\tag{18}
$$

where $\pmb { \theta } = ( \mathbf { P } , \mathbf { Q } , \mathbf { Z } , \pmb { \omega } )$ denotes the set of relevancerelated parameters, and $r _ { u k i } ( \pmb \theta ) = \mathbf p _ { u } ^ { T } \cdot \mathbf q _ { i } + \mathbf z _ { l } ^ { T } \cdot \mathbf q _ { i } - \pmb \omega ^ { T } \cdot \mathbf m _ { u k i }$ The learning problem is to find the optimal configuration <sup>∗</sup> that maximizes L. If the values of $P ( i \succ _ { u , k } \bar { j } )$ are provided, we can easily obtain the optimal <sup>∗</sup> that maximizes $\mathcal { L }$ using the stochastic gradient ascent (SGA) algorithm (Hastie et al. 2009). The procedure for estimating is given in Algorithm 1, where the input parameter $\pmb { \theta } ^ { ( 0 ) }$ is the initialization of and $\mathbb { P } =$ $\mathsf { \widehat { \{ P ( i \succ _ { u , k } j ) | } }  ( u , k , i , j ) \in D \}$ denotes the set of debiasing components. The algorithm first constructs the learning objective $\mathcal { L }$ based on the provided debiasing component P (line 2) and then iteratively updates parameters $\pmb { \theta } ^ { ( t ) }$ toward the direction of the gradient for a randomly drawn data sample (lines 3–6). Finally, the algorithm outputs the learned parameters ${ \pmb \theta } ^ { * }$ . A more detailed description of Algorithm 1, including the updating formulas for each dimension of the parameter in (i.e., $p _ { u f } ,$ $q _ { i f } , q _ { j f } , z _ { l f }$ , and ω ), is presented in Online Appendix E.

Algorithm 1 (Relevance\_Params\_Learner $( \pmb \theta ^ { ( 0 ) } , \mathbb { P } ) )$

1: Initialize training data D, learning rate $\eta _ { 1 }$ , number of iterations $T _ { 1 }$

2: Construct $\mathcal { L } ( \pmb { \theta } )$ with D and P based on Equation (18)

3: for $t = 1 , 2 , \ldots , T _ { 1 }$ do

4: Draw a data sample $\xi = ( u , k , i , j )$ uniformly from D

5: $\pmb { \theta } ^ { ( t ) } \gets \pmb { \theta } ^ { ( t - 1 ) } + \eta _ { 1 } \nabla \mathcal { L } ( \pmb { \theta } ^ { ( t - 1 ) } , \xi )$

6: end for

7: ${ \pmb \theta } ^ { * } = { \pmb \theta } ^ { ( T _ { 1 } ) }$

8: return $\pmb { \theta } ^ { \ast }$

Algorithm 1 learns the model parameters $\pmb { \theta } ^ { * }$ when the debiasing component P is provided. A natural question is how to ensure that $\mathbb { P }$ is estimated accurately. According to Equations (8) and (9), the debiasing component is formulated as

$$
P (i > _ {u, k} j) = \frac {1 - \sigma (r _ {u k j} (\pmb {\theta} ^ {*}))}{1 - \sigma (o _ {u k j} (\pmb {\rho})) \sigma (r _ {u k j} (\pmb {\theta} ^ {*}))}.\tag{19}
$$

Hence, an accurate estimation of debiasing components depends on a well-estimated parameter . Recalling the data generation process in Equation (6), we appoint a pointwise learning objective $\hat { \mathcal { L } } ^ { \prime }$ to maximize the likelihood of the data, expressed as max $\mathcal { L } ^ { \prime } = \mathrm { m a x } \sum _ { ( u , k , i , j ) \in D }$ ln $P ( Y _ { u k i } = 1 ) + \ln P ( \bar { Y } _ { u k j } = 0 )$ . Based on Equations (6) and (9), the learning objective $\mathcal { L } ^ { \prime }$ can be further derived as

$$
\begin{array}{c} \mathcal {L} ^ {\prime} (\boldsymbol {\rho}) = \sum_ {(u, k, i, j) \in D} [ \ln \sigma (o _ {u k i} (\boldsymbol {\rho})) + \ln \sigma (r _ {u k i} (\boldsymbol {\theta} ^ {*})) \\ \qquad + \ln (1 - \sigma (o _ {u k j} (\boldsymbol {\rho})) \times \sigma (r _ {u k j} (\boldsymbol {\theta} ^ {*}))) ]. \end{array}\tag{20}
$$

Similar to Algorithm 1, we can employ the standard SGA algorithm to find the optimal configuration of $\pmb { \rho } ^ { * }$ that maximizes $\mathcal { L } ^ { \prime }$ . The detailed procedure is given in Algorithm 2, which requires $\pmb { \theta } ^ { \ast }$ as the input parameter and returns the debiasing component $\mathbb { P } ^ { * }$ as the output. Compared with the provided debiasing component $\mathbb { P } ,$ the output $\mathbb { P } ^ { * }$ is considered to be a more accurate estimation because the parameter $\pmb { \rho } ^ { * }$ for calculating P<sup>∗</sup> has been optimized according to the data generation process.

Algorithm 2 (Debiasing\_Weight\_Corrector( ))

1: Initialize $\pmb { \rho } ^ { ( 0 ) }$ , training data $D ,$ learning rate $\eta _ { 2 } ,$ number of iterations $T _ { 2 }$

2: Construct $\mathcal { L } ^ { \prime } ( \pmb { \rho } )$ with D and based on Equation (20)

3: for $t = 1 , 2 , \ldots , T _ { 2 }$ do

4: Draw a data sample $\xi = ( u , k , i , j )$ uniformly from D

5: $\pmb { \rho } ^ { ( t ) }  \pmb { \rho } ^ { ( t - 1 ) } + \eta _ { 2 } \nabla \mathcal { L } ^ { \prime } ( \pmb { \rho } ^ { ( t - 1 ) } , \xi )$

6: end for

7: $\pmb { \rho } ^ { * } = \pmb { \rho } ^ { ( T _ { 2 } ) }$

8: Compute $\mathbb { P } ^ { * } = \{ P ( i > _ { u , k } j ) | ( u , k , i , j ) \in D \}$ with Equation (19)

9: return $\mathbb { P } ^ { * }$

Based on Algorithms 1 and 2, we are now ready to introduce the main learning algorithm for UMPR. Each of the two algorithms has a distinct focus for parameter learning. To be specific, Algorithm 1 (Relevance\_Params\_Learner) is responsible for learning the parameters in relevance scores when the debiasing component P is provided. On the other hand, Algorithm 2 (Debiasing\_Weight\_Corrector) is capable of correcting the estimation of P by using the parameters as input. Hence, the two learning algorithms are interdependent and can provide mutual enhancement in learning parameters, which motivates us to design an alternating learning algorithm based on the stochastic gradient ascent (Lei et al. 2017).

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 3 (UMPR-ASGA)
1: Initialize  $\boldsymbol{\theta}^{(0)}$ ,  $\mathbb{P}^{(0)} = 1$ ,  $t \leftarrow 0$ , and predefined threshold  $\epsilon$ 
2: repeat
3:  $t \leftarrow t + 1$ 
4:  $\boldsymbol{\theta}^{(t)} = \text{Relevance\_Params\_Learner}(\boldsymbol{\theta}^{(t-1)}, \mathbb{P}^{(t-1)})$ 
5:  $\mathbb{P}^{(t)} = \text{Debiasing\_Weight\_Corrector}(\boldsymbol{\theta}^{(t)})$ 
6: until  $\|\boldsymbol{\theta}^{(t)} - \boldsymbol{\theta}^{(t-1)}\| &lt; \epsilon$ 
7:  $\boldsymbol{\theta}^{*} = \boldsymbol{\theta}^{(t)}$ 
8: return  $\boldsymbol{\theta}^{*}$
</div>

Algorithm 3 shows the alternating SGA (ASGA) algorithm for UMPR. The algorithm first initializes all debiasing components with $\mathbf { \mathbb { P } } ^ { ( 0 ) } = 1$ (line 1). Then the algorithm alternates between Relevance\_Params\_Learner (line 4) and Debiasing\_Weight\_Corrector (line 5). In each round $t ,$ Relevance\_Params\_Learner optimizes the learning objective L to update the parameters $\mathbf { \pmb { \theta } } ^ { ( t ) }$ . Then Debiasing\_Weight\_Corrector uses $\pmb { \theta } ^ { ( t ) }$ as input and updates $\breve { \pmb { \rho } } ^ { ( t ) }$ to correct the estimation of the debiasing components P<sup>(t)</sup>. As the alternating rounds of the algorithm proceed, the debiasing component will be estimated more accurately, which further enhances the learning of through the proposed unbiased pairwise learning. Finally, the algorithm outputs the optimal configuration $\pmb { \theta } ^ { \ast }$ upon convergence.

With the best configured parameters ${ \pmb { \theta } } ^ { * } ,$ , we generate recommendations for each customer based on the estimated relevance scores. Given customer u at stage k and a target POI $i \in I \backslash i _ { u , k - 1 } $ , we first extract movement factors $\mathbf { m } _ { u k i }$ based on the movement path $\mathcal { P } ( i _ { u , k - 1 } , i )$ and then compute the relevance score $r _ { u k i } ( \pmb { \theta } ^ { * } )$ . For any customer $u \in U$ and all candidate POIs in the physical space, the top N recommendations with the highest relevance scores are presented to the customer.

## 5. Empirical Evaluation

In this section, we introduce the data set and evaluation procedure. Then we evaluate the recommendation performance of our method compared with state-of-the-art methods. In addition to benchmarking, we further analyze the contribution of each model component to the overall performance of our method. Furthermore, we examine how our method boosts economic returns and enhances recommendation fairness.

## 5.1. Data and Evaluation Procedure

To evaluate the performance of our method in providing physical recommendations, we focus on a salient context in P3M—shopping malls—to offer personalized store recommendations for pedestrian customers. In the digital era, shopping malls are leveraging big data and predictive analytics—specifically recommender systems—to create personalized shopping experiences and reap financial gains from in-store traffic (Ghose et al. 2019, Zeng et al. 2021). For this research, we obtained a unique shopping data set from a largescale shopping mall in Beijing city, with an indoor commercial area of more than one million square feet across four levels. On average, the mall has generated 40.8 million U.S. dollars in annual rental income and 319.9 million U.S. dollars in annual sales in recent years. Driven by the rapid development of digital technology, the shopping mall has deployed an intelligent video tracking and detection system that identifies customers with anonymized identifiers and records their store patronage behaviors, which offers a convenient tool for our data collection. After a typical five-filter strategy (by removing sequences with fewer than five visits; Sun et al. 2020), our research data set comprises 167,234 visitation sequences during the period of September 1 to November 23, 2019, resulting in 1,276,791 patronage behaviors across 175 stores in the mall. Each store patronage is captured by a customer ID, a store ID, a sequence ID, an entry timestamp, and an exit timestamp, recording who enters and exits which store at what time on a particular shopping trip.

For the evaluation, we divided the data set into a training set and a test set using the leave-one-out (LOO) strategy, which has been extensively employed in the recommendation literature (Rendle et al. 2009, Cheng et al. 2013, Sun et al. 2020). Concretely, LOO reserves the last store (i.e., the ground-truth) in each visitation sequence for testing and inputs the remaining sequence for model training.<sup>9</sup> To find the best hyperparameters, we applied the LOO strategy again on the training set to generate new training and validation sets; hence, the validation set was used for hyperparameter tuning using grid search. For evaluation, each method predicted the relevance score for each candidate store and generated a recommendation list of stores sorted by descending order of relevance scores. The recommendation performance of a method was evaluated by comparing the groundtruth stores against their recommendation lists generated by the underlying method. In this study, we adopted two widely used metrics for evaluating the recommendation performance, including recall and the discounted cumulative gain (DCG; Shani and Gunawardana 2011, Sun et al. 2020).<sup>10</sup> Both metrics are in the range [0, 1], with higher values indicating greater recommendation accuracy. Detailed formulas for these metrics are provided in Online Appendix G.

## 5.2. Benchmarks and Recommendation Performances

To demonstrate the superior performance of our method, we selected several classic and state-of-the-art recommendation methods as benchmarks. Existing implicit-feedback recommendation methods can be broadly categorized as neighborhood-based collaborative filtering, matrix factorization, and deep sequential models. For neighborhood-based collaborative filtering, we chose two classic recommendation methods, userbased K-nearest neighbors (UserKNN; Breese et al. 1998) and item-based K-nearest neighbors (ItemKNN; Sarwar et al. 2001). Because of their ease of implementation and reliable performance, UserKNN and ItemKNN are widely employed in industrial practice. For matrix factorization methods, we first chose two classic methods that are closely related to our method, namely, BPR-MF and FPMC; both methods employ classic pairwise learning, but FPMC further considers local interests (i.e., z<sup>T</sup> · q in Equation (12)) in addition to global preferences compared with BPR-MF. Moreover, we selected two variants of BPR-MF, namely, CoFiSet (Pan and Chen 2013) and Context-BPR (Liu et al. 2020), as benchmarks. CoFiSet relaxes the pairwise preference relations from the item to the item-set level, whereas Context-BPR integrates contextual information (including hour, week, month, store’s category, and floor) to enhance recommendation performance. Furthermore, to demonstrate the efficacy of modelbased debiasing by UMPR, we devised two variants of UMPR as benchmarks, named Cat-MPR and Dist-MPR, by employing representative heuristic-based debiasing strategies. Note that both Cat-MPR and Dist-MPR employ the same strategy as UMPR in modeling relevance scores (by considering preference-matching scores and movement costs as defined in Equations (11)–(13)). The only difference lies in how to identify negative feedback from unvisited stores: Cat-MPR randomly samples unvisited stores in the same category as the visited store to construct preference relations, whereas Dist-MPR estimates the probability of an unvisited store being negative as inversely proportional to the customer’s distance to this store.<sup>11</sup> For deep sequential models, typical architectures for sequence rep resentation include recurrent neural networks and attention mechanisms (Fang et al. 2020). For the architecture of recurrent neural networks, we selected two advanced benchmarks, including (1) GRU4Rec (Hidas et al. 2016), which encodes a visitation sequence onto a hidden layer based on gated recurrent units, and (2) JODIE (Kumar et al. 2019), which employs coupled recurrent neural networks to generate dynamic embedding trajectories for both user and items. For the architecture of attention mechanisms, we chose SSE-PT (Wu et al. 2020) as a state-of-the-art benchmark, which considers personalized user embedding in the transformer architecture and introduces stochastic shared embed dings as a regularization technique to improve recommendation performances. In addition, we also included a random recommender without any personalization efforts as a baseline. We anticipate that, under normal circumstances, the aforementioned personalized recommendation methods should outperform the random baseline. Table 3 summarizes the benchmark methods.<sup>12</sup>

Using the evaluation procedure and benchmark methods described above, we conducted experiments to test the recommendation performance of our method and the benchmarks. We varied the length of the recommendation lists with N � 1, 3, and 5. The recommen dation performances of UMPR and the benchmark methods are reported in Table 4, with values in parentheses indicating the relative improvement of UMPR over each benchmark.<sup>13</sup>

We have several observations regarding the evaluation results in Table 4. First, our UMPR method achieves the best performances across all metrics, exhibiting significant improvements over each benchmark method (paired t-tests; p < 0.001). The result suggests the superiority of our method in combining pedestrian movement with unbiased learning to deliver personalized recommendations in physical spaces. Second, in comparison with state-of-the-art deep sequential models, our method outperforms JODIE, GRU4Rec, and SSE-PT in Recall@3 by 9.2%, 16.4%, and 16.9%, respectively. The relative advantage of our method can be largely attributed to its ability to explicitly model pedestrian movement between successive visits, in contrast to the deep sequential models (i.e., JODIE, GRU4Rec, and SSE-PT) that focus on capturing sequential patterns implicitly. Last, we observe that UMPR exhibits considerable enhancements across the metrics compared with its variants: Dist-MPR and Cat-MPR. Given that all three methods employ the same matrix factorization approach (i.e., Equations (11)–(13)) to computing relevance scores, these relative enhancements underscore the superiority of UMPR’s modelbased debiasing component over the heuristic-based debiasing strategies.

Table 3. Summary of Benchmark Methods

<table><tr><td>Category</td><td>Methods</td></tr><tr><td>Neighborhood-based collaborative filtering</td><td>UserKNN, ItemKNN</td></tr><tr><td>Matrix factorization</td><td>BPR-MF, FPMC, CoFiSet, Context-BPR, Cat-MPR, Dist-MPR</td></tr><tr><td>Deep sequential models</td><td>GRU4Rec, JODIE, SSE-PT</td></tr><tr><td>Nonpersonalized baseline</td><td>Random</td></tr></table>

Table 4. Recommendation Performances of UMPR and Benchmark Methods

<table><tr><td>Method</td><td>Recall@1</td><td>Recall@3</td><td>Recall@5</td><td>DCG@3</td><td>DCG@5</td></tr><tr><td>UMPR (our method)</td><td>0.150</td><td>0.284</td><td>0.366</td><td>0.227</td><td>0.261</td></tr><tr><td>GRU4Rec</td><td>0.134(11.9%)</td><td>0.244(16.4%)</td><td>0.311(17.7%)</td><td>0.198(14.6%)</td><td>0.225(16.0%)</td></tr><tr><td>Dist-MPR</td><td>0.126(19.0%)</td><td>0.249(14.1%)</td><td>0.333(9.9%)</td><td>0.196(15.8%)</td><td>0.231(13.0%)</td></tr><tr><td>JODIE</td><td>0.124(21.0%)</td><td>0.260(9.2%)</td><td>0.344(6.4%)</td><td>0.202(12.4%)</td><td>0.236(10.6%)</td></tr><tr><td>SSE-PT</td><td>0.124(21.0%)</td><td>0.243(16.9%)</td><td>0.327(11.9%)</td><td>0.191(18.8%)</td><td>0.226(15.5%)</td></tr><tr><td>Cat-MPR</td><td>0.120(25.0%)</td><td>0.247(15.0%)</td><td>0.325(12.6%)</td><td>0.193(17.6%)</td><td>0.225(16.0%)</td></tr><tr><td>FPMC</td><td>0.111(35.1%)</td><td>0.238(19.3%)</td><td>0.318(15.1%)</td><td>0.184(23.4%)</td><td>0.217(20.3%)</td></tr><tr><td>Context-BPR</td><td>0.071(111.3%)</td><td>0.153(85.6%)</td><td>0.222(64.9%)</td><td>0.118(92.4%)</td><td>0.146(78.8%)</td></tr><tr><td>CoFiSet</td><td>0.056(167.9%)</td><td>0.140(102.9%)</td><td>0.202(81.2%)</td><td>0.104(118.3%)</td><td>0.130(100.8%)</td></tr><tr><td>BPR-MF</td><td>0.051(194.1%)</td><td>0.135(110.4%)</td><td>0.204(79.4%)</td><td>0.099(129.3%)</td><td>0.127(105.5%)</td></tr><tr><td>UserKNN</td><td>0.033(354.5%)</td><td>0.074(283.8%)</td><td>0.121(202.5%)</td><td>0.056(305.4%)</td><td>0.075(248.0%)</td></tr><tr><td>ItemKNN</td><td>0.025(500.0%)</td><td>0.070(305.7%)</td><td>0.112(226.8%)</td><td>0.051(345.1%)</td><td>0.068(283.8%)</td></tr><tr><td>Random</td><td>0.006(2,400.0%)</td><td>0.017(1,570.6%)</td><td>0.029(1,162.1%)</td><td>0.012(1,791.7%)</td><td>0.017(1,435.3%)</td></tr></table>

## 5.3. Ablation Studies

To understand the superior performance of our method, we conducted ablation studies to identify the contribution of each proposed component to the overall recommendation performance. Our method features two novel components: (1) the movement component (M), which is embodied as a linear combination of movement factors in the cost term $( c _ { u k i } )$ of Equation (13), and (2) the unbiasing component (U), which employs the debiasing component $( \mathrm { i . { { \bar { e } . } , \ P } } ( i > _ { u , k } j | D )$ defined in Equation (8)) to address exposure bias in pairwise learning. To demonstrate the contribution of each component, we designed two control methods by, respectively, dropping one component $( \mathrm { i . e . , } M$ or U) from our method. Specifically, we dropped the movement component from UMPR by setting $c _ { u k i } = 0$ to obtain the first control method, UMPR-M. Likewise, we dropped the unbiasing component from UMPR by setting $\bar { P ( i \succ _ { u , k } j | D ) } = 1$ for all relations $( u , k , i , j ) \in D$ , which results in the second control method, UMPR-U. Table 5 summarizes the recommendation performances of UMPR and the two control methods.

The results reveal several interesting findings. First, each model component $( \mathrm { i . e . , } \mathscr { U } \mathrm { o r } \mathscr { M } )$ significantly con tributes to the enhanced performance of our method, given the presence of the other. This suggests that both model components are indispensable and complemen tary to each other in improving the recommendation performance. Second, each model component has unique advantages for specific recommendation scenarios. The movement component M is particularly advantageous when recommendation lists are short $\left( \mathrm { e . g . , ~ } N = 1 \right)$ , whereas the unbiasing component U is more beneficial when the lengths increase $( \mathrm { e . g . , }$ $N \in \{ 3 , 5 \} )$ . Overall, the ablation studies validate the efficacy of both movement and debiasing components in addressing exposure bias and offering effective and unbiased recommendations for pedestrian customers.

Table 5. Recommendation Performances of UMPR, UMPR-M, and UMPR-U

<table><tr><td>Method</td><td>Recall@1</td><td>Recall@3</td><td>Recall@5</td><td>DCG@3</td><td>DCG@5</td></tr><tr><td>UMPR (our method)</td><td>0.150</td><td>0.284</td><td>0.366</td><td>0.227</td><td>0.261</td></tr><tr><td>UMPR-M</td><td>0.129</td><td>0.264</td><td>0.347</td><td>0.207</td><td>0.241</td></tr><tr><td>UMPR-U</td><td>0.131</td><td>0.255</td><td>0.336</td><td>0.203</td><td>0.236</td></tr><tr><td>UMPR over UMPR-M</td><td>16.3%</td><td>7.6%</td><td>5.5%</td><td>9.7%</td><td>8.3%</td></tr><tr><td>UMPR over UMPR-U</td><td>14.5%</td><td>11.4%</td><td>8.9%</td><td>11.8%</td><td>10.6%</td></tr></table>

## 5.4. Incremental Revenue Estimation

Having demonstrated the superior performance of our method, we further investigate whether the predictive performance can translate into desirable economic and humanistic perspectives (Abbasi et al. 2016). To showcase the economic value of our method, we introduced a key metric, incremental revenue (Sun et al. 2022), to quantify the added monetary value. In contrast to digital platforms, where users swiftly navigate between webpages with a single click on recommended items, pedestrian shoppers need to physically move from their current position to visit a recommended store if interested. During this movement process, they may be exposed to other recommended stores along the route and have a certain likelihood of patronizing these stores (Kłeczek and Wa˛s 2014). Therefore, one major source of incremental revenue arises from the conversions of these potential visits to the recommended stores along the route.

To estimate the incremental revenue, we devised a simulation procedure comprising four steps: (1) generating recommendation lists, (2) identifying exposed stores, (3) simulating visitation probabilities, and (4) estimating incremental revenue. In Step 3, we employed the decay rate $\gamma \in ( 0 , 1 )$ to characterize how fast the probability of visiting a store decreases with its rank in the corresponding recommendation list; A larger γ yields greater store visitation probabilities. In Step 4, the average revenue per visit is around \$1.26 based on the financial report from the data provider. Details about the simulation procedure are provided in Online Appendix I. In this simulation, we considered the typical scenario of top 5 recommendations (i.e.,

N � 5), given its prevalence in industry practice and recommendation literature (He et al. 2019).

To demonstrate the relative performance of our method, we selected the best-performing benchmark methods from each category based on their performance on Recall@5 in Table 4. Specifically, we chose (1) JODIE from the category of deep sequential models, (2) Dist-MPR and FPMC, the two best-performing bench marks with and without debiasing, from the category of matrix factorization, and (3) UserKNN from the category of neighborhood-based collaborative filtering. For each method, we conducted 100 parallel simulations and reported the average performances to mitigate the impact of randomness. Figure 6 presents the average incremental revenue per recommendation for different methods with varying decay rates of γ. In this figure, we labeled each method with the specific incremental revenue and marked the improvement of UMPR over each benchmark in parentheses. For instance, for $\gamma = 0 . 7 5$ , UMPR achieves an incremental revenue of \$0.405 per recommendation, yielding a 52.8% improvement over JODIE.

We highlight two key findings from this figure. First, our UMPR is expected to produce substantial added monetary value when deployed in physical spaces. Under different settings of γ, the incremental revenue ranges from \$0.056 to \$0.405. Taking $\gamma = 0 . 7 5$ as an example, it results in an average of \$0.405 in sales for each request of recommendation service. Considering the sheer size of 33 million visitors and an average of 7.7 visits per trip, this could translate into an additional \$103 million in incremental revenue, accounting for 32.2% of the mall’s total annual revenue in 2019. Second, our method consistently outperforms all benchmarks over different γ, with the improvements ranging from 33.3% to 340.2%. Even compared with the bestperforming benchmark, Dist-MPR, our method further exhibits a significant lift ranging from 33.3% to 35.5%. In summary, the results suggest that our method can create substantial monetary value for the physical retail industry. By providing tailored recommendations to pedestrian shoppers, our method has the potential to increase in-store traffic for store tenants and, ultimately, boost the revenue generated for the shopping mall.

Figure 6. (Color online) Incremental Revenue Generated by UMPR and Benchmark Methods  
![](/api/attachments/64TQ7628/fulltext/images/ca9b3385521585b85105cad537162a2b1605c7947db6e64756fdb19540832feb.jpg)

![](/api/attachments/64TQ7628/fulltext/images/2bd27a30927a3560392d924f6257179c2c24950f948892f654087da1b85d6b12.jpg)

![](/api/attachments/64TQ7628/fulltext/images/f7bd33d3dfff1b250f68cde47c7f4d5cf62a7270464096e649e1555a5b86a8cf.jpg)

## 5.5. Humanistic Fairness Analysis

Having demonstrated that the debiasing component $( \mathrm { i . e . , }$ UMPR over UMPR-U) leads to a notable performance improvement in Section 5.3, we further explore whether mitigating exposure bias promotes recommendation fairness across high- and low-exposed groups. To this end, we grouped the testing instances into high- and lowexposed groups based on each exposure factor, including Access, Visibility, and Popularity. Formally, given a customer’s visitation sequence $S _ { u } = < i _ { u , 1 } , . . . , i _ { u , k } , . . . , i _ { u , \mid S _ { u } \mid } >$ and the corresponding ground-truth store $i ^ { * } \in I ^ { d }$ , we, respectively, divided the groups based on each exposure factor according to Table 6. Taking the Access factor as an example, the “accessible” group refers to the list of ground-truth stores that are unvisited but have been accessed in the observed path $( A C _ { u k i ^ { * } } = 1 )$ , whereas the “inaccessible” group refers to the list of ground-truth stores that have not been accessed $( A C _ { u k i ^ { * } } = 0 )$

To assess recommendation fairness, we employed the widely used metric—ranking-based equal opportunity (REO)—to measure the performance discrepancy across different groups (Liu et al. 2023). A lower REO indicates a smaller discrepancy in recommendation performances across different groups and thus a greater level of recommendation fairness. Additionally, we calculated the performance improvement (PI) of UMPR over UMPR-U for each group; this metric gauges the contribution of incorporating the debiasing component in enhancing recommendation performances for different groups. The results pertaining to REO@5 and PI metrics (measured at Recall@5) are depicted in Figure 7.

Two main findings can be made from the figure. First, we observe that UMPR exhibits a lower REO compared with UMPR-U across different groups, leading to reductions in REO ranging from 13.5% to 66.7%. The result suggests that mitigating exposure bias by our method facilitates to promote recommendation fairness. Second, the PI is more pronounced for lowexposed groups compared with high-exposed groups, a pattern that remains consistent across different group divisions based on Access, Visibility, and Popularity. We anticipate that this pattern can produce significant benefits for multiple stakeholders of the shopping mall: (1) our method prioritizes recommending customers with relevant yet unexposed stores beyond their movement paths, thus creating a more exploratory shopping experience; (2) it effectively guides targeted customer traffic toward less visible stores, providing them with increased exposure chance; and (3) it contributes to boosting customer traffic for less popular stores, thus mitigating the “Matthew effect.” In the long run, these benefits contribute to favoring disadvantaged stores, enhancing recommendation fairness and promoting more balanced traffic management within shopping malls.

## 6. Conclusion

Given the remarkable success of personalized recommendations on digital platforms and the widespread adoption of positioning technologies in physical environments, brick-and-mortar businesses are actively exploring viable approaches to extend recommendation services from the online to offline scenarios. In response, our study introduces a generalized recommendation problem, termed P3M, which is characterized by two salient design elements: pedestrian movement and spatial layout. We posit that the dynamic interaction between pedestrian movement and spatial layout contributes to uneven exposure and, consequently, exposure bias. To address this issue, we propose a novel recommendation approach, UMPR, which integrates pedestrian movement modeling with unbiased pairwise learning to achieve effective and unbiased recommendations. Theoretically, we provide effectiveness guarantees of the proposed debiasing framework in reducing training errors, as detailed in Propositions 1 and 2. Empirically, using real-world shopping mall data, we demonstrate the superior performance of our method over state-of-the-art methods and validate the contribution of each designed compo nent to the overall performance. Furthermore, we explore the practical utility of our approach by examining its potential to increase economic value and promote recommendation fairness for multiple stakeholders in a physical context.

Table 6. Group Divisions Based on Exposure Factors

<table><tr><td>Group label</td><td>Definition</td></tr><tr><td>Accessible</td><td>If  $i^{*} \notin S_{u}$  and there exists  $k \in \{2,3,\ldots,|S_{u}|\}$  such that  $AC_{uki^{*}} = 1$ ;</td></tr><tr><td>Inaccessible</td><td> $AC_{uki^{*}} = 0$  holds for all  $k \in \{2,3,\ldots,|S_{u}|\}$ .</td></tr><tr><td>High visibility</td><td>There exists  $k \in \{2,3,\ldots,|S_{u}|\}$  such that  $VS_{uki^{*}} \geq \Delta$ , where the threshold  $\Delta = 0.1$  is calculated using the average of the visibility values ( $VS_{uki}$ ) in the training set;</td></tr><tr><td>Low visibility</td><td> $VS_{uki^{*}} < \Delta$  holds for all  $k \in \{2,3,\ldots,|S_{u}|\}$ .</td></tr><tr><td>High popularity</td><td> $i^{*}$  is one of the top 10 most popular stores based on its popularity  $PO$ ;</td></tr><tr><td>Low popularity</td><td>Otherwise.</td></tr></table>

Figure 7. Fairness Metrics and Performance Improvements for High- and Low-Exposed Groups  
![](/api/attachments/64TQ7628/fulltext/images/a669436f6d981ef44006ab9cd865d4ba87f34c632f3258246d7e018d661be328.jpg)

Our study makes several research contributions. First, unlike the abundant backdrop of recommendation literature on digital platforms (Yin et al. 2022, Li and Tuzhilin 2023, Wei et al. 2023, Chen et al. 2024), our research addresses a crucial yet understudied problem: POI recommendations in physical spaces. Specifically, we formulate a generalized P3M problem and identify a critical impediment—exposure bias arising from pedestrian movement—that hinders the effective learning of recommender systems. Notably, our study stands at the forefront of addressing exposure bias in physical recommendations by capturing the dynamic interaction between pedestrian movement and spatia layout. Therefore, our study advances the burgeoning field of design science research on artificial intelligence (Abbasi et al. 2024) with an innovative recommendation problem and design artifacts. Second, to address exposure bias, we propose a novel unbiased pairwise learning framework by integrating the learnable debiasing component into classic pairwise learning. Additionally, we devise a new alternating learning algorithm based on stochastic gradient ascent for parameter learning. The effectiveness of the proposed unbiased pairwise learning has been demonstrated through theoretical proofs of training error reduction and empirical evaluations of improved recommendation performance. Thus, our study contributes to the extant literature on recommendation bias (Adomavicius et al. 2022, Chen et al. 2023, Mousavi et al. 2023) with a novel and effective unbiased recommendation approach that integrates model-based debiasing with pairwise learning. Third, to characterize pedestrian movement, our study establishes a network representation of the physical space, develops representation operationalizations of movement factors, and integrates them into a novel movement-aware recommendation model. Our empirical results reveal that, in addition to preference matching, the cost of pedestrian movement is crucial for relevance assessment in physical spaces. Compared with the position dimension, moving direction and visual scope play more dominant roles in assessing movement costs, as evidenced by the movement factor analysis in Online Appendix J. These findings provide salient design insights for advancing future IS research on pedestrian movement modeling in realworld settings.

![](/api/attachments/64TQ7628/fulltext/images/5cab997d74b55e62c9855076655411a85cbbb6783639a76fef797c2b90fad5ec.jpg)

Our study also offers managerial implications. First, our method can be employed to provide effective recommendations to pedestrian customers across vari ous physical environments. Using the shopping mall context as an example, the deployment of our method could create personalized shopping experiences and, in turn, increase revenues and profits for store tenants and mall owners. As demonstrated in Section 5.4, our method yields an additional \$103 million in annual revenue, accounting for 32.2% of the mall’s total revenue in 2019. Beyond shopping malls, our method is applicable to other physical spaces characterized by pedestrian movement, such as hypermarkets, commercial pedestrian streets, and world expos. Considering the sheer size of the global retailing industry (i.e., 19.86 trillion U.S. dollars), our approach can bring huge financial gains for the physical retail market. Second, the promi nence of mitigating exposure bias by our method yields several advantages that are unattainable through biased recommendations. As exemplified in Section 5.5, our method exhibits superiority in recommending relevant yet less exposed stores, as opposed to conventional biased recommendations that could inadvertently exacerbate the “Matthew effect.” This characteristic not only enriches customers’ exploratory shopping experience but also provides disadvantaged stores with increased exposure chances, fostering more balanced traffic management within shopping malls. Therefore, our method has the potential to promote recommendation fairness among stakeholders and enrich the diversity of the physical retail ecosystem. Last, our method can be conveniently deployed in physical spaces to deliver personalized recommendations for pedestrian customers. With the pervasiveness of positioning technologies (e.g., GPS, Wi-Fi, RFID, and video cameras), automatic recording and collection of pedestrian movement data have become standard and mature practices in physical environments (Ghose et al. 2019). Based on the collected data, our method can be trained to learn its model parameters and generate personalized recommendations for each customer. These recommendations can be delivered through various channels, including push-based notifications via mobile apps and pullbased interactions through digital screens and AI robots, which are currently employed in the physical retail industry. In Online Appendix K, we outline the system implementation process and emphasize the key privacy-preserving principles (e.g., authorization and opt-in/opt-out mechanisms) that mall operators should adhere to. This ensures a personalized experience while prioritizing customer privacy.

Our research has its limitations and presents opportunities for future research. To simplify intricate relationships and facilitate efficient and manageable modeling, our proposed approach relies on several assumptions underpinning unbiased pairwise learning and pedestrian movement modeling.<sup>14</sup> First, the proposed unbiased pairwise learning framework in this study adopts the commonly adopted assumption in the stream of implicit-feedback recommendations (Rendle et al. 2009, Saito et al. 2020), stating that observed visits reflect positive preference (i.e., $P ( \bar { R } _ { u k i } = 1 | Y _ { u k i } = 1 ) = 1 )$ In future work, it would be worthwhile to investigate possible approaches to relax this assumption by gauging the probability of each visit as being positive (i.e., the value of $P ( R _ { u k i } = 1 | Y _ { u k i } = 1 ) )$ . A possible extension that utilizes dwell time can be found in Online Appendix M. Second, following the common practice in pedestrian movement modeling (Farley and Ring 1966, Penn and Turner 2002), this study adopts the shortest path assumption to simulate movement paths between successive visits. Although our investigations in Online Appendix N corroborate the effectiveness and efficiency of the shortest path strategy compared with alternative path simulation strategies (e.g., top-K path strategy), it would be interesting to augment the observed data set with real-world complete movement trajectories, thus making it possible to investigate the heterogeneity of individual movements in physical spaces and further enhance the recommendation effectiveness. Third, future studies may consider extending our agent-based movement modeling to three-dimensional (3D) space when comprehensive indoor spatial data (e.g., shelves or other height-oriented considerations) becomes available. This allows for more precise modeling of visibility and improved estimation of exposure likelihood. Fourth, a promising research direction lies in bridging our study with the shopping mode literature (Pfeiffer et al. 2020) and investigating how different shopping modes (e.g., exploratory, goal directed, and routine) influence exposure likelihood and store patronage decisions. In Online Appendix O, we present a preliminary attempt at identifying shopping modes and extending our model to incorporate exposure factors specific to each shopping mode. Fifth, future research may consider adapting and evaluating our approach to other physical environments, such as supermarkets and pedestrian streets, as well as the metaverse—a virtual 3D environment that mirrors and extends the physical world, enabling real-time movement and interaction. Our approach’s ability to capture customer preferences based on dynamic movement data can be employed to offer personalized experiences and boost economic value across these diverse settings. Finally, although this study follows the widely accepted practice of evaluating our method using archival data, it would be worthwhile to conduct field experiments for furthe evaluation. Through field experiments, we can observe how customers react to the recommendations and how the recommender system impacts the profits and revenues of retailers. In addition, the deployment of recommender systems in physical spaces may lead to the coexistence of various types of exposure bias arising from pedestrian movement, as well as the displays of recommender systems. In this setting, how to distinguish the different types of exposure bias to design unbiased recommendation approaches would be an interesting question that deserves future research.

## Acknowledgments

The authors thank the senior editor, associate editor, and three anonymous reviewers for insightful comments and suggestions throughout the review process and Jiayi Guo for constructive feedback on the theoretical analysis.

## Endnotes

<sup>1</sup> Customers may have multiple visitation sequences due to different visits to the physical space. For simplicity, the modeling section is described with a single sequence per customer, whereas the evaluation incorporates all observed visitation sequences.

<sup>2</sup> Here, $i _ { u , 0 }$ is a dummy starting position for a visitation sequence, such as the entrance.

<sup>3</sup> For a negative feedback j irrelevant to the prior visitation sequence, we have $\overset {  } { P } ( R _ { u k j } = 1 ) = 0$ and thereby $P ( R _ { u k j } = 0 | Y _ { u k j } = 0 ) = 1$ . Conversely, for a potentially positive feedback j with sequential relevance, we can estimate $P ( R _ { u k j } = 1 ) = 1$ and thus correctly obtain $P ( R _ { u k j } = 0 |$ $Y _ { u k j } = 0 ) = 0 .$

<sup>4</sup> When $| S _ { u } |  \infty ,$ , the proportion of overclaimed error reduction approaches $2 \tau _ { u } - \tau _ { u } ^ { 2 }$ , according to our monotonic analysis in Online Appendix B.

<sup>5</sup> The specific types of POI nodes are determined by physical environments, such as store entrances in malls and the positions of shelf spaces arranged by product categories in retail stores. Consequently, POI recommendations translate into store and product category recommendations, respectively.

<sup>6</sup> It is commonly accepted that the binocular visual scope ϑ for human eyes spans 120 degrees, with 60 degrees on each side of the moving direction d (Lu and Seo 2015).

<sup>7</sup> We omit the intercept term ω<sub>0</sub> in the formulation of $c _ { u k i }$ because the unbiased pairwise learning objective proposed in Equation (5) uses $c _ { u k i } - c _ { u k j } .$ , so the intercept term ω is eliminated.

<sup>8</sup> Robustness checks show that our method’s performance remains relatively consistent with various popularity measures, including monthly and daily popularity.

<sup>9</sup> The robustness checks in Online Appendix F corroborate the reliable and superior performances of our method across different evaluation settings (e.g., sequence splitting).

<sup>10</sup> Here, we omitted Precision and F-Measure because their values can be directly calculated based on the reported Recall using Precision@N � <sup>1</sup> Recall@N and $\begin{array} { r } { F @ N = \frac { 2 } { N + 1 } } \end{array}$ Recall@N in the LOO setting.

<sup>11</sup> We implemented Dist-MPR by replacing the debiasing component in Equation (18) using $P ( i \succ _ { u , k } j ) : = 1 / d i s ( i _ { u , k - 1 } , j ) .$ , where $d i s ( i _ { u , k - 1 } , j )$ measures the aggregate Euclidean distance of the movement path from the customer’s last visited store $i _ { u , k - 1 }$ to the target store j.

<sup>12</sup> The empirical results in Online Appendix H highlight the superiority of our method over association rules, with improvements ranging from 49.3% to 57.8% across the metrics.

<sup>13</sup> We omitted DCG@1 because it is identical to Recall@1 based on the definitions in Online Appendix G.

<sup>14</sup> An overview of these assumptions, along with the supporting literature and validity checks, can be found in Online Appendix L.

## References

Abbasi A, Sarker S, Chiang RH (2016) Big data research in informa tion systems: Toward an inclusive research agenda. J. Assoc. Inform. Systems 17(2):1–32.

Abbasi A, Parsons J, Pant G, Sheng ORL, Sarker S (2024) Pathways for design research on artificial intelligence. Inform. Systems Res. 35(2):441–459.

Adomavicius G, Bockstedt JC, Curley SP, Zhang J (2019) Reducing recommender system biases: An investigation of rating display designs. MIS Quart. 43(4):1321–1341.

Adomavicius G, Bockstedt J, Curley S, Zhang J (2022) Effects of per sonalized recommendations versus aggregate ratings on post consumption preference responses. MIS Quart. 46(1):627–644.

Afyouni I, Ray C, Claramunt C (2012) Spatial models for context aware indoor navigation systems: A survey. J. Spatial Inform. Sci. 1(4):85–123.

Antonini G, Bierlaire M, Weber M (2006) Discrete choice models of pedestrian walking behavior. Transportation Res. Part B: Methodological 40(8):667–687.

Bekker J, Davis J (2020) Learning from positive and unlabeled data: A survey. Machine Learn. 109(4):719–760.

Bell DR, Corsten D, Knox G (2011) From point of purchase to path to purchase: How preshopping factors drive unplanned buying. J. Marketing 75(1):31–45.

Braun M, Moe WW (2013) Online display advertising: Modeling the effects of multiple creatives and individual impression histories. Marketing Sci. 32(5):753–767.

Breese JS, Heckerman D, Kadie C (1998) Empirical analysis of predictive algorithms for collaborative filtering. Cooper GF, Moral S, eds. Proc. 14th Conf. Uncertainty Artificial Intelligence (Morgan Kaufmann Publishers, San Francisco, CA), 43–52.

Chen J, He L, Liu H, Yang YC, Bi X (2024) Background music recommendation on short video sharing platforms. Inform. Systems Res. 35(4):1890–1908.

Chen J, Dong H, Wang X, Feng F, Wang M, He X (2023) Bias and debias in recommender system: A survey and future directions. ACM Trans. Inform. Systems 41(3):1–39.

Chen J, Wang C, Zhou S, Shi Q, Feng Y, Chen C (2019) SamWalker: Social recommendation with informative sampling strategy. Proc. World Wide Web Conf. (ACM, New York), 228–239.

Cheng C, Yang H, Lyu MR, King I (2013) Where you like to go next: Successive point-of-interest recommendation. Rossi F, ed. Proc. 23rd Internat. Joint Conf. Artificial Intelligence (AAAI Press, Palo Alto, CA) 2605–2611.

Cox D, Cox AD (2002) Beyond first impressions: The effects of repeated exposure on consumer liking of visually complex and simple product designs. J. Acad. Marketing Sci. 30(2): 119–130.

Damak K, Khenissi S, Nasraoui O (2021) Debiased explainable pairwise ranking from implicit feedback. Proc. 15th ACM Conf. Recommender Systems (ACM, New York), 321–331.

Damak K, Khenissi S, Nasraoui O (2022) Debiasing the cloze task in sequential recommendation with bidirectional transformers. Proc. 28th ACM SIGKDD Conf. Knowledge Discovery Data Mining (ACM, New York), 273–282.

Deamer L (2020) Shopping mall robots are boosting retail. Accessed July 1, 2025, https://www.electronicspecifier.com/industries robotics/shopping-mall-robots-are-boosting-retail.

Fang H, Zhang D, Shu Y, Guo G (2020) Deep learning for sequential recommendation: Algorithms, influential factors, and evaluations. ACM Trans. Inform. Systems 39(1):1–42.

Farley JU, Ring LW (1966) A stochastic model of supermarket traffic flow. Oper. Res. 14(4):555–567.

Ghose A, Li B, Liu S (2019) Mobile targeting using customer trajectory patterns. Management Sci. 65(11):5027–5049.

Gibson M, Pullen M (1972) Retail turnover in the East Midlands: A regional application of a gravity model. Regional Stud. 6(2):183–196.

Guo J, He J, Wu X (2024) Shopping trip recommendations: A nove deep learning-enhanced global planning approach. Decision Support Systems 182:114238.

Hastie T, Tibshirani R, Friedman JH (2009) The Elements of Statistical Learning: Data Mining, Inference, and Prediction, Springer Series in Statistics, 2nd ed. (Springer, New York).

Haynes D (2021) Gable launches mall kiosk with twin big screens for directory and advertising. Accessed July 1, 2025, https:// www.sixteen-nine.net/2021/06/04/gable-launches-mall-kiosk with-twin-big-screens-for-directory-and-advertising/.

He J, Fang X, Liu H, Li X (2019) Mobile app recommendation: An involvement-enhanced approach. MIS Quart. 43(3):827–849.

Herlocker J, Konstan JA, Riedl J (2002) An empirical analysis of design choices in neighborhood-based collaborative filtering algorithms. Inform. Retrieval 5(4):287–310.

Hidasi B, Karatzoglou A, Baltrunas L, Tikk D (2016) Session-based recommendations with recurrent neural networks. Proc. 4th Internat. Conf. Learn. Representations (ICLR, Appleton, WI), 1–10.

Hoogendoorn S, Bovy P (2004) Pedestrian route-choice and activity scheduling theory and models. Transportation Res. Part B: Meth odological 38(2):169–190.

Hu Y, Koren Y, Volinsky C (2008) Collaborative filtering for implicit feedback datasets. Proc. 8th IEEE Internat. Conf. Data Mining (IEEE, New York), 263–272.

Hui SK, Fader PS, Bradlow ET (2009) Path data in marketing: An integrative framework and prospectus for model building. Marketing Sci. 28(2):320–335.

Hui SK, Inman JJ, Huang Y, Suher J (2013) The effect of in-store travel distance on unplanned spending: Applications to mobile promotion strategies. J. Marketing 77(2):1–16.

Kim M, Oh J, Do J, Lee S (2022) Debiasing neighbor aggregation for graph neural network in recommender systems. Proc. 31st ACM Internat. Conf. Inform. Knowledge Management (ACM, New York), 4128–4132.

Kłeczek P, Wa˛s J (2014) Simulation of pedestrians behavior in a shopping mall. Wa˛s J, Sirakoulis GC, Bandini S, eds. Cellular Automata, vol. 8751 (Springer International Publishing, Cham, Switzerland), 650–659.

Krause T, Deriyeva A, Beinke JH, Bartels GY, Thomas O (2024) Mitigating exposure bias in recommender systems—A comparative analysis of discrete choice models. ACM Trans. Recommender Systems 3(2):1–37.

Kumar D (2024) An update on Amazon’s plans for Just Walk Out and checkout-free technology. Accessed July 1, 2025, https:// www.aboutamazon.com/news/retail/amazon-just-walk-out-dash cart-grocery-shopping-checkout-stores.

Kumar S, Zhang X, Leskovec J (2019) Predicting dynamic embedding trajectory in temporal interaction networks. Proc. 25th ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining (ACM, New York), 1269–1278.

Lee D, Hosanagar K (2021) How do product attributes and reviews moderate the impact of recommender systems through pur chase stages? Management Sci. 67(1):524–546.

Lei Y, Li W, Lu Z, Zhao M (2017) Alternating pointwise-pairwise learning for personalized item ranking. Proc. ACM Conf. Infor mation Knowledge Management (ACM, New York), 2155–2158.

Leszczyc PTLP, Sinha A, Sahgal A (2004) The effect of multi purpose shopping on pricing and location strategy for grocery stores. J. Retailing 80(2):85–99.

Li P, Tuzhilin A (2023) When variety seeking meets unexpectedness: Incorporating variety-seeking behaviors into design of unexpected recommender systems. Inform. Systems Res. 35(3):1257–1273.

Li X, Grahl J, Hinz O (2022) How do recommender systems lead to consumer purchases? A causal mediation analysis of a field experiment. Inform. Systems Res. 33(2):620–637.

Li YM, Lin LF, Ho CC (2017) A social route recommender mechanism for store shopping support. Decision Support Systems 94:97–108.

Lian D, Wu Y, Ge Y, Xie X, Chen E (2020) Geography-aware sequential location recommendation. Proc. 26th ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining (ACM, New York), 2009–2019.

Liang D, Charlin L, McInerney J, Blei DM (2016) Modeling user exposure in recommendation. Proc. 25th Internat. Conf. World Wide Web (International World Wide Web Conferences Steering Committee), 951–961.

Lin Z, Zhang Y, Tan Y (2019) An empirical study of free product sampling and rating bias. Inform. Systems Res. 30(1):260–275.

Liu Z, Fang Y, Wu M (2023) Mitigating popularity bias for users and items with fairness-centric adaptive recommendation. ACM Trans. Inform. Systems 41(3):1–27.

Liu X, Zhang J, Yan C (2020) Towards context-aware collaborative filtering by learning context-aware latent representations. Knowledge-Based Systems 199:1–13.

Liu B, Fu Y, Yao Z, Xiong H (2013) Learning geographical preferences for point-of-interest recommendation. Proc. 19th ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining (ACM, New York), 1043–1051.

Lu Y, Seo HB (2015) Developing visibility analysis for a retail store: A pilot study in a bookstore. Environ. Planning B Planning Desing 42(1):95–109.

Mousavi N, Adamopoulos P, Bockstedt J (2023) The decoy effect and recommendation systems. Inform. Systems Res. 34(4):1533–1553.

Mowrey CH, Parikh PJ, Gue KR (2019) The impact of rack layout on visual experience in a retail store. Inform. Systems Oper. Res. 57(1):75–98.

Pan W, Chen L (2013) CoFiSet: Collaborative filtering via learning pairwise preferences over item-sets. Ghosh J, Obradovic Z, Dy J, Zhou Z-H, Kamath C, Parthasarathy S, eds. Proc. SIAM Internat. Conf. Data Mining (Society for Industrial and Applied Mathematics, Philadelphia), 180–188.

Pan R, Zhou Y, Cao B, Liu NN, Lukose R, Scholz M, Yang Q (2008) One-class collaborative filtering. Proc. 8th IEEE Internat. Conf. Data Mining (IEEE, New York), 502–511.

Penn A, Turner A (2002) Space syntax based agent simulation. Schreckenberg M, Sharma SD, eds. Pedestrian and Evacuation Dynamics (Springer-Verlag, Berlin), 99–114.

Pfeiffer J, Pfeiffer T, Meiβner M, Weiβ E (2020) Eye-tracking-based classification of information search behavior using machine learning: Evidence from experiments in physical shops and virtual reality shopping environments. Inform. Systems Res. 31(3):675–691.

Raghubir P, Krishna A (1996) As the crow flies: Bias in consumers map-based distance judgments. J. Consumer Res. 23(1):26–39.

Rendle S, Freudenthaler C, Schmidt-Thieme L (2010) Factorizing personalized Markov chains for next-basket recommendation. Proc. 19th Internat. Conf. World Wide Web (ACM, New York), 811–820

Rendle S, Freudenthaler C, Gantner Z, Schmidt-Thieme L (2009) BPR: Bayesian personalized ranking from implicit feedback Proc. 25th Conf. Uncertainty Artificial Intelligence (AUAI Press, Arlington, VA), 452–461.

Robin T, Antonini G, Bierlaire M, Cruz J (2009) Specification, estimation and validation of a pedestrian walking behavior model Transportation Res. Part B: Methodological 43(1):36–56.

Saito Y, Yaginuma S, Nishino Y, Sakata H, Nakata K (2020) Unbiased recommender learning from missing-not-at-random implicit feedback. Proc. 13th Internat. Conf. Web Search Data Mining (ACM, New York), 501–509.

Sarwar B, Karypis G, Konstan J, Riedl J (2001) Item-based collaborative filtering recommendation algorithms. Proc. 10th Internat. Conf. World Wide Web (ACM, New York), 285–295.

Shani G, Gunawardana A (2011) Evaluating recommendation systems. Ricci F, Rokach L, Shapira B, Kantor PB, eds. Recommender Systems Handbook (Springer US, Boston), 257–297.

Shin J, Lee C, Lim C, Shin Y, Lim J (2022) Recommendation in offline stores: A gamification approach for learning the spatiotemporal representation of indoor shopping. Proc. 28th ACM SIGKDD Conf. Knowledge Discovery Data Mining (ACM, New York), 3878–3888.

Sun C, Adamopoulos P, Ghose A, Luo X (2022) Predicting stages in omnichannel path to purchase: A deep learning model. Inform. Systems Res. 33(2):429–445.

Sun Z, Yu D, Fang H, Yang J, Qu X, Zhang J, Geng C (2020) Are we evaluating rigorously? Benchmarking recommendation for reproducible evaluation and fair comparison. Proc. 14th ACM Conf. Recommender Systems (ACM, New York), 23–32.

Synced (2020) Cheetah Mobile deploys 8,000 shopping mall robots boosting offline retail. Accessed July 1, 2025, https://syncedreview. com/2020/09/18/cheetah-mobile-deploys-8000-shopping-mall robots-boosting-offline-retail/.

Timmermans H (2004) Retail location and consumer spatial choice behavior. Barlow M, Bailly A, Gibson LJ, eds. Applied Geography, vol. 7 (Springer Netherlands, Dordrecht, the Netherlands), 133–147.

Tobler WR (1970) A computer movie simulating urban growth in the Detroit region. Econom. Geography 46:234–240.

Underhill P (2008) Why We Buy: The Science of Shopping: Updated and Revised for the Internet, the Global Consumer, and Beyond (Simon & Schuster, New York).

Walter FE, Battiston S, Yildirim M, Schweitzer F (2012) Moving recommender systems from on-line commerce to retail stores. Inform. Systems E-Bus. Management 10(3):367–393.

Wan Q, He X, Wang X, Wu J, Guo W, Tang R (2022) Cross pairwise ranking for unbiased item recommendation. Proc. ACM Web Conf. (ACM, New York), 2370–2378.

Wang X, Golbandi N, Bendersky M, Metzler D, Najork M (2018) Position bias estimation for unbiased learning to rank in personal search. Proc. Eleventh ACM Internat. Conf. Web Search Data Mining (ACM, New York), 610–618.

Wei Q, Mu Y, Guo X, Jiang W, Chen G (2023) Dynamic Bayesian network–based product recommendation considering consu mers’ multistage shopping journeys: A marketing funnel perspective. Inform. Systems Res. 35(3):1382–1402.

Wu L, Li S, Hsieh CJ, Sharpnack J (2020) SSE-PT: Sequential recommendation via personalized transformer. Proc. 14th ACM Conf. Recommender Systems (ACM, New York), 328–337.

Xiao B, Benbasat I (2015) Designing warning messages for detecting biased online product recommendations: An empirical investi gation. Inform. Systems Res. 26(4):793–811.

Ye M, Yin P, Lee WC, Lee DL (2011) Exploiting geographical influence for collaborative point-of-interest recommendation. Proc. 34th Internat. ACM SIGIR Conf. Res. Development Inform. Retrieval (ACM, New York), 325–334.

Yin K, Fang X, Chen B, Sheng ORL (2022) Diversity preference aware link recommendation for online social networks. Inform. Systems Res. 34(4):1398–1414.

Zeng D, Liu Y, Yan P, Yang Y (2021) Location-aware real-time recommender systems for brick-and-mortar retailers. INFORMS J. Comput. 33(4):1608–1623.

Zhao S, King I, Lyu MR, Zeng J, Yuan M (2017) Mining business opportunities from location-based social networks. Proc. 40th Internat. ACM SIGIR Conf. Res. Development Inform. Retrieval (ACM, New York), 1037–1040.

Zhao S, Zhao T, Yang H, Lyu M, King I (2016) STELLAR: Spatial temporal latent ranking for successive point-of-interest recommendation. Proc. AAAI Conf. Artificial Intelligence (AAAI Press, Palo Alto, CA), 315–321.

Zhao K, Zhang Y, Yin H, Wang J, Zheng K, Zhou X, Xing C (2020) Discovering subsequence patterns for next POI recommendation. Christian B, ed. Proc. 29th Internat. Joint Conf. Artificial Intelligence (International Joint Conferences on Artificial Intelli gence Organization, Yokohama, Japan), 3216–3222.

Zhu W, Timmermans H (2008) Cut-off models for the ‘go-home decision of pedestrians in shopping streets. Environment. Planning. B Planning Design 35(2):248–260.

Copyright of Information Systems Research (INFORMS) is the property of INFORMS: Institute for Operations Research & the Management Sciences and its content may not be copied or emailed to multiple sites without the copyright holder's express written permission. Additionally, content may not be used with any artificial intelligence tools or machine learning technologies. However, users may print, download, or email articles for individual use.
