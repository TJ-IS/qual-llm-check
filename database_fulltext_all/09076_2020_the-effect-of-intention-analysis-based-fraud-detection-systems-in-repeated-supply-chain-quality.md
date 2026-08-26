---
otero_id: 9076
otero_key: "ETB66RE7"
title: "The effect of intention analysis-based fraud detection systems in repeated supply Chain quality inspection: A context of learning and contract"
authors: "Jiaqi Yan; Xin Li; Yani Shi; Sherry Sun; Huaiqing Wang"
year: "2020"
journal: "Information & Management"
doi: "10.1016/j.im.2019.103177"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The efect of intention analysis-based fraud detection systems in repeated supply Chain quality inspection: A context of learning and contract

Jiaqi Yan<sup>a</sup>, Xin Li<sup>b</sup>, Yani Shi<sup>c,</sup>\*, Sherry Sun<sup>d</sup>, Huaiqing Wang<sup>e</sup>

<sup>a</sup> School of Information Management, Nanjing University, Xianlin Road, Qixia District, Nanjing, China

<sup>b</sup> Department of Information Systems, College of Business, City University of Hong Kong, 83 Tat Chee Avenue, Kowloon Tong, Hong Kong

<sup>c</sup> School of Economics and Management, Southeast University, Nanjing, China

<sup>d</sup> Seattle University, United States

<sup>e</sup> Bzisland Intelligent Technology Institute

## A R T I C L E I N F O

Keywords: Decision support Fraud intention analysi Supply chain quality inspection Laboratory experiment Supply contract Deception detection Learning

## A B S T R A C T

As a result of the information asymmetry on product quality, there is a risk of unethical suppliers defrauding buyers in a supply chain. Buyers often conduct quality inspection on shipments and frame supply contracts to punish quality fraud. Due to cost concerns, buyers need to estimate the suppliers’ fraud possibilities and choose appropriate testing methods and frequencies. As suppliers’ fraud intentions depend on their cost-benefit analysis, it is possible to analyze suppliers’ fraud intention with appropriate modeling of their profit-seeking behavior. In this research, we are interested in how fraud intention analysis may afect the quality inspection process. It should be noted that quality inspection can be a repeated process, with suppliers and buyers conducting multiple rounds of transactions (including transactions with frauds) and learning about each other during the process. Their supply contracts may also afect suppliers’ profit-seeking attitude. We conduct a laboratory experiment to examine the efect of fraud intention analysis systems on inspection decision making considering the learning and contract efects. We put the experiment in the context of a dairy supply chain as a critical and interesting example application. The experiment shows that if there are no strong punitive terms for fraud in the contract fraud intention analysis can improve buyers’ decision-making eficiency after controlling the learning efect, in terms of decision time, inspection cost, and correctness of rejecting suppliers’ fraudulent shipments.

## 1. Introduction

In a supply chain, suppliers provide materials or semi-manufactured goods to buyers, i.e., manufacturers, to produce final products. The suppliers and buyers essentially form a market, in which the suppliers sell “goods” to buyers. In certain contexts, the traded goods between suppliers and buyers are credence goods, whose quality suppliers can easily judge, but it is dificult or expensive for buyers to judge the quality of the goods after purchase [1,2]. For example, in milk powder production, a milk powder manufacturer buys raw milk from dairy farmers. Whether the shipped milk was produced following the industry standard is a fact that is easily observed by farmers but dificult for manufacturers to observe. Due to the existence of information asymmetry in credence goods trading, suppliers may defraud buyers by providing unqualified shipments.

To improve the eficiency of the credence goods market, it is necessary to ensure liability [3]. Quality inspection (QI) ensures suppliers provide goods of suficient quality [4]. A major challenge in QI is to optimize the allocation of inspection resources [5], including: 1) how to sample products for inspection, known as the sampling policy problem; and 2) what kind of testing method should be used, known as the testing policy problem. Mandroli et al. [6] showed that most previous research on QI focuses on the sampling policy problem, with some recent discussions touching the testing policy problem [7,8]. The testing policy problem refers to the tradeof between cost and accuracy in selecting testing methods, as some methods cannot detect fraud behavior and more accurate testing methods are generally more expensive. Thus, it would be beneficial to choose supply chain QI testing methods based on analyzing suppliers’ defraud intention.

Considering the suppliers’ defraud intention to improve the testing policy decision, a straightforward method is to build a supplier fraud intention analysis system for decision support. Intention Analysis-based Fraud Detection System (IAFDS) refers to the decision support system (DSS) that can assess the supplier’s fraud intention by calculating the expected economic profits of suppliers in terms of their potential production or deception behaviors [9–11]. From a system design perspective, the design objective is to improve the fraud prediction performance. However, as there are many other factors that influence the impacts of information technology (IT) on supply chain performance besides its technical capabilities [12,13], how much such IAFDS deci sion support can help the supply chain performance remains an issue to be studied. Further, as the supplier–buyer relationship is a long-term relationship, the testing policy problem involves repeated interactions between suppliers and buyers. As both the supplier and the buyer experience a learning process in this repeated game, the investigation of IAFDS impacts needs to take the learning efect into consideration. However, there is a lack of literature taking a repeated fraud and detection game perspective to study IT’s impacts on supply chain QI, which leads to raise our main research question: How does the decision support for supplier fraud intention analysis impact buyers’ decision performance in a repeated game of supply chain QI?

Moreover, prior literature has highlighted the moderating role of supply partnership factors on the relationship between IT use and its efect on supply chain performance [13,14]. To examine the efects of IAFDS on supply chain QI performance, it is necessary to consider the partnership factors that may impact the efects. Among the possible contextual factors of supply partnership, we are mainly interested in the supply contract type, particularly whether the suppliers will be punished if fraud activities are identified (i.e., penalty contract). The punishment in penalty contracts is a direct economic instrument to ensure liability in the credence goods market. As shown in previous supply chain research, it significantly afects the behaviors of buyers and suppliers [15–17]. The punitive terms in penalty contracts may afect suppliers’ defrauding intention [18,19], which may, in turn, affect the efectiveness of the IAFDS. Therefore, our research is also interested in how the supply contract influences supplier fraud intention analysis’s impact on buyers’ decision performance in supply chain QI.

To understand the human factor of quality fraud in quality inspection, we follow the experiment approach from behavior economics [3] and conduct a randomized laboratory experiment. In the experiment, the suppliers and buyers conduct multiple rounds of trading so that the buyers can gradually develop their testing policy over time based on their knowledge of the supplier. In our study, we find that the IAFDS decision support can help reduce buyers’ decision time after controlling the learning efect. Under traditional (non-penalty) contracts, it can slow down the increasing inspection cost (which reflects the use of more advanced inspection methods) caused by buyer–supplier learning. It can also improve the correctness of rejecting the suppliers’ shipments under traditional contracts. We also find the moderating efect of the contract type, in that the IAFDS decision support under penalty contracts can cause an increased inspection cost and lower rejection correctness.

The contribution of the paper is two-fold. First, this study extends the QI literature from a behavioral perspective in terms of suppliers quality fraud and buyers’ decision support. We employ the experi mental method from behavior economics to investigate the role of an optimal strategy-based fraud intention analysis to detect suppliers fraud behavior. The research illustrates the significant need for behavioral analysis in dealing with the quality fraud and quality inspection problems. Second, based on the performance improvement theory (PIT), this study provides a theoretical explanation of IAFDS’s impacts on supply chain performance by putting the unit of analysis at the transaction level of a repeated quality inspection game. We observe the joint efect of guidance and motivation for the performance improvement in QI. We identify the significant impacts of DSS guidance on the buyers’ QI performance and examine the efect of motivation in contract type. Although traditional operation management (OM) studies often focus on contract type in supply chain research, this study shows the importance of formalizing decision supports and guidance in organizations.

The paper is organized in the following manner. After the introduction and literature review, we introduce the problem context and develop testable hypotheses in Section 3. Then, we explain the experiment design in Section 4 and the experiment results in Section 5. Section 6 discusses findings about buyers and suppliers. Section 7 discusses implications of our findings and the limitations of our research. We conclude with some closing thoughts and comments in Section 8.

## 2. Literature review

## 2.1. Quality inspection and supply chain quality fraud

Quality is one of the most important factors in a company’s relationship between suppliers and customers. In a supply chain, the product quality depends on not only its manufacturer but also the suppliers that ofer the raw materials. Therefore, the focus of quality management has evolved from an intra-organization level to a supply chain level [20]. Foster [21] summarized the integration of quality management and supply chain management and defined supply chain quality management as a systems-based approach that integrates supply chain partners to improve performance and achieve customer satisfaction.

QI is a basic method in quality management [22]. By checking, measuring, or testing one or more product characteristics, QI relates the results to the requirements to confirm quality compliance. In supply chain QI, products that do not comply with the specifications are rejected or returned to improve the quality. In OM literature, supply chain QI is often studied as an optimization problem, i.e., to find the mathematical solution of optimal inspection policy and/or contract design to reduce fraud. For instance, Starbird [23] used a principalagent model to examine how inspection policies influence food quality and safety. Hsieh and Liu [24] studied the QI between one supplier and one buyer, each having imperfect production and inspection processes. However, as Khan et al. [25] pointed out, most current OM models on QI largely ignore the human factors.

Considering the human factors that cause the product defects, unqualified shipments may be due to quality fraud [20,22,26,27], in which suppliers intentionally substitute or add substances in a product for the purpose of increasing the apparent value of the product and/or reducing the cost of its production [27,28]. Food supply chains are an example where quality fraud is rampant, due to the high cost of accurate food QI [29]. There are multiple examples of supply chain quality fraud in recent years, such as in dairy products [30], cereals [31], and meat [32]. From a behavioral perspective, quality fraud is caused by deliberate and economical motivation [33]. Although the supply chain QI problem has been extensively mathematically studied, this behavioral side of quality fraud has not been fully explored. There is a pressing need to extend the current scope of QI literature by conducting experimental studies to examine the fraud behaviors in QI.

## 2.2. DSS in supply chain quality inspection

IT is an essential component afecting supply chain performance. In this study, we are interested in the systems and technologies dealing with the quality fraud problem in supply chain QI. In general, there are two approaches to tackle the quality fraud problem: to improve information sharing and to improve decision making [9].

From the information sharing perspective, IT can control quality fraud by reducing information asymmetry between buyers and suppliers. There are eforts to develop such systems. For example, Lyu et al. [34] proposed to integrate RFID with quality assurance systems. Xu [35] also emphasized the role of service-oriented architecture, RFID, agent, workflow management, and the Internet of Things as enablers of real-time quality management and control in the supply chain. Information sharing platforms are built for seamless supervising of food and edible agriculture product safety [36,37].

From the decision-making perspective, the focus is to gain more insight from the collected information. For instance, Chakraborty and Tah [38] presented an advisory DSS for making QI-related decisions. Wang and Yu [39] designed a DSS combining a structure light system, data mining, and RFID technology for product QI. Recently, Chang et al. [9] proposed a decision model to assess the risk of deliberate contamination of food production facilities with a dynamic and game theory perspective.

In addition to the eforts in system development, a more important problem is how these eforts afect supply chain performance. In general, the impact of IT usage on supply chain performance has been established. For instance, Vijayasarathy [13] studied the use of generic IT, including Bar Codes, Electronic Data Interchange (EDI), electronic mail, global positioning systems, intelligent agents, etc., and found the efect of technology use in the supply chain on its performance was moderated by process innovation, partnership quality, and competitive uncertainty. Liu et al. [40] studied impacts of the connectivity, compatibility, and modularity of generic IT usage on supply chain performance. These studies have found empirical evidence of IT’s efects on supply chain economic performance and perceived benefit. However, in the specific field of quality inspection, which is one important feature of supply chains, there are limited empirical studies addressing this problem.

In this study, we focus on the quality inspection systems that play a decision-making role in organizations (i.e., DSS). Although design science studies often emphasize new systems’ improved performance, the impact of DSS on supply chains in a real context is worth studying. Table 1 summarizes the major empirical studies on decision support systems in supply chains. As we can see, when putting DSS in a supply chain context, previous studies often inspect company-level performance, whether they are focused on supply chain operations or financial characteristics. Thus, the studies tend to be formulated as a survey-based study or event study. For instance, De Oliveira et al. [41] surveyed 788 diferent companies in diferent industries on perceived benefit of using business analytics in a global supply chain context. Daneshvar Kakhki and Palvia [42] examined the relationship between business intelligence and analytics (BI&A) implementation and business performance. They used human resource data as a proxy measurement of BI&A implementation, while using the company’s financial perfor mance to indicate the outcomes of BI. Although company-level mea sures can show the impact of DSS, they do not reveal the detailed stakeholders in the use of DSS in supply chains.

Furthermore, Table 1 reveals that existing studies generally take a static view of the DSS, i.e., the process of the DSS’s impact is simplified as the overall performance [43,45,47]. For instance, Trkman et al. [43] measured performance via Likert scale questions such as “overall, the Plan process area performs very well.” Chae et al. [45] measured the performance using perceived rating as compared with major competitors. Yogev et al. [44] measured perceived operational business value such as how much customer relations were enhanced. Thus, the dy namic impacts of DSS remain unclear in an interactive Context

## 2.3. Supply contract in supply chain quality inspection

In OM studies, supply contract and QI are two major instruments to deal with quality fraud, where QI focuses on the identification stage and supply contract focuses on the punishment after identification. A supply contract is an agreement between a buyer and a supplier, which sti pulates certain terms, conditions, and commitments for the supply relationship in a fixed period [48]. A supply contract can specify penalty terms as punishment for unqualified or fraudulent products.

A number of studies have examined the efects of supply contracts in supply chain QI as it is the major instrument to directly influence the suppliers. Prior literature on contract design in supply chain management indicates that the contract mechanism can be used to control product quality, as the penalty contract may raise the bar for suppliers fraud activities [17,49]. In particular, Starbird [50] examined the efect of contracts on suppliers’ behavior in supply chain QI and showed that the reward or penalty that motivates a supplier to deliver the buyer’s target quality depended upon inspection policy. In their following series research [23,51], it is found that the efectiveness of a supply chain contract depends on the accuracy of the inspection, the cost of failing to inspect, the cost of causing a foodborne illness, and the proportion of these costs paid by the supplier [52,53]. These studies demonstrated the contract’s impacts on supply chain QI and pave the road for our study.

To study DSS’s efect on supply chain QI, it is necessary to take supply contracts into consideration. First, previous studies have shown that the relationship between IT and supply chain performance is typically moderated by relationship, partnership, and collaboration levels of suppliers and buyers [13,14]. Supply contract is a typical measure for such supply chain relationships. Second, the penalty terms may afect suppliers’ defrauding intention and thus afect the efectiveness of fraud intention analysis and the efect of DSS on suppliers.

## 3. Problem context and hypotheses development

## 3.1. Problem context

Noting the limitations of existing studies, we take quality fraud detection as the venue to extend our understanding of DSS’s impact on supply chains at a more dynamic and detailed level. For this purpose, it is beneficial to take a laboratory experiment approach, which can capture the entire process of supply chain partners’ interactions in a repeated game context.

To conduct the experiment, we take the dairy supply chain as an example application. One practical reason for choosing the dairy supply chain is because the dairy industry is a typical sector of food supply chains where many product fraud cases happen. Although the dairy supply chain has diferent domain knowledge from other industries, the decision process for dairy supply chain QI is the same as for other industries. Further, our experimental subjects were familiar with the Chinese tainted milk scandal [54] that is related to inappropriate QI in the supply chain. In this scandal, some raw milk suppliers added melamine into diluted milk for profit, which is a deception that cannot be identified by traditional testing methods. To combat such activities, it is necessary to incorporate more advanced measurements, which will incur higher cost. This notable scenario of suppliers’ deception in QI provides a foundation for subjects to fully understand the process of QI, the reason to incorporate DSS in testing policy development, and fulfill the roles played in the experiment.

Table 1  
Prior Work on DSS’s Impact on Supply Chain Management.

<table><tr><td>Studies</td><td>Focus of the DSS</td><td>Performance</td><td>Unit of Study</td><td>Process</td><td>Methodology</td></tr><tr><td>[43]</td><td>Analytical capability of DSS</td><td>Perceived effectiveness of business processes</td><td>Company</td><td>Static</td><td>Survey</td></tr><tr><td>[41]</td><td>Business analytics</td><td>Perceived supply chain performance</td><td>Company</td><td>Static</td><td>Survey</td></tr><tr><td>[44]</td><td>Business intelligence system</td><td>Operational and strategic business value</td><td>Company</td><td>Static</td><td>Survey</td></tr><tr><td>[45]</td><td>Supply chain analytics</td><td>Order fulfillment, delivery, and flexibility to change</td><td>Company</td><td>Static</td><td>Survey</td></tr><tr><td>[42]</td><td>Business intelligence and analytics</td><td>ROI, ROA, ROE, ROS, Market Share</td><td>Company</td><td>Static</td><td>Analytics based on secondary data</td></tr><tr><td>[46]</td><td>Big data analysis system</td><td>Operational, market, and financial performance</td><td>Company</td><td>Static</td><td>Delphi study</td></tr></table>

![](/api/attachments/ETB66RE7/fulltext/images/3db091eba9af07a78ccce12f0096384da2310b72a91db73cc7392066d3dfa7c0.jpg)  
Fig. 1. The Sequence of Activities in the Milk Production Game.

Fig. 1 shows the general process of the milk production game, in which the solid lines show the timeline of the game and the dashed lines show the additional information flow between steps. Each period of the game is initiated by the milk supplier, who decides whether to cheat in the milk production process given her previous experience with the buyer (rejection of delivered milk, information on previous inspections, etc.) and the contract type. Then, she selects the milk production parameters (and fake procedures, if any). When the buyer receives the milk, she decides the testing methods to use given her prediction of the supplier’s behavior and the DSS’s recommendation. She rejects the milk that fails the test. (There is a possibility for wrong decisions due to inspection errors. But we do not allow for suppliers’ appeal in the ex periment.) In this repeated game, the interest of suppliers is to get more profit by avoiding rejections and reducing production costs; the interest of buyers is to get more profit by avoiding deceptive products and reducing testing costs.

In this research, we consider two influencing factors in the process, the DSS and the supply contract. For the DSS, we apply an IAFDS to analyze the intention of suppliers. For the contract, we assume the practice of the dairy industry, which has two types of contracts: traditional contract (T) and penalty contract (P). In a traditional contract, if the buyers reject the products, the suppliers will not receive payment. In a penalty contract, if the buyers reject the products, the suppliers will be assessed penalties in addition to not receiving payment [50]. Thus, suppliers under the penalty contract risk losing more money if they deceive in milk production.

## 3.2. Theoretical basis of learning in supply chain quality inspection

As we study supply chain quality inspection in a setup of repeated game between sellers and buyers, learning is an indispensable phenomenon [3,55,56]. On the one hand, supply chain players get more familiar with the operation of transactions due to task repetition, which can improve their work performance. For example, Wright [57] empirically observed that assembly costs of airplanes decreased as workers learned from repetition. On the other hand, the players can improve their collaborations or interactions by learning their supply chain partners’ behaviors through transactions in either cooperative or noncooperative games. For instance, researchers observed improved performance in total supply chain cost [55] in the context of beer supply chain games.

We therefore leverage the PIT [58,59] in understanding the learning efects in the decision making on supply chain quality inspections. PIT suggests that the performance improvement in a worker’s repeated task is influenced by his motivation for the work and guidance on the work. In the context of this paper, the providence of IAFDS (i.e., DSS) represents the guidance on the work (for buyers), and the supply contract type (i.e., level of penalty) manipulates the motivation for buyers and suppliers to complete the tasks. In the following subsections, we argue that the efect of motivation in contract type and guidance from DSS would afect buyers’ performance in supply chain QI.

In this study, we focus on buyers’ decision performance in decision time, inspection cost (the cost of decided testing methods), and rejection correctness (whether the rejection decision is correct). Although these measures are to some extent correlated, they are common indicators of buyers’ performance in the inspection process and outcome [60]. In the process of quality inspection, choosing inspection methods is associated with cognitive load, which is reflected in decision time. The diferent inspection methods are associated with diferent inspection costs and inspection correctness.

## 3.3. DSS guidance

Generally, in the process of supply chain quality fraud, the reason for a supplier to intentionally substitute or add a substance to the product is to increase the apparent value and reduce the cost of its production for profit [27,28]. If the IAFDS provides an objective assessment of the supplier’s possible actions and expected profits in defraud options, it would alert buyers to be clear about their suppliers choices and estimate quality fraud behaviors [9–11]. According to PIT, IAFDS could play a guidance role on the work to afect buyers’ performance improvement in some measures. In specific, we argue that the DSS can improve buyers’ performance in rejection correctness and inspection cost over time.

First, we expect the IAFDS can improve buyers’ rejection correctness over time. A buyer may wrongly reject a product shipment because the buyer regards the qualified product as unqualified [61]. This is generally caused by inspection errors from using inappropriate inspection methods [62]. With the assistance of IAFDS to assess the supplier’s expected profits, the possibility of wrongly estimating suppliers’ fraud intentions may be reduced and lead buyers to choose appropriate detection methods. Over time, as buyers get familiar with the DSS prin ciples and mechanisms for supplier intention analysis, we expect that DSS buyers can improve rejection correctness.

Hypothesis 1. With the accumulation of interactions between buyers and suppliers in a traditional contract, the usage of IAFDS improves the buyer’ rejection correctness over time.

Second, we expect the IAFDS can reduce buyers’ inspection costs over time, as IAFDS guide buyers to gain competence [63] in supply chain QI. High inspection cost is caused by unnecessary inspection [64]. When the buyer notices the supplier is unethical, the buyer may gradually apply more advanced (and more expensive) inspection methods. However, without objectively evaluating the supplier’s fraud intention, buyers may overestimate the fraud intention and apply some unnecessary inspections, leading to unnecessary inspection costs. In a traditional supply contract, IAFDS plays a guidance role as buyers learn suppliers’ behavior, which reduces overreactions and may alleviate increased inspection costs over time. Therefore, we hypothesize that:

Hypothesis 2. With the accumulation of interactions between buyers and suppliers in a traditional contract, the usage of IAFDS reduces the buyer’s inspection costs over time.

Regarding the inspection time, we have two competing hypotheses. A classical perspective of DSS’s impact suggests that the IAFDS will reduce the decision time. Recent findings suggest negative impacts of DSS on decision time in some contexts. In the classic view, human decisions are usually influenced by emotions and other cognitive factors [65,66]. In potentially risky situations, people tend to spend more time on the decision [67]. Thus, a buyer would spend more decision time on quality inspection if the supplier historically has quality fraud records. Compared with human decision making, DSS analysis is emotion-free, which can lead users to improve their decision time performance [68]. From this perspective, the IAFDS’s guidance will reduce the decision time as buyers become familiar with the DSS over time:

Hypothesis 3-0. With the accumulation of interactions between buyers and suppliers, the usage of IAFDS reduces the buyer’s decision time over time.

In addition to the classical view, some recent findings suggest negative impacts of DSS on decision time in some contexts. Wan et al. [69] investigated the paradoxical nature of decision support systems, suggesting that they may increase decision time if the decision aids increase the users’ cognitive burden. They argued that the decision aids may reveal the complexity and richness of the task, which users were not aware of without DSS. The QI task shares a similar situation, as the inexperienced buyer may not fully understand the complexity in the process. Note that decision time is a less important measure in supply chain QI; experienced buyers may focus on inspection cost and rejection correctness, which are more related to the buyer’s benefit, and sacrifice decision time. Accordingly, we hypothesize an alternative hypothesis:

Hypothesis 3-1. With the accumulation of interactions between buyers and suppliers, the usage of IAFDS will increase the buyer’s decision time over time, if reducing decision time is not associated with the buyer’s incentives.

## 3.4. Supply contract motivation

In supply chains, the buyers’ motivation is to improve economic return by reducing inspection cost and avoiding acceptance of fraudu. lent shipments. In our study, the subjects’ motivation is aligned with this as they will be rewarded according to the economic performance. This motivation may be afected by the contract. In a penalty contract, the punitive terms expose suppliers to greater loss if they conduct fraudulent behavior, which may afect suppliers defrauding intention [18,19]. The supplier has to consider efects of both the contract and the quality inspection, which makes their fraud decision more complicated. According to the PIT, the additional potential loss in the penalty contract may afect the supplier’s learning in supply chain QI, which will, in turn, afect the buyer’s inspection performance.

Note that our study intends to investigate IAFDS’s impact on the quality inspection process. Thus, it is necessary to consider both the buyers’ and the sellers’ learning efects under the impact of the penalty contract and the IAFDS. Under the pressure of a stronger motivation, a supplier’s learning of the buyer’s behavior may become faster according to PIT [58,59]. If the IAFDS used by the buyer is a static system and cannot evolve with the process of the QI game, suppliers may become familiar with its prediction model and eventually change their fraud strategy. As a result, the use of IAFDS will not make a big diference in catching defrauders. On the other hand, from a buyer’s perspective, the penalty contract makes it possible to punish the supplier and get economic benefit. It increases buyers’ motivation for detecting more frauds to punish their suppliers, which provides a stronger reason for buyers to make an efort to learn, even if IAFDS is not used. In such a context, applying the (static) IAFDS may not further improve the already increased eforts. In both cases, the relative efect of IAFDS is reduced. Therefore, we argue that in the penalty contract, the IAFDS may not improve the buyer’s QI performance on the inspection costs and rejection correctness. We hypothesize that:

Hypothesis 4. The punitive versus nonpunitive contract type will moderate the efects of IAFDS on the inspection cost and rejection correctness.

## 4. Research methodology

## 4.1. Experiment settings

To test our hypotheses, we conduct an experiment with 180 post graduate students enrolled in an advanced supply chain quality management course in China. The participants are randomly paired to conduct a repeated game, in which one is assumed to be a buyer and the other is assumed to be a supplier. They were given a lecture to introduce the concepts and foundations of supply chain quality management so that they had enough knowledge to participate in the experiment. The lecture was composed of two sessions: 1) general information on supply chain quality management, and 2) the related background on the experiment. In the first session, the lecturer introduced the concepts, goals, and processes of supply chain QI. The participants learnt how to measure the product quality, as well as how to estimate and judge whether a product was qualified. The participants were cognizant of the idea of tradeof between inspection costs and inspection accuracy. The lecturer also introduced the role of DSS in QI decisions and the performance measurements for decisions, i.e., accuracy, precision, and recall. In the second session, the lecturer further used the 2008 Chinese milk scandal to introduce the milk industry and the experiment settings. All the participants were aware of the case and its significant impacts. Because the experiment system was designed according to the production and inspection process of raw milk product, the case provided significant support for the participants to understand the related background of the experiment.

We simplify a supply chain as one buyer and one seller as it is common in the dairy industry for a dominant buyer (i.e., milk powder manufacturer) to have a monopoly on the raw milk procurement in one region. Each supplier (i.e., farmer) has to do transactions with the buyer day after day, while the buyer will not abandon a supplier unless there is a severe problem. Therefore, the buyer and each supplier essentially conduct a repeated game, and the accept/reject decision on each supplier does not involve other suppliers until the supplier is blocked for repeated fraud behavior. As we focus on decisions in the production and inspection process that afect the product cost, we simplify the product delivery process and assume that there is no delivery cost.

In our experiment, we set up two manipulations: NO-DSS vs. IAFDS. NO-DSS refers to presenting static advice (such as advantages and disadvantages of each inspection method) to buyers to aid their judgment. This is a common practice used in the milk industry for decades. IAFDS refers to the use of information technologies to provide analytic aid based on a previously developed BDI-based IAFDS [11], which will be elaborated in later sections. It is possible for buyers to make wrong decisions when using the DSS, which fact all the participants were taught and recognized in the training session. In this research, we take a 2 by 2 factorial experimental design (NO-DSS vs. IAFDS and penalty contract vs. traditional contract) to investigate the efectiveness of the IAFDS on the supply chain QI under diferent contract types.

In the experiment, we also manipulate the amount of information buyers and suppliers get from each other during the production and inspection process, i.e., process transparency. If the production process is observable, the buyers know the information on cows and feed that leads to the milk production. If the inspection process is observable, the suppliers know what testing methods are used to inspect the milk. In our experiments, we control these factors to have a more realistic experiment setup.

## 4.2. Experiment parameters

## 4.2.1. Milk production and inspection parameters

In the experiments, the major connection between a supplier and a buyer is through the produced milk. In each period (round) of the game, the supplier can choose diferent options on milk production and quality fraud, which will afect the milk quality. The buyer will check the quality of (some) milk and decide whether to accept the product.

In our experiment, we implement three quality dimensions of raw milk for the buyers: protein level $( Q _ { p r o t e i n } )$ , fat level $( Q _ { f a t } ) _ { : }$ , and antibiotic level $( Q _ { a n t i b i o } )$ . In the production step, we assume the quality measures depend on the suppliers’ choice of cow, feed, and antibiotic injection. This process is expressed as the following formulas:

$$
Q _ {p r o t e i n} = (I _ {c o w}) ^ {0. 5} (I _ {f e e d}) ^ {0. 5} \lambda_ {1}
$$

$$
Q _ {f a t} = (I _ {c o w}) ^ {0. 3} (I _ {f e e d}) ^ {0. 7} \lambda_ {2}
$$

$$
Q _ {a n t i b i o} = 1 0 0 - (I _ {a n t i b i o}) \lambda_ {3}
$$

where $I _ { c o w } , I _ { f e e d } , \mathrm { a n d } I _ { a n t i b i o }$ are the suppliers’ choices on cow, feed, and antibiotic, respectively, ranging from 0 to 100. $\lambda _ { 1 } , \lambda _ { 2 } ,$ and $\lambda _ { 3 }$ are random variables representing uncertainties in the production process, ranging from 0.7 to 1. In this setup, good inputs will generally lead to highquality products and higher cost. $Q _ { a n t i b i o } $ contains a negative sign in the formula as a low antibiotic injection level $I _ { a n t i b i o }$ is preferred. Injecting antibiotics can help to improve the input of cow quality by.

$$
I _ {c o w} = \min (I _ {c o w} ^ {\prime} + I _ {a n t i b i o} \times 0. 5, 1 0 0)
$$

The suppliers can voluntarily choose whether to deceive and how to deceive. If the suppliers decide on deception, our experiments implement three ways for the suppliers to change the milk to improve the (observed) quality measures:

1) Dilution: Dilution reduces milk’s unit cost (by 20% of the original cost, as more $" \mathrm { m i l k } ^ { \prime \prime }$ is produced), increases $Q _ { a n t i b i o } ,$ and decreases $Q _ { p r o t e i n }$ and $Q _ { f a t } .$ . Each dilution operation adds a multiple of 0.8 to each of the three measures.

2) Melamine: Adding melamine can increase the level of nitrogen and deceive on $Q _ { p r o t e i n } .$ Each melamine operation adds 0.3 g melamine and increases the nitrogen value $\mathsf { A } _ { \mathrm { N } } ,$ which is a measurement of $Q _ { p r o t e i n } ,$ by 30 (if the inspection instrument cannot detect this deception) and increases cost by 0.3.

3) Butter: Adding butter can increase the butter level and deceive on $Q _ { f a t } .$ Each butter operation adds 0.3 g butter and increases the measured $Q _ { f a t }$ by 30 (if the inspection instrument cannot detect thi deception) and increases cost by 0.3.

The supplier can repeat each deception step multiple times to en force the deception.

It should be noted that the buyer cannot directly observe the real quality of milk. She will carry out a QI to decide whether to accept this product. The aforementioned deception does not always change the real-quality level. Sometimes, it can only change the observed quality by some inspection instruments. In our experiment setup, we assume the following: 1) No perfect inspection method. 2) The more accurate, the higher the cost. 3) The cheapest one is the industry standard defined by the government. In the experiments, we have three ways for buyers to inspect protein, which is the key attribute in the melamine scandal: 1) An industry standard K-method, which estimates the protein level by measuring Nitrogen value $\mathbf { A _ { N } }$ under a random error. 2) A costly method, I-method, which can observe the real protein value $Q _ { p r o t e i n }$ under a random error. 3) A medium method, F-method, which can observe the real protein value $Q _ { p r o t e i n }$ under a larger random error than the I method. In other words, if the suppliers add melamine to increase the Nitrogen value, it will bias the quality inspection using the K-method. Imethod and F-method detect such type of fraud, while I-method is more accurate (and costly) than the F-method. In the experiment, we also design two ways to measure fat and antibiotics. In the experiment environment, if an inspection method is applied, the interface will show the observation value from the inspection. We set 50 as the threshold to pass a particular test. The buyer can only reject the product if there is a value from the inspections that was below 50, as evidence of poor quality is needed to reject the shipment. The buyer can accept the product even if there is a value from the inspections that was below 50, as the buyer may attribute the reason of below-50 to inspection errors.

## 4.2.2. IAFDS treatment: a BDI-based IAFDS

The IAFDS to support the inspection decision in the experiment was built based on previous research on fraud detection systems in supply chain QI [10,11]. The IAFDS is based on the Belief–Desire–Intention (BDI) modeling techniques [70], and we designed semantics and syntax to incorporate concepts into the BDI model (i.e., primitive propositions, state, path, event, and possible worlds) to represent and organize knowledge that can be used in QI. Based on the constructed BDI model, we develop a reasoning mechanism $( \mathrm { i . e . , }$ , production rule, deception rule, payment rule, and inspection rule) to predict suppliers’ probability of providing unqualified products. It should be noted that we do not design a learning mechanism to improve the accuracy of the reasoning. We implemented this framework for the dairy industry as a decision support system to help the buyers increase inspection accuracy while reducing inspection costs. The inputs to the IAFDS include the suppliers working facilities and production materials (e.g., the status of their cows and feeds, etc.), gain and cost in the production (e.g., costs of producing product at diferent quality levels, etc.), gain and cost of the quality fraud (e.g., costs and efect of adding melamine, etc.), and basic knowledge about the QI (e.g., the quality attributes that diferent testing methods inspect, costs of inspecting products with diferent testing methods, etc.).

According to Huber [71] definition of DSS, the IAFDS provides aid at the analytic stage in the decision making. The decision model in the IAFDS will calculate the expected economic incomes of the suppliers for every possible choice and suggest the most likely behavior according to the profit-maximizing principle to the buyers. In other words, the IAFDS will analyze the supplier’s intention and present the results to the buyer to make decisions on inspection policy. We will examine the IAFDS’s impact on the decision performance of supply chain QI from the perspective of a fraud and detection repeated game.

As shown in Fig. 2, based on information collected from the supplier about products, production processes, and plants, the IAFDS will infer which behaviors the supplier would choose to maximize profits. The IAFDS is developed with Jadex, which is a BDI reasoning engine that allows for programming intelligent software agents in XML and Java [72]. The information collected along the supply chain is taken as inputs for the supplier’s knowledge $( \mathrm { i . e . } ,$ , Belief in the BDI reasoning engine, representing what the supplier knows), and we assume the supplier’s goal is to maximize his/her profit $( \mathrm { i . e . , }$ Desire in the BDI reasoning engine). With the deliberation mechanism (i.e., Rules in the BDI reasoning engine), the IAFDS can infer a supplier’s profit-maximizing behaviors (i.e., Intention as the outputs of the BDI reasoning engine).

To minimize the interface’s impact in our experiments, we make the interfaces of the two DSS scenarios the same with a “DSS” button. In the NO-DSS scenario, this button is linked to a static page presenting general advice for QI. In the DSS scenario, the button is linked to a text message stating the DSS analysis results. Fig. 3 shows an example of the messages of the NO-DSS and IAFDS scenarios in our experiments.

## 4.2.3. Penalty contract treatment

In the treatment on contract type, the subjects are given a detailed explanation about the contract setup and how they will be punished if the milk is not accepted. Note that the treatments on contracts need to be associated with price changes. In practice, penalty contracts have higher penalties on unqualified products, and prices on qualified products are also higher. Otherwise, the two contracts will have systematic diferences in expected returns, and a rational, qualified supplier would never choose a penalty contract. In this experiment, the product price in the traditional contract was set as 6.5, which means if the buyer accepted the product in the traditional contract, the supplier would get 6.5, otherwise the supplier would get 0. The product price in the penalty contract was raised to 7, and the penalty was set as 1.5, which means if the buyer accepted the product in the penalty contract, the supplier would get 7, while if the buyer rejected the product due to failing the inspection, then the supplier would be charged 1.5 as a punishment. In this setup, the diference of the expected return of qualified products under the two contracts will be $0 . 5 \times r - 1 . 5 \times ( 1 - r ) = 0$ , where r is the precision of the basic QI methods. In other words, the expected outcome of increasing price and setting penalty equals 0 on qualified products that are considered as disqualified.

![](/api/attachments/ETB66RE7/fulltext/images/9a08ea71d7b8b5430d92c103d44f0dbd94851959fa6d39f68a52bbdd7cc3b38b.jpg)  
Fig. 2. IAFDS in Supply Chain QI.

## 4.2.4. Cost and benefit analysis

To ensure experiment realism and motivate participants, they were told that they would get a certification for the course and be paid depending on their performance. We ranked their performance according to the amount of profit they earned in the experiment and ofered different levels of bonus. The average bonus for each participant was approximately 50 RMB.

The supplier’s profit was calculated by the income they received from the transaction minus their production costs. Under the traditional contract, accepted shipments will receive 6.5 units payment, and rejected shipments will receive 0. Under the penalty contract, accepted shipments will receive 7 units payment, and rejected shipments will receive -1.5 units (i.e., penalty enacted). The original production cost is the sum of costs on cow, feed, and antibiotic, in which we assume a linear relationship between the input level and the cost, as shown in Fig. 4. Next, if the supplier diluted the milk, the cost would be reduced by 20% each time due to fraud. Third, if the supplier added melamine or butter into the product, the cost will increase 0.3 units for each addition operation.

The buyer’s profit was calculated by the return from the decision minus the inspection costs. If the buyer’s decision is correct, i.e., she either accepted the qualified product or rejected the unqualified product, she will receive 4 units of return. If the decision is wrong, s/he would lose 4 units. The cost for diferent inspection methods is shown in Fig. 5, in which the industry standard methods are very cheap because of mass adoption.

The payof for the supplier and the buyer in each transaction depends on both parties’ (fraud and inspection) decisions. So, their payof can be represented as a matrix where each block in both axes, respectively, represents a strategy they can choose. Fig. 6 is an example of the payof matrix for both the traditional contract and the penalty contract. In this example, we assume the supplier used $\mathrm { I } _ { \mathrm { c o w } } = 8 0 , \mathrm { I } _ { \mathrm { f e e d } } = 8 0$ , and $\mathrm { I _ { a n t i b i o } } = 4 0$ as the production inputs and got a product with $\mathrm { Q _ { p r o t e i n } = 8 3 , \ Q _ { f a t } = 8 0 , \ Q _ { a n t i b i o } = 6 5 }$ , and a cost of 3.4. S/he could either hand in the product to the buyer or choose product fraud $( \boldsymbol { \mathrm { e . g . , } }$ 80% dilute 4 times and add 0.3 g melamine). The upper part of Fig. 6 represents a normal production, and the lower part represents the quality fraud choice. The buyer could either inspect the product with industry standard (e.g., K-method) or advanced methods $( \boldsymbol { \mathrm { e . g . , } }$ Imethod), which are represented in the x axis. Thus, for each type of contract, there are four blocks representing the three final outcomes, including acceptance of the qualified product, rejection of the disqualified product, and acceptance of the disqualified product, which lead to diferent costs and returns. For instance, if the supplier chooses normal production while the buyer chooses inspection with advanced methods under a traditional contract, the product has a high possibility to pass the inspections and be accepted by the buyer. In this case, the supplier will receive 6.5 rewards by using 3.4 production costs, which is 3.1 units of profit. However, the buyer will gain 4 units return by putting 4 units inspection cost and receive 0 profit. We focus on the DSS impacts on the decision performance and assume the DSS has already been adopted. Its marginal cost is 0 and ignored in the payof matrix. Please note that there can be various scenarios with diferent payof matrix results, depending on how they choose their actions in the experiment. Instead of providing the specific payof matrixes, we provide participants with a table of production and deception costs for diferent methods and a table of inspection method costs. Although providing suficient information for the participants to complete the experiment, this setting did not help participants become game experts, which facilitates the observation of DSS guidance on the participants’ learning in the experiment process.

![](/api/attachments/ETB66RE7/fulltext/images/5a434f9953eeb9f824555ad8ee1b2cb68659c1f8286a806aff9df9f8668364e7.jpg)  
Fig. 3. Examples of the NO-DSS and IAFDS Treatments.

<table><tr><td>Cow inputs</td><td>Cost</td><td>Feed Inputs</td><td>Cost</td><td>Antibiotic Inputs</td><td>Cost</td></tr><tr><td> $I_{cow} = 100$ </td><td>2</td><td> $I_{feed} = 100$ </td><td>2</td><td> $I_{antibio} = 0$ </td><td>0</td></tr><tr><td> $I_{cow} = 80$ </td><td>1.6</td><td> $I_{feed} = 80$ </td><td>1.6</td><td> $I_{antibio} = 40$ </td><td>0.2</td></tr><tr><td> $I_{cow} = 60$ </td><td>1.2</td><td> $I_{feed} = 60$ </td><td>1.2</td><td> $I_{antibio} = 80$ </td><td>0.3</td></tr><tr><td> $I_{cow} = 40$ </td><td>0.8</td><td> $I_{feed} = 40$ </td><td>0.8</td><td></td><td></td></tr><tr><td> $I_{cow} = 20$ </td><td>0.4</td><td> $I_{feed} = 20$ </td><td>0.4</td><td></td><td></td></tr></table>

Fig. 4. Supplier’s Cow, Feed, and Antibiotic Input Costs.

## 4.3. Experimental procedure

We take a dyad design so that one supplier has one corresponding buyer. The pairing and assignment to the treatment groups are conducted randomly, so that individual characteristics such as participants’ age, gender, experience, and skills, which could afect decision-making approaches and outcomes, were controlled. Thus, the game between supplier and buyer is simplified to focus on contracts and DSS, with many confounding factors, such as competition, being controlled. The game is repeated multiple sessions for each pair of buyers and sellers, in which we rotate whether the supplier can observe the inspection process and whether the buyer can observe the production process.

All experimental sessions followed the same protocol, and all sessions were conducted at the same laboratory. The participants received a tutorial on the experiment system and the procedure before the ex periment. They arrived at the lab at a pre-specified time and spent the first 10 min reading the experiment instructions. After all participants had a chance to read the instructions, the teachers spent 30 min introducing the experiment rules and the use of software, using PowerPoint slides to illustrate examples and formulas, and answering questions. Participants took a pre-test before transactions. The pre-test is an exam with questions related to knowledge of supply chain QI and the experiment. The participants needed to complete the pre-test correctly to be qualified to do the experiment. In addition, they performed two rounds of practice before the experiment to make sure that all the participants were familiar with the experiment system. Participants then completed approximately 12–13 periods (subject to time limit) of transactions pair by pair, generally lasting less than 60 min.

## 5. Data analysis and results

## 5.1. Control and manipulation checks

Subjects’ individual characteristics, such as age, gender, and computer experience, were controlled by randomization. Further checks indicated that no significant diferences existed among subjects in all four treatments in terms of age among suppliers $( \mathrm { F } = 1 . 2 0 9 , \mathrm { p } > 0 . 1 )$ and buyers $( \mathrm { F } = 2 . 6 6 4 , \mathrm { ~ p ~ } > \mathrm { ~ 0 . 1 ) ~ }$ , computer experience among suppliers $( \mathrm { F } = 1 . 8 1 5 , \mathrm { ~ p ~ } > \ 0 . 1 )$ and buyers $( \mathrm { F } = 1 . 8 8 6 , \mathrm { ~ p ~ } > \mathrm { ~ } 0 . 1 )$ , and perceived understanding about the knowledge of supply chain quality management among suppliers $( \mathrm { F } = 0 . 1 0 5 , ~ \mathrm { ~ p ~ } > ~ 0 . 1 )$ and buyers $( \mathrm { F } = 1 . 3 8 3 , \mathrm { ~ p ~ } > \ 0 . 1 )$ . The Kruskal–Wallis test indicated that no significant diference was evident across the treatment groups in terms of gender ratio among suppliers $( \chi ^ { 2 } = 5 . 9 5 3 , \mathrm { ~ p ~ > ~ } 0 . 1 )$ and buyers $( \chi ^ { 2 } = 0 . 4 9 2 , \mathrm { ~ p ~ > ~ } 0 . 1 )$

Manipulation checks were conducted to ensure that our manipulation of DSS and supply contracts was successful in the experiment. Subjects were asked what kind of decision support and supply contracts they had, and all subjects answered correctly.

## 5.2. Sample characteristics

After removing the subjects who did not follow our experiment rules, we have experimental results on 86 supplier–buyer pairs, with 46 pairs using traditional contracts and 40 pairs using penalty contracts. There are an equal number of pairs using DSS and not using DSS under the two types of contracts, as shown in Table 2. We annotate the four settings by two letters, N (No-DSS) or F (IAFDS) and T (traditional

<table><tr><td>Protein Inspection</td><td>Cost</td><td>Fat Inspection</td><td>Cost</td><td>Antibiotic Inspection</td><td>Cost</td><td>Fig. 5. Buyer&#x27;s Inspection Cost.</td></tr><tr><td>K-method</td><td>0.1</td><td>B-method</td><td>0.1</td><td>M-method</td><td>0.1</td><td></td></tr><tr><td>F-method</td><td>1.5</td><td>G-method</td><td>2</td><td>L-method</td><td>2</td><td></td></tr><tr><td>I-method</td><td>4</td><td></td><td></td><td></td><td></td><td></td></tr></table>

![](/api/attachments/ETB66RE7/fulltext/images/98500aa1c118c54e915198eb63c4ee42766b08a2f90e6427b6b7cb89167cebaa.jpg)  
Fig. 6. Example Payof Matrixes for Traditional Contract and Penalty Contract.

contract) or P (penalty contract).

The 86 pairs of subjects together conducted 1040 periods of trans actions. In a rotating mechanism, in 48% of the transactions, the buyers’ inspection process is observable to the suppliers. In 50% of the transactions, the production process is observable to the buyers. Table 3 reports the descriptive statistics of these transactions. As it shows, 59% of the transactions have dilution activities, 33% of transactions have added melamine, and 26% of the transactions have added butter. Overall, 68% of the transactions have at least one of the deception activities. The inspection cost is measured as the cost that the buye spent for his/her inspection activities in the transactions. We measure the decision time as the duration between the moment that the buyer received the product and the moment that the buyer decided to accept or reject the product. On average, the buyers spend 1.21 units inspection cost and 75.24 s inspection time to inspect the shipments and reject 27% of the shipments. Among the 424 transactions with disqualified shipments, the buyers correctly rejected 59% of them, which is represented by the variable of correct rejection.

## 5.3. Development of the buyers’ behavior under diferent treatments

Table 3 reports the mean and standard deviation for the average buyer behaviors in terms of inspection decision time, inspection cost (reflecting the level of inspection instrument used), and the decision correctness based on the chosen inspection. We can make some general observations on the average buyer behavior. First, the joint use of DSS and penalty contract reduces the time for the buyers to make inspection decisions. As shown in the first row of Table 3, while bringing DSS or a penalty contract individually into the game slightly reduces decision time, if both treatments are applied, the decision time would be reduced from 79 s to 64 s. Second, without treatments, buyers tend to use a higher level of inspection methods, with a high inspection cost. If a penalty contract is used, buyers tend to trust the suppliers, and their inspection cost will be reduced to a very low level (i.e., buyers use simple inspection instruments). The use of DSS will revise the tendency to overuse or underuse inspection methods and change inspection cost to a medium level. Third, the use of DSS or a penalty contract individually will improve the buyer’s rejection correctness. But jointly using them does not provide advantages in our experiment setting, which may be due to the insuficient design of the IAFDS used in our experiments.

Table 3  
Descriptive Statistics of the Dataset.

<table><tr><td>Variable</td><td>Observations</td><td>Mean</td><td>Std. Dev.</td><td>Min</td><td>Max</td></tr><tr><td rowspan="5">Dilution</td><td>Total 1040</td><td>0.59</td><td>0.49</td><td>0</td><td>1</td></tr><tr><td>N/T 275</td><td>0.63</td><td>0.48</td><td>0</td><td>1</td></tr><tr><td>F/T 275</td><td>0.75</td><td>0.43</td><td>0</td><td>1</td></tr><tr><td>N/P 246</td><td>0.52</td><td>0.50</td><td>0</td><td>1</td></tr><tr><td>F/P 244</td><td>0.42</td><td>0.50</td><td>0</td><td>1</td></tr><tr><td rowspan="5">Add Melamine</td><td>Total 1040</td><td>0.33</td><td>0.47</td><td>0</td><td>1</td></tr><tr><td>N/T 275</td><td>0.41</td><td>0.49</td><td>0</td><td>1</td></tr><tr><td>F/T 275</td><td>0.35</td><td>0.48</td><td>0</td><td>1</td></tr><tr><td>N/P 246</td><td>0.23</td><td>0.42</td><td>0</td><td>1</td></tr><tr><td>F/P 244</td><td>0.31</td><td>0.46</td><td>0</td><td>1</td></tr><tr><td rowspan="5">Add Butter</td><td>Total 1040</td><td>0.26</td><td>0.44</td><td>0</td><td>1</td></tr><tr><td>N/T 275</td><td>0.37</td><td>0.49</td><td>0</td><td>1</td></tr><tr><td>F/T 275</td><td>0.31</td><td>0.46</td><td>0</td><td>1</td></tr><tr><td>N/P 246</td><td>0.13</td><td>0.34</td><td>0</td><td>1</td></tr><tr><td>F/P 244</td><td>0.22</td><td>0.42</td><td>0</td><td>1</td></tr><tr><td rowspan="5">Deception</td><td>Total 1040</td><td>0.68</td><td>0.47</td><td>0</td><td>1</td></tr><tr><td>N/T 275</td><td>0.74</td><td>0.44</td><td>0</td><td>1</td></tr><tr><td>F/T 275</td><td>0.79</td><td>0.41</td><td>0</td><td>1</td></tr><tr><td>N/P 246</td><td>0.57</td><td>0.50</td><td>0</td><td>1</td></tr><tr><td>F/P 244</td><td>0.59</td><td>0.49</td><td>0</td><td>1</td></tr><tr><td rowspan="5">Decision Time</td><td>Total 1040</td><td>75.24</td><td>71.56</td><td>0</td><td>535</td></tr><tr><td>N/T 275</td><td>79.27</td><td>71.76</td><td>0</td><td>392</td></tr><tr><td>F/T 275</td><td>77.77</td><td>84.43</td><td>0</td><td>535</td></tr><tr><td>N/P 246</td><td>78.26</td><td>72.97</td><td>4</td><td>423</td></tr><tr><td>F/P 244</td><td>64.79</td><td>50.37</td><td>8</td><td>324</td></tr><tr><td rowspan="5">Inspection Cost</td><td>Total 1040</td><td>1.21</td><td>1.50</td><td>0</td><td>12.3</td></tr><tr><td>N/T 275</td><td>1.51</td><td>1.74</td><td>0</td><td>11.8</td></tr><tr><td>F/T 275</td><td>1.15</td><td>1.23</td><td>0</td><td>8.0</td></tr><tr><td>N/P 246</td><td>1.01</td><td>1.16</td><td>0</td><td>7.6</td></tr><tr><td>F/P 244</td><td>1.14</td><td>1.73</td><td>0</td><td>12.3</td></tr><tr><td rowspan="5">Rejected</td><td>Total 1040</td><td>0.27</td><td>0.44</td><td>0</td><td>1</td></tr><tr><td>N/T 275</td><td>0.29</td><td>0.45</td><td>0</td><td>1</td></tr><tr><td>F/T 275</td><td>0.29</td><td>0.46</td><td>0</td><td>1</td></tr><tr><td>N/P 246</td><td>0.23</td><td>0.42</td><td>0</td><td>1</td></tr><tr><td>F/P 244</td><td>0.25</td><td>0.44</td><td>0</td><td>1</td></tr><tr><td rowspan="5">Correct Rejection</td><td>Total 424</td><td>0.59</td><td>0.49</td><td>0</td><td>1</td></tr><tr><td>N/T 131</td><td>0.56</td><td>0.50</td><td>0</td><td>1</td></tr><tr><td>F/T 120</td><td>0.62</td><td>0.49</td><td>0</td><td>1</td></tr><tr><td>N/P 76</td><td>0.61</td><td>0.49</td><td>0</td><td>1</td></tr><tr><td>F/P 97</td><td>0.57</td><td>0.50</td><td>0</td><td>1</td></tr></table>

Table 2  
Subject Distribution.

<table><tr><td></td><td>No-DSS (N)</td><td>IAFDS (F)</td></tr><tr><td>Traditional Contract (T)</td><td>N/T: 23 pairs, 275 transactions</td><td>B/T: 23 pairs, 275 transactions</td></tr><tr><td>Penalty Contract (P)</td><td>N/P: 20 pairs, 246 transactions</td><td>B/P: 20 pairs, 244 transactions</td></tr></table>

![](/api/attachments/ETB66RE7/fulltext/images/4f04d68badeef68d7ee8914a391c97cf75f3b28e9e0007ddafd5c2f6f46685f6.jpg)

![](/api/attachments/ETB66RE7/fulltext/images/aaa349d35919908718727d0df70bbe834614f08c40f6c68f2d54c43fd4a392c9.jpg)

![](/api/attachments/ETB66RE7/fulltext/images/53267461a521851a1f4ad918b61a60247cca7577fd64c0dc35e86858c98094f7.jpg)  
Fig. 7. Average Inspection Cost, Decision Time, and Judgment Correctness of Buyers in Each Period.

Although Table 3 presents overall buyer behavior, it may change over time in the repeated game, where players learn the economic transactions of the game settings and get more eficient [73]. Fig. 7 shows the development of buyer behaviors in terms of decision time, inspection cost, and decision correctness. There is a clear downward trend for the buyers’ decision time. As the experiment progresses, the buyers become more familiar with their supplier and the information involved in the decision process. The downtrend shows a learning efect (Fig. 7a). For the inspection cost (Fig. 7b), after a small period to get familiar with the supplier, a buyer without DSS will increase the inspection cost (i.e., adopt more advanced inspection methods) after learning a supplier’s deception activities. Using DSS can stabilize the inspection cost and maintain a reasonable inspection method. Under a penalty contract, buyers with DSS increased the inspection cost, which may be because DSS helps buyers increase the inspection standard, leading to underestimating. Fig. 7c also shows that there is a slight upward trend on the correct judgments with DSS in the traditional contract, which shows the buyers improved their knowledge and judgment correctness. However, the performance of correct rejection with DSS fluctuates under a penalty contract. We believe this shows a substitution efect of the penalty contract with the DSS. In other words, both the penalty contract and the DSS can improve the rejection correctness; however, the penalty contract may decrease the DSS’s efect, as they may have overlap efects on the rejection correctness.

## 5.4. Estimating the efects of DSS and contract on buyers’ quality inspection

In addition to the descriptive analytics, we build regression models on the three measures to control for the alternative explanations of our results. Following practice for analyzing repeated game data, such as [56,74], we conduct panel data analysis with random efect models. In the panel data, time is periods of experiments and individuals are the supplier–buyer pairs. In the model, we employ the period of experiments as an independent variable to control the learning efect. We create interaction variables between the periods and experiment treatments (using DSS, using penalty contract, and using both treatments) to study the change of treatment efect. We employ individuallevel random efects to account for inter-group heterogeneity. We also control the efect of production and inspection process transparency, which is implemented in our experiments and not shown in the de scriptive analytics. Note that decision time, inspection cost, and rejection correctness are three related factors. One’s decision time will be afected by the last period’s detection of deception. One’s inspection cost is a result of the decision. Additionally, the final rejection correctness will depend on the use of inspection method. Thus, we add the last period’s rejection, decision time, and inspection cost into the study of the three dependent variables. As the judgment correctness variable is binary, we employ a logit model on it and employ a linear model on the other two variables.

Table 4 shows the regression results. On the inspection time measure, models 1 and 2 show that buyers’ decision times are significantly increased if the last period’s decision is rejected (due to believed dis qualification). Obviously, a supplier’s historically bad records will in crease the buyer’s suspicion. Model 1 further shows that the use of DSS will significantly reduce decision time by approximately 18.7 s, which shows the role of DSS in alleviating the decision-maker’s information overload problem. Meanwhile, the inspection time will reduce over time due to the learning efect (coeficient -7.9 and -7.4 in models 1 and 2). However, the interaction variable between period and penalty contract is positive (coeficient 1.752), i.e., the learning process for the buyers under a penalty contract is slightly slower than that under a traditional contract. This may be due to the fact that suppliers apply trickier deception means under penalty contracts and learning about such methods is more dificult.

On the inspection cost measure, i.e., the level of inspection instruments applied, models 3 and 4 in Table 4 show that the inspection cost is positively related to decision time, i.e., longer thinking leads to more advanced inspection techniques (on suspicious cases). The inspection cost will improve over time (coeficient 0.070 in model 3 and 0.092 in model 4), i.e., buyers tend to trust the suppliers less and choose more advanced testing methods over time. Furthermore, as shown in model 4, the use of DSS under a traditional contract will slow down the increase of inspection cost over time (coeficient -0.061). However, under a penalty contract, DSS would lead to more complicated instruments and a higher cost (coeficient 0.091-0.061 = 0.03). This may be due to the fact that the DSS corrects buyer’s over-trust of suppliers under a penalty contract and under-trust of suppliers under a traditional contract.

In terms of rejection correctness, models 5 and 6 both show a more advanced instrument, i.e., higher inspection cost leads to higher rejection correctness. Furthermore, in terms of contract and DSS’s joint efect, model 6 shows that the use of DSS will gradually increase rejection correctness over time (coeficient 0.164) under a traditional contract. However, it will decrease the rejection correctness over time (coeficient - $\cdot 0 . 2 3 7 + 0 . 1 6 4 { = } . 0 7 3 )$ under a penalty contract. If there is no DSS, the rejection correctness will not have a learning efect, showing that it is dificult for a buyer to learn from previous errors and improve prediction correctness if there is no DSS. The diference of DSS’s impact under diferent contracts may be due to the fitting of the DSS with the contract, i.e., whether the DSS can correctly capture and reason out suppliers’ incentives under diferent contracts.

## 6. Discussion

## 6.1. Lessons on the buyers

This study investigates the supply chain performance from the buye perspective in a buyer-dominant supply chain. The use of IAFDS and the contract type are two diferent instruments for buyers to control the product quality in the experiment setup. The buyer’s goal is to optimize the setup of the inspection process to increase the rejection correctness while reducing the inspection costs and decision time.

Table 4  
Panel Data Regression Results.

<table><tr><td rowspan="3">Models</td><td colspan="2">Y = Decision Time</td><td colspan="2">Y = Inspection Cost</td><td colspan="2">Y = Rejection Correctness</td></tr><tr><td colspan="2">Random effect</td><td colspan="2">Random effect</td><td colspan="2">Random effect</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>Penalty</td><td>-13.877(10.773)</td><td>-2.203(15.276)</td><td>-0.203(0.234)</td><td>-0.182(0.328)</td><td>0.748(0.506)</td><td>0.212(0.698)</td></tr><tr><td>DSS</td><td>-18.712*(10.741)</td><td>-7.694(14.800)</td><td>0.027(0.232)</td><td>0.056(0.317)</td><td>-0.369(0.499)</td><td>-0.841(0.681)</td></tr><tr><td>Penalty × DSS</td><td></td><td>-23.376(21.601)</td><td></td><td>-0.047(0.463)</td><td></td><td>1.079(1.016)</td></tr><tr><td>Period</td><td>-7.917***(0.906)</td><td>-7.432***(1.041)</td><td>0.070***(0.020)</td><td>0.092***(0.023)</td><td>0.088(0.055)</td><td>0.039(0.061)</td></tr><tr><td>Period × Penalty</td><td>1.752*(1.063)</td><td>0.748(1.496)</td><td>-0.004(0.022)</td><td>-0.049(0.031)</td><td>-0.085(0.068)</td><td>0.040(0.100)</td></tr><tr><td>Period × DSS</td><td>1.381(1.059)</td><td>0.415(1.471)</td><td>-0.017(0.022)</td><td>-0.061**(0.031)</td><td>0.062(0.068)</td><td>0.164*(0.092)</td></tr><tr><td>Period × Penalty × DSS</td><td></td><td>2.015(2.117)</td><td></td><td>0.091**(0.045)</td><td></td><td>-0.237*(0.140)</td></tr><tr><td>Rejectt-1</td><td>14.379***(4.229)</td><td>14.485***(4.230)</td><td></td><td></td><td></td><td></td></tr><tr><td>DecisionTime</td><td></td><td></td><td>0.005***(0.001)</td><td>0.005***(0.001)</td><td></td><td></td></tr><tr><td>InspectionCost</td><td></td><td></td><td></td><td></td><td>0.304***(0.093)</td><td>0.321***(0.094)</td></tr><tr><td>ProcessTransparency</td><td>Controlled</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>N</td><td>954</td><td>954</td><td>1040</td><td>1040</td><td>424</td><td>424</td></tr><tr><td>R-sq</td><td>0.1202</td><td>0.122</td><td>0.0728</td><td>0.0844</td><td></td><td></td></tr><tr><td>Log likelihood</td><td></td><td></td><td></td><td></td><td>-271.53312</td><td>-269.8882</td></tr></table>

(Standard errors in parentheses; \* p < 0.10, \*\* p < 0.05, \*\*\* p < 0.01).

The experiment results show that the use of IAFDS (i.e., the DSS) under a traditional contract environment brings quite obvious benefits. Introducing the system into the process can reduce decision time. In a traditional contract environment, using the system can slow down the increase of the inspection cost (inspection methods) caused by the buyer’s awareness of the supplier’s fraud activities. It can also lead to an increased correctness level for the rejection decisions, which may be due to better capturing suppliers’ fraud intention in traditional contract environments. For buyers who do not possess powers to control the contract design, bringing the supplier fraud intention analysis systems into the QI process is a great choice to control product quality.

If the buyers are not equipped with an IAFDS but have the power to implement a penalty contract, the experiment results show that that their learning curve in terms of reducing decision time is slower over time. As we discussed, suppliers under the penalty contract have less incentive to implement complicated deception methods, which complicates the buyers’ reasoning process. Implementing a penalty contract does not show any obvious impact on the inspection cost (i.e., the chosen inspection methods) or the rejection correctness. The penalty contract indeed is an efective method that can be considered by buyers due to its maintaining inspection techniques while reducing cognitive eforts.

If both an IAFDS and a penalty contract are applied, our analysis shows some complicated results. In terms of inspection cost, the use of the system tends to increase the inspection cost over time under a penalty contract. In addition, the benefit of IAFDS in increasing rejection correctness under a traditional contract disappears if a penalty contract is applied. This shows the limitation of our experimental IAFDS. It needs to be improved to specifically take penalty contracts into consideration. If the buyers want to adopt IAFDS in QI under a penalty contract, more studies and experiments are needed to ensure the fitness between the contract and IAFDS.

Overall, our study increases our understanding of buyers’ behavior in QI under the impacts of IT and management instruments. In general, the IAFDS shows potential to facilitate the inspection process from a buyer perspective. For complicated scenarios, such as under a penalty contract, the IAFDS needs to be further improved to consider suppliers reactions under the contract. The contract can be a substitute for the DSS in supply chain quality management

## 6.2. Observations on the suppliers

Although the DSS and the contract type are mainly set up for the interest of the buyers, it also afects the behavior of suppliers. Fig. 8 shows the period-by-period percentage of non-dilution deception activities by suppliers. (The dilution activities cannot be detected by the inspection methods and remain at a high level over time.) As we can see, there are diferent behaviors between traditional and penalty contracts. With traditional contracts, there is a clear learning curve, showing that suppliers gradually notice their quality fraud can be de tected and turn away from/reduce fraud. With the penalty contract, the level of fraud is low because unethical suppliers are scared away by the possible punishment. This is consistent with the literature [3] that liability has a strong efect on the eficiency of the market. In both scenarios, the impact of IAFDS on suppliers is not significant, which may be due to the fact that the use of IAFDS by buyers is not observable by the suppliers in our experiments.

## 7. Implications and limitations

## 7.1. DSS in repeated fraud detection games

As supply chain QI can be regarded as a research context of fraud detection games, this study investigates the impacts of DSS in repeated fraud detection games. Fraud detection, or deception detection, has been a topic of heated discussion in many research contexts [75–78]. Although there are some discussions on how IT can provide decision support for detecting deceptions [79–81], this study extends the stream of fraud detection research to the context of supply chain quality management and studies the role of IT/DSS in the repeated supply chain transactions as an instance of a repeated fraud detection game [82].

The research findings from this laboratory experiment show that the impacts of DSS on the human decision process in the repeated fraud detection game. The DSS can improve the detectors’ decision performance over time in a nonpunitive context. However, the DSS does not work well in a punitive context. This may be because the punitive context will expose fraud to a greater loss and thus afect the defrauding intention, while the DSS in this research context has a “static” reasoning mechanism, with no learning mechanism to improve its accuracy to reason fraud intention. The study shows the DSS’s limitation in the repeated fraud detection game with a punitive environment. As we can see from the experiment results, the penalty terms in the supply contract afected the impacts of IAFDS on supply chain QI, causing an increased inspection cost and lower rejection correctness. This tells us that the IAFDS design may need to fit the supply contract type to further improve QI efectiveness. It also highlights an important message in designing DSS for fraud detection: more attention should be paid to human learning and irrational behavior in punitive contexts.

## 7.2. Analytic aid for improving supply chain performance

Performance improvement in supply chains is the basic objective of modern operations management approaches. The learning phenomenon has been extensively studied to improve performance in many supply chain tasks [83–85]. The complexity of studying and modeling the learning behavior lies in the in-depth investigation at the unit of analysis [59]. Through the laboratory setting, this study provided an ex ample of studying the learning behavior in supply chain QI and illu strated the significant efect of analytic aid for performance improvement.

![](/api/attachments/ETB66RE7/fulltext/images/55b30cbea3ea5dff06ffcacf794f887912ebefd2cba63fa419aa3daf5b5c4aac.jpg)  
Fig. 8. Supplier Deception Percentage on Non-dilution Activities.

This study shows the importance of analytic aid for improving the performance of a multiple-objective task. Without DSS’s analytical support, we find that the buyers significantly improve their perfor mance on decision time and inspection costs. However, they may not be able to improve the more complicated objective, rejection correctness. The guidance of the IAFDS alleviates this problem and helps buyers to improve performance on inspection cost and rejection correctness.

This study observes the joint efect of guidance and motivation for performance improvement. Assisting the buyer’s task and changing the buyer’s and supplier’s motivations may substitute for each other in terms of improving the buyer’s performance in supply chain QI. Although traditional OM studies often take contract type as a subject to study in supply chain, this study shows the importance of formalizing the level of analytical support in organizations.

## 7.3. Limitations

Although our experiment tries to control many factors involved in a real QI scenario, such as the use of DSS, the contract, the process transparency, the knowledge and background of suppliers and buyers, etc., our study still leaves some factors unexamined (or simplified), such as supplier’s reputation, competition, the complicatedness of the QI process, and the design of the DSS. Compared with the real-world scenario, we have simplified the concept of a supply chain as one buyer and one seller. The performance measurements for decision time, inspection costs, and rejection correctness are also simplified according to the experimental settings. In a buyer-dominated supply chain, suppliers often have strong competition with each other and may have a reputation with the buyer. The reputation record may afect the supplier’s long-term transactions and economic benefits because the buyer may block suppliers with repeated fraud behavior. Competition will afect the suppliers’ short-term benefits because each supplier is competing against each other in the production process and overly high or low quality as compared with peers will bring competitive disadvantages. Our experiments leave these two important factors of suppliers un examined.

Another limitation of our experiment is the level of complicatedness of the QI. In our experiment, we assume relatively simple possible combinations of inspection methods (3 × 2×2 combinations). In reality, more choices may exist. There may also be constraints on the use of inspection methods. For example, in milk powder production, if too many inspection methods are applied and too much inspection time is spent, the quality of the shipped milk may change. There are many more contextual factors that should be studied in addition to the contract factor investigated in this experiment, such as the stop condition for the user study.

In this study, we use the IAFDS to conduct experiments. There may exist diferent designs of QI DSS. Although our study does not directly measure the DSS itself (examine buyer’s behavior given the DSS’s suggestions), the DSS design and performance may have an impact on the examination of the problem. It is necessary to experiment on different types of QI DSS to cross-validate the findings in this study.

## 8. Conclusion and future directions

In this paper, we examine impacts of decision supports of supplier intention analysis on supply chain QI using laboratory experiments. Following the approach in previous literature on credence goods mar kets [3], we allow the suppliers and buyers to conduct multiple rounds of transactions so that the buyers can gradually develop their testing policy based on their understanding of the suppliers’ intention with the DSS’s support. In our study, we find that DSS can help reduce the buyer’s decision time. Under traditional (nonpenalty) contracts, it can slow down the increasing inspection cost (which reflects the use of more advanced inspection methods) caused by buyer–supplier distrust. It can also improve the correctness of rejecting the suppliers’ shipments under traditional contracts. The efect of DSS under a penalty contract causes an increased inspection cost and lower rejection correctness, which may be due to the correction of buyers’ over-trust of suppliers or insuficient DSS design. In the scope of our experiment, a DSS should be considered in QI if there is a lack of strong instruments to punish fraudulent suppliers.

This study has several implications for theory and practice. First, our study highlights the significance of behavioral research in supply chain management. Although more and more operations management scholars have become interested in considering human behaviors, there is a lack of studies in behavioral operations research in the use of information systems, such as the use of DSS in QI. As many information systems studies reveal, human behavior is an important aspect in understanding information systems. Our study also suggests that examining human behavior is needed for using information systems in supply chain management.

Second, this study provides a foundation to understand the impacts of advanced information technologies on supply chain management. In the coming big data era, supply chain professionals will be inundated with information that needs to be analyzed, which provides opportunities as well as challenges for supply chain management [86]. The use of DSS in supply chains is becoming a common practice. As shown in our research, the interaction between DSS and supply chain elements evolves due to the learning of suppliers and buyers. The use of DSS also makes the QI process more eficient (in terms of reducing decision time). Developing theoretical supply chain models and predictive DSS models will both provide potential to alleviate the QI problem. This study gives evidence supporting the inclusion of DSS in supply chain setups.

Third, our research will also lead to DSS designs that will improve supply chain efectiveness. On the one hand, our empirical findings support the use of DSS in QI. On the other hand, our experiment shows possible directions to improve QI DSS for diferent types of contracts. As suppliers’ cheating incentives vary under diferent contracts, it is necessary to model such a factor in the DSS. With improved DSS, buyers may save on cost while improving supply chain efectiveness and eficiency, which will lead to a better product for our society.

In the future, we will continue our study to understand DSS’ impact on QI. First, we will extend our experiment to more realistic setups, such as to consider competition among suppliers and reputations of suppliers, which are important for people’s behavior in a credence goods market [3]. Second, we will consider other context factors in QI, such as the complexity of the QI methods. Third, we will improve the decision models of QI DSS from a human behavioral perspective. As humans may not follow the optimal strategy but instead make a reasonable choice given the limited resources, we will consider other de cision models such as fuzzy logic to mimic suppliers’ reasoning process. We will also explore the incorporation of human irrationality into the simulation or prediction of human behaviors as part of the DSS.

## Acknowledgments

This research is partially supported by a grant from the National Natural Science Foundation of China (NSFC No. 71701091 and 71701043); Research Grants Council of the Hong Kong Special Administrative Region (City U 149412); Chinese Ministry of Education Project of Humanities and Social Science (No. 17YJC870020); Fundamental Research Funds for the Central Universities (No. 2242019K40157).

## Appendix A

## The design and implementation of IAFDS

The IAFDS is based on a knowledge-based approach with the Belief–Desire–Intention (BDI) modeling techniques, characterizing a rational supplier with certain mental attitudes of belief, desire, and intention. These mental attitudes determine the supplier’s behaviors. The overall process of IAFDS consists of four components. First, it collects domain information of products, supply chain contracts, suppliers’ transaction records, testing methods and quality deception methods. Second, the information collected is formalized and organized with BDI knowledge representation fra mework. Third, knowledge reasoning rules are provided for prediction based on reasoning existing knowledge. Last, suggestions are provided to the buyers to support their decisions.

Semantics and syntax are designed in IAFDS to represent the supplier’s knowledge in a supply chain quality inspection context, such as pro positions on contract, product, inspection policy, etc. Such semantics are used together with classic BDI elements to represent the possible states of the system, including the possible world of a supplier. Reasoning rules are provided for supply chain QI, including production rule, deception rule, payment rule, and inspection rule. Based on the possible world of suppliers, the reasoning rules are combined with the classic BDI satisfaction rules to infer new knowledge about supplier behaviors. Specifically, the knowledge is organized in the forms of the belief-accessible worlds $( \mathrm { i . e . , }$ what the supplier believes to be true) and the desire-accessible worlds (i.e., what the supplier wants to happen). With the reasoning rules, the BDI engine can infer the intention-accessible worlds $( \mathrm { i . e . , }$ what the supplier may do) to connect their beliefs and desires to their intention. Among the intention accessible worlds, IAFDS identifies the most likely supplier intention and use it to provide inspection suggestions.

![](/api/attachments/ETB66RE7/fulltext/images/62d9d1f8623cb29999ff4d0acd2b04e3befd06a9ebbd813652590ff581d12854.jpg)

## Execution Procedure

The IAFDS execution procedure can adaptively update the knowledge in the belief- and desire-accessible worlds at diferent time points. It will be executed once the system is ready, and will keep on executing as it contains a repeated loop. At the beginning of the loop, the new facts of the inspection environment will be collected to update the belief-accessible world. The knowledge in the desire-accessible world is also updated with the supplier’s new goals. So, when there are updates in the knowledge bases, the procedure will be executed to the next stage to derive the knowledge in the intention-accessible world using the reasoning mechanism. If the procedure identifies that the supplier intends to take certain deceiving actions, an alert is signaled and new suggestions will be given.

## References

[1] S. Baksi, P. Bose, Credence goods, eficient labelling policies, and regulatory en forcement, Environ, Resour, Econ, (Dordr) 37 (2) (2007) 411–430.

[2] T.J. Feddersen, T.W. Gilligan, Saints and markets: activists and the supply of cre dence goods, J. Econ, Manage, Strategy 10 (1) (2001) 149–171.

[3] U. Dulleck, R. Kerschbamer, M. Sutter, The economics of credence goods: an experiment on the role of liability, verifiability, reputation, and competition, Am. Econ, Rev, 101 (2) (2011) 526

[4] T.P. Berden, A.C. Brombacher, P.C. Sander, The building bricks of product quality: an overview of some basic concepts and principles, Int. J. Prod. Econ, 67 (1) (2o00) 3-15.

[5] P.B. Chevalier, L.M. Wein, Inspection for circuit board assembly, Manage. Sci. 43 (9) (1997) 1198–1213.

[6] S.S. Mandroli, A.K. Shrivastava, Y. Ding, A survey of inspection strategy and sensor distribution studies in discrete-part manufacturing processes, Jie Trans. 38 (4) (2006) 309–328.

[7] C. Chen, J. Zhang, T. Delaurentis, Quality control in food supply chain management: an analytical model and case study of the adulterated milk incident in China, Int. J. Prod. Econ. (2013) (in press).

[8] S.A. Starbird, Testing errors, supplier segregation, and food safety, Agric. Econ. 36 (3) (2007) 325–334.

[9] Y. Chang, A.L. Erera, C.C. White, Risk assessment of deliberate contamination of food production facilities, IEEE Trans. Syst. Man Cybern. Syst. PP (99) (2015) 1–13

[10] J. Yan, X. Li, S. Sun, Y. Shi, H. Wang, A bdi modeling approach for decision support in supply chain quality inspection, IEEE Trans. Syst. Man Cybern. Syst. (2017) 1–15.

[11] J. Yan, S. Sun, H. Wang, Y. Shi, D. Hu, Decision support systems to detect quality deceptions in supply Chain quality inspections: design and experimental evaluation Internationl Conference on Information Systems, (2014).

[12] T.A. Byrd, N.W. Davidson, Examining possible antecedents of it impact on the supply chain and its efect on firm performance, Inf. Manage. 41 (2) (2003) 243–255.

[13] L.R. Vijayasarathy, An investigation of moderators of the link between technology use in the supply chain and supply chain performance, Inf. Manage. 47 (7–8) (2010) 364–371.

[14] D. Kim, S. Tamer Cavusgil, The role of information technology in supply-chain relationships: does partner criticality matter? J. Bus. Ind. Mark. 20 (4/5) (2005) 169-178.

[15] C.H. Lee, B.-D. Rhee, T.C.E. Cheng, Quality uncertainty and quality-compensation contract for supply chain coordination, Eur, J. Oper, Res, 228 (3) (2013) 582–591.

[16] D.J. Reyniers. C.S. Tapiero. Contract design and the control of quality in a con: flictual environment, Eur, J. Oper, Res, 82 (2) (1995) 373–382

[17]. L. Zhu. J. You. Moral hazard strategy and quality contract design in a two-echelon supply chain, J. Syst. Sci. Syst. Eng. 20 (1) (2011) 70–86.

[18] C.A. Holt, S.K. Laury, Risk aversion and incentive efects, Am. Econ. Rev. 92 (5)

(2002) 1644–1655.

[19] J.W. Pratt, Risk aversion in the small and in the large, Econom.: J. Econom. Soc. (1964) 122–136.

[20] C.J. Robinson, M.K. Malhotra, Defining the concept of supply chain quality management and its relevance to academic and industrial practice, Int. J. Prod. Econ. 96 (3) (2005) 315–337.

[21] S.T. Foster, Towards an understanding of supply chain quality management, J. Oper. Manage. 26 (4) (2008) 461–467.

[22] A. Mitra, Fundamentals of Quality Control and Improvement, John Wiley & Sons, 2016.

[23] S.A. Starbird, Moral hazard, inspection policy, and food safety, Am. J. Agric. Econ. 87 (1) (2005) 15–27.

[24] C.-C. Hsieh, Y.-T. Liu, Quality investment and inspection policy in a supplier–ma nufacturer supply chain, Eur. J. Oper. Res. 202 (3) (2010) 717–729.

[25] M. Khan, M.Y. Jaber, A.-R. Ahmad, An integrated supply chain model with errors in quality inspection and learning in production, Omega 42 (1) (2014) 16–24.

[26] C. Chen, J. Zhang, T. Delaurentis, Quality control in food supply chain management: an analytical model and case study of the adulterated milk incident in China, Int. J. Prod. Econ, 152 (2014) 188–199

[27] L. Manning, R. Smith, J.M. Soon, Developing an organizational typology of criminals in the meat supply chain, Food Policy 59 (2016) 44–54.

[28] J. Spink, D.C. Moyer, H. Park, J.A. Heinonen, Defining the types of counterfeiters, counterfeiting, and ofender organizations, Crime Sci. 2 (1) (2013) 1.

[29] P. Shears, Food Fraud-a current issue but an old problem, Br. Food J. 112 (2) (2010) 198-213.

[30] H. Deelstra, D.T. Burns, M. Walker, The adulteration of food, lessons from the past, with reference to butter, margarine and fraud, Eur. Food Res. Technol. 239 (5) (2014) 725–744.

[31] N. Pegels, I. González, T. García, R. Martín, Authenticity testing of wheat, barley, rve and oats in food and feed market samples by real-time Pcr assays. LWT-Food Sci Technol. 60 (2) (2015) 867–875.

[32] K. Nakyinsige, Y.B.C. Man, A.Q. Sazili, Halal authenticity issues in meat and meat products, Meat Sci. 91 (3) (2012) 207–214.

[33] J.C. Moore, J. Spink, M. Lipp, Development and application of a database of food ingredient fraud and economically motivated adulteration from 1980 to 2010, J. Food Sci. 77 (4) (2012) R118–R126.

[34] J. Lyu Jr, S.-Y. Chang, T.-L. Chen, Integrating rfid with quality assurance system–Framework and applications, Expert Syst. Appl. 36 (8) (2009) 10877-10882.

[35] L.D. Xu, Information architecture for supply chain quality management, Int. J. Prod. Res. 49 (1) (2011) 183–198.

[36] W.-w. Gai, S.-h. Zhang, K.-f. Liu, Research on information sharing platform for seamless supervising of food safety, electric information and control engineering (ICEICE), 2011 International Conference on: IEEE, (2011), pp. 1635–1638.

[37] J. Zhang, X. Zhang, L. Dediu, C. Victor, Review of the current application of fingerprinting allowing detection of food adulteration and fraud in China, Food Control 22 (8) (2011) 1126–1135.

[38] S. Chakraborty, D. Tah, Real time statistical process advisor for efective quality control, Decis. Support Syst. 42 (2) (2006) 700–711.

[39] K. Wang, Q. Yu, Product quality inspection combining with structure light system, data mining and Rfid technology. Digital Product and Process Development Systems, Springer. 2013, pp. 205–220.

[40] H. Liu. W. Ke. K.K. Wei, Z. Hua, The impact of it capabilities on firm performance: the mediating roles of absorptive capacity and supply chain agility. Decis. Support Syst. 54 (3) (2013) 1452–1462.

[41] M.P.V. De Oliveira, K. McCormack, P. Trkman, Business analytics in supply chains–the contingent efect of business process maturity, Expert Syst. Appl. 39 (5) (2012) 5488–5498.

[42] M. Daneshvar Kakhki, P. Palvia, Efect of business intelligence and analytics on business performance, Twenty-Second Americas Conference on Information Systems (2016).

[43] P. Trkman. K. McCormack, M.P.V. de Oliveira, M.B. Ladeira, The impact of business analytics on supply chain performance, Decis, Support Syst, 49 (3) (2010) 318–327.

[44] N. Yogev, L. Fink, A. Even, How business intelligence creates value, European Conference on Information Systems, (2012), pp. 16–31.

[45] B. Chae, D. Olson, C. Sheu, The impact of supply chain analytics on operational performance: a resource-based view, Int. J. Prod. Res. 52 (16) (2014) 4695–4710.

[46] M. Brinch, J. Stentoft, J.K. Jensen, Big data and its applications in supply Chain management: findings from a delphi study, Proceedings of the 50th Hawai International Conference on System Sciences, (2017).

[47] R. Ganeshan, T. Boone, A.J. Stenger, The impact of inventory and flow planning parameters on supply chain performance: an exploratory study, Int. J. Prod. Econ. 71 (1–3) (2001).111-118

[48] M. Bansal, I. Karimi, R. Srinivasan, Optimal contract selection for the global supply and distribution of raw materials, Ind. Eng. Chem. Res. 46 (20) (2007) 6522–6539.

[49] X. Zu, H. Kaynak, An agency theory perspective on supply chain quality management, Int. J. Oper. Prod. Manage. 32 (4) (2012) 423–446.

[50] S.A. Starbird, Penalties, rewards, and inspection: provisions for quality in supply chain contracts, J. Oper. Res. Soc. 52 (1) (2001) 109–115.

[51] S.A. Starbird, Designing food safety regulations: the efect of inspection policy and penalties for noncompliance on food processor behavior, J. Agric, Resour, Econ. (2000) 616–635.

[52] S.A. Starbird, V. Amanor-Boadu, Do inspection and traceability provide incentives for food safety? J. Agric. Resour. Econ. (2006) 14–26.

[53] S.A. Starbird, V. Amanor-Boadu, Contract selectivity, food safety, and traceability, J. Agric. Food Ind. Organ. 5 (1) (2007).

[54] H. Xin, R. Stone, Chinese probe unmasks high-tech adulteration with melamine, Science 322 (5906) (2008) 1310–1311.

[55] M.K. Martin, C. Gonzalez, C. Lebiere, Learning to Make Decisions in Dynamic Environments: Act-R Plays the Beer Game), (2004)

[56] T. Neugebauer, J. Perote, U. Schmidt, M. Loos, Selfish-biased conditional cooperation: on the decline of contributions in repeated public goods experiments, J. Econ. Psychol. 30 (1) (2009) 52–60.

[57] T.P. Wright, Factors afecting the cost of airplanes, J. Aeronaut. Sci. 3 (4) (1936) 122–128.

[58] M.Y. Jaber, Learning Curves: Theory, Models, and Applications, CRC Press, 2011.

[59] J. Vits, L. Gelders, Performance improvement theory, Int. J. Prod. Econ. 77 (3) (2002) 285–298.

[60] S. Baiman, P.E. Fischer, M.V. Rajan, Information, contracting, and quality costs, Manage. Sci. 46 (6) (2000) 776–789.

[61] U. Guin, D. DiMase, M. Tehranipoor, Counterfeit integrated circuits: detection, avoidance, and the challenges ahead, J. Electron. Test. 30 (1) (2014) 9–23.

[62] W.G. Ferrell, A. Chhoker, Design of economically optimal acceptance sampling plans with inspection error, Comput, Oper, Res, 29 (10) (2002) 1283–1300.

[65] E.B. Andrade, D. Ariely, The enduring impact of transient emotions on decision making, Organ. Behav. Hum. Decis. Process. 109 (1) (2009) 1–8.

[66] E.A. Greenleaf, D.R. Lehmann, Reasons for substantial delay in consumer decision making, J. Consum. Res. 22 (2) (1995) 186–199.

[67] S.B. Sitkin, L.R. Weingart, Determinants of risky decision-making behavior: a test of the mediating role of risk perceptions and propensity. Acad. Manage. J. 38 (6) (1995) 1573–1592.

[68] P. Todd, I. Benbasat, Evaluating the impact of Dss, cognitive efort, and incentives on strategy selection, Inf. Syst. Res. 10 (4) (1999) 356–374.

[69] Y. Wan, S. Menon, A. Ramaprasad, The paradoxical nature of electronic decision aids on comparison-shopping: the experiments and analysis, J. Theor. Appl. Electron. Commer. Res. 4 (3) (2009) 80–96.

[70] A.S. Rao, M.P. Georgef, Decision procedures for bdi logics, J. Log. Comput. 8 (3) (1998) 293–343.

[71] G.P. Huber, The nature of organizational decision making and the design of decision support systems, Mis Q. (1981) 1–10.

[72] A. Pokahr, L. Braubach, W. Lamersdorf, Jadex: a Bdi reasoning engine, Multi-Agent Programming, Springer, 2005, pp. 149–174.

[73] Y.-W. Cheung, D. Friedman, Individual learning in normal form games: some laboratory results, Games Econ. Behav. 19 (1) (1997) 46–76.

[74] A. Chaudhuri, E. Sbai, Gender diferences in trust and reciprocity in repeated gift exchange games, New Zealand Econ. Pap. 45 (1-2) (2011) 81–95.

[75] M.L. Alonso-Quecuty, Deception detection and reality monitoring: a new answer to an old question, Psychol. Law: Int. Perspect. (1992) 328–332.

[76] R.J. Bolton, D.J. Hand, Statistical fraud detection: a review, Stat. Sci. (2002) 235–249.

[77] B.M. DePaulo, K. Charlton, H. Cooper, J.J. Lindsay, L. Muhlenbruck, The accuracyconfidence correlation in the detection of deception, Personal. Soc. Psychol. Rev. 1 (4) (1997) 346–357.

[78] P.A. Granhag, M. Hartwig, A new theoretical perspective on deception detection: on the psychology of instrumental mind-reading, psychology. Crime & Law 14 (3) (2008) 189–200.

[79] T.O. Meservy, M.L. Jensen, J. Kruse, J.K. Burgoon, J.F. Nunamaker, D.P. Twitchell, G. Tsechpenakis, D.N. Metaxas, Deception detection through automatic, unobtrusive analysis of nonverbal behavior. JEEE Intell. Syst. 20 (5) (2005) 36–43

[80] L. Zhou, J.K. Burgoon, J.F. Nunamaker, D. Twitchell, Automating linguistics-based cues for detecting deception in text-based asynchronous computer-mediated com: munications, Group Decis. Negot. 13 (1) (2004) 81–106.

[81] L. Zhou, J.K. Burgoon, D.P. Twitchell, T. Oin, J.F. Nunamaker Jr, A comparison of classification methods for predicting deception in computer-mediated communication, J. Manage, Inf, Syst, 20 (4) (2004) 139–166.

[82] K.E. Sip, M. Lynge, M. Wallentin, W.B. McGregor, C.D. Frith, A. Roepstorf, The production and detection of deception in an interactive game, Neuropsychologia 48 (12) (2010) 3619–3626.

[83] T. Chen, Enhancing the yield competitiveness of a semiconductor fabrication fac tory with dynamic capacity Re-Allocation, Comput. Ind. Eng. 57 (3) (2009) 931-936.

[84] E.M. Dar-El, Human Learning: From Learning Curves to Learning Organizations, Springer Science & Business Media. 2013.

[85] A.M. Jarkas, Critical investigation into the applicability of the learning curve theory to rebar fixing labor productivity, J. Constr. Eng. Manage. 136 (12) (2010) 1279–1288.

[86] M.A. Waller, S.E. Fawcett, Data science, predictive analytics, and big data: a revolution that will transform supply chain design and management, J. Bus. Logist. 34 (2) (2013) 77–84.

Jiaqi Yan is an Associate Professor and the Director of Peertech Blockchain Research Lab in the School of Information Management at Nanjing University. He got his Ph.D. degree in Information Systems from City University of Hong Kong, and a joint Ph.D. degree in Management Science and Engineering from the University of Science and Technology of China. His research interests focus on business intelligence, smart supply chain, blockchain, financial innovation and risk management. He has published papers in ACM Transactions on Management Information Systems, Decision Support Systems, Future Generation Computer Systems, IEEE Transactions on Systems, Man, and Cybernetics: Systems,

Journal of Information Systems, Expert Systems with Applicants, Financial Innovations, and various conference proceedings such as ICIS, HICSS.

Xin Li is an Associate Professor in the Department of Information Systems at the City University of Hong Kong. He received his Ph.D. in Management Information Systems from the University of Arizona. He received his Bachelor’s and Master's degrees from the Department of Automation at Tsinghua University, China. His research interests include business intelligence & knowledge discovery, social network analysis, social media, and scientometric analysis. His work has appeared in the MIS Quarterly, INFORMS Journal on Computing, Journal of Management Information Systems, Journal of the American Society for Information Science and Technology, ACM Transactions on Management Information Systems, IEEE Intelligent Systems, Bioinformatics, IEEE Transactions on Information Technology in Biomedicine, Nature Nanotechnology, IEEE Transactions on Intelligent Transportation Systems, among others, and in various conference proceedings.

Yani Shi is an Assistant Professor in the School of Economics and Management at th Southeast University. She received her Ph.D. degree in Information Systems from City University of Hong Kong, and a joint Ph.D. degree in Management Science and Engineering from the University of Science and Technology of China. Her research in terests include knowledge management, social media, and E-commerce. Her work has appeared in the International Journal of Information Management, IEEE Transactions on

Systems, Man, and Cybernetics: Systems, Journal of Global Information Management, ICIS, and various conference proceedings.

Dr. Sherry X. Sun holds a Ph.D. degree in Management and an M.S. degree in Management Information Systems from Eller College of Management, the University of Arizona, Tucson, Arizona, USA. Dr. Sun’s research deals with the construction of computational methodologies and tools for the management of enterprise information systems. She has published in academic journals such as Information Systems Research, INFORMS Journal on Computing, Journal of Management Information Systems, IEEE Transactions on Systems, Man, and Cybernetics, Information Sciences, Information Systems Frontier, and Journal of Systems and Software as well as other journals.

Huaiqing Wang was a Professor in the Department of Financial Mathematics and Financial Engineering at South University of Science and Technology of China. He is also the Honorary Dean and a Guest Professor of the School of Information Engineering, Wuhan University of Technology, China. He received his PhD from University of Manchester, UK, in 1987. Dr. Wang specializes in research of Financial Intelligence, and Intelligent Systems (such as intelligent financial systems, intelligent learning systems, business process management systems, knowledge management systems, conceptual modeling and ontology). He has published more than 70 international refereed SCI/SSCI journal articles and received more than 700 SCI citations.
