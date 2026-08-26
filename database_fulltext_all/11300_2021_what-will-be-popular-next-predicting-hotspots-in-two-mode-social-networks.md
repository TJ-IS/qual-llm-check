---
otero_id: 11300
otero_key: "GDDXMZEF"
title: "What Will Be Popular Next? Predicting Hotspots in Two-Mode Social Networks"
authors: "Zhepeng (Lionel) Li; Yong Ge; Xue Bai"
year: "2021"
journal: "MIS Quarterly"
doi: "10.25300/misq/2021/15365"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# WHAT WILL BE POPULAR NEXT? PREDICTING HOTSPOTS IN TWO-MODE SOCIAL NETWORKS<sup>1</sup>

Zhepeng (Lionel) Li Area of Innovation and Information Management, Faculty of Business and Economics, The University of Hong Kong, Pokfulam, HONG KONG {lionelzlee@gmail.com}

Yong Ge Department of Management Information Systems, Eller College of Management, University of Arizona, Tucson, AZ, U.S.A. {yongge@arizona.edu}

Xue Bai Department of Marketing and Supply Chain Management and Department of Management Information Systems, Fox School of Business, Temple University, Philadelphia, PA, U.S.A. {xue@temple.edu}

In social networks, social foci are physical or virtual entities around which social individuals organize joint activities, for example, places and products (physical form) or opinions and services (virtual form). Forecasting which social foci will diffuse to more social individuals is important for managerial functions such as marketing and public management operations. In terms of diffusive social adoptions, prior studies on user adoptive behavior in social networks have focused on single-item adoption in homogeneous networks. We advance this body of research by modeling scenarios with multi-item adoption and learning the relative propagation of social foci in concurrent social diffusions for online social networking platforms. In particular, we distinguish two types of social nodes in our two-mode social network model: social foci and social actors. Based on social network theories, we identify and operationalize factors that drive social adoption within the two-mode social network. We also capture the interdependencies between social actors and social foci using a bilateral recursive process— specifically, a mutual reinforcement process that converges to an analytical form. Thus, we develop a gradient learning method based on a mutual reinforcement process that targets the optimal parameter configuration for pairwise ranking of social diffusions. Further, we demonstrate analytical properties of the proposed method such as guaranteed convergence and the convergence rate. In the evaluation, we benchmark the proposed method against prevalent methods, and we demonstrate its superior performance using three real-world data sets that cover the adoption of both physical and virtual entities in online social networking platforms.

Keywords: Popularity prediction, social diffusion, machine learning, mutual reinforcement, online social networks

## Introduction

Recent developments in mobile technology have facilitated the use of social networking platforms to bridge online interactions and offline behaviors. These services allow users to share offline activities with their online friends through adoptive behaviors on mobile devices. The adopted entities may be in either physical or virtual forms and include places visited, products consumed, books read, and opinions accepted (Bao et al. 2012; Liu et al. 2012). For example, location-based service providers such as Facebook Places, Foursquare, and Meetup empower users to connect online with friends and share their check-ins to real-life places, and Indigo Books & Music Inc., the largest Canadian bookstore chain, has launched a mobile social networking platform that allows readers to share their opinions about books with friends and maintain online reading lists that express their book-reading intentions in a virtual form. Social readership platforms are developing quickly and the economic scale of global location-based services will approach \$61 billion by 2022, up from \$11 billion in 2014 (Malani 2017).

These social networking services constitute a multimodal social network setting in which a set of connected entities are adopted by a network of social individuals. In accordance with social focus theory, we consider the adopted entities to be social foci, or a set of explicitly or implicitly shared affiliations around which social life is organized, which, in turn, facilitate interactions among social actors (Feld 1981). Social actors are individual users of social networking platforms. Contagious adoption stems from the interaction between social actors and social foci and, as a result, social foci gain popularity when their adoptions propagate among social actors. A question of great interest for both research and practice is: How can information about social networking be leveraged to predict which social foci will be popular in the future? The proposed question emphasizes the fact that social foci coexist and that contagious adoption of social networks causes some to become more popular.

This study falls in the research domain of social diffusion (Valente 1996; Centola 2010). Prior IS and related academic studies have approached the social diffusion problem from various perspectives, including diffusion modeling (Valente 1996; Hosanagar et al. 2010), seeding actor selection (Kempe et al. 2003), adopter identification (Hill et al. 2003), viral product design (Aral and Walker 2011) and adoption probability prediction (Fang et al. 2013). Although both descriptive and predictive models have been proposed, the literature has predominantly focused on single-item diffusion, or the adoption of a single independent social focus. Consequently, the multiitem diffusion problem, in which concurrent diffusions of multiple social foci can attract the same user base, remains unresolved. Existing diffusion models appoint singlemode or bipartite network settings, which partially account for the interplay among actor-actor, focus-focus, and actor-focus relationships. In addition, researchers have found that peer effects among connected individuals characterize the contagious spreading of adoptive behavior (Aral et al. 2009; Fang et al. 2013). However, the effects across different types of social entities have yet to be defined and operationalized. More importantly, given a multifocus social diffusion scenario, adoptions of social foci will spread out interdependently among different social entities. Hence, an interactive model is desirable for capturing within-mode and cross-mode effects for multimodal social networks. We therefore aim to fill these research gaps by addressing multifocus social diffusion through an interactive propagation model and inferring the relative popularity of social foci.

However, beyond the academic relevance of this issue, the ability to predict popular social hotspots is also critical for practice domains such as marketing and public management. Predicting the popularity ranking of businesses would be useful for the advertising strategies of online social networking platforms, e.g., Yelp, YouTube, and Facebook, that display advertisements about related businesses or items. The profitability of such display advertisements depends on the click-through rate (CTR). Popularity estimation, which is widely adopted for prioritizing display ads and targeting personalized ads, is essential to boosting CTR. Considering the sheer number of online visits, a small increase in the CTR could result in substantial revenue growth (John et al. 2018). Future hotspots can also be leveraged in public security management. For example, rather than profiling individuals for their propensity to potential crimes, identifying hotspot areas where crimes may occur in the future is an effective strategy for allocating police resources (Kennedy et al. 2011). Given limitations in resources and personnel, police departments have adopted prediction-based decision support systems to efficiently distribute police officers, (Camacho-Collados and Liberatore 2015). Popularity assessment could also be used to support decision-making regarding optimal store placement (Karamshuk et al. 2013) and point-of-interest recommendations (Li et al. 2016) and can advance our understanding of human mobility (González et al. 2008, Song et al. 2010). As such, our research question has both academic and practical significance.

![](/api/attachments/GDDXMZEF/fulltext/images/a228b5736d51d122f05cf114c5c2d2a74b753d0d54e54a60faee4a6308d3af61.jpg)  
Figure 1. An Illustrative Example of Two-Mode Social Network

However, answering the proposed research question presents several methodological challenges. Figure 1 illustrates the challenges of multifocus social diffusion in its depiction of a two-mode social network model that captures the relations among the two types of social entities (Wasserman and Faust 1994): social foci (the square nodes) and social actors (the round nodes). Social actors are connected by social ties (the solid links), while ties among social foci can be attributed to activity-based connections or proximity-based connections. Social actors can also repeatedly adopt social foci (the solid arrow). In the context of the multimodal social network setting, there are several interesting theoretical challenges involved with studying the relative propagation of social foci.

First, social actors influence peers to adopt multiple social foci that coexist and compete. Thus, the adoptive diffusion of social foci depends not only on peer influences among individual social actors (Kempe et al. 2003, Aral et al. 2009, Fang et al. 2013) and characteristics of the target social focus (Aral and Walker 2011) but also on other competing social foci. For example, when social actor $v _ { 1 }$ decides whether to adopt social focus $f _ { 1 }$ (the dashed arrow), actor $v _ { 1 }$ is under the social influence of direct friend $v _ { 2 }$ who has visited $f _ { 1 }$ . At the same time, $v _ { 1 }$ is also influenced by $v _ { 2 }$ and $v _ { 3 }$ who have both visited $f _ { 2 } ^ { \mathrm { ~ ~ } }$ , and is also influenced by $v _ { 4 }$ and $v _ { 5 }$ who have both visited $f _ { 3 }$ . Therefore, the influences coming from different peers that favor competing social foci should not be ignored. Prior research models of user-level adoptions have examined one focus at a time and largely neglected peer influences even though multiple social foci exist.

Second, social foci facilitate interaction among social actors and thereby gain attractiveness. According to social focus theory (Feld 1981), social actors choose social foci to host joint activities with others. When choosing social foci, social actors conform to their local interaction needs (Feld 1981). Beyond peer effects, adoptive decisions can be attributed to the normative characteristics of social foci. Consequently, the attractiveness of a social focus for any social actor depends on the congruity between the social focus and the interacting parties. For example, the attractiveness of social focus $f _ { 1 }$ to $v _ { 1 }$ depends on the compatibility of $f _ { 1 }$ with the local interactions between $v _ { 1 }$ and $v _ { 1 } \mathrm { { ' s } }$ friends. Taking the interaction between $( v _ { 1 } , v _ { 2 } )$ as an example, social focus $f _ { 1 }$ may be attractive to $v _ { 1 }$ because $v _ { 1 }$ and $v _ { 2 }$ have both visited $f _ { 2 } ,$ a focus connected to $f _ { 1 }$

As stated above, social influences drive social actors to adopt foci (Hill et al. 2003, Aral et al. 2009, Fang et al. 2013); in turn, social foci accommodate interactions and thereby attract actors to propagate in the social network (Feld 1981; Kossinets and Watts 2006; Golder et al. 2007; Rivera et al. 2010). Such a feedback mechanism suggests that the peer influences among social actors for adopting social foci and the attractiveness of social foci for engaging social actors are contingent upon each other, a mutual dependency that has remained unaddressed in prior social diffusion studies. To the best of our knowledge, existing learning methods that estimate contagious adoptions do not account for the mutual dependency between social actors and social foci. Based on our motivations and research gap identified above we formulate the following research problem: Given a social network of social actors and social foci, as well as adoptive behavior by social actors toward social foci by time ??, social foci should be ranked according to popularity at time $t + 1$

In solving the formulated problem, our contribution to the literature is threefold. First, we propose a general two-mode social network model to capture the multifocus social diffusions articulated by our novel research question. Rooted in theoretical foundations, we operationalize driving factors for within-mode and cross-mode effects of social diffusions in the proposed networking model. Second, we formulate a bilateral recursive process that encodes the interactive propagation mechanism between social actors and social foci, and we show that the proposed process converges to an analytical form. Third, we propose a machine-learning method to predict the ranking resulting from contagious spreading based on the convergence state of the bilateral process. We also consider related issues such as the efficiency bound and hidden factors. The evaluations we conduct use real data sets on location visiting and book reading intentions.

## Related Work

Our work is related to research on user-level adoption in a social network setting. Research on social adoption has found that social diffusion underlies initial adoptions (Iyengar et al. 2011) as well as the postadoptive repeats (Iyengar et al. 2015). Factors such as social influence, homophily, and structural equivalence may drive the sustained use of physical and virtual items (Aral and Walker 2011; Fang et al. 2013; Li et al. 2017a). However, most current work has studied the adoption of a single item, and less attention has been paid to the coexistence of multiple items that share the same user base. In addition, few prior studies have addressed the impact of the adoption of different items on social interactions among individuals. Based on the different methods that have been used, related studies can be broadly categorized into unsupervised approaches and supervised learning methods. In the following subsections, we review representative methods in each category.

## Unsupervised Methods

Unsupervised approaches are primarily found in web analysis and diffusion modeling. In web analysis, rankingbased methods have been developed to estimate the relative importance of interconnected entities (e.g., web pages). For example, PageRank (Page 1997), HITS (Kleinberg 1999) and other variants (Li et al. 2002; Gleich 2015) were developed to gauge the importance of hyperlinked websites. Beyond single-mode networks, augmented ranking methods have been proposed to handle distinct groups of networked nodes (Rui et al. 2007, Deng et al. 2009, Cao et al. 2011, Zeng et al. 2013). Rui et al. (2007) adapted the HITS algorithm to rank the importance of nodes in a bipartite network, which is evaluated with web image annotation tasks, and devised an interesting initialization for the iterative updating of importance scores. Cao et al. (2011) improved entity ranking by introducing a generative probabilistic model that estimates initial scores based on the cooccurrence of entities. The importance scores are then propagated through an iterative refinement process. Deng et al. (2009) proposed the Co-HITS algorithm, which generalizes the HITS method by considering both sides of a bipartite graph and incorporating content and structural information for both sides as regularizations. This method has been shown to be useful in query-based searches.

Despite their successful applications in web analysis, ranking-based methods may not effectively address the focal research problem for several reasons. First, the results of ranking methods have limited use for predicting future importance; given current reference and/or citation relations, ranking methods focus on uncovering the implied importance of nodes during the same time period. As a result, the relative importance scores that are obtained do not necessarily apply to future time periods. Second, existing ranking methods have been developed for bipartite graphs, which differ from the general two-mode social networks in our study.<sup>2</sup> Although ranking methods have been extended to consider constraints in both sets of nodes (e.g., Deng et al. 2009), they largely neglect the interactions between multitype relations in two-mode social networks.

In addition, diffusion modeling studies the mechanisms for disseminating information or a product to a group of potential adopters (Bass 1969; Valente 1996, Kempe et al. 2003; Chen et al. 2010; Wang and Street 2018). A variety of models have been developed to capture the propagation of a single item; these can be divided into three groups: the Bass diffusion model (Bass 1969), the threshold model (Valente 1996; Chen et al. 2010; Wang and Street 2018), and the cascade model (Kempe et al. 2003; Leskovec et al. 2007). An analysis of the literature suggests that the Bass model estimates the distribution of initial adopters in a population and does not apply to the assessment of repeated adoptions at the individual level. The cascade model assumes one-time activation, which does not allow repeatable activation for social foci. Therefore, we have adopted threshold models for benchmarking. Despite successful application in social networks, existing social diffusion models target the propagation of one item at a time. They assume independence among the items to be disseminated, which should be relaxed for multifocus diffusion where items are spreading out interdependently. Diffusion models rely on heuristic mechanisms that can be enhanced by incorporating supervised learning components, e.g., parameter configurations, which we discuss next.

## Supervised Methods

Related supervised learning methods have been developed in two streams of studies. One stream of research stems from link prediction. Link prediction methods address the problem of how likely it is that interactions will be formed, given a snapshot of a social network (Liben-Nowell and Kleinberg 2007). Link prediction methods estimate the likelihood of future linkage occurrence between two social entities (Liben-Nowell and Kleinberg 2007; Lichtenwalter et al. 2010; Backstrom and Leskovec 2011).

More recently, link prediction methods have begun to explore heterogeneous social networks that are comprised of multityped social nodes and/or multityped social relations. Multityped link prediction is a nontrivial problem compared to its homogeneous counterpart (Sun and Han 2013). Studies in multityped link prediction have focused on addressing two crucial challenges: (1) how to incorporate multityped relations and/or multipartite nodes and define predictors accordingly, and (2) how to build and configure a predictive model from the obtained predictors. Benchettara et al. (2010) projected bipartite social networks onto unimodal graphs and extracted topological features from the projected networks. The predictive features were incorporated in decision tree models that learn linkage probabilities. Davis et al. (2011) used a probabilistic weighting scheme to aggregate multiple social relations based on their likelihood of occurring. Lichtenwalter et al. (2010) employed a flow-based classifier with bagging to estimate the linkage probabilities. To infer the types of heterogeneous links, Tang et al. (2012) proposed using triad-based patterns derived from social theories and incorporated them into a graph-based probabilistic model. Yang et al. (2012) addressed link prediction in multipartite social networks. This work extended an independent cascade model by weighing different relations based on asymmetric correlations, and the obtained features were used to build a logistic regression classifier. Considering multityped social nodes and relations, Gong et al. (2014) formulated a social-attribute network. The authors redefined topological features such as common neighbor, the Adamic/Adar index, random walk, and low-rank approximation, and then provided the redefined features as inputs to support vector machine (SVM) classifiers.

The focal two-mode social network is comprised of two distinct social nodes and two relations, and the popularity of a social focus can be viewed as the aggregation of potential adoptions by individuals and thus estimated by accumulating the predicted linkage likelihoods from individuals to that focus. However, link prediction methods cannot be effectively applied to our problem, for two main reasons. On the one hand, a careful aggregation of linkage probabilities is required to gauge the popularity of social foci. This aggregation step is nontrivial, especially when the link prediction methods suffer from relatively low accuracy, which is further exacerbated as the problem scales up (Li et al. 2017b). On the other hand, heterogeneous link predictions focus on generalizing multipartite nodes and multityped relations and mapping them to homogeneous models, but the existing methods largely ignore any mutual dependence across different entity groups and relations.

The second stream of supervised learning research has been developed in studies on recommending points of interest (POIs) for location-based social networks (LBSNs). Two clusters of methods have been proposed to predict LBSN location visits. The first cluster consists of classificationbased methods (Basu et al. 1998, Wang et al. 2013, Liu et al. 2016) in which classifiers are trained by user-location pairs. A training instance is labeled as positive when the user has visited the corresponding location; otherwise, it is labeled as negative. Features such as geographic distance and profile similarity are extracted for each user-location pair. The prediction task is to infer the class label for an incoming user-location pair. The second cluster focuses on predicting the next venue for individuals using rankingbased methods (Noulas et al. 2012a, 2012b) and collaborative-filtering-based (CF) methods (Salakhutdinov and Mnih 2008; Koren and Bell 2015). Noulas et al. (2012a, 2012b) proposed inferring the next visits of individuals in a descending order of likelihood. They used popularity and other temporal-spatial features in classic prediction models, including linear regression, M5 model tree (Noulas et al. 2012a) and random walk (Noulas et al. 2012b). The idea behind CF methods is that a user will visit a location if similar users have visited it. The learning objective for CF methods can be formulated as minimizing the rating-based error (Salakhutdinov and Mnih 2008) or maximizing the pairwise ranking consistency (Rendle et al. 2009). One representative approach using CF-based methods is probabilistic matrix factorization (PMF)

(Salakhutdinov and Mnih 2008), in which users and locations are represented with k-dimensional hidden vectors that need to be learned from the data. The PMF model bridges the square error minimization and the Bayes learning framework. Extensions of PMF have been proposed to further probe the social influence, data sparseness, and cold-start issues (Ma et al. 2011, Koren and Bell 2015). Prior literature has found that CF-based methods can outperform random-walk-based and regression-based approaches in many cases (Li et al. 2017).

However, the use of such CF-based or classification-based methods for predicting popular social foci poses several difficulties. First, their learning objective is to predict the likelihood of one individual user visiting a social focus, which differs from a learning objective at an aggregated level such as the ranking of total visits of social foci. Second, in accordance to learning theory (Hastie et al. 2009), trivially aggregating the predicted likelihood at the individual level, such as summing up by social focus, often incurs significantly greater prediction errors than directly approximating an aggregated objective, such as the ranking of total visits by social focus. Consequently, because of the large number of users on networking platforms, aggregating the focus-adoption propensity obtained from the methods discussed above may cumulate the individual errors to an unacceptable amount. Thus, direct application of classification-based and CF-based methods cannot effectively address the proposed research problem.

## Predicting Popular Social Foci: Problem Formulation and Method

In this section, we define a two-mode social network that formalizes the inter-entity dependence between social foci and social actors as a mutual reinforcement process and then predicts the relative spread of the social diffusions of the social foci as an optimization problem based on the converged mutual reinforcement process.

## Two-Mode Social Network

Two-mode social networks are well suited for capturing interactions among two social entities; these can be defined as a graph $G = < V \cup F , ~ \tilde { E } >$ , where the nodes in $V \cup F$ are social entities and the edges ??<sup>̃</sup> are social relations. Unlike one-mode social networks, the nodes in our twomode social network are social entities from two distinct sets, i.e., ?? and ??, where $V = \{ v _ { i } \} \ \mathrm { f o r } \ i = 1 , 2 , \dots , N$ is a set of social actors and $F = \{ f _ { h } \}$ for $h = 1 , 2 , \dots , M$ is a set of social foci. The social relations ??<sup>̃</sup> bridge the paired social entities. Two-mode social networks can have two types of social relations (Wasserman and Faust 1994), which we refer to as within-mode and cross-mode relations. While the within-mode relations connect social entities from the same set (either ?? or ??), cross-mode relations are only established across the sets of social entities. A two-mode social network can have two types of cross-mode links, namely, directional and nondirectional links. For example, a user’s visits to a place or a company’s outreaches to a customer are directional, as the relation is one-way. In contrast, phone calls between an individual and an organization can be encoded by nondirectional links for two-way communications. In our study, we use directional cross-mode links from social actors to social foci to account for the one-way relation of adoptive behavior. Thus, we use the augmented set of edges $\tilde { E } = \{ E _ { a } \cup E _ { f } \cup E _ { c } \}$ to define (in order) actor-actor, focus-focus and actor-focus relations. Stated concretely, we let $e _ { i j } \in E _ { a } = \{ V \times V \}$ represent a within-mode link connecting social actors $( v _ { i } , v _ { j } ) \in V ,$ , we let $\boldsymbol { e } _ { g h } \in E _ { f } = \{ \boldsymbol { F } \times \boldsymbol { F } \}$ represent the other type of within-mode link connecting social foci $\left( f _ { g } , f _ { h } \right) \in F$ , and we let $\boldsymbol { e } _ { i h } \in E _ { c } = \{ V \times F \}$ denote a cross-mode link from a social actor to a social focus $( v _ { i } , f _ { h } )$ where $v _ { i } \in V$ and $f _ { h } \in F$ . Each social actor $v _ { i }$ has a profile that is denoted as a preference vector $w _ { i } = <$ $w _ { i 1 } , w _ { i 2 } , \dots , w _ { i s } >$ , where element $w _ { i s }$ is the weight that $v _ { i }$ assigns to preference item ??. The detailed implementation of preference vectors is deferred to Section 4.1, which describes how user profiles are realized from our collected data sets.

## Factor Identification and Operationalization

We performed an extended literature review on factors that drive social contagion. In accordance with the review, and incorporated in our two-mode social network model, there are four fundamental groups of driving factors: (1) persuasive influences that stem from actor-actor social links, (2) competitive influences that depend on social actors’ topological positions in the network, (3) intrinsic homophily that are based on actors’ characteristics and independent of the social network structure, and (4) foci compatibility that can be attributed to the organization of the two-mode linkage. In this study, we operationalized one factor for each category to constitute a concise set of representative features: social influence ??, structural equivalence ??, homophily ??, and social compatibility ??.

These factors are defined to capture direct impacts from adjacent neighborhoods, while the indirect impacts of both social actors and foci are accommodated by the mutual reinforcement process proposed in Section 3.3.

## Social Influence $I _ { i h }$

When perceptions and beliefs are socially communicated, social influence occurs through the interactions among people in the social context (Rice et al. 1990). Social influence constitutes an important force affecting individuals’ adoption behaviors in social networks (Ibarra and Andrews 1993; Leenders 2002; Bruyn and Lilien 2008; Shalizi and Thomas 2011). Social influence network theory (Friedkin 1998) further posits that initial adopters receive information that has been disseminated in a social network and accordingly update their original opinions and attitudes. These theories converge at the central role of network-based social influence in making adoption decisions. Social actors are enabled to learn and reflect on others’ choices or opinions via social ties (Wellman 1997). The magnitude of the resulting social influence reflects the strength of the social ties that connect the actors. Generally speaking, stronger social ties deliver greater social influences than weaker social ties (Levy 1992; Levy and Nail 1993).

To operationalize social influence, the social actors ?? are linked by social ties, which can be directional or nondirectional (Wasserman and Faust 1994). In this study, we consider nondirectional social ties. We use the edge $e _ { i j }$ as an indicator to denote the presence of a social tie connecting social actors $( v _ { i } , v _ { j } ) \in V$ , with $v _ { i } \neq v _ { j }$ . When a social tie exists between $( v _ { i } , v _ { j } )$ , edge $e _ { i j } = e _ { j i } = 1$ , and if there is no social tie, $e _ { i j } = e _ { j i } = 0$ . While the linkage is given by the social network, the strength of a social tie encodes the relative intensity of interactions, which can be directly given or indirectly inferred (Brown and Reingen 1987, Rice et al. 1990). In our case, the social tie strength that $v _ { i }$ receives from $v _ { j }$ is inferred as follows:

$$
t s _ {j i} = \frac {e _ {i j}}{\sum_ {v _ {z} \in V \backslash \{v _ {i} \}} e _ {i z}}\tag{1}
$$

Equation (1) gauges the social tie strength from ??<sub>??</sub> to $v _ { i }$ as the proportional social interaction between $v _ { i }$ and $v _ { j }$ in relation to the interactions that $v _ { i }$ has received from the network, i.e., $\textstyle \sum _ { v _ { z } \in V \backslash \{ v _ { i } \} } e _ { i z }$ . Thus, the tie strength measure $t s _ { j i }$ ranges over [0,1]. According to prevalent diffusion models of social networks (Granovetter 1978; Kleinberg 2007; Fang et al. 2013), social entities’ focus adoption decisions are affected by other social entities that have already adopted the focus in question. Let $V ( \cdot ) \subset V$ denote the set of individual adopters for a social focus, e.g., ??(ℎ) refers to the adopters of social focus $f _ { h }$ . Then, we can aggregate the social influences that persuade $v _ { i }$ to adopt $f _ { h }$ as shown in Equation (2):

$$
I _ {i h} = \sum_ {v _ {j} \in V (h)} t s _ {j i}\tag{2}
$$

## Structural Equivalence $\pmb { E } _ { i h }$

In addition to social influences, the structural characteristics of a social actor’s position in the social network also affect persuasive impacts on others’ opinions and behaviors (Burt 1987; Wejnert 2002; Fang et al. 2013; Fang and Hu 2016). Social contagion occurs when social actors use other structurally approximate peers to manage uncertainty regarding adoptions (Burt et al. 1994). Two social entities are structurally equivalent if they connect to the same set of other entities (Lorrain and White 1971; Wasserman and Faust 1994). By approaching structural equivalence, social actors maneuver into the same position in the social structure and thereby tend to exhibit similar opinions and behaviors, even in the absence of direct communication that connects them together (Burt 1987). As Burt (1987) notes, the spread of an opinion or behavior in a social network is contingent on how the structure of the network brings people together. If they connect to the same group of people, two social actors likely exhibit similarity in adoptions, because they are in similar circumstances and can avert uncertainty in adoptions by mimicking each other (Rice and Aydin 1991). Thus, people with highly comparable social ties exhibit similar opinions or behaviors.

Structural equivalence measures the extent of similarity between social entities in terms of the network structure (Wasserman and Faust 1994). Given a nondirectional social network, two social actors $( v _ { i } , v _ { j } ) \in V$ are structurally equivalent if the following condition is satisfied: For each social actor $v _ { z } \in V \backslash \{ v _ { i } , v _ { j } \}$ , if there is a social link between $v _ { i }$ and $v _ { z }$ then there is also a social link between $v _ { j }$ and $v _ { z } .$ . However, perfect structural equivalence is unusual in realistic social networks (Wasserman and Faust 1994). Therefore, we measure structural equivalence between social entities using similarity (or dissimilarity) functions (Wasserman and Faust 1994). A common measure used for structural equivalence is the Euclidean distance measure (Burt 1976). For a social network with nondirectional social ties, the Euclidean distance $d _ { i j }$ of structural equivalence between social actors $v _ { i }$ and $v _ { j }$ is defined as

$$
d _ {i j} = \sqrt {\sum_ {v _ {z} \in v \backslash \{v _ {i} , v _ {j} \}} \left(e _ {i z} - e _ {j z}\right) ^ {2}}\tag{3}
$$

The Euclidean distance $d _ { i j }$ measures structural dissimilarity between $v _ { i }$ and $v _ { j }$ for nondirectional social ties. The higher the value of $d _ { i j }$ , the less structural equivalence there is between $v _ { i }$ and $v _ { j }$ . Accordingly, we define social actor $v _ { j } { ' } \mathbf { s }$ structural equivalence effect on social actor $v _ { i }$ as

$$
e e _ {j i} = \frac {d _ {m a x} - d _ {i j}}{d _ {m a x} - d _ {m i n}},\tag{4}
$$

where $d _ { m a x }$ and $d _ { m i n }$ denote the maximum and the minimum Euclidean distance of structural equivalence, respectively. According to Equation (4), the higher the structural equivalence between $v _ { i }$ and ??<sub>??</sub> (i.e., the lower $d _ { i j }$ is), the more powerful $\vec { v _ { j } \cdot \mathbf { s } }$ impact on $v _ { i } { } ^ { \ , } s$ adoption decision (through the effect of structural equivalence on $v _ { i } )$ , consistent with structural equivalence theories (Burt 1987). Similar to Equation (2), the social-equivalencebased influences that convince social actors to adopt originate from previous adopters (Granovetter 1978; Kleinberg 2007; Fang et al. 2013). Given $e e _ { j i }$ for all $v _ { j } \in$ $V ( h )$ , we can aggregate the effect that stems from structure equivalence for social actor $v _ { i }$ ’s adoption of social focus $f _ { h }$ as

$$
E _ {i h} = \sum_ {v _ {j} \in V (h)} e e _ {j i}\tag{5}
$$

## Homophily $H _ { i h }$

Homophily, or the degree to which two entities in a social network are similar based on their intrinsic characteristics (McPherson et al. 2001; Jackson 2008), constitutes another important force underlying adoption behaviors (Salancik and Pfeffer 1978). All else being equal, people with similar characteristics such as personal preferences and tastes are more likely to have similar opinions and behaviors (Aral et al. 2009). Such similarity also implies common interests and worldviews; people with highly similar demographic characteristics thus exhibit similar needs, wants, preferences, and tastes (Ibarra 1992). Social homophily also entails a behavioral dimension, insofar as people with similar behavioral profiles express similar opinions and behave similarly toward new products or services (Ibarra 1992, Centola 2011). In addition, people who have responded to products (services) similarly in the past are more likely to continue to respond similarly in the future. Hence homophily impacts social actors’ likelihood of adoption, independent of their direct interactions (McPherson et al. 2001). The similarity of two social actors, as measured by their preference profiles could thus foster similar adoption behaviors, with more aligned preferences indicating greater similarity in future adoptions.

Thus, homophily among social actors can be gauged by entity similarity based on the proximity between their entity preference profiles (Hand et al. 2001). Let $o _ { i j }$ be the similarity between preference vectors ${ \pmb w } _ { i }$ and $w _ { j }$ given by

$$
o _ {i j} = \operatorname{sim} \big (\pmb {w} _ {i}, \pmb {w} _ {j} \big),\tag{6}
$$

where ${ \pmb w } _ { i }$ and $w _ { j }$ are the preference vectors for actors $v _ { i }$ and $v _ { j }$ , and ??????(⋅) is a similarity function. Choice of the similarity function is application specific (Crandell et al. 2008) and depends on the types of attributes in ${ \pmb w } _ { i }$ (Tan et al. 2006). For our case of multidimensional vectors, we use cosine similarity to define $o _ { i j }$ . Slightly different from the effect of structural equivalence, the homophily effect from social entity $v _ { j }$ to $v _ { i }$ is defined as

$$
h e _ {j i} = \frac {o _ {i j} - o _ {m i n}}{o _ {m a x} - o _ {m i n}},\tag{7}
$$

where $o _ { m a x }$ and $o _ { m i n }$ respectively denote the maximum and the minimum similarity between social entities. Congruent with theories concerning entity similarity (Ibarra 1992; Centola 2011), Equation (8) formalizes the observation that the higher the entity similarity between $v _ { i }$ and $v _ { j }$ , the more likely $v _ { i }$ will resonate with $v _ { j }$ in adoption behavior. Having specified $h e _ { j i }$ for $v _ { j } \in V ( h )$ we can now define the homophily factor (i.e., $H _ { i h } )$ that indicates the tendency for social entity $v _ { i }$ to adopt social focus $f _ { h }$ as follows:

$$
H _ {i h} = \sum_ {v _ {j} \in V (h)} h e _ {j i}\tag{8}
$$

## Social Compatibility $C _ { h i }$

Social interaction foci have been defined as a variety of explicitly or implicitly shared affiliations around which social life is organized, which in turn facilitate interactions among social actors (Feld 1981; Kossinets and Watts 2009). Whereas the idea of foci may involve geographic closeness (Fischer et al. 1977), the conceptualization of social foci goes well beyond the collectivities that are defined in terms of physical proximity (Feld 1981; Gieryn 2000; Grossetti 2005). The concept of social foci includes workplaces, clubs, groups, and other affiliations where preferential interests (Uzzi and Dunlap 2005), status (Moody 2001), and sentiments (Homans 1961; Feld 1981) are aligned, and further cultural attachment is induced through joint activities (Entwisle et al. 2007). Geographically dispersed social foci have recently become more important in organizing attachments, given that technological advances facilitate communication and, as a result, lower geographic barriers (Jones et al. 2008). Thus, it is widely accepted that the term “social foci” can refer to social, psychological, legal, or physical entities as long as they associate social actors for organizing joint activities and developing friendships (Feld 1981; Kleinbaum et al. 2008; Leskovec and Horvitz 2007).

Connected social actors are inclined to use social foci to organize joint activities, which may be subject to severe restrictions among individual social actors, such as time, effort, emotions, and preferences (Feld 1981). Connected social actors are motivated to find and develop social foci that cater to their existing social needs with their peers (Rivera et al. 2010). The process of developing social foci is facilitated by the social foci’s compatibility with the types of activities and social interactions desired by the social actors. For example, a cinema is generally more compatible with couples’ than co-workers’ needs, and beauty salons and spas are typically more compatible with women’s needs than men’s. The more compatible a social focus is, the more likely it is that targeted social actors will adopt it (Feld 1981).

Thus, social compatibility reflects the extent to which social foci are attractive to social actors. Social actors need to maintain peer connections via shared activities. The more compatible a social focus is with local social interactions, the more likely it is to be used (Feld 1981). To operationalize social compatibility, we let focus $f _ { h } \mathrm { ' s }$ neighborhood $N ( h ) = \{ f _ { g } | e _ { g h } = 1 \}$ be the set of social foci that $f _ { h }$ directly connects to via a within-mode relation $e _ { g h }$ . Let $F ( i ) \subset F$ be the set of social foci that $v _ { i }$ has adopted. We can measure the compatibility effect of social focus $f _ { h }$ in relation to the shared social foci between social actor $v _ { i }$ and their neighbor $v _ { j }$ as follows:

$$
c e _ {i j} (h) = \frac {| N (h) \cap F (i) \cap F (j) |}{| F (i) \cap F (j) |}\tag{9}
$$

where $c e _ { i j } ( h )$ is defined to be zero if $F ( i ) \cap F ( j ) = \phi$ According to Equation (9), social focus $f _ { h }$ is compatible with the local interactions of two connected social actors $( v _ { i } , v _ { j } )$ when its neighborhood coincides with foci in $F ( i ) \cap F ( j )$ . Having defined $c e _ { i j } ( h )$ , we can now aggregate over the neighborhood of $v _ { i }$ to obtain the social compatibility $C _ { h i }$ that entices $v _ { i }$ to adopt $f _ { h }$ as follows:

$$
C _ {h i} = \sum_ {v _ {j} \in \{v _ {z} | e _ {i z} = 1 \}} c e _ {i j} (h)\tag{10}
$$

where $v _ { j }$ is in the direct neighborhood of social actor $v _ { i }$ and hence $e _ { i j } = 1$ for all $v _ { j }$

## Mutual Reinforcement Process

Given the underlying factors, we can now formalize the interdependence between social foci and social actors. We denote the propensity of social actor $v _ { i }$ to adopt a given social focus $f _ { h }$ as $p _ { i h }$ , which is subject to multiple actorbased factors—namely, the social influence factor $I _ { i h } .$ , the structural equivalence factor $E _ { i h }$ and the social homophily factor $H _ { i h }$ . The propensity $p _ { i h }$ is defined as a weighted sum of these three factors:

$$
p _ {i h} = \pmb {\alpha} _ {i} ^ {T} \times \left[ \begin{array}{l} I _ {i h} \\ E _ {i h} \\ H _ {i h} \end{array} \right],\tag{11}
$$

where ${ \pmb { \alpha } } _ { i } ^ { T } = \left[ { \alpha } _ { i g } \right] ^ { T }$ for $g \in \{ 1 , 2 , 3 \}$ is a row vector of weight parameters whose configurations are to be learned from the data. The parameters $\alpha _ { i 1 } , \alpha _ { i 2 }$ , and $\alpha _ { i 3 }$ are the weight coefficients of $I _ { i h } , E _ { i h }$ , and $H _ { i h }$ , respectively, as operationalized by Equations (2), (5), and (8).

According to social focus theory, the attractiveness that a social focus $f _ { h }$ has for social actor $v _ { i }$ depends on how compatible $f _ { h }$ is with the local interactions around $v _ { i } .$ . The attractiveness $q _ { h i }$ is

$$
q _ {h i} = \beta_ {i} \times C _ {h i},\tag{12}
$$

where $\beta _ { i }$ is a weight parameter to be learned from the data and the focus-centered social compatibility $C _ { h i }$ given by Equation (10) gauges how compatible social focus $f _ { h }$ is with social actor $v _ { i }$

Aside from the identified factors, diffusive propagations in social networks can also be attributed to unobservable factors. Confounding factors constitute an important source of effects that render social interaction and contagion (Manski 1993; Van den Bulte and Lilien 2001; Iyengar et al. 2011). Confounding factors are generally considered unobservable (Aral et al. 2009; Aral and Walker 2011; Fang et al. 2013). Therefore, we capture confounding factors as hidden variables in our proposed model, which we formulate next.

Let the gregariousness score $X _ { i }$ be the aggregated tendency of $v _ { i }$ to be persuaded to adopt any social foci, and let the popularity score $Y _ { h }$ be the aggregated propensity of $f _ { h }$ to attract any social actors. Thus, the interdependence between $X _ { i }$ and $Y _ { h }$ constitutes a bilateral recursive process— specifically, a mutual reinforcement process, defined as follows:

$$
\left\{ \begin{array}{l} X _ {i} = \sum_ {h} p _ {i h} \times Y _ {h} + \phi_ {i}, \\ Y _ {h} = \sum_ {i} q _ {h i} \times X _ {i} + \gamma_ {h}, \end{array} \right.\tag{13}
$$

where $\phi _ { i }$ and $\gamma _ { h }$ are hidden factors. Based on Equation (13), the gregariousness score $X _ { i }$ is a weighted sum of actor $\boldsymbol { v } _ { i } { } ^ { \ ' } \boldsymbol { \mathfrak { s } }$ s inclination to adopt any social focus $f _ { h }$ times the popularity of this social focus, while the popularity $Y _ { h }$ of a given social focus $f _ { h }$ is a weighted sum of its attractiveness to any actor $v _ { i }$ times actor $\vec { v _ { i } } \cdot \boldsymbol { \mathbf { s } }$ gregariousness. The value assignment for the parameters along with hidden factors in $p _ { i h }$ and $q _ { h i }$ can be learned from the data. Equation (13) captures the process of the mutual reinforcement between ${ \bar { X } } _ { i }$ and $Y _ { h }$ , which through numerous online and offline interactions among social actors and social foci will converge to a stationary point. We elaborate on the convergence in the Learning Algorithm and Scalability section below. In the following two sections, we define the learning problem and propose a supervised method to configure the parameters for our predictive model.

## Learning Objective

With the mutual reinforcement model, we aim to obtain the ranked social foci in terms of popularity. This requires learning the best parameters such that the predicted output of this model, i.e., the popularity $\widehat { Y } _ { h } .$ , will approach the optimum. In this section, we first define the learning objective and then formalize the proposed learning problem.

For the learning objective, we optimize a pairwise rankbased function that evaluates the predicted popular social foci. In training, the social foci can be ranked by true popularity scores and we can evaluate our prediction by comparing the ranking difference between the predicted rankings and the true ranking of social foci. For any pair of social foci $( f _ { h } , f _ { k } )$ , if $f _ { h } \mathrm { ' s }$ true popularity is greater than that of $f _ { k } ,$ then $f _ { h }$ is ranked higher than $f _ { k } ,$ , denoted by the true ranking relationship $f _ { h } \prec f _ { k }$ . Given the true ranking $f _ { h } \prec$ $f _ { k }$ , we check whether the predicted popularity score ${ \hat { Y } } _ { h }$ is larger than $\hat { Y } _ { k }$ . A reliable predictive model should satisfy two conditions. First, the inequality $\hat { Y } _ { h } \ge \hat { Y } _ { k }$ should hold whenever $f _ { h } \prec f _ { k }$ . Second, it is better to have a larger difference $\hat { Y } _ { h } - \hat { Y } _ { k }$ if the first property holds. Considering these two properties, we employ the sigmoid function to evaluate the learned predictive model. Thus, the objective function $L _ { h k }$ is given by

$$
\begin{array}{l} {L _ {h k} = S i g m o i d \big (\hat {Y} _ {h}, \hat {Y} _ {k} \big)} \\ {= \frac {1}{1 + \exp (- (\hat {Y} _ {h} - \hat {Y} _ {k}))} \mathrm{for} f _ {h} <   f _ {k},} \end{array}\tag{14}
$$

where ${ \hat { Y } } _ { h }$ and $\hat { Y } _ { k }$ are the predicted popularity scores for any pair of social foci $( f _ { h } , f _ { k } ) \in F$ . The value of $L _ { h k }$ ranges over (0,1). Given $f _ { h } \prec f _ { k } .$ , the value of $L _ { h k }$ is higher when $\hat { Y } _ { h } - \hat { Y } _ { k }$ is greater; otherwise, $L _ { h k }$ is smaller. As a result, we would like to maximize $L _ { h k }$ , which measures the pairwise ranking consistency between the actual popular social foci and the predicted ones. The global objective function can thus be obtained by aggregating over all possible ordered pairs of social foci, as follows:

$$
L = \sum_ {h, k \in (1, M) \cap f _ {h} \prec f _ {k}} \ln L _ {h k}.\tag{15}
$$

With the objective function specified, we can now formulate our learning problem. Given a two-mode social network $G ^ { t } = < V ^ { t } \bar { \cup } \bar { F } ^ { t } , \tilde { E } ^ { t } >$ with vertices $V ^ { t } \cup F ^ { t }$ edges ${ \tilde { E } } ^ { t }$ , and the true rank of social foci at time ??, the learning problem is to obtain the optimal parameters ${ \pmb \theta } ^ { * }$ that maximize the objective function $\sum ^ { t + 1 }$ in Equation (15) for time period ?? + 1, defined as

$$
\boldsymbol {\theta} ^ {*} = \underset {\boldsymbol {\theta}} {\operatorname{argmax}} L ^ {t + 1} (\boldsymbol {\theta})\tag{16}
$$

Without loss of generality, the hidden variables are included in the parameters. Next, we describe how the vector of parameters $\pmb { \theta } = \{ \pmb { \alpha } _ { i } , \beta _ { i } , \phi _ { i } , \gamma _ { h } \}$ for $i \in ( 1 , N )$ and $h \in ( 1 , \bar { M } )$ is learned from the data.

## Learning Parameters of the Model

Given the learning objective function specified in (16), we learn the model parameters ?? using a gradient ascent approach. Specifically, the learning iteratively updates the parameters in the direction of gradients until the maximal point is reached (Hastie et al. 2009). One major difficulty for a gradient-based approach is that the closed form of gradients is neither readily given nor necessarily achievable (Hastie et al. 2009; Bottou 2004). To handle this difficulty, we first show that the mutual reinforcement process in (13) converges to a closed form, and then we address the proposed learning problem by deriving analytical solutions of gradients. Pseudo code for the gradient learning method is provided in the Learning Algorithm and Scalability section below.

Given ?? social actors and ?? social foci, we represent the propensities to adopt $P = [ p _ { i h } ] _ { N \times M }$ and the attractiveness of foci $Q = [ q _ { h i } ] _ { M \times N }$ as matrices, where $p _ { i h }$ and $q _ { h i }$ are given by (11) and (12), respectively. Gregariousness $X =$ $[ X _ { 1 } , X _ { 2 } , \ldots , X _ { N } ] ^ { T }$ and popularity $\boldsymbol { Y } = [ Y _ { 1 } , Y _ { 2 } , \ldots , Y _ { M } ] ^ { T }$ are column vectors, where $[ \cdot ] ^ { \dot { T } }$ stands for the transposed vector. Hence the model in Equation (13) can be simplified using matrix expressions. Let ?? denote a step of interactions between social foci and social actors in the mutual reinforcement process. Then, we can rewrite the mutual reinforcement process in iterations as

$$
\left\{ \begin{array}{l} X ^ {(r)} = P Y ^ {(r - 1)} + \Phi , \\ Y ^ {(r)} = Q X ^ {(r - 1)} + \Gamma , \end{array} \right.\tag{17}
$$

where the hidden factors are denoted as column vectors $\Phi = [ \phi _ { 1 } , \phi _ { 2 } , \ldots , \phi _ { N } ] ^ { T }$ and $\Gamma = [ \gamma _ { 1 } , \gamma _ { 2 } , \dots , \gamma _ { M } ] ^ { T }$ As indicated in Equation (17), gregariousness ?? and popularity ?? evolve over time. The current $X ^ { ( r ) }$ and $Y ^ { ( r ) }$ depend on the system status of the last iteration, with gregariousness and popularity updating each other. As a result, the mutual reinforcement process will converge to a unique solution, given by Lemma 1:

Lemma 1: When $r  \infty ,$ , the mutual reinforcement process in (17) approaches a unique solution independent of the initializations (i.e., $Y ^ { 0 }$ and ${ \bf { \dot { \chi } } } ^ { 0 } )$ . The closed forms of ?? and ?? at convergence are given by

$$
\left\{ \begin{array}{l} X = (I - P Q) ^ {- 1} (P \Gamma + \Phi) \\ Y = (I - Q P) ^ {- 1} (Q \Phi + \Gamma) \end{array} \right.\tag{18}
$$

where ?? is the identity matrix.

Proof: see Appendix A for detailed derivations.

Lemma 1 gives us the closed forms of ?? and ?? in Equation (18). However, the best parameter configurations in ??, ??, Φ and Γ are to be learned from the data. We adopt a gradient ascent approach in which the gradients for each parameter are provided by the following Lemma 2 and Lemma 3.

Lemma 2: Given the closed form in Equation $( l \delta ) ,$ partial derivatives of ?? with respect to each parameter in ?? can be analytically derived as follows:

$$
\frac {\partial Y}{\partial \alpha_ {i g}} = (I - Q P) ^ {- 1} Q \frac {\partial P}{\partial \alpha_ {i g}} Y,\tag{19}
$$

$$
\frac {\partial Y}{\partial \beta_ {i}} = (I - Q P) ^ {- 1} \frac {\partial Q}{\partial \beta_ {i}} X,\tag{20}
$$

$$
\frac {\partial Y}{\partial \phi_ {i}} = [ (I - Q P) ^ {- 1} Q ] _ {\cdot i},\tag{21}
$$

$$
\frac {\partial Y}{\partial \gamma_ {h}} = [ (I - Q P) ^ {- 1} ] _ {\cdot h},\tag{22}
$$

where ?? is the identity matrix.

Proof: see Appendix B for detailed derivations.

Given the partial derivatives in Equations (19) - (22), Lemma 3 shows how we can obtain the closed-form gradients for the global objective function ??(??):

Lemma 3: Given Equations (14) and (18), the gradients of the objective function ??(??) with respect to each parameter in ?? are derived as

$$
\frac {\partial L}{\partial \alpha_ {i g}} = \sum_ {\{\forall h, k | f _ {h} \prec f _ {k} \}} R _ {h k} \left(\frac {\partial Y _ {k}}{\partial \alpha_ {i g}} - \frac {\partial Y _ {h}}{\partial \alpha_ {i g}}\right),\tag{23}
$$

$$
\frac {\partial L}{\partial \beta_ {i}} = \sum_ {\{\forall h, k | f _ {h} <   f _ {k} \}} R _ {h k} \left(\frac {\partial Y _ {k}}{\partial \beta_ {i}} - \frac {\partial Y _ {h}}{\partial \beta_ {i}}\right),\tag{24}
$$

$$
\frac {\partial L}{\partial \phi_ {i}} = \sum_ {\{\forall h, k | f _ {h} <   f _ {k} \}} R _ {h k} \left(\frac {\partial Y _ {k}}{\partial \phi_ {i}} - \frac {\partial Y _ {h}}{\partial \phi_ {i}}\right),\tag{25}
$$

$$
\frac {\partial L}{\partial \gamma_ {h}} = \sum_ {\{\forall h, k | f _ {h} <   f _ {k} \}} R _ {h k} \left(\frac {\partial Y _ {k}}{\partial \gamma_ {h}} - \frac {\partial Y _ {h}}{\partial \gamma_ {h}}\right),\tag{26}
$$

where $R _ { h k } = [ 1 + e x p ( Y _ { h } - Y _ { k } ) ] ^ { - 1 }$ and the partial derivatives of ?? on the right-hand sides are given by Equations (19) - (22) in Lemma 2.

Proof: see Appendix B for detailed derivations.<sup>3</sup>

## Learning Algorithm and Scalability

Given the gradients in Equations (23) - (26), we can train our model by optimizing the objective function ?? in (16) that provides the best parameters ${ \pmb \theta } ^ { * }$ via the gradient ascent approach. The predicted popularity will be $\hat { Y } =$ $Y ( \pmb \theta ^ { * } )$ , in accordance with Equation (18). However, training efficiency is a serious concern for large-scale underlying social networks. In Equation (15), the evaluation of the global objective function enumerates all possible ordered pairs of social foci $( f _ { h } , f _ { k } | f _ { h } < f _ { k } )$ . This is challenging because considering all ordered pairs of social foci has a complexity of $O ( | F | ^ { 2 } )$ , and this is repeated in every step of the parameter updating. As a consequence, the computational expense becomes overwhelming when the set of social foci |??| is very large and there is a large number of updating steps.

The stochastic gradient ascent (SGA) method has been widely adopted to address computational complexity. In each iteration of the parameter updating, SGA uses a single pair of social foci rather than evaluating the entire set of social foci (Spall 2003, Bottou 2004). The SGA method can efficiently approximate the gradient-based optimization by approaching a local maximum (Bottou 2004, Spall 2003). Although the SGA method has been shown to be effective, it is crucial to select a relevant pair of social foci. Evaluating an irrelevant pair of social foci may lead to poor algorithm convergence in training, and sometimes the convergence becomes unachievable (Spall 2003; Bottou 2004; Kiwiel 2004). Without loss of generality, we thus have a selection question regarding which social focus $f _ { k }$ should be drawn, given $f _ { h }$

Sampling is often used to draw a relevant pair of social foci $( f _ { h } , f _ { k } )$ for training. One well-recognized sampling method is bootstrapping, which randomly selects training instances with replacements following a uniform distribution (Davison and Hinkley 1997). However, the uniform distribution will impair the convergence rate of the bootstrapping since noninformative social foci pairs are selected with the same probability as informative ones. To address this issue, we propose empirical distribution sampling (EDS) of the training instances, based on the empirical distribution of the observed popularity ??<sup>̅</sup> of social foci. Given any social focus $f _ { h } ,$ EDS will select the second focus $f _ { k }$ with a probability $\rho ( k )$ that is proportional to the observed popularity ${ \bar { Y } } _ { k } ,$ $\mathrm { i . e . , } \rho ( k ) \propto \bar { Y } _ { k }$ . The following theorem shows that EDS will accelerate the convergence compared to alternative methods such as bootstrapping:

Theorem: The proposed SGA learning method using EDS is guaranteed to converge at a faster rate than SGA using bootstrapping.

Proof: See Appendix C for detailed analyses and derivations.

We propose a gradient learning method based on a mutual reinforcement process (GLMR), as shown in Figure 2. The method learns the parameter estimates ${ \pmb \theta } ^ { * }$ based on the social influence ??, structure equivalence ??, homophily ??, and compatibility ?? that are extracted from graph $G ^ { t }$ and the observed popularity $\bar { Y }$ by time ??. The vector of parameters ?? is optimized when the predicted ranking of social foci approximates the true ranking of the social foci. The GLMR randomly initializes the parameters multiple times to avoid saddle points and approximate the global optimum. Once ${ \pmb \theta } ^ { * }$ is obtained, we can use Equation (18) to compute the predicted popularity score for all social foci, and the foci are then ranked by the predicted popularity scores.

## Empirical Evaluations

We evaluated our proposed method with real-world data sets from two large location-based social networks and one book readership network on mobile platforms. We conducted experiments to demonstrate the efficacy of our method compared to prevalent methods from the literature. In addition to the benchmarking, we conducted empirical analyses and case studies to show the properties of the proposed method. This section describes the data and benchmark methods, details the experimental design, reports the evaluation results, and discusses our main findings.

## Data Preliminaries and Experimental Design

We employed the realistic settings of mobile locationbased social networking services and book readers’ social networking services. First, we collected two data sets from location-based social networking services. We consider location check-ins as a proxy for offline adoptions,<sup>4</sup> where the service users are social actors and the business locations are social foci with a physical form. Global leading players in the mobile location-based service domain are mostly headquartered in the United States or China (Berg Insight 2015). We collected data from two major location-based social networking platforms—one for China and one for the U.S. The Chinabased platform, Dianping, is the largest third-party review site for local consumption services.

Dianping allows users to build and maintain friendships with peers and comment on business locations. In addition to offering social networking services, Dianping has deployed a check-in function that users can use to share their visits to places such as restaurants, hotels, and stores within their friend circles. Like Dianping, the US-based service provider, Gowalla, enabled users to socialize with others as well as check-in at registered business locations on mobile devices. Gowalla became part of Facebook Places when it was acquired in 2011. In addition, we collected data from a readers’ social networking service, where readers are social actors and the books in reading lists are social foci with a virtual form.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
GLMR( $\lambda_{\alpha}, \lambda_{\beta}, \lambda_{\phi}, \lambda_{\Gamma}, \eta, \tau, maxIter$ )
 $\lambda_{\alpha}, \lambda_{\beta}, \lambda_{\phi}, \lambda_{\Gamma}$ : regularization parameters
 $\eta$ : predefined small learning rate
 $\tau$ : arbitrary threshold
maxIter: max number of iterations

Randomly generate multiple initializations  $\theta^{0} = &lt;\alpha^{0}, \beta^{0}, \Phi^{0}, \Gamma^{0}&gt;$ ;
For each initialization do
    $t \leftarrow 1;$ 
    While  $t \leq maxIter \cap |L(\theta^{t}) - L(\theta^{t-1})| &gt; \tau$  do
    Given  $f_{h}$ , randomly sample  $f_{k}$  at a chance  $\rho(k)$  such that  $f_{h} &lt; f_{k} \cap \rho(k) \propto \bar{Y}_{k};$ 
    For i = 1 to N do
    For g = 1 to 3 do
    $\alpha_{ig} \leftarrow \alpha_{ig} + \eta \cdot \frac{\partial L}{\partial \alpha_{ig}}$  according to (23);
    $\beta_{i} \leftarrow \beta_{i} + \eta \cdot \frac{\partial L}{\partial \beta_{i}}$  according to (24);
    $\phi_{i} \leftarrow \phi_{i} + \eta \cdot \frac{\partial L}{\partial \phi_{i}}$  according to (25);
    For h = 1 to M do
    $\gamma_{h} \leftarrow \gamma_{h} + \eta \cdot \frac{\partial L}{\partial \gamma_{h}}$  according to (26);
    $t \leftarrow t + 1;$ $\widehat{\theta} = \theta^{t}$ 
    Evaluate  $L(\widehat{\theta})$  according to (15);
    $\theta^{*} \leftarrow \widehat{\theta}$  with the largest objective function value  $L(\widehat{\theta})$ ;
    Return  $\theta^{*}$ 

Figure 2. The Gradient Learning Based on Mutual Reinforcement Process (GLMR)
</div>

We collected the data from a bookstore chain based in North America that launched a social platform for readers to socialize and share their opinions on books. On this platform, each reader maintains a reading list, and readers adopt social foci by adding books to their reading lists. To mitigate the possible concern of a niche method, we conducted benchmarking evaluations for all three data sets, and these cross-validated the efficacy of our proposed method.

The Dianping data were crawled from the website for a three-month period from May 30 to September 1, 2015. We followed the snowball sampling method (Aral et al. 2009). Specifically, we first selected all restaurants from a random district in Beijing as seeds and retrieved all users who had ever visited the seeding business locations.

Next, we collected and updated local social network (i.e., friends) information for each user once every other week, resulting in a biweekly evolving network structure. User check-in records were gathered for each business location, with each check-in record were stored as a three-tuple <Location ID, User ID, Timestamp>. In addition to the social network and check-ins, focus-focus links were inferred when the proximity between paired foci exceeded a threshold $( \mathrm { i } . \mathrm { e } . , 0 . 5 ) . ^ { 5 }$ User profiles were built based on users’ past cuisine preferences. The Gowalla data we collected span a four-month period from May 2010 to August 2010. They cover all registered business locations and users. The establishment of social links and check-ins are recorded with timestamps. We computed focus-focus proximity using Jaccard’s similarity coefficient, and the user profiles were built using the POI category for places visited in the past. The book readership data were collected over a seven-month period from January to July 2016, starting with the inception of the social networking service. During this period, we took snapshots of the social network on a monthly basis. We captured a single book-adding action as a three-tuple <Book ID, User ID, Timestamp>. In addition, we obtained a set of reading interest tags to build user profiles so that intrinsic similarities among readers could be computed. We computed Jaccard’s similarity coefficients between foci using characteristic tags, including book genre and keywords.

The characteristics of the Gowalla, Dianping, and book readership platforms are different, as reflected by measures of the average number of friends, the network clustering coefficient, and the average number of adoptions. Table 1 compares the three networks at the end of the data collection periods and shows that Gowalla’s network connectivity and check-ins were much sparser than those of the other networks. It should be noted that data sparsity may lead to difficulty in learning and predicting (Sarwar et al. 2001).

For the raw data from Dianping and Gowalla, each evaluation data set was subdivided into training and testing sets. We built the training and testing data sets in temporal order. For the Dianping data, the training data were extracted from a snapshot of the social network at the end of a given time ?? and the corresponding numbers of accumulated check-ins, while the testing data were similarly built by time ??′. For ??<sup>′</sup> > ??, we trained the proposed model with data for time ?? and tested the learned model with data for the future time ??′. The choices of time ?? and ??′ are detailed in Table 2 for four training and testing data pairs that were generated. To instantiate the training and testing data, we needed to compute the features ??, ??, ??, and ??, as specified in the Factor Identification and Operationalization section above, and needed to sort business locations by the actual numbers of check-ins to generate the true ranking list. The constructed evaluation data are depicted in Table 3. For the Dianping data, we focused on the same set of business locations, while the number of users and check-ins accumulated over time. By the end of the data collection period, we accrued 88,734 users, 2,472 locations, 859,379 social links and 381,029 check-ins.

Parallel to the Dianping data, we took snapshots of the Gowalla social network on a monthly basis and split the data from May to August 2010 to build training and testing sets. Specifically, we constructed training data using the social network and check-ins for month t and we built testing data for month t+1, where ?? ∈ {0, 1, 2, 3}. Details of the evaluation data built from Gowalla are provided in Table 4. Gowalla’s social network had a much larger scale than the Dianping social network. It grew over time because of incoming business locations and new users and had 55,701 users, 294,458 locations, 349,464 social links, and 2,975,446 check-ins by the end of the data collection period.

We split the book readership data by month to build training and testing data sets. The training data were built by using the observed data for month ??, and the test data were similarly built for month ?? + 1, where ?? ∈ {0, 1, 2, 3, 4, 5}. Table 5 describes the constructed data in the evaluation groups. The true ranking of books was generated by sorting the number of times they were added to users’ reading lists.

Using the check-in data sets, we conducted a preliminary examination of the evolution of the social foci ranking as well as correlations between the identified factors and social foci check-ins. First, we probed the extent to which the rankings of social foci changed organically over time. We measured the change of ranking using Kendall’s Tau coefficient (Tau), which gauges the similarity between two ranked lists. The formal definition of Tau is provided in Appendix G, along with other evaluation metrics. Specifically, we inspected both the noncumulative and cumulative ranking changes of social foci: (1) we compared the ranked list of social foci from the training set against that of the corresponding testing set in each evaluation pair, and (2) we compared the beginning rankings of social foci (i.e., in the training of Evaluation #1) to those of each testing across Evaluations #1 to #4.

We found that the average Tau between any given training and testing pair from the Dianping data was 64.21%, which indicates a nontrivial difference. Moreover, we found that this divergence grows over time. Comparisons of the social foci ranking in the training of Evaluation #1 with those from testing of Evaluations #1 to #4 are shown in Figure 3. The figure shows that the initial ranked list of social foci and those that follow drift apart as time elapses.<sup>6</sup>

Table 1. Comparing Dianping and Gowalla Data Sets

<table><tr><td></td><td>Dianping data</td><td>Gowalla data</td><td>Readership data</td></tr><tr><td>Average number of friends per user</td><td>19.01</td><td>9.08</td><td>21.01</td></tr><tr><td>Average clustering coefficient of social network</td><td>0.42</td><td>0.24</td><td>0.44</td></tr><tr><td>Average number of adoptions per social focus</td><td>143.50</td><td>7.74</td><td>13.99</td></tr></table>

Table 2. Training and Testing Data Sets from Dianping over Time

<table><tr><td>Data #</td><td>Training by t</td><td>Testing by t&#x27;</td></tr><tr><td>1</td><td>May 30, 2015</td><td>July 15, 2015</td></tr><tr><td>2</td><td>June 14, 2015</td><td>August 1, 2015</td></tr><tr><td>3</td><td>June 29, 2015</td><td>August 16, 2015</td></tr><tr><td>4</td><td>July 15, 2015</td><td>September 1, 2015</td></tr></table>

Table 3. Evaluation Data Description for Dianping

<table><tr><td>Biweekly evaluation #</td><td># of locations</td><td colspan="3">Training (t)</td><td colspan="3">Testing (t&#x27;)</td></tr><tr><td></td><td></td><td># of users</td><td>#. of check-ins</td><td>#. of links</td><td># of users</td><td># of check-ins</td><td># of links</td></tr><tr><td>1</td><td>2,472</td><td>71,243</td><td>327,786</td><td>660,381</td><td>82,071</td><td>355,138</td><td>794,137</td></tr><tr><td>2</td><td>2,472</td><td>77,211</td><td>339,186</td><td>697,413</td><td>86,121</td><td>368,872</td><td>820,130</td></tr><tr><td>3</td><td>2,472</td><td>77,971</td><td>344,266</td><td>742,286</td><td>87,996</td><td>373,992</td><td>849,934</td></tr><tr><td>4</td><td>2,472</td><td>82,071</td><td>354,138</td><td>794,137</td><td>88,734</td><td>381,029</td><td>859,379</td></tr></table>

Table 4. Evaluation Data Description for Gowalla

<table><tr><td>Monthly evaluation #</td><td># of locations</td><td colspan="3">Training (month t)</td><td colspan="3">Testing (month t + 1)</td></tr><tr><td></td><td></td><td># of Users</td><td>#. of check-ins</td><td>#. of Links</td><td># of Users</td><td>#. of check-ins</td><td>#. of Links</td></tr><tr><td>1</td><td>292,593</td><td>54,612</td><td>2,272,763</td><td>257,381</td><td>54,923</td><td>2,477,311</td><td>288,266</td></tr><tr><td>2</td><td>293,428</td><td>54,923</td><td>2,477,311</td><td>288,266</td><td>55,279</td><td>2,655,677</td><td>314,006</td></tr><tr><td>3</td><td>293,992</td><td>55,279</td><td>2,655,677</td><td>314,006</td><td>55,490</td><td>2,820,328</td><td>334,416</td></tr><tr><td>4</td><td>294,458</td><td>55,490</td><td>2,820,328</td><td>334,416</td><td>55,701</td><td>2,975,446</td><td>349,464</td></tr></table>

Table 5. Evaluation Data Description for Book Readership

<table><tr><td>Monthly evaluation #</td><td># of books</td><td colspan="3">Training (month t)</td><td colspan="3">Testing (month t + 1)</td></tr><tr><td></td><td></td><td># of Users</td><td>#. of Addings</td><td>#. of Links</td><td># of Users</td><td>#. of Addings</td><td>#. of Links</td></tr><tr><td>1</td><td>2178</td><td>247</td><td>827</td><td>2281</td><td>315</td><td>1617</td><td>3033</td></tr><tr><td>2</td><td>2178</td><td>315</td><td>1617</td><td>3033</td><td>441</td><td>2423</td><td>4384</td></tr><tr><td>3</td><td>2178</td><td>441</td><td>2423</td><td>4384</td><td>558</td><td>3438</td><td>5493</td></tr><tr><td>4</td><td>2178</td><td>558</td><td>3438</td><td>5493</td><td>1821</td><td>12442</td><td>22576</td></tr><tr><td>5</td><td>2178</td><td>1821</td><td>12442</td><td>22576</td><td>3455</td><td>28104</td><td>46798</td></tr><tr><td>6</td><td>2178</td><td>3455</td><td>28104</td><td>46798</td><td>3607</td><td>30468</td><td>49256</td></tr></table>

## Benchmark Methods

Based on an extensive review of related works, we evaluated our method against eight benchmark methods. We included prevailing unsupervised and supervised learning approaches ranging across diffusion models, ranking methods, link prediction methods, and recommendation methods. In addition, we included two baseline methods—baseline linear regression and the baseline persistence method—to ensure a comprehensive evaluation. The benchmark methods are summarized in Table 6 and implementation details for each method are given in Appendix D. In this section, we briefly describe the benchmark methods.

Ranking methods, which are represented by PageRank (Page 1997) and HITS (Kleinberg 1999), are widely used because they are effective in estimating the importance of web pages in the World Wide Web graph. Our implementation of the PageRank method assumes a homogeneous graph with weighted edges. We follow Page (1997) in computing the importance scores for social foci and then rank them according to the obtained scores. The HITS method estimates the hub and authority scores of social entities based on transition probabilities between social foci and social actors. We updated Kleinberg’s (1999) HITS method to a bipartite version and sorted social foci according to their authority scores.

Threshold models have been extensively adopted to study social diffusion (Valente 1996; Chen et al. 2015; Wang and Street 2018). As the Bass diffusion model and the cascade model do not apply to our case, we adopted the linear threshold (LT) model and multipath asynchronous threshold (MAT) model for benchmarking. For the LT model, we considered all previous adopters of a social focus to be active influencers, with each influencer casting convincing power over potential adopters in their neighborhood. Next, we linearly summed the influence over all potential adopters. The potential adopters were propagated when the received influences were greater than a local random threshold. For the MAT model, we followed Wang and Street (2018).

A two-mode link prediction (LP) method was devised by Gong et al. (2014) to predict the linkage probability between paired entities in two-mode social networks. The LP method adapts proximity features that were originally developed for homogeneous networks, such as common neighbor, Adamic-Adar, and low-rank approximation. The LP method redefines these measures to accommodate two-mode social networks. Given the adapted features, the LP method runs an SVM to predict linkage probabilities between social actors and social foci. The score of a social focus is computed by aggregating linkage probabilities from all potential social actors. The predicted rank of social foci is then obtained by sorting their scores.

Collaborative filtering (CF) has been successfully used in recommending items to users based on their historical interactions. The underlying idea is that users tend to like items that have been consumed by similar users (Adomavicius and Tuzhilin 2005). CF applies to our problem as long as the user-item interactions approximate actor-foci interactions in a social network. Our CF benchmark method outputs a propensity score for any given user-focus pair. Similar to LP, the benchmark CF method aggregates propensity scores across users for a given social focus. Social foci are then ranked by their aggregated scores.

Beyond the methods used in prior studies, a natural baseline method for our study is linear regression (BLR), which is widely used for good reliability and interpretability (Bishop 2006). This baseline can cover all of our identified factors— social influence (??), structure equivalence (??), homophily (??) and compatibility (??)—as features in a linear regression model. Thus, BLR encompasses all of the identified factors in a linear regression form with the exception of the mutual reinforcement process in our proposed method. In addition to BLR, we benchmarked with another baseline, namely the persistence method (BPM). BPM is a naive predictor that assumes that the conditions when a prediction is made will not change from the present conditions.

Therefore, tomorrow is predicted as being identical to today, and BPM thus predicts the rank of social foci in the testing as being the same as in the training. The persistence method works when the underlying pattern exhibits only minor changes over time; for example, it has served as a useful benchmark in weather forecasting (Foley et al. 2012).

## Evaluation Metrics

For performance metrics, we evaluated our proposed method by comparing two ranking lists for social foci: the predicted rank and the true rank. The predicted rank (PR) is a ranked list of predicted popular social foci given by the methods in our evaluation, while the true rank (TR) is the ranked list of actual popular social foci based on the observed number of adoptions. Given the PR and TR lists, we adopted four metrics to evaluate the performance of the different methods: top-K precision (Precision), average precision (AP), area under the ROC curve (AUC), and Kendall’s Tau coefficient (Tau).

![](/api/attachments/GDDXMZEF/fulltext/images/36fd4c19aa9de0b7494880dc64ca5acc72cd3a9d1fff045371b0d08041147f49.jpg)  
Figure 3. Rank Change of Social Foci over Time

<table><tr><td colspan="5">Table 6. Methods Compared in the Evaluations</td></tr><tr><td>Method</td><td>Abbreviation</td><td>Category</td><td>Supervised</td><td>Unsupervised</td></tr><tr><td>Gradient learning based on mutual reinforcement process</td><td>GLMR</td><td>Our method</td><td>√</td><td></td></tr><tr><td>PageRank</td><td>PageRank</td><td>Benchmark</td><td></td><td>√</td></tr><tr><td>HITS ranking</td><td>HITS</td><td>Benchmark</td><td></td><td>√</td></tr><tr><td>Linear threshold</td><td>LT</td><td>Benchmark</td><td></td><td>√</td></tr><tr><td>Multipath asynchronous threshold</td><td>MAT</td><td>Benchmark</td><td></td><td>√</td></tr><tr><td>Two-mode link prediction</td><td>LP</td><td>Benchmark</td><td>√</td><td></td></tr><tr><td>Collaborative filtering-based recommendation</td><td>CF</td><td>Benchmark</td><td>√</td><td></td></tr><tr><td>Baseline persistence method</td><td>BPM</td><td>Benchmark</td><td></td><td>√</td></tr><tr><td>Baseline linear regression</td><td>BLR</td><td>Benchmark</td><td>√</td><td></td></tr></table>

<table><tr><td colspan="8">Table 7. Performance Dimension and Scope of Evaluation Metrics</td></tr><tr><td>Metrics</td><td colspan="3">Dimensions</td><td colspan="2">TR</td><td colspan="2">PR</td></tr><tr><td></td><td>Number count</td><td>Ranking order</td><td>Class discrimination</td><td>Whole list</td><td>Top-K list</td><td>Whole list</td><td>Top-K list</td></tr><tr><td>Precision</td><td>√</td><td></td><td></td><td></td><td>√</td><td></td><td>√</td></tr><tr><td>AP</td><td></td><td>√</td><td></td><td></td><td>√</td><td>√</td><td></td></tr><tr><td>AUC</td><td></td><td></td><td>√</td><td>√</td><td></td><td>√</td><td></td></tr><tr><td>Tau</td><td></td><td>√</td><td></td><td>√</td><td></td><td>√</td><td></td></tr></table>

Specifically, precision calibrates the degree of overlap between the ?? top ranked items in TR and PR. AP is used to evaluate the outcome of information retrieval tasks for good discrimination and stability (Ponte et al. 1998); it gauges the average precision of predicting the top-?? lists with different sizes K. In our study, AUC (Fawcett 2006) determines the probability that a randomly chosen top-K social focus will have more adoptions than a randomly chosen non-top-K social focus and hence be ranked higher in PR. The AUC value ranges over [0,1]. Finally, we used Tau to measure the consistency of the pairwise order between the ranked lists TR and PR. Tau quantifies an ordinal rank-based correlation between the two complete lists.

The employed measures evaluate the performance of the proposed method and benchmarks from different perspectives. They emphasize different performance dimensions by comparing different parts of the PR and TR lists; Table 7 provides a summary. The variety of metrics allowed for a comprehensive examination of the benchmarking performance of our method. Detailed definitions of the metrics are provided in Appendix G.

## Evaluation Results

We evaluated our proposed method with three realistic data sets. Tables 8 and 9 report our benchmarking results using the Dianping and Gowalla data on location checkins, while Table 10 reports the evaluation results using the book readership data. We conducted multiple evaluations in time order for each performance metric. Within each metric group, the table lists the benchmark methods in order of average performance. The results shown in Tables 8-10 were obtained by setting K = 30. In addition to K = 30, we ran the experiments with different values of K and found that the relative performance was consistent across the K values (see Appendix E for details).

The evaluation results in Tables 8-10 lead to several observations. First, our proposed problem of predicting popular social foci is nontrivial. Using the Dianping results in Table 8 as an example, we observe that the precision measures of the baseline methods BLR and BPM are 0.54 and 0.44 on average, while GLMR achieves 0.74, which lifts the baseline performances by significant margins of 68.2% and 37%, respectively. The results for the other evaluation metrics, AP, AUC, and Tau, are congruent with this observation across the data sets as shown in Tables 8-10. This observation implies that the problem of predicting popular social foci cannot be addressed by intuitive approaches and that a specifically designed method is indeed needed.

Second, our method outperforms all benchmarks across the evaluation metrics by a significant margin. As shown in Table 8, for example, the AUC for GLMR achieves a mean of 0.95 on an effectiveness scale ranging from 0 to 1. The second-best benchmark is LP, whose AUC measure is 0.78 on average. The AUC of our method is a 21.8% improvement over that of LP. Conforming to this observation, our method outperforms the other benchmark methods BLR, BPM, CF, HITS, MAT, LT, and PageRank in terms of the AUC measure. This observation is also congruent for the rest of the performance measures (i.e., AP, AUC, and Tau) over all data sets. The results suggest that our proposed method is significantly more effective than existing methods.

Third, the consideration of interacting social foci and social actors is helpful and the mutual reinforcement process model incorporated in the proposed method is indispensable. The proposed method GLMR method reduces to the benchmark BLR when we drop the mutual reinforcement process model and capture the identified factors by a linear regression model. Although GLMR and BLR cover the same set of identified factors, the closest mean AUC performance that BLR can reach for the Dianping data is 0.75, which is 26.7% less effective than our method. Similar observations also hold for the Gowalla and book readership data.

Fourth, web page ranking methods are ineffective for predicting popular social foci. The performance of the ranking methods is surprisingly low across the board. It appears that HITS and PageRank can neither identify true top-K social foci nor rank the list of social foci properly. This observation can be primarily attributed to the facts that (1) ranking methods emphasize estimating features of a current importance score, such as the quality, authority, or hub score of social foci, which may not necessarily apply in predictions, and (2) HITS and PageRank are unsupervised machine learning approaches that could be improved by supervised learning approaches (Lichtenwalter et al. 2010). We also find the recommendation method to be unsuitable for our prediction task. As Tables 8-10 show, the CF method is outperformed by the baseline methods (i.e., BLR and BPM). Since recommendation methods infer user preferences rather than actions, our results reveal that similar usage behavior depends on complex social circumstances beyond merely being of a similar mind.

<table><tr><td colspan="9">Table 8. Evaluation Results using Dianping Data</td></tr><tr><td rowspan="2">Metrics</td><td rowspan="2">Methods</td><td colspan="4">Evaluation #</td><td rowspan="2">Mean</td><td rowspan="2">Std.</td><td rowspan="2">Method class</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td rowspan="9">Precision</td><td>GLMR</td><td>0.67</td><td>0.70</td><td>0.80</td><td>0.80</td><td>0.74</td><td>0.07</td><td>Our method</td></tr><tr><td>LP</td><td>0.53</td><td>0.57</td><td>0.63</td><td>0.63</td><td>0.59</td><td>0.05</td><td>SVM</td></tr><tr><td>BLR</td><td>0.47</td><td>0.50</td><td>0.60</td><td>0.60</td><td>0.54</td><td>0.07</td><td>Regression baseline</td></tr><tr><td>BPM</td><td>0.43</td><td>0.43</td><td>0.43</td><td>0.47</td><td>0.44</td><td>0.02</td><td>Heuristic baseline</td></tr><tr><td>CF</td><td>0.30</td><td>0.30</td><td>0.33</td><td>0.37</td><td>0.33</td><td>0.03</td><td>Collaborative filtering</td></tr><tr><td>HITS</td><td>0.17</td><td>0.17</td><td>0.20</td><td>0.17</td><td>0.18</td><td>0.02</td><td>Ranking</td></tr><tr><td>MAT</td><td>0.13</td><td>0.13</td><td>0.17</td><td>0.13</td><td>0.14</td><td>0.02</td><td>Diffusion model</td></tr><tr><td>LT</td><td>0.10</td><td>0.13</td><td>0.13</td><td>0.10</td><td>0.12</td><td>0.02</td><td>Diffusion model</td></tr><tr><td>PageRank</td><td>0.10</td><td>0.13</td><td>0.13</td><td>0.13</td><td>0.12</td><td>0.02</td><td>Ranking</td></tr><tr><td rowspan="9">AP</td><td>GLMR</td><td>0.83</td><td>0.84</td><td>0.84</td><td>0.86</td><td>0.84</td><td>0.01</td><td>Our method</td></tr><tr><td>LP</td><td>0.66</td><td>0.67</td><td>0.68</td><td>0.68</td><td>0.67</td><td>0.01</td><td>SVM</td></tr><tr><td>BLR</td><td>0.62</td><td>0.62</td><td>0.64</td><td>0.66</td><td>0.64</td><td>0.02</td><td>Regression baseline</td></tr><tr><td>BPM</td><td>0.58</td><td>0.58</td><td>0.59</td><td>0.57</td><td>0.58</td><td>0.01</td><td>Heuristic baseline</td></tr><tr><td>CF</td><td>0.45</td><td>0.45</td><td>0.47</td><td>0.47</td><td>0.46</td><td>0.01</td><td>Collaborative filtering</td></tr><tr><td>HITS</td><td>0.30</td><td>0.31</td><td>0.31</td><td>0.32</td><td>0.31</td><td>0.01</td><td>Ranking</td></tr><tr><td>MAT</td><td>0.28</td><td>0.26</td><td>0.26</td><td>0.28</td><td>0.27</td><td>0.01</td><td>Diffusion model</td></tr><tr><td>LT</td><td>0.24</td><td>0.24</td><td>0.23</td><td>0.24</td><td>0.24</td><td>0.00</td><td>Diffusion model</td></tr><tr><td>PageRank</td><td>0.25</td><td>0.24</td><td>0.24</td><td>0.24</td><td>0.24</td><td>0.01</td><td>Ranking</td></tr><tr><td rowspan="9">AUC</td><td>GLMR</td><td>0.94</td><td>0.94</td><td>0.96</td><td>0.97</td><td>0.95</td><td>0.02</td><td>Our method</td></tr><tr><td>LP</td><td>0.77</td><td>0.76</td><td>0.79</td><td>0.79</td><td>0.78</td><td>0.02</td><td>SVM</td></tr><tr><td>BLR</td><td>0.74</td><td>0.75</td><td>0.75</td><td>0.76</td><td>0.75</td><td>0.01</td><td>Regression baseline</td></tr><tr><td>BPM</td><td>0.71</td><td>0.73</td><td>0.72</td><td>0.71</td><td>0.72</td><td>0.01</td><td>Heuristic baseline</td></tr><tr><td>CF</td><td>0.67</td><td>0.68</td><td>0.69</td><td>0.65</td><td>0.67</td><td>0.02</td><td>Collaborative filtering</td></tr><tr><td>HITS</td><td>0.64</td><td>0.65</td><td>0.66</td><td>0.66</td><td>0.65</td><td>0.01</td><td>Ranking</td></tr><tr><td>MAT</td><td>0.62</td><td>0.62</td><td>0.63</td><td>0.63</td><td>0.63</td><td>0.01</td><td>Diffusion model</td></tr><tr><td>LT</td><td>0.59</td><td>0.61</td><td>0.60</td><td>0.58</td><td>0.60</td><td>0.01</td><td>Diffusion model</td></tr><tr><td>PageRank</td><td>0.59</td><td>0.60</td><td>0.61</td><td>0.61</td><td>0.60</td><td>0.01</td><td>Ranking</td></tr><tr><td rowspan="9">Tau</td><td>GLMR</td><td>0.87</td><td>0.88</td><td>0.90</td><td>0.92</td><td>0.89</td><td>0.02</td><td>Our method</td></tr><tr><td>LP</td><td>0.71</td><td>0.72</td><td>0.76</td><td>0.78</td><td>0.74</td><td>0.03</td><td>SVM</td></tr><tr><td>BLR</td><td>0.68</td><td>0.69</td><td>0.72</td><td>0.71</td><td>0.70</td><td>0.02</td><td>Regression baseline</td></tr><tr><td>BPM</td><td>0.62</td><td>0.64</td><td>0.65</td><td>0.66</td><td>0.64</td><td>0.02</td><td>Heuristic baseline</td></tr><tr><td>CF</td><td>0.58</td><td>0.62</td><td>0.64</td><td>0.65</td><td>0.62</td><td>0.03</td><td>Collaborative filtering</td></tr><tr><td>HITS</td><td>0.27</td><td>0.28</td><td>0.29</td><td>0.29</td><td>0.28</td><td>0.01</td><td>Ranking</td></tr><tr><td>MAT</td><td>0.26</td><td>0.25</td><td>0.27</td><td>0.26</td><td>0.26</td><td>0.01</td><td>Diffusion model</td></tr><tr><td>LT</td><td>0.21</td><td>0.23</td><td>0.23</td><td>0.21</td><td>0.22</td><td>0.01</td><td>Diffusion model</td></tr><tr><td>PageRank</td><td>0.21</td><td>0.21</td><td>0.23</td><td>0.22</td><td>0.22</td><td>0.01</td><td>Ranking</td></tr><tr><td colspan="9">Table 9. Evaluation Results using Gowalla Data</td></tr><tr><td rowspan="2">Metrics</td><td rowspan="2">Methods</td><td colspan="4">Evaluation #</td><td rowspan="2">Mean</td><td rowspan="2">Std.</td><td rowspan="2">Method class</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td rowspan="9">Precision</td><td>GLMR</td><td>0.60</td><td>0.63</td><td>0.70</td><td>0.73</td><td>0.67</td><td>0.06</td><td>Our method</td></tr><tr><td>LP</td><td>0.43</td><td>0.47</td><td>0.53</td><td>0.57</td><td>0.50</td><td>0.06</td><td>SVM</td></tr><tr><td>BLR</td><td>0.40</td><td>0.43</td><td>0.53</td><td>0.53</td><td>0.47</td><td>0.07</td><td>Regression baseline</td></tr><tr><td>BPM</td><td>0.37</td><td>0.37</td><td>0.40</td><td>0.47</td><td>0.40</td><td>0.05</td><td>Heuristic baseline</td></tr><tr><td>CF</td><td>0.27</td><td>0.27</td><td>0.30</td><td>0.30</td><td>0.29</td><td>0.02</td><td>Collaborative filtering</td></tr><tr><td>HITS</td><td>0.17</td><td>0.17</td><td>0.17</td><td>0.20</td><td>0.18</td><td>0.02</td><td>Ranking</td></tr><tr><td>MAT</td><td>0.13</td><td>0.13</td><td>0.17</td><td>0.13</td><td>0.14</td><td>0.02</td><td>Social diffusion</td></tr><tr><td>LT</td><td>0.10</td><td>0.10</td><td>0.13</td><td>0.10</td><td>0.11</td><td>0.01</td><td>Social diffusion</td></tr><tr><td>PageRank</td><td>0.07</td><td>0.10</td><td>0.13</td><td>0.10</td><td>0.10</td><td>0.02</td><td>Ranking</td></tr><tr><td rowspan="9">AP</td><td>GLMR</td><td>0.76</td><td>0.76</td><td>0.78</td><td>0.80</td><td>0.78</td><td>0.02</td><td>Our method</td></tr><tr><td>LP</td><td>0.56</td><td>0.58</td><td>0.58</td><td>0.59</td><td>0.58</td><td>0.01</td><td>SVM</td></tr><tr><td>BLR</td><td>0.53</td><td>0.55</td><td>0.54</td><td>0.57</td><td>0.55</td><td>0.02</td><td>Regression baseline</td></tr><tr><td>BPM</td><td>0.48</td><td>0.51</td><td>0.49</td><td>0.51</td><td>0.50</td><td>0.02</td><td>Heuristic baseline</td></tr><tr><td>CF</td><td>0.35</td><td>0.36</td><td>0.39</td><td>0.41</td><td>0.38</td><td>0.03</td><td>Collaborative filtering</td></tr><tr><td>HITS</td><td>0.27</td><td>0.28</td><td>0.29</td><td>0.32</td><td>0.29</td><td>0.02</td><td>Ranking</td></tr><tr><td>MAT</td><td>0.17</td><td>0.17</td><td>0.15</td><td>0.18</td><td>0.17</td><td>0.01</td><td>Social diffusion</td></tr><tr><td>LT</td><td>0.14</td><td>0.14</td><td>0.15</td><td>0.16</td><td>0.15</td><td>0.01</td><td>Social diffusion</td></tr><tr><td>PageRank</td><td>0.15</td><td>0.13</td><td>0.14</td><td>0.17</td><td>0.15</td><td>0.02</td><td>Ranking</td></tr><tr><td rowspan="9">AUC</td><td>GLMR</td><td>0.81</td><td>0.82</td><td>0.84</td><td>0.85</td><td>0.83</td><td>0.02</td><td>Our method</td></tr><tr><td>LP</td><td>0.65</td><td>0.66</td><td>0.67</td><td>0.69</td><td>0.67</td><td>0.02</td><td>SVM</td></tr><tr><td>BLR</td><td>0.63</td><td>0.65</td><td>0.66</td><td>0.64</td><td>0.65</td><td>0.01</td><td>Regression baseline</td></tr><tr><td>BPM</td><td>0.61</td><td>0.60</td><td>0.63</td><td>0.62</td><td>0.62</td><td>0.01</td><td>Heuristic baseline</td></tr><tr><td>CF</td><td>0.63</td><td>0.63</td><td>0.62</td><td>0.62</td><td>0.63</td><td>0.01</td><td>Collaborative filtering</td></tr><tr><td>HITS</td><td>0.57</td><td>0.59</td><td>0.59</td><td>0.62</td><td>0.60</td><td>0.02</td><td>Ranking</td></tr><tr><td>MAT</td><td>0.59</td><td>0.60</td><td>0.61</td><td>0.63</td><td>0.61</td><td>0.02</td><td>Social diffusion</td></tr><tr><td>LT</td><td>0.58</td><td>0.57</td><td>0.58</td><td>0.60</td><td>0.58</td><td>0.01</td><td>Social diffusion</td></tr><tr><td>PageRank</td><td>0.58</td><td>0.56</td><td>0.56</td><td>0.57</td><td>0.57</td><td>0.01</td><td>Ranking</td></tr><tr><td rowspan="9">Tau</td><td>GLMR</td><td>0.80</td><td>0.80</td><td>0.83</td><td>0.86</td><td>0.82</td><td>0.03</td><td>Our method</td></tr><tr><td>LP</td><td>0.64</td><td>0.63</td><td>0.66</td><td>0.67</td><td>0.65</td><td>0.02</td><td>SVM</td></tr><tr><td>BLR</td><td>0.62</td><td>0.64</td><td>0.64</td><td>0.65</td><td>0.64</td><td>0.01</td><td>Regression baseline</td></tr><tr><td>BPM</td><td>0.61</td><td>0.59</td><td>0.58</td><td>0.64</td><td>0.61</td><td>0.03</td><td>Heuristic baseline</td></tr><tr><td>CF</td><td>0.55</td><td>0.59</td><td>0.62</td><td>0.61</td><td>0.60</td><td>0.03</td><td>Collaborative filtering</td></tr><tr><td>HITS</td><td>0.26</td><td>0.28</td><td>0.29</td><td>0.31</td><td>0.29</td><td>0.02</td><td>Ranking</td></tr><tr><td>MAT</td><td>0.24</td><td>0.25</td><td>0.27</td><td>0.25</td><td>0.25</td><td>0.01</td><td>Social diffusion</td></tr><tr><td>LT</td><td>0.21</td><td>0.21</td><td>0.23</td><td>0.20</td><td>0.21</td><td>0.01</td><td>Social diffusion</td></tr><tr><td>PageRank</td><td>0.20</td><td>0.22</td><td>0.23</td><td>0.27</td><td>0.23</td><td>0.03</td><td>Ranking</td></tr></table>

<table><tr><td colspan="11">Table 10. Evaluation Results using Book Readership Data</td></tr><tr><td rowspan="2">Metrics</td><td rowspan="2">Methods</td><td colspan="6">Evaluation #</td><td rowspan="2">Mean</td><td rowspan="2">Std.</td><td rowspan="2">Method class</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td rowspan="9">Precision</td><td>GMRL</td><td>0.63</td><td>0.64</td><td>0.67</td><td>0.60</td><td>0.63</td><td>0.70</td><td>0.65</td><td>0.03</td><td>Our method</td></tr><tr><td>LP</td><td>0.46</td><td>0.46</td><td>0.50</td><td>0.40</td><td>0.43</td><td>0.53</td><td>0.46</td><td>0.04</td><td>SVM</td></tr><tr><td>BLR</td><td>0.40</td><td>0.43</td><td>0.47</td><td>0.40</td><td>0.43</td><td>0.50</td><td>0.44</td><td>0.04</td><td>Regression</td></tr><tr><td>BPM</td><td>0.37</td><td>0.40</td><td>0.43</td><td>0.37</td><td>0.40</td><td>0.47</td><td>0.41</td><td>0.03</td><td>Heuristic</td></tr><tr><td>CF</td><td>0.30</td><td>0.30</td><td>0.33</td><td>0.30</td><td>0.30</td><td>0.40</td><td>0.32</td><td>0.04</td><td>Collaborative filtering</td></tr><tr><td>HITS</td><td>0.17</td><td>0.17</td><td>0.20</td><td>0.17</td><td>0.17</td><td>0.27</td><td>0.19</td><td>0.04</td><td>Ranking</td></tr><tr><td>MAT</td><td>0.13</td><td>0.17</td><td>0.13</td><td>0.17</td><td>0.13</td><td>0.13</td><td>0.14</td><td>0.02</td><td>Social diffusion</td></tr><tr><td>LT</td><td>0.10</td><td>0.13</td><td>0.13</td><td>0.10</td><td>0.13</td><td>0.10</td><td>0.12</td><td>0.02</td><td>Social diffusion</td></tr><tr><td>PageRank</td><td>0.10</td><td>0.10</td><td>0.13</td><td>0.10</td><td>0.07</td><td>0.17</td><td>0.11</td><td>0.03</td><td>Ranking</td></tr><tr><td rowspan="9">AP</td><td>GMRL</td><td>0.77</td><td>0.78</td><td>0.80</td><td>0.74</td><td>0.76</td><td>0.83</td><td>0.78</td><td>0.03</td><td>Our method</td></tr><tr><td>LP</td><td>0.61</td><td>0.63</td><td>0.64</td><td>0.60</td><td>0.62</td><td>0.68</td><td>0.63</td><td>0.03</td><td>SVM</td></tr><tr><td>BLR</td><td>0.55</td><td>0.56</td><td>0.58</td><td>0.54</td><td>0.55</td><td>0.61</td><td>0.57</td><td>0.02</td><td>Regression</td></tr><tr><td>BPM</td><td>0.50</td><td>0.53</td><td>0.53</td><td>0.49</td><td>0.50</td><td>0.57</td><td>0.52</td><td>0.03</td><td>Heuristic</td></tr><tr><td>CF</td><td>0.38</td><td>0.40</td><td>0.41</td><td>0.37</td><td>0.36</td><td>0.45</td><td>0.40</td><td>0.03</td><td>Collaborative filtering</td></tr><tr><td>HITS</td><td>0.29</td><td>0.31</td><td>0.33</td><td>0.27</td><td>0.29</td><td>0.38</td><td>0.31</td><td>0.04</td><td>Ranking</td></tr><tr><td>MAT</td><td>0.22</td><td>0.21</td><td>0.23</td><td>0.24</td><td>0.25</td><td>0.23</td><td>0.23</td><td>0.01</td><td>Social diffusion</td></tr><tr><td>LT</td><td>0.17</td><td>0.19</td><td>0.18</td><td>0.17</td><td>0.19</td><td>0.25</td><td>0.19</td><td>0.03</td><td>Social diffusion</td></tr><tr><td>PageRank</td><td>0.18</td><td>0.19</td><td>0.19</td><td>0.16</td><td>0.17</td><td>0.24</td><td>0.19</td><td>0.03</td><td>Ranking</td></tr><tr><td rowspan="9">AUC</td><td>GMRL</td><td>0.85</td><td>0.85</td><td>0.86</td><td>0.82</td><td>0.81</td><td>0.89</td><td>0.85</td><td>0.03</td><td>Our method</td></tr><tr><td>LP</td><td>0.70</td><td>0.72</td><td>0.73</td><td>0.68</td><td>0.69</td><td>0.77</td><td>0.72</td><td>0.03</td><td>SVM</td></tr><tr><td>BLR</td><td>0.68</td><td>0.68</td><td>0.70</td><td>0.66</td><td>0.67</td><td>0.74</td><td>0.69</td><td>0.03</td><td>Regression</td></tr><tr><td>BPM</td><td>0.65</td><td>0.66</td><td>0.66</td><td>0.62</td><td>0.63</td><td>0.69</td><td>0.65</td><td>0.02</td><td>Heuristic</td></tr><tr><td>CF</td><td>0.64</td><td>0.64</td><td>0.65</td><td>0.60</td><td>0.61</td><td>0.68</td><td>0.64</td><td>0.03</td><td>Collaborative filtering</td></tr><tr><td>HITS</td><td>0.58</td><td>0.59</td><td>0.61</td><td>0.57</td><td>0.57</td><td>0.64</td><td>0.59</td><td>0.02</td><td>Ranking</td></tr><tr><td>MAT</td><td>0.61</td><td>0.59</td><td>0.61</td><td>0.59</td><td>0.60</td><td>0.63</td><td>0.61</td><td>0.01</td><td>Social diffusion</td></tr><tr><td>LT</td><td>0.58</td><td>0.57</td><td>0.57</td><td>0.59</td><td>0.59</td><td>0.58</td><td>0.58</td><td>0.01</td><td>Social diffusion</td></tr><tr><td>PageRank</td><td>0.58</td><td>0.58</td><td>0.60</td><td>0.56</td><td>0.56</td><td>0.62</td><td>0.58</td><td>0.02</td><td>Ranking</td></tr><tr><td rowspan="9">Tau</td><td>GMRL</td><td>0.83</td><td>0.84</td><td>0.84</td><td>0.80</td><td>0.81</td><td>0.87</td><td>0.83</td><td>0.02</td><td>Our method</td></tr><tr><td>LP</td><td>0.67</td><td>0.68</td><td>0.70</td><td>0.64</td><td>0.64</td><td>0.74</td><td>0.68</td><td>0.03</td><td>SVM</td></tr><tr><td>BLR</td><td>0.64</td><td>0.65</td><td>0.66</td><td>0.62</td><td>0.63</td><td>0.69</td><td>0.65</td><td>0.02</td><td>Regression</td></tr><tr><td>BPM</td><td>0.63</td><td>0.63</td><td>0.64</td><td>0.59</td><td>0.58</td><td>0.68</td><td>0.63</td><td>0.03</td><td>Heuristic</td></tr><tr><td>CF</td><td>0.58</td><td>0.59</td><td>0.61</td><td>0.56</td><td>0.56</td><td>0.64</td><td>0.59</td><td>0.03</td><td>Collaborative filtering</td></tr><tr><td>HITS</td><td>0.31</td><td>0.33</td><td>0.35</td><td>0.30</td><td>0.32</td><td>0.39</td><td>0.33</td><td>0.03</td><td>Ranking</td></tr><tr><td>MAT</td><td>0.29</td><td>0.31</td><td>0.31</td><td>0.32</td><td>0.33</td><td>0.35</td><td>0.32</td><td>0.02</td><td>Social diffusion</td></tr><tr><td>LT</td><td>0.26</td><td>0.27</td><td>0.29</td><td>0.25</td><td>0.26</td><td>0.29</td><td>0.27</td><td>0.02</td><td>Social diffusion</td></tr><tr><td>PageRank</td><td>0.26</td><td>0.26</td><td>0.28</td><td>0.23</td><td>0.24</td><td>0.32</td><td>0.27</td><td>0.03</td><td>Ranking</td></tr></table>

Fifth, the relative performance of our method compared to the benchmark methods is consistent across all data sets in the social diffusions of either physical location checkins or virtual book reading intentions. This indicates that the captured interactive mechanism between social foci and social actors is unlikely a niche data phenomenon. In addition, this shows that the efficacy of our method is not significantly affected by the sparseness issue suggested by Table 1. For example, comparing the results for Dianping and Gowalla, the largest performance drop of our method in terms of AUC is only 12.6%. In view of the drastic sparseness spike moving from Dianping to Gowalla, we deem this margin of performance drop to be minor.

Finally, we conducted three case studies with specific top-K lists using book readership data. The case studies examine items in the predicted top-K list of our proposed method and compare them to the true top-K lists and those obtained by linear regression. Specifically, the case studies (1) verified the efficacy of our proposed method in predicting the newly emerging social foci, (2) showed that our method is also capable of identifying the social foci that will become less popular, and (3) compared the ranking places obtained by linear regression and our method for the top-ranked foci. The results illustrate in a more explainable fashion that our proposed method outperforms BLR. Details of the case studies are provided in Appendix F.

## Performance Attribution

To further investigate the reliability of our method, we conducted an attribution analysis with alternative method specifications. Recall that our method uses five component factors: social influence (I), structure equivalence (E), homophily (H), compatibility (C), and hidden factors (Φ and Γ), in accordance with Equation (13). In our attribution analysis, we test the difference in performance when one factor(s) at a time (or pair of factors in the case of Φ and Γ) is eliminated from our proposed method. The difference between our method with and without the removed component factor(s) indicates the contribution of the factor. We examine the performances of the five factor-reduced versions of GLMR method, denoted as GLMR-I, GLMR-E, GLMR-H, GLMR-C, and GLMR-F; obviously, the first four of these denote the reduced methods obtained by eliminating ??, ??, ??, or ??, respectively, while the last one, GLMR-F, denotes the method that results from the elimination of hidden factors Φ and Γ. Although GLMR-I, GLMR-E, and GLMR-H are conveniently adapted from the GLMR model, GLMR-C drops the impact from social foci and, as a result, reduces the proposed method to a linear regression without the mutual reinforcement process.

Table 11 provides the findings of the attribution test. Since the testing outcomes are consistent across performance metrics and data sets, we report the AUC results using the Dianping data. As shown in Table 11, the removal of one peer influence factor (i.e., I, E or H) does not significantly compromise the performance of our proposed method. The AUC performances of these versions are still better than the benchmark methods presented in Table 8. Like I, E, and H, the removal of the hidden factors lowers the performance by about 15%. However, dropping the compatibility factor C essentially degrades the proposed method into a linear model; hence, we observe that the performance of GLMR-C declines considerably relative to the performance of the original GLMR. For example, the AUC performance drops from 0.94 to 0.70 in Evaluation #1. Our attribution experiment results suggest that (1) while the peer-effect factors I, E, and H as well as the hidden factors Φ and Γ contribute to our method, removing one of these will not seriously impair the performance of the proposed method; and (2) the compatibility factor C contributes the most compared to the other factors, which reflects the importance of considering the impacts of social foci in a mutual reinforcement process.

## Evaluating Method Convergence

In addition to the attribution test, we evaluated the convergence rate for our proposed method using EDS—i.e., how quickly the designed learning can converge to its optimum—and benchmarked it against bootstrapping. Our real-world data enabled us to empirically examine the theoretical advantage of using EDS. We conducted the convergence test over multiple random initializations. The stochastic gradient-ascent step requires sampling social foci pairs $( f _ { h } , f _ { k } )$ because computing over all possible pairs of social foci for each parameter update is not scalable. Given a social focus $f _ { h }$ , the EDS we propose selects the other social focus $f _ { k }$ based on its observed number of check-ins. In contrast to EDS, bootstrapping randomly samples the other $f _ { k }$ from a uniform distribution. For a fair comparison, we configured EDS-based GLMR and bootstrapping-based GLMR with the same initial parameters, convergence threshold, and learning rate. Because the pattern discovered is consistent across evaluations, Table 12 reports the results using the number of iterations needed to train in Evaluation #4 using the Gowalla data.

<table><tr><td colspan="7">Table 11. Results of Attribution Analysis in AUC using Dianping Data</td></tr><tr><td>Evaluation #</td><td>GLMR</td><td>GLMR-I</td><td>GLMR-E</td><td>GLMR-H</td><td>GLMR-F</td><td>GLMR-C</td></tr><tr><td>1</td><td>0.94</td><td>0.86</td><td>0.85</td><td>0.84</td><td>0.80</td><td>0.70</td></tr><tr><td>2</td><td>0.94</td><td>0.85</td><td>0.84</td><td>0.85</td><td>0.79</td><td>0.71</td></tr><tr><td>3</td><td>0.96</td><td>0.88</td><td>0.88</td><td>0.85</td><td>0.82</td><td>0.72</td></tr><tr><td>4</td><td>0.97</td><td>0.88</td><td>0.87</td><td>0.87</td><td>0.81</td><td>0.72</td></tr></table>

<table><tr><td colspan="8">Table 12. Convergence Rate: GLMR-EDS vs. GLMR-Bootstrapping</td></tr><tr><td rowspan="2" colspan="2">Sampling methods</td><td colspan="5">Random initial parameter values</td><td rowspan="2">Mean</td></tr><tr><td>IPV1</td><td>IPV2</td><td>IPV3</td><td>IPV4</td><td>IPV5</td></tr><tr><td rowspan="2">Number of Iterations</td><td>GLMR(EDS)</td><td>102</td><td>105</td><td>103</td><td>107</td><td>108</td><td>105</td></tr><tr><td>GLMR(Bootstrapping)</td><td>158</td><td>159</td><td>156</td><td>162</td><td>157</td><td>158</td></tr></table>

We ran algorithms GLMR (EDS) and GLMR (Bootstrapping) until the convergence threshold was met and counted the number of iterations used. We repeated the procedure for five randomly initialized parameter values (IPVs). Table 12 shows the number of iterations needed for the two approaches to converge. Although the number of iterations fluctuates with different parameter initializations, GLMR (EDS) consistently converges within a significantly smaller number of iterations than bootstrapping. Using IPV3 as an example, it took GLMR(EDS) 103 iterations to converge while GLMR(Bootstrapping) took 156 iterations. This result suggests that GLMR using EDS converges 51.5% faster than GLMR using the prevalent bootstrapping. This result highlights a significant advantage of using our EDS-based GLMR, especially in the case of large-scale social networks.

## Discussion and Conclusion

Predicting the popularity of social foci on social networking platforms poses a fundamental problem associated with using social contagion for business purposes. Grounded in social network and social focus theories, we identify and operationalize within-mode and cross-mode factors that drive social focus adoption. We propose a two-mode social network model and have developed an innovative learning method based on a mutual reinforcement process to predict the popularity of social foci using the proposed model and the identified key factors. This study makes several research contributions. First, we formalize a spread forecasting problem for multifocus social diffusions and propose a two-mode social network model that accommodates the interdependency between peer effects and the focused organization of a social network. In the new model, we identify and operationalize the driving factors for adoptive diffusions. Second, we formulate a bilateral recursive process— specifically, a mutual reinforcement process—to characterize the interactive multifocus diffusion in twomode social networks. We prove that the reinforcement process converges and present analytical solutions. Third, given the converged state of the reinforcement process, we propose a gradient-based machine learning method that captures the optimal model configurations for predicting pairwise ranking of popular social foci. The proposed method also accounts for unobserved confounding factors. Moreover, we propose an algorithmic mechanism to address the issue of training efficiency, and analytically prove the efficiency bound and evaluate it empirically. Based on repeated examinations using both physical and virtual social foci, we show that our proposed method—in contrast to niche phenomena—consistently outperforms benchmark methods. This suggests that our approach and empirical findings are applicable to a wider range of business practices.

This study has several research implications. First, multifocus social diffusion is a nontrivial problem that cannot be addressed by the existing methods in related work, such as the traditional diffusion model, web page ranking, link prediction, or recommendations. With a proper social network model and propagation mechanism design, a gradient-based machine learning method can predict the popularity of multifocus social diffusion at a satisfactory level. Second, our evaluation findings support the conclusion that a few key social networking characteristics contain sufficient predictive capacity for adoptive behavior in multifocus social diffusion. However, peer effects based solely on within-mode factors cannot fully capture the patterns underlying the adoption diffusion in our research question. Third, an interactive propagation mechanism between social actors and social foci is crucial for effectively solving the multifocus diffusion problem and, in this mechanism, confounding factors play an important role in the predictive model in addition to the observed factors. This corroborates that the collected data and the extracted features are not complete and likely never will be (Aral and Walker 2012; Fang et al. 2013). Hence, the impact of external factor(s) is not neglectable in multifocus social diffusion studies.

Our work also has practical implications for different stakeholders, such as individual businesses, online platforms, and government. First, individual businesses that manage a social focus can benefit from knowing their future popularity ranking in advance. When a business is anticipated to rise in the rankings, this offers an early signal that can be used to better coordinate stock management, customer experience, and procurement. In contrast, when a business is expected to drop considerably in the rankings, the decision maker can proactively plan online and offline campaigns or consider cutting the firm’s operating costs to regain competitive advantage. Second, online platforms that provide location-aware services can benefit from accurate predictions of social foci rankings. For example, platforms such as Yelp and Facebook Place can leverage predicted popularity rankings to boost their advertising profits, which represent a major revenue source for the operators. Display advertisements of competing businesses (i.e., social foci) are prioritized based on relevance, which depends on their relative popularity (Facebook Business 2019), and accurately predicting popularity rankings can help generate a relevance-based prioritization of ads that could lead to an improved click-through rate (CTR). Considering the enormous scale of online visits, a small rise in the CTR can generate significant revenues for online platforms. Furthermore, platforms may strategically target the web pages of predicted popular social foci to predefine an audience for ad placement (Facebook Business 2019). This can augment responses (e.g., clicks) to the ads placed on the selected web pages, which can boost revenue for platform operators. Third, government agency practices can be supported by popularity prediction for social foci in a local area. One prominent application involves police patrolling arrangements and focuses on the temporal and spatial characteristics of identified hotspots. Predicting top hotspot locations is crucial in building a decision support system for predictive police patrolling (Camacho-Collados and Liberatore 2015). The design of police patrol sectors could be further optimized with feedback data from an appropriate decision support system (Camacho-Collados et al. 2015).

The current study could be extended in several directions. First, the feature engineering and variable construction could be further enhanced to advance the performance and evaluations of the proposed method as well as benchmarks. Feature engineering could develop a more comprehensive set of features, such as centrality measures and PageRank and HITS scores, while variable construction could generate unbiased factors for improved benchmarking. Second, a heterogeneous social network that involves more types of social entities could help address more scenarios for social diffusion, e.g., n-mode social networks with ?? ≥ 3. Third, other variants of relationships between social foci and social actors could be captured and learned in different types of model, such as neural network learning models. Fourth, learning objectives could be altered beyond the pairwise ranking lists of social foci. For example, learning objectives could use a listwise ranking function (Xia et al. 2008) and could also be defined as a bi-objective of simultaneously optimizing popularity and gregariousness. Finally, the proposed method could be applied to other prediction objectives in a two-mode network setting, such as forecasting retained social foci instead of popular ones.

## Acknowledgments

We thank the senior editor, H. Raghav Rao, the anonymous associate editor and three reviewers for suggestions and comments on earlier version of this manuscript. This study was supported by the Natural Sciences and Engineering Research Council of Canada (RPIN-2017-05667) and the National Science Foundation of United States (IIS-1814771).

## References

Altshuler, Y., Pan, W., and Pentland, A. S. 2012. “Trends Prediction Using Social Diffusion Models,” in Proceedings of the International Conference on Social Computing, Behavioral-Cultural Modeling, and Prediction, pp. 97-104.

Adomavicius, G., and Tuzhilin, A. 2005. “Toward the Next Generation of Recommender Systems: A Survey of the Stateof-the-Art and Possible Extensions,” IEEE Transactions on Knowledge and Data Engineering (17:6), pp. 734-749.

Aral, S., L. Muchnik, and A. Sundararajan. 2009. “Distinguishing Influence Based Contagion from Homophily Driven Diffusion in Dynamic Networks,” Proceedings of the National Academy of Sciences (106:51), pp. 21544-21549.

Aral, S., and Walker, D. 2011. “Creating Social Contagion through Viral Product Design: A Randomized Trial of Peer Influence in Networks,” Management Science (57:9), pp. 1623-1639.

Aral, S., and Walker, D. 2012. “Identifying Influential and Susceptible Members Of Social Networks,” Science (337:6092), pp. 337-341.

Backstrom, L., and Leskovec, J. 2011. “Supervised Random Walks: Predicting and Recommending Links in Social Networks,” in Proceedings of the Fourth ACM International Conference on Web Search and Data Mining, pp. 635-644.

Bandari, R., Asur, S., and Huberman, B. A. 2012. “The Pulse of News in Social Media: Forecasting Popularity,” in Proceedings of International Conference on Web and Social Media, pp. 26-33.

Bao, J., Zheng, Y., and Mokbel, M. F. 2012. “Location-Based and Preference-Aware Recommendation Using Sparse Geo-Social Networking Data,” in Proceedings of the 20th International Conference on Advances in Geographic Information Systems, pp. 199-208,

Bass, F. 1969. “A New Product Growth for Model Consumer Durables,” Management Science (15:2), pp. 215-227.

Basu, C., Hirsh, H., and Cohen, W. 1998. “Recommendation as Classification: Using Social and Content-based Information in Recommendation,” in Proceedings of the AAAI Conference on Artificial Intelligence 714-720.

Benchettara, N., Kanawati, R., and Rouveirol, C. 2010. “Supervised Machine Learning Applied to Link Prediction in Bipartite Social Networks,” Proceedings of the International Conference on Advances in Social Networks Analysis and Mining, pp. 326-330.

Berg Insight 2015. “Mobile Location-Based Services” (http:// www.berginsight.com/reportpdf/productsheet/bi-lbs7-ps.pdf).

Bishop, C. M. 2006. Pattern Recognition and Machine Learning, Berlin: Springer.

Bottou, L. 2004. “Stochastic Learning,” in Advanced Lectures on Machine Learning, O. Bousquet, U. von Luxburg, and G. Rätsch (eds.), Berlin: Springer, pp. 146-168.

Brown, J. J., and Reigen, P. H. 1987. “Social Ties and Word-of-Mouth Referral Behavior,” Journal of Consumer Research (14:3), pp. 350-362.

Bruyn, A. D., and Lilien, G. L. 2008. “A Multi-Stage Model of Word-of-Mouth Influence through Viral Marketing,” International Journal of Research in Marketing 25:3), pp. 151- 163.

Burt, R. S. 1976. “Positions in Networks” Social Forces (55:1), pp. 93-122.

Burt, R. S. 1987. “Social Contagion and Innovation: Cohesion versus Structural Equivalence,” American Journal of Sociology (92:6), pp. 1287-1335.

Burt, R. S., Gabbay, S. M., Holt, G., and Moran, P. 1994. “Contingent Organization as a Network Theory: The Culture-Performance Contingency Function,” Acta Sociologica (37:4), pp. 345-370.

Camacho-Collados, M., and Liberatore, F. 2015. “A Decision Support System for Predictive Police Patrolling,” Decision Support Systems (75), pp. 25-37.

Camacho-Collados, M., Liberatore, F., and Angulo, J. M. 2015. “A Multi-Criteria Police Districting Problem for the Efficient and

Effective Design of Patrol Sector,” European Journal of Operational Research (246:2), pp. 674-684.

Cao, L., Guo, J., and Cheng, X. 2011. “Bipartite Graph Based Entity Ranking for Related Entity Finding,” in Proceedings of the International Conference on Web Intelligence and Intelligent Agent Technology, pp. 130-137.

Centola, D. 2010. “The Spread of Behavior in an Online Social Network Experiment,” Science (329:5996), pp. 1194-1197.

Centola, D. 2011. “An Experimental Study of Homophily in the Adoption of Health Behavior,” Science (334:6060), pp. 1269- 1272.

Chen, W., Yuan, Y., and Zhang, L. 2010. “Scalable Influence Maximization in Social Networks under the Linear Threshold Model,” in Proceedings of IEEE International Conference on Data Mining, pp. 88-97.

Clauset, A., Shalizi, C. R., and Newman, M. E. (2009). “Power-Law Distributions in Empirical Data. SIAM review (51:4), 661-703.

Crandall, D., Cosley, D., Huttenlocher, D. Kleinberg, J., and Suri., S. 2008. “Feedback Effects between Similarity and Social Influence in Online Communities,” in Proceedings of the 14th SIGKDD International Conference on Knowledge Discovery and Data Mining, pp. 160-168.

Davis, D., Lichtenwalter, R., and Chawla, N. V. 2011. “Multi-Relational Link Prediction in Heterogeneous Information Networks,” in Proceedings of the International Conference on Advances in Social Networks Analysis and Mining, pp. 281- 288.

Davison, A., and Hinkley, D. 1997. Bootstrap Methods and Their Application. Cambridge: Cambridge University Press.

Deng, H., Lyu, M., and King, I. 2009. “A Generalized Co-HITS Algorithm and Its Application to Bipartite Graphs,” in Proceedings of the International Conference SIGKDD, pp. 239-247.

Dhar, S., and Varshney, U. 2011. “Challenges and Business Models for Mobile Location-based Services and Advertising,” Communications of the ACM (54:5), pp. 121- 128.

Entwisle, B., Faust, K., Rindfuss, R. R., and Kaneda, T. 2007. “Networks and Contexts: Variation in the Structure of Social Ties,” American Journal of Sociology (112:5), pp. 1495-1533.

Facebook Business. 2019. “About Ad Auctions,” (https://www. facebook.com/business/help/430291176997542).

Fang, X., Hu, P. J. H., Li, Z., and Tsai, W. 2013. “Predicting Adoption Probabilities in Social Networks,” Information Systems Research (24:1), pp. 128-145.

Fang, X., and Hu, P. J. 2016. “Top Persuader Prediction for Social Networks,” MIS Quarterly (42:1), pp. 63-82.

Feld, S. L. 1981. “The Focused Organization of Social Ties,” American Journal of Sociology (86:5), pp. 1015-1035.

Festinger, L. 1954. “A Theory of Social Comparison Processes,” Human Relations (7:2), pp. 117-140.

Fischer, Claude S., R. M. Jackson, C. A. Stueve, K. Gerson, and L. M. Jones. 1977. Networks and Places: Social Relations in the Urban Setting. New York: Free Press.

Foley, A. M., Leahy, P. G., Marvuglia, A., and McKeogh, E. J. 2012. “Current Methods and Advances in Forecasting of Wind Power Generation,” Renewable Energy (37:1), pp. 1-8.

Friedkin, N. E. 1998. A Structural Theory of Social Influence, Cambridge: Cambridge University Press.

Gabaix, X., Gopikrishnan, P., Plerou, V., & Stanley, H. E. (2003). “A Theory of Power-Law Distributions in Financial Market Fluctuations,” Nature (423:6937), 267-270.

Gieryn, T. F. 2000. “A Space for Place in Sociology,” Annual Review of Sociology (26:1), pp. 463-496.

Gleich, D. 2015. “PageRank Beyond the Web. SIAM Review 57:3), pp. 321-363.

Granovetter, M. 1978. “Threshold Models of Collective Behavior,” American Journal of Sociology (83:6), pp. 1420– 1443.

Grossetti, M. 2005. “Where Do Social Relations Come From? A Study of Personal Networks in the Toulouse area of France,” Social Networks (27:4), pp. 289-300.

Golder, S. A., Wilkinson, D. M., Huberman, and B. A. 2007. “Rhythms of Social Interaction: Messaging within a Massive Online Network,” in Communities and Technologies 2007, C. Steinfield, B. T. Pentland, M. Ackerman, N. Contractor (eds.), London: Springer, pp. 41-66.

Gong, N. Z., Talwalkar, A., Mackey, L., Huang, L., Shin, E. C. R., Stefanov, E., Shi, E.R., and Song, D. 2014. “Joint Link Prediction and Attribute Inference Using A Social-Attribute Network,” ACM Transactions on Intelligent Systems and Technology (5:2), Article 27.

Gonzalez, M. C., Hidalgo, C. A., and Barabasi, A. L. 2008. “Understanding Individual Human Mobility Patterns. Nature (453:7196), pp. 779-782.

Hand, D. J., Mannila, H., and Smyth, P. 2001. Principles of Data Mining. Cambridge, MA: MIT Press.

Hastie, T., Tibshirani, R., and Friedman, J. 2009. The Elements of Statistical Learning: Data Mining, Inference, and Prediction, 2nd ed., Berlin: Springer

He, X., Gao, M., Kan, M., and Wang, M. 2016. “BiRank: Towards Ranking on Bipartite Graphs,” IEEE Transactions on Knowledge and Data Engineering (29:1), pp. 57-71.

Heider, F. 1946. “Attitudes and Cognitive Organization,” The Journal of Psychology (21:1), pp. 107-112.

Hill, S., F. Provost, and C. Volinsky. 2006. “Network-Based Marketing: Identifying Likely Adopters via Consumer Networks,” Statistical Science (21:2), pp. 256-276.

Homans, G. C. 1961. Human Behavior: Its Elementary Forms. New York: Harcourt, Brace & World.

Hosanagar, K., Han, P., and Tan, Y. 2010. “Diffusion Models for Peer-to-Peer (p2p) Media Distribution: On the Impact of Decentralized, Constrained Supply,” Information Systems Research (21:2), 271-287.

Ibarra, H. 1992. “Homophily and Differential Returns: Sex Differences in Network Structure and Access in an Advertising Firm,” Administrative Science Quarterly (37:3), pp. 422-447.

Ibarra, H., and Andrews, S. B. 1993. “Power, Social Influence, and Sense Making: Effects of Network Centrality and Proximity on Employee Perceptions,” Administrative Science Quarterly (38:2), pp. 277-303.

Iyengar, R., Van den Bulte, C., and Valente, T. W. 2011. “Opinion Leadership and Social Contagion in New Product Diffusion,” Marketing Science (30:2), pp. 195-212.

Iyengar, R., Van den Bulte, C., and Lee, J. Y. 2015. “Social Contagion in New Product Trial and Repeat,” Marketing Science (34:3), pp. 408-429.

Jackson, M. O. 2008. “Average Distance, Diameter, and Clustering in Social Networks with Homophily,” in Internet and Network Economics, C. Papadimitriou, and S. Zhang, S. (eds.), Berlin: Springer, pp. 4-11.

John, L. K., Kim, T., and Barasz, K. 2018. “Ads that Don’t Overstep,” Harvard Business Review (96:1), pp. 62-69.

Jones, B. F., Wuchty, S., and Uzzi, B. 2008. “Multi-University Research Teams: Shifting Impact, Geography, and Stratification in Science. Science (322:5905), pp. 1259-1262.

Karamshuk, D., Noulas, A., Scellato, S., Nicosia, V., and Mascolo, C. 2013. “Geo-Spotting: Mining Online Location-Based Services for Optimal Retail Store Placement,” in Proceedings of the 19th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (pp. 793-801).

Kempe, D., Kleinberg, J., and Tardos, É. 2003.” Maximizing the Spread of Influence through a Social Network,” in Proceedings of the Ninth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pp. 137-146.

Kennedy, Leslie W., Joel M. Caplan, and Eric Piza. 2011. “Risk Clusters, Hotspots, and Spatial Intelligence: Risk Terrain Modeling as An Algorithm for Police Resource Allocation Strategies,” Journal of Quantitative Criminology (27:3), pp. 339-362.

Kiwiel, K. 2004. “Convergence of Approximate and Incremental Subgradient Methods for Convex Optimization,” SIAM Journal of Optimization (14:3), pp. 807–840.

Kleinbaum, A. M., Stuart, T., and Tushman, M. 2008. Communication (and Coordination?) in A Modern, Complex Organization. Boston, MA: Harvard Business School.

Kleinberg, J. 1999. “Authoritative Sources in a Hyperlinked Environment,” Journal of the ACM (46:5), pp. 604-632.

Kleinberg, J. 2007. “Cascading Behavior in Networks: Algorithmic and Economic Issues,” in Algorithmic Game Theory, N. Nisan, T. Roughgarden, E. Tardos, and V. Vazirani (eds.), Cambridge: Cambridge University Press, pp. 613-632.

Koren, Y., Bell, R. 2015. “Advances in Collaborative Filtering,” in Recommender Systems Handbook, F. Ricci, L. Rokach, B. Shapira, and P. Kantor (eds.), Boston: Springer, pp. 77-118.

Kossinets, G., and Watts, D. J. 2006. “Empirical Analysis of an Evolving Social Network,” Science (311:5757), pp. 88-90.

Kossinets, G., and Watts, D. J. 2009. “Origins of Homophily in an Evolving Social Network,” American Journal of Sociology (115:2), pp. 405-450.

Leenders, R. T. A. J. 2002. “Modeling Social Influence through Network Autocorrelation: Constructing the Weight Matrix,” Social Networks (24:1), pp. 21-47.

Leskovec, J., and Horvitz, E. 2007. Worldwide Buzz: Planetary-Scale Views on an Instant-Messaging Network. Microsoft (https://www.microsoft.com/en-us/research/publication worldwide-buzz-planetary-scale-views-on-an-instantmessaging-network/).

Leskovec, J., Adamic, L., and Huberman, B. 2007. “The Dynamics of Viral Marketing,” ACM Transactions on the Web (1:1), Article 5.

Levy, D. A. 1992. The Liberating Effects of Interpersonal Influence: An Empirical Investigation of Disinhibitory Contagion,” The Journal of Social Psychology (132:4), pp. 469-473.

Levy, D. A., and Nail, P. R. 1993. “Contagion: A Theoretical and Empirical Review and Reconceptualization,” Genetic, Social and General Psychology Monographs (119) 235-285.

Li, H., Ge, Y., Hong, R., and Zhu, H. (2016). “Point-of-Interest Recommendations: Learning Potential Check-ins from Friends,” In Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pp. 975-984.

Li, L., Shang, Y., and Zhang, W. 2002. “Improvement of HITSbased Algorithms on Web Documents,” in Proceedings of the 11th International World Wide Web Conference, pp. 527-535.

Li, Z., Fang, X. Bai, X., Sheng, O. R. L. 2017a. “Utility-Based Link Recommendation for Online Social Networks,” Management Science (63:6), pp. 1938-1952.

Li, Z., Fang, X., and Sheng, O. R. L. 2017b. “A Survey of Link Recommendation for Social Networks: Methods, Theoretical Foundations, and Future Research Directions. ACM Transactions on Management Information Systems (9:1), Article 1.

Liben-Nowell, D., and Kleinberg, J. 2007. “The Link Prediction Problem for Social Networks,” Journal of the Association for Information Science and Technology (58:7), pp. 1019-1031.

Lichtenwalter, R. N., Lussier, J. T., and Chawla, N. V. 2010. “New Perspectives and Methods in Link Prediction,” in Proceedings of the 16th SIGKDD International Conference on Knowledge Discovery and Data Mining, pp. 243-252.

Liu, X., He, Q., Tian, Y., Lee, W. C., McPherson, J., and Han, J. 2012. “Event-Based Social Networks: Linking the Online and Offline Social Worlds,” in Proceedings of the 18th SIGKDD International Conference on Knowledge Discovery and Data Mining, pp. 1032-1040. ACM.

Liu, Q., Wu, S., Wang, L., and Tan, T. 2016. “Predicting the Next Location: A Recurrent Model with Spatial and Temporal Contexts,” in Proceedings of the AAAI Conference on Artificial Intelligence, pp. 194-200.

Lorrain, F., and White, H. C. 1971. “Structural Equivalence of Individuals in Social Networks. Journal of Mathematical Sociology (1) pp. 49-80.

Ma, H., Zhou, D., Liu, C., Lyu, M., and King, I. 2011. “Recommender Systems with Social Regularization,” in Proceedings of the International Conference on Web Search and Data Mining, pp. 287-296.

Malani, G. 2017. “Location Based Services Market by Component, Technology, Enhanced Observed Time Difference, Observed Time Difference, Cell ID, Application—Global Opportunity Analysis and Industry Forecast, 2014-2022,” Allied Market Research (www.alliedmarketresearch.com/location-basedservices-market).

Manski, C. F. 1993. “Identification of Endogenous Social Effects: The Reflection Problem,” Review of Economic Studies (60:3), pp. 531-542.

McPherson, M., Smith-Lovin, L., and Cook, J. M. 2001. “Birds of a Feather: Homophily in Social Networks,” Annual Review of Sociology (27), pp. 415-444.

Moody, J. 2001. “Race, School Integration, and Friendship Segregation in America,” American Journal of Sociology (107:3), pp. 679-716.

Newman, M. E. (2005). “Power laws, Pareto distributions and Zipf’s law,” Contemporary Physics (46:5), pp. 323-351.

Noulas, A., Scellato, S., Lathia, N., and Mascolo, C. 2012a. “Mining User Mobility Features for Next Place Prediction in Location-Based Services,” in Proceedings of IEEE 12th international conference on Data mining (ICDM), pp. 1038- 1043.

Noulas, A., Scellato, S., Lathia, N., and Mascolo, C. 2012b. “A Random Walk around the City: New Venue Recommendation in Location-Based Social Networks,” in Proceedings of Joint IEEE International Conference on Privacy, Security, Risk and Trust (PASSAT) & Social Computing (SocialCom), pp. 144- 153.

Okuyama, K., Takayasu, M., and Takayasu, H. (1999). “Zipf's Law in Income Distribution of Companies,” Physica A: Statistical Mechanics and Its Applications (269:1), pp. 125- 131.

Page, L. 1997. “PageRank: Bringing Order to the Web,” Stanford Digital Library Project (http://infolab.stanford.edu/\~page/ papers/pagerank/ppframe.htm).

Pfeffer, J., Salancik, G. R., and Leblebici, H. 1976. “The Effect of Uncertainty on the Use of Social Influence in Organizational Decision Making,” Administrative Science Quarterly (21:2), pp. 227-245.

Ponte, J. M., and Croft, W. B. 1998. “A Language Modeling Approach to Information Retrieval,” in Proceedings of the 21st Annual International SIGIR Conference on Research and Development in Information Retrieval, pp. 275-281.

Rendle. S., Freudenthaler. C., Gantner. Z., and Schmidt-Thieme, L. 2009. “BPR: Bayesian Personalized Ranking from Implicit Feedback.,” in Proceedings of the Conference on Uncertainty in Artificial Intelligence, pp. 452-461.

Rice, R. E., and Aydin, C. 1991. “Attitudes Toward New Organizational Technology: Network Proximity as a Mechanism for Social Information Processing,” Administrative Science Quarterly (36:2), pp. 219-244.

Rice, R. E., Grand, A. E., Schmitz, J., and Torobin, J. 1990. “Individual and Network Influences on the Adoption and Perceived Outcomes of Electronic Messaging. Social Networks (12:1), pp. 27-55.

Rivera, M. T., Soderstrom, S. B., and Uzzi, B. 2010. “Dynamics of Dyads in Social Networks: Assortative, Relational, and Proximity Mechanisms,” Annual Review of Sociology (36), pp. 91-115.

Rui, X., Li, M., Li, Z., Ma, W., and Yu, N. 2007. “Bipartite Graph Reinforcement Model for Web Image Annotation,” in Proceedings of the 15th ACM International Conference on Multimedia, pp. 585–594.

Salakhutdinov, R., and Mnih, A. 2008. “Probabilistic Matrix Factorization,” in Proceedings of the International Conference on Neural Information Processing Systems, pp. 1257-1264.

Salancik, G., and Pfeffer, J. 1978. “A Social Information Processing Approach to Job Attitudes and Task Design,” Administrative Science Quarterly (2:3), pp. 224-253.

Sarwar, B., Karypis, G., Konstan, J., and Riedl, J. 2001. “Itembased Collaborative Filtering Recommendation Algorithms,” Proceedings of the 10th International Conference on World Wide Web, pp. 285-295.

Shalizi, C. R., and Thomas, A. C. 2011. “Homophily and Contagion Are Generically Confounded in Observational Social Network Studies,” Sociological Methods & Research (40:2), pp. 211-239.

Song, C., Qu, Z., Blumm, N., and Barabási, A. L. 2010. “Limits of Predictability in Human Mobility,” Science (327:5968), pp. 1018-1021.

Spall, J. 2003. Introduction to Stochastic Search and Optimization, New York: Wiley.

Sun, Y., and Han, J., 2013. “Mining Heterogeneous Information Networks: A Structural Analysis Approach,” ACM SIGKDD Explorations Newsletter (14:2), pp. 20-28.

Tan, P.-N., Steinbach, M. and Kumar, V. 2006. Introduction to Data Mining. Boston: Pearson Addison Wesley.

Tang, J., Lou, T., Kleinberg, J. 2012. “Inferring Social Ties across Heterogeneous Networks, in Proceedings of the 5th ACM International Conference on Web Search and Data Mining, pp. 743-752.

Tucker, C., & Zhang, J. (2011). “How Does Popularity Information Affect Choices? Field Experiment,” Management Science (57:5), pp. 828-842.

Uzzi, B., and Dunlap, S. 2005. “How to Build Your Network,” Harvard Business Review (https://hbr.org/2005/ 12/how-to-build-your-network).

Valente, T. W. (1996). “Network Models of the Diffusion of Innovations,” Computational & Mathematical Organization Theory, (2:2), pp. 163-164.

Van den Bulte, C., Lilien, G. L. 2001. “Medical Innovation Revisited: Social Contagion versus Marketing Effort,” American Journal of Sociology (106:5), pp. 1409-1435.

Wang, F. 2012. “Why Police and Policing need GIS: An Overview,” Annals of GIS (18:3), pp. 159-171.

Wang, W., and Street, N. 2018. “Modeling and Maximizing Influence Diffusion in Social Networks for Viral Marketing,” Applied Network Science (3:1), Article 6.

Wang, H., Terrovitis, M., Manoulis, N. 2013. “Location Recommendation in Location-Based Social Networks Using User Check-in Data,” in Proceedings of SIGSPATIAL International Conference on Advances in Geographic Information Systems, pp. 374-383.

Wasserman, S., and Faust, K. 1994. Social Network Analysis: Methods and Applications, Cambridge: Cambridge University Press.

Wejnert, B. 2002. “Integrating Models of Diffusion of Innovations: A Conceptual Framework,” Annual Review of Sociology (28), pp. 297-326.

Wellman, B. 1997. “An Electronic Group Is Virtually A Social Network. In Culture of the Internet, S. Kiesler (ed.), Mahwah, NJ: Erlbaum, pp. 179-205.

Xia, F., Liu, T., Wang, J., Zhang, W., Li, Hang. 2008. “Listwise Approach to Learning to Rank Theory and Algorithm,” in Proceedings of the 25th International Conference on Machine Learning (ICML), pp. 1192-1199.

Yang, Y., Chawla, N., Sun, Y., and Hani, J., 2012. “Predicting Links in Multi-Relational and Heterogeneous Networks,” in Proceedings of the 12th International Conference on Data Mining, pp. 755-764.

Zeng, A., Gualdi, S., Medo, M., and Zhang, Y. C. 2013. “Trend Prediction in Temporal Bipartite Networks: The Case of MovieLens, Netflix, and Digg,” Advances in Complex Systems (16:4), Article 1350024.

## About the Authors

Zhepeng (Lionel) Li is an associate professor in the Faculty of Business and Economics at The University of Hong Kong. He received a Ph.D. in operations and information systems from the University of Utah with a minor in computer science in 2013. His research interests include computational data science, machine learning, and recommendation, with applications in business analytics, online marketing, and social network analytics. He has published in journals such as Management Science, Information Systems Research, MIS Quarterly and ACM Transactions. His research has been supported by the Natural Sciences and Engineering Research Council of Canada (NSERC).

Yong Ge is an assistant professor in the Eller College of Management at the University of Arizona. He received his Ph.D. degree in information technology from Rutgers Business School at Rutgers, The State University of New Jersey in 2013. His primary research interests include data mining, machine learning, and their applications in recommender systems, social networking, talent analytics, healthcare informatics, and transportation. His research has appeared in MIS Quarterly, IEEE Transactions on Knowledge and Data Engineering, ACM Transactions on Information Systems, and ACM SIGKDD. His research has been funded by National Science Foundation and the National Institutes of Health. He received the NSF CAREER Award in 2019.

Xue Bai is an associate professor and Milton F. Stauffer Senior Research Fellow in the Fox School of Business at Temple University. She received her Ph.D. degree from Carnegie Mellon University in 2007. Her research interests include data mining and mathematical modeling applied to online platforms and online social networks. She has published in journals such as Management Science, Information Systems Research, MIS Quarterly, and INFORMS Journal on Computing. She is a senior editor at Production and Operations Management and an associate editor at Decision Support Systems.

## Appendix A

## Proof of Convergence

Having iterative steps denoted as superscript, the process is repeated from Equation (17) as below,

$$
\left\{ \begin{array}{l} X ^ {(r)} = P Y ^ {(r - 1)} + \Phi \\ Y ^ {(r)} = Q X ^ {(r - 1)} + \Gamma . \end{array} \right.\tag{17}
$$

Without loss of generality, we emphasize on the proof of convergence for ?? due to the fact that the proof for ?? is similar. Given equations in (17), we can derive the form of $X ^ { ( r - 1 ) }$ by substituting with proper superscript, which is

$$
X ^ {(r - 1)} = P Y ^ {(r - 2)} + \Phi\tag{A1}
$$

Replacing the $X ^ { ( r - 1 ) }$ in (17) with (A1), we have

$$
Y ^ {(r)} = Q \big (P Y ^ {(r - 2)} + \Phi \big) + \Gamma\tag{A2}
$$

Based on (A2), we are able to derive the expansion series for ?? as provided below.

$$
Y ^ {(r)} = (Q P) ^ {(k - 2)} Y ^ {(r - k)} + \left[ \sum_ {a = 0} ^ {k - 3} (Q P) ^ {(a)} \right] \cdot Q \Phi + \left[ \sum_ {a = 0} ^ {k - 3} (Q P) ^ {(a)} \right] \cdot \Gamma\tag{A3}
$$

where ?? is any integer $\in [ 2 , r )$ . Let the mutual reinforcing update continue to infinity, i.e., $r  \infty ,$ , we have

$$
Y = \lim _ {r \to \infty} Y ^ {(r)}\tag{A4}
$$

where $Y ^ { ( r ) }$ is given by (A3). We know that the process specified in (A4) will converge if and only if (i) each eigenvalue of $Q P$ is less than 1, and $( \operatorname { i i } ) k \to \infty$

To achieve condition (i), we can apply normalizations on $Q P$ such that each of its eigenvalue, i.e., $| \eta _ { h } | < 1$ . According to Neumann series, the summation $\textstyle \sum _ { a = 0 } ^ { k - 3 } ( Q P ) ^ { ( a ) }$ approaches $( I - Q P ) ^ { - 1 }$ when we make $k \to \infty$ . As a result, (A4) converges at

$$
Y = (Q P) ^ {(k - 2)} Y ^ {(0)} + (I - Q P) ^ {- 1} \cdot Q \Phi + (I - Q P) ^ {- 1} \cdot \Gamma\tag{A5}
$$

Given that (i) is ensured, it is sufficient and necessary for that $\operatorname* { l i m } _ { k  \infty } ( Q P ) ^ { ( k - 2 ) } = 0$ holds. Therefore, the converged ?? does not depend on the initialization $( \mathrm { i } . \mathrm { e } . , Y ^ { ( 0 ) } )$ , which is given by

$$
Y = (I - Q P) ^ {- 1} \cdot Q \Phi + (I - Q P) ^ {- 1} \cdot \Gamma\tag{A6}
$$

[QED]

## Appendix B

## Gradients for Parameter Updating

In order to solve the optimization problem in (16), a commonly used approach is to regularize for the complexity of learned model (Bishop 2007). Combining (14-16) and adding Frobenius norm, the learning problem can be rewritten in a regularized form as follows.

$$
\boldsymbol {\theta} ^ {*} = \underset {\boldsymbol {\theta}} {\operatorname{argmin}} \sum_ {\{\forall h, k | f _ {h} \prec f _ {k} \}} \ln (1 + \exp (- Y _ {h} + Y _ {k})) + \lambda_ {\phi} \| \Phi \| _ {F} ^ {2} + \lambda_ {\Gamma} \| \Gamma \| _ {F} ^ {2} + \lambda_ {\alpha} \| \boldsymbol {\alpha} \| _ {F} ^ {2} + \lambda_ {\beta} \| \boldsymbol {\beta} \| _ {F} ^ {2}\tag{B1}
$$

In which, column $\Phi = [ \phi _ { i } ] ^ { T } , \Gamma = \big [ \gamma _ { j } \big ] ^ { T } , \pmb { \alpha } _ { i } = \big [ \alpha _ { i g } \big ] ^ { T }$ and $\pmb { \beta } = [ \beta _ { i } ] ^ { T }$ for $i \in ( 1 , N ) , j \in ( 1 , M )$ and $g \in ( 1 , 3 )$ . The regularization parameters $\lambda _ { \Phi } , \lambda _ { \Gamma } , \lambda _ { \alpha }$ , and $\lambda _ { \beta }$ are incorporated to trade off complexity (i.e., norm of parameters) for the model fitness (i.e., objective function value).

We approach (B1) by a gradient ascent method, which requires the gradient for each of the parameters. By taking partial derivatives upon each parameter in ??, we have

$$
\frac {\partial L}{\partial \alpha_ {i g}} = \sum_ {\{\forall h, k | f _ {h} <   f _ {k} \}} R _ {h k} \left(\frac {\partial Y _ {k}}{\partial \alpha_ {i g}} - \frac {\partial Y _ {j}}{\partial \alpha_ {i g}}\right) + 2 \lambda_ {\alpha} \alpha_ {i g}\tag{B2}
$$

$$
\frac {\partial L}{\partial \beta_ {i}} = \sum_ {\{\forall h, k | f _ {h} <   f _ {k} \}} R _ {h k} \left(\frac {\partial Y _ {k}}{\partial \beta_ {i}} - \frac {\partial Y _ {j}}{\partial \beta_ {i}}\right) + 2 \lambda_ {\beta} \beta_ {i}\tag{B3}
$$

$$
\frac {\partial L}{\partial \phi_ {i}} = \sum_ {\{\forall h, k | f _ {h} \prec f _ {k} \}} R _ {h k} (\frac {\partial Y _ {k}}{\partial \phi_ {i}} - \frac {\partial Y _ {j}}{\partial \phi_ {i}}) + 2 \lambda_ {\phi} \phi_ {i}\tag{B4}
$$

$$
\frac {\partial L}{\partial \gamma_ {h}} = \sum_ {\{\forall h, k | f _ {h} <   f _ {k} \}} R _ {h k} (\frac {\partial Y _ {k}}{\partial \gamma_ {h}} - \frac {\partial Y _ {h}}{\partial \gamma_ {h}}) + 2 \lambda_ {\gamma} \gamma_ {h}\tag{B5}
$$

where ?? is the objective function in (B1), and $R _ { h k } \equiv [ 1 + \exp ( Y _ { h } - Y _ { k } ) ] ^ { - 1 }$

To complete solutions (B2)-(B5), we further need to have analytical form for $\begin{array} { r } { \frac { \partial Y _ { h } } { \partial \alpha _ { i g } } , \frac { \partial Y _ { k } } { \partial \alpha _ { i g } } , \frac { \partial Y _ { h } } { \partial \beta _ { i } } , \frac { \partial Y _ { k } } { \partial \beta _ { i } } , \frac { \partial Y _ { h } } { \partial \phi _ { i } } , \frac { \partial Y _ { k } } { \partial \phi _ { i } } , \frac { \partial Y _ { h } } { \partial \gamma _ { h } } , \mathrm { a n d } \frac { \partial Y _ { k } } { \partial \gamma _ { h } } . } \end{array}$ To obtain them, ?? and ?? can be rewritten from (16) as follows.

$$
\begin{array}{r l} {X =} & {(I - P Q) ^ {- 1} (P \Gamma + \Phi)} \\ {=} & {\tilde {P} (P \Gamma + \Phi)} \\ {Y =} & {(I - Q P) ^ {- 1} (Q \Phi + \Gamma)} \\ {=} & {\tilde {Q} (Q \Phi + \Gamma)} \end{array}\tag{B6}
$$

(B7)

where $\tilde { P } \equiv ( I - P Q ) ^ { - 1 } \mathrm { ~ a n d ~ } \tilde { Q } \equiv ( I - Q P ) ^ { - 1 }$

Next we are to derive the ??’s gradients in terms of $\alpha _ { i g } , \beta _ { i } , \phi _ { i }$ , and $\gamma _ { h }$ .

(1) $\mathrm { S o l v e } \frac { \partial Y } { \partial \alpha _ { i g } } .$

$$
{ \begin{array}{r l} {\frac {\partial Y}{\partial \alpha_ {i g}}} & {= \frac {\partial \tilde {Q} (Q \Phi + \Gamma)}{\partial \alpha_ {i g}}} \\ & {= \frac {\partial \tilde {Q}}{\partial \alpha_ {i g}} (Q \Phi + \Gamma)} \\ & {= \tilde {Q} Q \frac {\partial P}{\partial \alpha_ {i g}} \tilde {Q} (Q \Phi + \Gamma)} \\ & {= \tilde {Q} Q \frac {\partial P}{\partial \alpha_ {i g}} Y} \end{array} }\tag{B8}
$$

where $\left[ \frac { \partial P } { \partial \alpha _ { i g } } \right]$ is a $N \times M$ matrix that has ??th row as none-zero values and the cell $\left[ \frac { \partial P } { \partial \alpha _ { i g } } \right] _ { i h }$ refers to the ??th element in $[ I _ { i h } , E _ { i h } , H _ { i h } ] ^ { T }$

(2) Solve $\frac { \partial Y } { \partial \beta _ { i } } .$

$$
{ \begin{array}{r l} {\frac {\partial Y}{\partial \beta_ {i}}} & {= \frac {\partial \tilde {Q} (Q \Phi + \Gamma)}{\partial \beta_ {i}}} \\ & {= \frac {\partial \tilde {Q}}{\partial \beta_ {i}} (Q \Phi + \Gamma) + \tilde {Q} \frac {\partial Q}{\partial \beta_ {i}} \Phi} \\ & {= \tilde {Q} \frac {\partial Q}{\partial \beta_ {i}} P \tilde {Q} (Q \Phi + \Gamma) + \tilde {Q} \frac {\partial Q}{\partial \beta_ {i}} \Phi} \\ & {= \tilde {Q} \frac {\partial Q}{\partial \beta_ {i}} X} \end{array} }\tag{B9}
$$

(3) Solve $\frac { \partial Y } { \partial \phi _ { i } } .$

$$
\begin{array}{r l} \frac {\partial Y}{\partial \phi_ {i}} & = \left[ \frac {\tilde {Q} (Q \Phi + \Gamma)}{\partial \Phi} \right] _ {i} \\ & = [ \tilde {Q} Q ] _ {. i} \end{array}\tag{B10}
$$

where $[ \tilde { Q } Q ] _ { . i }$ is the ??th column of matrix $\tilde { Q } Q$

(4) Solve $\frac { \dot { \partial _ { Y } } } { \partial \gamma _ { h } } .$

$$
\begin{array}{r l} \frac {\partial Y}{\partial \gamma_ {h}} & = \left[ \frac {\tilde {Q} (Q \Phi + \Gamma)}{\partial \Gamma} \right] _ {h} \\ & = [ \tilde {Q} ] _ {. h} \end{array}\tag{B11}
$$

where $[ ( \tilde { Q } ] _ { \cdot h }$ refers to the ℎth column of $\tilde { Q }$

Given the closed-form gradients (B8) - (B11), we can substitute corresponding terms into (B2) - (B5) and have analytical solutions for (B1). [QED]

## Appendix C

## Bound of Convergence Rate

We are about to show that the expected convergence rate of the proposed weighted sampling for stochastic gradient is guaranteed to outperform that of using bootstrapping. It does not depend on specifications of probability density function for the weighted sampling. We repeat the objective function in (15), which is equivalent to minimizing the following negative log likelihood.

$$
- \sum_ {h, k \in (1, M)} \ln {(s i g m o i d (\hat {Y} _ {h} - \hat {Y} _ {k}))}\tag{C1}
$$

Following stochastic gradient descent, it allows to minimize (C1) without enumerating all $( h , k )$ pairs via sampling informative training instances. Based on Lemma 2, we know the general parameter update for any given pair $( h , k )$ is

$$
\theta = \theta - \eta \left(1 - s i g m o i d \bigl (\hat {Y} _ {h} - \hat {Y} _ {k} \bigr)\right) \times \frac {\partial}{\partial \theta} (\hat {Y} _ {h} - \hat {Y} _ {k})\tag{C2}
$$

In which, ?? is a learning rate that is chosen small enough to ensure the updating is performed in the right direction, ?? is any given parameter in $\theta = \{ \alpha , \beta , \phi , \gamma \} , \hat { Y } _ { h }$ and $\hat { Y } _ { h }$ are obtained using ?? in the preceding iteration. We know from (C2) that the greater the gradient descent step size the faster it converges. Given that learning rate ?? is identical over sampling methods, the step size depends on a multiplicative scalar, which is namely, gradient magnitude:

$$
\Delta_ {h, k} = 1 - s i g m o i d \big (\hat {Y} _ {h} - \hat {Y} _ {k} \big)\tag{C3}
$$

With the definition of sigmoid function, we can derive and rewrite the right hand side of (C3) as

$$
\Delta_ {h, k} = \frac {1}{1 + e ^ {\hat {Y} _ {h} - \hat {Y} _ {k}}}\tag{C4}
$$

From (C4), we know that $\Delta _ { h , k } \in ( 0 , 1 )$ regardless of $\hat { Y } _ { h }$ and $\hat { Y } _ { k } .$ Therefore, the gradient descent is guaranteed and the magnitude depends on the instantiated value of $\hat { Y } _ { h } - \hat { Y } _ { k }$ . The convergence rate is higher for the iterative parameter updating when the value of $\hat { Y } _ { h } - \hat { Y } _ { k }$ is smaller.

Next we show the expected value of $\hat { Y } _ { h } - \hat { Y } _ { k }$ is greater using bootstrapping than that of using weighted sampling. Without loss of generality, we can assume that $\hat { Y } _ { k }$ ranges over $( 0 , \xi { \bar { Y } } _ { k } )$ , where $\bar { Y } _ { k }$ is observed in training and $\xi$ can be determined empirically from data and $\xi , \bar { Y } _ { k } > 0 .$ . To be specific, we iterate over all (or uniformly select one) $f _ { h } \in F$ and then compare choosing $f _ { \underline { { k } } }$ at a probability by uniform distribution (i.e., bootstrapping) against choosing that proportional to the value of observed popularity $\bar { Y } _ { k }$ (i.e., weighted sampling). Given $f _ { h }$ is drawn and ${ \hat { Y } } _ { h }$ is thus determined, we consider $\hat { Y } _ { k }$ as a random variable $x \in ( 0 , \xi { \bar { Y } } _ { k } )$ . As a result, the expectation of $\hat { Y } _ { h } - \hat { Y } _ { k }$ using bootstrapping is obtained by selecting $f _ { k }$ according to uniform distribution of ${ \bar { Y } } _ { k } .$ , which is written as follows.

$$
\mathbb {E} \big (\hat {Y} _ {h} - \hat {Y} _ {k} \big) _ {u n i f o r m} = \hat {Y} _ {h} - \int_ {0} ^ {\xi \bar {Y} _ {k}} \frac {x}{\xi \bar {Y} _ {k}} d _ {x}\tag{C5}
$$

Hence, we can derive from (C5) that the expectation of $\hat { Y } _ { h } - \hat { Y } _ { k }$ is $\widehat { Y } _ { h } - \textstyle \frac { 1 } { 2 } \xi \overline { { Y } } _ { k }$ . We are next to show that using the proposed weighted sampling method will lead to a smaller expectation value of $\hat { Y } _ { h } - \hat { Y } _ { k }$ . Given density function $\rho ( x )$ for weighted sampling, we have the expectation

$$
\mathbb {E} \big (\hat {Y} _ {h} - \hat {Y} _ {k} \big) _ {w e i g h t e d} = \hat {Y} _ {h} - \int_ {0} ^ {\xi \bar {Y} _ {k}} x \rho (x) d _ {x}\tag{C6}
$$

We suppose the unspecified density function $\rho ( x )$ is continuous and non-decreasing on $( 0 , \xi { \bar { Y } } _ { k } )$ . In order to prove the theorem, it is sufficient to show that $\left( \mathbf { C } 5 \right) > \left( \mathbf { C } 6 \right)$ , which is reduced to show that the following inequality holds.

$$
\int_ {0} ^ {\xi \bar {Y} _ {k}} x \rho (x) d _ {x} > \frac {1}{2} \xi \bar {Y} _ {k}\tag{C7}
$$

Without loss of generality, the inequality in (C7) reduces to show that

$$
\int_ {0} ^ {1} x \rho (x) d _ {x} > \frac {1}{2}\tag{C8}
$$

Weighted sampling method proposes to draw $f _ { k }$ by a chance that is proportional to $\bar { Y } _ { k }$ , which is to say, the density function $\rho ( x _ { 1 } ) <$ $\rho ( x _ { 2 } )$ when $x _ { 1 } < x _ { 2 }$ . We know that the left hand side of (C8) can be written as

$$
\int_ {0} ^ {1} x \rho (x) d _ {x} = \frac {1}{2} \int_ {0} ^ {1} \rho (x) d _ {x ^ {2}}\tag{C9}
$$

By substituting $x ^ { 2 } \to x ,$ we have that (C8) is equivalent to the inequality shown as below.

$$
\int_ {0} ^ {1} \rho (\sqrt {x}) d _ {x} > 1\tag{C10}
$$

For each $x \in ( 0 , 1 )$ , we know that $x < { \sqrt { x } }$ holds. Hence $\rho ( x ) < \rho ( { \sqrt { x } } )$ holds according to the definitions. Therefore, we arrive at $\begin{array} { r } { \int _ { 0 } ^ { 1 } \rho \big ( \sqrt { x } \big ) d _ { x } > \int _ { 0 } ^ { 1 } \rho ( x ) d _ { x } = 1 } \end{array}$ , which shows that (C10) holds. [QED]

## Appendix D

## Implementation Details of Benchmark Methods

Ranking method such as PageRank (Page 1997) and HITS (Kleinberg 1999) are widely used for they are effective in estimating the importance of web pages on the graph of World Wide Web. Ranking methods are adaptable to address our problem when web pages on WWW graph are considered as nodes in a social network. Implementation details of PageRank and HITS are provided as follows. On one hand, PageRank method assumes homogeneous network with weighted links. To operationalize, we first construct a fully connected homogeneous network of foci $F ,$ and then assign link weights using pairwise similarity $S _ { h k }$ between any foci $( f _ { h } , f _ { k } ) \in F \colon$

$$
S _ {h k} = \sum_ {Z \in \{I, E, H, C \}} S _ {h k} (Z)
$$

where the link weight $S _ { h k }$ sums over all identified power $Z \in \{ I , E , H , C \}$ with respect to a cosine similarity $S _ { h k } ( Z )$ given by

$$
S _ {h k} (Z) = C o s (\vec {Z} _ {i h}, \vec {Z} _ {i k})
$$

In which, vector $\vec { Z } _ { i h } = < Z _ { 1 h } , Z _ { 2 h } , \ldots , Z _ { N h } >$ and $\vec { Z } _ { i k } = < Z _ { 1 k } , Z _ { 2 k } , \ldots , Z _ { N k } >$ where elements are values of identified factors given user and foci. $Z _ { i h }$ and $Z _ { i k }$ are obtained in accordance to (2), (5), (8), and (10) for $Z = I , E , H$ , and ??, respectively. Given the specified network with weighted links, we follow Page (1997) to compute the importance scores of social foci, hence obtaining a ranked list of social foci by sorting importance scores. On the other hand, HITS method can estimate hub and authority scores of networked social nodes. It assumes link weights in both incoming and outgoing directions and determines transition probabilities accordingly. In our implementation, the transition probability from user ?? to foci ℎ is given by

$$
W _ {i h} = \sum_ {Z \in \{I, E, H \}} Z _ {i h}
$$

where $Z _ { i h }$ follows $( 2 ) , ( 5 )$ , and (8) for $Z = I , E , H$ , respectively. As for the other direction, we define transition probability from focus ℎ to user ?? as

$$
V _ {h i} = C _ {h i}
$$

where $C _ { h i }$ is given as (10). Following Kleinberg (1999), we can compute the authority score and hub score for all social foci. Socia foci are thus ranked by sorting over their authority scores.

Threshold models have been extensively adopted to study social diffusions (Valente 1996; Chen et al. 2015, Wang and Street 2018). In which, Linear threshold model (LT) and multipath asynchronous threshold model (MAT) are appointed for benchmarking. The implementation details are given as follows. For LT model, we consider, at a given time ??, all previous adopters of a social focus as active influencers. Each influencer $v _ { i }$ will cast convincing power $c p _ { i j }$ to a potential adopter $v _ { j }$ in her neighborhood. The strength of influence is $\begin{array} { r } { c p _ { i j } = \frac { 1 } { D _ { j } } , } \end{array}$ , where $D _ { j }$ is the size of ??<sub>??</sub>'s neighborhood. Next, we can linearly sum the influence over all potential ??<sub>??</sub> for any given active influencer. The potential adopter is propagated when the received influences are greater than a local random threshold ranging over [0,1]. The ranking of social foci at time ?? + 1 is then based on the number of propagated adopters. To implement MAT, we have followed Wang and Street (2018). In which, the decay rate ?? is set to 0.1 while maximum path length and delay are set to 3 and the overall network activeness $\hat { \mu } = 1$

Two-mode Link Prediction method (LP) has been devised to predict the linkage probability between a pair of entities in two-mode social networks (Gong et al. 2014), namely social attributes and social nodes. It adapts proximity features that are originally developed for homogeneous networks, such as Common Neighbor, Adamic-Adar, and Low-rank Approximation. LP method redefines these measures to accommodate two-mode social networks. Provided with adapted features, LP method runs a Support Vector Machine (SVM) classifier to predict linkage probability between users and foci. According to Gong et al. (2014), SAI-SAN algorithm was shown the most effective among alternative algorithms. Therefore, we view social attributes as social foci and treat social nodes as socia actors in our model so as to apply SAI-SAN algorithm. It predicts the future linkage probability between any pair of social focus and social actor. The score of a social focus ?? is computed by aggregating linkage probabilities from all users to $f .$ Therefore, predicted rank of social foci is obtained according to such scores.

Collaborative filtering (CF) has been a success in recommending items to users based on their historical interactions. The underlying idea entails that one tends to like items that have been consumed by similar users (Adomavicius and Tuzhilin 2005). A representative approach of CF is Probabilistic Matrix Factorization (PMF) (Salakhutdinov and Mnih 2007), which considers each user or item as one high-dimensional latent feature. When one user’s latent feature matches well with that of an item, it is deemed that the focal user likes the item. We realize PMF for benchmarking CF method. The input is in one observed user-focus matrix, where each cell is valued 1 if the corresponding user has adopted that focus and 0 otherwise. After learning the latent features for all users and foci following (Salakhutdinov and Mnih 2007), we manage to output a score for any given pair of user and focus. This score is considered the likelihood of one social actor adopting a social focus. Similar to LP, CF method aggregates likelihood scores over users for a given social focus and ranks social foci accordingly.

Beyond benchmarks in literature, a natural baseline lies in linear regression method (i.e., BLR), which is widely used for good reliability and interpretability (Bishop 2006). This baseline would cover identified social influence $( I ) .$ , structure equivalence (??), homophily (??) and compatibility (??) as features in a linear regression model. BLR infers the number of check-ins in the following form:

$$
Y _ {h} = a _ {0} + a _ {1} I _ {h} + a _ {2} E _ {h} + a _ {3} H _ {h} + a _ {4} C _ {h}
$$

where coefficients ??s are parameters to be learned by fitting the data. We let input features $\begin{array} { r } { I _ { h } = \sum _ { i } I _ { i h } , E _ { h } = \sum _ { i } E _ { i h } , H _ { h } = \sum _ { i } H _ { i h } } \end{array}$ , and $\begin{array} { r } { C _ { h } = \sum _ { i } C _ { h i } } \end{array}$ , where $I _ { i h } , E _ { i h } , H _ { i h }$ , and $C _ { h i }$ are obtained according to (2), (5), (8), and (10), respectively. To train this model, $Y _ { h }$ uses the observed number of adoptions for each focus. A major difference between BLR and our method (i.e., GLMR) lies in whether it accounts for the interdependency between social foci and social actors. Although BLR covers all identified factors in a linear model, it neglects the interaction between social actors and foci. In contrast, GLMR incorporates a mutual reinforcement process for such interaction, which is shown indispensable by our results.

We benchmark with another baseline persistence method (i.e., BPM). Persistence method is known as a naïve predictor that assumes the conditions at the time of prediction will not change from current time. In this vein, tomorrow is thus predicted as equal to today. To be specific, BPM predicts the rank of social foci in testing identical to the one in training, which is observable. Persistence method works when the underlying pattern exhibits minor change over time. It has served as a useful benchmark in weather forecasting (Foley et al. 2012).

## Appendix E

## Evaluation Results by Changing the Value of K

As the value of K may influence the measurements of ranking performance, we further demonstrate evaluation results with different K values. Specifically, we compute the performances in Precision, AP and AUC metrics with K = 30, 50, 120 and 240 for different methods with Dianping data and show the results in Table E1. Please be noted that we have used global Tau coefficient, which does not vary over different K. Hence it is not repeated here.

Table E1. Performances in Precision, Average Precision, and AUC with Different Values of K on Dianping Data

<table><tr><td colspan="7">Performance in Precision</td><td colspan="7">Performance in Average Precision</td><td colspan="6">Performance in AUC</td><td></td></tr><tr><td rowspan="2">Methods</td><td rowspan="2">K</td><td colspan="4">Evaluation #</td><td rowspan="2">Mean</td><td rowspan="2">Methods</td><td rowspan="2">K</td><td colspan="4">Evaluation #</td><td rowspan="2">Mean</td><td rowspan="2">Methods</td><td rowspan="2">K</td><td colspan="4">Evaluation #</td><td rowspan="2">Mean</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>1</td><td>2</td><td>3</td><td>4</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td rowspan="4">GLMR</td><td>30</td><td>0.67</td><td>0.70</td><td>0.80</td><td>0.80</td><td>0.74</td><td rowspan="4">GLMR</td><td>30</td><td>0.83</td><td>0.84</td><td>0.84</td><td>0.86</td><td>0.84</td><td rowspan="4">GLMR</td><td>30</td><td>0.94</td><td>0.94</td><td>0.96</td><td>0.97</td><td>0.95</td></tr><tr><td>50</td><td>0.62</td><td>0.64</td><td>0.64</td><td>0.66</td><td>0.64</td><td>50</td><td>0.79</td><td>0.80</td><td>0.81</td><td>0.82</td><td>0.81</td><td>50</td><td>0.90</td><td>0.91</td><td>0.91</td><td>0.92</td><td>0.91</td></tr><tr><td>120</td><td>0.58</td><td>0.60</td><td>0.60</td><td>0.62</td><td>0.60</td><td>120</td><td>0.69</td><td>0.71</td><td>0.71</td><td>0.72</td><td>0.71</td><td>120</td><td>0.85</td><td>0.85</td><td>0.86</td><td>0.86</td><td>0.86</td></tr><tr><td>240</td><td>0.50</td><td>0.51</td><td>0.51</td><td>0.52</td><td>0.51</td><td>240</td><td>0.56</td><td>0.57</td><td>0.59</td><td>0.61</td><td>0.58</td><td>240</td><td>0.63</td><td>0.62</td><td>0.62</td><td>0.64</td><td>0.63</td></tr><tr><td rowspan="4">LP</td><td>30</td><td>0.53</td><td>0.57</td><td>0.63</td><td>0.63</td><td>0.59</td><td rowspan="4">LP</td><td>30</td><td>0.66</td><td>0.67</td><td>0.68</td><td>0.68</td><td>0.67</td><td rowspan="4">LP</td><td>30</td><td>0.77</td><td>0.76</td><td>0.79</td><td>0.79</td><td>0.78</td></tr><tr><td>50</td><td>0.48</td><td>0.48</td><td>0.50</td><td>0.50</td><td>0.49</td><td>50</td><td>0.60</td><td>0.61</td><td>0.62</td><td>0.63</td><td>0.62</td><td>50</td><td>0.72</td><td>0.73</td><td>0.72</td><td>0.74</td><td>0.73</td></tr><tr><td>120</td><td>0.42</td><td>0.42</td><td>0.43</td><td>0.44</td><td>0.43</td><td>120</td><td>0.55</td><td>0.56</td><td>0.57</td><td>0.57</td><td>0.56</td><td>120</td><td>0.66</td><td>0.65</td><td>0.67</td><td>0.67</td><td>0.66</td></tr><tr><td>240</td><td>0.38</td><td>0.38</td><td>0.38</td><td>0.39</td><td>0.38</td><td>240</td><td>0.50</td><td>0.51</td><td>0.52</td><td>0.54</td><td>0.52</td><td>240</td><td>0.61</td><td>0.60</td><td>0.59</td><td>0.61</td><td>0.60</td></tr><tr><td rowspan="4">BLR</td><td>30</td><td>0.47</td><td>0.50</td><td>0.60</td><td>0.60</td><td>0.54</td><td rowspan="4">BLR</td><td>30</td><td>0.62</td><td>0.62</td><td>0.64</td><td>0.66</td><td>0.64</td><td rowspan="4">BLR</td><td>30</td><td>0.74</td><td>0.75</td><td>0.75</td><td>0.76</td><td>0.75</td></tr><tr><td>50</td><td>0.42</td><td>0.42</td><td>0.44</td><td>0.46</td><td>0.44</td><td>50</td><td>0.54</td><td>0.55</td><td>0.56</td><td>0.56</td><td>0.55</td><td>50</td><td>0.70</td><td>0.71</td><td>0.71</td><td>0.72</td><td>0.71</td></tr><tr><td>120</td><td>0.38</td><td>0.39</td><td>0.39</td><td>0.39</td><td>0.38</td><td>120</td><td>0.49</td><td>0.49</td><td>0.51</td><td>0.52</td><td>0.50</td><td>120</td><td>0.64</td><td>0.65</td><td>0.63</td><td>0.66</td><td>0.65</td></tr><tr><td>240</td><td>0.30</td><td>0.30</td><td>0.32</td><td>0.32</td><td>0.31</td><td>240</td><td>0.42</td><td>0.42</td><td>0.41</td><td>0.43</td><td>0.42</td><td>240</td><td>0.58</td><td>0.59</td><td>0.61</td><td>0.61</td><td>0.60</td></tr><tr><td rowspan="4">BPM</td><td>30</td><td>0.43</td><td>0.43</td><td>0.43</td><td>0.47</td><td>0.44</td><td rowspan="4">BPM</td><td>30</td><td>0.58</td><td>0.58</td><td>0.59</td><td>0.57</td><td>0.58</td><td rowspan="4">BPM</td><td>30</td><td>0.71</td><td>0.73</td><td>0.72</td><td>0.71</td><td>0.72</td></tr><tr><td>50</td><td>0.38</td><td>0.40</td><td>0.40</td><td>0.40</td><td>0.40</td><td>50</td><td>0.51</td><td>0.53</td><td>0.53</td><td>0.54</td><td>0.53</td><td>50</td><td>0.64</td><td>0.65</td><td>0.65</td><td>0.63</td><td>0.64</td></tr><tr><td>120</td><td>0.29</td><td>0.29</td><td>0.30</td><td>0.31</td><td>0.30</td><td>120</td><td>0.42</td><td>0.43</td><td>0.44</td><td>0.44</td><td>0.43</td><td>120</td><td>0.61</td><td>0.62</td><td>0.62</td><td>0.61</td><td>0.62</td></tr><tr><td>240</td><td>0.18</td><td>0.19</td><td>0.19</td><td>0.20</td><td>0.19</td><td>240</td><td>0.38</td><td>0.37</td><td>0.39</td><td>0.39</td><td>0.38</td><td>240</td><td>0.57</td><td>0.57</td><td>0.56</td><td>0.58</td><td>0.57</td></tr><tr><td rowspan="4">CF</td><td>30</td><td>0.30</td><td>0.30</td><td>0.33</td><td>0.37</td><td>0.33</td><td rowspan="4">CF</td><td>30</td><td>0.45</td><td>0.45</td><td>0.47</td><td>0.47</td><td>0.46</td><td rowspan="4">CF</td><td>30</td><td>0.67</td><td>0.68</td><td>0.69</td><td>0.65</td><td>0.67</td></tr><tr><td>50</td><td>0.26</td><td>0.26</td><td>0.28</td><td>0.28</td><td>0.27</td><td>50</td><td>0.41</td><td>0.42</td><td>0.44</td><td>0.43</td><td>0.43</td><td>50</td><td>0.62</td><td>0.63</td><td>0.64</td><td>0.64</td><td>0.63</td></tr><tr><td>120</td><td>0.20</td><td>0.20</td><td>0.21</td><td>0.21</td><td>0.21</td><td>120</td><td>0.37</td><td>0.39</td><td>0.38</td><td>0.39</td><td>0.38</td><td>120</td><td>0.59</td><td>0.60</td><td>0.61</td><td>0.61</td><td>0.60</td></tr><tr><td>240</td><td>0.16</td><td>0.16</td><td>0.17</td><td>0.18</td><td>0.17</td><td>240</td><td>0.31</td><td>0.32</td><td>0.32</td><td>0.33</td><td>0.32</td><td>240</td><td>0.55</td><td>0.57</td><td>0.58</td><td>0.58</td><td>0.57</td></tr><tr><td rowspan="4">HITS</td><td>30</td><td>0.17</td><td>0.17</td><td>0.20</td><td>0.17</td><td>0.18</td><td rowspan="4">HITS</td><td>30</td><td>0.30</td><td>0.31</td><td>0.31</td><td>0.32</td><td>0.31</td><td rowspan="4">HITS</td><td>30</td><td>0.64</td><td>0.65</td><td>0.66</td><td>0.66</td><td>0.65</td></tr><tr><td>50</td><td>0.12</td><td>0.16</td><td>0.16</td><td>0.18</td><td>0.16</td><td>50</td><td>0.25</td><td>0.25</td><td>0.26</td><td>0.27</td><td>0.26</td><td>50</td><td>0.61</td><td>0.61</td><td>0.62</td><td>0.61</td><td>0.61</td></tr><tr><td>120</td><td>0.08</td><td>0.08</td><td>0.10</td><td>0.12</td><td>0.10</td><td>120</td><td>0.21</td><td>0.22</td><td>0.25</td><td>0.25</td><td>0.23</td><td>120</td><td>0.57</td><td>0.56</td><td>0.58</td><td>0.58</td><td>0.57</td></tr><tr><td>240</td><td>0.07</td><td>0.10</td><td>0.09</td><td>0.13</td><td>0.10</td><td>240</td><td>0.20</td><td>0.21</td><td>0.23</td><td>0.23</td><td>0.22</td><td>240</td><td>0.54</td><td>0.53</td><td>0.55</td><td>0.54</td><td>0.54</td></tr><tr><td rowspan="4">PageRank</td><td>30</td><td>0.10</td><td>0.13</td><td>0.13</td><td>0.13</td><td>0.12</td><td rowspan="4">PageRank</td><td>30</td><td>0.25</td><td>0.24</td><td>0.24</td><td>0.24</td><td>0.24</td><td rowspan="4">PageRank</td><td>30</td><td>0.59</td><td>0.60</td><td>0.61</td><td>0.61</td><td>0.60</td></tr><tr><td>50</td><td>0.10</td><td>0.12</td><td>0.12</td><td>0.12</td><td>0.12</td><td>50</td><td>0.20</td><td>0.20</td><td>0.21</td><td>0.22</td><td>0.21</td><td>50</td><td>0.57</td><td>0.57</td><td>0.58</td><td>0.59</td><td>0.58</td></tr><tr><td>120</td><td>0.07</td><td>0.07</td><td>0.08</td><td>0.08</td><td>0.08</td><td>120</td><td>0.19</td><td>0.22</td><td>0.21</td><td>0.20</td><td>0.21</td><td>120</td><td>0.54</td><td>0.56</td><td>0.56</td><td>0.57</td><td>0.56</td></tr><tr><td>240</td><td>0.06</td><td>0.06</td><td>0.09</td><td>0.08</td><td>0.07</td><td>240</td><td>0.19</td><td>0.18</td><td>0.21</td><td>0.22</td><td>0.20</td><td>240</td><td>0.53</td><td>0.54</td><td>0.55</td><td>0.55</td><td>0.54</td></tr></table>

## Appendix F

## Case Studies

We demonstrate the evolution of true top-K lists of social foci and the efficacy of our prediction method using a case study. Examining the specific top-K item changes and the prediction breakdown in top-K lists will help understand the performance results in our benchmark evaluations, at a more concrete level.

## Analysis #1: Top-K List with Emerging Items

This case study analysis is conducted using Book Readership data with K =30. In Table F1, we show the true top-30 items in January 2016 along with the true top-30 items one month later in February 2016. The predicted top-30 items by our method in February 2016 are also provided for comparison. Items are encoded with 13-digits ISBN number.

Table F1. Demonstration: True Top-30 versus Predicted Top-30

<table><tr><td>Rank</td><td>True top-30 in Jan.</td><td>True top-30 in Feb.</td><td>Predicted top-30 in Feb.</td></tr><tr><td>1</td><td>9781443445238</td><td>9780399184413</td><td>9780399184413</td></tr><tr><td>2</td><td>9780812988406</td><td>9781338099133</td><td>9781770854703</td></tr><tr><td>3</td><td>9780385680912</td><td>9781501135910</td><td>9781338099133</td></tr><tr><td>4</td><td>9781476712109</td><td>9780385680912</td><td>9780451487155</td></tr><tr><td>5</td><td>9780553418026</td><td>9780812988406</td><td>9781476753914</td></tr><tr><td>6</td><td>9781501104565</td><td>9781476753652</td><td>9780316245418</td></tr><tr><td>7</td><td>9780670069323</td><td>9780316245418</td><td>9780672334436</td></tr><tr><td>8</td><td>9781250077486</td><td>9780385535595</td><td>9780385660044</td></tr><tr><td>9</td><td>9781443434867</td><td>9780385682312</td><td>9781422188613</td></tr><tr><td>10</td><td>9780312577223</td><td>9780307361172</td><td>9781476753652</td></tr><tr><td>11</td><td>9780062301239</td><td>9781443445238</td><td>9780771079665</td></tr><tr><td>12</td><td>9781594633881</td><td>9780544668256</td><td>9780613027823</td></tr><tr><td>13</td><td>9780307887443</td><td>9781607747307</td><td>9780307361172</td></tr><tr><td>14</td><td>9780804139298</td><td>9780399169472</td><td>9780385539258</td></tr><tr><td>15</td><td>9781476798172</td><td>9780143125471</td><td>9780385535595</td></tr><tr><td>16</td><td>9780525426615</td><td>9780804139298</td><td>9780544668256</td></tr><tr><td>17</td><td>9780062265432</td><td>9780553418026</td><td>9780385682312</td></tr><tr><td>18</td><td>9780544668256</td><td>9780771079665</td><td>9780812988406</td></tr><tr><td>19</td><td>9780307361172</td><td>9780062301239</td><td>9780143125471</td></tr><tr><td>20</td><td>9780066620992</td><td>9781594634474</td><td>9780385680912</td></tr><tr><td>21</td><td>9781476789255</td><td>9780670069323</td><td>9780061120084</td></tr><tr><td>22</td><td>9780262525671</td><td>9780676974034</td><td>9780307476074</td></tr><tr><td>23</td><td>9781476730752</td><td>9780062265432</td><td>9780804139298</td></tr><tr><td>24</td><td>9780771060540</td><td>9781476712109</td><td>9780061713804</td></tr><tr><td>25</td><td>9781594634710</td><td>9780345539847</td><td>9780062060242</td></tr><tr><td>26</td><td>9780887306662</td><td>9780743243315</td><td>9781476796055</td></tr><tr><td>27</td><td>9780394281827</td><td>9781476796055</td><td>9781443445238</td></tr><tr><td>28</td><td>9780345810090</td><td>9780307476074</td><td>9780062301239</td></tr><tr><td>29</td><td>9781476755748</td><td>9780385659802</td><td>9781501135910</td></tr><tr><td>30</td><td>9781594634475</td><td>9780451191144</td><td>9780062265432</td></tr></table>

Let us first explain notations using the true top-30 in February (i.e., 2nd column), where shaded ISBN numbers denote items that are carried over from the previous month, while the underscored bold ISBN numbers stand for items having newly emerged in February and not existed in January. For the predicted top-30 in February (i.e., 3rd column), shaded and underscored numbers have the same meaning while crossed ISBN numbers stand for prediction errors. Two observations are made in Table F1.

Observation (1): A considerable number of new top-K items emerge over time.

According to the second column, we count 19 out of 30 top-K items are newly emerged items which does not exist in true top-30 of the previous month. There are merely 11 out of 30 top-K items repeated from top-30 in January 2016 to top-30 in February 2016, which is consistent to the low average precision for BPM in the benchmarking results (e.g., BPM’s Precision is 0.41 in Table 9). The observation suggests that true top-K lists could change over time for certain domains. Hence using the previous true ranking list to predict for the next period turns out an ineffective forecasting approach in our data domains.

Observation (2): The predicted top-K list of our method captures newly emerged top-K items as well as carried-over top-K items.

From the third column, we learn that 11 out of 19 newly emerged top-K items are captured by the prediction of our method. In the meanwhile, our method can also predict 8 out of 11 carried over top-K items. The observation suggests that our method is not merely repeating the previous items but is able to capture emerging items.

## Analysis #2: Predicting Social Foci Becomes Less Popular

Since our method obtains the future rank of social foci, it should be able to predict which social foci are going to make the top-k as well as which are about to fall out. We have conducted the analysis to show whether the proposed method has this capacity. Given the predicted top-30 in Table F1 of analysis #1, our method has predicted 8 out of top-30 popular items are to be carried over to the next month. In another word, it has predicted 22 items to enter the new top-30 and 22 items to fall out from the previous top-30 list. To be specific, we have listed the book items that were top-30 in January and are predicted to fall out the top-30 in February; as well as th book items that were not among top-30 in January and are predicted to enter top-30 in February, as shown in the Table F2a and Tabl F2b. In which, book items are indexed by ISBN number, as before. The crossed ISBN items are incorrect predictions.

Given the results, we can observe that (1) predicting whom to fall out is correct for 19 items out of 22; (2) predicting new popular items is accurate for 11 out of 22 times. It suggests that the proposed method is capable to identify social foci who will become less popular and are about to drop out the top-K popular list. We are also noted by the relatively moderate accuracy in the second column. It may suggest that the interesting problem of predicting newly emerging social foci is somewhat harder and may be worth a separate stud down the stream.

We further investigate the capacity of predicting dramatic popularity drop in the number of ranking places. The pool has expanded to the top-100 items and analyzed their numbers of places dropped in popularity ranking. The following table illustrates the items that were among top-100 in January and their number of places dropped in popularity ranking during February. We have sorted the list by their predicted number of places dropped. Top-30 social foci with highest ranking drop are demonstrated in the table below, where the second column contains the predicted number of places to drop in ranking, by our method

According to the Table F3, the average absolute error for prediction is merely 7.3 in ranking places. The proposed method is found prominent in estimating the popularity rank drop, considering that the problem scale is very large.

<table><tr><td>Table F2a. Correct vs. Incorrect Social Foci that Are Predicted to Fall</td></tr><tr><td>The social foci that are predicted to fall out of the top-30 in February</td></tr><tr><td>9781501104565</td></tr><tr><td>9781250077486</td></tr><tr><td>9781443434867</td></tr><tr><td>9780312577223</td></tr><tr><td>9781594633881</td></tr><tr><td>9780307887443</td></tr><tr><td>9781476798172</td></tr><tr><td>9780525426615</td></tr><tr><td>9780066620992</td></tr><tr><td>9781476789255</td></tr><tr><td>9780262525671</td></tr><tr><td>9781476730752</td></tr><tr><td>9780771060540</td></tr><tr><td>9781594634710</td></tr><tr><td>9780887306662</td></tr><tr><td>9780394281827</td></tr><tr><td>9780345810090</td></tr><tr><td>9781476755748</td></tr><tr><td>9781594634475</td></tr><tr><td>9781476712109</td></tr><tr><td>9780553418026</td></tr><tr><td>9780670069323</td></tr></table>

<table><tr><td>Table F2b. Correct vs. Incorrect Social Foci That Are Predicted to Rise</td></tr><tr><td>The social foci that are predicted to enter the top-30 in Feb.</td></tr><tr><td>9780399184413</td></tr><tr><td>9781338099133</td></tr><tr><td>9780316245418</td></tr><tr><td>9781476753652</td></tr><tr><td>9780771079665</td></tr><tr><td>9780385535595</td></tr><tr><td>9780385682312</td></tr><tr><td>9780143125471</td></tr><tr><td>9780307476074</td></tr><tr><td>9781476796055</td></tr><tr><td>9781501135910</td></tr><tr><td>9781770854703</td></tr><tr><td>9780451487155</td></tr><tr><td>9781476753911</td></tr><tr><td>9780672334436</td></tr><tr><td>9780385660044</td></tr><tr><td>9781422188613</td></tr><tr><td>9780613027823</td></tr><tr><td>9780385539258</td></tr><tr><td>9780061120084</td></tr><tr><td>9780061713804</td></tr><tr><td>9780062060242</td></tr></table>

<table><tr><td colspan="4">Table F3. Predicted and True Ranking Drop for the Top-30 Dropped Social Foci</td></tr><tr><td>Top-30 dropped social foci</td><td>Predicted ranking drop</td><td>True ranking drop</td><td>Absolute Error</td></tr><tr><td>9780307887443</td><td>54</td><td>44</td><td>10</td></tr><tr><td>9780205309023</td><td>52</td><td>35</td><td>17</td></tr><tr><td>9780771060540</td><td>49</td><td>40</td><td>9</td></tr><tr><td>9781487000776</td><td>49</td><td>31</td><td>18</td></tr><tr><td>9781476730752</td><td>48</td><td>59</td><td>11</td></tr><tr><td>9780143197607</td><td>48</td><td>33</td><td>15</td></tr><tr><td>9781552453056</td><td>46</td><td>49</td><td>3</td></tr><tr><td>9781476789255</td><td>46</td><td>41</td><td>5</td></tr><tr><td>9780676971750</td><td>45</td><td>47</td><td>2</td></tr><tr><td>9780060883287</td><td>45</td><td>51</td><td>6</td></tr><tr><td>9780525426615</td><td>44</td><td>42</td><td>2</td></tr><tr><td>9780156012195</td><td>43</td><td>48</td><td>5</td></tr><tr><td>9781400098033</td><td>43</td><td>37</td><td>6</td></tr><tr><td>9781594633881</td><td>43</td><td>44</td><td>1</td></tr><tr><td>9781473613782</td><td>40</td><td>47</td><td>7</td></tr><tr><td>9780312577223</td><td>39</td><td>41</td><td>2</td></tr><tr><td>9780316017930</td><td>39</td><td>35</td><td>4</td></tr><tr><td>9781443431606</td><td>37</td><td>34</td><td>3</td></tr><tr><td>9781501104565</td><td>35</td><td>32</td><td>3</td></tr><tr><td>9781443412490</td><td>33</td><td>29</td><td>4</td></tr><tr><td>9780394281827</td><td>32</td><td>25</td><td>7</td></tr><tr><td>9780670026067</td><td>32</td><td>33</td><td>1</td></tr><tr><td>9781250095893</td><td>31</td><td>25</td><td>6</td></tr><tr><td>9780553418026</td><td>31</td><td>12</td><td>19</td></tr><tr><td>9780812979305</td><td>30</td><td>21</td><td>9</td></tr><tr><td>9781400067558</td><td>29</td><td>25</td><td>4</td></tr><tr><td>9781476712109</td><td>28</td><td>20</td><td>8</td></tr><tr><td>9780316067935</td><td>26</td><td>11</td><td>15</td></tr><tr><td>9781443445238</td><td>26</td><td>10</td><td>16</td></tr><tr><td>9780451209337</td><td>23</td><td>21</td><td>2</td></tr></table>

## Analysis #3: Comparison of Ranking Places Obtained by BLR and Our Method

To facilitate understanding of prediction errors made by our proposed method in relation to those made by BLR, we have conducted a further analysis using top-20 social foci. As shown in the Table F4, we have presented: (1) true rank of top-20 books (indexed by ISBN number), (2) respective ranks predicted by linear regression and our method, and (3) absolute errors made by linear regression and our method, in terms of ranking place. From the table, we observe that:

1. There are only two books (i.e., true rank #5 and #11) out of twenty where linear regression outperforms the proposed method;

2. Linear regression does make considerable errors in relation to our method. For example, the book truly ranked #2 is predicted to be #23 by BLR, while our method predicted it to be #3;

3. On average, the prediction error in ranking place is 17.95 for linear regression and 9.8 for our method, which occurs to be a noticeable difference.

Table F4. Ranking Places Comparison between Baseline Linear Regression (BLR) and Our Method

<table><tr><td>True Rank</td><td>Top-20 in February</td><td>Rank By linear regression</td><td>Error By linear regression</td><td>Rank by our method</td><td>Error By our method</td></tr><tr><td>1</td><td>9780399184413</td><td>13</td><td>12</td><td>1</td><td>0</td></tr><tr><td>2</td><td>9781338099133</td><td>23</td><td>21</td><td>3</td><td>1</td></tr><tr><td>3</td><td>9781501135910</td><td>35</td><td>32</td><td>29</td><td>26</td></tr><tr><td>4</td><td>9780385680912</td><td>28</td><td>24</td><td>20</td><td>16</td></tr><tr><td>5</td><td>9780812988406</td><td>16</td><td>11</td><td>18</td><td>13</td></tr><tr><td>6</td><td>9781476753652</td><td>18</td><td>12</td><td>10</td><td>4</td></tr><tr><td>7</td><td>9780316245418</td><td>15</td><td>8</td><td>6</td><td>1</td></tr><tr><td>8</td><td>9780385535595</td><td>19</td><td>11</td><td>15</td><td>7</td></tr><tr><td>9</td><td>9780385682312</td><td>29</td><td>20</td><td>17</td><td>8</td></tr><tr><td>10</td><td>9780307361172</td><td>32</td><td>22</td><td>13</td><td>3</td></tr><tr><td>11</td><td>9781443445238</td><td>4</td><td>7</td><td>27</td><td>16</td></tr><tr><td>12</td><td>9780544668256</td><td>21</td><td>9</td><td>16</td><td>4</td></tr><tr><td>13</td><td>9781607747307</td><td>39</td><td>26</td><td>31</td><td>18</td></tr><tr><td>14</td><td>9780399169472</td><td>43</td><td>29</td><td>33</td><td>19</td></tr><tr><td>15</td><td>9780143125471</td><td>34</td><td>19</td><td>19</td><td>4</td></tr><tr><td>16</td><td>9780804139298</td><td>38</td><td>22</td><td>23</td><td>7</td></tr><tr><td>17</td><td>9780553418026</td><td>49</td><td>32</td><td>36</td><td>19</td></tr><tr><td>18</td><td>9780771079665</td><td>10</td><td>8</td><td>11</td><td>7</td></tr><tr><td>19</td><td>9780062301239</td><td>7</td><td>12</td><td>28</td><td>9</td></tr><tr><td>20</td><td>9781594634474</td><td>42</td><td>22</td><td>34</td><td>14</td></tr><tr><td></td><td></td><td>Average error</td><td>17.95</td><td>Average error</td><td>9.8</td></tr></table>

## Appendix G

## Evaluation Metrics

For performance metrics, evaluating the proposed method is to essentially compare two ranking lists of social foci - Predicted Rank and True Rank. Predicted rank (PR) is a ranked list of predicted popular social foci given by methods in evaluation; meanwhile true rank (TR) is the ranked list of true popular social foci based on observed number of adopts. Given PR and TR lists, we adopt four metrics to evaluate the performance of methods: top-K Precision (Precision), Average Precision (AP), Area under the ROC Curve (AUC), and Kendall Tau Coefficient (Tau). The top-K precision calibrates the degree of overlap between top ranked ?? items from TR and PR, which is given b

$$
P r e c i s i o n (K) = \frac {| T R _ {K} \cap P R _ {K} |}{K}
$$

where $T R _ { K }$ denotes the set of top-?? social foci in the true ranking list ???? while $P R _ { K }$ is the set of top-?? social foci in the predicted list ????. The integer ?? ranges over [1, |??|]. Higher valued Precision means more social foci are predicted correctly within the first K items.

The average precision $( \mathrm { i } . \mathrm { e } . , A P )$ measure is used in evaluating the outcome of information retrieval tasks for its good discrimination and stability (Ponte et al. 1998). It gauges the average precision of predicting top-?? lists with different size k. More precisely, let ????(??) denote the ??th social focus in the true rank ???? for ${ \bar { 1 } } \leq k \leq K$ . Given a social focus $f ,$ we let $P R ^ { - 1 } ( f )$ denote its rank number in the predicted list ????. The definition of metric AP is thus given by

$$
A P (K) = \frac {\sum_ {k = 1} ^ {K} P r e c i s i o n (P R ^ {- 1} (T R (k)))}{K}
$$

As shown, the value of AP depends not only on the intersection of $T R _ { K }$ and $P R _ { K }$ , but also on where each top-K element in $T R _ { K }$ is located in the entire ???? list.

We employed another performance measure AUC, namely the area under the ROC curve (Fawcett 2006). AUC is a standard metric for assessing methods that prioritize testing instances in machine learning tasks, such as classification or ranking. According to (Fawcet 2006), AUC equals to the probability that a randomly chosen positive instance will be prioritized in ahead of a randomly chosen negative instance. In our case, AUC demonstrates the probability that a randomly chosen top-K social focus will receive more adoptions than a randomly chosen non-top-K social focus does, hence ranked higher in PR. In particular, we define the top-?? social foci in the ???? list as truly positive and regard all others as truly negative. Given ????, we count all pairs of truly positive and truly negative, and denote the number of possible pairs as $C _ { a l l } .$ Among all these pairs, we count the number of pairs where truly positive is ranked above truly negative in the ???? list, and denote this number as $C _ { p n }$ . Thus ?????? is given by

$$
A U C (K) = \frac {C _ {p n}}{C _ {a l l}}
$$

in which, AUC value ranges over [0,1]. The underlying predictor is preferred when ?????? value approaches 1. The case $A U C = 0$ means the focal method can never predict any truly popular social foci in the output top-?? list $P R _ { K }$ while $A U C = 0 . 5$ stands for random guessing.

The Kendall Tau Coefficient (Tau) is adopted to measure the consistency of pairwise order between ranked lists TR and PR. It quantifies an ordinal rank-based correlation given two lists. Let prediction $P R = \{ \delta _ { 1 } , \delta _ { 2 } , \dots , \delta _ { | F | } \}$ be a ranked list of social foci. We know from prior parts that ≺ denotes the preceding relationship in TR. For $m , n \in ( 1 , | F | )$ , a pair of $( \delta _ { m } , \delta _ { n } )$ is considered concordant if $\delta _ { m }$ precedes $\delta _ { n }$ in PR and $\delta _ { m } \prec \delta _ { n }$ or $\delta _ { n }$ precedes $\delta _ { m }$ in PR and $\delta _ { n } \prec \delta _ { m } ;$ otherwise it is deemed discordant. Therefore, performance metric Tau is computed by

$$
T a u = \frac {| C o n c o r d a n t p a i r s | - | D i s c o r d a n t p a i r s |}{| F | \times (| F | - 1) / 2}
$$

where |F| is the cardinality of social foci set that equals to the length of TR or PR. The denominator refers to the possible number of social foci pairs. Since it computes over the whole ???? list, correlation coefficient Tau does not depend on K value. The value of Tau ranges from -1 to 1. The method is perfect when Tau = 1 and implies random guessing when Tau = 0.

## Appendix H

## Discussion on Selection Bias

To further address the concern in selection bias, we have collected an observed real-world ranking and compared it against our ranking in the evaluation data. To be specific, we have purchased the book sales data for the first half of year 2016 in Canada since the book readership data was collected from the same region during the same time span. The purchased data cover the aggregated sales of all books for the region and the time. Thus, we can rank books by their sales volume. We have adopted Kendall’s Tau coefficient to measure the correlation between the real-world sales rank and the popularity rank in our evaluation data. For instance, we have compared the sales rank list in the real world against the true popularity rank list from our data in January. The result shows that the Tau coefficient is around 0.81. It reveals a relatively small difference between our popularity ranking and book sales ranking. The finding suggests that our evaluations are not subject to a severe selection bias problem. Nonetheless, the authors would like to point out that the collected real-world book sales data cover about 85% of offline stores and do not include online sales. This limitation could become an issue if the ranking of books in online and offline sales were dramatically different. Furthermore, a separate study might be needed to systematically address the selection bias issue.
