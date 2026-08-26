---
otero_id: 21005
otero_key: "R67M7Y2S"
title: "Dynamic profiling of consumers for customized offerings over the Internet: a model and analysis"
authors: "T.S. Raghu; P.K. Kannan; H.R. Rao; A.B. Whinston"
year: "2001"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(01)00106-3"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Dynamic profiling of consumers for customized offerings over the Internet: a model and analysis

T.S. Raghu <sup>a,)</sup>, P.K. Kannan <sup>b</sup>, H.R. Rao <sup>c</sup>, A.B. Whinston <sup>d</sup>

<sup>a</sup> School of Accountancy and Information Management, Arizona State UniÕersity, P.O. Box 873606, Tempe, AZ, 85287 USA UniÕersity of Maryland, College Park, College Park, MD, USA <sup>c</sup> State UniÕersity of New York at Buffalo, Buffalo, NY, USA <sup>d</sup> UniÕersity of Texas at Austin, Austin, TX, USA

## Abstract

Delivery of customized, targeted advertisement messages, and delivery of customized information products and software products to consumers requires effective gathering and analysis of preference information. In this paper, we propose a model for dynamically profiling consumers’ preferences that is based on the theory of questionnaires. The customization procedure is demonstrated for an example scenario of an informational brokerage where real-time financial, marketing, and company information products are offered to consumers. Simulation results show that the information acquisition and search process exhibits a nonlinear behavior in the information gained and the pattern of information gain is similar irrespective of the number of consumers polled. q 2001 Elsevier Science B.V. All rights reserved.

Keywords: Information search; Dynamic profiling; Customized advertisements; Customized product offerings; Modeling

## 1. Introduction

The development of Internet as a communication and transaction channel to reach consumers provides a means to transform many business concepts such as one-on-one marketing and relationship marketing into reality. By using the Internet, it is now possible to acquire immediate information about consumers needs and meet those needs by delivering products and product-related information, including advertisements, in real-time. The impact of the Internet has been strongly felt in application areas such as advertisements targeting and marketing of information products such as financial markets information, customized news, software, etc. In the case of advertisements, selection and bundling of specific advertisements to be targeted is done in real time as customers enter websites, while information products such as news are being generated in real-time even as significant events transcribe with ever-changing content and format. Development of multi-casting techniques such as Marimba’s Castanet www.´ Ž marimba.com are enabling businesses to deliver dig-. ital products or collections of digital products to multiple customer sites, install them, and update them on an ongoing basis.

While the Internet has created significant opportunities for customization, one-on-one marketing and targeted advertisement, it has also put an immense pressure for obtaining customer information needed for such customization. While technology exists to serve different and customized bundles of advertise ment messages to customers as they enter websites, profiling the entering customers in real-time and selecting the customized mix of offerings is a chal lenge. The customer base for such advertisements is dynamic as customers surf in and out of websites ,Ž . making it difficult to profile them on a continuing basis. Similarly, when information products can be produced almost instantaneously, such rapidly evolv ing content also compresses the time available for their design. This makes it difficult to implement traditional market research techniques to understand consumer preferences for the various features of the information product. Would consumers prefer more textual depth to less multimedia features on a piece of information? What features will they like best? These are some of the many questions information product designers have to cope with in an extremely shortened design cycle. Also, while traditionally such information products have been sold through sub scription plans, it is now possible to obtain pieces of information products say, a news column or anŽ article using micro-payments. Such advances also. render the customer base for such products dynamic, as customers enter and leave the market or switch toŽ competing services more easily making it more. difficult to measure their preferences. This further complicates the issue of product design and mass customization. The Internet provides the capability to collect preference-related information through ac tions and choices made by customers in viewing or subscribing to products<sup>r</sup>services. However, there is a critical need for methodologies that can collect the information most efficiently in the short time-frame, dynamically update consumer preferences as more information becomes available and provide implica tions for product customization and advertisement targeting in real-time. It is this need that our paper seeks to fulfill.

The primary objective of our paper, therefore, is to develop a model for dynamically profiling customer preferences to aid customized offerings— products or services or interactive advertisements. The model assumes that such customization is performed under resource constraints—that is, the extent of customization depends on resources available to provide individualized offerings in short cycle time applications. Since resource constraints permit customization only at a segment level generally, the model performs a dynamic segmentation of the customer population based on the profiles developed. The second objective of the paper is to examine the informational characteristics of the profiling technique for different sizes of the product attribute space and number of consumer segments. Simulations show an interesting phenomenon that acquisition of profile information from multiple consumers results in a nonlinear information gain behavior and also that the pattern of information gain from multiple consumers is independent of the number of consumers. These results provide insights into the information acquisition strategies that Internet based organizations have to adopt for efficient and effective customization. We start our exposition of the model with a discussion of the background of the problem and our motivation for the research.

## 2. Background and motivation

## 2.1. Customer profiling and customization

Today, the basis of most personalization on the web, whether for customized product offerings or targeting of advertisements, is the customer profile. An application such as an e-commerce server profiles each user and then, when a particular user logs in or attempts to perform some actions, reacts differently based on the profile. Current technology available on the web such as dynamic HTML, applets, and cookies provide the means to acquire individual customer profiles. Such information can be tracked to a high level of granularity, right down to the individual customer’s nature of interaction for ex-Ž ample, which pages were visited at what time and on which days with the vendor’s websites 28 . Such. <sup>w</sup> <sup>x</sup> information can be stored in repositories such as database of customer profiles. The information acquisition process itself is often sequential. This necessitates the utilization of partial information about customers to make customization decisions.

Applications can profile users in a number of ways. Some of the most common ones are 16 as<sup>w</sup> <sup>x</sup> follows.

vThe user explicitly provides information by filling out a registration form or survey by making a menu choice,

vThe application records the user’s actions and builds a profile based on this history. At the simplest level, a site that sells both CDs and books may note that a particular user never goes into the book section, only the CD section. That person gets profiled as a music lover, as opposed to a book lover.

vThe application uses statistical means to draw inferences about the user. For example, an online bookstore knows from previous buying patterns that readers who buy author A will likely buy author B.

In addition the application may implement context-based personalization, based on the user’s current activity. For instance, it may treat a consumer differently if browsing a history of past customer support incidents than if registering a new support incident.

Various types of personalization exist. Some of the most common are:

v Rules-based matching, based on user profiles or communities: For example, AIf the user is a Wall Street Journal reader, then display the Baron’s ad.B

v Context-based matching: AIf the user is on the sport’s page, display the sport’s equipment adB.

v Category-based matching: Content producers classify their content based on certain attributes, users rate their priorities in terms of the same attributes and an agent steers users to an appropriate content.

Many of the targeted and customized advertisement models that are operational on the web use some kind of matching techniques based on usage context. For example, Doubleclick’s targeting technique, called DART, works by reading 22 criteria such as domain type, time of day, etc., which is further refined by AcookiesB to enable the match.

Based on the customer profile so developed, Doubleclick’s server delves into its inventory of advertisements to select an ad mix in a sequential fashion to match marketers’ needs with the user profile. While the ad mix is designed in an ad hoc fashion in DART, the design of this mix is in real time. In order that the ad mix is AoptimalB in the sense of its overall effectiveness, it is necessary to acquire preference information from customers. For example, it is necessary to understand whether they are interested in sporting goods and sporting videos and sporting mementos, etc., so that a mix of such ads are designed specifically for each of them or for each segment of consumers, under constraints of time.

When the objective of the profiling exercise is to use the information in designing customized ad mix in real time or news products in real-time, the matching techniques may not be adequate. One has to use some type of feedback and learning technique for such requirements in which the application updates the user’s profile based on the user’s actions, either in real time or offline feedback. Currently, there are a limited number of methods that can use consumers’ choice and priority information in a useful manner to help vendors in making product offering or to group customers in a dynamic manner. One such method detailed in Ref. 9 provides targeting of<sup>w</sup> <sup>x</sup> appropriate audience based on psychographic or behavioral profiles of end users. Recording the computer activity and viewing habits of the end user forms the psychographic profile. Based on regression analysis of recorded responses of a first set of users viewing the advertisements, the target user profile is refined. Regression analysis of recorded responses of subsequent sets of users continually auto-targets and customizes ads for the optimal end-user audience. Another method developed in Ref. 10 focuses on<sup>w</sup> <sup>x</sup> developing stochastic methods based on the multiarmed bandit problem to optimally target banner ads at consumers who enter websites. Since bandit problems are very difficult to solve analytically, the authors use two highly stylized examples to illustrate their method.

In many instances where customized products are offered to customers over the web, customers prespecify what features they prefer and products are made to those specifications. Push technology, which allows servers to automatically broadcast updates to numerous desktops simultaneously, enables companies to automatically send data or information to a desktop web browser at scheduled times based on the priorities specified by the user 32 . However,<sup>w</sup> <sup>x</sup> user-specified criteria have to be small in number to effectively collect the data and also very general in terms of being useful for making information bundles. Multicasting of customized software is a similar concept. The application distributor helps distribute software application to user desktops directly thereby making the management of software distribution and upgrading more cost effective. In this scenario, the web browser functions as a distribution channel for software products 30,31 . Here, again, customization <sup>w</sup> <sup>x</sup> is possible on the basis of customer input. However, if the product is to be designed and bundled on the fly, there will not be enough time to get detailed information from customers and then react to it using conventional methods. This is where dynamic profiling methods will be very useful.

As new information becomes available about customer preferences in a sequential manner, the vendors should be able to use this information to adjust product offerings and ad mixes in accordance with the new information. Also, the vendor should be able to redesign or present customized information gathering experiments to the consumer whenever possible such that each such experiment yields most information about customer preferences. This is what our model proposes.

## 2.2. Model oÕerÕiew

Our model uses an adaptive nonmetric revealed preference approach to operationalize the process of preference information acquisition utilizing an information theory based approach 15,17,22,25 . Investi-<sup>w</sup> <sup>x</sup> gation of information gathering strategies as part of the decision-making system has been studied in Refs. <sup>w</sup> <sup>x</sup> 7,23,24,26 . The vendor AlearnsB about the consumer’s preference orderings and consequently about the utility associated with the product or advertisement attribute space. This learning is conducted adaptively through a succession of experiments. An Ž optimal process must, however, balance the expected gain from such information against the cost of obtaining it. In addition, we examine the vendor’s. problem of dynamically updating consumer preference profiles, based on consumers’ choices and priorities<sup>r</sup>preferences, with a view to making product mix and ad mix decisions. In the presence of resource constraints, constraints on the number of product<sup>r</sup>ad bundle mixes, we visualize the vendor’s problem as one of understanding consumers’ preferences and offering them a bundle of customized offerings. This is accomplished by allocating scarce resources to clusters of consumers with similar tastes. ŽWhile our model resembles an adaptive conjoint study 1 in terms of its interactive nature and com-<sup>w</sup> <sup>x</sup> parison of partial profiles, the amount of information acquisition is significantly lower and more efficient, as in conjoint studies one generally collects more data than needed 12 . Moreover, the focus of our<sup>w</sup> <sup>x</sup> model is dynamic profiling, whereas conjoint analysis is basically a static approach..

The following aspects characterize the scenario analyzed in this paper.

vThe vendor is faced with the problem of customizing product<sup>r</sup>ad offerings for a customer in real-time with whatever information he<sup>r</sup>she has of customer preferences. The vendor has to design a set of sequential priority<sup>r</sup>preference elicitation experiments to determine each customer’s preference for, or prioritization of, product<sup>r</sup>ad bundles. In developing the experimental design the vendor can make use of a priori information about customer priority rankings such that the information acquisition process can be made more efficient.

vIn an idealized situation, the vendor could meet the exact needs of each consumer by providing the customized offering that the customer wants. However, in practice this will not be possible due to a number of constraints and costs involved, particularly from the producer’s side. Exact matches may require infinite capacities. Hence, the vendor would need to categorize consumers into groups such that consumers belonging to a certain cluster have similar priority rankings or preferences for the product bundles. Given information about priorities, the vendor would then be able to customize product offerings for each consumer segment 8 . The number of seg-<sup>w</sup> <sup>x</sup> ments itself will be determined by the availability of resources.

This paper first presents a method to elicit consumer information in an efficient manner. Given the individual consumer preference, it then analyzes the problem of segmenting the consumers into groups or partitions with similar profiles using network structuring 5 . Using simulation and partition comparison<sup>w</sup> <sup>x</sup> techniques it explores the stability of the partitions as more information is obtained from consumers. The methods of segmentation discussed are applicable to scenarios where resource constraints exist, requiring that the same product bundle cannot be offered to multiple product segments, i.e., if a product bundle is offered to one customer segment, its complement may need to be offered to other consumer segments.

In the next subsection, we describe the problem scenario we consider. Section 3 focuses on the information acquisition process to elicit customer preference profiles. Section 4 discusses the customer categorization methodology that we use and the dynamic nature of the categorization process as information flows in. Section 5 provides the results of our simulation exercises. We conclude in Section 6 with the implications of results for dynamic profiling and customization.

## 2.3. An example scenario

In this section, we portray a scenario that illustrates the problem faced by an Internet information broker in customizing financial, marketing and company information products to a heterogeneous set of day traders and institutional traders mostly in realtime settings. This scenario is specific to an information product environment, however, similar scenarios are possible for other business environments such as the targeting of advertisement in real time.

Information brokerages can provide an effective meeting ground for potential customers and suppliers. Customers in the scenario include individual day traders and institutional traders looking for real-time informational products that can provide useful input for the trading decisions. Suppliers can be news services, corporations, financial brokerages, government, and consultants who may supply relevant information either free or for a price. The role of information brokerages would be to match customer needs with existing information bundles from suppliers, create new bundles of information that best match the needs of the market. Customizing the information bundles enhances the effectiveness of trading decisions of users.

Typically, an information broker would begin the customization process by collecting information on customer needs e.g., industries, companies, formatŽ of information , types of information and preferences. among types of information level of depth, featuresŽ of information, etc. . In order to customize effec-. tively, the brokerage should be able to collect, combine and process preference and priority information of its customers in an effective manner. While many preferences at the aggregate level can be obtained well in advance, there are still many features and customization options that will depend on the nature of the information evolving in real time. Currently, many such decisions of product design do not consider customization as there is not much time available for obtaining feedback from customers and then designing the information products. However, with the real-time nature of interactions on the Internet, it is possible to get instantaneous feedback either through interactive surveys or through observation of customer behavior at websites.

Assume that a number of traders and institutions have shown interest in specific industries. Information products will have to be developed tailored to these customers as and when information becomes available from different sources. The brokerage creates value by obtaining the information components from different sources, bundles and processes the information products according to customer’s tastes and distributes them. The brokerage’s resource constraint is processing time. It expends more time in collecting material from different sources broaderŽ coverage to increase reliability as compared to ma-. terial from a few sources narrow coverage . There-Ž . fore, the information products could be ordered in terms of increasing breadth of coverage and is quite specific to the information that is evolving. The brokerage can also add value by formatting the information product with many features which isŽ also situation specific depending on the information that is evolving —text vs. graph vs. multi-media,. etc. As the features in a product increase, the brokerage will have to allocate more time for processing and producing the product. Thus, for the purposes of this example, we divide the attribute space of an arbitrary information product over the Internet into two dimensions. One dimension reflects the breadth of coverage of sources. The other dimension is the number of features characterizing the product—it could be purely text-based one feature , or text-basedŽ . and sound clips two features or text plus all type ofŽ . multimedia three features , and so on. On the breadthŽ . dimension, ‘narrow’ indicates narrow coverage and ‘broad’ indicates broad coverage of sources. The product space shown in Fig. 1 is considered a preference or priority network, where each point in the product space is considered a vertex and the line joining two vertices is considered an edge of the priority network. The responses to the questionnaire lead to the introduction of edges between different vertices of this network. The priority profiles of the customers are directed networks.

For example, the vertex corresponding to one,Ž narrow indicates a narrow coverage of topics with. text-based features, whereas two, broad indicates aŽ . broad coverage of the material with two features. We assume that a consumer would want the maximum number of features for the product and a broad coverage. For the sake of exposition, we limit the maximum number of features in this example to three and thus the highest priority information bundle for a consumer here is three, broad . In the restŽ . of the paper, we use the term Aproduct bundleB for each vertex as shown in the figure below. By the same token, the vertex one, narrow will have theŽ . lowest priority. Obviously, if the brokerage can avoid it, it will try to provide a bundle better than one,Ž narrow . But to assure a three, broad could mean. Ž . expending a lot of effort in preparing and delivering the products. Given the resource constraint of time, the brokerage cannot deliver all the products requested by all consumers in the three, broad designŽ . format. In this case, the brokerage would like to know how the consumer evaluates the other bundles so that it can generate appropriate customized designs within the given resource constraints.

![](/api/attachments/R67M7Y2S/fulltext/images/dbdacfcee2604a47c40c12cd807b99ce4d080a25fef684b605eb35293863ee37.jpg)  
Fig. 1. Product space.

Although, for sake of exposition, we have assumed that the maximum number of features in this example is three, in a realistic scenario it could be a very large number depending on the application. This could lead to a large number of product bundles among which priority ordering for a consumer has to be determined. Also, when consumers dynamically enter and leave the market, when the level of demand is in real-time say, as in a financial applica-Ž tion , then products will have to be designed based. on the available information and offerings fine-tuned as more information comes in. The next section deals with information acquisition about the brokerage products.

## 3. The information acquisition and search process

The information acquisition process assumes that the vendor has fragmentary and incomplete prior information about the preferences or priorities of a consumer. For instance, based on the demographic characteristics of the consumer some assumptions about initial priority orderings can be made. Or, as in our example above, we could assume that three,Ž broad is the most preferred and one, narrow the. Ž . least preferred. Thus, a consumer could have any one of a large number of possible priority orderings over the discrete product bundles. The vendor uses a nonparametric revealed preference approach to operationalize the process of priority elicitation and to poll the consumer for information. In a cybermarketing scenario, for example, the vendor receives this information by analyzing the customer clicks and key strokes that are gathered when the customer interacts with the product catalogs<sup>r</sup>web pages of the vendor. Based on the customer clicks, the manager can tailor the polling process by adaptively changing the composition of the web pages<sup>r</sup>product bundles being shown to the consumer. By polling the consumer about priorities over discrete product bundles about which the vendor has no prior information, the vendor adaptively infers the consumers’ priority profile, through a succession of experiments. This eliminates the need to parameterize the individual’s utility function, and also the need for the vendor to make stronger assumptions about continuity and convexity <sup>w</sup> <sup>x</sup> <sub>6</sub> <sub>.</sub>

The experimental process utilized for eliciting information from the consumers is based on simple paired comparisons among the discrete product bundles. Such responses provide additional information about a consumer’s priority ranking. A succession of such responses allows the vendor to determine the priority rankings more and more accurately, till it is no longer necessary to pose new questions when the priority ranking is completely revealed. The complex experiment is then complete and the plan of experiments has formed a questionnaire <sup>w</sup> <sup>x</sup> 28 . The ultimate objective of accurately ranking priorities is to be able to allocate the product bundles to each consumer within a group in a manner that optimizes the total group welfare.

In the problem-solving process, the vendor makes the following assumptions about the product space and about consumers 26 . <sup>w</sup> <sup>x</sup>

vThe product space subsumes an a priori partial Ž . incomplete and fragmentary priority order 4 . Fun-<sup>w</sup> <sup>x</sup> damentally, the axiom of nonsatiety is followed 21<sup>w</sup> <sup>x</sup> implying that more units of a product are always preferred to less of the same 27 . Therefore, the <sup>w</sup> <sup>x</sup> vendor knows a priori the priority relationship between certain bundles but not between other bundles.

vAll consumers are rational; i.e., the axioms of reflexivity, transitivity and completeness are followed. However, our method would still work whenŽ this assumption is relaxed. Further, the hypothesis. of comparability is always satisfied, i.e., it is always possible for the consumer to say that a bundle has higher, lower or equal priority over another.

This kind of judgment is common in everyday life and consequently is intuitively appealing 18 . <sup>w</sup> <sup>x</sup>

## 3.1. Priority ranking elicitation

The discussion that follows details the experimental process of information gathering for a consumer. It is assumed, following 33 that individual con-<sup>w</sup> <sup>x</sup> sumer preferences do not change for the time frame of the experimental process. Further, it is also assumed that the product space considered is within the nonsatiated space of the consumer. The analysis that follows is entirely general, since efficient information acquisition strategies can be applied by the vendor to any or all consumers. Priorities across the consumers may of course be different.

Throughout this paper, it is assumed that the cost of each experiment is the same. Hence, minimizing the expected number of questions in a questionnaire that elicits information from consumers would also minimize the expected cost of the questionnaire. The experiment process directs the course of information elicitation from a consumer in such a way that the vendor will receive the maximum of information from the responses. The efficient identification of priorities is important, because it would have an impact on decreasing the cost of information gathering. We utilize the brokerage scenario described in the earlier section to illustrate the information acquisition process.

Let z denote any product bundle i.e., a vector of Ž the two features , and. $Z$ the space of all bundles under consideration. The partial order Ž . W is assumed to be a strictly increasing weak order on $Z ,$ Ž . as shown in Fig. 1 . Because of this structure of the product space, considerably fewer experiments are needed to determine the unique priority ordering for each consumer.

In the forthcoming discussion, we shall follow Ref. 26 in defining an ordinal function to be used <sup>w</sup> <sup>x</sup> for ranking of the set of bundles in the product space. In doing so, we follow the trend that only rank order data are supplied to most marketing computer algorithms that compute utility scales to determine consumer evaluations 13 . The fact that the<sup>w</sup> <sup>x</sup> determination of consumer evaluations involves ordinal priorities rather than intensity of priorities is often a criticism of the algorithms. However, a theŽ . algorithms do provide an indication of the relative importance and b when the utilities serve only as aŽ . means of choosing from among the best items from those offered, the utilities need only be ordinally scaled 11 . Ordinal relations are invariant under<sup>w</sup> <sup>x</sup> arbitrary strictly positive monotonic transformations of the scale of measurement. Ordinal functions are weaker than cardinal relations, and they have the advantage that they can be established empirically, even if there is not enough information to establish values on a cardinal scale 19 .<sup>w</sup> <sup>x</sup>

Definition 1. We define a function $f ( z )$ as follows: $f ( z ) = | \{ z ^ { \prime } \varepsilon Z | z \gtrsim z ^ { \prime } \} |$ <sup><</sup> Ž . The number of bundles, $z ^ { \prime } ,$ that are no better than the bundle z. <sup>w</sup> <sup>x</sup> 26 .

Such a function is a strictly increasing weak order on Z and satisfies the following equation:

$$
(\forall z \varepsilon Z): f (z) = | \left\{z ^ {\prime} \varepsilon Z | f (z) \geq f \left(z ^ {\prime}\right) \right\} |\tag{1}
$$

Conversely, any function $f \colon z \varepsilon N$ Žthe set of nonnegative integers satisfying the above properties, induces . a unique weak order <sup>G</sup>on Z defined by:

$$
\big (z \geq z ^ {\prime} \Leftrightarrow f (z) \geq f (z ^ {\prime}) \big)\tag{2}
$$

Consequently, we can define the set of priority orders also the set of linear extensions of the given Ž partial order , or the state space . F as follows:

$$
\text { Let   } F = \{f: z \varepsilon N | f \text {   satisfies   Eqs.   (1)   and   (2) } \}\tag{3}
$$

Applying the definitions to the brokerage products example above Fig. 1 , we have the following re- Ž . sults: f Ž . Ž . one, narrow <sup>s</sup> 1 since one, narrow is the only bundle no better than itself. Similarly fŽthree, board.<sup>s</sup>6 since none of the six bundles in the product space have higher priority than the bundle itself. The state space the set of priority orders isŽ . given by the set of $f ^ { \mathrm { h } } s ( h \varepsilon \{ 1 , \dots , | F | = 1 1 \} )$ in Table 1. Each column corresponds to a unique possible ranking of all the bundles in product space. Each column represented by $f ^ { i }$ is the finest partition of the state space. When the vendor identifies the finest partition, it is only then that complete information about a consumer’s priorities is available. Then the vendor can take the optimal product allocation decision.

ŽNote: In order to carry out the simulations detailed in later sections, and to test the questionnaire design below, a key assumption made is that all priority rankings states in state space areŽ . equally probable. An individual is as likely to have a particular priority order as any other. This is a reasonable assumption in terms of Hartley’s information theory <sup>w x</sup> <sup>w x</sup> 20 . In prior research 26 , other probability distributions have been simulated and the questionnaire design developed below has been found to be highly robust..

Table 1 The state space

<table><tr><td>z/f</td><td> $f^{1}$ </td><td> $f^{2}$ </td><td> $f^{3}$ </td><td> $f^{4}$ </td><td> $f^{5}$ </td><td> $f^{6}$ </td><td> $f^{7}$ </td><td> $f^{8}$ </td><td> $f^{9}$ </td><td> $f^{10}$ </td><td> $f^{11}$ </td></tr><tr><td>(one, narrow)</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>(one, broad)</td><td>2</td><td>3</td><td>3</td><td>4</td><td>4</td><td>2</td><td>3</td><td>3</td><td>2</td><td>3</td><td>3</td></tr><tr><td>(two, narrow)</td><td>3</td><td>2</td><td>3</td><td>2</td><td>2</td><td>3</td><td>2</td><td>3</td><td>3</td><td>2</td><td>3</td></tr><tr><td>(two, broad)</td><td>4</td><td>4</td><td>4</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td></tr><tr><td>(three, narrow)</td><td>5</td><td>5</td><td>5</td><td>3</td><td>4</td><td>4</td><td>4</td><td>4</td><td>5</td><td>5</td><td>5</td></tr><tr><td>(three, broad)</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td><td>6</td></tr></table>

## 3.1.1. Questionnaire design

The goal of the interrogation is to be able to label each product bundle z with a rank. The vendor starts labeling the product bundles with the minimal element of the product set corresponding to the coordinate one, narrow . This element is labeled with aŽ . rank<sup>s</sup>1 and is discarded from the set that has to be labeled. Z is then updated. Since it is a priori known that one, narrowŽ . Ž . <sup>-</sup> one, broad , the next experiment consists of a comparison of the two product bundles that correspond to the one, broad and two,Ž . Ž narrow . Based on the signal received, the next. coordinate is labeled. The vendor proceeds to delineate an ordering; labeling one coordinate with each experiment. After each labeling, the minimal element in the updated set of bundles coordinates is dis-Ž . carded. The process continues till the minimal element of the updated set coincides with the maximal element of $Z \ ( { \mathrm { r a n k } } = | Z | )$ Ž corresponding to three, broad . Using this questionnaire design, we get the. most efficient of possible strategies 26 .<sup>w</sup> <sup>x</sup>

The above questionnaire design guarantees the most efficient preference elicitation process for two dimensional product spaces, with one dimension restricted to two levels and the other dimension unrestricted in levels. For higher dimensional product spaces we do not have a proof for optimality, however, simulations indicate that the questionnaire design could still be used as a AgoodB heuristic.

## 4. Customer categorization

A critical question at this juncture deals with the extension to multiple consumers. Since the vendor is AbroadcastingB the questions to each consumer, each consumer will have individual and perhaps different answers to the questions. Ultimately of course, each consumer’s priority profile will coincide with one of the final partitions in the state space, i.e., each column in Table 1 represented by $f ^ { i }$ is the finest partition of the state space. When there are multiple consumers, customers with similar profiles can be clustered into sets and assigned customized products. This process has to be performed in a dynamic fashion.

## 4.1. Forming clusters for product offerings

Given individual customer preferences<sup>r</sup>priorities, it may still not be possible to perform individualized customization due to problems of resource constraints. The categorization of the customers into various clusters based on their profiles allows customized product bundles to be offered to each cluster. The vendor could assign to each cluster a tailored product offering based on a statistic that best represents the cluster. In this paper, we utilize a summary statistic similar to the median as the representative preference<sup>r</sup>priority profile of a cluster 3 . <sup>w</sup> <sup>x</sup> The median of a cluster represents the central location of the cluster. It is also important to find the extent of similarities<sup>r</sup>dissimilarities between the different consumer priority profiles in order to categorize the customers. Here, we use a distance metric similar to the Hamming distance metric used in information theory. The statistical model is briefly described below.

Preference networks of the kind shown in Fig. 1 can be represented as adjacency matrices with each cell having a value <sup>q</sup>1, <sup>y</sup>1, or 0. A value of<sup>q</sup>1 or <sup>y</sup>1 in the cell Ž . m, n indicates the presence of an edge between the vertices m and $n ,$ and its direction. A value of 0 indicates the absence of an edge between the vertices. Given two matrices $C _ { i }$ and $C _ { j }$ belonging to two customers, i and $j ,$ the distance, $\dot { d , }$ between the two customers is given by the following equation 5 .<sup>w</sup> <sup>x</sup>

$$
D \left(C _ {i}, C _ {j}\right) = \operatorname{tr} \left[ \left(C _ {i} - C _ {j}\right) ^ {\mathrm{T}} \left(C _ {i} - C _ {j}\right) \right]\tag{4}
$$

We now build a distance matrix that consists of all the customers being considered. If we have N customers, then the distance matrix will be of size $( N \times N )$ . This distance matrix is then used to categorize the customers into clusters. We use Ward’s method for clustering the data. It should be noted that alternate clustering procedures are available 2 ,<sup>w</sup> <sup>x</sup> however, evaluation of different clustering procedures for this problem is beyond the scope of this paper. Ward’s algorithm gives us the categorization of customers based on the distance between the priority networks of customers. It is possible to estimate the optimal number of clusters from cluster statistics such as, the cubic clustering criterionŽ Ž . . CCC or the F-statistic . However, the number of clusters will also depend on the resource constraint and how many product variations the resource constraint will allow. We assume that this information is exogenous to our problem and simulate for 4, 5 or 6 product lines or service lines. While some organizations may be forced to have only four lines because of resource constraints other richer organizations may afford larger number of service or product lines.

Our method does not call for a clustering algorithm to be run whenever a new piece of information comes in. Rather, we can use the confidence intervals derived for each cluster to classify the new priority ordering. As new information is obtained from consumer, the priority ordering is evaluated against each cluster’s median and checked whether it falls within the median’s confidence interval. If it falls within the interval, the consumer is placed in that cluster. It is, of course, possible that a consumer may belong to more than one cluster.

## 4.1.1. Determining product allocation

The next step in the customization process is to tailor the product makeup for the individual clusters. For this purpose, we have to determine the central priority network in each cluster. The median priority network $( C ^ { * } )$ for a cluster is a network $\mathbf { \dot { \rho } } _ { i } , \mathbf { \dot { \rho } } _ { i } ,$ whose sum of distances $\cdot _ { d } ,$ from other customer networks within the cluster is the minimum. For the distance metric considered in this paper, the median network in some cluster, $\Omega _ { \mathrm { c } }$ , is given by the following equation.

$$
C ^ {*} = \operatorname{argmin} _ {c ^ {*} \in \Omega_ {\mathrm{c}}} \sum_ {i = 1} ^ {r} d \left(c _ {i}, c ^ {*}\right)\tag{5}
$$

Here, r is the number of customers in the cluster $\Omega _ { \mathrm { c } } ,$ , such that, $c _ { i } \in \varOmega _ { \mathrm { c } } , \forall r \leq i \leq 1$

It is also possible to construct confidence intervals around the median using a bootstrap procedure. This will allow a new observation or a network corre- Ž sponding to a new customer to be classified as. belonging or not belonging to that cluster.

## 4.2. Dynamics of information acquisition

Since priority information is acquired sequentially from the customers, at any time the information acquired may be incomplete. Given the dynamics, the vendor may still have to form clusters with the existing information and then target the customers within each cluster with tailored product offerings. Ideally one would like to test the stability of the clusters whenever new information about customer priorities is available and determine if there are changes in cluster memberships. Changes in cluster membership may necessitate changes in product offerings. Thus, it is useful to examine the similarities<sup>r</sup>dissimilarities between clusters formed in each stage of information acquisition. The following discussion proposes the use of the Rand Index method <sup>w</sup> <sup>x</sup> 14 for such an examination.

## 4.2.1. Rand Index and cluster similarity

Rand Index is one of the most popular alternatives for comparing partitions 14 . Given a set of<sup>w</sup> <sup>x</sup> N customers, let $\varOmega ^ { m }$ be the set of clusters formed in information acquisition stage $m ,$ and let $\varOmega ^ { m + 1 }$ be the set of clusters formed in information acquisition stage $m + 1$ as follows.

$$
\begin{array}{l} \Omega^ {m} = \left\{\Omega_ {1} ^ {m}, \Omega_ {2} ^ {m}, \ldots \Omega_ {q} ^ {m} \right\} \\ \Omega^ {m + 1} = \left\{\Omega_ {1} ^ {m + 1}, \Omega_ {2} ^ {m + 1}, \ldots \Omega_ {q} ^ {m + 1} \right\}, \end{array}
$$

where $q$ is the total number of clusters formed. Let $C ^ { i j }$ denote the number of customers that are common to clusters $\varOmega _ { i } ^ { m } , \varOmega _ { i } ^ { m + 1 }$

A contingency table Table 2 for comparing the Ž . two sets of clusters can be built as follows 14 .<sup>w</sup> <sup>x</sup>

Table 2  
Contingency table for computing Rand index

<table><tr><td>Cluster</td><td> $\Omega_{1}^{m+1}$ </td><td> $\Omega_{2}^{m+1}$ </td><td>...</td><td> $\Omega_{q}^{m+1}$ </td><td>Sums</td></tr><tr><td> $\Omega_{1}^{m}$ </td><td> $C^{11}$ </td><td> $C^{12}$ </td><td></td><td> $C^{1q}$ </td><td> $C^{1.}$ </td></tr><tr><td> $\Omega_{2}^{m}$ </td><td> $C^{21}$ </td><td> $C^{22}$ </td><td></td><td> $C^{2q}$ </td><td> $C^{2.}$ </td></tr><tr><td>.</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $\Omega_{q}^{m}$ </td><td> $C^{q1}$ </td><td> $C^{q2}$ </td><td></td><td> $C^{qq}$ </td><td> $C^{q.}$ </td></tr><tr><td>Sums</td><td> $C^{.1}$ </td><td> $C^{.2}$ </td><td></td><td> $C^{.q}$ </td><td> $C^{.}=N$ </td></tr></table>

We have four different possibilities for any arbitrary pair of customers.

1. Customers in the pair are placed inside the same cluster in $\varOmega ^ { m } , \varOmega ^ { m + 1 }$

2. Customers in the pair are placed inside different clusters in $\varOmega ^ { \bar { m } } , \varOmega ^ { m + 1 }$

3. Customers in the pair are placed inside different clusters in $\varOmega ^ { m }$ , and the same cluster in $\varOmega ^ { m + 1 }$

4. Customers in the pair are placed inside the same cluster in $\Omega ^ { m }$ , and different clusters in $\varOmega ^ { m + 1 }$

Possibilities 1 and 2 imply agreement in clustering across the two stages of information acquisition. Possibilities 3 and 4 imply disagreement in clustering across the two stages of information acquisition. Let A represent the total number of agreements and D represent the total number of disagreements. Then,

$$
A + D = \binom{N}{2}\tag{6}
$$

It can be shown that

$$
\begin{array}{l} A = \binom {N} {2} + \sum_ {i = 1} ^ {q} \sum_ {j = 1} ^ {q} \left(C ^ {i j}\right) ^ {2} \\ - \frac {1}{2} \left(\sum_ {i = 1} ^ {q} \left(C ^ {i \cdot}\right) ^ {2} + \sum_ {i = 1} ^ {q} \left(C ^ {\cdot i}\right) ^ {2}\right) \\ D = \frac {1}{2} \left(\sum_ {i = 1} ^ {q} \left(C ^ {i \cdot}\right) ^ {2} + \sum_ {i = 1} ^ {q} \left(C ^ {\cdot i}\right) ^ {2}\right) - \sum_ {i = 1} ^ {q} \sum_ {j = 1} ^ {q} \left(C ^ {i j}\right) ^ {2} \end{array} \tag {7}
$$

Also, The probability of ${ \mathrm { a g r e e m e n t } } = { \frac { A } { \left( { \begin{array} { l } { N } \\ { 2 } \end{array} } \right) } }$

The probability of ${ \mathrm { l i s a g r e e m e n t } } = { \frac { D } { \left( { \begin{array} { l } { N } \\ { 2 } \end{array} } \right) } }$ . The difference between the probability of an agreement and disagreement $= { \frac { A \ { \stackrel { . } { - } } \ D } { \left( { \begin{array} { l } { N } \\ { 2 } \end{array} } \right) } }$ , we use this equation to the Rand Index value

compute the Rand Index value.

Using the above discussion, we can now present the algorithm for computing the Rand Index values to measure similarities in clusters across information acquisition stages.

4.2.1.1. Algorithm for Rand Index. 1. For any questioning stage m and $m + 1$ , find the clusters in m and $m + 1$ . Build a matrix with the rows representing the clusters in stage m and the columns representing the clusters in stage $m + 1$

2. For each cluster $\varOmega _ { i } ^ { m }$ and each cluster $\varOmega _ { j } ^ { m + 1 }$ increment the entry in that cell in the matrix by one for each common customer, e.g., if cluster $\varOmega _ { 1 } ^ { m }$ has customers 2, 4, 5, and 10, and cluster $\Omega _ { 2 } ^ { m + \mathbf { \bar { 1 } } }$ has customers 4, 6, 10, 11 cell 1, 2 will have the valueŽ . 2 stored in it.

3. Once the matrix is completely updated, the probability values of agreement, disagreement, and the difference between agreement and disagreement are computed as given by the above formulas.

## 5. A simulated example

In this section, we show computational results from a simulated customer categorization problem to demonstrate the dynamic information acquisition and customization procedure. We extend the brokerage example discussed earlier see Fig. 1 such that moreŽ . numbers of bundles are possible. We systematically vary the number of levels of features from 6 to 10 for conducting this simulation exercise.

For each level of feature dimension 6 throughŽ 10 we consider a hypothetical scenario wherein 40. customers are polled for priority information. Priority information was elicited by simulating the response of the customers from a uniform distribution. Customer response for a pair-wise ordering question can be one of higher priority 1 , lower priority Ž . Ž . Ž . <sup>y</sup>1 , or equal priority 0 with equal probability.

For a pair of bundles for which customer response is not yet known, expected value of priority is assumed. The information acquisition process is terminated when customer priority information for all pairs of knowledge bundles has been acquired. Each experiment is repeated over 100 iterations and the average of these iterations is presented in our results. We also vary the number of clusters to be formed from 4 through 6.

## 5.1. Comparison between successiÕe stages

Comparison of similarities between clusters formed in successive information acquisition stages is measured using the Rand Index. Sample plots of the Rand Index are shown in Fig. 2 when the number of features in the resource space are six and nine. For example, the value corresponding to stage 1 shows the similarity between cluster formed in the information acquisition stages 0 the initial stage and 1,Ž . stage 2 shows the index of similarity between the information acquisition stages 1 and 2, and so on.

Due to resource constraints, a vendor may want to target each cluster based on some representative statistic of the cluster. A discussed earlier, we utilize the median network of the cluster as the representative customer priority profile. A product vendor can use the median customer in a cluster as the basis for designing the characteristics of product offerings targeted to that cluster. For example, the median in each cluster would determine the features available to the customers. Thus, a change in the cluster

![](/api/attachments/R67M7Y2S/fulltext/images/d136a703c830218fe185bb2e630a39b83010c0555afe7a1b2a42bc9e12a9a418.jpg)

Comparison of Rand Index Between Sucessive Stages: Nine Feature Levels  
![](/api/attachments/R67M7Y2S/fulltext/images/d741ced1d92480b17597457156dc5342863f5731f9a7e8019388ceeddee4e34e.jpg)  
Fig. 2. Sample plots of cluster similarity during the information acquisition process.

Median changes between successive stages: Six Feature Levels  
![](/api/attachments/R67M7Y2S/fulltext/images/1cc8bc303b6bca60e2b3ee60d3868a4b03bfbe663176a15179ffcac6c52be53b.jpg)

Median changes between successive stages: Nine Feature Levels  
![](/api/attachments/R67M7Y2S/fulltext/images/428f650ebeba8e0489e9d295860d6283655df62e89cc06b29c9c958a2f2ec1ea.jpg)  
Fig. 3. Sample plots of median changes between successive clusters.

median signifies a change in the product characteristics aimed at the cluster, and hence has important implications for a vendor. We also investigate the cluster dynamics by observing how the medians of the clusters change in successive information acquisition stages. The plots in Fig. 3 show the average number of median changes between successive information acquisition stages.

It is observed from the plots that the similarity between successive stages jump up initially followed by a flat portion during which Rand Index increases only gradually. Following this, the similarity index jumps again and is followed by another flat portion in the curve till the end of the information acquisition process. The plot of median changes in Fig. 3 mirrors this behavior. It is observed that the change in medians is largely stable in the middle stages but changes rapidly in the beginning and final stages.

## 5.2. Comparison with the final clusters

If the vendor incurs significant costs during the information acquisition process, she may terminate the information acquisition process at some arbitrary stage. In such a case, it would be interesting to observe how the clusters formed in that stage would compare with the clusters formed in the final stage Žif the information acquisition process had been completed . For this purpose, we compare the clus-. ters formed at each stage with the clusters formed in the final stage. A sample plot of this comparison for six and nine feature levels is shown in Fig. 4. Similar plots are observed for other feature level also.

The plots in Fig. 4 are similar to that of Fig. 2 where successive stages were compared. The plots indicate that a vendor who wants to terminate the information acquisition process should either break it off in the first two or three stages or should continue the information acquisition process till almost the end of the information acquisition process to capture substantial information gains. If the vendor does not intend to complete the information acquisition process, it is not beneficial to terminate the information acquisition process in the middle stages.

## 5.3. Effect of preference probability Õalues

To test the robustness of the behavior exhibited by the information acquisition process, we altered

![](/api/attachments/R67M7Y2S/fulltext/images/eb7d62e549807ef182941278ddfffaedb661a68975ae18578259190468014139.jpg)

Comparison with the Final Clusters Using Rand Index: Nine Feature Levels  
![](/api/attachments/R67M7Y2S/fulltext/images/6a1a49afff07e9804ce15093c8a81092e57883b281fdc952b992277472cc095b.jpg)  
Fig. 4. Sample similarity Rand Index curve when compared with Ž . final clusters.

![](/api/attachments/R67M7Y2S/fulltext/images/8f0a55855f2ed98fe4f06402de87a3e7b198d5e6b20fa6a10595ee0db04ce766.jpg)

Comparison with Final Clusters: Six Feature Levels, 6 clusters  
![](/api/attachments/R67M7Y2S/fulltext/images/8050dac81abff0a72c6903d75913a941e6be28f9e8ca7a63a87f1d0ced36f03b.jpg)  
Fig. 5. Cluster comparisons for different probability values: six feature levels.

the probability values of the customer preference choices. The previous results were observed when all the three possible choices for pair-wise comparisons Ž . prefer, not prefer, and indifferent were assumed to be equally probable. We tested for two other probability values as follows.

Ž . 1 Probability of an AindifferentB response was set lower when compared to the other two responses, and the other two responses were equally probable Ži.e., indifferent <sup>s</sup> 0.25, prefer <sup>s</sup> 0.375, and not prefer<sup>s</sup>0.375 ..

Ž . 2 Probability of the consumer preferring broader coverage to narrow coverage in product bundles was considered higher. For example, given two bundles, Ž . Ž . three, narrow and two, broad , the probability of the consumer preferring two, broad was set higher. Ž . Specifically, we set a probability value of 0.5 for this, probability of not-preferring at 0.25 and indifference at 0.25.

Sample plots of comparison of cluster similarities under these conditions are shown in Figs. 5 and 6. We observe a phenomenon similar to the one observed earlier. Similar behavior has been observed in all other cases. Thus, it appears that the overall behavior of the information acquisition process is quite consistent, even though it is affected to some extent by the probability values associated with the customer choices.

## 5.4. Effect of number of customers

To test if the same results are observed when the number of customers are changed, we repeated the experiments with different number of customers Ž . varying the numbers between 20 and 50 . The behavior of the information acquisition process was observed to be essentially the same as in the previous sections. We have not presented the plots of the results for these experiments, as they are similar to the ones presented in the previous section.

![](/api/attachments/R67M7Y2S/fulltext/images/d20a4890c029cfc16151550ef4d1acf2db93840707a56c0a2aba2391f8c5d932.jpg)

Comparison with Final Clusters: Nine Feature Levels, 6 clusters  
![](/api/attachments/R67M7Y2S/fulltext/images/5da722e9a6e02a7f0bb776d5c2001f53711a885942a3f71857de556fba7879f4.jpg)  
Fig. 6. Cluster comparisons for different probability values: nine feature levels.

## 6. Discussion

The results from the previous section imply that an online marketer can benefit greatly by acquiring preference information about the customers in some initial time period. However, information acquisition that goes beyond the initial stages and stops during the midterm information acquisition stages does not seem to bring in additional value in a marginal sense. Thus, it appears that the information acquisition process follows a nonlinear pattern where a marketer would gain substantially by capturing some initial information about customer preferences. However, further information gathering that stops below the halfway stage would yield small gains in the preference information gathered. This may indicate that as new consumers come in, it pays off for the vendor to get some information from as many consumers as possible. Beyond the halfway stage, the vendor would again have substantial information gain up to a certain point, when the information gain starts tapering off again and finally levels off.

The pattern of median change curves of Fig. 3 indicates that the number of median changes quickly taper off within a few stages. For a vendor who is interested in targeting the median customer in each of the clusters this implies that the medians in each cluster are relatively stable after the first few stages. Thus, a vendor can target individual clusters using the medians fairly quickly during the information acquisition process. Only when it is required to have perfectly formed clusters will it be necessary to acquire additional priority information.

For the class of information acquisition problems studied here in a single agent case, it has been proven that information gain follows a logarithmic pattern where rapid information gain in the initial stages is followed by decreasing information gain in the latter stages 29 . However, there is no analytical<sup>w</sup> <sup>x</sup> solution available for the multiple agent case. The simulation conducted in this paper for the case of multiple agents shows a fascinating result. For a number of agents, n, such that $n > 1$ it appears that two logarithmic curves tacked onto each other represent the information acquisition process. In Figs. 7 and 8, we fit two piecewise logarithmic curves to the Rand Index plot of Fig. 4 Only Ž $n = 4 0$ is shown here . Note: In the regression equation, ‘ . Ž x’ indicates the information acquisition stage . As can be seen . from the figures, the curves closely match two piecewise logarithmic curves. It is observed that each piece occupies approximately half the total number of information acquisition stages. Furthermore, for all the cases tested $( n = 2 0 – 5 0 )$ the slope of the first logarithmic region is greater than the slope of the second logarithmic region.

All the above observations have several implications for an online marketer and they are as follows.

vIf the marketer is only interested in partially refined information, the first point of inflexion in the first piecewise logarithmic curve is the point to stop conducting information acquisition experiments.

vThe results of all the simulations show that this first point of inflexion corresponds to two information acquisition stages for each consumer.

![](/api/attachments/R67M7Y2S/fulltext/images/e33f30d5377f4536c604cf00d55070368c12762a46f0ba82b4862a75c2afa518.jpg)  
Fig. 7. Piecewise logarithmic curve fitting for the information acquisition process: six feature levels, four clusters.

![](/api/attachments/R67M7Y2S/fulltext/images/72a59526fdbfef352e8c61895c9c2eff06187afed2b0b7df81305f8ba7639855.jpg)  
Fig. 8. Piecewise logarithmic curve fitting for the information acquisition process: nine feature levels, six clusters.

vIf the marketer is interested in highly refined information then the second point of inflexion in the second piecewise logarithmic curve is where information acquisition should stop. Beyond this, there is not much appreciable information gain.

vIn any case, complete preference information acquisition cannot be justified because of the low information gain in advanced stages of information gathering.

vAt any information acquisition stage, the Rand Ž . similarity Index for an initial coarse clustering of consumers smaller number of clusters is less thanŽ . the Rand Index for an initial finer clustering largerŽ number of clusters see Fig. 4 . The similarity be-. Ž . tween the final and the initial clusters increases as the number of clusters of consumers increase. For instance, Fig. 4 shows that at the second information acquisition stage, for four clusters, the Rand Index is approximately 0.4, while for six clusters, the Rand Index is approximately 0.55. The implication is that the number of clusters of consumers chosen by the online marketer will have an impact on the quality of clusters defined in terms of the similarity obtained.Ž . This is more pronounced when less refined information is desired, i.e., when information gathering is stopped at the first inflexion point.

Having discussed several useful insights brought forth by our simulation experiments, we now present our concluding remarks in Section 7.

## 7. Conclusion

Recent technological advances have made it possible for businesses to track customer preferences dynamically, as opposed to static market research oriented preference information. This enables businesses to dynamically bundle their information products reacting to customer preferences in real time. However, currently there is a lack of theoretical models that can be used to acquire and analyze preference information, and customize such information gathering experiments. Further, there is also limited knowledge about the characteristics of the information acquisition process itself in such a dynamic setting and its impact on dynamically formed customer segments and product bundles. The contributions of the paper are twofold. First, it develops a model for dynamically profiling customer preferences to aid customized offerings in the presence of resource constraints based on the theory of questionnaires. Second, it examines the dynamics and the informational characteristics of the profiling technique for different sizes of the product attribute space and number of consumer segments. The model uses an adaptive nonmetric revealed preference approach to operationalize the process of preference information acquisition. The vendor AlearnsB about the customer’s preference orderings and consequently about the utility associated with the product or advertisement attribute space. This learning is conducted adaptively through a succession of experiments.

The vendor is faced with the problem of customizing product offerings for a customer. Ideally, the vendor could meet the exact needs of each consumer by providing the customized offering that each customer wants. However, in practice this will not be possible due to a number of constraints. Hence, the vendor would need to categorize consumers into groups such that consumers belonging to a certain cluster have similar priority rankings for the product bundles being offered. Given information about priorities, the vendor would then be able to customize product offerings for each consumer segment.

The following are the issues of concern here.

vModeling of dynamic profiles of customer preferences to aid responsive customized product offerings through customer segmentation.

vApplication of information theory based techniques to characterize preference networks of individual consumers.

vUsing clustering techniques to classify consumers into segments based on their preference networks.

vSimulation of the information acquisition process to observe its behavior in response to different sizes of the product attribute space and number of consumer segments. This is carried out using techniques such as the Rand Index and a network based median measure.

The paper presents a method for categorizing consumers based on preference network profiles collected sequentially and also utilizes the preference network profiles in each cluster to identify a representative customer profile, namely, the median network, for determining product attributes aimed at that cluster. Simulation exercises are conducted for different number of product attributes and different number of clusters to examine the behavior of these measures.

There are two limitations of the models discussed in this paper. First, it is assumed that no response errors are possible. Relaxation of this assumption is an area for future research. Second, the vendor makes only simple and fundamental minimal assumptions regarding the prior probabilities. In actual practice, however, the probabilities may have to be checked empirically and perhaps be derived from market share or other prior information. In such a case, the treatment shown in the paper above will not change, only the calculation of weights will. However, we believe that the results seen above in terms of the robustness of the questionnaires would allow us to use the strategy for questionnaire design under alternate prior distributions as well. Proof of this is an area for further research. Third, future research should also investigate the effect of changes in preference profiles over time, and the possibility that some consumer groups may change their preferences more frequently than others. In addition, it is important to point out that we have conducted the simulation results for up to 50 consumers. The computational complexity of the simulation runs lies in simulating the information acquisition process and not in the clustering of consumers itself. For statistical validity, we have chosen a large number of repeated simulations over a limited number of consumers, rather than choosing a large number of consumers and limited repeated simulations. In reality, a vendor would only need to compute the clusters based on the information gathered from customers. So, simulation of the information acquisition process would not be necessary. Hence, we believe that techniques presented here would be valid in larger scenarios as well.

## Acknowledgements

This research has been supported by NSF under grant 9505790 and the research of the third author has been supported in part by NSF under grant 9907325. We would like to thank the seminar participants at Cornell University, University of South Florida, University of Kansas, University of Missouri; Tulane University, University of Texas and Temple University, and the conference attendees at IJOQM, Ahmedabad, India, January 1999 and AIS Baltimore, 1999 for critical comments that have improved the lucidity of the paper.

## References

<sup>w</sup> <sup>x</sup> 1 M.K. Agarwal, P.E. Green, Adaptive conjoint analysis versus self-explicated models: some empirical results, International Journal of Research in Marketing 8 2 1991 141–146.Ž . Ž .

<sup>w</sup> <sup>x</sup> 2 P.V.S. Balakrishnan, M.C. Cooper, V.S. Jacob, P.A. Lewis, Comparative performance of the FSCL neural net and Kmeans algorithm for market segmentation, European Journal of Operational Research 93 2 1996 346–357.Ž . Ž .

<sup>w</sup> <sup>x</sup> 3 J.P. Barthelemy, B. Monjardet, The median procedure in data analysis: new results and open problems, in: H.H. Bock Ž . Ed. , Classification and Related Methods of Data Analysis, North Holland, Amsterdam, 1988.

4 K.P. Bogart, Some social applications of ordered sets, in: I. Rival Ed. , Ordered Sets. D. Reidel Publishing, Dordrecth, Ž . Holland, 1982.

<sup>w</sup> <sup>x</sup> 5 K.M. Carley, D. Banks, Metric inference for social networks, Journal of Classification 11 1995 121–150.Ž .

<sup>w</sup> <sup>x</sup> 6 M.L. Corstjens, D.A. Gautschi, Formal choice models in marketing, Marketing Science 2 1 1983 19–56.Ž . Ž .

<sup>w</sup> <sup>x</sup> 7 P. De, V.S. Jacob, R. Pakath, A formal approach for designing distributed expert problem-solving systems, Information Systems Research 4 2 1993 141–165.Ž . Ž .

<sup>w</sup> <sup>x</sup> 8 G. Dobson, S. Kalish, Positioning and pricing a product line, Marketing Science 7 2 1988 107–125.Ž . Ž .

<sup>w</sup> <sup>x</sup> 9 T.A. Gerace, US5848396: Method and Apparatus for Determining Behavioral Profile of a Computer User Patent Cita-Ž tion Issued: Dec. 8, 1998 ..

<sup>w</sup> <sup>x</sup>10 C.G. Gooley, J.M. Lattin, Dynamic customization of marketing messages in interactive media, Working Paper, Stanford University, 1998.

<sup>w</sup> <sup>x</sup> 11 P.E. Green, A.M. Krieger, Models and heuristics for product line selections, Marketing Science 4 1 1985 1–19.Ž . Ž .

<sup>w</sup> <sup>x</sup> 12 P.E. Green, V. Srinivasan, Conjoint analysis in marketing: new developments with implications for research and practice, Journal of Marketing 54 4 1990 3–19.Ž . Ž .

<sup>w</sup> <sup>x</sup> 13 P.E. Green, Y. Wind, New way to measure consumers judgements, Harvard Business Review 53 4 1975 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 14 L. Hubert, P. Arabie, Comparing partitions, Journal of Classifications 2 1988 193–218.Ž .

<sup>w</sup> <sup>x</sup>15 L. Hurwicz, Incentive aspects of decentralization, in: K.A. Arrow, M.D. Intrilligator Eds. , Handbook of MathematicalŽ . Economics, vol. III, North Holland, Amsterdam, 1986.

<sup>w</sup> <sup>x</sup> 16 J. Gantz, The web gets personal. Computerworld 1998 33, Ž . October.

<sup>w</sup> <sup>x</sup> 17 L. Hurwicz, T. Marschak, Discrete allocation mechanisms: dimensional requirements when desired outcomes are unbounded. Journal of Complexity 1 1985 264–303.Ž .

<sup>w</sup> <sup>x</sup> 18 E.M. Johnson, G.P. Huber, The technology of utility assessment. IEEE Systems, Man and Cybernetics 7 5 1977Ž . Ž . 311–325.

<sup>w</sup> <sup>x</sup> 19 J. Kalagnanam, H. Simon, Y. Iwasaki, The mathematical bases for qualitative reasoning, IEEE Expert 6 2 1991Ž . Ž . 11–19, April.

<sup>w</sup> <sup>x</sup> 20 S. Kullback, Information Theory and Statistics, Dover Publications, NY, 1968.

<sup>w</sup> <sup>x</sup> 21 R.D. Luce, Individual Choice Behavior: A Theoretical Analysis, Wiley, New York, 1959.

<sup>w</sup> <sup>x</sup>22 T. Marschak, Organizational design, in: K.A. Arrow, M.D. Intrilligator Eds. , Handbook of Mathematical Economics,Ž . vol. III, North Holland, Amsterdam, 1986.

<sup>w</sup> <sup>x</sup> 23 J. Marschak, R. Radner, Economic Theory of Teams, Yale Univ. Press, New Haven, CT, 1972.

<sup>w</sup> <sup>x</sup> 24 V.S. Mookerjee, B.L. Dos Santos, Inductive expert system design: maximizing system value, Information Systems Research 4 2 1993 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 25 J.C. Moore, H.R. Rao, A.B. Whinston, Multi-agent resource allocation: an incomplete information perspective, IEEE Transactions on Systems, Man and Cybernetics 24 8 1994Ž . Ž . August.

<sup>w</sup> <sup>x</sup> 26 J. Moore, H.R. Rao, A.B. Whinston, K. Nam, T.S. Raghu, Information acquisition policies for resource allocation among multiple agents, Information Systems Research 8 2 1997 Ž . Ž . 151–170.

<sup>w</sup> <sup>x</sup> 27 M. Mussa, S. Rosen, Monopoly and product quality, Journal of Economic Theory 18 1978 301–317.Ž .

<sup>w</sup> <sup>x</sup> 28 C.F. Picard, Graphs and Questionnaires. North Holland, Amsterdam, 1980.

<sup>w</sup> <sup>x</sup> 29 H.R. Rao, Two schemes for information acquisition: an entropic assessment, Automatica 30 5 1994 805–816.Ž . Ž .

<sup>w</sup> <sup>x</sup> 30 H.R. Rao, M. Agrawal, F. Salam, Internet browsers, in: J.G. Webster Ed. , Wiley Encyclopedia of Electrical and Elec-Ž . tronics Engineering, vol. 10, Wiley, New York, 1999.

<sup>w</sup> <sup>x</sup> 31 H. Sakagami et al., Effective personalization of Push-type Systems—Visualizing Information Freshness, presented at the 7th World Wide Web Conference, Australia, 1998.

<sup>w</sup> <sup>x</sup> 32 C. Sliwa, Customers not moved by push, Network World 14 Ž . Ž . 20 1997 .

<sup>w</sup> <sup>x</sup> 33 G.J. Stigler, S. Becker, De gustibus non est disputandum, American Economic Review 67 2 1977 76–90.Ž . Ž .

![](/api/attachments/R67M7Y2S/fulltext/images/31f2c96cf6ea0f55ce1ce1720e6767d9eae9917b8a865847e5f0767b47f197a9.jpg)

T.S. Raghu is Assistant Professor of Computer Information Systems in Arizona State University. Prior to joining ASU, he was a Mark Woodburn fellow at SUNY Buffalo, where he received his PhD in Management Information Systems. His research interests are in Business Process Change, Electronic Commerce, Collaborative Decision Making and Information Economics. He has also worked as a systems consultant at leading international IT consulting firms. His

publications have appeared in refereed international journals such as Information Systems Research, International Journal of Production Research, International Journal of Production Economics, Knowledge and Process Management, Decision Support Systems and Expert Systems with Applications. A number of his papers have also appeared in the proceedings of refereed international conferences such as ICIS, AIS, and Informs.

![](/api/attachments/R67M7Y2S/fulltext/images/0efe3f6dee896c263899999a2998800c232c23de538402dce7da6fb7869dd42c.jpg)

H.R. Rao is a Professor of Management Information Systems in State University of New York at Buffalo. His interests are in the areas of management information systems, decision support systems, and expert systems. He has chaired sessions at international conferences and presented numerous papers. He has authored or co-authored more than 50 technical papers, of which more than 30 are published in archival journals. He is the Co-Editor-in-chief of Information

Systems Frontiers: A journal of Research and Innovation. He has co-edited special issues of The Annals of Operations Research and the Communications of ACM and Decision Support Systems.

![](/api/attachments/R67M7Y2S/fulltext/images/e5a7cdb776525f3a2bf4fd1003743abb28ac77bff7ae70435ea782b377d7dcf1.jpg)

P.K. Kannan is a Safeway Fellow, Associate Professor of Marketing and Associate Director of the Center for E-Service in the Robert H. Smith School of Business at the University of Maryland, College Park. He received his PhD in Management from Purdue University. His current research focus is on e-commerce, centering around marketing information services on the Internet, pricing information products, e-promotions, and marketing and product developmen

![](/api/attachments/R67M7Y2S/fulltext/images/3aefbcef5cc9b27ae1572de361b323eafb2fceef1ef550b1352222ecfcd4be3f.jpg)

Andrew B. Whinston is the Hugh Cullen Chair Professor in information systems, computer science, and economics at the University of Texas at Austin. Dr. Whinston obtained his PhD from Carnegie-Mellon University in 1962. Since that time he has held academic posts at the University of Texas at Austin, Purdue University, University of Virginia, Yale University, and the University of California, Los Angeles. He was awarded the Ford Foundation

in virtual communities. His papers in this area have been published or forthcoming in Management Science, Communications of the ACM, and International Journal of Electronic Commerce. His other research interests center around consumer loyalty, competitive market structures, variety-seeking and reinforcement behaviors, and the effects of promotions on competition and competitive structures, with publications in Marketing Science, Management Science, Journal of Academy of Marketing Science, Journal of Business Research and International Journal of Research in Marketing. P.K. is an Associate Editor for Decision Support Systems and Electronic Commerce and serves on the editoria boards of Journal of SerÕice Research and International Journal of Electronic Commerce.

Faculty Research Fellowship in 1966. Dr. Whinston’s research has explored Artificial Intelligence, E-Commerce, Information Systems, and The New Economy. His professional service has been as Editor-in-Chief, Journal of Organizational Computing and Electronic Commerce. He is also the director for the Center for Research in Electronic Commerce. Contact him at abw@uts.cc. utexas.edu; http:<sup>rr</sup>crec.bus.utexas.edu.
