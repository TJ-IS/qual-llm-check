---
otero_id: 2096
otero_key: "PXGCDYRM"
title: "Mindfully going omni-channel: An economic decision model for evaluating omni-channel strategies"
authors: "Sabiölla Hosseini; Marieluise Merz; Maximilian Röglinger; Annette Wenninger"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.01.010"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Mindfully going omni-channel: An economic decision model for evaluating omni-channel strategies

ELSEVIER Decision Support Systems

Sabiölla Hosseini, Marieluise Merz, Maximilian Röglinger, Annette Wenninger

![](/api/attachments/PXGCDYRM/fulltext/images/0a5c2c59c10ce393a42e4db62c228a5731e852295c16daebe58dcdd01096e0fd.jpg)

PII: S0167-9236(18)30020-4

DOI: https://doi.org/10.1016/j.dss.2018.01.010

Reference: DECSUP 12925

To appear in: Decision Support Systems

Received date: 19 January 2017

Revised date: 30 December 2017

Accepted date: 26 January 2018

Please cite this article as: Sabiölla Hosseini, Marieluise Merz, Maximilian Röglinger, Annette Wenninger , Mindfully going omni-channel: An economic decision model for evaluating omni-channel strategies. The address for the corresponding author was captured as affiliation for all authors. Please check if appropriate. Decsup(2017), https://doi.org 10.1016/j.dss.2018.01.010

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Mindfully going omni-channel: An economic decision model for evaluating omni-channel strategies

## Authors:

Sabiölla Hosseini FIM Research Center University of Augsburg Universitaetsstrasse 12 86159 Augsburg, Germany

Marieluise Merz FIM Research Center University of Augsburg Universitaetsstrasse 12 86159 Augsburg, Germany

Maximilian Röglinger (corresponding author) FIM Research Center University of Bayreuth Wittelsbacherring 10 95444 Bayreuth, Germany maximilian.roeglinger@fim-rc.de

Annette Wenninger FIM Research Center University of Bayreuth Wittelsbacherring 10 95444 Bayreuth, Germany

# Mindfully going omni-channel: An economic decision model for evaluating omni-channel strategies

Abstract: In the digital age, customers want to define on their own how to interact with organizations during their customer journeys. Thus, many organizations struggle to implement an omni-channel strategy (OCS) that meets their customers’ channel preferences and can be operated efficiently. Despite this high practical need, research on omni-channel management predominantly takes a descriptive perspective. What is missing is prescriptive knowledge that guides organizations in the valuation and selection of an appropriate OCS. Most existing studies investigate single facets of omnichannel management in detail while neglecting the big picture. They also require customer journeys to follow sequential and organization-defined purchase decision processes. To address this research gap, we propose an economic decision model that considers online and offline channels, the opening and closing of channels, non-sequential customer journeys, and customers’ channel preferences. Drawing from the principles of value-based management, the decision model recommends choosing the OCS with the highest contribution to an organization’s long-term firm value. We applied and validated the decision model based on real-world data from a German bank.

Keywords: Channel switching, customer journey analytics, decision model, Markov chain, omnichannel management, value-based management

## 1 Introduction

Digital technologies such as mobile devices or social media fundamentally change omni-channel business (Choudhury & Karahanna, 2008; Mirsch, Lehrer, & Jung, 2016). For instance, today’s customers have access to comparison portals and reviews from online communities, and they seek information in traditional, online, and mobile channels simultaneously (Rapp, Baker, Bachrach, Ogilvie, & Beitelspacher, 2015; Schoenbachler & Gordon, 2002). In the digital age, customers want to decide on their own how to interact with organizations during their customer journeys (CJs) (Brynjolfsson, Hu, & Rahman, 2013; Nüesch, Alt, & Puschmann, 2015). Further, new channels and an increasing number of channels affect customers’ channel preferences (Gensler, Verhoef & Böhm, 2012). In the banking industry, for example, 20% of customers use digital channels for information seeking and purchases, whereas 58% use mobile devices for service requests (Accenture Strategy, 2016). Thus, a key challenge of omni-channel management (OCM) is the management of customer behavior across channels by implementing an appropriate omni-channel strategy (OCS) (Pophal, 2015).

The academic literature on OCM is mature and encompasses descriptive as well as prescriptive work. Researchers studied topics such as cross-channel customer behavior, channel adoption, channel choice, and channel usage as well as the effects on organizational performance. To name a few examples, insights include the effects of online and offline channels (Cao & Li, 2015; Lui & Piccoli, 2016; Pauwels, Leeflang, Teerling, & Huizingh, 2011), the duration of channel adoption (Venkatesan, Kumar, & Ravishanker, 2007), customers’ information search and purchase behavior (Balasubramanian, Raghunathan, & Mahajan, 2005; Verhoef, Neslin, & Vroomen, 2007), and the willingness to pay for various channels (Wang, Malthouse, & Krishnamurthi, 2015). Beyond these descriptive studies, very few prescriptive works offer actionable strategies and decision support. For example, attribute models such as “last-click wins” help allocate budgets to channels (Anderl, Becker, Wangenheim, & Schumann, 2014) or Markov-chain-based models assist in determining the impact of digital channels to CJs (Anderl, Becker, Wangenheim, & Schumann, 2016). In addition, Hosseini,

Oberländer, Röglinger, and Wolf (2015) offer a decision model that requires CJs to follow sequential and organization-defined purchase decision processes (PDPs). Finally, Thomas and Sullivan (2005) recommend strategies for targeting and communicating with customers in line with their channel preferences.

In sum, most OCM-related studies consider single facets in detail, but neglect the big picture. Further, there is mature descriptive knowledge, but hardly any prescriptive study that guides organizations in determining an appropriate OCS. Extant work rarely considers online and offline channels in an integrated manner, a simplification disregarding a constitutive feature of omnichannel environments (Holland & Flocke, 2014). Further, the circumstance that CJs are required to follow sequential and organization-defined PDPs neglects emerging customer channel preferences that become manifest in non-sequential CJs. In fact, customers’ willingness to comply with organization-defined PDPs has substantially dropped in omni-channel environments (Barwitz & Maas, 2016; Nüesch et al., 2015). Against this background, we investigate the following research question: How can organizations determine which channels they should offer for various PDP steps when considering non-sequential CJs in an omni-channel environment?

To address this research question, we propose an economic decision model that assists organizations in the valuation and selection of an appropriate OCS. The decision model caters for non-sequential CJs that cover pre-sales, purchase, and post-sales PDP steps as well as omni-channel environments with online and offline channels. To do so, the decision model builds on Markov chains for modelling CJs and the principles value-based management (VBM), which is rooted in investment theory and an accepted paradigm of corporate decision-making, for modelling the value contribution of OCSs. Accordingly, the decision model recommends choosing the OCS with the highest contribution to an organization’s long-term firm value. When specifying the decision model, we followed established guidelines of normative analytical modelling (Cohon, 2004; Meredith, Raturi, Amoako-Gyampah, & Kaplan, 1989).

The remainder of this paper is organized as follows: Section 2 introduces relevant theoretica background on OCM, CJs, Markov chains, and customers’ channel preferences to set the scene for the decision model presented in section 3. In section 4, we apply the decision model to real-world data from a German bank. We conclude in section 5 by summarizing key results and outlining limitations together with avenues for future research.

## 2 Theoretical Background

The availability of ever more channels and customers’ emancipation from organization-defined PDPs implies substantial challenges for managing the interaction between customers and organizations (Cao & Li, 2015; Pauwels & Neslin, 2015). This development makes organizations rethink their channel strategies, i.e. how they interact with their customers in line with customers’ channel preferences and which channels support the steps of the PDP for individual product and service offerings and/or customer segments including pre-sales, purchase, and after-sales activities (Choudhury & Karahanna, 2008). Common PDP steps are information search, evaluation of product options, purchase decision, and post-purchase support (Gupta et al., 2004). Channels are an organization’s media for interacting with customers (Lewis, Whysall, & Foster, 2014; Neslin et al., 2006). They can be split into online (e.g. websites or mobile apps), offline (e.g. agencies or stores), and traditional direct-marketing channels (e.g. catalogs or magazine advertisements) (Verhoef, Kannan, & Inman, 2015). Channel strategies can be formalized as matrices with a PDP and a channe dimension, indicating which channels supports which PDP steps (Anderl et al., 2016; Hosseini et al., 2015). Thereby, channel strategies define the boundary conditions for CJs as organizations and customers can only interact via open channels. In case of an inappropriate channel strategy, which

means that open and closed channels are misaligned with customers’ channel preferences, organizations run the risk of not tapping the potential of customer relationships as customers buy less, churn, or spread negative word of mouth (Sweetwood, 2016; Verhoef et al., 2007).

Against this backdrop, multi-channel management (MCM) has evolved into an established discipline for managing an organization’s interactions with customers via multiple channels. In the MCM context, however, channels are typically treated as independent silos and optimized separately (Nüesch et al., 2015). With each channel pursuing individual goals, organizations do not tap the economic potential of customer relationships by design (Piotrowicz & Cuthbertson, 2014; Pophal, 2015). Coping with the drawbacks of MCM, OCM focuses on customers’ channel preferences and channel dependencies (Nüesch et al., 2015). Verhoef et al. (2015) define OCM as “the synergetic management of the numerous available channels […] in such a way that the customer experience across channels and the performance over channels is optimized” (p.176). Thus, OCM reflects an integrated design and management of multiple channels (Melero, Sese, & Verhoef, 2016; Nunes & Cespedes, 2003; Van Bruggen, Antia, Jap, Reinartz, & Pallas, 2010). This feature is vital as customers are changing the way they collect and evaluate information, how they make decisions, and how they interact with organizations in the digital age (Brynjolfsson et al., 2013; Payne & Frow, 2004).

CJs capture the interactions between customers and an organization along the PDP from a customer perspective for a distinct product or service offering and/or customer segment (Anderl et al., 2014; Zomerdijk & Voss, 2010). As mentioned, channel strategies define the boundary conditions for CJs. CJs are an important concept of OCM as, on an aggregated level, they provide insights into customers’ current and future channel usage (Nenonen, Rasila, Junnonen, & Kärnä, 2008). As customers conduct different PDP steps via different channels to achieve a specific goal such as the purchase of a product or use of a service, CJs reflect customers’ channel preferences (Sanz, 2014). The number of channels, their characteristics, and customers’ channels preferences increase the complexity of today’s CJs (Crawford-Browne, 2016). For instance, customers may prefer the personal service at physical stores and the broad product range of online stores. Although PDPs are typically modelled as a sequence of pre-sales, sales, and post-sales activities, CJs also must reflect nonsequential behavior. That is, customers move forward and backward the PDP or temporarily leave the PDP instead of following an organization-defined sequence of PDP steps (Barwitz & Maas, 2016; Choudhury & Karahanna, 2008; Van Nierop, Leeflang, Teerling, & Huizingh, 2011).

For decision-making purposes, CJs must be captured mathematically (Zomerdijk & Voss, 2010). In the literature, Markov chains have evolved into an established tool for modelling, analyzing, and optimizing customer relationships and CJs (Anderl et al., 2016; Homburg, Steiner, & Totzek, 2009; Pfeifer & Carraway, 2000). Markov chains are defined by states and a matrix that contains transition probabilities among states. Major advantages of Markov chains are their well-developed mathematical foundation, which is rooted in stochastic processes and probability theory, as well as their flexibility that enables them to deal with customer migration or retention over time (Pfeifer & Carraway, 2000). The mathematical foundation of Markov chains also enables accounting for dependencies among states, predicting future customer behavior, and estimating expected values of relevant characteristics, e.g. the number of customers who access a distinct PDP step via a distinct channel (Styan & Smith, 1964). Although Markov chains have so far only been used for modelling sequential CJs, they can handle non-sequential CJs and comply with the matrix conceptualization of channel strategies introduced above. Markov chains are differentiated by their order. First-order Markov chains indicate that customer decisions are memoryless, i.e. the next state of a CJ depends on the current state as reflected in the current PDP step/channel constellation, customers’ channel preferences, and the OCS in focus (Ferschl, 1970; Sperandio & Coelho, 2006). This phenomenon has already been substantially covered in the literature. For instance, Hoyer (1984) found that customers

# ACCEPTED MANUSCRIPT

tend toward simple rules that allow for fast and effortless decisions. Lysonski, Durvasula, and Zotos (1996) as well as Kacen and Lee (2002) found that impulsiveness, which refers to unplanned and fast purchase decisions, is a central characteristic of customer decision-making. Further, Edelmann and Singer (2015) explain the shift from traditional CJs, characterized by long consideration and evaluation phases, to more spontaneous CJs, characterized by fast decision-making. The difference between first-order and higher-order Markov chains is that the simple transition probabilities between states turn into conditional probabilities as the next state also depends on one or more past states. Anderl et al. (2016) analyzed CJs modelled via Markov chains of different orders, showing that the number of required input parameters increases exponentially with a Markov chain’s order and that models quickly becomes too large to be handled efficiently. At the same time, higher-order Markov chains tend to be less significant than first- or second-order chains. Thus, lower-order Markov chains are appropriate for modelling CJs as they feature high real-world fidelity based on a reasonable amount of input data.

CJs strongly depend on customers’ channel preferences, particularly their channel switching behavior if channels are opened or closed for specific PDP steps (Sonderegger-Wakolbinger & Stummer, 2015). Thus, knowledge about customers’ channel switching behavior enables anticipating how CJs look like for different OCSs. This is important task in omni-channel decision-making (Payne & Frow, 2004). In general, customers traverse the PDP along those channels that create the highest subjective utility relative to costs (Reardon & McCorkle, 2002). On a more detailed level, channel switching behavior depends four factors: customer attributes, customer goals, product and service characteristics, and channel attributes (Sousa & Voss, 2012). In addition, the literature names experience, spillover effects, and channel similarity as determinants of channel switching behavior (Gensler et al., 2012; Gupta, Bo-chiuan, & Walter, 2004; Verhoef et al., 2007). Spillover effects capture to which extent the likelihood of using a channel for a distinct PDP step affects the likelihood of using the same channel for other steps. Gupta et al. (2004) found that particularly the similarity between channels determines customers’ switching behavior. The reason is that similar channels cause low (cognitive) opportunity costs and have similar attributes. Thus, channel similarity partly covers the factors introduced above. Hosseini et al. (2015) already used channel similarity as a proxy for customers’ channel switching behavior in the context of sequential CJs. In sum, channel similarity is a central driver of customers’ channel switching behavior (Barwitz & Maas, 2016; Neslin et al., 2006; Sousa & Voss, 2012).

## 3 Decision Model

## 3.1 Basic Idea

In line with the principles of VBM, the decision model aims to identify the OCS with the highest impact on the long-term firm value of the organization in focus (Ittner & Larcker, 2001; Martin & Petty, 2000). To do so, the decision model valuates OCSs by analyzing the CJs, which occur if a distinct OCS is implemented, as well as the opening and closing of channels for specific PDP steps in terms of recurring, investment, and configuration cash flows. Thus, the decision model comprises two central components: a CJ analysis and an investment analysis component (Figure 1). In the CJ analysis, the decision model analyzes CJs based on input parameters such as available channels, PDP steps, and customers’ channel preferences using first-order Markov chains. Regarding the investment analysis, the decision model determines the value contribution of OCSs based on the output of the CJ analysis and information on customer demand and cash flows. Thereby, the decision model takes a differential investment perspective, i.e. the value contribution of an OCS reflects the increased or decreased economic effect compared to the organization’s current OCS. Below, we provide details on the general setting and both components of the decision model.

Figure 1 - Structure of the decision model for a distinct new OCS

# ACCEPTED MANUSCRIPT

## 3.2 General Setting

In this section, we introduce the foundational concepts of the decision model, i.e. CJs, OCSs, and conversion rates that hold for the organization’s current OCS. To model modifications of CJs and conversion rates caused by the opening and closing of channels, we also introduce a restriction matrix and a switching matrix.

The unit of analysis of our decision model is the OCS of an organization for a specific product or service offering. To analyze CJs, we model CJs as an absorbing first-order Markov chain, a frequently used approach for modelling customer relationships and CJs (Anderl et al., 2016; Homburg, Steiner, & Totzek, 2009; Pfeifer & Carraway, 2000). Although Markov chains have so far only been used for modelling sequential CJs, they are capable of dealing with complex customer behavior that becomes manifest in non-sequential CJs (Tseng, Qinhai, & Su, 1999). This makes Markov chains particularly suitable for our purposes.

Markov chains consist of states and probabilities. In our case, states reflect admissible combinations of channels and PDP steps that customers traverse with specific probabilities during their CJs. Probabilities are expressed as conversion rates from one state to others and captured in terms of a conversion matrix. The absorbing Markov chain property enables the modelling of states that, once entered, cannot be exited. Such states characterize the end of ${ \mathsf { C l s , } }$ if a customer has bought an offering or left. First-order Markov chains assume that the next state of a CJ only depends on the conversion rates associated with the current state, not on further past states (Ferschl, 1970; Sperandio & Coelho, 2006). Of course, the next state also depends on the OCS under consideration that determines which channels are open or closed and whether customers can continue their CJ in line with their preferences. Using first-order Markov chains is sensible as customers are known to traverse PDPs based on spontaneous decisions (Lysonski et al., 1996; Kacen & Lee, 2002; Edelmann & Singer, 2015). Such customer behavior can also be captured via higher-order Markov chains. However, the real-world fidelity of our decision model would increase only slightly, while its applicability would suffer greatly, as conditional probabilities are much harder to estimate (Anderl et al., 2016). Thus, we assume:

(A1) The next state of a CJ only depends on the conversion rates associated with the current state of the CJ and the boundary conditions set by the OCS under consideration.

An OCS determines which channels support the PDP steps of a specific product or service offering (Fig. 2). This is why OCSs define the boundary conditions for CJs. PDP steps have a logical and sequential order (Anderl et al., 2016). We define a PDP as a sequence of steps $p _ { j } ,$ , with $j = 0 , \dots , N$ $( N \geq 1 )$ . A channel $c _ { i } , \mathsf { w i t h } i = 0 , \ldots , M ( M \geq 1 )$ , supports at least one PDP step. For technical reasons, we supplement the channels offered by the organization with an ‘Auxiliary’ channel to include an ’Indefinite’ and a ‘Termination point’ step. We use the ‘Indefinite’ step to model customers outside the organization’s PDP and to cover the possibility that customers can temporarily leave the part of the CJ visible for the organization. For example, a customer leaves the visible part of a CJ if he visits a comparison portal to verify product information obtained by the organization, before he may return to buy the product or not. The ‘Termination point’ covers the absorbing Markov chain property as a terminal point with no outgoing edges, where customers conclude their journeys by buying an offering or not. The PDP steps ‘Indefinite’ and ‘Termination point’ appear only in the ‘Auxiliary’ channel, but are technically treated as regular states in the OCS. As shown in Eq. (1), we model OCSs as matrices (Hosseini et $\mathsf { a l . } ,$ , 2015). Referring to a distinct state, the binary variable $x _ { i , j }$ specifies whether channel $c _ { i }$ supports PDP step $p _ { j }$ . The variable $x _ { 0 , 0 }$ represents the ‘Indefinite state, while $x _ { 0 , N }$ represents the ‘Termination point’. The states $x _ { 1 , 0 } , \ldots , x _ { M , 0 }$ and $x _ { 0 , 1 } , \ldots , x _ { 0 , N - 1 }$ and $x _ { 1 , N } , \ldots , x _ { M , N }$ are 0, as they are technical components.

$$
X = \left( \begin{array}{c c c} x _ {0, 0} & \dots & x _ {0, N} \\ \vdots & \ddots & \vdots \\ x _ {M, 0} & \dots & x _ {M, N} \end{array} \right) \qquad x _ {i, j} = \left\{ \begin{array}{c c} 1 & \text {if channel c_{i} supports process step p_{j}} \\ 0 & \text {else} \end{array} \right.\tag{1}
$$

The customers’ preferences to stay within the same channel or to switch channels along the PDP are captured in terms of the conversion matrix $R ,$ shown in Eq. (2). This matrix covers all conversion rates that reflect the organization’s current OCS. Each conversion rate $r _ { i , j , k , l }$ depicts the fraction of customers in channel $c _ { i }$ and process step $p _ { j }$ (state $x _ { i , j } )$ who continue their CJ via channel $c _ { k }$ to proceed to step $p _ { l }$ (state $x _ { k , l } )$

$$
R = \left( \begin{array}{c c c} r _ {0, 0, 0, 0} & \dots & r _ {0, 0, M, N} \\ \vdots & \ddots & \vdots \\ r _ {M, N, 0, 0} & \dots & r _ {M, N, M, N} \end{array} \right) \text {with} r _ {i, j, k, l} \in [ 0; 1 ] \forall i, k \in \{0, \ldots , M \} \land j, l \in \{0, \ldots , N \}\tag{2}
$$

## Figure 2 - Representation of channels, process steps, and non-sequential CJs in the PDP

Although customers want to determine on their own how to interact with organizations, CJs are subject to restrictions, for logical or legal reasons. For instance, a logical restriction is that a customer cannot have a meeting without scheduling it beforehand. A legal reason is that customers must have an obligatory consultation before signing the contract of a complex product or service. To account for such restrictions, we use a restriction matrix $\scriptstyle { Q , }$ as shown in Eq. (3), which determines whether it is possible to proceed from one PDP step to another. Thereby, the restriction matrix supports sequential, non-sequential, and hybrid CJs depending on the underlying PDP and limitations of firstorder Markov chains. ${ \sf A } s$ the ‘Termination point’ describes the final state of a $\complement \rfloor ,$ and there is no possibility of leaving this state, the variables $q _ { N , 0 } , . . . , q _ { N , N - 1 }$ are 0.

$$
Q = \left( \begin{array}{c c c} q _ {0, 0} & \dots & q _ {0, N} \\ \vdots & \ddots & \vdots \\ q _ {N, 0} & \dots & q _ {N, N} \end{array} \right),\tag{3}
$$

$$
\text {with} q _ {j, l} = \left\{ \begin{array}{l l} 1 & \text {if the conversion from step p_{j} to p_{l} is allowed} \\ 0 & \text {else} \end{array} \right. \quad \forall j, l \in \{0, \ldots , N \}
$$

The organization can change its current OCS by opening or closing channels either completely or for specific PDP steps. In the case of closing a channel for a specific PDP step, customers may no longer be able to traverse the PDP in line with their channel preferences. Instead, they must choose other channels and/or PDP steps to proceed or decide to leave (Reardon & McCorkle, 2002; Sonderegger-Wakolbinger $\&$ Stummer, 2015). This phenomenon is also known as enforced channel switching (Hosseini et al., 2015). In the banking industry, for instance, organizations tend to close branch offices for financial reasons, which means customers must shift to online channels. The opposite holds if new channels are opened. Customers then have more interaction possibilities. They may even get the possibility to follow the PDP in line with their channel preferences, which may not have been possible for the organization’s current OCS. To account for the effects of opening and closing channels, it is necessary to modify conversation rates, which reflect the customer behavior in the status quo. To do ${ \mathsf { S O } } ,$ we use channel switching rates $s _ { i , k }$ that denote the rate at which customers are willing to switch from channel $c _ { i }$ to another channel $c _ { k }$ . Switching rates are compiled in the switching matrix ??, as shown in Eq. (4). To facilitate data collection, we designed the switching matrix such that it does not need normalized input values that add up to 1, as switching rates can be set in relation to one another.

$$
S = \left( \begin{array}{c c c} s _ {0, 0} & \dots & s _ {0, M} \\ \vdots & \ddots & \vdots \\ s _ {M, 0} & \dots & s _ {M, M} \end{array} \right) \text {with} s _ {i, k} \in [ 0; 1 ]   \forall i, k \in \{0, \ldots , M \}\tag{4}
$$

The switching matrix comes into play if the organization changes its OCS, i.e. channels are opened or closed. In this case, customers prefer to switch to similar channels (Gupta et al., 2004). Channel similarity is a key driver of customers’ switching behavior as is partly covers factors such as customer attributes and goals as well as channel attributes (Sousa & Voss, 2012). As our decision model focuses on the OCS for a distinct offering, product and service characteristics, which also drive customers’ switching behavior, are covered implicitly by conversion rates. Further, the involved PDP steps have a moderating effect as the decision model ensures that, in line with empirically observed behavior, customers maintain the original direction of their CJ even if the OCS is changed (Melero et al., 2016). For example, if a customer is interested in buying a product and has already negotiated contract conditions, he is likely to proceed with the purchase step instead of continuing his CJ at early PDP steps. The restriction matrix ensures that CJs do not include forbidden or illogical transitions. In sum, the similarity-based switching matrix and the moderating effect of the PDP steps involved ensure the process/channel fit of customer behavior (Gensler et al., 2012). We assume:

(A2) The switching rates, which are used to modify conversion rates in case channels are opened or closed, only depend on channel similarity.

## 3.3 Customer Journey Analysis

We now show how the decision model uses the foundational concepts introduced above to calculate modified conversion rates. Thereby, we refer to modified conversion rates as $r _ { i , j , k , l } ^ { \mathrm { m o d } }$ , representing the conversion of customers between state $x _ { i , j }$ and state $x _ { k , l }$ in a changed OCS.

The effects of changed OCSs on conversion rates and CJs can be split into four effect categories. Fig. 3 represents these categories graphically, while Eq. (11) offers a mathematical specification. Every summand of Eq. (11) covers one effect category, using a fraction as auxiliary quantity for calculating its effect size. These auxiliary quantities are shown in Eq. (5), Eq. (6), Eq. (9), and Eq. (10). The first summand of Eq. (11) accounts for enforced channel switching, i.e. if a channel no longer supports a PDP step that has been supported in the organization’s current OCS. Consequently, customers switch to other states or leave. For example, an organization may cancel its catalog offerings, which means that customers must obtain information via other channels. The second summand captures the negative effects on conversion rates if a channel supports additional PDP steps. Customers may then use newly opened instead of existing channels. For instance, if an organization introduces a new mobile app, some customers refrain from visiting agencies or the organization’s website. The third summand considers the same effect, but from the perspective of newly opened states. As such states did not exist in the current OCS, they draw customers from established states. Finally, once a new state has been opened, it is important to know which states customers use subsequently. This is covered by the fourth summand. For instance, if customers use a new mobile app, they must decide via which channel they want to proceed to the next PDP step.

## Figure 3 - Possibilities to change an OCS

Before presenting Eq. (11) in detail, we introduce its components and their meaning. As mentioned, each summand includes a fraction $F _ { 1 } , \ldots , F _ { 4 }$ as auxiliary quantity that reflects the relative number of customers by which the conversion rates of the status quo must be increased or decreased, respectively.

Fraction $F _ { 1 }$ , which is used in the first summand of Eq. (11), determines the fraction of customers who switch to another state due to enforced channel switching. $F _ { 1 }$ is shown in Eq. (5). We define $F _ { 1 }$ as the ratio of the switching rate $s _ { t , k }$ to the switching rates from state $x _ { t , u }$ (depicting a closed state) to all open states that have a conversion from state $x _ { i , j }$ . Thus, we check whether there exists an outgoing edge (if $r _ { i , j , a , b }$ is greater than 0) and whether the referring state $x _ { a , b } ,$ , where the edge points to, still exists in the new OCS (if $x _ { a , b }$ equals 1). For this fraction, and for all following divisions, it is reasonable to define that, if the denominator of a division equals 0, the result of the division equals 0. Customers who wanted to move forward in the PDP will keep their attitude of moving forward, and customers who wanted to move backward in the PDP will keep their attitude of moving backward (Melero et al., 2016). Thus, we divided $F _ { 1 }$ in two cases to calculate the ratio of the switching rates to only those states that lie in the same direction along the PDP as that of the closed state (first case: backward direction, second case: forward direction). The “else” case occurs if the closed state $x _ { t , u }$ lies in the opposite direction than the currently observed conversion rate $r _ { i , j , k , l }$ is pointing to. As the ‘Indefinite’ state is not integrated in the process sequence, the switch to the ‘Indefinite’ state is included in both cases (see addition of $s _ { t , 0 }$ and $r _ { i , j , 0 , 0 }$ in the denominators) and thus independent from the customers’ attitude of moving forward or backward along the PDP.

$$
F_{1} = \left\{ \begin{array}{ll}\frac{s_{t,k}}{\sum_{a = 1}^{M}\sum_{b = 1}^{j}s_{t,a}\cdot x_{a,b}\cdot\mathrm{sgn}\big(r_{i,j,a,b}\big) + s_{t,0}\cdot\mathrm{sgn}\big(r_{i,j,0,0}\big)} & \text{if $u - j <   0\land l - j <   0$}\\ \frac{s_{t,k}}{\sum_{a = 1}^{M}\sum_{\substack{b = j\\ b\neq 0}}^{N}s_{t,a}\cdot x_{a,b}\cdot\mathrm{sgn}\big(r_{i,j,a,b}\big) + s_{t,0}\cdot\mathrm{sgn}\big(r_{i,j,0,0}\big)} & \text{if $u - j > 0\land l - j > 0$}\\ 0 & \text{else} \end{array} \right.\tag{5}
$$

Fraction $F _ { 2 } ,$ , which is used in the second summand of Eq. (11), determines the relative number of customers moving from their planned state to a newly opened state. $F _ { 2 }$ is shown in Eq. (6). Specifically, $F _ { 2 }$ equals the ratio of switching rate $s _ { k , t }$ to the switching rates between state $x _ { t , u }$ (depicting a newly opened state now) and all open states with a conversion from state $x _ { i , j }$ . The variable ???????? $t _ { j }$ used in $\operatorname { E q . } ( 7 )$ ensures an appropriate allocation to all new states. It displays the number of new states that customers can possibly move to starting from PDP step $p _ { j }$ . As such new states can change the customers’ attitude of moving forward or backward, we did not divide the fraction $F _ { 2 }$ into different cases, as we did for $F _ { 1 }$ . Thereby, the variable $y _ { t , u }$ shown in Eq. (8) equals 1 if the referring state $x _ { t , u }$ is a newly opened state and 0 in all other cases.

$$
F _ {2} = \frac {s _ {k , t}}{c o u n t _ {j} \cdot \sum_ {a = 0} ^ {M} \sum_ {b = 0} ^ {N} s _ {a , t} \cdot x _ {a , b} \cdot \operatorname{sgn} (r _ {i , j , a , b})}\tag{6}
$$

$$
c o u n t _ {j} = \sum_ {a = 0} ^ {M} \sum_ {b = 0} ^ {N} y _ {a, b} \cdot q _ {j, b}\tag{7}
$$

$$
y _ {t, u} = 1 + \mathrm{sgn} \big (x _ {t, u} - x _ {t, u} ^ {\mathrm{old}} - 1 \big) = \left\{ \begin{array}{l l} 1 & \text {if} x _ {t, u} \text {is a new state} \\ 0 & \text {else} \end{array} \right.\tag{8}
$$

In the third summand of Eq. (11), the fraction $F _ { 3 }$ considers the same effect as $F _ { 2 }$ but from the perspective of a newly opened state. Fraction $F _ { 3 }$ , which is shown in Eq. (9), is the ratio of switching rate $s _ { t , k }$ to the switching rates between states $x _ { k , l }$ and all open states that have a conversion from $x _ { i , j }$ , including the number of new states to which the customer can move from process step $p _ { j }$ .

$$
F _ {3} = \frac {s _ {t , k}}{c o u n t _ {j} \cdot \sum_ {a = 0} ^ {M} \sum_ {b = 0} ^ {N} s _ {a , k} \cdot x _ {a , b} \cdot \operatorname{sgn} (r _ {i , j , a , b})}\tag{9}
$$

Finally, $F _ { 4 }$ shown in Eq. (10) determines the relative number of customers leaving a newly opened state to another state to continue their journey. Thereby, $F _ { 4 }$ constitutes the ratio of the switching rate $s _ { i , k }$ to the switching rates between state $x _ { i , j }$ and all other open states.

$$
F _ {4} = \frac {s _ {i , k}}{\sum_ {a = 0} ^ {M} \sum_ {b = 0} ^ {N} s _ {i , a} \cdot x _ {a , b}}\tag{10}
$$

As all auxiliary fractions have been defined, we now focus on how these fractions are integrated in Eq. (11) to model the modified conversion rates.

$$
\begin{array}{r l} r _ {i, j, k, l} ^ {\mathrm{mod}} = & x _ {i, j} \cdot x _ {k, l} \cdot q _ {j, l} \cdot \{r _ {i, j, k, l} \\ & + \sum_ {t = 0} ^ {M} \sum_ {u = 0} ^ {N} F _ {1} \cdot r _ {i, j, t, u} \cdot (1 - x _ {t, u}) \\ & - \sum_ {t = 0} ^ {M} \sum_ {u = 0} ^ {N} F _ {2} \cdot r _ {i, j, k, l} \cdot y _ {t, u} \\ & + \sum_ {t = 0} ^ {M} \sum_ {u = 0} ^ {N} F _ {3} \cdot r _ {i, j, t, u} \cdot y _ {k, l} \\ & + \left. F _ {4} \cdot y _ {i, j} \right\} \end{array}\tag{11}
$$

where:

$r _ { i , j , k , l }$ Original conversion rate from state $x _ { i , j }$ to state $x _ { k , l }$ (as valid in the current OCS)

$r _ { i , j , k , l } ^ { \mathrm { m o d } }$ Modified conversion rate from state $x _ { i , j }$ to state $x _ { k , l }$

$x _ { i , j }$ Indicator showing whether state $x _ { i , j }$ is open in a changed OCS

$y _ { i , j }$ Indicator showing whether state $x _ { i , j }$ is newly opened

$q _ { j , l }$ Indicator showing whether a conversion from PDP step $p _ { j }$ to $p _ { l }$ is possible

$M$ Number of channels

$N$ Number of PDP steps, including the ‘Termination point

Fraction consisting of switching rate from a closed channel to switching rates $F _ { 1 }$ regarding all other relevant states

$F _ { 2 }$ Fraction consisting of switching rate to a specific new state to switching rates regarding all other relevant states (from the perspective of an existing state)

Fraction consisting of switching rate from a specific new state to switching rates $F _ { 3 }$ regarding all other relevant states (from the perspective of a new state)

Fraction consisting of switching rate from a state in a new channel to switching $F _ { 4 }$ rates regarding all other relevant states

Below, we explain the meaning of Eq. (11). The conversion rate $r _ { i , j , k , l }$ can only be applied in a changed OCS if states $x _ { i , j }$ and $x _ { k , l }$ are open and the conversion between both states is not restricted. The multiplication of the three binary variables $x _ { i , j } , x _ { k , l i }$ , and $q _ { j , l }$ captures this condition by assigning the value 0 to the conversion rate if the condition is violated. If both states are open and the conversion is not restricted, Eq. (11) modifies the original conversation rate by accounting for the effects categories outlined above and based on the fractions $F _ { 1 }$ to $F _ { 4 }$ .

The first summand accounts for enforced channel switching. It adds the rate of customers who switch to state $x _ { k , l }$ in the new OCS if some outgoing edges of state $x _ { i , j }$ are no longer supported. The product $r _ { i , j , t , u } \cdot \left( 1 - x _ { t , u } \right)$ checks whether the considered state $x _ { t , u }$ is a newly closed state. In this regard, the product equals 0 if $x _ { t , u }$ is an open state, or if the conversion rate $r _ { i , j , t , u }$ is 0 as the state $x _ { t , u }$ was already closed in the current OCS. It is greater than 0 if state $x _ { t , u }$ is a closed state and if there was originally some conversion from state $x _ { i , j }$ to the now closed state $x _ { t , u }$ . The second summand subtracts the rate of customers who choose to switch to newly opened states. Hereby, the $y _ { t , u }$ indicates all new states that can cause a loss of customers from existing states. The third summand defines the conversion to state $x _ { k , l } \mathrm { i f } \ x _ { k , l }$ <sub>??</sub> is a newly opened state. Graphically, this summand creates the ingoing edges into a new state. The variable $y _ { k , l }$ checks whether the state $x _ { k , l }$ is a newly opened state. Finally, the fourth summand calculates the conversion rates of the outgoing edges of $x _ { i , j } \mathrm { i f } \ x _ { i , j }$ is a new state. This case occurs if the variable $y _ { i , j }$ signals that state $x _ { i , j }$ is a new state.

After calculating the modified conversion rate $r _ { i , j , k , l } ^ { \mathrm { m o d } }$ for all states in the OCS, we normalize the conversion rates in Eq. (12). This step is necessary as Markov chains are based on probabilities. The conversion rates of outgoing edges represent the probability of customers moving on to the next state. All probabilities of the outgoing edges of a single state must thus accumulate to 1 or 0 in case of no outgoing edges. If this is not the case, two issues arise. On the one hand, the decision model would not record all customers, e.g. after a state is closed. Generally, customers using a specific state are then forced to switch or leave. If the conversion rates of the outgoing edges do not accumulate to 1, there is no information how some customers might proceed with their CJ after the OCS has been changed. On the other hand, if the accumulated conversion rates of the outgoing edges are greater than 1, e.g. after a state is closed, more customers would be distributed to other states or leave than the number of customers who used the closed state before. The modified and normalized conversion rates $r _ { i , j , k , l } ^ { \mathrm { r e s } } ,$ which are shown in Eq. (12), are the result of all previous calculations, and build the final modified conversion rate matrix $R ^ { \mathrm { r e s } }$ for a distinct changed OCS.

$$
r _ {i, j, k, l} ^ {\mathrm{res}} = \frac {r _ {i , j , k , l} ^ {\mathrm{mod}}}{\sum_ {a = 0} ^ {M} \sum_ {b = 0} ^ {N} r _ {i , j , a , b} ^ {\mathrm{mod}}} \forall i \in \{0, \dots , N \}; j \in \{0, \dots , M \}\tag{12}
$$

## 3.4 Investment Analysis

Finally, we show how the decision model determines the value contribution of an OCS, using the modified and normalized conversion rate matrix as well as additional information on customer

# ACCEPTED MANUSCRIPT

demand, time measurements, and cash flows as input. Complying with the principles of VBM, the decision model recommends choosing the OCS with the highest positive value contribution. The principles of VBM require that decisions are based on cash flows, take a long-term perspective in terms of a multi-period planning horizon (time value of money), and account for the involved decision-makers’ risk attitude (Damodaran, 2012).

Customer demand is an essential input parameter for omni-channel decision-making, as it indicates how many customers use a state at a distinct point in time. As the principles of VBM require considering each period of a multi-period planning horizon explicitly, customer demand is not static, but must be forecasted. Appropriate forecasts can be achieved if seasonality and/or trend effects are included (Fitzsimmons, Fitzsimmons, & Bordoloi, 2008). Thus, the decision model accounts for changes in customer demand via growth rates. Hereby, we distinguish between a ?????????????????????? $R a t e _ { \tau }$ , which reflects a proportional increase of customer demand in period $\tau ,$ and a $C h u r n R a t e _ { \tau } ,$ which captures a proportional decrease of customer demand. The demand vector $D _ { \tau }$ contains all states as entries (starting with all process steps of the first channel and so on) and depicts the average number of customers for every possible state as the starting point of CJs at the beginning of a period ?? (Eq. 13). That is, the demand vector indicates how many and in which state customers start their journey. As the demand vector does not only contain the demand of existing states, but also of potentially new states, it can be used to reflect the number of new customers attracted by new states.

$$
D _ {\tau + 1} = D _ {\tau} \cdot (1 + N e w C u s t o m e r R a t e _ {\tau} - C h u r n R a t e _ {\tau})\tag{13}
$$

Below, we elaborate on the time parameters and their relationships needed to capture the time value of money in line with the principles of VBM. The time parameters and their relationships are shown in Fig. 4. The planning horizon T indicates how many periods ?? are considered to determine the value contribution of an OCS. The length of a period is characterized by the variable $\theta ,$ which can be measured in, for instance, days or months. A period characterizes a planning period for recurring cash flows as well as the time basis for estimating the number of customers traversing the PDP. Further, the variable ?? describes the length of a PDP step, quantified in the same measurement unit as ??. Thus, every PDP step has a duration of ??. Nevertheless, customers can take more time for PDP steps, a circumstance that is represented via loops in CJs. For example, some customers require more time to decide on a product or may favor a second appointment. Such behavior can be modelled as loops in the Markov chain, representing a self-directed conversion from a state to itself. The last parameter for measuring time is the number of PDP steps ??, which is the maximum number of steps to complete a PDP. Thus, the ?? ∙ ?? measures the length of a PDP, and $\theta / ( H \cdot \eta )$ measures the number of PDPs in one period ??.

## Figure 4 - Relationship between time parameter

As for the cash flow effects of omni-channel decisions. the decision model accounts for three components of cash in- and outflows: recurring, investment, and configuration cash flows. These cash flow components are modelled in Eq. (14), Eq. (16), and Eq. (17), respectively. Recurring cash flows $I ^ { \mathrm { { r e c } } }$ accrue in each period for maintaining open channels according to the OCS under consideration. Investment cash flows $I ^ { \mathrm { i n v } }$ result from the opening and closing of channels, and configuration cash flows $I ^ { \mathrm { c o n f } }$ accrue if the PDP steps supported by a channel change. The recurring cash flows consist of variable outflows $\mu ^ { \mathrm { v a r } }$ (e.g. outflows for verifying a credit application), variable inflows ?? (e.g. the sales price of products or services), and channel-specific outflows $\mu ^ { \mathrm { c s } }$ (e.g. the

labor expenses for an offline channel or IT maintenance expenses for an online channel). For our purposes, we define every cash outflow ?? as a positive vector. We assume:

(A3) The organization adopts the principles of VBM. All considered cash flows as well as the time parameters are constant and deterministic during the planning horizon.

Below, we show how the cash flow components are calculated, starting with the recurring cash flows in Eq. (14).

$$
\begin{array}{r} I ^ {\mathrm{rec}} = \sum_ {\tau = 1} ^ {T} \left(\frac {\frac {\theta}{H \cdot \eta} \sum_ {h = 1} ^ {H} \left[ (D _ {\tau} ^ {\mathrm{mod}} \cdot (R ^ {\mathrm{res}}) ^ {h} - D _ {\tau} \cdot R ^ {h}) \cdot (\pi - \mu^ {\mathrm{var}}) \right]}{(1 + r) ^ {\tau}}\right) - \mu^ {\mathrm{cs}} \cdot \binom {Z _ {0}} {\vdots} \\ \cdot \frac {(1 + r) ^ {T} - 1}{(1 + r) ^ {T} \cdot r} \end{array}\tag{14}
$$

where: ?? Conversion rates of original OCS $R ^ { \mathrm { r e s } }$ Conversion rates of new OCS ?? Variable inflows per state $\mu ^ { \mathrm { v a r } }$ Variable outflows per state $\mu ^ { \mathrm { c } s }$ Channel-specific outflows $D _ { \tau }$ Demand vector in the original OCS in period ?? $D _ { \tau } ^ { \mathrm { m o d } }$ Demand vector in a changed OCS in period ?? ?? Number of periods ?? (planning horizon) ?? Maximum number of steps to complete a PDP ?? Length of a period ?? Length of one PDP step ?? Risk-adjusted interest rate $Z _ { i }$ Indicator showing whether channel ?? is newly opened

The first term of Eq. (14) calculates the variable cash flows for one period ??. The multiplication of the customer demand vector $D _ { \tau } ^ { \mathrm { m o d } }$ by $( R ^ { \mathrm { r e s } } ) ^ { h }$ determines the states of the customers after ℎ PDP steps, based on the properties of the Markov chain (Ferschl, 1970). Thereby, the decision model calculates different CJs and respective variable cash flows. This expression is then summed up for each PDP step in the CJs and multiplied by the number of PDPs to calculate the cash flows of one period ??.

The second term of Eq. (14) reflects the channel-specific outflows accruing for maintaining open channels. Thus, we add channel-specific outflows in our differential investment perspective if a channel is opened, and subtract channel-specific outflows if a channel is closed. Here, the variable $Z _ { i }$ shown in Eq. (15) is equal to 1 if channel $c _ { i }$ is new, –1 if channel $c _ { i }$ (with all corresponding steps) is closed, and 0 in all other cases.

$$
Z _ {i} = \operatorname{sgn} \left(\sum_ {n = 0} ^ {N} x _ {i, n}\right) - \operatorname{sgn} \left(\sum_ {n = 0} ^ {N} x _ {i, n} ^ {\text {old}}\right) = \left\{ \begin{array}{l l} 1 & \text {if c_{i} is a new channel} \\ 0 & \text {else} \end{array} \right.\tag{15}
$$

Further, the investment cash flows depend on the changes in the OCS that result from establishing or closing a complete channel compared with the original OCS. To calculate the investment and disinvestment outflows across all channels, we cumulate channel investment outflows for all newly opened channels and the channel disinvestment outflows for all newly closed channels, as shown in Eq. (16).

$$
I ^ {\mathrm{inv}} = - \sum_ {i = 0} ^ {M} \mu_ {i} ^ {\mathrm{inv,open}} \cdot [ \mathrm{sgn} (Z _ {i} - 1) + 1 ] - \sum_ {i = 0} ^ {M} \mu_ {i} ^ {\mathrm{inv,close}} \cdot [ 1 - \mathrm{sgn} (Z _ {i} + 1) ]\tag{16}
$$

where:

$\mu _ { i } ^ { \mathrm { i n v , o p e n } }$ Investment outflows for establishing channel ??

$\mu _ { i } ^ { \mathrm { i n v , c l o s e } }$ Disinvestment outflows for closing channel ?? completely

$Z _ { i }$ Indicator showing whether channel ?? is newly opened

When an OCS changes, the organization must invest or disinvest configuration cash flows $I ^ { \mathrm { c o n f } }$ for opened or closed states. The configuration cash flows are only taken into account for channels that already existed before the channel changes and still exist afterwards. Accordingly, Eq. (17) shows how the configuration cash flows are calculated:

$$
\begin{array}{r l} {I ^ {\mathrm{conf}} =} & {- \sum_ {i = 0} ^ {M} \sum_ {j = 0} ^ {N} \mu_ {i, j} ^ {\mathrm{conf,open}} \cdot y _ {i, j} \cdot \mathrm{sgn} \left(\sum_ {n = 0} ^ {N} x _ {i, n} ^ {\mathrm{old}}\right)} \\ & {- \sum_ {i = 0} ^ {M} \sum_ {j = 0} ^ {N} \mu_ {i, j} ^ {\mathrm{conf,close}} \cdot z _ {i, j} \cdot \mathrm{sgn} \left(\sum_ {n = 0} ^ {N} x _ {i, n} ^ {\mathrm{old}} + \sum_ {n = 0} ^ {N} y _ {i, j} - \sum_ {n = 0} ^ {N} z _ {i, n}\right)} \end{array}\tag{17}
$$

where:

$\mu _ { i , j } ^ { \mathrm { c o . } }$ nf,open Configuration outflows if channel ?? supports a new $\mathsf { P D P }$ step

$\mu _ { i , j } ^ { \mathrm { c o n f , c l o s e } }$ Configuration outflows if channel ?? no longer supports an established PDP step

$x _ { i , j } ^ { \mathrm { o l d } }$ Indicator showing whether state $x _ { i , j }$ is open in the current OCS

$y _ { i , j }$ Indicator showing whether state $x _ { i , j }$ is newly opened

$z _ { i , j }$ Indicator showing whether state $x _ { i , j }$ is newly closed

The computation of the configuration cash flows follows the same logic as the calculation of the investment cash flows. Conversely, $z _ { i , j }$ is an indicator variable equal to 1 if state $x _ { i , j }$ is closed, and 0 in all other cases, as shown in Eq. (18). Based on the introduced cash flow components, Eq. (19) allows for identifying the optimal OCS ??, which has the highest value contribution base on recurring, investment, and configuration cash flows.

$$
z _ {i, j} = - \text {sgn} \big (x _ {i, j} - x _ {i, j} ^ {\text {old}} + 1 \big) - 1 = \left\{ \begin{array}{l l} 1 & \text {if} x _ {i, j} \text {is a closed state} \\ 0 & \text {else} \end{array} \right.\tag{18}
$$

$$
X ^ {*} = \arg \max _ {X} (I ^ {\text { rec }} + I ^ {\text { inv }} + I ^ {\text { conf }})\tag{19}
$$

## 4 Real-world Application at a German Bank

## 4.1 Case Description

To demonstrate the applicability and usefulness of our decision model in real-world settings, we applied it to the omni-channel environment of a German bank. Thereby, we specifically investigated the bank’s OCS for its construction financing service. The bank is a German cooperative bank with a tradition of more than 200 years. It has about 600 employees in 40 branches and total assets of more than EUR 2 billion. To reach as many customers as possible, the bank offers diverse channels. As requested by the bank’s management, we thus refrained from changing or closing existing channels. Instead, the application of our decision model focused on new channels. Below, we outline the case context and provide information on the bank’s current OCS. After that, we explain how we collected and prepared required input data. Finally, we report the optimization results, before concluding with an analysis and interpretation.

The PDP of the construction financing service encompasses the following steps: ‘Need/Interest,’ ‘First contact,’ ‘Schedule of appointment,’ ‘Information,’ ‘Consulting,’ ‘Negotiation,’ and ‘Conclusion of contract.’ These steps are not mandatory in all CJs. Customers may skip ‘Need/Interest’ and ‘First contact’ as both steps can occur in any form, i.e. via the bank’s channels or word of mouth. In addition, the step ‘First contact’ is not mandatory as regular customers are already known to the bank. For prospects, however, the ‘First contact’ step is mandatory. The steps ‘Schedule of appointment,’ ‘Information,’ and ‘Negotiation’ are mandatory in all CJs. Some customers repeat these steps by rescheduling appointments, reconsidering provided information, or requiring several appointments to negotiate contract conditions. The PDP of the construction financing service ends with the conclusion of a contract or with customers leaving the PDP.

To enable interactions between the bank and its customers, the bank’s current OCS features three channels (Fig. 5): an ‘Agency’ channel, an ‘Online’ channel via a website and mobile app, which the bank considers as a single integrated channel, and a ‘Brochures’ channel for traditional marketing activities. In the future, with a planning horizon of three years, the bank plans to extend its OCS with an ‘Online for standards’ channel where standardized contracts and contract sections are processed automatically. Further, ‘Telephone’ and ‘Video’ channels shall offer customers new ways of contacting bank employees. The bank’s current OCS is the starting position for the application of our decision model. Currently, only the ‘Agency’ channel supports the PDP steps ‘Consulting,’

‘Negotiation,’ and ‘Conclusion of contract.’ The new channels have different properties, depending on whether customers conclude contracts personally with an agency, whether an interaction is ITsupported, and whether an interaction is one- or bi-directional. For example, the ‘Agency,’ ‘Telephone,’ and ‘Video’ channels support bi-directional personal contact between bank employees and customers. The response to customers using online channels is IT-supported. The ‘Brochures’ channel is one-directional, providing customers with company and product information. Owing to these channel properties, not all channels support all PDP steps. To illustrate the complexity of the bank’s current omni-channel environment, Figure 5 does not only visualize the bank’s current OCS, but also all CJs, depending on channel properties and mandatory PDP steps as specified in the restriction matrix. As can be seen, customer behavior can only be captured appropriately via nonsequential CJs. The more non-mandatory PDP steps and the more options for customers to choose between channels an OCS includes, the more complex the CJs.

## Figure 5 - Current omni-channel environment at the case company

## 4.2 Data Collection and Preparation

To apply the decision model to the bank’s omni-channel environment, we first presented our idea to the head of global bank management, the head of the sales department, and the department head for private and commercial customers. We then collected and validated required input data in an iterative process. Our primary informant was an employee of the bank’s sales department, who consulted and involved members of other departments wherever needed. If necessary, we also used additional information from the literature to prepare collected data and validate estimated values. In the case at hand, our primary data source is an in-depth analysis that the bank’s sales department had recently conducted of the construction financing service’s PDP with a focus on customers channel usage. We were also granted access to anonymized data from the bank’s customer relationship management system. Below, we provide information on our data sources, structured along the components of the decision model (i.e. CJ analysis and investment analysis). Table 1 summarizes input data that resulted from interviews and workshops with the bank’s employees, except for the conversion rates that are displayed in the Appendix due to the high number of conversion rates.

As for the Cl analysis component. the decision model reguires input data about the structure of the PDP and relevant restrictions, available and potential channels, and information about customers including conversion and switching rates. The bank’s omni-channel environment and possible CJs could be identified easily based on an interview with a member from the bank’s sales department, as channels and PDP steps are the sales department’s daily business. Likewise, we quickly reached consensus on the restriction matrix based on logical considerations and legal regulations when discussing CJs with the bank’s employees.

Conversion rates were tracked by the bank only in some cases. For example, the bank knew how many customers are leaving the PDP such that we could easily quantify the conversion rates for the ‘Auxiliary’ channel. We then estimated the remaining conversion rates by considering that the weights of a state’s outgoing edges must sum up to 1. Starting with known conversion rates from the bank’s channel usage analysis, we allocated the remaining fractions of the conversion rates based on the fraction of customers who used the involved channels.

The switching rates, which capture customer’s channel switching preferences if channels are opened or closed steps and which are used to modify conversion rates, were the most difficult to estimate.

# ACCEPTED MANUSCRIPT

With the modelling of customer behavior in terms of Markov chains and channel switching rates, as proposed in this study, being a novel approach, organizations do not have such data readily available. To estimate switching rates, we made use of the fact that the switching matrix does not need to be filled with absolute values. Instead, relative values are sufficient, a feature that simplified the collection of required input data. In agreement with the bank’s experts, we distinguished ‘low,’ ‘medium,’ ‘high,’ and ‘very high’ channel switching preferences, with values of 0.25, 0.5, 0.75, and 1, respectively. With channel similarity being a central drive of customer’s channel switching preferences, we based the classification just presented on channel similarity and customers’ channe usage trends identified by the bank (Gupta et al., 2004). We assigned high switching rates to similar channels and vice versa. By definition, the diagonal of the switching matrix refers to the category ‘very high’. Further, we applied the category ‘high’ between the ‘Online’ and the ‘Online channel for standards’ channels as well as the category ‘low’ between the ‘Online’ and ‘Agency’ channels. Switching to the ‘Auxiliary’ channel was based on the bank’s knowledge and the literature, suggesting that personal contact leads to higher preferences than brochures (Frambach, Roest, & Krishnan, 2007). Further, we accounted for the general trend that customers in the digital age tend to prefer online channels over offline channels (Gupta et al., 2004, Verhoef et al., 2015). Thus, we increased the switching rates from the ‘Agency’ to the ‘Online’ channel. We did the same when determining the switching rates starting from the ‘Auxiliary’ channel. The remaining part of the switching matrix was symmetric due to the channels’ similarity properties.

As for the investment analysis component, we needed information about the time horizon, customer demand, and cash flow effects. Relevant data on time (i.e. the planning horizon, the length of a period, and the length of PDP steps), customer demand, and how often the PDP steps of the construction financing service are executed, were provided by the bank’s sales management department and did not need to be estimated.

The bank’s controlling department provided us with data for monetary input parameters, particularly for variable cash flows, inter alia the sales prices of the construction financing service, investments outflows, and channel-specific outflows. We discussed these input data with experts from the bank’s sales department to ensure mutual comprehension of the different concepts used to describe monetary data and to break recurring cash outflows down to individual time periods if needed. Variable cash outflows per customer are based on the monetized average time consumption of an employee, which was known from the bank’s recent PDP analysis. The channel-specific outflows for established channels were directly provided by the sales department, whereas for new channels, where no historical data was available, we estimated channel-specific outflows using comparable data from existing channels and challenged the results in semi-structured interviews with experts from the bank’s private and commercial customers department. Further, we could use estimations of the sales department for investment outflows, which the bank had already made to prepare the introduction of the new channels. The configuration cash flows capture outflows for changing which PDP steps are supported by a distinct channel. As it is difficult to allocate some cash outflows to individual PDP steps, most organizations – including the bank – do not have detailed data on configuration outflows per state. We thus discussed these outflows in semi-structured interviews with employees from the bank’s sales department. Thereby, we assumed that the configuration outflows are equally high for the PDP steps within a distinct channel, but vary between channels. Regarding the cash outflows for the complete or partial closing of channels, neither historical data were available nor could we find reliable estimations in external sources. Thus, we agreed with the bank to refrain from analyzing OCSs that include the closing of channels to maintain the quality of our results. Although our primary focus was on the opening of new channels in line with the bank’s strategy, such analyses would have been interesting to find out whether there are favorable OCSs with a reduced number of existing channels.

## Table 1 - Real-world input data for the demonstration example

## 4.3 Optimization Results

In line with the bank’s strategy and the objective function of our decision model, we aimed to identify the OCS with the highest value contribution, i.e. the highest contribution to the bank’s longterm firm value. In our case, the optimal OCS yielded a value contribution of 877,212 EUR. To realize this value contribution, the bank is advised to open the ‘Online for standards’ channel completely except for the ‘Negotiation’ step, which is not needed for standard products as indicated in expert interviews. In addition, the bank should open the ‘Telephone’ channel for the PDP steps ‘Information’ and ‘Conclusion of contract’.

The problem of determining the optimal OCS is complex as it requires a full enumeration of all possible OCSs. In case at hand, we had to calculate the value contribution of 16,384 OCSs, a task for which we implemented a software prototype. Due to the high number of candidate OCS, we only present parts of the results, i.e. the most interesting OCSs from our perspective. Table 2 shows the bank’s current OCS, the stepwise opening of a channel to determine a channel-specific local optimum using the ‘Online for standards’ channel as example, and all combinations of introducing one, two, or all discussed channels. We further highlight the OCS that the bank would have implemented before gaining insights from the application of our decision model. We also compare this OCS with the optimal OCS determined by our decision model.

## Table 2 - OCSs and corresponding value contributions

## 4.4 Interpretation and Discussion

As outlined, the bank aims to offer a broad range of channels to reach as much customers as possible. Thus, we deliberately refrained from changing or closing channels of the bank’s current omni-channel environment. Instead, we focused on the three new channels the bank was currently considering. The results presented in Table 2 support that the decision model can be applied in realworld settings. Its input parameters can be collected or estimated with reasonable effort. Below, we discuss the various OCSs and their effects.

OCS 1 captures the bank's current OCS. Keeping this OCS leads to a value contribution of 0. a reasonable result that is rooted in the differential investment perspective underlying our decision model. Further, OCSs 2 to 7 capture the stepwise opening of the ‘Online for standards’ channel structured along the PDP of the construction financing service. Due to complex and non-sequential customer behavior, the opening of this channel only yields a positive value contribution if it supports all PDP steps. From OCSs 8 and 9, which refer to the ‘Telephone’ channel, we can infer that there are channel-specific local optima. For instance, in the ‘Telephone’ channel, it is more reasonable to support the last process steps ‘Negotiation’ (step 6) and ‘Conclusion of contract’ (step 7) than all process steps. Up to OCS 14, we list all combinations of the new channels. For every channel, OCSs 7, 9, and 10 reflect the respective local optima. Notably, the combination of locally optimized channel strategies does generally not lead to a globally optimal OCS in terms of value contribution. This phenomenon is again rooted in non-sequential CJs.

The bank initially aimed to implement an OCS that includes all three discussed channels. This OCS is included as OCS 15 in Table 2. and has a rather low. but positive value contribution. Thus far, the complete opening of the ‘Online for standards’ channel (OCS 7) had the highest value contribution (i.e. 796,693 EUR). The process step ‘Negotiation’ (step 6) causes considerable variable outflows as we modelled a loop for this step, catering for the fact that most customers need more time than planned. The effect on the bank’s omni-channel environment is that the decision model avoids the PDP step ‘Negotiation’ (step 6) if possible. OCS 16 accounts for this circumstance, showing that the optimal OCS includes a combination of the ‘Online for standards’ and ‘Telephone’ channels. This optimal OCS leads to a value contribution of 877,212 EUR, a value more than three times higher than the bank’s initially preferred OCS (OCS 15).

In the case at hand, we detected that it is not useful to ignore or open all new channels. The appropriate OCS depends on channel properties and customer’s preferences captured in terms of conversion and switching rates as well as on the economic effects associated with the opening, closing, and operations of channels for PDP steps. In the case at hand, the ‘Telephone’ and ‘Video channels are very similar compared to established channels in terms of their properties and cash flow effects. Thus, it is not reasonable to implement both channels as customers perceive them as substitutable. According to the collected data, the ‘Telephone’ channel causes lower cash outflows, but similar cash inflows as the ‘Video’ channel. Thus, it should was preferred. In addition, the investigated OCSs tended to yield higher value contributions if newly opened channels support every PDP step. Finally, our analysis revealed that time-intensive PDP steps of non-standardized products, such as the ‘Negotiation’ step, are realized by the ‘Agency’ channel, even if the bank introduces new channels. The reason was that customers prefer the personalized contact with agencies on matters concerning construction financing. Fig. 6 shows the bank’s omni-channel environment, including anticipated CJs after implementing the optimal OCS. Customers then have more possibilities to interact with the bank. Thus, the structure of CJs becomes even more complex. The ‘Agency’ channe is relieved by additional channels for the first four process steps and the ‘Conclusion of contract step.

## Figure 6 - Omni-channel environment at the case company after implementing the optimal OCS

## 16

To challenge the optimization results, we presented and discussed the optimal OCS (OCS 16) with a leading employee of the bank. According to the bank’s assessment, the PDP of the construction financing service was captured completely and accurately. The optimal OCS eliminates the so far preferred option of using the ‘Video’ channel for the reasons mentioned above (OCS 15). The leading employee indicated that the optimal OCS is a feasible design option for the bank. One reason was that the optimal OCS leads to less investment outflows than the initially preferred OCS because one channel less must be opened. Further, the bank confirmed that the most important tasks of the construction financing service’s PDP are still planned to be conducted by agencies, a property covered by the optimal OCS. Finally, the bank stated that our mathematical analysis of its OCS did not only yield interpretable and actionable results, but also advanced the management team’s thinking about complex customer behavior in terms of non-sequential CJs, channel dependencies that influence customers’ switching behavior, and the manifold cash flow effects associated with changing an organization’s OCS.

## 5 Conclusion

## 5.1 Summary and Contribution

To account for the increasing importance of OCM and the lack of related prescriptive knowledge, we investigated how organizations can determine which channels they should offer for various PDP steps when considering non-sequential CJs in an omni-channel environment. To do so, we proposed

# ACCEPTED MANUSCRIPT

an economic decision model that compares OCSs in terms of their contribution to an organization’s long-term firm value. For our purposes, we modeled OCSs as matrices with a channel and a PDP dimension, while capturing CJs via first-order Markov chains. This design enabled us to include online and offline channels, the opening and closing of channels for distinct PDP steps, customer churn due to enforced channel switching, and non-sequential customer behavior. With non-sequential customer behavior and synchronized interaction via multiple channels being essential in the digital age, we considered both phenomena in our decision model. We validated the decision model’s applicability using real-world data from a German bank, finding that the required input data can be gathered with reasonable effort and that the results are useful for subject matter experts.

Providing well-founded guidance on how to determine an appropriate OCS for a distinct organization, our decision model adds to the prescriptive knowledge on OCM. Compared to extant prescriptive works, our decision model takes a holistic perspective and is the first to combine nonsequential CJs modelled as first-order Markov chains with decision-making in line with the principles of VBM. Nevertheless, it difficult to infer general recommendations for the selection of OCSs based on the decision model per se due to the high number of input parameters. Such recommendations require a substantial amount of real-world case studies and computational experiments. However, organizations can still benefit from insights based on our decision model when deciding about different OCS without determining all input parameters and applying the model directly. For example, changing one’s OCS is not an either-or decision about opening or closing one or more channels. Rather, it implies a conscious deliberation of how customers will behave in case of adjustments. In some cases, closing a single state or opening a channel for specific PDP steps only is more reasonable than closing or opening a channel for the entire PDP. The real-world semantics of the components $F _ { 1 }$ to $F _ { 4 }$ provide further guidance for omni-channel decision-making. If an organization bears these semantics in mind, it can account for how the diverse effects of omni channel decision-making and related dependencies. For example, if a channel or state is closed, an organization must propose an alternative with similar characteristics to redirect CJs and avoid churn. Generally, organizations must be aware of their channel offering, the steps of the PDP, and consistently take a customer as well as an investment perspective. The decision model builds on relevant theoretical concepts from the literature and is able to handle manifold situations that occur in real-world settings. Thus, it can be applied in multiple organizational contexts.

## 5.2 Limitations and Future Research

Our decision model is beset with limitations that stimulate future research. Below, we present these limitations and related directions for future research, structured into model- and application-specific limitations.

As for model-specific limitations, the decision model makes some simplifying assumptions. First, we assume that most input parameters are constant and deterministic throughout the planning horizon. In real-world settings, however, cash flows and customer behavior are uncertain. As stochastic parameters require information about probability distributions, we deliberately restricted our decision model to deterministic parameters to keep its complexity and the amount of input data manageable. Second, we modeled CJs using first-order Markov chains, acting on the assumption that future customer behavior only depends on a customer’s current channel and PDP step combination. Although customers are known to traverse PDPs based on spontaneous decisions, second-order Markov chains would slightly increase the real-world fidelity of our decision model by covering experiences made in previous steps. From a mathematical modelling perspective, the decision mode can be extended easily, but its applicability would suffer greatly due to the increased data collection effort. Third, the switching matrix used in the decision model only covers switching rates from one channel to another. Based on the restriction matrix, the decision model also covers the moderating effect of the involved PDP as customers tend to keep their original direction through the PDP. Nevertheless, switching probabilities may differ per PDP step as well as for product or service offerings such that a more fine-grained conceptualization of the switching matrix would increase the real-world fidelity of our decision model. We accepted these limitations to keep the decision model applicable, focusing on those parameters with the highest effects as highlighted in the literature. Nevertheless, future research should challenge which assumptions can be purposefully relaxed. Thereby, one must keep in mind that the decision model aims to purposefully abstract from the real world, not to capture all its complexity. It is imperative to deliberate carefully whether an increase in real-world fidelity gained by relaxing assumptions outvalues corresponding increases in model complexity and data collection effort.

When applying the decision model to the case of a German bank, we determined the most appropriate OCS for a single offering, namely the construction financing service. In general, organizations have several product or service offerings, which differ in terms of their monetary effects and CJs. As channels can be used for all product and service offerings of an organization once they have been established, it is important to consider all offerings to ensure an integrated perspective on an organization’s omni-channel environment. However, analyzing CJs for one offering is already very complex. For this reason, our application focused on one service offering to validate how the decision model behaves in a real-world setting. Nevertheless, the decision model can be easily extended to account for several product or service offerings, e.g. by adding PDP steps. The main difficulty of applying our decision model is the estimation of required input parameters such as conversion or switching rates. However, with the conception and implementation of a novel OCS being a rather seldom and irreversible decision associated with long-term effects and huge investments, we are convinced that organizations should make the effort to determine all input parameters, apply the decision model accordingly, and calculate scenarios to mitigate potential estimation inaccuracies. We are convinced that this effort is justified given the enormous consequences of omni-channel decisions. In addition, in the digital age, data about channel preferences and CJs can be collected more easily as ever more data will become available in organizations. Although our real-world application demonstrated that data can be collected with reasonable effort, we recommend conducting additional case studies in different contexts to get a better understanding of realistic value ranges and to establish a knowledge base. Additional case studies and computational experiments will also lead to generalizable insights into the mechanics of omni-channel decision-making. Finally, when applying our decision model, we implemented a software prototype, which is fit for research purposes, but not user-friendly enough to be applied in manifold industry-scale settings. When conducting multiple case studies, the prototype should be enhanced by means of more sophisticated analysis functionality and a convenient user interface.

This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

## References

Accenture Strategy ‘Banking Customer 2020’.

https://www.accenture.com/t20150710T130243\_\_w\_\_/us-en/\_acnmedia/Accenture/Conversion-

Assets/DotCom/Documents/Global/PDF/Dualpub\_17/Accenture-Banking-Consumer-Pulse.pdf (Accessed September 15th, 2017).

Anderl, E., Becker, I., Wangenheim, F. V., & Schumann, J. H. (2014). Mapping the customer journey: A graph-based framework for attribution modelling in managerial practice. SSRN Electronic Journal.

Anderl, E., Becker, I., Wangenheim, F. V., & Schumann, J. H. (2016). Mapping the customer journey: Lessons learned from graph-based online attribution modelling. International Journal of Research in Marketing, 33(3), 457–474.

Balasubramanian, S., Raghunathan, R., & Mahajan, V. (2005). Consumers in a multichannel environment: Product utility, process utility, and channel choice. Journal of Interactive Marketing, 19(2), 12–30.

Barwitz, N., & Maas, P. (2016). Value Creation in an Omnichannel World: Understanding the Customer Journey. 25th Annual Frontiers in Service Conference, Bergen, Norway.

Brynjolfsson, E., Hu, Y. J., & Rahman, M. S. (2013). Competing in the Age of Omnichannel Retailing. MIT Sloan Management Review, 54(4), 23–29.

Cao, L., & Li, L. (2015). The Impact of Cross-Channel Integration on Retailers’ Sales Growth. Journal of Retailing, 91(2), 198–216.

Choudhury, V., & Karahanna, E. (2008). The Relative Advantage of Electronic Channels: A Multidimensional View. MIS Quarterly, 32(1), 179–200.

Cohon, J.L. (2004). Multiobjective programming and planning. New York: Dover Publishing. Crawford-Browne, S. (2016). How to design a branded customer experience. Warc Best Practice.

Damodaran, A. (2012). Investment valuation: Tools and techniques for determining the value of any asset (Vol. 666). John Wiley & Sons.

Edelman, D.C., & Singer, M. (2015). Competing on Customer Journeys. Harvard Business Review.

Ferschl, F. (1970). Markovketten. Berlin, Heidelberg: Springer.

Fitzsimmons, J. A., Fitzsimmons, M. J., & Bordoloi, S. (2008). Service management: Operations, strategy, and information technology (p. 4). New York, NY: McGraw-Hill.

Frambach, R. T., Roest, C. A., & Krishnan T. V. (2007). The impact of consumer internet experience on channel preference and usage intentions across the different stages of the buying process. Journal of Interactive Marketing, 21(2), 26–41.

Gensler, S., Verhoef, P.C., & Böhm, M. (2012). Understanding consumers’ multichannel choices across the different stages of the buying process. Marketing Letters, 23(4), 987–1003.

Gupta, A., Bo-chiuan, S., & Walter, Z. (2004). An Empirical Study of Consumer Switching from Traditional to Electronic Channel: A Purchase Decision Process Perspective. International Journal of Electronic Commerce, 8(3), 131–161.

Holland, H., & Flocke, L. (2014). Digitales Dialogmarketing. Customer-Journey-Analyse-Ein neuer Ansatz zur Optimierung des (Online-) Marketing-Mix. Springer Fachmedien.

Homburg, C., Steiner, V. V., & Totzek, D. (2009). Managing dynamics in a customer portfolio. Journal of Marketing, 73(5), 70–89.

Hosseini, S., Oberländer, A., Röglinger, M., & Wolf, T. (2015). Rethinking Multichannel Management in a Digital World - A Decision Model for Service Providers. In Proceedings of the 12th International Conference on Wirtschaftsinformatik (WI).

Hoyer, W. (1984). An examination of consumer decision making for a common repeat purchase product. Journal of Consumer Research, 11(3), 822–829.

Ittner, C. D., & Larcker, D. F. (2001). Assessing empirical research in managerial accounting: A valuebased management perspective. Journal of Accounting and Economics, 32(1), 349–410.

Kacen, J. J., & Lee, J. A. (2002). The influence of culture on consumer impulsive buying behavior. Journal of Consumer Psychology, 12(2), 163–176.

Katz, M. L., & Shapiro, C. (1994). Systems Competition and Network Effects. The Journal of Economic Perspectives, 8(2), 93–115.

Lewis, J., Whysall, P., & Foster, C. (2014). Drivers and technology-related obstacles in moving to multichannel retailing. International Journal of Electronic Commerce, 18(4), 43–68.

Lui, T.W., & Piccoli, G. (2016). The Effect of a Multichannel Customer Service System on Customer Service and Financial Performance. ACM Transactions on Management Information Systems, 7(2), 2– 15.

Lysonski, S., Durvasula, S., & Zotos, Y. (1996). Consumer decision-making styles: a multi-country investigation. European Journal of Marketing, 30(12), 10–21.

Martin, J. D., & Petty, J. W. (2000). Value based management. The corporate response to the shareholder revolution. Boston, Mass.: Harvard Business School Press.

Melero, I., Sese, F. and Verhoef, P.C. (2016) Recasting the Customer Experience in Today’s Omni channel Environment. Universia Business Review, 50(2), 18–37.

Meredith, J. R., Raturi, A., Amoako-Gyampah, K., & Kaplan, B. (1989). Alternative Research Paradigms in Operations. Journal of Operations Management, 8(4), 297–326.

Mirsch, T., Lehrer, C., & Jung, R. (2016). Channel Integration towards Omnichannel Management: A Literature Review. In Proceedings of the 20th Pacific Asia Conference on Information Systems (PACIS).

Nenonen, S., Rasila, H., Junnonen, J.M., & Kärnä, S. (2008). Customer Journey - a method to investigate user experience. In Proceedings of the Euro FM Conference Manchester.

Neslin, S. A., Grewal, D., Leghorn, R., Shankar, V., Teerling, M. L., Thomas, J. S., & Verhoef, P. C. (2006). Challenges and Opportunities in Multichannel Customer Management. Journal of Service Research, 9(2), 95–112.

Nüesch, R., Alt, R., & Puschmann, T. (2015). Hybrid Customer Interaction. Business and Information Systems Engineering, 57(1), 73–78.

Nunes, P. F., & Cespedes, F. V. (2003). The customer has escaped. Harvard Business Review, 81(11), 96–105.

Pauwels, K. H., Leeflang, P. S. H., Teerling, M. L., & Huizingh, E. (2011). Does Online Information Drive Offline Revenues?: Only for Specific Products and Consumer Segments! Journal of Retailing, 87(1), 1– 17.

Pauwels, K., & Neslin, S. A. (2015). Building with bricks and mortar: The revenue impact of opening physical stores in a multichannel environment. Journal of Retailing, 91(2), 182–197.

Payne, A., & Frow, P. (2004). The role of multichannel integration in customer relationship management. Industrial Marketing Management, 33(6), 527–538.

Pfeifer, P. E., & Carraway, R. L. (2000). Modelling customer relationships as Markov chains. Journal of Interactive Marketing, 14(2), 43–55.

Piotrowicz, W., & Cuthbertson, R. (2014). Introduction to the Special Issue Information Technology in Retail: Toward Omnichannel Retailing. International Journal of Electronic Commerce, 18(4), 5–16.

Pophal, L. (2015). Multichannel vs. Omnichannel Marketing: Is There a Difference, and What Does It Mean to You? Econtent, 38(2), 15–20.

Rapp, A., Baker, T. L., Bachrach, D. G., Ogilvie, J., & Beitelspacher, L. S. (2015). Perceived customer showrooming behavior and the effect on retail salesperson self-efficacy and performance. Journal of Retailing, 91(2), 358–369.

Reardon, J., & McCorkle, D. E. (2002). A consumer model for channel switching behavior. International Journal of Retail and Distribution Management, 30(4), 179–185.

Sanz, J. L. (2014). Enabling Front-Office Transformation and Customer Experience through Business Process Engineering. Enterprise Modelling and Information Systems Architectures, 9(1), 50–69.

Schoenbachler, D. D., & Gordon, G. L. (2002). Multi-channel shopping: understanding what drives channel choice. Journal of Consumer Marketing, 19(1), 42–53.

Sonderegger-Wakolbinger, L. M., & Stummer, C. (2015). An agent-based simulation of customer multi-channel choice behavior. Central European Journal of Operations Research, 23(2), 459–477.

Sousa, R., & Voss, C. (2012). The impacts of e-service quality on customer behaviour in multi-channel e-services. Total Quality Management and Business Excellence, 23(7–8), 789–806.

Sperandio, M., & Coelho, J. (2006). Constructing Markov Models for Reliability Assessment with Self-Organizing Maps. In Proceedings of the 9th International Conference on Probabilistic Methods Applied to Power Systems (PMAPS).

Styan, G. P. H., & Smith, H. (1964). Markov chains applied to marketing. Journal of Marketing Research, 1(1), 50–55.

Sweetwood, A.K. (2016). How One Company Used Data to Rethink the Customer Journey. Harvard Business Review Digital Articles, 2–5.

Thomas, J. S., & Sullivan, U. Y. (2005). Managing Marketing Communications with Multichannel Customers. Journal of Marketing, 69(4), 239–251.

Tseng, M. M., Qinhai, M., & Su, C. (1999). Mapping customers’ service experience for operations improvement. Business Process Management Journal, 5(1), 50–64.

Van Bruggen, G. H., Antia, K. D., Jap, S. D., Reinartz, W. J., & Pallas, F. (2010). Managing marketing channel multiplicity. Journal of Service Research, 13(3), 331–340.

Van Nierop, J. E., Leeflang, P. S., Teerling, M. L., & Huizingh, K. E. (2011). The impact of the introduction and use of an informational website on offline customer buying behavior. International Journal of Research in Marketing, 28(2), 155–165.

Venkatesan, R., Kumar, V., & Ravishanker, N. (2007). Multichannel shopping: Causes and consequences. Journal of Marketing, 71(2), 114–132.

Verhoef, P. C., Kannan, P. K., & Inman, J. J. (2015). From Multi-Channel Retailing to Omni-Channel Retailing. Journal of Retailing, 91(2), 174–181.

Verhoef, P. C., Neslin, S. A., & Vroomen, B. (2007). Multichannel customer management: Understanding the research-shopper phenomenon. International Journal of Research in Marketing, 24(2), 129–148.

Wang, R. J.H., Malthouse, E. C., & Krishnamurthi, L. (2015). On the go: how mobile shopping affects customer purchase behavior. Journal of Retailing, 91(2), 217–234.

Zomerdijk, L. G., & Voss, C. A. (2010). Service Design for Experience-Centric Services. Journal of Service Research, 13(1), 67–82.

## Appendix

Conversion rates serve as an additional input data for the real-world case. In our case, the conversion rate matrix is a 63 × 63 matrix. In Table A.1, we only display conversation rates that differ from 0.

<table><tr><td>from</td><td>to</td><td>value</td><td>from</td><td>to</td><td>value</td><td>from</td><td>to</td><td>value</td><td>from</td><td>to</td><td>value</td><td>from</td><td>to</td><td>value</td></tr><tr><td>c0p0</td><td>c0p0</td><td>0.1</td><td rowspan="2">c1p1</td><td rowspan="2">c2p3</td><td rowspan="2">13/80</td><td>c1p4</td><td>c3p4</td><td>0.01</td><td>c2p3</td><td>c3p4</td><td>0.184</td><td>c3p1</td><td>c2p2</td><td>0.125</td></tr><tr><td>c0p0</td><td>c0p8</td><td>0.5</td><td>c2p1</td><td>c0p0</td><td>0.1</td><td>c2p4</td><td>c0p0</td><td>0.02</td><td>c3p1</td><td>c2p3</td><td>0.125</td></tr><tr><td>c0p0</td><td>c1p1</td><td>0.03</td><td>c1p1</td><td>c3p2</td><td>0.05</td><td rowspan="2">c2p1</td><td rowspan="2">c1p2</td><td>17/80</td><td>c2p4</td><td>c1p4</td><td>0.01</td><td>c3p1</td><td>c3p2</td><td>0.05</td></tr><tr><td>c0p0</td><td>c1p2</td><td>1/12</td><td>c1p2</td><td>c0p0</td><td>0.1</td><td>0</td><td>c2p4</td><td>c2p4</td><td>0.01</td><td>c3p2</td><td>c0p0</td><td>0.25</td></tr><tr><td>c0p0</td><td>c1p3</td><td>0.03</td><td>c1p2</td><td>c1p3</td><td>0.4</td><td rowspan="2">c2p1</td><td rowspan="2">c1p3</td><td>17/80</td><td>c2p4</td><td>c2p5</td><td>0.95</td><td>c3p2</td><td>c1p3</td><td>0.375</td></tr><tr><td>c0p0</td><td>c2p1</td><td>0.03</td><td>c1p2</td><td>c2p3</td><td>0.5</td><td>0</td><td>c2p4</td><td>c3p4</td><td>0.01</td><td>c3p2</td><td>c2p3</td><td>0.375</td></tr><tr><td>c0p0</td><td>c2p2</td><td>1/12</td><td>c1p3</td><td>c0p0</td><td>0.05</td><td rowspan="2">c2p1</td><td rowspan="2">c2p2</td><td>17/80</td><td>c2p5</td><td>c0p0</td><td>0.05</td><td>c3p4</td><td>c0p0</td><td>0.02</td></tr><tr><td>c0p0</td><td>c2p3</td><td>0.03</td><td>c1p3</td><td>c1p3</td><td>0.01</td><td>0</td><td>c2p5</td><td>c2p6</td><td>0.95</td><td>c3p4</td><td>c1p4</td><td>0.01</td></tr><tr><td>c0p0</td><td>c3p1</td><td>0.03</td><td>c1p3</td><td>c1p4</td><td>0.276</td><td rowspan="2">c2p1</td><td rowspan="2">c2p3</td><td>17/80</td><td>c2p6</td><td>c0p0</td><td>0.175</td><td>c3p4</td><td>c2p4</td><td>0.01</td></tr><tr><td>c0p0</td><td>c3p2</td><td>1/12</td><td>c1p3</td><td>c2p3</td><td>0.01</td><td>0</td><td>c2p6</td><td>c2p6</td><td>0.55</td><td>c3p4</td><td>c2p5</td><td>0.95</td></tr><tr><td>c0p8</td><td>c0p8</td><td>1</td><td>c1p3</td><td>c2p4</td><td>0.47</td><td>c2p1</td><td>c3p2</td><td>0.05</td><td>c2p6</td><td>c2p7</td><td>0.275</td><td>c3p4</td><td>c3p4</td><td>0.01</td></tr><tr><td>c1p1</td><td>c0p0</td><td>0.3</td><td>c1p3</td><td>c3p4</td><td>0.184</td><td>c2p2</td><td>c0p0</td><td>0.05</td><td>c2p7</td><td>c0p8</td><td>1</td><td rowspan="10" colspan="3"></td></tr><tr><td rowspan="2">c1p1</td><td rowspan="2">c1p2</td><td rowspan="2">13/80</td><td>c1p4</td><td>c0p0</td><td>0.02</td><td rowspan="2">c2p2</td><td rowspan="2">c1p3</td><td>19/80</td><td>c3p1</td><td>c0p0</td><td>0.45</td></tr><tr><td>c1p4</td><td>c1p4</td><td>0.01</td><td>0</td><td>c3p1</td><td>c1p2</td><td>0.125</td></tr><tr><td rowspan="2">c1p1</td><td rowspan="2">c1p3</td><td rowspan="2">13/80</td><td>c1p4</td><td>c2p4</td><td>0.01</td><td rowspan="2">c2p2</td><td rowspan="2">c2p3</td><td>19/80</td><td rowspan="7">c3p1</td><td rowspan="7">c1p3</td><td rowspan="7">0.125</td></tr><tr><td>c1p4</td><td>c2p5</td><td>0.95</td><td>0</td></tr><tr><td rowspan="5">c1p1</td><td rowspan="5">c2p2</td><td rowspan="5">13/80</td><td rowspan="5" colspan="3"></td><td>c2p3</td><td>c0p0</td><td>0.05</td></tr><tr><td>c2p3</td><td>c1p3</td><td>0.01</td></tr><tr><td>c2p3</td><td>c1p4</td><td>0.276</td></tr><tr><td>c2p3</td><td>c2p3</td><td>0.01</td></tr><tr><td>c2p3</td><td>c2p4</td><td>0.47</td></tr></table>

Table A.1 - Conversion rates of the real-world case

## Mindfully going omni-channel: An economic decision model for evaluating omni-channel strategies Tables

<table><tr><td colspan="10">Current OCS</td></tr><tr><td>Channels/Process steps</td><td>Indefinite</td><td>Need/Interest</td><td>First contact</td><td>Schedule of appointment</td><td>Information</td><td>Consulting</td><td>Negotiation</td><td>Conclusion of contract</td><td>Termination point</td></tr><tr><td colspan="10">Established channels</td></tr><tr><td>Auxiliary channel</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td>Online</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Agency</td><td>0</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td>Brochures</td><td>0</td><td>1</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td colspan="10">Newly considered channels</td></tr><tr><td>Online (std.)</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Telephone</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Video</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td colspan="10">Restriction matrix</td></tr><tr><td>Process steps/Process steps</td><td>Indefinite</td><td>Need/Interest</td><td>First contact</td><td>Schedule of appointment</td><td>Information</td><td>Consulting</td><td>Negotiation</td><td>Conclusion of contract</td><td>Termination point</td></tr><tr><td>Indefinite</td><td>1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td>Need/Interest</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>First contact</td><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Schedule of appointment</td><td>1</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Information</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Consulting</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>Negotiation</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td><td>0</td></tr><tr><td>Conclusion of contract</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td>Termination point</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td colspan="10">Initial demand for two months ( $\eta \cdot H$ )</td></tr><tr><td>Channels/Process steps</td><td>Indefinite</td><td>Need/Interest</td><td>First contact</td><td>Schedule of appointment</td><td>Information</td><td>Consulting</td><td>Negotiation</td><td>Conclusion of contract</td><td>Termination point</td></tr><tr><td colspan="10">Established channels</td></tr><tr><td>Auxiliary channel</td><td>15</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Online</td><td>0</td><td>15</td><td>20</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Agency</td><td>0</td><td>7</td><td>36</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Brochures</td><td>0</td><td>4</td><td>3</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td colspan="10">Newly considered channels</td></tr><tr><td>Online (std.)</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Telephone</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Video</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td colspan="8">Switching matrix</td><td colspan="2">Time</td></tr><tr><td>Channels/Channels</td><td>Auxiliary channel</td><td>Online</td><td>Agency</td><td>Brochures</td><td>Online (std.)</td><td>Telephone</td><td>Video</td><td>H: Number of process steps for a PDP</td><td>12</td></tr><tr><td>Auxiliary channel</td><td>1</td><td>0.75</td><td>0.5</td><td>0.25</td><td>0.75</td><td>0.5</td><td>0.5</td><td rowspan="2"> $\eta$ : Length of one process step</td><td rowspan="2">5 days</td></tr><tr><td>Online</td><td>0.25</td><td>1</td><td>0.25</td><td>0.25</td><td>0.75</td><td>0.5</td><td>0.5</td></tr><tr><td>Agency</td><td>0.25</td><td>0.5</td><td>1</td><td>0.25</td><td>0.5</td><td>0.75</td><td>0.75</td><td rowspan="2"> $\theta$ : Length of one period</td><td rowspan="2">1 year</td></tr><tr><td>Brochures</td><td>0.75</td><td>0.25</td><td>0.25</td><td>1</td><td>0.25</td><td>0.25</td><td>0.25</td></tr><tr><td>Online (std.)</td><td>0.25</td><td>0.75</td><td>0.25</td><td>0.25</td><td>1</td><td>0.5</td><td>0.5</td><td>T: Planning horizon</td><td>3 years</td></tr><tr><td>Telephone</td><td>0.25</td><td>0.5</td><td>0.5</td><td>0.25</td><td>0.5</td><td>1</td><td>0.75</td><td rowspan="2"> $\eta \cdot H$ : Length of one PDP</td><td rowspan="2">60 days</td></tr><tr><td>Video</td><td>0.25</td><td>0.5</td><td>0.5</td><td>0.25</td><td>0.5</td><td>0.75</td><td>1</td></tr><tr><td colspan="8">Variable outflows per customer</td><td rowspan="2">Investment outflows</td><td rowspan="2">Channel-specific outflows</td></tr><tr><td>Channels/Process steps</td><td>First contact</td><td>Schedule of appointment</td><td>Information</td><td>Consulting</td><td>Negotiation</td><td>Conclusion of contract</td><td></td></tr><tr><td>Auxiliary channel</td><td>0.00 €</td><td>0.00 €</td><td>0.00 €</td><td>0.00 €</td><td>0.00 €</td><td>0.00 €</td><td>0.00 €</td><td>0.00 €</td><td>1,430.00 €</td></tr><tr><td>Online</td><td>0.00 €</td><td>0.00 €</td><td>0.00 €</td><td>0.00 €</td><td>0.00 €</td><td>0.00 €</td><td>0.00 €</td><td>18,416.67 €</td><td>New customer rate</td></tr><tr><td>Agency</td><td>0.00 €</td><td>0.75 €</td><td>2.00 €</td><td>123.59 €</td><td>40.00 €</td><td>19.48 €</td><td>0.00 €</td><td>33,450.00 €</td><td>2.30%</td></tr><tr><td>Brochures</td><td>0.20 €</td><td>0.00 €</td><td>0.00 €</td><td>0.00 €</td><td>0.00 €</td><td>0.00 €</td><td>0.00 €</td><td>833.33 €</td><td>Churn rate</td></tr><tr><td>Online (std.)</td><td>0.00 €</td><td>0.00 €</td><td>0.00 €</td><td>81.85 €</td><td>9.00 €</td><td>2.87 €</td><td>40,000.00 €</td><td>18,416.67 €</td><td>0%</td></tr><tr><td>Telephone</td><td>0.00 €</td><td>0.75 €</td><td>2.00 €</td><td>123.59 €</td><td>40.00 €</td><td>19.48 €</td><td>40,000.00 €</td><td>28,666.67 €</td><td>Interest rate</td></tr><tr><td>Video</td><td>0.00 €</td><td>0.75 €</td><td>2.00 €</td><td>123.59 €</td><td>40.00 €</td><td>19.48 €</td><td>40,000.00 €</td><td>33,000.00 €</td><td>5%</td></tr></table>

Table 1 - Real-world input data for the demonstration example

<table><tr><td rowspan="2">ID</td><td colspan="2">Overview of new states to be opened</td><td rowspan="2">Value contribution</td><td rowspan="2">Comment</td></tr><tr><td>Considered channel(s)</td><td>Considered process step(s)</td></tr><tr><td>1</td><td>-</td><td>1 2 3 4 5 6 7</td><td>0 €</td><td>Current OCS</td></tr><tr><td>2</td><td>Online for Standards</td><td>1 2 3 4 5 6 7</td><td>-68.304 €</td><td rowspan="6">Stepwise opening of a new channel (using the example of the channel Online for standards)</td></tr><tr><td>3</td><td>Online for Standards</td><td>1 2 3 4 5 6 7</td><td>-92.199 €</td></tr><tr><td>4</td><td>Online for Standards</td><td>1 2 3 4 5 6 7</td><td>-187.082 €</td></tr><tr><td>5</td><td>Online for Standards</td><td>1 2 3 4 5 6 7</td><td>-112.920 €</td></tr><tr><td>6</td><td>Online for Standards</td><td>1 2 3 4 5 6 7</td><td>-763.930 €</td></tr><tr><td>7</td><td>Online for Standards</td><td>1 2 3 4 5 6 7</td><td>796.693 €</td></tr><tr><td>8</td><td>Telephone</td><td>1 2 3 4 5 6 7</td><td>79.161 €</td><td>Complete opening of a new channel</td></tr><tr><td>9</td><td>Telephone</td><td>1 2 3 4 5 6 7</td><td>446.338 €</td><td>Channel-specific local optimum</td></tr><tr><td>10</td><td>Video</td><td>1 2 3 4 5 6 7</td><td>66.768 €</td><td>Complete opening of a new channel</td></tr><tr><td>11</td><td>Online for Standards &amp; Telephone</td><td>1 2 3 4 5 6 7</td><td>378.513 €</td><td rowspan="3">Combined complete opening of two new channels</td></tr><tr><td>12</td><td>Online for Standards &amp; Video</td><td>1 2 3 4 5 6 7</td><td>366.120 €</td></tr><tr><td>13</td><td>Telephone &amp; Video</td><td>1 2 3 4 5 6 7</td><td>2.227 €</td></tr><tr><td>14</td><td>Online for Standards, Telephone, &amp; Video</td><td>1 2 3 4 5 6 7</td><td>110.719 €</td><td>Combined complete opening of three new channels</td></tr><tr><td>15</td><td>Online for Standards, Telephone, &amp; Video</td><td>1 2 3 4 5 6 7</td><td>270.541 €</td><td>The bank&#x27;s initially preferred OCS</td></tr><tr><td>16</td><td>Online for Standards &amp; Telephone</td><td>1 2 3 4 5 6 7</td><td>877.212 €</td><td>Optimal OCS</td></tr></table>

Table 2 - OCSs and corresponding value contributions

# ACCEPTED MANUSCRIPT

<table><tr><td>from</td><td>to</td><td>value</td><td>from</td><td>to</td><td>value</td><td>from</td><td>to</td><td>value</td><td>from</td><td>to</td><td>value</td><td>from</td><td>to</td><td>value</td></tr><tr><td>c0p0</td><td>c0p0</td><td>0.1</td><td>c1p1</td><td>c2p3</td><td>13/80</td><td>c1p4</td><td>c3p4</td><td>0.01</td><td>c2p3</td><td>c3p4</td><td>0.184</td><td>c3p1</td><td>c2p2</td><td>0.125</td></tr><tr><td>c0p0</td><td>c0p8</td><td>0.5</td><td>c1p1</td><td>c3p2</td><td>0.05</td><td>c2p1</td><td>c0p0</td><td>0.1</td><td>c2p4</td><td>c0p0</td><td>0.02</td><td>c3p1</td><td>c2p3</td><td>0.125</td></tr><tr><td>c0p0</td><td>c1p1</td><td>0.03</td><td>c1p2</td><td>c0p0</td><td>0.1</td><td>c2p1</td><td>c1p2</td><td>17/80</td><td>c2p4</td><td>c1p4</td><td>0.01</td><td>c3p1</td><td>c3p2</td><td>0.05</td></tr><tr><td>c0p0</td><td>c1p2</td><td>1/12</td><td>c1p2</td><td>c1p3</td><td>0.4</td><td>c2p1</td><td>c1p3</td><td>17/80</td><td>c2p4</td><td>c2p4</td><td>0.01</td><td>c3p2</td><td>c0p0</td><td>0.25</td></tr><tr><td>c0p0</td><td>c1p3</td><td>0.03</td><td>c1p2</td><td>c2p3</td><td>0.5</td><td>c2p1</td><td>c2p2</td><td>17/80</td><td>c2p4</td><td>c2p5</td><td>0.95</td><td>c3p2</td><td>c1p3</td><td>0.375</td></tr><tr><td>c0p0</td><td>c2p1</td><td>0.03</td><td>c1p3</td><td>c0p0</td><td>0.05</td><td>c2p1</td><td>c2p3</td><td>17/80</td><td>c2p4</td><td>c3p4</td><td>0.01</td><td>c3p2</td><td>c2p3</td><td>0.375</td></tr><tr><td>c0p0</td><td>c2p2</td><td>1/12</td><td>c1p3</td><td>c1p3</td><td>0.01</td><td>c2p1</td><td>c3p2</td><td>0.05</td><td>c2p5</td><td>c0p0</td><td>0.05</td><td>c3p4</td><td>c0p0</td><td>0.02</td></tr><tr><td>c0p0</td><td>c2p3</td><td>0.03</td><td>c1p3</td><td>c1p4</td><td>0.276</td><td>c2p2</td><td>c0p0</td><td>0.05</td><td>c2p5</td><td>c2p6</td><td>0.95</td><td>c3p4</td><td>c1p4</td><td>0.01</td></tr><tr><td>c0p0</td><td>c3p1</td><td>0.03</td><td>c1p3</td><td>c2p3</td><td>0.01</td><td>c2p2</td><td>c1p3</td><td>19/80</td><td>c2p6</td><td>c0p0</td><td>0.175</td><td>c3p4</td><td>c2p4</td><td>0.01</td></tr><tr><td>c0p0</td><td>c3p2</td><td>1/12</td><td>c1p3</td><td>c2p4</td><td>0.47</td><td>c2p2</td><td>c2p3</td><td>19/80</td><td>c2p6</td><td>c2p6</td><td>0.55</td><td>c3p4</td><td>c2p5</td><td>0.95</td></tr><tr><td>c0p8</td><td>c0p8</td><td>1</td><td>c1p3</td><td>c3p4</td><td>0.184</td><td>c2p3</td><td>c0p0</td><td>0.05</td><td>c2p6</td><td>c2p7</td><td>0.275</td><td>c3p4</td><td>c3p4</td><td>0.01</td></tr><tr><td>c1p1</td><td>c0p0</td><td>0.3</td><td>c1p4</td><td>c0p0</td><td>0.02</td><td>c2p3</td><td>c1p3</td><td>0.01</td><td>c2p7</td><td>c0p8</td><td>1</td><td></td><td></td><td></td></tr><tr><td>c1p1</td><td>c1p2</td><td>13/80</td><td>c1p4</td><td>c1p4</td><td>0.01</td><td>c2p3</td><td>c1p4</td><td>0.276</td><td>c3p1</td><td>c0p0</td><td>0.45</td><td></td><td></td><td></td></tr><tr><td>c1p1</td><td>c1p3</td><td>13/80</td><td>c1p4</td><td>c2p4</td><td>0.01</td><td>c2p3</td><td>c2p3</td><td>0.01</td><td>c3p1</td><td>c1p2</td><td>0.125</td><td></td><td></td><td></td></tr><tr><td>c1p1</td><td>c2p2</td><td>13/80</td><td>c1p4</td><td>c2p5</td><td>0.95</td><td>c2p3</td><td>c2p4</td><td>0.47</td><td>c3p1</td><td>c1p3</td><td>0.125</td><td></td><td></td><td></td></tr></table>

Table A.1 - Conversion rates of the real-world case

# ACCEPTED MANUSCRIPT

Maximilian Röglinger is a Professor of Information Systems at the University of Bayreuth. Maximilian serves as Deputy Academic Director of the Research Center Finance & Information Management (FIM). Most of Maximilian’s work centers around business process management, customer relationship management, and digital transformation. He publishes in journals like Business & Information Systems Engineering, Business Process Management Journal, Decision Support Systems, Journal of the Association for Information Systems, and Journal of Strategic Information Systems. Maximilian is Technologies, Hilti, Radeberger Group, and Siemens. Maximilian earned his PhD at the University of Augsburg, and holds a Diploma in Business and Information Systems Engineering from the University of Bamberg.

Sabiölla Hosseini studied in the Elite Graduate Program Finance & Information Management at the University of Augsburg and the Technische Universität München. He also studied at Tongji University in Shanghai and Queensland University of Technology i Brisbane, Australia. Since 2015, Sabiölla is working as a research assistant at the Research Center Finance & Information Management. He gained practical experience in projects with BASF, Deutsche Bahn, and Siemens.

Annette Wenninger is studying in the Elite Graduate Program Finance & Information Management at the University of Augsburg and the Technische Universität München. Since summer 2016, Annette is a research fellow at the Research Center Finance & Information Management.

Marieluise Merz is studying in the Elite Graduate Program Finance & Information Management at the University of Augsburg and the Technische Universität München. She also studied at Santa Clara University in California. Since summer 2016, Marieluise is a research fellow at the Research Center Finance & Information Management.

# Mindfully going omni-channel: An economic decision model for evaluating omni-channel strategies

Highlights

\- We propose a decision model for determining an appropriate omni-channel strategy.

\- The decision model is the first to capture non-sequential customer journeys.

We evaluate the decision model based on real-world data from a German bank.

![](/api/attachments/PXGCDYRM/fulltext/images/7ec0c00e6d533a4bcf5f5acec6e8374dbdb246ee46268d7d090a13d78372fcf7.jpg)  
Figure 1

<table><tr><td></td><td>Indefinite</td><td>Process step 1</td><td>...</td><td>Process step N-1</td><td>Termination point</td></tr><tr><td>Auxiliary channel</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Channel 1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>...</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Channel M</td><td></td><td></td><td></td><td></td><td></td></tr></table>

Figure 2

![](/api/attachments/PXGCDYRM/fulltext/images/54622915e37a1fdef7b56ba371aa6954a93337cbacdaed8b4805dbc891d0aed4.jpg)

<table><tr><td colspan="4">Initial situation</td><td rowspan="15"><img src="/api/attachments/PXGCDYRM/fulltext/images/7c111711651ad584783c560c4684f99d55fc6ad5668232d7998bc3241313d325.jpg"/> Opening a new state Ingoing edges <img src="/api/attachments/PXGCDYRM/fulltext/images/fc3e5303643bd66a3c3bc2b7dde16f7f6dee16b26c4e0e0de5a585d0fb09e84a.jpg"/></td><td colspan="4">Perspective of an existing state First Summand</td><td rowspan="5" colspan="4">Perspective of a new state</td></tr><tr><td></td><td>Process step 1</td><td>Process step 2</td><td>Process step 3</td><td></td><td>Process step 1</td><td>Process step 2</td><td>Process step 3</td></tr><tr><td>Channel 1</td><td rowspan="3" colspan="3"><img src="/api/attachments/PXGCDYRM/fulltext/images/f693551c29a36a3086c6bfb4d6420962dc9142a46b9bb5cc6d531c346df95958.jpg"/></td><td>Channel 1</td><td rowspan="3" colspan="3"><img src="/api/attachments/PXGCDYRM/fulltext/images/ce7325eb395c407f23b5bb226eda73e7e63ed265f91e1e3cec10c3235af1cabb.jpg"/></td></tr><tr><td>Channel 2</td><td>Channel 2</td></tr><tr><td>Channel 3</td><td>Channel 3</td></tr><tr><td rowspan="10" colspan="4"> $r_{i,j,k,l}^{\text{mod}} = x_{i,j} \cdot x_{k,l} \cdot q_{j,i} \cdot \{r_{i,j,k,l} + \sum_{t=0}^{M} \sum_{u=0}^{N} F_1 \cdot r_{i,j,t,u} \cdot (1 - x_{\tau,u}) - \sum_{t=0}^{M} \sum_{u=0}^{N} F_2 \cdot r_{i,j,k,l} \cdot y_{\tau,u}$  <img src="/api/attachments/PXGCDYRM/fulltext/images/3045ce070ff9d2f3b64c418676d603b9dd3c85d374187c67eb8791dd9429fd70.jpg"/> +  $F_4 \cdot y_{i,j}$ </td><td colspan="4">Second Summand</td><td rowspan="5" colspan="4">Third Summand</td></tr><tr><td></td><td>Process step 1</td><td>Process step 2</td><td>Process step 3</td></tr><tr><td>Channel 1</td><td rowspan="5" colspan="3"><img src="/api/attachments/PXGCDYRM/fulltext/images/6ce65381816e12619189f7ef4bc9a2d8ae4e99d5656e8022b21a0b9f67e3b41b.jpg"/></td></tr><tr><td>Channel 2</td></tr><tr><td>Channel 3</td></tr><tr><td></td><td colspan="4">Fourth Summand</td></tr><tr><td></td><td rowspan="4"></td><td>Process step 1</td><td>Process step 2</td><td>Process step 3</td></tr><tr><td>Channel 1</td><td colspan="3"></td><td></td><td></td><td></td></tr><tr><td>Channel 2</td><td colspan="3"></td><td></td><td></td><td></td></tr><tr><td>Channel 3</td><td colspan="3"></td><td></td><td></td><td></td></tr></table>

Legend:

One PDP with H steps

One PDP with H steps

![](/api/attachments/PXGCDYRM/fulltext/images/074b4ebe0bc23773045c154a86abe5ee8f2569c5cc09e93ed67ed08fd69c9282.jpg)

Demand Vector D1

Period τ = 1

Demand Vector D2

Period τ = 2

Figure 4

![](/api/attachments/PXGCDYRM/fulltext/images/c850f5febc063998d47f6b966385afbe211dcb9b57d23b76b3029a2429be0002.jpg)  
Figure 5

![](/api/attachments/PXGCDYRM/fulltext/images/176615aedd34238119b8d8a5e3c92760408a3a3a381a5949ca72e5c8c131e2d6.jpg)  
Figure 6
