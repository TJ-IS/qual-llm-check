---
otero_id: 28570
otero_key: "GVYE476P"
title: "Ephemeral State-Dependent Recommendation for Digital Content"
authors: "Lanfei Shi; Jin Liu; Yongjun Li; Natasha Zhang Foutz"
year: "2025"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.664"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Ephemeral State-Dependent Recommendation for Digital Content

Lanfei Shi,<sup>a,</sup>\* Jin Liu,<sup>b,</sup>\* Yongjun Li,<sup>c</sup> Natasha Zhang Foutz<sup>d</sup>

<sup>a</sup> Information Technology and Innovation, McIntire School of Commerce, University of Virginia, Charlottesville, Virginia 22904; <sup>b</sup> Information Management, School of Economics and Management, Beijing Jiaotong University, Beijing 100044, China; <sup>c</sup> Management Science, The School of Management, University of Science and Technology of China, Hefei 230026, China; <sup>d</sup> Marketing, McIntire School of Commerce, University of Virginia, Charlottesville, Virginia 22904

\*Corresponding authors

Contact: ls4tj@virginia.edu, https://orcid.org/0000-0001-6521-8973 (LS); liujin0718@gmail.com, https://orcid.org/0000-0002-4485-8063 (JL); lionli@ustc.edu.cn, https://orcid.org/0000-0003-0072-268X (YL); nfoutz@virginia.edu, https://orcid.org/0000-0002-0663-4923 (NZF)

Received: November 30, 2022 Revised: December 6, 2023; August 12, 2024; December 8, 2024; January 28, 2025 Accepted: February 3, 2025 Published Online in Articles in Advance: February 24, 2025

https://doi.org/10.1287/isre.2022.664

Copyright: © 2025 INFORMS

Abstract. Building upon recent advances in consumption theories, we propose an ephemeral state-dependent framework for digital content recommendations. The framework accentuates a critical, yet understudied, interplay between a firm’s recommendation strategy (assimilation or diversification) and a consumer’s ephemeral state. This temporary state is gauged by the breadth of a consumer’s ephemeral preference at the moment of choice— either fixation on a single type of content or foraging across types. The framework adaptively recommends either assimilated or diversified content based on a consumer’s ephemeral state, accomplishing effective strategy-state pairing. A large-scale randomized field experiment in collaboration with a leading e-book platform demonstrates the consumption and profit impacts of such state-dependent recommendations. Although the strategy-state congruent scheme (i.e., assimilation when fixation, diversification when foraging) is overall superior, the incongruent scheme (i.e., assimilation when foraging, diversification when fixation) is more desirable for consumers with a more fluid or broader preference, revealing consumer heterogeneity and needs for refined personalization. We further demonstrat nuanced spillover effects on the nonrecommended content. This research contributes to the literature by incorporating theory-driven designs into recommender systems and provid ing important managerial insights for the digital content industry.

History: Olivia Liu Sheng, Senior Editor; Jingjing Zhang, Associate Editor.

Funding: Y. Li received financial support from the National Natural Science Foundation of China [Grants 72071192, 72188101, and 72091210].

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2022.664.

Keywords: digital content consumption • recommender system • recommendation framework • state-dependency • ephemeral state congruence • randomized field experiment

## 1. Introduction

The \$196 billion digital content platforms—including e-books, short videos, motion pictures, music, and gaming—are experiencing rapid growth, projected to reach \$340 billion by 2034.<sup>1</sup> Recommender systems play a vital role in enhancing consumer engagement and platform profitability, effectively matching consumers with their desired content among a vast number of choices. Although recommender systems for physical goods are better developed, those for digital content face unique challenges due to distinct consumer behavior when engaging with digital content. In particular, recent theoretical advancements underscore the transient and ephemeral nature of digital content consumption, a factor often overlooked by content recommendations.

The ephemerality of digital content consumption can be characterized by two dimensions. One is a consumer’s transient ephemeral preference, which is more capable than the longer-term enduring preference of capturing a consumer’s interest at the moment of choice (Salisbury and Feinberg 2012, Shaddy et al. 2021). The other is a consumer’s ephemeral state, which is a temporary consumption state capturing foraging or fixation consumption behavior (Trijp et al. 1996, Schweidel and Moe 2016, Bardhi and Eckhardt 2017). The ephemeral state can be gauged by the breadth of the consumer’s ephemeral preference. For instance, the consumer might be fixating on a single type of content (e.g., romantic e-books) or foraging across diverse content (romance, history, and science fiction). The ephemeral state offers valuable insights into predicting subsequent consumer choices. Accordingly, our study takes an initial step toward integrating the concept of ephemerality into digital content recommender systems to enhance their effectiveness.

Additionally, behavioral theories suggest that consumers display dual needs for both consistency and variety during content consumption (Etkin 2016, Gullo et al. 2019, Huang et al. 2019, Shaddy et al. 2021). To better address such dual needs, effective recommender systems must balance them by implementing an assimilation or diversification recommendation strategy, while also considering ephemerality, which has not yet been well explored. A consumer may choose a piece of recommended content similar to, or different from, what they have recently consumed. This choice importantly depends on the consumer’s ephemeral state (i.e., foraging or fixation). Thus, it is theoretically and practically crucial to incorporate the interplay between a firm’s recommendation strategy and the consumer’s ephemeral state into a content recommender system (Cialdini et al. 1995, Salisbury and Feinberg 2012, Bardhi and Eckhardt 2017).

Despite these insights, whether platforms should recommend assimilated or diversified content when a consumer is in a fixation or foraging state remains unclear. To address this gap, we propose an ephemeral state-dependent (state-dependent hereafter) framework that flexibly and effectively pairs a firm’s recommendation strategy<sup>2</sup> with a consumer’s ephemeral state at the moment of content choice. We refer to such a strategystate pairing as a recommendation scheme (or simply scheme).<sup>3</sup>

According to the congruence theory (Nadler and Tushman 1980, Miner et al. 1994), there are two possible pairings in our proposed state-dependent schemes. The congruent scheme aligns the recommendation strategy with the consumer’s ephemeral state (assimilation when fixation, diversification when foraging), whereas the incongruent scheme does the opposite (assimilation when foraging, diversification when fixation). The literature on congruence provides mixed empirical findings across various contexts on whether it is congruence or incongruence that leads to better outcomes (e.g., Miner et al. 1994, Yoon 2013, Peng et al. 2020). Without conclusive theoretical guidance, it remains an open question as to whether a congruent or incongruent scheme, particularly in a new context of digital content recommendations, would be more beneficial to a platform or a consumer. Specifically, we intend to address the following two key research questions:

Research Question 1. Are ephemeral state-dependent schemes superior to state-independent schemes?

Research Question 2. Which specific state-dependent scheme, congruent or incongruent, should a platform deploy to target which type of consumers?

To accomplish the above, we conduct a large-scale randomized field experiment in collaboration with a leading e-book platform in Asia that accrues an annual revenue of \$270 million. To systematically examine the value of the state-dependent schemes or strategy-state pairing, we adopt a between-subject design and randomly assign a consumer to one of the six experimental groups: (i) two state-independent schemes based on each consumer’s enduring preference (Control 1 � always assimilation, Control 2 � always diversification) as the baselines, (ii) two state-independent schemes based on each consumer’s ephemeral preference (Treat ment 1 � always assimilation, Treatment 2 � always diversification), and (iii) two state-dependent schemes based on each consumer’s ephemeral preference and ephemeral state (Treatment 3 � assimilation when foraging, diversification when fixation—the incongruent scheme; Treatment 4 � assimilation when fixation, diversification when foraging—the congruent scheme). We focus on comparing Treatment 3 and Treatment 4, both featuring the strategy-state pairing of core interest.

The analyses reveal several interesting findings. First, state-dependent schemes outperform state-independent schemes, highlighting the value of the adaptive pairing of a recommendation strategy and ephemeral state in a digital content recommender system (Research Question 1). This presents a valuable contribution to the literature on digital content consumption and literature on recommender systems. Second, between the two statedependent schemes, the congruent scheme is overall more effective in driving consumption (reading) and profit (payment) than the incongruent scheme, producing a remarkable 7.3% (\$19.73 million) lift to the platform’s annual revenues. Interestingly, the congruent scheme is not always optimal, as consumer heterogeneities prevail. For instance, the incongruent scheme is more desirable to consumers with a more fluid or broader preference, indicating the potential for nuanced personalization (Research Question 2). We further conduct a survey to gain a better understanding of the potential mechanisms. Our research hence examines heterogeneity in responses to a novel form of congruence— strategy-state congruence, shedding light on the mixed findings from the congruence literature. Lastly, the proposed state-dependent schemes also generate positive demand spillovers toward the nonrecommended contents, both within and across content categories, magnifying the value of such schemes to both theory and practice.

In summary, our research offers both academic contributions and actionable implications. It demonstrates the importance of integrating a distinct core characteristic of digital content consumption—ephemerality in consumer preference and consumption state—into content recommender systems. Through a carefully designed large-scale field experiment, we illustrate to the platform the value of strategy-state pairing and nuanced personalization in light of consumer heterogeneity. There is no one-size-fits-all solution: the incongruent scheme may outperform the congruent scheme among a segment of consumers. This research also highlights a holistic perspective, accounting for demand spillover toward nonrecommended contents, while implementing new recommendation schemes.

The remaining manuscript is organized as follows. Section 2 introduces the theoretical background and reviews the relevant literature. Sections 3 and 4 report the experimental design, empirical models, and findings. Section 5 concludes and discusses the managerial implications and future research.

## 2. Theoretical Background

We briefly review three streams of literature: liquid consumption, congruency, and recommender systems, which collectively and coherently construct the theoretical foundation of our design of the state-dependent recommendation schemes.

## 2.1. Ephemerality and State-Dependent Schemes

Our design of the state-dependent recommendation schemes stems from the literature on consumer behavior, which categorizes consumption into liquid versus solid (Binkley 2008, Rindfleisch et al. 2009, Bardhi et al. 2012, Bardhi and Eckhardt 2017). Along a spectrum, liquid consumption is ephemeral and access-based, such as consumption of e-books, music, or short videos, whereas solid consumption is enduring and material, such as consumption of durable goods. Liquid consumption accentuates ephemerality (Kozinets 2002) and characterizes instant, as opposed to long-lasting, consumption (Goulding et al. 2009). It importantly explains consumption in digital contexts (Weiss and Johar 2016, Bardh and Eckhardt 2017). Our research hence incorporates this essential characteristic of ephemerality into recommender systems for digital content.

Specifically, ephemerality encompasses two distinct dimensions: ephemeral preference and ephemeral state gauged by the breadth of ephemeral preference. Choice theories suggest that a consumer’s ephemeral preference at the moment of choice is distinct from the longer-term enduring preference, better aligned with the present goal and impacted by personal factors (e.g., health or mood) and contextual factors (e.g., choice set) (Hoch and Loewenstein 1991, Payne et al. 1993, Bettman et al. 1998, Amir and Levav 2008). For instance, a consumer exploring massive volumes and varieties of digital contents, such as fictions or short videos, commonly exhibits an ephemeral and fluid, instead of enduring and stable, preference for a particular genre or type of content (Gomez-Uribe and Hunt 2015, Song et al. 2019).

Meanwhile, ephemeral state, gauged by the breadth of a consumer’s ephemeral preference, critically determines consumer choice. Ephemeral state is often intermittent, influenced by an individual’s immediate cognitive accessibility and contextual factors (Lawson et al. 2021).

This is in contrast to the individual’s long-term traits, which are more stable, predictable, and associated with loyalty (Che et al. 2007, Simonov et al. 2020). We employ the terms foraging and fixation to characterize a consumer’s present, ephemeral mindset, or underlying consumption state (Bardhi et al. 2012, Bardhi and Eckhardt 2017). Fixation describes the consumption state where a consumer displays focused concentration, usually on certain categories or genres of content in a repetitive or even addictive manner (Chou and Ting 2003, Schweidel and Moe 2016). On the other hand, foraging depicts the switching behavior across content categories or genres. It seeks variation, variety, and exploration, driven by reward-seeking, curiosity, and resolution of boredom (McAlister and Pessemier 1982, Trijp et al. 1996). For instance, a consumer’s choice of an e-book could be drastically different if the consumer is in a state of fixation on a single genre of content (e.g., romance) or foraging across genres (romance, history, and comedy).

We hence propose and evaluate two ephemeral statedependent recommendation schemes (Treatment 3 and Treatment 4 described earlier). Although the dual needs of consumers for consistency and variety have been underexplored (Cialdini et al. 1995, Salisbury and Feinberg 2012, Bardhi and Eckhardt 2017), our proposed schemes aim to address such needs by adaptively deploying either assimilation or diversification recommendation strategies based on a consumer’s ephemeral state at any given moment. Specifically, the assimilation strategy focuses on providing consistency, offering comfort and familiarity (Shaddy et al. 2021), whereas the diversification strategy provides variety, enhancing psychological stimulation (Etkin 2016, Gullo et al. 2019, Huang et al. 2019) and reducing satiation from repeated experiences (Galak et al. 2013). To importantly boost effectiveness, recommender systems should better integrate and balance such dual needs. Our design thus adapts recommendations to match each consumer’s dynamic needs for consistency and variety, aligning them with the consumer’s transient ephemeral state.

In summary, our research incorporates an essential theoretical construct—ephemerality in liquid consumption— into recommender systems of digital content. We further demonstrate its importance via a large-scale randomized field experiment. In particular, our study represents an early endeavor to investigate the interplay between the recommendation strategy and ephemeral state in digital content consumption and incorporates a theory-driven adaptive design into a recommender system. Moreover, our research adds to the emerging studies on contextual marketing, where critical contextual information, such as weather, crowdedness, and, in our case, an essential consumer input, ephemeral state, is effectively leveraged to accomplish fine-grained personalization (Luo et al. 2014, Fong et al. 2015, Andrews et al. 2016). This research further broadens the burgeoning research on the online publishing industry from line extension (Gu et al. 2018), targeted promotion (Fong et al. 2019), and consumer reviews (Choi et al. 2019), to recommender systems.

## 2.2. Congruence

We draw from the congruence theory to understand the pairings between ephemeral state and recommendation strategies in our state-dependent schemes. According to Nadler and Tushman (1980, p. 45), “the congruence between two components is defined as the degree to which the needs, demands, goals, objectives, and/or structures of one component are consistent with the needs, demands, goals, objectives, and/or structure of another component,” highlighting the effectiveness of such alignment (Miner et al. 1994). As researchers delve deeper into the concept of congruence, mixed findings emerge. Some studies show positive effects of congruence, such as congruence between an organization’s social claim and its leadership gender on job applicants’ gender composition (Abraham and Burbano 2022); congruence between influencers and products on willingness to purchase (Belanche et al. 2021); and content-context congruence in answers on the perceived helpfulness of medical question-and-answer sites (Peng et al. 2020). Meanwhile, incongruence could be more beneficial, such as in advertising and other contexts (Mitchell et al. 1995, Lee and Schumann 2004, Yoon 2013).

In light of these mixed findings, whether a congruent or incongruent recommendation scheme is more desirable remains a debatable topic. Our study hence extends the above literature by examining a distinct type of congruence: strategy-state congruence. Specifically, we empirically investigate consumers’ decision making when presented with a congruent or incongruent recommendation scheme. Although a comprehensive understanding of this topic remains scant, we draw on relevant cognitive and psychological literature for insights. Specifically, two opposing forces might influence consumers’ reactions to congruent or incongruent recommendations. The Schema effect suggests that consumers prefer choices or information congruent with their existing preferences, which offer familiarity and ease of information retrieval and processing (Pezdek et al. 1989, Schaper et al. 2019). This reasoning supports congruent recommendation schemes. Conversely, the Isolation effect posits that consumers are drawn to surprises or changes that capture their attention and facilitate memory encoding (Hunt and Lamb 2001). As a result, some consumers could be more responsive to incongruent recommendation schemes. We build upon these psychological theories to investigate potential mechanisms underlying the (in)congruent recommendation schemes.

In summary, whether a strategy-state congruent or incongruent scheme is more desirable remains intriguingly inconclusive. Such ambiguity arises from not only the distinct context, but also underdeveloped theoretical understanding of how congruence influences information processing and decision making. We take an initial step exploring how consumers respond to state-(in)congruent content recommendations.

## 2.3. Recommender Systems

An interdisciplinary literature (Online Appendix A) has examined a variety of recommender systems, largely in the contexts of solid consumption and e-commerce (Fitzsimons and Lehmann 2004, De Bruyn et al. 2008, Chung et al. 2009, Ghose et al. 2012, Lu et al. 2016, Ansari et al. 2018). These systems emphasize accurate predictions of consumers’ product choices by primarily assimilating recommendations with consumers’ enduring preferences, hence reducing search costs and uplifting sales conversions (Linden et al. 2003, Adomavicius and Tuzhilin 2005, Gomez-Uribe and Hunt 2015, Panniello et al. 2016). These assimilation algorithms, although ful filling a consumer’s need for consistency, reduce choice diversity and potentially induce consumption fatigue or concentration bias (Fleder and Hosanagar 2009). To address these limitations, various diversification algorithms have been developed to integrate objectives beyond consistency, such as serendipity, novelty, coverage, and variety (Adomavicius and Kwon 2014, Kaminskas and Bridge 2016, Kunaver and Pozˇrl 2017, Castells et al. 2021). Our work extends this line of research by accommodating consumers’ dual needs with adaptive strategy-state pairing.

A growing Information Systems (IS) literature has also examined recommender systems (Xiao and Benbasat 2007, Li and Karahanna 2015). One stream stud ies the impact of recommender systems on consumer choice, willingness-to-pay, or sales diversity (Adomavicius et al. 2018, Kumar and Hosanagar 2019, Lee and Hosanagar 2019, Lee et al. 2020, Li et al. 2022, Wan et al. 2024a). For instance, Li et al. (2022) investi gate how the size and depth of a consideration set play mediating roles in consumer purchase. Another stream examines design considerations, such as which types of consumer data or contextual information should be incorporated into recommender systems (Mousavi et al. 2023, Peng and Liang 2023, Wan et al. 2024b). For instance, Peng and Liang (2023) compare the view-also-view and purchase-also-purchase models in collaborative filtering. In a nutshell, the above two lines of work concentrate on assimilation algo rithms and solid consumption in e-commerce.

A third line focuses on designing new recommendation algorithms, particularly diversification algorithms, while emphasizing technical or modeling innovations (Song et al. 2019, Yin et al. 2023, Li and Tuzhilin 2024). For instance, Yin et al. (2023) propose link prediction models that leverage individuals’ diversity preferences in a social network. Song et al. (2019) develop a multicategory utility model to accommodate a consumer’s cross-session content consumption. Li et al. (2022) propose diversification algorithms that effectively measure a consumer’s variety-seeking tendency.

Whereas the above literature examines either assimilation or diversification algorithm, our study proposes a general state-dependent recommendation framework, adaptively deploying either algorithm given ephemerality and strategy-state interplay. Such a state-dependent pairing does not constrain the use of any specific assimilation or diversification algorithm. In addition, our examination of demand spillover toward nonrecommended contents extends the spillover literature. Prior research has identified their positive externalities for similar products or complementary products, often through increased awareness or network amplification (Oestreicher-Singer and Sundararajan 2012, Liang et al. 2019). However, these studies primarily focus on assimilation strategies, leaving open how state-dependent recommendations might impact within- versus crosscategory spillovers.

## 3. Experimental Design

We conduct a large-scale randomized field experiment in collaboration with a leading e-book platform boasting an annual revenue of \$270 million. A total of 140 million monthly active customers access e-books via the platform’s mobile app. Each consumer receives an e-book recommendation daily via a personal virtual bookshelf. Each book belongs to 1 of the 20 distinct genres, such as fantasy, martial arts, horror, sci-fi, romance, and history. All books within a genre share a common theme, rendering genre a widely accepted measure of consumer preference in the digital content industry (Chen et al. 2010, Fong et al. 2019, Jiang et al. 2024, Morozov and Tuchman 2024). In a later section, we further validate genres as a reliable measure of consumer preference through content analysis. Moreover, the platform prohibits consumers from sharing accounts, which is rare, even without such a policy. We focus on consumers’ reading behavior because it is the core engagement metric used by e-book platforms. We also discuss monetary outcomes later for managerial insights.

## 3.1. Operationalization

Ephemeral preference captures a consumer’s transient preference that could dynamically shift, whereas enduring preference reflects the more stable, longer-term preference (Amir and Levav 2008, Narasimhan and Turut

2013, Guo 2016). The specific time window used to quantify a consumer’s ephemeral (or enduring) preference should align with the domain- or context-specific consumption cycle—for instance, a shorter window for short videos and a longer window for e-books. We follow the platform’s suggestion to measure each consumer’s ephemeral preference (enduring preference) based on the reading consumption over the rolling prior seven days<sup>5</sup> (three months). We also validate this before the experiment by inspecting the reading behavior of 1,294 randomly selected consumers (details in Online Appendix B).

Ephemeral state is gauged by the breadth of a consumer’s ephemeral preference (Amir and Levav 2008, Chen et al. 2010, Morozov and Tuchman 2024). Coherent with the executives’ suggestion, we measure a consumer’s ephemeral state simply as binary: fixation if reading only one genre and foraging if two or more genres, over the rolling prior seven days, consistent with the time window used to measure the ephemeral preferences. This measure is also supported by our analy sis of the same 1,294 consumers (details in Online Appendix B). We also present a stylized example of a consumer switching between the two ephemeral states over time, highlighting the importance of integrating this critical and fine-grained characteristic of digital con tent consumption into recommender systems (Figure B2 in the Online Appendix). As robustness checks, we further test alternative measures of ephemeral state using different time windows, as well as apply a more granular, continuous measure of ephemeral state derived from book content analysis, as detailed in Section 4.5.

## 3.2. Control and Treatment Groups

Our between-subject design consists of two control groups based on enduring preference (Control 1 or C1 hereafter, Control 2 or C2 hereafter)<sup>6</sup> and four treatment groups based on ephemeral preference, including two state-independent schemes (Treatment 1 or T1 hereafter, similar for T2) and two state-dependent schemes of focal interest (T3 � incongruent scheme, T4 � congruent scheme) (Tables 1 and 2). Table B1 in the Online Appendix further displays a few stylized examples of how recommendations differ across these six experimental groups, even when the enduring preference and ephemeral preference are identical.

As we focus on the state-dependent recommendation schemes—that is, different pairings of an assimilation/ diversification recommendation strategy with a foraging or fixation ephemeral state—we do not impose any restrictions on which specific recommendation algorithms are used to execute an assimilation or diversification strategy. In our empirical illustration, we intentionally choose a simple, rule-based recommendation algorithm for assimilation (diversification), where an e-book is randomly selected from the genres that the consumer has read (not read) over the prior seven days.<sup>7</sup> This design decision is grounded on three key considerations. One, as a first step to systematically quantify the marginal differences across recommendation schemes, complex or opaque algorithms are intentionally circumvented to ensure a cleaner identification. As we focus on a strategy-state pairing framework, it is essential to utilize a simple algorithm in our treatments. Two, this algorithm accommodates both assimilation and diversification to permit testing of different strategy-state pairings, without introducing additional confounders. Third, our approach to the same (different)-genre selection aligns with the established practice of using a robust starting point to evaluate various assimilation/diversification recommender systems (Gori and Pucci 2007, Chaney et al. 2018, Chaney 2021).

Table 1. Experimental Design: Pairings of Recommendation Strategy and Ephemeral State

<table><tr><td>State</td><td>Assimilation recommendation (0)</td><td>Diversification recommendation (1)</td></tr><tr><td>Fixation state (A)</td><td>A-0</td><td>A-1</td></tr><tr><td>Foraging state (B)</td><td>B-0</td><td>B-1</td></tr></table>

Table 2. Experimental Design: Experiment Groups and Corresponding Recommendation Schemes

<table><tr><td>Scheme</td><td>Description</td></tr><tr><td colspan="2">Benchmark schemes</td></tr><tr><td>C1</td><td>Always assimilation based on enduring preference (0)</td></tr><tr><td>C2</td><td>Always diversification based on enduring preference (1)</td></tr><tr><td colspan="2">State-independent schemes</td></tr><tr><td>T1</td><td>Always assimilation based on ephemeral preference, irrespective of ephemeral state (A-0, B-0)</td></tr><tr><td>T2</td><td>Always diversification based on ephemeral preference, irrespective of ephemeral state (A-1, B-1)</td></tr><tr><td colspan="2">State-dependent schemes</td></tr><tr><td>T3</td><td>Diversification when fixation, assimilation when foraging, both based on ephemeral preference (A-1, B-0)</td></tr><tr><td>T4</td><td>Assimilation when fixation, diversification when foraging, both based on ephemeral preference (A-0, B-1)</td></tr></table>

In summary, compared with a more conventional, static two (recommendation strategies) × two (ephemeral states) design, the proposed simple rule-based design elegantly integrates the dynamic ephemeral state inherent in digital content consumption. More importantly, it adaptively deploys either an assimilation or diversification strategy, given the consumer’s dynamic ephemeral state in real-time. This design also enables us to examine the value of the state-dependent schemes (T3 and T4) and to compare the incongruent (T3) and congruent (T4) schemes in order to illuminate when to offer a personalized assimilation versus diversification recommendation in light of the consumer’s real-time ephemeral state.

Given the platform’s interest in improving engagement with active users, we conduct the experiment among 108,158 consumers randomly drawn from those who have read at least once in the week prior to the experiment. The experiment lasts over five days, from September 1st to 5th, 2020. Each consumer is randomly assigned to one of the above six experimental groups on the first day of the experiment and then offered a recommendation during each of the five experimental days. The recommended book appears at the top of the consumer’s personal virtual bookshelf, clearly marked as “recommended” (a mock-up is in Online Appendix B, Figure B3). Such a repeated treatment over a span of several days aligns with the practical needs of digital content platforms because it permits an assessment of the aggregate effect of each state-dependent scheme on a regular basis (e.g., daily), rather than via a one-shot deployment. Our findings thus offer the platform critical and actionable insights into the best scheme to deploy.

As described earlier, each consumer’s enduring preference and ephemeral preference are, respectively, determined by the books read over the rolling prior three months and seven days before the experiment. The ephemeral state over each of the five experimental days is determined by the number of genres over the rolling prior seven days. Given that an average consumer takes 7 days to complete reading an e-book, we track each consumer’s reading behavior of the recommended books over a 12-day observational period. This includes the five experimental days with recommendations and the following seven days without interventions.

## 4. Empirical Results

## 4.1. Data and Models

Table 3 displays the summary statistics of the key variables in the analyses. Specifically, the independent variables include the dummy indicators of each experimental group, with C1 as the baseline. The dependent variables measure each consumer’s response to the recommendations over the 12-day observational period: readrate � percentage of the recommended books with at least one chapter read, and readtime � total time spent reading the recommended books.

Table 3. Summary Statistics

<table><tr><td>Variables</td><td>Description</td><td>Mean</td><td>SD</td><td>Min</td><td>Max</td></tr><tr><td colspan="6">Independent variables</td></tr><tr><td colspan="6">Treat</td></tr><tr><td>C2</td><td>1 if in C2, 0 otherwise</td><td>0.1688</td><td>0.3746</td><td>0</td><td>1</td></tr><tr><td>T1</td><td>1 if in T1, 0 otherwise</td><td>0.1658</td><td>0.3719</td><td>0</td><td>1</td></tr><tr><td>T2</td><td>1 if in T2, 0 otherwise</td><td>0.1659</td><td>0.3720</td><td>0</td><td>1</td></tr><tr><td>T3</td><td>1 if in T3, 0 otherwise</td><td>0.1666</td><td>0.3726</td><td>0</td><td>1</td></tr><tr><td>T4</td><td>1 if in T4, 0 otherwise</td><td>0.1659</td><td>0.3719</td><td>0</td><td>1</td></tr><tr><td colspan="6">Dependent variables</td></tr><tr><td colspan="6">Read</td></tr><tr><td>readrate</td><td># of recommended books read/total # recommended books (%)</td><td>0.0343</td><td>0.1272</td><td>0</td><td>1</td></tr><tr><td>readtime</td><td>Reading time (minutes)</td><td>34.3725</td><td>291.0087</td><td>0</td><td>13,004</td></tr><tr><td colspan="6">Pay</td></tr><tr><td>payment</td><td>Payment amount ($)</td><td>0.0254</td><td>0.4633</td><td>0</td><td>33.7600</td></tr></table>

We first conduct the randomization check (ANOVA) to ensure no statistically significant differences in the consumer characteristics (Table B2A in the Online Appendix) or recommended books (Table B2B in the Online Appendix) across the six experimental groups prior to our experiment. The results suggest a wellbalanced sample.

We estimate the causal impact of the recommendation scheme on reader behavior using an Ordinary Least Squares (OLS) regression for the continuous dependent variables (i.e., readtime) and a Fractional Logit Model for the percentage dependent variables (i.e., readrate). We further control the book-level covariates (Table B2B in the Online Appendix) in all analyses.

## 4.2. Reading

Reading is a key metric used by e-book platforms. Table 4 shows the preliminary value of accounting for the ephemeral preference (C1, C2 as baseline) and ephemeral state (T1, T2 as baseline). To address Research Question 1, we examine whether the state-dependent schemes (T3, T4) offer additional benefits to the platform relative to the state-independent schemes (T1, T2). The Wald tests confirm that the state-dependent schemes significantly uplift the readtime and readrate, compared with the state-independent schemes (e.g., T4 versus T1: $\chi ^ { 2 }$ (readrate) � 260.09, p-value < 0.001; F-stat (readtime) � 8.95, p-value � 0.0028). Whereas the behavioral literature recognizes the distinct characteristics of digital content consumption, our findings highlight the importance of integrating state-dependent recommendations (i.e., adaptive strategy-state pairing) into the design of content recommender systems (Che et al. 2007, Bardhi et al. 2012, Simonov et al. 2020).

Table 4. Effects of Recommendation Scheme on Reading

<table><tr><td>Variable</td><td>readrate (Fractional Logit)</td><td>readtime (OLS)</td></tr><tr><td>C2</td><td>-0.8680***(0.0482)</td><td>-16.9800***(3.0500)</td></tr><tr><td>T1</td><td>0.1930***(0.0376)</td><td>6.7110**(3.0300)</td></tr><tr><td>T2</td><td>-0.1320***(0.0460)</td><td>-12.3300***(3.1090)</td></tr><tr><td>T3</td><td>0.4350***(0.0410)</td><td>7.2260**(3.0480)</td></tr><tr><td>T4</td><td>0.7310***(0.0386)</td><td>15.8100***(3.0240)</td></tr><tr><td>Constant</td><td>-3.7620***(0.0402)</td><td>3.5590(2.8260)</td></tr><tr><td>Controls</td><td>√</td><td>√</td></tr><tr><td>p-value (T3 = T4)</td><td>&lt;0.0001</td><td>0.0050</td></tr><tr><td># obs.</td><td>108,158</td><td>108,158</td></tr><tr><td> $R^2$ </td><td>0.0296</td><td>0.0339</td></tr></table>

Notes. C1 serves as baseline. Robust standard errors are in parentheses. $^ { * } p < 0 . 1 ; ^ { * * } p < 0 . 0 5 ; ^ { * * * } p < 0 . 0 1 .$

Regarding Research Question 2, the Wald test shows that, overall, the state-dependent congruent scheme (T4) outperforms the state-dependent incongruent scheme (T3). That is, consumers are more responsive to the recommendations congruent with their ephemeral state. This finding documents the effectiveness of the strategy-state congruence in content recommender systems. Our exploration of the alignment between recommendation strategy and ephemeral state examines a novel type of congruency, thereby extending the literature on congruency (Miner et al. 1994). In summary, these results illustrate the importance of incorporating ephemeral state and adaptive strategy-state pairing into digital content recommendations.

## 4.3. Heterogeneous Treatment Effects

We further explore the heterogeneous treatment effects of the state-dependent schemes (T3 and T4), where T3 serves as the baseline. This will provide additional insights into which consumer segments respond better to which state-dependent scheme and shed light on the mixed findings from the congruency literature on whether congruence or incongruence is more beneficial (e.g., Mitchell et al. 1995, Lee and Schumann 2004, Greve et al. 2019, Boman et al. 2020). Additionally, this exploration will guide platforms to implement more targeted and personalized recommendations. Grounded on the choice literature where consumers’ preference heterogeneity influences their decision making (Ratner and Kahn 2002, Ching et al. 2013), we investigate three core traits: preference stability, preference breath, and engagement levels.

4.3.1. Preference Stability. We measure preference stability with the percentage of genres read in the seven days before the experiment that were also read in the three months prior (but excluding these latest seven days) (Rigby et al. 2016). This measure, ranging from zero (fluid) to one (stable), indicates how stable or expansive a consumer’s preference is (balanced across groups; p-value � 0.24).<sup>8</sup> Table 5 shows that the consumers with lower preference stability are more responsive to the incongruent scheme T3, whereas the congruent scheme T4 works better for consumers with higher preference stability (positive T4 × stability). Such heterogeneity in consumers’ preference for congruent versus incongruent schemes partly illuminates the mixed findings from the congruence literature (Boman et al. 2020, Peng et al. 2020, Belanche et al. 2021).

4.3.2. Preference Breadth. A consumer’s preference breadth is measured by the number of genres read in the three months prior to the experiment (but excluding the latest seven days) (balanced across groups; p-value � 0.75). Table 5 shows that the incongruent scheme T3 works better for consumers with a wider preference breadth (0.21 and 16.80). This reveals that preference breadth plays an important role in consumer decision making, and deploying a congruent scheme T4 is not always optimal. This also corroborates with the choice literature: consumers with diverse preferences may react differently to recommendations than those with more concentrated preferences (Dai et al. 2014, Shaddy et al. 2021).

4.3.3. Engagement Levels. Because consumers of varied engagement levels might react differently to congruent versus incongruent schemes, we further segment consumers based on their overall engagement—that is, total number of books read in the week prior to the experiment (balanced across groups; p-value � 0.3648). Table 5 shows that the incongruent scheme T3 works better for more engaged consumers than the congruent scheme T4. It is possible that highly engaged users are more drawn to surprises or changes that capture attention, which is facilitated by the incongruent scheme (Hunt and Lamb 2001).

Overall, these findings highlight that there is no onesize-fits-all scheme in content recommendations. Platforms should account for nuanced personalization, given consumer heterogeneity, while implementing state-dependent recommendation strategies (Che et al. 2007, Bardhi et al. 2012).

## 4.4. Demand Spillover and Economic Impact

We further investigate the economic impact of the state-dependent recommendation schemes below.

4.4.1. Payment. To assess the impact of the proposed schemes on the consumers’ payments, we show that, consistent with the finding on reading, state-dependent schemes lead to higher payments (Online Appendix C, Table C1). These coherent results along a consumer’s path-to-purchase (i.e., reading-to-purchase) reinforce the importance of accounting for ephemerality in digital content consumption and strategy-state congruence in recommender systems. They also enrich the congruence literature with a novel type of congruence, strategy-state congruence, in a new context of digital content consumption (Miner et al. 1994).

Table 5. Heterogeneous Treatment Effects

<table><tr><td rowspan="2">Variables</td><td colspan="2">Preference stability</td><td colspan="2">Preference breadth</td><td colspan="2">Engagement levels</td></tr><tr><td>readrate</td><td>readtime</td><td>readrate</td><td>readtime</td><td>readrate</td><td>readtime</td></tr><tr><td>T4</td><td>-0.1740(0.1400)</td><td>-12.1200(15.9500)</td><td>0.8490***(0.0626)</td><td>31.1600***(6.6740)</td><td>0.5790***(0.0483)</td><td>23.1700***(4.8580)</td></tr><tr><td> $T4 \times X$ </td><td>0.5090***(0.1490)</td><td>26.8700(16.7800)</td><td>-0.2350***(0.0207)</td><td>-9.6160***(2.6340)</td><td>-0.1010***(0.0114)</td><td>-4.4500***(1.3480)</td></tr><tr><td>X</td><td>-0.7410***(0.1130)</td><td>-38.0400***(13.0700)</td><td>0.2100***(0.0213)</td><td>16.8000***(2.3820)</td><td>0.0983***(0.0065)</td><td>3.7540***(0.9300)</td></tr><tr><td>Constant</td><td>-2.6730***(0.1110)</td><td>32.9000**(12.9600)</td><td>-3.7250***(0.0549)</td><td>-19.9300***(5.3990)</td><td>-3.5920***(0.0469)</td><td>-10.3000**(4.8210)</td></tr><tr><td>Controls</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td># obs.</td><td>35,957</td><td>35,957</td><td>35,957</td><td>35,957</td><td>35,957</td><td>35,957</td></tr><tr><td> $R^2$ </td><td>0.0128</td><td>0.0502</td><td>0.0165</td><td>0.0513</td><td>0.0189</td><td>0.0502</td></tr></table>

Notes. X represents each corresponding covariate. Robust standard errors in parentheses. \*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

4.4.2. Back-of-the-Envelope Analysis. We further show that the state-dependent congruent scheme T4 potentially translates into a \$19.73 million lift in the platform’s annual revenues, if our finding may be extrapolated to the 24.3 million paying customers on the platform and one daily recommendation per customer.<sup>9</sup> This demonstrates the tangible profit implications of implementing the proposed schemes.

4.4.3. Spillover Effect. To understand the holistic value of the proposed state-dependent schemes, we also explore whether the enhanced reading of the recommended content comes at the expense of the reduced consumption of other contents. Specifically, we examine the impact of the state-dependent schemes on the reading of the nonrecommended books from the same genre (focal\_category), a different genre (other\_categories), and any genre (overall).

Although we observe positive overall spillover effects in both the congruent (T4) and incongruent (T3) schemes, Table 6 also reveals interesting fine distinctions: whereas the incongruent scheme T3 boosts consumption in categories different than the recommended, the congruent scheme T4 elevates consumption both within- and across-categories, creating a stronger positive spillover. These insights underscore the broader impact of the state-dependent recommendation schemes. Overlooking such demand spillovers will underestimate the value of these schemes to a platform.

## 4.5. Robustness Checks

We perform a series of additional analyses to ensure the robustness of the findings.

Table 6. Spillover Effects of Recommendation Schemes

<table><tr><td>Variables</td><td>overall</td><td>focal_category</td><td>other_categories</td></tr><tr><td rowspan="2">C2</td><td>-0.0156*</td><td>-0.9130***</td><td>0.8380***</td></tr><tr><td>(0.0087)</td><td>(0.0130)</td><td>(0.0136)</td></tr><tr><td rowspan="2">T1</td><td>0.0081</td><td>0.1030***</td><td>-0.0737***</td></tr><tr><td>(0.0087)</td><td>(0.0112)</td><td>(0.0149)</td></tr><tr><td rowspan="2">T2</td><td>-0.2320***</td><td>-1.2340***</td><td>0.6070***</td></tr><tr><td>(0.0090)</td><td>(0.0142)</td><td>(0.0139)</td></tr><tr><td rowspan="2">T3</td><td>0.0362***</td><td>-0.4030***</td><td>0.7400***</td></tr><tr><td>(0.0086)</td><td>(0.0120)</td><td>(0.0137)</td></tr><tr><td rowspan="2">T4</td><td>0.2460***</td><td>0.1910***</td><td>0.3760***</td></tr><tr><td>(0.0085)</td><td>(0.0112)</td><td>(0.0143)</td></tr><tr><td rowspan="2">Constant</td><td>0.8740***</td><td>0.6200***</td><td>-0.4070***</td></tr><tr><td>(0.0082)</td><td>(0.0113)</td><td>(0.0133)</td></tr><tr><td>Controls</td><td>√</td><td>√</td><td>√</td></tr><tr><td>p-value (T3 = T4)</td><td>&lt;0.0001</td><td>&lt;0.0001</td><td>&lt;0.0001</td></tr><tr><td># obs.</td><td>108,158</td><td>108,158</td><td>108,158</td></tr><tr><td>R2</td><td>0.1173</td><td>0.0888</td><td>0.1239</td></tr></table>

Notes. We measure the number of nonrecommended books read by each subject and use Negative Binomial Regressions for count variables. C1 serves as baseline. Robust standard errors are in parentheses. \*p < 0.1; \*\*p < 0.05; \*\*\*p < 0.01.

4.5.1. Alternative Time Window. We reanalyze the data using only the responses from the five experimental days (Table D1, Online Appendix D) to confirm the consistent results without the seven additional obser vational days.

4.5.2. Alternative Model Specifications. We test alternative model specifications, such as the OLS regressions for readtime (Online Appendix D, Table D2). All findings remain consistent.

4.5.3. Genre as Measure of Preference. Our use of genre to gauge ephemeral preference and ephemeral state is consistent with the academic literature (Chen et al. 2010, Morozov and Tuchman 2024) and industry practice. Genre has been widely used by academics and industries to effectively define the themes and bound aries of book content and consumer preference. Moreover, we empirically validate this well-established approach by representing each book’s content (title, keywords, abstract) using embedding and then comparing the content distances of the books from the same versus different genres using t-tests (details in Online Appendix E). The books from the same genre have sig nificantly smaller distances compared with those from different genres, suggesting genre as a viable measure of consumer preference.

4.5.4. Operationalization of Ephemeral State. Our measure of the ephemeral state (foraging or fixation) is in accordance with the platform’s core metric of reading and orthogonal to the number of books read. Nonetheless, to ensure that this measure is not influenced by the number of books read, we analyze only those participants who read more than one book. Table D3 (Online Appendix D) exhibits consistent results.

We also seek to demonstrate the robustness of our findings by employing alternative measures of ephemeral state. Beyond the discrete, genre-based approach, we develop a more granular, continuous measure to capture finer nuances in ephemeral state. Specifically, we analyze the content of each book (title, keywords, abstract) to calculate the pairwise content similarity of the books read by a consumer over the three-, five-, and seven-day periods preceding the experiment. We take the maximum similarity score within each window to represent each consumer’s ephemeral consumption breadth: values in the lowest 25% of the distribution indicate a fixation state, whereas values in the highest 75% suggest a foraging state.<sup>10</sup>

Although it is not feasible to test this alternative measure in a new experiment, we simulate this approach through subsample analyses within our existing data set. Specifically, we focus on consumers whose ephemeral state can be reliably identified using the continuous measure described above across three-, five-, and seven-day windows (Table D4, Online Appendix D). All results remain consistent across these windows, further reinforcing the validity of our findings.

4.5.5. Engagement Depth. We also account for granular user engagement depth. We first conduct a sensitivity analysis by excluding occasional foragers (i.e., those who read only two genres) (Deng et al. 2024). The consistent results demonstrate that our findings are not affected by these occasional foragers (Online Appendix D, Table D5). Additionally, we control engagement depth within genres in our models. Specifically, we measure a consumer’s engagement depth using the Herfindahl-Hirschman Index (HHI) of the number of books that this consumer has read across genres preexperiment (HHI\_average). It ranges from zero (focused on a single genre) to one (even consumption across genres). We include this measure as a control variable in our model. All results remain consistent (Online Appendix D, Table D6).

4.5.6. Identification. We deliberately choose a repeated, instead of one-shot, treatment design to better align with the practical needs of a digital content platform, where recommender systems are utilized on a daily basis to offer recommendations to a consumer. By leveraging randomized assignments of recommendation schemes, we estimate the cumulative effects during the observational period. Nonetheless, we also conduct additional tests of the initial consumer reactions to the recommendations, aiming to isolate the subsequent consumption dependencies. Specifically, by analyzing the first two experimental days (Online Appendix D, Table D7),<sup>11</sup> we confirm that the initial effects are consistent with the main findings in Table 4. In addition, we carry out a daily panel analysis over the five experimental days, to account for the daily intraindividual and intertemporal heterogeneity. We also control for the previous reading behavior and demonstrate the robustness of our findings (Online Appendix D, Table D8).

4.5.7. Seasonality. To examine the potential impact of seasonality, we analyze the monthly distributions of genre consumption from January to September with a random sample of 1,294 consumers (Online Appendix B). Pairwise cosine similarities (mean � 0.994, SD � 0.003) show consistent distributions across the genres read over time, reinforcing the generalizability of the findings. Moreover, a subsample analysis excluding students who started school at the time of the experiment ensures generalizability to other consumer populations, such as the working professionals (Online Appendix D, Table D9).<sup>12</sup>

## 4.6. Online Survey

Although a thorough exploration of the potential mechanisms of the discovered effects of the (in)congruent schemes is beyond our scope, we strive to provide initial insights. Drawing on the relevant cognitive and psychological literature, we identify the key driving forces behind consumers’ responses to different schemes. On one hand, the Schema effect suggests that consumers prefer choices or information congruent with their existing preferences, as it offers familiarity and ease of information retrieval and processing (Pezdek et al. 1989, Schaper et al. 2019). This psychological mechanism helps explain why consumers prefer a congruent recommendation scheme. On the other hand, the Isolation effect posits that consumers may be drawn to surprises or changes that capture attention and facilitate memory encoding (Hunt and Lamb 2001). Hence, certain consu mers may benefit more from an incongruent scheme. To reconcile these two opposing forces, consumers who perceive a stronger Schema effect are more responsive to congruent schemes, whereas those more prone to a stronger Isolation effect favor incongruent schemes.

To explore these psychological drivers, we conduct an online survey. Specifically, we randomly assign 281 participants to either a congruent or incongruent scheme group using a between-subject design via the Credamo survey platform. These participants report comparable reading experiences and demographics as those in the main analysis. After designated survey questions, participants rate the Schema effect and the Isolation effect constructed from the established measures used in the literature (Schu¨ tzwohl 1998, Hunt and Lamb 2001, Manski 2004, Schaper et al. 2019, Buechel and Li 2023) (details in Online Appendix F).

We perform t-tests on the Likert scale responses. We confirm that consumers more responsive to the congruent scheme (i.e., willingness to read) are those more subject to the Schema effect (Q6: T3 > T4; p-value � 0.0003), whereas those preferring the incongruent scheme are more inclined toward the Isolation effect (Q7: T3 < T4; p-value < 0.0001). In summary, this survey provides additional insights into the potential mechanisms behind why the congruent scheme T4 is not always optimal for every consumer. It also sheds light on the mixed findings from the congruence literature regarding whether congruency or incongruency renders superior outcomes.

## 5. Conclusion

## 5.1. Summary of Key Findings

Designing effective recommender systems requires a deep understanding of consumer choice and incorporation of contextual insights. Grounded on behavioral theories and a large-scale randomized field experiment, our research highlights the importance of accounting for consumers’ ephemeral state and adaptive strategy-state pairing in digital content recommendations. We also uncover interesting consumer heterogeneities, revealing better performance of the incongruent scheme for certain consumer segments (e.g., with a more fluid or broader preference). Additionally, these state-dependent schemes demonstrate positive demand spillover onto the nonrecommended content, magnifying the value of the proposed framework to content platforms.

Although our findings demonstrate substantial promise, they represent a conservative estimate of the potential benefits. Extending deployment periods could better capture and accommodate dynamic consumer ephemeral states, potentially strengthening the effects and improving user experience. Our study integrates behavioral theory with recommender system design and advances the understanding of state dependency, underscoring the power of adaptive deployment strategies and nuanced personalization in digital content recommendations. It thus paves the way for future research to explore the broader implications of adaptive, behaviorinformed recommendation systems.

## 5.2. Theoretical Contributions

This research enriches the literature on recommendations, congruence, and demand spillover. It first introduces a theory-informed framework that integrates ephemeral state and strategy-state pairing into digital content recommendations. Analyses of a randomized field experiment uncover a preference for congruent statedependent recommendations, albeit with heterogeneity, enriching studies on choice dynamics and state dependency. In addition, the revealed consumer heterogeneity expands the literature on congruency by introducing a novel form of congruence and illuminating mixed findings regarding the superiority of congruence versus incongruence. Further, the discovered positive spillover toward nonrecommended offerings extends the literature on demand spillover in digital content recommendation, which has largely focused on assimilation strategies. It also indicates a potential undervaluation of state-dependent frameworks if such positive spillovers are left unaccounted for.

## 5.3. Managerial Implications

This research provides crucial strategic guidance to the multibillion-dollar digital content platforms. First, it quantifies the theoretical, practical, and economic values of employing flexible, adaptive, state-dependent recommendation schemes, illustrating the significant impacts on consumer engagement and platform profitability (by 7.3%). Second, this research uncovers interesting consumer heterogeneities, highlighting different optimal schemes for different consumer segments. Platforms should select either incongruent or congruent schemes for each individual, based on the stability and breadth of their preference, as well as their level of engagement. Third, our study reveals positive spillover onto nonrecommended contents, both within and across categories. This demonstrates that state-dependent schemes hold the potential to enrich experience, enhance satisfaction, and enact broader consumption beyond recommended offerings. For instance, the proposed scheme could enhance subsequent engagement for consumers who exhibit repetitive consumption patterns, hence indicative of fixation both within and across categories. Our study thus underscores the additional benefits of these adaptive, state-dependent frameworks and advocates for holistic valuations to fully materialize their promise.

We further highlight the potential generalizability of the proposed state-dependent framework, which imposes no constraints on specific recommendation algorithms. Our initial explorations using a simple, rule-based algorithm have already demonstrated its effectiveness, indicating that more sophisticated algorithms could yield even more profitable outcomes. Additionally, this framework is applicable to various digital content types beyond e-books, including images, videos, and audio on platforms like Instagram, Audible, YouTube, and Spotify. Importantly, platform managers should adapt the time window when defining the ephemeral state to align with context-specific consumption patterns—for instance, using a shorter window for YouTube videos compared with Audible books.

## 5.4. Limitations and Future Research

This research presents limitations that suggest avenues for future research. First, we focus on proposing a statedependent recommendation framework, with simple, rule-based algorithms as a starting point. Future research could explore more sophisticated recommendation algorithms across diverse industrial contexts, integrating additional consumer heterogeneities (e.g., price sensitivity, and mood). Second, our experiment identifies the aggregate effect of a recommendation scheme (i.e., strategy-state pairing) on a consumer. Future laboratory studies could further isolate the effect of each recommen dation scheme on each ephemeral state with a one-shot, instead of repeated, design. Third, future research could explore alternative measures and dimensions of ephem erality in diverse contexts. For example, although our use of genre to operationalize the ephemeral state renders a streamlined design and ease of implementation, future research may explore more granular measures to capture subtleties in content consumption. In addition, our current framework focuses on the ephemeral state of the active users. Future research could extend the framework by incorporating an “idle” state to account for inactive or occasional users. Fourth, further behavioral studies are needed to better understand the within- and acrosscategory demand spillover. Finally, we invite continued research on other aspects of recommender systems of value to content platforms, such as multiple-item recommendations, seasonality, culture, and longer-term effects of recommendations.

## Acknowledgments

The authors are grateful to the senior editor, Prof. Olivia Liu Sheng; the associate editor, Prof. Jingjing Zhang; and three anonymous reviewers for their helpful comments and suggestions. The authors also thank Prof. Peter Gray, as well as the participants of Conference on Digital Experi mentation 2021, the Harvard Data Science Workshop 2021, the University of Southern California Platform Competition Conference 2022, and Conference on Information Systems and Technology 2023 for their valuable feedback.

## Endnotes

<sup>1</sup> See Ankit Gupta, Digital Content Market Research Report, https:// www.marketresearchfuture.com/reports/digital-content-market-11516.

<sup>2</sup> Any suitable algorithm can be used to implement an assimilation or diversification recommendation strategy.

<sup>3</sup> We use state-dependent scheme and state-dependent framework interchangeably to refer to the strategy-state pairing.

<sup>4</sup> Related to recency, which emphasizes the time dimension (Larrain et al. 2015), ephemerality further highlights the transient nature of preference in digital content consumption (Kozinets 2002).

<sup>5</sup> We focus on revealed preference captured by historical data (Franke et al. 2009).

<sup>6</sup> C1 corresponds to the platform’s present practice. C2 employs the same diversification algorithm as in the treatment groups to maintain consistency. Yet, it is also grounded on the enduring, instead of ephemeral, preference.

<sup>7</sup> C2 is based on the enduring preference over the prior three months.

<sup>8</sup> For instance, if genres G1 and G2 are read during these seven days, whereas G1, G2, and G3 are read over the three months prior, excluding these most recent seven days, then preference stability � 1 because both G1 and G2 have been read before.

<sup>9</sup> According to the coefficients in Table C1: \$19.73 million � 365 days/year × \$0.002225 (i.e., \$0.0267/12 days) × 24.3 million paying customers.

<sup>10</sup> We choose 25% and 75% for a clean cutoff between two states. The results remain consistent with alternative thresholds tested.

<sup>11</sup> Note that focusing solely on the first day is not feasible due to the nature of our treatments (e.g., T1 and T3 being identical on day 1 only).

<sup>12</sup> We thank anonymous reviewers for suggesting these two analyses.

## References

Abraham M, Burbano V (2022) Congruence between leadership gender and organizational claims affects the gender composition of the applicant pool: Field experimental evidence. Organ. Sci. 33(1): 393–413.

Adomavicius G, Kwon Y (2014) Optimization-based approaches for maximizing aggregate recommendation diversity. INFORMS J. Comput, 26(2):351–369

Adomavicius G, Tuzhilin A (2005) Toward the next generation of recommender systems: A survey of the state-of-the-art and pos sible extensions. IEEE Trans. Knowl. Data Engrg. 17(6):734–749.

Adomavicius G, Bockstedt JC, Curley SP, Zhang J (2018) Effects of online recommendations on consumers’ willingness to pay. Inform. Systems Res. 29(1):84–102.

Amir O, Levav J (2008) Choice construction versus preference construction: The instability of preferences learned in context. J. Marketing Res. 45(2):145–158.

Andrews M, Luo X, Fang Z, Ghose A (2016) Mobile ad effectiveness: Hyper-contextual targeting with crowdedness. Marketing Sci. 35(2):218–233.

Ansari A, Li Y, Zhang JZ (2018) Probabilistic topic model for hybrid recommender systems: A stochastic variational Bayesian approach. Marketing Sci. 37(6):987–1008.

Bardhi F, Eckhardt GM (2017) Liquid consumption. J. Consumer Res. 44(3):582–597.

Bardhi F, Eckhardt GM, Arnould EJ (2012) Liquid relationship to possessions. J. Consumer Res. 39(3):510–529.

Belanche D, Casalo ´ LV, Flavia´n M, Iba´n˜ ez-Sa´nchez S (2021) Understanding influencer marketing: The role of congruence between influencers, products and consumers. J. Bus Res. 132(2021):186–195.

Bettman JR, Luce MF, Payne JW (1998) Constructive consumer choice processes. J. Consumer Res. 25(3):187–217.

Binkley S (2008) Liquid consumption: Anti-consumerism and the fetishized de-fetishization of commodities. Cultural Stud. 22(5): 599–623.

Boman L, Hewage GU, Hasford J (2020) The effect of emoji incongruency in social media: An abstract. Marketing Opportunities Challenges Changing Global Marketplace Proc. 2019 Acad. Marketing Sci. AMS Annu. Conf. (Springer International Publishing, Cham, Switzerland), 171–172.

Buechel EC, Li R (2023) Mysterious consumption: Preference for horizontal (vs. vertical) uncertainty and the role of surprise. J. Consumer Res. 49(6):987–1013.

Castells P, Hurley NJ, Vargas S (2021) Novelty and diversity in recommender systems. Ricci F, Rokach L, Shapira B, eds. Recom mender Systems Handbook (Springer, Boston), 881–918.

Chaney AJ (2021) Recommendation system simulations: A discussion of two key challenges. Preprint, submitted August 25, https://arxiv.org/abs/2109.02475.

Chaney AJ, Stewart BM, Engelhardt BE (2018) How algorithmic confounding in recommendation systems increases homogeneity and decreases utility. RecSys’18 Proc. 12th ACM Conf. Recom mender Systems (Association for Computing Machinery, New York), 224–232.

Che H, Sudhir K, Seetharaman PB (2007) Bounded rationality in pricing under state-dependent demand: Do firms look ahead, and if so, how far? J. Marketing Res. 44(3):434–449.

Chen Y, Harper FM, Konstan J, Li SX (2010) Social comparisons and contributions to online communities: A field experiment on MovieLens. Amer. Econom. Rev. 100(4):1358–1398.

Ching AT, Erdem T, Keane MP (2013) Learning models: An assess ment of progress, challenges, and new developments. Marketin Sci. 32(6):913–938.

Choi AA, Cho D, Yim D, Moon JY, Oh W (2019) When seeing help believing: The interactive effects of previews and reviews on e-book purchases. Inform. Systems Res. 30(4):1164–1183.

Chou TJ, Ting CC (2003) The role of flow experience in cyber-gam addiction. Cyberpsychol. Behav. 6(6):663–675.

Chung TS, Rust RT, Wedel M (2009) My mobile music: An adaptive personalization system for digital audio players. Marketing Sci. 28(1):52–68.

Cialdini RB, Trost MR, Newsom JT (1995) Preference for consistency: The development of a valid measure and the discovery of surprising behavioral implications. J. Personality Soc. Psych. 69(2):318.

Dai H, Milkman KL, Riis J (2014) The fresh start effect: Tempora landmarks motivate aspirational behavior. Management Sci. 60(10):2563–2582.

De Bruyn A, Liechty JC, Huizingh EK, Lilien GL (2008) Offering online recommendations with minimum customer input through conjoint-based decision aids. Marketing Sci. 27(3):443–460.

Deng J, Yang M, Pelster M, Tan Y (2024) Social trading, communica tion, and networks. Inform. Systems Res. 35(4):1546–1564.

Etkin J (2016) The hidden cost of personal quantification. J. Consumer Res. 42(6):967–984.

Fitzsimons GJ, Lehmann DR (2004) Reactance to recommendations: When unsolicited advice yields contrary responses. Marketing Sci. 23(1):82–94.

Fleder D, Hosanagar K (2009) Blockbuster culture’s next rise or fall: The impact of recommender systems on sales diversity. Management Sci. 55(5):697–712.

Fong NM, Fang Z, Luo X (2015) Geo-conquesting: Competitive loca tional targeting of mobile promotions. J. Marketing Res. 52(5): 726–735.

Fong N, Zhang Y, Luo X, Wang X (2019) Targeted promotions on an e-book platform: Crowding out, heterogeneity, and opportu nity costs. J. Marketing Res. 56(2):310–323.

Franke N, Keinz P, Steger CJ (2009) Testing the value of customization: When do customers really prefer products tailored to their preferences? J. Marketing 73(5):103–121.

Galak J, Kruger J, Loewenstein G (2013) Slow down! Insensitivity to rate of consumption leads to avoidable satiation. J. Consumer Res. 39(5):993–1009.

Ghose A, Ipeirotis PG, Li B (2012) Designing ranking systems for hotels on travel search engines by mining user-generated and crowdsourced content. Marketing Sci. 31(3):493–520.

Gomez-Uribe CA, Hunt N (2015) The Netflix recommender system: Algorithms, business value, and innovation. ACM Trans. Man agement Inform. Systems 6(4):13.

Gori M, Pucci A (2007) ItemRank: A random-walk based scoring algorithm for recommender engines. Sangal R, Mehta H, Bagga RK, eds. IJCAI’07 Proc. 20th Internat. Joint Conf. Artificial Intelli gence (Morgan Kaufmann Publishers, Inc., San Francisco), 2766-2771.

Goulding C, Shankar A, Elliott R, Canniford R (2009) The marketplace management of illicit pleasure. J. Consumer Res. 35(5):759–771.

Greve A, Cooper E, Tibon R, Henson RN (2019) Knowledge is power: Prior knowledge aids memory for both congruent and incongruent events, but in different ways. J. Experiment. Psych. Gen. 148(2):325.

Gu X, Kannan PK, Ma L (2018) Selling the premium in freemium. J. Marketing 82(6):10–27.

Gullo K, Berger J, Etkin J, Bollinger B (2019) Does time of day affect variety-seeking? J. Consumer Res. 46(1):20–35.

Guo L (2016) Contextual deliberation and preference construction. Management Sci. 62(10):2977–2993.

Hoch SJ, Loewenstein GF (1991) Time-inconsistent preferences and consumer self-control. J. Consumer Res. 17(4):492–507.

Huang Z, Liang Y, Weinberg CB, Gorn GJ (2019) The sleepy con sumer and variety seeking. J. Marketing Res. 56(2):179–196.

Hunt RR, Lamb CA (2001) What causes the isolation effect? J Experi ment. Psych. Learn. Memory Cognition 27(6):1359.

Jiang J, Ponnada A, Li A, Lacker B, Way SF (2024) A genre-based analysis of new music streaming at scale. WEBSCI’24 Proc. 16th ACM Web Sci. Conf. (Association for Computing Machinery, New York), 191–201.

Kaminskas M, Bridge D (2016) Diversity, serendipity, novelty, and coverage: A survey and empirical analysis of beyond-accuracy objectives in recommender systems. ACM Trans. Interactive Intelligent Systems 7(1):2.

Kozinets RV (2002) Can consumers escape the market? Emancipatory illuminations from burning man. J. Consumer Res. 29(1):20–38.

Kumar A, Hosanagar K (2019) Measuring the value of recommendation links on product demand. Inform. Systems Res. 30(3):819–838.

Kunaver M, Pozˇrl T (2017) Diversity in recommender systems—A survey. Knowledge-Based Systems 123(2017):154–162.

Larrain S, Trattner C, Parra D, Graells-Garrido E, Nørva˚ g K (2015) Good times bad times: A study on recency effects in collaborative filtering for social tagging. RecSys’15 Proc. 9th ACM Conf. Recommender Systems (Association for Computing Machinery, New York), 269–272.

Lawson SJ, Gleim MR, Hartline MD (2021) Decisions, decisions: Variations in decision-making for access-based consumption. J. Marketing Theory Practice 29(3):358–374.

Lee D, Hosanagar K (2019) How do recommender systems affect sales diversity? A cross-category investigation via randomized field experiment. Inform. Systems Res. 30(1):239–259.

Lee EJ, Schumann DW (2004) Explaining the special case of incon gruity in advertising: Combining classic theoretical approaches. Marketing Theory 4(1–2):59–90.

Lee D, Gopal A, Park SH (2020) Different but equal? A field experiment on the impact of recommendation systems on mobile and personal computer channels in retail. Inform. Systems Res. 31(3): 892–912.

Li SS, Karahanna E (2015) Online recommendation systems in a B2C E-commerce context: A review and future directions. J. Assoc. Inform. Systems 16(2):2.

Li P, Tuzhilin A (2024) When variety seeking meets unexpectedness: Incorporating variety-seeking behaviors into design of unexpected recommender systems. Inform. Systems Res. 35(3):1257–1273.

Li X, Grahl J, Hinz O (2022) How do recommender systems lead to consumer purchases? A causal mediation analysis of a field experiment. Inform. Systems Res. 33(2):620–637.

Liang C, Shi Z, Raghu TS (2019) The spillover of spotlight: Platform recommendation in the mobile app market. Inform. Systems Res. 30(4):1296–1318

Linden G, Smith B, York J (2003) Amazon.com recommendations: Itemto-item collaborative filtering. IEEE Internet Comput. 7(1):76–80

Lu S, Xiao L, Ding M (2016) A video-based automated recommender (VAR) system for garments. Marketing Sci. 35(3):484–510.

Luo X, Andrews M, Fang Z, Phang CW (2014) Mobile targeting. Management Sci. 60(7):1738–1756.

Manski CF (2004) Measuring expectations. Econometrica 72(5):1329–1376.

McAlister L, Pessemier E (1982) Variety seeking behavior: An inter disciplinary review. J. Consumer Res. 9(3):311–322.

Miner JB, Crane DP, Vandenberg RJ (1994) Congruence and fit in professional role motivation theory. Organ. Sci. 5(1):86–97.

Mitchell DJ, Kahn BE, Knasko SC (1995) There’s something in the air: Effects of congruent or incongruent ambient odor on consumer decision making. J. Consumer Res. 22(2):229–238.

Morozov I, Tuchman A (2024) Where does advertising content lead you? We created a bookstore to find out. Marketing Sci. 43(5): 925–1151.

Mousavi N, Adamopoulos P, Bockstedt J (2023) The decoy effect and recommendation systems. Inform. Systems Res. 34(4):1533–1553.

Nadler DA, Tushman ML (1980) A model for diagnosing organiza tional behavior. Organ. Dynam. 9(2):35–51.

Narasimhan C, Turut O <sup>¨</sup> (2013) Differentiate or imitate? The role of context-dependent preferences. Marketing Sci. 32(3):393–410.

Oestreicher-Singer G, Sundararajan A (2012) The visible hand? Demand effects of recommendation networks in electronic markets. Management Sci. 58(11):1963–1981.

Panniello U, Gorgoglione M, Tuzhilin A (2016) Research note—In CARSs we trust: How context-aware recommendations affect customers’ trust and other business performance measures of recommender systems. Inform. Systems Res. 27(1):182–196.

Payne JW, Bettman JR, Johnson EJ (1993) The Adaptive Decision Maker (Cambridge University Press, Cambridge, UK).

Peng J, Liang C (2023) On the differences between view-based and purchase-based recommender systems. MIS Quart. 47(2):875–900.

Peng CH, Yin D, Zhang H (2020) More than words in medical question-and-answer sites: A content-context congruence perspective. Inform. Systems Res. 31(3):913–928.

Pezdek K, Whetstone T, Reynolds K, Askari N, Dougherty T (1989) Memory for real-world scenes: The role of consistency with schema expectation. J Experiment. Psych. Learn. Memory Cogni tion 15(4):587.

Ratner RK, Kahn BE (2002) The impact of private versus public con sumption on variety-seeking behavior. J. Consumer Res. 29(2): 246–257.

Rigby D, Burton M, Pluske J (2016) Preference stability and choice consistency in discrete choice experiments. Environ. Resource Econom. 65(2):441–461.

Rindfleisch A, Burroughs JE, Wong N (2009) The safety of objects: Materialism, existential insecurity, and brand connection. J. Consumer Res. 36(1):1–16.

Salisbury LC, Feinberg FM (2012) All things considered? The role of choice set formation in diversification. J. Marketing Res. 49(3): 320–335.

Schaper ML, Kuhlmann BG, Bayen UJ (2019) Metamemory expectancy illusion and schema-consistent guessing in source monitoring. J. Experiment. Psych. Learn. Memory Cognition 45(3): 470–496.

Schu¨ tzwohl A (1998) Surprise and schema strength. J. Experiment. Psych. Learn. Memory Cognition 24(5):1182–1199.

Schweidel DA, Moe WW (2016) Binge watching and advertising. J Marketing 80(5):1–19.

Shaddy F, Fishbach A, Simonson I (2021) Trade-offs in choice. Annual Rev. Psych. 72(1):181–206.

Simonov A, Dube ´ J-P, Hitsch G, Rossi P (2020) State-dependent demand estimation with initial conditions correction. J. Market ing Res. 57(5):789–809.

Song Y, Sahoo N, Ofek E (2019) When and how to diversify—A multicategory utility model for personalized content recommendation. Management Sci. 65(8):3737–3757.

Trijp HCV, Hoyer WD, Inman JJ (1996) Why switch? Product category–level explanations for true variety-seeking behavior. J Marketing Res. 33(3):281–292.

Wan X, Kumar A, Li X (2024a) How do product recommendations help consumers search? Evidence from a field experiment Management Sci. 70(9):5776–5794.

Wan X, Kumar A, Li X (2024b) Retargeted versus generic product recommendations: When is it valuable to present retargeted recommendations? Inform. Systems Res. 35(3):1403–1421.

Weiss L, Johar GV (2016) Products as self-evaluation standards: When owned and unowned products have opposite effects on self-judgment. J. Consumer Res. 42(6):915–930.

Xiao B, Benbasat I (2007) E-commerce product recommendation agents: Use, characteristics, and impact. MIS Quart. 31(1):137–209.

Yin K, Fang X, Chen B, Liu Sheng OR (2023) Diversity preference aware link recommendation for online social networks. Inform. Systems Res. 34(4):1398–1414.

Yoon HJ (2013) Understanding schema incongruity as a process in advertising: Review and future recommendations. J. Marketin Commun. 19(5):360–376.

Copyright of Information Systems Research is the property of INFORMS: Institute for Operations Research & the Management Sciences and its content may not be copied or emailed to multiple sites without the copyright holder's express written permission. Additionally, content may not be used with any artificial intelligence tools or machine learning technologies. However, users may print, download, or email articles for individual use.
