---
otero_id: 28534
otero_key: "ADHBP92X"
title: "Software Components and Product Variety in a Platform Ecosystem: A Dynamic Network Analysis of WordPress"
authors: "Sungyong Um; Bin Zhang; Sunil Wattal; Youngjin Yoo"
year: "2023"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.1172"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Software Components and Product Variety in a Platform Ecosystem: A Dynamic Network Analysis of WordPress

Sungyong Um,<sup>a</sup> Bin Zhang,<sup>b</sup> Sunil Wattal,<sup>c,</sup>\* Youngjin Yoo<sup>d</sup>

<sup>a</sup> Department of Information Systems and Analytics, School of Computing, National University of Singapore, Singapore 119391; <sup>b</sup> Department of Information and Operations Management, Mays Business School, Texas A&M University, College Station, Texas 77843; <sup>c</sup> Department of Management Information Systems, Fox School of Business, Temple University, Philadelphia, Pennsylvania 19122; <sup>d</sup> Department of Design and Innovation, Weatherhead School of Management, Case Western Reserve University, Cleveland, Ohio 44106 \*Corresponding author

Contact: sungyong@nus.edu.sg, https://orcid.org/0000-0003-0408-0733 (SU); binzhang@tamu.edu, https://orcid.org/0000-0003-0675-2222 (BZ); swattal@temple.edu, https://orcid.org/0000-0003-4078-5052 (SW); yxy23@case.edu, https://orcid.org/0000-0001-8548-3475 (YY)

Received: October 26, 2020 Revised: December 7, 2021; June 16, 2022 Accepted: August 21, 2022 Published Online in Articles in Advance: November 18, 2022

https://doi.org/10.1287/isre.2022.1172

Copyright: © 2022 INFORMS

Abstract. Software components, such as application programming interfaces (APIs), provided by both the platform owner and external developers in a platform ecosystem are vital to online digital platforms. These APIs are associated with functionality provided by the platform. A larger number of APIs used is generally associated with an increase in the platform ecosystem’s variety of products. However, the precise nature of the relationship between the use of APIs and product variety in a platform ecosystem is not yet known because of the lack of appropriate methodologies to analyze the complex data generated in such platform ecosystems. Drawing on a recombinatorial design perspective, we use a dynamic network model to create metrics for product variety in a digital ecosystem and study how the use of different types of APIs affects product variety. In particular, we theorize that, contrary to existing models, the structure of APIs in a large platform ecosystem is not limited to a core–periphery structure, but includes an additional third layer that we refer to as the regular core. We further hypothesize that external APIs in the regular core play a crucial role in increasing product variety in the ecosystem. To test our hypothesis, we conduct an empirical study using longitudinal data of all available digital product (i.e., plug-in) source codes on WordPress.org, the world’s largest content management system and one of the most extensive digital platform ecosystems. By analyzing all of the plug-ins on WordPress over 10 years from its inception, we find the support of our three-layer structure of APIs in a platform ecosystem: complete core, regular core, and periphery. Our empirical analysis further supports the role of external APIs in the regular core in increasing product variety. We, however, find that the strength of this effect diminishes in a newly created product category.

History: Param Singh, Senior Editor; Pallab Sanyal, Associate Editor 5

Funding: This work was supported by the Ministry of Education Singapore [Grants R-253-000-122-133 and T1-251RES1916], the National Science Foundation [Grants 1261977 and 1120966], and Club Informatique des Grandes Entreprises Franc¸aises. Supplemental Material: The e-companion is available at https://doi.org/10.1287/isre.2022.1172

Keywords: digital innovation • platform ecosystem • product variety • combinatorial design • API • plug-in • network method • hierarchical clustering • block modeling

## 1. Introduction

In a digital platform ecosystem, a firm “inverts” the innovation process. The platform owner allows thirdparty developers to create new products and services for the platform using various software components, that is, application programming interfaces (APIs; Parker et al. 2017).<sup>1</sup> In so doing, a platform ecosystem accomplishes an unprecedented level of product variety. For example, out of more than 2.2 million applications available in the Apple App Store for iOS as of the first quarter of 2021 (www.statista.com), only 145 are designed by Apple. To invert the firm, the platform owner provides a set of APIs to third-party developers. In turn, third-party developers recombine these APIs with other APIs from external sources to build a variety of digital products, such as apps and plug-ins (Ghazawneh and Henfridsson 2013, Eaton et al. 2015). Whereas past studies demonstrate the role of third-party developers in inverting firms using APIs (Boudreau 2012, Boudreau and Jeppesen 2015), we still do not know exactly how product variety grows in a platform ecosystem. Our study seeks to fill this gap.

Gaining a deeper insight into how third-party developers use various APIs to innovate and, thus, increase product variety in a platform ecosystem is important for several reasons. First, product variety is important to a platform ecosystem because it signals the level of innovation; high product variety helps the platform attract more users, creating a positive network externality for developers who create more digital products (Parker and Van Alstyne 2005). Second, despite the critical roles that APIs play, our understanding of the way they contribute to the extent of innovation is limited. Existing studies mainly focus on the effect of APIs on building duplicates of existing products using the same APIs (Xue et al. 2019). It is not clear how APIs are used to create new functional categories of products in a platform ecosystem (not just duplicates). Third, past studies on innovations in platform ecosystems suggest that firms might pursue different strategies for the different types of APIs (Eisenmann et al. 2011, Foerderer et al. 2018, Tiwana 2018). APIs can be provided by the platform itself (hereafter referred to as internal APIs) or by others (hereafter referred to as external APIs). Existing literature shows that internal APIs provide rudimentary functions that mainly communicate with the basis of the system and have an insignificant effect on product variety (Foerderer et al. 2018). Therefore, if the goal of a platform owner is to increase product variety by inverting the innovation process, the platform owner must understand to what extent it should encourage third-party developers to use external APIs, avoiding the loss of control (Eaton et al. 2015). Few studies, if any, explore the role of external APIs in platform ecosystems.

We draw on a recombinatorial design perspective (Fleming 2001, Arthur 2009) to study the role of external APIs on product variety in a digital platform ecosystem. We conceptualize each digital product in a platform ecosystem as a combination of internal and external APIs. Using such a recombinatorial design perspective, we study how the recombination patterns of APIs define product categories and ultimately determine the variety of functional categories. Product variety in a dynamic platform ecosystem comprises identifying groups of different digital products similar in functionality (Baldwin et al. 2014). We use a network model to empirically depict dynamic relationships between digital products and APIs in a platform ecosystem (MacCormack et al. 2006, Baldwin et al. 2014).

We use a unique data set collected from WordPress.org, the world’s largest content management system. Our data set covers the entire ecosystem of WordPress over 10 years since its inception in 2004 to 2014. The WordPress ecosystem is known for its vibrant and diverse set of functions with a large number of digital products (called plug-ins), most of which are designed and built by third-party developers. Using the data set, we define two networks, the plug-in and API networks. In the plug-in network, a node represents a plug-in and an edge represents the similarity between two plug-ins based on their use of APIs. We use the plug-in network to extract functional categories of plug-ins using their similarity and create a unique measure for product variety. In the API network, a node represents an API and an edge between two nodes represents the pair of APIs being used in the same plug-ins. With the API network, we identify different groups of APIs based on their use frequencies among all plug-ins. Using these network models, we explore the roles of external APIs on product variety in an ecosystem. Our research question is the following: how does the use of external APIs affect product variety in a platform ecosystem?

The paper is organized as follows. We first review existing literature on product variety, recombinatorial design, and the types of APIs. Second, we introduce our network models that describe the creation of digita products in a platform ecosystem as a combinatorial design process and three-layer structure defined by API use frequencies, and then, we create a measure for product variety. Third, we develop our hypotheses about the role of external APIs on the product variety in a platform ecosystem. Fourth, we present the results of our empirical study and robustness checks. We finally conclude the paper by discussing the academic and managerial implications of our findings.

## 2. Conceptual Foundation

## 2.1. Product Variety in Platform Ecosystems

Product variety refers to “the number of variants within a specific product group” (Lancaster 1990, p. 189). The role of product variety receives particular attention from scholars in innovation and management (Musalem et al. 2010, Zhou and Wan 2017). In the context of platform ecosystems (Yoo et al. 2010, Tiwana 2018), product vari ety refers to the number of different digital product categories within the specific platform ecosystem (Boudreau 2012). Many successful technology companies, such as Google, Apple, and Facebook, build their platform ecosystems to harness the creation of various digital products built by third-party developers (hereafter developers) (Parker et al. 2017). Developers capture users’ functiona needs and develop functional specifications for products without the direct intervention of the platform owner (Yoo et al. 2010). By adding unique features to their prod ucts, developers extend the boundary of the platform ecosystem (Eaton et al. 2015). A high degree of product variety in a platform ecosystem attracts more users on the demand side of the ecosystem, which, in turn, attracts more developers on the supply side, forming a virtuous cycle between the two groups (Parker and Van Alstyne 2005, Hagiu 2014).

Given its importance, scholars examine how product variety can be achieved in a platform ecosystem (Adner and Kapoor 2010, Gawer and Cusumano 2002, Cennamo and Santalo 2013). In particular, APIs emerged as an important tool for developers to share knowledge in a platform ecosystem that, in part, increases product variety. Thus, a platform ecosystem with diverse APIs (Tiwana 2015) enjoys continuous innovation and increased product variety (Parker et al. 2017). Furthermore, in a platform ecosystem, digital products built through the recombination of various APIs do not just increase product variety of the same kind (Yoo et al. 2010, Tiwana 2015). In such a digital ecosystem, novel combinations of existing APIs can serve as the building blocks of different kinds of digital products (Arthur 2009, Stanko 2016, Tiwana 2018). In this process, the owner of the platform ecosystem can control or facilitate product variety primarily through provisioning its own internal APIs and controlling the use of external APIs.

Finally, the measure of product variety in a digital ecosystem is more complicated than simply counting the number of digital products belonging to the same category (Baldwin et al. 2014). Categories represented by their major functionalities do not necessarily mean that each product in the same category is built by the exact same APIs (Haefliger et al. 2008). Moreover, because the recombination of APIs to form digital products is an ongoing process, there is an underlying dynamism in the product variety of the ecosystem (Levinthal and Marino 2015), which needs a deeper understanding of the complex interrelations between APIs involved in building the digital ecosystem.

## 2.2. Recombinatorial Design and Digital Product Designs

The recombinatorial design refers to a way of building products through synthesizing constituent components (Fleming and Sorenson 2001). It has its root in Newell and Simon (1972), who conceptualize design as the process of pursuing desirable combinations of different components in a problem space. They see the problem space as a multidimensional space in which each point represents a particular combination with specific cost and performance. The recombinatorial design perspective provides a powerful foundation in understanding all forms of product design (Garud and Kumaraswamy 1995), organizational design (Ethiraj and Levinthal 2004), and innovation (Fleming and Sorenson 2004). It becomes even more important in the context of digital innovations (Arthur 2009, Brynjolfsson and McAfee 2014) because of the unique nature of digital technology that makes it easy for digital resources to be recombined (Yoo et al. 2010, 2012).

Scholars analytically conceptualize recombinatorial design using Kauffman’s (1993) model in which each design option is characterized as a combination of different components. Using a simulation model, Levinthal (1997) explores how different organization designs facilitate adaptation to changing environments. Fleming and his colleagues use patent data to show that scientific discovery changes the way innovators follow combinatorial design processes by eliminating fruitless combinations (Fleming and Sorenson 2004) and different collaborative structures influence the innovation (Fleming et al. 2007).

Building on this recombinatorial design framework, we conceptualize digital products in the WordPress ecosystem, called plug-ins, as a combination of various software components, namely, APIs (Lyytinen et al. 2010). Third-party developers pursue combinatorial designs of plug-ins by exploring different combinations of APIs.<sup>3</sup> It is worth noting that the problem space with APIs is theoretically unbounded for both platform owners and third-party developers as new APIs can continue to emerge. Thus, developers face recombinatorial choices that continue to change over time. Such continually changing recombinatorial problem space is likely to influence design choices of third-party developers for both new and existing plug-ins, influencing the product variety of the platform. No study, however, explores how the recombinatorial design of APIs influences product variety at the ecosystem level.

## 2.3. APIs and API Types

In a digital platform ecosystem, APIs play a crucial role as they are the primary means for how developers design digital products through recombination. An API is a set of functions that comes from the collective knowledge of builders and has a well-established set of interfaces (Yoo et al. 2012). It is an independent and interchangeable module for building digital products, hence allowing more efficient digital product designs (Laursen and Salter 2014).

Existing literature categorizes APIs into two types: internal APIs that are provided by platform owners and external APIs that are offered by other developers (Schubert et al. 2013, Tiwana 2018). Developers who create external APIs include other platform owners and individual developers who are outside of a focal platform. These external APIs allow developers to pursue various recombinations of APIs to increase product variety across multiple digital product providers (Yoo et al. 2010, Brunswicker et al. 2019). In a typical platform ecosystem, the platform owner plays a central role in distributing and sharing internal APIs that enable the easy adoption of useful components for the creation of all necessary functions of product designs (Von Hippel and Von Krogh 2003, Kleis et al. 2012). At the same time, by not offering certain internal APIs or by not allowing certain external APIs, the platform owner can exercise control over what types of innovation can or cannot be allowed in its ecosystem (Eaton et al. 2015, Foerderer et al. 2018).

Because different APIs come with different functions and qualities, not all APIs are equally useful. And use frequency of APIs among developers depends on their usefulness (Yoo et al. 2010). For example, there are many competing APIs with similar mapping function; Google Maps APIs is overwhelmingly popular among developers (www.statista.com). If an API is preferred by many developers, they are recombined with many other APIs. However, we know little about why certain external APIs have higher use frequency and are recombined with more diverse APIs, thus leading to higher product variety, than other APIs. Given that APIs are one of the most important and often contested tools for product variety in platform ecosystems (Stanko 2016, Brunswicker et al. 2019), it is important to understand how external APIs affect the product variety of a platform ecosystem.

## 3. Network Modeling

We use a network framework to explore how the recombinatorial design of APIs influences the product variety of a platform ecosystem. Our network model begins with the conceptualization of product design as a recombinatorial action in which a developer seeks to combine available APIs in order to build a product $( \mathrm { i . e . , }$ a plug-in) that delivers a certain functional value to target users (Simon 1996, Fleming 2001).<sup>4</sup> A network model shows how products are created through recombinations of different APIs based on function calls (MacCormack et al. 2006). Specifically, in a product network, plug-ins are represented as nodes, and the functional similarities between plug-ins are represented as edges. The functional similarity between any two plugins is calculated based on a ratio of the common APIs used between them.

In Figure 1, we display a recombinatorial design of three digital products $( P _ { 1 } , P _ { 2 } , P _ { 3 } )$ , developed by recombining five APIs, that is, two internal (A and B) and three external (C, D, and E) APIs. The three digital products form a network by sharing the same APIs. For example, $P _ { 1 }$ and $P _ { 2 }$ share the same functionality by using internal API A and external API C but have their own unique function by employing internal API B and external API D, respectively. For products that are built using the same APIs in their API uses, we define their

similarity as similarity $\begin{array} { r } { \mathbf { \langle } P _ { 1 } , P _ { 2 } ) = \cos ( \theta _ { 1 } ) = \frac { \overrightarrow { P _ { 1 } } \cdot \overrightarrow { P _ { 2 } } } { \Vert \overrightarrow { P _ { 1 } } \Vert \Vert \overrightarrow { P _ { 2 } } \Vert } . } \end{array}$

Some combinations of APIs are used with high frequency across many different functional product categories (Stanko 2016, Kyriakou et al. 2017). We group products with high similarity together and define them as a (functional) category. When a group of APIs are repeatedly used together and collectively define the architecture of a type of digital products, they can act as a design pattern (Abernathy and Utterback 1978, Henderson and Clark 1990). Thus, digital products containing the same design pattern belong to the same product category. From a network modeling perspective, these digital products with the same design pattern form a cluster in the network (MacCormack et al. 2006). The higher the ratio of common APIs shared by two products, the more closely they are connected.

With the clusters of similar digital products that share common APIs, the network can be represented as a topological overlap matrix (TOM) (Horvath 2011, Hawrylycz et al. 2012) in which each element represents the similarity of two plug-ins. The higher the ratio of APIs shared by two plug-ins, the higher their similarity (Ravasz et al. 2002). In prior literature, product variety is defined as the number of functional categories. A functional category is a group of products with similar functions (Boudreau 2012). Functional categories are nested; a large category contains multiple smaller subcategories (Ethiraj and Levinthal 2004). In our network model, subcategories are represented as smaller subclusters with a category, which are a group of products showing higher similarities than other products in the same category (Murmann and Frenken 2006). Therefore, the product variety at a functional category can be measured with the number of subclusters within each cluster. An increase in the number of subclusters not only increases product diversity within a cluster; it also eventually leads to the possibility that the cluster becomes diverse enough, giving birth to a new cluster. Therefore, the product variety at the ecosystem level is the sum of product variety in all functional categories. In summary, we measure the product varieties of the ecosystem by identifying all the categories and counting all subcategories within them (Hawrylycz et al. 2012).

Figure 1. The Recombinations of APIs and Digital Product Development  
![](/api/attachments/ADHBP92X/fulltext/images/bb2f07657eeb387a3e26aac3e17d1b05ff479ab91abd5e003dc577969e1f2a23.jpg)  
\*Similarity(P1,P2) = similarity({A,B,C}, {A,C,D}) = cos(θ1)

Table 1. Notation System for Modeling a Platform Ecosystem

<table><tr><td>Variable</td><td>Description</td></tr><tr><td> $\overrightarrow{I_{kt}}$ </td><td>A vector of all internal APIs used in digital products k at time t</td></tr><tr><td> $\overrightarrow{E_{kt}}$ </td><td>A vector of all external APIs used in digital products k at time t</td></tr><tr><td> $\overrightarrow{P_{kt}}$ </td><td>A vector of all APIs used in digital products k at time t</td></tr><tr><td> $\mathbf{I}_{t}$ </td><td>A matrix of all internal APIs at time t</td></tr><tr><td> $\mathbf{E}_{t}$ </td><td>A matrix of all external APIs at time t</td></tr><tr><td> $\mathbf{P}_{t}$ </td><td>A matrix of all APIs in digital products at time t</td></tr><tr><td> $\mathbf{S}_{t}$ </td><td>A similarity matrix of digital products at time t</td></tr><tr><td> $\mathbf{A}_{t}$ </td><td>A weighted adjacency matrix of digital products at time t</td></tr><tr><td> $\mathbf{W}_{t}$ </td><td>A TOM of digital products at time t</td></tr><tr><td> $\boldsymbol{\Gamma}_{t}$ </td><td>A software component (API) adjacency matrix at time t</td></tr><tr><td> $p_{ij}$ </td><td>Element in  $\mathbf{P}_{t}$ , binary indicator of digital product j using API i at time t</td></tr><tr><td> $s_{ij}$ </td><td>The similarity measure between digital products i and j in  $\mathbf{S}_{t}$ </td></tr><tr><td> $a_{ij}$ </td><td>The adjacency indicator between digital products i and j in  $\mathbf{A}_{t}$ </td></tr><tr><td> $\beta$ </td><td>The soft thresholding number to suppress low correlations in  $a_{ij}$ </td></tr><tr><td> $k_{i}$ </td><td>The sum of adjacency weights between digital product i and neighbors</td></tr><tr><td> $l_{ij}$ </td><td>The sum of adjacency weights when digital products i and j are connected</td></tr><tr><td> $w_{ij}$ </td><td>Element in TOM ( $\mathbf{W}_{t}$ ), topological overlap measure between API i and j</td></tr><tr><td> $\gamma_{ij}$ </td><td>Element in  $\boldsymbol{\Gamma}_{t}$ , a software component (API) adjacency matrix at time t</td></tr></table>

To see how the different use patterns of APIs affect product variety, we need to differentiate APIs based on their frequency of use. To achieve this goal, we build a second network model to describe the relationship between APIs. Specifically, in this model, nodes represent APIs and edges represent whether two APIs are used together to build the same plug-ins. The objective of this step is to confirm whether APIs with different use frequencies for combinatorial product designs can be grouped in a core-periphery structure. Prior studies find core/periphery structures, in which components that are used more frequently together are densely connected with each other and are defined as the core of the network, whereas those that are used less frequently are defined as the periphery of the network (Baldwin et al. 2014). Next, we explain in detail the mathematical model that describes the platform ecosystem and the combinatorial product design within it. For the complete notation system used in our modeling process, please refer to Table 1 in this section.<sup>5</sup>

## 3.1. Modeling of Product Network in Platform Ecosystem

First, we explain the modeling process of a product network in a digital platform ecosystem. We consider a platform ecosystem to be dynamic: across each time period, new APIs and new digital products emerge. Developers use existing and new APIs as they design new digital products and update existing ones. Therefore, the changing set of APIs affects the product variety in a platform ecosystem.

To model this, we represent a plug-in (a digital product) k in time period t as $P _ { k t }$ . In order to build $P _ { k t } ,$ , the developer combines an appropriate set of APIs from both available internal APIs, represented as set $I ,$ and external APIs, represented as E (see the following equations):

$$
\begin{array}{c} {I = \{I _ {1}, \ldots , I _ {M} \}, | I | = M,} \\ {E = \{E _ {1}, \ldots , E _ {N} \}, | E | = N.} \end{array}
$$

We define these chosen internal APIs for product k at time t as a column vector $I _ { k t } ^ { ' }$ . The length of the vector is equal to the total number of internal APIs. If the developer chose an API for $P _ { k t } ,$ , the corresponding representative element in the vector is set to one and otherwise zero. Similarly, we also define chosen external APIs to build $P _ { k t }$ as a column vector $\overrightarrow { E _ { k t } }$ . The resulting product $P _ { k t }$ is defined as a concatenation of column vectors $I _ { k t } ^ { ' }$ and $\overrightarrow { E _ { k t } }$ , that is, $\overrightarrow { P _ { k t } } = \overrightarrow { I _ { k t } } \overrightarrow { E _ { k t } }$ . For an example of the construction of $\overrightarrow { I _ { k t } } , \overrightarrow { E _ { k t } }$ , and $\overrightarrow { P _ { k t } }$ , please refer to Appendix $\mathrm { A } .$

Considering all the digital products created at time $t , P _ { 1 t } , \ldots , P _ { K t }$ , the internal APIs used to create the aforementioned products, $I _ { 1 t } , \ldots , I _ { K t }$ , can be combined column-wise as a matrix $\mathbf { I } _ { t } \colon$

$$
\mathbf {I} _ {t} = \left[ \begin{array}{c c c c} \overrightarrow {I _ {1 t}} & \overrightarrow {I _ {2 t}} & \ldots & \overrightarrow {I _ {K t}} \end{array} \right].
$$

Similarly, the usage of external APIs by all products can be defined as matrix $\mathbf { E } _ { t } \mathbf { . }$

$$
\mathbf {E} _ {t} = \left[ \begin{array}{c c c c} \overrightarrow {E _ {1 t}} & \overrightarrow {E _ {2 t}} & \ldots & \overrightarrow {E _ {K t}} \end{array} \right].
$$

Building upon the notation of $\mathbf { I } _ { t }$ and $\mathbf { E } _ { t } ,$ all products that are developed in the platform ecosystem at time t can be represented as matrix $\mathbf { P } _ { t } ,$ , which is the row-wise concatenation of $\mathbf { I } _ { t }$ and $\mathbf { E } _ { t } \mathbf { : }$ :

$$
\mathbf {P} _ {t} = \left[ \begin{array}{c} \mathbf {I} _ {t} \\ \mathbf {E} _ {t} \end{array} \right] = \left[ \begin{array}{c c c c} \overrightarrow {I _ {1 t}} & \overrightarrow {I _ {2 t}} & \ldots & \overrightarrow {I _ {K t}} \\ \overrightarrow {E _ {1 t}} & \overrightarrow {E _ {2 t}} & \ldots & \overrightarrow {E _ {K t}} \end{array} \right].
$$

At any given time period $t ,$ matrix $\mathbf { P } _ { t }$ can be interpreted as the relationship between APIs and products because each column of $\bar { \mathbf { P } } _ { t }$ represents a product’s APIs, both internal and external. Meanwhile, each row represents the usage of API in all products, $\overrightarrow { P _ { 1 t } } , \dots , \overrightarrow { P _ { K t } }$ . Based on this definition of the row and column, we can also name $\mathbf { P } _ { t }$ as the API–product matrix. For details and examples of the construction of $\mathbf { I } _ { t } , \ \mathbf { E } _ { t } ,$ , and $\mathbf { P } _ { t } ,$ , please refer to $\mathrm { A }$ ppendix A. Examples of how all the products evolve from one time period to the next are also presented in the same appendix.

Once matrix $\mathbf { P } _ { t }$ is obtained, we can define the product adjacency matrix $\mathbf { A } _ { t } \mathbf { : }$

$$
\mathbf {A} _ {t} = \left[ \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 K} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 K} \\ \vdots & \vdots & \ddots & \vdots \\ a _ {K 1} & a _ {K 2} & \dots & a _ {K K} \end{array} \right],
$$

where $a _ { i j } = ~ | s _ { i j } | ^ { \beta } , ~ s _ { i j } = { \frac { 1 + c o r r ~ ( { \overrightarrow { P _ { i t } } } , { \overrightarrow { P _ { j t } } } ) } { 2 } } ~ ( \beta \in \mathbb { Z } ^ { + } , \beta > 1 )$

Each cell in matrix $\mathbf { A } _ { t }$ describes the similarity of any two products based on the common API they share. The entry of adjacency matrix $\mathbf { A } _ { t } , a _ { i j } ,$ is defined as an exponentiation function of $s _ { i j } ,$ which is the entry of similarity matrix $\mathbf { S } _ { t }$ . Entry $s _ { i j }$ is a linear transformation of the correlation between two products, $P _ { i t } ^ { ' }$ and $P _ { j t }$ . The exponent $\beta ,$ also called the soft thresholding number, is an integer larger than one and serves to suppress low correlations. According to Langfelder and Horvath (2008), $\beta$ is set between 5 and 10 but most commonly at 6. Adjacency matrix $\mathbf { A } _ { t }$ only retains entries with a high value, whereas those with low value are approximated to zero. Digital product adjacency matrix ${ \bf A } _ { t }$ is symmetric with all zeros on the main diagonal. For the detailed definition of similarity matrix $\mathbf { S } _ { t } ,$ the transformation from $\mathbf { S } _ { t }$ to $\mathbf { A } _ { t } ,$ and examples of these two matrices, please refer to Appendix A.

Based on product adjacency matrix $\mathbf { A } _ { t } ,$ , we then construct the TOM, $\mathbf { W } _ { t } .$ , and identify groups of products that are built with similar APIs. The topological overlap matrix is a widely used tool for detecting nested network clusters that consist of nodes that are closely connected or highly similar (Ravasz et al. 2002, Horvath 2011). A topological overlap matrix at time $t , \mathbf { W } _ { t } ,$ is defined as

$$
\mathbf {W} _ {t} = \left[ \begin{array}{c c c c} w _ {1 1} & w _ {1 2} & \dots & w _ {1 K} \\ w _ {2 1} & w _ {2 2} & \dots & w _ {2 K} \\ \vdots & \vdots & \ddots & \vdots \\ w _ {K 1} & w _ {K 2} & \dots & w _ {K K} \end{array} \right],
$$

$$
w _ {i j} = \left\{ \begin{array}{c l} \frac {l _ {i j} + a _ {i j}}{\min \left(k _ {i} , k _ {j}\right) + 1 - a _ {i j}} & i f i \neq j \\ 1 & i f i = j, \end{array} \right.
$$

where $\begin{array} { r } { \boldsymbol { l } _ { i j } = \sum _ { u } a _ { i u } a _ { j u } , \boldsymbol { k } _ { i } = \sum _ { u } a _ { i u } , 1 \leq u \leq K , } \end{array}$ and the index u goes through all products. Entry $l _ { i j }$ measures the total number of common neighbors of i and $j ,$ and $k _ { i }$ is the sum of all the adjacency weights between product i and all its neighbors. It is the weighted degree (also called “close connectivity”) of i and represents the sum of the connection strengths of i with other network nodes (products). Consequently, the transformed entry $w _ { i j }$ (also called topological overlap measure) evaluates the relative connection strength between nodes in the network (Ravasz et al. 2002, Doncheva et al. 2012). It is also a measure of the similarity between nodes. It takes the degree centrality of each node into consideration and, thus, is a normalized measure and even better reflects similarity. Entry $w _ { i j }$ is within the range [0, 1]. The larger the value, the higher the similarity between two products i and j.

TOM W is a block matrix and is used to detect nested clusters representing subcategories. Clusters consist of densely connected products, in which connections represent the similarities between products. The higher the similarity between two products, the closer they are. Because similarity is derived from the ratio of commonly used APIs, and each API contains a particular function, similarity is also defined by functions. Each cluster represents a functional category. Different functional categories of products are constructed through particular combinations of APIs (Haefliger et al. 2008), which is how the functional characteristics come into being (MacCormack et al. 2006, Haefliger et al. 2008, Baldwin et al. 2014).

The more subclusters identified in a cluster of $\mathbf { } { \mathbf { } } { \mathbf { } } \mathbf { W } _ { t } ,$ the higher product variety that category has. In this paper, we use the number of subclusters in each cluster to measure the product variety in each functional category. For an example of using $\mathbf { W } _ { t }$ to find the nested clusters of products, please refer to Appendix A.

## 3.2. Modeling the Use Frequency of APIs

APIs differ in the extent of their use, and certain APIs are more frequently used than others when building products to achieve product variety (Von Hippel and Von Krogh 2003, Boudreau and Lakhani 2015). Following this reasoning, APIs can be grouped based on their frequency of use in building products (Baldwin et al. 2014). For the next step, we want to investigate whether product variety is affected by the use frequencies of APIs. Product variety can be driven by (the number of) common APIs that are used very frequently because APIs that have high use frequencies possess functions with a high degree of popularity. These kinds of APIs are the preferred components used in many subcategories in a functional category. The more popular APIs are, the more subcategories these APIs are used in. Now, taking the point of view of APIs, we want to use groups of APIs to explain the choice process through which APIs are used to create products.

To specifically explore the impact of the combination of APIs on creating products, we build a network about APIs. This network is modeled as an unweighted API adjacency matrix $\left( \Gamma _ { t } \right)$ as shown:

$$
\boldsymbol {\Gamma} _ {t} = \left[ \begin{array}{c c c c} \gamma_ {1 1} & \gamma_ {1 2} & \dots & \gamma_ {1 H} \\ \gamma_ {2 1} & \gamma_ {2 2} & \dots & \gamma_ {2 H} \\ \vdots & \vdots & \ddots & \vdots \\ \gamma_ {H 1} & \gamma_ {H 2} & \dots & \gamma_ {H H} \end{array} \right].
$$

Matrix $\Gamma _ { t }$ describes an indirect network and shows the use of each API in all products. Any entry $\gamma _ { i j }$ is binary equal to one if APIs i and j are both used in the same product and equal to zero otherwise. For an example of $\Gamma _ { t } ,$ please refer to Appendix A. A summary of all the notations we use is provided in Table 1.

By exploring the entries of $\Gamma _ { t . }$ , we can determine which APIs are important in the ecosystem (i.e., used more frequently and densely connected). We transform <sup>G</sup> to a core/periphery structure (Fortuna et al. 2011, Gallagher et al. 2021). A core/periphery structure classifies nodes in a network into two layers: core and periphery (Baldwin et al. 2014). A core is defined as a group of nodes that are densely, often fully, connected, whereas a periphery is defined as a group of nodes that are connected to the core nodes but themselves are not densely interconnected with other peripheral nodes (Borgatti and Everett 2000, Murmann and Frenken 2006). To iden tify the core/periphery structure in the API adjacency matrix, we use generalized blockmodeling (Doreian et al. 2005). Following this method, we move all the $^ { \prime \prime } { 1 ^ { \prime \prime } }$ entries in $\Gamma _ { t }$ to be adjacent to each other across the main diagonal and all the $\prime \prime 0 \prime \prime$ entries to be adjacent to each other so that a pattern of 1-block and 0-block is formed. After the transformation, a perfect 1-block indicates the core, and the rest form the periphery.<sup>6</sup>

## 4. Hypothesis Development

Existing literature conceptualizes a platform ecosystem with software components with two layers: a core and a periphery (Baldwin et al. 2014). In this model, the usefulness of software components differentiates use frequencies, which, in turn, divide them into two groups (Murmann and Frenken 2006). In the early stage of aplat form ecosystem, software components in the core are used to build system interfaces and back-end administra tion functions offered by the platform owner, and only a few external APIs enhance the functionality of the digital products on the platform. Because these functions need to exist in every product on the platform, software components in the core have high use frequency. APIs in the periphery have low use frequencies and provide useful functions (e.g., online payment and content management) that are not provided by the core APIs to products. As such, APIs in an early digital platform ecosystem are likely to follow a typical core–periphery structure.

Once a platform ecosystem grows, however, the number of digital components increases (Fortuna et al. 2011). New APIs are recombined with existing APIs to create digital products (with new features). Some APIs contain new functions that did not exist before. If those APIs are proven to be useful, more developers will likely use them, increasing their use frequency (Ethiraj and Levinthal 2004). At the same time, even though useful APIs are used by many products, they are not likely to be used by all products because those APIs are not necessarily essential to exist in the ecosystem. Therefore, we conjecture the emergence of a third layer of APIs, distinct from both core and periphery, as the platform ecosystem grows (Kojaku and Masuda 2018). That is, when the platform ecosystem grows into a mature and complex system, besides an all-ones block representing the core and an all-zeros block representing the periphery, we can also expect to see another layer with an imperfect 1-block in all time periods. An imperfect 1-block’s vast majority of entries are ones, and very few entries are zeros (Doreian et al. 2005).

In Figure 2, using a block-modeling analysis, we can represent three dotted rectangles in the diagonal region in the API adjacency matrix. First, following prior work (Borgatti and Everett 2000), we expect to find a block of

Figure 2. (Color online) An Example of the API Adjacency Matrix Consists of Three Blocks

<table><tr><td rowspan="2"></td><td colspan="2">Complete Core</td><td colspan="5">Regular Core</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>1</td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>2</td><td>1</td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>3</td><td>1</td><td>1</td><td></td><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td>4</td><td>1</td><td>1</td><td>1</td><td></td><td>1</td><td>1</td><td>0</td></tr><tr><td>5</td><td>1</td><td>1</td><td>1</td><td>1</td><td></td><td>0</td><td>0</td></tr><tr><td>6</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td></td><td>0</td></tr><tr><td>7</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr></table>

APIs that are fully connected with each other in the group and fully connected with APIs in other groups. We refer to them as the complete core. In Figure 2, the complete core APIs 1 and 2 are fully connected with all five other APIs as shown in the off-diagonal region. In a platform ecosystem, the complete core APIs act as a functional “core” containing the system interface and related services (Baldwin et al. 2014). In other words, they are always used together by all products in a platform system, acting as the source of basic functions for product creation (Tushman and Rosenkopf 1992, Murmann and Frenken 2006). Thus, complete core nodes are adjacent to all other APIs in the adjacency matrix. We expect these to be primarily internal APIs (represented by I ; Helfat and Raubitschek 2018).

Second, also consistent with the prior work (Borgatti and Everett 2000), we expect to find a null block of APIs grouped together. We refer to this group as the periphery. These are APIs that are sparsely connected with APIs in other blocks. These APIs are only occasionally used in individual products and are not used frequently in many products. In Figure 2, the periphery APIs 5, 6, and 7 are sparsely used together with other APIs as displayed in the off-diagonal region. APIs are used to functionally differentiate digital products compared with other digital products (Tushman and Rosenkopf 1992, Murmann and Frenken 2006), thus acting as the source of functional variations that increase design choice (Baldwin and Clark 2000). Hence, we expect that the majority of periphery APIs are external APIs (represented by E ).

Finally, following Doreian et al. (2005), we label the API block that sits between the complete core and the periphery as the regular core. Regular core APIs are not fully connected as are those in the complete core, but still possess a relatively high 1-entry ratio—much higher than the APIs on the periphery. In a platform ecosystem, regular core APIs are likely to be functionally useful and widely used across multiple functional categories. We expect that some of these APIs form a distinct set of cohesive functions that are repeatedly used by a functiona category of products. As such, we expect that regular core APIs construct the key functions of products and add functional varieties. In Figure 2, the regular core APIs 3 and 4 are connected to most other APIs as indicated in the off-diagonal region. For a detailed explanation of using generalized block modeling to identify the three-layer structure of API use frequency, please refer to Appendix A.3.

Taken together, an ecosystem in the early stage with a relatively small number of products (Fortuna et al. 2011) has a simple two-layer structure of a core and a periphery. The core includes the APIs for providing essential functions to exist in the ecosystem, whereas the periphery includes the APIs for defining useful functions. However, as the ecosystem grows into a large and mature ecosystem such as WordPress, we expect to see an additional layer of APIs that reflect the growing variety in design patterns of a large number of diverse products in the ecosystem.

Hypothesis 1 (APIs’ Layered Structure in the Later Stage). As the ecosystem grows into a mature and complex system, APIs can be categorized into three layers based on their use frequency: complete core, regular core, and periphery.

The use of external APIs helps developers to easily access the knowledge of others (Laursen and Salter 2006, Parker et al. 2017). For example, “Yahoo Weather API” is an external API for the latest weather information. “Culture Trip,” an app that provides tips for different locations, can include weather information by using “Yahoo Weather API” without creating weather-related functions (Lifshitz-Assaf 2018). Such functional uses of external APIs create a “spillover effect” (Laursen and Salter 2014) by which external APIs facilitate the creation of diverse digital products leveraging the knowledge of other developers (Parker et al. 2017, Jacobides et al. 2018). Through the APIs’ spillover effect, the product variety of the platform ecosystem grows to satisfy various users needs (Ghazawneh and Henfridsson 2013, Eaton et al. 2015). Many APIs are agnostic to products and can be easily used for any products as long as developers follow the established interfaces (Yoo et al. 2010). Thus, a growing pool of external APIs enhances the efficiency of creating digital products (Tiwana 2018). Taken together, the spillover effect broadens the functional uses of external APIs and results in the creation of more subcategories (Battke et al. 2016), thus increasing product variety.

However, not all external APIs have the same effect on product variety (Xue et al. 2019). Different functional values of external APIs lead to different frequen cies in their uses (MacCormack et al. 2006). If certain external APIs provide more functional value, they are more frequently adopted by many new products (Baldwin et al. 2014). These products form new subcategories that did not exist in the platform before (Fortuna et al. 2011). This positively impacts product variety (Baldwin and Clark 2006).

We use the three-layer structure to identify external APIs with different use frequency. When a periphery API is first used, certainly it is in the periphery. However, as the periphery API is used more frequently over time to build many products, eventually it can become a part of the regular core. Hence, external APIs in the regular core have high use frequency with strong spillover effects in increasing product variety. Therefore, an increase in the number of external APIs in the regular core positively affects the product variety in the functional categories. An increase in the number of external APIs in the regular core implies more available design choices to diversify the recombination of APIs and increase product variety (Baldwin and Clark 2006).

Hypothesis 2 (External APIs and Product Variety). The number of external APIs in the regular core is positively correlated with the product variety of each product functional category in a platform ecosystem.

Finally, the effect of external APIs in the regular core on product variety changes over time. In a platform ecosystem, when certain products gain popularity among users, they are likely to attract imitations from competitors that use similar, if not the same, combinations of APIs (Yoo et al. 2012). Such popular and commonly used APIs can become popular design patterns that are repeatedly used by developers (Anderson and Tushman 1990). As the number of products that use the same or a similar set of APIs grows, they eventually form a new functional category (Foerderer et al. 2018, Xue et al. 2019). Therefore, when a product category newly emerges, the majority of the developers are likely to try to imitate the popular design pattern that led to the emergence of the category (Ethiraj and Levinthal 2004, Burford et al. 2021). However, once these developers gain enough experience in using the design pattern, they are likely to start differentiating products by adding different functions to the existing design pattern, thus creating new variants of existing products in the same functional category (Levinthal and March 1993, Baldwin and Clark 2006). Therefore, in a brand-new functional category, the effect of external APIs in the regular core on the product variety is likely to be suppressed.

Hypothesis 3 (External APIs in a New Functional Category and Product Variety). The effect of external APIs in the regular core on product variety of a newly emerged product functional category is weaker than that of an existing product functional category.

## 5. Empirical Study 5.1. Data

We downloaded more than 100 GB of source code of all plug-ins written primarily on PHP script and MySQL in text files from WordPress (https://wordpress.org/ plugins/). The data covers from January 2004 with 86 plug-ins to December 2014 with 23,218 plug-ins. To identify API use in plug-ins, we use a text-mining program in Java that automatically captures the “function calls” of all internal and external APIs used in all versions of plug-in source codes. We collected detailed API information, such as name, function calls, and dependencies, from two different websites through an automated data extraction process. For internal APIs, we used the Word-Press website. For external APIs, we used the Programmable Web (www.programmableweb.com), a website that, as of September 2020, maintains a directory of more than 23,000 web APIs and mash-ups. From the function calls, we are able to learn the functions each API has. From the dependencies, we are able to learn what other APIs are used together with the current API. In January 2004, there were 40 internal APIs and four external APIs. In December 2014, there were 99 internal APIs and 344 external APIs. From the WordPress website, we extracted other available data about the age and the number of functional updates for each plug-in from the log files, including plug-in creation time, plug-in update, and the number of developers working on each plug-in.

## 5.2. Measuring Product Variety

We use TOM to measure product variety. First, from our monthly data set showing which plug-ins use which APIs, we construct a product network represented by adjacency matrix $\mathbf { P } _ { t } .$ . Then, we convert $\mathbf { P } _ { t } ^ { \phantom { \dagger } }$ into $\mathbf { } { \mathbf { } } { \mathbf { } } \mathbf { W } _ { t } ,$ the TOM that represents the plug-in network in each month, to explore how the underlying recombination pattern of plug-ins and their APIs changed over time. We then build a similarity matrix of plug-ins, $\mathbf { S } _ { t } .$ , for each month. Consider, for example, one time period of our data that includes 443 APIs, both internal and external, and 23,218 plug-ins. Thus, the similarity matrix $\mathbf { S } _ { t }$ has a size of $\bar { 2 } 3 , \bar { 2 1 } 8 \ \times \ 2 3 , 2 1 8$ . It was then transformed into an adjacency matrix $\mathbf { A } _ { t } ,$ whose entry $a _ { i j }$ is a power adjacency function of $s _ { i j } ,$ that is, $a _ { i j } = \lvert s _ { i j } \rvert ^ { \beta }$ . The purpose of matrix $\mathbf { A } _ { t }$ is to suppress low similarity.

Next, we build $\mathbf { W } _ { t }$ for each month. The entries of $\mathbf { W } _ { t }$ are metrics that quantitatively measure the normalized similarity of combinatorial patterns $( \mathrm { i . e . , }$ edge weights) and, hence, can be used to identify the underlying nested functional categories using hierarchical clustering. The clusters reveal that (1) each cluster represents a functional category of plug-ins; (2) within each category, there are subcategories consisting of plug-ins having similar functions; and (3) plug-ins displaying high edge weights are constructed by certain consistent recombination patterns of APIs in each category. When product variety in a functional category increases, it results in the creation of more statistically meaningful subcategories; hence, more subclusters are formed (Ravasz et al. 2002, Clauset et al. 2004). To help us identify the ideal number of functional categories, $\hat { k } ,$ we use a step-wise method using an elbow plot (Aggarwal and Reddy 2014). Thus, we use the number of subclusters identified by hierarchical clustering to measure the product variety in each functional category.

Figure 3. (Color online) The Evolution of a Plug-in Network Using Topological Overlap Plots  
![](/api/attachments/ADHBP92X/fulltext/images/4c6a24a697cf1d2ed46cb60e737ed36e12bba1716ebac14d56c58d99d3e41d84.jpg)  
(a) 86 plug-ins in Jan 2004

![](/api/attachments/ADHBP92X/fulltext/images/108418d806c9f916b76324001b6ade1697ed38ed71877ce08a7b9b6723b7cac0.jpg)  
(b)143 plug-ins in Dec 2006

![](/api/attachments/ADHBP92X/fulltext/images/05ce88ded54704b33d5be28418f21086c6bc1bbd7a6863076b8121eae6d1602f.jpg)  
(c)4,770 plug-ins in Dec 2010

![](/api/attachments/ADHBP92X/fulltext/images/8f7016cf5994d9a207604550f8744953c749d04740294ee37e5a12485699f4eb.jpg)  
(d) 23,218 plug-ins in Dec 2014  
Notes. (a) Eighty-six plug-ins in January 2004. (b) One hundred forty-three plug-ins in December 2006. (c) Four thousand, seven hundred seventy plug-ins in December 2010. (d) Twenty-three thousand, two hundred eighteen plug-ins in December 2014.

Figure 3 shows the evolution of a plug-in network from one functional category in 2004 to 11 functional categories in 2014. The red blocks represent functional categories identified by our hierarchical clustering method. For the details of the design and implementation for the method, please refer to Appendix B.1. The descriptive statistics for each functional category and APIs used can be seen in Tables B.1–B.3.

## 5.3. Identifying Layers of APIs

Our theory suggests that we can categorize APIs in the WordPress ecosystem into three layers: complete core, regular core, and periphery. To identify different layers of APIs, we build an API network for each month as represented by adjacency matrix $\Gamma _ { t } .$ . For each $\Gamma _ { t } ,$ we conduct a generalized block modeling to identify the three layers of complete core, regular core, and periphery, using the following steps.

Step 1. Detecting the complete core: The complete core consists of APIs that are used globally by all plug-ins so that any two APIs have been used together at least once. Thus, the complete core is a perfect 1-block. The condition for determining APIs in the complete core is

$$
\rho = c o r r (\boldsymbol {\Gamma} _ {c c}, \boldsymbol {\Delta} _ {1}) = 1.
$$

Matrix $\Gamma _ { c c }$ is the block representing the complete core. $\mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta }$ is a pattern matrix, in this case, an all-1 matrix. $\rho$ is the Pearson correlation between matrix $\Gamma _ { c c }$ and $\mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta }$ . If the correlation is one, $\Gamma _ { c c }$ is a perfect all-one matrix. Hence, all the nodes (APIs) in $\bar { \Gamma } _ { c c }$ comprise the complete core.

Step 2. Detecting the regular core: The regular core consists of APIs that are frequently used together by some of the plug-ins. The majority of them have been used together at least once. Therefore, the regular core is an imperfect 1-block:

$$
\rho = c o r r (\mathbf {\Gamma} _ {r c}, \mathbf {\Delta} _ {1}) \in [ 0. 8, 1).
$$

Matrix $\mathbf { \Gamma } _ { \mathbf { r } c }$ is the block representing the regular core. $\mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta }$ is still the all-one pattern matrix. $\rho$ is the correla tion between matrix $\Gamma _ { r c }$ and $\mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta } \mathbf { \Delta }$ . We consider a correlation of 0.8 to be a strong fit with an ideal all-one matrix. We varied correlation values and found that the results are consistent. If the correlation in the interval is greater than or equal to 0.8 and less than one, $\Gamma _ { r c }$ is a very dense matrix. All the nodes (APIs) belonging to this group are members of the regular core.

Step 3. Detecting the periphery: The periphery consists of APIs that are used to build the unique functions of each plug-in. They have never, or nearly never, been used together. Thus, the periphery is an imperfect 0-block in which the majority of the entries are zeros. The condition for determining the periphery is

$$
\rho = \operatorname{corr} \left(\boldsymbol {\Gamma} _ {p}, \boldsymbol {\Delta} _ {0}\right) \in [ 0. 7, 1 ].
$$

Matrix $\Gamma _ { p }$ is the block representing the periphery. $\Delta _ { 0 }$ is the pattern matrix with all zero entries. $\rho$ is the correlation between matrix $\Gamma _ { p }$ and $\Delta _ { 0 }$ . We consider a correlation of $0 . 7$ to be a strong fit with an ideal allzero matrix. We used different correlation values and found that the results are consistent. If the correlation in the interval is greater than or equal to 0.7 and less than or equal to one, $\Gamma _ { p }$ is a very sparse matrix. All nodes (APIs) belonging to this group are members of the periphery.

## 5.4. Hypotheses Testing

With Hypothesis 1, we theorize that an ecosystem starts with a two-layered structure with a core and periphery and evolves into a three-layer structure with a complete core, regular core, and periphery as it grows in size and complexity. Because Hypothesis 1 predicts the emergence of a third layer as the ecosystem grows in size and complexity, we have to decide the inflection point for WordPress. In this study, we define January 2008 as the cutoff point that separates the early and later stages. We made the choice because many widely used platforms, such as iPhone OS (rebranded as iOS in 2010), Hadoop, GitHub, Twitter, Android Beta, Airbnb, etc., that led to the increase of numerous APIs across platform ecosystems were started in 2007 (Friedman 2017). As a result, the number of internal APIs in the Word-Press ecosystem increased only by 31%, whereas the number of external APIs increased by whopping 442% for 1,052 plug-ins over a single year between 2007 and 2008 (see Table B.1).

Table 2. Results of ANOVA

<table><tr><td>Time period</td><td>F-test for two-layer</td><td>F-test for three layer</td><td>T-test</td><td></td></tr><tr><td>2004–2007</td><td>146.77</td><td>41.41</td><td> $H_0:F_1 < F_2$ </td><td>3.64**</td></tr><tr><td>2008–2014</td><td>280.37</td><td>378.40</td><td> $H_0:F_1 > F_2$ </td><td>2.73**</td></tr></table>

\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

To test Hypothesis 1, we first use the percentage of $^ { \prime \prime } { 1 ^ { \prime \prime } }$ entries $( \gamma _ { i j } = 1 )$ in each block to empirically evaluate the existence of different layers of APIs according to their use frequencies. The $^ { \prime \prime } { 1 ^ { \prime \prime } }$ entry percentage is the ratio between the number of entries of one and the total number of entries in the block and represents the ratio of APIs used together to build plug-ins to the total number of APIs in the layer. For each $\bar { \mathbf { I } } _ { t } ,$ we calculate the percentage of entries of $^ { \prime \prime } { 1 ^ { \prime \prime } }$ for each block. Then we compare the groups of APIs in terms of $^ { \prime \prime } { 1 ^ { \prime \prime } }$ entry percentages that are calculated across all months. If the difference between the two or three groups of percentages is significant, we are able to conclude that distinct layers exist in the platform ecosystem. The series of the first order differences do not show obvious autocorrelation patterns that affect the change of trend at the 5% significance level. Specifically, we conduct this test in two steps.

First, we fit the model as a two-layer structure. We run repeated-measures ANOVA in both time periods, 2004 to 2007 $( F _ { 1 , 4 9 } = 1 4 6 . 7 7 , p < 0 . 0 1 )$ and 2008 to 2014 $( F _ { 1 , 8 1 } =$ 280.37, $p < 0 . 0 5 )$ . Second, we run ANOVA again to test a three-layer structure in the same time periods, that ${ \mathrm { i s } } ,$ 2004 to 2007 $( F _ { 2 , 4 9 } = 4 1 . 4 1 , p < 0 . 0 5 )$ and 2008 to 2014 $( F _ { 2 , 8 1 }$ $= 3 7 8 . 4 0 , p < 0 . 0 1 )$ . From the comparison of the F-values, we find that an ecosystem has a more significant threelayer structure to categorize APIs in the later stage. In addition, a t-test comparing the F-values from ANOVA tests of each structure in the same time periods shows that, from 2004 to 2007, a two-layer structure is more significant than a three-layer structure, whereas from 2008 to 2014, a three-layer structure is more significant than a two-layer structure. Therefore, Hypothesis 1 is supported (Table 2). For the composition of the three layers and the examples of external APIs in the regular core and periph ery, please refer to Appendix B.3.

To test Hypotheses 2 and $^ { 3 , }$ we use an econometric model with the data generated from our network models. The unit of analysis of our econometric analysis is the functional category of digital products to explore the statistically meaningful pattern of changes. For each functional category, our response variable $Y _ { i t }$ is product variety and is measured by the number of subcategories within category i in a given month t. A subcategory is represented by a subcluster, which is a group of plug-ins sharing a more similar set of APIs than other plug-ins within the category (MacCormack et al. 2006). When a functional category contains a large number of subcategories, it has a high degree of product variety (Ethiraj and Levinthal 2004, Boudreau 2012).

Our main explanatory variables are the percentage of external APIs among regular core APIs in each func tional category and an indicator of whether the category is newly formed. We use measures from month t � 1 because it takes some time to build plug-ins, so we assume that the plug-ins existing in t are built with the APIs that exist at time � 1. Following this assumption, our independent variables are

1. $E X T R _ { i , t - }$ <sub>�1</sub> (external API ratio in regular core), the percentage of external APIs in the regular core of category i in month t � 1.

2. $N F C _ { i , t - }$ <sub>�</sub> (new functional category), which indicates whether category i is newly formed in month t � 1.

We control for variables that can potentially affect product variety. As with our explanatory variables, we use lags in our control variables too. We include the following control variables:

1. $C C _ { i , t - 1 }$ (complete core API number) denotes the number of APIs in the complete core in month t � 1. It is the total number of the APIs in the complete core in that month used by all the plug-ins.

2. $R C _ { i , t - 1 }$ (regular core API number) denotes the number of APIs in the regular core of category i in month t � 1. It is the total number of the APIs in the regular core in that month used by all the plug-ins.

3. $P E R _ { i , t - 1 }$ (periphery API number) is the number of APIs in the periphery of category i in month t � 1. It is the total number of the APIs in the periphery in that month used by all the plug-ins.

4. $D P P _ { i , t - 1 }$ (developers per plug-in) denotes the average number of developers per plug-in in category i and month t � 1. This variable captures the popularity of a functional category among developers by measuring the average number of developers who contribute to it.

5. $V U _ { i , t - 1 }$ (version upgrade) measures the number of plug-in version upgrades made in category i and in month t � 1. This variable indicates how many times plug-ins are updated

6. $P A G _ { i , t - }$ <sub>�1</sub> (plug-in age) is the average age of plugins in category i in month t � 1.

The descriptive statistics for the variables are provided in Table 3. We use the variance inflation factors (VIF) to ensure that multicollinearity does not pose a concern in our data; all the VIF values are within the acceptable threshold (Belsley et al. 2005). The detailed correlation table for all variables is provided in Appendix C.1.

The main model we estimate as follows:

$$
\begin{array}{r l} & {\log (Y _ {i t}) = \beta_ {0} + \beta_ {1} E X T R _ {i, t - 1} + \beta_ {2} E X T R _ {i, t - 1} \cdot N F C _ {i, t - 1}} \\ & {\qquad + \beta_ {3} N F C _ {i, t - 1} + \beta_ {4} C C _ {i, t - 1} + \beta_ {5} R C _ {i, t - 1}} \\ & {\qquad + \beta_ {6} P E R _ {i, t - 1} + \beta_ {7} D P P _ {i, t - 1} + \beta_ {8} V U _ {i, t - 1}} \\ & {\qquad + \beta_ {9} P A G _ {i, t - 1} + \varepsilon .} \end{array}\tag{1}
$$

We use different specifications to estimate our model coefficients as shown in Table 4.

In our first model, we only include independent variables (column (1), Table 4). Next, we add control variables to our model (column (2), Table 4). The $R ^ { 2 }$ increases from 0.346 to 0.724, suggesting an increase in the explanatory power of our model after adding the control variables. We test Hypothesis 2 using the external API ratio.

The coefficient of $E X T R _ { i , t - 1 }$ is positive and significant at the 0.01 level, showing that the external API ratio in the regular core has a positive effect on product variety, supporting Hypothesis 2.

Finally, we test Hypothesis 3 using an interaction term of category formation and the external API ratio. The coefficient of the interaction term is negative and significant, showing that the effect of the number of external APIs is weakened in the new category formed. We then draw a two-dimensional plot of the marginal interaction effect between $\mathrm { E X T } { R _ { i , t - 1 } }$ and $\boldsymbol { N F C } _ { i , t - 1 }$ on product variety (see Figure 4). The Y-axis indicates the predicted marginal effect on product variety. The Xaxis represents the external API ratio, for which we classify the ratio of external APIs from zero (no external API exists) to one (all APIs are external) depending on whether a category is newly formed in the last time period (indicated by one); otherwise, it is set to zero. The plot shows that, in a newly formed functional category, the effect of the external API ratio decreases. For a detailed marginal effect table, please refer to Appendix C.2.

In addition to the theorized hypotheses, we also explore different roles of three layers on product variety. As expected, the coefficient of $R C _ { i , t - 1 }$ is positive and significant at the 0.01 level. This suggests that the size of the regular core positively affects the product variety. This is consistent with our theoretical expectation that the regular core layer plays a crucial role in creating product variety in an ecosystem. At the same time, the coefficient of the $C C _ { i , t - 1 }$ variable is negative and sig nificant at the 0.01 level in column (2), which suggests that the size of the complete core negatively affects the product variety. This suggests that having a large

Table 3. Descriptive Statistics of the Econometric Model

<table><tr><td>Variable</td><td>Variable description</td><td>Variable</td><td>Mean</td><td>Standard deviation</td><td>Minimum</td><td>Maximum</td></tr><tr><td> $\log(Y_{it})$ </td><td>Log (number of subcategories in each cluster i at time t)</td><td>Dependent</td><td>2.03</td><td>0.525</td><td>0.69</td><td>3.37</td></tr><tr><td> $EXTR_{i,t-1}$ </td><td>External API percentage in the regular core in category i at time t - 1</td><td>Independent</td><td>0.06</td><td>0.077</td><td>0</td><td>0.36</td></tr><tr><td> $NFC_{i,t-1}$ </td><td>Whether a category i is newly formed at time t - 1</td><td>Independent</td><td>0.5</td><td>0.501</td><td>0</td><td>1</td></tr><tr><td> $CC_{i,t-1}$ </td><td>Total number of APIs in complete core in category i at time t - 1</td><td>Control</td><td>7.01</td><td>2.108</td><td>4</td><td>12</td></tr><tr><td> $RC_{i,t-1}$ </td><td>Total number of APIs in regular core API in category i at time t - 1</td><td>Control</td><td>27.92</td><td>24.736</td><td>1</td><td>119</td></tr><tr><td> $PER_{i,t-1}$ </td><td>Total number of periphery APIs of a category i at time t - 1</td><td>Control</td><td>80.83</td><td>37.065</td><td>9</td><td>152</td></tr><tr><td> $DPP_{i,t-1}$ </td><td>Number of developers per plug-in in the category i at time t - 1</td><td>Control</td><td>0.56</td><td>0.052</td><td>0.45</td><td>0.73</td></tr><tr><td> $VU_{i,t-1}$ </td><td>Average number of version upgrade of plug-ins in the category i at time t - 1</td><td>Control</td><td>54.87</td><td>47.675</td><td>0</td><td>429</td></tr><tr><td> $PAG_{i,t-1}$ </td><td>Average age of plug-ins in the category i at time t - 1</td><td>Control</td><td>59.55</td><td>28.591</td><td>14.05</td><td>133.09</td></tr></table>

Table 4. Results of the Econometric Model

<table><tr><td>DV:  $\log(Y_{it})$ </td><td>Panel OLS (without controls)</td><td>Panel OLS (with controls)</td></tr><tr><td> $EXTR_{i,t-1}$ </td><td>4.194***(0.446)</td><td>1.274***(0.351)</td></tr><tr><td> $EXTR_{i,t-1} \times NFC_{i,t-1}$ </td><td>-2.324***(0.572)</td><td>-1.906***(0.387)</td></tr><tr><td> $NFC_{i,t-1}$ </td><td>0.448***(0.052)</td><td>0.250***(0.037)</td></tr><tr><td> $CC_{i,t-1}$ </td><td>—</td><td>-0.055***(0.011)</td></tr><tr><td> $RC_{i,t-1}$ </td><td>—</td><td>0.010***(0.001)</td></tr><tr><td> $PER_{i,t-1}$ </td><td>—</td><td>0.001(0.001)</td></tr><tr><td> $DPP_{i,t-1}$ </td><td>—</td><td>0.034(0.133)</td></tr><tr><td> $VU_{i,t-1}$ </td><td>—</td><td>0.001*(0.0004)</td></tr><tr><td> $PAG_{i,t-1}$ </td><td>—</td><td>-0.010***(0.001)</td></tr><tr><td>Constant</td><td>1.663***(0.033)</td><td>2.367***(0.225)</td></tr><tr><td>Observation</td><td>422</td><td>422</td></tr><tr><td>Number of groups</td><td>11</td><td>11</td></tr><tr><td> $R^2$ </td><td>0.346</td><td>0.724</td></tr><tr><td>Category fixed effects</td><td>No</td><td>No</td></tr><tr><td>Time fixed effects</td><td>No</td><td>No</td></tr><tr><td>Control variables</td><td>No</td><td>Yes</td></tr><tr><td>Robust standard error</td><td>No</td><td>No</td></tr></table>

\*p < 0.1, \*\*p < 0.05, \*\*\*p < 0.01.

complete core, including internal APIs, decreases the product variety of a functional category. This is consistent with the past findings that show a tighter control by the platform owner dampens the innovation by third-party developers as a large complete core layer can imply tighter control by the platform owner (Eaton et al. 2015). Finally, the coefficient of $P E R _ { i , t - 1 }$ shows insignificance. This suggests that the size of the periphery does not affect the product variety. This suggests that most use of APIs in the periphery layer leads to imitations and minor differentiations within existing product categories.

Figure 4. (Color online) Marginal Effect of External API Ratio and Category Formation  
![](/api/attachments/ADHBP92X/fulltext/images/720fa975952cb9e0bc168bba0851a319c2ab8106564468b2f542db7d05f78104.jpg)

## 5.5. Robustness Checks

To confirm the robustness of our results, we first estimate the validity of measuring product variety. In particular, to validate if the functional categories built by our hierarchical clustering method using TOM are pairwise orthogonal to each other, we mathematically test the orthogonality between any two functional categories (Papoulis and Saunders 1989) represented by plug-in vectors. For the detailed test methods, please refer to Appendix B.2. We empirically test the degree to which functional categories are orthogonal. The test results confirm that all these functional cate gories are orthogonal.

To validate our measure for the response variable, we generate lists of the functional categories and the numbers of subcategories within each category of plugins constructed by the textual descriptions and of tags of plug-ins using two methods: one from topic modeling (Latent Dirichlet Allocation (LDA); Gong et al. 2018) and the other from word embedding (Doc2Vec; Qiao et al. 2020). We run two chi-squared tests: one compares the functional categories extracted by hierarchical clustering (which is the measure of our response variable) and those extracted by LDA, and the other compares the categories extracted by hierarchical clustering and those extracted by Doc2Vec. The results from both tests show that the functional categories extracted by the three methods are the same $( p < 0 . 0 0 1 )$ Therefore, we conclude that our current measure for our response variable is robust. For the details of our LDA and Doc2Vec results, please refer to Appendices B.3 and B.4, respectively.

After confirming the measurement validity of our response variable, we run a standard panel ordinary least squares (OLS) model with robust standard errors and show the results in column (2) of Table 5. A Breusch– Pagan test shows that the test of heteroskedasticity has a p-value of 0.0982. So we reject the null hypothesis and conclude that we do not have a heteroskedasticity prob lem. We also perform a series of robustness checks to address the potential issue of endogeneity that can drive biased, inconsistent parameter estimates. To control for category- and time-invariant unobserved heterogeneity, we use category- and time-specific fixed effects. Our results for the model with fixed effects are shown in column (2) of Table 5. They are qualitatively unchanged, suggesting that category- and time-invariant unobserved heterogeneity is not a concern in our data. We examine the overall effect of all external APIs on product variety and control for external APIs in the regular core. The estimation results are shown in Table C.3. The coefficient of all external APIs is insignificant, whereas that of external

Table 5. Robustness Test Results

<table><tr><td>DV:  $\log(Y_{it})$ </td><td>Panel OLS (robust standard error)</td><td>Panel OLS (time and category fixed effects)</td></tr><tr><td> $EXTR_{i,t-1}$ </td><td>1.274***(0.453)</td><td>0.653*(0.357)</td></tr><tr><td> $EXTR_{i,t-1} \times NFC_{i,t-1}$ </td><td>-1.906***(0.464)</td><td>-1.587***(0.375)</td></tr><tr><td> $NFC_{i,t-1}$ </td><td>0.250***(0.074)</td><td>0.204***(0.040)</td></tr><tr><td> $CC_{i,t-1}$ </td><td>-0.055***(0.017)</td><td>0.086(0.061)</td></tr><tr><td> $RC_{i,t-1}$ </td><td>0.010***(0.002)</td><td>0.009***(0.002)</td></tr><tr><td> $PER_{i,t-1}$ </td><td>0.002(0.002)</td><td>0.0003(0.001)</td></tr><tr><td> $DPP_{i,t-1}$ </td><td>0.034(0.247)</td><td>0.043(0.170)</td></tr><tr><td> $VU_{i,t-1}$ </td><td>0.001(0.001)</td><td>0.0001(0.001)</td></tr><tr><td> $PAG_{i,t-1}$ </td><td>-0.010**(0.004)</td><td>-0.008*(0.004)</td></tr><tr><td>Constant</td><td>2.367***(0.341)</td><td>0.943(0.980)</td></tr><tr><td>Observation</td><td>422</td><td>422</td></tr><tr><td>Number of groups</td><td>11</td><td>11</td></tr><tr><td> $R^2$ </td><td>0.724</td><td>0.798</td></tr><tr><td>Category fixed effects</td><td>No</td><td>Yes</td></tr><tr><td>Time fixed effects</td><td>No</td><td>Yes</td></tr><tr><td>Control variables</td><td>Yes</td><td>Yes</td></tr><tr><td>Robust standard error</td><td>Yes</td><td>No</td></tr></table>

\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

APIs in the regular core is still positive and significant $( p < 0 . 0 1 )$ . Thus, because of the insignificant effect of all external APIs, we decide not to include it in our fina model.

We additionally examine the effect of external APIs in different categories. In newly emerged categories, the results show that the effect of external APIs is lower. The moderating effect of new formation status of category is significantly negative. For the details, please refer to Table C.4. Next, we use the Ramsey RESET test (Ramsey 1969) to check if the functional form of the model is linear. The p-value of the time- and category-fixed effects model is 0.375. Thus, we conclude that nonlinear functions of the independent variables have no significant explanatory power, our model is properly specified.

In addition, we control for the possible autocorrelation in frequently used external APIs resulting from selection bias. Specifically, in our data, it is possible that some external APIs are considered more useful by developers and are more likely to be chosen for creating products, ceteris paribus. Thus, we implement a quasi-experimental design approach in our analysis framework to control the unobserved external API design choices, which should be time-invariant. We use a difference-in-difference (DID) model to compare the product variety affected by external APIs in the regular core (the treatment group) and external APIs not in the regular core (the control group) by resplitting the origi nal data set into two periods (Acemoglu et al. 2004, Bertrand et al. 2004, Mousavi and Gu 2019, Rishika and Ramaprasad 2019). We define the treatment date as January 2008 because various external APIs provided by various newly launched platform ecosystems $( \mathrm { e . g . } ,$ Twitter) in 2007 (Friedman 2017) started to be in Word-Press in 2008. In WordPress, the number of external APIs surges from seven in December 2007 to 38 in December 2008 and 70 in December 2009, whereas the number of internal APIs changes from 45 in December 2007 to 59 in December 2008 and 67 in December 2009.

Furthermore, we apply propensity score matching to our DID model to ensure the covariates have similar distributions between the control and treatment groups (Imbens 2000). We use both nearest neighbor and caliper matching to match the participants in the control and treatment groups (Foerderer 2020).

Our DID results are shown in Table 6. The first col umn shows the average treatment effect—the frequently used external APIs (those in the regular core)—can increase product variety by 31% compared with the rest of the external APIs (those in the periphery). The second column shows that the effect of frequently used external

Table 6. DID Estimation

<table><tr><td>DV:  $\log(Y_{it})$ </td><td>DID model I</td><td>DID model II</td></tr><tr><td> $DID_{i,t-1}$ </td><td>0.646***(0.047)</td><td>0.438**(0.112)</td></tr><tr><td> $EXTR_{i,t-1}$ </td><td>—</td><td>0.958**(0.398)</td></tr><tr><td> $EXTR_{i,t-1} \times NFC_{i,t-1}$ </td><td>—</td><td>-1.141**(0.556)</td></tr><tr><td> $NFC_{i,t-1}$ </td><td>—</td><td>0.210**(0.099)</td></tr><tr><td> $CC_{i,t-1}$ </td><td>—</td><td>0.108**(0.054)</td></tr><tr><td> $RC_{i,t-1}$ </td><td>—</td><td>0.004**(0.002)</td></tr><tr><td> $PER_{i,t-1}$ </td><td>—</td><td>-0.002(0.003)</td></tr><tr><td> $DPP_{i,t-1}$ </td><td>—</td><td>-0.224***(0.727)</td></tr><tr><td> $VU_{i,t-1}$ </td><td>—</td><td>-0.001(0.001)</td></tr><tr><td> $PAG_{i,t-1}$ </td><td>—</td><td>0.014*(0.008)</td></tr><tr><td>Constant</td><td>2.0551***(0.046)</td><td>3.010***(0.766)</td></tr><tr><td>Observation</td><td>154</td><td>154</td></tr><tr><td>Number of groups</td><td>11</td><td>11</td></tr><tr><td> $R^{2}$ </td><td>0.953</td><td>0.969</td></tr><tr><td>Category fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Time fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Control variables</td><td>Yes</td><td>Yes</td></tr><tr><td>Robust standard error</td><td>Yes</td><td>Yes</td></tr></table>

\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

APIs (in the regular core) has a 43.8% higher effect on increasing product variety than the rest of the external APIs with all the explanatory variables added. The second column shows that the size and significance of the coefficients of our explanatory variables are very similar to our original model. Thus, we conclude that our original results are robust.

Finally, to control for possible reverse causality, we use a generalized method of moments (GMM) model. For example, in our data, it is likely that functional categories with high product variety are more likely to form new categories than others because functional categories with high product variety are highly likely to have many subcategories. As new products keep being added to the categories, some subcategories keep expanding and eventually become categories themselves because of their size. The GMM model can control the potential endogeneity coming from the time-invariant unobserved heterogeneity and simultaneity that lead to biased and inconsistent estimates (Arellano and Bover 1995, Blundell and Bond 1998). The critical aspect of the GMM model is to use the lagged product variety (t � 2) as an instrumental variable to control the endogeneity of API use frequencies. In other words, we use the second order lagged dependent variable as an instrument for our explanatory variables by assuming that these higher order lagged variables are uncorrelated with the error term.

We examine the validity of the exogeneity assumptions of GMM using a series of empirical tests to estimate that there is no serial correlation in the error term. We conduct the Arellano–Bond test for the issue of autocorrelation with our instruments (Arellano and Bond 1991). The AR(1) process in the first difference rejects the null hypothesis at the 1% significance level, whereas the AR(2) process in the first difference does not reject the null hypothesis with $p = 0 . 5 6 3$ . The Durbin–Wu–Hausman test is used to check for endogeneity in our data (Greene 2003). The Sargan–Hansen test of overidentifying restrictions for the instrument variables (Hansen 1982) is strongly rejected with $\chi ^ { 2 } = 3 6 1 . 2 9 ~ ( p = 0 . 8 2 2 )$ . The overidentification test yields a $\chi ^ { 2 }$ distribution under the null hypothesis of instrument validity. The test results support the assumption that there is no serial correlation in the error term. Hence, from the test results, the orthogonality condition of the original model $\left( \epsilon _ { i , t - 1 } | y _ { t } , \ x _ { i , t - 1 } \right) = 0$ means that the lagged levels (t � 2) can be used as the proper specification of the instrument at the conventional level to control for the dynamic aspects of our empirical model. Our analysis (shown in Table 7) shows that the result is qualitatively consistent with our prior results and our hypotheses hold.

## 6. Discussion

How does a digital platform ecosystem grow in its product variety? Our study shows APIs, particularly certain

Table 7. GMM Estimation

<table><tr><td>DV:log(Yit)</td><td>GMM</td></tr><tr><td> $HIER_{i,t-1}$ </td><td>0.819***(0.033)</td></tr><tr><td> $EXTR_{i,t-1}$ </td><td>0.466**(0.227)</td></tr><tr><td> $EXTR_{i,t-1} \times NFC_{i,t-1}$ </td><td>-0.600**(0.256)</td></tr><tr><td> $NFC_{i,t-1}$ </td><td>0.064***(0.025)</td></tr><tr><td> $CC_{i,t-1}$ </td><td>-0.012*(0.007)</td></tr><tr><td> $RC_{i,t-1}$ </td><td>0.002***(0.001)</td></tr><tr><td> $PER_{i,t-1}$ </td><td>-0.001(0.002)</td></tr><tr><td> $DPP_{i,t-1}$ </td><td>-0.309(0.271)</td></tr><tr><td> $VU_{i,t-1}$ </td><td>-0.0001(0.0003)</td></tr><tr><td> $PAG_{i,t-1}$ </td><td>-0.004***(0.001)</td></tr><tr><td>Constant</td><td>0.855***(0.240)</td></tr><tr><td>Observation</td><td>422</td></tr><tr><td>Number of groups</td><td>11</td></tr><tr><td>F-test</td><td>278.73</td></tr><tr><td>Category fixed effects</td><td>No</td></tr><tr><td>Time fixed effects</td><td>No</td></tr><tr><td>Control variables</td><td>Yes</td></tr><tr><td>Robust standard error</td><td>No</td></tr></table>

\*p < 0.1, \*\*p < 0.05, \*\*\*p < 0.01.  
external APIs, play a crucial role. Our study makes several theoretical and methodological contributions.

## 6.1. Theoretical Contributions

Our study offers a few new insights for IS scholars regarding innovation and product variety in digital platform ecosystems. First, we show a multilayer structure in a platform ecosystem with three distinct layers of complete core, regular core, and periphery in a mature ecosystem. Figure 5 shows a conceptual representation of the three-layer structure. Particularly, we are the first to report the presence of the regular core. Past studies conceptualize a platform ecosystem as a two-layer structure that consists of a core and a periphery (Baldwin and Clark 2000, Murmann and Frenken 2006). In this view, product variety comes from the mix and match of APIs in the periphery. Our study expands this existing view and suggests the existence of an additional layer of the regular core that is distinct from the other two layers. Furthermore, we show that the APIs in the regular core play a substantial role on product variety at an ecosystem level. Most importantly, external APIs in the regular core, not the external APIs in the periphery nor the internal APIs in the complete core, are used frequently and encourage product variety.

Figure 5. A Multilayer Structure for API Use Frequency of Platform Ecosystem  
![](/api/attachments/ADHBP92X/fulltext/images/2730dc5888955f059c93c68d4c3cc78250908b19c95a3bdee709eaa75f458d2c.jpg)

Second, one of the key assumptions in the platform literature is that the success of an ecosystem depends on its product variety (Yoo et al. 2010, Tiwana 2018). Existing literature only concentrates on how platform owners can cultivate product variety and maintain control by using the internal APIs (Eaton et al. 2015, Foerderer et al. 2018). Our study adds value to this stream by switching the focus to the role of external APIs and quantifying their effect on product variety in platform ecosystems. Our work is one of the first studies to design a measure for product variety using source code data of various digital products (plug-ins) and creating a network structure based on various APIs used in the plug-ins. We also show how external APIs and their use frequencies have a different impact on product variety in such an ecosystem.

Third, we show an important, yet nuanced, role of external APIs in increasing the product variety in a platform ecosystem. A platform owner cannot achieve a high degree of product variety without the help of external APIs. It is the external APIs that attract many developers who build various plug-ins, increasing the product variety. At the same time, a platform owner must be aware that the mere supply of new external APIs does not necessarily increase the product variety in the ecosystem. If the combinatorial product designs overly depend on a few popular APIs, product variety is weakened because of duplicated product designs. The combinatorial designs would be simplified, resulting in many products with similar functions. If platform owners want to attract and satisfy all kinds of software requirements for users, they must offer a wide selection of products. To do so, they must continue to offer competing external APIs to join the ecosystem.

Finally, even though a large number of digital prod ucts in an ecosystem suggests vibrant and generative innovation activities in a platform ecosystem, we show that a large number of digital products does not necessarily mean unbounded digital innovations (Yoo et al. 2010) or an infinite variety of products (Caves 2000) as the literature suggests. Despite an exponential growth of the overall size of the ecosystem from 86 to 23,218 plug-ins, the WordPress ecosystem has only 11 functional categories. Therefore, we suggest that the early vision of a generative, unbounded potential of digital platform ecosystems must be modulated.

## 6.2. Methodological Contributions

To our knowledge, ours is the first empirical study of recombinatorial designs of digital products in a platform ecosystem. In fact, until recently, with some notable exceptions, there has been little empirical research that investigates how products are created through the combination of existing components (Fleming 2001). A likely reason for this sparsity in empirical research in this area is that it is really challenging to collect and analyze data about digital products and their composition over an extended period of time at the ecosystem level. As a result, most studies only use computer-based simulations, primarily Kauffman’s NK-landscape (Kauffman 1993), for their conceptual foundation (Levinthal 1997).

To empirically study product variety through recombination in a dynamic complex platform ecosystem, we build a comprehensive methodological framework from data collection to causality identification. The network approach is a superior tool to model design activities in recombinatorial design in which a relationship can happen between APIs, between plug-ins, and between APIs and plug-ins.

Our hierarchical clustering method also resolves the challenge of identifying unobserved product categories. It groups functionally similar products to corresponded categories and is able to identify nested subcategories when more new similar products are added to a category, and eventually, they form subcategories because of the high similarity (Ravasz et al. 2002). Our approach is proven to be useful in analyzing large and complex network contemporary studies (Hawrylycz et al. 2012, Zhang et al. 2013, Rajarajan et al. 2018, Bakken et al. 2021) Our study dynamically traces how plug-ins are created, and for each plug-in, we use a text mining algorithm to track the function calls of all internal and external APIs in that plug-in. We use LDA, a topic modeling method showing the best performance in categorization, to identify unobserved product functional categories at the platform ecosystem level. We also use a deep learning method, Doc2Vec, to validate the robustness of our categorization.

Together with our unique longitudinal data, our methodology overcomes the disadvantage of all existing methods assuming that the ecosystem is static, that both the numbers of software components and functional categories in the ecosystem must be constant and cannot be changed. Our methodology shows a striking example about how the recombination of APIs affects product variety across time.

## 6.4. Implications for Practice

Our results provide implications for practitioners to understand the impacts of external APIs on developers design decisions and how they, in turn, affect product variety through the combinatorial designs of APIs. First, we summarize the principle of software development using combinatorial design for practitioners. We expect developers to increase the efficiency of product design by reducing development cost to make their products more successful. Combined with our view of the three-layer API model, building plug-ins can be modeled as an easy-to-follow three-stage process that recombines APIs from the three layers: complete core, regular core, and periphery. Developers can select internal APIs to build core functions. They can use APIs in the complete core because they define the fundamental functions that all plug-ins must use, such as system interface and back-end administration. Next, they can choose useful internal APIs and particular external APIs from the regular core to build the most useful functions. These APIs define the major functions and determine the functional category in which the plug-in falls. Finally, developers can combine with external APIs to build unique and characteristic functions in a platform ecosystem. These APIs define the unique functions and characteristics of the plug-in. A plug-in is ultimately built by combining the APIs chosen from all three layers.

Second, our research has an interesting but dialectical finding: the effect of external APIs on product variety does not increase monotonically; instead, the effect can be weakened when most of the new products in the same category are built by duplicating the usage of APIs from other products. Thus, our findings suggest that, in order to maintain the increasing rate of product variety, the platform owner should stimulate developers’ creativity by connecting digital product providers and developers so that providers can know about the functional needs of developers and build corresponding APIs in a platform ecosystem.

## 6.5. Limitations and Future Research

There are a number of limitations to our study. First, we study a single ecosystem, WordPress. We could not explore the product design control of a focal firm affected by the use of external APIs. The functional uses of external APIs can indirectly influence a focal platform’s product variety by constructing the multi layered structure regarding their use frequencies.

Second, our study mainly focuses on the role of APIs. In a platform such as WordPress, developers’ diverse ideas and operationalizations are the primary sources of increasing product variety. However, we could not fully explore developers’ product design efforts because of the difficulty of quantifying the functional roles of the developers’ functions. Plug-ins are mainly built by (customized codes are mainly) PHP scripts facilitating (or processing) HTTP data (e.g., HTML). Hence, functions such as callback functions and interfaces created by developers in plug-ins were hard to capture the specific point of unique functional interactions. When studying a platform ecosystem in which developers have more programming freedom, we should incorporate measures of developers’ innovation efforts embedded in thei innovations.

Third, our study mainly looks at the supply side of the ecosystem, that is, developers. However, no platform ecosystem can exist without users. Users act as the primary source of natural selection, whereas the combinatorial digital innovations created by develop ers serve as the primary force for creating variation. Including users in the analysis will help to explain the complete growth of a platform ecosystem. However, we could not directly measure the extent of users’ plugin demand as WordPress does not provide a full set of such data. Future studies must incorporate users into their models and explore how user selection can influence a developer’s decision to choose to mix certain sets of APIs.

Despite these limitations, our study offers other exciting avenues for future research. First, a much deeper investigation of external software component builders and their strategic actions is needed. Future researchers can examine what motivates API creators, what makes certain external APIs more attractive than others, and how APIs evolve over time. Second, from our study it is quite clear that not all external APIs are created equal. Future studies must investigate which API attributes affect their impact on product variety in an ecosystem. Third, we can extend our empirical data to include more recent digital product information. Even though the current data specifically represent the role external APIs play in product variety, more recent empirical data will enable the exploration of more diverse combinatory patterns in a platform ecosystem under varying conditions.

## Acknowledgments

Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the sponsors.

## Appendix A. Mathematical Network Modeling

A.1. Modeling of Product Network in Platform Ecosystem Suppose, at a given time period t, a developer wants to design a product k. Let us denote this product as $P _ { k t }$ . In order to build new product $P _ { k t } ,$ the developer needs to choose an appropriate recombination of APIs among available internal and externa APIs. Internal APIs are offered by the platform owner, such as WordPress. Internal APIs provide functions related to platform interface and administration. External APIs are provided by other web service providers. External APIs are important as the developer might pursue features that were not originally envisioned by the platform owner. Define I as the set of all internal APIs that the platform owner provides and define E as the set of all the external APIs from which a developer can select. Sets I and E are defined as follows and have sizes M and $N ,$ respectively:

$$
\begin{array}{c} {I = \{I _ {1}, \ldots , I _ {M} \}, | I | = M,} \\ {E = \{E _ {1}, \ldots , E _ {N} \}, | E | = N.} \end{array}
$$

Define $\overrightarrow { I _ { k t } }$ as a column vector representing internal APIs that a developer uses to design a product $P _ { k }$ at time t with each component representing an internal API in set I. If an internal API is used to build product $P _ { k } ,$ , its corresponding value in $\overrightarrow { I _ { k t } }$ is set to one; otherwise, the value is set to zero. For example, if the platform owner offers three internal APIs $I _ { 1 } , I _ { 2 } ,$ , and ${ \cal I } _ { 3 } ,$ and a developer uses internal APIs $I _ { 1 }$ and $I _ { 3 }$ but not $\mathrm { A P I } I _ { 2 }$ to build product $P _ { k } ,$ we have vector $\overrightarrow { I _ { k t } } = [ 1 0 1 ] ^ { T }$ . Likewise, define $\overrightarrow { E _ { k t } }$ as a column vector indicating all external APIs that the developer uses in addition to the internal APIs to cre ate product $P _ { k }$ at time t with each component representing one external API. If the API is used in product $P _ { k } ,$ its value is set to one; otherwise, it is set to zero. For example, if there are two available external APIs $E _ { 1 }$ and $E _ { 2 }$ and the developer uses API $E _ { 2 }$ to build product $P _ { k } ,$ , we have vector $\overrightarrow { E _ { k t } } = [ 0 1 ] ^ { T }$ Because the developer designs product $P _ { k }$ using internal and external APIs, we can take the usage of APIs to represent the resulting product. Therefore, we define the resulting product $\overrightarrow { P _ { k t } }$ as a concatenation of column vectors $\overrightarrow { I _ { k t } }$ and $\overrightarrow { E _ { k t } }$ or $\overrightarrow { P _ { k t } } = \overrightarrow { I _ { k t } } \overrightarrow { E _ { k t } }$ . Using the previous examples for $\overrightarrow { I _ { k t } }$ and $\overrightarrow { E _ { k t } }$ product $P _ { k }$ designed with internal APIs $I _ { 1 }$ and $I _ { 3 }$ and external API $E _ { 2 }$ is presented as $\overrightarrow { P _ { k t } } \ = \overrightarrow { I _ { k t } } \overrightarrow { E _ { k t } } \ = [ 1 0 1 0 1 ] ^ { T }$ . Ultimately, the total number of products built in $t , \overrightarrow { P _ { 1 t } } , \overrightarrow { P _ { 2 t } } , \dots , \overrightarrow { P _ { K t } } , \mathrm { i s } \ K ,$ that is, $1 \leq k \leq K .$ . The internal APIs provided by the platform owner to support developers to design products $\overrightarrow { P _ { 1 t } } , \dots , \overrightarrow { P _ { K t } }$ at time t can be represented as a matrix $\mathbf { I } _ { t } ,$ in which each column vector, $\overrightarrow { I _ { k t } }$ , as defined in the previous paragraph, represents the usage of internal APIs by a product $P _ { k }$

For example, let us assume that there are four products $( \overrightarrow { P _ { 1 t } } , \overrightarrow { P _ { 2 t } } , \overrightarrow { P _ { 3 t } }$ , and $\overrightarrow { P _ { 4 t } } )$ , four internal APIs $( I _ { 1 } , I _ { 2 } , I _ { 3 } ,$ , and $I _ { 4 } )$ and two external APIs $( E _ { 1 }$ and $E _ { 2 } )$ . Product $P _ { 1 t }$ contains internal APIs $I _ { 1 }$ and I ; product $\overrightarrow { P _ { 2 t } }$ also contains internal APIs $I _ { 1 }$ and $I _ { 3 } ;$ product $\overrightarrow { P _ { 3 t } }$ contains internal APIs $I _ { 1 } , I _ { 2 } , I _ { 3 } ,$ and $I _ { 4 } ;$ and $\overrightarrow { P _ { 4 t } }$ also contains internal APIs $I _ { 1 }$ to $I _ { 4 }$ . Thus, the matrix I representing the usage of internal APIs by all four products (which can also be understood as the design choices about the internal APIs by all developers) can be defined as

$$
\mathbf {I} _ {t} = \left[ \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 0 & 0 & 1 & 1 \\ 1 & 1 & 1 & 1 \\ 0 & 0 & 1 & 1 \end{array} \right].
$$

Continuing the example, assume there are two available external APIs, $E _ { 1 }$ and $E _ { 2 } ,$ , at time t. Product $\overrightarrow { P _ { 1 t } }$ does not use any external $\operatorname { A P I } ,$ , product $\overrightarrow { P _ { 2 t } }$ contains external API $E _ { 2 } ,$ , product $\overrightarrow { P _ { 3 t } }$ contains external API $E _ { 1 }$ , and product $\overrightarrow { P _ { 4 t } }$ uses external API $E _ { 2 }$ . The matrix $\mathbf { E } _ { t }$ representing the usage of external APIs by all four products (which can also be understood as the design choices about the external APIs by all developers) can be defined as

$$
\mathbf {E} _ {t} = \left[ \begin{array}{c c c c} 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \end{array} \right].
$$

Combining the notation of $\mathbf { I } _ { t }$ and $\mathbf { E } _ { t } ,$ the outcome of the collective combinatorial design decisions by the entire group of developers in the platform ecosystem at time t can be represented as matrix $\mathbf { P } _ { t } ,$ , which is the column-wise concatenation of I and $\mathbf { E } _ { t }$ . Continuing our example, there are six APIs alto gether: four internal APIs, $I _ { 1 } , I _ { 2 } , I _ { 3 } ,$ , and ${ \cal I } _ { 4 } ,$ and two external APIs, $E _ { 1 }$ and $E _ { 2 }$ . Product $\overrightarrow { P _ { 1 t } }$ is built using internal APIs $I _ { 1 }$ and $I _ { 3 }$ and no external API, product $\overrightarrow { P _ { 2 t } }$ is built using internal APIs $I _ { 1 }$ and $I _ { 2 }$ and external API $E _ { 2 }$ , product $\overrightarrow { P _ { 3 t } }$ is built using internal APIs $I _ { 1 } { - } I _ { 4 }$ and external API $E _ { 1 } ,$ , and product $\overrightarrow { P _ { 4 t } }$ is built using internal APIs $I _ { 1 } { - } I _ { 4 }$ and external API $E _ { 2 }$ . The design choices about internal and external APIs for all the products at time $t ,$ thus, can be represented as

$$
\mathbf {P} _ {t} = \left[ \begin{array}{c} \mathbf {I} _ {t} \\ \mathbf {E} _ {t} \end{array} \right] = \left[ \begin{array}{c c c c} 1 & 1 & 1 & 1 \\ 0 & 0 & 1 & 1 \\ 1 & 1 & 1 & 1 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \end{array} \right].
$$

We now show how the product design evolves from one time period to the next. Assume that a new product appears in the new time period $t + 1$ . For example, besides the four products built in $t , \overrightarrow { P _ { 1 t } } , \overrightarrow { P _ { 2 t } } , \overrightarrow { P _ { 3 t } }$ , and $\overrightarrow { P _ { 4 t } }$ , one more product <sup>appears</sup> <sup>in</sup> <sup>the</sup> <sup>platform</sup> <sup>ecosystem</sup> <sup>in</sup> <sup>t</sup> <sup>+</sup> <sup>1.</sup> <sup>Let</sup> <sup>us</sup> <sup>further</sup>− → assume that the newly added product, $P _ { 5 , t + 1 }$ , consists of internal $\mathrm { A P I s } I _ { 1 }$ and $I _ { 2 }$ and a new external API, $E _ { 3 }$ . Then, $\mathbf { P } _ { t + 1 , }$ the design choices about internal API and external API for all the products at time t + 1, are defined as follows:

$$
\mathbf {P} _ {t + 1} = \left[ \begin{array}{c} \mathbf {I} _ {t + 1} \\ \mathbf {E} _ {t + 1} \end{array} \right] = \left[ \begin{array}{c c c c c} 1 & 1 & 1 & 1 & 1 \\ 0 & 0 & 1 & 1 & 0 \\ 1 & 1 & 1 & 1 & 1 \\ 0 & 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 1 \end{array} \right].
$$

The numbers of internal and external APIs, M and $N ,$ are determined at the end of time $T \ ( 1 \leq t \leq T )$ . Thus, they are constant across all the time periods t. The newly built product, $P _ { 5 , t + 1 }$ , is appended as a new column in matrix $\mathbf { P } _ { t + 1 }$

At any given time period $t ,$ matrix $\mathbf { P } _ { t }$ can also be interpreted as the relationship between APIs and products. Assuming there are M internal APIs, N external APIs, H APIs in total $( H = M + N )$ , and $K$ products, a generalized definition of matrix $\mathbf { P } _ { t }$ can be given as

$$
\begin{array}{c} \overrightarrow {P _ {1 t}} \quad \overrightarrow {P _ {2 t}} \quad \dots \quad \overrightarrow {P _ {K t}} \\ \mathbf {P} _ {t} = \left[ \begin{array}{c} \mathbf {I} _ {t} \\ \mathbf {E} _ {t} \end{array} \right] = \left[ \begin{array}{c c c c} I _ {1 1} & I _ {1 2} & \dots & I _ {1 K} \\ I _ {2 1} & I _ {2 2} & \dots & I _ {2 K} \\ \vdots & \vdots & \ddots & \vdots \\ I _ {M 1} & I _ {M 2} & \dots & I _ {M K} \\ E _ {1 1} & E _ {1 2} & \dots & E _ {1 K} \\ E _ {2 1} & E _ {2 2} & \dots & E _ {2 K} \\ \vdots & \vdots & \ddots & \vdots \\ E _ {N 1} & E _ {N 2} & \dots & E _ {N K} \end{array} \right] \\ = A P I _ {1} \left[ \begin{array}{c c c c} p _ {1 1} & p _ {1 2} & \dots & p _ {1 K} \\ p _ {2 1} & p _ {2 2} & \dots & p _ {2 K} \\ \vdots & \vdots & \ddots & \vdots \\ A P I _ {H} & p _ {H 1} & p _ {H 2} & \dots & p _ {H K} \end{array} \right] \end{array}
$$

According to this definition, in matrix $\mathbf { P } _ { t } ,$ , each column vector $\overrightarrow { P _ { j t } }$ represents a product. Each component of the column vector has a binary value, indicating whether API i is used in product $\overrightarrow { P _ { j t } }$ . If API i is used in product $\overrightarrow { P _ { j t } }$ , the corresponding entry $p _ { i j } = 1 ;$ otherwise, $p _ { i j } = 0$ . Meanwhile, each row vector $A P I _ { i }$ represents the usage of API in all products, $\overrightarrow { P _ { 1 t } } , \dots , \overrightarrow { P _ { K t } }$ Based on the meaning of the row and column, we can also name $\mathbf { P } _ { t }$ as the API–product matrix.

Once matrix $\mathbf { P } _ { t }$ is obtained at time $t ,$ we can consequently define the product similarity matrix $\mathbf { S } _ { t } ,$ in which any given entry, ${ } _ { s _ { i j } , }$ , represents the similarity between two products $\overrightarrow { P _ { i t } }$ and $\boldsymbol { P _ { j t } }$ . The definition of $\mathbf { S } _ { t }$ is given as

$$
\begin{array}{c} \mathbf {S} _ {t} = \left[ \begin{array}{c c c c} s _ {1 1} & s _ {1 2} & \dots & s _ {1 K} \\ s _ {2 1} & s _ {2 2} & \dots & s _ {2 K} \\ \vdots & \vdots & \ddots & \vdots \\ s _ {K 1} & s _ {i 2} & \dots & s _ {K K} \end{array} \right], \\ \text {where} s _ {i j} = \frac {1 + c o r r (\overrightarrow {P _ {i t}} , \overrightarrow {P _ {j t}})}{2}. \end{array}
$$

According to the second equation, the similarity $s _ { i j }$ is derived from $c o r r ( \overrightarrow { P _ { i t } } , \overrightarrow { P _ { j t } } )$ , where the correlation between two vectors represents the set of APIs used by products $P _ { i t }$ and $P _ { j t }$ . The more common APIs shared by two products, the higher their similarity. When products $\xrightarrow [ { P _ { i t } } ] { }$ and $\overrightarrow { P _ { j t } }$ share the same set of $\mathrm { A P I s } , s _ { i j }$ achieves the maximum value of one. When products $\overrightarrow { P _ { i t } }$ and $\overrightarrow { P _ { j t } }$ do not share any common APIs at all, $s _ { i j }$ achieves the minimum value of zero. Because there are $K$ products at time $t ,$ the size of the symmetric matrix $\mathbf { S } _ { t }$ is $K \bar { \times } K$ . As the similarity between a vector and itself is one, the main diagonal elements of $\mathbf { S } _ { t }$ are all ones.

After the similarity matrix $\mathbf { S } _ { t }$ is defined, we can transform it into a product (weighted) adjacency matrix $\mathbf { A } _ { t } .$ . This matrix represents the “combinatorial” relationship of products sharing the same API. The definition of matrix A is given as

$$
\mathbf {A} _ {t} = \left[ \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 K} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 K} \\ \vdots & \vdots & \ddots & \vdots \\ a _ {K 1} & a _ {K 2} & \dots & a _ {K K} \end{array} \right],
$$

$$
\text { where } a _ {i j} = | s _ {i j} | ^ {\beta}, \beta \in \mathbb {Z} ^ {+}, \beta > 1.
$$

The elements of adjacency matrix $\mathbf { A } _ { t } , a _ { i j } ,$ , are defined as an exponentiation function of $s _ { i j } ,$ , the elements of the similarity matrix $\mathbf { S } _ { t }$ . The exponent $\beta ,$ also called the soft thresholding number, is an integer larger than one and has the purpose of suppressing low correlations. According to Langfelder and Horvath (2008), $\beta$ is set between 5 and 10 and most commonly is set to $^ { 6 . }$ The exponentiation function forces small values of $a _ { i j }$ to converge to zero. When the similarity between two products $s _ { i j }$ is small, for example, $s _ { i j } = 0 . 1 , \ \beta = 6 ,$ , then $a _ { i j } = ~ | s _ { i j } | ^ { \beta } = | 0 . 1 | ^ { 6 } = 1 \times 1 0 ^ { - 6 } \approx 0 .$ . Compared with similarity matrix $\mathbf { S } _ { t } ,$ , adjacency matrix ${ \bf A } _ { t }$ also represents the similarity between any two products, $\overrightarrow { P _ { i t } }$ and $\overrightarrow { P _ { j t } }$ . Only entries with high value are kept, and those with low value are approxi mated to zero. Product adjacency matrix $\mathbf { A } _ { t }$ is also symmetric with all zeros on the main diagonal because it does not allow self-loops. Going back to our example, the following is an example of ${ \bf A } _ { t }$ that consists of four original products at time t that were built using six APIs:

$$
\mathbf {A} _ {t} = \left[ \begin{array}{c c c c} 0 & 0. 3 0 & 0. 0 6 & 0. 0 6 \\ 0. 3 0 & 0 & 0. 0 2 & 0. 2 1 \\ 0. 0 6 & 0. 0 2 & 0 & 0. 2 7 \\ 0. 0 6 & 0. 2 1 & 0. 2 7 & 0 \end{array} \right].
$$

## A.2. Mathematical Modeling of Functional Categories in the Digital Platform

So far, we characterize the design actions of individual developers as a combinatorial choice process in isolation. Here, the goal of a developer’s design action is to seek a particular recombination of APIs that satisfies the developer’s design goals. Now, let us consider how these individual design actions by developers collectively shape the product variety in a digital platform ecosystem. The product variety $( \mathrm { i . e . , }$ functional categories) in a digital platform system is the rate by which developers come up with unforeseen products in the ecosystem. We use product adjacency matrix $\mathbf { A } _ { t }$ to represent the collective design choices in the platform ecosystem made by all developers at time t. Once the project adjacency matrix $\mathbf { A } _ { t }$ is built, we can use it to construct the TOM $\mathbf { W } _ { t }$ and identify groups of products that are built with similar APIs. The topological overlap matrix (Ravasz et al. 2002, Ravasz and Baraba´si 2003) is a widely used tool to detect network clusters consisting of nodes that are closely connected or highly similar.

In our context, adjacency matrix ${ \bf A } _ { t }$ shows the similarity between any two products, whereas the topological overlap matrix $\mathbf { W } _ { t }$ shows groups of all products that are similar and visualizes the relationship among them through a heat map. We use it to explore and delineate the possible presence of recurring patterns $( \mathrm { i . e . , }$ topological overlaps) of API combinations, both internal and external, that form clusters of similar products in terms of their design choices. A topological overlap matrix at time $t , \mathbf { W } _ { t } ,$ is defined as

$$
\mathbf {W} _ {t} = \left[ \begin{array}{c c c c} w _ {1 1} & w _ {1 2} & \dots & w _ {1 K} \\ w _ {2 1} & w _ {2 2} & \dots & w _ {2 K} \\ \vdots & \vdots & \ddots & \vdots \\ w _ {K 1} & w _ {K 2} & \dots & w _ {K K} \end{array} \right],
$$

$$
w _ {i j} = \left\{ \begin{array}{c l} \frac {l _ {i j} + a _ {i j}}{\min (k _ {i} , k _ {j}) + 1 - a _ {i j}} & \text {if i\neq j} \\ 1 & \text {if i = j,} \end{array} \right.
$$

where $\begin{array} { r } { \boldsymbol { l } _ { i j } = \sum _ { u } a _ { i u } \boldsymbol { a } _ { j u } , \ \boldsymbol { k } _ { i } = \sum _ { u } a _ { i u } , \ 1 \leq u \leq K , } \end{array}$ , and the index u goes through all products. In particular, $k _ { i }$ is the sum of all the adjacency weights between product i and all its neighbors. It is the weighted degree (also called close connectivity) of i and represents the sum of connection strengths of i with other network nodes (products). In our context, the connectivity measures how similar a product is to all other products as meas ured by the common APIs used by the products. Furthermore, $l _ { i j }$ represents the sum of adjacency weights of products to which both i and j are connected. In other words, $l _ { i j }$ measures the total connectivity of all common neighbors of i and j.

The topological overlap matrix, $w _ { i j } ,$ also called the topo logical overlap measure, evaluates the relative interconnectedness between nodes in the network (Ravasz et al. 2002, Doncheva et al. 2012). It represents the weighted similarity measured in a network described by an adjacency matrix (Zhao et al. 2010). As such, the topological overlap matrix aims to measure proximity and then delineate the clusters of data points, all when considering the adjacency between two data points. In our context, products are represented by the recombination of APIs, and the connection strength represents the similarity in terms of common APIs shared with others. W is a symmetric matrix with all elements of the main diagonal equal to one. The value of $w _ { i j }$ achieves the maximum of one when two products i and $j$ are built using the same set of APIs; the value achieves the minimum of zero if products i and j do not share any APIs.

TOM $\mathbf { W } _ { t }$ is a block matrix and is used for cluster detection. Clusters are defined as groups of densely interconnected products. Because the presence of clusters represents the diversity in products, we can measure the product variety in a platform ecosystem using clusters of products. All the groups of products with high correlation are grouped together diagonally, displaying a similar combinatorial $\mathrm { \dot { A P I } }$ pattern calculated from the correlations of APIs used in products. The topological overlap measure offers a quantitatively robust understanding of a complex network by segmenting the boundary of nested clusters in a cluster to explore the hierarchical order (Ravasz et al. 2002, Yip and Horvath 2007). Nodes with similar entry values in the topological overlap matrix are likely to form a cluster in a network. Thus, the topological overlap measure specifies the entries to efficiently represent not only the nested clusters of a cluster, but also the hierarchical order of nested clusters. Using this method, clusters of nodes with high similarity across the main diagonal can be found. One advantage of this method is that it is able to identify nested clusters in a larger cluster, so the group composition can be highly detailed and accurate.

Going back to our example in Section 3.1, W<sub>t</sub> is shown (color online):

$$
\mathbf {W} _ {t} = \left[ \begin{array}{c c c c} 1 & 0. 2 6 & 0. 0 7 & 0. 0 9 \\ 0. 2 6 & 1 & 0. 1 7 & 0. 1 3 \\ \hline 0. 0 7 & 0. 1 7 & 1 & 0. 2 5 \\ 0. 0 9 & 0. 1 3 & 0. 2 5 & 1 \end{array} \right].
$$

In this example, there are two clusters across the main diagonal. The first cluster consists of two products with the highest similarity, 1 and $^ { 2 , }$ with a topological overlap similarity of 0.26. The second cluster also consists of two other product with the next highest similarity, 3 and $^ { 4 , }$ with a topological overlap similarity of 0.25. In our context, we use hierarchical clustering (Langfelder and Horvath 2008) to identify clusters of products that use a similar set of APIs. Therefore, the presence of a large number of clusters of third-party products represents product variety in a platform ecosystem.

A digital platform ecosystem is dynamic because new APIs are continuously added. Developers design new products using new APIs as they see new opportunities in the market. The emergence of new products, in turn, changes the formation of the existing clusters of products. The changes to the clusters of products can lead to the emergence of a new cluster, embodying new types of products, thus representing the product variety of the ecosystem because the form of product vari ety is primarily driven by the recombination of APIs.

To be more specific, once formed, each cluster of products continues to evolve as the number of products and of new APIs continue to increase. As the size of the cluster increases, nested clusters of products with the specific combination pattern of $\mathbf { I } _ { t }$ and $\mathbf { E } _ { t }$ can emerge. If the sizes of nested clusters within a cluster are large enough to be scientifically meaningful, a cluster can be further split into nested clusters. Going back to our example, at time t + 1, recall a new product $\xrightarrow [ P _ { 5 , t + 1 }$ is designed with the introduction of a new external API, $E _ { 3 }$ These additions create cascading changes in $\mathbf { P } _ { t + 1 } , \mathbf { S } _ { t + 1 } , \mathbf { A } _ { t + 1 } ,$ and $\mathbf { W } _ { t + 1 } . ^ { 7 }$ The new TOM $\mathbf { W } _ { t + 1 }$ is

$$
\mathbf {W} _ {t + 1} = \left[ \begin{array}{c c c c c} 1 & 0. 2 6 & 0. 0 7 & 0. 0 9 & 0. 2 9 \\ 0. 2 6 & 1 & 0. 0 7 & 0. 1 7 & 0. 1 3 \\ 0. 0 7 & 0. 0 7 & 1 & 0. 2 5 & 0. 0 3 \\ 0. 0 9 & 0. 1 7 & 0. 2 5 & 1 & 0. 0 4 \\ 0. 2 9 & 0. 1 3 & 0. 0 3 & 0. 0 4 & 1 \end{array} \right].
$$

To make clustering more obvious, we move row 5 and column 5 to row 1 and column 1, shifting the rest of the matrix down one, without affecting the network structure that matrix $\mathbf { W } _ { t + 1 }$ represents. We then have (color online):

$$
\mathbf {W} _ {t + 1} ^ {\prime} = \left[ \begin{array}{c c c c c} 1 & 0. 2 9 & 0. 1 3 & 0. 0 3 & 0. 0 4 \\ 0. 2 9 & 1 & 0. 2 6 & 0. 0 7 & 0. 0 9 \\ 0. 1 3 & 0. 2 6 & 1 & 0. 0 7 & 0. 1 7 \\ \hline 0. 0 3 & 0. 0 7 & 0. 0 7 & 1 & 0. 2 5 \\ 0. 0 4 & 0. 0 9 & 0. 1 7 & 0. 2 5 & 1 \end{array} \right].
$$

The addition of a new product and an external API at time t + 1 result in the growth of the first cluster that originally contained products 1 and 2. Now a subcluster comes into being in the first cluster, consisting of products 5 and 1 as represented by submatrix $\left[ \begin{array} { c c } { 1 } & { 0 . 2 9 } \\ { 0 . 2 9 } & { 1 } \end{array} \right]$

We represent these changes in the hierarchical clusters of the ecosystem using a dendrogram. Within each cluster, products that primarily use the same set of APIs are positioned in the topologically upper hierarchy, whereas those that use less popular APIs are located in the lower hierarchy (Ravasz et al. 2002). Therefore, products in the topologically upper hierarchy use APIs with the high use frequencies.

Recall that we have four products $\overrightarrow { P _ { 1 t } } , \overrightarrow { P _ { 2 t } } , \overrightarrow { P _ { 3 t } }$ , and $\overrightarrow { P _ { 4 t } }$ at time t. The first step is to find the two most similar products, according to the entries in TOM $\mathbf { } \mathbf { W } _ { t } .$ . The larger the value of $w _ { i j } ,$ the higher the similarity between the corresponding products $\overrightarrow { P _ { i t } }$ and $\overrightarrow { P _ { j t } }$ . Because $\overrightarrow { P _ { 1 t } }$ and $\overrightarrow { P _ { 2 t } }$ have a topological overlap similarity of 0.26, they merge to become cluster 1. The second step is to find that the next two most similar products, which are $\overrightarrow { P _ { 3 t } }$ and $\overrightarrow { P _ { 4 t } }$ , have a similarity of 0.25.

With $\xrightarrow [ P _ { 5 , t + 1 }$ added at time t + 1, the hierarchical clustering method finds that the first cluster of the two most similar products, $\xrightarrow [ P _ { 5 , t + 1 }$ and $\overrightarrow { P _ { 1 , t + 1 } }$ , has a topological similarity of 0.29. The second step is to find the next two most similar products, which are $\overrightarrow { P _ { 1 , t + 1 } }$ and $\overrightarrow { P _ { 2 , t + 1 , } }$ , with a similarity of 0.26. It is shown in Figure A.1. Because $\overrightarrow { P _ { 5 , t + 1 } }$ and $\overrightarrow { P _ { 1 , t + 1 } }$ already comprise cluster 1, cluster 1 becomes a subcluster of cluster 2, which include $\xrightarrow [ P _ { 2 , t + 1 } , ] { } \xrightarrow [ P _ { 1 , t + 1 }$ , and $\overrightarrow { P _ { 5 , t + 1 } }$ . The third step determines cluster 3, which consists of $\tilde { P _ { 3 , t + 1 } }$ and $\overrightarrow { P _ { 4 , t + 1 } }$ because they have the next highest similarity of 0.25. It is shown in Figure A.2.

Figure A.1. Hierarchical Clustering Dendrogram at Time t  
![](/api/attachments/ADHBP92X/fulltext/images/3618adc0abbe685fefb0821195c3c6450d4e5603329a602caaadad89c96bee0f.jpg)

Figure A.2. Hierarchical Clustering Dendrogram at Time t + 1  
![](/api/attachments/ADHBP92X/fulltext/images/a0af8d770a475cdd58d9ccbb80c5177b206bca580382514a45602d7b1a435d34.jpg)

## A.3. Modeling the Use Frequency of APIs

So far, we have explored how the combinatorial design actions of individual developers affect the digital platform ecosystem. We now look at what specific APIs are used to create different products. Not all APIs are equally useful; developers select certain APIs more frequently than others in order to build products. Following this logic, APIs can be grouped based on their frequency of use, and the TOM captures the relationships between products and shared APIs. From the point of view of products (or from the “top”), clusters are groups of highly similar products. From the point of view of APIs (or from the “bottom”), clusters (of API) can explain the decision choice about which API is used to create products.

To specifically explore the impact of the combination of APIs on creating products, we need to build an undirected network of APIs, which can be modeled as an unweighted API matrix (<sup>G</sup> ) as shown:

$$
\boldsymbol {\Gamma} _ {t} = \left[ \begin{array}{c c c c} \gamma_ {1 1} & \gamma_ {1 2} & \dots & \gamma_ {1 H} \\ \gamma_ {2 1} & \gamma_ {2 2} & \dots & \gamma_ {2 H} \\ \vdots & \vdots & \ddots & \vdots \\ \gamma_ {H 1} & \gamma_ {H 2} & \dots & \gamma_ {H H} \end{array} \right].
$$

The API adjacency matrix has a size of $H \times H ,$ , where H is the total number of APIs (both internal and external). The rows and columns are assigned to APIs, and the presence and absence of connections between any two APIs is displayed by a binary value. The binary entries are used to focus on the diverse uses of each API. The matrix elements, $\gamma _ { i j } ,$ are equal to one if API i and j are both used in the same product. $\Gamma _ { t }$ does not allow self-loops; thus, the main diagonal shows all zeroes. $\Gamma _ { t }$ is symmetric so that the entries of upper and lower bounds are the same. For example, <sup>G</sup> for our example with four products with six APIs (four internal and two external) at time t is

<table><tr><td></td><td>1 $(I_1)$ </td><td>2 $(I_2)$ </td><td>3 $(I_3)$ </td><td>4 $(I_4)$ </td><td>5 $(E_1)$ </td><td>6 $(E_2)$ </td></tr><tr><td>1  $(I_1)$ </td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>2  $(I_2)$ </td><td>1</td><td></td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>3  $(I_3)$ </td><td>1</td><td>1</td><td></td><td>1</td><td>1</td><td>1</td></tr><tr><td>4  $(I_4)$ </td><td>1</td><td>1</td><td>1</td><td></td><td>1</td><td>1</td></tr><tr><td>5  $(E_1)$ </td><td>1</td><td>1</td><td>1</td><td>1</td><td></td><td>0</td></tr><tr><td>6  $(E_2)$ </td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td></td></tr></table>

By exploring the entries of $\Gamma _ { t } ,$ we can determine which APIs are more important in the ecosystem than others $( \mathrm { i . e . , }$ those that are more densely connected with others, thus indicating frequent use). To do this, we transform $\Gamma _ { t }$ to a core/ periphery structure (Borgatti and Everett 2000). A typical core/periphery structure classifies nodes in a network into two classes: core and periphery. A core is defined as a group of nodes that are densely interconnected, often fully con nected, whereas a periphery is defined as a group of nodes that are connected to the core nodes but themselves are not densely interconnected with other peripheral nodes (Borgatti and Everett 2000).

However, as we note earlier, a digital platform ecosystem consists of multiple clusters of products that share a number of APIs. Therefore, a simple core/periphery structure may not capture the complexity of a digital platform ecosystem. To address this issue, we propose a multicore/periphery net work structure in an API adjacency matrix (Csermely et al. 2013, Baldwin et al. 2014, Rombach et al. 2014, Kojaku and Masuda 2017), which builds on the generalized block modeling of Doreian et al. (2005). To do this, we first move all the $^ { \prime \prime } 1 ^ { \prime \prime }$ entries of <sup>G</sup> to be adjacent to each other across the main diagonal and all the $\prime \prime 0 \prime \prime$ entries to be adjacent to each other so that the pattern of 1-block and 0-block is amplified. With our multicore/periphery network structure, instead of a simple dichotomy of 1-block and 0-block, we expect to find three types of API block: a perfect 1-block, an imperfect 1-block in which the majority of the entries are ones, and an imperfect 0-block in which the majority of the entries are zeros.

With a generalized blocking model, blocks can be defined as different types, such as complete, regular, and null. The differences among these types lie in the connections inside and between clusters. A complete block is a fully connected group and has the highest network density. A null block is a fully disconnected group in which no two members are connected, and thus, it has the lowest density among the three types. A regular block is a densely but not fully connected network, and thus, its density rests between a complete and null block. Based on this, we expect to identify three types of APIs from an API adjacency matrix.

First, we define complete core APIs, which are APIs fully connected with each other in $\Gamma _ { t }$ and densely connected with other APIs. Technically, they are grouped in a complete block. In a platform system, the complete core APIs act as a functional core to system performance (Baldwin et al. 2014). They are always used together by all products on a platform system. Complete core nodes are adjacent to all other APIs in the API adjacency matrix.

Second, we define regular core APIs, which is a regula block and is between complete core and periphery (Eppinger et al. 1994, Sosa et al. 2004). The regular core APIs are not as cohesively connected as those in the complete core, but are more cohesively connected with the APIs in the periphery (Csermely et al. 2013, Rombach et al. 2014, Kojaku and Masuda 2017). Technically, they are in a regular block. In a platform system, regular core APIs represent functionally useful APIs widely used together with others. Some of them are adjacent to one another and form a distinct set of functions that are cohesive and repeatedly used by a cluster of products in a platform ecosystem. As such, we expect that they do not necessarily need to be related to the system’s key performance, but may widen the functional diversification of products (Yoo et al. 2010, Baldwin et al. 2014). Regular core APIs bring internal stability within a cluster of an ecosystem and create varieties across clusters (Wilkie and Kitchenham 2000, Sosa et al. 2013).

Finally, we define periphery APIs as the periphery APIs that are sparsely connected with other APIs (Borgatti and Everett 2000). Technically, they are in a null block. They are not used frequently enough to form clusters of products and lead to low connection among APIs in a platform ecosystem.

In a multicore system, the core/periphery structure is not fixed over time (Baldwin et al. 2014). If some periphery APIs are repeatedly used, changes occur in $\Gamma _ { t }$ and eventually also in the product clusters.

Going back to our example, Figure A.3(a) is the API adjacency matrix $\left( \Gamma _ { t + 1 } \right)$ of the example at time t + 1 with five products and seven APIs (four internal and three external). $\boldsymbol { \mathrm { W e } }$ then apply generalized block modeling (Doreian et al. 2005) to the matrix. The transformed matrix $\mathbf { { \Gamma } } _ { t + 1 } ^ { r }$ is shown in Figure A.3(b). The row and column belonging to APIs 2 and 3 switch positions and are represented by $3 ^ { \prime }$ and $^ { 2 ^ { \prime } , }$ respectively. API 1 and $2 ^ { \prime }$ construct the complete core as each of them is linked with all the other APIs. $\mathrm { { A P I } } 3 ^ { \prime }$ and 4 construct the regular core as neither of them are connected with periphery $^ { 7 , }$ forming an imperfect 1-block. Besides 1 and ${ 2 ^ { \prime } } ,$ $\mathrm { { A P I } } 3 ^ { \prime }$ is also connected to $4 , 5 ,$ , and $6 ; \mathrm { A P I 4 }$ is linked with ${ 3 ^ { \prime } } ,$ $5 ,$ and 6. Finally, API $5 , 6 ,$ and 7 construct the periphery as they form an imperfect 0-block. They are linked with the core and regular core but not connected to each other.

Figure A.3. API Adjacency Matrix Consists of Complete Core, Regular Core, and Periphery  
(a)

<table><tr><td></td><td>1 $(I_1)$ </td><td>2 $(I_2)$ </td><td>3 $(I_3)$ </td><td>4 $(I_4)$ </td><td>5 $(E_1)$ </td><td>6 $(E_2)$ </td><td>7 $(E_3)$ </td></tr><tr><td>1  $(I_1)$ </td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>2  $(I_2)$ </td><td>1</td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td>3  $(I_3)$ </td><td>1</td><td>1</td><td></td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>4  $(I_4)$ </td><td>1</td><td>1</td><td>1</td><td></td><td>1</td><td>1</td><td>0</td></tr><tr><td>5  $(E_1)$ </td><td>1</td><td>1</td><td>1</td><td>1</td><td></td><td>0</td><td>0</td></tr><tr><td>6  $(E_2)$ </td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td></td><td>0</td></tr><tr><td>7  $(E_3)$ </td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td></td></tr></table>

(b)

<table><tr><td></td><td>1 $(I_1)$ </td><td>2&#x27;  $(I_3)$ </td><td>3&#x27;  $(I_2)$ </td><td>4 $(I_4)$ </td><td>5 $(E_1)$ </td><td>6 $(E_2)$ </td><td>7 $(E_3)$ </td></tr><tr><td>1 ( $I_1$ )</td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>2&#x27; ( $I_3$ )</td><td>1</td><td></td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>3&#x27; ( $I_2$ )</td><td>1</td><td>1</td><td></td><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td>4 ( $I_4$ )</td><td>1</td><td>1</td><td>1</td><td></td><td>1</td><td>1</td><td>0</td></tr><tr><td>5 ( $E_1$ )</td><td>1</td><td>1</td><td>1</td><td>1</td><td></td><td>0</td><td>0</td></tr><tr><td>6 ( $E_2$ )</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td></td><td>0</td></tr><tr><td>7 ( $E_3$ )</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td></td></tr></table>

Notes. (a) API adjacency matrix $\Gamma _ { t + 1 }$ before block modeling. (b) API adjacency matrix $\mathbf { { \Gamma } } _ { t + 1 } ^ { r }$ after block modeling.

## A.4. Hierarchical Clustering Procedure

Step 1. Define design choice matrix $\mathbf { P } _ { t + 1 } \colon$ Our observational data $\mathbf { P } _ { t + 1 }$ , the design choices of internal and external APIs for all the products at time t + 1, is shown:

$$
\mathbf {P} _ {t + 1} = \left[ \begin{array}{c} \mathbf {I} _ {t + 1} \\ \mathbf {E} _ {t + 1} \end{array} \right] = \left[ \begin{array}{c c c c c} 1 & 1 & 1 & 1 & 1 \\ 0 & 0 & 1 & 1 & 0 \\ 1 & 1 & 1 & 1 & 1 \\ 0 & 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 1 \end{array} \right].
$$

Step 2. Calculate similarity matrix $\mathbf { S } _ { t + 1 } \mathrm { ; }$ : The similarity matrix at time $t + 1 , \mathbf { S } _ { t + 1 }$ , is defined as follows:

$$
\mathbf {S} _ {t + 1} = \left[ \begin{array}{c c c c c} s _ {1 1} & s _ {1 2} & s _ {1 3} & s _ {1 4} & s _ {1 5} \\ s _ {2 1} & s _ {2 2} & s _ {2 3} & s _ {2 4} & s _ {2 5} \\ s _ {3 1} & s _ {3 2} & s _ {3 3} & s _ {3 4} & s _ {3 5} \\ s _ {4 1} & s _ {4 2} & s _ {4 3} & s _ {4 4} & s _ {4 5} \\ s _ {5 1} & s _ {5 2} & s _ {5 3} & s _ {5 4} & s _ {5 5} \end{array} \right],
$$

$$
\text { where } s _ {i j} = \frac {1 + c o r r (\overrightarrow {P _ {i , t + 1}} , \overrightarrow {P _ {j , t + 1}})}{2}.
$$

The corr $( \overrightarrow { P _ { i , t + 1 } } , \overrightarrow { P _ { j , t + 1 } } )$ is the cosine similarity between vectors $\overrightarrow { P _ { i , t + 1 } }$ and $\overrightarrow { P _ { j , t + 1 } } ,$ , which is defined as follows:

$$
c o r r \left(\overrightarrow {P _ {i , t + 1}}, \overrightarrow {P _ {j , t + 1}}\right) = \cos (\theta) = \frac {\overrightarrow {P _ {i , t + 1}} \cdot \overrightarrow {P _ {j , t + 1}}}{\| \overrightarrow {P _ {i , t + 1}} \| \| \overrightarrow {P _ {j , t + 1}} \|}.
$$

The magnitude of each vector $P _ { i , t + 1 } , \left( 1 \leq i \leq 5 \right)$ , is calculated as follows:

$$
\begin{array}{l} \| \overrightarrow {P _ {i , t + 1}} \| = \sqrt {p _ {1 i} ^ {2} + p _ {2 i} ^ {2} + p _ {3 i} ^ {2} + p _ {4 i} ^ {2} + p _ {5 i} ^ {2} + p _ {6 i} ^ {2} + p _ {7 i} ^ {2}}, \\ \overrightarrow {\| P _ {1 , t + 1} \|} = 1. 4 1, \overrightarrow {\| P _ {2 , t + 1} \|} = 1. 7 3, \overrightarrow {\| P _ {3 , t + 1} \|} = 2. 2 4, \\ \overrightarrow {\| P _ {4 , t + 1} \|} = 2. 2 4, \overrightarrow {\| P _ {5 , t + 1} \|} = 1. 7 3. \end{array}
$$

Hence, based on $\mathbf { P } _ { t + 1 }$ and $\xrightarrow [ P _ { i , t + 1 } ] { }$ , the similarity matrix at time t is calculated as follows:

$$
\mathbf {S} _ {t + 1} = \left[ \begin{array}{c c c c c} 1 & 0. 8 2 & 0. 6 3 & 0. 6 3 & 0. 8 2 \\ 0. 8 2 & 1 & 0. 5 2 & 0. 7 7 & 0. 6 7 \\ 0. 6 3 & 0. 5 2 & 1 & 0. 8 0 & 0. 5 2 \\ 0. 6 3 & 0. 7 7 & 0. 8 0 & 1 & 0. 5 2 \\ 0. 8 2 & 0. 6 7 & 0. 5 2 & 0. 5 2 & 1 \end{array} \right].
$$

Step 3. Calculate product adjacency matrix $\mathbf { A } _ { t } \mathbf { : }$ The product adjacency matrix at time $t + 1 , \mathbf { A } _ { t + 1 }$ , is defined as follows:

$$
\begin{array}{c} \mathbf {A} _ {t + 1} = \left[ \begin{array}{c c c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} & a _ {1 4} & a _ {1 5} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} & a _ {2 4} & a _ {2 5} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} & a _ {3 4} & a _ {3 5} \\ a _ {4 1} & a _ {4 2} & a _ {4 3} & a _ {4 4} & a _ {4 5} \\ a _ {5 1} & a _ {5 2} & a _ {5 3} & a _ {5 4} & a _ {5 5} \end{array} \right], \\ \text {where} a _ {i j} = | s _ {i j} | ^ {\beta}, \beta = 6. \end{array}
$$

Using the elements in similarity matrix $\mathbf { S } _ { t + 1 }$ calculated in the previous step, we can determine the elements for $\mathbf { A } _ { t + 1 } \colon$

$$
\begin{array}{c} \mathbf {A} _ {t + 1} = \left[ \begin{array}{c c c c c} 0 & | 0. 8 2 | ^ {6} & | 0. 6 3 | ^ {6} & | 0. 6 3 | ^ {6} & | 0. 8 2 | ^ {6} \\ | 0. 8 2 | ^ {6} & 0 & | 0. 5 2 | ^ {6} & | 0. 7 7 | ^ {6} & | 0. 6 7 | ^ {6} \\ | 0. 6 3 | ^ {6} & | 0. 5 2 | ^ {6} & 0 & | 0. 8 0 | ^ {6} & | 0. 5 2 | ^ {6} \\ | 0. 6 3 | ^ {6} & | 0. 7 7 | ^ {6} & | 0. 8 0 | ^ {6} & 0 & | 0. 5 2 | ^ {6} \\ | 0. 8 2 | ^ {6} & | 0. 6 7 | ^ {6} & | 0. 5 2 | ^ {6} & | 0. 5 2 | ^ {6} & 0 \end{array} \right] \\ = \left[ \begin{array}{c c c c c} 0 & 0. 3 0 & 0. 0 6 & 0. 0 6 & 0. 3 0 \\ 0. 3 0 & 0 & 0. 0 2 & 0. 2 2 & 0. 0 9 \\ 0. 0 6 & 0. 0 2 & 0 & 0. 2 6 & 0. 0 2 \\ 0. 0 6 & 0. 2 2 & 0. 2 6 & 0 & 0. 0 2 \\ 0. 3 0 & 0. 0 9 & 0. 0 2 & 0. 0 2 & 0 \end{array} \right]. \end{array}
$$

Step 4. Calculate topological overlap matrix $\mathbf { } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf { } } { \mathbf } { } { \mathbf } { } \mathbf { } { } \mathbf { } \mathbf { } { } \mathbf { } \mathbf { }  { \mathbf { } \mathbf { } } { \mathbf } { \mathbf { } } { \mathbf } { \mathbf } { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf  { \mathbf } { \mathbf \mathbf { } \mathbf } { \mathbf }  \mathbf $ : The TOM at time $t + 1 , \boldsymbol { W } _ { t + 1 }$ , is defined as follows:

$$
\mathbf {W} _ {t + 1} = \left[ \begin{array}{c c c c c} w _ {1 1} & w _ {1 2} & w _ {1 3} & w _ {1 4} & w _ {1 5} \\ w _ {2 1} & w _ {2 2} & w _ {2 3} & w _ {2 4} & w _ {2 5} \\ w _ {3 1} & w _ {3 2} & w _ {3 3} & w _ {3 4} & w _ {3 5} \\ w _ {4 1} & w _ {4 2} & w _ {4 3} & w _ {4 4} & w _ {4 5} \\ w _ {5 1} & w _ {5 2} & w _ {5 3} & w _ {5 4} & w _ {5 5} \end{array} \right],
$$

$$
\begin{array}{c} \text {where} w _ {i j} = \left\{ \begin{array}{c c} \frac {l _ {i j} + a _ {i j}}{\min (k _ {i} , k _ {j}) + 1 - a _ {i j}} & i f i \neq j \\ 1 & i f i = j, \end{array} \right. \\ l _ {i j} = \sum_ {u} a _ {i u} a _ {j u}, k _ {i} = \sum_ {u} a _ {i u}, 1 \leq u \leq 5. \end{array}
$$

In the preceding equation, replacing ${ { a } _ { i j } } ,$ , the element of product adjacency matrix $\mathbf { A } _ { t + 1 }$ , with the value calculated in the previous step, we can calculate all elements of matrix $\mathbf { W } _ { t + 1 } ;$

$$
\mathbf {W} _ {t + 1} = \left[ \begin{array}{c c c c c} 1 & 0. 2 6 & 0. 0 7 & 0. 0 9 & 0. 2 9 \\ 0. 2 6 & 1 & 0. 0 7 & 0. 1 7 & 0. 1 3 \\ 0. 0 7 & 0. 0 7 & 1 & 0. 2 5 & 0. 0 3 \\ 0. 0 9 & 0. 1 7 & 0. 2 5 & 1 & 0. 0 4 \\ 0. 2 9 & 0. 1 3 & 0. 0 3 & 0. 0 4 & 1 \end{array} \right].
$$

The calculated TOM in t + 1 matches that on Section 3.1 in the main text of the manuscript.

## Appendix B. Application of the Network Modeling B.1. Visualized Results of TOM

In this appendix, we show the 11 plug-in clusters of Word-Press as of December 2014.

Figure B.1 shows the heat maps for four different months: January 2004, December 2006, December 2010, and December 2014. These plots created by TOM provide a user-friendly view of large and complex networks and make hierarchical structure easily identified by visualization. In addition to the clusters of plug-ins, which can be provided by a dendrogram tree on the top, the heat map can also show the similarity of plug-ins across different clusters. In particular, each cell in the heat map can be matched to a node in the dendrogram, so we can visually identify how two plug-ins are related through shared APIs even though they belong to different clusters. In a dendrogram, each branch represents a cluster of plug-ins, and each leaf at the terminal end of a branch represents a plug-in. The bottom of the tree indicates low similarity, whereas the top represents high similarity (e.g., sharing commonly used APIs). Plug-ins that employ the most commonly used APIs are positioned at the top of each branch, whereas those that use less popular APIs are positioned at the bottom of the tree.

To specify the TOM structure introduced in the dendrogram, we used the dynamic cut tree method with a cluster size parameter of 700 in the R coding for the color bar (Langfelder and Horvath 2008). The cluster size parameter determines the precise location and height of the dendrogram tree for a horizontal cut to generate nested hierarchical clusters. The higher the number, the larger the average size of the cluster. Langfelder and Horvath (2008) suggest considering cluster stability and robustness with a heuristic process in order to choose optimal cluster size parameters depending on the nature of data with the lower bound being 25. We used data from 2010 through 2014 to choose a parameter that produced a stable and distinct pattern of clusters. Our heuristic process showed a stable result when we used a parameter between 650 and 750. Based on this, we fixed our cluster size parameter for the dynamic cut tree program at 700 (the median). We used the same value for the parameter for all monthly data from 2004 to 2014 to capture the changes in clusters over time.

Below the color bar of Figure B.1 is the plug-in network analysis with plug-ins arranged on both axes. Within the matrix, red represents high similarity and yellow represents low similarity. Thus, redness indicates densely connected regions and yellow represents sparsely connected areas. A cluster that is specified by a color bar can include nested clusters that represent a nested hierarchy. Nested clusters along the main diagonal line reveal that (1) there are certain repeated patterns of use of APIs, and (2) plug-ins are related to each other within the cluster. The different density of col ors within a cluster represents the degree of similarity (measured by the number of shared APIs) among plug-ins in each cluster. Connectedness in the off-diagonal region reveals how plug-ins belonging to different clusters interact with each other across different clusters specified by a color bar, indicating interdependency across clusters.

Table B.1 shows the emergence of plug-in clusters in the WordPress ecosystem over time. In 2004, WordPress started with a single cluster of only 86 plug-ins. The first split occurred in 2008, followed by two new clusters in 2010, after which new clusters continued to emerge in the ecosystem. A close examination of the results reveals an interesting relationship between the external APIs and the diversification of the ecosystem. The year that the first new plug-in cluster emerged (2008) is the same year that the number of external APIs grew from a mere 7 to 38. The growth of internal APIs stabilized after 2010 with only a few internal APIs added each year. The growth of external APIs, however, continued to grow at a much faster rate. The pattern of external API growth tracks the increase in the overall growth of the number of plug-ins as well as the continued emergence of new plug-in clusters.

Specifically, by measuring the nested clusters in a cluster for the dependent variable, we use two different values for the cluster size parameters, one for the upper bound and one for the lower bound, and we calculate two different numbers of clusters in a network. By calculating the difference between the two numbers, we then identify the size of a nested hierarchy for each cluster. For the upper bound parameter, we use 700, which is the value that we use to identify the clusters in our analysis (the results are reported in Table B.1). For December 2014, for example, as we have seen, there are 11 clusters. Then, for the lower bound parameter, we use 25, the amount allowed by the lower bound (Langfelder and Horvath 2008). For December 2014, it produces 70 clusters. Using the two different outputs, we calculate how many clusters created by the lower bound parameter are included in each of the 11 clusters generated by the upper bound parameter as a way to compute the number of nested hierarchies in a cluster. Plugin ID is used to classify which 70 clusters match the 11 clusters so that we can obtain the result for how many nested clusters are included in a cluster. Through the two steps, we are able to measure the number of nested hierarchies in each cluster in a plug-in network.

Figure B.1. (Color online) The Evolution of a Plug-in Network Using Topological Overlap Plots  
(a)  
(b)  
![](/api/attachments/ADHBP92X/fulltext/images/6ea3975561a5787d6581a773c5d8a7fb158fa147e0fd8d20b323e1c0bfc7c1e1.jpg)  
(c)  
(d)  
(a) Eighty-six plug-ins in January 2004. (b) One hundred forty-three plug-ins in December 2006. (c) Four thousand, seven hundred seventy plug ins in December 2010. (d) Twenty-three thousand, two hundred eighteen plug-ins in December 2014

Table B.1. Diversification of the WordPress Platform Ecosystem

<table><tr><td>Clusters</td><td>2004</td><td>2005</td><td>2006</td><td>2007</td><td>2008</td><td>2009</td><td>2010</td><td>2011</td><td>2012</td><td>2013</td><td>2014</td></tr><tr><td>Grey</td><td>86</td><td>139</td><td>150</td><td>298</td><td>328</td><td>564</td><td>500</td><td>1,775</td><td>2,304</td><td>2,473</td><td>3,080</td></tr><tr><td>Turquoise</td><td>0</td><td>0</td><td>0</td><td>0</td><td>724</td><td>1,998</td><td>1,860</td><td>1,961</td><td>2,297</td><td>2,796</td><td>3,257</td></tr><tr><td>Blue</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1,485</td><td>1,752</td><td>2,179</td><td>2,720</td><td>2,561</td></tr><tr><td>Brown</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>925</td><td>1,053</td><td>1,632</td><td>1,730</td><td>2,319</td></tr><tr><td>Yellow</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>942</td><td>1,507</td><td>1,270</td><td>2,161</td></tr><tr><td>Green</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>696</td><td>1,248</td><td>2,102</td></tr><tr><td>Red</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1,140</td><td>1,934</td></tr><tr><td>Black</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1,032</td><td>1,808</td></tr><tr><td>Pink</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1,737</td></tr><tr><td>Magenta</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1,272</td></tr><tr><td>Purple</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>897</td></tr><tr><td>Internal API</td><td>40</td><td>42</td><td>42</td><td>45</td><td>59</td><td>67</td><td>85</td><td>92</td><td>94</td><td>97</td><td>99</td></tr><tr><td>External API</td><td>4</td><td>5</td><td>5</td><td>7</td><td>38</td><td>70</td><td>116</td><td>163</td><td>208</td><td>253</td><td>344</td></tr><tr><td>Total plug-in</td><td>86</td><td>139</td><td>150</td><td>298</td><td>1,052</td><td>2,562</td><td>4,770</td><td>7,483</td><td>10,615</td><td>14,409</td><td>23,218</td></tr></table>

For each of these API interaction networks, we run core/ periphery analyses separately. This results in the identification of core and periphery for each of the 11 clusters. The dis tribution of internal and external APIs for core and periphery for each of the 11 clusters is shown in Table 4. Taken together there are 81 internal APIs and 38 external APIs throughout the cores of the 11 functional clusters.

Table B.3 shows that, whereas the use of internal APIs is somewhat consistent across the 11 clusters, showing 79.45 internal APIs on average (with 15.17 standard deviations), the use of external APIs varies more across different clusters, showing 79.91 external APIs on average (with 42.69 standard deviations), indicating that the differences across these cluster are primarily produced through external APIs. The standard deviation in each cluster is larger than the mean of each API usage in total API usages in Table $^ { 2 , }$ showing that certain APIs are clearly more frequently used than other APIs.

B.2. Test for the Orthogonality of Functional Categories We empirically conduct the following test. To measure the degree to which topics are orthogonal to each other, we first normalize all the column vectors $\overrightarrow { a _ { i } }$ representing 11 product categories such that

$$
\overrightarrow {| | a _ {i} | |} = 1
$$

because the orthogonality between two vectors is not determined by the lengths of the vectors, but their directions. We then construct matrix $\mathbf { A } ,$ which consists of 11 columns. Each column is an aforementioned normalized vector $\overrightarrow { a _ { i } }$ , which represents one product category out of the 11 categories we identified using topic modeling method, such as

$$
\mathbf {A} = \left[ \begin{array}{c c c c} \overrightarrow {a _ {1}} & \overrightarrow {a _ {2}} & \dots & \overrightarrow {a _ {1 1}} \end{array} \right].
$$

Table B.2. Distribution of Complete Cores and Periphery APIs

<table><tr><td>Cluster</td><td>Total API</td><td>Complete core API</td><td>Internal core API</td><td>External core API</td><td>Periphery API</td><td>Internal periphery API</td><td>External periphery API</td></tr><tr><td>Grey</td><td>263</td><td>120</td><td>81</td><td>38</td><td>143</td><td>6</td><td>137</td></tr><tr><td>Turquoise</td><td>135</td><td>27</td><td>20</td><td>7</td><td>108</td><td>44</td><td>64</td></tr><tr><td>Blue</td><td>184</td><td>51</td><td>39</td><td>12</td><td>133</td><td>38</td><td>95</td></tr><tr><td>Brown</td><td>153</td><td>41</td><td>34</td><td>7</td><td>112</td><td>47</td><td>65</td></tr><tr><td>Yellow</td><td>106</td><td>15</td><td>15</td><td>0</td><td>91</td><td>57</td><td>34</td></tr><tr><td>Green</td><td>145</td><td>25</td><td>22</td><td>3</td><td>120</td><td>51</td><td>69</td></tr><tr><td>Red</td><td>173</td><td>21</td><td>21</td><td>0</td><td>152</td><td>59</td><td>93</td></tr><tr><td>Black</td><td>71</td><td>10</td><td>10</td><td>0</td><td>61</td><td>34</td><td>27</td></tr><tr><td>Pink</td><td>106</td><td>12</td><td>12</td><td>0</td><td>94</td><td>42</td><td>52</td></tr><tr><td>Magenta</td><td>128</td><td>24</td><td>21</td><td>3</td><td>104</td><td>44</td><td>60</td></tr><tr><td>Purple</td><td>72</td><td>1</td><td>1</td><td>0</td><td>71</td><td>38</td><td>33</td></tr></table>

Table B.3. Internal and External API Statistics for Each Cluster Color

<table><tr><td>Clusters</td><td>Grey</td><td>Turquoise</td><td>Blue</td><td>Brown</td><td>Yellow</td><td>Green</td></tr><tr><td>Total number of APIs</td><td>278</td><td>179</td><td>204</td><td>174</td><td>124</td><td>164</td></tr><tr><td>Average of each API usage</td><td>106.16</td><td>78.12</td><td>119.15</td><td>82.84</td><td>58.14</td><td>108.75</td></tr><tr><td>Standard deviation</td><td>307.43</td><td>402.26</td><td>440.33</td><td>347.45</td><td>275.90</td><td>362.38</td></tr><tr><td>Maximum API usage</td><td>2,283</td><td>3,241</td><td>2,624</td><td>2,319</td><td>2,144</td><td>2,097</td></tr><tr><td>Minimum API usage</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Number of internal API usages</td><td>99</td><td>79</td><td>89</td><td>92</td><td>85</td><td>85</td></tr><tr><td>Average of each API usage</td><td>285.24</td><td>171.85</td><td>266.15</td><td>152.27</td><td>83.15</td><td>205.6</td></tr><tr><td>Standard deviation</td><td>463.82</td><td>592.34</td><td>637.16</td><td>466.93</td><td>330.23</td><td>483.58</td></tr><tr><td>Maximum API usage</td><td>2,283</td><td>2,341</td><td>2,624</td><td>2,319</td><td>2,144</td><td>2,097</td></tr><tr><td>Minimum API usage</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Number of external API usages</td><td>179</td><td>100</td><td>115</td><td>82</td><td>39</td><td>79</td></tr><tr><td>Average of each API usage</td><td>7.11</td><td>4.08</td><td>5.38</td><td>4.95</td><td>3.61</td><td>4.54</td></tr><tr><td>Standard deviation</td><td>16.16</td><td>6.05</td><td>9.80</td><td>8.86</td><td>4.27</td><td>7.19</td></tr><tr><td>Maximum API usage</td><td>98</td><td>27</td><td>44</td><td>51</td><td>19</td><td>37</td></tr><tr><td>Minimum API usage</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>Clusters</td><td>Red</td><td>Black</td><td>Pink</td><td>Magenta</td><td>Purple</td><td>-</td></tr><tr><td>Total number of APIs</td><td>185</td><td>94</td><td>120</td><td>147</td><td>84</td><td>-</td></tr><tr><td>Average of each API usage</td><td>136.12</td><td>28.33</td><td>57.08</td><td>60.72</td><td>45.18</td><td>-</td></tr><tr><td>Standard deviation</td><td>390.41</td><td>185.96</td><td>242.17</td><td>222.96</td><td>154.26</td><td>-</td></tr><tr><td>Maximum API usage</td><td>1,931</td><td>1,807</td><td>1,723</td><td>1,272</td><td>895</td><td>-</td></tr><tr><td>Minimum API usage</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>-</td></tr><tr><td>Number of internal API usages</td><td>92</td><td>57</td><td>68</td><td>77</td><td>51</td><td>-</td></tr><tr><td>Average of each API usage</td><td>269.92</td><td>45.40</td><td>98.54</td><td>113.30</td><td>72.94</td><td>-</td></tr><tr><td>Standard deviation</td><td>520.43</td><td>237.24</td><td>315.47</td><td>298.47</td><td>192.95</td><td>-</td></tr><tr><td>Maximum API usage</td><td>1,931</td><td>1,807</td><td>1,723</td><td>1,272</td><td>895</td><td>-</td></tr><tr><td>Minimum API usage</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>-</td></tr><tr><td>Number of external API usages</td><td>93</td><td>37</td><td>52</td><td>70</td><td>33</td><td>-</td></tr><tr><td>Average of each API usage</td><td>3.76</td><td>2.02</td><td>2.85</td><td>2.89</td><td>2.27</td><td>-</td></tr><tr><td>Standard deviation</td><td>6.06</td><td>1.65</td><td>3.64</td><td>4.20</td><td>2.08</td><td>-</td></tr><tr><td>Maximum API usage</td><td>32</td><td>7</td><td>22</td><td>29</td><td>9</td><td>-</td></tr><tr><td>Minimum API usage</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>-</td></tr></table>

We then calculate the product of A and its transpose $\mathbf { A } ^ { \top }$ $\mathbf { A } ^ { \top } \mathbf { A }$ , and test the product against an identity matrix $I _ { n } \colon$

$$
\left\{ \begin{array}{l l} H _ {0}: \mathbf {A} ^ {\top} \mathbf {A} = I _ {n} \\ H _ {a}: \mathbf {A} ^ {\top} \mathbf {A} \neq I _ {n}. \end{array} \right.
$$

The test result shows that the difference between $\mathbf { A } ^ { \top } \mathbf { A }$ and $I _ { n }$ is insignificant. Because a matrix is orthogonal if and only if all the column vectors form an orthonormal basis, we conclude that all the 11 product categories are pairwise orthogonal.

## B.3. Analyses of the Three-Layered Structure of APIs

In addition to the existence of the three layers after the later stage, we test the composition of APIs in each layer. We calculate the percentage of $" 1 \prime \prime$ entries $( \gamma _ { i j } = 1 )$ whose connected nodes are both external APIs in API adjacency matrix <sup>G</sup> for complete core, regular core, and periphery, respectively. The percentage of $^ { \prime \prime } 1 ^ { \prime \prime }$ entries connecting external APIs in the complete core across all time periods is zero. The average percentage of $^ { \prime \prime } 1 ^ { \prime \prime }$ entries connecting external APIs in the regular core is $0 . 0 6 2 \ : ( S D = 0 . 0 4 1 , M i n ^ { - } = 0 . 0 1 2 , M a x = 0 . 1 4 4 )$ for all time periods. Likewise, the average percentage of $" 1 \prime $ entries of external APIs in the periphery is 0.756 $\begin{array} { r } { ( S D = 0 . 0 8 4 , } \end{array}$ $M i n = 0 . 6 0 4 , M a x = 0 . 8 9 7 )$ ). A pairwise t-test to determine if the periphery has more external APIs than the regular core shows a significant difference, 0.693 $( S E = 0 . 0 1 3 , p < 0 . 0 0 1 )$ Table B.4 shows the descriptive statistics of different types of

APIs in three layers for each year (based on December of each year).

Table B.5 shows the examples of external APIs in the regular core and periphery.

## B.4. Product Categorization Using LDA

The five columns in Table B.1 show, for each cluster, the five most representative plug-ins, the total number of APIs used in each plug-in (including both internal and external APIs), the total number of internal APIs for each plug-in, the total number of external APIs in each plug-in, and the most fre quent keywords used in the description of plug-ins in the cluster, respectively. The main goal of this section is to check if the emergence of clusters of plug-ins based on the combinatorial pattern of APIs actually reflects increasing product varieties in the WordPress ecosystem. Because WordPress does not provide any a priori functional categorization of plug-ins, we compare the plug-in clusters created from the network analysis with another set of plug-in clusters based on similarities in textual information written by developers.

We use descriptions and tags together as the source data to categorize plug-ins. Descriptions are provided by the de velopers to explain the major functions of plug-ins when they are released. WordPress also uses tags to inform concise product features. When developers upload a plug-in to the WordPress ecosystem, they also use one or more single words representing the product’s function as tags. Hence, combining descriptions and tags of a product can give us more concrete textual information regarding its functions, and possibly help us to categorize product variety more accurately. We conducted our test in three steps using data from December 2014.

Table 
B.4. Average Number of Internal and External APIs in Regular Cores

<table><tr><td rowspan="2">Time</td><td rowspan="2">Number of clusters</td><td rowspan="2">Average number of nested clusters</td><td rowspan="2">Number of complete core Number</td><td colspan="2">Number of regular core internal API</td><td colspan="2">Number of regular core external API</td><td colspan="2">Number of periphery internal API</td><td colspan="2">Number of periphery external API</td></tr><tr><td>Average</td><td>Standard deviation</td><td>Average</td><td>Standard deviation</td><td>Average</td><td>Standard deviation</td><td>Average</td><td>Standard deviation</td></tr><tr><td>2008</td><td>2</td><td>6</td><td>5</td><td>18</td><td>9.90</td><td>0</td><td>0</td><td>21</td><td>7.07</td><td>18</td><td>9.90</td></tr><tr><td>2009</td><td>2</td><td>9.5</td><td>5</td><td>22</td><td>4.242</td><td>0.5</td><td>0.71</td><td>29</td><td>8.49</td><td>34.5</td><td>24.75</td></tr><tr><td>2010</td><td>4</td><td>9.25</td><td>6</td><td>24.25</td><td>16.07</td><td>0.5</td><td>0.87</td><td>31</td><td>7.07</td><td>41.25</td><td>17.54</td></tr><tr><td>2011</td><td>5</td><td>8.6</td><td>7</td><td>30.4</td><td>30.86</td><td>2.6</td><td>2.70</td><td>33</td><td>18.47</td><td>52.2</td><td>18.82</td></tr><tr><td>2012</td><td>6</td><td>11</td><td>7</td><td>29.5</td><td>28.97</td><td>4</td><td>3.80</td><td>37.83</td><td>18.23</td><td>58.33</td><td>28.61</td></tr><tr><td>2013</td><td>8</td><td>9.13</td><td>7</td><td>24</td><td>26.61</td><td>3.5</td><td>4.99</td><td>43.25</td><td>18.48</td><td>61.63</td><td>30.77</td></tr><tr><td>2014</td><td>11</td><td>9.27</td><td>12</td><td>27.4</td><td>21.26</td><td>6.46</td><td>10.97</td><td>41.91</td><td>14.19</td><td>66.27</td><td>32.39</td></tr></table>

First, we identify the thematic keywords of plug-ins that are associated with their functions as described by developers. We download the descriptions and tags of each of the 23,218 plug-ins from WordPress to identify thematic keywords (also known as controlled vocabularies), such as image, navigation, and search, that are repetitively used in conjunction to describe the function of a plug-in. We use LDA to discover and annotate the thematic keywords of plug-ins (Barde and Bainwad 2017). LDA follows an unsupervised learning algorithm to explore the hidden topical contents of text data by finding the semantic interpretation of keywords. A topic refers to a group of words frequently used together, assuming that the choice of words associated with particular content in the text data are bounded by several keywords. For example, words such as “genome,” “DNA,” and “sequence” are associated with genetics (Blei 2012).

LDA is used to explore how categorized thematic topics are connected to each other through a distribution of repetitively used words. As such, LDA statistically analyzes the hidden structure of topics used in multiple plug-in descriptions and tags, so it does not require any prior knowledge about the function of an individual API in each plug-in. In our context, a topic is a cluster of plug-ins, and a document is a plug-in description and tag. We do not use any information concerning API combinations and plug-in clusters from a plug-in coexpression network analysis. This ensures that the identification of functional clusters of plug-ins is performed completely independent of the combinatorial pattern of APIs among these plug-ins. Therefore, we expect to understand the driver of platform evolution by exploring the thematic pattern of plug-in descriptions and tags.

We follow a step-by-step procedure to analyze the text data (Gong et al. 2018). To preprocess data, we remove all unnecessary words, such as articles that do not include meaningful contexts in description, and convert all words to lowercase to vectorize the corpus of plug-in descriptions and tags (Manning et al. 2014). Then, we feed the preprocessed data to the LDA algorithm written in Java. The algorithm is based on using hierarchical Bayesian modeling to explore semantic linkage based on the frequency of words. To increase the accuracy, Markov chain Monte Carlo (i.e., Gibbs sampling) is applied to iterate the sampling process that helps to approximate the distribution of topics. Finally, we calculate the cosine similarity of plug-ins to explore the distance between the centroid of thematic keywords of plug-in and the description of each plug-in in each topic. In the fol lowing table, we select five plug-ins having the closest distance from the centroid in each topic. Also, we select five keywords with the highest frequency in each topic. We label each topic (cluster) based on the selected keywords.

Finally, a chi-squared test is applied to the two different types of clusters from TOM and LDA in order to understand if they are significantly different (or independent) from one another. The chi-squared value is 6,900, suggesting that the two distributions are not statistically independent at the p � 0.001 level. Thus, our results reveal that plug-in clusters from the combination of APIs using TOM and clusters from the texts (i.e., descriptions and tags) of plug-ins are statistically related to each other. Table B.6 shows the popular topics and keywords for each cluster. Table B.6 includes the list of frequently used keywords that describe each cluster, the list of most representative plug-ins, and the list of frequently used external APIs used in each cluster.

Table B.5. Examples of External APIs in the Regular Core and Periphery

<table><tr><td>External APIs in the regular core</td><td>External APIs in the periphery</td></tr><tr><td>Amazon S3, Facebook, Flicker, Gravatar, Google Maps, Instagram, LinkedIn, Twitter Search, YouTube</td><td>Bitly.ly, Dribbble, Eventbrite, Fitbit, Google Geocoding, Instapaper Yahoo PlaceFinder</td></tr></table>

## B.5. Product Categorization Using Similarity of Word Embeddings

In the previous section, we use LDA to identify the robustness of product functional categories based on the descriptions and tags of plug-ins. Because LDA is an unsupervised learning procedure without ground truth included, the number of product categories may be still in doubt if the description and tag do

Table B.6. Plug-in Categorization Using LDA, Description, and Tags

<table><tr><td>Category</td><td>Category name</td><td>Plug-in name</td><td>Most frequent keywords</td><td>Frequently used external APIs</td></tr><tr><td>1</td><td>E-commerce (gray section in TOM)</td><td>woocommerce, jigoshop placester, recipepress-reloaded, bigcommerce</td><td>Cart, shopping, online, store, featured</td><td>Google Maps, Google Picasa, YouTube</td></tr><tr><td>2</td><td>Topic taxonomy (Turquoise)</td><td>pods, organize series, permastructure, custom post type, toolset types</td><td>Contents, category, related, customization, list</td><td>Amazon S3, Google Font, Gravatar</td></tr><tr><td>3</td><td>Social media (blue)</td><td>wordpress social login, tweetpost, topical tweets, simple social icons, o3 social share</td><td>Social, network, sharing, bookmarking, activity</td><td>Facebook Real-time updates, Twitter, Bloglines</td></tr><tr><td>4</td><td>Gallery (brown)</td><td>nextgen, foogallery, nemus slider, microblog poster, envira</td><td>Image, photo, video, import, thumbnail</td><td>Facebook, Flicker, Instagram</td></tr><tr><td>5</td><td>Form builder (yellow)</td><td>gravity form, formidable, appointment booking, cubepm, olark for wordpress</td><td>Message, email, portfolio, jquery form</td><td>Twitter Summize, Twitter Search, Amazon S3</td></tr><tr><td>6</td><td>Widget (green)</td><td>wordpress popular post, single page sidebars, custom sidebars, content aware sidebars, mailchimp</td><td>Widget, sidebar, dashboard, testimonial, quote</td><td>Google Chart, Google Font, Google Ajax Search</td></tr><tr><td>7</td><td>Client portal (red)</td><td>membership, wordpress client, client dash, learndash, membermouse</td><td>Administration, profile, login, authentication, security</td><td>Gravatar, Flicker, LinkedIn</td></tr><tr><td>8</td><td>Navigation (black)</td><td>megamenu, page scroll to id, wordpress responsive, wordpress navigation filter, smarter navigation</td><td>Navigation, menu, header, buttons, XML</td><td>AddThis Menu, Google Ajax Search, Google Geocoding</td></tr><tr><td>9</td><td>Web syndication (pink)</td><td>wordpress rss aggregator, feed wordpress, blog networking, category specific rss feed menu, featured image</td><td>Feed, RSS, recent, dynamic, copy</td><td>Yahoo Weather, Amazon S3, Facebook</td></tr><tr><td>10</td><td>Search engine optimization (magenta)</td><td>squirrely seo, seo press, google keyword, google search, yeast seo fix for qtranslate</td><td>Search, analytics, statistics, redirect, sitemap</td><td>Twitter, Gravatar, Google Ajax Search</td></tr><tr><td>11</td><td>Content management (purple)</td><td>wordpress mobile pack, debug objects, wordpress google authenticator, spell checker, adminer</td><td>Formatting, template, HTML, CSS, PHP</td><td>Google Font, Google Chart, Google Analytics</td></tr></table>

Table B.7. Plug-in Categorization Using Doc2Vec

<table><tr><td>Category</td><td>Category name</td><td>Keywords</td></tr><tr><td>1</td><td>E-commerce</td><td>Cart, shopping, payment, store, marketing</td></tr><tr><td>2</td><td>Topic taxonomy</td><td>Contents, category, taxonomy, customization, type</td></tr><tr><td>3</td><td>Social media</td><td>Social, network, sharing, bookmarking, like</td></tr><tr><td>4</td><td>Gallery</td><td>Image, photo, video, slideshow, thumbnail</td></tr><tr><td>5</td><td>Form builder</td><td>Message, email, notification, contact, form</td></tr><tr><td>6</td><td>Widget</td><td>Widget, sidebar, dashboard, testimonial, display</td></tr><tr><td>7</td><td>Client portal</td><td>Admin, profile, registration, users, security</td></tr><tr><td>8</td><td>Navigation</td><td>Navigation, menu, theme, bar, slider</td></tr><tr><td>9</td><td>Web syndication</td><td>Feed, RSS, shortcode, cache, embed</td></tr><tr><td>10</td><td>Search engine optimization</td><td>Search, analytics, statistics, tracking, sitemap</td></tr><tr><td>11</td><td>Content management</td><td>Formatting, style, HTML, CSS, syntax</td></tr></table>

not contain accurate confirmation about the product functions. Hence, we use a word-embedding method (i.e., Doc2- Vec) to obtain robust statistical support in a neural network framework (Le and Mikolov 2014, Qiao et al. 2020). We use the same data used for LDA in Section B.4. Unlike LDA, Doc2Vec forms a vector space of plug-ins driven by the cooccurrences of words used across the descriptions and tags of plug-ins. Doc2Vec conduct a pairwise comparison between plug-ins in a vector space to find the semantic similarity of functions described by developers. Therefore, if the clustering results of TOM using API data statistically match with those of Doc2Vec using descriptions and tags, we can establish the robust validity of functional categorization of plug-ins.

We take the following steps to conduct the functional categorization of plug-ins using Doc2Vec. First, we construct the feature matrix of plug-ins using descriptions and tags in a vector space. The distributed representation of plug-ins is associated with the co-occurrences of similar words in their descriptions and tags (Le and Mikolov 2014). We create all possible pairs of plug-ins based on their cooccurrences of words to find if plug-ins share similar words with their neighboring plug-ins to describe functionality. For the randomness of plug-in comparisons, we apply skip-gram and continuous bag-of-words in a neural network framework. We then use K-means clustering to categorize plug-ins, based on the cosine similarity of word cooccurrences in the description and tags. The clustering method classified plug-ins into 11 clusters depending on the nearest mean distance and variance from a center plug-in in each cluster. The three columns in Table B.7 show, for each cluster, the cluster labels and the most frequent keywords used in the description of plug-ins in the cluster, respectively. Keywords defined by developers for naming of tags have very high flexibility with out any unified standards. Hence, some developers may use keyword from a piece of information meta data good chosen informally and personally.

Finally, a chi-squared test is applied to the two different types of clusters from TOM and Doc2Vec in order to under stand if they are significantly different (or independent) from one another. The chi-squared value is 7,100, suggesting that the two distributions are not statistically independent at the p � 0.001 level. Thus, our results reveal that clusters identified by Doc2Vec using the descriptions and tags and clusters identified by TOM using API uses in plug-ins are not significantly different. In addition, another chi-squared test was applied to the two results from LDA and Doc2Vec to understand if they are statistically different from one another. The chi-squared value is 6,300, suggesting that the two distributions are not statistically independent at the p � 0.001 level. This shows that the product categorization using LDA and using Doc2Vec shows statistically constant results, and both are valid. More specifically, comparing with Table B.6, Table B.7 shows the similar labels and key words of 11 clusters.

## Appendix C. Additional Econometric Analyses C.1. Correlation Table

Table C.1. Correlation Among Variables

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td> $1. \log(Y_{it})$ </td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $2. \text{EXTR}_{i,t-1}$ </td><td>0.488</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $3. \text{NFC}_{i,t-1}$ </td><td>0.420</td><td>0.263</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $2. \text{CC}_{i,t-1}$ </td><td>0.334</td><td>0.339</td><td>0.167</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td> $3. \text{RC}_{i,t-1}$ </td><td>0.612</td><td>0.510</td><td>0.259</td><td>0.095</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td> $6. \text{PER}_{i,t-1}$ </td><td>0.657</td><td>0.535</td><td>0.357</td><td>0.537</td><td>0.278</td><td>1</td><td></td><td></td><td></td></tr><tr><td> $7. \text{DPP}_{i,t-1}$ </td><td>0.064</td><td>-0.164</td><td>-0.158</td><td>0.388</td><td>0.018</td><td>-0.071</td><td>1</td><td></td><td></td></tr><tr><td> $8. \text{VU}_{i,t-1}$ </td><td>0.525</td><td>0.396</td><td>0.273</td><td>0.476</td><td>0.479</td><td>0.484</td><td>0.024</td><td>1</td><td></td></tr><tr><td> $9. \text{PAG}_{i,t-1}$ </td><td>-0.590</td><td>-0.339</td><td>-0.238</td><td>-0.738</td><td>-0.119</td><td>-0.794</td><td>-0.374</td><td>-0.450</td><td>1</td></tr></table>

Table C.2. Marginal Effects of New Functional Category and External API Ratio

<table><tr><td>External API ratio</td><td>New functional category</td><td>Predicted marginal effect</td></tr><tr><td>0</td><td>0</td><td>1.910 (0.027)</td></tr><tr><td>0</td><td>1</td><td>2.160 (0.027)</td></tr><tr><td>1</td><td>0</td><td>3.183 (0.335)</td></tr><tr><td>1</td><td>1</td><td>1.528 (0.266)</td></tr></table>

## C.2. Marginal Effects

To complement Figure 4 in the manuscript, the data in Table C.2 show a significant difference in the expected marginal effects on product variety as the ratio of the external APIs in the regular core for each cluster type increases. In particular, as the external API ratio increases, the predicted marginal effects on product variety likewise increase from 1.910 to 3.183 in the case of an existing cluster. In addition, as external API ratio increases, the predicted marginal effects on product variety decrease from 2.160 to 1.528 in the case of a newly generated cluster. Taken together, these results support Hypothesis 3.

C.3. The Effect of All External APIs on Product Variety We examine the effect of all external APIs on product variety and control for external APIs in the regular core. The results are shown in Table C.3. The coefficient of all external APIs is positive and insignificant, whereas that of external APIs in the regular core is still positive and significant (p < 0.01). External APIs can be in both the regular core and the periphery layers, and those in different layers have different impact on product variety. The regular core external APIs construct the key functions of products while adding functional varieties. They show high use frequency with strong spillover effects on other external APIs in increasing product variety. On the contrary, the periphery APIs do not increase product variety because they are not frequently used in building key functions of plug-ins within a functional category. Although periphery external APIs increase, such increase does not affect product variety. Hence, the regular core external APIs are the only type of APIs that can increase product variety. Additionally, given our extensive robustness checks in the paper, we do not believe that endogeneity is an issue in our model.

Table C.3. Estimation of All External APIs on Product Variety

<table><tr><td>DV:  $\log(Y_{it})$ </td><td>Estimates</td></tr><tr><td>All External  $APIs_{i,t-1}$ </td><td>0.008(0.007)</td></tr><tr><td>Regular Core External  $APIs_{i,t-1}$ </td><td>0.014***(0.005)</td></tr><tr><td> $DPP_{i,t-1}$ </td><td>-0.160(0.540)</td></tr><tr><td> $VU_{i,t-1}$ </td><td>0.001**(0.001)</td></tr><tr><td> $PAG_{,i,t-1}$ </td><td>-0.004(0.004)</td></tr><tr><td>Constant</td><td>0.967(0.635)</td></tr><tr><td>Observation</td><td>422</td></tr><tr><td>Number of groups</td><td>11</td></tr><tr><td> $R^2$ </td><td>0.631</td></tr><tr><td>Category fixed effects</td><td>Yes</td></tr><tr><td>Time fixed effects</td><td>Yes</td></tr><tr><td>Control variables</td><td>Yes</td></tr><tr><td>Robust standard error</td><td>Yes</td></tr></table>

\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

Table C.4. Estimation of External APIs on Product Variety Within Each Functional Category

<table><tr><td>Category</td><td>Category name</td><td>Coefficient for  $EXTR_{i,t-1}$ </td><td>Coefficient for  $EXTR_{i,t-1} \times NFC_{i,t-1}$ </td></tr><tr><td>1</td><td>E-commerce</td><td>1.081**(0.531)</td><td>-2.194**(1.035)</td></tr><tr><td>2</td><td>Topic taxonomy</td><td>0.978**(0.466)</td><td>-2.047**(0.952)</td></tr><tr><td>3</td><td>Social media</td><td>1.604**(0.805)</td><td>-1.552**(0.712)</td></tr><tr><td>4</td><td>Gallery</td><td>1.759**(0.883)</td><td>-1.538**(0.774)</td></tr><tr><td>5</td><td>Form builder</td><td>1.863**(0.922)</td><td>-1.734**(0.728)</td></tr><tr><td>6</td><td>Widget</td><td>1.845**(0.897)</td><td>-1.567**(0.653)</td></tr><tr><td>7</td><td>Client portal</td><td>1.937**(0.924)</td><td>-1.492**(0.734)</td></tr><tr><td>8</td><td>Navigation</td><td>0.884**(0.396)</td><td>-2.011**(0.858)</td></tr><tr><td>9</td><td>Web syndication</td><td>0.793**(0.324)</td><td>-2.213**(0.979)</td></tr><tr><td>10</td><td>Search engine optimization</td><td>0.641**(0.293)</td><td>-2.308**(1.156)</td></tr><tr><td>11</td><td>Content management</td><td>0.536**(0.248)</td><td>-2.406**(1.162)</td></tr></table>

\*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.001.

## C.4. The Effect of External APIs Across Functional Categories

We examine the effect of external APIs across 11 functional categories to more deeply understand the results shown in Table 5 and discussed in Section 5.5. First, we test Hypothesis 2 in all 11 product categories. The results are shown in Table C.4, column (1). In brand-new functional categories with many imitated products, such as navigation, the effect of external APIs on product variety is lower, represented by smaller coeffi cients. When the category contains mostly existing products, such as gallery, the effect of external APIs on product variety is higher, represented by larger coefficients. All the coefficients of $E X T R _ { I , t - 1 }$ across 11 categories distribute around the aggregated effect 1.274 (SD � 0.453), suggesting that all 11 coefficients come from the same distribution, confirming the robustness of the results in column (1) in Table 5. The results once more confirm the weakening effect of new functional categories on the impact of external APIs on product variety.

## Appendix D. Linear Independence in a Bipartite Network

We model the WordPress ecosystem as a bipartite network, which can be represented as a binary adjacency matrix B (Larremore et al. 2014), which is shown as follows. We define the API as a type a vertex and the plug-in as a type b vertex. Arcs starting from one API ending at some plug-ins mean an API is used to build multiple plug-ins, whereas arcs starting from a plug-in ending at some APIs mean a plug-in contains multiple APIs. The vertex size of the API is K and that of the plug-in is H. The dimensions of the bipartite network N × N, where $N = K + H$

$$
\mathbf {B} = \left[ \begin{array}{c c c c c c c c} \cdot & \cdot & \cdot & \cdot & b _ {1 1} & b _ {1 2} & \dots & b _ {1 H} \\ \cdot & \cdot & \cdot & \cdot & b _ {2 1} & b _ {2 2} & \dots & b _ {2 H} \\ \cdot & \cdot & \cdot & \cdot & \vdots & \vdots & \ddots & \vdots \\ \cdot & \cdot & \cdot & \cdot & b _ {K 1} & b _ {K 2} & \dots & b _ {K H} \\ b _ {1 1} & b _ {1 2} & \dots & b _ {1 K} & \cdot & \cdot & \cdot & \cdot \\ b _ {2 1} & b _ {2 2} & \dots & b _ {2 K} & \cdot & \cdot & \cdot & \cdot \\ \vdots & \vdots & \ddots & \vdots & \cdot & \cdot & \cdot & \cdot \\ b _ {H 1} & b _ {H 2} & \dots & b _ {H K} & \cdot & \cdot & \cdot & \cdot \end{array} \right]
$$

$$
\text { where } b _ {i j} = \{0, 1 \}.
$$

In the matrix, component (1) of the B matrix represents the API adjacency matrix at $K \times K .$ Component $( 2 )$ of the B matrix represents the plugin adjacency matrix at $H \times H$ Components (1) and (2) are both zero matrices.

$$
\left[ \begin{array}{c c c c} b _ {1 1} & b _ {1 2} & \dots & b _ {1 K} \\ b _ {2 1} & b _ {2 2} & \dots & b _ {2 K} \\ \vdots & \vdots & \ddots & \vdots \\ b _ {H 1} & b _ {H 2} & \dots & b _ {H K} \end{array} \right].
$$

The lower off-diagonal component (shown here) of matrix $\mathbf { B } ,$ $\{ b _ { i j } \}$ , defines the connections from the API mode network to the plugin mode network. Its size is $H \times K$ . This matrix is the same as $\mathbf { P } _ { t } ,$ , the API–product matrix in our network model in Section 3.1 and on Section A.1 in the appendix. The definition of $\mathbf { P } _ { t }$ in our model is given a follows:

$$
\mathbf {P} _ {t} = \left[ \begin{array}{c} \mathbf {I} _ {t} \\ \mathbf {E} _ {t} \end{array} \right] = \left[ \begin{array}{c c c c} \overrightarrow {I _ {1 t}} & \overrightarrow {I _ {2 t}} & \ldots & \overrightarrow {I _ {K t}} \\ \overrightarrow {E _ {1 t}} & \overrightarrow {E _ {2 t}} & \ldots & \overrightarrow {E _ {K t}} \end{array} \right] = \left[ \begin{array}{c c c c} b _ {1 1} & b _ {1 2} & \dots & b _ {1 K} \\ b _ {2 1} & b _ {2 2} & \dots & b _ {2 K} \\ \vdots & \vdots & \ddots & \vdots \\ b _ {H 1} & b _ {H 2} & \dots & b _ {H K} \end{array} \right].
$$

From $\mathbf { P } _ { t } ,$ we can then derive the plug-in adjacency matrix, $\mathbf { A } _ { t } ,$ and the TOM $\mathbf { } { \mathbf { } } { \mathbf { } } \mathbf { W } _ { t } ,$ from which we ultimately derive our response: product variety. $\mathbf { P } _ { t }$ is a more direct and concise representation than the bipartite network.

However, if our response Y and a major predictor $X$ are generated from the same bipartite network, there can be a concern that vectors Y and $\hat { X }$ are linearly dependent. If so, the projection of network B onto Y and $\mathrm { { \dot { Y } ^ { \prime } s } }$ projection back onto $X ,$ denoted as $X ^ { \prime } ,$ , generate the same network as $X ,$ that is, $X = X ^ { \prime } ,$ or a multiple of it, that is, $X ^ { \prime } = a X .$ . As we demonstrate in two different ways, this is not the case in our context, and X and $X ^ { \prime }$ are linearly independent.

## D.1. Method 1: Linear Independence in a Bipartite Network

Suppose that we have a bipartite network B (see Figure D.1). We define the unipartite network at the left as having the type X node, in which each node takes a label of $X _ { i } .$ The size of the X node is $n .$ The unipartite network at the right has the type Y node, in which each node has a label of $Y _ { j }$ . The size of the Y node is m. Because the aforementioned predictor is generated from the type X network, for the convenience of nota tion, we also use $\bar { X }$ to refer to the predictor variable and use $X _ { i }$ to represent an observation of variable $X ,$ whose value is also represented as $X _ { i } .$ Similarly, Y also represents the response, and $Y _ { j }$ represents the value of an observation of variable Y.

Figure D.1. An Example of a Bipartite Network with Two Types of Nodes, X and Y  
![](/api/attachments/ADHBP92X/fulltext/images/41a0c8fbf0d45d4e89d5e4160b231ee9402eb986528499a011692d918effe103.jpg)

Bipartite networks only allow connections between two nodes of different types. For the convenience of representa tion, they are usually converted to a one-mode projection in which only the relations among one type of nodes are shown. The one-mode projection ensures that the network only con tains one type of node: either X or Y. Two X nodes are connected only when they have at least one common neighboring Y node and vice versa (Zhou et al. 2007). Because the projection only contains information about one type of node, all the arcs (i.e., directed edges) in the projection need to be weighted. In Figure D.1, $w _ { i j }$ is the weight of the arc from $X _ { i }$ to $Y _ { j } ,$ measuring the proportion of the value of the $X _ { i }$ value contributing to $Y _ { j } ,$ whereas $w _ { j i } ^ { \prime }$ represents the weight of the arc from $Y _ { j }$ to $X _ { i } ,$ measuring the proportion of the value of $Y _ { j }$ contributing to $X _ { i } .$ . It is not necessarily to have $w _ { i j } = w _ { j i } ^ { \prime }$

D.1.1. Project Network onto Y Dimension. First, to represent the values of Y using X, we project the bipartite network B onto the Y dimension. In a Y projection, the value of each $Y _ { j }$ can be represented by the weighted sum of $X _ { i }$ :

$$
Y _ {j} = \sum_ {i = 1} ^ {n} w _ {i j} X _ {i},
$$

where $w _ { i j }$ is the weight of the arc starting from $X _ { i }$ and ending at $Y _ { j } .$ . The arc has the direction of $Y$ projection (also called projecting onto the Y dimension), $X  Y .$ . The definition of $w _ { i j }$ is provided in the following equation:

$$
w _ {i j} := \left\{ \begin{array}{c} \frac {1}{\deg (X _ {i})} \text { if } X _ {i} \text { connects   to } Y _ {j} \\ 0 \text { otherwise. } \end{array} \right.
$$

Here, weight $w _ { i j }$ is the reciprocal of the degree of $X _ { i }$ if $X _ { i }$ connects to $Y _ { j }$ or zero otherwise.

D.1.2. Project Y Network Back onto X Dimension. To represent the new values for X using $Y , X ^ { \prime }$ , we need to project the type Y network back onto the X dimension. We define the transformation from the Y projection to X as the $X ^ { \prime }$ projection. The values of the new $\ { \bar { X } } , \ { \bar { X } } _ { i } ^ { \prime } ,$ , can be described as the weighted sum of $Y _ { j }$ :

$$
X _ {i} ^ {\prime} = \sum_ {j = 1} ^ {m} w _ {j i} ^ {\prime} Y _ {j}.
$$

Replacing $Y _ { j }$ using the old value of $X _ { i }$ in $X ^ { \prime }$ projection, we get

$$
X _ {i} ^ {\prime} = \sum_ {j = 1} ^ {m} w _ {j i} ^ {\prime} \sum_ {i = 1} ^ {n} w _ {i j} X _ {i},
$$

where $w _ { j i } ^ { \prime }$ is the weight of the arc starting from $Y _ { j }$ and ending at $X _ { i }$ . The arc has the same direction as the $X ^ { \prime }$ projection, $Y  X ^ { \prime }$

$$
w _ {j i} ^ {\prime} := \left\{ \begin{array}{l l} \frac {1}{\deg (Y _ {j})} & \text { if   } Y _ {j} \text {   connects   to   } X _ {i} \\ 0 & \text { otherwise } \end{array} \right.,
$$

where weight $w _ { j i } ^ { \prime }$ is the reciprocal of the degree of $Y _ { j } \operatorname { i f } Y _ { j }$ connects to $X _ { i }$ or zero otherwise.

D.1.3. Linear Independence Between X and Y. To prove that vectors Y and X are not linearly dependent, we need to demonstrate that vectors X and $X ^ { \prime }$ are linearly independent. To accomplish this goal, we first give the matrix representation of the transformation from X to $X ^ { \prime }$ :

$$
\left[ \begin{array}{c} X _ {1} ^ {\prime} \\ X _ {2} ^ {\prime} \\ \vdots \\ X _ {n} ^ {\prime} \end{array} \right] = T (X) \left[ \begin{array}{c} X _ {1} \\ X _ {2} \\ \vdots \\ X _ {n} \end{array} \right]
$$

$$
= \left[ \begin{array}{c c c c} T _ {1 1} & T _ {1 2} & \dots & T _ {1 n} \\ T _ {2 1} & T _ {2 2} & \dots & T _ {2 n} \\ \vdots & \vdots & \ddots & \vdots \\ T _ {n 1} & T _ {n 2} & \dots & T _ {n n} \end{array} \right] \left[ \begin{array}{c} X _ {1} \\ X _ {2} \\ \vdots \\ X _ {n} \end{array} \right],
$$

where the elements of the transformation matrix T can be defined as the summation of weights from Y and X projections:

$$
\mathbf {T} = \left\{T _ {a b} \right\} = \left\{\sum_ {j = 1} ^ {m} w _ {j a} ^ {\prime} w _ {b j} \right\}.
$$

Once we replace the elements $T _ { a b }$ with the summation of weights, we have the following transformation:

$$
\left[ \begin{array}{c} X _ {1} ^ {\prime} \\ X _ {2} ^ {\prime} \\ \vdots \\ X _ {n} ^ {\prime} \end{array} \right] = \left[ \begin{array}{c c c c} \sum_ {j = 1} ^ {m} w _ {j 1} ^ {\prime} w _ {1 j} & \sum_ {j = 1} ^ {m} w _ {j 1} ^ {\prime} w _ {2 j} & \dots & \sum_ {j = 1} ^ {m} w _ {j 1} ^ {\prime} w _ {n j} \\ \sum_ {j = 1} ^ {m} w _ {j 2} ^ {\prime} w _ {1 j} & \sum_ {j = 1} ^ {m} w _ {j 2} ^ {\prime} w _ {2 j} & \dots & \sum_ {j = 1} ^ {m} w _ {j 2} ^ {\prime} w _ {n j} \\ \vdots & \vdots & \ddots & \vdots \\ \sum_ {j = 1} ^ {m} w _ {j n} ^ {\prime} w _ {1 j} & \sum_ {j = 1} ^ {m} w _ {j n} ^ {\prime} w _ {2 j} & \dots & \sum_ {j = 1} ^ {m} w _ {j n} ^ {\prime} w _ {n j} \end{array} \right] \left[ \begin{array}{c} X _ {1} \\ X _ {2} \\ \vdots \\ X _ {n} \end{array} \right].
$$

The transformation matrix is the very weighted adjacency matrix we use to demonstrate the association between vectors X and X<sup>′</sup>. If X and Y are generated through the same mechanism in the same bipartite network, then X and its transformed back, $X ^ { \prime } ,$ , are linearly dependent. This is due to the theorem of transformation matrix (Williams 2017)

Theorem D.1. Let T be a transformation matrix for vector X, X ∈ R<sup>n</sup>. If T is linearly independent, then vector X and its transformation ${ \dot { X ^ { \prime } } }$ are also linearly independent.

Hence, to prove the linear independence between X and $X ^ { \prime } ,$ we need to prove that the transformation matrix, T, is lin early independent. We introduce Theorems D.2 and D.3, regarding linear independence of vectors (Williams 2017).

Theorem D.2. Let A be an n × n matrix. If A’s determinant is not zero, then A is linearly independent. Otherwise, A is linearly dependent.

Theorem D.3. Let A be an n × n matrix. If A has two identical rows or columns, then the determinant of A is equal to zero.

From Theorems D.2 and D.3, we can get Corollary D.1

Corollary D.1. Let A be an n × n matrix. If A does not have identical rows or columns, then it is linearly independent

From Corollary D.1, we get that the transformation matrix, T, is linearly dependent only when two rows or two columns in the matrix are the same (Williams 2017). For example, define two randomly selected rows from T, a and b:

$$
r o w _ {a} (\mathbf {T}) = \left[ \sum_ {j = 1} ^ {m} w _ {j a} ^ {\prime} w _ {1 j} \quad \sum_ {j = 1} ^ {m} w _ {j a} ^ {\prime} w _ {2 j} \quad \dots \quad \sum_ {j = 1} ^ {m} w _ {j a} ^ {\prime} w _ {n j} \right],
$$

$$
r o w _ {b} (\mathbf {T}) = \left[ \sum_ {j = 1} ^ {m} w _ {j b} ^ {\prime} w _ {1 j} \quad \sum_ {j = 1} ^ {m} w _ {j b} ^ {\prime} w _ {2 j} \quad \dots \quad \sum_ {j = 1} ^ {m} w _ {j b} ^ {\prime} w _ {n j} \right].
$$

Equation row $\mathbf { \varepsilon } _ { a } ( \mathbf { T } ) = r o w _ { b } ( \mathbf { T } )$ stands when each pair of elements in two rows are the same:

$$
\sum_ {j = 1} ^ {m} w _ {j a} ^ {\prime} w _ {k j} = \sum_ {j = 1} ^ {m} w _ {j b} ^ {\prime} w _ {k j} (1 \leq k \leq n, k \in \mathbb {Z})
$$

in order to make the equation stand, meaning to satisfy $r o w _ { a } ( \mathbf { T } ) = r o w _ { b } ( \mathbf { T } )$ . This implies that multiple plug-ins have the same coding components (APIs), which is not realistic in the real-world scenario as every plug-in has at least one or more unique coding component.

See the hypothetical bipartite network in Figure D.2. $X _ { a }$ and $X _ { b }$ are APIs both used to create plug-ins $Y _ { 1 } { - } \bar { Y } _ { 3 } ,$ , and they are the only two APIs used. So we have $w _ { 1 a } ^ { \prime } + w _ { 2 a } ^ { \prime } + w _ { 3 a } ^ { \prime } = w _ { 1 b } ^ { \prime } +$ $\begin{array} { r } { w _ { 2 b } ^ { \prime } + w _ { 3 b } ^ { \prime } = \frac { 1 } { 2 } + \frac { 1 } { 2 } + \frac { 1 } { 2 } } \end{array}$ . In the WordPress context, it means that the multiple plug-ins are built by only two APIs or the same group of APIs. According to our definition, if three plug-ins, $\stackrel { \smile } { Y } _ { 1 } - \stackrel { \bullet } { Y } _ { 3 } ,$ , contain the same two APIs, they are identical and have the same function. Thus, $Y _ { 1 } { - } Y _ { 3 }$ are ultimately the same product. This condition does not fit with our context as two plugins cannot be made using the same APIs (this is also validated in our data).

The situation when two randomly selected columns are identical, $c o l _ { c } ( \mathbf { T } ) = c o l _ { d } ( \mathbf { T } )$ , follow the preceding proof regarding identical rows after we transpose the matrix T.

Figure D.2. A Hypothetical Bipartite Network for Illustrating Two Identical Rows Existing in Transformation Matrix T  
![](/api/attachments/ADHBP92X/fulltext/images/b4b083f93ac666630ce46a0049520acf6a0c05b5313dec253452bb652af48266.jpg)

In summary, in our context, $r o w _ { a } ( \mathbf { T } )$ ≠ $r o w _ { b } ( \mathbf { T } )$ and $c o l _ { c } ( \mathbf { T } )$ $\neq c o l _ { d } ( \mathbf { T } )$ , which means there are no plug-ins always built by only the same two APIs, and there are no two APIs having the same use count by all the plug-ins. Thus, our transformation matrix T is always linearly independent. Therefore, our predictor X is always linearly independent with $X ^ { \prime } ,$ the Y projection back to X. Although our model can be indirectly represented by a bipartite network, we still find that X and Y are linearly independent within this network.

Moreover, deriving two variables from the projections of a bipartite network onto two dimensions is an appropriate and widely used method. For example, Yang et al. (2021) use a customer-brand bipartite network to derive the similarity between customers by the common brands they favor and define the similarity between brands by common users who all own the brands.

## D.2. Method 2: Reprocessing of Predictor Using Indicator Function

In the previous section, we prove that two variables derived from the projections of one bipartite network on different dimensions are not linearly dependent. Our actual situation is stricter because one of the two variables is not directly derived from the projection of the bipartite network. We take a different approach to deriving our response and the major predictor. In our circumstance, we only use the Y projection (onto the plug-in) to derive the number of product clusters and use it as the response. For the X dimension (API), we use an indicator function to transform it into a ternary variable before deriving our predictor (Sections 3.2 and A.3). The indicator function is defined as follows:

$$
\mathbf {1} _ {r} (X _ {i}) := \left\{ \begin{array}{l l} 1 & \text { if } 0. 9 5 <   r \leq 1. \\ 2 & \text { if } 0. 8 0 <   r \leq 0. 9 5, \\ 3 & \text { if } r \leq 0. 8 0. \end{array} \right.
$$

$$
\mathrm{where} r = \sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {m} \frac {a _ {i j} a _ {j i} ^ {\prime}}{n},
$$

$$
a _ {i j} := \left\{ \begin{array}{l} 1 \text {   if   } X _ {i} \text {   connects   to   } Y _ {j} \\ 0 \text {   otherwise. } \end{array} \right.
$$

$$
a _ {j i} ^ {\prime} := \left\{ \begin{array}{l} 1 \text {   if   } Y _ {j} \text {   connects   to   } X _ {i} \\ 0 \text {   otherwise.   } \end{array} \right.
$$

And n is the total number of APIs, and m is the total number of plug-ins.

In our approach, two vectors can be linearly dependent if and only if they are collinear $( \mathrm { i . e . } ,$ , one is a scalar multiple of the other). $\bar { Y } _ { i }$ represents the degree of product variety measured by the number of subclusters within each category. $X _ { i }$ implies the number of external APIs used in the regular core within a particular product category. In the following example, $\gamma ^ { ' }$ is a scalar multiple of $\overrightarrow { X } , s o \overrightarrow { Y }$ and $\overrightarrow { X }$ are linearly dependent:

$$
\left[ \begin{array}{c} Y _ {1} \\ Y _ {2} \\ \vdots \\ Y _ {n} \end{array} \right] = a \left[ \begin{array}{c} X _ {1} \\ X _ {2} \\ \vdots \\ X _ {n} \end{array} \right].
$$

If an indicator function $\mathbf { 1 } _ { r } ( \cdot )$ is applied to each $X _ { i } ,$ , then we have

$$
\left[ \begin{array}{c} \mathbf {1} _ {r} (X _ {1}) \\ \mathbf {1} _ {r} (X _ {2}) \\ \vdots \\ \mathbf {1} _ {r} (X _ {n}) \end{array} \right].
$$

$\mathbf { 1 } _ { r } ( X _ { i } )$ is not linearly dependent on $Y _ { i }$ :

$$
\left[ \begin{array}{c} Y _ {1} \\ Y _ {2} \\ \vdots \\ Y _ {n} \end{array} \right] \neq a \left[ \begin{array}{c} \mathbf {1} _ {r} (X _ {1}) \\ \mathbf {1} _ {r} (X _ {2}) \\ \vdots \\ \mathbf {1} _ {r} (X _ {n}) \end{array} \right].
$$

Because of the transformation function, which is a nonlinear function, the indicator does not lead to the proportional relationships between X and Y. Thus, in our WordPress context, plug-in product variety is linearly independent with API use frequency category. A numeric value cannot be linearly dependent on a categorical value (Krzanowski 1975).

In summary, we confirm that our response and the major predictor are clearly linearly independent. This is demonstrated in the case of the projections of a bipartite network based on our network approach. Therefore, our empirical model is free of the endogeneity issue that is present when the dependence between the response and the major predictor is linear.

## Endnotes

<sup>1</sup> APIs are a set of functions and procedures that allow for the creation of applications that access data and features of other applications, services, or operating systems.

<sup>2</sup> Because a plug-in is a specific type of digital product that we empirically investigate in this paper, we only use the term “plug-$\mathrm { i n } ^ { \prime \prime }$ when we are referring to specific digital products that we examine in this study. The term “digital products” is used when we refer to it as a theoretical construct.

<sup>3</sup> In our context of WordPress, software components are APIs, whereas products are plug-ins. Thus, we use “software component” and “API” interchangeably and “product” and “plug-in” interchangeably.

4 Developers do write their own software codes that integrate these APIs and add additional functionalities and user interfaces. In this paper, however, we foreground the role of existing APIs in order to understand their role in the dynamics of a platform ecosystem and background local codes written by developers as we are focusing on the role of APIs in the product variety of platform ecosystems. We validate this combinatorial design approach through interviews with expert developers.

<sup>5</sup> It is worthwhile to point out that our phenomenon can also be modeled as a bipartite network in which APIs and plug-ins are two types of nodes. Arcs connect different types of nodes and never between the same type. Because the response and predictor are derived from the same network, people may suspect that linear dependence exists between these two variables. We prove that the two variables derived from projections onto two dimensions are lin early independent. For the detailed proof, please see Appendix D.

<sup>6</sup> People may suspect information loss when we project the bipartite network onto the API dimension. The information about the extent to which APIs are used to build plug-ins can be lost. However, following the core–periphery model by Borgatti and Everett (2000), we use the 1-entry ratio to represent the cooccurrences of APIs. Thus, information loss is not a concern in our situation.

<sup>7</sup> Because of space limitations, we include the calculations of all matrices involved in Appendix A.

## References

Abernathy WJ, Utterback JM (1978) Patterns of industrial innovation. Tech. Rev. 80(7):40–47.

Acemoglu D, Autor DH, Lyle D (2004) Women, war, and wages: The effect of female labor supply on the wage structure at midcentury. J. Political Econom. 112(3):497–551.

Adner R, Kapoor R (2010) Value creation in innovation ecosystems: How the structure of technological interdependence affects firm performance in new technology generations. Strategic Management J. 31(3):306–333.

Aggarwal CC, Reddy CK(2014) Data clustering. Algorithms and Applications, CRC Data Mining and Knowledge Discovery Series (Chapman Hall, London).

Anderson P, Tushman ML (1990) Technological discontinuities and dominant designs: A cyclical model of technological change. Admin. Sci. Quart. 604–633.

Arellano M, Bond S (1991) Some tests of specification for panel data: Monte Carlo evidence and an application to employment equations. Rev. Econom. Stud. 58(2):277–297.

Arellano M, Bover O (1995) Another look at the instrumental variable estimation of error-components models. J. Econometrics 68(1):29–51.

Arthur WB (2009) The Nature of Technology: What It Is and How It Evolves (Free Press, New York).

Bakken TE, Jorstad NL, Hu Q, Lake BB, Tian W, Kalmbach BE, Crow M (2021) Comparative cellular analysis of motor cortex in human, marmoset and mouse. Nature 598(7879):111–119.

Baldwin CY, Clark KB (2000) Design rules. The power of modular ity, vol. 1 (MIT Press, Cambridge, MA).

Baldwin C, Clark KB (2006) The architecture of participation: Does code architecture mitigate free riding in the open source devel opment model? Management Sci. 52(7):1116–1127.

Baldwin C, MacCormack A, Rusnak J (2014) Hidden structure: Using network methods to map system architecture. Res. Policy 43(8): 1381-1397

Barde BV, Bainwad AM (2017) An overview of topic modeling methods and tools. Internat. Conf. Intelligent Comput. Control Systems (IEEE).

Battke B, et al. (2016) Internal or external spillovers—Which kind of knowledge is more likely to flow within or across technologies. Res. Policy 45(1):27–41.

Belsley DA, Kuh E, Welsch RE (2005) Regression Diagnostics: Identify ing Influential Data and Sources of Collinearity (John Wiley & Sons, New Jersey).

Bertrand M, Duflo E, Mullainathan S (2004) How much should we trust differences-in-differences estimates? Quart. J. Econom. 119(1):249–275.

Blei DM (2012) Probabilistic topic models. Comm. ACM. 55(4):77–84

Blundell R, Bond S (1998) Initial conditions and moment restrictions in dynamic panel data models. J. Econometrics 87(1):115–143.

Borgatti S, Everett MG (2000) Models of core/periphery structures. Soc. Networks 21(4):375–395.

Boudreau KJ (2012) Let a thousand flowers bloom? An early look at large numbers of software app developers and patterns of innovation. Organ. Sci. 23(5):1409–1427.

Boudreau KJ, Jeppesen LB (2015) Unpaid crowd complementors: The platform network effect mirage. Strategic Management J. 36(12):1761–1777.

Boudreau KJ, Lakhani KR (2015) “Open” disclosure of innovations, incentives and follow-on reuse: Theory on processes of cumula tive innovation and a field experiment in computational biology. Res. Policy 44(1):4–19.

Brunswicker S, Almirall E, Majchrzak A (2019) Optimizing and satisficing: The interplay between platform architecture and producers’ design strategies for platform performance. Management Inform. Systems Quart. 43(4):1249–1277.

Brynjolfsson E, McAfee A (2014) The Second Machine Age: Work, Progress, and Prosperity in a Time of Brilliant Technologies (WW Norton & Company, New York).

Burford N, Shipilov AV, Furr NR (2021) How ecosystem structure affects firm performance in response to a negative shock to interdependencies. Strategic Management J. 43(1):30–57.

Caves RE (2000) Creative Industries: Contract Between Art and Com merce (Harvard Business School Press, Cambridge, MA).

Cennamo C, Santalo J (2013) Platform competition: Strategic trade-off in platform markets. Strategic Management J. 34(11):1331–1350.

Clauset A, et al. (2004) Finding community structure in very large networks. Phys. Rev. E 70(6):066111.

Csermely P, London A, Wu L-Y, Uzzi B (2013) Structure and dynam ics of core/periphery networks. J. Complex Networks 1(2):93–123.

Doncheva NT, Assenov Y, Domingues FS, Albrecht M (2012) Topological analysis and interactive visualization of biological networks and protein structures. Nature Protocols 7(4):670–685.

Doreian P, Batagelj V, Ferligoj A (2005) Generalized Blockmodeling (Cambridge University Press, Cambridge, UK).

Eaton B, Elaluf-Calderwood S, Sørensen C, Yoo Y (2015) Distributed tuning of boundary resources: The case of Apple’s iOS servic system. Management Inform. Systems Quart. 39(1):217–243.

Eisenmann T, Parker G, Van Alstyne M (2011) Platform envelop ment. Strategic Management J. 32(12):1270–1285.

Eppinger SD, Whitney DE, Smith RP, Gebala DA (1994) A modelbased method for organizing tasks in product development. Res. Engrg. Design 6(1):1–13.

Ethiraj SK, Levinthal D (2004) Modularity and innovation in com plex systems. Management Sci. 50(2):159–173.

Fleming L (2001) Recombinant uncertainty in technological search. Management Sci. 47(1):117–132.

Fleming L, Sorenson O (2001) Technology as a complex adaptive system: Evidence from patent data. Res. Policy 30(7):1019–1039.

Fleming L, Sorenson O (2004) Science as a map in technological search. Strategic Management J. 25(8–9):909–928.

Fleming L, Mingo S, Chen D (2007) Collaborative brokerage, generative creativity, and creative success. Admin. Sci. Quart. 52(3):443–475.

Foerderer J (2020) Interfirm exchange and innovation in platform ecosystems: Evidence from Apple’s Worldwide Developers Con ference. Management Sci. 66(10):4772–4787.

Foerderer J, Kude T, Mithas S, Heinzl A (2018) Does platform owner’s entry crowd out innovation? Evidence from Google Photos. Inform. Systems Res. 29(2):444–460.

Fortuna MA, Bonachela JA, Levin SA (2011) Evolution of a modular software network. Proc. Natl. Acad. Sci. U.S.A. 108(50):19985–19989.

Friedman TL (2017) Thank You for Being Late: An Optimist’s Guide to Thriving in the Age of Accelerations. (Picador, New York).

Gallagher RJ, Young JG, Foucault Welles B (2021) A clarified typology of core-periphery structure in networks. Sci. Adv. 7(12):eabc9800.

Garud R, Kumaraswamy A (1995) Technological and organizational designs for realizing economies of substitution. Strategic Management J. 16(S1):93–109.

Gawer A, Cusumano MA (2002) Platform Leadership: How Intel, Microsoft, and Cisco Drive Industry Innovation (Harvard Business School Press, Boston).

Ghazawneh A, Henfridsson O (2013) Balancing platform control and external contribution in third-party development: The boundary resources model. Inform. Systems J. 23(2):173–192.

Gong J, Abhishek V, Li B (2018) Examining the impact of keyword ambiguity on search advertising performance: A topic model approach. Management Inform. Systems Quart. 42(3):805–830.

Greene WH (2003) Econometric Analysis (Pearson Education, India).

Haefliger S, Von Krogh G, Spaeth S (2008) Code reuse in open source software. Management Sci. 54(1):180–193.

Hagiu A (2014) Strategic decisions for multisided platforms. MIT Sloan Management Rev. 55(2):71.

Hansen LP (1982) Large sample properties of generalized method of moments estimators. Econometrica: J. Econometric Society 1029–1054.

Hawrylycz MJ, Lein ES, Guillozet-Bongaarts AL, Shen EH, Ng L, Miller JA, van de Lagemaat LN, et al. (2012) An anatomically comprehensive atlas of the adult human brain transcriptome. Nature 489(7416):391–399.

Helfat CE, Raubitschek RS (2018) Dynamic and integrative capabil ities for profiting from innovation in digital platform-based eco systems. Res. Policy 47(8):1391–1399.

Henderson RM, Clark KB (1990) Architectural innovation: The reconfiguration of existing product technologies and the failure of established firms. Admin. Sci. Quart. 35(1):9–30.

Horvath S (2011) Weighted Network Analysis: Applications in Genomics and Systems Biology (Springer Verlag, Berlin).

Imbens GW (2000) The role of the propensity score in estimating dose-response functions. Biometrika 87(3):706–710.

Jacobides MG, Cennamo C, Gawer A (2018) Towards a theory of ecosystems. Strategic Management J. 39(8):2255–2276.

Kauffman SA (1993) The Origins of Order: Self Organization and Selec tion in Evolution (Oxford University Press, New York).

Kleis L, Chwelos P, Ramirez RV, Cockburn I (2012) Information technology and intangible output: The impact of IT investment on innovation productivity. Inform. Systems Res. 23(1):42–59.

Kojaku S, Masuda N (2017) Finding multiple core-periphery pairs in networks. Phys. Rev. E 96(5):052313.

Kojaku S, Masuda N (2018) Core-periphery structure requires something else in the network. New J. Phys. 20(4):043012.

Krzanowski WJ (1975) Discrimination and classification using both binary and continuous variables. J. Amer. Statist. Assoc. 70(352): 782–790.

Kyriakou H, Nickerson JV, Sabnis G (2017) Knowledge reuse for customization: Metamodels in an open design community for 3D printing. Management Inform. Systems Quart. 41(1):315–322.

Lancaster K (1990) The economics of product variety: A survey. Marketing Sci. 9(3):189–206.

Langfelder P, Horvath S (2008) WGCNA: An R package for weighted correlation network analysis. BMC Bioinformatics 9(1):559.

Larremore DB, et al. (2014) Efficiently inferring community structure in bipartite networks. Phys. Rev. E 90(1):012805.

Laursen K, Salter A (2006) Open for innovation: The role of open ness in explaining innovation performance among UK manufacturing firms. Strategic Management J. 27(2):131–150.

Laursen K, Salter AJ (2014) The paradox of openness: Appropriability, external search and collaboration. Res. Policy 43(5):867–878.

Le Q, Mikolov T (2014) Distributed representations of sentences and documents. Internat. Conf. Machine Learn., PMLR

Levinthal DA (1997) Adaptation on rugged landscapes. Management Sci. 43(7):934–950.

Levinthal DA, March JG (1993) The myopia of learning. Strategic Management J. 14(2):95–112.

Levinthal DA, Marino A (2015) Three facets of organizational adaptation: Selection, variety, and plasticity. Organ. Sci. 26(3):743–755.

Lifshitz-Assaf H (2018) Dismantling knowledge boundaries at NASA: The critical role of professional identity in open innovation. Admin. Sci. Quart. 63(4):746–782.

Lyytinen K, Rose G, Yoo Y (2010) Learning routines and disruptive technological change. Inform. Tech. People 23(2):165–192.

MacCormack A, Rusnak J, Baldwin CY (2006) Exploring the structure of complex software designs: An empirical study of open source and proprietary code. Management Sci. 52(7):1015–1030.

Manning C, et al. (2014) The Stanford CoreNLP natural language processing toolkit. Proc. 52nd Annual Meeting Assoc. Comput. Linguistics: System Demonstrations.

Mousavi R, Gu B (2019) The impact of Twitter adoption on lawmakers’ voting orientations. Inform. Systems. Res. 30(1):133–153.

Murmann JP, Frenken K (2006) Toward a systematic framework for research on dominant designs, technological innovations, and industrial change. Res. Policy 35(7):925–952.

Musalem A, Olivares M, Bradlow ET, Terwiesch C, Corsten D (2010) Structural estimation of the effect of out-of-stocks. Management Sci. 56(7):1180–1197.

Newell A, Simon HA (1972) Human Problem Solving (Prentice-Hall Englewood Cliffs, NJ).

Papoulis A, Saunders H (1989) Probability, Random Variables and Sto chastic Processes (McGraw-Hill, New York).

Parker G, Van Alstyne MW (2005) Two-sided network effects: A theory of information product design. Management Sci. 51(10):1494–1504.

Parker G, Van Alstyne MW, Jiang X (2017) Platform ecosystems: How developers invert the firm. Management Inform. Systems Quart. 41(1):255–266.

Qiao D, Lee SY, Whinston AB, Wei Q (2020) Financial incentives dampen altruism in online prosocial contributions: A study of online reviews. Inform. Systems Res. 31(4):1361–1375.

Ramsey JB (1969) Tests for specification errors in classical linear leastsquares regression analysis. J. Roy. Statist. Soc. B 31(2):350–371.

Rajarajan P, Borrman T, Liao W, Schrode N, Flaherty E, Casin˜ osamuel Powell C, Yashaswini C, et al. (2018) Neuron-specific signatures in the chromosomal connectome associated with schizophrenia risk. Sci. 362(6420):eaat4311.

Ravasz E, Baraba´si AL (2003) Hierarchical organization in complex networks. Phys. Rev. E 67(2):026112.

Ravasz E, Somera AL, Mongru DA, Oltvai ZN, Baraba´si AL (2002) Hierarchical organization of modularity in metabolic networks Sci. 297(5586):1551–1555.

Rishika R, Ramaprasad J (2019) The effects of asymmetric social ties, structural embeddedness, and tie strength on online content contribution behavior. Management Sci. 65(7):3398–3422.

Rombach MP, Porter MA, Fowler JH, Mucha PJ (2014) Core-periphery structure in networks. SIAM J. Appl. Math. 74(1):167–190

Schubert C et al. (2013) The means of managing momentum: Bridging technological paths and organisational fields. Res. Polic 42(8):1389–1405.

Simon HA (1996) The Sciences of the Artificial (MIT Press, Cambridge, MA).

Sosa ME, Eppinger SD, Rowles CM (2004) The misalignment of product architecture and organizational structure in complex product development. Management Sci. 50(12):1674–1689.

Sosa ME, Mihm J, Browning TR (2013) Linking cyclicality and product quality. Manufacturing Service Oper. Management 15(3): 473–491.

Stanko MA (2016) Toward a theory of remixing in online innovation communities. Inform. Systems Res. 27(4):773–791.

Tiwana A (2015) Evolutionary competition in platform ecosystems. Inform. Systems Res. 26(2):266–281.

Tiwana A (2018) Platform synergy: Architectural origins and com petitive consequences. Inform. Systems Res. 29(4):829–848.

Tushman ML, Rosenkopf L (1992) Organizational determinants of technological-change-toward a sociology of technological evolution. Res. Organ. Behav. 14:311–347.

Von Hippel E, Von Krogh G (2003) Open source software and the ‘private-collective’ innovation model: Issues for organization science. Organ. Sci. 14(2):209–223.

Wilkie FG, Kitchenham BA (2000) Coupling measures and change ripples in C++ application software. J. Systems Software 52(2–3): 157-164.

Williams G (2017) Linear Algebra with Applications (Jones & Bartlett Learning).

Xue L, Song P, Rai A, Zhang C, Zhao X (2019) Implications of ap plication programming interfaces for third-party new app

development and copycatting. Production Oper. Management 28(8):1887–1902.

Yang Y, Zhang K, Kannan PK (2021) Identifying market structure: A deep network representation learning of social engagement J. Marketing 86(4).

Yip AM, Horvath S (2007) Gene network interconnectedness and the generalized topological overlap measure. BMC Bioinformatics 8(1):22.

Yoo Y, Henfridsson O, Lyytinen K (2010) Research commentary— The new organizing logic of digital innovation: An agenda for information systems research. Inform. Systems Res. 21(4): 724–735.

Yoo Y, Boland RJ, Lyytinen K, Majchrzak A (2012) Organizing for innovation in the digitized world. Organ. Sci. 23(5):1398–1408.

Zhang B, Gaiteri C, Bodea LG, Wang Z, McElwee J, Podtelezhnikov AA, Zhang C, Xie T (2013) Integrated systems approach identifies genetic nodes and networks in late-onset Alzheimer’s dis ease. Cell 153(3):707–720.

Zhao W, Langfelder P, Fuller T, Dong J, Li A, Hovarth S (2010) Weighted gene coexpression network analysis: State of the art J. Biopharmaceutical Statist. 20(2):281–300.

Zhou T, et al. (2007) Bipartite network projection and personal rec ommendation. Phys. Rev. E 76(4):046115.

Zhou YM, Wan X (2017) Product variety, sourcing complexity, and the bottleneck of coordination. Strategic Management J. 38(8):1569–1587.

C<sub>opy</sub>ri<sub>g</sub>ht 2023 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
