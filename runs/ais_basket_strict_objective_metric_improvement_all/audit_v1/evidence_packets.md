# Manual-audit evidence packets

Generated from the fixed stratified sample. Extracts are navigation aids; manual judgments must be checked against the source full text.

# Audit 01: Integrating rich and heterogeneous information to design a ranking system for multiple products

- Group: `retained_layer:algorithm_or_computational_method`
- Model decision: `True`; centrality `exclusive`; layer `algorithm_or_computational_method`
- Gates: `{"purposeful_solution_design": true, "objective_metric_is_primary_target": true, "comparative_improvement_demonstrated": true, "objective_improvement_is_the_success_basis": true}`
- Model reason: 该文提出了一个明确的信息系统解决方案——多产品eWOM排名算法及原型系统；核心成功标准是排名与京东销售排名的Spearman相关系数这一客观指标；全文以该指标的对比实验为主要证据，展示了相对多个基线的显著改进；满意度、感知有用性等主观变量未作为成功依据。四项门控均通过，客观指标中心性为exclusive。
- Source: `E:\github\qual-llm-check-IS-utd\database_fulltext_all\08364_2016_integrating-rich-and-heterogeneous-information-to-design-a-ranking-system-for-multiple-products.md`

#### Abstract

The online review plays an important role as electronic word-of-mouth (eWOM) for potential consumers to make informed purchase decisions. However, the large number of reviews poses a considerable challenge because it is impossible for customers to read all of them for reference. Moreover, there are different types of online reviews with distinct features, such as numeric ratings, text descriptions, and comparative words, for example; such heterogeneous information leads to more complexity for customers. In this paper, we propose a method to integrate such rich and heterogeneous information. The integrated information can be classified into two categories: descriptive information and comparative information. The descriptive information consists of online opinions directly given by consumers using text sentiments and numeric ratings to describe one specific product. The comparative information comes from comparative sentences that are implicitly embedded in the reviews and online comparative votes that are explicitly provided by third-party websites to compare more than one product. Both descriptive information and comparative information are integrated into a digraph structure, from which an overall eWOM score for each product and a ranking of all products can be derived. We collect both descriptive and comparative information for three different categories of products (mobile phones, laptops and digital cameras) during a period of ten days. The results demonstrate that our method can provide improved performance compared with those of existing product ranking methods. A ranking system based on our method is also provided that can help consumers to compare multiple products and make appropriate purchase decisions effortlessly.

Keywords: text sentiments, numeric rating, comparative relationships, product rankings

#### 1 Introduction

With the rapid development of e-business and Web 2.0, an increasing number of people prefer to shop online and exchange opinions through the Internet. Researchers often refer to theses online opinions in consumer reviews about a product, service, brand or company as electronic word-of-mouth (eWOM). eWOM is becoming a major source of information for potential buyers to make informed purchase decisions [10][18][20]. Nicosia[39] argues that information search and alternatives evaluation are two of five essential stages of the consumer-purchase decision process: (1) problem recognition, (2) information search, (3) evaluation of alternatives, (4) purchase decisions, and (5) post-purchase behavior. A survey <sup>1</sup> found that 63% of online shoppers consistently search and read reviews before making a purchasing decision. Among these, 64% of the online shoppers spend 10 minutes reading reviews, whereas 33% spend 30 minutes or more. Evidently, an increasing number of consumers prefer to evaluate and choose products based on

#### 5 Experiments



#### 5.2 Evaluation and discussion



#### 5.2.1 Evaluation of our method

The online eWOM has been recognized widely as an important factor in product sales [5][6][20]. Some studies use sales rank as an indicator of product eWOM ranking [50][54], an approach also adopted in this paper. For each product, the e-commerce websites $J d . c o m ^ { 1 3 }$ in China provides sales rank in descending order, in which a rank of 1 represents the bestselling product. We use the correlation between our ranking results and Jd’s sales rank to measure the performance of our ranking method. The Spearman ranking correlation coefficient is defined as the correlation coefficient between the two ranks that is given by:

$$
\rho \left(\overrightarrow {R _ {x _ {i}}} - \overrightarrow {R _ {y _ {i}}}\right) = 1 - \frac {6 \sum_ {i = 1} ^ {n} \left(R _ {x _ {i}} - R _ {y _ {i}}\right) ^ {2}}{n \left(n ^ {2} - 1\right)}\tag{13}
$$

where $R _ { x _ { i } }$ and $\overrightarrow { R _ { y _ { i } } }$ are the rank by our approach and the rank from sales performance, respectively. The correlation coefficient ρ is between -1 and 1. ρ closer to 1 implies a more positive correlation between calculated products rank and Jd’s sales rank.

The methods most related to our research include Zhang and Guo’s product comparison networks (denoted as Z&G’s method for short)[54] and Zhang and Narayanan’s product comparison graph model [51][52] (denoted as Z&N’s method for short). Both Z&G’s method and Z&N’s method are inspired by PageRank algorithm [40]. Although we share the fundamental graph structure, there are some major differences between our method and the above two methods.

In Z&G’s method, they introduced a directed and weighted edge that indicates a comparative relationship between two products, and the weight on each edge was computed from comparative sentences. However, there was no weight for each node in their graph structure [54]. In short, Z&G’s method only use comparative sentences, and they ignore the other useful information such as ratings, sentiments or votes. Unfortunately, comparative sentences in consumer reviews are very rare. Among the 96 products we collected, there are only 34 products linked with edges. In other words, there are (a few) comparative sentences for only 34 products, and there is not a single comparative sentence for the other 62 products. As a result, only 34 products could be compared in a ranking; the others will have no ranking.

Z&N’s method was proposed to take both node and edge weights into account when ranking products

#### 6 Conclusions and Future Work

Recent trends have indicated that before making purchasing decisions, consumers prefer to compare the eWOM of products involved in online reviews. In this paper, we design a novel eWOM ranking method to help consumers compare multiple products by integrating the rich information from heterogeneous sources including numeric ratings, text reviews, comparative sentences and comparative votes. We find that with more information integrated, the ranking method can return better performance. In particular, comparative votes, which have attracted little attention in previous studies, contribute significantly to the ranking quality. An effective system is also demonstrated to help customers make informed choices when comparison shopping and assist manufacturers to maintain awareness of the exact positions of their products and to target implicit problems underlying the data.

In spite of the contributions made in this research, there are limitations which need further exploration. Although our approach exhibits a promising performance from experimental results, the current research could be enhanced by a more solid theoretical foundation to deeply analyze the working principle. For example, it could help improve the performance if the precise role or relative importance of each type of information could be determined theoretically.

There are certain studies that investigate the property of one type of information, such as rating [20], text sentiments [38] and comparative sentences [29], and several studies have noted a comparison between multiple types of information. Archak et al. [1] have addressed the question of whether text sentiments have more influence on product sales beyond the numeric ratings, and they observed that the absolute value of the coefficient on the average review rating goes down when textual data are incorporated into the model. Hu et al. [24] found that ratings have an indirect impact through sentiments, whereas sentiments have a direct significant impact on sales. Wang et al. proposed a general assumption that the reviewer assigns a rating by evaluating many aspects of the product based on the sentiments of words he used to discuss that aspect, and the overall rating depends on the weighted sum of all the aspect ratings[48]. In addition, Liu discovered that the impact of WOM is dynamic and its pattern could evolve over time [36], which makes it more difficult to determine a stable underlying mechanism. Furthermore, there is also certain negative evidence. For example, Dave et al. discovered that similar qualitative descriptions can yield very different quantitative reviews from reviewers, and in the some extreme cases, reviewers even do not understand the rating system [9]. In a word, the existing research has not presented any consistent conclusion, which could hardly provide a solid theoretical foundation but reward research direction for the future work.


# Audit 02: Content-based object organization for efficient image retrieval in image databases

- Group: `retained_layer:algorithm_or_computational_method`
- Model decision: `True`; centrality `exclusive`; layer `algorithm_or_computational_method`
- Gates: `{"purposeful_solution_design": true, "objective_metric_is_primary_target": true, "comparative_improvement_demonstrated": true, "objective_improvement_is_the_success_basis": true}`
- Model reason: 该文设计和实现了一个IS相关的解决方案（blob-centric图像检索方案），包含具体算法和数据结构；核心目标是提高客观指标（查询响应时间/IO成本），且通过解析模型和定量对比证明代表blob方法和索引方法相对于naive方法的显著改进；文章的成功主张完全依赖该客观效率指标，无主观结果。因此四个门均通过，centrality为exclusive。
- Source: `E:\github\qual-llm-check-IS-utd\database_fulltext_all\06616_2006_content-based-object-organization-for-efficient-image-retrieval-in-image-databases.md`

#### Abstract

Much research has focused on content-based image retrieval (CBIR) methods that can be automated in image classification and query processing. In this paper, we propose a blob-centric image retrieval scheme based on the blobworld representation. The blobcentric scheme consists of several newly proposed components, including an image classification method, an image browsing method based on semantic hierarchy of representative blobs, and a blob search method based on multidimensional indexing. We present the database structures and their maintenance algorithms for these components and conduct a performance comparison of three image retrieval methods, the naive method, the representative-blobs method, and the indexed-blobs method. Our quantitative analysis shows significant reduction in query response time by using the representative-blobs method and the indexed-blobs method.

© 2006 Elsevier B.V. All rights reserved.

Keywords: Blob-centric image representation; Content-based image retrieval; Image database management; MB<sup>+</sup>-trees; Multi-dimensional indexing; Object-oriented image organization

#### 1. Introduction

Research in information retrieval, database management, computer vision, and image processing is converging towards providing content-based access to image databases. Researchers in multimedia databases have outlined the main problems in image database management [7,11,15,17], including the semantic issues in image representation and organization, the methods of identifying and indexing image objects, browsing and searching images using sophisticated querying techniques such as imprecise queries, user-directed query processing, and similarity measures.

Common feature-based Query-by-Image-Content (QBIC) systems, such as IBM QBIC [5,18], and Photobook [21] incorporate various distance metrics and matching algorithms. Other systems that identify images using low-level properties such as color, texture and shape [16] include Virage [8], Candid [13], Chatbot [20]. All the above systems use the color-layout matching model, in which images are retrieved if and only if they contain the exact combination of low-level features specified in the query. Although low-level features are easily obtainable, the quality of the results retrieved based on these low-level features is often not satisfactory because the user may have difficulty in translating their needs into the appropriate values in these low-level features [15].

Research trends in content-based image retrieval (CBIR) have shifted to object-oriented techniques, for example region-based image retrieval [4,14,22]. These new techniques extract portions of the images and encapsulate their low-level features in data objects that take into account of spatial features as well. Based on these objects, images can then be classified and categorized in new ways that are not possible in the existing commercial image database systems. A major advantage of the object-oriented techniques is ease of query formulation and interpretation. Using the image objects, the user can formulate queries in more flexible ways such as using combinations of different sample objects, rather than using low-level features directly.

An object-oriented image representation called blobworld has been developed at the University of California at Berkeley [3,2]. In a blobworld, portions of image that are relatively homogeneous in image features are extracted from an existing image and are represented as objects, referred to as blobs. The most representative blobs are then used to identify similar images with automatic matching and classification 

#### 6. Performance analysis of the image retrieval techniques

In this section, we evaluate and analyze three CBIR methods, the naive method, the representative-blobs method, and the indexed-blobs method in order to compare their performances in terms of IO-bound property, and cost. The definitions and setups of the evaluations are given in Sections 6.1 and 6.2. The objective is to show the potential reduction in search costs by using representative-blobs and the MB<sup>+</sup>-tree.

#### 6.3. Performance analysis

We conducted a comparative analysis of the three blobbased image retrieval methods. The performance study examines the effects of several important parameters on the efficiency of the three methods. The results can indicate the applicability of each method and demonstrate the advantage of using representative blobs and applying an indexing method in blob-based image retrieval.

The default parameter values used in the performance analysis are given in Table 2. According to [10], the industry standard SCSI bus for nCUBE/2 multiprocessor system results in an effective IO bandwidth from 0.25 to 4 Megabytes per second. Therefore, we use 1 Megabytes per second as the default value for TransRate. We will also analyze the effect of various values in IO bandwidth.

Fig. 9 shows that there is a tremendous difference in total IO cost between the naive method and representative method because the number of representative blobs is 50,000 while the number of stored blobs in the naive method is 4,500,000. Therefore, using the representative method can reduce the query response time by 90 times. In essence, the representative-blobs method pre-computes and classifies all blobs into groups so that the cost required to compare the sample blob and the stored blobs is reduced. Of course, the true cost reduction in specific cases depends on the ratio of representative blobs and the total stored blobs in the naive method. But it is conceivable that this reduction can be very large for an image database in an application area where the number of blobs in each group is large. The figure also indicates that when the IO bandwidth is small to medium, the naive method is too slow to be satisfactory.

Default parameter values for the simulation

<table><tr><td>Parameter</td><td>Value</td><td>Unit</td></tr><tr><td>TransRate</td><td>1</td><td>Megabytes/s</td></tr><tr><td>BlobSize</td><td>296</td><td>Bytes</td></tr><tr><td>NumBlobsPerImage</td><td>9</td><td></td></tr><tr><td>NumImages</td><td>500,000</td><td></td></tr><tr><td>SeekTime</td><td>2</td><td>ms</td></tr><tr><td>PageSize</td><td>4</td><td>Kilobytes</td></tr><tr><td>RatioRepBlobs</td><td>0.1</td><td>NumRepBlobs/NumImages</td></tr><tr><td>MaxNumPagesPerQuery</td><td> $2^6$ </td><td></td></tr></table>

Naive ApproachRepresentative BlobsWith Index  
[image omitted]  
Fig. 9. Total IO cost as a function of data transfer rate.

The comparison in total IO cost between the representative-blobs method and the index method indicates also

#### 7. Conclusions

CBIR is one of the most important research areas in image databases. One major development in this area was the automatic identification and classification paradigms using region-based object extraction techniques such as the blobworld approach [3,2]. In a blobworld, portions of image that are relatively homogeneous in image features are extracted from an existing image and are represented as objects, referred to as blobs. The most representative blobs are then used to identify similar images with automatic matching and classification algorithms. However, no attempt has been made in applying the blobworld paradigm in a large-scale image database to support efficient querying and browsing.

In this paper, we proposed a blob-centric image retrieval scheme in image databases that is comprised of several new ideas in image database organization and CBIR using the blobworld representation. Our objective was to develop an image data organization and its related algorithms to support similarity-based image browsing and querying. Another important thrust of our study was to improve the query response time by means of representative-blobs and multi-dimensional indexing. Our main contributions can be outlined as follows:

1. We introduced the concepts of representative blob, blob group, and image category and developed the algorithms for their initialization and maintenance. The purpose of representative blobs is to reduce the search space while providing sufficient quality in image browsing and querying. We also applied the MB<sup>+</sup>-tree index to the blobworld paradigm and developed automatic algorithms for computing similarity-based queries using sample images and blobs.

2. We also developed a semantic-based data organization that allows the user to browse the image database without having to provide sample images. The initialization and maintenance algorithms for the data organization are also given. We suggested that finer classification of the representative blobs can potentially improve the accuracy of automatic classification of images.

3. To assess the potentials on efficiency improvement by applying the representative blobs and the MB<sup>+</sup>-tree indexing, we derived IO-bound cost models for three approaches, the naive method, the representative-blobs method, and the indexed-blobs method. Our research focused on large-scale image databases where efficient retrieval is a challenging issue. The quantitative analysis showed that over 90% reduction in query response time can be achieved in a large image database containing 500,000 images by using the representative-blobs method and the indexed-blobs method.

Some pending further improvements and enhancements on the proposed image retrieval scheme include studies of (1) object representation and formation techniques — what features should or should not be included in object representation for efficient retrieval and management; (2) object category — how to derive the object category and how to determine the relationships among representative blobs and their blob groups. Specific related techniques include shape similarity matching, color object searching, image object recognition, image content representation, visual object tracking, edge comparison, image registration and so on.


# Audit 03: A Matter of Equality: Linear Pricing in Combinatorial Exchanges

- Group: `retained_layer:digital_platform_mechanism_or_policy`
- Model decision: `True`; centrality `exclusive`; layer `digital_platform_mechanism_or_policy`
- Gates: `{"purposeful_solution_design": true, "objective_metric_is_primary_target": true, "comparative_improvement_demonstrated": true, "objective_improvement_is_the_success_basis": true}`
- Model reason: 论文设计了组合交易所的线性匿名定价机制（SL/BL/1L）和柔性投标语言，属于数字化平台机制设计；其核心目标是效率损失这一客观度量，并以WDP为基准通过理论证明和基于真实数据的数值实验显示SL/BL几乎达到最优、且显著优于1L，同时也展示计算可行性；论文没有依赖主观量表或满意度等指标，成功判断完全基于客观的贸易利得、计算时间和悖论拒绝投标比例等。因此四个门全部通过，客观指标中心性为exclusive。
- Source: `E:\github\qual-llm-check-IS-utd\database_fulltext_all\08542_2018_a-matter-of-equality-linear-pricing-in-combinatorial-exchanges.md`

#### 1. Introduction

This paper is motivated by the design of a combinatorial exchange to facilitate the reform of the fishing industry in New South Wales (NSW), Australia. This reform is needed because the NSW fishing industry sufers from overfishing that jeopardizes its long-run commercial viability. The industry is characterized by the familiar 80–20 rule, that is, fewer than 20% of the fishing businesses do more than 80% of the catching. Furthermore, there are no measures to prevent overfishing: anyone with a business license is allowed to catch any amount and type of fish.

To ensure ecological sustainability and improve the industry’s profitability, the NSW government decided to link (efort to) catch to fishery access rights, or “shares.” Some 20 years ago, these shares were distributed evenly among more than 1,100 commercial fishers, but they were never efectuated, that is, all that was needed to fish was a business license. Under the government’s recent “linkage program,” however, shares have become binding and are directly tied to possible catch (eforts). There are over a hundred different share classes describing diferent types of access rights across several regions. A share class may determine a permission to catch certain types and quantities of fish, or stipulate allowed eforts (e.g., maximum number of days of fishing per week, or the number of hooks per line, the number of nets, etc.).

A consequence of the linkage program is that the top 20% most active fishers face an immediate deficit of shares. They were originally given the same number of shares as other fishers but need far more to accommodate their high volumes of catch. To cover their deficits, active fishers will need to purchase shares from less active fishers who, in some cases, will wish to sell their entire business and leave the industry. The question is how to best accomplish this transfer of shares, taking into account institutional details and constraints.

Decentralized bargaining would certainly not work. Fishers are geographically dispersed across the state, making it very costly to find all eficient buyer–seller matches. Moreover, exiting fishers would have to sell their shares separately, exposing them to the risk that they sell some, but not all, of their shares. This exposure problem may cause exiting fishers to be left with a fragmented portfolio of shares and little proceeds. Finally, regulation requires those fishers that remain in the industry to hold a minimum number of shares in a g

#### 5. Experimental Evaluation

Our theoretical results are independent of a specific domain. In our experimental evaluation, we want to analyze the average eficiency losses incurred by linear prices, the payof distribution between buyers and sellers for single linear prices, the average proportion of paradoxically rejected bids in diferent pricing schemes, and the computational hardness of the allocation problem for the market for fishery access rights. Here we can consider the details of the environment, which gives us a good estimate of what can be expected in a real-world market. We are fortunate to have a data set from an Australian fishery market available, which allows us to generate realistic problem instances.

#### 5.2. Experimental Design

Overall, we have the following treatment variables for our numerical experiments:

• Prices: We analyze SL, BL, and 1L payment rules, described in Section 4. The eficient allocation without pricing (WDP) serves as the baseline.

• Participation probability $\rho \colon$ This determines the ratio of the total number of fishers to participate in the auction. When $\rho = 1 . 0 ,$ , this means that all 1,000 fishers (from our data set) submit bids. A value of $\rho = 0 . 5$ means that only half the fishers participate in the market. With participation probability $\rho = 1 . 0 _ { \cdot }$ , we get around 1,300 bids (each buyer can submit up to five bids).

• Sell bid probability α: This determines the ratio between buyers and sellers. We consider values 0.3 and 0.5.

• Probability of fixed buy-side bid $f \colon$ This determines the ratio of buyers who submit a buy-side bid for a specific quantity only rather than a range, that is, $\bar { Y } _ { b } = \underline { { \hat { Y } } } _ { b }$ . All others specify flexible bids with range of $\bar { Y } _ { b } > \underline { { Y } } _ { b }$ . We allow for two possible values. A value of $f = 0$ <sup>¯</sup>means that no bidder submits a fixed buy-side bid, and a value of $f = 0 . 5$ means that half of the bids have fixed quantities.

• Maximum package size κ: This determines the maximum amount of share classes that a sell bid may contain. We use the values 2 and 4.

• Spread of mean values $\Delta _ { \mu } .$ : This determines relative diference in the mean values of the buy-side and sell-side value distributions. We use the values 0.3 and $0 . 5 ;$ that is, on average, buyers (sellers) tend to overestimate (underestimate) the common value by 0.15% (0.25%).

• Standard deviation σ: This determines the standard deviation for the two value distributions. We use the values 0.2 and 0.4.

Of course, the number of shares included will also have an impact on the problem size, and a decreasing the number of shares will make it easier to solve. We decided to limit the number of treatment variables and rather use participation probability as a parameter to control problem size. Based on the underlying data about initial endowments of shares to fishers and diferent values for these treatment variables, we generate problem instances. Overall, we have seven treatment variables and a full factorial $4 \times 2 \times 2 \times 2 \times 2 \times$ $2 \times 2 = 2 5 6$ design with the response variables eficiency loss, w; pa

#### 5.3. Experimental Results

Let us first provide an overview of the results. Table 1 shows a summary of the experimental results for the welfare-maximizing solution (without pricing constraints; the WDP) and 1L, SL, and BL prices. It shows that BL and SL prices lead to almost no eficiency loss on average, but 1L pricing incurs an average eficiency loss of 6.2% across all treatment combinations. As we will see in the detailed results, the worst-case eficiency loss can also be higher, and there is a trade-of that regulators face between the benefits of a single linear price and the eficiency loss it causes. In summary, however, the average case eficiency loss in the experiments is much lower than what the worst-case analysis might suggest.

The mean seller payof ratio $\left( \hat \pi _ { S } \right)$ is only of interest for the 1L prices, and Table 1 shows that around 39% of gains from trade are allocated to sellers on average. If an equal split of the gains from trade were desirable, this could be considered in the price computation. Computation was rarely an issue, even though the highest MIP gap found for BL prices was 36% with a timeout of 500 seconds. The average MIP gap is negligible for all pricing rules, which is remarkable given the problem sizes, and it provides evidence that combinatorial exchanges of this size can be organized nowadays.

We also computed the outcome of the VCG mechanism for a number of instances. However, the budget deficit of the auctioneer was around 50% of the gains from trade generated by the auction, which would not be acceptable in the field. This is why we do not report VCG results. Let us now discuss the results for the different focus variables in more detail.

Table 1. Overall Comparison of Pricing Rules: Mean Social Welfare Loss w¯ , Mean Seller Payof Ratio ${ \bar { \pi } _ { S } } ,$ Mean Computation Time <sup>¯</sup>t, Mean MIP Gap g¯, Maximum MIP Gap max<sup>(</sup>g<sup>)</sup>, and Average Ratio of Paradoxically Rejected Bids e¯ Within a Run Time of 500 Seconds

<table><tr><td>Pricing</td><td> $\bar{w}$ </td><td> $\bar{\pi}_{S}$ </td><td> $\bar{t}$ </td><td> $\bar{g}$ </td><td> $\max(g)$ </td><td> $\bar{e}$ </td></tr><tr><td>WDP</td><td>0</td><td>0</td><td>0.28</td><td>0</td><td>0</td><td>0</td></tr><tr><td>BL</td><td>0.0039</td><td>0</td><td>11.3</td><td>0.00058</td><td>0.36074</td><td>0.022</td></tr><tr><td>SL</td><td>0</td><td>1</td><td>0.69</td><td>1.00E-05</td><td>1.00E-04</td><td>0.030</td></tr><tr><td>1L</td><td>0.0618</td><td>0.39<

#### 7. Conclusions

The design of electronic markets has been an important field of research in the management sciences. In particular, pricing and the design of bid languages have been key concerns adding to game-theoretical and purely algorithmic questions discussed in economics and computer science, respectively. Combinatorial exchanges are now possible because of the advances in information technology and efective methods to solve large integer programming problems. However, there is still little research on pricing and bid languages for combinatorial exchanges. This paper contributes to the growing information systems literature on electronic market design. This market design, and the environment, is interesting on its own, with applications also in other areas of the world and other domains.

Linear and anonymous prices are often a requirement in two-sided markets, motivated by equitable treatment of all buyers and sellers in a market. In combinatorial markets with package bids, it is typically impossible to compute Walrasian, that is, linear and anonymous, competitive equilibrium prices. Simple linear and anonymous prices are used on energy markets, but they can lead to welfare losses because they lead to additional constraints in the respective winner determination problems. In addition, there will be paradoxically rejected bids, that is, bids that are better than the market price but still rejected. So far, not much is known about combinatorial exchanges with linear prices, even though such prices are a requirement in many markets. For market designers, it is important to understand the order of magnitude of the eficiency losses due to linear and anonymous prices and the proportion of paradoxically rejected bids. We provide evidence that such markets are tractable for realistic problem sizes and that the eficiency losses due to linear prices are surprisingly small.

#### D.7. Experimental Result Notation

w¯ Mean social

$\sigma _ { w }$ Standard deviation for welfare loss

$\bar { \pi } _ { S }$ Mean seller payof ratio, that is, percentage of all

gains from trade that sellers get

<sup>¯</sup>t Mean computation time

$\sigma _ { t }$ Standard deviation for computation time

g¯ Mean MIP gap

max<sup>(</sup>g<sup>)</sup> Maximum MIP gap

e¯ Average ratio of paradoxically rejected bids


# Audit 04: Mobile Time-Based Targeting: Matching Product-Value Appeal to Time of Day

- Group: `retained_layer:digital_platform_mechanism_or_policy`
- Model decision: `True`; centrality `dominant`; layer `digital_platform_mechanism_or_policy`
- Gates: `{"purposeful_solution_design": true, "objective_metric_is_primary_target": true, "comparative_improvement_demonstrated": true, "objective_improvement_is_the_success_basis": true}`
- Model reason: 文章设计并实施了一种 IS 相关的移动时间定向机制——根据时段匹配 utilitarian/hedonic 价值诉求的短信推广，并在随机实地实验中以客观购买行为作为主要成功标准，展示了对行业基线（全时段 utilitarian 诉求）的显著改进（15% vs. 8.7%）。后续问卷中的主观购买意愿仅用于检验心理机制，属于从属地位；因此四个门均通过，客观指标中心性为 dominant。
- Source: `E:\github\qual-llm-check-IS-utd\database_fulltext_all\07344_2019_mobile-time-based-targeting-matching-product-value-appeal-to-time-of-day.md`

#### Introduction

Mobile technologies, as a key contemporary form of information technologies (ITs), are known for their capability to enable “any place, any time” communication [1, 6, 15]. This has given rise to a new phenomenon called “perpetual contact” [16, 59, 64], whereby people are always with their mobile devices and are available for communication throughout the day. As an indication of this, a recent report by Ofcom shows that people check their smartphones, on average, every 12 minutes of the waking day.

This unique property of mobile technologies is by no means trivial, given the intimate relationship between time and ITs that has been highlighted in the literature [65, 77, 85, 106]. As Saunders [85] notes in an editorial article, “Perspectives on Time,” which discusses the importance of time in IS research: “What is something that plays an important role in most of the things that you do, but about which you often don’t consciously think? It’s time.” (p. iii) Earlier research highlights how ITs change the ways tasks are performed in organizations (e.g., Lee [65]) and how individuals organize their daily activities around time (e.g., Green [45]), generally noting a change in the tasks and activities from being more constrained to being more flexible. The intimate IT-time relationship has become more salient with the emergence of mobile technologies, owing to their seamless integration into people’s everyday life [22, 45, 87].

Research in the recent decade has tried to address the relationships between ITs and time by considering specific aspects of time, such as time duration, time difference, and time of day (see Table A1 in the Online Appendix A for a review). Our review shows that most extant studies have considered duration as a time factor and how it influences and is influenced by IT behaviors (e.g., de Guinea and Webster [28], Fuller and Dennis [39], Ko and Dennis [61], Williams and Pollock [101]), with some attention also paid to the effects of time difference in the virtual team context (e.g., Cummings et al. [24] and Sarker et al. [84]). A minimal amount of attention has, however, been paid to how time context<sup>2</sup> in people’s everyday life such as time of day may influence IT behaviors, despite the call for more research that considers time as a contextual factor in people’s experience of everyday technologies, of which mobile technologies represent a pertinent type [106].

Motivated to further our understanding about the relationships betwee

#### Field Experiment and Data

To test the hypotheses Hypothesis 1 and Hypothesis 3, we conducted a randomized field experiment sponsored by one of the largest mobile service providers in the world. The research design with a randomized field experiment was employed because it can control for consumers’ unobservable heterogeneity and thus avoid the endogeneity and causality biases that might confound the estimation results of mobile time-based targeting [3, 44]. Since any other systematic variations are randomized away across consumers, the differences in purchase likelihoods can then be attributed to the impact of the mobile time-based targeting. To generalize field experiment results and further test the underlying mechanism as stated in Hypothesis 2 and Hypothesis 4, we collaborated with a professional research company to survey mobile users about their relevant psychological perceptions.

#### Experimental Design

Our targeted population consisted of mobile users from a large city in Asia who had bought a 4G-ready mobile phone but had not subscribed to the 4G service package. The subjects are regular customers of the company. The selected customers did not receive previous promotional offers to subscribe to the service. We also ensured that each mobile user would receive only a single mobile message during the study to ensure the between-subjects design.

Mobile time-based targeting was varied on an hour-by-hour basis in our field experiment design. To more precisely identify the effectiveness of mobile targeting by time of day, our experiment design involved 12 hours (from 8:00 am to 8:00 pm) x 2 product value appeal framing (utilitarian vs. hedonic) between-subjects design. We operationalized hour-by-hour treatments by ensuring each participant received a message at a specific selected hour. The hour treatment groups were established to receive a message within the hour, each hour between 8:00 am and 8:00 pm (i.e., the first hour block was 8:00 am-9:00 am, the last hour block was 7:00 pm-8:00 pm, altogether 12 hours). The mobile message used in the field experiment included a promotional offer that expired 60 minutes after the message was sent (e.g., for the participants assigned to the 7:00 pm-8:00 pm hour block, some might receive the message at 8:00 pm; for these participants, they could respond before 9:00 pm). The starting time (8:00 am) and ending time (8:00 pm) of the field experiment were determined to capture the main portion of participants’ active day while avoiding boundary conditions from participants who are not yet awake or already asleep. The 60-minute expiration of the mobile deal required purchase of the offered product (4G mobile Internet service) during the designated hour.

Our corporate partner could identify each consumer who had received a promotional message as part of the field experiment during each hour to guarantee no cross-hour contamination between the hour treatment conditions. All subjects are similar to the general users of the company and were randomly assigned into each hour block. We randomly selected consumers from among the company’s population of mobile users, on the condition that they had not subscribed to the 4G mobile Internet service and received no offer on this service before (this was to ensure a basic condition that the service is relevant to them). We then randomly assigned them to the experimental hour-by-hour gro

#### Model and Results

Our model estimates consumer purchase adoption likelihood, Purchase Probability<sup>HOUR</sup> as a logit function of hours. We assume an i.i.d. (independent and identically distributed)extreme value distribution of the error term in the logit model:

$$
\text { Purchase   Like   lihood } _ {i} ^ {\text { HOUR }} = \frac {\exp \left(U _ {i} ^ {\text { HOUR }}\right)}{1 + \exp \left(U _ {i} ^ {\text { HOUR }}\right)}\tag{1}
$$

$$
\begin{array}{l} U _ {i} ^ {H O U R} = a ^ {m} + \sum \beta_ {1, 2, \dots 1 1} ^ {m} \times H O U R _ {i} + \sum \zeta_ {1, 2, \dots 1 1} ^ {m} \times H O U R _ {i} \times U T I L I T _ {i} + \zeta^ {m} \\ \times U T I L I T _ {i} + \gamma^ {m} \times X _ {i} + \epsilon_ {i 2} ^ {m}, \end{array}
$$

where $U _ { i } ^ { H O U R }$ denotes the utility of a purchase, UTILIT denotes the product content emphasis of the same product (1 = utilitarian and 0 = hedonic), and $X _ { \mathrm { i } }$ is a vector of consumer’s usage controls, including individual users’ monthly phone bills (ARPU), minutes used (MOU), number of SMS sent and received, and data usage (GPRS). These account for the unobserved fixed effects in consumers’ mobile usage behaviors across heavy or light mobile users. Table 1 reports the summary statistics of these consumers’ usage behaviors. $\varepsilon _ { i }$ is comprised of the idiosyncratic error terms. $\beta$ tests the effects of hour on purchase probability after controlling for consumer usage fixed effects. Because we have a total of 12 hours in the experiment design, we only need 11 dummies (the final hour of 7:00 pm to 8:00 pm is the baseline; we have also analyzed the data with other time contrast coding and found consistent results).

We assess the model goodness-of-fit with Nagelkerke $\mathrm { R } ^ { 2 }$ as specified in Equation 2, Pearson Chi-square $\chi ^ { 2 }$ in Equation 3, and Cox and Snell $\mathrm { R } ^ { 2 }$ in Equation 4.

$$
\text { Nagelkerke's } \mathrm{R} _ {\mathrm{N}} ^ {2} = \frac {\mathrm{R} _ {\mathrm{CM}} ^ {2}}{1 - \mathrm{L} (\mathrm{B} ^ {(0)}) ^ {2 / n}}\tag{2}
$$

Table 1. Statistics of Users’ Mobile Usage in Field Experiment of Mobile Targeting by Time of Day

<table><tr><td rowspan="2" colspan="2"></td><td colspan="16">Percentile (percent)</td></tr><tr><td>N</td><td>Mean</td><td>Median</td><td>Sd</td><td>Min</td><td>Max</td><td>Kurtosis</td><td>10</td><td>20</td><td>30</td><td>40</td><td>50</td><td>60</td><td>70</td><td>80</td><td>90</td></tr><tr><td rowspan="3">Panel A 

#### Hypotheses Testing Results

We conducted ordinary least square (OLS) regression to analyze the data, given that many of the variables involved are single-item measurements (i.e., the different mood types, including being energetic and relaxed that are the focal variables). We first examine the descriptive statistics of the data (see Table 3). Within respectively the morning and afternoon sessions, people’s purchase intention was relatively higher when given the message with a utilitarian product value appeal in the morning (weakly significant at $\mathrm { ~ p ~ } = \ 0 . 0 7 5 )$ ; while it was the message with a hedonic product value appeal that led to a higher purchase intention in the afternoon $( \mathtt { p } < 0 . 0 5 )$ . These result patterns are consistent with our Hypothesis 1 and Hypothesis 3 and provide further supports to our field experiment results that people were more receptive towards utilitarian product value appeal in the morning, and otherwise (hedonic product value appeal) in the afternoon. It is also worth noting that, consistent with our expectations, people were relatively more energetic in the morning than in the afternoon $( \mathtt { p } < 0 . 0 5 )$ , and relatively more relaxed vice versa (weakly significant at $\mathfrak { p } = 0 . 0 6 8 )$ ).

We next assessed the measurement model followed by the structural model. As shown in Online Appendix E, the analysis of the measurement models indicates satisfactory reliability and convergent validity levels of the constructs, that is, Cronbach’s Alpha $\mathrm { ( C A ) } > 0 . 7 0$ , Composite Reliability $\mathrm { ( C R ) } > 0 . 7 0$ , and Average Variance Extracted (AVE) > 0.50. Discriminant validity was assessed by comparing the square-root of AVE of each construct against its correlations with other constructs. The results in Table E2 in Online Appendix E show that the diagonal elements (square-root of AVE) exceeded other entries in the same row or column, thus satisfying the discriminant validity requirement.

We proceeded to analyze the relationships among the variables, as the model demonstrated satisfactory reliability, convergent validity, and discriminant validity levels. Table 4 presents the analysis results. It can be seen that for the respondents presented with the utilitarian product value appeal in the morning, being energetic (which is relatively higher in the morning than in the afternoon) did play an important role in influencing their intention to purchase the 4G mobile Internet service 

#### Discussion

With mobile technologies enabling “perpetual contact” [16, 59, 64], firms are presented with unprecedented opportunity to communicate messages to consumers at any time of the day. However, due also to their seamless integration into people’s everyday life, such message communications are particularly prone to be perceived as highly intrusive and are likely to cause annoyance when they are deemed irrelevant [96]. Thus, a critical issue to unleash mobile capabilities is to communicate mobile messages in ways that are consistent with people’s needs and preferences. To this end, time being a pervasive component of everyday life [85] plays an important role, especially given the regularities uncovered in how people’s psychological states vary by different times of a day [43, 90, 102]. Focusing on mobile Internet service as an important class of IT, this study posits that highlighting the utilitarian or hedonic value of the IT service according to different times of day can yield better user response in terms of their purchase adoption.

With both field experiment and field survey, this research provides consistent evidence for the distinct temporal patterns in user response to the mobile Internet service offer. Specifically, we find that mobile targeting with utilitarian product value appeal should be employed in the morning hours, whereas mobile targeting with hedonic product value appeal of the same product should be employed in the afternoon hours. Our use of the same product with different mobile communication content permits meaningful direct comparison of response rates. An additional analysis shows that the optimal strategy should leverage utilitarian value appeal from 8:00 am to 12:00 pm and hedonic framing for the remaining hours of the day. This strategy would produce an average purchase rate of 15 percent, which almost doubles the current industry practice of using utilitarian-only content in all hours. Specifically, current industry practices largely focus on the utilitarian product value in mobile promotions [21, 29, 72, 95], which receives 8.7 percent purchase rate. The findings offer several important implications for research and practice as discussed in the following section.

#### Theoretical Implications

This research contributes to theory primarily in two ways. First, this study advances the notion that time of day is an important contextual element that influences the adoption of some types of ITs, such as mobile Internet service that can provide both utilitarian and hedonic values. A review of the IS literature (Table A1 in Online Appendix A) shows that some efforts have been taken to understand the role of time in IS research in the recent decade. However, most of the extant studies have considered time in terms of its duration, such as the time duration over which an IT has been used or implemented (e.g., Fuller and Dennis [39], Ko and Dennis [61], Williams and Pollack [101], Zahedi and Song [107]). This is consistent with the notion of time scale in the organization research [108], such as the time interval over which researchers conduct their observations on a phenomenon (e.g., IT use or implementation). Some attention has also been put on time difference, especially in research on virtual teams of which their members are typically geographically dispersed in different time zones (e.g., Cummings et al. [24] and Sarker et al. [84]). A minimal amount of attention has been put on time as a contextual factor in people’s everyday interaction with a technology. As Yoo [106] notes, it is important to consider how such a time dimension shapes the prevalent digitally mediated “embodied experiences” in our everyday activities through ITs today. Our study that unveils users’ different tendency to adopt a technology in different times of a day may serve to enrich our understanding of the relationships between ITs and time along this under-explored direction. Our findings suggest that inves

# Audit 05: Cost-Effective Quality Assurance in Crowd Labeling

- Group: `retained_layer:hybrid`
- Model decision: `True`; centrality `exclusive`; layer `hybrid`
- Gates: `{"purposeful_solution_design": true, "objective_metric_is_primary_target": true, "comparative_improvement_demonstrated": true, "objective_improvement_is_the_success_basis": true}`
- Model reason: 文章设计并实质改进了众包标注质量保障方案：提出多种动态标签分配算法、推断算法和基于价值的工人绩效度量，并以平均误分类成本、标签成本和工人保留等客观指标作为主要成功标准；通过模拟、真实数据集和现场实验与 GRR/NLU/固定费率等基准比较，展示了明确且大幅度的客观改进。四道门全部通过，且客观指标为中心，因此保留。
- Source: `E:\github\qual-llm-check-IS-utd\database_fulltext_all\00764_2017_cost-effective-quality-assurance-in-crowd-labeling.md`

#### 1. Introduction

Crowdsourcing has emerged over the last few years as an important new labor pool for a variety of tasks (Malone et al. 2009), ranging from microtasks posted on platforms like Amazon Mechanical Turk<sup>1</sup> (AMT) to big innovation contests conducted by Netflix<sup>2</sup> and Innocentive.<sup>3</sup> Today, AMT, in particular, dominates the market for crowdsourcing microtasks, which are easy for humans to accomplish but remain challenging for computers (Ipeirotis 2010). The employers on AMT can post a variety of small tasks, such as image tagging, sentiment judgment, language translation, and text annotation. Workers complete these tasks and get compensated in the form of micropayments, typically in the range of 5 to 20 cents per task. The immediate and elastic supply of cheap labor in microcrowdsourcing systems makes it possible to complete tasks at low cost and with high throughput.

Firms, ranging from Fortune 500 companies to small start-ups, are increasingly attracted to microcrowdsourcing to meet their business needs. Amazon has been using micro-crowdsourcing for more than 10 years to deduplicate products in catalogs uploaded to its platform by merchants. Microsoft has built the Universal Human Relevance System (UHRS) to evaluate and improve the performance of its search engine—Bing. Facebook has been relying on microcrowdsourcing for content moderation, and Twitter is using AMT to improve its real-time event detection accuracy. Many other companies employ microcrowdsourcing either directly or through an intermediary (e.g., AMT, CrowdFlower, CrowdSource).

Micro-crowdsourcing platforms are also increasingly used by information systems (IS) researchers for a wide variety of data labeling and annotation tasks. To study the impact of review text on product sales, Archak et al. (2011) recruited workers from AMT to extract product features and opinions about these features from the text of product reviews. Moreno and Terwiesch (2014) used AMT workers to code the sentiment of comments left by previous service buyers as either positive or negative and constructed a reputation measure for service providers based on this information. Wang et al. (2012) also relied on the AMT platform to obtain a reliable measure of the perceived helpfulness of user-generated reviews.

Despite the promise, significant challenges remain. Workers in microtask crowdsourcing markets usually have diferent levels of expertise and dedication and thus exhibit heterogeneous quality 

#### 2.2. Worker Performance Metrics

All of the above inference algorithms generate some indicators of worker performance in scalar, vector, or matrix form. For example, MV measures the accuracy rate of each worker by the proportion of the labels submitted by the worker in agreement with the majority labels. The EM algorithm proposed by Dawid and Skene (1979) returns a confusion matrix, which lists the probabilities of diferent classification errors made by each worker. Welinder et al. (2010) measure worker ability in a multidimensional space, with each element modeling the worker’s individual weight on each of the major components of the annotation task. Karger et al. (2011) use a set of task-specific worker messages to represent the belief of how reliable a worker is in labeling each specific task. Whitehill et al. (2009) employ a scalar value to model the expertise of each worker.

However, none of these metrics can efectively quantify the contributed value of each label provided by an individual worker in meeting the quality assurance needs of the employer. First, they cannot separate correctable errors from uncorrectable errors that workers make. For example, a malicious worker may always submit wrong labels, but these labels are informative, as they can be reversed to uncover the truth. In such cases, the naïve measurement of accuracy rate results in an underestimate of the value of workers who consistently give predictably incorrect answers. Second, they fail to take into account the relative costs of diferent types of classification errors. Understandably, some types of misclassification errors incur significantly higher costs than others. For example, allowing a porn image to pass a moderation filter is often more costly than blocking a legitimate image incorrectly. Third, a number of workers often need to work in tandem to generate labels of acceptable quality; therefore, it is more appropriate to evaluate the performance of each worker in a multiple-label setting than treating them as isolated. In our work, we propose a value-based performance metric that directly measures the monetary contribution of each worker in a multiple-label setting, after fixing correctable worker errors and accounting for heterogeneity in misclassification costs across diferent types of classification errors.

#### 6. Simulation Experiments

To test the performance of the inference and label allocation strategies, we run a set of simulation experiments using synthetic data generated by the labeling model described in Section 3.2. Simulation experiments are a powerful tool for modeling complicated market environments and conducting analyses under various parameter values $( \mathrm { e . g . }$ , Chiang and Mookerjee 2004, Adomavicius et al. 2009, Ketter et al. 2012). We describe below the setting for the simulations.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 5 (A general framework for dynamic label allocation)

Input: The set of objects $O = \{(o)\}$ to be labeled, misclassification cost matrix $\mathbf{c}$, cost threshold $\tau_c$, heuristic function $h^{(o)} \in \{h_{MP\text{-Reliab}}^{(o)}, h_{EM\text{-Cost}}^{(o)}, h_{GLAD\text{-Cost}}^{(o)}, h_{GLAD\text{-CostV}}^{(o)}\}$, inference and cost estimation algorithm $\eta \in \{EM, GLAD\}$

Output: Predicted class label $\hat{t}^{(o)}$ for each object ($o$)

1 Initialize $L = \emptyset$, $O^{(k)} = \emptyset$ for each worker ($k$), $avg\_cost = \infty$;

2 while $avg\_cost &gt; \tau_c$ do

3 When a worker ($k$) is ready to accept the next task,

4 Select the next object to label according to ($o$) = $\arg \max_{(o') \in O \setminus O^{(k)}} h^{(o')}$;

5 Once worker ($k$) finishes the task,

6 Add the acquired label $l_{(o)}^{(k)}$ to the label set: $L = L \cup \{l_{(o)}^{(k)}\}$;

7 Add object ($o$) to the set of objects labeled by worker ($k$): $O^{(k)} = O^{(k)} \cup \{(o)\}$;

8 Using algorithm $\eta$, estimate the class probability estimates $\mathbf{p}^{(o)}$ for each object ($o$);

9 sum_cost = 0;

10 for ($o$) ∈ $O$ do

11 Calculate the predicted label $\hat{t}^{(o)}$ and the estimated misclassification cost $EstCost^{(o)}$:

12 $\hat{t}^{(o)} = \arg \min_{j \in \{0,1\}} \sum_{i=0}^{1} p_i^{(o)} c_{ij}$;

13 $EstCost^{(o)} = \min_{j \in \{0,1\}} \sum_{i=0}^{1} p_i^{(o)} c_{ij}$;

14 sum_cost = sum_cost + EstCost$^{(o)}$;

15 end

16 $avg\_cost = \frac{sum\_cost}{|O|}$

17 end
</div>

The simulation setup is as follows: We have 1,000 objects evenly assigned to two classes. The easiness of each object $\beta ^ { ( o ) }$ is obtained by exponentiating a draw from a normal distribution ${ \dot { \mathcal { N } } } ( 0 , 1 { \dot { ) } } .$ . There are 200 workers whose quality parameters $\{ \grave { \alpha } _ { 0 } ^ { ( k ) } \}$ and $\{ \alpha _ { 1 } ^ { ( k ) } \}$ are drawn from

#### 7. Experiments on Real-World Crowdsourced Data Sets

One drawback of using simulation is that the underlying label generation model is artificial, which is unlikely to hold in real-world settings. For example, the generation of labels may not follow a specific model; the errors workers make might be correlated. For further evaluation, we test the performance of the proposed approaches on three publicly available data sets obtained using AMT. The first bluebird data set is collected by Welinder et al. (2010), in which workers are asked whether the presented image contains Indigo Bunting or Blue Grosbeak. The second rte data set and the third temp data set are both natural language processing data sets collected by Snow et al. (2008): rte represents the recognizing textual entailment task, where workers are presented with two sentences and given a binary choice of whether the second hypothesis sentence can be inferred from the first; temp represents the event temporal annotation task, where workers are presented with a dialogue and a pair of verb events from the dialogue, and asked whether the event described by the first verb occurs before or after the second. Table 2 summarizes these three data sets.

All three data sets in Table 2 are collected in a static way, regardless of the labels acquired at each intermediate step. At the end of the data collection, all of the objects receive the same number of labels. To simulate the dynamic label acquisition, we acquire labels in the following way:<sup>10</sup> At each step, we first pick a worker from the set of workers who still have labels, with the probability of being picked proportional to the number of available labels per worker; then, we choose the next object to label based on the dynamic allocation strategies proposed in Section 5, with the constraint that the object must have been labeled by the chosen worker; next, we put the assigned label to the observed label set, and remove it from the label pool available for drawing. We consider two cost settings $\mathbf { c } ^ { ( a ) }$ and $\mathbf { c } ^ { ( b ) }$ and average the results over 20 experimental runs.

Table 2. Description of the Three Real-World Data Sets

<table><tr><td>Data set</td><td>No. of objects(positive/negative)</td><td>No. ofworkers</td><td>No. of labelsper object</td><td>Mean/Medianno. of labelsper worker</td></tr><tr><td>bluebird</td><td>108 (60/48)</td><td>39</td><td>39</td><td>108/108</td></tr><tr><td>rte</td><td>800 (400/400)</td><td>164</td><td>10</td><td>49/20</td></tr><tr><t

#### 8. Generating Reliable Worker Performance Metrics

In Online Appendix D.2, we leverage the advantage of simulated data to check the accuracy of worker quality estimation by calculating the Spearman coeficient between workers’ true quality values and the estimated quality values using diferent inference algorithms. 12 The results show that both EM and GLAD achieve a fairly high level of accuracy and can be used as efective tools for evaluating worker quality. Unfortunately, neither the confusion matrix $\mathbf { e } ^ { ( k ) ^ { \ J } }$ returned by EM nor the quality vector $\hat { \alpha } ^ { ( k ) }$ returned by GLAD is a scalar, and therefore cannot be directly used to rank worker performance. Here, we introduce two scalar metrics of worker performance: one is based on the estimated misclassification cost of a worker’s label in single labeling (Section 8.2), and the other is based on the contributed value of a worker’s label in multiple labeling (Section 8.3).

#### 9. Conclusions and Discussion

Crowd labeling has rapidly become a commonly used tool for companies and researchers to acquire a huge number of cheap labels. However, such nonexpert labels are often noisy and unreliable, and employers need to rely on redundancy to achieve a desired level of quality, which significantly increases the total labeling expense. Therefore, devising cost-efective label acquisition strategies and establishing reliable worker performance metrics are of substantial interest to decision makers.

The contribution of this paper is twofold: First, we formulate a dynamic decision system in which label allocation and inference occur simultaneously, and propose several adaptive label allocation strategies that prioritize labels on objects that are more likely to yield higher rewards for employers. We demonstrate the superior performance of the proposed strategies over alternative approaches via extensive experiments on both simulated and real-world data sets. Second, we introduce two novel metrics that can be used to objectively rank the performance of crowdsourced workers, both allowing employers to separate workers’ correctable errors from uncorrectable errors and incorporate unequal costs of diferent types of classification errors. In particular, the contributed value metric directly measures worker’s individual contribution in quality assurance through redundancy and provides a basis for employers to develop more fair and eficient compensation schemes. As illustrated further in Online Appendix A, our work may serve as a fundamental quality control block for a variety of tasks, ensuring that the outcome of crowdsourced production reaches the quality levels desired by employers.

Although we focus on binary labeling tasks in this paper, most of our adaptive label allocation strategies can be generalized to multiclass settings.<sup>21</sup> The EM-Cost strategy can be directly applied to multiclass settings by (1) representing the performance of each worker by a multidimensional confusion matrix; (2) obtaining the class probability estimates for each object using the EM inference algorithm; and (3) estimating the misclassification cost based on the class probability estimates and a multidimensional cost matrix specified by the employer. To generalize GLAD-Cost and GLAD-CostV to multiclass scenarios, we can use a multidimensional vector to represent worker quality and a numeric value to represent object easiness. In the GLAD inference algorithm, the logistic function that jointly incorporates the class-dependent quality of the worker and the easiness of the object only gives the probability of obtaining the correct label. We need to make some simplification (e.g., assuming labeling errors are equally distributed across classes other than the correct one) to obtain the probability distribution over incorrect classes,<sup>22</sup> and then calculate the misclassification cost and the cost variation. Furthermore, the two worker performance metrics—estimated cost metric and contributed value metric—introduced in this paper can be readily used in multiclass settings by following the same procedure as described in Algorithms 6 and 7.

#### 9.1. Practical Implications

Despite the wide adoption of micro-crowdsourcing by various companies, quality assurance at minimal cost remains an issue yet to be explored. Many of today’s firms still operate on a static system in which a fixed number of labels are collected for each object first, and some aggregation method is then employed to infer the true classes of objects. However, the real-world crowd labeling system is inherently dynamic, which provides an opportunity for companies to allocate labels adaptively and eficiently so that the target data quality can be achieved at considerably less expense. As illustrated in previous experiments, compared with the nonadaptive scheme, our proposed label allocation strategies can reduce the labeling expense by 15%–50%. For big companies (e.g., Facebook, Twitter) that require tons of hum

# Audit 06: A decision support system for planning and coordination of hybrid renewable energy systems

- Group: `retained_layer:hybrid`
- Model decision: `True`; centrality `exclusive`; layer `hybrid`
- Gates: `{"purposeful_solution_design": true, "objective_metric_is_primary_target": true, "comparative_improvement_demonstrated": true, "objective_improvement_is_the_success_basis": true}`
- Model reason: 该文设计了一个IS相关的决策支持系统及内嵌的随机优化模型和MSA启发式算法；核心成功标准是客观的期望总成本最小化，且在第5节通过18个模拟场景将MSA与SAN、MNM比较，证明其在最优解差距指标上一致更优。全文没有依赖主观满意度、感知有用性等构念来判断方案是否成功，因此四个门全部通过，客观指标改进是唯一或主导的成功依据。
- Source: `E:\github\qual-llm-check-IS-utd\database_fulltext_all\15986_2014_a-decision-support-system-for-planning-and-coordination-of-hybrid-renewable-energy-systems.md`

#### 1. Introduction

With the United Nations predicting the world population growth from 6.6 billions in 2007 to 8.2 billions by 2030, demand for energy is expected to grow in an increasing speed over that period. According to [28], renewable energy sources, such as hydropower, solar and wind energies, only account for 19% of the total world energy demand in 2013. Renewable energies are green and clean resources. They are non-depletable, non-polluting and have minimal environmental and health impacts compared to fossil fuels. It has been long recognized that excessive fossil fuel consumption can lead to signi<sup>fi</sup>cant adverse impact on the environment through super<sup>fl</sup>uous carbon emissions, and in turn cause global climate change. While renewable energies are gaining more popularity over the decades, many countries are still resistant to increase the usage of the renewable energy, especially for the developing countries that are in dire need of power to sustain their economic growth. This is mainly due to the undesirable characteristics of renewable energies—their power supply is highly volatile and unpredictable; heavily relying on renewable energies is likely to result in instable power supply and could harm the economy.

Many countries are thus looking for other alternatives. Hybrid renewable energy system (HRES), which refers to a combination of at least one renewable energy source and a conventional power generator, is one viable and attractive choice that allows for the advantages of the renewable energies, while eliminating their disadvantages [7]. The HRES essentially utilizes renewable energies to ful<sup>fi</sup>ll the power demand and, if the power supply from the renewable energy sources is not suf<sup>fi</sup>cient, the conventional power generator is used to cover the power shortage, in turn ensuring that all power demand can be satis-<sup>fi</sup>ed. In fact, HRES has received a great deal of attention over the decade, not only because it is more environmental friendly, but also because it provides an excellent solution for electri<sup>fi</sup>cation of remote rural areas, where the grid extension is either dif<sup>fi</sup>cult or uneconomical.

Although HRES is attractive in many aspects, the planning and coordination of HRES so as to ful<sup>fi</sup>ll the power demand are very challenging. This is attributable to the unknown power demand of each area distributed in a wide region, the highly volatile renewable power supply over time, and the c

#### 4. Solution methodology

In this section, we develop an ef<sup>fi</sup>cient heuristic to solve the proposed model and obtain the optimal number of solar and wind power generators. The developed methodology, called metamodel-based simulated annealing (MSA), is a simulation optimization method. It possesses the basic framework of the traditional simulated annealing (SAN) [32], but is further adapted by incorporating a Monte Carlo approach, along with a sample size scheme, to enable quality estimation of the objective function, and a metamodel-based search strategy to accelerate the algorithm convergence.

The traditional SAN is a random-search-based algorithm developed based on an observation of the cooling process of a liquid or solid in which molecules have higher mobility at high temperatures and the mobility is lost or declines as the temperature decreases. This concept has been successfully applied in deterministic optimization to <sup>fi</sup>nd the lowest (or highest) value of the objective function. However, one disadvantage of SAN is that because it randomly selects a solution at each iteration, it may require an excessive number of iterations to <sup>fi</sup>nd the true optimal solution, especially when the parameter space is very large. For example, if a problem has 20 decision variables, and the value of each decision variable can vary from 1 to 50, it could take $5 0 ^ { 2 0 }$ iterations to <sup>fi</sup>nd the true optimal solution. The proposed MSA addresses this issue by using a metamodel-based search strategy, which basically builds a metamodel to represent the functional behavior of the objective function and solves for the optimal solution of the built metamodel, subject to the experimental design. Because MSA explores a region of the parameter space, rather than one point, at a time, the optimal solution can be located in a more ef<sup>fi</sup>cient manner.

#### 4.2. Metamodel-based simulated annealing method

The central idea that MSA capitalizes on building metamodels to represent the objective function within the experimental region and then performing optimization in light of the built metamodel, which is either a <sup>fi</sup>rst- or second-order polynomial function. Let the current best solution be $\mathbf { x } _ { k } = [ x _ { s 1 } , . . . , x _ { s M } , x _ { w 1 } , . . . , x _ { w M } ]$ . For each iteration, the experimental region is de<sup>fi</sup>ned as

$$
B (\mathbf {x} _ {k}, \Delta) = \left\{\mathbf {x} \in \mathbb {R} ^ {p}: \| \mathbf {x} - \mathbf {x} _ {k} \| \leq \Delta \right\},\tag{8}
$$

where $| | \cdot | |$ denotes the Euclidian norm and $\Delta > 0$ is the radius of the experimental region.

The full MSA method is given as follows.

• Step 0. Set the iteration counter $k = 0 .$ . Select an initial temperature $T _ { 0 } ,$ cooling coef<sup>fi</sup>cient $\rho ,$ size of experimental region $\Delta ,$ and an initial solution $\mathrm { X } _ { 0 } .$

• Step 1. Build a metamodel to represent the objective function within the experimental region (Section 4.2.1).

Please cite this article as: K.-H. Chang, A decision support system for planning and coordination of hybrid renewable energy systems, Decision Support Systems (2014), http://dx.doi.org/10.1016/j.dss.2014.04.001

• Step 2. Solve for the optimal solution of the metamodel subject to the experimental region x<sup>∗</sup> (Section 4.2.2).

• Step 3. Obtain estimates $\hat { Y } _ { k }$ and $\hat { Y } _ { k } ^ { * }$ for $\operatorname { E } [ G ( \mathbf { x } _ { k } , \omega ) ]$ and $\operatorname { E } [ G ( \mathbf { x } _ { k } ^ { * } , \omega ) ]$ respectively.

• Step 4. If $\hat { Y } _ { k } - \hat { Y } _ { k } ^ { * } { > } 0$ , accept $\mathbf { x } _ { k } ^ { * }$ and let $\mathbf { x } _ { k + 1 } = \mathbf { x } _ { k } ^ { * } .$ Otherwise, use the Metropolis criterion to determine whether to accept x<sup>∗</sup>. If x<sup>∗</sup> is accepted, let $\mathbf { x } _ { k + 1 } = \mathbf { x } _ { k } ^ { * }$ and go to Step 7. Otherwise, go to Step 6.

• Step 5. Randomly select a solution x<sup>∗</sup> in the parameter space. Follow Steps 3 and 4 to estimate $\hat { Y } _ { k } ^ { * } .$ . If $\hat { Y } _ { k } - \hat { Y } _ { k } ^ { * } > 0$ , accept x<sup>∗</sup> and let ${ \bf x } _ { k + 1 } =$ $\mathbf { x } _ { k } ^ { * } .$ Otherwise, use the Metropolis criterion to determine whether to accept x<sup>∗</sup>. If x<sup>∗</sup> is accepted, let $\ma

#### 5. Numerical experiments

In this section, we conduct a numerical study to understand the effectiveness and ef<sup>fi</sup>ciency of MSA. We use an array of simulated problems to compare the performance of MSA, SAN and the modi<sup>fi</sup>ed

[image omitted]  
Fig. 6. Sensitivity analysis of the DSS. (For interpretation of the references to color in this figure the reader is referred to the web version of this article.)

Nelder–Mead (MNM) method [5], which is one popular metaheuristic designed for simulation optimization problems.

Speci<sup>fi</sup>cally, 18 scenarios, constituted by 3 types of test functions, 3 types of dimensions, and 2 types of variance settings are created. The test problem is composed of a deterministic function with added noise, i.e., $G ( \mathbf { x } , \omega ) = g ( \mathbf { x } ) + \epsilon _ { x } .$ . Speci<sup>fi</sup>cally, for each test problem, three types of dimensions are considered: 4D, 12D and 16D, which correspond to low-, moderate-, and high-dimensional problems respectively. The added noise $\epsilon _ { x }$ is generated from $\mathcal { N } ( 0 , \sigma ^ { 2 } ( \mathbf { x } ) )$ with two types of variances: <sup>fi</sup>xed $( \sigma ( { \bf x } ) = 1 0 )$ and varying $( \sigma ( { \bf x } ) = 0 . 5 { \cdot } g ( { \bf x } ) )$ Note that in the latter setting, when the initial solution is selected far from the true optima, the function value g(x) will be large, making the response variable grossly noisy. This allows us to test the stability of algorithms.

The performance measure for comparison purposes is de<sup>fi</sup>ned a

$$
\log (g (\mathbf {x} _ {k} ^ {*}) - g ^ {*} + 1),\tag{14}
$$

where x<sup>∗</sup> and $g ^ { * }$ correspond to the best solution found when the algorithm is terminated and the true globally optimal function value, respectively. Eq. (14) refers to the gap of function values between the <sup>fi</sup>nal solution and the true optimum.

The test functions, g(x), are selected from literature in nonlinear optimization [24] and are considered dif<sup>fi</sup>cult even in deterministic settings. Speci<sup>fi</sup>cally, the <sup>fi</sup>rst type is the extended Rosenbrock function (ER),

$$
g (\mathbf {x}) = \sum_ {i = 1} ^ {p - 1} \left[ 1 0 0 \left(x _ {i} - x _ {i + 1} ^ {2}\right) ^ {2} + (1 - x _ {i}) ^ {2} \right],\tag{15}
$$

which is a multimodal function when $p \ge 4 \left[ 3 1 \right]$ . The second type is the Freudenstein and Roth function (FR),

$$
\begin{array}{l} g (\mathbf {x}) = \sum_ {i = 1} ^ {p

#### 6.2. Output results

With the input parameters given in Fig. 4, the main model can be solved and the result is shown in “Output Results.” In Fig. 5, the Generator Bar Graph on the left and upper corners provides the information about how many solar and wind power generators are required for each of the three power stations, where the blue, green, and red parts represent the power station 1, 2 and 3, respectively. The total number of solar and wind power generators for all the three power stations is 95 and 126, respectively and the total cost is 1210.2. Also, the “Cost Pie Chart” shows the fraction of power generation cost by solar, wind and conventional power generators. Finally, the “Cost Bar Chart” shows the cost associated with the equipment installation cost and the conventional power generation cost, respectively.

[image omitted]  
Fig. 9. Power generation, allocation and transmission of the DSS (part III).

#### 6.3. Sensitivity analysis

“Sensitivity Analysis” shows how the total cost and the optimal number of solar and wind power generators would change when one parameter of the model varies. In Fig. 6, the red portion represents the extra number of solar and wind power generators needed when the variance of power demand of each area is changed to 4.

#### 7. Conclusions

In this paper, we study the planning and coordination of HRES and propose a model to characterize the determination of the optimal number of solar and wind power generators of HRES in uncertain environments. The goal is to achieve the minimum total cost, while satisfying the power demand of each area. To solve the model, a simulation optimization method, MSA, coupled with a Monte Carlo simulation approach, is proposed. In particular, the MSA method is based on the traditional simulated annealing method, but is further adapted by incorporating a metamodel-based search strategy to accelerate the algorithm convergence. Numerical results show that in comparison with the existing methods, the proposed MSA can have superior convergence performance under the same computational budget. Finally, a decision support system (DSS) integrating the proposed model and the solution methodology is developed as an ef<sup>fi</sup>cient decision tool to enable effective and ef<sup>fi</sup>cient energy management of HRES. The visualized outputs of DSS allow decision makers to gain better understanding about the management of HRES, facilitating the decision making process.

Some future work is described as follows. First, when there is only limited historical data, it can be dif<sup>fi</sup>cult to specify the distribution of the power demand of each area and that of the renewable power supply of each power station. In this case, the decision model should account for the distribution ambiguity existing in the randomness. Second, the proposed Monte Carlo simulation method may require an excessive amount of time for generating one observation for estimating the additional power generation cost and the power storage cost, especially when the problem is of large scale, namely, the number of power stations and demand areas is large. A more ef<sup>fi</sup>cient approach should be developed to overcome the dif<sup>fi</sup>culty.


# Audit 07: An empirical study of web site navigation structures' impacts on web site usability

- Group: `retained_layer:interface_or_interaction_design`
- Model decision: `True`; centrality `dominant`; layer `interface_or_interaction_design`
- Gates: `{"purposeful_solution_design": true, "objective_metric_is_primary_target": true, "comparative_improvement_demonstrated": true, "objective_improvement_is_the_success_basis": true}`
- Model reason: 该文设计并构建了三种具有不同导航结构的 Web 站点（有目的的 IS 设计）；其核心成功标准是客观绩效指标 CAR 和 NT，并明确说明研究聚焦于绩效而非感知；两轮受控实验均展示了 usage-oriented 与 combined hierarchy 相对 subject-oriented hierarchy 在客观指标上的显著改进；感知测量是次要的，且第一轮不显著并不影响结论，因此客观绩效改进是主导的成功依据。四个门全部通过，centrality 判定为 dominant。
- Source: `E:\github\qual-llm-check-IS-utd\database_fulltext_all\12792_2007_an-empirical-study-of-web-site-navigation-structures-impacts-on-web-site-usability.md`

#### Abstract

Web sites are intended to facilitate knowledge acquisition, often in the interest of supporting decision making. Based on a taxonomy of factors influencing Web site usability, hypotheses are developed about usability of alternative navigation structures. These hypotheses are tested via experiments that measure user performance in accomplishing knowledge acquisition tasks and user perceptions of usability. Two rounds of experimentation are performed for both simple and relatively complex task sets. Results show that a usage-oriented hierarchy or a combined hierarchy is a navigation structure associated with significantly higher usabilit than subject-oriented hierarchies, for both simple and relatively complex knowledge acquisition tasks. © 2006 Elsevier B.V. All rights reserved.

Keywords: Experiment; Knowledge acquisition; Navigation structure; Web site design; Web site usability

#### 1. Introduction

A primary function of Web sites is to serve as a means for both the providers and the users of those sites to acquire knowledge [12]. Organizations recognize the importance of the Web as a conduit for acquiring knowledge about customers, competitors, and partners. They provide Web sites that aim to facilitate Web users' acquisition of knowledge about their organizations' activities, archives, products, and services. Thus, it is important for the provider of a Web site to ensure that it is developed in a way that provides a high degree of usability to those who seek to acquire knowledge through it.

Web sites are not always as successful or as usable as they could be. Web site users can encounter various problems when trying to acquire knowledge from a Web site and trying to use a Web site's functionalities. This leads to dissatisfaction with Web sites and blockage in knowledge acquisition (KA). Although one can find many tips for Web site design [45,31,35], the research literature holds little in the way of well-substantiated prescriptions for designing Web sites, such as what navigation structures are appropriate for facilitating KA in various circumstances. Thus, there is a need for research that explores Web-based KA in the sense of how to allow it to be accomplished with great usability.

Designing a Web site that is highly usable for acquiring knowledge is not a trivial undertaking. Five classes of features have been identified as joint contributors to Web site usability: task features, user features, provider features, system features, and environment features [12],

Table 1 Prior navigation structure research

which are further explained later in Section 2.2. Of these, system features are the most controllable. For a given provider aiming to facilitate the KA activities of certain kinds of users engaged in certain kinds of tasks and operating within a given environment, what system features can be designed into a Web site to enhance its KA usability? The research described here facilitates to answer this question with respect to alternative navigation structures that can be designed into a Web site. It considers usability of this system feature from the objective standpoint of user performance, as well as the standpoint of users' subjective perceptions.

A large-scale survey conducted by Georgia Tech's Graphics Visibility Usability (GVU) Center has found that the top three uses of the Web are information gathering, searching, and browsing. All three

#### 4. Constructing the experimental platform, web sites, and task sets

The experimental platform is devised to administer experimental sessions in which a user interacts with a Web site in order to acquire knowledge needed to perform online tasks. The platform presents a task, records a user's behavior in using a Web site to help accomplish the task, records the task outcome that the user produces, and then repeats this cycle with successive tasks. In the present study, the experimental platform is equipped with three distinct Web sites presenting knowledge about the domain of POM. Although each site has the same Web objects, they differ in terms of navigation structure: one being a subject-oriented hierarchy, another being a usage-oriented hierarchy, and a third providing a navigation structure that combines the former two. In this study, the experimental platform is equipped with two distinct sets of tasks which we call simple and complex. Designs of the three Web sites and two task sets are discussed below.

[image omitted]  
Fig. 2. Opening page for combined hierarchy.

The platform allows each experimental subject to have access to exactly one of the three sites, where site assignments are randomly determined based on his/her ID number. Similarly, each subject is randomly assigned to one of the two task sets. The platform presents a subject with tasks from the assigned task set. Each task takes the form of a question pertaining to the POM domain. For each task, the subject uses the assigned Web site's navigation structure in an effort to acquire knowledge needed to answer the presented question. Behind the scenes, the platform tracks the navigation time and records the subject's answers for subsequent analysis.

#### 5. Execution of the experiment



#### 5.3. Experimental procedures

To execute a round in the experiment, an announcement of the round was circulated among all students in the course. To elicit subjects' best efforts, volunteers were offered two types of incentives: course extra credit and cash prizes for top performers in each cell.

When subjects arrive at the lab, a researcher distributes a handout to each subject. The first page of the handout is a demographic questionnaire. The second page contains instructions for doing the experiment. The third page is a post-experiment questionnaire designed for capturing subjects' perceptions about site usability. The researcher gives a brief introduction to each page of the handout, and performs a demonstration to acquaint subjects with using the platform (such as how to input an ID number, get a task, acquire knowledge for a task's answer, type an answer, edit or clear an answer, and so forth).

In particular, the researcher tells the subjects that the rules on the instruction page must be followed. Failure to follow the rules will result in discarding a subject's data input and elimination from cash prize consideration. Throughout each session, the researcher stays in the lab, ensuring that subjects do nothing that may cause biased and false results (such as collaborating, interrupting other subjects, and resorting to other approaches for finding the correct answers).

A subject fills out the demographic questionnaire first, then reads the instruction page, performs two practice tasks, performs the assigned set of online tasks, and finally completes the perception questionnaire. The practice tasks are not counted for performance evaluation. The finished demographic and post-experiment questionnaires are turned into the researcher.

#### 6. Data analysis results



#### 6.1. Results from round one

Even though subjects are randomly assigned to each of the experimental cells, we are interested in assessing whether demographic data across experiment cells are uniform and similar. Critics may argue that random assignment cannot guarantee that subjects' demographic backgrounds across cells are identical. Results of a Chisquare analysis reveal no statistically significant differences in subjects' demographic backgrounds across six experiment cells at an alpha level of 0.01.

Before comparing any individual cells regarding usability differences, we run MANOVA (Multivariate Analysis of Variance) on performance data from all the cells. Particularly, we are interested in assessing the navigation structure main effect, the task main effect, and the interaction between them. Similarly, we perform a second MANOVA on the perception data in round one to assess navigation structure, task, and interaction effects. Table 6 shows the cell-wise averages for all usability performance and perception measures.

Using the correct answer ratio (CAR) and navigation time (NT) as dependent variables, the MANOVA across all the experimental cells shows significant navigation structure main effects and task main effects. However, the interaction between navigation structure and task complexity is not significant at a 0.05 level (Table 8). In terms of site main effects, the CAR for the usageoriented hierarchy is 6% higher than the CAR for the subject-oriented hierarchy. The CAR for the combined hierarchy is 10% higher than the CAR of subjectoriented hierarchy. The navigation time for the subjectoriented hierarchy is 52 s higher than the NT for the usage-oriented hierarchy, and 36 s higher than NT for the combined hierarchy. As for task main effects, the CAR for the simple tasks is 19.5% higher than the CAR for the complex tasks. The NT for complex tasks is 46 s higher than the NT for simple tasks.

The statistically significant results for CAR are as follows: both usage-oriented hierarchy and combined hierarchy are more usable than subject-oriented hierarchy. For navigation time, statistically significant results are that both usage-oriented hierarchy and combined hierarchy are more usable than subject-oriented hierarchy. Thus, for both usability measures, usage-oriented hierarchy and combined hierarchy navigation structures are superior to the subject-oriented hierarchy.

MANOVA statistics for experiment round one

<table><tr><td>Measure</td><td>Navigation structure main effect</

#### 6.2. Results from round two

In the subsequent semester, the experiment was repeated for the purpose of confirming the results obtained from round one. This second round was conducted with the participation of 99 subjects. Chisquare analysis indicates that there are no statistically significant demographic differences between the subjects in round one and round two. Neither is there any statistically significant demographic difference across the six experimental cells within round two.

Using the correct answer ratio (CAR) and navigation time (NT) as dependent variables, MANOVA again shows statistically significant navigation structure main effects and task main effects. As in the case of round one, the interaction between navigation structure and task type is not statistically significant at a 0.05 level (Table 9).

In terms of site main effects, the CAR for the usageoriented hierarchy is 9% higher than CAR for the subject-oriented hierarchy. The CAR for the combined hierarchy is 7% higher than CAR for subject-oriented hierarchy. The NT for the subject-oriented hierarchy is 25.0 s higher than the NT for the usage-oriented hierarchy, and 16.4 s higher than the NT for the combined hierarchy. As for task main effects, the CAR for the simple tasks is 17.2% higher than the CAR for the complex tasks. The NT for complex tasks is 30.7 s higher than the NT for simple tasks. Similar to the results from round one, the usage-oriented hierarchy and combined hierarchy navigation structures, for the second time, are statistically significantly more usable than subject-oriented hierarchy, in terms of both CAR and NT performance measures.

Table 9  
MANOVA statistics in experiment round two

<table><tr><td>Measure</td><td>Navigation structure main effect</td><td>Task main effects</td><td>Navigation and task interaction</td></tr><tr><td>Performance</td><td> $F=3.05, p=0.0184$ </td><td> $F=23.64, p<0.001$ </td><td> $F=0.74, p=ns$ </td></tr><tr><td>Perception</td><td> $F=3.50, p=0.0009$ </td><td> $F=1.41, p=ns$ </td><td> $F=0.67, p=ns$ </td></tr></table>

Using the four perception questions as dependent variables, the MANOVA results for round two show that navigation structure main effects are significant, which is different from the results in round one. Yet, again, task main effects and the interaction between navigation structure and task are not significant (Table 9). In particular, compared to those using the subject-oriented hierarchy, subjects using usage-oriented and combined hierarchies rate th

#### 7. Discussion



#### 7.1. Explanation for the findings

Mental model and schema theories offer insights that can help understand the results of this exploratory experiment. In experimental results from both rounds it turns out that the subject-oriented hierarchy was less usable than the combined hierarchy in terms of user performance. An interpretation is that the positive effects from including a usage-oriented hierarchy in a network are so strong that it not only counteracts negative effects from having more options (both in terms of semantics and syntax), but also yields some additional positive performance effects.

MANOVA results for perception data in the first round showed no significant navigation structure main effects. However, MANOVA results for the second round showed significant main effects for navigation structure (pointing out the vulnerability of relying on findings from a single repetition of an experiment).

Compared to perceptions of the subject-oriented hierarchy's users, the usage-oriented hierarchy and combined hierarchy received higher ratings in terms of satisfaction and ease of use. Interestingly, these higher perception ratings correspond to the better performances with usage-oriented hierarchy and combined hierarchy navigation structures. The explanation for these higher ratings is the same as those offered for the performance difference across three navigation structures in the previous paragraph.

In theory, navigation structure's semantics, syntax, and task complexity affect Web site usability. Compared to subject-oriented hierarchy, usage-oriented hierarchy and combined hierarchy associate with better performance usability. Not surprisingly, simple tasks associate with better performance usability than complex tasks for each type of navigation structure.


# Audit 08: <b>Research Note</b>—Awareness Displays and Social Motivation for Coordinating Communication

- Group: `retained_layer:interface_or_interaction_design`
- Model decision: `True`; centrality `exclusive`; layer `interface_or_interaction_design`
- Gates: `{"purposeful_solution_design": true, "objective_metric_is_primary_target": true, "comparative_improvement_demonstrated": true, "objective_improvement_is_the_success_basis": true}`
- Model reason: 该文明确设计并比较了awareness display的三种界面形态（无显示/抽象/全显示）和团队激励条件，属于有目的的信息系统界面设计；其核心成功标准是客观可测的通信时机（中断时目标负荷）、目标任务绩效、发起者任务绩效和眼动注意力，而非主观满意度或感知；实验中相对于无显示控制条件和抽象/全显示对比展示了显著的客观绩效改进与注意力权衡，且这些客观改进是文章结论的主要乃至唯一依据。因此四个门全部通过，centrality为exclusive。
- Source: `E:\github\qual-llm-check-IS-utd\database_fulltext_all\09894_2008_b-research-note-b-awareness-displays-and-social-motivation-for-coordinating-communication.md`

#### Introduction

A substantial body of research shows that group work is much more difficult to accomplish when coworkers are physically distributed than when they are collocated (see Hinds and Bailey 2003, Powell et al. 2004 for reviews). In distributed environments, team members don’t communicate enough (Kraut et al. 1990), they don’t have enough contextual information (Cramton 2001) and their communication can be ineffective (Olson and Olson 2000). Researchers and designers have been building awareness displays with the goal of improving the connection between distributed co-workers since the early 1990s (Hudson and Smith 1996, Tang et al. 1994, Dourish and Bly 1992). Despite the intuition that awareness displays should improve coordination, we have little evidence that they actually help coordinate communication and almost no systematic research about the conditions under which they do so. The work presented here examines the utility of awareness displays for coordinating communication interactions.

Inopportune or disruptive communication attempts can occur in both distributed (Kraut et al. 1990) and colocated settings (Perlow 1999) as a result of information asymmetry (i.e., initiators of a communication not knowing recipients’ availability) and incentive incompatibility (i.e., initiators caring more about executing the communication than about the recipients’ welfare). But addressing the information asymmetry issue by providing awareness<sup>1</sup> information does not guarantee mutually beneficial communication timing. For example, Fogarty et al. (2004) found that IBM employees subverted an awareness display, treating a signal that co-workers were extremely busy as an indication that now was a good time to interrupt—valuing the information they would receive in the communication over the disruption to their co-worker’s ongoing task. We do not yet have a good understanding of the social conditions under which people will use awareness displays for opportune communication timing.

We also know little about how awareness displays should be designed to improve coordination. The design of awareness displays has been ad hoc, in many cases divorced from theories of interpersonal and organizational communication. Neither the commercial nor research examples of awareness displays (Fish et al. 1993, Dourish and Bly 1992, Tang et al. 1994, Fogarty et al. 2004) have systematically explored the design space to explicitly test the utility of design techniques to facilitate coor

#### Communication Timing and Performance

Previous work suggests that it is possible to interrupt people at times that minimize the disruptive impact interruptions have on a target’s ongoing work (e.g., Gillie and Broadbent 1989, Speier et al. 2003). For example, programmers are more productive in debugging if they are not interrupted during periods of peak concentration (Fogarty et al. 2005), and interruptions are generally less disruptive if they occur at task and subtask boundaries (Adamczyk and Bailey 2004). Thus, it follows that if Initiators are attempting to minimize their impact on the Target they should attempt their communication at a time when the Target is free (e.g., not deeply engaged in a higher-priority task), and that doing so will lead to better performance on the Target’s primary task. The rest of our theory on initiating interaction rests on this assumption which we validate in the experiments described in this paper.

#### Experiment 1



#### Method

Overview. In Experiment 1 two subjects played a stylized game where one (the Initiator) was dependent on the other (the Target) for important information. The Initiator tried to guess the identity of pictures as they were slowly revealed, and was allowed to ask the Target for hints by sending messages over the computer. Doing so interrupted the Target, who was engaged in a variant of McFarlane’s (2002) Jumpers game. The experiment varied the amount of information Initiators had about Targets workload and whether the Initiators perceived that they and the Targets were a team or not. The experimental design was a 3 (Awareness information) by 2 (Team manipulation) mixed design, with the Awareness information manipulated within subjects and the Team manipulated between subjects.

Task. The Initiator’s task was to quickly and correctly guess the identity of a partially obscured picture (640 426 pixels) as it was slowly uncovered (see Area D of Figure 2(a)). Small black squares (8 <sub>×</sub> 8 pixels) covering the image were gradually removed over

Figure 2 From Top to Bottom: (a) Initiator’s Screen in Experiment, (b) Target’s Screen in Experiment, (c) Awareness Display Conditions (Counterclockwise from Top Left: No Display, Abstract, Full )

[image omitted]  
Note. (a) Boxes A through E indicate the regions for eye tracking and were not visible to participants.

four minutes while “clues,” or random larger squares of the picture (40 <sub>×</sub> 40 pixels), were revealed and then hidden again. The game consisted of three rounds, during each of which the Initiator had to guess the identity of four different pictures.

Targets’ primary task was the Jumpers video game used by McFarlane (2002). (See left side of Figure 2(b).) Targets attempted to save jumpers as they fell from a building by catching them on a stretcher and bouncing them to the ambulance. Their score was based on the number of jumpers they saved. Their workload varied from zero to nine jumpers on screen simultaneously, with new jumpers arriving at random intervals.

Targets were given a copy of the pictures that Initiators were trying to guess, and thus became experts with access to information that Initiators needed (see right side of Figure 2(b)). Initiators and Targets were seated in separate rooms, and Initiators were able to send Targets 20 yes/no questions over the computer about the picture they were attempting to guess. The Initiators were informed that these questions took over Targets’ s

#### Results

Manipulation Check. Initiators completed a 12- item survey measure of group identity to check the effectiveness of the team manipulation (Henry et al. 1999). The inter-item reliability for the measure was satisfactory (Cronbach’s alpha <sub>=</sub> 085). Although Initiators in the Team condition identified more strongly with their partner than did Initiators in the Independent condition (Means: Team <sub>=</sub> 507, Independent <sub>=</sub> 467, SE 016); this difference was only marginally significant with (t36 <sub>=</sub> 203, p <sub>=</sub> 009), with a moderate effect size (Cohen’s d <sub>=</sub> 042) (Rosenthal and Rosnow 1991). Follow-up analysis showed that the team involvement manipulation did not influence either the Initiators’ or the Targets’ performance. This suggests that the team manipulation was not successful, so we will not further discuss the results from Experiment 1 with respect to the Team manipulation and do not test Hypothesis 5 in Experiment 1.

#### Experiment 2



#### Method

Task. Experiment 2 utilized the same laboratory task as Experiment 1, with a modified reward structure. In Experiment 2, Initiators were rewarded based on the time taken to guess the contents of each picture being revealed, and not simply correct picture identification as in Experiment 1. By rewarding Initiators on speed as well as accuracy, we highlighted the conflict they might experience between getting help quickly and waiting for a lull in Targets’ workload. We also lengthened the duration of each interruption, so that questions stayed on Targets’ screen for at least five seconds. The longer interruption allowed us to better observe the effect of Initiators’ interruption timing on Targets’ performance.<sup>5</sup>

Awareness Display. Experiment 2 used the same three within-subjects awareness display conditions used in Experiment 1 (no-display, abstract-display, and full-display). As in Experiment 1, each subject saw each of the three awareness display conditions during one round of the game; display order was counter-balanced using a Latin square design.

Team Orientation. As in Experiment 1, we manipulated between subjects whether the Initiators were independent and received individual rewards or were part of a team and received joint rewards. In the team condition, Initiators were rewarded based on the average of their score and their Targets’ score; they were told they were on a team with their Targets competing against other teams for a fifty-dollar prize, and that they and their Targets wore matching jerseys. To enhance their feelings of attachment to their partners, we showed Initiators in the team condition a photograph of their partners wearing the team jersey while sitting in front of a computer playing the Jumpers game (Walther et al. 2001) with the explanation that we wanted them to see what their partner would be doing during the study. Work on computer-mediated communication (CMC) has shown that participating in getting-acquainted activities with a virtual partner can result in almost the same level of trust development as face-to-face meeting (Zheng et al. 2002). To increase the likelihood of such a bond developing, Initiators in the team condition also participated in a structured social chat with confederates whom they believed to be their partners. They were instructed to exchange information with their partners in response to a list of get-acquainted questions such as “What is your major?” “What did you do last weekend?” “What is you

#### Results

Manipulation Check. Initiators in Experiment 2 completed a 12-item survey measure of group identity to check the effectiveness of the team manipulation (Henry et al. 1999). The inter-item reliability for the measure was satisfactory (Cronbach’s alpha <sub>=</sub> 082). Initiators in the Team condition identified more strongly with their partners than did Initiators in the Independent condition (Means: Team <sub>=</sub> 424, Independent <sub>=</sub> 375, SE <sub>=</sub> 016, with t30 <sub>=</sub> 223, p < 005). Results show that the social identity manipulation was substantially stronger in Experiment 2 than in Experiment 1, with a 26% increase in effect size (Cohen’s d <sub>=</sub> 053) (Rosenthal and Rosnow 1991).

#### Discussion

The studies presented here sought to address three open research questions: (1) Can awareness displays with information about a co-worker’s activities help coordinate communication? (2) How should they best be designed to do so? (3) Under what social conditions will people use them in this fashion? Table 4 summarizes the empirical results of the studies presented and support for the hypotheses aimed at addressing the three questions above. We found that under conditions of shared rewards and common identity, awareness displays showing a communication target’s workload were beneficial for reducing the disruption associated with interruption. In both Experiment 1 and 2 the targets of interruptions performed better when the Initiators had information about the Targets’ workload and, in Experiment 2, when the Initiators had social incentives to use that information. Our results from both Experiment 1 and 2 also show that a display with abstract representations of potential communication targets’ activity is as useful for coordinating communication as a display showing everything that partners were doing. In addition, we found that the full display, showing everything that the potential target was doing, was distracting to those initiating communication. In Experiment 1, the full display negatively affected Initiators’ performance compared to the abstract one, and in Experiment 2, it consumed substantially more visual attention, was more cognitively demanding, and reduced the amount of attention the initiators paid to their primary task.

These results have practical implications for the way information technology can be used to coordinate communication, especially in distributed-work settings. The conclusions we can draw from the results go beyond the design of awareness display technology. We have learned something about the granularity of information required for communication timing online. Researchers examining interruptions in field settings have highlighted the detailed way in which people draw inferences from the rich behavior they observe in face-to-face settings (e.g., Kraut et al. 1990). For example, Heath and colleagues, examining the interactions in a London dealing room, suggested that individuals require extremely detailed information about their coworkers’ activities to coordinate interaction appropriately and avoid disruption (Heath et al. 1995). Our research suggests that you don’t need this fine-grained level of detail to strategically time communication; an abstract representation of individuals’ work status may be sufficient.

Our results also tell us something about how the social context surrounding an interaction affects conscientiousness when interrupting. Perlow’s fieldwork on interruption in a software engineering firm (1999) showed that engineers interrupted each other with little regard for their coworkers’ current status, disrupting each other so much that the group missed production deadlines. However, these engineers had little incentive to interrupt conscientiously because they were rewarded based on their individual performance. The research presented here, in contrast, shows that common incentives and identity promoted individuals to pay attention to their partners’ work state before interrupting them. This result could be applied to many work settings where interruption is endemic, by better aligning incentives with decisions to communication. The principle of incentive alignment applies across many types of information system—e.g., failure to use knowledge management systems, failure of ERP systems, etc. Considering the incentive structure surrounding system use allows one to predict when collaboration technology will be successful (Grudin 1994). Organizations can align incentives among actors with potentially conflicting goals through structural changes (e.g., basing compensation on team performance; see Barua et al. 1995, DeMatteo et al. 1998). Alternatively, they can attach incentives directly to the communication behavior, as some firms have done for adding useful information to knowledge management systems (Davenport and Prusak 2000) or has been proposed for pricing of electronic communication (Kraut et al. 2002).

#### Implications for the Design of




# Audit 09: An analytic approach to better understanding and management of coronary surgeries

- Group: `retained_layer:prediction_model`
- Model decision: `True`; centrality `exclusive`; layer `prediction_model`
- Gates: `{"purposeful_solution_design": true, "objective_metric_is_primary_target": true, "comparative_improvement_demonstrated": true, "objective_improvement_is_the_success_basis": true}`
- Model reason: 本文的核心贡献是设计和构建了面向CABG术后结局的预测模型体系，包含四种机器学习分类器及信息融合敏感度分析，属于IS相关的预测模型设计。主要成功标准是客观的分类准确率、敏感度和特异度，并在固定测试集上与多个基准模型进行对比，证明SVM模型取得最高准确率87.74%。全文没有依赖主观态度、满意度等问卷构念来判断方案是否成功，因此客观指标改善是唯一且核心的成功依据。四个门控条件均满足，客观指标中心性为exclusive。
- Source: `E:\github\qual-llm-check-IS-utd\database_fulltext_all\16308_2012_an-analytic-approach-to-better-understanding-and-management-of-coronary-surgeries.md`

#### 1. Introduction

In recent years, healthcare has become one of the most spoken issues that have a direct impact on quality of life in the US and abroad. While the demand for healthcare services is increasing with the aging population, the supply side is having serious problems to keep up with the needed level and quality of service. In order to close the gap, healthcare systems ought to signi<sup>fi</sup>cantly improve their operational ef<sup>fi</sup>cacy (i.e., effectiveness and ef<sup>fi</sup>ciency). Effectiveness (doing the right thing, e.g., diagnosing and treating accurately) and ef<sup>fi</sup>ciency (doing it the right way, e.g., using least amount of resources and using the least amount of time) are the two fundamental pillars upon which the healthcare system can be revived [16]. One promising way to improve the healthcare ef<sup>fi</sup>cacy is to take advantage of advanced modeling techniques and large and feature rich data sources (true re<sup>fl</sup>ections of medical and healthcare experiences) to support accurate and timely decision making [16].

Decisions in healthcare can roughly be classi<sup>fi</sup>ed as either managerial or clinical. Managerial decisions involve optimal allocation of resources to various demand centers (which at the more detail level involves forecasting, capacity planning, scheduling, etc.). Medical decisions involve making the right diagnosis and implementing the right treatment. Computer systems that help in making medical decisions are often called medical decision support systems or clinical decision support systems. Clinical decision support systems (CDSS) are interactive computer programs, which are designed to assist physicians and other healthcare professionals with decision making tasks. The main goal of a CDSS is to link health observations (i.e., data) with health knowledge (i.e., expertise) to guide health choices by clinicians and managers for an improved healthcare. These CDSS systems encompass knowledge to guide the decision maker in optimal analysis of patient's condition, and subsequently leading to accurate diagnosis and treatment. The knowledge component of these systems may come from the experts (via expert systems) and/or it can be extracted from historical data sources (via data mining).

According to the American Heart Association, cardiovascular disease (CVD) was the underlying cause for 20.67% of deaths in the US [14]. Since 1900, CVD has been the number one killer every year except 1918, which was the year 

#### 3. Research method

At the highest level, the methodology that we followed in this study can be depicted as a 4-step process as illustrated in Fig. 1. Step 1 involves data identi<sup>fi</sup>cation, data acquisition, and data preparation related tasks. The outcome of this step is a pre-processed dataset which can be used in the rest of the steps. Step 2 involves the model building and model calibration tasks. Here we used four different types of models (arti<sup>fi</sup>cial neural networks, support vector machines, and two types of decision trees, namely C5 and CART), and went through a large number of experimental runs to calibrate the modeling parameters for each model type. The outcome of this step is a list of trained prediction models which only used the training dataset. Step 3 involves the comparative testing of the prediction models. Speci<sup>fi</sup>cally, it involves applying and recording the prediction ability (as measured by accuracy, sensitivity and speci<sup>fi</sup>city) of each of the four model types using the test dataset. Step 4 is the <sup>fi</sup>nal step, where trained models are exposed to a sensitivity analysis procedure where the comparative contribution of the variables to the prediction is measured.

#### 4. Results



#### 4.1. Prediction results

To compare the classi<sup>fi</sup>cation models, three performance criteria are adopted as follows:

$$
\text { Accuracy } = \frac {T P + T N}{T P + T N + F P + F N}\tag{1}
$$

$$
\text { Sensitivity } = \frac {T P}{T P + F N}\tag{2}
$$

$$
\text { Specificity } = \frac {T N}{T N + F P}\tag{3}
$$

where TP, TN, FP, FN denote true positive, true negative, false positive and false negative, respectively. Accuracy, shown by Eq. (1), measures the proportion of correctly classi<sup>fi</sup>ed test examples, therefore predicting the overall probability of the correct classi<sup>fi</sup>cation. Sensitivity and speci<sup>fi</sup>city, shown by Eqs. (2) and (3) respectively, measure the model's ability to predict the individual groups within itself (i.e., how accurately model predicts the positives and negatives). Table 2 shows all of the validation results (using only the test dataset) for all four model types in a tabular format.

[image omitted]  
Fig. 2. A process map for training and testing four model types in IBM SPSS modeler.

As the results indicate, SVMs produced the best performance with a prediction accuracy of 87.74% on the holdout sample (also produced the best sensitivity and speci<sup>fi</sup>city results with 89.48% and 86.01% respectively). The second best model was the C5 decision tree algorithm with a prediction accuracy of 79.62% on the holdout sample (and sensitivity and speci<sup>fi</sup>city results of 80.29% and 78.96% respectively). The other two methods, ANNs and CART decision tree algorithms took the third and the last places with prediction accuracy of 74.72% and 71.15% on hold-out sample respectively.

#### 4.2. Information fusion-based sensitivity analysis results

In machine learning, sensitivity analysis is a method for extracting the cause and effect relationship between the inputs and outputs of a trained prediction model [8]. Sensitivity analysis is similar to feature selection in that they both try to <sup>fi</sup>nd the relative importance of the independent variables (features) as they relate to the output variable. The main difference is when they are used. Feature selection is often used before starting to build prediction models in order to identify which independent variables should be include in the model building phase. On the other hand, sensitivity analysis is used after the models are built and suf<sup>fi</sup>ciently accurate prediction results are obtained. Sensitivity analysis provides the user with information about the comparative contribution that each independent variable provides to the prediction of the output variable. That said, one can also use sensitivity analysis results to change the independent variable list (what to include/exclude based on their relative contribution to the prediction models) and reconvene back to the prediction model building phase. By doing so, he/she uses sensitivity analysis as an alternative to feature selection.

In the process of performing sensitivity analysis, after the model is trained the learning is disabled so that the model parameters (e.g., network weights in ANNs) are not affected. The fundamental idea is that the sensitivity analysis measures the predictor variables based on the change in modeling performance that occurs if a predictor variable is not included in the model. Hence, the measure of sensitivity of a speci<sup>fi</sup>c predictor variable is the ratio of the error of the neural network model without the predictor variable to the error of the model that includes this predictor variable. The more sensitive the model is to a particular variable, the greater the performance decrease would be in the absence of that variable, and therefore the greater the ratio of importance. The same method is followed in arti<sup>fi</sup>cial neural networks, support vector machines and decision trees to rank the variables in terms of their importance according to the sensitivity measure de<sup>fi</sup>ned in Eq. (4) [30].

Prediction accuracy results for all four model types based on the test dataset.

<table><tr><td rowspan="2">Model typea</td><td rowspan="2"></td><td colspan="2">Confusion matricesb</td><td rowspan="2">Accuracyc</td><td rowspan="2">Sensiti

#### 5. Discussion and conclusions

Data mining, as a knowledge discovery tool, is becoming a popular enabler for improving the decision performance and hence the effectiveness and ef<sup>fi</sup>ciency in healthcare. Better information and knowledge provided to the right person at the right time in a healthcare setting will undoubtedly lead to better decisions and more favorable outcomes. Such data/fact driven information/knowledge resources packaged in a user-friendly decision support system can be an invaluable aid to both managerial as well as clinical decision makers.

In this study, we showed the power of data mining (i.e., machine learning techniques) in predicting the outcome and in analyzing the prognostic factors of complex medical procedures such as CABG surgery. It is shown herein that using a number of methods (as opposed to only one) in a competitive experimental setting has the potential to produce better predictive as well as explanatory results. Among the four methods that we used, SVMs produced the best prediction results with prediction accuracy of 88% on the hold-out sample. The information fusion-based sensitivity analysis results revealed the ranked importance of the independent variables. Some of the top variables identi<sup>fi</sup>ed in this analysis having to overlap with the most important variables identi<sup>fi</sup>ed in previously conducted clinical and biological studies con<sup>fi</sup>rm the validity and effectiveness of the proposed data mining methodology.

[image omitted]  
Fig. 3. Information fusion-based sensitivity analysis results.

From the managerial standpoint, clinical decision support systems that uses the outcome of data mining studies (such as the ones presented in this paper) are not meant to replace healthcare managers and/or medical professionals. Rather, they meant to support them in making accurate and timely decision to optimally allocate resources in order to increase the quantity and quality of medical services. There still is a long way to go before we can see these decision aids being used extensively in healthcare practices. Among others, there are behavioral, ethical, and political reasons for this resistance to adoption. May be the need and the government incentives for better healthcare systems will expedite the adoption.

Although data mining methods are capable of extracting patterns and relationships hidden deep into large medical datasets, without the cooperation and feedback from the medical professional, their results would have very limited use. The patterns found with data mining methods should be evaluated by medical professionals who have years of experi ence in the problem domain to decide whether they are logical, actionable and novel to fuel new biological and clinical research directions, and become a part of medical decision support systems.

Data mining methods rely on the existence and the correctness of data. If the data is not present or it is not accurate, the data mining results would be worthless; exemplifying the famous GIGO (garbage in garbage out) syndrome. In order to reap the bene<sup>fi</sup>ts of data mining, healthcare organizations should pay extra attention to collecting, storing and making available the proper data sources while complying with the privacy related laws and regulations (e.g., HIPPA, Sarbanes Oxley and etc.).

In summary, as the results indicated, machine learning techniques are capable of predicting the outcome of complex medical procedures (such as CABG surgery, which was the case used in this study), providing invaluable information for decision making. A good prediction model does more than just predict the outcome; it also provides information on the ranked importance of the prognostic factors. Having a good understanding of the medical situation helps improve the effectiveness and the ef<sup>fi</sup>ciency of clinical decision making and hence optimal use of healthcare resources; not to mention it would save more lives, which unarguably is the most important bene<sup>fi</sup>t one would look for.


# Audit 10: Predicting the length of hospital stay of burn patients: Comparisons of prediction accuracy among different clinical stages

- Group: `retained_layer:prediction_model`
- Model decision: `True`; centrality `exclusive`; layer `prediction_model`
- Gates: `{"purposeful_solution_design": true, "objective_metric_is_primary_target": true, "comparative_improvement_demonstrated": true, "objective_improvement_is_the_success_basis": true}`
- Model reason: 文章提出并评估了针对烧伤患者LOS的预测模型（M5和SVM回归），并将预测准确性（MAE/MRE）作为主要成功标准。全文通过1080例数据的交叉验证，明确展示了后期治疗阶段预测误差显著下降、SVM回归相对线性回归有所改进等客观比较证据。所有四道门均通过，且客观指标是文章成功判断的唯一核心依据。
- Source: `E:\github\qual-llm-check-IS-utd\database_fulltext_all\00950_2010_predicting-the-length-of-hospital-stay-of-burn-patients-comparisons-of-prediction-accuracy-among.md`

#### 1. Introduction

The healthcare industry faces constant pressures to lower costs by improving the utilization of resources while maintaining and even enhancing the quality of service. Effective healthcare resource management is especially indispensable for addressing these seemingly contradictory pressures. Of particular importance are hospital beds, scarce and critical healthcare resources, whose effective management can bene<sup>fi</sup>t healthcare service planning, medical resource allocations, and clinical governance and audits [21,33]. Toward this end, predictions of an inpatient's length of stay (LOS) represents an essential issue that can be supported by statistical methods or proliferating arti<sup>fi</sup>cial intelligence (AI)-based prediction techniques. Prior studies have paid great attention on LOS predictions in various specialty areas, ranging from general medical divisions (including general surgery [26], internal medicine [26], trauma [8], psychiatric [21,31], intensive care [55], and long-term care [57]) to speci<sup>fi</sup>c medical diseases/treatments (e.g., transurethral resection of the prostate [1], stroke [6], chronic obstructive pulmonary concerns [23], cardiac surgery [51], single lung transplantation [29], and burns [2,20,54]).

In particular, LOS prediction is crucial for diseases or injuries that necessitate long treatments or involve scarce patient care resource. A good case in point is burn injuries, a disastrous trauma that can have wide-ranging complications that make such cases dif<sup>fi</sup>cult to manage and treat [12]. According to the study by Herndon and Spies [18], nearly 2 million people suffer burns every year in the United States, and approximately 100,000 of them are moderate to severe, requiring hospitalization [18]. Burn patients generally require long LOS for treatment. As the annual health statistics released by Department of Health, Taiwan, reveal, the mean LOS for burn patients was 11.43 days in 2004, longer than the average across all hospital beds (i.e., 9.96 days) [11]. Previous epidemiological studies of burn injuries also show longer LOS for burn patients than for others. Speci<sup>fi</sup>cally, reported average LOS of burn patients includes 20.4, 18, 16.7, 15.5, and 14.9 days, according to Burton et al. [4], Chien et al. [7], Lari et al. [28], da Silva et al. [45], and Lv et al. [33], respectively. However, hospital resources for burn patients are scarce. For example, only 0.17 beds, which account for only 0.29% 

#### 4. Empirical evaluation

In this section, we provide empirical evaluation results for the two AI-based prediction techniques (i.e., M5 and SVM regression) across the three clinical stages, using linear regression analysis (or regression for short) as the performance benchmark. In this study, we use Weka (www.cs.waikato.ac.nz/ml/weka/), an open source machine learning software, to construct LOS prediction models based on the linear regression analysis, $\mathsf { M } 5 , ^ { 2 }$ and SVM regression techniques. To avoid over<sup>fi</sup>tting each prediction technique to our evaluation data set, we simply adopt the parameter values suggested by Weka for each prediction technique without parameter tuning. In the following, we <sup>fi</sup>rst describe our data collection, then depict our empirical evaluation design (including the evaluation procedure and criteria), and <sup>fi</sup>nally discuss some important evaluation results.

#### 4.2. Evaluation procedure and criteria

To expand the number of trials when we estimate the effectiveness of the LOS prediction techniques for each clinical stage, we adopt a tenfold cross-validation strategy. Speci<sup>fi</sup>cally, we split the data set randomly into ten mutually exclusive subsets of equal size. We then designate each subset (i.e., 108 cases) as the testing data set while the others (i.e., 972 cases) serve as the training data set. To minimize potential biases that may result from the randomized folding process, we perform this tenfold cross-validation process three times and estimate the overall performance by averaging the performance estimates obtained from the 30 individual trials.

We measure the effectiveness of a LOS prediction technique according to the mean absolute error (MAE) and the mean relative error (MRE), de<sup>fi</sup>ned as follows:

$$
\begin{array}{l} M A E = \frac {\sum_ {i = 1} ^ {n} \left| P r e d i c t e d L O S _ {i} - A c t u a l L O S _ {i} \right|}{n} \text {and} \\ M R E = \frac {\sum_ {i = 1} ^ {n} \frac {\left| P r e d i c t e d L O S _ {i} - A c t u a l L O S _ {i} \right|}{A c t u a l L O S _ {i}}}{n} \end{array}
$$

where PredictedLOS is the predicted LOS for the ith testing instance, ActualLOS is the actual LOS of the ith testing instance, and n is the total number of testing instances.

#### 4.3. Comparative evaluation results

We <sup>fi</sup>rst examine the effectiveness of different LOS prediction techniques at each clinical stage. As Table 4(a) shows, the MAEs attained by the use of the regression, M5, and SVM regression techniques at the admission stage are 9.532, 9.246, and 8.992 days, respectively. When we perform the LOS prediction at the acute stage, the resultant MAEs (i.e., 9.503, 9.308, and 8.994 days, respectively) remain comparable to those observed at the admission stage. As we show in Table 4(b), for each prediction technique, the differential in MAE between the admission and acute stages is statistically insigni<sup>fi</sup>cant. That is, the inclusion of the two treatment variables in the acute stage (i.e., whether any surgical operation undergone, and interval between admission and <sup>fi</sup>rst surgery) does not improve the LOS prediction accuracy. In contrast, the LOS prediction during the post-treatment stage reduces the MAE by more than 30% for every prediction technique under investigation compared

Mean absolute error (MAE) and signi<sup>fi</sup>cant tests of LOS predictions.

<table><tr><td colspan="4">(a) Mean absolute error (MAE)</td></tr><tr><td></td><td>Admission</td><td>Acute</td><td>Post-treatment</td></tr><tr><td>Regression</td><td>9.532</td><td>9.503</td><td>6.314</td></tr><tr><td>M5</td><td>9.246</td><td>9.308</td><td>6.331</td></tr><tr><td>SVM regression</td><td>8.992</td><td>8.994</td><td>6.074</td></tr></table>

(b) Signi<sup>fi</sup>cant test (p-value) of different clinical stages

<table><tr><td></td><td>Regression</td><td>M5</td><td>SVM regression</td></tr><tr><td>Admission vs. acute</td><td>0.9345</td><td>0.8599</td><td>0.9956</td></tr><tr><td>Admission vs. post-treatment</td><td>0.0000***</td><td>0.0000***</td><td>0.0000***</td></tr><tr><td>Acute vs. post-treatment</td><td>0.000***</td><td>0.0000***</td><td>0.0000***</td></tr></table>

(c) Signi<sup>fi</sup>cant test (p-value) of different prediction techniques

<table><tr><td></td><td>Admission</td><td>Acute</td><td>Post-treatment</td></tr><tr><td>Regression vs. M5</td><td>0.2913</td><td>0.6388</td><td>0.9390</td></tr><tr><td>Regression vs. SVM Regression</td><td>0.0574*</td><td>0.2456</td><td>0.2791</td></tr><tr><td>M5 vs. SVM regression</td><td>0.3589</td><td>0.4791</td><td>0.2493</td></tr></table>

<sup>⁎</sup>: signi<sup>fi</sup>cant at pb0.1 on a two-tailed paired t-test.

Table 6

with the values during the admission and acute stages, speci<sup>fi</sup>cally, from 9.532 and 9.5

#### 4.4. Breakdown analysis

We further conduct a breakdown analysis of the effectiveness of different prediction techniques (using all independent variables pertaining to each clinical stage) according to the extent of burn (i.e., TBSA). Speci<sup>fi</sup>cally, we segment the 1080 burn cases into <sup>fi</sup>ve TBSA groups: 1–20%, 21–40%, 41–60%, 61–80%, and 81–100%. We obtain several interesting <sup>fi</sup>ndings from this analysis. First, as Table 8 (a) demonstrates, for each technique, the corresponding MAE increases as TBSA increases from 1–20% to 81–100%. This phenomenon occurs across all clinical stages. That is, all of the techniques investigated are more promising for predicting LOS for patients with minor or moderate burns than for patients with severe burns.

The higher MAE for patients with greater TBSAs likely re<sup>fl</sup>ects that the treatment of patients with minor or moderate burns is far less complicated and more controllable than that for patients with severe burns. As a result, the predictability of LOS for patients with lower TBSA should be higher than that for patients with greater TBSA. Second, as Table 8(a) and (b) show, SVM regression consistently outperforms the other two prediction techniques in the <sup>fi</sup>rst four TBSA groups (i.e., TBSA between 1% and 80%) across the three clinical stages. However, for the most severely burned group (i.e., TBSA 81– 100%), M5 is most effective during the admission and acute stages, whereas the regression technique is most accurate at the posttreatment stage. This <sup>fi</sup>nding may suggest that SVM regression has a tendency to train its prediction model toward larger groups (i.e., with more training instances) than M5 and the regression technique, because the most severely burned group contains only a very small percentage of the burn cases (i.e., 0.46%) in our data set.

We also perform a breakdown analysis of the effectiveness of different prediction techniques according to the burn cases' actual LOS. We divide the burn cases into <sup>fi</sup>ve groups according to their actual LOS: between 7–20 days, 21–34 days, 35–48 days, 49– 62 days, and 63–193 days. Over all clinical stages, the <sup>fi</sup>ndings remain similar to those from the TBSA breakdown analysis. First, as we show in Table 9(a), for each prediction technique, MAE correlates positively with actual LOS (i.e., the corresponding MAE increases as actual LOS increases from 7–20 to 63–193 days). This positive correlation may occur because patients

#### 5. Conclusion and future research directions

In this study, we evaluate the effectiveness of LOS predictions for burn patients across three different clinical stages, namely, admission, acute, and post-treatment. In addition, we compare the effectiveness of two AI-based prediction techniques (i.e., M5 and SVM regression), using linear regression analysis as our performance benchmark. On the basis of 1080 burn cases, our empirical evaluation results suggest that the accuracy of LOS prediction at the acute stage does not improve compared with that at the admission stage, but predictions during the post-treatment stage are signi<sup>fi</sup>cantly more accurate. Moreover, the two AI-based prediction techniques, especially SVM regression, appear more effective than the regression technique for predicting LOS across various clinical stages. Finally, our breakdown analyses indicate that SVM regression outperforms its counterparts for burn patients who suffer TBSA of less than 80% or require actual

Breakdown analysis by different extent of burn (TBSA) groups.

<table><tr><td colspan="10">(a) Mean absolute error (MAE)</td></tr><tr><td rowspan="2">Range of TBSA(% of burn cases)</td><td colspan="3">Admission</td><td colspan="3">Acute</td><td colspan="3">Post-treatment</td></tr><tr><td>Reg.</td><td>M5</td><td>SVM reg.</td><td>Reg.</td><td>M5</td><td>SVM reg.</td><td>Reg.</td><td>M5</td><td>SVM reg.</td></tr><tr><td>1–20% (77.78%)</td><td>7.467</td><td>7.192</td><td>7.060</td><td>7.445</td><td>7.352</td><td>7.041</td><td>5.158</td><td>5.122</td><td>4.933</td></tr><tr><td>21–40% (16.02%)</td><td>13.117</td><td>12.640</td><td>11.631</td><td>13.219</td><td>12.109</td><td>11.642</td><td>6.987</td><td>7.032</td><td>6.228</td></tr><tr><td>41–60% (3.61%)</td><td>19.530</td><td>21.334</td><td>19.110</td><td>19.561</td><td>20.508</td><td>19.132</td><td>13.477</td><td>12.958</td><td>12.070</td></tr><tr><td>61–80% (2.13%)</td><td>30.490</td><td>34.638</td><td>29.368</td><td>29.883</td><td>33.393</td><td>28.764</td><td>25.699</td><td>28.725</td><td>23.530</td></tr><tr><td>81–100% (0.46%)</td><td>53.201</td><td>38.398</td><td>68.122</td><td>55.767</td><td>43.285</td><td>71.021</td><td>44.346</td><td>55.164</td><td>55.978</td></tr></table>

Note: bolded numbers indicate the lowest MAE across all prediction techniques examined at each clinical stage.

<table><tr><td rowspan="2">Range of TBSA (% of Burn Cases)</td><td colspan="3">Admission</td><td colspan="3">Acute</td><td colspan="3">Post-treatment</td></tr><tr><td>Reg.</td><td>M5</td><td>SVM reg.</td><td>Reg.</td><td>M5</td><td>SVM reg.</td><td>Reg.</td><td>M5</td><td>SVM reg.</td></tr><tr><td>1–20% (77.78%)</td><td>0.496</td><td>0.484</td><td>0.439</td><td>0.498</td><td>0.495</td><td>0.440</td><td>0.319</td><td>0.319</td><td>0.289</td></tr><tr><td>21–40% (16.02%)</td><td>0.609</td><td>0.533</td><td>0.477</td><td>0.613</td><td>0.517</td><td>0.478</td><td>0.295</td><td>0.289</td><td>0.235</td></tr><tr><td>41–60% (3.61%)</td><td>0.383</td><td>0.417</td><td>0.311</td><td>0.389</td><td>0.410</td><td>0.312</td><td>0.252</td><td>0.237</td><td>0.211</td></tr><tr><td>61–80% (2.13%)</td><td>0.464</td><td>0.561</td><td>0.357</td><td>0.452</td><td>0.553</td><td>0.341</td><td>0.357</td><td>0.403</td><td>0.284</td></tr><tr><td>81–100% (0.46%)</td><td>0.317</td><td>0.224</td><td>0.421</td><td>0.336</td><td>0.265</td><td>0.443</td><td>0.286</td><td>0.396</td><td>0.348</td></tr></table>

Note: bolded numbers indicate the lowest MRE across all prediction techniques examined at each clinical stage.

Table 9  
Breakdown analysis by different LOS groups.

<table><tr><td colspan="10">(a) Mean absolute error (MAE)</td></tr><tr><td rowspan="2">Range of actual LOS(% of burn cases)</td><td colspan="3">Admission</td><td colspan="3">Acute</td><td colspan="3">Post-treatment</td></tr><tr><td>Reg.</td><td>M5</td><td>SVM reg.</td><td>Reg.</td><td>M5</td><td>SVM reg.</td><td>Reg.</td><td>M5</td><td>SVM reg.</td></tr><tr><td>7–20 (60.93%)</td><td>6.708</td><td>6.033</td><td>5.371</td><td>6.631</td><td>5.970</td><td>5.382</td><td>3.972</td><td>3.890</td><td>3.576</td></tr><tr><td>21–34 (23.98%)</td><td>8.398</td><td>8.039</td><td>7.989</td><td>8.506</td><td>8.309</td><td>8.000</td><td>5.893</td><td>5.812</td><td>5.574</td></tr><tr><td>35–48 (7.32%)</td><td>16.492</td><td>17.961</td><td>15.624</td><td>16.385</td><td>18.573</td><td>15.590</td><td>11.103</td><td>11.879</td><td>10.301</td></tr><tr><td>49–62 (3.51%)</td><td>17.200</td><td>18.709</td><td>18.600</td><td>16.990</td><td>19.491</td><td>18.471</td><td>14.704</td><td>15.898</td><td>14.754</td></tr><tr><td>63–193 (4.26%)</td><td>38.020</td><td>39.204</td><td>47.106</td><td>38.205</td><td>38.355</td><td>47.090</td><td>27.035</td><td>30.767</td><td>30.191</td></tr></table>

Note: bolded numbers indicate the lowest MAE across all prediction techniques examined at each clinical stage.

(b) Mean relative error (MRE)

<table><tr><td rowspan="2">Range of Actual LOS (% of Burn Cases)</td><td colspan="3">Admission


# Audit 11: Optimal Policy for Software Patents: Model and Comparative Implications

- Group: `retained_layer:prescriptive_model_or_optimization`
- Model decision: `True`; centrality `exclusive`; layer `prescriptive_model_or_optimization`
- Gates: `{"purposeful_solution_design": true, "objective_metric_is_primary_target": true, "comparative_improvement_demonstrated": true, "objective_improvement_is_the_success_basis": true}`
- Model reason: 四个门均通过：作者设计了一个可实施的专利政策决策规则（μ, λ, t）并通过解析与数值优化求解；社会总福利是明确且客观定义的优化目标；以自由市场NPE和PER内替代政策为参照，命题证明最优政策最大化社会福利并改善所有利益相关者；文章成功依据完全是客观福利指标，无主观构念。因此保留。
- Source: `E:\github\qual-llm-check-IS-utd\database_fulltext_all\13306_2009_optimal-policy-for-software-patents-model-and-comparative-implications.md`

### Optimal Policy for Software Patents: Model and Comparative Implications

Matt E. Thatcher & David E. Pingry

To cite this article: Matt E. Thatcher & David E. Pingry (2009) Optimal Policy for Software Patents: Model and Comparative Implications, Journal of Management Information Systems, 26:3, 103-134

To link to this article: http://dx.doi.org/10.2753/MIS0742-1222260304

[image omitted]

Published online: 08 Dec 2014.

[image omitted]

Submit your article to this journal

Article views: 9

[image omitted]

View related articles

### Optimal Policy for Software Patents: Model and Comparative Implications

Matt E. Thatche r and David E. Pin gry

Matt E. Thatche r is an Associate Professor of Computer Information Systems at the College of Business, University of Louisville. He holds a B.S. in economics and an M.A. and Ph.D. in information systems from the Wharton School of the University of Pennsylvania. His research examines the strategic and economic effects of IT with a focus on four themes: IT value, software patent policy design, IT outsourcing, and the social costs of information privacy. His work has appeared in Information Systems Research, Journal of Management Information Systems, MIS Quarterly, Communica tions of the ACM, Decision Support Systems, Journal of Strategic Information Systems, Journal of Financial Services Research, and Journal of Information Technology Theory and Application.

David E. Pingry is McClelland Professor of Management Information Systems and Economics at the Eller College of Management, University of Arizona, where he has been since 1974. He holds a Ph.D. in economics from Purdue University and an A.B. in Economics from the University of Illinois. Professor Pingry was also on the faculty at Virginia Tech, held visiting faculty positions at Purdue University and Texas A&M, and held the Treibick Visiting Endowed Chair in the Connecticut Information Technology Institute at the University of Connecticut. His current interests are decision support systems, patent policy, and IT productivity.

Abstract: We use a duopoly model of quality–price competition between a software innovator and an imitator to determine the socially optimal software patent policy and to assess the social welfare implications of alternative patent policies. We find that the optimal patent policy is to grant patent protection for the entire life of the innovative software product (i.e., set infinite patent length) and to set the novelty and nonobviousness requirement for attaining a patent (i.e., patent height) and the scope of patent protection (i.e., patent width) such that both the innovator and imitator produce higher-quality products than they would in the free market. This policy not only maximizes social welfare but also makes the innovator, imitator, and consumers better off than in the free market. However, counter to intuition, we find that firms exhibit lower research and development intensity under the socially optimal patent policy than they do under free market competition. While highly stylized, the model offers a useful framework within whic

#### Conclusions

Based on the m ode l, the reader may be tempted to believe that the patent authority should be able to clearly see the different PERs (or policy targets) over time and identify a portfolio of patent policies optimized across products and industries. However, there are implementation issues that affect the patent authority’s ability to see the PER and to set effective policy. Specifically, the data requirements for setting good patent policy are enormous. The patent authority must collect accurate information about the characteristics of consumer demand, the characteristics of the innovator’s cost structure, the innovator’s cost of quality parameter, and the imitator’s best response function, as well as forecast the patent life for each innovation. In addition, the patent authority must develop and maintain a complete, up-to-date repository of prior artifacts to assess the novelty of the innovator’s product. Since all of the information may change over time, it must be continuously collected, updated, and maintained to identify the size and location of the PER, and therefore, identify socially good policy options. In some cases, the PER may be impossible to identify since this information may not be available to the patent authority. A great deal of empirical research is needed to determine the perverse effects of these data issues and to determine ways to overcome them.

Although highly stylized, the model presented in this paper offers a useful framework for researchers, regulators, and policymakers to use to think about the economic aspects of software patent policy design and implementation [38]. It also opens the possibility for empirical explorations and model extensions. Many issues arose in the construction, analysis, and review of this model that call for future extensions. For example, future work may extend the model to examine the impact of sequential, cumulative innovation, consider software competition among more than two firms, and consider the impact of blocking patents. In addition, future work may compare and contrast the costs, benefits, and trade-offs among alternative intellectual property protection mechanisms—such as trade secrets, copyrights, and private protection technologies— and examine the socially optimal portfolio of protection mechanisms (both public and private). In addition, future work may also consider alternative product development cost structures and attempt to generalize the results beyond the software-specific assumptions in our model (e.g., zero imitation costs and zero marginal costs).

While the economic model presented in this paper demonstrates the potential benefits and pitfalls of awarding software patents, it also exposes the enormous amount of information required to attain the benefits while avoiding the pitfalls. The balance of the richness of the model (placing the patent authority in the first-mover position and the inclusion of all three critical policy parameters) and the simplicity of the model (using specific functional forms to derive the critical PER artifact) has created a framework that stimulates and enables a disciplined discussion of the critical economic trade-offs in making patent policy.

Acknowledgments: The authors gratefully thank Stephen M. Miller, Rob Kauffman, Reza Torkzadeh, John Drabicki, the Editor-in-Chief Vladimir Zwass, and the four anonymous reviewers for their helpful comments and contributions. Early versions of the paper were presented at the 2007 Hawaii International Conference on System Sciences, the 2004 Workshop on Information Systems and Economics, and at research seminars at the University of Louisville, Temple University, University of Nevada, Las Vegas, and University of Arizona. The contributions and suggestions provided at these presentations are acknowledged and appreciated.


# Audit 12: Hedging risks with interruptible load programs for a load serving entity

- Group: `retained_layer:prescriptive_model_or_optimization`
- Model decision: `True`; centrality `exclusive`; layer `prescriptive_model_or_optimization`
- Gates: `{"purposeful_solution_design": true, "objective_metric_is_primary_target": true, "comparative_improvement_demonstrated": true, "objective_improvement_is_the_success_basis": true}`
- Model reason: 文章提出并求解了一个可中断负荷采购的随机规划优化模型（Gate 1通过）；模型目标函数明确最小化CVaR，并以期望利润为约束，均为客观数值指标，且是文章的核心成功标准（Gate 2通过）；案例研究中通过与不采用可中断负荷的基本情形对比，展示了在供给冲击下ΔProfit和ΔCVaR的明确改善（Gate 3通过）；整篇文章的结论完全基于期望利润和CVaR等客观绩效改进，无主观构念作为成功依据（Gate 4通过）；因此strict_objective_improvement_match为true，centrality为exclusive。
- Source: `E:\github\qual-llm-check-IS-utd\database_fulltext_all\07286_2009_hedging-risks-with-interruptible-load-programs-for-a-load-serving-entity.md`

#### 1. Introduction

During the past two decades, the electric industry throughout the world has been subject to major changes. The power industry has moved from a vertically integrated structure to a more competitive one. The restructuring of electric industry has changed the role of traditional entities and created new entities such as generation companies (GENCOs), regulated transmission companies (TRANSCOs), and load serving entities (LSEs) [31].

An LSE buys electricity from the wholesale market for resale to its customers. The price of electricity in the wholesale market is set by the supply and demand equilibrium. Consequently, the spot market price is uncertain and volatile, so the LSE is exposed to price risk. In addition, the LSE is obliged to meet the varying demand of its customers at regulated prices. Therefore, the LSE is faced with the uncertainties of customers' demand. Nevertheless, the most challenging problem faced by the LSE is the market price risk such that uncontrolled exposure to this risk could lead to devastating consequences. For example, in February 2004, the marginal clearing prices in ERCOT (Electric Reliability Council of Texas), during a 3-day ice storm reached the maximum allowable of \$999 per megawatt hour, causing one LSE, Texas Commercial Energy, to lose substantial amounts of money that led to bankruptcy [9,12].

Using risk management techniques for managing and controlling of such uncertainties is necessary. There are several instruments such as forward contracts, future contracts, call/put options, which can be used by the LSE for hedging against risks [9,25,36]. Interruptible service contract is another type to be used by the LSE for managing and controlling the risks [15].

Interruptible load programs are voluntary options, in which customers receive credits for permitting the utility to interrupt temporarily part or all of their loads during the period of the contract [5]. Generally, in an interruptible contract, the supply of customers is not interrupted. Instead, the customers who fail to comply are subject to severe penalties, thereby providing an incentive for customers to interrupt their loads. In an interruptible contract, the number of interruptions over the period of the contract, the maximum duration of each interruption, and the noti<sup>fi</sup>cation time required prior to an interruption, which is typically between 5 min and 24 h, are speci<sup>fi</sup>ed [5].

Many papers have addressed the issue of interruptible load pr

#### 2. Basic methodologies



#### 4. Case study and results analysis



#### 4.2. Results analysis

The number of considered scenarios affects the results of the problem. A low number of scenarios may result in inaccuracy, while a large number of scenarios requires high computational burden. To determine the number of scenarios required for an accurate representation of the uncertainties, the expected pro<sup>fi</sup>t versus the number of

#### 4.3. Sensitivity analysis

As mentioned before, forward contracts are the ef<sup>fi</sup>cient means for hedging against risks. To determine how assumed contracts (forward contracts) affect the results, two scenarios with different volumes of forward contracts are considered (as compared with Table 1).

• Scenario FW1: In this scenario, it is assumed that the LSE procures its demand only from the pool. In other words, the LSE does not sign any forward contract.

(a)  
[image omitted]  
(b)

[image omitted]

• Scenario FW2: In this scenario, it is assumed that the LSE uses more forward contracts. It is assumed that the LSE procures the average of its demand through forward contracts. In other words, the purchased power from the on-peak and round-the-clock forward contracts are assumed to be 700 MW and 3500 MW, respectively, while the prices of forward contracts are remained unchanged.

The expected pro<sup>fi</sup>t and $\mathrm { C V a R } _ { 0 . 9 5 }$ of FW1 and FW2, for two base cases, i.e., normal state (case 1) and when a supply/demand shock occurs (case 5), are shown in Table 10. It is observed that in normal state, the expected pro<sup>fi</sup>t of FW1 is greater than that of FW2. In contrast, when the supply shock occurs, the expected pro<sup>fi</sup>t of FW2 is greater than that of FW1. In addition, in both scenarios, the risks of FW2 are smaller than that of FW1.

Table 11 shows the effects of interruptible load programs for scenarios FW1 and FW2, when the supply shock occurs. It is observed that in both scenarios, the expected pro<sup>fi</sup>t is considerably increased and the risks are signi<sup>fi</sup>cantly decreased. Meanwhile, as the volume of forward contracts increases, the effects of interruptible contracts on improving the expected pro<sup>fi</sup>t or reducing the risks decrease.

#### 5. Conclusions

This paper addressed the hedging problem of the LSE using interruptible load programs. A stochastic programming framework was proposed to determine the optimal procurement of interruptible loads, for a speci<sup>fi</sup>ed period of time. The objective was to minimize the risks in terms of a multi-period risk measure. As some risk measures such as variance and VaR fail to be coherent risk measures and are not appropriate for discrete functions, CVaR was used as a risk measurement index. The available amounts of interruptible loads were considered as a function of pecuniary compensation that the LSE offers to the participants. Different types of interruptible contracts were considered and their effects in the optimal procurement policy were analyzed.

The analysis showed that in usual cases, the effects of interruptible contracts on the expected pro<sup>fi</sup>t increasing and/or risks decreasing are insigni<sup>fi</sup>cant, but in situations where a supply or demand shock occurs and consequently the spot market prices are sharply increased, interruptible contracts can help the LSE to prevent decreasing/increasing its expected pro<sup>fi</sup>t/risks. Therefore, this option can act as an ef<sup>fi</sup>cient means for hedging risks in these situations.

[image omitted]

[image omitted]  
Fig. 8. The sample autocorrelation function.


# Audit 13: Developing maintainable software: The Readable approach

- Group: `retained_layer:software_system_or_artifact`
- Model decision: `True`; centrality `exclusive`; layer `software_system_or_artifact`
- Gates: `{"purposeful_solution_design": true, "objective_metric_is_primary_target": true, "comparative_improvement_demonstrated": true, "objective_improvement_is_the_success_basis": true}`
- Model reason: 四个门径均通过：作者有目的地设计了Readable这一IS相关解决方案（可执行表格化表示与执行环境）；主要成功标准是客观打分的是非题理解测试，明确以提升程序理解（尤其是控制流）为目标；实验将Readable与传统Java对照，H1在调整分和原始分上均显著改善，且其余构念未显著受损；结论完全基于客观测试结果，没有依赖主观量表或感知指标，因此objective_metric_centrality为exclusive。
- Source: `E:\github\qual-llm-check-IS-utd\database_fulltext_all\10622_2006_developing-maintainable-software-the-readable-approach.md`

#### Abstract

Software maintenance is expensive and difficult because software is complex and maintenance requires the understanding of code written by someone else. A prerequisite to maintainability is program understanding, specifically, understanding the control flows between software components. This is especially problematic for emerging software technologies, such as the World Wide Web, because of the lack of formal development practices and because web applications comprise a mix of static and dynamic content. Adequate representations are therefore necessary to facilitate program understanding. This research proposes an approach called R<sup>eadable</sup> (Readable, Executable, Augmentable Database-Linked Environment) that generates executable, tabular representations that can be used to both understand and manipulate software applications. A controlled laboratory experiment carried out to test the efficacy of the approach demonstrates that the representations significantly enhance program understanding. The results suggest that the approach and the corresponding environment may be useful to alleviate problems associated with the software maintainability of new web applications. <sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Web development; Maintenance; Programming

#### 1. Introduction

Software maintenance remains the most expensive component of information system development, consuming 50% to 80% of resources [7,38,42–44,67,86]. A major contributor to this cost is inadequate program understanding [10,42–44,56,94]. When programs are difficult to understand, maintainers, who are often not the same as developers, spend more time reading code, and make incorrect modifications to it. Most approaches to improving program understanding (e.g., CASE Tools, sophisticated Integrated Development Environments (IDE)) add presentation mechanisms to existing programming languages [11,15,45,52,72] instead of attempting to fundamentally change the way code is written. The understanding of code is thus linked to continued use of the CASE tool or IDE. This can be problematic because these tools are often used during the initial development of an application but are difficult to employ during maintenance. Maintenance typically involves looking at someone else’s code, often without access to the design or rationale captured using a CASE tool or an IDE.

The problem is more acute in applications developed for the World Wide Web, where documentation practices can be especially difficult to follow because of rapid development cycles [2,5]. The challenge is exacerbated by the structure of these applications, which includes a hybrid of static content and programming code [6,13,29]. The hybrid nature of such applications makes understanding the program, and consequently maintenance, an onerous task.

The objective of this research is to: propose a new approach to authoring applications (especially web applications) to improve their understanding during the maintenance phase. We conceptualize the solution as an approach that helps the programmer communicate to the maintainer information about a key program understanding construct, i.e., control flows [56]. To facilitate this communication, the information must be easy for a programmer to capture, and a maintainer to understand. The contribution of this research is an approach for capturing such manipulable representations of control flow information, and a corresponding environment that generates executable code based on these representations. Our work builds on prior research on control flow representations such as state-transitions [34,35], Turing Machines [78], and tables [53,58] to propose a layered approach, called R<sup>eadable</sup> (Readable, Executable, Augmented Database-Linked Environment), that represen

#### 4. Empirical analysis

To investigate whether the proposed approach with its instantiation as tabular representations [53,58] of Pennington’s constructs [56] would contribute to program understanding, a testable empirical model was developed. The model focused on investigating whether programs created with the R<sup>eadable</sup> approach and executed with the R<sup>eadable</sup> environment would be more understandable as compared to traditional programs. To reflect the critical nature of the control flow construct in program understanding [56], the model specifically focused on testing improvements in the understanding of this construct without compromising understanding of the other constructs, that is, components, variables, and program states [56]. Fig. 4 presents the research model.

A laboratory experiment was designed to test the claims embedded in the testable empirical model, specifically, the claim that the R<sup>eadable</sup> approach would enhance program understanding compared to traditional applications, and thus, simplify maintenance. The programming constructs were operationalized in the software following either A1: the READABLE approach, or A2: the Traditional approach. Four hypotheses were formulated that mapped directly to each of Pennington’s four constructs (see Table 5). A factual 20-item true/false questionnaire (presented as Appendix A.3) was employed to test the four hypotheses.

Of these four hypotheses, only H1 was of specific interest as it tested for hypothesized benefits of R<sup>eadable</sup>. The remaining three hypotheses were included as forms of statistical control. Specifically, H1 tested if the understanding of R<sup>eadable</sup>’s control flow would be superior to that of a traditional programming language. As program states combine an understanding of control and data flow, it was also hypothesized that subjects would more easily understand R<sup>eadable</sup> program states (H2). Even if R<sup>eadable</sup> improved subjects’ understanding of control flow, R<sup>eadable</sup> would not improve program understanding if it reduced understanding of a program’s data flow. Given sufficient statistical power, a failure to reject H3 would suggest that the R<sup>eadable</sup> approach did not produce unnecessary effects on data flow. Finally, as both R<sup>eadable</sup> and traditional programming modules are fundamentally the same, we would expect that our treatment and control groups would understand the modules equally well. If a difference 

#### 4.1. Experimental procedure

The study followed a laboratory experiment format patterned after Pennington [56]. Subjects were presented with the scenario that they were hired to maintain code while the chief programmer was on vacation. This required them to understand the source code of the program fully without recourse to an expert. The program they needed to understand was a Java program that solved the N-Queens problem.<sup>4</sup> A traditional programming problem was given in lieu of a web-based one, for two reasons. First, we could not identify a <sup>b</sup>classic<sup>Q</sup> web-based problem to administer to subjects. Second, to control for experimenter/subject relationships, subjects were students that were not taking a course taught by the experimenters. The experimenters, therefore, had to impose on the class time of colleagues. As web-based problems are harder to understand, the experimenters would have had to allocate more time to the experiment, thereby imposing additional burdens on colleagues and students.

The task assigned to the control group was to understand the program written in Java without the R<sup>eadable</sup> extensions. The task assigned to the treatment group was to understand the same program written in Java with the R<sup>eadable</sup> extensions. The treatment group had never previously encountered code written in the R<sup>eadable</sup> style. Therefore, they received a 1-page description of the R<sup>eadable</sup> approach prior to performing the task (shown in Appendix A.1). To reduce experimenter bias, the subjects were not given any specific training about the R<sup>eadable</sup> approach. Further details of the experiment are available at http://readable.eci.gsu.edu:8080/ examples/readableappendix.doc.

The subjects’ understanding of the programs was tested using a 20-item questionnaire, administered under examination conditions, which prevented subjects from discovering the number and type of alternate treatments, and thereby controlled for diffusion of treatments, compensatory rivalry, compensatory equalization, and resentful demoralization [21]. A demographic questionnaire (presented as Appendix A.2) was also administered to test both for equality between groups on extraneous factors, and to test for non-respondent bias. To minimize the effect of guessing, each item on the questionnaire was awarded 1, 0 or -1 points for every correct, blank, or incorrect answer, respectively. Thus, the expected value of guessing on all items was equal to t

#### 4.2. Results

Tests were performed for the successful randomization of subjects, and the impact of non-responses on the experimental design. To test for successful randomization, a post-hoc analysis was conducted to compare demographic characteristics of the subjects. Differences between age, years of work experience, years of IT experience, years of programming experience, and likelihood of participation given assignment to either the treatment or control group were evaluated using two way independent sample t-tests. Possible differences in groups due to gender and educational experience were tested using a chisquared test. No significant differences at the a V 0.05 level were found between the groups. Table 6 presents the test results.

To test for non-response bias, two-way one sample t-tests were conducted to compare characteristics of the respondent sample against known characteristics of the population of information systems students at the university. Tests were performed on gender and work experience. None of the results were significant suggesting that the sample was an accurate representation of the population being studied. The university did not collect statistics for the other demographic variables employed in the study.

One-tailed independent sample t-tests were administered to measure the results of hypotheses 1–3. A two-tailed independent sample t-test was administered to measure the result of hypothesis 4, as no direction was hypothesized. All tests were performed at the a V 0.05 level of significance and $1 - \beta \ge 0 . 8$ level of

#### 5. Discussion

We have described a novel approach called R<sup>ead-</sup> <sup>able</sup> for developing applications (especially multiparadigm applications such as those for the web). The approach facilitates communication of control flows between the developer and the maintainer, thereby simplifying program understanding. The empirical results suggest that R<sup>eadable</sup> does succeed in improving program understanding for the maintainer, thereby simplifying maintenance. The positive result for hypothesis H1 and the lack of negative results for hypotheses H2 to H4 suggest that R<sup>eadable</sup> contains the potential to be an effective approach for developing maintainable software.

Table 8  
Program understanding of R<sup>eadable</sup>—raw scores only

<table><tr><td></td><td>A1: mean (S.D.)</td><td>A2: mean (S.D.)</td><td>Effect size</td><td>t</td><td>p-value</td><td>95% Conf. interval (min)</td><td>95% Conf. interval (max)</td><td>Interpretation</td></tr><tr><td>H1</td><td>3.100 (1.410)</td><td>2.318 (1.359)</td><td>0.575</td><td>1.829</td><td>0.038</td><td>0.062</td><td>N/A</td><td>READABLE control flow is significantly easier to understand</td></tr><tr><td>H2</td><td>3.000 (1.589)</td><td>2.318 (1.323)</td><td>0.515</td><td>1.516</td><td>0.069</td><td>-0.075</td><td>N/A</td><td>READABLE program states may be significantly easier to understand</td></tr><tr><td>H3</td><td>2.800 (1.642)</td><td>2.818 (1.563)</td><td>0.012</td><td>-0.037</td><td>N/A</td><td>N/A</td><td>N/A</td><td>Data Flow is unlikely to be worse in READABLE</td></tr><tr><td>H4</td><td>3.050 (1.959)</td><td>2.591 (1.764)</td><td>0.260</td><td>0.799</td><td>0.214</td><td>-0.702</td><td>1.620</td><td>Likely that no differences can be found between the groups</td></tr></table>

The experimental R<sup>eadable</sup> approach represents a nexus of multiple theoretical bases drawn from the research streams of program understanding and software documentation. Specifically, the approach draws on Pennington’s [56] constructs and Parnas [53] and Peters and Parnas’s [58] suggestion that tabular representations can facilitate program understanding behaviors [82,83] regardless of the maintainers’ knowledge of the application domain [62,89]. The key contribution of this research is this conceptual exercise and its operationalization. The implementation we have described in this paper represents one primitive instantiation of this experimental approach for the Java programming language. This primitive implementation nevertheless demonstrates the feasibility and usefulness of our approach. Other, more elegant and sophisticated implementations using state charts or graphical interfaces can be developed. The approach developed in this paper can form the basis of further work of this nature. More efficient organization and retrieval mechanisms can be developed as well. This paper’s goal was to demonstrate the feasibility and establish potential usefulness of the R<sup>eadable</sup> approach; these extensions are, therefore, beyond the scope of the current study.

#### 6. Conclusion

The approach we have proposed for developing self-documenting and maintainable software for the web can significantly improve the practice and outcome of software created for this platform. The approach represents program components (e.g., HTML, Java Servlets) and their control-flows as tuples in a relational database. A corresponding environment uses the tuples in the relational database to execute the web application. The feasibility of the approach and environment has been demonstrated by extending Java and implementing multiple prototype applications. A limited empirical assessment of the approach has shown that R<sup>eadable</sup> facilitates program understanding. The results, thus, demonstrate that R<sup>eadable</sup> is both viable and useful for creating self-documenting web applications that promote greater program understanding, and hence become more maintainable. Our current research focuses on the application of R<sup>eadable</sup> towards developing software factories to facilitate the (semi) automatic manufacture of integrated software applications [22]. We are also studying the feasibility of integrating our approach and environment with CASE tools.

The R<sup>eadable</sup> approach provides opportunities for work in additional research streams. For example, it would be interesting to ascertain whether R<sup>eadable</sup> could be adapted successfully to other popular programmi

# Audit 14: A social route recommender mechanism for store shopping support

- Group: `retained_layer:software_system_or_artifact`
- Model decision: `True`; centrality `dominant`; layer `software_system_or_artifact`
- Gates: `{"purposeful_solution_design": true, "objective_metric_is_primary_target": true, "comparative_improvement_demonstrated": true, "objective_improvement_is_the_success_basis": true}`
- Model reason: 该文提出并实现了一个社交购物路线推荐系统（Gate 1通过）；核心成功指标是推荐路线准确率，即推荐路线与用户实际访问路线的重叠比例，且该客观指标是系统有效性评价的主要依据（Gate 2通过）；实验将全信息方法与多种消融及基线方法比较，结果显示所提方法准确率更高（Gate 3通过）；文章虽然同时报告了用户满意度等主观评分，但主要结论首先建立在客观路线准确率提升之上，主观结果处于辅助地位，因此客观改进为主导成功依据（Gate 4通过，centrality=dominant）。
- Source: `E:\github\qual-llm-check-IS-utd\database_fulltext_all\11228_2017_a-social-route-recommender-mechanism-for-store-shopping-support.md`

#### Abstract

To survive in a fiercely competitive business environment, it has become increasingly important for physical retailers to provide customers with services offering a better shopping experience. Many renovate and enlarge their shopping spaces to make their stores more enjoyable places to visit. The growth in social media and the use of mobile devices provide retailers with an opportunity to offer a context-aware guidance service to enhance customers’ in-store shopping experience. In this research, by extracting and analysing shopping information (shopping context, visiting trajectory) and social information (user’s interest, friends’ influence), a contextual store shopping recommendation system is e for first-time customers or those who are unfamiliar with a retailer’s shopping space. Our experimental results show that the proposed model is effective in providing an appropriate shopping route and enhancing users’ shopping experience, which could significantly improve the profitability and competitive advantage of the retailers.

Keywords: Social network analysis, Markov chain, Shopping context, User preference

#### 1. Introduction

In The Economist [35] Lundgren states that “It used to be catalogues killing physical stores, then it was TV shopping, and now it is online retail,” while Ryan [35] argues that brick-and-mortar shops are gravely threatened by Amazon and other online-only retailers. Amazon’s sales in 2011 were \$48 billion, compared with Macy’s \$26 billion. In 2011, online sales in America reached \$188 billion, about 8% of the total retail sales. They were forecasted to reach \$270 billion by 2015. Zaroban [46] indicates that, according to data from the U.S. Commerce Department, online sales accounted for more than half of the total retail sales growth in 2015. In recent years, retailers aiming to gain an advantage over online shopping stores have set to work on renovating their premises and enlarging their shopping space to make their stores more enjoyable places to visit. The Economist [35] reports that the shopping space per person in the U.S. increased from 18 sq. ft to 23 sq. ft in the period 1999–2009. Furthermore, in 2012 Macy’s announced that it was investing approximately \$400 million in restoring its 1.1 million sq. ft flagship store and increasing it by another 100,000 sq. ft. Such measures reflect retailers’ concern for providing customers with more comfortable places in which to shop, so that they will not feel crowded. However, emove all the barriers to an enjoyable shopping experience. According to Motorola’s survey [39], 33% of shoppers leave stores without spending because they do not obtain sufficient assistance in finding the desired products.

Fortunately, the prevalence of mobile devices and the considerable advances in network technology can greatly enhance customers’ shopping experiences. According to Nielsen [36], 78% of shoppers use their mobile devices to find the location of a store and 40% of shoppers use shopping lists on their mobile devices while shopping. In addition, customers are increasingly using their mobile devices to search for comments and review on products or stores. Clearly, providing a shopping service using mobile devices presents a great business opportunity for retailers in terms of enhancing customers’ shopping experience.

According to Bloomberg Businessweek [5], numerous companies (e.g., Google, Aisle411, IndoorAtlas) have started to provide indoor map services, enabling customers to check their location and

#### 3.1 Shopping Context Analysis Module

Customers of different ages and genders will display different shopping behaviours [18]. Furthermore, customers with different income levels will shop for different products [45]. Thus, in the proposed system, we consider the customer’s basic information to help us recognize the intrinsic shopping preferences of customer $c _ { i }$ using the following equation:

$$
\text { Gender } (c _ {i}) \in \left\{\text { male }, \text { female } \right\}, \text { Age } (c _ {i}) \in N ^ {+}, \text { Income } (c _ {i}) \in N ^ {+}.\tag{1}
$$

In general, customers will display preferences for certain time slots and days [6,40]. Therefore, in the set of individual contextual information, we also consider the time and day of shopping. We can formulate these contextual variables as follows:

Date(ci) ∈ {weekday, weekend}

(2)

$$
\operatorname{Time} \left(c _ {i}\right) \in \{\text { morning }, \text { lunch }, \text { afternoon }, \text { dinner }, \text { night } \}.\tag{3}
$$

Thus, the personal contextual information of customer $c _ { i }$ is represented as:

$$
P C \left(c _ {i}\right) = \left[ \text { Gender } (c _ {i}), \text { Age } (c _ {i}), \text { Income } (c _ {i}), \text { Date } (c _ {i}), \text { Time } (c _ {i}) \right].\tag{4}
$$

We also consider the number of customers in the store as a variable of group context because this will affect the intention of a customer to shop. Whereas some people may be attracted by a crowd, others may avoid crowded places. In this research we use the area density to represent the crowd context. Let $N S { \left( c _ { i } , r \right) }$ be the number of customers in area r of the store when customer $c _ { i }$ visits. Providing a better quantification of the density of shoppers, $N S { \big ( } c _ { i } , r { \big ) }$ excludes passing customers and customer $c _ { i }$ . The area for area r is denoted by $A r e a ( r )$ . The density context of area r visited by customer $c _ { i }$ is represented as follows:

$$
d s \left(c _ {i}, r\right) = \frac {N S \left(c _ {i} , r\right)}{\text { Area } (r)}.\tag{5}
$$

The shopping context for customer $c _ { i }$ in a space with m shopping areas is represented as:

$$
S C \left(c _ {i}\right) = \left[ d s \left(c _ {i}, 1\right), d s \left(c _ {i}, 2\right), \dots , d s \left(c _ {i}, m\right) \right].\tag{6}
$$

#### 3.2 Shopping Preference Analysis Module

In general, when customers have an interest in certain products, they will visit and spend more time in the areas in which the products are displayed. Even though customers may not put the products into their shopping bags, they will still spend time looking around these areas. Therefore, we can analyse the visiting trajectory of customers to identify their shopping preferences. We record a user’s visiting sequence of areas and the duration of stay in each area. These data are represented as $( ( r _ { 1 } , s t _ { 1 } ) , ( r _ { 2 } , s t _ { 2 } ) . . . , ( r _ { k } , s t _ { k } ) )$ , where $s t _ { k }$ is the time spent in area k and the time unit is second. Table 1 provides an example of visiting sequences with respect to different users.

Table 1 Users’ visiting sequences

<table><tr><td>User id</td><td>Visiting sequence</td></tr><tr><td>1</td><td> $((R_2,6),(R_1,10),(R_5,14),(R_6,3),(R_{10},17),(R_{16},4),(R_3,10),(R_{19},2),(R_{21},5))$ </td></tr><tr><td>2</td><td> $((R_2,3),(R_5,5),(R_{11},9),(R_{15},4),(R_{16},14))$ </td></tr><tr><td>3</td><td> $((R_3,2),(R_2,12),(R_{18},10),(R_2,9),(R_{11},5),(R_6,18))$ </td></tr><tr><td>4</td><td> $((R_2,3),(R_3,5),(R_4,8),(R_3,10),(R_{11},9),(R_{15},8),(R_{16},8),(R_{20},3))$ </td></tr><tr><td>5</td><td> $((R_2,3),(R_5,5),(R_{15},8),(R_{16},8),(R_{20},3))$ </td></tr></table>

Different customers will have different visiting sequences, which reveal their preference for certain areas. Therefore, each visited area reveals its preference value for each customer. Customers may visit the same area many times during shopping as they may think twice or change their minds. Equally, their duration of stay in different areas may represent different time units. Let us assume that there are m shopping areas arranged in the shopping mall. $V N ( c _ { i } , r )$ denotes the total number of visits by customer $c _ { i }$ to area r and $S T ( c _ { i } , r )$ denotes the sum of the duration of stay (different time units) by customer $c _ { i }$ in area $r .$ The preference level of customer $c _ { i }$ for visiting area r is measured as:

$$
s p \left(c _ {i}, r\right) = \frac {V N \left(c _ {i} , r\right) \times S T \left(c _ {i} , r\right)}{\sum_ {s = 1} ^ {m} \left(V N \left(c _ {i} , s\right) \times S T \left(c _ {i} , s\right)\right)}.\tag{7}
$$

The shopping preference for customer $c _ { i }$ is represented as:

$$
S P \left(c _ {i}\right) = \left[ s p \left(c _ {i}, 1\right), s p \left(c _ {i}, 2\right), \dots , 

#### 3.3 Social Information Analysis Module

Although retailers may not know their customers’ shopping interests from offline shopping activities, they can utilize information collected from social media to deduce these customers’ preferences for certain products. We utilize the users’ social affiliation networks [27] to predict the products in which users will have an interest and use this information to deduce the users’ preferences.

A social affiliation network can be built based on a group of users with similar tastes for products and their social relationships. For example, as shown in Figure 2, the links between users represents friendships and those with thicker lines represent greater relationship strength. A solid edge between a user and a product denotes that this user has an interest in the product. A dashed line shows that a user will potentially be interested in a product because of the social influence. If user A has an interest in product D and shares this with user B, the social influence may take effect and arouse the interest of user B. However, not all the friends of a customer have the same power to arouse interest. For example, in Figure 2 users A and C are friends of user B, but user B has a closer relationship (represented by the thicker line) with user C. If user A and user C like different products (D and E, respectively) and share their interest in these products, user B will be likely to show more interest in product E because of the stronger influence exerted by user C.

[image omitted]  
Figure 2 The social affiliation network

Therefore, we consider the closeness of social relationships to evaluate the degree of social influence that friends may exert on a customer. If two people have more friends in common, the social ties between them will be stronger [16]. Friends $( c _ { i } )$ denotes the set of friends of customer $c _ { i } .$ The weight of the closeness of the social relationship between user $c _ { i }$ and friend f is measured as:

$$
s c \left(c _ {i}, f\right) = \frac {\left| F r i e n d s \left(c _ {i}\right) \cap F r i e n d s (f) \right|}{\sum_ {b \in F r i e n d s \left(c _ {i}\right)} \left| F r i e n d s \left(c _ {i}\right) \cap F r i e n d s (b) \right|}.\tag{9}
$$

On social media, customers can join the retailer’s page and receive product information from the retailer. When customers read feeds and have an interest in or like a particular product, they will click the “Like” button to express their opinion (Wikipedia, n.d.) [44]. When customers’ fr

#### 4 Experiments

In this section, we conduct an experimental study and verify the effectiveness of the proposed framework of shopping route recommendation. We implemented the in-store shopping mechanism by developing a mobile app and invited participants to use the app in a shopping mall. The shopping information (shopping context information and visiting sequence) was manually collected from the activities during the experiments. The social information (product preference and social relationship with friends) was extracted from Facebook pages.

The experimental design and processes are described as follows. In subsection 4.1, we describe the processes of data collection. In subsection 4.2, we examine and determine the appropriate number of clusters. In subsection 4.3, we then describe the experimental processes in detail.

#### 4.3 Experimental Procedures

To evaluate the effectiveness of the proposed system, an experiment was designed to provide a route to a first-time user visiting the shopping space, so the user could receive instructions on his/her mobile device before entering the shopping space. The route comprised a blue line and red points, with the blue line representing the shopping route and the red points indicating the product areas that form the shopping route. The user could report the areas visited and the density in those areas.

The experiments were conducted using the following procedures:

(1) The participants downloaded the mobile app which is developed based on our proposed mechanism and registered.

(2) The participants were given the starting point (entrance door) and the mobile device in which

#### 5 Results and Evaluations



#### 5.1 Clustering Performance

In this section, we evaluate the performance of the proposed system. We first asked the users to users actually visited. To evaluate the effectiveness of the route recommended by the proposed mechanism further, we examined whether the areas included in the recommended route were included in the users’ routes. The more areas in the proposed route that were included in the users’ routes, the closer the proposed routes were considered to be to the users’ preferences. The accuracy of the route recommendation is measured by equation (25):

$$
A c c u r a c y = \frac {\left| \Phi_ {u s e r ^ {\prime} s r o u t e \cap p r o p o s e d r o u t e} \right|}{\left| \Phi_ {p r o p o s e d r e g i o n} \right|},\tag{25}
$$

where $\Phi _ { u s e r " s r o u t e \bigcap p r o p o s e d r o u t e }$ represents the set of areas that appear in both the user’s route and the proposed route in the same order and $\Phi _ { p r o p o s e d r e g i o n }$ is the set of areas included in the proposed route.

We compared the routes generated based on four different approaches:

(1) The first route is generated by an approach using only SI and PC information to cluster and make the route recommendation.

(2) The second route is generated by an approach using SI , PC , and SP information to cluster and make the route recommendation.

(3) The third route is generated by an approach using SI , PC , and SC information to cluster and make the route recommendation.

(4) The fourth route is generated by an approach using SI , PC , SP , and SC information to

The results are shown in Figure 7. We can observe that the accuracy of the proposed system that uses all the factors ( SI , PC , SP , and SC ) is greater than the other three approaches that only use a subset of the factors.

[image omitted]  
Figure 7 Average accuracy of the routes


# Audit 15: Designing Conversational Dashboards for Effective Use in Crisis Response

- Group: `retained_theory_driven`
- Model decision: `True`; centrality `dominant`; layer `software_system_or_artifact`
- Gates: `{"purposeful_solution_design": true, "objective_metric_is_primary_target": true, "comparative_improvement_demonstrated": true, "objective_improvement_is_the_success_basis": true}`
- Model reason: 该文明确设计并实现了会话式危机响应仪表盘这一IS解决方案（Gate 1通过）；核心成功标准是客观度量的透明交互、效率和有效性，NLP性能作为技术支持性指标，而自评自我效能仅作为操纵检验（Gate 2通过）；用户实验直接比较了不同仪表盘类型和有无onboarding的条件，并报告了显著的客观改进，NLP性能也与相关系统基准比较（Gate 3通过）；文章结论和设计理论主要依据客观行为指标的改进，主观指标不构成成功判据（Gate 4通过）。因此，严格客观改进匹配为真，中心性为dominant。
- Source: `E:\github\qual-llm-check-IS-utd\database_fulltext_all\13598_2023_designing-conversational-dashboards-for-effective-use-in-crisis-response.md`

#### Abstract

Governments and health organizations are increasingly using dashboards to provide real-time information during natural disasters and pandemics. Although these dashboards aim to make crisisrelated information accessible to the general public, the average user can have a hard time interacting with them and finding the information needed to make everyday decisions. To address this challenge, we draw on the theory of effective use to propose a theory-driven design for conversational dashboards intended for crisis response that can improve users’ transparent interaction with these dashboards and facilitate access to crisis-related information during crises. We instantiate our proposed design in a conversational dashboard for the COVID-19 pandemic that enables natural language interaction in spoken or written form and helps users familiarize themselves with the use of natural language through conversational onboarding. The evaluation of our artifact shows that being able to use natural language improves users’ interaction with the dashboard and ultimately increases their efficiency and effectiveness in finding information. This positive effect is amplified when users complete the onboarding before interacting with the dashboard, particularly when they can use both natural language and mouse interaction. Our findings contribute to research on dashboard design, both in general and in the specific context of crisis response, by providing prescriptive knowledge for extending crisis response dashboards with natural language interaction capabilities. In addition, our work contributes to the democratization of data science by proposing design guidelines for making information on crisis response dashboards more accessible to the general public.

Keywords: Dashboard, Conversational User Interface, Crisis Response, Design Science Research, Theory of Effective Use

Roger Chiang, Ahmed Abbasi, and Jennifer Xu were the accepting senior editors. This research article was submitted on April 15, 2021 and underwent two revisions. This paper is part of the Special Issue on Data Science for Social Good.

#### 1 Introduction

By nature, crises are unpredictable, sudden, and often chaotic situations. When a crisis occurs, people want to find accurate and up-to-date information quickly so that they can make the best decisions for themselves, their families, and their communities (Leong et al., 2015). To satisfy information needs, governments and health organizations are increasingly relying on crisis response dashboards. Similar to business intelligence (BI) dashboards designed to support decision makers in organizations (Abbasi et al., 2016), crisis response dashboards are designed to provide citizens with key information about the current state of a crisis. As such, these data science artifacts primarily aim to democratize data science by making complex data accessible to the general public (Koch, 2021; Matheus et al., 2020). While crisis response dashboards have previously been developed for earthquakes (Zook et al., 2010), wildfires (Liu & Palen, 2010), and virus outbreaks (Cheng et al., 2011), they took center stage during the COVID-19 pandemic (Pietz et al., 2020). For example, the dashboard provided by Johns Hopkins University received more than a billion hits per day during the height of the pandemic (Gardner et al., 2021). COVID-19 dashboards served not only as a primary source of information about cases, deaths, and other key metrics for the general public, but were also frequently used to guide everyday decision-making (e.g., about visiting a friend or getting a haircut) (Flowers, 2020).

Both researchers and practitioners share the assumption that COVID-19 dashboards were highly effective in helping billions of users find the information they needed quickly, as long as the underlying data was accurate and the visualizations were interactive (Patino, 2021; Soper et al., 2021). However, while the reported numbers of daily dashboard users certainly look impressive, we know from the literature that to achieve their goals, people must use information systems (IS) effectively—rather than just using them (Burton-Jones & Grange, 2013). The fundamental dimension of effective use is transparent interaction, which describes how well users can access information from an IS unimpeded by its physical and surface structures (e.g., the user interface) (Burton-Jones & Grange, 2013). If users are unable to interact with a dashboard transparently, they are unlikely to find the information they need and make good decisions (e.g., about wearing a mask in regions with increasing case numbe

#### 4 Evaluation

We performed two evaluations of our artifact. First, we conducted a performance evaluation of its key technical component to assess whether it enables effective natural language interaction in spoken and written form. Second, we carried out an experimental study to test whether our proposed design can improve users’ transparent interaction with a crisis response dashboard.

#### 4.1 Performance Evaluation of the Natural Language Processing (NLP) Component

At the heart of our artifact is an NLP component that allows the conversational dashboard to understand and act on the user’s natural language input. To assess the NLP component’s quality, we conducted a performance evaluation that specifically focused on speech-to-text translation, entity extraction, and intent mapping. For the evaluation, we used the dataset of 3119 natural language inputs collected in our user evaluation (see Section 4.2 for details). Initially, this dataset only included natural language input used to navigate the dashboard (e.g., “Show me Idaho August 31st”) and the corresponding results provided by the NLP component (e.g., intent = “filter,” entities = “Idaho” and “August 31”). Since no ground truth was available in the dataset for the evaluation, we recruited 264 crowd workers on Amazon Mechanical Turk to obtain ground truth labels for each natural language input. Additionally, we instructed workers to highlight if they recognized an input as syntactically incorrect or if there were misunderstandings (e.g., “soon out” instead of “zoom out”). Each input was labeled by two workers who had a moderate level of agreement (Cohen’s kappa = 0.52). To break ties in cases of disagreement, a research assistant who received the same instructions and explanations reviewed each input with a disagreement between the workers and assigned a final label. The final dataset included 3119 natural language inputs, results of the NLP component, and human ground-truth labels for speech-to-text, entities, and intents.

#### 4.1.1 Performance Measures

We used established measures to evaluate the performance of the NLP component. First, to verify the speech-to-text translation quality for all spoken input, we used the binary label that specified whether a particular input was syntactically correct. Based on our labeled dataset, we calculated the accuracy of speechto-text translation as the ratio of correctly translated spoken inputs to the total number of spoken inputs. Second, to evaluate the entity extraction and intent mapping performance, we compared the results provided by our NLP component against the intent and entity labels that human workers provided. We used standard classification measures that have been used in similar work (e.g., Siering et al., 2021)—that is, precision, recall, and the F1-score—and calculated them through microaveraging the classes (i.e., intent or entity). Precision measures the percentage of correctly classified instances (i.e., intents and entities) to the total number of instances for that class of instances retrieved by the intent mapping or entity extraction $\begin{array} { r } { ( P r e c i s i o n = \frac { T P } { T P + F P } ) } \end{array}$ . Recall measures the percentage of correctly classified instances among all true positive cases of that class of instances $\begin{array} { r } { ( R e c a l l = \frac { T P ^ { - } } { T P + F N } ) } \end{array}$ . The F1-score is calculated as the weighted average of precision and recall $\begin{array} { r } { ( \ F 1 = 2 * \overbrace { \frac { P r e c i s i o n * R e c a l l } { P r e c i s i o n + R e c a l l } } ^ { P r e c i s i o n * R e c a l l } \ ) } \end{array}$ Further, to benchmark our intent mapping against related systems (Srinivasan & Stasko, 2018), we additionally calculated the accuracy as the number of correctly classified inputs divided by the total number of inputs $\begin{array} { r } { ( A c c u r a c y = \frac { T P + T N } { T P + F P + F N + T N } ) . } \end{array}$

#### 4.1.2 Results

Speech-to-text: Out of a total of 3119 natural language inputs, 2499 (80.1%) were performed using spoken language. For these spoken inputs, we calculated an overall speech-to-text accuracy of 90.2%. This means that 9.8% of the spoken input included syntactical errors that could have negatively affected the subsequent entity extraction and intent mapping steps. For example, the word “cases” was incorrectly translated to “kisses” several times, resulting in user input that missed the metric “cases.” However, the overall accuracy of more than 90% indicates that our speech-to-text translation was able to achieve a good performance.

Entity extraction: For the analysis of the entity extraction performance, we used all 3119 spoken and written inputs made by users, including those labeled as syntactically incorrect. Based on the F1-scores shown in Table 3, entity extraction worked the best for dates (95%) and states (94%). In contrast, entity extraction yielded a lower F1-score of 83% for the entity “metric.” One reason for the lower performance of this entity is that the phrase “people had died” was used to describe “deaths,” which was not included in the training data for this entity. Overall, the entity extraction step achieved an F1-score of 92%. Moreover, the results show that our entity extraction performed equally well for spoken (91%) and written input (93%). Table 3 provides the overall and entitylevel precision and recall measures.

Intent mapping: The final step of the analysis was to evaluate the intent mapping performance. Again, we used all 3119 natural language inputs, including those labeled as syntactically incorrect. Only 98 inputs (3.1%) were labeled as fallback (i.e., not supported input). Overall, our intent mapping achieved a high accuracy of 82%, demonstrating comparable or better performance than related systems that offer natural language interaction with data visualizations (e.g., Srinivasan & Stasko, 2018). Additionally, the results show that our intent mapping performed equally well for spoken (83%) and written input (79%). The slight differences can be partially explained by spelling mistakes, such as “Select ketncuky,” which mainly occurred in written input. In sum, our intent mapping achieved a high overall F1-score of 82% on the unbalanced dataset. While our main intents performed well, the fallback intent achieved a lower precision level (20%) because it included user input with errors from incorrect speech-to-text translation. Fu

#### 4.2 User Evaluation

To evaluate whether our proposed design can improve users’ transparent interaction with a crisis response dashboard, we conducted a large-scale online experiment. Following the approach of Morana et al. (2019), we developed six versions of our artifact with different combinations of instantiated DPs to examine their effect on transparent interaction. More specifically, we compared a traditional dashboard (TDB) with two types of conversational dashboards: natural language-only (CDB-NLO) and natural language-enhanced (CDB-NLE). As Table 4 shows, the CDB-NLO instantiated only DP1, whereas the CDB-NLE instantiated both DP1 and DP2. TDB did not instantiate these DPs to establish a baseline condition representing the current design of crisis response dashboards. Further, we developed two different versions of each dashboard with and without conversational and/or traditional onboarding (DP3) depending on the respective dashboard type, resulting in a total of six different dashboards.

Against the backdrop of these different artifact instantiations, we translated our previously derived design propositions (see Section 3.4) into four specific hypotheses that we empirically tested in the experiment. According to our first proposition, a crisis response dashboard equipped with a CUI should improve transparent interaction because it allows users to interact with the dashboard using spoken or written language in a natural way. Based on this proposition, we argue that users will achieve higher levels of transparent interaction with a conversational dashboard than with a traditional dashboard, regardless of whether natural language interaction replaces existing ways of interacting with a dashboard using the mouse (CDB-NLO) or whether it complements them (CDB-NLE). Hence, we hypothesize:

H1-H2: Users who interact with a natural language-only conversational dashboard (CDB-NLO; H1) or a natural language-enhanced conversational dashboard (CDB-NLE; H2) achieve higher levels of transparent interaction than those interacting with a traditional dashboard (TDB).

According to our second proposition, a conversational crisis response dashboard equipped with conversational onboarding should improve transparent interaction because it facilitates users’ learning by walking them through the natural language interaction with the dashboard. Therefore, based on our second proposition, we argue that users of conversational dashboards, regardless of whether natural language interaction rep

#### 4.2.1 Method

To test our hypotheses, we conducted an online experiment in which participants interacted with one of the six dashboards to perform four information-finding tasks. The experiment used a 3 (dashboard type: TDB vs. CDB-NLO vs. CDB-NLE) × 2 (onboarding: absent vs. present) between-subjects design, resulting in six experimental conditions.

Experimental procedure: Participants accessed the experiment via a link provided on Amazon Mechanical Turk (Mturk). After reading a short description and providing informed consent, participants were randomly assigned to one of the six experimental conditions. In the first step, participants were instructed to test their microphones to ensure that they would be able to use natural language in spoken form during the experiment and that there was only minimal background noise. Only if the system was able to understand them correctly, could they continue with the experiment. Next, participants watched a 50-second video that provided an overview of the dashboard and its COVID-19 data visualizations. After watching the video, participants in the three conditions without onboarding immediately entered the main part of the experiment. In contrast, participants in the other three conditions first completed the onboarding 

# Audit 16: Representing Part-Whole Relations in Conceptual Modeling: An Empirical Evaluation

- Group: `retained_theory_driven`
- Model decision: `True`; centrality `dominant`; layer `interface_or_interaction_design`
- Gates: `{"purposeful_solution_design": true, "objective_metric_is_primary_target": true, "comparative_improvement_demonstrated": true, "objective_improvement_is_the_success_basis": true}`
- Model reason: 四个门均通过：作者设计并比较了概念模型中复合物的两种信息表示方式（实体/类 vs 关系/关联），以问题求解准确率这一客观评分的任务绩效作为主要成功标准；实验证明ontologically clear表示显著提高准确率（大效应量），时间和感知易用性仅为辅助且不显著，因此客观改进是主要成功依据。中心性为dominant。
- Source: `E:\github\qual-llm-check-IS-utd\database_fulltext_all\06360_2008_representing-part-whole-relations-in-conceptual-modeling-an-empirical-evaluation.md`

### REPRESENTING PART-WHOLE RELATIONS IN CONCEPTUAL MODELING: AN EMPIRICAL EVALUATION $^{1}$

By: Graeme Shanks
Department of Information Systems
University of Melbourne
Parkville, Victoria 3052
AUSTRALIA
gshanks@unimelb.edu.au

Elizabeth Tansley
School of Computing Sciences
Central Queensland University
Rockhampton, Queensland 4702
AUSTRALIA
e.tansley@cqu.edu.au

Jasmina Nuredini
Simsion and Associates
131-135 Gore Street
Fitzroy, Victoria 3065
AUSTRALIA
jasminan@optusnet.com.au

Daniel Tobin
Marketing and Communications
University of Melbourne
Parkville, Victoria 3052
AUSTRALIA
dtobin@unimelb.edu.au

Ron Weber
Faculty of Information Technology
Monash University
Caufield East, Victoria 3145
AUSTRALIA
ron.weber@infotech.monash.edu.au

## Abstract

The part-of construct is a fundamental element of many conceptual modeling grammars that is used to associate one thing (a component) with another thing (a composite). Substantive theoretical issues surrounding the part-of construct remain to be resolved, however. For instance, contrary to widespread claims, some researchers now argue the relationship between components and composites is not always transitive. Moreover, how the part-of construct should be represented in a conceptual schema diagram remains a contentious issue. Some analysts argue composites should be represented as a relationship or association. Others argue they should be represented as an entity. In this paper we use an ontological theory to support our arguments that composites should be represented as entities and not relationships or associations. We also describe an experiment that we undertook to test whether representing composites as relationships or entities enables users to understand a domain better. Our results support our arguments that using entities to represent composites enables users to better understand a domain.

Keywords: Conceptual modeling, information systems development, ontology, part-of relations, aggregation, composition, meronymic relations, mereology, mereotopology

## Introduction

The notion that one thing may be a “part of” or a “component of” another thing (e.g., a wheel is part of a car) seems fundamental to the way humans conceive some types of phenomena in the perceptual worlds they create. For this reason, part-whole (meronymic) relations have been a focus of psychologists concerned with human cognition (e.g., Winston et al. 1987) and philosophers concerned with ontology (the nature of the world) (e.g., Bunge 1977). Indeed, within the field of philosophy, part-whole relations are the primary focus of 

#### Abstract

The part-of construct is a fundamental element of many conceptual modeling grammars that is used to associate one thing (a component) with another thing (a composite). Substantive theoretical issues surrounding the part-of construct remain to be resolved, however. For instance, contrary to widespread claims, some researchers now argue the relationship between components and composites is not always transitive. Moreover, how the part-of construct should be represented in a conceptual schema diagram remains a contentious issue. Some analysts argue composites should be represented as a relationship or association. Others argue they should be represented as an entity. In this paper we use an ontological theory to support our arguments that composites should be represented as entities and not relationships or associations. We also describe an experiment that we undertook to test whether representing composites as relationships or entities enables users to understand a domain better. Our results support our arguments that using entities to represent composites enables users to better understand a domain.

Keywords: Conceptual modeling, information systems development, ontology, part-of relations, aggregation, composition, meronymic relations, mereology, mereotopology

#### Introduction

The notion that one thing may be a “part of” or a “component of” another thing (e.g., a wheel is part of a car) seems fundamental to the way humans conceive some types of phenomena in the perceptual worlds they create. For this reason, part-whole (meronymic) relations have been a focus of psychologists concerned with human cognition (e.g., Winston et al. 1987) and philosophers concerned with ontology (the nature of the world) (e.g., Bunge 1977). Indeed, within the field of philosophy, part-whole relations are the primary focus of the subfields of mereology and mereotopology (e.g., Gerstl and Pribbenow 1996; Simons 1987; Smith 1996; Varzi 1996). Moreover, recently philosophers also have begun to focus specifically on the mereology of artifacts (Simons and Dement 1996).

Part-whole relations also have long been a concern of information systems and computer science researchers and practitioners concerned with finding better ways to model the world. For instance, they feature in early work on “database abstractions” (Smith and Smith 1977) and extensions to Chen’s (1976) entity-relationship model (Teorey et al. 1986). Subsequent to this early work, they have remained a focus of researchers concerned with conceptual modeling (e.g., Storey 1991). More recently, part-whole relations feature in object-oriented conceptual modeling approaches (e.g., Artale et al. 1996, Opdahl et al. 2001)—in particular, the de facto standard for object-oriented conceptual modeling, the unified modeling language (UML) (Rumbaugh et al. 2005).

In the context of conceptual modeling work, part-whole relations remain problematical for two reasons. First, substantive theoretical issues surrounding them remain unresolved. For example, Rumbaugh et al. (2005, p. 164) state: "The aggregation (part-whole) relationship is transitive and antisymmetric across all aggregation links, even across those from different aggregation associations." Winston et al. (1987, pp. 431-432) illustrate the difficulties with such claims using the following example: If Simpson's arm is a part of Simpson, and Simpson is a part of the Philosophy Department, by transitivity Simpson's arm is a part of the Philosophy Department. They point out that the validity of this conclusion is questionable because "part of" has two different meanings in their example. One is a component-object relation (arm is a part of Simpson). The other is a member-collection relation (Simpson is a part of the Philosophy Department). Moreover, W

#### Research Method

To test our proposition, we chose an experiment so that we could control extraneous factors that might confound any impacts of alternative representations of part-whole relations on how well users understand these relations.

#### Results

Our data analysis involved four steps. First, we calculated scores for individual items on the problem-solving measure. Second, we performed reliability analyses on the problem-solving and ease-of-use measures. Third, we performed statistical analyses to test for treatment differences in the scores for the problem-solving, time, and ease-of-use measures. Fourth, we analyzed the qualitative data we had collected to better understand how the two treatment groups differed in terms of their performance on the problem-solving tasks.

#### Quantitative Data Analysis

Table 2 shows descriptive statistics for the total accuracy, total time, and ease-of-use measures. Because the total accuracy and total time scores for the 11 problem-solving questions are relatively uncorrelated (r = -.216, p = .251), we used an independent samples multivariate t-test to compare the performance of the ontologically clear and ontologically unclear treatment groups rather than multivariate analysis of variance (Tabachnick and Fidell 1996, p. 402). For all three dependent measures, Levene's test indicated that the variances of the ontologically clear and ontologically unclear groups could be considered to be the same.

For problem-solving accuracy, the difference between the two groups was statistically significant using a two-tailed multivariate t-test (t = 7.465, df = 28, p < .001). $^{15}$ Eta squared was .666, which means that 66.7 percent of the variance in problem-solving accuracy is accounted for by the treatment. For the problem-solving time performance measure, however, the difference between the ontologically clear and ontologically unclear groups was not significant using a two-tailed test $t = -1.166, df = 28, p = .253$ . Similarly, for the ease-of-use measure, the difference between the two groups was not statistically significant using a two-tailed test $t = 0.371, df = 28, p = .713$ .

Table 2. Descriptive Statistics for Dependent Measures

<table><tr><td>Group</td><td>Measure</td><td>Mean</td><td>Std. Dev.</td><td>Skewness</td><td>Kurtosis</td></tr><tr><td rowspan="3">Ontologically Clear (n = 15)</td><td>Problem Solving</td><td>24.533</td><td>6.022</td><td>-0.44</td><td>-0.481</td></tr><tr><td>Time</td><td>33.244</td><td>11.464</td><td>0.089</td><td>-1.534</td></tr><tr><td>Ease of Use</td><td>8.94</td><td>2.417</td><td>-0.242</td><td>0.175</td></tr><tr><td rowspan="3">Ontologically Unclear (n = 15)</td><td>Problem Solving</td><td>10.7</td><td>3.904</td><td>-0.159</td><td>0.52</td></tr><tr><td>Time</td><td>38.989</td><td>15.258</td><td>0.896</td><td>1.587</td></tr><tr><td>Ease of Use</td><td>8.56</td><td>3.143</td><td>-0.049</td><td>-0.962</td></tr><tr><td rowspan="3">Total (n = 30)</td><td>Problem Solving</td><td>17.617</td><td>8.623</td><td>0.278</td><td>-1.074</td></tr><tr><td>Time</td><td>36.117</td><td>13.578</td><td>0.774</td><td>1.246</td></tr><tr><td>Ease of Use</td><td>8.75</td><td>2.761</td><td>-0.161</td><td>-0.604</td></tr></table>

To identify how the two groups differed in terms of problem-solving accuracy, follo

#### Qualitative Data Analysis

A qualitative analysis of the data was undertaken to obtain insights that we could not obtain via the quantitative analysis about the effect of the treatment. Recall, each participant's verbalizations were tape-recorded. Moreover, we took notes of participants' reactions and responses to the experimental materials. Our goal was to obtain a deeper understanding of participants' thought processes as they attempted to answer the problem-solving questions.

As a first step in analyzing the transcriptions and notes, we derived iteratively a set of problem-solving phases that we concluded participants would most likely traverse as they attempted to answer the problem-solving questions. In essence, we employed a model-based approach to verbal protocol analysis. Following Ericsson and Simon (1993, pp. 198-199), we formulated a tentative model, evaluated it against participant protocols and our notes, and then refined the model until we concluded the model's phases provided a comprehensive and useful way of categorizing those verbalizations in the participant protocols that interested us. By first articulating this model, we could then identify and code specific verbalizations that we believed were pertinent to testing our proposition.

The seven problem-solving phases we used as the basis for our coding were

\- Phase 1: Can I understand the question asked/problem posed?

\- Phase 2: What are the key real-world concepts in the question asked/problem posed?

<table><tr><td colspan="4">Table 3. Accuracy Performance on Problem-Solving Questions</td></tr><tr><td rowspan="2">Question</td><td>Ontologically Clear(n = 15)</td><td>Ontologically Unclear(n = 15)</td><td rowspan="2">t-Statistic(2-tail Significance)</td></tr><tr><td>Mean(Standard Deviation)</td><td>Mean(Standard Deviation)</td></tr><tr><td>1</td><td>2.467(1.077)</td><td>0.933(1.033)</td><td>3.980(.000)</td></tr><tr><td>2</td><td>1.500(1.309)</td><td>0.467(1.060)</td><td>2.376.025</td></tr><tr><td>3</td><td>2.100(1.137)</td><td>0.200(0.561)</td><td>5.805(.000)</td></tr><tr><td>4</td><td>2.233(1.208)</td><td>2.100(1.242)</td><td>0.298(.768)</td></tr><tr><td>5</td><td>2.667(0.990)</td><td>0.400(0.910)</td><td>6.859(.000)</td></tr><tr><td>6</td><td>2.400(1.121)</td><td>0.333(0.617)</td><td>6.254(.000)</td></tr><tr><td>7</td><td>2.367(1.043)</td><td>1.033(0.935)</td><td>3.687(.001)</td></tr><tr><td>8</td><td>1.900(1.256)</td><td>1.000(0.926)</td><td>2.233(.034)</td></tr><tr><td>9</td><td>2.467(1.126)</td><td>0.400(

#### Implications of the Research

Our results have implications for practice and research. For practice, we believe we have strong support for our proposition that composites should be modeled as an entity or class and not as a relationship or an association. When composites are modeled as an entity or class, the resulting diagram is syntactically more complex because it contains more elements. In the context of problem-solving, however, our results suggest that the additional semantics contained in an ontologically clear diagram overcome the disadvantages associated with its higher syntactic complexity. We recommend, therefore, that practitioners be especially circumspect if they model composites as relationships or associations. They run the risk that they will undermine users' understanding of the real-world phenomena that a conceptual schema diagram is intended to represent. Syntactically simpler conceptual schema diagrams might be useful if the goal is to give users a surface-level understanding of a domain. Where a deep-level understanding of a domain is needed, however, our results support the notion that ontologically clear diagrams are essential (Bodart et al. 2001; Gemino and Wand 2005).

Our results also suggest a way in which information systems practitioners might validate the conceptual models they create. To date, little guidance has been provided on how this task should be undertaken. A typical suggestion is that users should simply be asked to examine conceptual models and provide feedback. Unless users engage fully with a conceptual model, however, they are unlikely to identify errors, omissions, redundancies, or ambiguities. Our results support those obtained by Gemino and Wand (2005) and Bodart et al. (2001) on the efficacy of problem-solving tasks as a means of testing how well conceptual models communicate the semantics of a domain to users. Thus, asking users to validate a conceptual model by requiring them to solve problems using the model (use-cases in UML) seems a fruitful way to proceed. Other approaches, such as asking users to recall models, answer comprehension questions about models, and verify models against user requirement statements, seem less efficacious (e.g., Bodart et al. 2001).

In terms of research, our results add strength to a growing body of empirical work that supports the usefulness of ontological theories, especially Bunge's (1977) theory, as a means of predicting the strengths and weaknesses of conceptual modeling grammars and practices (e.g.


# Audit 17: Designing Promotional Incentives to Embrace Social Sharing: Evidence from Field and Online Experiments

- Group: `retained_theory_driven`
- Model decision: `True`; centrality `dominant`; layer `digital_platform_mechanism_or_policy`
- Gates: `{"purposeful_solution_design": true, "objective_metric_is_primary_target": true, "comparative_improvement_demonstrated": true, "objective_improvement_is_the_success_basis": true}`
- Model reason: 文章设计并测试了数字平台上的促销激励机制（可分享性、稀缺性/数量），属于有意的 IS 相关方案设计；主要成功判据是发送者购买概率、成功推荐概率、短期净收入和长期 CLV 等客观行为/经济指标，并提供了与提醒组、hold-out 组及各处理组相比的显著改进证据。在线实验中的感知排他性和社交动机是解释机制，处于从属地位，因此客观指标改进是主导成功依据。四个门槛均通过，保留为 strict_objective_improvement_match=true。
- Source: `E:\github\qual-llm-check-IS-utd\database_fulltext_all\01090_2021_designing-promotional-incentives-to-embrace-social-sharing-evidence-from-field-and-online-experi.md`

### DESIGNING PROMOTIONAL INCENTIVES TO EMBRACE SOCIAL SHARING: EVIDENCE FROM FIELD AND ONLINE EXPERIMENTS<sup>1</sup>

Tianshu Sun Marshall School of Business, University of Southern California Los Angeles, CA, U.S.A. {tianshus@marshall.usc.edu}

Siva Viswanathan Robert H. Smith School of Business, University of Maryland College Park, MD, U.S.A. {sviswana@rhsmith.umd.edu}

Ni Huang C. T. Bauer College of Business, University of Houston Houston, TX, U.S.A. {nhuang5@uh.edu}

Elena Zheleva Department of Computer Science, University of Illinois at Chicago Chicago, IL, U.S.A. {ezheleva@uic.edu}

Despite the increasing connectivity between consumers and the large volume of social shares supported by digital technologies, there is an absence of research systematically investigating how firms can design promotional incentives that jointly consider their consumers as both purchasers and sharers. In this study, we examine whether and how firms can leverage consumers’ social connections and engage consumers to share promotional incentives. In collaboration with a leading online deal platform, we report a large-scale randomized field experiment to test the effectiveness of different incentive designs (varying in the shareability and scarcity of promotion codes) in driving social sharing senders’ purchases and successful referrals. We find that the different incentive designs have distinct impacts on the purchase and referral outcomes. Specifically, providing senders with one non-shareable promo code significantly increases their own purchase likelihood, compared to the other experimental groups. In contrast, senders who receive one shareable promo code are less likely to purchase themselves yet are more likely to make successful referrals. Surprisingly, the incentive design with two promo codes containing one non-shareable code and one shareable code increases neither the senders’ purchases nor their successful referrals. Managerially, we estimate that although the one nonshareable promo code group derives the highest net revenue for the experimental period, the one shareable promo code group derives the highest customer lifetime value for the firm from the new customers acquired through the successful referrals. We further conducted two online experiments on Amazon Mechanical Turk that replicate the field experiment’s findings and explore the underlying mechanisms of the observed relationships. We find that exclusivity perception and social motives triggered by the incentive designs with one promo code mediate their effects on senders’ self-purchases and successful referrals, respect

#### Introduction

Developments in information technologies have significantly boosted the prevalence of social sharing by making it convenient for consumers to disseminate digital information within their social connections (Gerlitz and Helmond 2013; Nielsen 2016). Recognizing this opportunity, major online retailers and e-commerce platforms such as Amazon and Groupon have integrated social features and channels on their product pages to facilitate the effortless sharing of commercial information (Huang et al. 2018). While the direct impact of social sharing has been extensively studied in prior literature (Godes and Mayzlin 2009; Gu et al. 2012; Susarla et al. 2012; Yin et al. 2014, 2016; Geva et al. 2019), there is limited research on how firms can design promotional incentives to leverage ITenabled social sharing. <sup>2</sup> For instance, many firms still follow traditional ways of designing promotions that focus on isolated purchase decisions of individual consumers without considering the new opportunities derived from social sharing among consumers. Similarly, despite extensive research attention on the role of firms as observers and moderators of online social sharing and word-of-mouth (e.g., Godes et al. 2005, Berger 2014), there is surprisingly little understanding on how firms can embrace social sharing to improve on their influence in actively engaging with potential customers via promotional incentives. Given the increasing connectivity among consumers and the low cost of social sharing enabled by digital technologies, it is paramount for firms to revisit their current promotional strategies in the social media era. Keeping the above in mind, our study aims to address the following research questions:

Should firms engage consumers as isolated and independent purchasers, or as both purchasers and sharers that are interconnected to each other?

• How can firms design incentives differently to engage their consumers across both roles?

What are the mechanisms underlying the effectiveness of such incentive designs?

Considering the dual roles of consumers as purchasers and sharers in social sharing, we propose that firms can design incentives along two dimensions: shareability and scarcity. Prior research on IT-enabled social sharing has primarily focused on the sharing of information among consumers (Ryu and Feick 2007; Hong et al. 2017) and the consequences of such actions (e.g., Godes and

Mayzlin 2004; Gu et al. 2012; Susarla et al. 2012). However, past work 

#### Field and Online Experiments



#### Study 1: Randomized Field Experiment

In Study 1, we designed and implemented a randomized field experiment in collaboration with a leading online deal platform (hereafter referred to as our partner platform) to examine the causal impact of different incentive designs that vary in shareability and scarcity, on consumers’ own purchases and their successful referrals. The partner platform, similar to Groupon.com, offers a wide variety of limited-time deals at relatively high discount rates, including travel, events, dining, and products, and has attracted a substantial customer base in the market space. Users of the platform can directly purchase a deal through the deal page or share the deal with their social connections using the social sharing feature on the deal pages. Social sharing can occur either before or after purchase when users click the prominently displayed sharing buttons on the webpage to share the deals. Each social share action only includes one specific deal. Although a considerable number of social shares are made on the partner platform every day, only a small percentage of the shares lead to purchases.

#### Experimental Design

Our field experiment employed a between-subjects design. In particular, we focused on the organic social sharing senders who had shared any deal with their social connections in the past 24 hours but did not end up purchasing the shared deal themselves.<sup>10</sup> We randomly assigned the eligible subjects (i.e., original deal senders) into one of the five experimental groups, as presented in Table 1 below. The experimental manipulation was performed at the sender level. The platform observed the senders’ own purchases as well as their successful referrals (i.e., others’ purchases attributed to the sender’s sharing of the deal).<sup>11</sup> Notably, we delivered unique and personalized promo code(s) for each sender in the treatment groups, which enabled us to accurately track both a sender’s purchase and any successful referrals.<sup>12</sup>

#### Results

We begin with reporting the graphical evidence and the mean comparisons by experimental groups for our outcome of interests. Figure 5 presents the bar graphs of the average likelihood of purchase and the average probability of successful referral across experimental groups. The error bars in the graphs reflect the 95% confidence intervals. We also report the results of t-tests with the group mean comparisons in Table 2 and Table 3. Overall, we find that different incentive designs significantly influence the senders’ own purchase likelihood and senders’ successful referral, but in distinct ways. To begin with, we observe a significant greater likelihood of senders’ purchase in the one non-shareable promo code group $( M _ { \mathrm { o n e n o n - s h a r e a b l e p r o m o c o d e } } = 0 . 0 6 6 )$ , relative to the simple reminder group $( M _ { \mathrm { { s i m p l e r e m i n d e r } } } = 0 . 0 4 9 ; t = 3 . 4 7 0 , p$ $= 0 . 0 0 1 )$ , to the one shareable promo code group (M<sub>one</sub> <sub>shareable</sub> $\mathrm { p r o m o c o d e } = 0 . 0 5 6 ; t = - 2 . 0 8 0 , p = 0 . 0 3 8 )$ , and to the two promo codes group $( M _ { \mathrm { t w o c o d e s } } = 0 . 0 5 4 ; t = - 2 . 4 8 0 , p = 0 . 0 1 3 ) .$ . Thus, H1a and H2a are supported but H3a is not supported. Next, we find that the sender’s probability of successful referral is significantly higher in the one shareable promo code group $( M _ { \mathrm { o n e } }$ shareable promo $_ \mathrm { c o d e } ~ = ~ 0 . 0 3 6 )$ , compared to the simple reminder group $( M _ { \mathrm { { s i m p l e r e m i n d e r } } } = 0 . 0 2 5 ; t = 2 . 9 4 0 , p = 0 . 0 0 3 )$ to the one non-shareable promo code group (M<sub>one</sub> <sub>non-shareable</sub> $\mathtt { p r o m o c o d e } = 0 . 0 2 8 ; t = 1 . 9 9 0 , p = 0 . 0 4 7 )$ , and to the two promo codes group $( \mathbf { M } _ { \mathrm { t w o ~ c o d e s } } = 0 . 0 2 9 ; \ t = - 1 . 8 8 0 , \ p = 0 . 0 6 0 )$ Meanwhile, the sender’s successful referral in the one nonshareable code group does not significantly differ from that in the control group $( p \ : = \ : 0 . 3 3 7 )$ . Thus, H1b are H2b are supported; however, H3b is not supported.

We next present the estimations on the average treatment effects using regressions, which could produce the estimates with higher precision than pairwise t-tests (Duflo et al. 2007). Since our outcome variables are binary in nature, we employ both a linear probability model (LPM) and a logistic or prob

#### Discussion: Study 1

The principal advantage of the field experiment (Study 1) is the direct manipulation of the incentive designs and the granular observation of real-life purchase as well as referral outcomes in the field setting. In Study 1, we found evidence on the effectiveness of one non-shareable promo code and one shareable promo code in elevating senders’ likelihood of purchase and successful referral, supporting H1a, b, and H2a, b. Meanwhile, contrary to hypotheses H3a and H3b, our field experiment shows that the incentive design with two promo codes in Treatment 3 does not lead to more purchases or referrals as compared to the design with one shareable code in Treatment 2.

<table><tr><td colspan="4">Table 6. Average Treatment Effects (DV = Short-Term Overall Purchase Volume)</td></tr><tr><td>Variables</td><td>(1) LPM</td><td>(2) FE LPM</td><td>(3) FE LPM</td></tr><tr><td>Hold-out</td><td>-0.009(0.007)</td><td>-0.009(0.005)</td><td>-0.008(0.004)</td></tr><tr><td>One non-shareable promo code</td><td>0.021**(0.007)</td><td>0.021*(0.006)</td><td>0.021*(0.006)</td></tr><tr><td>One shareable promo code</td><td>0.018**(0.007)</td><td>0.018*(0.005)</td><td>0.017*(0.006)</td></tr><tr><td>Two promo codes</td><td>0.009(0.007)</td><td>0.009*(0.003)</td><td>0.009*(0.003)</td></tr><tr><td>Constant</td><td>0.074***(0.005)</td><td>0.074***(0.002)</td><td>0.311(0.296)</td></tr><tr><td>Observations</td><td>20,375</td><td>20,375</td><td>20,375</td></tr><tr><td>F statistics</td><td>6.62***</td><td>21.09***</td><td>--</td></tr><tr><td>R-squared</td><td>0.001</td><td>0.001</td><td>0.006</td></tr><tr><td>Category fixed effect</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>Time fixed effect</td><td>No</td><td>No</td><td>Yes</td></tr></table>

Note: Simple reminder group as baseline. \*\*\* p < 0.001, \*\* p < 0.01, \* p < 0.05, + p <0.1  
Robust standard errors are clustered at the deal category level.

<table><tr><td colspan="4">Table 7. Short-Term Net Revenue Estimates</td></tr><tr><td></td><td>Short-term overall purchase</td><td>Price</td><td>Short-term net revenue</td></tr><tr><td>Simple reminder</td><td>1.00</td><td>1.00</td><td>1.00</td></tr><tr><td> $One\ non-share^a$ </td><td>1.28</td><td>0.85</td><td>1.09</td></tr><tr><td> $One\ share^b$ </td><td>1.23</td><td>0.85</td><td>1.05</td></tr><tr><td> $Two\ codes^c$ </td><td>1.12</td><td>0.85</td><td>0.95</td></tr><tr><td colspan="4"> $^a 1 + (0.021/0.074) = 1.28$  $^b 1 + (0.018/0.074) = 1.24$  $^c 1 + (0.009/0.074) = 1.12$ </td></tr></table>

<table><tr><td colspan="6">Table 8. Lifetime Value Analysis</td></tr><tr><td>Experimental group</td><td>Sender purchase</td><td>Referrals (exist. customers)</td><td>Referrals (new customers)</td><td>Total referral</td><td>Lifetime value of the treatment $^{\dagger}$ </td></tr><tr><td>Simple reminder</td><td>197</td><td>50</td><td>51</td><td>101</td><td>767.2</td></tr><tr><td>One non-share</td><td>268</td><td>62</td><td>54</td><td>116</td><td>880.8</td></tr><tr><td>One share</td><td>223</td><td>72</td><td>72</td><td>144</td><td>1029.4</td></tr><tr><td>Two codes</td><td>219</td><td>64</td><td>54</td><td>118</td><td>833.8</td></tr><tr><td colspan="6"> $^{\dagger}$ Lifetime value of the treatment = Number of Sender Purchases * 1 + Number of Referrals (existing customers) * 1 + Number of Referrals (new customers) * 11.2</td></tr></table>

Note: The senders’ purchase number and total referral number, both from existing customers and new customers, are extracted from the actual purchase data in the field experiment.

By removing the incentive’s scarcity constraints in Treatment 2, the initial goal of Treatment 3 was to encourage consumers to not only purchase the deal using the non-shareable code but also drive successful referrals using the shareable code. However, a sender receiving multiple promo codes may also perceive the incentive as not being exclusive and would perhaps be therefore less likely to redeem it for purchase (Barone and Roy 2010; Dreze and Nunes 2008).<sup>21</sup> In addition, providing more promo codes may also influence consumers’ perceptions of the quality of the product as they may infer that the firm is trying to clear undesirable inventory (Nelson 1970, Cao et al. 2018).<sup>22</sup> Further, senders given two codes may be less likely to engage in social shares, as this may appear less altruistic, making sharing potentially less useful for building positive social image than it would be in the one shareable code context (Ariely et al. 2009, Rotemberg 2014).<sup>23</sup>

Bearing the above considerations in mind, we extend the analytical framework to include behavioral factors such as exclusivity and social motives (see Figure 6) in an attempt to provide plausible explanations for the divergence between our hypotheses and the empirical findings. While the incentive design with two promo codes lifts the scarcity constraint on consumers’ decisions (D<sub>i</sub>, S<sub>i</sub>), it may also negatively influence consumers’ perc


# Audit 18: Web-based intervention support system for health promotion

- Group: `retained_theory_driven`
- Model decision: `True`; centrality `dominant`; layer `software_system_or_artifact`
- Gates: `{"purposeful_solution_design": true, "objective_metric_is_primary_target": true, "comparative_improvement_demonstrated": true, "objective_improvement_is_the_success_basis": true}`
- Model reason: 文章明确设计并实现了一个Web-based干预支持系统（WISS），属于IS相关解决方案；其首要成功标准是客观指标——药物停用率和TTM阶段分布——并通过随机对照实验证明相对无干预对照组的显著改进；呼叫中心代表的主观满意反馈只是辅助性证据，不构成主要成功判据。因此四个门控均通过，客观指标改进为核心贡献。
- Source: `E:\github\qual-llm-check-IS-utd\database_fulltext_all\04378_2006_web-based-intervention-support-system-for-health-promotion.md`

#### Abstract

The Web has attracted considerable attention as an avenue to improve healthcare delivery. This paper describes the development of a Web-based intervention support system (WISS) that helps provide tailored interventions to enhance healthrelated behavior change. The tailoring strategy is based on the transtheoretical model (TTM). The performance of WISS was assessed by a pilot study, a controlled randomized longitudinal experiment involving 366 multiple sclerosis (MS) patients. Results suggest that WISS can reduce MS patients’ medication discontinuation rate and move more patients to a stage where dropout is least likely to occur.

<sup>D</sup> 2005 Elsevier B.V. All rights reserved.

Keywords: Web-based decision support systems; Transtheoretical model; Tailored intervention; Health behavior change

#### 1. Introduction

Web-based decision support systems (WDSS) refer to computerized systems that deliver decision support information or decision support tools to business end users using regular Web browsers [51,60] The ubiquity of the Web greatly extends the reach of WDSS capability so that decision-relevant information can be readily available to managers and staff users in geographically distributed locations [11,21,33,34,36,65] at a relatively low cost [64].

WDSS entails benefits in three dimensions: userfriendly dialog, seamless data access, and effortless sharing of business decision models [64]. Users can focus on system use and be freed from software installation, updates, and management by using WDSS [10,12]. Moreover, the Web makes it possible for firms to rent WDSS capability on a per-use basis from Application Service Providers [60]. WDSS have become the center of DSS vendors’ development activity [60] with the explosive use of the Web in business and personal activities.

Particularly, WDSS has received considerable attention in the healthcare arena, since the Web has increasingly become an innovative and important avenue for transforming healthcare [61]. The Web holds the promise of disseminating healthcare information, enhancing communication, and facilitating a wide range of interactions between patients and other stakeholders in the healthcare system [3]. A variety of WDSS have been applied in the healthcare practice including electronic patient records [35], telemedicine [28,57], the smart card application [14], computerized physician order entry systems [6], physician profiling systems [38], and community healthcare data warehouses [9]. By leveraging the power of the Web, these applications can integrate clinical and administrative information and share knowledge among healthcare stakeholders. Knowledge sharing is desirable in healthcare practice. The key to success is to embed specialized knowledge into IT that knowledge workers use to do their jobs [17]. WDSS is a promising tool to make knowledge sharing available in healthcare practice.

This paper describes the development and preliminary evaluation of a Web-based intervention support system (WISS) that shares knowledge about providing tailored interventions to individual patients. The WISS is designed to help patients with chronic diseases make decisions about their medication persistency. The objective is to motivate patients to continue taking their medications. The transtheoretical model (TTM), a 

#### 4. Preliminary evaluation

A pilot study was carried out to preliminarily evaluate the implementation success of the WISS. The existing literature does not agree upon a single approach to define information systems’ implementation success, and a variety of different variables have been employed to reflect this construct [2,19].

DeLone and McLean [20] summarize information systems success dependent variables into a taxonomy which has six dimensions. In the latest update of their information systems success model DeLone and McLean [19] add net benefits as a new variable and remark that <sup>b</sup>the choice of where the impacts should be measured will depend on the system or systems being evaluated and their purpose.<sup>Q</sup> Zmud and Cox [74] also state that implementation success refers to realizing the intended benefits of the DSS. The WISS we developed is a specialized DSS intending to increase MS patients’ medication persistency. Enhancing medication persistency or reducing medication discontinuation is the purpose of the WISS. Therefore, we need to measure the variables that can reflect medication persistency. Specifically, the patient’s medication discontinuation rate and stages of change will be measured to reflect the system success. Randomized controlled trial is considered the most rigorous study design for evaluating the effect of IT applications in healthcare [67]. In order to test the causal relationship between the WISS and its intended benefits, we used a randomized controlled experiment for system evaluation.

#### 4.2. Experimental design

A longitudinal experiment was designed to evaluate the WISS. The experiment involved a treatment group and a control group with 224 patients in each group. All of the patients were currently taking Avonex to treat MS. Patients were randomly assigned to either the treatment group or the control group. A special randomization algorithm was utilized for the random assignment so that each group had the same number of patients.

Interventions were provided to the patients in the treatment group but not to those in the control group. Patients in Stage 1 with an importance scale rating greater than 7 were contacted every four weeks, whereas patients in Stage 2 or Stage 3 or with an importance scale rating less than or equal to 7 were called every two weeks. The ideal frequency for calling a patient was not known. The frequencies used in this study were based on practical experience of a pharmacy group who had extensive patient consultation experiences.

Three call center representatives were assigned to conduct interventions. Each representative received a short training course on how to use WISS. The experiment lasted three months. During this time, call center representatives made a series of calls to each patient in the treatment group. At the beginning of each intervention, patients were restaged and their perceived importance ratings were re-measured. Follow-up calls were scheduled based on the latest stage information and importance values. Therefore, the frequency for receiving interventions might fluctuate for each patient in the treatment group. At the end of the three months, final data collection was conducted by phone and online surveys.

#### 4.3. Results

A total of 448 patients were recruited. There were 100 Stage 1 patients, 100 Stage 2 patients, and 24 Stage 3 patients in each group. The data of 82 patients became unusable during the experiment because we lost contact with the patients or the patients’ medical condition changed. At the end of the survey, a total of 366 patients’ data were collected. Table 1 shows the stage distribution of the 366 patients at the beginning of the experiment. Chi-square test shows that the stage proportions in the two groups were not significantly different $( \chi ^ { 2 } = . 6 8 , p = . 7 \bar { 1 } )$ . Ages ranged from 23 to 79 with an average of $4 6 . 0 \ \mathrm { ( S D } { = } 9 . 1 3 \mathrm { ) }$ . Approximately 83% of the patients were female and nearly 85% of the patients had received some college or higher education. Since the patients were randomly assigned to each group, their demographic data should be roughly the same. A T-test and Chi-square tests confirmed the two groups were not significantly different in terms of age $( t = . 9 2 , p = . 3 6 )$ , sex $( \chi ^ { 2 } = . 1 7 , p = . 6 8 )$ and education $( \chi ^ { 2 } = 1 . 6 5 , p = . 8 9 )$

At the end of the experiment, 17 patients in the control group and 2 patients in the treatment group discontinued Avonex (Table 2). The Chi-square test shows that the discontinuation rate in the two groups is significantly different from each other $( \chi ^ { 2 } = 1 0 . { \bar { 5 5 } } .$ $p { = } . 0 0 1 )$ ). The discontinuation rate in the treatment group (1.2%) is much lower than that in the control group (8.7%), indicating that the interventions supported by the WISS have affected the patients decision to discontinue their Avonex regimen. Therefore, H1 is supported.

An examination of the stage distribution at the end of the experiment revealed that the treatment group had relatively more patients in Stage 1 and fewer patients in Stage 2 than the control group (Table 3). Since the stage distributions of the two groups were the same at the beginning of the experiment, this suggests that some patients in the treatment group moved from Stage 2 toward Stage 1. Chi-square test indicates that the stage proportions are significantly dependent on the group $( \chi ^ { 2 } { = } 9 . 6 1 , ~ p { = } . 0 0 8 )$ . This result shows that the interventions supported by the WISS lead to stage differences between the two groups. Therefore, H2 is supported.

Table 1  
Stage distribution at the beginning of the experiment

#### 5. Discussion



#### 5.1. Implications for healthcare

WISS can contribute to MS patients’ health by preventing them from prematurely discontinuing their Avonex regimens. MS has a relapsing form featured by sporadic exacerbations. A patient might feel that it is unnecessary to continue taking medication during the stable period. However, MS may continue to develop insidiously without overt symptomatology [41]. If the patient stops taking Avonex, his or her MS may worsen and eventually cause serious deterioration in health which could have been avoided. WISS has the potential to reduce the number of physician visits. Based on our telephone interviews, many patients were at risk to discontinue Avonex because of psychological factors. For example, if a patient had an exacerbation and thought Avonex was not working, he or she may want to switch to an alternative medication. However, because of the nature of MS, the treatments can only control the disease, which means they only stop MS from getting worse but the current disease severity will not be decreased. If the patient switches to another medication, it is likely that he or she will also lose confidence in the new medication after another exacerbation. In this case, it is not clinically advantageous to switch medications and WISS may be able to convince the patient that Avonex is working without explicit sign of symptom alleviation.

From the standpoint of Biogen, the WISS is a marketing tool to reduce customer churn. The interventions could increase patient satisfaction with Biogen and Avonex and help Biogen maintain its market position. Although the WISS intends to promote the health of MS patients, it can also be beneficial to Biogen in the meantime. WISS creates a win–win situation for both MS patients and Biogen.

WISS deliver two types of decision support capabilities through two channels: the <sup>b</sup>chauffeured<sup>Q</sup> approach and the direct Web access. These vehicles pertain to the decision making of call center representatives and patients. First, the WISS supports the call center representatives to make decisions on how to intervene with MS patients. It turns the call center representatives into professional intervention counselors by transferring knowledge from TTM experts to the representatives by means of the WISS. Second, the WISS supports the MS patients’ decision making on whether to discontinue their Avonex regimens or not. The WISS delivers pertinent information, motivation, and empathy to the patients to prevent them from moving to

#### 5.2. Experimental design adequacy

The preliminary evaluation of the WISS used a control group and a treatment group and randomly assigned patients to each group. This randomized, controlled experimental design allows the logical conclusion of a cause and effect relationship between the stimulus (independent variable) and the response (dependent variable) to be made manifest [40]. There are three requirements of causality: concomitant variation, order of occurrence of variables, and elimination of other possible causal factors [59]. The research design of this study satisfies all of these requirements. First, the presence of the WISS and the patient discontinuation behavior are correlated (concomitant variation). Second, the interventions were provided before the response differences took place (order of occurrence). Finally, the existence of the control group and random assignment controlled all the extraneous variables that could affect patient responses [32]. The effects of these extraneous variables were deemed theoretically equal between the treatment and the control group (elimination of other possible causal factors). The intervention was considered the only variable differentiating the two groups. Therefore, the significant differences in the drug discontinuation rates and stage proportions between the treatment group and the control group are attributed to the intervention supported by the WISS.

It is worth noting that WISS is used to improve effectiveness of call center representatives, not efficiency. Providing behavioral interventions to multiple sclerosis patients requires substantial professional training in health psychology. The representatives did not have such training and could not provide tailored intervention independently. WISS offers stepby-step instructions to enable representatives to conduct tailored interventions. It is clear that WISS is designed to enable people to do something they couldn’t do before, rather than to do things more efficiently which they have been doing. The idea is to make professional knowledge available to lay people who work as call center representatives and employ these lay people to provide health behavioral interventions, thereby reducing healthcare delivery costs. Therefore, this paper focuses on effectiveness of WISS-supported interventions rather than improved efficiency of call center representatives as a result of using WISS.

#### 6. Conclusion

The Web’s ability to disseminate knowledge and drive down interaction costs is fundamentally transforming the healthcare system [31]. Tailored health information can be disseminated on the Web and delivered to patients. This paper describes the development and evaluation of a Web-based intervention support system that enhances MS patients’ medication persistency. The intervention strategy based on the TTM is built into the system after careful planning and research. Results of preliminary system evaluation indicate that the WISS can reduce the MS patients’ medication discontinuation rate and move more patients to the stage where discontinuation is less likely to happen. The findings suggest that the integration of behavioral theories and Web-based DSS can make significant contribution to the healthcare delivery to the public. In addition, this re

# Audit 19: Online government advisory service innovation through Intelligent Support Systems

- Group: `near_miss_three_gates`
- Model decision: `False`; centrality `mixed`; layer `software_system_or_artifact`
- Gates: `{"purposeful_solution_design": true, "objective_metric_is_primary_target": true, "comparative_improvement_demonstrated": true, "objective_improvement_is_the_success_basis": false}`
- Model reason: Gate 1-3 均通过：作者设计了三种在线政务咨询工具，并利用客观计分的决策质量（DQ）进行三组比较，显著证明了优化解释 ISS 的客观改进。但 Gate 4 失败：文章的核心贡献是授权理论视角下的公民感知模型，DQ 只是多个目标结果之一，主观的 DMS、DMT、SoC、PPR、GSPI 才是主要成功依据；客观改进并非唯一或支配性的成功标准。因此客观指标中心性为 mixed，不能保留。
- Source: `E:\github\qual-llm-check-IS-utd\database_fulltext_all\10408_2011_online-government-advisory-service-innovation-through-intelligent-support-systems.md`

#### 1. Introduction

The public administration sector has recently started to provide online Intelligent Support Systems (ISS) on government agency portals, especially in countries like Australia and Canada whose egovernment readiness index is high. Online ISS are web-based advisory systems that assist citizens in obtaining and interpreting information about their country’s e-government material, to selfassess their eligibility for aid, etc., and to make informed decisions on whether to proceed to the next stage of their application process. In practice ISS range from relatively simple tools, like smart financial calculators, to complex pension advisory systems incorporating compound rule bases.

When appropriately designed, ISS can improve the public’s experience with the government agency and help in establishing a long term engaging and trusted relationship. Such tools can be an effective way to ease the strain between the citizens’ need for more efficient and higher quality public service and the previously cumbersome, inconsistent and arbitrary decision making provided by government officials [5].

Although ISS have been extensively studied, most research has focused on organizational users; there has been a dearth of studies on the value of ISS tools for public use. Our study was aimed at filling this gap. Therefore, we took a citizen’s perspective to answer three questions:

(1) Can online advisory services supplied by government agencies lead to potential benefits for the public?

(2) If yes, what are the benefits?

(3) Do the optimized explanation capabilities of ISS increase the benefits?

To limit the scope of the study, we did not consider the digital divide or related issues such as access and convenience of the ISS. Despite their importance, we were concerned with how the advisory systems compared with other means of decision support that might be available, such as online manuals. We therefore limited our investigation to situations where alternative means of advice were accessible to Internet users.

#### 4. Research method



#### 4.2. Experiment design and procedures

A between-subject design was used. The treatment variable was the type of support available on the e-government website. There were three treatment groups. The first was forwarded to a website that provided ISS with optimized explanation aids to help the subjects. The second was forwarded to a website that provided an ISS with limited explanation. The third was forwarded to a website that provided text-based explanations. Participants could choose the language with which they felt more comfortable (English or Chinese) by simply clicking on a link at the top-right corner of the tool. Subjects were randomly divided into one of the three groups. Appendix A outlines all the independent and dependent variables.

Experiments were conducted in computer laboratories. The experiment supervisors first reminded all subjects that their participation was the voluntary and told them the objectives of our study. Then, subjects were given a hypothetical case scenario, containing information such as the date of registration of their business, which they used while filling out the self-assessment. They were first asked to read the case scenarios, after which, they followed the instructions and used one of the experimental websites to complete their task. At the end of the study, the participants completed a questionnaire intended to capture their feelings about their experience.

The three websites simulated self-assessment tools provided by the Ministry of Commerce of a hypothetical country; a hypothetical government agency was used to remove, as much as possible, any pre-existing perceptions of the participants. Removing this pre-imposed attitude allowed us to be more accurate in capturing the effect of providing different decision aids in measuring the citizen’s perception of the hypothetical agency.

The websites were designed after scrutinizing existing online advisory tools in Australia. All the decision rules underlying the tool were developed by consulting real government agency assessment rules. Thus the impact of using a hypothetical government was minimized.

[image omitted]  
Fig. 2. Example screen shots of online ISS with optimized explanations. Note: To ensure the experiment material is close to real-life, the rules underlying the software used material from the MOFCOM.

The decision support tools were (1) ISS with optimized explanations (Fig. 2), (2) ISS with limited explanations (Fig. 3) or (3) text-based system (electronic) in a PDF document (Fig. 4).

The 

#### 5. Data analysis and results

To improve the performance of the statistical analysis, several aspects of the data screening process were performed. Checking for incompleteness or failure to pass the consistency check required us to remove nine surveys from the 171 cases collected. Further, the relationships between demographic factors (gender, language used and age) and dependent variables were investigated through independent T-tests and ANOVA using SPSS 15.0 (see Appendix B). The result showed that among different demographic groups there was no significant difference in their response about the dependent variables of interest.

After going through data screening, the hypotheses and research model of the study were ready to be tested. First, hypotheses H1, H2, H3 were examined using ANOVA to reveal the impact of providing different online self-assessment tools (i.e., type of support, a categorical variable) on DMS, DMT and DQ. Second, given the complex nature of the later three hypotheses and the existence of intervening variables, PLS analysis in SEM form was employed. PLS was used as the best tool for dealing with small sample sizes, since it made few assumptions about the distribution of data. It is also a very robust tool when multicollinearities exist in the data.

Table 1 ANOVA result.

<table><tr><td>Dependent variable</td><td>(I) Group (mean, std dev.)</td><td>(J) Group (mean, std. dev.)</td><td>Mean difference (I-J)</td><td>Std. error</td></tr><tr><td rowspan="2">DMS</td><td>G-EXP (5.22, 0.67)</td><td>G-LMT (3.83, 064)</td><td>1.39*</td><td>0.13</td></tr><tr><td>G-LMT (3.83, 0.64)</td><td>G-TXT (2.09, 0.65)</td><td>1.74*</td><td>0.13</td></tr><tr><td rowspan="2">DMT</td><td>G-EXP (5.24, 0.52)</td><td>G-LMT (3.73, 0.68)</td><td>1.51*</td><td>0.11</td></tr><tr><td>G-LMT (3.73, 0.68)</td><td>G-TXT (2.05, 0.49)</td><td>1.68*</td><td>0.11</td></tr><tr><td rowspan="2">DQ</td><td>G-EXP (67.4, 15.7)</td><td>G-LMT (51.1, 16.1)</td><td>16.33*</td><td>2.81</td></tr><tr><td>G-LMT (51.1, 16.1)</td><td>G-TXT (29.0, 11.6)</td><td>22.1*</td><td>2.81</td></tr></table>

<sup>\*</sup> The mean difference is significant at the 0.05 level. G-EXP: online ISS with optimized explanations; G-LMT: online ISS with limited explanations; G-TXT: text-based systems.

The result of ANOVA analysis showed that there were significant differences among the means of DMS $( F ( 2 , 1 5 9 ) = 3 1 0 . 2 , p < 0 . 0 1 ) , \mathrm { D M T } ( F ( 2 , 1 5 9 ) = 4 2 3 . 9 , p < 0 . 0 1 )$ and $\operatorname { D Q } ( 

#### 6. Conclusions and discussion

The exploratory stage of our study revealed six key constructs of interest in the empowering process: decision making transparency, decision making satisfaction, and decision quality, empowerment outcomes (power and control), and their impact on the government agencies’ service provider image. The experimental stage showed that online ISS, especially those with optimized explanation features yields higher decision satisfaction, transparency, and quality. Among these effectiveness indicators, transparency is the most important predictor of the public’s sense of control over their destiny, attitude towards their power relationship, and the perceived government service provider image.

Explanation and transparency are key to the success of online advisory systems; an appropriately designed online advisory tool provides a more transparent decision making process due to the publication of its decision criteria, and this process empowers the citizens. In contrast, decision quality was not shown to have significant impact on the dependent variables of interest. This disparity from theory prediction might be a result of the participants not being aware of their actual performance, which is often the case in real life, when people use online government services to conduct self-assessment.

Our mixed-method approach allowed us to integrate theory and practice. The initial phase of the study involved a series of exploratory techniques, through which the authors managed to develop a practical understanding of the phenomenon, despite the dearth of published work. The second phase of the study used experiments, through which we were able to quantitatively examine the proposed research model. This multi-method approach enhanced both the rigor and the applicability of the study and triangulated the research findings.

Some limitations of the study must be addressed: one is related to the use of explanations by participants in the group with optimized explanations. As pointed out by Gregor [9], the availability of an explanation is not equivalent to explanation use, or reading, and understanding of the explanations; the difficulty in measuring actual explanation use has been acknowledged by various researchers; protocol analysis techniques, such as concurrent verbalisation has to sacrifice experimental realism and run the risk of sensitising participants. However, our study took an extra step with the optimized explanation group only of asking participants ‘‘how frequently did you access the explanations?’’ at the end of the questionnaire. This factor was found to have minimal impact on the results of the study.

The second limitation is related to the threat to experimental validity due to experiment control. There were a number of supervisors involved in the experiments and although they were provided with consistent protocols, it is still possible that some procedures might not have been followed as intended. The potential impacts of experiment supervisors could affect the generalizability of the result.

Practically, our findings provide insights that benefit both the public and the government agencies. From the public’s viewpoint, effective online advisory tools have the potential to reshape governance and empower them. From government agencies viewpoint, a more relevant success indicator of the government, whether at the municipal or state level, is the increased appreciation of the general public rather than its performance. Having effective online self-assessment tools is a good starting point to improve public service delivery and responsiveness for its citizens.

Appendix A. Variables, their measurement scales, sources, and item loadings.

<table><tr><td>Variable name</td><td>Measure</td><td>Mean (SD)</td><td>Std. loading</td></tr><tr><td colspan="4">Decision making satisfaction (from Pereira [16]) Cronbach&#x27;s α: 0.94</td></tr><tr><td>DMS1</td><td>This online self-assessment tool is one of the best ways to assist me to decide on LSCa eligibility</td><td></td><td>0.92</td></tr><tr><td>DMS2</td><td>If I had to make another similar self-assessment, I&#x27;d rather not use this online tool again</td><td></td><td>0.85</td></tr><tr><td>DMS3</td><td>I am not happy that I used this online self-assessment tool to decide on my eligibility</td><td>3.72</td><td>0.88</td></tr><tr><td>DMS4</td><td>If I had to make a decision about LSC eligibility again, and an online self-assessment tool such as this was available, I would be very likely to use it</td><td>(1.43)</td><td>0.89</td></tr><tr><td>DMS5</td><td>If a friend was making a decision on his business&#x27;s LSC and I knew that an online Guide like this was available, I would be very likely to recommend it to him</td><td></td><td>0.92</td></tr><tr><td colspan="4">Decision making transparency (from Milne and Culnan [15]) Cronbach&#x27;s α: 0.93</td></tr><tr><td>DMT1</td><td>How the LSC rules are applied to my situation is easy to understand</td><td></td><td>0.92</td></tr><


# Audit 20: Optimizing Two-Sided Promotion for Transportation Network Companies: A Structural Model with Conditional Bayesian Learning

- Group: `near_miss_three_gates`
- Model decision: `False`; centrality `mixed`; layer `digital_platform_mechanism_or_policy`
- Gates: `{"purposeful_solution_design": true, "objective_metric_is_primary_target": true, "comparative_improvement_demonstrated": true, "objective_improvement_is_the_success_basis": false}`
- Model reason: Gate 1-3 通过：论文提出了可实施的平台促销政策并通过仿真对比展示 objective metric 改进。Gate 4 未通过：文章的核心贡献是结构模型估计和司机学习/促销效应的实证解释，政策优化只是其中一个应用组成部分，客观指标改进不是文章主要结论的排他性或主导性成功依据，因此 centrality 为 mixed。
- Source: `E:\github\qual-llm-check-IS-utd\database_fulltext_all\04164_2020_optimizing-two-sided-promotion-for-transportation-network-companies-a-structural-model-with-cond.md`

#### 1. Introduction

A transportation network company (TNC) is defined as “a service that does not own vehicles or employ drivers, and relies on software to connect passengers to rides” (California Public Utilities Commission 2013, p. 3). Early operators of transportation network apps include such well-funded firms as Uber, Lyft, Hailo, Ola Cabs, and Didi Dache. A TNC creates a two-sided market with two versions of its app, one for passengers to generate orders and the other for drivers to select orders. Both versions can be easily downloaded from major app platforms, including the App Store, Google Play, and Windows Phone Apps.

TNCs have drawn the attention of information systems and economics researchers due to the transformative and disruptive impact of their informationtechnology-enabled features on transportation systems. Those features, which are, in general, available in any TNC app, significantly reshape the business process and thus create economic value as follows. First, TNC apps typically provide internet-based matching, which expands the choice sets of both sides of users, passengers and drivers, beyond those of telephone reservation or roadside matching. Second, as the TNC is fundamentally a reservation-based business model, TNC apps brings more flexibility by allowing users to cancel orders or reservations, which is typically prohibited in the traditional reservationbased transportation model. With the cancellation function, users can easily react to updated information about the quality of orders and about other options, such as roadside hailing.

Third, most of the mainstream TNC apps enhance simplicity and flexibility in the transaction process by featuring “online pay,” which enables passengers to handle their payments automatically. Once a trip is completed, the TNC app digitally transfers the fare from the passenger to the driver’s online-pay account and immediately reports the fare, route, and time through email to passengers. Prior research has quantified the transformative impact of TNC at an aggregative level, such as the overall impact of TNC on a particular dimension, by treating TNC’s entry or exit as the finest grain (Greenwood and Wattal 2017, Gong et al. 2017, Park et al. 2017, Zhang and Li 2017, Burtch et al. 2018, Rhee et al. 2018). Scant research has quantified the transformative impact at a microlevel and identified its economic value at the attribute (feature) level, such as the value of matching, cancellation, or online pay.

Although TNC 

#### 5. Estimation Results



#### 5.2. Estimation Results

In this section, we present the estimation results and insights associated with the estimates. We present the results in the same order as seen in our model, starting from the decisions of drivers and followed by the drivers’ beliefs about passengers’ decisions to use online pay. All point estimates as well as standard errors are presented in Table 4. In addition, we show the latent learning process by explicitly displaying the updated perceived attributes and updated perceived variance parameters of the three decisions to help to understand the learning process. The attribute values are simulated based on estimated parameters and are shown in Figure 4.

5.2.1. Stage 1. Note that in our forward-looking dynamic model, drivers’ expectations of Stage 2 utility affect their Stage 1 decision. Driver cashback, passenger cashback, passenger bids, and platform sub sidy thus could affect drivers’ Stage 1 decision indirectly through the expectation of Stage 2 utility functions. Given the model structure, the effect of driver cashback, passenger cashback, passenger bids, and platform subsidy on the Stage 1 decision should be consistent with that of Stage 2 qualitatively. Therefore, we omit the repeated qualitative interpretation, which is more extensively discussed in the Stage 2 results, and estimate only the promotion elasticities of a driver’s likelihood of accepting an order to highlight the quantitative findings. We show that a one-standarddeviation increase in driver cashback, platform subsidy, passenger bid, and passenger cashback, on average, would increase the probability of accepting an order by 6.7%, 2.9%, 2.2%, and 0.5%, respectively.

Figure 3. Fitness per a Comparison of Nonparametric Aggregate Estimation Versus Prediction from Our Model  
[image omitted]

[image omitted]

Fitness of Conditional Decision to Pav Online  
[image omitted]

We further find strong evidence of learning, as shown in Table 4 and Figure 4. The prior parameter for app attribute $A _ { a 0 }$ is <sup>−</sup>2.02, which is significantly lower than the normalized posterior parameter $\dot { A _ { a 1 } }$ (Z-score of <sup>−</sup>3.31). This difference indicates the undervaluation of the TNC app by drivers before they start to use it and suggests that learning can help to eliminate the perception bias gradually. We estimate $\log ( \sigma _ { a 1 } ^ { 2 } )$ to be 0.16, or the variance of signal $\sigma _ { a 1 } ^ { 2 }$ of 1.17, larger than the one-normalized experience variabilit

#### 5.3. Extended Analysis and Robustness Check

We report the results of three extended analyses to check the robustness of our finding. First, we include the estimation results of Model 3 in the model comparison, which uses random parameters to substitute our latentclass parameters. Second, because our observation period includes a major holiday, a potential concern is whether seasonality would affect our results. Therefore, we include holiday/nonholiday as a variable that governs the utility of accepting an order online.

Given the complexity of our proposed model, especially the specification in Stages 1 and 2, we further estimate a simplified model that combines the two stages into one. In particular, we treat declining an order in Stage 1 the same as canceling in Stage 2, termed “not fulfill,” and as a result, there is only one stage of decision to fulfill or not. All of the independent variables in the utility functions of Stages 1 and 2 in our proposed model are included, except that this model has only one learning process for fulfilling an order, as only one type of signal for learning, driver’s experience of fulfilling orders, exists.

A more detailed specification and the results are reported in the Online Appendix. This detailed report shows that the random parameter approach and seasonality do not greatly affect the other parameters in our model, and that the qualitative interpretation of our main results is still robust. In addition, the simplified model results generate similar insights to the findings of the proposed model, which, once again, indicates the robustness of our analysis.

#### 7. Conclusion and Implications

TNC app platforms are attempting to accelerate drivers’ learning about new features and maintain their high app-usage rates in a cost-effective way. By leveraging transaction-level data of drivers on a TNC app, we find a means to reduce their reliance on sales promotions by developing an understanding of the following mechanisms: (1) the economic value of TNC matching, cancellation, and online-pay features; (2) how new drivers learn those features and form their initial preference of TNC apps; and (3) how a two-sided sales promotion affects the formation of initial learning.

Our findings extend the understanding of the transformative and disruptive impact of IT in transportation to a finer-grained attribute/feature level. In particular, our results show the utility value/cost associated with matching an order, canceling an order, and paying online. Because those features are essential components of TNC apps, our work decomposes the economic value of TNC apps into finergrained components, which sheds light on the TNC app attributions and designs.

Our analysis also reveals drivers’ learning process of multiple features on TNC apps. We show that TNC app users underestimate the attribute values of matching and cancellation and the perceived value of passengers’ preference to use an online-pay function. As a result, drivers form a comparably lower willingness to use the app and higher willingness to cancel an order. These biased perceptions are corrected with accumulated usage experience, with accepting an order on TNC as learned most quickly and the fulfilling/ canceling feature as learned most slowly. Once the learning process is completed, drivers are more tolerant of accepting and fulfilling orders and are more optimistic about being rewarded with a cashback bonus. These results indicate the significant role of usage experience in alleviating bias from uncertainty and support the common industry practice of enhancing usage experience during product introduction.

We contribute to the promotional strategy literature by empirically examining how a two-sided promotion affects a driver’s app use and learning. Our results qualitatively and quantitatively show how bids from passengers, subsidies from the app provider, and an online-pay-contingent cashback bonus for passengers and for drivers affect drivers’ decisions through a direct effect of immediate impact on the latent utility level, an indirect effect of drivers’ learning, and another indirect effect of drivers’ forward-looking on passengers’ decisions to use online pay. Interestingly, we show that passenger bids and platform subsidy exhibit a smaller magnitude of impact on a driver’s willingness to accept and fulfill an order as compared with cashback for drivers. One potential explanation is that a bid or a subsidy might also signal high risk and/or low quality of that order.

We further explicitly display the existence and the magnitude of the two indirect effects. The indirect effect through learning indicates that a sales promotion is an effective tool for user learning, and thus, a sales promotion in the introductory period has more value than does a promotion that is launched later. An early sales promotion additionally affects decisions in later periods through early accumulated usage experience that corrects the attribute perception bias. This finding justifies the importance of an early sales promotion for a recently introduced product and explains why most TNC app platforms put forth enormous effort toward sales promotions in early stages.

In addition, the indirect effect through forwardlooking indicates a cross effect of a two-sided sales promotion. Sales promotions for passengers can influence the decisions of drivers when drivers are rationally forward-looking, and the decisions of passengers affect drivers’ earnings. This suggests the importance of the interdependency when designing a two-sided promotion for a two-sided market. Finally, to shed more light on the practical aspects of our findings, we propose revised promotion policies that take advantage of both indirect effects to help the TNC alleviate the supply shortage while controlling its cost.

Our paper has several limitations. First, the data available for researchers are limited. Our data limit us from investigating the order-generation process. In addition, the introductory period of the product might indicate incomprehensiveness of data maintenance. For each transaction, our data do not include such information as pickup locations, destinations, duration, or traffic routes, even though drivers might be able to partially obtain or infer such information.

Such a limitation restricts our investigation under the assumption of homogeneity of orders in terms of drivers’ learning process. Second, we take sales promotion as exogenous. Research that considers a strategic sales promotion could allow investigation of competition among different platforms and extend our learning framework 


# Audit 21: Applying behavioral economics in predictive analytics for B2B churn: Findings from service quality data

- Group: `near_miss_three_gates`
- Model decision: `False`; centrality `dominant`; layer `prediction_model`
- Gates: `{"purposeful_solution_design": true, "objective_metric_is_primary_target": true, "comparative_improvement_demonstrated": false, "objective_improvement_is_the_success_basis": true}`
- Model reason: 该文提出了理论驱动的B2B流失预测模型（理性与有限理性服务疼痛特征），并以AUC作为明确的客观预测指标，因此Gate 1和Gate 2通过，且成功判断以客观预测表现为基础，Gate 4也通过。但全文没有与基线、基准、消融或对照组模型直接比较AUC，只报告了测试层AUC绝对值（约0.58–0.68），不满足Gate 3要求的对比改进证据，故strict_objective_improvement_match为false。
- Source: `E:\github\qual-llm-check-IS-utd\database_fulltext_all\11476_2017_applying-behavioral-economics-in-predictive-analytics-for-b2b-churn-findings-from-service-qualit.md`

### APPLYING BEHAVIORAL ECONOMICS IN PREDICTIVE ANALYTICS FOR B2B CHURN: FINDINGS FROM SERVICE QUALITY DATA

Arash Barfar Information Systems Department College of Business University of Nevada at Reno

Balaji Padmanabhan & Alan Hevner Information Systems & Decision Sciences Department Muma College of Business, University of South Florida 4202 E. Fowler Avenue, Tampa, FL 33620

Abstract: Motivated by the long-standing debate on rationality in behavioral economics and the potential of theory-driven predictive analytics, this paper examines the link between service quality and B2B churn. Using longitudinal B2B transactional data with service quality indicators provided by a large company, we present evidence that both rationality and bounded-rationality assumptions play significant roles in predicting organizational decisions on churn. Specifically, variables that relate to the assumed rationality of organizations appear to provide accurate predictions while, at the same time, variables that capture boundedly rational decision rules appear to play a role through “somatic states” that make organizations more sensitive to the rational variables. In addition to presenting a novel approach for predicting organizational decisions on churn, this paper offers theoretical and managerial insights as well as opportunities for future research at the intersection of behavioral economics and predictive analytics for decisionmaking.

Keywords: organizational decision analytics, B2B service operations, churn, service quality, decision-making, rationality, bounded rationality, heuristics, adaptive toolbox, somatic states

### APPLYING BEHAVIORAL ECONOMICS IN PREDICTIVE ANALYTICS FOR B2B CHURN: FINDINGS FROM SERVICE QUALITY DATA

Abstract: Motivated by the long-standing debate on rationality in behavioral economics and the potential of theory-driven predictive analytics, this paper examines the link between service quality and B2B churn. Using longitudinal B2B transactional data with service quality indicators provided by a large company, we present evidence that both rationality and bounded-rationality assumptions play significant roles in predicting organizational decisions on churn. Specifically, variables that relate to the assumed rationality of organizations appear to provide accurate predictions while, at the same time, variables that capture boundedly rational decision rules appear to play a role through “somatic states” that make organizations more sensitive to the rational variables. In addition to presenting a novel approach for predicting organizational decisions on churn, this paper offers theoretical and managerial insights as well as opportunities for future research at the intersection of behavioral economics and predictive analytics for decisionmaking.

Keywords: organizational decision analytics, B2B service operations, churn, service quality, decision-making, rationality, bounded rationality, heuristics, adaptive toolbox, somatic states

## APPLYING BEHAVIORAL ECONOMICS IN PREDICTIVE ANALYTICS FOR B2B CHURN: FINDINGS FROM SERVICE QUALITY DATA

## 1. INTRODUCTION

Service organizations are highly invested in maintaining strong relationships with their customer base, both individual customers (B2C) and business entities (B2B). Loyalty in B2B service operations is particularly important since B2B interactions are perhaps fewer but provide greater numbers of transactions and more revenue per transaction (Rauyruen & Miller 2007). To understand the role that service quality plays in B2B loyalty, we analyze a rich longitudinal service quality database from a large company. The database covers two years of weekly service transactions for nearly 100,000 Small and Medium Enterprises (SMEs) as service customers. These SMEs may be viewed as active processors of service quality, which constantly analyze their service records and decide whether to stop or continue their business with the service company (Koufteros et al. 2014). Using this fine-grained and longitudinal B service quality data to examine the role that service quality plays in B2B churn provides the applied context of this research.

The methodological context of this research is informed by two stimulating resear

#### APPLYING BEHAVIORAL ECONOMICS IN PREDICTIVE ANALYTICS FOR B2B CHURN: FINDINGS FROM SERVICE QUALITY DATA



#### 1. INTRODUCTION

Service organizations are highly invested in maintaining strong relationships with their customer base, both individual customers (B2C) and business entities (B2B). Loyalty in B2B service operations is particularly important since B2B interactions are perhaps fewer but provide greater numbers of transactions and more revenue per transaction (Rauyruen & Miller 2007). To understand the role that service quality plays in B2B loyalty, we analyze a rich longitudinal service quality database from a large company. The database covers two years of weekly service transactions for nearly 100,000 Small and Medium Enterprises (SMEs) as service customers. These SMEs may be viewed as active processors of service quality, which constantly analyze their service records and decide whether to stop or continue their business with the service company (Koufteros et al. 2014). Using this fine-grained and longitudinal B service quality data to examine the role that service quality plays in B2B churn provides the applied context of this research.

The methodological context of this research is informed by two stimulating research streams. The field of behavioral economics has the potential to fuel new streams of interdisciplinary Information Systems (IS) research (Goes 2013). At the same time, the recent explosion of interest in predictive analytics has highlighted the potential of leveraging massive fine-grained behavioral data that are becoming available (Martens et al. 2016). This paper is one of the first that brings these two areas together in the context of an important decision support context (i.e. managing customer churn).

Our approach involves designing rational and boundedly rational measures of service pain assessment, which relate to the neoclassical and behavioral perspectives on the rationality assumption in organizational decision making. Do levels of service pain affect the SME’s decision on churn? Can different perspectives on the rationality assumption help us design different service pain evaluation variables that capture such effects and, subsequently, predict organizational decisions on churn? This paper takes up these broad questions and examines both explanation and prediction (Shmueli 2010). That is, we investigate (i) if the service pain evaluation variables are associated with SMEs’ decisions to churn and (ii) whether such variables help generate accurate predictions.

Using a finely-granular service database to construct theoretical features also pres

#### 5. ANALYSES AND RESULTS

We examine the large service database to see if rational and boundedly rational decision rules help the service company explain and predict an SME’s churn. We use one-third of the churners to build the descriptive dataset and the remaining two-thirds for the explanatory/predictive analyses.

#### 5.1. Descriptive Analysis

The aims of the study’s descriptive analysis are twofold. First, it intrinsically covers the two essential steps in building predictive models (Shmueli & Koppius 2011); i.e. exploratory analysis and choice of variables. We have defined five churn decision rules in Section 4 each of which can be calculated with $p _ { t }$ or $\bar { p _ { t } }$ of eight SQIs. The descriptive analysis helps decide which application measures, of which decision rules, with regard to which SQIs can be potential predictors for organizational churn.

Second, the study’s descriptive analysis aims to address the view in behavioral economics that rejects positivism and the elements of statistical significance such as $p \mathrm { . }$ value and lack of fit (Hosseini 2003; Ziliak & McCloskey 2008). Thus, in the descriptive analysis we refrain from rushing into the tests of statistical significance; we first investigate any descriptive evidence of the application of churn decision rules.

The descriptive ETL is designed to extract the three measures from the descriptive dataset. These measures in part address the application of the suggested decision rules in churn:

Measure 1- Percentage of churners that immediately follow the firing of a decision rule compared to nonchurners (for whom the condition of the relevant decision rule holds in the last six weeks of their matched service episodes),

Measure 2- Percentage of churners for whom the decision rule fired at least once compared to non-churners (for whom the condition of the relevant decision rule holds at least once in their matched episodes),

#### 6. CONCLUSIONS AND FUTURE WORK

Figure 8: Churn tree for new customers  
[image omitted]

In this paper we have shown how behavioral economics can inspire feature engineering and help build parsimonious models for an important business problem using theory-driven predictive analytics. Our analyses corroborate the role of the rationality assumption in explaining/ predicting the future behavior of organizations (Friedman 1953; Simon 1979). Besides shedding new light on the rationality debate, the results have important implications for B2B service operations. Our findings suggest that the service company should keep the total service pain low. This is an important finding in B2B operations where the prior conception is that firms do not follow a rational model of service quality assessment in making decisions about service renewals (Bolton et al. 2006). Concomitantly, the service provider should monitor every service failure and be alert to the extensional service evaluation heuristic, which can cause a somatic state for the SME—making it more sensitive to the past total service pain.

#### 6.1. Implications for Behavioral Organizational Economics

Behavioral economics views administrative decision-making as a combination of both intuitive and analytical skills (Simon 1997). Accordingly, our feature engineering designed both rational and boundedly rational measures of service pain assessment. The rational measure of pain assessment is simply the temporal average of service pain. The boundedly rational service pain assessment measures are different variants of the two most comprehensive heuristics; i.e. representativeness and availability heuristics (Tversky & Kahneman 1974). These measures also include more rational variants of the heuristic decision rules, which appreciate utility and probability (i.e. extensional target evaluation).

Regarding the analytical service pain evaluation techniques, both descriptive and predictive analyses suggest that the average behavior of SMEs as a group is as if they are rational (Friedman 1953). In particular, the rational measures of service pain evaluation help explain and predict the SMEs’ decisions on churn. Individual SMEs might practice different boundedly rational decision rules; however, it is their assumed rationality that helps explain and predict their future behavior (Friedman 1953, 1978). This finding is also endorsed by Friedman (1953) and Shugan (2009); i.e. the theory’s fruitfulness is evaluated by its predictive accuracy, not by its assumptions realism. Nonetheless, our findings should not characterize the SMEs as wholly rational. What we demonstrate with our analyses is that, overall, the SMEs’ assumed rationality appears to contribute to our models’ statistical and practical significance. This is also consistent with the findings in experimental economics that concur with neoclassical predictions (e.g. List 2004).

Regarding the heuristic service pain evaluation techniques, our findings are consistent with the somatic marker hypothesis in neuroeconomics (Bechara & Damasio 2005). The biasing nature of intuitive decision rules might cause a somatic state which draws the SME’s attention to the service quality issues and calls for judgment, which might be carried out in a relatively rational way. In this vein, while the proportional peak pain draws the SME’s attention to the corresponding service issue, the SME’s information systems may play the role of a working memory that is necessary for coherent analytical reasoning after the somatic marker operates. Being in a somatic state caused by the peak pain, the organization carries out the subsequent ev

#### 6.2. Implications for Predictive Analytics and Churn

The hybrid deductive-inductive approach to building predictive models for churn makes this research one of the first B2B churn studies where service quality is shown to be an important determinant for customer attrition—especially for those with whom the service provider has not yet established a deep business relationship. This is an important finding for B2B operations, where the number of potential service providers is less than in B2C—making the ‘quality-churn’ connection more difficult to build on. Interestingly, the few B2B churn studies that consider service quality features (e.g. Chen et al. 2014) do not find them among the top ranked predictors. However, the high quality and longitudinal nature of the data used in this study present a compelling case for the importance of service quality in B2B operations.

Furthermore, this paper takes a unique approach to discovering churners and pinpointing their churn dates in a non-contractual environment. This makes the present paper one of the first non-contractual churn studies where subjects have different prediction periods, compared to predetermined prediction periods.

### APPLYING BEHAVIORAL ECONOMICS IN PREDICTIVE ANALYTICS FOR B2B CHURN: FINDINGS FROM SERVICE QUALITY DATA

## Highlights

 The paper presents an approach that integrates behavioral economics and predictive analytics in a B2B churn modeling context.

 We present evidence that both rationality and bounded-rationality assumptions play significant roles in predicting organizational decisions on churn.

Unlike many studies at the individual level we do not find strong evidence for human decision making biases or heuristics at play here at the organization level.


# Audit 22: Sensing the Future: A Design Framework for Context-Aware Predictive Systems

- Group: `near_miss_three_gates`
- Model decision: `False`; centrality `mixed`; layer `none`
- Gates: `{"purposeful_solution_design": true, "objective_metric_is_primary_target": true, "comparative_improvement_demonstrated": true, "objective_improvement_is_the_success_basis": false}`
- Model reason: Gate 1、2、3通过：文章提出了CAPS设计框架并据此构建/修改了预测工件，COST_FE是明确目标，且相对Croston基线展示了4%和20%的客观改进。但Gate 4不通过：文章的核心贡献是CAPS框架本身及设计命题，其成功主要依据框架的实用性、可推广性、专家反馈和定性评估；客观指标改进只是作为评价框架的例证之一，而非判定该框架成功的主要或唯一依据。因此objective_metric_centrality为mixed，不能保留。
- Source: `E:\github\qual-llm-check-IS-utd\database_fulltext_all\05836_2023_sensing-the-future-a-design-framework-for-context-aware-predictive-systems.md`

#### Abstract

Sensors embedded in smart objects, smart machines, and smart buildings produce ever-growing streams of contextual data that convey information of interest about their operating environment. Although an increasing number of industries have embraced the utilization of sensors in routine operations, no clear framework is available to guide designers who aim to leverage contextual data collected from these sensors to develop predictive systems. In this paper, we applied design science research methodology to develop and evaluate a general framework that can help designers build predictive systems utilizing sensor data. Specifically, we developed a framework for designing context-aware predictive systems (CAPS). We then evaluated the framework through its application in MAN Diesel & Turbo, which served as a case company. The framework can be generalized into a class of demand-forecasting problems that rely on sensor-generated contextual data. The CAPS framework is unique and can help practitioners make better-informed decisions when designing context-aware predictive systems.

Keywords: Design Framework, Systems Design, Sensor Data, IoT Data, Trace Data, Predictive Analytics, Forecasting, Design Science Research

Sandeep Purao was the accepting senior editor. This research article was submitted on November 30, 2015 and underwent six revisions.

#### 1 Introduction

Context-aware computing emerged as a term with the introduction of ubiquitous computing (Weiser, 1991). Context here refers to any information that describes the situation or environment of an entity, such as a person, place, or object (Abowd et al., 1999). Sensors are best equipped to capture context by leveraging situational and environmental information to offer timely, situated, and usable content, functions, and experiences (Perera et al., 2013).

As digital technologies continue to evolve, we see everyday objects—smartphones, cars, homes, and even clothes—being embedded with sensor technologies that respond to physical stimuli and generate contextual data (Aarts & Marzano, 2003; Abowd et al., 1999; Javaid et al, 2021; Uckelmann et al., 2011). Such objects can collect, process, and communicate data about their situation, functionality, and operating environment that can then be used for context-aware computing (Cook & Das, 2004; Shim et al., 2019). Although there are ample examples of the successful utilization of sensorgenerated contextual data, the identification of patterns in such data for the purpose of harnessing them to make predictions is still not commonplace in everyday applications (Sampath et al., 2019).

The data generated by sensors can be used to make sense of past events and also to predict future events. Although making predictions is an established practice in organizational decision-making (Aldahiri, et. al., 2021; Deming, 2000; Kim et al., 2018), predictive analytics applications that utilize sensor data are a relatively recent phenomenon. Predictive analytics refers to the use of data to predict future trends and events. It uses historical data to forecast potential scenarios that can help inform strategic decisions. Predictive analytics using contextual data differ from traditional analytics methods in the way in which data are collected and used (Nardi, 1996). Predictive analytics using contextual data extract data from sensors, which are often custom designed to obtain specific data types. These sensors can generate and collect a wide range of data, including readings on temperature, water levels, air moisture, fuel levels, electrical impulses, and a host of other metrics, depending on how and where they are deployed and the needs at hand. The growing demand for additional trusted data sources to be utilized by predictive analytics systems has led to the development of new sensors and smart devices that can generate contextual 

#### 5 Evaluation of the CAPS Framework

One approach to evaluating the CAPS framework would be to present the framework to relevant industry experts and ask them to comment on the benefits and utility of the framework (Dey, 2001). A more robust approach would be to utilize the framework to build context-aware predictive systems in an actual company. We took the latter approach, and we describe in this section how we utilized the CAPS framework in a development project at MAN Diesel & Turbo to design multiple artifacts. Figure 6 depicts the evaluation strategy and the design process. We built three artifacts with the goal of reducing forecasting errors by including sensor-based data. We also designed two additional artifacts that included a more advanced use of sensors. The following section provides a short summary of the design iterations and describes the five artifacts.

Due to differences between candidate solutions in our case, multiple context-aware artifacts had to be built: some solutions could be completely implemented and evaluated within the period of the project, while others could only be evaluated, based on the current knowledge (see Figure 6). Following the CAPS framework, the initial step, goal definition (see Figure 5), calls for a thorough evaluation of the environment to determine what makes the predictive design suitable for a given context and how to quantitatively measure the cost associated with prediction errors. The following two steps, IT artifacts building and model evaluation, are executed for designs under evaluation using the previously defined evaluation criteria (i.e., the cost of prediction errors, contextual systematic bias, and efficacy). We suggest starting with a state-ofthe-art solution from the knowledge base to provide a baseline and ensure the necessary grounding in previous academic work. The model evaluation steps (Steps 3a, 3b, and 3c—see Figure 5) should then justify and evaluate the previously developed objective function as well as identify variables that are not monitored, perhaps introducing a systematic bias that can be removed in subsequent design iteration. When iteration cycles provide a satisfactory output, the environment and the installed base can be fed back with the newly designed predictive framework and the insights acquired during the design process.

#### 5.1 Settings and Context of the Evaluation

MAN Diesel & Turbo is the world market leader for very large diesel engines for use in ships and power plants, and it is one of the three leading suppliers of turbo machines. The roots of the company go back to

1758. In the years 1893-1897, Rudolf Diesel and MAN engineers developed the first diesel engine, and in 1904 the company constructed its first steam turbine. MAN Diesel & Turbo is a market leader—MAN has designed about 70% of the world’s engines for active goods-carrying vessels, culminating in about 85% of the seaborne share of world trade (IHS Global Services, 2009). Overall, MAN engines propel more than half of world trade (Maritime-Insight, 2013). Since the 1980s, MAN Diesel & Turbo has ceased building engines and the manufacturing process has been outsourced mainly to Asian business partners. The company’s strategy concentrates on (1) engineering-intensive engine design processes, (2) creating revenues from selling manufacturing licenses to third parties to build MAN engines, (3) generating revenue from engines in use, and (4) shifting the focus to the aftersales part of the business—namely, offering spare parts and services (Song & Zipkin, 1996).

The focus on aftersales has introduced challenges to MAN’s supply chain, especially in forecasting spare parts and service demand. Aftersales-based business models usually involve a higher level of heterogeneity and product variation than initial sales environments, leading to higher levels of demand uncertainty and making demand predictions relatively more difficult (Teunter et al., 2011). Moreover, in the marine business design, changes introduced in the manufacturing process are widespread, typically due to local material availability or shipyard manufacturing limitations, causing alterations in instantiations of the same design and additional variation of the installed base (e.g., Dekker et al., 2010; Minner, 2011). Finally, the license-based business model implemented by MAN creates additional obstructions to aftersales activities because it introduces the engine builder (i.e., MAN licensee) as an intermediary between MAN and the end customer (i.e., ship owner). Thus, the engine builder both partners with MAN in the production phase and competes with MAN on the aftersales market of spare parts. This setup limits the information flow between customers and MAN and also challenges the current process of spare parts demand forecasting. All of the above is considered in the CAPS framework as organiz

#### 6 Discussion

The application of the CAPS framework to the case provided an opportunity to evaluate the framework and engage in further reflection. Our experience with its application and evaluation in the MAN Diesel & Turbo case offers the opportunity to develop knowledge propositions that could be helpful in designing similar predictive systems in other companies and other problem domains. The propositions aim to help organizations implement the CAPS framework and realize its value in their context.

The first proposition stems from our design decision to utilize sensor data from already established sources and other data already collected for a different purpose. This approach not only greatly lowers the cost and simplifies the implementation process but also ensures a certain level of data quality; if the data are already in use, they are being reviewed, and some potential quality issues might be spotted and corrected. The risk factor for the investment is also significantly lower; at the time of design, the exact format and structure of the data were available, helping to avoid any surprises in terms of practical sensor limitations.

Generalizing these observations beyond the discussed case led us to formulate the first proposition for designing context-aware predictive systems:

Proposition 1 (infrastructure reusability): Readily available sensor data streams should be utilized to cut infrastructure costs, reduce system complexity, and ensure a certain level of data quality.

While developing an activity-sensor-based predictive system, our focus was on data quality and data estimation methods. Our experience shows that when sample size and data quality problems are predicted upfront, they can be mitigated, for example, by redesigning sensor infrastructure or data projection, capturing essential relationships from a small data sample, and encapsulating it into an estimation function (as in our implementation of activity sensor design). Generalizing these observations beyond the discussed case led us to formulate the second proposition for designing predictive systems:

Proposition 2 (data quality): Data quality measurement mechanisms should be provided as soon as possible to substantiate the predictive algorithms’ assurance and mitigate prediction validity concerns.

The key takeaway from investigating a multisensor continuous monitoring system is that when using sensor technologies, it is crucial to be clear about what the most interesting variable data to sense is and how this sensing activity should be implemented. Our example has shown that when a system measures a phenomenon of interest through a proxy measure, such as measuring the wear of piston rings from the temperature surrounding the rings, the process of analyzing the collected data might be both significantly and unnecessarily hindered. Generalizing these observations beyond the discussed case led us to formulate the third proposition for designing predictive systems:

Proposition 3 (choice of sensors): Sensors that measure metrics of interest should be selected to optimally balance between artifact predictive ability and complexity.

The insights related to implementing a remote monitoring interface evolve around the cost of forecasting errors. In the IoT world, it is common to dive into a sensor project merely because such projects are popular, without a welldefined project plan and benefits definition. For MAN, the design proved to be quite expensive, in terms of both initial implementation and running cost of the system, while some steps along the way were not completely focused on what factors added the most value. In general, the benefit of having the system in place must outweigh the cost, but this can only happen in an environment wherein the cost of prediction is very high and can be optimized. Generic solutions, such as our baseline approach or those presented in the literature review section, will sometimes be more affordable to implement, as they do not always require investment in new sensor infrastructure. This leads us to suggest that sensor-based predictive systems will usually be feasible for environments with high prediction error costs, typically characterized by high uncertainty, and we have formulated that observation as the fourth proposition for designing predictive systems:

Proposition 4 (contextual features): Context-aware predictive features should be developed to improve prediction quality only when the estimated cost of prediction errors is higher than the implementation cost.

#### 7 Conclusion

Although digital sensing technologies have become ubiquitous and increasingly embedded in industrial environments, the ubiquity of smart objects that produce ever-growing streams of contextual sensing data still presents challenges for forecasting systems. We applied a design science research methodology to develop a framework for predictive analytics on contextual data. Specifically, we developed a framework and a set of propositions for designing and evaluating context-aware predictive systems. The framework can be generalized to similar problems in related industrial domains.

Clearly, the usability and value of the proposed framework depend on its applicability to other case environments. Although a single case inherently poses a threat to external validity and generalization, in this study, the case-anchored system development and evaluation served as a proof of concept and an exemplification (Zhang et al., 2002). Additionally, the scope of the framework’s application may be perceived as somewhat limited, given that it focuses on predictive analytics of context-aware data. However, the growing availability of contextual information and the rapid expansion of sensor-based technologies will likely help popularize predictive analytics with sensors.

Future work could focus on further replication and validation of the framework in new environments by instantiating it in different cases. MAN Diesel & Turbo is a large global company and a market leader in its target market; thus, the experience of the CAPS framework in the MAN case can perhaps translate to new insights regarding predictive m

# Audit 23: A generic framework for sentiment analysis: Leveraging opinion-bearing data to inform decision making

- Group: `near_miss_three_gates`
- Model decision: `False`; centrality `mixed`; layer `software_system_or_artifact`
- Gates: `{"purposeful_solution_design": true, "objective_metric_is_primary_target": true, "comparative_improvement_demonstrated": true, "objective_improvement_is_the_success_basis": false}`
- Model reason: Gate1-3通过：作者提出并实现了ECCO情感分析框架/系统，以分类准确率为显式目标之一，并在四个数据集上相对于词典方法、无预处理基线和文献基准展示了比较性改进。但Gate4不通过：论文的中央贡献是综合决策支持框架，成功依据既有客观准确率改进，也有对分析组件/可操作洞察的定性示例；客观指标不是唯一或绝对主导的成功基础，因此centrality为mixed，严格保留条件不成立。
- Source: `E:\github\qual-llm-check-IS-utd\database_fulltext_all\03102_2020_a-generic-framework-for-sentiment-analysis-leveraging-opinion-bearing-data-to-inform-decision-ma.md`

### A generic framework for sentiment analysis: Leveraging opinion-bearing data to inform decision making

Jacqueline Kazmaier<sup>1</sup>, Jan H van Vuuren

Stellenbosch Unit for Operations Research in Engineering, Department of Industrial Engineering, Stellenbosch University, Private Bag XI, Matieland, 7602, South Africa

<sup>1</sup>Corresponding author.

E-mail addresses: jqkazmaier@gmail.com (J Kazmaier), vuuren@sun.ac.za (JH van Vuuren)

## Abstract

The increased exposure of the average citizen and customer to polarised content from various sources has been of significant consequence for companies and governmental organisations. Such content has, for example, served as a catalyst for violent uprisings and shifts in stock market prices. The collection and study of opinion have therefore become a necessity in many industries. Due to the vast nature of such data, however, manual approaches to this problem are no longer feasible. Several computational approaches have been proposed within the field of sentiment analysis, which successfully address many aspects of this problem, such as the classification of data into one of several sentiment categories. The research in the field is lacking, however, with respect to the integration and application of these techniques in practice, as well as their incorporation into the decision-making process of affected entities. In this paper, a generic framework for sentiment analysis is proposed, with a focus on facilitating the model development process for a user in a manner such that good performance may be achieved irrespective of the problem domain, as well as facilitating a flexible, exploratory analysis of model results in combination with existing structured attributes in order to gain actionable insights. The objective of the framework is to aid organisations in successfully leveraging unstructured, opinion-bearing data in combination with structured data sources to inform decision making.

Keywords: Sentiment analysis, Machine learning, Natural language processing, Decision Support Systems

## 1. Introduction

Public opinion has long been an area of research interest. With the exponential growth of the Internet and social media, and the resulting increase in the volume of user-generated content publicly available online, this interest has become even more pronounced. Concomitantly, however, the process of manually studying such content has become increasingly cumbersome.

This situation gave rise to the research field of sentiment analysis or opinion mining — the computational study of people’s opinions, attitudes

#### Abstract

The increased exposure of the average citizen and customer to polarised content from various sources has been of significant consequence for companies and governmental organisations. Such content has, for example, served as a catalyst for violent uprisings and shifts in stock market prices. The collection and study of opinion have therefore become a necessity in many industries. Due to the vast nature of such data, however, manual approaches to this problem are no longer feasible. Several computational approaches have been proposed within the field of sentiment analysis, which successfully address many aspects of this problem, such as the classification of data into one of several sentiment categories. The research in the field is lacking, however, with respect to the integration and application of these techniques in practice, as well as their incorporation into the decision-making process of affected entities. In this paper, a generic framework for sentiment analysis is proposed, with a focus on facilitating the model development process for a user in a manner such that good performance may be achieved irrespective of the problem domain, as well as facilitating a flexible, exploratory analysis of model results in combination with existing structured attributes in order to gain actionable insights. The objective of the framework is to aid organisations in successfully leveraging unstructured, opinion-bearing data in combination with structured data sources to inform decision making.

Keywords: Sentiment analysis, Machine learning, Natural language processing, Decision Support Systems

#### 1. Introduction

Public opinion has long been an area of research interest. With the exponential growth of the Internet and social media, and the resulting increase in the volume of user-generated content publicly available online, this interest has become even more pronounced. Concomitantly, however, the process of manually studying such content has become increasingly cumbersome.

This situation gave rise to the research field of sentiment analysis or opinion mining — the computational study of people’s opinions, attitudes and emotions [1].

The potential applications of sentiment analysis are vast and powerful. Polarised content on the Internet has swayed public elections, led to events of mass activism, such as the Egyptian Revolution, and has significantly impacted the reputation of various organisations, with shifts in sentiment on social media having been shown to correlate with shifts in the stock market [1, 2, 3]. The collection and study of opinion, using both external data from the Internet and internal data such as direct customer communication, have therefore become a necessity in many industries [1].

While there is an abundance of research dedicated to developing algorithms for the purpose of classifying sentiment, little guidance exists on how to apply these algorithms in practice, as well as how to incorporate model results into the decision-making process of affected entities.

Existing frameworks for sentiment analysis in the literature focus on the implementation of a specific model with a predetermined set of features. The fact that the classification performance of such a model depends on the domain in which it is applied, as well as the feature set employed as input [4, 5], is typically not addressed by these frameworks. Furthermore, the process of tuning the parameters of machine learning models, in particular, is rarely included in such frameworks in spite of it being an essential part of the model development process [6].

Moreover, only few frameworks go beyond simple summaries of the proportional representation of specified sentiment classes as determined by the results of a given classification model. In order to effectively leverage sentiment analysis in an organisation, a deeper analysis of the model results is required, focusing on the topics discussed in reviews and the relationship between sentiment and various additional sources of information that may be available.

In this paper, a generic framework for the evaluation of unstructured, o

#### 3. The proposed sentiment analysis framework

In this section, our sentiment analysis framework is presented in detail. A generic data science paradigm is first described, within which the proposed framework is set. Subsequently, a high-level overview of the proposed framework is given, and this is followed by a detailed description of its primary components using data flow diagrams (DFDs).

#### Figure 1: A high-level abstraction of a generic data science paradigm.

Raw data are provided by the user via the GUI. The data collection step of the data science process is therefore assumed to have already been completed by the user. These data are then processed by $m _ { 1 }$ functionally coherent modules residing in the processing component, which may perform several tasks, including data cleaning, data transformations (e.g. of unstructured data into structured data) and normalisation. This component thus incorporates the data processing and data cleaning steps of the data science process.

Processed data are then provided as input to the modelling component. The $m _ { 2 }$ modules residing in this component perform tasks related to the model building and evaluation step in the data science process. The nature of the models included in this component is determined by the objectives of the particular study and may include classification models, regression models and traditional forecasting models. Of the, possibly several, models evaluated and compared during this process, the selected model may then be applied to new data to obtain a classification for each new observation.

In order to extract valuable information and insight from these results, however, a subsequent analysis of the results is necessary. This may take the form of a simple visualisation of results or a more complex analysis aimed at identifying patterns explaining the model results. Such functions are performed by the $m _ { 3 }$ modules residing in the analysis component, as shown in Figure 1. The resulting information is then communicated to the user by means of the GUI, reflecting the communication of results step of the data science process.

Throughout the execution of the modules in the processing, modelling and analysis components, data may be stored in and retrieved from a common database in order to reduce the interdependence between the modules in each of these components. The processed data may, for example, flow from the processing component to the database where they may be retrieved by the modules in the modelling component. The data flows in Figure 1 are shown to flow directly between model components merely for the sake of intuitive understanding. Furthermore, user input may be elicited and feedback given to the user at any stage of the process. The modules need not be executed sequentially, and can also be implemented in an iterative fashion, incorporating user input and allowing the user to alter this input after having observed the effects of changes to the input. In this manner, users may perform, to some extent, the exploratory data analysis step of the data science process. User interaction is, however, not required, as indicated by the dashed lines in Figure 1.

#### 3.5. The analysis component

The working of the final component of the ECCO framework, the analysis component, is illustrated in Figure 7. It comprises six modules, numbered 13.0 18.0 , which are designed to facilitate the analysis of the results returned by the sentiment classification model selected by the user. This component thus aims to execute and enrich the process of sentiment summarisation. Module 13.0 facilitates the deployment of the selected model, taking as input the unlabelled documents that have been processed by modules 1.0 5.0 and the model that was developed in modules 6.0 12.0 , and returning the sentiment class assigned to each document by the model. These results are stored in a local database for later use by other modules in the analysis component. Modules 15.0 and 16.0 are aimed at analysing the unstructured, textual component of the data, whilst modules 17.0 and 18.0 facilitate an investigation of the relationship between the structured, supplementary data attributes and the documents’ sentiment classification. Finally, Module 14.0 enables the user to filter the results of the analyses in modules 16.0 18.0 according to the outputs of Module 15.0 .

Figure 7: Level-one DFD of the analysis component.

In Module 15.0 , the corpus is analysed in terms of its underlying topics or frequently occurring key words. As is shown in the level-two DFD in Figure 7, this entails first performing topic analysis and then visualising the sentiment exhibited for each of the identified topics. Topics may be extracted using dependency trees, noun phrase extraction or topic modelling techniques such as LDA. In the latter case, model hyperparameters may have to be specified by the user. Additionally, topics may also be identified manually by the user. The visualisation of selected sentiment-topic relationships may take the form of a histogram or alternative representations such as rose plots or low-dimensional representations of word distributions.

Figure 8: Level-two DFD of the analysis component.

Module 16 is responsible for generating the summaries typically associated with text mining for the current selection of data. Such traditional summaries take the form of textual summaries, which are generated using either template instantiation or passage extraction, or visual summaries, either of which is typically accompanied by sample documents for a clearer overview. These summaries may also make use of the topics discovered by Module 15.0 in order to give a more detailed overv

#### 4. Case study experiments

In order to demonstrate the potential of the proposed ECCO framework, an instantiation of the framework was implemented in the form of a computer program and applied to four case studies from four different domains. To this end, generic components of the framework were populated with specific algorithms and elements in order to illustrate the functionality of the framework. The resulting program, called the ECCO system, is an example of the type of DSS that may be developed using the ECCO framework as a blueprint.

The system was developed in Python 3.7. Data were stored, where applicable, in DataFrame constructs native to the Python library Pandas or arrays native to the Python library Numpy. Three different application frameworks were employed during the development of the ECCO system. The first is Qt, which was used to develop the user interface that houses the processing component and the sentiment modelling component of the ECCO framework. The Tensorboard framework was used to visualise the performance of deep learning models during the hyperparameter tuning process. Finally, the Dash web application framework was used to implement the analysis component of the ECCO framework, which executed by means of a user interface hosted on the user’s web browser. Machine learning models were implemented by means of the Scikit-learn and Keras libraries. Any additionally employed packages are described later along with their functions.

In this section, a brief description of the case study data is first given. This is followed by illustrative examples of case study experiments performed on the data, which showcase the working of the framework. These examples are partitioned according to the three primary components of the ECCO framework, related to (1) processing steps performed on the data, (2) the model development process and (3) the analysis and synthesis of results returned by a selected model in conjunction with structured data sources.


# Audit 24: Exploring Modes of Facilitative Support for GDSS Technology

- Group: `near_miss_three_gates`
- Model decision: `False`; centrality `dominant`; layer `none`
- Gates: `{"purposeful_solution_design": false, "objective_metric_is_primary_target": true, "comparative_improvement_demonstrated": true, "objective_improvement_is_the_success_basis": true}`
- Model reason: 该文是一项关于GDSS辅助支持模式的受控实验研究，比较了驾驶员驱动与促进者驱动两种人类支持角色对群体共识的影响。研究没有设计、构建或实质修改任何信息系统方案：SAMM是既有系统，操纵的核心变量是外部人类支持角色，而非IS制品或其功能。因此Gate 1（有目的方案设计）未通过。虽然客观共识指标确实是主要成功标准（Gate 2通过），并且chauffeur-driven相对facilitator-driven有显著改进证据（Gate 3通过），客观指标也是结论的主导依据（Gate 4通过），但中心贡献不是IS方案设计，故整体不保留。
- Source: `E:\github\qual-llm-check-IS-utd\database_fulltext_all\08946_1988_exploring-modes-of-facilitative-support-for-gdss-technology.md`

#### Abstract

The use of group decision support systems (GDSS) is rapidly growing. One key factor in the effectiveness of these systems may be the manner in which users are supported in their use of this technology. This paper explores two types of GDSS facilitative support: chauffeur-driven and facilitator-driven. In the former case, a person is used to reduce the mystique of the GDSS technology for users. In the latter case, a person assists the group with its group process in addition to reducing the mystique of the technology. The work unfolds a research story in which the original thinking of the research team to the effect that facilitator-driven GDSS facilitative support is superior is proven incorrect. The results of a pilot study caused the research team to reverse its thinking and hypothesize that, given the nature of the facilitation used and the task faced by the group, chauffeur-driven facilitation would have an advantage. The results of the experiment reported in this paper support this hypothesis. Arguments are presented to the effect that, to be effective in a judgment task environment, facilitation must be open and adaptive rather than restrictive.

Keywords: Decision support, electronic meetings, group support systems, group consensus, group facilitation

ISRL Categories: AA0902, AC0402, AI0105, HA0301

Introduction

Only recently has technology been introduced that is intended to support groups in their work. Does the manner by which groups new to such technology receive support in their interaction with the technology affect their performance? This research uses an experimental approach in attempting to answer this question. The evidence not only suggests that the answer is “yes,” but also suggests that to fully achieve the potential benefits of group technology, much more work on the subject of “support” is justified.

Recently, there has been a substantial amount of research activity on the subject of group decision support systems (GDSS). $^{1}$ Since 1988, GDSS research has been reported in a number of articles and conference proceedings (see George, et al., 1990, for a summary up to 1988. Other, more recent, examples include: Connolly, et al., 1990; Gallupe, et al., 1991; Grohowski, et al., 1990; Hiltz, et al., 1989; Ho and Raman, 1989; Mantei, 1989; Mennecke, et al., 1992; Nunamaker, et al., 1991; and Rao and Jarvenpaa, 1991). As reported in these sources, groups (or members of teams) interact to perform some sort of task. They are supported in the interaction by a set of computer hardware and software that constitutes the GDSS. In addition, support may be provided by a person who assists the group in using the GDSS. The literature, furthermore, reports that GDSS support takes various forms.

In some cases, the GDSS support involves a facilitator. In these instances, the facilitator directs the group members as to what GDSS features to use and when to use them. In other cases, the GDSS interaction may not be supported by a person and is user-driven. User-driven GDSSs give each group member full access to all system features at their workstations, which they can use in any way and in any order they wish. A less commonly used form of GDSS support is the chauffeur-driven approach. A chauffeur-driven GDSS involves an individual who, at the direction of the group members, implements features of the GDSS system for the group but does not assist the group with the process.

The purpose of this research is to shed some light on how a group's performance is affected by the type of support provided to groups interacting with a GDSS. This is an important issue for several reasons:

1. GDSSs represent a new technology for most individuals. GDSS users are likely to be unfamiliar with both the technology and, in many cases, the meeting process structure that may be associated with a particular GDSS (or provided by a process leader such as a facilitator). Thus, the manner in which GDSS technology is introduced and used (especially in an initial exposure) may have a significant effect on how the system is accepted and how successful its use is.

2. If the type of support provided to groups interacting with a GDSS is related to meeting effectiveness, then there are serious GDSS design (architecture) ramifications. At the one extreme, GDSSs that must be facilitated could be at a disadvantage compared to those without this requirement (and its associated process structure). At the other extreme, user-driven GDSSs may allow too much group process freedom and should be designed with some restrictiveness incorporated into the technology.

3. There is the possibility that GDSS research to date may (unintentionally) be presenting results that are an artifact of the type of GDSS support rather than the effect of the GDSS itself. In some cases, for example, the skill of a facilitator rather than the GDSS may have resulted in differences in GDSS outcomes.

4. Despite the considerable level of GDSS research activity noted 

#### H2: The groups will not differ in performance based on the person serving the role of the “guide.”

The other secondary hypothesis addresses an interesting point that bears significant importance when the experimental results are discussed later—the nature of the facilitator-driven process employed in the pilot study and carried through to the expanded study. The facilitator-driven role used in the pilot (and described more fully in the next section) was not “rich” or flexible. Rather, it was fixed and procedural. This type of role might be found in practice, such as when a facilitator follows a set script and closely adheres to features provided by a particular technology. This all suggests (and relates to Table 1), that facilitative task support needs to be expanded to structured task support and flexible task support.

This study considers only the structured facilitative task support. In the pilot study and in the expanded experiment, the facilitators primarily prescribed the steps to be used in performing the task and their order (which was based upon a theoretical “good” decision-making procedure—see the “Manipulations” section in this paper). Additionally, the facilitators made sure the group members clarified their individual positions and that the group was satisfied with the completeness of the various phases of their work. Had the facilitator role (as used in our experiment)

been richer and more flexible (thus idiosyncratic), a significant interaction between support mode and guide would be expected since one person might be a much better facilitator than another. The chauffeur role, on the other hand, is by its basic nature so non-prescriptive that it is hard to imagine why differences would occur according to the individual playing the role. For these reasons, the third hypothesis is:

H3: There will be no interaction effect between the form of GDSS support mode and the guides providing the support mode.

To test the major hypothesis and its underpinnings as well as the secondary hypotheses, an expanded experiment involving modes of GDSS support was conducted.

#### The Experiment

The previous material describes the background to this experiment and the pilot study, as well as detail about variables, measurement, and procedures. This section concentrates only on elaboration of and differences from the material presented thus far. A summary of the specifications for the expanded experiment is shown in Table 4. There were no differences among treatment groups in terms of demographic data such as age, gender, work experience, etc.

#### Method

The expanded experimental procedure differed in one important way from the one employed in the pilot study. For this experiment, individual allocation data was collected from the subject pool, and then groups were formed to meet certain pre-consensus standards. We wanted no extremely high or extremely low pre-consensus groups. Groups outlying in pre-consensus scores (> .40 or < .15) are rare, but with individuals randomly assigned to groups and groups randomly assigned to treatments, it is possible to lose some experimental control due to groups (or treatments) having great initial agreement or disagreement. Note in Table 3 that the user-driven pilot study treatment groups had much lower pre-consensus scores than either of the other treatments. The table also shows that chauffeured group number 1 had very high initial agreement compared to the other groups (and, in fact, was the only team to have a drop in its consensus score after the GDSS session).

By collecting individual pre-consensus data, then forming groups, and then assigning these groups to a treatment cell, we were able to obtain an initial balance on pre-consensus (both in terms of the score expected from any given group and the scores in any cell of the experiment). The pre-consensus scores used to analyze the experimental results, however, were the result of a second round of individual allocations made just prior to commencing the experiment (see below).

The subjects involved in this study were MBA students enrolled in several sections of an introductory course in information systems and decision sciences (see Table 4). Students from both day and evening sections participated in the study. During one class session, student participation was solicited and, for those agreeing to participate, the foundation task was administered. This took approximately 10 minutes. The allocations just described were used to form the students into three- to five- (in one case six-) person teams based upon pre-consensus scores. (As a result of this prodecure, many of the students did not know one another and had not worked together previously as a group.) Group size averaged five members, to be consistent with previous studies in the Minnesota GDSS research stream. One of the studies (Watson, 1987) found no differences in group performance in groups with three to four members. In this study, where there was variation in group size, the research results were analyzed for a size effect to ensure that group size d

#### Results

For the sake of completeness, Table 5 shows the entire set of pre- and post-consensus by each GDSS support mode and “guide.” In interpreting the results, the discussion, and the conclusions, several limitations should be noted. First, only one particular GDSS implementation, the SAMM system, was used. Other GDSS systems having different features, greater electronic intragroup communication features, or more advanced user interfaces could yield different results. Second, the results are based upon one non-intellective task involving allocation (affected by personal value systems) of funds. Third, the results stem from a “one-shot” use of the GDSS rather than ongoing use, such as might be made by a standing foundation awards committee. Fourth, very specific implementations of two facilitative modes were used. Clearly, modifications in how the GDSS was used can be expected to influence the results.

Table 5. Pre- and Post-Consensus Scores By GDSS Support Mode and Guide

<table><tr><td colspan="4">Facilitator-Driven</td><td colspan="2">Chauffeur-Driven</td></tr><tr><td colspan="6">Guide A</td></tr><tr><td>Group Size</td><td>Pre-Consensus</td><td>Post-Consensus</td><td>Group Size</td><td>Pre-Consensus</td><td>Post-Consensus</td></tr><tr><td>4</td><td>0.2371</td><td>0.2336</td><td>3</td><td>0.1847</td><td>0.3908</td></tr><tr><td>4</td><td>0.2296</td><td>0.3219</td><td>3</td><td>0.2432</td><td>0.4426</td></tr><tr><td>6</td><td>0.2305</td><td>0.3240</td><td>5</td><td>0.2085</td><td>0.5515</td></tr><tr><td>5</td><td>0.2917</td><td>0.3242</td><td>5</td><td>0.2045</td><td>0.7579</td></tr><tr><td>3</td><td>0.3352</td><td>0.4591</td><td>5</td><td>0.1683</td><td>0.8244</td></tr><tr><td>4</td><td>0.3370</td><td>0.5529</td><td>4</td><td>0.1710</td><td>0.8670</td></tr><tr><td>3</td><td>0.2764</td><td>0.6260</td><td>4</td><td>0.2372</td><td>0.8714</td></tr><tr><td>4</td><td>0.2512</td><td>0.6665</td><td>3</td><td>0.2212</td><td>0.9231</td></tr><tr><td>3.</td><td>0.1513</td><td>0.8549</td><td>4</td><td>0.2770</td><td>1.0000</td></tr><tr><td>Mean:</td><td>0.2600</td><td>0.4848</td><td></td><td>0.2128</td><td>0.7365</td></tr><tr><td colspan="6">Guide B</td></tr><tr><td>4</td><td>0.2454</td><td>0.2520</td><td>4</td><td>0.1835</td><td>0.2593</td></tr><tr><td>4</td><td>0.1740</td><td>0.2968</td><td>3</td><td>0.2274</td><td>0.4724</td></tr><tr><td>4</td><td>0.3171</td><td>0.3590</td><td>3</td><td>0.2721</td><td>0.4880</td></tr><tr><td>3</td><td>0.1876</td><td>0.4661</td><td>3</td>

#### Discussion

To set the scene for discussion it is worthwhile to recapitulate a few of the results. Some are direct restatements of what has been formally presented above. Others, however, have not been formally highlighted, but are of enough interest to deserve mention.

1. In two studies, the pilot and the expanded, the results show that chauffeur-driven groups had higher levels of post-meeting consensus than the facilitator-driven groups. H1 is therefore supported. The design of the present study did not include direct statistical comparison with the user-driven approach, but the overall results do lend support to the position that, in one-time use, user-driven systems are at a disadvantage to the other two support modes in achieving group post-consensus in our task environment.

2. Overall, there was no difference between the performance of the groups according to the person playing the guide role, thus H2 is supported.

3. H3 is also supported, and the results are worth looking at in more detail. First of all, examination of Table 5 indicates that Guide A had very high (0.74) post-consensus as a chauffeur. At first glance, it might appear that a significant result is present. However, examination of Table 6 shows that overall performance by the guides using the two support modes, coupled with the variability in the post-consensus scores, was such that the overall interaction effect was not statistically significant. This point is discussed later. Note also from Table 5 that Guide B's groups did perform slightly better (post-consensus = .56 vs .52) when she chauffeured the groups.

4. Groups that simply met in a room without any technology or process help had high levels of post-consensus (.55) performing the foundation task (Table 7). This is a high standard to meet, and, to date, only the chauffeur-driven GDSS support mode (.65) and the Watson, et al. (1988) manual groups (.62) have been able to do so.


# Audit 25: Integrating social networking support for dyadic knowledge exchange: A study in a virtual community of practice

- Group: `near_miss_three_gates`
- Model decision: `False`; centrality `dominant`; layer `none`
- Gates: `{"purposeful_solution_design": false, "objective_metric_is_primary_target": true, "comparative_improvement_demonstrated": true, "objective_improvement_is_the_success_basis": true}`
- Model reason: Gate 1失败：文章是观察性/准实验性的因果解释研究，利用Logclub平台已有的社交网络功能整合作为自然实验，作者没有设计、构建、实施或修改任何信息系统方案；尽管客观行为指标的原生性与比较改进证据充分（Gate 2、3、4通过），但这不是一篇提出或实质性修改IS方案的文章，因此不满足保留条件。
- Source: `E:\github\qual-llm-check-IS-utd\database_fulltext_all\01082_2015_integrating-social-networking-support-for-dyadic-knowledge-exchange-a-study-in-a-virtual-communi.md`

#### Abstract

Virtual community of practice (VCoP) is an important form of knowledge management systems. Would the integration of social networking support into traditional forum-based VCoP benefits knowledge exchange in the community? If so, why? Based on social capital theory and transactive memory system research, this study suggests that social networking support will enhance knowledge exchange in VCoP. In a field study, this study found social networking support intensifies dyadic knowledge excha d reduces the probability that dyads stop knowledge exchange. These findings empirically confirm the for practitioners.

Keywords: Virtual community of practice, knowledge management, online social network, knowledge sharing, knowledge exchange.

#### 1 Introduction

Typical employees spend a third of their time looking for information (Davenport & Lawrence, 2000). Managers spend up to two hours a day on this activity (Accenture, 2007). Facilitating knowledge seeking and sharing is an important element in boosting productivity Various knowledge management systems (KMS) have been deployed in organizations to support the capturing, storage, and exchange of knowledge (Xu, Kim, & Kankanhalli, 2010-2011). However, the usage of KMS often sees only limited success, plagued by problems such as low knowledge contribution intention (Kankanhalli, Tan, & Wei, 2005), low usage (Gray & Durcikova, 2006), and a cold environment where the interpersonal relationship between knowledge sharers and seekers is hard to maintain (Xu et al., 2010-2011).

#### 4 Methodology



#### 5 Discussion and Implications



#### 5.1 Discussion of Findings

This study seeks to propose a model to explain the effect of social networking integration on knowledge exchange in VCoPs. Based on social capital theory and transactive memory system research, we hypothesize that the effect of integration would be particularly salient for friend dyads in the community. Social networking support would make friends who did not communicate more likely to start knowledge exchange, it would make friends who had prior knowledge exchange more active in the activity, and it would make friends who had prior knowledge exchange less likely to stop exchange.

Our analysis of a real VCoP lent strong support to all three hypotheses. The differences in the birth rate, activeness, and death rate of exchange clearly indicated the effect of system integration. The unique staged implementation of social networking support in the VCoP and the use of difference-in-difference analysis allowed us to exclude alternative explanations of friendship effect and history effect. In sum, we empirically confirmed the effect of social networking technology on knowledge exchange because it can enhance members’ social capital and transactive memory.

With regard to the control variables, a larger difference between two participants the earlier member’s interest. A later member might judge the interest of an early member by her posts. However, the earlier member might have changed her interest. This mismatch in interest would decrease interactions. The difference in the number of threads had a positive effect on knowledge exchange. A plausible reason is that one member of the dyad is likely to be very active. Her activeness helps maintain an on-going exchange relationship between the two.

#### 5.2 Theoretical and Practical Implications

This study offers interesting theoretical insights. First, it enriches the social view of knowledge management by investigating the dyadic outcome of social relationships. Past literatures have confirmed the impact of social factors on knowledge sharing at individual level (Chang & Chuang, 2011; Chen, 2007; Chiu et al., 2006; Choi & Scott, 2013; Wasko & Faraj, 2005), but few have analyzed their dyadic outcome. However, in a social network, individual level behavior does not imply the same aggregate outcomes, due to the interdependent and sub-additive nature of collective action (Libai, Muller, & Peres, 2010). It is therefore important to provide direct evidence at the aggregate level. This study takes the research one step further in this direction.

Second, this study investigates the impact of an actual social technology on knowledge sharing. Usability and sociability represent two fundamental value dimensions of virtual communities (Phang et al. 2009). Both usability and sociability can be greatly facilitated by technologies. However, except for a few limited investigation of TAM factors (Lin, 2006; Phang et al., 2009; Sharratt & Usoro, 2003), the literature surprisingly shies away from more in-depth study of new technologies such as social networking support. This lack of research

#### 6 Conclusion

Would the integration of social networking support and forum-based VCoP benefit knowledge exchange in the community? If so, why? This study provides an answer to these questions. Based on social capital theory and transactive memory system research, this study suggests that social networking support will enhance knowledge exchange in VCoP. In a field study with a unique and advantageous data set, this study found that social networking support intensifies dyadic knowledge exchange among friends, and reduces the probabilities that dyads stop exchange. Our findings empirically confirm the effect of social networking support in enhancing social capitals in VCoP, provide a justification for investment in such a technology, and offer guidance for practitioners to evaluate the outcomes of a technology investment in the context of knowledge management in VCoP.


# Audit 26: Using “last-minute” sales for vertical differentiation on the Internet

- Group: `near_miss_three_gates`
- Model decision: `False`; centrality `exclusive`; layer `prescriptive_model_or_optimization`
- Gates: `{"purposeful_solution_design": false, "objective_metric_is_primary_target": true, "comparative_improvement_demonstrated": true, "objective_improvement_is_the_success_basis": true}`
- Model reason: Gate 1（purposeful_solution_design）未通过：文章是垄断者基于风险厌恶与质量差异的价格歧视理论模型，虽给出了最优定价/随机销售策略这一‘处方’，但未设计或实质性修改任何信息系统相关解决方案（没有系统、算法、接口、平台机制或可部署工件）。其他三个门在孤立意义下成立：利润是客观且主要的优化目标，文中通过证明和数值算例与确定性及非随机基准比较，且成功判据完全基于利润改进。但由于缺少被设计的IS方案，整体不满足严格保留条件，取保守排除。
- Source: `E:\github\qual-llm-check-IS-utd\database_fulltext_all\09906_2011_using-last-minute-sales-for-vertical-differentiation-on-the-internet.md`

#### 1. Introduction

In Internet-based commerce, sellers often use multiple distribution channels for the sale of standard consumer goods. For example, within a two-week period, Carnival Cruise Lines offered units of the same cabin class on one of its ships in three distinct ways: standard posted prices, ascending bid (“English”) auctions, and “last-minute” clearance sales. A possible explanation for such behavior is that sellers like Carnival are deliberately embedding price uncertainties into their sales channels in order to employ second-degree price discrimination among buyers who are risk-averse. Buyers who assign higher values to the offered product are typically more reluctant to risk compromising their surplus and are therefore prone to purchase at a higher posted price earlier, while buyers with lower values may wait and attempt to acquire the product at a bargain price.

The Internet has given buyers unprecedented ability to learn about sellers' behavior and use the information in order to search for the best deals. As a result, it is often imperative for online sellers to give careful consideration to strategic consumer behavior when these sellers determine their pricing policies. As an illustration of this, Fig. 1 depicts pricing data sampled from US Airways' website for economy-class travel from three cities in western New York (Buffalo, Rochester, and Syracuse) to Philadelphia. US Airways is the only airline offering nonstop services on these three routes. As the <sup>fi</sup>gure shows, the airline offered dramatically reduced e-Saver™ airfares on <sup>fl</sup>ights from Syracuse about 72 h before their departure but did not offer similar discounts on <sup>fl</sup>ights from either Rochester or Buffalo. Similar to the pattern shown by Fig. 1, the airline offered e-Saver™ discounts from Rochester, Buffalo, or

Syracuse to Philadelphia on 17 out of 35 consecutive weekends (or about 50% of the time) during our observation period.<sup>1</sup> It was not immediately clear to us whether in the presence of well-informed and sophisticated consumers US Airways could sustain a pricing policy that entailed charging advance-purchase prices of up to \$800 for a <sup>fl</sup>ight while offering “last-minute” fares of less than \$200 for a similar <sup>fl</sup>ight with high frequency.

According to our observations, US-based carriers such as American Airlines and US Airways offer special “last-minute” Internet fares only for travel in economy-class. However, some retail trave


# Audit 27: Performance Outcomes of Test-Driven Development: An Experimental Investigation

- Group: `excluded_objective_without_design`
- Model decision: `False`; centrality `mixed`; layer `none`
- Gates: `{"purposeful_solution_design": false, "objective_metric_is_primary_target": true, "comparative_improvement_demonstrated": true, "objective_improvement_is_the_success_basis": false}`
- Model reason: Gate 1失败：文章并非设计或实质性修改一个IS解决方案，而是评估已有的TDD实践与传统test-last方法的比较效果。Gate 4失败：文章的主要结论同时依赖客观软件质量提升和主观任务满意度提升，二者是并列的主要假设和贡献，客观指标并非唯一或主导的成功标准。中心性分类为mixed，因此不满足保留条件。
- Source: `E:\github\qual-llm-check-IS-utd\database_fulltext_all\13262_2020_performance-outcomes-of-test-driven-development-an-experimental-investigation.md`

### Performance Outcomes of Test-Driven Development: An Experimental Investigation

Vikram S. Bhadauria<sup>1</sup>, RadhaKanta Mahapatra<sup>2</sup>, Sridhar P. Nerur<sup>3</sup> <sup>1</sup>Texas A&M University Texarkana, USA, vbhadauria@tamut.edu <sup>2</sup>University of Texas Arlington, USA, mahapatra@uta.edu <sup>3</sup>University of Texas Arlington, USA, snerur@uta.edu

## Abstract

Despite the growing popularity of test-driven development (TDD), there is no empirical confirmation of the benefits that this contemporary practice confers on its users. Prior research findings on its efficacy have largely been inconclusive. We conducted a laboratory experiment to assess the impact of TDD on software quality and task satisfaction. Additionally, we investigated the productivity aspect of TDD as compared to the traditional test-last method of software development. Results indicate that software quality and task satisfaction are significantly improved when TDD is used. Despite the additional requirements of testing, TDD is not more resource intensive than the test-last method. We also examined TDD’s impact on learning post hoc and discuss the implications of our findings and directions for future research.

Keywords: Test-Driven Development, Software Quality, Developer Satisfaction, Learning, Experimental Design

Sandeep Purao was the accepting senior editor. This research article was submitted on March 25, 2017, and underwent two revisions.

## 1 Introduction

Ever since the agile manifesto was articulated (Beck et al., 2001), there has been a proliferation of development methods (e.g., Scrum and Extreme Programming) and their attendant practices aimed at enhancing the quality of software while satisfying the constraints of time and cost. Arguably, the most celebrated of these “best” practices is test-driven or test-first development, which advocates continuous cycles of test-code-refactor rather than the traditional, <sup>1</sup> linear approach of testing after performing analysis, design, and implementation. Not only does test-driven development (TDD) alter the workflow of development activities that were dominant for several decades, but it also forces developers to continually adapt their design strategies and the code that follows. An integral part of TDD is rapid feedback on the system being developed, which provides an opportunity to frequently inquire into what works and what doesn’t, and to evolve appropriate designs based on this reflection.

TDD’s emphasis on evolving test cases prior to coding is a significant departure from 

#### Abstract

Despite the growing popularity of test-driven development (TDD), there is no empirical confirmation of the benefits that this contemporary practice confers on its users. Prior research findings on its efficacy have largely been inconclusive. We conducted a laboratory experiment to assess the impact of TDD on software quality and task satisfaction. Additionally, we investigated the productivity aspect of TDD as compared to the traditional test-last method of software development. Results indicate that software quality and task satisfaction are significantly improved when TDD is used. Despite the additional requirements of testing, TDD is not more resource intensive than the test-last method. We also examined TDD’s impact on learning post hoc and discuss the implications of our findings and directions for future research.

Keywords: Test-Driven Development, Software Quality, Developer Satisfaction, Learning, Experimental Design

Sandeep Purao was the accepting senior editor. This research article was submitted on March 25, 2017, and underwent two revisions.

#### 1 Introduction

Ever since the agile manifesto was articulated (Beck et al., 2001), there has been a proliferation of development methods (e.g., Scrum and Extreme Programming) and their attendant practices aimed at enhancing the quality of software while satisfying the constraints of time and cost. Arguably, the most celebrated of these “best” practices is test-driven or test-first development, which advocates continuous cycles of test-code-refactor rather than the traditional, <sup>1</sup> linear approach of testing after performing analysis, design, and implementation. Not only does test-driven development (TDD) alter the workflow of development activities that were dominant for several decades, but it also forces developers to continually adapt their design strategies and the code that follows. An integral part of TDD is rapid feedback on the system being developed, which provides an opportunity to frequently inquire into what works and what doesn’t, and to evolve appropriate designs based on this reflection.

TDD’s emphasis on evolving test cases prior to coding is a significant departure from erstwhile approaches to software development. It must be noted that upfront testing is not simply a reordering of the phases of development but rather a design strategy (see Janzen & Saiedian, 2006) that reduces the time between thought and action, thereby fostering a climate for reflective practice (Schon, 1983). The test-code-refactor-test cycle provides immediate feedback on actions, is more conducive to opportunistic designs, and facilitates continual framing and reframing of the problem and its attendant solution. As the primary cornerstones of the TDD practice, immediate feedback and the capability to redesign rapidly not only engage developers but also enhance their satisfaction (see Tripp & Riemenschneider, 2014).

Empirical studies on the efficacy of test-driven development (TDD) abound (Rafique & Misic, 2013; Wilkerson, Nunamaker, & Mercer, 2012; Madeyski, 2005; Erdogmus, Morisio, & Torchiano, 2005). However, the findings are inconsistent, perhaps because of the varied methods used to study the effects of TDD. For the most part, these studies have focused on the outcomes of TDD, such as external solution quality measured in terms of defect reduction, rather than on the internal processes that this approach facilitates. In order to fill this void, our research uses an experimental study to investigate whether TDD does indeed outperform the traditional approach of softwa

#### 5 Research Methodology



#### 5.1 Experimental Design

We conducted a controlled laboratory experiment to validate the research model because it allows better control over potentially confounding extraneous factors, thus leading to precise measurements of the variables. The experiment involved two programming tasks—a warm-up task followed by the main task. The warm-up task required the participants to create an application for a movie rental business and the main task consisted of developing an application for a bookstore. Detailed task descriptions are provided in Appendices A and B.

Undergraduate and graduate students majoring in information systems or computer science participated in the experiment. Each participant was randomly assigned to one of the two groups. Participants in one group developed the solution using the traditional test-last method of software development, while participants in the other group used TDD for the same purpose. Randomization of the assignment was performed to ensure that the study was not influenced by any potential bias. Power analysis suggests a group size of 42 per condition for a large population effect size at a 0.05 significance level (Cohen, 1992).

Students participating in the experiment were already familiar with the traditional software development process but were not knowledgeable about TDD. In order to familiarize all students with the TDD approach, a tutorial session was offered by one of the authors. Following this session, the students completed an assignment on using JUnit test cases to verify that they had adequate knowledge and skills. Thereafter, they were allowed to participate in the experiment.

A total of 88 students participated in the experiment. Participation was completely voluntary. To encourage participation, extra credit was given to the students by their respective instructors. The students who chose not to participate in the experiment were allowed to complete an alternate assignment of equal credit. The experiment was conducted following a script that included informed consent and debriefing. Results from four participants were excluded from data analysis for various reasons. One person fell sick during the experiment and could not finish the main task. Three others did not completely respond to the questionnaire used for data collection. Thus, the final data analysis included responses from 84 subjects. The mean age of the participants was 26.06 years with a standard deviation of 5. Demographic details about the participants are shown in Ta

#### 5.2 Experimental Setting and Procedure

Prior to the main experiment, we conducted a pilot test using four subjects to clarify the experimental protocol. Two of the participants used TDD, while the other two followed the traditional method of software development. Minor changes were made to the protocol based on the feedback received from the pilot study. During the main experiment, participants were supervised to ensure that no socializing occurred. Based on the observations from the pilot test, the participants were allowed up to 30 minutes for the warm-up task and up to two hours to complete the main task. Laptop computers with Eclipse IDE (integrated development environment) were provided to all participants. JUnit test cases were enabled only in machines that were used by the participants using TDD. Internet access was disabled to prevent subjects from searching for solutions online. However, participants did have access to the JAVA API provided by Eclipse. Subjects in the control group were specifically instructed to use the test-last approach, whereas those in the treatment group were told to use TDD. The latter were informed that the JUnit test suite was already installed within the Eclipse environment on their computers. The control group did not have access to the JUnit test suite. All subjects were instructed to submit working code that met the stated requirements.

Table 2. Demographic Details of Participants

<table><tr><td>Demographic variable</td><td>Number of subjects</td><td>Percentage</td></tr><tr><td>Gender</td><td></td><td></td></tr><tr><td>Male</td><td>62</td><td>73.8%</td></tr><tr><td>Female</td><td>22</td><td>26.2%</td></tr><tr><td>Education</td><td></td><td></td></tr><tr><td>Undergraduate</td><td>49</td><td>58.3%</td></tr><tr><td>Graduate</td><td>35</td><td>41.7%</td></tr><tr><td>Programming experience</td><td></td><td></td></tr><tr><td>&lt;1year</td><td>46</td><td>54.7%</td></tr><tr><td>1 year-2 years</td><td>22</td><td>26.2%</td></tr><tr><td>2 years-3 years</td><td>9</td><td>10.7%</td></tr><tr><td>&gt;3 years</td><td>7</td><td>8.3%</td></tr><tr><td>Java experience</td><td></td><td></td></tr><tr><td>&lt; 1year</td><td>56</td><td>66.7%</td></tr><tr><td>1 year-2 years</td><td>19</td><td>22.6%</td></tr><tr><td>2 years-3 years</td><td>3</td><td>3.6%</td></tr><tr><td>&gt;3 years</td><td>6</td><td>7.1%</td></tr></table>

#### 6 Analysis and Results

The comparison between programmers using the testlast method of software development and those using TDD was designed to reveal important and significant differences between the two methods. MANOVA and ANOVA were used for identifying these differences between the two groups.

#### 6.1 Factor Analysis

Cronbach’s alpha is an indicator of internal consistency and homogeneity of a measured variable (Kerlinger, 1986) and values over 0.7 are considered adequate for assuming reliability (Nunnally, 1978). The four items used to measure overall task satisfaction were checked for internal consistency, and Cronbach’s alpha was found to be 0.956. Table 3 shows the mean values, standard deviations, and the correlation matrix for the items used for this perceptual measure. Exploratory factor analysis was performed using principal component analysis. All four items were found to load onto a single factor. Table 4 shows the factor loadings found as a result of using principal component analysis, along with Eigen value and variance explained. Since high factor loadings were found, a composite score for overall task satisfaction was used. The item scores were summated and then averaged to compute the composite score, which was used in the subsequent analysis.

#### 7 Additional Data Analysis

Our study clearly demonstrates the efficacy of TDD in terms of software quality and task satisfaction. However, some questions still remain. For instance, prior studies have been inconclusive regarding the effect of TDD on productivity. The question that presents itself is whether higher software quality and task satisfaction come at the expense of productivity. In addition, given similarities between TDD and Kolb’s experiential learning model (1976), it seems reasonable to expect that those engaged in TDD will experience greater learning outcomes. In this section, we inquire into these two questions:

1. How does TDD influence productivity?

2. Does TDD facilitate learning?

#### 8 Discussion

Our study demonstrates that the TDD approach results in enhanced software quality when compared with the test-last approach and that this gain in software quality occurs without any loss of productivity. Furthermore, we found that subjects who used TDD were more satisfied than those who adopted the test-last approach. These findings are consistent with our hypotheses derived from a review of the extant literature. The superior software quality generated by TDD users may be attributed to the fact that it is not just a different testing practice but a design strategy that facilitates improvisation, because design ideas embodied in the test cases are continually refined as the code unfolds. While these findings are interesting, it must be kept in mind that the subjects in our experiment had limited programming experience, and, therefore, the results of our study are likely more applicable to entry-level developers.

As discussed above, TDD’s cycle of software development is reminiscent of Kolb’s experiential learning model. Given the similarities between TDD and Kolb’s model, another plausible reason for the improved software quality of TDD users vis-à-vis subjects in the test-last condition is the greater opportunity for learning deriving from failed tests, adapting, and making necessary changes. The applicability of this finding to other domains such as product innovation is supported by a similar observation by Eisenhardt and Tabrizi (1995) that “iterations and testing would rapidly build understanding and create multiple options” (p. 104); they showed that an experiential strategy using repeated iterations with frequent testing and improvisation leads to faster product innovation. We believe that demonstrating/affirming such empirical regularity across disciplines and/or multiple domains is an import

# Audit 28: Using Self-Regulatory Learning to Enhance E-Learning-Based Information Technology Training

- Group: `excluded_objective_without_design`
- Model decision: `False`; centrality `dominant`; layer `none`
- Gates: `{"purposeful_solution_design": false, "objective_metric_is_primary_target": true, "comparative_improvement_demonstrated": true, "objective_improvement_is_the_success_basis": true}`
- Model reason: 该文设计并检验的是训练前和训练中纸质脚本这一教学干预，而非对e-learning系统或数字工件的修改；干预本质上是用于验证SRL理论的信息/激励性消息，不属于本筛选标准所要求的IS相关解决方案。因此Gate 1未通过。即使学习成果的客观改善很明显（Gate 2、3、4均通过），由于没有设计或实质性修改IS工件，不能保留。
- Source: `E:\github\qual-llm-check-IS-utd\database_fulltext_all\00256_2008_using-self-regulatory-learning-to-enhance-e-learning-based-information-technology-training.md`

#### Introduction

Almost every employee today has to be skilled in using information technology (IT); therefore, organizations continue to invest significantly in IT training for their employees, and universities offer many IT training courses for students (Agarwal and Ferratt 2001, Bureau of Labor Statistics 2004, Homer and Povar 2004, Piccoli et al. 2001). Given the extensive deployment of IT training in corporations and institutions, it is not surprising that information systems (IS) researchers expend substantial efforts to identify the most effective training methods and strategies (e.g., Agarwal et al. 2000, Bostrom et al. 1990, Compeau et al. 1995, Compeau and Higgins 1995a, Johnson and Marakas 2000, Olfman and Mandviwalla 1994a, Lim et al. 1997, Santhanam and Sein 1994, Venkatesh 1999, Yi and Davis 2003).

In recent years, IT training is increasingly being delivered through electronic means such as technology-mediated learning (TML) methods instead of through face-to face interactions between learners and trainers. TML as a training vehicle is growing rapidly because it is seen as a cost-effective way to deliver training at convenient times and at remote locations to large numbers of employees and students (Zhang et al. 2004). A study by the Sloan Consortium finds that educational institutions use TML extensively: 81% offer at least one fully online or blended course, and 34% offer complete technology-based degree programs (Allen and Seaman 2005). In practice, however,

TML has not provided the benefits that were originally anticipated; corporations, educational institutions, and IS researchers are thus very motivated to search for ways to improve TML effectiveness (Alavi and Leidner 2001, Gupta and Bostrom 2005, Moller 2002, Olfman et al. 2006, Sasidharan and Santhanam 2006).

IS researchers emphasize the exigency of conducting research on TML for several reasons. First, this research can build on and contribute to the cumulative knowledge developed by IS research on the interaction of IT and human problem solving and learning processes (Alavi and Leidner 2001, Leidner and Jarvenpaa 1995). Second, because IT training is an integral component of IS research, existing findings on how best to develop and test IT skills could contribute to our understanding of whether IT infrastructures are effective IT training platforms (Gupta and Bostrom 2005, Olfman et al. 2006). It can also help us research IT software aspects that provide new opportunities for the control and pac

#### Research Method

To test our hypotheses, we chose a laboratory experiment as the suitable approach. We performed a pilot test before we conducted the experiment (see Appendix 1).

Facilities, Target IT Application, and Participants Using an e-learning platform used in training employees and students, we conducted the experiment at a large public university. The IT training package provided a course on website design and development with Microsoft FrontPage software. In this course, learners proceeded through several modules as they underwent training in the conceptual elements and procedures used to set up websites. The training laboratory was similar to an IT training room, with 16 standalone computers in individual cubicles. Each participant, wearing a headset, completed the course independently, without interference from other learners. Training was interactive and delivered by audio and video components. The participant sequentially activated and completed the learning modules.

For our experiment, we selected eight consecutive modules from the course, providing enough information content to develop a website with linked pages and internal and external links. Each screen within a course module displayed a typical FrontPage interface with a box that described the screen layout and menu options. The participant was asked to choose one of the menu options, to type text, and to execute appropriate actions. The participant viewed the results. If satisfied, the participant hit the forward button and proceeded to the next screen, but could move backward or forward within the module at any time. After a module was completed, the participant moved on to the next one. Undergraduate business students participated over four semesters and were given course credit for volunteering. Students who had web-design experience were excluded, but were given course credit through other means. We next describe our experimental procedures and then provide details on the interventions and measures used in this study.

#### Experimental Procedures

Immediately after students volunteered for the study, they were given a background information survey that measured their individual learner traits and demographics (see Appendix 2). They were then assigned to one of the training sessions. Prior to starting the e-learning training, participants received either a treatment or control script. During the training session, they received feedback in the form of another treatment or control script. Thus, the combination of treatment or control scripts prior to and during training resulted in four different conditions: treatment-treatment $( \mathrm { T } _ { 1 } \ – \mathrm { T } _ { 2 } ) .$ , treatment-control $( \mathrm { T } _ { 1 } \mathrm { - } \mathrm { C } _ { 2 } ) .$ control-treatment $( \mathrm { C } _ { 1 } \mathrm { - T } _ { 2 } )$ , and control-control $( \mathsf { C } _ { 1 } \mathrm { - } \mathsf { C } _ { 2 } )$ We refer to the scripts provided prior to training as pretraining scripts and those provided during training as midpoint scripts (see Figures 3 and 4).

At their scheduled training session, participants were randomly assigned to receive either the treatment $( \mathrm { T } _ { 1 } )$ or the control $( \mathsf { C } _ { 1 } )$ pretraining script. They were given eight minutes to read the pretraining scripts and then they completed manipulation check measures on motivation to learn and computerlearning self-efficacy beliefs, described below. Next, participants received training through four modules of the e-learning system. As a pretext to provide participants with feedback, we asked them to answer five easy-to-answer multiple-choice questions on website design. The purpose was not to determine participants’ learning scores, but to demonstrate that our feedback was based on their performance. Therefore, after completing four modules, participants answered these questions and received feedback from the midpoint script (treatment [T ] or control [C ], randomly assigned). After reading this script, they continued through the next four modules. At the end of the eight modules they were asked to answer questions testing their declarative knowledge. Next they were asked to complete a hands-on performance task (see Appendix 3): to develop a website in about 20 minutes (the time determined in the pilot study).

We collected data through 16 experimental sessions. Participants spent an average of about 2 hours and 20 minutes completing the assignment: the background information survey took about 2

#### Results

Of the 134 participants who volunteered for the experiment, 10 were eliminated because of their prior Webdevelopment experience and six because of technical problems (their computers froze or their audio did not work). For the remaining 118 participants, the average age was 21.6, the average GPA was 3.3, and they were almost equally divided between males and females (see Table 1a). All had experience with popular software packages like Word and PowerPoint, but none had experience with Web-development software. As shown in Tables 1a and 1b, we found no significant demographic differences among the training groups. A factor analysis and validity checks of individual learner traits showed a high correlation between learning orientation and self-efficacy for self-regulation, and a lack of discriminant validity. Therefore, it was decided to drop the learning orientation measure and conduct the factor analy-

Table 1a Demographic Information

<table><tr><td>Demographic measures</td><td> $T_{1}-T_{2}$ </td><td> $T_{1}-C_{2}$ </td><td> $C_{1}-T_{2}$ </td><td> $C_{1}-C_{2}$ </td><td>Overall</td></tr><tr><td>Mean age (SD)</td><td>21.5 (1.7)</td><td>21.8 (2.0)</td><td>21.8 (1.7)</td><td>21.4 (1.5)</td><td>21.6 (1.7)</td></tr><tr><td>Mean GPA (SD)</td><td>3.3 (0.4)</td><td>3.3 (0.4)</td><td>3.2 (0.4)</td><td>3.3 (0.5)</td><td>3.3 (0.4)</td></tr><tr><td>Number of males</td><td>14</td><td>15</td><td>13</td><td>15</td><td>57</td></tr><tr><td>Number of females</td><td>22</td><td>10</td><td>12</td><td>17</td><td>61</td></tr></table>

Note. Treatment-treatment (T -T ), treatment-control $( \mathsf { T } _ { 1 } \mathsf { - C } _ { 2 } )$ , controltreatment $( { \complement } _ { 1 } \ – { \tilde { \mathbf { l } } } _ { 2 } ) .$ , control-control $( \mathsf C _ { 1 } - \mathsf C _ { 2 } )$

Table 1b Tests of Demographic Differences Between Conditions

<table><tr><td rowspan="2">Demographic measures</td><td colspan="3">Experimental conditions</td></tr><tr><td> $T_{1}-T_{2}$  vs.  $C_{1}-C_{2}$ </td><td> $T_{1}-T_{2}$  vs.  $T_{1}-C_{2}$ </td><td> $T_{1}-T_{2}$  vs.  $C_{1}-T_{2}$ </td></tr><tr><td>p values of differences in means test</td><td></td><td></td><td></td></tr><tr><td>Age</td><td>0.40</td><td>0.47</td><td>0.46</td></tr><tr><td>GPA</td><td>0.47</td><td>0.45</td><td>0.23</td></tr></table>

Note. Treatment-treatment $( \mathsf { T } _ { 1 } \cdot \mathsf { T } _ { 2 } ) ,$ treatment-control $( \mathsf { T } _ { 1 } \mathsf { - C } _ { 2 } ) _ { : }$ , controltreatment 

#### Discussion

Based on Alavi and Leidner’s (2001) framework, we examined the interaction of features of information technology, psychological learning processes, and instructional strategies embedded in an e-learningbased IT training environment. Because learners may not be exercising the high levels of self-directed learning strategies required in this training set-up, we developed instructional strategies that included interventions to induce learners to apply higher levels of self-directed learning strategies. Our tests showed that when the instructional strategy included such interventions that taught learners to self-regulate, learners applied more self-regulatory learning strate-${ \mathrm { g i e s } } ,$ leading to enhanced learning outcomes. We also found that during the training session, providing positive feedback to learners on their use of SRL reinforces the use of SRL strategies, suggesting that learners must be reminded and motivated if they are to continue using SRL strategies. Results show that the group instructed to follow SRL before and during training achieved the highest learning outcomes, whereas the group that received no instructions to self-regulate learning either before or during training received the lowest learning scores. Our results showed that all learners apply some level of SRL, but e-learning necessitates a higher level of SRL. Interventions like those examined in this study could induce learners to apply the higher levels of SRL needed in e-learning-based training contexts, thereby leading to higher learning outcomes.

Table 4 Learning Outcomes by Condition

<table><tr><td rowspan="2">Learning outcomes</td><td colspan="4">Experimental conditions</td></tr><tr><td>Treatment-treatment (T1-T2) (n = 36)</td><td>Treatment-control (T1-C2) (n = 25)</td><td>Control-treatment (C1-T2) (n = 25)</td><td>Control-control (C1-C2) (n = 32)</td></tr><tr><td>Mean outcome score (SD)</td><td></td><td></td><td></td><td></td></tr><tr><td>Declarative knowledge (Max = 15)</td><td>7.67 (2.50)</td><td>6.40b(2.18)</td><td>5.76a(2.31)</td><td>5.63a(2.87)</td></tr><tr><td>Hands-on performance (Max = 35)</td><td>30.56 (4.14)</td><td>29.56 (3.64)</td><td>29.16c(4.23)</td><td>28.12b(5.36)</td></tr></table>

Note. Means with superscripts a, b, and c differ from the corresponding treatment-treatment $( \mathsf { T } _ { 1 } \cdot \mathsf { T } _ { 2 } )$ condition at significance levels of 0.01, 0.05, and 0.1 respectively.

Based on past IS training research, we hypothesized that individual learner traits relating to SRL may influence learning outcomes. Our results did not support this premise. We found that the learning orientation and self-efficacy for self-regulation measures were correlated, perhaps because each of them taps into different forms of regulation. Although learning orientation taps into regulation relating to achievement motivation, and self-efficacy for self-regulation taps into academic motivation, they did not emerge as distinct measures and could not be tested simultaneously. We tested self-efficacy for self-regulation and computer-learning efficacy; these did not have direct or interactive effects on learning performance. One explanation can be found in the theory itself, which states that SRL is very situation specific and has to be activated in any given context, pointing to the importance of interventions. Learners who had higher self-efficacy beliefs for self-regulation and computer learning may not all have activated their self-efficacy beliefs in the new e-learning context. Another explanation for the lack of significant effects for individual learner traits can be found in the debates over the role of individual traits and their effects on learning performance. Researchers have argued that there is a marked difference in the effects of the distal trait variables when compared to the proximal state variables of the same construct (George 1991). Our findings, along with other prior findings, signal conflicting findings on the relationship between trait-like individual differences and learning performance, suggesting that we must investigate more closely the influence of traitlike measures of individual differences relating to selfregulation and learning performance.

Figure 5 Graphs of Learning Outcomes  
[image omitted]

[image omitted]  
Note. $\bar { \mathsf { I } } _ { 1 } { - } \bar { \mathsf { I } } _ { 2 } ,$ Treatment-treatment; $\bar { \mathsf { I } } _ { 1 } { - } \hat { \mathsf { G } } _ { 2 } ,$ treatment-control; $\mathsf { C } _ { 1 } - \mathsf { T } _ { 2 } ,$ controltreatment; $\mathsf { C } _ { 1 } { - } \mathsf { C } _ { 2 } ,$ control-control.

Table 5a Learning Outcomes for Pretraining Conditions

<table><tr><td></td><td colspan="2">Experimental conditions</td><td rowspan="2">Differences in means (t-tests)</td></tr><tr><td>Outcome measures for pretraining conditions</td><td>Treatment (n = 61)</td><td>Control (n = 57)</td></tr><tr><td colspan="4">Mean outcome score (SD)</td


# Audit 29: <b>Research Note</b>—An Investigation of the Appropriation of Technology-Mediated Training Methods Incorporating Enactive and Collaborative Learning

- Group: `excluded_objective_without_design`
- Model decision: `False`; centrality `mixed`; layer `none`
- Gates: `{"purposeful_solution_design": false, "objective_metric_is_primary_target": true, "comparative_improvement_demonstrated": true, "objective_improvement_is_the_success_basis": false}`
- Model reason: Gate 1 失败：文章是理论驱动的实验研究，比较现有训练方法，作者没有设计、构建或实质性修改信息系统工件；WBT 是商业产品，协作指导是教学方法而非数字工件。Gate 2 和 Gate 3 在狭义上部分通过：认知知识测验分数是客观且为假设中的主要结果之一，且 WBT 相对视频有显著提升；但 Gate 4 失败：文章的主要成功标准同时包括自我效能和过程满意度等主观构念，客观认知分数与主观结果同为主要结果，客观改进不是唯一或主导的成功依据。因此整体不满足保留条件，centrality 为 mixed。
- Source: `E:\github\qual-llm-check-IS-utd\database_fulltext_all\15010_2013_b-research-note-b-an-investigation-of-the-appropriation-of-technology-mediated-training-methods.md`

### Research Note—An Investigation of the Appropriation of Technology-Mediated Training Methods Incorporating Enactive and Collaborative Learning

Saurabh Gupta, Robert Bostrom,

## To cite this article:

Saurabh Gupta, Robert Bostrom, (2013) Research Note—An Investigation of the Appropriation of Technology-Mediated Training Methods Incorporating Enactive and Collaborative Learning. Information Systems Research 24(2):454-469. http:// dx.doi.org/10.1287/isre.1120.0433

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2013, INFORMS

Please scroll down for article—it is on subsequent pages

[image omitted]

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

### An Investigation of the Appropriation of Technology-Mediated Training Methods Incorporating Enactive and Collaborative Learning

Saurabh Gupta

Department of Management, Coggin School of Business, University of North Florida, Jacksonville, Florida 32224, s.gupta@unf.edu

Robert Bostrom

MIS Department, Terry College of Business, University of Georgia, Athens, Georgia 30602, bostrom@uga.edu

he growth in the application of information technology to student and employee learning underscores the need to understand the impact of technology-mediated learning (TML) methods. Using previous developed TML models, based on social cognitive theory and adaptive structuration meta-theory, the effectiveness of three training methods were examined in this study: technology mediated (using both vicarious and enactive learning), and collaborative and combined (collaborative plus technology mediated). The study also focused on the learning process. The experimental study results showed a significant positive influence of enactive learning enabled TML and collaborative training on specific training outcomes, and the combined training method shows positive results on all training outcomes. The study results also showed that faithful appropriation of the training methods during the learning process has a moderator effect on training outcomes. The study provides important research implications for theory and practice

Key words: technology-mediated learning; appropriation; simulation; e-learning; training; laboratory experiments; longitudinal research; collaborative learning

History: Vallabh Sambamurthy, Senior Editor; Radhika Santhanam, Associate Editor. This paper was received on April 6, 2009, and was with the authors 21 months for 5 revisions. Published online in Articles in Advance August 24, 2012.

## 1. Introduction

Training within organizations is one of the most pervasive methods for enhancing productivity of individuals and communicating organizations’ goals to new personnel. A recent meta-analysis reported a weighted effect size of training’s positive impact on behavior/skill change in business organizations as 0.60 to 0.63, a medium to large effect (Arthur et al. 2003). In 2010, U.S. organizations with 100 or more employees spent \$171.5 billion on formal training, with the highest amount being spent on information technology (IT) training (ASTD 2011). The importance and growth of IT training, makes it an ideal context to study the impact of new training methods such as technology-mediated learning (TML).

TML, also referred to as e-learning (a term that is used interchangeably with TML in 

#### 1. Introduction

Training within organizations is one of the most pervasive methods for enhancing productivity of individuals and communicating organizations’ goals to new personnel. A recent meta-analysis reported a weighted effect size of training’s positive impact on behavior/skill change in business organizations as 0.60 to 0.63, a medium to large effect (Arthur et al. 2003). In 2010, U.S. organizations with 100 or more employees spent \$171.5 billion on formal training, with the highest amount being spent on information technology (IT) training (ASTD 2011). The importance and growth of IT training, makes it an ideal context to study the impact of new training methods such as technology-mediated learning (TML).

TML, also referred to as e-learning (a term that is used interchangeably with TML in this manuscript), is “an environment in which the learner’s interactions with learning materials, peers, and/or instructor are mediated through advanced information technology” (Alavi and Leidner 2001, p. 2). TML has steadily grown over the last 10 years. For example, 40.1% of training of users on computer tools in 2010 was done through TML (ASTD 2011). There are similar trends in universities and other educational institutions. For example, over 5.6 million students took a TML class in the Fall of 2009 (Allen and Seaman 2010). In spite of this growth in TML, it has only recently attracted the attention of information systems (IS) scholars (Alavi and Leidner 2001, Sasidharan and Santhanam 2006).

The emergent research does not address three important issues. First, new technologies allow for a more immersive training experience in a simulated environment, which includes practicing the skills. Limited research exists on these simulated environments to provide a clear picture regarding their impact. Secondly, a review of literature points out that learning strategies are shifting toward a more active and team-oriented learning approach referred to as collaborative learning (Alavi et al. 1995). The few collaborative TML studies in IT training (summarized in Gupta et al. 2010) and Education (summarized in Lehtinen et al. 2003) have found mixed results. More collaborative learning research is needed in the IT training context and these mixed results need to be explained. Finally, recent researchers have called for an examination of the learning process (Alavi and Leidner 2001, Gupta et al. 2010).

This paper summarizes a theoretically grounded empirical research study that investiga

#### 2.2. Training Methods

The study compares different implementations of four training methods based on social cognitive theory across two axes: type of technology mediation and extent of collaboration. Technology mediation consisted of computer-based training conducted via an instructor led video recording or a Web-based training (WBT), and extent of collaboration consisted of either an individual learning or collaborative learning condition. The instructor led video with no collaboration training method was used as a baseline because most previous research had focus on this method and it is one of the most prevalent training methods used in business. The main interest of current study was the other three methods and how they compared to the baseline method.

Gupta and Bostrom (2009) outlined four distinct model constructs to understand any TML system: learning context, training method structures, learning process, and learning outcomes. The learning context is primarily comprised of the training goals and spirit of the training design. In this study, the learning goals deal with training participants in a specific information technology application software. The design spirit for the training methods came from the social cognitive perspective. The training method structures operationalized were enactive and vicarious training methods. The specific training method structural dimensions are discussed in subsequent paragraphs. The learning process is captured in terms of participant’s appropriation of the learning technology. The learning outcomes measure the extent to which participants have been trained in the software system in terms of cognitive knowledge, self-efficacy, and satisfaction with the learning process.

In this study, two similar TML training technologies were used to deliver video-based demonstrations: an instructor-led video recording and video demonstrations delivered through a WBT. The Gupta and

Bostrom (2009) model postulates that the implementation similarities or differences between training methods would be evident in their levels of structural dimensions. Although SCT does not identify structural dimensions explicitly, a review of the broader training literature and existing tools and manuals (a process suggested by DeSanctis and Poole 1994) identified eight SCT structural dimensions that are relevant to a TML environment. These dimensions are described in Table 1.

Four of these dimensions are primarily relevant to the implementation of vicarious learning

#### 3.2. Data Analysis

All constructs showed good convergent and discriminant validity as well as good reliability across all periods (see Appendix A). The data analysis involved a two-pronged approach depending on the nature of the hypothesis.

The first three hypotheses (H1–H3) focused on testing of mean differences across training methods. Traditional techniques, such as MANOVA, are ideally suited for such analysis because they use regression for differentiation (Maruyama 1997). Repeated measures MANOVA was used because repeated observations were taken of the same subject. Repeated measures MANOVA allows for interval independent variables, such as gender, initial motivation, etc. to be used as covariates (Hair 1998).

The second set of hypotheses (H4A–H4B) focused on the learning process and effect of training method appropriation on learning outcomes. WBT groups (TM2, TM4) were analyzed to see if the level of faithfulness of WBT structures had a moderation effect on learning outcomes, and collaboration groups (TM3, TM4) were analyzed to see if the level of collaboration had a moderation effect on learning outcomes. Here again, MANOVA was used to analyze the data. Median scores (after adding variables across time) for faithfulness of WBT structures appropriation (21.00), attitude toward WBT (52.00), and collaboration structures appropriation (101.00) were used to split the groups into high levels of appropriation and low levels of appropriation. Effect size was calculated using partial $\dot { \eta } ^ { 2 }$ where 0.009 constitutes a small effect, 0.058 a medium effect and 0.138 a large effect (Cohen 1988). In cases where degree of freedom of the numerator is one guidelines for eta-squared would be the square of these, i.e., 0.01 is a small effect, 0.09 a medium effect, and 0.25 a large effect (Levine and Hullett 2002).

3.2.1. Training Method Effects. The first task was to see if there was an overall treatment effect, i.e., did learning outcomes significantly differ across training methods? A one-way MANOVA revealed a significant multivariate main effect for training methods, Wilks  = 00852, F 41201225 = 50848, p < 00001, partial $\eta ^ { 2 }$ (partial eta-squared = 00052, and observed power = 0099). All the interval independent covariates had significant effect on the learning outcomes: intrinsic motivation $( p < 0 . 0 1 )$ , initial extrinsic motivation $( p < 0 . 0 5 ) .$ gender $( p < 0 . 0 5 )$ , and initial computer self-efficacy $( p < 0 . 0 1 )$

Given the signif

#### 4. Discussion

One of the key contributions of the study is a practical illustration of distinguishing two similar looking training methods through the concept of structural dimensions. More importantly, the study answered the following question using the structural dimensions comparison approach: Do Web-based training methods with higher levels of enactive learning dimensions have a greater positive effect than other technology-mediated training methods? The answer is “yes.” The WBT method featured higher levels of the enactive learning structural dimensions and had a positive impact on all learning outcomes except process satisfaction when compared to non-WBT methods.

There was a great variance in student satisfaction from the learning process $( \sigma = 3 . 8 9 , \ \bar { x } = 3 . 7 ,$ range = 2–7 on seven point scale). The variance is also captured in qualitative data gathered. One student commented “I would prefer to be taught by a human being than by a computer 0 0 0” and another commented $\bar { \cdot } \ldots . \mathrm { i t }$ really helped me develop into a real go getter. Thanks Element $\mathrm { K ! ^ { \prime \prime } }$ This indicates that some participants were very satisfied with the use of TML, and some were not. This indicates that individual differences and interpersonal dynamics might play an important role in training satisfaction. The discussion on individual attitudes toward technology discussed later in this section provides support for this assertion. Overall, the results suggest that trainers and researchers should focus on structured enactive learning (beyond practice) as an addition to behavioral training to enhance learning outcomes.

Paired learning is a relatively new method of training in IT training literature. This study used a much broader conceptualization of learning outcomes than the previous study, which looked at paired learning, in IT training (Yi and Davis 2001). When conceptualized with multiple learning outcomes, interpretation of the findings from this study shows that participants do indeed benefit from paired learning. Self-efficacy perceptions are improved, which may be due to the implicit comparison of skills between participants. In addition, participants were encouraged to teach each other. Pairs were also able to discuss and explore the software together as exemplified by this quote from a participant: “We were able to find new and cool charts through teamwork.” Such teamwork can alleviate the concerns that some students have regarding the impersonal nature of technology-based learning, enhancing overall satisfaction with training.

There was, however, no direct benefit from collaboration on cognitive outcomes. A possible reason for this could be the lack of initial development of collaboration dimensions as a part of the experimental design. Team development activities have been shown to enhance collaboration levels in GSS settings and could prove to be useful in training as well. We obtained some evidence to support this conjecture in the study. Levels of collaboration showed a positive change over time (mean $\Delta = 1 . 7 , ~ p < 0 . 1 0 )$ . As pai

# Audit 30: Computer-Related Task Performance: A new perspective

- Group: `excluded_objective_without_design`
- Model decision: `False`; centrality `exclusive`; layer `none`
- Gates: `{"purposeful_solution_design": false, "objective_metric_is_primary_target": true, "comparative_improvement_demonstrated": false, "objective_improvement_is_the_success_basis": false}`
- Model reason: Gate 1未通过：本文没有设计或实质修改任何IS相关解决方案；自我预言只是向被试提出的一个预测问题，属于社会心理学干预/信息提示，而非IS工件、算法、界面或平台机制。Gate 2在狭义上通过，因为二元任务正确性是主要客观因变量；但Gate 3未通过：处理组与对照组比较未显示显著改进，仅SP=1与SP=0的预测方向比较显著，不能证明干预本身改善绩效；Gate 4因此也不成立。该文本质上是理论驱动的行为实验，而非解决方案设计并验证客观改进的IS研究。
- Source: `E:\github\qual-llm-check-IS-utd\database_fulltext_all\04338_2016_computer-related-task-performance-a-new-perspective.md`

### Computer-Related Task Performance: A new perspective

Phil Longstreet <sup>a,</sup>\*, Xiao Xiao <sup>b</sup>, Saonee Sarker <sup>c</sup>

<sup>a</sup> University of Michigan – Flint, 2145 Riverfront Ctr W., Flint, MI 48502, USA

<sup>b</sup> Copenhagen Business School, Howitzvej 60, 2000 Frederiksberg, Denmark

<sup>c</sup> The University of Virginia, 125 Ruppel Dr, Charlottesville, VA 22903, USA

## A R T I C L E I N F O

Article history: Received 25 August 2014 Received in revised form 10 November 2015 Accepted 22 December 2015 Available online xxx

Keywords: Computer self-efficacy Self-prophecy Self-fulfilling prophecy Computer-related task performance

## A B S T R A C T

The existing information system (IS) literature has acknowledged computer self-efficacy (CSE) as an important factor contributing to enhancements in computer-related task performance. However, the empirical results of CSE on performance have not always been consistent, and increasing an individual’s CSE is often a cumbersome process. Thus, we introduce the theoretical concept of self-prophecy (SP) and examine how this social influence strategy can be used to improve computer-related task performance. Two experiments are conducted to examine the influence of SP on task performance. Results show that SP and CSE interact to influence performance. Implications are then discussed in terms of organizations ability to increase performance.

\- 2015 Elsevier B.V. All rights reserved.

## 1. Introduction

In the field of information systems (ISs), there has been an enduring interest in efforts to predict and enhance individuals performance on computer-related tasks. This is evident in models such as the task technology fit [17], among others, which articulates the relationships between task, technology, and individual characteristics and their impacts on task performance. A large body of work within the IS field has shown that computer self-efficacy or CSE [11] significantly influences individuals performance on technology-related tasks. Further, it has also been demonstrated that improving performance on a technologyrelated task requires extensive training to enhance an individual’s CSE. Despite the large volume of work on this subject, the ability of CSE to predict performance has not yet been fully explained. Moreover, studies conducted earlier have shown that CSE may occasionally exhibit contradictory results [12–14,24].

These contradictory results highlight the need for further research on CSE. One such study has argued that the construct 

#### 1. Introduction

In the field of information systems (ISs), there has been an enduring interest in efforts to predict and enhance individuals performance on computer-related tasks. This is evident in models such as the task technology fit [17], among others, which articulates the relationships between task, technology, and individual characteristics and their impacts on task performance. A large body of work within the IS field has shown that computer self-efficacy or CSE [11] significantly influences individuals performance on technology-related tasks. Further, it has also been demonstrated that improving performance on a technologyrelated task requires extensive training to enhance an individual’s CSE. Despite the large volume of work on this subject, the ability of CSE to predict performance has not yet been fully explained. Moreover, studies conducted earlier have shown that CSE may occasionally exhibit contradictory results [12–14,24].

These contradictory results highlight the need for further research on CSE. One such study has argued that the construct of CSE is multifaceted, consisting of internal and external components, and the reasons for contradictory findings surrounding CSE in the past could have been owing to a lack of understanding of these multifaceted components [42]. Thatcher et al. [42] further noted that additional research will be required to explicate how each of the facets interacts to influence task performance. Despite these findings, studies employing the multifaceted model still have reported inconsistent results, suggesting that additional models or moderating variables may be necessary to fully understand the nature of CSE and its influence on performance (see Table 1 for a summary of a sample of studies that help highlight the equivocal nature of CSE). To summarize, the ability of CSE to predict performance is still slightly ambiguous suggesting that it might be beneficial to examine if there are other relevant constructs in similar domains that can individually or in conjunction with CSE help explain performance.

An examination of the consumer psychology literature reveals one such relevant construct and highlights that the IS field is not alone in its desire to predict and influence individual performance and behavior. This particular construct represents a phenomenon whereby behavior is changed by merely asking people to make an a priori prediction about their performance [29]. This phenomenon is often referred to as self-prophecy (or SP

#### 3.1. Study 1



#### 3.1.1. Research method

In order to explore the effectiveness of the SP construct within the technological context and to test the first three hypotheses, we designed and conducted an experiment using student subjects. While students may not always be the ideal subject pool because of their limited knowledge base [28], for this study the use of student subjects was determined to be appropriate given that we needed a population that did not have prior exposure to the types of applications used in the study [21].

3.1.1.1. Subjects. For this study, 152 subjects were recruited from an introductory IS course within the College of Business at a large northwestern university in the U.S. Subjects varied in age from 18 to 38, with a mean age of 20.5. Approximately 64% of the subjects were male, with the remaining 36% being female. Subjects were given course credit for their participation in this research with no other incentives provided.

3.1.1.2. Experiment procedure. This study was based around a hypothetical summer internship to make it more realistic for the student subjects. The subjects were asked to imagine that they had been hired as a summer intern for an architecture firm, and that their job would be to determine the best architecture software application for the company to purchase when the company’s current architecture software license expired later in the summer. An excerpt from the script has been provided below.

You have been recently hired as a summer intern for an architecture firm that specializes in designing and building custom single-family homes. The company is currently contemplating acquiring a software application to help them with drawing designs, as well as managing the home building process. Your job will be to evaluate various different software packages that the company is thinking about purchasing, and as your first project, you will evaluate the technical specifications of two different architecture software packages that the company is considering acquiring.

For empirical evaluation of the proposed research hypotheses, we designed three experimental scenarios. In the first group, subjects were exposed to the SP instrument before the CSE construct, while in the second group this was reversed with the CSE instrument being introduced before the SP instrument. This split in the dataset was determined to be necessary because previous research on SP has suggested that exposure to the SP instrument could prime the subjects, thus introducing confounding influ

#### 3.1.3. Data analysis

The data were initially analyzed using a one-way analysis of variance (ANOVA) to test for significant differences in task performance between the treatment and the control group. The ANOVA showed no significant difference between the three groups (F = 0.211, p = 0.405), so the data from the two treatment groups were combined into one group for the remainder of the analysis.

Due to the presence of binary indicators, hierarchical logistic regression was used to tease out the interaction between SP and CSE. Table 4 shows the results of the analysis of the interaction between CSE and SP (Model 2).

From these results, model 2 shows that SP does not exhibit a significant effect on the task performance (p = 0.227), while CSE did have a significant influence on task performance $( p = 0 . 0 1 8 )$ The interesting result shown in this model, however, is the significant interaction between CSE and SP, $p = 0 . 0 4 1$ . Model 2 also shows a significant change in $R ^ { 2 } \left( p = 0 . 0 1 \bar { 8 } \right)$ , thus indicating that the inclusion of the interaction provides the ability to significantly explain a degree of the variance in the underlying model (model significance, p < 0.05). Finally, while it has been suggested that IT knowledge, decision confidence, and gender may influence task performance, the results of this study demonstrated that none of these control variables exhibited a significant influence on performance.

Correlations (n = 152).

<table><tr><td colspan="2">Variables</td><td>SP</td><td>CSE</td><td>DC</td><td>ITK</td><td>Choice</td></tr><tr><td rowspan="3">SP</td><td>Correlation</td><td>1.000</td><td>0.348</td><td>-0.225</td><td>0.242</td><td>0.137</td></tr><tr><td>Significance (two-tailed)</td><td></td><td>0.000</td><td>0.006</td><td>0.003</td><td>0.093</td></tr><tr><td>df</td><td>0</td><td>149</td><td>149</td><td>149</td><td>149</td></tr><tr><td rowspan="3">CSE</td><td>Correlation</td><td>0.348</td><td>1.000</td><td>-0.248</td><td>0.286</td><td>0.213</td></tr><tr><td>Significance (two-tailed)</td><td>0.000</td><td></td><td>0.002</td><td>0.000</td><td>0.009</td></tr><tr><td>df</td><td>149</td><td>0</td><td>149</td><td>149</td><td>149</td></tr><tr><td rowspan="3">DC</td><td>Correlation</td><td>-0.225</td><td>-0.248</td><td>1.000</td><td>-0.082</td><td>-0.123</td></tr><tr><td>Significance (two-tailed)</td><td>0.006</td><td>0.002</td><td></td><td>0.316</td><td>0.132</td></tr><tr><td>df</td><td>149</td><td>149</td><td>0</td><td>149</td><td>14

#### 3.1.4. Study 1 discussion

Study 1 shows that CSE has a significant effect on task performance and further shows the significant effects of interaction between SP and CSE. This interaction, when more closely examined, shows support for the supposition that SP moderates the influence of CSE on task performance. As shown, CSE does not show any significant effect on task performance for those individuals who predicted that they would perform the task well. However, CSE has a strong effect on task performance when the subject predicted that they would not perform the task well.

In study 1, students were performing in a structured environment, wherein they were only allowed to work on the specified task. However, this is probably not the case in the realworld working environment, where employees will not be restricted to only one task. Previous literature on organizational climate defines structure as ‘‘. . .the feelings that employees have about constraints in the group, how many rules, regulations, procedures there are. . .’’ ([23], pp. 81–82). In addition to being one of the key dimensions that define the organizational climate, it has also been found that organizational climate has an impact on individuals’ motivation to pursue a positive job outcome and hence affects the job performance [6]. Therefore, it may be beneficial to also study the effects of CSE and SP in an unstructured working environment.

[image omitted]  
Fig. 1. Moderating effect of SP on the relationship between CSE and task outcome.

#### 3.2. Study 2



#### 3.2.1. Research method

3.2.1.1. Subjects. As with the previous experiment, 257 students were recruited from an introductory IS course at a large northwestern university. These subjects were recruited during a different semester to minimize the overlap between studies. Subjects varied in age from 18 to 50, with a mean age of 20.3. Approximately 65% of the subjects were male, with the remaining 35% being female. Subjects were given course credit for their participation in this research study with no other incentives provided.

3.2.1.2. Experiment procedure. For this study, subjects were given the same scenario and asked to perform the same task as the subjects in study 1. However, the restrictions enforced in Study 1 to ensure that subjects only working on this task were removed. Instead, for this study, we handed out the instruction sheets to the subjects and then let them work on the task on their own; in a completely unrestricted classroom environment without the use of content monitoring and internet blocking we had employed in study 1. Further, students were allowed (but not encouraged) to interact with each other during this task. These conditions were deemed to be the closest to the actual world that we could achieve with student subjects in a classroom environment.

#### 3.2.3. Data analysis

As with the previous study, an ANOVA was conducted on the performance data from the two treatment groups and the control group. Results from this ANOVA revealed no significant difference (F = 0.236, p = 0.32) between the three groups. Based on these findings, the data from the treatment groups were once again collapsed to just one group for the remainder of the analysis.

Table 6  
Descriptive statistics (n = 257).

<table><tr><td>Variables</td><td>n</td><td>Minimum</td><td>Maximum</td><td>Mean</td><td>Standard deviation</td></tr><tr><td>SP</td><td>257</td><td>0</td><td>1</td><td>0.82</td><td>0.387</td></tr><tr><td>CSE</td><td>257</td><td>0.50</td><td>10.00</td><td>5.756</td><td>1.817</td></tr><tr><td>ITK</td><td>257</td><td>1.57</td><td>5.00</td><td>3.472</td><td>0.638</td></tr><tr><td>DC</td><td>257</td><td>1.00</td><td>5.00</td><td>2.637</td><td>0.776</td></tr><tr><td>Performance</td><td>257</td><td>0</td><td>1</td><td>0.56</td><td>0.497</td></tr><tr><td>Gender</td><td>257</td><td>0</td><td>1</td><td>0.63</td><td>0.483</td></tr></table>

Please cite this article in press as: P. Longstreet, et al., Computer-Related Task Performance: A new perspective, Inf. Manage. (2016), http://dx.doi.org/10.1016/j.im.2015.12.001

Table 7 Correlations (n = 257).

<table><tr><td colspan="2">Variables</td><td>SP</td><td>CSE</td><td>DC</td><td>ITK</td><td>Performance</td></tr><tr><td rowspan="3">SP</td><td>Correlation</td><td>1.000</td><td>0.179</td><td>-0.122</td><td>0.110</td><td>0.107</td></tr><tr><td>Significance (two-tailed)</td><td></td><td>0.004</td><td>0.050</td><td>0.078</td><td>0.087</td></tr><tr><td>df</td><td>0</td><td>254</td><td>254</td><td>254</td><td>254</td></tr><tr><td rowspan="3">CSE</td><td>Correlation</td><td>0.179</td><td>1.000</td><td>-0.165</td><td>0.360</td><td>-0.064</td></tr><tr><td>Significance (two-tailed)</td><td>0.004</td><td></td><td>0.008</td><td>0.000</td><td>0.305</td></tr><tr><td>df</td><td>254</td><td>0</td><t
