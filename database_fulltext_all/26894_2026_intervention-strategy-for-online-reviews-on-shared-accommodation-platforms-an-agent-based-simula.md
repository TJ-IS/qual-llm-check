---
otero_id: 26894
otero_key: "HXHTWTF6"
title: "Intervention Strategy for Online Reviews on Shared Accommodation Platforms: An Agent-Based Simulation Model"
authors: "Guoyin Jiang; Yingchao Fu"
year: "2026"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00980"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Volume 27 Issue 3

Article 1

2026

# Intervention Str ategy for Online Re   views on Shar ed Accommodation Platforms: An Agent-Based Simulation Model

Guoyin Jiang , jiangguoyin@uestc.edu.cn

Yingchao Fu

, 202221160315@std.uestc.edu.cn

Follow this and additional works at: https://aisel.aisnet.org/jais

ISSN 1536-9323

# Intervention Strategy for Online Reviews on Shared Accommodation Platforms: An Agent-Based Simulation Model

Guoyin Jiang,<sup>1</sup> Yingchao Fu<sup>2</sup>

<sup>1</sup>University of Electronic Science & Technology of China, China, jiangguoyin@uestc.edu.cn <sup>2</sup>University of Electronic Science & Technology of China, China, 202221160315@std.uestc.edu.cn

## Abstract

Although previous studies have underscored the significance of management interventions for online reviews on sharing platforms, limited research has comprehensively examined the dynamics of review interventions within competitive contexts. This study addresses this gap by developing a data-driven agent-based model that can simulate complex stakeholder interactions on shared accommodation platforms. This model examines the coevolution of direct interventions (i.e., positive review incentives) and indirect interventions (i.e., managerial responses and overstatement) alongside pricing and service strategies. The market is categorized into egoistic, altruistic, and hybrid types, thereby showing the influences of market composition on the effectiveness and marginal effects of review interventions. Findings reveal that positive review incentives and overstatement have a complementary relationship: The increase in one aspect results in a rise in the other aspect. However, prohibiting positive review incentives has unintended consequences, such as increased overstatement. Meanwhile, a substitutive relationship exists between positive review incentives and managerial responses. These interventions exert different impacts on providers’ profits: Positive review incentives have an inverted U-shaped effect on providers profits, whereas other interventions have a positive correlation with profits. Furthermore, the shifts between market types change the marginal effects of these strategies, which can mitigate some of their negative consequences. This research advances the understanding of review intervention dynamics across different market settings and provides guidance for platforms in formulating effective operation policies.

Keywords: Sharing Platforms, Intervention Strategy, Online Reviews, Agent-Based Modeling, Egoism and Altruism

John Qi Dong was the accepting senior editor. This research article was submitted on March 10, 2024, and underwent three revisions.

## 1 Introduction

Platforms for short-term accommodations, such as Booking.com and Airbnb, have rapidly become popular because they have streamlined the efficiency of utilizing and sharing idle resources. Their pronounced growth and influence on the hospitality industry have attracted considerable attention. Accommodation services are driven by the guests’ experience: Consumers can only extensively evaluate the quality of a service after they experience it; therefore, online reviews are critical for consumers’ decision-making (Li & Wu, 2018). A survey conducted by TripAdvisor about consumers’ reliance on such reviews reveals that 81% of travelers regularly or always consult reviews before booking. In addition, 79% select higher-rated properties among similar options, whereas 52% would never consider booking a hotel without reviews (TripAdvisor, 2019).

With the growing influence of online reviews, platforms and businesses are now actively shaping review dynamics. For instance, platforms provide incentives for users to entice them to write reviews and boost engagement (Fradkin & Holtz, 2023; Liu et al., 2024; Ma et al., 2024).

Meanwhile, incentives for positive reviews may be offered by businesses to enhance their reputation and sales. However, such practice can compromise fair market competition, which can drive platforms to tighten their policies. One such policy is Amazon’s 2016 Antimanipulation policy, which delists products and suspends accounts that have been involved in fraudulent activities.<sup>1</sup> Similarly, other platforms, such as Airbnb and Booking.com, have reinforced the integrity of reviews by restricting incentives for customer feedback.<sup>2</sup> <sup>,3</sup> Despite these efforts, businesses continue to incentivize positive reviews because of their proven positive effect on sales (Wang et al., 2022; Yin et al., 2016); meanwhile, platforms struggle to monitor and enforce compliance effectively. Aside from incentivizing reviews, businesses also indirectly steer the direction of reviews through managerial responses and overstatement; such an intervention influences consumer perceptions and purchasing decisions (Liu et al., 2023; Ullah et al., 2016).

Although researchers have focused on individual intervention strategies (Chen et al., 2019; Wu et al., 2023; Zhang et al., 2023), the dynamic interactions among these strategies in competitive settings require additional investigation. Notably, conventional mathematical or quantitative methods have not extensively discussed stakeholders’ nonlinear and nuanced interactions, bounded rationality, and feedback loops (Hannah et al., 2021; He et al., 2017). The present study addresses this gap by using a data-driven agent-based modeling (ABM) approach, which is suitable for investigating systems that are characterized by adaptive agents, emergent dynamics, and evolving behavior patterns in context of IS discipline (Benbya et al., 2020; Dong, 2022). Platform ecosystems exhibit properties of complex adaptive systems, where providers interact with consumers by dynamically adjusting their strategies (e.g., review interventions, pricing, and quality) based on performance feedback and strategic responses from competitors. Although the nonlinear and path-dependent dynamics that arise from these interactions are difficult to capture using analytical models, they can be effectively investigated through bottom-up ABM simulations (Benbya et al., 2020; Epstein & Axtell, 1996). The ABM approach can explore how direct interventions (i.e., positive review incentives) and indirect interventions (i.e., managerial responses and overstatement) coevolve with pricing and service decisions, which can ultimately influence stakeholder outcomes and social welfare. It can also examine the covariant relationships between these interventions and identify the conditions under which providers are likely to adopt specific strategies.

Moreover, the diversity of service providers across shortterm accommodation platforms has intensified the complexity of these behavior dynamics. Previous studies have demonstrated how participant strategies and outcomes are influenced by market type differences, which are driven by several factors, such as demand size (Zhou et al., 2019), consumer sensitivity (Liu et al., 2019b; Wang et al., 2017), consociality, and platform intermediation (Danatzis et al., 2024; Perren & Kozinets, 2018). However, these works have focused on demandside heterogeneity or entirely distinct markets. As such, they have inadequately explored the influence of supplyside differences within the same industry on strategy effectiveness. The emergence of homestay providers into the hotel-dominated market presents a practical scenario to examine this issue. Current studies have investigated how homestay providers’ market entry has affected hotel operators’ sales performance, pricing strategies, and market share fragmentation (Dogru et al., 2019; Li & Srinivasan, 2019; Zervas et al., 2017). However, few studies have investigated the influence of market composition on providers’ review interventions and the marginal effects of their actions. This study addresses this gap by deepening the exploration of the issue.

Three primary types of market composition in the shortterm accommodation sector are considered: platforms dominated by hotel operators (e.g., Hotelbeds), those dominated by homestay providers (e.g., Airbnb), and hybrid platforms (e.g., Booking.com and Ctrip) that cater to B2C and C2C markets by collaborating with both hotel operators and homestay providers. Homestay hosts in C2C markets often behave altruistically. They take measures to enhance guest experiences to foster crosscultural exchanges and build social reputations. However, they typically only benefit guests who are directly associated with their services because information about other participants’ benefits is usually inaccessible. Given that egoism and altruism are not mutually exclusive (Krebs, 1991), homestay providers may display altruistic behaviors while maintaining profitability. This behavior can be referred to as partial altruism. By contrast, hotel operators are mainly profit driven and exhibit egoistic behaviors. Based on these distinctions, this work models homestay hosts as partially altruistic providers and hotel operators as purely egoistic providers. Then, it categorizes markets into two homogeneous types, where only partially altruistic or purely egoistic providers exist, and one heterogeneous type, where both providers coexist. Notably, prior research has predominantly focused on profit-driven markets, thus paying little attention to the effects of strategies in heterogeneous markets with altruistic and egoistic providers (Shmidt, 2020). Understanding the coexistence between altruism and egoism is important for analyzing competitive behaviors and decision-making processes in these environments. This study examines these market structures by addressing two key questions:

(1) How do different review intervention strategies coevolve on platforms under a competitive environment?

(2) How do shifts between market types alter the marginal effects of these interventions on participant benefits?

We answer these questions by creating a data-driven agent-based shared accommodation model (DASAM), which simulates complex supply-demand interactions across platforms with varying market compositions. Based on the literature on review intervention strategies, value cocreation theory, expectation confirmation theory, and online reviews, the model is implemented and validated using secondary consumer booking data and primary data on provider-consumer review interactions from Airbnb. It captures the dynamic interactions between providers and consumers, thereby highlighting the covariant relationships among various review intervention strategies.

Key findings reveal that positive review incentives and overstatement have a complementary relationship, that is, increasing one aspect tends to increase the other aspect. However, platform policies that strictly prohibit positive review incentives may result in unintended outcomes, such as increased overstatement. Similarly, managerial responses and overstatement have a complementary relationship. Notably, altruistic providers rarely adopt both strategies simultaneously. Effective responses to negative reviews not only reflect providers’ characteristics but also indicate consumer-friendly decision-making. Additionally, a substitutive effect is observed between positive review incentives and managerial responses. Positive review incentives follow an inverted U-shaped relationship with provider profits, whereas managerial responses and overstatement have a positive correlation with profits. Furthermore, shifts between market types modify the marginal effects of these interventions, thereby possibly alleviating some negative outcomes. Overall, this bottom-up perspective on complex information systems provides insights into how review intervention strategies operate across different markets. It provides platform operators with guidelines for designing adaptive regulatory policies.

The rest of this paper is organized as follows. Section 2 reviews the relevant literature. Then, Section 3 details the operational processes of shared accommodation platforms and describes agents’ decision-making. Next, Section 4 extensively discusses the empirical data mining, model validation, and experimental design. The experimental results are presented in Section 5, where their underlying reasons are also explored. Finally, Section 6 concludes with the study’s contributions, limitations, and suggestions for future research.

## 2 Literature Review

## 2.1 Intervention Strategies for Online Reviews

Online reviews have posed numerous challenges and opportunities. As such, managers have become increasingly motivated to explore strategies that improve review quality and positivity, which can subsequently boost business profits. This study focuses on three common interventions.

## 2.1.1 Positive Review Incentives Strategy

Previous studies have comprehensively discussed strategies for incentivizing online reviews, which involve platforms offering monetary rewards, discounts, gifts, or coupons to encourage consumers to share valuable feedback. Although these incentives substantially increase the review volume (Burtch et al., 2018; Khernam-nuai et al., 2018), they may compromise the quality of consumer feedback. Moreover, the broader effects of these rewards remain debatable. Incentives may motivate moderately satisfied consumers to contribute; such added feedback can improve the representativeness of review distribution (Karaman, 2021). However, such incentives, which seek to reduce reviewers’ self-selection, have also been found to lower the quality of transaction matching (Fradkin & Holtz, 2023; Park et al., 2023). Moreover, offering monetary incentives can lead to product selection bias because highly rated products will receive a disproportionately large number of reviews (Khern-amnuai et al., 2018). Performance-based incentives that offer rewards based on the quality of feedback can also affect subsequent reviews and have spillover effects (Liu et al., 2024; Ma et al., 2024).

Our study focuses on a business-driven approach referred to as positive review incentives or praise cashback strategies, which is different from platform-implemented incentives. For instance, consumers receive incentives (e.g., cash) after they have posted a positive online review (Wu et al., 2023). Although this strategy is controversial, it is preferred by businesses because it can boost sales (Wang et al., 2022; Yin et al., 2016). Service recovery theory proposes that monetary compensation can mitigate consumer dissatisfaction from service failures, thereby decreasing the likelihood of making negative reviews (Nazifi et al., 2022). However, such an incentive may encourage users to create fake reviews that may diminish the product matching quality and undermine social welfare (Lee et al., 2018; Wu et al., 2023).

## 2.1.2 Managerial Response Strategy

The engagement of businesses with review-response interactions reflects how these entities prioritize online reviews. A managerial response (MR) is a recovery mechanism for service failures (Proserpio & Zervas, 2017). It helps businesses to mitigate the effects of negative reviews and protect their reputation (Liu et al., 2023). Responding to negative reviews improves consumer satisfaction (Chen et al., 2019; Gu & Ye, 2014) and strengthens brand image and corporate reputation (Sparks et al., 2016). Meanwhile, MR to positive reviews is effective only under specific conditions. For instance, it often highlights the positive aspects that are mentioned in reviews; consumers may perceive this action as a marketing tactic, thereby potentially generating negative reactions among future consumers (Wang & Chaudhry, 2018).

Furthermore, the effectiveness of MR is significantly determined by their characteristics, such as volume, intensity, emotional tone, timeliness, similarity, richness, and relevance (Huang et al., 2021; Kim et al., 2021; Le & Ha, 2021; Liu et al., 2021; Sheng et al., 2021). Building on these insights, this study categorizes MR into two types: enhancing responses and destructive responses. Enhancing responses involve addressing consumer concerns directly and demonstrating a proactive managerial attitude. According to service recovery and value cocreation theories, timely and targeted enhancing responses bolster consumers’ perceptions of a product or service’s emotional value (Chen et al., 2019; Gu & Ye, 2014). Therefore, it improves the provider’s image (Sparks et al., 2016). Meanwhile, destructive responses are often generic, dismissive, or demeaning; hence, they cannot resolve review concerns, which can lead to negative outcomes (Liu et al., 2021). These two types elucidate the providers’ response preferences. Moreover, they are useful in examining how MR influences stakeholder decision-making and benefits.

## 2.1.3 Overstatement Strategy

Marketer-generated content (MGC) commonly uses overstatement as a strategy, which involves companies exaggerating their product or service quality to increase profits (Lv et al., 2023). Although online reviews reduce information asymmetry, the prevalence of review interventions and fake reviews motivates managers to make inflated claims. Overstatement can attract consumers; however, it can also reduce review valence because unmet expectations lead to negative feedback (Ullah et al., 2016). Given these considerations, the degree of overstatement must be balanced carefully. Research has found that authentic advertising generally increases sales, yet excessive truthfulness can negatively affect profits (Becker et al., 2019). Overstatement in MGC has been extensively studied in the context of experience-based products (Liang et al., 2020; Song et al., 2019; Uthaisar et al., 2023). However, additional research is needed to determine its relationship with other review intervention strategies (Zhang et al., 2023). Accordingly, this study incorporates overstatement as a key factor in this correlation.

## 2.2 Review Types Classification Based on Value Cocreation

Value creation theory explains how businesses and consumers interact to create value. As such, servicedominant logic states that value is cocreated through the collaboration between consumers and providers (Maglio & Spohrer, 2008; Vargo et al., 2008). Providers of shared accommodations actively engage with consumers by offering services through authentic interactions that fulfill consumer needs and generate positive experiences (Camilleri & Neuhofer, 2017). Consumers assess the service’s real value during its delivery while comparing it with their expectations; this evaluation determines the consumers’ satisfaction levels (An & Han, 2020). As an emotional state, low satisfaction elicits negative emotions, whereas high satisfaction induces positive emotions. The cognition-emotion-behavior framework suggests that consumers’ satisfaction levels influence their motivation to leave reviews (Li et al., 2024). Thus, perceived value can be inferred from review text (Camilleri & Neuhofer, 2017; Dolan et al., 2019). However, value interaction extends beyond the period of the guest’s stay. Provider responses have two functions: influencing guest satisfaction and shaping potential customers’ attitudes (Esmark Jones et al., 2018). Therefore, reviews significantly influence potential consumers’ initial value judgements. Subsequently, the responses of the provider contribute to the consumers’ final perception. On the basis of their final value state, reviews are classified into four categories: value cocreation, review-side value decline, response-side value decline, and value co-destruction. Section 3.2.2 discusses how these reviews are categorized.

## 2.3 Complex System and Agent-Based Model

Research on review interventions has extensively relied on empirical testing and game theory (Zhang et al., 2023). However, the effectiveness of these approaches is often challenged by the complexity of online platforms (Malgonde et al., 2020). The limited availability of data has hindered the empirical investigation of microlevel dynamics of behaviors and the underlying mechanisms (Harrison et al., 2007; Wei et al., 2023). Although analytical models can provide equilibrium solutions, they often overlook the critical aspects of real platform environments, such as dynamic interactions, agent heterogeneity, randomness, and bounded rationality, because of their oversimplified assumptions (Benbya et al., 2020; He et al., 2017; Yu et al., 2020). The review intervention problem examined in this study inherently belongs to the domain of complex adaptive systems (CAS) due to three key features. First, the system involves high agent heterogeneity, that is, service providers differ fundamentally in behavioral logic depending on whether they are egoistic or altruistic. Furthermore, consumers not only diverge in their preferences but also encounter dynamically evolving decision scenarios. Cumulative system feedback can alter consumers’ perception of reviews over time. As such, the decision environment can vary per individual. Second, intervention strategies and consumer responses exhibit nonlinear and mutually dependent dynamics. Consumer feedback and the strategic behaviors of competitors influence how providers make and modify decisions. Simultaneously, these strategies can sway consumer perceptions, thus creating interactional feedback loops. Third, agents adaptively adjust their behavior under bounded rationality. In this scenario, they continuously update their decisions based on experiences, payoff outcomes, and environmental signals. Providers seek to optimize multiple competing objectives under uncertain demand, while consumers adjust their choice based on evolving reputational cues.

ABM is an effective framework for understanding complex, dynamic interactions. It is a bottom-up simulation approach that is tailored for CAS contexts and reveals the macrolevel patterns that arise from microlevel behaviors and interactions (Benbya et al., 2020; Epstein & Axtell, 1996). ABM diverges from static or equationbased models by providing flexibility and representational fidelity, thus making it suitable for tracing the influence of adaptive behavior on system-level outcomes over time. These advantages have resulted in the extensive application of ABM in socioeconomic research, including market competition (He et al., 2017), recommender systems (Malgonde et al., 2020), innovation platforms (Haki et al., 2024), and online reviews (Jiang et al., 2020). The current study builds on the existing research, which informs the development of DASAM. It deconstructs microinteractions to identify the internal pathways through which review interventions affect stakeholders’ macrolevel benefits. In doing so, this work extends the application of ABM in online review research.

Over-parameterization presents substantial challenges in ABM. This issue has motivated scholars to emphasize the importance of validating and verifying simulation models to provide an accurate representation of real-world systems (Fioretti, 2013; Heath et al., 2009). For instance, Carley (2002) categorized validation into four levels, namely, grounding (including face, process, and parameter validation), calibration, verification, and harmonizing. Furthermore, Sargent (2015) integrated verification and validation into the development of a simulation model; this process involved three important steps, namely, verifying the computational model, validating the conceptual models, and using actual data for operational validation. This study follows these recommendations by incorporating real hotel booking and Airbnb review datasets to construct a data-driven simulation model. Then, the proposed DASAM is validated by comparing simulation outcomes with the various aspects of real-world data.

## 3 Agent-Based Model for Shared Accommodation Platforms

## 3.1 Overview

We constructed a bilateral matching market with two distinct accommodation providers and ?? heterogeneous consumers. In this model, a sharing economy platform acts as an intermediary that offers services to providers and consumers. Additionally, it charges providers a commission fee to support the delivery of services. Table 1 presents the variables for these agents. Meanwhile, Figure 1 illustrates DASAM’s workflow.

The DASAM process for each period ?? is detailed as follows:

(1) Provider decision-making: Providers determine the price $P _ { i } ^ { ( t ) }$ , service quality $S _ { i } ^ { ( t ) }$ , positive review incentives $\varepsilon _ { i } ^ { ( t ) }$ , and degree of overstatement $\zeta _ { i } ^ { ( t ) }$ for period ?? . The providers’ response preferences are exogenous in the model.

(2) Consumer booking and check-in: A subset of consumers logs into the platform. Then, the consumers book available rooms that suit their preferences. The model is simplified by assuming that consumers check in on the same day as the day of their booking.

(3) Consumer feedback: After checking out, consumers decide whether to post a review about their experience.

(4) Provider response: Providers rely on their response preferences when responding to consumer reviews.

## 3.2 Behavior of Consumer Agents

The daily number of consumers (?? ) who log into the platform follows a probability density function $f _ { X } .$ . Each consumer’s stay duration ( ?? , in days) is assumed to follow a distribution $f _ { D } .$ . In this scenario, a consumer logs into the platform on a specific ???????? with a planned stay duration of ?? days. Upon logging ${ \mathrm { i n } } ,$ the consumer evaluates the available rooms based on prices, claimed service quality, and existing reviews. Then, they decide whether to book a room with that provider. If a booking is made, then the consumer checks in on their selected date and checks out after ?? days.

Table 1. Agent-Related Variables Used in DASAM

<table><tr><td>Agent</td><td>Variable</td><td>Remark</td><td> $Type^a$ </td></tr><tr><td rowspan="8">Provider i</td><td> $\Gamma_i$ </td><td>Type of the provider i</td><td>XV</td></tr><tr><td> $g_i$ </td><td>Degree of altruism</td><td>XV</td></tr><tr><td> $(\delta p_i, \delta n_i)$ </td><td>Response probabilities for positive and negative reviews</td><td>XV</td></tr><tr><td> $(\gamma p_i, \gamma n_i)$ </td><td>Response preference for positive and negative reviews</td><td>XV</td></tr><tr><td> $P_i^{(t)}$ </td><td>Room price of provider i at period t</td><td>DV</td></tr><tr><td> $S_i^{(t)}$ </td><td>Actual service level (or quality) of provider i at period t</td><td>DV</td></tr><tr><td> $\zeta_i^{(t)}$ </td><td>Degree of overstatement at period t</td><td>DV</td></tr><tr><td> $\varepsilon_i^{(t)}$ </td><td>Amount of positive review incentives at period t</td><td>DV</td></tr><tr><td rowspan="6">Consumer j</td><td> $v_0$ </td><td>Fixed utility of accommodation service</td><td>XV</td></tr><tr><td> $\alpha_j$ </td><td>Reputation preference</td><td>RV</td></tr><tr><td> $d_j^{(t)}$ </td><td>Duration of consumer accommodation</td><td>RV</td></tr><tr><td> $b_j^{(l)}$ </td><td>Effect of type l reviews on consumer choice</td><td>XV</td></tr><tr><td> $a_j^{(l)}$ </td><td>Effect of type l reviews on consumer benefit</td><td>XV</td></tr><tr><td> $Po\_val_j$ </td><td>Value threshold for positive reviews</td><td>RV</td></tr><tr><td>Platform</td><td>β</td><td>Commission rates</td><td>XV</td></tr><tr><td colspan="4">Note: a DV: decision variable; XV: exogenous variable; RV: random variable. The values of DVs are updated at each time step t, whereas XV values remain fixed in the model and vary only across simulation scenarios. RVs follow the specified distributions.</td></tr></table>

![](/api/attachments/HXHTWTF6/fulltext/images/41ad31aa36b76457ac3a6b8ed706750f6f24eec42d221fec2f6e7adda65d121a.jpg)  
Figure 1. Flowchart of the DASAM

![](/api/attachments/HXHTWTF6/fulltext/images/ad2627ce851b70d135f0b1bf1c43036e1b7193836b5525b128619923ee5cc8a3.jpg)  
Note: Different lines represent the formation pathways of reviews with different value states  
Figure 2. Classification and Formation of Review Types

## 3.2.1 Expected Surplus for Consumers

Consumers’ expected surplus is determined by two types of information: (1) providers’ self-disclosed information (e.g., prices and claimed quality) and (2) information about the providers’ reputation from online reviews (Chen & Xie, 2008).

## (1) Consumer surplus from self-disclosure information

Consumers derive a fixed utility $( v _ { 0 } )$ from fulfilling their accommodation needs. Their expected unit surplus is calculated based on the prices $P _ { i } ^ { ( t ) }$ and claimed service level $\left( 1 + \zeta _ { i } ^ { ( t ) } \right) \cdot S _ { i } ^ { ( t ) }$

$$
U s p _ {i, j} ^ {(t)} = v _ {0} + \left(1 + \zeta_ {i} ^ {(t)}\right) \cdot S _ {i} ^ {(t)} - P _ {i} ^ {(t)}\tag{1}
$$

## (2) Consumer surplus from reputation information

Consumers assess the service quality of a provider through online reviews (Weathers et al., 2007). They tend to avoid exaggerated claims, especially for experiential goods, such as short-term accommodation. Potential customers reduce their uncertainty about a service by reading reviews about the firsthand experiences of past users.

Review types: The interaction between consumer reviews and provider responses results in six possible review states. Based on the responses of providers, online reviews are categorized into value cocreation, value decline at the response side, value decline at the review side, and value co-destruction reviews. Figure 2 illustrates the mechanisms that form each type. A review is initially either positive or negative. Meanwhile, the managerial response is either enhancing or destructive. When provider responses are unavailable, the reviews are classified as positive or negative reviews without response.

Reputation preference of consumers: Reputation preference $\left( \alpha _ { j } \right)$ reflects how consumers prioritize the reputation of the provider. It follows a normal distribution: $\alpha _ { j } { \sim } N ( \mu _ { \alpha } , \sigma _ { \alpha } )$ . In addition, a positive correlation exists between review credibility and review volume (Xu, 2014). As the cumulative number of reviews $\begin{array} { r } { ( r v _ { i } ^ { ( t ) } = \sum _ { l } r v _ { i , l } ^ { ( t ) } } \end{array}$ where ${ r v } _ { i , l } ^ { ( t ) }$ represents the number of type ?? reviews for provider ??) increases, consumers’ reputation preferences converge to their true preference $\alpha _ { j }$ . Thus, the actual reputation preference of consumer ?? for provider ?? at time t is defined as

$$
\alpha_ {i, j} ^ {(t)} = \left(1 - e ^ {- r v _ {i} ^ {(t)}}\right) \cdot \alpha_ {j}.\tag{2}
$$

Assume that $b ^ { ( l ) }$ denotes the effect of type ?? reviews on the expected surplus of consumers; therefore, the expected surplus based on information regarding the provider’s reputation is calculated as

$$
U r _ {i, j} ^ {(t)} = \left[ \left(\sum_ {l} r v _ {i, l} ^ {(t)} \cdot b ^ {(l)}\right) / r v _ {i} ^ {(t)} \right] \cdot U s p _ {i, j} ^ {(t)}.\tag{3}
$$

In accordance with the principles of expected surplus maximization and loss aversion, consumers optimize their choices as follows:

$$
\max _ {i} U _ {i, j} ^ {(t)} = \left(1 - \alpha_ {i, j} ^ {(t)}\right) \cdot U s p _ {i, j} ^ {(t)} + \alpha_ {i, j} ^ {(t)} \cdot U r _ {i, j} ^ {(t)}, \quad s. t. U _ {i, j} ^ {(t)} \geq 0. \tag {4}
$$

If no option yields a positive surplus, then consumers cancel their reservation.

## 3.2.2 Review Rule of Consumers

After consumers have received a service, they assess the quality and calculate their actual unit surplus $( v _ { i , j } ^ { ( t ) } =$ $v _ { 0 } + S _ { i } ^ { ( t ) } - P _ { i } ^ { ( t ) } )$ . Expectation confirmation theory states that consumer satisfaction decreases if their expectations have not been met (Oliver, 1980), thus leading to emotional imbalance and low perceived value (Ho et al., 2017; Ullah et al., 2016). We model consumer satisfaction as $\pi _ { C S _ { i , j } } ^ { ( t ) } = \big ( v _ { i , j } ^ { ( t ) } - U _ { i , j } ^ { ( t ) } \big ) / U _ { i , j } ^ { ( t ) }$ and calculate perceived experiential value by using Equation 5. When $v _ { i , j } ^ { ( t ) } \geq 0 .$ 2 perceived experiential value increases as satisfaction rises. However, when $v _ { i , j } ^ { ( t ) } < 0$ , negative satisfaction is achieved. The perceived experiential value decreases correspondingly:

$$
v a l _ {i, j} ^ {(t)} = \left\{ \begin{array}{l} v _ {i, j} ^ {(t)} \cdot \left(1 + \left(v _ {i, j} ^ {(t)} - U _ {i, j} ^ {(t)}\right) / U _ {i, j} ^ {(t)}\right), i f v _ {i, j} ^ {(t)} \geq 0 \\ v _ {i, j} ^ {(t)} \cdot \left(1 + \left| \left(v _ {i, j} ^ {(t)} - U _ {i, j} ^ {(t)}\right) / U _ {i, j} ^ {(t)} \right|\right), i f v _ {i, j} ^ {(t)} <   0 \end{array} \right. \tag {5}
$$

Satisfaction reflects the consumers’ emotional state. Low satisfaction elicits negative emotions, whereas high satisfaction fosters positive ones; consequently, consumers’ level of satisfaction can influence their review behavior (Ho et al., 2017). Thus, we represent the probability of posting a review as $0 . 5 \cdot \stackrel { \textstyle \binom { - } { 1 } + } { \textstyle \binom { 1 + } { 1 , j } } -$ $U _ { i , j } ^ { ( t ) } { \Big ) } / U _ { i , j } ^ { ( t ) } { \Big | } { \Big ) }$

Consumers have individual thresholds for positive reviews, which follow a normal distribution:

$$
P o _ {v a l _ {j}} \sim N \big (\mu_ {P o _ {v a l}}, \sigma_ {P o _ {v a l}} ^ {2} \big).\tag{6}
$$

Given that providers incentivize positive reviews, review behavior follows nuanced rules:

(1) Spontaneous positive reviews: Consumers leave positive reviews when $v a l _ { i , j } ^ { ( t ) } \geq P o \_ v a l _ { j }$ , even without incentives; nevertheless, they receive incentives for doing so (Wu et al., 2023).

(2) Incentivized positive reviews: Consumers leave incentivized positive reviews when ???? $l _ { i , j } ^ { ( t ) } < P o _ { - } v a l _ { j }$ but $v a l _ { i , j } ^ { ( t ) } + \varepsilon _ { i } ^ { ( t ) } \geq P o \_ v a l _ { j }$

(3) Negative reviews: Consumers retain negative reviews when ???? $l _ { i , j } ^ { ( t ) } + \varepsilon _ { i } ^ { ( t ) } < P o .$ \_??????<sub>??</sub>.

## 3.2.3 Actual Perceived Benefits for Consumers

Consumers’ perceived benefits include perceived experience value, economic benefits, and provider response effects. Perceived experience value reflects the consumers’ adjusted surplus based on their satisfaction levels; as such, this value entails functional and emotional benefits (Candi & Kahn, 2016). Consumers gain economic benefits when they receive praise incentives from providers. Providers’ responses influence the consumers’ perceived benefits. Enhancing responses increase perceived benefits (through value cocreation or value compensation), whereas destructive responses reduce consumers’ perceptions (through value decline or value co-destruction). The total perceived benefits for each transaction are calculated as

$$
\pi_ {C _ {i, j}} ^ {(t)} = v a l _ {i, j} ^ {(t)} \cdot d _ {j} ^ {(t)} + \lambda_ {i, j} ^ {(t)} \cdot \varepsilon_ {i} ^ {(t)} + \sum_ {l} a ^ {(l)} \cdot r _ {j, l} ^ {(t)},\tag{7}
$$

where $\lambda _ { i , j } ^ { ( t ) }$ indicates whether a consumer has received incentives for leaving a positive review. $r _ { j , l } ^ { ( t ) }$ denotes whether consumer j left a type l review. $\begin{array} { r } { \sum _ { l } r _ { j , l } ^ { ( t ) } \le 1 } \end{array}$ implies that each consumer can submit at most one review. $a ^ { ( \hat { l } ) }$ represents the unit change in consumer benefits from forming a type ?? review.

## 3.3 Behavior of Provider Agents

The intrinsic traits (i.e., egoism or altruism combined with response preferences) and external strategies $( \mathrm { i . e . , }$ , review interventions and price-quality decisions) of providers are varying. Egoistic providers prioritize their benefits, whereas altruistic providers balance their gains and the consumers’ benefits based on their altruism level.<sup>4</sup>

The actual benefit over a time step for egoistic providers is defined as

$$
\pi_ {i} ^ {(t)} = \sum_ {j \in M _ {i} ^ {(t)}} \left[ d _ {j} ^ {(t)} \cdot ((1 - \beta_ {k}) \cdot P _ {i, k} ^ {(t)} - S _ {i, k} ^ {(t)}) - \lambda_ {i, j} ^ {(t)} \cdot \varepsilon_ {i} ^ {(t)} \right]\tag{8}
$$

where $M _ { i } ^ { ( t ) }$ represents the consumers served by provider ?? during time step ??. For simplicity, unit costs are equal to the actual service quality, which reflects a direct costquality relationship.

The providers’ decisions are formulated as an optimization problem:

$$
\begin{array}{r l} & {\underset {P _ {i, k} ^ {(t)}, S _ {i, k} ^ {(t)}, \zeta_ {i} ^ {(t)}, \varepsilon_ {i} ^ {(t)}} {\max} g _ {i} \cdot \sum_ {j \in M _ {i} ^ {(t)}} \pi_ {C _ {i, j}} ^ {(t)} + (1 - g _ {i}) \cdot \pi_ {i} ^ {(t)}} \\ & {\quad s. t. \left\{ \begin{array}{l l} 0 \leq P _ {i} ^ {(t)} <   \overline {{P}} \\ 0 \leq S _ {i} ^ {(t)} <   \overline {{S}} \\ 0 \leq \zeta_ {i} ^ {(t)} \leq \overline {{\zeta}} \\ 0 \leq \varepsilon_ {i} ^ {(t)} \leq \overline {{\varepsilon}} \\ \pi_ {i} ^ {(t)} \geq 0 \end{array} \right.} \end{array}\tag{9}
$$

where $g _ { i } = 0$ denotes an egoistic provider. Otherwise, the provider is altruistic. $\bar { P } _ { k }$ and $\bar { S } _ { k }$ are upper bounds for price and service quality, respectively. ??̅ and ?? ̅ represent the maximum degree of overstatement and positive review incentives, respectively. Although altruistic providers prioritize consumers’ needs, these providers also safeguard their own gains. This scenario is a realistic constraint in shared accommodation contexts.

The competitive decision among providers is a complex game with multiple decision variables and infinite possible solutions. Thus, this study applies a genetic algorithm to transform this issue into a multi-objective optimization problem, which generates approximate Pareto-optimal solutions. According to noncooperative game theory, rational strategies may decrease the possibility of having Pareto-optimal outcomes, as seen in the prisoner’s dilemma. This situation can result in market inefficiencies or failures in resource allocation. Platforms or regulators can address these issues by enforcing policies that can help achieve Pareto improvements and reach Pareto equilibrium (Guo et al., 2023; Tsunoda & Zennyo, 2021). Folk theorem states that Pareto-optimal equilibrium can be achieved in infinitely repeated games if the discount factor is sufficiently high (Friedman, 1971). Based on these analyses, decision combinations within the Pareto-optimal set are treated as potential game outcomes under bounded rationality. Providers make optimal decisions based on their current situation. A single solution will be randomly selected as the game outcome when multiple Paretooptimal solutions are available.

## 3.4 Platform Revenue and Total Social Welfare

A platform generates revenue through interactions between providers and consumers. Notably, this study has excluded the operational costs and additional revenue sources of platforms (e.g., traffic and advertising). Platform revenue is calculated as the sum of commissions from providers:

$$
\pi_ {p} ^ {(t)} = \sum_ {i = 1} ^ {H} \sum_ {j \in M _ {i} ^ {(t)}} d _ {j} ^ {(t)} \cdot (1 - \beta) \cdot P _ {i} ^ {(t)}.\tag{10}
$$

Total social welfare is derived from the aggregate benefits of all stakeholders:

$$
w ^ {(t)} = \pi_ {p} ^ {(t)} + \sum_ {i = 1} ^ {H} \pi_ {i} ^ {(t)} + \sum_ {i = 1} ^ {H} \sum_ {j \in M _ {i} ^ {(t)}} \pi_ {C _ {i, j}} ^ {(t)}.\tag{11}
$$

## 4 Simulation System Implementation and Experiments

## 4.1 Parameter Setting

Two empirical datasets from the hotel and shared accommodation industries were used to minimize the influence of certain parameters in the simulation model on the outcomes. The first dataset consisted of 119,390 reservation records from two hotels in Portugal, covering the period from July 1, 2015, to August 31, 2017 (Antonio et al., 2019). This information provided probability distributions for the stay duration and daily arrivals of guests. The second dataset contained 12,173 Airbnb listings in China, with 519,176 online reviews and 115,413 managerial responses collected from January 2018 to December 2019. This information supported the analysis on how providers’ response patterns and review type affect consumers’ purchase intentions. Appendix A1 presents the detailed utilization of these datasets and corresponding insights.

This study balanced computational efficiency and generalizability by examining two providers that were managing multiple rooms. The total numbers of rooms and consumer arrivals were scaled down by a factor of 10. This modification resulted in 17 rooms per provider and an average of 9.38 daily guest arrivals (Appendix A1.1). The 3-σ principle was used to set the normal distribution standard deviation to one third of the error’s upper limit. Statistical data and relevant literature were used as a basis to set some of the fixed parameter values in DASAM so that the simulation closely resembled the real system (Table 2). The other parameters were determined through multiple simulation experiments to ensure rationality.

DASAM is implemented within the non-dominated sorting genetic algorithm II (NSGA-II) framework to achieve multi-objective optimization (Deb et al., 2002). NSGA-II effectively handles the two or three objectives problem because of its efficient non-dominated sorting and crowding distance calculations, thus maintaining a balance between solution diversity and convergence. Therefore, NSGA-II is appropriate for addressing the biobjective optimization problem in this study, which includes conflicting goals among competing providers. Moreover, this framework has a relatively low computational complexity, thus making it suitable for the multiperiod evolution that is required in the simulation model. The parameters of the genetic algorithm include a population size of 30, 30 iterations, a crossover rate of 1, and a mutation rate of 1/8 (the reciprocal of the decision variable dimension). Constraints have been established so that each participant’s benefit exceeds 0.

Table 2. Values of Fixed Parameters in the Simulation Experiments

<table><tr><td>Parameter</td><td>Default value</td><td>Source</td></tr><tr><td> $g_i$ of altruistic providers</td><td>0.5</td><td>—</td></tr><tr><td> $v_0$ </td><td>0.3</td><td>—</td></tr><tr><td> $\bar{\varepsilon}$ </td><td>0.3</td><td>—</td></tr><tr><td> $\bar{\zeta}$ </td><td>0.3</td><td>—</td></tr><tr><td> $\bar{P}=\bar{S}$ </td><td>1</td><td>—</td></tr><tr><td> $N(\mu_\alpha,\sigma_\alpha)$ </td><td> $N(0.65,0.35/3)$ </td><td>From secondary data (Statista, 2020, 2021, 2023)</td></tr><tr><td> $N(\mu_{Po\_val},\sigma_{Po\_val})$ </td><td> $N(-0.2,0.1/3)$ </td><td>—</td></tr><tr><td> $\delta p_i,\delta n_i$ </td><td>0.198, 0.378</td><td>Airbnb (see Appendix A1.2)</td></tr><tr><td> $\gamma p_i,\gamma n_i$ </td><td>0.94, 0.50</td><td>Airbnb (see Appendix A1.2)</td></tr><tr><td> $b^{(1)},b^{(2)},b^{(3)},b^{(4)},b^{(5)},b^{(6)}$ </td><td>1.1, -1.5, 1.7, 0, 0, -2.3</td><td>Airbnb (see Appendix A1.2)</td></tr><tr><td> $a^{(1)},a^{(2)},a^{(3)},a^{(4)},a^{(5)},a^{(6)}$ </td><td>0, 0, 0.1, 0.15, -0.15, -0.15</td><td>Ullah et al. (2016)</td></tr><tr><td>β</td><td>0.15</td><td>Booking.com*</td></tr><tr><td colspan="3">* Taking Booking.com as an example, the commission rate of such accommodation platforms typically ranges between 10% and 20%. https://partner.booking.com/en-gb/help/commission-invoices-tax</td></tr></table>

Table 3. Descriptive Statistics of the Providers’ Decision

<table><tr><td>Market type</td><td>Subject</td><td>Type</td><td> $\zeta_i$ </td><td> $\varepsilon_i$ </td><td> $P_i$ </td><td> $S_i$ </td></tr><tr><td rowspan="3"> $EG^a$ </td><td>Provider 1</td><td>Egoism</td><td>.153(.088) $^b$ </td><td>.076(.068)</td><td>.561(.213)</td><td>.241(.186)</td></tr><tr><td>Provider 2</td><td>Egoism</td><td>.152(.089)</td><td>.075(.068)</td><td>.562(.215)</td><td>.238(.186)</td></tr><tr><td>Average</td><td>-</td><td>.153(.064)</td><td>.076(.047)</td><td>.562(.143)</td><td>.240(.133)</td></tr><tr><td rowspan="3">HB</td><td>Provider 1</td><td>Egoism</td><td>.154(.089)</td><td>.076(.067)</td><td>.549(.215)</td><td>.258(.197)</td></tr><tr><td>Provider 2</td><td>Altruism</td><td>.120(.089)</td><td>.140(.085)</td><td>.444(.267)</td><td>.186(.173)</td></tr><tr><td>Average</td><td>-</td><td>.137(.063)</td><td>.108(.053)</td><td>.500(.163)</td><td>.222(.128)</td></tr><tr><td rowspan="3">AL</td><td>Provider 1</td><td>Altruism</td><td>.122(.092)</td><td>.145(.085)</td><td>.420(.255)</td><td>.209(.189)</td></tr><tr><td>Provider 2</td><td>Altruism</td><td>.121(.090)</td><td>.140(.086)</td><td>.412(.251)</td><td>.200(.182)</td></tr><tr><td>Average</td><td>-</td><td>.121(.063)</td><td>.143(.060)</td><td>.416(.168)</td><td>.204(.121)</td></tr><tr><td colspan="3">ANOVA among different market types $^c$ </td><td>F=10759.534p&lt;.001</td><td>F=70285.031p&lt;.001</td><td>F=38875.716p&lt;.001</td><td>F=3402.669p&lt;.001</td></tr></table>

Note: <sup>a</sup> Variable abbreviations: EG: egoistic market; HB: hybrid market; AL: altruistic market; $\zeta _ { i } \colon$ provider $i ^ { \gamma } \mathbf { s }$ overstatement degree; $\varepsilon _ { i } \dot { : }$ provider $i ^ { \gamma } \mathrm { s }$ positive review incentives; $P _ { i } \colon$ provider i’s room price; $S _ { i } { : }$ provider i’s service quality. <sup>b</sup> The two values represent the mean and standard deviation (in parentheses) of the providers’ decision variables across multiple simulations and multi-period evolutions. <sup>c</sup> An ANOVA with an assumed homogeneity of variances was applied, followed by post hoc multiple comparisons using the HSD test. Welch’s ANOVA was performed only when the assumed homogeneity of variances was violated. The same testing procedure applies to all subsequent analyses unless otherwise specified.

## 4.2 Experimental Design and Model Outputs

This study examined dynamics across different market types, which function as distinct experimental scenarios. Providers’ response preferences were treated as exogenous variables in the analysis of the coevolution of endogenous decision variables. Empirical data show that providers responded favorably to positive reviews with near certainty (probability = 0.939, small standard deviation). Meanwhile, negative reviews received enhancing responses with a probability of approximately 0.50 and a large standard deviation (Appendix A1.2). Therefore, we focused on response preferences for negative reviews by testing $\gamma n _ { i }$ values of 0.1, 0.5, and 0.9. Then, we conducted $3 \times 3 \times 3$ experiments to evaluate the effects of online review interventions on agent behaviors, as well as their benefits across various submarkets. The proposed DASAM was implemented using Python. Then, the model was run 1,000 times per experiment to ensure robust statistical validity (Dong, 2021; Hu et al., 2011). The evolutionary model spanned 100 steps, with each step representing a 30- day period. The following output metrics were tracked:

(1) Social welfare ( ?? ), platform revenue $\left( \begin{array} { l } { \pi _ { p } } \end{array} \right)$ individual provider benefit $( \ \pi _ { i } \ ) ,$ and average consumer benefits per provider $\begin{array} { r l } { \big ( } & { { } \hat { \pi } _ { C _ { i } } = } \end{array}$ $\left( \sum _ { j \in M _ { i } } \pi _ { C _ { i , j } } \right) / | M _ { i } | )$

(2) Total provider benefits $\textstyle ( { \widehat { \pi } } = \sum \pi _ { i } )$ , platform-wide average consumer benefits $\begin{array} { r } { ( \bar { \pi } _ { C } = \left( \sum _ { i } \sum _ { j \in M _ { i } } \pi _ { C _ { i , j } } \right) / } \end{array}$ $\Sigma | M _ { i } | )$ and satisfaction $( \bar { \pi } _ { C S } )$

(3) Price $( P _ { i } )$ , service quality $( S _ { i } ) ,$ , net unit profit $( P _ { - } S _ { i } =$ $( 1 - \beta ) * P _ { i } - S _ { i } )$ , degree of overstatement $( \zeta _ { i } ) _ { : }$ , and positive review incentives (??<sub>??</sub>).

(4) Consumer perceptions of reviews $\begin{array} { r l } { ( } & { { } r p _ { i } = } \end{array}$ $\left( \sum _ { l } r v _ { i , l } \cdot b ^ { ( l ) } \right) / r v _ { i } \big )$

(5) Total number of consumers served by each provider $\left( | M _ { i } | \right)$ and by the platform $\begin{array} { r } { \left( M = \sum \vert M _ { i } \vert \right) } \end{array}$ during the current period.

## 4.3 Verification and Validation

Despite various challenges, ABMs must be verified and validated. Highly novel models can be validated by replicating prior results or comparing their results with empirical data (Dong, 2019). Therefore, this study built on the methodologies of Jiang et al. (2020), Wei et al. (2023), and Wei et al. (2024) to perform the following validation steps: conceptual model validation, which confirmed the theoretical foundations and assumptions of DASAM; computer model verification, which ensured that the concepts were translated accurately into the simulation; and input-output validation, which ensured that the model aligned with real-world systems. Input validation used empirical data (Appendix A1), while output validation compared the simulation results with real-world data (Appendix A2). The effect of various review and response types on the performance of providers was also examined. The results were cross-validated against previous studies.

## 4.3.1 Effect of Market Type on Providers’ Decision-Making

The simulation outputs confirmed that our conceptual model was implemented accurately. Table 3 presents the comparative analysis across market types, which demonstrates that egoistic and altruistic providers exhibit distinct behavioral patterns. Egoistic providers consistently set higher prices $( P _ { i } \colon 0 . 5 6 2$ vs. 0.416; 0.549 vs. $0 . 4 4 4 ) , ^ { 5 }$ offer lower incentives $( \varepsilon _ { i } \colon 0 . 0 7 6 \ \mathrm { v s . } \ 0 . 1 4 3 ;$ $0 . 0 7 6 \mathrm { v s } . 0 . 1 4 0 )$ , and engage in greater overstatement $( \zeta _ { i } \colon$ 0.153 vs. 0.121; 0.154 vs. 0.120) than altruistic providers. This strategic divergence is a result of fundamental differences in the providers’ objectives. For example, although overstatement can attract consumers, its potential to generate value co-destructive reviews contradicts altruistic goals. Therefore, altruistic providers lessen their reliance on this practice.

Prices and service levels declined progressively along the spectrum from egoistic to altruistic markets $( P _ { i } \colon 0 . 5 6 2 >$ $0 . 5 0 0 > 0 . 4 1 6 ; S _ { i } \colon 0 . 2 4 0 > 0 . 2 2 2 > 0 . 2 0 4 )$ . Prices decreased more sharply than service quality because altruistic providers value consumer benefits more highly than egoistic providers. Therefore, altruistic markets have favorable price-quality ratios. Moreover, competition induced strategic moderation because egoistic providers tend to adopt more consumer-friendly approaches in hybrid markets than they do in purely egoistic environments $( P _ { i } \colon$ $0 . 5 4 9 < 0 . 5 6 2 ; S _ { i } \colon 0 . 2 5 8 > 0 . 2 4 0 )$

An important trade-off can be observed in the incentive structure. Positive review incentives generate favorable reviews. However, profit-focused providers must carefully balance the cost of these incentives. Meanwhile, altruistic providers offer generous incentives, which are consistent with their value cocreation objectives. This reflects realworld practices, such as hosts offering their guests small gifts to foster positive feedback and relationships. The findings reveal that the model achieves internal consistency with conceptual agent goals. It also demonstrates how market composition influences strategic decision-making on platforms.

## 4.3.2 Effect of Market Type on Benefits of Stakeholders

The analysis of stakeholder benefits confirms that significant variations exist across different market types (Table 4). Platform revenue declined consistently from an egoistic market to an altruistic one $( \pi _ { p }$ 6 $1 . 1 8 3 > 5 3 . 8 0 5 > 4 7 . 3 2 9 )$ . This phenomenon was primarily driven by the pricing strategies of providers. This pricing dynamic created conflicting effects on consumption, with purchase volumes demonstrating an inverse relationship (??: 236.178 < 242.581 < 253.303).

The total provider benefits aligned with trends in platform revenue. By contrast, consumer benefits and overall social welfare exhibited opposing patterns (??̂: $1 4 1 . 0 9 1 > 1 1 0 . 4 0 2 > 7 8 . 0 3 6 ; \bar { \pi } _ { C } \colon 0 . 1 1 2 < 0 . 2 7 9 <$ 0.453; $w \colon 2 2 9 . 3 3 5 < 2 3 3 . 4 9 2 < 2 4 0 . 4 0 5 )$ . This finding indicates that consumers obtain great benefits from altruistic providers despite these providers receiving low returns because of low unit profits. In addition, the transactions between supply and demand create value that subsequently generates social welfare. Thus, high transaction volumes and improved transaction experiences improve total social welfare.

Table 4. Descriptive Statistics of Stakeholder Benefits

<table><tr><td rowspan="2">Subject</td><td colspan="3">Market type</td><td rowspan="2">ANOVA among different market types</td></tr><tr><td> $EG^a$ </td><td>HB</td><td>AL</td></tr><tr><td> $\pi_p$ </td><td>61.183(20.622) $^b$ </td><td>53.805(19.527)</td><td>47.329(18.892)</td><td>F=10057.599,p&lt;.001</td></tr><tr><td> $\pi_1$ </td><td>70.434(29.702)</td><td>71.128(24.918)</td><td>38.730(24.827)</td><td>F=46228.242,p&lt;.001</td></tr><tr><td> $\pi_2$ </td><td>70.657(29.766)</td><td>39.273(27.826)</td><td>39.306(24.456)</td><td>F=34065.535,p&lt;.001</td></tr><tr><td> $\hat{\pi}$ </td><td>141.091(28.073)</td><td>110.402(35.796)</td><td>78.036(37.315)</td><td>F=79813.829,p&lt;.001</td></tr><tr><td> $\bar{\pi}_{C_1}$ </td><td>.124(.120)</td><td>.134(.131)</td><td>.446(.244)</td><td>F=65691.955,p&lt;.001</td></tr><tr><td> $\bar{\pi}_{C_2}$ </td><td>.119(.113)</td><td>.444(.278)</td><td>.445(.243)</td><td>F=98040.449,p&lt;.001</td></tr><tr><td> $\bar{\pi}_C$ </td><td>.112(.083)</td><td>.279(.178)</td><td>.453(.180)</td><td>F=143359.420,p&lt;.001</td></tr><tr><td> $\bar{\pi}_{CS}$ </td><td>-2.082(1.538)</td><td>-1.560(1.304)</td><td>-.998(.811)</td><td>F=17589.873,p&lt;.001</td></tr><tr><td>w</td><td>229.335(42.421)</td><td>233.492(39.055)</td><td>240.405(32.256)</td><td>F=2513.506,p&lt;.001</td></tr><tr><td>M</td><td>236.178(45.455)</td><td>242.581(42.183)</td><td>253.303(34.826)</td><td>F=4883.021,p&lt;.001</td></tr><tr><td>rp</td><td>.704(.127)</td><td>.891(.096)</td><td>1.080(.064)</td><td>F=356600.187,p&lt;.001</td></tr><tr><td colspan="5">Note: $^a$  Variable abbreviations: EG: egoistic market; HB: hybrid market; AL: altruistic market;  $\pi_p$ : platform revenue;  $\pi_i$ : individual provider benefit;  $\hat{\pi}$ : total provider benefits;  $\bar{\pi}_{C_i}$ : average consumer benefits for provider i;  $\bar{\pi}_C$ : platform-wide average consumer benefits;  $\bar{\pi}_{CS}$ : platform-wide average</td></tr></table>

Note:<sup>a</sup> Variable abbreviations: EG: egoistic market; HB: hybrid market; AL: altruistic market; <sup>??</sup>??: platform revenue; <sup>??</sup>??: individual provider benefit; ??̂: total provider benefits; <sup>??̅</sup>??<sub>??</sub>: average consumer benefits for provider i; ??̅<sub>??</sub>: platform-wide average consumer benefits; ??̅<sub>????</sub>: platform-wide average consumer satisfaction; ??: social welfare; ??: total consumers served by the platform; ????: consumer’s review perception. <sup>b</sup> The two values represent the mean and standard deviation (in parentheses) of specific variables across multiple simulations and multi-period evolutions.

Table 5. Changed Values in Sensitivity Analyses

<table><tr><td>Parameter</td><td>Remark</td><td>Changed values</td></tr><tr><td> $g_i$  of altruistic providers</td><td>Altruism degree of altruistic providers</td><td>0.2,0.8</td></tr><tr><td> $N(\mu_\alpha,\sigma_\alpha)$ </td><td>Distribution of consumer&#x27;s reputation preference</td><td> $N(0.3,0.1),N(0.8,0.2/3)$ </td></tr><tr><td> $N(\mu_{Po\_val},\sigma_{Po\_val})$ </td><td>Distribution of consumer&#x27;s threshold for positive reviews</td><td> $N(-0.3,0.1/3),N(-0.1,0.1/3)$ </td></tr><tr><td> $b^{(1)},b^{(2)},b^{(3)},b^{(4)},b^{(5)},b^{(6)}$ </td><td>Impacts of reviews with different value states on consumer choices</td><td>(1.045,-1.425,1.615,0,0,-2.185),(1.155,-1.575,1.785,0,0,-2.415)</td></tr><tr><td> $a^{(1)},a^{(2)},a^{(3)},a^{(4)},a^{(5)},a^{(6)}$ </td><td>Impacts of reviews with different value states on consumer benefits</td><td>(0,0,0.095,0.1425,-0.1425,-0.1425),(0,0,0.105,0.1575,-0.1575,-0.1575)</td></tr></table>

## 4.3.3 Sensitivity Analyses

An extensive sensitivity analysis was conducted on key model parameters, including the altruism level of providers, consumer preferences for review reputation, thresholds for positive reviews, and the impact of reviews on consumer behavior and benefits. Table 5 presents the potential values of these parameters. The results indicate that providers’ decisions across different markets aligned with the conceptual model. These outcomes are qualitatively consistent with the existing findings, which are presented in Tables 3 and 4. <sup>6</sup>

## 5 Results

## 5.1 Correlations of Provider’s Internal Decisions

The natural breakpoint method was used to classify intervention levels. This approach facilitated the examination of how the focal provider’s other decisions vary depending on the intensity of specific review interventions while competitors optimize their strategies. This observation clarifies the nonlinear covariation between the focal provider’s other decisions or outcomes and the review interventions. The elbow method was used to divide the provider’s positive review incentives and overstatement into five levels (Tables 6 and 7).

## 5.1.1 Effect of Positive Review Incentive on Other Decisions

Providers’ review reputations were consistently enhanced across all market types when providers increased their incentives for positive reviews (Table 6). A clear pattern emerged in the providers overstatement behavior: Overstatement initially decreased when incentives were introduced. When providers did not offer incentives, they compensated for this by exaggerating claims, which can lead to the lowest review perception. We can derive that strictly prohibiting positive review incentives may inadvertently encourage overstatement, thus serving as a warning for platforms. Notably, providers gradually increased their overstatement practices when the incentive levels rose. These two factors have synergistic effects. Incentives improve review reputation and drive purchases, while overstatement boosts consumer appeal. In addition, incentives mitigate expectation-reality gaps caused by overstatement, thereby reducing negative feedback.

From the consumer perspective, low incentives effectively attract purchases, but higher levels reduce consumer demand in markets that are dominated by egoistic providers (Table 6a). This situation occurs because moderate incentives improve consumers’ review perception, thus raising their expected benefits. Meanwhile, excessive incentives boost providers’ costs. Consequently, providers may reduce consumer-friendly pricing and service decisions (reflected in the increased net profit margin) and suppress demand. Moreover, incentives had a negligible influence on consumer purchase in altruistic markets (Table 6d). Altruistic providers balanced overstatement and price-quality adjustments, thereby concealing the relationship between incentives and consumer decisions.

## 5.1.2 Effect of Overstatement on Other Decisions

Considering the existence of overstatement, providers increased incentives for positive review when overstatement levels rose, which confirms the complementary relationship between positive reviews and overstatement (Table 7). However, overstatement had varying effects on egoistic and altruistic providers. The former’s reputation diminished (Table 7a, 7b), whereas the latter still maintained its reputation (Table 7c, 7d). This difference occurred because cost constrained egoistic providers’ ability to offset satisfaction declines through incentives, whereas altruistic providers could effectively mitigate the reputational effect of overstatement.

Table 6. Covariation Between Providers’ Other Decisions and Outcomes with Positive Review Incentives

<table><tr><td>Provider type</td><td>Subjecta</td><td>No use</td><td>Low</td><td>Moderately low</td><td>Middle</td><td>Moderately high</td><td>High</td><td>Change directionb</td><td colspan="2">ANOVA</td></tr><tr><td rowspan="4">(a) Egoistic provider in egoistic market</td><td> $\zeta_i$ </td><td>.153</td><td>.149</td><td>.154</td><td>.158</td><td>.157</td><td>.162</td><td> $\searrow\nearrow$ </td><td>F=8.937</td><td>p&lt;.001</td></tr><tr><td> $rp_i$ </td><td>.621</td><td>.642</td><td>.672</td><td>.688</td><td>.691</td><td>.686</td><td> $\nearrow$ </td><td>F=78.043</td><td>p&lt;.001</td></tr><tr><td> $|M_i|$ </td><td>115.626</td><td>122.647</td><td>121.208</td><td>115.855</td><td>110.315</td><td>97.948</td><td> $\nearrow\searrow$ </td><td>F=70.760</td><td>p&lt;.001</td></tr><tr><td> $P\_S_i$ </td><td>.244</td><td>.230</td><td>.233</td><td>.239</td><td>.248</td><td>.271</td><td> $\searrow\nearrow$ </td><td>F=29.009</td><td>p&lt;.001</td></tr><tr><td rowspan="4">(b) Egoistic provider in hybrid market</td><td> $\zeta_i$ </td><td>.155</td><td>.146</td><td>.153</td><td>.167</td><td>.165</td><td>.159</td><td> $\searrow\nearrow$ </td><td>F=17.036</td><td>p&lt;.001</td></tr><tr><td> $rp_i$ </td><td>.615</td><td>.650</td><td>.677</td><td>.679</td><td>.679</td><td>.682</td><td> $\nearrow$ </td><td>F=31.077</td><td>p&lt;.001</td></tr><tr><td> $|M_i|$ </td><td>125.35</td><td>126.835</td><td>124.177</td><td>120.226</td><td>115.938</td><td>105.337</td><td> $\nearrow\searrow$ </td><td>F=54.455</td><td>p&lt;.001</td></tr><tr><td> $P\_S_i$ </td><td>.208</td><td>.204</td><td>.203</td><td>.212</td><td>.219</td><td>.224</td><td> $\searrow\nearrow$ </td><td>F=14.328</td><td>p&lt;.001</td></tr><tr><td rowspan="4">(c) Altruistic provider in hybrid market</td><td> $\zeta_i$ </td><td>.114</td><td>.111</td><td>.117</td><td>.119</td><td>.117</td><td>.134</td><td> $\searrow\nearrow$ </td><td>F=13.000</td><td>p&lt;.001</td></tr><tr><td> $rp_i$ </td><td>1.082</td><td>1.097</td><td>1.109</td><td>1.112</td><td>1.114</td><td>1.115</td><td> $\nearrow$ </td><td>F=23.432</td><td>p&lt;.001</td></tr><tr><td> $|M_i|$ </td><td>116.211</td><td>116.721</td><td>122.193</td><td>119.633</td><td>116.198</td><td>119.566</td><td> $\nearrow\searrow$ </td><td>F=3.753</td><td>P=.002</td></tr><tr><td> $P\_S_i$ </td><td>.185</td><td>.183</td><td>.178</td><td>.195</td><td>.204</td><td>.209</td><td> $\searrow\nearrow$ </td><td>F=12.489</td><td>p&lt;.001</td></tr><tr><td rowspan="4">(d) Altruistic provider in altruistic market</td><td> $\zeta_i$ </td><td>.108</td><td>.105</td><td>.118</td><td>.126</td><td>.127</td><td>.134</td><td> $\searrow\nearrow$ </td><td>F=43.578</td><td>p&lt;.001</td></tr><tr><td> $rp_i$ </td><td>1.068</td><td>1.086</td><td>1.100</td><td>1.104</td><td>1.105</td><td>1.106</td><td> $\nearrow$ </td><td>F=51.930</td><td>p&lt;.001</td></tr><tr><td> $|M_i|$ </td><td>127.649</td><td>126.369</td><td>127.269</td><td>125.569</td><td>127.056</td><td>126.023</td><td>—</td><td>F=1.915</td><td>p&lt;.088</td></tr><tr><td> $P\_S_i$ </td><td>.128</td><td>.138</td><td>.139</td><td>.158</td><td>.153</td><td>.166</td><td> $\nearrow$ </td><td>F=42.770</td><td>p&lt;.001</td></tr></table>

Note: <sup>a</sup> Variable abbreviations: $\zeta _ { i } \colon$ provider i’s overstatement degree; $r p _ { i } \colon$ consumer’s review perception for provider i; $\left| M _ { i } \right| ;$ total consumers served by provider i; $P _ { - } S _ { i } \colon$ provider i’s net unit profit (inversely proportional to consumer friendliness). <sup>b</sup> The “Change direction” column reflects the approximate change trend of a variable as the focal provider changes tactics, from not implementing a specific review intervention strategy to adopting it at a high level.

Table 7. Covariation Between Providers’ Other Decisions and Outcomes with Overstatement

<table><tr><td>Market type</td><td>Subjecta</td><td>No use</td><td>Low</td><td>Moderately low</td><td>Middle</td><td>Moderately high</td><td>High</td><td>Change directionb</td><td colspan="2">ANOVA</td></tr><tr><td rowspan="4">(a) Egoistic provider in egoistic market</td><td> $\varepsilon_i$ </td><td>.071</td><td>.069</td><td>.073</td><td>.074</td><td>.077</td><td>.077</td><td> $\searrow\nearrow$ </td><td>F=8.563</td><td>p&lt;.001</td></tr><tr><td> $rp_i$ </td><td>.694</td><td>.689</td><td>.671</td><td>.667</td><td>.656</td><td>.655</td><td> $\searrow$ </td><td>F=23.719</td><td>p&lt;.001</td></tr><tr><td> $|M_i|$ </td><td>111.416</td><td>116.015</td><td>116.038</td><td>118.459</td><td>117.37</td><td>118.677</td><td> $\nearrow$ </td><td>F=5.363</td><td>p&lt;.001</td></tr><tr><td> $P\_S_i$ </td><td>.213</td><td>.221</td><td>.234</td><td>.235</td><td>.248</td><td>.251</td><td> $\nearrow$ </td><td>F=43.225</td><td>p&lt;.001</td></tr><tr><td rowspan="4">(b) Egoistic provider in hybrid market</td><td> $\varepsilon_i$ </td><td>.084</td><td>.067</td><td>.078</td><td>.071</td><td>.080</td><td>.081</td><td> $\searrow\nearrow$ </td><td>F=13.682</td><td>p&lt;.001</td></tr><tr><td> $rp_i$ </td><td>.680</td><td>.688</td><td>.668</td><td>.663</td><td>.653</td><td>.661</td><td> $\nearrow\searrow$ </td><td>F=12.578</td><td>p&lt;.001</td></tr><tr><td> $|M_i|$ </td><td>118.659</td><td>120.308</td><td>120.181</td><td>121.552</td><td>120.347</td><td>125.222</td><td> $\nearrow$ </td><td>F=7.969</td><td>p&lt;.001</td></tr><tr><td> $P\_S_i$ </td><td>.198</td><td>.199</td><td>.207</td><td>.208</td><td>.214</td><td>.217</td><td> $\nearrow$ </td><td>F=15.783</td><td>p&lt;.001</td></tr><tr><td rowspan="4">(c) Altruistic provider in hybrid market</td><td> $\varepsilon_i$ </td><td>.126</td><td>.137</td><td>.133</td><td>.146</td><td>.149</td><td>.149</td><td> $\nearrow$ </td><td>F=12.955</td><td>p&lt;.001</td></tr><tr><td> $rp_i$ </td><td>1.108</td><td>1.109</td><td>1.108</td><td>1.108</td><td>1.112</td><td>1.109</td><td>—</td><td>F=.844</td><td>p=.518</td></tr><tr><td> $|M_i|$ </td><td>136.565</td><td>124.153</td><td>123.391</td><td>117.195</td><td>111.736</td><td>108.448</td><td> $\searrow$ </td><td>F=33.204</td><td>p&lt;.001</td></tr><tr><td> $P\_S_i$ </td><td>.120</td><td>.165</td><td>.173</td><td>.200</td><td>.228</td><td>.249</td><td> $\nearrow$ </td><td>F=92.160</td><td>p&lt;.001</td></tr><tr><td rowspan="4">(d) Altruistic provider in altruistic market</td><td> $\varepsilon_i$ </td><td>.127</td><td>.134</td><td>.140</td><td>.145</td><td>.150</td><td>.159</td><td> $\nearrow$ </td><td>F=43.744</td><td>p&lt;.001</td></tr><tr><td> $rp_i$ </td><td>1.104</td><td>1.100</td><td>1.098</td><td>1.097</td><td>1.100</td><td>1.100</td><td>—</td><td>F=1.915</td><td>p=.088</td></tr><tr><td> $|M_i|$ </td><td>135.082</td><td>131.093</td><td>126.944</td><td>124.42</td><td>123.15</td><td>122.821</td><td> $\searrow$ </td><td>F=46.255</td><td>p&lt;.001</td></tr><tr><td> $P\_S_i$ </td><td>.104</td><td>.118</td><td>.140</td><td>.161</td><td>.174</td><td>.187</td><td> $\nearrow$ </td><td>F=254.239</td><td>p&lt;.001</td></tr></table>

Note: <sup>a</sup> Variable abbreviations: ?? : provider i’s positive review incentives; ???? : consumer’s review perception for provider i; |?? |: total consumers served by provider i; $P _ { - } S _ { i } \colon$ provider i’s net unit profit (inversely proportional to consumer friendliness). <sup>b</sup> The “Change direction” column reflects the approximate change trend of a variable as the focal provider changes tactics, from not implementing a specific review intervention strategy to adopting it at a high level.

Table 8. Covariation Between Providers’ Other Decisions and Outcomes with Enhancing Response Preference

<table><tr><td>Provider type</td><td>Subjecta</td><td>Low</td><td>Middle</td><td>High</td><td>Change directionb</td><td colspan="2">ANOVA</td></tr><tr><td rowspan="5">(a) Egoistic provider in egoistic market</td><td> $\zeta_i$ </td><td>.148</td><td>.154</td><td>.156</td><td>↗</td><td>F=38.303</td><td>p&lt;.001</td></tr><tr><td> $\varepsilon_i$ </td><td>.081</td><td>.074</td><td>.071</td><td>↘</td><td>F=111.450</td><td>p&lt;.001</td></tr><tr><td> $rp_i$ </td><td>.827</td><td>.667</td><td>.615</td><td>↘</td><td>F=11917.976</td><td>p&lt;.001</td></tr><tr><td> $|M_i|$ </td><td>116.187</td><td>117.292</td><td>117.962</td><td>↗</td><td>F=6.919</td><td>p=.001</td></tr><tr><td> $P\_S_i$ </td><td>.241</td><td>.238</td><td>.236</td><td>↘</td><td>F=11.342</td><td>p&lt;.001</td></tr><tr><td rowspan="5">(b) Egoistic provider in hybrid market</td><td> $\zeta_i$ </td><td>.150</td><td>.156</td><td>.159</td><td>↗</td><td>F=26.233</td><td>p&lt;.001</td></tr><tr><td> $\varepsilon_i$ </td><td>.081</td><td>.076</td><td>.071</td><td>↘</td><td>F=56.502</td><td>p&lt;.001</td></tr><tr><td> $rp_i$ </td><td>.820</td><td>.666</td><td>.593</td><td>↘</td><td>F=7407.148</td><td>p=.032</td></tr><tr><td> $|M_i|$ </td><td>121.825</td><td>121.747</td><td>122.398</td><td>—</td><td>F=1.141</td><td>p=.319</td></tr><tr><td> $P\_S_i$ </td><td>.212</td><td>.209</td><td>.208</td><td>↘</td><td>F=5.051</td><td>p=.006</td></tr><tr><td rowspan="5">(c) Altruistic provider in hybrid market</td><td> $\zeta_i$ </td><td>.121</td><td>.120</td><td>.118</td><td>—</td><td>F=1.839</td><td>p=.159</td></tr><tr><td> $\varepsilon_i$ </td><td>.146</td><td>.141</td><td>.133</td><td>↘</td><td>F=55.895</td><td>p&lt;.001</td></tr><tr><td> $rp_i$ </td><td>1.145</td><td>1.109</td><td>1.015</td><td>↘</td><td>F=7396.224</td><td>p&lt;.001</td></tr><tr><td> $|M_i|$ </td><td>118.486</td><td>118.932</td><td>120.179</td><td>—</td><td>F=2.801</td><td>p=.061</td></tr><tr><td> $P\_S_i$ </td><td>.197</td><td>.194</td><td>.183</td><td>↘</td><td>F=20.832</td><td>p&lt;.001</td></tr><tr><td rowspan="5">(d) Altruistic provider in altruistic market</td><td> $\zeta_i$ </td><td>.121</td><td>.122</td><td>.121</td><td>—</td><td>F=1.713</td><td>p=.180</td></tr><tr><td> $\varepsilon_i$ </td><td>.148</td><td>.144</td><td>.137</td><td>↘</td><td>F=89.322</td><td>p&lt;.001</td></tr><tr><td> $rp_i$ </td><td>1.137</td><td>1.099</td><td>1.003</td><td>↘</td><td>F=16553.106</td><td>p&lt;.001</td></tr><tr><td> $|M_i|$ </td><td>126.678</td><td>126.526</td><td>126.393</td><td>—</td><td>F=.307</td><td>p=.735</td></tr><tr><td> $P\_S_i$ </td><td>.155</td><td>.150</td><td>.140</td><td>↘</td><td>F=82.935</td><td>p&lt;.001</td></tr></table>

Note: <sup>a</sup> Variable abbreviations: $\zeta _ { i } \colon$ provider $i ^ { \gamma } { \bf s }$ overstatement degree; $\varepsilon _ { i } :$ provider $i ^ { \circ } { \bf s }$ positive review incentives; $r p _ { i } \colon$ consumer’s review perception for provider i; $\left| M _ { i } \right| :$ total consumers served by provider i; $\mathrm { ~ , ~ } P _ { - } S _ { i } \mathrm { { : } }$ provider i’s net unit profit (inversely proportional to consumerfriendliness). <sup>b</sup> The “Change direction” column reflects the approximate change trend of a variable as the focal provider’s enhancing response preference increases.

For egoistic providers (Table 7a, 7b), overstatement increased consumer numbers. However, the effectiveness of this strategy depends on competitors. Engaging in overstatement effectively attracts more consumers than refraining from engaging in it, even at a low level, when egoistic providers compete against other egoistic providers (Table 7a). However, only high overstatement can effectively increase the influx of consumers when egoistic providers compete with altruistic competitors (Table 7b), who have strong reputations and consumer-friendly pricing.

## 5.1.3 Effect of Enhancing Response Preference for Negative Reviews on Other Decisions

Conversely, when altruistic providers engaged in increased overstatement, their number of consumers decreased (Table 7c, 7d). Excessive overstatement can drive altruistic providers to focus more on maximizing profit through increased unit margins than on maintaining consumer benefits. Thus, high overstatement indicates altruistic providers’ shift toward self-serving behaviors, which can pose disadvantages to consumers. This pattern emerged when providers exaggerated their service quality to gain profits. Therefore, platforms should strengthen their ability to detect false advertising to prevent altruistic providers from adopting egoistic behaviors in markets with altruistic providers.

We examined how providers’ tendency to give enhancing responses to negative reviews influenced the use of positive review incentives and overstatement. Low, middle, and high probabilities were set to 0.1, 0.5, and 0.9, respectively, in Table 8.

Egoistic providers raised overstatement levels and reduced positive review incentives while enhancing their responses to negative reviews (Table 8a, 8b). This strategy was effective for two reasons. (1) Enhancing responses cushioned the impact of negative feedback on reputation, thus ensuring that high overstatement could attract consumers. (2) These responses functionally replaced positive review incentives, thereby lowering costs. The conserved resources could then be used to improve price-quality decisions, as reflected in the decreased net profit margin. This finding suggests that active response behavior reflects not only the providers’ characteristics but also their consumer-oriented decision-making.

![](/api/attachments/HXHTWTF6/fulltext/images/1ff103597870897ac35003e491dacac200892702938e03b97940d681b161ee33.jpg)

![](/api/attachments/HXHTWTF6/fulltext/images/4d49aba85c932386c8763d362a4762bf34ee01bbb5d079c66f2dbb46702291ac.jpg)  
Figure 3. Effects of Positive Review Incentives on Provider and Consumer Benefits

Providers in egoistic markets (Table 8a) attracted consumers by leaving enhancing responses. However, this approach diminished the providers’ review reputation because of increased overstatement (producing negative reviews) and decreased incentives (lessening reviews on value cocreation). When egoistic providers compete with altruistic ones in a hybrid market (Table 8b), these synergistic strategies may fail to attract additional consumers because superior reputations and price–quality offerings maintain the competitive advantage of altruistic providers. For altruistic providers (Table 8c, 8d), increasing the enhancing responses does not tend to lead to increased overstatement, which is consistent with their altruistic orientation.

## 5.2 Effect of Review Intervention Strategies on Stakeholder Benefits

This study also analyzed how review intervention strategies influenced individual stakeholders and overall market outcomes. The results of this analysis can guide providers’ and consumers’ decision-making processes. Moreover, they can aid platforms and regulators in creating and improving relevant policies.

## 5.2.1 Effect of Review Intervention Strategies on Individual Benefit

The profits of egoistic and altruistic providers had an inverted U-shaped relationship with positive review incentives (Figure 3a). Table 6 demonstrates that these incentives improved the providers’ reputation. However, these providers had difficulty in consistently attracting customers. Providers raised prices when incentives were high, thus ultimately reducing the number of purchases.

Consumer benefits (Figure 3b) exhibited the opposite trend: benefits first declined and then rose as incentives increased. The consumer received the lowest benefits when providers set low or moderately low incentives for positive reviews. In this scenario, providers incurred minimal costs from incentives, thereby allowing them to set attractive pricing and quality decisions that encouraged consumer purchases. However, consumers’ perceived benefits declined because their high expectations were not met. This condition shows that incentives can negatively affect service matching quality.

Although increasing overstatement levels boosted the profits of all providers, the patterns differed across markets (Figure 4a). Low overstatement delivers the highest marginal benefits in egoistic markets, whereas further increases in overstatement can raise profits but only up to a certain point. In hybrid markets, egoistic providers must resort to high overstatement to maximize their profits when competing against altruistic providers’ better price-quality offerings and stronger reputations. While overstatement boosted provider profits, it consistently reduced consumer benefits across different markets (Figure 4b). High overstatement led to pricing and quality decisions that were not consumer friendly (Table 7), thus considerably reducing the benefits for customers.

Increasing the likelihood of enhancing responses to negative reviews significantly raised earnings for egoistic providers while reducing earnings for altruistic providers (Figure 5a). Tables 8a and 8b present the analysis of the covariance among provider strategies. They indicate that positive review incentives are reduced by the high probability of enhancing responses, thus allowing egoistic providers to increase their earnings by cutting costs that are associated with incentives. By contrast, altruistic providers experienced a substantial reduction in their net profit margins (Table 8c, 8d). This outcome suggests that altruistic providers prioritize consumer benefits over financial gains when they increase the probability of enhancing responses. This approach significantly benefits consumers (Figure 5b) because the enhancing responses lead to favorable price-quality decisions and offer emotional value by addressing service failures. Ultimately, consumer satisfaction increases.

![](/api/attachments/HXHTWTF6/fulltext/images/300b9fbef38cc59fdbb60100bf1990f5c0ada7878d7c463cafd852c1e23ef913.jpg)

![](/api/attachments/HXHTWTF6/fulltext/images/c55fe838bf146fc9782fb0bf71e8023e3575eba757a33a6820574a187501e7f6.jpg)  
Figure 4. Effects of Overstatement on Provider and Consumer Benefits

![](/api/attachments/HXHTWTF6/fulltext/images/f302627a37e729c2142c784605febf5bda2bb2d0e9781220a218534dd826af8c.jpg)

![](/api/attachments/HXHTWTF6/fulltext/images/2e667f5e1726ac83c4911449f67a21d6f04983ca897f9aa6f2af79c373062536.jpg)  
Figure 5. Effects of Enhancing Response Preference on Provider and Consumer Benefits

## 5.2.2 Effect of Review Intervention Strategies on Overall Benefits

We evaluated how review interventions affect key market outcomes, including total provider benefits ??̂ , average consumer benefits $\mathit { \overline { { \pi } } } _ { C } ,$ average consumer satisfaction $\overline { { \pi } } _ { C S } .$ platform revenue $\pi _ { p }$ , and total social welfare ?? . Our stepwise regression analysis (Appendix A5) reveals that these interventions had nonlinear effects at the macro level.

Although individual providers may benefit from giving low incentives for positive reviews, the market-wide adoption of this strategy reduces the overall benefits of providers (Figure 6a). Therefore, such incentives may have strong negative spillover effects on competitors benefits, thus ultimately diminishing the total benefits for all providers. Market type also serves as a moderator in this situation.

(1) In low-incentive markets, shifting from an egoistic market to a hybrid one reduces the negative effects on total provider benefits (i.e., positive review incentives in hybrid markets yield higher marginal effects at low incentive levels, compared to the effects in egoistic markets, as shown in Figure 6a). Meanwhile, altruistic markets mitigate the adverse effects of positive review incentives on provider benefits regardless of the level of incentives.

(2) In high-incentive markets, shifting from an egoistic market to a hybrid or altruistic one magnifies the positive marginal effect on consumer benefits (Figure 6b) and boosts social welfare (Figure 6e).

(3) Across all incentive levels, shifting from an egoistic market to a hybrid or altruistic one buffers the negative effect of these incentives on consumer satisfaction (Figure 6c).

Overstatement consistently reduced total social welfare across all market types (i.e., marginal effects are always below 0, as shown in Figure 7e). In egoistic markets, overstatement initially increased the total provider benefits because moderate levels of overstatement attract consumers without significantly damaging a provider’s reputation. However, when the optimal threshold was exceeded, negative reviews outmatched any benefits from overstatement, thus diminishing profits (Figure 7a). Hybrid and altruistic markets have different dynamics. High overstatement prompts altruistic providers to raise their unit profits significantly. Although provider benefits increase (Figure 7a), consumer benefits (Figure 7b) and satisfaction (Figure 7c) decrease. When excessive overstatement occurs, social welfare declines more steeply in markets with altruistic providers than in egoistic markets (Figure 7e). This situation suggests that regulators should prioritize controlling overstatement in these markets.

Market type strongly influences how enhancing responses to negative reviews affect market outcomes. In egoistic markets, the increased probability that providers will offer enhancing responses to negative reviews slightly reduces the average satisfaction of consumers. Nevertheless, it raises the overall stakeholder benefits and social welfare (Figure 8). Although provider gains are reduced, consumer satisfaction improves in hybrid markets. Altruistic markets present a trade-off. The providers’ earnings rise with enhancing responses, whereas consumer benefits and satisfaction decline, with neutral effects on social welfare and platform revenue.

We can derive that platforms in egoistic markets should promote proactive responses to negative reviews while also prioritizing consumer satisfaction. Meanwhile, platforms in hybrid markets should encourage providers to respond positively to negative reviews by offering incentives. Platforms in altruistic markets can promote enhancing responses according to their participants’ priorities.

![](/api/attachments/HXHTWTF6/fulltext/images/38c26c448d92a6a40dbc5949e1ce7d451078648e07a278d8e8d20741b4d98484.jpg)

![](/api/attachments/HXHTWTF6/fulltext/images/0c3a4018ff39fbac199b8b09317951f0a0df5cf9dccb60ed0da0d14a54a8a56e.jpg)

![](/api/attachments/HXHTWTF6/fulltext/images/67be535af6e19870b615e50388903b310b976c2c35b2cf8d7d1329a98e441fa7.jpg)

![](/api/attachments/HXHTWTF6/fulltext/images/0cacf43ce1e520e5d42aa61046759234f753b74b6577f96501ca7350599cd215.jpg)  
Figure 6. Marginal Effects of Positive Review Incentives on Market Outcomes

![](/api/attachments/HXHTWTF6/fulltext/images/b6285b3a30a5678da4808db7421307d4730586caede019fae82f7521949e5174.jpg)

![](/api/attachments/HXHTWTF6/fulltext/images/13076fa3a8ca98d7b0d60c45f8a933351b3d14d29d45b090b54aebfe6e44c5d0.jpg)

![](/api/attachments/HXHTWTF6/fulltext/images/f592afdc20aa40171a0e0e942e59b4e90be36a69bac12977abb679ff0ba541ca.jpg)

![](/api/attachments/HXHTWTF6/fulltext/images/408c50aa8bd9f43613fe7bc4c9c5106d107b745b90b0e003194ae5972aa2561a.jpg)

![](/api/attachments/HXHTWTF6/fulltext/images/dcc9cbdedda7ae934a85f4138ebcd6097fe5be6ef64d07e49fb3e7ea0955f85e.jpg)  
Figure 7. Marginal Effects of Overstatement on Market Outcomes

![](/api/attachments/HXHTWTF6/fulltext/images/423487051af48af36be9d486c340646ef981f9b5b74adc14b79914d01284cddf.jpg)

![](/api/attachments/HXHTWTF6/fulltext/images/70c61f26b2d68c5bae0667bf5a51380130f578ad4b5143a8d610a63932833c06.jpg)

![](/api/attachments/HXHTWTF6/fulltext/images/bf5bad913f6e251f970c2ddfa3298b329f891d202eeedbe664f3f5a58287c3d7.jpg)

![](/api/attachments/HXHTWTF6/fulltext/images/d3562d1d56dc4204e54289c28cc7b2e2522331c6738b1492963a324f7897ace3.jpg)

![](/api/attachments/HXHTWTF6/fulltext/images/a3d1ba04aff2019ee0d68346037cf680fcf966ff915b112bc5c5ca7a9a04fd10.jpg)

![](/api/attachments/HXHTWTF6/fulltext/images/9fd0564209717c8ed22bfaf3c52460da865edc742becb86a00df1ed77c94907e.jpg)  
Figure 8. Marginal Effects of Enhancing Response Preference on Market Outcomes

## 6 Discussion and Conclusion

This study developed a data-driven DASAM to assess the interaction between providers’ review intervention strategies, including positive review incentives, overstatement, managerial response, and consumer review behavior in egoistic, altruistic, and hybrid markets. Our analysis reveals the varying effects of review interventions on providers’ decisions, social welfare, and stakeholder benefits. Table 9 presents an overview of the study’s key contributions and implications. The following sections summarize these findings.

## 6.1 Contributions to Research

The findings improve our macrolevel understanding of providers’ behavior and its outcomes across different markets. Prior research has extensively examined the effects of the entry of peer-to-peer platforms, such as Airbnb, on the traditional local hotel industry (Blal et al., 2018; Li & Srinivasan, 2019). However, researchers have focused on market share fragmentation (Dogru et al., 2019), hotel sales performance (Blal et al., 2018), and pricing strategies (Roma et al., 2019; Zervas et al., 2017). The broad view of providers’ other behaviors has not been examined. The present study explores how providers behaviors related to review interventions and pricing quality decisions differ across various types of competitive markets. This work pays added attention to hybrid markets, which consist of homestay hosts and hotel operators, compared with egoistic markets and altruistic markets. As also observed by Zervas et al. (2017), homestay hosts (modeled as partial altruists in this study) create market-wide benefits. Consequently, egoistic competitors are driven to engage in consumerfriendly practices in response to reputation pressures and price-quality competition. Conversely, altruistic providers may moderate their altruism when they compete against egoistic providers. Our results indicate that egoistic providers engage in greater service exaggeration and offer fewer positive review incentives than altruistic providers because they prioritize short-term consumer acquisition over reputation-building costs.

Furthermore, this work elucidates the intermediary mechanisms through which review interventions influence review reputation and providers’ competitive performance. First, unlike prior research, which established that only low-level positive review incentives optimize a business’s outcomes (Wu et al., 2023), our study elaborates on the consequences of nonoptimal decision-making. Providers typically increase incentives while diminishing their services’ pricequality attractiveness to offset costs. However, this approach suppresses consumer purchases, even as the providers’ review reputation increases because of positive review incentives. Market-level analysis shows that increasing average incentives can reduce the total provider revenues. Therefore, the negative spillover effects on competing providers’ revenues outweigh the benefits to focal providers. This effect justifies why platforms should strictly prohibit providers from offering incentives to customers’ positive reviews.

Second, egoistic providers use overstatement to raise their revenue by increasing customer acquisition and optimizing unit profits through price-quality adjustments. However, the effectiveness of overstatement depends on the competitive context (Huang et al., 2021). Moderate overstatement works best for egoistic providers when they compete with similar providers. Meanwhile, providers can increase their profits by solely adopting aggressive overstatement when they compete with altruistic competitors. When altruistic providers adopt increased overstatement, they move toward egoistic behavior: Increased overstatement reduces the number of customers but substantially increases their profit per unit.

Table 9. Summary of Contributions to Research

<table><tr><td>Previous research</td><td>Literature gaps</td><td>Contributions</td></tr><tr><td>Effect of market entry by homestay providers on the sales performance of hotel providers (Blal et al., 2018; Zervas et al., 2017)</td><td>1. Limited exploration of the broader behavioral changes among providers resulting from shifts in market types.</td><td>1. This study examines how provider behaviors related to review interventions and pricing quality decisions differ across various types of competitive markets.</td></tr><tr><td>Effect of market entry by homestay providers on the pricing strategies of hotel providers (Li &amp; Srinivasan, 2019; Roma et al., 2019)</td><td rowspan="2">2. Insufficient investigation into the broad spillover effects caused by shifts in market types.</td><td rowspan="2">2. This study focuses on the effect of review intervention strategies by examining how the marginal effects of different review intervention behaviors on stakeholder benefits vary across different market types.</td></tr><tr><td>Effect of market entry by homestay providers on market share fragmentation among hotel providers (Dogru et al., 2019)</td></tr><tr><td>Effect of cashback strategies on consumer surplus and social welfare in the presence of strategic consumers (Wu et al., 2023)</td><td rowspan="3">Limited discussion on the intermediary mechanisms by which different types of review interventions affect review and revenue.</td><td rowspan="3">This study developed a data-driven agent-based model to deconstruct micro-interactions, thereby identifying the evolutionary mechanisms through which review interventions influence the benefits for stakeholders over time.</td></tr><tr><td>Proactive engagement in responses enhances guest satisfaction and increases sales (Liu et al., 2023; Lui et al., 2018)</td></tr><tr><td>Managerial responses positively influence the quantity of subsequent customer reviews (Chen et al., 2019)</td></tr><tr><td>Research on positive review incentives (Wu et al., 2023), research on managerial response (Chen et al., 2019), and research on overstatement (Zhang et al., 2023)</td><td>Limited to an analysis of the effects of a single review intervention, lacking discussion on the covariance relationships between different review intervention strategies.</td><td>This study treats providers&#x27; positive review incentives and overstatement decisions as endogenous, thus enabling providers to consider the effects of various review interventions comprehensively when making decisions. In turn, the exploration of the interconnections between review intervention behaviors is facilitated.</td></tr></table>

Finally, regarding managerial responses, prior research has demonstrated that proactive managerial responses improve guest satisfaction and sales (Liu et al., 2023), enhance online reviews (Chen et al., 2019), and boost competitive performance (Lui et al., 2018). Our findings confirm that egoistic providers’ effective responses to negative reviews can enhance their competitive performance. However, previous studies have not considered the relationship between managerial responses and price-quality decisions. We demonstrate that managerial responses can reflect not only the providers’ characteristics (Yhee et al., 2023) but also the consumer friendliness of their price-quality decisions. Our analysis of the intermediary mechanisms shows a decline in positive review incentives because managerial responses lead to cost savings, which ultimately feed back into price-quality decisions.

This study also contributes to the literature on review intervention strategies by analyzing the covariant relationships between different review interventions. Prior research has focused on the isolated effects of single interventions (Chen et al., 2019; Wu et al., 2023). By contrast, our analysis focuses on how these behaviors interact with each other and with price-quality decisions. Unlike traditional ABM approaches, which manipulate variables of interest to examine their effect on outcomes (Haki et al., 2024), our model endogenizes the providers’ positive review incentives and overstatement decisions. This information can help providers in considering the effects of various review interventions comprehensively during decision-making. This approach replicates real-world decision-making scenarios. Review intervention behaviors exhibit the following covariant relationships. Positive review incentives and overstatement are typically complementary. When platforms prohibit incentives, providers compensate with disproportionately increased overstatement. This nonlinear relationship indicates the need for platforms to scrutinize the unintended consequences of strict incentive bans.

Enhancing responses to negative reviews have a substitution effect with positive review incentives (Liu et al., 2019a); however, it is complementary with overstatement. Meanwhile, altruistic providers generally do not increase both strategies simultaneously. When providers focus on enhancing responses, their overstatement levels typically increase (except for altruistic providers), whereas positive incentives decrease.

Paradoxically, providers who strongly prefer enhancing responses to negative reviews will likely experience a decrease in consumers’ review perception. This counterintuitive result can be attributed to two factors. First, increased overstatement creates expectation-reality gaps. Second, reduced positive review incentives generate fewer value cocreation reviews.

Finally, platforms are increasingly changing their market types to diversify services and boost transaction volumes (Blal et al., 2018). However, additional exploration is needed to understand the broad implications of such an action. The entry of homestay hosts into the industry has produced complex effects that go beyond simply increasing supply (Li & Srinivasan, 2019). This study examines how market transformation influences the marginal effects of review intervention. It shows that transitioning to hybrid markets protects providers against the negative impacts of positive review incentives on consumer satisfaction at all incentive levels. Furthermore, even a low level of overstatement can reduce consumer benefits and satisfaction in hybrid markets. Therefore, these settings require strict regulations against false advertising. Finally, enhancing responses to negative reviews appear to have the strongest positive effect on consumer average benefits, satisfaction, and overall social welfare in hybrid markets.

## 6.2 Theoretical Implications

This study offers several theoretical implications. First, it contributes to the literature on review interventions by adopting a complex systems perspective. This view helps to examine how various review intervention strategies function on shared accommodation platforms. Empirical testing and game theory have been used in prior research to examine specific interventions (Burtch et al., 2018; Chen et al., 2019; Le & Ha, 2021; Sheng et al., 2021; Wu et al., 2023). However, these approaches have been unable to fully capture the platform’s inherent complexity, including supply-demand randomness, multivariate provider decisions, and agent heterogeneity (Malgonde et al., 2020). These interactions, which are rooted in microlevel behaviors, evolve into nonlinear dynamics that influence individual and market-level outcomes. This study used a data-driven agent-based model to simulate these complex operational processes. Then, it analyzed the distinct effects of review interventions at the individual and collective levels. The model clarifies the behavioral mechanisms and intermediary processes through which review interventions influence participants’ benefits. Furthermore, we also validate this for practical application in bridging theory and practice. Unlike prior studies focusing on single strategies, this research simultaneously investigated three intervention strategies. Moreover, this work emphasizes the covariant relationships of these interventions. Positive review incentives, which are common but under-researched in previous studies (Wu et al., 2023), have a complementary relationship with overstatement in boosting provider benefits. Meanwhile, they have a substitution relationship with enhancing responses. Additionally, overstatement and enhancing responses have a complementary relationship. This study reveals potential nonlinear shifts within these relationships, and also finds that providers tend to exaggerate more when they do not use low-level positive review incentives than when they do. Therefore, analyzing review interventions from a bottom-up perspective of complex systems is valuable because it provides a holistic understanding of these strategies.

Second, this study expands the use of value cocreation theory by applying it to online review management and online review interactions. Traditional value cocreation theory posits that providers and consumers in the sharing economy cocreate experiential value by interacting with one another directly (Camilleri & Neuhofer, 2017). This work broadens the scope of this theory by demonstrating how online review systems extend these value interactions beyond the immediate experience to postexperience review interactions. This study augments the existing research that examines consumer participation in service improvement through reviews (Zhang et al., 2021). Specifically, it explores two additional dimensions of value cocreation in online review interactions. Consumers indirectly influence the booking decisions of potential consumers, thereby affecting perceived value. Providers actively engage in review responses, which directly affects the current consumer’s value state and signals a positive environment to future consumers. In turn, this scenario shapes future consumers’ behavior. From this perspective, we enlarge the typology of online reviews by distinguishing different value states (i.e., value cocreation, review-side value decline, response-side value decline, and value co-destruction), thereby encapsulating how reviews affect authors and potential consumers. This classification, which is based on value cocreation theory, reveals the processes through which management responses influence value, and provides an improved understanding of review-response dynamics within this framework.

Third, this study expands the scope of research on review interventions by incorporating a range of platform market structures. As such, this work extends beyond previous studies focusing only on egoistic providers. Integrating partially altruistic providers allows homestay host behavior to be represented accurately. It also shows how intervention outcomes vary across market types (Medina-Hernandez et al., 2021). Platforms are increasingly beginning to view hotel and homestay providers as partners. Therefore, understanding how review interventions work across these markets can guide adaptive policy formulation. The findings suggest that shifting from an egoistic market to a hybrid one can alleviate the negative effects of positive review incentives on consumer satisfaction. Simultaneously, this shift can augment the welfare benefits of enhancing responses. The study also highlights how the marginal effects of review interventions vary across markets and intervention levels, thus allowing us to perceive the potential spillover effects in market transitions.

## 6.3 Practical Implications

The findings provide platform stakeholders with actionable insights that can help them adjust their behaviors to respond to intervention dynamics. Such insights allow platform operators across different market types to develop targeted, evidence-based policies that address certain challenges while maximizing new opportunities.

This study has several implications for consumers. First, while altruistic markets may deliver the greatest benefits, their availability is limited. Thus, hybrid markets are a practical alternative. Competitive pressures in such markets force even egoistic providers to employ more consumer-friendly practices than they would in purely egoistic markets. Second, policies that strictly prohibit positive review incentives may drive providers to exaggerate their claims about their products and services. Therefore, consumers should remain alert to any potential information asymmetry on such platforms. Third, a provider’s preference for enhancing responses to negative reviews may reliably indicate consumerfriendly decision-making. Thus, it guides consumers to select providers who respond constructively to negative feedback to enhance their experience.

Review interventions are effective only when they are applied in the correct competitive context. Therefore, providers must strategically adapt their approaches on the basis of market dynamics because egoistic providers who are competing with fellow egoistic providers can increase their profits effectively by applying only low levels of overstatement. However, they can only increase profits by employing high levels of overstatement when competing with altruistic providers. Providers should also calibrate their positive review incentives because only low or moderately low levels are likely to attract more consumers and maximize profits.

This study offers platform operators crucial insights into review intervention policies. First, according to marketlevel analysis, positive review incentives reduce overall provider profits and consumer satisfaction. This finding justifies why such incentives should be prohibited. However, platforms must simultaneously strengthen their monitoring of providers’ overstatement, which tends to occur on a large scale after incentives are banned. Moreover, overstatement consistently diminishes social welfare and consumer benefits across all market types.

Although reviews may aid in mitigating information asymmetry to some extent, platforms should enforce strict regulations against overstatement. Finally, enhancing responses to negative reviews are the most suitable strategy because they have neutral or positive effects on social welfare and platform revenue. Based on the varied effects of this strategy across market types, platforms should (1) encourage providers to offer enhancing responses to negative reviews, which can boost consumer satisfaction, (2) incentivize responses in hybrid markets, and (3) consider the relative benefits for each participant group when deciding whether to encourage enhancing responses in altruistic markets.

## 6.4 Limitations and Future Research

This study has a number of limitations that should be taken into account. First, the proposed model employs a multi-objective genetic algorithm to simulate decisionmaking between two competing providers. Sophisticated models with a large provider base could be incorporated into future research to better capture complex market dynamics. Second, our analysis focuses on how a provider’s internal decisions covary when competitors adapt, but does not adequately explore the strategic relationships among providers. This work could be extended through the derivation of in-depth insights into competitive behavior to examine how providers influence one another’s strategies. Finally, future research could use artificial intelligence methods to investigate incentivized positive reviews and quantify the overstatement among providers. This approach could advance empirical research on review interventions.

## 6.5 Conclusion

This study develops a data-driven agent-based model called DASAM to simulate complex operations in shared accommodation platforms and examine the distinct effects of review interventions at the individual and collective levels. Simulations show that direct interventions (i.e., positive review incentives) and indirect interventions (i.e., managerial responses and overstatement) covary with price-quality decisions, thus having unintended consequences. Notably, prohibiting positive review incentives may unintentionally increase the provider’s overstatement, whereas enhancing responses to negative reviews may decrease the provider’s review reputation. The marginal effects of these interventions may be altered by shifting between market types, which can mitigate some of their negative outcomes.

## Acknowledgments

This work was supported in part by the National Natural Science Foundation of China (No. 72071031), the Major Project of National Social Science Fund of China (No. 22&ZD128), and the National Natural Science Foundation of Sichuan (No. 2024NSFSC0265).

## References

Ahmad, F., & Guzmán, F. (2021). Negative online reviews, brand equity and emotional contagion. European Journal of Marketing, 55(11), 2825- 2870.

An, M.-A., & Han, S.-L. (2020). Effects of experiential motivation and customer engagement on customer value creation: Analysis of psychological process in the experience-based retail environment. Journal of Business Research, 120, 389-397.

Antonio, N., de Almeida, A., & Nunes, L. (2019). Hotel booking demand datasets. Data in Brief, 22, 41- 49.

Becker, M., Wiegand, N., & Reinartz, W. J. (2019). Does it pay to be real? Understanding authenticity in TV advertising. Journal of Marketing, 83(1), 24-50.

Benbya, H., Nan, N., Tanriverdi, H., & Yoo, Y. (2020). Complexity and information systems research in the emerging digital world. MIS Quarterly, 44(1), 1-17.

Blal, I., Singal, M., & Templin, J. (2018). Airbnb’s effect on hotel sales growth. International Journal of Hospitality Management, 73, 85-92.

Burtch, G., Hong, Y. L., Bapna, R., & Griskevicius, V. (2018). Stimulating online reviews by combining financial incentives and social norms. Management Science, 64(5), 2065-2082.

Camilleri, J., & Neuhofer, B. (2017). Value co-creation and co-destruction in the Airbnb sharing economy. International Journal of Contemporary Hospitality Management, 29(9), 2322-2340.

Candi, M., & Kahn, K. B. (2016). Functional, emotional, and social benefits of new B2B services. Industrial Marketing Management, 57, 177-184.

Carley, K. M. (2002). Computational organizational science and organizational engineering. Simulation Modelling Practice and Theory, 10(5- 7), 253-269.

Chen, W., Gu, B., Ye, Q., & Zhu, K. X. (2019). Measuring and managing the externality of managerial responses to online customer reviews. Information Systems Research, 30(1), 81-96.

Chen, Y., & Xie, J. (2008). Online consumer review: Word-of-mouth as a new element of marketing communication mix. Management science, 54(3), 477-491.

Danatzis, I., Möller-Herm, J., & Herm, S. (2024). Curbing customer-to-customer misbehavior contagion in the sharing economy. Journal of Business Research, 173, Article 114460.

Deb, K., Pratap, A., Agarwal, S., & Meyarivan, T. (2002). A fast and elitist multiobjective genetic algorithm: NSGA-II. IEEE Transactions on Evolutionary Computation, 6(2), 182-197.

Dogru, T., Mody, M., & Suess, C. (2019). Adding evidence to the debate: Quantifying Airbnb’s disruptive impact on ten key hotel markets. Tourism Management, 72, 27-38.

Dolan, R., Seo, Y., & Kemper, J. (2019). Complaining practices on social media in tourism: A value cocreation and co-destruction perspective. Tourism Management, 73, 35-45.

Dong, J. (2022). Using simulation in information systems research. Journal of the Association for Information Systems, 23(2), 408-417.

Dong, J. Q. (2019). Numerical data quality in simulation research: A reflection and epistemic implications. Decision Support Systems, 126, Article 113134.

Dong, J. Q. (2021). Technological choices under uncertainty: Does organizational aspiration matter? Strategic Management Journal, 42(5), 898-916.

Epstein, J. M., & Axtell, R. (1996). Growing artificial societies: Social science from the bottom up. Brookings Institution Press.

Esmark Jones, C. L., Stevens, J. L., Breazeale, M., & Spaid, B. I. (2018). Tell it like it is: The effects of differing responses to negative online reviews. Psychology & Marketing, 35(12), 891-901.

Fioretti, G. (2013). Agent-based simulation models in organization science. Organizational Research Methods, 16(2), 227-242.

Fradkin, A., & Holtz, D. (2023). Do incentives to review help the market? Evidence from a field experiment on Airbnb. Marketing Science, 42(5), 853-865.

Friedman, J. W. (1971). A non-cooperative equilibrium for supergames. The Review of Economic Studies, 38(1), 1-12.

Gu, B., & Ye, Q. (2014). First step in social media: Measuring the influence of online management responses on customer satisfaction. Production and Operations Management, 23(4), 570-582.

Guo, Y. H., Zhang, Y., Boulaksil, Y., Qian, Y. G., & Allaoui, H. (2023). Modelling and analysis of online ride-sharing platforms: A sustainability perspective. European Journal of Operational Research, 304(2), 577-595.

Haki, K., Tanriverdi, H., Safaei, D., Schmid, M., Aier, S., & Winter, R. (2024). Generativity and profitability on B2B innovation platforms: A simulation-based theory development. MIS Quarterly, 48(2), 583- 612.

Hannah, D. P., Tidhar, R., & Eisenhardt, K. M. (2021). Analytic models in strategy, organizations, and management research: A guide for consumers. Strategic Management Journal, 42(2), 329-360.

Harrison, J. R., Lin, Z., Carroll, G. R., & Carley, K. M. (2007). Simulation modeling in organizational and management research. Academy of Management Review, 32(4), 1229-1245.

He, Z., Xiong, J., Ng, T. S., Fan, B., & Shoemaker, C. A. (2017). Managing competitive municipal solid waste treatment systems: An agent-based approach. European Journal of Operational Research, 263(3), 1063-1077.

Heath, B., Hill, R., & Ciarallo, F. (2009). A survey of agent-based modeling practices (January 1998 to July 2008). JASSS—The Journal of Artificial Societies and Social Simulation, 12(4), 1-9.

Ho, Y.-C., Wu, J., & Tan, Y. (2017). Disconfirmation effect on online rating behavior: A structural model. Information Systems Research, 28(3), 626- 642.

Hu, S., Blettner, D., & Bettis, R. A. (2011). Adaptive aspirations: Performance consequences of risk preferences at extremes and alternative reference groups. Strategic Management Journal, 32(13), 1426-1436.

Huang, Y. L., Jin, Y., & Huang, J. H. (2021). Impact of managerial responses on product sales: Examining the moderating role of competitive intensity and market position. Journal of the Association for Information Systems, 22(2), 544- 570.

Jiang, G. Y., Shang, J., Liu, W. P., Feng, X. D., & Lei, J. L. (2020). Modeling the dynamics of online review life cycle: Role of social and economic moderations. European Journal of Operational Research, 285(1), 360-379.

Karaman, H. (2021). Online review solicitations reduce extremity bias in online review distributions and increase their representativeness. Management Science, 67(7), 4420-4445.

Khern-am-nuai, W., Kannan, K., & Ghasemkhani, H. (2018). Extrinsic versus intrinsic rewards for contributing reviews in an online platform. Information Systems Research, 29(4), 871-892.

Kim, D., Park, S.-P., & Yi, S. (2021). Relevant and rich interactivity under uncertainty: Guest reviews, host responses, and guest purchase intention on Airbnb. Telematics and Informatics, 65, Article 101708.

Krebs, D. L. (1991). Altruism and egoism: A false dichotomy? Psychological Inquiry, 2(2), 137-139.

Le, L. H., & Ha, Q.-A. (2021). Effects of negative reviews and managerial responses on consumer attitude and subsequent purchase behavior: An experimental design. Computers in Human Behavior, 124, 106912.

Lee, S. Y., Qiu, L., & Whinston, A. (2018). Sentiment manipulation in online platforms: An analysis of movie tweets. Production and Operations Management, 27(3), 393-416.

Li, H., & Srinivasan, K. (2019). Competitive dynamics in the sharing economy: An analysis in the context of Airbnb and hotels. Marketing Science, 38(3), 365- 391.

Li, J., Dong, W., & Ren, J. (2024). The effects of user- and marketer-generated content on customer satisfaction: A textual analysis approach. Electronic Commerce Research and Applications, 65, Article 101407.

Li, X. T., & Wu, L. (2018). Herding and social media word-of-mouth: Evidence from Groupon. MIS Quarterly, 42(4), 1331-1351.

Liang, S., Schuckert, M., Law, R., & Chen, C. C. (2020). The importance of marketer-generated content to peer-to-peer property rental platforms: Evidence from Airbnb. International Journal of Hospitality Management, 84, Article 102329.

Liu, H. F., Jayawardhena, C., Dibb, S., & Ranaweera, C. (2019a). Examining the trade-off between compensation and promptness in EWOMtriggered service recovery: A restorative justice perspective. Tourism Management, 75, 381-392.

Liu, J., Xie, K. L., Chen, W., Liu, Y., & Sun, Y. (2023). How incumbents beat disruption? Evidence from hotel responses to home sharing. Production and Operations Management, 32(9), 2758-2774.

Liu, L., Zhao, L., & Ren, X. (2019b). Optimal preservation technology investment and pricing policy for fresh food. Computers & Industrial Engineering, 135, 746-756.

Liu, S., Wang, N., Gao, B., & Gallivan, M. (2021). To be similar or to be different? The effect of hotel managers' rote response on subsequent reviews. Tourism Management, 86, Article 104346.

Liu, X., Han, M., Liu, J., & Zhang, Z. (2024). Smart users: Effort management in earning rewards. Annals of Tourism Research, 108, Article 103802.

Lui, T.-W., Bartosiak, M., Piccoli, G., & Sadhya, V. (2018). Online review response strategy and its effects on competitive performance. Tourism Management, 67, 180-190.

Lv, J. C., Bi, G. B., & Xu, Y. (2023). Crowdfunding pricing and quality overstatement in the presence

of platform regulation. Journal of Retailing and Consumer Services, 70, Article 103179.

Ma, Y., Yao, Z., Zhang, J., & Tang, P. (2024). Unveiling the impacts of performance-contingent incentivized reviews on subsequent supplementary reviews. Information Processing & Management, 61(3), Article 103692.

Maglio, P. P., & Spohrer, J. (2008). Fundamentals of service science. Journal of the Academy of Marketing Science, 36, 18-20.

Malgonde, O., Zhang, H., Padmanabhan, B., & Limayem, M. (2020). Taming complexity in search matching: Two-sided recommender systems on digital platforms. MIS Quarterly, 44(1), 49-84.

Medina-Hernandez, V. C., Ferrer-Rosell, B., & Marine-Roig, E. (2021). Value co-creation in non-profit accommodation platforms. Frontiers in Psychology, 12, Article 763211.

Nazifi, A., Roschk, H., Ordenes, F. V., & Marder, B. (2022). Bad intentions: Customers’ negative reactions to intentional failures and mitigating conditions. Journal of Travel Research, 61(8), 1808-1827.

Oliver, R. L. (1980). A cognitive model of the antecedents and consequences of satisfaction decisions. Journal of Marketing Research, 17(4), 460-469.

Park, S., Shin, W., & Xie, J. (2023). Disclosure in incentivized reviews: Does it protect consumers? Management Science, 69(11), 7009-7021.

Perren, R., & Kozinets, R. V. (2018). Lateral exchange markets: How social platforms operate in a networked economy. Journal of Marketing, 82(1), 20-36.

Proserpio, D., & Zervas, G. (2017). Online reputation management: Estimating the impact of management responses on consumer reviews. Marketing Science, 36(5), 645-665.

Roma, P., Panniello, U., & Lo Nigro, G. (2019). Sharing economy and incumbents' pricing strategy: The impact of Airbnb on the hospitality industry. International Journal of Production Economics, 214, 17-29.

Sargent, R. G. (2015). An introductory tutorial on verification and validation of simulation models. Proceedings of the Winter Simulation Conference (pp. 1729-1740).

Sheng, J., Wang, X. J., & Amankwah-Amoah, J. (2021). The value of firm engagement: How do ratings benefit from managerial responses? Decision Support Systems, 147, Article 113578.

Shmidt, M. (2020). Participants’ interaction with sharing economy platforms in Russia. Information

Technology & People, 33(3), 897-917.

Song, T. T., Huang, J. H., Tan, Y., & Yu, Y. F. (2019). Using user- and marketer-generated content for box office revenue prediction: Differences between microblogging and third-party platforms. Information Systems Research, 30(1), 191-203.

Sparks, B. A., So, K. K. F., & Bradley, G. L. (2016). Responding to negative online reviews: The effects of hotel responses on customer inferences of trust and concern. Tourism Management, 53, 74-85.

Statista. (2020). Trust in the source of information about a product when shopping online in Russia in 2020, by medium and federal district. Retrieved December 23, 2023, from https://www.statista. com/statistics/1177124/russia-trust-in-thesource-of-information-about-a-product-whileshopping/

Statista. (2021). Level of trust in crowd-sourced review websites by online users in the United States and the United Kingdom as of April 2021. Retrieved December 23, 2023, from https://www.statista. com/statistics/1243212/us-uk-trust-reviewwebsites/

Statista. (2023). Consumers’ trust in information sources in the United States as of February 2023. Retrieved December 23, 2023, from https://www.statista.com/statistics/1411395/cons umers-trust-information-sources-us

TripAdvisor. (2019). Online reviews remain a trusted source of information when booking trips, reveals new research. https://ir.tripadvisor.com/newsreleases/news-release-details/online-reviewsremain-trusted-source-information-whenbooking

Tsunoda, Y., & Zennyo, Y. (2021). Platform information transparency and effects on third-party suppliers and offline retailers. Production and Operations Management, 30(11), 4219-4235.

Ullah, R., Amblee, N., Kim, W., & Lee, H. (2016). From valence to emotions: Exploring the distribution of emotions in online product reviews. Decision Support Systems, 81, 41-53.

Uthaisar, S., Eves, A., & Wang, X. L. (2023). Tourists' online information search behavior: Combined user-generated and marketer-generated content in restaurant decision making. Journal of Travel Research, 63(6), 1549-1573.

Vargo, S. L., Maglio, P. P., & Akaka, M. A. (2008). On value and value co-creation: A service systems and service logic perspective. European Management Journal, 26(3), 145-152.

Wang, H., Du, R., Shen, W., Qiu, L., & Fan, W. (2022).

Product reviews: A benefit, a burden, or a trifle? How seller reputation affects the role of product reviews. MIS Quarterly, 46(2), 1243-1272.

Wang, S., Hu, Q., & Liu, W. (2017). Price and qualitybased competition and channel structure with consumer loyalty. European Journal of Operational Research, 262(2), 563-574.

Wang, Y., & Chaudhry, A. (2018). When and how managers' responses to online reviews affect subsequent reviews. Journal of Marketing Research, 55(2), 163-177.

Weathers, D., Sharma, S., & Wood, S. L. (2007). Effects of online communication practices on consumer perceptions of performance uncertainty for search and experience goods. Journal of Retailing, 83(4), 393-401.

Wei, X., Zhang, Y., & Luo, X. (2024). Modeling the evolution of collective overreaction in dynamic online product diffusion networks. Decision Support Systems, 181, Article 114232.

Wei, X., Zhang, Y., Luo, X. R., Pan, G., & Nie, G. (2023). Qualitative cusp catastrophe multi-agent simulation model to explore abrupt changes in online impulsive buying behavior. Journal of the Association for Information Systems, 25(2), 304- 340.

Wu, P., Ngai, E. W. T., & Wu, Y. (2023). Impact of praise cashback strategy: Implications for consumers and e-businesses. Production and Operations Management, 32(9), 2825-2845.

Xu, Q. (2014). Should I trust him? The effects of reviewer profile characteristics on EWOM credibility. Computers in Human Behavior, 33, 136-144.

Yhee, Y., Kim, H., Kim, J., & Koo, C. (2023). Trust in

managerial response offsets negative review. Annals of Tourism Research, 102, Article 103641.

Yin, D. Z., Mitra, S., & Zhang, H. (2016). When do consumers value positive vs. Negative reviews? An empirical investigation of confirmation bias in online word of mouth. Information Systems Research, 27(1), 131-144.

Yu, S.-m., Fan, Y., Zhu, L., & Eichhammer, W. (2020). Modeling the emission trading scheme from an agent-based perspective: System dynamics emerging from firms’ coordination among abatement options. European Journal of Operational Research, 286(3), 1113-1128.

Zervas, G., Proserpio, D., & Byers, J. W. (2017). The rise of the sharing economy: Estimating the impact of Airbnb on the hotel industry. Journal of Marketing Research, 54(5), 687-705.

Zhang, M., Fan, B., Zhang, N., Wang, W., & Fan, W. (2021). Mining product innovation ideas from online reviews. Information Processing & Management, 58(1), Article 102389.

Zhang, Y., Gao, J., Bilgihan, A., & Lorenz, M. (2023). A holistic assessment of EWOM management effectiveness with agent-based modeling. International Journal of Contemporary Hospitality Management, 35(3), 785-827.

Zhou, J., Zhao, R., & Wang, W. (2019). Pricing decision of a manufacturer in a dual-channel supply chain with asymmetric information. European Journal of Operational Research, 278(3), 809-820.

Zhu, F., & Xiaoquan, Z. (2010). Impact of online consumer reviews on sales: The moderating role of product and consumer characteristics. Journal of Marketing, 74(2), 133-148.

## Appendix

## A1. Parameter Setting Derived from Real Data

## A1.1. Fitting of Arrivals and Room Nights

To validate DASAM, we sourced empirical data from a hotel booking dataset containing 119,390 reservation records from two hotels in Portugal, spanning from July 1, 2015, to August 31, 2017 (Antonio et al., 2019). These data provided insights into probability distributions for stay duration and daily arrivals. Many parameters must be fixed for simulation models. This study did not focus on consumer arrival distributions or stay durations, so these parameters were derived from this dataset to minimize their potential influence on the results.<sup>7</sup> We used frequency counting to obtain the distribution of consumer stay durations, as shown in Table A1.

Table A1. Distribution of Consumer Length of Stay

<table><tr><td>Length of accommodation (day)</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td></tr><tr><td>Probability</td><td>.1797</td><td>.2364</td><td>.2315</td><td>.1486</td><td>.0666</td><td>.0330</td><td>.0740</td><td>.0099</td><td>.0072</td><td>.0097</td><td>.0034</td></tr></table>

To determine daily consumer arrivals and the corresponding number of rooms,<sup>8</sup> we conducted a frequency analysis of daily check-ins followed by distribution fitting. As shown in Figure A1, a t-distribution minimizes the sum of squared errors, with a degree of freedom of 26.61, a location parameter of 93.55, and a scale parameter of 32.99. The fitting result does not reject the Kolmogorov-Smirnov test null hypothesis (p = 0.197). Daily consumer arrivals on the platform were then modeled to follow a Poisson distribution, whereas the actual number of consumers staying, constrained by room availability, was assumed to follow the fitted t-distribution.<sup>9</sup>

![](/api/attachments/HXHTWTF6/fulltext/images/b8e72c1521545be90e15358f349772b6ebd72afe0c36d0155f31252ccd908b54.jpg)  
Figure A1. Fitting the Distribution of Daily Occupancy

We implemented a heuristic algorithm to simulate consumer arrival and departure processes. This algorithm treats the number of provided rooms and the Poisson distribution parameter as decision variables. It embeds consumer arrival, check-in, and departure dynamics, minimizing the sum of squared errors between the real occupancy data (fitted with a t-distribution) and the simulated occupancy distributions. The results indicate that actual consumer arrivals followed a Poisson distribution with a parameter of 93.8, and the total number of rooms available was set to 340.

## A1.2. Provider Response Preferences and Effects of Different Reviews

We gathered data from 12,173 Airbnb listings in China, covering 519,176 online reviews and 115,413 managerial responses from January 2018 to December 2019. This dataset enabled us to investigate provider response patterns and the influence of different review types on potential consumers’ purchase intentions. Using deep learning techniques, we classified the sentiment polarity of reviews and responses into positive reviews, negative reviews, enhancing responses, and destructive responses. As detailed in Section 3.2.1 and illustrated in Figure 2, we constructed a panel dataset with 80,663 observations to track the cumulative and monthly increase of each review type. We used the monthly increase in reviews as a proxy for purchase volume. A fixed-effects regression was employed to assess how the cumulative number of each review type influences consumers’ purchase intentions. The key findings include:

1. Providers more frequently addressed negative reviews, with response probabilities of 0.198 for positive reviews and 0.378 for negative reviews.

2. Enhancing responses were more common for positive reviews, with probabilities of 0.939 $( S D = 0 . 1 9 2 )$ for positive reviews and 0.498 (SD = 0.464) for negative reviews.

3. Positive reviews without responses positively influenced purchase intentions $( b ^ { ( 1 ) } = 0 . 1 1 )$ , whereas unanswered negative reviews had a detrimental effect $( b ^ { ( 2 ) } = - 0 . 1 5 )$

4. Reviews that signal value co-creation significantly boosted purchase intentions $( b ^ { ( 3 ) } = 0 . 1 7 )$ , whereas reviews indicating value decline had no significant effect $( b ^ { ( 4 ) } = b ^ { ( 5 ) } = 0 )$ . The most pronounced negative effect arose from value-destructive reviews $( b ^ { ( 6 ) } = - 0 . 2 3 )$

## A2. Output Validation

Simulated providers were matched with real-world counterparts based on their response probabilities, response preferences, and proportions of positive reviews. Table A2 presents the comparison of review proportions for the top 100, 10, and 5 real providers that most closely match the simulated providers. The results demonstrate consistent review proportions between the simulated and real providers. The absolute review proportions of the top five real providers align closely with those of the simulated providers. This consistency indicates that DASAM effectively captures the dynamics of review responses between supply and demand

Table A2. Comparison of Simulated Proportions of Different Review Types With Real-World Data

<table><tr><td></td><td>Variable</td><td>Top 100 matches</td><td>Top 10 matches</td><td>Top 5 matches</td><td>Simulated providers</td></tr><tr><td rowspan="5">Matching variables</td><td>Response probability for positive reviews  $\gamma p$ </td><td>.149</td><td>.218</td><td>.190</td><td>.198</td></tr><tr><td>Response probability for negative reviews  $\gamma n$ </td><td>.468</td><td>.389</td><td>.384</td><td>.378</td></tr><tr><td>Response preference for positive reviews  $\delta p$ </td><td>.967</td><td>.995</td><td>1.000</td><td>.939</td></tr><tr><td>Response preference for negative reviews  $\delta n$ </td><td>.495</td><td>.500</td><td>.500</td><td>.500</td></tr><tr><td>Proportion of positive reviews</td><td>.909</td><td>.874</td><td>.840</td><td>.820</td></tr><tr><td rowspan="6">Output validation</td><td>Positive reviews without response</td><td>.777</td><td>.685</td><td>.681</td><td>.657</td></tr><tr><td>Negative reviews without response</td><td>.048</td><td>.076</td><td>.098</td><td>.112</td></tr><tr><td>Value co-creation</td><td>.131</td><td>.190</td><td>.159</td><td>.152</td></tr><tr><td>Value decline at response side</td><td>.020</td><td>.024</td><td>.031</td><td>.034</td></tr><tr><td>Value decline at review side</td><td>.005</td><td>.001</td><td>.000</td><td>.010</td></tr><tr><td>Value co-destruction</td><td>.020</td><td>.024</td><td>.031</td><td>.034</td></tr><tr><td colspan="6">Bolded values indicate those closest to the simulated results across different matching sample sizes.</td></tr></table>

We selected the top 100 real providers whose review proportions closely matched those of the simulated providers as our comparison group. Owing to tailing effects in the price decisions of real providers—potentially influenced by factors such as brand and room type—we applied two methods to address these variations: (1) taking the logarithm of prices and (2) using the top 80% of price values in the matching sample. After normalizing prices across datasets, we conducted kernel density estimation on the two distributions. The results, presented in Figure A2, show that the distribution of price decisions made by providers in the simulation system aligns with those of real providers with similar review characteristics. The Kolmogorov-Smirnov test results indicate no significant differences between the two distributions $( p _ { I } = 0 . 3 8 ; p _ { 2 } = 0 . 3 3 )$ . Thus, the proposed simulation model offers valuable insights for understanding the complex interactive behaviors of bilateral entities on shared accommodation platforms.

![](/api/attachments/HXHTWTF6/fulltext/images/6572ad41c282ea8b678b04e44194be2bfc737b494d8b129a38750f59d6a6316f.jpg)

![](/api/attachments/HXHTWTF6/fulltext/images/710945816c1cf60d15aa891091eb9795d578c2411f068a8e0b62afc7f83f5053.jpg)  
Figure A2. Comparison of Simulation Outcomes With Real-World Data

We further compared simulation outputs with findings from prior studies on online reviews and managerial responses. Specifically, we analyzed the effect of positive and negative reviews, along with different managerial response types, on current sales. The results (Table A3) demonstrate that positive reviews increased sales, whereas negative reviews decreased sales. Enhancing responses boosted sales, whereas destructive responses reduced sales, in line with previous research findings (Ahmad & Guzmán, 2021; Le & Ha, 2021; Zhu & Xiaoquan, 2010).

Table A3. Effect of Different Types of Reviews and Responses on Provider Performance

<table><tr><td>Variable</td><td>Provider&#x27;s sales volume</td><td>Provider&#x27;s revenue</td></tr><tr><td>Cumulative positive reviews</td><td>.032 [.025, .041]</td><td>.026 [.018, .035]</td></tr><tr><td>Cumulative negative reviews</td><td>-.032 [-.041, -.024]</td><td>-.027 [-.036, -.017]</td></tr><tr><td>Cumulative enhancing responses</td><td>.018 [.013, .024]</td><td>.016 [.010, .023]</td></tr><tr><td>Cumulative destructive responses</td><td>-.016 [-.023, -.010]</td><td>-.017 [-.024, -.010]</td></tr><tr><td>Price</td><td>-1.216 [-1.226, -1.206]</td><td>-.993 [-1.002, -.985]</td></tr><tr><td>Service quality</td><td>1.141 [1.130, 1.151]</td><td>.719 [.710, .728]</td></tr><tr><td>Competitor&#x27;s price</td><td>.410 [.404, .417]</td><td>.531 [.523, .539]</td></tr><tr><td>Competitor&#x27;s service quality</td><td>-.368 [-.374, -.361]</td><td>-.468 [-.477, -.460]</td></tr></table>

Note: Owing to high collinearity between the number of reviews and responses, as well as between price and service quality, we applied partial least squares (PLS) regression to evaluate the effect of reviews and responses on provider performance. The number of PLS components was set to $5 ,$ determined by minimizing the Akaike information criterion and Bayesian information criterion. The significance of the coefficients was assessed using the bootstrap method (B = 1000), with 95% confidence intervals shown in brackets.

## A3. Paired-Sample T-Test Results of Provider Decisions in a Hybrid Market

Table A4 presents the supplementary material for Section 4.3.1.

Table A4. Paired-Sample T-Test Results of Provider Decisions in a $\mathbf { H } \mathbf { y }$ brid Market

<table><tr><td>Market type</td><td>Subject</td><td>Type</td><td> $\zeta_i$ </td><td> $\varepsilon_i$ </td><td> $P_i$ </td><td> $S_i$ </td></tr><tr><td rowspan="2">HB</td><td>provider1</td><td>egoism</td><td>.154(.089)</td><td>.076(.067)</td><td>.549(.215)</td><td>.258(.197)</td></tr><tr><td>provider2</td><td>altruism</td><td>.120(.089)</td><td>.140(.085)</td><td>.444(.267)</td><td>.186(.173)</td></tr><tr><td colspan="3">Paired-sample t-test</td><td>t=81.795p&lt;.001</td><td>t=-173.187p&lt;.001</td><td>t=87.870p&lt;.001</td><td>t=79.651p&lt;.001</td></tr><tr><td colspan="7">Note: Variable abbreviations: HB: hybrid market;  $\zeta_i$ : provider i&#x27;s overstatement degree;  $\varepsilon_i$ : provider i&#x27;s positive review incentives;  $P_i$ : provider i&#x27;s room price;  $S_i$ : provider i&#x27;s service quality.</td></tr></table>

## A4. Effect of Review Interventions on Individual-Level Benefits

Tables A5 and A6 present the supplementary material for Section 5.2.1.

Table A5. Effect of Review Interventions on Provider i’s Benefits

<table><tr><td>Market type</td><td>Subject</td><td>No use</td><td>Low</td><td>Moderately low</td><td>Middle</td><td>Moderately high</td><td>High</td><td>Change direction</td><td colspan="2">ANOVA</td></tr><tr><td rowspan="3">Egoistic provider in egoistic market</td><td> $\varepsilon_i$ </td><td>73.109</td><td>77.720</td><td>75.315</td><td>67.249</td><td>59.830</td><td>46.168</td><td>↗↘</td><td>F=428.859</td><td>p&lt;.001</td></tr><tr><td> $\zeta_i$ </td><td>66.519</td><td>69.300</td><td>70.341</td><td>70.334</td><td>70.328</td><td>71.731</td><td>↗</td><td>F=5.830</td><td>p&lt;.001</td></tr><tr><td> $\gamma n_i$ </td><td></td><td>68.658</td><td></td><td>70.314</td><td></td><td>71.308</td><td>↗</td><td>F=37.571</td><td>p&lt;.001</td></tr><tr><td rowspan="3">Egoistic provider in hybrid market</td><td> $\varepsilon_i$ </td><td>78.708</td><td>79.479</td><td>74.586</td><td>68.000</td><td>61.643</td><td>48.260</td><td>↗↘</td><td>F=307.472</td><td>p&lt;.001</td></tr><tr><td> $\zeta_i$ </td><td>71.135</td><td>68.652</td><td>69.887</td><td>71.113</td><td>69.924</td><td>74.899</td><td>↘↗</td><td>F=16.753</td><td>p&lt;.001</td></tr><tr><td> $\gamma n_i$ </td><td></td><td>70.955</td><td></td><td>71.275</td><td></td><td>72.281</td><td>↗</td><td>F=7.491</td><td>p&lt;.001</td></tr><tr><td rowspan="3">Altruistic provider in hybrid market</td><td> $\varepsilon_i$ </td><td>38.648</td><td>42.237</td><td>42.868</td><td>39.585</td><td>36.415</td><td>35.078</td><td>↗↘</td><td>F=24.001</td><td>p&lt;.001</td></tr><tr><td> $\zeta_i$ </td><td>34.937</td><td>37.910</td><td>39.654</td><td>40.238</td><td>40.188</td><td>39.077</td><td>↗</td><td>F=5.001</td><td>p&lt;.001</td></tr><tr><td> $\gamma n_i$ </td><td></td><td>40.287</td><td></td><td>39.158</td><td></td><td>36.778</td><td>↘</td><td>F=40.615</td><td>p&lt;.001</td></tr><tr><td rowspan="3">Altruistic provider in altruistic market</td><td> $\varepsilon_i$ </td><td>42.886</td><td>43.524</td><td>41.892</td><td>40.889</td><td>37.328</td><td>34.126</td><td>↗↘</td><td>F=84.037</td><td>p&lt;.001</td></tr><tr><td> $\zeta_i$ </td><td>32.914</td><td>34.679</td><td>38.409</td><td>40.858</td><td>42.887</td><td>45.340</td><td>↗</td><td>F=106.938</td><td>p&lt;.001</td></tr><tr><td> $\gamma n_i$ </td><td></td><td>40.847</td><td></td><td>39.591</td><td></td><td>36.348</td><td>↘</td><td>F=174.396</td><td>p&lt;.001</td></tr><tr><td colspan="11">Note: Variable abbreviations:  $\varepsilon_i$ : provider i&#x27;s positive review incentives;  $\zeta_i$ : provider i&#x27;s overstatement degree;  $\gamma n_i$ : provider i&#x27;s probability of</td></tr></table>

Note: Variable abbreviations: ?? : provider i’s positive review incentives; ?? : provider i’s overstatement degree; ???? : provider i’s probability of giving enhancing responses to negative reviews;

Table A6. Effect of Review Interventions on Consumers’ Average Benefits Associated with Provider i

<table><tr><td>Market type</td><td>Subject</td><td>No use</td><td>Low</td><td>Moderately low</td><td>Middle</td><td>Moderately high</td><td>High</td><td>Change direction</td><td colspan="2">ANOVA</td></tr><tr><td rowspan="3">Egoistic provider in egoistic market</td><td> $\varepsilon_i$ </td><td>.113</td><td>.091</td><td>.103</td><td>.128</td><td>.161</td><td>.218</td><td> $\searrow\neg$ </td><td>F=267.244</td><td>p&lt;.001</td></tr><tr><td> $\zeta_i$ </td><td>.141</td><td>.134</td><td>.123</td><td>.123</td><td>.119</td><td>.104</td><td> $\searrow$ </td><td>F=31.959</td><td>p&lt;.001</td></tr><tr><td> $\gamma n_i$ </td><td></td><td>.119</td><td></td><td>.120</td><td></td><td>.125</td><td> $\nearrow$ </td><td>F=13.755</td><td>p&lt;.001</td></tr><tr><td rowspan="3">Egoistic provider in hybrid market</td><td> $\varepsilon_i$ </td><td>.134</td><td>.104</td><td>.110</td><td>.135</td><td>.172</td><td>.252</td><td> $\searrow\neg$ </td><td>F=143.607</td><td>p&lt;.001</td></tr><tr><td> $\zeta_i$ </td><td>.147</td><td>.153</td><td>.146</td><td>.145</td><td>.122</td><td>.11</td><td> $\nearrow\neg$ </td><td>F=32.511</td><td>p&lt;.001</td></tr><tr><td> $\gamma n_i$ </td><td></td><td>.126</td><td></td><td>.133</td><td></td><td>.142</td><td> $\nearrow$ </td><td>F=32.724</td><td>p&lt;.001</td></tr><tr><td rowspan="3">Altruistic provider in hybrid market</td><td> $\varepsilon_i$ </td><td>.445</td><td>.425</td><td>.414</td><td>.439</td><td>.446</td><td>.459</td><td> $\searrow\neg$ </td><td>F=6.983</td><td>p&lt;.001</td></tr><tr><td> $\zeta_i$ </td><td>.465</td><td>.453</td><td>.447</td><td>.425</td><td>.418</td><td>.422</td><td> $\searrow$ </td><td>F=6.687</td><td>p&lt;.001</td></tr><tr><td> $\gamma n_i$ </td><td></td><td>.418</td><td></td><td>.437</td><td></td><td>.476</td><td> $\nearrow$ </td><td>F=109.162</td><td>p&lt;.001</td></tr><tr><td rowspan="3">Altruistic provider in altruistic market</td><td> $\varepsilon_i$ </td><td>.434</td><td>.414</td><td>.424</td><td>.415</td><td>.456</td><td>.467</td><td> $\searrow\neg$ </td><td>F=36.521</td><td>p&lt;.001</td></tr><tr><td> $\zeta_i$ </td><td>.482</td><td>.475</td><td>.459</td><td>.423</td><td>.403</td><td>.383</td><td> $\searrow$ </td><td>F=94.197</td><td>p&lt;.001</td></tr><tr><td> $\gamma n_i$ </td><td></td><td>.419</td><td></td><td>.436</td><td></td><td>.484</td><td> $\nearrow$ </td><td>F=362.658</td><td>p&lt;.001</td></tr><tr><td colspan="11">Note: Variable abbreviations:  $\varepsilon_i$ : provider i&#x27;s positive review incentives;  $\zeta_i$ : provider i&#x27;s overstatement degree;  $\gamma n_i$ : provider i&#x27;s probability of giving enhancing responses to negative reviews</td></tr></table>

## A5. Effect of Review Intervention Measures on Market Outcomes

Table A7 presents the effects of the average level of review interventions in the market on the market outcomes. These results correspond to the analysis discussed in Section 5.2.2 of the paper.

Table A7. Effect of Average Review Intervention Measures on Market Outcomes

<table><tr><td></td><td colspan="3"> $\widehat{\pi}$ </td><td colspan="3"> $\overline{\pi}_{C}$ </td><td colspan="3"> $\overline{\pi}_{CS}$ </td></tr><tr><td></td><td>EG</td><td>HB</td><td>AL</td><td>EG</td><td>HB</td><td>AL</td><td>EG</td><td>HB</td><td>AL</td></tr><tr><td>Intercept</td><td>71.743***</td><td>62.896***</td><td>-76.969***</td><td>.117***</td><td>-.047***</td><td>1.266***</td><td>.548***</td><td>-1.609</td><td>2.448***</td></tr><tr><td> $\varepsilon$ </td><td>-13.758***</td><td>—</td><td>—</td><td>.407***</td><td>-.181***</td><td>-.182***</td><td>-5.305***</td><td>-3.080***</td><td>-1.564***</td></tr><tr><td> $\varepsilon^{2}$ </td><td>-480.311***</td><td>-548.513***</td><td>-258.006***</td><td>-.252***</td><td>2.870***</td><td>1.418***</td><td>-8.565***</td><td>2.506*</td><td>3.068***</td></tr><tr><td> $\zeta$ </td><td>13.569***</td><td>116.236***</td><td>113.951***</td><td>-.340***</td><td>-.335***</td><td>-.198***</td><td>-13.193***</td><td>-7.730***</td><td>-5.457***</td></tr><tr><td> $\zeta^{2}$ </td><td>-74.094***</td><td>-161.005***</td><td>—</td><td>.635***</td><td>-.466***</td><td>-1.177***</td><td>25.217***</td><td>6.847***</td><td>2.435***</td></tr><tr><td> $\gamma n$ </td><td>6.299***</td><td>-7.697***</td><td>—</td><td>.009***</td><td>.114***</td><td>—</td><td>-.188***</td><td>.431***</td><td>-.059***</td></tr><tr><td> $\gamma n^{2}$ </td><td>—</td><td>—</td><td>2.582***</td><td>—</td><td>.016*</td><td>-.017***</td><td>—</td><td>—</td><td>—</td></tr><tr><td> $rp$ </td><td>5.115***</td><td>-17.239***</td><td>88.171***</td><td>-.006***</td><td>.376***</td><td>-.652***</td><td>-.845***</td><td>1.139***</td><td>-2.304***</td></tr><tr><td>TCA</td><td>.236***</td><td>.220***</td><td>.182***</td><td>—</td><td>0***</td><td>0***</td><td>-.001***</td><td>—</td><td>-.001***</td></tr><tr><td>Observations</td><td>178200</td><td>89100</td><td>178200</td><td>178200</td><td>89100</td><td>178200</td><td>178200</td><td>89100</td><td>178200</td></tr><tr><td> $R^{2}$ </td><td>.054</td><td>.072</td><td>.078</td><td>.049</td><td>.138</td><td>.092</td><td>.066</td><td>.104</td><td>.119</td></tr><tr><td>AIC</td><td>1.689e+06</td><td>8.834e+05</td><td>1.782e+06</td><td>-3.824e+05</td><td>-6.637e+04</td><td>-1.219e+05</td><td>-3.636e+05</td><td>-6.096e+04</td><td>-1.011e+05</td></tr><tr><td>BIC</td><td>1.689e+06</td><td>8.835e+05</td><td>1.782e+06</td><td>-3.823e+05</td><td>-6.628e+04</td><td>-1.218e+05</td><td>-3.635e+05</td><td>-6.087e+04</td><td>-1.010e+05</td></tr></table>

<table><tr><td></td><td colspan="3">w</td><td colspan="3"> $\pi_p$ </td></tr><tr><td></td><td>EG</td><td>HB</td><td>AL</td><td>EG</td><td>HB</td><td>AL</td></tr><tr><td>Intercept</td><td>108.919***</td><td>32.912***</td><td>197.005***</td><td>25.383***</td><td>21.565***</td><td>18.833***</td></tr><tr><td>ε</td><td>162.925***</td><td>8.352***</td><td>—</td><td>63.272***</td><td>43.635***</td><td>46.872***</td></tr><tr><td> $ε^2$ </td><td>-738.914***</td><td>—</td><td>42.787***</td><td>-161.022***</td><td>-132.330***</td><td>-72.827***</td></tr><tr><td>ζ</td><td>-48.100***</td><td>—</td><td>-30.652***</td><td>16.895***</td><td>-41.315***</td><td>-87.791***</td></tr><tr><td> $ζ^2$ </td><td>—</td><td>-231.883***</td><td>-73.525***</td><td>-60.437***</td><td>105.049***</td><td>262.364***</td></tr><tr><td>γn</td><td>17.307***</td><td>24.746***</td><td>—</td><td>5.647***</td><td>2.159***</td><td>—</td></tr><tr><td> $γn^2$ </td><td>-3.469**</td><td>3.751*</td><td>—</td><td>-1.478*</td><td>—</td><td>—</td></tr><tr><td>rp</td><td>5.636***</td><td>82.765***</td><td>-71.933***</td><td>-.727*</td><td>3.096***</td><td>—</td></tr><tr><td>TCA</td><td>.384***</td><td>.416***</td><td>.444***</td><td>.103***</td><td>.102***</td><td>.104***</td></tr><tr><td>Observations</td><td>178200</td><td>89100</td><td>178200</td><td>178200</td><td>89100</td><td>178200</td></tr><tr><td> $R^2$ </td><td>.034</td><td>.116</td><td>.084</td><td>.015</td><td>.012</td><td>.023</td></tr><tr><td>AIC</td><td>1.844e+06</td><td>9.002e+05</td><td>1.733e+06</td><td>1.585e+06</td><td>7.818e+05</td><td>1.550e+06</td></tr><tr><td>BIC</td><td>1.844e+06</td><td>9.003e+05</td><td>1.733e+06</td><td>1.585e+06</td><td>7.818e+05</td><td>1.550e+06</td></tr><tr><td colspan="7">Note: ***p&lt;.01, **p&lt;.05, *p&lt;.1. Variable abbreviations: EG: egoistic market; HB: hybrid market; AL: altruistic market; ε: average incentives for positive reviews; ζ: average level of overstatement; γn: average probability of giving enhancing responses to negative reviews; rp: average review perception; TCA: total consumer arrivals;  $\hat{\pi}$ : total provider benefits;  $\bar{\pi}_C$ : average consumer benefits;  $\bar{\pi}_{CS}$ : average consumer satisfaction;  $\pi_p$ : platform revenue; w: total social welfare</td></tr></table>

Table A8. Marginal Effect of Review Interventions on Market Outcomes

<table><tr><td>Independent variable</td><td>Dependent variable</td><td>EG</td><td>HB</td><td>AL</td></tr><tr><td rowspan="5">ε</td><td> $\hat{\pi}$ </td><td> $\Uparrow (ME: -13.758-960.622\varepsilon)$ </td><td> $\Uparrow (ME: -1097.026\varepsilon)$ </td><td> $\Uparrow (ME: -516.012\varepsilon)$ </td></tr><tr><td> $\bar{\pi}_{C}$ </td><td> $\Uparrow (ME: 0.407-0.504\varepsilon)$ </td><td> $\Uparrow \Uparrow (ME: -0.181+5.74\varepsilon)$ </td><td> $\Uparrow (ME: -0.182+2.836\varepsilon)$ </td></tr><tr><td> $\bar{\pi}_{CS}$ </td><td> $\Uparrow (ME: -5.305-17.129\varepsilon)$ </td><td> $\Uparrow (ME: -3.080+5.012\varepsilon)$ </td><td> $\Uparrow \Uparrow (ME: -1.564+6.135\varepsilon)$ </td></tr><tr><td> $\pi_{p}$ </td><td> $\Uparrow \Uparrow (ME: 63.272-322.045\varepsilon)$ </td><td> $\Uparrow \Uparrow (ME: 43.635-264.660\varepsilon)$ </td><td> $\Uparrow \Uparrow (ME: 46.872-145.653\varepsilon)$ </td></tr><tr><td>w</td><td> $\Uparrow \Uparrow (ME: 162.925-1477.827\varepsilon)$ </td><td> $\Uparrow (ME: 8.352)$ </td><td> $\Uparrow (ME: 85.574\varepsilon)$ </td></tr><tr><td rowspan="5">ζ</td><td> $\hat{\pi}$ </td><td> $\Uparrow \Uparrow (ME: 13.569-148.187\zeta)$ </td><td> $\Uparrow (ME: 116.236-322.009\zeta)$ </td><td> $\Uparrow (ME: 113.951)$ </td></tr><tr><td> $\bar{\pi}_{C}$ </td><td> $\Uparrow \Uparrow (ME: -0.340+1.271\zeta)$ </td><td> $\Uparrow (ME: -0.335-0.932\zeta)$ </td><td> $\Uparrow (ME: -0.198-2.354\zeta)$ </td></tr><tr><td> $\bar{\pi}_{CS}$ </td><td> $\Uparrow \Uparrow (ME: -13.193+50.435\zeta)$ </td><td> $\Uparrow (ME: -7.730+13.695\zeta)$ </td><td> $\Uparrow (ME: -5.457+4.871\zeta)$ </td></tr><tr><td> $\pi_{p}$ </td><td> $\Uparrow \Uparrow (ME: 16.895-120.875\zeta)$ </td><td> $\Uparrow \Uparrow (ME: -41.315+210.1\zeta)$ </td><td> $\Uparrow \Uparrow (ME: -87.791+524.729\zeta)$ </td></tr><tr><td>w</td><td> $\Uparrow (ME: -48.100)$ </td><td> $\Uparrow (ME: -463.766\zeta)$ </td><td> $\Uparrow (ME: -30.652-147.051\zeta)$ </td></tr><tr><td rowspan="5">γn</td><td> $\hat{\pi}$ </td><td> $\Uparrow (ME: 6.299)$ </td><td> $\Uparrow (ME: -7.697)$ </td><td> $\Uparrow (ME: 5.164\gamma n)$ </td></tr><tr><td> $\bar{\pi}_{C}$ </td><td> $\Uparrow (ME: 0.009)$ </td><td> $\Uparrow (ME: 0.114+0.033\gamma n)$ </td><td> $\Uparrow (ME: -0.034\gamma n)$ </td></tr><tr><td> $\bar{\pi}_{CS}$ </td><td> $\Uparrow (ME: -0.188)$ </td><td> $\Uparrow (ME: 0.431)$ </td><td> $\Uparrow (ME: -0.059)$ </td></tr><tr><td> $\pi_{p}$ </td><td> $\Uparrow (ME: 5.647-2.955\gamma n)$ </td><td> $\Uparrow (ME: 2.159)$ </td><td>— (ME: 0)</td></tr><tr><td>w</td><td> $\Uparrow (ME: 17.307-6.937\gamma n)$ </td><td> $\Uparrow (ME: 24.746+7.502\gamma n)$ </td><td>— (ME: 0)</td></tr><tr><td colspan="5">Note: ME: marginal effect. Variable abbreviations—EG: egoistic market; HB: hybrid market; AL: altruistic market; ε: average incentives for positive reviews; ζ: average level of overstatement; γn: average probability of giving enhancing responses to negative reviews; η: total provider benefits;  $\bar{\pi}_{C}$ : average consumer benefits;  $\bar{\pi}_{CS}$ : average consumer satisfaction;  $\pi_{p}$ : platform revenue; w: total social welfare</td></tr></table>

## About the Authors

Guoyin Jiang is a full Professor at the University of Electronic Science and Technology of China. He received his PhD from the Huazhong University of Science and Technology, China. His research interests include information systems, platform economy, information management, and social simulation. He has published over 110 peer-reviewed papers in academic journals and conference proceedings, including IEEE Transactions on Mobile Computing, European Journal of Operational Research, Information & Management, and International Journal of Information Management, among others

Yingchao Fu received his bachelor’s degree in information management and information systems from the University of Electronic Science and Technology of China in 2022, where he is currently pursuing a PhD in management science and engineering. His research interests include information systems, big data and social simulation.

Copyright © 2026 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee, provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via email from publications@aisnet.org.
