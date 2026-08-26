---
otero_id: 27993
otero_key: "UFZMKAC9"
title: "Competition and Distortion: A Theory of Information Bias on the Peer-to-Peer Lending Market"
authors: "Zhenhua Wu; Lin Hu; Zhijie Lin; Yong Tan"
year: "2021"
journal: "Information Systems Research"
doi: "10.1287/isre.2020.0956"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Competition and Distortion: A Theory of Information Bias on the Peer-to-Peer Lending Market

Zhenhua Wu,<sup>a</sup> Lin Hu,<sup>b</sup> Zhijie Lin,<sup>c,</sup>\* Yong Tan<sup>d</sup>

<sup>a</sup> School of Management, Nanjing University, Nanjing, Jiangsu 210000, P.R. China; <sup>b</sup> College of Business and Economics, Australian National University, Canberra, Australian Capital Territory 2601, Australia; <sup>c</sup> School of Economics and Management, Tsinghua University, Beijing 100084, P.R. China; <sup>d</sup> Michael G. Foster School of Business, University of Washington, Seattle, Washington 98195 \*Corresponding author

Contact: zhenhua.w@hotmail.com (ZW); lin.hu@anu.edu.au (LH); dr.zhijie.lin@gmail.com, https://orcid.org/0000-0003-0770-2390 (ZL); ytan@uw.edu, https://orcid.org/0000-0001-8087-3423 (YT)

Received: October 30, 2017 Revised: November 4, 2018; December 15, 2019; May 7, 2020 Accepted: May 22, 2020 Published Online in Articles in Advance: May 3, 2021

https://doi.org/10.1287/isre.2020.0956

Copyright: © 2021 INFORMS

Abstract. Despite the popular emergence of peer-to-peer (P2P) lending platforms, relevant research investigating the role of these platforms on P2P markets still lags. In this paper, we present a model to study the market incentives of P2P lending platforms’ optimal information-reporting strategies when the following exist: (i) uncertainty on the return of loans and (ii) competition from entrants. We focus on the information bias of platforms driven by demand-side actors—investors’ optimism/pessimism about risk—while we keep the platforms being rational. We characterize platforms’ equilibrium reporting strategies under different market conditions. Surprisingly, we find that when uncertainty is significant, and the threat of entry is strong but not detrimental, the platform has incentives to bias information toward investors’ biased beliefs. This result demonstrates a case where competition and uncertainty may jointly lead to information bias. However, a properly designed uncertainty-resolution mechanism could reduce the incentive. Our findings contribute to the literature on the P2P lending market by analyzing platform decisions and offer policy implications for regulating P2P lending market.

History: Senior Editor, Eric Zheng; Associate Editor, Yuliang Yao. Funding: This work was supported by National Natural Science Foundation of China [Grants 71872080, 72022007, 71729001, and 71490723].

Supplemental Material: The online appendices are available at https://doi.org/10.1287/isre.2020.0956.

Keywords: peer-to-peer lending platforms • information provider • <sup>fi</sup>nancial intermediaries • information bias • perfect Bayesian equilibrium

“Yes, competition rewards the sharp and hardworking. But it also often compels them to keep the frontiers of subtle deception in view. . . . The problem is that the promise of genuine ‘unique information’ comes with the reality of vulnerability to deception.” Robert J. Shiller (2015)

## 1. Introduction

The peer-to-peer (P2P) lending market has experienced rapid growth in many countries in the last few years because of the improvement of information technology (IT). It facilitates small business, which needs financial support to get investment directly and conveniently from investors through platforms such as Prosper and Lending Club. As of December 2018, the total volume of transactions conducted through the online P2P lending market had reached \$197.6 billion globally (Statista 2019). The market volume of P2P lending in the United States reached more than \$48 billion in 2018, which marked a 30% year-on-year increase from 2017. In the United Kingdom, P2P market volume was tripled from \$3.6 billion in 2015 to \$11.3 billion in 2018. In China, the total P2P trading volume (outstanding loans) had reached \$192 billion in 2017 (Liu and Jun 2018), and this number jumped to \$217.96 billion in 2018 (PYMNTS 2018).

The P2P lending market allows individual borrowers to acquire risky loans from other individuals without interacting with intermediary financial institutions such as banks. The most innovative feature of this market is the use of IT with automated algorithms to price and underwrite loans. However, the classical information-asymmetry problem is still one of the greatest challenges in this market. For instance, the borrowers usually know about their own financia status and repayment capabilities, but the individual lenders usually have little information about the true financial state of the purchased loans.

To mitigate this problem, most P2P lending platforms have developed their own algorithms to filter out and narrow down the type of borrowers or loans for the lenders. Platforms such as Upstart have announced they have created systems that use the most cutting-edge technology, such as machine learning and artificial intelligence, to assess the risk of a borrower and the market. In the meantime, research, for example, Michels (2012), finds that borrowers additional information disclosure on the P2P lending platform has improved the P2P lending-market efficiency. Additionally, some platforms design new market mechanisms, such as enabling direct communication between borrowers and lenders, to further reduce the information asymmetry between borrowers and lenders (Xu and Chau 2018).

Nonetheless, platforms per se also have information advantages over investors. First, after precisely assessing information through cutting-edge technology, the platforms have discretion on how to disclosure it. They can fully disclose the observed information, filter part of the information, or even distort the information based on their interests. Second, whether the cutting-edge technology can accurately assess risks is private information because the platform may not have the perfect technology. In the meantime, platforms may adopt different technologies—some platform may produce more accurate risk assessment than the others— because of, for instance, heterogenous background of founders. The heterogeneity in technology further gives platforms an incentive to overstate their technology advancement to attract more customers.

These two aspects explain the source of information asymmetry, in terms of adverse selection and moral hazard, on the side of platforms. Therefore, in this paper, we try to understand how information asymmetry on the side of platforms affects the market outcome of the P2P lending market. More specifically, we seek to study to what extent and through what mechanism rational P2P lending platforms filter or distort their observed information. We explore the possible consequences and whether there is any mechanism to prevent the platforms from doing so exists.

We develop a model of information bias on the P2P lending market to study the incentives of P2P lending platforms and how they choose different informationdisclosure strategies. The model has two periods. In every period, a random state represents the risk of the loan. Two platforms sequentially enter the market. Each platform investigates the risk and observes an informative signal about risk, based on which it announces the return rate of its loan product associated with the assessment of risk. The investor (or lender) then decides whether to invest in the platforms based on the platforms’ assessment of risk. The risk of loan has two components—systematic risk and idiosyncratic risk. Our model focuses on the systematic risk, because in principle, idiosyncratic risk can be diversified by constructing a loan portfolio. The factors influencing systematic risk can be, for example, overall economy, unemployment rate, government policy, regulation, and the nature of the loan.

One premise of our analysis is that we study the information bias of platforms driven by demand-side factors, that is, investors’ optimism/pessimism about risk, while we keep the platforms being rational. In principle, as intermediation between borrowers and investors, platforms may not have incentives to distort or filter the observed signal if the investors have an unbiased belief about the systematic risk before investment. Thus, in the model, without taking into account investors’ biased belief, platforms do not have incentives to distort or filter the signal and prefer disclosing accurate information. However, in reality, investors very often have optimistic or pessimistic beliefs or perceptions about the risk in the P2P lending market, especially, for instance, during economic booms or recessions. The biased beliefs would certainly affect investors’ investment decision, particularly when the platforms differ in their technological ability. As investors may doubt the platform’s technology to investigate or monitor the borrowers, their prior beliefs about the systematic risk may affect their posterior beliefs about the platform’s technological ability. Therefore, the platform may choose to bias the observed information toward investors’ biased prior beliefs in order to signal its capability as an accurate information provider.

We find several notable results. We find that when uncertainty is significant, and the threat of entry is strong but not detrimental—in other words, investors believe the likelihood of the entrant having high technological ability is high but not extremely high—the platform has an incentive to generate a biased risk assessment toward investors’ biased prior beliefs. This result demonstrates a case where competition and uncertainty may jointly lead to information bias and challenges the conventional view—competition mitigates market inefficiency. We illustrate this result by the following simple example. Suppose a P2P platform’s big-data analysis indicates the property market is going to crash soon, and in turn predicts a high default risk of a home loan product. However, if the investor initially believes the property-market crash is unlikely, he would probably infer that the risk assessment is inaccurate. Therefore, a platform that cares about future transactions and thus investors’ posterior beliefs has the incentive to bias the observed signal toward confirming the investors prior. The platform may filter or distort information for future concern though it has a disutility from not disclosing the observed signal. The more biased the investor’s prior is, the less likely the platform is to generate a risk assessment contradicting the prior.

Our second result shows the platform’s incentive to distort the observed signal will be weakened if an uncertainty-resolution mechanism exists. Given that the mechanism (e.g., the supervision from media or independent authority) could possibly reveal the true state of the systematic risk to the public, the chance that investors may observe the true state induces the platform to disclose the observed signal truthfully. The key assumption driving this result is that the platforms are assumed to care about their market reputation. Therefore, if a platform biases the observed signal to confirm the investor’s prior, it takes the risk that the true state will be revealed and contradict the risk assessment. Then, the platform could suffer because the investor might withdraw the investment and choose a new platform. The chance of ex-post uncertainty resolution increases, and the likelihood of information bias in equilibrium decreases.

Nevertheless, conventional wisdom, which argues competition mitigates market inefficiency, still persists under certain conditions. If the uncertainty-resolution tmechanism is extremely effective (i.e., resolves the uncertainty with extremely high probability), the incumbent platform has no incentive to distort information. Moreover, when market power is imbalanced in the sense that the threat of entry is either weak or too strong, the incumbent platform would truthfully disclose the information even if uncertainty is never resolved. In this situation, the platform can do little to change the outcome except to truthfully disclose the information, because disutility arises from not doing so. As the likelihood of uncertainty resolution increases, an additional cost of nontruthful disclosure arises: Once the truth is revealed, the investor would withdraw investment from the platform if its risk assessment does not match the truth.

We also find the previous results hold not only in the case of sequential competition but also in the case of simultaneous duopoly competition, where two platforms simultaneously compete for the market share. In both cases, platforms have incentives to distort the information because of the uncertainty of risk and the threat of entry. However, the potential loss of reputation return, that is, future benefit, will reduce these incentives.

Our results shed lights on policy implications on the P2P lending market and are particularly relevant in the information era. The advancement of IT, such as filtering algorithms, makes platforms easier to identify and then cater to investors’ biased beliefs. As our model suggests, introducing competition in the market may not always be effective in reducing the demand-side information bias. Thus, identifying conditions under which competition improves efficiency becomes important. Alternatively, in order to reduce information friction and improve the development of the P2P lending market, we may also turn to ways that affect investors’ perception of the market and platforms.

## 2. Literature Review

The growing importance of P2P lending markets has recently attracted academic attention. However, most of the research on this topic focuses on either the supply side, lenders, or the demand side, borrowers, of the market. To the best of our knowledge, this paper is the first analytical paper to focus on the P2P lending platform’s behavior and analyze how market mechanisms affect these platforms’ incentives and behaviors. Our research is generally related to three streams of literature.

## 2.1. Online P2P Lending

Our research focuses on the market of P2P lending platforms. We study the competition among platforms and how it affects platforms’ and investors decisions. Research on P2P lending platforms studies different mechanisms adopted by platforms, such as loan price, trust building, and design of incentive systems. For instance, Chen et al. (2014) investigate the uniform-price auction mechanism, which Prosper used before 2010. They theoretically prove that in both complete- and incomplete-information settings, borrowers might overpay the lenders. Wei and Lin (2016) investigate two pricing mechanisms: auctions and posted price. They find the posted-price mechanism brings short-term benefits to both borrowers and lenders but results in a net loss in social welfare. Caldieraro et al. (2018) analyze an online P2P lending market by proposing and testing a theory in which countersigning provides a mechanism to alleviate information asymmetry about loans posted on a platform. More specifically, they demonstrate that borrowers can post unverifiable loan descriptions on the P2P lending platform to signal loan quality to the investors. From the view of information provision, Vallee and Zeng (2019) share a similar feature with our research. They study optimal platform design in terms of the loan information provided to investors to maximize volumes. However, the mechanism they characterize differs from ours. The authors argue that because of the heterogeneity on the investor side, choosing a high prescreening intensity to provide more information to the investor may not be optimal for the platform.

Empirically, Greiner and Wang (2010) investigate trust-building mechanisms on the P2P lending platform. They find borrowers’ financial information, such as economic status and credit score, and other nonfinancial information, such as borrowers’ social capital, can also influence lenders’ trust. Lin et al. (2013) use the data from Prosper.com to empirically study how the networks influence the transactions in the online P2P lending market. They find the online friendship of borrowers can be a signal of credit quality, whereby the friendships increase the chance of successful funding. Iyer et al. (2015) study the screening mechanism in a P2P lending market where lenders can observe both standard financial information and soft information about borrower quality. They find the lender can predict default with greater accuracy than the prediction based only on a borrower’s credit score. Hildebrand et al. (2016) investigate the impact of the origination fee on the borrower’s default rate. After eliminating the origination fee, they find group leaders bids are perceived as a signal of high loan quality; however, they also have high default rates. The default rate decreases only when a group leader has sufficient skin in the game or when the origination fee is eliminated. Jiang et al. (2018) empirically study the investors’ herding behaviors with consideration of the market structure. They find the investors’ herding behavior is accentuated by platforms’ market share and the total volume of the total fund but is attenuated by their time in operation.

Most of these studies focus on the platform per se and either focus on factors related to the supply side (i.e., small investors or lenders) or the demand side (i.e., small businesses or borrowers) of a P2P lending market. However, the market mechanisms, such as competition and market reputation, are not explicitly studied. Our research differs from this stream by explicitly modeling the P2P market competition with consideration of asymmetric information on the platform’s technology. It further helps us understand how the platform’s disclosure strategy is influenced jointly by the threat of entry and uncertainty of risks.

Current research about investors’ decisions on P2P platforms investigates what factors may affect their decisions. They find that interest rate, borrowers characteristics, and other verifiable information are influential (Bachmann et al. 2011, Herzenstein et al. 2011b, Duarte et al. 2012). The P2P lending platforms in these studies are assumed to be dummy players that provide reliable information on borrowers. Our work differs from these studies and allows the platform per se to be a strategic player. Then, we study how market competition and investors’ beliefs about the systematic risk and the platform’s technology adoption affect platforms’ decisions.

## 2.2. Financial Intermediation

This research is also related to the literature on financial intermediation, which is pioneered by Brealey et al. (1977) and Diamond (1984). Classical research on financial intermediation, for example, Allen and Santomero (1997), Bhattacharya and Chiesa (1995), Hellmann et al. (2000), and Santomero (1984), demonstrates that because of asymmetric information between borrowers and lenders, financial markets can poorly perform or even fail when borrowers privately observe their characteristics, for example, the present value of the risky projects, but lenders cannot distinguish between them. Then, Diamond (1984) argues that financial intermediaries can help alleviate problems of asymmetric information by acting as delegated monitors. Gorton and Pennacchi (1995) empirically find the effect of technological progress can reduce the information asymmetries between lenders and borrowers.

Research since Holmstrom and Tirole (1997), for example, Sufi (2007) and Keys et al. (2010), finds traditional financial intermediaries, namely, banks, have a serious moral-hazard problem because their monitoring and due-diligence efforts are unobservable. To alleviate the moral-hazard problem from the financial intermediary, the literature argues that retaining a large financial stake in the borrowing firm could make the intermediary exert the necessary effort in due diligence and monitoring.

In this study, we model the P2P lending platform as a financial intermediary that cannot retain any financial stake of borrowers but can only provide information such as risk assessments about the true state of the risk, which relates to return of loans. Given this feature of the P2P lending platform, our results show that a third party that could reveal the true state may mitigate the distortion in the P2P lending market.

## 2.3 Herding

Herding in individual choice has been studied in a wide range of fields, including economics, finance, and information systems. In the economics and finance literature, our work is closely related to the herding on the priors. The literature, for example, Scharfstein and Stein (1990), Banerjee (1992), Prendergast (1993), and Brandenburger and Polak (1996), studies how an agent’s actions depend on prior beliefs of factors that may determine the agent’s utility.

Most similarly, Prendergast (1993) theoretically illustrates that when an agent, for example, a worker, observes a noisy signal about the opinion of the principal, for example, a manager, the agent would bias his report toward what he believes the principa wants to hear. Logically, our work shares some common features with this paper. The P2P lending platform in our paper is similar to the agent, and the investor is similar to the principle. However, our paper does not focus on the incentive contract within an organization, but on the market incentive, namely, competition. One of our main results illustrates that the uncertainty about the true state of the systematic risk and the technology adoption of the P2P lending platform implies information is not communicated as efficiently as when competition is absent Our paper highlights a tradeoff between inducing platforms to stay in the market to reduce the transaction cost and encouraging them to be honest in disclosing their findings on the risky loans.

Research in information systems studies the herding phenomenon in P2P lending. For instance, Zhang and Liu (2012) provide evidence of rational herding among investors on listings on Prosper.com. They use a listing’s cumulative amount of funding as the measure of herding and find that well-funded listings tend to attract more funding. Simonsohn and Ariely (2008) and Herzenstein et al. (2011a) define herding behavior as a greater likelihood of receiving additional bids, and they find that strategic herding in a loan auction is positively associated with its subsequent performance. Liu et al. (2015) provide evidence of relational herding, where investors are more likely to herd when the crowd includes friends rather than strangers. Furthermore, herding happens more often among offline friends than among online friends and strangers. All these studies empirically focus on herding behavior among investors. Our paper differs from theirs by studying how the P2P lending platform herds on investors’ beliefs about the systematic risk through strategically disclosing the observed information on the systematic risk.

## 3. Baseline Model

## 3.1. Setup

Consider a P2P lending market where a mass of borrowers seeks to raise funds and an investor seeks to invest her excess wealth through P2P lending platforms. Two P2P lending platforms, indexed by $j \in \{ \bar { 1 } , 2 \}$ sequentially enter the market in period $t \in \{ 1 , 2 \}$

3.1.1. Borrowers and Loan Products. A unit mass of heterogeneous borrowers applies for loans from each platform every period, whose credit risks will be assessed by platforms. Each platform designs a loan product based on the borrowers’ credit risk.

Two types of risks for loans exist. One is the idiosyncratic risk of individual borrowers. It comes from shocks to individual borrowers’ characteristics (e.g., individual income shock) and can be diversified from forming a loan portfolio. The other is the systematic risk from the market that cannot be diversified by forming portfolios. It can be influenced, for instance, by the overall economy, unemployment rate, government policy, regulation, and the nature of the loan (e.g., the risk of a home loan is influenced by the housing market). The systematic risk is the same across platforms but can vary over time.

Here, a loan product from each platform is a portfolio of risky loans from the mass of borrowers. The idiosyncratic risk of borrowers has been diversified through the portfolio. The systematic risk of the loan at period t is summarized by a random state $s _ { t } \in \{ l , h \} .$ where $s _ { t } = l ( \mathrm { r e s p e c t i v e l y } , s _ { t } = h )$ means that at period $t ,$ the systematic risk of the loan product is low (respectively, high). In particular, the probability of $s _ { t } = l$ $( \mathrm { i . e . } )$ , the systematic risk is low) is $\mathrm { P r } ( s _ { t } = l ) = p ,$ whereas the probability of $s _ { t } = h \ ( \mathrm { i . e . }$ , the systematic risk is high) is $\operatorname* { P r } ( s _ { t } = \dot { h } ) = 1 - p .$ The distribution of systematic risk is publicly known. So p is the common prior of the state being l for all players.

The price of the loan is determined by the demand and the supply of the loan market. In the case of a binary state, we assume there is a return rate that is associated with each state realization. That ${ \mathrm { i } } \mathbf { s } ,$ the return of the loan is $R _ { l }$ (respectively, $R _ { h } )$ if the state is l (respectively, h). According to asset-pricing theory (Cochrane 2009), we assume a risk premium exists, that is, $R _ { h } > R _ { l }$

3.1.2. Platforms. At every period $t ,$ each platform $j$ processes loan applications from borrowers. It assesses the risks of the loans and forms a loan portfolio to diversify the idiosyncratic risk. Then, based on its assessment of the state $s _ { t } ,$ that is, the systematic risk, it sets the return rate of the loan product. For simplicity, we assume all platforms can diversify the idiosyncratic risks, and henceforth we focus on whether the platform can accurately assess the systematic risk (the state).

More specifically, during the process of assessment, each platform receives a signal $\omega _ { j , t } \in \{ l , h \}$ (about the state), whose distribution depends on the risk assessment technology of the platform. With probability $\lambda _ { j } ,$ platform j is high tech and observes the signal that perfectly reveals the true state. With probability $1 - \bar { \lambda _ { j } } ,$ the platform is mediocre and observes a noisy signal distributed according to

$$
\operatorname * {P r} \bigl (\omega_ {j, t} = h | s _ {t} = h \bigr) = \operatorname * {P r} \bigl (\omega_ {j, t} = l | s _ {t} = l \bigr) = q.
$$

That is, the probability of observing l (respectively, h) state when the true state is l (respectively, h) is q. Write $\theta _ { j } \in \{ \theta _ { T } , \theta _ { M } \}$ for the type of platform $j ,$ where $\theta _ { T }$ represents the high-tech type, and $\theta _ { M }$ represents the mediocre type. Type is private information and can only be observed by platform j itself.

The high-tech and mediocre types capture the fact that platforms may have different ability in predicting the state. The high-tech platforms have better information sources or information-processing technologies than the mediocre type in assessing the state. For instance, some platforms may have better access to special information sources or advanced information technologies because of their connections to governments, banks, tech giants, and so on.<sup>1</sup> We assume the high-tech type can fully observe the true state for simplicity. In fact, as long as the high-tech type can observe more accurate signal than that observed by the mediocre platform, our analyses still hold.

We assume the signal observed by the mediocre platform is noisy yet informative in Assumption 1. That is, although the signal is not perfect about the true state $( \mathrm { i . e . , ~ } q < 1 )$ , conditional on observing a signal of l (respectively, h), the true state is more likely to be l (respectively, $h ) _ { \ast }$ , that is, $\mathrm { P r } ( s _ { t } = l | \omega _ { j , t } = l ) > \dot { \mathrm { P r } } ( s _ { t } = l )$ (respectively, $\mathrm { P r } ( s _ { t } = h | \omega _ { j , t } = h ) > \mathrm { P r } ( s _ { t } = h ) )$ , which is equivalent to $q > p .$

Assumption 1. The signal observed by the mediocre platform is informative, that is, $q \in ( p , 1 )$

Based on the signal observed, each platform j makes an assessment about the state $x _ { j , t } ( \bar { \omega } _ { j , t } ) \in \{ l , \bar { h } \}$ , and announces the associated return rate $\dot { R } ( x _ { j , t } ) \in \{ R _ { l } , R _ { h } \}$ The return rate $R ( \cdot )$ is strictly increasing in $x _ { j , t } \ \left( \mathrm { i . e . , } \right.$ $R _ { l } < R _ { h } )$ and thus is a sufficient statistic of $x _ { j , t }$ . Therefore, by announcing return rate $R ( x _ { j , t } )$ , the platform implicitly discloses its assessment of the state $x _ { j , t } .$ Thus, platform $j ^ { \prime } \mathbf { s }$ strategy can be summarized by its choice $\sigma ( x _ { j , t } | \omega _ { j , t } , \theta _ { j } )$ at every history, where σ $\cdot ( x _ { j , t } | \omega _ { j , t } , \theta _ { j } )$ specifies the probability that the type $\theta _ { j }$ platform implicitly reports the assessment $x _ { j , t }$ when the signal realization is $\omega _ { j , t }$ . We say a platform truthfully discloses the signal at period t if its assessment is the same as the signal observed at that period $x _ { j , t } = \omega _ { j , t }$ . That ${ \mathrm { i } } \mathbf { s } ,$ taking investor and the other platform’s strategies as given, a type $\theta _ { j } \in \{ \theta _ { T } , \theta _ { M } \}$ platform j plays $\sigma ( \omega _ { j , t } \big | \tilde { \omega } _ { j , t } , \theta \big ) \big = 1$ for any $\omega _ { j , t } \in \{ l , h \}$ . Otherwise, we say it nontruthfully discloses the signal.

We say a platform reports the true state if the assessment is the same as the true state, that is, $x _ { j , t } = s _ { t } .$ Otherwise, we say the platform misreports the true state. A platform misreports the true state in two cases: (i) the platform receives a signal the same as the true state $( \omega _ { j , t } = s _ { t } )$ but nontruthfully discloses the signal $( x _ { j , t } \neq \omega _ { j , t } ) ; \mathrm { ( i i ) }$ the platform receives a signal different from the true state $( \omega _ { j , t } \neq s _ { t } )$ but truthfully discloses the signal $( x _ { j , t } = \omega _ { j , t } )$

At every period, a platform earns a payoff $B > 0$ if the investor invests in that platform, and 0 if the investor does not invest. The platform’s payoff also depends on whether its assessment of the state matches the true state. At every period, if a platform misreports the true state, a disutility $C > 0$ would arise. Thus, in this case, the platform $\mathbf { \chi } ^ { \prime } \mathbf { s }$ stage payoff at that period is $B - C$ . The disutility can arise from the fact that the platform dislikes not accurately predicting the state or is afraid of potential reputation damage when the market doubts its ability to predict the true state.

Formally, platform $j ^ { \prime } \mathbf { s }$ stage payoff at period t is

$$
U _ {j, t} = \mathbb {1} _ {j, t} ^ {\mathrm{invest}} B - \left(1 - \mathbb {1} _ {x _ {j, t} = s _ {t}}\right) C,
$$

where

$\mathbb { 1 } _ { j , t } ^ { \mathrm { i n v e s t } } = \left\{ { \small \begin{array} { l } { 1 } \\ { 0 } \end{array} } \right.$ if invest in platform j at period t if not invest in platform j at period t

$$
\text { and } \mathbb {1} _ {x _ {j, t} = s _ {t}} = \left\{ \begin{array}{l l} 1 & \text { if } x _ {j, t} = s _ {t} \\ 0 & \text { if } x _ {j, t} \neq s _ {t}. \end{array} \right.
$$

The platform cares about its payoff at every period, and the time discount factor is $\beta .$ Thus, platform $j ^ { \prime } \mathrm { s }$ expected payoff at the beginning of the first period is $\mathrm { E } ( \hat { U } _ { j , 1 } ) + \hat { \beta } \mathrm { E } ( \mathbf { \hat { \it U } } _ { j , 2 } )$ . Here, $\Breve { U } _ { 2 , 1 } = \Breve { 0 }$ because platform 2 enters the market in the second period.

3.1.3. The Investor. The investor has a unit of cash. At the beginning of every period, the investor first decides whether to invest in the P2P lending market and then chooses which platform to invest in. If she does not invest in the $\mathrm { P } 2 \mathrm { P }$ lending market, she will receive $v _ { 0 }$ utility. If she chooses to invest in platform $j$ at period $t ,$ she earns a net payoff $v ( R ( x _ { j , t } ) , \bar { s } _ { t } )$ if the state is $s _ { t }$ . We denote the investor’s utility at period t as

$$
V _ {t} = \mathbb {1} _ {j, t} ^ {\text { invest }} v \big (R \big (x _ {j, t} \big), s _ {t} \big) + \Big (1 - \mathbb {1} _ {j, t} ^ {\text { invest }} \Big) v _ {0}.
$$

We assume the net payoff $v ( R ( x _ { j , t } ) , s _ { t } )$ satisfies two properties as stated in Assumption 2. First, information is valuable to the investor. That is, the investor’s expected payoff is weakly higher when the return is matched with the true state. Consequently, ceteris paribus, the investor prefers an accurate assessment of the risk and thus weakly prefers the hightech type to the mediocre type ex ante.

Second, the utility of purchasing a loan is higher than that of not purchasing. This assumption is for simplicity and would not affect the qualitative nature of our results. In the case where it is violated, we would need an extra condition to ensure the investor chooses to invest in any platform, under which our analysis remains the same.

Assumption 2. We assum $v ( R ( x _ { j , t } ) , s _ { t } )$ satisfies the $f o l -$ lowing properties.

i. Given any period and any realization of the true state $s \in \{ l , h \} , \operatorname { E } _ { s } [ \tilde { v ( R _ { s } , s ) } ] \geq \operatorname { E } _ { s } [ v ( \bar { R } _ { s ^ { \prime } } , s ) ]$ for any $s ^ { \prime } \in \{ l , h \}$ and $s ^ { \prime } \neq s ,$ , where $\mathbb { E } _ { s } [ v ( R _ { s } , s ) ]$ and $\mathrm { E } _ { s } [ v ( R _ { s ^ { \prime } } , s ) ]$ are the investors expected payoff of the loan products with return rate $R _ { s }$ and $R _ { s ^ { \prime } }$ at true state $s ,$ respectively.<sup>2</sup>

ii. For $\begin{array} { r } { z n y p a i r o f ( x , s ) \in \{ l , h \} \times \{ l , h \} , \operatorname* { m i n } _ { ( x , s ) } v ( R ( x ) , s ) \geq v _ { 0 } . } \end{array}$ Here, mi $\boldsymbol { \mathfrak { n } } _ { ( x , s ) } v ( R ( x ) , s )$ represents the investor’s utility of purchasing a loan product in the worst-case scenario.

At the end of every period, the investor may directly observe the true state with probability $\rho \in \dot { ( 0 , 1 ) }$ The rationale for introducing this uncertainty-resolution mechanism is to capture institutional constraints, such as law restrictions, government regulations, or media supervisions. When $\rho \to 1$ , it corresponds to a market with a relatively complete law system, government regulations, and media supervisions, whereas $\rho \to 0$ corresponds to the opposite case.

If the investor observes the true state at the end of period $t ,$ we say uncertainty is resolved. Otherwise, we say uncertainty is not resolved. We denote the outcome of uncertainty resolution by $a _ { t } \in \{ l , h , \emptyset \}$ , where $a _ { t } = l$ represents that the investor observes the state being l at period $t , a _ { t } = h$ represents that the investor observes the state being h at period $t ,$ and $a _ { t } = \emptyset$ represents that the investor does not observe the state at period t.

The investor cares about her payoff at every period, and the time discount factor is also $\beta .$ . Thus, investor’s expected payoff at the beginning of the first period is $\mathsf { \hat { E } } ( V _ { 1 } ) + \mathsf { \hat { \beta } } \mathsf { \hat { E } } ( V _ { 2 } )$ .

3.1.4. Investor’s Beliefs. The investor has beliefs on the state and the type of the platform. Because the distribution of the state is public, the investor’s prior of the state being l is $p .$ Without loss of generality, we assume that ex ante, the investor (or the public) is optimistic about the state. That is, she thinks the systematic risk of loans is more likely to be low, that is, $p > 1 / 2$

Assumption 3. The investor is optimistic about the systematic risk of loans, that is, $p > 1 / 2$

Investor optimism is one kind of investor sentiment about the market. The investment sentiment literature documents that investors can be optimistic or pessimistic under different scenarios (Baker and Wurgler (2006)). Here, we do not take a stand on whether the investor is optimistic or pessimistic about risks. We take the optimism as an example of investors’ biased attitude against risks, and the result would be symmetric if we assume investor pessimism instead of investor optimism. Our focus is on how investor sentiment affects the platform’s incentive to bias information and the associated implications on P2P markets.

The investor’s prior of platform j being high tech $( \theta _ { T } )$ is $\lambda _ { j } .$ . The investor updates her belief about a platform’s type when she observes (i) the return rate posted by that platform or (ii) the outcome of uncertainty resolution is realized. The investor’s posterior belief at any node of the game under any information set A is a mapping $\mu _ { j } : A \to [ 0 , 1 ]$ , where $\mu _ { j } ( A )$ specifies the probability of platform j being type $\theta _ { T }$ , and the information set A includes all the history about platforms’ actions and the outcome of uncertainty resolution if any.

3.1.5. Timeline. The timeline of the game evolves as follows.

1. Period 1

1a. Nature determines platforms’ types $\theta _ { j }$ for $j \in \{ 1 , 2 \} ,$ ; each platfrom observes its own type.

1b. The borrowers apply for loans at platform 1, and the state $s _ { 1 }$ is realized but is not observed by players. The common prior of the state being l is $p .$ .

1c. Platform 1 assesses the loan risk and observes a signal $\omega _ { 1 , 1 }$ about the state s .

1d. Platform 1 sets the return rate $R ( x _ { 1 , 1 } )$

1e. The investor decides whether to invest in platform 1. If she does not invest in platform 1, then she quits the P2P lending market and executes her outside option; otherwise, the game continues as follows.

1f. The investor observes the true state $s _ { 1 }$ with probability $\rho \in ( 0 , 1 )$ , and the outcome of uncertainty resolution $a _ { 1 }$ is realized.

1g. The investor updates her belief of platform j being high tech and decides whether to stay in the current investment or withdraw the investment from platform 1.

2. Period 2

2a. Platform 2 enters the market.

2b. The borrowers apply for loans in the platforms, and the state $s _ { 2 }$ is realized but is not observed by players. The common prior of the state being l is $p .$

2c. Each platform $j \in \{ 1 , 2 \}$ assesses the loan risk and observes a signal $\omega _ { j , 2 }$ about the state $s _ { 2 }$

2d. Each platform $j \in \{ 1 , 2 \}$ sets the return rate $R ( x _ { j , 2 } )$

2e. The investor updates her beliefs about the platforms.

• If the investor keeps the investment with platform 1 at the end of the first period, she decides whether to renew the loan product with a new return rate offered by platform 1.

• If the investor withdraws any investment at the end of the first period, she decides whether to purchase the loan products of platform 2.

• If she does not invest in any platform, then she quits the market and executes her outside option.

2f. The investor observes the true state s with probability $\rho ^ { \prime } \in ( 0 , 1 )$ and the outcome of uncertainty resolution $a _ { 2 }$ is realized.

$2 \mathrm { g } .$ . The investor withdraws the investment, and the return of the investment is realized.

## 3.2. Discussion of the Model

3.2.1. Role of Borrowers. The role of borrowers is passive in our model. In practice, P2P platforms offer loans to borrowers and at the same time sell loan products to the investors. Here, we assume the former part has already happened, and focus on the strategic interaction in the latter. The literature has been discussing the interactions between platforms and borrowers, while hardly addressing the interactions between platforms and investors, which we think are of great importance as well.

3.2.2. Sequential Entering. We have two reasons to assume P2P lending platforms entering the market sequentially. First, in practice, we often observe P2P platforms are sequentially entering the P2P lending market. For instance, Prosper, the first $\mathrm { P } 2 \mathrm { P }$ platform in the United States, entered the market in 2005 and played as a monopolist until in 2007 the Lending Club entered the market. Second, we aim to use the most parsimonious model to endogenously capture the reputation effect in the P2P lending market. This assumption is not crucial for the qualitative nature of our results but can significantly simplify our analysis. To show robustness, Section 5 studies an alternative setting where both platforms enter the market simultaneously, and the result is consistent with our baseline model.

## 4. Equilibrium Analysis

Our model specifies a dynamic game of incomplete information. We study the perfect Bayesian equilibrium of the game, in which the following conditions must hold:

i. Each type of platform’s strategy is optimal given the investor’s belief and strategy, and (if any) the other platform’s strategy.

ii. The investor’s strategy is optimal, given the platforms’ strategies.

iii. The investor’s beliefs follow the Bayes Rule whenever applicable.

We define two forms of equilibria based on whether the platforms truthfully disclose the signal.

De<sup>fi</sup>nition 1. Truth disclosure equilibrium (TDE).

i. We say an equilibrium is a truth disclosure equilibrium (TDE) if at every history on the equilibrium path, all types of platforms truthfully disclose the signals, that is, $\sigma ( \omega _ { j , t } | \omega _ { j , t } , \theta ) = 1$ for any $j \in \{ 1 , 2 \}$ $t \in \{ 1 , 2 \} , \theta \in \{ \theta _ { T } , \theta _ { M } \}$ and $\omega _ { j , t } \in \{ l , h \}$

ii. Otherwise, we say an equilibrium is a non–truth disclosure equilibrium (n-TDE).

Remark 1. In what follows, we investigate under what scenarios we have (n-)TDE. We first study two benchmarks of our baseline model in which (i) no threat of entry exists, and (ii) uncertainty of the state is always resolved. We show in these two cases any equilibrium is a TDE. We then characterize the equilibrium of the general model and show how the threat of entry and uncertainty of the state jointly distorts the platforms incentives from disclosing the true state.

## 4.1. Benchmark 1: No Threat of Entry

We first consider the case where no threat of entry exists in the second period, and thus platform 1 is a monopoly. Without the threat of entry, platform 1 faces the same problem in two periods, and thus simply maximizes its per-period payoff. As a result, the platform always truthfully discloses the signal regardless whether it is a high tech or mediocre type.

Proposition 1. In a monopoly market without threat of entry, any equilibrium is a TDE.

## Proof. See Online Appendix A. □

This result implies that in a monopoly market without the threat of entry, the platform has no incentive to bias the information but at its best to disclose the true state independent of its type. This result holds regardless whether the investor has a chance to observe the state or not. Without the threat of entry, platform 1 believes the investor will invest in the platform anyway and has no incentive to cater to the investor’s biased belief about the state.

4.2. Benchmark 2: Uncertainty Is Always Resolved We now turn to the case where a threat of entry exists in the second period. In the meantime, the uncertainty of the state is always resolved at the end of the first period, that is, $\rho = 1$

First, each type of platform will always truthfully disclose the signal in the second period because each type of platform would maximize its per-period payoff. By $\rho = 1$ , ceteris paribus, the investor weakly prefers the high-tech type. Thus, in the first period, a hightech–type platform 1 will always truthfully disclose the signal. Second, a mediocre-type platform 1 would want to mimic the behavior of the high-tech type so that the investor would hold to the investment in platform 1 in the second period. Because the signal received by a mediocre-type platform is informative, that is, $q > p ,$ the best way to report the true state is to disclose the signal truthfully. The following proposition formally states this result.

Proposition 2. If uncertainty is resolved at the end of the first period, that is, $\rho = 1$ , any equilibrium is a TDE.

## Proof. See Online Appendix A. □

Combined with Section 4.1, we show that unresolved uncertainty of the state or the threat of entry alone cannot shape the platform’s incentive to bias information. In what follows, we show in the general case that with the above two elements, the platform would bias information toward the investor’s prior about the state.

## 4.3. The General Model

We turn to the general model where platform 2 enters the market in the second period, and uncertainty is not fully resolved at the end of the first period, that is, $\rho \in [ 0 , \dot { 1 } )$ . Lemma 1 characterizes each type of platform’s equilibrium strategies in the second period. In the second period, each type of platform would maximize its per-period payoff and thus truthfully disclose the signal.

Lemma 1. In equilibrium, both the high-tech– and the mediocre-type platform truthfully disclose the signal in t 2.

## Proof. See Online Appendix A. □

4.3.1. Platforms’ Strategies. Lemma 1 specifies all types of platforms’ strategies in the second period in any equilibrium. Thus, for platforms’ equilibrium strategies, we only need to characterize each type of platform 1’s strategy in the first period, because only platform 1 is in the market in the first period. Henceforth, we drop the subscript j from $\omega _ { j , t } , x _ { j , t } , \theta _ { j }$ in period t 1, that is, $\omega _ { 1 } \equiv \omega _ { 1 , 1 } , x _ { 1 } \equiv x _ { 1 , 1 }$ and $\dot { \theta _ { 1 } } \equiv \theta$ . For simplicity for any $s , s ^ { \prime } \in \{ l , h \}$ , we write $\sigma ( s | \hat { s ^ { \prime } } ; \theta ) \equiv \sigma ( x _ { 1 } = s | \omega _ { 1 } \hat { = } s ^ { \prime } ; \bar { \theta } )$

for the probability that the type $\theta$ platform 1 reports return $R _ { s }$ when observing a signa $s ^ { \prime }$ at the first period.

4.3.2. Investors’ Strategies. We then turn to investors strategies. Over time, the investor makes three decisions: (i) at stage 1e of the timeline, she decides whether to invest in platform 1; (ii) at stage 1g, she decides whether to hold to her investment in platform 1 or withdraw her investment from platform 1 so that she can consider the loan product in platform $2 ;$ and (iii) at stage ${ 2 \mathrm { e } } ,$ she decides whether to invest in platform 1 or 2, which depends on her decision on (ii). By Assumption 2, for case (i) the investor would invest in platform 1, and for case (iii) would invest in the platform chosen in case (ii). So we only need to consider case (ii). We write $d ( A ) : A \to [ 0 , 1 ]$ for the investor’s decision (ii) at her information set A at stage ${ 1 } _ { \mathrm { g } } ,$ where $d ( A ) \in [ 0 , 1 ]$ represents the probability that the investor holds to the investment in platform 1.

In particular, at stage $1 { \mathrm { g } } \left( { \mathrm { i . e . } } \right.$ , at the end of the first period), the investor’s information set A includes the platform’s risk assessment $x _ { 1 }$ (and thus its associated return rate $R ( x _ { 1 } ) )$ , as well as the outcome of uncertainty resolution $a _ { 1 }$ in the first period, where $( x _ { 1 } , a _ { 1 } ) \in$ $\{ l , h \} \times \{ l , h , \emptyset \}$ . Thus, we can write the investor’s decision at stage 1g as $d ( x _ { 1 } , a _ { 1 } ) \in [ 0 , 1 ]$ and her belief at stage 1g as $\mu ( x _ { 1 } , a _ { 1 } ) \in [ 0 , 1 ]$

## 4.4. Equilibrium Characterization

We first consider the TDE. Suppose a TDE exists where platforms truthfully disclose the signal, that is, $\sigma ^ { * } ( l | \widehat { l } ; \widehat { \theta ) } = 1$ and $\sigma ^ { * } ( h | \widehat { h } ; \theta ) = 1$ for all $\theta ;$ the investor chooses her decision $d ^ { * } ( x _ { 1 } , a _ { 1 } )$ under her posterior belief $\bar { \mu } ( x _ { 1 } , a _ { 1 } )$ for any $( x _ { 1 } , a _ { 1 } ) \in \{ l , h \} \times \{ l , h , \emptyset \}$ . Lemma 2 specifies the investor’s posterior belief in any TDE.

Lemma 2. In any TDE, for any $( x _ { 1 } , a _ { 1 } ) \in \{ l , h \} \times \{ l , h , \emptyset \}$ the investor’s posterior belief $\bar { \mu } ( x _ { 1 } , a _ { 1 } )$ satisfies the following conditions:

$$
\begin{array}{l} 0 = \bar {\mu} (l, h) = \bar {\mu} (h, l) <   \bar {\mu} (h, \emptyset) <   \lambda_ {1} <   \bar {\mu} (l, \emptyset) <   \bar {\mu} (l, l) \\ = \bar {\mu} (h, h) <   1, \end{array}
$$

where

$$
\bar {\mu} (l, \emptyset) = \frac {\lambda_ {1} p}{\lambda_ {1} p + (1 - \lambda_ {1}) (q + p - 2 p q)},
$$

$$
\bar {\mu} (h, \emptyset) = \frac {\lambda_ {1} (1 - p)}{\lambda_ {1} (1 - p) + (1 - \lambda_ {1}) (q + p - 2 p q)},
$$

$$
a n d \bar {\mu} (l, l) = \bar {\mu} (h, h) = \frac {\lambda_ {1}}{\lambda_ {1} + (1 - \lambda_ {1}) q}.
$$

## Proof. See Online Appendix A. □

First, if uncertainty is resolved $( \mathrm { i . e . , } a _ { 1 } = l \mathrm { o r } h )$ and the platform misreports the true state $( { \mathrm { i . e . , } } x _ { 1 } \neq a _ { 1 } )$ , the investor would infer platform 1 is of a mediocre type with probability 1, because a high-tech platform receives a perfect signal and thus always reports the true state in a TDE. Thus, we have $\bar { \mu } ( l , h ) = \bar { \mu } ( h , l ) = 0 .$

Second, if the uncertainty is resolved $( \mathrm { i . e . , } a _ { 1 } = l \mathbf { o } 1$ r h) and the platform reports the true state $( { \mathrm { i . e . , } } x _ { 1 } = a _ { 1 } )$ then in a TDE, the platform can be of a high-tech type that always receives a perfect signal or a mediocre type that receives a signal that matches the true state. We can compute the investor’s posterior by applying the Bayes rule, and show that $\bar { \lambda _ { 1 } } < \bar { \mu } ( l , l ) = \bar { \mu } ( \bar { h } , \bar { h } ) < \bar { 1 }$ Intuitively, the investor’s posterior of the platform being a high-tech type is lower than 1 because a mediocre platform may also report the true state but higher than the prior because a mediocre platform cannot always report the true state.

Finally, if the uncertainty is not resolved $( \mathrm { i . e . , } a _ { 1 } = \varnothing )$ we have $0 < \bar { \mu } ( h , \emptyset ) < \lambda _ { 1 } \dot { < } \bar { \mu } ( l , \emptyset )$ by the Bayes rule. Intuitively, the investor has a biased prior toward state $l ;$ thus, she believes that the true state is more likely to be l. Because in a TDE, a high tech platform reports the true state more often than the mediocre platform, the investor would believe a platform to be more likely of a high-tech type than she thought ex ante $\left( \mathrm { i . e . , } \bar { \mu } ( l , \emptyset ) > \bar { \lambda _ { 1 } } \right)$ if its assessment of state is l. By contrast, the investor would believe a platform to be less likely of a high-tech type than she thought ex ante $( \mathrm { i . e . , } \bar { \mu } ( h , \emptyset ) < \lambda _ { 1 } )$ if its assessment of state is $h ,$ because the chance that a high-tech platform’s assessment is h is positive, $\bar { \mu } ( h , \emptyset ) > 0$

Proposition 3 shows a unique TDE exists under three scenarios. The first is that the resolution mechanism is very strong; that $\mathrm { i s } , \rho$ is sufficiently close to 1. This case is similar to that of benchmark 2 where a high-tech platform would truthfully disclose the signal to indicate its type, whereas the mediocre platform has an incentive to mimic the high-tech type. As a result, all types of platforms truthfully disclose the signal.

In the second scenario, the investor ex ante believes the entrant (platform 2) is highly likely to be of the high-tech type. In particular, when the investor’s belief about platform 2 being high tech is higher than her posterior of platform 1 conditional on platform 1’s risk assessment matching with the true state, she would always withdraw her investment from platform 1 and consider investing in platform 2. Then, all types of platform 1 would prefer truthfully to nontruthfully disclosing the signal because disutility arises from not doing so. When the investor’s belief about platform 2 being high tech is not as high but is still higher than her posterior of platform 1 conditional on platform $1 ^ { \prime } { \mathrm { s } }$ risk assessment being l and uncertainty not being resolved, the investor would choose to withdraw her investment from platform 1 if she does not observe the true state. As a best response, all types of platform 1 would truthfully disclose the signal so that the investor is most likely to hold to her investment in platform 1 when uncertainty is resolved.

In the third scenario, the investor ex ante believes platform 2 is highly unlikely to be of the high-tech type. In particular, when the investor’s belief about platform 2 being high tech is lower than her posterior of platform 1 conditional on platform $1 ^ { \prime } \bar { \bf s } ^ { \bar { } }$ risk assessment being h and uncertainty not being resolved, the investor would hold to her investment in platform 1 unless she observes the true state differing from platform 1’s risk assessment. As a best response, all types of platform 1 would again truthfully disclose the signal to maximize the likelihood of the investor holding to her investment.

Before stating the proposition, we denote $\begin{array} { r } { \rho ^ { * } \equiv _ { 2 \beta Q ( 1 - \hat { \psi } ) } ^ { \beta Q - ( 1 - 2 \hat { \psi } ) C } } \end{array}$ as a cutoff value for the probability of uncertainty resolution, where $\begin{array} { r } { \hat { \psi } = \frac { ( 1 - q ) \overset { \star } { p } } { q + p - 2 p q } } \end{array}$ and $Q = B - ( 1 - q ) C$

## Proposition 3. A unique TDE exists in the following three cases.

i. Given any $\lambda _ { 2 } \in ( \bar { \mu } ( h , \emptyset ) , \bar { \mu } ( l , \emptyset ) )$ , and $\rho > \rho ^ { * } .$ , a unique TDE exists in which $\boldsymbol { d } ( l , \emptyset ) = \boldsymbol { d } ( h , h ) = \boldsymbol { d } ( l , l ) = 1$ and $d ( h , l ) = d ( l , h ) = d ( h , \emptyset ) = 0$

ii. Given any $\lambda _ { 2 } > \bar { \mu } ( l , \emptyset ) ,$ a unique TDE exists in which $d ( h , l ) = d ( l , h ) { \overset { } { = } } d ( h , { \overset { . } { 0 } } ) = d ( l , \emptyset ) = 0 , d ( h , h ) = d ( l , l ) = 1 |$ $i f \lambda _ { 2 } < \bar { \mu } ( h , h ) ;$ otherwise, $d ( h , h ) = d ( l , l ) = 0 .$

iii. Fix any $\lambda _ { 2 } < \bar { \mu } ( h , 0 ) .$ , a unique TDE exists in which $d ( h , \emptyset ) = d ( l , \bar { \emptyset } ) = d ( h , h ) = d ( l , l ) = \dot { 1 } a n d d ( h , l ) = d ( l , h ) = 0 .$

## Proof. See Online Appendix A. □

Proposition 4 characterizes the scenario where a unique n-TDE exists. In this scenario, the investor does not have an extreme prior belief about platform 2, and the uncertainty-resolution mechanism is not extremely strong. In this case, when uncertainty is not resolved, the investor is more likely to hold to her investment in platform 1 if the risk assessment is $l ,$ that is, $d ( h , \emptyset ) < d ( l , \emptyset )$ . This result arises from the fact that the investor is optimistic about the risk. Thus, when a platform observes a state $h ,$ it may nontruthfully disclose the signal to cater to the investor’s optimism about the risk, especially when uncertainty is not likely to be resolved.

However, nontruthful disclosure comes with two costs. First, when uncertainty is resolved, the investor would withdraw any investment in platform 1 if the risk assessment differs from the true state. Thus, once got caught, platform 1 would lose its market share. This cost is less likely to occur when $\rho$ is relatively low. Second, a platform has a disutility C every period from nontruthful disclosure, which exists regardless of the uncertainty-resolution outcome. Thus, only when the benefit from catering to the investor’s optimism crosses the hurdle of the platform’s disutility and the cost of getting caught would the platform nontruthfully disclose the signal.

Proposition 4. Given any $\lambda _ { 2 } \in ( \bar { \mu } ( h , \emptyset ) , \bar { \mu } ( l , \emptyset ) )$ and $\rho < \rho ^ { * }$ any equilibrium is an $n { - } \check { T } D E$ . In particular,

$\begin{array} { r } { \dot { i } . ~ \sigma ( l | \hat { l } ; \theta ) = 1 } \end{array}$ for all $\theta \in \{ \theta _ { T } , \theta _ { M } \}$ , and $0 \leq \sigma ( l | \hat { h } ; \theta _ { T } ) <$ $\sigma ( l | \hat { h } ; \theta _ { M } ) \leq 1$

ii. $d ( h , h ) = d ( l , l ) = 1 , d ( h , l ) = d ( l , h ) = 0 , a n d 0 \leq d ( l , \emptyset ) \leq$ $d ( h , \emptyset ) \leq 1$

## Proof. See Online Appendix A. □

The messages are clear from this proposition. Given that the investor has a balanced belief about the types of platforms 1 and 2, and uncertainty is not resolved, the investor will be more inclined to hold to the in vestment if the risk assessment is $l ,$ that is, $d ( l , \emptyset ) \leq$ $d ( h , \emptyset )$ , because of her optimism about risk. As a response, at least the mediocre type platform 1 is likely to bias the information to cater to investors’ optimism, that is, $\sigma ( l | \hat { h } ; \theta _ { M } ) > 0$

If we restrict our attention to the equilibrium where a high-tech platform always truthfully discloses the signal, only one such equilibrium exists. In this case, the mediocre type still assigns positive probability to the strategy of nontruthfully disclosing the signal. The following corollary states the above result.

Corollary 1. Given any $\lambda _ { 2 } \in ( \bar { \mu } ( h , \emptyset ) , \bar { \mu } ( l , \emptyset ) )$ , and $\rho < \rho ^ { * }$ an n-TDE that has the high-tech type always truthfull disclosing the signal exists and is unique in which

i. σ<sub>(</sub>l<sub>|</sub><sup>ˆ</sup>l; θ<sub>)</sub> <sub></sub> 1 for all $\theta \in \{ \theta _ { T } , \theta _ { M } \} , \sigma ( l | \hat { h } ; \theta _ { T } ) = 0$ and

$$
\begin{array}{l} \sigma \Big (l | \hat {h}; \theta_ {M} \Big) \\ = \left\{ \begin{array}{l l} 1 - \frac {\lambda_ {1} (1 - \lambda_ {2}) (1 - p)}{\lambda_ {2} (1 - \lambda_ {1}) (p + q - 2 p q)} & i f \bar {\mu} (h, \emptyset) <   \lambda_ {2} <   \lambda_ {1} \\ \frac {\lambda_ {1} p (1 - \lambda_ {2})}{\lambda_ {2} (1 - \lambda_ {1}) (p + q - 2 p q)} - \frac {p q + (1 - p) (1 - q)}{p + q - 2 p q} \\ & i f \lambda_ {1} <   \lambda_ {2} <   \bar {\mu} (l, \emptyset). \end{array} \right. \end{array}
$$

$$
\mathrm{ii.} d (h, h) = d (l, l) = 1, d (h, l) = d (l, h) = 0,
$$

$$
d (h, \emptyset) = \left\{ \begin{array}{l l} 1 - \frac {(1 - 2 \hat {\psi}) (C + \rho \beta Q)}{(1 - \rho) \beta Q} & i f \bar {\mu} (h, \emptyset) <   \lambda_ {2} <   \lambda_ {1}, \\ 0 & i f \lambda_ {1} <   \lambda_ {2} <   \bar {\mu} (l, \emptyset), \end{array} \right.
$$

and

$$
d (l, \emptyset) = \left\{ \begin{array}{l l} 1 & \text {if} \bar {\mu} (h, \emptyset) <   \lambda_ {2} <   \lambda_ {1}, \\ \frac {(1 - 2 \hat {\psi}) (C + \rho \beta Q)}{(1 - \rho) \beta Q} & \text {if} \lambda_ {1} <   \lambda_ {2} <   \bar {\mu} (l, \emptyset). \end{array} \right.
$$

Proof. See Online Appendix A. □

In general, if a high-tech platform truthfully discloses the signal, the mediocre type would tend to mimic the high-tech type. However, as we see in the corollary, even if a high-tech platform truthfully discloses the signal, the mediocre platform still would not always truthfully disclose the signal. Thus, the equilibrium strategies $\sigma ( l | \hat { h } ; \theta _ { M } )$ and $\sigma ( \bar { l } | \hat { h } ; \theta _ { M } )$ in Corollary 1 serve as lower bounds of those among all n-TDEs.

We summarize our results in Figure 1, which illustrates how the effectiveness of the uncertaintyresolution mechanism and the degree of the threat of entry affect the type of equilibrium (TDE or n-TDE). When the uncertainty-resolution mechanism is not extremely effective, and the entry of threat is strong but not detrimental (region 2), the platform has an incentive to bias information toward the investor’s biased belief. This result demonstrates a case where competition may lead to information bias.

When the threat of entry is weak (region 1) or detrimental (region 4), the market power is imbalanced, the platform cannot do much to change the outcome. $\mathrm { A s } \mathrm { \ a }$ result, the platform will truthfully disclose the signal because a disutility arises from not doing so.

On the other hand, when the uncertainty-resolution mechanism is extremely effective (region 3), that ${ \mathrm { i } } \mathbf { s } ,$ $\rho > \rho ^ { * } .$ , the platform is highly likely to incur the cost of being caught if it nontruthfully discloses the signal. As a result, it truthfully discloses the signal. The cutoff value $\rho ^ { * }$ increases in the investor’s prior about the state being $l , p ,$ and the discount factor, $\beta .$ As the investor’s prior becomes more biased, or the platform cares more about the future, $\rho ^ { * }$ increases, meaning the equilibrium is more likely to be an n-TDE.

## 5. Extensions

In this section, we extend our baseline model in two directions. First, we consider a continuum of heterogeneous investors instead of a representative investor in the market. Second, we use an alternative duopoly model to analyze the (simultaneous) competition. The results of the two extensions are consistent with those of our baseline model.

Figure 1. Plot Equilibrium Forms Against $\rho$ and $\lambda _ { 2 }$  
![](/api/attachments/UFZMKAC9/fulltext/images/4e1cde8cdd4caf1860a5834fcd881a8a79c56e93e2ba525a54f8236daccbdf4a.jpg)

To simplify the analysis, throughout this section, we assume $\dot { \lambda } _ { 1 } = \lambda _ { 2 } \equiv \dot { \lambda _ { , } }$ , that is, investor ex ante believes the two platforms are equally likely to be of a high-tech type. In doing so, we focus on the case where the two platforms have equal market power ex ante.

## 5.1. Heterogeneous Investors

The baseline model assumes one representative investor, which is equivalent to assuming investors are homogenous. Now, we relax this assumption by assuming a continuum of heterogenous investors indexed by $\alpha \in [ 0 , \bar { \alpha } ]$ , where α represents investors heterogenous characteristics such as risk aversion attitude, investment experience and so on. We then write investor $\alpha ^ { \prime } \mathrm { s }$ utility of investing in platform j at period t as $v ( R ( x _ { j , t } ) , s _ { t } ; \alpha )$ . Similar as before, investor α receives $v _ { 0 }$ utility from not investing in any platform. Throughout this section, instead of assuming Assumption 2, we make similar but slightly stronger assumptions about investors’ net payoffs.

Assumption 4. Given any period t, any platform j, and any $\alpha \in [ 0 , \bar { \alpha } ] , v ( R ( x _ { j , t } ) , s _ { t } ; \alpha )$ satisfies the following properties i. $\mathrm { E } _ { s } [ v ( R _ { s _ { t } } , s _ { t } ; \alpha ) ] \geq \mathrm { E } _ { s _ { t } } [ v ( R ( x _ { j , t } ) , s _ { t } ; \alpha ) ]$ , where $\mathrm { E } _ { s _ { t } } [ v ( R _ { s _ { t } } ,$ $s _ { t } ; \alpha ) ]$ represents investor α’s expected per-period payoff of her investment in platform j when the platform alway reports the true state, and $\mathrm { E } _ { s _ { t } } [ v ( R ( x _ { j , t } )$ , s ; α represents the investor α’s expected per-period payoff of her investment given any risk-assessment realization $x _ { j , t }$ of the platform. ii. $v ( R ( x _ { j , t } ) , s _ { t } ; \alpha )$ is continuous in $\alpha ,$ and max min $( x _ { j , t } , s _ { t } )$ $v ( R ( x _ { j , t } ) , s _ { t } ; \alpha ) > v _ { 0 }$ for any pair of $( x _ { j , t } , s _ { t } ) \in \{ l , h \} \times \{ l , h \}$

Similar as before, Assumption 4, part i, implies accurate information is valuable. Here, we assume investor α has the highest expected payoff when risk assessment of the platform she invested in always matches the true state among all risk assessment-state $\left( { { x } _ { j , t } } , { { s } _ { t } } \right)$ pairs. Part ii ensures that a positive mass of investors gain higher utility from investing in any platform than that from not investing at all.

The timeline is the same as in the baseline model Then, at stage ${ 1 } \mathrm { g } ,$ if investor α does not invest in platform 1 at stage 1e, the investor would consider each platform’s product with $\textstyle { \frac { 1 } { 2 } }$ probability and then decide whether to invest in the platform at stage 2e, because ex ante investor equally prefers the two platforms.

We denote $D _ { t }$ for the set of investors investing in any platform at period $t ,$ and thus the measure of set $D _ { t } , m ( D _ { t } )$ , represents the demand of the P2P lending market at period t.

Lemma 3. In any equilibrium, the following statements about the demand of the P2P market hold:

i. m<sub>(</sub>D<sub>t)</sub> > 0 for any $t \in \{ 1 , 2 \}$

$$
D _ {1} = D _ {2}
$$

Proof. See Online Appendix B. □

Lemma 3 suggests that, in every period, a positive mass of investors invest in the P2P lending market $( m ( D _ { t } ) > 0 )$ , and the investors who invest in the market in the first period continue to invest in the market in the second period $\left( D _ { 1 } = D _ { 2 } \right)$ ). Henceforth, we drop the subscript t from $D _ { t }$

An investor who chooses to invest in the market in the first period would quit the market in the second period only if her expected per-period payoff is lower than the payoff from her outside option. The situation would not happen because her expected per-period payoff of the second period from investing in the market would at least be as high as that of the first period. Following the same logic as in the baseline model, an investor would invest in platform 1 in the second period if and only if her posterior of platform 1 being high tech is higher than her prior of platform 2 being high tech, whereas the latter equals to the investor’s prior of platform 1 being high tech in the first period. In the meantime, in the second period, all types of platforms truthfully disclose the signal. By the facts that their signals are informative, and investors gain higher payoff from true state-reporting, an investor who invests in the first period expects a higher per-period payoff in period 2 than period 1. As a result, the demand of the P2P lending market does not vary across periods. The demand is positive because a positive mass of investors gain higher payoffs from investing in any platform than that from not investing at all by Assumption 4, part ii.

Corollary 2. In any equilibrium, the equilibrium strategies of the platforms are the same as in Propositions 3 and 4 and Corollary 1 with $\lambda _ { 1 } = \lambda _ { 2 } \equiv \lambda ;$ ; any investor $\alpha \in D p l a y s$ the same strategy as the representative investor in Propositions 3 and 4 and Corollary 1 with $\lambda _ { 1 } = \lambda _ { 2 } \equiv \lambda ;$ and any investor $\alpha ^ { \prime } \notin D$ quits the market at stage 1e of the timeline and executes her outside options.

## Proof. See Online Appendix B. □

Corollary 2 shows that the results in the model with heterogenous investors are consistent with that in the baseline model. By Lemma 3, as long as an investor invests in the market in the first period, she would continue to invest in the market in the second period. As a result, her decision relies purely on the comparison of her beliefs of each platform being a hightech type. Therefore, the incentives between this kind of investors and the platforms are the same as in the baseline model, and thus we have the same equilibrium prediction of their strategies. Meanwhile, those investors who decide not to invest in the market at the first period would quit the market and execute their outside options in stage 1e. Therefore, they would not affect the equilibrium outcomes of other players in the game.

## 5.2. Duopoly Market

The alternative model has only one period because two P2P lending platforms simultaneously enter the market. Hence, throughout Section 5.2, we drop the subscript t from all time-varying variables in the baseline model. Now two platforms simultaneously post the return rates $( R ( x _ { 1 } ) , R ( x _ { 2 } ) )$ <sub>)</sub> and implicitly report the associated risk assessments $( x _ { 1 } , x _ { 2 } )$ . After observing the return rates (or equivalently, the risk assessments), the investor updates her belief, chooses one of the platforms and invests one unit asset to th platform. If the investor’s expected payoffs from the two platforms are the same, the investor will invest in either platform with equal probability. The timeline of the game in the alternative model is as follows.

1. Nature determines each platform’s type $\theta _ { j } \in \{ \theta _ { T } , \theta _ { M } \}$ for $j \in \{ 1 , 2 \} .$ ; each platform observes its own type.

2. The borrowers apply for loans at both platforms, and the state of systematic risk s is determined but is not observed by players. The common prior of the state being l is $p .$

3. Each platform j assesses the loan risk and observes a signal ω about the state s.

4. Each platform $j \in \{ 1 , 2 \}$ sets its return rate $R ( x _ { j } ) \in \{ R _ { l } , \hat { R } _ { h } \}$

5. The investor observes the true state of systematic risk s with probability $\rho \in ( 0 , 1 )$ , updates her belief about the type of each platform, and decides whether to invest in any platform and which one to invest in.

6. The payoffs are realized at the end of the game.

The per-period payoff of the investor is the same as in the baseline model, but she only cares about her payoff at the current period. The payoff of the platform is a bit different. As before, if the investor invests in platform $j ,$ then the platform gains a utility $B > 0 ;$ otherwise, it gains a utility 0. If the platform nontruthfully discloses the signal, a disutility s arises. However, in the alternative model, if the investor invests in the platform, the latter has a reputation gain $z ,$ which is a random variable with the support $\{ \bar { 0 } , Z \}$

$$
z = \left\{ \begin{array}{l l} Z & \text {if s = a or a = \emptyset ,} \\ 0 & \text {otherwise,} \end{array} \right.
$$

where $Z \geq B$ . It means, conditional on investor’s investment in a platform, the latter gains a utility Z if it risk assessment matches the uncertainty-resolution outcome or uncertainty is never resolved, and 0 utility otherwise. Thus, the payoff of platform $j \in \{ 1 , 2 \}$ in the alternative model is

$$
U _ {j} = \mathbb {1} _ {j} ^ {\mathrm{invest}} B - \Big (1 - \mathbb {1} _ {x _ {j} = s} \Big) C + \operatorname{E} (z).
$$

5.2.1. Players’ Strategies. For any $s , s ^ { \prime } \in \{ l , h \}$ and $\theta \in$ $\{ \theta _ { T } , \theta _ { M } \}$ , we write $\sigma _ { j } ( s | \hat { s ^ { \prime } } ; \theta ) \equiv \dot { \sigma _ { j } } ( x _ { j } = s | \omega _ { j } = s ^ { \prime } ; \theta )$ for platform $j ^ { \prime } \mathbf { s }$ strategy, that is, the probability that the type θ reports return $R _ { s }$ when observing a signal $s ^ { \prime }$ at stage 4 of the timeline. We write $( d _ { j } ( \bar { x } _ { 1 } , x _ { 2 } , a ) ) _ { j = 1 , 2 } \in$ $[ 0 , \breve { 1 } ] \times [ 0 , 1 ]$ for the investor’s strategy where $( x _ { 1 } , x _ { 2 } , a ) \in$ $\{ l , h \} \times \{ l , h \} \times \{ l , h , \emptyset \}$ , and $d _ { j } ( x _ { 1 } , x _ { 2 } , a )$ represents the probability that the investor invests in platform j at stage 5 of the timeline.

5.2.2. Equilibrium Predictions. In this section, we focus on pure strategy equilibrium. Proposition 5 shows $\operatorname { t h a t } ,$ under two conditions, any equilibrium is an n-TDE if the two platforms simultaneously compete in the market. The first condition is that the resolution mechanism is not very strong. Similar as before, if the probability of uncertainty resolution is not large, the mediocre platforms have incentives not to truthfully disclose the signal, because the expected loss from nontruthfully disclosing will be less than the benefit of convincing the investor to invest in the platform. The second condition imposes an restriction on the investor’s net payoffs: The expected payoff of investing in a mediocre platform that truthfully discloses the signal when the signal is l is higher than that when the signal is h.

Proposition 5. Any equilibrium is an n-TDE if the $f o l -$ lowing conditions hold: (i) $\begin{array} { r } { \rho < \frac { \hat { \psi } ( B + Z ) + ( 1 - \hat { \psi } ) ( \hat { B - C } ) } { 2 ( 1 - \hat { \psi } ) ( B + Z ) + ( 1 - \hat { \psi } ) ( B - C ) } } \end{array}$ and (ii) $q v ( R _ { l } , l ) + ( 1 - q ) v ( R _ { l } , h ) \geq q v ( R _ { h } , h ) + ( 1 - q ) v ( R _ { h } , l )$

## Proof. See Online Appendix B. □

In the extension, the market power of the two platforms are equal, so we no longer need the discussion about the comparison of the priors on platforms. Beyond that, our result is consistent with before: When the possibility of uncertainty resolution is low, platforms have incentives to filter or distort information toward the investor’s biased belief.

## 6. Discussion

An extensive literature on the P2P lending market, for example, Bachmann et al. (2011), Duarte et al. (2012), and Herzenstein et al. (2011b), finds that factors such as interest rate, borrowers’ characteristics, and information (both hard and soft) may affect investors decisions. Investors lean on these factors to infer the quality of loans, which is not directly observed by investors. In other words, these factors are tools for investors to alleviate the agency problem of the borrowers. Therefore, we expect the rise of P2P lending platforms as financial intermediations and information providers would alleviate the classical agency problems between investors and borrowers, especially when the competition is introduced to the market. However, the previous argument implicitly assumes away the agency problems of platforms per se. Logically, this assumption is questionable, because the platforms are operated by rational individuals who are subject to the agency problem, including both adverse selection and moral hazard (see Arrow 1971, Marschak and Radner 1972, and Holmstrom 1982 for the most classical argument).

As discussed in the Introduction, we do observe evidence in which platforms do not always provide truthful information about their loan products. The cause can be that (i) platforms may have inferior information technology and thus provide inaccurate information, or (ii) they strategically filter or distort information for their own interests. As a response, investors doubt platforms’ abilities and their motives and change their decisions correspondingly. We ex amine the strategic interaction among different kinds of platforms and investors and study the associated equilibrium outcome. Interestingly, we find cases where platforms bias information to cater to the investor’s biased belief when the threat of entry exists, and uncertainty is not always resolved, even though no player prefers releasing/receiving biased information. This result challenges the conventional view that introducing competition always mitigates in formation asymmetry: By introducing an entrant, the incumbent may filter or distort information that hurts the welfare of all players.

Alternatively, we can view the platforms’ equilibrium behavior as herding: When competition is introduced, the platforms herd on the investor’s prior about the risk of the loan to gain reputation and keep the investor in the future. As a result, the market incentive mechanism, namely, competition, may not work effectively because of the herding behavior of the P2P lending platforms. This view supplements to the herding literature (Prendergast 1993, Brandenburger and Polak 1996). On the one hand, the platforms herding behaviors induce information frictions. On the other hand, their herding behaviors help the platforms maintain their customer base and facilitate transactions between borrowers and investors. Hence, our study highlights a tradeoff between reducing transaction costs and inducing information frictions

Caution should be exercised when extrapolating our result to the general argument that the equilibrium with information friction (n-TDE) always exists under threat of entry and thus competition is useless. In fact, n-TDE exists only if the following two conditions are satisfied. First, the entrant platform is similar to the incumbent platform ex ante. Second, the probability that the uncertainty of the state of risk will be resolved is not high.

One premise of our analysis is that we study the information bias of platforms driven by demand-side factors, that is, investors’ optimism about risk, while we keep the platforms being rational. The rationality assumption of platforms allows us to study the demanddriven information bias in the most parsimonious model. In practice, platforms may have an incentive to bias information because of their own behavioral bias about risk. Our model provides a benchmark with rational platforms and can be extended to study supplyside bias because of platforms’ own preferences in future research.

Our results shed light on policy implications on the P2P lending market and are particularly relevant in the information era. The advancement of IT, such as filtering algorithms, makes platforms easier to identify and then cater to investors’ biased beliefs. As our model suggests, introducing competition in the market may not always be effective in reducing the demandside information bias. Thus, identifying conditions under which competition improves efficiency becomes particularly important.

For instance, when uncertainty is very likely to be resolved, and/or the entrant is very likely to be a high-tech type, any equilibrium is a TDE; that is, no information friction is introduced by competition. As a result, to reduce information friction of the P2P lending market overall, we may want to fund independent organizations to investigate the aggregate/ systematic risks, which increases the likelihood of uncertainty resolution. Meanwhile, improving the quality of entrants by setting a higher barrier to entry increases investors’ perception of entrants being high tech and thus reduces information friction in the P2P lending market. The regulator can impose a stricter qualification requirement for entrant platforms on the P2P lending market.

Alternatively, in order to reduce information friction and improve the development of the P2P lending market, we may also turn to ways that affect investors’ perception of the market and platforms. For instance, by increasing media exposure on financial knowledge or news, the investor may have a less biased belief about risk.

From the perspective of platforms, to increase the likelihood of a successful entry, they can seek endorsement from credible third parties to enhance investors’ prior belief about their ability as information providers. Prosper and the Lending Club have adopted this strategy. For instance, Prosper puts media with a good reputation in the business report, such as Bloomberg Businessweek and Wall Street Journal, on their front page. The Lending Club uses Economist and New York Times to endorse its qualifications.

## 7. Conclusion

In this paper, we present a new model to understand how the P2P lending platforms’ information-reporting strategies would be affected by investors’ biased beliefs. Interestingly, we find that when uncertainty is significant, and the threat of entry is strong but not detrimental, truthful disclosure of observed information may not happen in equilibrium, especially when the competition is introduced. This result does not arise from the P2P lending platforms’ own preference of biased reporting but from rational platforms’ desire to stay in the market for long-term returns. Our model sheds light on policy implications for the P2P lending market because it identifies conditions that may improve information efficiency.

Nevertheless, our model still has limitations and leaves several questions open. First, our model assumes investors can only decide whether to purchase loans and have no bargaining power to influence the platforms’ decisions in other ways. Although in reality, the majority of the supply side of the P2P lending market is small investors, institutional investors do exist and can potentially influence the platforms in other ways. Introducing institutional investors<sup>3</sup> that have the bargaining power would boost the P2P lending market on the one hand and affect the platform’s incentive to disclose observed information on the other hand. Moreover, the institutional investor usually could conduct regular monitoring/ supervision on platforms’ performance, which would mitigate the platform’s agency problem.

Second, our main results rely on the assumption that the P2P lending platforms care about their future reputation return from the market. In the baseline model, we endogenize this market return in a reduced form so that we can use the most parsimonious model to highlight the channel of demand-side information bias. Future research could examine a more complex market structure that could determine the reputation return and how it would affect platforms’ decisions.

Finally, P2P lending and other FinTech products are the joint products of financial and technological innovations. The outcome of innovations strongly depends on the government’s preferences and regulations. Therefore, we could also consider the role of government in this model. One direct strategy is to endogenize the parameter ρ as a decision variable of the regulator, which may shed light on implications for government decisions. Overall, our model can be the building block for all these extensions.

## Endnotes

<sup>1</sup> For instance, we could consider the Funding Circle, a UK P2P lending platform that has received 100 million pounds from the stateowned British Business Bank, as a platform that, with high proba bility, might be a high-tech platform.

<sup>2</sup> Note that E v R , s pv R , l 1 p v R , h and $\operatorname { E } _ { s } [ v ( R _ { s ^ { \prime } } , s ) ] =$ $p v ( R _ { h } , l ) + ( 1 - p ) v ( R _ { l } , h ) .$

<sup>3</sup> See https://www.siliconrepublic.com/start-ups/p2p-lending-peer -to-peer-investors.

## References

Allen F, Santomero AM (1997) The theory of financial intermediation. J. Bank. Finance 21(11–12):1461–1485.

Arrow KJ (1971) The Theory of Risk Aversion (Markam, Chicago)

Bachmann A, Becker A, Buerckner D, Hilker M, Kock F (2011) Online peer-to-peer lending - a literature review. J. Internet Banking Commerce 16(2):1–18.

Baker M, Wurgler J (2006) Investor sentiment and the cross-section of stock returns. J. Finance 61(4):1645–1680.

Banerjee AV (1992) A simple model of herd behavior. Quart. J. Econom. 107(3):798–817.

Bhattacharya S, Chiesa G (1995) Proprietary information, financial intermediation, and research incentives. J. Financial Intermediaries 4(4):328–357.

Brandenburger A, Polak B (1996) When managers cover their pos teriors: Making the decisions the market wants to see. RAND J. Econom. 27(3):523–541.

Brealey R, Leland HE, Pyle DH (1977) Informational asymmetries, financial structure, and financial intermediation. J. Finance 32(2): 371–387.

Caldieraro F, Zhang JZ, Cunha M, Shulman JD (2018) Strategic information transmission in peer-to-peer lending markets. J. Marketing 82(2):42–63.

Chen N, Ghosh A, Lambert NS (2014) Auctions for social lending: A theoretical analysis. Games Econom. Behav. 86:367–391.

Cochrane JH (2009) Asset Pricing, revised ed. (Princeton University. Press, Princeton, NJ).

Diamond DW (1984) Financial intermediation and delegated moni toring. Rev. Econom. Stud. 51(3):393–414.

Duarte J, Siegel S, Young L (2012) Trust and credit: The role of appearance in peer-to-peer lending. Rev. Financial Stud. 25(8): 2455–2484.

Gorton GB, Pennacchi GG (1995) Banks and loan sales marketing nonmarketable assets. J. Monetary Econom. 35(3):389–411.

Greiner ME, Wang H (2010) Building consumer-to-consumer trust in e-finance marketplaces: An empirical analysis. Internat. J. Electronic Commerce 15(2):105–136.

Hellmann TF, Murdock KC, Stiglitz JE (2000) Liberalization, moral hazard in banking, and prudential regulation: Are capital re quirements enough? Amer. Econom. Rev. 90(1):147–165.

Herzenstein M, Dholakia UM, Andrews RL (2011a) Strategic herding behavior in peer-to-peer loan auctions. J. Interactive Marketing 25(1):27–36.

Herzenstein M, Sonenshein S, Dholakia UM (2011b) Tell me a good story and I may lend you money: The role of narratives in peerto-peer lending decisions. I Marketing Res. 48:S138–S149

Hildebrand T, Puri M, Rocholl J (2016) Adverse incentives in crowdfunding. Management Sci. 63(3):587–608

Holmstrom B (1982) Moral hazard in teams. Bell J. Econom. 13(2): 324–340.

Holmstrom B, Tirole J (1997) Financial intermediation, loanable funds, and the real sector. Quart. J. Econom. 112(3):663–691.

Iyer R, Khwaja AI, Luttmer EF, Shue K (2015) Screening peers softly: Inferring the quality of small borrowers. Management Sci. 62(6): 1554–1577.

Jiang Y, Ho YC, Yan X, Tan Y (2018) Investor platform choice: Herding, platform attributes, and regulations. J. Management Inform. Systems 35(1):86–116.

Keys BJ, Mukherjee T, Seru A, Vig V (2010) Did securitization lead to lax screening? evidence from subprime loans. Quart. J. Econom. 125(1):307–362.

Lin M, Prabhala NR, Viswanathan S (2013) Judging borrowers by the company they keep: Friendship networks and information asym metry in online peer-to-peer lending. Management Sci. 59(1):17–35.

Liu A, Jun L (2018) China’s peer-to-peer lenders are falling like dominoes as panic spreads. Bloomberg (July 20), https://www .bloomberg.com/news/articles/2018–07–20/china–s–p2p –platform–failures–surge–as–panic–spreads–in–market

Liu D, Brass D, Lu Y, Chen D (2015) Friendships in online peer-topeer lending: Pipes, prisms, and relational herding. Managemen Inform. Systems Quart. 39(3):729–742.

Marschak J, Radner R (1972) Economic Theory of Teams (Yale Uni versity Press, New Haven, CT).

Michels J (2012) Do unverifiable disclosures matter? evidence from peer-to-peer lending. Accounting Rev. 87(4):1385–1413.

Prendergast C (1993) A theory of “yes men”. Amer. Econom. Rev 83(4):757–770.

PYMNTS (2018) Protests mark china’s ruptured p2p lending land scape. PYMNTS (August 14), https://www.pymnts.com/news/ international/2018/china–protestors–p2p–lending–regulation -fraud-debt/.

Santomero AM (1984) Modeling the banking firm: A survey. J. Money Credit Banking 16(4):576–602

Scharfstein DS, Stein JC (1990) Herd behavior and investment. Amer. Econom. Rev. 80(3):465–479.

Shiller RJ (2015) Do crowdfunding rules ignore human nature? MarketWatch (November 18), http://www.marketwatch.com story/crowdfunding–or–crowdphishing–2015–11–18.

Simonsohn U, Ariely D (2008) When rational sellers face nonrational buyers: evidence from herding on ebay. Management Sci. 54(9): 1624–1637.

Statista (2019) Alternative lending report 2019. Statista (May), https:// www.statista.com/study/50625/fintech–report–alternative –lending/.

Sufi A (2007) Information asymmetry and financing arrangements: Evidence from syndicated loans. J. Finance 62(2):629–668.

Vallee B, Zeng Y (2019) Marketplace lending: a new banking paradigm? Rev. Financial Stud. 32(5):1939–1982.

Wei Z, Lin M (2016) Market mechanisms in online peer-to-pee lending. Management Sci. 63(12):4236–4257.

Xu JJ, Chau M (2018) Cheap talk? the impact of lender-borrower communication on peer-to-peer lending outcomes. J. Manage ment Inform. Systems 35(1):53–85.

Zhang J, Liu P (2012) Rational herding in microloan markets. Man agement Sci. 58(5):892–912

C<sub>opy</sub>ri<sub>g</sub>ht 202 1 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e p</sub>r<sub>ope</sub>rt<sub>y o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>express wr</sub>itt<sub>en perm</sub>i<sub>ss</sub>i<sub>on.</sub> H<sub>owever users may pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
