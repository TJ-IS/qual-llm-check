---
otero_id: 12102
otero_key: "8EWREW98"
title: "Filtering trust opinions through reinforcement learning"
authors: "Han Yu; Zhiqi Shen; Chunyan Miao; Bo An; Cyril Leung"
year: "2014"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2014.06.006"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Han Yu <sup>a,</sup>⁎, Zhiqi Shen <sup>a</sup>, Chunyan Miao <sup>a</sup>, Bo An <sup>a</sup>, Cyril Leung

<sup>a</sup> School of Computer Engineering, Nanyang Technological University 637659, Singapore

<sup>b</sup> Department of Electrical and Computer Engineering, the University of British Columbia, Vancouver, BC V6T1Z4, Canada

## a r t i c l e i n f o

Article history: Received 23 September 2013 Received in revised form 4 June 2014 Accepted 10 June 2014 Available online 26 June 2014

Keywords: Trust Reputation Credibility Collusion

## a b s t r a c t

In open online communities such as e-commerce, participants need to rely on services provided by others in order to thrive. Accurately estimating the trustworthiness of a potential interaction partner is vital to a participant's well-being. It is generally recognized in the research community that third-party testimony sharing is an effective way for participants to gain knowledge about the trustworthiness of potential interaction partners without having to incur the risk of actually interacting with them. However, the presence of biased testimonies adversely affects a participant's long term well-being. Existing trust computational models often require complicated manual tuning of key parameters to combat biased testimonies. Such an approach heavily involves subjective judgments and adapts poorly to changes in an environment. In this study, we propose the Actor–Critic Trust (ACT) model, which is an adaptive trust evidence aggregation model based on the principles of reinforcement learning. The proposed method dynamically adjusts the selection of credible witnesses as well as the key parameters associated with the direct and indirect trust evidence sources based on the observed bene<sup>fi</sup>ts received by the trusting entity. Extensive simulations have shown that the ACT approach signi<sup>fi</sup>cantly outperforms existing approaches in terms of mitigating the adverse effect of biased testimonies. Such a performance is due to the proposed accountability mechanism that enables ACT to attribute the outcome of an interaction to individual witnesses and sources of trust evidence, and adjust future evidence aggregation decisions without the need for human intervention. The advantage of the proposed model is particularly signi<sup>fi</sup>cant when service providers and witnesses strategically collude to improve their chances of being selected for interaction by service consumers.

© 2014 Elsevier B.V. All rights reserved.

## 1. Introduction

In open online communities where users are from diverse backgrounds and may have con<sup>fl</sup>icting interest, trust-based interaction decision support is needed to sustain long term interactions among them. Nowadays, such systems are quite common (e.g., service oriented computing systems [1], e-commerce systems [2], wireless communication networks [3], and multi-agent systems [4] etc.). In such environments in which services and devices usually have limited capabilities, users often have to interact with each other in order to complete complex tasks. These interactions usually involve an exchange of services, information, or goods with value. Sel<sup>fi</sup>sh users may renege on their commitments. thereby breaching the trust placed in them by others. Therefore. trust and reputation management mechanisms are often used to minimize the negative impact of sel<sup>fi</sup>sh users.

## 1.1. Background

Generally, users in an open online community that can be modeled as multi-agent systems (MASs) may play two types of roles [1]:

• service providers (SPs), who provide services, goods or information requested by others and do not need to rely on others to perform these services; and

• service consumers (SCs), who need to rely on service providers to accomplish certain tasks.

The main objective of evidence-based trust models is to estimate the trustworthiness of a potential interaction partner which represents its true behavior pattern. Evidences about a service provider from the perspective of a service consumer are usually from two sources:

• direct trust evidence: which consists of a service consumer's direct interaction experience with the service provider; and

• indirect trust evidence: which consists of third-party testimonies about the service provider from other service providers in the system.

In practical systems, it is not possible to de<sup>fi</sup>nitively know the trustworthiness of a service provider. Therefore, it is often estimated using trust evidences. The estimation of a service provider's trustworthiness derived from the direct trust evidence of a service consumer alone is called direct trust, while that derived from the indirect trust evidence is called indirect trust. According to [4], an estimation derived from both sources of trust evidence is commonly known as the reputation of a service provider. In the eyes of a service consumer, other service consumers who provide it with indirect trust evidence (i.e. testimonies)

about a service provider are regarded as witnesses. A witness's reliability in terms of providing useful testimonies is referred to as its credibility.

Since such systems tend to be very large in practice, service consumers often have to interact with service providers with whom they may not be very familiar (i.e. have little or no prior interaction experience with) [5]. Thus, it is both necessary and advantageous to allow service consumers to act as witnesses to provide their own <sup>fi</sup>rst-hand interaction experience as testimonies to other service consumers who lack such information. However, such an approach is not without its perils.

Third-party testimonies may be biased and, thus, degrade the accuracy of trust decisions [1]. Therefore, testimonies from witnesses need to be <sup>fi</sup>ltered before being used to evaluate a service consumer's reputation.

To this end, a number of evidence-based trust and reputation management (TRM) models have been proposed over the years. The general <sup>fl</sup>ow for a service consumer to decide which service provider to select for interaction is illustrated in Fig. 1. Each service consumer continuously records its direct interaction experience with service providers over time. When a service provider's trustworthiness needs to be evaluated, the service consumer may request third-party testimonies from witnesses, depending on the service consumer's con<sup>fi</sup>dence on its own direct trust evidence. These testimonies are preprocessed in an attempt to <sup>fi</sup>lter out unfair ratings. The resulting direct and indirect trust evidences are then aggregated to form a trustworthiness evaluation for that particular service provider. At the end of this process, the service consumer decides which service provider to interact with based on their trustworthiness evaluations.

## 1.2. Research objectives

Existing approaches for third-party testimony <sup>fi</sup>ltering and aggregation commonly involve a crucial step in which the weight assigned to each third-party testimony and the weight assigned to the direct and the indirect sources of trust evidence need to be determined [6–9].

However, existing approaches often require manual tuning of key parameters in their models which heavily involves subjective judgments and adapts poorly to changes in the environment.

In this paper, we address this limitation by proposing the Actor–Critic Trust (ACT) model based on the principles of the Actor-Critic Learning Method [10]. The ACT approach automates the adjustment of key threshold based parameters to eliminate human subjectivity and enhance the effectiveness of existing reputation evaluation models. Speci<sup>fi</sup>cally, it enables existing evidence-based trust models to dynamically make two important decisions when presented with third-party testimonies for a service provider: 1) how much weight to assign to its own personal direct trust evidence and the collective opinions from witnesses, and 2) how much weight to assign to the testimonies from each witness. Experimental results, presented in Section 4, show that the ACT approach outperforms state-of-the-art approaches by around 20% in terms of improving the accuracy of <sup>fi</sup>nding trustworthy service providers in the presence of biased testimonies, especially when witnesses collude with malicious service providers.

The rest of the paper is organized as follows. Section 2 reviews related work. Section 3 presents the basic notations used in this paper and the details of the proposed ACT approach. Section 4 describes the simulation test-bed and analyzes the results. The implications of the proposed approach for practical decision support in online product review systems are discussed in Section 5. Finally, Section 6 presents a summary of our contributions and possible future work.

## 2. Related work

It is widely recognized within the research community that the importance of incorporating mechanisms to mitigate the adverse effects of biased testimonies. In this section, we discuss some recent research work on aggregating trust evidence from different sources and <sup>fi</sup>ltering out biased testimonies. For a more comprehensive review of this <sup>fi</sup>eld, readers may refer to [1–3].

## 2.1. Trust evidence aggregation approaches

Evidence-based trust models often make use of two distinct sources of information to evaluate the trustworthiness of a service provider: direct trust evidence and indirect trust evidence. The majority of existing trust models adopt a weighted average approach when aggregating these two sources of trust evidence [3]. Direct trust evidence is often assigned a weight of $0 \leq \gamma \leq 1$ , and indirect evidence is assigned a corresponding weight of $1 - \gamma .$ Existing approaches for aggregating direct and indirect trust evidence can be divided into two broad categories: 1) static approaches, where the value of γ is pre-de<sup>fi</sup>ned; and 2) dynamic approaches, in which the value of γ is continually adjusted by the service consumer.

In many papers, static γ values for trust evidence aggregation. The majority of them tend to take a balanced approach by assigning a value of 0.5 to γ [6,9,7,11,12]. In some studies, the authors assign the value 0 [13,14] or 1 [15] to γ to exclusively use only one source of trust information. Barber and Kim [16] have empirically shown, without considering the presence of biased testimonies, that direct trust evidence is the most useful to a service consumer over the long term while indirect trust evidence gives an accurate picture more quickly. Thus, approaches that discard one source or the other, forfeit some of the advantages provided by evidence based trust models. However, using a static value for γ is also not always a good strategy.

![](/api/attachments/8EWREW98/fulltext/images/f957af8f0d015a3a57fbb2c04d6859ab81b4b05e44bcc897026e3ebdc71919eb.jpg)  
Fig. 1. The general <sup>fl</sup>ow of trust–aware interaction decision making for evidence-based trust and reputation management models, and the contributions by the proposed ACT approach.

Some researchers have explored adjusting the value of $\gamma$ dynamically based on different rationales. In [17], the value of γ is varied according to the number of direct observations on the behavior of a service provider $s _ { j }$ available to a service consumer $c _ { i } .$ It is assumed that every service consumer starts with no prior interaction experience with a service provider and gradually accumulates direct trust evidence over time. Initially, the service consumer relies completely on indirect trust evidence $( \mathrm { i } . \mathsf { e } . \gamma = 0 )$ to select service providers for interaction. As the number of its interactions with a service provider s increases, the value of γ also increases according to the formula

$$
\gamma = \left\{ \begin{array}{l l} \frac {N _ {j} ^ {i}}{N _ {\min}}, & \text { if } N _ {j} ^ {i} <   N _ {\min} \\ 1, & \text { Otherwise } \end{array} \right.\tag{1}
$$

where $N _ { j } ^ { i }$ is the total number of direct observations of $\overset { \cdot } { s _ { j } s }$ behavior by $c _ { i } ,$ and $N _ { m i n }$ is the minimum number of direct observations required in order to achieve a pre-determined acceptable level of error rate ε and con<sup>fi</sup>dence level ϑ. $N _ { m i n }$ is calculated following the Chernoff Bound Theorem [18]:

$$
N _ {m i n} = - \frac {1}{2 \varepsilon^ {2}} l n \bigg (\frac {1 - \vartheta}{2} \bigg).\tag{2}
$$

This approach is not concerned with <sup>fi</sup>ltering potentially biased third-party testimonies. Rather, its aim is to accumulate enough direct trust evidence so that a service consumer can make a statistically accurate estimation on the trustworthiness of a service provider without relying on indirect trust evidence. Since the value of γ increases to 1, this approach implicitly assumes that agent behaviors do not change with time. This may not always be true and limits the applicability of the approach under more dynamic scenarios. On the other hand, the ACT approach does not make this assumption and continuously make adjustments as the situation changes.

In [5], an approach based the Q-learning technique [19] to select a γ value from a pre-speci<sup>fi</sup>ed set of candidate γ values has been proposed. In order to select appropriate values for this set, expert opinions about the underlying system characteristics are assumed to be available. Based on the reward accumulated by a service consumer under different γ values, Q-learning selects the γ value associated with the highest accumulated reward at each time step. This work provided the <sup>fi</sup>rst step towards using interaction outcomes to enable the service consumer to weigh the two sources of trust evidence. However, as this method uses a predetermined set of γ values, its performance is affected by the quality of the expert opinions used to form the set of permissible γ values. In contrast, the ACT model adjusts both the γ value as well as the weight values for individual witnesses in <sup>fi</sup>nely grained steps so that it does not have to rely on the subjective opinions of the designer.

## 2.2. Testimony filtering approaches

A number of models for <sup>fi</sup>ltering potentially biased third-party testimonies have been proposed. However, these models usually assume the presence of some infrastructure support or special characteristics in the environment. In this section, some representative models in this sub-<sup>fi</sup>eld are discussed.

The model in [20] makes use of the social relationships among the members of a community to determine the credibility of witnesses. Pre-determined fuzzy rules are used to estimate the credibility of each witness which, in turn, is used as the weight of its testimony for a service provider when aggregating all the testimonies. This model relies on the availability of social network information among the agents which may not be present in many systems.

In [21], unfair testimonies are assumed to exhibit certain characteristics. The proposed approach is closely coupled with the Beta Reputation System (BRS) [22] which records testimonies in the form of counts of successful and unsuccessful interactions with a service provider. The received testimonies are aggregated with equal weights to form a majority opinion and then, each testimony is tested to see if it is outside the q quartile and $\left( 1 { - } q \right)$ quartile of the majority opinion. If so, the testimony is discarded and the majority opinion updated. This model assumes that the majority opinion is always correct. Thus, it is not effective in highly hostile environments where the majority of witnesses are malicious.

In [6], it is assumed that the direct experience of the service consumer is the most reliable source of belief about the trustworthiness of a particular service provider, and it is used as the basis for <sup>fi</sup>ltering testimonies before aggregating them to form a reputation evaluation. An entropy-based approach is proposed to measure how much a testimony deviates from the current belief of the service consumer before deciding whether to incorporate it into the current belief. However, by depending on having suf<sup>fi</sup>cient direct interaction experience with a service provider, this assumption con<sup>fl</sup>icts with the purpose for relying on third-party testimonies, which is to help service consumers make better interaction decisions when they lack direct trust evidence.

The model in [7] supports interaction outcomes recorded in multidimensional forms. It applies two rounds of clustering of the received testimonies to identify testimonies which are extremely positive or extremely negative about a trustee. If neither the extremely positive opinion cluster nor the extremely negative opinion cluster forms a clear majority, they are both discarded as unfair testimonies and the remaining testimonies are used to estimate the reputation of a service provider. Otherwise, the majority cluster is considered as the reliable testimonies. Due to its iterative nature, the computational complexity of this method is high, with a time complexity of $O ( m n ^ { 2 } )$ where m is the number of candidate service providers whose reputations need to be evaluated and n is the number of testimonies received for each candidate service provider. The method is also not robust in hostile environments where the majority of the witnesses are malicious.

## 3. The ACT approach

## 3.1. System model

Before discussing details of the proposed model, we introduce the system model under which the ACT approach is designed to operate. At each time step t, a service consumer $c _ { i }$ will interact with at most one service provider $s _ { j }$ in our target system. For each interaction, $c _ { i }$ chooses a service provider from among several candidates based on their estimated trustworthiness values. Whenever c needs to assess the trustworthiness of $s _ { j } ,$ it draws upon both its own direct trust evidence about $s _ { j }$ (if there is any) as well as testimonies from a list of witnesses $W _ { i j } ( \bar { t } )$ which are known by $c _ { i }$ at time t to have previously interacted with $S _ { j \cdot i }$ A witness $w _ { k }$ may reply to $c _ { i } ^ { \prime } s$ request at time step t with a testimony $d _ { j } ^ { k } ( t )$ . In this study, a malicious $w _ { k }$ may distort its testimonies before sharing them with others. The service provider chosen for interaction by $c _ { i }$ at time step t is affected by the selection of witnesses as well as the weights given to direct and indirect trust evidence.

Each interaction with $s _ { j } , c _ { i }$ incurs a utility cost of $C _ { i j } .$ I $\mathrm { f } \ s _ { j }$ successfully completes the task assigned to it by $c _ { i } ,$ c receives a utility gain of G. We assume that the outcome of the interaction $O _ { i j } ( t )$ can be observed by $c _ { i }$ within the same time step in which the interaction occurs. We further assume that the interaction outcome is either successfu $( O _ { i j } ( \mathrm { t } ) = 1 )$

or unsuccessful $( O _ { i j } ( \mathrm { t } ) = 0 )$ . By comparing the recommendation $d _ { j } ^ { k } ( \mathfrak { t } )$ by each $w _ { k } { \in } W _ { i j } ( \mathsf { t } )$ about $s _ { j }$ at time t with $O _ { i j } ( \mathrm { t } ) , c _ { i }$ can learn the ranking of each $w _ { k }$ in $W _ { i j } ( \mathfrak { t } )$ . New witnesses for discovered by $c _ { i }$ over time are added into $W _ { i j } .$ . The interaction outcome value, $O _ { i j } ( \mathrm { t } ) ,$ , is further compared with the recommended interaction decision value, $D _ { i j } ^ { d } ( \mathfrak { t } )$ , based on direct trust evidence and the value, $D _ { i j } ^ { i n d } ( \mathrm { t } )$ , based on indirect trust evidence from the testimonies of selected witnesses. Reward and penalty values are assigned to these two sources of trust evidence by c in its local record to determine how much to rely on either source in the future. In the presence of uncertainty in service providers' performance and the credibility of third-party testimonies, the objective of an individual service consumer is to improve its chance of <sup>fi</sup>nding trustworthy service providers.

The general framework of the proposed ACT approach is presented in Fig. 2. Each service consume $\dot { c } _ { i }$ keeps two local lists: 1) a list of known witnesses, and 2) a list of known service providers. Since a witness may only have interacted with a few service providers, the list of known witnesses organizes the witnesses into sub-lists indexed according to known service providers. The list of known service providers stores the direct trust evidence $c _ { i }$ has for each known service provider and the weight assigned to the direct trust evidence $\gamma _ { i j }$ in the case of that service provider. These two lists grow as $c _ { i }$ acquires more interaction experience with these two types of system participants.

The ACT approach is designed based on a variant of the reinforcement learning (RL) approach — the actor–critic method [23]. The actor–critic method requires minimal computation when selecting an action. The actor module represents the policy used to choose which witnesses' testimonies should be selected and how much weight each of them should have when aggregating them together to form the indirect trust evidence. The policy also determines how much weight should be given to the direct and indirect trust evidence in order to evaluate the service provider's trustworthiness. The critic module represents the value function that determines whether the service provider $c _ { i }$ is better off or worse off after each interaction with a selected service provider $s _ { j } .$ Overtime, the learning parameters of the ACT approach are updated in such a way that more preference is given to witnesses and the source of trust evidence that enhance $c _ { i } ^ { \prime } s$ well-being.

Although the ACT approach can be used together with many possible trust evaluation models, to be speci<sup>fi</sup>c, we assume that the popular Beta Reputation System (BRS) [22] is used as the underlying trust evaluation method. The direct trust for s by c at t can be calculated using the BRS as:

$$
\tau_ {i j} ^ {d} (t) \triangleq \frac {\alpha + 1}{\alpha + \beta + 2}\tag{3}
$$

where α is the total number of successful interactions between $s _ { j }$ and $c _ { i } ,$ while $\beta$ is the total number of unsuccessful interactions between s and c<sub>i</sub> up to t.

## 3.2. Learning witness credibility ranking

According to the principles of reinforcement learning, the ACT model needs to de<sup>fi</sup>ne a reward function $( r _ { i j } )$ for a service consumer which, in turn, requires the speci<sup>fi</sup>cation of a source of reinforcement $( \mu _ { j } ^ { i } ( t ) )$ . In the critic module, the reward function for $c _ { i }$ is de<sup>fi</sup>ned as:

$$
r _ {i j} \triangleq \mu_ {j} ^ {i} (t) \cdot \left(G - C _ {i j}\right) - \left(1 - \mu_ {j} ^ {i} (t)\right) \cdot C _ {i j}.\tag{4}
$$

$r _ { i j }$ is computed at the end of each interaction between $c _ { i }$ and $s _ { j } .$ The parameter $\mu _ { j } ^ { i } ( t )$ is de<sup>fi</sup>ned as:

$$
\mu_ {j} ^ {i} (t) = \left\{ \begin{array}{l l} 0, & \text { if } O _ {i j} (t) = 0 | D _ {i j} (t) = 1 \\ 1, & \text { if } O _ {i j} (t) = 1 | D _ {i j} (t) = 1 \end{array} \right.\tag{5}
$$

$D _ { i j } ( t )$ denotes the overall decision by $c _ { i }$ to interact with $s _ { j }$ at time t based on both the direct and indirect trust evidence currently available. Here, we only consider the case when the decision is to interact with a service provider $( \mathrm { i } . \mathsf { e } . D _ { i j } ( t ) = 1 )$ , because in order for a service consumer $c _ { i }$ to be able to observe the actual interaction outcome with a service provider $\cdot s _ { j }$ at the end of time $t , s _ { j }$ must be selected by $c _ { i }$ for interaction in that time step. When $D _ { i j } ( t ) = \dot { 0 } ,$ , it implies that c deems s untrustworthy based on its reputation value. Thus, in these cases, no interaction between them will take place at that time and no $O _ { i j } ( t )$ value can be observed. In this way, the source of reinforcement is related to the performance of a witness as judged by the actual outcome of an interaction. Note that learning only occurs if an interaction takes place. We assume that the agents' direct trust values and indirect trust values are normalized to a range of [0, 1]. A testimony $t e s t _ { j } ^ { k } ( t )$ is simply $w _ { k } { } ^ { \prime } s$ direct trust value for s based on its own direct trust evidence up to time t. Thus, its value is also within the range [0, 1].

![](/api/attachments/8EWREW98/fulltext/images/068b5d51e9df34923c94d6f703435a5730332c61a1aff5d767d3db5d93aad7dc.jpg)  
Fig. 2. The general framework of the ACT approach based on reinforcement learning

Once the interaction outcome is known, a reward correction value $\theta _ { k j }$ is computed for each of the M selected witnesses whose testimonies have been used to calculate the reputation of s namely:

$$
\theta_ {k j} = \frac {1}{T _ {k j}} \sum_ {t = 1} ^ {T _ {k j}} \left[ d _ {j} ^ {k} (t) \cdot \left(1 - O _ {i j} (t)\right) \right].\tag{6}
$$

$T _ { k j }$ denotes the total number of times that w 's testimonies about has been used by $c _ { i } ,$ and $d _ { j } ^ { k } ( t )$ represents the interaction recommendation implied by $w _ { k } { } ^ { \prime } s$ testimony, test<sup>k</sup>(t), on $s _ { j }$ at time step t and is given by:

$$
d _ {j} ^ {k} (t) = \left\{ \begin{array}{l l} 0, & \text { if } t e s t _ {j} ^ {k} (t) <   T h \\ 1, & \text { otherwise } \end{array} \right.\tag{7}
$$

where $T h { \in } [ 0 , 1 ]$ is a prede<sup>fi</sup>ned threshold value. $\theta _ { k j }$ increases with the number of times that $w _ { k }$ has given testimonies suggesting a service provider is trustworthy but the actual interaction outcome is unsuccessful. It is used to penalize the act of unfairly praising a service provider, which is the most common form of collusion between service providers and witnesses.

The critic process is carried out by updating the learning parameter $p _ { k j }$ for each of the M witnesses whose testimonies resulted in the selection of $\dot { s } _ { j }$ by ${ \mathrm { ~ \vec { ~ } { ~ C } } } _ { i }$ at t. This is achieved by jointly considering the latest reward function value, the accumulated reward, the reward correction value, the previous credibility ranking of $\dot { c } _ { i } ,$ and the learning rate parameters as follows:

$$
p _ {k j} \leftarrow p _ {k j} + \rho \cdot \left(r _ {i j} - \widetilde {r _ {i j}} - \delta \cdot \theta_ {k j}\right) \left(1 - \pi_ {k j}\right).\tag{8}
$$

The constant $( 0 < \rho \leq 1 )$ denotes the learning rate. As ρ increases, the learning parameter $p _ { k j }$ changes more rapidly as new interaction outcomes become available. In this paper, we choose $\textsf { a } \rho$ value close to 0 to make $p _ { k j }$ vary more smoothly. The constant $( 0 < \delta \leq 1 )$ represents the bias towards penalizing collusion when updating the learning parameter; we select its value to be signi<sup>fi</sup>cantly smaller than 1 to avoid drastic changes in the value of $p _ { k j } .$

The credibility ranking value $\pi _ { k j }$ of each known w with regard to a service provider $s _ { j }$ is calculated using the Gibbs softmax method [19] as:

$$
\pi_ {k j} = \frac {e ^ {p _ {k j}}}{\sum_ {l = 1} ^ {M} e ^ {p _ {l j}}}.\tag{9}
$$

The resulting values of $\pi _ { k j }$ is used to rank the witnesses known to c to facilitate subsequent witness selections. The sum of all $\pi _ { k j }$ values always equals to 1. Thus, it can be regarded as the probability of soliciting testimonies from each of the witnesses known to $c _ { i }$ at time t.

After the credibility ranking values are calculated, the total accumulated reward $\widetilde { r } _ { i j }$ is updated. It is used as a reference in the process of evaluating the well-being o $\dot { \boldsymbol { { \mathbf { \ell } } } } _ { c _ { i } }$ resulted from interactions with $s _ { j } .$ It is updated as:

$$
\widetilde {r _ {i j}} \leftarrow \varphi \cdot \widetilde {r _ {i j}} + (1 - \varphi) \cdot r _ {i j}\tag{10}
$$

where the constant $0 < \varphi \leq 1 )$ determines the in<sup>fl</sup>uence of the latest rewards in the smoothed baseline reward $\widetilde { r _ { i j } } .$ When $\varphi = 1$ , only the current reward is used to evaluate the credibility of each witness.

The indirect trust for s by c can be computed as the sum of witness testimonies weighted by their respective credibility ranking values:

$$
\tau_ {i j} ^ {i n d} (t) \triangleq \frac {\sum_ {k = 1} ^ {M} \left(\pi_ {k j} \cdot t e s t _ {j} ^ {k} (t)\right)}{\sum_ {k = 1} ^ {M} \pi_ {k j}}.\tag{11}
$$

## 3.3. Learning the weights for sources of trust evidence

With the values of $\mathbf { \dot { \tau } } _ { \bar { \imath } \bar { \jmath } } ^ { d } ( t )$ and $\tau _ { i j } ^ { i n d } ( t )$ calculated using Eqs. (3) and (11) respectively, the next step is to aggregate them to compute the reputation of s<sub>j</sub>. In the ACT approach, for each s<sub>j</sub> known to $c _ { i } ,$ two critic modules are used to learn the weights for the two sources of trust evidence and one actor module is used for estimating the trustworthiness of $s _ { j } .$ . The critic module in the proposed method determines the relative merit of each source of trust evidence through reward accumulation. The learning process is similar to that presented in Section 4.1. Since the two critic modules are essentially the same but only use different sources of trust evidence as input data, in the following, we only discuss the critic module for the direct trust evidence source.

For this step, the value function for the direct trust evidence is designed as:

$$
r _ {d} \triangleq \widetilde {\mu} (t) \cdot R + \left(1 - \widetilde {\mu} (t)\right) \cdot P\tag{12}
$$

$$
\widetilde {\mu} (t) = \left\{ \begin{array}{c c} 1, & \text { if } O _ {i j} (t) = D _ {i j} ^ {d} (t) \\ & 0, \text { otherwise } \end{array} \right.\tag{13}
$$

$$
D _ {i j} ^ {d} (t) = \left\{ \begin{array}{c} 1, \text {   if   } \tau_ {i j} ^ {d} (t) \geq T h \\ 0, \text {   otherwise   } \end{array} \right.\tag{14}
$$

$r _ { d }$ can be considered as the time averaged per interaction reward achieved by $c _ { i }$ through relying on its direct trust evidence source about $s _ { j }$ with the current weight value $\gamma _ { i j } .$ . R and P are predetermined constant values for reward and penalty, based on the consequences of the interaction decision. The ratio of R to $P ,$ rather than their absolute values, is important to the learning process. A small R:P ratio means that trust is hard for a service provider to gain, but easy to lose. The variable $\widetilde { \mu } ( t ) )$ determines whether this trust evidence source should be rewarded or penalized at time t. Its value toggles between 0 and 1 according to the relationship between the interaction decision $D _ { i j } ^ { d } ( t )$ , which is related to the direct trustworthiness evaluation $( 0 \leq \tau _ { i j } ^ { \bar { d } } ( t ) \leq 1 )$ , and the actual interaction outcome $O _ { i j } ( t )$ . As $D _ { i j } ^ { d } ( t )$ is only one component of the overall interaction, it is possible that even as $D _ { i j } ^ { d } ( t )$ suggests not to interact with $s _ { j } ,$ the overall decision is otherwise.

Once the latest $r _ { d }$ is calculated, it is compared with the baseline reward $\widetilde { r } _ { d }$ accumulated by this trust evidence source to update the learning parameter $p _ { d }$ according to:

$$
p _ {d} \leftarrow p _ {d} + \rho \cdot (r _ {d} - \widetilde {r} _ {d}) \cdot (1 - \pi_ {d}).\tag{15}
$$

After $p _ { d }$ is updated, $\widetilde { r } _ { d }$ is updated to incorporate the latest reward $r _ { d } .$

$$
\widetilde {r} _ {d} \leftarrow \varphi \cdot \widetilde {r} _ {d} + (1 - \varphi) \cdot r _ {d}.\tag{16}
$$

$\widetilde { r } _ { d }$ can be treated as a basis for comparing whether $c _ { i }$ is better off or worse off by aggregating the direct trust evidence into the estimation for the trustworthiness of $\dot { \boldsymbol { s } } _ { j }$ using the latest $\gamma _ { i j }$ value.

Similarly, the learning parameter $p _ { i n d }$ for the indirect source of trust evidence can be obtained. When both $p _ { d }$ and $p _ { i n d }$ are obtained, the learning parameters $\pi _ { d }$ and $\pi _ { i n d }$ are updated as:

$$
\pi_ {d} \triangleq \frac {e ^ {p _ {d}}}{e ^ {p _ {d}} + e ^ {p _ {i n d}}}\tag{17}
$$

$$
\pi_ {i n d} \triangleq \frac {e ^ {p _ {i n d}}}{e ^ {p _ {d}} + e ^ {p _ {i n d}}}.\tag{18}
$$

$\pi _ { d }$ and $\pi _ { i n d }$ can be treated as the probability of selecting each source of trust evidence $\pi _ { d } + \pi _ { i n d } = 1$ . In the ACT approach, the value of $\gamma _ { i j }$ is

set to $\pi _ { d } .$ The working process of the ACT approach is shown in Algorithm 1.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1. The ACT testimony aggregation algorithm
Require: $\tau_{ij}^{d}(t)$ for all $s_j$ with who $c_i$ had prior interactions.
1: if $c_i$ needs to select an SP for interaction then
2: explorationProbability = random(0, 1)
3: if explorationProbability $\leq Pr(Exp)$ then
4: Randomly select an unknown SP with for interaction
5: else
6: Rank known SPs in descending order of their $\tau_{ij}^{d}(t)$ values
7: for each candidate known SP $s_j$ do
8: $c_i$ asks the top $M$ ranked witnesses known to $c_i$ for testimonies on $s_j$
9: end for
10: Evaluate $\tau_{ij}^{ind}$ for each known candidate SP following Eq.(11)
11: Evaluate $r_j(t)$ for each known SP following Eq.(19)
12: Delegate the task to the SP with the highest $r_j(t)$ value
13: Observe the interaction outcome $O_{ij}(t)$ with the selected SP
14: Update $\tau_{ij}^{d}(t)$ following Eq.(3)
15: Update the $p_{kj}$ values according to Eq.(8) for all witnesses $w_k$ who provided testimonies for the selected SP in the last time step
16: Update their $\pi_{kj}$ values following Eq.(9)
17: Rank known witnesses in descending order of their new $\pi_{kj}$ values
18: Update the $\gamma_{ij}$ and $(1 - \gamma_{ij})$ values according to Eq.(17) and Eq.(18) respectively
19: end if
20: end if
</div>

## 3.4. Exploration vs. exploitation

While the strategy for exploiting known witnesses with high credibility is relatively straightforward (i.e. selecting the top M most credible witnesses to request testimonies from), balancing it with exploration for addition witnesses requires careful design. In the ACT approach, the exploration process is controlled by two parameters: 1) an exploration probability Pr(Exp), and 2) the magnitude of M. The value of Pr(Exp) is initialized to 1 at the start of a service consumer c 's life time to enable $c _ { i }$ to explore when the list of known witnesses is empty. The value of $P r ( E x p )$ is gradually decreased over time until it reaches a pre-de<sup>fi</sup>ned minimum value, $P r _ { m i n } .$ Testimonies returned by previously unknown witnesses are given the bene<sup>fi</sup>t of the doubt and included in the calculation of the service provider's reputation with weight values equal to the lowest $\pi _ { k j }$ among that of the selected known witnesses. This is to ensure that $c _ { i }$ will always have some opportunity to discover new witnesses.

A service provider $s _ { j } ^ { \prime } s$ reputation is calculated as:

$$
r _ {j} (t) \triangleq \gamma_ {i j} \cdot \tau_ {i j} ^ {d} (t) + \left(1 - \gamma_ {i j}\right) \cdot \tau_ {i j} ^ {i n d} (t).\tag{19}
$$

$r _ { j } ( t )$ represents the overall reputation of s and is used by $c _ { i }$ to estimate $\boldsymbol { s } _ { j } ^ { \prime } \boldsymbol { s }$ trustworthiness. At each time step, c might have more than one candidate service providers to choose from. In this study, we assume that c always selects the service provider with the highest overall reputation for interaction. For convenience, the symbols used in this paper are listed in Table 1.

## 4. Experimental evaluations

In order to comprehensively evaluate the performance of the ACT model under different witness behavior conditions, we have designed a test-bed which allows the well-being of service consumers adopting different approaches to be gauged. Through extensive simulations varying the witness population composition, it has been shown that the ACT approach signi<sup>fi</sup>cantly outperforms existing approaches in terms of the reduction in normalized average utility loss and, in the case of colluding witnesses, the reduction in their collusion power.

Table 1 Symbols used in this paper.

<table><tr><td>Symbol</td><td>Meaning</td></tr><tr><td> $c_i$ </td><td>A service consumer.</td></tr><tr><td> $C_{ij} \in \mathbb{R}^+$ </td><td>The cost incurred by  $c_i$  when engaging the service of  $s_j$ .</td></tr><tr><td> $d_j^k(t) \in \{0,1\}$ </td><td>The interaction decision as suggested by  $test_j^k(t) \in [0,1]$ .</td></tr><tr><td> $D_{ij}^d(t) \in \{0,1\}$ </td><td>The decision by  $c_i$  on whether to interact  $s_j$  with at time  $t$  based on direct trust evidence only.</td></tr><tr><td> $D_{ij}^{ind}(t) \in \{0,1\}$ </td><td>The decision by  $c_i$  on whether to interact  $s_j$  with at time  $t$  based on indirect trust evidence only.</td></tr><tr><td> $D_{ij}(t) \in \{0,1\}$ </td><td>The overall decision by  $c_i$  on whether to interact  $s_j$  with at time  $t$  based on both direct and indirect trust evidence.</td></tr><tr><td> $\delta \in (0,1]$ </td><td>The bias towards penalizing collusion.</td></tr><tr><td> $G \in \mathbb{R}^+$ </td><td>The utility derived from a successful interaction.</td></tr><tr><td> $\mu_j^j(t) \in \{0,1\}$ </td><td>The outcome-based determinant of reward/punishment during learning.</td></tr><tr><td> $O_{ij}(t) \in \{0,1\}$ </td><td>The outcome of an interaction between  $c_i$  and  $s_j$  at time  $t$ .</td></tr><tr><td> $P \in \mathbb{R}^+$ </td><td>The penalty assigned to a source of trust evidence.</td></tr><tr><td> $p_d \in \mathbb{R}$ </td><td>The learning parameter for updating the credibility ranking of the direct trust evidence source.</td></tr><tr><td> $p_{kj} \in \mathbb{R}$ </td><td>The learning parameter for updating the credibility ranking of  $w_k$  with respect to  $s_j$ .</td></tr><tr><td> $\pi_{kj} \geq 0$ </td><td>The credibility of  $w_k$  for  $s_j$  in  $c_i$ &#x27;s local record.</td></tr><tr><td> $\pi_d \geq 0$ </td><td>The weight assigned to the direct source of trust evidence by a consumer.</td></tr><tr><td> $R \in \mathbb{R}^+$ </td><td>The reward assigned to a source of trust evidence.</td></tr><tr><td> $r_j(t) \in [0,1]$ </td><td>The reputation of  $s_j$  at time  $t$ .</td></tr><tr><td> $r_{ij} \in \mathbb{R}$ </td><td>The reward for  $c_i$  derived from interactions with  $s_j$ .</td></tr><tr><td> $\widetilde{r}_{ij} \in \mathbb{R}$ </td><td>The accumulated reward for  $c_i$  from past interactions with  $s_j$ .</td></tr><tr><td> $\rho \in (0,1]$ </td><td>The learning rate parameter.</td></tr><tr><td> $s_j$ </td><td>A service provider.</td></tr><tr><td> $test_j^k(t) \in [0,1]$ </td><td>A testimony from  $w_k$  with regard to  $s_j$  at time  $t$ .</td></tr><tr><td> $\tau_{ij}^d(t) \in [0,1]$ </td><td>The direct trust placed on  $s_j$  by  $c_i$  at time  $t$ .</td></tr><tr><td> $\tau_{ij}^{ind}(t) \in [0,1]$ </td><td>The indirect trust placed on  $s_j$  by  $c_i$  at time  $t$ .</td></tr><tr><td> $w_k$ </td><td>A witness.</td></tr><tr><td> $\theta_{kj} \in [0,1]$ </td><td>The reward correction value for  $w_k$  with regard to  $s_j$ .</td></tr><tr><td> $W_{ij}(t)$ </td><td>A list of witnesses for  $s_j$  known to  $c_i$  at time  $t$ .</td></tr></table>

## 4.1. Simulation test-bed

The test-bed simulates a scenario where a number of service consumers need the services offered by service providers. A service consumer incurs a cost of $C _ { i j }$ in order to utilize the service of a service provider. If the service provider acts honestly, i.e. satis<sup>fi</sup>es the service consumer's request, the service consumer gains an amount of utility of G after the interaction; otherwise, it gains zero utility. Therefore, the maximum average utility gain a service consumer can achieve is $G - C _ { i j } ,$ corresponding to all its interactions with service providers being successful; the minimum of this value $\mathrm { i } s - C _ { i j } ,$ if all its interactions are unsuccessful.

The main purpose of this test-bed is to investigate the effectiveness of the proposed ACT approach in mitigating the adverse effects of unfair testimonies relative to existing approaches. Although there are multiple ways of modeling the malicious behavior of service providers in a system, it is impractical to investigate the proposed model for all possible service provider population con<sup>fi</sup>gurations. In our experiments, we adopt one of the common modeling approaches used by previous studies such as [9]. The service provider population is hostile to the service consumers and consists of

• 10% honest service providers (which renege randomly with a probability of 10%);

• 10% Type I dishonest service providers (which renege randomly with an initial probability of 40%);

• 40% Type II dishonest service providers (which renege randomly with an initial probability of 60%); and

• 40% Type III dishonest service providers (which renege randomly with an initial probability of 80%).

Except for the honest service provider group, the behavior patterns of all other groups changes gradually during the simulation. A service provider's behavior can change according to three different pro<sup>fi</sup>les: 1) increasing reneging probability, 2) decreasing reneging probability, or

3) unchanging reneging probability. The magnitude of each change is randomly chosen from the interval [0, 0.01]. Each dishonest service provider chooses one of the three pro<sup>fi</sup>les in each interaction with equal probability (i.e. <sup>1</sup>). The test-bed environment consists of 1000 service providers with different behavior patterns. During each round of simulation, each service consumer attempts to solve a total of $N _ { m }$ problems. The service consumers select service providers for interaction based on their reputation. The outcome of the interaction is assumed to be binary, namely successful or unsuccessful, depending on whether the service provider provides the requested service.

There are 100 witnesses who accumulate direct trust evidence about the service providers and respond to service consumers requesting testimonies. When a request for testimony is received by a witness it will return a testimony to the requester if it has prior interaction experience with the particular service provider in the request; otherwise, it will decline the request. Two categories of malicious testimony sharing strategies are studied: 1) random lying, and 2) collusive lying.

In the case of random lying, a malicious witness does not collude with any other service provider. It either positively distorts a testimony (ballot-stuffing) or negatively distorts a testimony (badmouthing) following a preset lying probability. In the case of collusive lying, a number of service providers collude with lying witnesses to in<sup>fl</sup>ate their reputation in the eyes of service consumers (ballot-stuffing). The colluding witnesses do not give unfair testimonies about service providers who are outside the collusion ring. This is because, relative to a large online community, the sizes of collusion rings tend to be small. The costs for ballot-stuf<sup>fi</sup>ng within collusion rings are signi<sup>fi</sup>cantly less than the costs for badmouthing a large number of competitors. The actual situation observed on e-commerce systems such as eBay.com supports this assumption [9]. In both random lying and collusive lying cases, the distortions are implemented as offset values added to or subtracted from the original testimony. Two types of unfair testimonies are supported in the test-bed:

• Moderately Unfair Testimonies (MUT): the magnitude of the offset is randomly chosen in the range [0.1, 0.4];

• Highly Unfair Testimonies (HUT): the magnitude of the offset is randomly chosen in the range [0.8, 1.0].

The values of the distorted testimonies are always kept within the range [0, 1] by hard-limiting to 1 (or 0) if the distorted testimonies after adding (or subtracting) exceeds 1 (or falls below 0).

In the proposed ACT approach, we use BRS as the trust evaluation model in this study. The values selected for the parameters in the ACT approach are listed in Table 2. Through these choices of values, we give preference for a medium rate of learning and do not allow the latest interaction outcome to outweigh past observed behaviors of a service provider. They can achieve a good balance between learning speed and smooth changes in learning results as suggested by existing literature [10,19]. By adopting a well balanced set of values for the learning algorithm parameters and varying the behavior patterns of the witness agent population, the experiments allow us to draw reasonable conclusions about the relative performances of the comparative approaches.

## 4.2. Evaluation metrics

Two evaluation metrics from [9] are adopted to facilitate comparisons with state-of-the-art methods:

1. Normalized Average Utility Leftover (NAUL): the normalized average utility $( 0 \leq \sigma \leq 1 )$ measures the average per time step utility gain as a percentage of the maximum possible utility gain for each service consumer over its lifetime. It is calculated as:

Parameter values used in the simulations

<table><tr><td>Parameter</td><td>Th</td><td> $\varphi$ </td><td> $\delta$ </td><td> $\rho$ </td><td>M</td><td> $N_{m}$ </td><td>G</td><td> $C_{ij}$ </td><td>R</td><td>P</td><td> $Pr_{min}$ </td></tr><tr><td>Value</td><td>0.5</td><td>0.6</td><td>0.1</td><td>0.4</td><td>10</td><td>200</td><td>5</td><td>1</td><td>1</td><td>-10</td><td>0.1</td></tr></table>

$$
\sigma = \frac {1}{T N} \frac {\sum_ {t = 1} ^ {T} \sum_ {i = 1} ^ {N} g _ {i} (t) - g _ {m i n}}{g _ {m a x} - g _ {m i n}}.\tag{20}
$$

T is the total number of times a service consumer $c _ { i }$ has interacted with the service providers, N is the number of service consumers adopting the same approach as c<sub>i</sub> does in the test-bed and $g _ { m a x } =$ $G - C _ { i j } , g _ { m i n } = - C _ { i j } . g _ { i } ( t )$ is the actual utility gain of each c after each interaction at time t. If the interaction is successful $g _ { i } ( t ) = g _ { m a x } ;$ otherwise, $g _ { i } ( t ) = g _ { m i n } .$ NAUL is then $( 1 - \sigma )$ . With perfect foresight, $( 1 - \sigma ) = 0 .$ . It measures the percentage difference between the actual utility gain and the maximum possible utility gain per service consumer per time step (i.e., the leftover utility that the service consumers following a trust-aware interaction approach are not able to gain). The closer $( 1 - \sigma )$ is to 0, the better the performance of a given model.

2. Collusion Power: the Collusion Power, cp, is a measure of the effectiveness of different models in the face of collusion [9]. It is de<sup>fi</sup>ned as:

$$
c p = \frac {\sum_ {c _ {i} \in A _ {n c}} \# t r y (c _ {i})}{| A _ {n c} | \cdot N _ {m}}\tag{21}
$$

where $A _ { n c }$ denotes the set of non-colluding service consumers, $c _ { i }$ is a service consumer in this set, and $\# t r y ( c _ { i } )$ is the number of times c interacted with any colluding service provider during the simulation. In essence, cp represents the percentage of all tasks delegated to any of the colluding service providers in the simulated community.

## 4.3. Experiment design

For each experiment, the composition of the common witness population is altered to simulate different scenarios. In the following sections, Hon denotes a population consisting entirely of honest common witnesses. BMn denotes a population consisting of n% badmouthing witnesses and $( 1 0 0 - n ) \%$ honest witnesses. BSn denotes a population consisting of n% ballot-stuf<sup>fi</sup>ng witnesses and $( 1 0 0 - n ) \%$ honest witnesses. The malicious witness populations consist of half giving out MUTs and half giving out HUTs.

The experiments include two parts:

1. Studying the effectiveness of the adaptive trust evidence aggregation module of the ACT approach (labeled as ACT″). Under ACT″, the testimonies from witnesses are treated as of equal importance and aggregated through simple averaging. The $A C T ^ { \prime \prime }$ module only adjusts the weights of the direct trust evidence and the indirect trust evidence, $\gamma ,$ when calculating the reputation of a candidate trustee.

2. Studying the effectiveness of the ACT approach as a whole (labeled as ACT).

In Part 1 of the experiment, <sup>fi</sup>ve groups of service consumers are simulated for comparison. They are:

• Group γ = 0: service consumers who completely rely on indirect trust evidence;

• Group $\gamma = 0 . 5 \mathrm { : }$ service consumers who rely on a balanced mix of direct and indirect trust evidence;

• Group γ = 1: service consumers who completely rely on direct trust evidence;

• Group M2002: service consumers who use the method described in [17] to set the γ value;

• Group F2007: service consumers who use the method described in [5] to set the γ value.

![](/api/attachments/8EWREW98/fulltext/images/e13050b671abcb2632bd4cc65113f0def28377d17608db4b2fdc158558938855.jpg)  
Fig. 3. Ranges of variation of NAUL by service consumer groups under non-collusive conditions.

The group of service consumers equipped with the ACT approach is labeled as Group ACT″. Each group consists of 100 agents. All competing groups only request for testimonies from the common witness group.

In Part 2 of this experiment, we compare the performance of the complete ACT approach against:

• Group W2010: service consumers which employ an existing state-ofthe-art method [9];

• Group Y2003: service consumers which employ a classic method [8];

• Group B2002: service consumers who only rely on their direct interaction experience to evaluate a service provider's trustworthiness using BRS [22].

The group of service consumers equipped with the ACT method is labeled as Group ACT. Each group also consists of 100 agents. All groups only request for testimonies from the common witness group same as in Part 1 of the experiment. The existing approaches are executed in parallel with the proposed model under the same experimental settings to obtain fair comparisons of performances.

## 4.4. Experiment results — Part 1

## 4.4.1. The effect of adaptive γ values

Part 1 of this study is conducted assuming non-collusive common witnesses. The common witness population composition is altered from BM80 to Hon and then to BS80 to test the performance of service consumers employing different testimony aggregation methods. The results are summarized in Fig. 3. It can be observed that Group $\gamma = 1$ achieves the highest NAUL values as they need more exploration to identify trustworthy service providers. Its performance is not affected by the changes in the common witness population composition. Completely relying on indirect trust evidence is also not a good strategy as the performance of Group $\gamma = 0$ is heavily affected by the presence of unreliable witnesses of both BM and BS types. However, the saving in exploration from completely relying on third party testimonies allows Group $\gamma = 0$ to achieve lower NAUL values than Group $\gamma = 1$ . Nevertheless, the advantage drops with number of misbehaving witnesses as shown in Fig. 4. The performance of the Group $\gamma = 0 . 5$ is the best among the three groups using static γ values. Group F2007's performance is similar to that of Group M2002. As F2007 tries to learn which static strategy $( \gamma = 0 , 0 . 5 , o r 1 )$ is the best under different conditions, its performance more or less tracks that of Group $\gamma = 0 . 5$ in our experiments. Group $A C T ^ { \prime \prime }$ outperforms all other methods under all testing conditions by an average of 20.79% in terms of the reduction in NAUL. A detailed comparison is shown in Table 3.

![](/api/attachments/8EWREW98/fulltext/images/857f04e848bfd043eda1cc9a4b2a47245fd84f4ca4cbceb54f30db4be14f4375.jpg)  
Fig. 4. Performance of various service consumer groups under different non-collusive common witness populations

Table 3  
Improvement of Group ACT″ over other groups.

<table><tr><td>Group</td><td>Improvement</td></tr><tr><td> $\gamma = 0$ </td><td>23.00%</td></tr><tr><td> $\gamma = {0.5}$ </td><td>16.82%</td></tr><tr><td> $\gamma = 1$ </td><td>31.99%</td></tr><tr><td>M2002</td><td>16.73%</td></tr><tr><td>F2007</td><td>15.41%</td></tr><tr><td>Average</td><td>20.79%</td></tr></table>

The performance achieved by the proposed $A C T ^ { \prime \prime }$ service consumers can be attributed to their ability to adapt the values of γ for each service provider as the environment conditions change in a continuous manner. Fig. 5 shows a snap-shot of the γ value from a service consumer in Group $A C T ^ { \prime \prime }$ with respect to an honest service provider in its local record. As the witness population becomes increasingly hostile, the reliance on third-party testimonies is reduced to mitigate their negative in<sup>fl</sup>uence on the service consumer's interaction decisions.

## 4.5. Experiment results — part 2

## 4.5.1. Performance of ACT under non-collusive lying

In Part 2 of this study, the performance of the complete ACT approach is investigated. The distributions of the NAUL achieved by all <sup>fi</sup>ve models in this study are shown in Fig. 6(a). Group ACT has achieved

![](/api/attachments/8EWREW98/fulltext/images/8fc2d372e9a8d36b413e40510ac930285e3aaccb0d8cd9dd93c57d4c2af12ccf.jpg)  
Fig. 5. The variation of the γ value from the record of a service consumer in Group ACT″ with respect to an honest service provider under different non-collusive common witness populations.

![](/api/attachments/8EWREW98/fulltext/images/931b9d747797110949237f73f34e17244fa7777db01e7d8f5c7691ba35ce1311.jpg)

![](/api/attachments/8EWREW98/fulltext/images/be18d5d57b9619ee78cf4115ae6330c2ce297695d1acbbc800dbc344cfac2760.jpg)  
(a) Ranges of variation of <sup>NAUL</sup> by service consumer groups under <sup>non-collusive</sup> conditions.  
(b) Performance of various service consumer groups under di<sup>f</sup>erent <sup>non-collusive</sup> common witness populations.

![](/api/attachments/8EWREW98/fulltext/images/5698a6642207a2954f67081198a355b975e1480be99389e59039704d2e8594fb.jpg)  
(c) Ranges of variation of <sup>NAU</sup> <sup>L</sup>by service consumer groups under <sup>collusive</sup> conditions.

![](/api/attachments/8EWREW98/fulltext/images/30588a20fe7f9c42687ddc9bc66cdb600a6cb605f36d2d606119a9c042e84142.jpg)  
(d) Performance of various service consumer groups under di<sup>f</sup>erent <sup>collusive</sup> common witness populations.

![](/api/attachments/8EWREW98/fulltext/images/60a71372b5a37f942b03db8d0ffb9a6b576f376057afd24534e72d9f81ee5972.jpg)  
(e) Ranges of variation of Collusion Power by service consumer groups under <sup>collusive</sup> conditions.

![](/api/attachments/8EWREW98/fulltext/images/e370bcb368c5de3a04363b7f69cdc0731c083d58871ece3f4b0d5b3b094aeb21.jpg)  
(f) Performance of various service consumer groups under di<sup>f</sup>erent<sup>collusive</sup> common witness populations.  
Fig. 6. Results for Experiment Part 2.

signi<sup>fi</sup>cantly lower level of NAUL than existing models. As shown in Fig. 6(b), when the percentage of malicious witnesses increases, the performance of Group B2002 is relatively stable as it does not take into account testimonies from witnesses when making trustworthiness evaluations. However, the NAUL of Group Y2003 deteriorates signi<sup>fi</sup>- cantly. The performance of groups W2010 and ACT are relatively consistent across different witness population con<sup>fi</sup>gurations. The consistent performance achieved by the ACT approach is due to that fact that it uses the interaction outcomes with the service providers rather than the majority opinion of the witnesses to update the credibility ranking of known witnesses, as well as its ability to adjust its preference of the two trust evidence sources dynamically. As can be seen from Table $^ { 4 , }$ overall, Group ACT outperforms all other groups in terms of reduction in NAUL by signi<sup>fi</sup>cant margins. The advantage is more signi<sup>fi</sup>cant under ballot-stuf<sup>fi</sup>ng conditions due to the addition of the reward correction value $\theta _ { k j }$ in Eq. (6) that penalizes positively biased testimonies.

Table 4  
Improvement of Group ACT over other groups.

<table><tr><td>Group</td><td>Badmouthing</td><td>Ballot-stuffing</td><td>Overall</td></tr><tr><td>W2010</td><td>18.44%</td><td>29.91%</td><td>25.16%</td></tr><tr><td>Y2003</td><td>64.18%</td><td>70.20%</td><td>66.98%</td></tr><tr><td>B2002</td><td>69.07%</td><td>74.18%</td><td>71.66%</td></tr></table>

## 4.5.2. Performance of ACT under collusive lying

In our test-bed, the collusive witnesses always form collusion rings with Type III malicious service providers to try to promote their reputation. The proportion of collusive witnesses in the total common witness population is varied from Hon to BS80. From Fig. 6(c), it can be seen that the presence of colluding witnesses tricks the Y2003 group into interacting more often with collusive service providers than other groups. In addition, by comparing Fig. 6(c) with (a), we <sup>fi</sup>nd that the negative impact of collusion is more powerful than that of noncollusive random lying. The most adversely affected group is still the Y2003 group. The highest NAUL of this group is about 0.3 under BS80 without collusion. However, under BS80 with collusion, this value increases to around 0.6 (as shown in Fig. 6(d)). This is due to the fact that colluding witnesses do not give unfair testimonies about noncolluding service providers, so that their testimonies are considered accurate in these cases. Thus, they are strategically building up their credibility with the service consumers in order to mislead them into interacting with collusive service providers later.

The performance of all the models studied in our test-bed deteriorated under the in<sup>fl</sup>uence of collusion as shown in Table 5. Although Group ACT and Group W2010 managed to maintain the witness agents' collusion power at relatively low levels compared to other groups as illustrated in Fig. 6(e), their performances in terms of NAUL still deteriorated under collusion. It is observed, from Table $^ { 6 , }$ that the ACT approach signi<sup>fi</sup>cantly outperforms all other approaches in terms of mitigating the adverse effect of collusion. The over performance in terms of reduction in collusion power is the most signi<sup>fi</sup>cant when the majority of the witness population consists of collusive witnesses, as can be seen from Fig. 6(f).

## 4.6. Sensitivity analysis

To study the in<sup>fl</sup>uence of M on the proposed ACT approach, we alter the value of M and re-run the experiments. The value of M is varied to be equivalent to between 5% and 20% of the common witness population. The experiments are re-run only for the cases where collusion exists since collusive testimonies are more powerful in affecting the credibility models. From Fig. 7, it can be seen that generally, collusion power increases with the fraction of colluding witness agents. However, the value of collusion power is maintained at a relatively low level by the ACT approach. This trend is true for the different values of M.

Table 5  
Performance deterioration due to collusion (NAUL).

<table><tr><td>Group</td><td>Without collusion</td><td>With collusion</td></tr><tr><td>ACT</td><td>0.0890</td><td>0.1825</td></tr><tr><td>W2010</td><td>0.1283</td><td>0.2479</td></tr><tr><td>Y2003</td><td>0.2895</td><td>0.4145</td></tr></table>

Table 6  
Improvement of Group ACT over other groups.

<table><tr><td>Group</td><td>Collusion power</td><td>NAUL</td></tr><tr><td>W2010</td><td>77.60%</td><td>26.37%</td></tr><tr><td>Y2003</td><td>85.94%</td><td>55.97%</td></tr></table>

It is expected that the effectiveness of the ACT approach improves with M. However, the value of M also determines the storage capacity required at each individual service consumer as well as the time taken to estimate the reputation of a service provider. Therefore, a service consumer needs to balance the trade-off between potentially more accurate interaction decisions and the extra effort required to gather testimonies from more witnesses.

## 4.7. Analysis of results

Several reasons contribute to the superior performance of Group ACT model over Groups W2010 and Y2003:

• Y2003 uses the number of past interactions between a service consumer $c _ { i }$ and the service provider of interest $s _ { j }$ to determine whether third-party testimonies are required. If the number of past interactions between $c _ { i }$ and $s _ { j }$ exceeds a prede<sup>fi</sup>ned threshold, $c _ { i }$ will not ask for testimonies when estimating $s _ { j } ^ { \prime } s$ trustworthiness. However, since the behavior of the witnesses are changing in the experiments, $c _ { i } ^ { \prime } s$ direct trust evidence may become outdated. This increases c<sub>i</sub>'s risk exposure in the long run.

• W2010 applies an adaptive strategy in aggregating third-party testimonies. However, it also uses a service consumer c<sub>i</sub>'s own evaluation of a service provider $s _ { j } ^ { \prime } s$ trustworthiness as a baseline to determine which testimonies are potentially unfair. It proposed a measure of uncertainty induced by additional testimonies. If a new testimony contradicts $c _ { i } ^ { \prime } s$ current belief about the trustworthiness of $s _ { j } ,$ it would be regarded as increasing $c _ { i } ^ { \prime } s$ uncertainty and discarded. While this approach is more dynamic than Y2003, it still suffers from the effect of changing service provider behavior to some degree.

• In contrast, the ACT approach always seeks testimonies from witnesses when estimating a service provider's reputation. By learning the weights assigned to different witnesses' testimonies based on the outcomes after each interaction, the ACT approach dynamically decides which witnesses to keep in the top M list for each service provider based on their contributions to the well-being of the service consumer. Even in the face of highly hostile witness populations, the ACT approach still can maintain a relatively good performance by relying more on the direct trust evidence source. This mechanism also helps the service consumers when the behavior of a service provider changes. If this change is re<sup>fl</sup>ected <sup>fi</sup>rst in the testimonies, the service consumer can increase the weight given to the indirect trust evidence source to reduce the need for trial and error; if this change is detected <sup>fi</sup>rst by the service consumer itself, it can increase the weight given to the direct trust evidence source to reduce its chance of being misled by outdated opinions from others.

![](/api/attachments/8EWREW98/fulltext/images/e094346f81fa9d61b74846f7bf92b9fea4e040f2857a9c07ef956981f66c181c.jpg)  
Fig. 7. The in<sup>fl</sup>uence of the parameter M on the performance of ACT under different witness population compositions

## 5. Implications

The ACT approach is designed for improving the performance of existing reputation models. Such models have been widely applied in practical applications. For example, in TripAdvisor,<sup>1</sup> individual travelers and hotel operators provide reviews on hotels in popular destinations to help customers decide which hotels to book. Currently, customers need to manually assess the content and credibility of the reviews and consider their personal experience in the past (if there is any) to decide which hotel to book for their next trip. With the large volumes of data collected by TripAdvisor (e.g., Hilton Singapore was reviewed by more than 1000 people), it is practically impossible for a customer to ef<sup>fi</sup>ciently consider the available information and make a holistic decision.

The ACT approach can be implemented as a personal trust agent to provide decision support for customers in online review systems. The agent keeps track of the customer's own reviews on products and services using any existing trust model (as long as its trust evaluations can be normalized to a range of [0,1]). In addition, it <sup>fi</sup>lters and aggregates reviews for products or services the customer is interested in and ranks them based on their reputations to advise the customer on which one to select. Moreover, the ACT approach eliminates the need for manually tuning the values of parameters important to the performance of underlying trust models. It enables the trust models to adapt based on the actual outcomes of past interactions between a service consumer and other service providers. As a result, its performance is less affected by biased third-party testimonies. It also does not require additional infrastructure support (e.g., social relationship information) in order to function. Thus, it forms an ef<sup>fi</sup>cient basis for providing automated decision support to customers of online review systems.

## 6. Conclusions and future work

A trust evidence aggregation model, based on the principles of the actor–critic learning, was proposed to mitigate the adverse effects of biased testimonies. It dynamically adjusts the weights given to selected testimonies as well as the relative emphasis given to the direct and indirect trust evidence sources to reduce a service consumer's risk of being misled by biased third-party testimonies or outdated direct past experience. The ACT approach can be applied to most existing trust models as long as their trust evaluations can be normalized to a range of [0,1] and the interaction outcomes can be represented as either successful or unsuccessful. Experimental results show that ACT outperforms state-of-the-art approaches by around 20% in terms of improving the accuracy of <sup>fi</sup>nding trustworthy service providers in the presence of biased testimonies.

In the computational trust research literature, the most popular metrics used to determine the relative merits of trust models are individually rational in nature. Such measures include various forms of long term average monetary gain for service consumers, and the deviation of estimated trustworthiness from ground truth. Other means of assessing trust decisions on the social welfare of an entire system are rarely considered. It is our belief that apart from the utility enhancement goals, trust models must take into consideration the fair treatment of trustworthy service providers during their decision making processes. This is a crucial consideration that may hold the key to ensuring the long term sustainable operation of a system built on trust. We will investigate this topic in subsequent work.

## Acknowledgment

This research is supported in part by Interactive and Digital Media Programme Of<sup>fi</sup>ce (IDMPO), National Research Foundation (NRF) hosted at Media Development Authority (MDA), Singapore (grant no.: MDA/IDM/2012/8/8-2 VOL 01).

## References

[1] A. Jøang, R. Ismail, C. Boyd, A survey of trust and reputation systems for online service provision, Decision Support Systems 43 (2) (2007) 618–644.

[2] Z. Noorian, M. Ulieru, The state of the art in trust and reputation systems: a framework for comparison, Journal of Theoretical and Applied Electronic Commerce Research 5 (2) (2010) 97–117.

[3] H. Yu, Z. Shen, C. Miao, C. Leung, D. Niyato, A survey of trust and reputation management systems in wireless communications, Proceedings of the IEEE 98 (10) (2010) 1755–1772.

[4] H. Yu, Z. Shen, C. Leung, C. Miao, V.R. Lesser, A survey of multi-agent trust management systems, IEEE Access 1 (1) (2013) 35–50.

[5] K.K. Fullam, K.S. Barber, Dynamically learning sources of trust information: experience vs. reputation, Proceedings of the 6th International Joint Conference on Autonomous Agents and Multiagent Systems (AAMAS'07), 2007, pp. 1055–1060.

[6] J. Weng, C. Miao, A. Goh, An entropy-based approach to protecting rating systems from unfair testimonies, IEICE Transactions on Information and Systems E89-D (9) (2006) 2502–2511.

[7] S. Liu, J. Zhang, C. Miao, Y.-L. Theng, A.C. Kot, iCLUB: An integrated clustering-based approach to improve the robustness of reputation systems, Proceedings of the 10th International Conference on Autonomous Agents and Multiagent Systems (AAMAS'11), 2011, pp. 1151–1152.

[8] B. Yu, M.P. Singh, Detecting deception in reputation management, Proceedings of the 2nd International Joint Conference on Autonomous Agents and Multi-Agent Systems (AAMAS'03), 2003, pp. 73–80.

[9] J. Weng, Z. Shen, C. Miao, A. Goh, C. Leung, Credibility: how agents can handle unfair third-party testimonies in computational trust models IEEE Transactions on Knowledge and Data Engineering (TKDE) 22 (9) (2010) 1286–1298

[10] G. Tesauro, Temporal difference learning and td-gammon, Communications of the ACM 38 (3) (1995) 58–68.

[11] Z. Shen, H. Yu, C. Miao, J. Weng, Trust-based web-service selection in virtual communities, Journal for Web Intelligence and Agent Systems (WIAS) 9 (3) (2011) 227–238.

[12] H. Yu, S. Liu, A.C. Kot, C. Miao, C. Leung, Dynamic witness selection for trustworthy distributed cooperative sensing in cognitive radio networks, IEEE 13th International Conference onCommunication Technology (ICCT), 2011, pp. 1–6.

[13] C.M. Jonker, J. Treur, Formal analysis of models for the dynamics of trust based on experiences, Proceedings of the 9th European Workshop on Modelling Autonomous Agents in a Multi-Agent World (MAAMAW'99), 1999, pp. 221–231.

[14] M. Schillo. P. Funk, I. Stadtwald. M. Rovatsos, Using trust for detecting deceitful agents in arti<sup>fi</sup>cial societies, Journal of Applied Arti<sup>fi</sup>cial Intelligence 14 (8) (2000) 825-848.

[15] J. Shi, G.V. Bochmann, C. Adams, Dealing with recommendations in a statistical trust model, Workshop on Trust in Agent Societies in conjunction with the 4th International Joint Conference on Autonomous Agents and Multi Agent Systems (AAMAS'05), 2005, pp. 144–155

[16] K.S. Barber, J. Kim, Soft Security: Isolating Unreliable Agents from Society 2631 (2003) 224–233.

[17] L. Mui, M. Mohtashemi, A computational model of trust and reputation, 35th Annual Hawaii International Conference on System Sciences (HICSS'02), 7, 2002, pp. 188–197.

[18] H. Chernoff, A measure of asymptotic ef<sup>fi</sup>ciency for tests of a hypothesis based on the sum of observations, The Annals of Mathematical Statistics 23 (4) (1952) 493-655.

[19] R.S. Sutton, A.G. Barto, Reinforcement learning: an introduction, MIT Press 1998.

[20] J. Sabater, C. Sierra, Reputation and social network analysis in multi-agent systems, Proceedings of the 1st International Conference on Autonomous Agents and Multi-Agent Systems (AAMAS'02), 2002, pp. 475–482.

[21] A. Whitby, A. Jøsang, J. Indulska, Filtering out unfair ratings in Bayesian reputation systems, Workshop on Trust in Agent Societies at the 4rd International Joint Conference on Autonomous Agents and Multi-Agent Systems (AAMAS'05), 2005.

[22] A. Jøang, R. Ismai, The beta reputation system, Proceedings of the 15th Bled Electronic Commerce Conference, 2002, pp. 41–55.

[23] V.R. Konda, J.N. Tsitsiklis, On actor–critic algorithms, SIAM Journal on Control and Optimization 42 (4) (2002) 1143-1166

![](/api/attachments/8EWREW98/fulltext/images/87aca65e121fe81901ea8af70be4e8fe76301855466d957be93c986f9dabb6fc.jpg)  
Han Yu is a post-doctoral researcher in the Joint NTU-UBC Research Centre of Excellence in Active Living for the Elderly (LILY). He received his PhD from the School of Computer Engineering, Nanyang Technological University (NTU), Singapore in 2014. He was a Singapore Millennium Foundation (SMF) PhD scholar from 2008 to 2012. He obtained his B.Eng. in Computer Engineering from NTU in 2007 with First Class Honours. From 2007 to 2008, he worked as a systems engineer in Hewlett-Packard (HP) Singapore Pte Ltd. His research interests include trust management in multi-agent systems and intelligent agent augmented interactive digital media in education. His works have been published in top conferences (e.g., AAAI, AAMAS, IJCAI, and IUI) and journals (e.g., Proceedings

of the IEEE). In 2011, he has received the Best Paper Award from the 13th IEEE International Conference on Communication Technologies (ICCT).

![](/api/attachments/8EWREW98/fulltext/images/6be4f4059eacef2df0c2eb5267721365b1af41e8112bd3d135697cbe7618172d.jpg)

Zhiqi Shen is a Senior Research Scientist with the School of Computer Engineering, Nanyang Technological University, Singapore. He obtained B.Sc. in Computer Science and Tech nology from Peking University, M.Eng. in Computer Engineering in Beijing University of Technology, and PhD in Nanyang Technological University, respectively. His research interests include Arti<sup>fi</sup>cial Intelligence, Software Agents, Multi-agent Systems (MAS); Goal Oriented Modeling, Agent Oriented Software Engineering; Semantic Web/Grid, e-Learning, Bio-informatics and Bio-manufacturing; Agent Augmented Interactive Media, Game Design, and Interactive Sto rytelling.

![](/api/attachments/8EWREW98/fulltext/images/3ad5433aa8639c7d95a9a185c473af8fa7ad8e5ece94130746c3af41aea35692.jpg)

Chunyan Miao is an Associate Professor in the School of Computer Engineering (SCE) at Nanyang Technological University (NTU). She is the director of the Joint NTU-UBC Research Centre of Excellence in Active Living for the Elderly (LILY). Prior to joining NTU, she was an Instructor and Postdoctoral Fellow at the School of Computing, Simon Fraser University, Canada. Her major research focus is on studying the cognitive and social characteristics of intelligent agents in multi-agent and distributed AI/CI systems, such as trust, emotions, motivated learning, ecological and organizational behavior. She has made signi<sup>fi</sup>cant contributions in the integration of the above research into emerging technologies such as interactive digital media (e.g., virtual world, social networks, and massively multi-player game), cloud computing, mobile communication, and humanoid robots.

![](/api/attachments/8EWREW98/fulltext/images/548dd7ff9e49bd5285aa87186814d917ebff706c17c0b2eb9b815ca5dfb2819a.jpg)

Bo An is an Assistant Professor at the School of Computer Engineering, Nanyang Technological University since July 2013. Prior to that, he spent one year as an associate professor at the Institute of Computing Technology, the Chinese Academy of Sciences. During October 2010 to June 2012, he was a postdoctoral researcher at the University of Southern California. He received the PhD degree in Computer Science from the University of Massachusetts, Amherst. Prior to that, he received the B.Sc. and M.Sc. degrees in Computer Science from Chongqing University, China. His research interests include arti<sup>fi</sup>cial intelligence, multi-agent systems, game theory, automated negotiation, resource allocation, and optimization. He has published over 30 referred papers at top conferences (e.g., AAMAS, IJCAI, and AAAI) and journals (e.g., JAAMAS,

IEEE Transactions). He has served as program committee members for many top conferences (e.g., AAMAS, IJCAI, AAAI) and was co-chair for some key international conferences/symposia. He is the recipient of the 2010 IFAAMAS (International Foundation for Autonomous Agents and Multiagent Systems) Victor Lesser Distinguished Dissertation Award. He won an Operational Excellence Award from the Commander, First Coast Guard District of the United States. He also won the Best Innovative Application Paper award at the 11th International Joint Conference on Autonomous Agents and Multi-Agent Systems (AAMAS 2012). Recently, he won the 2012 INFORMS Daniel H. Wagner Prize for Excellence in Operations Research Practice.

![](/api/attachments/8EWREW98/fulltext/images/3178a5b4964ce4ce5b6ec62fbd0f72cb7c873f433b04e4d9f32737b313993575.jpg)

Cyril Leung is a member of the IEEE and the IEEE Computer Society. He received the B.Sc. (Honours) degree from Imperial College, University of London, England, in 1973, and the M.S. and Ph.D. degrees in electrical engineering from Stanford University in 1974 and 1976 respectively. From 1976 to 1979 he was an Assistant Professor in the Department of Electrical Engineering and Computer Science, Massachusetts Institute of Technology. During 1979–1980 he was with the Department of Systems Engineering and Computing Science, Carleton University, Ottawa, Canada. Since July 1980, he has been with the Department of Electrical and Computer Engineering, the University of British Columbia, Vancouver, B.C., Canada, where he is a Professor and currently holds the PMC-Sierra Professorship in Networking and Communications. He is the co-director of the Joint NTU-UBC Research Centre of Excellence in Active Living for the Elderly (LILY). His current research interests are in wireless communications systems. He is a member of the Association of Professional Engineers and Geoscientists of British Columbia, Canada
