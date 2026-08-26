---
otero_id: 6228
otero_key: "E72QBRNR"
title: "Predicting Adoption Probabilities in Social Networks"
authors: "Xiao Fang; Paul Jen-Hwa Hu; Zhepeng (Lionel) Li; Weiyu Tsai"
year: "2013"
journal: "Information Systems Research"
doi: "10.1287/isre.1120.0461"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Predicting Adoption Probabilities in Social Networks

Xiao Fang, Paul Jen-Hwa Hu, Zhepeng (Lionel) Li, Weiyu Tsai David Eccles School of Business, University of Utah, Salt Lake City, Utah 84112 {xiao.fang@business.utah.edu, paul.hu@business.utah.edu, lionel.li@business.utah.edu, weiyu.tsai@business.utah.edu}

n a social network, adoption probability refers to the probability that a social entity will adopt a prod-Iuct, service, or opinion in the foreseeable future. Such probabilities are central to fundamental issues in social network analysis, including the influence maximization problem. In practice, adoption probabilities have significant implications for applications ranging from social network-based target marketing to political campaigns, yet predicting adoption probabilities has not received sufficient research attention. Building on relevant social network theories, we identify and operationalize key factors that affect adoption decisions: social influ ence, structural equivalence, entity similarity, and confounding factors. We then develop the locally weighted expectation-maximization method for Naïve Bayesian learning to predict adoption probabilities on the basis of these factors. The principal challenge addressed in this study is how to predict adoption probabilities in the presence of confounding factors that are generally unobserved. Using data from two large-scale social networks, we demonstrate the effectiveness of the proposed method. The empirical results also suggest that cascade methods primarily using social influence to predict adoption probabilities offer limited predictive power and that confounding factors are critical to adoption probability predictions.

Key words: adoption probability; social network; Bayesian learning; social influence; structural equivalence; entity similarity; confounding factor

History: Chris Dellarocas, Senior Editor; Panagiotis Ipeirotis, Associate Editor. This paper was received on January 16, 2012, and was with the author 3 months for 1 revision. Published online in Articles in Advance January 14, 2013.

## 1. Introduction

Fostered by the ubiquitous information technology, social networks such as those facilitated by Facebook, Twitter, electronic mail, or mobile phone (Dodds et al. 2003, Kleinberg 2008, Eagle et al. 2009) have attracted increasing attention from both academia and industry that explores how to leverage such networks for greater business and societal benefits (Domingos and Richardson 2001, Pentland 2008, Chen and Zeng 2009, Weng et al. 2010, Aral et al. 2011). A salient feature of social networks is the spread of adoption behavior (e.g., adoption of a product, service, or opinion) from one social entity to another in a social network (Kleinberg 2008). This feature is central to a wide variety of applications in business (e.g., Domingos and Richardson 2001), public health (e.g., Chen et al. 2011), and politics (e.g., Carr 2008). Predicting the probability that a social entity will adopt a product, service, or opinion in the foreseeable future, namely, adoption probability, is critical to these applications. For business organizations, such predictions are crucial to many important applications enabled by the growing proliferation of social media, such as social networkbased target marketing (Hill et al. 2006), viral marketing (Domingos and Richardson 2001), and demand prediction (Hartmann 2010, Altshuler et al. 2012).<sup>1</sup> Consider viral marketing as an example; it targets an initial group of consumers and exploits social networks to market to a broader population. Effective viral marketing requires optimal selection of initially targeted consumers (Dye 2000, Domingos and Richardson 2001), which in turn depends on reliable prediction of adoption probabilities because to compare target options and search for the optimal one, one needs to predict how likely other consumers will adopt if initially targeted consumers adopt.

Although predicting adoption probabilities is critical for many social network-based applications enabled by social media, it is also an important academic research problem. Studying the spread of adoption in a social network has long been a fundamental area in social sciences, particularly social computing (Kleinberg 2007). To better understand the spread of adoption, a fundamental question is how to predict (future) adoption probabilities for individuals who have not adopted by now. Answering this question is a precursor to solving several challenging problems in social computing, such as the influence maximization problem (Kempe et al. 2005). Solutions to the problem can provide methodological foundations to novel business applications enabled by social media, such as viral marketing. Existing methods for influence maximization rely on adoption probabilities that typically are set arbitrarily or assumed as given (Kempe et al. 2005, Chen et al. 2010). In actuality, adoption probabilities are often not given; however, how to predict these probabilities has been mostly unexplored (Kleinberg 2007).

Although critical from both research and practice standpoints, predicting adoption probabilities has not received adequate investigative attention. This motivates our work, to which previous studies of cascade methods (Kempe et al. 2003; Kimura and Saito 2006; Chen et al. 2009, 2010) are relevant. Building on the independent cascade model (Kleinberg 2007), cascade methods compute a social entity’s likelihood of adoption from the lens of social influence (Chen et al. 2009, 2010). Cascade methods assume that a social entity’s likelihood of adoption at time t + 1 depends on his or her neighbors, who become adopters at time t through their social influences (Chen et al. 2009, 2010).<sup>2</sup> They further assume that each adopter neighbor of a social entity influences the entity independently (Chen et al. 2009, 2010). Concretely, at time $t ,$ let $v$ be a nonadopter and U be $v ^ { \prime } \mathrm { s }$ neighbors who become adopters at time t. With these two assumptions, the probability $p _ { v }$ of v adopting at time t + 1 is then computed as (Chen et al. 2009, 2010)

$$
p _ {v} = 1 - \prod_ {u \in U} (1 - p _ {u, v}),\tag{1}
$$

where $p _ { u , v }$ denotes the probability that u influences v to become an adopter. Assuming that each adopter neighbor of a social entity has an equal probability of influencing that entity to become an adopter, $p _ { u , v }$ is set to $1 / k$ for all $u \in \dot { U } .$ , where k is the number of social neighbors of v (Chen et al. 2009, 2010), or it is set as a constant, such as 0.1 or 0.01 (Kempe et al. 2003, Kimura and Saito 2006).

Goyal et al. (2010) propose a method to learn influence probabilities in a social network. With the same assumptions that cascade methods normally make, the influence probability method also uses Equation (1) to predict the likelihood of adoption (Goyal et al. 2010). Instead of arbitrarily setting $p _ { u , v }$ in Equation (1) as $1 / k$ or a constant, the influence probability method learns $p _ { u , v } ,$ namely, influence probability (Goyal et al. 2010), from logs of user actions. Specifically, this method learns $p _ { u , v }$ as the ratio of the number of actions propagated from u to v to the total number of actions performed by u (Goyal et al. 2010). A review of existing methods suggests several limitations. First, these methods often depend on one factor $( \mathrm { i . e . , }$ social influence) for predicting an entity’s likelihood of adoption. In addition to social influence, there could exist other factors that affect a social entity’s adoption decision, such as structural equivalence (Burt 1987) or confounding factors (Van den Bulte and Lilien 2001). Methods not considering these additional factors may not holistically reveal the adoption decision; consequently, their adoption likelihood predictions could become unreliable. Second, these methods approach a social entity’s adoption likelihood from a rather confined scope, typically focusing on social neighbors of the entity. However, a social entity’s adoption decision could be influenced by other adopters that are not social neighbors, e.g., through structural equivalence (Burt 1987). Third, most existing methods seem to utilize partial social network data to predict adoption probabilities, normally, social network structure data such as the number of social neighbors and the number of adopter neighbors. Other social network data, including intrinsic characteristics of individual entities as well as interaction intensities or relations among entities, could be important for adoption probability predictions and therefore should be considered.

To address these limitations, we target the following research questions:

(1) What key factors underlie a social entity’s adoption decision? How can these factors be operationalized with more comprehensive social network data?

(2) How can we better predict adoption probabilities by considering important factors underlying individuals’ adoption decisions?

(3) Although confounding factors are generally considered to be unobserved (Aral et al. 2009, Aral 2011), we cannot ignore their significance in adoption probability predictions because they may constitute an important force of the adoption decision. Thus, a more challenging question is how to predict adoption probabilities in the presence of unobserved confounding factors.

These questions are central to novel techniques enabled by social media, such as social networkbased target marketing and demand prediction, that are essential to social commerce and online gaming. To address these research questions, we develop a Bayesian learning method for predicting adoption probabilities, which represents an essential contribution of our study. The proposed method employs relevant social network theories to identify key factors underlying adoption decisions; it is developed with appropriate machine learning theories and techniques. The principal challenge addressed by our method is how to predict adoption probabilities in the presence of unobserved confounding factors. We demonstrate the effectiveness of our method with data from two large-scale social networks. Our empirical results offer two interesting observations. First, cascade methods that exclusively use social influence to predict adoption probabilities seem ineffective. Second, confounding factors appear to play a significant role in adoption probability predictions, as manifested by the substantial improvement when taking such factors into consideration. Overall, our findings suggest that individuals’ adoption decisions in a social network could be influenced by several related but distinct forces, above and beyond social influence, and that adoption probabilities could be better analyzed and predicted from a holistic perspective that uses more comprehensive social network data.

The rest of the paper is organized as follows. We identify key factors underlying adoption decision and propose how to operationalize these factors with social network data in §2. The problem of predicting adoption probabilities is formulated and a Bayesian learning method is then proposed to solve the problem in §3. We evaluate the effectiveness of the proposed method with data from two large-scale social networks and report our evaluation results and observations in §4. The paper concludes with discussions of contributions, managerial implications, and limitations in §5.

## 2. Key Factors Underlying Adoption Decision: Theoretical Foundations and Operationalization

We review relevant social network theories that point to several key factors underlying a social entity’s adoption decision and then propose ways to operationalize these factors with social network data.

## 2.1. Theoretical Foundations

The social information processing model (Salancik and Pfeffer 1978) suggests that socially communicated perceptions and beliefs can influence individuals’ opinions or behaviors. Specifically, social influences, or the impacts created through the interactions among people in a social context (Rice et al. 1990), represent an important force affecting individuals’ adoption behaviors in a social network (Ibarra and Andrews 1993, Leenders 2002, Bruyn and Lilien 2008, Shalizi and Thomas 2011). Social comparison theory (Festinger 1950) also suggests that people are motivated to evaluate their opinions and behaviors by comparing themselves with others. Furthermore, social influence network theory (Friedkin 1998)

posits that a person endowed with an initial opinion or behavioral assessment receives and responds to information propagated in a social network and could choose to modify an original opinion or assessment accordingly. These theories converge regarding the central role of the process by which people are influenced in communications and interactions with others, which leads to the creation of social influence (Leenders 2002). By communicating and interacting with one another, people create social influences that affect their opinions, attitudes, and behaviors (Rice et al. 1990, Leenders 2002, Iyengar et al. 2011). Bruyn and Lilien (2008) report that personal interactions among acquaintances impact not only consumption choice and purchase decision but also expectation, pre-usage attitude, and post-usage perception. People’s social ties, formed through communications and interactions, enable them to learn and reflect on others’ choices or opinions (Wellman 1997); the intensity of the resulting social influence reflects the strength of the social ties that connect them. In general, strong social ties entail substantial investments of time and reciprocity; therefore, people are more likely to trust each other for information sharing, opinion assessment, and decision making (Wellman 1997). As a result, people connected by stronger ties have greater influences on one another than those connected by weaker ties (Levy 1992, Levy and Nail 1993).

The structural characteristics of a social network may also affect opinions and behaviors (Burt 1987, Wejnert 2002). Network theorists argue that people develop similar opinions and behaviors through relationship patterns in a social network (Wellman 1983, Wejnert 2002). Structural equivalence is a fundamental structural characteristic of social network (Burt 1987); two social entities are structurally equivalent if they connect to other entities identically (Lorrain and White 1971, Wasserman and Faust 1994). Structurally equivalent people occupy the same position in the social structure and are proximate to varying extents. Such structural equivalence may be crucial to social contagion; two people identically positioned in the flow of influential communications can use the other as a frame of reference for subjective judgments and they are likely to make similar judgments, even without direct communications (Burt 1987). Therefore, weighting social entities by both structural equivalence and communications could produce more accurate adoption predictions than could focusing only on their direct communications (Wejnert 2002).

Structural equivalence also moderates adoptions by affecting the homogeneity of adopters’ behaviors (Wejnert 2002). Thus, people with similar social ties in a social network exhibit similar opinions or behaviors. Structural equivalence can reduce the uncertainty associated with the focal adoption, as perceived by individual entities; it represents an important force on their adoption behaviors, even in the absence of social ties that connect them directly. As Burt (1987) has noted, the spread of an opinion or behavior in a social network probably is contingent on the way the structure of the network brings people together. If they connect to the same group of people, two social entities likely exhibit similarity because they vicariously experience or even mimic each other through the others with which they interact in the network, and thus uncertainty associated with adoption decreases (Rice and Aydin 1991). In this light, people with highly comparable social ties exhibit similar opinions or behaviors.

In addition, entity similarity, or the degree to which two entities in a social network are similar demographically and behaviorally (Jackson 2008), constitutes another important force that influences adoption behaviors (Salancik and Pfeffer 1978). According to Lazarsfeld and Merton (1954), major sociodemographic dimensions can stratify societyascribed characteristics (e.g., ethnicity, gender, age) and acquired characteristics (e.g., education, occupation, behavior patterns). People with similar characteristics are more likely to exhibit similarity in their opinions and behaviors than otherwise (Aral et al. 2009). Such similarity also implies common interests and world views; people with highly similar demographic characteristics thus exhibit similar needs, wants, preferences, or tastes (Ibarra 1992). Entity similarity may also entail a behavioral dimension, such that people with similar behavioral profiles express similar opinions and prefer similar behaviors toward a new product or service (Ibarra 1992, Centola 2011). All else being equal, people who have responded to products (services) similarly before are more likely to continue exhibiting that similarity in the future. Brown and Reingen (1987) and Centola (2011) also consider similarity in demographic characteristics. Finally, entity similarity can affect social entities’ adoption probabilities, independent of their direct interactions (McPherson et al. 2001). The similarity of two social entities, measured demographically and behaviorally, thus could explain their adoption behaviors, in that the more similar they are, the greater similarity they exhibit in their adoption behaviors.

Adoption decisions in a social network may depend, though, on factors beyond social influences, structural equivalence, and entity similarity. These normally unobserved confounding factors appear influential in previous research (Van den Bulte and Lilien 2001, Aral et al. 2009). Aral (2011) identifies several sources of bias in both cross-sectional and longitudinal data that can confound the outcomes of social influence analyses; these are related to interactions and outcomes among peers, such as contextual and correlated effects (Manski 1993), unobserved heterogeneity (Van den Bulte and Lilien 2001), and marketing efforts, whose omission Iyengar et al. (2011) recognize creates upward biases in social contagion estimation. Despite the identification of several sources of confounding effects, many unobserved factors remain (Aral 2011) and may account for a significant portion of the variance in adoption behaviors observed in a social network. Our review of relevant theories thus sheds light on several important factors underlying adoption decision: social influence, structural equivalence, entity similarity, and unobserved confounding factors. We operationalize each, except unobserved confounding factors, with social network data.

## 2.2. Operationalization

Let $V = \{ v _ { 1 } , v _ { 2 } , \ldots , v _ { n } \}$ be a set of social entities. Pairs of social entities are linked by social ties, which can be directional or nondirectional (Wasserman and Faust 1994). For example, a social network on Twitter consists of Twitterers $( \mathrm { i . e . , }$ , social entities) connected by directional social ties $( \mathrm { i . e . , }$ one Twitterer following another), whereas a social network facilitated by mobile phone service consists of service users (i.e., social entities) connected by nondirectional social ties (i.e., two-way phone communications). The strength of a social tie reflects the intensity of actions through the tie (Brown and Reingen 1987). Considering the dynamic nature of social tie strength (Kossinets and Watts 2006), we denote $\boldsymbol { x } _ { i j } ^ { t }$ as the strength of the social tie from social entity $v _ { i } \in V$ to entity $\bar { v } _ { i } \in V$ at time t. $\boldsymbol { x } _ { i j } ^ { t }$ generally differs from $x _ { j i } ^ { t }$ for directional ties, $\boldsymbol { x } _ { i j } ^ { t }$ equals $x _ { j i } ^ { t }$ for nondirectional ties, and $x _ { i j } ^ { t } = 0$ if there is no social tie from $v _ { i }$ to $v _ { j }$ until time t. The strength $\boldsymbol { x } _ { i j } ^ { t }$ of a social tie can be gauged as the aggregated intensity of actions through the tie by time t (Kossinets and Watts 2006). Using the aforementioned mobile phone social network as an example, $\boldsymbol { x } _ { i j } ^ { t }$ can be measured as the average communication time between $v _ { i }$ and $v _ { j }$ by time $t ,$ and $x _ { i j } ^ { t } = 0$ if there is no communication between the entities until time t.

We measure social entity $\boldsymbol { v } _ { i } ^ { \prime } \mathbf { s }$ power of social influence (hereafter influence power) on entity $v _ { j }$ at time $t ,$ $I _ { i j } ^ { t } ,$ using the strength $\boldsymbol { x } _ { i j } ^ { t }$ of the social tie from $v _ { i }$ to $v _ { j } ,$ and we have

$$
I _ {i j} ^ {t} = \frac {x _ {i j} ^ {t} - x _ {\mathrm{min}}}{x _ {\mathrm{max}} - x _ {\mathrm{min}}},\tag{2}
$$

where $x _ { \mathrm { m a x } }$ and $x _ { \mathrm { m i n } }$ denote the maximum and the minimum social tie strength, respectively, and normalization helps avoid the dependence of $I _ { i j } ^ { t }$ on the measurement unit of $\boldsymbol { x } _ { i j } ^ { t }$ (Han and Kamber 2006). Equation (2) is congruent with social influence theories: the stronger the tie from $v _ { i }$ to $v _ { j } ,$ the more powerful $\boldsymbol { v } _ { i } ^ { \prime } \mathbf { s }$ influence on $\boldsymbol { v } _ { j } ^ { \prime } \mathbf { s }$ adoption decision (Levy 1992, Levy and Nail 1993).

Social entities $v _ { i } \in V$ and $v _ { i } \in V$ are structurally equivalent if the following condition is satisfied (Wasserman and Faust 1994): for each $v _ { z } \in V \backslash \{ v _ { i } , v _ { i } \}$ whenever there is a social tie from $v _ { i }$ to $v _ { z } ,$ there is also a social tie from $v _ { j }$ to $v _ { z } ;$ moreover, whenever there is a social tie from v to $v _ { i } ,$ there is also a social tie from $v _ { z }$ to $v _ { j } .$ . Perfect structural equivalence is rare in real-world social networks (Wasserman and Faust 1994). Therefore, structural equivalence between social entities is measured as the extent to which they are structurally equivalent (Wasserman and Faust 1994). A common measure of structural equivalence is the Euclidean distance measure (Burt 1976). Let $y _ { i j } ^ { t }$ be the Euclidean distance of structural equivalence between social entities $v _ { i }$ and $v _ { j }$ at time t. According to Burt (1976) and Wasserman and Faust (1994), for a social network with directional social ties, $y _ { i j } ^ { t }$ is calculated as

$$
y _ {i j} ^ {t} = \sqrt {\sum_ {v _ {z} \in V \backslash \{v _ {i} , v _ {j} \}} [ (l _ {i z} ^ {t} - l _ {j z} ^ {t}) ^ {2} + (l _ {z i} ^ {t} - l _ {z j} ^ {t}) ^ {2} ]};\tag{3}
$$

whereas for a social network with nondirectional social ties, $y _ { i j } ^ { t }$ is evaluated as

$$
y _ {i j} ^ {t} = \sqrt {\sum_ {v _ {z} \in V \backslash \{v _ {i} , v _ {j} \}} (l _ {i z} ^ {t} - l _ {j z} ^ {t}) ^ {2}},\tag{4}
$$

where $l _ { a b } ^ { t } = 1$ if there is a social tie from $v _ { a }$ to $v _ { b }$ by time $t ,$ and $l _ { a b } ^ { t } = 0$ otherwise. Online Appendix $_ { \mathrm { A . 1 } }$ illustrates the calculation of $y _ { i j } ^ { t }$ . (The online appendix is available at http://dx.doi.org/10.1287/isre.1120 .0461.) The higher the value of $y _ { i j } ^ { t } ,$ the less structural equivalence between $v _ { i }$ and $v _ { j } .$ . Accordingly, we evaluate social entity $\boldsymbol { v } _ { i } ^ { \prime } \mathbf { s }$ power of structural equivalence (hereafter equivalence power) on entity $v _ { j }$ at time $t , E _ { i j } ^ { t } .$ as the following:

$$
E _ {i j} ^ {t} = \frac {y _ {\mathrm{max}} - y _ {i j} ^ {t}}{y _ {\mathrm{max}} - y _ {\mathrm{min}}},\tag{5}
$$

where $y _ { \mathrm { m a x } }$ and $y _ { \mathrm { m i n } }$ denote the maximum and the minimum Euclidean distance of structural equivalence, respectively. According to (5), the higher the structural equivalence between $v _ { i }$ and $v _ { j }$ (i.e., lower $y _ { i j } ^ { t } )$ , the more powerful $\boldsymbol { v } _ { i } ^ { \prime } \mathbf { s }$ impact on $v _ { j } ^ { \prime } s$ adoption decision (through $v _ { i } ^ { \prime } \mathbf { s }$ equivalence power on $v _ { j } )$ , consistent with structural equivalence theories (Burt 1987).

Entity similarity can be assessed with the distance between entity characteristics (Hand et al. 2001). A social entity is described by its intrinsic characteristics, which include time-invariant characteristics such as gender and time-variant characteristics such as behavioral characteristics. We thus represent the intrinsic characteristics of a social entity $v _ { i }$ at time t using a time-dependent vector ${ \bf { c } _ { i } ^ { t } . }$ Let $d _ { i j } ^ { t }$ be the distance between intrinsic characteristics of $v _ { i }$ and those of $v _ { j }$ at time t. According to Hand et al. (2001), we have

$$
d _ {i j} ^ {t} = \mathrm{dis} (\mathbf {c _ {i} ^ {t}}, \mathbf {c _ {j} ^ {t}}),\tag{6}
$$

where $\mathbf { c _ { i } ^ { t } }$ and ${ \bf c _ { i } ^ { t } }$ are the respective characteristic vector of $v _ { i }$ and $v _ { j }$ at time $t ,$ dis(.) is a distance function, and $d _ { i j } ^ { t } \geq 0$ . Intrinsic characteristics of social entities differ with applications. As a result, choice of distance function is application specific (Crandall et al. 2008) because some functions are appropriate for realvalued characteristics and others are suitable for a mix of nominal and real-valued characteristics (Han and Kamber 2006). We describe the distance function used in our study in $\ S 4 . \ d _ { i j } ^ { t }$ measures dissimilarity between $v _ { i }$ and $v _ { j } .$ . Hence, the higher the value of $d _ { i j } ^ { t } ,$ the less entity similarity between $v _ { i }$ and $v _ { j }$ . Like equivalence power, social entity $\boldsymbol { v } _ { i } ^ { \prime } \mathbf { s }$ similarity power on entity $v _ { j }$ at time $t , S _ { i j } ^ { t } ,$ , is measured as

$$
S _ {i j} ^ {t} = \frac {d _ {\mathrm{max}} - d _ {i j} ^ {t}}{d _ {\mathrm{max}} - d _ {\mathrm{min}}},\tag{7}
$$

where $d _ { \operatorname* { m a x } }$ and $d _ { \operatorname* { m i n } }$ denote the maximum and the minimum dissimilarity between social entities, respectively. Congruent with theories concerning entity similarity (Ibarra 1992, Centola 2011), we formalize, in Equation $( 7 )$ , that the higher the entity similarity between $v _ { i }$ and $v _ { j } ,$ the more powerful $v _ { i } ^ { \prime } \mathbf { s }$ impact on ${ v _ { j } } ^ { \prime } \{$ s adoption decision, through $v _ { i } ^ { \prime } \mathsf { s }$ similarity power on $v _ { j } .$ . Because confounding factors are generally unobserved, their power on adoption decision (hereafter confounding power) is hidden. However, considering hidden confounding power is crucial, which makes it a principal challenge for predicting adoption probabilities.

## 3. Predicting Adoption Probabilities: Problem Formulation and Proposed Method

We study the problem of predicting adoption probabilities in the context that adoption of an item is diffused among social entities V in a social network over a time horizon $t = 0 , 1 , 2 , \ldots ,$ with 0 being the start of the time horizon. The adopted item (e.g., a particular product) and the unit of time (e.g., week) are application dependent. Under this context, the problem is defined as follows.

Given adoption information observed at current time $T ,$ which includes

(1) adoption decision (i.e., adoption or not) for each social entity in V by T and

(2) adoption time for each social entity who has adopted by $T ,$

predict the probability of adopting at time $T + 1$ for each social entity who has not adopted until T .

To solve the problem, in §3.1, we analyze powers underlying a social entity’s adoption decision based on observed adoption information. A method is then proposed in §3.2 to predict adoption probabilities.

## 3.1. Analysis of Powers Underlying Adoption Decision

Let $V _ { A } ^ { t }$ denote the set of social entities who have adopted by time t and $V _ { N } ^ { t }$ represent the set of social entities who have not adopted until time t. Formally, $V _ { A } ^ { t } = \{ v _ { m } \mid v _ { m } \in V , \tau _ { m } \leq t$ and $V _ { N } ^ { t } = V \backslash V _ { A } ^ { t }$ , where $\tau _ { m }$ is the adoption time of $v _ { m }$ . According to prevalent diffusion models in social networks (Granovetter 1978, Kleinberg 2007), a social entity’s adoption decision is affected by other social entities who have already adopted. Hence, a social entity $v _ { j } ^ { \prime } \mathbf { s }$ adoption decision is affected by social entities in $V _ { A } ^ { t }$ through their influence, equivalence, and similarity powers on $v _ { j } ,$ where $v _ { j } \in \bar { V } _ { N } ^ { t }$ . We thus have

$$
I _ {j} ^ {t} = \sum_ {v _ {i} \in V _ {A} ^ {t}} I _ {i j} ^ {t},\tag{8}
$$

$$
E _ {j} ^ {t} = \sum_ {v _ {i} \in V _ {A} ^ {t}} E _ {i j} ^ {t},\tag{9}
$$

$$
S _ {j} ^ {t} = \sum_ {v _ {i} \in V _ {A} ^ {t}} S _ {i j} ^ {t},\tag{10}
$$

where $I _ { j } ^ { t } \geq 0 , E _ { j } ^ { t } \geq 0 ,$ , and $S _ { j } ^ { t } \geq 0$ denote the total influence, total equivalence, and total similarity power on $v _ { j }$ at time $t ,$ respectively; $I _ { i j } ^ { t } , \ E _ { i j } ^ { t } ,$ and $S _ { i j } ^ { t }$ are given in Equations (2), (5), and (7), respectively.

Receiving the powers defined in Equations (8)–(10) and the hidden confounding power at time $t , v _ { j }$ may become an adopter or still be an nonadopter at time t + 1.

We are ready to construct training data for learning adoption probabilities by analyzing the various powers from observed adoption information. At current time $T ,$ we observe the set $V _ { A } ^ { T }$ of social entities who have adopted by $T$ and their adoption times as well as the set $V _ { N } ^ { T }$ of social entities who have not adopted until T . $V _ { N } ^ { T }$ consists of all social entities that have not adopted until $T ;$ that is, $V _ { N } ^ { T } = V \backslash V _ { A } ^ { T }$ . The algorithm shown in Figure 1 is developed to construct training data from observed adoption information. Two for-loops constitute the algorithm. The first for-loop computes, for each adopter in $V _ { A } ^ { T } .$ , the total influence, equivalence, and similarity power that affect the adopter’s decision of adoption. The second for-loop calculates, for each nonadopter in $V _ { N } ^ { T } .$ , the total influence, equivalence, and similarity power received by the nonadopter at time T − 1, which affect the nonadopter’s decision at time T (i.e., the latest observable decision of the nonadopter). An illustration of the algorithm is provided in Appendix A.2.

## 3.2. Predicting Adoption Probabilities

Using the algorithm shown in Figure 1, we construct training data TRAIN from adoption information

Figure 1 Constructing Training Data from Observed Adoption Information

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Construct_train (T,  $V_{A}^{T}$ ,  $\{\tau_{k}\}$ ,  $V_{N}^{T}$ )
    T: current time
    $V_{A}^{T}$ : set of adopters by T
    $\tau_{k}$ : adoption time of  $v_{k} \in V_{A}^{T}$ $V_{N}^{T}$ : set of nonadopters by T

    // Initialization
    clock = 0.    //clock: clock time evolving from 0 to T
    $V_{clk} = \phi$ .    // $V_{clk}$ : set of adopters with adoption time equals to clock
    $V_{early} = \phi$ .    // $V_{early}$ : set of adopters with adoption time less than clock
    TRAIN =  $\phi$ .    //TRAIN: training data
Sort social entities in  $V_{A}^{T}$  by their adoption time from the earliest to the latest.
For each  $v_{k} \in V_{A}^{T}$  //from the earliest adopter to the latest adopter
If ( $\tau_{k} &gt; clock$ )
    $V_{early} = V_{early} \cup V_{clk}$ .
    $V_{clk} = \phi$ .
    clock =  $\tau_{k}$ .
End if
    $V_{clk} = V_{clk} \cup \{v_{k}\}$ .
    $I_{k}^{\tau_{k}-1} = \sum_{v_{i} \in V_{early}} I_{ik}^{\tau_{k}-1}$ .    //by (8),  $I_{k}^{\tau_{k}-1}$ : total influence power on  $v_{k}$  at time  $\tau_{k}-1$ $E_{k}^{\tau_{k}-1} = \sum_{v_{i} \in V_{early}} E_{ik}^{\tau_{k}-1}$ . //by (9),  $E_{k}^{\tau_{k}-1}$ : total equivalence power on  $v_{k}$  at time  $\tau_{k}-1$ $S_{k}^{\tau_{k}-1} = \sum_{v_{i} \in V_{early}} S_{ik}^{\tau_{k}-1}$ . //by (10),  $S_{k}^{\tau_{k}-1}$ : total similarity power on  $v_{k}$  at time  $\tau_{k}-1$ $A_{k}^{\tau_{k}} = 1$ .    //  $A_{k}^{\tau_{k}}: v_{k}'s$  adoption decision at  $\tau_{k}$ 
    (1 - adoption; 0 - non-adoption)
    TRAIN = TRAIN ∪ {⟨Iₖ⁻¹, Eₖ⁻¹, Sₖ⁻¹, Aₖ⁻¹⟩}.
End for
For each  $v_{j} \in V_{N}^{T}$ $I_{j}^{T-1} = \sum_{v_{i} \in V_{early}} I_{ij}^{T-1}$ .    //by (8),  $I_{j}^{T-1}$ : total influence power on  $v_{j}$  at time T-1
    $E_{j}^{T-1} = \sum_{v_{i} \in V_{early}} E_{ij}^{T-1}$ .    //by (9),  $E_{j}^{T-1}$ : total equivalence power on  $v_{j}$  at time T-1
    $S_{j}^{T-1} = \sum_{v_{i} \in V_{early}} S_{ij}^{T-1}$ . //by (10),  $S_{j}^{T-1}$ : total similarity power on  $v_{j}$  at time T-1
    $A_{j}^{T} = 0.$ .    //  $A_{j}^{T}: v'j's$  adoption decision at T
    (1 - adoption; 0 - non-adoption)
    TRAIN = TRAIN ∪ {⟨Iⱼ⁻¹, Eⱼ⁻¹, Sⱼ⁻¹, Aⱼ⁻¹⟩}.
End for
Return TRAIN.
observed at current time T. For a social entity  $v_{q}$ , who has not adopted until T, influence  $I_q$ , equivalence  $E_q$ , and similarity  $S_q$  power on  $v_q$  at time T can be calculated according to Equations (8)-(10):
</div>

$$
\begin{array}{l} I _ {q} = \sum_ {v _ {i} \in V _ {A} ^ {T}} I _ {i q} ^ {T}, \\ E _ {q} = \sum_ {v _ {i} \in V _ {A} ^ {T}} E _ {i q} ^ {T}, \\ S _ {q} = \sum_ {v _ {i} \in V _ {A} ^ {T}} S _ {i q} ^ {T}. \end{array}
$$

Our objective is to learn from TRAIN the probability $P ( A _ { q } = \mathrm { \large { 1 } } \mid I _ { _ q } , E _ { q } , S _ { q } , H _ { q } )$ of $v _ { q }$ adopting at time $T + \mathsf { \bar { 1 } }$

Figure 2 Predicting Adoption Probability $P ( A _ { q } = 1 | I _ { q } , E _ { q } , S _ { q } , H _ { q } )$  
![](/api/attachments/E72QBRNR/fulltext/images/fb96ae33a1825ce6e898a90fcf123137d3ad917c41de4a1eb4dd80375dca933e.jpg)  
$\left( \mathrm { i . e . , ~ } A _ { q } = 1 \right)$ conditioning on influence $I _ { q } ,$ equivalence $E _ { q } ,$ similarity $S _ { q } ,$ and hidden confounding $H _ { q }$ power on $v _ { q }$ at time $T . ^ { 3 }$ To achieve this objective, as illustrated in Figure 2, we face two major difficulties: (1) each record of TRAIN only consists of influence (I), equivalence (E), similarity (S) power, and adoption decision (A) but is missing hidden confounding power (H), and hence TRAIN is incomplete, and (2) hidden confounding power $H _ { q }$ on $v _ { q }$ is also missing. In this subsection, we discuss how we tackle these difficulties.

Applying Bayes rule, we have

$$
\begin{array}{c} P (A _ {q} = 1 \mid I _ {q}, E _ {q}, S _ {q}, H _ {q}) \\ = \frac {P (A _ {q} = 1) P (I _ {q} , E _ {q} , S _ {q} , H _ {q} \mid A _ {q} = 1)}{\sum_ {a = 0 , 1} P (A _ {q} = a) P (I _ {q} , E _ {q} , S _ {q} , H _ {q} \mid A _ {q} = a)}. \end{array}\tag{11}
$$

To compute $P ( A _ { q } = 1 \mid I _ { q } , E _ { q } , S _ { q } , H _ { q } )$ , each component in the right-hand side of (11) needs to be learned from TRAIN. Suppose we have data on confounding power, a natural way to learn these components is the Naïve Bayes method (Mitchell 1997), which has been shown to have several attractive properties such as computational efficiency and good classification performance (Domingos and Pazzani 1997, Friedman 1997, Hastie et al. 2001). Note that we face the reality of not having data on confounding power in §3.2.1. The Naïve Bayes method makes a conditional independence assumption (Mitchell 1997); in our case, the method assumes that $I _ { q } , E _ { q } , S _ { q } ,$ , and $H _ { q }$ are independent given $A _ { q } ,$ and we thus obtain

$$
\begin{array}{r l} & P (A _ {q} = 1 \mid I _ {q}, E _ {q}, S _ {q}, H _ {q}) \\ & \quad = \big (P (A _ {q} = 1) P (I _ {q} \mid A _ {q} = 1) P (E _ {q} \mid A _ {q} = 1) \\ & \qquad \cdot P (S _ {q} \mid A _ {q} = 1) P (H _ {q} \mid A _ {q} = 1) \big) \end{array}
$$

$$
\begin{array}{c} \cdot \left(\sum_ {a = 0, 1} P (A _ {q} = a) P (I _ {q} \mid A _ {q} = a) P (E _ {q} \mid A _ {q} = a) \right. \\ \left. \cdot P (S _ {q} \mid A _ {q} = a) P (H _ {q} \mid A _ {q} = a)\right) ^ {- 1}. \end{array} \tag {3}\tag{12}
$$

Let us first consider how to estimate $P ( I _ { q } \mid A _ { q } = a )$ in (12), where $a = 0 , 1$ . For Naïve Bayes learning, representing a continuous input with an exponential family distribution $( \mathrm { e . g . , }$ normal or exponential distribution) is a common approach (Mitchell 1997). Because influence power I is continuous-valued and $I \geq 0$ , we assume an exponential distribution for I given adoption decision a and estimate $P ( I _ { q } \mid A _ { q } = a )$ as the density at $I _ { q }$ (Mitchell 1997). That is, given a, I follows an exponential distribution with density $f ( x ) = \lambda _ { I | a } \exp ( - \lambda _ { I | a } x ) , x \geq 0 .$ , where $\lambda _ { I \mid a }$ is the density parameter and $a = 0 , 1$ $P ( I _ { q } \mid A _ { q } \stackrel { . } { = } a )$ can then be estimated as $f ( I _ { q } )$ . We can estimate $P ( E _ { q } \mid A _ { q } = a )$ $P ( S _ { q } \mid A _ { q } = a )$ , and $P ( H _ { q } \mid A _ { q } = a )$ in the same way. Therefore, to compute $\overset { \prime } { P } ( A _ { q } ^ { ' } = 1 \mid I _ { q } , E _ { q } , S _ { q } , H _ { q } )$ , we need to learn from TRAIN the following vector È of parameters:

$$
\pmb {\theta} = \left\langle p _ {1}, \lambda_ {I | 1}, \lambda_ {E | 1}, \lambda_ {S | 1}, \lambda_ {H | 1} p _ {0}, \lambda_ {I | 0}, \lambda_ {E | 0}, \lambda_ {S | 0}, \lambda_ {H | 0} \right\rangle
$$

where $p _ { a }$ is the estimate of prior probability $P ( A _ { q } = a )$ and $\lambda _ { I | a } , \lambda _ { E | a } , \lambda _ { S | a } ,$ and $\lambda _ { H \mid a }$ are respective density parameter for influence power $I ,$ equivalence power $E ,$ similarity power $S ,$ and hidden confounding power H given adoption decision a, $a = 0 ,$ 1 1. In §3.2.1, we show how to learn È by addressing the difficulty of incomplete TRAIN; we discuss in §3.2.2 how to inference adoption probability $P ( A _ { q } =$ $1 \mid I _ { q } , E _ { q } , S _ { q } , H _ { q } )$ by tackling the difficulty of hidden confounding power $H _ { q } .$

3.2.1. Learning È. Two obstacles arise when computing $P ( A _ { q } = 1 | \breve { I _ { q } } , E _ { q } , S _ { q } , H _ { q } )$ using (12). One is associated with learning È. Because confounding power is hidden, we have no data in TRAIN for learning $\lambda _ { H \mid a }$ directly. How can we learn $\mathbf { \delta } _ { \mathbf { \theta } } \mathbf { \delta } _ { \mathbf { \theta } }$ especially $\lambda _ { H \mid a } ,$ from incomplete TRAIN? The second is related to the strong assumption of conditional independence by the Naïve Bayes method. How can we preserve the nice properties of the Naïve Bayes method such as computational efficiency while at the same time relax its strong assumption of conditional independence? To overcome these obstacles, we propose a method based on the classical expectation-maximization (EM) framework (Dempster et al. 1977) and the local learning theory (Atkeson et al. 1997), which are described in the following. The EM framework, developed by Dempster et al. (1977), is a widely used framework for learning from incomplete data (Bishop 2006). It is an iterative procedure starting from an initial parameter estimation (Bishop 2006). Each iteration of EM consists of the expectation step based on current parameter estimation and the maximization step, which maximizes the expectation and computes a revised parameter estimation (Bishop 2006). Whereas regular learning employs all training data and treats each record of training data indifferently, local learning focuses on the region of training data close to the test record and weights each record of training data according to its distance to the test record (Atkeson et al. 1997). It has been shown that violations of the conditional independence assumption could be mitigated by focusing on the region of training data close to the test record (Frank et al. 2003). It is therefore appealing to integrate local learning with the Naïve Bayes method, thereby preserving the method’s nice properties while relaxing the method’s strong assumption to some extent.

Although our method is built upon the EM framework and the local learning theory, prior EM and local learning methods cannot conquer the two obstacles in our study. First, as Bishop (2006) points out, EM is a framework and its application to a problem under analysis requires problem-specific details to be defined and solved. To apply EM to our problem, we need to define the objective function to maximize and figure out how to maximize the objective function. Second, existing local learning methods are primarily developed for learning problems with observed variables. Thus, hidden confounding power poses a unique challenge for our problem: how do we develop a locally weighted Naïve Bayes method in the presence of a hidden variable? Finally, how to integrate EM and local learning techniques to address both obstacles in one method? In response, we propose the locally weighted EM method for Naïve Bayes learning.

Our proposed method learns È using maximum likelihood estimation. Let a record in TRAIN be $\langle I _ { i } , E _ { i } , S _ { i } , A _ { i } \rangle$ , where $i = 1 , 2 , \dots , n$ and n is the number of records in TRAIN. We denote hidden confounding power for record i as $H _ { i } .$ Let D be complete training data and its record is $D _ { i } = \langle I _ { i } , E _ { i } , S _ { i } , \boldsymbol { H } _ { i } \rangle _ { \boldsymbol { A } _ { i } } \rangle _ { \mathrm { \scriptscriptstyle ~ + ~ } }$ where $i = 1 , 2 , \dots , n$ . We denote $P ( D \mid \mathbf { \boldsymbol { \theta } } )$ as the likelihood of D given È. According to Mitchell (1997), we have 11

$$
P (D \mid \boldsymbol {\theta}) = \prod_ {i = 1} ^ {n} P (D _ {i} \mid \boldsymbol {\theta}).
$$

Maximum likelihood parameter estimate ${ \bf \delta \theta _ { \mathrm { { M L } } } }$ maximizes $P ( D \mid \mathbf { \theta } )$ (Mitchell 1997). It is typical to maximize l $\Im [ P ( D \mid \mathbf { \boldsymbol { \theta } } ) ]$ instead of $P ( D \mid \mathbf { \boldsymbol { \theta } } )$ because it is normally easier to maximize the former than the latter and parameter estimate maximizing the former also maximizes the latter (Mitchell 1997). We thus have

$$
\boldsymbol {\theta} _ {\mathrm{ML}} = \underset {\boldsymbol {\theta}} {\arg \max} \sum_ {i = 1} ^ {n} \ln [ P (D _ {i} \mid \boldsymbol {\theta}) ].\tag{13}
$$

To mitigate violations of the conditional independency assumption, our method weights records in D differently. Let the weight of record $D _ { i }$ be $W _ { i } .$ . Following the local learning theory (Atkeson et al. 1997), we set $W _ { i }$ higher if the distance between $D _ { i }$ and the test record $\langle \bar { I _ { q } } , E _ { q } , S _ { q } , H _ { q } \rangle$ is smaller. Hence, we have

$$
W _ {i} = K - \underbrace {[ (I _ {i} - I _ {q}) ^ {2} + (E _ {i} - E _ {q}) ^ {2} + (S _ {i} - S _ {q}) ^ {2} + (H _ {i} - H _ {q}) ^ {2} ]} _ {\text { Square   of   the   Euclidean   Distance }},\tag{14}
$$

where the distance between $D _ { i }$ and the test record is measured as the square of the Euclidian distance between $D _ { i }$ and the test record and K is a constant. We note that both $H _ { i }$ and $H _ { q }$ in (14) are hidden. Having introduced weight $W _ { i } ,$ , our objective becomes maximizing the weighted likelihood of $D .$ That is, we want to find weighted maximum likelihood parameter estimate ${ \Theta } _ { \mathrm { W M L } }$ such that

$$
\boldsymbol {\theta} _ {\mathrm{WML}} = \arg \max _ {\boldsymbol {\theta}} \sum_ {i = 1} ^ {n} W _ {i} \ln [ P (D _ {i} \mid \boldsymbol {\theta}) ].\tag{15}
$$

It is difficult to maximize (15) directly because hidden variables exist in both $W _ { i }$ and $P ( D _ { i } \mid \mathbf { \boldsymbol { \theta } } )$

Following the EM framework (Dempster et al. 1977, Bishop 2006), instead of maximizing the weighted likelihood of $D ,$ our method maximizes the expected weighted likelihood of D given current parameter estimate È<sup>¯</sup>, where

$$
\bar {\pmb {\theta}} = \bigl \langle \bar {p} _ {1}, \bar {\lambda} _ {I | 1}, \bar {\lambda} _ {E | 1}, \bar {\lambda} _ {S | 1}, \bar {\lambda} _ {H | 1}, \bar {p} _ {0}, \bar {\lambda} _ {I | 0}, \bar {\lambda} _ {E | 0}, \bar {\lambda} _ {S | 0}, \bar {\lambda} _ {H | 0} \bigr \rangle .
$$

We will discuss how to set $\bar { \bf { \otimes } }$ after Theorem 2. Let $f ( H _ { q } \mid \bar { \boldsymbol { \Theta } } )$ be probability density function of $H _ { q }$ given È<sup>¯</sup> and $f ( H _ { i } \mid A _ { i } , \bar { \boldsymbol { \Theta } } )$ be probability density function of $H _ { i }$ given $A _ { i }$ and È<sup>¯</sup>. Given È<sup>¯</sup>, the expected weighted likelihood of $D ,$ expected on hidden variables $H _ { i }$ and $H _ { q } ,$ is expressed as

$$
\begin{array}{l} E _ {H _ {i}, H _ {q} | \bar {\boldsymbol {\theta}}} \Bigg \{\sum_ {i = 1} ^ {n} W _ {i} \ln [ P (D _ {i} | \boldsymbol {\theta}) ] \Bigg \} \\ = \sum_ {i = 1} ^ {n} \iint \underbrace {[ K - C _ {i} - (H _ {i} - H _ {q}) ^ {2} ]} _ {W _ {i}} \ln [ P (D _ {i} | \boldsymbol {\theta}) ] \\ \quad \cdot f (H _ {i} | A _ {i}, \bar {\boldsymbol {\theta}}) f (H _ {q} | \bar {\boldsymbol {\theta}}) d _ {H _ {i}} d _ {H _ {q}}, \end{array}\tag{16}
$$

where expected weight ${ \cal E } _ { H _ { i } , H _ { q } | \bar { \bf \theta } } [ W _ { i } ] > 0$ for all $i =$ $1 , 2 , \ldots , n ,$

$$
\begin{array}{r l} E _ {H _ {i}, H _ {q} \mid \bar {\boldsymbol {\theta}}} [ W _ {i} ] = & \iint [ K - C _ {i} - (H _ {i} - H _ {q}) ^ {2} ] f (H _ {i} \mid A _ {i}, \bar {\boldsymbol {\theta}}) \\ & \cdot f (H _ {q} \mid \bar {\boldsymbol {\theta}}) d _ {H _ {i}} d _ {H _ {q}}, \end{array} \tag {1}\tag{17}
$$

$$
C _ {i} = (I _ {i} - I _ {q}) ^ {2} + (E _ {i} - E _ {q}) ^ {2} + (S _ {i} - S _ {q}) ^ {2}.\tag{18}
$$

We set K adequately such that ${ \cal E } _ { H _ { i } , H _ { q } | \bar { \bf \theta } } [ W _ { i } ] > 0$ for all $i = 1 , 2 , \dots , n ,$ and we set

$$
K = C _ {i} ^ {\mathrm{max}} + \frac {2}{\bar {\lambda} _ {H | 0} ^ {2}} + \frac {2}{\bar {\lambda} _ {H | 1} ^ {2}},\tag{19}
$$

where $C _ { i } ^ { \mathrm { m a x } }$ represents the maximum among all $C _ { i } ,$ $i = 1 , 2 , \dots , n ,$ and $\bar { \lambda } _ { H \mid 0 } ^ { 2 }$ and $\bar { \lambda } _ { H \mid 1 } ^ { 2 }$ denote the square of $\bar { \lambda } _ { H \mid 0 }$ and $\bar { \lambda } _ { H \mid 1 }$ , respectively. Derivation of (19) is given in Appendix B.

We want to find È<sup>ˆ</sup> that maximizes the expected weighted likelihood of D expressed in (16). That is,

$$
\hat {\boldsymbol {\theta}} = \arg \max _ {\boldsymbol {\theta}} E _ {H _ {i}, H _ {q} | \bar {\boldsymbol {\theta}}} \left\{\sum_ {i = 1} ^ {n} W _ {i} \ln [ P (D _ {i} | \boldsymbol {\theta}) ] \right\},\tag{20}
$$

where

$$
\hat {\boldsymbol {\theta}} = \langle \hat {p} _ {1}, \hat {\lambda} _ {I | 1}, \hat {\lambda} _ {E | 1}, \hat {\lambda} _ {S | 1}, \hat {\lambda} _ {H | 1}, \hat {p} _ {0}, \hat {\lambda} _ {I | 0}, \hat {\lambda} _ {E | 0}, \hat {\lambda} _ {S | 0}, \hat {\lambda} _ {H | 0} \rangle .
$$

To maximize (20), we show in Theorem 1 that the Hessian matrix of ${ \cal E } _ { H _ { i } , H _ { a } | \bar { \bf \theta } } \{ \sum _ { i = 1 } ^ { n } W _ { i } \ln [ P ( D _ { i } | \bf \theta ) ] \}$ 9 is negative definite, which satisfies the sufficient condition to maximize a multivariable function (Greene 2008); we further show in Theorem 2 the necessary condition (Greene 2008) that all first-order partial derivatives of ${ \cal E } _ { H _ { i } , H _ { q } | \bar { \bf { \theta } } } \{ \sum _ { i = 1 } ^ { \bar { n } } W _ { i } \ln [ P ( D _ { i } | { \bf { \theta } } { \bf { \theta } } ) ] \}$ equal to 0 is met and give closed form solution for each parameter in $\hat { \bf { \theta } }$

<sup>Theorem</sup> <sup>1.</sup> The Hessian matrix of

$$
E _ {H _ {i}, H _ {q} | \bar {\boldsymbol {\theta}}} \left\{\sum_ {i = 1} ^ {n} W _ {i} \ln [ P (D _ {i} | \boldsymbol {\theta}) ] \right\}
$$

is negative definite.

<sup>Proof.</sup> See Appendix C.1.

Theorem 2. <sub>Given</sub> $\bar { \mathbf { 6 } } ,$ parameters in $\hat { \bf { \theta } }$ that maximize the expected weighted likelihood of D are derived as below,

$$
\hat {p} _ {1} = \frac {\sum_ {i = 1} ^ {n} A _ {i} Q _ {i}}{\sum_ {i = 1} ^ {n} [ A _ {i} Q _ {i} + (1 - A _ {i}) R _ {i} ]},\tag{21}
$$

$$
\hat {\lambda} _ {I | 1} = \frac {\sum_ {i = 1} ^ {n} A _ {i} Q _ {i}}{\sum_ {i = 1} ^ {n} A _ {i} I _ {i} Q _ {i}},\tag{22}
$$

$$
\hat {\lambda} _ {E | 1} = \frac {\sum_ {i = 1} ^ {n} A _ {i} Q _ {i}}{\sum_ {i = 1} ^ {n} A _ {i} E _ {i} Q _ {i}},\tag{23}
$$

$$
\hat {\lambda} _ {S | 1} = \frac {\sum_ {i = 1} ^ {n} A _ {i} Q _ {i}}{\sum_ {i = 1} ^ {n} A _ {i} S _ {i} Q _ {i}},\tag{24}
$$

$$
\begin{array}{l}\hat {\lambda} _ {H | 1} = \left(\sum_ {i = 1} ^ {n} A _ {i} \bar {\lambda} _ {H | 1} Q _ {i}\right) \cdot \left(\sum_ {i = 1} ^ {n} A _ {i} \big [ R _ {i} + 2 \bar {\lambda} _ {H | 1} ^ {2} \right.\\\qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad + 2 \bar {p} _ {1} (2 \bar {\lambda} _ {H | 0} ^ {2} + \bar {\lambda} _ {H | 1} ^ {2} - 3 \bar {\lambda} _ {H | 0} \bar {\lambda} _ {H | 1}) - 6 \bar {\lambda} _ {H | 0} ^ {2} ]\left. \right) ^ {- 1},\end{array}\tag{25}
$$

where

$$
\begin{array}{l} Q _ {i} = (K - C _ {i}) \bar {\lambda} _ {H | 0} ^ {2} \bar {\lambda} _ {H | 1} ^ {2} - 2 \bar {\lambda} _ {H | 0} ^ {2} - 2 \bar {p} _ {0} (\bar {\lambda} _ {H | 1} ^ {2} - \bar {\lambda} _ {H | 0} \bar {\lambda} _ {H | 1}), \\ R _ {i} = (K - C _ {i}) \bar {\lambda} _ {H | 0} ^ {2} \bar {\lambda} _ {H | 1} ^ {2} - 2 \bar {\lambda} _ {H | 1} ^ {2} - 2 \bar {p} _ {1} (\bar {\lambda} _ {H | 0} ^ {2} - \bar {\lambda} _ {H | 0} \bar {\lambda} _ {H | 1}). \\ \text {   PROOF.   See   Appendix   C.2.   } \end{array}
$$

In Theorem 2, we only present the parameters for adoption decision equal to 1 but omit those for adoption decision equal to 0 because these two sets of parameters are similar. Please refer to Appendix C.2 for the equations of all parameters. By Theorems 1 and 2, we can compute È<sup>ˆ</sup> from È<sup>¯</sup> and training data TRAIN. Whereas TRAIN is constructed using the algorithm shown in Figure 1, we need to initialize È<sup>¯</sup> . We set $\bar { p } _ { 1 } , \bar { p } _ { 0 } , \bar { \lambda } _ { I | 1 } ^ { \smile } , \bar { \lambda } _ { I | 0 } , \bar { \lambda } _ { E | 1 } , \bar { \lambda } _ { E | 0 } , \bar { \lambda } _ { S | 1 } ,$ , and $\bar { \lambda } _ { S \mid 0 }$ in È<sup>¯</sup> as maximum likelihood estimates of these parameters from TRAIN. The estimates, as shown in Equations (26)–(33), are standard estimates for Naïve Bayes learning, and derivations of them can be found in Mitchell (1997). It is more appropriate to learn the effect of confounding power on parameter estimates from data and adjust parameter estimates accordingly than to set the effect arbitrarily during the initialization of È<sup>¯</sup> . Thus, parameter estimates in (26)–(33) do not consider the following factors: confounding power and weight, which takes confounding power as a component term according to (14). The effect of these factors on parameter estimates will be learned and used to adjust parameter estimates when computing $\hat { \bf { \theta } }$ from È<sup>¯</sup> .

$$
\bar {p} _ {1} = \frac {\sum_ {i = 1} ^ {n} A _ {i}}{n},\tag{26}
$$

$$
\bar {p} _ {0} = 1 - \bar {p} _ {1},\tag{27}
$$

$$
\bar {\lambda} _ {I | 1} = \frac {\sum_ {i = 1} ^ {n} A _ {i}}{\sum_ {i = 1} ^ {n} A _ {i} I _ {i}},\tag{28}
$$

$$
\bar {\lambda} _ {I | 0} = \frac {\sum_ {i = 1} ^ {n} (1 - A _ {i})}{\sum_ {i = 1} ^ {n} (1 - A _ {i}) I _ {i}},\tag{29}
$$

$$
\bar {\lambda} _ {E | 1} = \frac {\sum_ {i = 1} ^ {n} A _ {i}}{\sum_ {i = 1} ^ {n} A _ {i} E _ {i}},\tag{30}
$$

$$
\bar {\lambda} _ {E | 0} = \frac {\sum_ {i = 1} ^ {n} (1 - A _ {i})}{\sum_ {i = 1} ^ {n} (1 - A _ {i}) E _ {i}},\tag{31}
$$

$$
\bar {\lambda} _ {S | 1} = \frac {\sum_ {i = 1} ^ {n} A _ {i}}{\sum_ {i = 1} ^ {n} A _ {i} S _ {i}},\tag{32}
$$

$$
\bar {\lambda} _ {S | 0} = \frac {\sum_ {i = 1} ^ {n} (1 - A _ {i})}{\sum_ {i = 1} ^ {n} (1 - A _ {i}) S _ {i}}.\tag{33}
$$

We consider three possible cases for $\bar { \lambda } _ { H | a } ;$ given adoption decision a, on average, confounding power is the largest, average, or smallest among all powers underlying adoption decision. These cases are modeled using Equations (34)–(36), respectively:

$$
\frac {1}{\bar {\lambda} _ {H | a}} = \max \left(\frac {1}{\bar {\lambda} _ {I | a}}, \frac {1}{\bar {\lambda} _ {E | a}}, \frac {1}{\bar {\lambda} _ {S | a}}\right) \times (1 + \varepsilon_ {1}),\tag{34}
$$

$$
\frac {1}{\bar {\lambda} _ {H | a}} = \frac {(1 / \bar {\lambda} _ {I | a} + 1 / \bar {\lambda} _ {E | a} + 1 / \bar {\lambda} _ {S | a})}{3} \times (1 + \varepsilon_ {2}),\tag{35}
$$

$$
\begin{array}{c} \frac {1}{\bar {\lambda} _ {H | a}} = \min \left(\frac {1}{\bar {\lambda} _ {I | a}}, \frac {1}{\bar {\lambda} _ {E | a}}, \frac {1}{\bar {\lambda} _ {S | a}}\right) \times (1 - \varepsilon_ {3}), \\ a = 0, 1 (\text { smallest   case }) \end{array}\tag{36}
$$

where $1 / \bar { \lambda } _ { H \mid a } , 1 / \bar { \lambda } _ { I \mid a } , 1 / \bar { \lambda } _ { E \mid a } ,$ and $1 / \bar { \lambda } _ { S \mid a }$ are the mean of confounding, influence, equivalence, and similarity power, respectively. Random terms $\varepsilon _ { 1 } , \varepsilon _ { 2 } ,$ and $\varepsilon _ { 3 }$ introduce randomness into the equations; in our empirical study, we set $\varepsilon _ { 1 }$ and $\varepsilon _ { 3 }$ uniformly distributed over (01 0001) and $\varepsilon _ { 2 }$ uniformly distributed over (−0.005, 0.005). Rather than choosing a case arbitrarily, we consider all three cases and let data decide which case is most appropriate. Therefore, three different initializations of È<sup>¯</sup> are set: Equations (26)–(33) and (34), Equations (26)–(33) and (35), and Equations (26)–(33) and (36).

We propose the locally weighted EM method for Naïve Bayes learning (LEMNB) in Figure 3. The method learns parameter estimate È<sup>ˆ</sup> from TRAIN for a social entity receiving influence $I _ { q } ,$ equivalence $E _ { q } ,$

## Figure 3 The Locally Weighted EM Method for Naïve Bayes Learning (LEMNB)

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
LEMNB (M, N,  $I_{q}$ ,  $E_{q}$ ,  $S_{q}$ )
M: number of bootstrap samples
N: number of trials
 $I_{q}$ ,  $E_{q}$ ,  $S_{q}$ : influence, equivalence, similarity power
Create M bootstrap samples from TRAIN:  $TRAIN_{1}$ ,
 $TRAIN_{2}$ , ...,  $TRAIN_{M}$ .
For k = 1 to 3 step 1
    For h = 1 to N step 1
    TRAIN =  $TRAIN_{1}$ .
    Generate random term  $\varepsilon_{1}$ ,  $\varepsilon_{2}$  or  $\varepsilon_{3}$ .
    If (k = 1)
    Initialize  $\bar{\theta}_{kh}$  according to Equations (26)–(33) and (34).
    Else if (k = 2)
    Initialize  $\bar{\theta}_{kh}$  according to Equations (26)–(33) and (35).
    Else
    Initialize  $\bar{\theta}_{kh}$  according to Equations (26)–(33) and (36).
    End if
    For j = 2 to M step 1
    TRAIN =  $TRAIN_{j}$ .
    Compute  $\hat{\theta}_{kh}$  from  $\bar{\theta}_{kh}$  and TRAIN according to Theorem 2.
    $E_{kh} = E_{H_{i}, H_{q} | \bar{\theta}_{kh}}\{\sum_{i=1}^{n} W_{i} \ln[P(D_{i} | \hat{\theta}_{kh})]\}$ .
    If (j &lt; M)
    $\bar{\theta}_{kh} = \hat{\theta}_{kh}$ .
    End if
    End for
    End for
    $\hat{\theta}_{k} = \sum_{h=1}^{N} \hat{\theta}_{kh}/N.$ $E_{k} = \sum_{h=1}^{N} E_{kh}/N.$ 
End for
 $\hat{\theta} = \hat{\theta}_{k}$  with the largest  $E_{k}$  for k = 1, 2, 3.
Return  $\hat{\theta}$ .
</div>

Figure 4 Computing $\hat { \mathbf { \theta } } _ { k h }$

![](/api/attachments/E72QBRNR/fulltext/images/b1df5713cc35c435240826be3a57648781e8a49b13ae1f75395b2388ef4947d9.jpg)

and similarity $S _ { q }$ power. LEMNB first creates bootstrap samples form TRAIN.<sup>4</sup> It then loops through the three cases (for-loop on k5. Each case consists of N trials (for-loop on h5. $\bar { \bf { \theta } } _ { \mathbf { k h } }$ denotes hth trial of parameter initialization for case $k .$ For each $\bar { \bf { \otimes } } _ { \mathbf { k h } } ,$ as illustrated in Figure 4, the method computes $\hat { \bf { \theta } } _ { \mathbf { k h } }$ iteratively through bootstrap samples. Bootstrap sampling introduces variations into training data and thus reduces the chance of overfitting. As a byproduct of computing $\widehat { \mathbf { \theta } } _ { \mathbf { k h } } ,$ LEMNB also calculates the maximum expected weighted likelihood $E _ { k h } .$ . For each case, average parameter estimate $\hat { \bf { \theta } } _ { \mathbf { { k } } }$ and average likelihood $E _ { k }$ across N trials are calculated. The most appropriate case is determined as the one with the largest $E _ { k }$ and the parameter estimate $\hat { \bf { \theta } } _ { \mathbf { { k } } }$ of this case is used as the final parameter estimate. We set the number of bootstrap samples M and the number of trials N adequately such that $\hat { \bf { \theta } } _ { \mathbf { k h } }$ and $\hat { \bf { \theta } } _ { \mathbf { { k } } }$ converge.

3.2.2. Inference. Having learned parameter estimate È<sup>ˆ</sup> , inference adoption probability is a relatively easier task. Given parameter estimate $\begin{array} { r } { \hat { \bf { \theta } } = \langle \hat { p } _ { 1 } , \hat { \lambda } _ { I | 1 } , } \end{array}$ $\hat { \lambda } _ { E | 1 } , \hat { \lambda } _ { S | 1 } , \hat { \lambda } _ { H | 1 } , \hat { p } _ { 0 } , \hat { \lambda } _ { I | 0 } ^ { * } , \hat { \lambda } _ { E | 0 } , \hat { \lambda } _ { S | 0 } , \hat { \lambda } _ { H | 0 } \rangle$ , by (12), we have

$$
\begin{array}{l} P (A _ {q} = 1 \mid I _ {q}, E _ {q}, S _ {q}, H _ {q}) \\ \quad = (P (A _ {q} = 1) P (I _ {q} \mid A _ {q} = 1) P (E _ {q} \mid A _ {q} = 1) P (S _ {q} \mid A _ {q} = 1) \\ \quad \cdot P (H _ {q} \mid A _ {q} = 1)) \cdot \bigg (\sum_ {a = 0, 1} P (A _ {q} = a) P (I _ {q} \mid A _ {q} = a) \\ \quad \cdot P (E _ {q} \mid A _ {q} = a) P (S _ {q} \mid A _ {q} = a) \\ \quad \cdot P (H _ {q} \mid A _ {q} = a) \bigg) ^ {- 1} \\ \quad = (\hat {p} _ {1} \hat {\lambda} _ {I | 1} \exp (- \hat {\lambda} _ {I | 1} I _ {q}) \hat {\lambda} _ {E | 1} \exp (- \hat {\lambda} _ {E | 1} E _ {q}) \hat {\lambda} _ {S | 1} \\ \quad \cdot \exp (- \hat {\lambda} _ {S | 1} S _ {q}) \hat {\lambda} _ {H | 1} \exp (- \hat {\lambda} _ {H | 1} H _ {q})) \end{array}
$$

$$
\begin{array}{l} \cdot \left(\sum_ {a = 0, 1} \hat {p} _ {a} \hat {\lambda} _ {I | a} \exp (- \hat {\lambda} _ {I | a} I _ {q}) \hat {\lambda} _ {E | a} \exp (- \hat {\lambda} _ {E | a} E _ {q}) \hat {\lambda} _ {S | a} \right. \\ \left. \cdot \exp (- \hat {\lambda} _ {S | a} S _ {q}) \hat {\lambda} _ {H | a} \exp (- \hat {\lambda} _ {H | a} H _ {q})\right) ^ {- 1}. \end{array} \tag {3}\tag{37}
$$

To compute adoption probability using (37), the only difficulty is the hidden variable ${ \bar { H _ { q } } } .$ However, given È<sup>ˆ</sup>, probability density of $H _ { q }$ is known and we have

$$
\begin{array}{r l} & f (H _ {q} \mid \hat {\pmb {\theta}}) = f (H _ {q} \mid A _ {q} = 1, \hat {\pmb {\theta}}) P (A _ {q} = 1 \mid \hat {\pmb {\theta}}) \\ & \qquad + f (H _ {q} \mid A _ {q} = 0, \hat {\pmb {\theta}}) P (A _ {q} = 0 \mid \hat {\pmb {\theta}}). \end{array}\tag{38}
$$

Therefore, we can approximate adoption probability $P ( A _ { q } = 1 | I _ { q } , E _ { q } , S _ { q } , \bar { H _ { q } } )$ with its expectation on $H _ { q }$ and compute the expectation using Monte Carlo method (Bishop 2006).<sup>5</sup> As shown in Figure 5, the adoption probability inference algorithm repeatedly generates a sample of $H _ { q }$ and calculates adoption probability using the sample and Equation (37) until convergence. The algorithm outputs the expectation of the adoption probability, i.e., expected on $H _ { q } .$

## 4. Empirical Evaluations

We evaluated the proposed method with data from two large-scale social networks. One is a social network of communications among mobile phone users. Mobile communication-based social networks have been used to evaluate theories, methods, or applications in social network research (Pentland 2008; Eagle et al. 2009, 2010). We further examined the proposed method with a virtual world social network—a social network of avatars.<sup>6</sup> This additional evaluation is closely related to online gaming, a fast-growing industry that has been transformed by social media (Zukerman and Albrecht 2001, Hemp 2006). The proposed method could be highly beneficial for marketing virtual items to game players, a fast-growing revenue source for online game service providers. According to PlaySpan (2012), game players in the United States purchased \$2.3 billion worth of virtual items in 2011—nearly 30% growth compared with 2009. By using our method, service providers could more effectively prioritize their marketing efforts and focus on consumers more likely to adopt new virtual products in the next time period. We report evaluation results with the mobile social network in this section. We observe similar evaluation results in the avatar social network and report key findings in Appendix D for space consideration.

## Figure 5 Inferencing Adoption Probability

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Inference ( $\hat{\theta}$ ,  $I_{q}$ ,  $E_{q}$ ,  $S_{q}$ ,  $\sigma$ )

 $\hat{\theta}$ : parameter estimate

 $I_{q}$ ,  $E_{q}$ ,  $S_{q}$ : influence, equivalence, similarity power

 $\sigma$ : predefined convergence threshold

count = 0.

sum = 0.

mean = 0.

Do

pre_mean = mean.

Generate a sample  $h_{q}$  of  $H_{q}$  according to its probability density in (38).

Calculate  $P(A_{q}=1 \mid I_{q}, E_{q}, S_{q}, h_{q})$  using (37).

sum = sum +  $P(A_{q}=1 \mid I_{q}, E_{q}, S_{q}, h_{q})$ .

count = count + 1.

mean = sum/count.

Until  $\left(\frac{|\text{mean} - \text{pre\_mean}|}{\text{mean}} \leq \sigma\right)$ 

Return mean.
</div>

## 4.1. Data and Evaluation Procedure

Our evaluations used data sets collected from a major mobile service provider. One data set consists of 14.7 million records of mobile phone communications among 34,797 users over a one-year period. Each record contains the identifications of the two users connected by a communication and the time and duration of the communication.<sup>7</sup> Another data set contains profiles of the 34,797 users. Each user profile is composed of two time-invariant demographic characteristics, gender and age, and 18 timevariant behavioral characteristics: the frequency of using each of the 18 calling modes offered by the service provider.<sup>8</sup> We also collected data on weekby-week adoption of a mobile service A launched at the beginning of the study period; i.e., who, out of the 34,797 users, adopted the service in which week.<sup>9</sup> Consistent with existing literature (Bass 1969, Iyengar et al. 2011), the week of adopting service A is the week of initial purchase of A. Figure 6 shows weekly adoption rates over the entire study period.<sup>10</sup> On average, 110 users adopted the service in a week, yielding an average weekly adoption rate of 0.42%. The unit of time in our evaluations was week because of weekly adoption data. We thus constructed from data 52 snapshots of the mobile social network, each of which corresponded to the social network by the end of week $t , \ i = 1 , 2 , \dots , 5 2$ . In each snapshot, social entities $\left( v _ { i } \right)$ corresponded to users; a social tie between social entities $v _ { i }$ and $v _ { j }$ was created if there was communication between their corresponding users, and the strength of the social tie $\boldsymbol { x } _ { i j } ^ { t }$ was measured as the average weekly communication time between the users by week $t ;$ and the intrinsic characteristics $\mathbf { c _ { i } ^ { t } }$ of a social entity $v _ { i }$ by week t consisted of the two time-invariant characteristics and the 18 time-variant characteristics.

In an evaluation, we picked a week as current time T . Using social network data and adoption data by the end of week T as training data, we applied the proposed method and eight benchmark methods to predict adoption probability in week $T + 1$ for each social entity who has not adopted by the end of week T . Specifically, we predicted adoption probabilities of social entities that will adopt in week $\bar { T } + 1$ as well as those that will not adopt in week T + 1. Several implementation details of the proposed method warrant descriptions. Because intrinsic characteristics $\mathbf { c _ { i } ^ { t } }$ involve different types of attribute, we employed a standard distance function for measuring the similarity between entities with a mix of nominal, real-valued, and integer attributes (Han and Kamber 2006). For two entities with n attributes, $x =$ $( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ and $y = ( y _ { 1 } , y _ { 2 } , \ldots , y _ { n } )$ , where $x _ { i }$ is the value of the ith attribute for entity $x , i = 1 , 2 , \ldots n ,$ the distance between x and y for each attribute is measured first. Let $d ( x _ { i } , y _ { i } )$ be the distance between x and $y$ for the ith attribute. According to Han and Kamber (2006), if the ith attribute is nominal, $d ( x _ { i } , y _ { i } )$ is given by

$$
d (x _ {i}, y _ {i}) = \left\{ \begin{array}{l l} 0 & \text { if } x _ {i} = y _ {i}, \\ 1 & \text { otherwise }, \end{array} \right.\tag{39}
$$

if the ith attribute is real-valued or integer, $d ( x _ { i } , y _ { i } )$ is

$$
d (x _ {i}, y _ {i}) = \frac {| x _ {i} - y _ {i} |}{\max _ {i} - \min _ {i}},\tag{40}
$$

where max and min denote the maximum value and the minimum value of the ith attribute among all entities, respectively. The distance between x and y then can be computed by integrating their distance on each attribute,

$$
d (x, y) = \frac {\sum_ {i = 1} ^ {n} d (x _ {i} , y _ {i})}{n}.\tag{41}
$$

In Equations (2), (5), and $( 7 ) , x _ { \mathrm { m i n } } , y _ { \mathrm { m i n } } ,$ and $d _ { \mathrm { m i n } }$ were set to $0 ; \ x _ { \mathrm { m a x } } , \ y _ { \mathrm { m a x } } ,$ and $d _ { \operatorname* { m a x } }$ were set to equal the maximum social tie strength, the maximum Euclidean distance of structural equivalence, and the maximum dissimilarity between social entities by the end of week T , respectively. We set M and N in the LEMNB method (Figure 3) to 5 and 20, respectively.

Prior studies of cascade methods are related to our work. Therefore, three cascade methods (Chen et al.

Table 1 Methods Compared in the Evaluations

<table><tr><td>Method</td><td>Abbreviation</td><td>Note</td></tr><tr><td>Locally weighted EM method for Naïve Bayes learning</td><td>LEMNB</td><td>Proposed method</td></tr><tr><td>Cascade methods</td><td>CM1, CM2, CM3</td><td>Benchmark</td></tr><tr><td>Influence probability method</td><td>IP</td><td>Benchmark</td></tr><tr><td>Naïve Bayes</td><td>NB</td><td>Benchmark</td></tr><tr><td>Locally weighted Naive Bayes</td><td>LWNB</td><td>Benchmark</td></tr><tr><td>k-nearest neighbor</td><td>k-NN</td><td>Benchmark</td></tr><tr><td>Support vector machine</td><td>SVM</td><td>Benchmark</td></tr></table>

2009), namely CM1, CM2, and CM3, were benchmarked. Derived from (1), a cascade method computes the probability $p _ { v }$ of v adopting in week $T + 1$ as

$$
p _ {v} = 1 - (1 - p) ^ {l},\tag{42}
$$

where l is the number of v’s neighbors who adopt in week $T ; p$ is set to $1 / k , 0 . 1$ , and 0.01, respectively, by CM1, CM2, and CM3 (Chen et al. 2009, Kempe et al. 2003); and k is the number of neighbors of v in week T . We also compared the proposed method with the influence probability method (Goyal et al. 2010), which calculates adoption probabilities with Equation (1) and learns $p _ { u , v }$ in (1) as the ratio between the number of actions propagated from u to v and the total number of actions performed by u. In the context of this study, actions in Goyal et al. (2010) refer to service adoptions. To implement the influence probability method, we gathered additional data regarding weekly adoptions of all other mobile services by the same group of users during the one-year study period and used the additional data to calculate $p _ { u , v } . ^ { 1 1 }$ According to Goyal et al. (2010), if v adopts service B after $u ^ { \prime } \mathrm { s }$ adoption of B and there exists a social tie connecting u and v before $u ^ { \prime } \mathrm { s }$ adoption of $B ,$ adoption of service B is considered to be propagated from u to v. If u adopts services $B , C ,$ , and D, but only B is propagated from u to $v ,$ then $p _ { u , v } = 1 / 3$ (Goyal et al. 2010). We also included representative classification methods as benchmarks. Because the proposed method is built on the Naïve Bayes method and employs local learning techniques, we compared it with the Naïve Bayes method (Mitchell 1997), the locally weighted Naive Bayes method (Frank et al. 2003), and the k-nearest neighbor method (Hand et al. 2001). We also benchmarked against support vector machine (Burges 1998), which has been shown good predictive power among classification methods (Huang and Ling 2005). Table 1 summarizes the methods compared in the evaluations.

Figure 6 Weekly Adoption Rate  
![](/api/attachments/E72QBRNR/fulltext/images/96646fae0b6115d68e8928bc687a8de3cbb47d441ec58fcc012c38ce0842bedf.jpg)

## 4.2. Evaluation Results and Analyses

Following the evaluation procedure, we conducted 50 evaluations to compare the proposed method and the benchmarks, with T ranging from 2 to 51. The performance of each method was evaluated using AUC, i.e., the area under the ROC (Receiver Operating Characteristic) curve (Fawcett 2006). AUC is a standard metric for assessing methods that predict classification probabilities (Huang and Ling 2005). According to Fawcett (2006), AUC is equivalent to the probability that a randomly chosen positive instance will be predicted to have a higher probability of belonging to the positive class than will a randomly chosen negative instance. In our case, AUC is equivalent to the probability that a randomly chosen adopter will be predicted to have a higher adoption probability than a will randomly chosen nonadopter. Therefore, a method that yields a higher AUC generally offers greater predictive power than a method that produces a lower AUC (Fawcett 2006).

In Table 2, we show AUCs of the proposed method and those of the benchmark methods across 50 evaluations. To examine whether our proposed method outperformed each benchmark method, we conducted the Wilcoxon signed-ranks test (Demsar 2006), which is widely used for comparing the performance of predictive methods on the basis of AUC (Demsar 2006). We applied the Wilcoxon test to the AUCs in Table 2; testing results suggested that the proposed method significantly outperformed each benchmark method $( p < 0 . 0 0 1 )$ ). In addition to demonstrating the superior predictive power of our method over each benchmark method statistically, we also observed substantial AUC improvements by our method over the benchmarks, as shown in Table 2. For example, across all 50 evaluations, the average AUC of our method is 0.8029, whereas that of k-NN is 0.6910.

For k-NN in Table 2, we followed the strategy by Hand et al. (2001) to set the value of k. Specifically, each possible k value was evaluated with 10-fold cross-validation using training data; we selected the k value that yielded the best average AUC across the 10 folds. The SVM method in Table 2 used

RBF kernel (Burges 1998) and was implemented with the standard software package LIBSVM (Chang and Lin 2011). We experimentally tuned the SVM parameters according to the commonly accepted guidelines (Hsu et al. 2003). We also benchmarked our method against SVM with other kernels including linear, polynomial, and sigmoid (Burges 1998). The Wilcoxon testing results suggest our method significantly outperforms SVM with any investigated kernel $( p < \dot { 0 } . 0 0 1 )$ . We do not include detailed AUCs of SVM with linear, polynomial, and sigmoid kernels because of space consideration.

Several observations warrant attention. First, the AUCs of the cascade methods and the influence probability method are barely greater than 0.5, which suggests their predictive power is only marginally higher than that of random guess (Fawcett 2006). The poor performance of these methods partly reflects their exclusive reliance on social influence for adoption probability predictions (Chen et al. 2009, Goyal et al. 2010). Consequently, they predict that the adoption probability of a social entity in week T + 1 is zero if that entity has zero neighbors who adopt in week T , as in Equation (47). Figure 7 shows the percentage of adopters (nonadopters) in week T + 1 who have zero neighbors adopting in week T . Across all 50 evaluations, on average 95.78% of adopters in week T + 1 have zero neighbors who adopt in week T and 98.51% of nonadopters in week T + 1 have zero neighbors who adopt in week T . Therefore, on average, adoption probabilities of 95.78% of adopters and 98.51% of nonadopters are predicted as zero by these benchmark methods; hence, these social entities cannot be differentiated by them, which explains their performance. Low weekly adoption rates (0.42% on average) make these high percentages unsurprising. We note that adoption rates in our data are not uncommon; comparable or lower adoption rates have been reported by prior studies (Aral et al. 2009, Iyengar et al. 2011). Furthermore, similar percentages of adopters (nonadopters) having zero adopter neighbors have also been noted (Aral et al. 2009). The proposed method, on the other hand, considers a more comprehensive set of factors underlying adoption decision; therefore, it can predict adoption probabilities more effectively.

Table 2 Comparative AUC Analyses of Proposed and Benchmark Methods

<table><tr><td>Evaluation week (T+1)</td><td>LEMNB</td><td>CM1</td><td>CM2</td><td>CM3</td><td>IP</td><td>NB</td><td>LWNB</td><td>SVM</td><td>k-NN</td></tr><tr><td>3</td><td>0.8722</td><td>0.5166</td><td>0.5167</td><td>0.5167</td><td>0.5295</td><td>0.5254</td><td>0.7050</td><td>0.8257</td><td>0.6675</td></tr><tr><td>4</td><td>0.8299</td><td>0.5023</td><td>0.5023</td><td>0.5023</td><td>0.5196</td><td>0.8181</td><td>0.6202</td><td>0.7664</td><td>0.7113</td></tr><tr><td>5</td><td>0.8505</td><td>0.5019</td><td>0.5019</td><td>0.5019</td><td>0.5131</td><td>0.7809</td><td>0.6120</td><td>0.7691</td><td>0.6555</td></tr><tr><td>6</td><td>0.8666</td><td>0.5025</td><td>0.5025</td><td>0.5025</td><td>0.5169</td><td>0.8072</td><td>0.6839</td><td>0.7786</td><td>0.7489</td></tr><tr><td>7</td><td>0.8643</td><td>0.5032</td><td>0.5032</td><td>0.5032</td><td>0.5218</td><td>0.8241</td><td>0.6701</td><td>0.7319</td><td>0.7713</td></tr><tr><td>8</td><td>0.8286</td><td>0.5030</td><td>0.5030</td><td>0.5030</td><td>0.5258</td><td>0.8121</td><td>0.5565</td><td>0.6518</td><td>0.7516</td></tr><tr><td>9</td><td>0.8083</td><td>0.5023</td><td>0.5023</td><td>0.5023</td><td>0.5300</td><td>0.7200</td><td>0.7613</td><td>0.7657</td><td>0.7087</td></tr><tr><td>10</td><td>0.8011</td><td>0.5013</td><td>0.5013</td><td>0.5013</td><td>0.5339</td><td>0.7826</td><td>0.6340</td><td>0.6339</td><td>0.7245</td></tr><tr><td>11</td><td>0.8643</td><td>0.5032</td><td>0.5032</td><td>0.5032</td><td>0.5381</td><td>0.8200</td><td>0.7903</td><td>0.5123</td><td>0.7901</td></tr><tr><td>12</td><td>0.7974</td><td>0.5030</td><td>0.5030</td><td>0.5030</td><td>0.5313</td><td>0.7422</td><td>0.7680</td><td>0.5508</td><td>0.6769</td></tr><tr><td>13</td><td>0.8339</td><td>0.5021</td><td>0.5021</td><td>0.5021</td><td>0.5256</td><td>0.7244</td><td>0.8004</td><td>0.6020</td><td>0.6446</td></tr><tr><td>14</td><td>0.8223</td><td>0.5020</td><td>0.5020</td><td>0.5020</td><td>0.5291</td><td>0.7315</td><td>0.7962</td><td>0.6269</td><td>0.7369</td></tr><tr><td>15</td><td>0.8654</td><td>0.5022</td><td>0.5022</td><td>0.5022</td><td>0.5132</td><td>0.8656</td><td>0.6106</td><td>0.8112</td><td>0.7103</td></tr><tr><td>16</td><td>0.7240</td><td>0.5020</td><td>0.5020</td><td>0.5020</td><td>0.5292</td><td>0.7046</td><td>0.6813</td><td>0.6822</td><td>0.6718</td></tr><tr><td>17</td><td>0.7270</td><td>0.5033</td><td>0.5033</td><td>0.5033</td><td>0.5293</td><td>0.7460</td><td>0.7468</td><td>0.6122</td><td>0.6814</td></tr><tr><td>18</td><td>0.8276</td><td>0.5022</td><td>0.5022</td><td>0.5022</td><td>0.5272</td><td>0.7967</td><td>0.7389</td><td>0.7972</td><td>0.7359</td></tr><tr><td>19</td><td>0.8323</td><td>0.5035</td><td>0.5035</td><td>0.5035</td><td>0.5262</td><td>0.8458</td><td>0.7796</td><td>0.8342</td><td>0.7333</td></tr><tr><td>20</td><td>0.7221</td><td>0.5028</td><td>0.5028</td><td>0.5028</td><td>0.5103</td><td>0.7215</td><td>0.7653</td><td>0.6694</td><td>0.6439</td></tr><tr><td>21</td><td>0.7852</td><td>0.5050</td><td>0.5050</td><td>0.5050</td><td>0.5195</td><td>0.7967</td><td>0.7614</td><td>0.7138</td><td>0.6604</td></tr><tr><td>22</td><td>0.8497</td><td>0.5015</td><td>0.5015</td><td>0.5015</td><td>0.5267</td><td>0.8571</td><td>0.8049</td><td>0.7181</td><td>0.7329</td></tr><tr><td>23</td><td>0.7905</td><td>0.5026</td><td>0.5026</td><td>0.5026</td><td>0.5295</td><td>0.7924</td><td>0.7607</td><td>0.7621</td><td>0.6871</td></tr><tr><td>24</td><td>0.7982</td><td>0.5054</td><td>0.5054</td><td>0.5054</td><td>0.5228</td><td>0.7843</td><td>0.7643</td><td>0.7611</td><td>0.6854</td></tr><tr><td>25</td><td>0.7838</td><td>0.5054</td><td>0.5054</td><td>0.5054</td><td>0.5117</td><td>0.7945</td><td>0.7633</td><td>0.7772</td><td>0.6414</td></tr><tr><td>26</td><td>0.8302</td><td>0.5011</td><td>0.5011</td><td>0.5011</td><td>0.5165</td><td>0.8159</td><td>0.7352</td><td>0.6746</td><td>0.7355</td></tr><tr><td>27</td><td>0.7832</td><td>0.5026</td><td>0.5026</td><td>0.5026</td><td>0.5184</td><td>0.7939</td><td>0.7701</td><td>0.8032</td><td>0.6695</td></tr><tr><td>28</td><td>0.7165</td><td>0.5024</td><td>0.5024</td><td>0.5024</td><td>0.5134</td><td>0.7030</td><td>0.7491</td><td>0.6381</td><td>0.6305</td></tr><tr><td>29</td><td>0.7825</td><td>0.5028</td><td>0.5028</td><td>0.5028</td><td>0.5333</td><td>0.7445</td><td>0.7749</td><td>0.6567</td><td>0.6026</td></tr><tr><td>30</td><td>0.7650</td><td>0.5043</td><td>0.5043</td><td>0.5043</td><td>0.5179</td><td>0.7884</td><td>0.7517</td><td>0.7464</td><td>0.6623</td></tr><tr><td>31</td><td>0.6681</td><td>0.5058</td><td>0.5060</td><td>0.5060</td><td>0.5152</td><td>0.6410</td><td>0.6539</td><td>0.6639</td><td>0.6328</td></tr><tr><td>32</td><td>0.7232</td><td>0.5041</td><td>0.5042</td><td>0.5042</td><td>0.5004</td><td>0.6341</td><td>0.6755</td><td>0.6558</td><td>0.6327</td></tr><tr><td>33</td><td>0.7121</td><td>0.5040</td><td>0.5041</td><td>0.5041</td><td>0.5106</td><td>0.6415</td><td>0.6894</td><td>0.6805</td><td>0.6691</td></tr><tr><td>34</td><td>0.6840</td><td>0.5073</td><td>0.5073</td><td>0.5073</td><td>0.5085</td><td>0.6066</td><td>0.6661</td><td>0.6253</td><td>0.5930</td></tr><tr><td>35</td><td>0.7289</td><td>0.5027</td><td>0.5024</td><td>0.5024</td><td>0.5351</td><td>0.6695</td><td>0.6881</td><td>0.5908</td><td>0.6446</td></tr><tr><td>36</td><td>0.7413</td><td>0.5073</td><td>0.5072</td><td>0.5072</td><td>0.5219</td><td>0.6135</td><td>0.6318</td><td>0.6276</td><td>0.6802</td></tr><tr><td>37</td><td>0.7577</td><td>0.5018</td><td>0.5017</td><td>0.5017</td><td>0.5072</td><td>0.5412</td><td>0.5440</td><td>0.5282</td><td>0.5606</td></tr><tr><td>38</td><td>0.7414</td><td>0.5006</td><td>0.5006</td><td>0.5006</td><td>0.5106</td><td>0.5069</td><td>0.5018</td><td>0.5728</td><td>0.6174</td></tr><tr><td>39</td><td>0.6999</td><td>0.5030</td><td>0.5031</td><td>0.5031</td><td>0.5118</td><td>0.5621</td><td>0.6038</td><td>0.6693</td><td>0.6367</td></tr><tr><td>40</td><td>0.8505</td><td>0.5184</td><td>0.5184</td><td>0.5184</td><td>0.5122</td><td>0.6437</td><td>0.5796</td><td>0.8374</td><td>0.6690</td></tr><tr><td>41</td><td>0.7509</td><td>0.5146</td><td>0.5150</td><td>0.5150</td><td>0.5240</td><td>0.5235</td><td>0.5194</td><td>0.5450</td><td>0.7320</td></tr><tr><td>42</td><td>0.7528</td><td>0.5150</td><td>0.5150</td><td>0.5150</td><td>0.5266</td><td>0.5446</td><td>0.5613</td><td>0.7351</td><td>0.7171</td></tr><tr><td>43</td><td>0.8218</td><td>0.5151</td><td>0.5150</td><td>0.5150</td><td>0.5029</td><td>0.5128</td><td>0.5013</td><td>0.7132</td><td>0.7110</td></tr><tr><td>44</td><td>0.8392</td><td>0.5012</td><td>0.5011</td><td>0.5011</td><td>0.5102</td><td>0.6082</td><td>0.5245</td><td>0.7381</td><td>0.7201</td></tr><tr><td>45</td><td>0.8542</td><td>0.5019</td><td>0.5019</td><td>0.5019</td><td>0.5231</td><td>0.7425</td><td>0.5545</td><td>0.7801</td><td>0.6911</td></tr><tr><td>46</td><td>0.8633</td><td>0.5167</td><td>0.5168</td><td>0.5168</td><td>0.5102</td><td>0.7627</td><td>0.5658</td><td>0.7610</td><td>0.7356</td></tr><tr><td>47</td><td>0.8864</td><td>0.5049</td><td>0.5050</td><td>0.5050</td><td>0.5241</td><td>0.8041</td><td>0.5431</td><td>0.7905</td><td>0.7625</td></tr><tr><td>48</td><td>0.8777</td><td>0.5172</td><td>0.5175</td><td>0.5175</td><td>0.5214</td><td>0.8501</td><td>0.5913</td><td>0.7833</td><td>0.7563</td></tr><tr><td>49</td><td>0.8847</td><td>0.5110</td><td>0.5111</td><td>0.5111</td><td>0.5120</td><td>0.8651</td><td>0.5836</td><td>0.8214</td><td>0.7278</td></tr><tr><td>50</td><td>0.8942</td><td>0.5165</td><td>0.5168</td><td>0.5168</td><td>0.5358</td><td>0.8400</td><td>0.5553</td><td>0.7757</td><td>0.7390</td></tr><tr><td>51</td><td>0.8922</td><td>0.5128</td><td>0.5130</td><td>0.5130</td><td>0.5111</td><td>0.8397</td><td>0.6072</td><td>0.7992</td><td>0.7251</td></tr><tr><td>52</td><td>0.8990</td><td>0.5025</td><td>0.5025</td><td>0.5025</td><td>0.5180</td><td>0.8450</td><td>0.5930</td><td>0.7795</td><td>0.7243</td></tr><tr><td>Avg.</td><td>0.8029</td><td>0.5055</td><td>0.5056</td><td>0.5056</td><td>0.5203</td><td>0.7288</td><td>0.6658</td><td>0.7069</td><td>0.6910</td></tr><tr><td>Std.</td><td>0.0625</td><td>0.0053</td><td>0.0053</td><td>0.0053</td><td>0.0091</td><td>0.1072</td><td>0.0939</td><td>0.0876</td><td>0.0503</td></tr></table>

Second, the proposed method outperforms the benchmarked classification methods: NB, LWNB, SVM, and k-NN. The superiority of the proposed method over the benchmarked classification methods can be attributed to the consideration of hidden confounding power by the proposed method but not by the classification methods. Thus, experimental results in Table 2 also highlight the importance of hidden confounding power (and hence confounding factors) for predicting adoption probabilities. Both LWNB and the proposed method are NB-based classification methods. Methodologically, NB (Mitchell 1997) does not use local learning nor consider hidden confounding power; LWNB (Frank et al. 2003) employs local learning but does not consider hidden confounding power. Applying the Wilcoxon test to the AUCs of NB and LWNB, testing results suggest that

Figure 7 Percentage of Zero Neighbors Adopting in Week T  
![](/api/attachments/E72QBRNR/fulltext/images/6fc671d0ce0d76b927d209cc0574fb9851784247c98621a5568c9f18c72270b8.jpg)

NB significantly outperforms LWNB (p < 0001). The performance of local learning methods depends on appropriate weights of training records (Atkeson et al. 1997). For our study, the hidden confounding power is unobserved, and LWNB weights training records using only observed (partial) variables, so training records may not be properly weighted, which could lead to the performance differential we observed. With local learning and consideration of hidden confounding power, the proposed method avoids this problem associated with LWNB and therefore can yield better performance than both NB and LWNB.

Third, as we report in Table 2, the ratio of the standard deviation to the mean for LEMNB is higher than that for cascade methods; however, the ratio for LEMNB is comparable to or lower than that for NB, LWNB, SVM, and k-NN. Note that LEMNB, NB, LWNB, SVM, and k-NN are learning-based predictive methods. These methods learn adoption patterns from training data and then leverage such patterns to predict future adoption behaviors. The deviation between prior adoption patterns and future adoption behaviors might affect the performance of these methods. If the deviation increases, the performance of a learning-based method is likely to decline; if the deviation decreases, its performance could improve. Thus, for LEMNB, NB, LWNB, SVM, and k-NN, we observe their performance varying across 50 evaluation weeks, though on average these methods (especially LEMNB) demonstrate good predictive performance, as suggested by their high average AUC scores. Cascade methods, on the other hand, predict the adoption probability of a social entity in week T + 1 based on his or her neighbors who adopt in week T . As we have discussed, the high percentage of adopters (nonadopters) having zero neighbors adopting in week T explains the poor performance of cascade methods. Thus, although the performance of cascade methods is relatively stable across evaluation weeks, it is stable at a very low performance level. In Appendix E, we plot the AUCs of each method across 50 evaluations.

Our evaluation results with the mobile social network show that the proposed method substantially outperforms all benchmark methods. Similar results emerge from our comparative evaluations with the avatar social network, as we detail in Appendix D. This superior performance derives from our consideration of a more comprehensive set of factors underlying adoption decision, including unobserved confounding factors. Our results also indicate that the predictive power of cascade methods that consider social influence solely is limited and that confounding factors are critical to effective adoption probability predictions.

## 5. Discussion and Conclusion

We take a data-driven approach to study adoption behaviors in a social network by predicting individuals’ adoption probabilities from observed adoption data. From the lens of established social network theories, we identify and operationalize key factors underlying adoption decision and then develop the locally weighted EM method for Naïve Bayes learning to predict adoption probabilities on the basis of these key factors. Our study makes several research contributions. First, we develop a method to predict adoption probabilities by considering a more comprehensive set of factors underlying adoption decision than do existing methods. An essential novelty of our method is the consideration of unobserved confounding factors for predicting adoption probabilities. Second, we evaluate the proposed method with real-world data from two large-scale social networks and produce empirical evidence that reveals greater predictive power of the proposed method over all benchmark methods across the two social networks we studied. Third, our evaluation results shed light on the significance of confounding factors in adoption probability predictions; they further suggest that adoption probabilities should be predicted with factors beyond social influence. Our findings support and reinforce the motivation of the proposed method, i.e., better predicting adoption probabilities with a more comprehensive set of key factors underlying adoption decision, including confounding factors.

Our findings suggest that cascade methods relying on exclusive use of social influence seems limited in predictive power. This is intriguing because previous research shows the important effects of social influence (Pan et al. 2011, Altshuler et al. 2012, Pickard et al. 2011), while pointing out the significance of other forces. Forces above and beyond social influence are also recognized by Bakshy et al. (2011) and Watts and Peretti (2007), congruent with our approach. Overall, our results shed light on potential limitations of cascade methods solely using social influence rather than defy the value of social influence for predictions. Our findings also suggest the consideration of other forces, particularly unobserved confounding factors, which could augment the predictive power of methods emphasizing social influence. In particular, our study offers a viable way to operationalize confounding factors for predicting individuals’ adoption probabilities in a network enabled by social media.

Our study also has several implications for practice. First, firms can use our method to enhance their social network-based target marketing efforts by better promoting product (service) adoptions in a network enabled by social media. Different from traditional target marketing, social network-based target marketing leverages essential structural linkage and interactions among individuals in a social network (Hill et al. 2006). Supported by our method, social commerce firms and online gaming providers alike can predict individual adoption probabilities on the basis of their social, demographic, and behavioral information and select a subset of customers to focus on in each time period. By ranking potential adopters by their probabilities, a firm can differentiate consumers and design personalized incentives in light of each individual’s adoption probability, rather than offering a uniform incentive. Firms could approach top-ranked potential adopters with strong cross- or up-selling strategies to generate more revenues and provide less likely potential adopters with incentives that lure them into adopting. Second, social commerce firms and online game providers also can use our method to estimate aggregate demand for their offerings over time. By summing adoption probabilities across potential adopters, a firm could predict the expected number of adopters in the next time period. Such prediction allows firms to gauge whether an offering is likely to go viral, which has crucial implications for their business decisions (Altshuler et al. 2012, Bandari et al. 2012). For example, if an offering is likely to go viral, the firm could act proactively to leverage the anticipated viral with appropriate marketing strategies, such as bundling or cross-selling. In addition, with effective estimates by our method, firms could allocate their resources and capabilities dynamically and intelligently across different time periods to improve performance and utilization efficiency. For example, firms can allocate more resources for time periods in which they predict a greater number of consumers will adopt their services. Furthermore, our method supports viral marketing, which requires identifying a target set of social entities whose adoptions will trigger the greatest spread of adoption throughout a social network. Identifying such seeds involves effective adoption probability predictions. Supported by our method, firms can become more effective in seed selection for viral marketing and perform the selection dynamically over time.

Our study could be extended in several directions. First, although the proposed method considers a more comprehensive set of factors underlying individuals’ adoption decisions than do existing methods, there could be other factors not considered by the method, such as viral product features (Aral and Walker 2011), strength of weak ties (Granovetter 1973), and the connectedness of adopter neighbors (Backstrom et al. 2006). Future research should extend the proposed method by exploring and incorporating additional important factors and evaluate the effectiveness accordingly. In Appendix F, we provide a preliminary study that illustrates how to incorporate the connectedness of adopter neighbors into our method. Future research should also consider how to utilize useful information about hidden confounding power for better initialization of $\bar { \lambda } _ { H \mid a } ,$ which in turn could improve the performance of the proposed method. Second, although our study provides a preliminary analysis of the performance differential between LWNB and NB, systematic methodological analyses as well as in-depth empirical evaluations are needed to analyze situations in which LWNB performs differently from NB. Third, prior studies have explored the interaction effects of social influence and entity similarity on adoption decisions (Aral et al. 2009, Aral and Walker 2012). In light of these studies, future research should examine how to extend the proposed method by incorporating such effects. Fourth, it is interesting to investigate alternative operationalizations of the factors underlying adoption decision and evaluate our method accordingly. A preliminary exploration in this direction is given in Appendix G. In addition, the current implementation of our method may not be scalable to social networks with millions of nodes, primarily because of the method’s pairwise distance calculation, which requires $O ( n ^ { 2 } )$ time under current implementation, where n is the number of nodes in a social network. Toward that end, use of a hierarchical tree-based distance calculation algorithm can reduce the time requirement for pairwise distance calculations from

$O ( n ^ { 2 } )$ to O4n log n5 (Barnes and Hut 1986). The computational time requirements can be further reduced through parallel computing. Therefore, it is important to investigate how to reduce the time required by the proposed method for large social networks with millions of nodes. Finally, conducting a case study is worthy of future research attention, perhaps in the form of social network-based target marketing.

## Electronic Companion

An electronic companion to this paper is available as part of the online version at http://dx.doi.org/10.1287/ isre.1120.0461.

## Acknowledgments

The authors thank the senior editor Chrysanthos Dellarocas, the associate editor Panos Ipeirotis, and three anonymous reviewers for their guidance and constructive comments that have tremendously improved the manuscript. The authors thank Ritu Agarwal for organizing the ISR Special Issue Workshop, from which our manuscript has benefited greatly. The authors also thank Sinan Aral for chairing the manuscript discussion session in the ISR Workshop and for his valuable suggestions. The authors gratefully acknowledge insightful feedbacks from the seminar participants at the University of Connecticut and the University of Utah as well as the ISR Workshop participants at the University of Maryland.

## References

Altshuler Y, Pan W, Pentland A (2012) Trends prediction using social diffusion models. Internat. Conf. Soc. Comput., Behav.- Cultural Modeling, and Prediction, College Park, MD, 97–104.

Aral S (2011) Identifying social influence: A comment on opinion leadership and social contagion in new product diffusion. Marketing Sci. 30(2):217–223.

Aral S, Walker D (2011) Creating social contagion through viral product design: A randomized trial of peer influence in networks. Management Sci. 57(9):1623–1639.

Aral S, Walker D (2012) Identifying influential and susceptible members of social networks. Science 337(6092):337–341.

Aral S, Muchnik L, Sundararajan A (2009) Distinguishing influence based contagion from homophily driven diffusion in dynamic networks. Proc. National Acad. Sci. 106(51):21544–21549.

Aral S, Muchnik L, Sundararajan A (2011) Engineering social contagions: Optimal network seeding and incentive strategies. Working paper,

Atkeson CG, Moore AW, Schaal S (1997) Locally weighted learning. Artificial Intelligence Rev. 11:11–73.

Backstrom L, Huttenlocher D, Kleinberg J, Lan X (2006) Group formation in large social networks: Membership, growth, and evolution. Proc. 12th ACM SIGKDD Internat. Conf. Knowledge Discovery and Data Mining, Philadelphia, 44–54.

Bakshy E, Hofman JM, Mason WA, Watts DJ (2011) Everyone’s an influencer: Quantifying influence on Twitter. Proc. 4th ACM Internat. Conf. Web Search and Data Mining, Hong Kong, China, 65–74.

Bandari R, Asur S, Huberman B (2012) The pulse of news in social media: Forecasting popularity. Working paper, HP Labs.

Barnes J, Hut P (1986) A hierarchical O(N log N ) force-calculation algorithm. Nature 324:446–449.

Bass F (1969) A new product growth for model consumer durables. Management Sci. 15(5):215–227.

Bishop CM (2006) Pattern Recognition and Machine Learning (Springer, New York).

Brown JJ, Reingen PH (1987) Social ties and word-of-mouth referral behavior. J. Consumer Res. 14(3):350–362.

Bruyn AD, Lilien GL (2008) A multi-stage model of word-of-mouth influence through viral marketing. Internat. J. Res. Marketing 25(3):151–163.

Burges C (1998) A tutorial on support vector machines for pattern recognition. Data Mining Knowledge Discovery 2(2):121–167.

Burt RS (1976) Positions in networks. Soc. Forces 55(1):93–122.

Burt RS (1987) Social contagion and innovation: Cohesion versus structural equivalence. Amer. J. Sociol. 92(6):1287–1335.

Carr D (2008) How Obama tapped into social networks’ power. The New York Times (November 9), http://www.nytimes.com/ 2008/11/10/business/media/10carr.html?\_r=0.

Centola D (2011) An experimental study of homophily in the adoption of health behavior. Science 334(6060):1269–1272.

Chang C-C, Lin CJ (2011) LIBSVM: A library for support vector machines. ACM Trans. Intelligent Systems Tech. 2(3):1–27.

Chen H, Zeng D (2009) AI for global disease surveillance. IEEE Intelligent Systems 24(6):66–69.

Chen W, Wang C, Wang Y (2010) Scalable influence maximization for prevalent viral marketing in large-scale social networks. Proc. 16th ACM SIGKDD Internat. Conf. Knowledge Discovery and Data Mining, Washington, D.C., 1029–1038.

Chen W, Wang Y, Yang S (2009) Efficient influence maximization in social networks. Proc. 15th ACM SIGKDD Internat. Conf. Knowledge Discovery and Data Mining, Paris, 199–208.

Chen Y-D, Brown SA, Hu PJ-H, King C-C, Chen H (2011) Managing emerging infectious diseases with information systems: Reconceptualizing outbreak management through the lens of loose coupling. Inform. System Res. 22(3):447–468.

Crandall D, Cosley D, Huttenlocher D, Kleinberg J, Suri S (2008) Feedback effects between similarity and social influence in online communities. Proc. 14th ACM SIGKDD Internat. Conf. Knowledge Discovery and Data Mining, Las Vegas, 160–168.

Dempster AP, Laird NM, Rubin DB (1977) Maximum likelihood from incomplete data via the EM algorithm. J. Royal Statist. Soc.: Series B 39(1):1–38.

Demsar J (2006) Statistical comparisons of classifiers over multiple data sets. J. Machine Learn. Res. 7:1–30.

Dodds PS, Muhamad R, Watts DJ (2003) An experimental study of search in global social networks. Science 301:827–829.

Domingos P, Pazzani M (1997) On the optimality of the simple Bayesian classifier under zero-one loss. Machine Learn. 29:103–130.

Domingos P, Richardson M (2001) Mining the network value of customers. Proc. 7th ACM SIGKDD Internat. Conf. Knowledge Discovery and Data Mining, San Francisco, 57–66.

Dye R (2000) The buzz on buzz. Harvard Bus. Rev. 78(6):139–146.

Eagle N, Macy M, Claxton R (2010) Network diversity and economic development. Science 328(5981):1029–1031.

Eagle N, Pentland A, Lazer D (2009) Inferring social network structure using mobile phone data. Proc. National Acad. Sci. 106(36):15274–15278.

Fawcett T (2006) An introduction to ROC analysis. Pattern Recognition Lett. 27:861–874.

Festinger L (1950) Informal social communication. Psych. Rev. 57:271–282.

Frank E, Hall M, Pfahringer B (2003) Locally weighted Naive Bayes. Proc. Conf. Uncertainty in Artificial Intelligence, Acapulco, Mexico, 249–256.

Friedkin NE (1998) A Structural Theory of Social Influence (Cambridge University Press, UK).

Friedman JH (1997) On bias, variance, 0/1—Loss, and the curse-ofdimensionality. Data Mining Knowledge Discovery 1:55–77.

Goyal A, Bonchi F, Lakshmanan L (2010) Learning influence probability in social networks. Proc. 3rd ACM Internat. Conf. Web Search and Data Mining, New York, 241–250.

Granovetter M (1973) The strength of weak ties. Amer. J. Sociol. 78(6):1360–1380.

Granovetter M (1978) Threshold models of collective behavior. Amer. J. Sociol. 83(6):1420–1443.

Greene WH (2008) Econometric Analysis (Prentice Hall, Upper Saddle River, NJ).

Han J, Kamber M (2006) Data Mining: Concepts and Techniques (Morgan Kaufmann, San Francisco).

Hand DJ, Mannila H, Smyth P (2001) Principles of Data Mining (MIT Press, Cambridge, MA).

Hartmann WR (2010) Demand estimation with social interactions and the implications for targeted marketing. Marketing Sci. 29(4):585–601.

Hastie T, Tibshirani R, Friedman J (2001) The Elements of Statistical Learning (Springer, New York).

Hemp P (2006) Avatar-based marketing. Harvard Bus. Rev. 84(6):48–57.

Hill S, Provost F, Volinsky C (2006) Network-based marketing: Identifying likely adopters via consumer networks. Statist. Sci. 21(2):256–276.

Hsu C-W, Chang C-C, Lin C-J (2003) A practical guide to support vector classification. Technical report, Department of Computer Science, National Taiwan University.

Huang J, Ling CX (2005) Using AUC and accuracy in evaluating learning algorithms. IEEE Trans. Knowledge Data Engrg. 17(3):299–310.

Ibarra H (1992) Homophily and differential returns: Sex differences in network structure and access in an advertising firm. Admin. Sci. Quart. 37(3):422–447.

Ibarra H, Andrews SB (1993) Power, social influence, and sense making: Effects of network centrality and proximity on employee perceptions. Admin. Sci. Quart. 38(2):277–303.

Iyengar R, Van den Bult C, Valente TW (2011) Opinion leadership and social contagion in new product diffusion. Marketing Sci. 30(2):195–212.

Jackson MO (2008) Average distance, diameter, and clustering in social networks with homophily. Papadimitriou C, Zhang S, eds. Internet and Network Economics, Lecture Notes in Computer Science, Vol. 5385 (Springer, Berlin), 4–11.

Kempe D, Kleinberg J, Tardos V (2003) Maximizing the spread of influence through a social network. Proc. 9th ACM SIGKDD Internat. Conf. Knowledge Discovery and Data Mining, Washington, D.C., 137–146.

Kempe D, Kleinberg J, Tardos V (2005) Influential nodes in a diffusion model for social network. Proc. 32nd Internat. Colloquium on Automata, Languages and Programming, Lisboa, Portugal.

Kimura M, Saito K (2006) Tractable models for information diffusion in social networks. Proc. 10th Eur. Conf. Principles and Practice of Knowledge Discovery in Databases, Berlin, 259–271.

Kleinberg J (2007) Cascading behavior in networks: Algorithmic and economic issues. Algorithmic Game Theory (Cambridge University Press, U.K.).

Kleinberg J (2008) The convergence of social and technological networks. Commun. ACM 51(11):66–72.

Kossinets G, Watts DJ (2006) Empirical analysis of an evolving social network. Science 3(11):88–90.

Lazarsfeld PF, Merton RK (1954) Friendship as a social process: A substantive and methodological analysis. Berger M, ed.

Freedom and Control in Modern Society (Van Nostrand, New York), 18–66.

Leenders RTAJ (2002) Modeling social influence through network autocorrelation: Constructing the weight matrix. Soc. Networks 24(1):21–47.

Levy DA (1992) The liberating effects of interpersonal influence: An empirical investigation of disinhibitory contagion. J. Soc. Psych. 132(4):469–473.

Levy DA, Nail PR (1993) Contagion: A theoretical and empirical review and reconceptualization. Genetic, Soc. General Psych. Monographs 119:235–285.

Lorrain F, White HC (1971) Structural equivalence of individuals in social networks. J. Math. Sociol. 1:49–80.

Manski CF (1993) Identification of endogenous social effects: The reflection problem. Rev. Econom. Stud. 60(3):531–542.

McPherson M, Smith-Lovin L, Cook JM (2001) Birds of a feather: Homophily in social networks. Annual Rev. Sociol. 27:415–444.

Mitchell TM (1997) Machine Learning (McGraw Hill, New York). New chapters accessed at http://www.cs.cmu.edu/<sup>\~</sup>tom/ NewChapters .html.

Pan W, Aharony N, Pentland A (2011) Composite social network for predicting mobile apps installation. Proc. Twenty-Fifth AAAI Conf. Artificial Intelligence, San Francisco, 821–827.

Pentland A (2008) Reality mining. MIT Technology Rev. 111(2):54–56.

Pickard G, Pan W, Rahwan I, Cebrian M, Crane R, Madan A, Pentland A (2011) Time-critical social mobilization. Science 334(6055):509–512.

PlaySpan (2012) http://www.businesswire.com/news/home/ 20120229006232/en/PlaySpan-Study-Shows-Percentage-Consumers -Buying-Virtual. Accessed July 15, 2012.

Rice RE, Aydin C (1991) Attitudes toward new organizational technology: network proximity as a mechanism for social information processing. Admin. Sci. Quart. 36(2):219–244.

Rice RE, Grand AE, Schmitz J, Torobin J (1990) Individual and network influences on the adoption and perceived outcomes of electronic messaging. Soc. Networks 12(1):27–55.

Salancik G, Pfeffer J (1978) A social information processing approach to job attitudes and task design. Admin. Sci. Quart. 2(3):224–253.

Shalizi CR, Thomas AC (2011) Homophily and contagion are generically confounded in observational social network studies. Sociol. Methods Res. 40(2):211–239.

Van den Bulte C, Lilien GL (2001) Medical innovation revisited: Social contagion versus marketing effort. Amer. J. Sociol. 106(5):1409–1435.

Wasserman S, Faust K (1994) Social Network Analysis: Methods and Applications (Cambridge University Press, UK).

Watts DJ, Peretti J (2007) Viral marketing for the real world. Harvard Bus. Rev. 85(5):22–23.

Wejnert B (2002) Integrating models of diffusion of innovations: A conceptual framework. Annual Rev. Sociol. 28:297–326.

Wellman B (1983) Network analysis: Some basic principles. Collins R, ed. Sociology Theory (Jossey-Bass, San Francisco), 155–200.

Wellman B (1997) An electronic group is virtually a social network. Kiesler S, ed. Culture of the Internet (Lawrence Erlbaum, Mahwah, NJ), 179–205.

Weng J, Lim E, Jiang J, He Q (2010) TwitterRank: Finding topicsensitive influential twitterers. Proc. 3rd ACM Internat. Conf. Web Search and Data Mining, New York, 261–270.

Zukerman I, Albrecht DW (2001) Predictive statistical models for user modeling. User Modeling User-Adapted Interaction 11(1): 5–18.
