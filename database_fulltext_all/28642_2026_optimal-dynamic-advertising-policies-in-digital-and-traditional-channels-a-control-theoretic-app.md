---
otero_id: 28642
otero_key: "ZV22Z4YT"
title: "Optimal Dynamic Advertising Policies in Digital and Traditional Channels: A Control-Theoretic Approach"
authors: "Rui Guo; Yonghua Ji; Zhengrui Jiang"
year: "2026"
journal: "Information Systems Research"
doi: "10.1287/isre.2023.0779"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Optimal Dynamic Advertising Policies in Digital and Traditional Channels: A Control-Theoretic Approach

Rui Guo,<sup>a</sup> Yonghua Ji,<sup>b</sup> Zhengrui Jiang<sup>c,</sup>\*

<sup>a</sup> School of Business, Nanjing University, Nanjing 210093, China; <sup>b</sup> School of Business, University of Alberta, Edmonton, Alberta T6G 2R6, Canada; <sup>c</sup> Shenzhen Finance Institute, School of Management and Economics, The Chinese University of Hong Kong, Shenzhen 518172, China \*Corresponding author

Contact: ruiguo@smail.nju.edu.cn, https://orcid.org/0009-0006-8111-385X (RG); yji@ualberta.ca, https://orcid.org/0000-0001-7507-8548 (YJ); zjiang@cuhk.edu.cn, https://orcid.org/0000-0002-8576-7643 (ZJ)

Received: December 17, 2023 Revised: September 14, 2024; March 19, 2025 Accepted: April 11, 2025 Published Online in Articles in Advance: May 19, 2025

https://doi.org/10.1287/isre.2023.0779

Copyright: © 2025 INFORMS

Abstract. In today’s complex and dynamic market environment, simultaneously deploying and optimizing multiple advertising channels is crucial for firms’ success. In the present study, we apply optimal control theory to address the multichannel advertising optimization problem for a monopolistic firm that manages a digital ad channel and a traditional ad channel. By considering the competitive relationship between advertising efforts in different channels in satisfying consumers’ informational needs, this study explicitly models their substitution effect. Furthermore, we propose an alternative approach to account for different decay rates of incremental goodwill in the two channels, allowing the system dynamics to be directly represented by the firm’s total goodwill without separating it into multiple channel-specific components. Technically, this approach leads to the system dynamics being governed by an integro-differential equation rather than an ordinary differential equation. Our analysis reveals that the marginal value of goodwill in the digital ad channel is greater than that in the traditional ad channel due to a lower decay rate. However, this comparative advantage of the digital ad channel progressively diminishes over time. As a result, the firm should always invest in digital advertising, whereas employing traditional advertising only when the comparative advantage of the digital ad channel becomes weak in later stages. When additionally considering the synergistic effect between advertising efforts in the two channels, we find that as the intensity of synergistic effect increases, it is optimal to adopt traditional advertising earlier; when the synergistic effect is sufficiently strong, the optimal traditional advertising effort will remain positive throughout the planning horizon.

History: Olivia Liu Sheng, Senior Editor; Hong Guo, Associate Editor. Funding: R. Guo’s research is supported by the China Scholarship Council [Grant 202406190180]. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2023.0779.

Keywords: multichannel advertising • goodwill • substitution effect • synergistic effect • optimal contro

## 1. Introduction

Over the past decade, the landscape of the advertising industry has experienced profound changes. The advancement of digital technology has facilitated the expansion of firms’ reach to consumers through a great variety of channels, including online platforms, socia media, search engines, and streaming services (Zhu et al. 2024). Combined with the diversification of traditiona media, it gives rise to a portfolio of multiple advertising channels, which allows consumers to autonomously opt for their preferred channel at each phase of the purchasing journey, thereby effectively granting firms access to a broader consumer base (Cui et al. 2021). Although the proliferation of various advertising channels brings new opportunities for firms, it also poses a challenge: How should firms dynamically allocate their advertising efforts across multiple channels over time to ensure optimal resource utilization and maximize their profits?

Because of the varying effectiveness, cost, and reach of each channel, as well as the potential interactions between different channels, solving this problem is not a trivial task.

The dynamic allocation of advertising efforts across multiple channels has received considerable attention from both researchers and practitioners. Many dynamic advertising models in the multichannel setting have been proposed in the past few decades (Fruchter and Kalish 1998, Naik and Raman 2003, Raman et al. 2012, Danaher 2023, Zhu et al. 2024). It is widely recognized that firms should not only consider the distinct characteristics of each channel (e.g., advertising effectiveness and cost), but also account for the synergistic effect between advertising in different channels, which refers to the mutually reinforcing impact that arises when different forms of advertising are employed in conjunction (Naik et al. 2005). However, it is important to note that another effect—the substitution effect—between advertising in different channels has not been explicitly taken into account in dynamic advertising models, despite the fact that it has been demonstrated by many empirical studies (Goldfarb and Tucker 2011, Dinner et al. 2014). Here, the substitution effect specifically refers to the phenomenon that the marginal return of advertising in one channel declines when advertising investments in other channels increase (Abedi et al. 2022). To formulate optimal advertising policies across multiple channels, it is necessary for firms to consider the synergistic and substitution effects simultaneously.

Furthermore, prior research typically assumes that the incremental goodwill or sales generated by advertising in different channels follow the same decay rate; the limited few exceptions (Abedi et al. 2022, Zhu et al. 2024) allow different decay rates, but do not explicitly incorporate interactions between advertising in different channels. Because of the inherent differences between multiple channels, it is crucial to recognize that they vary not only in advertising effectiveness and cost, but also in the decay rates of goodwill. For instance, researchers have found that, compared with traditional ad channels (e.g., television and print ads), advertising content presented through digital ad channels (e.g., online websites, search engines, and social media) is more relevant to the interests of target consumers, more visually appealing, and allow real-time interactions with consumers (Rodgers and Thorson 2017). These features make digital advertising more difficult to be forgotten by consumers, thereby indicating lower decay rates in digital ad channels (Kwon et al. 2019). Hence, when deriving the optimal advertising policies across multiple channels, a model incorporating the varying decay rate in each channel reflects reality better, thus generating more meaningful and reliable managerial insights.

To fill the aforementioned research gaps, this study applies optimal control theory as an analytical framework to address the dynamic optimization problem of allocating advertising efforts across multiple channels. We consider a firm that manages two different channels, that is, a digital ad channel and a traditional ad channel. In our model, the state variable is the stock of goodwill that captures the cumulative effect of current and past advertising efforts in both channels (Nerlove and Arrow 1962), and the control variables are the firm’s advertising efforts in two channels. The firm’s objective is to maximize the present value of its profit stream over a finite time horizon.

We next elaborate on how our model takes into account the substitution effect between advertising efforts in two channels and their different decay rates. First, to capture the substitution effect, we consider the fact that advertisements in different channels deliver similar informational content to consumers by promoting the same products. As a firm increases its advertising investments in one channel, it amplifies the volume of product-related information conveyed to consumers, thereby satisfying their informational needs for making informed purchasing decisions. Consequently, additional information from other channels becomes redundant, reducing its perceived value and usefulness in influencing consumer decisions. This effectively captures the substitution effect between advertising efforts in different channels (Dinner et al. 2014, Abedi et al. 2022). Second, different from previous studies, we propose an alternative approach to incorporate the different decay rates associated with the two channels, such that the system dynamics can be directly represented by a firm’s total goodwill without separating it into multiple channel-specific components. Specifically, we assume that the lifetime of the incremental goodwil generated by advertising effort in each channel follows a different distribution, thus leading to a different survival function (Hartl 1984). Here, the lifetime of each unit of goodwill refers to the period of time during which consumers remember the goodwill, and the survival function of the lifetime of each unit of goodwill can be interpreted as the probability that goodwill can still be remembered by consumers at a certain time. Technically, this assumption results in the state dynamics of our model being governed not by an ordinary differential equation, but rather by an integro-differential equation. Despite the increased complexity, we are still able to derive a closed-form solution, which further solidifies the contribution of this work.

Given the complexity of our problem and for better clarity, we consider only the substitution effect in the base model while incorporating both substitution and synergistic effects in the subsequent extended model. In both models, we assume that the decay rates associated with the two channels are different. Unlike the majority of prior studies that focus on the optimal long-run stationary equilibrium in an infinite time horizon (Sethi 2022, p. 98), we analyze how a firm’s optimal advertising effort in each channel dynamically changes over time in a finite time horizon (i.e., the optimal trajectory during the entire process). Although a finite time horizon makes the optimal control problem more challenging to solve, it better aligns with real-world settings faced by decision makers, thus offering more practical managerial insights (Raman et al. 2012).

Several novel findings emerge from our analysis. First, from the base model, we find that (i) because the digital ad channel exhibits a lower decay rate than the traditional ad channel, its marginal value of goodwill (i.e., shadow price of goodwill) is greater. However, this comparative advantage of the digital ad channel gradu ally diminishes over time; (ii) the firm should always invest in the digital ad channel, while employing tradi tional advertising only when the comparative advantage of the digital ad channel becomes weak in later stages. This strategy allows the firm to combine and leverage the advantages offered by both channels, thus maximizing its total profit; and (iii) when it is optimal for the firm to invest in two channels simultaneously, the ratio of the optimal advertising efforts between the digital and traditional ad channels monotonically decreases with time. In other words, it implies that as the comparative advantage of the digital ad channel weakens over time, the firm should progressively allocate more advertising effort to the traditional ad channel. Second, from the extended model, we find that (i) as the intensity of synergistic effect increases, the firm should adopt traditional advertising earlier; with a sufficiently large intensity, the optimal traditional advertising effort should remain positive throughout the entire planning horizon; (ii) the trajectory of the optimal allocation ratio between digital and traditional advertising efforts depends on the intensity of synergistic effect. When the synergistic effect is weak, the optimal allocation ratio monotonically decreases with time. When the synergistic effect is strong, the mechanism of a positive feedback loop between the digital and traditional advertising efforts kicks in, leading to an increasing trend in the trajectory of the optimal allocation ratio; and (iii) as the synergistic effect intensifies, the firm should allocate more budget to the channel with weaker advertising power, which depends on the direct ad spending cost, the indirect information opportunity cost, and the decay rate of incremental goodwill.

The remainder of the paper is organized as follows. We review the related literature in Section 2 and present our base model in Section 3. In Section 4, we derive the closed-form solutions for the optimal advertising efforts in two channels and conduct further analyses. In Section 5, we analytically and numerically examine the sensitivity of the optimal advertising efforts with respect to key parameters. In Section 6, we analyze two extended models that consider the synergistic effect and three advertising channels, respectively. Finally, concluding remarks are provided in Section 7.

## 2. Literature Review

The optimal allocation of advertising efforts across multiple channels or media has garnered significant attention in the last few decades. To investigate the most effective strategies, various methods and approaches have been employed. In this study, we focus on research that applies optimal control theory as an analytical framework to address the problem of multichannel ad budget allocation.

When considering the impact of advertising efforts across multiple channels on a firm’s goodwill or product sales, many prior studies assume that advertising efforts in different channels are independent of each other, and their effects on the firm’s goodwill or sales exhibit an additive functional form (Chintagunta and Vilcassim 1994, Fruchter and Kalish 1998, Raman et al. 2012, Abedi et al. 2022, Danaher 2023, Zhu et al. 2024).

Although this assumption of cross-channel advertising independence ensures analytical tractability, it overlooks the interactions between advertising efforts in different channels and thus is unable to adequately reflect reality. The seminal paper by Naik and Raman (2003) takes into account the synergistic effect between different advertising; that is, simultaneously deploying multiple channels can yield outcomes that surpass the additive effects of deploying each channel in isolation. Their study considers two advertising channels, and the dynamics of a firm’s sales is influenced not only by the advertising effort in each channel, but also by the positive impact of their interaction. Assuming an infinite time horizon, they derive the firm’s optimal long-run stationary equilibrium.

Although the work of Naik and Raman (2003) marks a significant step forward in understanding the optimal allocation of advertising efforts across multiple channels, it still has room for improvement. In particular, (i) the prior work only applies to monopolistic firms while leaving out the interfirm competition in duopoly or oli gopoly markets; (ii) it assumes a deterministic state dynamics of a firm’s sales and does not consider the impact of uncertainty; and (iii) its theoretical analysis focuses solely on the optimal long-run stationary equilibrium (i.e., steady state), without considering how the optimal advertising effort in each channel dynamically changes over time.

Subsequent research has aimed to address these limitations. Specifically, Raman and Naik (2004) consider the impact of uncertainty by incorporating a Wiener process (also known as a Brownian motion). Naik et al. (2005) investigate competition across multiple firms with two marketing instruments (i.e., advertising and price promotion) in a dynamic oligopoly market. They extend the Lanchester model by incorporating the synergistic effect between different marketing instruments and estimate the market share of five detergent brands using Kalman filtering and maximum likelihood estimation. Prasad and Sethi (2009) propose a stochastic optimal control model with two advertising channels. By assuming that the value function is a linear function of the state variable, they derive explicit closed-loop solutions, where the optimal advertising effort in each channel depends on the firm’s prevailing sales.

Additionally, the model of Naik and Raman (2003) has been further extended to encompass more application scenarios. Naik and Peters (2009) investigate the crossmedia and within-media synergistic effects by considering different types of media (e.g., online and offline chan nels) and their specific forms (e.g., paid search ads, television ads, and printed ads). Aravindakshan et al. (2015) explore how marketing managers of a blood bank should utilize various advertising media to effectively manage blood donations. In their model, the blood bank’s objective is to maintain blood collection within a certain range to prevent shortage and excess supply.

From the discussion above, it can be seen that prior research over the past two decades has made significant progress in optimal advertising allocation policies across multiple channels. However, there are still several research gaps to be addressed. First, prior studies have primarily focused on the synergistic effect between advertising efforts in different channels while not considering their substitution effect. In one exception, Abedi et al. (2022) investigate how the advertising budget for one channel changes with the total advertising budget for other channels, and distinguish between the synergistic effect and the substitution effect; however, their model does not explicitly incorporate the interactions between advertising in different channels. Additionally, one might expect that by assigning a negative coefficient to the interaction term between different advertising efforts in the model of Naik and Raman, the substitution effect can also be captured (Naik et al. 2005). However, we note that such a treatment will potentially lead to some issues. On the one hand, a negative interaction term suggests that the substitution effect dominates the synergistic effect, which may not hold in practice. On the other hand, an excessively strong substitution effect could cause the advertising effectiveness of one channel to become negative. This implies that advertising in a channel reduces instead of increasing the firm’s goodwill, which typically does not make practical sense. For these reasons, we conclude that existing models lack the capability to capture the substitution effect between advertising efforts in different channels, which is a research gap we aim to fill in this study.

Second, existing dynamic advertising models in the multichannel setting all implicitly assume that the incremental goodwill generated by advertising in different channels has the same decay rate, with only a few exceptions (Naik and Raman 2003, Abedi et al. 2022, Zhu et al. 2024). To capture different decay rates across multiple channels, previous studies typically decompose a firm’s total goodwill into individual goodwill in different channels (or, channel-specific goodwill). However, as suggested by the literature on advertising attribution (Berman 2018), because customers often interact with various channels and touchpoints before making a purchase, it is challenging for firms to explicitly distinguish and estimate the individual goodwill generated in each channel. For example, a brick-and-mortar retailer that simultaneously employs television commercials and social media ads will face great difficulty in determining the contribution of each channel to the total goodwill or sales. Different from previous studies, the present research proposes an alternative approach that allows the state equation to be directly represented by the dynamics of a firm’s total goodwill. Specifically, we assume that the lifetime of incremental goodwill generated from each channel follows a different distribution, and the retention of the incremental goodwill in each channel at a certain time is characterized by a unique survival function (Hartl 1984, Feichtinger et al. 1994). From a technical perspective, this treatment suggests that the system dynamics of our model is governed by an integro-differential equation instead of an ordinary differential equation. Furthermore, by jointly considering the substitution effect, synergistic effect, and differential goodwill decay rates across multiple channels, we are able to conduct a more comprehensive analysis that differs significantly from prior studies such as Naik and Raman (2003), Abedi et al. (2022), and Zhu et al. (2024).

In sum, this study fills several existing research gaps by assuming that (i) advertising in different channels competes with each other in fulfilling consumers’ informational needs and that (ii) the lifetime of incremental goodwill generated in each channel follows a different distribution. Furthermore, unlike most of previous studies that assume an infinite time horizon and focus on the optimal long-run stationary equilibrium, we are more interested in examining how a firm’s optimal advertising effort in each channel dynamically changes over time in a finite time horizon. Although the finite time horizon leads to more complexity, it makes our mode more realistic and thus able to offer more reliable managerial insights.

A summary of control-theoretic advertising models proposed for the multichannel setting is provided in Table A.1 in the Online Appendix, which highlights the differences between previous studies and ours. We introduce our model in the next section.

## 3. Base Model

Consider a monopolistic firm that plans to launch an advertising campaign for its product over a finite time window [0, T], where the terminal time T is exogenously determined. Let $u _ { 1 } ( t )$ and $u _ { 2 } ( t )$ denote the advertising efforts in digital and traditional ad channels, respec tively. As advertising campaigns through the two channels proceed, the firm collects and cumulates goodwill over time. Let G(t) denote the stock of goodwill that captures the cumulative effect of current and past advertising efforts in the two channels. For each channel $i \in \{ 1 , 2 \}$ , every time its advertising effort is exerted, it produces an instantaneous increase in the goodwill $( \mathrm { i . e . , }$ incremental goodwill), which then decays over time due to consumers’ forgetting of the advertising content. Because of the substitution effect between advertising efforts in the two channels, the production function of goodwill (also known as advertising response function; Feichtinger et al. 1994) for channel, i depends not only on the advertising effort in its own channel, but also on that in the other channel. Thus, we denote the production function of goodwill in channel i by $g _ { i } ( u _ { i } ( t ) , u _ { j } ( t ) )$ $i \neq j ,$ , the specific functional form of which will be discussed in detail later. As mentioned before, after the production of incremental goodwill, it experiences a subsequent decay process, which can be represented by a survival function of the lifetime of each unit of goodwill (Hartl 1984, Feichtinger et al. 1994). Because digital and traditional ad channels inherently have different characteristics (Rodgers and Thorson 2017, Kwon et al. 2019), it is plausible to assume that the lifetime of goodwill produced in each channel follows a different survival function. Denote the survival function of the lifetime of goodwill in channel i by S<sub>i</sub>(t). Then, the stock of goodwill can be expressed as the sum of the convolution of the production function of goodwill and the survival function of its lifetime in each channel (Hartl 1984):

$$
G (t) = G _ {0} + \sum_ {i = 1} ^ {2} \int_ {0} ^ {t} g _ {i} \bigl (u _ {i} (\tau), u _ {j} (\tau) \bigr) S _ {i} (t - \tau) d \tau ,\tag{1}
$$

where $G _ { 0 }$ denotes the initial value of goodwill at $t = 0$ Taking the time derivative, we can rewrite Equation (1) as the following integro-differential equation:

$$
\begin{array}{l} \dot {G} (t) = \sum_ {i = 1} ^ {2} \Big (g _ {i} (u _ {i} (t), u _ {j} (t)) \\ \qquad - \int_ {0} ^ {t} g _ {i} (u _ {i} (\tau), u _ {j} (\tau)) f _ {i} (t - \tau) d \tau \Big), \end{array}\tag{2}
$$

where f (t) is the density function of the lifetime of goodwill in channel $i ,$ that is $, f _ { i } ( t ) = - d S _ { i } ( t ) / d t$ . The second term in (2) is negative due to the decay of previously generated goodwill.

We now elaborate on the specific functional forms of $g _ { i } ( u _ { i } ( t ) , u _ { j } ( t ) ) , S _ { i } ( t )$ , and f (t). As mentioned before, the production function of goodwill in channel i depends on the advertising efforts in both channels due to their substitution effect. In the existing literature, discussions about the substitution effect between different advertising channels typically focus on the mechanism of “information substitution” (Dinner et al. 2014, p. 538; Abedi et al. 2022, p. 2144). Because advertisements in different channels promote the same products, they deliver similar informational content to consumers. As a firm intensifies its advertising investments in one channel, the amount of product-related information conveyed to consumers increases, thereby satisfying their informational needs to make informed purchasing decisions. Consequently, additional information from other channels becomes redundant, reducing its perceived value and usefulness in influencing consumer decisions. Mathematically, we specify

$$
g _ {i} (u _ {i} (t), u _ {j} (t)) = k _ {i} u _ {i} (t) (M - k _ {i} u _ {i} (t) - k _ {j} u _ {j} (t)),\tag{3}
$$

where $k _ { i }$ is the coefficient of advertising effectiveness in channel i and M is the initial level of consumers’ perceived information usefulness. For each channel, the rate at which consumers’ perceived information usefulness diminishes depends on its advertising effectiveness. The reason is that more effective advertisements provide more comprehensive product-related information. As a result, consumers will perceive subsequent advertisements delivered through the other channel as less valuable and useful. Furthermore, Equation (3) captures the diminishing marginal effect of advertising effort in each channel, which means that when the advertising effort in the other channel is held constant, the marginal return of advertising effort in one channel also declines as its advertising effort increases.

Regarding the functional forms of $S _ { i } ( t )$ and $f _ { i } ( t ) .$ , we assume that the lifetime of goodwill in each channel follows an exponential distribution with a different decay rate. In other words, it means that the amount of good will in each channel decays exponentially at a different rate. Essentially, an exponential decay suggests that the decay of goodwill at each instant is proportional to its prevailing level, which has been acknowledged and widely implemented in prior research (Nerlove and Arrow 1962, Feichtinger et al. 1994). Mathematically, we specify

$$
S _ {i} (t) = e ^ {- \delta_ {i} t}, f _ {i} (t) = \delta_ {i} e ^ {- \delta_ {i} t},\tag{4}
$$

where $\delta _ { i }$ is the decay rate in channel i. As discussed before, because previous studies have indicated that digital advertising is typically more difficult to be forgotten by consumers (Rodgers and Thorson 2017, Kwon et al. 2019), we assume $\delta _ { 1 } < \delta _ { 2 }$ , implying that the goodwill produced by digital advertising has a lower rate of decay compared with that produced by traditional advertising.

The firm’s objective is to maximize the net present value of its profit stream in [0, T]:

$$
\max _ {u _ {1} (t), u _ {2} (t)} \int_ {0} ^ {T} e ^ {- r t} \bigl (p G (t) - c _ {1} u _ {1} ^ {2} (t) - c _ {2} u _ {2} ^ {2} (t) \bigr) d t,\tag{5}
$$

where $p$ is the revenue rate, $c _ { i }$ is the unit cost of advertising in channe $i ,$ and r is the discount rate. Following the prior literature (Danaher 2023), we assume that the firm’s revenue is linearly proportional to the stock of goodwill and the advertising cost in each channel takes a quadratic form. Additionally, an implicit assumption made in the objective function (5) is that there is no sal vage value beyond the firm’s planning horizon, which essentially implies that any additional profit that can be generated by the remaining goodwill beyond the planning horizon is too uncertain to be worth considering. This assumption is reasonable for marketing campaigns of seasonal and one-time products (Jørgensen et al. 2006). Furthermore, we note that such an assumption is very common in the literature on optimal control theory because it ensures analytical tractability (Hu and Sun 2022). This treatment is also widely adopted in dynamic advertising research in the multichannel setting (Naik et al. 2005, Abedi et al. 2022). Therefore, we follow this tradition and adopt the zero salvage value assumption.

The firm’s optimization problem is to maximize (5) subject to (2), (3), and (4). To solve this optimal control problem, we apply Pontryagin’s maximum principle (Kamien and Schwartz 1991, Sethi 2022). The currentvalue Hamiltonian is formulated as

$$
\begin{array}{l} H = p G (t) - c _ {1} u _ {1} ^ {2} (t) - c _ {2} u _ {2} ^ {2} (t) \\ \qquad + \sum_ {i = 1} ^ {2} k _ {i} u _ {i} (t) (M - k _ {i} u _ {i} (t) - k _ {j} u _ {j} (t)) \\ \qquad \left(\lambda (t) - \int_ {t} ^ {T} e ^ {- r (\tau - t)} \lambda (\tau) f _ {i} (\tau - t) d \tau\right), \end{array}\tag{6}
$$

where $\lambda ( t )$ is the current-value adjoint variable associated with G(t) and satisfies

$$
\dot {\lambda} (t) = r \lambda (t) - p, \quad \lambda (T) = 0.\tag{7}
$$

It is important to note that, under our formulation where the state dynamics is given by an integro-differential equation rather than an ordinary differential equation, $\lambda ( t )$ only represents the current effect of marginal goodwill at time t. The future effect is captured by the integral term in (6). Define

$$
\varphi_ {i} (t) := \lambda (t) - \int_ {t} ^ {T} e ^ {- r (\tau - t)} \lambda (\tau) f _ {i} (\tau - t) d \tau .\tag{8}
$$

Then $\varphi _ { i } ( t )$ measures the total $( \mathrm { i . e . } ,$ , current and future) value of marginal goodwill in channel i and thus can be interpreted as its shadow price (Hartl 1984).

## 4. Optimal Advertising Policies

Because our optimization problem involves two control variables, an interior maximum exists only when the Hessian matrix is negative definite. We first specify the condition for the existence of an interior maximum.

Lemma 1. An interior maximum exists only when the following condition holds for all $t \in [ 0 , T ]$

$$
4 \big (c _ {1} + k _ {1} ^ {2} \varphi_ {1} (t) \big) \big (c _ {2} + k _ {2} ^ {2} \varphi_ {2} (t) \big) - k _ {1} ^ {2} k _ {2} ^ {2} \big (\varphi_ {1} (t) + \varphi_ {2} (t) \big) ^ {2} > 0,\tag{9}
$$

Notice that Inequality (9) can be satisfied with a relatively large value of $c _ { 1 }$ or $^ { c _ { 2 } , }$ which requires that the unit cost of digital or traditional advertising must not be too low. We note that this requirement is consistent with real-life observations. Although the development of information technology has significantly reduced the unit cost of digital advertising, the unit cost of traditional advertising remains high (Olson 2020). This is primarily due to (i) high production costs $( \mathrm { e . g . }$ , the usage of high-end equipment, professional actors, and intricate visual effects), (ii) high distribution costs $( \mathrm { e . g . } ,$ , the cost of printing and distributing magazines and newspapers), (iii) scarcity of premium advertising avenues (e.g., prime time television slots, full-page magazine ads), and (iv) broader reach to audiences. Marketing statistics (Mandese 2022) show that the average cost per mille (CPM) for traditional media was around \$16.14 in 2022, ranging from \$2 to \$54 depending on the specific medium (e.g., television, radio, print, and out-of-home ads). In contrast, CPMs for social media ads across different online platforms (e.g., Facebook, Twitter, Instagram, and LinkedIn) varied from \$5.76 to \$9.06, with an average of \$6.89 (Chawlani 2024). This reveals that traditional channels typically incur higher costs to reach customers. Thus, for simplicity, we will only consider situations where (9) holds. Then, the optimal advertising effort in each channel can be derived.

Proposition 1. Given the existence of an interior maximum, the optimal advertising effort in channel i is

u<sup>∗</sup><sub>i</sub> (t)

$$
= \max \left\{\frac {M k _ {i} (2 c _ {j} \varphi_ {i} (t) + k _ {j} ^ {2} \varphi_ {j} (t) (\varphi_ {i} (t) - \varphi_ {j} (t)))}{4 (c _ {i} + k _ {i} ^ {2} \varphi_ {i} (t)) (c _ {j} + k _ {j} ^ {2} \varphi_ {j} (t)) - k _ {i} ^ {2} k _ {j} ^ {2} (\varphi_ {i} (t) + \varphi_ {j} (t)) ^ {2}}, 0 \right\},\tag{10}
$$

where

$$
\varphi_ {i} (t) = \frac {p}{\delta_ {i} + r} (1 - e ^ {- (\delta_ {i} + r) (T - t)}).
$$

Proposition 1 suggests that the optimal advertising effort $u _ { i } ^ { * } ( t )$ depends on the marginal values of goodwill $\varphi _ { i } ( t )$ and $\varphi _ { j } ( t )$ . For channel $i ,$ its optimal advertising effort is strictly positive when

$$
\frac {\varphi_ {j} (t)}{\varphi_ {i} (t)} (\varphi_ {j} (t) - \varphi_ {i} (t)) <   \frac {2 c _ {j}}{k _ {j} ^ {2}}, \quad \forall t <   T.\tag{11}
$$

Here, the term $\varphi _ { j } / \varphi _ { i } ( \varphi _ { j } - \varphi _ { i } )$ reflects the comparative advantage of channel j in the marginal value of goodwill compared with channel i (for simplicity, referred to as the comparative advantage of channel j thereafter), whereas the term $2 c _ { j } / k _ { j } ^ { 2 }$ measures the amount of cost required to produce one unit of incremental goodwill in channel j, which is referred to as the cost inefficiency of channel j in the remaining discussion. Inequality (11) states that the firm should invest in channel i only when the comparative advantage of the other channel j cannot compensate for its cost inefficiency. This strategy allows the firm to combine and leverage the advantages offered by both channels, for the purpose of maximizing its total profit.

To better understand the properties of the optimal advertising policy, we further compare the marginal values of goodwill in digital and traditional ad channels and reach a number of conclusions.

Proposition 2. The marginal value of goodwill in the digital channel is always larger than that in the traditional channel, that is, $\varphi _ { 1 } ( t ) \geq \varphi _ { 2 } ( t )$ , where the equality holds only at $t = T$

Proposition 3. The comparative advantage of the digital channel in the marginal value of goodwill compared with the traditional channel, $\begin{array} { r } { h ( t ) = \frac { \varphi _ { 1 } ( t ) } { \varphi _ { 2 } ( t ) } ( \varphi _ { 1 } ( t ) - \varphi _ { 2 } ( t ) ) } \end{array}$ , always decreases with time.

Because $\varphi _ { 1 } ( t ) \geq \varphi _ { 2 } ( t )$ , Inequality (11) related to $u _ { 1 } ^ { * } ( t )$ $( \mathrm { i } . \mathrm { e } . , i = 1$ and $j = 2 )$ is always satisfied, which ensures that $u _ { 1 } ^ { * } ( t ) > 0$ for $t < T$ and $u _ { 1 } ^ { * } ( T ) = 0$ . We summarize this result in Corollary 1.

Corollary 1. The optimal advertising effort in the digital ad channel is always strictly positive for $t < T$ and only reaches zero at $t = \dot { T }$

For the traditional channel, the positivity of its optimal advertising effort depends on the tradeoff between the comparative advantage of the digital channel (denoted by h(t)) and its cost inefficiency (expressed as $2 c _ { 1 } / k _ { 1 } ^ { 2 } )$ Proposition 3 reveals that, although the marginal value of goodwill in the digital channel is greater than that in the traditional channel, its comparative advantage diminishes over time. This is because the difference between the retention of goodwill in the two channels progressively decreases as the remaining duration in the planning horizon shortens. For traditional advertising, it should remain at zero until the comparative advantage of the digital channel becomes insufficient to offset its cost inefficiency in later stages. Essentially, it suggests a zero-positive pattern for the optimal advertising effort in the traditional channel. When the cost inefficiency of the digital channel is particularly high (i.e., $2 c _ { 1 } / k _ { 1 } ^ { 2 } > h ( 0 ) )$ the optimal advertising effort in the traditional channel remains positive throughout the planning horizon and only reaches zero at the end of the horizon. We formally present this result in Corollary 2.

Corollary 2. When $2 c _ { 1 } / k _ { 1 } ^ { 2 } > h ( 0 )$ , the optimal advertising effort in the traditional ad channel $u _ { 2 } ^ { * } ( t )$ is always strictly positive for $t < T$ and only reaches zero at $t = T$ . Conversely, when $2 \dot { c } _ { 1 } / k _ { 1 } ^ { 2 } \le h ( 0 )$ , it follows a zero-positive pattern:

$$
u _ {2} ^ {*} (t) \left\{ \begin{array}{l l} = 0, & t \in [ 0, t _ {a} ] \cup \{T \}, \\ > 0, & t \in (t _ {a}, T), \end{array} \right.
$$

where $t _ { a }$ represents the unique solution of ${ \bf \ddot { \boldsymbol { h } } } ( t ) = 2 c _ { 1 } / k _ { 1 } ^ { 2 }$

Furthermore, we analyze the rates of change in optimal advertising efforts across the two channels in Corollary 3. Because of the diminishing comparative advantage of digital advertising, the firm should initially invest in the digital channel at the maximum level and then gradually reduce it over time. Therefore, the optimal trajectory of digital advertising shows a decreasing trend throughout the planning horizon. Regarding the rate of change in traditional advertising, analytical results are almost unat tainable due to the complexity of $\alpha ( t )$ . We thus conduct multiple numerical simulations. As shown in Figures 1 and ${ \hat { 2 } } ,$ the optimal trajectory of traditional advertising typically follows a “zero-increasing-decreasing” or “increasing-decreasing” pattern. Namely, when the firm begins adopting traditional advertising, it should gradu ally increase the investment as the comparative advantage of digital advertising diminishes. Toward the end of the planning horizon, investment in traditional adver tising is tapered given the zero salvage value at the terminal time. In an extreme scenario where the cost inefficiency of digital advertising is especially severe (i.e., $2 c _ { 1 } / \dot { k _ { 1 } ^ { 2 } } \geq \alpha ( t ) _ { m a x } )$ , the traditional channel holds strategic importance equal to that of the digital channel. Under this condition, the firm cannot maximize its profit by delaying the deployment of traditional advertising or gradually increasing investment in the traditional channel. Instead, the firm should immediately hike the investment in traditional advertising to the maximum level at the outset of the campaign, and subsequently reduce it over time. As a result, the optimal trajectory of traditional advertising exhibits a monotonic decrease in the entire process.

Figure 1. (Color online) Optimal Trajectories of Digital and Traditional Advertising Efforts When $2 c _ { 1 } / k _ { 1 } ^ { 2 } < \alpha ( t ) _ { m a x }$  
![](/api/attachments/ZV22Z4YT/fulltext/images/692db1939e4af428b42ef5407868b027f33a6e6a6f3760256830734cf7eec404.jpg)  
Notes. p � 1, k � 0.47, c � 0.43, c � 1, δ � 0.38, δ � 0.6, r � 0.1, M � 1, T � 2. (i) k � 2.5; (ii) k � 1.

![](/api/attachments/ZV22Z4YT/fulltext/images/dadbe898f18687120af759f50edb30929029d8decddb51551a948bdf6bd03f29.jpg)

Figure 2. (Color online) Optimal Trajectories of Digital and Traditional Advertising Efforts When $2 c _ { 1 } / k _ { 1 } ^ { 2 } \ge \alpha ( t ) _ { m a x }$  
![](/api/attachments/ZV22Z4YT/fulltext/images/7a4dc15ef43c20240468bb3573cec817afbbd356b7ff89d51c3ea3ae258298f0.jpg)  
Note. $p = 1 , k _ { 1 } = 0 . 3 , k _ { 2 } = 0 . 4 7 , c _ { 1 } = 0 . 4 3 , c _ { 2 } = 1 , \delta _ { 1 } = 0 . 3 8 , \delta _ { 2 } = 0 . 6 , r = 1 \quad \mathrm { ~ a ~ n ~ s ~ } \quad \forall \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm { ~ d ~ } \mathrm  ~ d$ 0.1, M � 1, T � 2.

Corollary 3. The optimal digital advertising effort always decreases with time throughout the planning horizon. When the optimal traditional advertising effort is strictly positive, it monotonically increases with time when $\alpha ( t ) > 2 c _ { 1 } / k _ { 1 } ^ { 2 }$ and decreases with time otherwise. (The expression for α(t) is provided in the Online Appendix.)

It is worth noting that, even if the digital channel is completely superior to the traditional channel in terms of both marginal value of goodwill and cost inefficiency, the firm should still invest in traditional advertising during the later stages of the planning horizon, given that the comparative advantage of the digital ad channel diminishes over time. In other words, it is optimal for the firm to deploy digital and traditional advertising in a sequential manner. In fact, many firms have already adopted the strategy of initially leveraging low-cost, effective digital advertising to penetrate the market, followed by investments in traditional advertising to further expand the market share. For instance, Airbnb initially implemented a strong digital marketing strategy, focusing on search engine optimization, paid search ads, and content marketing to build its short-term rental marketplace. However, as Airbnb expanded into new markets and targeted broader demographics such as seniors and families, it started using traditional advertising including television commercials and subway ads (Mock The Agency 2023). The sequential use of digital and traditional advertising has effectively enabled Airbnb to broaden its market reach and attract diverse traveler segments, contributing to a significant increase in its net income to \$4.8 billion in 2023.<sup>2</sup>

In order to make informed decisions on the dynamic multichannel advertising strategy, it is crucial for the firm to optimally allocate advertising efforts across different channels, that ${ \mathrm { i s } } ,$ the ratio of the optimal advertising efforts in different channels, defined as $\Omega ( t ) : = u _ { 1 } ^ { * } ( t ) / u _ { 2 } ^ { * } ( t )$ in our model. Although previous studies have engaged in some discussions, they typically either analyze based on a static framework (Gatignon and Hanssens 1987, Gopalak rishna and Chatterjee 1992) or focus on the optimal longrun stationary equilibrium in a dynamic framework (Naik and Raman 2003, Raman and Naik 2004). Thus, the ratio of the optimal advertising efforts across different channels remains a time-invariant constant in these studies, which cannot provide managerial insights into its dynamic change during a firm’s entire planning horizon. We analyze the property of Ω(t) and summarize the result in the following proposition:

Proposition 4. When the optimal advertising efforts in the two channels are both positive, their ratio

$$
\Omega (t) := \frac {u _ {1} ^ {*} (t)}{u _ {2} ^ {*} (t)} = \frac {k _ {1} \left(2 c _ {2} \varphi_ {1} (t) + k _ {2} ^ {2} \varphi_ {2} (t) \left(\varphi_ {1} (t) - \varphi_ {2} (t)\right)\right)}{k _ {2} \left(2 c _ {1} \varphi_ {2} (t) + k _ {1} ^ {2} \varphi_ {1} (t) \left(\varphi_ {2} (t) - \varphi_ {1} (t)\right)\right)}
$$

monotonically decreases with time.

Proposition 4 indicates that when it is optimal for the firm to invest in both digital and traditional advertising, the firm should gradually shift its advertising effort from the digital channel to the traditional channel over time. Therefore, as the comparative advantage of the digital channel decreases, the optimal traditional advertising effort not only displays a zero-positive pattern, but its magnitude relative to the optimal digital advertising effort should increase over time.

## 5. Sensitivity Analysis

In the previous section, we discussed the firm’s optimal advertising policies for digital and traditional ad channels. In this section, we conduct sensitivity analyses to examine the impact of varying parameter values on the firm’s optimal advertising efforts in the two channels.

## 5.1. Analytical Sensitivity Analysis

We first analytically derive the sensitivity of the optimal advertising efforts in each channel with respect to some key model parameters, as summarized in the following proposition.

Proposition 5. When $u _ { i } ^ { * } ( t ) , i \in \{ 1 , 2 \}$ , is positive, it has the following properties:

1. The optimal advertising effort u<sup>∗</sup>(t) monotonically increases with M and $\delta _ { j } ,$ , and monotonically decreases with $c _ { i }$ and $\delta _ { i }$ .

2. The optimal advertising effort $\boldsymbol { u } _ { i } ^ { * } ( t )$ monotonically increases with $k _ { i }$ when $\begin{array} { r } { \dot { \Theta _ { i } ( t ) } < \frac { 2 c _ { i } } { k _ { i } ^ { 2 } } , } \end{array}$ , where $\Theta _ { i } ( t ) =$ $\frac { 4 c _ { j } \varphi _ { i } ( t ) - k _ { j } ^ { 2 } ( \varphi _ { i } ( t ) - \varphi _ { j } ( t ) ) ^ { 2 } } { 2 ( c _ { j } + k _ { j } ^ { 2 } \varphi _ { j } ( t ) ) }$ . Conversely, it monotonically decreases with $\begin{array} { r } { k _ { i } w h e n \Theta _ { i } ( t ) > \frac { 2 c _ { i } } { k _ { i } ^ { 2 } } . } \end{array}$

3. The optimal digital advertising effort $u _ { i } ^ { * } ( t )$ monotonically decreases with $k _ { 2 }$ and increases with $c _ { 2 }$ when $\begin{array} { r } { h ( t ) < \frac { 2 c _ { 1 } } { k _ { * } ^ { 2 } } . } \end{array}$ Conversely, it monotonically increases with $k _ { 2 }$ <sup>1</sup>and decreases with $c _ { 2 }$ when $\begin{array} { r } { h ( t ) > \frac { 2 c _ { 1 } } { k _ { \ast } ^ { 2 } } } \end{array}$

4. The optimal traditional advertising effort $u _ { 2 } ^ { * } ( t )$ monotonically decreases with $k _ { 1 }$ and increases with $c _ { 1 }$ .

For each channel $i ,$ where $i = 1 \mathrm { o r } 2 ,$ the optimal advertising effort monotonically increases with the initia level of consumers’ perceived information usefulness M and decreases with its advertising cost $c _ { i } \ ( \mathrm { i . e . }$ , Proposition 5(1)). The explanation is that, as M increases, the potential incremental goodwill that can be generated by advertising also increases, which amplifies the margina return of advertising effort in each channel. Moreover, an increase in the decay rate in one channel leads to more goodwill being forgotten by consumers within the planning horizon. Thus, this channel becomes less preferred by the firm. Mathematically, the optimal advertising effort in channel i monotonically decreases with $\delta _ { i }$ and increases with $\delta _ { j }$ (i.e., Proposition 5(1)). Regarding the impact of advertising effectiveness $k _ { i } ,$ the sensitivity analysis becomes more complex. On the one hand, a higher advertising effectiveness signifies that a unit of advertising effort can produce more units of incremental goodwill. On the other hand, it implies a faster rate in satisfying consumers’ informational needs, thus diminishing the perceived information usefulness of its own advertising at future times. According to Proposition 5(2), when the cost inefficiency of channel i is high (i.e., smaller $k _ { i }$ or larger c ), the firm should increase its advertising effort in channel i as $k _ { i }$ increases. However, when the cost inefficiency of channel i is low (i.e., larger $k _ { i }$ or smaller c ), contrary to what one might expect, increasing advertising effort with a larger $k _ { i }$ would be counterproductive. This result mainly stems from the diminishing marginal return of advertising in each channel. As previously discussed, when the advertising effort in channel is held constant, the marginal return of advertising in channel i monotonically decreases as its own advertising effort increases. Therefore, when the cost inefficiency of channel i is sufficiently low, the optimal advertising effort $u _ { i } ^ { * } ( t )$ becomes sufficiently large, as indicated in Equation (10). Under this condition, further increasing $u _ { i } ^ { * } ( t )$ as its advertising becomes more effective will lead to significantly low marginal returns that cannot compensate for the cost of advertising. To avoid the counterproductive effect of excessive advertising, the firm should optimally decrease $u _ { i } ^ { * } ( t )$ with $k _ { i }$ .

In addition, the optimal advertising effort in one channel is also influenced by the advertising effectiveness and cost in the other channel $( \mathrm { i . e . , } k _ { j }$ and $c _ { j } )$ . For digital advertising, when its comparative advantage cannot offset its cost inefficiency $( \mathrm { i . e . , \ } h ( t ) < 2 c _ { 1 } / k _ { 1 } ^ { 2 } ) .$ , the firm should allocate some advertising effort to the traditional ad channel in order to maximize its total profit. Under this condition, if the traditional ad channel exhibits greater effectiveness or lower cost, the allocated advertising effort will be greater. Conversely, when the comparative advantage of digital advertising can compensate for its cost inefficiency $( \mathrm { i . e . , ~ } h ( t ) > 2 c _ { 1 } / k _ { 1 } ^ { 2 } )$ , it implies that digital advertising outperforms traditional advertising in all aspects. In this situation, it is optimal for the digital ad channel to take all the firm’s advertising effort. It is important to note that although the firm has not yet adopted the traditional ad channel at this time, it will definitely engage in traditional advertising in later stages, given that the comparative advantage of the digital ad channel diminishes over time. If the cost inefficiency of the traditional ad channel is low $( \mathrm { i . e . , }$ larger $k _ { 2 }$ or smaller $c _ { 2 } )$ , the firm needs to allocate more advertising effort to the traditional ad channel in later stages. To ensure that the digital ad channel can stil generate sufficient profits, the firm should accordingly increase the digital advertising effort in earlier stages (when $u _ { 2 } ^ { * } ( t ) = 0 )$ . As a result, the optimal digital advertising effort increases with $k _ { 2 }$ and decreases with $c _ { 2 } ~ ( \mathrm { i . e . } ,$ Proposition 5(3)).

Regarding traditional advertising, recall that the firm would invest in it only when $h ( t ) \stackrel { \smile } { < } 2 c _ { 1 } / k _ { 1 } ^ { 2 }$ . If the effectiveness of digital advertising is smaller or its cost is larger, its cost inefficiency becomes higher, leading to a greater amount of advertising effort allocated to the traditional ad channel. Thus, the optimal traditional advertising effort monotonically decreases with the effectiveness of digital advertising and increases with the unit cost of digital advertising (i.e., Proposition 5(4)).

Because the cost inefficiencies of the two channels critically determine the optimal advertising paths, we further illustrate in Figures $3 ^ { \bar { - } } { 5 }$ how the optimal advertising policy changes in accordance with the cost inefficiencies of the digital and traditional channels $\mathrm { ( i . e . , ~ } 2 c _ { 1 } / k _ { 1 } ^ { 2 }$ and

Figure 3. Patterns of Optimal Advertising Efforts When $\varphi _ { 1 } ( t ) / \varphi _ { 2 } ( t ) < 3$  
![](/api/attachments/ZV22Z4YT/fulltext/images/00e6e486f2de69810b59e6baabf5834a0ed8df6ea8f6c84ae57af5b21aedeae2.jpg)

Figure 4. Patterns of Optimal Advertising Efforts When $3 < \varphi _ { 1 } ( t ) / \varphi _ { 2 } ( t ) < 3 + 2 \sqrt { 2 }$  
![](/api/attachments/ZV22Z4YT/fulltext/images/74916d48fd3ec91a5859586d85e2df424bc455084528bf04eafd61f2ff9c650a.jpg)  
Cost Inefficiency in Digital Channel (2c1/k2)

$2 c _ { 2 } / k _ { 2 } ^ { 2 } )$ . The scenarios depicted in the three figures differ in the ratio of marginal values of goodwill associated with the two channels. Additionally, all three figures include multiple regions, with detailed characteristics summarized in Table 1. When $\varphi _ { 1 } ( t )$ is sufficiently larger than $\varphi _ { 2 } ( t )$ (more specifically, $\varphi _ { 1 } ( t ) / \varphi _ { 2 } ( t ) > 3 )$ as shown in Figures 4 and 5, the cost inefficiency in the digital ad channel cannot simultaneously satisfy $2 c _ { 1 } / k _ { 1 } ^ { 2 } < \Theta _ { 1 } ( t )$ and $2 c _ { 1 } / k _ { 1 } ^ { 2 } > h ( t )$ . Thus, Region V does not occur.

## 5.2. Numerical Sensitivity Analysis

As shown in Proposition $5 ,$ the sensitivity of the optimal advertising efforts in the digital and traditional ad channels with respect to some key parameters $( k _ { 1 } , k _ { 2 } , c _ { 1 } ,$ , and $c _ { 2 } )$ varies over the planning horizon. Consequently, it is difficult to draw general conclusions regarding the sensitivity of the firm’s total advertising efforts with respect to these parameter values. We then conduct several numerical simulations to investigate how changes in $k _ { 1 } ,$ $k _ { 2 } , c _ { 1 }$ , and $c _ { 2 }$ influence the firm’s total advertising efforts and total profit. Each time we vary the value of one parameter while keeping other parameter values fixed. Table 2 lists the baseline values of parameters. We consider a firm that introduces its new product at the beginning of the planning horizon, thus the initial value of goodwill $G _ { 0 }$ is zero. The planning period T is two years.

Table 1. Characteristics of Different Patterns of Optimal Advertising Effort  
Figure 5. Patterns of Optimal Advertising Efforts When<sub>fifi√</sub> $\varphi _ { 1 } ( t ) / \varphi _ { 2 } ( t ) > 3 + 2 \sqrt { 2 }$  
![](/api/attachments/ZV22Z4YT/fulltext/images/b4662453f0f91c9f1fe8ed0023202e2938202b0d9d9586508afb5c8681baf19b.jpg)  
Cost Inefficiency in Digital Channel (2c1/k2

The discount rate r is set to 0.1 when time is measured in years (Peres and Van den Bulte 2014). The initial level of consumers’ perceived information usefulness M and the revenue rate $p$ are both set to one without loss of generality. We set the decay rates in two channels to $\delta _ { 1 }$ $= 0 . 3 8$ and $\delta _ { 2 } = 0 . 6 ,$ corresponding to the lower bound and upper bound, respectively, of estimates reported by Bass and Clarke $( 1 9 7 2 ) . ^ { 3 }$ Because digital advertising has been empirically validated to be more effective than traditional advertising (Summers et al. 2016), the coefficients of advertising effectiveness in the two channels are set to $k _ { 1 } = 0 . 8 1$ and $k _ { 2 } = 0 . 4 7 ,$ , which represent the upper bound and lower bound, respectively, of estimates reported by Naik et al. (2008). We also examined the case where the ad effectiveness in the traditional channel exceeds that in the digital channel, and the results were qualitatively similar. Regarding the unit cost of advertising in the two channels, marketing statistics (Mandese 2022) show that the average CPM for traditional media was around \$16.14 in 2022, ranging from \$2 to \$54 depending on the specific medium (e.g., television, radio, print, and out-of-home ads). In contrast, CPMs for social media ads across different online platforms $( \mathrm { e . g . }$ , Facebook, Twitter, Instagram, and LinkedIn) varied from \$5.76 to \$9.06, with an average of \$6.89 (Chawlani 2024). This indicates that the unit cost of digital advertising is approximately 43% of that of traditional advertising on average. Thus, in our numerical study, we normalize the unit cost of traditional advertising $c _ { 2 }$ to one and set the unit cost of digital advertising $c _ { 1 }$ to 0.43. For practical relevance, the full ranges of key parameters are limited to $0 . 2 \leq k _ { 1 } \leq 5 , 0 . 2 \leq k _ { 2 } \leq \bar { 5 } ,$ $0 . 2 \leq c _ { 1 } \leq 2$ , and $0 . 2 \leq c _ { 2 } \leq 2 ,$ , which are close to the estimates reported in the previously mentioned studies.

<table><tr><td></td><td> $du_{1}^{*}(t)/dk_{1}$ </td><td> $du_{1}^{*}(t)/dk_{2}$ </td><td> $du_{1}^{*}(t)/dc_{1}$ </td><td> $du_{1}^{*}(t)/dc_{2}$ </td><td> $du_{2}^{*}(t)/dk_{1}$ </td><td> $du_{2}^{*}(t)/dk_{2}$ </td><td> $du_{2}^{*}(t)/dc_{1}$ </td><td> $du_{2}^{*}(t)/dc_{2}$ </td><td>Optimal policy</td></tr><tr><td>Region I</td><td>-</td><td>+</td><td>-</td><td>-</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>Only digital ads</td></tr><tr><td>Region II</td><td>+</td><td>+</td><td>-</td><td>-</td><td>N/A</td><td>N/A</td><td>N/A</td><td>N/A</td><td>Only digital ads</td></tr><tr><td>Region III</td><td>+</td><td>-</td><td>-</td><td>+</td><td>-</td><td>-</td><td>+</td><td>-</td><td>Digital and traditional ads</td></tr><tr><td>Region IV</td><td>+</td><td>-</td><td>-</td><td>+</td><td>-</td><td>+</td><td>+</td><td>-</td><td>Digital and traditional ads</td></tr><tr><td>Region V</td><td>-</td><td>-</td><td>-</td><td>+</td><td>-</td><td>+</td><td>+</td><td>-</td><td>Digital and traditional ads</td></tr></table>

Table 2. Baseline Parameter Values

<table><tr><td>Parameter</td><td>Baseline value</td></tr><tr><td>Revenue rate (p)</td><td>1</td></tr><tr><td>Discount rate (r)</td><td>0.1</td></tr><tr><td>Initial value of goodwill ( $G_0$ )</td><td>0</td></tr><tr><td>Length of the planning horizon (T)</td><td>2</td></tr><tr><td>Digital ad effectiveness ( $k_1$ )</td><td>0.81</td></tr><tr><td>Traditional ad effectiveness ( $k_2$ )</td><td>0.47</td></tr><tr><td>Unit cost of digital advertising ( $c_1$ )</td><td>0.43</td></tr><tr><td>Unit cost of traditional advertising ( $c_2$ )</td><td>1</td></tr><tr><td>Decay rate in the digital ad channel ( $\delta_1$ )</td><td>0.38</td></tr><tr><td>Decay rate in the traditional ad channel ( $\delta_2$ )</td><td>0.6</td></tr><tr><td>Initial level of consumers&#x27; perceived information usefulness (M)</td><td>1</td></tr></table>

Figure 6 shows the impact of varying the advertising effectiveness. An increase in the advertising effectiveness in either the digital or traditional ad channel results in an increase in the total profit and a decrease in the total advertising effort in the other channel. However, it does not necessarily imply an increase in its own advertising effort. As one can see, when the cost inefficiency of the focal channel is high (i.e., lower advertising effectiveness), the total advertising effort in the focal channe monotonically increases with its advertising effectiveness. Conversely, when the cost inefficiency is low (i.e., higher advertising effectiveness), the total advertising effort in the focal channel monotonically decreases with its advertising effectiveness. This finding is largely consistent with Proposition 5(2). In addition, Figure 7 illustrates the result obtained when varying the advertising cost. When the advertising cost in channel i increases, there is an inevitable decline in the firm’s total profit. To mitigate this negative impact as much as possible, the firm would reduce its advertising effort in channel i and instead increase its advertising effort in channel j.

Figure 6. (Color online) Impact of Varying Advertising Effectiveness  
(i)  
![](/api/attachments/ZV22Z4YT/fulltext/images/44cc5e99ed3e2c50cac09b97a534eb569506e1d7373aa92f1f633c7da8cf16ee.jpg)

## 6. Model Extensions

In the preceding sections, we discussed the substitution effect between digital and traditional advertising efforts, which captures the competition between the two channels in fulfilling consumers’ informational needs. In this section, we analyze two extended models that consider the synergistic effect and three advertising channels, respectively.

## 6.1. Synergistic Effect

In the literature on multichannel dynamic advertising (Naik and Raman 2003, Prasad and Sethi 2009, Aravindakshan et al. 2015, Keller and Swaminathan 2019), it is well documented that the simultaneous deployment of different channels can enhance the combined effect of a firm’s advertising campaigns, yielding outcomes that surpass the additive effects of deploying each channel in isolation. In other words, in addition to the incremental goodwill generated by advertising in individual channels, the synergistic effect between different types of advertising can yield additional goodwill to a firm, thereby accelerating the dynamic evolution of its total goodwill. Following this stream of literature, we reformulate the expression for the stock of goodwill as follows:

$$
\begin{array}{l} G (t) = G _ {0} + \sum_ {i = 1} ^ {2} \int_ {0} ^ {t} g _ {i} \big (u _ {i} (\tau), u _ {j} (\tau) \big) S _ {i} (t - \tau) d \tau \\ \qquad + \int_ {0} ^ {t} \beta k _ {1} k _ {2} u _ {1} (\tau) u _ {2} (\tau) \xi (t - \tau) d \tau , \end{array}\tag{12}
$$

where $\beta \ge 0$ represents the intensity of synergistic effect and $\xi ( t )$ denotes the survival function of the lifetime of each unit of additional goodwill produced by the synergistic effect. Essentially, the term $\beta k _ { 1 } k _ { 2 } u _ { 1 } ( \tau ) u _ { 2 } ( \tau )$ ) reflects the acceleration in goodwill dynamics resulting from the synergistic effect at time $\tau ,$ where its decay is captured via the survival function $\xi ( t - \tau )$ . Taking the time derivative yields the following state equation:

![](/api/attachments/ZV22Z4YT/fulltext/images/481d2f5f13cac808b6ae61ad1dcfb1878c3379e6af36802043762fcfda07a992.jpg)

Figure 7. (Color online) Impact of Varying Advertising Cost  
![](/api/attachments/ZV22Z4YT/fulltext/images/1c6fff811d0945800b4f516f305ff9faa2cfb7e3cba6572931d5854bd8eb035b.jpg)

$$
\begin{array}{l} \dot {G} (t) = \sum_ {i = 1} ^ {2} \left(g _ {i} \big (u _ {i} (t), u _ {j} (t) \big) - \int_ {0} ^ {t} g _ {i} \big (u _ {i} (\tau), u _ {j} (\tau) \big) f _ {i} (t - \tau) d \tau\right) \\ \qquad + \beta k _ {1} k _ {2} u _ {1} (t) u _ {2} (t) - \int_ {0} ^ {t} \beta k _ {1} k _ {2} u _ {1} (\tau) u _ {2} (\tau) \eta (t - \tau) d \tau , \end{array}\tag{13}
$$

where $\eta ( t )$ is the density function associated with $\xi ( t ) ,$ that is, $\dot { \eta } ( t ) = - d \xi ( t ) / d t$ . We also assume that the lifetime of each unit of additional goodwill generated by the synergistic effect follows an exponential distribution:

$$
\xi (t) = e ^ {- \sigma t}, \eta (t) = \sigma e ^ {- \sigma t},\tag{14}
$$

where $\sigma$ is the decay rate. The extended model is then to maximize (5) subject to (3), (4), (13), and (14). The current-value Hamiltonian is formulated $\mathsf { a s } ^ { 4 }$

$$
\begin{array}{r l} & H = p G (t) - c _ {1} u _ {1} ^ {2} (t) - c _ {2} u _ {2} ^ {2} (t) + \beta k _ {1} k _ {2} u _ {1} (t) u _ {2} (t) \psi (t) \\ & \qquad + k _ {1} u _ {1} (t) \varphi_ {1} (t) (M - k _ {1} u _ {1} (t) - k _ {2} u _ {2} (t)) \\ & \qquad + k _ {2} u _ {2} (t) \varphi_ {2} (t) (M - k _ {1} u _ {1} (t) - k _ {2} u _ {2} (t)), \end{array}\tag{15}
$$

where $\begin{array} { r } { \psi ( t ) : = \lambda ( t ) - \int _ { t } ^ { T } \lambda ( \tau ) \eta ( \tau - t ) d \tau , } \end{array}$ and λ(t) and $\varphi _ { i } ( t )$ are given in (7) and (8), respectively. Here, ψ(t) can be interpreted as the marginal value of additional goodwill generated by the synergistic effect, which should remain positive throughout the planning horizon. Because the extended optimization problem still involves two control variables, we also need to assume that the Hessian matrix is always negative definite to ensure the existence of an interior maximum.

![](/api/attachments/ZV22Z4YT/fulltext/images/5fb3ff77bf93c5e5cb76da792e6be693faa4197f226d9e38ed7a76bbc229d9ec.jpg)

Lemma 2. For the extended model with synergistic effect, an interior maximum exists only when the following condition holds for all $t \in [ 0 , T ]$ :

$$
\begin{array}{r l} & 4 (c _ {1} + k _ {1} ^ {2} \varphi_ {1} (t)) (c _ {2} + k _ {2} ^ {2} \varphi_ {2} (t)) \\ & - k _ {1} ^ {2} k _ {2} ^ {2} (\varphi_ {1} (t) + \varphi_ {2} (t) - \beta \psi (t)) ^ {2} > 0. \end{array}\tag{16}
$$

Similar to Lemma 1, Inequality (16) can be ensured with a large value of $c _ { 1 }$ or $c _ { 2 }$ . Based on our previous discussion in Lemma 1, it is plausible to assume that (16) holds as well. Given the existence of an interior maximum, the optimal advertising policy is provided in Proposition 6.

Proposition 6. For the extended model with synergistic effect, given the existence of an interior maximum, the optimal advertising effort in channel i is

$$
\begin{array}{l} u _ {i} ^ {*} (t) \\ = \max \left\{\frac {M k _ {i} (2 c _ {j} \varphi_ {i} (t) + k _ {j} ^ {2} \varphi_ {j} (t) (\varphi_ {i} (t) - \varphi_ {j} (t) + \beta \psi (t)))}{4 (c _ {i} + k _ {i} ^ {2} \varphi_ {i} (t)) (c _ {j} + k _ {j} ^ {2} \varphi_ {j} (t)) - k _ {i} ^ {2} k _ {j} ^ {2} (\varphi_ {i} (t) + \varphi_ {j} (t) - \beta \psi (t)) ^ {2}}, 0 \right\}, \end{array}
$$

where

$$
\begin{array}{l} \varphi_ {i} (t) = \frac {p}{\delta_ {i} + r} (1 - e ^ {- (\delta_ {i} + r) (T - t)}), \\ \psi (t) = \frac {p}{\sigma + r} (1 - e ^ {- (\sigma + r) (T - t)}. \end{array} .
$$

Proposition 6 reveals that the optimal advertising effort in channel i is strictly positive when

$$
\frac {\varphi_ {j} (t)}{\varphi_ {i} (t)} (\varphi_ {j} (t) - \varphi_ {i} (t) - \beta \psi (t)) <   \frac {2 c _ {j}}{k _ {j} ^ {2}}, \quad \forall t <   T.\tag{17}
$$

Compared with (11), (17) suggests that when deciding whether to invest in channel i, the firm should conside not only the comparative advantage of channel j in the marginal value of goodwill and its cost inefficiency, but also the impact of synergy. In particular, we observe that given ${ \hat { \beta } } > 0 , ( 1 7 )$ is more likely to hold than (11). This implies that in the presence of synergistic effect, the firm is more inclined to invest in both advertising channels simultaneously. Because of the comparative advantage of the digital channel in the marginal value of goodwill, the firm should still prioritize investments in digital advertising throughout the entire process, as stated in Corollary 4.

Corollary 4. In the presence of synergistic effect, the optimal digital advertising effort $u _ { 1 } ^ { * } ( t )$ is strictly positive for $t < T$ and only reaches zero at $t = T$

However, the zero-positive pattern of the optimal traditional advertising effort does not always hold in the presence of synergistic effect. Specifically, we find that when the intensity of synergistic effect is sufficiently large $( { \boldsymbol { \beta } } \geq { \hat { \boldsymbol { \beta } } } )$ , simultaneous investments in both advertising channels can effectively stimulate the firm’s goodwill dynamics, thereby improving the firm’s total profit. As a result, the firm is compelled to actively engage in traditional advertising campaigns throughout the entire planning horizon. Conversely, when the intensity of synergistic effect is sufficiently small $( { \boldsymbol { \beta } } \leq { \check { \boldsymbol { \beta } } } ) .$ , the acceleration of goodwill dynamics resulting from the concurrent use of both types of advertising is not expected to have a significant impact. Therefore, the firm should allocate resources to the traditional channel only when the comparative advantage of the digital channel substantially diminishes in the later stages. Under this condition, the optimal pattern of traditional advertising aligns with the conclusions drawn from the base model. We summarize the optimal pattern of traditional advertising in the presence of synergistic effect in Corollary 5.

Corollary 5. In the presence of synergistic effect, the optimal traditional advertising effort $u _ { 2 } ^ { * } ( t )$ possesses the following properties:

1. When the synergistic effect is sufficiently large $( i . e .$ $\beta \geq \hat { \beta } )$ , the optimal traditional advertising effort is strictly positive for $t < T$ and only reaches zero at $\bar { t } = T$

2. When the synergistic effect is sufficiently small $( i . e . ,$ $\beta \leq \check { \beta } )$ and the cost inefficiency of the digital channel is sufficiently high $( i . e . , ~ 2 c _ { 1 } / k _ { 1 } ^ { 2 } > \tilde { h } ( 0 ) )$ , the optimal traditional advertising effort is strictly positive for $t < T$ and only reaches zero at $t = T$ , where

$$
\tilde {h} (t) = \frac {\varphi_ {1} (t)}{\varphi_ {2} (t)} \big (\varphi_ {1} (t) - \varphi_ {2} (t) - \beta \psi (t) \big).
$$

3. When the synergistic effect is sufficiently small $( i . e .$ $\beta \leq \check { \beta } )$ and the cost inefficiency of the digital channel is not too $\mathit { h i g h } ( i . e . , 2 c _ { 1 } / k _ { 1 } ^ { \widetilde { 2 } } \leq \tilde { h } ( \widetilde { 0 } ) )$ , the optimal traditional advertising effort follows a zero-positive pattern:

$$
u _ {2} ^ {*} (t) \left\{ \begin{array}{l l} = 0, & t \in [ 0, t _ {b} ] \cup \{T \}, \\ > 0, & t \in (t _ {b}, T), \end{array} \right.
$$

where $t _ { b }$ represents the unique root for $\tilde { h } ( t ) = 2 c _ { 1 } / k _ { 1 } ^ { 2 }$ . (The expressions for β <sup>ˆ</sup> and $\check { \beta }$ are provided in the Online Appendix.)

When the intensity of synergistic effect is at a moderate level $( { \check { \beta } } < \beta < { \hat { \beta } } )$ , analytically investigating the opti mal pattern of traditional advertising is challenging. Therefore, we resort to numerical simulations. As shown in Table 3, we find that when $\beta$ is low, the opti mal pattern of traditional advertising still exhibits a zero-positive pattern. However, as $\beta$ increases, it is opti mal to adopt traditional advertising earlier; when $\bar { \boldsymbol { \beta } }$ is sufficiently large, the optimal traditional advertising effort will remain positive throughout the planning horizon. Furthermore, the amount of cumulative traditional advertising effort and its ratio to cumulative digi tal advertising effort also increase with $\beta ,$ indicating that the synergistic effect strengthens the importance of the traditional channel in the firm’s multichannel marketing strategies.

Proposition 7. In the presence of synergistic effect, when the optimal advertising efforts in the two channels are both positive, their ratio

$$
\tilde {\Omega} (t) = \frac {k _ {1} (2 c _ {2} \varphi_ {1} (t) + k _ {2} ^ {2} \varphi_ {2} (t) (\varphi_ {1} (t) - \varphi_ {2} (t) + \beta \psi (t)))}{k _ {2} (2 c _ {1} \varphi_ {2} (t) + k _ {1} ^ {2} \varphi_ {1} (t) (\varphi_ {2} (t) - \varphi_ {1} (t) + \beta \psi (t)))}
$$

monotonically decreases with time when $B ( t ) > \beta$ and increases with time when $B ( t ) < \beta$ . (The expression for $B ( t )$ is provided in the Online Appendix.)

The impact of the synergistic effect on the trajectory of the optimal allocation ratio $\tilde { \Omega } ( t )$ between digital and traditional advertising efforts is more complex. Recall that, in the absence of synergistic effect $( \mathrm { i . e . , } \beta = 0 )$ , the firm needs to allocate more investments to the traditiona channel over time, resulting in a decreasing trend in the optimal allocation ratio $( \mathrm { i . e . , }$ Proposition 4). In the presence of a synergistic effect, this conclusion remains valid only when the synergistic effect is weak $( \mathrm { i . e . , } B ( t ) > \beta )$ When the synergistic effect is strong $( \mathrm { i . e . , } B ( t ) < \beta )$ , the firm is better off increasing its investments in the traditional channel to benefit from the acceleration in the goodwill dynamics. Interestingly, as the traditional advertising effort increases, it also significantly boosts the marginal return of digital advertising (via the term $\beta k _ { 1 } k _ { 2 } u _ { 1 } u _ { 2 }$ in (12)), prompting further investments in the digital channel. Therefore, a strong synergistic effect creates a positive feedback loop between digital and traditional advertising, leading to an increasing trend in the optimal allocation ratio. As suggested by Proposition $^ { 7 , }$ the firm needs to dynamically evaluate the effectiveness of synergistic effect $( \mathrm { i . e . , }$ compare $B ( t )$ and $\beta$ at each instant) before determining the optimal trajectory of the allocation ratio between the two ad channels. Although it presents a challenging task, the closed-form expression for B(t) provided in the Online Appendix substantially alleviate the difficulty.

Proposition 8. In the presence of synergistic $e f f e c t ,$ , the optimal allocation ratio $\tilde { \Omega } ( t )$ monotonically increases with $\beta$ when $\gamma _ { 1 } ( t ) < \gamma _ { 2 } ( t )$ and decreases with $\beta$ otherwise, where $\begin{array} { r } { \gamma _ { i } ( t ) = \frac { k _ { i } ^ { 2 } \varphi _ { i } ^ { 2 } ( t ) } { c _ { i } + k _ { i } ^ { 2 } \varphi _ { i } ( t ) } . } \end{array}$

We further investigate the sensitivity of the optimal allocation ratio with respect to the intensity of synergistic effect. Proposition 8 reveals how the optimal allocation ratio between digital and traditional advertising efforts varies with $\beta .$ Here, $\gamma _ { i } ( t )$ can be interpreted as the advertising power of channel i (Sethi 2022, p. 376). This is because its numerator reflects the benefits brought by advertising effort in channel $i ,$ whereas its denominator measures the total (direct and indirect) cost of channel i. For channel $i ,$ its advertising effort not only incurs direct ad spending cost $( \mathbf { i . e . , \it { c } _ { i } ) }$ , but also brings the indirect information opportunity cost $( \mathrm { i . e . , } k _ { i } ^ { 2 } \varphi _ { i } ( t ) )$ by fulfilling consumers’ informational needs and thus diminishing their perceived information usefulness toward subsequent advertisements. This, in turn, reduces the marginal returns of advertising effort in channel $j .$ Fundamentally, Proposition 8 suggests that when the synergistic effect strengthens, the firm should allocate more budget to the channel with weaker advertising power. This finding appears counterintuitive but can be explained as follows. $\operatorname { A s } \beta$ increases, the increment in advertising effort in channel i depends not only on its own advertising effectiveness and cost, but also on the magnitude of advertising effort in the other channel j. According to the first-order conditions from the current-value Hamiltonian (15), we can obtain $d u _ { i } ^ { * } / d \beta \propto u _ { j } ^ { * } / ( c _ { i } + k _ { i } ^ { 2 } \varphi _ { i } )$ . If the advertising power of channel i is larger than that of channel $j ,$ the increment in the optimal advertising effort in channel i is less than that in channel $j$ as $\beta$ increases (i.e., $d u _ { i } ^ { * } / { d \beta } < d u _ { j } ^ { * } / { d \beta } )$ . Consequently, more advertising investments will be optimally allocated to channel j.

In fact, the favoring of weaker channels as the synergistic effect increases is one of the central features of multichannel marketing strategies (Naik and Raman 2003, Prasad and Sethi 2009). However, previous studies typically differentiate channels based solely on advertising effectiveness. Our study contributes to this stream of literature by emphasizing that, in the presence of substitution effect, synergistic effect, and differential goodwill decay rates across different channels, firms must simultaneously consider the advertising effectiveness, direct ad spending cost, indirect information opportunity cost, and different marginal values of goodwill in order to make informed decisions regarding the optimal budget allocation.

## 6.2. Three Advertising Channels

Our previous analysis focused on a single digital channel and a single traditional channel. In practice, firms typically have access to multiple digital or traditional channels, such as YouTube, Facebook, television, and magazines. Therefore, we next examine a three-channel dynamic advertising model, where a firm simultaneously manages a digital channel and two traditional channels.<sup>5</sup> While retaining the assumption that the decay rate of the digital channel is lower than that of either traditional channel, we also account for the differences in goodwill decay rates between the two traditional channels. Specifically, the three-channel dynamic advertising model is formulated as follows:

$$
\begin{array}{l} \max _ {u _ {1} (t), u _ {2} (t), u _ {3} (t)} \int_ {0} ^ {T} e ^ {- r t} \left(p G (t) - \sum_ {i = 1} ^ {3} c _ {i} u _ {i} ^ {2} (t)\right) d t, \\ s. t. \left\{ \begin{array}{l} \dot {G} (t) = \sum_ {i = 1} ^ {3} (g _ {i} (u _ {i} (t), u _ {j} (t), u _ {l} (t)) - \int_ {0} ^ {t} g _ {i} (u _ {i} (\tau), u _ {j} (\tau), u _ {l} (\tau)) f _ {i} (t - \tau) d \tau) \\ \qquad + \sum_ {i \neq j} (\beta_ {i j} k _ {i} k _ {j} u _ {i} (t) u _ {j} (t) - \int_ {0} ^ {t} \beta_ {i j} k _ {i} k _ {j} u _ {i} (\tau) u _ {j} (\tau) \eta_ {i j} (t - \tau) d \tau), \\ g _ {i} (u _ {i} (t), u _ {j} (t), u _ {l} (t)) = k _ {i} u _ {i} (t) (M - k _ {i} u _ {i} (t) - k _ {j} u _ {j} (t) - k _ {l} u _ {l} (t)), \\ f _ {i} (t) = \delta_ {i} e ^ {- \delta_ {i} t}, \qquad \eta_ {i j} (t) = \sigma_ {i j} e ^ {- \sigma_ {i j} t}, \\ G (0) = G _ {0}, \qquad u _ {i j} \geq 0, \end{array} \right. \end{array}
$$

where $\beta _ { i j }$ denotes the intensity of synergistic effect between ${ \bf \ddot { \boldsymbol { u } } } _ { i } ( t )$ and $u _ { j } ( t ) , \eta _ { i j } ( t )$ represents the density function of the lifetime of the additional goodwill generated by the synergistic effect between $u _ { i } ( t )$ and $u _ { j } ( t ) _ { \ j }$ , and $\sigma _ { i j }$ is the decay rate associated with $\eta _ { i j } ( t )$ . Without loss of generality, we assume $\delta _ { 1 } < \delta _ { 2 } < \delta _ { 3 } ^ { ^ { \prime } }$ . The optimal advertising policy is summarized in Proposition ${ \bf { \bar { 9 . } } } ^ { 6 }$

Table 3. Impact of the Synergistic Effect on the Optimal Traditional Advertising Effort

<table><tr><td>β</td><td>Optimal timing to adopt traditional advertising</td><td>Cumulative traditional advertising effort</td><td>Ratio of cumulative traditional ads to cumulative digital ads</td></tr><tr><td>0.01</td><td>0.1148</td><td>0.0208</td><td>0.0513</td></tr><tr><td>0.02</td><td>0.0288</td><td>0.0222</td><td>0.0547</td></tr><tr><td>0.03</td><td>0</td><td>0.0237</td><td>0.0584</td></tr></table>

Note. p � 1, M � 1, T � 2, k � 2, k � 0.47, c � 0.43, c � 1, r � 1, δ � 0.38, δ � 0.6, σ � 0.4.

Proposition 9. Given the existence of an interior maximum, the optimal advertising efforts in the three channels, respectively, are

$$
\begin{array}{l} u _ {1} ^ {*} = \max \left\{ \begin{array}{c} M (k _ {1} \varphi_ {1} (B _ {2} B _ {3} - A _ {2 3} ^ {2}) + k _ {2} \varphi_ {2} (A _ {1 3} A _ {2 3} - A _ {1 2} B _ {3}) \\ + k _ {3} \varphi_ {3} (A _ {1 2} A _ {2 3} - A _ {1 3} B _ {2})) \\ \hline 2 A _ {1 2} A _ {1 3} A _ {2 3} + B _ {1} B _ {2} B _ {3} - A _ {1 2} ^ {2} B _ {3} - A _ {1 3} ^ {2} B _ {2} - A _ {2 3} ^ {2} B _ {1}, 0 \end{array} \right\}, \\ u _ {2} ^ {*} = \max \left\{ \begin{array}{c} M (k _ {1} \varphi_ {1} (A _ {1 3} A _ {2 3} - A _ {1 2} B _ {3}) + k _ {2} \varphi_ {2} (B _ {1} B _ {3} - A _ {1 3} ^ {2}) \\ + k _ {3} \varphi_ {3} (A _ {1 2} A _ {1 3} - A _ {2 3} B _ {1})) \\ \hline 2 A _ {1 2} A _ {1 3} A _ {2 3} + B _ {1} B _ {2} B _ {3} - A _ {1 2} ^ {2} B _ {3} - A _ {1 3} ^ {2} B _ {2} - A _ {2 3} ^ {2} B _ {1}, 0 \end{*}, \\ u _ {3} ^ {*} = \max \left\{ \begin{array}{c} M (k _ {1} \varphi_ {1} (A _ {1 2} A _ {2 3} - A _ {1 3} B _ {2}) + k _ {2} \varphi_ {2} (A _ {1 2} A _ {1 3} - A _ {2 3} B _ {1}) \\ + k _ {3} \varphi_ {3} (B _ {1} B _ {2} - A _ {1 2} ^ {2})) \\ \hline 2 A _ {1 2} A _ {1 3} A _ {2 3} + B _ {1} B _ {2} B _ {3} - A _ {1 2} ^ {2} B _ {3} - A _ {1 3} ^ {2} B _ {2} - A _ {2 3} ^ {2} B _ {1}, 0 \\ \end{array} \right\}, \end{array}
$$

where $A _ { i j } = k _ { i } k _ { j } ( \varphi _ { i } + \varphi _ { j } - \beta _ { i j } \psi _ { i j } ) , B _ { i } = 2 ( c _ { i } + k _ { i } ^ { 2 } \varphi _ { i } ) , \varphi _ { i } =$ $\begin{array} { r } { \frac { p } { \delta _ { i } + r } ( 1 - e ^ { - ( \delta _ { i } + r ) ( T - t ) } ) } \end{array}$ , and $\begin{array} { r } { \psi _ { i j } = \frac { p } { \sigma _ { i j } + r } ( 1 - e ^ { - ( \sigma _ { i j } + r ) ( T - t ) } ) } \end{array}$

Because of the complexity of the interactions among the three channels, it becomes challenging to analytically determine the optimal pattern of advertising effort in each channel. Therefore, we conduct a series of numerical simulations and illustrate the trajectories of optimal advertising efforts across three channels in Figure 8. The results indicate that, when the synergistic effect is sufficiently weak, the firm should prioritize investment in the digital channel with the lowest decay rate, whereas deferring investment in the two traditional channels until the comparative advantage of the digital channel diminishes to a critical threshold in later stages. However, as the synergistic effect intensifies, the firm should adopt traditional advertising earlier; with a sufficiently large synergistic effect, the optimal investments in both traditional channels will remain positive throughout the planning horizon. These findings align well with the conclusions derived from the base model.

The impact of the synergistic effect on the optimal advertising allocation across three channels is presented in Table 4. We observe that as the synergistic effect between any two focal channels strengthens, the firm should increase its overall investment in these focal channels while decreasing its advertising expenditure in the third, nonfocal channel. Additionally, the optimal allocation of advertising investment between the two focal channels continues to follow the pattern established in Proposition 8. Specifically, although the majority of the investment is initially directed toward the stronger channel with greater advertising power, the firm should progressively reallocate resources from the stronger channel to the weaker channel as the synergistic effect intensifies. Our analysis of the three-channel dynamic advertising model effectively demonstrates the robustness of our analytical results and managerial implications.

## 7. Concluding Remarks

In this study, we apply optimal control theory to address the multichannel advertising optimization problem for a monopolistic firm that manages both digital and traditional ad channels. To the best of our knowl edge, we are the first to propose an analytical model that examines substitution and synergistic effects between advertising efforts in multiple channels and their different decay rates in the goodwill. In solving this dynamic optimization problem, we obtain a closed form solution for the firm’s optimal advertising policy and analyze how the optimal advertising efforts in the two channels evolve over time. Furthermore, we analytically and numerically investigate the optimal trajectories of the firm’s advertising efforts and the sensitivity of the optimal advertising policy with respect to key model parameters and derive some noteworthy findings.

Figure 8. (Color online) Optimal Advertising Trajectories in the Three-Channel Model  
![](/api/attachments/ZV22Z4YT/fulltext/images/85b5ecc442ef14c63e7bb6f182c4faa2897b5f0ba5991ada21827093bb87c1c0.jpg)

![](/api/attachments/ZV22Z4YT/fulltext/images/d70a7a2fc9277a9a210ce52b827fc3296ec8f88f445810b1affbee63a7f10377.jpg)  
Note. p � 1, M � 1, T � 2, r � 0.1, k � 0.8, k � 0.6, k � 0.4, c � 0.1, c � 1.2, c � 0.8, δ � 0.1, δ � 0.5, δ � 0.8, σ � σ � σ � 0.4.

Table 4. Impact of the Synergistic Effect on Advertising Allocation in the Three-Channel Model

<table><tr><td> $\beta_{12}$ </td><td> $\beta_{13}$ </td><td> $\beta_{23}$ </td><td>Cumulative ad effort in Channel 1 (% of total)</td><td>Cumulative ad effort in Channel 2 (% of total)</td><td>Cumulative ad effort in Channel 3 (% of total)</td></tr><tr><td>0.2</td><td>0.2</td><td>0.2</td><td>93.99%</td><td>3.83%</td><td>2.18%</td></tr><tr><td>0.6</td><td>0.2</td><td>0.2</td><td>89.28%</td><td>8.82%</td><td>1.90%</td></tr><tr><td>1.0</td><td>0.2</td><td>0.2</td><td>85.43%</td><td>12.99%</td><td>1.58%</td></tr><tr><td>0.2</td><td>0.6</td><td>0.2</td><td>89.93%</td><td>3.47%</td><td>6.60%</td></tr><tr><td>0.2</td><td>1.0</td><td>0.2</td><td>85.80%</td><td>2.91%</td><td>11.29%</td></tr><tr><td>0.2</td><td>0.2</td><td>0.6</td><td>93.89%</td><td>3.83%</td><td>2.28%</td></tr><tr><td>0.2</td><td>0.2</td><td>1.0</td><td>93.77%</td><td>3.84%</td><td>2.39%</td></tr></table>

Note. p � 1, M � 1, T � 2, r � 0.1, k<sub>1</sub> � 0.8, k<sub>2</sub> � 0.6, k<sub>3</sub> � 0.4, c<sub>1</sub> � 0.1, c<sub>2</sub> � 1.2, c<sub>3</sub> � 0.8, δ<sub>1</sub> � 0.1, δ<sub>2</sub> � 0.5, δ<sub>3</sub> � 0.8, σ<sub>12</sub> � σ<sub>13</sub> � σ<sub>23</sub> � 0.4, γ<sub>1</sub> > γ<sub>2</sub> > γ<sub>3</sub>.

Our work makes several important contributions to dynamic advertising research in the multichannel setting. First, prior studies typically focus on the additive effect (Abedi et al. 2022, Danaher 2023, Zhu et al. 2024) and synergistic effect (Naik and Raman 2003, Prasad and Sethi 2009, Aravindakshan et al. 2015) of different advertising efforts across multiple channels on a firm’s goodwill or product sales. Expanding this stream of literature, our research emphasizes that the substitution effect also plays a critical role in formulating a firm’s optimal advertising policy. Prior studies usually show that a firm should try to make investments in all available advertising channels due to the presence of synergistic effect (Naik and Raman 2003). However, our study highlights that this conclusion does not necessarily hold when the substitution effect is considered. In particular, our analysis reveals that, in determining whether to invest in a certain channel, a firm should dynamically evaluate the comparative advantage of its competing channel in the marginal value of goodwill against the cost inefficiency. Therefore, by extending dynamic multichannel advertising models to the scenario involving the substitution effect, this study derives more insightful findings about multichannel advertising investments.

Second, we contribute to the stream of literature that considers different decay rates in multiple ad channels. In prior studies, to capture the different nature of decay rates in multiple channels, the dynamics of a firm’s goodwill is typically represented as the sum of the dynamics of channel-specific goodwill (Naik and Raman 2003, Abedi et al. 2022, Zhu et al. 2024). Our study proposes an alternative approach to model different decay rates in multiple channels by letting the lifetime of incremental goodwill produced in each channel follow a different distribution. Consequently, the retention of goodwill in each channel can be characterized by a unique survival function. Our approach ensures that the system dynamics can be directly captured by a firm’s total goodwill without separating it into multiple channel-specific components. Given the implicit and ambiguous nature of goodwill, it is usually challenging for firms to accurately estimate channel-specific good will in practice (Berman 2018). Therefore, the model proposed in this study not only provides a more nuanced understanding of different decay rates in multiple ad channels, but also improves the utility of our conclu sions in practical applications.

Third, this study also contributes to the literature on the optimal allocation of advertising efforts between multiple channels. Prior studies typically either draw conclusions about a static framework (Gatignon and Hanssens 1987, Gopalakrishna and Chatterjee 1992) or focus on the optimal long-run stationary equilibrium in a dynamic framework (Naik and Raman 2003, Raman and Naik 2004). By showing how the ratio of a firm’s advertising efforts between different channels dynamically evolves over time, this study represents an important addition to this line of literature. In particular, we find that the ratio of a firm’s optimal advertising effort in the digital channel to that in the traditional channel monotonically decreases over time. When additionally incorporating the synergistic effect, we find that, although a weak synergistic effect does not change the decreasing pattern of the optimal allocation ratio, a strong synergistic effect creates a positive feedback loop between digital and traditional advertising, thus leading to an increasing trend in the optimal allocation ratio. Our insights urge firms not to fix the ratio of investments in different channels during the planning horizon, but rather to adjust it dynamically over time. Making dynamic advertising spending allocation between multiple channels is a complex problem, but is made easy by the closed-form solutions provided in this study. By directly applying our solutions and learning from our conclusions, firms can significantly improve the efficiency of their multichannel advertising and thus achieve higher profits.

Fourth, our study supplements the literature on the sequence of digital and traditional advertising investments. According to the purchase funnel theory (Lemon and Verhoef 2016), prior research typically suggests that in mature markets with established competitors, firms should prioritize traditional advertising in the early stages of the consumer purchasing journey to build broad awareness, with digital advertising employed primarily at the end of the funnel to capture potential customers and drive sales (referred to as the traditional first strategy). In contrast, our findings indicate that the traditional-first strategy is not optimal in monopolisti markets. Instead, firms should consistently invest in digital advertising while reserving traditional advertising for the later stages of the planning horizon (termed the digital-first strategy). This insight offers a new perspective on the advertising investment sequence, emphasizing the role of market structure in shaping firms’ advertising strategies. Specifically, owing to its broad reach and effectiveness in building widespread awareness, traditional advertising is essential for promoting brand differentiation and enhancing competitiveness in mature markets (Song 2025). However, its impact shrinks in monopolistic markets where interfirm competition is less important. In contrast, digital advertising excels in precision targeting, providing diverse ad content and formats, and facilitating real-time interaction with consumers (Rodgers and Thorson 2017). These characteristics contribute to the development of sustained and long-lasting goodwill. Coupled with other advantages such as lower costs, more efficient ad evaluation, and shorter feedback cycles (Rodgers and Thorson 2017), the digital-first strategy offers significant benefits for rapid market penetration, promoting sales, and achieving profitability in monopolistic markets. Furthermore, in the new e-commerce era, awareness and attention can often generate sales simultaneously, especially in the expanding influencer economy, where influencers continuously monetize their influence. In other words, the traditional purchase funnel theory may not fully align with this evolving landscape. In our model, awareness directly contributes to revenue, making it a better fit for the modern e-commerce context. Therefore, although the traditional-first strategy can be advantageous in fostering brand differentiation and enhancing competitiveness, its efficacy is highly contextdependent. Our research makes a contribution to this stream of literature by clarifying the boundaries of the applicability of the traditional-first strategy.

The present research has a few limitations, which suggest possible directions for future research. First, to ensure analytical tractability, we assume that there is no salvage value beyond the firm’s planning horizon. Although this assumption is widely adopted and reasonable for marketing campaigns of seasonal and onetime products, and for application scenarios where the revenue stream beyond the planning horizon carries significant uncertainty, incorporating a salvage value term into the model can be a valuable extension to our work. Second, our model applies only to monopolistic firms and does not take into account interfirm competition in duopoly or oligopoly markets. To comprehensively analyze the market environment, future research could explore the scenario involving multiple firms. Third, we assume a deterministic system dynamics for a firm’s goodwill while neglecting the impact of uncertainty. In actual market environments, uncertainty is inevitable, which may arise from market fluctuations, changes in consumer behaviors, and other external factors. Therefore, subsequent studies could incorporate environmental uncertainty into our model to examine the robustness of our managerial insights.

## Endnotes

<sup>1</sup> For simplicity, we abbreviate H(G(t), u (t), u (t), λ(t), t) as H.

<sup>2</sup> See https://www.sec.gov/Archives/edgar/data/1559720/00015 5972021000010/airbnb-10k.htm (accessed July 15, 2024).

<sup>3</sup> We only take into account their estimates using the first-order lag models.

<sup>4</sup> For simplicity, we abbreviate H(G(t), u<sub>1</sub>(t), u<sub>2</sub>(t), λ(t), t) as H.

<sup>5</sup> An alternative three-channel advertising model, comprising two digital channels and one traditional channel, is analyzed in the Online Appendix. The key findings are qualitatively robust.

<sup>6</sup> For simplicity, time arguments are omitted hereafter.

## References

Abedi VS, Berman O, Feinberg FM, Krass D (2022) Strategic new product media planning under emergent channel substitution and synergy. Production Oper. Management 31(5):2143–2166.

Aravindakshan A, Rubel O, Rutz O (2015) Managing blood dona tions with marketing. Marketing Sci. 34(2):269–280

Bass FM, Clarke DG (1972) Testing distributed lag models of adver tising effect. J. Marketing Res. 9(3):298–308.

Berman R (2018) Beyond the last touch: Attribution in online advertising. Marketing Sci. 37(5):771–792.

Chawlani Y (2024) What is a good CPM? Understanding CPM for B2B. Accessed February 3, 2025, https://salespanel.io/blog/ marketing/what-is-a-good-cpm/.

Chintagunta PK, Vilcassim NJ (1994) Marketing investment decisions in a dynamic duopoly: A model and empirical analysis. Internat. J. Res. Marketing 11(3):287–306.

Cui TH, Ghose A, Halaburda H, Iyengar R, Pauwels K, Sriram S, Tucker C, Venkataraman S (2021) Informational challenges in omnichannel marketing: Remedies and future research. J. Marketing 85(1):103–120.

Danaher PJ (2023) Optimal microtargeting of advertising. J. Marketing Res. 60(3):564–584

Dinner IM, Van HJH, Neslin SA (2014) Driving online and offline sales: The cross-channel effects of traditional, online display, and paid search advertising. J. Marketing Res. 51(5):527–545.

Feichtinger G, Hartl RF, Sethi SP (1994) Dynamic optimal control models in advertising: Recent developments. Management Sci 40(2):195–226.

Fruchter GE, Kalish S (1998) Dynamic promotional budgeting and media allocation. Eur. J. Oper. Res. 111(1):15–27.

Gatignon H, Hanssens DM (1987) Modeling marketing interactions with application to salesforce effectiveness. J. Marketing Res. 24(3):247–257.

Goldfarb A, Tucker C (2011) Search engine advertising: Channel substitution when pricing ads to context. Management Sci. 57(3):458–470

Gopalakrishna S, Chatterjee R (1992) A communications response model for a mature industrial product: Application and implications. J. Marketing Res. 29(2):189–200.

Hartl RF (1984) Optimal dynamic advertising policies for hereditary processes. J. Optim. Theory Appl. 43(1):51–72.

Hu B, Sun Z (2022) Managing self-replicating innovative goods. Management Sci. 68(1):399–419.

Jørgensen S, Kort PM, Zaccour G (2006) Advertising an event. Auto matica 42(8):1349–1355.

Kamien MI, Schwartz NL (1991) Dynamic Optimization: The Calculus of Variations and Optimal Control in Economics and Management (Advanced Textbooks in Economics), vol. 31 (Elsevier Science, Amsterdam).

Keller KL, Swaminathan V (2019) Strategic Brand Management: Building, Measuring, and Managing Brand Equity (Pearson, Harlow, UK).

Kwon ES, King KW, Nyilasy G, Reid LN (2019) Impact of media context on advertising memory. J. Advertising Res. 59(1):99–128.

Lemon KN, Verhoef PC (2016) Understanding customer experience throughout the customer journey. J. Marketing 80(6):69–96.

Mandese J (2022) Study benchmarks cheapest/most expensive ad media. Accessed February 3, 2025, https://www.mediapost. com/publications/article/371523/study-benchmarks-cheapest most-expensive-ad-media.html.

Mock The Agency (2023) The branding, marketing and design transfor mation of Airbnb. Accessed July 15, 2024, https://mocktheagency. com/content/branding-marketing-design-transformation-airbnb/.

Naik PA, Peters K (2009) A hierarchical marketing communications model of online and offline media synergies. J. Interactive Mar keting 23(4):288–299.

Naik PA, Raman K (2003) Understanding the impact of synergy in multimedia communications. J. Marketing Res. 40(4):375–388.

Naik PA, Prasad A, Sethi SP (2008) Building brand awareness in dynamic oligopoly markets. Management Sci. 54(1):129–138.

Naik PA, Raman K, Winer RS (2005) Planning marketing-mix strategies in the presence of interaction effects. Marketing Sci. 24(1):25–34.

Nerlove M, Arrow KJ (1962) Optimal advertising policy under dynamic conditions. Economica 29(114):129–142.

Olson EJ (2020) Digital vs traditional advertising: How much does each cost? Accessed July 8, 2024, https://thisisarray.com digital-vs-traditional-advertising-how-much-does-each-cost/.

Peres R, Van den Bulte C (2014) When to take or forgo new product exclusivity: Balancing protection from competition against word-of-mouth spillover. J. Marketing 78(2):83–100.

Prasad A, Sethi SP (2009) Integrated marketing communications in markets with uncertainty and competition. Automatica 45(3): 601–610.

Raman K, Naik PA (2004) Long-term profit impact of integrated marketing communications program. Rev. Marketing Sci. 2(1):0000102202154656161014.

Raman K, Mantrala MK, Sridhar S, Tang YE (2012) Optimal resource allocation with time-varying marketing effectiveness margins and costs. J. Interactive Marketing 26(1):43–52.

Rodgers S, Thorson E (2017) Digital Advertising: Theory and Research (Routledge, New York).

Sethi SP (2022) Optimal Control Theory: Applications to Management Science and Economics (Springer Texts in Business and Economics) (Springer, Cham, Switzerland).

Song SX (2025) Digital vs. traditional advertising and the recognition of brand intangible assets. Management Sci. 71(3):2035–2055.

Summers CA, Smith RW, Reczek RW (2016) An audience of one: Behaviorally targeted ads as implied social labels. J. Consumer Res. 43(1):156–178.

Zhu W, Kumar S, Mookerjee V (2024) Coordination in multibrand, multimedia advertising: Is it always a good thing? Inform. Systems Res. 35(3):1011–1033.

Copyright of Information Systems Research (INFORMS) is the property of INFORMS: Institute for Operations Research & the Management Sciences and its content may not be copied or emailed to multiple sites without the copyright holder's express written permission. Additionally, content may not be used with any artificial intelligence tools or machine learning technologies. However, users may print, download, or email articles for individual use.
