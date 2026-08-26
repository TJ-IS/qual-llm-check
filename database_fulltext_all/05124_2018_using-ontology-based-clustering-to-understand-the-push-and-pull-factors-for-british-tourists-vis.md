---
otero_id: 5124
otero_key: "VCEBJFZ8"
title: "Using ontology-based clustering to understand the push and pull factors for British tourists visiting a Mediterranean coastal destination"
authors: "Aida Valls; Karina Gibert; Alícia Orellana; Salvador Antón-Clavé"
year: "2018"
journal: "Information & Management"
doi: "10.1016/j.im.2017.05.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Title: Using Ontology-based Clustering to understand the push and pull factors for British tourists visiting a Mediterranean coastal destination

Authors: Aida Valls, Karina Gibert, Al´ıcia Orellana, Salvador Anton-Clav´ e´

![](/api/attachments/VCEBJFZ8/fulltext/images/4e446be3d8c7de99711c0ca0e82df431b493f2e0ff1da347398eddb2a6bd45ee.jpg)

PII: S0378-7206(17)30392-0

DOI: http://dx.doi.org/doi:10.1016/j.im.2017.05.002

Reference: INFMAN 3000

To appear in: INFMAN

Received date: 4-12-2015

Revised date: 6-3-2017

Accepted date: 2-5-2017

Please cite this article as: Aida Valls, Karina Gibert, Al´ıcia Orellana, Salvador Anton-´ Clave, Using Ontology-based Clustering to understand the push and pull factors´ for British tourists visiting a Mediterranean coastal destination, Information and Managementhttp://dx.doi.org/10.1016/j.im.2017.05.002

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Using Ontology-based Clustering to understand the Push and Pull factors for British tourists visiting a Mediterranean coastal destination

Aida Valls<sup>(1),</sup> Karina Gibert<sup>(2),</sup> Alícia Orellana<sup>(3),</sup> Salvador Antón-Clavé<sup>(4)</sup>

<sup>(1)</sup>Department of Computer Science and Mathematics. Universitat Rovira i Virgili. Tarragona, Catalonia (Spain) aida.valls@urv.cat

<sup>(2)</sup>Department of Statistics and Operations Research Knowledge Engineering and Machine Learning group Universitat Politècnica de Catalunya-BarcelonaTech, Barcelona. Catalonia (Spain) karina.gibert@upc.edu

<sup>(3)</sup>Costa Daurada Observatory of Tourism. Tourism and Leisure Science & Technology Park alicia.orellana@pct-turisme.cat

<sup>(4)</sup> Research Group on Territorial Analysis and Tourism Studies. Universitat Rovira i Virgili. Vila-seca, Catalonia (Spain) salvador.anton@urv.cat

Corresponding author: Aida Valls aida.valls@urv.cat

## Highlights

 Motivation and destination meaning are crucial to understand tourist’s choices

 Destination managers should include motivation and meaning as open questions in surveys

 Semantic interpretation of open questions can be performed with ontologies

 Clustering based on Ontologies can discover more meaningful tourist segments

## Abstract

This paper studies why British tourists decide to travel to a particular destination in a Catalan region. The analysis is based on a survey that includes open-ended questions.

#

First, we propose the operationalization of the concepts of motivation and meaning as push–pull factors when choosing a destination. Second, an ontology-based clustering method is presented, which makes it possible to analyse these qualitative factors from a semantic perspective to obtain tourist segments. A benchmark confirms that the segmentation obtained is better than that generated using classic clustering methods. The results show that different meanings can be associated with any single place.

Data Mining; Tourism Motivations; Destination Meaning; Ontologies; Qualitative data Tourism Geography.

## 1. Introduction, aims and objectives

There is a great need to understand how travellers choose their holiday destinations (Jang et al., 2009; Guillet et al., 2011), and there is therefore an increasing amount of research being performed to analyse the roles played by many factors that affect the decision-making of tourists travelling to a single destination (Krippendorf, 1987; Dann, 2014; Prayag and Hosany, 2014; Wang et al, 2015).

It has long been acknowledged that tourists are influenced by psychological aspects when choosing a destination (Gee et al., 1984; Gardiner et al., 2013; Pearce and Parker, 2013; French et al., 2000; Pearce and Lee 2005) and that motivations are one of the main determinants of their destination choice (Iso-Ahola, 1982; Sirakava et al., 2001; Pearce, 1993; Crompton, 1979; Dann, 1981; Pearce and Lee, 2005; Um and Cromptom 1990; Zhao, 2014; Nyaupane et al., 2011). It has also been recognised that decisionmaking is linked to factors related to the characteristics of each single destination, mainly to its attractions and attributes (Grimm and Needham, 2012). However, despite this general recognition, there is still limited empirical evidence on the scope and characteristics of the relationship between the roles played by motivations and destination attributes in the decision-making process. Indeed, it can even be assumed that this may be very specific to each person for each destination (Jang et al., 2009). Attempting to relate the psychosocial needs that predispose a person towards travelling and the attributes and characteristics that attract a person to one specific destination rather than another, the classic push–pull theory (Dann, 1977), widely accepted in the tourist literature (Jang and Cai, 2002; Barkhordari et al, 2014; Ward, 2014; Mody et al, 2014), is a valid framework for trying to understand the decision-making behind tourism travel (Jang and Cai, 2002; Klenosky, 2002; Uysal et al, 2008; Dann, 2014).

Research related to this aspect has mainly been performed using data from some of the periodic surveys conducted elsewhere in the world (Baloglu, 2000). A significant number of investigations have also designed their own data collection procedures. However, in most cases, the available data do not make it possible to really understand the central issue of why tourists select a specific destination in which to spend their holidays. Interestingly, a common feature of many surveys, as recommended by Eurostat and the United Nations World Tourism Organization (see Massieu, 2007), is the use of closed-ended categories when asking about reasons for going to the destination. Investigations usually also apply conventional statistical analysis to process the resulting available data. Bearing this in mind and considering the extent and utility of the results obtained so far, it can be stated that another kind of approach might be worth exploring.

Aware of the importance of having extensive knowledge of tourists and tourist decisionmaking, the Costa Daurada Tourism Observatory in Southern Catalonia has since 2001 been conducting a continuous survey through the observation of tourist activity in the local destinations of the two main regional tourism brands of the province of Tarragona: the Costa Daurada and the Terres de l’Ebre. A report is issued periodically and includes basic statistics on tourist characteristics, demographic profiles, types of trip, relations with the destination, and other issues relating to destination choice.

It is interesting to note that after working for 10 years using questions with closedended responses (as do most of the surveys in other destinations when asking about the reasons behind the tourist’s decision to come to the destination), the Observatory decided some years ago to change and start using some open-ended type questions. The reason for this was that the final users of the survey results, mainly tourist firms, operators and destination managers, were unable to draw relevant insights about destination choice using closed-ended responses. As a result, since 2011, the Observatory has included two open-ended questions when asking tourists about their motivations and the meaning of the destination, which also relates to their reason for selecting it.

All the responses are given spontaneously by tourists and have no vocabulary restrictions. These data are clearly of a different type to those obtained from classic closed-ended responses where the respondent has to choose from an a priori closed set of predefined possible answers. They also provide a myriad of new opportunities for analysis including the chance to explore new ways of analysing the tourist’s specific destination choice and to disentangle the roles of motivation and destination factors in this decision.

The main purpose of this paper is therefore to introduce specially designed advanced methods of processing the open-ended spontaneous responses given by travellers when asked about the motivations and meanings of a certain destination and extracting relevant knowledge as regards why they decided to visit that destination. To do this, we operationalise the Push–Pull theory (Dann, 1977; Dann, 1981; Dann, 2014; Crompton, 1979; Klenosky, 2002) by using motivations as the push factor and meanings as the pull factor.

Analysing openly expressed non-numerical information obviously requires more sophisticated techniques than the descriptive statistics conventionally used up to now in this context. Therefore, we apply recent advances in the field of Artificial Intelligence (AI), and indeed we aim to show how methods derived from the field of AI may be really suitable for solving this problem and, in particular, for exploring the segmentation of tourists according to the relationship existing between the motivation and meaning of the tourist destination.

To conduct a proper analysis, the tourists’ spontaneous responses had to be processed (semantic analysis), and therefore segmentation techniques were appropriately combined with the interpretation of the terms used by tourists from a semantic point of view. Segmentation was first used in marketing in the last century (Smith, 1956). Automatic clustering techniques were introduced in the seminal paper by Haley (1968) and became a popular and useful market segmentation tool based on survey data (Dolnicar, 2002). Punj (1983) discussed the advisability of using clustering methods to support the automatic construction of segments. Some limitations of classic clustering algorithms are outlined in a more recent survey (Dolnicar, 2013). In the present paper, automatic clustering methods will be used in a proposal of general methodology that can be easily extended to other scenarios and replicated for other languages. A new clustering technique known asClustering based on Ontologies (CbO) (Batet et al., 2010) that addresses the problem in these terms has been used to find clusters that could automatically consider the interpretation of the terms.

Thus, the analysis presented here uses ontology-based clustering to exploit the data from the Costa Daurada Tourism Observatory database relating to the open-ended questions concerning motivations and meanings for British tourists visiting the province the Tarragona. The results show that the method can coherently, appropriately and effectively identify segments of tourists by using qualitative descriptions of the motivation for choosing the destination, openly expressed, and qualitative words related to the general meaning that the destination has for these tourists. The method can generate meaningful, useful and distinguishable tourist profiles that fulfil the standard requirements of effectiveness already referred to by Bull (1995).

The paper is structured as follows: Section 2 sets out the state of the art in the research areas of both tourists’ decision-making regarding travel to a destination and AI applications to tourism. Section 3 proposes a new methodological framework to make the segmentation of tourists based on the push–pull factor model. Section 4 presents the results obtained in a case study of British tourists visiting the Costa Daurada and the Terres de l’Ebre (regional tourism brands for the province of Tarragona in southern Catalonia, Spain) and finally Section 5 presents the conclusions of this case study along with conclusions regarding the methodological framework proposed.

## 2. State of the art

This section discusses the state of the art of relevant topics for the analysis relating to the fields of tourism research and computational analysis.

## 2.1. Introducing the meaning of destinations as a pull factor for understanding traveller choices

Widely used in tourism research, the push–pull theory (Dann 2014) is a valid framework for understanding tourism travel and decision-making (Nikjoo and Ketabi, 2015; Barkhordari et al, 2014; Ward, 2014; Mody et al, 2014; Uysal et al, 2008; Prayag and Hosany, 2014). Most importantly for the analysis performed in this paper, it is also useful for framing the operationalization of the two types of open-ended question (motivations and meanings) available from the Costa Daurada Tourism Observatory.

In conventional Push–Pull theory, push factors are those considered to be psychosocial needs that predispose a person to travel, while pull factors are those that attract a person

#

to a specific destination rather than another once the push processes have been activated. In early studies on this classic theory, Dann (1977) and Crompton (1979) provided empirical evidence by reporting nine factors—seven psychosocial push factors and two pull factors—classified as cultural by the authors. The push factors considered by Crompton (1979) were the need to escape from the everyday environment, exploration and evaluation of the self, relaxation, prestige, regression due to moments of less responsibility, improved family relationships (as travel is an opportunity to bring the members of the family together) and the promotion of social relationships (as holidays are a suitable time for this). According to Dann (1977), these are factors that stimulate the desire to travel and are related to the commonly accepted concept of motivation. Additionally, Crompton considered that the pull or drag factors emerging from the tourist destination were novelty and education. According to this theory, the specific content of the pull or drag factors could be very specific to each person and especially to each destination. Overall, factors are generally related to the characteristics of the destination, its attractions and attributes (Klenosky, 2002).

When reviewing the academic tourism literature, it emerges clearly that motivation— the push factor in most analyses using the Push–Pull theoretical framework—is a relevant factor. Indeed, even though the oldest theories on motivation were merely classifications and typologies of tourists (Cohen, 1972; Plog, 1971; 1990; 1991), motivation has been extensively used to divide the tourist market into meaningful segments (Beh and Bruyère 2007; Chang et al., 2006; Formica and Uysak 1998; Sung et al., 2016; Park and Yoon 2009; Brida et al., 2012; Lee et al., 2013; Hsu et al., 2010). However, as stated in the introduction, the tourist’s decision-making process derives not only from motivation but also from other factors—the pull factors—related to the destination, such as the images, perceptions, previous experience and available information that tourists have (Brown and Chalmers, 2003; Lin et al, 2007). On the other hand, unlike the push factor, which is usually analysed through motivations, the pull factor has been operationalised through a number of different indicators including destination attributes and the perceived images of the destination. The latter is the case, for instance, of a recent study (Prayag and Hosany, 2014) analysing the reasons that why young tourists from the United Arab Emirates come to Europe, and, along similar lines, it is also the case of studies such as those by Baloglu and McCleary (1999), Beerli and Martin (2004), Prayag, (2010), Kim and Perdue (2011), Prayag and Ryan (2011) and Mariné-Roig and Anton-Clavé (2017).

Unlike papers that use perceived images, perceptions or destination attributes as pull factors, our paper seeks to take as a pull factor the ‘meaning that a destination evokes to tourists’. This indicator has not been commonly used, probably because of the type of data available from regular surveys on destinations or because of the various means usually used by researchers when trying to quantitatively measure the meaning of a single destination rather than the usefulness of the concept. In this regard, it is common in studies that analyse the meaning of destination, for example, to measure it indirectly using stay data, services consumed or the interaction among tourists (Dolnicar and Grün, 2013; Snepenger et al., 2004) instead of obtaining results directly from the spontaneous responses of tourists as we have through the survey used by the Costa Daurada Tourism Observatory.

To introduce the meaning of a destination in a Push–Pull model of segmentation of tourists according to their decision to travel while at the same time including their motivations, it is essential that these can be measured and analysed. In this paper, we propose a simultaneous measurement of the motivations and meanings of tourists that, as far as the authors are aware, has not been explored before. Thus, our contribution takes a step forward by defining a push–pull operationalization relating to motivations and meaning that introduces two different novelties. First, the introduction of the meaning of the destination as a pull factor when operationalizing the model, and second, the use of open-ended responses when analysing both motivations and meanings.

Meaning is a complex term with many competing and complementary definitions and interpretations that can be studied from various disciplines (Gergen, 1994 p.19; MacCannell, 2003) and is related to the geographical expression of sense of place (Cresswell, 2005). Some papers propose emotional approaches to the concept of meaning (Hirschman and Stern 1999; Prayag et al., 2017; Dickinger and Lalicic, 2016; Gaski and Etzel 1986), while a few deal with meaning within the field of leisure and tourism services, practices and places (Ekinci et al. 2013). In our analysis, the meaning of destination can be understood as the summary of everything coming to tourists from

#

the sphere of emotions associated with the destination. Meaning is relevant because emotions, personal feelings, perceptions and attitudes related to the destination can be summarised through it. It can also provide precise market segmentation, grouping homogeneous customers together (Wedel and Kamakura, 2000) and helping to understand the dynamic and changing nature of human motivation (Pearce and Packer, 2013).

Meaning is obviously not an objective factor, and one destination can have different meanings for different people. Nevertheless, this does not necessarily constitute a constraint as regards introducing it into the Push Pull modelling; in fact, it will be useful in helping to better understand why tourists with different motivations decide to go to the same destination. What really matters here is not whether the meaning given to a destination is real, but whether the transformation of the destination into an idea (the meaning that it has for each single tourist) determines any process of decision-making related to a willingness to travel there. This transformation, far from being objective, clearly states the difference between the destination and the meaning of the destination, as can be explained in accordance with the system of social values (MacCannell, 1976; MacCannell, 2003) that frames the decision of each individual. It is known that the value of a destination directly depends on the meaning it has for each tourist (Bourdieu, 1979) and, in the same vein, it is also well known that, from a sociological perspective, some authors (Urry, 1990; Hankinson, 2004) argue that destinations, as part of their functional attributes, have symbolic attributes which are reflected in the meaning they have for tourists.

Thus, it can be interpreted that meaning can consistently act as a pull factor for each specific destination and, combined with motivations, can make it possible to discover why tourists visit them. The challenge is, then, how to measure both motivations and meanings and how to handle the data in order build an explanation of why a destination is selected. We decided to solve these last issues through the use of advanced techniques of tourist segmentation able to deal with open-ended survey answers and the application of semantic clustering procedures.

## 2.2. On the techniques used for tourist segmentation

The segmentation process is fundamental in tourism marketing. According to the American Marketing Association, different customer segments can be chosen as market targets needing different marketing strategies. Useful segments should be effective, identifiable, distinguishable, accessible, measurable, substantial, operative and stable to make sustainable predictions for the future (Pires et al., 2001).

Market segmentation in the field of tourism has a long tradition. There are two fundamental approaches: a priori segmentation (where the relevant criteria for distinguishing tourists are known in advance, such as archetypes or demographic profiles) and post hoc segmentation (derived from data analysis usually from surveys). This second approach has attracted greater interest since the 1980s, as shown in the review (Dolnicar, 2002). Tourist segmentation is mainly approached using statistical techniques such as correspondence analysis (Diana and Pronello, 2010), exploratory factor analysis, discriminant techniques, chi-squared automatic interaction detection (Chen 2003) and different cluster analysis methods such as k-means (Pronello and Camusso, 2011; Pesonen 2012) and Ward’s method (Bigné and Andreu, 2004; Park and Yoon, 2009; Hosany and Prayag, 2013). Most of these expect a dataset containing strictly numerical variables. Recently, Brida et al. (2013) made a proposal for binary variables.

The data types considered in the literature in the context of tourism typically combine numerical variables with nominal variables (Diana and Pronello, 2010), binary variables (Brida et al., 2013; D’Urso et al., 2013) or variables with a numerical Likert-type scale (with five or seven values) (Chen, 2003; Bigne and Andreu, 2004; Hosany and Prayag 2013). This makes it appropriate to combine cluster analysis with factor analysis (Wedel and Kamakura, 2000; Park and Yoon, 2009; Pronelo and Camusso, 2011; Pesonen, 2012). However, this approach leads to clusters identified over the factorial space, which might cause interpretation problems, since the interpretation of the factors is not always trivial.

Despite the apparent relevance of tourist segmentation for business, the generation of homogeneous and useful market segments with heterogeneous datasets is still an open problem (Pires et al., 2011). The benefits of innovative technologies for cluster identification continue to be poorly exploited in the field (Chen, 2003). Following this direction, the latest developments in data mining and artificial intelligence offer new possibilities for analysing heterogeneous data matrices without the need to move to a fictitious space, such as the factorial space, thereby avoiding interpretation drawbacks. In addition, AI introduces the possibility of analysing qualitative information from a semantic point of view, as well as open-ended questions, which can fit well into the framework of trying to obtain tourist segments based on the motivation of the tourists and taking into account the meaning that the destination evokes for them. In this work, both the motivations and the meanings are modelled through words directly expressed by the tourists. Special attention is paid to taking into account the semantics of those words in the process of identifying tourists with similar motivations or meanings. This can be performed by using the semantic clustering method described in Section 2.3.

## 2.3 Semantic Clustering

The importance of including domain knowledge in the data mining procedure is crucial in many information systems (Feelders et al., 2000; Chen et al., 2013). Some works show the benefits of managing the semantics of the terms to improve data analysis (Chen, 2006; Gibert et al., 2010; Al-Hassan et al., 2013). Several approaches can be found in the literature, such as fuzzy sets (Zadeh, 1975; Martínez et al., 2009) and the Bayesian model (García-Alonso et al., 2013).

To date, clustering techniques applied to crisp heterogeneous data matrices have not considered the semantics of the terms. This is currently widely accepted, probably due to the lack of proper tools for representing and managing conceptual values together with their semantics. However, AI provides some well-developed tools, which may be of interest when it comes to improving clustering performance by considering semantics.

In the approach presented in this paper (Section 3), we make the most of ontology-based semantic techniques. Ontologies are a knowledge representation model that enables relationships between concepts to be expressed under the logic paradigm (Gómez-Pérez et al., 2004). They are a suitable model for expressing semantics because they are highly flexible and provide sufficient expressiveness for the purpose of this work. This avoids the need for quantitative models for expertise and domain knowledge, indirect measurements through indicators that must be previously validated, direct expert-based quantification of similarities between terms, the definition of membership functions for fuzzy sets and the definition of a priori probability distributions, as in more classic models.

The authors are not aware of other clustering algorithms using ontologies for segmentation purposes. Ontology-based data mining methods have been proposed for other tasks, such as classification (Bernstein et al., 2005; Ceccaroni et al, 2004; García et al, 2011; Moreno et al. 2014; Moreno et al., 2015, Zucon et al, 2013), rule-based decision systems (Esposito and De Pietro, 2011; Zhang et al, 2002), neural networks (Breen et al, 2002; Trappey et al., 2013), Bayesian causal networks (Helsper and van der Gaag, 2002) and even case-based reasoning (Yang et al., 2005). It is worth highlighting the increasing interest in ontology-based analysis for text mining and document classification (Steyvers et al., 2001; Hotho et al., 2003; Thangamani and Thangaraj, 2010; Song et al., 2011; Gu et al., 2009; Vadivelou and Ilavarsan, 2014). Some works combine word interpretation with some structural information, such as blog articles (Feng et al., 2011) and lexicons (Pluempitiwiriyaweja and Cerconeb, 2009).

Most of these approaches (Vadivelou and Ilavarsan, 2014; Steyvers et al., 2001; Hotho et al., 2003; Thangamani and Thangaraj, 2010; Song et al., 2011) do not use classic two-dimensional data matrices, in which objects are described by several variables, as in the approach presented in this paper.

Our approach uses data matrices with the individuals (tourists in the application presented here) in rows and the variables in columns. The columns can be heterogeneous, including numerical and qualitative variables (where the values are words), some with multiple responses. A generalization of Ward’s method is proposed. The calculation of distances is refined using the semantics of the terms for those qualitative variables for which semantic information is available in the reference ontology. Pre-processing methods (Gibert et al., 2017) are used to appropriately transform the multiple responses to be introduced into the clustering with no loss of relevant information. Sections 3.3 and 3.4 provide details on how ontologies are introduced into the clustering algorithm to better measure similarities between objects.

## 3. Materials and methods

## 3.1 Methodological framework

The methodology used in this paper to find tourist segments according to their decision to visit a certain tourist destination provides several contributions with regard to the traditional procedure for analysing tourists’ answers to questionnaires:

1. From the tourism analysis point of view:

a. The operationalisation of the push and pull factors through motivation and meaning,

b. The use of qualitative open-ended questions to measure tourists motivations and meanings.

2. From the computational analysis point of view:

a. The use of reference ontologies to obtain semantic information about the terms used by users in the open-ended questions,

b. The use of semantic clustering techniques to perform multivariate analysis of tourists taking into account both the qualitative answers and other variables to provide a semantically interpretable tourist segmentation.

The main novelty resides in introducing the meaning of the destination as a pull factor instead of the perceived image of the destination. As previously stated, the second of these options has the greater presence in the related literature, probably for two main reasons: the scarcity of data measuring meaning directly from the tourists’ spontaneous responses and the difficulties in analysing it using conventional statistical systems. In addition to this, the contribution is supported by the idea that meaning represents a variable that concentrates greater decision-making influence in the destination selection process.

An additional contribution of this work consists of obtaining motivation and meaning from open and free responses, in which the vocabulary considered by users finds no constraint other than their own terminological ability instead of using the closed and preconceived lists of terms classically used for qualitative variables in Statistics and Artificial intelligence. Thus, in the approach presented here, the tourist can use any word they consider appropriate to indicate the motivation and meaning of a destination.

The study is thereby not reduced to a limited range of pre-established motivations or fixed meanings, which, even when including the classic “other(s), please specify” option common in closed questions today, might bias the expression of the user. Indeed, the simple vision of the terms suggested in the closed lists can even limit the free association of ideas with the destination. The authors in fact point out that this might be precisely the reason why the classic formulation on closed lists has brought about little advancement in improving knowledge of the destination selection process beyond what it is already known in the sector. The proposed approach goes beyond the inherent restrictions of questions with predefined lists of responses and those deriving from the use of indirect measures through scales or indicators (whose validity is widely controversial in most fields, including psychometrics, market research, etc.).

Finally, another innovation of our method consists of allowing respondents to give more than one answer to the questions. The use of such a multiple response open-ended question is also a new field that has not been explored in tourism, as far as we know.

The proposed model for tourism formalisation, including open qualitative variables for obtaining the meaning and motivation of the destination, requires the most up-to-date generation analysis tools that go beyond the econometric models traditionally used in this area. Ontology-based clustering (Batet et al., 2010) is proposed as a means to segment tourists according to motivation and meaning expressed through open, unrestricted vocabulary. This methodology represents a step forward in the analysis of data containing qualitative information because:

 it enables the simultaneous analysis of numerical, categorical and semantic data

 semantics is expressed through ontologies

 the sense of the terms is considered so as to compare tourists’ answers

 multi-valued open questions are processed for intelligent analysis.

The main consequence of taking into account the semantics of the terms used is that the resulting clusters are more compact and consistent from a conceptual point of view and are therefore more easily understandable by the end user, in this case the tourism professional (Gibert et al., 2014; Gibert and Conti 2014; Moreno et al., 2015).

Thus, the proposed methodological framework materialises the link between the ontology and the classifier through the introduction of an appropriate distance between individuals (in this case tourists), as will be seen in the following sections.

## 3.2. Ontology-based clustering

The CbO method (Batet et al., 2010) is an extension of the classic hierarchical agglomerative clustering algorithms (Jain et al., 1999; Bouguettaya et al, 2015), in which a nested set of classes is constructed in a bottom-up approach by merging a pair of objects or classes at each step. Two basic parameters guide the procedure, giving rise to different clustering algorithms:

 An aggregation criterion to prioritise which pair of classes or individuals are to be merged at each iteration

 The function used to measure distances between pairs of objects. When dealing with different types of variables, this distance function must have particular characteristics (discussed in the following sections).

CbO is an ascendant hierarchical method based on a classical baseline of the reciprocal neighbours algorithm (deRham, 1980). For an aggregation criterion, it uses Ward’s criterion (Ward, 1963). This method first merges the pairs, with minimisation of the loss of interclass inertia being its main criterion because inertia is a function of the squared Euclidean distance between the terms compared. As an underlying distance, it uses a Generalized Gibert’s mixed metrics (GGMM) (described in Section 3.3), which makes it possible to cluster individuals described by numerical, categorical and semantic variables simultaneously while taking into account the semantics of the terms, when available, in the comparisons. To be more precise, our proposal uses a generalisation of

Ward’s criterion that in the classical expression substitutes the classical Euclidean distance with a GGMM.

This clustering method has been implemented in a software system called KLASS (Gibert and Nonell, 2008), which was used for the study presented in this paper.

## 3.3. Generalized Gibert’s mixed metrics

Given the structure of the problem to be dealt with in this research, a means of comparing two individuals described by numerical, categorical and semantic variables simultaneously is required. The literature is rich in semantic distances (Pedersen et al., 2007; Lee et al., 2008). There are also proposals for comparing objects with numerical and categorical attributes, such as those made by Gower (1971) and Ichino and Yaguchi (1994). The authors are not aware of any proposals in the literature that allow comparisons in a general case that includes all the numerical, categorical and semantic variables together, except for the GGMM previously developed by the authors themselves (Gibert et al., 2014). Ontology-based clustering CbO, therefore, uses GGMM as the underlying distance of the algorithm.

Although categorical variables are the classical representation for qualitative variables, those for which additional background knowledge is available to help interpret the semantics of the terms are known as semantic variables, the meaning of their values can be interpreted and become concepts rather than simple modalities. In our approach, the background knowledge providing this additional semantics will be formalised by means of ontologies.

GGMM is a compatibility measure that combines different distances according to the type of variable. It has been shown to perform well in other applications related to clustering tasks.

Given a set ${ \mathcal { W } } \mathbf { = } \{ \ X \boldsymbol { k } , \boldsymbol { k } = 1 : K \ \}$ of variables of three different types $\zeta = \{ k : X _ { k }$ numerical variable, $k = 1 : K \} , \ Q = \{ k : X _ { k }$ categorical variable, $k = 1 : K \} , \mathcal { S } = \{ k : X _ { k }$ semantic variable, $k = 1 : K \}$ , such that $\mathcal { U } { = } \zeta \cup \mathcal { Q } \cup \mathcal { S } ,$ , the GGMM is defined as follows:

$$
d _ {(\alpha , R, \nu)} ^ {2} (i, i ^ {\prime}) = \alpha d _ {r} ^ {2} (i, i ^ {\prime}) + \beta d _ {0} ^ {2} (i, i ^ {\prime}) + \gamma d _ {s} ^ {2} (i, i ^ {\prime}), (\alpha , \beta , \gamma) \in [ 0, 1 ] ^ {3}, \alpha + \beta + \gamma = 1\tag{2}
$$

, where:

$d _ { 7 } ^ { 2 } ( i , i ^ { \prime } )$ the normalised Euclidean metrics used with numerical variables

$d _ { o } ^ { 2 } ( i , i ^ { \prime } )$ is the $\chi ^ { 2 }$ metrics to be computed with the categorical variable (see Gibert and Cortés, 1997) and

$d _ { \mathscr { s } } ^ { 2 } ( i , i ^ { \prime } )$ is the superconcept-based distance (SCD) to be used for semantic variables (see Section 3.4 and Gibert et al., 2014).

The GGMM is, in fact, a family of metrics indexed by three parameters $d _ { ( \infty , R , v ) } ^ { 2 } ( i , i ^ { \prime } )$ In Gibert Cortés (1997), it is shown that the weights given below provide good results associated with clustering processes:

$$
\alpha = \frac {a}{\cdots} a n d \beta = \frac {o}{\cdots} a n d \gamma = \frac {c}{\cdots}\tag{3}
$$

where

$$
a = \frac {n _ {\zeta}}{, 2} a n d b = \frac {n _ {0}}{, 2} a n d c = \frac {n _ {\delta}}{, 2}\tag{4}
$$

with $n _ { \zeta } = c a r d ( \zeta ) , n _ { \ O } = c a r d ( Q )$ and $n _ { s } = c a r d ( \mathcal { S } )$ , while $d _ { \tilde { \tau } \ m a x * } ^ { 2 } , \ d _ { 0 \ m a x * } ^ { 2 }$ and $d _ { \mathcal { S } m a x } ^ { 2 } .$ are the truncated maximums of the different subdistances. They balance the contribution of all types of variable in the final distance and provide robustness in the presence of outliers.

## 3.4 SuperConcept-based Distance

The SuperConcept-based Distance (SCD) enables comparisons to be made between two terms of a qualitative variable for which semantics is available. Hence, it would be expected to give a lower distance between church and cathedral than between church and theatre or restaurant. A common approach in the literature is to use ontologies to express relationships between terms and to define semantic distances between terms that exploit the ontology’s geometry. Most of these are based on the minimum path between the terms compared (Pedersen et al., 2007) and thereby lose considerable valuable information. Therefore, the ontology-based clustering presented in Section 3.2 uses a recent proposal made by the authors (Gibert et al., 2014)—the SCD—as the third component in the GGMM, $d _ { \mathscr { s } } ^ { 2 } ( i , i ^ { \prime } )$ . This distance is based on the existence of a reference ontology, in which the terms of the semantic variables appear and which is able to provide more accurate distances between terms taking into account all the taxonomic evidence available (i.e., all the superconcepts) and not only the minimum path.

Given a set of concepts $C ,$ an ontology $H ^ { C }$ containing a set of taxonomies over the elements in $C ,$ and a concept $c _ { i } \in H ^ { C }$ , we consider the set of super-concepts (ancestors in the taxonomy) of $c _ { i }$ as the subset of all the concepts in $C$ preceding c<sub>i</sub> in some of the taxonomies of $H ^ { C } .$ , including $c _ { i }$ itself:

$A ( c _ { i } ) = c _ { j } \in C$ such that $c _ { j } = c _ { i } \vee c _ { j }$ is the ancestor or super-concept of $c _ { i }$ , $\forall c _ { i } \in H ^ { C }$

Concepts $c _ { i }$ and $c _ { j }$ are compared on the basis of the ratio between the non-overlapping taxonomic knowledge and the total number of ancestors of both terms.

Definition 1. SuperConcept-based distance (SCD)

$$
S C D \left(c _ {i}, c _ {j}\right) = \sqrt {\frac {\operatorname{card} \left\{\mathrm{A} \left(c _ {i}\right) \cup \mathrm{A} \left(c _ {j}\right) \right\} - \operatorname{card} \left\{\mathrm{A} \left(c _ {i}\right) \cap \mathrm{A} \left(c _ {j}\right) \right\}}{\operatorname{card} \left\{\mathrm{A} \left(c _ {i}\right) \cup \mathrm{A} \left(c _ {j}\right) \right\}}}\tag{1}
$$

SCD fulfils the properties of a metric (i.e. positivity, symmetry and triangular inequality), which enables its use in hierarchical clustering algorithms (Gibert et al., 2014; Batet et al., 2010) as it is equivalent to computing the Euclidean distance between the binary vectors resulting in a flattening of the ontology in a vector of terms and a description of a concept as its path towards the root.

## 3.5 The reference ontology

As mentioned earlier, a reference ontology is used by the SCD to improve comparisons between the terms used in semantic variables. In turn, the SCD becomes a component of the GGMM to permit global distances to be calculated between pairs of individuals partially described by numerical, categorical and semantic variables. This is the distance used by ontology-based clustering to find segments of individuals in this research. Thus, in this section, the characteristics of the reference ontology used here are presented.

#

Ontologies formalise and represent domain knowledge (Gómez-Pérez et al., 2004), providing a graphic model in which semantic interrelations are modelled as links between concepts. They are highly flexible and provide sufficient expressiveness for our purposes. Research into the structure of existing ontologies through the Swoogle ontology search engine (Ding et al., 2004) has shown that domain ontologies usually model only taxonomic relationships. Although the proposed methodology is general for any reference ontology, in this work, WordNet (Fellbaum 1998) is used as it is a general purpose ontology commonly used for semantic analysis with the English language. In other domains, specific ontologies (like SNOMED in medicine) of reduced terminology might also be used with the same methodology. WordNet offers a lexicon, a thesaurus and semantic linkage between a large number of English terms. WordNet contains around 120,000 nouns and 11,500 verbs. Hypernymy is by far the most common relation, accounting for over 80% of all the semantic links modelled. The maximum depth of the noun hierarchy is 16 nodes. WordNet is a general purpose ontology that provides a sound background for any application.

Topics related through the management of semantics are language-dependent most of the time. In the case of non-English applications, terms can be previously translated into English and WordNet kept as the reference ontology or any ontology originally designed in the native language might also be used if available. In the case of descriptions of motivation and meaning, it is best to avoid translating the terms used by the tourists, as several authors point out the biases that translations can introduce in this particular, given that different languages have different words to describe landscapes and emotions according to different values, interests and goals that are characteristic of the different cultures (Picard and Robinson 2012). EuroWordNet is a general-purpose multilingual ontology that includes seven languages that might be considered for applications: Spanish (Vossen, 1999), French, Italian, Dutch, German, Czech and Estonian.

## 3.6 Dealing with multivalued semantic variables

One of the characteristics of this research is that the open-ended questions allow the tourist to provide more than one word for the both the reason and meaning questions. This not only produces a richer view of the tourist but also makes the structure of the

#

problem more complex, since the data matrix contains cells with values which are no longer single words (with or without semantics associated) but vectors of words, known as multivalued variables. There are a number of different solutions available. One way would be to pre-process the data by identifying the most frequent lists of words used by the tourists and substitute them with a more global concept that represents the complete list (e.g. sand, sunbathe, sun… would be substituted by beach). This can be done by hand, provided that the lists of combinations are not long, but it can also be done by using the reference ontology, automatically determining the Least Common Subsumer. Another way would be to analyse the distribution of the number of words given in each response and determine the length of lists covering more than a certain threshold of individuals, and then using as many columns for the variable as determined. For example, in our application, over 90% of the respondents only used one word, thus only one variable has been used. Should a relevant percentage provide a second word, two columns for the meaning could be considered in the analysis as the main meaning and secondary meaning. In the first approach, the order in which the words are spoken is dismissed. For those contexts in which the order of the words becomes important, the second approach might be more suitable.

## 3.7. Obtaining segmentation using a hierarchical method

The result of a hierarchical method is a dendrogram (see Fig. 2) with the sequence of nested classes built throughout the process. The leaves are the original individuals (in our case, the tourists). The internal nodes represent the intermediate classes created. The level of an internal node is proportional to the class’s homogeneity. The dendrogram provides a visualisation of the inner structure of the dataset, which can be analysed a posteriori, and the number of final classes (i.e. segments) determined accordingly, contrary to what happens in partitioning clustering methods such as K-means, where the number of classes to be found is an input parameter (Aparna and Nair, 2015). This is a major advantage of hierarchical methods over partitioning methods, since in the general case the number of interesting and relevant tourist segments is not known in advance and has to be discovered during the data mining process.

The suggested number of classes is usually identified in the dendrogram as the horizontal cut with the longest branches. This often coincides with the optimisation of certain quality indexes such as the indexes of Calinski–Harabasz (Calinski and Harabasz, 1974) or the Davies–Bouldin (Davies and Bouldin, 1979). In this paper, the Calinski–Harabasz criterion is used. Each horizontal cut of the tree generates a partition with a number k of clusters, k ϵ {2:n}. The Calinski–Harabasz index is evaluated at every horizontal cut $C H _ { k }$ . The best cluster is the one maximising the Calinski– Harabasz index. For a given number of classes $k ,$ it is computed as:

$$
C H _ {k} = \frac {B _ {k} / (k - 1)}{W _ {k} / (n - k)}
$$

, where n is the sample size, $k$ is the number of clusters, $W ( k )$ is the within-cluster variability and $B ( k )$ is the between-cluster variability. The Calinski–Harabasz index is higher as the clusters are more compact and distinguishable from each other. Therefore, it is considered that the best clustering among all those suggested by a dendrogram is the one that maximises the Calinski–Harabasz index.

## 3.8. Interpretation-oriented post-processing tools

In the area of data mining, much of the research in the last decade has focused on the development of better and quicker algorithms to capture the underlying structure of the dataset analysed, covering the data exploitation step itself. However, the other steps in the knowledge-discovery process are of considerable importance for the completion of the process (Fayyad et al., 1996). One of the most critical issues for the real impact of data mining results on the target domain is to consider a post-processing step oriented at the understandability of those results (Gibert and Conti, 2014). The current gap between data mining results and effective decision-making has been argued in previous works (Gibert et al., 2013), and several tools have been developed to post-process clustering results to understand the clusters. These include annotated Traffic Lights Panels (Gibert and Conti, 2015), Class Panel Graphs (CPGs) (Gibert et al., 2008), or direct concept induction from dendrograms (Gibert, 2014). In this paper, CPGs are used to understand the meaning of the clusters (see Fig. 3).

#

The CPG is actually a way of identifying relevant variables in the classes based on a compact visualisation of the conditional distributions of many variables on a single page, thus providing an overall perspective of the behaviours of variables in classes.

## 3.9. Data collection and sampling

To apply the proposed methodology to ascertain the role of push–pull factors in tourists decision-making, empirical research into the motivations and meanings of British tourists on holiday was conducted in the province of Tarragona, a Spanish coastal tourist region in Southern Catalonia with two main regional tourism brands (Costa Daurada and Terres de l’Ebre) and many local tourism destinations. The study focused on the British tourist market for two main reasons. First, English is the language most studied in Computational Linguistics research, and therefore large, detailed ontologies for general purposes (like WordNet) already exist in the language. Second, the British market has a long tradition and a large magnitude in this particular region of Spain (Sanz Ibáñez and Anton Clavé, 2016). Additionally, because of its numerical relevance, focusing on the British visitor market also facilitates the design of a focused analysis of the utmost interest to destination managers in the area.

## 3.9.1 Survey instrument

Since 2001, the Costa Daurada Tourism Observatory has conducted a regular omnibus survey of tourists who visit the region and its main local destinations. This omnibus survey is the major existing data gathering tool providing information about the characteristics and profiles of tourists travelling to the Costa Daurada and the Terres de l’Ebre. The survey measures socio-demographic characteristics, types of trip and tourist perceptions and contains a set of questions aimed at ascertaining the reasons for choosing any single local destination in the region. This is the concept on which this work focuses.

The questionnaire, which is implemented by means of a direct survey of tourists, is structured in accordance with the following groups of questions:

1. Characteristics of visitors by age, origin, social class, level of studies and activity profile of the person who provides the main source of the household’s economic income.

2. Characteristics of the stay and motivations for travelling to the destination.

3. Activities performed by visitors in the destination and the places visited or planned to be visited during the stay, among other things.

4. Satisfaction related to several issues and the features of the tourism destination.

The two key questions for the analysis undertaken in this paper are two open-ended short answer questions, spontaneous and multiple, that are located in Sections 2 and 4 of the questionnaire described above. If more than one response is given, interviewees are asked to rank them from most to least important. Using open-ended questions instead of categorical choices, the questionnaire solves the problem of any anchoring effect. The questions are formulated as follows:

 What is/are the reason(s) behind this destination choice of yours to spend your holidays?

 Could you tell me, with the first word that comes to mind, what this place means to you?

The way the questions are formulated may be taken into account when interpreting the results of the analysis.

## 3.9.2. Sampling

The sample consists of 460 British tourists over 15 years old who visited any Costa Daurada and Terres de l’Ebre local destination during the summer of 2011. The survey was conducted from April to September 2011. Only 20 of the 480 British tourists contacted refused to participate, resulting in a response rate of 95%.

As regards the sampling technique applied, the survey was conducted on a sample of visitors selected using a multi-stage sampling procedure. This procedure was established to guarantee statistical representativeness. Since the survey is implemented in open public spaces distributed throughout the many local destinations where tourists take holidays, a key aspect of the sampling process is the selection of the individuals to interview and the definition of the points of interaction with them.

The first stage of the sampling design consists of determining the points of the survey and their area of influence. On the basis of the expertise of a committee of experts on tourist activities in the area, a set of 16 key survey points covering the most visited local destinations and all the varied typology of the tourists was selected. The committee of experts comprised a geographer, two market research analysts, the directors of the local destination management organisations involved in the study and a representative from the hotel association. These points were subsequently validated by means of field observation performed by members of the research team. The first sampling stage determines the geographical coverage of the sample, guaranteeing the possibility that a visitor may be interviewed independently of where their accommodation is located.

The second stage is the configuration of the survey fieldwork as regards both time and geography. This means determining in which places the survey will be activated, and on which days and at what time. The final sample contained all the time slots and all the places selected during both weekends and workdays. The survey was implemented from 9 a.m. to 9 p.m. This second stage guarantees the possibility of selecting tourists that are out of their accommodation only during the morning or only during the afternoon/evening. It also ensures that the selection will randomly include both weekend tourists and tourists that are in the destination only during the other days of the week.

The third stage consisted of a systematic sampling selection of the individuals to interview. They were chosen from the flow on the basis of ‘1 group or individual from every 3 groups or individuals’ among tourists walking to the point of the survey, taking into account the whole section of promenade or equivalent previously determined by the research director. When a group was selected, the member interviewed was whichever individual in the group over 15 years old would soonest reach their birthday. The random selection of the individual to answer the questionnaire guarantees the selection of people of all age groups, genders and origins.

#

In the case of areas in the province of Tarragona with lower numbers of visitors, the tourists were interviewed in the reception area of their accommodation. In this case, the first stage was to select those places with available tourist accommodation and then randomly select the destinations to be part of the sample. This ensures that all accommodation facilities chosen by tourists will have an equal probability of being in the sample. The second stage was to assign the days to carry out the survey during both weekends and weekdays. This made it possible to select not only tourists who visited the place during the weekend but also tourists who visited it on weekdays. Interviews were conducted in the morning from breakfast until the end of check-out time. Mornings are the part of the day with the highest probability of finding all the people hosted at a particular place of accommodation. To choose the person to be interviewed, the same procedure of random selection as above was applied.

The questionnaire was implemented in open spaces in the case of the most important tourism destinations and in accommodation establishments in the case of destinations with fewer visitors. Since accuracy is important, an experienced interviewer conducted the questionnaire to ensure that the respondent was answering it seriously. Although when asked to participate in the survey, people are going about their own business, it should be noted that the selected individuals need to collaborate properly during the interview process. As they are on holiday, they have enough time to spend answering the questionnaire, and therefore the time used to answer it and how this could affect the quality of the responses is not a concern in the case of this survey. Usually the individuals participating in the survey took approximately 7 minutes to answer the questionnaire. Questions about motivations and meanings are to be found during the second minute of the interview. The answer is totally spontaneous and not directed. The interviewer notes down verbatim the exact expression used by the respondent. The proportion of no answers to these two specific questions is almost zero. Uncompleted questionnaires or cases in which the respondent did not behave normally are not included in the sample.

#

## 4. Results

In this section, we first explain in detail the processes for preparing data for the analysis and the subsequent application of the clustering algorithm. The segments obtained are then identified and described.

## 4.1. Data selection and preparation

This study aims to understand the reasons why British tourists decide to go to a particular local destination within the Costa Daurada and Terres de l’Ebre regions. A tourist segmentation will be carried out taking into account both the location of the tourist and the Push–Pull factors explained earlier (for a detailed analysis of the projected and perceived image of Spain as a tourism destination for British travellers, see Andre, Bigné and Cooper, 2001). The analysis may help discover whether there is any relationship between the specific destination chosen, the tourists’ motivations and their meanings so as to identify several profiles of tourists according to this relationship. Four variables were therefore selected and prepared using the information provided from the corresponding survey questions.

In an initial stage, some preliminary data preparation was done when required. The main characteristics and processing of the four variables in this study are summarised below:

 Place: this variable refers to where the interview was held. There are 28 different locations on the Costa Daurada and in the Terres de l’Ebre, including those in the capital city, Tarragona, coastal tourism destinations such as Salou, Cambrils and La Pineda and other small towns within the province of Tarragona.

 Zone: the geographical area of the province is divided into nine different zones: North, Tarragona, La Pineda, Salou, Cambrils, Terres de l’Ebre, inland Costa Daurada, other Central areas and South. The areas of Tarragona, Cambrils, Salou and La Pineda account for 87% of the interviews. This is because they are the most tourist-oriented places in the province.

 Motivation-Reason (push factor): this variable contains the textual answers given by the tourists to question Q1. People were allowed to answer with a

#

maximum of three words. Each word should correspond to a different motive for their visit. All answers were in English. To interpret their meaning using the WordNet ontology, the words used in the answers have to appear in WordNet. Minimal changes were made to preserve the original answers as much as possible. The first transformation is to change adjectives and verbs into nouns (for instance, Enjoy is changed to Enjoyment). Second, some specific names or expressions were changed to the most similar and general concept (for instance, PortAventura, which is the name of an amusement park, is changed to Entertainment; Gaudí is changed to Culture (see Table 1)). Most of the tourists gave just one answer, so in the end only the first word has been considered in this study. There are 43 different motivationsreasons, but only 10 motivations are given by more than 5 respondents. Hence, there are 33 answers that are rather infrequent, but they may include words indicating quite similar motivations, for example, heritage and history, beauty and niceness, museum and culture. These semantic relations are then exploited by the clustering method to correctly identify these similar reasons to construct the segments.

 Meaning (pull factor): this variable contains the textual answers given by the tourists to question Q2. People were allowed to answer with a maximum of three words. Each word should correspond to a different motive for their visit. All answers were in English. The same recoding procedure was applied to ensure that all the answers appear in the WordNet ontology. Some minimal changes were made to preserve the original answers as far as possible (see Table 2). In this variable, only 1.8% of respondents used two words to indicate the meaning of the place, while the rest gave a one-word answer. The answers were much more diverse than with motivations, with 69 different words. The most frequent meaning is Goodness (15% of the tourists), whereas Holiday, Beach, Sun, Niceness and Relaxation have a frequency of approximately 8–10%.

#

## 4.2. Semantic clustering

Clustering based on Ontologies (CbO) is performed on these data with the following parameters:

 Aggregation method: Ward criterion (Ward, 1963)

Distance: Gibert Generalized Mixed Metrics (Gibert et al., 2014), with α=0 as no numerical variables are used in this particular application, and β and γ as suggested in eq. 3

 Categorical variables: Place and Zone

 Semantic variables: Motivation-Reason and Meaning

 Ontology: WordNet

The execution of the CbO method with this configuration led to the dendrogram shown in Fig. 1. At a higher level, we can see two classes: C457 and C454. Then, for a 3-class cut, C457 is divided into C456 and C455 and so on. To obtain a partition of the individuals into a set of non-overlapping clusters, a horizontal cut at a certain level of the dendrogram must be made. Following the classic Calinski–Harabaz criterion (see Section 3.7 for details), the cut level has been established at the point indicated in Fig. 1, giving a partition into six classes.

Figure 2 shows the number of tourists belonging to each segment (n<sub>c</sub>) and the CPG for those six segments. Two classes can be observed with approximately 150 tourists, three classes with 40–50 individuals and another with 27. Because of the high number of values given in some of the variables, it is impossible to show the names of all the terms on the X-axis of the bar charts. Some of them were therefore deleted for the sake of clarity. The CPG clearly shows different distributions of values in each of the segments, which indicates that they represent different tourist profiles. In particular, differences in the push–pull factors through different segments can be analysed. The Reason (or motivation) dubbed ‘Holiday’ displays a high frequency in four of the segments. However, this main reason is found in combination with other different concepts in each segment. Meanwhile, Meaning is different in all segments, with three clear values that appear exclusively in three different classes.

The information provided by the distribution of the values in each class has been used to extract a definition for each of the segments. In this definition, the geographic information provided by the variables ‘Place’ and ‘Area’ have also been included so as to facilitate the subsequent analysis of the territorial distribution of the different British tourist profiles. For a better understanding, the places were classified according to the type of places they are: iconic city sites, central places in the city, beaches with a unique landscape, inland regions and quiet places in natural surroundings.

 C453 Visiting. Group of 151 people whose fundamental push factor is accessing culture, sightseeing and shopping. These are people who travel to go to museums, see the sights and get to know places. The pull factor that leads to the place is the sense that it is associated with achievable culture and wellness and considered to be a suitable place for tourism. All the tourists who have come to the destination to visit family and friends are in this segment.

This group differs from the others because it largely corresponds to tourists coming to Tarragona city, mainly interviewed at an iconic place located within the city, although it should be noted that tourists surveyed in inland places are also located in this segment. The segment also includes tourists surveyed in quiet southern areas of natural environment, although in lower proportions than in the “Enjoying” class. Some tourists with this profile are distributed without too much incidence among the different locations of Salou (18 persons), La Pineda (14 people) and Cambrils (13 people), with those surveyed in an iconic place of La Pineda and an iconic place of Cambrils being a group of only secondary importance.

C455. Enjoying. Group of 149 people who conjure up a single push factor which is holidays, with the main pull factor for reaching this destination being the goodness and niceness of the place, although this group also includes those who valued relaxation and the possibilities of entertainment offered by the PortAventura theme park. A significant proportion of these tourists were interviewed in Salou, La Pineda and Cambrils, with a particular presence of those who were interviewed in the iconic place of La Pineda and at its spot point and at the iconic places and spot points of Salou and Cambrils. It can also be observed that this segment contains a certain number of tourists who have chosen inland areas and Tarragona city, although this is not the main class of visitor to these areas.

 C446. Holidaying. Group of 52 people whose push factor is to choose a beach holiday destination. The pull factor, which attracts to the destination of choice and not to another, is the fact of considering it their ‘holiday destination’. The sense of place is clearly associated with their holidays. These tourists were mainly surveyed in the area of Salou and La Pineda, and the biggest group was interviewed on unique beaches in Salou, with a notable incidence of interviews also occurring in Cambrils, both at its iconic place and in a central point.

 C449. Beaching. Group of 42 people whose push factor is to take a beach holiday. The pull factor that leads them to choose the destination is the beach. These are tourists that are centrally motivated by the beach and who therefore choose the destination because of the characteristics of its beaches. They are mostly found in Salou, mainly in the central points of the town and then at the iconic place and another central point of La Pineda. Some isolated tourists aligned with this profile might also be found outside these areas, but only exceptionally.

 C438. Sunbathing. Group of 39 people whose push factors are mainly holidays and the beach and whose pull factor is the sun. Basically, this territory evokes in them the sun. They are found in central parts of Salou and on one of its unique beaches, although also on the beaches of La Pineda, in the iconic place of La Pineda and in smaller groups throughout all locations. There is a certain incidence of this segment among interviewees in Tarragona and marginally in the quiet southern areas of natural environment.

 C414. Relaxing. Very homogeneous group of 27 people for whom the main motivation or push factor is the beach. They differ from the previous groups in that the meaning of the destination is associated with the beauty of the place and the landscape, wellness and relaxation. This result hints at a conception of the beach in the sense of its being a natural element. In general, they are located primarily in a central point of Salou and at an iconic place of La Pineda, but they tend to be more numerous on the unique beaches. Outside Salou and La Pineda, only a small proportion of this profile is observed at an iconic place of Cambrils and very marginally in the quiet southern areas of natural environment.

#

The following table summarises the push and pull factors of each segment and their location in the different tourist zones of the area studied.

## 5. Discussion

The results show the existence of clearly different profiles of tourists coming from Britain to different local destinations in the region of the Costa Daurada and the Terres de l’Ebre according to their motivations and the meaning they give to their selected destination. Identifying different types of tourists following this Push–Pull model opens up an opportunity to better understand the reasons behind the tourist destination selection process and, from a practitioner perspective, a chance to design new marketing strategies. Some important findings of general interest for other Mediterranean coastal tourism destinations are the following:

 Sun and sand appear separately as pull factors and not together as a single concept. One observed meaning of the destination is based exclusively on the beach concept and a different one is based on sunbathing, though these are two concepts that are traditionally considered together by the tourism literature. The results show that they can operate as two different pull factors to a destination.

 Not all the tourists for whom Beach is their main push factor have the same types of interests. Out of 128 tourists for whom Beach is a push factor, only 40% are mainly attracted by Beach as the main pull factor, whereas the rest are found in two other segments with different views. Another group of approximately 40% of these tourists associates the destination with the concept of Holidays, which is much broader than the concept of Beach. Finally, a group of 20% of the tourists chose this destination for the beauty of the place, the niceness and good feeling and for the image of relaxation that the destination offers them.

 There is a set of British tourists whose motivation is basically the Sun but linked to Holidays rather than Beach. Although the concept of Beach in the

#

previous segments probably also implicitly includes the concept of Sun, this is not the meaning that popped into the tourists’ minds when answering the questionnaire. Therefore, it is important for both academics and decisionmakers to know that destinations with sun but without beach also have a segment of British tourists who would potentially be interested in visiting this kind of place. This would apply to several inland towns in the area of the Costa Daurada and the Terres de l’Ebre.

 Finally, a segment of British tourists that is not associated with either beach or sun has also been identified. They mainly chose this destination for its cultural heritage, shopping and the other kinds of tourism activities available. It is worth noting that this is the predominant profile in the capital city of Tarragona.

## 6. Comparison with traditional approaches

The same dataset has been analysed using some traditional approaches to evaluate the performance of our solution. We have focused on clustering methods that require no previous hypothesis about the number of existing clusters (as happens with some partitioning algorithms like C-means) because we do not want to introduce this constraint into the model a priori.

Being the partition P our proposal (obtained by using the Ward’s hierarchical method with the GGMM and optimizing the Calinski–Harabaz index to determine the number of clusters over de resulting dendrogram), another seven approaches have been used to compare the results. Ward’s method has also been used with other metrics that do not take into account the semantic conditions of the variables Meaning and Motivation (e.g. Chi-squared and Hamming, both assuming all variables are categorical). For the case using Chi-squared, two possible cut levels appear on the dendrogram and both were considered. Density-based methods (well known for their capacity to detect clusters of any general shape) are also used. Thus, both OPTICS and DBSCAN are used with the Chi-squared metrics, assuming all variables to be qualitative. Each was also tested with a second metrics: Hamming metrics with OPTICS and DBSCAN with GGMM.

#

Although validation in non-supervised settings is still an open issue, to compare and quantify the goodness of the clusters discovered, we considered 15 indexes available in the literature. They are as follows (+ indicates that the index must be maximised, - indicates that it must be minimised):

 AvBet (+) is the between-clusters average distance.

 AvWit (-) is the within-clusters average distance.

 MaxDiam (-) gives the diameter of the biggest class.

 MinSep (+) gives the minimum separation between clusters.

 wSS (-) is the within-clusters sum of squares.

 AvSilWidth (+) averages the silhouette (Rousseeuw, 1987) of all the elements in each cluster, which quantifies how well an object lies in its cluster.

 G2 (+) corresponds to Goodman and Kruskal’s Gamma coefficient (Gordon, 1999).

 Pearson’s Gamma (+) is a normalised Hubert Gamma coefficient (Halkidi et al., 2002), which correlates the distances between objects with a binary matrix indicating whether two objects are in the same cluster.

 Dunn Index, D (+) attempts to identify compact and well-separated clusters (Halkidi et al., 2002).

 Dunn-like, D2 (+) is a robust generalisation of the Dunn index proposed by Bezdek and Pal (1998), substituting point-to-point distances by average distances in both numerator and denominator.

 Entropy (-) of the distribution of cluster memberships.

 wbRatio (-) is the ratio between the within-average distance and the betweenaverage distance.

 CH (+) is the Calinski–Harabaz index, based on reaching a compromise between both the between-cluster and the within-cluster distances.

 Widest Gap (-) gives the length of the biggest gap inside a cluster.

#

 Sindex (+) measures the Davies–Bouldin Index (Davies and Bouldin, 1979), averaging one index for each cluster, which measures the maximum pairwise comparison involving the cluster and the other clusters in the solution.

These indexes provide several metrics to quantify the structural properties of the clusters, which are indirectly related with the distinguishability of clusters (like AvBet) or with their compactness (like AvWit or wS) or which even sometimes evaluate the relationship between both characteristics (like CH or Dunn). They provide a quantitative reference regarding the structural strength of clusters. However, in the end and on top of structural validity, a further step is always required to verify the meaning and usefulness of the classes obtained (see 3.8).

Finally, we introduce a new index, RankSum, which is the sum of ranks of all the indexes, as a new means of summarising the information provided by them all and enabling the best cluster from all points of view to be identified. In RankSum, the tests were ranked increasingly or decreasingly according to the index interpretation (a higher rank is always assigned to the best partition, and this corresponds to the maximum or minimum value depending on the index, e.g. the higher MinSep the better, whereas the lower widestGap the better). The sum of ranks is maximal if the cluster is the best according to all indexes, which basically means some clusters are more compact and distinguishable than others.

Table 4 shows the values of these validity indexes. Our proposed GG-Ward is among the top positions in most of the indicators. For example, it is the best in the MaxDiam, wSS and widestGap indexes (which indicates that the clusters are compact and without internal gaps); it is the second in MinSep, the Dunn and Dunn2 indexes (which shows that the clusters are also well separated); and it is third in AvBet, avSilWidth, G2, Pearson, CH and Sindex. The score position of our partition is 4 (out of 8) for Entropy and wbRatio.

According to the RankSum value, our proposal is the best solution (scoring 93.5 points), outperforming all the other partitions obtained by a large margin except for the one obtained using the Hamming-Ward-Mode method, which is in second position with a slightly lower score (91 points). Although the final scores are quite similar, once the meaning of the proposed classes in this experiment is analysed, the partition obtained with Hamming is dominated by the Location and Zone variables. It therefore fails in the semantic interpretation of the other variables, mixing tourists with overlapping motivations and meanings in each single clustering, and this does not fit with the aims of the study. In addition, the terms associated with classes are quite generic (only beach, beauty, culture, goodness and holiday show an important presence in the clusters and most of these appear in several classes), providing a result which is good from a structural point of view but not good as a decision support for destination managers.

## 7. Conclusions and future work

This paper shows that, by using semantic data mining methods to analyse the terms used by respondents when answering two open-ended questions related to their motivations for choosing the destination and the personal meaning of the destination, we can go one step forward from the type of results obtained when conventionally grouping tourists according to their characteristics, perceptions or motivations. Using the ontology-based clustering method proposed, it has been possible to identify common structures among groups of travellers and to establish relevant relationships between motivations and meanings that might contribute to a better understanding of the decision-making process followed by tourists and their selection of particular places for their holidays. Undoubtedly, the application of this method to other destinations will also enable the specific reasons for holidaying in a certain place to be obtained. The study validates a new and useful method of analysis for both academics and practitioners. One relevant conclusion of the study is that, if tourists with different motivations decide to go to the same destination, this is because the destination has different meanings for each group of tourists. Thus, having a tool for understanding the relationship between motivations and meanings such as the one introduced in this paper becomes a first step towards a new way of understanding tourists’ decisions that could be implemented in any type of destination.

From a methodological point of view, this study denotes a shift in the way information on tourist demand is usually collected using surveys and analysed using conventional

#

statistical tools. It leads us first to consider the greater importance that qualitative, openended questions must acquire to characterise tourist demand and find out about their decisions. Second, the ontology-based clustering methodology as proposed in this study can take advantage of the existence of reference information regarding the semantics of the terms used to describe the elements to be segmented (in this case the tourists), thereby guiding the classification process. With this method, it is possible to analyse qualitative responses from a semantic point of view by considering an automatic interpretation of what words mean based on the use of a reference ontology that provides a formal framework for describing the conceptual relationships between the words used by the tourists. With ontology-based clustering, the information directly expressed by the user can be analysed, thus avoiding, on the one hand, the use of indirect measures which, even when they can be validated are always controversial, and on the other hand, the need to apply prior transformations to the data for the purposes of analysis, maintaining the analysis within the space of the original variables. In addition, it enables multiple variables of different types to be taken into account, thereby providing a segmentation of the tourists that considers the various factors in a comprehensive manner. Hence, the clusters obtained better represent the distinct segments of tourists, identifying different profiles that can be explained through the semantic information provided by the qualitative variables.

In this particular application, WordNet ontology has been used as the reference ontology because it is standard, free-distributed, available, general purpose and provides support to the English language, which is that used in the questionnaires. Because of introducing the reference ontology into the clustering process, it has also been required for introducing specific means for comparing individuals, able to take into account the reference knowledge provided in the ontology itself. In particular, the SCD can evaluate the semantic proximity between two words, taking into account their conceptual relationship expressed in the reference ontology. Thus, this distance is suitable in the clustering process for evaluating the semantic proximity between the words used by the tourists and for building the clusters accordingly.

From the point of view of the results obtained, important findings also arise. The results show that tourists travelling to the same destination do not form a single and homogeneous group. In the case of the Costa Daurada and Terres de l’Ebre analysis, this can be seen particularly as regards the sun and sea motivation. In fact, although traditional analysis leads us to think that there is a pure tourist who spends their holiday on the beach, which is the main attraction asset for the British tourist in the Costa Daurada and Terres de l’Ebre, the analysis performed shows that in addition to this segment, which does indeed exist, there is another segment looking for a beach holiday whose sense of the place is that the area is their holiday destination, a tourist destination typical of beach holidays. There is yet another segment motivated by the beach but which chooses the destination taking into account its ability to offer relaxation, beautiful landscapes and wellness, where the concept of beach appears as being more attached to its values of wellness and relaxation.

Among British tourists, there is a segment of tourism motivated to spend a holiday in the sun, and that is the main focus of their motivation and of the meaning the destination has for such tourists. We should point out the emergence of beach tourism as being separate from sun tourism. This concept breaks with the usual association of the two words sun and sand. Although the beach will require sun in almost all cases, it is interesting that destinations or areas that have sun but not beach can be made aware that the meaning of sun has a segment of potential demand in itself, at least insofar as the British tourism is concerned. Moreover, a segment appears in the British tourism that is not associated with the beach or coastal destinations per se, but who choose the destination because of its cultural wealth, its shopping, and because it is a tourism destination in itself.

The results also have implications related to the Push–Pull theoretical framework. It certainly appears useful and appropriate to have destination meaning values as pull factors. This is a framework that, when used as proposed in this paper, allows a complex understanding of the decision taken by different segments of tourists visiting the same place. Indeed, the pull factor based on the meaning of the destination has proved more useful in defining segments than the push factor itself. In other words, including the meaning of the destination to identify different segments and define the motivation behind the choice of destination has shown that tourists who manifested similar push factors have been understood as being different based on the meaning given to the chosen destination. The study has also shown that semantic data mining allows a much richer analysis because it works with the meaning (semantics) of every response, opening the door to combined studies in which the numerical information associated with a more classical approach can be analysed alongside the information obtained in conceptual terms without losing the richness that an open qualitative response can offer and providing a more integral view of the tourists as a whole.

Finally, the paper has several practical implications for destination managers because it proves that destinations can be segmented on the basis of what they mean to the tourists as places. Destination managers can exploit the tourist segments discovered to improve the effectiveness of their marketing decisions. For example, they can design different advertising campaigns or strategically address messages to any relevant segment by taking into account the reasons that explain the decision-making process of the individuals it comprises. Additionally, the proposed methodology could also be applied to other fields that require working with surveys with open questions and geographical information. Pull and push factors can also be recognised in other domains. Their interpretation will then be different, but the Ontology-based Clustering method could still be a good tool to use to discover interesting profiles.

As a future work, we plan to study other international tourist markets that also have a significant number of visitors to the Costa Daurada and the Terres de l’Ebre. In this case, the language will have to be changed, which means the appropriate ontologies to be used during the clustering process will have to be found. A comparison of the segments identified from different countries would be also interesting to detect the similar and unique factors of each when selecting the destination. This would help the managers of these tourist destinations to devise more appropriate marketing campaigns and define appropriate policies to promote the tourist attractions of the different places involved.

## References

A.A. Al-Hassan, F. Alshameri, E.H. Sibley, A research case study: difficulties and recommendations when using a textual data mining tool, Information & Management, 50, 2013, 540-552.

L. Andreu, E. Bigné, C. Cooper, Projected and perceived image of Spain as a Tourist Destination for British travellers. Journal of Travel & Tourism Marketing, 9 (4), 2001, 47-67.

K. Aparna, M.K. Nair, Comprehensive study and analysis of partitional data clustering techniques. International Journal of Business Analytics, 2(1), 2015, 23-38.

R. Barkhordari, A. Yusof, S.K. Geok, Understanding tourists' motives for visiting Malaysia's national park. Journal of Physical Education and Sport, 4(4), 2014. 599.

M. Batet, A. Valls, K. Gibert, Performance of ontology-based semantic similarities in clustering, Artificial Intelligence and Soft Computing, Lecture Notes in Artificial Intelligence, 6113, 281-288, 2010.

A. Beerli, J.D. Martin, Factors influencing destination image. Annals of tourism research, 31(3), 2004, 657-681.

A. Beh, B.L. Bruyere (2007). Segmentation by visitor motivation in three Kenyan national reserves. Tourism Management, 28(6), 2007, 1464-1471.

A. Bernstein, F. Provost, S. Hill, Toward intelligent assistance for a data mining process: an ontology based approach for cost-sensitive classification. IEEE Transactions on Knowledge Data Engineering, 17(4), 2005, 503–518.

J.C., Bezdek, N.R. Pal, Some new indexes of cluster validity. IEEE Transaction on Systems, Man and Cybernetics, 28(3), 1998, 301-315.

J.E. Bigné, L. Andreu, Emotions in segmentation, an empirial study, Annals of tourism Research, 31(3), 2004, 682-696.

A. Bouguettaya, Q. Yu, X. Liu, X. Zhou, A. Song, Efficient agglomerative hierarchical clustering. Expert Systems with Applications, 42(5), 2015, 2785-2797.

S. Baloglu, A path analytic model of visitation intention involving information sources, socio-psychological motivations, and destination image. Journal of Travel & Tourism Marketing, 8 (3), 2000, 81-90.

P. Bourdieu, La distinction: critique sociale du jugement. Ed. Les Éditions de Minuit, 1979.

C. Breen, L. Khan, A. Ponnusamy, Image classification using neural networks and ontologies, Proceedings of the 13th international workshop on Database and expert systems applications, 2002, pp 98–102.

J.G. Brida, M. Disegna, L. Osti, Segmenting visitors of cultural events by motivation: A sequential non-linear clustering analysis of Italian Christmas Market visitors. Expert Systems with Applications, 39(13), 2012, 11349-11356.

J.G. Brida, M. Disegna, R. Scuderi, Visitors of two types of museums: a segmentation study, Expert Systems with Applications, 40, 2013, 2224-2232.

B. Brown, M. Chalmers, Tourism and mobile technology. In Proceedings ECSCW 2003. pp. 335-354. Springer Netherlands, 2003.

A. Bull, Economics of travel and tourism, Longmans, Green & Co Ltd; 2nd edition, 1995.

T. Calinski, J. Harabasz, A dendrite method for cluster analysis, Communications in Statistics – Theory and Methods, 3(1), 1974, 1-27.

J.M. Castaño Blanco, A. Moreno Sáez, S. García Dauder, A. Crego Díaz, Aproximación psicosocial a la motivación turística: variables implicadas en la elección de Madrid como destino. Estudios turísticos, 158, 2003, 5-42.

L. Ceccaroni L, U. Cortés, M. Sánchez-Marré, Ontowedss: augmenting environmental decision-support systems with ontologies. Environmental Modelling & Software 19(9), 2004, 785–797.

E. Cohen, Toward a sociology of international tourism. Social research, 1972, 164-182.

J. Chang, G. Wall, S.T.T. Chu, Novelty seeking at aboriginal attractions. Annals of Tourism Research, 33(3), 2006, 729-747.

J.S. Chen, Market segmentation by tourists’ sentiments, Annals of Tourism Research, 30(1), 2003, 178-193.

Y-J. Chen, H-C. Chu, Y-M. Chen, C-Y. Chao, Adapting domain ontology for personalized knowledge search and recommendation, Information & Management, 50 , 2013, 285-303.

Z. Chen, From data mining to behaviour mining, International Journal of Information Technology & Decision Making, 5(4), 2006, 703-711.

J.L. Crompton, Motivations for pleasure vacation. Annals of Tourism Research, 6(4), 1979, 408-424.

G. Dann, Anomie, ego-enhancement and tourism. Annals of Tourism Research, 4(4), 1977, 184-194.

G. Dann, Tourist motivation an appraisal. Annals of Tourism Research, 8(2), 1981, 187- 219.

G.M.S. Dann, G.M.S. Why, oh why, oh why, do people travel abroad? In: Prebensen, N.K., Chen, J.S. and Uysal, M.S. (eds.) Creating experience value in tourism. CABi, Oxfordshire, UK, 2014, pp. 48-62

D.L. Davis, D.W. Bouldin, A cluster separation measure, IEEE Transactions on Pattern Analysis and Machine Intelligence, 1(2), 1979, 224-227.

A. Dickinger, L. Lalicic, An analysis of destination brand personality and emotions: A comparison study. Information Technology & Tourism, 15(4), 2016, 317-340.

L. Ding, T. Finin, A. Joshi, R. Pan, R.S. Cost, Y. Peng, O. Reddivari, V. Doshi, J. Sachs, Swoogle. Proceedings of the Thirteenth ACM conference on Information and knowledge management – CIKM, 2004, pp. 652-659.

M. Diana, C. Pronello, Traveler segmentation strategy with nominal variables through correspondence analysis, Transport Policy, 17, 2010, 183-190.

S. Dolnicar, A review of data-driven market segmentation in tourism, Journal of Travel & Tourism Marketing, 12(1), 2002, 1-10.

S. Dolnicar, Tourism market segmentation – a step by step guide, Handbook of Tourism Economics: Analysis, New Applications and Case Study, New Jersey: Worlds Scientific, 2013, 87-105.

S. Dolnicar, B. Grün, Validly measuring destination image in survey studies. Journal of Travel Research, 52(1), 2013, 3-14.

Y. Ekinci, E. Sirakaya-Turk, S. Preciado, Symbolic consumption of tourism destination brands. Journal of Business Research, 66(6), 2013, 711-718.

M. Esposito, G. De Pietro, An ontology-based fuzzy decision support sytem for multiple sclerosis, Engineering Applications of Artificial Intelligence, 24(8), 2011, 1340-1354.

U. Fayyad, G. Piatetsky-Shapiro, P. Smyth, From data mining to knowledge discovery: an overview, Advances in Knowledge Discovery and Data Mining, AAAI/MIT Press, Cambridge, Mass., 1996.

A. Feelders, H. Daniels, M. Holsheimer, Methodological and practical aspects of data mining, Information & Management, 37, 2000, 271-281.

C. Fellbaum, WordNet: An Electronic Lexical Database, Cambridge, MA: MIT Press, 1998.

S. Feng, J. Pang, D. Wang, G, Yu, F. Yang, D. Xu, A novel approach for clustering sentiments in Chinese blogs based on graph similarity, Computers and Mathematics with Applications, 62(7), 2011, 2770-2778.

S. Formica, M. Uysal, Market segmentation of an international cultural-historical event in Italy. Journal of Travel Research, 36(4), 1988, 16-24.

C.N. French, A. Collier, S. J. Craig-Smith, Principles of Tourism (2nd ed). Longman Australia, Sydney, 2000.

A. García, C. Bentes, R. Melo, B. Zadrozny, T. Penna, Sensor data analysis for equipment monitoring, Knowledge Information Systems, 28, 2011, 333–364.

C.R. García-Alonso, P. Campoy-Muñoz, M. Salazar-Ordoñez, A multi-objective evolutionary algorithm for enhancing Bayesian Networks hybrid-based modeling, Computers and Mathematics with Applications, 66(10), 2013, 1971-1980.

S. Gardiner, C. King, D. Grace, Travel decision making: an empirical examination of generational values, attitudes, and intentions. Journal of Travel Research, 52(3), 2013, 310-324.

J.F. Gaski, M.J. Etzel, The index of consumer sentiment toward marketing. The Journal of Marketing, 50,3, 1986, 71-81.

C.Y. Gee, D.J. Choy, J.C. Makens, The travel industry. AVI Publishing Company, Inc., 1984.

K.J. Gergen, The communal creation of meaning. The nature and ontogenesis of meaning, 1994, Chapter 2, pp.19-40.

K. Gibert, Automatic generation of classes interpretation as a bridge between clustering and decision making, International Journal of Multicriteria Decision Making 4(2), 2014, 154-182.

K. Gibert, D. Conti, On the understanding of profiles by means of post-processing techniques: An application to financial assets, International Journal of computer mathematics, 2014. DOI 10.1080/00207160.2014.898065 Taylor and Francis

K. Gibert, D. Conti, aTLP: A color-based model of uncertainty to evaluate the risk of decisions based on prototypes. Artificial Intelligence Communications 28, 2015, 113- 126.

K. Gibert, U. Cortés, Weighting quantitative and qualitative variables in clustering methods, Mathware and soft computing 4 (3), 1997, 251-266.

K. Gibert, A. García-Rudolph, G. Rodríguez-Silva, The role of KDD Support-Interpretation tools in the conceptualization of medical profiles: An application to neurorehabilitation. Acta Informatica Medica 16(4), 2008, 178-182.

K. Gibert, R. Nonell, Pre and post-processing in KLASS. Proc. of the iEMSs IVth International Congress of Environmental Modeling and Software (DM-TES'08 Workshop), vol III: 1965-1966, 2008.

K. Gibert, G. Rodríguez-Silva, R. Annicchiarico, Post-processing: bridging the gap between modelling and effective decision-support. The Profile Assessment Grid in Human Behaviour. Mathematical and Computer Modelling 57(7-8), 2013, 1633-1639.

K. Gibert, G. Rodríguez-Silva, I. Rodríguez-Roda, Knowledge discovery with clustering based on rules by states: a water treatment application. Environmental Modelling Software, 25, 2010, 712–723.

K. Gibert, M. Sànchez-Marrè, J. Izquierdo, A Survey on Pre-processing Techniques in the Context of Environmental Data Mining. Artificial Intelligence Communications, 29(6), 2016, 627-663.

K. Gibert, A. Valls, M. Batet, Introducing semantic variables in mixed distance measures: impact on hierarchical clustering, Knowledge and Information Systems, 40 (3), 2014, 559-593.

A. Gómez-Pérez, M. Fernández-López, O. Corcho, Ontological engineering. Springer, Berlin, 2004.

A. D. Gordon, A. D. Classification, Chapman and Hall, 1999.

J. Gower, A general coefficient of similarity and some of its properties. Biometrics 27(4), 1991, 857–874.

K. E. Grimm, M.D. Needham, Moving beyond the “I” in motivation: Attributes and perceptions of conservation volunteer tourists. Journal of Travel Research, 51(4), 2012, 488-501.

P. Gu, Q. Zhu, C. Zhang, A multi-view approach to semi-supervised document classification with incremental Naive Bayes, Computers and Mathematics with Applications, 57(6), 2009, 1030-1036.

B.D. Guillet, A. Lee, R. Law, R. Leung, Factors affecting outbound tourists’ destination choice: The case of Hong Kong. Journal of Travel and Tourism Marketing, 28(5), 2011, 556-566.

M. Halkidi Y. Batistakis, M. Vazirgiannis, On clustering validity checking methods: part II. ACM Sigmoid Record, 31(3), 2002, 19-27.

G. Hankinson, The brand images of tourism destinations: a study of the saliency of organic images, Journal of Product and Brand Management, 13(1), 2004, 6–14.

R. Harrill, T.D. Potts, Social psychological theories of tourist motivation: Exploration, debate, and transition. Tourism Analysis, 7(2), 2002, 105-114.

E. Helsper, L. van der Gaag, Building Bayesian networks through ontologies, Proceedings of European Conference on Artificial Intelligence, 2002, pp 680–684.

S. Hosany, G. Prayag, Patterns of tourists’ emotional responses, satisfaction, and intention to recommend, Journal of Business Research, 66, 2013, 730-737.

A. Hotho, S. Staab, G. Stumme (2003) Ontologies improve text document clustering. Proceedings of the 3rd IEEE international conference on Data mining, 2003. pp 541– 544.

E.C. Hirschman, B.B. Stern, The roles of emotion in consumer research. Advances in consumer research, 26, 1999, 4-11.

C.H. Hsu, L.A. Cai, M. Li, Expectation, motivation, and attitude: A tourist behavioral model. Journal of Travel Research. 49(3), 2009, 282-296.

M. Ichino, H. Yaguchi, Generalized Minkowski metrics for mixed feature-type data analysis. IEEE Transactions Systems Man Cybernetics, 22(2), 1994, 146–153.

S.E. Iso-Ahola, Toward a social psychological theory of tourism motivation: A rejoinder. Annals of tourism research, 9(2), 1982, 256-262.

A.K. Jain, M.N. Murty, P.J. Flynn, Data clustering: a review, ACM Computing Surveys, 1999.

S.S. Jang, B. Bai, C. Hu, C.M.E. Wu, Affect, travel motivation, and travel intention: A senior market. Journal of Hospitality and Tourism Research, 33(1), 2009, 51-73.

S. Jang, L.A. Cai, Travel motivations and destination choice: A study of British outbound market. Journal of Travel and Tourism Marketing, 13(3), 2002, 111-133.

D. Kim, R. R. Perdue, The influence of image on destination attractiveness. Journal of Travel & Tourism Marketing, 28(3), 2011, 225-239.

D.B. Klenosky, The “pull” of tourism destinations: A means-end investigation. Journal of Travel Research, 40(4), 2002, 396-403.

J. Krippendorf, Ecological approach to tourism marketing. Tourism Management, 8(2), 1987, 174-176.

C.K. Lee, S.K. Kang, Y. K. Lee, Segmentation of mega event motivation: The case of Expo 2010 Shanghai China. Asia Pacific Journal of Tourism Research, 18(6), 2013, 637-660.

W.N. Lee, N. Shah, K. Sundlass, M. Musen, Comparison of ontology-based semanticsimilarity measures, Proceedings of AMIA Annual Symposium, 2008, 384-388.

C.H.Lin, D.B. Morais, D.L.Kerstetter, A.S. Hou, Examining the role of cognitive and affective image in predicting choice across natural developed, and theme-park destinations. Journal of Travel Research, 46, 2007, 183-194.

D. MacCannell, The tourist: A new theory of the leisure class. Univ of California Press, 1976.

D. MacCannell, El Turista: una nueva teoría de la clase ociosa. Melusina, 2003.

Y. Mansfeld, From motivation to actual travel. Annals of Tourism Research, 19(3), 1992, 399-419.

E. Mariné-Roig, S. Anton-Clavé, Semi-automatic content analysis of trip diaries: Catalonia pull factors. Kozak, M. & Kozak, N. (Eds). Tourist Behavior: An International Perspective. CABI, Wallingford y Cambridge, 2017.

A. Massieu, Recomendaciones Internacionales sobre estadísticas de turismo de la Organización Mundial de Turismo. Revista de estadística y sociedad, 24, 2007, 9-10.

L. Martínez, D. Ruan, F. Herrrera, E. Herrera-Viedma, P.P. Wang, Linguistic decision making: tools and applications, Information Sciences, 179(14), 2009, 2297-2298.

M. Mody, J. Day,S. Sydnor, W. Jaffe, X, Lehto, The different shades of responsibility: Examining domestic and international travelers' motivations for responsible tourism in India. Tourism Management Perspectives, 12, 2014, 113-124.

A. Moreno, A. Valls, D. Isern, L. Marin, J. Borràs, SigTur/E-Destination: ontologybased personalized recommendation of Tourism and Leisure Activities, Engineering Applications of Artificial Intelligence, 26(1), 2013, 663-651.

A. Moreno, A. Valls, S. Martínez, C. Vicient, L. Marín, F. Mata, Personalised recommendations based on novel semantic similarity and clustering procedures, AI Communications, 28 (1), 2014, 27-142.

A. H. Nikjoo, M. Ketabi, The role of push and pull factors in the way tourists choose their destination. Anatolia, 26(4), 2015, 588-597.

G. P. Nyaupane, C.M. Paris, V. Teye, Study abroad motivations, destination selection and pre‐trip attitude formation. International Journal of Tourism Research, 13(3), 2011, 205-217.

D.B. Park, Y.S. Yoon, Segmentation by motivation in rural tourism: A Korean case study. Tourism management, 30(1), 2009, 99-108.

P.L. Pearce, Fundamentals of tourism motivation. Tourism research: Critique and challenges, 1993, 113-134.

P.L. Pearce, U.I. Lee, Developing the travel career approach to tourist motivation. Journal of Travel Research, 43(3), 2005, 226-237.

P.L. Pearce, J. Packer, Minds on the move: New links from psychology to tourism. Annals of Tourism Research, 40, 2013, 386-411.

T. Pedersen, S. Pakhomov, S. Patwardhan, C. Chute, Measures of semantic similarity and relatedness in the biomedical domain. Journal of Biomedical Informatics, 40, 2007, 288–299.

J.A. Pesonen, Segmentation of rural tourists: combining pupsch and pull motivations, Tourism and hospitality Management, 18(1), 2012, 69-82.

D. Picard, M. Robinson, Emotion in motion: Tourism, affect and transformation. Ashgate Publishing, Ltd., 2012.

G.D. Pires, J. Stanton, P. Stanton, Revisiting the substantiality criterion: from ethnic marketing to market segmentation, Journal of Business Research, 64, 2011, 988-996.

S.C. Plog Why destination areas rise and fall in popularity. Cornell hotel and restaurant administration quarterly, 1974, 14(4), 55-58.

S.C. Plog, A carpenter’s tools: An answer to Stephen LJ Smith’s review of psychocentrism/allocentrism. Journal of Travel Research, 28(4), 1990, 43-45.

S.C. Plog, Leisure travel: making it a growth market.... again!. John Wiley and Sons, Inc, 1991.

G. Prayag, Images as pull factors of a tourist destination: A factor-cluster segmentation analysis. Tourism Analysis, 15(2), 2010, 213-226.

G. Prayag, S. Hosany, When Middle East meets West: Understanding the motives and perceptions of young tourists from United Arab Emirates. Tourism Management, 40, 2014, 35-45.

G. Prayag, S. Hosany, B. Muskat, G. Del Chiappa,. Understanding the Relationships between Tourists’ Emotional Experiences, Perceived Overall Image, Satisfaction, and Intention to Recommend. Journal of Travel Research, 56(1), 2017, 41-54.

G. Prayag, C. Ryan, The relationship between the ‘push’and ‘pull’factors of a tourist destination: The role of nationality–an analytical qualitative research approach. Current Issues in Tourism, 14(2), 2011, 121-143.

C. Pronello, C. Camusso, Traveller’s profiles definition using statistical multivariate analysis of attitudinal variables, Journal of Transport Geography, 19, 2011, 1294-1308.

C. Pluempitiwiriyaweja, N. Cerconeb, X. An, Lexical acquisition and clustering of word senses to conceptual lexicon construction, Computers and Mathematics with Applications, 57(9), 2009, 1537-1546.

G. Punj, D.W. Stewart, Cluster analysis in marketing research: Review and suggestions for application. Journal of marketing research, 20(2), 1983, 134-148.

P.J. Rousseeuw, Silhouettes: a graphical aid to the interpretation and validation of cluster analysis. Journal of Computational and Applied Mathematics, 20, 1987, 53-65.

C. Sanz-Ibáñez, S. Anton Clavé, Strategic coupling evolution and destination upgrading. Annals of Tourism Research, 56 (1): 2016 1-15

E. Sirakaya, S.F. Sonmez, H.S. Choi, Do destination images really matter? Predicting destination choices of student travellers. Journal of Vacation Marketing, 7 (2), 2001, 125-142.

E. Sirakaya, M. Uysal, C.F. Yoshioka, Segmenting the Japanese tour market to Turkey. Journal of Travel Research, 41(3), 2003, 293-304.

W. R. Smith, Product differentiation and market segmentation as alternative marketing strategies. Journal of Marketing, 21(1), 1956, 3-8.

D. Snepenger, S. Reiman, J. Johnson, M. Snepenger, Is downtown mainly for tourists?. Journal of Travel Research, 36(3), 1998, 5-12.

D. Snepenger, L. Murphy, M. Snepenger, W. Anderson, Normative meanings of experiences for a spectrum of tourism places. Journal of Travel Research, 43(2), 2004, 108-117.

D. Snepenger, M. Snepenger, M. Dalbey, A. Wessol, Meanings and consumption characteristics of places at a tourism destination. Journal of Travel Research, 45(3), 2007, 310-321.

S. Song, Z. Guo, P. Chen, Fuzzy document clustering using weighted conceptual model. Information Technology Journal, 10(6), 2011, 1178–1185.

M. Steyvers, P. Smyth, C. Chemuduganta, Combining background knowledge and learned topics, Topics in Cognitive Science, 3, 2001, 18–47

P.A. Stokowski, Languages of place and discourses of power: Constructing new senses of place. Journal of Leisure Research, 34(4), 2002, 368.

Y. K. Sung, K.C. Chang, Y. F. Sung, Market segmentation of international tourists based on motivation to travel: A case study of Taiwan. Asia Pacific Journal of Tourism Research, 21(8), 2016, 862-882.

M. Thangamani, P. Thangaraj, Integrated clustering and feature selection scheme for text documents. Journal of Computer Science, 6(5), 2010, 536–541.

A.J.C. Trappey, C.V. Trappey, T-A. Chiang, Y-H. Huang, Ontology-based neural network for patent knowledge management in design collaboration, International Journal of Production Research, 51(7), 2013, 1992-2005.

S. Um, J.L. Crompton, Attitude determinants in tourism destination choice. Annals of Tourism Research, 17(3), 1990, 432-448.

J. Urry, The Consumption of Tourism. Sociology, 24(1), 1990, 23-35.

M. Uysal, X. Li, E. Sirakaya-Turk, Push-pull dynamics in travel decisions. In: Pizam, A. (ed.) Handbook of hospitality marketing management. Elsevier, Oxford, UK, 2008, 412-439.

P. D’Urso, L. De Giovanni, M. Disegna, R. Massari, Bagged clustering and its application to tourism market segmentation, Expert Systems with Applications, 40, 2013, 4944-4956.

G. Vadivelou, E. Ilavarasan, Performance Evaluation of Semantic Approaches for Automatic Clustering of Similar Web Services, Proceedings of the World Congress on Computing and Communication Technologies, 2014, pp. 237-242.

P. Vossen (ed), EuroWordNet: A Multilingual Database with Lexical Semantic Networks. Springer, 1999.

B Wang, Y. Miao, H. Zhao, J. Jin, Y. Chen, A biclustering-based method for market segmentation using customer pain points, Engineering Applications of Artificial Intelligence, 2015 in press.

J.H.Jr. Ward, Hierarchical Grouping to Optimize an Objective Function, Journal of the American Statistical Association, 58, 1963, 236–244.

A. Ward, A. Segmenting the senior tourism market in Ireland based on travel motivations. Journal of Vacation Marketing, 20(3), 2014, 267-277.

M. Wedel, W.A. Kamakura, Market Segmentation: Conceptual and Methodological Foundations. Dordrecht: Kluwer, 2<sup>nd</sup> edition, 2000.

S. Yang, P. Liao, C. Ho, An ontology-supported case-based reasoning technique for FAQ proxy service, Proceedings of the 17th international conference on software engineering and knowledge engineering, 2005, pp 639–644.

X. Zhao, H.-Z. Guan, H. Wang, An analysis on choice behavior of tourist destination based on tourist motivation, Journal of Transportation Systems Engineering and Information Technology, 14(5), 2014.

L. A. Zadeh, The concept of a linguistic variable and its application to approximate reasoning. Information Sciences 8, 1975, 199–249.

J. Zhang, A. Silvescu, V. Honavar, Ontology-driven induction of decision trees at multiple levels of abstraction. In: Koenig S, Holte R (eds) Abstraction, reformulation, and approximation, vol. 2371 of Lecture Notes in Computer Science, Springer, Berlin, Heidelberg, 2002, pp 316–323.

#

G. Zuccon, A.S. Wagholikar, A.N. Nguyen, L. Butt, K. Chu, S.Martin, J. Greenslade, Automatic classification of free-text radiology reports to identify limb fractures using machine learning and the Snomed CT ontology, Proceedings of AMIA Summits on Translational Science, 2013, pp. 300-304.

Aida Valls is a Lecturer at the Department of Computer Science and Mathematics in Universitat Rovira i Virgili (URV). She received her PhD in Computer Science from the Technical University of Catalonia in 2002. Her research interests include multiple criteria decision-making, recommender systems, data mining and privacy preserving. Her work is mainly focused on the treatment of linguistic and semantic information. She has participated in several Spanish and EU research projects, with applications in Tourism, Environment Risk Management and Health Care. She is the author of more than 80 papers published in international journals and conferences. She is currently the Vice-president of the Catalan Association for Artificial Intelligence and the Head of the PhD Program in Computer Science and Mathematics of Security at URV.

Karina Gibert is an Associate Professor at the Universitat Politècnica de Catalunya-BarcelonaTech (UPC). She received her PhD in Computer Science. She was a Pioneer member (1986) and current Head of the Knowledge Engineering and Machine Learning research Group (UPC), with excellence certificate from the Catalan government. Her areas of interest include hybrid AI and Statistics Data Mining, AI, intelligent data analysis, pre and post-processing, knowledge discovery and data mining, intelligent decision support, and data science. She was particularly interested in multidisciplinar and applied research as well as technology transfer to productive sector. She has long experience in health and environmental applications. She has participated in several Spanish and EU research projects. She was a Technical consultant of Catalan Government for Spanish Dependency Law deployment (2006–2008); Consultant of the Mental Health Department at WHO (2008–2010); Head of Plant-Guesser project (Aquology, AGBAR group, 2014); IP of Diet4You project (2015-, Spanish Government); EU-best e-Health European project for K4Care (2010). She was a Winner of 1rst HackingBullipedia contest (Telefonica and elBulliFoundation from Ferran Adrià, nov 2013). She organizes special workshops in Data Mining and Intelligent decision support systems in the International conferences from 2000, in particular, in the Int’l Congress on Environmental Modelling and Software from 2002. She has conducted intensive scientific research (more than 300 papers, 37 SCI-papers, H-index:17), with uninterrupted excellence certification from the Spanish government since 1990.

Alicia Orellana is the Director of the Tourism Observatory at the Science and Technology Park for Tourism and Leisure of Catalonia. She holds a large experience in tourism market research. She is in charge of the measurement of the performance of the tourism accommodation industry in several tourism brands and local destinations in Catalonia since 2001. As a director of the Tourism Observatory, she has also been in charge of ad hoc market and destination survey operations, data analysis and in company statistical research studies. She is a Social Pyschologist from the Rovira I Virgili University (1996).

Salvador Antón-Clavé is a Full Professor of Regional Geographical Analysis at the Rovira i Virgili University (URV) and serves as the Director of Research at the Science & Technology Park for Tourism and Leisure. He is currently Head of the Phd Program in Tourism and Leisure at the URV and Research Scholar at the International Institute of Tourism Studies at the George Washington University. He has served as the

Director/Dean of the Tourism and Leisure School/Faculty of Tourism and Geography at the Rovira i Virgili University between 2002 and 2012. His has extensively published on the analysis of the evolution of tourism destinations, urban and regional tourism planning and development, the globalization of leisure facilities and issues concerning tourism and ICT.

![](/api/attachments/VCEBJFZ8/fulltext/images/b44dd7df49452e486f44a12ecb8b8d8c62c7dc8009b7bfcd4ead1490cb41bf11.jpg)  
Fig. 1. Dendrogram representing the hierarchical clustering of British tourists.

![](/api/attachments/VCEBJFZ8/fulltext/images/10b1c8956ea98663ca6141fc2378f0b10bfea0ad91743890e3302a6d1aebb002.jpg)

Table 1. Recoding of original answers to Motivation-Reason into WordNet concepts.

<table><tr><td>Original answer</td><td>WordNet term</td><td>Freq</td><td></td></tr><tr><td>Port Aventura</td><td></td><td></td><td></td></tr><tr><td></td><td>1. Entertainment</td><td>2. 5</td><td></td></tr><tr><td>Aquopolis</td><td></td><td></td><td></td></tr><tr><td></td><td>3. Entertainment</td><td>4. 1</td><td></td></tr><tr><td>Visiting friends</td><td></td><td></td><td></td></tr><tr><td></td><td>5. Friend</td><td>6. 5</td><td></td></tr><tr><td>Vacances</td><td></td><td></td><td></td></tr><tr><td></td><td>7. Holiday</td><td>8. 4</td><td></td></tr><tr><td>Second home</td><td></td><td></td><td></td></tr><tr><td></td><td>9. Property</td><td>10. 2</td><td></td></tr><tr><td>Owned house</td><td></td><td></td><td></td></tr><tr><td></td><td>11. Property</td><td>12. 1</td><td></td></tr><tr><td>Visit parents</td><td></td><td></td><td></td></tr><tr><td></td><td>13. Family</td><td>14. 2</td><td></td></tr><tr><td>Gaudí</td><td></td><td></td><td></td></tr><tr><td></td><td>15. Culture</td><td>16. 1</td><td></td></tr><tr><td>Tarraco Viva</td><td></td><td></td><td></td></tr><tr><td></td><td>17. Culture</td><td>18. 1</td><td></td></tr><tr><td>Love it</td><td></td><td></td><td></td></tr><tr><td></td><td>19. Beauty</td><td>20. 1</td><td></td></tr><tr><td>Too see historical things</td><td></td><td></td><td></td></tr><tr><td></td><td>21. History</td><td>22. 1</td><td></td></tr><tr><td>Been before</td><td></td><td></td><td></td></tr><tr><td></td><td>23. Return</td><td>24. 1</td><td></td></tr><tr><td>Our way to Morocco</td><td></td><td></td><td></td></tr><tr><td></td><td>25. Transition</td><td>26. 1</td><td></td></tr><tr><td>Stay here</td><td></td><td></td><td></td></tr><tr><td></td><td>27. Permanence</td><td>28. 1</td><td></td></tr><tr><td>Spanish people</td><td></td><td></td><td></td></tr><tr><td></td><td>29. People + location</td><td>30. 1</td><td></td></tr><tr><td>Good-looking</td><td></td><td></td><td></td></tr><tr><td></td><td>31. Attractiveness</td><td>32. 1</td><td></td></tr><tr><td>Party</td><td></td><td></td><td></td></tr><tr><td></td><td>33. Festivity</td><td>34. 1</td><td></td></tr><tr><td>School music tour</td><td></td><td></td><td></td></tr><tr><td></td><td>35. Concerts</td><td>36. 1</td><td></td></tr><tr><td>Holidays fishing</td><td></td><td></td><td></td></tr><tr><td></td><td>37. Sportfishing</td><td>38. 1</td><td></td></tr><tr><td>Work</td><td></td><td></td><td></td></tr><tr><td></td><td>39. Job</td><td>40. 1</td><td></td></tr><tr><td>Very Spanish</td><td></td><td></td><td></td></tr><tr><td></td><td>41. Typicality</td><td>42. 1</td><td></td></tr><tr><td>No commercial</td><td></td><td></td><td></td></tr><tr><td></td><td>43. Calmness</td><td>44. 1</td><td></td></tr><tr><td>Near the sea</td><td></td><td></td><td></td></tr><tr><td></td><td>45. Sea</td><td>46. 1</td><td></td></tr></table>

Table 2. Recoding of original answers to Meaning into WordNet concepts.

<table><tr><td>Original answer</td><td>WordNet term</td><td>Freq</td><td></td></tr><tr><td>Port Aventura</td><td></td><td></td><td></td></tr><tr><td></td><td>47. Entertainment</td><td>48. 12</td><td></td></tr><tr><td>Good-looking</td><td></td><td></td><td></td></tr><tr><td></td><td>49. Attractiveness</td><td>50. 8</td><td></td></tr><tr><td>Very-good</td><td></td><td></td><td></td></tr><tr><td></td><td>51. Goodness</td><td>52. 2</td><td></td></tr><tr><td>Vacances</td><td></td><td></td><td></td></tr><tr><td></td><td>53. Holiday</td><td>54. 1</td><td></td></tr><tr><td>Beach water</td><td></td><td></td><td></td></tr><tr><td></td><td>55. Sea</td><td>56. 1</td><td></td></tr><tr><td>Different</td><td></td><td></td><td></td></tr><tr><td></td><td>57. Distinctiveness</td><td>58. 1</td><td></td></tr><tr><td>Restful</td><td></td><td></td><td></td></tr><tr><td></td><td>59. Relaxation</td><td>60. 1</td><td></td></tr><tr><td>Balcó Mediterrani</td><td></td><td></td><td></td></tr><tr><td></td><td>61. Landscape</td><td>62. 1</td><td></td></tr><tr><td>Friendly</td><td></td><td></td><td></td></tr><tr><td></td><td>63. Kindness</td><td>64. 1</td><td></td></tr><tr><td>Good price</td><td></td><td></td><td></td></tr><tr><td></td><td>65. Cheapness</td><td>66. 1</td><td></td></tr><tr><td>Blue sky</td><td></td><td></td><td></td></tr><tr><td></td><td>67. Sky</td><td>68. 1</td><td></td></tr></table>

Table 3. Segmentation of the British tourism in the Costa Daurada and Terres de l’Ebre.

<table><tr><td></td><td>Push factorsMotivation-Reason</td><td>Pull factorMeanings</td><td>Location</td><td>Typology of places</td></tr><tr><td rowspan="2">C453VisitingN=151</td><td></td><td></td><td></td><td>71. 72. Iconic(51)City spots (24)Inland (12)Quiet southern natural areas (11)</td></tr><tr><td>Tourism (21)Shopping (20)</td><td>Tourism (19)Culture (16)Niceness (11)</td><td>Cambrils (13)Salou (18)La Pineda (14)Terres de l'Ebre (11)</td><td></td></tr><tr><td rowspan="3">C455EnjoyingN=149</td><td></td><td></td><td></td><td>75. 76. Iconic(36)City spots (34)Quiet southern natural areas (23)Iconic (9)Inland (5)</td></tr><tr><td></td><td></td><td>La Pineda (33)Cambrils (22)Tarragona (23)</td><td></td></tr><tr><td></td><td>Niceness (21)Relaxation (16)Entertainment (9)</td><td>South (19)Inland TE (9)</td><td></td></tr><tr><td>C446HolidaysN=52</td><td></td><td></td><td></td><td>79. 80. Iconic (7)Unique Beaches (6)City spots (6)</td></tr><tr><td></td><td>Beach (14)</td><td colspan="3">Cambrils (12) Pineda (13)</td></tr><tr><td colspan="5">C449</td></tr><tr><td rowspan="3">Beaching N=42</td><td rowspan="3">{</td><td rowspan="2">{</td><td>83.</td><td rowspan="2">84. City spots (22)</td></tr><tr><td>Iconic (5)</td></tr><tr><td colspan="3">La Pineda (14)</td></tr><tr><td colspan="5">Beach (8)</td></tr><tr><td colspan="5">C438</td></tr><tr><td rowspan="3">Sunbathing N=39</td><td rowspan="3">{</td><td rowspan="2">{</td><td>87.</td><td rowspan="2">88. City spots (9)</td></tr><tr><td>Unique beaches (6) Iconic (9)</td></tr><tr><td colspan="3">La Pineda (10) Tarragona (5)</td></tr><tr><td colspan="5">Beach (8)</td></tr><tr><td colspan="5">C414</td></tr><tr><td rowspan="3">Relaxing N=27</td><td rowspan="2">{</td><td rowspan="2">{</td><td>91.</td><td rowspan="2">92. City spots(5)</td></tr><tr><td>Iconic (5) Unique beaches (5) Quiet southern natural areas (3)</td></tr><tr><td>Goodness (5) Relaxation (4)</td><td colspan="3">La Pineda (6) South (3)</td></tr></table>

##

##

Table 4. Cluster validity indexes for several clustering methods.

<table><tr><td>Metrics</td><td>Partition</td><td>AvBet</td><td>AvWit</td><td>MaxDia m</td><td>MinSep</td><td>wSS</td><td>avSilWidth</td><td>G20.4</td><td>Pearson</td><td>D0.1</td><td>D20.8</td><td>Entropy</td><td>wbRatio</td><td>CH</td><td>widestGap</td><td>Sindex</td><td>RankSum</td></tr><tr><td rowspan="4">GG</td><td>Ward</td><td>0.82</td><td>0.65</td><td>1.72</td><td>0.26</td><td>99.39</td><td>0.20</td><td>50.3</td><td>0.39</td><td>50.0</td><td>60.2</td><td>1.57</td><td>0.80</td><td>42.96</td><td>0.95</td><td>0.31</td><td>93.50</td></tr><tr><td>Ward-cut1.7</td><td>0.71</td><td>0.41</td><td>3.33</td><td>0.05</td><td>116.06</td><td>0.05</td><td>50.3</td><td>0.22</td><td>20.0</td><td>10.2</td><td>1.56</td><td>0.58</td><td>14.31</td><td>2.07</td><td>0.06</td><td>81.00</td></tr><tr><td>Ward-cut2.2</td><td>0.74</td><td>0.46</td><td>4.11</td><td>0.05</td><td>165.30</td><td>0.03</td><td>00.8</td><td>0.23</td><td>10.5</td><td>01.0</td><td>1.08</td><td>0.62</td><td>3.77</td><td>2.75</td><td>0.06</td><td>69.00</td></tr><tr><td>Ward-Mode</td><td>3.68</td><td>2.57</td><td>4.00</td><td>2.00</td><td>1634.60</td><td>0.30</td><td>6-0.4</td><td>0.61</td><td>00.0</td><td>80.1</td><td>1.37</td><td>0.70</td><td>108.31</td><td>3.00</td><td>2.00</td><td>91.00</td></tr><tr><td rowspan="2">chi2</td><td>Optics</td><td>0.38</td><td>0.67</td><td>4.34</td><td>0.03</td><td>174.71</td><td>-0.45</td><td>10.8</td><td>-0.17</td><td>10.0</td><td>60.8</td><td>0.34</td><td>1.75</td><td>-3.32</td><td>2.21</td><td>0.05</td><td>40.50</td></tr><tr><td>OpticsDBSCA</td><td>3.62</td><td>2.50</td><td>4.00</td><td>0.00</td><td>1573.86</td><td>0.23</td><td>10.1</td><td>0.55</td><td>00.0</td><td>50.7</td><td>1.69</td><td>0.69</td><td>70.70</td><td>3.00</td><td>0.96</td><td>70.00</td></tr><tr><td rowspan="2">Hamm</td><td>N</td><td>0.79</td><td>0.74</td><td>1.72</td><td>0.00</td><td>130.82</td><td>-0.05</td><td>70.1</td><td>0.09</td><td>00.0</td><td>10.2</td><td>1.69</td><td>0.95</td><td>10.82</td><td>1.05</td><td>0.02</td><td>55.50</td></tr><tr><td>DBSCA</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>chi2</td><td>N</td><td>0.63</td><td>0.61</td><td>4.34</td><td>0.00</td><td>188.81</td><td>-0.03</td><td>6</td><td>0.01</td><td>0</td><td>3</td><td>1.69</td><td>0.98</td><td>-8.00</td><td>2.23</td><td>0.05</td><td>39.50</td></tr></table>
