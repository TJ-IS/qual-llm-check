---
otero_id: 1094
otero_key: "ERKASX7A"
title: "Determining Optimal CRM Implementation Strategies"
authors: "Seung Hyun Kim; Tridas Mukhopadhyay"
year: "2011"
journal: "Information Systems Research"
doi: "10.1287/isre.1100.0309"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/ERKASX7A/fulltext/images/da76576cfce9543521cd2a4896eb6dff1173e534bedb4518053bc5283e3e2a98.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Determining Optimal CRM Implementation Strategies

Seung Hyun Kim, Tridas Mukhopadhyay,

## To cite this article:

Seung Hyun Kim, Tridas Mukhopadhyay, (2011) Determining Optimal CRM Implementation Strategies. Information Systems Research 22(3):624-639. http://dx.doi.org/10.1287/isre.1100.0309

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2011, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/ERKASX7A/fulltext/images/5c7125746c124474f1372a5c570231c3e5f645a6ff7a72555c0e7626cec287d0.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Determining Optimal CRM Implementation Strategies

Seung Hyun Kim

Department of Information Systems, National University of Singapore, Singapore 117417, kimsh@comp.nus.edu.sg

Tridas Mukhopadhyay

Tepper School of Business, Carnegie Mellon University, Pittsburgh, Pennsylvania 15213, tridas@cmu.edu

lthough companies have spent a great deal of money to adopt CRM (customer relationship management) technologies, many have not seen satisfactory returns on their CRM implementations. We study optimal CRM implementation strategies and the impact of CRM investments on profitability. For our analysis, we classify CRM technologies into two broad categories: targeting-related and support-related technologies. While targeting CRM improves the success rate of distinguishing between nonloyal and loyal customers, support CRM increases the probability of retaining the loyalty of existing customers. We also consider the costs of implementing each CRM type separately as well as both types simultaneously. We show that the optimal CRM implementation strategy depends on the initial mass of loyal customers and diseconomies of scale in simultaneous implementation. We also find that the two types of CRM technologies are substitutive rather than complementary in generating revenue. We discuss why it is difficult to avoid overinvestments in CRM when the nature of the investments is misunderstood. We study the optimal CRM implementation scope and the impact of different types of CRM on customers. We develop a model that not only considers both the revenue and costs sides but is also helpful in determining the deployment of right CRM technology in the right scope.

Key words: customer relationship management; IT investments; CRM costs; consumer surplus; complementarity; substitutability; economics of IS

History: Seungjin Whang, Senior Editor; Gautam Ray, Associate Editor. This paper was received on November 15, 2007, and was with the authors 15 <sup>1</sup> months for 2 revisions. Published online in Articles in Advance November 18, 2010.

## 1. Introduction

Despite the fast growth of the CRM market<sup>1</sup> and a great deal of money spent by companies (typically \$5,000 per user and \$2 million to \$5 million per deployment), many have not seen a satisfactory return on their CRM installations (Fox 2001, Hendricks et al. 2007).<sup>2</sup> Evidence also shows that many CRM features are never used after implementation (Lacey 2002). We attribute one of the reasons for such dissatisfaction to the lack of understanding of the impact of CRM technologies, which are very different from traditional cost-cutting and quality enhancing IT. Due to the popularity of CRM and marketing efforts of CRM software vendors, firms are likely to choose inappropriate CRM technologies and may overinvest in CRM technologies. Firms could end up with low ROI (return on investment) unless a full consideration of their environments and customers is given.

We study optimal CRM implementation strategies and the impact of CRM investments on firm profitability. This study differs from the prior literature in three aspects. First, we address the new role of information technologies by analyzing the impact of customer-oriented technologies. Second, we attempt to capture the multifaceted effects of CRM technologies and how these effects might interact in generating revenues. CRM software usually consists of various modules such as marketing automation, call-center, analytical, self-service, and salesforce automation modules with distinct functionalities. Based on the literature and our interviews with CRM experts and consultants, we classify CRM software modules into two broad categories, targeting-related and support-related modules, to analyze optimal CRM implementation strategies. This taxonomy is important and useful in studying CRM implementation strategies because implementing each category of CRM technology requires different sets of knowledge and resources. Additionally, each type has a distinct impact on firm profits. Targeting-related CRM modules are associated with direct profit generation due to increased knowledge of customers, and include marketing automation, analytics, and business intelligence modules. Support-related CRM modules are associated with relationship-building with customers by providing enhanced service, and they include call-center, e-business, field service, and selfservice modules. This taxonomy is similar to the industry view of CRM technologies as “back-office CRM” versus “front-office CRM” (Dyche 2001) or “analytical CRM” versus “operational CRM” (Laudon and Laudon 2005). Third, we explicitly model the costs of implementing each CRM type separately as well as both types simultaneously. We then turn our attention to the implementation side of CRM based on our taxonomy. Should a firm concentrate on one type of CRM or implement both? If both types are implemented, should they be installed simultaneously or not?

Our main results can be summarized as follows.

• The conventional wisdom in the IS (information systems) literature has been that computer assets are likely to be complementary (e.g., Tanriverdi 2006). However, we find that different types of CRM investments can be substitutive from the revenue point of view. This substitution effect strengthens the possibility that a firm can specialize in one category of CRM technology rather than choosing to be an all-around player by investing in diverse CRM technologies. A lack of knowledge of the substitutive effect leads to overinvestment (Siggelkow 2002) in CRM technologies, which might explain why firms do not receive as much benefit as they expect. Even the potential integration benefit of the two types of CRM systems does not ensure that they are complementary. In addition, we show that a lack of understanding of the effects of such factors as the size of initial loyal customers and change in the customer base (i.e., entry and exit of customers) on the optimal implementation strategy would lead to suboptimal CRM implementation decisions.

• The simultaneous implementation of both types of CRM technologies is likely to be optimal when the diseconomies of scale in implementing two types of CRM technologies are low, such that implementing one type of CRM technology only moderately increases or even decreases the marginal cost of implementing the other type of CRM technology. With greater levels of diseconomies of scale, where implementing one type of CRM technology substantially increases the marginal cost of implementing the other type of CRM technology, a firm endowed with a high portion of loyal customers should specialize in support-related modules rather than in targetingrelated modules.

• More investments in both targeting and supportrelated CRM technologies might decrease consumer surplus. That is, a firm can extract more surplus from customers not only from its investments in enhanced capability to discriminate between loyal and nonloyal customers but also through investments in customersupport technologies to enhance customer loyalty. The marketing literature has emphasized the welfaredecreasing impact of certain technologies (Tyagi 2004, Chen et al. 2001). However, at times, with an increase in diseconomies of scale in simultaneous implementation of both types of CRM systems, the optimal scope of each type might reduce, resulting in higher consumer surplus.

The managerial implication of this paper is that the economic impact of different types of CRM technologies should be understood in order to decide a firm’s optimal implementation scope and strategies. Managers should consider market conditions as well as the challenges of implementing different types of CRM simultaneously. Their decisions should not be biased by a vendor’s discount on bundled purchase of multiple CRM products. Our analytical model can isolate the main effects of different types of CRM technologies from other hard-to-measure factors and focus on why even good systems might not meet managers’ expectations.

This paper is organized as follows. Section 2 presents a review of prior literature. Section 3 outlines our research model. Section 4 presents our principal analytical results on the optimal CRM implementation strategy. Section 5 analyzes the strategic implications of two types of CRM technologies. Section 6 discusses producer and consumer surplus. Section 7 extends the model setting to check for the robustness of our results. Section 8 concludes the paper.

## 2. Related Literature

This paper is related to both IS and marketing literatures. Although the concept of CRM and “relationship marketing” emerged in marketing, the technological aspect of CRM has not received much attention in marketing. The CRM focus in the marketing literature has been on how to optimize the marketing mix variables to enhance relationship and customers’ lifetime value (e.g., Rust and Verhoef 2005, Rust and Chung 2006). In contrast with the rich literature of

CRM that studies how to optimize marketing activities, relatively less effort has been spent to study the role and impact of CRM technologies. Several studies (Chen et al. 2001, Chen and Iyer 2002, Villas-Boas 2004) have addressed the issue of investing in customer-oriented capabilities such as targetability, addressability, and customer recognition capability. More recently, studies like Jayachandran et al. (2005), Srinivasan and Moorman (2005), and Mithas et al. (2005) have reported the positive outcomes of CRM investments. However, the implementation of CRM technology has not been the main focus in these studies. This tendency is partly due to a “holistic” view of CRM beyond technology implementation (Payne and Frow 2005). Although CRM can be implemented without sophisticated technology (Rigby et al. 2002), technology is still essential for successful CRM deployment at any firm of significant size.

The IS literature has a well-established tradition of research on the impact of IT investments. For instance, Barua et al. (1991), Thatcher and Pingry (2004), and Demirhan et al. (2006) have used analytical models to examine the impact of IT investments that lead to improved quality or reduced variable cost. Firm-level empirical studies (Brynjolfsson 1996, Brynjolfsson and Hitt 1996) have showed that IT investments increase firm productivity and consumer surplus. Similarly, studies of specific technologies (e.g., Kekre and Mukhopadhyay 1992, Mukhopadhyay and Kekre 2002, Mukhopadhyay et al. 1995, Riggins and Mukhopadhyay 1994, Srinivasan et al. 1994) and research at the process level (e.g., Ashworth et al. 2004; Barua et al. 1995; Davamanirajan et al. 2006; Mukhopadhyay and Mangal 1997; Mukhopadhyay et al. 1997a, b) have quantified IT value at a finer level. Two new trends have surfaced in this literature. First, research is moving from measuring the value of IT impact to why IT investments lead to different organizational outcomes (e.g., Devaraj and Kohli 2003, Melville 2004). Second, many recent studies focus on enterprise applications such as ERP, CRM, and SCM (Cotteleer and Bendoloy 2006, Gattiker and Goodhue 2005, Hitt et al. 2002, Ranganathan and Brown 2006, Mithas et al. 2005, Hendricks et al. 2007) that require much more expenditure of organizational resources.

In this paper, we follow the recent trends and study why CRM investments might not deliver the expected outcomes. We focus on CRM implementation strategies, which have received scant attention in the marketing literature. To our best knowledge, our paper is the first attempt to examine CRM implementation strategies and scopes by considering different types of CRM systems.

## 3. Model

## CRM Classification from an IT Perspective

To analyze the effects of different CRM technologies, we classify diverse CRM modules available from commercial software vendors into two broad categories based on the common classification in the literature and among practitioners: targeting-related and support-related CRM modules (Dyche 2001, Laudon and Laudon 2005). This taxonomy is critical when considering CRM implementation because implementing each category of CRM software technologies not only requires different sets of knowledge and resources but also has distinct impact on a firm’s profit and its customers. As support-related CRM involves close interactions with customers, it directly influence customers’ perception of service quality and loyalty if successful. User training for support-related CRM should differ from that for targeting-related CRM because interactions and communication with customers are part of customer support processes. On the other hand, targeting-related CRM is based more on data warehouses, data mining, online analytical processing (OLAP), and other data analysis tools. For these reasons, firms often choose to implement one type of CRM modules first and move to implementing the other type of CRM modules later.

We define targeting-related CRM modules as software components that involve analyzing customers’ preferences and purchasing behaviors without faceto-face interactions with customers. This type of CRM technology is often called “analytical,” “strategic,” or “back-office” CRM. Although they might be sold by different names by different CRM vendors, common examples of targeting-related CRM modules include marketing automation modules, analytical modules, and business intelligence modules. The expected benefit of implementing such modules is the enhanced ability to analyze customers’ preference and to better target those customers for future marketing activities. For example, companies such as Amazon, Harrah’s, Capital One, and the Boston Red Sox have taken dominant positions in their industries by leveraging the power of analytical tools across various customer management activities (Davenport 2006). As we will see shortly, we model this benefit as increased accuracy in classifying customers as either loyal or nonloyal customers.

We define support-related CRM modules as software components that involve direct interactions with customers to provide customized service, which is often called “front-office” or “operational” CRM. Examples of support-related CRM modules include call-center, e-business, salesforce automation, and field service modules. These modules enable a firm to streamline communications from and to customers. Because implementing support-related modules should consider direct interactions with customers, systems development and employee training should be done in a way to meet individual customers’ expectations and maximize customer value (Xu et al. 2002). The expected benefit of implementing these modules is the enhanced ability to support customers and deliver higher customer satisfaction. We will model this benefit as an increased probability of customers to stay or become loyal after their purchases. Table 1 summarizes our taxonomy of CRM modules.<sup>3</sup>

Table 1 Categorization of CRM Modules

<table><tr><td>Category</td><td>Examples</td><td>Expected benefit</td><td>Modeling</td></tr><tr><td>Targeting-related CRM modules</td><td>MarketingAnalytical modulesBusiness intelligence</td><td>Enhanced targeting accuracy</td><td>Accurate classification of customers</td></tr><tr><td>Support-related CRM modules</td><td>Call-centerSalesforceField serviceOrder management</td><td>Enhanced customer support quality</td><td>Higher probability of being loyal</td></tr></table>

## Revenue from CRM Implementation

Let us begin with a preview of our model. Each period, a firm faces two types of customers: loyal (L) and nonloyal (NL) customers. Loyal customers are less sensitive to price and are willing to purchase a product without any price promotion (Chen et al. 2001, Rigby and Ledingham 2004, Varian 1980). Nonloyal customers are sensitive to price and are willing to hold off purchase until they are offered a price promotion. To keep our exposition simple, we use the term “loyal” and “price-insensitive” (“nonloyal” and “price-sensitive”) interchangeably. Customer loyalty might change with time; a loyal customer might become nonloyal and vice versa. The firm provides support to its existing customers to induce loyalty without complete success. It has imperfect knowledge of the identity of loyal and nonloyal customers. With a base level of targeting capability without sophisticated targeting-related CRM modules, it makes offers only to those who are deemed to be nonloyal customers. In effect, it succeeds in targeting a fraction of nonloyal customers. At the end of each period, a fraction of customers exits the market.

The firm enters the next period when it decides what types of CRM technologies should be implemented and to what extent, before making the next round of promotional offers. Upon CRM implementation, its enhanced support-CRM (assuming it implemented more support capabilities in this period)

begins to affect loyalty of existing customers, who were either loyal or nonloyal in the previous period, such that more existing customers remain loyal or more nonloyal customers switch to being loyal customers. Some nonloyal customers, who did not receive an offer and did not make a purchase in the previous period, might also join the loyal segment in this period. For example, their circumstances might have changed over time such that their heightened need for the product (and/or higher income and affluence) induces them to buy it without an offer. At the beginning of each period, a new set of fresh customers enters the market. The firm does not have perfect knowledge of who left or who entered the market. Some new customers may also be willing to purchase the product without a promotional offer (loyal) while others would not buy without a special deal (nonloyal). Before the end of this period, the firm attempts to make promotional offers again to those deemed as nonloyal customers. We do not make any assumption about the exact timing of the promotion during the purchasing cycle; indeed, the targeting CRM could dictate the timing.<sup>4</sup> The new targeting accuracy is improved (but still remains imperfect) with the implementation of sophisticated targeting-related CRM modules (assuming it implemented more targeting capabilities in this period).

In summary, at any period the firm knows who bought the product in the prior period. Some paid the full price and were loyal customers, others paid the discounted price; some of those who paid the discounted price might have been loyal but were mistakenly offered a discount due to imperfect targeting accuracy. The firm does not know with certainty (i) who among its customers from the previous period remained in (or left) the market, (ii) who are the new customers, and (iii) who is price-sensitive (nonloyal) among these two types of customers. Strictly speaking, they should be called prospective customers. To keep our exposition simple, we do not use the more precise term “prospective customers” for these groups.

Now we explain the model in details. Each customer purchases at most one unit of a product or service every period from a single product monopolist (Villas-Boas 2004). The price of the product is $p ,$ which is exogenously given. Let d denote a promotional discount and c be the cost to reach one individual customer; c includes the variable cost incurred in mailing, calling, and associated labor. This setting is congruent with common managerial practices of offering discounts to vulnerable customers (Rigby and Ledingham 2004). Considering the cost of contacting a loyal customer and the risk of offering a promotion, the firm’s objective is to contact only nonloyal customers and offer them a price promotion. For notational simplicity, we use $c ^ { \prime } = c + d$ as the cost to acquire one customer, classified as nonloyal, because c and d do not need to be distinguished from a firm’s point of view. The two parameters will become relevant when we analyze the CRM impact on consumers.

Let S denote the level of support-related CRM modules.<sup>5</sup> We assume that customers who purchased in the previous period can be either loyal or nonloyal in the current period and the probability of existing customers staying loyal is a function of a firm’s support modules, which is f 4S5. Let $f _ { 0 }$ denote the base level of customer support without support-related CRM modules such that $f _ { 0 } < f ( S ) . ^ { 6 }$ In fact, several researchers have found a link between CRM technology, customer satisfaction, and retention (Jayachandran et al. 2005, Mithas et al. 2005, Mittal and Kamakura 2001, Srinivasan and Moorman 2005). As explained earlier, a customer who was nonloyal in the prior period but was not targeted (and did not purchase) might join the loyal segment in this period with probability . This reflects that some customers price sensitivity might change independent of the firm’s interventions. With $0 < \bar { \tau } < f _ { 0 } < \bar { f } ( S )$ , we ensure that a customer’s chance of switching from the nonloyal to the loyal segment is lower than the probability of existing customers remaining loyal due to customer support. We assume $f _ { S } > 0$ and $\dot { f } _ { S S } < 0 , 7$ so that the probability level increases with support modules implemented but at a decreasing rate to reflect diminishing marginal returns.<sup>8</sup>

We set the initial market size to 1 and denote the initial size of the loyal segment in period 0 by $l _ { 0 } .$ The size of the loyal segment in the nth period is denoted as $l _ { n } .$ We assume that a fraction $1 - \rho$ of existing customers exits the market at the end of each period, while a group of new customers w enters the market at the beginning of each period. That is, the market size in the nth period is $\begin{array} { r } { { M _ { n } = \rho ^ { n } + w \sum _ { i = 1 } ^ { n } \rho ^ { i - 1 } } , } \end{array}$ where $n \geq 1$ (cf. Beggs and Klemperer 1992). As stated earlier, a fraction of the new customer segment is insensitive to price. We assume that of the w new customers who enter the market at each period,  · w of them will be loyal while 41−5·w will be nonloyal. That is, the probability of a new customer being priceinsensitive equals the probability that a previously nonloyal customer becomes price-insensitive in this period. This assumption keeps our model tractable and parsimonious.

The new CRM support level begins to affect the loyalty of existing customers (who bought in the last period) at the start of this period. Before the end of this period, the firm attempts to classify customers between loyal and nonloyal segments, which is congruent with the role of targeting and discrimination accuracy in the literature (Chen et al. 2001, Rigby and Ledingham 2004). Let T denote the level of targeting-related CRM modules. Now define $\operatorname* { P r } ( i \mid j )$ as the probability that a firm classifies the customer from a segment j into the segment i, where $i , j \in$ 8L1 NL9. We adopt the unbiasness assumption from Chen et al. (2001): the estimated sizes of the two segments are equal to the corresponding sizes of the actual market. That $\mathrm { i s } , \ l _ { n } \ \cdot \ \mathrm { P r } ( L \ | \ L ) ^ { - } + ( M _ { n } \ - \ l _ { n } ) \ .$ $\Pr ( L \ | \ N L ) = l _ { n }$ and $l _ { n } \cdot P \mathbf { r } ( N L \mid L ) + ( M _ { n } - l _ { n } )$ $\operatorname* { P r } ( N L \mid N L ) = M _ { n } - l _ { n }$ . Although a firm has imperfect targeting capability, it can estimate how precise its targeting capability is by analyzing past data and/or by testing with a small subset of customers to find out how many of its customers can be classified as loyal. Thus firms can obtain overall estimates of customer segments (loyal versus nonloyal), while the same property (loyalty) of individual customers might not always be known accurately. For example, Peppers et al. (1999) show how companies can combine internal customer data and external market research data to first identify and classify customers before embarking on targeting specific customers. Similarly, Rigby et al. (2002) develop a customer strategy that divides customers into multiple segments before investing in CRM loyalty programs. As probability Pr4L $\mid N L \bar { } ) +$ $\mathrm { P r } ( N L \mid \dot { N } L ) \dot { = 1 }$ and $\operatorname* { P r } ( L \mid L ) \hat { + } \operatorname* { P r } ( N L \mid L ) = 1$ are satisfied. The revenue function can now be derived as in Lemma 1.

<sup>Lemma</sup> <sup>1.</sup> Suppose a firm provides a selective promotional offer only to the segment of customers believed to be nonloyal, to avoid the cost of contacting an individual customer and the risk of offering a promotion to a loyal customer; its revenue in period n becomes $R _ { n } = l _ { n } p + ( { \dot { M } } _ { n } - l _ { n } )$ $\{ { \mathrm { P r } } ( N L \mid N L ) p - c ^ { \prime } \} . ^ { \dot { 9 } }$

Because the revenue function depends only on Pr4NL  NL5, we define Pr4NL  NL5, the targeting accuracy of the firm as a function of the targeting modules implemented. Let $g ( T ) = \operatorname* { P r } ( N L | N L )$ . We assume $g _ { T } > 0$ and $g _ { T T } < 0$ so that a firm’s targeting accuracy increases with the scope of targeting modules implemented at a decreasing rate to reflect diminishing marginal returns. Let $g _ { 0 }$ denote the base level of targeting capability without targeting-related CRM modules such that $g _ { 0 } < g ( T )$ . Note in Lemma 1 that the profit from new customers w increases in its targeting capability by attracting more new customers.

Note that our model could extended to n periods, and the sizes of both segments can be modeled as a Markov process.<sup>10</sup> We define the transition matrix of a customer state as

$$
\begin{array}{r l} \text { Period   } n - 1 & M = \underset {\text { Nonloyal }} {\text { Loyal }} \left[ \begin{array}{c c} f (S _ {n}) & 1 - f (S _ {n}) \\ g (T _ {n - 1}) f (S _ {n}) & 1 - g (T _ {n - 1}) f (S _ {n}) \\ + \{1 - g (T _ {n - 1}) \} \tau & - \{1 - g (T _ {n - 1}) \} \tau \end{array} \right] \\ & = \left[ \begin{array}{c c} m _ {1 1} & m _ {1 2} \\ m _ {2 1} & m _ {2 2} \end{array} \right], \end{array}
$$

where $S _ { n }$ and $T _ { n - 1 }$ denote the level of support CRM modules in period n and the level of targeting CRM modules in period $n - 1 ,$ , respectively. From the matrix above, by $m _ { 2 1 } ,$ a nonloyal customer at the beginning of period $n - 1$ would have been classified correctly as a nonloyal customer and offered a promotion with probability $g ( T _ { n - 1 } )$ . These customers are qualified as existing customers in period n and then provided support services to induce loyalty, with the probability $f ( S _ { n } )$ . As explained above, a nonloyal customer might not receive an offer in period $n - 1$ with probability of $\{ 1 - g ( T _ { n - 1 } ) \}$ but might be willing to buy the product in period n without a discount with probability of $\tau .$ Thus, if the size of the loyal segment in period $n - 1$ was $l _ { n - 1 }$ , the size of loyal segment in the next period is

$$
\begin{array}{r} l _ {n} = \rho \cdot l _ {n - 1} f (S _ {n}) + \rho \cdot (M _ {n - 1} - l _ {n - 1}) g (T _ {n - 1}) f (S _ {n}) \\ + \rho \cdot (M _ {n - 1} - l _ {n - 1}) \{1 - g (T _ {n - 1}) \} \cdot \tau + w \tau , \end{array}
$$

where $M _ { n - 1 }$ was the size of the market in beginning of period $n - 1$ . Figures 1 and 2 illustrate how the state and size of the initial loyal and nonloyal segments change over time when $g ( T _ { n - 1 } )$ is set to $g _ { 0 }$ given the initial size of loyal segment in period $0 , \bar { l } _ { 0 } .$ For simplicity, we show only who buys the product, but not the price paid by each group $( \mathrm { e . g . , }$ some loyal customers mistakenly get the promotion and pay the discounted price). As explained before, those who purchased the product in the last period are known to the firm and become eligible for support at the start of this period, but the promotion might take effect at any time during this period. Similarly, for convenience of illustrating the state changes of old customers, the new customers w are not included in the figures, although they are included throughout our analyses. Note that the size of customers who were initially nonloyal but make a purchase in the next period increases with the level of both targeting and support CRM modules.

## Cost of CRM Implementation

We assume that the cost of CRM implementation, including software, hardware, consulting, and process reengineering, increases as more targeting- and support-related CRM modules are implemented. If the two types of CRM systems are implemented separately, the costs are $C ^ { S } ( { \dot { S } } )$ and $C ^ { T } ( T )$ with $C _ { S } ^ { S } > 0$ and $C _ { T } ^ { T } > \bar { 0 } ,$ , where superscript S and T represent support and targeting CRM modules, respectively. We also assume $\overset { \sim } { C } _ { S S } ^ { S } \geq 0$ and $C _ { T T } ^ { T } \geq 0 .$ . That is, the cost increases with the number of modules implemented at a nondecreasing rate. The convexity of cost functions in the system context is a frequently used assumption (see, e.g., Wang et al. 1997).

If a firm implements both types of modules simultaneously, the cost function is ${ \bf \dot { \cal C } } ^ { S T } ( S , T \mid e , I ) ,$ , which satisfies $\overset { \triangledown } { C _ { S } ^ { S T } } > 0 , \ C _ { T } ^ { S T } > 0 , \ C _ { S S } ^ { S T } \geq 0 ,$ , and $C _ { T T } ^ { S T } \geq 0$ as in separate implementation above. We conceptualize that there are two sources of cross-effects of costs in simultaneous implementation: vendor’s discount as an external source and diseconomies of scale as an internal source. Note that e is a parameter that captures the degree of vendor’s discount on a bundled purchase of two types such that $C _ { S e } ^ { S T } < 0 , \ C _ { T e } ^ { S T } <$ 0, $C _ { e } ^ { S \hat { T } } < 0 ,$ , and $C _ { S T e } ^ { S T } < \bar { 0 }$ with $e \geq 0 . { } ^ { 1 1 }$ We additionally assume $C _ { e e } ^ { S T } > 0$ because a vendor’s discount is usually offered to only a limited extent. Otherwise, $C ^ { S \bar { T } } > 0$ is not ensured when e is very large. Note that I captures diseconomies of scale or internal inefficiency in simultaneous implementation such that $C _ { S I } ^ { S T } > 0 , ^ { ^ { \prime } } C _ { T I } ^ { S T } > 0 , \ C _ { I } ^ { S T } > 0 ,$ and $C _ { S T I } ^ { S T } > 0 .$ The major source of diseconomies of scale and inefficiency stems from the difficulty to manage large-scale complex projects across multiple business areas (Keil and Mann 2000). In fact, Siebel, the largest CRM vendor, has recommended a phased implementation rather than a big-bang implementation of CRM modules to its customers due to the problems in managing large software projects. We assume $C _ { I I } ^ { S T } \ge 0$ to reflect that unfavorable factors in simultaneous implementation increase the cost of implementation at a nondecreasing rate. This assumption can be justified from the exponential growth in complexity and coordination difficulty in project management when the CRM implementation involves multiple divisions and business units within an organization, making the project difficult to manage. Without loss of generality, we assume $C ^ { S T } ( S , T | \stackrel { \smile } { e } = 0 , I = 0 ) = C ^ { T } + { \breve { C } } ^ { S }$ . Thus, positive I indicates diseconomies of scale such that $\dot { C } ^ { S T } ( S , T \mid e = 0 , I > 0 ) > C ^ { T } + C ^ { S }$ . Note that the sign of cross-effect of costs, $C _ { S T } ^ { S T } .$ , is determined by the magnitudes of both e and I.

Figure 1 Timeline and Illustration of the Model for Customers Who Were Loyal at Period 0  
![](/api/attachments/ERKASX7A/fulltext/images/15712e6e6ae263261bb10dea984b1b21e7462ff6590f52d0dccbeaa07c551a80.jpg)

Figure 2 Timeline and Illustration of the Model for Customers Who Were Nonloyal at Period 0  
![](/api/attachments/ERKASX7A/fulltext/images/4154c8d7c888088f59cd768058dfaae8ac7c95d68554dab3a5bccb045f6eb578.jpg)

## 4. CRM Implementation Strategy

We consider that each consumer has one purchasing incidence after CRM implementation and derive the optimal strategy in this section.<sup>12</sup> The CRM implementation decision involves two stages. The firm can choose from one of three CRM implementation strategies: targeting-specialization, support-specialization, and simultaneous implementation strategy. Then it decides the amount of investments in each component. For example, the transition matrix for the simultaneous implementation strategy is

$$
\begin{array}{c} B = \left[ \begin{array}{c c} f (S) & 1 - f (S) \\ g _ {0} f (S) + (1 - g _ {0}) \tau & 1 - g _ {0} f (S) - (1 - g _ {0}) \tau \end{array} \right] \\ = \left[ \begin{array}{c c} B _ {1 1} & B _ {1 2} \\ B _ {2 1} & B _ {2 2} \end{array} \right], \end{array}
$$

and the revenue is $R ^ { S T } = \{ \rho \cdot l _ { 0 } B _ { 1 1 } + \rho \cdot ( 1 - l _ { 0 } ) B _ { 2 1 } + w \tau \}$ $p + \{ \rho \cdot l _ { 0 } B _ { 1 2 } + \rho \cdot ( 1 - l _ { 0 } ) B _ { 2 2 } + w ( 1 - \tau ) \} \{ g ( T ) p - c ^ { \prime } \}$ We use $R ^ { j }$ and ç<sup>j</sup> to denote the revenue and the profit for the implementation strategy $j \in \{ T , S , S T \}$ The superscripts T , S, and ST denote the targetingspecialization, support-specialization, and simultaneous implementation strategies, respectively. Table 2 summarizes the notation used in this paper.

Table 2 Summary of Notations

<table><tr><td>Parameter</td><td>Description</td></tr><tr><td> $T$ </td><td>The degree of targeting-related CRM modules implemented</td></tr><tr><td> $S$ </td><td>The degree of support-related CRM modules implemented</td></tr><tr><td> $I_0$ </td><td>The initial fraction of loyal customers</td></tr><tr><td> $I_n$ </td><td>The size of loyal customers after support but before targeting in period  $n$ </td></tr><tr><td> $M_n$ </td><td>The market size in period  $n$ </td></tr><tr><td> $ρ$ </td><td>A fraction of customers who are still active in the next period</td></tr><tr><td> $w$ </td><td>Inflow of new potential customers</td></tr><tr><td> $τ$ </td><td>The probability of a nonloyal customer who did not make a purchase in the previous period to switch to a loyal segment</td></tr><tr><td> $p$ </td><td>Price charged by firm without a promotional offer</td></tr><tr><td> $c$ </td><td>Cost to reach individual customer</td></tr><tr><td> $d$ </td><td>Promotional discount for nonloyal customers</td></tr><tr><td> $c'$ </td><td>The cost to acquire one perceived nonloyal customer, which is  $c+d$ </td></tr><tr><td> $f(S)$ </td><td>The probability that a customer who purchased a product becomes loyal in the next period when  $S$  was implemented</td></tr><tr><td> $f_0$ </td><td>The base level of customer support without support-related CRM modules</td></tr><tr><td> $g(T)$ </td><td>The probability that firm can classify nonloyal customers as nonloyal customers correctly when  $T$  was implemented</td></tr><tr><td> $g_0$ </td><td>The base level of targeting capability without targeting-related CRM modules</td></tr><tr><td> $R^j$ </td><td>The revenue when the strategy  $j$  was chosen</td></tr><tr><td> $Π^j$ </td><td>The profit when the strategy  $j$  was chosen</td></tr><tr><td> $C^j$ </td><td>Cost to implement CRM modules when the strategy  $j$  was chosen</td></tr><tr><td> $I$ </td><td>An exogenous parameter to capture (dis)economies of scale in implementing two types of modules due to increased inefficiency and complexity</td></tr><tr><td> $e$ </td><td>An exogenous parameter to capture vendors’ discount on a bundled purchase of two types of CRM</td></tr><tr><td> $U$ </td><td>Utility of an individual customer when a product is purchased</td></tr><tr><td> $v$ </td><td>Customer’s valuation of a product and takes the value of either  $\bar{v}$  if a loyal customer or  $\underline{v}$  if a nonloyal customer</td></tr><tr><td> $p_L/p_{NL}$ </td><td>The endogenized price charged to a customer in the loyal/nonloyal segment</td></tr></table>

<sup>Proposition</sup> <sup>1.</sup> (i) There exist threshold levels $I ^ { + } , I ^ { + + } ,$ and $l ^ { + }$ such that the firm’s optimal CRM implementation strategy can be determined by the magnitudes of $l _ { 0 }$ and I as in the table below:

<table><tr><td></td><td>Diseconomies of scale in simultaneous implementation</td><td>Optimal strategy</td></tr><tr><td rowspan="2">Small loyal segment ( $l_0 < l^+$ )</td><td>Large ( $I > I^+$ )</td><td>Targeting CRM specialization</td></tr><tr><td>Small ( $I \leq I^+$ )</td><td>Simultaneous</td></tr><tr><td rowspan="2">Large loyal segment ( $l_0 \geq l^+$ )</td><td>Large ( $I > I^{++}$ )</td><td>Support CRM specialization</td></tr><tr><td>Small ( $I \leq I^{++}$ )</td><td>Simultaneous</td></tr></table>

where (1) $I ^ { + } = I ^ { + + }$ when $l _ { 0 } = l ^ { + } , \ ( 2 ) \ I ^ { + } > I ^ { + + }$ when $l _ { 0 } > l ^ { + }$ , and $\left( 3 \right) I ^ { + } < I ^ { + + }$ when $l _ { 0 } < l ^ { + }$

(ii) With the targeting-specialization strategy, the optimal implementation scope decreases with $l _ { 0 } .$ With the support-specialization strategy, the optimal implementation scope increases with $l _ { 0 } .$

(iii) There exists a threshold level $\sigma ^ { + }$ such that $i f c ^ { \prime } <$ $\sigma ^ { + } , l ^ { + } > 1$ and thus it reduces to the case $( l _ { 0 } < l ^ { + } )$ above. Also, there exists a threshold level $\sigma ^ { + + }$ such that $i f c ^ { \prime } >$ $\sigma ^ { + + } , l ^ { + } < 0$ and thus it reduces to the case $( l _ { 0 } \geq l ^ { + } )$ above.

$$
\sigma^ {+ +} = \frac {\rho \cdot g _ {0} \{f _ {0} - f (S ^ {*}) \} p - [ \rho \cdot \{1 - g _ {0} f (S ^ {*}) - (1 - g _ {0}) \tau \} + w (1 - \tau) ] g (T _ {0}) p}{\rho \cdot g _ {0} \{f (S ^ {*}) - f _ {0} \}}
$$

$$
+ \frac {[ \rho \cdot \{1 - g _ {0} f _ {0} - (1 - g _ {0}) \tau \} + w (1 - \tau) ] g (T ^ {*}) p + C ^ {S} (S ^ {*}) - C ^ {T} (T ^ {*})}{\rho \cdot g _ {0} \{f (S ^ {*}) - f _ {0} \}},
$$

and

$$
\begin{array}{l} \sigma^ {+} = (\rho \{f _ {0} - f (S ^ {*}) \} p + \{\rho (1 - f _ {0}) + w (1 - \tau) \} g (T ^ {*}) p \\ \qquad - \{\rho \cdot \{1 - f (S ^ {*}) \} + w (1 - \tau) \} g _ {0} p - C ^ {T} (T ^ {*}) + C ^ {S} (S ^ {*})) \\ \qquad \cdot (\rho \cdot \{f (S ^ {*}) - f _ {0} \}) ^ {- 1}, \end{array}
$$

where <sup>∗</sup> denotes the optimal level chosen for targeting- and support-related CRM modules.

Proposition 1 derives the optimal implementation strategy and has several important implications. First, the diseconomies of scale parameter I in simultaneous implementation plays an important role in determining the firm’s optimal CRM implementation strategy. There always exist threshold levels I<sup>+</sup> and $I ^ { + + }$ that determine the choice of optimal CRM strategies between specialization and simultaneous strategies. To the contrary, there do not necessarily exist such threshold levels of e. For example, if $I = 0$ (i.e., no diseconomies of scale) simultaneous strategy weakly dominates specialization strategies for all e. Thus, we conclude that I is a more important criterion to consider in deciding between simultaneous and specialization strategies. This result is driven by our assumption that $C _ { I I } ^ { T \widetilde { S } } \geq 0$ . To the extent that the assumption is justified, a firm should not give into a vendor’s marketing efforts and discounts in the presence of considerable diseconomies of scale in simultaneous implementation. Figure 3 illustrates Proposition $1 - i )$ graphically. Note that $I ^ { + } = I ^ { + + }$ when $l _ { 0 } = l ^ { + }$

Figure 3 Optimal CRM Implementation Strategy on l I-Plane  
![](/api/attachments/ERKASX7A/fulltext/images/c040f2bb32cdbc2fa7cd3a61d533c59add829376fae20c9e5a7c2e7487674e13.jpg)

Second, a firm with a large loyal customer base will prefer specialization in support-related CRM technology to targeting-related CRM technology. Thus, under a sufficiently large loyal customer base, a firm will choose between support specialization strategy and simultaneous implementation strategy, while it will choose between targeting specialization strategy and simultaneous implementation strategy under a small loyal customer base. For example, when Union National Community Bank, a small regional bank in Mount Joy, PA, could not retain many customers, it decided to install a CRM package that allowed it to segment its 37,000 accounts by profitability using CRM analytics and business intelligence modules (Overby 2002). This example illustrates the efficacy of the targeting-oriented strategy under a small segment of loyal customers. As an example of support-specialization, the CRM implementation in York International, a leading provider of heating, ventilation, and air conditioning services, focused more on call center, service sales, and service execution, which can be classified as support-related modules in our categorization. Our comparative statics analysis in Proposition 1(ii) reveals that the change in the size of initial loyal segment tends to influence the optimal scopes for targeting and support CRM implementation in the opposite direction. A larger loyal customer base increases the scope for support-specialization but decreases the scope for targeting-specialization. Therefore, a firm endowed with more loyal customers not only prefers support-specialization as in Proposition 1(i) but also deploys support CRM technology with a larger scope. Later, Proposition 2 will provide more insights on why the support-specialization is preferred to targeting-specialization under a large loyal customer base.

Third, it is possible that either the targeting-specialization strategy or support-specialization strategy strictly dominates the other strategy, depending on the cost of attracting nonloyal customers, which is represented by $c ^ { \prime }$ in our model. If this cost is smaller than $\sigma ^ { + }$ , the targeting-specialization dominates support-specialization. However, the supportspecialization dominates targeting-specialization if the cost of attracting new customers is larger than $\sigma ^ { + + }$ This result is reasonable because a firm with low cost of attracting nonloyal customers does not have incentive to provide cutting-edge support service to retain its old customers, and thus targeting-specialization becomes optimal. We view $c ^ { \prime }$ is exogenously given in each industry as empirical evidence supports that the ROI of customer-oriented activities varies across industries (Gupta and Zeithaml 2006).

## 5. Strategic Implications of CRM Implementation

## Substitution Effects of CRM Technologies

<sup>Proposition</sup> <sup>2.</sup> Suppose simultaneous implementation. (i) On the revenue side, the two types of CRM modules substitute the effect of each other. (ii) Defining the degree of revenue substitutability as $S B = - \dot { R } _ { S T } ^ { \dot { S } T }$ 1 SB decreases in S and $T$ but increases in  and $l _ { 0 } .$ (iii) Under sufficiently large revenue substitutability, the optimal level of $S ^ { * }$ might decrease with w. Similarly, under sufficiently large revenue substitutability, the optimal level of $T ^ { * } o r \stackrel { } { S ^ { * } }$ might decrease with $\rho .$

In recent years, the topic of interaction among activity choices of firms has received a great deal of attention in the organization, economics, management, and IS literatures (Milgrom and Roberts 1990, 1995; Siggelkow 2002; Zhu 2004; Stieglitz and Heine 2007). Assets or activities are mutually complementary “if the levels of any subset of the activities are increased, then the marginal return to increases in any or all the remaining activities rises” (Milgrom and Roberts 1990). On the other hand, activities are substitutes, if doing more of one activity decreases the marginal benefit of the other activities (Stieglitz and Heine 2007). It is important to understand the complementary or substitutive nature of different assets and activities to realize the full benefit of firms’ investments while avoiding inefficiencies and redundancies (Siggelkow 2002). Our interest in the CRM context is whether the investment in one type of CRM technology will increase (i.e., strategic complements) or decrease $( \mathrm { i . e . , }$ strategic substitutes) the marginal return to the increase in the other type of CRM technology. Avoiding misperceptions of such interactions is important because such misperceptions are likely to lead to either underinvestment or overinvestment in CRM systems.

Interestingly, we find that one type of CRM technology could substitute the effectiveness of the other type of CRM technology on the revenue side. We can explain this result in the following manner. The investment in support-related modules is likely to increase the size of loyal segment. However, the marginal benefit of targeting-related modules relies on the size of the nonloyal segment. The more loyal customers there are, the less incentive there is to invest in targeting-related modules because the ROI is likely to decrease. Therefore, as the level of support increases resulting in more loyal customers, the marginal return to investing in targeting modules decreases. These interactions create a substitution effect of the investments in two types of modules. Additionally, the degree of revenue substitution decreases in both S and T .

A more traditional view on why too much investment in CRM at once might not work has focused on the ignorance of diseconomies of scale on the cost side, which is modeled as I in this paper. Our finding suggests that a firm should avoid overinvestment in CRM by considering the substitution effect on the revenue side as well. It will be detrimental if a firm considers the two types of CRM systems as strong complements. Figure 4 visualizes our proposition. The marginal return out of investing more in one type of CRM technology, which is represented by the slope in the graph, is smaller under larger investments in the other type of CRM. The differences in slopes converge as a firm invests more in one type of CRM.

We further examine under what conditions the degree of revenue substitutability is greater. When fewer customers exit the market (larger ), the substitution effect should be taken more seriously in simultaneous implementation. The market growth w does not influence the substitution because the CRM initiative by nature focuses on existing customers. The degree of substitution increases with the size of initial loyal segment. Taken together, other things being equal, the misperception and overinvestment in CRM systems may be more common when a firm is initially endowed with more loyal customers and fewer customers exit the market. This will be an interesting empirical question for future research.

Proposition 2(iii) adds the implication of revenue substitutability. In anticipation of favorable market conditions, managers might implement both types of CRM technologies in larger scopes. A higher degree of market continuity $\rho$ and market growth w are considered such favorable conditions for business. However, our comparative statics analysis shows that an increase in $\rho$ or w could lead to a decrease in the optimal implementation scope for either support or targeting CRM modules. For instance, under large negative revenue substitution it becomes likely that $R _ { S T } ^ { S T } < C _ { S T } ^ { S T }$ ; in that case, it is optimal to reduce investments in support CRM technology while investing more in targeting CRM technology as w increases. Similarly, the scope for one of the two CRM technologies might decrease with $\rho$ under a high degree of revenue substitution or large positive cross-effect in cost $( \mathrm { i . e . , ~ } C _ { S T } ^ { S T } )$ for the simultaneous implementation case. That is, the revenue substitutability could lead to specializing more in one type of CRM technologies even under favorable business conditions. If managers simply take more investments in both CRM technologies for granted in anticipation of favorable market conditions in terms of an enhanced customer base, the chance of overinvestment and low ROI will become higher.

Figure 4 Substitutability of Targeting and Support CRM Technologies  
![](/api/attachments/ERKASX7A/fulltext/images/f330480a8c850b42cc79e58bb737c6cf935948702786fc3d61cc46c94450061d.jpg)

There are other interesting points that we would like to highlight in reference to Proposition 2. Hendricks et al. (2007) has examined the impact of ERP, SCM, and CRM systems on a firm’s long-term stock market performance and profitability measures. The authors have shown that firms’ CRM efforts did not pay off in terms of stock market returns and profitability measures, compared to returns to SCM and ERP implementations. If we believe that the market is sufficiently efficient, the result implies that there might exist systematic inefficiencies in firms’ investments in CRM systems. In fact, it is an empirical question whether such systematic overinvestments might be present due to the ignorance of the substitution effect. Nonetheless, we do not see many CRM success stories where a company has deployed every CRM module and has had a strong financial gain as well. Another issue we consider about Proposition 2 is the potential cross-departmental conflicts due to investments in different CRM technologies. In many cases, a firm’s customer analysis and targeting activities are conducted by the marketing department, while customer support activities might be performed by a separate unit. If the performance metrics for the two departments are not aligned, the substitutability effect might create conflicts because activities by one department could decrease the performance of other departments. This shows why CRM should be implemented as an organizational strategic initiative rather than as a single department’s efforts.

![](/api/attachments/ERKASX7A/fulltext/images/962aaa328026a0a269df9e85d75de329c0107f895cda7e03a814ef7b1f378199.jpg)

## Integration of CRM Technologies

We have so far assumed that two types of CRM do not directly influence the efficacy of each other. However, it is possible that a firm benefits more from the integration of front-end support CRM and back-end targeting CRM systems. The case of Harrah’s Entertainment in the casino entertainment industry shows how integrated processes in relationship management can improve competitive advantage. Harrah’s collected and consolidated information from hotel management, slot machine, reservation, and transactional systems to classify its customers into different segments. The company in turn could utilize its analysis to better support its customers in a more individualized fashion (Loveman 2003).<sup>13</sup> Despite the challenge of full integration, it is worthwhile to examine how the existence and the degree of such integration benefits will change the nature of the substitutability of the two types of CRM technologies. Both CRM capabilities $( \dot { f }$ and g) are now functions of both targeting and support CRM technologies such that we have $f ( S , T )$ and $g ( T , S )$ instead of $f ( S )$ and $g ( T )$ . Such integration benefits might be realized when (1) a firm’s targeting (support) capability improves as a firm invests more in support (targeting) CRM technology such that $g _ { s } =$ $\partial g ( T , \stackrel { \cdot } { S } ) / \partial S > 0 ( f _ { T } = \partial f ( S , T ) / \partial T > 0 )$ , or (2) the marginal improvement in targeting (support) capability by investing in firm’s targeting (support) CRM increases as a firm invests more in support (targeting) CRM technology such that $g _ { S T } > 0 \ ( f _ { S T } > 0 )$

<sup>Proposition</sup> <sup>3.</sup> There exists a complementarity between targeting and support-related CRM technologies if and only if $\dot { \cdot } \dot { f } _ { S T } + J _ { 1 } \cdot J _ { 2 } \cdot g _ { S T } > ( f _ { T } g _ { S } + f _ { S } g _ { T } ) \cdot J _ { 2 } ,$ , where

$$
\begin{array}{r l} & J _ {1} = \left[ \rho \cdot l _ {0} (1 - f) + \rho \right. \\ & \qquad \cdot (1 - l _ {0}) \{1 - g _ {0} f - (1 - g _ {0}) \tau \} + w (1 - \tau) \big ] / \\ & \qquad \rho \{l _ {0} + (1 - l _ {0}) g _ {0} \} > 0, \end{array}
$$

and

$$
J _ {2} = p / (p - g p + c ^ {\prime}) > 0.
$$

Proposition 3 implies that positive $f _ { T }$ and $g _ { S }$ alone do not ensure the complementarity between the two types of CRM. For example, investing in targetingrelated CRM might improve the overall level of support-capability, but it is not sufficient to create the strategic complementarity. Unless both targeting and support CRM technologies are managed in a fully integrated fashion such that a firm’s investment in one type of CRM boosts up the marginal benefit of the other type of CRM technologies, the two types of CRM technologies are likely to work as strategic substitutes. It is difficult to avoid overinvestment in CRM if managers consider different types of CRM as strategic complements based on integration benefits without a clear understanding of the magnitude and nature of the integration benefits.

## 6. Producer and Consumer Surplus

In this section, we examine producer and consumer surplus in detail when a firm adopts targeting- and support-related CRM modules simultaneously. We also examine how the revenue substitutability is linked with consumer surplus. We have made an important assumption that the price of product or service is fixed. To analyze the impact of different types of CRM technologies on social surplus, we endogenize a firm’s price in this section. We assume a threestage decision by a firm and customers; at stage 1, the firm determines its investments in CRM technologies; at stage 2, the firm decides on its price and promotion; at stage $^ { 3 , }$ consumers decide whether to buy or not. Note that our earlier results on substitutability are not affected given this sequential three-stage decision in the spirit of backward induction.

We define a utility function of an individual customer as $U = v - p _ { i } ,$ which is consistent with our previous transition matrix. v denotes customers’ valuation of a good influenced by service quality, which is distributed on two valuations {v°, v}. That is, a loyal customer’s valuation of a product or service is ${ \overline { { v } } } ,$ while a nonloyal customer $\cdot \prime _ { \mathrm { { S } } }$ valuation is v with $\overline { { v } } > \underline { { v } } . ^ { 1 4 }$ Given a firm’s technologies and customers’ valuation, its equilibrium price to attract all loyal customers, $p _ { L } ,$ is $\bar { v }$ as those in the loyal segment will not take any price higher than it. Any price lower than $\bar { v }$ is not at equilibrium because the firm can earn more by charging higher price. Similarly, for the nonloyal segment, given the technologies, its equilibrium price to capture all nonloyal customers is $p _ { N L } = \underline { { v } }$ . It follows that the promotional discount is $d = \overline { { v } } - \underline { { v } }$ . To confine our analysis to a case where selling to loyal and nonloyal customers is profitable, we assume $\underline { { v } } > c .$ The total consumer surplus is given as follows:

$$
\begin{array}{c} C S = \big \{\rho \cdot l _ {0} B _ {1 2} + \rho \cdot (1 - l _ {0}) B _ {2 2} + w (1 - \tau) \big \} \\ \cdot \big \{1 - g (T) \big \} (\overline {{v}} - \underline {{v}}). \end{array}
$$

Among $\{ \rho \cdot l _ { 0 } B _ { 1 2 } + \rho \cdot ( 1 - l _ { 0 } ) B _ { 2 2 } + w ( 1 - \tau ) \}$ nonloyal customers who receive a promotional offer, $1 - g ( T )$ of them are those who are incorrectly classified as nonloyal customers. The additional surplus for each loyal customer in this category is ${ \overline { { v } } } - { \underline { { v } } } .$

Proposition 4. <sub>(i)</sub> $\partial \Pi ^ { * } / \partial l _ { 0 } > 0$ in the equilibrium. In addition, $\partial \Pi / \partial l _ { 0 }$ increases in S but decreases in T .

(ii) For the simultaneous implementation, consumer surplus decreases with firm’s investments in either targetingor support-related CRM technologies. The average surplus per consumer also decreases with firm’s investments in either targeting- or support-related CRM technologies.

(iii) $\bar { C S } _ { S T } > 0$ such that the marginal effect of supportrelated CRM on consumer surplus increases with targetingrelated CRM, and vice versa.

(iv) If $S _ { I } ^ { * } ~ < ~ 0$ and $T _ { I } ^ { * } ~ < ~ 0 ,$ consumer surplus increases with diseconomies of scale in simultaneous implementation (I ).

Proposition 4(i) reveals that a firm with more favorable market conditions in terms of $l _ { 0 }$ will end up with more profits after its CRM implementation, no matter what implementation strategy is chosen. Loyal customers are important assets that make CRM more profitable. While a firm with a large loyal customer base might seemingly have little incentive to go with CRM, ceteris paribus, it still has an incentive to implement CRM because $\partial \Pi ^ { * } / \partial l _ { 0 } > 0 .$ . We can interpret $\partial \Pi / \partial l _ { 0 }$ as the marginal value of having one more unit of loyal customer. As $\partial \Pi / \partial l _ { 0 }$ increases in S but decreases in T , the shift of one nonloyal customer to a loyal one is more profitable for a firm when it invests in higher support capability. This is because with the higher level of support capability, a firm is more likely to retain the loyal customer, and thus it benefits from a larger base of loyal customers. When it improves targeting capability, the value of loyal customers is not as much because it can tell more precisely only to which segment each customer belongs; thus its profit does not gain from the total base of loyal customers.

Proposition 4(ii) states that consumer surplus essentially decreases with investments in either type of

CRM systems. Proposition 4(ii) makes sense because a firm can extract more surplus from its loyal customers as it improves its targeting accuracy with more sophisticated targeting-related CRM modules. Because improved targeting accuracy enables a firm to charge different prices to different segments of customers more precisely, consumer surplus from loyal customers who could purchase at lower price diminishes. This is similar to Chen et al. (2001), who also showed that a firm can extract more surplus from its loyal customers as its targetability improves. We find that an increase in S leads to a decrease in consumer surplus as well. Although firms might emphasize that they serve their customers better with their advanced support techniques and employees, investing in support-related CRM technology can be viewed as a method to extract more surplus from customers. We further find that the average surplus per consumer decreases in S and T . This shows that the decreased total consumer surplus due to CRM results not from the change in customer base due to CRM but from more efficient extraction of consumer surplus from each consumer on average. Proposition 4(iii) demonstrates the changes in consumer surplus with more investments in both CRM types simultaneously. As the level of investment in one type of CRM technology increases, a firm’s marginal efficiency gain in extracting surplus by investment in the other type decreases. This result is like the mirror image of the revenue substitutability.

Proposition 4(iv) examines how the cost of CRM implementation influences overall consumer surplus. We find that consumer surplus increases with diseconomies of scale in simultaneous implementation (I 5 as long as $S _ { I } ^ { * } < 0$ and $T _ { I } ^ { * } < 0 .$ . Thus, a firm’s internal inefficiency in managing a large scale CRM implementation project might contribute to consumers’ excess surplus. However, it is notable that most companies misconstrue CRM capabilities and implement such systems with a larger scope than it can manage or actually needs. Many prior studies in IS have identified that managers might overestimate project management capability and face project cost escalation (Keil and Mann 2000). In the CRM context, if managers fail to realize that diseconomies of scale in simultaneous implementation (I 5 are on the rise when $S _ { I } ^ { * } < 0$ and $T _ { I } ^ { * } < \bar { 0 } .$ , they might not reduce investments in support or targeting modules. The resultant outcomes are a loss in the firm’s profit due to suboptimal decisions and, interestingly, a decreased consumer surplus than it would be under the optimal CRM levels. Although $S _ { I } ^ { * } < 0$ and $T _ { I } ^ { * } < 0$ are likely in most cases, some exceptions could occur as well. Under large negative $\Pi _ { S T . } ^ { S \hat { T } }$ , consumer surplus might not increase with diseconomies of scale in simultaneous implementation (I 5 as either $S _ { I } ^ { * } > 0$ or $T _ { I } ^ { * } > 0$ is possible. Because we assume $C _ { S T I } ^ { S T } > 0 \ ( \ S 3 )$ , an exception may take place only when the revenue substitutability is large negative and/or I is very large such that $C _ { S T } ^ { S T }$ is sufficiently large and positive.

While investments in IT have been shown to increase consumer surplus at the aggregate level $( \mathrm { e . g . , }$ Brynjolfsson 1996), there is a possibility that firms’ CRM investments enable them to extract more surplus from consumers by building long-term relationships with customers and decreasing consumer welfare in the end. The marketing literature has begun to pay attention to the welfare-decreasing impact of technology as well. For example, Tyagi (2004) showed that a reduction in transaction cost by technological advance reduces the surplus of a certain segment of consumers and the consumer share in the total social surplus. Our contribution is that an individual firm’s investments, even in support-related CRM primarily to enhance customers’ satisfaction, can be used as a tool to extract more surplus, and the impact is determined by interactions with targeting technologies. Our study extends current understanding of managerial roles in technology adoption in that an overestimation of returns or an overly optimistic view of CRM implementation capability reduces overall consumer surplus as well.

## 7. Discussions

## CRM Implementation with Multiple Periods

We have characterized the CRM investment decisions as a one-time phenomenon. However, a firm might decide to invest in CRM in each period. Such an approach is suitable when market conditions keep changing over time and future conditions can be better estimated based on recent developments. For example, customer exit and entry rates might change from period to period, or new CRM modules might become available. In this scenario, our modeling approach can be used repeatedly by managers to finetune the CRM strategy in each period.

We have so far assumed that CRM implementation is completed within a single period. Now we consider CRM implementation over multiple periods. Despite the debate about which approach is better for enterprise software implementation, an allat-once or a phased implementation (Fichman and Moses 1999), there has been little research on the revenue aspect of the two approaches in the CRM context. Because some CRM projects can take years to complete, a firm’s profit is likely to be sensitive to not only the implementation approach but also the order of implementing different CRM modules. That is, in the case of phased implementation, should a firm improve the relationship with customers through enhanced support-related CRM technology first, or adopt targeting-related CRM technology first for immediate revenue generation by discrimination?

For this analysis, we use  as the discount factor, with $\delta \in ( 0 , 1 )$ . We find the following results.

• With strong diseconomies of scale in simultaneous implementation, the optimal strategy shifts from the all-at-once implementation to the phased implementation.

• In general, a larger loyal customer segment makes a firm prefer to implement support-related CRM modules first and then move toward targetingrelated CRM modules.<sup>15</sup>

• For both all-at-once and phased implementation strategies, $\partial T ^ { * } / \partial \delta > 0$ and $\partial S ^ { * } \bar { / } \partial \delta > 0$ if the two CRM technologies are complementary or moderately substitutive. If the substitutability is greater than a certain point, either $\partial T ^ { * } / \partial \delta < 0$ or $\partial \bar { S } ^ { * } / \partial \breve { \delta } < 0$ is possible.

The first two points highlight that our findings based on the two-period setting are similar to Proposition 1. Our last point additionally explains why overinvestments in CRM might occur based on the two-period setting. When the discount factor $\delta \in ( 0 , 1 )$ increases such that the relative importance of future profit increases, the seemingly reasonable response by a firm is to increase the implementation scope. So $\operatorname { f a r } ,$ it has been believed that firms deploy CRM in larger scopes early to enjoy the full benefits of CRM over a longer period of time. However, when the degree of revenue substitution or diseconomy of scale is sufficiently strong (resulting in large negative $\Pi _ { S T } ^ { j } ) .$ , an increase in $\delta$ might even decrease the optimal implementation scope for either targeting or support CRM. That is, although the relative importance of future profit increases, a firm might have to reduce the implementation scope to avoid the severe substitution in future profit incurred by today’s large investments in both types of CRM technologies. This insight is new because one of the greatest incentives for a firm to deploy CRM with wider scope has been to realize larger profits as early as possible. Overall, our analysis of the multiperiod setting supports our main findings.

## 8. Conclusions

In this paper, we developed a parsimonious model to investigate the optimal CRM implementation strategy under various conditions. The main contribution of this paper is that instead of viewing CRM technology as a single composite innovation, we examined the interactive nature of different types of CRM technologies and thus attempted to open up the “black box” of CRM system implementation. Without the consideration of the interactions between different types of CRM technologies, firms may make biased decisions to either overinvest or underinvest in CRM systems. This could explain why many companies are not satisfied with their CRM investments and report unexpectedly low ROI. We investigated how profits and optimal scope of CRM implementation change under varying conditions. In addition, a firm can extract more surplus from customers not only from its investments in enhanced capability to discriminate between loyal and nonloyal customers but also through investments in customer support technologies to enhance customer loyalty. Surprisingly, with an increase in diseconomies of scale in simultaneous implementation of both types of CRM systems, the optimal scope of each type might reduce, resulting in higher consumer surplus. We have also found that the mere existence of systems integration benefits might not eliminate the risk of overinvestment in CRM systems. We extended our analysis to multiperiod settings and addressed the issue of selecting the right implementation approach between an all-at-once and a phased implementation to selecting the right order of CRM implementation. We find that even when the future benefit becomes relatively more important, it might be optimal to reduce the implementation scope for one of the two types of CRM due to revenue substitutability. Our model considers CRM costs, IT implementation issues, and marketing-related factors and is helpful in determining the right CRM technology, in the right amount and in the right order. In contrast to prior studies in marketing and economics, where the technologies to distinguish customers is assumed to be readily available $( \mathrm { e . g . } ,$ , Chen et al. 2001, Villas-Boas 2004), our study examines the acquisition of both targeting and support technologies in the presence of project management risks and integration benefits.

Despite the new results of this paper, our model contains some restrictive assumptions for analytical tractability. The generalizability of the results can be limited to the extent that our assumptions do not reflect specific contexts. First, we assume that targeting CRM in our model is mainly used for price discrimination. However, it could also be used for other purposes: cross-selling, up-selling, and new product development. Some CRM components such as marketing automation modules are also aimed to save and better control marketing costs. That is, our classification of CRM technologies might not be exhaustive. Nevertheless, the classification is useful, corresponds to the practitioner’s view of CRM, and provides insights into what the firm’s CRM implementation strategy should be. Second, we assume that CRM systems will be developed and delivered as intended, once a firm makes the required investments. Empirical evidence supports that developing and adopting new enterprise-wide systems are challenging and could even fail. However, our paper highlights why even technically successful systems might not produce the economic returns that a firm has expected at the time of investment decision. Third, an alternative approach will be to further consider the heterogeneity of individual customers. For instance, we can model consumer utility as $U = \theta + v - p$ with a uniformly distributed valuation parameter . It allows even a nonloyal customer to make a purchase without a promotional offer when her valuation is large because of her needs. We did not take this approach because our main interest is on the implementation side, and our current model setting is sufficient in showing the welfare-decreasing effects of supportrelated CRM technology. Fourth, our result on consumer surplus is based on the assumption that CRM investments do not influence the reservation price of consumers. This might be restrictive because some firms claim that upon CRM implementation, they also enhance the quality of service and provide individualized solutions. Last, we do not directly address a generalized model with n periods, which would involve numerical solutions. In general, the purchasing incidences of customers would depend on the nature of products and services and the specific industry. The implementation period of CRM systems might sometimes extend beyond two periods.

This study can be improved and extended in several ways. First, our model can be extended to examine the effect of competition. An interesting question would be how the role of supportor targeting-related CRM innovation changes under competition. Second, while we assume that customers are not forward-looking, it is possible that customers’ behaviors change when they can predict that they will be locked in for being loyal. For example, a rather extreme case can be found in Villas-Boas (2004), where a monopolist can be worse off if it can identify its existing customers. Third, empirical tests of the results in the paper might be also interesting. For example, we can study whether IT spending in CRM has actually increased or decreased consumer surplus. The substitutability of investments on the revenue side in different types of CRM systems can also be tested at the firm level. A number of possible extensions of our paper imply that it can point to further research on this topic of academic and practical significance.

## 9. Electronic Companion

An electronic companion to this paper is available as part of the online version that can be found at http:// isr.journal.informs.org/.

## Acknowledgments

The authors thank all seminar participants at the Carnegie Mellon University and the 2006 International Conference on Information Systems (ICIS), the senior and associate editors, and the two anonymous reviewers for their helpful comments and suggestions. An earlier version of this paper was presented in ICIS (International Conference on Information Systems), 2006.

## References

Ashworth, M., T. Mukhopadhyay, L. Argote. 2004. Information technology and organizational learning: An empirical analysis. Proc. 25th Internat. Conf. Inform. Systems, Washington, DC, 481–492. http://aisel.aisnet.org/icis2004/38.

Barua, A., C. H. Kriebel, T. Mukhopadhyay. 1991. An economic analysis of strategic information technology investments. MIS Quart. 15(3) 313–331.

Barua, A., C. H. Kriebel, T. Mukhopadhyay. 1995. Information technologies and business value: An analytic and empirical investigation. Inform. Systems Res. 6(1) 3–23.

Beggs, A., P. Klemperer. 1992. Multi-period competition with switching costs. Econometrica 60(3) 651–666.

Brynjolfsson, E. 1996. The contribution of information technology to consumer welfare. Inform. Systems Res. 7(3) 281–300.

Brynjolfsson, E., L. Hitt. 1996. Paradox lost? Firm-level evidence on the returns to information systems spending. Management Sci. 42(4) 541–558.

Chen, Y., G. Iyer. 2002. Consumer addressability and customized pricing. Marketing Sci. 21(2) 197–208.

Chen, Y., C. Narasimhan, Z. J. Zhang. 2001. Individual marketing with imperfect targetability. Marketing Sci. 20(1) 23–41.

Clark, T. 2004. The key to success. Consumer Goods Tech. (March) 15–16. http://www.consumergoods.com/ME2/Sites/dirmod .asp?sid=234FFCB1E8DF4FACBAFF60DFFD8AD37C&nm=&type =MultiPublishing&mod=PublishingTitles&mid=A533BDC658294- 7448BBFA37BFF6394FF&tier=2&SiteId=7E5BCA545BF5490C84- FD6DF21BB791BF&did=BF715CFAF59B488C99260862C3C22096 &dtxt=March+2004.

Cotteleer, M. J., E. Bendoly. 2006. Order lead-time improvement following enterprise information technology implementation: An empirical study. MIS Quart. 30(3) 643–660.

Cyert, R. M., M. H. DeGroot, C. A. Holt. 1978. Sequential investment decisions with Bayesian learning. Management Sci. 24(7) 712–718.

Davamanirajan, P., R. J. Kauffman, C. H. Kriebel, T. Mukhopadhyay. 2006. Systems design, process performance, and economic outcomes in international banking. J. MIS 23(2) 67–92.

Davenport, T. H. 2006. Competing on analytics. Harvard Bus. Rev. 84(1) 98–107.

Demirhan, D., V. S. Jacob, S. Raghunathan. 2006. Information technology investment strategies under declining technology cost. J. MIS 22(3) 321–350.

Devaraj, S., R. Kohli. 2003. Performance impacts of information technology: Is actual usage the missing link? Management Sci. 49(3) 273–289.

Dyche, J. 2001. The CRM Handbook: A Business Guide to Customer Relationship Management. Addison-Wesley, Boston.

Ebner, M., A. Hu, D. Levitt, J. McCrory. 2002. How to rescue CRM. McKinsey Quart. Special Edition: Tech. (4) 49–57.

Fichman, R. G., S. A. Moses. 1999. An incremental process for software implementation. Sloan Management Rev. 40(2) 39–52.

Fox, F. 2001. CRM nightmare will go away. COMPUTER-WORLD (December 03). Accessed October 2010, http://www .computerworld.com/s/article/66195/CRM.

Gartner. 2007. Gartner says worldwide customer relationship management software market will grow 14 percent in 2007. Accessed October 2010, http://www.gartner.com/it/page.jsp ?id=519316.

Gartner. 2009. Gartner says reviewing the state of CRM in 2000 foretells its future in 2020. Accessed January 2010, http://www .gartner.com/it/page.jsp?id=899012.

Gattiker, T. F., D. L. Goodhue. 2005. What happens after ERP implementation: Understanding the impact of interdependence and differentiation on plant-level outcomes. MIS Quart. 29(3) 559–585.

Gupta, S., V. Zeithaml. 2006. Customer metrics and their impact on financial performance. Marketing Sci. 25(6) 718–739.

Hendricks, K., V. Singhal, J. Stratman. 2007. The impact of enterprise systems on corporate performance: A study of ERP, SCM and CRM system implementation. J. Oper. Management 25(1) 65–82.

Hitt, L. M., D. J. Wu, X. Zhou. 2002. Investment in enterprise resource planning: Business impact and productivity measures. J. Management Inform. Systems 19(1) 71–98.

IT Facts. 2005. Global CRM market is worth \$3.2 bln in 2005. Accessed November 2008, http://blogs.zdnet.com/ITFacts/ ?p=8423.

Jayachandran, S., S. Sharma, P. Kaufman, P. Raman. 2005. The role of relational information processes and technology use in customer relationship management. J. Marketing 69(4) 177–192.

Keil, M., J. Mann. 2000. Why software projects escalate: An empirical analysis and test of four theoretical models. MIS Quart. 24(4) 631–664.

Kekre, S., T. Mukhopadhyay. 1992. Impact of electronic data interchange on quality improvement and inventory reduction programs: A field study. Internat. J. Production Econom. 28(3) 265–282.

Lacey, E. 2002. Siebel competitor offers free licenses. ZDNet UK. Accessed April 2006, http://news.zdnet.co.uk/software/0 ,39020381,2110442,00.htm.

Laudon, K., J. Laudon. 2005. Management Information Systems: Managing the Digital Firm, 9th ed. Prentice Hall, Upper Saddle River, NJ.

Loveman, G. 2003. Diamonds in the data mine. Harvard Bus. Rev. 81(5) 109–113.

Manakas, T. 2002. Popping bubbles-maximizing CRM ROI. CRM Today Article. Accessed October 2010, http://www.crm2day .com/highlights/EpFlkEAkEpNxESiDvF.php.

Melville, N., K. Kraemer, V. Gurbaxani. 2004. Review: Information technology and organizational performance: An integrative model of IT business value. MIS Quart. 28(2) 283–322.

Milgrom, P., J. Roberts. 1990. The economics of modern manufacturing: Technology, strategy, and organization. Amer. Econom. Rev. 80(3) 511–528.

Milgrom, P, J. Roberts. 1995. Complementarities and fit: Strategy, structure, and organizational change in manufacturing. J. Accounting Econom. 19(2) 179–208.

Mithas, S., M. S. Krishnan, C. Fornell. 2005. Why do customer relationship management applications affect customer satisfaction? J. Marketing 69(4) 201–209.

Mittal, V., W. A. Kamakura. 2001. Satisfaction, repurchase intent and repurchase behavior: Investigating the moderating effect of customer characteristics. J. Marketing Res. 38(1) 131–142.

Mukhopadhyay, T., S. Kekre. 2002. Strategic and operational benefits of electronic integration in B2B procurement processes. Management Sci. 48(10) 1301–1313.

Mukhopadhyay, T., V. Mangal. 1997. Direct and indirect impacts of information technology applications on productivity: A field study. Internat. J. Electronic Commerce 1(3) 85–100.

Mukhopadhyay, T., S. Kekre, S. Kalathur. 1995. Business value of information technology: A study of electronic data interchange. MIS Quart. 19(2) 137–156.

Mukhopadhyay, T., J. Lerch, V. Mangal. 1997a. Assessing the impact of information technology on labor productivity: A field study. Decision Support Systems 19(2) 109–122.

Mukhopadhyay, T., S. Rajiv, K. Srinivasan. 1997b. Information technology impact on process output and quality. Management Sci. 43(12) 1645–1659.

Overby, S. 2002. The little banks that could. CIO 15(16) 102–108.

Payne, A., P. Frow. 2005. A strategic framework for customer relationship management. J. Marketing 69(4) 167–176.

Peppers, D., M. Rogers, B. Dorf. 1999. Is your company ready for one-to-one marketing? Harvard Bus. Rev. 77(1) 3–12.

Ranganathan, C., C. V. Brown. 2006. ERP investments and the market value of firms: Toward an understanding of influential ERP project variables. Inform. Systems Res. 17(2) 145–161.

Rigby, D. K., D. Ledingham. 2004. CRM done right. Harvard Bus. Rev. 82(11) 118–129.

Rigby, D. K., F. Reichheld, P. Schefter. 2002. Avoid the four perils of CRM. Harvard Bus. Rev. 80(2) 101–109.

Riggins, F. J., T. Mukhopadhyay. 1994. Interdependent benefits from interorganizational systems: Opportunities for business process re-engineering. J. Management Inform. Systems 11(2) 37–57.

Rust, R. T., T. S. Chung. 2006. Marketing models of service and relationships. Marketing Sci. 25(6) 560–580.

Rust, R. T., P. C. Verhoef. 2005. Optimizing the marketing interventions mix in intermediate-term CRM. Marketing Sci. 24(3) 477–489.

Siggelkow, N. 2002. Misperceiving interactions among complements and substitutes: Organizational consequences. Management Sci. 48(7) 900–916.

Srinivasan, R., C. Moorman. 2005. Strategic firm commitments and rewards for customer relationship management in online retailing. J. Marketing 69(4) 193–200.

Srinivasan, K., S. Kekre, T. Mukhopadhyay. 1994. Impact of electronic data interchange technology on JIT shipments. Management Sci. 40(10) 1291–1304.

Stieglitz, N., K. Heine. 2007. Innovation and the role of complementarities in a strategic theory of the firm. Strategic Management J. 28(1) 1–15.

Tanriverdi, H. 2006. Performance effects of information technology synergies in multibusiness firms. MIS Quart. 30(1) 57–77.

Thatcher, M. E., D. E. Pingry. 2004. An economic model of product quality and IT value. Inform. Systems Res. 15(3) 268–286.

Tyagi, R. K. 2004. Techonological advances, transaction costs, and consumer welfare. Marketing Sci. 23(3) 335–344

Varian, H. R. 1980. A model of sales. Amer. Econom. Rev. 70(4) 651–659.

Villas-Boas, J. M. 2004. Price cycles in markets with customer recognition. RAND J. Econom. 35(3) 486–501.

Wang, E. T. G., T. Barron, A. Seidman. 1997. Contracting structures for custom software development: The impacts of informational rents and uncertainty on internal development and outsourcing. Management Sci. 43(12) 1726–1744.

Xu, Y., D. Yen, B. Lin, D. Chou. 2002. Adopting customer relationship management technology. Indust. Management Data Systems 102(8–9) 442–452.

ZDNet. 2002. CRM: Dream or nightmare? ZDNet. Accessed May 31, http://techrepublic.com.com/5100-10878-1054704.html.

Zhu, K. 2004. The complementarity of information technology infrastructure and e-commerce capability: A resource-based assessment of their business value. J. MIS 21(1) 167–202.
