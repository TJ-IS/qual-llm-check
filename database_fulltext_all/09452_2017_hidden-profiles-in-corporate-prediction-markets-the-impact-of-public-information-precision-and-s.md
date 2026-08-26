---
otero_id: 9452
otero_key: "32E665DK"
title: "Hidden Profiles in Corporate Prediction Markets: The Impact of Public Information Precision and Social Interactions1"
authors: "Liangfei Qiu; Hsing Kenneth Cheng; Jingchuan Pu"
year: "2017"
journal: "MIS Quarterly"
doi: "10.25300/misq/2017/41.4.11"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# HIDDEN PROFILES IN CORPORATE PREDICTION MARKETS: THE IMPACT OF PUBLIC INFORMATION PRECISION AND SOCIAL INTERACTIONS<sup>1</sup>

Liangfei Qiu Warrington College of Business, University of Florida, Gainesville, FL 32611 U.S.A. {liangfeiqiu@ufl.edu}

Hsing Kenneth Cheng

Warrington College of Business, University of Florida, Gainesville, FL 32611 U.S.A. {hkcheng@ufl.edu} and School of Information Management and Engineering, Shanghai University of Finance and Economics, Shanghai, CHINA

Jingchuan Pu

Warrington College of Business, University of Florida, Gainesville, FL 32611 U.S.A. {jingchuan@ufl.edu}

Recently, large companies have been experimenting with corporate prediction markets run among their employees. In the present study, we develop an analytical model to analyze the effects of information precision and social interactions on prediction market performance. We find that increased precision of public information is not always beneficial to the prediction market accuracy because of the “hidden profiles” effect: the information-aggregation mechanism places a larger-than-efficient weight on existing public information. We show that a socially embedded prediction market with information sharing among participants may help correct such inefficiency and improve prediction market performance. We also identify conditions under which increased precision of public information is detrimental in a nonnetworked prediction market and in a socially embedded prediction market. These results should be of interest to practitioners as the managerial implications highlight the detrimental effect of public information and the role of social networking among employees in a corporate prediction market.

Keywords: Prediction markets, social networks, public information, information sharing, hidden profiles

Prediction markets comprising a diverse set of consumers can be valuable tools for companies spanning a wide range of industries and at every stage in the product or service life cycle and be used for: narrowing the new-product development funnel; concept testing; forecasting; pricing; message optimization; and promotion testing.

— Julie Schlack, Senior Vice President at Communispace<sup>2</sup>

Actors do not behave or decide as atoms outside a social context. — Granovetter (1985, p. 487)

## Introduction

How to take advantage of the knowledge dispersed in various parts of their organizations for better decision making has been a persistent challenge for large corporations. Lew Platt, the former chief executive of Hewlett-Packard, observed that, “if only HP knew what HP knows, we would be three times more productive.”<sup>3</sup> Enterprise collective intelligence isn’t about changing a specific industry, but rather revolutionizing the nature of how businesses operate and changing the landscape of corporate decision making. In the classic commandand-control model of businesses, corporate decision making is generally hierarchical. The manager of each business department is responsible for acquiring all information from that department, synthesizing it, and making decisions or reporting it up the chain of command. While this approach can sometimes lead to an optimal quantity and quality of information reaching the corporate decision maker, it also has a significant informational problem: The information necessary to make a decision can be filtered or distorted in the hierarchy (Abaramowicz and Henderson 2007).

An alternative model of decision making is to facilitate the flow of information around the hierarchy by tapping into and exploiting the collective intelligence within the organization. A common application of corporate collective intelligence is a prediction market—a speculative or betting market that invites participants to speculate on uncertain future events. It works similarly to a financial market. A risky asset is defined as reflecting an issue of interest to the company such as the product’s readiness to launch and sales trends of a new product. Prediction market prices have informational value because they aggregate the beliefs of market participants and reveal what the market’s overall forecasts are.

Companies have made increasing use of prediction markets to help make business decisions. As documented in Chen and Plott (2002), Cowgill et al. (2009), and Cowgill and Zitzewitz (2015), a number of companies in a broad range of industries, such as Hewlett-Packard, Intel, BestBuy, Microsoft, Ford, Chrysler, Google, Eli Lilly, General Electric, and Siemens, have begun experimenting with corporate prediction markets. The prediction tasks vary from drug development success at Eli Lilly<sup>4</sup> to monthly operating profits and revenues at Hewlett-Packard (Chen and Plott 2002); from a project completion date at Siemens (Leigh and Wolfers 2007) to allocation of manufacturing capacity at Intel (Hopman 2007); and from weekly vehicle sales at Ford (Montgomery et al. 2013) to the number of Gmail users at Google (Cowgill et al. 2009). Early evidence on the performance of corporate prediction markets has been encouraging: Similar successes have been repeatedly observed in many corporate prediction markets, and the prediction markets outperform existing mechanisms in terms of forecasting precision.

A fundamental innovation of corporate prediction markets is to introduce a collaborative market mechanism to augment the hierarchical decision-making process and improve overall decision quality. Essentially, a prediction market is a smart market system that can provide decision support in complex environments (Bichler et al. 2010). Coase (1937) explained that the existence of firms is driven by the fact that the benefits of hierarchy and command-and-control exceed the transaction costs. Prediction markets have the potential to profoundly reduce the costs of hierarchy by allowing information to flow to top decision makers (Abaramowicz and Henderson 2007). CEOs and high-ranking managers are tasked with filtering and analyzing information; however, the data that they receive is also filtered (and distorted) by their subordinates. The social pressures within a company may lead some employees to conform to existing public information, such as official reports or the opinion of some highranking managers, although these employees may have valuable information to share—an effect known as “hidden profiles” (Stasser and Titus 1985; Stasser and Titus 2003; Sunstein 2005). The original idea of the hidden profile effect describes a biased pattern of information distribution in which some information, prior to group discussion, is shared by all group members (public information), and some is unique to individual members (private information). Group members often fail to effectively pool their information because discussions tend to be dominated by public information that members hold before the discussion. In other words, hidden profile refers to the phenomenon of overweighting public information in general, and it can arise from different sources. Prendergast (1993) proposed an economic theory of “yes men,” where employees have an economic incentive to conform to the opinion of their supervisors. Therefore, one potential source of hidden profile is that individual employees tend to place a larger weight on existing public information than justified by its informational content when they report their opinions to upper-level decision makers in corporate hierarchy.

Prior literature argued that a prediction market can help alleviate the hidden profile effect—the overreaction of corporate decision making to existing public information (Abaramowicz and Henderson 2007). The basic logic is as follows: In a corporate prediction market, employees would have incentives to correct the conformity and overreaction to public information, especially if they can trade anonymously. As highlighted by Bo Cowgill, a Google economic analyst, the anonymous trading system in prediction markets lets the Google hierarchy discover its employees’ uncensored opinions.

If you let people bet on things anonymously, they will tell you what they really believe because they have money at stake. This is a conversation that’s happening without politics. Nobody knows who each other is, and nobody has any incentive to kiss up.<sup>5</sup>

Consequently, the use of corporate prediction markets can help decision makers reduce the possibility that errors propagate through the hierarchy all the way to the top, as individual employees who dissent from an official report would have a financial incentive to trade against the official report. The market approach with the protection of anonymity gives a voice to internal employees who otherwise would be affected by hidden profiles or yes men due to various pressures or expected costs from speaking out.

However, can a corporate prediction market completely solve the problem of overweighting public information? In this paper, we develop an analytical model of market trading to analyze the impact of information quality on prediction market performance. As defined in prior literature (Angeletos and Pavan 2007; Chen and Jiang 2006; Morris and Shin 2002), we differentiate between two types of information within an organization according to the way the information is generated: (1) public information that is common to all prediction market participants, such as official company reports, and (2) private information that can be accessed only by individual employees, such as tacit knowledge from their working experience. Although prediction market participants place individually optimal Bayesian weights on both public and private information in our model, we find that a prediction market can cause another type of hidden profile effect: The information-aggregation mechanism in a corporate prediction market will place a larger (less) than efficient weight on public (private) information. This result suggests that even if the effect of hidden profiles at the individual level can be corrected by a corporate prediction market, the informationaggregation mechanism (market mechanism) can be another source of the hidden profile effect (the problem of overweighting public information).

A key assumption of our model is that a prediction market participant lacks the ability to extract other participants’ information from market prices. Because of this bounded rationality, a corporate prediction market will place a larger-thanefficient weight on public information. Essentially, our model is different from the efficient market literature (Malkiel and Fama 1970) in how a competitive market serves to communicate information between the market participants. The classic efficient market assumption states that the equilibrium price aggregates all the available information in the market perfectly, and participants have unlimited cognitive abilities to process information (Grossman 1976, 1978; Malkiel and Fama 1970). However, if the equilibrium price really aggregates all the available information perfectly as Grossman (1976, 1978) suggested, participants will neglect their own private information because it is useless. According to this logic, it is unclear why the price should reflect the private information in the first place (Hellwig 1980). A number of empirical studies in finance also show that a competitive market does not aggregate information as efficiently as we expect (Bondt and Thaler 1985; Jensen 1978; Shiller 1981). Our study relaxes the assumption that the equilibrium price aggregates information perfectly by introducing more realistic constraints on participants’ information-processing abilities.

Another key finding of our research is that increased precision of private information always enhances prediction market performance as expected, but, surprisingly, increased precision of public information is detrimental to the prediction market performance when public information is relatively noisy. An intuitive explanation is that the presence of public information might have a distortive effect on the prediction market price formation. All prediction market participants receive the same public information. As such, each participant will form her best guess according to her own private information as well as the same public information. In the process of aggregating all participants’ best guesses, a corporate prediction market mechanism will count the public information multiple times. Therefore, the aggregated prediction market forecast will overreact to the public information, and any noise contained in the public information will be magnified.

Of greater importance, we uncover the specific mechanism through which the problem of overweighting the public information might be mitigated, which is an issue unaddressed by the extant literature. In particular, social interactions and information sharing among prediction market participants may help correct the overreaction to public information. Actually, a distinct feature of a corporate prediction market versus a public prediction market, such as Iowa Electronic Markets (Berg et al. 2008), is that internal employees are more likely to be socially connected: They can exchange information with each other through personal networks and social relations, which are important conduits of knowledge (Qiu et al. 2014a, 2014b).<sup>6</sup>

As social media technologies have grown explosively, employees are increasingly using public social media platforms such as Twitter, Facebook, and LinkedIn for work-related purposes (Parise et al. 2015). Many companies, such as 7-Eleven, Capital One, and Dow Chemical, have developed their own in-house corporate platforms to promote social networking among employees (Mello 2014). Knowledge sharing in knowledge networks becomes much more common in today’s digitally connected world (Hansen 2002). Therefore, beyond a nonnetworked corporate prediction market with independent bettors, we examine a model of a socially embedded prediction market, in which participants can share information with their social connections.

In our study, we highlight that public information is a doubleedged instrument in a prediction market. It conveys information on the fundamentals of the asset traded in the prediction market, but on the other hand, the noisiness of public information can be enhanced in the prediction market due to the overreaction to the disclosure of public information. Corporate managers should be aware that increased precision of public information might have a detrimental effect on the aggregation of information into prediction market prices. Our results on socially embedded prediction markets further illustrate the complex interaction between private and public information.

## Literature Review

The literature on prediction market design has been growing rapidly in recent decades (e.g., Berg et al. 2009; Cowgill and Zitzewitz 2015; Fang et al. 2007, 2010; Guo et al. 2006; Healy et al. 2010; Jian and Sami 2012; Van Bruggen et al. 2010). Most of these studies, explicitly or implicitly, assumed that prediction market participants are isolated in the sense that they cannot communicate their private information with each other. As we have stated, in a corporate internal prediction market, participants are more likely to be socially connected. Although a handful of recent empirical studies have begun considering socially embedded prediction markets (Cowgill et al. 2009; Qiu et al. 2014a), analytical analysis is limited in this area. To bridge this research gap, our work provides a modeling framework to understand the role of information precision in a socially embedded prediction market, and to improve the design of corporate prediction markets.<sup>7</sup>

Our work is more broadly related to the literature on the wisdom of crowds. An intriguing question is about the boundary conditions of crowd wisdom: When is a crowd wise? In an analytical model, Golub and Jackson (2010) showed that whether a crowd is wise depends critically on the structure of social networks. Lorenz et al. (2011) studied a forecast-report context in which the crowd prediction is a linear combination of all individuals’ predictions, and found experimental evidence that sharing information among individuals may undermine the wisdom of crowd effect. In a similar context, Davis-Stober et al. (2015) demonstrated how to create optimal forecasting groups. In the context of expertsystems design, Jiang et al. (2005) considered a sequential information gathering problem in which input data may be distorted by system users. The optimal design of other smart systems, such as internal knowledge investment (Ba et al. 2001), consumer contests (Liu et al. 2007), consumer review systems (Jiang and Guo 2015), and dynamic electricity trading systems (Ketter et al. 2016a, 2016b), has also been widely examined in the literature. Our model focuses on a specific form of the wisdom of crowds: a prediction market in which the forecast is generated from market prices using a security-trading mechanism.

Recent empirical studies in finance documented evidence that social networks play an important role in financial markets (Cohen et al. 2008; Coval and Moskowitz 2001). A stream of analytical studies showed that social communications among traders improve market efficiency (Colla and Mele 2010; Han and Yang 2013; Ozsoylev and Walden 2011). Our work differs from theirs for two reasons. First, in our study, we focus on the role of public information in a nonnetworked prediction market versus a socially embedded prediction market. Although Han and Yang (2013) pointed out that increased precision of private information improves price informativeness, none of these studies have considered the detrimental effect of public information. Our analytical results complement their research and highlight that the effect of information precision on market efficiency depends on the way the information is generated. Increased precision of private information always enhances prediction market performance regardless of whether a social network is embedded, but increased precision of public information could be detrimental under some market conditions. Second, this stream of studies adopted the large economy analysis by assuming the number of market participants is infinity, and investigated the asymptotic properties of an equilibrium. This approach is well defined and valid in financial markets. However, unlike a financial market or a public prediction market, a thin market is an important feature of a corporate prediction market because of confidentiality reasons. There is often a need to limit participation for prediction topics with strategic importance (Cowgill and Zitzewitz 2015). Therefore, our model focuses on the case that the number of prediction market participants is limited. We demonstrate that the number of prediction market participants has a significant impact on when increased precision of public information is more likely to be detrimental.<sup>8</sup>

Following the prior finance literature on difference of opinions (DO), in our model, we assume that prediction market participants do not condition on prices to infer private information of others. The DO behavior can be explained by (1) behavioral biases such as bounded rationality and limited attention, or by (2) heterogeneous priors among rational agents (Banerjee et al. 2009; Banerjee and Kremer 2010). From a perspective of behavioral biases, Hong and Stein (1999) proposed a DO model to explain the momentum phenomenon in financial markets. Hong and Stein (2003) developed an analytical framework of market crashes based on difference of opinions among investors.<sup>9</sup> Scheinkman and Xiong (2003) used overconfidence as a source of difference of opinions to examine speculative bubbles in asset prices. Banerjee et al. (2009) showed that difference of opinions is necessary to generate price drift, which is an empirical regularity in financial markets.

From a perspective of heterogeneous priors, early studies used the DO approach to avoid the No Trade theorem resulting from rational expectations, and to generate positive trading volume in analytical models (Harris and Raviv 1993; Harrison and Kreps 1978; Kandel and Pearson 1995). They demonstrated that DO can generate trading patterns consistent with stylized empirical evidence. Cao and Ou-Yang (2009) analyzed the effects of DO on the dynamics of trading volume in stocks. Banerjee and Kremer (2010) developed a dynamic DO model to generate positive autocorrelation in trading volume.

Our paper differs from the prior DO studies in several aspects. First, the previous DO literature has mainly focused on using DO to explain a number of empirical features of price and volume dynamics in financial markets, such as momentum and positive autocorrelation in trading volume. However, our paper focuses on prediction market accuracy—specifically, the impact of public information on prediction market accuracy in the DO framework. Second, a few studies have noticed that the problem of overweighting public information can be caused by the DO framework, and the overweight issue is the underlying driving force of some empirical regularities in financial markets, such as price drift (e.g., Banerjee et al. 2009). However, as far as we know, none of these studies have examined the following key results on the optimal design of prediction markets in our work: (1) increased precision of public information is not always beneficial to prediction market accuracy and can be detrimental when public information is relatively noisy; (2) social networks among employees help correct the problem of overweighting public information and improve prediction market accuracy; (3) the social network, however, has a side effect. As the level of social interaction increases, increased precision of public information may be more likely to be detrimental under some market conditions; and (4) although social interactions can correct the overweighting problem, the homophily effect (the errors of friends’ private signals are positively correlated) tends to weaken the correction because friends’ information is less useful under homophily.

Our study is also related to social psychology literature on hidden profiles. The implication from the prior psychology experiments is that individuals tend to attach a larger weight to shared common information than justified by its informational content in their decision-making process (Stasser and Titus 1985, 2003). A stream of economics literature on the role of public information (Angeletos and Pavan 2007; Morris and Shin 2002) found a similar result when individuals have coordination motives using analytical models.<sup>10</sup> Instead of focusing on the effect of hidden profiles in the individual level, our model digs deeper into the overweighting problem of the information-aggregation mechanism (the effect of hidden profiles) in prediction markets: Even if there is no distortion in the individual level, the problem of overweighting the public information can be caused by the prediction market mechanism itself. In our model, the social value of network communications is to alleviate the overreaction of prediction market prices to the public information.

## A Benchmark Nonnetworked Prediction Market

## Model Setup

In a corporate prediction market, assets are created whose final value is tied to a particular event—for example, the sale of a new product. People trade the assets according to their forecasts. Specifically, in our model, people trade a single asset according to the outcome of a future random variable, V. A manager wants to forecast $V ,$ and she resorts to n prediction market participants (internal employees) to obtain an accurate prediction. Table 1 provides a list of the notations used in our model.

All the prediction market participants share a common prior on V, given by

$$
V \sim N (V _ {0}, 1 / \rho_ {V})
$$

where $V _ { 0 }$ is the mean of the prior, and $\rho _ { \nu }$ is the precision of the prior. Before the prediction market opens, each participant can access a private signal

$$
S _ {i} = V + \varepsilon_ {i}, \varepsilon_ {i} \sim N (0, 1 / \rho_ {\varepsilon}). \varepsilon_ {i} \perp \varepsilon_ {j}\tag{1}
$$

where $\rho _ { \varepsilon }$ is the precision of participant $i ^ { \circ } \mathrm { s }$ information source for $i = 1 , 2 , . . . , n . ^ { 1 1 }$ The signals’ errors are independent across participants and are also independent of V. In this nonnetworked benchmark model, we assume that each participant accesses a private independent signal and does not communicate with each other.<sup>12</sup> Then, in later sections, we relax this assumption, and allow communication among friends and correlated private signal errors (homophily).<sup>13</sup>

We provide a running example of corporate prediction markets to show how our model setups are tied to reality, as follows: In the business practice, the random variable V could refer to the next month’s sales of a product or the following quarter’s monthly sales of a product (Chen and Plott 2002). At Google or Ford, there is a prediction market associated with every event they are trying to predict, such as the growth rate of Gmail users at Google (Cowgill et al. 2009) or sales volumes for selected Ford models (Montgomery et al. 2013).

The common prior can be interpreted as the existing public information available to prediction market participants. Many projects at Google had “dashboards,” or online summaries of

<table><tr><td colspan="2">Table 1. Summary of Notations</td></tr><tr><td>Notation</td><td>Description</td></tr><tr><td> $V$ </td><td>A random future event that will be forecasted in a corporate prediction market</td></tr><tr><td> $S_i$ </td><td>Each individual&#x27;s private signal</td></tr><tr><td> $\varepsilon_i$ </td><td>The noise contained in the private signal</td></tr><tr><td> $V_0$ </td><td>The mean of the common prior (public information)</td></tr><tr><td> $\rho_V$ </td><td>The precision of public information</td></tr><tr><td> $\rho_\varepsilon$ </td><td>The precision of private information</td></tr><tr><td> $n$ </td><td>The number of prediction market participants</td></tr><tr><td> $x_i$ </td><td>Each individual&#x27;s trading position in a prediction market</td></tr><tr><td> $\pi_i$ </td><td>Each individual&#x27;s trading profits</td></tr><tr><td> $I_i$ </td><td>Each individual&#x27;s information set</td></tr><tr><td> $k$ </td><td>The number of friends each participant has in a regular network</td></tr><tr><td> $a_0$ </td><td>The proportion of degree 0 participants</td></tr><tr><td> $N_i(g)$ </td><td>The set of individual i&#x27;s friends</td></tr><tr><td> $\gamma$ </td><td>Risk averse parameter</td></tr><tr><td> $\delta$ </td><td>Correlation coefficient under homophily</td></tr><tr><td> $m$ </td><td>The number of participants that use the DO approach to make inferences</td></tr></table>

project status. These dashboards are typically visible to all Google employees and can be treated as public information. If Google contains a prediction market related to a project that has a dashboard, the prediction market webpage includes a link to the dashboard (Coles et al. 2007). Actually, many high-tech companies use dashboards to track project status. Private signals reflect the diverse information that can be assessed by internal employees in their daily work. For instance, if data analysts in a company’s marketing department are asked to predict future sales of a product, they may have different information sources from their working experience.<sup>14</sup> The private signal in Google’s prediction markets refers to information only available to a small number of individuals or personal interpretations. For instance, a manager on the search quality team at Google mentioned that she had private information when a prediction market was related to her own projects. Another Google prediction market participant said “the one time I thought I had good (private) information on a Google project, where there was a market I traded like crazy on $\mathrm { i t } ^ { \dag }$ (Coles et al. 2007, p. 12).

In a competitive security-trading prediction market, participants trade anonymously, taking prices as given. Participant $i ^ { \circ } \mathrm { s }$ profits are given by $\pi _ { i } = ( V - P ) x _ { i } ,$ where P is the prediction market price of the risky asset tied to $V ,$ and $x _ { i }$ is the demand for the security of participant i. $\operatorname { I f } x _ { i } > 0 .$ , participant i holds a positive position in the risky asset; i $\dot { \boldsymbol { x } } _ { i } < 0 ,$ participant i shorts the risky asset. We further assume that participant i’s preferences over random profits are described by a mean-variance utility function, which has been widely adopted in the economics and finance literature (Aid et al. 2011; Levy and Markowitz 1979). Therefore, participant i is risk averse, and her utility depends on the expected profits as well as the variance of the random profits.

$$
\mathbf {E} [ \pi_ {i} ] - \gamma \mathbf {V A R} [ \pi_ {i} ]\tag{2}
$$

where $\gamma$ is a parameter that captures the risk aversion of participants. If γ is larger, participants are more risk averse. Following the finance literature (e.g., Cespa and Vives 2015), we assume all participants share the same risk aversion parameter γ to simplify the calculation.

Our benchmark model is a two-date static model. Following the standard timeline setup in the finance literature (Banerjee et al. 2009; Cespa and Vives 2015; Grossman and Stiglitz 1980; O’Hara 1995), we describe the timeline of our model as follows: At time 1, prediction market participants receive private signals and trade the risky asset. The market price of the asset and the trading position of each individual are simultaneously determined. At time 2, the random variable V is realized.<sup>15</sup>

According to equation 2, participant i’s optimization problem of choosing the optimal quantity becomes

$$
\max _ {x _ {i}} \mathbf {E} \big [ (V - P) x _ {i} | I _ {i} \big ] - \gamma \mathbf {V a r} \big [ (V - P) x _ {i} | I _ {i} \big ]\tag{3}
$$

where $I _ { i }$ is the information set of participant i. The first order condition (F.O.C) yields

$$
x _ {i} ^ {*} = \frac {\mathbf {E} [ V | I _ {i} ] - P}{2 \gamma \mathbf {V a r} [ V | I _ {i} ]}\tag{4}
$$

In the prior finance literature, there are two major paradigms for modeling the inference process in financial markets (what the information set I should contain) rational expectation equilibrium (REE) and DO. Both approaches share the view that investors have different valuations, and prices aggregate the different views during the trading process. The difference between the REE and DO models is in the information set of participants, $I _ { i \cdot } \quad ^ { \epsilon } \mathrm { I n }$ an REE, an agent conditions both on the private signal and the price vector. In the DO model, however … each agent conditions only on his or her private signal” (Banerjee et al. 2009, p. 3712). Specifically, the REE approach implies that participants are able to learn from the price: the quantity they demand for a given price depends on the information the price reveals about the value of the asset (Cespa and Vives 2015; Grossman and Stiglitz 1980; O’Hara 1995). The information set under REE should include the private signal as well as the expected price, $I _ { i } = \{ S _ { i } , P ^ { * } \}$ . In contrast, the DO approach assumes that participants are not as sophisticated as REE participants, and they do not learn from the information contained in market price. The information set under DO includes only the private signal, $I _ { i } = \{ S _ { i } \}$

Next, we look at a pure DO model where all participants do not learn from the information contained in market price. The reality of corporate prediction markets is likely to be neither as efficient as in an REE nor as inefficient as in a pure DO equilibrium, but somewhere in between. Therefore, in the subsequent section, we develop a mixture model that nests both the REE and DO approaches: among total n participants, m participants use the DO approach to make inferences (they do not learn from the expected price), and n – m participants use the REE approach to make inferences (they are sophisticated traders and learn from the expected price). This modeling setup captures the heterogeneity of participants in cognitive capabilities. $\operatorname { I f } m = n$ , the model converts to a pure DO model; if $\dot { m } = 0 ;$ , the model converts to a pure REE model.

## A DO Model of a Nonnetworked Prediction Market

We first look at a pure DO model of prediction markets for two reasons. First, as documented in the prior literature (Banerjee et al. 2009), the appeal of DO models is that the predictions from DO models are consistent with real-world empirical evidence in financial markets. For instance, a typical feature of REE in financial markets is the no trade theorem (Tirole 1982): no trader expects a positive monetary gain from his trade; thus, the trading volume is zero. The intuition of this theorem is that in the REE framework (traders are completely rational), if one participant has information that induces her to want to trade at the current asset price, then other rational participants would be unwilling to trade with her, because they realize that she must have superior information. The no-trade result derived from the REE framework is not consistent with the empirical evidence observed in real-world corporate prediction markets (Cowgill and Zitzewitz 2015; Montgomery et al. 2013): Participants actively trade in corporate prediction markets. In contrast, the DO models do not generate the no-trade result and are consistent with the observed evidence. The empirical literature in financial markets (Banerjee and Kremer 2010) has documented that a number of regularities on observed levels and patterns of trading volume are difficult to reconcile in standard REE models (even in noisy REE models). In contrast, the DO framework appears better suited to address the empirical evidence involving trading volume (Banerjee and Kremer 2010). Broadly, Lovell (1986) summarized a number of empirical studies challenging the validity of rational expectation hypothesis in contexts other than financial markets.

Second, prediction market participants in our context are corporate employees, not professional traders in financial markets. For instance, an active trader in Google’s prediction markets admitted: “I never play the real-world stock market” (Coles et al. 2007, p. 12). Therefore, they may not be as sophisticated as professional traders who can learn from the information contained in the expected price. Essentially, REE requires extraordinary analytical and computational capabilities for a fully rational approach. It is highly impractical and cognitively demanding for non-professional traders in prediction markets to learn from the information contained in the expected price and to do the required calculations. The DO paradigm can be motivated by behavioral biases, such as bounded rationality (Banerjee and Kremer 2010), and this approach is more appropriate in our corporate prediction market context.

In a pure DO model, each participant makes a Bayesian inference using her private signal and the common prior

$$
\begin{array}{r} \mathbf {E} [ V | I _ {i} ] = \mathbf {E} [ V | S _ {i} ] = \frac {\rho_ {V}}{\rho_ {\varepsilon} + \rho_ {V}} V _ {0} + \frac {\rho_ {\varepsilon}}{\rho_ {\varepsilon} + \rho_ {V}} S _ {i}, \\ \mathbf {V a r} [ V | I _ {i} ] = 1 / (\rho_ {\varepsilon} + \rho_ {V}) \end{array}
$$

Essentially, participant i’s conditional expectation, E[V|I ], is a weighted average of the prior mean and her private signal. Note that $\frac { \rho _ { V } } { \rho _ { \varepsilon } + \rho _ { V } }$ is the Bayesian weight given to public information, and $\frac { \rho _ { \varepsilon } } { \rho _ { \varepsilon } + \rho _ { V } }$ is the weight given to private information. We close the model by imposing the market clearing condition, which determines the prediction market price $P \colon$ $\textstyle \sum _ { i = 1 } ^ { n } x _ { i } ^ { * } = 0 .$ , where n is the number of participants in the prediction market. The market clearing condition simply means that the sum of each participant’s position should be equal to zero. We assume n is a limited number. However, our model can be easily extend to the case of $n  \infty$

We characterize the benchmark equilibrium without social networks when participants are allowed to trade assets in a competitive prediction market in the following proposition. All of the proofs can be found in Appendix A.

Proposition 1 (Prediction Market Equilibrium Without Social Networks) In a nonnetworked prediction market, the equilibrium prediction market price is given by

$$
\begin{array}{r l} P ^ {*} = \frac {1}{n} \sum_ {i = 1} ^ {n} & E [ V | I _ {i} ] = \frac {\rho_ {V}}{\rho_ {\varepsilon} + \rho_ {V}} V _ {0} + \frac {1}{n} \sum_ {i = 1} ^ {n} \frac {\rho_ {\varepsilon}}{\rho_ {\varepsilon} + \rho_ {V}} S _ {i} \\ & = \frac {\rho_ {V}}{\rho_ {\varepsilon} + \rho_ {V}} V _ {0} + \frac {\rho_ {\varepsilon}}{\rho_ {\varepsilon} + \rho_ {V}} V + \frac {\rho_ {\varepsilon}}{\rho_ {\varepsilon} + \rho_ {V}} \overline {{\mathcal {E}}} \end{array}
$$

where $\overline { { \mathcal { E } } } = \textstyle { \frac { 1 } { n } } \sum _ { i = 1 } ^ { n } \varepsilon _ { i }$ , and the equilibrium position for each participant is ${ x _ { i } ^ { * } } = \frac { \rho _ { \varepsilon } ( \varepsilon _ { i } - \overline { { \varepsilon } } ) } { 2 \gamma }$

The market price $P ^ { * }$ is the forecast/estimator generated from the prediction market. Proposition 1 shows the information aggregation mechanism of a prediction market where $P ^ { * }$ reflects participants’ diverse expectations, ${ \scriptstyle { \frac { 1 } { n } } } \sum _ { i = 1 } ^ { n } \mathbf { E } [ V | I _ { i } ]$ According to the equation

$$
P ^ {*} = \frac {\rho_ {V}}{\rho_ {\varepsilon} + \rho_ {V}} V _ {0} + \frac {1}{n} \sum_ {i = 1} ^ {n} \frac {\rho_ {\varepsilon}}{\rho_ {\varepsilon} + \rho_ {V}} S _ {i},
$$

the information-aggregation mechanism places weights on the public information and each individual’s private information. The weight on the public information in a nonnetworked prediction market is given by

$$
W _ {N P} = \frac {\rho_ {V}}{\rho_ {\varepsilon} + \rho_ {V}} / \left(\frac {\rho_ {V}}{\rho_ {\varepsilon} + \rho_ {V}} + \frac {1}{n} \sum_ {i = 1} ^ {n} \frac {\rho_ {\varepsilon}}{\rho_ {\varepsilon} + \rho_ {V}}\right) = \frac {\rho_ {V}}{\rho_ {\varepsilon} + \rho_ {V}}\tag{5}
$$

A natural question arises: What is the socially efficient weight on the public information? Suppose that we have an ideal scenario. The corporate manager can perfectly assess all prediction market participants’ private information without relying on a corporate prediction market. Then, the corporate manager’s best guess is her conditional expectation of $V ,$ which is a weighted average of the public information and all private signals

$$
P _ {m} = \mathbf {E} \big [ V | I _ {m} \big ] = \frac {\rho_ {V}}{n \rho_ {\varepsilon} + \rho_ {V}} V _ {0} + \sum_ {i = 1} ^ {n} \frac {\rho_ {\varepsilon}}{n \rho_ {\varepsilon} + \rho_ {V}} S _ {i}
$$

where $I _ { m }$ is the managers’ information set. Therefore, the efficient weight on the public information (first best) is

$$
W _ {m} = \frac {\rho_ {V}}{n \rho_ {\varepsilon} + \rho_ {V}} / \left(\frac {\rho_ {V}}{n \rho_ {\varepsilon} + \rho_ {V}} + \sum_ {i = 1} ^ {n} \frac {\rho_ {\varepsilon}}{n \rho_ {\varepsilon} + \rho_ {V}}\right) = \frac {\rho_ {V}}{n \rho_ {\varepsilon} + \rho_ {V}}\tag{6}
$$

Comparing equation 6 with equation 5, we find that $W _ { _ { N P } } \geq$ $W _ { m } ,$ which implies that the weight on the public information in a nonnetworked prediction market is larger than the efficient weight. This shows that the problem of overweighting the public information still exists in a corporate prediction market.

Following the prior literature (Davis-Stober et al. 2015; Lamberson and Page 2012), we use the mean squared error (MSE) to measure the prediction market performance or prediction accuracy. The MSE of an estimator measures the average of the squares of the “errors.” The larger the MSE is, the less accurate the forecast generated from the prediction market is. In a nonnetworked prediction market, the MSE of the forecast $P ^ { * }$ is given by

$$
\operatorname{MSE} (P ^ {*}) = \mathbf {E} \left[ (V - P ^ {*}) ^ {2} \right] = \frac {\rho_ {V}}{\left(\rho_ {\varepsilon} + \rho_ {V}\right) ^ {2}} + \frac {\rho_ {\varepsilon}}{n \left(\rho_ {\varepsilon} + \rho_ {V}\right) ^ {2}}\tag{7}
$$

and the MSE in the ideal scenario in which the manager can assess all prediction market participants’ private information is

$$
\operatorname{MSE} \left(P _ {m}\right) = \mathbf {E} \left[ \left(V - P _ {m}\right) ^ {2} \right] = \frac {1}{n \rho_ {\varepsilon} + \rho_ {V}} \leq \operatorname{MSE} (P ^ {*})\tag{8}
$$

From equation 7, we have the following proposition:

Proposition 2 (Comparative Statics on MSE) In a nonnetworked prediction market, the MSE of the forecast $P ^ { * }$ decreases with the number of prediction market participants, $n ,$ and the precision of private signals, $\rho _ { \varepsilon }$ $I f \frac { \rho _ { V } } { \rho _ { \varepsilon } } \leq \frac { n - 2 } { n }$ , the MSE increases with the precision of the common prior (public information); $i f \ \frac { \rho _ { V } } { \rho _ { \varepsilon } } > \frac { n - 2 } { n }$ , the MSE decreases with the precision of public information.

The implications of this proposition are as follows: First, the result of comparative statics of n on MSE is straightforward and consistent with our intuition. The prediction market accuracy increases with the number of participants. This result is reminiscent of the power of the wisdom of crowds: “Under the right circumstances, groups are remarkably intelligent, and are often smarter than the smartest people in them” (Surowiecki 2004, p. 41). The prediction errors are cancelled out when the number of participants is large. $\operatorname { I f } n  \infty .$ , the MSE converges to $\rho _ { \ / \ / } / ( \rho _ { \varepsilon } + \rho _ { \ / \ / } ) ^ { 2 }$

More importantly, we find that in a nonnetworked prediction market, increased precision of private information always enhances the prediction market accuracy. However, the impact of the public information precision is intriguing: When the precision of public information, $\rho _ { V } ,$ is relatively large to the precision of private information, $. \rho _ { \varepsilon }$ , greater precision of the public information increases prediction market accuracy. However, when $. \rho _ { V }$ is relatively small to $\rho _ { \varepsilon }$ , greater precision of public information is detrimental to prediction market accuracy.

In a prediction market with a very large number of participants $( n \to \infty )$ , our result can be simplified as follows: $\mathrm { I f } \rho _ { \scriptscriptstyle V } \geq$ $\rho _ { \varepsilon } ,$ the MSE decreases with $\rho _ { V } ; \mathrm { i f } \rho _ { V } < \rho _ { \varepsilon }$ , the MSE increases with $\rho _ { V }$ . This result is surprising in the sense that when we consider each participant’s decision making problem, more precise information is generally beneficial to the participant no matter whether the information is private (available only to participant i) or public (shared by all participants). However, it is not always the case that greater precision of the public information is desirable in terms of prediction market performance.

The key insight from our model is that increased precision of public information is beneficial only when it is precise. The underlying intuition is in line with the overweighting effect documented in the extant literature (Angeletos and Pavan 2007; Morris and Shn 2002). In our prediction market, the public information conveys useful information on the uncertain event, V. On the other hand, everyone receives the same public information. The detrimental impact arises from the fact that the information-aggregation mechanism places a larger-than-efficient weight on the public information: $W _ { _ { N P } \_ } >$ $W _ { m }$ . Specifically, when each participant forms her expectation of the uncertain event, $\mathbf { E } [ V | I _ { i } ]$ , she will give certain weight to the public information as her best guess. Then, the prediction market aggregates all participants’ expectations using a security-trading mechanism. Since every participant gives certain weight to the public information, the prediction market forecast will overreact to the public information because the public information is counted multiple times. Any noise contained in the public information will be magnified by overweighting the public information. Therefore, when the public information is less precise, we are more likely to observe that greater precision of public information lowers the prediction market accuracy. Note that the impact of increased precision of public information in a nonnetworked prediction market is given by

$$
\frac {\partial}{\partial \rho_ {V}} \operatorname{MSE} (P ^ {*}) = \underbrace {\frac {(n - 2) \rho_ {\varepsilon}}{n (\rho_ {\varepsilon} + \rho_ {V}) ^ {3}}} _ {\text { Detrimental   Effect }} - \underbrace {\frac {\rho_ {V}}{(\rho_ {\varepsilon} + \rho_ {V}) ^ {3}}} _ {\text { Beneficial   Effect }}\tag{9}
$$

where the first term indicates the detrimental effect of public information on the prediction market performance due to the overweighting problem, and the second term indicates the beneficial effect of public information since it conveys useful information about V. The impact of increased precision of the public information depends on the relative strength of these two effects.

Our following numerical example further illustrates the implications of Proposition 2 and gives a visualization of the regions of $\dot { \rho } _ { V } \mathrm { a n d } \rho _ { \varepsilon } ,$ , for which the prediction market accuracy measured by the MSE is increasing or decreasing in $\rho _ { V } .$ . In this numerical example, we set the number of prediction market participants, $n = 5 0$ . The results are robust when we vary n. Figure 1(a) displays the MSE for different values of the precisions of private information and public information. Figure 1(b) depicts the contour lines of the MSE. The whole

$$
\frac {\rho_ {V}}{\rho_ {\varepsilon}}
$$

$\scriptstyle = { \frac { n - 2 } { n } } = { \frac { 4 8 } { 5 0 } }$ . In Region I, greater precision of the public information increases the prediction market accuracy. However, in Region II, greater precision of the public information is detrimental to prediction market accuracy.

Figure 2 shows how the number of participants affects the size of Region II. The dotted line is $\frac { \rho _ { V } } { \rho _ { \varepsilon } } = \frac { 1 } { 3 }$ , which corresponds to $n = 3$ . Similarly, the solid and dashed lines represent $\frac { \rho _ { V } } { \rho _ { \varepsilon } } = \frac { 8 } { 1 0 }$ and $\frac { \rho _ { V } } { \rho _ { \varepsilon } } = \frac { 4 8 } { 5 0 }$ , respectively. As the number of participants increases, the marginal line will move up and converge to $\frac { \rho _ { V } } { \rho _ { \varepsilon } } = 1$ . In other words, when the number of participants is larger, increased precision of public information is more likely to be detrimental—that is, Region II is larger, and Region I is smaller. $\operatorname { I f } n = 3$ , the condition for a detrimental effect of the public information is $\rho _ { \varepsilon } \ge 3 \rho _ { \nu }$ . If n $= 5 0 \mathrm { _ }$ , the condition for a detrimental effect of the public information is $\rho _ { \varepsilon } \ge \frac { 2 5 } { 2 4 } \rho _ { V } .$ . Generally, we have the following proposition:

![](/api/attachments/32E665DK/fulltext/images/0aa9df175e4fc173928d61f58421c8227678fe7811e2e4a96ff331a45878026a.jpg)

![](/api/attachments/32E665DK/fulltext/images/f16c09626c0fc9255d0de78c4979d904ee703deee84d10eded1cb53c8362ef25.jpg)  
Figure 1. The Impact of Public Information and Private Information on Prediction Market Performance (Nonnetworked Case), n = 50

Proposition 3 In a nonnetworked prediction market, increased precision of public information is more likely to be detrimental to the prediction market performance as n increases.

The intuition of Proposition 3 can be derived by examining equation 9. The beneficial effect in equation 9 does not depend on $n ,$ but the detrimental effect increases with n. Actually, the overweighting problem becomes more serious as n increases. From equations 5 and 6, we find that the weight difference, $W _ { N P } - W _ { m } ,$ , increases with n. Therefore, increased precision of public information is more likely to be detrimental to the prediction market performance as n increases. Note that in the practice of corporate prediction markets, the number of participants typically varies from 20 to 50 or even larger (Chen and Plott 2002). When $n = 2 0 .$ , the condition for a detrimental effect of the public information is $\rho _ { \varepsilon } \geq \frac { 1 0 } { 9 } \rho _ { V } .$ It means that whenever the precision of the

private signal is greater than 10/9 of the precision of the public information, prediction market accuracy is decreasing in $\rho _ { V } .$ . This condition is likely to hold in reality because corporate prediction market participants are internal employees, and they may have more precise insider information (private signals) than the public information (Qiu et al. 2014b).

In summary, in the corporate prediction market design, the number of participants is critical not because it can directly affect the prediction market performance. According to equation 7, the marginal beneficial effect of prediction market size decreases as n increases. Prior empirical studies have also confirmed that the marginal beneficial effect of prediction market size on prediction market accuracy is small when the number of participants exceeds 20 (McHugh and Jackson 2012). The real reason why we should care about n is its impact on the condition for a detrimental effect of the public information: $\frac { \rho _ { \nu } } { \rho _ { \varepsilon } } \leq \frac { n - 2 } { n }$ . Proposition 2 can inform

managers the market conditions under which increased precision of public information is not beneficial. In the design of a corporate prediction market, managers should exercise caution in how much and how precise the public information they reveal. When the public information is relatively noisy, revealing more precise public information to prediction market participants may hurt prediction market accuracy.

## A Mixture Model of REE and DO

We develop a mixture model that nests both the REE and DO approaches where, among total n participants, m participants use the DO approach to make inferences, and n – m participants use the REE approach to make inferences. We denote the set of DO traders as $C _ { D O } .$ , which contains m participants. The rest n – m participants are REE traders. A DO trader $i \in C _ { D O }$ makes a Bayesian inference using her private signal and the common prior, as described in the previous section.

![](/api/attachments/32E665DK/fulltext/images/e11cd0d6773d13054da31c8e78fa27c801ccdd4e0a256c1772cfa588837d2d24.jpg)  
Figure 2. The Impact of the Number of Prediction Market Participants

If participant i is an REE trader, then her information set $I _ { i }$ is her private signal $S _ { i }$ as well as the price function $P ^ { * } ( V )$ . We denote the set of REE traders as $C _ { R E E } ,$ which contains $n - m$ participants. The central tenet of the REE literature (Grossman and Stiglitz 1980; Kyle 1985; O’Hara 1995) is that the market price is a function of the fundamental value V. Hence, a fully rational consumer is able to learn from the price function $P ^ { * } ( V )$ . Intuitively speaking, $P ^ { * } ( V )$ is self-fulfilling: When participants think prices as being generated by $P ^ { * } ( V )$ they will act in such a way that the market clears at $P ^ { * } ( V )$ Mathematically speaking, it is essentially a fixed-point problem. Following the finance and economics literature (Grossman and Stiglitz 1980; Kyle 1985; O’Hara 1995), we solve the fixed-point problem by assuming that an REE participant forms a linear conjecture on the equilibrium price function

$$
P ^ {*} (V) = a + b V + c \bar {\varepsilon}
$$

where $\begin{array} { r } { \bar { \varepsilon } = \frac { 1 } { n } et { } { ' } { \sum } _ { i = 1 } ^ { n } \varepsilon _ { i } } \end{array}$ , and a, b, and c are three constants to be determined. Recall that for both types of traders, the optimal trading position is given by equation 4. Using the market clearing condition, $\sum _ { i \in C _ { D O } } x _ { i } ^ { * } + \sum _ { j \in C _ { R E E } } x _ { j } ^ { * } = 0$ , we obtain the following proposition:

Proposition 4 (Prediction Market Equilibrium with both DO and REE Traders) In a prediction market with both DO and REE traders, the equilibrium prediction market price is given by

$$
P ^ {*} = a + b V + c \bar {\varepsilon}
$$

where $a = \frac { \rho _ { V } } { ( n + 1 - m ) \rho _ { \varepsilon } + \rho _ { V } } V _ { 0 }$ , and $\begin{array} { r } { b = c = \frac { \bigl ( n + 1 - m \bigr ) \rho _ { \varepsilon } } { \bigl ( n + 1 - m \bigr ) \rho _ { \varepsilon } + \rho _ { V } } . } \end{array}$

From Proposition 4, we find that the weight on public information in a market with both DO and REE traders is $\frac { \rho _ { V } } { ( n + 1 - m ) \rho _ { \varepsilon } + \rho _ { V } }$ From equation $^ { 6 , }$ the socially efficient weight is $\frac { \rho _ { V } } { n \rho _ { \varepsilon } + \rho _ { V } }$ . When there is more than one DO trader $( \mathrm { i } . \mathrm { e } . , \ m \ > \ 1 )$ , the problem of overweighting the public information still exists in a prediction market with both DO and REE traders, and the overweighting problem is most serious when all prediction market participants are DO traders, $m = n$ . We also compute the MSE of in a prediction market with both DO and REE traders:

$$
\begin{array}{c} \operatorname{MSE} (P ^ {*}) = \mathbf {E} [ (V - P ^ {*}) ^ {2} ] = \\ \frac {\rho_ {V}}{\left[ (n + 1 - m) \rho_ {\varepsilon} + \rho_ {V} \right] ^ {2}} + \frac {\rho_ {\varepsilon} (n + 1 - m) ^ {2}}{n \left[ (n + 1 - m) \rho_ {\varepsilon} + \rho_ {V} \right] ^ {2}} \end{array}
$$

Note that when $m = n ,$ , the MSE above will convert to the MSE in a prediction market where all participants are DO traders. Based on the MSE, we obtain the following two propositions.

Proposition 5 In a prediction market with both DO and REE traders, when $m \geq 1$ , the MSE of the forecast $P ^ { * }$ increases with the number of DO traders, m.

This proposition is consistent with our explanations on the overweight problem of public information. As the number of DO traders increases, the problem of overweighting public information will become more serious, and hence the prediction market performance will decrease (the MSE will increase).

Proposition 6 (Comparative Statics on MSE) In a prediction market with both DO and REE traders, the MSE of the forecast $P ^ { * }$ decreases with the number of prediction market participants, n, and the precision of private signals, $\rho _ { \varepsilon } .$ When $m \leq { \frac { n + 2 } { 2 } }$ , the MSE of the forecast P\* always decreases with the precision of public information. When m > $\frac { n + 2 } { 2 } \ : , \ : i f \ : \ : \frac { \rho _ { V } } { \rho _ { \varepsilon } } \leq \frac { \left( 2 m - 2 - n \right) \left( n + 1 - m \right) } { n }$ , the MSE increases with the precision of public information; and $i f \frac { \rho _ { V } } { \rho _ { \varepsilon } } > \frac { ( 2 m - 2 - n ) \left( n + 1 - m \right) } { n }$ the MSE decreases with the precision of public information.

The results in a prediction market that consists of both DO and REE traders are similar to those in a prediction market that consists of only DO traders. Increased number of participants and increased precision of private information always enhance prediction market accuracy; however, the impact of public information precision is conditional on the number of DO traders, m. If $m > \ \frac { n + 2 } { 2 }$ , the impact of the public information precision depends on the precisions of private and public information.

As we have shown in Propositions 4, 5, and 6, the key analytical results in the model that nests both the REE and DO approaches are qualitatively similar to those in a pure DO model: (1) the public information is overweighted, and (2) increased precision of public information is not always beneficial to prediction market performance. In the remainder of the paper, analyzing a socially embedded prediction market, we will focus on the pure DO model because the model nesting both the REE and DO approaches complicates our analyses and does not add additional analytical insights.

## A Socially Embedded Prediction Market

In this section, we examine the impact of information exchange in social networks on the prediction market performance in a pure DO framework. In our benchmark model, participants are isolated in the sense that they receive conditionally independent private information and cannot communicate with each other. However, in real corporate prediction markets, participants may receive information from each other in different forms (Qiu et al. 2014a). For instance, they may chat about their prediction tasks during their coffee breaks. Cowgill et al. (2009) found correlated tradings among employees who sit within a few feet of one another and employees with social or work relationships in Google’s prediction markets, which suggest that prediction market participants may share private information with their social connections. Specifically, in our socially embedded prediction markets, each participant receives a private signal and exchanges information with their friends in a social network. The social network $\Gamma = ( N , L )$ is given by a finite set of nodes $N = \{ 1 , 2 , . . . , n \}$ and a set of links $L \subseteq N \times N .$ Each node represents a participant in the prediction market. The social connections between the participants are described by an $n \times$ n dimensional matrix denoted by $g \in \{ 0 , 1 \} ^ { n \times n }$ , such that

$$
g _ {i j} = \left\{ \begin{array}{l l} 1, & i f (i, j) \in L \\ 0, & o t h e r w i s e \end{array} \right.
$$

where $g _ { i j } = 1$ implies that participants i and j are friends; otherwise, they are not. Let $N _ { i } ( g ) = \{ j \in N ; g _ { i j } = 1 \}$ represent the set of friends of participant i. The degree of participant i is the number of participant i’s friends: $k _ { i } ( g ) = \# N _ { i } ( g )$ Following the prior literature (Han and Yang 2013; Ozsoylev and Walden 2011), we assume that the social network is undirected and that prediction market participants can freely communicate their private signals to others that are connected to them in the network.<sup>16</sup> In other words, participant i can observe her friends’ signals, $S _ { i } , j \in N _ { i } ( g )$ , and take them into account in her inference process.

In the DO framework, each participant completely ignores others’ information contained in market prices. However, in our social network setup, we assume that DO participants consider the signals from their friends in the inference process. Actually, these two assumptions are compatible. As we pointed out, DO can be motivated by behavioral biases, such as bounded rationality and limited computational capacity, or heterogeneous priors. In our study, we adopt the first explanation: A prediction market participant lacks the ability to extract other participants’ information from market prices.<sup>17</sup> However, if other participants’ signals are directly given to her, she should have no problems using the signals. The rationality requirement for using available signals from friends is much lower than extracting other participants’ information from market prices, because drawing inferences from market prices requires complete knowledge of the market clearing process and correct conjectures on equilibrium prices. In our bounded rationality framework, the fact that a participant ignores others’ information contained in market prices is not because she always wants to ignore others’ information. The underlying deep reason is the constraint on participants’ information-processing abilities: They are unable to extract others’ information from market prices because they have limited cognitive abilities to process information (Kahneman 2003).

The key difference between the information contained in market prices and signals passed from friends is how information is presented and displayed. In an analytical model, Hirshleifer and Teoh (2003) assumed that financial information that is presented in a salient, easily processed form can be absorbed more easily by traders than information that is less salient and difficult to process because traders have limited attention and processing power. In our context, other participants’ information contained in market prices is less salient and difficult to process.<sup>18</sup> Peng (2005) pointed out that learning from prices is not free, since doing so requires knowledge of the structure of the market. Traders have limited time and attention to process information, and the capacity constraint limits the amount of information that she can process. An important argument in Hirshleifer and Teoh (2003) is that limited information processing capacity tends to induce participants to use information that is presented in salient, easily processed form (in our context, it refers to the signals from friends) rather than non-salient or hard-toprocess information (in our context, it refers to the information contained in market prices).<sup>19</sup>

Additionally, experimental evidence in prior literature suggests that extracting information from prices is more difficult than using available information directly. The time and attention needed to process financial information contained in prices is nontrivial. The empirical findings from laboratory markets show that traders rarely extract information that is available in prices. For instance, Bloomfield et al. (2009) tested a key assumption in Hong and Stein in a laboratory experiment—traders’ inability to draw inferences from the market price—and found evidence supporting that the traders fail to infer other traders’ information from market prices. In another laboratory experiment, Corgnet et al. (2015) found that their data can be best explained by the model in which traders do not infer other traders’ information from market prices but apply Bayes’ rule to compute the expected value of the asset given their own information.

To make our model analytically tractable, we consider three special cases of a general social graph g:

(1) A regular social network without homophily, where every participant has the same degree k (Jackson 2008). In this case, we assume the private signal errors to be independent across all participants.

(2) A regular social network with homophily. Homophily is a typical phenomenon observed in social networks in that there are inherent similarities in friends’ personal characteristics (Aral and Walker 2011; Bapna and Umyarov 2015; Gu et al. 2014). In this case, we assume that the errors of private signals are positively correlated.

(3) A heterogeneous social network where a participant has either degree 0 or degree (the analytical results of this case can be found in Appendix B).

Although oversimplified, the network structure in these three cases reflects some fundamental features of typical social networks in reality and enables us to draw analytical insights. For instance, Cases (1) and (2) are more balanced social networks without degree heterogeneity and reflect a flat organization since no one is located in the center of the network. This is similar to the assumption in Ozsoylev and Walden (2011): No agent is informationally superior and possesses too much information. Case (3) is a more heterogeneous social network and may reflect a socially embedded prediction market consisting of both well-connected employees who have high social skills and isolated employees who have low social skills. Because the case of a general social graph is not analytically tractable, we run numerical simulations and show that our analytical insights remain robust when the underlying networks are more complicated (e.g., the Erdos–Renyi random graph, the Gilbert graph, the “small world” graph, and the preferential attachment graph).

## A Regular Social Network Without Homophily

In a regular network, each participant has k friends and can receive private signals of her friends. Therefore, a participant i’s information set, $I _ { i } ,$ includes her private signal, her friends’ private signals (k signals), and the common prior. She makes an inference as follows:

$$
\begin{array}{c} \mathbf {E} \big [ V | I _ {i} \big ] = \frac {\rho_ {V}}{(k + 1) \rho_ {\varepsilon} + \rho_ {V}} V _ {0} + \frac {\rho_ {\varepsilon}}{(k + 1) \rho_ {\varepsilon} + \rho_ {V}} S _ {i} + \\ \sum_ {j \in N _ {i} (g)} \frac {\rho_ {\varepsilon}}{(k + 1) \rho_ {\varepsilon} + \rho_ {V}} S _ {j}, \\ \mathbf {V a r} [ V | I _ {i} ] = 1 / [ (k + 1) \rho_ {\varepsilon} + \rho_ {V} ] \end{array}
$$

Similarly, participant i’s position is given by equation 4, and the equilibrium prediction market price $P ^ { * }$ is determined by the market clearing condition, $\textstyle \sum _ { i = 1 } ^ { n } x _ { i } ^ { * } = 0$

The following proposition characterizes the equilibrium of a prediction market with a regular social network.

Proposition 7 (Prediction Market Equilibrium in a Regular Social Network) In a prediction market with a regular social network, the equilibrium prediction market price is given by

$$
P ^ {*} = \frac {\rho_ {V}}{(k + 1) \rho_ {\varepsilon} + \rho_ {V}} V _ {0} + \frac {(k + 1) \rho_ {\varepsilon}}{(k + 1) \rho_ {\varepsilon} + \rho_ {V}} V + \frac {(k + 1) \rho_ {\varepsilon}}{(k + 1) \rho_ {\varepsilon} + \rho_ {V}} \overline {{\mathcal {E}}}
$$

where $\overline { { \mathcal { E } } } = \textstyle { \frac { 1 } { n } } \sum _ { i = 1 } ^ { n } \varepsilon _ { i }$ , and the equilibrium position for each participant is

$$
x _ {i} ^ {*} = \frac {\rho_ {\varepsilon}}{2 \gamma} \Bigg [ \varepsilon_ {i} + \sum_ {j \in N _ {i} (g)} \varepsilon_ {j} - (k + 1) \overline {{\varepsilon}} \Bigg ]
$$

Proposition 7 indicates that in a prediction market with a regular social network, the weight on public information is given by

$$
W _ {R S} = \frac {\rho_ {V}}{(k + 1) \rho_ {\varepsilon} + \rho_ {V}} \leq W _ {N P}\tag{10}
$$

If we compare equation 10 with equations 5 and 6, we find that $W _ { m } \leq W _ { R S } \leq W _ { N P } ,$ , where $W _ { m } = W _ { R S }$ when $k = n - 1 ,$ , and $W _ { R S } = W _ { N P }$ when $k = 0$ . The implication is that social interaction among prediction market participants can correct the problem of overweighting the public information. When the level of social interactions reaches the maximum (a complete or a fully connected social network, $k = n - 1 )$ , the weight on the public information is efficient in a prediction market with a regular network.

Then, we compute the MSE of $P ^ { * }$ in a prediction market with a regular social network.

$$
\begin{array}{r l} \operatorname{MSE} (P *) & = \mathbf {E} \left[ (V - P *) ^ {2} \right] \\ & = \frac {\rho_ {V}}{\left[ (k + 1) \rho_ {\varepsilon} + \rho_ {V} \right] ^ {2}} + \frac {\rho_ {\varepsilon} (k + 1) ^ {2}}{n \left[ (k + 1) \rho_ {\varepsilon} + \rho_ {V} \right] ^ {2}} \end{array}\tag{11}
$$

Note that when $k = 0 _ { \cdot }$ , the MSE in a prediction market with a regular social network given by equation 11 will convert to equation 7, the MSE in a nonnetworked prediction market. In general, we can consider a nonnetworked prediction market as a special case of a prediction market with a regular network $( k = 0 )$

Comparing the MSE in a prediction market with a regular social network with that in a nonnetworked prediction market, we obtain the following proposition:

Proposition 8 (MSE Comparison: No Network Versus Regular Network) The MSE in a nonnetworked prediction market is greater than the MSE in a prediction market with a regular social network.

Proposition 8 shows that a prediction market with a regular social network outperforms a prediction market without social networks. As we have explained before, the problem of a nonnetworked prediction market is that the informationaggregation process will count the public information multiple times, and therefore magnify the noise contained in the public information. The existence of a regular social network facilitates private information exchange among participants, which effectively puts a larger weight on the private information. In a regular network, each participant will receive her friends private signals, and her own private signal will be received by k friends. In other words, each private signal will be counted k times when participants’ predictions are aggregated in the prediction market. Such multiple counting of private information is beneficial to the prediction market performance because it can correct the bias toward the public information caused by overweighting the public information. Essentially, the advantage of embedding a social network is to use the multiple counting of private information to neutralize the harmful effect from the multiple counting of public information.

We examine the effect of the level of social interactions, k, on the prediction market performance in the following proposition:

Proposition 9 (Impact of Social Interaction Level) The MSE in a prediction market with a regular network decreases with k.

Proposition 9 shows that the prediction market performance increases with the level of social interactions, k. In practice, a manager may want to encourage social interactions among participants to improve prediction market accuracy. The intuition is similar to that in Proposition 8. As the level of social interactions, k, increases, the bias toward the public information will be corrected to a larger extent, and the weight on the public information in the informationaggregation process will be closer to the efficient value.

To examine the impact of the precision of public and private information, we have the following proposition:

Proposition 10 (Comparative Statics on MSE) In a prediction market with a regular social network, the MSE of the forecast $P ^ { * }$ decreases with the number of prediction market participants, n, and the precision of private signals, $\rho _ { \varepsilon } .$ $\begin{array} { r } { I f \frac { \rho _ { V } } { \rho _ { \varepsilon } } \leq \left( k + 1 \right) \left[ \frac { n - 2 \left( k + 1 \right) } { n } \right] } \end{array}$ , the MSE increases with the precision of public information; $\begin{array} { r } { i f \ \frac { \rho _ { V } } { \rho _ { \varepsilon } } > \left( k + 1 \right) \left[ \frac { n - 2 \left( k + 1 \right) } { n } \right] } \end{array}$ , the MSE decreases with the precision of public information.

The results in a prediction market with a regular social network are similar to those in a nonnetworked prediction market. Increased precision of private information always enhances prediction market accuracy, but the impact of public information precision depends on the relative precision of private information versus public information. When $\rho _ { \varepsilon }$ is relatively small to $\rho _ { V } ,$ greater precision of the public information increases the prediction market accuracy. When $\rho _ { \varepsilon }$ is relatively large to $\rho _ { V } ,$ greater precision of the public information decreases the prediction market accuracy. In a socially embedded prediction market, the prediction performance depends on not only the precisions of private and public information but also the level of social interactions, k.

An interesting observation from Propositions 8, 9, and 10 is that a socially embedded prediction market with low precision of the private information may perform as well as a nonnetworked prediction market with high precision of the private information. A managerial implication of this result is about the selection of prediction market participants. In general, an internal employee has two types of skills: work skills and social skills. In our context, the level of work skills refers to the ability to acquire precise private information (knowledge creation and information production) and is measured by $\rho _ { \varepsilon } .$ In contrast, the level of social skills refers to the ability to communicate and share information with colleagues (knowledge transfer and information communication) and is measured by k. Intuitively, a manager should select employees who have a high level of work skills $( \rho _ { \varepsilon } )$ as prediction market participants. This is also consistent with Proposition 10. However, Proposition 9 shows that the level of social skills (k) also matters when we consider the prediction market performance. A group of participants who have a medium level of work skills but a high level of social skills may outperform those who have a high level of work skills but a low level of social skills. We provide a numerical example in Appendix C.

Regarding the precision of public information, in a prediction market with a regular network, the impact of increased precision of public information is given by

$$
\frac {\partial}{\partial \rho_ {V}} \operatorname{MSE} (P *) = \underbrace {\frac {[ n - 2 (k + 1) ] (k + 1) \rho_ {\varepsilon}}{n [ (k + 1) \rho_ {\varepsilon} + \rho_ {V} ] ^ {3}}} _ {\text { Detrimental   Effect }} - \underbrace {\frac {\rho_ {V}}{[ (k + 1) \rho_ {\varepsilon} + \rho_ {V} ] ^ {3}}} _ {\text { Beneficial   Effect }}\tag{12}
$$

As we have stated, the impact of increased precision of public information depends on the relative strength of the detrimental and beneficial effects. The beneficial effect in equation 12 does not depend on n, but the detrimental effect increases with n. Therefore, we should expect that increased precision of public information is more likely to be detrimental to the prediction market performance as n increases. As for the level of social interactions, $k ,$ we have the following proposition:

Proposition 11 In a prediction market with a regular network, increased precision of public information is more likely to be detrimental to the prediction market performance as n increases. When $n \geq 4 ( k + 1 )$ , increased precision of public information is more likely to be detrimental to the prediction market performance as k increases; when $n < 4 ( k \scriptsize { \mathit { \Phi } } + 1 )$ increased precision of public information is less likely to be detrimental to the prediction market performance as k increases. Specifically, $i f n < 2 ( k + 1 )$ , the prediction market performance will always increase with the precision of public information.

As in the previous section, we define Region I as the range of market conditions in which increased precision of public information enhances the prediction market accuracy and Region II as the range of market conditions in which increased precision of public information decreases the prediction market accuracy. Proposition 11 indicates the conditions in which Region II becomes larger as the level of social interactions, k, increases in a prediction market with a regular social network. When n is large relative to k, the size of Region II increases with k. When n is small relative to k, the size of Region II decreases with k.

To provide some additional intuition, we conduct a numerical analysis and visualize Proposition 11. In Figure 3, we set n = 50, and vary degree k. The solid line represents $\frac { \rho _ { V } } { \rho _ { \varepsilon } } =$ $\displaystyle ( k + 1 ) \left[ { \frac { n - 2 { \big ( } k + 1 { \big ) } } { n } } \right]$ , where $k = 1 0 , 2 0$ , and 25, and the dashed line represents the marginal line in the case of no social networks $( k = 0 ) \colon \frac { \rho _ { V } } { \rho _ { \varepsilon } } = \frac { n - 2 } { n }$ . According to Proposition 11, if $n \geq 2 ( k + 2 )$ , Region II should be larger in a prediction market with a regular social network than in a nonnetworked prediction market. In Figure 3(a), the marginal line moves up as k increases from 0 to 1, which suggests that Region II is larger when a prediction market is embedded in a regular social network. In Figures 3(a) and (b), we find that Region II becomes larger as k increases from 1 to 10. However, the size of Region II shrinks as k increases from 10 to 20 in Figures 3(b) and 3(c). Eventually, when $k = 2 5$ , Region II does not exist (only Region I left) in Figure 3(d). These results are consistent with Proposition 11: (1) When $n \geq$ $4 ( k + 1 )$ , increased precision of public information is more likely to be detrimental to the prediction market performance as k increases; (2) when $n < 4 ( k + 1 )$ , increased precision of public information is less likely to be detrimental to the prediction market performance as k increases; and (3) when $n < 2 ( k + 1 )$ ), the prediction market performance will always increase with the precision of public information.

precision of public information, it may not be a good idea to disclose it to all prediction market participants. In a socially embedded prediction market, the size of Region II could be much larger than in a nonnetworked prediction market under some circumstances. For instance, in Figure 3(b), where $k =$ 10 and $n = 5 0$ , increased precision of public information is detrimental to the prediction market performance if $\frac { \rho _ { V } } { \rho _ { \varepsilon } } \leq 6 . 1 6$ (the solid line). However, in a nonnetworked environment, increased precision of public information is detrimental to the prediction market performance if $\frac { \rho _ { V } } { \rho _ { \varepsilon } } \leq 0 . 9 6$ (the dashed line). Additionally, when $n  \infty ( \mathrm { a }$ large prediction market with many participants), increased precision of public information is detrimental to prediction market performance if $\frac { \rho _ { V } } { \rho _ { \varepsilon } } \leq k + 1$ in a regular network case, whereas the condition is $\frac { \rho _ { V } } { \rho _ { \varepsilon } } \leq 1$ in a nonnetworked case. For reasonable parameter choices in reality, the detrimental effect of public information is much more likely to occur in a socially embedded prediction market than in a nonnetworked case.

## A Regular Social Network with Homophily

In the previous analysis, we assume the private signal errors to be independent across all participants. In our context, participants connected through a social network may be similar to each other, and therefore may have similar information sources when formulating their private information, such as reading the same reports and news articles, working in the same department of the company, having similar educational and working experiences and so on.<sup>20</sup> In this section, we relax the assumption of independent private information and assume that the errors of friends’ private signals are positively correlated to reflect the plausible existence of homophily.

![](/api/attachments/32E665DK/fulltext/images/5405fb8c41b29d2223f5f647bafe692dd74be6d1c75011ccf7b2a0ba0efb5a73.jpg)  
Figure 3. The Impact of Public Information and Private Information on Prediction Market Performance (Regular Network), n = 50

For analytical tractability, we first look at a regular social network with $k _ { i } \left( g \right) = k = 1$ . It means that each participant has one friend and can receive the private signal of her friend. We will examine the impact of homophily in more complicated social networks using simulations in the next section. Because of the homophily effect, the error of participant i’s private signal, $\mathbf { \nabla } _ { \mathcal { E } _ { i } } ,$ is correlated with her friend j’s private signal error $\varepsilon _ { j } .$

$$
\binom{\boldsymbol {\varepsilon} _ {i}}{\boldsymbol {\varepsilon} _ {j}} \sim N (0, \Sigma), \Sigma = \left( \begin{array}{c c} 1 / \rho_ {\varepsilon} & \delta / \rho_ {\varepsilon} \\ \delta / \rho_ {\varepsilon} & 1 / \rho_ {\varepsilon} \end{array} \right)
$$

where G is the covariance matrix for participant $i ^ { \circ } \mathrm { s }$ and participant $j ^ { \prime } s$ signal errors, and δ is the correlation coefficient. In order to capture the homophily effect, we assume that $0 \leq \delta \leq 1$ . Participant i makes an inference as follows:

$$
\begin{array}{r l} & {\mathbf {E} \big [ V | I _ {i} \big ] = \frac {\rho_ {V}}{\frac {2}{1 + \delta} \rho_ {\varepsilon} + \rho_ {V}} V _ {0} + \frac {\rho_ {\varepsilon}}{\frac {2}{1 + \delta} \rho_ {\varepsilon} + \rho_ {V}} \frac {1}{1 + \delta} S _ {i} +} \\ & {\qquad \frac {\rho_ {\varepsilon}}{\frac {2}{1 + \delta} \rho_ {\varepsilon} + \rho_ {V}} \frac {1}{1 + \delta} S _ {j}, \mathbf {V a r} \big [ V | I _ {i} \big ] = 1 / \left[ \frac {2}{1 + \delta} \rho_ {\varepsilon} + \rho_ {V} \right]} \end{array}
$$

The following proposition characterizes the equilibrium of a prediction market with a homophily social network.

Proposition 12 (Prediction Market Equilibrium under Homophily) In a prediction market under homophily, the equilibrium prediction market price is given by

$$
P ^ {*} = \frac {\rho_ {V}}{\frac {2}{1 + \delta} \rho_ {\varepsilon} + \rho_ {V}} V _ {0} + \frac {2 \rho_ {\varepsilon}}{\frac {2}{1 + \delta} \rho_ {\varepsilon} + \rho_ {V}} \frac {1}{1 + \delta} V + \frac {2 \rho_ {\varepsilon}}{\frac {2}{1 + \delta} \rho_ {\varepsilon} + \rho_ {V}} \frac {1}{1 + \delta} \overline {{\mathcal {E}}}
$$

Proposition 12 shows that in a prediction market under homophily, the weight on public information is $W _ { H } = \frac { \rho _ { V } } { \frac { 1 } { 1 + \delta } \rho _ { \varepsilon } + \rho _ { V } }$ According to our previous analysis, in a prediction market with a regular social network (no homophily), the weight on public information when $k \ = \ 1 \quad \mathrm { i s } \quad W _ { R S } \ =$ $\frac { \rho _ { V } } { ( k + 1 ) \rho _ { \varepsilon } + \rho _ { V } } = \frac { \rho _ { V } } { 2 \rho _ { \varepsilon } + \rho _ { V } } \le W _ { H }$ . The implication is that even though social interaction among prediction market participants can correct the problem of overweighting the public information, the homophily effect tends to weaken the correction because the friend’s information is less useful under homophily. In an extreme case with perfect correlation $( \delta =$ 1), ${ \cal W } _ { H } = { \cal W } _ { N P } ,$ which means that social interactions cannot correct the overweighting problem at all when the friend’s private signal does not contain additional value.

Then, we compute the MSE of $P ^ { * }$ in a prediction market under homophily.

$$
\operatorname{MSP} (P ^ {*}) = \mathbf {E} [ (V - P ^ {*}) ^ {2} ] =
$$

$$
\frac {\rho_ {V}}{\left[ \frac {2}{1 + \delta} \rho_ {\varepsilon} + \rho_ {V} \right] ^ {2}} + \frac {\rho_ {\varepsilon} \frac {4}{1 + \delta}}{n \left[ \frac {2}{1 + \delta} \rho_ {\varepsilon} + \rho_ {V} \right] ^ {2}}
$$

and we obtain the following propositions:

Proposition 13 (Impact of Homophily) The MSE in a prediction market under homophily increases with δ.

Proposition 14 (Comparative Statics on MSE) In a prediction market under homophily, the MSE of the forecast $P ^ { * }$ decreases with the number of prediction market participants, $n ,$ and the precision of private signals, $\rho _ { \varepsilon } .$ $\begin{array} { r } { I f { \frac { \rho _ { \nu } } { \rho _ { \varepsilon } } } \leq { \frac { 2 } { 1 + \delta } } \Big [ { \frac { n - 4 } { n } } \Big ] } \end{array}$ the MSE increases with the precision of public information; $i f \frac { \rho _ { V } } { \rho _ { \varepsilon } } > \frac { 2 } { 1 + \delta } { \left[ \frac { n - 4 } { n } \right] }$ , the MSE decreases with the precision of public information.

Proposition 13 suggests that the homophily effect tends to be detrimental to the prediction market performance. Proposition 14 further shows that the impact of increased precision of public information depends on the information correlation coefficient $\delta ,$ which measures the effect of homophily.

A surprising result based on Proposition 14 is that, as the homophily effect δ increases, the region in which greater precision of the public information is detrimental to the prediction market accuracy becomes smaller. In other words, increased precision of public information is less likely to be detrimental to the prediction market performance when the homophily effect is stronger. The intuition is as follows: If the role of public information precision is relatively important compared with the role of private information precision, greater public information precision is beneficial to the prediction market performance; otherwise, it is detrimental to the performance (a main analytical result that is robust in all our different cases). For instance, if public information precision is high, then the role of public information is relatively important, and greater public information precision is more likely to be beneficial. However, if private information precision is high, then the role of public information is relatively unimportant, and greater public information precision is more likely to be detrimental. If homophily is more significant, it will reduce the informational value of friends’ signals, and the role of private/public information precision will become smaller/ larger because a focal participant will receive less valuable information from her friends. Therefore, greater public information precision is less likely to be detrimental.

## Numerical Simulations on More Complicated Social Networks

We examine prediction markets in which participants are embedded in more complicated social networks, including the Gilbert graph, the Erdos–Renyi random graph, the “small world” graph, and the preferential attachment graph. We use CONTEST, a network toolbox for MATLAB, to simulate the aforementioned random graphs (Taylor and Higham 2009).

The Gilbert graph and the Erdos–Renyi random graph are classical random graph models. In Gilbert’s (1959) model, a link between two prediction market participants is formed with an independent probability p. We set the parameter values $n = 5 0$ $V _ { 0 } = 1 0 , \rho _ { \varepsilon } = 0 . 1$ , and $p = 0 . 0 5$ , and run the simulation 10,000 times to calculate the MSE in the prediction market. The results are robust for other parameter values. Figures 4(a) and 4(b) show the effect of the precision of public information on the MSE in a prediction market with a Gilbert network under no homophily/homophily (the homophily correlation coefficient is 0.2). The results are consistent in both no homophily and homophily cases. When the public information is noisy, increased precision of public information is detrimental to the prediction market performance. When public information is precise, increased precision of public information is beneficial to the prediction market performance.

In the Erdos–Renyi model (Erdos and Renyi 1960), the number of links, $m ,$ in the network is specified. We then select uniformly at random from the set of all social networks containing $n = 5 0$ participants and m links. We follow Taylor and Higham (2009) and set m to be the smallest integer bigger than (nlogn)/2. The result is similar and shown in Figure 5.

Motivated by the fact that many real-world networks have a small average shortest path length, Watts and Strogatz (1998) proposed a small-world network in which most nodes are not neighbors of one another, but most nodes can be reached from every other by a small number of steps. Following Taylor and Higham, the Watts-Strogatz model begins with a k-nearest neighbor ring. Then, each participant is considered independently in turn. With a fixed probability p, a participant is given an extra link connecting it to a participant chosen uniformly at random across the network. We choose the default parameter values in Taylor and Higham: k = 2 and $p$ = 0.1 The result is shown in Figure 6.

The preferential attachment graph is a scale-free network that has a power-law degree distribution (Barabasi and Albert 1999). Scale-free networks are widely observed in reality. In Barabasi and Albert’s model, the graph grows until n participants haven been created. Each new participant is given d links on arrival. These new connections are not chosen uniformly—the new links to an existing participant with a probability that is proportional to the current degree of that participant. In this way, well-connected participants tend to become even better connected as the graph evolves. We follow Taylor and Higham and set d = 2. We observe that the result in Figure 7 is similar. To provide a benchmark, we also depict the nonnetworked case using the same parameter values in Figure D.1, which can be found in online Appendix D.

![](/api/attachments/32E665DK/fulltext/images/85d54b27352348c7082a8567240ceb142170e81c26d1ff7a3c27578009591d96.jpg)  
(a) No Homophily

![](/api/attachments/32E665DK/fulltext/images/6058ac64949bcad6ea9ed17b7d0328d385edc01907d8b814a3dc8b230578beff.jpg)  
(b) Homophily

Figure 4. The Effect of Precision of Public Information on the MSE in a Gilbert Network, n = 50, $\pmb {  } \mathbf { [ \eta \pmb { \eta } ] } = \mathbf { [ \eta \pmb { \eta } ] } \mathbf { [ \eta ] }$ $\pmb {  } \pmb {  } \pmb {  } \pmb {  } \pmb {  } \pmb {  } \pmb {  } \pmb {  } \pmb {  } \pmb {  } \pmb {  } \pmb {  } \pmb {  } \pmb {  } \pmb { [ \pmb {  } \pmb { [ \alpha } \pmb { [ \alpha } \pmb { [ \alpha } \pmb {  }     }$ and p = 0.05  
![](/api/attachments/32E665DK/fulltext/images/8c8a3d2edc17e2ba8b17d6c6e0d78e532e029ec03254e5928346d6a5a737bb8a.jpg)  
(a) No Homophily

![](/api/attachments/32E665DK/fulltext/images/e3e0081814139ff8456ad5de5fb69469e67004f2b6e26ee307e07e90dc645281.jpg)  
(b) Homophily

Figure 5. The Effect of Precision of Public Information on the MSE in an Erdos–Renyi Network, $\pmb { \omega } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta }$ $\pmb { \mathbb { W } } \mathbf { \mathbb { H } } \mathbf { \Theta }$ and $\pmb {  } \mathbf { s } \mathbf { \Theta } \mathbf { s } \mathbf { \Theta } [ \pmb { 0 } \mathbf { \Theta } ]$  
![](/api/attachments/32E665DK/fulltext/images/a0149f1346764731fc98e15ff812b82fbc54caa55e4ba1344af97ad99fa17cc6.jpg)  
(a) No Homophily

![](/api/attachments/32E665DK/fulltext/images/fe7d1eb9e3cda87accf9e8dd07e357cd7f2e7e32931968a8c4d9eeda9cf0179c.jpg)  
(b) Homophily  
Figure 6. The Effect of the Precision of Public Information on the MSE in a Small-World Network, $\pmb {  } \varkappa \mathbf { \Theta } ^ { \ast } ( \pmb {  } )$ $\mathfrak { W } _ { 0 } \mathbf { \equiv } \mathbf { 0 } \mathbf { \equiv } \mathbf { 0 }$ and $\pmb {  } \mathbf { s } \mathbf { \Theta } \mathbf { \boxed { 9 } } \mathbf { \Theta }$

![](/api/attachments/32E665DK/fulltext/images/0f3f778b39f64a4a587c9e3af1d91147f9ed6a4b588db798d297d8e174171474.jpg)  
(a) No Homophily

![](/api/attachments/32E665DK/fulltext/images/f7709f0b56daab164452419767f79a5dac8f4e8d2e7800c9ffab35e5b0dad69a.jpg)  
(b) Homophily  
Figure 7. The Effect of the Precision of Public Information on the MSE in a Preferential Attachment Network, n = 50, V<sub>0</sub> = 10, and ρ<sub>ε</sub> = 0.1

## Managerial Implications

The advancement of social media technologies has provided an unprecedented opportunity for corporate prediction market designers to facilitate information communications within organizations and to improve the prediction market performance. Our analytical results have the following implications and guidance for corporate prediction market design.

When should a corporate manager disclose more precise public information? Although increased precision of the public information is always beneficial to individual prediction market participants, it can be detrimental to prediction market performance as a whole when the public information is relatively noisy. When corporate prediction market designers choose the extent of public information disclosure, they need to know the level of public information precision relative to private information precision. If the private information is relatively precise, the corporation may want to hide the public information as much as possible. However, if the public information is relatively precise, the corporation may want to disclose the public information as much as possible.<sup>21</sup>

When should a corporate manager encourage social interactions among prediction market participants? Our model shows that social interactions among prediction market participants can improve the prediction market performance. The social network, however, has a side effect. As the level of social interaction increases, increased precision of public information may be more likely to be detrimental under some market conditions. Corporate prediction market designers should consider the pros and cons of embedding social networks in a prediction market. If increasing the level of social interactions is beneficial, managers can (1) encourage employees to be involved in multiple projects throughout the company and to become effective information hubs, and (2) promote social networking among employees using Facebook, Twitter, LinkedIn, or the in-house corporate network.<sup>22</sup>

Managers can directly measure the actual information flow among employees, such as employees’ discussions, in the internal social media platform or infer the information flow through monitoring correlated prediction market trading behavior among corporate employees.<sup>23</sup>

In general, our analytical model reminds corporate managers that the prediction market is not a panacea for all decisionmaking problems. It is true that corporate hierarchy can cause individual employees to overweight the existing public information. However, a prediction market may lead to a similar problem: The information-aggregation mechanism places a larger-than-efficient weight on the public information. As a result, increased precision of public information can be detrimental. The bottom line is that managers should be fully aware of the market conditions in which disclosing more precise public information is detrimental.

## Conclusions

Introducing corporate prediction markets has become a popular way for companies to improve business decision making. In the present study, we examine the roles of information precision and social interactions in corporate prediction markets. The wisdom of crowds hypothesis states that existing prediction market prices always incorporate and reflect all relevant information of individuals. However, this hypothesis considers only the aggregation of diverse private information, leaving out the role of public information that is available to all participants. In our analytical model, we find that the prediction market mechanism places a larger than efficient weight on the public information. If a social network is embedded, information sharing among participants may help correct this inefficiency. Therefore, the integration of prediction markets with a social network is not only theoretically interesting (a social context is often neglected in the modeling of prediction markets), but also practically important. Our analysis should serve as a guide for corporate managers when they design internal prediction markets.

provide internal social media platforms for prediction market participants to communicate with each other. Montgomery et al. (2013) documented that Ford employees participating in the prediction market saw an internal social platform as an outlet for expressing their opinions about predictions and demonstrated a strong desire to write comments attempting to convince each other of their positions.

There are several possible extensions to our research. First, in our model, we assume that participants are able to observe their friends’ private signals without information loss. It would be interesting to examine the information loss or bias caused by communication barriers or strategic issues (Chen et al. 2011; Lin et al. 2005). Second, one avenue of extending our model is to incorporate semipublic information that is available only to a specific group of participants in a heterogeneous network. In the present paper, we distinguish two extreme types of information: private information that is received by single individuals only and public information that is available to all participants. In future research, one may allow for intermediate degrees of publicity: information that is common knowledge to only a fraction of all participants. For instance, in a company, the semipublic information in the marketing department might be different from that in the engineering department. Another potential avenue for further research is to study how social network structures affect the role of public information precision in prediction markets.

## References

Abaramowicz, M., and Henderson, M. T. 2007. “Prediction Markets for Corporate Governance,” Notre Dame Law Review (82:4), pp. 1343-1414.

Aid, R., Chemla, G., Porchet, A., and Touzi, N. 2011. “Hedging and Vertical Integration in Electricity Markets,” Management Science (57:8), pp. 1438-1452.

Angeletos, G. M., and Pavan, A. 2007. “Efficient Use of Information and Social Value of Information,” Econometrica (75:4), pp. 1103-1142.

Aral, S., and Walker, D. 2011. “Creating Social Contagion through Viral Product Design: A Randomized Trial of Peer Influence in Networks,” Management Science (57:9), pp. 1623-1639.

Ba, S., Stallaert, J., and Whinston, A. B. 2001. “Optimal Investment in Knowledge Within a Firm Using a Market Mechanism,” Management Science (47:9), pp. 1203-1219.

Banerjee, S., Kaniel, R., and Kremer, I. 2009. “Price Drift as an Outcome of Differences in Higher-Order Beliefs,” Review of Financial Studies (22:9), pp. 3707-3734.

Banerjee, S., and Kremer, I. 2010. “Disagreement and Learning: Dynamic Patterns of Trade,” Journal of Finance (65:4), pp. 1269-1302.

Bapna, R., and Umyarov, A. 2015. “Do Your Online Friends Make You Pay? A Randomized Field Experiment on Peer Influence in Online Social Networks,” Management Science (61:8), pp. 1902-1920.

Barabasi, A. L., and Albert, R. 1999. “Emergence of Scaling in Random Networks,” Science (286:5439), pp. 509-512.

Berg, J. E., Forsythe, R., Nelson, F., and Rietz, T. 2008. “Results from a Dozen Years of Election Futures Markets Research,” in Handbook of Experimental Economics Results (Volume 1, Chapter 80), C. R. Plott and V. L. Smitt (eds.), Amsterdam: North Holland, pp. 742-751.

<sup>23</sup>If trading positions of two employees are highly correlated over time, it suggests an information flow between them. Using the past trading behavior data, a company can have a better idea about the actual information flows within the organization.

Berg, J. E., Neumann, G. R. , and Rietz, T. A. 2009. “Searching for Google’s Value: Using Prediction Markets to Forecast Market Capitalization Prior to an Initial Public Offering,” Management Science (55:3), pp. 348-361.

Berg, J. E., and Rietz, T. A. 2003. “Prediction Markets as Decision Support Systems,” Information Systems Frontiers (5:1), pp. 79-93.

Bloom, N., Liang, J., Roberts, J., and Ying, Z. J. 2015. “Does Working from Home Work? Evidence from a Chinese Experiment,” Quarterly Journal of Economics (130:1), pp. 165-218.

Bloomfield, R. J., Tayler, W. B., and Zhou, F. H. 2009. “Momentum, Reversal, and Uninformed Traders in Laboratory Markets,” Journal of Finance (64:6), pp. 2535-2558.

Bichler, M., Gupta, A., and Ketter, W. 2010. “Designing Smart Markets,” Information Systems Research (21:4), pp. 688-699.

Bondt, W. F., and Thaler, R. 1985. “Does the Stock Market Overreact?,” Journal of Finance (40:3), pp. 793-805.

Cao, H. H., and Ou-Yang, H. 2009. “Differences of Opinion of Public Information and Speculative Trading in Stocks and Options,” Review of Financial Studies (22:1), pp. 299-335.

Cespa, G., and Vives, X. 2015. “The Beauty Contest and Short-Term Trading,” Journal of Finance (70:5), pp. 2099-2154.

Chen, J., Xu, H., and Whinston, A. B. 2011. “Moderated Online Communities and Quality of User-Generated Content,” Journal of Management Information Systems (28:2), pp. 237-268.

Chen, K., and Plott, C. 2002. “Information Aggregation Mechanisms: Concept, Design and Implementation for a Sales Forecasting Problem,” Working Paper No. 1131, Division of the Humanities and Social Sciences, California Institute of Technology Social Science, Pasadena, CA.

Chen, Q., and Jiang, W. 2006. “Analysts’ Weighting of Private and Public Information,” Review of Financial Studies (19:1), pp. 319-355.

Coase, R. H. 1937. “The Nature of the Firm,” Economica (4:16), pp. 386-405.

Cohen, L., Frazzini, A., and Malloy, C. 2008. “The Small World of Investing: Board Connections and Mutual Fund Returns,” Journal of Political Economy (116:5), pp. 951-979.

Coles, P. A., Lakhani, K. R., and McAfee, A. 2007. “Prediction Markets at Google,” Harvard Business School Case 9-607-088, Boston, MA.

Colla, P., and Mele, A. 2010. “Information Linkages and Correlated Trading,” Review of Financial Studies (23:1), pp. 203-246.

Corgnet, B., DeSantis, M., and Porter, D. 2015. “Revisiting Information Aggregation in Asset Markets: Reflective Learning and Market Efficiency,” Working paper, Economic Science Institute, Chapman University, Orange, CA (available at http://econpapers.repec.org/paper/chuwpaper/15-15.htm).

Coval, J. D., and Moskowitz, T. J. 2001. “The Geography of Investment: Informed Trading and Asset Prices,” Journal of Political Economy (109:4), pp. 811-841.

Cowgill, B., Wolfers, J., and Zitzewitz, E. 2009. “Using Prediction Markets to Track Information Flows: Evidence from Google,” in Auctions, Market Mechanisms and Their Applications: First

International ICST Conference, AMMA 2009, Boston, MA, May 8-9, Revised Selected Papers (Vol. 14, p. 3), New York: Springer Science & Business Media.

Cowgill, B., and Zitzewitz, E. 2015. “Corporate Prediction Markets: Evidence from Google, Ford, and Firm X1,” Review of Economic Studies (82:4), pp. 1309-1341.

Davis-Stober, C. P., Budescu, D. V., Broomell, S. B., and Dana, J. 2015. “The Composition of Optimally Wise Crowds,” Decision Analysis (12:3), pp. 130-143.

Erdos, P., and Renyi, A. 1960. “On the Evolution of Random Graphs,” Publications of the Mathematical Institute of the Hungarian Academy of Sciences (5), pp. 17-61.

Fang, F., Stinchcombe, M., and Whinston, A. B. 2007. “Putting Your Money Where Your Mouth Is—Betting Mechanism Design for Better Prediction,” Review of Network Economics (6:3), pp. 214-238.

Fang, F., Stinchcombe, M., and Whinston, A. B. 2010. “Proper Scoring Rules with Arbitrary Value Functions,” Journal of Mathematical Economics (46:6), pp. 1200-1210.

Foutz, N. Z., and Jank, W. 2010. “Prerelease Demand Forecasting for Motion Pictures Using Functional Shape Analysis of Virtual Stock Markets,” Marketing Science (29:3), pp. 568-579.

Gilbert, E. N. 1959. “Random Graphs,” Annals of Mathematical Statistics (30:4), pp. 1141-1144.

Granovetter, M. 1985. “Economic Action and Social Structure: The Problem of Embeddedness,” American Journal of Sociology (91:3), pp. 481-510.

Grossman, S. 1976. “On the Efficiency of Competitive Stock Markets Where Trades Have Diverse Information,” Journal of Finance (31:2), pp. 573-585.

Grossman, S. 1978. “Further Results on the Informational Efficiency of Competitive Stock Markets,” Journal of Economic Theory (18:1), pp. 81-101.

Grossman, S. J., and Stiglitz, J. E. 1980. “On the Impossibility of Informationally Efficient Markets,” American Economic Review (70:3), pp. 393-408.

Golub, B., and Jackson, M. 2010. “Naive Learning in Social Networks and the Wisdom of Crowds,” American Economic Journal: Microeconomics (2:1), pp. 112-149.

Gu, B., Konana, P., Raghunathan, R., and Chen, H. M. 2014. “The Allure of Homophily in Social Media: Evidence from Investor Responses on Virtual Communities,” Information Systems Research (25:3), pp. 604-617.

Guo, Z., Fang, F., and Whinston, A. B. 2006. “Supply Chain Information Sharing in a Macro Prediction Market,” Decision Support Systems (42:3), pp. 1944-1958.

Han, B., and Yang, L. 2013. “Social Networks, Information Acquisition, and Asset Prices,” Management Science (59:6), pp. 1444-1457.

Hansen, M. T. 2002. “Knowledge Networks: Explaining Effective Knowledge Sharing in Multiunit Companies,” Organization Science (13:3), pp. 232-248.

Harris, M., and Raviv, A. 1993. “Differences of Opinion Make a Horse Race,” Review of Financial Studies (6:3), pp. 473-506.

Harrison, J. M., and Kreps, D. M. 1978. “Speculative Investor Behavior in a Stock Market with Heterogeneous Expectations,” Quarterly Journal of Economics (92:2), pp. 323-336.

Healy, P. J., Linardi, S., Lowery, J. R., and Ledyard, J. O. 2010. “Prediction Markets: Alternative Mechanisms for Complex Environments with Few Traders,” Management Science (56:11), pp. 1977-1996.

Hellwig, M. F. 1980. “On the Aggregation of Information in Competitive Markets,” Journal of Economic Theory (22:3), pp. 477-498.

Hirshleifer, D., and Teoh, S. H. 2003. “Limited Attention, Information Disclosure, and Financial Reporting,” Journal of Accounting and Economics (36:1), pp. 337-386.

Hong, H., and Stein, J. C. 1999. “A Unified Theory of Underreaction, Momentum Trading, and Overreaction in Asset Markets,” Journal of Finance (54:6), pp. 2143-2184.

Hong, H., and Stein, J. C. 2003. “Differences of Opinion, Short-Sales Constraints, and Market Crashes,” Review of Financial Studies (16:2), pp. 487-525.

Hopman, J. W. 2007. “Using Forecasting Markets to Manage Demand Risk,” Intel Technology Journal (11:2), pp. 127-135.

Jackson, M. O. 2008. Social and Economic Networks, Princeton, NJ: Princeton University Press.

Jensen, M. C. 1978. “Some Anomalous Evidence Regarding Market Efficiency,” Journal of Financial Economics (6:2/3), pp. 95-101.

Jian, L., and Sami, R. 2012. “Aggregation and Manipulation in Prediction Markets: Effects of Trading Mechanism and Information Distribution,” Management Science (58:1), pp. 123-140.

Jiang, Y., and Guo, H. 2015. “Design of Consumer Review Systems and Product Pricing,” Information Systems Research (26:4), pp. 714-730.

Jiang, Z., Mookerjee, V. S., and Sarkar, S. 2005. “Lying on the Web: Implications for Expert Systems Redesign,” Information Systems Research (16:2), pp. 131-148.

Kandel, E., and Pearson, N. D. 1995. “Differential Interpretation of Public Signals and Trade in Speculative Markets,” Journal of Political Economy (103:4), pp. 831-872.

Kahneman, D. 2003. “Maps of Bounded Rationality: Psychology for Behavioral Economics,” American Economic Review (93:5), pp. 1449-1475.

Ketter, W., Peters, M., Collins, J., and Gupta, A. 2016a. “Competitive Benchmarking: An IS Research Approach to Address Wicked Problems with Big Data and Analytics,” MIS Quarterly (40:4), pp. 1057-1080.

Ketter, W., Peters, M., Collins, J., and Gupta, A. 2016b. “A Multiagent Competitive Gaming Platform to Address Societal Challenges,” MIS Quarterly (40:2), pp. 447-460.

Keuschnigg, M., and Ganser, C. 2017. “Crowd Wisdom Relies on Agents’ Ability in Small Groups with a Voting Aggregation Rule,” Management Science (63:3), pp. 818-828.

Kyle, A. S. 1985. “Continuous Auctions and Insider Trading,” Econometrica (53:6), pp. 1315-1335.

Lamberson, P. J., and Page, S. E. 2012. “Optimal Forecasting Groups,” Management Science (58:4), pp. 805-810.

Leigh, A., and Wolfers, J. 2007. “Prediction Markets for Business and Public Policy,” Melbourne Review: A Journal of Business and Public Policy (3:1), pp. 7-15.

Levy, H., and Markowitz, H. M. 1979. “Approximating Expected Utility by a Function of Mean and Variance,” American Economic Review (69:3), pp. 308-317.

Lin, L., Geng, X., and Whinston, A. B. 2005. “A Sender–Receiver Framework for Knowledge Transfer,” MIS Quarterly (29:2), pp. 197-219.

Liu, D., Geng, X., and Whinston, A. B. 2007. “Optimal Design of Consumer Contests,” Journal of Marketing (71:4), pp. 140-155.

Lorenz, J., Rauhut, H., Schweitzer, F., and Helbing, D. 2011. “How Social Influence Can Undermine the Wisdom of Crowd Effect,” Proceedings of the National Academy of Sciences (109:22), pp. 9020-9025.

Lovell, M. C. 1986. “Tests of the Rational Expectations Hypothesis,” American Economic Review (76:1), pp. 110-124.

Malkiel, B. G., and Fama, E. F. 1970. “Efficient Capital Markets: A Review of Theory and Empirical Work,” Journal of Finance (25:2), pp. 383-417.

Mello, J. A. 2014. Strategic Human Resource Management, Stamford, CT: Cengage Learning.

McHugh, P., and Jackson, A. 2012. “Prediction Market Accuracy: The Impact of Size, Incentives, Context and Interpretation,” Journal of Prediction Markets (6:22), pp. 22-46.

Montgomery, T. A., Stieg, P. M., Cavaretta, M. J., and Moraal, P. E. 2013. “Experience from Hosting a Corporate Prediction Market: Benefits Beyond the Forecasts,” in Proceedings of the 19<sup>th</sup> ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, New York: ACM Press, pp. 1384-1392.

Morris, S., and Shim, H. S. 2002. “Social Value of Public Information,” American Economic Review (92:5), pp. 1521-1534.

O’Hara, M. 1995. Market Microstructure Theory, Malden, MA: Blackwell.

Ozsoylev, H. N., and Walden, J. 2011. “Asset Pricing in Large Information Networks,” Journal of Economic Theory (146:6), pp. 2252-2280.

Parise, S., Whelan, E., and Todd, S. 2015. “How Twitter Users Can Generate Better Ideas,” MIT Sloan Management Review (56:4), pp. 21-25.

Peng, L. 2005. “Learning with Information Capacity Constraints,” Journal of Financial and Quantitative Analysis (40:2), pp. 307-329.

Prendergast, C. 1993. “A Theory of Yes Men,” American Economic Review (83:4), pp. 757-70.

Qiu, L., Rui, H., and Whinston, A. B. 2014a. “Effects of Social Networks on Prediction Markets: Examination in a Controlled Experiment,” Journal of Management Information Systems (30:4), pp. 235-268.

Qiu, L., Rui, H., and Whinston, A. B. 2014b. “The Impact of Social Network Structures on Prediction Market Accuracy in the Presence of Insider Information,” Journal of Management Information Systems (31:1), pp. 145-172.

Scheinkman, J. A., and Xiong, W. 2003. “Overconfidence and Speculative Bubbles,” Journal of Political Economy (111:6), pp. 1183-1220.

Shiller, R. J. 1981. “Do Stock Prices Move Too Much to Be Justified by Subsequent Changes in Dividends?,” American Economic Review (71:3), pp. 421-436.

Stasser, G., and Titus, W. 1985. “Pooling of Unshared Information in Group Decision Making: Biased Information Sampling During Discussion,” Journal of Personality and Social Psychology (48:6), pp. 1467-1478.

Stasser, G., and Titus, W. 2003. “Hidden Profiles: A Brief History,” Psychological Inquiry (14:3/4), pp. 304-313.

Surowiecki, J. 2004. The Wisdom of Crowds: Why the Many Are Smarter than the Few and How Collective Wisdom Shapes Business, Economies, Societies, and Nations, New York: Doubleday.

Sunstein, C. R. 2005. “Group Judgements: Statistical Means, Deliberation, and Information Markets,” New York University Law Review (80), pp. 962-1895.

Taylor, A., and Higham, D. J. 2009. “CONTEST: A Controllable Test Matrix Toolbox for MATLAB,” ACM Transactions on Mathematical Software (35:4), pp. 26:1-26:17.

Tirole, J. 1982. “On the Possibility of Speculation under Rational Expectations,” Econometrica (50:5), pp. 1163-1181.

Van Bruggen, G. H., Spann, M., Lilien, G. L., and Skiera, B. 2010. “Prediction Markets as Institutional Forecasting Support Systems,” Decision Support Systems (49:4), pp. 404-416.

Vives, X. 1993. “How Fast Do Rational Agents Learn?,” Review of Economic Studies (60:2), pp. 329-347.

Watts, D. J., and Strogatz, S. H. 1998. “Collective Dynamics of ‘Small-World’ Networks,” Nature (393:6684), pp. 440-442.

## About the Authors

Liangfei Qiu is an assistant professor in the Department of Information Systems and Operations Management at the Warrington College of Business, University of Florida. He received his Ph.D. in Economics from the University of Texas at Austin. His current research focuses on economics of information systems, prediction markets, social media, and telecommunications policy. His research has been published in journals such as Information Systems Research, Journal of Management Information Systems, and Decision Support Systems.

Hsing Kenneth Cheng is the John B. Higdon Eminent Scholar, Department of Information Systems and Operations Management, Warrington College of Business at the University of Florida. He received his Ph.D. in computers and information systems from William E. Simon Graduate School of Business Administration, University of Rochester. His research interests focus on analyzing the impact of Internet and information technology on software development and marketing, and information systems policy issues, in particular, the national debate on network neutrality.

Jingchuan Pu is a Ph.D. student in the Department of Information Systems and Operations Management at the Warrington College of Business, University of Florida. His research interests include economics of information systems, prediction markets, and economic effects of online review systems.

# HIDDEN PROFILES IN CORPORATE PREDICTION MARKETS: THE IMPACT OF PUBLIC INFORMATION PRECISION AND SOCIAL INTERACTIONS

Liangfei Qiu Warrington College of Business, University of Florida, Gainesville, FL 32611 U.S.A. {liangfeiqiu@ufl.edu}

Hsing Kenneth Cheng Warrington College of Business, University of Florida, Gainesville, FL 32611 U.S.A. {hkcheng@ufl.edu} and School of Information Management and Engineering, Shanghai University of Finance and Economics, Shanghai, CHINA

Jingchuan Pu Warrington College of Business, University of Florida, Gainesville, FL 32611 U.S.A. {jingchuan@ufl.edu}

## Appendix A

## Proof of Proposition 1

Proof. Each participant’s demand for the security is given by equation 4. We solve the equilibrium prediction market price $P ^ { * }$ by plugging equation 4 into the market clearing condition, $\begin{array} { r } { \sum _ { i = 1 } ^ { n } x _ { i } ^ { * } = 0 . } \end{array}$ . Then we can obtain the equilibrium demand $x _ { i } ^ { * }$

## Proof of Proposition 2

Proof. From equation 7, it is obvious that MSE(P\*) decreases with n. We can also obtain

$$
\frac {\partial}{\partial \rho_ {\varepsilon}} \mathrm{MSE} (P ^ {*}) = \frac {1}{(\rho_ {\varepsilon} + \rho_ {V}) ^ {3}} \biggl [ - \frac {\rho_ {\varepsilon}}{n} + (\frac {1}{n} - 2) \rho_ {V} \biggr ] <   0
$$

and

$$
\frac {\partial}{\partial \rho_ {V}} \mathrm{MSE} (P *) = \frac {1}{(\rho_ {\varepsilon} + \rho_ {V}) ^ {3}} \left[ \left(\frac {n - 2}{n}\right) \rho_ {\varepsilon} - \rho_ {V} \right]
$$

Therefore, if $\frac { \rho _ { V } } { \rho _ { \varepsilon } } \leq \frac { n - 2 } { n } , \frac { \partial } { \partial \rho _ { V } } \mathrm { M S E } \big ( P \ast \big ) \geq 0 \mathrm { , ~ i f ~ } \frac { \rho _ { V } } { \rho _ { \varepsilon } } > \frac { n - 2 } { n } , \frac { \partial } { \partial \rho _ { V } } \mathrm { M S E } \big ( P \ast \big ) < 0 .$

## Proof of Proposition 3

Proof. The marginal line $\begin{array} { r } { \frac { \rho _ { V } } { \rho _ { \varepsilon } } = \frac { n - 2 } { n } } \end{array}$ determines the range of two regions (whether or not increased precision of public information is detrimental), and $\frac { n - 2 } { n }$ increases with ݊. Therefore, as ݊ increases, the region, $\frac { \rho _ { V } } { \rho _ { \varepsilon } } \leq \frac { n - 2 } { n } .$ , becomes larger, and the region, $\frac { \rho _ { V } } { \rho _ { \varepsilon } } > \frac { n - 2 } { n } .$ , shrinks.

## Proof of Proposition 4

Proof. Each participant’s demand for the security is given by equation $\begin{array} { r } { x _ { i } ^ { * } = \frac { \mathbf E [ V | I _ { i } ] - P } { 2 \gamma \mathbf { V } \mathbf { a r } [ V | I _ { i } ] } . } \end{array}$ . For a DO trader $i \in C _ { D O }$

$$
\begin{array}{r} \mathbf {E} [ V | I _ {i} ] = \mathbf {E} [ V | S _ {i} ] = \frac {\rho_ {V}}{\rho_ {\varepsilon} + \rho_ {V}} V _ {0} + \frac {\rho_ {\varepsilon}}{\rho_ {\varepsilon} + \rho_ {V}} S _ {i}, \\ \mathbf {V a r} [ V | I _ {i} ] = \mathbf {V a r} [ V | S _ {i} ] = 1 / (\rho_ {\varepsilon} + \rho_ {V}) \end{array}
$$

For an REE trader $i \in C _ { R E E }$

$$
\begin{array}{c} \mathbf {E} [ V | I _ {i} ] = \mathbf {E} [ V | S _ {i}, P ^ {*} ] \\ = \frac {\rho_ {V}}{\left(\frac {n b ^ {2}}{c ^ {2}} + 1\right) \rho_ {\varepsilon} + \rho_ {V}} V _ {0} + \frac {\rho_ {\varepsilon}}{\left(\frac {n b ^ {2}}{c ^ {2}} + 1\right) \rho_ {\varepsilon} + \rho_ {V}} S _ {i} + \frac {\frac {n b ^ {2}}{c ^ {2}} \rho_ {\varepsilon}}{\left(\frac {n b ^ {2}}{c ^ {2}} + 1\right) \rho_ {\varepsilon} + \rho_ {V}} \Big (\frac {P ^ {*} - a}{b} \Big), \\ \mathbf {V a r} [ V | I _ {i} ] = \mathbf {V a r} [ V | S _ {i}, P ^ {*} ] = 1 / \left[ \left(\frac {n b ^ {2}}{c ^ {2}} + 1\right) \rho_ {\varepsilon} + \rho_ {V} \right] \end{array}
$$

We solve the equilibrium prediction market price $P ^ { * }$ by plugging these equations into the market clearing condition, $\textstyle \sum _ { i \in C _ { D O } } x _ { i } ^ { * } +$ $\begin{array} { r } { \sum _ { j \in C _ { R E E } } x _ { j } ^ { * } = 0 } \end{array}$ Then we compare the solution from the market clearing condition with the initial conjecture:

$$
P ^ {*} = a + b V + c \overline {{\varepsilon}},
$$

and determine the coefficients $a , b ,$ and c.

## Proof of Proposition 5

$$
\mathbf {P r o o f . W h e n} m \geq 1, \frac {\partial}{\partial m} \mathrm{MSE} (P ^ {*}) = \frac {2 \rho_ {\varepsilon} \rho_ {V}}{[ (n + 1 - m) \rho_ {\varepsilon} + \rho_ {V} ] ^ {3}} - \frac {2 (n + 1 - m) \rho_ {\varepsilon}}{[ (n + 1 - m) \rho_ {\varepsilon} + \rho_ {V} ] ^ {2}} + \frac {2 (n + 1 - m) ^ {2} \rho_ {\varepsilon} ^ {2}}{n [ (n + 1 - m) \rho_ {\varepsilon} + \rho_ {V} ] ^ {3}} = \frac {2 (m - 1) \rho_ {\varepsilon} \rho_ {V}}{n [ (n + 1 - m) \rho_ {\varepsilon} + \rho_ {V} ] ^ {3}} \geq 0.
$$

## Proof of Proposition 6

$$
\begin{array}{r l} & {\mathrm{Proof.} \frac {\partial}{\partial n} \mathrm{MSE} (P ^ {*}) = - \frac {2 \rho_ {\varepsilon} \rho_ {V}}{[ (n + 1 - m) \rho_ {\varepsilon} + \rho_ {V} ] ^ {3}} + \frac {2 (n + 1 - m) \rho_ {\varepsilon}}{n [ (n + 1 - m) \rho_ {\varepsilon} + \rho_ {V} ] ^ {2}} - \frac {(n + 1 - m) ^ {2} \rho_ {\varepsilon}}{n ^ {2} [ (n + 1 - m) \rho_ {\varepsilon} + \rho_ {V} ] ^ {2}} - \frac {2 (n + 1 - m) ^ {2} \rho_ {\varepsilon} \rho_ {V}}{n [ (n + 1 - m) \rho_ {\varepsilon} + \rho_ {V} ] ^ {3}} =} \\ & {\frac {- 2 (m - 1) n \rho_ {\varepsilon} \rho_ {V} - (n + 1 - m) ^ {2} [ (n + 1 - m) \rho_ {\varepsilon} + \rho_ {V} ] \rho_ {\varepsilon}}{n ^ {2} [ (n + 1 - m) \rho_ {\varepsilon} + \rho_ {V} ] ^ {3}} <   0.} \\ & {\frac {\partial}{\partial \rho_ {\varepsilon}} \mathrm{MSE} (P ^ {*}) = - \frac {2 (n + 1 - m) \rho_ {V}}{[ (n + 1 - m) \rho_ {\varepsilon} + \rho_ {V} ] ^ {3}} + \frac {(n + 1 - m) ^ {2}}{n [ (n + 1 - m) \rho_ {\varepsilon} + \rho_ {V} ] ^ {2}} - \frac {2 (n + 1 - m) ^ {3} \rho_ {\varepsilon}}{n [ (n + 1 - m) \rho_ {\varepsilon} + \rho_ {V} ] ^ {3}} = \frac {- (n + 1 - m) (m + n - 1) \rho_ {V} - (n + 1 - m) ^ {3} \rho_ {\varepsilon}}{n ^ {2} [ (n + 1 - m) \rho_ {\varepsilon} + \rho_ {V} ] ^ {3}} <   0.} \\ & {\frac {\partial}{\partial \rho_ {V}} \mathrm{MSE} (P ^ {*}) = \frac {1}{[ (n + 1 - m) \rho_ {\varepsilon} + \rho_ {V} ] ^ {2}} - \frac {2 \rho_ {V}}{[ (n + 1 - m) \rho_ {\varepsilon} + \rho_ {V} ] ^ {2}} - \frac {2 (n + 1 - m) ^ {2} \rho_ {\varepsilon}}{n [ (n + 1 - m) \rho_ {\varepsilon} + \rho_ {V} ] ^ {3}} = \frac {(n + 1 - m) (2 m - n - 2) \rho_ {\varepsilon} - n \rho_ {V}}{n ^ {2} [ (n + 1 - m) \rho_ {\varepsilon} + \rho_ {V} ] ^ {3}}.} \end{array}
$$

$$
\mathrm{If} m \leq \frac {n + 2}{2}, \frac {\partial}{\partial \rho_ {V}} \mathrm{MSE} (P ^ {*}) <   0. \mathrm{If} m > \frac {n + 2}{2} \mathrm{and} \frac {\rho_ {V}}{\rho_ {\varepsilon}} \leq \frac {(2 m - 2 - n) (n + 1 - m)}{n}, \frac {\partial}{\partial \rho_ {V}} \mathrm{MSE} (P ^ {*}) \geq 0; \mathrm{if} \frac {\rho_ {V}}{\rho_ {\varepsilon}} > \frac {(2 m - 2 - n) (n + 1 - m)}{n}, \frac {\partial}{\partial \rho_ {V}} \mathrm{MSE} (P ^ {*}) <   0.
$$

## Proof of Proposition 7

Proof. We plug $\begin{array} { r } { x _ { i } ^ { * } = \frac { \mathbf { E } [ V | I _ { i } ] - P } { 2 \gamma \mathbf { V } \mathbf { a r } [ V | I _ { i } ] } } \end{array}$ into the market clearing condition and obtain

$$
P ^ {*} = \frac {1}{n} \sum_ {i = 1} ^ {n} \mathbf {E} [ V | I _ {i} ] = \frac {\rho_ {V}}{(k + 1) \rho_ {\varepsilon} + \rho_ {V}} V _ {0} + \frac {(k + 1) \rho_ {\varepsilon}}{(k + 1) \rho_ {\varepsilon} + \rho_ {V}} V + \frac {(k + 1) \rho_ {\varepsilon}}{(k + 1) \rho_ {\varepsilon} + \rho_ {V}} \overline {{\varepsilon}}
$$

Then,

$$
x _ {i} ^ {*} = \frac {\mathbf {E} [ V | I _ {i} ] - P ^ {*}}{2 \gamma \mathbf {V a r} [ V | I _ {i} ]} = \frac {\rho_ {\varepsilon}}{2 \gamma} \big [ \varepsilon_ {i} + \sum_ {j \in N _ {i} (g)} \varepsilon_ {j} - (k + 1) \overline {{\varepsilon}} \big ]
$$

## Proof of Proposition 8

Proof. From equations 7 and 11, we can obtain the difference between the MSE in a prediction market without social networks and the MSE in a prediction market with a regular social network:

$$
\frac {\rho_ {V}}{(\rho_ {\varepsilon} + \rho_ {V}) ^ {2}} + \frac {\rho_ {\varepsilon}}{n (\rho_ {\varepsilon} + \rho_ {V}) ^ {2}} - \frac {\rho_ {V}}{[ (k + 1) \rho_ {\varepsilon} + \rho_ {V} ] ^ {2}} - \frac {\rho_ {\varepsilon} (k + 1) ^ {2}}{n [ (k + 1) \rho_ {\varepsilon} + \rho_ {V} ] ^ {2}} \geq 0
$$

where the equality holds when $k = 0$

## Proof of Proposition 9

Proof. From equation 11, we can obtain:

$$
\frac {\partial}{\partial k} \mathrm{MSE} (P ^ {*}) = \frac {1}{[ (k + 1) \rho_ {\varepsilon} + \rho_ {V} ] ^ {3}} \left[ - 2 \rho_ {\varepsilon} \rho_ {V} + \frac {2}{n} \rho_ {\varepsilon} \rho_ {V} (k + 1) \right] \leq 0
$$

The inequality comes from the fact that $k + 1 \leq n$ in a regular network.

## Proof of Proposition 10

Proof. From equation 11, it is obvious that MSE(ܲ<sup>∗</sup>) decreases with ݊. From equation 11, we can also obtain

$$
\begin{array}{r l} & {\frac {\partial}{\partial \rho_ {\varepsilon}} \mathrm{MSE} (P ^ {*})} \\ & {= \frac {1}{[ (k + 1) \rho_ {\varepsilon} + \rho_ {V} ] ^ {3}} \Big [ - \frac {\rho_ {\varepsilon} (k + 1) ^ {3}}{n} + \Big (\frac {k + 1}{n} - 2 \Big) \rho_ {V} (k + 1) \Big ] <   0} \end{array}
$$

and

$$
\begin{array}{r l} & {\frac {\partial}{\partial \rho_ {V}} \mathrm{MSE} (P ^ {*})} \\ & {= \frac {1}{[ (k + 1) \rho_ {\varepsilon} + \rho_ {V} ] ^ {3}} \left[ \left(\frac {n - 2 (k + 1)}{n}\right) (k + 1) \rho_ {\varepsilon} - \rho_ {V} \right]} \end{array}
$$

Therefore, the result follows.

## Proof of Proposition 11

Proof. The marginal line $\begin{array} { r } { \frac { \rho _ { V } } { \rho _ { \varepsilon } } = \left( k + 1 \right) \left[ \frac { n - 2 \left( k + 1 \right) } { n } \right] } \end{array}$ determines the range of two regions (whether or not increased precision of public information is detrimental). The right hand side $\left( k + 1 \right) \left[ { \frac { n - 2 ( k + 1 ) } { n } } \right]$ increases with ݊, increases with ݇ i $\therefore n \geq 4 ( k + 1 )$ , and decreases with ݇ if $n < 4 ( k + 1 )$ .

## Proof of Proposition 12

Proof. Each participant’s demand for the security is given by equation $\begin{array} { r } { x _ { i } ^ { * } = \frac { \mathbf E [ V | I _ { i } ] - P } { 2 \gamma \mathbf { V } \mathbf { a r } [ V | I _ { i } ] } . } \end{array}$ . In the homophily case,

$$
\mathbf {E} [ V | I _ {i} ] = \frac {\rho_ {V}}{\frac {2}{1 + \delta} \rho_ {\varepsilon} + \rho_ {V}} V _ {0} + \frac {\rho_ {\varepsilon}}{\frac {2}{1 + \delta} \rho_ {\varepsilon} + \rho_ {V}} \frac {1}{1 + \delta} S _ {i} + \frac {\rho_ {\varepsilon}}{\frac {2}{1 + \delta} \rho_ {\varepsilon} + \rho_ {V}} \frac {1}{1 + \delta} S _ {j}, \mathbf {V a r} [ V | I _ {i} ] = 1 / \left[ \frac {2}{1 + \delta} \rho_ {\varepsilon} + \rho_ {V} \right]
$$

We solve the equilibrium price by using the market clearing condition $\begin{array} { r } { \sum _ { i = 1 } ^ { n } x _ { i } ^ { * } = 0 } \end{array}$

## Proof of Proposition 13

$$
\mathbf {P r o o f .} \frac {\partial}{\partial \delta} \mathrm{MSE} (P ^ {*}) = \frac {4 \rho_ {V} \rho_ {\varepsilon}}{(1 + \delta) ^ {2} (\rho_ {V} + \frac {2 \rho_ {\varepsilon}}{1 + \delta}) ^ {3}} + \frac {1 6 \rho_ {\varepsilon} ^ {2}}{n (1 + \delta) ^ {3} (\rho_ {V} + \frac {2 \rho_ {\varepsilon}}{1 + \delta}) ^ {3}} - \frac {4 \rho_ {\varepsilon}}{n (1 + \delta) ^ {2} (\rho_ {V} + \frac {2 \rho_ {\varepsilon}}{1 + \delta}) ^ {2}} = \frac {4 \rho_ {\varepsilon} [ (- 1 + n) (1 + \delta) \rho_ {V} + 2 \rho_ {\varepsilon} ]}{n [ (1 + \delta) \rho_ {V} + 2 \rho_ {\varepsilon} ] ^ {3}} > 0.
$$

## Proof of Proposition 14

$$
\begin{array}{r l} & {\mathbf {P r o o f .} \frac {\partial}{\partial n} \mathrm{MSE} (P ^ {*}) = - \frac {4 \rho_ {\varepsilon}}{n ^ {2} (1 + \delta) (\rho_ {V} + \frac {2 \rho_ {\varepsilon}}{1 + \delta}) ^ {2}} <   0.} \\ & {\frac {\partial}{\partial \rho_ {\varepsilon}} \mathrm{MSE} (P ^ {*}) = - \frac {4 \rho_ {V}}{(1 + \delta) (\rho_ {V} + \frac {2 \rho_ {\varepsilon}}{1 + \delta}) ^ {3}} - \frac {1 6 \rho_ {\varepsilon}}{n (1 + \delta) ^ {2} (\rho_ {V} + \frac {2 \rho_ {\varepsilon}}{1 + \delta}) ^ {3}} + \frac {4}{n (1 + \delta) (\rho_ {V} + \frac {2 \rho_ {\varepsilon}}{1 + \delta}) ^ {2}} = - \frac {4 (1 + \delta) [ (- 1 + n) (1 + \delta) \rho_ {V} + 2 \rho_ {\varepsilon} ]}{n [ (1 + \delta) \rho_ {V} + 2 \rho_ {\varepsilon} ] ^ {3}} <   0.} \\ & {\frac {\partial}{\partial \rho_ {V}} \mathrm{MSE} (P ^ {*}) = - \frac {2 \rho_ {V}}{(\rho_ {V} + \frac {2 \rho_ {\varepsilon}}{1 + \delta}) ^ {3}} - \frac {8 \rho_ {\varepsilon}}{n (1 + \delta) (\rho_ {V} + \frac {2 \rho_ {\varepsilon}}{1 + \delta}) ^ {3}} + \frac {1}{(\rho_ {V} + \frac {2 \rho_ {\varepsilon}}{1 + \delta}) ^ {2}} = - \frac {(1 + \delta) ^ {2} [ n (1 + \delta) \rho_ {V} - 2 (- 4 + n) \rho_ {\varepsilon} ]}{n [ (1 + \delta) \rho_ {V} + 2 \rho_ {\varepsilon} ] ^ {3}}.} \end{array}
$$

$\begin{array} { r } { \mathrm { I f } \frac { \rho _ { V } } { \rho _ { \varepsilon } } \leq \frac { 2 } { 1 + \delta } \Big [ \frac { n - 4 } { n } \Big ] , \frac { \partial } { \partial \rho _ { V } } \mathrm { M S E } ( P ^ { * } ) } \end{array}$ is positive; $\begin{array} { r } { \operatorname { i f } \frac { \rho _ { V } } { \rho _ { \varepsilon } } > \frac { 2 } { 1 + \delta } \left[ \frac { n - 4 } { n } \right] , \frac { \partial } { \partial \rho _ { V } } \operatorname { M S E } ( P ^ { * } ) } \end{array}$ is negative.

## Appendix B

## A Heterogeneous Social Network

In a heterogeneous social network, we have two types of participants: (1) participants whose degree is 0; and (2) participants whose degree is ݇. The proportions of degree 0 and degree ݇ participants are $a _ { 0 }$ and $1 - a _ { 0 } ,$ , respectively. Note that if $a _ { 0 } = 1$ or 0, a prediction market with a heterogeneous social network will degenerate to two special cases: a nonnetworked prediction market $( a _ { 0 } = 1 )$ or a prediction market with a regular social network $( a _ { 0 } = 0 )$ . We denote the set of degree 0 participants by $D _ { 0 } ,$ and the set of degree ݇ participants by $D _ { k } .$ . Therefore, the set of all participants $N = D _ { 0 } \cup D _ { k }$

In a heterogeneous social network, degree 0 and degree ݇ participants have different information sets. The inference process of a degree 0 participant is similar to that of a participant in a nonnetworked prediction market. For an individual $i \in D _ { 0 }$ , she makes an inference using her own private signal and the common prior:

$$
\begin{array}{r} \mathbf {E} _ {0} [ V | I _ {i} ] = \mathbf {E} _ {0} [ V | S _ {i} ] = \frac {\rho_ {V}}{\rho_ {\varepsilon} + \rho_ {V}} V _ {0} + \frac {\rho_ {\varepsilon}}{\rho_ {\varepsilon} + \rho_ {V}} S _ {i}, \\ \mathbf {V a r} _ {0} [ V | I _ {i} ] = 1 / (\rho_ {\varepsilon} + \rho_ {V}) \end{array}
$$

where $\mathbf { E } _ { 0 } [ V | I _ { i } ]$ and $\mathbf { V a r } _ { 0 } [ V | I _ { i } ]$ are the conditional expectation and conditional variance of a degree 0 participant.

The inference process of a degree ݇ participant is similar to that of a participant in a prediction market with a regular network. A degree ݇ participant’s information set includes her private signal, her friends’ private signals (݇ signals), and the common prior. For an individual $j \in$ $D _ { k } ,$ , she makes an inference as follows:

$$
\begin{array}{r} \mathbf {E} _ {k} [ V | I _ {j} ] = \frac {\rho_ {V}}{(k + 1) \rho_ {\varepsilon} + \rho_ {V}} V _ {0} + \frac {\rho_ {\varepsilon}}{(k + 1) \rho_ {\varepsilon} + \rho_ {V}} S _ {i} + \sum_ {h \in N _ {j} (g)} \frac {\rho_ {\varepsilon}}{(k + 1) \rho_ {\varepsilon} + \rho_ {V}} S _ {h}, \\ \mathbf {V a r} _ {k} [ V | I _ {j} ] = 1 / [ (k + 1) \rho_ {\varepsilon} + \rho_ {V} ] \end{array}
$$

where $\mathbb { E } _ { k } \big [ V | I _ { j } \big ]$ and $\mathbf { V a r } _ { k } \big [ V | I _ { j } \big ]$ are the conditional expectation and conditional variance of a degree ݇ participant. The market clearing condition is given by:

$$
\sum_ {i \in D _ {0}} x _ {i} ^ {*} + \sum_ {j \in D _ {k}} x _ {j} ^ {*} = 0
$$

where $x _ { i } ^ { * }$ and $x _ { j } ^ { * }$ indicate the optimal positions of degree 0 and degree ݇ participants respectively and are given as follows:

$$
x _ {i} ^ {*} = \frac {\mathbf {E} _ {0} [ V | I _ {i} ] - P}{2 \gamma \mathbf {V a r} _ {0} [ V | I _ {i} ]}, x _ {j} ^ {*} = \frac {\mathbf {E} _ {k} [ V | I _ {j} ] - P}{2 \gamma \mathbf {V a r} _ {k} [ V | I _ {j} ]}
$$

The equilibrium is characterized in the following proposition:

Proposition B.1 (Prediction Market Equilibrium in a Heterogeneous Social Network) In a prediction market with a heterogeneous social network, the equilibrium prediction market price is given by

$$
\begin{array}{r l} & P ^ {*} = \frac {\frac {a _ {0} n}{\mathbf {V a r} _ {0} [ V | I _ {i} ]}}{\frac {a _ {0} n}{\mathbf {V a r} _ {0} [ V | I _ {i} ]} + \frac {(1 - a _ {0}) n}{\mathbf {V a r} _ {k} [ V | I _ {j} ]}} \sum_ {i \in D _ {0}} \frac {\mathbf {E} _ {0} [ V | I _ {i} ]}{a _ {0} n} + \frac {\frac {(1 - a _ {0}) n}{\mathbf {V a r} _ {k} [ V | I _ {j} ]}}{\frac {a _ {0} n}{\mathbf {V a r} _ {0} [ V | I _ {i} ]} + \frac {(1 - a _ {0}) n}{\mathbf {V a r} _ {k} [ V | I _ {j} ]}} \sum_ {j \in D _ {k}} \frac {\mathbf {E} _ {k} [ V | I _ {j} ]}{(1 - a _ {0}) n} \\ & = \delta V _ {0} + (1 - \delta) V + \frac {\rho_ {\varepsilon}}{[ a _ {0} + (1 - a _ {0}) (k + 1) ] \rho_ {\varepsilon} + \rho_ {V}} \Bigl [ \sum_ {i \in D _ {0}} \frac {\varepsilon_ {i}}{n} + (k + 1) \sum_ {j \in D _ {k}} \frac {\varepsilon_ {j}}{n} \Bigr ] \end{array}
$$

where $\begin{array} { r } { \delta = \frac { \rho _ { V } } { [ a _ { 0 } + ( 1 - a _ { 0 } ) ( k + 1 ) ] \rho _ { \varepsilon } + \rho _ { V } } . } \end{array}$ The equilibrium position for individual $\begin{array} { r } { i \in D _ { 0 } \ i s \ x _ { i } ^ { * } = \frac { E _ { 0 } \left[ V \left| I _ { i } \right. \right] - P ^ { * } } { 2 \gamma V a r _ { 0 } \left[ V \left| I _ { i } \right. \right] } , } \end{array}$ and the equilibrium position for individual $\begin{array} { r } { j \in D _ { k } \mathrm { ~ } i s \mathrm { ~ } x _ { j } ^ { * } = \frac { E _ { k } [ V | I _ { j } | - P ^ { * }  } {  2 \gamma V a r _ { k } [ V | I _ { j } ]  } } \end{array}$

The market price, $P ^ { * } { } _ { ; }$ , in a heterogeneous social network is a weighted average of the individual expectations, and the weight depends on $\mathbf { V a r } _ { 0 } [ V | I _ { i } ]$ and $\mathbf { V a r } _ { k } \big [ V | I _ { j } \big ]$ . In a nonnetworked prediction market or a prediction market with a regular network, $P ^ { * }$ is a simple average of individual expectations and is independent of $\mathbf { V a r } [ V | I _ { i } ]$ [. This is because in these two cases, $\mathbf { V a r } [ V | I _ { i } ]$ is the same across participants and cancels in the market clearing condition. However, in a heterogeneous social network, $\mathbf { V a r } _ { 0 } [ V | I _ { i } ] \neq \mathbf { V a r } _ { k } \big [ V | I _ { j } \big ]$ , so $P ^ { * }$ depends on both $\mathbf { V a r } _ { 0 } [ V | I _ { i } ]$ and $\mathbf { V a r } _ { k } \big [ V | I _ { j } \big ]$

Then, we compute the MSE of $P ^ { * }$ in a prediction market with a heterogeneous social network:

$$
\mathrm{MSE} (P ^ {*}) = \mathbf {E} [ (V - P ^ {*}) ^ {2} ] = \frac {\rho_ {V} + \frac {1}{n} a _ {0} \rho_ {\varepsilon} + \frac {1}{n} \rho_ {\varepsilon} (1 - a _ {0}) (k + 1) ^ {2}}{\left[ [ a _ {0} + (1 - a _ {0}) (k + 1) ] \rho_ {\varepsilon} + \rho_ {V} \right] ^ {2}}\tag{B.1}
$$

Note that when $a _ { 0 } = 1$ , the MSE in a prediction market with a heterogeneous social network will be degenerated to equation 7, the MSE in a nonnetworked prediction market; when $a _ { 0 } = 0$ , the MSE in equation B.1 will be degenerated to equation 11, the MSE in a regular network. When $n \to \infty$ , the MSE in equation B.1 converges to $\frac { \rho _ { V } } { \left[ [ a _ { 0 } + ( 1 - a _ { 0 } ) ( k + 1 ) ] \rho _ { \varepsilon } + \rho _ { V } \right] ^ { 2 } } .$ . If we compare the MSEs in different cases, we obtain th following proposition:

Proposition B.2 (MSE Comparison) When $n \to \infty$ , the MSE in a nonnetworked prediction market is greater than the MSE in a prediction market with a heterogeneous social network, and the MSE in a prediction market with a heterogeneous social network is greater than the MSE in a prediction market with a regular social network.

In the following proposition, we examine the impact of the precision of public and private information.

Proposition B.3 (Comparative Statics on MSE) In a prediction market with a heterogeneous social network, the MSE of the forecast $P ^ { * }$ decreases with the number of prediction market participants, ݊, and the precision of private signals, ߩ<sub>ఌ</sub>. $\begin{array} { r } { I f \ \frac { \rho _ { V } } { \rho _ { \varepsilon } } \leq \frac { n - 2 } { n } a _ { 0 } \ 1 } \end{array}$ $\textstyle ( 1 - a _ { 0 } ) ( k + 1 ) \left[ { \frac { n - 2 ( k + 1 ) } { n } } \right] .$ , the MSE increases with the precision of public information; $\begin{array} { r } { i f _ { \rho _ { \varepsilon } } ^ { \rho _ { V } } > \frac { n - 2 } { n } a _ { 0 } + ( 1 - a _ { 0 } ) ( k + 1 ) \left[ \frac { n - 2 ( k + 1 ) } { n } \right] , } \end{array}$ , the MSE decreases with the precision of public information.

Similarly, Proposition B.3 shows that in a prediction market with a heterogeneous social network, increased precision of private information always enhances the prediction market accuracy, but increased precision of public information might be detrimental under some marke conditions. The marginal line in a heterogeneous social network $\begin{array} { r } { , \frac { \hat { \rho } _ { V } } { \rho _ { \varepsilon } } = \frac { n - 2 } { n } a _ { 0 } + ( 1 - a _ { 0 } ) ( k + 1 ) \left[ \frac { n - 2 ( k + 1 ) } { n } \right] } \end{array}$ , is between the marginal line in a nonnetworked prediction market, $\frac { \rho _ { V } } { \rho _ { \varepsilon } } = \frac { n - 2 } { n } ;$ , and the marginal line in a regular social network, $\begin{array} { r } { \frac { \rho _ { V } } { \rho _ { \varepsilon } } = \left( k + 1 \right) \left[ \frac { n - 2 \left( k + 1 \right) } { n } \right] } \end{array}$ . The following numerical example illustrates the market conditions in which increased precision of public information is detrimental in a prediction market with a heterogeneous social network. Figure B.1 depicts the contour lines of the MSE in a heterogeneous social network when $n = 5 0 , k =$ 9, and $a _ { 0 } = 0 . 8$ . The marginal line in a heterogeneous social network (the solid line) is between the marginal line in a nonnetworked prediction market (the dashed line) and the marginal line in a regular social network (the dash-dot line). It means that Region II in a heterogeneous network is larger than that in a nonnetworked prediction market, but smaller than that in a regular network under the chosen parameter values. The intuition is that a heterogeneous network is a linear combination of a regular network and a nonnetworked environment.

Figure B1. The Impact of Public Information Precision on Prediction Market Performance (Heterogeneous Network), n = 50, k = 9, a<sub>0</sub> = 0.8

Therefore, the marginal line in a heterogeneous social network, $\begin{array} { r } { \frac { \rho _ { V } } { \rho _ { \varepsilon } } = \frac { n - 2 } { n } a _ { 0 } + ( 1 - a _ { 0 } ) ( k + 1 ) \left[ \frac { n - 2 ( k + 1 ) } { n } \right] } \end{array}$ , is a linear combination of the two: i $\begin{array} { r } { \mathrm { f } a _ { 0 } = 1 , \frac { \rho _ { V } } { \rho _ { \varepsilon } } = \frac { n - 2 } { n } ; \mathrm { i f } a _ { 0 } = 0 , \frac { \rho _ { V } } { \rho _ { \varepsilon } } = \left( k + 1 \right) \left[ \frac { n - 2 \left( k + 1 \right) } { n } \right] } \end{array}$

![](/api/attachments/32E665DK/fulltext/images/1a679c2ef22d2e37dcfcab436cc5364097670542fd0d6dd49ab50e5e442b682b.jpg)

## Appendix C

## Selection of Prediction Market Participants

An interesting observation from Propositions 8, 9, and 10 is that a socially embedded prediction market with low precision of private information may perform as well as a nonnetworked prediction market with high precision of private information. The following numerical example in Figure C.1 illustrates the impacts of the precision of private information, $\rho _ { \varepsilon } ,$ and the level of social interactions, $k ,$ on prediction market performance when $n = 5 0$ and $\rho _ { V } = 0 . 2 . \ : \mathrm { A s }$ we expected, prediction market performance increases with $\rho _ { \varepsilon }$ and ݇. In a nonnetworked prediction market $( k = 0 ) , \mathrm { i f } \rho _ { \varepsilon } = 0 . 1 2 5$ , the MSE is around 2. To reach a similar level of MSE, much lower precision of private information is needed in a socially embedded prediction market with $k = 5 \colon \rho _ { \varepsilon } = 0 . 0 2 5$

A managerial implication of this result is about the selection of prediction market participants. In general, an internal employee has two types of skills: "work skills" and "social skills." In our context, the level of work skills refers to the ability to acquire precise private information (knowledge creation and information production) and is measured by $\rho _ { \varepsilon } .$ . In contrast, the level of social skills refers to the ability to communicate and share information with colleagues (knowledge transfer and information communication) and is measured by ݇. Intuitively, a manager should select employees who have a high level of work skills $( \rho _ { \varepsilon } )$ as prediction market participants. This is also consistent with Proposition 10. However, Propositions 8 and 9 show that the level of social skills (݇) also matters when we consider prediction market performance. A group of participants who have a medium level of work skills but a high level of social skills may outperform those who have a high level of work skills but a low level of social skills. Actually, Figure C.1 visually shows this implication by varying $\rho _ { \varepsilon }$ and ݇.

![](/api/attachments/32E665DK/fulltext/images/4ed00803fdd6ce59aba61a625ae81a28c904e983a78d26ab575d4290f968653e.jpg)  
Figure C1. The Impact of Social Interaction on Prediction Market Performance, n = 50 and <sub>ࢂ</sub>࣋ ૙ = . ૛

## Appendix D

## Additional Numerical Analysis

To provide a benchmark, in Figure D.1, we depict the nonnetworked case using the same parameter values as those in Section 4.3. The pattern is similar, but we have two additional observations: (i) The MSE in a nonnetworked prediction market is significantly greater than that in a socially embedded prediction market, which is consistent with the spirit of Proposition 5. (ii) The range of a detrimental effect of public information is smaller in a nonnetworked prediction market than in a socially embedded prediction market under the chosen parameter values. This is reminiscent of Proposition 11.

![](/api/attachments/32E665DK/fulltext/images/c857f09619c41af07ee12c65b9b111c566b4e38aa7094bb204575328adce2ceb.jpg)  
Figure D1. The Effect of the Precision of Public Information on the MSE in a Nonnetworked Prediction ૚ .૙ =<sub>ࢿ</sub>࣋ and ,<sub>૙</sub> = ૚૙ࢂ ,૙૞ = ࢔ ,Market

We also conduct simulation analysis to examine the impact of social influence. In our numerical analysis, 20% of prediction market participants are experts and they have more precise private signals (the precision is twice as the precision of private signals of ordinary participants). In this case, people will place larger weights on the information from these experts. The simulation results in a benchmark nonnetworked market and in a regular social network (k = 2) are presented in Figures D2 and D3, respectively.

![](/api/attachments/32E665DK/fulltext/images/41e8b407935d8d9681371e65c2083f74ff8ab2dd2cef5e7c7b8c041dd2d34583.jpg)  
Figure D2. The Effect of the Precision of Public Information in a Nonnetworked Prediction Market: Experts Versus Ordinary Participants

![](/api/attachments/32E665DK/fulltext/images/ce6d94529c196e921c4d3b185fe1e71fdc8bc5cce6f5dbcbff141edc88bc7c13.jpg)  
Figure D3. The Effect of the Precision of Public Information in a Regular Social Network: Experts Versus Ordinary Participants  
The simulation results with the heterogeneous precision setting in additional complicated social networks are presented in Figure D4. We find that our results are robust: greater public information precision may be detrimental to prediction market accuracy.

![](/api/attachments/32E665DK/fulltext/images/68774fdaa345f60042d3e6ece977af1c8b1bc34d5c89a95248d3b5fa3db3bf51.jpg)  
(a) Gilbert Network

![](/api/attachments/32E665DK/fulltext/images/652a091b90500b070eb7ca54ef9d70801c3367a188b5e7c563fdff1d407444b1.jpg)  
(b) Erdos-Renyi Network

![](/api/attachments/32E665DK/fulltext/images/bf3c60b20c0ae804410110ee741a6e0cd3586d9c70c64031fc1c81a228dbbf3b.jpg)  
(c) Small-World Network

![](/api/attachments/32E665DK/fulltext/images/c7700f8001119a4ea2452ca79d0533fb253da392418dc0a8c90c33a8e8c50388.jpg)  
(d) Preferential Attachment Network

Figure D4. The Effect of the Precision of Public Information in Complicated Social Networks: Experts Versus Ordinary Participants

## Appendix E

## Forecast-Report Prediction Market Mechanism

In real-world prediction markets, there are two commonly used mechanisms of information aggregation: a security-trading mechanism and a forecast-report mechanism (Jian and Sami 2012). A security-trading mechanism is similar to a competitive financial market, and people trade securities based on their forecasts. The market clears when the aggregate demand for securities equals the supply, and market clearing determines the prediction market price. In this paper, we focus mainly on the security-trading mechanism.

A forecast-report mechanism is a proper scoring rule that elicits the true beliefs of participants as probabilistic forecasts. The proper scoring rules give the participants the incentives to report truthfully, then the principal aggregates the private information of all participants. For instance, the Ford Prediction Exchange (FPEx) was the first prediction market at Ford, developed in 2006. Instead of buying and selling stock, it used a scored polling mechanism in which traders made forecasts by specifying the individual predictions (Montgomery et al. 2013). In this appendix, we show that the overweight issues still exist in a forecast-report prediction market mechanism.

The basic model setup of a forecast-report mechanism is similar to that in the “Model Setup” section. All the prediction market participants share a common prior on ܸ, given by

$$
V \sim N (V _ {0}, 1 / \rho_ {V})
$$

Before the prediction market opens, each participant can access a private signal:

$$
S _ {i} = V + \varepsilon_ {i}, \varepsilon_ {i} {\sim} N (0, 1 / \rho_ {\varepsilon}), \varepsilon_ {i} \perp \varepsilon_ {j}
$$

The manager designs a quadratic loss function to elicit the private information of prediction market participants. A participant’s payoff function is given by

$$
w (x _ {i}, V) = a - b (x _ {i} - V) ^ {2}
$$

where $x _ { i }$ is the prediction reported by participant ݅, and $b ( x _ { i } - V ) ^ { 2 }$ is a quadratic penalty term for mistakes in the forecast. The optimal report for participant ݅		is $x _ { i } ^ { * } = E [ { \bar { V } } | I _ { i } ] = E [ V | S _ { i } ]$ [, where $I _ { i }$ is the information set of participant ݅.

Following the prior literature (Armstrong 2001), we assume that the manager adopts a simple averaging rule to aggregate all participants’ forecasts, and his prediction is

$$
\begin{array}{r} \frac {1}{n} \sum_ {i = 1} ^ {n} x _ {i} ^ {*} = \frac {1}{n} \sum_ {i = 1} ^ {n} \mathbf {E} [ V | I _ {i} ] = \frac {\rho_ {V}}{\rho_ {\varepsilon} + \rho_ {V}} V _ {0} + \frac {1}{n} \sum_ {i = 1} ^ {n} \frac {\rho_ {\varepsilon}}{\rho_ {\varepsilon} + \rho_ {V}} S _ {i} \\ = \frac {\rho_ {V}}{\rho_ {\varepsilon} + \rho_ {V}} V _ {0} + \frac {\rho_ {\varepsilon}}{\rho_ {\varepsilon} + \rho_ {V}} V + \frac {\rho_ {\varepsilon}}{\rho_ {\varepsilon} + \rho_ {V}} \overline {{\varepsilon}} \end{array}
$$

The weight on public information in a forecast-report mechanism is given by

$$
W _ {F} = \frac {\rho_ {V}}{\rho_ {\varepsilon} + \rho_ {V}} \geq W _ {m} = \frac {\rho_ {V}}{n \rho_ {\varepsilon} + \rho_ {V}}
$$

where $W _ { m }$ is the efficient weight on public information. Therefore, the issue of overweighting public information still exists in a forecastreport prediction market mechanism.

## Appendix F

## Trade-Off between Information Precision and Information Diversity

As argued in Keuschnigg and Ganser (2017), crowd wisdom does not only depend on the prediction ability/precision of agents, but also depends on the information diversity. In our simulation analysis, we examine the trade-off between information precision and information diversity by looking at two departments within a company. In Department H, each employee can access a high precision signal with $\rho _ { \varepsilon H } =$ 0.15, while in Department L, each employee receives a low precision signal with $\rho _ { \varepsilon L } = 0 . 1$ . In other words, employees in Department H have more precise information on this specific prediction market topic. For instance, employees in the marketing department of a company may have more precise information on product sales. In order to capture correlated information sources within a department, we assume that the private signal errors of two employees in a same department are positively correlated, but are independent if they are from different departments.

We consider an optimal selection problem of prediction market participants. Suppose that a corporate manager wants to a build a prediction market with $n = 5 0$ participants, and all prediction market participants will be chosen from either Department H or Department L (without loss of generality, we assume that each department has 50 employees). In other words, $n _ { H } + n _ { L } = 5 0$ , where $n _ { H }$ is the number of participants chosen from Department $H ,$ and $n _ { L }$ is the number of participants chosen from Department L. In the following simulation analysis, we examine the impact of information diversity on the composition of prediction market participants. For simplicity, we set parameter values $V _ { 0 } = 1 0 _ { : }$ $\rho _ { V } = 0 . 1$ and ݇ = 1. Since we are interested in the impact of information diversity, we vary the correlation coefficient of private signal errors of employees in a same department: $\delta = 0 , 0 . 3 , 0 . 6 , 0 . 9$ . Under each correlation coefficient, we run the simulation 10,000 times to compute the optimal number of participants chosen from Department $H , n _ { H } ^ { * }$ , that achieves the highest prediction performance (the lowest MSE), and plot the following figure.

![](/api/attachments/32E665DK/fulltext/images/ee348fe6f5cf382c87fa7ae6fc126d7d193c930088613f46ab054345f79686c3.jpg)  
Figure F1. The Trade-Off between Information Precision and Information Diversity

Apparently, when the correlation coefficient $\delta = 0 _ { ; }$ all prediction market participants should come from Department H. The reason is that when information within a department is not correlated, the effect of information precision dominates: The manager should choose employees with the highest prediction precision. As the correlation coefficient increases, we find that the optimal number of participants chosen from Department $H , n _ { H } ^ { * }$ , decreases, which shows a clear trade-off between information precision and information diversity. When δ is high, the information sources within a same department are highly correlated. Although Department H employees have more precise information, it is beneficial to have some Department L employees as diverse information sources.

## References

Armstrong, J. S. 2001. Principles of Forecasting: A Handbook for Researchers and Practitioners, Norwell, MA: Kluwer Academic.

Jian, L., and Sami, R. 2012. “Aggregation and Manipulation in Prediction Markets: Effects of Trading Mechanism and Information Distribution,” Management Science (58:1), pp. 123-140.

Keuschnigg, M., and Ganser, C. 2017. “Crowd Wisdom Relies on Agents’ Ability in Small Groups with a Voting Aggregation Rule,” Management Science (63:3), pp. 818-828.

Montgomery, T. A., Stieg, P. M., Cavaretta, M. J., and Moraal, P. E. 2013. “Experience from Hosting a Corporate Prediction Market: Benefits Beyond the Forecasts,” in Proceedings of the 19<sup>th</sup> ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, New York: ACM Press, pp. 1384-1392
