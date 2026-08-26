---
otero_id: 14548
otero_key: "H8KSFXEZ"
title: "Eye-Tracking-Based Classification of Information Search Behavior Using Machine Learning: Evidence from Experiments in Physical Shops and Virtual Reality Shopping Environments"
authors: "Jella Pfeiffer; Thies Pfeiffer; Martin Meißner; Elisa Weiß"
year: "2020"
journal: "Information Systems Research"
doi: "10.1287/isre.2019.0907"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/H8KSFXEZ/fulltext/images/df6b6822f2ad74b691b42fd0c4d1f264ea39897958a024330346ecaead23e945.jpg)

# Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Eye-Tracking-Based Classification of Information Search Behavior Using Machine Learning: Evidence from Experiments in Physical Shops and Virtual Reality Shopping Environments

Jella Pfeiffer, Thies Pfeiffer, Martin Meißner, Elisa Weiß

To cite this article:

Jella Pfeiffer, Thies Pfeiffer, Martin Meißner, Elisa Weiß (2020) Eye-Tracking-Based Classification of Information Search Behavior Using Machine Learning: Evidence from Experiments in Physical Shops and Virtual Reality Shopping Environments. Information Systems Research

Published online in Articles in Advance 13 May 2020

https://doi.org/10.1287/isre.2019.0907

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2020, The Author(s)

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Eye-Tracking-Based Classi<sup>fi</sup>cation of Information Search Behavior Using Machine Learning: Evidence from Experiments in Physical Shops and Virtual Reality Shopping Environments

Jella Pfeiffer,<sup>a</sup> Thies Pfeiffer,<sup>b</sup> Martin Meißner,<sup>c</sup> Elisa Weiß<sup>d</sup>

<sup>a</sup> Justus Liebig University Giessen, 35394 Gießen, Germany; <sup>b</sup> University of Applied Sciences Emden/Leer, 26723 Emden, Germany; <sup>c</sup> Zeppelin University, 88045 Friedrichshafen, Germany; <sup>d</sup> Karlsruhe Institute of Technology, 76133 Karlsruhe, Germany Contact: jella.pfeiffer@wirtschaft.uni-giessen.de, https://orcid.org/0000-0001-6125-2808 (JP); thies.pfeiffer@hs-emden-leer.de, https://orcid.org/0000-0001-6619-749X (TP); martin.meissner@zu.de, https://orcid.org/0000-0002-3574-4283 (MM); elisa@fam-weiss.de (EW)

Received: September 25, 2017 Revised: October 19, 2018; July 25, 2019 Accepted: October 19, 2019 Published Online in Articles in Advance: May 13, 2020

https://doi.org/10.1287/isre.2019.090

Copyright: © 2020 The Author(s)

Abstract. Classifying information search behavior helps tailor recommender systems to individual customers’ shopping motives. But how can we identify these motives without requiring users to exert too much effort? Our research goal is to demonstrate that eye tracking can be used at the point of sale to do so. We focus on two frequently investigated shopping motives: goal-directed and exploratory search. To train and test a prediction model, we conducted two eye-tracking experiments in front of supermarket shelves. The first experiment was carried out in immersive virtual reality; the second, in physical reality—in other words, as a field study in a real supermarket. We conducted a virtual reality study, because recently launched virtual shopping environments suggest that there is great interest in using this technology as a retail channel. Our empirical results show that support vector machines allow the correct classification of search motives with 80% accuracy in virtual reality and 85% accuracy in physical reality. Our findings also imply that eye movements allow shopping motives to be identified relatively early in the search process: our models achieve 70% prediction accuracy after only 15 seconds in virtual realit and 75% in physical reality. Applying an ensemble method increases the prediction accuracy substantially, to about 90%. Consequently, the approach that we propose could be used for the satisfiable classification of consumers in practice. Furthermore, both environments’ best predictor variables overlap substantially. This finding provides evi dence that in virtual reality, information search behavior might be similar to the one used in physical reality. Finally, we also discuss managerial implications for retailers and companies that are planning to use our technology to personalize a consumer assistance system.

![](/api/attachments/H8KSFXEZ/fulltext/images/62ed0c3a21d6f85d56d9d52271a6111695921b9a2c9cbba5430fc066b9fc8d43.jpg)

History: Kartik Hosanagar, Senior Editor; Jesse Bockstedt, Associate Editor. History: Kartik Hosanagar, Senior Editor; Jesse Bockstedt, Associate Editor

Open Access Statement: This work is licensed under a Creative Commons Attribution- NonCommercial-NoDerivatives 4.0 International License. You are free to download this work and share with others, but cannot change in any way or use commercially without permission, and you must attribute this work as “Information Systems Research. Copyright © 2020 The Author(s). https://doi.org/10.1287 isre.2019.0907, used under a Creative Commons Attribution License: https://creativecommons.org licenses/bv-nc-nd/4.0/."

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2019.0907.

Keywords: virtual reality • recommender system • mobile eye tracking • goal-directed search • exploratory search • electronic commerce • <sup>fi</sup>eld experiments • laboratory experiments • decision support systems

## 1. Introduction

Understanding the ways in which humans direct their attention while searching for information is fundamental in guiding the design of information systems. In the information systems domain, several studies have indicated that eye tracking is suitable for studying human-computer interaction (Ajanki et al. 2009, Bednarik et al. 2012) or to improve electroencephalographic recording for analyzing attention and cognitive processing (Léger et al. 2014). Previous research in other domains has shown that monitoring eye movements can provide valuable insight into information search and choice processes in various contexts, such as online decision making (Shi et al. 2013), learning (Lai et al. 2013), training (Tien et al. 2014), and multiattribute choice (Meißner et al. 2016) Despite promising opportunities for information systems research, these past works focus on understanding human attention but do not actively use eye tracking to unobtrusively personalize information systems to users’ needs and their context. The active use of eye tracking could be very helpful, for example, for consumer assistance systems such as recommender or consumer decision support systems.

In this paper, we investigate two categories of human search behavior: goal-directed and exploratory search (Janiszewski 1998). Both are frequently discussed in the literature because they determine users’ contexts and needs. In goal-directed search, subjects are motivated to find a product that fulfills their shopping needs (Janiszewski 1998). The efficiency of the search process as well as its outcome is what satisfies a goal-directed searcher (Dickinger and Stangl 2011). In exploratory search, subjects are more susceptible to bargain hunting (Wolfinbarger and Gilly 2001, Chiou and Ting 2011). Furthermore, Moe (2003) and Chiou and Ting (2011) have shown that the two search motives differ with respect to the specific pieces of information subjects search for. Our research is based on the theory of shopping motivation that reaches back to Hirschman and Holbrook (1982), who saw shopping motives as important precursors of consumer behavior. It is further in line with research by Janiszewski (1998) as well as Kaltcheva and Weitz (2006), who also distinguished two main shopping motives (one with a task/goal orientation and one with a hedonistic/recreational/exploratory orientation) based on this basic theory of shopping motivation. In sum, we argue that identifying the search motive is a prerequisite for providing assistance that is helpful in the relevant search situation.

Existing research has (i) shown that eye movements are well suited to describe information search behavior and choice processes and (ii) provided evidence that consumers’ information needs are dependent on their search motives (goal-directed versus exploratory search). From a managerial (retailer) perspective, questions arise as to whether and how companies can easily and cost-effectively gather consumers’ eye-tracking data (availability of data), whether and how they can predict consumers’ search motive based only on their eye movements (feasibility of approach), and what costs and benefits are associated with this approach (costs and benefits). Against this background, the primary goal of our paper is to show the feasibility of the approach. We therefore answer a call by Shmueli and Koppius (2011), who stated that the “near-absence of predictive analytics in mainstream empirical IS [information systems] research” (p. 554) is a particularly large gap in IS research despite its “great theoretical and practical value” (p. 569). On the basis of the literature and expert knowledge of state-of-the art technology, we also provide solutions for the availability problem and discuss costs and benefits.

We carried out two experiments to collect data to train and test our prediction models in order to achieve our main goal (feasibility of approach). The first experiment involved 29 participants in virtual reality (VR); the second experiment, with 20 participants, was conducted in physical reality, in a real supermarket. In both environments, mobile eye tracking was used to record the participants’ eye movements. We trained our classification model and tested its predictive validity in these two search environments (virtual and physical reality). Altogether, we compared three prediction approaches: logistic regression, support vector machines (SVMs), and random forest.

We decided to conduct the first study in VR for the following reasons. First, virtual stores have relatively recently (in 2018) started entering the mass markets (e.g., eBay, Myer, SATURN, and IKEA). It is therefore extremely relevant from both a research and a managerial perspective to study consumer behavior in this new environment. Second, for technical reasons, eye tracking is a fundamental part of next-generation VR devices, making the data easily available to all future VR shopping environments. Third, VR laboratory studies allow researchers to control for confounding factors and to automatically analyze eyetracking data, making them a powerful supplement for our physical reality study.

Our studies have three major results: First, eyetracking data can accurately classify search motives in both virtual and physical reality. We already achieve 70% prediction accuracy in an early phase of the search process in VR and 75% in physical reality using SVMs. When we apply ensemble methods, we can increase the average prediction accuracy over the whole search process to 90% in VR and to 92% in physical reality. Second, we find a substantial overlap between the best predictors across the two environments (virtual and physical), as well as a substantial overlap with empirical research using clickstream analysis in an e-commerce environment. However, our results also show that the variance of fixation duration is a strong predictor for our life-sized environments. This variable has rarely been discussed in the e-commerce literature. Third, when comparing the e-commerce literature’s results with ours, we find that, compared with the point of sale, e-commerce search behavior is similar in terms of most of the eyemovement variables.

Our paper not only addresses the three major managerial problems—availability, feasibility, and evaluation of benefits and costs—but also makes four main contributions to research. First, we contribute to information systems research by demonstrating that eye-tracking data can provide sufficient information to classify search motives. This can be useful in, for example, designing information systems to personalize assistance systems. Second, we contribute to the field of method research dealing with study environments (e.g., laboratory versus field) and show that there is a substantial overlap between behavior in a virtual reality and physical reality. Third, our paper contributes to the marketing and decision-making literature, as we identify key variables that differentiate between goal-directed and exploratory search motives and explain the procedural differences in line with information processing theory. Fourth, our research is of particular relevance to researchers aiming to investigate human-computer interaction. Because eye-tracking data can be analyzed in real time in VR, it offers research opportunities in this field, particularly regarding interacting with VR simulations (Tanriverdi and Jacob 2000) to support communication in immersive teleconferencing (Duchowski et al. 2004).

We build on prior research by following the crossindustry standard process for data mining design process model (CRISP; see Wirth and Hipp (2000)). CRISP is an often-used standard for data mining projects (Mariscal et al. 2010) and consists of the following six steps: business understanding, data understanding, data preparation, modeling, evaluation, and deployment. Taking an academic rather than an industry perspective in this paper, we refrain from implementing the deployment step and also replace business understanding with “problem and motivation.” As such, our approach resembles the salient parts of the design science paradigm (Hevner et al. 2004, Peffers et al. 2007). More specifically, the problem formulation and motivation of our work is outlined in the introduction In the two follow: ing theoretical sections, we ensure the rigor of our approach by drawing from existing theory and knowledge (Hevner et al. 2004) on both the two search motives and the eye-tracking technology. Section 3 provides insights on the step “data understanding.” We describe the data collection, which is an important part of the step “data preparation,” in detail in the respective subsections on the experimental setup and procedure of studies 1 (VR) and 2 (physical). Furthermore, we elaborate on the data preparation of the two studies in Sections 4.3 and 5.2. As the “modeling” approach is identical for both studies, it is described only for Study 1 in Section 4.4. The “evaluation” step comprises Sections 4.5 and 5.3 as well as Section 6, showing and discussing the empirical results. In Section 7, where we look at managerial implications, we outline how the implementation of the proposed system would add concrete value to an organization or business. As such, we address the call by Hevner et al. (2004) by presenting a solution of a “heretofore unsolved and important business problem” (p. 84) and ensure that we rigorously evaluate its “utility, quality, and efficacy” (p. 85).

## 2. Theoretical and Technical Background on Virtual Reality and Eye Tracking

Recent launches of virtual shopping environments suggest that companies are becoming increasingly interested in using VR technology as a retail channel. Examples are Europe’s largest consumer electronics retailer, SATURN; the Chinese e-commerce company Alibaba; the U.S. department store Macy’s; the Swedish company IKEA; and Amazon, with its VR kiosks. SATURN has created two VR shopping environments in its Virtual SATURN market: consumers can place and interact with the products and sales personnel either in a loft or on the planet Saturn. The shopping environment runs on standard headmounted VR devices, and thus consumers can shop in Virtual SATURN at home. Providers of such VR shopping environments aim to improve their image as pioneers and like to provide hedonic values to their customers. Yet many other benefits of VR shopping environments might be realized in the future with re spect to utilitarian values for the customers, profiling of customers’ needs and personalizing assistance systems (as will be discussed in Section 7).

In this paper, we present the results of two experiments that collect eye-tracking data in a VR shopping environment setup and in a store in the physical reality. Because using eye tracking for learning about user behavior in an immersive VR environment is particularly new for information systems and business research (for an exception, see Bigné et al. (2016)) and has rather been used in other areas such as visual inspections and sports research (see, e.g., Duchowski et al. (2002a) and Diaz et al. (2013)), we first provide background information on VR, on how to use eye tracking in this environment, and on the opportunities to collect eye-tracking data.

## 2.1. De<sup>fi</sup>nition of Virtual Reality

In physical reality, we perceive the physical world directly as first-order sensations and actions have direct consequences that follow the laws of physics. In VR, technology mediates the sensation, which makes VR a second-order sensation. VR is interactive, and users’ actions have consequences, yet there is no direct link between an action and a reaction. Instead, a computer simulation mediates between actions and reactions. VR can therefore be described as interactive computer-generated multimodal secondorder sensations, which users perceive as firstorder sensations.

Instead of this more technical description, VR has also been defined according to its ability to allow users to feel telepresence (Steuer 1992) and its degree of immersion. Telepresence can be defined as the degree to which one feels present in an environment mediated by any communication technology. Immersion describes the degree to which a VR system’s output is comparable to physical stimuli (Bowman and McMahan 2007) and comprises four dimensions: extensive, surrounding, inclusive, and matching (Slater et al. 1995). Because immersion is objective and measurable (Slater 2003, Bowman and McMahan 2007), VR systems can be classified according to their degree of immersion (Gutiérrez Alonso et al. 2008, p. 130): from nonimmersive or semi-immersive to fully immersive systems.

## 2.2. Virtual Reality Display and Interaction Technologies

There are various hardware setups with which to implement visual virtual environments (Loomis et al. 1999): the primary two are head-mounted displays (HMDs) (Sutherland 1968), such as the HTC Vive Pro or Oculus Rift, which are glasses that provide a personal, fully immersive experience, and cave automatic virtual environments (CAVEs) (Cruz-Neira et al. 1993), which are rooms with projection screens (not unlike StarTrek’s HoloDeck) that provide semiimmersive experiences. At the time when our studies were conducted (2015), we decided to use a CAVE for its following advantages: First, CAVEs have the advantage of providing a large field of view and a high pixel resolution. Both aspects are important for observing visual search processes accurately. Second, compared with HMD users, CAVE users perceive their own body and therefore have fewer problems with estimating distance and size. Third, a CAVE provides an isometric environment in which users can walk around naturally, with a 1:1 mapping between their movements in the physical world and the simulated movements in the virtual world, without having to learn or use a controller-based navigation method or having to trust the HMD-based system to prevent collisions with physical obstacles. Additionally, the increased visual stability of a CAVE environment compared with that of HMDs means that there are only a few or no problems with cybersickness, a feeling of nausea and discomfort caused by using VR technology. Since 2015, the introduction of highresolution HMDs and room-scale tracking systems for HMDs have solved many of these issues for consumer devices. Today, the same study could be conducted using consumer HMDs.

All professional VR systems track the user’s head perspective, which is required to create the secondorder stimulations. Different systems can be used for the tracking, ranging from inexpensive inertial (such as accelerometers or gyroscopes) tracking systems (Zhu and Zhou 2004) to expensive full-body motion capturing systems (Moeslund and Granum 2001). Modern consumer HMDs make use of hybrid approaches, combining visual tracking, either inside out (HTC Vive and Windows Mixed Reality) or outside in (Oculus Rift), and inertial tracking to measure both the user’s perspective and the controllers’ position and orientation.

## 2.3. Eye Tracking in Physical and Virtual Reality

In eye-tracking research, we can measure the information a user has actually looked at very precisely. Two different eye-tracking measures are central: a fixation refers to when the “eye remains almost still for a period of time” (Holmqvist et al. 2011, p. 21), whereas a visit (or dwell) is defined as several con secutive fixations on the same area of interest (AOI)— for example, a product.

Eye tracking has a long history in human-computer interaction in VR (Duchowski et al. 2002a, b). Wellknown companies’ acquisitions of eye-tracking companies that offer advanced virtual and augmented reality (AR) technologies (the EyeTribe by Facebook/ Oculus and SMI by Apple, both in 2017) underline the importance of eye tracking for mixed reality. There are four important reasons to have eye tracking in VR devices: identification of the user (implemented e.g., in the HoloLens 2), precise measuring of the positions of the eyes to calibrate the view matrix for the projection of the three-dimensional (3D) graphics; foveated rendering (Godin et al. 2004), in which only fixated areas will be rendered with high quality to reduce power consumption; and gaze-based interaction, to reduce head movements, which are currently required for the head-pointing approach used in many VR headsets. Besides that, precise and low latency data of position and orientation of the eyes are important for creating adaptive optics, for example, to adapt flexible lenses to the depth of fixation to overcome the vergence-accomodation conflict (Kramida 2016), which, at the time writing, is still a technical limitation. These developments will make eye tracking available in AR and for VR displays on a larger scale and at a much lower cost in the near future. The studies in the research at hand were conducted in 2015 and required expensive scientific eye-tracking systems, but, in 2019, companies such as FOVE Inc., Magic Leap Inc., StarVR Corporation, Microsoft, and HTC have already provided systems with built-in eye tracking for the professional and consumer markets.

In physical reality, eye-tracking data recorded on scene videos with mobile devices need to be manually annotated before they can be analyzed (see Meißner et al. (2017) for more detailed explanations), which is very time consuming and subjective. In principle, the scene videos could be (post)processed using computer vision and deep learning to segment and classify regions of interest (semi)automatically. This is not feasible with a 100% success rate, but the technologies are still under development. However, when mobile eye tracking is used in VR, fixations can be automatically assigned to the specific area of interest, and this information is available with minimal effort from the moment the eye fixations are recorded (Meißner et al. 2017). It is therefore possible to build interactive, gaze-contingent systems (Guenter et al. 2012).

The precise calibration of the eye-tracking system for a semantic mapping of gaze and AOIs is a practical eye-tracking problem. Eye-tracking experts have already developed systems with an automatic calibration that a broad range of users can use directly. There are, however, still users who require a calibration or for whom even a calibration will not achieve the necessary precision and accuracy (Blattgerste et al. 2018). However, not all features that can be extracted from eye movements require this external calibration. Fixation count, fixation duration, saccade frequency, and duration, as well as the number of eye blinks, can be measured solely by means of eye images. New interaction and calibration procedures based on smooth pursuit (Vidal et al. 2013) might also be viable alternatives.

In the near future, both worlds (physical and virtual) will come together in AR technology. First consumer AR glasses are equipped with eye tracking (Magic Leap, HoloLens 2). Combined with the localization and environment tracking technologies embedded in such AR-ready smart glasses, automatic gaze mapping is basically an interesting side effect of the technical processes that already run on the hardware. Eyewear computing (see, e.g., Pfeiffer et al. (2016)) is the term coined for these types of devices.

## 3. Theoretical Background on the Two Search Motives

## 3.1. Goal-Directed and Exploratory Search

The marketing and decision-making literature distinguishes two broad categories of shopping motives— goal-directed search and exploratory/experiential. Wolfinbarger and Gilly (2001, p. 35) use the terms “for fun” (exploratory) and “for efficiency” (goaldirected) to describe and distinguish consumers’ divergent orientations. The two shopping motives differ largely regarding consumers’ information search processes and information needs: Consumers undertaking a goal-directed search will be motivated to gather information efficiently by utilizing a search routine or strategy to achieve their goal. By contrast, a consumer with an exploratory search motive is presumed to scan the decision environment and build up knowledge that might become relevant later. Exploratory search can be best described as the browsing and the scanning of a search environment without pursuing a search goal. To summarize, prepurchase deliberation and a goal orientation to complete a task characterize a goal-directed search, whereas building knowledge about a product category or hedonic reasons motivate an exploratory search (Hoffman and Novak 1996).

Moe (2003) further distinguished two goal-directed (directed buying and deliberation and search) as well as two exploratory (hedonic search and knowledge building) search strategies. Deliberation and search as well as knowledge building are particularly interesting (and selected for the experiment) because assistance systems can potentially help consumers find products that best meet their search goals or support the knowledge building process. We refer the reader to Moe (2003) for further deliberation on the other two search strategies.

## 3.2. Procedural Differences Between Search Motives According to Information Processing Theory

We are aware of only two studies (Moe 2003, Chiou and Ting 2011) that investigated the differences between the two search motives with respect to information processing. These studies were conducted in an e-commerce context using clickstream data and not in a physical environment, such as a supermarket. Moe (2003) collected clickstream data from a real online store and applied a post hoc clustering to identify the search motives. Chiou and Ting (2011) directly manipulated the type of search the subjects used in a mock online store that only sold products from two product categories. A product was defined as considered if the user clicked on the product and opened the web page with product details. In the following paragraphs, we review the potential predictors (the predictor names appear in parentheses) that both studies used and explain the procedural differences between the two search motives on the basis of information processing theory.

The average duration a product is viewed (AVG-VISITDURPROD) measures how long a consumer looks at a product before considering the next one. An exploratory search is rather undirected, because the goal is to obtain an overview of the assortment; consequently, it resembles browsing behavior. By contrast, in a goal-directed search, the consumer has to search for particular pieces of information (e.g., on the product packages) to verify whether a product meets her criteria. In line with Chiou and Ting (2011), we therefore expect AVGVISITDURPROD to be longer when consumers have a goal-directed motive than when they have an exploratory motive.

The total number of different products viewed (NUMBDIFFPROD) quantifies how many different products the consumer has clicked on or has fixated on at least once. Pieters and Warlop (1999, p. 3) used the term “filtration” to explain that “consumers skip certain elements of information about the brands in the display, or do not fixate some brands at all.” Consumers with a concrete search goal, such as finding a muesli that “contains chocolate and almonds,” can use (task) knowledge to direct their attention to relevant stimuli. For example, consumers are expected to direct their attention at stimuli with brown colors on the product package. Directing attention to relevant stimuli—that is, filtration—can be achieved with parafoveal and peripheral viewing during scanning (i.e., without looking directly at each product on the shelf) (Janiszewski 1998, Pieters and Warlop 1999). Consequently, in a goal-directed task, we expect NUMBDIFFPROD to be smaller.

The maximum number of revisits (MAXREVISIT) quantifies how often a consumer returns to the most often inspected product. Shimojo et al. (2003) and Shi et al. (2013) found that the ultimately chosen products received more attention and that the likelihood of fixating on the chosen alternative increases until the decision is made. Verification processes offer a possible explanation for this finding. Consumers with a goal-directed motive are expected to more frequently use verification processes by looking at the ingredient, brand, or price information. Consumers with an exploratory motive have no reasons to return to a particular product frequently. Thus, in line with previous eye-tracking studies and Moe (2003), we expect MAXREVISIT to be larger in goal-directed search.

The number of viewings of detailed product information (NUMBDETAIL) and price information (NUMBPRICE) in the goal-directed situation depends on the decision maker’s individual goals. In our experiments, the participants needed to check detailed product information. By contrast, we expect consumers with an exploratory motive to compare products based on information that is relatively easy to access, such as price information displayed on separate price tags, in order to obtain an overview. In line with Moe (2003), we therefore expect consumers with a goal-directed motive to more often view detailed product information, whereas, in line with Chiou and Ting (2011), we expect these consumers to less often look at price information.

## 3.3. Additional Eye-Tracking Measures for Investigating Procedural Differences

Eye-tracking research allows for identifying further information processing measures that might be indicative of the shopping motive.

The number of fixations and visits is one of the most frequently investigated eye-tracking measures (Hyon¨ a et al. ¨ 2003, Holmqvist et al. 2011, van der Lans et al. 2011). NUMBPROD quantifies the number of products visited (including products revisits). Furthermore, the average number of revisits per product measures how often each product is visited on average (AVGREVISIT). Further measures include the percentage of fixations on a brand and a logo (PERCENTBRAND), prices (PERCENTPRICE), or detailed product information (PERCENTDETAIL).<sup>2</sup>

Furthermore, eye tracking allows for measuring the duration of fixations (Holmqvist et al. 2011, van der Lans et al. 2011). Longer average durations have been interpreted as indicating deeper information processing (Rayner 1998, Holmqvist et al. 2011). We will examine the average duration per fixation (AVGDUR), the average fixation duration per product (AVGDURPROD), and the average fixation duration on price, detailed information, and price or logo information (AVGDURPRICE, AVGDURDETAIL, and AVGDURBRAND, respectively), as well as calculate the variances over these duration measures. Equivalent measures can be determined for visits instead of fixations. The duration of a visit is equal to the time interval between the first fixation on the currently fixated AOI and the end of the last fixation on this same AOI. Thus, in contrast to the duration measures, which are based on fixations, the visit measurements include the saccadic times on an AOI. A saccade is a movement of the eyes from one fixation location to the next.

Distance measures that capture the length of saccades are another type of measure. Goal-directed and exploratory search could differ substantially with respect to the length of saccades. Scanning, for example, would lead to an increase in the average saccadic distance between visits to different AOIs. We therefore examine the average distance between two consecutive visits (AVGFIXDIST) and the maximum distance (MAXDIST). We normalize both measures by dividing by the shelf size (the maximum possible distance on the shelf between any two products), because we have different shelf sizes in the different experimental setups.

The fourth and final group of measures are pair and triple comparisons between attributes (Russo and Leclerc 1994). These measures reflect a search strat egy, meaning that they help to identify a search process presumed to be systematic, such as goal-directed search. For example, if a sequence of fixations consists of only two alternatives (e.g., X-Y-X or X-Y-X-Y), the search process can be described as a paired comparison (COMPARE2PROD). If the search contains three products (e.g., X-Y-Z-Y or X-Y-Z-X-Z-Y. . .), it is denoted as COMPARE3PROD.

We refer to Table 4 in the online appendix for a summary of all 22 measures that we retrieved from our literature analysis on clickstream data and the literature on common eye-tracking measures.

## 4. Study 1

## 4.1. Experimental Setup

We conducted the first experiment in the CAVE of the Virtual Reality Laboratory at the Center of Excellence Cognitive Interaction Technology (CITEC) at Bielefeld University and used the Advanced Realtime Tracking Flystick as an interaction device. The front wall displayed a replicated supermarket shelf with 3D models of the products. The projection on the floor displayed dark tiles, as well as a marker indicating a starting point. To the right of the starting point, the participant saw a virtual shopping cart. Details of the technical setup appear in Online Appendix B.

## 4.2. Procedure

Before the experiment started, we asked participants to sign a consent form. Thereafter, we determined the interpupillary distance and each participant’s dominant eye. When entering the CAVE, we gave each participant 3D glasses (polarized filters) with a builtin eye tracker and the Flystick. The cable connecting the eye tracker with the server allowed the participants to move freely in the CAVE. The participants were instructed on how to use the equipment, and the eye tracker was calibrated. We first presented a practice shelf with 24 identical product packages to familiarize the participants with the new virtual environment’s capabilities. In the practice task and the following experiment, the participants could play around with the environment, touch products and turn them around, read detailed information on the packages, and so on.

The experiment was part of a larger study in which each participant had to execute five tasks. Only the first two tasks, in which different products of the same product category (muesli) were displayed, were relevant for this paper (Figure 1(a)). The participants could take the products off the shelf for closer inspection by using the Flystick (Figure 1(b)). They could view the products from different angles, just as they could if they had a real product in their hands. Once the participants had finished the task, they were asked to put the product in the virtual shopping cart (Figure 1(c)), which triggered the transition to the next task. After completing the tasks, the equipment was removed from the participants, and they were asked to answer a questionnaire.

In each of the two tasks, participants saw one shelf comprising 24 types of muesli. The displayed types were randomly drawn without replacement from a total set of 48 types of muesli to ensure the participants never saw a product twice. The products were arranged by brand in order to resemble a real supermarket (Chandon et al. 2009) and in keeping with the two configurations, which differed in respect of where the brands were positioned. We randomized the products’ position on the shelf according to the specific shelf configuration. In a between-subject design, we randomly assigned each participant to either the goal-directed or the exploratory search condition.

The experimental instructions were developed based on prior research in the field. In line with Chiou and Ting (2011) as well as Kaltcheva and Weitz (2006), respondents’ shopping motives were manipulated by providing different shopping scenarios. Our manip ulation is quite similar to the one Kaltcheva and Weitz (2006) used, with specific objectives for each of the products respondents were asked to buy in the taskoriented condition and no specific objectives in the recreation-oriented condition. In the goal-directed task, we asked the participants to select a type of muesli for a friend who would be visiting. We told participants that the friend likes raisins, but not chocolate, and that she prefers a low-calorie muesli

Figure 1. (Color online) Experimental Setup of the VR Experiment  
(a)  
![](/api/attachments/H8KSFXEZ/fulltext/images/0dd1bc2462cfa1cca8d402b1391ced329d487780dc4f835b8abb6032f73fc539.jpg)  
Virtual product shelf

(b)  
![](/api/attachments/H8KSFXEZ/fulltext/images/689006b99410c5e11618408bd01751c2bef7d32b234d2a6dd1b8714a28669a68.jpg)  
Detailedinformation

(c)  
![](/api/attachments/H8KSFXEZ/fulltext/images/8c1fab19e41bfc0cb20142ecbb5bfb2802dd64840a89ffca1ef61d96ad951b6b.jpg)  
Virtual shopping cart

The task was to find a type of muesli in line with the friend’s preferences. We ensured that there was exactly one product on display that fulfilled the requirements for each shelf.<sup>3</sup> Participants in the exploratory motive condition were asked to obtain an overview of the product assortment, to think about product attributes that are important for them, and to finally make a purchase. We decided to let each participant make two choices, because we wanted to increase the number of observations.

## 4.3. Data

In total, 29 students participated in this experiment. Participants wearing glasses or heavy eye makeup were excluded from the study to avoid potential problems with data recording. The participants received V5 and one of the products on display during the experiment as an incentive to participate in the study. Owing to technical problems, we could not record eye movements in some tasks. Our data set therefore consists of 50 observations (26 for task 1 and 24 for task 2). The mean age in the final sample is 22.88 years (SD = 2.49; min = 18; max = 27), with 13 (50%) female participants. Of the participants, 14 (53.84%) were asked to conduct the goal-directed search. On average, the participants in the exploratory motive condition took 127 seconds (SD = 79.9; min = 27; max = 348) and those in the goal-directed motive condition took 151.49 seconds (SD = 64.4; min = 64; max = 405) to finish the task.

## 4.4. The Classi<sup>fi</sup>cation Model

From the participants’ eye-tracking data, we computed all the predictors listed in Table 4 in the online appendix and z-standardized them. We excluded all fixations shorter than 100 milliseconds. We compare the performance of three types of classifiers for the modeling: a logistic regression, a random forest, and an SVM. We utilize two R packages—namely, caret (Kuhn et al. 2018) for classification and regression training and e1071 (Meyer et al. 2017)—to build SVMs. We use polynomial kernels (caret type svmPoly) for SVMs and Breiman’s random forest algorithm (caret type rf, with ntree = 500) for random forests (Breiman 2001), and we optimize the parameters degree, scale, and cost for the SVMs and mtry for the random forests with a parameter grid search.

When using mobile eye tracking in the field or VR, small sample sizes are unavoidable, because only one participant is recorded at a time. Although larger sample sizes are much more common when applying machine learning algorithms, these algorithms have been proven to be useful in settings with small sample size (see, e.g., Krol and Krol (2017)) if certain precautions are undertaken (Witten et al. 2016). We used a leave-one-out cross-validation to increase the size of the training in order to evaluate the models and also compared it with 0.632 bootstrap (we refer to Witten et al. (2016) for details on these concepts) Because the bootstrap approach tends to be optimistic (Aggarwal 2015), we decided to use the onefold crossvalidation. Finally, we keep the model complexity low by only allowing a maximum of four predictors per model (Hastie et al. 2013, Aggarwal 2015). If the sample size is small or hardly larger than the number of features available, the model is prone to overfitting (James et al. 2013, pp. 203–204). Keeping the number of predictors small also results in a cost-efficient predictor (Guyon and Elisseeff 2003), which is particularly important, as our goal is to predict the search process on the fly (i.e., while the participant is making a decision). Focusing on a smaller set of variables also facilitates the interpretation of the parameters.

We consider only the first 100 seconds of the data: First, the participants can stop searching whenever they like, which means we then have fewer observations with which to train the classifiers later in the search process. Participants in the exploratory motive condition stopped searching earlier than those in the goal-directed motive condition. After 100 seconds, 37.5% (11.53%) of the participants with an exploratory (goal-directed) motive finished their search. Figure 5 in the online appendix provides more details of the dropout rate. Second, we try to predict the search motive as early as possible, because our goal is to provide assistance based on the predicted situation. Third, we analyze a restricted time span, because we try to classify the search motive on the fly and not post hoc, when the search has been completed. We can therefore only use eye-movement information observed until time step t. We therefore need to rebuild the model for every next second, which is when additional eye fixations and movements are observed. Consequently, we need to build 99 models for the first 100 seconds (we start at second 2). The variable NUMBPROD, which is the number of products visited (including revisits), is an appropriate example. Up to time $t ,$ we can count the number of products visited. $\mathrm { A }$ participant might have visited products 1, 12, 3, and 1 up to second t 10. The NUMBPROD would then be 4 for the model computed for second t 10. If, in the next second, the participant looks, for example, at product with ID $6 ,$ the prediction model for t 11 would use NUMBPROD 5 as an input. This approach helps us detect how much time needs to be observed to classify the observation satisfactorily.

We determined the time frame of 1 second based on the fixation duration, which is typically between 150 milliseconds and 500 milliseconds. In 1 second, between two and seven fixations will therefore be added to the data, which provides enough potential for a substantial change in the search process and enough potential for the prediction of the search motive to change. In future applications, the timely detection of the search motive is crucial, as the system should provide help when it is needed. We therefore decided against using longer time frames.

Because we build a new model for every second, it is possible that the predictor variables that perform best differ from second to second. We therefore choose the model with the best average prediction accuracy over the whole time span (up to second 100). We then compare the performance of the three different modeling approaches, binary logistic regression, SVM, and random forest.

## 4.5. Results

Figure 2 shows the best models, and Table 1 reports the mean of all 99 models with respect to accuracy, recall, and precision. The SVM performs significantly better than the regression (80.23% versus 74.74%, tested with two-sided paired t-test) and the random forest (79.50%). In the first 15 seconds, SVM achieves 70% accuracy and random forest 80%. The random forest is more suited for prediction in the first half of the time period, after which SVM outperforms it (tested with paired t-tests). This is also clear when comparing the predictors that the approaches select as the best subset out of the 22 predictors. Although the SVM’s choice is almost identical to the regression, it differs substantially from the random forest. NUMBPROD is the most important predictor in all three approaches, but its importance decreases toward the end of the search process, whereas the importance of VARAVGDUR in the SVM and the regression increases. In the SVM, MAXRE-VISIT is particularly important toward the end of the process (for details, see Figure 6 in the online appendix).

The recall and precision measures<sup>4</sup> indicate that SVM and random forest perform well on all four measures; however, the random forest seems to better address the trade-off between recall and precision, whereas SVM tends to more often predict that the goal-directed motive would be used. Please note that goal directed is the class that appears slightly more often than the explorative class with 54% versus 46% of observations being goal directed.

Figure 2. Study 1: Best Models for the VR Study  
![](/api/attachments/H8KSFXEZ/fulltext/images/1cd2264a46cf459b111727015da7e8431cb9510c1a3937ad3b8d5a14538b6344.jpg)

To summarize, we demonstrated that the two shopping motives can be classified with an accuracy of about 80% in VR. Because we only used eye-tracking information in our prediction model, this is a substan tial improvement compared with a random guess. Because no other work has yet predicted the two search motives solely on eye-tracking data, we cannot provide any other benchmark.

Several questions remain that we aim to address in Study 2. First, will the same prediction accuracy be achieved in physical reality? Second, does our prediction model also work in other product categories? Third, can we improve the prediction accuracy by using ensemble methods?

## 5. Study 2

## 5.1. Experimental Setup

Study 2 is an experiment in the field in a mediumsized supermarket. We asked each participant to perform four search tasks, each in a different product category (muesli, cereal, marmalade, and tea). The participants had to use a goal-directed motive in two tasks and an exploratory motive in another two tasks. The participants started randomly with either a goaldirected or an exploratory search. In each product category, we used the products that were offered by the supermarket as experimental stimuli. The participants could choose from 117 types of muesli, 76 types of cereal, 202 kinds of marmalade, and 190 tea varieties. The instructions of the different task types were equivalent to the ones used in Study 1. For an overview of the key characteristics of each task, see Table 5 in the online appendix.

The participants wore SMI eye-tracking glasses with 30 Hz and an accuracy of 0.5 degrees, a scene camera gaze overlay with 24 Hz at a resolution of 1280 × 960, and a field of view of $6 0 ^ { \circ } \times 4 6 ^ { \circ }$ . Fixations were annotated manually, because there is as yet no reliable solution for automatically annotating gaze data collected with mobile eye tracking in a natural environment (Meißner et al. 2017).

## 5.2. Data

We recruited 20 shoppers directly when they entered the supermarket. The participants were 31.3 years old on average (SD = 13.27; max = 53), of whom 14 (70%) were female. As an incentive to participate, the participants received V10. As there were four tasks to complete, the data contained 80 observations, but because of problems during recording with the USB port, 13 observations are incomplete. Furthermore, three participants had to be excluded because for these, despite calibration, only a low accuracy for gaze estimation could be achieved. As a result, 17 complete observations remained for the category muesli, 14 for cereal, 15 for marmalade, and 15 for tea. In total, 29 (47.5%) of the 61 observations were goal directed and 32 (52.5%) exploratory. It took the participants an average of 93.31 seconds (SD = 64.03; min = 1.84; max = 338.04) to complete tasks with an exploratory motive, which is less than for those with a goal-directed motive, which took the participants 163.72 seconds (SD = 115.91; min = 24.69; max = 458.10) on average. Figure 7 in Online Appendix C provides an overview of the number of observations per second we collected in the two search motives. The coding of the video material was done at each 10th of a second once the data collection had been finished. The details of the coding procedure can be found in Online Appendix C.

Table 1. Study 1: Prediction Accuracy of the Best Models

<table><tr><td>Approach</td><td>Predictors</td><td>Prediction accuracy (%)</td><td>GD recall (%)</td><td>GD precision (%)</td><td>EXP recall (%)</td><td>EXP precision (%)</td></tr><tr><td>Regression</td><td>NUMBPROD, VARAVGDUR, AVGDUR, COMPARE2PROD</td><td>74.74</td><td>80.62</td><td>74.66</td><td>67.87</td><td>75.04</td></tr><tr><td>Random forest</td><td>NUMBPROD, COMPARE2PROD, VARVISITDURPROD, VARVISITDUR</td><td>79.50</td><td>81.33</td><td>80.86</td><td>77.37</td><td>78.27</td></tr><tr><td>SVM</td><td>NUMBPROD, VARAVGDUR, AVGDUR, MAXREVISIT</td><td>80.23</td><td>85.79</td><td>79.93</td><td>73.71</td><td>81.30</td></tr></table>

We used the same prediction models and procedure for training and testing as in Study 1 (see Section 4.4) and therefore present the results directly in the following section.

## 5.3. Results

Figure 3 and Table 2 show the physical reality’s results. With an average accuracy of 85.41%, SVM performs significantly better than both the regression (76.46%) and the random forest (75.71%). In the first 15 seconds, SVM already achieves a 75% accuracy. Again, SVM and regression pick similar predictors with the difference that SVM focuses on only two—namely, NUMBPROD (with decreasing importance over time) and VARAVGDUR (with increasing importance). Whereas the random forest uses duration measures, the regression includes the strategy measure (COMPARE2PROD). VARAVGDUR is the most important predictor in all three approaches (see Figure 8 in the online appendix).

Figure 3. Study 2: Best Models for the Study in the Physical Reality  
![](/api/attachments/H8KSFXEZ/fulltext/images/04df43e7269884bbf5fcfeec3d07b519384c1eba43bf4b9ca0ab20cd4dce8909.jpg)

## 6. Discussion and Further Improvement of Results

6.1. Comparison of the Models of Both Studies We compare the classification models of the two studies according to two criteria—namely, the predictors and classification algorithms that perform best and the accuracy achieved.

SVMs outperform random forests and regressions in both environments, with random forests ranking second and dealing better with the trade-off between recall and precision. Both environments’ predictors overlap substantially. In VR, the model with four predictors performs best. These predictors include only two types of metrics: fixations and visits (NUMBPROD and MAXREVISIT) and the duration of fixations (VARAVGDUR and AVGDUR). Metrics of AOIs such as price, detailed product information, or brand/logo; distance metrics; and strategy metrics (such as COMPARE2PROD) are not included as predictors, which is a promising result. These would require extra computational efforts if they were to be implemented in a real-time application.

The best predictors of the physical reality study are NUMBPROD and VARAVGDUR, which are a subset of the predictors suggested as predicting search motives in VR. These predictors’ similarity is a first indication that the participants behaved similarly in both environments. It is remarkable that such a high prediction accuracy can be achieved by only using these two variables. Furthermore, the variance over the average fixation duration performs well across both environments (virtual and physical reality), even when we vary the number of products displayed between 24 and 202.

Overall, the prediction accuracy was significantly (paired t-tests) better in physical reality (85.41%) than in VR (80.23%), although the VR offered a higher experimental control, with more accurate eyetracking data (Section 2.3). A reason might be the bigger sample size of the study or the larger number of observations per participant. Given the baseline of roughly 50% for a random guess, both results are promising, which is noteworthy, as the identified best approaches use only a few distinct eye-tracking measures.

Table 2. Study 2: Prediction Accuracy of the Best Models for the Study in the Physical Reality

<table><tr><td>Approach</td><td>Predictors</td><td>Prediction accuracy (%)</td><td>GD recall (%)</td><td>GD precision (%)</td><td>EXP recall (%)</td><td>EXP precision (%)</td></tr><tr><td>Regression</td><td>NUMBPROD, VARAVGDUR, COMPARE2PROD</td><td>76.46</td><td>64.68</td><td>82.57</td><td>87.17</td><td>73.00</td></tr><tr><td>Random forest</td><td>NUMBDIFFPROD, VARAVGDUR, AVGDURDETAIL, AVGVISITDUR</td><td>75.71</td><td>71.22</td><td>76.51</td><td>79.79</td><td>75.18</td></tr><tr><td>SVM</td><td>NUMBPROD, VARAVGDUR</td><td>85.41</td><td>75.99</td><td>92.34</td><td>94.04</td><td>81.41</td></tr></table>

## 6.2. Further Model Improvements

In the analyses described so far, we restricted our modeling approaches to simple models, because we only consider the pure application of one machine learning approach and a fixed set of predictors for the entire time span. Ensemble methods that combine multiple models have the potential to produce more precise predictions. The main idea of ensemble methods is to combine a set of models, each of which solves the same original task (we refer to Opitz and Maclin (1999) and Kuncheva (2004) for details on these concepts). We therefore tried two ensemble methods. In the first attempt, we applied each of the three models with their respective parameters and predictors that we had found to perform best in our main analysis (Tables 1 and 2) and let it predict the class label. No new training was required. This approach resulted in three predictions per second per observation. We then assigned the class label to the observation that was predicted by at least two of the three methods (for details on this majority vote, we refer to Kuncheva (2004)). However, with an average prediction accuracy of 75.90% for Study 1 and 76.34% for Study 2, the prediction accuracy was not an improvement on the simple models. It seems that SVM is clearly the better approach, and an outvote of the two other approaches, regression and random forest, weakens the results.

In a second attempt, we kept only the best approach, SVM, but allowed the predictors to vary per second. As we had already done a complete enumeration of all predictor combinations for each second in our main analysis, the implementation of this approach was easy. As for our first ensemble attempt, no new training was required. For each second, we just selected the SVM model that had performed best, with its set of parameters and predictors. The results (see Figure 4) improved significantly to an 89.81% average prediction accuracy for VR and 92.47% for physical reality. However, this improvement comes at a cost, because the ensemble needs 49 predictor combinations for the VR setup and 47 for the physical reality one. Furthermore, in both environments, all 22 predictors are used in at least one model.

## 6.3. Comparison with Desktop-Based Clickstream Studies and Theoretical Implications

Table 3 compares the results of the two clickstream studies discussed in Section 3.2 with those of our own two studies. Moe (2003) and Chiou and Ting (2011) examined the differences when observing the entire search process but were unable to investigate how information processing changed during the task. We therefore also report the results referring to the course of the search process. Please note that Moe (2003) did not test for significant differences.

As can be seen from Table 3, with regard to most of the measures, we find strong empirical support for the two e-commerce studies’ results. Our findings similarity to those of Moe (2003) and Chiou and Ting (2011) surprised us, mainly because the process data were substantially different and because the search context differs substantially (e-commerce site versus life-sized shelf displays).

It is worthwhile reflecting on which expectations formulated in Section 3.2 hold and speculate which procedural differences between the two search motives lead to the observed differences in eye-tracking measures. First, filtration allows respondents to direct attention to relevant stimuli. We find evidence for greater selectivity of attention to a smaller set of stimuli as NUMBDIFFPROD (as well as NUMBPROD that includes revisits) is smaller when respondents have a goal-directed search motive. Interestingly, the results show that the effect does not change (GD < EXP for all seconds), suggesting that filtration is a process that applies from the start to the end of the search and regardless of whether the search takes place in virtual or physical reality. Similarly, detailed search is a process that applies throughout the search, as respondents mostly need to look at details to achieve their search goal. The results for detailed search also do not differ between virtual and physical reality. Our results suggest that filtration and detailed search are fundamental processes that change when respondents use different search motives.

Figure 4. Ensemble Method: Best SVM Model per Second  
![](/api/attachments/H8KSFXEZ/fulltext/images/e2a43cbed579874b95db7ee9b1bb8f35e3af1e6f05bd39d9baa0c880c4ae6316.jpg)

Table 3. Comparison of Own Results with Studies Using Clickstream Data

<table><tr><td>Measure</td><td>Moe (2003)(no significance tested)</td><td>Chiou and Ting (2011)</td><td>Expectations developed in Section 3.2</td><td>VR data</td><td>Physical reality data</td></tr><tr><td>AVGVISITDURPROD</td><td>—</td><td>GD &gt; EXP</td><td>GD &gt; EXP</td><td>GD &lt; EXP (not sign. 2–48), GD &gt; EXP (sign. 70–74, 77–86, 99, and 100)</td><td>GD &gt; EXP (not sign.; for some seconds, GD &lt; EXP)</td></tr><tr><td>NUMBDIFFPROD</td><td>GD &gt; EXP</td><td>GD &lt; EXP (not sign.)</td><td>GD &lt; EXP</td><td>GD &lt; EXP (sign. 6–32, 43–59, 79, 84–93, and 100)</td><td>GD &lt; EXP (sign. 9–94)</td></tr><tr><td>MAXREVISIT</td><td>GD &gt; EXP</td><td>—</td><td>GD &gt; EXP</td><td>GD &lt; EXP for 10–46 (sign. only for 24–32 (not 27)), GD &gt; EXP for 47–100 (sign. from 67)</td><td>GD &lt; EXP (not sign.; for seconds 4 and 6, GD &gt; EXP)</td></tr><tr><td>NUMBDETAIL</td><td>GD &gt; EXP</td><td>—</td><td>GD &gt; EXP</td><td>GD &gt; EXP (sign. 47–100)</td><td>GD &gt; EXP (sign. 21–100)</td></tr><tr><td>NUMBPRICE</td><td>—</td><td>GD &lt; EXP</td><td>GD &lt; EXP</td><td>GD &lt; EXP (not sign.)</td><td>GD &lt; EXP (sign. 18–94, not 27–29)</td></tr></table>

Notes. We report the differences in the variables during the process (seconds 1–100). Time spans whose differences are significant appear in parentheses (one-sided t-tests). GD, goal directed; EXP, exploratory; sign., significant.

Second, the results of the variables AVGVISITDUR-PROD and MAXREVISIT suggest that the relevance of verification processes largely changes during the search. Analyzing the VR data on a second-to-second basis, we find that, in the early phases of the search process, AVGVISITDURPROD and MAXREVISIT tend to be smaller in goal-directed search. The results contradict our initial expectations and also the findings by Moe (2003) and Chiou and Ting (2011). We theorize that changing the relevance of verification processes in goal-directed search causes the observed differences between the search motives. The information processing literature (Janiszewski 1998, Pieters and Warlop 1999) suggests that participants with goal-directed motives scan the environment when they begin the search process to identify potential target products that need to be examined in more detail. When scanning, they will look at many different products. At the same time, the fixations used for scanning are, on average, shorter (the result for AVGDUR), in line with Glockner and Herbold (¨ 2011), and can therefore reduce the average duration of visited products (AVGVISITDURPROD). Verification processes are therefore less relevant in the beginning of the search but more relevant at the end. The findings for the variable VARAVGDUR, which is a key predictor in our approach, also support this theoretical explanation. We find that the variance in average fixation duration is much larger for goaldirected search (GD > EXP for all seconds), which is plausible because short fixations are used for scanning, but longer fixations are used for verification processes in goal-directed search. In exploratory search, changes in the use of scanning and verification processes are less prevalent, as indicated by a smaller variance in fixation durations.

We further speculate that the lower familiarity with VR might have increased the amount of scanning early in the search process, which could explain the observed differences between the virtual and physical environment. A future research step might therefore be manipulating respondents’ familiarity with the environment to examine the effect on verification and scanning processes.

## 7. Managerial Implications

The key suggestion of our paper is that eye-tracking data can be used as input for consumer assistance systems such as recommender or consumer decision support systems. In this section, we consider managerial implications and discuss the benefits of the approach. Costs of and guidance on implementation and operation as well as privacy risks of the proposed approach are further outlined in Online Appendix E.

## 7.1. Bene<sup>fi</sup>ts of Virtual Reality as Shopping Environment

As outlined in Section 2.3, eye tracking has recently been integrated in VR and AR devices, and eyetracking data can be automatically and instantly analyzed in VR. Therefore, we will first discuss virtual shopping environments in which implementing our approach is particularly easy and relevant.

Besides all the advantages of standard e-commerce, virtual shopping environments provide multiple sensorial experiences in that they use visual, audio, olfactory, and haptic channels (MacLean 2008, Berg and Vance 2017). High-immersive virtual environments have also been shown to generate hedonic benefits (Lau and Lee 2019) and positively influence user adoption via a hedonic path (Peukert et al. 2019). Burke (2018) and Bonetti et al. (2018) argued that VR and AR technology has the potential to provide more emotionally engaging customer experiences during the purchase journey. When technical problems such as low resolution are resolved in future equipment, the full potential of VR shopping might unfold. This will also apply to utilitarian values (Peukert et al. 2019), for example, because of enriched possibilities to evaluate the size, color, or style of products such as apparel or furniture (Lau and Lee 2019). Cowan and Ketron (2019) emphasized that VR environments may reinforce customer participation and cocreation if the environment generates a high level of engagement, interaction, and enjoyment. Virtual shopping environments therefore offer opportunities to use cocreation as an instrument to foster strong relationships with customers.

Virtual shopping environments can also be extended to allow social interaction, because consumers could communicate with sales personnel or with friends in the form of avatars. Tracking the user’s eye movements will improve understanding of the communication processes between users, or between users and sales personnel. VR might foster information sharing, processing efficiency, and collaborative learning (Boyd and Koles 2019) if users have the possibility to interact with other users or retail agents. Similarly, virtual retail avatars can interact with users based on eye-tracking information. For example, a virtual sales agent could approach the customer if the gaze indicates that the customer needs help.

## 7.2. Bene<sup>fi</sup>ts of Personalized Assistance Based on Search Motives

The benefits of our approach can be classified as indirect (in line with the framework proposed by Iacovou et al. (1995)). The rationale of the argument is that personalizing the shopping experience and profiling customers’ needs as described in the following sections will enable the generation of additional value for customers and will also increase customer satisfaction and loyalty, which will create competitive advantages (Inman and Nikolova 2017).

The proposed approach can be used to identify customers with exploratory search motives who have a less concrete purchase goal. Identifying browsing offers opportunities for marketers to persuade consumers to buy and not just browse (Lee et al. 2018), for example, by offering special coupons or showing advertisements. The point when a consumer decision support system actively approaches the user might be dependent on the search motive. We speculate that users in a goal-directed search situation might want assistance at an earlier stage than users with an exploratory motive. In an additional study (Online

Appendix D), we found that consumers in an exploratory search want other assistance functionalities than those in goal-directed situations. In exploratory situations, they see value in receiving product recommendations (based on the similarity to other customers), special offers, and discounts. By contrast, consumers in a goal-directed search situation favor product filters that eliminate products based on thresholds as well as recommendation agents that elicit preferences through an explicit user dialogue before providing recommendations. In addition, we speculate that in exploratory search situations, social shopping is more important than in goal-directed situations. For example, users might be particularly interested in communicating with friends and getting advice from influencers.

## 7.3. Bene<sup>fi</sup>ts of Using Eye Tracking for Pro<sup>fi</sup>ling of Customers’ Needs

Beyond what has been suggested so far, individuallevel eye-tracking data can be seen as an instrument to more precisely profile customers’ needs. For example, eye-tracking allows marketers to identify which products and brands potentially interest customers. Research has shown that fixation frequency is strongly correlated with the individual utility values of products in consumer choice (see an alternative focus effect in Meißner et al. (2016)). Retailers can analyze eye-tracking data and build individual consideration sets consisting of brands the customer gazes at frequently, in a similar way as it has been proposed for household panel data (Van Nierop et al. 2010). Consideration sets can then be used as a source for targeted advertisements. For example, a customer can be made aware that a product in her consideration set is on sale. Moreover, the analysis of the search process might comprise other simple eye-tracking measures that indicate price sensitivity (or brand attractiveness). For example, it can be easily quantified how often a customer looks at price tags or how early price information is considered when searching. This information could be used for customized pricing, in case consumers respond positively (David et al. 2017). Similarly, consumers can be made aware of products that address very personal needs. For example, consumers with special health concerns could be guided to products that best fit their dietary needs.

## 7.4. Bene<sup>fi</sup>ts Resulting from the Use of Eye Tracking Instead of Direct Questioning or Clickstreams

Eye tracking is a value-adding alternative to other approaches, such as directly asking the consumer or analyzing clickstreams (Moe 2003, Chiou and Ting 2011). In comparison with the first approach of selfreports, eye tracking is unobtrusive and does not rely on explicit user input, nor does the user have to spend time when using the system. Both aspects have been considered as important dimensions of consumer effort (Xiao and Benbasat 2007). Reducing user input has been a primary goal, particularly in the field of decision aids and recommender systems for consumer decisions (De Bruyn et al. 2008, Scholz et al. 2017). A system that interrupts consumers too often may generate information overload in two ways (Speier et al. 1999). First, attention is taken away from making a purchase and turned toward the interruption. If the same sensory channel (e.g., the visual system) is used, structural inferences may result. Second, the interruptions can place greater demand on cognitive processing.

Clickstreams as well as eye tracking are implicit and unobtrusive, with the above-mentioned advantages. Compared with clickstreams, eye tracking provides more fine-grained data and also renders data from the first second of the choice process. Eye movements are rarely under volitional control, which means that the system will get very reliable input data, as respondents can hardly withhold their true interests indicated by their gaze (Section E.2 in the online appendix contains a discussion on the data privacy implications). Finally, in AR and VR settings, there are little clickstream data available. This is why in these environments interaction data such as body movement or sensor data from smartphones are usually used to make systems context aware.

## 8. Conclusions and Limitations

In this paper, we analyzed whether eye movements can be used to classify two search motives: goaldirected and exploratory search. To this end, we conducted a laboratory experiment that studied users information search in a virtual supermarket and compared the result with an experiment in the field in a physical supermarket. From the data, we trained three classifiers by using predictors based on eyemovement data. Because the proposed system makes use of eye-tracking data as a primary data input source, our research is built on the assumption that users direct their gaze to stimuli that are relevant to execute the specific search motive, which is that gaze direction is primarily controlled by top-down processes (Orquin and Mueller Loose 2013).

A first limitation is related to the instructions we used in the empirical studies. In the exploratory search condition, participants were instructed to “obtain an overview of the product assortment.” Because the word “overview” is semantically related to the words “view” and “eye” and the expression “look it over,” we might have implicitly instructed participants to look at a large number of products in the exploratory search condition. Besides this effect, we do not think the instructions suggested (either explicitly or implicitly) that participants should process the information in a specific way.

A second limitation of our study is that we dichotomized the search behavior as being either goal directed or exploratory (in line with Janiszewski (1998)) When shopping outside the experimental context, customers may exhibit different degrees of goaldirectedness (Hui et al. 2009) and might switch between exploratory and goal-directed search motives. One first approach to investigate that question with our algorithm and our training data would be to consider class probabilities: in case the algorithm does not really differ between classes when predicting, this points to a case where the extent of goal-directedness is probably rather weak.

Despite these limitations, the empirical results of both studies indicate that the future development of assistance systems using eye-movement data are promising: First, using a standard SVM, we predict search motives with a high degree of accuracy early on in the process. Second, the model is based on sets of variables that are easy to record with eye trackers— namely, the number and duration of fixations and visits. As long as objects in the environment can be easily separated, these measures could be easily determined on the fly, even without deeper knowledge about the object’s semantics (meaning that the measure does not include knowledge about the specific type of muesli somebody looked at or even that these objects were types of muesli or the category of information (price, brand, etc.) looked at). Other measures, such as saccades (the distances between fixated objects) or strategy measures, were not included in the best prediction models. In the physical reality also, only two predictors are required, which is very promising, as determining eye-tracking measures on the fly is more difficult in physical reality compared with VR (see Section 2.3). Third, we did not need to rely on a user-specific training of the models. The observations across the different tasks (search mo tives) were treated independently. The classifier would therefore achieve the accuracy reported here in respect of an unknown, new user. Fourth, although we did not include the task order information in the models, we expect prediction accuracy to increase if potentia learning effects would be integrated to personalize the models. Fifth, the results were robust across four product categories. As a consequence, the results in dicate that there is no need to develop different models for different product categories. Sixth, the results were robust across two environments—an immersive virtual environment and a physicalenvironment. Seventh if using slightly more advanced ensemble methods that rely on the computation of all 22 predictors, the performance increases substantially, reaching about

90% accuracy on average. In many search and choice contexts, eye-movement patterns vary substantially between individuals (Rayner 1998, van der Lans et al. 2008); a classifier that has to work for unknown users, as in our paper, might therefore not achieve a much higher degree of accuracy.

The inclusion of other measures, such as users interaction with their hands and personal data (e.g., past purchases, profile data, knowledge about the need for cognition (Cacioppo et al. 1996), or the need for cognitive closure (Webster and Kruglanski 1994) could further increase prediction accuracy. But achieving greater accuracy might be unnecessary, as the current level might already allow for classifying consumers sufficiently. Future research needs to justify this conjecture.

Shopping in VR might soon enter the mass market, which makes this paper interesting from a practical standpoint. Nevertheless, our study is also interesting from a methodological viewpoint. In general, research strongly needs to replicate laboratory studies in environments offering a high degree of ecological validity. Indeed, conducting experiments in VR might help resolve researchers’ trade-off conflict (Loomis et al. 1999) between experimental control and ecological validity. In VR, experimental factors can be controlled, and the high degree of telepresence should elicit behavior similar to that in physical reality. Furthermore, the full experimental setup can be archived and made available to other researchers to replicate the experiment and validate the results. Because everything that happens in the experiment is programmed precisely, this allows for rigid experimental descriptions (the VR simulation is the fully specified description of the experiment), which were rarely achieved in the past. However, Foulsham et al. (2011) and Kahn (2017) emphasized that participants information search and behavior might differ substantially between the laboratory and physical (natural) environments. We therefore call for research that compares behavior in the virtual versus the physical reality. This paper makes a first contribution by showing the similarities between the two environments regarding information search behavior.

A few empirical studies have demonstrated the usefulness of eye tracking to adapt information systems in the context of online recommender systems using desktop-based eye tracking (e.g., Xu et al. (2008) and De Melo et al. (2015)). In this paper, we go a step further and study whether, at the point of sale, we can also predict users’ search situation using mobile eye trackers. In future work, our prediction model could be tested for incorporation into a recommender system in virtual or AR shopping environments. In addition to that, our approach can be considered similar to apps that use the inertial measurement units in smartphones to count steps and other activities to provide higher-level personalized services such as fitness coaching. Both approaches also share the same privacy issues and concerns. Once smart eye glasses are fashionable, a classification of user behavior based on visual search patterns, as prototypically realized in this paper, will be a stepping stone to providing higher-level services in the physical world using AR technology.

Shmueli (2010) stated that “bridg[ing] the gap between methodological development and practical application can be easier to achieve through the combination of explanatory and predictive modeling” (p. 304), because “they [predictive models] also play an important role alongside explanatory mod eling in theory building and theory testing” (Shmueli and Koppius 2011, p. 553). Indeed, these authors argue that this is especially true in fast-changing environments, which VR and e-commerce most certainly are. In sum, our paper makes important contributions by assessing the practical relevance of individual predictors and by formulating expectations about these predictors’ causal relationship to search behavior (Shmueli 2010). This paper sheds light on the actual performance of existing empirical models based on clickstream data and shows that the relevant variables studied to date do not best predict search motives. Our predictive model also creates a benchmark because it quantifies a phenomenon’s level of predictability (Ehrenberg and Bound 1993). It should therefore be interesting to develop the model further for practical application and to develop exploratory models based on our explorative findings in future research, in order to contribute more strongly to consumer behavior theory.

## Acknowledgments

The authors gratefully acknowledge the senior editor, the associate editor, and the reviewers for their constructive feed back, thoughtful guidance, and support.

## Endnotes

<sup>1</sup> Please note that, in line with Janiszewski (1998), we use the terms “goal-directed” (for deliberation and search) and “exploratory” (for knowledge building) search in this paper to simplify the use of the terminology.

<sup>2</sup> We will include these percentages instead of the absolute values (NUMBERBRAND, NUMBPRICE, and NUMBDETAIL) in ou models.

<sup>3</sup> Because our goal was to manipulate the goal-directed motive explicitly, we had to give the participant concrete instructions regarding the product characteristics to search for. As one of the reviewers noted, the goal-directed motive in our experiment might still differ from the average consumer’s goal-directed motive if such a consume only plans her purchase in respect of the brand or product category but does not have more concrete purchase plans.

<sup>4</sup> GD (EXP) recall means that we interpret goal directed (exploratory) as the true class.

## References

Aggarwal CC (2015) Data Mining (Springer International Publishing, Cham, Switzerland).

Ajanki A, Hardoon DR, Kaski S, Puolamaki K, Shawe-Taylor J (2009) ¨ Can eyes reveal interest? Implicit queries from gaze patterns. User Model. User-Adapted Interaction 19(4):307–339.

Bednarik R, Vrzakova H, Hradis M (2012) What do you want to do next: A novel approach for intent prediction in gaze-based in teraction. Spencer SN, ed. Proc. Sympos. Eye Tracking Res. Appl. (ACM, New York), 83–90.

Berg LP, Vance JM (2017) Industry use of virtual reality in product design and manufacturing: A survey. Virtual Reality 21(1):1–17.

Bigné E, Llinares C, Torrecilla C (2016) Elapsed time on first buying triggers brand choices within a category: A virtual reality-based study. J. Bus. Res. 69(4):1423–1427.

Blattgerste J, Renner P, Pfeiffer T (2018) Advantages of eye-gaze over head-gaze-based selection in virtual and augmented reality under varying field of views. Porto M, Majaranta P, eds. Proc. Workshop Comm. Gaze Interaction (ACM, New York), Article 4.

Bonetti F, Warnaby G, Quinn L (2018) Augmented reality and virtual reality in physical and online retailing: A review, synthesis and research agenda. Jung T, tom Dieck M, eds. Augmented Reality and Virtual Reality (Springer, Cham, Switzerland), 119–132.

Bowman DA, McMahan RP (2007) Virtual reality: How much im mersion is enough? Computer 40(7):36–43.

Boyd DE, Koles B (2019) Virtual reality and its impact on B2B mar keting: A value-in-use perspective. J. Bus. Res. 100(July):590–598. Breiman L (2001) Random forests. Machine Learn. 45(1):5–32.

Burke RR (2018) Virtual reality for marketing research. Moutinho L, Sokele M, eds. Innovative Research Methodologies in Management— Volume II: Futures, Biometrics and Neuroscience Research (Springer, Cham, Switzerland), 63–82.

Cacioppo JT, Petty RE, Feinstein JA, Jarvis WBG (1996) Dispositional differences in cognitive motivation: The life and times of indi viduals varying in need for cognition. Psych. Bull. 119(2):197–253.

Chandon P, Hutchinson WJ, Bradlow ET, Young SH (2009) Does instore marketing work? Effects of the number and position of shelf facings on brand attention and evaluation at the point of purchase. J. Marketing 73(6):1–17.

Chiou JS, Ting CC (2011) Will you spend more money and time on internet shopping when the product and situation are right? Comput. Human Behav. 27(1):203–208.

Cowan K, Ketron S (2019) A dual model of product involvement for effective virtual reality: The roles of imagination, co-creation, telepresence, and interactivity. J. Bus. Res. 100(July):483–492.

Cruz-Neira C, Sandin DJ, DeFanti TA (1993) Surround-screen projection-based virtual reality: The design and implementation of the CAVE. Proc. 20th Annual Conf. Comput. Graphics In teractive Techniques (ACM, New York), 135–142.

David ME, Bearden WO, Haws KL (2017) Priced just for me: The role of interpersonal attachment style on consumer responses to customized pricing. J. Consumer Behav. 16(6):e26–e37.

De Bruyn A, Liechty JC, Huizingh EK, Lilien GL (2008) Offering online recommendations with minimum customer input through conjoint-based decision aids. Marketing Sci. 27(3):443–460.

De Melo EV, Nogueira EA, Guliato D (2015) Content-based filtering enhanced by human visual attention applied to clothing recommendation, 2015 JEEE 27th Internat, Conf. Tools Artifi cial Intelligence (IEEE Computer Society, Los Alamitos, CA), 644–651.

Diaz G, Cooper J, Rothkopf C, Hayhoe M (2013) Saccades to future ball location reveal memory-based prediction in a virtual-reality interception task. J. Vision 13(1):1–14.

Dickinger A, Stangl B (2011) Online information search: Differences between goal-directed and experiential search. Inform. Tech. Tourism 13(3):239–257.

Duchowski AT, Medlin E, Cournia N, Gramopadhye A, Melloy B, Nair S (2002a) 3D eye movement analysis for VR visual in spection training. Vertegaal R, Senders JW, eds. Proc. 2002 Sympos. Eye Tracking Res. Appl. (ACM, New York), 103–110.

Duchowski AT, Cournia N, Cumming B, McCallum D, Gramopadhye A, Greenstein J, Sadasivan S, Tyrrell RA (2004) Visual deictic reference in a collaborative virtual environment. Duchowski A, Vertegaal R, eds. Proc. 2004 Sympos. Eye Tracking Res. Appl. (ACM, New York), 35–40.

Duchowski AT, Medlin E, Cournia N, Murphy H, Gramopadhye A, Nair S, Vorah J, Melloy B (2002b) 3-D eye movement analysis. Behav. Res. Methods Instruments Comput. 34(4):573–591.

Ehrenberg AS, Bound JA (1993) Predictability and prediction. J. Roy Statist. Soc. Ser. A 156(2):167–206.

Foulsham T, Walker E, Kingstone A (2011) The where, what and when of gaze allocation in the laboratory and the natural en vironment. Vision Res. 51(17):1920–1931.

Glockner A, Herbold AK (2011) An eye-tracking study on in-¨ formation processing in risky decisions: Evidence for compen satory strategies based on automatic processes. J. Behav. Decision Making 24(1):71–98.

Godin G, Massicotte P, Borgeat L (2004) Foveated stereoscopic display for the visualization of detailed virtual environments. Coquillart S, Gobel M, eds.¨ Proc. 10th Eurographics Conf. Virtual Environment (Eurographics Association, Aire-la-Ville, Switzerland), 7–16.

Guenter B, Finch M, Drucker S, Tan D, Snyder J (2012) Foveated 3D graphics. ACM Trans. Graphics 31(6):164:1–164:10.

Gutiérrez Alonso MA, Vexo F, Thalmann D (2008) Stepping into Virtual Reality (Springer, London).

Guyon I, Elisseeff A (2003) An introduction to variable and feature selection. J. Machine Learn. Res. 3(March):1157–1182

Hastie TJ, Tibshirani RJ, Friedman JH (2013) The Elements of Statistical Learning: Data Mining, Inference, and Prediction, 2nd ed., corr. 7th printing (Springer, New York).

Hevner AR, March ST, Park J, Ram S (2004) Design science in in formation systems research. MIS Quart. 28(1):75–105.

Hirschman EC, Holbrook MB (1982) Hedonic consumption: Emerg ing concepts, methods and propositions. J. Marketing 46(3):92–101.

Hoffman DL, Novak TP (1996) Marketing in hypermedia computermediated environments: Conceptual foundations. J. Marketing 60(3):50–68.

Holmqvist K, Nystrom M, Andersson R, Dewhurst R, Jarodzka H,¨ Van de Weijer J (2011) Eye Tracking: A Comprehensive Guide to Methods and Measures (Oxford University Press, Oxford).

Hui SK, Fader PS, Bradlow ET (2009) Path data in marketing: An integrative framework and prospectus for model building. Marketing Sci. 28(2):320–335.

Hyon¨ a J, Radach R, Deubel H (2003)¨ The Mind’s Eye: Cognitive and Applied Aspects of Eye Movement Research (North-Holland, Amsterdam).

Iacovou CL, Benbasat I, Dexter AS (1995) Electronic data interchange and small organizations: Adoption and impact of technology. MIS Quart. 19(4):465–485.

Inman JJ, Nikolova H (2017) Shopper-facing retail technology: A retailer adoption decision framework incorporating shoppe attitudes and privacy concerns. J. Retailing 93(1):7–28.

James G, Witten D, Hastie TJ, Tibshirani RJ (2013) An Introduction to Statistical Learning: With Applications in R (Springer, New York).

Janiszewski C (1998) The influence of display characteristics on visual exploratory search behavior. J. Consumer Res. 25(3):290–301.

Kahn BE (2017) Using visual design to improve customer perceptions of online assortments. J. Retailing 93(1):29–42

Kaltcheva VD, Weitz BA (2006) When should a retailer create an exciting store environment? J. Marketing 70(1):107–118.

Kramida G (2016) Resolving the vergence-accommodation conflict in head-mounted displays. IEEE Trans. Visualization Comput. Graphics 22(7):1912–1931.

Krol M, Krol M (2017) A novel approach to studying strategic decisions with eye-tracking and machine learning. Judgment Decision Making 12(6):596–609.

Kuhn M, Wing J, Weston S, Williams A, Keefer C, Engelhardt A, Cooper T, Mayer Z, Kenkel B, Benesty M, et al. (2018) Caret: Classification and regression training. R package version 6.0-80. Accessed October 12, 2018, https://rdrr.io/cran/caret/.

Kuncheva LI (2004) Combining Pattern Classifiers: Methods and Algo rithms (John Wiley & Sons, Hoboken, NJ).

Lai M-L, Tsai M-J, Yang F-Y, Hsu C-Y, Liu T-C, Lee SW-Y, Lee M-H, Chiou G-L, Liang J-C, Tsai C-C (2013) A review of using eyetracking technology in exploring learning from 2000 to 2012. Educational Res. Rev. 10(December):90–115.

Lau KW, Lee PY (2019) Shopping in virtual reality: A study on consumers’ shopping experience in a stereoscopic virtual reality. Virtual Reality 23(3):255–268.

Lee L, Inman JJ, Argo JJ, Bottger T, Dholakia U, Gilbride T, van ¨ Ittersum K, et al (2018) From browsing to buying and beyond: The needs-adaptive shopper journey model. J. Assoc. Consumer Res. 3(3):277–293.

Léger PM, Sénecal S, Courtemanche F, de Guinea AO, Titah R, Fredette M, Labonte-LeMoyne E (2014) Precision is in the eye of the be<sup>´</sup> holder: Application of eye fixation-related potentials to information systems research. J. Assoc. Inform. Systems 15(10):651–678.

Loomis JM, Blascovich JJ, Beall AC (1999) Immersive virtual environment technology as a basic research tool in psychology. Behav. Res. Methods Instruments Comput. 31(4):557–564.

MacLean KE (2008) Haptic interaction design for everyday interfaces. Rev. Human Factors Ergonomics 4(1):149–194.

Mariscal G, Marban O, Fernandez C (2010) A survey of data mining and knowledge discovery process models and methodologies. Knowledge Engrg. Rev. 25(2):137–166.

Meißner M, Musalem A, Huber J (2016) Eye tracking reveals processes that enable conjoint choices to become increasingly efficient with practice. J. Marketing Res. 53(1):1–17.

Meißner M, Pfeiffer J, Pfeiffer T (2017) Combining virtual reality and mobile eye tracking to provide a naturalistic experimental environment for shopper research. J. Bus. Res. 100(July):445–458.

Meyer D, Dimitriadou E, Hornik K, Weingessel A, Leisch F (2017) e1071: Misc functions of the Department of Statistics, Probability Theory Group (formerly: E1071), TU Wien. R package version 1.6-8. Accessed October 12, 2018, https://CRAN.R-project.org/ package=e1071.

Moe WW (2003) Buying, searching, or browsing: Differentiating between online shoppers using in-store navigational clickstream. J. Consumer Psych. 13(1–2):29–39.

Moeslund TB, Granum E (2001) A survey of computer vision-based human motion capture. Comput. Vision Image Understanding 81(3): 231–268.

Opitz DW, Maclin R (1999) Popular ensemble methods: An empirical study. J. Artificial Intelligence Res. 11:169–198.

Orquin JL, Mueller Loose S (2013) Attention and choice: A review on eye movements in decision making. Acta Psych. 144(1):190–206.

Peffers K, Tuunanen T, Rothenberger MA, Chatterjee S (2007) A design science research methodology for information systems research. J. Management Inform. Systems 24(3):45–77.

Peukert C, Pfeiffer J, Meißner M, Pfeiffer T, Weinhardt C (2019) Shopping in virtual reality stores: The influence of immersion on system adoption. J. Management Inform. Systems 36(3):755–788.

Pfeiffer T, Feiner SK, Mayol-Cuevas WW (2016) Eyewear computing for skill augmentation and task guidance. Bulling A, Cakmakci O, Kunze K, Regh JM, eds. Eyewear Computing—Augmenting the Human with Head-Mounted Wearable Assistants, vol. 23 (Dagstuh Publishing, Wadern, Germany), 199–203.

Pieters R, Warlop L (1999) Visual attention during brand choice: The impact of time pressure and task motivation. Internat. J. Res. Marketing 16(1):1-16

Rayner K (1998) Eye movements in reading and information processing: 20 years of research. Psych. Bull. 124(3):372–422.

Russo EJ, Leclerc F (1994) An eye-fixation analysis of choice processes for consumer nondurables. J. Consumer Res. 21(2):274–290.

Scholz M, Pfeiffer J, Rothlauf F (2017) Using PageRank for non personalized default rankings in dynamic markets. Eur. J. Oper. Res. 260(1):388–401.

Shi SW, Wedel M, Pieters FGM (2013) Information acquisition during online decision making: A model-based exploration using eyetracking data. Management Sci. 59(5):1009–1026.

Shimojo S, Simion C, Shimojo E, Scheier C (2003) Gaze bias both reflects and influences preference. Nature Neurosci. 6(12):1317–1322.

Shmueli G (2010) To explain or to predict? Statist. Sci. 25(3):289–310.

Shmueli G, Koppius OR (2011) Predictive analytics in information systems research. MIS Quart. 35(3):553–572.

Slater M (2003) A note on presence terminology. Presence Connec 3(3):1–5.

Slater M, Usoh M, Steed A (1995) Taking steps: The influence of a walking technique on presence in virtual reality. ACM Trans. Comput.-Human Interaction 2(3):201–219.

Speier C, Valacich JS, Vessey I (1999) The influence of task interruption on individual decision making: An information overload perspective. Decision Sci. 30(2):337–360.

Steuer J (1992) Defining virtual reality: Dimensions determining telepresence. J. Comm. 42(4):73–93.

Sutherland IE (1968) A head-mounted three dimensional display. Proc. Fall Joint Comput. Conf., Part I (ACM, New York), 757–764.

Tanriverdi V, Jacob RJK (2000) Interacting with eye movements in virtual environments. Turner T, Szwillus G, eds. Proc. CHI 2000 (ACM Press, New York), 265–272.

Tien T, Pucher PH, Sodergren MH, Sriskandarajah K, Yang GZ, Darzi A (2014) Eye tracking for skills assessment and training: A systematic review. J. Surgical Res. 191(1):169–178.

van der Lans R, Pieters R, Wedel M (2008) Competitive brand salience. Marketing Sci. 27(5):922–931.

van der Lans R, Wedel M, Pieters R (2011) Defining eye-fixation sequences across individuals and tasks: The binocularindividual threshold (bit) algorithm. Behav. Res. Method 43(1):239–257.

Van Nierop E, Bronnenberg B, Paap R, Wedel M, Franses PH (2010) Retrieving unobserved consideration sets from household panel data. J. Marketing Res. 47(1):63–74.

Vidal M, Bulling A, Gellersen H (2013) Pursuits: Spontaneous interaction with displays based on smooth pursuit eye movement and moving targets. Canny JF, Langheinrich M, Rekimoto J, eds. Proc. 2013 ACM Internat. Joint Conf. Pervasive Ubiquitous Comput. (ACM Press, New York), 439–448

Webster DM, Kruglanski AW (1994) Individual differences in need for cognitive closure. J. Personality Soc. Psych. 67(6):1049–1062.

Wirth R, Hipp J (2000) CRISP-DM: Towards a standard process model for data mining. Proc. 4th Internat. Conf. Practical Appl. Knowledge Discovery Data Mining, Manchester, UK, (Practical Application Company, Blackpool, UK) 29–39.

Witten IH, Frank E, Hall MA, Pal CJ (2016) Data Mining: Practical Machine Learning Tools and Techniques (Morgan Kaufmann, Burlington, MA).

Wolfinbarger M, Gilly MC (2001) Shopping online for freedom, control, and fun. Calif. Management Rev. 43(2):34–55.

Xiao B, Benbasat I (2007) E-commerce product recommendation agents: Use, characteristics, and impact. MIS Quart. 31(1): 137–209.

Xu S, Jiang H, Lau F (2008) Personalized online document, image and video recommendation via commodity eye-tracking. Proc. 2008 ACM Conf. Recommender Systems (ACM, New York), 83–90.

Zhu R, Zhou Z (2004) A real-time articulated human motion tracking using tri-axis inertial/magnetic sensors package. IEEE Trans. Neural Systems Rehabilitation Engrg. 12(2):295–302.
