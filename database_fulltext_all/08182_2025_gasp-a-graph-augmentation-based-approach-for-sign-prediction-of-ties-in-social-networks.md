---
otero_id: 8182
otero_key: "VJCRW7RC"
title: "GASP: A Graph Augmentation-Based Approach for Sign Prediction of Ties in Social Networks"
authors: "Mukul Gupta; Samrat Gupta; Giri Kumar Tayi"
year: "2025"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00941"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
2025

# GASP: A Graph Augmentation-Based Approach for Sign Prediction of Ties in Social Networks

Mukul Gupta , mukulg@iimidr.ac.in

Samrat Gupta , samratg@iima.ac.in

Giri Kumar Tayi , gtayi@albany.edu

Follow this and additional works at: https://aisel.aisnet.org/jais

ISSN 1536-9323

# GASP: A Graph Augmentation-Based Approach for Sign Prediction of Ties in Social Networks

Mukul Gupta,<sup>1</sup> Samrat Gupta,<sup>2</sup> Giri Kumar Tayi<sup>3</sup>

<sup>1</sup>Department of Information Systems, Indian Institute of Management Indore, India, mukulg@iimidr.ac.in <sup>2</sup>Department of Information Systems, Indian Institute of Management Ahmedabad, India / University of Agder, Norway, samratg@iima.ac.in

<sup>3</sup>Management Science and Information Systems, University at Albany, SUNY, USA, gtayi@albany.edu

## Abstract

This paper proposes a method for the sign prediction of ties in social networks using a design science research process. The proposed method is grounded in social network analysis and leverages the tenets of graph augmentation and a graph regularized framework for information diffusion. To the best of our knowledge, this is the first study that develops a sign prediction method for social networks based on the principles of design science research. This study makes several contributions. We demonstrate the utility and applicability of the proposed method for predicting trust/distrust on a user-user network created from the IMDb platform, which represents ties between reviewers based on their movie evaluation preferences. We describe and discuss the novel aspects of graph augmentation, symmetric normalization of the affinity matrix, and graph regularized label propagation, and discuss their synergistic use to predict the signs of network ties. We also establish the effectiveness of the proposed method by comparing its performance with two different metrics for balanced networks and two metrics for unbalanced networks using four state-of-the-art methods. The benchmarking networks used for experiments originate from online platforms such as Slashdot, Epinions, Wikipedia, and the Yeast Genetic Interaction Network from the biology domain. Experiments show that the proposed method provides significant performance improvements in the sign prediction of ties in social networks. This study provides valuable insights for social media platform owners seeking to improve their platforms by building new features and business leaders seeking to target advertisements and personalized content to users. We also discuss the theoretical, practical, and societal implications of this research.

Keywords: Sign Prediction, Design Science, Social Network Analysis, Social Media, Online Platforms

Kim Huat Goh was the accepting senior editor. This research article was submitted on November 12, 2023, and underwent two revisions.

## 1 Introduction

## 1.1 Motivation

How can the information about signs of social network ties be made salient on social media platforms? This is a crucial question for many knowledge managers, marketers, and organizational leaders (Kane et al., 2014). As the economic impact of social media platforms on businesses is increasing (Das et al., 2022; Drenik, 2022), with platform features formalizing the nuanced capabilities of entities within social media networks (such as followers or friends, individual or organization), increased attention is being directed toward articulating the relational meanings of ties (i.e., whether the relationship is positive or negative) (Katona et al., 2011; Stieglitz & Dang-Xuan, 2013; Krasnova et al., 2015).

Though negative ties only constitute 3-8% of relationships in any organization, they have a greater effect on task and socioemotional outcomes than positive relationships (Kane et al., 2014). For example, for an individual who otherwise has positive (or neutral) relationships at work, even one negative relationship can pose a serious risk to their financial and emotional stability and can threaten the productive functioning of the organization as a whole (Labianca & Brass, 2006).

As such, the research findings regarding the effects of social media use on users’ subjective well-being are unclear. Some studies have identified positive consequences of social media use, such as life satisfaction, while others have suggested that social media participation leads to undesirable states such as anxiety, depression, and narcissism (Apaolaza et al., 2013; Bergman et al., 2011; Valenzuela et al., 2009).

Participation on social media platforms under certain conditions may proliferate social comparisons and feelings of envy, thereby triggering the development of negative relationships (Lee, 2014; Krasnova et al., 2015). As negative feelings, judgments, and behavioral intentions toward others in a network recur, negative relationships stabilize (Labianca & Brass, 2006). However, most of the existing research on social networks and social media platforms has ignored the notion of negative ties, considering ties as neutral or positive only (i.e., relationships of friendship, support, trust, or love).

The identification and labeling of negative ties in social networks is an emerging phenomenon, constituting a gap in social network (and social media) research that has limited the emergence of a diverse repertoire of theories and methodologies for understanding complex business and societal phenomena (Brzozowski et al., 2008; Casciaro & Lobo, 2008; Leidner, 2020). Identifying negative relationships in social networks can improve the understanding of the complete social ledger (potential liabilities and potential benefits of social relationships) within organizational and societal settings (Labianca & Brass, 2006). Therefore, as social networking sites are redefined and new social media platforms emerge, many organizations are grappling with decisions on how to build and deploy technological capabilities that can consider the signs of network ties (Boyd & Ellison, 2007; Maier et al., 2015) in a meaningful way.

In considering tie signs in a network, the underlying challenge is labeling the ties with their respective signs. Manually labeling ties with positive or negative signs in social networks may not be feasible due to the size of the network or the lack of expertise or domain-related information. Moreover, information about the signs of all ties may not be available since negative relationships (envy, distrust, enmity, dislike) are based on secretive emotions that individuals generally seek to avoid revealing (Greene et al., 2006; Krasnova et al., 2015). Therefore, the complementary use of predictive methods to mitigate the lack of information about the signs of network ties is sorely needed. Although some social media platforms allow users to recognize negative ties (Brzozowski et al., 2008), a common approach for dealing with negative ties in social media networks is to simply enable users to disregard negative relationships. For example, Facebook allows users to “hide” information from specific users, and on X (formerly Twitter), users can prevent certain individuals from following them. The ability to manage negative relationships in a social network emanating from a social media platform may be critically important for the platform’s functioning (Kane et al., 2014). The explicit expression of such negative ties might result in strengthened relationships among some users (e.g., opposing a common connection, celebrity, or politician can prompt some users to deepen relationships), thus providing more value for the platform. The availability of information about the signs of social media network ties can also help in studying opinion diffusion-driven prediction of stock returns, recommending products or services, and studying social media-induced polarization (Chen et al., 2014; Kitchens et al., 2020; Stieglitz & Dang-Xuan, 2013). Therefore, methods for predicting relationship signs in social media networks have an immense potential to impact businesses and society alike.

## 1.2 Problem Scope or Statement

To this end, we developed an artifact guided by the design science research (DSR) process framework (Gregor & Hevner, 2013; Peffers et al., 2007), a salient framework originating in the information systems discipline, for generating sign predictions in a social network of users from any social platform. We mapped different stages of the proposed artifact with the activities of the DSR framework. Due to the scarcity of signed network datasets, prior research recommends the evaluation of proposed artifacts for signed networks in (a limited number of) publicly available benchmark networks providing tie sign information and in networks from social media platforms on which signs can be inferred based on user activities (Kirkley et al., 2019; Leskovec et al., 2010a, 2010b). Following this recommendation, we leveraged the IMDb platform to scrape data related to user-movie ratings for the creation of a trust/distrust network (positively and negatively labeled links) among users. Adhering to the DSR process, we demonstrated the utility and applicability of the proposed artifact for predicting trust/distrust on the aforementioned user-user network created from this platform.

IMDb is the world’s most authoritative source for information related to movie ratings and reviews (Gupta et al., 2024; Schoenmueller et al., 2020). Users rate movies and TV shows on IMDb, and these ratings help IMDb provide users with personalized recommendations. Recommended titles are shown under “Top picks” in the “What to watch” section on the IMDb homepage. Figure 1 shows an example of the role of signs (based on users’ movie ratings) in improving movie recommendations. Similarly, YouTube uses the “like” feature on videos for recommendations. These recommendations can provide targeted online video advertising leads for various products and services. Since relationship signs may be unknown or only partially known, recommendations are traditionally performed based on similarity, i.e., trust/friendship (positive aspect of relationships), while ignoring dissimilarity, i.e., distrust/enmity (negative aspect of relationships) (Fast et al., 2023; Liebman et al., 2019). Recommendations can be further improved by considering relationship signs (trust/distrust, like/dislike, helpful/unhelpful) among reviewers/commenters that are implicitly formed when users review online content. Therefore, sign prediction in networks can help social media platforms present the right content at the right time to the right users. Social media platforms such as Tripadvisor, Yelp, etc., can use trust/distrust user relationship information to improve the recommendation performance of content, products, and services (Richa & Bedi, 2021; Victor et al., 2011; Wang et al., 2018).

We evaluated the effectiveness of GASP using four diverse signed social network benchmark datasets originating from different contexts. Each of the benchmark networks covered a different social phenomenon in the real world. The first network emerged from requests submitted by community members or candidates for adminship on Wikipedia, with supportive, neutral, or opposing votes cast by Wikipedia members. This results in a network consisting of distinct voter/votee pairs. The second network originated from Epinions (later acquired by Shopping.com), an online marketplace for writing and accessing reviews about products and services. Users on Epinions could indicate trust (positive) or distrust (negative) relationships with each other. The third network was derived from Slashdot, a social news platform featuring news on technology, science, and politics submitted by users and evaluated by editors. During its early years of inception, Slashdot introduced the Zoo feature, which allowed users to tag each other as friends or foes. Finally, to validate the generalizability of the proposed method, we considered a network emerging from a biology context—a genetic interaction network of yeast. Information systems studies investigating social networks have previously used the biology context since molecular networks can provide a comprehensive understanding of complex systems (Danger et al., 2014; Gupta & Mishra, 2020; Kumar et al., 2017).

![](/api/attachments/VJCRW7RC/fulltext/images/1862de1196e756ebbf778caa78c7f43b3b874f515ede1f05db65cf0f145d038c.jpg)  
Figure 1. An Example of the Role of Sign Prediction in Making Movie Recommendations by Social Media Platforms such as IMDb

## 1.3 Research Questions

Most earlier approaches have used structural balance theory to predict tie signs in social networks (Pang et al., 2021; Leskovec et al., 2010b; Lee et al., 2020; Xu et al., 2022). However, given the theoretical problems with structural balance theory, a nuanced understanding of social networks and sign prediction of network ties is needed (Kirkley et al., 2019; Leskovec et al., 2010a). For instance, the assumption of balanced triads considers the possible signs between three individuals positioned in a triangle (see Figure 2), positing that triangles with three positive signs (three mutual friends) and those with one positive sign (two friends and a common enemy) are more plausible (and hence likely more prevalent in real networks) than triangles with two positive signs (two enemies and a common friend) or none (three mutual enemies). Reflecting the theoretical tension regarding this criterion for considering structural balance, some researchers have argued that it is a stringent criterion and that while triangles with two positive ties (two enemies and a common friend) are implausible in real networks, triangles with no positive ties (three mutual enemies) are plausible (Kirkley et al., 2019; Leskovec et al., 2010a). Another theoretical problem with structural balance theory arises due to the assumption of transitivity in social networks, which can have different notions (Leskovec et al., 2010a). For instance, a signed link from A to B can have more than one possible interpretation: a positive link from A to B may signify A’s friendship with B, but it could also signify that A considers B to have a higher status (than A). Similarly, a negative link from A to B may signify that B is an enemy of A or that B has a lower status than A. Given this, if A links positively to B, and B in turn links positively to C, the sign of the link from C to A should be positive according to the notion of friendship but negative according to the notion of status (Leskovec et al., 2010a). There have been some attempts to overcome the limitations of structural balance theory— for example, a global network structure has been used to make sign predictions on unlabeled ties (Aggarwal et al., 2016; Gupta & Mishra, 2020; Jung et al., 2020). However, these approaches have been found to be ineffective (in terms of prediction accuracy) due to limitations that lead to information loss. To this end, we pose the following theoretical questions:

Can the prediction of tie signs in social networks be enhanced by synergistically using partially available tie sign information in the context of a network’s structural information?

Can the prediction of tie signs in social networks be enhanced by moving beyond the traditional notions of triadic balance and the transitivity of relationships?

In this study, we address these questions by designing a domain-independent methodology to overcome the limitations of earlier work on the sign prediction of ties in social networks. The two main strategies of the proposed artifact are: graph augmentation by converting labeled ties into labeled nodes and random walk-based graph regularized transductive label propagation. The proposed artifact is termed graph augmentation-based sign prediction (GASP). GASP augments the signed network by converting labeled edges<sup>1</sup> into labeled edge nodes. Using this augmented network, the similarity between nodes is computed, resulting in an affinity matrix. Using this affinity matrix, GASP performs random walk-based graph regularized transductive label propagation for the labeling of the unsigned edges in the network using the prior label information of the signed edges.

## 1.4 Contributions

## 1.4.1 Theoretical Contributions

The existing approaches for the sign prediction of edges in social networks can be categorized mainly into three streams. The first stream focuses on decompositionbased approaches, which reduce complexity through projection or use domain-specific knowledge to make sign predictions (Pang et al., 2021; Gupta & Mishra, 2020). However, such approaches often face challenges related to information loss and generalization due to decomposition and/or reliance on a specific domain. The second stream involves using statistical and random walk-based models to infer edge signs (Jung et al., 2020; Aggarwal et al., 2016; Leskovec et al., 2010b). These approaches struggle with sparsity because they discard unlabeled edges. The third-stream leverages propagation- and embedding-based techniques to predict edge signs (Guha et al., 2004; Lee et al., 2020; Xu et al., 2022). These approaches generate embeddings and then isolate positive and negative subgraphs or proximities, leading to information loss. We elaborate on the specific approaches within these three streams in Section 2 (Table 1). In this study, we address the shortcomings of these approaches by synergistically combining graph augmentation, symmetric normalization, information diffusion, and label propagation. In doing so, this study offers several theoretical contributions, straddling the divide between decomposition-based approaches, statistical and random walk-based approaches, and propagation and embedding-based approaches.

First, doing away with structural balance theory and its assumptions of balanced triads and transitivity of relationships (Cartwright & Harary, 1956; Harary et al., 1965), this study develops a novel and principled approach where each tie iteratively propagates its sign information to its neighbors until a globally stable state is reached. Second, in contrast to existing approaches, the proposed approach overcomes information loss by using affinity matrix propagation and graph augmentation to preserve all edge relationships, including unlabeled ones. Third, the graph-regularized framework incorporates both local neighborhood structure as well as global graph properties, where unlabeled ties iteratively receive information from their neighbors while retaining prior information, leading to superior sign prediction even in sparse networks. Fourth, the proposed artifact does not rely on domain-specific knowledge and is adaptable to varying levels of sparsity, making it broadly applicable to diverse networks and scalable to large networks. Fifth, the proposed artifact demonstrates how the available information about a network can be complemented and leveraged for better learning of the intrinsic structure of a signed network while facilitating algorithmic convergence. Finally, this study contributes to the design science research paradigm by helping to build a cumulative research tradition of developing novel computational artifacts for addressing business and societal problems (Gregor & Hevner, 2013; Gupta & Tiwari, 2022; John et al., 2016; Leidner, 2020; Peffers et al., 2007; Velichety & Ram, 2020). This study also puts forth a set of design guidelines that can benefit future design problems with similar characteristics.

## 1.4.2 Practical Contributions

This study also makes contributions to the practical aspects of social networks. First, this study serves as a generative mechanism for the needs-affordancesfeatures perspective on social media, according to which the psychological needs of users motivate social media use depending on the extent to which social media platforms provide affordances to satisfy these needs (Karahanna et al., 2018; Leonardi, 2011; Turel & Qahri‐Saremi, 2023). For example, features labeling network ties as positive or negative can enable a social media affordance to fulfill the psychological need for autonomy. Second, this study presents a domain-independent approach to label ties in a social network for which sign information is not available. GASP is generalizable and applicable to social networks emanating from varied domains. GASP performs the integration of graph augmentation and graph-regularized transductive label propagation, which is important for the problem considered here. The novel combination of these two methods performs effectively in that it prevents the loss of information by not requiring the creation of separate positive and negative subgraphs from the original graph. Therefore, the complete information given is utilized for sign prediction of unlabeled edges in the network. The combination of graph augmentation and graphregularized transductive label propagation is novel and is associated with performance gains. For sign prediction of ties in social networks, the performance of GASP is superior to state-of-the-art diverse approaches such as random walk-based signed random walk with restart (SRWR), deep learning-based adversarial signed network embedding (ASiNE), dual-branch density ratio estimation (DDRE), and the network projection-based edge classification framework (NPECF) (Jung et al., 2020; Lee et al., 2020; Xu et al., 2022; Gupta & Mishra, 2020).

## 2 Literature Review

In any relationship, negative interactions, thoughts, or actions occasionally occur; thus, relationships, in general, have both positive and negative aspects (Labianca & Brass, 2006). Individuals weigh the various consequences (i.e., costs and benefits)—of their connections with others and decide whether to break off or maintain relationships based on these judgments (Gersick et al., 2000). People thus develop general “dislike” and “like” judgments about others. The dislike may be mild or intense, depending on personal associations, preconceptions, whims, envy, or specific objections to the other’s social or professional behavior or performance (Krasnova et al., 2015). It is crucial to understand that conflict encounters and negative relationships are not the same (Labianca et al., 1998; Venkataramani et al., 2013). Negative encounters between people are possible without forming negative relationships. On the other hand, there may be no overt or covert conflict between two people who dislike each other. Negative relationships represent an enduring, recurring set of negative judgments, feelings, and behavioral intentions toward another person (Labianca & Brass, 2006). The needs-affordances-features theoretical lens has emphasized the importance of generating methods for identifying the salient affordances of social platforms (Karahanna et al., 2018). Research contributing to the aforementioned theoretical premise has started to emerge but is still in its nascent stage (Chen et al., 2020; Sajtos et al., 2023).

In line with the aforementioned stream of research, we posit that sign prediction for ties in social networks holds importance for various business and societal applications such as recommendation systems, community detection, influence maximization, and anomaly detection. In social network research, label prediction for nodes (also known as node classification) is a problem that has been widely researched and several methods have been proposed (Gupta & Mishra, 2020; Leskovec et al., 2010b). However, the problem of sign prediction for ties in social networks is comparatively challenging because of the idiosyncratic nature of ties versus nodes (Aggarwal et al., 2016; Gupta & Kumar, 2020; Jung et al., 2020).

Structural (or social) balance theory is useful for understanding the origin and structure of negative relationships between individuals in a social network (Cartwright & Harary, 1956). This relationship structure between individuals is represented as a signed social network in which the cycles in the network with negative ties are the potential source of tension between individuals (Cartwright & Harary, 1956). As shown in Figure 2, the connected network triads or triangles (cycles of length three) are considered balanced when they are positive (Cartwright & Harary, 1956).

Based on structural balance theory, several methods have been proposed for the sign prediction of network ties. These methods require domain information, and the network should be balanced in terms of structural balance theory, as most of these methods use tie features derived from structural balance theory. The formulations of structural balance theory often make simplifying assumptions about the nature of relationships, such as transitivity, which may not fully represent the intricacies of real social networks (Harary et al., 1965). Also, the assumptions of balanced triads may not be satisfied in all domains, which may limit the applicability and effectiveness of methods based on structural balance theory (Jung et al., 2020; Stein et al., 2023).

Pang et al. (2021) proposed a method called the sign prediction model by tri-domain relationship pattern (SP-TDRP), utilizing knowledge of the network domain. This method performs knowledge transfer from one domain to the domain of interest for sign prediction. Another method, called LOGIT utilizes the logistic regression model for predicting the label of a tie selected arbitrarily from all the network ties (Leskovec et al., 2010b). This method proposes using several features for ties derived from the application of structural balance theory. Another trust/distrust propagation-based approach called TRUST depends on the domain, and its applicability depends on the problem circumstance and is also specific to the network (Guha et al., 2004). Also, deep learning-based methodologies have been proposed for sign prediction: ASiNE (Lee et al., 2020) and

DDRE (Xu et al., 2022) are methods that generate lowdimensional embeddings for the network, which can be utilized for the sign prediction of unlabeled ties in the network. ASiNE generates low-dimensional embeddings by considering the positive and negative subgraphs from the original signed network and then performs adversarial learning (Lee et al., 2020). DDRE proposes a dual-branch density ratio estimation architecture for expected matrix factorization for proximity computation separately for positive and negative graphs (Xu et al., 2022) for embedding generation.

Other methods have also been proposed for the sign prediction of ties that do not require domain information. Domain independence enhances the applicability and generalizability of these methods (Aggarwal et al., 2016; Gupta & Mishra, 2020; Jung et al., 2020). Recently, methods like NbA (neighborhood-based algorithm), SRWR, and NPECF have been proposed to predict tie signs in networks (Jung et al., 2020; Gupta & Mishra, 2020). These methods are domain-independent and can predict the label of unsigned ties based on network structure only. NbA is based on the local neighborhood and considers the ties incident on the nodes in their local neighborhood, i.e., considering nodes that are directly connected to the node while predicting the label of unsigned ties (Aggarwal et al., 2016). Therefore, the performance of the NbA is not effective, as many of the ties are unlabeled, and the real-world networks are typically sparse (Gupta & Mishra, 2020). SRWR is based on the signed random walk (Jung et al., 2020). The tie sign determines the sign of the random walker after passing through it. Based on this, once the convergence is achieved by the random walker, the tie sign can be predicted. In SRWR, to predict the label of unsigned ties, all unsigned ties are removed, and then the method is applied. This removal may lead to an unconnected network, and when the ties are highly sparsely labeled initially, the accuracy of the method may be significantly affected.

![](/api/attachments/VJCRW7RC/fulltext/images/1026a1b7755a7a85f4650dae862a37cfa14721bb09bdacaeeebb17128447b58b.jpg)  
Note: Blue edges represent the friendship (positive relationship) between nodes, and red edges represent enmity (negative relationship) between nodes. In these triangles, Nodes A and B are directly connected and also connected through Node C. The sentences corresponding to different triangles show the relationship between Nodes A and B.  
Figure 2. Simplest Cases of Balanced Triangles Following Structural Balance Theory

NPECF was also proposed to predict the sign of network ties. This method projects the signed networks into three projection networks, i.e., projection with positive labeled ties and unlabeled ties, projection with negative labeled ties and unlabeled ties, and projection with all ties without signs. Using these three projections, NPECF computes the probability of the unlabeled ties belonging to the positive class and negative class by means of the random walk-based method SimRank (Jeh & Widom, 2002). NPECF method has shown better performance than NbA and SRWR even when the ties are scarcely labeled. However, NPECF does not consider the whole network in one go and results in information loss (Gupta & Mishra, 2020).

Considering the limitations of the previously discussed work in the domain of sign prediction for network ties, this study proposes a novel method based on graph augmentation. In the augmented graph, we have a network in which the labeled ties of a partially signed social network are represented as nodes with the label information called edge nodes. Using this augmented graph, we can perform transductive learning by propagating the sign information of the ties in the network for the sign prediction of unlabeled ties. Thus, the proposed method (GASP) considers the whole network, and there is no information loss, as the whole network with positive and negative sign information is simultaneously considered when the label information is propagated. Also, by using this augmented graph, we can measure the affinity between nodes, which would be useful for improving accuracy while performing transductive learning. Apart from this, GASP uses the graph regularized framework for sign prediction, which further improves the accuracy of the prediction, as the graph regularization controls for overfitting while learning the sign of the edges. GASP does not require assumptions of relationship transitivity or balanced triads in a signed network to predict the sign of the unlabeled edges in the network. Table 1 provides a summary of the related work. Methods like NPECF, LOGIT, and TRUST can use both balanced and imbalanced datasets after preprocessing in terms of positive and negative ties in social networks.

## 3 Research Methodology

This study follows the design science research approach for developing the proposed method (Gregor & Hevner, 2013; Peffers et al., 2007). Previously, DSR has been used to introduce a pedagogical framework for developing computational thinking skills (Gupta & Tiwari, 2022), a recommendation method for online communities of interest to social media platform users (Velichety & Ram, 2020), and a graph theoretic approach to identify similar questions on social question answering platforms (John et al., 2016). According to the DSR knowledge contribution framework, a research study can be positioned as routine design (high application domain and solution maturity), exaptation (low application maturity and high solution maturity), improvement (high application domain and low solution maturity), and invention (low application domain and solution maturity) (Gregor & Hevner, 2013). This study contributes to DSR knowledge as an improvement by providing a new solution to a known problem. To develop the proposed method for the sign prediction of ties in social networks, we used a DSR process model comprising six stages, namely problem identification and motivation, objectives of the solution, design and development, demonstration, evaluation, and communication (Peffers et al., 2007). Figure 3 presents the mapping of the sections of our research to the stages of the specific DSR process that we adopted for this study and illustrates how these sections and stages map to the broader framework of the DSR paradigm (Gregor & Hevner, 2013; Peffers et al., 2007).

The numbered sections of this paper correspond to the six stages of our DSR process. First, in Section 1, we introduce the study by identifying the problem of sign prediction of network ties; we discuss the motivation behind solving this problem in the real world and underscore the significance of the problem through a diagrammatic illustration for recommending content on the IMDb platform (Figure 1). We also pose two research questions that guide the design of the solution. Next, in Section 2, we present the prior research works relevant to this study, including empirical research studies, theories, methods, and findings from practice. In the current section, Section 3, we emphasize the adoption of the DSR approach of Peffers et al. (2007), consisting of six stages and a design-and developmentcentered approach, as shown in Figure 3.

In Section 4, we describe the artifact. The artifact was designed in two phases. In the design and development phase, we computed different types of matrices to meet the desired objectives. First, we performed graph augmentation by converting labeled ties to labeled nodes. Then we used Jaccard similarity to compute the affinity matrix of the augmented graph. Subsequently, the diagonal weighted degree matrix and affinity matrix were used to compute the symmetric normalization of the affinity matrix. Then, to perform label propagation in the network, we iteratively used the column-normalized prior label information matrix and a hyper-parameter to control for the effect of the information diffusion. This iterative process was continued to refine the node scores until they converged, and signs were determined using the converged scores. We also assessed the space complexity of the proposed solution. Then, in the demonstration phase, we used the proposed method for labeling a network of users emanating from the IMDb platform and explained the results. This is in line with the recommendation of previous research proposing that artifacts for signed networks should be evaluated against publicly available benchmark networks where tie sign information is provided, as well as on networks derived from social media platforms where signs could be inferred based on user activities (Kirkley et al., 2019; Leskovec et al., 2010a; Leskovec et al., 2010b).

In Section 5, we discuss the evaluation phase and compare the performance of the proposed artifact (GASP) with four state-of-the-art methods on four benchmark datasets using two evaluation metrics each for balanced connected component and imbalanced connected component. Finally, in Section 6, we present the communication phase and discuss the significance of GASP, proposing four design guidelines that researchers can use to solve similar design problems in network settings. We conclude this section by discussing theoretical implications, practical implications, limitations, and future research directions.

Table 1. Summary of Related Work

<table><tr><td rowspan="2">Method name</td><td colspan="2">Network used in experiments</td><td rowspan="2">Based on structural balance theory/status theory</td><td rowspan="2">Brief description</td><td rowspan="2">Limitation(s)</td></tr><tr><td>Balanced</td><td>Imbalanced</td></tr><tr><td colspan="6">Decomposition-based approaches</td></tr><tr><td>SP-TDRP, Pang et al., 2021</td><td></td><td>√</td><td>Yes</td><td>Performs the knowledge transfer from one domain to the domain of interest</td><td>Requires the domain knowledge related to the network for predicting the label of the unsigned edges</td></tr><tr><td>NPECF, Gupta &amp; Mishra, 2020</td><td>√</td><td>√</td><td>No</td><td>Projects the partially labeled signed network into three projections to predict the label</td><td>Suffers from the information loss as in projections only positive/negative edges would be there</td></tr><tr><td colspan="6">Statistical and random walk-based approaches</td></tr><tr><td>SRWR, Jung et al., 2020</td><td></td><td>√</td><td>No</td><td>Ranking of nodes is performed by signed random walk after removing the unlabeled edges</td><td>Requires the removal of unlabeled edges that causes the information loss</td></tr><tr><td>NbA, Aggarwal et al., 2016</td><td></td><td>√</td><td>No</td><td>Neighborhood-based approach and utilizes the unlabeled as well as labeled edges.</td><td>Performance is affected when the network is sparse and a large number of edges are unlabeled</td></tr><tr><td>LOGIT, Leskovec et al., 2010b</td><td>√</td><td>√</td><td>Yes</td><td>Utilized logistic regression model for predicting the label of an edge selected arbitrarily</td><td>The edge features are based on the triad formation based on theories of balance and status</td></tr><tr><td colspan="6">Propagation and embedding-based approaches</td></tr><tr><td>TRUST, Guha et al., 2004</td><td>√</td><td>√</td><td>No</td><td>Propagates trust/distrust scores between the nodes to determine the trustworthiness</td><td>Specific to the network/circumstances and requires domain information</td></tr><tr><td>ASiNE, Lee et al., 2020</td><td></td><td>√</td><td>Yes</td><td>Adversarial learning-based methodology to generate the embeddings</td><td>Information loss due to breaking the network in positive and negative subgraph</td></tr><tr><td>DDRE, Xu et al., 2022</td><td></td><td>√</td><td>Yes</td><td>Generation of signed network embedding using the dual-branch density ratio estimation</td><td>Positive and negative proximities are computed in isolation that leads to the information loss</td></tr></table>

![](/api/attachments/VJCRW7RC/fulltext/images/233181f19146a5a268f9a9180b45858a24f9532d4de8b41ab5da34ecad82bbfc.jpg)  
Figure 3. Design Science-Based Research Methodology for the Proposed Method

Although the DSR process follows a nominally sequential structure, there is no expectation that researchers would always carry out Stages 1 through 6 in this sequence. Rather, researchers could begin at almost any stage (four possible research entry points, namely problem-centered initiation, objective-centered initiation, design- and development-centered initiation, and client/context-centered initiation) and proceed outward (Peffers et al., 2007). Since, GASP is based on analogical approaches (of graph augmentation, symmetric normalization, and random walk-based graph regularized transductive label propagation), which have not yet been formally thought through as a solution to the problem of sign prediction of ties in a network, the DSR process in this study is a design- and development-centered initiation and thus starts with Stage 3. Finally, in Section 7, we conclude this study and discuss the applicability of the proposed solution to practice and real-world scenarios.

## 4 Artifact Description

## 4.1 Design of GASP

The idea behind GASP is to diffuse the prior label information of the labeled ties smoothly in the network in order to predict the labels of the unsigned ties. Assuming a social network emanating from a social media platform, we performed graph augmentation, affinity matrix computation, symmetric normalization, and label propagation for the sign prediction of network ties (relationships). Figure 4 shows a snippet of the usermovie interaction and the corresponding user-user trust/distrust toy network. Based on Figure 4a, the prior trust/distrust relationships between users are depicted separately in Figure 4b using colored lines. The dashed lines indicate the requirement of predicting the labels between the relationships of those users for better recommendation generation in this scenario.

This and the following subsections discuss the components of the GASP design. Table 2 provides a list of notations used to design GASP.

Signed network (Definition 1): An undirected signed network can be represented using a graph $G ^ { S } =$ $( V , E ^ { + } \cup E ^ { - } )$ with a set of vertices |??| = ?? and set of edges |??| = ??. All the edges in the signed network are labeled either with a positive or negative sign. The values in adjacency matrix of the signed network ??<sup>??</sup> ∈ $\{ - 1 , 0 , 1 \} ^ { n \times n }$ are 1 if there is a positive relationship between the nodes, –1 if the relationship is negative and 0 if there is no relationship. An example of a signed graph and its adjacency matrix is shown in Figure 5.

We obtained the undirected signed network of users from IMDb and predicted signs for the unlabeled edges. In Definition 2 below, we define the problem of sign prediction for unlabeled edges (Aggarwal et al., 2016).

![](/api/attachments/VJCRW7RC/fulltext/images/e65f35baa2cbfd58b2a454f61288a7d9a7299cfc390da5d32da62d68bafd24db.jpg)

![](/api/attachments/VJCRW7RC/fulltext/images/95661468b24c5e9ddb1aef340d192b9b761b9af0c106932d47b4c6517e389c2e.jpg)  
(a) A user-item network with trust/distrust relationships between users  
(b) A trust/distrust relationship network between users  
Note: Trust and distrust relationships are shown using blue and red colors, respectively. The dashed relationships between users show the unknown type of relationships.

Figure 4. A Toy Network Showing the User-Item Interaction and User-User Trust/Distrust Relationships and the Corresponding User-User Network for Trust/Distrust Relationships.

Table 2. List of Frequently Utilized Notations

<table><tr><td>Notation</td><td>Description</td></tr><tr><td> $G^{S} = (V, E^{+} \cup E^{-})$ </td><td>Signed graph with a set of positive edges  $E^{+}$ , negative edges  $E^{-}$  and a set of nodes  $V$ </td></tr><tr><td> $A^{S} \in \{-1,0,1\}^{n \times n}$ </td><td>Adjacency matrix of the signed graph with  $|V| = n$ </td></tr><tr><td> $G^{PS} = (V, E^{L} \cup E^{UL})$ </td><td>Partially labeled signed graph with a set of labeled edges  $E^{L}$  (positive and negative) and unlabeled edges  $E^{UL}$ </td></tr><tr><td> $A^{PS} \in \{-1,0,1, x\}^{n \times n}$ </td><td>Adjacency matrix of a partially labeled signed graph with  $|V| = n$  and the sign is to be predicted for the edges with value  $x$  in the adjacency matrix</td></tr><tr><td> $G^{AG} = (V^{AG}, E^{AG})$ </td><td>Augmented graph for  $G^{PS}$  where  $V^{AG} = V \cup V^{LE}$  and  $E^{AG} \in V^{AG} \times V^{AG}$ . Here  $V^{LE}$  is the set of labeled edge nodes and  $|V^{LE}| = p$ </td></tr><tr><td> $A^{AG} \in \{0,1\}^{(n+p) \times (n+p)}$ </td><td>Adjacency matrix of the augmented graph</td></tr><tr><td> $W, S, P_{0}$ </td><td>Affinity matrix and its symmetric normalization using diagonal weighted degree matrix  $D$ , prior label matrix that contains sign information of the labeled edges</td></tr></table>

![](/api/attachments/VJCRW7RC/fulltext/images/1a4d24fcdfabb60c6bba8c7bfeb82e7e14697e335d299b1d36ec575827cc3982.jpg)

![](/api/attachments/VJCRW7RC/fulltext/images/e22b05221e8195bdcda48f76f62afc26f31f0785f662d70a1ec1b72eb87f4da2.jpg)  
Note: The red edges indicate negative sign (distrust) and the blue edges indicate positive sign (trust). The signed adjacency matrix of this network is also shown, and it is a symmetric matrix.  
Figure 5. A Signed Network with Six Nodes and Eight Edges.

![](/api/attachments/VJCRW7RC/fulltext/images/ab95cec2e5422f671c53f94e668b014447a0920faa2996a58676441debe3636a.jpg)  
Note: The red edges are with a negative sign and the blue edges are with a positive sign. The dashed edges are unlabeled. The adjacency matrix of this network is also shown where ?? indicates the unlabeled edge.

Figure 6. A Partially Labeled Signed Network with Six Nodes and Eight Edges  
![](/api/attachments/VJCRW7RC/fulltext/images/0d0f00320be49f6abd7a08b4b927b45a8f80279d8930430dc4fa6692340e434b.jpg)  
Figure 7. The Augmented Graph of the Partially Labeled Signed Network Shown in Figure 6

Edge sign prediction (Definition 2): For a partially labeled undirected signed graph $G ^ { P S } = ( V , E ^ { L } \dot { \cup } E ^ { U L } )$ where $E ^ { L } = E ^ { + } \cup E ^ { - }$ is the set of labeled edges and $E ^ { U L }$ is the set of unlabeled edges for which the sign is to be predicted.

For the problem being considered here, there would be a partially labeled signed network, and the task would be to predict the label of unsigned edges as explained in Definition 2. An example of a partially labeled signed network and its adjacency matrix is shown in Figure 6.

Augmented graph (Definition 3): An augmented graph of a partially labeled signed network $G ^ { \smile P S } = ( V , \overline { { { E } } } ^ { L }$ ∪ $E ^ { U L } )$ is a graph $G ^ { A G } = \mathsf { \bar { ( } } V ^ { A G } , E ^ { A G } )$ where $V ^ { A G } = V$ ∪ $V ^ { L }$ is the set of object nodes $V = \{ v _ { 1 } , v _ { 2 } , \dots , v _ { n } \}$ and edge nodes $V ^ { L } = \left\{ e _ { 1 } , e _ { 2 } , \ldots , e _ { p } \right\}$ considering labeled edges as nodes and $\bar { E } ^ { A G } \in V ^ { A G } \times V ^ { A G }$

The partially labeled signed network is augmented using the labeled edges as nodes. In this augmented graph, the labeled edges are removed and converted to labeled edge nodes. These labeled edge nodes would be connected to those two object nodes in the augmented graph on which the labeled edges were incident. An example of an augmented graph for the partially labeled signed network shown in Figure 6 is shown below in Figure 7. The labeled edge nodes in the augmented graph are blue (for the positive/trust label) or red (for the negative/distrust label). Once the augmented graph is formed for the given network, we can compute the affinity matrix between the nodes in the augmented graph using the Jaccard similarity measure (Han et al., 2011) as given below.

Affinity matrix (Definition 4): The affinity matrix ?? has pairwise affinity between the nodes in the augmented graph and is computed using the Jaccard similarity measure as follows:

$$
w _ {i j} = \frac {| N _ {i} \cap N _ {j} |}{| N _ {i} \cup N _ {j} |},
$$

where $N _ { i }$ and $N _ { j }$ are the neighborhood sets of nodes $i , j \in V ^ { A G }$

Once graph augmentation is performed, the label information is disseminated through nodes. The scores of the label for nodes in the augmented graph would depend on the number of connections and the affinity strength in the network.

Label score (Definition 5): The label scores for positive and negative classes for a node ?? can be computed considering the neighborhood $N _ { i }$ of the node and the affinity strength as follows

$$
\begin{array}{r} p _ {i} ^ {P O S} = \sum_ {j \in N _ {i}} w _ {i j} p _ {j} ^ {P O S}, \\ p _ {i} ^ {N E G} = \sum_ {j \in N _ {i}} w _ {i j} p _ {j} ^ {N E G}, \end{array}
$$

where $p _ { i } ^ { P O S }$ and $p _ { i } ^ { N E G }$ are the positive and negative label scores respectively for node ?? and $p _ { j } ^ { P O S }$ and $p _ { j } ^ { N E G }$ are the positive and negative label scores, respectively, for node ?? in the augmented graph, and $w _ { i j } = W [ i , j ]$ is the affinity between nodes ?? and $j \in N _ { i }$

This idea is implemented as an iterative procedure to refine the scores of nodes. Since it is an additive procedure, we need to perform the normalization of the scores so that the iterative procedure stabilizes and converges. Inspired by graph regularization (Zhou et al., 2004) for smooth propagation of the label information in the network, edge weights in the augmented graph are symmetrically normalized using Equations (1) and (2):

$$
p _ {i} ^ {P O S} = \sum_ {j \in N _ {i}} \frac {w _ {i j}}{\sqrt {d _ {i}} \sqrt {d _ {j}}} p _ {j} ^ {P O S},\tag{1}
$$

$$
p _ {i} ^ {N E G} = \sum_ {j \in N _ {i}} \frac {w _ {i j}}{\sqrt {d _ {i}} \sqrt {d _ {j}}} p _ {j} ^ {N E G},\tag{2}
$$

where $d _ { i }$ and $d _ { j }$ are the degrees of nodes ?? and $j .$ , respectively. This will positively affect the result of the proposed method for sign prediction using random walkbased diffusion. To account for the prior label information of the edge nodes in the augmented graph, we incorporate the prior label information $p _ { 0 } ^ { i , P \bar { O S } }$ and $p _ { 0 } ^ { i , N E G }$ in the score update through Equations (3) and (4):

$$
p _ {i} ^ {P O S} = \alpha \sum_ {j \in N _ {i}} \frac {w _ {i j}}{\sqrt {d _ {i}} \sqrt {d _ {j}}} p _ {j} ^ {P O S} + (1 - \alpha) p _ {0} ^ {i, P O S},\tag{3}
$$

$$
p _ {i} ^ {N E G} = \alpha \sum_ {j \in N _ {i}} \frac {w _ {i j}}{\sqrt {d _ {i}} \sqrt {d _ {j}}} p _ {j} ^ {N E G} + (1 - \alpha) p _ {0} ^ {i, N E G},\tag{4}
$$

where ?? is the hyper-parameter to control for the effect of information diffusion in the network and the prior label information during the iterative process. For the object nodes in the augmented graph, the prior label information would be zero. In the matrix form, we can write equations as follows:

$$
P = \alpha (S P) + (1 - \alpha) P _ {0},\tag{5}
$$

where $S = D ^ { - 1 / 2 } W D ^ { - 1 / 2 }$ , the symmetric normalization of the affinity matrix ?? and ?? is the diagonal degree matrix of the augmented graph, $P$ and $P _ { 0 }$ are the label score matrix and prior label information matrix respectively with two columns corresponding to positive and negative label scores for all the nodes in the augmented graph. So, $P [ i , P O S ] = p _ { i } ^ { P O S }$ and $P [ i , N E G ] = p _ { i } ^ { N E G }$

As shown in Figure 8, GASP basically works in two broad steps i.e., first, it performs the graph augmentation of the given partially signed network; then, using that it performs the graph regularized label propagation on the augmented graph to predict the label of the unsigned edges in the network. In the first step, the partially signed network is augmented using labeled edges by converting them to labeled edge nodes. The augmented graph has two types of nodes—i.e., object nodes, which are the nodes in the partially labeled signed network, and labeled edge nodes, which are the labeled edges in the partially labeled signed network. We created the prior label matrix, which contained the information of the label of the edges in the network. Those edges that are not labeled and whose labels are to be predicted would not be in the prior label matrix. In the second stage of GASP, the pairwise affinity between nodes of the augmented graph is computed using the Jaccard measure (Han et al., 2011). This gives the scores for relatedness between nodes in the augmented graph. Using the degree diagonal matrix of the augmented graph, the affinity matrix is symmetrically normalized. Using this symmetrically normalized affinity matrix, the graph regularized label propagation is performed for the prior label information using the prior label matrix. After convergence, the label for the unsigned edges in the network can be predicted by comparing the scores for the positive label and negative label for the object nodes connecting the unlabeled edges, as summarized in Algorithm 1:

## Algorithm 1. Prediction of labels for edges

Input: Adjacency matrix $A ^ { A G }$ of augmented graph $G ^ { A G } = ( V ^ { A G } , E ^ { A G } )$ , prior label matrix $P _ { 0 }$ parameter $\alpha ,$ and error tolerance ??

Output: Predicted labels for unlabeled edges $\forall e \in$ $\mathsf { \bar { E } } ^ { U L } \mathrm { i n } G ^ { P S } = ( V , E ^ { L } \cup E ^ { U L } )$

Begin

1. Compute affinity matrix ?? for adjacency matrix $A ^ { A G }$ of augmented graph. For $w _ { i j } \in W , \forall i , j ,$

$$
w _ {i j} = \frac {| N _ {i} \cap N _ {j} |}{| N _ {i} \cup N _ {j} |},
$$

where $N _ { i }$ and $N _ { j }$ are the neighborhood sets of nodes $\forall i , j \in V ^ { A G }$

2. Compute diagonal weighted degree matrix $D _ { \iota }$ where

$$
(D) _ {i i} = \sum_ {j = 1} ^ {| V ^ {A G} |} w _ {i j}.
$$

3. Compute symmetric normalized affinity matrix $S = \dot { D } ^ { - 1 / 2 } \dot { W } D ^ { - 1 / 2 }$

4. Randomly initialize ??.

5. While ?????????? $\geq \varepsilon$

$$
P \leftarrow \alpha S P + (1 - \alpha) P _ {0}.
$$

6. Predict the label for unlabeled edges $\forall e \in E ^ { U L }$ incident on object nodes ?? and ??.

$$
\begin{array}{c} \text {label} (e) \leftarrow + \quad \text {if} \quad (P [ i, P O S ] + P [ j, P O S ]) > \\ (P [ i, N E G ] + P [ j, N E G ]). \end{array}
$$

Otherwise

$$
l a b e l (e) \leftarrow -
$$

End

![](/api/attachments/VJCRW7RC/fulltext/images/02bd2e5c74cbc529dcae06bb8acf62b630b6668da9f932dbb553ceee240acc5e.jpg)  
Figure 8. Flow Diagram of GASP

The space complexity of the proposed model is mainly attributed to the memory requirement for augmented graph $G ^ { A G } = ( V ^ { A G } , E ^ { A G } )$ . In the augmented graph, the number of edges would be $E ^ { A G } = 2 | E ^ { L } | + | E ^ { \dot { U } L } |$ and the number of nodes $V ^ { A G } = \vert V \vert + \vert E ^ { L } \vert$ This augmented graph would be highly sparse, as $( 2 | E ^ { L } | +$ $| E ^ { \bigcup _ { L } } | ) \ll ( \breve { ( | V | } + | E ^ { L } | ) ^ { 2 } )$ , so most of the entries in the adjacency matrix for the augmented graph would be zero if stored in a naive manner. Thus, by using the appropriate data structure, the space requirement for the augmented graph would be $O ( 2 \bar { | } E ^ { L } | + | { \cal E } ^ { U L } | )$ Regarding computational complexity, mainly the computation of matrices ?? and ?? in Steps 3 and ${ 5 , }$ respectively, in Algorithm 1 would contribute. In Step 3, the matrix ?? would require $O ( ( | V | + | E | ) ^ { 2 } )$ , as the matrix ?? is diagonal; since the matrix ?? has only two columns, the computation of ?? would require $O ( k ( | V | + | E | ) ^ { 2 } )$ , where ?? is the number of iterations taken for convergence. So, the primary computational complexity of the proposed model would be $O ( k ( | V | +$ |??|)<sup>2</sup>) . Thus, the important factor for the time requirement of the proposed model is the number of iterations taken for convergence. As shown empirically in the experiment section, the proposed method does not take a large number of iterations so can be applied on real-world networks. Other competing methods like NPECF (Gupta & Mishra, 2020) and SRWR (Jung et al., 2020) are also scalable. NPECF has quadratic complexity in terms of network size; however, the performance of NPECF falls short due to its limitation from information loss, where projections only involve positive/negative edges (Gupta & Mishra, 2020). For SRWR, the time complexity depends on the number of iterations taken for convergence and network size, considering the nodes and edges in the network (Jung et al., 2020). Therefore, SRWR would be scalable, but its performance would be impacted by the requirement of the removal of unlabeled edges in the network, which causes information loss.

Table 3. Descriptive Statistics

<table><tr><td></td><td>Count</td><td>Average</td><td>Median</td><td>Min</td><td>Max</td><td>SD</td></tr><tr><td>Reviews</td><td>14136</td><td>35.6*</td><td>10</td><td>1</td><td>906</td><td>85.4</td></tr><tr><td>Reviewers</td><td>10861</td><td>1.30**</td><td>1</td><td>1</td><td>38</td><td>1.45</td></tr><tr><td>Individual ratings</td><td>14136</td><td>7.45</td><td>9</td><td>1</td><td>10</td><td>3.22</td></tr><tr><td>Movie-wise ratings</td><td>397</td><td>6.84</td><td>7.33</td><td>1</td><td>10</td><td>2.19</td></tr><tr><td>User-wise ratings</td><td>10861</td><td>7.63</td><td>9</td><td>1</td><td>10</td><td>3.16</td></tr></table>

Note: \*indicates average number of times a movie is reviewed. \*\*indicates average number of times a reviewer reviews different movies

## 4.2 Demonstration

Given the scarcity of data on signed networks, prior research has recommended evaluating proposed artifacts in the signed network setting on a variety of datasets comprising of domains where tie signs are overtly denoted (through actions such as positive or negative voting on Wikipedia), as well as domains where signs can be inferred through the activities and attitudes of users (through ratings or reviews on products) (Kirkley et al., 2019; Leskovec et al., 2010a). Moreover, prior studies suggest that sign prediction methods, which are generally benchmarked over a few publicly available signed network datasets (as shown in Section 5.1), should be generalizable across online social media platforms (Leskovec et al., 2010b). Even though links in networks emanating from social media platforms can have different semantic interpretations, they are still guided by general principles for sign inference in networks (Tang et al., 2016). Therefore, we created a new signed network dataset (originating from IMDb platform) to demonstrate the applicability and utility of the GASP. For the prediction of trust/distrust in this network, we considered different percentages (60, 65, 70, 75, 80) of ties to be labeled and the remaining ties to be unlabeled.

## 4.2.1 Signed Network Creation from IMDb

We collected a dataset of movies and corresponding user ratings from IMDb to derive the positive (trust) and negative (distrust) relationships between IMDb users. IMDb is the world’s most popular platform for information related to content (movies, TV shows, celebrity, etc.), covering more than 17 million titles with over 8 million user-written reviews.<sup>2</sup> Additionally, users are asked to score movies and TV shows on a scale of 1 to 10, and the results are used to create a weighted mean rating (Gupta et al., 2016; Schoenmueller et al., 2020) that is shown for each movie, TV show, etc. The addition of the rating is accompanied by a mandatory review headline and a mandatory review text. We scraped the data of user-movie ratings during a 5-year period (2017-2021) for a regional cluster of the Indian film industry known as Tollywood. This dataset contained 14,136 ratings given by 10,861 users to 397 movies on a scale of 1 to 10.

First, we curated the list of all movies released during 2017-2021, comprising 566 movies in total. However, out of these 566 movies, 169 movies had no ratings/reviews, thus leaving us with 397 rated movies. Table 3 provides a summary of the dataset scraped from IMDb. We transformed the user-movie interaction bipartite network to a user-user unipartite network (Gupta & Kumar, 2021), wherein each user had a movie rating vector associated with them. In these movie rating vectors, if a movie was not rated by a user, the corresponding value was indicated as not applicable. To determine signs of relationships between users, we considered the Pearson correlation between the movie rating vectors of users and assigned a positive sign (trust) to the relationship between users if the correlation was positive, and a negative sign (distrust) otherwise. Then, we found the largest balanced as well as imbalanced connected component of the signed network of 10,861 users, as shown in Figure 9.

The imbalanced signed network contained 766 users and 4,845 trust and distrust relationships represented as positive and negative ties, respectively. In this network, 3,104 relationships were defined as trust relationships (positive), 1,741 relationships were defined as distrust (negative), and 99.17% was the sparsity of the network. We also extracted the balanced subnetwork from the imbalanced connected component of the signed network. The balanced signed network contained 708 users and 3199 relationships, with 1599 trust relationships (positive) and 1600 distrust relationships (negative). The visualization of imbalanced and balanced signed subnetworks is shown in Figure 8. The structural information of these two networks is given in Table 4. It is important to note that in both the balanced and imbalanced subnetworks, the average clustering coefficient was found to be much higher than the equivalent random network (0.478 vs. 0.012 and 0.735 vs. 0.016) Also, the average path length for both balanced and imbalanced networks was found to be numerically close to that of the equivalent random network (3.034 is close to 2.99 and 2.77 is close to 2.61). The log-log degree distributions of balanced and imbalanced datasets are shown in Figure 10, which shows that both balanced and imbalanced datasets follow the power-law degree distribution. Thus, the IMDb user-user network meets the mathematical properties needed to be considered a real empirical network (Kumar et al., 2017; Gupta & Kumar, 2020).

(b) Balanced network  
![](/api/attachments/VJCRW7RC/fulltext/images/50464724f8252a2a0ba28ca6d3fc9c07f258141fe6ef95d910f8137318246ccf.jpg)  
(a) Imbalanced network

![](/api/attachments/VJCRW7RC/fulltext/images/955990cfb41a72d99976fffacfc92020bbc1630c7ef2ba9fc7e669d6b4f2dd0c.jpg)  
Note: The blue and red relationships correspond to similar (trust) and dissimilar (distrust) users in the network.  
Figure 9. Balanced and Imbalanced Signed Network of Users Formed from the IMDB User-Movie Interactions

Table 4. Structural Information of the Balanced and Imbalanced IMDb Networks

<table><tr><td></td><td>Balanced network</td><td>Imbalanced network</td></tr><tr><td>Number of nodes (|V|)</td><td>708</td><td>766</td></tr><tr><td>Number of edges (|E|)</td><td>3,199</td><td>4,845</td></tr><tr><td>Sparsity</td><td>99.36%</td><td>99.17%</td></tr><tr><td>Number of positive edges (|E+|)</td><td>1,599 (49.98%)</td><td>3,104 (64.07%)</td></tr><tr><td>Number of negative edges (|E-|)</td><td>1,600 (50.02%)</td><td>1,741 (35.93%)</td></tr><tr><td>Average degree (ignoring the sign of edges)</td><td>8.99</td><td>12.65</td></tr><tr><td>Local average clustering coefficient (ignoring the sign of the links)</td><td>0.478*</td><td>0.735*</td></tr><tr><td>Average path length (ignoring the sign of the links)</td><td>3.034**</td><td>2.771**</td></tr><tr><td>Balance score (frustration method) (Aref &amp; Wilson, 2018)</td><td>0.571</td><td>0.587</td></tr></table>

Note: \*The values of the average clustering coefficient for the equivalent random network are 0.012 and 0.016, respectively. \*\*The values of average path length for the equivalent random network are 2.99 and 2.61, respectively.

Degree Distribution  
![](/api/attachments/VJCRW7RC/fulltext/images/9856a51fe68b1fe769c6f9d83fce1b19992f5cdb9a7870a5517430de03af51ed.jpg)  
(a) IMDB balanced signed network

Degree Distribution  
![](/api/attachments/VJCRW7RC/fulltext/images/5fd3128cac4c9c36bfa327448e12ab00209fb718f3ce89f547ff22a66cd28d90.jpg)  
(b) IMDB imbalanced signed network  
Figure 10. Log-Log Degree Distribution Plots of Balanced and Imbalanced IMDB Signed Networks

Table 5. Performance Comparison of the Methods for Balanced IMDb Dataset

<table><tr><td rowspan="3">Labeled edges (%)</td><td colspan="10">Method</td></tr><tr><td colspan="2">ASiNE</td><td colspan="2">DDRE</td><td colspan="2">NPECF</td><td colspan="2">SRWR</td><td colspan="2">GASP</td></tr><tr><td>ACC</td><td>OP</td><td>ACC</td><td>OP</td><td>ACC</td><td>OP</td><td>ACC</td><td>OP</td><td>ACC</td><td>OP</td></tr><tr><td>60%</td><td>62.31%</td><td>54.91%</td><td>61.82%</td><td>56.75%</td><td>52.66%</td><td>41.03%</td><td>60.59%</td><td>37.93%</td><td>63.66%</td><td>52.95%</td></tr><tr><td>65%</td><td>62.34%</td><td>60.49%</td><td>63.69%</td><td>58.35%</td><td>52.11%</td><td>39.11%</td><td>61.63%</td><td>39.4%</td><td>64.45%</td><td>53.45%</td></tr><tr><td>70%</td><td>63.12%</td><td>62.35%</td><td>65.87%</td><td>63.81%</td><td>52.53%</td><td>38.35%</td><td>62.73%</td><td>41.2%</td><td>64.82%</td><td>54.46%</td></tr><tr><td>75%</td><td>63.87%</td><td>59.22%</td><td>64.66%</td><td>61.95%</td><td>52.76%</td><td>38.66%</td><td>62.82%</td><td>40.84%</td><td>65.39%</td><td>55.21%</td></tr><tr><td>80%</td><td>64.58%</td><td>59.97%</td><td>65.2%</td><td>64.24%</td><td>53.28%</td><td>40.78%</td><td>63.39%</td><td>41.61%</td><td>65.96%</td><td>54.01%</td></tr></table>

Note: AsiNE = adversarial signed network embedding, DDRE = dual-branch density ratio estimation, NPECF = network projection-based edge classification framework, SRWR = signed random walk with restart, ACC = accuracy, OP = optimized precision

Table 6. Performance Comparison of the Methods for Imbalanced IMDb Dataset

<table><tr><td rowspan="3">Labeled edges (%)</td><td colspan="10">Method</td></tr><tr><td colspan="2">ASiNE</td><td colspan="2">DDRE</td><td colspan="2">NPECF</td><td colspan="2">SRWR</td><td colspan="2">GASP</td></tr><tr><td>macro F1</td><td>GM (S,N)</td><td>macro F1</td><td>GM (S,N)</td><td>macro F1</td><td>GM (S,N)</td><td>macro F1</td><td>GM (S,N)</td><td>macro F1</td><td>GM (S,N)</td></tr><tr><td>60%</td><td>47.29%</td><td>34.3%</td><td>52.25%</td><td>42.01%</td><td>44.87%</td><td>30.73%</td><td>53.75%</td><td>45.03%</td><td>65.04%</td><td>65.96%</td></tr><tr><td>65%</td><td>47.98%</td><td>35.35%</td><td>55.38%</td><td>46.65%</td><td>44.1%</td><td>29.42%</td><td>55.57%</td><td>47.46%</td><td>65.95%</td><td>67.34%</td></tr><tr><td>70%</td><td>50.67%</td><td>39.57%</td><td>57.04%</td><td>49.14%</td><td>43.1%</td><td>27.64%</td><td>56.94%</td><td>49.29%</td><td>65.85%</td><td>67.44%</td></tr><tr><td>75%</td><td>49.99%</td><td>38.5%</td><td>58.74%</td><td>51.57%</td><td>42.98%</td><td>27.39%</td><td>58.03%</td><td>50.73%</td><td>67.33%</td><td>69.08%</td></tr><tr><td>80%</td><td>53.57%</td><td>43.92%</td><td>59.84%</td><td>53.22%</td><td>41.96%</td><td>25.72%</td><td>58.69%</td><td>51.68%</td><td>67.14%</td><td>69.04%</td></tr></table>

Note: AsiNE = adversarial signed network embedding, DDRE = dual-branch density ratio estimation, NPECF = network projection-based edge classification framework, SRWR = signed random walk with restart, GM(S,N) = geometric mean of specificity and negative predicted values

## 4.2.2 Sign Prediction Using GASP on the Network of Users Originating from IMDb

For the sign prediction of ties in the network of reviewers on IMDb, we used NPECF, SRWR, ASiNE, and DDRE to compare the performance of GASP. In addition, we evaluated how well the proposed method performed on balanced and imbalanced components of the IMDb reviewers’ network. Finally, we also evaluated the sign prediction performance at different percentages of labeled ties. Tables 5 and 6 show the results for sign prediction in the balanced and imbalanced IMDb network datasets. These results used different evaluation metrics for the balanced network (accuracy and optimized precision) and the imbalanced network (macro F1 and GM of specificity and negative predictive values) for comparison. We present the evaluation metrics for 60, 65, 70, 75, and 80 percent of labeled edges. Table 5 shows that GASP outperformed NPECF and SRWR in terms of accuracy and optimized precision and ASiNE, and DDRE in terms of accuracy. In addition, Table 6 shows that the proposed method obtained higher values of macro F1 and geometric mean of specificity and negative predictive values (GM(S,N)), as the negative sign is the minority class for this dataset and the prediction of the minority class sign is more significant (Branco et al., 2016) for sign prediction on the imbalanced network across different percentages of labeled edges. We discuss the aforementioned evaluation metrics and state-of-the-art methods used for comparison in Sections 5.2 and 5.3, respectively. We used a system with R version 4.1.0 to perform all demonstrations and experiments. Overall, the demonstration of these results on the network of reviewers originating from IMDb suggests that the graph augmentation and graph regularized information diffusion approach synergistically produces high-quality outcomes.

In this way, GASP can be applied to a signed network emanating from any domain or online platform (such as Amazon, Tripadvisor, etc.) to predict the signs of relationships of new users with existing users.

## 5 Evaluation

## 5.1 Benchmark Datasets Used for Comparison

To perform benchmarking experiments, we utilized four different datasets—namely Epinions, <sup>3</sup> Wikipedia Requests for Adminship<sup>4</sup> (RfA), Slashdot Zoo,<sup>5</sup> and the

Yeast Genetic Interaction Network<sup>6</sup> (GIN). It is also important to note that there is a scarcity of publicly available signed network datasets; therefore, these datasets are considered standard datasets for benchmarking analytical algorithms in signed network settings (Leskovec et al., 2010b; Tang et al., 2016). As discussed in Section 1, these networks are partially signed networks originating from different phenomena in real-world situations. Table 7 provides the details of these four datasets.

The Epinions network dataset has several online consumers who post reviews on the website Epinions.com (now Shopping.com<sup>7</sup>), and they exhibit a who-trusts-whom relationship. This dataset is useful from the point of view of recommendation generation, and trust and distrust relationships can help improve recommendation performance. The Wikipedia RfA dataset is related to Wikipedia editors voting to allow others/themselves to become administrators (Leskovec et al., 2010a). The datasets reflect the competition and collaboration between individuals in a social network and represent the dynamics of human relationships.

The social network of the Slashdot Zoo dataset comprises users of the technology-related news website Slashdot.org. These users were able to tag other users as friends or foes after the Slashdot Zoo feature was introduced by Slashsdot.org<sup>8</sup>(Leskovec et al., 2010a). These friend or foe relationships represent how people perceive each other in communities and show how relationships can have positive or negative polarity depending on people’s viewpoints. Another dataset utilized for experiments is drawn from the biology domain. The Yeast Genetic Interaction Network (GIN) forms positive and negative relationships between yeast genes and thus yields a signed network (Gupta & Mishra, 2020; Stark et al., 2006). This dataset represents how living molecular entities compete or support each other in the real world.

Thus, the selection of these datasets covers different phenomena in real-world situations and also signifies the importance of the sign prediction task in real-world scenarios. In raw form, these networks are highly imbalanced in terms of the ratio of positive ties to negative ties and contain self-loops or multiple ties. Also, the Epinions, Wikipedia RfA, and Slashdot Zoo datasets are directed while the Yeast GIN network is undirected. To make these networks suitable for experiments, we first transformed these directed networks into undirected networks and then removed the self-loops and multiple ties between the nodes, if any (Girdhar & Bharadwaj, 2019; Gupta & Mishra, 2020). We also discarded the ties corresponding to neutral polarity. To make the directed networks undirected, we considered only those pairs of nodes that had pairs of ties in opposite directions with the same sign that was either positive or negative (Girdhar & Bharadwaj, 2019; Gupta & Mishra, 2020; Tremblay & Cheston, 2003).

Table 7. Overview of Datasets Used in Experiments

<table><tr><td></td><td>Epinions</td><td>Wikipedia RfA</td><td>Slashdot Zoo</td><td>Yeast GIN</td></tr><tr><td>Domain</td><td>Network of online consumers</td><td>Wikipedia adminship election network</td><td>User community of technology-related news website network</td><td>Genetic interaction network</td></tr><tr><td>Directed network</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td></tr><tr><td>Number of nodes (|V|)</td><td>1,31,828</td><td>11,279 (without neutral votes)</td><td>77,350</td><td>5,361</td></tr><tr><td>Number of edges (|E|)</td><td>8,41,372</td><td>1,85,627 (without neutral votes)</td><td>5,16,575</td><td>1,05,812</td></tr><tr><td>Number of positive edges (|E+|)</td><td>7,17,667 (85.297%)</td><td>1,44,451 (77.818%)</td><td>3,96,378 (76.732%)</td><td>16,943 (16.012%)</td></tr><tr><td>Number of negative edges (|E-|)</td><td>1,23,705 (14.703%)</td><td>41,176 (22.182%)</td><td>1,20,197 (23.268%)</td><td>88,869 (83.988%)</td></tr><tr><td>Number of bidirectional edges with same sign (without self-loops and multiple edges)</td><td>1,26,886</td><td>5,606</td><td>46,133</td><td>1,05,812</td></tr><tr><td>Number of bidirectional positive edges (without self-loops and multiple edges)</td><td>1,24,538 (98.15%)</td><td>5,429 (96.843%)</td><td>41,600 (90.174%)</td><td>16,943 (16.012%)</td></tr><tr><td>Number of bidirectional negative edges (without self-loops and multiple edges)</td><td>2,348 (1.85%)</td><td>177 (3.157%)</td><td>4,533 (9.826%)</td><td>88,869 (83.988%)</td></tr></table>

However, since conversion to undirected networks may create disconnected components in these networks and for experiments, we created a balanced connected component where each node was connected to at least one node in the component. Also, in a balanced connected component, the ratio of negative ties to positive ties is approximately 1. The networks after preprocessing are shown in Figure 11. To visualize these networks, we utilized the Gephi software (Bastian et al., 2009). The details of these datasets are given in Table 8, which shows that the proportion of positive and negative edges is almost the same and that these networks are balanced, undirected, and connected, thus making them suitable for our experiments (Gupta & Mishra, 2020). The normalized frustration index values of these networks are also listed in the table to illustrate how noisy these networks are from the point of view of unbalanced triads in the network (Aref & Wilson, 2018).

To evaluate the effectiveness of the proposed method on the imbalanced datasets, we also created connected components of these networks in which the ratio of positive to negative edges was almost the same as the original network. These networks are visualized in Figure 12.

As shown in Figure 12, in the Epinions, Wikipedia RfA, and Slashdot Zoo networks, there are more positive edges than negative edges. However, in the Yeast GIN network, there are more negative edges than positive edges. The details of these imbalanced datasets with normalized frustration index values are provided in Table 9, which shows that in these imbalanced datasets, the ratio of positive and negative labeled edges is skewed either towards the positive sign (in Epinions, Wikipedia RfA, and Slashdot Zoo datasets) or the negative sign (in the Yeast GIN dataset). The ratio of positive edges to negative edges is close to that of the original datasets. Using these imbalanced datasets, we also compared the performance of the proposed method with other methods.

![](/api/attachments/VJCRW7RC/fulltext/images/e572edd143d92b4c82d3ee72dd4d5f2cb0d864d7c6d555b548a133b01def2cc4.jpg)

![](/api/attachments/VJCRW7RC/fulltext/images/7d14e86a4623432701113362239f361e07876de2a849f6882f3ad3161e8984a2.jpg)

![](/api/attachments/VJCRW7RC/fulltext/images/9bec19cc9e487c4188ce3696e14524deabeddba61345f11edcc605bea45393c9.jpg)

![](/api/attachments/VJCRW7RC/fulltext/images/b9608dea1f65529e8154568204bf3a537aa136cd141723bc3bbf47a730a1d4d6.jpg)  
Note: The blue edges represent the positive relationships, and the red edges represent the negative relationships in these networks. Figure 11. Different Balanced Signed Networks Used for Experiments

Table 8. Overview of Balanced Connected Component of the Datasets Obtained After Pre-Processing

<table><tr><td></td><td>Epinions</td><td>Wikipedia RfA</td><td>Slashdot Zoo</td><td>Yeast GIN</td></tr><tr><td>Number of nodes (|V|)</td><td>2,952</td><td>1,738</td><td>3,772</td><td>3,451</td></tr><tr><td>Number of edges (|E|)</td><td>5,923</td><td>2,968</td><td>6,299</td><td>8,982</td></tr><tr><td>Number of positive edges (|E+|)</td><td>2,960 (49.97%)</td><td>1,482 (49.93%)</td><td>3,150 (50.01%)</td><td>4,493 (50.02%)</td></tr><tr><td>Number of negative edges (|E-|)</td><td>2,963 (50.03%)</td><td>1,486 (50.07%)</td><td>3,149 (49.99%)</td><td>4,489 (49.98%)</td></tr><tr><td>Normalized Frustration Index</td><td>0.4867</td><td>0.4697</td><td>0.3596</td><td>0.3986</td></tr></table>

![](/api/attachments/VJCRW7RC/fulltext/images/9f188f586c81cb1984773cfaf14a709976435c0a9f31648722d5d3644f86d453.jpg)  
(a) Epinions network

![](/api/attachments/VJCRW7RC/fulltext/images/d1a2ef10a6c90417aa16db961f3d083b7b5afe56117dd963c659d480f93f5d3a.jpg)  
(b) Wikipedia RfA network

![](/api/attachments/VJCRW7RC/fulltext/images/85c7e13c54612e78bbb0f78e0c8d97336add5cfd028e9cbfb772eef25881f986.jpg)  
(c) Slashdot Zoo network

![](/api/attachments/VJCRW7RC/fulltext/images/88fe331c959351be93144912dd7fd78f03b3811fd8551022e887e5d8440e50e5.jpg)  
(d) Yeast GIN network  
Note: The blue edges represent the positive relationships, and the red edges represent the negative relationships in these networks. Figure 12. Different Imbalanced Signed Networks Used for Experiments.

Table 9. Overview of Imbalanced Connected Component of the Datasets Obtained After Pre-Processing

<table><tr><td></td><td>Epinions</td><td>Wikipedia RfA</td><td>Slashdot Zoo</td><td>Yeast GIN</td></tr><tr><td>Number of nodes (|V|)</td><td>3,490</td><td>1,708</td><td>3,240</td><td>3,453</td></tr><tr><td>Number of edges (|E|)</td><td>9,958</td><td>2,973</td><td>6,012</td><td>8,976</td></tr><tr><td>Number of positive edges (|E+|)</td><td>8,468 (85.34%)</td><td>2,356 (79.25%)</td><td>4,810 (80.01%)</td><td>1,546 (17.22%)</td></tr><tr><td>Number of negative edges (|E-|)</td><td>1,490 (14.96)</td><td>617 (20.75%)</td><td>1,202 (19.99%)</td><td>7,430 (82.78%)</td></tr><tr><td>Normalized frustration index</td><td>0.6047</td><td>0.6179</td><td>0.6038</td><td>0.2999</td></tr></table>

## 5.2 Evaluation Metrics

To measure the performance of the different methods, we used a number of classification performance measures. In this work, the objective is to predict the positive or negative label of the unsigned ties in the network, which can be deemed a binary classification problem. Thus, we utilized the following performance evaluation measures. For balanced datasets, we utilized accuracy (Han et al., 2011) and optimized precision (Ranawana & Palade, 2006) to evaluate the performance of different methods. Since for balanced datasets, both classes are almost equal in proportion, the accuracy of the method reflects how well it can correctly predict the instances of both classes. We also utilized optimized precision for performance evaluation in the case of balanced datasets. We were interested not only in both positive and negative classes but also in how well both classes were correctly classified. As the accuracy value of a method could be high even for a particular class (positive or negative), the accuracy may be low, as this measure considers the global accuracy and may hence not give a clear idea of the performance of a method. Therefore, we utilized optimized precision (Ranawana & Palade, 2006).

For imbalanced datasets, where the instances of negative and positive classes are not similarly proportioned, we could not use accuracy or optimized precision, as these are suitable only for balanced datasets (Boughorbel et al., 2017). In this work, since we are interested in both the classes, i.e., positive or negative, a measure that is suitable for evaluating performance by considering only the positive class (or negative class) would be inadequate for an imbalanced dataset.

Even in the case of imbalanced datasets, both classes are equally important to us, and method performance should be evaluated based on that fact. Therefore, we utilized the macro F1 measure, which considers both classes to be equally important (Xu et al., 2022). The Macro F1 measure is computed by taking the mean of the F1 scores for each class. This evaluation measure is suitable for measuring the performance of methods for imbalanced datasets when all classes are important (Xu et al., 2022). To measure the class-specific performance, we also considered the geometric mean of specificity and negative predictive values (NPV) for the negative (rare) class. It has been observed that in classimbalanced situations, it is the minority/rare class that is considered interesting and important. Thus, this class must be predicted as correctly as possible, as it is highly relevant for end users (e.g., in the detection of fraudulent transactions, see Branco et al., 2016).

## 5.3 Algorithms Used for Comparison

In this work, we consider the problem of sign prediction for unlabeled ties in the undirected and unweighted signed social networks. We propose a method that is domain independent and can perform prediction based only on the network structure; hence, it does not utilize structural balance theory, which may not necessarily be followed by all real-world signed networks (Aref & Wilson, 2018). The proposed GASP method is also domain independent and does not utilize structural balance theory. Recently, methods like NPECF, SRWR, and NbA have been proposed. It has already been shown that NbA may not be able to label all unsigned ties, depending on how many ties incident on a node have label information (Gupta & Mishra, 2020). Therefore, in this work, we compare the performance of GASP with NPECF and SRWR. Tto show the efficacy of GASP, we also compare its performance with the deep learningbased methods ASiNE and DDRE, which utilize the structural balance theory for sign prediction tasks.

NPECF (network projection-based edge classification framework): This method performs the projection of the original network in three parts, namely, positive signed edges with unlabeled edges, negative signed edges with unlabeled edges, and the whole network without considering the sign of edges. Then using the three projections, it performs the prediction of the unlabeled edges (Gupta & Mishra, 2020).

SRWR (signed random walk with restart): This method performs the ranking of the nodes in the signed network using signed random walk with restart. Using the ranking of the nodes, it can predict the label of the unsigned edges by first removing all the unlabeled edges and then performing signed random walks (Jung et al., 2020).

AsiNE (adversarial signed network embedding): This method learns the low-dimensional representation of nodes in the network by performing adversarial learning. Using the lowdimensional representation, sign prediction can be performed for the unsigned edges in the network (Lee et al., 2020).

DDRE (dual-branch density ratio estimation): This method utilizes the dual-branch density ratio estimation architecture to learn the signed network embedding. It consists of a dual-branch network to deal with the confusing examples and expected matrix factorization without sampling (Xu et al., 2022).

For comparison of these methods, following random subsampling for positive and negative classes, we randomly used ??% ( ?? = 60, 65, 70, 75, 80 ) of the edges as prior labeled edges in the network and used these labeled edges to predict the labels of the remaining edges in the network. We performed this experiment 10 times for each value of ??; we report average values of the results of different evaluation measures for all unlabeled edges. For the SRWR algorithm, we used the values of parameters ?? and ?? as 0.5 and 0.9 for the Epinions and Yeast GIN networks (Jung et al., 2020). For the Slashdot Zoo dataset, we used ?? and ?? as 0.6 and 0.9, and for the Wikipedia RfA dataset we used ?? and ?? as 0.1 and 0.6 (Jung et al., 2020). For all datasets, we took the value of 0.15 of parameter ?? for SRWR (Jung et al., 2020). For NPECF, we took the the decay factor of 0.6, and for all datasets, the number of iterations was 5 (Gupta & Mishra, 2020). For ASiNE and DDRE methods, we used the proposed settings for experiments, as mentioned in the respective studies (Lee et al., 2020; Xu et al., 2022). For GASP, we used the value of 0.7 for ?? for all the datasets used in the experiments. The datasets and the implementation of the proposed GASP method in R are available on GitHub.<sup>9</sup>

![](/api/attachments/VJCRW7RC/fulltext/images/d8a270bc5746e34e8a36ae61c566af6c975ee2a1415c2b018e465c72ff4897e8.jpg)  
(a) Accuracy results for Epinions

![](/api/attachments/VJCRW7RC/fulltext/images/40784d45276b9a268ac62ba3db6095e33e2a807fec77c72530e7e7cab064c6d7.jpg)  
(b) Optimized Precision for Epinions

![](/api/attachments/VJCRW7RC/fulltext/images/de1ead8c1b62b6d502238e2335370f9a40e19e0c5cddef22172972321ad60214.jpg)  
(c) Accuracy results for Wikipedia RfA

![](/api/attachments/VJCRW7RC/fulltext/images/b003fa2db7d427d952fbc45201cda104ac9478f8613d0878d97427f4df886deb.jpg)  
(d) Optimized Precision for Wikipedia RfA

![](/api/attachments/VJCRW7RC/fulltext/images/cc15563a3c2d039ac931e724e1c0e750da7baba3bcd4d143ef66aa04b98ada6f.jpg)  
(e) Accuracy results for Slashdot Zoo

![](/api/attachments/VJCRW7RC/fulltext/images/6ce081008abffd0fb88e9c1cdc5f760ec940ecddc17831e4f8773c46abaf57b5.jpg)  
(f) Optimized Precision for Slashdot Zoo

![](/api/attachments/VJCRW7RC/fulltext/images/43cc5247499b859182fae2939dbd3adaf567d2abc6c0ad83ee5e29ab225a19cb.jpg)  
(g) Accuracy results for Yeast GIN

![](/api/attachments/VJCRW7RC/fulltext/images/21fe0c890c1f7bb9b79f7b6d41fc9be4a539cec3c79ef5c7c18321a59fd67bea.jpg)  
(h) Optimized Precision for Yeast GIN  
Figure 13. Accuracy and Optimization Precision values for GASP, NPECF, SRWR, ASiNE, and DDRE Algorithms Used for Comparison on Different Balanced Datasets Used for Experiments.

## 5.4 Evaluation in Balanced Benchmark Datasets

In Figure 13, the average values of accuracy and optimized precision of different algorithms are plotted for different percentages of labeled edges in the networks. The figure shows that the accuracy of GASP was significantly better than that of other methods used for comparison. The results show that the accuracy of GASP was stable even when the labeled percentage of edges in the networks was low. The optimized precision values of GASP for different datasets were also significantly better than those of the other methods used for comparison. For 80% of edges defined as labeled and those remaining unlabeled in the Epinions dataset, GASP achieved a prediction accuracy and optimized precision of 0.8847 and 0.8747, respectively. Similarly, in the Wikipedia RfA, Slashdot Zoo, and Yeast GIN datasets, the performance of GASP was better than NPECF, SRWR, ASiNE, and DDRE in terms of accuracy and optimized precision values for all percentage values of labeled edges. NPECF performed better than SRWR in most of the datasets across different percentages of labeled edges. However, in the case of the Yeast GIN dataset, the performance of SRWR was better than that of NPECF. ASiNE performed better than DDRE in terms of both the metrics in the Wikipedia RfA and the Slashdot Zoo datasets. In the Epinions dataset, ASiNE and DDRE competed closely on both evaluation metrics. In the Yeast

GIN network, DDRE performed better than ASiNE in terms of accuracy but lagged behind in terms of optimized precision. Nonetheless, the results show that GASP can predict the unlabeled ties in signed networks from different domains more effectively and consistently than other methods for balanced datasets.

## 5.5 Evaluation in Imbalanced Benchmark Datasets

For imbalanced datasets, we utilized macro F1 for assessing the overall performance of the methods for both classes. For class-specific performance, we utilized the geometric mean of specificity and NPV for the negative (rare) sign prediction task. In Figure 14, the average values of macro F1 of different algorithms are plotted for different percentages of labeled edges in the networks. In the Wikipedia RfA, Slashdot Zoo, and Yeast GIN datasets, the performance of the proposed GASP method achieved better macro F1 values for all percentage values of labeled edges than all other methods used for comparison. In the Epinions dataset, GASP achieved macro F1 measure values of 0.6316 and 0.6323 for the 60% and 65% labeled edges, respectively, and performed better than other methods. In the case of imbalanced datasets, ASiNE and DDRE methods performed better in terms of macro F1 measure than NPECF and SRWR in the Wikipedia RfA and Yeast GIN datasets for different percentages of labeled edges.

![](/api/attachments/VJCRW7RC/fulltext/images/4f89eb8a793e12d516c91568da5f31740af2dba156eb602b770c588d6311993f.jpg)  
(a) Macro F1 results for Epinions

![](/api/attachments/VJCRW7RC/fulltext/images/888ba01ce4976e47e62451a32b7c8506c3ad172d971c66fb2b2b49c7a5c7320e.jpg)

![](/api/attachments/VJCRW7RC/fulltext/images/5e276ad00e37741e5a5468854a9461a612a8490b4550d34d11e25ed1e6e30068.jpg)  
(b) Macro F1 results for Wikipedia RfA

(c) Macro F1 results for Slashdot Zoo  
![](/api/attachments/VJCRW7RC/fulltext/images/a5471ca5ee4503e42a1cc3c87b953f4d8e1d7e546e661d938fbe831488a100b4.jpg)  
(d) Macro F1 results for Yeast GIN  
Figure 14. Macro F1 values for GASP, NPECF, SRWR, ASiNE, and DDRE Algorithms Used for Comparison on Different Imbalanced Datasets Used for Experiments

![](/api/attachments/VJCRW7RC/fulltext/images/4be04b5c4495ee9304123788225c0bf4604d7edc65a6c4a12c3874ee3e98fd0e.jpg)  
(a) GM (Specificity and NPV) for Epinions

![](/api/attachments/VJCRW7RC/fulltext/images/1b38286b311a11a29b68be03fa2479a71dbdc717c64ecb44970b09bcec38ebfa.jpg)  
(b) GM (Specificity and NPV) for Wikipedia RfA

![](/api/attachments/VJCRW7RC/fulltext/images/bd00cb90c7cb643dbaf73a8b80a6392ea80efcf19220e2c1fe0f0ef4922f341d.jpg)  
(c) GM (Specificity and NPV) for Slashdot Zoo

![](/api/attachments/VJCRW7RC/fulltext/images/8fa413054f7c77e1a7e94490c0d8a9d303b45f5c45ef5f9c30877040e30a3fe5.jpg)  
(d) GM (Specificity and NPV) for Yeast GIN  
Note: \*For Epinions, Slashdot Zoo, and Wikipedia RfA negative is the rare class and for Yeast GIN positive is the rare class.  
Figure 15. GM of Specificity and NPV\* for GASP, NPECF, SRWR, ASiNE, and DDRE Algorithms Used for Comparison on Different Imbalanced Datasets Used for Experiments

For class-specific performance, the results in Figure 15 show that GASP performed better than the other methods for the prediction of signs for the minority/rare class. In the Epinions, Wikipedia RfA, and Slashdot Zoo datasets, the negative sign class is the minority; in the Yeast GIN dataset, the positive sign class is the minority. For the minority class sign prediction, the GM of specificity and NPV (considering the negative sign as the class of interest for Epinions, Wikipedia RfA, and Slashdot Zoo, and the positive sign as the class of interest for Yeast GIN) were better for GASP than the other methods. The results suggest that GASP has a better predictive ability for sign prediction in imbalanced situations, as minority class prediction is considered to be more important (Branco et al., 2016).

The experimental evaluation suggests that the proposed GASP method is stable and performs better than the other domain-independent and structural balance theory-based methods used for comparison. The performance of the GASP is better because it utilizes the network structural information completely without any loss. In GASP, all ties, whether labeled or unlabeled, are utilized when performing information diffusion to predict the sign of unlabeled ties in a network. In contrast, NPECF and SRWR do not fully utilize the network structural information when predicting the sign of unlabeled ties. For SRWR, unlabeled ties must first be removed, leading to information loss. In NPECF, the two subnetworks contain only positive edges with unlabeled edges and negative edges with unlabeled edges, respectively, leading to information loss. For ASiNE and DDRE, information loss would also be present since these methods consider the positive subnetwork and negative subnetwork separately when learning the embeddings. The proposed GASP method is effective in predicting the labels for unsigned edges in networks for both balanced and imbalanced datasets.

The evaluation also shows that GASP is applicable when there is no information regarding the domain and when there is no information about which type of relationship (positive or negative) between objects dominates. For example, in the case of the Yeast GIN dataset, there are more negative ties, while in the other datasets, there are more positive ties.

## 5.6 Scalability Analysis

In order to evaluate the scalability of GASP, we also evaluated the number of iterations it takes to converge on benchmark datasets. As shown in Figure 16, the number of iterations required to converge (?????????? ≤

0.00001) to compute the final scores, which can be used to predict the label of the unsigned ties, is no more than 55 for all the benchmark datasets. Figure 16a plots the average error value for the different balanced datasets used for experiments and the number of iterations. Thus, GASP converges quickly and requires no more than 55 iterations to provide the converged scores. Also, for the unbalanced datasets (Figure 16b), the average error value converges in no more than 55 iterations. This analysis shows that GASP converges quickly and the number of iterations does not change drastically for different network sizes, thus providing evidence that the proposed method is suitable for realworld situations and scalable to large networks.

![](/api/attachments/VJCRW7RC/fulltext/images/dbc62b3617b3c7a5fd3fdbaa5f4afb1dc1a4a5264686ada9770efe40462b1bc6.jpg)

## 5.7 Sensitivity Analysis for α

To check the impact of α on the performance of the proposed GASP method, we performed a sensitivity analysis. We took different values of $\alpha \in [ 0 . 5 , 0 . 9 ]$ in the step size of 0.05; for each value, we plotted accuracy for balanced datasets and macro-F1 for imbalanced datasets for 60% labeled edges. The plots for balanced and imbalanced datasets are shown in Figure 17, which clearly shows that the performance of the GASP is not highly sensitive to the value of α and that performance is not impacted very much by the changing values of α. This suggests that the proposed GASP method is suitable in different domains.

(a) Plot for balanced datasets  
![](/api/attachments/VJCRW7RC/fulltext/images/88ccb72a567ac2b97f29ec592150b04685e349278983576c0fddfdeb3d685fb7.jpg)  
(b) Plot for imbalanced datasets  
Figure 16. Error vs Iteration Number Curve for Different Datasets

![](/api/attachments/VJCRW7RC/fulltext/images/1c08b06f0247f563f421808b1c424428ca0cc5cabad9c792a3b1e375391927d8.jpg)  
(a) Accuracy for different αvalues for balanced datasets

![](/api/attachments/VJCRW7RC/fulltext/images/0e848fc9563836cabdfc644fb3c9c28dfdd9cf976fa9e6721947b891a0c9493e.jpg)  
(b) Macro-F1 for different αvalues for imbalanced datasets  
Figure 17. Sensitivity Analysis for α for Different Datasets

## 6 Discussion

Social media platforms are increasingly impacting business and societal outcomes by facilitating individual expression and serving as a source of market intelligence to enhance brand loyalty through increased customer engagement . As such, the characteristics of nodes and ties in social media networks have theoretical and practical implications for mechanisms that provide informational and structural value. Tie signs in both online and offline networks are crucial, as they contribute to information disclosure and build affordances that can satisfy users’ needs (Karahanna et al., 2018). Despite the prevalence of structural and usergenerated data available on social media platforms, there is a conspicuous lack of available information on negative relationships (distrust) among users, thus limiting the algorithmic curation and recommendation capabilities of social media platforms (Kane et al., 2014). It is important to understand that the importance of positive and negative signed ties could be different depending on the research context. Typically, it is the minority class that users consider more interesting for predicting rare phenomena (e.g., in the context of credit card transactions, the interest would be in predicting fraudulent transactions, which would be the minority class; legitimate transactions would be the majority class). Aiming to enhance such capabilities, we propose a domain-agnostic design science-based method to predict tie signs in social networks irrespective of the minority or majority of one particular class.

The proposed GASP artifact consists of multiple network modeling and transformation techniques for the sign prediction of ties, and its credibility was demonstrated on a network of users curated from the IMDb platform. Further, experiments and comparative analysis performed over a variety of real-world networks demonstrated that the proposed artifact yields improved and robust sign prediction performance. As shown in Figures 13-15, the proposed sign prediction method performed consistently well irrespective of whether the negative signs or positive signs were in the minority. The results suggest that techniques such as augmented graph, symmetric normalization, graph regularization, and transductive label propagation complement each other to generate substantially better results for the sign prediction of network ties. The synergies of the graph regularized framework, random walks, symmetric normalization, and graph augmentation address several limitations of traditional methods, such as scalability issues, overfitting, and sensitivity to noise. Since edges are idiosyncratic in nature and the notion of homophily is not directly applicable, the proposed artifact could serve as a foundation for addressing other network-related problems, such as community detection and link prediction in signed networks. The proposed method’s integration of diverse theories represents a significant advancement in network analysis, with the potential to redefine limitations in the field of sign prediction and beyond. To the best of our knowledge, this is the first study that uses a design science approach for the sign prediction of network ties, thus allowing us to introduce four design guidelines that can benefit future design problems with similar characteristics.

The first design guideline pertains to the avoidance of decomposition of a network into subnetworks, which has been addressed in prior studies (Gupta & Mishra, 2020). When a network is decomposed (in any form, based on information available about the nodes or links of a network), critical information regarding the interconnections between subnetworks that could provide valuable insights into global patterns are disregarded, impairing the predictive or prescriptive outcomes. In contrast, when a model considers the entire network, it can better account for the full spectrum of influences and relationships, leading to more robust and reliable predictions. Therefore, network modeling methods should be based on strategies to augment and integrate the different types of information available in a network. This might include incorporating metadata about nodes (e.g., user attributes, interaction histories) or enhancing link data with additional context (e.g., communication content, frequency of interactions). By enriching the network with this augmented information, models can avoid the pitfalls associated with decomposition while better representing the true nature of relationships within a network.

The second design guideline is related to developing and utilizing new network datasets from emerging social media platforms to demonstrate, experiment with, and generalize the performance of proposed artifacts. This practice should complement experimentation and evaluation in established benchmark networks, contributing to a cumulative tradition of design science research where artifacts are rigorously evaluated both in previously available contexts and new evolving ones. While benchmark networks provide a standardized way to compare the performance of different artifacts, relying solely on them can limit the generalizability of research findings. Social media platforms are continually evolving, with new platforms emerging and existing ones undergoing significant changes in interaction patterns and network structures. Artifacts developed for network analysis must be evaluated in these contemporary contexts to ensure they remain effective and relevant. By doing so, researchers can ensure that their artifacts are not only grounded in established research traditions but also capable of meeting the demands of an evolving digital landscape.

The third design guideline concerns leveraging both the local and global structure of a network to develop domain-independent artifacts for network settings. Networks, whether social, biological, or technological, are characterized by complex interdependencies that can be analyzed at multiple levels. The local structure of a network refers to the immediate environment of a node, including its direct connections. This local perspective is crucial for understanding how individual nodes influence each other and how microlevel interactions contribute to the overall network behavior. The global structure encompasses the entire network’s topology, including large-scale patterns such as the overall connectivity, clustering, and the presence of hubs that play a critical role in the network’s function. Considering the global structure is essential for understanding how local interactions aggregate to form broader network phenomena. The effectiveness of artifacts designed for network analysis often hinges on their ability to capture both the local and global features. This dual approach ensures that the artifacts can effectively capture the intricate dynamics within a network, making them adaptable across different domains and applications.

The fourth design guideline pertains to using both balanced and imbalanced networks for experiments and for evaluating artifacts. The performance and utility of artifacts can vary significantly, depending on whether the network is balanced or imbalanced in terms of its structural properties (such as prevalence of positive vs. negative ties, distribution of node degrees, etc.). Evaluation in both balanced and imbalanced networks can help researchers ensure that the artifact is not overfitted to a specific type of network. Evaluating artifacts in balanced networks provides a baseline understanding of their performance, allowing researchers to assess an artifact’s functionality under controlled and ideal conditions. At the same time, since most real-world networks are not balanced, it is crucial to evaluate artifacts in imbalanced networks to understand their true effectiveness. Evaluation in imbalanced networks ensures that the artifact can handle complexities (such as skewed class distributions, varying node influence, and unpredictable interaction patterns) while delivering reliable results. By following this design guideline, researchers can ensure that their design science artifacts are tested comprehensively and are capable of delivering high-quality results across a variety of networked settings.

## 6.1 Theoretical Implications

This study has several theoretical implications. Social media platform owners use different features to build affordances ranging from self-presentation to competition to satisfy psychological needs such as selfidentity and autonomy (Karahanna et al., 2018). Thus, this study can help advance our understanding of how tie signs shape the characteristics and formation of social media networks and affect users’ networking behavior. Previous research in this realm has been limited to the strength and modality of ties (one-mode, two-mode, etc.), identifying the importance of nodes and clusters of closely related nodes (Gupta & Kumar, 2020; Gupta & Kumar, 2021; Kane & Alavi, 2008). Our research offers a new outlook for theoretical developments by developing a method for predicting tie signs in social networks.

Second, this study contributes to the literature on using design science research approaches for network analysis (Gupta & Tiwari, 2022; John et al., 2016; Sharif Vaghefi & Nazareth, 2021; Velichety & Ram, 2020). The design science research process is helpful in tackling grand societal challenges and can guide the development of artifacts to support social stability. The way we design, adapt, and synergistically combine the approaches of graph augmentation, affinity matrix computation, symmetric normalization, and label propagation for solving the problem of the sign prediction of network ties constitutes the underlying essence of the proposed artifact. In doing so, we also demonstrate the importance of rigorous evaluation of design science artifacts— particularly regarding separate evaluation in balanced and imbalanced networks and the significance of different evaluation metrics for these networks.

Third, this study offers scholars a new way to theorize about empirically observed performance variations in network mining tasks such as community detection, link prediction, and influence maximization. Earlier studies have used network decomposition-based approaches, limiting their generalizability due to information loss (Gupta & Mishra, 2020). The principles of the proposed sign prediction method can inspire the design of new artifacts for a variety of network processes. The synergistic effect of theoretical tenets such as graph theory, structural balance theory, random walk on graphs, and graph regularization can enhance the collective levels of utility of data generated through social media platforms.

Finally, this study underscores the importance of designing specifications for describing organizational interactions to capture the crucial aspects required for the initialization of signs of network ties. Such specifications can not only help in initialization but also in updating the characteristics of networks and their evolution due to changing user priorities or uncertainties in the business environment. The proposed GASP method performs graph augmentation in its initial stage, making it capable of handling label updates, which has implications for realizing flexible network-based technology implementations.

## 6.2 Practical Implications

Today’s social media landscape can be characterized by heterogeneity in applications. As applications have evolved from simple text-based posting platforms (for example, orkut.com) to complex platforms hosting live video streaming (such as instagram.com, etc.), relational ties in these platforms have emerged as important enablers of cross-side network effects that drive their revenues (Dou & Wu, 2021; Hinz et al., 2020). Therefore, it is important to more precisely consider the polarity of ties for estimating the network effects in twosided markets. The proposed GASP method for the sign prediction of network ties could be immensely beneficial for advertisers seeking to co-create value for social media platforms and their clients.

Second, our study suggests that business activities can be significantly improved by characterizing ties with signs rather than considering all ties to be positive or neutral. For example, in a massive multiplayer online game known as Pardus, every player can mark other players as “friends” or “enemies,” and on Bitcoin trading platforms known as Bitcoin Alpha, users can provide trust/distrust ratings (-10 to 10) to others (Szell & Thurner, 2010). This study designs a domainindependent approach for predicting signs of network ties, thereby offering a granular way to model social networks. Such an approach is crucial to advance the literature on how the generation of new social platforms can deliver superior business value. For example, GASP could be extended to build recommenders on review platforms such as TripAdvisor, Yelp, etc., by considering the polarity of relationships among users based on their hotel ratings. This could help hotel marketers evolve their targeting strategies over time.

Third, GASP could also help curb the negative effects of social media, such as societal polarization due to the propagation of misinformation, extremism, and conspiracy theories (Kaur & Gupta, 2023). Social media-induced polarization is a serious problem that requires an urgent solution (Gupta et al., 2022; Kitchens et al., 2020). The existing methods for detecting and quantifying polarization in social networks are scarce and do not consider the relationship signs (Qureshi et al., 2020). The proposed GASP method can be extended to detect and mitigate the polarization of communities in social networks because the availability of network tie sign information is a primary step in this endeavor.

## 6.3 Limitations and Future Work

This study attempts to bridge the research gap via convincing evidence in terms of the competitiveness of the proposed artifact with state-of-the-art methods. However, it is not without limitations. We hope that these limitations can be addressed in future research related to network analysis and design science.

First, GASP is applicable only to undirected social networks. The inference of tie signs in directed networks is an interesting avenue of research that could offer additional insights into the theoretical underpinnings leading to the formation and evolution of social media networks. In the future, we hope to extend the proposed approach for sign prediction to directed networks.

Second, GASP performs matrix operations for binary networks only, i.e., it gives the same weight to both positive and negative ties. Operations such as graph augmentation, symmetric normalization, and graph regularization should be explored and formulated for valued networks. Previous studies for community detection and link prediction in networks have attempted to model weighted networks (Zhang et al., 2016; Li et al., 2022). However, the sign prediction of ties in valued networks has not yet been examined in the context of the proposed framework. Our study opens the door for future studies to develop graph augmentation and label propagation strategies that consider the weighted scheme of signed network ties.

Third, the proposed method performs graph augmentation, which increases the network size. Thus, it may pose some challenges from the point of view of implementation in the context of very large networks. Advanced data structures could be explored for the efficient implementation of the concepts proposed in this work, making it more effective in very large networks. Also, if the prior label information is incorrect due to noisy information collection (Kirkley et al., 2019; Aref & Wilson, 2018), then it may affect the performance of the proposed method. Thus, improvements could be incorporated to make the proposed methodology more robust and to provide a higher level of performance for sign prediction.

Fourth, we used only user ratings on movies when creating the signed network from IMDb, ignoring the review text. The polarities of review texts could also be combined with ratings to create a social network. Also, we exclusively used the IMDb platform for our data collection and experiments. There is no theoretical reason to believe that GASP would not be effective in the sign prediction of networks emanating from other review platforms, such as TripAdvisor, Amazon, eBay, or Yelp. We hope to continue working on these aspects to test the effectiveness of the proposed approach.

## 7 Conclusion

This study introduced a novel sign prediction method for ties in social networks, which is based on the concepts of graph augmentation, symmetric normalization of the affinity matrix, graph regularization, and transductive label propagation. In doing so, we followed the design science research process, positioning our method as an improvement in the problem domain of the sign prediction of network ties. Prior studies have introduced the local neighborhood-based NbA method, the signed random walk-based SRWR method, the projection-based NPECF method, and deep learning-based ASiNE and DDRE methods. However, since they cannot accurately predict tie signs, their application is significantly limited. This study addresses the shortcomings of these state-of-the-art methods by using hitherto unexplored concepts of graph augmentation and random walk-based graph regularized transductive label propagation. Moreover, unlike other prior studies in this problem domain, our research follows the design science research paradigm, eliminates the assumptions of structural balance theory, and is applicable to both balanced and unbalanced networks.

The proposed solution can be applied to practice and real-world scenarios. For instance, in professional networks such as LinkedIn, competition, envy, or snobbism could result in implicit negative ties (Huang & Fan, 2022; Krasnova et al., 2015). The proposed solution can be used to infer the sign of professional ties

in such professional social media platforms, thereby improving networking opportunities and career prospects. Moreover, the proposed solution can play a significant role in managing conflicts within online communities by more accurately predicting negative ties and by helping platform administrators intervene more effectively. By proactively managing inimical behavior and reinforcing positive social connections, platforms could foster healthier online environments. Additionally, on gaming platforms, antagonistic behavior among players can reduce their participation and satisfaction. By identifying negative ties through the proposed solution, game developers and administrators could promptly mitigate such behavior and provide a more positive gaming environment. Last but not least, in collaborative learning environments, the proposed solution could assist educators in identifying negative dynamics within study forums or groups, enabling timely interventions that could improve learning and collaboration outcomes.

This study aims to stimulate more investigation into the intricate networks emanating from social media platforms. We hope that this research will serve as a springboard for future IS studies seeking to identify and address new, significant issues leading to the development of new social media features that can enable affordances to fulfill the psychological needs of users.

## References

Aggarwal, C., He, G., & Zhao, P. (2016). Edge classification in networks. Proceedings of the 32nd IEEE International Conference on Data Engineering (pp. 1038-1049).

Apaolaza, V., Hartmann, P., Medina, E., Barrutia, J. M., & Echebarria, C. (2013). The relationship between socializing on the Spanish online networking site Tuenti and teenagers’ subjective wellbeing: The roles of self-esteem and loneliness. Computers in Human Behavior, 29(4), 1282-1289.

Aref, S., & Wilson, M. C. (2018). Measuring partial balance in signed networks. Journal of Complex Networks, 6(4), 566-595.

Bastian, M., Heymann, S., & Jacomy, M. (2009). Gephi: An open source software for exploring and manipulating networks. Proceedings of the 3rd International AAAI Conference on Weblogs and Social Media.

Bergman, S. M., Fearrington, M. E., Davenport, S. W., & Bergman, J. Z. (2011). Millennials, narcissism, and social networking: What narcissists do on social networking sites and why. Personality and Individual Differences, 50(5), 706-711.

Boughorbel, S., Jarray, F., & El-Anbari, M. (2017). Optimal classifier for imbalanced data using Matthews correlation coefficient metric. PLOS One, 12(6), Article e0177678.

Branco, P., Torgo, L., & Ribeiro, R. P. (2016). A survey of predictive modeling on imbalanced domains. ACM Computing Surveys, 49(2), 1-50.

Boyd, D. M., & Ellison, N. B. (2007). Social network sites: Definition, history, and scholarship. Journal of Computer‐Mediated Communication, 13(1), 210-230.

Brzozowski, M. J., Hogg, T., & Szabo, G. (2008). Friends and foes: ideological social networking. Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 817- 820).

Cartwright, D., & Harary, F. (1956). Structural balance: a generalization of Heider’s theory. Psychological Review, 63(5), 277-293.

Casciaro, T., & Lobo, M. S. (2008). When competence is irrelevant: The role of interpersonal affect in taskrelated ties. Administrative Science Quarterly, 53(4), 655-684.

Chen, H., De, P., Hu, Y., & Hwang, B. H. (2014). Wisdom of crowds: The value of stock opinions transmitted through social media. The Review of Financial Studies, 27(5), 1367-1403.

Chen, X., Wei, S., Davison, R. M., & Rice, R. E. (2020). How do enterprise social media affordances affect social network ties and job performance? Information Technology & People, 33(1), 361- 388.

Danger, R., Pla, F., Molina, A., & Rosso, P. (2014). Towards a Protein–Protein Interaction information extraction system: Recognizing named entities. Knowledge-Based Systems, 57, 104-118.

Das, A. C., Gomes, M., Patidar, I. L., & Thomas, R. (2022). Social media as a service differentiator: How to win. McKinsey & Company. https://www.mckinsey.com/capabilities/operatio ns/our-insights/social-media-as-a-servicedifferentiator-how-to-win

Dou, Y., & Wu, D. J. (2021). Platform competition under network effects: Piggybacking and optimal subsidization. Information Systems Research, 32(3), 820-835.

Drenik, G. (2022). The creator economy is booming. Here’s how businesses can tap into its potential. Forbes. https://www.forbes.com/sites/garydrenik/ 2022/08/23/the-creator-economy-is-boomingheres-how-businesses-can-tap-into-its-potential

Fast, V., Schnurr, D., & Wohlfarth, M. (2023). Regulation of data-driven market power in the digital economy: Business value creation and competitive advantages from big data. Journal of Information Technology, 38(2), 202-229.

Gersick, C. J., Dutton, J. E., & Bartunek, J. M. (2000). Learning from academia: The importance of relationships in professional life. Academy of Management Journal, 43(6), 1026-1044.

Girdhar, N., & Bharadwaj, K. K. (2019). Community detection in signed social networks using multiobjective genetic algorithm. Journal of the Association for Information Science and Technology, 70(8), 788-804.

Greene, K., Derlega, V. J., & Mathews, A. (2006). Selfdisclosure in personal relationships. The Cambridge handbook of personal relationships, 409, 427.

Gregor, S., & Hevner, A. R. (2013). Positioning and presenting design science research for maximum impact. MIS Quarterly, 37(2),337-355.

Guha, R., Kumar, R., Raghavan, P., & Tomkins, A. (2004). Propagation of trust and distrust. Proceedings of the 13th International Conference on World Wide Web (pp. 403-412).

Gupta, M., & Mishra, R. (2020). Network projectionbased edge classification framework for signed

networks. Decision Support Systems, 135, Article 113321.

Gupta, S., Deodhar, S. J., Tiwari, A. A., Gupta, M., & Mariani, M. (2024). How consumers evaluate movies on online platforms? Investigating the role of consumer engagement and external engagement. Journal of Business Research, 176, Article 114613.

Gupta, S., Jain, G., & Tiwari, A. A. (2022). Polarised social media discourse during COVID-19 pandemic: evidence from YouTube. Behaviour & Information Technology, 1-22.

Gupta, S., & Kumar, P. (2020). An overlapping community detection algorithm based on rough clustering of links. Data & Knowledge Engineering, 125, Article 101777.

Gupta, S., & Kumar, P. (2021). A constrained agglomerative clustering approach for unipartite and bipartite networks with application to credit networks. Information Sciences, 557, 332-354.

Gupta, S., Kumar, S., & Kumar, P. (2016). Evaluating the predictive power of an ensemble model for economic success of Indian movies. The Journal of Prediction Markets, 10(1), 30-52.

Gupta, S., & Tiwari, A. A. (2022). A design-based pedagogical framework for developing computational thinking skills. Journal of Decision Systems, 31(4), 433-450.

Han, J., Pei, J., & Kamber, M. (2011). Data mining: Concepts and techniques. Elsevier.

Harary, F., Norman, R. Z., & Cartwright, D. (1965). Structural models: An introduction to the theory of directed graphs. John Wiley & Sons.

Hinz, O., Otter, T., & Skiera, B. (2020). Estimating network effects in two-sided markets. Journal of Management Information Systems, 37(1), 12-38.

Huang, X., & Fan, P. (2022). The dark side of social media in the workplace: A social comparison perspective. Computers in Human Behavior, 136, Article 107377.

Jeh, G., & Widom, J. (2002, July). Simrank: a measure of structural-context similarity. Proceedings of the 8th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (pp. 538- 543).

John, B. M., Chua, A. Y., Goh, D. H. L., & Wickramasinghe, N. (2016). Graph-based cluster analysis to identify similar questions: A design science approach. Journal of the Association for Information Systems, 17(9), 590-613.

Jung, J., Jin, W., & Kang, U. (2020). Random walk-based ranking in signed social networks: Model and

algorithms. Knowledge and Information Systems, 62(2), 571-610.

Kane, G. C., & Alavi, M. (2008). Casting the net: A multimodal network perspective on user-system interactions. Information Systems Research, 19(3), 253-272.

Kane, G. C., Alavi, M., Labianca, G., & Borgatti, S. P. (2014). What’s different about social media networks? A framework and research agenda. MIS Quarterly, 38(1), 275-304.

Karahanna, E., Xu, S. X., Xu, Y., & Zhang, N. A. (2018). The needs–affordances–features perspective for the use of social media. MIS Quarterly, 42(3), 737-756.

Katona, Z., Zubcsek, P. P., & Sarvary, M. (2011). Network effects and personal influences: The diffusion of an online social network. Journal of Marketing Research, 48(3), 425-443.

Kaur, K., & Gupta, S. (2023). Towards dissemination, detection and combating misinformation on social media: a literature review. Journal of Business & Industrial Marketing, 38(8), 1656-1674.

Kirkley, A., Cantwell, G. T., & Newman, M. E. (2019). Balance in signed networks. Physical Review E, 99(1), Article 012320.

Kitchens, B., Johnson, S. L., & Gray, P. (2020). Understanding echo chambers and filter bubbles: The impact of social media on diversification and partisan shifts in news consumption. MIS Quarterly, 44(4), 1619-1649.

Krasnova, H., Widjaja, T., Buxmann, P., Wenninger, H., & Benbasat, I. (2015). Research note—why following friends can hurt you: an exploratory investigation of the effects of envy on social networking sites among college-age users. Information Systems Research, 26(3), 585-605.

Kumar, P., Gupta, S., & Bhasker, B. (2017). An upper approximation-based community detection algorithm for complex networks. Decision Support Systems, 96, 103-118.

Labianca, G., & Brass, D. J. (2006). Exploring the social ledger: negative relationships and negative asymmetry in social networks in organizations. Academy of Management Review, 31(3), 596-614.

Labianca, G., Brass, D. J., & Gray, B. (1998). Social networks and perceptions of intergroup conflict: The role of negative relationships and third parties. Academy of Management Journal, 41(1), 55-67.

Lee, S. Y. (2014). How do people compare themselves with others on social network sites? The case of

Facebook. Computers in Human Behavior, 32, 253-260.

Lee, Y. C., Seo, N., Han, K., & Kim, S. W. (2020). ASiNE: Adversarial signed network embedding. Proceedings of the 43rd International ACM SIGIR Conference on Research and Development in Information Retrieval (pp. 609-618).

Leidner, D. E. (2020). What’s in a contribution?. Journal of the Association for Information Systems, 21(1), 238- 245.

Leonardi, P. M. (2011). When flexible routines meet flexible technologies: Affordance, constraint, and the imbrication of human and material agencies. MIS Quarterly, 35(1), 147-167.

Leskovec, J., Huttenlocher, D., & Kleinberg, J. (2010a). Signed networks in social media. Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 1361-1370).

Leskovec, J., Huttenlocher, D., & Kleinberg, J. (2010b). Predicting positive and negative links in online social networks. Proceedings of the 19th International Conference on World Wide Web (pp. 641-650).

Li, L., Wen, Y., Bai, S., & Liu, P. (2022). Link prediction in weighted networks via motif predictor. Knowledge-Based Systems, 242, Article 108402.

Liebman, E., Saar-Tsechansky, M., & Stone, P. (2019). The right music at the right time: Adaptive personalized playlists based on sequence modeling. MIS Quarterly, 43(3), 765-786.

Maier, C., Laumer, S., Eckhardt, A., & Weitzel, T. (2015). Giving too much social support: social overload on social networking sites. European Journal of Information Systems, 24(5), 447-464.

Pang, J., Yuan, W., & Guan, D. (2021). Tri-domain pattern preserving sign prediction for signed networks. Neurocomputing, 421, 234-243.

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. Journal of Management Information Systems, 24(3), 45-77.

Qureshi, I., Bhatt, B., Gupta, S., & Tiwari, A. A. (2020). Special issue call for papers: Causes, symptoms and consequences of social media induced polarization (SMIP). Information Systems Journal. https://onlinelibrary.wiley.com/pb-assets/assets/ 13652575/ISJ\_SMIP\_CFP.pdf?msockid=0bf62b5 8b0e96b7138143f02b1746a6a

Ranawana, R., & Palade, V. (2006). Optimized precision—a new measure for classifier performance evaluation. Proceedings of the IEEE

International Conference on Evolutionary Computation (pp. 2254-2261).

Richa, & Bedi, P. (2021). Trust and distrust based crossdomain recommender system. Applied Artificial Intelligence, 35(4), 326-351.

Sajtos, L., Cao, J. T., Zhang, W., Peko, G., & Sundaram, D. (2023). Developing a feature-centric and affordance-based conceptualization of social media interactions. Asia Pacific Journal of Marketing and Logistics, 35(5), 1224-1244.

Schoenmueller, V., Netzer, O., & Stahl, F. (2020). The polarity of online reviews: Prevalence, drivers and implications. Journal of Marketing Research, 57(5), 853-877.

Sharif Vaghefi, M., & Nazareth, D. L. (2021). Mining online social networks: Deriving user preferences through node embedding. Journal of the Association for Information Systems, 22(6), 1625- 1658.

Stieglitz, S., & Dang-Xuan, L. (2013). Emotions and information diffusion in social media—sentiment of microblogs and sharing behavior. Journal of Management Information Systems, 29(4), 217- 248.

Stark, C., Breitkreutz, B. J., Reguly, T., Boucher, L., Breitkreutz, A., & Tyers, M. (2006). BioGRID: a general repository for interaction datasets. Nucleic Acids Research, 34(suppl\_1), D535-D539.

Stein, J., Mandemakers, J., & van de Rijt, A. (2023). Limited evidence for structural balance in the family. Network Science, 11(4), 589-614.

Szell, M., & Thurner, S. (2010). Measuring social dynamics in a massive multiplayer online game. Social Networks, 32(4), 313-329.

Tang, J., Chang, Y., Aggarwal, C., & Liu, H. (2016). A survey of signed network mining in social media. ACM Computing Surveys, 49(3), 1-37.

Tremblay, J. P., & Cheston, G. A. (2003). Data structures and software development in an object-oriented domain: Java edition. Prentice Hall.

Turel, O., & Qahri‐Saremi, H. (2023). Responses to ambivalence toward social networking sites: A typological perspective. Information Systems Journal, 33(2), 385-416.

Valenzuela, S., Park, N., & Kee, K. F. (2009). Is there social capital in a social network site?: Facebook use and college students’ life satisfaction, trust, and participation. Journal of Computer-Mediated Communication, 14(4), 875-901.

Velichety, S., & Ram, S. (2020). Finding a needle in the haystack: Recommending online communities on social media platforms using network and design

science. Journal of the Association for Information Systems, 22(5), 1285-1310.

Venkataramani, V., Labianca, G. J., & Grosser, T. (2013). Positive and negative workplace relationships, social satisfaction, and organizational attachment. Journal of Applied Psychology, 98(6), 1028.

Victor, P., Cornelis, C., De Cock, M., & Teredesai, A. M. (2011). Trust-and distrust-based recommendations for controversial reviews. IEEE Intelligent Systems, 26(1), 48-55.

Wang, W., Xu, J., & Wang, M. (2018). Effects of recommendation neutrality and sponsorship disclosure on trust vs. distrust in online recommendation agents: Moderating role of

explanations for organic recommendations. Management Science, 64(11), 5198-5219.

Xu, P., Zhan, Y., Liu, L., Yu, B., Du, B., Wu, J., & Hu, W. (2022). Dual-branch density ratio estimation for signed network embedding. Proceedings of the ACM Web Conference (pp. 1651-1662).

Zhang, K., Bhattacharyya, S., & Ram, S. (2016). Largescale network analysis for online social brand advertising. MIS Quarterly, 40(4), 849-868.

Zhou, D., Bousquet, O., Lal, T. N., Weston, J., & Schölkopf, B. (2004). Learning with local and global consistency. Proceedings of the 17th International Conference on Neural Information Processing Systems (pp. 321-328).

## About the Authors

Mukul Gupta is an associate professor in the Information Systems area at the Indian Institute of Management Indore, India. He received his PhD in information technology and systems from the Indian Institute of Management Lucknow, India. Mukul Gupta has published in reputed journals in the areas of recommender systems, information network analytics, and signed networks. His current research interests include e-commerce, recommendation systems, signed information networks, web and data mining, and social media analytics.

Samrat Gupta is an associate professor in the Information Systems area at the Indian Institute of Management Ahmedabad, India. He also serves as a senior researcher at the University of Agder, Norway, and a research fellow at the Bratislava University of Economics and Business, Slovakia. He obtained his doctoral fellowship from the Indian Institute of Management Lucknow, India. He has extensively published in journals of international repute (including FT-50 and CABS 4/4\*) contributing to the areas of network theoretic modeling, information disorder, user engagement on online platforms, and user-centered digitalization. His research projects have been funded by the Ministry of Education, Government of India’s SPARC program, Slovak Research and Development Agency, and the European Union’s Horizon research and innovation program.

Giri Kumar Tayi is a professor of management science and information systems at the State University of New York at Albany. He obtained his PhD from Carnegie Mellon University, and his research and teaching interests are interdisciplinary and span the fields of information systems, operations management, and operations research. He has published over 75 refereed journal articles, covering the above three fields. Many of the articles appear in top-tier (FT-50 and UTD-24) academic journals. He serves or has served on the editorial boards of top-tier academic journals such as Information Systems Research (AE and SE), Journal of the Association for Information Systems (SE), and Production and Operations Management (SE). He serves or has served as a visiting research professor/scholar at universities and management institutes around the world
