---
otero_id: 28364
otero_key: "H5BMZU2H"
title: "Coordination in Multibrand, Multimedia Advertising: Is It Always a Good Thing?"
authors: "Wangsheng Zhu; Subodha Kumar; Vijay Mookerjee"
year: "2024"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.0283"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Coordination in Multibrand, Multimedia Advertising: Is It Always a Good Thing?

Wangsheng Zhu,<sup>a</sup> Subodha Kumar,<sup>b,</sup>\* Vijay Mookerjee<sup>a</sup>

<sup>a</sup> Naveen Jindal School of Management, University of Texas at Dallas, Richardson, Texas 75080; <sup>b</sup> Fox School of Business, Temple University, Philadelphia, Pennsylvania 19122

Contact: wangsheng.zhu@utdallas.edu, https://orcid.org/0000-0002-4478-659X (WZ); subodha@temple.edu, https://orcid.org/0000-0002-4401-7950 (SK); vijaym@utdallas.edu, https://orcid.org/0000-0001-5583-3585 (VM)

Received: May 8, 2022 Revised: March 11, 2023; June 22, 2023 Accepted: July 1, 2023 Published Online in Articles in Advance: August 24, 2023

https://doi.org/10.1287/isre.2022.0283

Copyright: © 2023 INFORMS

Abstract. The growing online retail market has led to the prevalence of multichannel retail ing. Meanwhile, retailers are increasingly combining multichannel retailing with a multibranding strategy. Although this can further increase the retailer’s sales, it brings new advertising challenges. Multibrand, multichannel retailers usually launch advertising cam paigns for different brands on multiple media. Thus, the retailer’s advertising efforts fall into a set of brand-media units. Each unit’s advertising efforts can affect the sales of all brands on all channels. Therefore, retailers need to coordinate the advertising efforts of different units to maximize advertising efficiency in propelling sales. So far, the optimization problem of multibrand, multimedia advertising has not been analyzed in the literature, and our study aims to bridge this gap. We develop a stochastic differential equation model to estimate the impact of multimedia advertising on sales in a multibrand, multichannel context. Using the data from a jewelry retailer in the United States, we show that our model is effective in predicting future sales driven by advertising. Afterward, we formulate the advertising optimization problems under four coordination strategies: (i) noncoordination, (ii) brand coordination, (iii) media coordination, and (iv) global coordination. By solving the problem for each strategy, the retailers can obtain the optimal expenditure for each unit under that strategy. Finally, we compare the retailer’s profits under four strategies. Interestingly, we find that brand or media coordination may result in a profit lower than noncoordination. Our findings provide insights regard ing the selection of coordination strategies for multibrand, multichannel retailers with multimedia advertising campaigns, especially when they cannot do global coordination.

History: Ram Gopal, Senior Editor; Huaxia Rui, Associate Editor. Supplemental Material: The e-companion is available at https://doi.org/10.1287/isre.2022.0283.

Keywords: multibrand retailer • multichannel retailer • advertising optimization • advertising coordination • stochastic differential equation

## 1. Introduction

The online retailing market is proliferating. In the past years, U.S. online retail sales have maintained a 15% annual growth (Ali and Young 2021). The breakout of coronavirus disease 2019 has accelerated this process and boosted U.S. online retail sales to above \$210 billion per quarter in 2021 (U.S. Census Bureau 2021). Along with the growth of the e-commerce market, many offline retailers have launched online retail websites to boost their sales. Compared with a single channel, multichannel retailing can significantly increase sales. For example, Gap Inc. achieved \$2.5 billion in-store sales and \$1.5 billion e-commerce sales during the third quarter of fiscal 2021 (Gap Inc. 2021).

In addition to multichannel retailing, multibranding is another strategy commonly used by retailers to expand their business. Multibranding or the house-of-brands strategy refers to one company owning multiple independent brands (Junior 2018). Gap Inc. is a typical multibrand retailer with multiple brands, such as Gap and Old Navy (Gap Inc. 2021). These brands all belong to the clothing market, but each has a unique brand image. A diverse brand portfolio can help retailers accommodate the needs of different customers and serve a broader market. Retailers have also begun to combine multichannel retailing with multibranding. For example, H&M has so far established 10 brands and opened digital and physical stores for each brand (H&M 2020).

Although multibrand, multichannel retailing dramatically increases sales, it brings new marketing challenges. Along with the rising of multichannel retailing, firms started to deliver advertisements on multiple media. For instance, Gap spent more than \$2 billion in the past few years on their advertising campaigns across magazines, televisions, and digital platforms (Gap Inc. 2020). Com pared with their single-media counterparts, multimedia advertising campaigns may increase purchases significantly. According to a recent report (Square Inc. 2020), the purchase rate under multimedia advertising campaigns is 287% higher than single-media campaigns.

For a multibrand, multichannel retailer with multimedia advertising, both researchers and practitioners have found that advertising on any media for any brand can affect sales of all brands on all channels (e.g., Danaher et al. 2020). Because the advertising effects of different brand-media units are not isolated, the retailer faces the task of balancing advertising efforts across them to optimize total sales. Prior studies have examined the problems of either single-brand, multimedia advertising (e.g., Lesscher et al. 2020) or single-media, multibrand advertising (e.g., Choi and Liu 2019). Apart from in the work of Danaher et al. (2020), who empirically examined the impact of multimedia advertising in a multibrand, multichannel environment, optimal advertising strategies in this domain remain largely unexplored. We aim to bridge this important gap by studying a dynamic, structural model to evaluate various advertising strategies for multibrand, multichannel retailers with multimedia advertising. The main focus is the investigation of different coordination strategies to balance the advertising efforts across different brand-media units.

## 1.1. Motivation

To launch effective multimedia advertising campaigns, Nielsen (2020, para. 2) suggests that “a collaborative approach to balancing physical and digital advertising strategies is the key to unlocking omnichannel success.” Knowing the advertising returns is important for developing a balanced multimedia advertising plan. It was previously believed that advertising on one medium mainly boosts sales on its native channel (e.g., email advertising mainly drives the sales on the e-commerce website) (Dinner et al. 2014). Later, people started to highlight the effect of advertising on sales channels other than the native one (namely, the crosschannel salesboosting effect). For example, in 2019, the United States had 54 million shoppers who collected brand information on multiple media (Nielsen 2020). They may see advertisements on the online (offline) media yet purchase from offline (online) stores (Cui et al. 2021, Sun et al. 2022). Thus, the effect of advertising is not restricted to its native channel. For example, Osinga et al. (2019) find a 2% increase in offline sales after launching a mobile advertising campaign.

In addition to the crosschannel sales boost, there might be crosschannel cannibalization as well; that is, advertising on one medium could attract customers to migrate from other channels to the native channel. Thus, sales on other channels may decrease. For example, Ansari et al. (2008) find that email advertising can make customers switch their purchase channels from catalog to e-commerce websites. We call this phenomenon the crosschannel interference effect.

There is a considerable industry practice that focuses on measuring the crosschannel effect. For example, Google has developed tools that estimate the impact of TV advertising on online sales (Gleason 2018). Facebook offers a service that helps its enterprise customers to track how advertisements on Facebook affect their offline sales. With this service, Gina Tricot was able to eval uate the crosschannel effect, optimize its advertising efforts on different media in a synergistic manner, and increase the total advertising returns by 160% (Facebook 2019). These examples suggest that media coordination (MC), which refers to the task of balancing advertising efforts on different media based on both native-channel and crosschannel effects, is crucial to improve advertising performance.

As discussed earlier, in addition to multichannel retailing, multibranding is also commonly used by retailers. Although most multibrand retailers try to position their brands in different market segments, the target consumers of these brands often overlap (Franke 2019). For example, the brands in the portfolio of Gap Inc. have different design styles, but the main products of all brands are clothing. Thus, these brands have common customers (Safdar 2019). Because of the market overlap, the advertisements for different brands may reach the same customer group (Franke 2019).

There is plenty of evidence supporting that advertisements from one brand affect the sales of other brands. However, findings in extant studies are inconsistent. On the one hand, exposure to one brand’s advertisements can raise the customers’ awareness of the product category and stimulate their interest in other brands in the same category (Guitart et al. 2019). As a result, advertising by other brands increases the sales of the focal brand (Shapiro 2018). We refer to this effect as a crossbrand sales-boosting effect.

On the other hand, researchers also find a crossbrand interference effect; that is, the advertisements of other brands decrease the focal brand’s sales. For example, Danaher et al. (2020) find that one brand increasing its catalog advertising by 1% leads to a 3.5% drop in another brand’s offline sales. This is because different brands may advertise to the same customer because of overlapping consumer segments. Exposure to another brand’s advertisements may directly attract customers to switch from the focal brand to that brand. Besides, other brands’ advertisements may weaken a customer’s recall of the focal brand and indirectly make her leave the focal brand (Kim and Moon 2020).

Facing crossbrand sales boosts and interference, brand coordination (BC)—the task of allocating resources across brands based on their interactions—can help retailers enhance advertising returns. Bob Brown, the founder of Brown Analytics Advisory Group, suggests that brand coordination can help firms “leverage the data and dollars across all brands for more efficient marketing spend” (Franke 2019 para. 10). In practice, there are also firms, such as Lytho, that provide software for multibrand firms to coordinate advertising efforts across brands and improve marketing efficiency (Lehojarvi 2021).

As for retailers with multibrand, multimedia advertising campaigns, they need to coordinate the marketing activities on both brand and media dimensions to maximize advertising returns. For example, Foot Locker pays attention to the synergistic management of its online and offline activities (Zacks Equity Research 2021). It also uses Adobe Experience Cloud to centralize the activities of the brands in its portfolio (Blustein 2019). Motivated by such examples, we use the term “global coordination” (GC) to denote the task of coordinating marketing activities across all brand-media units.

Although global coordination can maximize advertising returns, not all retailers employ it when launching multibrand, multimedia advertising campaigns. For example, although the retailer H&M emphasizes integration across different channels and media, each brand uses a separate managing team for its marketing activities,<sup>1</sup> possibly implying a lack of brand coordination. Similarly, each brand of Gap Inc. has an independent team to plan marketing activities that are coordinated across media.<sup>2</sup> Because of differences in brand positioning, it is common to see multibrand retailers use separate teams to manage different brands. Because each team has its own operational style, this adds to the complexity of brand coordination. Some retailers may also choose not to coordinate brands in order to maintain the operational flexibility and creativity of each brand (Franke 2019).

Similarly, a brand may have independent teams to manage online and offline advertising. These teams may operate differently, making media coordination a challenging task (Cui et al. 2021). Besides, when designing coordinated marketing strategies, many retailers do not have a holistic picture of the returns of their multimedia advertising activities and struggle with the allocation of their advertising budget among different media (Nielsen 2021). This arises for various reasons, such as a lack of budget, a shortage of personnel who know how to enact coordination strategies, and a lack of models to measure the contribution of each media (McGee 2018, Cui et al. 2021).

Our research investigates the problem of multimedia advertising optimization for multibrand, multichannel retailers. We consider a retailer with two brands. Each brand uses two channels to sell and runs advertising campaigns on two types of media. We consider four strategies to coordinate advertising and investigate their impact on the retailer’s profit: (1) noncoordination (NC), (2) MC, (3) BC, and (4) GC.

## 1.2. Research Questions and Contributions

Although the benefit of coordination has been widely recognized, it is still challenging for many retailers to find optimal advertising expenditures under coordination (e.g., Nielsen 2021). Thus, we first investigate the following. For a multibrand, multichannel retailer with multimedia advertising campaigns, what is the optimal advertising expenditure of each brand-media unit under NC, MC, BC, and GC? To answer this question, we develop a stochastic differential equation (SDE) to model the evolution of each brand’s sales on each channel driven by advertising. We consider both crosschannel and crossbrand effects to capture the overall impact of advertising in a multibrand, multichannel, and multime dia context. With the data set from one of the largest U.S. jewelry retailers, we demonstrate how to use maximum likelihood estimation (MLE) to recover the parameters in the model.

To test the reliability of our model, we compare the predictive accuracy of our model with that of several benchmark models. The results show that our model achieves high accuracy in sales predictions relative to the benchmark, which lends support to the validity of our model. In addition to prediction accuracy, the key advantage of our model lies in that it is a structural model. Thus, it has the ability to do counterfactual anal ysis and prescribe the optimal advertising expenditures of different units under any coordination scenario. To demonstrate this, we formulate an optimization problem for each unit under each coordination strategy. By solving these problems, the retailer can determine the optimal advertising expenditures of different brandmedia units under each coordination scenario.

Our approach not only helps with the derivation of optimal advertising expenditures but also enables the evaluation of the retailer’s profit under each coordination strategy. This allows us to examine another set of questions.

• Which strategy is the best among NC, MC, and BC, and how do crosschannel and crossbrand advertising effects affect their performances?

• Although global coordination should clearly maximize the total profit, how do the performances of NC, MC, and BC fare relative to GC?

For retailers who are not able to implement global coordination, these questions are important for the selection of the coordination strategy. Besides, because prior studies mainly focus on single-media, multibrand o single-brand, multimedia advertising problems that only face a choice between NC and BC (or MC), the comparison among the four coordination strategies remains elu sive in the literature. Our case study sheds light on these questions by examining the retailer’s profits and comparing the performances of four coordination strategies under different (i) crossbrand interference magnitudes, (ii) crossbrand sales-boosting effectiveness, and (iii) crosschannel sales-boosting effectiveness.

Intuitively, taking either crosschannel or crossbrand effect into account leads to a more comprehensive understanding of the advertising impact compared with when only the same-brand native-channel effect is considered. Thus, one might expect that media or brand coordination can increase profit. Although this holds for single-media, multibrand or single-brand, multimedia advertising, interestingly, it may not be true for multibrand, multimedia advertising. For example, we find that BC may result in a profit lower than NC when the crosschannel sales-boosting effect is significant. Similarly, MC is also found to be inferior to NC when the crossbrand interference effect is significant. These findings imply that the wrong kind of coordination may be worse than no coordination.

Overall, our findings show that crosschannel and crossbrand effects profoundly influence the relative performances of NC, MC, and BC. This provides useful, practical implications regarding the selection of coordination strategy for multibrand, multichannel retailers, especially when they are unable or do not want to do the global coordination. For example, NC could be the optimal strategy among NC, BC, and MC under certain levels of crosschannel and crossbrand effects. Thus, the retailer does not need to waste money on building supportive infrastructures for BC or MC.

Our study contributes to the literature on the optimal advertising problem. To our knowledge, our study is among the first to develop a dynamic, structural model about how the sales of a multibrand, multichannel retailer evolve under multimedia advertising campaigns. More importantly, the contribution of our model lies in its ability to prescribe the optimal advertising expenditure of each brand-media unit and investigate the optimal coordination strategy facing different crosschannel and crossbrand effects. The next section further elaborates on our contributions with respect to the literature.

## 2. Literature Review

Our study has points of contact with the literature on (i) the impact of advertising on sales and (ii) advertising optimization and coordination. Although our study intersects with previous research on these domains, there are key differences between our work and extant studies.

## 2.1. Impact of Advertising on Sales

There is abundant literature that measures the impact of advertising on sales. Studies in this domain start with the impact of aggregated advertising efforts on a firm’s total sales (e.g., Assmus et al. 1984, Manchanda et al. 2006). Researchers have also developed more finegrained models to measure the advertising effect. These studies have examined (i) time dynamics of the advertising effect (e.g., Bass et al. 2007), (ii) crossbrand advertising effects in the presence of multiple brands (e.g., Danaher et al. 2008, Sahni 2016, Guitart et al. 2019), and (iii) crosschannel advertising effects in the multichannel and multimedia environment (e.g., Lewis and Reiley 2014, Lesscher et al. 2020).

Although the problem of single-brand, multimedia or single-media, multibrand advertising has received much attention, research is at a nascent stage regarding multibrand, multimedia advertising. To our knowledge, Danaher et al. (2020) is the first study in this area. Using the data set from a multibrand, multichannel retailer, they evaluate the advertising effectiveness across media, channels, and brands. Although our work also falls in this field, there are key differences between our work and their study.

First, in terms of research questions, Danaher et al. (2020) focus on estimating the advertising impact on sales. In contrast, our study goes beyond estimation work by also analyzing the optimal advertising strategy based on the estimations. Thus, our study has a prescriptive component in addition to a predictive component. Danaher et al. (2020) highlight that their findings provide evidence for the importance of brand coordination. However, they do not investigate how to optimize the advertising expenditures across brands as we do in this study.

Second, from a methodological perspective, Danaher et al. (2020) measure the advertising impact by a system of reduced-form regression models, whereas we use a structural, continuous-time stochastic diffusion equation. There is a long tradition of measuring the advertising effect by econometric models (Clarke 1973). These models estimate the advertising effect in a temporally (e.g., weekly) aggregated manner. Although these models have shown a good fit on the real-world data, it has been argued that temporal aggregations may introduce biases on the estimated advertising effects (Vanhonacker 1983). Hence, some studies advocate the use of continuous-time models to avoid such biases (Rao 1986). Although Danaher et al. (2020) extend the use of reduced-form regression models to multimedia advertising in a multibrand, multichannel environment, similar work has not been done on structural, continuous-time models. Our work contributes to the literature by addressing this gap.

## 2.2. Advertising Optimization and Coordination

Because a great amount of money is spent on advertising every year, optimizing the utilization of the advertising budget has received considerable attention. For example, Sethi (1983) analyzes the optimal advertising effort, as a response to the current sales, that maximizes a firm’s profit. Prasad and Sethi (2004) analyze the optimal advertising strategies of two firms in a duopoly market. Among the studies on advertising optimization, our work is closely related to those centering on (i) media coordination that balances the advertising expenditures on different media (e.g., Wang et al. 2018) and (ii) brand coordination that manages different brands advertising campaigns systematically to maximize the profit of the parent firm (e.g., Basu and Batra 1988, Choi and Liu 2019).

Although brand or media coordination has been explored in the literature, extant studies mainly focus on single-media, multibrand or single-brand, multimedia advertising optimization. In contrast, our study focuses on multimedia advertising campaigns in a multibrand, multichannel environment. In this case, global coordination is the optimal strategy to maximize the returns of advertising, which has not been investigated in the literature. Besides, because of the contexts of previous studies, only one of brand coordination and media coordination is meaningful to investigate in one study. On the contrary, in our study, the coexistence of crossbrand and crosschannel advertising effects raises new issues regarding the choice between brand coordination and media coordination.

## 3. Conceptual Framework

There are many multibrand, multichannel retailers in practice. For example, Foot Locker Inc. is a retailer with seven footwear brands, and each brand operates both digital and brick-and-mortar stores (Foot Locker Inc. 2021). All brands owned by Foot Locker Inc. focus on athletically inspired footwear and clothing, so their target customers overlap despite their different product designs. These brands advertise their products on a variety of media, including social media platforms, search engines, out-of-home billboards, and magazines. Motivated by such examples, we consider a scenario in which a firm runs two brands with overlapped market positioning. Each brand sells its products through two channels. To boost sales, each brand delivers ads on two types of media.

In our model, there are four (brands × media) advertising units that launch advertising campaigns on different media for different brands. We develop a two-stage framework to optimize advertising expenditures under different coordination scenarios. Figure 1 depicts this framework. In the first stage, we construct a model that captures the sales generation process and forecasts future sales given certain advertising expenditures. In the second stage, we formulate and solve an optimization problem to choose advertising spending based on the prediction model.

The marketing mix of a retailer may include advertising and promotion. Advertising refers to the content delivered on the media that aims to communicate brand information to potential customers and influence their attitudes toward the brand. Promotions are incentives that encourage customers to take certain actions toward the brand. Such incentives, like allowances and coupons, are additions to the basic benefits that customers can acquire from buying the product. Our focus is on optimizing advertising expenditures in this study.

Figure 1. Conceptual Framework  
![](/api/attachments/H5BMZU2H/fulltext/images/56515a963582e5a8ab7f39456dd4c8b2d9662ab5800214c709f6579a56bf1595.jpg)

3.1. Stage 1: Sales Generation Process Modeling To find the optimal advertising expenditures, we need to know how advertising affects sales. Advertising communicates brand information to customers, which may lead to a purchase (Danaher et al. 2020). Traditionally, advertising campaigns on one media are designed to boost sales on the native channel of this media; for example, email advertising is mainly used to increase orders via e-commerce websites (Dinner et al. 2014). Many studies have examined how advertising drives sales on the native channel, such as the effect of newspaper advertising on in-store sales (Yucelt and Kaynak 1984), search engine advertising on sales via paid search advertisements (Ghose and Yang 2009), etc. Without loss of generality, we assume that the native channel of media 0 (or 1) is channel 0 (or 1). The effect of advertising on its native channel is called the same-brand nativechannel effect (solid lines in Figure 1). After learning about a brand from one media, customers may use other channels to buy the product (Neslin et al. 2006), leading to the same-brand crosschannel effect (dotted lines in Figure 1). It is worth noting that the crosschannel effect may also decrease sales on other channels because seeing advertisements on one medium may make customers on other channels migrate to this medium’s native channel.

Advertising for one brand can also influence the sales of other brands. The literature has different results regarding the crossbrand effect. For example, Fischer et al. (2011) find a negative crossbrand effect, whereas Du et al. (2019) find a positive impact. The contradictory findings arise because advertising communicates not only brand information but also product category information. Danaher et al. (2020) find that crossbrand advertising effects exist at both native-channel and crosschannel levels. Figure 1 depicts these effects: crossbrand native-channel (dashed lines in Figure 1) and crossbrand crosschannel (dashed-dotted lines in Figure 1).

The first stage of our framework uses SDE to model the effect of advertising on sales. Such models have been widely adopted in both the analytical and empirical literature in different contexts, such as Sethi (1977), Prasad and Sethi (2004), Bass et al. (2005), and Yang et al. (2022). We develop our SDE framework by extending the Vidale–Wolfe model to the multibrand, multimedia, and multichannel context. The parameters in the model are estimated using MLE. The time-series analysis literature has proposed various models that can be used to predict sale, such as the autoregressive integrated moving average (ARIMA) model and the generalized autoregressive conditional heteroskedasticity (GARCH) model. Our SDE model differs from these reduced-form approaches in that it allows for the incorporation of different types of advertising effects and structurally captures the sales generation process. This is important to our study because we use this structural model to optimize advertising expenditures.

3.2. Stage 2: Optimization Model Construction Given a set of advertising expenditures, the prediction model trained in stage 1 forecasts the evolution of sales as well as the resulting profit. In stage 2, we formulate the problem of optimizing advertising expenditures to maximize profit. In the optimization stage of the problem, we assume that the parameters estimated in stage 1 are constants. This assumption is reasonable in a stable market environment where parameters tend to be relatively stable. If this assumption is not tenable, the retailer can use more recent data to estimate new parameter values. For example, Yang et al. (2022) suggests that parameters that are not constants can be reestimated from recent data before solving the optimization problem.

In the next section, we discuss the details of our predic tion model. After that, we present the optimization problems and discuss how to solve them by resorting to the Hamilton–Jacobi–Bellman (HJB) equation. Finally, we use a real-world case as an example to illustrate the implementation of our framework and demonstrate the implications regarding the selection of coordination strategies.

## 4. Model for Sales Generation Process

The goal of this section is to devise a model that captures the evolution of sales driven by advertising. As stated previously, we consider a retailer with two brands, and each brand has two sales channels and delivers advertisements on two media types. We denote the sales of brand i on channel j at time t by $x _ { i , j , t } ,$ where $i , j \in \{ 0 , 1 \}$ . Let $u _ { i , j , t }$ be the expenditure incurred by brand i for advertising on media j at time t. Finally, $c _ { j }$ is the unit advertising cost on media j.

We seek a prediction model for the sales of any brand i on any channel j. We develop the model in a forwardlooking manner. More formally, given the sales of brand i on channel j at time $\cdot ( \mathrm { i . e . , } x _ { i , j , t } )$ and four units’ advertising expenditures (i.e., $u _ { 0 , 0 , t } , u _ { 1 , 0 , t } , u _ { 0 , 1 , t } ,$ and $u _ { 1 , 1 , t } )$ , our model predicts the sales $( \mathrm { i . e . , ~ } x _ { i , j , t + d t } )$ at time $t \ + \ d t ,$ where dt is a short interval of time. Therefore, all advertising effects discussed subsequently refer to the impac of advertising on sales between time t and t + dt.

## 4.1. Same-Brand Native-Channel Advertising Effect

We first model the same-brand native-channel effect (i.e., the increase on $x _ { i , j , t }$ caused by $u _ { i , j , t } )$ . Before the widespread use of the internet, researchers had examined how different types of traditional advertising media affect sales on traditional channels, such as how print advertising and TV advertising drive in-store sales (e.g., Woodside and Waddle 1975, Tellis and Weiss 1995). Assmus et al. (1984) conducted a meta-analysis of the literature regarding the elasticity of sales to traditional media advertising. They find that the elasticity estimated in the literature is 0.22 on average. After the proliferation of online platforms, there is a growing interest in measuring the advertising effectiveness of various digital media. For example, Manchanda et al. (2006) analyzes the relationship between banner advertising and customers purchase probabilities on the e-commerce website. By examining the relationship between advertising and sales in a variety of industries, prior studies suggest that advertisements for brand i on media j can increase its sales on its native channel.

The same-brand native-channel effect depends on (i) the advertising expenditure $( \mathrm { i } . \mathrm { e } . , u _ { i , j , t } )$ and (ii) the current sales of brand i on channel $j \ ( \mathrm { i . e . } , x _ { i , j , t } )$ . A larger expenditure can lead to a larger sales increase, and this relationship is not linear (Little 1979). As the expenditure increases, there is a higher chance of showing ads to the same customer. Repetitive exposure can make customers bored and pay less attention to the ads (Bass et al. 2007, Todri et al. 2020). Thus, the marginal advertising effectiveness decreases as the expenditure increases. To reflect this diminishing marginal effect, we model the relation between the same-brand nativechannel effect and the advertising expenditure as $\alpha _ { i , j } \sqrt { u _ { i , j , t } / c _ { j } }$ , where $\alpha _ { i , j }$ is the unit sales-boosting effectiveness of $u _ { i , j , t }$ on $x _ { i , j , t }$

The same-brand native-channel effect is also affected by current sales of brand i (Vidale and Wolfe 1957). The remaining market for brand i decreases as its sales increase. The remaining market reflects the number of people who would potentially respond to the ad. Thus, the advertising effect decreases with sales (Seth 1983). On the other hand, as sales increase, customers generate more word-of-mouth (WOM) communication about brand i. This can enhance advertising effectiveness (Keller and Fay 2012, Deng et al. 2022). Such impact becomes more important as the growth of online communities makes information sharing easier (Hu et al. 2019, Liu et al. 2020, Pu et al. 2020, Dong et al. 2022).

Let $M _ { i , j }$ be the maximum sales that can be potentially achieved for brand i on channel j. We use $\sqrt { M _ { i , j } - x _ { i , j , t } }$ to model the relation between the same-brand nativechannel effect and current sales. As $x _ { i , j , t }$ increases, the same-brand native-channel effect decreases, but the conversion rate of potential customers $( \mathrm { i . e . , }$ $\sqrt { M _ { i , j } - x _ { i , j , t } } / ( M _ { i , j } - x _ { i , j , t } ) )$ is larger because of WOM. Taking the impacts of the expenditure and current sales together, the same-brand native-channel effect is modeled as $\alpha _ { i , j } \sqrt { ( M _ { i , j } - x _ { i , j , t } ) u _ { i , j , t } / c _ { j } }$

## 4.2. Same-Brand Crosschannel Advertising Effect

Although it was previously thought that advertising media primarily influenced its native channel $( \mathrm { e . g . , }$ Ansari et al. 2008, Wiesel et al. 2011), researchers have found significant crosschannel advertising effects $( \mathrm { e . g . }$

Lewis and Reiley 2014). Naik and Peters (2009) were among the first to measure advertising effects in a multichannel context. Using the data from a car company, they find that banner advertising substantially increases customers’ visits to dealers’ offline showrooms. Wiesel et al. (2011) find that $7 3 \%$ of the benefits generated by Google AdWords are from the increase in orders via telephone, mail, and store visits and that 20% of the benefits created by printed flyers come from increased sales on websites. Motivated by such studies, we next model the same-brand crosschannel effect (i.e., the impact of advertising on media $1 - j \ ( \mathrm { i . e . , \ } u _ { i , 1 - j , t } )$ on the sales of channel $j \left( \mathrm { i . e . , } x _ { i , j , t } \right) )$

The crosschannel effects are closely related to the fact that customers may use multiple media to gather product information (Neslin et al. 2006). Thus, they may purchase the product through a channel that is nonnative to the media where they learned about the brand (Neslin et al. 2006). Except for the separation between the purchase channel and information-gathering media, the same-brand crosschannel effect has the same underlying mechanism as the native-channel effect. Both of them increase $x _ { i , j , t }$ by communicating brand information to customers (Wiesel et al. 2011). Similar to the same-brand native-channel effect, the same-brand crosschannel effect is modeled as $\beta _ { i , j } \sqrt { ( M _ { i , j } - x _ { i , j , t } ) u _ { i , 1 - j , t } / c _ { 1 - j } } ,$ , where $\beta _ { i , j }$ is the unit sales-boosting effectiveness of ${ u } _ { i , 1 - j , t } \mathrm { o n } x _ { i , j , t }$

In addition to crosschannel sales boosts, studies on multichannel retailers also suggest the possibility of channel cannibalization (Forman et al. 2009). Customers on channel j may migrate to channel $1 - j .$ In this case, channel $1 - j$ cannibalizes the sales of channel j. Besides, exposure to advertising on another channel may acceler ate customers’ memory loss about the focal channel, resulting in a sales decrease on the channel. For example, Ansari et al. (2008) find that email advertising lowers the likelihood of customers purchasing via catalogs. Koll mann et al. (2012) find that customers’ channel selection is related to the source where they are informed about the brand. We call the negative impact of $u _ { i , 1 - j , t } \mathrm { o n } x _ { i , j , t }$ the same-brand crosschannel interference effect.

The crosschannel interference effect depends on the magnitudes of $u _ { i , 1 - j , t }$ and $x _ { i , j , t } . \ A s \ u _ { i , 1 - j , i }$ increases, the cannibalization effect can cause a larger decrease in $x _ { i , j , t }$ (Ansari et al. 2008). Similar to the same-channel effect, a larger advertising amount increases the chance of repetitively advertising to the same customer. Repetitions cause customers to lose interest in the advertisement (Bass et al. 2007). As a result, the marginal cannibalization effect decreases progressively as $u _ { i , 1 - j , t }$ increases. Thus, we include $- \varsigma _ { i , j } \sqrt { u _ { i , 1 - j , t } / c _ { 1 - j } }$ in the formulation of the same-brand crosschannel interference effect where $\varsigma _ { i , j }$ is the unit cannibalization of $u _ { i , 1 - j , t }$ on $x _ { i , j , t }$

The cannibalization effect is also affected by current sales of brand i on channel $j .$ If channel j has no sales, advertising on media 1 � j cannot reduce its sales. As the sales increase, the cannibalization effect can cause a larger decrease in $x _ { i , j , t }$ (Sahni 2016). Besides, higher sales on channel j can lead to the scale advantage and increase the operational efficiency on this channel (Tagashira and Minami 2019). Better operations on channel j can enhance customer experience and improve customer loyalty to the channel. Thus, the marginal impact of $x _ { i , j , t }$ on the crosschannel interference effect decreases. Combining these findings with the discussion on $u _ { i , 1 - j , t . }$ , we model the same-brand crosschannel interference effect $\mathbf { a s } - \varsigma _ { i , j } \sqrt { x _ { i , j , t } ( u _ { i , 1 - j , t } / c _ { 1 - j } } )$

In addition to the exposure to different media, the literature also suggests that different shopping experiences between channels can drive channel migration (Shriver and Bollinger 2022). For example, customers may switch channels because of different consultation service qualities across channels (Kollmann et al. 2012) and exclusive price promotions on a channel (Breugelmans and Campo 2016). However, this cannibalization effect does not relate to advertising expenditures. Because this section discusses advertising effects, our discussion so far focuses on advertising-induced cannibalization. Section 4.4 discusses how our model accounts for cannibalization caused by the differences between different channels’ shopping experiences.

## 4.3. Crossbrand (Native-Channel and Crosschannel) Advertising Effect

The sales of brand i are affected not only by its own advertising efforts but also by the advertising of brand 1 � i. Danaher et al. (2020) show that there are both crossbrand native-channel and crossbrand crosschannel advertising effects. We start with the crossbrand nativechannel effect $( \mathrm { i . e . } ,$ , the impact of $u _ { 1 - i , j , t }$ on $x _ { i , j , t } )$ . Prior studies indicate that competitive advertising can reduce the focal brand’s sales $( \mathrm { e . g . }$ , Danaher et al. 2008, Dinner et al. 2014). Fischer et al. (2011) find a negative relationship between a brand’s sales and its competitors’ advertising efforts in two pharmaceutical product categories. Danaher et al. (2020) find that one brand’s email advertising can reduce online sales of other brands. We call this negative impact the crossbrand native-channel interference effect.

There are two causes for crossbrand interference. Brands use advertising to compete for customers. Advertisements from brand 1 � i may stimulate customers interest in this brand. Thus, customers who would have purchased products from brand i may switch to brand $1 - i$ (Guitart et al. 2019). Besides, the advertising of brand 1 � i may weaken a customer’s recalls of brand i (Danaher et al. 2008). Naturally, a customer’s memory of one brand diminishes over time. Aside from time passage, prior studies show that advertisements from competing brands can hasten memory loss (McGeoch 1932). Therefore, in addition to directly driving customers away from brand $i ,$ the advertising of brand 1 � i may cause them to forget brand i more quickly, thereby indirectly lowering its sales.

Similar to the crosschannel interference effect, the crossbrand native-channel interference effect also depends on the magnitudes of $u _ { 1 - i , j , t }$ and $x _ { i , j , t }$ . An increase in $u _ { 1 - i , j , t }$ can lead to a more significant interference effect (Fischer et al. 2011, Danaher et al. 2020). Besides, similar to the same-brand effect, the marginal interference effect de creases with $u _ { i , 1 - j , t }$ because of the repetitive advertising. Thus, we include $- \gamma _ { i , j } \sqrt { u _ { 1 - i , j , t } / c _ { j } }$ in the formulation of the crossbrand native-channel interference effect, where $\gamma _ { i , j }$ is the unit interference of ${ u } _ { 1 - i , j , t } \mathrm { o n } x _ { i , j , t }$

As for the relationship between the interference effect and $x _ { i , j , t } ,$ , Sahni (2016) suggests that the magnitude of the interference effect increases with $x _ { i , j , t }$ . Besides, as brand i has more sales, customer loyalty becomes higher because of the increased WOM communications (Gauri et al. 2008, Garnefeld et al. 2011). Thus, customers of brand i are less sensitive to the advertising of brand $1 - i .$ Therefore, we model the crossbrand native-channel interference effect as $- \gamma _ { i , j } \sqrt { x _ { i , j , t } ( u _ { 1 - i , j , t } / c _ { j } ) }$ . Brand i loses more sales because of the interference effect as $x _ { i , j , t }$ increases, but the customer turnover rate $( \mathrm { i . e . , ~ } - \gamma _ { i , j }$ $\sqrt { u _ { 1 - i , j , t } / ( c _ { j } x _ { i , j , t } ) } )$ diminishes progressively with $x _ { i , j , t }$ because of WOM.

Although the advertising of brand 1 � i helps customers learn about brand $1 - i ,$ it may also arouse their interest in the product category. Driven by such interests, customers may search for similar brands and eventually make purchases from brand i (Guitart et al. 2019). Thus, the advertis ing of brand 1 � i may attract new customers for brand i. For example, Danaher et al. (2008) find that one brand’s sales may be assisted by its competitors’ advertising. Sahni (2016) finds that advertising may remind customers of brands not appearing in the ad and increase the sales of these brands. Du et al. (2019) show that TV advertising by competitors can increase online searches for the focal brand. We refer to this positive effect as the crossbrand native-channel sales-boosting effect. This effect is modeled similarly to the same-brand native-channel sales-boosting effect: that is, $\phi _ { i , j } \sqrt { ( M _ { i , j } - x _ { i , j , t } ) u _ { 1 - i , j , t } / c _ { j } } ,$ where $\phi _ { i , j }$ is the unit sales-boosting effectiveness of $u _ { 1 - i , j , t } \mathrm { o n } x _ { i , j , t }$

To summarize, the crossbrand native-channel advertising effect $( \mathrm { i . e . , }$ , the effect of $u _ { 1 - i , j , t } \mathrm { o n } x _ { i , j , t } )$ consists of two opposite effects—crossbrand native-channel sales boosts and interference. Similar to $u _ { 1 - i , j , t . }$ , advertising of brand $1 - i$ on media $1 - j \ : ( \mathrm { i . e . , } \ : u _ { 1 - i , 1 - j , t } )$ also generates sales boosts and interference on $x _ { i , j , t }$ because customers may learn about brand information or product category information on media 1�j but make purchases on channel j (Kollmann et al. 2012). The crossbrand, crosschannel interference is modeled as $- \lambda _ { i , j } \sqrt { x _ { i , j , t } ( u _ { 1 - i , 1 - j , t } / c _ { 1 - j } ) } ,$ where $\lambda _ { i , j }$ is the unit interference of $u _ { 1 - i , 1 - j , t }$ on $x _ { i , j , t } .$ The crossbrand crosschannel sales-boosting effect is modeled as $\psi _ { i , j } { \sqrt { ( M _ { i , j } - x _ { i , j , t } ) u _ { 1 - i , 1 - j , t } / c _ { 1 - j } } } ,$ where $\psi _ { i , j }$ is the unit sales-boosting effectiveness of $u _ { 1 - i , 1 - j , t }$ on $x _ { i , j , t }$

## 4.4. Model Description

To model the evolution of sales, we consider a simplified microstructure—the instantaneous change of sales $( \mathrm { i . e . , }$ $d x _ { i , j , t } )$ within a short time interval from t to $t + d t .$ . As mentioned, the sales of brand i on channel j are affected by same-brand and crossbrand advertising effects in both native-channel and crosschannel manners. Table 1 summarizes the advertising effects discussed previously.

In addition to advertising, there are other factors that affect sales, such as product obsolescence and variety seeking of customers (Prasad and Sethi 2004). As mentioned, even without competitive advertising, the passage of time diminishes customers’ memories of one brand, which may decrease the sales (Danaher et al. 2008). Experience-induced channel cannibalization is another nonadvertising factor that may influence sales.

Ansari et al. (2008) find that offline customers migrated to online channels during 1998–2002, and this trend is independent of the advertising impact. Vidale and Wolfe (1957) empirically show that the aggregated impact of nonadvertising factors can be captured as a decay term, $- \delta _ { i , j } x _ { i , j , t . }$ , where $\delta _ { i , j }$ is the decay rate. We use $\mu _ { i , j }$ to denote the total impact of advertising and other factors on the sales $x _ { i , j , t } { : } ^ { 3 }$

$$
\begin{array}{l} \mu_ {i, j} (u _ {i, j, t}, u _ {1 - i, j, t}, u _ {i, 1 - j, t}, u _ {1 - i, 1 - j, t}) \\ = \left(\alpha_ {i, j} \sqrt {\frac {u _ {i , j , t}}{c _ {j}}} + \beta_ {i, j} \sqrt {\frac {u _ {i , 1 - j , t}}{c _ {1 - j}}} + \phi_ {i, j} \sqrt {\frac {u _ {1 - i , j , t}}{c _ {j}}} \right. \\ \left. + \psi_ {i, j} \sqrt {\frac {u _ {1 - i , 1 - j , t}}{c _ {1 - j}}}\right) \sqrt {M _ {i , j} - x _ {i , j , t}} - \left(\varsigma_ {i, j} \sqrt {\frac {u _ {i , 1 - j , t}}{c _ {1 - j}}} \right. \\ \left. + \gamma_ {i, j} \sqrt {\frac {u _ {1 - i , j , t}}{c _ {j}}} + \lambda_ {i, j} \sqrt {\frac {u _ {1 - i , 1 - j , t}}{c _ {1 - j}}}\right) \sqrt {x _ {i , j , t}} - \delta_ {i, j} x _ {i, j, t}. \end{array}\tag{1}
$$

In addition to the factors, sales are also affected by the inherent randomness of the market environment (Prasad and Sethi 2004). A stochastic term $( \mathrm { i . e . , ~ } \sigma _ { i , j } \sqrt { x _ { i , j , t } } d w _ { i , j , t } )$ is used to reflect the randomness in the sales evolution. $d w _ { i , j , t } \sim \mathcal { N } ( 0 , d t )$ is the Wiener process. $\sigma _ { i , j }$ affects the magnitude of the randomness. $\sqrt { x _ { i , j , t } }$ is commonly used to avoid the sales that ${ } ^ { \mathrm { g o } }$ to below zero because of the randomness because the variance of $\sigma _ { i , j } \sqrt { x _ { i , j , t } } d w _ { i , j , t }$ vanishes as the state approaches zero. Table 2 summarizes the notations and variables. In a nutshell, the change of $x _ { i , j , t }$ from t to $t + d t \left( \mathrm { i . e . , } d x _ { i , j , t } \right)$ consists of a deterministic component and a stochastic component:

Table 1. Advertising Effects on the Sales $x _ { i , j , t }$

<table><tr><td></td><td>Native-channel</td><td>Crosschannel</td></tr><tr><td>Same-brand</td><td>Sales-boosting effect $\alpha_{i,j} \sqrt{\frac{u_{i,j,t}}{c_j}} \sqrt{M_{i,j} - x_{i,j,t}}$ Source. Brand information dissemination by  $u_{i,j,t}$ .</td><td>Sales-boosting effect $\beta_{i,j} \sqrt{\frac{u_{i,1-j,t}}{c_{1-j}}} \sqrt{M_{i,j} - x_{i,j,t}}$ Source. (1) Brand information dissemination by  $u_{i,1-j,t}$ .(2) Separation between information-gathering media and purchase channels used by customers.Interference effect $-\varsigma_{i,j} \sqrt{\frac{u_{i,1-j,t}}{c_{1-j}}} \sqrt{x_{i,j,t}}$ </td></tr><tr><td>Crossbrand</td><td>Sales-boosting effect $\phi_{i,j} \sqrt{\frac{u_{1-i,j,t}}{c_j}} \sqrt{M_{i,j} - x_{i,j,t}}$ Source. Product category information dissemination by  $u_{1-i,j,t}$ .Interference effect $-\gamma_{i,j} \sqrt{\frac{u_{1-i,j,t}}{c_j}} \sqrt{x_{i,j,t}}$ Source. Customers&#x27; brand switching and accelerated memory loss caused by  $u_{1-i,j,t}$ .</td><td>Source. Channel migration and accelerated memory loss about channel  $j$  caused by  $u_{i,1-j,t}$ .Sales-boosting effect $\psi_{i,j} \sqrt{\frac{u_{1-i,1-j,t}}{c_{1-j}}} \sqrt{M_{i,j} - x_{i,j,t}}$ Source. (1) Product category information dissemination by  $u_{1-i,1-j,t}$ . (2) Separation between information-gathering media and purchase channels used by customers.Interference effect $-\lambda_{i,j} \sqrt{\frac{u_{1-i,1-j,t}}{c_{1-j}}} \sqrt{x_{i,j,t}}$ Source. (1) Customers&#x27; brand switching and accelerated memory loss caused by  $u_{1-i,1-j,t}$ . (2) Separation between information-gathering media and purchase channels used by customers.</td></tr></table>

Table 2. Key Notations and Variables

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td>i</td><td>Index of brand, i ∈ {0,1}</td></tr><tr><td>j</td><td>Index of channel/media, j ∈ {0,1}</td></tr><tr><td>t</td><td>Index of time</td></tr><tr><td colspan="2">Variables</td></tr><tr><td>x</td><td>Sales</td></tr><tr><td>u</td><td>Advertising expenditure</td></tr><tr><td>dx</td><td>Instantaneous change of sales</td></tr><tr><td>μ</td><td>Deterministic component of dx, μ = E[dx]</td></tr><tr><td>dw</td><td>Wiener process</td></tr><tr><td colspan="2">Parameters</td></tr><tr><td>c</td><td>Unit advertising cost</td></tr><tr><td>α</td><td>Same-brand native-channel sales-boosting effectiveness</td></tr><tr><td>β</td><td>Same-brand crosschannel sales-boosting effectiveness</td></tr><tr><td>s</td><td>Same-brand crosschannel interference parameter</td></tr><tr><td>φ</td><td>Crossbrand native-channel sales-boosting effectiveness</td></tr><tr><td>ψ</td><td>Crossbrand crosschannel sales-boosting effectiveness</td></tr><tr><td>γ</td><td>Crossbrand native-channel interference parameter</td></tr><tr><td>λ</td><td>Crossbrand crosschannel interference parameter</td></tr><tr><td>M</td><td>Market size</td></tr><tr><td>δ</td><td>Nonadvertising decay rate</td></tr><tr><td>σ</td><td>Magnitude of the stochastic component</td></tr></table>

$$
d x _ {i, j, t} = \mu_ {i, j} d t + \sigma_ {i, j} \sqrt {x _ {i , j , t}} d w _ {i, j, t}.\tag{2}
$$

## 5. Optimization Problems

With the prediction model, we now turn to the model of optimizing advertising expenditures. There are four advertising units. They may make decisions separately. For example, brand i may select the advertising efforts to drive its own sales without considering brand $1 - i$ (Basu and Batra 1988). Online (offline) units may select advertising expenditures that aim to maximize sales on the native channel (Dinner et al. 2014). The retailers may also bring some units together to make joint decisions. In this section, we discuss the advertising optimization problems under different decision scenarios.

## 5.1. Problem Formulations Under Different Coordination Scenarios

Table 3 presents how advertising expenditures are decided under NC, MC, BC, and GC.

5.1.1. Noncoordination. Without coordination, unit $( i , j )$ tries to maximize the profit of brand i on channel j. Let $\pi _ { i , j }$ be the profit margin of brand i on channel j. It is the average profit brand i gains from each dollar of sales on channel j after deducting nonadvertising costs. Following past studies (e.g., Sethi 1983), we write the objective of unit $( i , j )$ as one of maximizing the timediscounted total profit over an infinite horizon. With a time-discounting rate $\rho ,$ the objective is given by

$$
\max _ {u _ {i, j, t}} E \left[ \int_ {0} ^ {\infty} e ^ {- \rho t} \left(\pi_ {i, j} x _ {i, j, t} - u _ {i, j, t}\right) d t \right].\tag{3}
$$

Because $x _ { i , j , t }$ is affected by the advertising of other units, the optimal $u _ { i , j , t }$ is associated with $u _ { i , 1 - j , t } , u _ { 1 - i , j , t }$ and $u _ { 1 - i , 1 - j , t }$ . However, under NC, a unit makes decisions without knowing other units’ decisions. Such a problem is often characterized by a game-theoretic model where multiple players make decisions in a noncooperative manner when their payoffs are affected by others’ actions. This model is usually too complicated to manage in practice, and executives hardly use it to make decisions (Coyne and Horn 2009). Instead, units may guess others’ actions and use the guesses to make decisions. We examine this idea in our study.

Suppose that unit $( i , j )$ guesses that the expenditure of unit $( i ^ { \prime } , j ^ { \prime } ) \ _ { . } ( \mathrm { i . e . , } \ u _ { i ^ { \prime } , j ^ { \prime } , t } )$ is $\stackrel { i , j } { e _ { i ^ { \prime } , j ^ { \prime } } ^ { i , j } }$ where $( i ^ { \prime } , j ^ { \prime } ) { \overset { \cdot } { = } } ( i , j ) . ^ { 4 }$ For example, $e _ { i ^ { \prime } , j ^ { \prime } } ^ { i , j }$ can be the average historical expenditure of unit $( i ^ { \prime } , j ^ { \prime } )$ . As a robustness check for this constant guess assumption, in the e-companion (Section EC.5), we use our data set to test a model where each unit dynamically updates its guess based on the theory of reference effects (Coulter and Krishnamoorthy 2014, Zhang et al. 2014, Kirshner and Ovchinnikov 2019). We do not find evidence that the units in our data set dynamically update their guesses. Under the constant guess assumption, the problem of unit $( i , j )$ under NC is given by

$$
\max _ {u _ {i, j, t}} E \left[ \int_ {0} ^ {\infty} e ^ {- \rho t} (\pi_ {i, j} x _ {i, j, t} - u _ {i, j, t}) d t \right]\tag{Problem NC}
$$

subject to

$$
d x _ {i, j, t} = \mu_ {i, j} (u _ {i, j, t}, e _ {1 - i, j} ^ {i, j}, e _ {i, 1 - j} ^ {i, j}, e _ {1 - i, 1 - j} ^ {i, j}) d t + \sigma_ {i, j} \sqrt {x _ {i , j , t}} d w _ {i, j, t}.\tag{4}
$$

We next solve the optimal control problem for the optimal advertising expenditure.

Table 3. Coordination Scenarios

<table><tr><td>Scenario</td><td>Description</td></tr><tr><td>Noncoordination</td><td>Unit (i, j) makes decisions to maximize the sales of brand i on the native channel j</td></tr><tr><td>Media coordination</td><td>Two units of brand i make joint decisions to maximize the total sales of brand i considering the same-brand crosschannel effect</td></tr><tr><td>Brand coordination</td><td>Two units that deliver ads on media j make joint decisions to maximize the total sales on channel j considering crossbrand native-channel effects</td></tr><tr><td>Global coordination</td><td>Four units make joint decisions to maximize the retailer&#x27;s profit considering both crossbrand and crosschannel effects</td></tr></table>

Proposition 1. The optimal advertising expenditure in Problem NC, denoted by $u _ { i , j , t } ^ { N C } ,$ , is

$$
u _ {i, j, t} ^ {N C} = \frac {\alpha_ {i , j} ^ {2} (V _ {x} ^ {N C}) ^ {2} (M _ {i , j} - x _ {i , j , t})}{4 c _ {j}},\tag{5}
$$

where $V _ { x } ^ { N C }$ is the solution to the following HJB equation:

$$
\begin{array}{l} \rho V ^ {N C} - \pi_ {i, j} x _ {i, j, t} + u _ {i, j, t} ^ {N C} = V _ {x} ^ {N C} \mu_ {i, j} (u _ {i, j, t} ^ {N C}, e _ {1 - i, j} ^ {i, j}, e _ {i, 1 - j} ^ {i, j}, e _ {1 - i, 1 - j} ^ {i, j}) \\ \qquad + \frac {1}{2} \sigma_ {i, j} ^ {2} x _ {i, j, t} V _ {x x} ^ {N C}. \end{array} \tag {6}
$$

Proof. All proofs are provided in Section EC.2 in the e-companion. w

The HJB equation is a differential equation that does not lend itself to a closed-form solution. Thus, we solve it numerically. After that, we substitute the numerical solution to $V _ { x } ^ { \breve { N } C }$ into $u _ { i , j , t } ^ { N C }$ and obtain the numerical value of $u _ { i , j , t } ^ { N C }$

5.1.2. Media Coordination. In this case, two units of brand i make decisions together to maximize their total profit. Units (i, 0) and (i, 1) need to guess the expenditures of brand 1 � i. Suppose that they guess $e _ { 1 - i , j } ^ { i }$ for $u _ { 1 - i , j , t }$ . The problem of brand i is given by

$$
\max _ {u _ {i, 0, t}, u _ {i, 1, t}} E \left[ \int_ {0} ^ {\infty} e ^ {- \rho t} (\pi_ {i, 0} x _ {i, 0, t} - u _ {i, 0, t} + \pi_ {i, 1} x _ {i, 1, t} - u _ {i, 1, t}) d t \right]
$$

(Problem MC)

subject to

$$
\begin{array}{c} d x _ {i, j, t} = \mu_ {i, j} (u _ {i, j, t}, e _ {1 - i, j} ^ {i}, u _ {i, 1 - j, t}, e _ {1 - i, 1 - j} ^ {i}) d t \\ + \sigma_ {i, j} \sqrt {x _ {i , j , t}} d w _ {i, j, t} \text {for} j = 0, 1. \end{array}\tag{7}
$$

Similar to the previous scenario, we can solve the optimal control problem under MC by resorting to the HJB equation. We state the result in the following proposition.

Proposition 2. The optimal advertising expenditure in Problem MC, denoted by $u _ { i , j , t } ^ { M C } ,$ is

$$
u _ {i, j, t} ^ {M C} = \frac {1}{4 c _ {j}} \left(V _ {x _ {i, j, t}} ^ {M C} \alpha_ {i, j} \sqrt {M _ {i , j} - x _ {i , j , t}} + V _ {x _ {i, 1 - j, t}} ^ {M C} B _ {1}\right) ^ {2},\tag{8}
$$

where $B _ { 1 } = ( \beta _ { i , 1 - j } \sqrt { M _ { i , 1 - j } - x _ { i , 1 - j , t } } - \zeta _ { i , 1 - j } \sqrt { x _ { i , 1 - j , t } } )$ and $V _ { x } ^ { M C }$ is the solution to the HJB equation:

$$
\begin{array}{r l} \rho V ^ {M C} = & \sum_ {j = 0} ^ {1} (\pi_ {i, j} x _ {i, j, t} - u _ {i, j, t} ^ {M C}) \\ & + \sum_ {j = 0} ^ {1} V _ {x _ {i, j, t}} ^ {M C} \mu_ {i, j} (u _ {i, j, t} ^ {M C}, e _ {1 - i, j} ^ {i}, u _ {i, 1 - j, t} ^ {M C}, e _ {1 - i, 1 - j} ^ {i}) \\ & + \sum_ {j = 0} ^ {1} \sum_ {k = 0} ^ {1} \frac {\partial^ {2} V ^ {M C}}{2 \partial x _ {i , j , t} \partial x _ {i , k , t}} \sigma_ {i, j, t} \sigma_ {i, k, t} \sqrt {x _ {i , j , t} x _ {i , k , t}} \end{array}\tag{9}
$$

5.1.3. Brand Coordination. Under BC, units $( 0 , j )$ and $( 1 , j )$ decide their expenditures together and maximize their total profit. Because they are not coordinated with the units responsible for advertising on media $1 - j ,$ they guess $e _ { i , 1 - j } ^ { j }$ for $u _ { i , 1 - j , t }$ . The problem of units $( 0 , j )$ and $( 1 , j )$ is given by

$$
\max _ {u _ {0, j, t}, u _ {1, j, t}} E \left[ \int_ {0} ^ {\infty} e ^ {- \rho t} (\pi_ {0, j} x _ {0, j, t} - u _ {0, j, t} + \pi_ {1, j} x _ {1, j, t} - u _ {1, j, t}) d t \right]
$$

(Problem BC)

subject to

$$
\begin{array}{c} d x _ {i, j, t} = \mu_ {i, j} (u _ {i, j, t}, u _ {1 - i, j, t}, e _ {i, 1 - j} ^ {j}, e _ {1 - i, 1 - j} ^ {j}) d t \\ + \sigma_ {i, j} \sqrt {x _ {i , j , t}} d w _ {i, j, t} \text {for} i = 0, 1. \end{array}\tag{10}
$$

The following proposition characterizes the optimal advertising decision in Problem MC.

Proposition 3. The optimal advertising expenditure in Problem BC, denoted by $u _ { i , j , t } ^ { B C } ,$ is

$$
u _ {i, j, t} ^ {B C} = \frac {1}{4 c _ {j}} \Big (V _ {x _ {i, j, t}} ^ {B C} \alpha_ {i, j} \sqrt {M _ {i , j} - x _ {i , j , t}} + V _ {x _ {1 - i, j, t}} ^ {B C} B _ {2} \Big) ^ {2},\tag{11}
$$

where $B _ { 2 } = \phi _ { 1 - i , j } \sqrt { M _ { 1 - i , j } - x _ { 1 - i , j , t } } - \gamma _ { 1 - i , j } \sqrt { x _ { 1 - i , j , t } }$ and $V _ { x } ^ { B C }$ is the solution to the HJB equation:

$$
\begin{array}{l} \rho V ^ {B C} = \sum_ {i = 0} ^ {1} (\pi_ {i, j} x _ {i, j, t} - u _ {i, j, t} ^ {B C}) \\ \qquad + \sum_ {i = 0} ^ {1} V _ {x _ {i, j, t}} ^ {B C} \mu_ {i, j} (u _ {i, j, t} ^ {B C}, u _ {1 - i, j, t} ^ {B C}, e _ {i, 1 - j} ^ {j}, e _ {1 - i, 1 - j} ^ {j}) \\ \qquad + \sum_ {i = 0} ^ {1} \sum_ {k = 0} ^ {1} \frac {\partial^ {2} V ^ {B C}}{2 \partial x _ {i , j , t} \partial x _ {k , j , t}} \sigma_ {i, j, t} \sigma_ {k, j, t} \sqrt {x _ {i , j , t} x _ {k , j , t}} \end{array}\tag{12}
$$

5.1.4. Global Coordination. In global coordination, four units cooperate to decide the advertising efforts so that the profit of the parent firm is maximized. The optimiza tion problem, in this case, is formulated as follows:

$$
\max _ {u _ {i, j, t}} E \left[ \int_ {t = 0} ^ {\infty} \sum_ {i = 0} ^ {1} \sum_ {j = 0} ^ {1} e ^ {- \rho t} (\pi_ {i, j} x _ {i, j, t} - u _ {i, j, t}) d t \right]
$$

(Problem GC)

subject to

$$
\begin{array}{l} d x _ {i, j, t} = \mu_ {i, j} (u _ {i, j, t}, u _ {1 - i, j, t}, u _ {i, 1 - j, t}, u _ {1 - i, 1 - j, t}) d t \\ \qquad + \sigma_ {i, j} \sqrt {x _ {i , j , t}} d w _ {i, j, t}, \text {   for   } i, j \in \{0, 1 \}. \end{array}\tag{13}
$$

The following proposition characterizes the optimal advertising decision in Problem GC.

Proposition 4. The optimal advertising expenditure in Problem GC, denoted by $u _ { i , j , t } ^ { G C } ,$ , is

$$
\begin{array}{l} u _ {i, j, t} ^ {G C} = \frac {1}{4 c _ {j}} \left(V _ {x _ {i, j, t}} ^ {G C} \alpha_ {i, j} \sqrt {M _ {i , j} - x _ {i , j , t}} + V _ {x _ {i, 1 - j, t}} ^ {G C} B _ {1} + V _ {x _ {1 - i, j, t}} ^ {G C} B _ {2} \right. \\ \left. + V _ {x _ {1 - i, 1 - j, t}} ^ {G C} B _ {3}\right) ^ {2}, \end{array} \tag {14}
$$

where $B _ { 3 } = \psi _ { 1 - i , 1 - j } \sqrt { M _ { 1 - i , 1 - j } - x _ { 1 - i , 1 - j , t } } - \lambda _ { 1 - i , 1 - j } \sqrt { x _ { 1 - i , 1 - j , t } }$ and $V _ { x } ^ { G C }$ is the solution to the HJB equation:

$$
\begin{array}{l} \rho V ^ {G C} = \sum_ {i = 0} ^ {1} \sum_ {j = 0} ^ {1} (\pi_ {i, j} x _ {i, j, t} - u _ {i, j, t} ^ {G C}) \\ \qquad + \sum_ {i = 0} ^ {1} \sum_ {j = 0} ^ {1} \sum_ {k = 0} ^ {1} \sum_ {l = 0} ^ {1} \frac {\partial^ {2} V ^ {G C}}{2 \partial x _ {i , j , t} \partial x _ {k , l , t}} \sigma_ {i, j, t} \sigma_ {k, l, t} \sqrt {x _ {i , j , t} x _ {k , l , t}} \\ \qquad + \sum_ {i = 0} ^ {1} \sum_ {j = 0} ^ {1} V _ {x _ {i, j, t}} ^ {G C} \mu_ {i, j} (u _ {i, j, t} ^ {G C}, u _ {1 - i, j, t} ^ {G C}, u _ {i, 1 - j, t} ^ {G C}, u _ {1 - i, 1 - j, t} ^ {G C}) \end{array}\tag{15}
$$

5.2. Coordination and the Retailer’s Profit For Ω ∈ {NC, MC, BC, GC}, the expected retailer’s profit under Ω, denoted by $P ^ { \Omega }$ , is given by

$$
P ^ {\Omega} = E \left[ \int_ {0} ^ {\infty} \sum_ {i = 0} ^ {1} \sum_ {j = 0} ^ {1} e ^ {- \rho t} (\pi_ {i, j} x _ {i, j, t} - u _ {i, j, t} ^ {\Omega}) d t \right]\tag{16}
$$

subject to

$$
\begin{array}{c} d x _ {i, j, t} = \mu_ {i, j} (u _ {i, j, t} ^ {\Omega}, u _ {1 - i, j, t} ^ {\Omega}, u _ {i, 1 - j, t} ^ {\Omega}, u _ {1 - i, 1 - j, t} ^ {\Omega}) d t + \sigma_ {i, j} d w _ {i, j, t}, \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \text {for} i \in \{0, 1 \},   j \in \{0, 1 \}, \end{array}\tag{17}
$$

where $u ^ { \Omega }$ is the solution to Problem � Ω.

By comparing the formulation of Problem GC with that of $P ^ { \Omega }$ , we can see that Problem GC exactly maximizes Equation (16) under Equation (17). Thus, among the four coordination scenarios, GC always achieves the highest profit. Problem NC, Problem MC, and Problem BC are three approximations to Problem GC. These approximations simplify the problem by allowing a unit to guess other units’ decisions so that different units decisions are disentangled and can be solved independently. However, because each unit guesses others advertising efforts instead of using the true values, this implies that the crossbrand and crosschannel advertising effects are approximated when making advertising decisions. This makes the solutions under NC, MC, and BC suboptimal compared with that under GC.

Both crossbrand and crosschannel advertising effects are approximated under NC, whereas only one of these effects is approximated under MC and BC. From this perspective, MC and BC may seem to be better than NC. However, this is not always true. Mathematically, for the variables $y _ { 1 } , y _ { 2 } , z _ { 1 } , z _ { 1 }$ and the functions $f _ { 1 } , f _ { 2 } , g _ { 1 } , g _ { 2 } ,$ we have the following maximization problem:

$$
\begin{array}{l} \max _ {y _ {1}, y _ {2}} (f _ {1} (y _ {1}, y _ {2}, \hat {z} _ {1}, \hat {z} _ {2}) + f _ {2} (y _ {1}, y _ {2}, \hat {z} _ {1}, \hat {z} _ {2})) \\ \qquad + \max _ {z _ {1}, z _ {2}} (g _ {1} (\hat {y} _ {1}, \hat {y} _ {2}, z _ {1}, z _ {2}) + g _ {2} (\hat {y} _ {1}, \hat {y} _ {2}, z _ {1}, z _ {2})). \end{array}\tag{18}
$$

The optimum in the problem may be larger or smaller than the optimum of the following maximization prob lem involving no coordination:

$$
\begin{array}{l} \max _ {y _ {1}} f _ {1} (y _ {1}, \hat {y} _ {2}, \hat {z} _ {1}, \hat {z} _ {2}) + \max _ {y _ {2}} f _ {2} (\hat {y} _ {1}, y _ {2}, \hat {z} _ {1}, \hat {z} _ {2}) \\ \qquad + \max _ {z _ {1}} g _ {1} (\hat {y} _ {1}, \hat {y} _ {2}, z _ {1}, \hat {z} _ {2}) + \max _ {z _ {2}} g _ {2} (\hat {y} _ {1}, \hat {y} _ {2}, \hat {z} _ {1}, z _ {2}). \end{array}\tag{19}
$$

The difference in the two optimums depends on the functional forms, parameter values, and the choices of $\hat { y } _ { 1 } , \hat { y } _ { 2 } , \hat { z } _ { 1 } , \hat { z } _ { 2 }$ (corresponding to guessed quantities in the model).<sup>5</sup>

From the practical perspective, partial coordination may be worse than no coordination because only consid ering the crossbrand or crosschannel effect may aggravate the approximation error, compared with the error that occurs when both these effects are ignored. Notice that the retailer’s profits under NC, MC, and BC are related to the guesses. To simplify the discussion, we assume that the guesses under NC, MC, and BC are zero. When the crossbrand interference is more significant than the crosschannel and crossbrand sales boosting effects, the sum of the crossbrand and crosschannel effects is negative. Thus, the unit overestimates advertising returns under NC. Under MC, the overestimation is more severe because the unit only considers the crosschannel sales effects (suppose the crosschannel interference is less than the crosschannel boost). Thus, MC may be worse than NC.

Similarly, when the crosschannel sales boosting effects are large and the crossbrand sales boost is small, BC may be worse than NC. If the crosschannel boosting effects are large enough, the sum of the crosschannel and crossbrand effects is positive. Thus, NC underestimates the advertising returns. Different from NC, BC considers the two crossbrand effects but ignores the crosschannel effect. If the crossbrand sales boost is smaller than the interference, the sum of the two crossbrand effects is negative. Under these conditions, we can expect that BC will underestimate the advertising returns more than NC. Thus, BC may be worse than NC.

Because of the complexity of the problem, we are unable to analytically examine when NC is better than BC or MC and when it is not. Instead, we conduct a study on a real-world data set to numerically analyze how different coordination strategies affect profit. We describe the details of our data set in the next section. After that, we show how to implement our two-stage framework on the data set.

Figure 2. (Color online) Online and Offline Sales Curves of Two Brands  
![](/api/attachments/H5BMZU2H/fulltext/images/ba53036afc2f6a7666ed1c291566c337f5a5c8def9e70c36b9da234be97864bb.jpg)

## 6. Data Description

We collaborate with one of the largest jewelry retailers in the United States.<sup>6</sup> This retailer owns two brands, and both offer a variety of jewelry. Each brand has online and offline stores in the United States. We observe each brand’s online and offline sales at the weekly level (Figure 2). Our data include 208 consecutive weeks from 2009 to 2013. There are three hot seasons for jewelry sales: Christmas, Mother’s Day, and Valentine’s Day. Although sales for other weeks are stable, sales increase significantly during hot seasons.

In the literature on time-series analysis, seasonal boosts are usually handled by adding seasonal dummy variables to the model. This works well for structurefree models that do not delve into the underlying sales generation process. However, for a structural model that considers the details of the sales generation process, using dummy variables to capture seasonality may be challenging.

Sales boosts on holidays arise because of several reasons. First, people are more willing to buy jewelry in order to celebrate holidays. The increased interest in jewelry may decrease the market decay rate. Besides, although some customers are insensitive to holidays and buy jewelry whenever they need it, some customers only consider buying jewelry on holidays. Thus, the market size may be larger during holidays. Moreover, holiday-insensitive customers may react to ads differently from holiday-sensitive customers. Thus, the average advertising effects are different between regular periods and hot seasons. Thus, to capture the seasonality, we need to include a seasonality dummy variable for each parameter in our model. This increases the model’s complexity and makes its implementation too difficult.

An alternative way to deal with seasonality is to divide the advertising problem into a set of subproblems, such as the decision problems for regular periods and holiday seasons. For each problem (e.g., Christmas season), we estimate the parameters using the data during the historical Christmas seasons and select the optimal advertising expenditures for the next Christmas season. However, because the holiday seasons are usually short and because we have sparse data for each holiday season, it is difficult to robustly estimate holiday-specific parameters.

To deal with seasonality, we divide the total market during holidays into regular demand and extra demand during holidays. As a response to the larger potential market during holidays, firms often launch additional advertising campaigns during holidays. Thus, we decompose the total advertising effect during holidays into four parts as Figure 3 shows. In this study, as an illustrative example of our two-stage framework, we focus on the impact of regular advertising on the regular market. Thus, we estimate the holiday-only demand and remove it from our data set. The analyses in subsequent sections are based on the de-seasonalized data that only reflect regular demand. Details about seasonality removal can be found in Section EC.3 in the e-companion.

Both brands have online and offline advertising campaigns. We collect their weekly online and offline advertising expenditures. The offline advertising data cover newspaper, radio, television, and billboard campaigns. The online advertising data measure the expenditure of digital display advertising. Around the hot seasons, firms launch extra advertising campaigns in addition to regular advertising campaigns. As mentioned previously, we focus on the impact of regular advertising efforts. Thus, we estimate the extra expenditures spent on the holiday advertising campaigns and remove them from the data. Details can be found in Section EC.4 in the e-companion. The rest of this paper is based on the data after seasonal advertising expenditures are removed (Table 4).

Figure 3. Decomposition of Advertising Effects in Hot Seasons  
![](/api/attachments/H5BMZU2H/fulltext/images/9bdfd814c35b5dffa1cca0ed57752f1191da16571b262c59e85f3216f91d3662.jpg)

Table 4. Descriptive Statistics

<table><tr><td rowspan="2">Variable</td><td colspan="4">Before seasonality removal</td><td colspan="4">After seasonality removal</td></tr><tr><td>Min</td><td>Max</td><td>M</td><td>SD</td><td>Min</td><td>Max</td><td>M</td><td>SD</td></tr><tr><td>Online sales of Brand 0</td><td>0.610</td><td>7.633</td><td>1.513</td><td>1.145</td><td>0.610</td><td>3.028</td><td>1.143</td><td>0.332</td></tr><tr><td>Offline sales of Brand 0</td><td>8.917</td><td>81.056</td><td>17.246</td><td>10.844</td><td>6.101</td><td>34.393</td><td>13.690</td><td>3.012</td></tr><tr><td>Online sales of Brand 1</td><td>0.030</td><td>0.967</td><td>0.169</td><td>0.152</td><td>0.030</td><td>0.395</td><td>0.124</td><td>0.057</td></tr><tr><td>Offline sales of Brand 1</td><td>4.719</td><td>37.132</td><td>8.240</td><td>5.205</td><td>2.943</td><td>13.683</td><td>6.524</td><td>1.186</td></tr><tr><td>Online ad expenditure of Brand 0</td><td>0.000</td><td>0.358</td><td>0.038</td><td>0.059</td><td>0.000</td><td>0.255</td><td>0.030</td><td>0.044</td></tr><tr><td>Offline ad expenditure of Brand 0</td><td>0.000</td><td>7.567</td><td>0.740</td><td>1.619</td><td>0.000</td><td>5.794</td><td>0.363</td><td>0.841</td></tr><tr><td>Online ad expenditure of Brand 1</td><td>0.000</td><td>0.180</td><td>0.047</td><td>0.075</td><td>0.000</td><td>0.180</td><td>0.041</td><td>0.064</td></tr><tr><td>Offline ad expenditure of Brand 1</td><td>0.000</td><td>0.202</td><td>0.061</td><td>0.094</td><td>0.000</td><td>0.139</td><td>0.053</td><td>0.081</td></tr></table>

Note. SD, standard deviation.

## 7. Stage 1: Sales Generation Process Modeling

To apply the model to our data set, let $i = 0$ denote online media, and i � 1 is offline media. Similarly, $j = 0$ refers to the online channel, and j � 1 stands for the offline channel. When training the prediction model on our data set, we consider two SDE models. The first model is the one described in Section 4.4 (i.e., Equation (1) with $d x _ { i , j , t }$ given by Equation (2)). The second model is the one without crosschannel cannibalization (i.e., $\varsigma _ { i , j }$ in Equation (2) is fixed to zero). We consider a model without advertising-induced channel cannibalization because although it may take place between some types of channels and media, there is a lack of empirical evidence for the existence of such channel cannibalization when advertising and sales data are broadly aggregated into online and offline groups.

We train and compare the prediction performance of these two models. The results demonstrate that the prediction accuracy is better when the model does not consider advertising-induced channel cannibalization. Avery et al. (2012) find that channel cannibalization may exist in the short term following the introduction of a new channel. However, it diminishes over time. This may explain why including cannibalization effects does not improve predictions because both online and offline channels in our data set have existed for years. In the subsequent analysis, we focus on the model without cannibalization. The prediction performance of the model with it is provided in Section EC.1 in the ecompanion.

Let $\theta \equiv ( c , \alpha , \beta , \phi , \psi , \gamma , \delta , \lambda , \sigma , M )$ be the parameters to be estimated. Following Yang et al. (2019), we use MLE to recover θ. To apply MLE, we need to know the density function of $x _ { i , j , t + 1 } { \mathrm { ~ g i v e n ~ } } x _ { i , j , t }$ . For any $z \geq t ,$ , the sales at time z conditional on $x _ { i , j , t }$ are $x _ { i , j , z } \mid x _ { i , j , t } = x _ { i , j , t }$ $\textstyle + \int _ { t } ^ { z } d x _ { i , j , s } d s$ . The well-known Fokker–Planck equation (FPE) characterizes the density function $f ( x _ { i , j , z } , z \mid x _ { i , j , t } )$ (Jordan et al. 1998). In our study, the FPE is given by

$$
\begin{array}{r l} & {\frac {\partial}{\partial z} f (x _ {i, j, z}, z \mid x _ {i, j, t}) = - \frac {\partial}{\partial x _ {i , j , z}} [ \mu_ {i, j} f (x _ {i, j, z}, z \mid x _ {i, j, t}) ]} \\ & {\qquad + \frac {\partial^ {2}}{\partial x _ {i , j , z} ^ {2}} \left[ \frac {1}{2} \sigma_ {i, j} ^ {2} x _ {i, j, z} f (x _ {i, j, z}, z \mid x _ {i, j, t}) \right].} \end{array}\tag{20}
$$

For any time $t ,$ we substitute the observed values of $x _ { i , j , t }$ and $u _ { i , j , t }$ into the FPE and numerically solve it in MATLAB. Let $\tilde { f } ( x _ { i , j , z } , z \mid x _ { i , j , t } )$ be the numerical solution to FPE. The log-likelihood function of observing $\{ x _ { i , j , 1 } , \dotsc , x _ { i , j , T } \}$ is given by

$$
\ln \mathcal {L} (\theta) = \sum_ {t = 1} ^ {T - 1} \ln \tilde {f} (x _ {i, j, t + 1}, t + 1 | x _ {i, j, t}).\tag{21}
$$

The MLE estimator of $\theta$ is acquired by maximizing the log-likelihood function. We obtain the MLE estimates using the simulated annealing algorithm:

$$
\hat {\theta} \equiv (\hat {\alpha}, \hat {\beta}, \hat {\phi}, \hat {\psi}, \hat {\gamma}, \hat {\delta}, \hat {\eta}, \hat {\sigma}, \hat {M}) = \arg \max _ {\theta} \ln \mathcal {L} (\theta).\tag{22}
$$

To accelerate the convergence, we use a linear regression (LR) model to obtain the initial values as the input to the optimization algorithm. The U.S. retail sales of jewelry from 2009 to 2013 are 51, 51.8, 56.3, 57, and 57.9 billion dollars, respectively (Golan 2018). We take their average as the total size of the jewelry market. The initial value of $M _ { i , j }$ is considered to be the total market size multiplied by how much the sales segment $( i , j )$ accounts for the retailer’s total sales. After that, we obtain the initial values for $\alpha , \beta , \gamma , \delta , \lambda$ by running the regression specified by Equation (23). Finally, we obtain the residuals of the regression model and take the standard deviation of residuals as the initial value of σ:

Table 5. Parameter Estimates

<table><tr><td>Brand</td><td>Channel</td><td> $\hat{\alpha}$ </td><td> $\hat{\beta}$ </td><td> $\hat{\phi}$ </td><td> $\hat{\psi}$ </td><td> $\hat{\delta}$ </td></tr><tr><td>0</td><td>Online</td><td>0.520***(0.061)</td><td>0.464***(0.059)</td><td>0.435***(0.049)</td><td>0.746***(0.083)</td><td>0.122***(0.017)</td></tr><tr><td>0</td><td>Offline</td><td>0.175***(0.006)</td><td>0.522***(0.020)</td><td>0.579***(0.019)</td><td>0.659***(0.022)</td><td>0.096***(0.004)</td></tr><tr><td>1</td><td>Online</td><td>0.463***(0.013)</td><td>0.417***(0.013)</td><td>0.381***(0.010)</td><td>0.243***(0.007)</td><td>0.230***(0.008)</td></tr><tr><td>1</td><td>Offline</td><td>0.476***(0.025)</td><td>0.300***(0.017)</td><td>0.786***(0.039)</td><td>0.463***(0.023)</td><td>0.029***(0.002)</td></tr></table>

Note. Standard errors are displayed in parentheses.  
\*\*\*Significant at 0.01.

$$
\begin{array}{l} d x _ {i, j, t} \\ \sim \alpha_ {i, j} \sqrt {\frac {u _ {i , j , t}}{c _ {j}}} \sqrt {M _ {i , j} - x _ {i , j , t}} + \beta_ {i, j} \sqrt {\frac {u _ {i , 1 - j , t}}{c _ {1 - j}}} \sqrt {M _ {i , j} - x _ {i , j , t}} \\ + \phi_ {i, j} \sqrt {\frac {u _ {1 - i , j , t}}{c _ {j}}} \sqrt {M _ {i , j} - x _ {i , j , t}} + \psi_ {i, j} \sqrt {\frac {u _ {1 - i , 1 - j , t}}{c _ {1 - j}}} \sqrt {M _ {i , j} - x _ {i , j , t}} \\ + \gamma_ {i, j} \left(- \sqrt {\frac {u _ {1 - i , j , t}}{c _ {j}}} \sqrt {x _ {i , j , t}}\right) + \lambda_ {i, j} \left(- \sqrt {\frac {u _ {1 - i , 1 - j , t}}{c _ {1 - j}}} \sqrt {x _ {i , j , t}}\right) \\ + \delta_ {i, j} (- x _ {i, j, t}). \end{array} \tag {23}
$$

Because $c _ { j }$ always appears with $\alpha _ { i , j } , \phi _ { i , j }$ and $\gamma _ { i , j ^ { \prime } }$ we cannot separate $c _ { j }$ with them during MLE. Similarly, we cannot estimate $c _ { 1 - j }$ separately. During MLE, we fix $c _ { 0 } =$ \$2 and $c _ { 1 } = \$ 28$ based on the cost per thousand impressions reported by Morgan Stanley (O’Kane 2010).

## 7.1. Estimation Results

Tables 5 and 6 display the estimates of parameters. First, consistent with the literature (e.g., Danaher et al. 2020), we find that online and offline advertisements have significant spillovers to sales on nonnative channels. Such same-brand crosschannel effectiveness $( \mathrm { i . e . , } \hat { \beta } )$ is comparable with its native-channel counterpart (i.e., αˆ). For offline sales of brand 0, the same-brand crosschannel effectiveness is even larger than the same-brand nativechannel effectiveness.

Tables 5 and 6 also provide evidence for crossbrand (native-channel and crosschannel) sales-boosting effects $( \mathrm { i . e . , } \hat { \phi }$ and $\hat { \psi } )$ . Among the four sales segments, online sales of brand 1 are the least affected by the crossbrand sales-boosting effect. For the other segments, the crossbrand sales boosts are comparable with or greater than the same-brand boosts. Besides, each brand’s sales also suffer from crossbrand (native-channel and crosschannel) interference $( \mathrm { i . e . , } \hat { \gamma }$ and λ<sup>ˆ</sup>). For the sales of brand 0, the advertising of brand 1 boosts them more than the negative interference effect in most cases. For the sales of brand 1, the advertising of brand 0 generates more negative effects than positive impacts.

The main takeaway of Tables 5 and 6 is that the advertising of each unit affects the sales of all segments. The sales-boosting effectiveness and interference parameters vary drastically across sales segments and advertising units. Besides, recall that both sales boosts and interference depend on sales. Thus, to achieve advertising efficiency, the retailer needs a comprehensive model that estimates all types of advertising effects and dynamically coordinates the advertising efforts of all units based on sales.

## 7.2. Model Validation

Before using the SDE model in optimization problems, we need to verify its ability to predict future sales. If the SDE predicts sales with high accuracy, the optimal advertising expenditures derived from it are highly likely to achieve a high profit; otherwise, there is no meaning in making decisions based on the SDE model. The ideal way to validate our model is through field experiments. However, such experiments are costly and beyond our ability. Instead, following Yang et al. (2019), we validate our SDE model by examining its prediction performance compared with benchmark models.

We consider the following benchmark models: naive method (NM), ARIMA, GARCH, ARIMA-GARCH, and vector autoregression (VAR). An NM(m) model uses the unweighted average sales from week t � m to t � 1 as the sales prediction for week t. ARIMA(p, d, q) is a widely used time-series model. If $d = 0 ,$ , ARIMA takes $x _ { i , j , t }$ as the dependent variable (DV). If $d > 0 ,$ , the differenced data $( \mathrm { i . e . , ~ } x _ { i , j , t } ^ { \prime } = x _ { i , j , t } - x _ { i , j , t - d } )$ are taken as the DV. ARIMA decomposes the DV into an autoregressive part and a moving average part. The autoregressive part of the DV is a linear function of the DV from week $t - p$ to $t - 1 ,$ and the moving average part is a linear function of the forecast errors from week $t - q$ to t � 1. GARCH(a, b) is used to handle time-series data with heterogeneous variances across time. It decomposes the variance of $x _ { i , j , t }$ into a linear function of the estimated variances in the previous a weeks and another linear function of the squared prediction residuals in the previous b weeks. $\bar { A R I M A ( p , d , q ) } - G A R C H ( a , b )$ combines the previous two models. $V A R ( p )$ models the vector of observations in week i as a function of the observations in the previous p weeks.

Table 6. Parameter Estimates

<table><tr><td>Brand</td><td>Channel</td><td> $\hat{\gamma }$ </td><td> $\hat{\lambda }$ </td><td> $\hat{\sigma }$ </td><td> $\hat{M}$ </td></tr><tr><td>0</td><td>Online</td><td>0.392*** (0.053)</td><td>0.416*** (0.046)</td><td>0.293*** (0.028)</td><td>5.009*** (1.835)</td></tr><tr><td>0</td><td>Offline</td><td>0.243*** (0.010)</td><td>0.749*** (0.024)</td><td>1.042*** (0.033)</td><td>50.04*** (2.105)</td></tr><tr><td>1</td><td>Online</td><td>0.561*** (0.019)</td><td>0.291*** (0.008)</td><td>0.119*** (0.003)</td><td>0.556*** (0.018)</td></tr><tr><td>1</td><td>Offline</td><td>0.377*** (0.023)</td><td>0.619*** (0.030)</td><td>0.517*** (0.024)</td><td>26.705*** (2.364)</td></tr></table>

\*\*\*Significant at 0.01.  
Note. Standard errors are displayed in parentheses.

We also consider three linear models as our benchmark because LMs have been used for sales predictions and shown good performance (e.g., Cohen et al. 2021). The first one is the linear model (denoted by LM) used in Cohen et al. (2021). In the model, p is the number of lags used to predict $x _ { i , j , t } \colon$

$$
\begin{array}{l} x _ {i, j, t} = \omega_ {0} + \sum_ {k = 1} ^ {p} \omega_ {k} x _ {i, j, t - k} + \kappa_ {1} x _ {1 - i, j, t - 1} + \kappa_ {2} x _ {i, 1 - j, t - 1} \\ \quad + \kappa_ {3} x _ {1 - i, 1 - j, t - 1} + \epsilon . \end{array} \tag {2}\tag{24}
$$

The second is the log-log linear model (LL) adapted from the model in Cohen et al. (2017):

$$
\begin{array}{c} \ln (x _ {i, j, t}) = \omega_ {0} + \sum_ {k = 1} ^ {p} \omega_ {k} \ln (x _ {i, j, t - k}) + \kappa_ {1} \ln (x _ {1 - i, j, t - 1}) \\ + \kappa_ {2} \ln (x _ {i, 1 - j, t - 1}) + \kappa_ {3} \ln (x _ {1 - i, 1 - j, t - 1}) + \epsilon . \end{array}\tag{25}
$$

Finally, in the previous section, we use Equation (23) as a warm start to our estimation process. We also take it as a benchmark model (denoted by LR).

Following the literature (e.g., Yang et al. 2019), we separate our data into the training set and the test set.

For each model, we use the first two thirds of our data as the training set to estimate the parameters. Details about the parameter selection for benchmark models can be found in Section EC.8 in the e-companion. After obtaining the parameters, we use the model to generate predictions for the sales in the test set (i.e., the remaining one third of the data). We conduct a one-step prediction analysis (i.e., we forecast the sales in one week based on the observed sales in the week before it).

The performance metrics used in this study include the mean squared error (MSE), mean absolute error (MAE), and symmetric mean absolute percent error (SMAPE). Based on Table 7, the performance of our SDE model is better than the benchmarks in general. There are cases where SDE is slightly worse than some benchmarks. This does not undermine the potential of SDE. An important advantage of our SDE model is that it is a structural model that allows for counterfactual analysis.

## 8. Stage 2: Optimization Problem Formulation

In stage 2, we formulate the optimization problem. For any coordination scenario, to obtain the optimization problem described in Section 5, we need to know another set of parameters— $- \rho , \pi ,$ and e. In practice, a retailer can decide these parameters based on the operational details. However, in our case study, we do not have such information and need to estimate it from the data.

## 8.1. Estimation Procedures

To estimate the parameters, we need to know under which scenario our advertising data are generated. To answer this question, we first derive a diffusion equation for each coordination scenario. A scenario-specific diffusion equation captures the evolution process of sales when the optimal advertising efforts under that scenario are used. We use MLE to recover the parameters in four scenario-specific equations and compare their performances in sales predictions.

Table 7. Prediction Performance

<table><tr><td></td><td>Brand</td><td>Channel</td><td>SDE</td><td>NM</td><td>ARIMA</td><td>GARCH</td><td>ARIMA-ARCH</td><td>VAR</td><td>LR</td><td>LM</td><td>LL</td></tr><tr><td rowspan="4">MAE</td><td>0</td><td>Online</td><td>0.193</td><td>0.221</td><td>0.198</td><td>0.290</td><td>0.545</td><td>0.335</td><td>0.248</td><td>0.339</td><td>0.348</td></tr><tr><td>0</td><td>Offline</td><td>1.633</td><td>1.968</td><td>2.097</td><td>1.790</td><td>2.262</td><td>2.090</td><td>2.142</td><td>2.345</td><td>2.450</td></tr><tr><td>1</td><td>Online</td><td>0.038</td><td>0.038</td><td>0.033</td><td>0.059</td><td>0.102</td><td>0.072</td><td>0.045</td><td>0.073</td><td>0.074</td></tr><tr><td>1</td><td>Offline</td><td>0.637</td><td>0.720</td><td>1.306</td><td>0.655</td><td>0.809</td><td>0.674</td><td>0.681</td><td>0.669</td><td>0.687</td></tr><tr><td rowspan="4">MSE</td><td>0</td><td>Online</td><td>0.091</td><td>0.104</td><td>0.094</td><td>0.174</td><td>0.467</td><td>0.214</td><td>0.110</td><td>0.214</td><td>0.224</td></tr><tr><td>0</td><td>Offline</td><td>6.936</td><td>5.597</td><td>7.842</td><td>6.111</td><td>7.850</td><td>7.863</td><td>7.952</td><td>8.939</td><td>9.637</td></tr><tr><td>1</td><td>Online</td><td>0.003</td><td>0.003</td><td>0.002</td><td>0.006</td><td>0.015</td><td>0.008</td><td>0.004</td><td>0.008</td><td>0.008</td></tr><tr><td>1</td><td>Offline</td><td>0.757</td><td>1.116</td><td>2.288</td><td>0.892</td><td>1.045</td><td>0.940</td><td>1.007</td><td>0.937</td><td>0.984</td></tr><tr><td rowspan="4">SMAPE</td><td>0</td><td>Online</td><td>0.144</td><td>0.159</td><td>0.144</td><td>0.215</td><td>0.328</td><td>0.254</td><td>0.184</td><td>0.260</td><td>0.268</td></tr><tr><td>0</td><td>Offline</td><td>0.143</td><td>0.112</td><td>0.145</td><td>0.120</td><td>0.145</td><td>0.142</td><td>0.145</td><td>0.161</td><td>0.170</td></tr><tr><td>1</td><td>Online</td><td>0.208</td><td>0.209</td><td>0.185</td><td>0.365</td><td>0.690</td><td>0.479</td><td>0.273</td><td>0.496</td><td>0.504</td></tr><tr><td>1</td><td>Offline</td><td>0.131</td><td>0.108</td><td>0.183</td><td>0.097</td><td>0.121</td><td>0.099</td><td>0.100</td><td>0.099</td><td>0.102</td></tr></table>

8.1.1. NC Scenario. We first explain the scenariospecific diffusion equation under NC. In this case, the evolution process of $x _ { i , j , t }$ is given by the following diffusion equation:

$$
\begin{array}{c} d x _ {i, j, t} = \mu_ {i, j} (u _ {i, j, t} ^ {N C}, u _ {1 - i, j, t}, u _ {i, j, t}, u _ {1 - i, 1 - j, t}) d t \\ + \sigma_ {i, j} \sqrt {x _ {i , j , t}} d w _ {i, j, t}. \end{array}\tag{26}
$$

Compared with Equation (2), the observed advertising effort $u _ { i , j , t }$ is replaced by the theoretical optimal advertising effort under $\mathrm { N } \check { \mathbf { C } } \ ( \mathrm { i . e . , } u _ { i , j , t } ^ { N C } )$ in Equation (26). Although perfectly achieving the theoretical optimal effort is difficult and although it is common to see a difference between the observed effort and the optimal one in theory, such a difference should not be very large if NC is indeed the strategy used by the retailer. Thus, if unit $( i , j )$ decides its advertising expenditure without any coordination, it can be anticipated that Equation (26) can capture the evolution process of $x _ { i , j , t }$ similar to Equation (2).

Parameters to be estimated under NC are $\kappa ^ { N C } \equiv ( \rho ,$ $\pi _ { i , j } , e _ { 1 - i , j } ^ { i , j } , e _ { i , 1 - j } ^ { i , j } , e _ { 1 - i , 1 - j } ^ { i , j } )$ . For other parameters $( \mathrm { i } . \mathrm { e } . , c , \alpha ,$ $\beta , \gamma , \delta , \lambda , \sigma , \mathrm { { M } } )$ , we use the estimates obtained previously. We apply MLE to recover $\kappa ^ { N C }$ . The density function $\mathsf { \bar { f } } ^ { N C } ( x _ { i , j , z } , z \vert x _ { i , j , t - 1 } )$ under Equation (26) is obtained by solving the FPE:

$$
\begin{array}{r} \frac {\partial f ^ {N C}}{\partial z} = - \frac {\partial}{\partial x _ {i , j , z}} [ f ^ {N C} \mu_ {i, j} (u _ {i, j, z} ^ {N C}, u _ {1 - i, j, z}, u _ {i, j, z}, u _ {1 - i, 1 - j, z}) ] \\ + \frac {\partial^ {2}}{\partial x _ {i , j , z} ^ {2}} \left[ \frac {1}{2} \sigma_ {i, j} ^ {2} x _ {i, j, z} f ^ {N C} \right]. \end{array}\tag{27}
$$

Let $\tilde { \boldsymbol { f } } ^ { N C }$ be the numerical solution to the equation. The log-likelihood function is given by

$$
\mathcal {L} ^ {N C} (\kappa^ {N C}) = \sum_ {t = 1} ^ {T - 1} \ln \tilde {f} ^ {N C} (x _ {i, j, t + 1}, t + 1 \mid x _ {i, j, t}; \kappa^ {N C})).\tag{28}
$$

The maximum likelihood estimator of $\hat { \kappa } ^ { N C }$ is acquired by maximizing the log-likelihood function. The value of ρ does not affect the estimates and was fixed at 0.001:

$$
\hat {\kappa} ^ {N C} \equiv (\hat {\rho}, \hat {\pi} _ {i, j}, \hat {e} _ {1 - i, j} ^ {i, j}, \hat {e} _ {i, 1 - j} ^ {i, j}, \hat {e} _ {1 - i, 1 - j} ^ {i, j}) = \arg \max _ {\kappa^ {N C}} \mathcal {L} ^ {N C} (\kappa^ {N C}).\tag{29}
$$

8.1.2. MC Scenario. If our data are generated under MC, the observed sales evolution of units (i, 0) and (i, 1) should be captured by the following equations:

$$
\begin{array}{r l} & {d x _ {i, 0, t} = \mu_ {i, 0} (u _ {i, 0, t} ^ {M C}, u _ {1 - i, 0, t}, u _ {i, 1, t} ^ {M C}, u _ {1 - i, 1, t}) d t} \\ & {\qquad + \sigma_ {i, 0} \sqrt {x _ {i , 0 , t}} d w _ {i, 0, t}} \\ & {d x _ {i, 1, t} = \mu_ {i, 1} (u _ {i, 1, t} ^ {M C}, u _ {1 - i, 1, t}, u _ {i, 0, t} ^ {M C}, u _ {1 - i, 0, t}) d t} \\ & {\qquad + \sigma_ {i, 1} \sqrt {x _ {i , 1 , t}} d w _ {i, 1, t}.} \end{array}\tag{30}
$$

(31)

Similar to the equation under NC, the observed efforts $u _ { i , 0 , t }$ and $u _ { i , 1 , t }$ are replaced by the theoretical optimal efforts under MC $( \mathrm { i . e . , } u _ { i , 0 , t } ^ { M C }$ and $u _ { i , 1 , t } ^ { M C } )$ in Equations (30) and (31), relative to Equation (2).

8.1.3. BC Scenario. In the case of brand coordination, the diffusion process of the sales of units $( 0 , j )$ and $( 1 , j )$ can be described as follows:

$$
\begin{array}{r l} & d x _ {0, j, t} = \mu_ {0, j} (u _ {0, j, t} ^ {B C}, u _ {1, j, t} ^ {B C}, u _ {0, 1 - j, t}, u _ {1, 1 - j, t}) d t \\ & \qquad + \sigma_ {0, j} \sqrt {x _ {0 , j , t}} d w _ {0, j, t} \\ & d x _ {1, j, t} = \mu_ {1, j} (u _ {1, j, t} ^ {B C}, u _ {0, j, t} ^ {B C}, u _ {1, 1 - j, t}, u _ {0, 1 - j, t}) d t \\ & \qquad + \sigma_ {1, j} \sqrt {x _ {0 , j , t}} d w _ {1, j, t}. \end{array}\tag{32}
$$

(33)

8.1.4. GC Scenario. Finally, we present the diffusion equation under global coordination:

$$
\begin{array}{c} d x _ {i, j, t} = \mu_ {i, j} (u _ {i, j, t} ^ {G C}, u _ {1 - i, j, t} ^ {G C}, u _ {i, 1 - j, t} ^ {G C}, u _ {1 - i, 1 - j, t} ^ {G C}) d t \\ + \sigma_ {i, j} \sqrt {x _ {i , j , t}} d w _ {i, j, t}. \end{array}\tag{34}
$$

Similar to NC, we can recover π and e under MC, BC, and GC by solving the corresponding FPE and maximizing the log-likelihood function. Details can be found in Section EC.7 in the e-companion.

## 8.2. Estimation Results

To investigate under which scenario our data are generated, we take two thirds of our data to recover the parameters in each scenario-specific diffusion equation. Then, we take the remaining one third as the test data set, use each scenario-specific diffusion equation to generate the predictions on the test data set, and calculate the prediction performance.

Table 8 shows that the prediction performance in NC is the best among the four scenarios. Thus, NC is the most probable scenario under which our data set is generated. Further, Table 9 presents the estimates of parameters under NC. As the table shows, the estimates for guesses are insignificant. In summary, not only is NC the best-fitting scenario in our data set, but we also do not find evidence that each unit considers other units advertising efforts when it makes its own advertising decisions.

Table 8. Scenario Validation Results

<table><tr><td></td><td>Brand</td><td>Channel</td><td>NC</td><td>MC</td><td>BC</td><td>GC</td></tr><tr><td rowspan="4">MAE</td><td>0</td><td>Online</td><td>0.234</td><td>0.258</td><td>0.288</td><td>0.333</td></tr><tr><td>0</td><td>Offline</td><td>1.742</td><td>1.912</td><td>2.179</td><td>2.437</td></tr><tr><td>1</td><td>Online</td><td>0.049</td><td>0.070</td><td>0.054</td><td>0.083</td></tr><tr><td>1</td><td>Offline</td><td>0.813</td><td>0.946</td><td>0.872</td><td>1.152</td></tr><tr><td rowspan="4">MSE</td><td>0</td><td>Online</td><td>0.133</td><td>0.159</td><td>0.164</td><td>0.237</td></tr><tr><td>0</td><td>Offline</td><td>7.686</td><td>8.324</td><td>7.932</td><td>8.821</td></tr><tr><td>1</td><td>Online</td><td>0.004</td><td>0.009</td><td>0.007</td><td>0.011</td></tr><tr><td>1</td><td>Offline</td><td>1.192</td><td>1.977</td><td>1.432</td><td>2.245</td></tr><tr><td rowspan="4">SMAPE</td><td>0</td><td>Online</td><td>0.161</td><td>0.229</td><td>0.537</td><td>0.663</td></tr><tr><td>0</td><td>Offline</td><td>0.147</td><td>0.165</td><td>0.204</td><td>0.280</td></tr><tr><td>1</td><td>Online</td><td>0.182</td><td>0.185</td><td>0.355</td><td>0.338</td></tr><tr><td>1</td><td>Offline</td><td>0.136</td><td>0.136</td><td>0.146</td><td>0.750</td></tr></table>

Table 9. Parameter Estimates Under NC

<table><tr><td>Brand</td><td>Channel</td><td> $\pi$ </td><td> $e_{0,0}$ </td><td> $e_{0,1}$ </td><td> $e_{1,0}$ </td><td> $e_{1,1}$ </td></tr><tr><td>0</td><td>Online</td><td>0.226** (0.135)</td><td>—</td><td>0.005 (0.140)</td><td>0.057 (0.139)</td><td>0.071 (0.135)</td></tr><tr><td>0</td><td>Offline</td><td>0.793*** (0.069)</td><td>0.059 (0.070)</td><td>—</td><td>0.011 (0.070)</td><td>0.030 (0.070)</td></tr><tr><td>1</td><td>Online</td><td>0.698*** (0.091)</td><td>0.009 (0.074)</td><td>0.046 (0.064)</td><td>—</td><td>0.028 (0.081)</td></tr><tr><td>1</td><td>Offline</td><td>0.245** (0.106)</td><td>0.018 (0.108)</td><td>0.093 (0.107)</td><td>0.088 (0.107)</td><td>—</td></tr></table>

Note. Standard errors are displayed in parentheses.  
\*\*Significant at 0.05; \*\*\* significant at 0.01.

## 9. Coordination Performance

In this section, we analyze how much the profit can be improved if the retailer adopts one coordination strategy. We also investigate the impact of parameters on the coordination performance by changing the parameter values and reestimating the retailer’s profit. Specifically, we examine how crossbrand interference, crossbrand sales boosts, and crosschannel sales boosts affect the retailer’s profit. Under NC, MC, and BC, the optimal advertising efforts depend on how each unit guesses other units’ efforts $( \mathrm { i . e . , } e )$ . Because we do not find evidence that any unit guesses other units’ efforts, we consider that all guesses are zero during the experiments.

## 9.1. Crossbrand Interference Effects

We start with the impact of crossbrand interference $( \mathrm { i . e . , } \gamma$ and λ). Let $\hat { \gamma } _ { i , j }$ and $\hat { \lambda } _ { i , j }$ be the previous estimates of $\gamma _ { i , j }$ and $\lambda _ { i , j }$ . We evaluate the retailer’s profits under NC, MC, BC, and GC when the crossbrand interference parameters are $k \hat { \gamma } _ { i , j }$ and $k \hat { \lambda } _ { i , j }$ for $k \in [ 0 , 1 . 6 ]$ . We conduct two experiments. In the first experiment, except λ and γ, other parameters are fixed to the previous estimates. In the second experiment, we further set $\phi _ { i , j } =$ $\psi _ { i , j } = 0 \ \mathrm { ( i . e . }$ , no crossbrand sales boosts). The results are displayed in Figure 4. In Figure 4, the retailer’s profit decreases as the crossbrand interference increases, regardless of the coordination strategies. This is because a larger interference effect implies a higher intraportfolio brand competition and reduces the advertising returns at the retailer’s level.

In Figure 4(a), the gap between MC and GC first reduces and then increases with k. Recall that GC considers all advertising effects and that MC ignores the crossbrand sales boosts and interference. When the magnitudes of the crossbrand sales boosts and interference are similar so that their joint effect is close to zero, MC achieves a profit similar to GC. Second, BC is better than NC when k is small. Relative to GC, BC underestimates the advertising returns because it neglects the same-brand crosschannel sales boosts. When k is small, the joint effect of the crossbrand sales boosts, and interference is positive. Thus, relative to BC, NC further underestimates the advertising returns by ignoring the joint crossbrand effect. However, as k increases, the joint crossbrand effect becomes negative. Thus, NC becomes better than BC because considering the joint crossbrand effect under BC makes the retailer underestimate the advertising returns more than NC.

Third, Figure 4(a) indicates that there exist scenarios such that NC is the best strategy among BC and MC. This happens when the joint effect of crosschannel sales boosts, crossbrand sales boosts, and crossbrand interference is close to zero. In this case, the advertising returns estimated by NC are the closest to GC because NC ignores these effects. MC only considers the positive crosschannel sales-boosting effect and significantly overestimates the returns. BC only considers the negative joint crossbrand effect and underestimates the returns. Therefore, MC and BC are worse than NC.

Figure 4. (Color online) Impacts of the Crossbrand Advertising Interference $( k \hat { \gamma } _ { i , j }$ and $k \hat { \lambda } _ { i , j } )$ on the Retailer’s Profit  
(a)  
![](/api/attachments/H5BMZU2H/fulltext/images/8b6968d724ec4ca9be79d82d3aa110d1f5c30a89f13d26d994083a943a7861a5.jpg)

(b)  
![](/api/attachments/H5BMZU2H/fulltext/images/47173c40665b986e094062bb32c293dd06e33e07a3a4bb50b64f72f06f86f587.jpg)

The results displayed in Figure 4(b) are qualitatively the same as those in Figure 4(a). In Figure 4(a), the joint crossbrand effect becomes close to zero when k is around 0.4. Thus, we have that the profit under MC (BC) is similar to that under GC (NC). In Figure 4(b), the crossbrand sales boosts are zero. Thus, similar results arise under k � 0, wherein the joint crossbrand effect is zero.

Figure 4(b) extends the implications of Figure 4(a) in two aspects. First, Figure 4(b) shows that when crossbrand interference is strong, MC can lead to a negative profit because the retailer advertises too much when the advertising effectiveness is less than the unit advertising cost. In practice, some multibrand retailers deliberately create intense internal competition across their brands to incentivize each brand to improve its operations (Junior 2018). Our results suggest that such retailers should not focus on MC as it may hurt profit.

Besides, Figure 4(a) shows that BC is better than NC when k is small and becomes worse than NC as k increases. Figure 4(b) shows that when k is large enough, BC becomes better again. When k is large, the joint crossbrand effect is negative and dominates the crosschanne boosts. Thus, BC underestimates the advertising return, whereas NC overestimates it. When the overestimation under NC is larger than the underestimation under BC, BC becomes better than NC again. To explore this further, we extend the range of k in our numerical experiment. Our results show that the retailer’s profits under NC, MC BC, and GC converge to $- 2 , 6 7 3 , \bar { - 2 2 } , 8 6 7 ,$ 174, and 174, respectively, for high values of k. This suggests that BC closely matches GC when crossbrand interference is significant.

To summarize, the relative performances of NC, MC, and BC change significantly under different values of the crossbrand interference parameters (i.e., λ and γ). Thus, for retailers that are unable to do global coordination, Figure 4 highlights the importance of selecting an appropriate coordination strategy among NC, MC, and BC. More importantly, under some values of λ and $\gamma ,$ NC can be the best among these three strategies. In this case, partial coordination even hurts the retailer compared with noncoordination, so the retailer should not invest in MC and BC at all.

We conclude this section by noting that all the findings are caused by the coexistence of the same-brand crosschannel effect and the joint crossbrand effect. Thus, these findings are unique to the multibrand, multimedia advertising problem because retailers with single-brand, multimedia or single-media, multibrand advertising only face one of these two effects. This highlights the fundamental differences between the multibrand, multimedia advertising problem and other advertising problems.

## 9.2. Crossbrand Sales-Boosting Effectiveness

This section investigates the impact of the crossbrand sales-boosting effectiveness $( \mathrm { i . e . , } \phi$ and ψ) on the retailer’s profit. Similar to the earlier section, we examine the retailer’s profit when the crossbrand sales-boosting effectiveness is $k \hat { \phi } _ { i , j }$ and $k \hat { \psi } _ { i , j }$ for $k \in [ 0 , 1 . 6 ]$ ]. We also conduct two experiments: one with the crossbrand interference parameters set to previous estimates $( \gamma _ { i , j } =$ $\hat { \gamma } _ { i , j } , \lambda _ { i , j } = \hat { \lambda } _ { i , j } )$ and one without the crossbrand interference effect $( \dot { \gamma } _ { i , j } = \lambda _ { i , j } = 0 )$ ). Other parameters are set to the estimates in earlier sections. The experimental results are displayed in Figure 5.

Figure 5(a) displays the retailer’s profit when the crossbrand interference effects are given by the estimates $\hat { \lambda } _ { i , j }$ and $\hat { \gamma } _ { i , j } .$ We can observe that the retailer’s profit increases with the crossbrand sales-boosting effectiveness. This is because a more significant crosschannel sales-boosting effect means more advertising returns. As for the comparison among NC, MC, and ${ \mathrm { B C } } ,$ when k is small, MC is the worst strategy, whereas BC is the best one. This is because in this case, crossbrand interference plays the dominant role among all crossunit advertising effects. BC considers the dominant effect and thus, achieves the highest profit among these three strategies. Both NC and MC overestimate the advertising return, but MC overestimates it more than NC. Therefore, MC is worse than NC.

(a)  
Figure 5. (Color online) Impacts of the Crossbrand Sales-Boosting Effectiveness $( k \hat { \phi } _ { i , j }$ and $k \hat { \psi } _ { i , j } ^ { \mathrm { ~ ~ } } )$ ) on the Retailer’s Profit  
![](/api/attachments/H5BMZU2H/fulltext/images/72c358e6dbe98ea44c62138d6c9b6a34c76f3057569d74ed961dfde374befe82.jpg)

(b)  
![](/api/attachments/H5BMZU2H/fulltext/images/f62dd8d5be2bdba1828f7177c64f6427b792f1aa7f0a6c910977b8f734a87079.jpg)

As k increases, BC becomes the worst strategy. This is because as k increases, the joint crossbrand effect (i.e., the sum of the crossbrand sales boosts and interference) changes from negative to zero. This changes the dominant effect from the joint crossbrand effect to the samebrand crosschannel boosts. In this case, NC and BC underestimate the advertising returns. BC underestimates the returns more than NC because BC considers the negative joint crossbrand effect. Thus, BC is worse than NC. As k increases further, the joint crossbrand effect becomes closer to zero. Considering the joint crossbrand effect causes a smaller difference between BC and NC. Thus, the advantage of NC over BC decreases.

In Figure 5(b), when there is no crossbrand sales interference, NC is always the worst strategy. In this case, the joint crossbrand effect is positive. Thus, both MC and BC underestimate the returns of advertising because they ignore either the same-brand crosschannel effect or the joint crossbrand effect. NC underestimates the returns more than MC and BC because it ignores all crossunit effects.

## 9.3. Same-Brand Crosschannel Sales-Boosting Effectiveness

In this section, we compare the performances of four coordination strategies when the same-brand crosschannel advertising effectiveness is $k \hat { \beta } _ { i , j }$ for $i , j \in \{ 0 , 1 \}$ and $k \in [ 0 , 1 . 6 ]$ . Other parameters are set to the estimates in earlier sections. Figure 6 visualizes the experimental results. First, we observe that as the same-brand crosschannel sales-boosting effectiveness increases, the retailer’s profit increases. Second, BC is better than MC when the same-brand crosschannel effects are small. This is because the joint crossbrand effect dominates the same-brand crosschannel effect. As k increases, MC becomes better because the same-brand crosschannel effect plays a more important role. This implies that BC is a better choice than MC if a retailer does not have many multichannel shoppers.

Figure 6. (Color online) Impacts of Crosschannel Sales-Boosting Effectiveness on the Retailer’s Profit  
![](/api/attachments/H5BMZU2H/fulltext/images/664c5d6cc76aa12167fbc8b59a4f235efa7591fc6e8ec5ceebe44c0d79a607ea.jpg)

Third, MC is always better than NC as the samebrand crosschannel effectiveness increases. However, BC results in a profit less than NC when the same-brand crosschannel sales-boosting effect is significant. This is because the retailer faces a positive same-brand crosschannel effect and a negative joint crossbrand effect. When the same-brand crosschannel sales-boosting effect plays a dominant role, both BC and NC underestimate the advertising returns, but the underestimation under BC is more significant because it considers the negative joint crossbrand effect.

## 10. Conclusions and Insights

This study investigates the optimal multimedia advertising strategy of the multibrand, multichannel retailer. Toward this end, we consider a retailer with two brands. Each brand has two sales channels and delivers its advertisements on two types of media. We develop an SDE model to study how the advertising of each brand-media unit affects sales. Our model not only considers the samebrand native-channel advertising effect but also incorporates the crossbrand and crosschannel effects. We use MLE to recover the model parameters using a data set from one of the largest jewelry retailers in the United States. The model is validated by comparing its predictive performance against classical time-series models. The results indicate that our model achieves high accuracy in sales predictions.

Because of the interactions among different brandmedia units, a multibrand, multichannel retailer with multimedia advertising campaigns needs to coordinate the advertising efforts across different units to propel its sales efficiently. Depending on the coordinated dimensions, we summarize four coordination strategies: non coordination, brand coordination, media coordination, and global coordination. Although the importance of coordination has been widely recognized, it is still re ported by marketers that how to design coordinated advertising plans is one of the major challenges faced by them (McGee 2018). So far, little attention has been paid to prescribing the optimal advertising efforts for the multibrand, multichannel retailer with multimedia advertising campaigns. Taking advantage of the prescriptive ability of our SDE model, we formulate the optimization problem under each coordination strategy. By solving the problem, the retailer can find the optimal advertising expenditure for each unit.

## 10.1. Managerial Implications

Our model allows us to estimate the profits of four coordination strategies under different advertising salesboosting effectiveness and interference parameters. The values of these parameters vary across different retailers. Depending on these parameters, the performances of different coordination strategies can be quite different. Thus, before investing in any coordination strategy, retailers need to evaluate the performance of each coordination strategy and select the optimal strategy based on their advertising effectiveness. To the best of our knowledge, our study is the first to develop a model that can help the multibrand, multichannel retailer tailor the multimedia coordination strategy based on its practical conditions.

This study provided some key insights for managing advertising expenditures in firms with both online and physical sales channels. One insight is “a little knowledge is a dangerous thing.” This phrase, coined by Alexander Pope (1688–1744), was provided to mean that partial knowledge can mislead people into thinking that they are more expert than what they really are, which can lead to mistakes being made. In the context of our study, managers may wrongly believe that some coordination is always better than no coordination. For example, a C-level marketing executive may vigorously promote brand-level coordination in an organization that was doing no coordination. If crosschannel effects are dominant in the markets served by the firm, such brand-level coordination may end up doing more harm than good.

The performances of NC, BC, and MC depend on the magnitudes of the crosschannel and crossbrand sales boosts and interference. Interestingly, we find that NC could be better than BC and MC in some cases. Thus, retailers that are unable or unwilling to do global coordination have to be careful about media or brand coordination because they may hurt the profit relative to noncoordination.

We also found that media coordination can be a very good strategy (comparable with global coordination) if the crossbrand interference effect cancels the crossbrand boosting effect. Conversely, if the crossbrand interference effect is large, brand coordination can be a very good option (comparable with global coordination).

10.2. Limitations and Future Research Directions In this study, we develop our SDE model based on the Vidale–Wolfe model. The literature has proposed a variety of diffusion equation models to capture the evolution process of sales. For example, the Nerlove–Arrow model is another well-established model in prior studies. Depending on the retailers’ characteristics (e.g., the market size of the industry), the best method to model sales evolution may change (Sethi 1977). Thus, it is also meaningful to develop advertising coordination frameworks based on other diffusion equation models to cater to the needs of different retailers.

Our study is not without limitations. In practice, coordination can incur high costs for retailers. We do not consider such costs when modeling the retailer’s profit. By choosing an appropriate format for the coordination costs and incorporating it into the optimization problem, a more comprehensive understanding can be obtained regarding the selection of the coordination strategy. Second, we use aggregated data and analyze the coordination problem at a macro level. It will be interesting if future research can investigate this problem at a micro level using the advertising data on each individual media and individual-level transaction data.

Besides, we consider that each unit uses a constant guess for other units’ decisions. One alternative way is suggested by the theory of reference effects, as mentioned in Section 5; that is, each unit updates its guess at time t + 1 based on other units’ efforts observed at time t. This can lead to interesting questions, like the optimal way to update guesses given the observed efforts. To update the guesses at time t + 1, the unit needs to know other units’ efforts at time t. Such information transmis sion needs to be facilitated by the retailer. This leads to an information design problem for the retailer. Because uncoordinated units myopically maximize their own objectives instead of the retailer’s total profit, is it better for the retailer to truthfully reveal information or manipulate the information? These are fruitful directions worth investigating. Finally, our model of advertising uses a control that depends on the instantaneous sales rate. The assumption of a Markov control simplifies the analysis. However, it is worth exploring models of advertising that depend on the sales rate history, providing a full feedback control or more generally, any control that is adapted to the Wiener term in the stochastic process of the sales rate.

## Endnotes

<sup>1</sup> The sources are https://hmgroup.com/about-us/corporate-govern ance/company-management/ and https://hmgroup.com/about-us/ markets-and-expansion/ (accessed January 15, 2023).

<sup>2</sup> The source is https://www.gapinc.com/en-us/careers (accessed January 15, 2023).

<sup>3</sup> For ease of exposition, we abbreviate $\mu _ { i , j } ( u _ { i , j , t } , u _ { 1 - i , j , t } , u _ { i , 1 - j , t } ,$ $u _ { 1 - i , 1 - j , t } ) \mathrm { b y } \mu _ { i , j }$ when this does not cause any confusion.

## References

Ali F, Young J (2021) U.S. ecommerce grows 44.0% in 2020. Accessed February 2, 2022, https://www.digitalcommerce360.com/article/ us-ecommerce-sales/.

Ansari A, Mela CF, Neslin SA (2008) Customer channel migration. J. Marketing Res. 45(1):60–76.

Assmus G, Farley JU, Lehmann DR (1984) How advertising affects sales: Meta-analysis of econometric results. J. Marketing Res. 21(1):65–74.

Avery J, Steenburgh TJ, Deighton J, Caravella M (2012) Adding bricks to clicks: Predicting the patterns of cross-channel elasticities over time. J. Marketing 76(3):96–111.

Bass FM, Bruce N, Majumdar S, Murthi B (2007) Wearout effects of different advertising themes: A dynamic Bayesian model of the advertising-sales relationship. Marketing Sci. 26(2):179–195.

Bass FM, Krishnamoorthy A, Prasad A, Sethi SP (2005) Advertising competition with market expansion for finite horizon firms. J. Indust. Management Optim. 1(1):1–19.

Basu AK, Batra R (1988) Adsplit: A multi-brand advertising bud get allocation model. J. Advertising 17(2):44–51.

Blustein A (2019) Foot Locker centralizes back-end brand experience with Adobe integration. Accessed February 2, 2022, https:// www.thedrum.com/news/2019/02/15/foot-locker-centralizesback-end-brand-experience-with-adobe-integration.

Breugelmans E, Campo K (2016) Cross-channel effects of price pro motions: An empirical analysis of the multi-channel grocery retail sector. J. Retailing 92(3):333–351.

Choi TM, Liu N (2019) Optimal advertisement budget allocation and coordination in luxury fashion supply chains with multiple brand-tier products. Transportation Res. Part E Logist. Transporta tion Rev. 130(2019):95–107.

Clarke DG (1973) Sales-advertising cross-elasticities and advertising competition. J. Marketing Res. 10(3):250–261.

Cohen MC, Kalas JJ, Perakis G (2021) Promotion optimization for multiple items in supermarkets. Management Sci. 67(4):2340–2364.

Cohen MC, Leung NHZ, Panchamgam K, Perakis G, Smith A (2017) The impact of linear optimization on promotion plan ning. Oper. Res. 65(2):446–468.

Coulter B, Krishnamoorthy S (2014) Pricing strategies with reference effects in competitive industries. Internat. Trans. Oper. Res. 21(2):263–274.

Coyne KP, Horn J (2009) Predicting your competitor’s reaction. Har vard Bus. Rev. 87(4):90–97.

Cui TH, Ghose A, Halaburda H, Iyengar R, Pauwels K, Sriram S, Tucker C, Venkataraman S (2021) Informational challenges in omnichannel marketing: Remedies and future research. J. Mar keting 85(1):103–120.

Danaher PJ, Bonfrer A, Dhar S (2008) The effect of competitive advertising interference on sales for packaged goods. J. Marketing Res. 45(2):211–225.

Danaher PJ, Danaher TS, Smith MS, Loaiza-Maya R (2020) Advertising effectiveness for multiple retailer-brands in a multimedia and multichannel environment. J. Marketing Res. 57(3):445–467.

Deng Y, Zheng J, Khern-am-nuai W, Kannan K (2022) More than the quantity: The value of editorial reviews for a usergenerated content platform. Management Sci. 68(9):6865–6888.

Dinner IM, Heerde Van HJ, Neslin SA (2014) Driving online and off line sales: The cross-channel effects of traditional, online display, and paid search advertising. J. Marketing Res. 51(5): 527–545.

Dong H, Ren J, Padmanabhan B, Nickerson JV (2022) How are social and mass media different in relation to the stock market? A study on topic coverage and predictive value. Inform. Man agement 59(2):103588.

Du RY, Xu L, Wilbur KC (2019) Immediate responses of online brand search and price search to TV ads. J. Marketing 83(4): 81–100.

Facebook (2019) Improving in-store return on ad spend with Facebook conversion lift. Accessed February 2, 2022, https://www. facebook.com/business/success/gina-tricot.

Fischer M, Albers S, Wagner N, Frie M (2011) Dynamic marketing budget allocation across countries, products, and marketing activities. Marketing Sci. 30(4):568–585.

Foot Locker Inc. (2021) Foot Locker Inc. 2020 annual report. Accessed February 2, 2022, https://investors.footlocker-inc.com/static-files df07b24b-6630-42ac-93fd-5c5dce0efec8.

Forman C, Ghose A, Goldfarb A (2009) Competition between local and electronic markets: How the benefit of buying online depends on where you live. Management Sci. 55(1):47–57.

Franke M (2019) How to market in a multi-brand organization. Accessed February 2, 2022, https://www.epsilon.com/us/insights/blog/howto-market-in-a-multi-brand-organization

Gap Inc. (2020) Gap Inc. 2020 annual report. Accessed February 2, 2022, https://s24.q4cdn.com/508879282/files/doc\_financials/ 2020/ar/Gap-Inc.-10-K-FY2020\_FINAL\_print-version.pdf.

Gap Inc. (2021) Gap Inc. quarterly report for the quarterly period ended October 30, 2021. Accessed February 2, 2022, https://s24. q4cdn.com/508879282/files/doc\_financials/2021/q3/ca222f63- 5f53-4d7f-8724-8bf5579489b1.pdf.

Garnefeld I, Helm S, Eggert A (2011) Walk your talk: An experimental investigation of the relationship between word of mouth and communicators’ loyalty. J. Service Res. 14(1):93–107.

Gauri DK, Bhatnagar A, Rao R (2008) Role of word of mouth in online store loyalty. Comm. ACM 51(3):89–91.

Ghose A, Yang S (2009) An empirical analysis of search engine advertising: Sponsored search in electronic markets. Management Sci. 55(10):1605–1622.

Gleason D (2018) Google Analytics 360: The features worth \$150k a year. Accessed February 2, 2022, https://cxl.com/blog/google analytics-360/.

Golan E (2018) The U.S. jewelry market is much smaller than you think. Accessed February 2, 2022, https://www.edahngolan. com/jewelry-market-is-much-smaller-than-you-think/.

Guitart IA, Hervet G, Gelper S (2019) Competitive advertising strategies for programmatic television. J. Acad. Marketing Sci. 48(4): 753–775.

H&M (2020) H&M Group 2020 annual report. Accessed February 2, 2022, https://hmgroup.com/wp-content/uploads/2021/04/HM-Annual-Report-2020.pdf

Hu T, Tripathi A, Berkman H (2019) The value of free content on social media: Evidence from equity research platforms. Lang KR, Xu J, Zhu B, Liu X, Shaw MJ, Zhang H, Fan M, eds. 18th Workshop e-Business WeB 2019 (Springer, Munich, Germany), 123–130.

Jordan R, Kinderlehrer D, Otto F (1998) The variational formulation of the Fokker–Planck equation. SIAM J. Math. Anal. 29(1):1–17.

Junior ECSS (2018) Brand portfolio strategy and brand architecture: A comparative study. Cogent Bus. Management 5(1):1483465.

Keller E, Fay B (2012) Word-of-mouth advocacy: A new key to advertising effectiveness. J. Advertising Res. 52(4):459–464.

Kim G, Moon I (2020) Online banner advertisement scheduling for advertising effectiveness. Comput. Indust. Engrg. 140(2020):106226.

Kirshner SN, Ovchinnikov A (2019) Heterogeneity of reference effects in the competitive newsvendor problem. Manufacturing Service Oper. Management 21(3):571–581.

Kollmann T, Kuckertz A, Kayser I (2012) Cannibalization or syn ergy? Consumers’ channel selection in online–offline multichan nel systems. J. Retailing Consumer Services 19(2):186–194.

Lehojarvi E (2021) Build the ultimate branding tech stack. Accessed February 2, 2022, https://www.business2community.com/techgadgets/build-the-ultimate-branding-tech-stack-02390081.

Lesscher L, Lobschat L, Verhoef PC (2020) Do offline and online go hand in hand? Cross-channel and synergy effects of direct mailing and display advertising. Internat. J. Res. Marketing 38(3):678–697.

Lewis RA, Reiley DH (2014) Online ads and offline sales: Measuring the effect of retail advertising via a controlled experiment on Yahoo! Quant. Marketing Econom. 12(3):235–266.

Little JD (1979) Aggregate advertising models: The state of the art. Oper. Res. 27(4):629–667.

Liu X, Wang GA, Fan W, Zhang Z (2020) Finding useful solutions in online knowledge communities: A theory-driven design and multilevel analysis. Inform. Systems Res. 31(3):731–752.

Manchanda P, Dube ´ JP, Goh KY, Chintagunta PK (2006) The effect of banner advertising on Internet purchasing. J. Marketing Res. 43(1):98–108.

McGee T (2018) Omnichannel marketing chart: The biggest chal lenges to marketers’ omnichannel strategies. Accessed February 2, 2022, https://marketingsherpa.com/article/chart/challenges to-omnichannel-strategies.

McGeoch JA (1932) Forgetting and the law of disuse. Psych. Rev. 39(4):352–370.

Naik PA, Peters K (2009) A hierarchical marketing communications model of online and offline media synergies. J. Interactive Mar keting 23(4):288–299.

Neslin SA, Grewal D, Leghorn R, Shankar V, Teerling ML, Thomas JS, Verhoef PC (2006) Challenges and opportunities in multi channel customer management. J. Service Res. 9(2):95–112.

Nielsen (2020) Digital and omnichannel sweet spots for auto advertisers. Accessed February 2, 2022, https://www.nielsen.com/ us/en/insights/article/2020/digital-and-omnichannel-sweetspots-for-auto-advertisers/.

Nielsen (2021) It’s time for brands to rethink their omnichannel strategies. Accessed January 25, 2023, https://www.nielsen. com/insights/2021/its-time-for-brands-to-rethink-their-omni channel-strategies/.

O’Kane C (2010) Average online CPMs still lagging behind other media. Accessed February 2, 2022, https://www.exchangewire.com/blog 2010/06/15/average-online-cpms-still-lagging-behind-other-media/.

Osinga EC, Zevenbergen M, van Zuijlen MW (2019) Do mobile banner ads increase sales? Yes, in the offline channel. Internat. J. Res. Marketing 36(3):439–453.

Prasad A, Sethi SP (2004) Competitive advertising under uncertainty: A stochastic differential game approach. J. Optim. Theory Appl. 123(1):163–185.

Pu J, Chen Y, Qiu L, Cheng HK (2020) Does identity disclosure help or hurt user content generation? Social presence, inhibition, and displacement effects. Inform. Systems Res. 31(2):297–322.

Rao RC (1986) Estimating continuous time advertising-sales models. Marketing Sci. 5(2):125–142.

Safdar K (2019) Gap to split into two public companies. Accessed February 2, 2022, https://www.wsj.com/articles/gap-to-splitinto-two-publicly-traded-companies-11551389463.

Sahni NS (2016) Advertising spillovers: Evidence from online field experiments and implications for returns on advertising. J. Mar keting Res. 53(4):459–478.

Sethi SP (1977) Dynamic optimal control models in advertising: A survey. SIAM Rev. 19(4):685–725.

Sethi SP (1983) Deterministic and stochastic optimization of a dynamic advertising model. Optimal Control Appl. Methods 4(2):179–184.

Shapiro BT (2018) Positive spillovers and free riding in advertising of prescription pharmaceuticals: The case of antidepressants. J. Political Econom. 126(1):381–437.

Shriver SK, Bollinger B (2022) Demand expansion and cannibalization effects from retail store entry: A structural analysis of mul tichannel demand. Management Sci. 68(12):8829–8856.

Square Inc. (2020) 6 tips for omnichannel marketing success. Accessed February 2, 2022, https://www.forbes.com/sites/square/2020/ 12/10/6-tips-for-omnichannel-marketing-success.

Sun C, Adamopoulos P, Ghose A, Luo X (2022) Predicting stages in omnichannel path to purchase: A deep learning model. Inform. Systems Res. 33(2):429–445.

Tagashira T, Minami C (2019) The effect of cross-channel integration on cost efficiency. J. Interactive Marketing 47(1):68–83.

Tellis GJ, Weiss DL (1995) Does TV advertising really affect sales? The role of measures, models, and data aggregation. J. Advertising 24(3):1–12.

Todri V, Ghose A, Singh PV (2020) Trade-offs in online advertising Advertising effectiveness and annoyance dynamics across the purchase funnel. Inform. Systems Res. 31(1):102–125

U.S. Census Bureau (2021) Quarterly retail e-commerce sales for the 3rd quarter 2021. Accessed February 2, 2022, https://www2. census.gov/retail/releases/historical/ecomm/21q3.pdf.

Vanhonacker WR (1983) Carryover effects and temporal aggregation in a partial adjustment model framework. Marketing Sci. 2(3):297–317.

Vidale M, Wolfe H (1957) An operations-research study of sale response to advertising. Oper. Res. 5(3):370–381.

Wang X, Li P, Hawbani A (2018) An efficient budget allocation algorithm for multi-channel advertising. Liu C, Chellappa R, Pietikainen M, eds. Proc. 24th Internat. Conf. Pattern Recognition (IEEE, Piscataway, NJ), 886–891.

Wiesel T, Pauwels K, Arts J (2011) Practice prize paper-marketing’s profit impact: Quantifying online and off-line funnel progression. Marketing Sci. 30(4):604–611.

Woodside AG, Waddle GL (1975) Sales effects of in-store advertising. J. Advertising Res. 15(3):29–33.

Yang M, Zheng Z, Mookerjee V (2019) Prescribing response strategies to manage customer opinions: A stochastic differential equation approach. Inform. Systems Res. 30(2):351–374.

Yang Y, Feng B, Salminen J, Jansen BJ (2022) Optimal advertising for a generalized Vidale–Wolfe response model. Electronic Commerce Res. 22(2022):1275–1305.

Yucelt U, Kaynak E (1984) A study of measuring influence of advertising and forecasting cigarette sales. Managerial Decision Econom. 5(4):213–218.

Zacks Equity Research (2021) Foot Locker (FL) shines: Omni-channel efforts boost growth. Accessed February 2, 2022, https://www. nasdaq.com/articles/foot-locker-fl-shines%3A-omni-channelefforts-boost-growth-2021-01-21.

Zhang J, Chiang Wy K, Liang L (2014) Strategic pricing with reference effects in a competitive supply chain. Omega 44(2014): 126–135.

C<sub>opy</sub>ri<sub>g</sub>ht 2024 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
