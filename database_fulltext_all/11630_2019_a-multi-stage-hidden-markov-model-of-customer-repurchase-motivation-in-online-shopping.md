---
otero_id: 11630
otero_key: "H2AQH4N5"
title: "A multi-stage hidden Markov model of customer repurchase motivation in online shopping"
authors: "Xiaolin Li; Yuan Zhuang; Benjiang Lu; Guoqing Chen"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.03.012"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A multi-stage hidden Markov model of customer repurchase motivation in online shopping

![](/api/attachments/H2AQH4N5/fulltext/images/d3c9cfff873ae3e1ec79abb1cb7af17681a3d8f7126fa50e4cef2ed60b08f8f8.jpg)

Xiaolin Li<sup>a</sup>, Yuan Zhuang<sup>a</sup>, Benjiang Lu<sup>a,⁎</sup>, Guoqing Chen<sup>b</sup>

<sup>a</sup> School of Management, Nanjing University, Nanjing, Jiangsu 210093, China

<sup>b</sup> School of Economics and Management, Tsinghua University, Beijing 100084, China

## A R T I C L E I N F O

Keywords: Multi-stage Repurchase behavior Signaling theory Hidden Markov model

## A B S T R A C T

Product promotions and liberal return policies are two efective signals that can increase customers' repurchase behavior when online shopping, and how these signals work at diferent stages of market growth for various customer groups is an important topic for research and applications. Thus, to help online merchants make more efective decisions regarding the use of such signals, this paper proposes a multi-stage hidden Markov model (MS-HMM) to explore the motivational process behind customer repurchase behavior through the lens of the Signaling Theory. The customer-merchant relationship (CMR) is represented as the latent state in the hidden Markov model and is coupled with stage-heterogeneity in terms of state transition probabilities and state-dependent choice probabilities. Moreover, extensive experiments with real-world data are conducted to validate the effectiveness of the MS-HMM.

## 1. Introduction

With the widespread proliferation of online shopping, the question of how to retain existing customers has raised more attention in both practice and research than ever before [19]. A high customer retention rate can guarantee repeat purchases, which further provides the merchants with obvious competitive advantages. In addition, retaining existing customers usually costs less time and efort than attracting new ones [36]. In online shopping, many customers are more sensitive to price changes and less likely to remain loyal to one brand than of-line customers [1]. Therefore, it is desirable and necessary for online merchants to possess efective tools for understanding the motivational process behind online customer repurchase behavior [8].

In previous literature, the customer-merchant relationship (CMR) [2] has been identified as a key determinant of online repurchase intentions and is often understood in terms of various psychological factors, such as organizational trust, perceived ease of use or perceived usefulness [8]. However, such psychological factors are too general to guide online merchants' specific planning for the retention of existing customers.

From a practical perspective, online merchants usually prompt customers to repurchase by releasing positive marketing signals [42]. For example, liberal product return policies (i.e., no-hassle return) [16] and frequent promotions [17] have been widely adopted by merchants to attract customers. In 2016, the average online return rate of clothing products was 30% in China.<sup>1</sup> For promotions, in the first half of 2017, there were more than forty “Faux Carnivals” promoted by the Alibaba B2C platform (e.g., the Cowboy Carnival, the 6.18 Carnival, etc.) Although these marketing signals attracted plenty of research attention, previous research eforts were generally limited to providing merchants with efective strategies in relation to releasing related signals [3,14,41], which may be the case for the following reasons. First, a theoretical link between related signals and customer behavior motivation has not been systematically developed. In fact, most of the previous research generally treated the two signals as direct antecedents of merchants' various outcomes, leaving the customer motivational process untouched [20,39]. Second, the signals could be timeaware [11,21]. Signaling Theory has suggested that the efects of the salient signals and less salient signals could be diferent [22,26] and that the release time of e-commerce signals is generally accepted as one of the factors that determine their saliency. For example, the efect of a promotion signal released in the past degenerates over time, whereas a recent one may work better because of its higher relevance in directly triggering the purchase behavior of customers [21]. It is therefore essential to further analvze time effects when exploring the influence of related signals. Third, signals could be context-aware. For example, a promotion signal might be beneficial for developed merchants to retain customers and strengthen the CMR, but this approach may not be beneficial for those who are emerging or declining (e.g., a signal of low quality) [32]. In addition, customers with diferent characteristics (e.g., online shopping experience) may also respond to signals in diferent ways. Without taking into consideration these diferent situations, the efects of the signals can become blurred. In summary, the limitations of those previous research eforts leave space to further uncover the “black box” of motivational mechanisms behind customer repurchase behaviors.

Specifically, our study aims to build a theoretical link between related signals and customer behavior motivation by decomposing the signals' efects from the following two perspectives. First, with respect to time-awareness, the study classifies the signals' efects on repurchase behavior into the following two types: (i) the previous signals' efects on CMR formation; and (ii) the current signals' efects on purchase behavior. Second, with respect to context-awareness, the study categorizes the market growth of online merchants into the following three stages [11]: (i) stage 1: the introduction stage; (ii) stage 2: the growth stage; and (iii) stage 3: the declining stage. Furthermore, the study analyzes diferences among customers by introducing the transformation of the CMR to repurchases. In this way, the study can provide a good understanding of the customer motivational process behind returns and promotions, and better support merchants' decision-making on how to efectively release product promotion and return signals. Our study therefore focuses on the following research question:

Research Question: How do the signals (returns and promotions) affect customer repurchase through CMR, and do the signal efects vary in diferent situations (i.e., diferent stages of market growth and diferent customer groups)?

To answer this question, our study extends the hidden Markov model (HMM) to capture the efect diferences of signals on customer repurchase behavior in the three stages. Given state-related observations, the HMM model's learning task is to find the best set of statetransition possibilities and state-dependent choices. To address the stage heterogeneity of the efects, the stage dimension is incorporated into the HMM model, giving rise to a new model: MS-HMM (multi-stage hidden Markov model). Furthermore, the unobserved CMR is treated in terms of latent customer states in MS-HMM, and the customers' in dividual diferences (e.g., credit scores, active time, VIP grade, distance, provincial Internet users, provincial e-commerce penetration rate) are considered in the transformation from customer latent states to repurchase behaviors.

The remainder of the paper is organized as follows: Section 2 reviews related research in the literature; Section 3 formulates the problem and presents the extended model, namely, the MS-HMM; Section 4 discusses the extensive experiments conducted with real-world data; Section 5 highlights the research contributions from both the theore tical and practical point of view; and Section 6 concludes the paper by proposing future research directions.

## 2. Related work

Related research can be categorized in three ways: customer re purchase behavior; signals in e-commerce; and hidden Markov model.

## 2.1. Customer repurchase behavior

Customer repurchase behavior is an important concept in online merchants' market growth [8]. Compared to ofline settings, motivating online customer repurchases is regarded as more dificult because switching barriers significantly influence customer loyalty [19], and the switching cost is much lower in online shopping. Based on this, a large number of research efort has been expended to understand what makes customers repurchase online, as detailed below.

Marketing studies usually use psychological theories to explain the formation of repurchase intentions. Researchers have found that branding, awareness, and trust remain important sources of heterogeneity among online merchants [1]. Jones [27] argued that in online shopping, a user's willingness to repurchase is based on their satisfaction with previous transactions. The work in [8] showed that trust, perceived ease of use, and perceived usefulness and enjoyment are significant positive predictors of customers' online repurchase intentions. In addition, some research has explored how exactly these psychological factors afect the formation of repurchase intentions [4,23]. Fang et al. [13] demonstrated the negative role of e-commerce institutional mechanisms in online repurchase settings. Other research indicates that at the same level of brand satisfaction, repurchase rates are systematically diferent among diferent customer groups [36].

In conclusion, those customer-related psychological factors are always proved to be positive determinants for repurchases. In addition to these psychological factors, some researchers also investigated into the customer repurchase from a practical perspective based on the signaling framework. However, the efects of these signals were generally conflict or mixed (see details in Section 2.2), leaving us a compelling research gap to fill by uncovering the “black box” of the motivational mechanisms of customers' repurchase via decomposing the signals' efects under diferent contexts.

## 2.2. Signals in e-commerce

In many areas of research and for a broad range of applications, Signaling Theory has been applied to help explain the influence of information asymmetries for a wide range of contexts [9]. Traditional market signals include unconditional money-back guarantee [31], branding, advertising [28], etc., whereas in e-commerce, the concept of signals is extended, and more contexts or states are introduced as signals [35]: for example, online reviews and the voice of the public are also regarded as signals released by the public, and these signals can influence the behavior of other platform users [6,43].

Scholars show that in the case of e-commerce, signals do not only provide direct product information but also related and indirect information [31]. For example, a refund guarantee provides consumers with a direct insurance for return/refund and indirectly conveys the signal of guaranteed product quality and service [37]. Lee et al. [31] studied the influence of unconditional return guarantees on customer purchase intention and trust factors through behavioral experiments and verified that the signal can improve purchase rates. Advertising messaging is indirect as well, and some scholars have found that advertising does not only provide product information but also sends signals related to quality and brand [40].

Our study focuses on two observable signals that are directly related to sales: returns and promotions (advertising). Drawing on previous studies as shown in Table 1, we can see that promotions and returns are not always good for sales, and as a matter of fact, findings regarding their efects in various situations are mixed.

The studies regarding return issues mostly extended traditional theories or methods from other domains to understand the motivations behind return events, such as price perception, attribute-level performance, and satisfaction [25]. Grifis et al. [20] examined the relationship between customer return experience and subsequent shopping behaviors. Some researchers found that the returns management process could significantly and positively influence repurchase behaviors [20]. On the other hand, Kuan et al. [29] investigated the return issue from the perspective of the cognitive dissonance theory and suggested that the return experience could have a negative correlation with subsequent purchase behaviors.

As for promotions, findings show that brand trust could be significantly moderated by promotions [12,33]. Furthermore, Lvovskaya et al. [34] suggested that repurchase rates are negatively afected by previous promotions. In addition, Ndubisi and Moi [39] showed that price discounts and bonus packs were associated with product trial:

Table 1  
Summary of main stream research on signals of return and promotion.

<table><tr><td>Signals</td><td>Valence</td><td>Target</td><td>Heterogeneity</td><td>Main studies</td></tr><tr><td>Return management</td><td>Positive</td><td>Trust, purchase</td><td>Customer</td><td>[20], etc.</td></tr><tr><td>Return guarantee</td><td>Not negative</td><td>Purchase</td><td>None</td><td>[41], etc.</td></tr><tr><td>Return experience</td><td>Negative</td><td>Trust</td><td>Multi-channel</td><td>[29], etc.</td></tr><tr><td>Promotion experience</td><td>Positive &amp; negative</td><td>Branding</td><td>Customer</td><td>[3,14], etc.</td></tr><tr><td>Promotion experience</td><td>Positive &amp; negative</td><td>Repurchase</td><td>Merchant</td><td>[34], etc.</td></tr><tr><td>Promotion experience</td><td>Not negative</td><td>Branding, repurchase</td><td>Stage</td><td>[10], etc.</td></tr></table>

trials determined repurchase behaviors and mediated the efect of sale promotions on the repurchases.

## 2.3. Hidden Markov model

The HMM model predefines a finite set of relationship states to reflect the dynamic process behind a set of observed behaviors. The HMM model has been successfully applied in many domains, such as speech recognition [15,24], behavior recognition [44], text recognition [30], and fault diagnosis [18].

In customer behavior studies, many research eforts have focused on the model's ability to capture and explain customers' unobserved states. Chen et al. [5] detected the syndromic surveillance of flu on Twitter using a temporal topic model. Mukherjee et al. [38] captured the cus tomers' experiences and interests with a generative HMM-LDA model. A new reputation management system has also been developed based on a hidden semi-Markov model (HSMM-RMS) [45]. Cheung et al. [7] constructed an HMM to investigate the dynamics of customer purchasing behavior based on multiple purchase preference factors.

However, those eforts have often treated the dynamic process as stage constant; in other words, the transition probabilities from state 1 to state 2, for instance, did not change across diferent time periods, which is not intuitive. This motivated us to introduce a modeling fra mework in our study for understanding repurchase dynamics motivated by promotion and return signals throughout the market-growth lifecycle. A market-stage dimension is therefore incorporated into our model to reflect the changes in signal efects during diferent stages, resulting in a multi-stage hidden Markov model (MS-HMM).

## 3. The MS-HMM model

## 3.1. Problem statement

As shown in Fig. 1, the methodology workflow describes how re turns and promotions impact the CMR and customer repurchase at a single stage [20,29,41]. Specifically, in the early period of a specific stage t<sup>′</sup>, based on the last CMR at t-1, customers can perceive signal released by merchants (i.e., returns/promotions). These perceptions can enhance or weaken the CMR. Subsequently, the formed CMR at t<sup>′</sup>, which is defined as an unobserved latent state, can be transformed into customer repurchases in the current period t<sup>′′</sup>. Simultaneously, current returns and promotions perceived by customers will also have shortterm efects on the transformation process. In addition, stage heterogeneity and customers' individual diferences will have an impact on the signals' efects as well. Based on this information, our research question can be decomposed into three subquestions:

• Subquestion 1: How do previous signals (returns and promotions) afect customer repurchase behaviors by influencing the latent re lationship between customers and merchants (CMR)?

Subquestion 2: How do current signals (returns and promotions) affect the transformation from customers' latent states to customer repurchase behaviors?

• Subquestion 3: How do the two efects noted above change in different situations (i.e., in the case of this paper, across diferent stages of merchant market growth and diferent customer groups)?

In addition, the three intuitions behind the proposed MS-HMM model are described as follows:

• Intuition 1: The motivational process behind customer repurchase in online shopping exhibits stage-heterogeneity during a merchant's market growth;

• Intuition 2: Each stage t can be divided into two separate periods: the previous period t<sup>′</sup> and the current period t<sup>′′</sup>;

Intuition 3: For any given stage, the purchase behavior in period t<sup>′</sup> is defined as the customer repurchase behavior.

Specifically. our model is developed in three steps, as follows (symbol notations in Table 2): (i) initialize the initial state distribution: the probability that at stage 1, customer i is at state s is $P ( S _ { i 1 } = s ) = \pi _ { i s } ;$ (ii) generate the state transition probability: the probability that at stage t, customer i transits from state s to s<sup>′</sup> is P $( S _ { i t } = s \vert S _ { i ( t - 1 ) } = s ^ { ' } ) = \theta _ { i t s s ^ { ' } }$ (in which stage-heterogeneity is included); and (iii) generate the state-dependent choice probability: the probability that at stage t, customer i repurchases as conditioned by the current state s is $P ( Y _ { i t } = 1 | S _ { i t } = s ) = \gamma _ { i t | s }$ (where both the stage-heterogeneity and the customer individual diferences are included).

## 3.2. The state transition

In the proposed MS-HMM model, the transition between latent states is modeled as a random walk process where only transitions to adjacent states are allowed. That is, at stage t, a customer i can only move from the current state s to state s-1 or state s + 1 or remain in the same state. This assumes that customer propensities for transition are based on previous signals released by the merchant in the previous period t<sup>′</sup>.

![](/api/attachments/H2AQH4N5/fulltext/images/e805dd030e93864ed0dd333a48f10ac3e75aa43af85b2732e956288dd9d48df1.jpg)  
Fig. 1. The general workflow of the proposed method.

Table 2 Symbol notation.

<table><tr><td>Notation</td><td>Description</td></tr><tr><td> $i$ </td><td>The customer  $i \in \{0, ...,NI\}$ </td></tr><tr><td> $s$ </td><td>The latent state  $s \in \{0, ...,NS\}$ </td></tr><tr><td> $t$ </td><td>The stage  $t \in \{0, ...,NT\}$ </td></tr><tr><td> $\pi_{is}$ </td><td>The initial relationship state distribution</td></tr><tr><td> $\theta_{itss'}$ </td><td>The relationship state transition probability</td></tr><tr><td> $\gamma_{it|s}$ </td><td>The state-dependent choice probability</td></tr><tr><td> $\alpha_{it}$ </td><td>The customer previous relationship signals</td></tr><tr><td> $\rho_{st}$ </td><td>The time-aware effects of relationship signals</td></tr><tr><td> $\xi_{i}'$ </td><td>The vector of the customer individual differences</td></tr><tr><td> $\widehat{\omega}_{0ts}$ </td><td>The state-specific coefficient for state  $s$ </td></tr><tr><td> $\omega_{ts}$ </td><td>The coefficient of the behavior transition effects</td></tr><tr><td> $\tau_{s}$ </td><td>The coefficient of the individual differences</td></tr><tr><td> $\beta_{it}'$ </td><td>The behavior motivating factors</td></tr></table>

Specifically, the state transition probability $\theta _ { i t }$ for customer i at stage t is modeled as an ordered logit form (i.e., Eq. (1)–(3)):

$$
\begin{array}{r l} \theta_ {i t s, s - 1} & = P r (t r a n s i t i o n f r o m s t o s t a t e s - 1) \\ & = \frac {e x p (\mu (l , s) - \alpha_ {i t} ^ {\prime} \rho_ {s t})}{1 + e x p (\mu (l , s) - \alpha_ {i t} ^ {\prime} \rho_ {s t}) ^ {\prime}}; \end{array}\tag{1}
$$

$$
\begin{array}{r l} \theta_ {i t s, s} & = P r (t r a n s i t i o n f r o m s t o s t a t e s) \\ & = \frac {e x p (\mu (h , s) - \alpha_ {i t} ^ {\prime} \rho_ {s t})}{1 + e x p (\mu (h , s) - \alpha_ {i t} ^ {\prime} \rho_ {s t})} \\ & - \frac {e x p (\mu (l , s) - \alpha_ {i t} ^ {\prime} \rho_ {s t})}{1 + e x p (\mu (l , s) - \alpha_ {i t} ^ {\prime} \rho_ {s t})}; \end{array}\tag{2}
$$

$$
\begin{array}{r l} \theta_ {i t s, s + 1} & = P r (t r a n s i t i o n f r o m s t o s t a t e s + 1) \\ & = 1 - \frac {e x p (\mu (h , s) - \alpha_ {i t} ^ {\prime} \rho_ {s t})}{1 + e x p (\mu (h , s) - \alpha_ {i t} ^ {\prime} \rho_ {s t}) ^ {\prime}}; \end{array}\tag{3}
$$

Here, state $s + 1$ represents a stronger relationship than state s; likewise, state s-1 is weaker than state s + 1 and state s. The threshold $. \mu$ is state-specific, and the state transition will occur if the propensity for transition passes the respective threshold. Thus, $\mu$ in the higher state is larger than that in the lower state. To this end, we apply a constraint on $\mu \colon \mu ( s + 1 ) > \mu ( s )$ . In addition, $\mu ( l , s )$ is the lower threshold, and $\mu ( h , s )$ is the upper threshold. The vector $\alpha _ { i t } ^ { \phantom { \dagger } }$ represents the value of previous signals as perceived by customer i at stage t. Finally, we capture the stage-aware efects of previous signals perceived by customers during state s at stage t, with the coeficient vector $\rho _ { s t } .$

## 3.3. The state-dependent customer response

In this subsection, we model the state-dependent customer response with behavior transformation covariates. In the current period $t ^ { ' } ,$ customer repurchase behaviors not only depend on their relationship states but also on their current signals as perceived by the customers. The probability of observing customer i's repurchase behaviors during state s at stage t is given in Eq. (4):

$$
\gamma_ {i t | s} = \frac {e x p (\widehat {\omega} _ {0 t s} + \beta_ {i t} ^ {\prime} \omega_ {t s} + \xi_ {i} ^ {\prime} \tau_ {s})}{1 + e x p (\widehat {\omega} _ {0 s} + \beta_ {i t} ^ {\prime} \omega_ {s} + \xi_ {i} ^ {\prime} \tau_ {s})};\tag{4}
$$

Here, customer repurchase choice $P ( Y _ { i t } = 1 | S _ { i N T } = s ) = \gamma _ { i t | s }$ follows a binary logit model. The expression $\widehat { \omega } _ { 0 t s }$ is the state-specific coeficient vector for state $s ,$ and $\omega _ { t s }$ is the coeficient vector capturing the shortterm efects of the current signals $\beta _ { i t } ^ { ' }$ . In addition, the proposed model takes into account that the individual diferences of customers may have efects on the transformation from a relationship to actual repurchase. For instance, customers who have been active for a long time may be less price sensitive and are not so afected by promotions. Therefore, the proposed model introduces the vector of customer individual diferences $\boldsymbol { \xi } _ { i } ^ { \prime }$ and the respective coeficient $\tau _ { s }$ to obtain more focused results. Furthermore, the proposed model also imposes a restriction on the state-specific coeficient $\widehat { \omega } _ { 0 t s } .$ . The restriction is given in Eq. (5):

$$
\widehat {\omega} _ {0 t s} = \widehat {\omega} _ {0 t 1} + \sum_ {s ^ {\prime} = 2} ^ {s} e x p (\widehat {\omega} _ {0 t s ^ {\prime}}); \qquad s = 2, \dots , N S.\tag{5}
$$

The customer repurchase choice is set as a binary value; therefore, the probability $P ( Y _ { i t } \mid S _ { i N T } = s ) = { \widetilde { \gamma } } _ { i t \mid }$ s that customer i will make choice $Y _ { i t }$ at stage t during state s is given by Eq. (6):

$$
P (Y _ {i t} \mid S _ {i N T} = s) = \gamma_ {i t | s} ^ {Y _ {i t}} \cdot (1 - \gamma_ {i t | s}) ^ {1 - Y _ {i t}};\tag{6}
$$

## 3.4. The estimation procedure

The joint likelihood of a sequence of observed choices is given by the sum of all possible paths that the customer could go through between two latent states across all stages. Thus, given a sequence of observed choices $Y _ { i } ,$ the joint likelihood for customer i is formulated as in Eq. (7):

$$
P (Y _ {i t} = y _ {i 1}, \dots , Y _ {i t} = y _ {N T}) = \pi_ {i} \left(\prod_ {t = 1} ^ {N T - 1} \widetilde {\Gamma} _ {i t} \Theta_ {i t}\right) \mathbf {1} ^ {\prime};\tag{7}
$$

Here, π is the initial state distribution for customer i. In addition, $\Gamma _ { i t }$ is an NS × NS diagonal matrix, where the element vector in the diag onal is $\gamma _ { i t | s } .$ Likewise, $\Theta _ { i t }$ is an NS × NS matrix, where the elements represent the state transition probabilities at stage t. In addition, 1<sup>′</sup> is an NS × 1 vector of ones. The final scaled log-likelihood function across customers is the sum of all the customer scaled joint log-likelihood over $i \in \{ 1 , \ldots , N I \}$

Next, our proposed model is estimated based on the final scaled loglikelihood function. Parameters to be estimated are those in the transition matrix and the state-dependent choice matrix, as described in Eq. (1)–(5). The estimation procedure used on our model is a nonlinear minimization procedure to minimize the negative value of the final scaled log-likelihood.

## 4. Data experiments

In this section, three data experiments are conducted that attempt to answer the three subquestions noted before as well as evaluate the performance of the proposed MS-HMM model.

## 4.1. Data description

The dataset used to calibrate and validate the model was extracted from the purchase records of one online cosmetic merchant at Taobao. com, the largest B2C platform in China. This data set consists of 51,546 purchase records from January 1, 2011 to December 31, 2013.

As previously discussed, the merchant's market growth could be described in three stages [11]; namely, stage 1 (the introduction stage), stage 2 (the growth stage), and stage 3 (the declining stage). Fig. 2 compared the average value of orders, returns, and promotions per month with the total orders of all the customers over the three years. It can be seen that total sales for all customers slightly increased in 2011. Next, the market growth increased sharply in 2012, followed by a de cline in total sales in 2013. In addition, two types of signal efects were analyzed: previous signal efects and current signal efects. The dataset was therefore divided into three stages and six periods:

![](/api/attachments/H2AQH4N5/fulltext/images/7f9dc730e92177b5bec52f408a196749978093468466a8d198308c9c084f45d9.jpg)  
Fig. 2. Comparison of attributes across three years.

Stage 1: The data from January 1, 2011 to December 31, 2011 was divided into two periods: period 1′ (previous period) from January 1, 2011 to August 31, 2011; and period 1″ (current period) from September 1, 2011 to December 31, 2011;

Stage 2: The data from January 1, 2012 to December 31, 2012 was divided into two periods: period 2′ (from January 1, 2012 to August 31, 2012) and period 2″ (from September 1, 2012 to December 31, 2012);

• Stage 3: The data from January 1, 2013 to December 31, 2013 was divided into two periods: period 3′ (from January 1, 2013 to August 31, 2013) and period 3″ (from September 1, 2013 to December 31, 2013).

The previous signals perceived by customers were reflected by previous orders, previous returns, and previous promotions in the previous period (relationship formation). Current signals perceived by customers were reflected by current returns and promotions in the current period (behavior transformation). Table 3 shows the statistical analysis of the important attributes in the dataset. Note that this cosmetics merchant began to provide the no-hassle return service on September 1, 2011. Therefore, in the backstage database, the return amount in period 1′ is zero.

The estimated coeficients of the main attributes in stage 2 based on the proposed model are presented in Table 4, for which the value of the state was set to 3. Moreover, in order to eliminate the efects of other potential factors, customer individual diferences (i.e., credit scores, active time, VIP grade, distance, provincial Internet users and provincial e-commerce penetration rate) were taken into consideration in the current period. As seen from the values of the thresholds, the values increased from state 1 to state 3; therefore, the customer-merchant relationship was getting stronger. That is, there were three types of customers: weak-CMR (state 1); medium-CMR (state 2); and strong-CMR (state 3).

Table 3  
Statistics of the attributes.

<table><tr><td>Attribute</td><td>Mean</td><td>Std.</td><td>Min</td><td>Max</td></tr><tr><td>distance_rank</td><td>1.9243</td><td>0.8469</td><td>0</td><td>3</td></tr><tr><td>Internet_users_rank</td><td>1.95554</td><td>0.6283</td><td>0</td><td>3</td></tr><tr><td>penetration_rate_rank</td><td>1.94515</td><td>0.65761</td><td>0</td><td>3</td></tr><tr><td>customer_credit</td><td>573.1848</td><td>543.2282</td><td>10</td><td>9386</td></tr><tr><td>vip_grade</td><td>4.183314</td><td>1.211957</td><td>0</td><td>7</td></tr><tr><td>active_time</td><td>1749.911</td><td>648.0837</td><td>427.23</td><td>3819.03</td></tr><tr><td>previous_order1</td><td>3.786085</td><td>9.944322</td><td>0</td><td>354</td></tr><tr><td>current_order1</td><td>3.811778</td><td>4.576657</td><td>1</td><td>67</td></tr><tr><td>previous_order2</td><td>8.211894</td><td>15.99796</td><td>0</td><td>406</td></tr><tr><td>current_order2</td><td>7.675808</td><td>22.26599</td><td>0</td><td>1033</td></tr><tr><td>previous_order3</td><td>13.68707</td><td>44.63102</td><td>0</td><td>2271</td></tr><tr><td>current_order3</td><td>3.738164</td><td>17.41995</td><td>0</td><td>905</td></tr><tr><td>current_return1</td><td>0.0736143</td><td>0.4043613</td><td>0</td><td>6</td></tr><tr><td>previous_return2</td><td>0.0470554</td><td>0.3318366</td><td>0</td><td>7</td></tr><tr><td>current_return2</td><td>0.3071594</td><td>1.300301</td><td>0</td><td>30</td></tr><tr><td>previous_return3</td><td>1.07015</td><td>2.362594</td><td>0</td><td>55</td></tr><tr><td>current_return3</td><td>0.2549076</td><td>1.01816</td><td>0</td><td>30</td></tr><tr><td>previous_discount1</td><td>1.370958</td><td>7.038985</td><td>0</td><td>312</td></tr><tr><td>current_discount1</td><td>1.518764</td><td>3.151336</td><td>0</td><td>54</td></tr><tr><td>previous_discount1</td><td>3.603926</td><td>8.441482</td><td>0</td><td>179</td></tr><tr><td>current_discount1</td><td>5.396651</td><td>14.58256</td><td>0</td><td>595</td></tr><tr><td>previous_discount1</td><td>10.57823</td><td>41.19791</td><td>0</td><td>2110</td></tr><tr><td>current_discount1</td><td>2.957564</td><td>16.85683</td><td>0</td><td>894</td></tr></table>

## 4.2. Data experiments related to subquestion 1

In this subsection, our task is to figure out the exact changes in the previous signal efects on customer repurchase behaviors, via influencing the latent customer-merchant relationship (CMR). Two types of previous signals were analyzed: previous\_return and previous\_promotion. The attribute “previous\_order” indicates the value of the original CMR. As we can see in Fig. 3, compared to current signals, the coefi cients of the previous signals were mostly low in the growth stage (stage 2). Furthermore, all three signals had negative efects on the CMR, except for “previous\_order” in state 2. Notably, for state 2 the lower bound was higher than the upper bound, as can be seen in Table 4. Considering the coeficients of the previous signals, customers in state 2 would stay in the same state only when they had placed numerous orders, had few returns, and experienced few promotions of the merchant's products. Medium orders, returns and promotions enhanced the CMR to an upper state, while few orders, numerous returns and promotions weakened the CMR. The coeficient distributions of diferent signals appeared to be similar across diferent states. That is, for all the states, previous orders had the largest impact, which was followed by previous promotions then previous returns. Moreover, in state 2, previous orders had the highest positive efect, while previous promotions had the highest negative efect among the three states. Apparently, customers in state 2 were more likely to adjust relationships when they had perceived the previous signals.

## 4.3. Data experiments related to subquestion 2

In this subsection, we examine the efects of current signals on the transformation from customers' latent states to repurchase behaviors. There were two types of current signals considered: current\_return and current\_promotion, as shown in Table 4. Next, their coeficients across diferent states were compared in Fig. 4. It is clear that current signals can strongly afect customer repurchase behaviors, especially compared to the previous signals. The coeficient distributions of diferent current signals appear to be similar across diferent states. That is, for all the states, promotions had a higher efect on repurchase behavior than returns. For customers in diferent states, the current return signals exerted a similar efect on repurchase behavior. This means that current returns do not have diferent efects on diferent customers, implying that it may be useless to carry out diferent return policies for diferent customer groups in the current period.

## 4.4. Data experiments related to subquestion 3

In this subsection, the performances of the proposed model (MS-HMM) and a basic HMM (BA-HMM) model (without stage-heterogeneity) were compared to determine whether stage-heterogeneity is important for releasing signals to motivate customer repurchase behaviors. As shown in Table 5, MS-HMM outperformed BA-HMM on the validation of the log-likelihood. That is, by introducing stage-heterogeneity, the fit indicators of BA-HMM could be greatly improved. Fur thermore, when BA-HMM introduced stage-heterogeneity to current signals (BA+Curr), the performance also improved. In conclusion, stageheterogeneity of signals can improve the fit indicators of the basic model.

Table 4  
Attribute coeficients at Stage 2 in MS-HMM.

<table><tr><td>Attribute</td><td>Coefficient</td><td>Attribute</td><td>Coefficient</td></tr><tr><td>current_return_state1</td><td>3.7731</td><td>current_promotion_state1</td><td>6.2630</td></tr><tr><td>current_return_state2</td><td>3.4429</td><td>current_promotion_state2</td><td>6.7431</td></tr><tr><td>current_return_state3</td><td>3.6185</td><td>current_promotion_state3</td><td>6.6116</td></tr><tr><td>previous_return_state1</td><td>-0.0053</td><td>previous_promotion_state1</td><td>-0.2374</td></tr><tr><td>previous_return_state2</td><td>-0.0124</td><td>previous_promotion_state2</td><td>-0.3548</td></tr><tr><td>previous_return_state3</td><td>-0.0114</td><td>previous_promotion_state3</td><td>-0.2824</td></tr><tr><td>previous_order_state1</td><td>-0.0677</td><td>threshold_state1</td><td>[-0.4730,0.0467]</td></tr><tr><td>previous_order_stae2</td><td>0.5834</td><td>threshold_state2</td><td>[0.5748,0.1029]</td></tr><tr><td>previous_order_state3</td><td>-0.0517</td><td>threshold_state3</td><td>[0.0062,1.1029]</td></tr><tr><td>buyer_credit_state1</td><td>0.1017</td><td>vip_info_state1</td><td>-0.0397</td></tr><tr><td>buyer_credit_state2</td><td>0.0483</td><td>vip_info_state2</td><td>0.0496</td></tr><tr><td>buyer_credit_state3</td><td>-0.050</td><td>vip_info_state3</td><td>0.07152</td></tr><tr><td>active_time_state1</td><td>-0.0843</td><td>distance_state1</td><td>-0.0592</td></tr><tr><td>active_time_state2</td><td>-0.1007</td><td>distance_state2</td><td>-0.0268</td></tr><tr><td>active_time_state3</td><td>-0.1107</td><td>distance_state3</td><td>-0.0807</td></tr><tr><td>Internet_users_state1</td><td>-0.0192</td><td>penetration_rate_state1</td><td>0.0463</td></tr><tr><td>Internet_users_state2</td><td>0.0895</td><td>penetration_rate_state2</td><td>-0.0313</td></tr><tr><td>Internet_users_state3</td><td>0.0374</td><td>penetration_rate_state3</td><td>-0.0723</td></tr></table>

![](/api/attachments/H2AQH4N5/fulltext/images/a471c13c449e0b0da929a916e3bafa716f1d7a48db0845ac342827f71ac78ca9.jpg)  
Fig. 3. Previous Signals in Stage 2.

![](/api/attachments/H2AQH4N5/fulltext/images/0b8d2a4b214c39f950ff0dbef352b248b6ef8a380212f0bfcad7f998c35a9999.jpg)  
Fig. 4. Current Signals in Stage 2.

Table 5  
Comparison of model performance.

<table><tr><td></td><td>Log-likelihood</td><td>BIC</td><td>AIC</td><td>Variables estimated</td></tr><tr><td>MS-HMM</td><td>-15,391.46</td><td>30,613.02</td><td>30,686.92</td><td>78</td></tr><tr><td>BA-HMM</td><td>-21,782.32</td><td>43,394.74</td><td>43,731.6</td><td>42</td></tr><tr><td>BA + Curr</td><td>-15,402.61</td><td>30,635.32</td><td>-30,709.22</td><td>60</td></tr></table>

![](/api/attachments/H2AQH4N5/fulltext/images/a9db79eacea636da68aaed943d79f2d35584cd8163c199fc557bd1505920000c.jpg)  
Fig. 5. Efects of current promotions.

Furthermore, we examined the efect changes of current signals across the stages. Fig. 5 depicts the efect curves of current promotions across three stages and three states. It can be seen that in the introduction stage (stage 1) of the market growth, the efect of current promotions had a negative correlation with the strength of the CMR and was apparently weaker than the efect curves of the other two stages. That is, highly loyal customers were less likely to be motivated by current promotions in the introduction stage. However, with the growth of the market, higher-loyalty customers became more sensitive to promotions. Finally, in the declining stage (stage 3), highly loyal customers were the most likely to be motivated among the three customer groups. It is worth noting that the single efect curve of BA-HMM was not in line with the three curves generated by MS-HMM. Therefore, the single curve could hardly reflect the characteristics at diferent stages and the trends in efect changes.

Second, the efect curves of current returns across three stages and three states are shown in Fig. 6. Similar to current promotions, the efect curves of current returns demonstrated similar trends across the three stages. The signal efects in stage 1 were apparently weaker than the signal efects in the other two stages. Furthermore, the efect curve of BA-HMM was entirely diferent from the three curves generated by MS-HMM.

In addition, the efect curves of previous promotions and returns across three stages and three states were analyzed as an extra study of the changes in the efects of signals (see Figs. 7 and 8).

The efect curves of previous signals in the declining stage (stage 3) were noticeably diferent from the other two stages. That is, current signals were clearly diferent in stage 1, while previous signals were clearly diferent in stage 3. Moreover, most of previous signals showed negative efects on the influence of latent states, except for state 2 in stage 3. Thus, previous signals released by merchants had weak negative efects on CMR formation. Only in stage 3, customers in state 2 could be positively afected by previous signals. It is also worth noting that the single efect curve of BA-HMM was completely diferent from the three curves generated by MS-HMM.

![](/api/attachments/H2AQH4N5/fulltext/images/8be02415e095dab192f9c1ceb8233c5e92cf60eeff2e7bae102c502f4bfc15f0.jpg)  
Fig. 6. Efects of current returns.

![](/api/attachments/H2AQH4N5/fulltext/images/acc04378eebc185840c06b3ee121d65ff8ac2b101cb9f7a71c21dca955df04b8.jpg)  
Fig. 7. Efects of previous promotions.

![](/api/attachments/H2AQH4N5/fulltext/images/9d26e9236d0bde9e99ca1c654c0f88b1298716005a8446daf9d4bfe14c6ea1dd.jpg)  
Fig. 8. Efects of previous returns.

## 4.5. Discussion

To examine previous signal efects and current signal efects, data experiments 1 and 2 took stage 2 as an example. In data experiment 1, we found that previous signals always had negative, but relatively weak, efects on the formation of the CMR. Customers in state 2 were more likely to be afected by previous signals (positively or negatively). Moreover, only the customers in state 2 could be positively afected by previous returns. In addition, in data experiment 2, current signals played a positive role in motivating repurchases and showed few efect changes across diferent customer groups. Releasing frequent promotion signals (previous or current) was the most efective way to influence customers. Briefly, in the current period, once the merchant released signals to motivate customer repurchase behavior, the customers were positively afected. However, the released signals had negative, but weak, efects on the subsequent CMR formation, except for customers in stage 2 and state 2. Merchants could target medium-loyal customers in stage 2 to transform them into highly loyal customers.

The proposed model demonstrates its efectiveness in capturing the changes in signal efects across diferent stages. It seems necessary to introduce the stage dimension into the HMM model. In this way, merchants can make appropriate decisions at diferent stages of their market growth. For instance, current signals in stage 1 could clearly have weak efects on motivating repurchases, so merchants should find other ways to improve sales rather than adopting liberal product return policies and ofering frequent promotions. In addition, in terms of previous signals, merchants should act cautiously in the declining stage (stage 3) since the signal efects could vary significantly for diferent customer groups at this stage.

## 5. Theoretical contributions and practical implications

The study in this paper makes several contributions to theory. First, the proposed model (MS-HMM) provides a novel perspective on understanding the motivational process behind customer repurchase. In this way, MS-HMM builds the theoretical links among signals (returns and promotions), latent customer-merchant states, and repurchase be haviors. Furthermore, we classified two types of signal efects based on our model: (i) previous signal efects and (ii) current signal efects, along with respective discussions and verifications of efect changes in relation to growth stages and customer states.

The findings could be added to the research literature in addressing whether or not returns and promotions are beneficial for the sales. Second, the proposed model contributes to the e-commerce signaling literature by taking into account time-awareness (i.e., previous and current) and context-awareness (i.e., diferent stages and customer groups) in the efects of returns and promotions. Third, MS-HMM extends the basic HMM model by incorporating stage-heterogeneity, which was verified for its efectiveness with real-world data experiments.

In addition, our study also provides useful practical insights. The MS-HMM model could guide online merchants in releasing efective signals according to diferent market growth stages and diferent customer groups. For instance, if a merchant is in a growth stage, more liberal return signals and frequent promotion signals can be released to medium-loyal customers than other customers, thus promoting a subsequent customer-merchant relationship (CMR) while motivating current purchases. The medium-loyal customers can then be easily transformed into highly loyal customers. However, if a merchant is in an introduction stage, it may not be efective to motivate customer repurchases by releasing such signals, especially for loyal customers.

## 6. Conclusion

In this paper, we gained insight into the motivational process behind customer repurchase behaviors from an e-commerce signaling perspective and proposed a multi-stage hidden Markov model (MS-HMM). In our model, the stage dimension was introduced to capture the efect diferences across market growth stages and to identify the key determinants of repurchase behavior. Extensive data experiments also demonstrated that the proposed model outperforms the basic HMM on the validation of the log-likelihood. Therefore, stage-heterogeneity plays an important role in CMR formation and repurchase motivation.

However, as the current study focused only on a specific merchant, the outcomes and implications should be generalized with caution. Conservatively speaking, the MS-HMM model validated in this study may also be applied to other e-commerce contexts that are of multistage growth patterns and product attributes $( \boldsymbol { \mathrm { e . g . } } ,$ experience, hedonic, nondurable) similar to those of online cosmetic markets. For diferent contexts/markets, future studies are needed to validate the general ization of the MS-HMM model, with larger datasets in a longer time span.

## Acknowledgements

This research was supported by the National Nature Science Foundation of China (NSFC) via grant numbers 61773199 and 71732002.

## References

[1] E. Brynjolfsson, M.D. Smith, Frictionless commerce? A comparison of internet and conventional retailers, Manag. Sci. 46 (4) (2000) 563–585, https://doi.org/10. 1287/mnsc.46.4.563.12061.

[2] M. Carter, R. Wright, J.B. Thatcher, R. Klein, Understanding online customers' ties to merchants: the moderating influence of trust on the relationship between switching costs and e-loyalty, Eur. J. Inf. Syst. 23 (2) (2014) 185–204, https://doi. org/10.1057/ejis.2012.55.

[3] P.L. Chang, M.H. Chieng, Building consumer brand relationship: a cross-cultural experiential view. Psychol. Mark, 23 (11) (2006) 927–959. https://doi,org/10 1002/mar,20140

[4] C.M. Chen, H.M. Liu, The moderating efect of competitive status on the relation ship between customer satisfaction and retention, Total Qual. Manag. Bus. Excell. (4) (2017) 1–24, https://doi.org/10.1080/14783363.2017.1333413.

[5] L. Chen, K.S.M.T. Hossain, P. Butler, N. Ramakrishnan, B.A. Prakash, Flu gone viral: syndromic surveillance of flu on twitter using temporal topic models, 14th IEEE International Conference on Data Mining (ICDM), Shenzhen, PEOPLES R CHINA 2014, pp. 755–760, , https://doi.org/10.1109/ICDM.2014.137.

[6] C.M.K. Cheung, B.S. Xiao, I.L.B. Liu, Do actions speak louder than voices? The signaling role of social information cues in influencing consumer purchase decisions, Decis. Support. Syst. 65 (1) (2014) 50–58, https://doi,org/10.1016/j.dss. 2014.05.002

[7] S. Cheung, Y. Shirai, H. Morita, H. Takashima, Application of hidden Markoy model to analvze enthusiasts' dynamics of a lifestyle brand. 49th Hawaji International Conference on System Sciences (HICSS). Koloa. 2016, pp. 1557–1566.. https://doi org/10.1109/HICSS.2016.197.

[8] C.-M. Chiu, C.-C. Chang, H.-L. Cheng, Y.-H. Fang, Determinants of customer repurchase intention in online shopping, Online Inf. Rev. 33 (4) (2009) 761–784, https://doi.org/10.1108/14684520910985710.

[9] B.L. Connelly, S.T. Certo, R.D. Ireland, C.R. Reutzel, Signaling theory: a review and assessment, J. Manag. 37 (1) (2011) 39–67, https://doi.org/10.1177/ 0149206310388419.

[10] S. Davis, J.J. Inman, L. Mcaslister, Promotion has a negative efect on brand evaluations: or does it? Additional disconfirming evidence, J. Mark. Res. 29 (1) (1992) 143–148, https://doi.org/10.2307/3172499.

[111 V. Dickinson, Cash flow patterns as a proxy for firm life cycle, Account. Rey. 86 (6 (2011) 1969–1994, https://doi.org/10.2308/accr-10130.

[12] T.C. Earle, Trust in risk management: a model-based review of empirical research, Risk Anal, 30 (4) (2010) 541–574, https://doi,org/10.1111/i,1539-6924.2010 01398.x.

[13] Y. Fang, I. Qureshi, H. Sun, P. Mccole, E. Ramsey, K.H. Lim, Trust, satisfaction, and online repurchase intention: the moderating role of perceived effectiveness of ecommerce institutional mechanisms, MIS O. 38 (2) (2014) 407–427, https://doi. org/10.25300/MISQ/2014/38.2.04.

[14] S. Fournier, Consumers and their brands: developing relationship theory in consumer research. J. Consum. Res, 24 (4) (1998) 343–353. https://doi,org/10.1086/ 209515.

[15] R. Fu, H. Wang, W. Zhao, Dynamic driver fatigue detection using hidden Markoy model in real driving condition, Expert Syst, Appl, 63 (C) (2016) 397–411, https:/

[16] Y. Fu, G. Liu, S. Papadimitriou, H. Xiong, X. Li, G. Chen, Fused latent models for assessing product return propensity in online commerce, Decis. Support. Syst. 91 (2016) 77–88, https://doi.org/10.1016/j.dss.2016.08.002.

[17] R. Garfinkel, R. Gopal, B. Pathak, F. Yin, Shopbot 2.0: integrating recommendations and promotions with comparison shopping, Decis. Support. Syst. 46 (1) (2009)

61–69, https://doi.org/10.1016/j.dss.2008.05.006.

[18] G. Georgoulas, M.O. Mustafa, I.P. Tsoumas, J.A. Antonino-Daviu, V. Climente-Alarcon, C.D. Stylios, G. Nikolakopoulos, Principal component analysis of the startup transient and hidden Markov modeling for broken rotor bar fault diagnosis in asynchronous machines, Expert Syst. Appl. 40 (17) (2013) 7024–7033, https://doi. org/10.1016/j.eswa.2013.06.006.

[19] E. Ghazali, B. Nguyen, D.S. Mutum, A.A. Mohd-Any, Constructing online switching barriers: examining the efects of switching costs and alternative attractiveness on e-store loyalty in online pure-play retailers, Electron. Mark. 26 (2) (2016) 157–171, https://doi.org/10.1007/s12525-016-0218-1.

[20] S.E. Grifis, S. Rao, T.J. Goldsby, T.T. Niranjan, The customer consequences of returns in online retailing: an empirical analysis, J. Oper. Manag. 30 (4) (2012) 282–294, https://doi.org/10.1016/j.jom.2012.02.002.

[21] H.J.V. Heerde, P.S.H. Leeflang, D.R. Wittink, Decomposing the sales promotion bump with store data, Mark. Sci. (2004) 317–334, https://doi.org/10.1287/mksc 1040.0061.

[22] J.W. Hutchinson, J.W. Alba, Ignoring irrelevant information: situational determi nants of consumer learning, J. Consum. Res. 18 (3) (1991) 325–345, https://doi. org/10.1086/209263.

[23] L. Jiang, M. Jun, Z. Yang, Customer-perceived value and loyalty: how do key service quality dimensions matter in the context of b2c e-commerce? Serv. Bus. 10 (2) (2015) 301–317, https://doi.org/10.1007/s11628-015-0269-y.

[24] P. Jiang, X. Liu, J. Zhang, X. Yuan, A framework based on hidden Markov model with adaptive weighting for microcystin forecasting and early-warning, Decis. Support. Syst. 84 (C) (2016) 89–103, https://doi.org/10.1016/i.dss.2016.02.003

[25] P. Jiang, B. Rosenbloom, Customer intention to return online: price perception, attribute-level performance, and satisfaction unfolding over time, Eur. J. Mark. 39 (1/2) (2005) 150–174, https://doi.org/10.1108/03090560510572061.

[26] Z. Jiang, I. Benbasat, Virtual product experience: efects of visual and functional control of products on perceived diagnosticity and flow in electronic shopping, J. Manag. Inf. Syst. 21 (3) (2004) 111–147, https://doi.org/10.1080/07421222.2004. 11045817.

[27] T.O. Jones, Why satisfied customers defect, J. Manag. Eng. 73 (6) (1996) https:/ doi.org/10.1061/(ASCE)0742-597X(1996)12:6(11.2 , (11–11).

[28] A. Kirmani, The efect of perceived advertising costs on brand perceptions, J. Consum. Res. 17 (2) (1990) 160–171, https://doi.org/10.1086/208546.

[29] H.H. Kuan, G.-W. Bock, J. Lee, A cognitive dissonance perspective of customers online trust in multi-channel retailers, Proceedings of the Fifteenth European Conference on Information Systems (ECIS), St. Gallen, Switzerland, 2007, pp. 13–23 https://dblp.org/rec/bib/conf/ecis/KuanBL07.

[30] Y. Kwon, K. Kang, J. Jin, J. Moon, J. Park, Hierarchically linked infinite hidden Markov model based trajectory analysis and semantic region retrieval in a trajectory dataset, Expert Syst. Appl. 78 (2017) 386–395, https://doi.org/10.1016/j. eswa.2017.02.026.

[31] B.C. Lee, L. Ang, C. Dubelaar, Lemons on the web: a signaling approach to the problem of trust in internet commerce, J. Econ. Psychol. 26 (5) (2005) 607–623, https://doi.org/10.1016/j.joep.2005.01.001.

[32] K.N. Lemon, T.B. White, R.S. Winer, Dynamic customer relationship management: incorporating future considerations into the service retention decision, J. Mark. 66 (1) (2013) 1–14, https://doi.org/10.1509/jmkg.66.1.1.18447.

[33] S.T. Luk, LS. Yip. The moderator effect of monetary sales promotion on the re: lationship between brand trust and purchase behaviour. J. Brand Manag. 15 (6 (2008) 452–464. https://doi.org/10.1057/bm.2008.12.

[34] Y. Lyoyskava, S. Tan, C. Zhong, Online Discount Coupon Promotions & Repurchasing Behaviors: The Groupon Case (PhD thesis), MÃ¤lardalen University, 2012, http://www.diva-portal.org/smash/get/diva2:535745/FULLTEXT01.

[35] T. Mavlanova, R. Benbunan-Fich, G. Lang, The role of external and internal signals in e-commerce, Decis. Support. Syst. 87 (2016) 59–68, https://doi.org/10.1016/j. dss.2016.04.009

[36] V. Mittal, W.A. Kamakura, Satisfaction, repurchase intent, and repurchase behavior: investigating the moderating effect of customer characteristics, J. Mark. Res. 38 (1) (2001) 131–142, https://doi.org/10.1509/imkr.38.1.131.18832

[37] S. Moorthy, K. Srinivasan, Signaling quality with a money-back guarantee: the role of transaction costs, Mark, Sci. 14 (4) (1995) 442–466, https://doi,org/10.1287 mksc 14.4.442

[38] S. Mukheriee, H. Lamba, G. Weikum, Experience-aware item recommendation in evolving review communities, 15th IEEE International Conference on Data Mining (ICDM). Atlantic City, NJ. 2015, pp. 925–930. , https://doi.org/10.1109/ICDM. 2015.111.

[39] N.O. Ndubisi, C.T. Moi, Customers behavioural responses to sales promotion: the role of fear of losing face, Asia Pac. J. Mark. Logist. (2013), https://doi.org/10. 1108/13555850510672278

[40] P. Nelson, Advertising as information, J. Polit. Econ. 82 (4) (1974) 729–754, https://doi.org/10.1086/260231.

[41] J.A. Petersen, V. Kumar, Are product returns a necessary evil? Antecedents and consequences. J. Mark. 73 (3) (2009) 35–51. https://doi.org/10.1509/imkg 73 3.35.

[42] A.E. Schlosser, T.B. White, S.M. Lloyd, Converting web site visitors into buyers: how web site investment increases consumer trusting beliefs and online purchase in tentions, J. Mark. 70 (2) (2006) 133–148, https://doi.org/10.1509/jmkg.70.2.133.

[43] A. Tiwana, A.A. Bush, Spotting lemons in platform markets: a conjoint experiment on signaling, IEEE Trans. Eng. Manag. 61 (3) (2014) 393–405, https://doi.org/10.

1109/TEM.2014.2311074.

[44] T. Vojir, J. Matas, J. Noskova, Online adaptive hidden Markov model for multitracker fusion, Comput. Vis. Image Underst. 31 (5) (2016) 125–141, https://doi. org/10.1016/j.cviu.2016.05.007.

[45] S. Xiao, M. Dong, Hidden semi-Markov model-based reputation management system for online to ofline (o2o) e-commerce markets, Decis. Support. Syst. 77 (C) (2015) 87–99, https://doi.org/10.1016/j.dss.2015.05.013.

Xiaolin Li received her Ph.D. degree in computer science from School of Computer Science and Technology, Jilin University, China in 2005. She joined Department of Computer Science and Technology of Nanjing University from 2005 to 2007 as a post doctor. Currently she is an associate Professor at Department of Marketing and Electronic Business, School of Management, Nanjing University, China. Her current research inter ests include data mining, business intelligence, decision making.

Yuan Zhuang is a Master candidate at the School of Management, Nanjing University,

Jiangsu, China. Her research interests focus on e-commerce customer behaviors and data mining.

Benjiang Lu is an assistant Professor in the Department of Marketing and Electronic Business, School of Management, Nanjing University (NJU), China since 2018. He received his Ph.D. on Management Science and Engineering from Tsinghua University in 2018. His research interests include intra- and extra-organizational online knowledg sharing communities, employee performance and creativity, and e-commerce customer behaviors.

Guoqing Chen is currently EMC Chair Professor of Information Systems at the School of Economics and Management, Tsinghua University, Beijing, China. He received the Ph.D. degree from the Catholic University of Leuven, Leuven, Belgium, in 1992. His research interests include IT management and strategy, business Intelligence, and e-Business. Dr. Chen served as the founding president of China Association for Information Systems (AIS China Chapter, CNAIS).
