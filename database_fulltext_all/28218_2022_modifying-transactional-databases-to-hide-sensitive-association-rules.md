---
otero_id: 28218
otero_key: "K336DBU9"
title: "Modifying Transactional Databases to Hide Sensitive Association Rules"
authors: "Syam Menon; Abhijeet Ghoshal; Sumit Sarkar"
year: "2022"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.1033"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Modifying Transactional Databases to Hide Sensitive Association Rules

Syam Menon,<sup>a</sup> Abhijeet Ghoshal,<sup>b</sup> Sumit Sarkar<sup>a</sup>

<sup>a</sup> Jindal School of Management, University of Texas at Dallas, Richardson, Texas 75080; <sup>b</sup> Gies College of Business, University of Illinois Urbana–Champaign, Champaign, Illinois 61820

Contact: syam@utdallas.edu, https://orcid.org/0000-0003-1028-0862 (SM); abhi@illinois.edu, https://orcid.org/0000-0002-0165-4204 (AG); sumit@utdallas.edu, https://orcid.org/0000-0003-3045-1024 (SS)

Received: November 11, 2019

Revised: September 12, 2020; January 9, 2021

Accepted: March 21, 2021

Published Online in Articles in Advance: December 16, 2021

https://doi.org/10.1287/isre.2021.1033

Copyright: © 2021 INFORMS

Abstract. Firms have been sharing transactional data with business partners ever since electronic data interchange was introduced to the retail industry in the 1980s. The potential bene<sup>fi</sup>ts of data sharing notwithstanding, there has been continued reluctance on the part of data owners to share their data, for fear of sensitive information potentially making its way to competitors. Approaches that can help hide sensitive information could alleviate such concerns and increase the number of <sup>fi</sup>rms that are willing to share. Sensitive information in transactional databases often manifests itself in the form of association rules. Association rules can be concealed by altering transactions such that these sensitive rules stay hidden when the data are mined. The problem of hiding sensitive association rules is NP-hard, and to date, it has only been addressed via heuristic approaches. In this paper, we introduce a nonlinear integer formulation to hide sensitive association rules while max imizing the accuracy of the altered database. We then separate it into two problems: the sanitization problem, which hides sensitive association rules from a speci<sup>fi</sup>c transaction while altering the transaction as minimally as possible, and the accuracy maximization problem, which maximizes the accuracy of the altered database, given a solution to the sanitization problem. We show how the sanitization problem can be represented as an integer program and propose a heuristic based on intuition from this formulation to solve it. Next, we formulate the accuracy maximization problem as a nonlinear integer program, show how it can be linearized, and derive various results that help reduce the size of the problem to be solved. Computational experiments are conducted on real and synthetic data sets, the largest of which has 100 million transactions. Our results show that although the nonlinear integer formulations are not practical, the linearizations and problem-reduction steps make a signi<sup>fi</sup>cant impact on solvability and solution time. We also <sup>fi</sup>nd that there are substantial gains to be realized vis-a-vis existing approaches in terms of both solution quality and solu-\` tion time and that hiding the rules directly (rather than by hiding the associated itemsets) can result in signi<sup>fi</sup>cantly fewer transactions being sanitized.

History: Ram Gopal, Senior Editor; Zhengrui Jiang, Associate Editor.

Keywords: database sharing maximizing accuracy association rule hiding data quality

## 1. Introduction

Effective data governance strategies play a critical role in determining organizational success. Ladley (2012, p. 34) observes that a business case for data governance is best made by illustrating business value, which usually comes from identifying “opportunities where data governance supports business programs that want to increase revenue, lower costs, and reduce risk.” In an increasingly data-centric world, an important data governance issue is that of sharing data across business partners. A critical consideration therein is to accomplish this for mutual bene<sup>fi</sup>t without undermining the privacy concerns of the data owner (e.g., by the revelation of information deemed sensitive by the owner). This paper considers the problem of sharing transactional market basket data with business partners while hiding sensitive information.

A 2015 report from the European Union Agency for Cybersecurity (ENISA) underscores the importance of the problem being studied (Acquisto et al. 2015). It em phasizes the concept of “privacy by design,” and it provides an overview of “speci<sup>fi</sup>c identi<sup>fi</sup>ed privacy enhancing technologies : : : of special interest for the current and future big data landscape” (p. 5). The report identi<sup>fi</sup>es various privacy-preserving approaches—including those related to hiding sensitive association rules similar to that proposed in this paper—that are available to reduce the likelihood of data inference. It goes on to assert that scalable privacy-preserving data mining is among “the high-priority security and privacy issues that need to be further researched” (p. 42).

The phenomenon of data sharing is not new in itself, and there is a large body of work discussing the various bene<sup>fi</sup>ts of doing so. For example, Aviv (2002) and Aviv (2007) highlight the bene<sup>fi</sup>ts of collaborative forecasting and replenishment, and Lee et al. (2000), Chen et al. (2000), and Croson and Donohue (2003) point out that sharing transactional point-of-sale (POS) data can help reduce the bullwhip effect. The ease with which transactional data could be shared took a major step forward in 1992, when Walmart introduced Retail Link to become the <sup>fi</sup>rst retailer to deploy a retail portal (Askuity 2018). Since then, an increasing number of retailers have been sharing transactional data with their suppliers, with Home Depot (HomeDepotLink), Lowe’s (VendorDart), and Target (MerchIQ) being some prominent examples (Retail Velocity 2019). As also noted by Retail Velocity (2019), the frequency of sharing varies and can be daily, weekly, or monthly, whereas certain types of data are shared on demand. The range of sharing modes also vary from <sup>fl</sup>at <sup>fi</sup>les to access via vendor portals.

More recently, suppliers have been realizing that there is a lot more to be gained from the data being shared. Weinswig (2020) notes that retailer-supplier data sharing increases revenues signi<sup>fi</sup>cantly for both parties. In addition to inventory management bene<sup>fi</sup>ts, 93.2% of the retailers responding to their survey reported a greater than 1% increase in revenues as a result of increased shopper engagement, and 91% reported a greater than 1% increase as a result of increased sales. Over half the respondents reported revenue increases of over 4% along each of these dimensions. These are signi<sup>fi</sup>cant increases in revenue and can add up to millions of dollars for most retailers. Vendors saw similar signi<sup>fi</sup>cant increases in revenue as well. Paul Beduhn, then chief executive of<sup>fi</sup>cer of Vision Chain (a leading provider of supply chain solutions for consumer products, now called Orchestro) noted that suppliers had “started mining point-of-sale (POS) data, following the lead of top retailers that have been doing so for years” (Beduhn 2009). Indeed, many consumer goods manufacturers regularly pay to access detailed, transaction-level retailer data, to the bene<sup>fi</sup>t of both parties involved (Munves 2013). Retail Touchpoints (2017, p. 3) identi<sup>fi</sup>es collaborative merchandising strategies, targeted promotional programs, and tighter promotional effectiveness as some of the bene<sup>fi</sup>ts of supplier-retailer data sharing. They go on to provide the example of a leading retailer who discovered against conventional wisdom that “customers were more likely to purchase meat products, such as sausages, than salty snacks with their alcoholic beverages”—by allowing manufacturers to mine their data. Along the same lines, Kraft found that a retailer’s sales increased when Kraft’s salad dressings were dis played next to fresh produce (Nayar 2019).

Although retailers recognize that there are considerable gains to be made from sharing transactional data with suppliers, they are also aware of the potentially se rious adverse consequences associated with complete, unconditional data sharing. This concern is well articu lated by Konzak (2012, p. 4), who notes that several re tailers in a modern distribution management (MDM) survey were not doing so because “distributors are concerned that manufacturers will use that information to bypass the distributor and go direct. Or that manufac turers will hand off the data or leads from the data to competing distributors—something that has happened to some of the distributors who responded to the MDM survey.” The 2013 Retailer/Supplier Shared Data Study (Alaimo 2013) echoed the same concerns. The 2015 edi tion of the study (Terry 2015) noted that about a third of the retailers were still not sharing data with suppliers, and this number may not have changed much since, as the 2018 POS Data Study (Askuity 2018, p. 12) reports that only two-thirds of its respondents were “actively using POS data.” Consider the Kraft example (Nayar 2019) mentioned earlier. Once Kraft has gained this knowledge, it can replicate it with other retailers. If this had been a result of a particularly successful promotion by the retailer who shared Kraft’s data, this would have resulted in Kraft losing a trade secret, along with the associated competitive advantage and revenues. Although there are many examples of retailers mining their own data and discovering interesting relationships (like the much discussed beer-diaper example (Power 2002), for instance), there was no need to hide information in these situations as data were not being shared with anothe party. The relatively new phenomenon of suppliers mining data shared by retailers is what has made this an im portant issue of concern. The signi<sup>fi</sup>cance of the problem will only increase as more suppliers start mining such data, as will the need for effective approaches to hide sensitive information before sharing.

Market research <sup>fi</sup>rms are aware of these concerns: Weinbaum (2017) notes that transactional data sharing is a delicate subject for data owners and argues that as distributors rely on the sensitive information contained in the data to be competitive, they fear that sharing could expose them to risk in various forms. The types of risk mentioned parallel those voiced by Konzak (2012) and involve concerns about receivers (often manufacturers) using the data to sell directly to their customers, the possibility of revealing trade secrets, and an increased likelihood of the data ending up with competitors. The potential bene<sup>fi</sup>ts and privacy concerns associated with sharing data across organizations were also the topic of a recent episode of the McKinsey on AI podcast (DeLallo and Tennison 2020). It reiterated that although such sharing can have signi<sup>fi</sup>cant societal bene<sup>fi</sup>ts, <sup>fi</sup>rms remain hesitant to share because of concerns around giving up competitive advantage—indicating that the problem continues to be critically important today.

Weinbaum (2017) goes on to clarify that sharing can be mutually bene<sup>fi</sup>cial even if the data have been sanitized to remove sensitive information. In particular, he asserts that “there is no reason your channel partners cannot con<sup>fi</sup>dently provide you with some useful information without turning over their most sensitive data. By discovering a compromise that is mutually bene<sup>fi</sup>- cial, everyone has the opportunity to walk away satis-<sup>fi</sup>ed (and without feeling ‘used’).” Researchers have been aware of this opportunity for decades, and many approaches to mitigate the negative effects of sharing transactional data have been proposed (e.g., Oliveira and Zaïane 2002 and Stavropoulos et al. 2016).

Our objective in this paper is to develop a methodology to hide sensitive information that alleviates concerns related to data sharing in the context of the technique most commonly used to glean information when mining transactional data, association rules (Agrawal and Srikant 1994). The report from ENISA (Acquisto et al. 2015, p. 59) identi<sup>fi</sup>es approaches similar to that studied in this paper as being of particular interest. It points to one of the papers that initiated the stream of research on association rule hiding (Dasseni et al. 2001), noting that measures tailored to such contexts “can be applied and have been used in the case of big data.” Association rules are relationships among products that suggest that people who buy a product (or set of products) also tend to buy another product (or set of products). Such rules can be used to shape new marketing strategies and could result from natural customer purchasing behavior or from promotions run by the retailer. Some of these rules are often of strategic value to the retailer and therefore deemed sensitive.

Retailers regularly run marketing campaigns that connect items together, such as bundle promotions and recommendations. For example, Kroger’s 2016 Fact Book (Kroger 2017) states that “through analysis of shopper data … we consistently strive to understand our customers and the trends that impact them. The insights we uncover help us deliver solutions that create a valuable shopping experience” (p. 45). This approach helped them deliver over 3 billion recommendations in 2017 (Kroger 2018). They use analytics to help “marketers better understand campaign performance” (Redman 2020). That is, insights gained from their own data often drive speci<sup>fi</sup>c promotions. Any such promotion that was more successful than expected is a candidate for being deemed sensitive, as the fact that it was surprising suggests that others are unlikely to be aware of it. This does not imply that the supports or con<sup>fi</sup>dences are necessarily very high, just that they were higher than expected. Identifying rules as sensitive using this approach is relatively straight forward, as the extent of success of a promotion provides the proof directly, without any need for additional analysis.

In addition, there is an entire stream of research devoted to the identi<sup>fi</sup>cation of interesting association rules (e.g., Klemettinen et al. 1994, Silberschatz and Tuzhilin 1995, Sahar 1999, and Padmanabhan and Tuzhilin 2006) and on the bene<sup>fi</sup>ts of validating them with the help of experts (e.g., Adomavicius and Tuzhilin 2001, 2007). Various measures of “interestingness” have also been proposed in the literature. For example, Guillet and Hamilton (2007) devote many chapters to discuss interestingness in the context of association rules. These measures provide alternative ways to identify sensitive rules.

As the revelation of sensitive rules would undermine a retailer’s competitive advantage, more retailers would be willing to share transactional-level data if such sensitive information could be suppressed before sharing. From a data governance perspective, this would mitigate the risk associated with data sharing while allowing both parties to create business value through it. In this paper, we focus on the problem of hiding association rules that represent information sensitive to the owner of the data while minimizing the detrimental impact on data quality—another important dimension of data governance (Ladley 2012).

Hiding is usually achieved by selectively removing items from a carefully chosen subset of transactions such that the sensitive association rules are no longer revealed when the database is mined. In order to max imize the bene<sup>fi</sup>ts of sharing, the database should be altered as little as possible while ensuring the hiding of the sensitive rules. A transaction is said to be sani tized if the items removed result in the transaction not supporting any sensitive rule.

As mentioned earlier, data quality is very closely entwined with data governance. Effective data governance is often viewed as a vehicle to better data quality (Hankinson 2016), and companies seldom implement data governance initiatives “without the intention to improve data quality” (Askham 2014). Baesens (2018) goes a step further and suggests that data governance initiatives are often put in place for the explicit purpose of making sure that data quality is high. Redman (2016) underscores the critical nature of data quality to businesses in the title of his article: “Bad data costs the U.S. \$3 trillion per year.” The fact that the gross domestic product of the United States was about \$18 trillion when the article was written puts that number in perspective, and it emphasizes the considerable economic gains that could be realized by ensuring reliable data quality.

Accuracy has been recognized as an important aspect of data quality for a long time (e.g., Ivanov 1972). There have been books written on the importance of accuracy (e.g., Olson 2003), and it is a vital part of any data quality assurance program. du Mars (2012) notes that “data accuracy is critical in technology-driven business processes” and can have signi<sup>fi</sup>cant economic impact. Traditionally, accuracy has often been the primary focus of most data quality improvement efforts, and Wang and Strong (1996) found accuracy to be the most important data quality attribute from the 118 that were part of their survey. It is essential, therefore, to ensure that accuracy is as high as possible. These wellestablished reasons lead us to use accuracy as the measure of the quality of the altered database, as in Menon et al. (2005). Reddy and Wang (1995) de<sup>fi</sup>ned the accuracy of a relation to be the proportion of accurate tuples in the relation, where a tuple is accurate if and only if every attribute value in it is accurate. We follow this de<sup>fi</sup>nition, noting that the accuracy of the sanitized database relative to the original is the proportion of transactions that have not been altered.

In addition, accuracy does not require knowledge of the receiver’s mining parameters, unlike the other measure of quality that has been proposed in the literature—the number of nonsensitive rules that are concealed in the process of hiding the sensitive ones (Verykios et al. 2004). The mining parameters the receiver of the data plans to use are seldom shared; indeed, because of the very nature of data mining, the receivers of the data may themselves not be certain of these parameters until they have started mining the data. And even when the parameters are shared, there is no guarantee that the receiver of the data will adhere to the shared values. If the parameters used to mine the altered database are different from those assumed when the sensitive rules were hidden, not only could the number of nonsensitive rules hidden in reality be quite different from what was intended, but the data owner could be at risk for revealing sensitive rules. On the other hand, accuracy is unaffected by the receiver’s mining parameters and is immune to these risks. It is, therefore, the only measure in the literature that is appropriate when the receiver’s mining parameters are not known with certainty.

## 1.1. Contributions

One common theme across all association rule hiding research to date is that they have been heuristic based. Another is that they have all conducted experiments on relatively small databases; the largest database across all the papers on rule hiding discussed in Section 2 (Literature Review) involved 100,000 transactions. Realistic databases can have millions of transactions, and as many of these approaches do not scale up particularly well, their utility from a practical standpoint is somewhat limited. Our paper stands out from existing research on both fronts. We <sup>fi</sup>rst decompose the problem into two: the sanitization problem, to decide how to hide sensitive association rules from any given transaction, and the accuracy maximization problem, to maximize the accuracy of the altered database, given a solution to the sanitization problem. We then present results that allow for the accuracy maximization problem to be solved op timally given a sanitization approach and illustrate its effectiveness by solving problems involving very large databases (with as many as 100 million transactions), often in a few seconds. In addition, unlike some papers that do not guarantee that sensitive rules will be hidden, ours ensures that they will be.

1. We formulate the problem of maximizing the accuracy of a transactional database to be shared—after hiding sensitive association rules by selectively removing items from it—as a nonlinear integer program, and we show that it is NP-hard.

2. We separate it into two problems: one that hides sensitive association rules from a speci<sup>fi</sup>c transaction while altering the transaction as minimally as possible (the sanitization problem) and another that maximizes the accuracy of the altered database, given a solution to the sanitization problem (the accuracy maximization problem).

3. We show how the sanitization problem can be represented as an integer program. Although the problems are quite small and can be solved quickly, it may become necessary to solve them faster when the data sets involve hundreds of millions of transactions. For such situations, we develop a heuristic based on intuition from the integer programming formulation.

4. We demonstrate that the accuracy maximization problem can be formulated as another nonlinear integer program that takes as input the results from the sanitization problem.

5. We identify several structural properties that allow us to transform the nonlinear formulation into a linea one and to reduce the size of this linearized formulation.

6. We show that these transformations allow us to solve the accuracy maximization problem optimally (given a sanitization approach) by conducting extensive computational experiments on two real and three synthetic data sets, the largest of which involves 100 million transactions.

The rest of the paper is organized as follows. We discuss literature related to hiding association rules in Section 2. The exact nonlinear integer programming formulation is presented in Section 3. Section 4 motivates the need to separate the sanitization decision from the problem of maximizing accuracy, presents the integer programming formulation of the sanitization problem, develops a simple heuristic based on intuition from this formulation, and presents a nonlinear integer formulation for the accuracy maximization problem. The linearized version of the accuracy maximization problem is discussed in Section 5, along with the various propositions that help reduce the size of the eventual formulation to be solved. The computational experiments and associated results are discussed in Section 6, and Section 7 concludes.

## 2. Literature Review

Although there is a considerable amount of research on hiding sensitive information in general (e.g., Gar<sup>fi</sup>nkel et al. 2002 and Nunez et al. 2007), the techniques proposed in the context of nontransactional data are not applicable to the hiding of sensitive rules mined from transactional data. Among the earliest works involving hiding sensitive information from transactional data is that of Atallah et al. (1999), who show that many of the problems in this context are NP-hard. As a result, most approaches that have been developed to solve these problems have been heuristic based.

Research in this context falls into two broad categories, with one focusing on the hiding of sensitive itemsets (e.g., Menon et al. 2005, Lin et al. 2016, and Stavropoulos et al. 2016) and the other on hiding sensitive rules (e.g., Verykios et al. 2004, Gkoulalas-Divanis and Verykios 2006, and Cheng et al. 2016). Although some research exists on optimal approaches to hide sensitive itemsets (e.g., Menon et al. 2005 and Menon and Sarkar 2016), to our knowledge there has been no work done to date on optimal approaches to hide sensitive rules. Our paper <sup>fi</sup>lls this gap.

As our work is on hiding sensitive association rules, we focus the literature review on methods that explicitly attempt to hide rules, rather than the corresponding itemsets. As already mentioned, Atallah et al. (1999) have introduced versions of the problem involving the hiding of sensitive information. One of the earliest works to consider the hiding of rules is that of Dasseni et al. (2001), who present three algorithms to hide sensitive rules: (i) decrease rule con<sup>fi</sup>dence by increasing the support of its antecedent without affecting the support of the rule, (ii) decrease rule con<sup>fi</sup>dence by decreasing its support without affecting the support of its antecedent, and (iii) decrease rule support by removing items that are part of a rule supported by a transaction. They conduct experiments on data sets with as many as 10,000 transactions and 4 sensitive rules. Verykios et al. (2004) extend this work and provide <sup>fi</sup>ve approaches to hide rules, one of which involves the addition of items. Their experiments involve data sets with up to 100,000 transactions and 10 sensitive rules.

Since then, a large number of heuristic approaches have been proposed to hide sensitive association rules while reducing some potential side effects. These include Afshari et al. (2016) and Gopalan and Murthy (2019), who use data sets involving as many as 8,124 transactions, and Telikani and Shahbahrami (2017), who use data sets with as many as 88,162 items and 400 sensitive rules. Wu et al. (2007) present a heuristic approach to hide sensitive rules while reducing side effects. They consider data sets with as many as 25,000 transactions and 5 sensitive rules. Although their approach considers the addition of items, it trades off the number of sensitive rules hidden with the side effects generated, thereby leaving open the possibility of not hiding some sensitive rules. The same is true of Cheng et al. (2015) and Talebi and Dehkordi (2018). Cheng et al. (2015) address the problem using evolutionary multiobjective optimization and consider datas sets with as many as 88,162 transactions, whereas Talebi and Dehkordi (2018) use an electro magnetic <sup>fi</sup>eld optimization algorithm when considering data sets with as many as 8,124 transactions. The ap proach proposed by Navale and Mali (2019) also falls into this category, and it does not guarantee the hiding of sensitive rules. Telikani and Shahbahrami (2017) and Telikani et al. (2020), on the other hand, ensure that sensitive information will be hidden. Both consider databases with as many as 88,162 transactions, and whereas Telikani and Shahbahrami (2017) propose a modi<sup>fi</sup>ed border-based heuristic, Telikani et al. (2020) present heuristic approaches based on a binary arti<sup>fi</sup>cial bee colony approach. There have also been survey papers (e.g., Telikani and Shahbahrami 2018 and Zhang et al. 2019) and books (e.g., Gkoulalas-Divanis and Verykios 2006) on the topic.

It is possible for sensitive information to exist at dif ferent levels (e.g., store, regional, organizational) of an enterprise. Hao et al. (2007) consider this problem in the context of hiding sensitive item sets. Although we consider sensitive information in the centralized organizational-level database, the approach presented in this paper along with all the propositions apply to the distributed version of the rule hiding problem as well. However, that is a signi<sup>fi</sup>cantly harder problem to solve from a practical perspective, as the number of constraints increases signi<sup>fi</sup>cantly depending on the number of levels and units (e.g., stores) in each level.

Transactions can also be altered by adding items to it. However, there are signi<sup>fi</sup>cant drawbacks associated with doing so. For example, the addition of items can result in the generation of spurious frequent itemsets (as opposed to just spurious rules), which, in turn, would generate more spurious rules; this cannot happen if only item removal is considered. This is echoed by Verykios et al. (2004, p. 445), who <sup>fi</sup>nd that the only algorithm in their paper involving the addition of items resulted in the generation of “an unacceptable number of new rules.” As we discuss later, there are also various practical implications that make the addition of items undesirable, including the fact that the associated bene<sup>fi</sup>ts are likely to be low. For all these reasons, we have also focused on the removal of items in this paper—as has most research in this area. In Appendix B, we provide the formulation when adding items is considered, along with a brief discussion on the implications of doing so.

Another possibility is to eliminate transactions entirely. However, doing so is also likely to result in the generation of spurious itemsets. In addition, removing all the items in the transaction will affect other rules generated from the data set, similar to blanket sanitization (Menon and Sarkar 2007)—more itemsets, rules, and antecedents of rules would lose support, and the net effect will be more rules lost and more spurious rules generated.

## 3. The Rule Hiding Problem

The problem studied in this paper involves the removal of items from a transactional data set with minimal damage to the data while hiding a set of association rules that have been identi<sup>fi</sup>ed as sensitive to the data owner. We now make the problem de<sup>fi</sup>nition more precise and show how it can be formulated as a nonlinear integer program.

## 3.1. Relevant Notation

A database D is a set of transactions over a set of items $\mathcal { T } ,$ where a transaction $\boldsymbol { \mathcal { T } } = \left( \boldsymbol { i } , \boldsymbol { T } \right)$ is a pair with unique identi-<sup>fi</sup>er i and $T \subseteq { \mathcal { D } }$ . An itemset $j \subseteq \mathcal { I }$ is a subset of items from the database. A transaction $\tau$ is said to support itemset j if $j \subseteq T$ (i.e., if all the items in itemset j are contained in transaction T ). The support $\sigma _ { j }$ of itemset j is the number of transactions in D that support j. An itemset is frequent if at least a prede<sup>fi</sup>ned minimum number, $\sigma _ { \mathrm { m i n } }$ of transactions support it; $\mathcal { F }$ is the set of all frequent itemsets.

An association rule r is an expression of the form $r ^ { a } \Rightarrow r ^ { c }$ , where $r ^ { a }$ and $r ^ { c }$ are itemsets, and $\left\{ r ^ { a } \cap r ^ { c } \right\} = \phi$ We denote by $r ^ { \mu }$ the antecedent of rule $r ,$ and $r ^ { c }$ its consequent. The support $\sigma _ { r }$ of an association rule r is the support of the itemset $\{ r ^ { a } \cup r ^ { c } \}$ in D and can be interpreted as the probability of observing this itemset in $\hat { \mathcal { D } } .$ . The confidence $\gamma _ { r }$ of an association rule $r$ is the conditional probability of having $r ^ { c }$ in a transaction, given that $r ^ { a }$ is in it $\begin{array} { r } { ( \mathrm { i . e . , } \gamma _ { r } = P ( r ^ { c } \mid r ^ { a } ) = \frac { \sigma _ { \{ r ^ { a } \bigcup r ^ { c } \} } } { \sigma _ { r } ^ { a } } ) } \end{array}$ . Note that R is the set of association rules generated from $\mathcal { F }$ such that the con<sup>fi</sup>- dence of every rule $r \in \mathcal { R }$ is at least $\gamma _ { \mathrm { m i n } }$ . The values of $\sigma _ { \mathrm { m i n } }$ and $\gamma _ { \mathrm { m i n } }$ used to generate $\mathcal { R }$ are called the mining thresholds for support and con<sup>fi</sup>dence, respectively.

The set of sensitive rules—the rules the data owner wants to hide—is $\mathcal { R } ^ { S } ; \mathcal { R } ^ { S _ { a } }$ comprises the antecedents of the sensitive rules, with $\sigma _ { r } ^ { a }$ being the support of antecedent $r ^ { a } \in \mathcal { R } ^ { S _ { a } }$ in D. We denote by $\sigma _ { h } ^ { r }$ the support threshold for hiding rule $r { \mathrm { - i f } }$ the support of rule r drops below $\boldsymbol { \sigma } _ { h } ^ { r }$ in $\mathcal { D } ,$ the data owner considers r to be hidden in $\mathcal { D } .$ . Similarly, $\gamma _ { h } ^ { r }$ is the con<sup>fi</sup>dence threshold for hiding rule $r ;$ that ${ \mathrm { i } } \mathbf { s } ,$ , rule r is considered hidden if the con<sup>fi</sup>dence of r drops to $\gamma _ { h } ^ { r }$ or below in $\mathcal { D } .$ . The data owner chooses the hiding thresholds $\boldsymbol { \sigma } _ { h } ^ { r }$ and $\gamma _ { h } ^ { r }$ such that they are comfortable revealing sensitive rules if the receiver mines the data using mining thresholds at or below these values, because the large number of rules generated when mining with lower thresholds will make the revelation of sensitive rules unlikely.

## 3.2. An Exact Nonlinear Programming Formulation

The problem facing the data owner—the rule hiding problem—is to remove items from the fewest number of transactions such that every sensitive rule $r \in \mathcal { R } ^ { S }$ gets hidden. A sensitive rule can be hidden either by lowering its support in D to a value below $\sigma _ { h } ^ { r }$ or by lowering its con<sup>fi</sup>dence in $\mathcal { D }$ to $\gamma _ { h } ^ { r }$ or below, or both. The problem of hiding sensitive frequent itemsets by lowering their supports is a special case of the rule hiding problem, and Atallah et al. (1999) have shown it to be NP-hard. Therefore, the rule hiding problem is NP-hard as well.

The rule hiding problem can be formulated as the nonlinear integer program RHP (1–10), after de<sup>fi</sup>ning the following. Variable $v _ { k i }$ is 1 if item k is marked for removal from transaction i and 0 otherwise.<sup>1</sup> Variable $\omega _ { i r }$ is 1 if rule r loses the support of transaction i and 0 otherwise. Similarly, variable $\omega _ { i r } ^ { a }$ is 1 if ${ \boldsymbol { r } } ^ { a } ,$ the antecedent of rule $r ,$ loses the support of transaction i and 0 otherwise. Variable $x _ { i }$ is 1 if transaction i is altered and 0 otherwise. Variables $y _ { r }$ and $z _ { r }$ are de<sup>fi</sup>ned to be 1 if rule r is hidden based on support and con<sup>fi</sup>dence, respectively, and 0 otherwise:

(RHP)

min $\sum _ { i \in { \mathcal { D } } } x _ { i }$

$$
\mathrm{s.t.} \quad \sum_ {i \in \mathcal {D}} \omega_ {i r} \geq (\sigma_ {r} - \sigma_ {h} ^ {r} + 1) y _ {r} \quad \forall r \in \mathcal {R} ^ {S},\tag{1}
$$

$$
\left(\frac {\sigma_ {r} - \sum_ {i \in \mathcal {D}} \omega_ {i r}}{\sigma_ {r} ^ {a} - \sum_ {i \in \mathcal {D}} \omega_ {i r} ^ {a}}\right) \leq \gamma_ {h} ^ {r} + (1 - \gamma_ {h} ^ {r}) (1 - z _ {r}) \quad \forall r \in \mathcal {R} ^ {S},
$$

$$
y _ {r} + z _ {r} \geq 1\tag{2}
$$

$$
v _ {k i} \leq \omega_ {i r}
$$

$$
\forall r \in \mathcal {R} ^ {S},\tag{3}
$$

$$
\sum_ {k \in r} v _ {k i} \geq \omega_ {i r}
$$

$$
\forall i \in \mathcal {D}; \forall r \in \{\mathcal {R} ^ {S} \mid r \subseteq i \};
$$

$$
\forall k \in r,
$$

$$
\forall i \in \mathcal {D};\tag{4}
$$

$$
\forall r \in \{\mathcal {R} ^ {S} \mid r \subseteq i \},
$$

$$
v _ {k i} \leq \omega_ {i r} ^ {a}\tag{5}
$$

$$
\forall i \in \mathcal {D};
$$

$$
\forall r ^ {a} \in \{\mathcal {R} ^ {S _ {a}} \mid r ^ {a} \subseteq i \};
$$

$$
\forall k \in r ^ {a},\tag{6}
$$

$$
\sum_ {k \in r ^ {a}} v _ {k i} \geq \omega_ {i r} ^ {a}
$$

$$
\forall i \in \mathcal {D};
$$

$$
\forall r ^ {a} \in \{\mathcal {R} ^ {S _ {a}} \mid r ^ {a} \subseteq i \},
$$

$$
\omega_ {i r} \leq x _ {i}\tag{7}
$$

$$
\forall i \in \mathcal {D};
$$

$$
\forall r \in \{\mathcal {R} ^ {S} \mid r \subseteq i \},\tag{8}
$$

$$
\omega_ {i r} ^ {a} \leq x _ {i}
$$

$$
\forall i \in \mathcal {D};
$$

$$
\forall r ^ {a} \in \{\mathcal {R} ^ {S _ {a}} \mid r ^ {a} \subseteq i \},\tag{9}
$$

$$
v _ {k i}, \omega_ {i r}, \omega_ {i r ^ {a}} ^ {a}, x _ {i}, y _ {r}, z _ {r} \in \{0, 1 \}.\tag{10}
$$

The objective function minimizes the number of transactions altered, which is equivalent to maximizing the accuracy of the altered database. As noted earlier, a sensitive rule can be hidden either by lowering its support in D or by lowering its con<sup>fi</sup>dence in $\mathcal { D } ,$ or both. Constraint (1) says that if sensitive rule r is hidden based on reducing support, then at least $( \sigma _ { r } - \sigma _ { h } ^ { r } + 1 )$ transactions supporting r should be marked for sanitization. Constraint (2) states that the ratio of the remaining support for sensitive rule r to the remaining support for the antecedent of r should not exceed the hiding threshold for con<sup>fi</sup>dence if r is hidden based on lowered con<sup>fi</sup>dence. Constraint (3) ensures that at least one of support or con<sup>fi</sup>dence is lowered enough to ensure that every sensitive rule r gets hidden. Constraint (4) states that if item $k \in r$ is removed from a transaction i that supported sensitive rule $r , r$ is marked as having lost the support of transaction i. Constraint (5) ensures that if sensitive rule r is marked as having lost the support of a transaction i that originally supported it, at least one item of r is removed from transaction i. Constraints (6) and (7) serve similar purposes as Constraints (4) and (5) for the antecedents of the sensitive rules. Constraint (8) says that if a sensitive rule r loses the support of transaction i, transaction i is marked as having been altered; Constraint (9) makes a similar statement for rule antecedents.

## 3.3. An Illustrative Example

Consider the 10-transaction data set in Table 1. Suppose the <sup>fi</sup>ve rules in Table 2 are identi<sup>fi</sup>ed as sensitive by the data owner, who speci<sup>fi</sup>es hiding thresholds of $\begin{array} { r } { \sigma _ { h } ^ { \dot { r } } = 2 \operatorname { a n d } \gamma _ { h } ^ { r } = 0 . 3 . } \end{array}$ . That is, the data owner will consider the sensitive rules hidden if they cannot be mined at a support threshold of 2 and a con<sup>fi</sup>dence threshold over 30%. We use this as a running example in the paper.

Only the <sup>fi</sup>ve transactions that support sensitive rules $( t _ { 3 } , t _ { 4 } , \ t _ { 6 } , \ t _ { 7 } , \ t _ { 8 } )$ are candidates for sanitization. So, for example, even though $t _ { 5 }$ supports the antecedent of rule $r _ { 2 } ,$ we can ignore ${ \mathrm { i t } } ,$ as sanitizing t cannot decrease either the support or the con<sup>fi</sup>dence of $r _ { 5 } .$ Along the same lines, items 1, $6 ,$ 8, and 10 are not part of any sensitive rule and are not relevant to the problem, as removing these items will not affect the supports or con<sup>fi</sup>dences of any sensitive rule. As there are <sup>fi</sup>ve relevant transactions, the objective of RHP is to minimize $\left( x _ { 3 } + x _ { 4 } + x _ { 6 } + x _ { 7 } + x _ { 8 } \right)$ . Constraint (1) involves <sup>fi</sup>ve constraints, one for each rule. They are as follows.

Table 1. Example Database D

<table><tr><td>ID</td><td>Items</td><td>ID</td><td>Items</td></tr><tr><td> $t_{1}$ </td><td>1, 2, 3, 8</td><td> $t_{6}$ </td><td>1, 2, 3, 4, 5, 9</td></tr><tr><td> $t_{2}$ </td><td>6, 7, 8, 9</td><td> $t_{7}$ </td><td>3, 4, 6, 7</td></tr><tr><td> $t_{3}$ </td><td>3, 4, 7</td><td> $t_{8}$ </td><td>1, 2, 3, 4, 5, 7</td></tr><tr><td> $t_{4}$ </td><td>4, 5, 7, 8, 9</td><td> $t_{9}$ </td><td>8, 9</td></tr><tr><td> $t_{5}$ </td><td>3, 6, 7</td><td> $t_{10}$ </td><td>7, 8, 9, 10</td></tr></table>

$$
\begin{array}{r} \omega_ {6 1} + \omega_ {8 1} \geq 1 y _ {1} \\ \omega_ {3 2} + \omega_ {7 2} + \omega_ {8 2} \geq 2 y _ {2} \end{array} \left| \begin{array}{l l} \omega_ {4 3} + \omega_ {6 3} & \geq 1 y _ {3} \\ \omega_ {6 4} + \omega_ {8 4} & \geq 1 y _ {4} \\ \omega_ {4 5} + \omega_ {6 5} & \geq 1 y _ {5} \end{array} \right.
$$

These state that if a sensitive rule r is to be hidden by reducing support, then it has to be hidden from enough transactions supporting r. For example, $\mathrm { i f } r _ { 1 }$ is to be hidden by lowering support, then at least one $t _ { 6 }$ or $t _ { 8 }$ will need to be altered. Constraint (2) enforces a similar requirement on con<sup>fi</sup>dence and involves the following <sup>fi</sup>ve constraints.

$$
\begin{array}{r l} \frac {2 - \omega_ {6 1} - \omega_ {8 1}}{2 - \omega_ {6 1} ^ {a} - \omega_ {8 1} ^ {a}} & \leq 0. 3 + 0. 7 (1 - z _ {1}) \\ \frac {3 - \omega_ {3 2} - \omega_ {7 2} - \omega_ {8 2}}{4 - \omega_ {3 2} ^ {a} - \omega_ {7 2} ^ {a} - \omega_ {8 2} ^ {a}} & \leq 0. 3 + 0. 7 (1 - z _ {2}) \\ \frac {2 - \omega_ {4 3} - \omega_ {6 3}}{5 - \omega_ {4 3} ^ {a} - \omega_ {6 3} ^ {a}} & \leq 0. 3 + 0. 7 (1 - z _ {3}) \\ \frac {2 - \omega_ {6 4} - \omega_ {8 4}}{2 - \omega_ {6 4} ^ {a} - \omega_ {8 4} ^ {a}} & \leq 0. 3 + 0. 7 (1 - z _ {4}) \\ \frac {2 - \omega_ {4 5} - \omega_ {6 5}}{3 - \omega_ {4 5} ^ {a} - \omega_ {6 5} ^ {a} - \omega_ {8 5} ^ {a}} & \leq 0. 3 + 0. 7 (1 - z _ {5}) \end{array}
$$

For example, if $r _ { 3 }$ is to be hidden based on lowering con<sup>fi</sup>dence, then the ratio of the eventual support for $r _ { 3 }$ $\left( \mathrm { i . e . , ~ } 2 - \omega _ { 4 3 } - \omega _ { 6 3 } \right)$ and the eventual support for $r _ { 3 } ^ { a } ,$ , the antecedent of $r _ { 3 } ( \mathrm { i } . \mathrm { e } . , 5 - \omega _ { 4 3 } ^ { a } - \omega _ { 6 3 } ^ { a } ) .$ , has to be at most 0.3. Constraint (3) is straightforward; it ensures that at least one y and $z _ { r }$ is set to 1 for every sensitive rule r.

$$
\begin{array}{l} y _ {1} + z _ {1} \geq 1 \\ y _ {2} + z _ {2} \geq 1 \end{array} \left| \begin{array}{l} y _ {3} + z _ {3} \geq 1 \\ y _ {4} + z _ {4} \geq 1 \end{array} \right| y _ {5} + z _ {5} \geq 1
$$

Constraint (4) is needed for every relevant combination of items, transactions, and rules. In this ex ample, that leads to the following 29 constraints.

$$
\begin{array}{l l l l l} v _ {2 6} \leq \omega_ {6 1} & v _ {3 3} \leq \omega_ {3 2} & v _ {3 8} \leq \omega_ {8 2} & v _ {3 6} \leq \omega_ {6 4} & \\ v _ {5 6} \leq \omega_ {6 1} & v _ {7 3} \leq \omega_ {3 2} & v _ {7 8} \leq \omega_ {8 2} & v _ {4 6} \leq \omega_ {6 4} & v _ {5 4} \leq \omega_ {4 5} \\ v _ {4 6} \leq \omega_ {6 1} & v _ {4 3} \leq \omega_ {3 2} & v _ {4 8} \leq \omega_ {8 2} & v _ {5 6} \leq \omega_ {6 4} & v _ {9 4} \leq \omega_ {4 5} \\ v _ {2 8} \leq \omega_ {8 1} & v _ {3 7} \leq \omega_ {7 2} & v _ {9 4} \leq \omega_ {4 3} & v _ {3 8} \leq \omega_ {8 4} & v _ {5 6} \leq \omega_ {6 5} \\ v _ {5 8} \leq \omega_ {8 1} & v _ {7 7} \leq \omega_ {7 2} & v _ {4 4} \leq \omega_ {4 3} & v _ {4 8} \leq \omega_ {8 4} & v _ {9 6} \leq \omega_ {6 5} \\ v _ {4 8} \leq \omega_ {8 1} & v _ {4 7} \leq \omega_ {7 2} & v _ {9 6} \leq \omega_ {6 3} & v _ {5 8} \leq \omega_ {8 4} & \\ & & v _ {4 6} \leq \omega_ {6 3} & & \end{array}
$$

The <sup>fi</sup>rst of these states that if item 2 is removed from transaction $t _ { 6 } ,$ then sensitive rule $r _ { 1 }$ loses the support of $t _ { 6 } .$ The others make similar statements for the other relevant combinations of items, transactions, and rules.

Constraint (5) is needed for every pair of relevant transactions and sensitive rules, and it leads to the following 11 constraints. For example, the <sup>fi</sup>rst of these states that if $r _ { 1 }$ is marked as having lost the support of $t _ { 6 } ,$ then at least one of the items $2 , 4 ,$ , or 5 needs to be removed from $t _ { 6 } .$

$$
\begin{array}{c c} v _ {2 6} + v _ {4 6} + v _ {5 6} \geq \omega_ {6 1} & v _ {3 7} + v _ {4 7} + v _ {7 7} \geq \omega_ {7 2} \\ v _ {2 8} + v _ {4 8} + v _ {5 8} \geq \omega_ {8 1} & v _ {3 8} + v _ {4 8} + v _ {7 8} \geq \omega_ {8 2} \\ v _ {3 3} + v _ {4 3} + v _ {7 3} \geq \omega_ {3 2} & v _ {4 4} + v _ {9 4} \geq \omega_ {4 3} \\ v _ {4 6} + v _ {9 6} \geq \omega_ {6 3} & \\ v _ {3 6} + v _ {4 6} + v _ {5 6} \geq \omega_ {6 4} & v _ {5 4} + v _ {9 4} \geq \omega_ {4 5} \\ v _ {3 8} + v _ {4 8} + v _ {5 8} \geq \omega_ {8 4} & v _ {5 6} + v _ {9 6} \geq \omega_ {6 5} \end{array}
$$

Constraint (6) parallels Constraint (4), except that it ap plies to the items in the antecedents, rather than in the rules. This results in the following 19 constraints.

Table 2. Sensitive Rules $\mathcal { R } ^ { s }$

<table><tr><td rowspan="2">Sensitive rules</td><td colspan="2">Rule</td><td colspan="2">Antecedent</td><td rowspan="2">Confidence (%)</td></tr><tr><td>Supported by</td><td>Support</td><td>Supported by</td><td>Support</td></tr><tr><td> $r_1: \{2, 5\} \Rightarrow \{4\}$ </td><td> $t_6, t_8$ </td><td>2</td><td> $t_6, t_8$ </td><td>2</td><td>100.00</td></tr><tr><td> $r_2: \{3, 7\} \Rightarrow \{4\}$ </td><td> $t_3, t_7, t_8$ </td><td>3</td><td> $t_3, t_5, t_7, t_8$ </td><td>4</td><td>75.00</td></tr><tr><td> $r_3: \{9\} \Rightarrow \{4\}$ </td><td> $t_4, t_6$ </td><td>2</td><td> $t_2, t_4, t_6, t_9, t_{10}$ </td><td>5</td><td>40.00</td></tr><tr><td> $r_4: \{3, 5\} \Rightarrow \{4\}$ </td><td> $t_6, t_8$ </td><td>2</td><td> $t_6, t_8$ </td><td>2</td><td>100.00</td></tr><tr><td> $r_5: \{5\} \Rightarrow \{9\}$ </td><td> $t_4, t_6$ </td><td>2</td><td> $t_4, t_6, t_8$ </td><td>3</td><td>66.67</td></tr></table>

$$
\begin{array}{c c c} v _ {2 6} \leq \omega_ {6 1} ^ {a} & v _ {3 3} \leq \omega_ {3 2} ^ {a} & v _ {3 8} \leq \omega_ {8 2} ^ {a} \\ v _ {5 6} \leq \omega_ {6 1} ^ {a} & v _ {7 3} \leq \omega_ {3 2} ^ {a} & v _ {7 8} \leq \omega_ {8 2} ^ {a} \\ v _ {2 8} \leq \omega_ {8 1} ^ {a} & v _ {3 7} \leq \omega_ {7 2} ^ {a} & v _ {9 4} \leq \omega_ {4 3} ^ {a} \\ v _ {5 8} \leq \omega_ {8 1} ^ {a} & v _ {7 7} \leq \omega_ {7 2} ^ {a} & v _ {9 6} \leq \omega_ {6 3} ^ {a} \\ \hline v _ {3 6} \leq \omega_ {6 4} ^ {a} & v _ {5 4} \leq \omega_ {4 5} ^ {a} \\ v _ {5 6} \leq \omega_ {6 4} ^ {a} & v _ {5 6} \leq \omega_ {6 5} ^ {a} \\ v _ {3 8} \leq \omega_ {8 4} ^ {a} & v _ {5 8} \leq \omega_ {8 5} ^ {a} \\ v _ {5 8} \leq \omega_ {8 4} ^ {a} & \end{array}
$$

Constraint (7) enforces requirements on antecedents similar to what Constraint (5) enforced on rules, and it involves 12 constraints.

$$
\begin{array}{c c} v _ {2 6} + v _ {5 6} \geq \omega_ {6 1} ^ {a} & v _ {3 7} + v _ {7 7} \geq \omega_ {7 2} ^ {a} \\ v _ {2 8} + v _ {5 8} \geq \omega_ {8 1} ^ {a} & v _ {3 8} + v _ {7 8} \geq \omega_ {8 2} ^ {a} \\ v _ {3 3} + v _ {7 3} \geq \omega_ {3 2} ^ {a} & v _ {9 4} \geq \omega_ {4 3} ^ {a} \\ v _ {9 6} \geq \omega_ {6 3} ^ {a} & v _ {5 4} \geq \omega_ {4 5} ^ {a} \\ v _ {3 6} + v _ {5 6} \geq \omega_ {6 4} ^ {a} & v _ {5 6} \geq \omega_ {6 5} ^ {a} \\ v _ {3 8} + v _ {5 8} \geq \omega_ {8 4} ^ {a} & v _ {5 8} \geq \omega_ {8 5} ^ {a} \end{array}
$$

Constraint (8) is needed for every relevant pair of transactions and rules, leading to 11 constraints. For example, $\omega _ { 6 1 } \leq x _ { 6 }$ ensures that transaction $t _ { 6 }$ is marked as altered if rule $r _ { 1 }$ is marked as having lost the support of $t _ { 6 } .$

$$
\begin{array}{r l} \omega_ {6 1} \leq x _ {6}; \omega_ {8 1} \leq x _ {8} & \left| \begin{array}{l} \omega_ {4 3} \leq x _ {4}; \omega_ {6 3} \leq x _ {6} \\ \omega_ {3 2} \leq x _ {3}; \omega_ {7 2} \leq x _ {7}; \omega_ {8 2} \leq x _ {8} \end{array} \right. \\ \omega_ {6 4} \leq x _ {6}; \omega_ {8 4} \leq x _ {8} \\ \omega_ {4 5} \leq x _ {4}; \omega_ {6 5} \leq x _ {6} \end{array}
$$

Along the same lines, Constraint (9) is needed for every relevant pair of transactions and antecedents, and it involves 12 constraints.

$$
\begin{array}{r l} \omega_ {6 1} ^ {a} \leq x _ {6}; \omega_ {8 1} ^ {a} \leq x _ {8} & \Bigg | \omega_ {4 3} ^ {a} \leq x _ {4}; \omega_ {6 3} ^ {a} \leq x _ {6} \\ \omega_ {3 2} ^ {a} \leq x _ {3}; \omega_ {7 2} ^ {a} \leq x _ {7}; \omega_ {8 2} ^ {a} \leq x _ {8} & \omega_ {6 4} ^ {a} \leq x _ {6}; \omega_ {8 4} ^ {a} \leq x _ {8} \\ \omega_ {4 5} ^ {a} \leq x _ {4}; \omega_ {6 5} ^ {a} \leq x _ {6} \\ \omega_ {8 5} ^ {a} \leq x _ {8} \end{array}
$$

Altogether, formulation RHP for this example (which has 5 relevant transactions and 5 sensitive rules) involves 57 variables and 109 constraints. One optimal solution is $v _ { 4 3 } = v _ { 4 8 } = v _ { 9 6 } = 1 , \omega _ { 3 2 } = \omega _ { 6 3 } = \omega _ { 6 4 } = \omega _ { 6 5 } = \omega _ { 8 1 } = \omega _ { 8 2 } =$ $\omega _ { 8 4 } = 1 , ~ \omega _ { 6 3 } ^ { a } = 1 , ~ y _ { 1 } = y _ { 2 } = y _ { 3 } = y _ { 4 } = y _ { 5 } = 1 , ~ z _ { 2 } = ~ z _ { 3 } = 1 ,$ and $x _ { 3 } = x _ { 6 } = x _ { 8 } = 1$ . That is, item 4 is removed from $t _ { 3 }$ and $t _ { 8 }$ (because $v _ { 4 3 }$ and $v _ { 4 8 } = 1 )$ , whereas item 9 is removed from $t _ { 6 }$ (because $v _ { 9 6 } = 1 ) . ^ { 2 }$ This results in $r _ { 2 }$ losing the support of $t _ { 3 }$ (because $\omega _ { 3 2 } = 1 )$ $r _ { 3 }$ and $r _ { 5 }$ losing the support of $t _ { 6 }$ (because $\omega _ { 6 3 } = \omega _ { 6 4 } = 1 )$ , and $r _ { 1 } , r _ { 2 } ,$ and $r _ { 4 }$ losing the support of $t _ { 8 }$ (because $\omega _ { 8 1 } = \omega _ { 8 2 } = \omega _ { 8 4 } = 1 )$ The support of the antecedent of $r _ { 3 }$ also drops by 1 (because $\omega _ { 6 3 } ^ { a } = 1 )$ ). The solution hides all sensitive rules by lowering support (because $y _ { 1 } = y _ { 2 } = y _ { 3 } = y _ { 4 } = y _ { 5 } = 1 )$ . In addition, the con<sup>fi</sup>dences of $r _ { 2 }$ and $r _ { 3 }$ are also brought below the hiding threshold for con<sup>fi</sup>dence (because $z _ { 2 } = z _ { 3 } = 1 )$ . The new supports of sensitive rules $r _ { 1 } , r _ { 2 } , r _ { 3 } , r _ { 4 }$ ; and $r _ { 5 }$ are 1, 1, 1, 1, and $^ { 1 , }$ respectively; the corresponding con<sup>fi</sup>dences are ${ \scriptstyle { \frac { 1 } { 2 } } } , { \frac { 1 } { 4 } } , { \frac { 1 } { 4 } } , { \frac { 1 } { 2 } } ,$ and ${ } _ { \frac { 1 } { 3 } . } ^ { \frac { 1 } { 3 } } .$ All the supports have dropped below $\sigma _ { h } ^ { r }$ (which was $\bar { 2 } ) ,$ , and the con<sup>fi</sup>dences of $r _ { 2 }$ and $r _ { 3 }$ have dropped below $\gamma _ { h } ^ { r }$ (which was 0.3).

As this example illustrates, RHP can be quite large even for a small problem. The size of RHP makes it impractical for problems of realistic size, in addition to the fact that it has nonlinear constraints involving integer variables. The growth in the size of RHP is driven primarily by Constraints (4)–(7). Although Constraints (1)–(3) involve $| \mathcal { R } ^ { s } |$ constraints apiece, Constraints (4)–(7) involve substantially more. Constraint (4), for instance, has as many constraints as there are items in sensitive rules supported by each transaction. Even when a transaction supports only a single sensitive rule $r ,$ there are r constraints associated with that transaction alone. Real databases usually involve millions of transactions, and although all transactions will not support sensitive rules, there wil be a signi<sup>fi</sup>cant number that do. Consequently, Constraint (4) alone could involve millions of constraints. Similarly, Constraints (5)–(7) are also likely to have millions of constraints each in any realistic problem context. So although representing the rule hiding problem compactly as formulation RHP is useful, it is too large to be solvable even for small databases.

## 4. Separating the Sanitization and Accuracy Maximizing Decisions

Given that RHP is not solvable directly for problems of realistic size, we need an alternative approach. In this section, we take the <sup>fi</sup>rst step toward such an approach by separating the requirements of the <sup>fi</sup>rst three constraints of RHP from those of the next fou and making independent sanitization decisions for each transaction (the sanitization problem), the results of which are used as input into the accuracy maximization decision (the accuracy maximization problem). Whereas the accuracy maximization problem involves the identi<sup>fi</sup>cation of transactions to modify, the sanitization problem involves the identi<sup>fi</sup>cation of items to remove from a transaction that could be marked for modi<sup>fi</sup>cation.

Suppose we are given the optimal values of the $x _ { i }$ variables in formulation RHP—that is, suppose we have been given the transactions to be modi<sup>fi</sup>ed. As the remaining variables do not affect the objective function value, we would be left with the task of ensuring feasibility by identifying valid settings for these variables. This translates to the identification of a set of items to delete from each of these transactions such that Constraints (1)–(10) are satis<sup>fi</sup>ed. Now consider a simpli<sup>fi</sup>ed scenario where the items in the consequents of the sensitive rules do not appear in the antecedents of any of the rules. In this case, removing the items in the consequents of any rule leaves all the antecedents unaffected. So for every transaction i for which $x _ { i }$ is 1, setting $v _ { k i }$ to 1 for all items k that are consequents of rules supported by transaction i (and to 0 for all other items) will ensure that all sensitive rules supported by i are hidden, and no antecedent supported by i is. This, in turn, means that we need to set $\omega _ { i r }$ to 1 for all rules supported by transaction i (as all the rules are being hidden) but can set all relevant $\omega _ { i r } ^ { a }$ to 0 (as no antecedent is being affected). Consider transaction $t _ { 7 }$ in the example, and suppose we are told that it has to be sanitized $( \mathrm { i } . \mathrm { e } . , x _ { 7 } = 1 )$ . This transaction supports rule $r _ { 2 } ,$ whose consequent (i.e., item 4) does not appear in the antecedent of any rule. Therefore, t can be sanitized by removing item 4 from it—that is, by setting $v _ { 4 7 }$ to 1. This would require setting $\omega _ { 7 2 }$ to 1 to satisfy the constraint $v _ { 4 7 } \leq \omega _ { 7 2 } ,$ , and setting $v _ { 3 7 } =$ $v _ { 7 7 } = 0$ is feasible to $v _ { 3 7 } \leq \omega _ { 7 2 } , v _ { 7 7 } \leq \omega _ { 7 2 } , v _ { 3 7 } \leq \omega _ { 7 2 } ^ { a }$ and $v _ { 7 7 } \leq \omega _ { 7 2 } ^ { a } ,$ with $\omega _ { 7 2 } ^ { a } = 0$ . This setting of the variables also satis<sup>fi</sup>es v $+ v _ { 4 7 } + v _ { 7 7 } \ge \omega _ { 7 2 }$ , v $v _ { 7 7 } \geq \omega _ { 7 2 } ^ { a }$ , ω $\leq x _ { 7 } .$ , and $\omega _ { 3 2 } ^ { a } \leq x _ { 7 }$ . As this example illustrates, in the special case where none of the consequents of sensitive rules appears in any of their antecedents, Constraint (8) can be satis<sup>fi</sup>ed by setting $\omega _ { i r }$ to 1 for all $x _ { i } = 1 ;$ Constraints (4) and (5) can be satis<sup>fi</sup>ed by setting $v _ { k i } = 1 \mathrm { i f } \omega _ { i r } = 1$ , where k is an item in the consequent of rule r (with $v _ { k i } = 0$ for all other items $k ) ;$ and Constraints (6), (7), and (9) can be satis<sup>fi</sup>ed by setting all the $\omega _ { i r } ^ { a }$ to 0, along with all $v _ { k i }$ appearing in Constraints (6) and (7).

Given the $x _ { i }$ values, setting all possible $\omega _ { i r }$ to 1 $( \mathrm { i . e . , }$ the $\omega _ { i r }$ corresponding to all the $x _ { i }$ that are 1) will result in the largest possible value of the left-hand side of Constraint (1). If this value is greater than or equal to $( \sigma _ { r } - \sigma _ { h } ^ { r } + 1 )$ , the corresponding value of $y _ { r }$ can be set to 1 (which would satisfy Constraints (1) and (3)); the value of $y _ { r }$ can be set to 0 otherwise. Along the same lines, the settings used for $\omega _ { i r } \ ( \mathrm { i . e . , } \ 1 )$ and $\omega _ { i r } ^ { a } \ ( \mathrm { i . e . , ~ } 0 )$ result in the smallest possible value of the left-hand side of Constraint (2), because the numerator will be as small as possible, whereas the denominator will be as large as possible. If this ratio is less than the hiding threshold for con<sup>fi</sup>dence $\gamma _ { h } ^ { r } ,$ , the corresponding z variable can be set to 1 (satisfying Constraints (2) and (3) in the process). Note that the settings of the $\omega _ { i r }$ and $\omega _ { i r } ^ { a }$ variables provide the best chance for Constraints (1)–(3) to be satis<sup>fi</sup>ed. Because the given $x _ { i }$ were optimal, this setting of $\omega _ { i r }$ and $\omega _ { i r } ^ { a }$ (along with the corresponding settings of $y _ { r }$ and $z _ { r } )$ has to be feasible.

Although the simpli<sup>fi</sup>ed context of this example (where items in the consequents of sensitive rules do not appear in the antecedents of any sensitive rule) may not be typical, it highlights the trade-offs involved. First, if a transaction is marked for modi<sup>fi</sup>cation, eliminating every sensitive rule supported by it provides the best chance of satisfying Constraint (1) with $y _ { r } = 1$ . This also reduces the numerator of Constraint (2) by the greatest extent possible (which provides the best chance of satisfying Constraint (2) with $z _ { r } = 1 )$ ). On the other hand, consider a situation where the antecedent of a sensitive rule is supported by a transaction, whereas the rule itself is not. Although reducing the support of this antecedent has no impact on Constraint (1), it reduces the denominator of Constraint (2), making it harder to satisfy. This suggests that if a transaction is marked for modi<sup>fi</sup>cation, it should ideally be modi<sup>fi</sup>ed by eliminating the support for all sensitive rules while keeping the number of antecedents affected to as small a number as possible. This intuition forms the basis for the sanitization problem: in our context, the objective of the sanitization problem is to hide all the rules supported by a transaction by removing items such that the fewest number of antecedents of sensitive rules are eliminated. The sanitization problem is NP-hard, as it is equivalent to the red-blue set covering problem<sup>3</sup> (Carr et al. 2000), with the blue elements representing the rules and the red elements representing the antecedents.

In Section 4.1, we formulate the sanitization problem as an integer program. Before we do, however, it is important to recognize that the preceding discussion assumed that a solution in the $x _ { i }$ variables is available to us—this is clearly not true in reality. However, the point of being able to solve the sanitization problem for a single transaction is this: once we know how each transaction should be modi<sup>fi</sup>ed $i f$ it is marked for sanitization, we can use this information to identify exactly which transactions should be sanitized. That is, for each transaction that supports a sensitive rule, we can solve the sanitization problem to identify exactly how we would modify it $i f$ needed.

This will then be used to determine the speci<sup>fi</sup>c set of transactions to select for sanitization, so the total number selected is as small as possible.

## 4.1. The Sanitization Problem

In order to formulate the sanitization problem as an integer program, we need the following additional de<sup>fi</sup>nitions. De<sup>fi</sup>ne $\mathcal { R } _ { T } ^ { S } \subseteq \mathcal { R } ^ { S }$ to be the set of sensitive rules supported by transaction $\tau ,$ , and let $\mathcal { R } _ { T } ^ { S _ { a } }$ be the set of all sensitive rule antecedents supported by $\tau$ De<sup>fi</sup>ne parameter $h _ { k r }$ to be 1 if item $k \in \mathcal T$ belongs to rule $r \in \bar { \mathcal { R } } _ { T } ^ { S }$ and 0 otherwise. Similarly, de<sup>fi</sup>ne parameter $g _ { k r }$ to be 1 if item $k \in \mathcal T$ belongs to antecedent $r ^ { a } \in \mathcal { R } _ { T } ^ { S _ { a } }$ . We note that it is possible for a transaction to support only the antecedent of a sensitive rule, and not the rule itself—parameter $g _ { k r }$ is 1 even if this is the case, as we want to retain as many relevant antecedents as possible. In addition, de<sup>fi</sup>ne $\rho _ { r }$ to be the number of items in antecedent $r ^ { a } \in \mathcal { R } _ { T } ^ { S _ { a } } \mathrm { ~ } \dot { ( \mathrm { i . e . , ~ } \rho _ { r } = } | r ^ { a } | )$ . We de<sup>fi</sup>ne two sets of variables: variable $\xi _ { r }$ is 1 if antecedent $r ^ { a } \in$ $\mathcal { R } _ { \mathcal { T } } ^ { S _ { a } }$ gets hidden and 0 otherwise, whereas variable $\theta _ { k }$ is de<sup>fi</sup>ned to be 1 if item k is removed from $\tau$ and 0 otherwise. The sanitization integer program is as follows:

(SAN)

min <sup></sup> ξ<sub>r</sub> r<sup>a</sup><sub>∈</sub>R<sup>Sa</sup><sub>T</sub>

$$
\mathrm{s.t.} \sum_ {k \in \mathcal {T}} h _ {k r} \theta_ {k} \geq 1 \quad \forall r \in \mathcal {R} _ {\mathcal {T}} ^ {S},\tag{11}
$$

$$
\sum_ {k \in \mathcal {T}} g _ {k r} \theta_ {k} \leq \rho_ {r} \times \xi_ {r} \quad \forall r ^ {a} \in \mathcal {R} _ {\mathcal {T}} ^ {S _ {a}},\tag{12}
$$

$$
\theta_ {k}, \xi_ {r} \in \{0, 1 \}.\tag{13}
$$

The objective minimizes the number of antecedents of sensitive rules that get hidden. Constraint (11) ensures that all sensitive rules supported by transaction T are eliminated, whereas Constraint (12) makes sure that if an item from an antecedent supported by the transaction is removed, that antecedent is marked as being hidden.

This formulation does not differentiate between antecedents of sensitive rules supported by a transaction, and antecedents of sensitive rules not supported by the transaction. That is, so long as the antecedent of a sensitive rule is supported by the transaction (irrespective of whether the associated rule is supported or not), it is part of the formulation. It could be argued that it is preferable to conserve antecedents of rules that are not supported by the transaction than antecedents of rules supported by it; eliminating an item in the antecedent of a supported rule reduces both the numerator and the denominator of Constraint (2) by 1, whereas eliminating an item from the antecedent of a rule not supported by the transaction reduces the denominator of Constraint (2) without impacting the numerator. In a relative sense, the latter makes satisfying Constraint (2) slightly harder. If it is preferable that antecedents of sensitive rules not supported by the transaction be retained in case there are multiple optima to SAN, the objective function coef<sup>fi</sup>cient of the $\xi _ { r }$ variable associated with these antecedents can be set to 1  , where  is a very small number.

Consider transaction $t _ { 6 }$ in the example database in Table 1. It contained items 1, 2, 3, 4, 5, and $^ { 9 , }$ and it supported every sensitive rule but $r _ { 2 }$ and every antecedent except that of $r _ { 2 }$ . The only relevant items from a sanitization standpoint are those that are in any of the sensitive rules supported by $t _ { 6 }$ or in any relevant antecedent supported by $t _ { 6 } .$ Therefore, item 1 is not relevant and can be ignored. The sanitization formulation for $t _ { 6 }$ is as follows:

$$
\min \xi_ {1} + \xi_ {3} + \xi_ {4} + \xi_ {5},
$$

$$
\mathrm{s.t.} \quad \theta_ {2} + \theta_ {4} + \theta_ {5}
$$

$$
\geq 1,
$$

$$
\theta_ {4} + \theta_ {9}\tag{\( (r_{1}) \}
$$

$$
\geq 1,\tag{\( (r_{3}) \}
$$

$$
\theta_ {3} + \theta_ {4} + \theta_ {5}
$$

$$
\geq 1,\tag{\((r_4)\}
$$

$$
\theta_ {5} + \theta_ {9}
$$

$$
\geq 1,\tag{\((r_{5})\}
$$

$$
\theta_ {2} + \theta_ {5}
$$

$$
\leq 2 \xi_ {1},
$$

$$
\theta_ {9}\tag{\((r_1^a)\}
$$

$$
\theta_ {3} + \theta_ {5}
$$

$$
\leq \xi_ {3},\tag{\( (r_{3}^{a}) \}
$$

$$
\theta_ {5}
$$

$$
\leq 2 \xi_ {4},\tag{\(\left(r_{4}^{a}\right)\}
$$

$$
\leq \xi_ {5},\tag{\((r_5^a)\}
$$

$$
\theta_ {2}, \theta_ {3}, \theta_ {4}, \theta_ {5}, \theta_ {9}, \xi_ {1}, \xi_ {3}, \xi_ {4}, \xi_ {5} \in \{0, 1 \}.
$$

The optimal solution is $\theta _ { 4 } = \theta _ { 9 } = \xi _ { 3 } = 1$ (i.e., to remove items 4 and $^ { 9 , }$ resulting in the loss of the antecedent of r<sub>3</sub>).

## 4.2. A Sanitization Heuristic

There could be a large number of transactions supporting sensitive rules. As we will be solving the sanitization problem as a preprocessor in order to identify which transactions need to be sanitized, this problem needs to be solved for each such transaction. In some situations, the number of transac tions supporting sensitive rules could run into several millions, and therefore, we would need to solve the sanitization problem millions of times. From a practical standpoint, it may not always be viable to do so, even though the instances are small. For such situations, we develop a simple heuristic based on intuition from the integer programming formulation of the sanitization problem.

The problem of sanitizing a transaction has been considered in prior work (e.g., Atallah et al. 1999 and Menon and Sarkar 2007), with the approaches suggested being tailored to the speci<sup>fi</sup>c type of sensitive information being hidden. In the context of the problem considered in this paper, the key tradeoff is between the number of rules hidden and the number of antecedents that need to be sacri<sup>fi</sup>ced in order to hide them. This trade-off can form the basis of a simple greedy heuristic to sanitize a transaction $\tau .$

This heuristic involves <sup>fi</sup>nding the item in $\tau$ with the largest ratio of the number of sensitive rules in $\tau$ involving the item to the number of antecedents in $\tau$ involving the item and then marking it for removal. If any sensitive rules remain to be hidden in $\tau ,$ the ratios are updated (as the number of sensitive rules and antecedents of sensitive rules involving the remaining items in the list could have changed) and the item with the (new) largest ratio identi<sup>fi</sup>ed. Ties can be broken based on the numerator (the number of rules that will be hidden by removing this item). This heuristic is ef<sup>fi</sup>cient, involving the calculation of a few ratios involving the items in T , and <sup>fi</sup>nding the largest among them a few times.

Going back to $t _ { 6 }$ from the example database, the number of sensitive rules and relevant antecedents involving each of the relevant items are presented in Table 3, along with the associated ratios.

The highest ratio is associated with item $^ { 4 , }$ so 4 is marked for removal from $t _ { 6 } ,$ and the numbers updated. Removing 4 suppresses $r _ { 1 } , r _ { 3 } ,$ and $r _ { 4 } ,$ leaving only $r _ { 5 }$ being supported by $t _ { 6 } .$ The updated table is shown as Table 4.

The largest ratio is for item 9, which is marked for removal. Note that $t _ { 6 }$ no longer supports sensitive rules, and the heuristic concludes with the optimal solution in this instance.

Once we have the results from solving the sanitization problem, we have the information necessary to solve the accuracy maximization problem, where we identify the speci<sup>fi</sup>c transactions to sanitize.

## 4.3. The Accuracy Maximization Problem

A few additional de<sup>fi</sup>nitions are necessary before we can formulate the accuracy maximization problem as a mathematical program. We de<sup>fi</sup>ne $a _ { i r }$ to be 1 if sanitizing transaction i reduces the support for rule r and 0 otherwise. Similarly, $b _ { i r }$ is de<sup>fi</sup>ned to be 1 if sanitizing transaction i reduces the support for the antecedent of rule r (regardless of whether transaction i supports rule r) and 0 otherwise. Note that although the values of $a _ { i r }$ will be 1 for all sensitive rules r supported by transaction i, the values of $b _ { i r }$ come from the solution of the sanitization problem and therefore depend on the sanitization approach used. For example, based on the solution to the sanitization problem, the $a _ { i r }$ and $b _ { i r }$ values for transaction $t _ { 6 }$ are a<sub>61</sub> a<sub>62</sub> a<sub>63</sub> a<sub>64</sub> $a _ { 6 5 } ] = [ 1 0 1 1 1 ]$ and $[ b _ { 6 1 }$ b<sub>62</sub> $b _ { 6 3 } b _ { 6 4 } b _ { 6 5 } ] \stackrel {  } { = } [ 0 0 1 0 0 ] .$ , respectively. The variables $x _ { i } , y _ { r } ,$ , and $z _ { r }$ are as de<sup>fi</sup>ned earlier. The non linear integer programming formulation to hide sensitive rules while maximizing accuracy can be formulated as AMP:

Table 3. Original Ratios for the Items in $t _ { 6 }$

<table><tr><td rowspan="2"></td><td colspan="5">Item</td></tr><tr><td>2</td><td>3</td><td>4</td><td>5</td><td>9</td></tr><tr><td>Sensitive rules involving item</td><td>1</td><td>1</td><td>3</td><td>3</td><td>4</td></tr><tr><td>Relevant antecedents involving item</td><td>1</td><td>1</td><td>0</td><td>3</td><td>2</td></tr><tr><td>Ratio</td><td>1</td><td>1</td><td>∞</td><td>1</td><td>2</td></tr></table>

Table 4. Updated Ratios of the Items in $t _ { 6 }$ After Removing Item 4

<table><tr><td rowspan="2"></td><td colspan="4">Item</td></tr><tr><td>2</td><td>3</td><td>5</td><td>9</td></tr><tr><td>Sensitive rules involving item</td><td>0</td><td>0</td><td>1</td><td>1</td></tr><tr><td>Relevant antecedents involving item</td><td>1</td><td>1</td><td>3</td><td>1</td></tr><tr><td>Ratio</td><td>0</td><td>0</td><td>1/3</td><td>1</td></tr></table>

(AMP)

$$
\begin{array}{l l} \min & \sum_ {i \in \mathcal {D}} x _ {i} \\ \text {s.t.} & \sum_ {i \in \mathcal {D}} a _ {i r} x _ {i} \qquad \qquad \geq (\sigma_ {r} - \sigma_ {h} ^ {r} + 1) y _ {j} \qquad \forall r \in \mathcal {R} ^ {S}, \end{array}\tag{14}
$$

$$
\left(\frac {\sigma_ {r} - \sum_ {i \in \mathcal {D}} a _ {i r} x _ {i}}{\sigma_ {r} ^ {a} - \sum_ {i \in \mathcal {D}} b _ {i r} x _ {i}}\right) \leq \gamma_ {h} ^ {r} + (1 - \gamma_ {h} ^ {r}) (1 - z _ {r}) \forall r \in \mathcal {R} ^ {S},\tag{15}
$$

$$
y _ {r} + z _ {r} \geq 1 \quad \forall r \in \mathcal {R} ^ {S},
$$

$$
x _ {i}, y _ {r}, z _ {r} \in \{0, 1 \}.\tag{16}
$$

(17)

The objective minimizes the number of transactions marked for sanitization. The logic behind Constraints (14)–(16) is similar to that of Constraints (1)–(3), except for the fact that the sanitization decisions are assumed to have been made already. This problem remains NP-hard, as the problem studied in Menon et al. (2005) is a specia case. However, it is a signi<sup>fi</sup>cantly smaller problem than RHP and involves only $\overset { \smile } { 3 } \times \lvert \mathcal { R } ^ { S } \rvert$ constraints.

In our example, the $a _ { i r }$ and $b _ { i r }$ values for the relevant transactions based on the sanitization heuristic are

$$
\begin{array}{r l} & {[ a _ {3 1} a _ {3 2} a _ {3 3} a _ {3 4} a _ {3 5} ] = [ 0 1 0 0 0 ], [ b _ {3 1} b _ {3 2} b _ {3 3} b _ {3 4} b _ {3 5} ] = [ 0 0 0 0 0 ],} \\ & {[ a _ {4 1} a _ {4 2} a _ {4 3} a _ {4 4} a _ {4 5} ] = [ 0 0 1 0 1 ], [ b _ {4 1} b _ {4 2} b _ {4 3} b _ {4 4} b _ {4 5} ] = [ 0 0 0 0 1 ],} \\ & {[ a _ {6 1} a _ {6 2} a _ {6 3} a _ {6 4} a _ {6 5} ] = [ 1 0 1 1 1 ], [ b _ {6 1} b _ {6 2} b _ {6 3} b _ {6 4} b _ {6 5} ] = [ 0 0 1 0 0 ],} \\ & {[ a _ {7 1} a _ {7 2} a _ {7 3} a _ {7 4} a _ {7 5} ] = [ 0 1 0 0 0 ], [ b _ {7 1} b _ {7 2} b _ {7 3} b _ {7 4} b _ {7 5} ] = [ 0 0 0 0 0 ], \mathrm{and}} \\ & {[ a _ {8 1} a _ {8 2} a _ {8 3} a _ {8 4} a _ {8 5} ] = [ 1 1 0 1 0 ], [ b _ {8 1} b _ {8 2} b _ {8 3} b _ {8 4} b _ {8 5} ] = [ 0 0 0 0 0 ].} \end{array}
$$

Given this, formulation AMP for the example is as follows

$$
\begin{array}{l l} \min & x _ {3} + x _ {4} + x _ {6} + x _ {7} + x _ {8} \\ \text {s.t.} & x _ {6} + x _ {8} \geq y _ {1} \\ & x _ {3} + x _ {7} + x _ {8} \geq 2 y _ {2} \\ & x _ {4} + x _ {6} \geq y _ {3} \\ & x _ {6} + x _ {8} \geq y _ {4} \\ & x _ {4} + x _ {6} \geq y _ {5} \end{array} \left| \begin{array}{c} \left(\frac {2 - x _ {6} - x _ {8}}{2 - 0}\right) \leq 0. 3 + 0. 7 (1 - z _ {1}) \\ \left(\frac {3 - x _ {3} - x _ {7} - x _ {8}}{4 - 0}\right) \leq 0. 3 + 0. 7 (1 - z _ {2}) \\ \left(\frac {2 - x _ {4} - x _ {6}}{5 - x _ {6}}\right) \leq 0. 3 + 0. 7 (1 - z _ {3}) \\ \left(\frac {2 - x _ {6} - x _ {8}}{2 - 0}\right) \leq 0. 3 + 0. 7 (1 - z _ {4}) \\ \left(\frac {2 - x _ {4} - x _ {6}}{2 - x _ {4}}\right) \leq 0. 3 + 0. 7 (1 - z _ {5}) \end{array} \right.
$$

$$
x _ {3}, x _ {4}, x _ {6}, x _ {7}, x _ {8}, y _ {1}, y _ {2}, y _ {3}, y _ {4}, y _ {5}, z _ {1}, z _ {2}, z _ {3}, z _ {4}, z _ {5} \in \{0, 1 \}
$$

The optimal solution is $x _ { 3 } = x _ { 6 } = x _ { 7 } = 1 , y _ { 1 } = y _ { 2 } = y _ { 3 } =$ $y _ { 4 } = y _ { 5 } = 1$ , and $z _ { 3 } = 1$ , with the objective function value being 3. In this example, this is the same solution as the one provided by RHP.

Of course, any sanitization approach can be used to hide the sensitive rules. For example, blanket sanitization (Menon and Sarkar 2007) involves the removal of all but one of the items in a transaction. Although this will hide all sensitive rules supported by the transaction, it will also eliminate all antecedents supported by the transaction irrespective of whether the associated rule was supported or not (unless the item remaining is an antecedent by itself). As the results of the sanitization process are provided as input into the accuracy maximization problem, this could have an adverse impact on the number of transactions marked for sanitization. In addition, having fewer nonzero $b _ { i r }$ values makes the nonlinear constraints less complicated; in the extreme case when all the $b _ { i r }$ values are 0 for a rule r, the nonlinear constraints become linear. Consequently, there are important computational advantages to solving the sanitization problem as well as possible. Using $t _ { 6 }$ again as an example, blanket sanitization will eliminate the supports for antecedents $r _ { 1 } ^ { a } , r _ { 3 } ^ { a } , r _ { 4 } ^ { a } ,$ , and $r _ { 5 } ^ { a }$ while eliminating the support for rules $r _ { 1 } , r _ { 3 } , r _ { 4 } ,$ and $r _ { 5 } .$ Sanitizing $t _ { 6 }$ with the loss of a single antecedent is clearly preferable to doing so with the loss of 4. Formulation AMP, when assuming a blanket sanitization approach that leaves only the <sup>fi</sup>rst item in any sanitized transaction, is as follows.

$$
\begin{array}{r l r} \min & x _ {3} + x _ {4} + x _ {6} + x _ {7} + x _ {8} \\ \text {s.t.} & x _ {6} + x _ {8} & \geq y _ {1} \\ & x _ {3} + x _ {7} + x _ {8} & \geq 2 y _ {2} \\ & x _ {4} + x _ {6} & \geq y _ {3} \\ & x _ {6} + x _ {8} & \geq y _ {4} \\ & x _ {4} + x _ {6} & \geq y _ {5} \\ & & y _ {1} + z _ {1} \geq 1 \\ & & y _ {2} + z _ {2} \geq 1 \\ & & y _ {3} + z _ {3} \geq 1 \\ & & y _ {4} + z _ {4} \geq 1 \\ & & y _ {5} + z _ {5} \geq 1 \end{array} \left| \begin{array}{c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c c} \left(\frac {2 - x _ {6} - x _ {8}}{2 - x _ {6} - x _ {8}}\right) & \leq 0. 3 + 0. 7 (1 - z _ {1}) \\ \left(\frac {3 - x _ {3} - x _ {7} - x _ {8}}{4 - x _ {3} - x _ {7} - x _ {8}}\right) & \leq 0. 3 + 0. 7 (1 - z _ {2}) \\ \left(\frac {2 - x _ {4} - x _ {6}}{5 - x _ {4} - x _ {6}}\right) & \leq 0. 3 + 0. 7 (1 - z _ {3}) \\ \left(\frac {2 - x _ {6} - x _ {8}}{2 - x _ {6} - x _ {8}}\right) & \leq 0. 3 + 0. 7 (1 - z _ {4}) \\ \left(\frac {2 - x _ {4} - x _ {6}}{2 - x _ {4} - x _ {6} - x _ {8}}\right) & \leq 0. 3 + 0. 7 (1 - z _ {5}) \end{array} \right|
$$

$$
x _ {3}, x _ {4}, x _ {6}, x _ {7}, x _ {8}, y _ {1}, y _ {2}, y _ {3}, y _ {4}, y _ {5}, z _ {1}, z _ {2}, z _ {3}, z _ {4}, z _ {5} \in \{0, 1 \}
$$

Whereas the optimal solution is not affected in this example (as we know that the optimal formulation in this example involved lowering the support constraints of all the sensitive rules), the other drawbacks become clear. All the con<sup>fi</sup>dence constraints are nonlinear, and as sanitization in this example involves eliminating support for every rule and every antecedent supported by the transaction, the denominator will decrease by at least the same number as the numerator will (and potentially by more, as some transactions may support only the antecedent of a rule and not the rule itself—e.g., t<sub>8</sub> supports the antecedent of $r _ { 5 }$ but not $r _ { 5 } )$ . The result will be that the con<sup>fi</sup>dencebased constraints are less likely to be binding, which, in turn, is likely to result in decreased accuracy levels.

We note that the optimal solutions to the sanitization problem and the heuristic were the same in every instance we tried. This suggests that the heuristic is very effective. Additionally, if the heuristic deviates from the optimal solution to the sanitization problem, the impact on formulation AMP will be to make it more dif<sup>fi</sup>cult (as, e.g., the denominator of the con<sup>fi</sup>dence constraint is likely to involve more variables). In such instances, therefore, AMP is likely to get even easier to solve if the optimal sanitization approach is used.

## 5. The Linear Integer Program and Problem Reduction

Although AMP is substantially smaller than RHP, it remains nonlinear. Depending on the size of the database and the number of sensitive rules, AMP can also be a relatively large problem. In this section, we <sup>fi</sup>rst show how to reformulate AMP as a linear integer program, and then we present various results to reduce the size of the problem that needs to be solved. The proofs of all propositions are in Appendix A.

## 5.1. The Linear Equivalent of the Accuracy Maximization Problem

Although it is possible to try and solve formulation AMP in a state-of-the-art nonlinear integer solver such as BARON (Sahinidis 2014), linearizing it allows us to exploit the considerable capabilities of commercial integer programming solvers such as CPLEX (IBM 2018).

Constraint (15) is nonlinear in the binary variables $x _ { i }$ and $z _ { r } .$ If we consider the two possible values of $z _ { r } ,$ this constraint is saying that $\left( { \frac { \sigma _ { r } - \sum _ { i \in { \mathcal { D } } } a _ { i r } x _ { i } } { \sigma _ { r } ^ { a } - \sum _ { i \in { \mathcal { D } } } b _ { i r } x _ { i } } } \right) \leq \gamma _ { h } ^ { r } { \mathrm { ~ i f ~ } } z _ { r } = 1$ and that $\left( \frac { \sigma _ { r } - \sum _ { i \in \mathcal { D } } a _ { i r } x _ { i } } { \sigma _ { r } ^ { a } - \sum _ { i \in \mathcal { D } } b _ { i r } x _ { i } } \right) \leq 1$ if $z _ { r } = 0$ (effectively, this constraint is redundant if $\begin{array} { r } { z _ { r } = 0 ) . \left( \frac { \sigma _ { r } - \sum _ { i \in \mathcal { D } } a _ { i r } x _ { i } } { \sigma _ { r } ^ { a } - \sum _ { i \in \mathcal { D } } b _ { i r } x _ { i } } \right) \leq \gamma _ { h } ^ { r } } \end{array}$ implies that $\begin{array} { r } { \sigma _ { r } - \sum _ { i \in \mathcal { D } } a _ { i r } x _ { i } \le \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } - \gamma _ { h } ^ { r } \sum _ { i \in \mathcal { D } } b _ { i r } x _ { i } , } \end{array}$ , which simpli<sup>fi</sup>es to $\begin{array} { r } { \sum _ { i \in \mathcal { D } } ( a _ { i r } - \gamma _ { h } ^ { r } b _ { i r } ) x _ { i } \ge ( \sigma _ { r } - \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } ) } \end{array}$

De<sup>fi</sup>ne $\alpha _ { r }$ to be a large value, and consider the constraint $\begin{array} { r } { \sum _ { i \in \mathcal { D } } ( a _ { i r } - \gamma _ { h } ^ { r } b _ { i r } ) x _ { i } \ge - \alpha _ { r } + ( \sigma _ { r } - \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } + \alpha _ { r } ) z _ { r } . } \end{array}$ When $z _ { r } = 1$ , the $\alpha _ { r }$ cancels with the $( - \alpha _ { r } ) ,$ , and the constraint simpli<sup>fi</sup>es to $\begin{array} { r } { \sum _ { i \in \mathcal { D } } ( a _ { i r } - \gamma _ { h } ^ { r } b _ { i r } ) x _ { i } \ge ( \sigma _ { r } - \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } ) . } \end{array}$ which is what we want. On the other hand, when $z _ { r } =$ $0 ,$ this constraint reduces to $\begin{array} { r } { \sum _ { i \in \mathcal { D } } ( a _ { i r } - \gamma _ { h } ^ { r } b _ { i r } ) x _ { i } \ge - \alpha _ { r } , } \end{array}$ which is redundant for large values of $\alpha _ { r } .$ The term $\left( - \alpha _ { r } \right)$ is needed to ensure that we are not cutting off feasible solutions, and this will not happen if $\begin{array} { r } { \alpha _ { r } \geq \gamma _ { h } ^ { r } \times \left( \sum _ { \{ i \in \mathcal { D } | a _ { i r } = 0 \} } b _ { i r } \right) } \end{array}$ . Consequently, this is equivalent to the nonlinear Constraint (15), and a linearinteger formulation equivalent to AMP is LRH:

(LRH)

$$
\begin{array}{l l} \min & \sum_ {i \in \mathcal {D}} x _ {i} \\ \text {s.t.} & \sum_ {i \in \mathcal {D}} a _ {i r} x _ {i} \end{array} \qquad \geq (\sigma_ {r} - \sigma_ {h} ^ {r} + 1) y _ {r} \quad \forall r \in \mathcal {R} ^ {S},\tag{18}
$$

$$
\sum_ {i \in \mathcal {D}} (a _ {i r} - \gamma_ {h} ^ {r} b _ {i r}) x _ {i} \geq - \alpha_ {r} + (\sigma_ {r} - \gamma_ {h} ^ {r} \sigma_ {r} ^ {a} + \alpha_ {r}) z _ {r}
$$

$$
\forall r \in \mathcal {R} ^ {S},\tag{19}
$$

$$
y _ {r} + z _ {r} \geq 1 \quad \forall r \in \mathcal {R} ^ {S},\tag{20}
$$

$$
x _ {i}, y _ {r}, z _ {r} \in \{0, 1 \}.\tag{21}
$$

For the example data set, $\begin{array} { r } { \sum _ { \{ i \in \mathcal { D } | a _ { i r } = 0 \} } b _ { i r } = 0 } \end{array}$ for all <sup>fi</sup>ve rules, as there is no rule r that has $\begin{array} { r } { b _ { i r } = 1 } \end{array}$ and $a _ { i r } = 0$ in any transaction i. This implies that any value greater than 0 is a valid value for $\alpha _ { r } ,$ with lower values resulting in tighter formulations. LRH for the example with $\alpha _ { r } = 0$ is as follows.

$$
\begin{array}{r l} & {\min x _ {3} + x _ {4} + x _ {6} + x _ {7} + x _ {8}} \\ & {\mathrm{s.t.} \quad x _ {6} + x _ {8} \geq y _ {1}} \\ & {\quad x _ {3} + x _ {7} + x _ {8} \geq 2 y _ {2}} \\ & {\quad x _ {4} + x _ {6} \geq y _ {3}} \\ & {\quad x _ {6} + x _ {8} \geq y _ {4}} \\ & {\quad x _ {4} + x _ {6} \geq y _ {5}} \\ & {\quad y _ {1} + z _ {1} \geq 1} \\ & {\quad y _ {2} + z _ {2} \geq 1} \\ & {\quad y _ {3} + z _ {3} \geq 1} \\ & {\quad y _ {4} + z _ {4} \geq 1} \\ & {\quad y _ {5} + z _ {5} \geq 1} \\ & {\quad x _ {3}, x _ {4}, x _ {6}, x _ {7}, x _ {8}, y _ {1}, y _ {2}, y _ {3}, y _ {4}, y _ {5}, z _ {1}, z _ {2}, z _ {3}, z _ {4}, z _ {5} \in \{0, 1 \}} \end{array}
$$

This has the same number of constraints as AMP (i.e., $3 \times | \mathcal { R } ^ { S } | )$ , but none of the constraints is nonlinear. The following subsections identify ways in which the size of LRH can be reduced.

## 5.2. Reducing Problem Size

As mentioned earlier, the only relevant transactions are those that support sensitive rules; we have already applied this in our example. In addition, the following results help reduce the size of the problem further.

## 5.2.1. Eliminating Constraint $\pmb { y } _ { r } + \pmb { z } _ { r } \ge 1$

Proposition 1. There is always an optimal solution where $y _ { r } + z _ { r } = 1$

In the optimal solution to the example, both y and $z _ { 3 }$ were set to 1. However, a solution that sets only one of these $( \mathsf { s a y } , \ y _ { 3 } )$ to 1 and the other to 0 is also optimal with all the other variables staying at the same values as before. The only impact is that although the solution tells us that $r _ { 3 }$ is being hidden as a result of reduced support, it does not explicitly provide us with the additional information that the con<sup>fi</sup>dence of $r _ { 3 }$ is being lowered below the hiding threshold as well. Note that this is easy to infer after the problem has been solved, and it does not impact the optimal solution. Proposition 1 allows us to eliminate Constraint (20) by substituting $z _ { r } =$ $1 - y _ { 1 }$ into Constraint (19). This results in the reduced integer program as follows:

$$
\begin{array}{r l} \min & \sum_ {i \in \mathcal {D}} x _ {i} \\ \mathrm{s.t.} & \sum_ {i \in \mathcal {D}} a _ {i r} x _ {i} \qquad \ge (\sigma_ {r} - \sigma_ {h} ^ {r} + 1) y _ {r} \quad \forall r \in \mathcal {R} ^ {\mathrm{S}}, \end{array}\tag{22}
$$

$$
\sum_ {i \in \mathcal {D}} (a _ {i r} - \gamma_ {h} ^ {r} b _ {i r}) x _ {i} \geq - \alpha_ {r} + (\sigma_ {r} - \gamma_ {h} ^ {r} \sigma_ {r} ^ {a} + \alpha_ {r}) (1 - y _ {r})
$$

$$
\forall r \in \mathcal {R} ^ {S},\tag{23}
$$

$$
x _ {i}, y _ {r} \qquad \in \{0, 1 \}.\tag{24}
$$

5.2.2. Eliminating Selected Variables and Constraints. Proposition 2. $\begin{array} { r } { I f \left( \sigma _ { h } ^ { r } - 1 \right) < \gamma _ { h } ^ { r } ( \sigma _ { r } ^ { a } - \sum _ { i \in \mathcal { D } } b _ { i r } ) } \end{array}$ for sensitive rule $r ,$ the optimal solution will always set y to 0.

Proposition 3. If $( \sigma _ { h } ^ { r } - 1 ) > \gamma _ { h } ^ { r } \sigma _ { r } ^ { a }$ for sensitive rule $r ,$ the optimal solution will always set y to 1.

Setting $y _ { r } = 0$ implies that Constraint (22) becomes redundant for rule r. Consequently, this constraint can be eliminated corresponding to each rule for which Proposition 2 holds. Similarly, Constraint (23) can be eliminated for each rule that meets the condition in Proposition 3. A straightforward consequence of Propositions 2 and 3 is Corollary 1.

Corollary 1. $\begin{array} { r } { I f \sum _ { i \in \mathcal { D } } b _ { i r } = 0 } \end{array}$ for sensitive rule $r ,$ the support and confidence constraints for rule r can be represented by the equivalent single constraint $\begin{array} { r } { \sum _ { i \in \mathcal { D } } a _ { i r } x _ { i } \ge \operatorname* { m i n } \{ ( \sigma _ { r } - }  \end{array}$ $\bar { \sigma _ { h } ^ { r } } + 1 ) , \ \bar { ( } \sigma _ { r } - \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } ) \}$

## 5.2.3. Tightening Constraints.

Proposition 4. If $( \sigma _ { h } ^ { r } - 1 ) < \gamma _ { h } ^ { r } \sigma _ { r } ^ { a }$ for sensitive rule $r ,$ the support constraint for rule r can be written equivalently as $\begin{array} { r } { \dot { \sum } _ { i \in \mathcal { D } } a _ { i r } x _ { i } \ge \big ( \sigma _ { r } - \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } \big ) + \big ( \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } - \sigma _ { h } ^ { r } + 1 \big ) y _ { r } \forall r \in \mathcal { R } ^ { S } } \end{array}$

Proposition 4 could expedite the solution of the integer program, as this will likely result in larger fractional values for the $y _ { r }$ variables (relative to those resulting from Constraint (22)) during branch and bound. In turn, this is likely to result in a more ef<sup>fi</sup>- cient branch-and-bound procedure.

If we apply Propositions 2 and 3 to our example, we get the following results:

$$
\begin{array}{c} r _ {1} \colon (\sigma_ {h} ^ {1} - 1) = (2 - 1) = 1 > \gamma_ {h} ^ {1} \sigma_ {1} ^ {a} = 0. 3 \times 2 = 0. 6 \\ \Rightarrow y _ {1} = 1, z _ {1} = 0, \\ r _ {2} \colon (\sigma_ {h} ^ {2} - 1) = (2 - 1) = 1 <   \gamma_ {h} ^ {2} \bigg (\sigma_ {2} ^ {a} - \sum_ {i \in \mathcal {D}} b _ {i 2} \bigg) = 0. 3 \times (4 - 0) = 1. 2 \end{array}
$$

$$
\begin{array}{c} \Rightarrow y _ {2} = 0, z _ {2} = 1, \\ r _ {3}: (\sigma_ {h} ^ {3} - 1) = (2 - 1) = 1 <   \gamma_ {h} ^ {3} \bigg (\sigma_ {3} ^ {a} - \sum_ {i \in \mathcal {D}} b _ {i 3} \bigg) = 0. 3 \times (5 - 1) = 1. 2 \\ \Rightarrow y _ {3} = 0, z _ {3} = 1, \\ r _ {4}: (\sigma_ {h} ^ {4} - 1) = (2 - 1) = 1 > \gamma_ {h} ^ {4} \sigma_ {4} ^ {a} = 0. 3 \times 2 = 0. 6 \\ \Rightarrow y _ {4} = 1, z _ {4} = 0, \text {and} \\ r _ {5}: (\sigma_ {h} ^ {5} - 1) = (2 - 1) = 1 > \gamma_ {h} ^ {5} \sigma_ {5} ^ {a} = 0. 3 \times 3 = 0. 9 \\ \Rightarrow y _ {5} = 1, z _ {5} = 0. \end{array}
$$

The values of $\begin{array} { r } { \sum _ { i \in \mathcal { D } } b _ { i 2 } \ : ( \mathrm { i . e . , 0 } ) } \end{array}$ and $\textstyle \sum _ { i \in { \mathcal { D } } } b _ { i 3 } \left( { \mathrm { i } } . \mathbf { e } . , 1 \right)$ come from formulation AMP presented earlier. In this example, the only support constraints that remain relate to $r _ { 1 } , \ r _ { 4 } ,$ and $r _ { 5 } .$ . Proposition 4 does not apply to any of these, because $( \sigma _ { h } ^ { 1 } - 1 ) = 1 \not \times \gamma _ { h } ^ { 1 } \sigma _ { 1 } ^ { a } = 0 . 6 ,$ $( \sigma _ { h } ^ { 4 } - 1 ) = 1 \not \times \gamma _ { h } ^ { 4 } \sigma _ { 4 } ^ { a } = 0 . 6 ,$ and $( \sigma _ { h } ^ { 5 } - 1 ) = 1 \not \times \gamma _ { h } ^ { 5 } \sigma _ { 5 } ^ { a } = 0 . 9 .$ This results in the integer program in what follows; in this case, only 5 of the original 15 constraints remain, along with 5 of the original 15 variables. This is a signi<sup>fi</sup>cantly easier problem to solve from a practical perspective than the equivalent versions of RHP, AMP, or LRH, before incorporating Propositions 1–4.

$$
\begin{array}{l l} \min & x _ {3} + x _ {4} + x _ {6} + x _ {7} + x _ {8} \\ \text {s.t.} & x _ {6} + x _ {8} \geq 1 \\ & x _ {6} + x _ {8} \geq 1 \\ & x _ {4} + x _ {6} \geq 1 \\ & x _ {3} + x _ {7} + x _ {8} \geq 1. 8 \\ & x _ {4} + 0. 7 x _ {6} \geq 0. 5 \\ & x _ {3}, x _ {4}, x _ {6}, x _ {7}, x _ {8} \in \{0, 1 \} \end{array}
$$

The propositions presented in this section help linearize and reduce formulation AMP to the condensed equivalent LRH. We note that although LRH solves AMP optimally, the optimal solution to AMP is not necessarily optimal to RHP. The solution to LRH and AMP is optimal, given that every transaction marked for sanitization will be sanitized of all sensitive rules supported by it. It is possible that RHP could have a better solution that involves partially sanitizing some transactions.

We had recognized earlier that sensitive rules could potentially exist at different levels in an organization. For example, products related to cold weather might play a role in sensitive rules in Minnesota, whereas items related to the beach could be in sensitive rules in Florida (i.e., rules that are sensitive in one store need not be sensitive in another or at the organizational level). If sensitive rules need to be hidden at the organizational and store levels, constraints of the form (14)–(16) would be needed for the sensitive rules in each store, in addition to those at the organizational level. As the propositions developed in this paper are for any sensitive rule, they are agnostic to whether sensitive rules are at the store level or the organizational level. Therefore, all of them remain valid even when sensitive rules exist at different levels. In addition, the sanitization problem remains identical to SAN, except for the fact that sensitive rules at both the organizational and store levels need to be considered. Importantly, the formulation for a transaction that supports multiple sensitive rules would not change regardless of whether the sensitive rules are all at the organizational level or all at the store level, or whether they are distributed across the store level and the organizational level.

## 6. Computational Experiments

We conduct computational experiments on two real transactional data sets, retail and bms-pos, available from the repository of the <sup>fi</sup>rst workshop on Frequent Itemset Mining Implementations (http://<sup>fi</sup>mi. uantwerpen.be/data/), and on three large synthetic data sets with 10, 50, and 100 million transactions (10m, 50m, and 100m, respectively) generated using IBM’s synthetic data generator (Agrawal and Srikant 1994). The retail data set has 88,162 transactions, 16,470 items, and an average transaction length of 10. 3, and bms-pos has 515,597 transactions, 1,657 items, and an average transaction length of 6.5. The synthetic data sets 10m, 50m, and 100m have 100,000 items and an average transaction length of 10.

All data sets were mined with a minimum support $\sigma _ { \mathrm { m i n } }$ of 0.1% and a minimum con<sup>fi</sup>dence $\gamma _ { \mathrm { m i n } }$ of 20%. This resulted in 7,587, 372,974, 103,247, 103,197, and 103,214 rules being generated for retail, bms-pos, 10m, 50m, and 100m, respectively. The hiding thresholds were set to the corresponding mining thresholds in all the experiments. Experiments were conducted with 5, 20, 50, 100, and 200 sensitive rules, and the sensitive rules were selected randomly. Four categories of experiments were conducted, based on the sensitive rules being randomly drawn from the set of rules with con<sup>fi</sup>- dences in the following ranges: (i) 20%–30%, (ii) 20%–50%, (iii) 20%–70%, and (iv) 20%–90%.<sup>4</sup> A variety of experiments are conducted to illustrate different aspects of the problem studied in this paper.

## 6.1. Solving the Nonlinear Formulation AMP

In the <sup>fi</sup>rst set of experiments, we solve the nonlinear integer program AMP using BARON (Sahinidis 2014), a state-of-the-art solver for nonlinear integer programs. These experiments are run on the NEOS Server (Gropp and More´ 1997, Czyzyk et al. 1998, Dolan 2001). The server machines are all dual-CPU multicore machines with at least 64 GB of RAM; the detailed hardware speci<sup>fi</sup>cations of the NEOS server machines are available at http://neos-guide.org/content/FAQ A time limit of one hour was imposed on each experiment, and the associated results are in Table 5.

Although BARON solved AMP in 31 of the 100 problems involved, these were the smaller problems considered in this paper—none of the larger problems could be solved within one hour. For the problems that were solved, the time taken increased signi<sup>fi</sup>cantly with the number of sensitive rules (which affects the number of constraints) and the number of relevant transactions (which is related to the number of variables in the formulation). In addition, the solver concluded with suboptimal solutions in 10 of the 31 instances solved.

## 6.2. Solving the Linearization LRH

The next set of experiments involve the solution of LRH, the linearized version of the problem. Table 6 presents the results of solving the linearization; it reports the times needed to solve LRH with and without the problem reduction results presented in Section 5. All the programs used in the experiments were implemented in C on a PC with 64 GB of RAM, running Windows 10 on an Intel i7-7700, 3.60 GHz processor; the integer programs were solved using CPLEX (IBM 2018).

Linearizing AMP helps considerably, with only 19 of the 100 problems being left unsolved after one hour. Reducing the size of the problem by incorporating the results from Propositions 1–4 makes a further substantive impact—not only was every problem solved optimally but they were solved in an average time of 13.29 seconds, with the longest taking a little over 5 minutes. The main drivers of these gains in solution times are the signi<sup>fi</sup>cant reductions in problem sizes and integrality gaps (i.e., the gaps between LRH and its linear programming relaxation, which can have an impact on the amount of time spent on integer programming branch and bound).

Table 7 shows the number of constraints impacted by Propositions 2–4. The impact of Proposition 1 is straightforward in that it eliminates exactly $| \mathcal { R } ^ { s } |$ constraints in every problem; therefore, this has not been reported in Table 7. The average number of sensitive rules across all our experiments was 75, and therefore, LRH in its original form will have $3 \times | \mathcal { R } ^ { S } |$ constraints. As a result, LRH before incorporating any of the propositions has an average of 225 constraints. Incorporating Proposition 1 brings the number of constraints down to $2 \times | \mathcal { R } ^ { S } |$ , or 150, on average.

Across all 100 experiments, on average, 26.13 constraints were eliminated as a result of Proposition 2 and 45.94 as a result of Proposition 3. Therefore, Propositions 1–3 together bring the number of relevant constraints down to 77.93, on average, approximately a third of the number of constraints in the original version of LRH. Proposition 4 potentially becomes relevant only for support constraints that have not been deleted as a result of Proposition 2 and consequently had limited impact, playing a role in only 2.93 constraints, on average.

When the con<sup>fi</sup>dence levels of the rules identi<sup>fi</sup>ed as sensitive were low, the number of constraints eliminated through Proposition 2 were high, indicating that it was usually preferable to hide rules based on con<sup>fi</sup>- dence rather than support. For example, when the maximum con<sup>fi</sup>dence levels of sensitive rules were 30% or less, an average of 50.6 constraints were eliminated as a result of Proposition 2, and only 19.36 were eliminated as a result of Proposition 3. As the maximum con<sup>fi</sup>- dence levels of the sensitive rules increased, it became less and less attractive to hide the rules based on con<sup>fi</sup>- dence. When the maximum con<sup>fi</sup>dence level was 90%, most of the constraints (63.88, on average) eliminated were through Proposition 3, with Proposition 2 accounting, on average, for only 9.6 constraints.

Table 8 provides the absolute integrality gaps for all the problems considered in this paper. The relative gaps averaged 43.38% before incorporating the Propositions 1–4 but were reduced to an average of 0.76% once these propositions were incorporated. The linear programming solution was integral in 8 of the 100 problems solved, with problems that had larger gaps taking longer to solve in general. Together, the signi<sup>fi</sup>cant reductions in problem size and the marked reductions in the integrality gaps help solve problems on data sets involving millions of transactions very quickly. In addition, the accuracies of the modi<sup>fi</sup>ed databases remain high, ranging between 96.08% and 99.98%, with an average accuracy of 99.01%. These results show that not only can sensitive information be hidden with limited damage to the data but also the approach presented in the paper makes it viable for large, real-world transactional databases.

We also conducted experiments on the 10-milliontransaction data set where we varied the hiding threshold for support. We tried two new hiding thresholds for support (0.05% and 0.15%). The same sensitive rules that were used in the original experiments (where the hiding threshold for support was 0.10%) were used in these experiments, to make comparisons easier. The results were as expected: as the hiding threshold for support increases (i.e., as hiding based on reducing support becomes easier), fewer transactions are sanitized. As the hiding threshold for support increases, so does the number of constraints eliminated based on Proposition 3, whereas the number of constraints eliminated based on Proposition 2 goes down. That is, more constraints that relate to hiding based on reducing con<sup>fi</sup>dence become redundant (and are eliminated) as the hiding threshold for support increases, implying that more rules will be hidden by lowering support.

One side effect of removing items from a database is the possibility of generating rules that were not generated when the original database was mined. For example, consider a potential rule r $( r ^ { a } \Rightarrow r ^ { c } )$ with support $\sigma _ { r }$ and con<sup>fi</sup>dence $\gamma _ { r }$ in the original (nonsanitized) data set. If $\sigma _ { r } \geq \sigma _ { \operatorname* { m i n } }$ and $\gamma _ { r } < \gamma _ { \mathrm { m i n } } ,$ this rule will not be generated because its con<sup>fi</sup>dence is below the corresponding mining threshold. Depending on the items removed as part of the solution to problems SAN and LRH, it is possible

Table 5. Results from Solving the Nonlinear Formulation AMP

<table><tr><td rowspan="3">Data set</td><td rowspan="3">No. of sensitive rules</td><td colspan="12">Confidence levels</td></tr><tr><td colspan="3">30%</td><td colspan="3">50%</td><td colspan="3">70%</td><td colspan="3">90%</td></tr><tr><td>No. of transactions sanitized</td><td>Accuracy (%)</td><td>Time (sec)</td><td>No. of transactions sanitized</td><td>Accuracy (%)</td><td>Time (sec)</td><td>No. of transactions sanitized</td><td>Accuracy (%)</td><td>Time (sec)</td><td>No. of transactions sanitized</td><td>Accuracy (%)</td><td>Time (sec)</td></tr><tr><td rowspan="5">retail</td><td>5</td><td>77</td><td>99.99</td><td>0.14</td><td>71</td><td>99.92</td><td>0.17</td><td>160</td><td>99.82</td><td>0.17</td><td>97</td><td>99.89</td><td>0.17</td></tr><tr><td>20</td><td>235</td><td>99.73</td><td>2.35</td><td>237</td><td>99.73</td><td>2.43</td><td>397</td><td>99.55</td><td>1.79</td><td>521</td><td>99.41</td><td>3.62</td></tr><tr><td>50</td><td> $384^a$ </td><td>99.56</td><td>1,370.68</td><td>618</td><td>99.30</td><td>34.76</td><td>976</td><td>98.89</td><td>12.26</td><td> $1,062^a$ </td><td>98.80</td><td>34.44</td></tr><tr><td>100</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>200</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td rowspan="5">bms-pos</td><td>5</td><td> $119^a$ </td><td>99.98</td><td>4.65</td><td>462</td><td>99.91</td><td>3.70</td><td>385</td><td>99.93</td><td>4.36</td><td>395</td><td>99.92</td><td>9.43</td></tr><tr><td>20</td><td> $464^a$ </td><td>99.91</td><td>198.37</td><td> $973^a$ </td><td>99.81</td><td>66.82</td><td>1,659</td><td>99.68</td><td>97.14</td><td>1,220</td><td>99.76</td><td>179.87</td></tr><tr><td>50</td><td>842</td><td>99.84</td><td>602.45</td><td>1,891</td><td>99.63</td><td>433.75</td><td> $1,748^a$ </td><td>99.66</td><td>297.74</td><td> $1,352^a$ </td><td>99.74</td><td>867.82</td></tr><tr><td>100</td><td>—</td><td>—</td><td>—</td><td> $1,977^a$ </td><td>99.62</td><td>1,247.12</td><td> $2,193^a$ </td><td>99.57</td><td>946.29</td><td> $1,833^a$ </td><td>99.64</td><td>971.36</td></tr><tr><td>200</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td rowspan="5">10m</td><td>5</td><td>12,274</td><td>99.88</td><td>2,156.08</td><td>12,616</td><td>99.87</td><td>1,393.68</td><td>13,748</td><td>99.86</td><td>1,295.78</td><td>13,919</td><td>99.86</td><td>1,567.84</td></tr><tr><td>20</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>50</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>100</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>200</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td rowspan="5">50m</td><td>5</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>20</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>50</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>100</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>200</td><td>-</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td rowspan="5">100m</td><td>5</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>20</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>50</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>100</td><td>—</td><td>—</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>200</td><td>—</td><td>—</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<sub>( inated</sub> <sub>with</sub> <sub>a</sub> <sub>s</sub>u<sup>boptimal</sup> <sup>so</sup> Note. The em dash (—) indicates that the problem was not solved within one hour.

Note. w/o Red., without reduction; with Red., with reduction (based on Propositions 1–4); the em dash (—) indicates that the problem was not solved within one hour.

<table><tr><td rowspan="4">Data set</td><td rowspan="4">No. of sensitive rules</td><td colspan="12">Confidence levels</td></tr><tr><td colspan="3">30%</td><td colspan="3">50%</td><td colspan="3">70%</td><td colspan="3">90%</td></tr><tr><td rowspan="2">No. of transactions sanitized</td><td colspan="2">Solution time (sec)</td><td rowspan="2">No. of transactions sanitized</td><td colspan="2">Solution time (sec)</td><td rowspan="2">No. of transactions sanitized</td><td colspan="2">Solution time (sec)</td><td rowspan="2">No. of transactions sanitized</td><td colspan="2">Solution time (sec)</td></tr><tr><td>w/o Red.</td><td>with Red.</td><td>w/o Red.</td><td>with Red.</td><td>w/o Red.</td><td>with Red.</td><td>w/o Red.</td><td>with Red.</td></tr><tr><td rowspan="5">retail</td><td>5</td><td>77</td><td>0.00</td><td>0.00</td><td>71</td><td>0.00</td><td>0.00</td><td>160</td><td>0.00</td><td>0.00</td><td>97</td><td>0.01</td><td>0.01</td></tr><tr><td>20</td><td>235</td><td>0.05</td><td>0.01</td><td>237</td><td>0.06</td><td>0.02</td><td>397</td><td>0.08</td><td>0.05</td><td>521</td><td>0.02</td><td>0.01</td></tr><tr><td>50</td><td>373</td><td>0.21</td><td>0.04</td><td>618</td><td>0.78</td><td>0.03</td><td>976</td><td>0.03</td><td>0.02</td><td>1,024</td><td>0.03</td><td>0.02</td></tr><tr><td>100</td><td>530</td><td>2.53</td><td>0.54</td><td>876</td><td>2.85</td><td>0.11</td><td>1,626</td><td>0.10</td><td>0.04</td><td>1,541</td><td>0.09</td><td>0.03</td></tr><tr><td>200</td><td>774</td><td>27.36</td><td>4.25</td><td>1,292</td><td>11.81</td><td>0.73</td><td>2,634</td><td>4.38</td><td>0.19</td><td>2,121</td><td>2.34</td><td>0.02</td></tr><tr><td rowspan="5">bms-pos</td><td>5</td><td>111</td><td>4.65</td><td>0.01</td><td>462</td><td>0.02</td><td>0.06</td><td>385</td><td>0.03</td><td>0.01</td><td>395</td><td>0.01</td><td>0.01</td></tr><tr><td>20</td><td>457</td><td>198.37</td><td>0.04</td><td>971</td><td>0.17</td><td>0.03</td><td>1,659</td><td>0.18</td><td>0.06</td><td>1,220</td><td>2.55</td><td>0.05</td></tr><tr><td>50</td><td>842</td><td>602.45</td><td>0.61</td><td>1,891</td><td>1.50</td><td>0.14</td><td>1,747</td><td>1.16</td><td>0.13</td><td>1,343</td><td>1.25</td><td>0.23</td></tr><tr><td>100</td><td>1,510</td><td>—</td><td>8.51</td><td>1,960</td><td>77.10</td><td>1.85</td><td>2,162</td><td>7.26</td><td>1.13</td><td>1,670</td><td>36.33</td><td>0.50</td></tr><tr><td>200</td><td>2,105</td><td>—</td><td>325.45</td><td>2,471</td><td>154.21</td><td>9.24</td><td>2,735</td><td>229.06</td><td>2.81</td><td>2,493</td><td>246.76</td><td>4.89</td></tr><tr><td rowspan="5">10m</td><td>5</td><td>12,274</td><td>0.76</td><td>0.06</td><td>12,616</td><td>0.77</td><td>0.05</td><td>13,748</td><td>0.71</td><td>0.05</td><td>13,919</td><td>0.37</td><td>0.05</td></tr><tr><td>20</td><td>37,154</td><td>4.50</td><td>0.27</td><td>68,332</td><td>4.74</td><td>0.30</td><td>46,345</td><td>3.23</td><td>0.24</td><td>66,091</td><td>2.90</td><td>0.28</td></tr><tr><td>50</td><td>73,565</td><td>15.05</td><td>0.72</td><td>112,579</td><td>16.47</td><td>0.76</td><td>118,638</td><td>13.31</td><td>0.79</td><td>148,685</td><td>13.66</td><td>0.81</td></tr><tr><td>100</td><td>98,311</td><td>36.07</td><td>1.13</td><td>171,442</td><td>37.47</td><td>1.46</td><td>193,924</td><td>33.35</td><td>1.52</td><td>226,422</td><td>35.08</td><td>1.62</td></tr><tr><td>200</td><td>117,698</td><td>67.43</td><td>1.76</td><td>233,588</td><td>81.33</td><td>3.14</td><td>294,212</td><td>80.83</td><td>3.86</td><td>342,223</td><td>87.67</td><td>3.10</td></tr><tr><td rowspan="5">50m</td><td>5</td><td>67,724</td><td>16.21</td><td>0.33</td><td>32,594</td><td>10.72</td><td>0.27</td><td>23,757</td><td>11.61</td><td>0.32</td><td>76,623</td><td>9.00</td><td>0.26</td></tr><tr><td>20</td><td>219,593</td><td>160.79</td><td>1.90</td><td>204,233</td><td>78.31</td><td>1.44</td><td>225,310</td><td>99.37</td><td>1.80</td><td>381,889</td><td>210.88</td><td>1.45</td></tr><tr><td>50</td><td>383,942</td><td>750.40</td><td>4.57</td><td>584,748</td><td>1,074.22</td><td>4.39</td><td>578,687</td><td>1,047.72</td><td>5.81</td><td>826,577</td><td>967.82</td><td>4.92</td></tr><tr><td>100</td><td>500,591</td><td>2,294.97</td><td>8.32</td><td>876,324</td><td>3,070.76</td><td>89.57</td><td>1,068,407</td><td>2,737.53</td><td>12.62</td><td>1,372,019</td><td>—</td><td>10.09</td></tr><tr><td>200</td><td>603,752</td><td>—</td><td>13.78</td><td>1,247,501</td><td>—</td><td>208.25</td><td>1,371,631</td><td>—</td><td>17.02</td><td>1,930,559</td><td>—</td><td>20.73</td></tr><tr><td rowspan="5">100m</td><td>5</td><td>95,539</td><td>122.02</td><td>0.60</td><td>89,337</td><td>112.24</td><td>0.49</td><td>137,520</td><td>199.19</td><td>0.61</td><td>206,019</td><td>360.88</td><td>0.59</td></tr><tr><td>20</td><td>325,496</td><td>1,435.26</td><td>2.92</td><td>497,164</td><td>2,098.35</td><td>3.20</td><td>518,007</td><td>1,036.92</td><td>43.74</td><td>828,627</td><td>1,047.66</td><td>3.43</td></tr><tr><td>50</td><td>685,512</td><td>—</td><td>7.84</td><td>1,395,943</td><td>—</td><td>9.90</td><td>1,038,620</td><td>—</td><td>7.95</td><td>1,503,890</td><td>—</td><td>9.70</td></tr><tr><td>100</td><td>1,038,197</td><td>—</td><td>14.82</td><td>2,030,581</td><td>—</td><td>18.94</td><td>1,902,826</td><td>—</td><td>17.56</td><td>2,337,655</td><td>—</td><td>19.63</td></tr><tr><td>200</td><td>1,159,894</td><td>—</td><td>24.56</td><td>2,762,765</td><td>—</td><td>18.70</td><td>2,830,741</td><td>—</td><td>34.35</td><td>3,474,653</td><td>—</td><td>35.34</td></tr></table>

Table 6. Results from Solving the Linearized Formulation LRH

Table 7. Impact of Propositions 2–4

<table><tr><td rowspan="4">Data set</td><td rowspan="4">No. of rules</td><td colspan="13">Confidence levels</td></tr><tr><td colspan="3">30%</td><td colspan="3">50%</td><td colspan="3">70%</td><td colspan="3">90%</td><td></td></tr><tr><td colspan="3">Proposition</td><td colspan="3">Proposition</td><td colspan="3">Proposition</td><td colspan="3">Proposition</td><td></td></tr><tr><td>2</td><td>3</td><td>4</td><td>2</td><td>3</td><td>4</td><td>2</td><td>3</td><td>4</td><td>2</td><td>3</td><td>4</td><td></td></tr><tr><td rowspan="5">retail</td><td>5</td><td>1</td><td>4</td><td>0</td><td>1</td><td>4</td><td>0</td><td>0</td><td>5</td><td>0</td><td>0</td><td>5</td><td>0</td><td></td></tr><tr><td>20</td><td>11</td><td>9</td><td>0</td><td>6</td><td>13</td><td>1</td><td>3</td><td>17</td><td>0</td><td>2</td><td>18</td><td>0</td><td></td></tr><tr><td>50</td><td>28</td><td>19</td><td>3</td><td>14</td><td>33</td><td>3</td><td>9</td><td>41</td><td>0</td><td>7</td><td>43</td><td>0</td><td></td></tr><tr><td>100</td><td>57</td><td>38</td><td>5</td><td>38</td><td>56</td><td>6</td><td>13</td><td>84</td><td>3</td><td>8</td><td>89</td><td>3</td><td></td></tr><tr><td>200</td><td>112</td><td>72</td><td>16</td><td>66</td><td>114</td><td>20</td><td>24</td><td>166</td><td>10</td><td>15</td><td>180</td><td>5</td><td></td></tr><tr><td rowspan="5">bms-pos</td><td>5</td><td>2</td><td>3</td><td>0</td><td>1</td><td>4</td><td>0</td><td>1</td><td>4</td><td>0</td><td>0</td><td>4</td><td>1</td><td></td></tr><tr><td>20</td><td>9</td><td>11</td><td>0</td><td>1</td><td>19</td><td>0</td><td>5</td><td>14</td><td>1</td><td>1</td><td>16</td><td>3</td><td></td></tr><tr><td>50</td><td>18</td><td>25</td><td>7</td><td>2</td><td>45</td><td>3</td><td>7</td><td>40</td><td>3</td><td>2</td><td>45</td><td>3</td><td></td></tr><tr><td>100</td><td>33</td><td>44</td><td>23</td><td>4</td><td>87</td><td>9</td><td>9</td><td>83</td><td>8</td><td>4</td><td>89</td><td>7</td><td></td></tr><tr><td>200</td><td>47</td><td>88</td><td>65</td><td>13</td><td>163</td><td>24</td><td>14</td><td>171</td><td>15</td><td>5</td><td>183</td><td>12</td><td></td></tr><tr><td rowspan="5">10m</td><td>5</td><td>4</td><td>1</td><td>0</td><td>2</td><td>3</td><td>0</td><td>1</td><td>4</td><td>0</td><td>1</td><td>4</td><td>0</td><td></td></tr><tr><td>20</td><td>17</td><td>3</td><td>0</td><td>7</td><td>13</td><td>0</td><td>3</td><td>17</td><td>0</td><td>5</td><td>15</td><td>0</td><td></td></tr><tr><td>50</td><td>38</td><td>12</td><td>0</td><td>22</td><td>28</td><td>0</td><td>12</td><td>38</td><td>0</td><td>9</td><td>41</td><td>0</td><td></td></tr><tr><td>100</td><td>80</td><td>20</td><td>0</td><td>45</td><td>55</td><td>0</td><td>30</td><td>70</td><td>0</td><td>17</td><td>82</td><td>1</td><td></td></tr><tr><td>200</td><td>162</td><td>36</td><td>2</td><td>90</td><td>107</td><td>3</td><td>65</td><td>132</td><td>3</td><td>35</td><td>164</td><td>1</td><td></td></tr><tr><td rowspan="5">50m</td><td>5</td><td>4</td><td>1</td><td>0</td><td>2</td><td>3</td><td>0</td><td>2</td><td>3</td><td>0</td><td>0</td><td>5</td><td>0</td><td></td></tr><tr><td>20</td><td>17</td><td>3</td><td>0</td><td>11</td><td>9</td><td>0</td><td>4</td><td>16</td><td>0</td><td>0</td><td>20</td><td>0</td><td></td></tr><tr><td>50</td><td>44</td><td>6</td><td>0</td><td>23</td><td>26</td><td>1</td><td>16</td><td>34</td><td>0</td><td>6</td><td>44</td><td>0</td><td></td></tr><tr><td>100</td><td>86</td><td>14</td><td>0</td><td>49</td><td>47</td><td>4</td><td>32</td><td>68</td><td>0</td><td>16</td><td>84</td><td>0</td><td></td></tr><tr><td>200</td><td>170</td><td>27</td><td>3</td><td>95</td><td>97</td><td>8</td><td>63</td><td>136</td><td>1</td><td>36</td><td>164</td><td>0</td><td></td></tr><tr><td rowspan="5">100m</td><td>5</td><td>5</td><td>0</td><td>0</td><td>2</td><td>3</td><td>0</td><td>3</td><td>2</td><td>0</td><td>2</td><td>3</td><td>0</td><td></td></tr><tr><td>20</td><td>17</td><td>3</td><td>0</td><td>7</td><td>13</td><td>0</td><td>6</td><td>13</td><td>1</td><td>5</td><td>15</td><td>0</td><td></td></tr><tr><td>50</td><td>44</td><td>6</td><td>0</td><td>19</td><td>31</td><td>0</td><td>18</td><td>32</td><td>0</td><td>7</td><td>43</td><td>0</td><td></td></tr><tr><td>100</td><td>87</td><td>13</td><td>0</td><td>45</td><td>55</td><td>0</td><td>38</td><td>62</td><td>0</td><td>19</td><td>80</td><td>1</td><td></td></tr><tr><td>200</td><td>172</td><td>26</td><td>2</td><td>96</td><td>102</td><td>2</td><td>69</td><td>131</td><td>0</td><td>38</td><td>161</td><td>1</td><td></td></tr></table>

that the support of the antecedent $r ^ { \mu }$ will decrease enough to make the con<sup>fi</sup>dence of r in the sanitized data set greater than $\gamma _ { \mathrm { m i n } }$ (whereas the support for r remains above $\sigma _ { \mathrm { m i n } } )$ . The number of such spurious rules—rules that show up when they should not based on the original data set—is a function of the sanitization method used. So too are the number of rules that existed in the original data set and are missing from the sanitized one—the number of lost rules. A more drastic sanitization approach (such as the blanket approach) is likely to have a more adverse impact on both these metrics than a more selective approach such as the one presented in Section 4. Table 9 provides information on the extent of these two side effects. The fraction of spurious rules generated is low in all the experiments, suggesting that this is not of great concern. On average, spurious rules comprised 0.00%–3.73% of the rules generated from the sanitized data set, with the average fraction being 0.9% over the 100 problems solved. On average, 10.61% of the original rules were lost, with the extent of the loss increasing with the number of sensitive rules to be hidden. The loss was most perceptible for bms-pos, which lost an average of 34.12% of its original rules. This is expected, because bms-pos is an aggregated (categorylevel) data set and therefore denser. The losses for the other four data sets were signi<sup>fi</sup>cantly better, with retail, 10m, 50m, and 100m losing 7.22%, 3.82%, 3.74%, and 4.18% of their original rules, respectively.

## 6.3. Hiding Sensitive Rules vs. Hiding the Corresponding Itemsets

Hiding itemsets automatically hides all rules that can be generated from them. Doing so, however, could come at the expense of more transactions getting sanitized. We conduct a set of experiments to compare the number of transactions sanitized when hiding sensitive association rules with that when hiding the itemsets corresponding to the sensitive rules (which is also an NP-hard problem). The results of these experiments are in Table 10; the hiding thresholds for support and con<sup>fi</sup>dence were 0.1% and 20%, respectively, in each of these experiments.

Across all 100 experiments, an average of 45.90% more transactions were sanitized when hiding itemsets rather than rules. Broken up by con<sup>fi</sup>dence category, the average number of excess transactions sanitized when hiding the itemsets were 110.33% when the con<sup>fi</sup>dence levels of the sensitive rules are between 20% and 30%, and the corresponding values were 34.75%, 26.99%, and 11.51% when the con<sup>fi</sup>dence levels of the sensitive rules are between 20% and 50%, 20% and 70%, and 20% and 90%, respectively. Rules with very high con<sup>fi</sup>dence are less likely to be unexpected and less likely to be sensitive. The reverse is likely to be true for rules with lower con<sup>fi</sup>dence levels, and therefore, it is more likely that sensitive rules fall into this category. So although fewer transactions need to be sanitized in general when sanitizing sensitive rules, the reduction is particularly pronounced when the con<sup>fi</sup>dence levels of the rules being hidden are low—exactly the rules that are more likely to be sensitive. These experiments show that there is bene<sup>fi</sup>t to sanitizing databases by hiding the sensitive rules directly, rather than by hiding the corresponding itemsets.

Table 8. Integrality Gaps

<table><tr><td rowspan="3">Data set</td><td rowspan="3">No. of sensitive rules</td><td colspan="8">Confidence levels</td></tr><tr><td colspan="2">30%</td><td colspan="2">50%</td><td colspan="2">70%</td><td colspan="2">90%</td></tr><tr><td>w/o Red.</td><td>with Red.</td><td>w/o Red.</td><td>with Red.</td><td>w/o Red.</td><td>with Red.</td><td>w/o Red.</td><td>with Red.</td></tr><tr><td rowspan="5">retail</td><td>5</td><td>31.76</td><td>0.80</td><td>27.83</td><td>0.60</td><td>58.17</td><td>0.00</td><td>29.83</td><td>0.00</td></tr><tr><td>20</td><td>109.75</td><td>3.00</td><td>119.49</td><td>3.14</td><td>150.40</td><td>1.40</td><td>196.87</td><td>0.20</td></tr><tr><td>50</td><td>176.87</td><td>4.90</td><td>309.55</td><td>6.49</td><td>436.34</td><td>2.00</td><td>434.23</td><td>0.40</td></tr><tr><td>100</td><td>250.60</td><td>11.27</td><td>446.75</td><td>12.15</td><td>803.68</td><td>5.19</td><td>672.41</td><td>0.20</td></tr><tr><td>200</td><td>382.15</td><td>19.91</td><td>659.85</td><td>16.67</td><td>1,305.14</td><td>9.41</td><td>930.42</td><td>1.04</td></tr><tr><td rowspan="5">bms-pos</td><td>5</td><td>38.84</td><td>0.00</td><td>207.93</td><td>0.60</td><td>173.26</td><td>0.00</td><td>180.38</td><td>2.40</td></tr><tr><td>20</td><td>216.19</td><td>1.44</td><td>523.17</td><td>0.60</td><td>841.41</td><td>14.60</td><td>699.97</td><td>50.33</td></tr><tr><td>50</td><td>488.54</td><td>58.60</td><td>1,146.26</td><td>54.07</td><td>887.75</td><td>20.74</td><td>731.25</td><td>45.07</td></tr><tr><td>100</td><td>916.24</td><td>123.50</td><td>1,095.57</td><td>40.56</td><td>1,132.03</td><td>13.00</td><td>885.83</td><td>56.80</td></tr><tr><td>200</td><td>1,351.03</td><td>300.38</td><td>1,402.54</td><td>32.58</td><td>1,440.59</td><td>81.75</td><td>1,278.33</td><td>61.87</td></tr><tr><td rowspan="5">10m</td><td>5</td><td>4,285.80</td><td>1.00</td><td>4,684.83</td><td>0.60</td><td>5,297.83</td><td>0.40</td><td>4,485.07</td><td>0.00</td></tr><tr><td>20</td><td>13,817.85</td><td>3.60</td><td>29,010.16</td><td>2.60</td><td>17,682.72</td><td>20.40</td><td>25,179.60</td><td>1.40</td></tr><tr><td>50</td><td>29,462.28</td><td>9.00</td><td>48,130.38</td><td>4.00</td><td>50,297.00</td><td>1.80</td><td>59,623.70</td><td>2.60</td></tr><tr><td>100</td><td>41,471.75</td><td>14.80</td><td>75,942.75</td><td>7.40</td><td>84,921.10</td><td>4.80</td><td>90,280.18</td><td>5.00</td></tr><tr><td>200</td><td>51,552.61</td><td>15.30</td><td>105,636.14</td><td>1191.19</td><td>130,400.20</td><td>1,173.03</td><td>141,288.13</td><td>6.00</td></tr><tr><td rowspan="5">50m</td><td>5</td><td>26,085.03</td><td>0.80</td><td>8,914.71</td><td>0.40</td><td>4,622.45</td><td>1.00</td><td>30,744.38</td><td>0.00</td></tr><tr><td>20</td><td>87,750.22</td><td>3.40</td><td>83,160.64</td><td>1.40</td><td>85,874.34</td><td>1.80</td><td>145,224.12</td><td>0.00</td></tr><tr><td>50</td><td>157,240.05</td><td>7.00</td><td>258,668.31</td><td>5946.92</td><td>237,707.28</td><td>2.80</td><td>321,017.28</td><td>1.80</td></tr><tr><td>100</td><td>211,351.36</td><td>10.60</td><td>391,030.37</td><td>6208.83</td><td>454,337.67</td><td>4.00</td><td>554,909.40</td><td>4.80</td></tr><tr><td>200</td><td>261,123.68</td><td>3017.24</td><td>576,214.00</td><td>6199.63</td><td>602,762.03</td><td>5.80</td><td>809,542.88</td><td>5.60</td></tr><tr><td rowspan="5">100m</td><td>5</td><td>30,623.20</td><td>2.40</td><td>26,439.89</td><td>0.80</td><td>49,393.53</td><td>1.20</td><td>76,079.58</td><td>0.00</td></tr><tr><td>20</td><td>120,147.48</td><td>4.80</td><td>204,295.45</td><td>1.40</td><td>203,838.82</td><td>1.80</td><td>321,016.31</td><td>1.00</td></tr><tr><td>50</td><td>271,950.23</td><td>8.20</td><td>638,040.88</td><td>4.00</td><td>428,093.70</td><td>1.20</td><td>564,656.96</td><td>1.80</td></tr><tr><td>100</td><td>432,950.03</td><td>9.40</td><td>917,705.65</td><td>6.40</td><td>811,970.29</td><td>4.60</td><td>897,701.24</td><td>3.00</td></tr><tr><td>200</td><td>491,055.51</td><td>6,112.03</td><td>1,292,463.17</td><td>8.00</td><td>1,232,834.44</td><td>4.60</td><td>1,397,579.05</td><td>4.20</td></tr></table>

Note. w/o Red., without reduction; with Red., with reduction (based on Propositions 1–4).

We also conducted similar experiments using three benchmarks from the literature: algorithms 2.a and 2.b from Verykios et al. (2004) and the method proposed by Telikani and Shahbahrami (2017). The results of these experiments are in Table 11. In general, these benchmarks could not <sup>fi</sup>nd solutions for more than half the problems considered, even after 24 hours. In addition, their performances on the problems where they could <sup>fi</sup>nd solutions in 24 hours were much worse than the corresponding solutions of the optimal approach.

Algorithms 2.a and 2.b of Verykios et al. (2004) identi<sup>fi</sup>ed solutions for 40 of the 100 problems across the <sup>fi</sup>ve data sets within the 24-hour limit. Speci<sup>fi</sup>cally, they solved all 20 problems associated with retail, 16 of 20 associated with bms-pos, the 4 problems involving <sup>fi</sup>ve sensitive rules associated with 10m, and none of the problems associated with 50m or 100m. Across these problems, the average solution times were 5,138.18 and 5,024.32 seconds for algorithms 2.a and 2.b, respectively, and the average numbers of transactions sanitized were 13,549.93 and 5,307.80, respectively. By contrast, the optimal approach sanitized 2,188.05 transactions across these 40 problems while taking an average of 0.49 seconds. The approach of Telikani and Shahbahrami (2017) solved 49 of the 100 problems within 24 hours: all 40 associated with retail and bms-pos and the 4 problems involving <sup>fi</sup>ve sensitive rules associated with each of 10m and 50m. The average solution time across these 48 problems was 4,114.55 seconds, and the average number of transactions sanitized was 16,418.83. On the other hand, the optimal approach sanitized 6,208.83 transactions across these 48 problems in an average of 7.57 seconds. These experiments establish the signi<sup>fi</sup>cant gains to be made by using the optimal approach: whereas the benchmarks could not solve more than half of the problems considered in our experiments within 24 hours, the optimal approach solved them in 13.29 seconds, on average. In addition, the numbers of transactions sanitized by the benchmarks were many multiples more than the numbers sanitized by the corresponding optimal approach.

Table 9. Spurious Rules Generated and Rules Lost

<table><tr><td rowspan="3">Data set</td><td rowspan="3">No. of sensitive rules</td><td colspan="8">Confidence levels</td></tr><tr><td colspan="2">30%</td><td colspan="2">50%</td><td colspan="2">70%</td><td colspan="2">90%</td></tr><tr><td>Spurious</td><td>Lost</td><td>Spurious</td><td>Lost</td><td>Spurious</td><td>Lost</td><td>Spurious</td><td>Lost</td></tr><tr><td rowspan="5">retail</td><td>5</td><td>0</td><td>42</td><td>0</td><td>44</td><td>0</td><td>70</td><td>1</td><td>47</td></tr><tr><td>20</td><td>0</td><td>168</td><td>1</td><td>170</td><td>1</td><td>220</td><td>2</td><td>256</td></tr><tr><td>50</td><td>0</td><td>349</td><td>2</td><td>485</td><td>1</td><td>485</td><td>0</td><td>596</td></tr><tr><td>100</td><td>1</td><td>602</td><td>7</td><td>740</td><td>1</td><td>891</td><td>0</td><td>926</td></tr><tr><td>200</td><td>2</td><td>812</td><td>5</td><td>1,072</td><td>2</td><td>1,549</td><td>1</td><td>1,426</td></tr><tr><td rowspan="5">bms-pos</td><td>5</td><td>7</td><td>18,311</td><td>0</td><td>63,504</td><td>1</td><td>56,055</td><td>3</td><td>41,812</td></tr><tr><td>20</td><td>278</td><td>59,631</td><td>13</td><td>111,336</td><td>6</td><td>137,105</td><td>3</td><td>134,596</td></tr><tr><td>50</td><td>7</td><td>107,852</td><td>245</td><td>169,343</td><td>18</td><td>176,148</td><td>22</td><td>181,487</td></tr><tr><td>100</td><td>7</td><td>150,862</td><td>15</td><td>209,642</td><td>218</td><td>208,820</td><td>676</td><td>218,735</td></tr><tr><td>200</td><td>1,345</td><td>204,412</td><td>428</td><td>235,006</td><td>38</td><td>241,778</td><td>535</td><td>251,520</td></tr><tr><td rowspan="5">10m</td><td>5</td><td>0</td><td>4</td><td>0</td><td>25</td><td>0</td><td>619</td><td>160</td><td>1,130</td></tr><tr><td>20</td><td>1,204</td><td>1,317</td><td>114</td><td>819</td><td>182</td><td>1,875</td><td>224</td><td>2,080</td></tr><tr><td>50</td><td>2,477</td><td>2,803</td><td>1,389</td><td>2,385</td><td>1,093</td><td>5,441</td><td>385</td><td>3,551</td></tr><tr><td>100</td><td>3,703</td><td>4,219</td><td>1,444</td><td>5,703</td><td>1,644</td><td>7,520</td><td>1,567</td><td>7,448</td></tr><tr><td>200</td><td>2,846</td><td>4,817</td><td>1,855</td><td>6,776</td><td>1,930</td><td>9,303</td><td>3,567</td><td>11,048</td></tr><tr><td rowspan="5">50m</td><td>5</td><td>972</td><td>978</td><td>0</td><td>7</td><td>0</td><td>52</td><td>0</td><td>181</td></tr><tr><td>20</td><td>2,222</td><td>2,304</td><td>1,347</td><td>1,804</td><td>727</td><td>2,452</td><td>15</td><td>617</td></tr><tr><td>50</td><td>3,198</td><td>3,403</td><td>2,528</td><td>3,501</td><td>1,837</td><td>4,219</td><td>15</td><td>3,682</td></tr><tr><td>100</td><td>3,528</td><td>3,841</td><td>3,065</td><td>5,143</td><td>2,453</td><td>6,245</td><td>1,190</td><td>6,899</td></tr><tr><td>200</td><td>2,316</td><td>4,980</td><td>2,025</td><td>6,921</td><td>3,304</td><td>8,965</td><td>1,720</td><td>11,043</td></tr><tr><td rowspan="5">100m</td><td>5</td><td>1,204</td><td>1,210</td><td>0</td><td>16</td><td>736</td><td>1,340</td><td>753</td><td>1,758</td></tr><tr><td>20</td><td>2,263</td><td>2,380</td><td>0</td><td>2,160</td><td>1,763</td><td>3,698</td><td>800</td><td>3,082</td></tr><tr><td>50</td><td>2,631</td><td>2,889</td><td>834</td><td>4,362</td><td>2,552</td><td>4,924</td><td>754</td><td>4,615</td></tr><tr><td>100</td><td>2,438</td><td>5,038</td><td>1,017</td><td>5,129</td><td>3,038</td><td>5,924</td><td>1,886</td><td>8,058</td></tr><tr><td>200</td><td>1,880</td><td>4,729</td><td>1,837</td><td>6,819</td><td>1,711</td><td>8,143</td><td>1,879</td><td>9,940</td></tr></table>

## 7. Conclusions

Although the bene<sup>fi</sup>ts of sharing transactional pointof-sale data to improving supply chain performance have been recognized for decades, suppliers have only recently realized that the potential bene<sup>fi</sup>ts go far beyond that, and they have started mining the data to their advantage. However, many retailers have been hesitant to share transactional data, with the fear of divulging sensitive information leading to this reluctance. Consequently, if sensitive information could be effectively suppressed, more retailers are likely to share.

Transactional data are commonly mined to identify association rules. In this environment, sensitive information could be the result of successful bundling and other promotion strategies or surprising rules identi-<sup>fi</sup>ed while mining that can be taken advantage of to extract business value. The data owner would not want the relationships implied by these rules to be revealed, and effectively hiding these relationships prior to sharing would go a long way in alleviating the data owner’s concerns.

We consider the problem of maximizing the accuracy of shared transactional databases when some of the association rules are deemed sensitive and need to be hidden before the data can be shared. Solving this problem with the least possible impact on data quality would allow the retailer to generate business value while tempering risk. To our knowledge, this is the <sup>fi</sup>rst paper to present optimal approaches to solving this problem. We <sup>fi</sup>rst present an exact, but very large, nonlinear integer program to solve the problem, and we motivate how it can be decomposed into two related problems—a sanitization problem and an accuracy maximization problem—that allow the overall problem to be solved more easily. We formulate the sanitization problem as an integer program and develop a heuristic based on intuition from the formulation to solve it. We then show how the nonlinear integer formulation of the accuracy maximization problem can be linearized, and we present several results to reduce problem size. We conduct extensive computational experiments that show that although the nonlinear problem is very dif<sup>fi</sup>cult to solve, the linearization and the problem reduction steps reduce the time needed for solution substantially. We also <sup>fi</sup>nd that hiding the rules directly—rather than hiding the itemsets associated with them—can result in far fewer transactions being marked for sanitization. This bene<sup>fi</sup>t is observed to be more pronounced as the con<sup>fi</sup>dence levels of the sensitive rules are reduced. Given that rules with high con<sup>fi</sup>dence are less likely to be unexpected (and therefore, sensitive), this suggests that hiding the rules directly is likely to have a perceptible impact on the number of transactions affected more often than not. The process of hiding sensitive rules does not impact the quality of the sanitized data sets signi<sup>fi</sup>cantly: the average accuracy across the 100 problems solved was about 99% of the original data sets, on average.

Table 10. Hiding Rules vs. Itemsets: Impact on Accuracy

<table><tr><td rowspan="4">Data set</td><td rowspan="4">No. of sensitive rules</td><td colspan="12">Confidence levels</td></tr><tr><td colspan="3">30%</td><td colspan="3">50%</td><td colspan="3">70%</td><td colspan="3">90%</td></tr><tr><td colspan="2">No. of transactions sanitized</td><td rowspan="2">Excess (%)</td><td colspan="2">No. of transactions sanitized</td><td rowspan="2">Excess (%)</td><td colspan="2">No. of transactions sanitized</td><td rowspan="2">Excess (%)</td><td colspan="2">No. of transactions sanitized</td><td rowspan="2">Excess (%)</td></tr><tr><td>Rules</td><td>Itemsets</td><td>Rules</td><td>Itemsets</td><td>Rules</td><td>Itemsets</td><td>Rules</td><td>Itemsets</td></tr><tr><td rowspan="5">retail</td><td>5</td><td>77</td><td>91</td><td>18.18</td><td>71</td><td>119</td><td>67.61</td><td>160</td><td>160</td><td>0.00</td><td>97</td><td>97</td><td>0.00</td></tr><tr><td>20</td><td>235</td><td>435</td><td>85.11</td><td>237</td><td>374</td><td>57.81</td><td>397</td><td>447</td><td>12.59</td><td>521</td><td>612</td><td>17.47</td></tr><tr><td>50</td><td>373</td><td>939</td><td>151.74</td><td>618</td><td>930</td><td>50.49</td><td>976</td><td>1,122</td><td>14.96</td><td>1,024</td><td>1,232</td><td>20.31</td></tr><tr><td>100</td><td>530</td><td>1,353</td><td>155.28</td><td>876</td><td>1,393</td><td>59.02</td><td>1,626</td><td>1,885</td><td>15.93</td><td>1,541</td><td>1,765</td><td>14.54</td></tr><tr><td>200</td><td>774</td><td>1,900</td><td>145.48</td><td>1,292</td><td>2,006</td><td>55.26</td><td>2,634</td><td>2,934</td><td>11.39</td><td>2,121</td><td>2,362</td><td>11.36</td></tr><tr><td rowspan="5">bms-pos</td><td>5</td><td>111</td><td>331</td><td>198.20</td><td>462</td><td>560</td><td>21.21</td><td>385</td><td>467</td><td>21.30</td><td>395</td><td>395</td><td>0.00</td></tr><tr><td>20</td><td>457</td><td>1,123</td><td>145.73</td><td>971</td><td>1,062</td><td>9.37</td><td>1,659</td><td>2,423</td><td>46.05</td><td>1,220</td><td>1,482</td><td>21.48</td></tr><tr><td>50</td><td>842</td><td>1,835</td><td>117.93</td><td>1,891</td><td>2,152</td><td>13.80</td><td>1,747</td><td>2,276</td><td>30.28</td><td>1,343</td><td>1,584</td><td>17.94</td></tr><tr><td>100</td><td>1,510</td><td>2,963</td><td>96.23</td><td>1,960</td><td>2,149</td><td>9.64</td><td>2,162</td><td>2,551</td><td>17.99</td><td>1,670</td><td>2,015</td><td>20.66</td></tr><tr><td>200</td><td>2,105</td><td>3,676</td><td>74.63</td><td>2,471</td><td>3,175</td><td>28.49</td><td>2,735</td><td>3,084</td><td>12.76</td><td>2,493</td><td>2,744</td><td>10.07</td></tr><tr><td rowspan="5">10m</td><td>5</td><td>12,274</td><td>26,121</td><td>112.82</td><td>12,616</td><td>18,861</td><td>49.50</td><td>13,748</td><td>16,386</td><td>19.19</td><td>13,919</td><td>15,938</td><td>14.51</td></tr><tr><td>20</td><td>37,154</td><td>77,589</td><td>108.83</td><td>68,332</td><td>82,384</td><td>20.56</td><td>46,345</td><td>50,584</td><td>9.15</td><td>66,091</td><td>70,299</td><td>6.37</td></tr><tr><td>50</td><td>73,565</td><td>148,739</td><td>102.19</td><td>112,579</td><td>147,421</td><td>30.95</td><td>118,638</td><td>140,418</td><td>18.36</td><td>148,685</td><td>163,829</td><td>10.19</td></tr><tr><td>100</td><td>98,311</td><td>192,152</td><td>95.45</td><td>171,442</td><td>226,823</td><td>32.30</td><td>193,924</td><td>240,771</td><td>24.16</td><td>226,422</td><td>251,050</td><td>10.88</td></tr><tr><td>200</td><td>117,698</td><td>233,177</td><td>98.11</td><td>233,588</td><td>312,801</td><td>33.91</td><td>294,212</td><td>356,943</td><td>21.32</td><td>342,223</td><td>381,756</td><td>11.55</td></tr><tr><td rowspan="5">50m</td><td>5</td><td>67,724</td><td>120,846</td><td>78.44</td><td>32,594</td><td>59,367</td><td>82.14</td><td>23,757</td><td>54,784</td><td>130.60</td><td>76,623</td><td>76,623</td><td>0.00</td></tr><tr><td>20</td><td>219,593</td><td>417,911</td><td>90.31</td><td>204,233</td><td>256,535</td><td>25.61</td><td>225,310</td><td>270,741</td><td>20.16</td><td>381,889</td><td>381,889</td><td>0.00</td></tr><tr><td>50</td><td>383,942</td><td>766,717</td><td>99.70</td><td>584,748</td><td>691,479</td><td>18.25</td><td>578,687</td><td>716,897</td><td>23.88</td><td>826,577</td><td>870,700</td><td>5.34</td></tr><tr><td>100</td><td>500,591</td><td>1,021,664</td><td>104.09</td><td>876,324</td><td>1,148,909</td><td>31.11</td><td>1,068,407</td><td>1,290,594</td><td>20.80</td><td>1,372,019</td><td>1,500,762</td><td>9.38</td></tr><tr><td>200</td><td>603,752</td><td>1,196,086</td><td>98.11</td><td>1,247,501</td><td>1,606,858</td><td>28.81</td><td>1,371,631</td><td>1,633,615</td><td>19.10</td><td>1,930,559</td><td>2,138,268</td><td>10.76</td></tr><tr><td rowspan="5">100m</td><td>5</td><td>95,539</td><td>241,021</td><td>152.27</td><td>89,337</td><td>143,070</td><td>60.15</td><td>137,520</td><td>280,826</td><td>104.21</td><td>206,019</td><td>259,779</td><td>26.09</td></tr><tr><td>20</td><td>325,496</td><td>694,664</td><td>113.42</td><td>497,164</td><td>596,753</td><td>20.03</td><td>518,007</td><td>623,587</td><td>20.38</td><td>828,627</td><td>897,912</td><td>8.36</td></tr><tr><td>50</td><td>685,512</td><td>1,449,876</td><td>111.50</td><td>1,395,943</td><td>1,606,808</td><td>15.11</td><td>1,038,620</td><td>1,189,394</td><td>14.52</td><td>1,503,890</td><td>1,642,945</td><td>9.25</td></tr><tr><td>100</td><td>1,038,197</td><td>2,051,741</td><td>97.63</td><td>2,030,581</td><td>2,431,379</td><td>19.74</td><td>1,902,826</td><td>2,310,907</td><td>21.45</td><td>2,337,655</td><td>2,700,034</td><td>15.50</td></tr><tr><td>200</td><td>1,159,894</td><td>2,399,335</td><td>106.86</td><td>2,762,765</td><td>3,531,809</td><td>27.84</td><td>2,830,741</td><td>3,517,243</td><td>24.25</td><td>3,474,653</td><td>4,025,320</td><td>15.85</td></tr></table>

algorithm 2.b); T&S, Telikani and Shahbahrami (2017). Notes. A time limit of 24 hours was imposed. An em dash (—) indicates that the problem was not solved within 24 hours. V2a, Verykios et al. (2004, algorithm 2.a); V2b, Verykios et al. (2004,  
<sub>11.</sub> <sub>Bench</sub>m<sup>ark</sup> <sup>Experi</sup>

<table><tr><td rowspan="4">Data set</td><td rowspan="4">No. of sensitive rules</td><td colspan="12">Confidence levels</td></tr><tr><td colspan="3">30%</td><td colspan="3">50%</td><td colspan="3">70%</td><td colspan="3">90%</td></tr><tr><td colspan="3">No. of transactions sanitized</td><td colspan="3">No. of transactions sanitized</td><td colspan="3">No. of transactions sanitized</td><td colspan="3">No. of transactions sanitized</td></tr><tr><td>V2a</td><td>V2b</td><td>T&amp;S</td><td>V2a</td><td>V2b</td><td>T&amp;S</td><td>V2a</td><td>V2b</td><td>T&amp;S</td><td>V2a</td><td>V2b</td><td>T&amp;S</td></tr><tr><td rowspan="5">retail</td><td>5</td><td>481</td><td>100</td><td>132</td><td>480</td><td>128</td><td>152</td><td>600</td><td>170</td><td>351</td><td>537</td><td>107</td><td>353</td></tr><tr><td>20</td><td>1,787</td><td>596</td><td>454</td><td>1,910</td><td>490</td><td>602</td><td>2,181</td><td>549</td><td>1,189</td><td>2,283</td><td>759</td><td>1,474</td></tr><tr><td>50</td><td>3,566</td><td>1,554</td><td>958</td><td>4,221</td><td>1,373</td><td>1,620</td><td>5,292</td><td>1,605</td><td>2,947</td><td>5,313</td><td>1,745</td><td>3,378</td></tr><tr><td>100</td><td>7,129</td><td>2,865</td><td>1,793</td><td>7,051</td><td>2,719</td><td>2,718</td><td>9,541</td><td>3,249</td><td>5,809</td><td>9,261</td><td>3,071</td><td>6,226</td></tr><tr><td>200</td><td>11,704</td><td>5,112</td><td>3,058</td><td>11,293</td><td>4,814</td><td>4,785</td><td>16,101</td><td>6,539</td><td>10,486</td><td>15,065</td><td>5,706</td><td>10,949</td></tr><tr><td rowspan="5">bms-pos</td><td>5</td><td>2,056</td><td>499</td><td>600</td><td>2,920</td><td>808</td><td>1,621</td><td>2,775</td><td>835</td><td>1,464</td><td>2,616</td><td>599</td><td>1,647</td></tr><tr><td>20</td><td>5,685</td><td>2,704</td><td>2,393</td><td>7,879</td><td>2,225</td><td>5,144</td><td>9,812</td><td>4,842</td><td>5,386</td><td>8,341</td><td>3,200</td><td>5,826</td></tr><tr><td>50</td><td>12,684</td><td>6,777</td><td>5,695</td><td>15,435</td><td>6,519</td><td>10,987</td><td>16,078</td><td>7,640</td><td>10,923</td><td>14,349</td><td>6,634</td><td>11,449</td></tr><tr><td>100</td><td>19,984</td><td>13,905</td><td>10,582</td><td>22,928</td><td>11,565</td><td>17,221</td><td>23,167</td><td>11,991</td><td>16,962</td><td>21,539</td><td>10,527</td><td>17,313</td></tr><tr><td>200</td><td>—</td><td>—</td><td>18,195</td><td>—</td><td>—</td><td>25,672</td><td>—</td><td>—</td><td>26,501</td><td>—</td><td>—</td><td>25,687</td></tr><tr><td rowspan="5">10m</td><td>5</td><td>60,235</td><td>26,307</td><td>15,371</td><td>56,487</td><td>18,967</td><td>21,998</td><td>59,419</td><td>16,473</td><td>24,923</td><td>61,812</td><td>16,044</td><td>35,530</td></tr><tr><td>20</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>50</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>100</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>200</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td rowspan="5">50m</td><td>5</td><td>—</td><td>—</td><td>75,692</td><td>—</td><td>—</td><td>104,556</td><td>—</td><td>—</td><td>84,079</td><td>—</td><td>—</td><td>145,253</td></tr><tr><td>20</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>50</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>100</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>200</td><td>-</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td rowspan="5">100m</td><td>5</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>20</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>50</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>100</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>200</td><td>一</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr></table>

These results suggest that the impact of sanitizing a transactional data set to suppress sensitive rules would be marginal if conducted using the proposed approach and that the receiver of the data should still be able to extract substantial value from the sanitized data set. This should, in turn, mitigate data owners’ concerns and increase the incidence of transactional data sharing among business partners.

A related aspect of the problem not explicitly considered here is that sharing is often a repetitive process, and there is the possibility of rules being deemed sensitive after some sharing has already occurred. If this is a result of new sensitive rules being created as a result of new items getting added over time, there is no reason to worry, as the rule could not exist in previously shared data. What could be risky is a situation where a rule that was originally not sensitive gets deemed sensitive at a later time. It is unlikely, however, for a known relationship to suddenly get deemed sensitive. Therefore, the identi<sup>fi</sup>cation of new sensitive rules over time may not be a signi<sup>fi</sup>cant cause for concern. Nevertheless, if there are rules that the data owner suspects could become sensitive later, the data owner should be conservative in identifying sensitive rules when the decision to share is made, so situations like this can be avoided.

## Appendix A. Proofs of Propositions

Proposition 1. There is always an optimal solution where $y _ { r } + z _ { r } = 1$

Proof. Setting $y _ { r }$ and $z _ { r }$ to 1 implies that both the support and con<sup>fi</sup>dence are being lowered below the speci-<sup>fi</sup>ed thresholds. As hiding is accomplished by lowering either the support or the con<sup>fi</sup>dence below the appropriate threshold, setting either the $y _ { r }$ or the $z _ { r }$ to 1 will ensure that rule r will get hidden. Once one of these variables has been set to 1, the value of the other plays no further role in the hiding process and can be set to 0 without loss of generality. w

Proposition 2. If $\begin{array} { r } { ( \sigma _ { h } ^ { r } - 1 ) < \gamma _ { h } ^ { r } ( \sigma _ { r } ^ { a } - \sum _ { i \in \mathcal { D } } b _ { i r } ) } \end{array}$ for sensitive rule $r ,$ the optimal solution will always set $y _ { r }$ to 0.

Proof. Constraint (23) can be written as $\begin{array} { r } { \sum _ { i \in { \mathcal { D } } } a _ { i r } x _ { i } \ge } \end{array}$ $\begin{array} { r } { \gamma _ { h } ^ { r } \sum _ { i \in \mathcal { D } } b _ { i r } x _ { i } - \alpha _ { r } + ( \sigma _ { r } - \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } + \alpha _ { r } ) ( 1 - y _ { r } ) . } \end{array}$ Comparing the right-hand side of this with that of Constraint (22), we can say that if $\begin{array} { r } { ( \sigma _ { r } - \sigma _ { h } ^ { r } + 1 ) > \gamma _ { h } ^ { r } \sum _ { i \in \mathcal { D } } b _ { i r } x _ { i } + ( \sigma _ { r } - \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } ) } \end{array}$ for rule $r ,$ Constraint (23) will always be satis<sup>fi</sup>ed before Constraint (22), and consequently, $y _ { r }$ should be set to 0. The maximum value of $\gamma _ { h } ^ { r } \sum _ { i \in \mathcal { D } } b _ { i r } x _ { i } + \left( \sigma _ { r } - \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } \right) { \mathrm { ~ i s ~ } } \gamma _ { h } ^ { r } \sum _ { i \in \mathcal { D } } b _ { i r } + \left( \sigma _ { r } - \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } \right)$ Therefore, when $\begin{array} { r } { ( \sigma _ { r } - \sigma _ { h } ^ { r } + 1 ) > \ \gamma _ { h } ^ { r } \sum _ { i \in \mathcal { D } } b _ { i r } + ( \sigma _ { r } - \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } ) } \end{array}$ , the optimal solution will have $y _ { r } = 0$ and $z _ { r } = 1$ . Simplifying this inequality gives us the result. w

Proposition 3. ${ \cal I } f \left( \sigma _ { h } ^ { r } - 1 \right) > \gamma _ { h } ^ { r } \sigma _ { r } ^ { a }$ for sensitive rule r, the opti mal solution will always set $y _ { r }$ to 1.

Proof. Using a similar argument as in Proposition $^ { 2 , }$ we can see that if $\begin{array} { r } { ( \sigma _ { r } - \sigma _ { h } ^ { r } + 1 ) < \gamma _ { h } ^ { r } \sum _ { i \in \mathcal { D } } b _ { i r } x _ { i } + ( \sigma _ { r } - \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } ) . } \end{array}$ Constraint (22) will always be satis<sup>fi</sup>ed before Constraint (23), and that y will be set to 1. The minimum value of $\begin{array} { r } { \gamma _ { h } ^ { r } \sum _ { i \in \mathcal { D } } b _ { i r } x _ { i } + \dot { ( } \sigma _ { r } - \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } ) } \end{array}$ is $( \sigma _ { r } - \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } )$ . Therefore, when $\left( \sigma _ { r } - \sigma _ { h } ^ { r } + 1 \right) < \left( \sigma _ { r } - \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } \right)$ , the optimal solution will have $\begin{array} { r l r } { y _ { r } } & { { } = } & { 1 } \end{array}$ . Simplifying the inequality gives us the result. w

Setting $y _ { r } = 0$ implies that Constraint (22) becomes redun dant for rule r. Consequently, this constraint can be eliminated whenever Proposition 2 holds. Similarly, Constraint (23) can be eliminated for each rule that meets the condition in Proposition 3. A straightforward consequence of Propositions $\bar { 2 }$ and 3 is Corollary 1.

Corollary 1. $\begin{array} { r } { I f \sum _ { i \in \mathcal { D } } b _ { i r } = 0 } \end{array}$ for sensitive rule r, the support and confidence constraints for rule r can be represented by the equivalen single constrain $\begin{array} { r } { \sum _ { i \in { \mathcal { D } } } a _ { i r } x _ { i } \ge } \end{array}$ min $\{ ( \sigma _ { r } - \sigma _ { h } ^ { r } + 1 ) , ~ ( \sigma _ { r } - \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } ) \}$

Proof. When $\begin{array} { r } { \sum _ { i \in \mathcal { D } } b _ { i r } = 0 , } \end{array}$ , Constraints (22) and (23) reduce to $\begin{array} { r } { \sum _ { i \in \mathcal { D } } a _ { i r } x _ { i } \geq \overline { { ( \sigma _ { r } - \sigma _ { h } ^ { r } + 1 ) } } y _ { r } \forall r \in \mathcal { R } ^ { S } } \end{array}$ and $\begin{array} { r } { \sum _ { i \in \mathcal { D } } a _ { i r } x _ { i } \ge ~ ( \sigma _ { r } - } \end{array}$ $\gamma _ { h } ^ { r } \sigma _ { r } ^ { a } ) ( 1 - y _ { r } ) \ \forall r \in \mathcal { R } ^ { S }$ , respectively. When $( \sigma _ { h } ^ { r } - 1 ) \neq \ \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } ,$ Propositions 2 and 3 lead to the result directly because Proposition 2 holds when $( \sigma _ { h } ^ { r } - 1 ) > \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } ,$ , and Proposition 3 holds when $( \sigma _ { h } ^ { r } - 1 ) < \gamma _ { h } ^ { r } \sigma _ { r } ^ { a }$ . When $( \stackrel { \cdot \cdot } { \sigma _ { h } ^ { r } } - 1 ) = \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } ,$ , a logic similar to that used in those propositions still applies. In this case, the right-hand sides of the two constraints are equal, and $y _ { r }$ can be set to 0 or 1 without affecting feasibility. w

Proposition 4. ${ \cal I } f \left( \sigma _ { h } ^ { r } - 1 \right) < \gamma _ { h } ^ { r } \sigma _ { r } ^ { a }$ for sensitive rule $r ,$ the support constraint for rule r can be written equivalently as $\begin{array} { r } { \sum _ { i \in \mathcal { D } } a _ { i r } x _ { i } \ge ( \bar { \sigma _ { r } } - \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } ) + ( \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } - \sigma _ { h } ^ { r } + 1 ) y _ { r } \forall r \in \mathcal { R } ^ { \bar { S } } } \end{array}$

Proof. Constraint (23) is equivalent to $\begin{array} { r } { \sum _ { i \in \mathcal { D } } a _ { i r } x _ { i } \ge } \end{array}$ $\begin{array} { r } { \gamma _ { h } ^ { r } \sum _ { i \in \mathcal { D } } b _ { i r } x _ { i } - \alpha _ { r } + ( \sigma _ { r } - \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } + \alpha _ { r } ) ( 1 - y _ { r } ) } \end{array}$ . Rearranging the terms on the right, we have $\begin{array} { r l } { \sum _ { i \in \mathcal { D } } a _ { i r } x _ { i } \ge \gamma _ { h } ^ { r } } & { { } \sum _ { i \in \mathcal { D } } b _ { i r } x _ { i } + } \end{array}$ $( \sigma _ { r } - \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } ) - ( \sigma _ { r } - \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } + \alpha _ { r } ) y _ { r }$ . This constraint is relevant when $y _ { r } = 0 ,$ in which case we have $\begin{array} { r } { \sum _ { i \in \mathcal { D } } a _ { i r } x _ { i } \ge } \end{array}$ $\begin{array} { r } { \mathbf { \Sigma } _ { \gamma } ^ { h r } \sum _ { i \in \mathcal { D } } \dot { b } _ { i r } x _ { i } + ( \sigma _ { r } - \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } ) } \end{array}$ , which implies that $\textstyle \sum _ { i \in { \mathcal { D } } } a _ { i r } x _ { i }$ is at least $( \sigma _ { r } - \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } ) . \mathrm { ~ I f ~ } y _ { r } = 1$ , Constraint (22) implies that $\textstyle \sum _ { i \in { \mathcal { D } } } a _ { i r } x _ { i }$ is at least $( \sigma _ { r } - \sigma _ { h } ^ { r } + 1 )$ . Therefore, irrespective of the actual value of $\begin{array} { r l } { y _ { r } , } & { { } \sum _ { i \in \mathcal { D } } a _ { i r } x _ { i } } \end{array}$ has to be at least min $\{ ( \sigma _ { r } - \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } ) , ~ ( \sigma _ { r } - \sigma _ { h } ^ { r } + 1 ) \}$ . Because we know that $( \sigma _ { h } ^ { r } -$ $1 ) < \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } ,$ we know that min $\{ ( \sigma _ { r } - \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } )$ σ<sub>r</sub> $\sigma _ { h } ^ { r } + 1 ) \} = ( \sigma _ { r } - \gamma _ { h } ^ { r } \sigma _ { r } ^ { a } )$ . Therefore, Constraint (22) can be written as $\begin{array} { r } { \sum _ { i \in \mathcal { D } } a _ { i r } x _ { i } \ge \big ( \sigma _ { r } - \gamma _ { r } ^ { h } \sigma _ { r } ^ { a } \big ) + \big [ \big ( \sigma _ { r } - \sigma _ { h } ^ { r } + 1 \big ) - \big ( \sigma _ { r } - \mathbf { \gamma } } \end{array}$ $\begin{array} { r } { \gamma _ { r } ^ { h } \sigma _ { r } ^ { a } ) ] y _ { r } , \mathrm { o r } \sum _ { i \in D } a _ { i r } x _ { i } \ge ( \sigma _ { r } - \gamma _ { r } ^ { h } \dot { \sigma } _ { r } ^ { a } ) + ( \gamma _ { r } ^ { h } \sigma _ { r } ^ { a } - \sigma _ { h } ^ { \ddot { r } } + 1 ) y _ { r } . } \end{array}$ w

## Appendix B. Hiding Rules When Items Can Be Added and Removed

The notation used in this supplement follows that in the manuscript. We provide them here for ease of reference. The set of items is $\mathcal { T } ,$ with a subset of items from I repre senting a transaction, T . The database to be sanitized, $\mathcal { D } ,$ comprises a set of transactions. The set of sensitive rules is $\mathcal { R } ^ { s } .$ , whereas $\mathcal { R } ^ { S _ { a } }$ represents the set of antecedents of the rules in $\mathcal { R } ^ { s }$

Note that $\sigma _ { r }$ is the support for sensitive rule r in $\mathcal { D } ,$ whereas $\sigma _ { r } ^ { a }$ is the support of its antecedent; $\boldsymbol { \sigma } _ { h } ^ { r }$ is the hiding threshold for support for rule $r ,$ whereas $\gamma _ { h } ^ { r }$ is its hiding threshold for con<sup>fi</sup>dence. We de<sup>fi</sup>ne four new parameters: (i) $m _ { i r } ,$ the number of items from rule r missing from transaction $i , \ ( \mathrm { i i } ) \ p _ { i r } ,$ the number of items from rule $r ,$ already in transaction $i ,$ for r currently not supported by i (therefore, $m _ { i r } + p _ { i r } =$ number of items in r), (iii) $m _ { i r } ^ { a } ,$ , the number of items in ${ \boldsymbol { r } } ^ { a } ,$ the antecedent of rule $r ,$ missing from transaction i, and (iv) $p _ { i r } ^ { a } ,$ , the number of items from the antecedent ${ \boldsymbol { r } } ^ { \alpha } ,$ already in transaction i, for antecedents not supported by r (implying that $m _ { i r } ^ { a } + p _ { i r } ^ { a } =$ the number of items in $r ^ { a } )$

The variables in the problem comprise those de<sup>fi</sup>ned originally and three new sets. The original variables are as follows: $x _ { i }$ is 1 if transaction i is modi<sup>fi</sup>ed and 0 otherwise, y<sub>r</sub> is 1 if sensitive rule r is hidden based on reducing support and 0 otherwise, $z _ { r }$ is 1 if sensitive rule r is hidden based on reducing con<sup>fi</sup>dence and 0 otherwise, $v _ { k i }$ is 1 if item k is removed from transaction i and 0 otherwise, $\omega _ { i r }$ is 1 if rule r loses the support of transaction i and 0 otherwise, and $\omega _ { i r } ^ { a }$ is 1 if the antecedent of rule r loses the support of transaction i and 0 otherwise. The three new variables are as follows: $u _ { k i }$ is 1 if item k is added to transaction i and 0 otherwise, $\rho _ { i r }$ is 1 if rule r gains the support of transaction i and 0 otherwise, and $\rho _ { i r } ^ { a }$ is 1 if antecedent of rule r gains the support of transaction i and 0 otherwise.

Given these de<sup>fi</sup>nitions, the rule hiding problem where both item removal and item addition are allowed can be formulated as in Section B.1.

## B.1. The Formulation

The objective is still to maximize accuracy, so the objective function remains

$$
\min \sum_ {i \in \mathcal {D}} x _ {i}.
$$

The key difference from the formulation where only removals is considered is that the number of relevant $x _ { i }$ variables is now D , whereas earlier, only the transactions that supported sensitive rules were relevant.

If a sensitive rule is hidden based on reducing support, the net of the number of transactions from which the rule loses support and the number of transactions in which the rule gains support has to be at least $\left( \sigma _ { r } - \sigma _ { h } ^ { r } + 1 \right)$ . Therefore,

$$
\sum_ {\{i \in \mathcal {D} | r \subseteq i \}} \omega_ {i r} - \sum_ {\{i \in \mathcal {D} | r \not \subseteq i \}} \rho_ {i r} \geq (\sigma_ {r} - \sigma_ {h} ^ {r} + 1) y _ {r} \quad \forall   r \in \mathcal {R} ^ {S}.\tag{B.1}
$$

If a sensitive rule is hidden based on reducing con<sup>fi</sup>dence, we need to account for the possibility of both the rules and their antecedents gaining support. Therefore,

$$
\left(\frac {\sigma_ {r} - \sum_ {\{i \in \mathcal {D} | r \subseteq i \}} \omega_ {i r} + \sum_ {\{i \in \mathcal {D} | r \not \subseteq i \}} \rho_ {i r}}{\sigma_ {r} ^ {a} - \sum_ {\{i \in \mathcal {D} | r ^ {a} \subseteq i \}} \omega_ {i r} ^ {a} + \sum_ {\{i \in \mathcal {D} | r ^ {a} \not \subseteq i \}} \rho_ {i r} ^ {a}}\right) \leq \gamma_ {h} ^ {r} + (1 - \gamma_ {h} ^ {r}) (1 - z _ {r}) \forall r \in \mathcal {R} ^ {S}.\tag{B.2}
$$

The numerator of the ratio on the left-hand side is the new support of rule $r ,$ whereas the denominator is the new support of its antecedent.

Sensitive rules have to be hidden by lowering either sup port or con<sup>fi</sup>dence, or both. Therefore,

$$
y _ {r} + z _ {r} \geq 1 \quad \forall r \in \mathcal {R} ^ {S}.\tag{B.3}
$$

If an item that is part of a sensitive rule is removed from a transaction that supported that rule, the rule loses the support of that transaction. That is, if $v _ { k i }$ is 1 for any item k from rule r that was supported by transaction i, then $\omega _ { i r }$ has to be 1:

$$
v _ {k i} \leq \omega_ {i r} \quad \forall i \in \mathcal {D}; \quad \forall r \in \{\mathcal {R} ^ {S} | r \subseteq i \}; \quad \forall k \in r.\tag{B.4}
$$

If a sensitive rule loses the support of a transaction, at least one item from that rule must be removed from the transaction. That ${ \mathrm { i } } s ,$ if $\omega _ { i r }$ is set to 1, at least one item k from rule r has to be removed from transaction i:

$$
\sum_ {k \in r} v _ {k i} \geq \omega_ {i r} \quad \forall i \in \mathcal {D}; \quad \forall r \in \{\mathcal {R} ^ {S} \mid r \subseteq i \}.\tag{B.5}
$$

Similar arguments hold for the antecedents of sensitive rules:

$$
v _ {k i} \leq \omega_ {i r} ^ {a} \quad \forall i \in \mathcal {D}; \forall r ^ {a} \in \{\mathcal {R} ^ {S _ {a}} | r ^ {a} \subseteq i \}; \forall k \in r ^ {a},
$$

$$
\sum_ {k \in r ^ {a}} v _ {k i} \geq \omega_ {i r} ^ {a} \quad \forall i \in \mathcal {D}; \forall r ^ {a} \in \{\mathcal {R} ^ {S _ {a}} | r ^ {a} \subseteq i \}.\tag{B.6}
$$

(B.7)

If transaction i gains the support of rule $r ,$ all items in rule r that were missing from transaction i must have been added to it. That is, if $\rho _ { i r }$ is 1, $\boldsymbol { u } _ { k i }$ has to be 1 for all items k that make up part of rule r that were missing from transaction i:

$$
\rho_ {i r} \leq u _ {k i} \quad \forall i \in \mathcal {D}; \quad \forall r \in \{\mathcal {R} ^ {S} \mid r \not \subseteq i \}; \quad \forall k \in \{r \mid k \notin i \}.\tag{B.8}
$$

If $\rho _ { i r }$ is set to 1, all ${ { u } _ { k i } }$ associated with missing items k also have to be set to 1. Conversely, $\rho _ { i r }$ can be set to 1 only if every relevant $u _ { k i }$ has been set to 1.

If transaction i that did not support a sensitive rule r contained some item k from $r , r$ can gain the support of i only if these items are not removed from i. That is, $\rho _ { i r }$ can be 1 only if $( 1 - v _ { k i } )$ is 1 for all such items k:

$$
\rho_ {i r} \leq (1 - v _ {k i}) \forall i \in \mathcal {D}; \forall r \in \{\mathcal {R} ^ {S} | r \not \subseteq i \}; \forall k \in \{r | k \in i \}.\tag{B.9}
$$

Although Constraints (B.8) and (B.9) ensure $\rho _ { i r }$ can be set to 1 only if every item in rule r is in transaction i, they leave open the possibility of $\rho _ { i r }$ being 0 even if all items in r are in i. However, if all missing items from a rule have been added to a transaction and no existing item in that transac tion from that rule has been removed, that rule should be marked as having gained the support of that transaction (i.e., $\rho _ { i r }$ has to be 1). Let $\sum _ { k \in r } u _ { k i }$ be the number of missing items from rule r added to transaction $i ,$ and let $\sum _ { k \in r } v _ { k i }$ be the number of items in rule r that were already present in transaction i that have been removed. A rule r can gain the support of transaction i only if (i) all missing items from a partially supported rule r are added to $\begin{array} { r } { i \ \mathrm { ( i . e . , ~ } \sum _ { k \in r } u _ { k i } = } \end{array}$ $m _ { i r } ) .$ <sup>∈</sup>, and (ii) no items k in r that is already in i are removed (i.e., $\Sigma _ { k \in r } v _ { k i } = 0 )$ . This can happen if

$$
\sum_{\substack{k  \in   r\\ k\notin i}}u_{ki} - \sum_{\substack{k  \in   r\\ k  \in   i}}v_{ki}\leq m_{ir} - 1 + \rho_{ir}\qquad \quad \forall   i\in \mathcal{D};\quad \forall   r\in \{\mathcal{R}^{S}  |  r\not\subseteq i\} .\tag{B.10}
$$

If the left-hand side equals $m _ { i r } ,$ Constraint (B.10) will require $\rho _ { i r }$ to be 1. If it is less than $m _ { i r } ,$ Constraint (B.10) will allow $\rho _ { i r }$ to be 0 or 1. We need it to equal 0 in that case, as rule r would not have gained the support of transaction i. This can be accomplished through Constraint (B.11):

$$
\sum_{\substack{k\in r\\ k\notin i}}u_{ki} - \sum_{\substack{k\in r\\ k\in i}}v_{ki}\geq (m_{ir} + p_{ir})\rho_{ir} - p_{ir} \forall i\in \mathcal{D};  \forall r\in \{\mathcal{R}^{S}|r\notin i\} .\tag{B.11}
$$

The left-hand side of Constraint (B.11) is the same as that of Constraint (B.10). As already noted, when the left-hand side equals $m _ { i r } ,$ Constraint (B.10) will require $\rho _ { i r }$ to be 1, which keeps Constraint (B.11) feasible (because $\sum _ { k \in r } u _ { k i } -$ $\sum _ { k \in \boldsymbol { r } } { v _ { k i } } = m _ { i r } )$ . When the left-hand side is less than $m _ { i r } ,$ Constraint (B.10) allows for $\rho _ { i r }$ to be set to 0 or 1. However, $\rho _ { i r } = 1$ will not be feasible to Constraint (B.11), because $\sum _ { k \in r } u _ { k i } - \sum _ { k \in r } v _ { k i } < m _ { i r }$ . Therefore, $\rho _ { i r }$ will be forced to be 0, making this constraint feasible (because $\sum _ { k \in { r } } u _ { k i } -$ $\begin{array} { r } { \sum _ { k \in r } v _ { k i } = 0 > - p _ { i r } ) } \end{array}$ . Therefore, Constraints (B.10) and (B.11) together ensure that $\rho _ { i r } = 1$ when rule r gains the support of transaction i and $\rho _ { i r } = 0$ when it does not

Similar requirements are needed for the antecedents of sensitive rules. Therefore, we get

$$
\rho_ {i r} ^ {a} \leq u _ {k i} \quad \forall i \in \mathcal {D}; \quad \forall r ^ {a} \in \{\mathcal {R} ^ {S _ {a}} | r ^ {a} \not \subseteq i \}, k \in r ^ {a}, k \notin i,\tag{B.12}
$$

$$
\rho_ {i r} ^ {a} \leq (1 - v _ {k i}) \quad \forall i \in \mathcal {D}; \forall r ^ {a} \in \{\mathcal {R} ^ {S _ {a}} | r ^ {a} \nsubseteq i \}, k \in r ^ {a}, k \in i,\tag{B.13}
$$

$$
\sum_ {\substack {k \in r ^ {a} \\ k \notin i}} u _ {k i} - \sum_ {\substack {k \in r ^ {a} \\ k \in i}} v _ {k i} \leq m _ {i r} ^ {a} - 1 + \rho_ {i r} ^ {a} \quad \forall i \in \mathcal {D}; \quad \forall r ^ {a} \in \left\{\mathcal {R} ^ {S _ {a}} \mid r ^ {a} \nsubseteq i \right\}, \tag{P.14}\tag{B.14}
$$

$$
\sum_{\substack{k\in r^{a}\\ k\notin i}}u_{ki} - \sum_{\substack{k\in r^{a}\\ k\in i}}v_{ki}\geq \big(m_{ir}^{a} + p_{ir}^{a}\big)\rho_{ir}^{a} - p_{ir}^{a}\quad \forall i\in \mathcal{D}; \forall r^{a}\in \{\mathcal{R}^{S_{a}}|r^{a}\not\subset i\} . \tag{P.15}\tag{B.15}
$$

If a sensitive rule r loses the support of transaction i, the transaction has to be marked as altered:

$$
\omega_ {i r} \leq x _ {i} \quad \forall i \in \mathcal {D}; \quad \forall r \in \{\mathcal {R} ^ {S} \mid r \subseteq i \}.\tag{B.16}
$$

This is true if a sensitive rule gains the support of transaction i as well:

$$
\rho_ {i r} \leq x _ {i} \quad \forall i \in \mathcal {D}; \quad \forall r \in \{\mathcal {R} ^ {S} | r \not \subseteq i \}.\tag{B.17}
$$

Similar requirements hold if the antecedents of sensitive rule r loses or gains the support of transaction i:

$$
\omega_ {i r} ^ {a} \leq x _ {i} \quad \forall i \in \mathcal {D}; \quad \forall r ^ {a} \in \{\mathcal {R} ^ {S _ {a}} | r ^ {a} \subseteq i \},\tag{B.18}
$$

$$
\rho_ {i r} ^ {a} \leq x _ {i} \quad \forall i \in \mathcal {D}; \quad \forall r ^ {a} \in \{\mathcal {R} ^ {S _ {a}} | r ^ {a} \not \subseteq i \}.\tag{B.19}
$$

Finally, there are binary requirements on all the variables:

$$
v _ {k i}, u _ {k i}, \omega_ {i r}, \omega_ {i r ^ {a}} ^ {a}, \rho_ {i r}, \rho_ {i r} ^ {a}, x _ {i}, y _ {r}, z _ {r} \in \{0, 1 \}\tag{∀i,r,k.}
$$

(B.20)

This formulation for the 10-transaction database and the 5 sensitive rules used in the illustrative example has 180 variables and 498 constraints (compared with 57 variables and 109 constraints for the formulation where only item removal was considered). BARON (Sahinidis 2014) had considerable dif<sup>fi</sup>culty solving this formulation, concluding incorrectly that the formulation was infeasible.

The only potential bene<sup>fi</sup>t from adding items comes from a potential increase in the denominator of the con<sup>fi</sup>- dence constraints. On the other hand, there are various drawbacks to doing so. From a conceptual point of view, adding items can result in the generation of spurious frequent itemsets; this cannot happen if only item removal is considered. From a practical perspective, the size of the formulation to be solved explodes in terms of the number of variables, number of constraints, and number of nonlinear components. This makes the solution of even the small 10-transaction, 5-rule database impractical for a state-of-the-art solver such as BARON, and it underscores the dif<sup>fi</sup>culty associated with it.

Given these signi<sup>fi</sup>cant conceptual and practical drawbacks, we conclude that adding items to hide sensitive rule is not a desirable practice. This is re<sup>fl</sup>ected in the literature, where many methods involving the removal of items have been proposed, and the very few methods involving item addition have had signi<sup>fi</sup>cant disadvantages, such as the generation of an unacceptable number of spurious rules or not guaranteeing the hiding of sensitive information.

## Endnotes

<sup>1</sup> For expositional convenience, we often refer to the transaction using its unique identifier i.

<sup>2</sup> Typically, when association rules are mined, the number of units of the items sold in each transaction does not play a part. Each item removed when sanitizing a transaction can therefore be “added” into another transaction that involved that item by simply increasing the number of units appropriately. This will ensure that the total numbers of each item sold are conveyed to the supplier correctly.

<sup>3</sup> Given disjoint sets R and B of red and blue elements, respectively, and a family $S \subseteq 2 ^ { R \cup B }$ , the red-blue set covering problem is to find a subfamily $C \subseteq S$ that covers all the blue elements and the fewest number of red elements.

<sup>4</sup> Hereafter, they are referred to as confidence levels of 30%, 50%, 70%, and 90%, respectively.

## References

Acquisto G, Domingo-Ferrer J, Kikiras P, Torra V, de Montjoye Y, Bourka A (2015) Privacy by design in big data: An overview of privacy enhancing technologies in the era of big data analytics. ENISA report, European Union Agency for Cybersecurity, Attiki, Greece.

Adomavicius G, Tuzhilin A (2001) Expert-driven validation of rulebased user models in personalization applications. Data Mining Knowledge Discovery 5(1–2):33–58.

Adomavicius G, Tuzhilin A (2007) Measuring the bullwhip effect: Discrepancy and alignment between information and material <sup>fl</sup>ows. INFORMS J. Comput. 19(2):185–200.

Afshari M, Dehkordi M, Akbari M (2016) Association rule hiding using cuckoo optimization algorithm. Expert Systems Appl. 64: 340–351.

Agrawal R, Srikant R (1994) Fast algorithms for mining association rules in large databases. Bocca J, Jarke M, Zaniolo C, eds. Proc. 20th Internat. Conf. Very Large Data Bases (Morgan Kaufmann, San Francisco), 487–499.

Alaimo D (2013) CGT/RIS retailer/supplier shared data study: A supplement to Consumer Goods Technology and RIS News. Report, RSi Retail Solutions, San Jose, CA.

Askham N (2014) Is data governance the same as data quality? Experian (blog), August, https://www.experian.co.uk/blogs/ latest-thinking/data-and-innovation/is-data-governance-thesame-as-data-quality/.

Askuity (2018) 2018 POS data study. https://www.askuity.com/wpcontent/uploads/2018/01/2018-POS-Data-Study.pdf.

Atallah M, Bertino E, Elmagarmid A, Ibrahim M, Verykios V 1999) Disclosure limitation of sensitive rules. Scheuermann P, ed. Proc. 1999 Workshop Knowledge Data Engrg. Exchange (IEEE Computer Society, Los Alamitos, CA), 45–52.

Aviv Y (2002) Gaining bene<sup>fi</sup>ts from joint forecasting and replenishment processes: The case of auto-correlated demand. Manufacturing Service Oper. Management 4(1):55–74.

Aviv Y (2007) On the bene<sup>fi</sup>ts of collaborative forecasting partnerships between retailers and manufacturers. Management Sci. 53(5):777–794.

Baesens B (2018) Improving data quality using data governance. Big Data Quart. 4(1):43–44.

Beduhn P (2009) Elephants in your haystack: Manufacturers take their <sup>fi</sup>rst crack at mining point-of-sale data. Teradata Magazine 9(2).

Carr R, Doddi S, Konjevod G, Marathe M (2000) On the red-blue set cover problem. Randall D, ed. Proc. 11th Annual ACM-SIAM Sympos. Discrete Algorithms (ACM, New York), 345–353.

Chen F, Drezner Z, Ryan J, Simchi-Levi D (2000) Privacy and big data: Scalable approaches to sanitize large transactional databases for sharing. Management Sci. 46(3):436–443.

Cheng P, Lin C-W, Pan J-S (2015) Use HypE to hide association rules by adding items. PLoS One 10(6):e0127834.

Cheng P, Roddick JF, Chu S-C, Lin C-W (2016) Privacy preservation through a greedy, distortion-based rule-hiding method. Appl. Intelligence 44(2):295–306.

Croson R, Donohue K (2003) Impact of POS data sharing on supply chain management: An experimental study. Production Oper. Management 12(1):1–11

Czyzyk J, Mesnier M, More J (1998) The NEOS server. ´ IEEE J. Com putational Sci. Engrg. 5(3):68–75.

Dasseni E, Verykios V, Elmagarmid A, Bertino E (2001) Hiding association rules by using con<sup>fi</sup>dence and support. Moskowitz IS, ed. Inform. Hiding: Proc. 4th Internat. Inform. Hiding Work shop, Pittsburgh, PA (Springer, Berlin), 382–396.

DeLallo D, Tennison J (2020) How to make the most of AI? Open up and share data. McKinsey on AI podcast (June 9), 18:19, https://www.mckinsey.com/business-functions/mckinseyanalytics/our-insights/how-to-make-the-most-of-ai-openup-and-share-data.

Dolan E (2001) The NEOS Server 4.0 administrative guide. Technical Report ANL/MCS-TM-250, Mathematics and Computer Science Division, Argonne National Laboratory, Argonne, IL.

du Mars R (2012) Data quality process needs all hands on deck. TechTarget (June 12), https://searchdatamanagement.techtarget com/feature/Data-quality-process-needs-all-hands-on-deck

Gar<sup>fi</sup>nkel R, Gopal R, Goes P (2002) Privacy protection of binary con<sup>fi</sup>dential data against deterministic, stochastic, and insider threat. Management Sci. 48(6):749–764.

Gkoulalas-Divanis A, Verykios V (2006) An integer programming approach for frequent itemset hiding. Proc. 15th ACM Internat. Conf. Inform. Knowledge Management (ACM, New York), 748–757.

Gopalan N, Murthy T (2019) Association rule hiding using chemical reaction optimization. Bansal J, Das K, Nagar A, Deep K, Ojh A, eds. Soft Computing for Problem Solving (Springer Singapore, Singapore), 249–255.

Gropp W, More J (1997) Optimization environments and the NEOS´ server. Buhmann M, Iserles A, eds. Approximation Theory and Optimization: Tributes to M. J. D. Powell (Cambridge University Press, Cambridge, UK), 167–182.

Guillet F, Hamilton R (2007) Quality Measures in Data Mining. Studies in Computational Intelligence, Vol. 43 (Springer-Verlag, Berlin).

Hankinson S (2016) The tipping point: Financial services and data governance. Collibra (blog), September 30, https://www. collibra.com/blog/the-tipping-point-<sup>fi</sup>nancial-services-and-datagovernance.

Hao J, Menon S, Sarkar S (2007) Preserving privacy when sharing distributed transactional data. 17th Annual Workshop Inform. Tech. Sustems. Montreal. Canada

IBM (2018) IBM ILOG CPLEX 12.8 User’s Manual (IBM Corporation, Armonk, NY).

Ivanov K (1972) Quality-control of information: On the concept of accuracy of information in data banks and in management information systems. PhD thesis, University of Stockholm/Royal Institute of Technology, Stockholm.

Klemettinen M, Mannila H, Ronkainen P, Toivonen H, Verkamo A (1994) Finding interesting rules from large sets of discovered association rules. Adam NR, Bhargava BK, Yesha Y, eds. Proc. Third Internat. Conf. Inform. Knowledge Management(ACM, New York), 401–407.

Konzak L (2012) Sharing point-of-sale data: Challenges and opportunities. MDM special report, Modern Distribution Management, Niwot, CO

Kroger (2017) 2016 Kroger Fact Book (Kroger Company, Cincinnati). Kroger (2018) 2017 Kroger Fact Book (Kroger Company, Cincinnati).

Ladley J (2012) Data Governance: How to Design, Deploy, and Sustain an Effective Data Governance Program (Morgan Kaufmann, Wal tham, MA).

Lee H, So K, Tang C (2000) The value of information sharing in a two-level supply chain. Management Sci. 46(5):626–642.

Lin J, Liu Q, Fournier-Viger P, Hong T, Voznak M, Zhan J (2016) A sanitization approach for hiding sensitive itemsets based on particle swarm optimization. Engrg. Appl. Artificial Intelligence 53(August):1–18.

Menon S, Sarkar S (2007) Minimizing information loss and preserving privacy. Management Sci. 53(1):101–116.

Menon S, Sarkar S (2016) Privacy and big data: Scalable approaches to sanitize large transactional databases for sharing. MIS Quart. 40(4):963–981.

Menon S, Sarkar S, Mukherjee S (2005) Maximizing accuracy of shared databases when concealing sensitive patterns. Inform. Systems Res. 16(3):256–270.

Munves G (2013) Wake up, retailers! Make money from your big data. Chain Store Age (April 3), https://chainstoreage.com news/wake-retailers-make-money-your-big-data/.

Navale G, Mali S (2019) Lossless and robust privacy preservation of association rules in data sanitization. Cluster Comput. 22(S1): 1415–1428.

Nayar A (2019) Top 3 insights that suppliers gain from downstream data. Manthan (blog). https://www.manthan.com/blogs/vl-top-3- insights-that-suppliers-gain-from-downstream-data/.

Nunez M, Gar<sup>fi</sup>nkel R, Gopal R (2007) Stochastic protection of con<sup>fi</sup>- dential information in databases: A hybrid of data perturbation and query restriction. Oper. Res. 55(5):890–908.

Oliveira S, Zaïane O (2002) Privacy preserving frequent itemset mining. Clifton C, Estivill-Castro V, eds. Proc. IEEE ICDM Workshop Privacy, Security Data Mining (Australian Computer Society, Darlinghurst, NSW, Australia), 43–54.

Olson J (2003) Data Quality: The Accuracy Dimension (Morgan Kauf mann, San Francisco).

Padmanabhan B, Tuzhilin A (2006) On characterization and discovery of minimal unexpected patterns in rule discovery. IEEE Trans. Knowledge Data Engrg. 18(2):202–216.

Power D (2002) What is the “true story” about data mining, beer and diapers? DSS News 3(23). http://www.dssresources.com/ newsletters/66.php.

Reddy M, Wang R (1995) Estimating data accuracy in a federated database environment. Bhalla S, ed. Proc. Sixth Internat. Conf. In form. Systems Management Data (Springer, Berlin), 115–134.

Redman T (2016) Bad data costs the U.S. \$3 trillion per year. Harvard Bus. Rev. (September 22), https://hbr.org/2016/09/bad-datacosts-the-u-s-3-trillion-per-year.

Redman R (2020) Kroger gives CPG advertisers more sales visibility. Su permarket News (February 14), https://www.supermarketnews.com/ marketing/kroger-gives-cpg-advertisers-more-sales-visibility.

Retail Touchpoints (2017) Winning with data sharing: Driving new analytical and revenue opportunities. White paper, Retail Touchpoints, Hasbrouck Heights, NJ.

Retail Velocity (2019) Retailer POS data sources. Accessed October 3, 2021, https://www.retailvelocity.com/downstream-pos-dataretail-sales-analysis-sources.

Sahar S (1999) Interestingness via what is not interesting. Proc. Fifth ACM SIGKDD Internat. Conf. Knowledge Discovery Data Minin (ACM, New York), 332–336.

Sahinidis NV (2014) BARON 14.3.1: Global Optimization of Mixed Integer Nonlinear Programs (User’s Manual).

Silberschatz A, Tuzhilin A (1995) On subjective measures of interestingness in knowledge discovery. Fayyad UM, Uthurusamy R, eds. Proc. First Internat. Conf. Knowledge Discovery Data Minin (AAAI Press, Palo Alto, CA), 275–281.

Stavropoulos E, Verykios V, Kagklis V (2016) A transversal hypergraph approach for the frequent itemset hiding problem. Knowledge Inform. Systems 47(3):625–645.

Talebi B, Dehkordi M (2018) Sensitive association rules hiding using electromagnetic <sup>fi</sup>eld optimization algorithm. Expert Systems Appl. 114:155–172.

Telikani A, Shahbahrami A (2017) Optimizing association rule hid ing using combination of border and heuristic approaches. Appl. Intelligence 47(2):544–557.

Telikani A, Shahbahrami A (2018) Data sanitization in association rule mining: An analytical review. Expert Systems Appl. 96:406–426.

Telikani A, Gandomi A, Shahbahrami A, Dehkordi M (2020) Privacypreserving in association rule mining using an improved discrete binary arti<sup>fi</sup>cial bee colony. Expert Systems Appl. 144:113097.

Terry L (2015) CGT/RIS retailer/supplier shared data study: A supplement to Consumer Goods Technology and RIS News. Report, RSi Retail Solutions, San Jose, CA.

Verykios V, Elmagarmid A, Bertino E, Saygin Y, Dasseni E (2004) Association rule hiding. IEEE Trans. Knowledge Data Engrg. 16(4):434–447.

Wang R, Strong D (1996) Beyond accuracy: What data quality means to data consumers. J. Management Inform. Systems 12(4):5–33.

Weinbaum A (2017) 9 strategies that will encourage distributors to submit channel POS data. Report, Computer Market Research, San Diego.

Weinswig D (2020) Measuring the value of retail data sharing and analytics. Coresight Research/SPS commerce research report, Coresight Research, New York.

Wu Y, Chiang C, Chen A (2007) Hiding sensitive association rules with limited side effects. IEEE Trans. Knowledge Data Engrg. 19(1):29–41.

Zhang L, Wang W, Zhang Y (2019) Privacy preserving association rule mining: Taxonomy, techniques, and metrics. IEEE Access 7: 45032-45047

C<sub>opy</sub>ri<sub>g</sub>ht 2022 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
