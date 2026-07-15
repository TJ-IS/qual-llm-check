---
otero_id: 7098
otero_key: "EQEMG87U"
title: "Does IT Matter to Acquisitions? The Impacts of IT Distance on Post-Acquisition Performance"
authors: "Kyunghee Lee; Kunsoo Han; Animesh Animesh; Alain Pinsonneault"
year: "2022"
journal: "MIS Quarterly"
doi: "10.25300/misq/2022/16039"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# DOES IT MATTER TO ACQUISITIONS? THE IMPACTS OF IT DISTANCE ON POST-ACQUISITION PERFORMANCE <sup>1</sup>




---
奥特罗 ID：7098
otero_key：“EQEMG87U”
标题：“IT 对收购重要吗？IT 距离对收购后绩效的影响”
作者：“李庆熙、韩建秀、Animesh Animesh、Alain Pinsonneault”
年份：“2022”
期刊：《管理信息系统季刊》
doi：“10.25300/misq/2022/16039”
查询：“构造”
来源：“https://ais.kexu.win”
图片下载：假
---
# 这对收购重要吗？ IT 距离对收购后绩效的影响<sup>1</sup>


Kyunghee Lee Department of Management and Information Systems, Mike Ilitch School of Business, Wayne State University, Detroit, MI, U.S.A. {kyunghee.lee@wayne.edu}




Kyunghee Lee 美国密歇根州底特律韦恩州立大学 Mike Ilitch 商学院管理与信息系统系 {kyunghee.lee@wayne.edu}


Kunsoo Han, Animesh Animesh, Alain Pinsonneault Desautels Faculty of Management, McGill University, Montreal, QC, CANADA {kunsoo.han@mcgill.ca}{animesh.animesh@mcgill.ca}{alain.pinsonneault@mcgill.ca}




Kunsoo Han、Animesh Animesh、Alain Pinsonneault Desautels 管理学院，麦吉尔大学，蒙特利尔，魁北克省，加拿大 {kunsoo.han@mcgill.ca}{animesh.animesh@mcgill.ca}{alain.pinsonneault@mcgill.ca}


Although researchers have examined the role of dyadic dynamics (i.e., interactions between the acquirer and the target firm) in the success of acquisitions, little attention has been devoted to the role of information technology (IT). In this study, we extend this literature by examining how pre-acquisition IT distance (i.e., the difference between the enterprise IT systems of the two firms that reflects the system incompatibility and resulting costs of system integration) affects the acquirer’s post-acquisition performance. To measure IT distance, we used a word-embedding technique to map each firm’s IT systems portfolio to a low-dimensional embedding space and calculate the distance between the firms in that space. Using data on U.S. firms’ acquisition activities over seven years, we found that IT distance is negatively associated with the acquirer’s post-acquisition performance. Also, the adverse effect of IT distance is stronger for acquisitions motivated by operational synergies, compared to those seeking nonoperational synergies. This finding supports our fundamental premise that IT distance disrupts postacquisition synergy creation, and more so when the combined firm has a greater need for tight integration to create acquisition synergies. This research contributes to the merger and acquisition (M&A) literature in management and IS by introducing a novel concept of IT distance and by theorizing and empirically examining its performance implications in acquisitions. The findings of this study can inform practitioners on how to devise IT strategies in corporate acquisitions to mitigate IT risks and achieve greater postacquisition performance.




尽管研究人员已经研究了二元动态（即收购方和目标公司之间的互动）在收购成功中的作用，但很少有人关注信息技术（IT）的作用。在本研究中，我们通过研究收购前的 IT 距离（即两家公司的企业 IT 系统之间的差异，反映系统不兼容性和由此产生的系统集成成本）如何影响收购方的收购后绩效来扩展该文献。为了测量 IT 距离，我们使用词嵌入技术将每个公司的 IT 系统组合映射到低维嵌入空间，并计算该空间中公司之间的距离。利用美国公司七年来收购活动的数据，我们发现 IT 距离与收购方收购后的绩效呈负相关。此外，与寻求非运营协同效应的收购相比，IT 距离的不利影响对于运营协同效应驱动的收购更为严重。这一发现支持了我们的基本前提，即 IT 距离会扰乱收购后协同效应的产生，尤其是当合并后的公司更需要紧密整合以创造收购协同效应时。这项研究通过引入 IT 距离的新概念，并通过理论分析和实证检验其在收购中的绩效影响，为管理和信息系统领域的并购 (M&A) 文献做出了贡献。本研究的结果可以帮助从业者了解如何在企业收购中制定 IT 战略，以降低 IT 风险并实现更高的收购后绩效。


Keywords: IT distance, incompatibility of IT systems, corporate acquisitions, post-acquisition operating performance, natural language processing, word embedding, Word2Vec, Bayesian model averaging




关键词：IT距离、IT系统不兼容、企业收购、收购后经营绩效、自然语言处理、词嵌入、Word2Vec、贝叶斯模型平均


## Introduction




＃＃ 介绍


While acquisitions are generally believed to create economic value (Chatterjee, 1986; Seth, 1990), they often fail to deliver the expected returns (Capron, 1999). The gap between the expected and realized value has motivated scholars to investigate value-creation mechanisms in acquisitions (Graebner et al., 2017). The extant research has examined an extensive list of factors affecting acquisition outcomes, including firm attributes such as historical performance (Chatterjee, 1992) and firm size (Moeller et al., 2004), deal characteristics such as types of deal payments (King et al., 2004), managerial self-interest (Grinstein & Hribar, 2004), and the firm’s learning capability from prior acquisitions (Zollo & Winter, 2002).




虽然人们普遍认为收购能够创造经济价值（Chatterjee，1986；Seth，1990），但它们往往无法带来预期回报（Capron，1999）。预期价值和实现价值之间的差距促使学者们研究收购中的价值创造机制（Graebner et al., 2017）。现有研究考察了影响收购结果的一系列因素，包括公司属性，如历史业绩（Chatterjee，1992）和公司规模（Moeller 等，2004）、交易特征，如交易付款类型（King 等，2004）、管理层自身利益（Grinstein 和 Hribar，2004）以及公司从先前收购中的学习能力（Zollo 和 Winter， 2002）。


While most studies have examined the effects of acquiring firms’ characteristics on post-acquisition performance (Cording et al., 2008; Heron & Lie, 2002; Malmendier & Tate, 2008; Puranam et al., 2009; Zhou & Wu, 2009), another stream of research recognizes that acquisitions essentially combine two separate entities that have presumably followed different paths in most aspects of firms’ strategy and resource profiles. This stream focuses on the role of dyadic differences or relatedness between acquiring and target firms in value creation (Bauer & Matzler, 2014; Yang et al., 2010). To capture the differences in various resources in a dyad, researchers have defined the concept of distance between firms. Specifically, prior studies have examined how interfirm distance in products (Hoberg & Phillips, 2010; Kim & Finkelstein, 2009; Wang & Zajac, 2007), knowledge (Ahuja & Katila, 2001; Makri et al., 2010; Yang et al., 2010), geography (Laursen et al., 2012), culture (Bauer & Matzler, 2014; Datta, 1991; Larsson & Finkelstein, 1999; Stahl & Voigt, 2008), and markets/clients (Rogan, 2014; Rogan & Sorenson, 2014) affect performance. We adopt this dyadic perspective and focus on the differences between the acquirer and target firms in terms of their information technology (IT) systems.




虽然大多数研究都考察了收购公司的特征对收购后绩效的影响（Cording et al., 2008; Heron & Lie, 2002; Malmendier & Tate, 2008; Puranam et al., 2009; Zhou & Wu, 2009），但另一组研究认识到收购本质上是结合了两个独立的实体，而这两个实体在公司战略和资源状况的大多数方面可能遵循不同的路径。该流重点关注收购公司和目标公司之间的二元差异或相关性在价值创造中的作用（Bauer & Matzler，2014；Yang 等，2010）。为了捕捉二元体中各种资源的差异，研究人员定义了企业之间距离的概念。具体来说，先前的研究已经考察了产品中的企业间距离（Hoberg & Phillips，2010；Kim & Finkelstein，2009；Wang & Zajac，2007）、知识（Ahuja & Katila，2001；Makri 等人，2010；Yang 等人，2010）、地理（Laursen 等人，2012）、文化（Bauer & Matzler，2014；Datta，1991；Stahl 和 Voigt，2008）以及市场/客户（Rogan，2014；Rogan 和 Sorenson，2014）影响绩效。我们采用这种二元视角，重点关注收购方和目标公司在信息技术（IT）系统方面的差异。


Specifically, we develop the concept of IT distance, which captures the differences between the IT systems of the acquirer and target firms before the acquisition. IT distance reflects the degree of incompatibility between the enterprise IT systems of the merging firms and the costs associated with integrating the disparate systems. We suggest that IT distance is an important factor in post-acquisition value creation because compatible IT systems are essential for crossboundary coordination and for facilitating seamless data exchange across firms (Barki & Pinsonneault, 2005), which are necessary for realizing the potential synergies of M&As. Higher IT distance, which reflects a greater incompatibility of IT systems, is likely to hinder synergy creation due to higher costs of system integration and increased systems complexity.




具体来说，我们提出了IT距离的概念，它反映了收购前收购方和目标公司IT系统之间的差异。 IT距离反映了合并企业的企业IT系统之间的不兼容程度以及与集成不同系统相关的成本。我们认为，IT 距离是收购后价值创造的一个重要因素，因为兼容的 IT 系统对于跨界协调和促进企业间无缝数据交换至关重要（Barki & Pinsonneault，2005），这对于实现并购的潜在协同效应是必要的。 IT距离越远，反映出IT系统的不兼容性越严重，由于系统集成成本越高、系统复杂性越高，可能会阻碍协同效应的产生。


Because the extant M&A literature has mainly focused on organizational differences pertaining to human-related factors (e.g., market, culture, knowledge), it offers little insight in terms of whether IT distance, the resolution of which mainly involves technological integration, matters in acquisitions. Also, it is unclear whether the costs associated with IT distance would be significant enough to adversely affect post-acquisition performance; therefore, whether IT distance matters for postacquisition performance remains an empirical question.




由于现有的并购文献主要关注与人相关因​​素（例如市场、文化、知识）有关的组织差异，因此对于IT距离（其解决主要涉及技术整合）是否在收购中发挥作用提供了很少的见解。此外，尚不清楚与 IT 距离相关的成本是否足以对收购后的绩效产生不利影响；因此，IT 距离对于收购后的绩效是否重要仍然是一个实证问题。


In practice, IT is often neglected during the pre-acquisition discussion and due diligence stage, as firms primarily focus on financial and strategic considerations (Akella et al., 2009; Sarrazin & West, 2011). Yet, cases abound where inadequate attention to IT integration and the resulting IT risks have led to several deficiencies in value creation and even acquisition failures (Henningsson & Kettinger, 2016). An example is Revlon’s acquisition of Elizabeth Arden in 2016: due to the premature rollout of new ERP systems, the firm was “unable to fulfill product shipments of approximately \$64m of net sales and the company incurred \$53.6 million of incremental charges to remediate the decline in customer services levels”




在实践中，IT 在收购前讨论和尽职调查阶段经常被忽视，因为公司主要关注财务和战略考虑（Akella 等人，2009 年；Sarrazin 和 West，2011 年）。然而，对 IT 集成关注不够以及由此产生的 IT 风险导致价值创造方面存在缺陷甚至收购失败的案例比比皆是（Henningsson & Kettinger，2016）。露华浓 (Revlon) 2016 年收购伊丽莎白雅顿 (Elizabeth Arden) 就是一个例子：由于新 ERP 系统过早推出，该公司“无法完成约 6400 万美元净销售额的产品发货，并产生了 5360 万美元的增量费用，以弥补客户服务水平的下降”


(Saran, 2019). Its stock price plummeted by 6.4%, and the shareholders filed a class-action lawsuit. In contrast, the Danisco-Genencor (Yetton et al., 2013) and Suncorp-Promina (Henningsson & Kettinger, 2016) acquisitions were able to avert disruptions by taking proactive measures to address the potential IT risks associated with incompatible IT systems.




（萨兰，2019）。其股价暴跌6.4%，股东提起集体诉讼。相比之下，Danisco-Genencor（Yetton 等人，2013 年）和 Suncorp-Promina（Henningsson & Kettinger，2016 年）的收购能够通过采取主动措施解决与不兼容 IT 系统相关的潜在 IT 风险来避免中断。


Although anecdotal evidence suggests that IT distance might have important performance implications in acquisitions, the IS literature has not yet addressed this important topic. Rather, the majority of the acquisition literature in IS focuses on the outcome of post-acquisition IT integration projects, such as the time and money spent on these projects and the quality of integrated systems (Henningsson et al., 2018). Another research stream has examined the outcome of acquisitions but from the perspectives of the acquirer’s IT integration capabilities (Benitez et al., 2018; Tanriverdi & Uysal, 2011) and business-IT alignment (Baker & Niederman, 2014; Mehta & Hirschheim, 2007; Wijnhoven et al., 2006). Therefore, our understanding of how ex ante IT distance affects acquisition outcomes remains limited.




尽管传闻证据表明 IT 距离可能对收购绩效产生重要影响，但 IS 文献尚未讨论这一重要主题。相反，IS 中的大多数收购文献都关注收购后 IT 集成项目的结果，例如在这些项目上花费的时间和金钱以及集成系统的质量（Henningsson 等，2018）。另一个研究流从收购方的 IT 集成能力（Benitez 等人，2018 年；Tanriverdi 和 Uysal，2011 年）和业务与 IT 一致性（Baker 和 Niederman，2014 年；Mehta 和 Hirschheim，2007 年；Wijnhoven 等人，2006 年）的角度审视了收购的结果。因此，我们对事前 IT 距离如何影响采购结果的理解仍然有限。


Our study aims to fill this gap in the literature by examining the role of IT distance—dyadic differences in merging firms’ IT systems—in post-acquisition value creation. Specifically, we theorize and empirically examine whether and how the IT distance between merging firms affects synergy creation in corporate acquisitions. To measure IT distance, we adopt a word-embedding technique (Word2Vec) to map each firm’s enterprise IT systems portfolio to a low-dimensional embedding space and calculate the distance between the IT vendors in that space. Using data on U.S. firms’ acquisition activities during 2007-2013, we find that IT distance is negatively associated with the acquirer’s post-acquisition performance. Also, the adverse effect of IT distance is stronger for acquisitions motivated by operational synergies than for those seeking non-operational synergies. This finding supports our premise that IT distance disrupts post-acquisition synergy creation, especially when the combined firm has a greater need for tight integration to create synergies. We discuss the implications of our findings with respect to how firms should devise IT strategies in corporate acquisitions to mitigate IT risks and achieve stronger post-acquisition performance.




我们的研究旨在通过研究 IT 距离（合并公司 IT 系统的二元差异）在收购后价值创造中的作用来填补文献中的这一空白。具体来说，我们从理论上和实证上检验了合并公司之间的 IT 距离是否以及如何影响企业收购中协同效应的产生。为了测量IT距离，我们采用词嵌入技术（Word2Vec）将每个公司的企业IT系统组合映射到低维嵌入空间，并计算该空间中IT供应商之间的距离。利用 2007 年至 2013 年美国公司收购活动的数据，我们发现 IT 距离与收购方收购后的绩效呈负相关。此外，IT 距离的不利影响对于由运营协同效应推动的收购比那些寻求非运营协同效应的收购更严重。这一发现支持了我们的假设，即 IT 距离会扰乱收购后协同效应的创造，特别是当合并后的公司更需要紧密集成以创造协同效应时。我们讨论了我们的研究结果对于企业应如何在企业收购中制定 IT 战略以降低 IT 风险并实现更强劲的收购后绩效的影响。


## Related Literature




## 相关文献


The management literature has extensively studied M&As. A research stream related to our study investigates how merging firms’ pre-acquisition organizational differences affect synergy creation, with a particular focus on the distance in such dimensions as firm size and earning streams (Chatterjee, 1986; Seth, 1990), business/products (Hoberg & Phillips, 2010; Kim & Finkelstein, 2009; Wang & Zajac, 2007), knowledge (Ahuja & Katila, 2001; Makri et al., 2010; Yang et al., 2010), geography (Laursen et al., 2012), culture (Bauer & Matzler, 2014; Datta, 1991; Larsson & Finkelstein, 1999; Stahl & Voigt, 2008), and markets/clients (Rogan, 2014; Rogan & Sorenson, 2014).




管理文献对并购进行了广泛的研究。与我们的研究相关的一个研究流调查了合并公司收购前的组织差异如何影响协同效应的产生，特别关注公司规模和盈利流（Chatterjee，1986；Seth，1990）、业务/产品（Hoberg & Phillips，2010；Kim & Finkelstein，2009；Wang & Zajac，2007）、知识（Ahuja & Zajac，2007）等维度上的距离。 Katila，2001；Makri 等人，2010；Yang 等人，2010）、地理（Laursen 等人，2012）、文化（Bauer 和 Matzler，2014；Datta，1991；Larsson 和 Finkelstein，1999；Stahl 和 Voigt，2008）以及市场/客户（Rogan， 2014；罗根和索伦森，2014）。


While the extant management literature provides significant insights regarding how various organizational differences affect synergy, IT distance differs from these types of distance in two important ways. First, while the distance examined in prior literature (e.g., culture, strategy, knowledge) primarily concerns human-related organizational components (Jemison & Sitkin, 1986), IT distance captures IT systems incompatibility, which is mainly technological (i.e., nonhuman-related) in nature. To resolve the other types of organizational distance, the employees of the two firms must actively engage in frequent interaction and communication, as well as in the alignment and standardization of routines and processes during the integration process (Graebner et al., 2017), incurring primarily human-related costs (career uncertainty, concerns about financial security, the lack of coworker trust, feelings of alienation, emotional conflicts, etc.). In contrast, IT distance arising from the incompatibility of IT infrastructure can be resolved by connecting backend systems without incurring many human-related costs (Harrell & Higgins, 2002).<sup>2</sup> Because the extant literature has only focused on organizational integration dimensions pertaining to human-related factors, it offers little insight into whether IT infrastructure incompatibility, the resolution of which mainly involves technological integration, matters in acquisitions.




虽然现有的管理文献提供了关于各种组织差异如何影响协同效应的重要见解，但 IT 距离在两个重要方面与这些类型的距离不同。首先，虽然先前文献（例如文化、战略、知识）中研究的距离主要涉及与人类相关的组织组件（Jemison & Sitkin，1986），但 IT 距离捕获了 IT 系统的不兼容性，这主要是技术性的（即与人类无关的）。为了解决其他类型的组织距离，两家公司的员工必须积极参与频繁的互动和沟通，以及在整合过程中对常规和流程进行协调和标准化（Graebner等，2017），这主要产生与人相关的成本（职业不确定性、对财务安全的担忧、同事缺乏信任、疏远感、情感冲突等）。相比之下，由于IT基础设施不兼容而产生的IT距离可以通过连接后端系统来解决，而不会产生许多与人相关的成本（Harrell & Higgins, 2002）。<sup>2</sup>由于现有文献仅关注与人相关因​​素相关的组织整合维度，因此很少深入探讨IT基础设施不兼容的解决是否主要涉及技术整合，是否涉及收购问题。


Second, the mechanisms underlying the IT distanceperformance relationship are different from other types of distance. Extant research theoretically argues and empirically demonstrates that the distance in such dimensions as the market, knowledge, and culture can affect acquisition outcomes through two different mechanisms (Hoberg & Phillips, 2010; Makri et al., 2010): complementarity, which leads to a positive impact on performance (Makri et al., 2010; Zollo & Singh, 2004); and incompatibility, which might negatively affect the performance (due to clashes/conflicts) (Bauer & Matzler, 2014; Stahl & Voigt, 2008). For instance, the cultural distance between the merging firms can cause cultural clashes within the merged organization. Yet, at the same time, such cultural distance can also provide opportunities for learning from diverse cultural perspectives, thereby positively influencing organizational performance. Similarly, differences in knowledge may initially hinder communication and coordination between members of the merging firms due to differences in their knowledge bases and knowledge-generating processes. However, knowledge diversity can also provide learning opportunities, thereby contributing to creativity and innovativeness. Further, while differences in the markets that each firm serves may create challenges in setting up priorities, as each market serves different customer segments, such market differences can lead to complementarity by creating cross-selling opportunities. As such, the coexistence of the two mechanisms (i.e., complementarity and incompatibility) generates ambiguity in the overall performance impact of these types of organizational distance, as reflected in the mixed empirical evidence (Graebner et al., 2017).




其次，IT 距离绩效关系的基础机制不同于其他类型的距离。现有研究从理论上论证并从实证上证明，市场、知识和文化等维度上的距离可以通过两种不同的机制影响收购结果（Hoberg & Phillips, 2010；Makri et al., 2010）： 互补性，这会对绩效产生积极影响（Makri et al., 2010；Zollo & Singh, 2004）；和不兼容性，这可能会对性能产生负面影响（由于冲突/冲突）（Bauer & Matzler，2014；Stahl & Voigt，2008）。例如，合并公司之间的文化距离可能会导致合并组织内部的文化冲突。但与此同时，这种文化距离也可以提供从不同文化角度学习的机会，从而对组织绩效产生积极影响。同样，由于知识基础和知识生成过程的差异，知识差异最初可能会阻碍合并公司成员之间的沟通和协调。然而，知识多样性也可以提供学习机会，从而有助于创造力和创新性。此外，虽然每个公司服务的市场差异可能会给确定优先级带来挑战，因为每个市场服务于不同的客户群，但这种市场差异可以通过创造交叉销售机会来实现互补。因此，两种机制的共存（即互补性和不相容性）会导致这些类型的组织距离对整体绩效的影响变得模糊，正如混合的经验证据所反映的那样（Graebner et al., 2017）。


In contrast, IT distance, which captures systems incompatibility, operates through only one mechanism (incompatibility) and can therefore only have a negative impact on post-acquisition performance; the positive mechanism (complementarity) does not operate in the context of IT distance. Nevertheless, it is unclear whether the cost of IT distance would be significant enough to adversely affect post-acquisition performance. If the cost of integration were small due to the commoditization of IT systems, the total cost and its negative impact on performance might be negligible vis-à-vis other costs. However, if the costs involved in integrating disparate IT systems (to resolve the incompatibility) were substantially large, it would significantly influence post-acquisition performance. Given that whether IT distance matters for post-acquisition performance is an unexplored empirical question, our study develops a novel, fine-grained conceptualization and operationalization of IT distance and empirically examines its impact on post-acquisition performance.




相比之下，捕获系统不兼容性的 IT 距离仅通过一种机制（不兼容性）运作，因此只能对收购后的绩效产生负面影响；积极机制（互补性）在信息技术距离的背景下不起作用。然而，尚不清楚 IT 距离的成本是否足以对收购后的绩效产生不利影响。如果由于 IT 系统的商品化而导致集成成本很小，那么与其他成本相比，总成本及其对性能的负面影响可能可以忽略不计。然而，如果整合不同IT系统（以解决不兼容问题）所涉及的成本非常大，则会显着影响收购后的绩效。鉴于 IT 距离是否对收购后绩效重要是一个尚未探索的实证问题，我们的研究开发了一种新颖的、细粒度的 IT 距离概念化和可操作化，并实证检验了其对收购后绩效的影响。


There has been limited research in IS on the role of IT in postacquisition performance, but it has only examined the postacquisition IT integration process. Most studies in this research stream have focused on the IT integration process and project outcomes rather than value creation; moreover, the outcome variables have mostly been IT integration objectives, such as integration project timelines, budget overruns, etc. (Henningsson et al., 2018; Henningsson & Kettinger, 2016; Jain & Ramesh, 2015; Kovela & Skok, 2012). Few studies (Tanriverdi & Uysal, 2011) have investigated the broader performance implications of IT integration. For example, Tanriverdi and Uysal (2011) employed a survey methodology to measure cross-business IT integration capability and found that acquirers with high levels of IT integration capability achieve higher performance. Unlike these prior studies, which have focused on how firms can better achieve post-acquisition IT integration, we focus on the ex ante IT systems incompatibility between firms (as measured by IT distance) and examine whether and how ex ante IT distance affects postacquisition performance ceteris paribus. Given that capability building takes time and is costly, our study extends and complements prior studies by shedding light on when firms need strong IT integration capabilities (i.e., when two merging firms have high IT distance and a strong need for integration).




IS 领域关于 IT 在收购后绩效中的作用的研究有限，但仅研究了收购后 IT 整合过程。该研究领域的大多数研究都侧重于 IT 集成过程和项目成果，而不是价值创造；此外，结果变量主要是 IT 集成目标，例如集成项目时间表、预算超支等（Henningsson 等人，2018 年；Henningsson & Kettinger，2016 年；Jain & Ramesh，2015 年；Kovela & Skok，2012 年）。很少有研究（Tanriverdi & Uysal，2011）调查了 IT 集成的更广泛的性能影响。例如，Tanriverdi和Uysal（2011）采用调查方法来衡量跨业务IT集成能力，发现具有高水平IT集成能力的收购方可以获得更高的绩效。与这些先前的研究重点关注企业如何更好地实现收购后 IT 整合不同，我们关注的是企业之间事前 IT 系统的不兼容性（通过 IT 距离衡量），并研究事前 IT 距离是否以及如何影响收购后的绩效（其他条件不变）。鉴于能力建设需要时间且成本高昂，我们的研究扩展并补充了先前的研究，揭示了企业何时需要强大的 IT 集成能力（即，当两家合并企业的 IT 距离较远且集成需求强烈时）。


To summarize, our cross-disciplinary literature review suggests that despite IT’s potential impacts in M&As and calls for research on the role of IT in the value-creation process in acquisitions, we still have a limited understanding of whether, how, and why differences in IT systems impact post-acquisition performance. This study proposes IT distance as a novel construct and empirically demonstrates its role in synergy creation in acquisitions; it thereby contributes to the broader M&A literature by adding IT as another critical aspect of organizational differences that determine post-acquisition performance.




总而言之，我们的跨学科文献综述表明，尽管 IT 在并购中具有潜在影响，并呼吁研究 IT 在收购价值创造过程中的作用，但我们对 IT 系统差异是否、如何以及为何影响收购后绩效的了解仍然有限。本研究提出 IT 距离作为一种新颖的结构，并实证证明了其在收购中创造协同效应中的作用；因此，它通过将 IT 添加为决定收购后绩效的组织差异的另一个关键方面，为更广泛的并购文献做出了贡献。


## Theoretical Background




## 理论背景


## Need for Integrated IT Systems and IT Distance as a Hurdle




## 集成 IT 系统的需求和 IT 距离成为障碍


Integrated IT systems facilitate the exchange of data, information, knowledge, and resources, both within and across organizational boundaries. At the core, they ensure data integrity, a common network, and security protocols for system-level communication, enabling IT applications to interoperate and exchange data in real time (Benitez et al., 2018; Vernadat, 2007). Such characteristics of integrated systems can help firms better sense internal/external changes, coordinate workflows and operations, and reconfigure resource allocation to achieve global optimization (Rai et al., 2012, 2006). Furthermore, enhanced sensing and reconfiguration capabilities may in turn enhance the structural flexibility of decision-making (Benitez et al., 2018). Because information is available at any point in the organizational grid, decision-making can be decentralized to local managers (Dean et al., 1992) and aided by cross-functional teams dynamically formed to tackle issues requiring diverse expertise, which is likely distributed across departments (Majchrzak et al., 2000). Hence, integrated IT systems in a merged organization increase the firm’s ability to materialize synergies.




集成的 IT 系统促进组织内部和跨组织边界的数据、信息、知识和资源的交换。它们的核心是确保数据完整性、通用网络和系统级通信的安全协议，使 IT 应用程序能够实时互操作和交换数据（Benitez 等人，2018 年；Vernadat，2007 年）。集成系统的这些特性可以帮助企业更好地感知内部/外部变化，协调工作流程和运营，重新配置资源配置以实现全局优化（Rai等，2012，2006）。此外，增强的传感和重新配置能力可能反过来增强决策的结构灵活性（Benitez et al., 2018）。由于信息在组织网格中的任何点都可用，因此决策可以下放给当地管理者（Dean 等，1992），并由动态组建的跨职能团队协助，以解决需要不同专业知识的问题，这些专业知识可能分布在各个部门（Majchrzak 等，2000）。因此，合并后的组织中的集成 IT 系统提高了公司实现协同效应的能力。


Merging firms, however, must make significant integration efforts to obtain the benefits of integrated IT systems because firms’ IT systems are inherently idiosyncratic and incompatible for numerous reasons, such as the lack of industry standards, use of proprietary technologies to lock in clients, and the lack of holistic and systematic approaches to




然而，合并后的企业必须做出巨大的整合努力才能获得集成IT系统的好处，因为企业的IT系统本质上是特殊的且不兼容，原因有很多，例如缺乏行业标准、使用专有技术来锁定客户以及缺乏整体和系统的方法来整合客户。


IT development (Akella et al., 2009; Chellappa et al., 2010; Chellappa & Saraf, 2010; Schoenherr et al., 2010; Zhu & Zhou, 2011). The greater the incompatibility of merging firms’ IT systems is, the greater the efforts and costs required to reach the desired level of IT systems integration. To capture the degree of the difficulty of systems integration presented by IT incompatibility, we conceptualize “IT distance” as the difference between the enterprise IT systems of two firms involved in an acquisition, which reflects the systems incompatibility and resulting costs of system integration. Our conceptualization of IT distance is similar to that of other types of distance that capture (1) how far apart or different certain objects or points are, as well as (2) the costs or efforts required to connect the two separate concepts. For instance, physical distance implies the transportation costs incurred in covering the distance between two locations, and psychic distance is defined in terms of the barriers to learning and understanding (Nordstrom & Vahlne, 1994). Essentially, IT distance captures the costs associated with resolving the barriers in exchanging information between two enterprise IT systems that differ in terms of technology infrastructure and system architecture, conceptual data models, user interfaces, and specific functionalities, as well as the modeling of business processes. Enterprise systems comprising homogenous and compatible components can be characterized as being low in IT distance. In contrast, systems with a large number of disparate subsystems are high in IT distance, thus requiring greater efforts to bridge the distance.




IT 开发（Akella 等人，2009；Chellappa 等人，2010；Chellappa 和 Saraf，2010；Schoenherr 等人，2010；Zhu 和 Zhou，2011）。合并企业的IT系统不兼容程度越高，达到预期IT系统集成水平所需的努力和成本就越大。为了衡量IT不兼容带来的系统集成的难度程度，我们将“IT距离”概念定义为参与收购的两家企业的企业IT系统之间的差异，它反映了系统不兼容以及由此产生的系统集成成本。我们对 IT 距离的概念化与其他类型距离的概念化类似，后者捕获 (1) 某些对象或点相距多远或不同，以及 (2) 连接两个独立概念所需的成本或工作。例如，物理距离意味着两个地点之间的距离所产生的运输成本，而心理距离则根据学习和理解的障碍来定义（Nordstrom & Vahlne，1994）。从本质上讲，IT 距离捕获了与解决两个企业 IT 系统之间交换信息的障碍相关的成本，这两个企业 IT 系统在技术基础设施和系统架构、概念数据模型、用户界面和特定功能以及业务流程建模方面存在差异。由同质且兼容的组件组成的企业系统的特点是 IT 距离较低。相比之下，具有大量不同子系统的系统的 IT 距离较高，因此需要付出更大的努力来弥合距离。


## IT Distance and the Long-Term Costs of Systems Complexity




## IT 距离和系统复杂性的长期成本


Besides these short-term integration costs, merging firms with high IT distance can also incur long-term costs due to increased systems complexity from systems integration. In general, systems that “consist of diverse rule-following entities whose behaviors are interdependent” are considered complex (Page, 2010, p. 17). Similarly, the complexity of enterprise systems is characterized by the number and variety of components and their interactions (Schneberger & McLean, 2003). These elements of complexity are shared among the conceptualization of different types of complexity, such as task complexity (Campbell, 1988).




除了这些短期整合成本之外，由于系统集成增加了系统复杂性，IT 距离较远的合并公司也会产生长期成本。一般来说，“由行为相互依赖的不同规则遵循实体组成”的系统被认为是复杂的（Page，2010，第 17 页）。同样，企业系统的复杂性以组件的数量和种类及其交互为特征（Schneberger & McLean，2003）。这些复杂性元素在不同类型复杂性的概念化之间共享，例如任务复杂性（Campbell，1988）。


From an information processing perspective, complex systems comprising a large number of distinct components could overstretch the cognitive capacity of developers and managers (Banker et al., 1998; Darcy et al., 2005; Espinosa et al., 2007; Schneberger & McLean, 2003). As the scope and variety of components grow, managers and developers must acquire and process a greater amount of information than they would with a homogenous system. They need to understand how these components work and how they must be configured and connected to work together. Furthermore, when changing a module connected to others, they must anticipate how these changes will cascade into other modules.




从信息处理的角度来看，包含大量不同组件的复杂系统可能会超出开发人员和管理者的认知能力（Banker et al., 1998; Darcy et al., 2005; Espinosa et al., 2007; Schneberger & McLean, 2003）。随着组件范围和种类的增加，管理人员和开发人员必须获取和处理比同质系统更多的信息。他们需要了解这些组件如何工作以及必须如何配置和连接它们才能协同工作。此外，当更改连接到其他模块的模块时，他们必须预测这些更改将如何级联到其他模块。


From a system architecture point of view, the lack of standardization among systems components indicates the absence of “the agreement on common specifications for information exchange formats, data repositories, and processing tasks at the interfaces between subsystems” (Gosain et al., 2004, p. 14). Without standards, these subsystems’ interfaces need customization, which increases systems interdependency and thus complexity. There are some integration technologies, such as enterprise application integration (EAI) and middleware, but these are not immune to the complexity issue. For instance, incompatible components, which cannot communicate with each other, would require an integration layer<sup>3</sup> to translate between distinct protocols. The integration layer is designed to reduce complexity by separating the technical translation for interprotocol communication from implementing business rules and operations. However, as opposed to its purpose, this layer could ironically increase complexity in several ways. Introducing another layer into the system architecture means adding additional interfaces; these involve more lines of code to be executed and thus require greater computing power and network resources for execution, which results in an execution penalty and performance degradation (Zhang & Jacobsen, 2003). Moreover, attempts to overcome these performance issues often result in overly complicated configurations for the integration layer, further adding to systems complexity (Vinoski, 2002). It is also known that the integration layer is often built on proprietary technologies, thereby making systems specialized, interdependent, and complex (Vinoski, 2002). Because IT distance captures the differences between the IT systems of the acquirer and target firms, systems with higher IT distance are likely to require greater efforts to integrate, which would lead to higher immediate costs of system integration and long-term costs due to increased systems complexity.




从系统架构的角度来看，系统组件之间缺乏标准化表明缺乏“关于子系统之间接口的信息交换格式、数据存储库和处理任务的通用规范的协议”（Gosain et al., 2004, p. 14）。如果没有标准，这些子系统的接口就需要定制，这增加了系统的相互依赖性，从而增加了复杂性。有一些集成技术，例如企业应用程序集成（EAI）和中间件，但这些技术都无法避免复杂性问题。例如，不兼容的组件无法相互通信，因此需要集成层<sup>3</sup>来在不同的协议之间进行转换。集成层旨在通过将协议间通信的技术转换与实现业务规则和操作分开来降低复杂性。然而，与它的目的相反，这一层可能会以多种方式增加复杂性。在系统架构中引入另一层意味着添加额外的接口；这些涉及要执行的代码行更多，因此需要更大的计算能力和网络资源来执行，这会导致执行损失和性能下降（Zhang & Jacobsen，2003）。此外，克服这些性能问题的尝试通常会导致集成层的配置过于复杂，从而进一步增加系统的复杂性（Vinoski，2002）。众所周知，集成层通常建立在专有技术之上，从而使系统变得专业化、相互依赖和复杂（Vinoski，2002）。由于IT距离体现了收购方和目标公司IT系统之间的差异，IT距离较高的系统可能需要更大的努力来集成，这将导致系统集成的直接成本更高，并且由于系统复杂性增加而导致长期成本更高。


## Hypotheses Development




## 假设发展


## IT Distance and Post-Acquisition Performance




## IT 距离和收购后绩效


As discussed above, the systems complexity arising from IT distance can impede synergy creation in acquisitions and increase both short- and long-term costs. Here, we elaborate on the kinds of costs that firms incur from post-acquisition system complexity caused by ex ante IT distance. First, IT distanceinduced systems complexity can increase the cost associated with software development and maintenance (Banker et al., 1998; Darcy et al., 2005; Schneberger & McLean, 2003). The variety of subsystems increases the number of information cues required for managers and developers to comprehend the systems and validate the modifications made to them. The resulting cognitive overload makes it more difficult to correct faults, improve performance, or adapt to changes in the environment, leading to increases in the overall maintenance costs (Banker et al., 1998). In fact, Schneberger and McLean (2003) show that from the dimensions of systems complexity, the variety of components (distinct, incompatible subsystems) has been found to have a greater effect than the number of components; that is, it is easier to deal with a large number of components with similar architectures and configurations than a few disparate subsystems from different vendors or with different configurations. Thus, IT distance, which reflects the degree of incompatibility among components, could be a major cost driver in the post-acquisition integration and maintenance of IT systems.




如上所述，IT 距离造成的系统复杂性可能会阻碍收购中协同效应的产生，并增加短期和长期成本。在这里，我们详细阐述了企业因事前 IT 距离而导致收购后系统复杂性所产生的各种成本。首先，IT 距离引起的系统复杂性会增加与软件开发和维护相关的成本（Banker 等人，1998 年；Darcy 等人，2005 年；Schneberger 和 McLean，2003 年）。子系统的多样性增加了管理人员和开发人员理解系统并验证对其所做修改所需的信息线索的数量。由此产生的认知超载使得纠正错误、提高性能或适应环境变化变得更加困难，从而导致总体维护成本增加（Banker et al., 1998）。事实上，Schneberger 和 McLean (2003) 表明，从系统复杂性的维度来看，组件的多样性（不同的、不兼容的子系统）被发现比组件的数量具有更大的影响；也就是说，处理大量具有相似架构和配置的组件比处理来自不同供应商或具有不同配置的几个不同子系统更容易。因此，反映组件之间不兼容程度的IT距离可能是IT系统收购后集成和维护的主要成本驱动因素。


Second, IT distance could disrupt existing business operations, as it may increase the chance of critical incidents, defined as “unexpected, nonroutine, and situational incidents that require contextual responses not readily available through standardized operating procedures” (Langer et al., 2014, p. 365). Coping with complexity due to IT distance requires great information-processing capacity for firms (Pich et al., 2002; Xia & Lee, 2005). However, the lack of familiarity with each other’s IT systems due to IT distance may constrain firms’ cognitive capacity. Langer et al. (2014) demonstrate that high complexity, coupled with low familiarity, tends to create high information gaps, which can lead to critical incidents. Subsequently, critical incidents can hinder development progress by forcing re-work on partially done software to which any changes have cross-impacts on highly interdependent software modules (Espinosa et al., 2007). The consequences will manifest as a form of “delay and disruption”—budget and schedule overruns, compromised performance, and missed opportunities (Pich et al., 2002). Prior studies have suggested that the speed of integration increases the chance of synergy creation by reducing uncertainty among employees, customers, and partners, and also by minimizing the time spent in a suboptimal condition, ultimately facilitating faster exploitation of synergies (Angwin, 2004; Bauer & Matzler, 2014; Homburg & Bucerius, 2006). Delays in the integration process, on the other hand, will lead to suboptimal decision-making, increased costs from operating in a suboptimal condition, and the disruption of expected value from potential synergies.




其次，IT 距离可能会扰乱现有的业务运营，因为它可能会增加发生关键事件的可能性，关键事件被定义为“需要通过标准化操作程序无法轻松获得的上下文响应的意外、非常规和情景事件”（Langer 等，2014 年，第 365 页）。应对因 IT 距离而导致的复杂性需要企业具备强大的信息处理能力（Pich 等，2002；Xia 和 Lee，2005）。然而，由于IT距离而对彼此的IT系统缺乏熟悉可能会限制企业的认知能力。兰格等人。 (2014) 表明，高复杂性加上低熟悉度往往会造成高信息差距，从而导致严重事件。随后，关键事件可能会迫使对部分完成的软件进行返工，从而阻碍开发进度，任何更改都会对高度相互依赖的软件模块产生交叉影响（Espinosa 等，2007）。其后果将表现为某种形式的“延误和中断”——预算和进度超支、绩效受损以及错失机会（Pich et al., 2002）。先前的研究表明，整合的速度通过减少员工、客户和合作伙伴之间的不确定性，以及通过最大限度地减少在次优条件下花费的时间来增加产生协同效应的机会，最终促进更快地利用协同效应（Angwin，2004；Bauer＆Matzler，2014；Homburg＆Bucerius，2006）。另一方面，整合过程的延误将导致决策不理想、在不理想的条件下运营导致成本增加以及潜在协同效应的预期价值受到破坏。


Among other costs, the most serious involves unplanned disruptions of existing business operations (Datta, 1991; Zollo & Singh, 2004). Failure to provision essential IT functions to support operations when needed has serious strategic and financial implications (Tanriverdi & Uysal, 2011). For example, in HP’s acquisition of Compaq, massive backlogs due to data integrity issues caused several weeks of delays and poor IT integration, which cost the company \$400 million (Thibodeau & Tennant, 2004).




在其他成本中，最严重的是现有业务运营的意外中断（Datta，1991；Zollo & Singh，2004）。如果无法在需要时提供必要的 IT 功能来支持运营，则会产生严重的战略和财务影响（Tanriverdi & Uysal，2011）。例如，在惠普收购康柏的过程中，由于数据完整性问题导致大量积压，导致了数周的延误和糟糕的 IT 集成，导致公司损失了 4 亿美元（Thibodeau & Tennant，2004）。


Lastly, IT distance-induced systems complexity can render integrated systems highly interdependent, and can thus make them difficult to reconfigure, limiting their strategic value. As noted earlier, interdependence among subsystems rises with IT distance due to the need for customization. Although customization allows incompatible components to be interoperable, resulting increases in interdependence make them “inflexible”—difficult to change, disentangle, and recombine into new configurations. Systems that are highly interdependent and complex may not be amenable to the scope, scale, or pace of the changes required for redeploying resources to create synergies. As a result, the intended synergy creation may be delayed or undermined due to the lack of reconfigurability and scalability of IT functions. This view is consistent with prior work positing that IT compatibility is a critical determinant of IT flexibility, which can facilitate synergy creation in interfirm collaboration (Gosain et al., 2004; Tafti et al., 2013) and M&As (Benitez et al., 2018; Tanriverdi & Uysal, 2011).




最后，IT 距离引起的系统复杂性会使集成系统高度相互依赖，从而使它们难以重新配置，从而限制了它们的战略价值。如前所述，由于定制的需要，子系统之间的相互依赖性随着 IT 距离的增加而增加。尽管定制允许不兼容的组件进行互操作，但由此导致的相互依赖性的增加使它们变得“不灵活”——难以更改、分解和重新组合成新的配置。高度相互依赖和复杂的系统可能无法适应重新部署资源以产生协同效应所需的变革范围、规模或速度。因此，由于 IT 功能缺乏可重新配置性和可扩展性，预期的协同效应可能会被延迟或破坏。这一观点与之前的研究一致，即 IT 兼容性是 IT 灵活性的关键决定因素，这可以促进公司间协作（Gosain 等人，2004 年；Tafti 等人，2013 年）和并购（Benitez 等人，2018 年；Tanriverdi 和 Uysal，2011 年）中协同效应的产生。


Based on the discussion so far regarding the different types of post-acquisition costs arising from pre-acquisition IT distance, we posit:




根据迄今为止关于因收购前 IT 距离而产生的不同类型的收购后成本的讨论，我们假设：


H1: Pre-acquisition IT distance between an acquirer and a target firm has a negative association with the acquirer’s post-acquisition performance.




H1：收购前收购方与目标公司之间的 IT 距离与收购方收购后绩效呈负相关。


## The Role of Acquisition Motivation in the IT Distance-Performance Relationship




## 收购动机在 IT 距离与绩效关系中的作用


As described above, a key factor affecting the complexity of an integrated system and the ensuing costs is the interdependence among systems components—the extent to which those components interact with, and thus depend on one another (Banker et al., 1998; Page, 2010; Schneberger & McLean, 2003). When merging firms’ systems require frequent and intensive interactions with each other (i.e., high interdependence), the integration would need complex configuration to support the interaction bandwidth, thereby increasing the overall systems complexity for the merged organization. In contrast, when the systems of merging firms require minimal interactions (i.e., low interdependence), and thus a low level of integration, the systems complexity and associated costs will be lower at the same level of IT distance. Therefore, the adverse effect of IT distance on postacquisition performance will vary based on the level of systems interdependence in an acquisition.




如上所述，影响集成系统复杂性和随之而来的成本的一个关键因素是系统组件之间的相互依赖性，即这些组件之间相互作用并因此相互依赖的程度（Banker et al., 1998; Page, 2010; Schneberger & McLean, 2003）。当合并公司的系统需要彼此频繁且密集的交互（即高度相互依赖）时，集成将需要复杂的配置来支持交互带宽，从而增加合并后组织的整体系统复杂性。相比之下，当合并公司的系统需要最少的交互（即低相互依赖性）并因此需要低水平的集成时，在相同的IT距离水平下，系统复杂性和相关成本将会较低。因此，IT 距离对收购后绩效的不利影响将根据收购中系统相互依赖的程度而有所不同。


A key determinant of systems interdependence involves the extent to which merging firms’ operations and resources are interdependent, which critically hinges on the kind of synergy that firms seek in an acquisition (i.e., acquisition motivation) (Henningsson et al., 2018). One widely adopted way to classify acquisitions is according to the types of synergies that firms aim to achieve (Chatterjee, 1986; Seth, 1990). In particular, acquisitions are often classified into those undertaken to achieve operational synergy and those striving to attain non-operational (financial) synergy. Operational synergies refer to efficiency gains from economies of scale/scope and complementarity (e.g., maximizing the utilization of or minimizing the duplication of sharable input factors in production). In contrast, non-operational synergies arise from “risk pooling” based on financial diversification and include the reduced cost of capital from asymmetric capital access, the reduced chance of bankruptcy from an imperfect correlation between firms’ earning streams, increased debt capacity, and improved tax benefits.




系统相互依赖的一个关键决定因素涉及合并企业的运营和资源相互依赖的程度，这在很大程度上取决于企业在收购中寻求的协同效应（即收购动机）（Henningsson等人，2018）。一种广泛采用的对收购进行分类的方法是根据公司旨在实现的协同效应的类型（Chatterjee，1986；Seth，1990）。特别是，收购通常分为为实现运营协同效应而进行的收购和努力实现非运营（财务）协同效应的收购。运营协同效应是指规模经济/范围经济和互补性带来的效率收益（例如，最大限度地利用生产中可共享的投入要素或最大限度地减少重复生产）。相比之下，非经营性协同效应则源于基于金融多元化的“风险分担”，包括因资本准入不对称而降低的资本成本、因企业盈利流之间不完全相关性而导致的破产机会降低、债务能力的增强以及税收优惠的改善。


Acquisitions seeking operational synergies require firms to implement a high level of organizational integration, which involves extensive changes to business processes (e.g., asset divesture, cross-selling, cross-advertising, and knowledge sharing), thereby rendering their operation and resources highly interdependent (Seth, 1990). In contrast, nonoperational synergies (e.g., risk pooling from financial diversification) require minimal integration and process changes, thereby resulting in low levels of operational and resource interdependence (Seth, 1990).




寻求运营协同效应的收购要求企业实施高水平的组织整合，这涉及业务流程的广泛变革（例如资产剥离、交叉销售、交叉广告和知识共享），从而使其运营和资源高度相互依赖（Seth，1990）。相比之下，非运营协同效应（例如，金融多元化带来的风险分担）需要最少的整合和流程变化，从而导致运营和资源相互依赖程度较低（Seth，1990）。


The difference in the levels of organizational interdependence, which depends on the acquisition synergy, translates into the difference in the systems interdependence and resulting systems complexity. Acquisitions seeking non-operational synergies require rather simple and infrequent exchanges of information and knowledge across merging firms (Henningsson & Kettinger, 2016). Implementing such a lowinterdependence linkage is characterized by relatively few components to connect and minimal interaction bandwidth (asynchronous, periodic data exchange). Also, the instructions and tasks for developing such software tend to be simple and well-defined, and thus can be managed by standard operating procedures (Langer et al., 2014). Therefore, systems complexity and the associated costs (mentioned in the previous section) will be relatively low.




组织相互依赖程度的差异取决于收购协同作用，转化为系统相互依赖程度的差异以及由此产生的系统复杂性。寻求非运营协同效应的收购需要合并公司之间相当简单且不频繁的信息和知识交换（Henningsson＆Kettinger，2016）。实现这种低相互依赖性链接的特点是要连接的组件相对较少，并且交互带宽最小（异步、定期数据交换）。此外，开发此类软件的指令和任务往往简单且定义明确，因此可以通过标准操作程序进行管理（Langer 等，2014）。因此，系统复杂性和相关成本（在上一节中提到）将相对较低。


In contrast, firms in acquisitions seeking operational synergies need to create a broad, high-bandwidth organizational linkage that can support high levels of organizational interdependence. To achieve this, IT systems need to be tightly integrated to support the frequent and intensive interaction and communication among a large number of components. Moreover, the resulting increases in systems complexity renders the integrated system less flexible, making it more difficult to reconfigure the system to adapt to environmental changes, which can have long-term consequences (Benitez et al., 2018). As such, acquisitions aiming to achieve operational synergy have a stronger need to create highly interdependent linkages. This will inevitably increase the systems complexity and associated costs, thereby undermining the post-acquisition performance to a greater extent, compared to acquisitions seeking non-operational synergy. Therefore, we posit:




相比之下，寻求运营协同效应的收购公司需要建立广泛的、高带宽的组织联系，以支持高水平的组织相互依赖。为此，IT系统需要紧密集成，以支持大量组件之间频繁、密集的交互和通信。此外，由此带来的系统复杂性的增加使得集成系统的灵活性降低，使得重新配置系统以适应环境变化变得更加困难，这可能会产生长期后果（Benitez et al., 2018）。因此，旨在实现运营协同效应的收购更需要建立高度相互依赖的联系。与寻求非运营协同的收购相比，这将不可避免地增加系统复杂性和相关成本，从而更大程度地损害收购后的业绩。因此，我们假设：


H2: The negative association between IT distance and the acquirer’s post-acquisition performance will be stronger for acquisitions motivated by operational synergy, compared to acquisitions motivated by non-operational synergy.




H2：与非运营协同驱动的收购相比，运营协同驱动的收购中，IT 距离与收购方收购后业绩之间的负相关关系更强。


## Method




＃＃ 方法


## Sample Selection




## 样本选择


We collected data on corporate acquisition transactions from the Securities Data Company (SDC) Platinum database. Our sample includes U.S. domestic acquisition deals undertaken by Fortune 1000 firms during the period 2007-2013. We considered acquisitions whose deal size was larger than 1 million USD, and in which an acquiring firm had owned less than 50% of the target firm’s shares before the announcement but 100% after the transaction was completed (Moeller et al., 2004). The sample is further limited by the availability of accounting fundamentals (COMPUSTAT), financial information (CRSP), and IT system specifications (CI Technology Database; CITDB hereafter), which were used to generate the dependent, independent, and control variables. Lastly, we excluded the acquisitions by acquirers who went through more than one acquisition per year, as they could confound the realized returns. This resulted in a total of 2,257 deals, out of which we kept only those deals where CITDB reports the vendors of the IT modules for both acquirer and target firms, resulting in 215 deals. Matching the abnormal operating performance with COMPUSTAT reduced the sample size by 21, and matching the market cap from CRSP further reduced the sample by 9, which resulted in 185 acquisition deals. The final sample accounts for 8.2% of the total acquisition deals that took place during the sample period.<sup>4</sup>




我们从证券数据公司 (SDC) 白金数据库收集了有关企业收购交易的数据。我们的样本包括财富 1000 强企业在 2007 年至 2013 年期间进行的美国国内收购交易。我们考虑了交易规模超过 100 万美元的收购，其中收购公司在公告之前拥有目标公司股份的比例低于 50%，但在交易完成后则为 100%（Moeller 等，2004）。样本进一步受到会计基础知识 (COMPUSTAT)、财务信息 (CRSP) 和 IT 系统规范（CI 技术数据库；以下简称 CITDB）的可用性的限制，这些信息用于生成因变量、自变量和控制变量。最后，我们排除了每年进行多次收购的收购方的收购，因为它们可能会混淆已实现的回报。这总共产生了 2,257 笔交易，其中我们只保留了 CITDB 报告收购方和目标公司 IT 模块供应商的交易，最终产生了 215 笔交易。将异常经营业绩与COMPUSTAT进行匹配，样本量减少了21个，与CRSP的市值进行匹配，进一步减少了9个样本，最终产生了185起收购交易。最终样本占样本期内发生的收购交易总数的 8.2%。<sup>4</sup>


## Identification




＃＃ 鉴别


To estimate the causal effect of a treatment (or event) on an outcome, one must ensure that conditional on the observables, there are no confounders that impact both the outcome and treatment of interest (i.e., conditional independence). To this end, we employed the event-study framework, one of the most applied methods in the M&A literature, where the effect of the event (i.e., abnormal operating performance of a corporate acquisition) is calculated by comparing an acquirer’s realized and expected outcomes. The expected outcome serves as a counterfactual—the acquirer’s performance if it had not gone through the acquisition.




为了估计治疗（或事件）对结果的因果影响，必须确保在可观察的条件下，不存在影响结果和感兴趣的治疗的混杂因素（即条件独立性）。为此，我们采用了事件研究框架，这是并购文献中最常用的方法之一，其中事件的影响（即企业收购的异常经营绩效）是通过比较收购方的已实现结果和预期结果来计算的。预期结果是反事实——收购方在没有进行收购的情况下的表现。


This approach has several merits. First, matching on the firm characteristics that might affect both the acquisition decision and performance minimizes concerns regarding observable confounders. Second, differencing the pre- and post-event outcomes can eliminate any unobservable confounders that are constant over time. Third, firms are matched on historical performance, indicating that the companies used for measuring the expected performance share parallel outcome trends prior to the acquisition. This matching is important because balancing over lagged outcomes addresses the issue with time-varying unobservables, as it resembles the interactive fixed-effect model that allows factor loadings to vary over time (Gobillon & Magnac, 2016). This approach— matching on the pre-event outcome—is shared among other econometric methods, such as the DID framework (Dehejia & Wahba, 1999), interactive fixed-effect model (Gobillon & Magnac, 2016), and synthetic control method (Abadie, 2021), to minimize the effects of potential time-varying unobservable confounders.




这种方法有几个优点。首先，匹配可能影响收购决策和业绩的公司特征可以最大限度地减少对可观察到的混杂因素的担忧。其次，区分事件前和事件后的结果可以消除任何随着时间的推移而持续存在的不可观察的混杂因素。第三，公司的历史业绩是匹配的，这表明用于衡量预期业绩的公司在收购之前共享平行的结果趋势。这种匹配很重要，因为平衡滞后结果可以解决随时间变化的不可观测值的问题，因为它类似于允许因子负载随时间变化的交互式固定效应模型（Gobillon & Magnac，2016）。这种与事件前结果相匹配的方法在其他计量经济学方法中共享，例如 DID 框架（Dehejia & Wahba，1999）、交互式固定效应模型（Gobillon & Magnac，2016）和综合控制方法（Abadie，2021），以最大限度地减少潜在的时变不可观察混杂因素的影响。


## Dependent Variable: Abnormal Post-Acquisition Operating Performance




## 因变量：收购后经营业绩异常


Following the literature (Barber & Lyon, 1996), abnormal operating performance is defined as the difference between an acquirer’s realized performance and its expected performance in Equation (1):




根据文献（Barber & Lyon，1996），异常经营绩效被定义为收购方已实现绩效与其预期绩效之间的差异，如公式（1）所示：


$$
A O P _ {i} = (O P _ {i t + 4} - O P _ {i t - 1}) - (O P _ {j t + 4} - O P _ {j t - 1})\tag{1}
$$




$$
A O P _ {i} = (O P _ {i t + 4} - O P _ {i t - 1}) - (O P _ {j t + 4} - O P _ {j t - 1})\tag{1}
$$


The realized performance (the first term) is calculated by subtracting the acquirer’s one-year lagged operating performance from its post-acquisition operating performance (four years after the fiscal year when the acquisition was undertaken). To compute a focal acquirer firm’s expected performance, we chose a group of firms that met the following criteria: (1) firms that did not go through any M&A activities for one year before and after the acquisition by the focal firm, (2) firms operating in the same industry based on two-digit SIC codes, and (3) firms whose operating performance was in the range of 90-110% of the focal firm. If a focal firm had no matched control firms, we relaxed the SIC criterion to one digit to find a match. If there was no match even with the relaxed condition, no SIC restriction was imposed. If no firm was matched, then a firm whose performance was the closest to the focal firm is chosen. The group of chosen firms serves together as a counterfactual of the focal firm, which proxies for what the focal firm’s performance would be had it not gone through the acquisition. Sensitivity to these matching criteria is tested later.




已实现业绩（第一项）的计算方法是从收购后的经营业绩（收购后的会计年度四年后）减去收购方滞后一年的经营业绩。为了计算焦点收购方公司的预期绩效，我们选择了一组满足以下标准的公司：（1）在被焦点公司收购前后一年内没有进行任何并购活动的公司，（2）基于两位数SIC代码在同一行业运营的公司，以及（3）经营业绩在焦点公司的90-110％范围内的公司。如果焦点公司没有匹配的控制公司，我们将 SIC 标准放宽到一位数以找到匹配。如果即使放宽条件也没有匹配，则不施加SIC限制。如果没有匹配的公司，则选择业绩最接近焦点公司的公司。选定的公司组一起充当焦点公司的反事实，它代表了焦点公司在没有进行收购的情况下的绩效。稍后测试对这些匹配标准的敏感性。


As the measure of operating performance, we used EBITDA (operating income before interest, tax, and depreciation and amortization) scaled by the market value of assets. This has been widely used as a measure of operating performance, as it can filter out any resulting changes from reshaping the firm’s capital structure due to acquisitions, such as financial expenses and taxes (Barber & Lyon, 1996; Fee & Thomas, 2004; Tanriverdi & Uysal, 2011).




作为衡量经营业绩的指标，我们使用按资产市场价值衡量的 EBITDA（未计利息、税项、折旧及摊销前的营业收入）。这已被广泛用作经营绩效的衡量标准，因为它可以过滤掉因收购而重塑公司资本结构所带来的任何变化，例如财务费用和税收（Barber & Lyon，1996；Fee & Thomas，2004；Tanriverdi & Uysal，2011）。


## Independent Variable




## 自变量


## IT Distance




## IT 距离


To measure IT distance, we collected detailed specifications of the firm’s enterprise systems from CITDB. We considered six IT components that are deeply tied to the firm’s business processes and operations—human resources, accounting/finance, supply-chain management, customer relationship management, data warehouse/business intelligence, and database management systems.<sup>5</sup> We collected information regarding the vendors of these six items for both acquirers and targets in our sample to construct the vector of the firms’ IT vendors.




为了衡量 IT 距离，我们从 CITDB 收集了该公司企业系统的详细规格。我们考虑了与公司业务流程和运营密切相关的六个 IT 组件——人力资源、会计/财务、供应链管理、客户关系管理、数据仓库/商业智能和数据库管理系统。<sup>5</sup>我们为样本中的收购方和目标收集了有关这六个项目的供应商的信息，以构建公司 IT 供应商的向量。


Individual components constituting IT systems are codependent—one cannot function without the others (Milgrom & Roberts, 1990). Thus, the IT distance in any one of the individual components would affect the performance of the other components, and ultimately, the system as a whole. Therefore, we operationalized IT distance based on the incompatibility in all six IT components as a whole. A similar holistic approach has been adopted by prior studies when conceptualizing IT systems and capabilities (Mehta & Hirschheim, 2007; Tanriverdi, 2006; Tanriverdi & Uysal, 2011).




构成 IT 系统的各个组件是相互依赖的——一个组件离开其他组件就无法发挥作用（Milgrom & Roberts，1990）。因此，任何一个单独组件中的 IT 距离都会影响其他组件的性能，并最终影响整个系统的性能。因此，我们根据所有六个IT组件作为一个整体的不兼容性来实施IT距离。先前的研究在概念化 IT 系统和功能时也采用了类似的整体方法（Mehta & Hirschheim，2007；Tanriverdi，2006；Tanriverdi & Uysal，2011）。


The operationalization of IT distance poses several challenges, one of which involves the degree of incompatibility between systems, which depends on how firms actually deploy and use them. Natively incompatible systems can communicate with the help of middleware that translates the different protocols and data models between them. This makes it difficult to hard-code incompatibility solely based on the specifications. Also, it would not be possible to determine a priori whether a certain pair of vendors would have a shorter or longer distance than the other pairs (e.g., whether the compatibility between Peoplesoft and SAP is better than that between Peoplesoft and Microsoft). One solution would be to quantify the distance based on the availability of support for intermodule communication, such as the number of APIs provided by the vendors. However, this would not tell us how well those APIs actually work regarding the ease of implementation and system performance.




IT距离的实施带来了一些挑战，其中之一涉及系统之间的不兼容程度，这取决于企业实际部署和使用它们的方式。本机不兼容的系统可以借助中间件进行通信，中间件可以在它们之间转换不同的协议和数据模型。这使得仅根据规范硬编码不兼容性变得困难。此外，不可能先验地确定某一对供应商是否比其他供应商对具有更短或更长的距离（例如，Peoplesoft 和 SAP 之间的兼容性是否优于 Peoplesoft 和 Microsoft 之间的兼容性）。一种解决方案是根据模块间通信支持的可用性（例如供应商提供的 API 数量）来量化距离。然而，这并不能告诉我们这些 API 在实施的简易性和系统性能方面的实际工作情况如何。


Given these challenges, the best way to measure IT distance is to rely on a grounded approach based on firms’ actual usage patterns of enterprise systems from different vendors. If a certain set of vendors are frequently adopted together within a firm, those vendors may have an acceptable level of compatibility. This assumption is reasonable: first, the enterprise systems that are adopted together by a large number of firms are likely to have a lower effort/cost of integration due to the ecosystem of tools and technologies that can facilitate integration; moreover, the human resources skilled in integrating these systems are likely to be more developed and easily accessible. Second, to the extent that the enterprise systems adopted together have a lower cost of integration due to the presence of greater knowledge, learning, and resource availability, a firm is likely to opt for vendors that are frequently adopted together to minimize integration costs. Therefore, those vendors appearing together more often within a firm can be considered “closer” in IT distance than other vendors that are rarely observed together.




考虑到这些挑战，衡量 IT 距离的最佳方法是依靠基于公司对不同供应商的企业系统的实际使用模式的扎实方法。如果某组供应商经常在公司内一起采用，那么这些供应商可能具有可接受的兼容性级别。这个假设是合理的：首先，由于可以促进集成的工具和技术生态系统，被大量公司共同采用的企业系统可能会降低集成的工作量/成本；此外，熟练整合这些系统的人力资源可能会更加发达并且更容易获得。其次，由于存在更多的知识、学习和资源可用性，一起采用的企业系统具有较低的集成成本，因此公司可能会选择经常一起采用的供应商，以最大限度地降低集成成本。因此，那些在公司内部经常一起出现的供应商可以被认为比其他很少一起出现的供应商在 IT 方面的距离“更近”。


Co-occurrence is the basis of modern natural language processing (NLP) techniques, such as word embedding. These are systematic and computational methods used to extract discernible, frequent patterns in terms of how words appear together in a sentence, paragraph, or document. The basic assumption is that those words appearing together are closely related in forming a semantic meaning; for example, the words “food,” “restaurant,” “burger,” and “pasta” appear together because they are related in the context of “eat.”




同现是现代自然语言处理（NLP）技术的基础，例如词嵌入。这些是系统性的计算方法，用于根据单词如何在句子、段落或文档中一起出现来提取可辨别的频繁模式。基本假设是，这些一起出现的词在形成语义时密切相关；例如，“食物”、“餐厅”、“汉堡”和“意大利面”这些词一起出现，因为它们在“吃”的上下文中相关。


Borrowing this idea, we employed a word-embedding technique called Word2Vec to extract patterns of IT vendor “co-occurrence.” The assumption we make here pertains to the relationship between co-occurrence and compatibility: if certain vendors are frequently adopted together within a firm, the systems from those co-appearing vendors are more compatible than the systems from other vendors that do not appear together. This operationalization based on co-occurrence addresses the aforementioned issues related to hard-coding—it captures compatibility based on the actual data regarding how frequently systems from different vendors are used together by firms.




借鉴这个想法，我们采用了一种名为 Word2Vec 的词嵌入技术来提取 IT 供应商“共现”的模式。我们在这里做出的假设涉及共现和兼容性之间的关系：如果某些供应商在一个公司内经常一起采用，那么来自这些共同出现的供应商的系统比其他不一起出现的供应商的系统具有更高的兼容性。这种基于共现的操作化解决了上述与硬编码相关的问题——它根据有关公司一起使用不同供应商的系统的频率的实际数据捕获兼容性。


To apply Word2Vec, we collected information on the vendors of enterprise systems for all companies available in CITDB at the establishment level. In CITDB, each firm has multiple establishments that may use the same or different vendors for the same IT component (e.g., CRM). The list of IT vendors adopted in a given firm is similar to the list of words used together in a sentence or document. After excluding firms with a single establishment, the number of firms with an available vendor list ranged from 4,500 to 23,000, depending on the enterprise systems components.




为了应用 Word2Vec，我们收集了 CITDB 中机构级别所有公司的企业系统供应商信息。在 CITDB 中，每个公司都有多个机构，这些机构可能使用相同或不同的供应商来提供相同的 IT 组件（例如 CRM）。给定公司采用的 IT 供应商列表类似于句子或文档中一起使用的单词列表。排除单一机构的公司后，拥有可用供应商名单的公司数量从 4,500 家到 23,000 家不等，具体取决于企业系统组件。


With these vendor lists, we first split the data into two sets— one for training the model and the other for validation. Then, the vendor lists were converted into the input data, which contain every possible ordered pair of vendors appearing within the same firm. For example, if a firm adopted three vendors— Microsoft, Oracle, and Intuit, then a total of six ordered pairs would be generated: (Microsoft, Oracle), (Microsoft, Intuit), (Oracle, Microsoft), (Oracle, Intuit), (Intuit, Microsoft), and (Intuit, Oracle). Using the input data, a neural network was trained that consisted of a 1 x N input layer, a 1 x M output layer, and an N x M hidden layer in between, where N is the total number of unique vendors, and M is the embedding size or the number of neurons in the hidden layer.<sup>6</sup> The input layer is a onehot encode vector with 1 for a focal vendor (e.g., Microsoft), and 0 for all other vendors. The hidden layer represents each vendor as an M-dimensional vector with numerical values, or as the embedding of a vendor, which looks up the embedding for the focal vendor identified by the input layer. Then, for each vendor (e.g., Oracle), the output layer calculates the probability that a randomly chosen vendor near the focal vendor (Microsoft) is this vendor (Oracle). The network is trained by minimizing the difference between the probabilities and the actual data. After training the network, we took the weight matrix of the hidden layer, or the embeddings. The procedure was repeated for all other components. The prediction accuracy on the validation dataset ranges from 0.81 to 0.91, which indicates that the trained network is able to predict whether a pair of two vendors appears in the same company in eight or nine out of 10 cases.




有了这些供应商列表，我们首先将数据分成两组——一组用于训练模型，另一组用于验证。然后，供应商列表被转换为输入数据，其中包含出现在同一公司内的每个可能的有序供应商对。例如，如果一家公司采用了三个供应商——Microsoft、Oracle 和 Intuit，那么总共会生成六个有序对：(Microsoft, Oracle)、(Microsoft, Intuit)、(Oracle, Microsoft)、(Oracle, Intuit)、(Intuit, Microsoft) 和 (Intuit, Oracle)。使用输入数据训练神经网络，该网络由 1 x N 输入层、1 x M 输出层和中间的 N x M 隐藏层组成，其中 N 是唯一供应商的总数，M 是隐藏层中的嵌入大小或神经元数量。<sup>6</sup>输入层是一个单热编码向量，其中 1 表示焦点供应商（例如 Microsoft），0 表示所有其他供应商。隐藏层将每个供应商表示为具有数值的 M 维向量，或者表示为供应商的嵌入，它查找输入层标识的焦点供应商的嵌入。然后，对于每个供应商（例如，Oracle），输出层计算靠近焦点供应商（Microsoft）的随机选择的供应商是该供应商（Oracle）的概率。通过最小化概率与实际数据之间的差异来训练网络。训练网络后，我们获取隐藏层的权重矩阵或嵌入。对所有其他组件重复该过程。验证数据集的预测准确度范围为 0.81 到 0.91，这表明经过训练的网络能够在 10 个案例中预测出 8 个或 9 个案例中两个供应商是否出现在同一家公司。


We calculated the distance between acquirer and target firms for each of the six IT components based on the cosine dissimilarity between the embeddings of the two vendors.<sup>7</sup> Then, the distance values were averaged across the six IT components to calculate the IT distance at the acquisition level, which we used as our primary independent variable.




我们根据两个供应商嵌入之间的余弦差异，计算了六个 IT 组件中每一个组件的收购方与目标公司之间的距离。<sup>7</sup>然后，对六个 IT 组件的距离值进行平均，以计算收购层面的 IT 距离，我们将其用作主要自变量。


## Validation of the IT Distance Measure




## IT 距离测量的验证


To check the validity of the embedding approach, we conducted several tests. First, we leveraged the fact that the IT distance between systems in the same product suite should be lower than that between systems from different vendors. Consider Peoplesoft, one of the major players in the accounting software market. Based on IT distance, the top three closest vendors to Peoplesoft’s accounting system in our sample are Microsoft (0.18), JD-Edwards (0.21), and Oracle (0.24). It is not surprising that JD-Edwards and Oracle are on top because Oracle acquired both Peoplesoft and JD-Edwards. Because these products belong to the Oracle suite, the compatibility among them is likely to be greater than that with other vendors’ products (Chellappa & Saraf, 2010). For SAP, another major player in enterprise accounting software, the closest vendors are Microsoft (0.30), Peoplesoft (0.41), and Mapics (acquired by Infor; 0.42). While these companies are all major players in the market and are presumably compatible with one another, the distance between SAP and Peoplesoft is larger than that between Peoplesoft and the other Oracle products (Oracle and JD-Edwards). This finding indicates that in our data, Peoplesoft is more frequently observed together with JD-Edwards and Oracle within a firm than SAP is with Peoplesoft, thereby indicating a greater level of compatibility.




为了检查嵌入方法的有效性，我们进行了多次测试。首先，我们利用了这样一个事实：同一产品套件中的系统之间的 IT 距离应该低于不同供应商的系统之间的 IT 距离。以 Peoplesoft 为例，它是会计软件市场的主要参与者之一。根据 IT 距离，在我们的样本中，与 Peoplesoft 会计系统最接近的前三个供应商是 Microsoft (0.18)、JD-Edwards (0.21) 和 Oracle (0.24)。 JD-Edwards 和 Oracle 名列前茅并不奇怪，因为 Oracle 收购了 Peoplesoft 和 JD-Edwards。由于这些产品属于 Oracle 套件，因此它们之间的兼容性可能比其他供应商的产品更好（Cellaappa & Saraf，2010）。对于企业会计软件领域的另一家主要厂商 SAP，最接近的供应商是 Microsoft (0.30)、Peoplesoft (0.41) 和 Mapics（被 Infor 收购；0.42）。虽然这些公司都是市场上的主要参与者，并且可能彼此兼容，但 SAP 和 Peoplesoft 之间的距离比 Peoplesoft 和其他 Oracle 产品（Oracle 和 JD-Edwards）之间的距离更大。这一发现表明，在我们的数据中，Peoplesoft 在一家公司内与 JD-Edwards 和 Oracle 一起出现的频率比 SAP 与 Peoplesoft 在一起的频率更高，从而表明了更高程度的兼容性。


Second, we conducted a survey of IT professionals to examine whether our measure based on co-occurrence is comparable with experts’ opinions in the field (see Appendix 1 for details). In each question, survey participants (247 in the final sample) were asked to rank-order three pairs of ES vendors (e.g., Peoplesoft – Salesforce) of a particular ES module (e.g., CRM) in terms of the relative cost of integrating the systems (or making them interoperable) from the two vendors in a given pair (Rank 1: the lowest cost; Rank 3: the highest cost). For each vendor pair in each module, we calculated IT distance using the average rank from the survey responses. Then, this surveybased IT distance measure was compared against our primary IT distance measure estimated using the word-embedding technique. The Pearson correlation between the two measures confirms a positive correlation (0.371, p < 0.01), as do alternative correlation measures and sampling methods, which further strengthens the validity of our IT distance measure (See Table A1 in the Appendix).




其次，我们对IT专业人士进行了调查，以检验我们基于共现的衡量标准是否与该领域专家的意见具有可比性（详见附录1）。在每个问题中，调查参与者（最终样本中的 247 名）被要求根据给定对中两个供应商集成系统（或使其可互操作）的相对成本对特定 ES 模块（例如，CRM）的三对 ES 供应商（例如，Peoplesoft – Salesforce）进行排名（排名 1：最低成本；排名 3：最高成本）。对于每个模块中的每个供应商对，我们使用调查回复的平均排名来计算 IT 距离。然后，将这种基于调查的 IT 距离测量与我们使用词嵌入技术估计的主要 IT 距离测量进行比较。两种测量之间的 Pearson 相关性证实了正相关（0.371，p < 0.01），替代相关测量和抽样方法也是如此，这进一步增强了我们的 IT 距离测量的有效性（参见附录中的表 A1）。


## M&A Motivation




## 并购动机


We collected data on the strategic motivation of each M&A deal from SDC. Based on the “purpose” code in the SDC database, a deal was marked as either M&A for operational synergy (e.g., “strengthen operations,” “create synergies; eliminate duplicate services/operations”) or M&A for nonoperational synergy (e.g., “increase shareholder value/dilute the number of outstanding shares,” “raise cash in conjunction with financing the concurrent acquisition/merger”) if it included one of the motivations defined for the category. Table A2 reports the complete list of M&A motivations. Sensitivity to alternative operationalizations is tested later.




我们从 SDC 收集了有关每笔并购交易战略动机的数据。根据 SDC 数据库中的“目的”代码，如果交易包含为该类别定义的动机之一，则该交易被标记为运营协同效应的并购（例如，“加强运营”、“创造协同效应；消除重复的服务/运营”）或非运营协同效应的并购（例如，“增加股东价值/稀释流通股数量”、“筹集现金并为同时收购/合并融资”）。表 A2 报告了并购动机的完整列表。稍后测试对替代操作的敏感性。


## Control Variables




## 控制变量


We considered a set of control variables that have been found to affect post-acquisition performance, including public company indicator (1 if the target is a publicly traded company, and 0 otherwise), firm size (acquirer’s market capitalization), relative transaction size (ratio of the transaction size to the acquirer’s market capitalization), book leverage (acquirer’s debt-to-asset ratio), prior financial performance (acquirer’s operating income one year prior to the acquisition), prior acquisition experience (total number of acquisitions an acquirer completed in the past three years), prior acquisition performance (ratio of the number of acquisitions with a positive CAR to the total number of acquisitions in the past three years), market-to-book value of an acquirer’s assets, industry-relatedness indicators (SIC2 (SIC4) is assigned 1 if the acquirer and target are in the same two-digit (four-digit) SIC industry, and 0 otherwise), same-state indicator (1 if the acquirer and target are in the same state, and 0 otherwise), and industry IT intensity (IT budgets aggregated at the four-digit SIC level). Tables 1 and 2 report the descriptive statistics and pairwise correlations.




我们考虑了一组影响收购后绩效的控制变量，包括上市公司指标（如果目标是上市公司，则为1，否则为0）、公司规模（收购方的市值）、相对交易规模（交易规模与收购方市值的比率）、账面杠杆（收购方的资产负债率）、先前的财务绩效（收购方收购前一年的营业收入）、先前的收购经验（收购方近三年完成的收购总数）、过往收购业绩（资本充足率为正的收购数量占近三年收购总数的比例）、收购方资产市净率、行业相关性指标（如果收购方与目标公司属于同一两位数（四位）SIC行业，则SIC2（SIC4）为1，否则为0），同状态指标（如果收购方与目标公司属于相同的两位数（四位数）行业，则SIC2（SIC4）为1，否则为0）。收购方和目标处于相同状态，否则为 0），以及行业 IT 强度（IT 预算以四位数 SIC 级别汇总）。表 1 和表 2 报告了描述性统计数据和成对相关性。


## Model Specification




## 型号规格


To test our hypotheses, we estimated Equation (2):




为了检验我们的假设，我们估计了方程（2）：


$$
Y _ {i} = \alpha + \beta \cdot I _ {i} + X _ {i} \pmb {\gamma} _ {i} + \varepsilon_ {i}\tag{2}
$$




$$
Y _ {i} = \alpha + \beta \cdot I _ {i} + X _ {i} \pmb {\gamma} _ {i} + \varepsilon_ {i}\tag{2}
$$


where $Y _ { i }$ is the acquirer’s abnormal operating performance for acquisition i, and $I _ { i }$ is the IT distance between the acquirer and target firms of that acquisition. $X _ { i }$ is a vector of the control variables mentioned above, as well as a set of announcementyear indicators, accounting for temporal shocks on the abnormal operating performance of the acquisition. $\varepsilon _ { i }$ is the error component. ?? captures the effect of IT distance on abnormal operating performance. We estimated the model using ordinary least squares (OLS) with robust standard errors.




其中$Y _ { i }$是收购方在收购i时的异常经营业绩，$I _ { i }$是收购方与该次收购的目标公司之间的IT距离。 $X _ { i }$是上述控制变量的向量，以及一组公告年度指标，解释了收购异常经营绩效的时间冲击。 $\varepsilon _ { i }$ 是误差分量。 ??捕捉 IT 距离对异常运营绩效的影响。我们使用具有稳健标准误差的普通最小二乘法 (OLS) 来估计模型。


## Results




＃＃ 结果


## Effect of IT Distance on Abnormal Operating Performance




## IT距离对异常运营绩效的影响


Figure 1 shows scatter plots of the M&As for non-operational synergy, operational synergy, and the total number of M&As, with the level of IT distance on the x-axis and the abnormal operating performance on the y-axis. The rightmost panel indicates a downward slope of performance as IT distance increases, with a coefficient of -0.14 (p < 0.05). This model-free evidence indicates that IT distance is negatively associated with post-acquisition performance.




图1展示了非运营协同、运营协同和并购总数的并购散点图，横轴为IT距离水平，纵轴为经营绩效异常水平。最右边的面板表明随着 IT 距离的增加，性能呈下降趋势，系数为 -0.14 (p < 0.05)。这一无模型的证据表明，IT 距离与收购后的绩效呈负相关。


Next, we regressed the abnormal operating performance on IT distance, as well as the control variables. The first column of Table 3 is the baseline model only with the control variables. The second model shows a negative and statistically significant coefficient of IT distance (-0.153; p < 0.05), supporting H1, that IT distance is negatively associated with post-acquisition performance. Compared to the first model, the R-squared of the second model increases by 17% (0.118 to 0.139; p < 0.05), suggesting that adding IT distance significantly improves the model’s explanatory power.




接下来，我们对 IT 距离以及控制变量上的异常运行性能进行了回归。表 3 的第一列是仅包含控制变量的基线模型。第二个模型显示 IT 距离的负系数且具有统计显着性（-0.153；p < 0.05），支持 H1，即 IT 距离与收购后绩效负相关。与第一个模型相比，第二个模型的 R 平方增加了 17%（0.118 至 0.139；p < 0.05），表明增加 IT 距离显着提高了模型的解释力。


<table><tr><td colspan="5">Table 1. Descriptive Statistics</td></tr><tr><td></td><td>Mean</td><td>SD</td><td>Min</td><td>Max</td></tr><tr><td>Abnormal operating performance</td><td>0.00</td><td>0.03</td><td>-0.12</td><td>0.18</td></tr><tr><td>IT distance</td><td>0.13</td><td>0.14</td><td>-0.00</td><td>0.70</td></tr><tr><td>Public</td><td>0.31</td><td>0.46</td><td>0.00</td><td>1.00</td></tr><tr><td>Firm size</td><td>9.16</td><td>1.48</td><td>5.68</td><td>12.39</td></tr><tr><td>Relative transaction size</td><td>0.13</td><td>0.20</td><td>0.00</td><td>1.69</td></tr><tr><td>Book leverage</td><td>0.64</td><td>0.18</td><td>0.22</td><td>1.17</td></tr><tr><td>Prior financial performance</td><td>0.10</td><td>0.05</td><td>0.00</td><td>0.27</td></tr><tr><td>Prior M&amp;A experience</td><td>1.99</td><td>2.13</td><td>0.00</td><td>13.00</td></tr><tr><td>Prior M&amp;A performance</td><td>0.34</td><td>0.39</td><td>0.00</td><td>1.00</td></tr><tr><td>Market-to-book value of assets</td><td>1.50</td><td>0.49</td><td>0.74</td><td>3.00</td></tr><tr><td>Industry relatedness (SIC2)</td><td>0.52</td><td>0.50</td><td>0.00</td><td>1.00</td></tr><tr><td>Industry relatedness (SIC4)</td><td>0.28</td><td>0.45</td><td>0.00</td><td>1.00</td></tr><tr><td>Same state</td><td>0.10</td><td>0.30</td><td>0.00</td><td>1.00</td></tr><tr><td>Industry IT intensity</td><td>20.24</td><td>1.52</td><td>15.99</td><td>23.72</td></tr><tr><td>Observations</td><td colspan="4">185</td></tr></table>




<table><tr><td colspan="5">表1.描述性统计</td></tr><tr><td></td><td>平均值</td><td>SD</td><td>最小值</td><td>最大值</td></tr><tr><td>异常操作性能</td><td>0.00</td><td>0.03</td><td>-0.12</td><td>0.18</td></tr><tr><td>IT距离</td><td>0.13</td><td>0.14</td><td>-0.00</td><td>0.70</td></tr><tr><td>上市</td><td>0.31</td><td>0.46</td><td>0.00</td><td>1.00</td></tr><tr><td>公司大小</td><td>9.16</td><td>1.48</td><td>5.68</td><td>12.39</td></tr><tr><td>相对交易尺寸</td><td>0.13</td><td>0.20</td><td>0.00</td><td>1.69</td></tr><tr><td>预订杠杆</td><td>0.64</td><td>0.18</td><td>0.22</td><td>1.17</td></tr><tr><td>之前的财务状况业绩</td><td>0.10</td><td>0.05</td><td>0.00</td><td>0.27</td></tr><tr><td>之前的并购经验</td><td>1.99</td><td>2.13</td><td>0.00</td><td>13.00</td></tr><tr><td>之前的并购业绩</td><td>0.34</td><td>0.39</td><td>0.00</td><td>1.00</td></tr><tr><td>市净率资产</td><td>1.50</td><td>0.49</td><td>0.74</td><td>3.00</td></tr><tr><td>行业相关性(SIC2)</td><td>0.52</td><td>0.50</td><td>0.00</td><td>1.00</td></tr><tr><td>行业相关性(SIC4)</td><td>0.28</td><td>0.45</td><td>0.00</td><td>1.00</td></tr><tr><td>相同州</td><td>0.10</td><td>0.30</td><td>0.00</td><td>1.00</td></tr><tr><td>行业IT强度</td><td>20.24</td><td>1.52</td><td>15.99</td><td>23.72</td></tr><tr><td>观察</td><td colspan="4">185</td></tr></table>


Table 2. Pairwise Correlations




表 2. 成对相关性


<table><tr><td></td><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td></tr><tr><td>1</td><td>Abnormal operating performance</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>IT distance</td><td>-0.14*</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>Public</td><td>-0.02</td><td>0.01</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>Firm size</td><td>-0.01</td><td>-0.07</td><td>0.36***</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>Relative transaction size</td><td>0.04</td><td>-0.00</td><td>0.34***</td><td>-0.19**</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6</td><td>Book leverage</td><td>0.01</td><td>-0.13*</td><td>0.08</td><td>0.06</td><td>0.13*</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7</td><td>Prior financial performance</td><td>-0.09</td><td>0.01</td><td>-0.05</td><td>0.14*</td><td>-0.20***</td><td>-0.50***</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>8</td><td>Prior M&amp;A experience</td><td>-0.00</td><td>0.08</td><td>0.16**</td><td>0.38***</td><td>-0.13*</td><td>-0.16**</td><td>0.18**</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>9</td><td>Prior M&amp;A performance</td><td>-0.06</td><td>0.13*</td><td>-0.11</td><td>0.09</td><td>-0.05</td><td>-0.14**</td><td>0.09</td><td>0.35***</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>10</td><td>Market-to-book value of assets</td><td>-0.08</td><td>0.07</td><td>-0.06</td><td>0.27***</td><td>-0.29***</td><td>-0.38***</td><td>0.72***</td><td>0.27***</td><td>0.12*</td><td>1.00</td><td></td><td></td><td></td><td></td></tr><tr><td>11</td><td>Industry relatedness (SIC2)</td><td>-0.09</td><td>-0.05</td><td>0.06</td><td>-0.16**</td><td>0.16**</td><td>0.15**</td><td>-0.09</td><td>-0.29***</td><td>-0.12*</td><td>-0.12*</td><td>1.00</td><td></td><td></td><td></td></tr><tr><td>12</td><td>Industry relatedness (SIC4)</td><td>-0.03</td><td>-0.01</td><td>0.01</td><td>-0.10</td><td>0.10</td><td>0.15**</td><td>-0.08</td><td>-0.14*</td><td>-0.02</td><td>-0.09</td><td>0.59***</td><td>1.00</td><td></td><td></td></tr><tr><td>13</td><td>Same state</td><td>0.03</td><td>-0.02</td><td>0.04</td><td>0.08</td><td>-0.05</td><td>-0.15**</td><td>0.11</td><td>0.12*</td><td>0.03</td><td>0.06</td><td>-0.04</td><td>-0.02</td><td>1.00</td><td></td></tr><tr><td>14</td><td>Industry IT intensity</td><td>0.01</td><td>-0.11</td><td>0.19***</td><td>0.29***</td><td>0.04</td><td>0.30***</td><td>-0.25***</td><td>0.09</td><td>-0.01</td><td>-0.27***</td><td>0.11</td><td>0.18**</td><td>0.05</td><td>1.00</td></tr></table>




<table><tr><td></td><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td >8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td></tr><tr><td>1</td><td>异常经营性能</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><t d></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>IT距离</td><td>-0.14*</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td>< td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>浦blic</td><td>-0.02</td><td>0.01</td><td>1.00</td><td></td><td></td><td></td><td></td><t d></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>公司尺寸</td><td>-0.01</td><td>-0.07</td><td>0.36***</td><td>1.00</td><td></td><td></td><td></td> <td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>相对交易尺寸</td><td>0.04</td><td>-0.00</td><td>0.34***</td><td>-0.19**</td><td>1.00</td><td></td><td> </td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6</td><td>预订杠杆</td><td>0.01</td><td>-0.13*</td><td>0.08</td><td>0.06</td><td>0.13*</td><td>1.00</td><td ></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7</td><td>之前金融性能</td><td>-0.09</td><td>0.01</td><td>-0.05</td><td>0.14*</td><td>-0.20***</td><td>-0.50***</td ><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>8</td><td>之前并购体验</td><td>-0.00</td><td>0.08</td><td>0.16**</td><td>0.38***</td><td>-0.13*</td><td>-0.16**</td><td >0.18**</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>9</td><td>之前并购性能</td><td>-0.06</td><td>0.13*</td><td>-0.11</td><td>0.09</td><td>-0.05</td><td>-0.14**</td><td>0.09</td ><td>0.35***</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>10</td><td>市场账面价值的值资产</td><td>-0.08</td><td>0.07</td><td>-0.06</td><td>0.27***</td><td>-0.29***</td><td>-0.38***</td><td>0.72***< /td><td>0.27***</td><td>0.12*</td><td>1.00</td><td></td><td></td><td></td><td></td></tr><tr><td>11</td><td>行业相关性(SIC2)</td><td>-0.09</td><td>-0.05</td><td>0.06</td><td>-0.16**</td><td>0.16**</td><td>0.15**</td><td>-0.09</td><td >-0.29***</td><td>-0.12*</td><td>-0.12*</td><td>1.00</td><td></td><td></td><td></td></tr><tr><td>12</td><td>行业相关性(SIC4)</td><td>-0.03</td><td>-0.01</td><td>0.01</td><td>-0.10</td><td>0.10</td><td>0.15**</td><td>-0.08</td><td>- 0.14*</td><td>-0.02</td><td>-0.09</td><td>0.59***</td><td>1.00</td><td></td><td></td></tr><tr><td>13</td><td>相同状态</td><td>0.03</td><td>-0.02</td><td>0.04</td><td>0.08</td><td>-0.05</td><td>-0.15**</td><td>0.11</td><td>0.12 *</td><td>0.03</td><td>0.06</td><td>-0.04</td><td>-0.02</td><td>1.00</td><td></td></tr><tr><td>14</td><td>行业信息技术强度</td><td>0.01</td><td>-0.11</td><td>0.19***</td><td>0.29***</td><td>0.04</td><td>0.30***</td><td>-0.25***< /td><td>0.09</td><td>-0.01</td><td>-0.27***</td><td>0.11</td><td>0.18**</td><td>0.05</td><td>1.00</td></tr></table>


Note: \*p < 0.1, \*\*p < 0.05, \*\* p < 0.01




注：\*p < 0.1、\*\*p < 0.05、\*\* p < 0.01


![](/api/attachments/EQEMG87U/fulltext/images/9ab24670495a1eab470b3868c012be5bb108f663f56aaecf075370d38bc4ce32.jpg)  
Figure 1. Abnormal Operating Performance by Acquisition Motivation




![](/api/attachments/EQEMG87U/fulltext/images/9ab24670495a1eab470b3868c012be5bb108f663f56aaecf075370d38bc4ce32.jpg)  
图 1. 按收购动机划分的异常经营业绩


<table><tr><td colspan="5">Table 3. Effect of IT Distance on Abnormal Operating Performance</td></tr><tr><td></td><td colspan="2">(1)</td><td colspan="2">(2)</td></tr><tr><td>Public</td><td>-0.087</td><td>(-1.02)</td><td>-0.074</td><td>(-0.90)</td></tr><tr><td>Firm size</td><td>0.059</td><td>(0.69)</td><td>0.036</td><td>(0.43)</td></tr><tr><td>Relative transaction size</td><td>0.060</td><td>(0.73)</td><td>0.061</td><td>(0.75)</td></tr><tr><td>Book leverage</td><td>-0.053</td><td>(-0.51)</td><td>-0.069</td><td>(-0.66)</td></tr><tr><td>Prior financial performance</td><td>-0.130</td><td>(-0.75)</td><td>-0.156</td><td>(-0.93)</td></tr><tr><td>Prior M&amp;A experience</td><td>-0.068</td><td>(-0.93)</td><td>-0.060</td><td>(-0.80)</td></tr><tr><td>Prior M&amp;A performance</td><td>-0.094</td><td>(-1.07)</td><td>-0.075</td><td>(-0.90)</td></tr><tr><td>Market-to-book value of assets</td><td>0.085</td><td>(0.56)</td><td>0.108</td><td>(0.73)</td></tr><tr><td>Industry relatedness (SIC2)</td><td>-0.156*</td><td>(-1.92)</td><td>-0.161*</td><td>(-1.96)</td></tr><tr><td>Industry relatedness (SIC4)</td><td>-0.092</td><td>(-1.19)</td><td>-0.090</td><td>(-1.15)</td></tr><tr><td>Same state</td><td>0.081</td><td>(1.14)</td><td>0.079</td><td>(1.20)</td></tr><tr><td>Industry IT intensity</td><td>0.003</td><td>(0.02)</td><td>0.012</td><td>(0.11)</td></tr><tr><td>IT distance</td><td></td><td></td><td>-0.153**</td><td>(-2.13)</td></tr><tr><td>R-squared</td><td>0.118</td><td></td><td>0.139</td><td></td></tr><tr><td>N</td><td colspan="2">185</td><td colspan="2">185</td></tr></table>




<table><tr><td colspan="5">表 3. IT 距离对异常运营绩效的影响</td></tr><tr><td></td><td colspan="2">(1)</td><td colspan="2">(2)</td></tr><tr><td>公开</td><td>-0.087</td><td>(-1.02)</td><td>-0.074</td><td>(-0.90)</td></tr><tr><td>公司大小</td><td>0.059</td><td>(0.69)</td><td>0.036</td><td>(0.43)</td></tr><tr><td>相对交易尺寸</td><td>0.060</td><td>(0.73)</td><td>0.061</td><td>(0.75)</td></tr><tr><td>预订杠杆</td><td>-0.053</td><td>(-0.51)</td><td>-0.069</td><td>(-0.66)</td></tr><tr><td>之前的财务状况业绩</td><td>-0.130</td><td>(-0.75)</td><td>-0.156</td><td>(-0.93)</td></tr><tr><td>之前的并购经验</td><td>-0.068</td><td>(-0.93)</td><td>-0.060</td><td>(-0.80)</td></tr><tr><td>之前的并购业绩</td><td>-0.094</td><td>(-1.07)</td><td>-0.075</td><td>(-0.90)</td></tr><tr><td>市净率资产</td><td>0.085</td><td>(0.56)</td><td>0.108</td><td>(0.73)</td></tr><tr><td>行业相关性(SIC2)</td><td>-0.156*</td><td>(-1.92)</td><td>-0.161*</td><td>(-1.96)</td></tr><tr><td>行业相关性(SIC4)</td><td>-0.092</td><td>(-1.19)</td><td>-0.090</td><td>(-1.15)</td></tr><tr><td>相同状态</td><td>0.081</td><td>(1.14)</td><td>0.079</td><td>(1.20)</td></tr><tr><td>行业IT强度</td><td>0.003</td><td>(0.02)</td><td>0.012</td><td>(0.11)</td></tr><tr><td>IT距离</td><td></td><td></td><td>-0.153**</td><td>(-2.13)</td></tr><tr><td>R-平方</td><td>0.118</td><td></td><td>0.139</td><td></td></tr><tr><td>N</td><td colspan="2">185</td><td colspan="2">185</td></tr></table>


Note: The dependent variable is the acquirer's abnormal operating income measured as the change in the performance-adjusted operating performance scaled by assets from Year -1 to Year +4. Standardized beta coefficients and robust standard errors are used. t-statistics are in parentheses. Announcement years and industries are controlled. $^ { \star } p < 0 . 1 , ^ { \star \star } p < 0 . 0 5 , ^ { \star \star } p < 0 . 0 1$




注：因变量为收购方非正常营业收入，以-1年至+4年按资产调整业绩调整后的经营业绩变化来衡量。使用标准化贝塔系数和稳健标准误差。 t-统计量在括号中。公告年份及行业受控。 $^ { \star } p < 0 。 1 , ^ { \star \star } p < 0 。 0 5 , ^ { \star \star } p < 0 。 0 1$


## Differential Effects of IT Distance by Acquisition Motivation




## IT 距离对收购动机的不同影响


H2 suggests that the performance effect of IT distance will be stronger in acquisitions motivated by operational synergies (i.e., when value creation heavily depends on the integration of IT systems) than in acquisitions motivated by non-operational synergies (i.e., when IT integration is not vital to creating synergy). To test H2, we split the samples into two groups based on whether an acquisition is motivated by operational or nonoperational synergy.




H2表明，IT距离对绩效的影响在由运营协同效应驱动的收购中（即，当价值创造严重依赖于IT系统的集成时）比在由非运营协同效应驱动的收购中（即，当IT集成对于创造协同效应并不重要时）更强。为了测试 H2，我们根据收购是由运营协同还是非运营协同推动将样本分为两组。


In Table 4, the first column shows the regression estimates for the acquisitions motivated by operational synergy. The coefficient of IT distance is negative and significant (-0.317, p < 0.01), and the magnitude of the coefficient is substantially larger than the full sample estimate (see Table 3). In contrast, the coefficient of IT distance from the acquisitions motivated by non-operational synergy (the second column) is very small (0.025) and statistically insignificant. This result is consistent with the modelfree evidence in Figure 1—the slope of the best fit line for the acquisitions driven by non-operational synergy (the first panel) is flat, while the best fit line for the acquisitions seeking operational synergy (the second panel) is clearly downward-sloping. Taken together, the results support H2 that the effect of IT distance is more pronounced for acquisitions seeking operational synergy than those motivated by non-operational synergy.




在表 4 中，第一列显示了运营协同推动的收购的回归估计。 IT距离的系数为负且显着（-0.317，p < 0.01），并且系数的大小远大于全样本估计（见表3）。相比之下，IT 与非运营协同推动的收购（第二列）的距离系数非常小 (0.025)，并且在统计上不显着。这一结果与图 1 中的无模型证据一致——非运营协同驱动的收购（第一幅图）的最佳拟合线的斜率是平坦的，而寻求运营协同的收购（第二幅图）的最佳拟合线明显向下倾斜。总而言之，结果支持 H2，即 IT 距离对于寻求运营协同效应的收购的影响比非运营协同效应的收购更为明显。


## Sensitivity Analyses




## 敏感性分析


To ensure the robustness of the findings, we conducted a series of sensitivity analyses by considering an alternative operating performance measure, identification assumptions, model uncertainty, variable definitions, outliers, and the cooccurrence assumption.




为了确保研究结果的稳健性，我们通过考虑替代经营绩效指标、识别假设、模型不确定性、变量定义、异常值和共现假设，进行了一系列敏感性分析。


## An Alternative Operating Performance Measure




## 另一种运营绩效衡量标准


Our original measure of operating performance used the market value of assets instead of the book value as the denominator, as the former reflects the current value of assets more accurately than the latter (Barber & Lyon, 1996; Healy et al., 1992). However, it has been suggested that the market value may be correlated with the operating income, which could cancel out any changes in performance (Heron & Lie, 2002); therefore, this may cause biases in our estimates. To address this concern, we estimated abnormal operating performance using the book value-scaled measure and repeated the regression analyses. Models 4-6 in Table A3 report the results, which are consistent with our main findings (see Models 1-3).




我们最初衡量经营业绩的方法是使用资产的市场价值而不是账面价值作为分母，因为前者比后者更准确地反映资产的当前价值（Barber & Lyon，1996；Healy 等，1992）。然而，有人认为市场价值可能与营业收入相关，这可能会抵消业绩的任何变化（Heron & Lie，2002）；因此，这可能会导致我们的估计出现偏差。为了解决这个问题，我们使用账面价值衡量指标来估计异常经营绩效，并重复回归分析。表 A3 中的模型 4-6 报告了结果，这与我们的主要发现一致（参见模型 1-3）。


## Identification Assumptions




## 识别假设


Our estimation of post-acquisition performance depends on the assumption that a company’s decision to engage in an acquisition is independent of the decision’s outcome (i.e., post-acquisition performance), conditional on its historical performance and the industry segment to which it belongs. This identification assumption is proposed by Barber and Lyon (1996), who demonstrate the superiority of this method over various alternative measures of abnormal operating performance. Although this assumption has been widely adopted by management researchers (Heron & Lie, 2002; Tanriverdi & Uysal, 2011; Zollo & Meier, 2008), it is still possible that there may be some other factors that are unaccounted for in the model but nevertheless have the potential to affect both the decision and performance.




我们对收购后业绩的估计取决于这样的假设：公司进行收购的决定独立于决策结果（即收购后业绩），并以其历史业绩和所属行业为条件。这种识别假设是由 Barber 和 Lyon (1996) 提出的，他们证明了这种方法相对于异常运行绩效的各种替代措施的优越性。尽管这一假设已被管理研究人员广泛采用（Heron & Lie，2002；Tanriverdi & Uysal，2011；Zollo & Meier，2008），但模型中仍有可能未考虑到其他一些因素，但仍有可能影响决策和绩效。


To address this issue, we added two matching criteria to our estimation procedure: firms whose size (based on assets) is in the range of 70%-130% of the focal firm, and firms located in the same state. When a focal firm had no matched control firms, we first excluded the same state restriction and the firm size restriction, and then followed the exclusion order of the original measure.




为了解决这个问题，我们在估算程序中添加了两个匹配标准：规模（基于资产）在焦点公司的 70%-130% 范围内的公司，以及位于同一州的公司。当焦点企业没有匹配的控制企业时，我们首先排除相同的国家限制和企业规模限制，然后遵循原始措施的排除顺序。


Another potential issue is that some firms may possess private information allowing them to reduce the uncertainty associated with acquisition deals and their potential outcome, which will facilitate the justification and execution of these acquisitions. To address this issue, when choosing a control group, we matched a sample firm to those companies that not only shared similar historical performance and operated in the same industry, but also had announced an acquisition but did not complete it.<sup>8</sup> The rationale is that while the companies that announced an acquisition (but did not follow up) are likely to have similar unobserved characteristics with those that announced and completed an acquisition, their operating performance would not be affected by the acquisition (because it was not completed). Adding this “no-completion” rule ensured that in our setting, the acquisition decision was independent of the acquisition outcome.




另一个潜在问题是，一些公司可能拥有私人信息，使他们能够减少与收购交易及其潜在结果相关的不确定性，这将有助于这些收购的合理性和执行。为了解决这个问题，在选择对照组时，我们将样本公司与那些既具有相似的历史业绩且经营相同行业，又宣布收购但未完成的公司进行了匹配。<sup>8</sup>理由是，虽然宣布收购（但未跟进）的公司可能与宣布并完成收购的公司具有类似的未观察到的特征，但其经营业绩不会受到收购的影响（因为收购未完成）。添加此“不完成”规则可确保在我们的设置中，收购决策独立于收购结果。


We applied this no-completion rule to both the primary (market value-scaled) and alternative (book value-scaled) operating performance measures. In Table A3, Models 7-9 and Models 10-12 show the results based on our primary operating performance measure with the no-completion rule and the alternative measure with the same criteria, respectively. Overall, the findings are consistent, thereby adding to the validity of our results.




我们将这种不完成规则应用于主要（按市值衡量）和替代（按账面价值衡量）经营绩效指标。在表 A3 中，模型 7-9 和模型 10-12 分别显示了基于不完成规则的主要经营绩效衡量标准和具有相同标准的替代衡量标准的结果。总的来说，研究结果是一致的，从而增加了我们结果的有效性。


<table><tr><td colspan="5">Table 4. IT Distance Effects by Different Acquisition Motivations</td></tr><tr><td rowspan="2"></td><td colspan="2">(1)</td><td colspan="2">(2)</td></tr><tr><td colspan="2">Operational synergy</td><td colspan="2">Non-operational synergy</td></tr><tr><td>Public</td><td>-0.081</td><td>(-0.82)</td><td>-0.030</td><td>(-0.14)</td></tr><tr><td>Firm size</td><td>0.123</td><td>(1.11)</td><td>-0.204</td><td>(-1.26)</td></tr><tr><td>Relative transaction size</td><td>0.025</td><td>(0.24)</td><td>0.104</td><td>(0.73)</td></tr><tr><td>Book leverage</td><td>-0.206</td><td>(-1.60)</td><td>0.194</td><td>(1.50)</td></tr><tr><td>Prior financial performance</td><td>-0.147</td><td>(-0.84)</td><td>-0.206</td><td>(-0.57)</td></tr><tr><td>Prior M&amp;A experience</td><td>0.039</td><td>(0.36)</td><td>-0.128</td><td>(-0.70)</td></tr><tr><td>Prior M&amp;A performance</td><td>-0.116</td><td>(-0.90)</td><td>-0.015</td><td>(-0.12)</td></tr><tr><td>Market-to-book value of assets</td><td>0.088</td><td>(0.60)</td><td>0.088</td><td>(0.29)</td></tr><tr><td>Industry relatedness (SIC2)</td><td>-0.137</td><td>(-1.43)</td><td>-0.193</td><td>(-1.14)</td></tr><tr><td>Industry relatedness (SIC4)</td><td>0.025</td><td>(0.27)</td><td>-0.021</td><td>(-0.12)</td></tr><tr><td>Same state</td><td>0.071</td><td>(0.87)</td><td>-0.062</td><td>(-0.44)</td></tr><tr><td>Industry IT intensity</td><td>-0.036</td><td>(-0.31)</td><td>0.346*</td><td>(1.71)</td></tr><tr><td>IT distance</td><td>-0.317***</td><td>(-3.67)</td><td>0.025</td><td>(0.22)</td></tr><tr><td>R-squared</td><td>0.263</td><td></td><td>0.304</td><td></td></tr><tr><td>N</td><td colspan="2">111</td><td colspan="2">74</td></tr><tr><td>IT distance between-group difference</td><td colspan="4">p&lt;0.001</td></tr></table>




<table><tr><td colspan="5">表 4. 不同收购动机对 IT 距离的影响</td></tr><tr><td rowspan="2"></td><td colspan="2">(1)</td><td colspan="2">(2)</td></tr><tr><td colspan="2">运营协同</td><td colspan="2">非经营性协同效应</td></tr><tr><td>公开</td><td>-0.081</td><td>(-0.82)</td><td>-0.030</td><td>(-0.14)</td></tr><tr><td>公司大小</td><td>0.123</td><td>(1.11)</td><td>-0.204</td><td>(-1.26)</td></tr><tr><td>相对交易尺寸</td><td>0.025</td><td>(0.24)</td><td>0.104</td><td>(0.73)</td></tr><tr><td>预订杠杆</td><td>-0.206</td><td>(-1.60)</td><td>0.194</td><td>(1.50)</td></tr><tr><td>之前的财务状况业绩</td><td>-0.147</td><td>(-0.84)</td><td>-0.206</td><td>(-0.57)</td></tr><tr><td>之前的并购经验</td><td>0.039</td><td>(0.36)</td><td>-0.128</td><td>(-0.70)</td></tr><tr><td>之前的并购业绩</td><td>-0.116</td><td>(-0.90)</td><td>-0.015</td><td>(-0.12)</td></tr><tr><td>市净率资产</td><td>0.088</td><td>(0.60)</td><td>0.088</td><td>(0.29)</td></tr><tr><td>行业相关性(SIC2)</td><td>-0.137</td><td>(-1.43)</td><td>-0.193</td><td>(-1.14)</td></tr><tr><td>行业相关性(SIC4)</td><td>0.025</td><td>(0.27)</td><td>-0.021</td><td>(-0.12)</td></tr><tr><td>相同状态</td><td>0.071</td><td>(0.87)</td><td>-0.062</td><td>(-0.44)</td></tr><tr><td>行业IT强度</td><td>-0.036</td><td>(-0.31)</td><td>0.346*</td><td>(1.71)</td></tr><tr><td>IT距离</td><td>-0.317***</td><td>(-3.67)</td><td>0.025</td><td>(0.22)</td></tr><tr> <td>R平方</td><td>0.263</td><td></td><td>0.304</td><td></td></tr><tr><td>N</td><td colspan="2">111</td><td colspan="2">74</td></tr><tr><td>组间IT距离差异</td><td colspan="4">p<0.001</td></tr></table>


Note: The dependent variable is the acquirer's abnormal operating income measured as the change in the performance-adjusted operating performance scaled by assets from Year -1 to Year +4. Standardized beta coefficients and robust standard errors are used. t-statistics are in parentheses. Announcement years and industries are controlled. $^ { \star } p < 0 . 1 , ^ { \star \star } p < 0 . 0 5 , ^ { \star \star } p < 0 . 0 1$




注：因变量为收购方非正常营业收入，以-1年至+4年按资产调整业绩调整后的经营业绩变化来衡量。使用标准化贝塔系数和稳健标准误差。 t-统计量在括号中。公告年份及行业受控。 $^ { \star } p < 0 。 1 , ^ { \star \star } p < 0 。 0 5 , ^ { \star \star } p < 0 。 0 1$


## Model Uncertainty




## 模型不确定性


Model uncertainty refers to the uncertainty regarding which variables to include in the model specifications: researchers explore different specifications by adding or dropping variables. Ignoring this uncertainty may overstate or understate the effect of the variables (Arin et al., 2015).




模型不确定性是指模型规格中包含哪些变量的不确定性：研究人员通过添加或删除变量来探索不同的规格。忽略这种不确定性可能会夸大或低估变量的影响（Arin 等，2015）。


To check the sensitivity of our results to model specifications, we adopted Bayesian model averaging (BMA)—a systematic framework that allows us to incorporate both parameter and model uncertainty into the estimation (Arin et al., 2015; Montgomery & Nyhan, 2010). BMA represents the data as a hierarchical mixture model and assigns a prior distribution to the model parameters as well as the models.<sup>9</sup> Specifically, it explores the entire model space spanned by every possible combination of a variable set (in our case, 11 independent variables yield $2 ^ { 1 1 } = 2 { , } 0 4 8$ models) and estimates the expected value for the coefficients by averaging them across the model space. From the marginal distribution of the mixture model, the posterior probability of a given model $( M _ { i } )$ is derived as Equation (3):




为了检查我们的结果对模型规范的敏感性，我们采用了贝叶斯模型平均（BMA）——一个系统框架，允许我们将参数和模型不确定性纳入估计中（Arin 等人，2015 年；Montgomery 和 Nyhan，2010 年）。 BMA 将数据表示为分层混合模型，并将先验分布分配给模型参数和模型。<sup>9</sup>具体来说，它探索变量集的每种可能组合所跨越的整个模型空间（在我们的示例中，11 个自变量产生 $2 ^ { 1 1 } = 2 { , } 0 4 8$ 模型），并通过在整个模型空间中对系数进行平均来估计系数的预期值。根据混合模型的边际分布，可以得出给定模型 $( M _ { i } )$ 的后验概率，如方程 (3) 所示：


$$
P (M _ {i} | Y) \propto P (Y | M _ {i}) P (M _ {i})\tag{3}
$$




$$
P (M _ {i} | Y) \propto P (Y | M _ {i}) P (M _ {i})\tag{3}
$$


Using the posterior model probabilities as weight factors, we can derive the expected value of a given coefficient (??) by taking the weighted average of the expected values of the coefficient across the model space as Equation (4):




使用后验模型概率作为权重因子，我们可以通过模型空间中系数期望值的加权平均值得出给定系数的期望值（??），如方程（4）所示：


$$
E (\beta | Y) = \sum_ {i = 1} ^ {2 ^ {k}} E (\beta_ {i} | M _ {i}, Y) P (M _ {i} | Y)\tag{4}
$$




$$
E (\beta | Y) = \sum_ {i = 1} ^ {2 ^ {k}} E (\beta_ {i} | M _ {i}, Y) P (M _ {i} | Y)\tag{4}
$$


Figure 2 illustrates a mixture of the posterior distributions of IT distance across the model space, conditional on the inclusion of IT distance. The solid vertical line is the median of the posterior distribution. The dotted vertical lines represent the 95% credible interval (ranging from -0.066 to -0.005). The posterior distribution clearly leans toward the negative area, and the 95% credible interval does not include 0. These BMA results suggest that after accounting for model uncertainty, the effect of IT distance on post-acquisition performance is still significant, thereby lending further credence to our results.




图 2 说明了模型空间中 IT 距离的后验分布的混合，以包含 IT 距离为条件。垂直实线是后验分布的中值。垂直虚线代表 95% 可信区间（范围从 -0.066 到 -0.005）。后验分布明显偏向负值区域，并且 95% 可信区间不包括 0。这些 BMA 结果表明，在考虑模型不确定性后，IT 距离对收购后绩效的影响仍然显着，从而进一步证实了我们的结果。


## Variable Definitions




## 变量定义


We considered alternative definitions of acquisition motivation—whether an acquisition is motivated by operational synergy or not. The current definition pertains only to those deals whose motivation strictly relates to operational synergy. We relaxed this definition to include those deals in which operational synergy, albeit not primarily, is considered to some extent. Specifically, we included deals motivated by restructuring and market expansion. The results reported in Table A4 are consistent with our main findings.




我们考虑了收购动机的其他定义——收购是否是出于运营协同效应的动机。当前的定义仅适用于其动机与运营协同效应严格相关的交易。我们放宽了这一定义，将那些在某种程度上考虑了运营协同效应（尽管不是主要因素）的交易纳入其中。具体来说，我们包括了由重组和市场扩张推动的交易。表 A4 中报告的结果与我们的主要发现一致。


![](/api/attachments/EQEMG87U/fulltext/images/beaf080bb09bd89ade11720e45a7dc2023c2dc260b0df59f0715d9ed31f7771a.jpg)  
Figure 2. Conditional Posterior Distribution of IT Distance from Bayesian Model Averaging




![](/api/attachments/EQEMG87U/fulltext/images/beaf080bb09bd89ade11720e45a7dc2023c2dc260b0df59f0715d9ed31f7771a.jpg)  
图 2. 贝叶斯模型平均的 IT 距离的条件后验分布


In addition, we considered the possibility that the number of components used to estimate IT distance might affect the findings. Specifically, while our IT distance measure considers all six enterprise systems components, not all pairs of the acquirer and target in our sample had all six components prior to the acquisition. In our sample, each pair of acquirer and target firms had at least two components available in both companies. If some components were not available, those missing components were ignored when calculating the average IT distance of the individual components. If the number of components were somehow correlated with the IT distance, then it might affect our results. To examine this possibility, we estimated the main model with four subsamples: pairs with three or more components, pairs with four or more, pairs with five or more, and pairs with all six components. As reported in Table A5, the results are consistent across the subsamples.




此外，我们还考虑了用于估计 IT 距离的组件数量可能会影响结果的可能性。具体来说，虽然我们的 IT 距离度量考虑了所有六个企业系统组件，但并非样本中的所有收购方和目标对在收购之前都拥有所有六个组件。在我们的样本中，每对收购方和目标公司都至少有两个可用的组件。如果某些组件不可用，则在计算各个组件的平均 IT 距离时将忽略那些缺失的组件。如果组件的数量与 IT 距离存在某种相关性，那么它可能会影响我们的结果。为了检查这种可能性，我们用四个子样本估计了主模型：具有三个或更多组件的对，具有四个或更多组件的对，具有五个或更多组件的对，以及具有所有六个组件的对。如表 A5 所示，子样本的结果是一致的。


## Outliers




## 异常值


To examine whether our findings were influenced by potential outliers, we winsorized the dependent variables at the fifth and 95th percentiles by replacing values smaller than the fifth percentile with the fifth percentile, and values greater than the 95th percentile with the 95th percentile. The results reported in Table A6 are again consistent with the previous findings.




为了检查我们的研究结果是否受到潜在异常值的影响，我们对第 5 个和第 95 个百分位数的因变量进行了缩尾处理，方法是将小于第 5 个百分位数的值替换为第 5 个百分位数，将大于第 95 个百分位数的值替换为第 95 个百分位数。表 A6 中报告的结果再次与之前的发现一致。


## Validation of the Co-occurrence Assumption




## 同现假设的验证


The IT distance measure is valid only to the extent that the underlying assumption is true: a set of technologies are compatible if they are frequently adopted together within a firm. This assumption, while reasonable, might be strong. For instance, local business units might pick vendors without considering the overall compatibility with the other business units. In such cases, the co-occurrence of vendors would not imply system compatibility.




IT 距离度量仅在基本假设成立的情况下才有效：如果一组技术在公司内经常一起采用，则它们是兼容的。这个假设虽然合理，但可能是强有力的。例如，本地业务部门可能会选择供应商，而不考虑与其他业务部门的整体兼容性。在这种情况下，供应商的共存并不意味着系统兼容性。


To test the validity of our assumption, we devised a set of scenarios where the degree of the relationship between cooccurrence and compatibility can vary. If the co-occurrence assumption is not valid, the IT distance should not vary across these scenarios; however, if the assumption is valid, the IT distance would be greater (smaller) in scenarios where the relationship is stronger (weaker). Two such scenarios are considered.




为了测试我们假设的有效性，我们设计了一组场景，其中共现和兼容性之间的关系程度可以变化。如果同现假设无效，则 IT 距离在这些场景中不应变化；然而，如果假设成立，则在关系较强（较弱）的情况下，IT 距离会更大（更小）。考虑两种这样的场景。


IT distance and recent acquisitions: The technologies used by the target prior to the acquisition may be less compatible with those of the acquiring firm because they were not chosen by the acquiring firm. Given this possibility, the relationship between co-occurrence and compatibility within a firm would become weaker as the firm goes through more acquisitions. To the extent that this is true, a firm with more recent acquisitions would be using a set of technologies that are less compatible with one another, compared to other comparable firms with fewer acquisitions. Therefore, the IT distance in the former should be greater than that in the latter.




IT距离和最近的收购：收购前目标公司使用的技术可能与收购公司的技术不太兼容，因为这些技术不是收购公司选择的。鉴于这种可能性，随着公司进行更多的收购，公司内部的共现和兼容性之间的关系将变得更弱。如果确实如此，那么与收购次数较少的其他类似公司相比，最近进行收购的公司将使用一系列彼此兼容性较差的技术。因此，前者的IT距离应大于后者。


IT distance and decentralized IT governance: The technologies within firms whose IT decision is decentralized (made by local business units) may be less compatible, compared to firms where IT decisions are centralized (made by headquarters). Therefore, the relationship between cooccurrence and compatibility would be weaker under a greater level of decentralization. To the extent that this is true, a firm with decentralized IT governance would be using a set of technologies that are less compatible, compared to other similar firms with centralized IT governance. If our IT distance measure indeed captures the degree of incompatibility, the IT distance would be greater for firms with decentralized IT governance than for those with centralized governance.




IT 距离和分散式 IT 治理：与 IT 决策集中化（由总部制定）的公司相比，分散式 IT 决策（由本地业务部门制定）的公司内部技术的兼容性可能较差。因此，在更高水平的去中心化下，共现和相容之间的关系会更弱。如果确实如此，与其他具有集中式 IT 治理的类似公司相比，具有分散式 IT 治理的公司将使用一组兼容性较差的技术。如果我们的 IT 距离测量确实反映了不兼容的程度，那么采用分散式 IT 治理的公司的 IT 距离将比采用集中式治理的公司更大。


To test our assumption under the two scenarios, we first estimated the acquirer’s within-IT distance at the time of a deal announcement. Specifically, we measured the distance between each pair of vendors adopted by the sites of a given acquirer and averaged all the distances. Suppose there is a firm that uses eight different vendors across its sites. The eight vendors would result in 64 pairs, and the firm’s IT distance would be the average of the distances of the 64 pairs. In a special case where a firm uses the same vendor across all sites, the IT distance would be 0.




为了测试我们在两种情况下的假设，我们首先估计了收购方在交易公告时的 IT 距离。具体来说，我们测量了给定收单方站点采用的每对供应商之间的距离，并对所有距离进行平均。假设有一家公司在其站点上使用八个不同的供应商。八家供应商将产生 64 对，公司的 IT 距离将是 64 对距离的平均值。在公司的所有站点都使用同一供应商的特殊情况下，IT 距离将为 0。


Then, we regressed the acquirer’s IT distance on (1) the number of past acquisitions, and (2) IT decentralization. The measure for IT decentralization is derived from Xue et al. (2011), who use the same database (CITDB). Specifically, in the database, each establishment has information regarding where IT purchase decisions are made, which can be either “Local” or “Parent.” Following Xue et al. (2011), we measured IT decentralization as the percentage of business units whose purchase decision is “Local” for each firm. As shown in Table A7, both the past acquisition and IT decentralization have positive and significant coefficients, indicating that IT distance increases when firms have a larger number of recent acquisitions, and their IT decisions are made more locally. These findings support our co-occurrence assumption.




然后，我们对收购方的 IT 距离进行了回归：(1) 过去收购的数量，以及 (2) IT 分散化。 IT去中心化的衡量标准源自Xue等人。 （2011），他们使用相同的数据库（CITDB）。具体来说，在数据库中，每个机构都有有关 IT 购买决策的信息，可以是“本地”或“母公司”。继薛等人之后。 (2011)，我们将 IT 权力下放衡量为每家公司购买决策为“本地”的业务部门的百分比。如表 A7 所示，过去的收购和 IT 分散化都具有正且显着的系数，表明当企业近期收购数量较多时，IT 距离会增加，并且其 IT 决策更多地在本地做出。这些发现支持我们的共现假设。


## Unequal Weight Distribution of the IT Module




## IT模块权重分配不均


We operationalized IT distance as the equal-weight average of the six modules’ IT distance, each of which is estimated independently. This approach is based on the codependency of IT systems—one cannot function without the others (Milgrom & Roberts, 1990)—and has been used by prior studies conceptualizing IT systems and IT capabilities (Mehta & Hirschheim, 2007; Tanriverdi, 2006; Tanriverdi & Uysal,




我们将 IT 距离操作为六个模块 IT 距离的等权平均值，每个模块都是独立估计的。这种方法基于 IT 系统的相互依赖性——一个系统的运行离不开其他系统（Milgrom & Roberts, 1990）——并且已被先前概念化 IT 系统和 IT 能力的研究所使用（Mehta & Hirschheim, 2007；Tanriverdi, 2006；Tanriverdi & Uysal,


2011). However, it is possible that each module’s contribution to IT distance might be disproportionate; for instance, the SCM module may create an incompatibility issue more than the CRM module does. Although we do not have a theoretical basis to make a priori predictions regarding which modules contribute more (or less) to the overall incompatibility, we tested the sensitivity of our findings by assigning an unequal weight (200%) to one of the six modules and the equal weight (100%) to the rest. We further complemented this analysis with experts’ opinions. During the survey conducted for IT distance validation, participants were also asked to rank the modules in terms of the relative impact of their integration on a firm’s financial performance. Based on the average rank from the survey, each module was given a weight between 0 and 1, which was in turn used to calculate the weighted IT distance. The results shown in Table A8 are consistent across the weight distributions, indicating that our results are not sensitive to the modules’ weights.




2011）。然而，每个模块对 IT 距离的贡献可能不成比例；例如，SCM 模块可能比 CRM 模块更容易产生不兼容性问题。尽管我们没有理论基础来对哪些模块对整体不兼容性的贡献更大（或更少）做出先验预测，但我们通过为六个模块之一分配不等的权重（200％）并为其余模块分配相等的权重（100％）来测试我们的研究结果的敏感性。我们进一步补充了专家意见的分析。在针对 IT 距离验证进行的调查期间，参与者还被要求根据模块集成对公司财务绩效的相对影响对模块进行排名。根据调查的平均排名，每个模块都被赋予 0 到 1 之间的权重，该权重又用于计算加权 IT 距离。表 A8 中显示的结果在权重分布上是一致的，表明我们的结果对模块的权重不敏感。


## Discussion and Conclusion




## 讨论与结论


This study contributes to the theory in the broader M&A literature, as well as the IS literature by conceptualizing IT distance and theorizing its role in value creation in acquisitions. The M&A literature has long examined how dyadic differences create or destroy the synergy potential in acquisitions from various perspectives on organizational differences (Graebner et al., 2017), except for IT. Despite the strong relevance of IT to the realization of acquisition synergies, the IT aspect of organizational difference has rarely been recognized in the IS literature. This study presents IT distance—the difference in IT systems—as another critical aspect of organizational differences and explicates the mechanisms through which it diminishes an acquisition’s synergy potential.




本研究通过概念化 IT 距离并理论化其在收购中价值创造中的作用，为更广泛的并购文献以及信息系统文献中的理论做出了贡献。并购文献长期以来一直从组织差异的不同角度研究二元差异如何创造或破坏收购中的协同潜力（Graebner 等，2017），IT 除外。尽管 IT 与实现收购协同效应密切相关，但 IT 方面的组织差异却很少在 IS 文献中得到认可。这项研究将 IT 距离（IT 系统的差异）视为组织差异的另一个关键方面，并阐明了 IT 距离削弱收购协同潜力的机制。


In the nascent research stream examining IT and acquisitions, conversations have been confined to decisions and outcomes involved in the IT integration process (Henningsson & Kettinger, 2016; Jain & Ramesh, 2015; Kovela & Skok, 2012) and have rarely been extended to the value-creation mechanism in acquisitions (Tanriverdi & Uysal, 2011). The lacking evidence of clear performance implications makes it difficult to contend the relevance of IT in acquisition decisions (Benitez et al., 2018; Tanriverdi & Uysal, 2011, 2015). This study is among the first to establish a link between IT and acquisition outcomes by proposing the concept of IT distance and theorizing how it influences the costs involved in integrating disparate IT systems to resolve such incompatibility. Our paper demonstrates that IT distance has significant performance implications, underscoring the value of the ability to predict this IT risk beforehand. Acquirers should consider IT distance early in the decision process so that they can filter out target firms whose synergetic potential is great but unlikely to materialize due to IT distance. By allowing firms to account for IT-related potential disruptions in advance, IT distance can help them assess a more realistic value of a deal and achieve better outcomes.




在审视 IT 和收购的新兴研究流中，对话仅限于 IT 集成过程中涉及的决策和结果（Henningsson & Kettinger，2016；Jain & Ramesh，2015；Kovela & Skok，2012），很少扩展到收购中的价值创造机制（Tanriverdi & Uysal，2011）。由于缺乏明确绩效影响的证据，因此很难争论 IT 在收购决策中的相关性（Benitez 等，2018；Tanriverdi & Uysal，2011，2015）。这项研究首次提出了 IT 距离的概念，并理论化了 IT 距离如何影响集成不同 IT 系统以解决这种不兼容性所涉及的成本，从而在 IT 和采购结果之间建立了联系。我们的论文表明，IT 距离具有显着的性能影响，强调了提前预测此 IT 风险的能力的价值。收购方应在决策过程中尽早考虑IT距离，以便筛选出协同潜力巨大但由于IT距离而难以实现的目标公司。通过允许公司提前考虑与 IT 相关的潜在中断，IT 距离可以帮助他们评估更现实的交易价值并取得更好的结果。


Also, most prior work examines “IT fit” in the context of business-IT alignment (Baker & Niederman, 2014; Mehta & Hirschheim, 2007; Wijnhoven et al., 2006), which substantially differs from the IT fit captured by IT distance. The incompatibility or misalignment between IT systems is rarely proposed as a prominent construct or linked to post-acquisition performance. Our study proposes a research model and measure for this novel construct, thereby expanding our understanding of the (mis)alignment of IT systems between organizations (e.g., acquirer and target firms in the context of M&As).




此外，大多数先前的工作都是在业务与 IT 一致性的背景下检验“IT 契合度”（Baker & Niederman，2014 年；Mehta & Hirschheim，2007 年；Wijnhoven 等人，2006 年），这与 IT 距离捕获的 IT 契合度有很大不同。 IT 系统之间的不兼容或不一致很少被认为是一个突出的结构，也很少被认为与收购后的绩效相关。我们的研究为这种新颖的结构提出了一个研究模型和衡量标准，从而扩大了我们对组织之间 IT 系统（例如并购背景下的收购方和目标公司）之间 IT 系统（错误）协调的理解。


Another contribution of our study involves identifying a contingent factor influencing the extent to which IT distance affects post-acquisition performance. The literature suggests that the type of synergy sought by an acquisition is a primary determinant of the required level of organizational integration because it determines how much synergy creation depends on establishing new interdependencies in the value chain (Pablo, 1994). The findings demonstrate that the effect of IT distance is significantly influenced by the strategic acquisition motivation. This also serves as a validity check for our research model on IT distance by identifying a theory-driven boundary condition for when IT distance does and does not matter.




我们研究的另一个贡献是确定了一个影响 IT 距离对收购后绩效影响程度的偶然因素。文献表明，收购所寻求的协同效应类型是所需组织整合水平的主要决定因素，因为它决定了协同效应的产生在多大程度上取决于在价值链中建立新的相互依赖关系（Pablo，1994）。研究结果表明，IT 距离的影响很大程度上受到战略收购动机的影响。通过确定 IT 距离何时重要和不重要的理论驱动边界条件，这也可以作为我们关于 IT 距离研究模型的有效性检查。


This study also makes a methodological contribution by introducing a novel way of estimating system compatibility. Measuring compatibility is challenging due to interoperability—systems that are natively incompatible can work together through translators. Therefore, it requires an indepth study of system configurations and user experiences to directly measure the degree of compatibility. Obviously, this method is neither practical nor scalable, which may explain the limited amount of related empirical research (Henningsson et al., 2018). To overcome these challenges, we adopted a wordembedding technique (Word2Vec) wherein the proximity among words is estimated based on the co-occurrence of words within a corpus. The notion of system compatibility is nothing new; yet its efficacy has never been validated in a large-scale setting due to the lack of data and the methodology used to measure the construct in a way that is aligned with its conceptualization. The proposed approach can measure systems compatibility based on the assumption drawn from its conceptualization and can fully utilize large-scale data. This is a significant methodological advance not only for the M&A literature in IS, but also for the IS literature examining the business value of IT infrastructure (Tilson et al., 2010).




这项研究还通过引入一种估计系统兼容性的新方法做出了方法论贡献。由于互操作性，测量兼容性具有挑战性——本来不兼容的系统可以通过转换器协同工作。因此，需要深入研究系统配置和用户体验来直接衡量兼容程度。显然，这种方法既不实用，也不具有可扩展性，这也许可以解释相关实证研究数量有限的原因（Henningsson et al., 2018）。为了克服这些挑战，我们采用了词嵌入技术（Word2Vec），其中根据语料库中单词的共现来估计单词之间的接近度。系统兼容性的概念并不是什么新鲜事。然而，由于缺乏数据和用于以与其概念化相一致的方式衡量构造的方法，其功效从未在大规模环境中得到验证。所提出的方法可以基于其概念化的假设来测量系统兼容性，并且可以充分利用大规模数据。这不仅对于 IS 领域的并购文献而言是一个重大的方法论进步，对于检查 IT 基础设施商业价值的 IS 文献来说也是如此（Tilson 等，2010）。


Moreover, this technique is applicable to other research contexts where researchers want to measure the similarity/dissimilarity between any entities based on nonnumeric attributes, the distance between which is a priori unknown. Unlike numeric attributes where the differences between adjacent values are equidistant, non-numeric attributes contain categorical values that, in and of themselves, reveal nothing about how close or distant they are. Leveraging the co-occurrence assumption, the proposed technique feeds this necessary information to the coded similarity/dissimilarity between categorical values. There could be numerous applications in the IS and management fields, including industry relatedness (based on the cooccurrence of the industry codes in which a firm operates), technological knowledge distance (based on the cooccurrence of the patent classes within a firm), and job similarity (based on the co-occurrence of specific job descriptions within a resume).




此外，该技术适用于其他研究环境，在这些环境中，研究人员想要测量基于非数字属性的任何实体之间的相似性/不相似性，而实体之间的距离是先验未知的。与相邻值之间的差异是等距的数字属性不同，非数字属性包含分类值，这些值本身并不能揭示它们的远近程度。利用共现假设，所提出的技术将这些必要的信息提供给分类值之间的编码相似性/相异性。在信息系统和管理领域可能有很多应用，包括行业相关性（基于公司运营的行业代码的共现）、技术知识距离（基于公司内专利类别的共现）和工作相似性（基于简历中特定职位描述的共现）。


Our approach to measuring IT distance is innovative from a research standpoint, but also bears a unique practical merit in that it solely relies on publicly available (albeit proprietary) information. Firms looking to make an acquisition can benefit from using our approach to gauge the IT risks associated with potential targets, even before engaging in the due diligence process for a specific target. Typically, a target’s detailed system specifications are only shared during the due diligence phase, and an acquirer can afford to consider only a few final candidates due to costs while leaving out potentially more suitable candidates in terms of IT synergies. Therefore, the ability to assess the IT risks of potential targets based on a commercially available dataset can be valuable to practitioners.




从研究的角度来看，我们测量 IT 距离的方法是创新的，但也具有独特的实际优点，因为它仅依赖于公开可用的（尽管是专有的）信息。寻求收购的公司可以受益于使用我们的方法来评估与潜在目标相关的 IT 风险，甚至在对特定目标进行尽职调查之前也是如此。通常情况下，目标公司的详细系统规格仅在尽职调查阶段共享，收购方出于成本考虑只能考虑少数最终候选者，而在 IT 协同效应方面可能会遗漏更合适的候选者。因此，基于商用数据集评估潜在目标的 IT 风险的能力对于从业者来说非常有价值。


Although this study focuses on the context of M&As, the concept of IT distance is also applicable to other contexts where coordination through IT systems is important. An interesting extension of this study, for example, would be in the context of strategic alliances. In such a context, many partnering firms exchange information/knowledge and coordinate tasks across organizational boundaries, while each of them has only limited and shared control over a subset of the partners’ IT systems. With its unique organizational setting, a strategic alliance has many possibilities that could lead to interesting theoretical and practical implications, which would be a fruitful venue for future research.<sup>10</sup> Moreover, some other types of intra- or interorganizational coordination, such as multibusiness units within an organization and virtually integrated supply chain models, would also be interesting contexts to investigate.




尽管本研究重点关注并购背景，但 IT 距离概念也适用于通过 IT 系统进行协调很重要的其他背景。例如，这项研究的一个有趣的扩展是在战略联盟的背景下。在这样的背景下，许多合作伙伴公司跨组织边界交换信息/知识并协调任务，而每个公司对合作伙伴 IT 系统的子集只有有限的共享控制权。凭借其独特的组织环境，战略联盟具有多种可能性，可以带来有趣的理论和实践影响，这将是未来研究的富有成果的场所。<sup>10</sup>此外，一些其他类型的组织内或组织间协调，例如组织内的多业务部门和几乎集成的供应链模型，也将是值得研究的有趣背景。


This study is not without limitations. First, our sample is restricted by the data availability of the CITDB survey, and thus might differ from companies randomly sampled from the population. Although such a selection issue is not uncommon in social science research (wherein the focal measures dictate a sample space), one needs to exercise caution in generalizing our findings. Second, it should be noted that our study examines the period 2007-2013, which was chosen to obtain the most comprehensive IT distance measure comparable across the longest period possible (given that CITDB had occasionally changed its survey instruments). During this period, however, companies might have experienced some irregularities in business due to the financial crisis of 2007. Although there is little reason to believe that such an external shock could alter the internal mechanism of how IT distance hinders a firm’s integration and coordination capabilities, further research with a broader sample period range is needed to strengthen the generalizability of our findings. Lastly, the effect of IT distance might be heterogeneous because firms with the same level of IT distance might incur differential integration costs due to their differences in other firm resources and practices. Although it is beyond the scope of our study, we believe that uncovering firm-specific factors that can influence how IT distance affects post-acquisition integration and performance will be an interesting avenue for future research.<sup>11</sup>




这项研究并非没有局限性。首先，我们的样本受到 CITDB 调查数据可用性的限制，因此可能与从总体中随机抽样的公司有所不同。尽管这样的选择问题在社会科学研究中并不罕见（其中焦点指标决定了样本空间），但在概括我们的研究结果时需要谨慎行事。其次，值得注意的是，我们的研究考察了 2007 年至 2013 年期间，选择这一时期是为了获得尽可能长的时期内可比较的最全面的 IT 距离衡量标准（考虑到 CITDB 偶尔会改变其调查工具）。然而，在此期间，由于2007年的金融危机，企业可能会出现一些业务上的异常情况。尽管没有理由相信这种外部冲击会改变IT距离阻碍企业整合和协调能力的内部机制，但仍需要在更广泛的样本时期范围内进行进一步研究，以加强我们研究结果的普遍性。最后，IT距离的影响可能是异质的，因为具有相同IT距离水平的公司可能由于其他公司资源和实践的差异而产生不同的整合成本。尽管这超出了我们的研究范围，但我们相信，揭示能够影响 IT 距离如何影响收购后整合和绩效的公司特定因素将是未来研究的一个有趣途径。<sup>11</sup>


To conclude, this study introduced a novel concept of IT distance, capturing the dissimilarities between the acquirer’s and target’s enterprise systems. We demonstrated that IT distance significantly undermines post-acquisition performance. This finding supports our theoretical argument that IT distance creates serious obstacles to post-acquisition integration and impedes acquisition synergies. Our conceptualization, theoretical framework, and empirical findings shed new light on the critical role of IT (especially enterprise systems) in the context of acquisitions. They also provide valuable insights for managers in terms of why it is imperative to consider IT when conducting due diligence and making decisions involved in their acquisitions, and how they should devise an IT strategy to improve postacquisition performance.




总之，本研究引入了 IT 距离的新概念，捕捉收购方和目标企业系统之间的差异。我们证明，IT 距离会严重影响收购后的绩效。这一发现支持了我们的理论论点，即 IT 距离对收购后整合造成了严重障碍，并阻碍了收购协同效应。我们的概念、理论框架和实证研究结果为 IT（尤其是企业系统）在收购中的关键作用提供了新的视角。他们还为管理者提供了宝贵的见解，说明为什么在进行尽职调查和制定收购相关决策时必须考虑 IT，以及他们应如何制定 IT 战略来提高收购后绩效。


## Acknowledgments




## 致谢


We gratefully acknowledge financial support from the Social Science and Humanities Research Council of Canada (SSHRC). Grant [435-2018-0605].




我们衷心感谢加拿大社会科学和人文研究委员会 (SSHRC) 的财政支持。格兰特[435-2018-0605]。


## References




＃＃ 参考


Abadie, A. (2021). Using synthetic controls: feasibility, data requirements, and methodological aspects. Journal of Economic Literature, 59(2), 391-425.




阿巴迪，A.（2021）。使用综合控制：可行性、数据要求和方法方面。经济文献杂志，59(2), 391-425。


Ahuja, G., & Katila, R. (2001). Technological acquisitions and the innovation performance of acquiring firms: A longitudinal study. Strategic Management Journal, 22(3), 197–220.




Ahuja, G. 和 Katila, R. (2001)。技术收购和收购公司的创新绩效：纵向研究。战略管理杂志，22（3），197-220。


Akella, J., Buckow, H., & Rey, S. (2009). IT architecture: Cutting costs and complexity. McKinsey Digital. http://www.mckinsey.com/business-functions/digitalmckinsey/our-insights/it-architecture-cutting-costs-andcomplexity




Akella, J.、Buckow, H. 和 Rey, S. (2009)。 IT 架构：降低成本和复杂性。麦肯锡数字。 http://www.mckinsey.com/business-functions/digitalmckinsey/our-insights/it-architecture-cutting-costs-andcomplexity


Angwin, D. (2004). Speed in M&A integration: The first 100 days. European Management Journal, 22(4), 418–430.




安格温，D.（2004）。并购整合速度：前 100 天。欧洲管理杂志，22(4), 418–430。


Arin, K. P., Huang, V. Z., Minniti, M., Nandialath, A. M., & Reich, O. F. M. (2015). Revisiting the determinants of entrepreneurship. Journal of Management, 41(2), 607–631.




Arin, K. P.、Huang, V. Z.、Minniti, M.、Nandialath, A. M. 和 Reich, O. F. M. (2015)。重新审视创业的决定因素。管理杂志，41（2），607-631。


Baker, E. W., & Niederman, F. (2014). Integrating the IS functions after mergers and acquisitions: Analyzing business-IT alignment. Journal of Strategic Information Systems, 23(2), 112-127.




贝克，E.W. 和尼德曼，F. (2014)。并购后整合 IS 功能：分析业务与 IT 的一致性。战略信息系统杂志，23(2), 112-127。


Banker, R. D., Davis, G. B., & Slaughter, S. A. (1998). Software development practices, software complexity, and software maintenance performance: A field study. Management Science, 44(4), 433-450.




Banker, R. D.、Davis, G. B. 和 Slaughter, S. A. (1998)。软件开发实践、软件复杂性和软件维护性能：现场研究。管理科学，44(4), 433-450。


Barber, B. M., & Lyon, J. D. (1996). Detecting abnormal operating performance: The empirical power and specification of test statistics. Journal of Financial Economics, 41(3), 359-399.




巴伯，B.M. 和里昂，J.D. (1996)。检测异常运行性能：检验统计的经验力量和规范。金融经济学杂志，41(3), 359-399。


Barki, H., & Pinsonneault, A. (2005). A model of organizational integration, implementation effort, and performance. Organization Science, 16(2), 165-179.




Barki, H. 和 Pinsonneault, A. (2005)。组织整合、实施工作和绩效的模型。组织科学，16(2), 165-179。


Bauer, F., & Matzler, K. (2014). Antecedents of M&A success: The role of strategic complementarity, cultural fit, and degree and speed of integration. Strategic Management Journal, 35(2), 269-291.




鲍尔，F. 和马茨勒，K. (2014)。并购成功的因素：战略互补性、文化契合度以及整合程度和速度的作用。战略管理杂志，35(2), 269-291。


Benitez, J., Ray, G., & Henseler, J. (2018). Impact of information technology infrastructure flexibility on mergers and acquisitions. MIS Quarterly, 42(1), 25-43.




贝尼特斯，J.，雷，G.，＆亨塞勒，J.（2018）。信息技术基础设施灵活性对并购的影响。 《管理信息系统季刊》，42(1)，25-43。


Bharadwaj, A. S. (2000). A resource-based perspective on information technology capability and firm performance: An empirical investigation. MIS Quarterly, 24(1), 169-196.




巴拉德瓦吉，A.S. (2000)。关于信息技术能力和公司绩效的基于资源的视角：实证调查。 《管理信息系统季刊》，24(1)，169-196。


Campbell, D. J. (1988). Task complexity: A review and analysis. Academy of Management Review, 13(1), 40-52.




坎贝尔，D.J. (1988)。任务复杂性：回顾和分析。管理学院评论，13(1), 40-52。


Capron, L. (1999). The long-term performance of horizontal acquisitions. Strategic Management Journal, 20(11), 987- 1018.




卡普伦，L.（1999）。横向收购的长期绩效。战略管理杂志，20（11），987-1018。


Chatterjee, S. (1986). Types of synergy and economic value: The impact of acquisitions on merging and rival firms. Strategic Management Journal, 7(2), 119-139.




查特吉，S.（1986）。协同效应和经济价值的类型：收购对合并和竞争对手公司的影响。战略管理杂志，7(2), 119-139。


Chatterjee, S. (1992). Sources of value in takeovers: Synergy or restructuring: Implications for target and bidder firms. Strategic Management Journal, 13(4), 267-286.




查特吉，S.（1992）。收购中的价值来源：协同或重组：对目标公司和投标公司的影响。战略管理杂志，13(4), 267-286。


Chellappa, R. K., Sambamurthy, V., & Saraf, N. (2010). Competing in crowded markets: Multimarket contact and the nature of competition in the enterprise systems software industry. Information Systems Research, 21(3), 614-630.




Chellappa, R.K.、Sambamurthy, V. 和 Saraf, N. (2010)。在拥挤的市场中竞争：多市场接触和企业系统软件行业竞争的本质。信息系统研究，21(3), 614-630。


Chellappa, R. K., & Saraf, N. (2010). Alliances, rivalry, and firm performance in enterprise systems software markets: A social network approach. Information Systems Research, 21(4), 849- 871.




Chellappa, R.K. 和 Saraf, N. (2010)。企业系统软件市场中的联盟、竞争和公司绩效：社交网络方法。信息系统研究，21（4），849-871。


Cording, M., Christmann, P., & King, D. R. (2008). Reducing causal ambiguity in acquisition integration: intermediate goals as mediators of integration decisions and acquisition performance. Academy of Management Journal, 51(4), 744- 767.




Cording, M.、Christmann, P. 和 King, D. R. (2008)。减少收购整合中的因果模糊性：中间目标作为整合决策和收购绩效的中介。管理学会杂志，51（4），744-767。


Darcy, D. P., Kemerer, C. F., Slaughter, S. A., & Tomayko, J. E. (2005). The structural complexity of software an experimental test. IEEE Transactions on Software Engineering, 31(11), 982- 995.




Darcy, D. P.、Kemerer, C. F.、Slaughter, S. A. 和 Tomayko, J. E. (2005)。软件结构复杂性的实验测试。 IEEE 软件工程汇刊，31(11), 982-995。


Datta, D. K. (1991). Organizational fit and acquisition performance: Effects of post‐acquisition integration. Strategic Management Journal, 12(4), 281-297.




达塔，D.K. (1991)。组织契合度和收购绩效：收购后整合的影响。战略管理杂志，12(4), 281-297。


Dean, J. W., Yoon, S. J., & Susman, G. I. (1992). Advanced manufacturing technology and organization structure: empowerment or subordination? Organization Science, 3(2), 203-229.




Dean, J. W.、Yoon, S. J. 和 Susman, G. I. (1992)。先进制造技术和组织结构：授权还是从属？组织科学，3(2), 203-229。


Dehejia, R. H., & Wahba, S. (1999). Causal effects in nonexperimental studies: reevaluating the evaluation of training programs. Journal of the American Statistical Association, 94(448), 1053-1062.




Dehejia, R. H. 和 Wahba, S. (1999)。非实验研究中的因果效应：重新评估培训计划的评估。美国统计协会杂志，94(448)，1053-1062。


Espinosa, J. A., Slaughter, S. A., Kraut, R. E., & Herbsleb, J. D. (2007). Familiarity, complexity, and team performance in geographically distributed software development. Organization Science, 18(4), 613-630.




Espinosa, J. A.、Slaughter, S. A.、Kraut, R. E. 和 Herbsleb, J. D. (2007)。地理分布式软件开发的熟悉程度、复杂性和团队绩效。组织科学，18(4), 613-630。


Fee, C. E., & Thomas, S. (2004). Sources of gains in horizontal mergers: Evidence from customer, supplier, and rival firms. Journal of Financial Economics, 74(3), 423-460.




Fee, C. E. 和 Thomas, S. (2004)。横向合并的收益来源：来自客户、供应商和竞争对手公司的证据。金融经济学杂志，74(3), 423-460。


Gobillon, L., & Magnac, T. (2016). Regional policy evaluation: Interactive fixed effects and synthetic controls. The Review of Economics and Statistics, 98(3), 535-551.




Gobillon, L. 和 Magnac, T. (2016)。区域政策评估：互动固定效应和综合控制。经济与统计评论，98(3), 535-551。


Gosain, S., Malhotra, A., & El Sawy, O. A. (2004). Coordinating for flexibility in e-business supply chains. Journal of Management Information Systems, 21(3), 7-45.




Gosain, S.、Malhotra, A. 和 El Sawy, O. A. (2004)。协调电子商务供应链的灵活性。管理信息系统杂志，21(3), 7-45。


Graebner, M. E., Heimeriks, K. H., Huy, Q. N., & Vaara, E. (2017). The process of postmerger integration: A review and agenda for future research. The Academy of Management Annals, 11(1), 1-32.




Graebner, M. E.、Heimeriks, K. H.、Huy, Q. N. 和 Vaara, E. (2017)。并购后整合的过程：未来研究的回顾和议程。 《管理学院年鉴》，11(1), 1-32。


Grinstein, Y., & Hribar, P. (2004). CEO compensation and incentives: Evidence from M&A bonuses. Journal of Financial Economics, 73(1), 119-143.




Grinstein, Y. 和 Hribar, P. (2004)。首席执行官薪酬和激励：来自并购奖金的证据。金融经济学杂志，73(1), 119-143。


Harrell, H. W., & Higgins, L. (2002). IS integration: Your most critical M&A challenge? Journal of Corporate Accounting & Finance, 13(2), 23. https://doi.org/10.1002/jcaf.1220




哈雷尔，H.W.，＆希金斯，L.（2002）。 IS 整合：您最严峻的并购挑战？ 《企业会计与金融杂志》，13(2), 23。https://doi.org/10.1002/jcaf.1220


Healy, P. M., Palepu, K. G., & Ruback, R. S. (1992). Does corporate performance improve after mergers? Journal of Financial Economics, 31(2), 135-175.




Healy, P. M.、Palepu, K. G. 和 Ruback, R. S. (1992)。合并后企业业绩是否有所改善？金融经济学杂志，31(2), 135-175。


Henningsson, S., & Kettinger, W. J. (2016). Understanding information systems integration deficiencies in mergers and acquisitions: A configurational perspective. Journal of Management Information Systems, 33(4), 942-977.




Henningsson, S. 和 Kettinger, W. J. (2016)。了解并购中的信息系统集成缺陷：配置视角。管理信息系统杂志，33(4), 942-977。


Henningsson, S., Yetton, P. W., & Wynne, P. J. (2018). A review of information system integration in mergers and acquisitions. Journal of Information Technology, 33(4), 255-303.




Henningsson, S.、Yetton, P. W. 和 Wynne, P. J. (2018)。并购中的信息系统集成综述信息技术杂志，33(4), 255-303。


Heron, R., & Lie, E. (2002). Operating performance and the method of payment in takeovers. The Journal of Financial and Quantitative Analysis, 37(1), 137-155.




Heron, R. 和 Lie, E. (2002)。经营业绩及收购支付方式。金融与定量分析杂志，37(1), 137-155。


Hoberg, G., & Phillips, G. (2010). Product market synergies and competition in mergers and acquisitions: A text-based analysis. The Review of Financial Studies, 23(10), 3773-3811.




霍伯格，G. 和菲利普斯，G. (2010)。并购中的产品市场协同效应和竞争：基于文本的分析。金融研究评论，23(10), 3773-3811。


Homburg, C., & Bucerius, M. (2006). Is speed of integration really a success factor of mergers and acquisitions? An analysis of the role of internal and external relatedness. Strategic Management Journal, 27(4), 347-367.




Homburg, C. 和 Bucerius, M. (2006)。整合速度真的是并购成功的因素吗？分析内部和外部关联性的作用。战略管理杂志，27(4), 347-367。


Jain, R. P., & Ramesh, B. (2015). The roles of contextual elements in post-merger common platform development: An empirical investigation. European Journal of Information Systems, 24(2), 159-177.




Jain, R. P. 和 Ramesh, B. (2015)。上下文元素在合并后通用平台开发中的作用：实证调查。欧洲信息系统杂志，24(2), 159-177。


Jemison, D. B., & Sitkin, S. B. (1986). Corporate acquisitions: A process perspective. Academy of Management Review, 11(1), 145-163.




杰米森 D. B. 和西特金 S. B. (1986)。公司收购：过程视角。管理学院评论，11(1), 145-163。


Kim, J.-Y., & Finkelstein, S. (2009). The effects of strategic and market complementarity on acquisition performance: Evidence from the U.S. commercial banking industry, 1989-2001. Strategic Management Journal, 30(6), 617-646.




Kim, J.-Y. 和 Finkelstein, S. (2009)。战略和市场互补性对收购绩效的影响：来自美国商业银行业的证据，1989-2001 年。战略管理杂志，30(6), 617-646。


King, D. R., Dalton, D. R., Daily, C. M., & Covin, J. G. (2004). Meta-analyses of post-acquisition performance: indications of unidentified moderators. Strategic Management Journal, 25(2), 187-200.




King, D. R.、Dalton, D. R.、Daily, C. M. 和 Covin, J. G. (2004)。收购后绩效的荟萃分析：身份不明的调节者的迹象。战略管理杂志，25(2), 187-200。


Kovela, S., & Skok, W. (2012). Mergers and acquisitions in banking: Understanding the IT integration perspective. International Journal of Business and Management, 7(18), 69- 81.




Kovela, S. 和 Skok, W. (2012)。银行业并购：了解 IT 集成视角。国际商业与管理杂志，7（18），69-81。


Langer, N., Slaughter, S. A., & Mukhopadhyay, T. (2014). Project managers’ practical intelligence and project performance in software offshore outsourcing: A field study. Information Systems Research, 25(2), 364-384.




Langer, N.、Slaughter, S. A. 和 Mukhopadhyay, T. (2014)。软件离岸外包中项目经理的实用智慧和项目绩效：实地研究。信息系统研究，25(2), 364-384。


Larsson, R., & Finkelstein, S. (1999). Integrating strategic, organizational, and human resource perspectives on mergers and acquisitions: A case survey of synergy realization. Organization Science, 10(1), 1-26.




拉尔森，R. 和芬克尔斯坦，S. (1999)。整合并购的战略、组织和人力资源视角：协同效应实现的案例调查。组织科学，10(1), 1-26。


Laursen, K., Masciarelli, F., & Prencipe, A. (2012). Regions matter: How localized social capital affects innovation and external knowledge acquisition. Organization Science, 23(1), 177-193.




劳尔森，K.，马西亚雷利，F.，＆普伦西比，A.（2012）。地区很重要：本地化社会资本如何影响创新和外部知识获取。组织科学，23(1), 177-193。


Majchrzak, A., Rice, R. E., Malhotra, A., King, N., & Ba, S. (2000). Technology adaptation: The case of a computer-supported inter-organizational virtual team. MIS Quarterly, 24(4), 569- 600.




Majchrzak, A.、Rice, R. E.、Malhotra, A.、King, N. 和 Ba, S. (2000)。技术适应：计算机支持的组织间虚拟团队的案例。 《管理信息系统季刊》，24(4)，569-600。


Makri, M., Hitt, M. A., & Lane, P. J. (2010). Complementary technologies, knowledge relatedness, and invention outcomes in high technology mergers and acquisitions. Strategic Management Journal, 31(6), 602-628.




Makri, M.、Hitt, M. A. 和 Lane, P. J. (2010)。高科技并购中的互补技术、知识相关性和发明成果。战略管理杂志，31(6), 602-628。


Malmendier, U., & Tate, G. (2008). Who makes acquisitions? CEO overconfidence and the market’s reaction. Journal of Financial Economics, 89(1), 20-43.




Malmendier, U. 和 Tate, G. (2008)。谁进行收购？ CEO过度自信和市场反应。金融经济学杂志，89（1），20-43。


Mata, F. J., Fuerst, W. L., & Barney, J. B. (1995). Information technology and sustained competitive advantage: a resourcebased analysis. MIS Quarterly, 19(4), 487.




Mata, F. J.、Fuerst, W. L. 和 Barney, J. B. (1995)。信息技术和持续竞争优势：基于资源的分析。 《管理信息系统季刊》，19(4), 487。


Mehta, M., & Hirschheim, R. (2007). Strategic alignment in mergers and acquisitions: Theorizing IS integration decision making. Journal of the Association for Information Systems, 8(3), 143-174.




梅塔，M.，＆赫希海姆，R.（2007）。并购中的战略调整：理论化 IS 整合决策。信息系统协会杂志，8(3), 143-174。


Milgrom, P., & Roberts, J. (1990). The economics of modern manufacturing: Technology, strategy, and organization. The American Economic Review, 80(3), 511-528.




米尔格罗姆，P.，＆罗伯茨，J.（1990）。现代制造业的经济学：技术、战略和组织。 《美国经济评论》，80(3), 511-528。


Moeller, S. B., Schlingemann, F. P., & Stulz, R. M. (2004). Firm size and the gains from acquisitions. Journal of Financial Economics, 73(2), 201-228.




Moeller, S. B.、Schlingemann, F. P. 和 Stulz, R. M. (2004)。公司规模和收购收益。金融经济学杂志，73(2), 201-228。


Montgomery, J. M., & Nyhan, B. (2010). Bayesian model averaging: Theoretical developments and practical applications. Political Analysis, 18(02), 245-270.




蒙哥马利，J.M. 和尼汉，B. (2010)。贝叶斯模型平均：理论发展和实际应用。政治分析，18(02), 245-270。


Nordstrom, K., & Vahlne, J.-E. (1994). Is the globe shrinking? Psychic distance and the establishment of Swedish sales subsidiaries during the last 100 years. In M. Landeck (Ed.), International Trade: Regional and Global Issues (pp. 41-56). Macmillan.




Nordstrom, K. 和 Vahlne, J.-E. （1994）。地球正在缩小吗？过去 100 年来的心理距离和瑞典销售子公司的建立。见 M. Landeck（主编），《国际贸易：区域和全球问题》（第 41-56 页）。麦克米伦。


Pablo, A. L. (1994). Determinants of acquisition integration level: a decision-making perspective. Academy of Management Journal, 37(4), 803-836.




巴勃罗，A.L. (1994)。收购整合水平的决定因素：决策视角。管理学会杂志，37(4), 803-836。


Page, S. (2010). 1. On diversity and complexity. In S. E. Page (Ed.), Diversity and Complexity (pp. 16-53). Princeton University Press.




佩奇，S.（2010）。 1.关于多样性和复杂性。见 S. E. Page（主编），多样性和复杂性（第 16-53 页）。普林斯顿大学出版社。


Pich, M. T., Loch, C. H., & Meyer, A. D. (2002). On uncertainty, ambiguity, and complexity in project management. Management Science, 48(8), 1008-1023.




Pich, M. T.、Loch, C. H. 和 Meyer, A. D. (2002)。关于项目管理中的不确定性、模糊性和复杂性。管理科学，48（8），1008-1023。


Puranam, P., Singh, H., & Chaudhuri, S. (2009). Integrating acquired capabilities: When structural integration is (un)necessary. Organization Science, 20(2), 313-328.




Puranam, P.、Singh, H. 和 Chaudhuri, S. (2009)。整合已获得的能力：当结构整合是（不需要）必要时。组织科学，20(2), 313-328。


Rai, A., Patnayakuni, R., & Seth, N. (2006). Firm performance impacts of digitally enabled supply chain integration capabilities. MIS Quarterly, 30(2), 225-246.




Rai, A.、Patnayakuni, R. 和 Seth, N. (2006)。数字化供应链整合能力对公司绩效的影响。 《管理信息系统季刊》，30(2)，225-246。


Rai, Pavlou, Im, & Du. (2012). Interfirm IT capability profiles and communications for cocreating relational value: Evidence from the logistics industry. MIS Quarterly, 36(1), 233-262.




拉伊、帕夫卢、伊姆和杜。 （2012）。共同创造关系价值的公司间 IT 能力概况和沟通：来自物流行业的证据。 《管理信息系统季刊》，36(1)，233-262。


Rogan, M. (2014). Too close for comfort? The effect of embeddedness and competitive overlap on client relationship retention following an acquisition. Organization Science, 25(1), 185-203.




罗根，M.（2014）。距离太近不舒服？嵌入性和竞争重叠对收购后客户关系保留的影响。组织科学，25(1), 185-203。


Rogan, M., & Sorenson, O. (2014). Picking a (poor) partner. Administrative Science Quarterly, 59(2), 301-329.




罗根，M.，＆索伦森，O.（2014）。选择一个（糟糕的）合作伙伴。行政科学季刊，59(2), 301-329。


Saran, C. (2019). SAP disruption leads to Revlon class action lawsuit. ComputerWeekly. https://www.computerweekly.com/ news/252464278/SAP-disruption-leads-to-Revlon-classaction-lawsuit




萨兰，C.（2019）。 SAP 中断导致 Revlon 集体诉讼。计算机周刊。 https://www.computerweekly.com/news/252464278/SAP-disruption-leads-to-Revlon-classaction-lawsuit


Sarrazin, H., & West, A. (2011). Understanding the strategic value of IT in M&A. McKinsey & Company. http://www.mckinsey.com/business-functions/strategy-andcorporate-finance/our-insights/understanding-the-strategicvalue-of-it-in-m-and-38a




扎拉青，H. 和韦斯特，A. (2011)。了解 IT 在并购中的战略价值。麦肯锡公司。 http://www.mckinsey.com/business-functions/strategy-andcorporate-finance/our-insights/understanding-the-strategicvalue-of-it-in-m-and-38a


Schneberger, S. L., & McLean, E. R. (2003). The complexity cross: implications for practice. Communications of the ACM, 46(9), 216-225.




施内伯格，S.L. 和麦克莱恩，E.R. (2003)。复杂性交叉：对实践的影响。 ACM 通讯，46(9), 216-225。


Schoenherr, T., Hilpert, D., Soni, A. K., Venkataramanan, M. A., & Mabert, V. A. (2010). Enterprise systems complexity and its antecedents: A grounded-theory approach. International Journal of Operations & Production Management, 30(6), 639- 668.




Schoenherr, T.、Hilpert, D.、Soni, A. K.、Venkataramanan, M. A. 和 Mabert, V. A. (2010)。企业系统复杂性及其前因：扎根理论方法。国际运营与生产管理杂志，30(6), 639-668。


Seth, A. (1990). Sources of value creation in acquisitions: An empirical investigation. Strategic Management Journal, 11(6), 431-446.




赛斯，A.（1990）。收购中价值创造的来源：实证调查。战略管理杂志，11(6), 431-446。


Stahl, G. K., & Voigt, A. (2008). Do cultural differences matter in mergers and acquisitions? A tentative model and examination. Organization Science, 19(1), 160-176.




斯塔尔，G.K.和沃伊特，A.（2008）。文化差异在并购中重要吗？暂定模型和检验。组织科学，19(1), 160-176。


Tafti, A., Mithas, S., & Krishnan, M. S. (2013). the importance of IT-enabled flexibility in alliances. MIT Sloan Management Review, 54(3), 13-14.




Tafti, A.、Mithas, S. 和 Krishnan, M.S. (2013)。 IT 支持的联盟灵活性的重要性。麻省理工学院斯隆管理评论，54(3), 13-14。


Tanriverdi, H. (2006). Performance effects of information technology synergies in multibusiness firms. MIS Quarterly, 30(1), 57-77.




坦里韦尔迪，H.（2006）。多业务公司信息技术协同效应的绩效影响。 《管理信息系统季刊》，30(1)，57-77。


Tanriverdi, H., & Uysal, V. B. (2011). Cross-business information technology integration and acquirer value creation in corporate mergers and acquisitions. Information Systems Research, 22(4), 703-720.




Tanriverdi, H. 和 Uysal, V. B. (2011)。企业并购中的跨业务信息技术整合和收购方价值创造。信息系统研究，22(4), 703-720。


Tanriverdi, H., & Uysal, V. B. (2015). When IT capabilities are not scale-free in merger and acquisition integrations: how do capital markets react to IT capability asymmetries between acquirer and target? European Journal of Information Systems, 24(2), 145-158.




Tanriverdi, H. 和 Uysal, V. B. (2015)。当并购整合中 IT 能力不是无标度时：资本市场如何应对收购方和目标公司之间 IT 能力的不对称？欧洲信息系统杂志，24(2), 145-158。


Thibodeau, P., & Tennant, D. (2004). Q&A: HP’s CIO details company’s ERP migration problems. ComputerWorld. https://www.computerworld.com/article/2565959/q-a--hp-scio-details-company-s-erp-migration-problems.html




Thibodeau, P. 和 Tennant, D. (2004)。问答：惠普 CIO 详细介绍了公司的 ERP 迁移问题。计算机世界。 https://www.computerworld.com/article/2565959/q-a--hp-scio-details-company-s-erp-migration-problems.html


Tilson, D., Lyytinen, K., & Sørensen, C. (2010). Research commentary—Digital infrastructures: The missing IS research agenda. Information Systems Research, 21(4), 748-759.




蒂尔森，D.，Lyytinen，K.，＆索伦森，C.（2010）。研究评论——数字基础设施：缺失的信息系统研究议程。信息系统研究，21(4), 748-759。


Vernadat, F. B. (2007). Interoperable enterprise systems: Principles, concepts, and methods. Annual Reviews in Control, 31(1), 137-145.




Vernadat，F.B.（2007）。可互操作的企业系统：原理、概念和方法。 《控制》年度审查，31(1), 137-145。


Vinoski, S. (2002). Where is is middleware. IEEE Internet Computing, 6(2), 83-85.




维诺斯基，S.（2002）。中间件在哪里。 IEEE 互联网计算，6(2), 83-85。


Wang, L., & Zajac, E. J. (2007). Alliance or acquisition? A dyadic perspective on interfirm resource combinations. Strategic Management Journal, 28(13), 1291-1317.




Wang, L. 和 Zajac, E. J. (2007)。联盟还是收购？公司间资源组合的二元视角。战略管理杂志，28（13），1291-1317。


Wijnhoven, F., Spil, T., Stegwee, R., & Fa, R. T. A. (2006). Postmerger IT integration strategies: An IT alignment perspective. The Journal of Strategic Information Systems, 15(1), 5-28.




Wijnhoven, F.、Spil, T.、Stegwee, R. 和 Fa, R. T. A. (2006)。合并后 IT 集成策略：IT 调整视角。战略信息系统杂志，15(1), 5-28。


Xia, W., & Lee, G. (2005). Complexity of information systems development projects: Conceptualization and measurement development. Journal of Management Information Systems, 22(1), 45-83.




夏 W. 和李 G. (2005)。信息系统开发项目的复杂性：概念化和测量开发。管理信息系统杂志，22(1), 45-83。


Xue, L., Ray, G., & Gu, B. (2011). Environmental uncertainty and IT infrastructure governance: A curvilinear relationship. Information Systems Research, 22(2), 389-399.




薛 L.、雷 G. 和顾 B. (2011)。环境不确定性和 IT 基础设施治理：曲线关系。信息系统研究，22(2), 389-399。


Yang, H., Lin, Z. (john), & Lin, Y. (lisa). (2010). A multilevel framework of firm boundaries: Firm characteristics, dyadic differences, and network attributes. Strategic Management Journal, 31(3), 237-261.




杨 H.、林 Z. (约翰) 和林 Y. (丽莎)。 （2010）。企业边界的多层次框架：企业特征、二元差异和网络属性。战略管理杂志，31(3), 237-261。


Yetton, P., Henningsson, S., & Bjørn-Andersen, N. (2013). “Ready to acquire”: The IT resources required for a growth-byacquisition business strategy. MIS Quarterly Executive, 12(1), 19-35.




Yetton, P.、Henningsson, S. 和 Bjørn-Andersen, N. (2013)。 “准备收购”：通过收购实现增长的业务战略所需的 IT 资源。 MIS 执行季度报告，12(1), 19-35。


Zhang, C., & Jacobsen, H.-A. (2003). Quantifying aspects in middleware platforms. Proceedings of the 2nd International Conference on Aspect-Oriented Software Development (pp. 130-139).




张，C.，和雅各布森，H.-A。 （2003）。量化中间件平台的各个方面。第二届面向方面的软件开发国际会议论文集（第 130-139 页）。


Zhou, K. Z., & Wu, F. (2009). Technological capability, strategic flexibility, and product innovation. Strategic Management Journal, 31(5), 547-561.




周克Z.和吴F.（2009）。技术能力、战略灵活性和产品创新。战略管理杂志，31(5), 547-561。


Zhu, K. X., & Zhou, Z. Z. (2011). Research note—Lock-in strategy in software competition: Open-source software vs. proprietary software. Information Systems Research, 23(2), 536-545.




朱克新，周志忠 (2011)。研究报告——软件竞争中的锁定策略：开源软件与专有软件。信息系统研究，23(2), 536-545。


Zollo, M., & Meier, D. (2008). What is M&A performance? Academy of Management Perspectives, 22(3), 55-77.




Zollo, M. 和 Meier, D. (2008)。什么是并购绩效？管理学院观点，22(3), 55-77。


Zollo, M., & Singh, H. (2004). Deliberate learning in corporate acquisitions: Post-acquisition strategies and integration capability in U.S. bank mergers. Strategic Management Journal, 25(13), 1233-1256.




佐洛，M. 和辛格，H. (2004)。企业收购中的刻意学习：美国银行合并中的收购后策略和整合能力。战略管理杂志，25（13），1233-1256。


Zollo, M., & Winter, S. G. (2002). Deliberate learning and the evolution of dynamic capabilities. Organization Science, 13(3), 339-351.




Zollo, M. 和 Winter, S. G. (2002)。刻意学习和动态能力的演变。组织科学，13(3), 339-351。


## About the Authors




## 关于作者


Kyunghee Lee is an assistant professor of information systems Management at the Mike Ilitch School of Business, Wayne State University. He received a Ph.D. and M.S. in management engineering, and a B.S. in electrical engineering, all from the Korea Advanced Institute of Science and Technology (KAIST). He was a postdoctoral research fellow at the Desautels Faculty of Management, McGill University. He studies the economic and societal impacts of IT, with a focus on the decentralization of business models and organizational structures. His research has been published in MIS Quarterly and Journal of Management Information Systems, among other outlets.




Kyunghee Lee 是韦恩州立大学迈克伊利奇商学院信息系统管理学助理教授。他获得了博士学位。和硕士。管理工程学士学位和学士学位电气工程博士均来自韩国科学技术院（KAIST）。曾任麦吉尔大学德索特尔管理学院博士后研究员。他研究 IT 的经济和社会影响，重点关注业务模式和组织结构的去中心化。他的研究成果发表在 MIS Quarterly 和 Journal of Management Information Systems 等媒体上。


Kunsoo Han is a Bensadoun Faculty Scholar and an associate professor of information systems at the Desautels Faculty of Management, McGill University. He received his Ph.D. from the University of Minnesota, and his B.S. and M.S. from the Korea Advanced Institute of Science and Technology (KAIST). Prior to joining academia, he worked at a large IT consulting company in Korea. He teaches undergraduate courses on systems analysis and modeling and information systems, and a Ph.D. seminar on the economics of IT. His research interests include IT outsourcing, the business value of IT, societal impacts of IT, and IT-enabled channels. His work has been published in Information Systems Research, MIS Quarterly, Production and Operations Management, Journal of Management Information Systems, and MIT Sloan Management Review, among other outlets.




Kunsoo Han 是麦吉尔大学 Desautels 管理学院的 Bensadoun 学院学者和信息系统副教授。他获得了博士学位。从明尼苏达大学获得学士学位，并获得学士学位。和硕士。来自韩国科学技术院（KAIST）。在加入学术界之前，他曾在韩国一家大型 IT 咨询公司工作。他教授有关系统分析和建模以及信息系统的本科课程，以及博士学位。 IT 经济学研讨会。他的研究兴趣包括 IT 外包、IT 的商业价值、IT 的社会影响以及 IT 支持的渠道。他的研究成果发表在《信息系统研究》、《管理信息系统季刊》、《生产与运营管理》、《管理信息系统杂志》和《麻省理工学院斯隆管理评论》等媒体上。


Animesh Animesh is an associate professor of information systems at the Desautels Faculty of Management, McGill University. Animesh has a Ph.D. from the University of Maryland, an M.S. in Information Systems Management from Carnegie Mellon University, and a B.S. in Business Studies from Delhi University. He studies the adoption, design, and impact of internet technologies, digital platforms, and business models. His research has been published in top journals, such as Information Systems Research, MIS Quarterly, Journal of Operations Management, and Marketing Science.




Animesh Animesh 是麦吉尔大学 Desautels 管理学院信息系统副教授。 Animesh 拥有博士学位。来自马里兰大学，硕士学位卡内基梅隆大学信息系统管理学士学位和理学士学位德里大学商业研究学士学位。他研究互联网技术、数字平台和商业模式的采用、设计和影响。他的研究成果发表在《Information Systems Research》、《MIS Quarterly》、《Journal of Operations Management》和《Marketing Science》等顶级期刊上。


Alain Pinsonneault is a Fellow of the Royal Society of Canada, of the National Order of Québec, and of the Association for Information Systems. He is a Distinguished James McGill Professor and the Imasco Chair of Information Systems at the Desautels Faculty of Management, McGill University. His current research interests include the organizational and individual impacts of information technology, user adaptation, and business models in the digital economy, e-health, and the business value of IT. His research has appeared in numerous journals, including Management Science, MIS Quarterly, Information Systems Research, Journal of Management Information Systems, Decision Support Systems, and Organization Science. He has served on the editorial boards of several other journals, including MIS Quarterly, Information Systems Research, Organization Science, and Journal of Management Information Systems.




Alain Pinsonneault 是加拿大皇家学会、魁北克国家勋章和信息系统协会的会员。他是麦吉尔大学 Desautels 管理学院的杰出 James McGill 教授和 Imasco 信息系统主席。他目前的研究兴趣包括信息技术对组织和个人的影响、数字经济中的用户适应和商业模式、电子医疗以及 IT 的商业价值。他的研究成果发表在众多期刊上，包括《管理科学》、《管理信息系统季刊》、《信息系统研究》、《管理信息系统杂志》、《决策支持系统》和《组织科学》。他曾担任其他几本期刊的编辑委员会成员，包括《MIS Quarterly》、《Information Systems Research》、《Organization Science》和《Journal of Management Information Systems》。


## Appendix




＃＃ 附录


## Expert Survey on the Cost of Enterprise Systems Integration




## 关于企业系统集成成本的专家调查


The survey was initially sent out to around 3,000 managers, of which 311 responded (turnout rate = 10%). Of the 311 respondents who initiated the survey, 64 of them were screened out during the survey due to failure to pass the quality assurance tests, which are explained below, leaving 247 as the final sample. Our sample consists of IT experts who have significant work experience in IT and enterprise systems (ES). On average, the respondents have worked in IT fields for 10.87 years and have 9.5 years of experience working with ES. Most of the respondents work in the IT department of a corporation (132), followed by IT consulting (61), systems integration (31), ES vendors (9), and others (14).




该调查最初发送给约 3,000 名管理人员，其中 311 名进行了回应（投票率 = 10%）。在发起调查的 311 名受访者中，有 64 名受访者因未能通过质量保证测试而在调查过程中被筛选出（解释如下），留下 247 名作为最终样本。我们的样本由在 IT 和企业系统 (ES) 方面拥有丰富工作经验的 IT 专家组成。受访者平均在IT领域工作时间为10.87年，在ES领域工作经验为9.5年。大多数受访者在企业的 IT 部门工作（132 人），其次是 IT 咨询（61 人）、系统集成（31 人）、ES 供应商（9 人）和其他（14 人）。


Three-level screening was implemented for quality assurance. First, two questions were asked, one at the beginning and the other in the middle of the survey, to screen out those who seemed to answer randomly. Those who failed both questions were immediately screened ou of the survey. Second, on the first page of the survey, participants were asked about their level of knowledge on the subjects of ES and ES integration using 10-point scales. Those whose answers were less than or equal to 2 (1: not knowledgeable, 10: extremely knowledgeable) were again immediately screened out. The average knowledge level of the participants remaining in the sample was around eight. Third, we also asked how familiar participants are with a given ES module and a given ES vendor. The answers of participants who answered “not at all familiar” with a given ES module and ES vendor were excluded.




实行三级筛选，确保质量。首先，问了两个问题，一个在调查开始时，另一个在调查中间，以筛选出那些看似随意回答的人。那些没有通过这两个问题的人立即被排除在调查之外。其次，在调查的第一页，参与者被问及他们对 ES 和 ES 整合主题的知识水平，采用 10 分制。那些回答小于或等于2（1：不了解，10：非常了解）的人再次被立即筛选掉。样本中剩余参与者的平均知识水平约为 8。第三，我们还询问参与者对给定 ES 模块和给定 ES 供应商的熟悉程度。对于给定的 ES 模块和 ES 供应商回答“完全不熟悉”的参与者的答案被排除在外。


The participants were asked to rate three pairs of ES vendors (e.g., SAP – Oracle) of a particular ES module (e.g., CRM) in terms of the relative cost of integrating systems from the two vendors in a given pair or making them interoperable (Rank 1: the lowest; Rank 3: the highest). Participants answered three questions for each ES module, rating nine vendor pairs in total. These vendor pairs were chosen from a list of the actual pairs existing in the data with varying IT distance levels. We then randomly assigned three modules to each participant (which makes the total number of pairs to rate 27 per participant). We determined that rating all 54 pairs (= 9 pairs x 6 modules) would be too demanding, and thus may increase the chance of inaccurate assessment on their part.




参与者被要求根据集成给定对中两个供应商的系统或使它们具有互操作性的相对成本，对特定 ES 模块（例如 CRM）的三对 ES 供应商（例如 SAP – Oracle）进行评分（排名 1：最低；排名 3：最高）。参与者针对每个 ES 模块回答了三个问题，总共对九个供应商对进行了评分。这些供应商对是从数据中存在的具有不同 IT 距离级别的实际对列表中选择的。然后，我们为每个参与者随机分配三个模块（这使得每个参与者评分的总对数为 27）。我们认为对所有 54 对（= 9 对 x 6 个模块）进行评级过于苛刻，因此可能会增加评估不准确的机会。


<table><tr><td colspan="3">Table A1. Comparison between the Survey-Based and Proposed IT Distance Measures</td></tr><tr><td></td><td>Sample 1</td><td>Sample 2</td></tr><tr><td>Pearson</td><td>0.371***</td><td>0.410***</td></tr><tr><td>Spearman</td><td>0.306**</td><td>0.389***</td></tr><tr><td>Kendall</td><td>0.259***</td><td>0.333***</td></tr></table>




<table><tr><td colspan="3">表 A1。基于调查的 IT 距离测量与建议的 IT 距离测量之间的比较</td></tr><tr><td></td><td>样本 1</td><td>样本2</td></tr><tr><td>皮尔逊</td><td>0.371***</td><td>0.410***</td></tr><tr><td>斯皮尔曼</td><td>0.3 06**</td><td>0.389***</td></tr><tr><td>肯德尔</td><td>0.259***</td><td>0.333***</td></tr></table>


Note: The Pearson correlation is calculated between the survey-based (continuous) and proposed IT distance measures (continuous). Spearman and Kendall correlations are calculated between the survey-based (rank) and proposed IT distance measures (rank). Sample 1: All qualified samples are included. Sample 2: 29 respondents not very knowledgeable on ES and ES integration (whose answers to the knowledge questions are less than or equal to 5) are excluded. $^ { \star } p < 0 . 1 , ^ { \star \star } p < 0 . 0 5 , ^ { \star \star \star } \bar { p } < 0 . 0 1$




注：Pearson 相关性是在基于调查的（连续）和建议的 IT 距离测量（连续）之间计算的。 Spearman 和 Kendall 相关性是在基于调查的（排名）和建议的 IT 距离测量（排名）之间计算的。样品1：包含所有合格样品。样本2：排除29名对ES和ES集成不太了解的受访者（其知识问题的答案小于或等于5）。 $^ { \star } p < 0 。 1 , ^ { \star \star } p < 0 。 0 5 , ^ { \star \star \star } \bar { p } < 0 。 0 1$


For each vendor pair in each module, we calculated IT distance using its average rank from the survey responses. Then, this survey-based IT distance measure was compared with the IT distance estimated using Word2Vec. In Table A1, the first and second rows report the Pearson and Spearman correlations between the two measures. In addition to these raw correlation metrics, the average of Kendall’s coefficients is reported in the third row. That is, for each question, the survey ranks of three vendor pairs were compared with the ranks from the original measure, and Kendall’s coefficient was calculated to measure the proximity between these ranks. For instance, if the ranks of the three pairs are exactly the same (opposite) between the two sets, the coefficient will be +1 (-1). Otherwise, a value between -1 and +1 is assigned, depending on the number of concordant (discordant) pairs. Furthermore, we repeated the tests for a restricted sample where the participants’ knowledge level (ES and ES integration) is above six (29 participants excluded), which is shown in the second column. The correlation between the two IT distance measures increases when we use the responses from more knowledgeable participants.




对于每个模块中的每个供应商对，我们使用调查响应中的平均排名来计算 IT 距离。然后，将这种基于调查的 IT 距离测量与使用 Word2Vec 估计的 IT 距离进行比较。在表 A1 中，第一行和第二行报告了两个度量之间的 Pearson 和 Spearman 相关性。除了这些原始相关性指标之外，第三行还报告了肯德尔系数的平均值。也就是说，对于每个问题，将三个供应商对的调查排名与原始测量的排名进行比较，并计算肯德尔系数来衡量这些排名之间的接近程度。例如，如果两组之间三对的排名完全相同（相反），则系数将为 +1 (-1)。否则，根据一致（不一致）对的数量分配 -1 到 +1 之间的值。此外，我们对一个限制样本进行了重复测试，其中参与者的知识水平（ES 和 ES 整合）高于 6（排除 29 名参与者），如第二列所示。当我们使用知识渊博的参与者的回答时，两个 IT 距离度量之间的相关性就会增加。


<table><tr><td colspan="13">Table A2. Acquisition Motivation</td></tr><tr><td>SDC purpose code</td><td colspan="3">SDC purpose code description</td><td colspan="3">Operational synergy</td><td colspan="3">Operational synergy (including new asset/product)</td><td colspan="3">Operational synergy (including new asset/product and market expansion)</td></tr><tr><td>R</td><td colspan="3">Concentrate on core businesses/assets</td><td colspan="3">1</td><td colspan="3">1</td><td colspan="3">1</td></tr><tr><td>CMP</td><td colspan="3">Acquire competitors' technology/strategic assets</td><td colspan="3">1</td><td colspan="3">1</td><td colspan="3">1</td></tr><tr><td>STR</td><td colspan="3">Strengthen operations</td><td colspan="3">1</td><td colspan="3">1</td><td colspan="3">1</td></tr><tr><td>SYN</td><td colspan="3">Create synergies; eliminate duplicate services/operations</td><td colspan="3">1</td><td colspan="3">1</td><td colspan="3">1</td></tr><tr><td>RST</td><td colspan="3">General restructuring of business/operations</td><td colspan="3">0</td><td colspan="3">1</td><td colspan="3">1</td></tr><tr><td>CSH</td><td colspan="3">Raise cash through disposal</td><td colspan="3">0</td><td colspan="3">1</td><td colspan="3">1</td></tr><tr><td>PRD</td><td colspan="3">Allow offering new products and services</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">1</td></tr><tr><td>EPM</td><td colspan="3">Strengthen existing operations/expand presence in the primary market</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">1</td></tr><tr><td>ESM</td><td colspan="3">Strengthen existing operations/expand presence in the secondary market</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">1</td></tr><tr><td>EPG</td><td colspan="3">Expand presence in new geographical regions</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">1</td></tr><tr><td>EXP</td><td colspan="3">Expand presence in new/foreign markets</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">1</td></tr><tr><td>DBT</td><td colspan="3">Proceeds used to pay down existing outstanding debt</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">0</td></tr><tr><td>DIS</td><td colspan="3">Dispose of surplus cash on hand</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">0</td></tr><tr><td>DOS</td><td colspan="3">Increase shareholder value / dilute number of outstanding shares</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">0</td></tr><tr><td>ESP</td><td colspan="3">Purchase shares for ESOP</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">0</td></tr><tr><td>FCA</td><td colspan="3">Raise cash in conjunction with financing of concurrent acq./merger</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">0</td></tr><tr><td>GEN</td><td colspan="3">General strategy to take advantage of sound investment opportunities</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">0</td></tr><tr><td>ISV</td><td colspan="3">Increase shareholder value</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">0</td></tr><tr><td>LEG</td><td colspan="3">Change in legislation allows increased foreign ownership</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">0</td></tr><tr><td>ODO</td><td colspan="3">Offset dilution caused by the exercise of options</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">0</td></tr><tr><td>OTH</td><td colspan="3">Other</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">0</td></tr><tr><td>PEB</td><td colspan="3">Private equity buy-and-build strategy.</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">0</td></tr><tr><td>REG</td><td colspan="3">Sale to comply with regulatory requirements</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">0</td></tr><tr><td>RTO</td><td colspan="3">Response to other bid / tender offers</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">0</td></tr><tr><td>SEL</td><td colspan="3">Sell a loss-making/bankrupt operation</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">0</td></tr><tr><td>TXI</td><td colspan="3">Tax inversion</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">0</td></tr><tr><td rowspan="3"></td><td colspan="3">Performance+Industry</td><td colspan="3">Performance+Industry (BV)</td><td colspan="3">Performance+Industry+Size+Geo</td><td colspan="3">No-completion rule</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td><td>(7)</td><td>(8)</td><td>(9)</td><td>(10)</td><td>(11)</td><td>(12)</td></tr><tr><td>Full sample</td><td>Operational synergy</td><td>Non-operational synergy</td><td>Full sample</td><td>Operational synergy</td><td>Non-operational synergy</td><td>Full sample</td><td>Operational synergy</td><td>Non-operational synergy</td><td>Full sample</td><td>Operational synergy</td><td>Non-operational synergy</td></tr><tr><td>Public</td><td>-0.074(-0.90)</td><td>-0.081(-0.82)</td><td>-0.030(-0.14)</td><td>-0.146*(-1.84)</td><td>-0.067(-0.66)</td><td>-0.193(-1.33)</td><td>-0.058(-0.68)</td><td>-0.134(-1.30)</td><td>0.134(0.70)</td><td>-0.014(-0.20)</td><td>0.038(0.45)</td><td>-0.053(-0.36)</td></tr><tr><td>Firm size</td><td>0.036(0.43)</td><td>0.123(1.11)</td><td>-0.204(-1.26)</td><td>-0.084(-0.77)</td><td>-0.207(-1.64)</td><td>-0.190(-1.05)</td><td>0.067(0.84)</td><td>0.162(1.40)</td><td>-0.083(-0.57)</td><td>0.093(1.15)</td><td>0.149(1.41)</td><td>-0.091(-0.59)</td></tr><tr><td>Relative transaction size</td><td>0.061(0.75)</td><td>0.025(0.24)</td><td>0.104(0.73)</td><td>0.146(1.30)</td><td>0.116(0.75)</td><td>0.061(0.53)</td><td>0.081(0.93)</td><td>0.073(0.58)</td><td>0.098(0.70)</td><td>0.103(1.52)</td><td>0.163**(2.10)</td><td>0.035(0.30)</td></tr><tr><td>Book leverage</td><td>-0.069(-0.66)</td><td>-0.206(-1.60)</td><td>0.194(1.50)</td><td>-0.014(-0.15)</td><td>-0.078(-0.71)</td><td>0.146(1.19)</td><td>-0.087(-0.78)</td><td>-0.134(-0.96)</td><td>-0.003(-0.02)</td><td>-0.144(-1.63)</td><td>-0.304***(-2.97)</td><td>-0.018(-0.13)</td></tr><tr><td>Prior financial performance</td><td>-0.156(-0.93)</td><td>-0.147(-0.84)</td><td>-0.206(-0.57)</td><td>-0.338**(-2.44)</td><td>-0.376**(-2.26)</td><td>-0.066(-0.26)</td><td>-0.296*(-1.67)</td><td>-0.214(-1.21)</td><td>-0.571(-1.55)</td><td>-0.379***(-2.68)</td><td>-0.458***(-2.69)</td><td>-0.279(-0.84)</td></tr><tr><td>Prior M&amp;A experience</td><td>-0.060(-0.80)</td><td>0.039(0.36)</td><td>-0.128(-0.70)</td><td>0.186*(1.67)</td><td>0.405***(3.18)</td><td>-0.108(-0.61)</td><td>-0.096(-1.29)</td><td>-0.020(-0.21)</td><td>-0.152(-0.95)</td><td>-0.000(-0.01)</td><td>0.003(0.03)</td><td>0.049(0.34)</td></tr><tr><td>Prior M&amp;A performance</td><td>-0.075(-0.90)</td><td>-0.116(-0.90)</td><td>-0.015(-0.12)</td><td>-0.152**(-2.10)</td><td>-0.118(-1.24)</td><td>-0.236**(-2.44)</td><td>-0.005(-0.06)</td><td>-0.064(-0.51)</td><td>0.056(0.42)</td><td>-0.106(-1.22)</td><td>-0.180*(-1.87)</td><td>-0.069(-0.41)</td></tr><tr><td>Market-to-book value of assets</td><td>0.108(0.73)</td><td>0.088(0.60)</td><td>0.088(0.29)</td><td>0.280**(2.04)</td><td>0.198(1.37)</td><td>0.216(0.83)</td><td>0.188(1.25)</td><td>0.155(1.01)</td><td>0.310(0.96)</td><td>0.192*(1.81)</td><td>0.254**(2.00)</td><td>0.149(0.55)</td></tr><tr><td>Industry relatedness (SIC2)</td><td>-0.161*(-1.96)</td><td>-0.137(-1.43)</td><td>-0.193(-1.14)</td><td>-0.102(-1.14)</td><td>-0.081(-0.75)</td><td>-0.168(-1.54)</td><td>-0.159*(-1.89)</td><td>-0.113(-1.09)</td><td>-0.242*(-1.84)</td><td>-0.158**(-2.11)</td><td>-0.213**(-2.34)</td><td>-0.056(-0.38)</td></tr><tr><td>Industry relatedness (SIC4)</td><td>-0.090(-1.15)</td><td>0.025(0.27)</td><td>-0.021(-0.12)</td><td>-0.035(-0.45)</td><td>-0.079(-0.88)</td><td>0.141(1.27)</td><td>-0.043(-0.53)</td><td>0.072(0.76)</td><td>-0.017(-0.09)</td><td>-0.049(-0.59)</td><td>-0.030(-0.30)</td><td>0.043(0.24)</td></tr><tr><td>Same state</td><td>0.079(1.20)</td><td>0.071(0.87)</td><td>-0.062(-0.44)</td><td>0.104(1.44)</td><td>0.142(1.56)</td><td>-0.135(-1.28)</td><td>0.099(1.51)</td><td>0.117(1.34)</td><td>0.080(0.58)</td><td>0.001(0.02)</td><td>-0.075(-1.03)</td><td>-0.092(-0.70)</td></tr><tr><td>Industry IT intensity</td><td>0.012(0.11)</td><td>-0.036(-0.31)</td><td>0.346*(1.71)</td><td>0.263***(2.74)</td><td>0.193(1.64)</td><td>0.672**(2.36)</td><td>-0.096(-0.75)</td><td>-0.054(-0.41)</td><td>-0.047(-0.22)</td><td>0.016(0.17)</td><td>-0.145(-1.36)</td><td>0.425**(2.27)</td></tr><tr><td>IT distance</td><td>-0.153**(-2.13)</td><td>-0.317***(-3.67)</td><td>0.025(0.22)</td><td>-0.153**(-2.38)</td><td>-0.231***(-2.82)</td><td>-0.094(-0.89)</td><td>-0.177**(-2.44)</td><td>-0.294***(-2.95)</td><td>-0.132(-1.32)</td><td>-0.197**(-2.53)</td><td>-0.295***(-3.72)</td><td>-0.096(-0.72)</td></tr><tr><td>R-squared</td><td>0.139</td><td>0.263</td><td>0.304</td><td>0.246</td><td>0.420</td><td>0.437</td><td>0.142</td><td>0.237</td><td>0.302</td><td>0.302</td><td>0.444</td><td>0.325</td></tr><tr><td>N</td><td>185</td><td>111</td><td>74</td><td>183</td><td>110</td><td>73</td><td>185</td><td>111</td><td>74</td><td>182</td><td>109</td><td>73</td></tr><tr><td>ITD btw. group cf.</td><td></td><td colspan="2">0.001</td><td></td><td colspan="2">0.092</td><td></td><td colspan="2">0.069</td><td></td><td colspan="2">0.097</td></tr></table>




<table><tr><td colspan="13">表 A2。收购动机</td></tr><tr><td>SDC目的代码</td><td colspan="3">SDC目的代码说明</td><td colspan="3">运营协同</td><td colspan="3">运营协同（包括新资产/产品）</td><td colspan="3">运营协同（包括新资产/产品和市场）扩张）</td></tr><tr><td>R</td><td colspan="3">专注于核心业务/资产</td><td colspan="3">1</td><td colspan="3">1</td><td colspan="3">1</td></tr><tr><td>CMP</td><td colspan="3">收购竞争对手技术/战略资产</td><td colspan="3">1</td><td colspan="3">1</td><td colspan="3">1</td></tr><tr><td>STR</td><td colspan="3">加强运营</td><td colspan="3">1</td><td colspan="3">1</td><td colspan="3">1</td></tr><tr><td>SYN</td><td colspan="3">创造协同效应；消除重复的服务/运营</td><td colspan="3">1</td><td colspan="3">1</td><td colspan="3">1</td></tr><tr><td>RST</td><td colspan="3">业务/运营的一般重组</td><td colspan="3">0</td><td colspan="3">1</td><td colspan="3">1</td></tr><tr><td>CSH</td><td colspan="3">通过处置筹集现金</td><td colspan="3">0</td><td colspan="3">1</td><td colspan="3">1</td></tr><tr><td>PRD</td><td colspan="3">允许提供新产品和服务</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">1</td></tr><tr><td>EPM</td><td colspan="3">加强现有业务/扩大一级市场业务</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">1</td></tr><tr><td>ESM</td><td colspan="3">加强现有业务/扩大二级市场业务</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">1</td></tr><tr><td>EPG</td><td colspan="3">扩大在新地理区域的影响力</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">1</td></tr><tr><td>EXP</td><td colspan="3">扩大在新/国外市场的影响力</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">1</td></tr><tr><td>DBT</td><td colspan="3">用于偿还现有未偿债务的收益</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">0</td></tr><tr><td>DIS</td><td colspan="3">处理手头剩余现金</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">0</td></tr><tr><td>DOS</td><td colspan="3">增加股东价值/稀释流通股数量</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">0</td></tr><tr><td>ESP</td><td colspan="3">购买员工持股计划</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">0</td></tr><tr><td>FCA</td><td colspan="3">筹集现金与同时收购/合并的融资相结合</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">0</td></tr><tr><td>GEN</td><td colspan="3">利用良好投资机会的总体策略</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">0</td></tr><tr><td>ISV</td><td colspan="3">增加股东价值</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">0</td></tr><tr><td>LEG</td><td colspan="3">立法变更允许增加外资所有权</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">0</td></tr><tr><td>ODO</td><td colspan="3">造成抵消稀释通过行使期权</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">0</td></tr><tr><td>OTH</td><td colspan="3">其他</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">0</td></tr><tr><td>PEB</td><td colspan="3">私募股权购买和构建策略。</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">0</td></tr><tr><td>REG</td><td colspan="3">销售符合监管要求</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">0</td></tr><tr><td>RTO</td><td colspan="3">对其他出价/要约的回应</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">0</td></tr><tr><td>SEL</td><td colspan="3">出售亏损/破产业务</td><td colspan="3">0</td><td colspan="3">0</td><td colspan="3">0</td></tr><tr><td>TXI</td><td colspan="3">税收倒置</td><td
colspan="3">0</td><td colspan="3">0</td><td colspan="3">0</td></tr><tr><td rowspan="3"></td><td colspan="3">业绩+行业</td><td colspan="3">业绩+行业 (BV)</td><td colspan="3">业绩+行业+规模+地理位置</td><td colspan="3">未完成规则</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td>< td>(7)</td><td>(8)</td><td>(9)</td><td>(10)</td><td>(11)</td><td>(12)</td></tr><tr><td>完整样本</td><td>运营协同</td><td>非运营协同</td><td>完整样本</td><td>运营协同</td><td>非运营协同</td><td>完整样本</td><td>运营协同</td><td>非运营协同</td><td>完整示例</td><td>运营协同</td><td>非运营协同效应</td></tr><tr><td>公开</td><td>-0.074(-0.90)</td><td>-0.081(-0.82)</t d><td>-0.030(-0.14)</td><td>-0.146*(-1.84)</td><td>-0.067(-0.66)</td><td>-0.193 (-1.33)</td><td>-0.058(-0.68)</td><td>-0.134(-1.30)</td><td>0.134(0.70)</td><t d>-0.014(-0.20)</td><td>0.038(0.45)</td><td>-0.053(-0.36)</td></tr><tr><td>坚定尺寸</td><td>0.036(0.43)</td><td>0.123(1.11)</td><td>-0.204(-1.26)</td ><td>-0.084(-0.77)</td><td>-0.207(-1.64)</td><td>-0.190(-1.05)</td><td> 0.067(0.84)</td><td>0.162(1.40)</td><td>-0.083(-0.57)</td><td>0.093(1. 15)</td><td>0.149(1.41)</td><td>-0.091(-0.59)</td></tr><tr><td>相对交易尺寸</td><td>0.061(0.75)</td><td>0.025(0.24)</td><td>0.104(0.73)</t d><td>0.146(1.30)</td><td>0.116(0.75)</td><td>0.061(0.53)</td><td>0 .081(0.93)</td><td>0.073(0.58)</td><td>0.098(0.70)</td><td>0.103(1. 52)</td><td>0.163**(2.10)</td><td>0.035(0.30)</td></tr><tr><td>预订杠杆</td><td>-0.069(-0.66)</td><td>-0.206(-1.60)</td><td>0.194(1.50)< /td><td>-0.014(-0.15)</td><td>-0.078(-0.71)</td><td>0.146(1.19)</td><td>-0 .087(-0.78)</td><td>-0.134(-0.96)</td><td>-0.003(-0.02)</td><td>-0.144(-1) .63)</td><td>-0.304***(-2.97)</td><td>-0.018(-0.13)</td></tr><tr><td>之前金融性能</td><td>-0.156(-0.93)</td><td>-0.147(-0.84)</td><td>-0.206(-0.57) </td><td>-0.338**(-2.44)</td><td>-0.376**(-2.26)</td><td>-0.066(-0.26)</td><t d>-0.296*(-1.67)</td><td>-0.214(-1.21)</td><td>-0.571(-1.55)</td><td>-0.379** *(-2.68)</td><td>-0.458***(-2.69)</td><td>-0.279(-0.84)</td></tr><tr><td>之前并购经验</td><td>-0.060(-0.80)</td><td>0.039(0.36)</td><td>-0.128(-0.7) 0)</td><td>0.186*(1.67)</td><td>0.405***(3.18)</td><td>-0.108(-0.61)</td> <td>-0.096(-1.29)</td><td>-0.020(-0.21)</td><td>-0.152(-0.95)</td><td>-0。 000(-0.01)</td><td>0.003(0.03)</td><td>0.049(0.34)</td></tr><tr><td>之前并购性能</td><td>-0.075(-0.90)</td><td>-0.116(-0.90)</td><td>-0.015(-0.12) </td><td>-0.152**(-2.10)</td><td>-0.118(-1.24)</td><td>-0.236**(-2.44)</td><td >-0.005(-0.06)</td><td>-0.064(-0.51)</td><td>0.056(0.42)</td><td>-0.106(-1.22) )</td><td>-0.180*(-1.87)</td><td>-0.069(-0.41)</td></tr><tr><td>市价比的值资产</td><td>0.108(0.73)</td><td>0.088(0.60)</td><td>0.088(0.29)</t d><td>0.280**(2.04)</td><td>0.198(1.37)</td><td>0.216(0.83)</td><td>0 .188(1.25)</td><td>0.155(1.01)</td><td>0.310(0.96)</td><td>0.192*(1.8 1)</td><td>0.254**(2.00)</td><td>0.149(0.55)</td></tr><tr><td>行业相关性(SIC2)</td><td>-0.161*(-1.96)</td><td>-0.137(-1.43)</td><td>-0.193(-1.14)</td><td>-0.193(-1.14)</td> td><td>-0.102(-1.14)</td><td>-0.081(-0.75)</td><td>-0.168(-1.54)</td><td>-0。 159*(-1.89)</td><td>-0.113(-1.09)</td><td>-0.242*(-1.84)</td><td>-0.158**(-2 .11)</td><td>-0.213**(-2.34)</td><td>-0.056(-0.38)</td></tr><tr><td>行业相关性(SIC4)</td><td>-0.090(-1.15)</td><td>0.025(0.27)</td><td>-0.021(-0.12)< /td><td>-0.035(-0.45)</td><td>-0.079(-0.88)</td><td>0.141(1.27)</td><td >-0.043(-0.53)</td><td>0.072(0.76)</td><td>-0.017(-0.09)</td><td>-0.049 (-0.59)</td><td>-0.030(-0.30)</td><td>0.043(0.24)</td></tr><tr><td>相同状态</td><td>0.079(1.20)</td><td>0.071(0.87)</td><td>-0.062(-0.44)</td><td>-0.062(-0.44)</td><td> td><td>0.104(1.44)</td><td>0.142(1.56)</td><td>-0.135(-1.28)</td><td>0 .099(1.51)</td><td>0.117(1.34)</td><td>0.080(0.58)</td><td>0.001(0.02) </td><td>-0.075(-1.03)</td><td>-0.092(-0.70)</td></tr><tr><td>行业信息技术
强度</td><td>0.012(0.11)</td><td>-0.036(-0.31)</td><td>0.346*(1.71 )</td><td>0.263***(2.74)</td><td>0.193(1.64)</td><td>0.672**(2.36)</td>< td>-0.096(-0.75)</td><td>-0.054(-0.41)</td><td>-0.047(-0.22)</td><td>0.0 16(0.17)</td><td>-0.145(-1.36)</td><td>0.425**(2.27)</td></tr><tr><td>IT距离</td><td>-0.153**(-2.13)</td><td>-0.317***(-3.67)</td><td>0.025(0.22)</td>< td>-0.153**(-2.38)</td><td>-0.231***(-2.82)</td><td>-0.094(-0.89)</td><td>-0.177**( -2.44)</td><td>-0.294***(-2.95)</td><td>-0.132(-1.32)</td><td>-0.197**(-2.53)</td>< td>-0.295***(-3.72)</td><td>-0.096(-0.72)</td></tr><tr><td>R 平方</td><td>0.139< /td><td>0.263</td><td>0.304</td><td>0.246</td><td>0.420</td><td>0.437</td><td>0.142 </td><td>0.237</td><td>0.302</td><td>0.302</td><td>0.444</td><td>0.325</td></tr><tr ><td>N</td><td>185</td><td>111</td><td>74</td><td>183</td><td>110</td><td>73</td><t d>185</td><td>111</td><td>74</td><td>182</td><td>109</td><td>73</td></tr><tr><td>ITD顺便说一句。组比照</td><td></td><td colspan="2">0.001</td><td></td><td colspan="2">0.092</td><td></td><td colspan="2">0.069</td><td></td><td colspan="2">0.097</td></tr></table>


Note: The dependent variable is the acquirer’s abnormal operating income measured as the change in the performance-adjusted operating performance scaled by assets from Year -1 to Year +4. Standardized beta coefficients and robust standard errors are used. t-statistics are in parentheses. Announcement years and industries are controlled. \*p < 0.1, \*\*p < 0.05, \*\*\*p < 0.01 BV(book value) indicates that a measure is scaled by the asset’s book value instead of the market value Performance+Industry chooses a comparison group of companies that share a similar performance history and operate in the same industry. Performance+Industry+Size+Geo adds additional conditions on the firm’s size and geographic location to Performance+Industry. The no-completion rule chooses a comparison group of companies that share a similar performance history, operate in the same industry, and announced (but did not complete) an acquisition during the period.




注：因变量为收购方非正常营业收入，以-1年至+4年按资产调整业绩调整后的经营业绩变化来衡量。使用标准化贝塔系数和稳健标准误差。 t-统计量在括号中。公告年份及行业受控。 \*p < 0.1, \*\*p < 0.05, \*\*\*p < 0.01 BV（账面价值）表示衡量指标是根据资产的账面价值而不是市场价值进行衡量。 绩效+行业选择具有相似绩效历史且在同一行业运营的公司的比较组。绩效+行业+规模+地理位置在绩效+行业的基础上增加了关于公司规模和地理位置的附加条件。不完成规则选择具有相似业绩历史、在同一行业运营并在此期间宣布（但未完成）收购的公司进行比较。


Table A4. Alternative Definitions for Operational Synergy Motivation




表 A4。运营协同激励的替代定义


<table><tr><td rowspan="2"></td><td colspan="2">Including restructuring</td><td colspan="2">Including expansion</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td>Public</td><td>-0.083(-0.84)</td><td>-0.021(-0.10)</td><td>-0.134*(-1.66)</td><td>0.274(1.05)</td></tr><tr><td>Firm size</td><td>0.121(1.09)</td><td>-0.254(-1.48)</td><td>0.081(0.82)</td><td>-0.169(-0.74)</td></tr><tr><td>Relative transaction size</td><td>0.065(0.56)</td><td>0.044(0.30)</td><td>0.090(1.02)</td><td>0.094(0.33)</td></tr><tr><td>Book leverage</td><td>-0.178(-1.40)</td><td>0.201(1.53)</td><td>-0.138(-1.24)</td><td>0.107(0.48)</td></tr><tr><td>Prior financial performance</td><td>-0.104(-0.59)</td><td>-0.335(-0.88)</td><td>-0.064(-0.38)</td><td>-0.740(-1.44)</td></tr><tr><td>Prior M&amp;A experience</td><td>-0.003(-0.03)</td><td>-0.090(-0.51)</td><td>-0.009(-0.11)</td><td>-0.304*(-1.98)</td></tr><tr><td>Prior M&amp;A performance</td><td>-0.099(-0.77)</td><td>-0.061(-0.52)</td><td>-0.078(-0.75)</td><td>-0.276(-1.58)</td></tr><tr><td>Market-to-book value of assets</td><td>0.098(0.67)</td><td>0.202(0.62)</td><td>0.111(0.77)</td><td>0.327(0.78)</td></tr><tr><td>Industry relatedness (SIC2)</td><td>-0.151(-1.59)</td><td>-0.166(-0.99)</td><td>-0.111(-1.30)</td><td>-0.646**(-2.87)</td></tr><tr><td>Industry relatedness (SIC4)</td><td>-0.038(-0.40)</td><td>0.095(0.56)</td><td>-0.024(-0.30)</td><td>-0.549**(-2.27)</td></tr><tr><td>Same state</td><td>0.078(0.97)</td><td>0.008(0.05)</td><td>0.042(0.64)</td><td>0.239(1.51)</td></tr><tr><td>Industry IT intensity</td><td>0.021(0.18)</td><td>0.262(1.17)</td><td>-0.039(-0.30)</td><td>0.445*(1.80)</td></tr><tr><td>IT distance</td><td>-0.302***(-3.57)</td><td>-0.006(-0.05)</td><td>-0.198**(-2.22)</td><td>0.099(0.58)</td></tr><tr><td>R-squared</td><td>0.247</td><td>0.311</td><td>0.165</td><td>0.794</td></tr><tr><td>N</td><td>114</td><td>71</td><td>149</td><td>36</td></tr><tr><td>ITD btw. group cf.</td><td colspan="2">0.001</td><td colspan="2">0.016</td></tr></table>




<table><tr><td rowspan="2"></td><td colspan="2">包括重组</td><td colspan="2">包括扩展</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td>公开</td><td> -0.083(-0.84)</td><td>-0.021(-0.10)</td><td>-0.134*(-1.66)</td><td>0.274(1.05)</td></tr><tr><td>坚定大小</td><td>0.121(1.09)</td><td>-0.254(-1.48)</td><td>0.081(0.82)</td><td>-0.169(-0.74)</td></tr><tr><td>相对交易尺寸</td><td>0.065(0.56)</td><td>0.044(0.30)</td><td>0.090(1.02)</td><td>0.094(0.33)</td></tr><tr><td>预订杠杆</td><td>-0.178(-1.40)</td><td>0.201(1.53)</td><td>-0.138(-1.24)</td><td>0.107(0.48)</td></tr><tr><td>过往财务状况业绩</td><td>-0.104(-0.59)</td><td>-0.335(-0.88)</td><td>-0.064(-0.38)</td><td>-0.740(-1.44)</td></tr><tr><td>先前并购经验</td><td>-0.003(-0.03)</td><td>-0.090(-0.51)</td><td>-0.009(-0.11)</td><td>-0.304*(-1.98)</td></tr><tr><td>先前并购业绩</td><td>-0.099(-0.77)</td><td>-0.061(-0.52)</td><td>-0.078(-0.75)</td><td>-0.276(-1.58)</td></tr><tr><td>市净率资产</td><td>0.098(0.67)</td><td>0.202(0.62)</td><td>0.111(0.77)</td><td>0.327(0.78)</td></tr><tr><td>行业关联度(SIC2)</td><td>-0.151(-1.59)</td><td>-0.166(-0.99)</td><td>-0.111(-1.30)</td><td>-0.646**(-2.87)</td></tr><tr><td>行业相关性(SIC4)</td><td>-0.038(-0.40)</td><td>0.095(0.56)</td><td>-0.024(-0.30)</td><td>-0.549**(-2.27)</td></tr><tr><td>相同州</td><td>0.078(0.97)</td><td>0.008(0.05)</td><td>0.042(0.64)</td><td>0.239(1.51)</td></tr><tr><td>行业IT强度</td><td>0.021(0.18)</td><td>0.262(1.17)</td><td>-0.039(-0.30)</td><td>0.445*(1.80)</td></tr><tr><td>IT距离</td><td>-0.302***(-3.57)</td><td>-0.006(-0.05)</td><td>-0.198**(-2.22)</td><td>0.099(0.58)</td></tr><tr><td>R平方</td><td >0.247</td><td>0.311</td><td>0.165</td><td>0.794</td></tr><tr><td>N </td><td>114</td><td>71</td><td>149</td><td>36</td></tr><tr><td>ITD顺便说一句。组比照</td><td colspan="2">0.001</td><td colspan="2">0.016</td></tr></table>


Note: The dependent variable is the acquirer’s abnormal operating income measured as the change in the performance-adjusted operating performance scaled by assets from Year -1 to Year +4. Standardized beta coefficients and robust standard errors are used. t-statistics are in parentheses. Announcement years and industries are controlled. $^ { \star } p < 0 . 1 , ^ { \star \star } p < 0 . 0 5 , ^ { \star \star \star } p < 0 . 0 1$ Restructuring includes general restructuring of the business/operations and/or raise cash through disposal. Expansion includes expand presence in new geographical regions, expand presence in new/foreign markets, allow offering new products and services, and strengthen existing operations/expand presence in the primary and/or secondary markets.




注：因变量为收购方非正常营业收入，以-1年至+4年按资产调整业绩调整后的经营业绩变化来衡量。使用标准化贝塔系数和稳健标准误差。 t-统计量在括号中。公告年份及行业受控。 $^ { \star } p < 0 。 1 , ^ { \star \star } p < 0 。 0 5 , ^ { \star \star \star } p < 0 。 0 1$ 重组包括业务/运营的一般重组和/或通过出售筹集现金。扩张包括扩大在新地理区域的业务，扩大在新/国外市场的业务，允许提供新产品和服务，以及加强现有业务/扩大在一级和/或二级市场的业务。


Table A5. ITD Impacts When Controlling for the Number of Modules Used to Estimate ITD




表 A5。控制用于估计 ITD 的模块数量时 ITD 的影响


<table><tr><td rowspan="2"></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td>3 or more modules</td><td>4 or more modules</td><td>5 or more modules</td><td>All 6 modules</td></tr><tr><td>Public</td><td>-0.074(-0.90)</td><td>-0.001(-0.01)</td><td>-0.004(-0.03)</td><td>-0.154(-0.93)</td></tr><tr><td>Firm size</td><td>0.036(0.43)</td><td>-0.085(-0.84)</td><td>-0.169(-1.43)</td><td>-0.202(-1.30)</td></tr><tr><td>Relative transaction size</td><td>0.061(0.75)</td><td>0.005(0.05)</td><td>-0.023(-0.19)</td><td>0.167(0.91)</td></tr><tr><td>Book leverage</td><td>-0.069(-0.66)</td><td>-0.111(-0.88)</td><td>-0.046(-0.37)</td><td>-0.070(-0.36)</td></tr><tr><td>Prior financial performance</td><td>-0.156(-0.93)</td><td>-0.160(-0.93)</td><td>-0.163(-0.82)</td><td>-0.149(-0.72)</td></tr><tr><td>Prior M&amp;A experience</td><td>-0.060(-0.80)</td><td>-0.086(-1.06)</td><td>-0.145(-1.38)</td><td>-0.172(-1.20)</td></tr><tr><td>Prior M&amp;A performance</td><td>-0.075(-0.90)</td><td>-0.090(-1.02)</td><td>-0.028(-0.27)</td><td>-0.018(-0.12)</td></tr><tr><td>Market-to-book value of assets</td><td>0.108(0.73)</td><td>0.221(1.37)</td><td>0.244(1.19)</td><td>0.380(1.58)</td></tr><tr><td>Industry relatedness (SIC2)</td><td>-0.161*(-1.96)</td><td>-0.172*(-1.95)</td><td>-0.239**(-2.33)</td><td>-0.247*(-1.79)</td></tr><tr><td>Industry relatedness (SIC4)</td><td>-0.090(-1.15)</td><td>-0.135(-1.42)</td><td>-0.195*(-1.74)</td><td>-0.291*(-1.89)</td></tr><tr><td>Same state</td><td>0.079(1.20)</td><td>0.042(0.52)</td><td>0.033(0.32)</td><td>0.092(0.70)</td></tr><tr><td>Industry IT intensity</td><td>0.012(0.11)</td><td>0.127(1.22)</td><td>0.167(1.44)</td><td>0.287**(2.06)</td></tr><tr><td>IT distance</td><td>-0.153**(-2.13)</td><td>-0.197***(-2.82)</td><td>-0.180**(-2.00)</td><td>-0.148(-1.37)</td></tr><tr><td>R-squared</td><td>0.139</td><td>0.212</td><td>0.205</td><td>0.326</td></tr><tr><td>N</td><td>185</td><td>149</td><td>126</td><td>85</td></tr></table>




<table><tr><td rowspan="2"></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td>3个或更多模块</td><td>4个或更多模块</td><td>5个或更多模块</td><td>全部6个模块</td></tr><tr><td>公开</td><td>-0.074(-0.90)</td><td>-0.001(-0.01)</td><td>-0.004(-0.03)</td><td>-0.154(-0.93)</td></tr><tr><td>公司大小</td><td>0.036(0.43)</td><td>-0.085(-0.84)</td><td>-0.169(-1.43)</td><td>-0.202(-1.30)</td></tr><tr><td>相对交易尺寸</td><td>0.061(0.75)</td><td>0.005(0.05)</td><td>-0.023(-0.19)</td><td>0.167(0.91)</td></tr><tr><td>预订杠杆</td><td>-0.069(-0.66)</td><td>-0.111(-0.88)</td><td>-0.046(-0.37)</td><td>-0.070(-0.36)</td></tr><tr><td>过往财务状况业绩</td><td>-0.156(-0.93)</td><td>-0.160(-0.93)</td><td>-0.163(-0.82)</td><td>-0.149(-0.72)</td></tr><tr><td>先前并购经验</td><td>-0.060(-0.80)</td><td>-0.086(-1.06)</td><td>-0.145(-1.38)</td><td>-0.172(-1.20)</td></tr><tr><td>先前并购业绩</td><td>-0.075(-0.90)</td><td>-0.090(-1.02)</td><td>-0.028(-0.27)</td><td>-0.018(-0.12)</td></tr><tr><td>市净率资产</td><td>0.108(0.73)</td><td>0.221(1.37)</td><td>0.244(1.19)</td><td>0.380(1.58)</td></tr><tr><td>行业关联度(SIC2)</td><td>-0.161*(-1.96)</td><td>-0.172*(-1.95)</td><td>-0.239**(-2.33)</td><td>-0.247*(-1.79)</td></tr><tr><td>行业相关性(SIC4)</td><td>-0.090(-1.15)</td><td>-0.135(-1.42)</td><td>-0.195*(-1.74)</td><td>-0.291*(-1.89)</td></tr><tr><td>相同状态</td><td>0.079(1.20)</td><td>0.042(0.52)</td><td>0.033(0.32)</td><td>0.092(0.70)</td></tr><tr><td>行业IT强度</td><td>0.012(0.11)</td><td>0.127(1.22)</td><td>0.167(1.44)</td><td>0.287**(2.06)</td></tr><tr><td>IT距离</td><td>-0.153**(-2.13)</td><td>-0.197***(-2.82)</td><td>-0.180**(-2.00)</td><td>-0.148(-1.37)</td></tr><tr><td>R平方</td> <td>0.139</td><td>0.212</td><td>0.205</td><td>0.326</td></tr><tr><td>N</td><td>185</td><td>149</td><td>126</td><td>85</td></tr></table>


Note: The dependent variable is the acquirer's abnormal operating income measured as the change in the performance-adjusted operating performance scaled by assets from Year -1 to Year +4. Standardized beta coefficients and robust standard errors are used. t-statistics are in parentheses. Announcement years and industries are controlled. $^ { \star } p < 0 . 1 , ^ { \star \star } p < 0 . 0 5 , ^ { \star \star \star } p < 0 . 0 1$




注：因变量为收购方非正常营业收入，以-1年至+4年按资产调整业绩调整后的经营业绩变化来衡量。使用标准化贝塔系数和稳健标准误差。 t-统计量在括号中。公告年份及行业受控。 $^ { \star } p < 0 。 1 , ^ { \star \star } p < 0 。 0 5 , ^ { \star \star \star } p < 0 。 0 1$


<table><tr><td rowspan="2"></td><td colspan="3">Performance+Industry</td><td colspan="3">Performance+Industry (BV)</td><td colspan="3">Performance+Industry+Size+Geo</td><td colspan="3">No-completion rule</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td><td>(7)</td><td>(8)</td><td>(9)</td><td>(10)</td><td>(11)</td><td>(12)</td></tr><tr><td></td><td>Full sample</td><td>Operational synergy</td><td>Non-operational synergy</td><td>Full sample</td><td>Operational synergy</td><td>Non-operational synergy</td><td>Full sample</td><td>Operational synergy</td><td>Non-operational synergy</td><td>Full sample</td><td>Operational synergy</td><td>Non-operational synergy</td></tr><tr><td>Public</td><td>-0.073(-0.79)</td><td>-0.063(-0.52)</td><td>-0.075(-0.42)</td><td>-0.189**(-2.23)</td><td>-0.095(-0.84)</td><td>-0.228(-1.59)</td><td>-0.071(-0.77)</td><td>-0.142(-1.20)</td><td>0.086(0.47)</td><td>-0.032(-0.41)</td><td>0.029(0.29)</td><td>-0.120(-0.73)</td></tr><tr><td>Firm size</td><td>-0.037(-0.40)</td><td>0.028(0.22)</td><td>-0.192(-1.23)</td><td>-0.114(-1.05)</td><td>-0.249**(-2.01)</td><td>-0.216(-1.24)</td><td>0.023(0.27)</td><td>0.122(0.97)</td><td>-0.105(-0.68)</td><td>0.086(0.98)</td><td>0.140(1.20)</td><td>-0.093(-0.53)</td></tr><tr><td>Relative transaction size</td><td>0.068(0.76)</td><td>0.015(0.13)</td><td>0.093(0.67)</td><td>0.107(1.26)</td><td>0.064(0.50)</td><td>0.071(0.61)</td><td>0.111(1.16)</td><td>0.118(0.86)</td><td>0.089(0.63)</td><td>0.115(1.60)</td><td>0.167*(1.93)</td><td>0.038(0.35)</td></tr><tr><td>Book leverage</td><td>-0.051(-0.54)</td><td>-0.247**(-2.39)</td><td>0.193(1.35)</td><td>0.035(0.38)</td><td>-0.024(-0.21)</td><td>0.155(1.23)</td><td>-0.101(-0.92)</td><td>-0.183(-1.42)</td><td>-0.020(-0.10)</td><td>-0.121(-1.34)</td><td>-0.301***(-3.01)</td><td>0.072(0.48)</td></tr><tr><td>Prior financial performance</td><td>-0.128(-0.74)</td><td>-0.122(-0.65)</td><td>-0.177(-0.55)</td><td>-0.306**(-2.12)</td><td>-0.335*(-1.86)</td><td>-0.081(-0.32)</td><td>-0.301*(-1.78)</td><td>-0.292(-1.56)</td><td>-0.413(-1.18)</td><td>-0.302**(-2.33)</td><td>-0.420**(-2.54)</td><td>-0.094(-0.30)</td></tr><tr><td>Prior M&amp;A experience</td><td>-0.081(-1.01)</td><td>0.028(0.22)</td><td>-0.084(-0.55)</td><td>0.182(1.62)</td><td>0.438***(3.82)</td><td>-0.083(-0.49)</td><td>-0.133*(-1.77)</td><td>-0.074(-0.83)</td><td>-0.129(-0.84)</td><td>-0.004(-0.04)</td><td>0.007(0.06)</td><td>0.087(0.51)</td></tr><tr><td>Prior M&amp;A performance</td><td>-0.065(-0.92)</td><td>-0.127(-1.37)</td><td>-0.006(-0.04)</td><td>-0.190***(-2.86)</td><td>-0.177**(-2.01)</td><td>-0.242**(-2.48)</td><td>-0.009(-0.13)</td><td>-0.105(-1.11)</td><td>0.081(0.53)</td><td>-0.096(-1.25)</td><td>-0.182**(-2.07)</td><td>-0.071(-0.46)</td></tr><tr><td>Market-to-book value of assets</td><td>0.045(0.31)</td><td>0.014(0.09)</td><td>0.027(0.09)</td><td>0.250*(1.79)</td><td>0.179(1.18)</td><td>0.216(0.82)</td><td>0.166(1.18)</td><td>0.165(1.04)</td><td>0.178(0.54)</td><td>0.119(1.11)</td><td>0.204(1.56)</td><td>0.022(0.08)</td></tr><tr><td>Industry relatedness (SIC2)</td><td>-0.180**(-2.11)</td><td>-0.164(-1.56)</td><td>-0.154(-1.01)</td><td>-0.166**(-2.04)</td><td>-0.172(-1.64)</td><td>-0.162(-1.46)</td><td>-0.140(-1.61)</td><td>-0.102(-0.86)</td><td>-0.184(-1.51)</td><td>-0.140*(-1.74)</td><td>-0.225**(-2.27)</td><td>0.031(0.20)</td></tr><tr><td>Industry relatedness (SIC4)</td><td>-0.134(-1.58)</td><td>-0.033(-0.30)</td><td>-0.001(-0.00)</td><td>-0.057(-0.69)</td><td>-0.128(-1.29)</td><td>0.154(1.35)</td><td>-0.026(-0.30)</td><td>0.078(0.73)</td><td>0.037(0.20)</td><td>-0.102(-1.20)</td><td>-0.098(-1.00)</td><td>0.054(0.28)</td></tr><tr><td>Same state</td><td>0.117(1.61)</td><td>0.103(1.22)</td><td>-0.012(-0.08)</td><td>0.111(1.56)</td><td>0.140(1.43)</td><td>-0.114(-1.17)</td><td>0.144**(2.16)</td><td>0.151*(1.72)</td><td>0.114(0.80)</td><td>0.023(0.32)</td><td>-0.084(-1.04)</td><td>-0.026(-0.20)</td></tr><tr><td>Industry IT intensity</td><td>0.162(1.51)</td><td>0.083(0.72)</td><td>0.469**(2.34)</td><td>0.276***(2.75)</td><td>0.165(1.37)</td><td>0.695**(2.62)</td><td>0.026(0.22)</td><td>0.064(0.50)</td><td>0.098(0.44)</td><td>0.018(0.18)</td><td>-0.148(-1.28)</td><td>0.482**(2.46)</td></tr><tr><td>IT distance</td><td>-0.156*(-1.83)</td><td>-0.359***(-3.92)</td><td>0.055(0.44)</td><td>-0.137**(-2.08)</td><td>-0.216***(-2.74)</td><td>-0.070(-0.66)</td><td>-0.194**(-2.54)</td><td>-0.340***(-3.06)</td><td>-0.112(-1.07)</td><td>-0.177**(-2.35)</td><td>-0.296***(-3.53)</td><td>-0.063(-0.48)</td></tr><tr><td>R-squared</td><td>0.166</td><td>0.285</td><td>0.368</td><td>0.252</td><td>0.409</td><td>0.463</td><td>0.145</td><td>0.238</td><td>0.254</td><td>0.259</td><td>0.416</td><td>0.307</td></tr><tr><td>N</td><td>185</td><td>111</td><td>74</td><td>183</td><td>110</td><td>73</td><td>185</td><td>111</td><td>74</td><td>182</td><td>109</td><td>73</td></tr><tr><td>ITD btw. group cf.</td><td></td><td colspan="2">0.001</td><td></td><td colspan="2">0.129</td><td></td><td colspan="2">0.055</td><td></td><td colspan="2">0.051</td></tr></table>




<table><tr><td rowspan="2"></td><td colspan="3">业绩+行业</td><td colspan="3">业绩+行业 (BV)</td><td colspan="3">业绩+行业+规模+地理位置</td><td colspan="3">未完成规则</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td><td>( 7)</td><td>(8)</td><td>(9)</td><td>(10)</td><td>(11)</td><td>(12)</td></tr><tr><td></td><td>完整样本</td><td>运营协同</td><td>非运营协同</td><td>完整样本</td><td>运营协同</td><td>非运营协同</td><td>完整样本</td><td>运营协同</td><td>非运营协同</td><td>完整示例</td><td>运营协同</td><td>非运营协同效应</td></tr><tr><td>公开</td><td>-0.073(-0.79)</td><td>-0.063(-0.52)</t d><td>-0.075(-0.42)</td><td>-0.189**(-2.23)</td><td>-0.095(-0.84)</td><td>-0.22 8(-1.59)</td><td>-0.071(-0.77)</td><td>-0.142(-1.20)</td><td>0.086(0.47)</td><t d>-0.032(-0.41)</td><td>0.029(0.29)</td><td>-0.120(-0.73)</td></tr><tr><td>坚定尺寸</td><td>-0.037(-0.40)</td><td>0.028(0.22)</td><td>-0.192(-1.23)</t d><td>-0.114(-1.05)</td><td>-0.249**(-2.01)</td><td>-0.216(-1.24)</td><t d>0.023(0.27)</td><td>0.122(0.97)</td><td>-0.105(-0.68)</td><td>0.086(0 .98)</td><td>0.140(1.20)</td><td>-0.093(-0.53)</td></tr><tr><td>相对交易尺寸</td><td>0.068（0.76）</td><td>0.015（0.13）</td><td>0.093（0.67）</td><td>0.093（0.67）</td> td><td>0.107(1.26)</td><td>0.064(0.50)</td><td>0.071(0.61)</td><td> 0.111(1.16)</td><td>0.118(0.86)</td><td>0.089(0.63)</td><td>0.115(1 .60)</td><td>0.167*(1.93)</td><td>0.038(0.35)</td></tr><tr><td>预订杠杆</td><td>-0.051(-0.54)</td><td>-0.247**(-2.39)</td><td>0.193(1.35) )</td><td>0.035(0.38)</td><td>-0.024(-0.21)</td><td>0.155(1.23)</td><td>- 0.101(-0.92)</td><td>-0.183(-1.42)</td><td>-0.020(-0.10)</td><td>-0.121(- 1.34)</td><td>-0.301***(-3.01)</td><td>0.072(0.48)</td></tr><tr><td>之前金融性能</td><td>-0.128(-0.74)</td><td>-0.122(-0.65)</td><td>-0.177(-0.55) )</td><td>-0.306**(-2.12)</td><td>-0.335*(-1.86)</td><td>-0.081(-0.32)</td><t d>-0.301*(-1.78)</td><td>-0.292(-1.56)</td><td>-0.413(-1.18)</td><td>-0.302* *(-2.33)</td><td>-0.420**(-2.54)</td><td>-0.094(-0.30)</td></tr><tr><td>之前并购经验</td><td>-0.081(-1.01)</td><td>0.028(0.22)</td><td>-0.084(-0.5) 5)</td><td>0.182(1.62)</td><td>0.438***(3.82)</td><td>-0.083(-0.49)</td>< td>-0.133*(-1.77)</td><td>-0.074(-0.83)</td><td>-0.129(-0.84)</td><td>-0。 004(-0.04)</td><td>0.007(0.06)</td><td>0.087(0.51)</td></tr><tr><td>之前并购性能</td><td>-0.065(-0.92)</td><td>-0.127(-1.37)</td><td>-0.006(-0.04)< /td><td>-0.190***(-2.86)</td><td>-0.177**(-2.01)</td><td>-0.242**(-2.48)</td><t d>-0.009(-0.13)</td><td>-0.105(-1.11)</td><td>0.081(0.53)</td><td>-0.096(-1.25) )</td><td>-0.182**(-2.07)</td><td>-0.071(-0.46)</td></tr><tr><td>市场账面价值的值资产</td><td>0.045(0.31)</td><td>0.014(0.09)</td><td>0.027(0.09)</td><td>0.027(0.09)</td> td><td>0.250*(1.79)</td><td>0.179(1.18)</td><td>0.216(0.82)</td><td> 0.166(1.18)</td><td>0.165(1.04)</td><td>0.178(0.54)</td><td>0.119(1. 11)</td><td>0.204(1.56)</td><td>0.022(0.08)</td></tr><tr><td>行业相关性(SIC2)</td><td>-0.180**(-2.11)</td><td>-0.164(-1.56)</td><td>-0.154(-1.01)< /td><td>-0.166**(-2.04)</td><td>-0.172(-1.64)</td><td>-0.162(-1.46)</td><td >-0.140(-1.61)</td><td>-0.102(-0.86)</td><td>-0.184(-1.51)</td><td>-0.140*( -1.74)</td><td>-0.225**(-2.27)</td><td>0.031(0.20)</td></tr><tr><td>行业相关性(SIC4)</td><td>-0.134(-1.58)</td><td>-0.033(-0.30)</td><td>-0.001(-0.00) )</td><td>-0.057(-0.69)</td><td>-0.128(-1.29)</td><td>0.154(1.35)</td>< td>-0.026(-0.30)</td><td>0.078(0.73)</td><td>0.037(0.20)</td><td>-0.102 (-1.20)</td><td>-0.098(-1.00)</td><td>0.054(0.28)</td></tr><tr><td>相同状态</td><td>0.117(1.61)</td><td>0.103(1.22)</td><td>-0.012(-0.08)</t d><td>0.111(1.56)</td><td>0.140(1.43)</td><td>-0.114(-1.17)</td><td>0.1 44**(2.16)</td><td>0.151*(1.72)</td><td>0.114(0.80)</td><td>0.023(0.32) )</td><td>-0.084(-1.04)</td><td>-0.026(-0.20)</td></tr><tr><td>行业信息技术
强度</td><td>0.162(1.51)</td><td>0.083(0.72)</td><td>0.469**(2.34 )</td><td>0.276***(2.75)</td><td>0.165(1.37)</td><td>0.695**(2.62)</td ><td>0.026(0.22)</td><td>0.064(0.50)</td><td>0.098(0.44)</td><td>0.018 (0.18)</td><td>-0.148(-1.28)</td><td>0.482**(2.46)</td></tr><tr><td>IT距离</td><td>-0.156*(-1.83)</td><td>-0.359***(-3.92)</td><td>0.055(0.44)</td><t d>-0.137**(-2.08)</td><td>-0.216***(-2.74)</td><td>-0.070(-0.66)</td><td>-0.194**(- 2.54)</td><td>-0.340***(-3.06)</td><td>-0.112(-1.07)</td><td>-0.177**(-2.35)</td><t d>-0.296***(-3.53)</td><td>-0.063(-0.48)</td></tr><tr><td>R 平方</td><td>0.166</td> td><td>0.285</td><td>0.368</td><td>0.252</td><td>0.409</td><td>0.463</td><td>0.145< /td><td>0.238</td><td>0.254</td><td>0.259</td><td>0.416</td><td>0.307</td></tr><tr> <td>N</td><td>185</td><td>111</td><td>74</td><td>183</td><td>110</td><td>73</td><td >185</td><td>111</td><td>74</td><td>182</td><td>109</td><td>73</td></tr><tr><td>ITD顺便说一句。组比照</td><td></td><td colspan="2">0.001</td><td></td><td colspan="2">0.129</td><td></td><td colspan="2">0.055</td><td></td><td colspan="2">0.051</td></tr></table>


Note: The dependent variable is the acquirer's abnormal operating income measured as the change in the performance-adjusted operating performance scaled by assets from Year -1 to Year +4. Standardized beta coefficients and robust standard errors are used. t-statistics are in parentheses. Announcement years and industries are controlled. $^ { \star } \mathsf { p } < 0 . 1 , ^ { \star \star } \mathsf { p } < 0 . 0 5 , ^ { \star \star \star } p < 0 . 0 1$ BV(book value) indicates that a measure is scaled by the asset's book value instead of the market value. Performance+Industry chooses a comparison group of companies that share a similar performance history and operate in the same industry. Performance+Industry+Size+Geo adds the additional conditions on the firm's size and geographic location to Performance+Industry. The no-completion rule chooses a comparison group of companies that share a similar performance history, operate in the same industry, and announced (but did not) complete an acquisition during the period. The dependent variable is winsorized at the 5th and 95th percentiles.




注：因变量为收购方非正常营业收入，以-1年至+4年按资产调整业绩调整后的经营业绩变化来衡量。使用标准化贝塔系数和稳健标准误差。 t-统计量在括号中。公告年份及行业受控。 $^ { \star } \mathsf { p } < 0 。 1 , ^ { \star \star } \mathsf { p } < 0 。 0 5 , ^ { \star \star \star } p < 0 。 0 1$ BV（账面价值）表示衡量指标是根据资产的账面价值而不是市场价值来衡量的。绩效+行业选择具有相似绩效历史且在同一行业运营的公司作为比较组。绩效+行业+规模+地理位置在绩效+行业的基础上添加了有关公司规模和地理位置的附加条件。不完成规则选择具有相似业绩历史、在同一行业运营并宣布（但未）在此期间完成收购的公司进行比较。因变量在第 5 个和第 95 个百分位数处进行缩尾处理。


<table><tr><td colspan="4">Table A7. Validation For IT Distance Measure</td></tr><tr><td rowspan="2"></td><td>(1)</td><td>(2)</td><td>(3)</td></tr><tr><td>Acquirer IT distance</td><td>Acquirer IT distance</td><td>Acquirer IT distance</td></tr><tr><td>Prior M&amp;A experience</td><td>0.229***(2.77)</td><td></td><td>0.223***(2.75)</td></tr><tr><td>IT decentralization</td><td></td><td>0.118*(1.66)</td><td>0.129*(1.90)</td></tr><tr><td>Industry IT intensity</td><td>0.068(0.82)</td><td>0.092(1.07)</td><td>0.075(0.88)</td></tr><tr><td>Observations</td><td>185</td><td>177</td><td>177</td></tr></table>




<table><tr><td colspan="4">表 A7。 IT 距离测量验证</td></tr><tr><td rowspan="2"></td><td>(1)</td><td>(2)</td><td>(3)</td></tr><tr><td>收单机构 IT 距离</td><td>收单机构 IT 距离</td><td>收单机构 IT距离</td></tr><tr><td>之前的并购经历</td><td>0.229***(2.77)</td><td></td><td>0.223***(2.75)</td></tr><tr><td>IT去中心化</td><td></td><td>0.118*(1.66)</td><td>0.129*(1.90)</td></tr><tr><td>行业IT强度</td><td>0.068(0.82)</td><td>0.092(1.07)</td><td>0.075(0.88)</td></ tr><tr><td>观察值</td><td>185</td><td>177</td><td>177</td></tr></table>


Note: Standardized beta coefficients and robust standard errors are used. t-statistics are in parentheses. Announcement years and industries are controlled. $^ { \star } p < 0 . 1 , ^ { \star \star } p < 0 . 0 5 , ^ { \star \star \star } p < 0 . 0 1$




注：使用标准化贝塔系数和稳健标准误差。 t-统计量在括号中。公告年份及行业受控。 $^ { \star } p < 0 。 1 , ^ { \star \star } p < 0 。 0 5 , ^ { \star \star \star } p < 0 。 0 1$


<table><tr><td colspan="8">Table A8. IT Distance based on Unequal Weights</td></tr><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td><td>(7)</td></tr><tr><td>2x weight given to (except Model 7)</td><td>ACC</td><td>HR</td><td>CRM</td><td>SCM</td><td>BI</td><td>DBMS</td><td>Survey</td></tr><tr><td>Public</td><td>-0.079(-0.95)</td><td>-0.071(-0.86)</td><td>-0.081(-0.96)</td><td>-0.076(-0.91)</td><td>-0.074(-0.90)</td><td>-0.067(-0.81)</td><td>-0.078(-0.94)</td></tr><tr><td>Firm size</td><td>0.036(0.42)</td><td>0.031(0.37)</td><td>0.051(0.60)</td><td>0.043(0.50)</td><td>0.037(0.44)</td><td>0.025(0.30)</td><td>0.041(0.48)</td></tr><tr><td>Relative transaction size</td><td>0.059(0.73)</td><td>0.058(0.73)</td><td>0.064(0.78)</td><td>0.061(0.75)</td><td>0.061(0.76)</td><td>0.061(0.76)</td><td>0.061(0.76)</td></tr><tr><td>Book leverage</td><td>-0.065(-0.62)</td><td>-0.075(-0.72)</td><td>-0.064(-0.62)</td><td>-0.066(-0.62)</td><td>-0.068(-0.64)</td><td>-0.069(-0.66)</td><td>-0.066(-0.63)</td></tr><tr><td>Prior financial performance</td><td>-0.151(-0.89)</td><td>-0.166(-0.99)</td><td>-0.152(-0.90)</td><td>-0.149(-0.87)</td><td>-0.155(-0.92)</td><td>-0.152(-0.91)</td><td>-0.154(-0.90)</td></tr><tr><td>Prior M&amp;A experience</td><td>-0.064(-0.88)</td><td>-0.061(-0.81)</td><td>-0.058(-0.76)</td><td>-0.058(-0.76)</td><td>-0.061(-0.81)</td><td>-0.066(-0.90)</td><td>-0.060(-0.80)</td></tr><tr><td>Prior M&amp;A performance</td><td>-0.079(-0.93)</td><td>-0.068(-0.82)</td><td>-0.083(-0.98)</td><td>-0.081(-0.96)</td><td>-0.075(-0.91)</td><td>-0.067(-0.84)</td><td>-0.079(-0.94)</td></tr><tr><td>Market-to-book value of assets</td><td>0.106(0.70)</td><td>0.112(0.76)</td><td>0.100(0.67)</td><td>0.103(0.69)</td><td>0.107(0.72)</td><td>0.105(0.71)</td><td>0.106(0.71)</td></tr><tr><td>Industry relatedness (SIC2)</td><td>-0.161*(-1.94)</td><td>-0.154*(-1.89)</td><td>-0.164**(-2.00)</td><td>-0.158*(-1.93)</td><td>-0.161*(-1.96)</td><td>-0.165**(-2.01)</td><td>-0.162*(-1.97)</td></tr><tr><td>Industry relatedness (SIC4)</td><td>-0.090(-1.15)</td><td>-0.091(-1.16)</td><td>-0.088(-1.13)</td><td>-0.093(-1.19)</td><td>-0.090(-1.15)</td><td>-0.088(-1.13)</td><td>-0.090(-1.15)</td></tr><tr><td>Same state</td><td>0.079(1.17)</td><td>0.077(1.19)</td><td>0.076(1.11)</td><td>0.080(1.22)</td><td>0.078(1.19)</td><td>0.085(1.32)</td><td>0.078(1.17)</td></tr><tr><td>Industry IT intensity</td><td>0.010(0.09)</td><td>0.019(0.17)</td><td>0.001(0.01)</td><td>0.011(0.09)</td><td>0.012(0.11)</td><td>0.022(0.20)</td><td>0.008(0.07)</td></tr><tr><td>IT distance</td><td>-0.115(-1.47)</td><td>-0.176**(-2.39)</td><td>-0.126*(-1.84)</td><td>-0.126*(-1.72)</td><td>-0.147**(-2.03)</td><td>-0.200***(-2.85)</td><td>-0.130*(-1.84)</td></tr><tr><td>R-squared</td><td>0.130</td><td>0.146</td><td>0.133</td><td>0.132</td><td>0.138</td><td>0.154</td><td>0.134</td></tr><tr><td>N</td><td>185</td><td>185</td><td>185</td><td>185</td><td>185</td><td>185</td><td>185</td></tr></table>




<table><tr><td colspan="8">表 A8。基于不等权重的IT距离</td></tr><tr><td></td><td>(1)</td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td><td>(7)</td></tr><tr><td>2x权重给予（型号除外） 7)</td><td>ACC</td><td>HR</td><td>CRM</td><td>SCM</td><td>BI</td><td>DBM S</td><td>调查</td></tr><tr><td>公开</td><td>-0.079(-0.95)</td><td>- 0.071(-0.86)</td><td>-0.081(-0.96)</td><td>-0.076(-0.91)</td><td>-0.074( -0.90)</td><td>-0.067(-0.81)</td><td>-0.078(-0.94)</td></tr><tr><td>坚定尺寸</td><td>0.036(0.42)</td><td>0.031(0.37)</td><td>0.051(0.60)</td><td>0.043(0.50)< /td><td>0.037(0.44)</td><td>0.025(0.30)</td><td>0.041(0.48)</td></tr><tr><td>相对交易尺寸</td><td>0.059(0.73)</td><td>0.058(0.73)</td><td>0.064(0.78)</td><td>0.061(0.75) )</td><td>0.061(0.76)</td><td>0.061(0.76)</td><td>0.061(0.76)</td></tr><tr><td>预订杠杆</td><td>-0.065(-0.62)</td><td>-0.075(-0.72)</td><td>-0.064(-0.62)</td><td>-0.066(-0) .62)</td><td>-0.068(-0.64)</td><td>-0.069(-0.66)</td><td>-0.066(-0.63)</td></tr><tr><td>之前金融性能</td><td>-0.151(-0.89)</td><td>-0.166(-0.99)</td><td>-0.152(-0.90)</td><td>-0.149(- 0.87)</td><td>-0.155(-0.92)</td><td>-0.152(-0.91)</td><td>-0.154(-0.90)</td></tr><tr><td>之前并购经验</td><td>-0.064(-0.88)</td><td>-0.061(-0.81)</td><td>-0.058(-0.76)</td><td>-0.058(- 0.76)</td><td>-0.061(-0.81)</td><td>-0.066(-0.90)</td><td>-0.060(-0.80)</td></tr><tr><td>之前并购性能</td><td>-0.079(-0.93)</td><td>-0.068(-0.82)</td><td>-0.083(-0.98)</td><td>-0.081(-0.96) )</td><td>-0.075(-0.91)</td><td>-0.067(-0.84)</td><td>-0.079(-0.94)</td></tr><tr><td>市场账面价值的值资产</td><td>0.106(0.70)</td><td>0.112(0.76)</td><td>0.100(0.67)</td><td>0.103(0.69) </td><td>0.107(0.72)</td><td>0.105(0.71)</td><td>0.106(0.71)</td></tr><tr><td>行业相关性(SIC2)</td><td>-0.161*(-1.94)</td><td>-0.154*(-1.89)</td><td>-0.164**(-2.00)</td><td>-0.158*(-1.9) 3)</td><td>-0.161*(-1.96)</td><td>-0.165**(-2.01)</td><td>-0.162*(-1.97)</td></tr><tr><td>行业相关性(SIC4)</td><td>-0.090(-1.15)</td><td>-0.091(-1.16)</td><td>-0.088(-1.13)</td><td>-0.093(-1. 19)</td><td>-0.090(-1.15)</td><td>-0.088(-1.13)</td><td>-0.090(-1.15)</td></tr><tr><td>同上状态</td><td>0.079(1.17)</td><td>0.077(1.19)</td><td>0.076(1.11)</td><td>0.080(1.22) </td><td>0.078(1.19)</td><td>0.085(1.32)</td><td>0.078(1.17)</td></tr><tr><td>行业信息技术强度</td><td>0.010(0.09)</td><td>0.019(0.17)</td><td>0.001(0.01)</td><td>0.011( 0.09)</td><td>0.012(0.11)</td><td>0.022(0.20)</td><td>0.008(0.07)</td></tr><tr><td>IT距离</td><td>-0.115(-1.47)</td><td>-0.176**(-2.39)</td><td>-0.126*(-1.84)</td><td>-0.126*(-1.72)</td ><td>-0.147**(-2.03)</td><td>-0.200***(-2.85)</td><td>-0.130*(-1.84)</td></tr><tr><td>R 平方</td><td>0 .130</td><td>0.146</td><td>0.133</td><td>0.132</td><td>0.138</td><td>0.154</td><td>0.134</td></tr><tr><t d>N</td><td>185</td><td>185</td><td>185</td><td>185</td><td>185</td><td>185</td><td>185</td></tr></table>


Note: The dependent variable is the acquirer's abnormal operating income measured as the change in the performance-adjusted operating performance scaled by assets from Year -1 to Year +4. Standardized beta coefficients and robust standard errors are used. t-statistics are in parentheses. Announcement years and industries are controlled. $^ { \star } p < 0 . 1 , ^ { \star \star } p < 0 . 0 5 , ^ { \star \star \star } p < 0 . 0 1$ ACC: accounting software, HR: human resource software, CRM: customer relationship management software, SCM: supply chain management software, BI: business intelligence software, DBMS: database management systems.




注：因变量为收购方非正常营业收入，以-1年至+4年按资产调整业绩调整后的经营业绩变化来衡量。使用标准化贝塔系数和稳健标准误差。 t-统计量在括号中。公告年份及行业受控。 $^ { \star } p < 0 。 1 , ^ { \star \star } p < 0 。 0 5 , ^ { \star \star \star } p < 0 。 0 1$ ACC：会计软件，HR：人力资源软件，CRM：客户关系管理软件，SCM：供应链管理软件，BI：商业智能软件，DBMS：数据库管理系统。
