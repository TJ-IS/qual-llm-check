---
otero_id: 26873
otero_key: "EM976JN4"
title: "Paid Search Marketing vs. Search Engine Optimization: Analytical Models of Search Marketing Based on Search Engine Quality"
authors: "Kai Li; Chunyang Shen; Mei Lin; Zhangxi Lin"
year: "2026"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00961"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
2026

# Paid Search Marketing vs. Search Engine Optimization: Analytical Models of Search Marketing Based on Search Engine Quality

Kai Li , likai@nankai.edu.cn

Chunyang Shen , shenchunyang@mail.nankai.edu.cn

Mei Lin , mlin@smu.edu.sg

Zhangxi Lin , zhangxi.lin@ttu.edu

Follow this and additional works at: https://aisel.aisnet.org/jais

# Paid Search Marketing vs. Search Engine Optimization: Analytical Models of Search Marketing Based on Search Engine Quality

Kai Li,<sup>1</sup> Chunyang Shen,<sup>2</sup> Mei Lin,<sup>3</sup> Zhangxi Lin<sup>4</sup>

<sup>1</sup>Business School, Nankai University, China, likai@nankai.edu.cn

<sup>2</sup>Business School, Nankai University, China, shenchunyang@mail.nankai.edu.cn

<sup>3</sup>School of Information Systems, Singapore Management University, Singapore, mlin@smu.edu.sg <sup>4</sup>Jerry S. Rawls College of Business Administration, Texas Tech University, USA, Zhangxi.lin@ttu.edu

## Abstract

As search engines are leading revenue growth in online marketing, search marketing has become a popular area of academic research. Although search engine advertising has interested researchers for decades and much has been learned, one thing that puzzles scholars is why search engine optimization companies are tolerated rather than excluded from the market, even though they capture a significant share of the advertising market. In this paper, we shed light on this phenomenon and establish an analytical model based on organic search quality. Through analysis of the model, we were able to draw several intriguing conclusions. First, there is no strictly positive correlation between advertisers’ willingness to pay and the click price of paid search marketing. In other words, the click price may decrease as advertisers’ willingness to pay increases. Secondly, improving the effectiveness of a search engine has the potential to attract more searchers, but it may also result in a decline in the search engine’s profits. Finally, a search engine may achieve higher profits by allowing search engine optimization firms to remain in the market rather than driving them out. We discuss our contribution to search engine marketing and provide implications for search engines, search engine optimization firms, and advertisers.

Keywords: Search Engine, Search Engine Advertising, Search Engine Optimization, Paid Search Marketing

Kim Huat Goh was the accepting senior editor. This research article was submitted on June 16, 2024, and underwent two revisions. Chunyang Shen is the corresponding author.

## 1 Introduction

With the exponential growth of information available on digital platforms, search engines (SEs) have become popular among users due to their highly efficient information-matching capabilities (Ghose et al., 2019). They have gradually become a primary tool for users interested in obtaining information and discovering new websites (Agarwal et al., 2015; Compiani et al., 2024; Erdmann et al., 2022; Yang et al., 2022). Google, for example, processes approximately 3.5 billion searches per day, and in 2023, it recorded 84.2 billion monthly visits, with 63.41% of U.S. web traffic referrals originating from Google (Ong, 2024). Search engine marketing (SEM), now one of the most popular forms of advertising, has experienced substantial growth (Chen, 2021; Donnelly et al., 2024; Gong et al., 2018; Kannan et al., 2022), surpassing traditional advertising models and establishing dominance in the digital advertising market. In 2023, search advertising revenue increased by 5.2% year over year, reaching \$88.8 billion and accounting for 39.5% of digital ad market revenue (IAB, 2024). Notably, Google Ads revenue grew from \$7 million in 2001 to \$23.786 billion in 2023 (Statista, 2025). Today, SEs are essential channels for the promotion of e-commerce websites (Agarwal et al., 2015; Long et al., 2022; Yang et al., 2020; Zhuang et al., 2021), and SEM has firmly established itself as a core component of corporate marketing strategies (Joo et al., 2024; Yang et al., 2024).

The effectiveness of an SE primarily relies on its capability to identify valuable webpages.<sup>1</sup> given that each SE indexes only a fraction of the internet’s content (Gong et al., 2018; Liu et al., 2010). Limited by cognitive and temporal constraints (Ghose et al., 2019; Lee & Hosanagar, 2019; Ursu, 2018), users attention diminishes exponentially with lower-ranking results, indicating that most users focus primarily on top-ranked results (Jin et al., 2022; Schultheiß & Lewandowski, 2020; Ursu et al., 2023). Therefore, more prominent, higher search engine rankings enable advertisers to capture increased user attention, leading to greater traffic (Jin et al., 2022; Kim & Balachander, 2023; Schultheiß & Lewandowski, 2020; Tunuguntla et al., 2023).

To enhance webpage rankings, advertisers may select from two primary strategies. The first approach, paid search marketing (PSM), is offered by SEs such as Google and Yahoo!, where sponsored advertisements are positioned in specific areas on the search results page, alongside organic search results, as illustrated in Figure 1. In PSM, the costs borne by advertisers are determined through keyword auction prices (Erdmann et al., 2022; Gong et al., 2018; Kannan et al., 2022; Kim & Balachander, 2023; Yang et al., 2022). The second strategy, search engine optimization (SEO), is provided by third-party companies, such as SEO Inc., which charge for optimizing particular keywords to enhance a webpage’s ranking in organic search results and thereby increase traffic (Edelman & Lai, 2016; Erdmann et al., 2022; Katona & Sarvary, 2010; Nagpal & Petersen, 2021).

Compared to PSM, SEO functions as an unofficial service offered by numerous small SEO firms. These firms, acting as secondary service providers affiliated with SEs, may confer certain advantages, such as being perceived as delivering more objective and impartial results that increase user engagement (Agarwal et al., 2015; Erdmann et al., 2022). Nonetheless, they also face considerable survival pressures. On the one hand, SEO is not only complex and time-intensive (Reisenbichler et al., 2022) but also costly (Erdmann et al., 2022), with outcomes that are often unpredictable (Berman & Katona, 2013). Considering that advertisers can easily “purchase” search rankings through paid means, choosing SEO in the face of uncertainties does not seem to be a prudent decision. On the other hand, SEO companies frequently encounter resistance from dominant SEs due to the potential adverse effects of SEO on the quality of organic links (Agarwal et al., 2015; Berman & Katona, 2013; Chiou & Tucker, 2022). SEO firms provide optimization services by analyzing and utilizing search engine algorithms; however, excessive techniques such as keyword stuffing and content rewriting may compromise the quality and accuracy of search results (Aswani et al., 2018; Baeza-Yates, 2018). Algorithms play a critical role in the retrieval performance of SEs; therefore, to mitigate the effects of SEO, SEs must regularly modify and update their algorithms. Since 2007, SEs have begun incorporating various undisclosed factors into their ranking algorithms to ensure the fairness of search results. According to Google, its algorithm includes more than 200 signals to determine website rankings,<sup>2</sup> and as of 2022, Google was implementing 500-600 algorithm changes per year—almost 1.5 times per day (Galov, 2025).

The presence of SEO increases the pressure on SEs to continually update their algorithms and captures market share from PSM, negatively affecting SEs’ advertising revenue. Despite SEs’ dominant market position, SEO companies continue to thrive within the SEM sector. The SEO market is projected to reach \$122.11 billion by 2028, with a compound annual growth rate (CAGR) of 9.6% (Hartzer, 2022). This trend prompts significant questions regarding the survival prospects of SEO companies and their relationship with SEs. Key research questions include: Why do SEO companies persist in a market dominated by SEs? Under what conditions can SEO firms remain viable? What factors influence the dynamic competition between SEO and SEs? Although SEM has been widely studied, research specifically examining the relationship between SEO and PSM remains limited, even though it is crucial for both SEs and SEO companies because they share revenue from the search advertising market. A comprehensive investigation into these issues could provide managers from both sides with insights for making more strategic, forward-looking decisions.<sup>3</sup>

![](/api/attachments/EM976JN4/fulltext/images/a8179f6d7c79569e96c6a0504306af7215a20795194e383c713aca00a44b0505.jpg)  
Figure 1. Sponsored Ads and Organic Search Results on Google

To address these issues, this study applied a game theory model to analyze the competitive dynamics between PSM and SEO, examining the impact of SEO on the search engine advertising market. Several noteworthy findings emerged. Firstly, SEO firms do not inherently diminish the optimal profits of SEs. While SEO firms may capture a share of the SEM, their presence simultaneously motivates SEs to refine their strategies. For example, SEs may boost their competitiveness by reducing PSM prices or enhancing the effectiveness of search algorithms. If these optimizations effectively maintain the SE’s market dominance and drive the overall expansion of the SEM, thereby creating a mutually beneficial relationship between SEs and SEO firms, then SEO firms can coexist within the SEM market. Secondly, the study defines the conditions under which SEO firms can survive, finding that factors such as search engine effectiveness, robustness, and advertisers’ willingness to pay critically affect SEO firms’ viability. These factors directly influence the competitive landscape, thereby affecting the revenues of both SEO firms and the SE. Furthermore, the study reveals that the relationship between an SE’s effectiveness and its optimal profit is not always straightforward; while higher effectiveness may increase revenue, it also enhances SEO firms’ profitability, intensifying competition within the SE’s ecosystem.

This study makes four major contributions. This study enhances the theoretical understanding of the relationship between SEO and PSM, offering a novel perspective on the positive role of SEO within the SEM. The paper investigates the competitive dynamics between SEO and PSM in the SEM, revealing that their competition can effectively lower advertising costs for marketers and consequently expand the SEM market. This, in turn, will positively impact the overall market.

Secondly, this study makes a significant contribution to SEO literature by elucidating the mechanisms through which SEO companies maintain their presence in an SEdominated competitive environment. Specifically, the research demonstrates that the existence of SEO forces dominant SEs to make more optimized decisions, such as reducing PSM prices and improving the effectiveness of search engine algorithms, thereby enhancing their profitability. This paper identifies the key factors enabling SEO to thrive in an SE-dominated market, enriching the academic literature and providing valuable insights for both theoretical research and practical applications in SEO.

Additionally, this paper makes a significant contribution to the literature on SEM, enhancing the existing knowledge in the field. On the one hand, it offers an in-depth analysis of emerging trends in the SEM market, focusing on the integration of AI large models with SEs and the impact of mobile SEs on SEM, thus addressing a gap in current research. Furthermore, from a quality perspective, the paper investigates two key attributes of search engine algorithms—effectiveness and robustness—and assesses their influence on SEO company survival, search engine decision-making, and profitability. This work provides novel research insights and directions for future studies in the SEM field.

Moreover, this paper also contributes to the literature on platform economics by developing an optimal decisionmaking model for search engine platforms, offering a novel perspective on the theoretical development of the field. As noted by Zhong (2023), search functionality is essential to online platforms, and search management is a key issue in platform decision-making. The analysis of the competitive relationship between SEO and PSM enhances the understanding of platform strategic decision-making, carries significant practical implications, and provides a theoretical foundation for decision-making in related fields.

The structure of the article is as follows: Section 2 provides an introduction to the background of internet SEs and reviews the relevant literature. Section 3 presents a framework for search engine quality and develops the model used for analysis in this study. Section 4 analyzes the conclusions of the basic model. Section 5 focuses on emerging trends in the SEM market and extends the baseline model along multiple dimensions to verify the robustness of the core conclusions. Finally, Sections 6 and 7 summarize the key findings of the model and provide an in-depth discussion of its managerial implications. Additionally, we highlight the limitations of this study and propose directions for future research.

## 2 Literature Review

The rapid growth of search engine marketing has attracted substantial academic interest (Agarwal et al., 2015; Donnelly et al., 2024; Tunuguntla et al., 2023; Yang & Ghose, 2010; Yang et al., 2022). Unlike traditional marketing models, search engine marketing is directly associated with users’ search behaviors, enabling advertisers to present highly relevant ads to internet users in a minimally intrusive manner, effectively reducing users’ search costs (Lee & Hosanagar, 2019; Liu et al., 2010; Ursu, 2018; Yang & Ghose, 2010). Furthermore, search engine marketing allows advertisers to precisely target potential users and addresses the “cold start” problem (Gong et al., 2018; Nie et al., 2021; Tunuguntla et al., 2023; Yang et al., 2024), positioning it as a central aspect of modern corporate advertising strategies and a subject of extensive academic inquiry. Search engine marketing consists primarily of two forms: search engine optimization (SEO) and paid search marketing (PSM), both of which are closely aligned with the primary literature streams relevant to this study.

SEO entails modifying the technical elements of a website, such as content, design, and keywords, to improve its organic ranking and enhance website traffic (Erdmann et al., 2022; Liu & Toubia, 2018; Nagpal & Petersen, 2021). SEO is a crucial component of advertisers’ search engine marketing strategies (Long et al., 2022; Nagpal & Petersen, 2021). While research on search engine marketing has predominantly focused on PSM, relatively few studies have examined SEO (Aswani et al., 2018; Nagpal &

Petersen, 2021; Zhang & Cabage, 2017), with most of the existing work emphasizing technical explanations and optimization strategies. Malaga (2008) categorized SEO techniques into two approaches: black-hat and white-hat. Black-hat techniques manipulate ranking by exploiting algorithm vulnerabilities, which increases “noise” in online content and presents challenges for SEs (Aswani et al., 2018). Conversely, white-hat techniques focus on optimizing advertisers’websites in accordance with search engine guidelines (Moreno & Martinez, 2013). Common SEO practices include ranking algorithm design and optimization (Garcia et al., 2022), anti-spam tactics (Ju et al., 2021), keyword selection (Erdmann et al., 2022), article spinning, link building, and link farms (Aswani et al., 2018). SEO is essential for attaining high organic search rankings (Erdmann et al., 2022), with organic results more likely to capture users’ attention and clicks (Agarwal et al., 2015; Joo et al., 2024). However, several scholars have highlighted SEO’s limitations. Berman and Katona (2013) noted that SEO services often require upfront payment from advertisers, yet their effectiveness may not be immediately evident and carries significant uncertainty. Reisenbichler et al. (2022) further asserted that SEO depends heavily on professional expertise, involves substantial investment, and is subject to frequent algorithm updates, which introduce considerable uncertainty regarding SEO investment outcomes.

PSM, also known as sponsored advertising or sponsored links, is a form of paid advertising conducted through bidbased tools provided by SEs, allowing websites to be positioned prominently in search results (Erdmann et al., 2022). Advertisers pay only when users click on the advertisement and visit the corresponding website (Agarwal et al., 2015; Chen, 2021; Yang et al., 2020). Compared to SEO, PSM has garnered significant academic attention due to its distinct advantages (Chen, 2021; Kannan et al., 2022; Kim & Balachander, 2023; Long et al., 2022; Nie et al., 2021; Tunuguntla et al., 2023; Yang et al., 2020, 2024). According to Zhang and Feng (2011), sponsored search—one of the internet’s most successful advertising models—enables advertisers to dynamically adjust bids and rankings, allowing for realtime returns. Berman and Katona (2013) pointed out that sponsored links operate on a pay-per-click basis, eliminating the need for advertisers to make upfront investments while providing predictable outcomes. Long et al. (2022) argued that, compared to organic listings, sponsored ads are product-oriented, which not only generates revenue for the platform but also serves a crucial informational role by revealing advertisers’ private information. Likewise, Yang et al. (2024) noted that sponsored links can signal unobservable product quality to search users. Additional research has analyzed various stages in the PSM process, including auction mechanism design (Chen, 2021; Liu et al., 2010; Long et al., 2022), keyword selection (Gong et al., 2018; Tunuguntla et al., 2023), bidding behavior in keyword auctions (Katona & Sarvary, 2010; Yang et al., 2020), competitive dynamics in keyword auctions (Nie et al., 2021), and the impact of sponsored ads on user behavior and sales (Chiou & Tucker, 2022; Schultheiß & Lewandowski, 2020; Yang et al., 2022; Zhuang et al., 2021).

SEO and PSM exhibit considerable overlap in marketing effectiveness, resulting in inevitable competition between the two (Berman & Katona, 2013; Katona & Sarvary, 2010; Reisenbichler et al., 2022). This rivalry has prompted scholars to investigate the interactions between organic and sponsored links (Berman & Katona, 2013; Long et al., 2022; Yang et al., 2024; Yang & Ghose, 2010). Some studies have focused on the substitutive effects between organic search results and sponsored ads (Agarwal et al., 2015; Blake et al., 2015; Chiou & Tucker, 2022; Joo et al., 2024). For instance, Chiou and Tucker (2022) analyzed consumer behavior on major SEs, revealing that sponsored listings and organic results act as substitutes when consumers search for brand names, given that their primary goal is navigation. Joo et al. (2024) examined how ranking positions affect competition between organic and sponsored listings, finding that higher-ranked organic listings have a distinct advantage over sponsored ones for experiential goods, although this advantage declines at lower ranks. Similarly, Blake et al. (2015) conducted large-scale field experiments on eBay, demonstrating the near-complete substitutability between paid and unpaid traffic. Other scholars have focused on the complementary effects between organic and sponsored links (Berman & Katona, 2013; Long et al., 2022; Xu et al., 2012; Yang et al., 2024; Yang & Ghose, 2010). Long et al. (2022), Xu et al. (2012), and Yang et al. (2024) examined the informational role of both sponsored and organic links in decision-making. Specifically, bids for sponsored links can reveal advertisers’private information, assisting platforms in enhancing organic links. Similarly, organic listings can serve as an information source that influences bidding behavior in sponsored links, helping advertisers achieve more favorable bidding positions and ultimately affecting the outcomes of sponsored listings.

In contrast to previous research, this paper explores the competition between SEO and PSM, an area that warrants further research in the academic literature.<sup>4</sup> This study is distinct from studies on the competition between sponsored links and organic search results. Existing studies generally focus on the interaction between sponsored links and organic search results on search engine results pages, primarily from the perspectives of users or advertisers. These studies have investigated the mutual effects of these factors on click-through rates, conversion rates, and brand appeal. As illustrated in Table 1, this research diverges from existing studies in several significant ways. First, the interaction between SEO and PSM is fundamentally different from the interaction between organic search and sponsored links. The competitive and cooperative relationship between organic search and sponsored links primarily affects the way advertisers acquire traffic, while the interaction between SEO and PSM is more complex. On the one hand, the competition between SEO and PSM is influenced not only by factors such as search ranking, click-through rate, and conversion rate but also by the SE’s pricing decisions for PSM and the strategic interactions among multiple stakeholders in the SEM market. On the other hand, SEO is not the only way to achieve organic rankings. Therefore, the conclusions drawn from studies on the competition between organic search and sponsored links cannot be directly applied to the competition between SEO and PSM. Second, existing research has overlooked a crucial factor—the dominant position of SEs in the SEM market, which enables them to determine the survival of SEO firms. Even though sponsored links and organic search results are complementary from the perspectives of advertisers or visitors, this relationship alone does not guarantee the survival of SEO firms. As demonstrated by Berman and Katona (2013) and Agarwal et al. (2015), a complementary relationship does exist between sponsored and organic links. However, these studies failed to address the role of SEs as market leaders. SEs not only control the effectiveness of algorithms but also significantly influence ad display and matching mechanisms. This dominant role is key to shaping the competitive dynamics between SEO and PSM. Moreover, the existing literature has yet to explain why SEO firms continue to thrive in the market, which constitutes a central research question of this paper.

## 3 Model

Existing literature on the search engine advertising market is insufficient for explaining the effect of SEO because it primarily associates organic search quality with user satisfaction. Additionally, clients face a tradeoff between quality and cost when choosing between two competing search engine market services.

## 3.1 Search Quality

The concept of quality has been traditionally defined across many disciplines (Leffler, 1982). In research on the search engine market, quality evaluation is primarily conducted from the perspective of users. This quality dimension encompasses SEs’professional knowledge in meeting searchers’ information needs, including “crawling and indexing algorithms, database indexing, and search and retrieval algorithms” (Bhargava & Feng, 2005). In this paper, we refer to this quality dimension as algorithm effectiveness. Higher effectiveness leads to greater satisfaction and increased demand in the search market (Gong et al., 2018; Telang et al., 2004).

Table 1. Comparison of Our Study with Prior Studies

<table><tr><td>Reference</td><td>Research subject</td><td>Perspective</td><td>Key mechanism</td><td>SEO</td><td>PSM</td><td>Impact on SE</td></tr><tr><td>Yang &amp; Ghose, 2010</td><td>Search advertising</td><td>Advertiser</td><td>CTR</td><td></td><td>√</td><td></td></tr><tr><td>Xu et al., 2012</td><td>Ads’ bidding strategies</td><td>Advertiser</td><td>Firms’ market appeal</td><td></td><td>√</td><td></td></tr><tr><td>Berman &amp; Katona, 2013</td><td>Ad’s decision</td><td>Advertiser</td><td>Visitor satisfaction</td><td>√</td><td></td><td>√</td></tr><tr><td>Agarwal et al., 2015</td><td>Ads’ PSM performance</td><td>Advertiser</td><td>CTR and conversion rate</td><td></td><td>√</td><td></td></tr><tr><td>Aswani et al., 2018</td><td>Negative impacts of SEO</td><td>Advertiser</td><td>Customer satisfaction</td><td>√</td><td></td><td></td></tr><tr><td>Long et al., 2022</td><td>Online retail market</td><td>Sellers</td><td>Asymmetric information</td><td></td><td>√</td><td></td></tr><tr><td>Yang et al., 2024</td><td>Ranking of search listings</td><td>Search platform</td><td>Product quality information</td><td></td><td></td><td>√</td></tr><tr><td>Joo et al., 2024</td><td>Sponsored product listings</td><td>Sellers</td><td>CTR and conversion rate</td><td></td><td>√</td><td></td></tr><tr><td>This work</td><td>Search algorithms</td><td>SE</td><td>Characteristics of search algorithms</td><td>√</td><td>√</td><td>√</td></tr></table>

Table 2. The Difference Between Robustness and Effectiveness

<table><tr><td></td><td>Effectiveness</td><td>Robustness</td></tr><tr><td>Objective</td><td>Deliver search results that align precisely with user intent to meet their needs.</td><td>To reduce SEO and third-party optimization interference, ensure search quality by blocking low-quality or irrelevant content.</td></tr><tr><td>Relation to SE updates</td><td>Focuses on core algorithm optimization aimed at enhancing user experience. Updates occur relatively infrequently and require a significant investment of resources.</td><td>Relies on dynamic algorithm adjustments with frequent updates to address rapid advancements in SEO techniques and prevent algorithm exploitation for ranking manipulation.</td></tr><tr><td>Challenges</td><td>Require precise interpretation of user intent and effective matching of relevant content through algorithms.</td><td>Involves identifying and countering external interference (e.g., SEO manipulation) to maintain the quality of search results and ensure stability in adversarial scenarios.</td></tr><tr><td>Impact</td><td>Directly affects user search experience and preference for the SE, influencing its competitiveness, traffic, and market share.</td><td>Impact of algorithms on resistance to external manipulation and the cost of SEO firms manipulating rankings, while maintaining the credibility and fairness of SEs.</td></tr><tr><td>Revenue model</td><td>Directly enhances the user base and traffic, thereby generating higher revenue.</td><td>Indirectly affects the SE&#x27;s reputation, user trust, and platform fairness, which in turn influences profitability.</td></tr><tr><td>Evaluation metrics</td><td>Click-through rate, page dwell time, user satisfaction, and other metrics to assess whether search results meet user needs.</td><td>Ranking stability, noise reduction rate, and ranking fluctuation rate, among other metrics, to evaluate the SE&#x27;s stability and resistance in complex environments.</td></tr></table>

In the search engine advertising market, SEs aim to rank pages unbiasedly based on relevance standards (Xing & Lin, 2006), while SEO can introduce noise, weakening their influence (Aswani et al., 2018). The existence of SEO distinguishes the noise-handling capability of SEs. Stronger noise-handling capability reduces the negative impact of SEO, referred to as the algorithm’s robustness. As an SE’s algorithmic robustness improves, SEO firms need to invest more effort into optimization, leading to higher costs for webpage ranking optimization. In other words, algorithmic robustness can be seen as the “inverse quality” of SEO companies.

Generally, SE effectiveness primarily affects user satisfaction, which is largely influenced by the initial investment in the SE. For instance, Google’s core ranking algorithm is based on PageRank,<sup>5</sup> which is a patented information retrieval technology that Google applied for at the time of its inception. On the other hand, SE robustness mainly affects the difficulty of providing SEO services, driven by dynamic competition between SEs and SEO companies as both continuously learn and improve. Table 2 summarizes the differences between the robustness and effectiveness of SEs. In the base model, effectiveness and robustness are assumed to be independent. However, in Section 5.3, we explore their potential interdependence. The results remain robust, suggesting that this interdependence does not significantly affect the model’s conclusions. In the next section, we provide a detailed introduction to the model proposed in this article.

## 3.2 Setting

Suppose there is one SE and many SEO firms in the market for a period, both offering advertising services. In Appendix $\mathrm { C } ,$ Section C6, we extend the basic model to consider the scenario where competition exists among SEs. Let $q _ { e }$ denote the algorithm effectiveness (userbased quality) and $q _ { r }$ algorithm robustness (SEO-based quality) of the SE. Besides the SE and SEO firms, the market also includes advertisers and searchers. Advertisers differ in their conversion rate (the ratio of sales to advertising clicks) and their valuation of the keyword, both of which can be represented by the random variable ??, indicating the willingness to pay for online advertisement. For simplicity, assume ?? follows a uniform distribution over the interval [0, V].

The demand for the SE, denoted as ??, is defined as the total number of searchers expected to click on either organic or sponsored results during a certain period. Since searchers do not pay a fee to the SE, we propose that searcher demand is solely influenced by the quality of the search experience, represented by $q _ { e }$ . We describe the relationship between searcher demand and algorithm effectiveness with the function $D ( q _ { e } ) = \alpha q _ { e } ,$ , where ?? is a positive slope. This linear assumption simplifies the mathematical expressions and is widely used in existing literature, discussing keyword auctions (Chen et al., 2009; Liu et al., 2010).

To analyze advertisers’ problems, we assume they possess perfect knowledge of the payoffs associated with both types of advertisements, acquired through learning and experience. This assumption is justified, as advertisers can utilize advanced technologies to regularly track link referral effectiveness and calculate the profit per referred customer. Consistent with the keyword auction settings (Chen et al., 2009; Liu et al., 2010; Sambhara et al., 2017; Xu et al., 2011), the market clearing price of the per-click fee $p _ { S E }$ charged by the SE is determined by keyword auctions. Advertisers can choose between SEO and PSM to improve their webpage ranking, with differing click-through rates for organic and sponsored results. We denote them as $r _ { o }$ and $r _ { s }$ respectively, with $r _ { o }$ typically being greater than $r _ { s }$ (Ghose & Yang, 2009). The payoff for advertisers, denoted by ??, is positively correlated with the size of the searchers, aligning with the concept of indirect network externality (Basu et al., 2003; Gupta et al., 1999).

In this context, the advertiser’s payoff from PSM depends on the size of the searcher pool of the engine. Specifically, it equals the total advertising value from sponsored links minus the total cost. The number of users arriving at the SE in a period is $\alpha q _ { e }$ . For advertisers, each click-through generates a net payoff, which is the difference between the value of a clickthrough and its cost $( v - p )$ . In the equation, the net payoff from sponsored links, $u _ { 1 }$ , is:

$$
u _ {1} = \alpha q _ {e} r _ {s} (v - p)\tag{1}
$$

Let $u _ { 2 }$ denote the net payoff from SEO, which equals the payoff from organic results per period minus the SEO fee. Unlike in Equation (1), advertisers pay $f ,$ a lump sum fee per period. The equation is:

$$
u _ {2} = \alpha q _ {e} r _ {o} v - f
$$

Assuming perfect competition in the SEO market, the optimization of search results offered by SEO firms is considered to be homogeneous across firms, industries, and keywords. Thus, the price of SEO firms, denoted as $f ,$ , is influenced by the algorithm robustness $q _ { r }$ . The SEO fee is assumed to be a strictly increasing function of $q _ { r }$ implying that the price of SEO firms is $\beta q _ { r }$ . Here, parameter $\beta$ measures the sensitivity of the SEO fee to $q _ { r }$ Therefore, in a perfectly competitive market, we have:

$$
u _ {2} = \alpha q _ {e} r _ {o} v - \beta q _ {r}\tag{2}
$$

Additionally, advertisers can also choose both SEO and PSM simultaneously. Nonetheless, White (2013) and Edelman and Lai (2016) argue for a competitive relationship between the two marketing strategies. As such, the effectiveness of SEO is reduced with the presence of PSM. Therefore, the utility obtained by advertisers who choose both SEO and PSM simultaneously is:

$$
u _ {2} = \gamma \alpha q _ {e} r _ {o} v - \beta q _ {r} + \alpha q _ {e} r _ {s} (v - p)\tag{3}
$$

where ?? represents the portion of the original utility that SEO can achieve when both SEO and PSM are chosen, compared to when only the SEO strategy is adopted.

Advertisers face the problem of choosing an advertising strategy that maximizes their payoff. Based on the net payoff, advertisers must choose among four alternatives: no advertisement, PSM, SEO, and PSM+SEO. The equation for this problem is:

$$
\begin{array}{l} \text {max} \left\{ \begin{array}{c} \text {No Advertisem} \\ P S M \\ S E O \\ P S M + S E O \end{array} \right. \\ = \text {max} \left\{ \begin{array}{c} u _ {0} \\ u _ {0} + \alpha q _ {e} r _ {s} (v - p) \\ u _ {0} + \alpha q _ {e} r _ {o} v - \beta q _ {r} \\ u _ {0} + \gamma \alpha q _ {e} r _ {o} v - \beta q _ {r} + \alpha q _ {e} r _ {s} (v - p) \end{array} \right. \end{array}\tag{4}
$$

where $u _ { 0 }$ is the payoff from no advertisement, meaning organic listing without PSM or SEO.

## 4 Model Analysis

We can now discuss the market shares of SEs and SEO firms in the search engine advertising market by focusing on the search engine market share and partitioning the online advertising market by advertiser type ?? . Specifically, let $p _ { 2 } ( v )$ be the market-clearing price for advertisers of type ?? who are indifferent between using SEO and PSM. Given that prices of paid advertisements are determined through auctions, with $u _ { 1 } = u _ { 2 }$ , we can obtain:

$$
p _ {2} (v) = \frac {\lambda q _ {r}}{\alpha q _ {e} r _ {s}} - \frac {r _ {o} - r _ {s}}{r _ {s}} v\tag{5}
$$

Similarly, the price at which there is no difference between PSM+SEO and SEO is:

$$
p _ {3} (v) = [ 1 - \frac {(1 - \gamma) r _ {o}}{r _ {s}} ] v\tag{6}
$$

The intuition behind this result is that advertisers with willingness to pay ?? will not bid higher than $p _ { i } ( v )$ ; if they must bid higher to win the auction, they might choose SEO.

Lemma 1. Based on the equation above, the market clearing price is: if $\begin{array} { r } { V \le \frac { \lambda q _ { r } } { \alpha q _ { e } r _ { s } } , } \end{array}$ , then $\mathrm { \Delta p } = \mathrm { v } ;$ whereas $\begin{array} { r } { \mathrm { i f } \ \frac { \lambda q _ { r } } { \alpha q _ { e } r _ { s } } \le V \le \frac { \lambda q _ { r } } { \alpha \gamma q _ { e } r _ { s } } } \end{array}$ , then $\begin{array} { r } { p = \frac { \lambda q _ { r } } { \alpha q _ { e } r _ { s } } - \frac { r _ { o } - r _ { s } } { r _ { s } } v } \end{array}$ otherwise, $\begin{array} { r } { p = [ 1 - \frac { ( 1 - \gamma ) r _ { o } } { r _ { s } } ] v . } \end{array}$

For advertisers, the increase in ?? can alleviate their fixed cost $\beta q _ { r } ,$ referred to as the expected cost dilution effect in this paper. According to Lemma 1, when the advertiser’s willingness to pay ?? is less than the threshold value ${ \frac { \lambda q _ { r } } { \alpha q _ { e } r _ { s } } } ,$ the market-clearing price ?? equals the advertiser’s willingness to pay. This occurs because the expected cost dilution effect is low, making the revenue of SEO lower than its cost, resulting in the disappearance of SEO from the market. As a result, the competition in the search engine market disappears, and the market-clearing price is equal to the advertiser’s

## willingness to pay.

When ?? is in the middle range, an interesting phenomenon occurs: The market-clearing price decreases as the advertiser’s willingness to pay increases, as illustrated in Figure 2. This phenomenon occurs because as ?? increases, the cost dilution effect increases, causing SEO revenue to exceed its cost. Consequently, market competition intensifies, driving the marketclearing price down. When ?? exceeds threshold $\frac { \lambda q _ { r } } { \alpha \gamma q _ { e } r _ { s } } ,$ the positive correlation between advertisers’ willingness to pay, and the market-clearing price is restored. This occurs because the cost dilution effect is dominant, and the emergence of SEO + PSM reduces market competition, leading to an increase in the marketclearing price ?? with an increase in ??.

## 4.1 Advertiser’s Strategy Choice

Based on Equation (4), advertisers will pay the SE for sponsored links service only if $u _ { 1 } > 0 , u _ { 1 } > u _ { 2 }$ and $u _ { 1 } > u _ { 3 }$ , which means:

$$
\left\{ \begin{array}{c} p <   v \\ p <   \frac {\lambda q _ {r}}{\alpha q _ {e} r _ {s}} - \frac {r _ {o} - r _ {s}}{r _ {s}} v \\ v <   \frac {\lambda q _ {r}}{\alpha \gamma q _ {e} r _ {s}} \end{array} \right.
$$

Similarly, when advertisers choose SEO or SEO + PSM, we have:

$$
\left\{ \begin{array}{c} \frac {\lambda q _ {r}}{\alpha q _ {e} r _ {s}} <   v \\ p <   \frac {\lambda q _ {r}}{\alpha q _ {e} r _ {s}} - \frac {r _ {o} - r _ {s}}{r _ {s}} v \text {and} \\ p <   [ 1 - \frac {(1 - \gamma) r _ {o}}{r _ {s}} ] v \end{array} \right. \left\{ \begin{array}{c} p <   [ 1 - \frac {(1 - \gamma) r _ {o}}{r _ {s}} ] v \\ \frac {\lambda q _ {r}}{\alpha \gamma q _ {e} r _ {s}} <   v \\ v <   \frac {r _ {o} + r _ {s}}{r _ {s}} v - \frac {\lambda q _ {r}}{\alpha \gamma q _ {e} r _ {s}} \end{array} \right.
$$

Since the price of PSM, $p _ { i } ( v )$ , is determined by keyword auction, it is never greater than ??, the maximal willingness to pay in a given market segment. As a result, the market share of the SE is depicted as the shaded area in Figure 3.

![](/api/attachments/EM976JN4/fulltext/images/ec02799d5fbb289b0a9583450ee7ee308cf7a08fb32f5b66e5fcfd3b6b89f947.jpg)  
Figure 2. Indifference Line of Advertisers in Search Marketing

![](/api/attachments/EM976JN4/fulltext/images/7cd4ef7cf250c717b51aba046f91e414aa4d7fa02afda102eb66168957bc126b.jpg)  
Figure 3. Market Share of Search Engine

![](/api/attachments/EM976JN4/fulltext/images/61a0b24f6dbe2e95906b69c77ebf95e4e033309f4b89a49e9bd44ab89a4eaa2b.jpg)  
Figure 4. Operation Region of SEO

In Figure 3, the market share of the SE can be divided into three areas by this line: Area I, Area II and Area III. In Area I, the payoff $u _ { 2 }$ for advertisers who choose SEO firms is less than 0. Therefore, advertisers within the interval $[ 0 , \frac { \lambda q _ { r } } { \alpha q _ { e } r _ { o } } ]$ will not choose SEO firms. That is, advertisers within the interval $[ 0 , \frac { \lambda q _ { r } } { \alpha q _ { e } r _ { o } } ]$ belong to the SE. Advertisers within the interval $\big [ \frac { \lambda q _ { r } } { \alpha q _ { e } r _ { o } } , \frac { \lambda q _ { r } } { \alpha \gamma q _ { e } r _ { o } } \big ]$ may choose SEO firms because the payoff may be greater than 0. Thus, the SE and SEO firms compete for this part of the market. Additionally, advertisers within the interval $\big [ \frac { \lambda q _ { r } } { \alpha \gamma q _ { e } r _ { o } } , V \big ]$ may select both SE and SEO firms, resulting in a shared market.

From the equation above, we learn that advertisers with a low willingness to pay (v) absolutely choose the PSM service provided by SEs. The customers of SEO firms only exist in advertisers with a high willingness to pay. The model formally explains why SEO only appeals to higher-type advertisers. Therefore, we can obtain the survival conditions of SEO firms:

$$
\frac {\lambda q _ {r}}{\alpha q _ {e} r _ {o}} <   v\tag{7}
$$

As SEO firms passively accept the decisions made by SEs, their survival depends on two aspects: algorithm robustness and effectiveness. Based on Equation (7), the line $\begin{array} { r } { \frac { \lambda q _ { r } } { \alpha q _ { e } r _ { o } } = v } \end{array}$ denotes all critical points $( q _ { r } , q _ { e } )$ at which SEO firms can be driven out of the market. Figure 4 demonstrates the “acceptance region” where SEO firms may be retained in the market. In contrast, in the rejection region, SEO firms will be driven out of the market.

Lemma 2: (SEO Acceptance Area) SEO firms can only survive in an “acceptance Area” determined by both algorithm effectiveness and algorithm robustness of the SE, with the critical condition being $\begin{array} { r } { \frac { q _ { e } } { q _ { r } } = \frac { \lambda } { \alpha r _ { s } V } . } \end{array}$

Given a certain $q _ { e }$ , Figure 4 indicates that the SE could drive SEO firms out of the market if its algorithm robustness is sufficiently high. As the algorithm robustness increases, it becomes harder for SEO firms to create noise in organic search results. Thus, advertisers will not choose SEO firms.

Similarly, given a certain $q _ { r } ,$ , Figure 4 indicates that the SEO firm will survive if the algorithm effectiveness is sufficiently high. If the SE has excellent algorithm effectiveness, there are more searchers. This means a higher market share for both SEs and SEO firms. The situation of Yahoo after Google entered the market closely matches this finding. After Google became a clear leader in algorithm effectiveness, it became a major target for SEO firms. Google Dance Syndromes (Telang & Mukhopadhyay, 2005), events where Google drastically revises its ranking algorithm and updates its index, are explicit attempts to counteract SEO practice. In contrast, such events seldom occurred in Yahoo in its early stages. According to the model, this is because Yahoo had lower algorithm effectiveness and less search demand. This made SEO with Yahoo less sustainable.

From Figure 4, we see that the slope of the boundary line is $\frac { \lambda } { \alpha r _ { s } V } ,$ affecting the size of the acceptance region. If ?? is greater, the acceptance area becomes larger. As discussed above, the customers of SEO firms only exist among advertisers with a high willingness to pay. Advertisers are assumed to be uniformly distributed over the interval [0, ??] . If V increases, there will be more advertisers with a high willingness to pay, and SEO firms will have more opportunities to be retained. We can also see that if $r _ { o }$ becomes larger, the acceptance area will also expand. For many online business firms, the click-through rate is vital. This is also adopted in SEO firms. SEO firms should not only strive to keep their customers’ links ranked in higher positions in organic search results but should also optimize landing pages to enhance relevance and achieve a higher clickthrough rate. Many conventional means of vicious competition can cause customers’ links to appear in organic searches where there are high page rankings but CTR remains low. This actually reduces the survival space for SEO firms.

## 4.2 Profit Analysis of SE

The above discussions pave the way for analyzing SE’s profit and revealing the factors that may affect the profit of the SE in the search engine market. First, let $C ( q _ { e } )$ be the cost function of the SE. This cost is a quadratic function of $q _ { e }$ , denoted by $\begin{array} { r } { C ( q _ { e } ) = \frac { 1 } { 2 } \xi { q _ { e } } ^ { 2 } } \end{array}$ . It is also assumed that $q _ { r } ,$ the algorithm robustness of the SE, is a long-term investment decision and that c is thus sunk at the time of decision-making (Jiang et al., 2023). By definition, in the absence of SEO firms in the market, the profit function of the SE can be derived as follows:

$$
\pi_ {I} = \frac {1}{V} \int_ {0} ^ {V} \alpha q _ {e} r _ {s} p _ {1} d v - \frac {1}{2} \xi q _ {e} ^ {2}
$$

In the presence of SEO firms, the SE’s profit can be expressed as:

$$
\pi_ {I I} = \frac {1}{v _ {1}} \int_ {0} ^ {v _ {1}} \alpha q _ {e} r _ {s} p _ {1} d v + \frac {1}{V - v _ {1}} \int_ {v _ {1}} ^ {V} \alpha q _ {e} r _ {s} p _ {2} d v - \frac {1}{2} \xi q _ {e} ^ {2}
$$

Similarly, in the presence of SEO+PSM in the market, the profit of the SE is given by:

$$
\begin{array}{r} \pi_ {I I I} = \frac {1}{v _ {1}} \int_ {0} ^ {v _ {1}} \alpha q _ {e} r _ {s} p _ {1} d v + \frac {1}{v _ {2} - v _ {1}} \int_ {v _ {1}} ^ {v _ {2}} \alpha q _ {e} r _ {s} p _ {2} d v \\ + \frac {1}{V - v _ {2}} \int_ {v _ {2}} ^ {V} \alpha q _ {e} r _ {s} p _ {3} d v - \frac {1}{2} \xi q _ {e} ^ {2}, \end{array}
$$

where $\begin{array} { r } { v _ { 1 } = \frac { \lambda q _ { r } } { \alpha q _ { e } r _ { o } } , v _ { 2 } = \frac { \lambda q _ { r } } { \alpha \gamma q _ { e } r _ { o } } . } \end{array}$

## 4.3 Equilibrium Analysis

Based on the equations for $\pi _ { I } , \ \pi _ { I I }$ and $\pi _ { I I I }$ , the optimal decision for the SE is shown in Proposition 1. It is worth noting that, to maintain clarity and conciseness in the main text, the proof processes for all propositions and the theorem are presented in Appendix A.

Proposition 1: Without SEO firms in the market, if $\frac { V ^ { 2 } \alpha ^ { 2 } r _ { s } r _ { o } } { 2 \lambda \xi } \leq q _ { r } .$ , the optimal effectiveness is $q _ { e } { ^ { * } } = \frac { V \alpha r _ { s } } { 2 \xi }$ and the maximum achievable profit for the SE is $\begin{array} { r } { \pi _ { \mathrm { I } } { } ^ { * } = \frac { V ^ { 2 } \alpha ^ { 2 } r _ { s } ^ { 2 } } { 8 \xi } ; } \end{array}$ ； otherwise, the optimal effectiveness is $q _ { e } ^ { * } = \frac { \lambda q _ { r } } { V \alpha r _ { o } }$ and the maximum achievable profit for SE is $\begin{array} { r } { \pi _ { \mathrm { I } } ^ { \ * } = \frac { \lambda q _ { r } ( V ^ { 2 } \alpha ^ { 2 } r _ { s } r _ { o } - \lambda \xi q _ { r } ) } { 2 V ^ { 2 } \alpha ^ { 2 } r _ { o } ^ { 2 } } . } \end{array}$

Intuitively, a positive correlation exists between an SE’s effectiveness and the number of searchers it attracts—a higher level of effectiveness typically draws more searchers, thereby increasing revenue. However, the analysis of Proposition 1 demonstrates that enhancing effectiveness is not always the optimal strategy when an SE’s robustness is relatively low. In such cases, greater effectiveness may actually reduce the SE’s optimal profit. This counterintuitive outcome can be attributed to the “cost dilution effect.”

When the robustness of a search algorithm is low, SEO services are more likely to penetrate the SEM market. In these scenarios, improving effectiveness further intensifies the cost dilution effect, rendering SEO services more appealing to advertisers. This occurs because the average cost that advertisers incur for adopting SEO services decreases as effectiveness increases. As a result, while higher effectiveness may enhance the user search experience, it also increases the SE’s operational costs $\xi q _ { e } { ^ 2 } / 2$ and raises advertisers’ inclination to use SEO services. These factors collectively diminish the SE’s revenue, ultimately reducing its profitability.

Proposition 1 highlights how an SE strategically adjusts the “effectiveness” of its search algorithm in response to its “robustness” to maintain market dominance and achieve profit maximization. The findings indicate that robustness is not merely a tool for ensuring algorithmic stability but serves as a critical moderating factor in the profitability strategy of an SE. Instead of unilaterally pursuing higher effectiveness, an SE should make rational decisions based on the level of algorithmic robustness to optimize its profits.

When the robustness $q _ { r }$ of a search algorithm exceeds a specific threshold $\frac { V ^ { 2 } \alpha ^ { 2 } r _ { s } r _ { o } } { 2 \lambda \xi }$ , the SE can freely select its optimal level of effectiveness to attract more users and maximize profits. This is because high robustness creates substantial entry barriers for SEO services in the SEM domain, effectively establishing a strong “moat” for the SE. Conversely, when robustness falls below the threshold $\frac { V ^ { 2 } \alpha ^ { 2 } r _ { s } r _ { o } } { 2 \lambda \xi } ,$ the SE must take strategic measures to constrain the survival space of SEO firms and mitigate the impact of reduced entry barriers in the SEM market. In this scenario, the SE should reduce its effectiveness to limit market expansion, alleviating the competitive pressure caused by the cost dilution effect. This strategy influences advertisers’ resource allocation decisions between SEO and PSM, preserving the SE’s monopoly position and profit margins.

The robustness adjustment mechanism described in Proposition 1 provides valuable guidance for search engine managers seeking to balance user experience optimization with profit maximization. For emerging SEs or platforms aiming to enter new markets, understanding how the cost dilution effect influences advertisers’ decisions can enhance platform attractiveness and entry barriers without excessive reliance on high effectiveness. By controlling costs and strategically managing algorithmic effectiveness and robustness, platforms can attract appropriate advertisers, optimize market distribution, and sustain long-term competitiveness.

For SEO firms, when advertisers exhibit low willingness to pay, the SE may adjust algorithmic effectiveness based on robustness to limit the survival of SEO firms. However, SEO firms should recognize that their primary constraint lies in the high service costs $\lambda q _ { r }$ which hinder advertisers from obtaining sufficient benefits to justify these costs. In such situations, SEO firms should focus on improving their competitiveness, irrespective of whether the SE’s algorithmic effectiveness is high or low. For instance, SEO firms can enhance technological innovation by leveraging large language models to improve service efficiency. Collaborating with the SE—via joint promotions or technology sharing—can also help SEO firms better understand and adapt to algorithmic changes, thereby increasing click-through rates for their services. These efforts can reduce advertisers’ costs, improve their loyalty, and ultimately expand the survival space for SEO firms. How will the SE’s strategies evolve as market conditions change while SEO services persist?

Proposition 2: When advertisers exhibit a moderate willingness to pay, suggesting the potential existence of SEO companies in the market, an increase in effectiveness results in a decline in the optimal profit for the SE. Consequently, in this scenario, the optimal decision for the SE is $q _ { e } ^ { * } = \frac { \lambda q _ { r } } { V \alpha r _ { o } }$ , and the maximum profit is $\begin{array} { r } { \pi _ { I I } { } ^ { * } = \frac { \lambda q _ { r } ( 3 V ^ { 2 } \alpha ^ { 2 } r _ { s } r _ { o } - \lambda \xi \bar { q _ { r } } ) } { 2 V ^ { 2 } \alpha ^ { 2 } r _ { o } ^ { 2 } } . } \end{array}$

Moderate advertiser willingness to pay often leads to the adoption of SEO services, creating necessary conditions for the survival of SEO firms. Similar to Proposition 1, Proposition 2 highlights a counterintuitive relationship: increased effectiveness can paradoxically lead to a decline in the SE’s profit, irrespective of the algorithm’s robustness. This phenomenon is primarily driven by the cost dilution effect, which lowers the average cost for advertisers utilizing SEO services.

The underlying mechanisms in Proposition 1 and Proposition 2, however, differ significantly. In Proposition 1, the cost dilution effect stems from the algorithm’s low robustness, which lowers entry barriers and reduces total costs for providing SEO services. In contrast, in Proposition 2, increased advertiser willingness to pay intensifies the cost dilution effect. Higher advertiser willingness to pay reduces demand for performance-based PSM while increasing the appeal of SEO services, adversely affecting the SE’s advertising revenue.

Under such conditions, enhanced effectiveness further amplifies the cost dilution effect, bolstering SEO firms’ competitiveness and intensifying market competition for the SE. Moreover, improving effectiveness demands significant costs $\xi q _ { e } { ^ 2 } / 2$ including investments in manpower, time, and financial resources. However, in a competitive market, such investments often fail to yield commensurate returns. As a result, the revenue generated by increased effectiveness is insufficient to offset associated costs, further diminishing the SE’s profit. To mitigate these adverse effects, the SE often opts to reduce its effectiveness, thereby constraining market expansion and alleviating the negative impact of the cost dilution effect.

Proposition 2 suggests that in a market where SEO firms can sustain their operations, the SE must implement flexible management strategies to preserve the attractiveness and profitability of performance-based PSM while mitigating the competitive pressure introduced by the cost dilution effect of SEO. The SE faces a strategic trade-off between improving internal competitiveness (against SEO firms) and enhancing external competitiveness (attracting searchers). In some cases, the SE may prioritize internal competitiveness over external competitiveness. This approach is exemplified by the practices of certain SEs, such as

Baidu, that have faced criticism for the low effectiveness of their webpage rankings yet refrained from significantly improving their algorithms. The underlying logic is that maintaining lower algorithmic effectiveness can reduce the competitive impact of SEO on PSM.

Consequently, the SE must dynamically adjust its algorithm’s effectiveness based on market conditions. When advertisers demonstrate moderate willingness to pay, the SE should lower its effectiveness to alleviate the competitive pressures of SEO on PSM. Conversely, when advertisers exhibit a clear preference for PSM, the SE should moderately enhance its effectiveness to expand the SEM market and boost advertising revenue.

Under such conditions, the SE can further strengthen PSM’s competitive differentiation by offering valueadded services, such as customized data analytics tools, performance tracking, and optimized PSM algorithms.

These enhancements enable advertisers to more accurately target user groups, increase their dependence on PSM, and diminish the market competitiveness of SEO. This strategy allows the SE to better allocate resources, maximize returns, and secure a larger market share at a specific level of effectiveness. These enhancements help advertisers precisely target user groups, increase their reliance on PSM, and weaken the market competitiveness of SEO. Such a strategy enables the SE to optimize resource allocation and improve returns, ultimately achieving a higher market share at a specific level of algorithmic effectiveness.

However, the SE’s strategy may lead to certain negative consequences, particularly adverse effects on consumer welfare, as SEs often lack the incentive to address or rectify such issues. Therefore, regulatory authorities should focus on monitoring scenarios where advertisers exhibit moderate willingness to pay, emphasizing the competitive dynamics between SEO and performancebased PSM. By collecting and analyzing market data on the behaviors of SEs, SEO firms, and advertisers, regulators can periodically assess changes in search engine algorithm effectiveness and the market share of SEO firms. Such assessments would enable the development of guidelines to ensure that SEs do not abuse their market position to suppress SEO firms, thereby mitigating potential harm to users. Additionally, regulators should establish standards for search engine behavior concerning algorithm adjustments, requiring that effectiveness modifications do not excessively compromise user experience, thus protecting consumer welfare. By setting baseline effectiveness indicators and providing policy guidance, regulators can promote collaboration and healthy competition between SEs and SEO firms, ensuring sustainable market development and safeguarding users’ legitimate interests.

For SEO firms, it is essential to adapt their service strategies to thrive in low-effectiveness market environments. Proposition 2 indicates that when advertisers exhibit moderate willingness to pay, SEs may intentionally lower algorithm effectiveness to diminish SEO’s appeal to advertisers. Consequently, SEO firms must enhance their competitiveness under such conditions. Specifically, they can optimize longtail keywords, improve content quality, and enhance user experience to boost SEO click-through rates. This approach not only strengthens SEO’s market appeal but also reduces the range within which SEs can adjust their effectiveness (i.e., the interval $\begin{array} { r } { \frac { \lambda q _ { r } } { V \alpha r _ { o } } < q _ { e } < \frac { \lambda q _ { r } } { V \alpha \gamma r _ { o } } } \end{array}$ becomes smaller), thereby mitigating the negative impact on SEO operations.

Furthermore, SEO firms should prioritize analyzing advertisers’ willingness to pay and market segmentation. Proposition 2 highlights the impact of advertisers’ willingness to pay on SEO business performance. Thus, SEO firms should conduct comprehensive market research, monitor fluctuations in willingness to pay, and adapt client targeting and marketing strategies accordingly. For advertisers with moderate willingness to pay, SEO firms can introduce medium-to-long-term optimization plans that provide consistent traffic acquisition services, fostering greater reliance on SEO solutions. Furthermore, leveraging advanced technological tools to innovate value-added services can help SEO firms address market uncertainties from reduced search engine effectiveness. For example, by utilizing artificial intelligence to lower SEO service costs (i.e., reducing the cost coefficient ??), SEO firms can offer personalized solutions that integrate data analytics and user behavior insights, enabling clients to achieve more precise traffic management. These measures allow SEO firms to strengthen advertisers’ dependence on their services, ensuring that SEO retains its value even when the SE reduces its effectiveness.

Proposition 3. When SEO + PSM exists in the market, if the robustness $( q _ { r } )$ of SEs exceeds the threshold of $\frac { V ^ { 2 } \alpha ^ { 2 } \gamma r _ { o } [ r _ { s } - ( 1 - \gamma ) r _ { o } ] } { 2 \lambda \xi }$ then the optimal effectiveness is $\begin{array} { r } { q _ { e } { ' } = \frac { \lambda q _ { r } } { V \alpha \gamma r _ { o } } } \end{array}$ , and the maximum profit is?? $\begin{array} { r } { \dot { { ^ { \prime } I I I } } ^ { * } = \frac { \lambda q _ { r } \{ V ^ { 2 } \alpha ^ { 2 } \gamma r _ { o } [ ( 3 + 2 \gamma ) r _ { s } - 3 ( 1 - \gamma ) r _ { o } ] - \lambda \xi q _ { r } \} } { 2 V ^ { 2 } \alpha ^ { 2 } \gamma ^ { 2 } r _ { o } ^ { 2 } } } \end{array}$ otherwise, $\begin{array} { r } { { q _ { e } } ^ { * } = \frac { V \alpha ( r _ { s } - r _ { o } + \gamma r _ { o } ) } { 2 \xi } } \end{array}$ and $\pi _ { I I I } { } ^ { * } =$ $\frac { V ^ { 2 } \alpha ^ { 2 } \gamma r _ { o } [ r _ { s } - ( 1 - \gamma ) r _ { o } ] ^ { 2 } + 8 \lambda \xi q _ { r } [ ( 1 + \gamma ) r _ { s } - ( 1 - \gamma ) r _ { o } ] } { 8 \gamma \xi r _ { o } } .$

In contrast to the scenarios described in Propositions 1 and 2, when advertisers exhibit strong willingness to pay, indicating a preference to invest in both SEO and performance-based paid search marketing, the influence of search algorithm robustness $q _ { r }$ on the SE’s decisionmaking process reverses. Proposition 3 reveals that if advertisers choose SEO and PSM simultaneously, the SE can achieve unconstrained optimal decisions and profits when robustness is low $\begin{array} { r } { \mathrm { ~ ( ~ } q _ { r } < \frac { V ^ { 2 } \alpha ^ { 2 } \gamma r _ { o } [ r _ { s } - ( 1 - \gamma ) r _ { o } ] } { 2 \lambda \xi } \mathrm { ~ ) ~ } } \end{array}$ ).

Conversely, in a market restricted to PSM, high robustness $\begin{array} { r } { \big ( \frac { V ^ { 2 } \alpha ^ { 2 } r _ { s } r _ { o } } { 2 \lambda \xi } \le q _ { r } \ \big ) } \end{array}$ prevents the SE from achieving unconstrained optimal profits.

This disparity arises from variations in advertisers willingness to pay. When willingness to pay is low, resulting in a market limited to PSM, the SE must restrict SEO’s attractiveness to maintain PSM’s monopolistic dominance. However, when advertisers exhibit high willingness to pay $( \frac { \lambda q _ { r } } { \alpha \gamma q _ { e } r _ { o } } \le V )$ , they tend to invest in both SEO and PSM, significantly alleviating competitive pressures between the SE and SEO firms. With the reduced impact of cost dilution, the SE no longer needs to limit SEO’s appeal by reducing algorithmic effectiveness. Instead, it can enhance effectiveness to improve external market competitiveness and maximize profits more effectively.

When the SE’s robustness $q _ { r }$ exceeds the threshold $\frac { V ^ { 2 } \alpha ^ { 2 } \gamma r _ { o } [ r _ { s } - ( 1 - \gamma ) r _ { o } ] } { 2 \lambda \xi }$ , it must select higher effectiveness $\begin{array} { r } { ( \frac { \lambda q _ { r } } { V \alpha \gamma r _ { o } } \leq q _ { e } ) } \end{array}$ to balance internal competition. However, this choice leads to higher costs $\xi q _ { e } ^ { ~ 2 } / 2$ . Notably, the marginal benefits of increased effectiveness diminish while marginal costs rise, causing optimal profits to decline as effectiveness $( q _ { e } )$ increases. Therefore, to maintain the coexistence of SEO and PSM, the SE strategically minimizes effectiveness to maximize profits.

Conversely, when the SE’s robustness $q _ { r }$ falls below the threshold $\frac { V ^ { 2 } \alpha ^ { 2 } \gamma r _ { o } [ r _ { s } - ( 1 - \gamma ) r _ { o } ] } { 2 \lambda \xi }$ , advertisers are more likely to adopt a combined SEO + PSM strategy, significantly reducing internal competitive pressures on the SE. In such scenarios, the SE shifts its primary objective toward enhancing external competitiveness by increasing the effectiveness of its search algorithm. This adjustment enables the SE to achieve unconstrained optimal decisions and maximize profits.

Proposition 3 outlines the SE’s optimization strategies under varying levels of robustness $q _ { r }$ and explores the profound impact of robustness on effectiveness decisions and profit-maximization pathways when advertisers demonstrate a high willingness to pay. In high-robustness environments, the SE can achieve higher profits by increasing effectiveness $q _ { e \mathrm { ~ . ~ } }$ , albeit at substantial cost. Consequently, the SE must focus on optimizing the costeffectiveness of effectiveness improvements, striking a dynamic balance between expenditures and market expansion. This scenario contrasts with low advertiser willingness to pay, where the SE focuses more on balancing internal and external competition. Technological advancements, such as implementing efficient indexing mechanisms to improve search ranking accuracy or employing large language models to refine algorithm development, can bolster the efficiency of effectiveness enhancements. Additionally, since improved effectiveness benefits SEO firms, the SE may consider forming collaborative partnerships with these firms to share costs, lower marginal expenses, and facilitate market expansion. In low-robustness environments, the SE’s primary objective shifts toward enhancing user satisfaction with search results, adopting measures to boost platform attractiveness, and increasing investments in algorithmic advancements. Enhancing effectiveness in such contexts promotes market growth, strengthens customer retention, and increases the appeal of both SEO and PSM.

For SEO firms, strategies should align with the SE’s robustness level. In high-robustness environments, where the SE may moderately limit SEO effectiveness, SEO firms should focus on strengthening partnerships with the SE. By sharing the costs of algorithmic improvements, SEO firms can enhance the sustainability of the SEO + PSM strategy while contributing to the expansion of the overall search marketing market, creating mutual benefits. Conversely, in low-robustness environments, SEO firms should emphasize increasing their attractiveness to boost click-through rates. Strategies such as improving service quality and expanding keyword coverage can enhance advertisers’ satisfaction and the expected returns on SEO investments. Higher click-through rates encourage more advertisers to adopt a combined SEO + PSM strategy, fostering a favorable internal competitive environment $( \frac { \lambda q _ { r } } { V \alpha \gamma r _ { o } } )$ and creating opportunities for revenue growth for both the SE and SEO firms.

For advertisers, the core strategic focus should be optimizing resource allocation to maximize marketing efficiency, rather than merely comparing the costeffectiveness of SEO and PSM. Advertisers should first devise dynamic budget allocation strategies that align with their marketing objectives and budgetary constraints, leveraging the complementary advantages of SEO and PSM. For instance, SEO can improve the organic ranking of branded keywords, ensuring a stable and sustainable traffic source, while PSM can deliver rapid market coverage and high conversion rates through precise targeting. Additionally, advertisers should emphasize the synergies between SEO and PSM, rigorously evaluating their combined effects to reduce redundant investments and enhance overall marketing efficiency. This integrated approach strengthens the effectiveness of advertising campaigns and establishes a solid foundation for longterm competitive advantages in highly competitive markets.

## Theorem 1: The expulsion of SEO companies from the market by SEs does not necessarily maximize the SE’s profits.

Intuitively speaking, it may seem that an SE can increase its profitability by excluding SEO companies to monopolize market share. However, deeper analysis indicates that under certain conditions, the presence of SEO companies can enhance the SE’s optimal profit.

SEO companies, for instance, can manipulate webpage content or links to boost their clients’ rankings on search engine results pages (SERPs). While this practice improves client visibility, it may diverge from the SE’s primary objective of “prioritizing the most relevant content,” potentially reducing the relevance of search results. This reduction in relevance can mislead users with deceptive links or unnecessary redirections, ultimately degrading the overall user experience. Furthermore, competition between SEO companies and SEs may weaken the latter’s control over the advertising market, negatively impacting its advertising revenue.

Xu et al. (2012) argued that SEO companies, by artificially inflating prominence in organic search results, could harm an SE’s profitability. This study, however, finds that the presence of SEO companies can, in fact, support the SE in achieving higher optimal profits. Eliminating SEO is advantageous only when the advertiser’s willingness to pay is exceptionally low. One plausible explanation is that the presence of SEO companies drives the SE to optimize its search algorithms more effectively. Specifically, when $\begin{array} { r } { q _ { r } < \frac { V ^ { 2 } \alpha ^ { 2 } r _ { s } r _ { o } } { 2 \lambda \xi } } \end{array}$ , the optimal effectiveness with SEO $\big ( \frac { \lambda q _ { r } } { V \alpha r _ { o } } \big )$ exceeds the optimal effectiveness without SEO $( \frac { V \alpha r _ { s } } { 2 \xi } )$ . Conversely, when $\frac { V ^ { 2 } \alpha ^ { 2 } r _ { s } r _ { o } } { 2 \lambda \xi } < q _ { r }$ , the optimal effectiveness with SEO and PSM $( \frac { \lambda q _ { r } } { V \alpha \gamma r _ { o } } )$ is greater than the optimal effectiveness without SEO $( \frac { \lambda q _ { r } } { V \alpha r _ { o } } )$ . Improved algorithmic effectiveness enables the SE to expand its market coverage, increasing revenue. Conversely, attempts to exclude SEO companies may lead to suboptimal decision-making, deviating from the optimal path and resulting in reduced profitability compared to theoretical maxima. To present our conclusions more clearly, we have also conducted numerical analysis on the relevant findings. Please refer to Appendix B for the results of the analysis.

Theorem 1 explains why dominant SEs tolerate the existence of SEO within their markets. This study demonstrates that SEO contributes to the vitality of the search ecosystem. SEs should therefore view SEO not merely as a competitive threat but as a form of “constructive competition.” Rather than limiting market growth or sacrificing revenue to exclude SEO companies, SEs should focus on improving algorithmic effectiveness to enhance the relevance of search results, thereby increasing platform attractiveness and expanding the market. Additionally, SEs could explore indirect revenue models, such as offering performance evaluation tools for SEO companies through data analytics. This approach would integrate SEO activities into the SE’s revenue system, reduce competition in the SEM market, diversify revenue streams, and extend the value chain.

SEO companies, in turn, must recognize that their relationship with SEs is not a zero-sum game. Instead, they should consider themselves key participants in the search ecosystem. To avoid exclusionary actions, SEO companies should collaborate with SEs, focusing on keyword optimization and content quality improvement. By delivering high-quality SEO services, SEO companies can assist SEs in enhancing user experience, fostering the sustainable development of the search ecosystem, and achieving mutually beneficial outcomes.

## 5 Model Extension

In the previous section, we examined the competitive dynamics between PSM and SEO. Building on this analysis, the current section extends the basic model by incorporating emerging trends in the search engine marketing landscape with the goal of providing deeper insights and demonstrating the robustness of the model’s conclusions.

## 5.1 Search Engine Marketing on Mobile Platforms

With the widespread adoption of smartphones and mobile internet, mobile search traffic has become a pivotal component of the search engine market. Statistical data indicates that approximately 68.22% of search traffic originates from mobile devices, while only 30.2% comes from desktop devices.<sup>6</sup> This trend underscores a shift in the majority of search behavior toward mobile platforms. Compared to traditional desktop search, mobile search presents several distinct advantages.

Mobile search offers superior convenience and flexibility, allowing users to access information anytime and anywhere to meet their on-the-go needs. Moreover, it is particularly effective in addressing personalized user demands. By leveraging location data, mobile devices can deliver tailored search recommendations based on users’ daily behaviors. However, the limited screen size of mobile devices poses significant challenges for information presentation. Smaller displays constrain the amount of content visible on a single page, potentially reducing the efficiency of information retrieval. Compared to desktop search, mobile search may impair the user experience when navigating complex webpages or reading lengthy texts. Additionally, mobile search introduces greater complexity in SEO optimization, as it requires consideration of a broader range of factors than traditional desktop SEO.

Building on this analysis, we have expanded the base model to emphasize the characteristics of mobile search engines. In the mobile environment, the utility function for advertisers choosing a PSM strategy is defined as follows:

$$
u _ {1} ^ {m} = r _ {s} \alpha q _ {e} ^ {m} (1 - \theta_ {1} ^ {m}) (1 + \theta_ {2} ^ {m}) (v _ {1} - p)
$$

In this context, the superscript ?? represents the scenario within the mobile search environment, where $\theta _ { 1 } ^ { m }$ reflects the impact of reduced search information volume and lower information retrieval efficiency on the user scale, assuming all other conditions remain the same. Conversely, $\theta _ { 2 } ^ { m }$ signifies the positive impact of mobile search’s convenience and personalization features on the user scale. When advertisers opt for an SEO strategy, the utility they can derive is as follows:

$$
u _ {2} ^ {m} = r _ {o} \alpha q _ {e} ^ {m} (1 - \theta_ {1} ^ {m}) (1 + \theta_ {2} ^ {m}) v _ {1} - \lambda (1 + \theta_ {3} ^ {m}) q _ {r}
$$

Here, the term $\theta _ { 3 } ^ { m }$ denotes the additional costs that SEO firms must incur to meet mobile users’ demands, with all other conditions held constant. Specifically, when $\theta _ { 3 } ^ { m } = $ 1, mobile search does not influence the difficulty of SEO optimization. Similarly, the utility that advertisers can gain from choosing the SEO + PSM strategy is represented as:

$$
\begin{array}{r} u _ {3} = \gamma r _ {o} \alpha q _ {e} ^ {m} (1 - \theta_ {1} ^ {m}) (1 + \theta_ {2} ^ {m}) v _ {1} - \lambda (1 + \theta_ {3} ^ {m}) q _ {r} \\ + r _ {s} \alpha q _ {e} ^ {m} (1 - \theta_ {1} ^ {m}) (1 + \theta_ {2} ^ {m}) (v _ {1} - p) \end{array}
$$

By solving and analyzing the above model, Theorem 2 can be obtained. For a more detailed discussion of this extension, please refer to Section C1 of Appendix C.

Theorem 2: SEO firms will not be driven out of the mobile search market by search engines. In other words, the presence of SEO benefits mobile search engines as well.

Theorem 2 indicates that despite changes in the characteristics and structure of mobile search, these adjustments have not fundamentally affected the conclusions drawn from desktop search. Specifically, when mobile search engines have low information retrieval efficiency, SEO firms face heightened survival challenges. As shown in Figure 5, when $\phantom { + } \theta _ { 1 } ^ { m }$ increases, the survival space for SEO firms diminishes, especially compared to desktop search engines.

However, when the negative impact of mobile search engines on information retrieval efficiency is minimal, or when users place higher demands on convenience, SEO firms will find it easier to thrive in the mobile search engine marketing market. This is largely due to the fact that the efficiency and convenience of mobile search directly influence the total number of searchers. When mobile search exhibits higher information retrieval efficiency or users demand greater convenience, it attracts more searchers, thereby amplifying the effect of cost dilution. Specifically, when advertisers choose ${ \mathrm { S E O } } ,$ a greater cost dilution effect significantly reduces the survival pressure on SEO firms, thus providing them with more survival space. In this case, the competitiveness of PSM in the search engine marketing market diminishes, prompting the SE to lower PSM prices in order to enhance market competitiveness.

![](/api/attachments/EM976JN4/fulltext/images/d83190e0f695ec3a528cff6c626c6c207aa520f2dde6cffcef9a3ded3c574200.jpg)

Secondly, in the mobile search market, the efficiency of information retrieval and convenience significantly affects the survival prospects of SEO firms. However, these factors do not alter the core conclusion of the base model—that the existence of SEO firms in the search engine marketing market is likely more beneficial to search engines. This suggests that, despite certain changes in the characteristics and structure of mobile search, these changes have not fundamentally affected the key conclusions derived from desktop search. Consequently, even in the mobile search environment, search engines do not need to eliminate SEO firms from the market.

In addition, we examined the scenario in which the platform simultaneously operates both mobile and desktop search services and demonstrated that this does not materially affect our main conclusions. The detailed analysis is provided in Appendix C, Section C2.

(a)  
![](/api/attachments/EM976JN4/fulltext/images/a8a49591b0f7e29bcfdd1e6435edaedbd253d32fbb6838f83a3cc29a41b815be.jpg)  
(b)  
Figure 5. Changes in the Survival Space of SEO Companies in Mobile Search

## 5.2 Impact of AI on Search Engine Marketing

In recent years, the rapid advancement of artificial intelligence (AI) technology has significantly influenced SEs. On the one hand, an increasing number of SEs have integrated AI large language models into their systems, utilizing AI to process, refine, and aggregate retrieved information, thereby enhancing the user search experience. On the other hand, AI has also supported SEO firms in streamlining operations and reducing costs. These factors have collectively had a substantial impact on search engine marketing.

Given the ongoing advancements in AI technology, this paper extends the existing model to examine the impact of AI development on the search engine marketing market. When a search engine incorporates large language models into its system, the expected utility that users derive from retrieving target keywords can be represented as:

$$
\rho_ {1} ^ {A I} v _ {1} \alpha q _ {e} + (1 - \rho_ {1} ^ {A I}) [ (1 - \rho_ {2} ^ {A I}) v _ {2} + \rho_ {2} ^ {A I} v _ {1} \omega ] \alpha q _ {e}
$$

The superscript $" A I ^ { \dag }$ refers to the scenario in which the search engine incorporates a large language model. The parameter $\rho _ { 1 } ^ { A I }$ represents the probability of AIgenerated summaries appearing in the search results, while $\rho _ { 2 } ^ { A I }$ denotes the probability of AI-generated content being accurate. When the AI-generated content is accurate, it provides users with more personalized and precise information, thus enhancing user utility, which is represented by ??, where $\omega > 1$ . Conversely, if the AI-generated content is incorrect, user utility decreases, such that $v _ { 2 } > v _ { 1 }$ . For simplicity, we normalize $v _ { 2 }$ to 0. Under these conditions, the utility gained by advertisers under different strategic choices can be expressed as follows:

$$
u _ {1} = r _ {s} (1 + \rho_ {3} ^ {A I}) \alpha q _ {e} \{[ \rho_ {1} ^ {A I} v _ {1} + \rho_ {2} ^ {A I} (1 - \rho_ {1} ^ {A I}) \omega v _ {1} ] - p \}
$$

$$
u _ {2} = r _ {o} \alpha q _ {e} [ \rho_ {1} ^ {A I} v _ {1} + \rho_ {2} ^ {A I} (1 - \rho_ {1} ^ {A I}) \omega v _ {1} ] - \delta \lambda q _ {r}
$$

$$
\begin{array}{r} u _ {3} = \gamma r _ {o} [ \rho_ {1} ^ {A I} v _ {1} + \rho_ {2} ^ {A I} (1 - \rho_ {1}) \omega v _ {1} ] \alpha q _ {e} - \delta \lambda q _ {r} + r _ {s} (1 \\ + \rho_ {3} ^ {A I}) [ \rho_ {1} ^ {A I} v _ {1} + \rho_ {2} ^ {A I} (1 - \rho_ {1} ^ {A I}) \omega v _ {1} - p ] \alpha q _ {e} \end{array}
$$

Here, $\rho _ { 3 } ^ { A I }$ represents the capability of AI technology to assist the SE in more accurately placing advertisements, thereby enabling PSM to better align with user needs and increase the click-through rate. ?? (where $\delta < 1 )$ indicates that the introduction of AI helps SEO companies reduce costs. For a more detailed and comprehensive introduction and analysis of the model, please refer to Section C3 in Appendix C.

By comparing the utility of advertisers under different strategies, we can assess the SE’s market share, as shown in Figure 6. Two scenarios emerge: the first is when the utility increase provided by AI to searchers is minimal or when the probability of AI errors is high, as illustrated in Figure 6a. To enhance the clarity of the illustration, we depict only the case of $r _ { o } - ( 1 + \rho _ { 3 } ) > 0$ here, as $r _ { o } - ( 1 + \rho _ { 3 } ) < 0$ does not affect the survival space of SEO, thereby leaving the main content in Figure 6 unchanged. The second scenario occurs when AI significantly improves utility for searchers, denoted by $\rho _ { 2 } \omega - \rho _ { 1 } ( 1 - \rho _ { 2 } \omega ) > 1$ , as shown in Figure 6b.

Thus, we derive Lemma 3, which demonstrates the impact of AI technology on the search engine market share.

Lemma 3: When $\rho _ { 2 } < 1 / \omega _ { \mathrm { \Omega } }$ , the introduction of AI may constrain the survival of SEO firms, and in the presence of SEO competition, the SE will increase the price of PSM. Conversely, when $\rho _ { 2 } > 1 / \omega ,$ , the AI technology introduced by the SE will facilitate the expansion of SEO firms’ survival space, and in the presence of SEO competition, the SE will choose to reduce the price of PSM.

p  
![](/api/attachments/EM976JN4/fulltext/images/e5e99fc64dc903f21203e5b640a875f9acecb8f41cf79fffb65e9c80c727521d.jpg)  
(a) $\mathrm { K } = \rho _ { 2 } \omega + \rho _ { 1 } ( 1 - \rho _ { 2 } \omega ) { < } 1$

p  
![](/api/attachments/EM976JN4/fulltext/images/97355e4bfae203879afa21b2ac30be58be10a369832806045acdc296280a0669.jpg)  
(b.1) $\mathrm { K } = \rho _ { 2 } \omega + \rho _ { 1 } ( 1 - \rho _ { 2 } \omega ) { > } 1$

p  
![](/api/attachments/EM976JN4/fulltext/images/0706b6be5e7053ca197b986c25ffa33ed88653f8108e0403f9fcc09e8fcc3736.jpg)  
(b. 2) K = ρ2ω + ρ1(1 − ρ2ω)]>1  
Figure 6. Market Share of the SE Under the Influence of AI

To better understand the changes in the survival space of SEO firms following the introduction of AI, we conducted a numerical analysis comparing the survival space of SEO firms in both the base model and the model with AI, as illustrated in Figure 7. By integrating Lemma 3 with Figure 7, we derived several key conclusions. First, the value of $\rho _ { 1 }$ does not significantly affect the SEO firm’s survival environment. A possible explanation for this is that advertisements also exist within an AI overview (e.g., Google’s), meaning that the introduction of AI does not eliminate the competition between SEO and PSM, but rather alters the target of competition in traditional search results. Consequently, regardless of whether $\rho _ { 1 }$ is high or low, the survival conditions of SEO firms remain relatively stable.

Moreover, when $\rho _ { 2 }$ is small, introducing AI in SEs could increase survival pressure on SEO firms, hindering their development. However, when the introduction of AI leads to a significant increase in expected value for advertisers, or when $\rho _ { 2 }$ is large, AI may help alleviate the survival pressure on SEO firms. In other words, if the AI overview does not significantly increase the expected value for advertisers, or if the accuracy of AI-generated answers is low, SEO firms are more likely to be pushed out of the market by the SE, as depicted in Figure 7. Interestingly, in such scenarios, the SE may choose to raise the price of PSM in response to SEO competition. A possible explanation for this is that while the AI overview captures part of the traditional search market share, when the likelihood of inaccurate results is high, the additional revenue generated by the AI overview for SEO firms fails to compensate for the revenue lost in traditional search, leading to a reduction in SEO earnings. This, in turn, diminishes the negative impact of cost dilution on the SE, ultimately reducing the survival space for SEO firms. For the SE, the introduction of the AI overview with a lower value of $\rho _ { 2 }$ can help mitigate the cost dilution effect to some extent, thereby enhancing the competitiveness of PSM services. Consequently, this provides the SE with the opportunity to increase prices, even in the presence of SEO competition.

![](/api/attachments/EM976JN4/fulltext/images/e52584196fb5263cc5aa2332a7c516e0930c1fdb6d1c7005236129056b008aa8.jpg)  
(a)

Conversely, when the accuracy of AI-generated answers is high, the AI overview can generate sufficient revenue for SEO firms, thereby exacerbating the cost dilution effect and further expanding their survival space. At this point, SEO firms will capture some of the market share from PSM. As a result, the SE may lower the price of PSM to maintain its revenue. Lemma 3 indicates that the introduction of AI and the provision of an AI overview by the SE influence the cost dilution effect, which, in turn, impacts the competition dynamics between SEs and SEO firms.

Similar to the base model, we can determine the optimal decisions and profits for the SE under different scenarios. By comparing the optimal profit of the SE, we derive Theorem 3, as follows:

Theorem 3: The introduction of AI does not fundamentally alter the survival conditions of SEO firms, regardless of whether SEO firms use AI tools. In the search engine marketing market, eliminating SEO firms is not a wise strategy for search engines.

![](/api/attachments/EM976JN4/fulltext/images/74d6bf038ce62028904eb1613cb2cb02255ec2327f587c50cca6a82e0f04964e.jpg)  
(b)  
Figure 7. Comparison of SEO Firm Survival Space Under AI Influence

Theorem 3 reveals that the introduction of AI, whether in the form of the AI overview used by SE or the AI tools used by SEO firms, does not significantly alter the conclusions of the base model. On the one hand, in the search engine marketing market, the SE is the dominant player. Therefore, even if SEO firms use AI tools to reduce costs, this only strengthens their competitive advantage within existing conditions. However, as the market leader, the SE can adjust its decisions to limit the competitive advantage gained by SEO firms through AI tools. Consequently, changes in market share suggest that the use of AI tools by SEO firms does not significantly impact the SE’s market share. Furthermore, even if the SE introduces an AI overview, eliminating SEO firms may not be a wise decision for the SE. As shown in Figure 6, while the introduction of an AI overview affects the SE’s market share and pricing decisions, it does not fundamentally eliminate the cost dilution effect and may even exacerbate it.

## 5.3 Independence of Effectiveness and Robustness

In the base model, this paper assumes “independence between effectiveness and robustness.” While effectiveness and robustness are conceptually distinct, and SEs generally optimize them using separate strategies, indirect interactions between them may still occur. For example, enhancing robustness may indirectly affect effectiveness, and vice versa, improving effectiveness may influence robustness. To explore these potential interactions, we extended the basic model.

For a more thorough and detailed discussion and analysis of this extended model, please refer to Section C4 of Appendix C. If an indirect interaction exists

![](/api/attachments/EM976JN4/fulltext/images/7987a30f26e4f836cf968ae6d74f52cd469b6b1e0b5044c7d82b54a93393dee5.jpg)

$$
q _ {r} + q _ {e} \theta_ {2} ^ {c o} <   q _ {e} + \theta_ {1} ^ {c o} q _ {r}
$$

between effectiveness and robustness, the utility derived by advertisers from selecting different strategies is as follows:

$$
\begin{array}{r l} & u _ {1} = r _ {s} \alpha (q _ {e} + \theta_ {1} ^ {c o} q _ {r}) (v _ {1} - p) \\ & u _ {2} = r _ {o} v _ {1} \alpha (q _ {e} + \theta_ {1} ^ {c o} q _ {r}) - \lambda (q _ {r} + \theta_ {2} ^ {c o} q _ {e}) \\ & u _ {3} = \gamma r _ {o} v _ {1} \alpha (q _ {e} + \theta_ {1} ^ {c o} q _ {r}) - \lambda (q _ {r} + \theta_ {2} ^ {c o} q _ {e}) \\ & \qquad + r _ {s} \alpha \big (q _ {e} + \theta_ {1} ^ {c o} q _ {r} \big) (v _ {1} - p), \end{array}
$$

where $q _ { e } + \theta _ { 1 } ^ { c o } q _ { r }$ denotes the overall effectiveness of the search engine algorithm, which is influenced by the SE’s efforts to enhance effectiveness and robustness. Notably, measures aimed at improving effectiveness have a more pronounced impact, i.e., $\theta _ { 1 } ^ { c o } < 1$ Additionally, $\lambda ( q _ { r } + \theta _ { 2 } ^ { c o } q _ { e } )$ indicates that as algorithmic effectiveness increases, the difficulty for SEO firms in providing services also escalates.

By comparing and analyzing the results, the changes in the SE’s market share, as shown in Figure 8, can be identified. Additionally, the impact of SEO firms’ presence on the SE’s revenue can be evaluated.

Lemma 4: When $0 < q _ { e } < \sqrt { \theta _ { 1 } ^ { c o } / \theta _ { 2 } ^ { c o } } q _ { r }$ , SEO firms are more likely to survive in the market compared to the base model. In this case, if competition exists among SEO firms, the SE will choose to lower the price of PSM. Conversely, when $\sqrt { \theta _ { 1 } ^ { c o } / \theta _ { 2 } ^ { c o } } q _ { r } < q _ { e } ,$ the survival difficulty of SEO firms increases; however, if competition exists among SEO firms, the SE will choose to raise the price of PSM.

Theorem 4: When effectiveness and robustness are not entirely independent, completely eliminating SEO firms from the market is not the optimal strategy for search engines.

![](/api/attachments/EM976JN4/fulltext/images/e4ae9fdbb226e4aec88d3b2a10049319f93ac06e4be0866e26100cfd73ff5408.jpg)  
Figure 8. The Market Share of the SE Under the Correlation Between Effectiveness and Robustness

![](/api/attachments/EM976JN4/fulltext/images/6842b149b9dd6c10d9cfe282e5084cf1e7982d08e5e53a58c2be12cc1dc86d3a.jpg)  
(a)

![](/api/attachments/EM976JN4/fulltext/images/da489f765be608d0a01453c8f96f1dc45a9559d84b6b6398f7869e5b829af4d8.jpg)  
(b)  
Figure 9. Survival Region for SEO Survival under Non-Independence of Robustness and Effectiveness

Lemma 4 and Theorem 4 indicate that when a correlation exists between effectiveness and robustness, SEO firms’ survival conditions are influenced to some extent, but their fundamental ability to survive in the market remains unchanged. Specifically, when efforts by SEs to enhance the robustness of algorithms significantly impact effectiveness, or when $\theta _ { 2 } ^ { c o }$ is small, SEO firms are more likely to survive, as shown in Figures 8 and 9. This phenomenon may result from the positive spillover effect that measures taken by SEs to improve algorithm robustness can have on algorithm effectiveness, thereby mitigating the negative impact of $q _ { r }$ on SEO firms’ survival. Furthermore, this spillover effect can promote market expansion, enhance the costdilution effect, and improve SEO firms’ market position. Consequently, SEO firms have greater room for survival.

On the other hand, to counter the presence of SEO firms and maintain the competitiveness of PSM, SEs will choose to lower the price of PSM. This strategy reflects the trade-off that SEs must make in a competitive market to balance market structure and optimize overall profits.

The correlation between effectiveness and robustness does not fundamentally alter the main conclusions of the model. Even when such a correlation exists, its primary impact is limited to the size of SEO firms’ survival space, rather than completely excluding SEO firms from the market. This extended analysis further confirms the robustness of the base model.

SEs should recognize the potential interactions between effectiveness and robustness, especially when the improvement in robustness generates spillover effects on effectiveness. This synergistic effect will not only enhance user experience, but it will also expand market size, thereby increasing overall profits while maintaining moderate competition among SEO firms. Therefore, SEs should adopt a comprehensive optimization strategy to fully exploit this spillover effect and achieve a win-win outcome.

This extension demonstrates that the interaction between robustness and effectiveness indeed affects the survival of SEO firms in the search engine marketing market, influencing the size of their survival space. However, it also suggests that even when effectiveness and robustness are not completely independent, the model’s primary conclusions remain qualitatively unchanged.

In addition to the aforementioned extensions, this study explores several other expanded scenarios, as detailed in Appendix C. These include: the integration of mobile and desktop search engine marketing (Section C2 of Appendix C), the use of PSM data by advertisers to guide SEO services (Section C5 of Appendix C), competition between SEs (Section C6 of Appendix C), and competition among advertisers (Section C7 of Appendix C). An in-depth analysis of these extended models confirms the robustness of the conclusions derived from the base model. For a comprehensive discussion of the extended models, please refer to Appendix C.

## 6 Managerial and Policy Implications

In this section, we present a comprehensive summary of our key findings and analyze their managerial and policy implications.

## 6.1 Managerial Insights

Based on the research findings, we further explore their application in managerial practice to assist SEs and SEO firms in formulating effective strategies for sustainable development.

First, SEs and SEO firms should establish a collaborative ecosystem to foster their coordinated development. SEs should not perceive SEO firms merely as competitors but should rather recognize their constructive role in optimizing the search ecosystem, enhancing platform market appeal, and improving profitability. To promote a robust search ecosystem, SEs should adopt more open strategies, such as providing optimization guidelines and increasing algorithm transparency, thereby incorporating SEO firms into their operational framework to enable coevolution. Such collaboration will boost the platform’s market competitiveness and ultimately foster a mutually beneficial relationship between SEs and SEO enterprises.

Second, when optimizing the algorithm, SEs should balance internal competition and the impact on SEO. When refining algorithm performance, SEs should fully consider their impact on SEO firms to ensure the sustainability of the platform ecosystem. Managers must recognize that algorithmic effectiveness is critical for enhancing platform performance. While optimizing algorithmic effectiveness may not always align with profit maximization, it may foster a more sustainable environment for SEO firms. SEs should conduct in-depth analyses of market dynamics and technological trends to find an optimal balance between improving algorithm effectiveness and maintaining SEO competition. When enhancing algorithmic effectiveness, SEs should adopt rational strategies to improve service attractiveness rather than imposing excessive constraints on the normal operations of SEO firms. Concurrently with persistent optimization of user experience, it is imperative to maintain healthy collaboration and foster mutual development with SEO firms.

Third, SEs should balance internal and external competition to ensure the sustainable development of their platforms. In the SEM market, SE revenue is shaped by internal competition, particularly between SEO firms and the SE, directly impacting short-term platform profitability. Simultaneously, platforms must navigate external competitive pressures, including rivalry among SEs and between mobile and desktop search markets. These factors shape the platform’s long-term appeal and indirectly impact user demand and advertising revenue. Managers should flexibly adjust strategies in response to market dynamics, balancing internal and external competition to maintain long-term platform viability while avoiding excessive exclusion of SEO firms, thereby achieving sustainable profitability growth.

Moreover, firms in the SEM market should adapt to new market dynamics and actively respond to the development of mobile search and AI. In the rapidly evolving SEM market, enterprises must adapt to technological advancements and the resulting market transformations. While optimizing the mobile search experience, it is crucial to fully leverage AI’s potential to enhance search efficiency, improve ad targeting precision, and personalize user experiences, while also actively addressing challenges related to information accuracy and credibility. Although AI may impact the SEO industry, the role of SEO in the SEM market remains significant. Search engine enterprises should adopt appropriate strategies to facilitate the integration of SEO and AI technologies rather than using AI to replace traditional SEO optimization. By fostering a collaborative ecosystem, SEs can strengthen their market position amid technological advancements and drive sustainable growth in the SEM market.

Finally, SEO firms should proactively adjust their strategies and actively integrate into the search engine ecosystem. SEO enterprises must acknowledge that actively integrating themselves into the search engine ecosystem, thereby contributing to content quality improvement, is crucial for fostering long-term mutually beneficial relationships with SEs and ensuring sustainable growth. In the context of technological advancement, SEO firms must adapt to mobile search trends, seize AIdriven opportunities, and leverage advanced technologies to enhance service capabilities and competitiveness. Additionally, SEO enterprises should actively utilize PSM data to provide data-driven optimization and create synergistic effects with advertisers. These initiatives mitigate direct competition with SEs and enhance core competitiveness in the evolving market landscape.

## 6.2 Policy Insights

Beyond firm-level decision-making, regulatory authorities play a crucial role in maintaining fair market competition and optimizing the user experience. Therefore, we further analyze relevant policy recommendations to promote the development of the search market.

First, regulators must take proactive measures to prevent market monopolization and curb SEs’ employment of “technical blockades” to suppress SEO firms. To uphold a fair and competitive search market, regulators should remain highly vigilant against SEs leveraging algorithmic adjustments and other technical means to restrict the growth of SEO enterprises. This concern is particularly relevant in markets where advertisers exhibit a lower willingness to pay, as SEs may have stronger incentives to diminish the influence of SEO enterprises to protect their advertising revenue. To mitigate these risks, regulators should establish a transparent algorithm oversight mechanism, requiring SEs to disclose the rationale behind core ranking adjustments to prevent the unfair exclusion of SEO firms. Strengthening market supervision and fair competition policies will foster a diversified search market while ensuring the stability and health of the industry ecosystem.

Second, regulators must safeguard the user experience and prevent information manipulation and content degradation. As the SEM industry evolves, regulators should enhance oversight and establish standards for search optimization practices to prevent both SEO firms and SEs from manipulating search results through improper methods for short-term gains. Such practices can compromise the user experience and undermine the fairness and effectiveness of search outcomes. Regulators should promote transparency in ranking mechanisms to ensure fairness in the search ecosystem and should develop a comprehensive content quality oversight system to penalize improper SEO practices as well as SEs’ abuse of algorithms. Furthermore, a user feedback mechanism should be established to enhance the market’s self-regulation capacity, ensuring the relevance and impartiality of search results and fostering the long-term healthy development of the industry.

Additionally, regulators must adapt to market changes and intensify mobile search and AI technology oversight. In response to the growing influence of mobile search and AI technology, authorities should develop targeted regulatory frameworks to uphold market fairness and ensure sustainable development. On the one hand, regulators should ensure transparency in mobile search ranking rules, preventing SEs from leveraging mobile platforms to suppress SEO firms. On the other hand, a regulatory framework for AI-generated content should be established to prevent low-quality or misleading AIgenerated information from saturating search results, thereby safeguarding the credibility of search content. Ultimately, regulators should guide SEO enterprises and SEs in the responsible application of AI to improve content quality, foster the healthy evolution of the search ecosystem, and achieve a balanced development between technological advancement and market fairness.

## 6.3 Theoretical Implications

This paper uses game theory modeling to analyze the dynamic competitive relationship between SEs and SEO firms in the advertising market. It challenges traditional assumptions, such as the maximization of exclusive monopoly profits and the exclusionary behavior of dominant platforms toward secondary competing service providers. The findings offer valuable insights for theoretical researchers.

First, traditional platform competition theory primarily focuses on zero-sum games between dominant platforms and their direct competitors. However, this study reveals that the “asymmetric symbiotic” relationship between SEs and SEOs can enhance overall market efficiency. This finding suggests that the interaction between platforms and affiliated service providers is not simply competitive but rather characterized by interdependence and co-opetition, which ultimately improves market performance. Consequently, researchers should develop more sophisticated game models that integrate multiple market participants within a “platform-affiliated service provider” dual-layer competition framework. This approach would enable the analysis of how affiliated service providers, such as SEOs, can influence platform strategies and user decisions through service differentiation. Such a model offers a fresh perspective on platform ecosystems and can guide future research in other areas of platform economics, particularly regarding the cooperation and competition between service platforms and affiliated service providers.

Second, this paper decouples algorithmic effectiveness and robustness as independent variables and examines their distinct impacts on market structure. This result provides key insights for researchers, particularly in platform economics and information retrieval. Theorists can apply this framework to explore the interactions of other technical attributes within platform algorithms. In particular, when analyzing market equilibrium, it is essential to distinguish the various attributes of technical parameters. For example, the model could be extended to the recommendation algorithms of social media platforms, where the balance between content quality and anti-spam mechanisms is crucial, or to the analysis of search ranking fairness and promotional tool competition on e-commerce platforms.

Finally, this paper extends the model to explore the impact of mobile search and AI technologies on market structure. Although these technological advancements have influenced market dynamics, they have not undermined the core conclusions of the model. This suggests that, when studying the impact of technological evolution on platform markets, theorists should consider both “change and continuity.” While technological development undoubtedly presents new challenges and opportunities, its effect on market competition is typically gradual rather than disruptive. Therefore, future research should focus on how technological evolution can profoundly impact existing platform competition frameworks, particularly in terms of how platforms adjust their competitive strategies while maintaining core business models and market equilibrium.

## 7 Conclusion

Search engine advertising is a complex and continually evolving area of the internet marketing industry, especially in relation to SEO. While significant research has been conducted in this field, certain aspects remain less explored. This paper establishes a model of the SE advertising market, analyzes the market share of PSM and SEO, and investigates SEO’s impact on the SE advertising market. Furthermore, the basic model is extended to examine the competitive dynamics between SEs and advertisers, assessing the impact of the evolving SEM market, including AI advancements and the widespread adoption of mobile search, to ensure the robustness of the conclusions. Through analyzing the survival of SEO firms, SE’s profits, and the dynamic competition between SEs and SEO firms, we obtained several interesting insights.

First, it is noteworthy that the presence of SEO firms in the market is not necessarily detrimental to SEs and may even increase their profitability. Although SEO can disturb SEs and potentially affect organic search results adversely (Xu et al., 2012), our findings suggest that eliminating SEO firms and monopolizing the advertising market does not optimize SE performance. Our extended model further illustrates that while market competition and technological advancements, such as the development of mobile search and the progress of AI, may influence the survival conditions of SEO companies, these factors do not fundamentally alter our conclusion: The presence of SEO could yield additional profits for SEs.

Secondly, an SE’s effectiveness is not strictly monotonically correlated with its optimal profit. Increasing an SE’s effectiveness can sometimes reduce its profitability. Furthermore, an SE’s robustness directly affects its decisions on effectiveness. When effectiveness is high, the cost dilution effect strengthens, lowering the average cost for advertisers to use SEO services. This, in turn, may heighten internal competition, reducing the SE’s market share and profitability.

Moreover, the survival of SEO companies is influenced by various factors, including advertisers’ willingness to pay and the SE’s effectiveness and robustness. Specifically, when advertisers exhibit a low willingness to pay, revenue from opting for SEO services may not cover fixed costs, making PSM advertising the preferred alternative. SEO firms can only thrive when advertisers show a strong willingness to pay. The SE’s effectiveness and robustness are pivotal in regulating the cost dilution effect and responding to market competition, exerting a notable influence on the survival of SEO companies.

Finally, the findings of this study reveal an interaction between the internal and external competition faced by SEs. Under external competitive pressure, SEs must improve their effectiveness to maintain a competitive edge. However, achieving external advantages by, for example, competing with mobile search engines and SEO firms can intensify the cost dilution effect. This, in turn, may weaken SEs’ internal competitive position, placing them at a disadvantage against SEO firms. Therefore, while striving to enhance external competitiveness, SEs must carefully balance internal and external competition to sustain long-term profitability.

There are several limitations in this study. First, the uniform distribution assumption of advertisers’ willingness to pay is simplistic. Second, the model is limited to advertisers in one industry. One possible extension is to model industry differences and advertiser differences with a hierarchical distribution, separating the two effects. The result could yield managerial insights in terms of market segmentation. Alternatively, a horizontal differentiation model could address advertiser heterogeneity in keyword preferences. This differentiation echoes the product differentiation of the online marketplace in reality because keywords, like consumer products, could also be differentiated. This alternative shifts the focus to advertisers’ profit and strategies. Future inquiries will benefit from these limitations and suggestions, allowing them to explore the search market and SEO more comprehensively.

## Acknowledgments

The authors would like to thank the senior editor, Kim Huat Goh, and the two anonymous reviewers for their constructive comments and insightful suggestions, which substantially improved the quality of this paper. This work was supported by the National Natural Science Foundation of China (Grant No. 72572088). The authors also gratefully acknowledge the efforts and support of the journal’s editorial office throughout the review and publication process. Chunyang Shen is the corresponding author.

## References

Agarwal, A., Hosanagar, K., & Smith, M. D. (2015). Do organic results help or hurt sponsored search performance? Information Systems Research, 26(4), 695-713.

Aswani, R., Kar, A. K., Ilavarasan, P. V., & Dwivedi, Y. K. (2018). Search engine marketing is not all gold: Insights from Twitter and SEOClerks. International Journal of Information Management, 38(1), 107-116.

Baeza-Yates, R. (2018). Bias on the web. Communications of the ACM, 61(6), 54-61.

Basu, A., Mazumdar, T., & Raj, S. (2003). Indirect network externality effects on product attributes. Marketing Science, 22(2), 209-221.

Berman, R., & Katona, Z. (2013). The role of search engine optimization in search marketing. Marketing Science, 32(4), 644-651.

Bhargava, H. K., & Feng, J. (2005). Recommendation bias in information gatekeepers. Working Paper Graduate School of Management.

Biancalana, C., Gasparetti, F., Micarelli, A., Sansonetti, G., & Technology. (2013). An approach to social recommendation for context-aware mobile services. ACM Transactions on Intelligent Systems 4(1), 1-31.

Blake, T., Nosko, C., & Tadelis, S. (2015). Consumer heterogeneity and paid search effectiveness: A large-scale field experiment. Econometrica, 83(1), 155-174.

Chen, J., Liu, D., & Whinston, A. B. (2009). Auctioning keywords in online search. Journal of Marketing, 73(4), 125-141.

Chen, X., Li, G., Li, S., & Zheng, Q. (2024). When should a sharing platform adopt the bilateral review system? MIS Quarterly 48(3), 1121-1156

Chen, Y. J. (2021). Optimal design of revenuemaximizing position auctions with consumer search. Production and Operations Management, 30(9), 3297-3316.

Chiou, L., & Tucker, C. (2022). How do restrictions on advertising affect consumer search? Management Science, 68(2), 866-882.

Compiani, G., Lewis, G., Peng, S., & Wang, P. (2024). Online search and optimal product rankings: An empirical framework. Marketing Science, 43(3), 615-636.

Dogpile. (n.d.). Different engines different results: Web searchers not always finding what they are looking for. http://www.assessmentpsychology. com/metasearch-analysis.pdf

Donnelly, R., Kanodia, A., & Morozov, I. (2024). Welfare effects of personalized rankings. Marketing Science, 43(1), 92-113.

Edelman, B., & Lai, Z. (2016). Design of search engine services: Channel interdependence in search engine results. Journal of Marketing Research, 53(6), 881-900.

Erdmann, A., Arilla, R., & Ponzoa, J. M. (2022). Search engine optimization: The long-term strategy of keyword choice. Journal of Business Research, 144, 650-662.

Galov, N. (2025). 20 Google update statistics: Why algorithm changes are vital for SEO? Web tribunal. https://webtribunal.net/blog/googleupdate-statistics/#gref

Garcia, J. E., Lima, R., & da Fonseca, M. J. S. (2022). Search engine optimization (SEO) for a company website. Proceedings of the World Conference on Information Systems and Technologies (pp. 524-531).

Ghose, A., Ipeirotis, P. G., & Li, B. (2019). Modeling consumer footprints on search engines: An interplay with social media. Management Science, 65(3), 1363-1385.

Ghose, A., & Yang, S. (2009). An empirical analysis of search engine advertising: Sponsored search in electronic markets. Management Science, 55(10), 1605-1622.

Gong, J., Abhisek, V., & Li, B. (2018). Examining the impact of keyword ambiguity on search advertising performance: A topic model approach. MIS Quarterly, 42(3), 805-829.

Gu, Z., & Tayi, G. K. (2023). Consumer self‐design and brand competition. Production and Operations Management 32(8), 2420-2437.

Gummerus, J., & Pihlström, M. (2011). Context and mobile services’ value-in-use. Journal of Retailing and Consumer Services 18(6), 521- 533.

Gupta, S., Jain, D. C., & Sawhney, M. S. (1999). Modeling the evolution of markets with indirect network externalities: An application to digital television. Marketing Science, 18(3), 396-416.

Ha, A. Y., Tong, S., & Zhang, H. (2011). Sharing demand information in competing supply chains with production diseconomies. Management Science 57(3), 566-581.

Haghirian, P., Madlberger, M., & Tanuskova, A. (2005). Increasing advertising value of mobile marketing-an empirical study of antecedents. Proceedings of the 38th Annual Hawaii International Conference on System Sciences.

Hartzer, B. (2022). Global SEO market to reach \$122.11 billion by 2028. BillHartzer.com. https://www.billhartzer.com/seo/global-seomarket-2028/

Hristova, N., & O’Hare, G. M. (2004). Ad-me: wireless advertising adapted to the user location, device and emotions. Proceedings of the 37th Annual Hawaii International Conference on System Sciences.

IAB. (2024). Internet advertising revenue report. https://www.iab.com/wp-content/uploads/ 2024/04/IAB\_PwC\_Internet\_Ad\_Revenue\_Re port\_2024.pdf

Jiang, Z. Z., Cui, S., He, N., Li, K., & Tian, L. (2023). Contract selection and piracy surveillance for video platforms in the age of social media. Production and Operations Management, 34(12), 3775-3792.

Jin, C., Yang, L., & Hosanagar, K. (2022). To brush or not to brush: Product rankings, consumer search, and fake orders. Information Systems Research, 34(2), 532-552.

Joo, M., Shi, J., & Abhishek, V. (2024). Do sellers benefit from sponsored product listings? Evidence from an online marketplace. Marketing Science, 43(4), 817-839.

Ju, J., Cho, D., Lee, J. K., & Ahn, J. H. (2021). Can it clean up your inbox? Evidence from South Korean anti‐spam legislation. Production and Operations Management, 30(8), 2636-2652.

Kannan, K., Pamuru, V., & Rosokha, Y. (2022). Analyzing frictions in generalized second-price auction markets. Information Systems Research, 34(4), 1437-1454.

Katona, Z., & Sarvary, M. (2010). The race for sponsored links: Bidding patterns for search advertising. Marketing Science, 29(2), 199-215.

Kim, A. J., & Balachander, S. (2023). Coordinating traditional media advertising and online advertising in brand marketing. Production and Operations Management, 32(6), 1865-1879.

Lee, Y. E., & Benbasat, I. (2003). Interface design for mobile commerce. Communications of the ACM 46(12), 48-52.

Lee, D., & Hosanagar, K. (2019). How do recommender systems affect sales diversity? A cross-category investigation via randomized field experiment. Information Systems Research, 30(1), 239-259.

Leffler, K. B. (1982). Ambiguous changes in product quality. The American Economic Review, 72(5), 956-967.

Liu, D., Chen, J., & Whinston, A. B. (2010). Ex ante information and the design of keyword auctions. Information Systems Research, 21(1), 133-153.

Liu, J., & Toubia, O. (2018). A semantic approach for estimating consumer content preferences from online search queries. Marketing Science, 37(6), 930-952.

Long, F., Jerath, K., & Sarvary, M. (2022). Designing an online retail marketplace: Leveraging information from sponsored advertising. Marketing Science, 41(1), 115-138.

Malaga, R. A. (2008). Worst practices in search engine optimization. Communications of the ACM, 51(12), 147-150.

Moreno, L., & Martinez, P. (2013). Overlapping factors in search engine optimization and web accessibility. Online Information Review, 37(4), 564-580.

Nagpal, M., & Petersen, J. A. (2021). Keyword selection strategies in search engine optimization: How relevant is relevance? Journal of Retailing, 97(4), 746-763.

Nie, C., Zheng, Z., & Sarkar, S. (2021). A strategic group analysis of competitor behavior in search advertising. Journal of the Association for Information Systems, 22(6), 1659-1685.

Okazaki, S., & Mendez, F. (2013). Exploring convenience in mobile commerce: Moderating effects of gender. Computers in Human Behavior 29(3), 1234-1242.

Ong, S. Q. (2024). Google search statistics to bookmark for 2024, ahrefsblog. https://ahrefs. com/blog/google-search-statistics/

Reisenbichler, M., Reutterer, T., Schweidel, D. A., & Dan, D. (2022). Frontiers: Supporting content marketing with natural language generation. Marketing Science, 41(3), 441-452.

Sambhara, C., Rai, A., Keil, M., & Kasi, V. (2017). Risks and controls in internet-enabled reverse auctions: Perspectives from buyers and suppliers. Journal of Management Information Systems, 34(4), 1113-1142.

Schultheiß, S., & Lewandowski, D. (2020). How users’ knowledge of advertisements influences their viewing and selection behavior in search engines. Journal of the Association for Information Science and Technology, 72(3), 285-301.

Shi, L., & Hu, B. (2024). Frontiers in operations: Battery as a service: Flexible electric vehicle battery leasing. Manufacturing & Service Operations Management 26(4), 1269-1285.

Statista. (2025). Advertising revenue of Google from 2001 to 2024. https://www.statista.com/ statistics/266249/advertising-revenue-ofgoogle/

Telang, R., & Mukhopadhyay, T. (2005). Drivers of web portal use. Electronic Commerce Research and Applications, 4(1), 49-65.

Telang, R., Rajan, U., & Mukhopadhyay, T. (2004). The market structure for Internet search engines. Journal of Management Information Systems, 21(2), 137-160.

Tunuguntla, V., Rakshit, K., & Basu, P. (2023). Bidding for an optimal portfolio of keywords in sponsored search advertising: From generic to branded keywords. European Journal of Operational Research, 307(3), 1424-1440.

Ursu, R. M. (2018). The power of rankings: Quantifying the effect of rankings on online consumer search and purchase decisions. Marketing Science, 37(4), 530-552.

Ursu, R. M., Zhang, Q., & Honka, E. (2023). Search gaps and consumer fatigue. Marketing Science, 42(1), 110-136.

White, A. (2013). Search engines: Left side quality versus right side profits. International Journal of Industrial Organization, 31(6), 690-701.

Xing, B., & Lin, Z. (2006). The impact of search engine optimization on online advertising market. Proceedings of the 8th International Conference on Electronic Commerce (pp. 519- 529).

Xu, H., Luo, X. R., Carroll, J. M., & Rosson, M. B. (2011). The personalization privacy paradox: An exploratory study of decision making process for location-aware marketing. Decision Support Systems 51(1), 42-52.

Xu, L., Chen, J., & Whinston, A. (2011). Price competition and endogenous valuation in search advertising. Journal of Marketing Research, 48(3), 566-586.

Xu, L., Chen, J., & Whinston, A. (2012). Effects of the

presence of organic listing in search advertising. Information Systems Research, 23(4), 1284- 1302.

Yang, J., Sahni, N. S., Nair, H. S., & Xiong, X. (2024). Advertising as information for ranking ecommerce search listings. Marketing Science, 43(2), 360-377.

Yang, S., & Ghose, A. (2010). Analyzing the relationship between organic and sponsored search advertising: Positive, negative, or zero interdependence? Marketing Science, 29(4), 602-623.

Yang, W., Xiao, B., & Wu, L. (2020). Learning and pricing models for repeated generalized secondprice auction in search advertising. European Journal of Operational Research, 282(2), 696- 711.

Yang, Y., Zhao, K., Zeng, D. D., & Jansen, B. J. (2022). Time-varying effects of search engine advertising on sales—An empirical investigation in e-commerce. Decision Support Systems, 163, Article 113843.

Zhang, D., Adipat, B., & Mowafi, Y. (2009). Usercentered context-aware mobile applications: The next generation of personal mobile computing. Communications of the Association for Information Systems 24, 27-46.

Zhang, S., & Cabage, N. (2017). Search engine optimization: Comparison of link building and social sharing. Journal of Computer Information Systems, 57(2), 148-159.

Zhang, X., & Feng, J. (2011). Cyclical bid adjustments in search-engine advertising. Management Science, 57(9), 1703-1719.

Zhong, Z. (2023). Platform search design: The roles of precision and price. Marketing Science, 42(2), 293-313.

Zhuang, M., Fang, E., Lee, J., & Li, X. (2021). The effects of price rank on clicks and conversions in product list advertising on online retail platforms. Information Systems Research, 32(4), 1412-1430.

## Appendix A: Proofs of Propositions and Theorems

## Proof of Proposition 1

Based on the equation presented in Section 4.2, it can be deduced that in the absence of SEO companies in the market, the search engine’s profit derived from PSM services is given by the expression $\begin{array} { r } { \pi _ { I } = \frac { 1 } { 2 } V \alpha q _ { e } r _ { s } - \frac { 1 } { 2 } \xi q _ { e } ^ { 2 } } \end{array}$ . Additionally, the function $\pi _ { I }$ is convex with respect to the effectiveness $q _ { e } ,$ . Consequently, by calculating the first derivative, the optimal decision for the search engine can be determined as $\begin{array} { r } { q _ { e } = \frac { V \alpha r _ { s } } { 2 \xi } } \end{array}$ . The absence of SEO companies in the market implies that the effectiveness and robustness of the search engine must satisfy $\begin{array} { r } { V < \frac { \lambda q _ { r } } { q _ { e } \alpha r _ { o } } . } \end{array}$ , which can be equivalently expressed as $q _ { e } <$ $\frac { \lambda q _ { r } } { V \alpha r _ { o } }$ . Hence, in the case where $\frac { V \alpha r _ { s } } { 2 \xi } < \frac { \lambda q _ { r } } { V \alpha r _ { o } } ;$ or equivalently, when the robustness condition $\frac { V ^ { 2 } \alpha ^ { 2 } r _ { s } r _ { 0 } } { 2 \lambda \xi } < q _ { r }$ is satisfied, the optimal decision for the search engine is $\begin{array} { r } { q _ { e } ^ { * } = \frac { V \alpha r _ { s } } { 2 \xi } } \end{array}$ , resulting in the optimal profit of $\begin{array} { r } { \pi _ { I } ^ { * } = \frac { V ^ { 2 } \alpha ^ { 2 } r _ { s } ^ { 2 } } { 8 \xi } . } \end{array}$ . Otherwise, the search engine can only choose the boundary values, where $\begin{array} { r } { q _ { e } ^ { * } = \frac { \lambda q _ { r } } { V \alpha r _ { o } } } \end{array}$ , and $\begin{array} { r } { \pi _ { I } ^ { * } = \frac { \lambda q _ { r } ( V ^ { 2 } \alpha ^ { 2 } r _ { s } r _ { o } - \lambda \xi q _ { r } ) } { 2 V ^ { 2 } \alpha ^ { 2 } r _ { o } ^ { 2 } } } \end{array}$ . Therefore, Proposition 1 is proven.

## Proof of Proposition 2

Similar to Proposition 1, when there is SEO in the market but no SEO + PSM, i.e., $\begin{array} { r } { \frac { \lambda q _ { r } } { V \alpha r _ { o } } < q _ { e } < \frac { \lambda q _ { r } } { V \alpha \gamma r _ { 0 } } , } \end{array}$ , the profit obtained by the search engine can be expressed as $\begin{array} { r } { \pi _ { I I } = \frac { 1 } { 2 } [ q _ { r } ( \lambda + \frac { 2 \lambda r _ { s } } { r _ { \mathrm { o } } } ) + V \alpha q _ { e } ( r _ { s } - r _ { \mathrm { { o } } } ) ] - \frac { 1 } { 2 } \xi q _ { e } ^ { 2 } } \end{array}$ . It can be observed that the search engine achieves the optimal profit when $\begin{array} { r } { q _ { e } = \frac { V \alpha ( r _ { s } - \bar { r _ { 0 } } ) } { 2 \xi } } \end{array}$ . However, due to the constraint $\begin{array} { r } { q _ { e } = \frac { V \alpha ( r _ { s } - r _ { 0 } ) } { 2 \xi } < 0 } \end{array}$ and $\begin{array} { r } { \frac { { \partial \pi _ { I I } } } { { \partial q _ { e } } } < 0 } \end{array}$ , the optimal decision for advertisers in this case is $\begin{array} { r } { q _ { e } ^ { * } = \frac { V \alpha r _ { s } } { 2 \xi } } \end{array}$ , and the optimal profit is $\begin{array} { r } { \pi _ { I I } ^ { * } = \frac { \lambda q _ { r } ( 3 V ^ { 2 } \alpha ^ { 2 } r _ { s } r _ { o } - \lambda \xi q _ { r } ) } { 2 V ^ { 2 } \alpha ^ { 2 } r _ { o } ^ { 2 } } } \end{array}$

## Proof of Proposition 3

The proof process for Proposition 3 follows a similar approach as that of Proposition 1; hence, the detailed proof procedure is omitted here.

## Proof of Theorem 1

The optimal decisions of the search engine under different scenarios can be derived from Proposition 1, Proposition 2, and Proposition 3. To facilitate the analysis, let

$$
\pi_ {I 1} ^ {*} = \frac {\lambda q _ {r} (V ^ {2} \alpha^ {2} r _ {s} r _ {o} - \lambda \xi q _ {r})}{2 V ^ {2} \alpha^ {2} r _ {o} ^ {2}};
$$

$$
\pi_ {I 2} ^ {*} = \frac {V ^ {2} \alpha^ {2} r _ {S} ^ {2}}{8 \xi};
$$

$$
\pi_ {I I} ^ {*} = \frac {\lambda q _ {r} (3 V ^ {2} \alpha^ {2} r _ {s} r _ {o} - \lambda \xi q _ {r})}{2 V ^ {2} \alpha^ {2} r _ {o} ^ {2}};
$$

$$
\pi_ {I I I 1} ^ {*} = \frac {V ^ {2} \alpha^ {2} \gamma r _ {o} [ r _ {s} - (1 - \gamma) r _ {o} ] ^ {2} + 8 \lambda \xi q _ {r} [ (1 + \gamma) r _ {s} - (1 - \gamma) r _ {o} ]}{8 \gamma \xi r _ {o}};
$$

$$
\pi_ {I I I 2} ^ {*} = \frac {\lambda q _ {r} \{V ^ {2} \alpha^ {2} \gamma r _ {o} [ (3 + 2 \gamma) r _ {s} - 3 (1 - \gamma) r _ {o} ] - \lambda \xi q _ {r} \}}{2 V ^ {2} \alpha^ {2} \gamma^ {2} r _ {o} ^ {2}};
$$

For the search engine, if eliminating the existing SEO companies in the market is the optimal choice, the following conditions need to be satisfied simultaneously:

① When $\begin{array} { r } { q _ { r } < \frac { V ^ { 2 } \alpha ^ { 2 } \gamma r _ { o } [ r _ { s } - ( 1 - \gamma ) r _ { o } ] } { 2 \lambda \xi } ; } \end{array}$ it is necessary for both $\pi _ { I I } ^ { * } < \pi _ { I 1 } ^ { * }$ and $\pi _ { I I I 1 } ^ { * } < \pi _ { I 1 } ^ { * }$ to hold simultaneously.

② $\begin{array} { r } { \mathrm { W h e n } \frac { V ^ { 2 } \alpha ^ { 2 } \gamma r _ { o } [ r _ { s } - ( 1 - \gamma ) r _ { 0 } ] } { 2 \lambda \xi } < q _ { r } < \frac { V ^ { 2 } \alpha ^ { 2 } r _ { s } r _ { 0 } } { 2 \lambda \xi } } \end{array}$ , it is necessary for both $\pi _ { I I } ^ { * } < \pi _ { I 1 } ^ { * }$ and $\pi _ { I I I 2 } ^ { * } < \pi _ { I 1 } ^ { * }$ to hold simultaneously.

③ When $\frac { V ^ { 2 } \alpha ^ { 2 } r _ { s } r _ { 0 } } { 2 \lambda \xi } < q _ { r }$ , it is required that a $\pi _ { I I } ^ { * } < \pi _ { I 2 } ^ { * }$ and $\pi _ { I I I 2 } ^ { * } < \pi _ { I 2 } ^ { * }$ hold simultaneously.

In other words, irrespective of whether the robustness of this search engine is high or low, the profit achieved by eliminating SEO companies, denoted as $\pi _ { I i } ^ { * } ( \mathrm { i } = 1 , 2 )$ , must be globally maximized. However, when $\begin{array} { r } { q _ { r } < \frac { V ^ { 2 } \alpha ^ { 2 } r _ { s } r _ { 0 } } { 2 \lambda \xi } } \end{array}$ , it can be easily deduced that $\pi _ { I 1 } ^ { * } < \pi _ { I I } ^ { * }$ holds consistently. Furthermore, when $\frac { V ^ { 2 } \alpha ^ { 2 } r _ { s } r _ { 0 } } { 2 \lambda \xi } < q _ { r }$ , eliminating SEO companies is the optimal choice for this search engine only if the following conditions are simultaneously satisfied: $\begin{array} { r } { \frac { r _ { 0 } - r _ { s } } { r _ { 0 } } < \gamma \leq \gamma _ { 1 } } \end{array}$ and $0 < V < V _ { 1 } , \mathrm { o r } \gamma _ { 1 } < \gamma \leq 1$ and $0 < V < V _ { 2 }$

Here, $\gamma _ { 1 }$ satisfies $\begin{array} { r } { \gamma _ { 1 } ( 3 6 r _ { \mathrm { s } } ^ { 2 } - 3 6 r _ { \mathrm { s } } r _ { \mathrm { o } } ) + \gamma _ { 1 } ^ { 4 } ( 7 r _ { \mathrm { s } } ^ { 2 } - 1 2 r _ { \mathrm { s } } r _ { \mathrm { o } } - 3 6 r _ { \mathrm { o } } ^ { 2 } ) + \gamma _ { 1 } ^ { 2 } ( - 4 6 r _ { \mathrm { s } } ^ { 2 } + 1 0 8 r _ { \mathrm { s } } r _ { \mathrm { o } } - 3 6 r _ { \mathrm { o } } ^ { 2 } ) + \gamma _ { 1 } ^ { 3 } ( - 1 2 r _ { \mathrm { s } } ^ { 2 } - 1 2 r _ { \mathrm { s } } r _ { \mathrm { o } } ) \gamma _ { 1 } ( - 3 6 r _ { \mathrm { s } } ^ { 2 } + 1 2 r _ { \mathrm { s } } ^ { 2 } ) \gamma _ { 2 } ( - 4 6 r _ { \mathrm { s } } ^ { 2 } + 1 2 r _ { \mathrm { s } } r _ { \mathrm { o } } ^ { 2 } ) } \end{array}$ $6 0 r _ { 5 } r _ { 0 } + 7 2 r _ { 0 } ^ { 2 } ) - r _ { s } ^ { 2 } = 0 ;$

$V _ { 1 }$ satisfies $4 \lambda ^ { 2 } \xi ^ { 2 } q _ { r } ^ { 2 } - 1 2 \alpha ^ { 2 } \lambda \xi V _ { 1 } ^ { 2 } q _ { r } r _ { s } r _ { 0 } + \alpha ^ { 4 } V _ { 1 } ^ { 4 } r _ { s } ^ { 2 } r _ { 0 } ^ { 2 } = 0$ ; and $V _ { 2 }$ is a solution for $4 \lambda ^ { 2 } \xi ^ { 2 } q _ { r } ^ { 2 } + V _ { 2 } ^ { 4 } \alpha ^ { 4 } \gamma ^ { 2 } r _ { s } ^ { 2 } r _ { 0 } ^ { 2 } +$ $V _ { 2 } ^ { 2 } ( 1 2 \alpha ^ { 2 } \gamma \lambda \xi q _ { r } r _ { 0 } ^ { 2 } - 1 2 \alpha ^ { 2 } \gamma \lambda \bar { \xi } q _ { r } r _ { s } r _ { 0 } - 8 \alpha ^ { 2 } \gamma ^ { 2 } \lambda \bar { \xi } q _ { r } r _ { s } r _ { 0 } - 1 2 \alpha ^ { 2 } \gamma ^ { 2 } \lambda \bar { \xi } q _ { r } r _ { 0 } ^ { 2 } ) = 0$

Hence, eliminating SEO companies in the market is not an advantageous strategy for the search engine. In other words, from an overall perspective, SEO companies will continue to exist in the market.

## Proof of Proposition C1, Theorem C1, and Theorem C2

Based on the proof processes of the relevant conclusions in the basic model, it is observed that the proof processes of Proposition C1, Theorem C1, and Theorem C2 share similarities. Therefore, we have omitted the detailed proof processes here.

## Appendix B: Numerical Analysis

![](/api/attachments/EM976JN4/fulltext/images/e40a4fbf1a9ac66ab434dbff7fcb7f5221abee67dccf717918bc87d267f1aeb7.jpg)  
(a) Basic model

![](/api/attachments/EM976JN4/fulltext/images/466014077c36a3a9655a3de0e787900fcbb3ffd25bb51795bf16bf0f32d704dc.jpg)  
(b) There is competition among SEs

![](/api/attachments/EM976JN4/fulltext/images/406814000d24a304dfbb2c23ad066a2d958662c38d96a94daf8c7a89b6b970c5.jpg)  
(c) There is competition among Ads  
Figure A1. The Profits of SE(s) in the Basic Model and the Extended Model

Figure A1 illustrates the correlation between the profitability and robustness of the search engine (SE) in both the basic and competitive models. Figure A1 further corroborates the main conclusion of this paper, which suggests that eliminating SEO companies from the market is not necessarily the optimal choice for the SE. As previously mentioned, the existence of SEO companies in the market introduces internal competition pressures for the SE, driving it to constantly innovate its technology to improve its efficacy. The improvement in effectiveness helps attract more advertisers to the SE, thereby increasing its revenue.

Furthermore, an intriguing phenomenon deserves attention: contrary to intuition, when there is competition among search engines, the SE tends to achieve higher profits, regardless of the presence of SEO companies in the market. However, when there is competition among advertisers, the SE may experience lower levels of profitability compared to the basic model. This suggests that competition with other search engines can be advantageous for the SE, as external competition compels it to enhance its effectiveness to attract advertisers and elevate its revenue. Nevertheless, competition among advertisers may adversely affect the search engine’s optimal profit in contrast to the basic model. One possible explanation is that competition among advertisers may lead to increased costs for some advertisers, causing them to exit the market and consequently exert a negative effect on the search engine’s optimal profit.

Therefore, for the search engine, competing with other companies may be an effective strategy to attract more advertisers and increase revenue by enhancing its effectiveness. However, excessive competition among advertisers can adversely affect the search engine’s optimal profit, necessitating careful management of competition among advertisers. Preserving the presence of SEO companies in the market helps foster internal competition, driving innovation and improving the effectiveness of the search engine. Overall, the interplay between competition in the search engine market and competition among advertisers requires managers to consider a holistic approach to achieve the search engine’s optimal profit.

Therefore, for the search engine, competing with other companies may be an effective strategy to attract more advertisers and increase revenue by enhancing its effectiveness. However, excessive competition among advertisers can negatively impact the search engine’s optimal profit, necessitating the need for careful management of advertiser competition. The presence of SEO firms in the market fosters internal competition, stimulating innovation and improving the search engine’s effectiveness. In conclusion, the interaction between competition in the search engine market and competition among advertisers calls for managers to adopt a comprehensive approach to attain the search engine’s optimal profit.

## Appendix C: Model Extensions

## C1. Search Engine Marketing on the Mobile Platform

The widespread adoption of smartphones and the rapid growth of mobile internet have positioned mobile search traffic as a central element of the search engine market. Recent statistics indicate that approximately 68.22% of search traffic originates from mobile devices, while only 30.2% comes from desktop devices.<sup>7</sup> This shift highlights a significant transition in search behavior, with mobile devices now dominating the landscape. Consequently, this trend has amplified the importance of mobile search within the search engine ecosystem and catalyzed further transformation in search engine marketing.

As more users access websites via mobile devices, search engines increasingly prioritize mobile content for indexing and ranking. In 2016, for example, Google announced that its crawling, indexing, and ranking processes would primarily be based on the mobile version of websites.<sup>8</sup> This strategic shift has accelerated the optimization of search engines for mobile platforms.

Compared to traditional desktop search, mobile search presents several distinct advantages.

First, mobile search offers enhanced convenience and greater flexibility (Gummerus & Pihlström, 2011; Okazaki & Mendez, 2013). It enables users to search anytime and anywhere, meeting their on-the-go needs. According to the China Internet Network Information Center, internet users using desktop devices primarily access the web from fixed locations, such as homes, workplaces, or internet cafes. In contrast, mobile users are more likely to access the web in dynamic settings, such as homes, dormitories, and classrooms. The compact size and portability of smartphones, coupled with the widespread availability of WiFi and 4G/5G networks, eliminate many of the time and location constraints associated with desktop search. Conversely, desktop search relies on stable hardware, such as keyboards and mice, which limits its usage flexibility.

Furthermore, mobile search is particularly effective in addressing users’ personalized needs (Biancalana et al., 2013; Hristova & O’Hare, 2004; Xu et al., 2011; Zhang et al., 2009). Mobile devices can access users’ location data and offer precise search recommendations tailored to their daily behaviors. For instance, relevant content can be recommended based on users’ browsing history, or nearby points of interest can be suggested based on their current location. This personalization improves the user experience and enhances the overall value of search engine services.

However, the limited screen size of mobile devices presents challenges for information presentation (Haghirian et al., 2005; Lee & Benbasat, 2003). Smaller screens restrict the amount of content displayed on a single page, which can hinder information retrieval efficiency. Compared to desktop search, mobile search may diminish the user experience when navigating complex webpages or lengthy articles, particularly when dealing with intricate webpages or extended texts.

Moreover, mobile search complicates SEO optimization. Unlike desktop SEO, mobile SEO requires consideration of a wider range of factors. For instance, aspects such as location data, screen size, the dimensions of buttons and links, layout, and spacing optimization are crucial to prevent accidental clicks. Additionally, the simplicity of page design, loading speed, touch-friendliness, and responsive design are key to successful mobile SEO. These considerations compel SEO firms to adapt more thoroughly to user behavior patterns and device characteristics during optimization.

Building on this analysis, we have expanded the base model to emphasize the characteristics of mobile search engines. In the mobile environment, the utility function for advertisers choosing a PSM strategy is defined as follows:

$$
u _ {1} ^ {m} = r _ {s} \alpha q _ {e} ^ {m} (1 - \theta_ {1} ^ {m}) (1 + \theta_ {2} ^ {m}) (v _ {1} - p)\tag{A1}
$$

In this context, the superscript m represents the scenario within the mobile search environment, where $\theta _ { 1 } ^ { m }$ reflects the impact of reduced search information volume and lower information retrieval efficiency on the user scale, assuming all other conditions remain the same. Conversely, $\theta _ { 2 } ^ { m }$ signifies the positive impact of mobile search’s convenience and personalization features on the user scale. When advertisers opt for an SEO strategy, the utility they can derive is as follows:

$$
u _ {2} ^ {m} = r _ {o} \alpha q _ {e} ^ {m} (1 - \theta_ {1} ^ {m}) (1 + \theta_ {2} ^ {m}) v _ {1} - \lambda (1 + \theta_ {3} ^ {m}) q _ {r}\tag{A2}
$$

Here, the term $\theta _ { 3 } ^ { m }$ denotes the additional costs that SEO firms must incur to meet mobile users’ demands, with all other conditions held constant. Specifically, when $\theta _ { 3 } ^ { m } = 1$ , mobile search does not influence the difficulty of SEO optimization.

Similarly, the utility that advertisers can gain from choosing the SEO + PSM strategy is represented as:

$$
u _ {3} = \gamma r _ {o} \alpha q _ {e} ^ {m} (1 - \theta_ {1} ^ {m}) (1 + \theta_ {2} ^ {m}) v _ {1} - \lambda (1 + \theta_ {3} ^ {m}) q _ {r} + r _ {s} \alpha q _ {e} ^ {m} (1 - \theta_ {1} ^ {m}) (1 + \theta_ {2} ^ {m}) (v _ {1} - p)\tag{A3}
$$

The procedure for solving the optimal decision and profits of the search engine (SE) is analogous to that of the benchmark model presented in Section 4. Consequently, the solution process is not detailed here. Similarly, the solution procedures for other extended models in Appendix C are also omitted. By comparing the utility of advertisers under different scenarios, the profit function of search engines and the market share of mobile search engines can be derived. After a comparative analysis, Lemma 1 can be obtained.

Lemma C1: When $\frac { \theta _ { 2 } ^ { m } } { 1 + \theta _ { 2 } ^ { m } } < \theta _ { 1 } ^ { m }$ , SEO firms’ survival in the mobile search market becomes more challenging. In comparison to the traditional desktop search market, if SEO competition exists, the SE will increase the price of PSM. Conversely, when $\begin{array} { r } { \theta _ { 1 } ^ { m } < \frac { \theta _ { 2 } ^ { m } } { 1 + \theta _ { 2 } ^ { m } } , } \end{array}$ SEO firms will enjoy greater survival space in the mobile search marketing market, and in this scenario, facing competition from SEO firms, the SE will opt to lower the PSM price.

Theorem C1: SEO firms will not be driven out of the mobile search market by SEs. In other words, the presence of SEO benefits mobile search engines as well.

p  
![](/api/attachments/EM976JN4/fulltext/images/7597b47941dfa17519c4c818807f923a6a371cd1e1aaff43e66cae431f6a082a.jpg)  
(a) (1 −0) (1 + θ7) < 1  
p

![](/api/attachments/EM976JN4/fulltext/images/bed1252c66a65d2464756714840bf412e489abb2fcac026ee8155de0dae91f62.jpg)  
(b) (1 −θ) (1 + θ2) > 1  
Figure C1. Market Share of the Mobile Search Engine

Lemma C1 and Theorem C1 illustrate the survival conditions for SEO firms and the shifts in market share within the mobile search engine marketing landscape. Specifically, when mobile search engines have low information retrieval efficiency, SEO firms face heightened survival challenges. As shown in Figure C2, when $\theta _ { 1 } ^ { m }$ increases, the survival space for SEO firms diminishes, especially compared to desktop search engines.

However, when the negative impact of mobile search engines on information retrieval efficiency is minimal, or when users place higher demands on convenience, SEO firms will find it easier to thrive in the mobile search engine marketing market. This is largely due to the fact that the efficiency and convenience of mobile search directly influence the total number of searchers. When mobile search exhibits higher information retrieval efficiency or users demand greater convenience, it attracts more searchers, thereby amplifying the effect of cost dilution. Specifically, when advertisers choose SEO, a greater cost dilution effect significantly reduces the survival pressure on SEO firms, thus providing them with more survival space. In this case, the competitiveness of PSM in the search engine marketing market diminishes, prompting the SE to lower PSM prices in order to enhance market competitiveness.

Second, in the mobile search market, the efficiency of information retrieval and convenience significantly affect the survival prospects of SEO firms. However, these factors do not alter the core conclusion of the base model—that the existence of SEO firms in the search engine marketing market is likely more beneficial to search engines. This suggests that, despite certain changes in the characteristics and structure of mobile search, these changes have not fundamentally affected the key conclusions derived from desktop search. Consequently, even in the mobile search environment, search engines do not need to eliminate SEO firms from the market.

p  
![](/api/attachments/EM976JN4/fulltext/images/c21f15d50c0c61c124a7960d7a65bd9f5110d8b61b0d3fd1ebe9237192973577.jpg)  
(a)

![](/api/attachments/EM976JN4/fulltext/images/6a893d4b0678055a3ff20442dae83e6fd59a780802629b680e624fa62036a8b8.jpg)  
(b)  
Figure C2. Changes in the Survival Space of SEO Companies in Mobile Search

## C2. Search Engine Marketing in Mobile-Desktop Integration

The rapid proliferation of mobile SEs has led an increasing number of platforms to operate both mobile and desktop search services. Although mobile and desktop SEs operate under the same platform, competition persists. Understanding how the interplay of competition and cooperation between mobile and desktop SEs influences the survival of SEO firms has become a crucial question of inquiry. To examine this issue in depth, we extend the basic model to analyze the impact of mobile search engine competition on the survival environment of SEO firms.

First, it is important to recognize that there is indeed competition between mobile and desktop search engines. However, this competition differs from the third-party competition discussed in Extended Model C6. On one hand, while there is competition for user traffic, both types of search engines belong to the same ecosystem and share the same brand, technology, and databases. Furthermore, user behavior across different devices may influence each other. For example, although the content of webpages on mobile and desktop platforms may not be identical, some pages may overlap, whether they are ranked via SEO or PSM.

Based on the above analysis, we further develop an extended model to explore the impact of mobile search engine competition on the search engine marketing market. As in Extended Model C1, we assume that the validity of the desktop search engine algorithm is represented by $q _ { e 1 } ^ { m { \bar { c } } }$ , and the validity of the mobile search engine algorithm is represented by $q _ { e 2 } ^ { m c }$

![](/api/attachments/EM976JN4/fulltext/images/8b0a9db6fbd53a51f1526778ad1608beb35a54fee6aaf1e90fe18fc9d9d81509.jpg)

![](/api/attachments/EM976JN4/fulltext/images/62e78abbde3dfb14ac576a1991806cc6a3e5bdccce5f7e4aeee832c12c395b58.jpg)  
where??<sub>1</sub> = (?? + ?? − ????)??<sub>??1</sub><sup>????</sup> + [???? − ??(1 − ??<sub>1</sub><sup>????</sup>)(1 + ??<sub>2</sub><sup>????</sup>2)(1 − ??)]??<sub>??2</sub><sup>????</sup>  
Figure C3. Market Share of the Search Engine Under Mobile Search Engine Competition

In the context of mobile search engine competition, the utility that advertisers can obtain when selecting the PSM strategy is as follows:

$$
\begin{array}{r} u _ {1} ^ {m c} = r _ {s} \{\alpha q _ {e 1} ^ {m c} + \beta [ q _ {e 1} ^ {m c} - (1 - \theta_ {1} ^ {m c}) (1 + \theta_ {2} ^ {m c}) q _ {e 2} ^ {m c} ] (v _ {1} - p) + \rho r _ {s} (v _ {1} - p) \} \\ - p) \{\alpha q _ {e 2} ^ {m c} + \beta [ (1 - \theta_ {1} ^ {m c}) (1 + \theta_ {2} ^ {m c}) q _ {e 2} ^ {m c} - q _ {e 1} ^ {m c} ] \} \end{array}\tag{A4}
$$

Here, the superscript mc indicates the scenario involving mobile search engine competition. $\theta _ { 1 } ^ { m c }$ and $\theta _ { 2 } ^ { m c }$ represent the impact of mobile search’s information retrieval efficiency and convenience on user scale, under the same validity conditions. In the presence of mobile competition, the number of searchers is denoted by $q _ { e 1 } ^ { m c } \alpha + \beta [ q _ { e 1 } ^ { m c } - ( 1 -$ $\theta _ { 1 } ^ { m c } ) ( 1 + \theta _ { 2 } ^ { m c } ) ] q _ { e 2 } ^ { m c }$ , with the second term indicating the impact of mobile competition on the desktop user base. $\rho$ represents the influence of advertisers’ desktop rankings on their mobile rankings. Specifically, the probability that the desktop ranking is consistent with the mobile ranking.

Similarly, the utility that advertisers can gain when selecting the SEO strategy is as follows:

$$
\begin{array}{r} u _ {2} ^ {m c} = r _ {o} v _ {1} \{\alpha q _ {e 1} ^ {m c} + \beta [ q _ {e 1} ^ {m c} - (1 - \theta_ {1} ^ {m c}) (1 + \theta_ {2} ^ {m c}) q _ {e 2} ^ {m c} ] \} \\ + \rho r _ {o} v _ {1} \{\alpha q _ {e 2} ^ {m c} + \beta [ (1 - \theta_ {1} ^ {m c}) (1 + \theta_ {2} ^ {m c}) q _ {e 2} ^ {m c} - q _ {e 1} ^ {m c} ] \} - \lambda q _ {r} \end{array}\tag{A5}
$$

The utility that advertisers can derive from choosing the SEO+PSM strategy is as follows:

$$
\begin{array}{r l} & u _ {3} ^ {m c} = \gamma r _ {o} v _ {1} \{\alpha q _ {e 1} ^ {m c} + \beta [ q _ {e 1} ^ {m c} - (1 - \theta_ {1} ^ {m c}) (1 + \theta_ {2} ^ {m c}) q _ {e 2} ^ {m c} ] \\ & \qquad + \rho \gamma r _ {o} v _ {1} \{\alpha q _ {e 2} ^ {m c} + \beta [ (1 - \theta_ {1} ^ {m c}) (1 + \theta_ {2} ^ {m c}) q _ {e 2} ^ {m c} - q _ {e 1} ^ {m c} ] \} - \lambda q _ {r} + r _ {s} \{\alpha q _ {e 1} ^ {m c} \\ & \qquad + \beta [ q _ {e 1} ^ {m c} - (1 - \theta_ {1} ^ {m c}) (1 + \theta_ {2} ^ {m c}) q _ {e 2} ^ {m c} ] (v _ {1} - p) + \rho r _ {s} (v _ {1} \\ & \qquad - p) \{\alpha q _ {e 2} ^ {m c} + \beta [ (1 - \theta_ {1} ^ {m c}) (1 + \theta_ {2} ^ {m c}) q _ {e 2} ^ {m c} - q _ {e 1} ^ {m c} ] \} \end{array}\tag{A6}
$$

Using the profit function of the ${ \mathrm { S E } } ,$ we can determine the optimal decisions and profits for the SE in this context.

Lemma C2: $\begin{array} { r } { \mathrm { W h e n } \frac { 1 + q _ { e 2 } ^ { m c } [ \beta \left( 1 - \theta _ { 1 } ^ { m c } \right) \left( 1 + \theta _ { 2 } ^ { m c } \right) \left( 1 - \rho \right) - \alpha \rho ] } { \alpha + \beta - \beta \rho } < q _ { e 1 } ^ { m c } } \end{array}$ SEO firms in desktop search are able to secure a larger survival space. In this scenario, as a response to competition among SEO firms, search engines will opt to lower the price of PSM. Otherwise, SEO firms will face greater survival pressure, and in the context of competition with SEO, the price of PSM will decrease accordingly.

Theorem C2: When both desktop and mobile search engines coexist, ensuring the survival of SEO firms remains the optimal strategy for the SE in the search engine marketing market.

Lemma C2 and Theorem C2 analyze how the characteristics of a mobile search engine affect the survival environment of desktop SEO firms when there is competition between mobile and desktop search engines. Through Lemma C2, we observe that as the effectiveness of mobile search engines increases, the survival pressure on desktop SEO firms gradually rises. This is primarily due to the competitive relationship between mobile and desktop search engines, where an increase in mobile search engine effectiveness weakens the overall competitiveness of desktop search engines, thereby impacting their user base. When the effectiveness of the mobile search engine is relatively high, the number of desktop Searchers decreases, significantly mitigating the negative impact of the cost dilution effect on the search engine. Under such circumstances, SEO firms’ survival in the search engine marketing market becomes more challenging. On the other hand, if the desktop search engine is more attractive, the negative effects of the cost dilution effect are exacerbated, thus providing SEO firms with more room for survival.

The above conclusions suggest that even though there exists a positive spillover effect between mobile and desktop search engines, the search engine must balance internal and external competition to achieve higher overall profits. Moreover, although the competition from the mobile search engine affects the survival space of SEO firms, it does not completely drive them out of the market. The competition between mobile and desktop search engines, although different from the competition within search engines, does not alter the core conclusion of the model that maintaining the survival of SEO firms can help search engines achieve higher overall profits.

Our findings indicate that whether in a purely mobile environment or in a competitive scenario involving both mobile and desktop search engines, the main conclusions remain robust. The prevalence of mobile search does not significantly affect the conclusions of the basic model, which further reinforces the universality and practical significance of the research.

## C3. Impact of AI on Search Engine Marketing

In recent years, advancements in machine learning and deep learning have driven the rapid development of artificial intelligence (AI) systems. Currently, AI influences search engines in two primary ways: The first mode involves search engines integrating and synchronizing large models, focusing on incorporating generative AI capabilities into the search process. For example, Bing has integrated the ChatGPT language model, Baidu uses ERNIE Bot to introduce “AI-powered Q&A” on its search page, and Google has launched “AI Overviews” through generative AI models. Since Microsoft introduced New Bing with the “ChatGPT + Search” model, major players such as Baidu, Google, and 360 have followed by implementing “Search + Large Models” strategies to redefine their search capabilities and secure market share in the next generation of intelligent search. For example, Baidu has prioritized the integration of generative AI technology into Baidu Search as a central initiative to adopting large-model technologies. In May 2024, during the first-quarter earnings call, Baidu’s founder, chairman, and CEO, Robin Li, revealed that 11% of search results on Baidu Search were generated by AI. With this integration, Baidu Search has evolved from simple text-based input and result matching to an intelligent search engine, enhancing its ability to understand user queries and deliver more accurate, diverse content and services, thereby meeting user needs more effectively. This mode entails traditional search engines leveraging large language models to process, synthesize, and summarize retrieved information to enhance the user search experience. Furthermore, search engines can utilize AI tools for targeted advertising, ensuring ads are precisely delivered to users who need the product, thereby improving click-through rates.

The second mode involves stakeholders within search platforms using AI to conduct business operations. AI tools like ChatGPT have amassed a substantial user base in recent years, significantly impacting search engines and SEO. More businesses are adopting AI tools to handle search engine-related tasks. For instance, tools like SEMrush have integrated AI for keyword research, competitor analysis, and other SEO tasks. The convergence of SEO and AI is transforming the search engine optimization landscape, presenting new opportunities and challenges. By understanding and adapting to these developments, stakeholders can harness AI to optimize their SEO strategies and maintain a competitive edge.

AI also aids SEO firms in reducing costs and increasing efficiency. In SEO processes, AI can enhance various aspects such as keyword research, content creation, technical optimization, and link building. For example, keyword research remains a cornerstone of search engine optimization (SEO), enabling businesses to understand the intent behind user queries and create more relevant and engaging content. AI significantly enhances this process by efficiently identifying opportunities such as long-tail, related, and semantic keywords that might otherwise be overlooked. Similarly, content creation is another critical aspect of SEO that AI can transform. AI accelerates content production by generating creative ideas, titles, outlines, paragraphs, or entire articles based on a business’s keywords or topics and ensures it aligns with SEO requirements. Furthermore, AI assists in optimizing content by analyzing its performance, identifying gaps, and offering recommendations to improve alignment with search engine algorithms and user expectations. This optimization ultimately boosts the ranking and visibility of content in search results. In summary, by analyzing large datasets, generating insights, and providing actionable recommendations, AI enables companies to save time, boost productivity, and achieve better outcomes. Given the aforementioned developments, we expand on existing models to investigate the impact of AI advancements on search engines.

First, the effectiveness of SEs is expected to be significantly influenced by AI technology. In this expanded model, we assume that AI has been fully integrated into search engines. The world’s leading search engines have already announced or are implementing measures aligned with these advancements. For instance, Google’s AI overview uses generative AI to collect information from various sources across the web and create concise answers. Similarly, subsequent to the integration of Bing and ChatGPT, the new Bing was launched; following the integration of Baidu with ERNIE Bot, an AI intelligent question-answering service was introduced. With AI, search engines can leverage large models’ information processing capabilities to collect and analyze data from websites, ultimately producing concise answers that are easy for users to read and understand, as illustrated in Figure C4.

Despite the introduction of AI, not all search results in mobile search engines currently feature AI-generated brief answers. Taking Baidu as an example, in 2024, Baidu’s founder, chairman, and CEO, Robin $\mathrm { L i } ,$ stated in the first-quarter earnings call that currently, 11% of the search results on Baidu Search are generated by AI. This indicates that a significant portion of searches still does not include AI-generated concise answers, even though this proportion has recently increased. Consequently, we hypothesize that when users employ search engines for information retrieval, there is $\rho _ { 1 }$ likelihood that AI-generated summaries will appear as concise answers. These summaries not only save users’time by directly addressing their queries but also have the potential to deliver more personalized and accurate results, tailored to user feedback and context, thus responding to both explicit and implicit queries. This can significantly enhance the overall user experience. However, it is essential to acknowledge that, due to the “hallucination” problem, AI-generated responses may occasionally be factually incorrect. For instance, as illustrated in Figure C5, Google’s AI overview once erroneously suggested that users should eat stones. We hypothesize that the probability of an AI-generated answer being correct is $\rho _ { 2 }$ . Therefore, the expected utility for a user retrieving the target keyword from the search engine can be expressed as:

$$
\rho_ {1} v _ {1} \alpha q _ {e} + (1 - \rho_ {1}) [ (1 - \rho_ {2}) v _ {2} + \rho_ {2} v _ {1} \omega ] \alpha q _ {e}
$$

The first term represents the scenario where search results do not contain AI-generated content, thus aligning with traditional search results. In this case, the expected utility is the product of probability $\rho _ { 1 }$ and utility $v _ { 1 } \alpha q _ { e }$ . The second term describes the situation where AI-generated content is included in the search results. If the AI-generated content lacks a comprehensive understanding of the business context, fails to align with the user’s needs, or even contains errors, advertisers can expect a utility of $v _ { 2 } ( v _ { 2 } < v _ { 1 } )$ . At this point, even when the content generated by AI does not fully align with user needs, the advertisers’ webpages still gain increased exposure and traffic, regardless of whether users click on them. This can also provide certain value to advertisers. Therefore, when viewers encounter erroneous search results, the utility they derive is the product of the probability $1 - \rho _ { _ 1 }$ and the utility $v _ { 2 } .$ . For generality, we standardize the utility $v _ { 2 }$ to 0, a method commonly adopted by various scholars (Chen et al., 2024; Shi & Hu, 2024).

![](/api/attachments/EM976JN4/fulltext/images/8e35a254bba8e7bab607a8d4f352ddecb0fed8e5c45e449a5abac256f67bc235.jpg)  
Figure C4. Overview of Responses from Google AI

When the content generated by AI is incorrect, the searchers’ choice—whether to conduct a new search or to browse traditional search results—does not affect our main conclusions. This is because such scenarios ultimately revert to either our extended model or the baseline model. When the AI-generated content is correct, it helps advertisers achieve higher value, denoted as $v _ { 1 } \omega ( \omega 2 1 )$ . Here, we assume that advertisers attribute a higher expected value to the content of AI overviews. Under $\omega = 1$ , the expected value of AI overviews’ content is no different from that of traditional search results. Therefore, under different strategies, the utility that advertisers can derive is as follows:

$$
u _ {1} = r _ {s} (1 + \rho_ {3}) \alpha q _ {e} \{[ \rho_ {1} v _ {1} + \rho_ {2} (1 - \rho_ {1}) \omega v _ {1} ] - p \}\tag{A7}
$$

$$
u _ {2} = r _ {o} \alpha q _ {e} [ \rho_ {1} v _ {1} + \rho_ {2} (1 - \rho_ {1}) \omega v _ {1} ] - \delta \lambda q _ {r}\tag{A8}
$$

$$
u _ {3} = \gamma r _ {o} [ \rho_ {1} v _ {1} + \rho_ {2} (1 - \rho_ {1}) \omega v _ {1} ] \alpha q _ {e} - \delta \lambda q _ {r} + r _ {s} (1 + \rho_ {3}) [ \rho_ {1} v _ {1} + \rho_ {2} (1 - \rho_ {1}) \omega v _ {1} - p ] \alpha q _ {e}\tag{A9}
$$

Here, $r _ { s } ( 1 + \rho _ { _ 3 } )$ indicates that the introduction of AI enables the search engine to leverage AI’s precision in ad placement. This allows PSM ads to better match user needs, resulting in a higher click-through rate. ?? ( 1) represents the cost incurred by advertisers when choosing an SEO strategy. The introduction of AI reduces SEO-related costs, which in turn lowers the fees charged by SEO firms. In a perfectly competitive market, if SEO firms adopt AI technology without reducing their service fees, they may obtain additional profits, which would attract new entrants to the market and subsequently drive down their profits. Therefore, we assume that after adopting AI technology, the fees charged by SEO firms for their services to advertisers will also decrease accordingly. Furthermore, we assume that AI-generated content may also include advertisements for two primary reasons.

![](/api/attachments/EM976JN4/fulltext/images/c8a6ab301e75a561c1fbc97352c3d413e77f24077a9d0e127cd2d1ffe22692d5.jpg)  
Figure C5. Incorrect Content in Google’s AI Overview Response

First, some AI-generated content in search engines already includes advertisements. As shown in Figure C6, New Bing’s AI-generated responses reference advertisements and provide links to advertisers. Second, advertising revenue is the most significant income source for search engines. For instance, in 2023, Google’s advertising revenue exceeded \$230 billion, accounting for 77.4% of its total revenue. Search engines have no incentive to forgo this revenue stream. Moreover, Google’s Vice President of Ads, Vidhya Srinivasan, publicly announced that Google would soon begin testing search and shopping ads in the AI overview for US users. Although no specific timeline has been provided, it is anticipated that ads will be launched soon.

![](/api/attachments/EM976JN4/fulltext/images/a186d4cc6dfff0bffc6853cb82ea8e4da88666bdfdcfb1f0fd80e4d6002c2ba5.jpg)  
Figure C6. Advertisement Content in New Bing’s Response

p

By comparing the utility of advertisers under different strategies, we can assess the search engine’s market share, as shown in Figure C7. Two scenarios emerge: the first is when the utility increase provided by AI to searchers is minimal or when the probability of AI errors is high, as illustrated in Figure C7a. To enhance the clarity of the illustration, we depict only the case of $r _ { o } - ( 1 + \rho _ { _ 3 } ) { > } 0$ here, as $r _ { o } - ( 1 + \rho _ { _ 3 } ) { < } 0$ does not affect the survival space of SEO, thereby leaving the main content in Figure C7 unchanged. The second scenario occurs when AI significantly improves utility for searchers, denoted by $\rho _ { 2 } \omega - \rho _ { 1 } ( 1 - \rho _ { 2 } \omega ) { \circ } 1$ , as shown in Figure C7b.

![](/api/attachments/EM976JN4/fulltext/images/d0e94a1227bc3ffc1e946b4c3455f77d0331760cdfb383a529b9cce81d186fad.jpg)  
(a) K = ρ2ω + ρ1(1 − ρ2ω)<1

![](/api/attachments/EM976JN4/fulltext/images/a4f0ba08994d218cb4c87f3cecd0746b0c2d524d1fd20082d70039ec89b49716.jpg)

![](/api/attachments/EM976JN4/fulltext/images/b7dfc4deff117939359380f6d75993a23711d9c0f28f6ef72a3c910ee13e037d.jpg)  
(b. 2) K = ρ2ω + ρ1(1 − ρ2ω)]>1  
Figure C7. Market Share of the SE Under the Influence of AI

Thus, we derive Lemma C3, which demonstrates the impact of AI technology on the search engine market share.

Lemma C3: When $\rho _ { 2 } < 1 / \omega$ , the introduction of AI may constrain the survival of SEO firms, and in the presence of SEO competition, the SE will increase the price of PSM. Conversely, when $\rho _ { 2 } > 1 / \omega$ , the AI technology introduced by the SE will facilitate the expansion of SEO firms’ survival space, and in the presence of SEO competition, the SE will choose to reduce the price of PSM.

To better understand the changes in the survival space of SEO firms following the introduction of AI, we conducted a numerical analysis comparing the survival space of SEO firms in both the base model and the model with AI, as illustrated in Figure C8. By integrating Lemma C3 with Figure C8, we derived several key conclusions. First, the value of $\dot { \rho } _ { 1 }$ does not significantly affect the SEO firm’s survival environment. A possible explanation for this is that advertisements also exist within the AI overview, meaning that AI’s introduction does not eliminate the competition between SEO and PSM, but rather alters the target of competition in traditional search results. Consequently, regardless of whether $\rho _ { 1 }$ is high or low, the survival conditions of SEO firms remain relatively stable.

![](/api/attachments/EM976JN4/fulltext/images/0483c490b88db73a85f1cfc0c2ea063357d8ccd7472041b986f5938d3f8004b1.jpg)  
(a)

![](/api/attachments/EM976JN4/fulltext/images/92908e22ca022caf999c379b9e74d59ddbedc83cab2f2d912ee93b4f779ade37.jpg)  
(b)  
Figure C8. Comparison of SEO Firm Survival Space Under AI Influence

Moreover, when $\rho _ { 2 }$ is small, introducing AI in search engines could increase survival pressure on SEO firms, hindering their development. However, when the introduction of AI leads to a significant increase in expected value for advertisers, or when $\rho _ { 2 }$ is large, AI may help alleviate the survival pressure on SEO firms. In other words, if the AI overview does not significantly increase the expected value for advertisers, or if the accuracy of AI-generated answers is low, SEO firms are more likely to be pushed out of the market by the search engine, as depicted in Figure C8. Interestingly, in such scenarios, the search engine may choose to raise the price of PSM in response to SEO competition. A possible explanation for this is that while the AI overview captures part of the traditional search market share, when the likelihood of inaccurate results is high, the additional revenue generated by an AI overview for SEO firms fails to compensate for the revenue lost in traditional search, leading to a reduction in SEO earnings. This, in turn, diminishes the negative impact of cost dilution on the search engine, ultimately reducing the survival space for SEO firms. For the search engine, the introduction of an AI overview with a lower value of $\rho _ { 2 }$ can help mitigate the cost dilution effect to some extent, thereby enhancing the competitiveness of PSM services. Consequently, this provides the search engine with the opportunity to increase prices, even in the presence of SEO competition.

Conversely, when the accuracy of AI-generated answers is high, the AI overview can generate sufficient revenue for SEO firms, thereby exacerbating the cost dilution effect and further expanding their survival space. At this point, SEO firms will capture some of the market share from PSM. As a result, the search engine may lower the price of PSM to maintain its revenue. Lemma C3 indicates that the introduction of AI and the provision of AI overviews by search engines influence the cost dilution effect, which, in turn, can impact the competition dynamics between search engines and SEO firms.

Similar to the base model, we can determine the optimal decisions and profits for the search engine under different scenarios. By comparing the optimal profit of the search engine, we derive Theorem C3, as follows:

Theorem C3: The introduction of AI does not fundamentally alter the survival conditions of SEO firms, regardless of whether SEO firms use AI tools. In the search engine marketing market, eliminating SEO firms is not a wise strategy for search engines.

Theorem C3 reveals that the introduction of AI, whether in the form of an AI overview used by search engines or AI tools used by SEO firms, does not significantly alter the conclusions of the base model. On the one hand, in the search engine marketing market, the search engine is the dominant player. Therefore, even if SEO firms use AI tools to reduce costs, this only strengthens their competitive advantage within existing conditions. However, as the market leader, the search engine can adjust its decisions to limit the competitive advantage gained by SEO firms through AI tools. Consequently, changes in market share suggest that the use of AI tools by SEO firms does not significantly impact the search engine’s market share. Furthermore, even if the search engine introduces an AI overview, eliminating SEO firms may not be a wise decision for the search engine. As shown in Figure C8, while the introduction of an AI overview affects the search engine’s market share and pricing decisions, it does not fundamentally eliminate the cost dilution effect and may even exacerbate it.

## C4. Independence of Effectiveness and Robustness

In the base model presented in this paper, we adopt the assumption of “independence between effectiveness and robustness” to clearly illustrate the competitive relationship between search engines and SEO firms, as well as to analyze the optima decisions of search engines in various market scenarios. This assumption is primarily employed to simplify the model and more accurately reflect the practical aspects of search engine algorithm updates.

Effectiveness measures a search engine’s ability to deliver relevant search results to users, while robustness evaluates its capacity to resist manipulation by SEO. In the base model, we assume that effectiveness and robustness are independent, primarily for the following reasons:

First, fundamentally, these two metrics target different objectives: effectiveness focuses on enhancing the user experience, whereas robustness aims to mitigate SEO interference. Furthermore, search engines typically employ distinct technical approaches and different strategies and resource allocations to optimize effectiveness and robustness independently, providing a theoretical basis for modeling them as separate variables. For instance, enhancing effectiveness primarily involves optimizing retrieval algorithms and incorporating machine learning models to improve the relevance of search results, thereby increasing user satisfaction. On the other hand, enhancing robustness relies more on updating anti-spam algorithms and detecting SEO manipulation behaviors. These measures are relatively independent in practice and generally do not directly and significantly affect the relevance of search results. This practical observation supports the validity of modeling effectiveness and robustness as independent variables.

Moreover, assuming interdependence between effectiveness and robustness would significantly increase the model’s complexity. Although such models could still yield closed-form solutions and support equilibrium analysis, our aim is to develop a clear and comprehensible theoretical framework that elucidates the optimal decision-making patterns of search engines in various market contexts. Treating effectiveness and robustness as independent parameters simplifies the model, allows for a sharper focus on core issues, and facilitates a more precise depiction of the dynamic relationship between search engines and SEO firms. More importantly, this assumption does not significantly affect the accuracy or robustness of the primary conclusions. Making such assumptions to streamline models and enhance interpretability is common in mathematical modeling research, as demonstrated by studies that adopt similar modeling (Gu & Tayi, 2023; Kim & Balachander, 2023).

Although effectiveness and robustness are conceptually independent, and search engines typically optimize them through distinct strategies, indirect interactions between the two may occur. For example, when a search engine updates its algorithms to improve robustness, this may indirectly influence the effectiveness of search results. Similarly, adjustments aimed at optimizing effectiveness could have an indirect impact on robustness. To further explore this potential interaction, we extend the base model. The specifics are as follows:

When a correlation exists between the robustness and effectiveness of search engine algorithms, the utility gained by advertisers from choosing the PSM strategy is given by:

$$
u _ {1} = r _ {s} \alpha (q _ {e} + \theta_ {1} ^ {c o} q _ {r}) (v _ {1} - p)\tag{A10}
$$

Where $q _ { e } + \theta _ { 1 } ^ { e o } q _ { r }$ can be regarded as the overall effectiveness of the search engine algorithm, which is influenced not only by the measures taken by the search engine to enhance algorithmic effectiveness but also by its efforts to strengthen algorithmic robustness. $\ a ( q _ { e } + \theta _ { 1 } ^ { c o } q _ { r } )$ represents the number of searchers reaching the search engine within a specific period. In this context, user volume is influenced not only by updates to the effectiveness of the search engine algorithm but also by updates to its robustness. Notably, the impact of improvements in robustness on user volume is smaller than that of improvements in effectiveness, $\theta _ { 1 } ^ { c o } < \bar { 1 }$ . The utility gained by advertisers when selecting SEO is expressed as:

$$
u _ {2} = r _ {o} v _ {1} \alpha (q _ {e} + \theta_ {1} ^ {c o} q _ {r}) - \lambda (q _ {r} + \theta_ {2} ^ {c o} q _ {e})\tag{A11}
$$

Here, $\lambda ( q _ { r } + \theta _ { 2 } ^ { c o } q _ { e } )$ represents that as the search engine improves effectiveness, the difficulty of SEO firms in providing SEO services increases, resulting in higher costs. Similarly, the utility gained by advertisers when selecting the SEO+PSM service is:

$$
u _ {3} = \gamma r _ {o} v _ {1} \alpha (q _ {e} + \theta_ {1} ^ {c o} q _ {r}) - \lambda (q _ {r} + \theta_ {2} ^ {c o} q _ {e}) + r _ {s} \alpha (q _ {e} + \theta_ {1} ^ {c o} q _ {r}) (v _ {1} - p)\tag{A12}
$$

By comparing the utilities of advertisers under different strategies, the market share of search engines can be determined, as illustrated in Figure C9.

According to Figure C9, Lemma C4 can be derived. Lemma C4 describes the changes in the market share of search engines when a correlation exists between effectiveness and robustness, compared to the base model.

Lemma C4: When $0 < q _ { e } < \sqrt { \theta _ { 1 } ^ { c o } / \theta _ { 2 } ^ { c o } } q _ { r }$ , SEO firms are more likely to survive in the market compared to the base model. In this case, if competition exists among SEO firms, search engines (SE) will choose to lower the price of PSM. Conversely, when $\sqrt { \theta _ { 1 } ^ { c o } / \theta _ { 2 } ^ { c o } } q _ { r } { < } q _ { e }$ , the survival difficulty of SEO firms increases; however, if competition exists among SEO firms, the SE will choose to raise the price of PSM.

Theorem C4: When effectiveness and robustness are not entirely independent, completely eliminating SEO firms from the market is not the optimal strategy for the SE.

Lemmas C6 and Theorem C4 indicate that when a correlation exists between effectiveness and robustness, SEO firms’ survival conditions are influenced to some extent, but their fundamental ability to survive in the market remains unchanged. Specifically, when efforts by search engines to enhance the robustness of algorithms significantly impact effectiveness, or when $\theta _ { 2 } ^ { \bar { c } o }$ is small, SEO firms are more likely to survive, as shown in Figure C9 and Figure C10. This phenomenon may result from the positive spillover effect that measures taken by search engines to improve algorithm robustness can have on algorithm effectiveness, thereby mitigating the negative impact of $q _ { r }$ on SEO firms’ survival. Furthermore, this spillover effect can promote market expansion, enhance the cost-dilution effect, and improve SEO firms’ market position. Consequently, SEO firms have greater room for survival.

On the other hand, to counter the presence of SEO firms and maintain the competitiveness of PSM, the SE will choose to lower the price of PSM. This strategy reflects the trade-off that the SE must make in a competitive market to balance market structure and optimize overall profits.

The correlation between effectiveness and robustness does not fundamentally alter the main conclusions of the model. Even when such a correlation exists, its primary impact is limited to the size of SEO firms’ survival space, rather than completely excluding SEO firms from the market. This extended analysis further confirms the robustness of the base model.

p  
![](/api/attachments/EM976JN4/fulltext/images/75378f7628d96de9fda626f374b1b2f3333da13701ef824735e7e23ee6354ee3.jpg)  
(a) qr + qeθ2° < qe+θ1°qr

p  
![](/api/attachments/EM976JN4/fulltext/images/ce7cd1914b5f8223b2abecd972e3c77d2222a0ca194200d5816dc55a199497f4.jpg)  
(b) qr + qeθ2o > qe + qrθ1°  
Figure C9. The Market Share of the Search Engine under the Correlation Between Effectiveness and Robustness

![](/api/attachments/EM976JN4/fulltext/images/69f84660e96efad3042233f0f176fd8cb1772a4b28e193670dc3e175b4b7acb7.jpg)  
(a)

![](/api/attachments/EM976JN4/fulltext/images/2b2bcefbdcae0ca98cba990c86d49e80bad2b8fe3bdd5a437c8e4738f4ddc6e6.jpg)  
(b)  
Figure C10. Survival Region for SEO Survival Under Non-Independence of Robustness and Effectiveness

Search engines should recognize the potential interactions between effectiveness and robustness, especially when the improvement in robustness generates spillover effects on effectiveness. This synergistic effect not only enhances user experience but also expands market size, thereby increasing overall profits while maintaining moderate competition among SEO firms. Therefore, search engines should adopt a comprehensive optimization strategy to fully exploit this spillover effect and achieve a win-win outcome.

This extension demonstrates that the interaction between robustness and effectiveness indeed affects the survival of SEO firms in the search engine marketing market, influencing the size of their survival space. However, it also suggests that even when effectiveness and robustness are not completely independent, the model’s primary conclusions remain qualitatively unchanged.

## C5. Guiding SEO with PSM Data

Indeed, as the search engine market continues to evolve, advertisers’ strategies have undergone significant transformation. Initially, SEO and PSM were considered two independent, mutually exclusive approaches. However, some companies have integrated the two into a complementary, unified strategy. For example, by leveraging data analysis tools from paid search, advertisers can track key metrics such as click-through rates, conversion rates, and cost-effectiveness, applying these insights to enhance their SEO efforts. Through data-driven reports, advertisers can optimize content creation and adjust their strategies, thereby improving the overall performance of their websites.

This shift reflects the increasingly complex competitive pressures faced by businesses within the search engine ecosystem. SEO enhances organic search rankings through high-quality content optimization and backlinks, while PSM generates paid search traffic via targeted advertising. The integration of both strategies not only increases brand visibility but also boosts return on investment (ROI) through synergies. This approach may significantly impact the relationship between SEO and PSM. In response, we extended the base model to incorporate scenarios in which advertisers use PSM data to guide SEO practices and examined the effect of this strategy on SEO click-through rates.

Building on this, we have expanded the base model to focus on how PSM-generated data can inform SEO and its impact on advertisers’SEO click-through rates. The utility function when an advertiser chooses PSM or SEO individually remains unchanged, as shown in Equations (A13) and (A14):

$$
u _ {1} = \alpha q _ {e} r _ {s} (v - p)\tag{A13}
$$

$$
u _ {2} = \alpha q _ {e} r _ {o} v - \beta q _ {r}\tag{A14}
$$

When an advertiser opts to use PSM-generated data to guide SEO optimization, the resulting utility is expressed as follows:

$$
u _ {3} = \gamma_ {1} \alpha q _ {e} r _ {o} p (1 + \gamma_ {2}) v - (1 + \gamma_ {3}) \beta q _ {r} + \alpha q _ {e} r _ {s} (v - p)\tag{A15}
$$

Where $\boldsymbol { \gamma } _ { 2 }$ represents the effect of PSM-generated data on guiding SEO, helping the advertiser improve click-through rates, and $\boldsymbol { \gamma } _ { 3 }$ indicates the additional costs for SEO firms to align their strategies with PSM data. In this case, SEO firms incur higher costs, such as data analysis and resource allocation to tailor SEO efforts to the advertiser’s specifications. By comparing the utilities under different strategies, the market share of search engines can be determined, as illustrated in Figure C11.

![](/api/attachments/EM976JN4/fulltext/images/0f062b6f824981587df9adca413042f74d997be5b37cc56f36b0df650c81d9e9.jpg)  
Figure C11. Market Share of the SE When Guiding SEO with PSM Data

Theorem C5: The use of PSM data to guide SEO does not qualitatively impact the survival of SEO firms, nor does it significantly alter the conclusions of the base model.

Theorem C5 indicates that even with the use of PSM data to guide SEO, there is no significant impact on the relationship between SEO firms and the SE. On the one hand, using PSM data to guide SEO does not eliminate the competitive dynamics between SEO and PSM, as not all advertisers adopt the SEO+PSM strategy. As a result, SEO continues to capture a portion of the market that would otherwise be allocated to PSM. In other words, although the competitive relationship between SEO and PSM has evolved from initial separation to greater integration and complementarity, it has not fully removed their competition. On the other hand, despite the persistence of competition between SEO and PSM, completely eliminating SEO firms from the market would not be a prudent decision for the SE. As illustrated in Figure C12, while using PSM data to guide SEO can, to some extent, increase the survival space for SEO firms, if the robustness of the search algorithm is high and the effect of PSM data on guiding SEO is minimal, the use of PSM data will not significantly improve SEO firms’ survival conditions. Only when PSM data is highly effective in guiding SEO will the integration of both strategies yield the desired positive outcomes.

![](/api/attachments/EM976JN4/fulltext/images/146f2142c8a26ca9c01d831992fbfa69fef2e5e3640c9d637c976c994d586c18.jpg)  
(a)

![](/api/attachments/EM976JN4/fulltext/images/799cb342702477e9a86f4b6b5951281675785cb458ca23464dc415fee41e3e19.jpg)  
(b)  
Figure C12. Comparison of SEO Firms’ Survival Space After Using PSM Data to Guide SEO

The extensions in C1, C2, C3 and C4 further develop the existing model by considering the impact of market environment factors, such as technological advancements, on the dynamic relationship between SEO and PSM. These extended conclusions demonstrate that our model adapts well to current market changes. Moreover, after considering new market conditions, the conclusions remain robust. Therefore, we argue that these extensions enable the paper to align with the current market environment more effectively, preserving the model’s applicability while ensuring the timeliness and robustness of the research findings.

## C6. Competition Among SEs

Our base model assumes that there is only one SE in the SEM market, meaning that the number of searchers on the SE is solely determined by the effectiveness of its algorithm, which is widely adopted in related studies to ensure analytical tractability and interpretability. In this section, we relax this assumption to improve the robustness of our conclusions.

Specifically, this section considers a market scenario where two SEs, namely $s e _ { 1 }$ and $s e _ { 2 }$ , compete with each other. Without loss of generality, we will analyze the optimal decisions and profits of $s e _ { 1 }$ in the latter part of this article. In this competitive market, apart from its effectiveness, the demand for $s e _ { 1 } \mathrm { ~ } \mathbf { \dot { s } }$ searchers will also be influenced by the effectiveness of its competitor. Like many previous researchers (Ha et al., 2011; Jiang et al., 2023; Kim & Balachander, 2023), we adopt a widely-used linear demand function to investigate market demand, which incorporates the difference between an SE’s effectiveness and that of its competitor as a determinant. The searchers’ demand is formulated as follows:

$$
D ^ {c s} = \alpha q _ {e 1} + \beta (q _ {e 1} - q _ {e 2})
$$

Where the superscript cs indicates the existence of competition between SEs, $q _ { e 1 }$ and $q _ { e 2 }$ represent the effectiveness of search engines SEs $s e _ { 1 }$ and $s e _ { 2 }$ respectively. Specifically, when the effectiveness of competitor $q _ { e 2 }$ exceeds that of $s e _ { 1 }$ $s e _ { 1 }$ ’s searcher market demand decreases, and vice versa. Additionally, $\beta \mathrm { : }$ measures the sensitivity of $s e _ { 1 }$ ’s searcher market demand to the effectiveness of its competitor.

![](/api/attachments/EM976JN4/fulltext/images/461bd64a7bff17cf5b1ec5480b0493791cdcd87248cc8d488e3ab374ecc73ff3.jpg)  
Figure C13. Market Share of Search Engine

Therefore, the outcomes for advertisers under the three strategies are:

$$
\begin{array}{c} {u _ {1} = [ \alpha q _ {e 1} + \beta (q _ {e 1} - q _ {e 2}) ] r _ {s} (v - p)} \\ {u _ {2} = [ \alpha q _ {e 1} + \beta (q _ {e 1} - q _ {e 2}) ] r _ {o} v - \beta q _ {r}} \\ {u _ {2} = \gamma r _ {o} v [ \alpha q _ {e 1} + \beta (q _ {e 1} - q _ {e 2}) ] - \beta q _ {r} + [ \alpha q _ {e 1} + \beta (q _ {e 1} - q _ {e 2}) ] r _ {s} (v - p)} \end{array}
$$

The region of an advertiser’s strategic choices when SEs compete can be derived using the above equation, as shown in Figure C13.

Lemma C5: When search engine ${ \mathsf { s e } } _ { 1 }$ has a competitive advantage, SEO companies in ${ \mathsf { s e } } _ { 1 }$ are more likely to survive, while the survival space of SEO companies in $\mathsf { s e } _ { 1 }$ is smaller when $\mathsf { s e } _ { 1 }$ is at a disadvantage in competition with ${ \mathsf { s e } } _ { 2 }$

Lemma C5 demonstrates that the competition among SEs directly and indirectly impacts competitors, SEO firms, and advertisers. More specifically, when SEs hold a dominant position in the market, they attract more searchers through brand awareness and brand loyalty, strengthening their influence on advertisers’ choice of SEO strategy. Moreover, economies of scale give SEs a competitive edge in price competition, leading to increased market share and a stronger effect of cost dilution. In such a scenario, SEO companies can expand their survival space by capitalizing on search engine traffic and providing superior services.

However, when SEs are at a disadvantage, the benefits of advertisers’ SEO strategy decrease, reducing the survival space of SEO firms. Hence, SEs must constantly enhance competitiveness through innovation, service optimization, and improved search result quality to ensure survival and growth. At the same time, competitors must adopt effective strategies and flexible response mechanisms to maintain their advantage and market share. For SEO companies and advertisers, it is essential to understand the market position and competitive landscape in-depth, adjusting strategies promptly for better market outcomes and commercial benefits.

In summary, competition among SEs is crucial for all market participants. Therefore, all entities must constantly monitor and analyze market conditions, respond flexibly, and adjust strategies to survive and thrive in a fiercely competitive environment. $\mathrm { S o } ,$ how should SEs determine their optimal decision when facing competition? Next, we present the optimal decisions for the SE $s e _ { 1 }$ under various scenarios. Without losing generality, in the subsequent analysis of this section, we assume that $s e _ { 1 }$ has a competitive advantage, which does not significantly affect the main conclusions of this section.

Proposition C1: The optimal decision of ${ \tt S e } _ { 1 }$ can be summarized as follows:

(1) In the absence of SEO in the market, $\begin{array} { r } { \mathrm { I f } \frac { V r _ { o } [ V r _ { s } ( \alpha + \beta ) ^ { 2 } - 2 \beta \xi q _ { e 2 } ] } { 2 \lambda \xi } < q _ { r } } \end{array}$ and $\begin{array} { r } { q _ { e 2 } < \frac { V r _ { s } ( \alpha + \beta ) ^ { 2 } } { 2 \beta \xi } . } \end{array}$ , then $\begin{array} { r } { q _ { e 1 } ^ { s e * } = \frac { V ( \alpha + \beta ) r _ { s } } { 2 \xi } , } \end{array}$ $\begin{array} { r } { \pi _ { I } ^ { S e * } = \frac { V r _ { s } [ V ( \alpha + \beta ) ^ { 2 } r _ { s } - 4 \beta \xi q _ { e 2 } ] } { 8 \xi } ; \mathrm { I f } \ q _ { e 2 } < \frac { V r _ { s } ( \alpha + \beta ) ^ { 2 } } { 2 \beta \xi } \mathrm { a n d } \ 0 < q _ { r } < \frac { V r _ { o } [ V r _ { s } ( \alpha + \beta ) ^ { 2 } - 2 \beta \xi q _ { e 2 } ] } { 2 \lambda \xi } , } \end{array}$ then $\begin{array} { r } { q _ { e 1 } ^ { s e * } = \frac { \lambda q _ { r } + V \beta q _ { e 2 } r _ { o } } { V \alpha r _ { o } + V \beta r _ { o } } , } \end{array}$ $\begin{array} { r } { \pi _ { I } ^ { s e * } = \frac { V \lambda q _ { r } r _ { o } [ V ( \alpha + \beta ) ^ { 2 } r _ { s } - 2 \beta \xi q _ { e 2 } ] - \lambda ^ { 2 } \xi q _ { r } ^ { 2 } - V ^ { 2 } \beta ^ { 2 } \xi q _ { e 2 } ^ { 2 } r _ { o } ^ { 2 } } { 2 V ^ { 2 } ( \alpha + \beta ) ^ { 2 } r _ { o } ^ { 2 } } ; } \end{array}$ Otherwise, $\mathsf { s e } _ { 1 }$ will choose to exit the market, and therefore <sub>I</sub><sup>se∗</sup> = 0.

(2) When SEO exists in the market but not SEO+PSM, the optimal robustness is $\begin{array} { r } { q _ { e 1 } ^ { s e * } = \frac { \lambda q _ { r } + V \beta q _ { e 2 } r _ { o } } { V \alpha r _ { o } + V \beta r _ { o } } . } \end{array}$ and the profit

$$
\mathrm {of s e _ {1} is \pi_ {II} ^ {se*} = \frac {V\lambda q_ {r} r_ {o} [3V(\alpha+ \beta) ^ {2} r_ {s} - 2\beta\xi q_ {e2} ]- \lambda^ {2} \xi q_ {r} ^ {2} - V^ {2} \beta^ {2} \xi q_ {e2} ^ {2} r_ {o} ^ {2}}{2 V^ {2} (\alpha+ \beta) ^ {2} r_ {o} ^ {2}} .}
$$

$$
\begin{array}{l} \text {(3) When SEO + PSM exists in the market, if} \frac {V \gamma r _ {o} \left\{V (\alpha + \beta) ^ {2} [ r _ {s} - (1 - \gamma) r _ {o} ] - 2 \beta \xi q _ {e 2} \right\}}{2 \lambda \xi} <   q _ {r}, \text {then} q _ {e 1} ^ {s e *} = \frac {\lambda q _ {r} + V \beta \gamma q _ {e 2} r _ {o}}{V \alpha \gamma r _ {o} + V \beta \gamma r _ {o}}, \pi_ {I I I} ^ {s e *} = \\ \frac {V \gamma \lambda q _ {r} r _ {o} \left\{V (\alpha + \beta) ^ {2} [ (3 + 2 \gamma) r _ {s} - 3 (1 - \gamma) r _ {o} ] - 2 \beta \xi q _ {e 2} \right\} - \lambda^ {2} \xi q _ {r} ^ {2} - V ^ {2} \beta^ {2} \gamma^ {2} \xi q _ {e 2} ^ {2} r _ {o} ^ {2}}{2 V ^ {2} (\alpha + \beta) ^ {2} \gamma^ {2} r _ {o} ^ {2}}; \text {otherwise, the optimal decision for the} s e _ {1} \text {is} \\ q _ {e 1} ^ {s e *} = \frac {V (\alpha + \beta) (r _ {s} - r _ {o} + \gamma r _ {o})}{2 \xi}, \qquad \text {and} \qquad \text {the maximum profit is} \qquad \pi_ {I I I} ^ {s e *} = \\ \frac {8 \lambda \xi q _ {r} [ (1 + \gamma) r _ {s} - (1 - \gamma) r _ {o} ] + V \gamma r _ {o} [ r _ {s} - (1 - \gamma) r _ {o} ] \left\{V (\alpha + \beta) ^ {2} [ r _ {s} - (1 - \gamma) r _ {o} ] - 4 \beta \xi q _ {e 2} \right\}}{8 \gamma \xi r _ {o}}. \end{array}
$$

Based on Proposition C1, without SEO in the market, the auction pricing of PSM services by an SE is influenced by its robustness and the effectiveness of its competitors. Specifically, when an SE possesses a high level of robustness while its competitors exhibit lower effectiveness, it can achieve maximum profits. This is because the SE’s robustness reduces cost dilution effects, giving it an advantage in internal and external competition. However, cost dilution effects increase as SE robustness decreases, leading to heightened internal competition. Without changes, the optimal decision for the SE is to lower its effectiveness to alleviate the cost dilution effects, even though this may intensify the external competition. When a competitor’s effectiveness surpasses a certain threshold, the optimal strategy for the SE is to exit the market to avoid costly investments. Consequently, it is imperative for SEs to appropriately adjust their effectiveness and robustness to maintain a competitive advantage in both internal and external competition. In highly competitive markets, careful consideration of market trends is crucial, and lowering effectiveness may sometimes be warranted to gain an edge.

Additionally, when SEO or SEO+PSM exists, proposition 3’s conclusions still hold, indicating that the competition among SEs does not significantly affect the baseline model’s main conclusions. Then, to what extent does SE competition impact SEO companies’ survival?

Theorem C6: When there is competition among search engines, eliminating SEO does not necessarily lead to the optimality of search engines. In other words, even with competition, it is not possible to eliminate existing SEO companies.

Theorem C6 presents an important conclusion, verifying the robustness of this paper’s argument. Specifically, SEs will not choose to eliminate SEO companies, even in the fierce external competitive environment. In practice, this means the SE $s e _ { 1 }$ must balance internal and external competition to maximize its interests.

Competition among SEs is an external pressure on $\mathrm { S E } s e _ { 1 }$ , requiring it to possess strong competitive abilities, constantly innovate, and maintain market share. However, competition between SEs and SEO companies is an internal issue, and the existence of SEO firms also poses a certain threat to the market share and profitability of the SE $s e _ { 1 }$ . External competition affects the survival of SEO companies. SEs with a competitive advantage in external competition will attract more SEO firms and face fiercer internal competition. Therefore, SE $s e _ { 1 }$ needs to balance internal and external competition to maximize its interests. This requires the SE $s e _ { 1 }$ to recognize the importance of SEO firms and coexist with them through reasonable competition strategies. In summary, the SE $s e _ { 1 }$ must balance internal and external competition and implement effective strategies to maintain its competitive position and profitability. Additionally, it is crucial to recognize the significance of SEO companies and coexist with them through reasonable competition strategies while enhancing user experience.

This section discusses the effects of SE competition on the earlier conclusions. However, in reality, competition among advertisers is equally fierce. As such, we will examine the impact of advertiser competition on SEs, SEO companies, and advertisers themselves.

## C7. Competition Among Advertisers

In the base model, we assume that the search engine marketing market consists of only one advertiser, meaning that the advertiser’s bid solely determines the final transaction price in the PSM auction. However, in reality, the auction price is influenced not only by the advertiser’s bid but also by factors such as the keyword quality scores of both the advertiser and their competitors. In this section, we relax the assumption of a single advertiser and introduce two competing advertisers in the market.

This section investigates the effects of advertiser competition on the SE advertising market. Notably, advertiser competition does not affect the price of SEO services. Section 4 assumed a perfectly competitive SEO market, where service prices are influenced mainly by SE robustness.

In practice, the price of PSM is influenced by the advertiser’s bid $p$ and keyword quality score e. The quality score evaluates the keyword and associated webpage, reflecting search users’ recognition of the keyword. Advertisers with higher quality scores can achieve more desirable ad rankings at lower prices. Therefore, we assume that there are two competing advertisers (denoted as $a d _ { 1 }$ and $a d _ { 2 } )$ in the market, and advertiser $a d _ { 1 }$ bids p in the keyword auction, resulting in the final auction price:

$$
\frac {e _ {1}}{e _ {2}} p\tag{A16}
$$

In practice, a higher quality score for an advertiser’s keyword grants a competitive advantage, as it lowers the quality scores of competitors’ keywords, reducing the final auction price. This point is evident in Equation (A16), where the quality scores $e _ { 1 }$ and $e _ { 2 }$ represent the quality scores of the two competing advertisers’ keywords. Therefore, we derive the utility function of advertiser $a d _ { 1 }$ under different strategies:

$$
\begin{array}{c} {u _ {1} = \alpha q _ {e} r _ {s} (v - \frac {e _ {2}}{e _ {1}} p)} \\ {u _ {2} = \alpha q _ {e} r _ {o} v - \beta q _ {r}} \\ {u _ {3} = \gamma \alpha q _ {e} r _ {o} v - \beta q _ {r} + \alpha q _ {e} r _ {s} (v - \frac {e _ {2}}{e _ {1}} p)} \end{array}
$$

The strategy selection area of advertiser $a d _ { 1 }$ can be obtained through the utility comparison of advertiser $a d _ { 1 { : } }$ , as shown in Figure C14.

It is evident that the competition among advertisers does not significantly affect the survival conditions $( \frac { \lambda q _ { r } } { \alpha \gamma q _ { e } r _ { o } } < V )$ of

SEO firms. This is primarily because the competitors of SEO enterprises are the SEs, not other advertisers. Although the competition among advertisers may influence the prices of advertisements, it will not impact the robustness of the SE, which is a crucial factor affecting the survival of SEO enterprises.

Even though the competition among advertisers has no effect on the survival conditions of SEO enterprises, we have found that it exerts a significant impact on the final auction price of PSM. When advertiser $a d _ { 1 }$ has a competitive advantage $\left( e _ { 2 } < e _ { 1 } \right)$ , the price offered by $a d _ { 1 }$ will be higher than in a non-competitive market and may exceed the advertiser’s maximum willingness to pay (V). This is because $a d _ { 1 }$ knows the high quality of its keywords, reducing the final transaction price of PSM in the auction. Conversely, when $a d _ { 1 }$ is disadvantaged, it should lower its bid for PSM to prevent an excessively high final transaction price.

![](/api/attachments/EM976JN4/fulltext/images/62cb30c002ec76cf2ea4281bbf414bf641911806cf6c9a473dc4543d7879225f.jpg)  
(1) $e _ { 1 } { < } e _ { 2 }$

![](/api/attachments/EM976JN4/fulltext/images/d38cc9957c59306c486ee87f3ff6249bbf90798ff0848af8756243a2b61262a4.jpg)  
(2) $e _ { 2 } < e _ { 1 }$  
Figure C14. Market share of the SE in the Presence of Competition Among Advertisers

Comparing the optimal decisions and maximum profits of SEs under different conditions leads to Theorem C7, which primarily elucidates the influence of advertiser competition on the survival of SEO enterprises.

Theorem C7: For SEs, it may not always be the optimal choice to eliminate SEO enterprises from the market when there is competition among advertisers.

Similar to the basic model, when PSM is the only option available, greater robustness benefits SEs by restricting the development of SEO companies. When SEO exists without SEO+PSM, the primary goal of SEs should be to minimize the market share of SEO companies. In contrast, when SEO+PSM is present, lower robustness is favorable for expanding the strategy selection of SEO+PSM, reducing internal competition, and thereby achieving optimal profit.

By comparing the optimal profits of SEs under different conditions, it can be concluded that competition among advertisers does not alter the conclusions from the baseline model, particularly Theorem 1. Therefore, eliminating SEO enterprises and removing external noise in search engine rankings may not necessarily be the optimal choice for SEs, irrespective of advertiser competition. Specifically, competition among advertisers influences their bidding behavior and the optimal decisions and profits of the SE. This competition prompts advertisers to adopt more competitive bidding strategies, which in turn affects SE decisions and profits. However, this competition does not fundamentally alter the conclusions of Theorem 1 and C1. The findings from these theorems remain applicable even in a competitive market environment.

This finding implies that SEs should thoroughly evaluate the decision to eliminate SEO enterprises in the context of advertiser competition and recognize that removing external noise may not always be the most advantageous option. In a fiercely competitive market, SEs must consider the impact of advertiser competition on optimal decision-making and profit to find the balance that best aligns with their interests. Managers should learn from this conclusion and fully consider the complexities of market competition when formulating marketing strategies and making decisions, to ensure sustainable competitive advantages and profit growth.

In summary, the results of the extended model in this section indicate that competition between advertisers influences their bidding strategies, which, in turn, affects the SE’s optimal decisions and profits. This competitive environment drives advertisers to adopt more aggressive bidding approaches, thereby further influencing the SE’s decisions and profitability However, we also demonstrate that, in line with the base model, advertiser competition does not alter the core conclusions of the baseline model. Specifically, even in the presence of competition, excluding SEO firms is not necessarily the SE’s optimal choice.

## Appendix D: Document Analysis

To provide a more comprehensive overview of the research landscape, we conducted a systematic analysis of relevant literature using the VOSviewer tool. The analysis involved the following steps: first, we retrieved articles from the Web of Science (WOS) Core Collection database using “search engine optimization” as the topic. In this paper, our research focuses on two primary forms of search engine marketing: search engine optimization and paid marketing. It is important to clarify that the term “paid search marketing” was not selected as a keyword in the retrieval process due to the broad categorization and inconsistent nomenclature associated with paid marketing approaches. For instance, “PSM” (pay-persale), as mentioned in the text, represents one designation within this category; other common terms include PPC (payper-click), CPM (cost per mille or thousand impressions), and CPC (cost per click). In contrast, employing “Search Engine Optimization” as a keyword facilitates a clearer delineation of the relationship between SEO and paid marketing strategies while mitigating issues arising from naming inconsistencies.

We then selected the top 2,000 most relevant papers for analysis. Using VOSviewer, we generated a keyword cooccurrence map of these articles, as shown in Figure D1. Notably, keywords related to “paid search marketing” were absent in the results for “search engine optimization,” suggesting that research on “search engine optimization” rarely addresses aspects related to paid search marketing.

![](/api/attachments/EM976JN4/fulltext/images/6e2fcede2df5188cd291dc9cacbd2e8f211a2bed6cb2b69fbdc9ce863e3c0c99.jpg)  
Figure D1. Keyword Co-Occurrence Map of Articles on Search Engine Optimization

Figure D2 shows the keywords most related to search engine optimization. The keywords most frequently associated with “Search Engine Optimization” include “optimization,” “performance,” “machine learning,” “algorithm,” “system,” “design,” and “information retrieval,” as illustrated in Figure D2. This indicates that the literature predominantly focuses on technological advancements, such as machine learning, to optimize algorithms and achieve desired outcomes. However, few studies have examined the competitive or cooperative dynamics between search engine optimization and paid search marketing.

![](/api/attachments/EM976JN4/fulltext/images/7c5784bebcd075bb60957ac67305e2e9e8f7cfd35e1df0d0364f692d77d8af75.jpg)  
Figure D2. Keywords Most Closely Related to Search Engine Optimization

This finding suggests that the existing literature on search engine optimization predominantly emphasizes technical aspects while offering relatively little insight into its competitive dynamics within the digital marketing ecosystem. Although search engine optimization and paid search marketing constitute two fundamental strategies that firms use to compete for search engine traffic—coexisting and interacting over the long term in real-world markets—the academic community has yet to systematically investigate their competitive interactions and underlying market mechanisms. Our study directly addresses this critical research gap by conducting a comprehensive analysis of the competitive dynamics between search engine optimization and paid search marketing, as well as their impact on market participants, with the goal of uncovering the underlying principles of search engine market evolution. This research not only enhances the understanding of search engine business models but also offers theoretical support to firms in developing more effective online marketing strategies, ultimately bolstering their competitiveness in the digital economy.

## About the Authors

Kai Li is a professor of information systems at the Business School of Nankai University. He received his PhD in technical economy and management from Nankai University. His research interests include online platforms, online privacy, and business intelligence. He has published papers in journals including Decision Support Systems, Information and Management, Journal of Small Business Management, among others.

Chunyang Shen is a PhD candidate in information systems at the Business School, Nankai University. His research interests include e-commerce platforms, platform business models, and artificial intelligence.

Lin Mei is an assistant professor at the School of Information Systems, Singapore Management University. Her research focuses on information systems, economics of information systems, and two-sided markets, and she has published in journals such as Journal of Management Information Systems and Decision Support Systems.

Zhangxi Lin is a professor at the Business School of Texas Tech University. His research interests lie in e-commerce, data mining, and information economics, and he has published papers in journals such as Decision Support Systems, European Journal of Information Systems, European Journal of Operational Research, and Information Systems Research.

Copyright © 2025 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via email from publications@aisnet.org.
