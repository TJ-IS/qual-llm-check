---
otero_id: 10974
otero_key: "7SZQCBWP"
title: "A dynamic decision support system to predict the value of customer for new product development"
authors: "S.L. Chan; W.H. Ip"
year: "2011"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.07.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A dynamic decision support system to predict the value of customer for new product development

S.L. Chan ⁎, W.H. Ip

Department of Industrial and Systems Engineering, The Hong Kong Polytechnic University, Hung Hom, Hong Kong

a r t i c l e i n f o

Article history: Received 29 November 2010 Received in revised form 7 June 2011 Accepted 19 July 2011 Available online 28 July 2011

Keywords: Decision support systems New product development Customer relationships Value of customer

## a b s t r a c t

In recent years, <sup>fi</sup>rms have focused on how to enter markets and meet customer requirements by improving product attributes and processes to boost their market share and pro<sup>fi</sup>ts. Consequently, market-driven product design and development has become a popular topic in the literature. However, past research neither covers all of the major in<sup>fl</sup>uencing factors that together drive customers to make purchase decisions, nor connects these various in<sup>fl</sup>uencing factors to customer purchasing behavior. Past studies further fail to take the time value of money and customer value into consideration. This study proposes a decision support system to (a) predict customer purchasing behavior given certain product, customer, and marketing in<sup>fl</sup>uencing factors, and (b) estimate the net customer lifetime value from customer purchasing behavior toward a speci<sup>fi</sup>c product. This will not only enable decision-makers to compare alternatives and select competitive products to launch on the market, but will also improve the understanding of customer behavior toward particular products for the formulation of effective marketing strategies that increase customer loyalty and generate greater pro<sup>fi</sup>ts in the long term. Decision-makers can also make use of the system to build up con<sup>fi</sup>dence in new product development in terms of idea generation and product improvement. The application of the proposed system is illustrated and con<sup>fi</sup>rmed to be sensible and convincing through a case study.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Decisions on new product development are crucial but complex. New product development is regarded as a competitive weapon that helps <sup>fi</sup>rms to survive and succeed in dynamic markets. Lucrative new products play an important role not only in penetrating markets, but also building and retaining customer relationships and yielding pro<sup>fi</sup>ts. However, new product development, from idea creation to product introduction, requires inter-departmental communication among designers, engineers, and marketing personnel. Furthermore, to achieve a competitive edge in a market, sensible decisions must be made about various aspects of new product development, such as product attributes, customer segment, and promotion and marketing strategies. These decisions are inter-linked and will ultimately affect pro<sup>fi</sup>tability. It is challenging to reach a consensus among the various parties involved in product development, who have different responsibilities and concerns. Decision aids such as a decision support system are thus of bene<sup>fi</sup>t in solving such decision problems.

In recent years, many conventional and market-based decision support systems for product design have been developed [1,22,23,29,66]. These highlight the key areas that ought to be considered in making decisions on new product development, including customer requirements, customer satisfaction, market demand, product quality, product design, and pricing. In particular, Gao et al.[20] stated that the timely response to market changes and customer needs becomes one of the competitive advantages. They proposed a novel process model for concurrent product design. Within feature-based part design and process planning, the dynamic change, model reduction, path search and time consumption of concurrent design process are analyzed, which helps improve the overall design process and shorten the product development cycle. However, no decision support system takes all of the key areas into account at the same time. Further, existing systems are insuf<sup>fi</sup>cient and unconvincing in their ability to determine the most lucrative products among alternatives. Some disregard the in<sup>fl</sup>uence of customer behavior and satisfaction, and most fail to take the time value of money into consideration. A new, comprehensive decision support system that overcomes these shortcomings is needed to help <sup>fi</sup>rms make more sensible and reliable decisions on new product development.

In response to this need, this study proposes a decision support system for new product development that consists of two submodels: a customer purchasing behavior (CPB) model and a net customer lifetime value (NCLV) estimation model. The system predicts customer purchasing behavior using a system dynamics approach based on three pieces of information: product attractiveness, customer preferences and satisfaction, and marketing strategy. It also estimates the long-term NCLV based on Markov analysis. This can help managers to determine which product will be most lucrative to launch and the kinds of marketing strategies that should be adopted for the new product. It also helps improve new product development in the future by collating up to date information on market and product attributes.

This section has given the general background to the study. Section 2 discusses the literature on new product development and related decision support systems. The methodology for the development of the proposed decision support system is presented in Section 3. Section 4 introduces the proposed system and discusses its <sup>fi</sup>ndings. Some concluding remarks are offered in Section 5.

## 2. Literature review

## 2.1. Importance of customer relationships in new product development

From the modern management perspective, maximizing customer value is the key to surviving <sup>fi</sup>erce competition in the business world. Hence, many <sup>fi</sup>rms actively engage in developing new products. By delivering value through new products, <sup>fi</sup>rms satisfy customers and generate pro<sup>fi</sup>ts. It has been empirically established that customer satisfaction leads to customer loyalty and, in the long term, to pro<sup>fi</sup>tability [24,45]. It is clear that new products are a crucial driver of customer satisfaction, and that customer satisfaction plays a key role in business sustainability. This suggests that new product development and relationship marketing are associated, especially as customer relationship management is a core relationship marketing tool in the delivery of customer value through products [16]. According to Chan and Li [13], CRM is an effective instrument with which companies can enhance their competitive advantages and improve customer satisfaction and loyalty.

## 2.2. Current approaches to new product development

To survive and succeed in the current business environment, <sup>fi</sup>rms usually focus on several areas to improve their new product development, such as identifying customer needs for continuous new product development [37,40], improving product quality [32,57,58], and accelerating the process of commercialization [40,58,66]. Stanley and War<sup>fi</sup>eld [57] integrated design, engineering, and manufacturing information to provide product information across and beyond the entire enterprise, which extended into the supplier and customer base. Xu et al.[65] applied a polychromatic sets approach to conceptual design. Shu and Wang [55] discussed the key elements of product lifecycle modeling and proposed a framework for it. They also discussed the relationship and evolvement of product models at different stages of the product life cycle. Xu [64] enhanced our awareness of the quality of products and suggested exploring the roles of service-oriented architecture, RFID, agents, work<sup>fl</sup>ow management, and the Internet of Things (IoT) as enablers to improve the value of customer in new product development. Further, numerous decision support systems are available in the literature that aid product classi<sup>fi</sup>cation [43], single product design [6,42,66], product line design [1,30,67], and marketbased product development [1,12,22,23,29,44].

## 2.3. Decision support systems for market-based product development

We discuss decision support systems for market-based product development, because customer requirements are often aligned with new product success, and new product development and relationship marketing issues are inseparable. Although some market-based decision support systems for new product development [1,12,22,23,29,44] consider both design and market information, the in<sup>fl</sup>uencing factors that they include vary widely.

The following three areas, which cover various in<sup>fl</sup>uencing factors, have been identi<sup>fi</sup>ed as signi<sup>fi</sup>cant and requisite in making new product development decisions. However, none of the currently available decision support systems considers all of these areas concurrently.

(a) Product attributes speci<sup>fi</sup>ed by designers [27,66]: the product itself is the major stimulus that in<sup>fl</sup>uences customer affect, cognition, and behavior. Customers may evaluate product attributes in terms of their own values, beliefs, and past experiences when they purchase [56]. However, it is unlikely that customers will make a purchase based on product attributes alone. Their requirements and satisfaction are also vital, as is and marketing competence.

(b) Customer requirements and satisfaction [23,37,40]: capturing the voice of customers is essential in manufacturing products that have a high value for customers. Satisfying customer needs not only enables <sup>fi</sup>rms to build and retain customer relationships successfully, but also encourages positive word of mouth communication among customers, which in turn in<sup>fl</sup>uences market demand.

(c) Marketing competence [17,36]: marketing activities usually serve as a catalyst to make customers recognize products and induce them to purchase. It also in<sup>fl</sup>uences whether the purchase and use of a product is likely to be rewarding [46]. Thus, high-quality marketing campaigns are likely to improve the market share gained from the introduction of new products. Conversely, poor marketing planning and execution have been blamed for the failure of new products [14].

Most current decision support systems help managers select the best new product among alternatives in terms of market share, return maximization, or product development time minimization. However, the measurement of market share or return maximization excludes the time value of money, whereas that of product development time minimization disregards market demand and the effect on customer behavior of relationship marketing. These shortcomings may affect the outcome of new product development.

The shortcomings of existing systems can be overcome by modeling customer purchasing behavior in a way that takes into account the impacts of all of the important areas discussed, and by calculating the NCLV to aid the selection of the best new product to launch. This study proposes a decision support system for new product development that performs these tasks. The system helps managers to understand the managerial aspects of product decision problems and to make appropriate decisions on market-based new product development.

## 3. Study approach

The framework of the proposed decision support system is shown in Fig. 1. The proposed system comprises of two sub-models: a customer purchasing behavior (CPB) model (sub-model 1) and a net customer lifetime value (NCLV) model (sub-model 2).

The proposed system was developed using system dynamics, which is a system modeling and simulation tool. System dynamics is an analytical method for studying feedback systems using casual loop diagrams. It is “a powerful tool to predict behavior and the relative results of a system so as to get helpful suggestions and support decision making” [49]. System dynamics has been extensively employed in strategic planning [21,34,38,53], policy design and analysis [33,52,54], and business decision-making [4,9,10,25]. It helps potential users to gain insight into the dynamic behavior of complex systems and make appropriate decisions [35,59]. The proposed system has the key features of complex systems [48]. It is a dynamic network in which customers are adaptive and their behavior depends on many factors, and its structure involves complex interactions. The proposed system focuses on product, customer, and marketing issues, and new product development decisions in relation to product attributes, marketing planning, and customer behavior are analyzed from a systems perspective. From that perspective, the relationships among components in the system are recognized in line with War<sup>fi</sup>eld [61]. More speci<sup>fi</sup>cally, a system's structural perspective [63] is taken, as the proposed system provides a cohesive structure relating to product, customer, and marketing.

![](/api/attachments/7SZQCBWP/fulltext/images/fa551293f14c8e418cdf71c8bc143c78ecc68a5801828e93da97da536c47a5c9.jpg)  
Fig. 1. Framework of the proposed decision support system.

In sub-model 1 of the proposed system, three types of issues – product, customer, and marketing issues – are assumed to in<sup>fl</sup>uence the dynamic behavior of customers. There are various in<sup>fl</sup>uencing factors under each type of issue. Product issues refer to product attractiveness in terms of performance, quality, design, packaging, and competitiveness. Customer issues include the impact of word of mouth, customer satisfaction, and the relative importance of customer requirements for new products. Marketing issues focus on the effectiveness of marketing for potential customers and re-marketing for active customers. The parameters of the product-related factors are judged by experts in the product development team through a product attractiveness assessment, whereas the parameters of the customer-related factors are established through customer surveys and those of the marketing-related factors are obtained from a <sup>fi</sup>rm's historical marketing data.

After establishing the probable market demand through submodel 1 and examining the <sup>fi</sup>nancial data of the <sup>fi</sup>rm, the NCLV is estimated in sub-model 2 through Markov analysis. The NCLV is the sum of the present value of the future pro<sup>fi</sup>t from lifelong customer relationships. In general, current systems support new product development decision-making based on pro<sup>fi</sup>tability maximization and transaction-based calculations. However, such systems are inaccurate and unreliable because they fail to consider the time value of money and long-term customer relationships. Pursuing lifelong customer relationships is the ultimate goal of many <sup>fi</sup>rms, as it brings greater pro<sup>fi</sup>ts and sustainability [10]. Furthermore, it is more cost-effective to retain existing customers than to acquire new customers [10,51]. Using the NCLV, rather than short-term pro<sup>fi</sup>t maximization and transaction-based calculations, supports decisionmaking on new product development from a long-term perspective. This novel approach should effectively overcome the shortcomings of existing systems.

Based on the results of sub-models 1 and 2, the effectiveness of new product development and marketing plans can be illustrated in monetary terms. This will also inspire <sup>fi</sup>rms to improve long-term pro<sup>fi</sup>ts by adjusting existing new product development and marketing strategies.

## 4. Proposed system for new product development

This section describes the development of the proposed decision support system. The framework of the model and the in<sup>fl</sup>uencing factors included in sub-model 1 are explained, and the details of submodel 2 are then presented.

## 4.1. Sub-model 1: CPB model

Sub-model 1 is shown in Fig. 2. It was developed with the ithink® application, which uses system dynamics. Sub-model 1 includes three groups of customers (potential customers, <sup>fi</sup>rst-time customers, and active customers), and <sup>fi</sup>ve customer states (potential, <sup>fi</sup>rst-time, regular, frequent, and loyal customers). The last three customer states cover active customers. Various factors in<sup>fl</sup>uence customer purchasing behavior. Having no experience of using any of the <sup>fi</sup>rm's products, potential customers initially make a purchase based on “overall product attractiveness” (OPA), “marketing effectiveness” (ME), and “word of mouth” (WOM). The “acquisition rate” (AR) of motivating potential customers to adopt a product initially is determined by Eq. (1). Existing customers, in contrast, have their own experience and satisfaction level of using the <sup>fi</sup>rm's products. They are retained by the <sup>fi</sup>rm based on “OPA” and “WOM” but also “re-marketing effectiveness” (RE), and “overall customer satisfaction” (OCS). The “retention rate” (RR) of upgrading <sup>fi</sup>rst-time customers to active customers and keeping active customers in the company is determined by Eqs. (2)–(5). The factors in<sup>fl</sup>uencing customer purchasing behavior toward a new product are assumed to be independent of each other. The terms used in sub-model 1 are de<sup>fi</sup>ned in Table 1.

$$
A R _ {t} = \text { random } \left[ C _ {1, t} \min \left(E _ {1, t}, E _ {2, t}, E _ {3, t}\right), C _ {1, t} \max \left(E _ {1, t}, E _ {2, t}, E _ {3, t}\right) \right],\tag{1}
$$

$$
R R _ {t} = \sum_ {s = 2} ^ {4} R R _ {s, t},\tag{2}
$$

$$
R R _ {2, t} = \text { random } \left[ C _ {2, t} \min \left(E _ {1, t}, E _ {3, t}, E _ {4, t}, E _ {5, t}\right), C _ {2, t} \max \left(E _ {1, t}, E _ {3, t}, E _ {4, t}, E _ {5, t}\right) \right],\tag{3}
$$

$$
R R _ {3, t} = \text { random } \left[ C _ {3, t} \min \left(E _ {1, t}, E _ {3, t}, E _ {4, t}, E _ {5, t}\right), C _ {3, t} \max \left(E _ {1, t}, E _ {3, t}, E _ {4, t}, E _ {5, t}\right) \right],\tag{4}
$$

$$
R R _ {4, t} = \text { random } \left[ C _ {4, t} \min \left(E _ {1, t}, E _ {4, t}, E _ {5, t}\right), C _ {4, t} \max \left(E _ {1, t}, E _ {4, t}, E _ {5, t}\right) \right],\tag{5}
$$

![](/api/attachments/7SZQCBWP/fulltext/images/1d1205de68df8fd02db274f3999fe1ac49b7c2cfcc5e70638126f3130f6830e6.jpg)  
Fig. 2. Sub-model 1: CPB model.

where $C _ { s , t }$ denotes the number of customers in state (s) at time (t), in which s=1, 2, 3, 4, 5 represent the <sup>fi</sup>ve customer states of potential, <sup>fi</sup>rst-time, regular, frequent, and loyal customers, respectively; E refers to the parameters of the <sup>fi</sup>ve in<sup>fl</sup>uencing factors of customer purchasing behavior at t, in which n=1, 2, 3, 4, 5 represent “OPA,” “ME,” “WOM,” “RE,” and “OCS,” respectively; and $R R _ { s , t }$ refers to the “RR” of customers at $s = 2 , 3 ,$ , 4 at time t moving on to the next state.

## 4.1.1. Product influencing factors

Overall product attractiveness (OPA) is the main stimulus in<sup>fl</sup>uencing consumer affect, cognition, and behavior. Consumers may evaluate product attributes based on their own values, beliefs, and past experiences in making a purchase [56]. OPA is often assessed in terms of design, quality, performance, packaging, and competitiveness. For each dimension of OPA, there are two determinants: the attractiveness of product attributes according to experts in the company, and the relative importance of different customer requirements. Including both determinants gives a more comprehensive assessment of new product attractiveness.

The attractiveness of product attributes (in terms of design, quality, performance, packaging, and competitiveness) is a key determinant of OPA and hence customer purchase behavior. These parameters are determined internally, often by senior management and the new product development team. However, customer preferences are critical to product selection, and thus the relative importance of different customer requirements (including design, quality, performance importance, packaging, and competitiveness) is another determinant of OPA and customer purchasing behavior. These parameters can be obtained through customer surveys and analyzed using a fuzzy analytic hierarchy process. OPA is expressed mathematically by Eq. (6).

$$
E _ {1, t} = \sum_ {f = 1} ^ {5} I _ {f, t} A _ {f, t},\tag{6}
$$

where f=1, 2, 3, 4, 5 refers to “design,” “quality,” “performance,” “packaging,” and “competitiveness,” respectively; $I _ { f , t }$ denotes the parameters of the relative importance of customer requirements in terms of f at t; and $A _ { f , t }$ indicates the parameters of product attractiveness in terms of f at t.

## 4.1.2. Customer influencing factors

It is unlikely that customers make purchase decisions based on product attributes alone. Word of mouth (WOM) and overall customer satisfaction (OCS) are other important factors affecting customer purchasing behavior.

WOM refers to the likelihood of customers sharing with others their impressions and recommendations of their experiences in using a product [46]. Marketing planners generally try to encourage positive WOM communication among consumers, as this helps to spread awareness of the introduction of new products [7]. According to the advertising agency JWT Worldwide, over 85% of the top 1000 marketing <sup>fi</sup>rms now use WOM tactics [62]. According to Arndt [5], exposure to favorable WOM increases the pro<sup>fi</sup>tability of a purchase, and vice versa. WOM clearly merits attention when making new product development and relationship marketing decisions, and is thus regarded as a customer in<sup>fl</sup>uencing factor in the customer purchasing behavior in sub-model 1.

WOM is closely connected with OCS. It is usual for customers to share their views on a product in their social network based on their level of satisfaction in purchasing and using the product. Satis<sup>fi</sup>ed customers share positive WOM, whereas dissatis<sup>fi</sup>ed customers engage in negative WOM communication with others. Many studies have found that WOM and customer satisfaction are positively related, and that both are powerful factors in<sup>fl</sup>uencing customer purchasing behavior [2,19,50,60]. OCS is thus considered to be a determinant of WOM. Given the parameter for OCS, the parameter for WOM can be determined through a graphical function (see Fig. 3), rather than an equation. A positive WOM parameter means that customers share favorable comments about the product, which encourages customers to make a (re)purchase, and vice versa.

OCS, another in<sup>fl</sup>uencing factor included in sub-model 1, in-<sup>fl</sup>uences the likelihood of customers engaging in WOM, and also encourages <sup>fi</sup>rst-time customers to purchase and active customers to repurchase. Customers with a higher satisfaction level often have a stronger intention to repurchase and to be loyal. Several studies have found that a higher level of customer satisfaction leads to greater customer loyalty [3,19,50]. Thus, in sub-model 1 OCS is considered to in<sup>fl</sup>uence WOM and also RR. The OCS parameter can be obtained through a customer survey.

Terminology used in sub-model 1.

<table><tr><td>Terms</td><td>Implications</td></tr><tr><td>Potential customers</td><td>Target customers who will probably make a purchase</td></tr><tr><td>First-time customers</td><td>Customers who make an initial purchase of a newly launched product</td></tr><tr><td>Active customers</td><td>Customers who make repeat purchases of a product and are regular, frequent, or loyal customers</td></tr><tr><td>Overall product attractiveness (OPA)</td><td>Product design, quality, performance, packaging, and competitiveness, all of which stimulate customers to make purchases</td></tr><tr><td>Word of mouth (WOM)</td><td>Likelihood of customers sharing their impressions and recommendations of their experience of using the product with others</td></tr><tr><td>Overall customer satisfaction (OCS)</td><td>Level of customer satisfaction with the product based on personal experience and perceptions of using the product after purchase</td></tr><tr><td>Marketing effectiveness (ME)</td><td>The effectiveness of a firm&#x27;s activities to acquire customers from among the public, such as advertisements</td></tr><tr><td>Re-marketing effectiveness (RE)</td><td>The effectiveness of a firm&#x27;s activities to retain customers, such as a membership program</td></tr><tr><td>Marketing approach (MA)</td><td>The marketing strategy adopted by the firm, whether an individual marketing campaign or a mixed marketing plan</td></tr><tr><td>Re-marketing approach (RA)</td><td>The re-marketing strategy adopted by the firm, whether an individual re-marketing campaign or a mixed re-marketing plan</td></tr><tr><td>Attractiveness of product design, quality, performance, packaging, and competitiveness</td><td>Scores that the product achieves for design, quality, performance, packaging, and competitiveness as rated by senior management and the new product development team</td></tr><tr><td>Design, quality, performance, packaging, and competitiveness importance</td><td>The importance of customer preferences in evaluating a product (in terms of product design, quality, performance, packaging, and competitiveness) and deciding whether to purchase it (i.e., the weights of customer requirements)</td></tr></table>

## 4.1.3. Marketing influencing factors

It is critical for <sup>fi</sup>rms to launch new products successfully to maintain market leadership. Unfortunately, empirical data indicates that one-third to one-half of all new products fail to meet the <sup>fi</sup>rm's <sup>fi</sup>nancial and marketing goals [8,15,39]. Poor marketing planning and execution is offered as a possible explanation [14]. Marketing information also in<sup>fl</sup>uences whether the purchase and use of a product is likely to be rewarding [46]. It is clear that marketing factors and customer purchasing behavior are linked, and are key to product success. “Marketing effectiveness” (ME) and “re-marketing effectiveness” (RE) are thus included in the sub-model 1 as marketing factors in<sup>fl</sup>uencing customer purchasing behavior.

![](/api/attachments/7SZQCBWP/fulltext/images/0902f1cf1ba5becb17046c6d20aec7f95677505e3a87fb385d70d8b9b99b5599.jpg)  
Fig. 3. Graphical function of WOM versus OCS.

There are many possible forms of (re)marketing campaigns, such as advertising, sales promotions, event sponsoring, and membership programs. Firms often use mixed (re)marketing campaigns as a strategy. In general, marketing campaigns that are effective in conveying messages about a <sup>fi</sup>rm's product to its target customers are more valuable. However, (re)marketing budgets are often limited, and <sup>fi</sup>rms have to leverage the budget and effectiveness of marketing for new products. Three types of marketing approach (MA) (i.e., MA1, MA2, and MA3) and three types of re-marketing approach (RA) (i.e., RA1, RA2, and RA3) de<sup>fi</sup>ned according to the size of budget (i.e., small, medium, and large, respectively) are available as options in submodel 1. The relationship between the marketing approaches and ME is expressed in Eqs. (7)–(8), and the relationship between the remarketing approaches and RE is stated in Eqs. (9)–(10).

$$
E _ {2, t} = \sum_ {x = 1} ^ {3} M _ {x, t} X _ {x, t},\tag{7}
$$

$$
M _ {x, t} = \left\{ \begin{array}{l l} 1 & , i f x i s a d o p t e d \\ 0 & , o t h e r w i s e, \end{array} \right.\tag{8}
$$

$$
E _ {4, t} = \sum_ {y = 1} ^ {3} R _ {y, t} Y _ {y, t},\tag{9}
$$

$$
R _ {y, t} = \left\{ \begin{array}{l l} 1 & , i f y i s a d o p t e d \\ 0 & , o t h e r w i s e, \end{array} \right.\tag{10}
$$

where $M _ { x , t }$ represents whether marketing approach x is adopted at time t; $X _ { x , t }$ refers to the respective effectiveness value of marketing approach x at time t; x=1, 2, 3 refers to MA1, MA2, and MA3, respectively; $R _ { y , t }$ represents whether re-marketing approach y is adopted at time t; $Y _ { y , t }$ refers to the respective effectiveness value of remarketing approach y at time t; and y=1, 2, 3 refers to RA1, RA2, and RA3, respectively.

## 4.1.4. Prediction of customer purchasing behavior

Based on the aforementioned in<sup>fl</sup>uencing factors, the number of potential, <sup>fi</sup>rst-time, and active customers can be predicted by Eqs. (11)–(14).

$$
C _ {1, t} = C _ {1, t - d t} + \left(\sum_ {s = 3} ^ {5} L R _ {s, t} - A R _ {1, t}\right) d t,\tag{11}
$$

$$
C _ {2, t} = C _ {2, t - d t} + \left(A R _ {1, t} - \sum_ {s = 2} ^ {4} R R _ {s, t}\right) d t,\tag{12}
$$

$$
C _ {3 - 5, t} = \sum_ {s = 3} ^ {5} C _ {s, t - d t} + \left(\sum_ {s = 2} ^ {4} R R _ {s, t} - \sum_ {s = 3} ^ {5} L R _ {s, t}\right) d t,\tag{13}
$$

$$
L R _ {s, t} = \left\{ \begin{array}{l l} C _ {s, t} Z _ {s, 1} & , i f E _ {5, t} \geq 0. 7 5 \\ C _ {s, t} Z _ {s, 2} & , i f E _ {5, t} <   0. 5, \\ C _ {s, t} Z _ {s, 3} & , o t h e r w i s e \end{array} \right.\tag{14}
$$

where $L R _ { s , t }$ indicates the “loss rate” of customers at s = 3, 4, 5 at time t; $Z _ { s , z }$ refers to the fraction of leaving customers at s=3, 4, 5 that are subject to the conditions $z = 1 , 2 , 3 ;$ and $z = 1 , 2 , 3$ represents $E _ { 5 , t } 2 0 . 7 5$ , and $E _ { 5 , t } { < } 0 . 5$ otherwise.

To make sub-model 1 effective and operative in assessing the extent of the in<sup>fl</sup>uencing factors and overall customer satisfaction (OCS) and supporting decision-making about new product development, we make good use of slider input devices. Such devices help decision-makers input and update the parameters for the various factors and determinants more easily. A chained switch is also applied to the set of marketing approach (MA) and re-marketing approach (RA) options in Eqs. (8) and (10), respectively. Decision-makers can select the desired MA and RA option by simply turning on the option in the respective chain with one-click, which causes the other options to be turned off. The interface layer for the sub-model is shown in Fig. 4.

## 4.2. Sub-model 2: NCLV estimation model

The net customer lifetime value (NCLV) is de<sup>fi</sup>ned as the sum of the current lifetime values of all customers, where customer lifetime value refers to the present value of future pro<sup>fi</sup>t from a customer. A consensus has been reached by many scholars that customers are not equally pro<sup>fi</sup>table [11,26,47], and that building long-term customer loyalty is crucial to business sustainability [28,31,41]. Differentiating more pro<sup>fi</sup>table customers from less pro<sup>fi</sup>table customers and focusing on lifelong, rather than short-term, customer relationships are key business strategies for survival in today's competitive marketplace. The NCLV is applied in this study to make this differentiation.

Sub-model 2 applies a Markov chain to estimate the NCLV based on the outputs of sub-model 1, which represent the probability of customers switching states over time. Our case study shows that customers can only be in one of the <sup>fi</sup>ve customer states of potential, <sup>fi</sup>rst-time regular, frequent, and loyal customers. Hence, customer switching behavior forms a $5 \times 5$ probability matrix, P, along with the earning vector, E. Eq. (15) is applied to calculate the NCLV.

$$
P = \left[ \begin{array}{c c c c c} 1 - p _ {1} & p _ {1} & 0 & 0 & 0 \\ 1 - p _ {2} & 0 & p _ {2} & 0 & 0 \\ 1 - p _ {3} & 0 & 0 & p _ {3} & 0 \\ 1 - p _ {4} & 0 & 0 & 0 & p _ {4} \\ 0 & 0 & 0 & 0 & 1 \end{array} \right]; E = \left[ \begin{array}{c} R P - M C \\ - R C \\ - R C \\ - R C \\ 0 \end{array} \right]
$$

$$
N C L V = \sum_ {s = 1} ^ {5} \sum_ {t = 0} ^ {T} P ^ {t} E (1 + D) ^ {- t} - C S\tag{15}
$$

where $p _ { 1 }$ is the probability of customers switching from the current state $( \mathrm { i } . \mathrm { e } . , s = 1 )$ to the next state $( \mathrm { i } . \mathrm { e } . , s = 2 )$ , which is also applied to explain p , p , p ; $R P$ refers to the retail price of a product; MC is the marketing cost; RC is the re-marketing cost; CS is the cost of the goods sold; $P ^ { t }$ is the switching probability at time t; and D is the discount rate. As mentioned, the outputs of sub-model 1 serve as the inputs of sub-model 2. Hence, $p _ { 1 }$ is equivalent to $A R _ { t = 0 }$ divided by the initial number of potential customers; $p _ { 2 }$ equals $R R _ { 2 , t = 1 }$ divided by $C _ { 2 , t = 0 } ;$ $p _ { 3 }$ equals $R R _ { 3 , t = 2 }$ divided by $C _ { 3 , t = 1 } ;$ and $p _ { 4 }$ is equivalent to $R R _ { 4 , t = 3 }$ divided by $C _ { 4 , t = 2 } .$

## 5. Application to the power tools industry

The application of the proposed system is illustrated and veri<sup>fi</sup>ed through a case study. A brief description of the case company and data is given, and the proposed model is then estimated and evaluated.

![](/api/attachments/7SZQCBWP/fulltext/images/8ddc85adab2ee9ef84c10835e98331f64c5600a49ce8ea4b691721a8ffb4d6db.jpg)  
Fig. 4. Interface layer of sub-model 1.

## 5.1. Company and data

The case company is a world-class leader in innovative electrical products with a high value and powerful brands. Its products are marketed to both the construction industry and individual households worldwide. It launched over 300 new products in 2009, which drove over one third of sales. With a strategic focus on cutting-edge products and sophisticated marketing plans, the company is successful in its market, and reported a strong net pro<sup>fi</sup>t growth of 180.7% in 2009.

The company possesses a data warehouse. Data on product attributes, customer satisfaction and behavior, marketing plans and signi<sup>fi</sup>cance, and <sup>fi</sup>nancial information from the warehouse are used in this study. Seven power tools (Products A–G) in the same product family are randomly chosen as representative samples. Due to con<sup>fi</sup>dentiality, all of the actual data, excluding retail prices and discount rates, are concealed, but their parameters are displayed in Table 2. The cost of goods sold and the marketing and re-marketing costs are neither displayed nor converted to parameters due to data con<sup>fi</sup>dentiality. The data are applied to the proposed system for simulation, to calculate the NCLV, and to calculate the original CLV using the Eq. (16) without using the proposed system.

$$
C L V = \sum_ {t = 0} (R P _ {t} - M C _ {t}) (1 + D) ^ {- t} + \sum_ {t = 1} ^ {T} (R P _ {t} - R C _ {t}) (1 + D) ^ {- t} - C S.\tag{16}
$$

## 5.2. Discussion of the results of sub-model 1

By running sub-model 1 with the parameters shown in Table 2, the customer purchasing behavior toward Products A–G is predicated.

Table 2  
Input parameters for the proposed system.

<table><tr><td>Product</td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td></tr><tr><td colspan="8">Parameters for sub-model 1:</td></tr><tr><td>Attractiveness of product performance</td><td>0.375</td><td>0.375</td><td>0.25</td><td>0</td><td>0.375</td><td>0.875</td><td>1</td></tr><tr><td>Attractiveness of product quality</td><td>0.4583</td><td>0.4583</td><td>0.5417</td><td>0.4583</td><td>0.7083</td><td>0.4583</td><td>0.4583</td></tr><tr><td>Attractiveness of product design</td><td>0.5625</td><td>0.5</td><td>0.4688</td><td>0.625</td><td>0.5313</td><td>0.4375</td><td>0.3125</td></tr><tr><td>Attractiveness of product packaging</td><td>1</td><td>1</td><td>0.75</td><td>0.5</td><td>0.75</td><td>0.75</td><td>0.75</td></tr><tr><td>Attractiveness of product competitiveness</td><td>0.5</td><td>0.5</td><td>0.5</td><td>0.5833</td><td>0.5</td><td>0.5</td><td>0.5</td></tr><tr><td>Marketing approach option</td><td>2</td><td>2</td><td>1</td><td>1</td><td>2</td><td>3</td><td>3</td></tr><tr><td>Re-marketing approach option</td><td>3</td><td>2</td><td>2</td><td>2</td><td>1</td><td>2</td><td>2</td></tr><tr><td>Importance of performance</td><td></td><td></td><td></td><td>0.6867</td><td></td><td></td><td></td></tr><tr><td>Importance of quality</td><td></td><td></td><td></td><td>0.3038</td><td></td><td></td><td></td></tr><tr><td>Importance of design</td><td></td><td></td><td></td><td>0.1514</td><td></td><td></td><td></td></tr><tr><td>Importance of packaging</td><td></td><td></td><td></td><td>0.1246</td><td></td><td></td><td></td></tr><tr><td>Importance of competitiveness</td><td></td><td></td><td></td><td>0.1515</td><td></td><td></td><td></td></tr><tr><td>Overall customer satisfaction</td><td></td><td></td><td></td><td>0.83</td><td></td><td></td><td></td></tr><tr><td colspan="8">Parameters for sub-model 2:</td></tr><tr><td>Retail price (USD)</td><td>$336</td><td>$361</td><td>$149</td><td>$139</td><td>$299</td><td>$349</td><td>$339</td></tr><tr><td>Discount rate</td><td></td><td></td><td></td><td>10.9%</td><td></td><td></td><td></td></tr></table>

Table 3  
Results of the proposed system

<table><tr><td>Product</td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td></tr><tr><td colspan="8">Outputs from sub-model 1:</td></tr><tr><td> $p_{1}$ </td><td>0.44</td><td>0.36</td><td>0.29</td><td>0.31</td><td>0.33</td><td>0.33</td><td>0.37</td></tr><tr><td> $p_{2}$ </td><td>0.39</td><td>0.44</td><td>0.48</td><td>0.5</td><td>0.49</td><td>0.64</td><td>0.38</td></tr><tr><td> $p_{3}$ </td><td>0.48</td><td>0.56</td><td>0.68</td><td>0.68</td><td>0.53</td><td>0.76</td><td>0.53</td></tr><tr><td> $p_{4}$ </td><td>0.43</td><td>0.62</td><td>0.36</td><td>0.34</td><td>0.17</td><td>0.04</td><td>0.48</td></tr><tr><td colspan="8">Outputs from sub-model 2:</td></tr><tr><td>NCLV (USD)</td><td>$866.8</td><td>$997.7</td><td>$370.5</td><td>$333.5</td><td>$690.9</td><td>$868.6</td><td>$837.2</td></tr><tr><td>NCLV in order</td><td>3</td><td>1</td><td>6</td><td>7</td><td>5</td><td>2</td><td>4</td></tr></table>

The customer switching probabilities $( \mathrm { i . e . , ~ } p _ { 1 } , ~ p _ { 2 } , ~ p _ { 3 } ,$ and $p _ { 4 } )$ are estimated and presented in Table 3. The migration of customers from the state of potential customers to that of active customers is shown in Fig. 5, which shows the number of customers against time.

Table 3 shows that the customer switching probabilities vary across products and time. Customers often behave in a different way toward products with speci<sup>fi</sup>c attributes under the impact of (re)marketing campaigns. With reference to Products F and G, the company invested in the same kind of (re)marketing campaigns to introduce them into the market. However, the customer switching probabilities of Products F and G differ, and show no common trend. This demonstrates that customer purchasing behavior depends not only on marketing in<sup>fl</sup>uencing factors, but also product and customer in<sup>fl</sup>uencing factors. Furthermore, customer purchasing behavior is dynamic.

Although the results in Table 3 perhaps show no speci<sup>fi</sup>c trend in customer switching probabilities, the results in Fig. 5 suggest that there is a pattern to customer purchasing behavior toward Products $\mathsf { A } { - } \mathsf { G } .$ The movement of potential and active customers follows an Sshaped curve, whereas that of <sup>fi</sup>rst-time customers follows a bellshaped curve. Fig. 5 infers that the company is unlikely to acquire all target customers, and that it is most important to motivate <sup>fi</sup>rst-time customers to become active customers and retain active customers in the long term. The acquisition cost of new customers exceeds the cost of retaining existing customers by a substantial margin [18]. Customer loyalty is thus important for the company to sustain growth and maximize pro<sup>fi</sup>ts.

According to Fig. 5, and taking Product E as an example, the number of <sup>fi</sup>rst-time customers continues to grow in the <sup>fi</sup>rst 1.75 years but starts to decline thereafter. The <sup>fi</sup>gure also demonstrates that potential customers are active in purchasing and then switch to the state of <sup>fi</sup>rst-time customers during the <sup>fi</sup>rst 1.75 years due to their initial purchase. It is thus more effective for the company to promote the product during this period to capture more customer value. Mass marketing campaigns, such as advertising/publicity, trade shows and events, mass media, and online marketing are likely to be most suitable here. After customers have been acquired, greater emphasis should be placed on customer retention. Re-marketing to <sup>fi</sup>rst-time and active customers after the <sup>fi</sup>rst 1.75 years following the introduction of Product E is essential to achieve market sustainability. Membership programs, face-to-face marketing activities, and privilege offers are likely to be particularly effective after the <sup>fi</sup>rst 1.75 years and up to the fourth year.

Fig. 5 further shows that the number of active customers of Products A–G reaches a peak and remains steady thereafter. This implies that the target market segment is saturated and the products launched have already ful<sup>fi</sup>lled customer needs. In this circumstance, customers are neither interested in the products nor intend to purchase them further. Armed with knowledge of this customer migration (see Fig. 5), the company can anticipate when a new product should be launched to prolong the relationship with its customers. For example, the number of customers of Product B in the target segment approaches the maximum after 4.375 years after product introduction (see Fig. 5). This is then the optimal time for the company to launch another new product to expand its market reach and further satisfy customer needs.

![](/api/attachments/7SZQCBWP/fulltext/images/96276d423825a8a90025ff37eab22c9537ed957b71caa96ecb11440b496da439.jpg)

![](/api/attachments/7SZQCBWP/fulltext/images/6281d119fd9e5df6eb75966a6f912a68a5aea67942f732f961ad9aa3e80806e1.jpg)

![](/api/attachments/7SZQCBWP/fulltext/images/a7b63783d80d74876621ff1352a2de58b53d4cc6ab7d629b4f89301d102fdf57.jpg)

![](/api/attachments/7SZQCBWP/fulltext/images/6caecf99c58b630d47f310cc8925688ee7d454adfda269ce8f9ee8e0eb25765b.jpg)

![](/api/attachments/7SZQCBWP/fulltext/images/a1845fe928ca0d5fee5ebb6250aa6027b8bf06ed65bc469417eefe4b0d65b60b.jpg)

![](/api/attachments/7SZQCBWP/fulltext/images/400a2771b1d60eefba42752acc808ab6773b99248fc24fd892b1e484460ca9bd.jpg)

![](/api/attachments/7SZQCBWP/fulltext/images/de6b4bc242f4dd7218a229d0c11a385e3d740975711c38ca8f63c689c670fb83.jpg)  
Fig. 5. Customer purchasing behavior toward Products A–G.

## 5.3. Discussion of the results of sub-model 2

To predict the net customer lifetime value (NCLV) for Products A–G, the probabilities that result from the sub-model 1 are used as inputs into the probability matrix P in sub-model 2. The predicted probabilities are combined with information on retail price, marketing cost, remarketing cost, and discount rate to determine the NCLV for Products A–G over four periods (see Table 3). To verify the proposed system, the original customer lifetime value (CLV) of each product is estimated using Eq. (16). The results of the original CLV and the difference between the CLV and NCLV for each product are shown in Table 4.

Table 4  
Comparison of NCLVs with the original CLVs.

<table><tr><td>Product</td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td></tr><tr><td>NCLV (USD)</td><td>$866.8</td><td>$997.7</td><td>$370.5</td><td>$333.5</td><td>$690.9</td><td>$868.6</td><td>$837.2</td></tr><tr><td>Original CLV (USD)</td><td>$889.6</td><td>$1013.3</td><td>$378.7</td><td>$349.0</td><td>$713.7</td><td>$879.1</td><td>$871.8</td></tr><tr><td>Original CLV in order</td><td>2</td><td>1</td><td>6</td><td>7</td><td>5</td><td>3</td><td>4</td></tr><tr><td>Difference</td><td>2.56%</td><td>1.54%</td><td>2.17%</td><td>4.44%</td><td>3.19%</td><td>1.19%</td><td>3.97%</td></tr><tr><td>Profitability in order</td><td>3</td><td>1</td><td>6</td><td>7</td><td>5</td><td>2</td><td>4</td></tr></table>

By prioritizing the NCLVs for Products A–G in Table 4, it becomes clear that in a long-term customer relationship Product B is the most pro<sup>fi</sup>table product (NCLV= \$997.7) and Product D is the least pro<sup>fi</sup>table (NCLV=\$333.5). The results in Table 3, Table 4, and Fig. 5 indicate that there is no obvious evidence to indicate which in<sup>fl</sup>uencing factor drives Product B to be relatively more favorable, or to explain why Product B is the most pro<sup>fi</sup>table and Product D the least. This <sup>fi</sup>nding implies that customer purchasing behavior is based on a combination of the various in<sup>fl</sup>uencing factors, rather than any one factor alone.

It is not necessarily the case that a product that initially has a higher probability of motivating potential customers to purchase is the most pro<sup>fi</sup>table in the long term, and vice versa. For example, the probability of potential customers buying Product A is 0.44 (see Table 3), which is the highest among the various alternatives. However, the NCLV for Product A is \$866.8 (see Table 3), which ranks third, showing that it is not the most pro<sup>fi</sup>table product. This suggests that the company should place emphasis not only on customer acquisition but also on customer retention and loyalty. The amount of pro<sup>fi</sup>t derived from the customer relationship is attributable to the degree of customer loyalty and the length of the customer relationship, rather than the rate of customer acquisition. Clearly, securing lifelong customer relationships is the key to product success and greater pro<sup>fi</sup>ts for the company.

Table 4 demonstrates that the differences between the original CLVs and NCLVs range from 1.19% to 4.44%, which are considered minor and acceptable. This further implies that the proposed system is reliable and sensible at a 95% signi<sup>fi</sup>cance level. However, the order of the NCLVs for Products A–G differs slightly from that of the original CLVs. This may affect how decision-makers sift through the product alternatives to <sup>fi</sup>nd the relatively more favorable products that will generate greater pro<sup>fi</sup>ts. To further verify the precision of the proposed system and explore this issue, additional data on the pro<sup>fi</sup>tability of Products A–G are acquired from the case company (see Table 4). The information shows that the order of Products A–G in terms of pro<sup>fi</sup>tability is identical to that of the NCLVs. This further con<sup>fi</sup>rms that the proposed system is precise and accurate in determining the NCLV and prioritizing products.

Compared with the NCLVs, the original CLVs are inaccurate and overestimated. This is possibly because the calculation fails to consider customer purchasing behavior speci<sup>fi</sup>cally in terms of the customer switching probability. In contrast, the insight into customer purchasing behavior obtained from the NCLVs could play an important part in helping <sup>fi</sup>rms to make appropriate decisions on new product development and relationship marketing. This further adds value to the proposed system.

## 5.4. Implications

It is challenging for <sup>fi</sup>rms to respond to customer needs in today's competitive marketplace due to rapid technological advancement and volatile demand. Customer purchasing behavior is dynamic. Simply observing historical customer purchasing behavior is ineffective in supporting new product development decisions. Furthermore, decisions on new product development are complicated, and require knowledge about the product, its customers, and marketing and communication between multiple departments. Sub-model 1 of the proposed system is a dynamic feedback system capable of helping a <sup>fi</sup>rm to integrate product, customer, and marketing information through simulation to analyze and predict customer purchasing behavior. Submodel 1 is designed to enable decision-makers to input and update parameters to make decisions in a fast and ef<sup>fi</sup>cient manner. By gaining insight into customer purchasing behavior, a <sup>fi</sup>rm can make future plans for new product development and formulate proper marketing strategies. Sub-model 1 offers signi<sup>fi</sup>cant support for decisions on new product development and relationship marketing.

In the literature, pro<sup>fi</sup>t maximization is normally used as the basis for the selection of new products among alternatives. Pro<sup>fi</sup>t is generally calculated in the short term using historical or current data, which may be inaccurate or out of date. This may lead a <sup>fi</sup>rm to introduce less lucrative and even unfavorable products into the market, which will negatively affect its market share and pro<sup>fi</sup>tability. To take long-term pro<sup>fi</sup>t into account, we estimate the NCLV in submodel 2 by making use of the outputs from sub-model 1. The NCLV is useful in distinguishing the best product and for prioritizing products in terms of their long-term pro<sup>fi</sup>tability. This allows a <sup>fi</sup>rm to select relatively more favorable and lucrative products for market launch to generate greater pro<sup>fi</sup>t in the long term.

Overall, the proposed decision support system is signi<sup>fi</sup>cant and valuable. It helps <sup>fi</sup>rms to (a) respond to customer needs by designing and developing new products that are market-driven; (b) stimulate customers to make (re)purchases by formulating proper marketing strategies; and (c) sustain business growth and pro<sup>fi</sup>tability through the selection and launch of rewarding products. Firms can easily evaluate different marketing approaches and new product ideas using the system by altering the input values of the model. This will help them to forecast the long-term return on investment of tentative business strategies and identify improvements to new product ideas and (re)marketing approaches.

## 6. Conclusions and future research

A decision support system for new product development and relationship marketing is proposed that focuses on the modeling of customer purchasing behavior and the NCLV. The proposed system consists of a CPB model (sub-model 1) and an NCLV estimation model (sub-model 2). The structure and formulation of these two sub-models are described. The applicability of the system is veri<sup>fi</sup>ed by applying it to seven power tools products from the same company. The implications of using the proposed system are explored, and it is concluded that the system offers effective decision support by predicting the customer switching probability and determining the NCLV for products. The results show that it is convincing and accurate, and should help companies to develop competitive new products and relationship marketing strategies that increase business growth and sustainability.

The system proposed in this study is not used to assess the individual impacts of the various in<sup>fl</sup>uencing factors on product success or conduct a sensitivity analysis of product, customer, and marketing factors. However, it could certainly be extended in the future to these areas. We apply the system to the power tool industry to test its applicability, but it would be of interest to implement it in other industries. Future research could conduct case studies in a range of different industries to test the system's capability or make customizations if necessary.

## Acknowledgments

The authors would like to express their sincere thanks to the Hong Kong Polytechnic University for its <sup>fi</sup>nancial support of this research work under project number RPV2.

## References

[1] G. Alexouda, A user-friendly marketing decision support system for the product line design using evolutionary algorithms, Decision Support Systems 38 (2005) 495–509.

[2] E. Anderson, Customer satisfaction and word of mouth, Journal of Service Research 1 (1)(1998) 5–17.

[3] E.W. Anderson, M. Sullivan, The antecedents and consequences of customer satisfaction for <sup>fi</sup>rms, Marketing Science 12 (2) (1993) 125–143.

[4] B.J. Angerhofer, M.C. Angelides, System dynamics modeling in supply chain management: research review, Proceedings of the 32nd conference on Winter Simulation, Orlando, Florida, 2000, pp. 342–351.

[5] J. Arndt, Product-based conversations in the diffusion of new products, Journal of Marketing Research (1968) 291–295.

[6] P.V. Balakrishnan, V.S. Jacob, Triangulation in decision support systems: algorithms for product design, Decision Support Systems 14 (4) (1995) 313–327

[7] B.L. Bayus, Word of mouth: the indirect effects of marketing efforts, Journal of Advertising Research, June–July, 1985 31–39.

[8] A. Booz, A. Allen, A. Hamilton, New Product Management for the 1980's, Booz, Allen and Hamilton, New York, 1982.

[9] S.L. Chan, W.H. Ip, A Markov chain repurchasing model for CRM using system dynamics, Proceeding of the IASTED International Conference on Modelling and Simulation (MS 2008), 2008, Paper No.: 620–038.

[10] S.L. Chan, W.H. Ip, V. Cho, A model for predicting customer value from perspectives of product attractiveness and marketing strategy, Expert Systems with Applications 37 (2010) 1207–1215.

[11] B. Chen, W.H. Ip, Y.B. Zhou, B. Liang, H.L. Yu, The design of a lean CRM software process model, Proceedings of the Fourth International Conference on Electronic Business — shaping business strategy in a networked world, Tsinghua University, Beijing, 2001, pp. 335–339.

[12] C.H. Chen, L.P. Khoo, W. Yan, Web-enabled customer-oriented product concept formation via laddering technique and Kohonen association, Concurrent Engineering 10 (2002) 299–310.

[13] Y. Chen, L. Li, Deriving information from CRM for knowledge management — a note on a commercial bank, Systems Research and Behavioral Science 23 (2) (2006) 141–146.

[14] M.J. Cooper, An evaluation system for project selection, Research Management 21 (1979) 29–33.

[15] R.G. Cooper, E. Kleinschmidt, Uncovering the keys to new product success, IEEE Engineering Management Review 21 (Winter 1993) 5–18.

[16] C. Cronroos, Service Management and Marketing: A Customer Relationship Management Approach, John Wiley & Sons New York 2000

[17] U. De Brenetani, C. Droge, Determinants of the new product screening decision: a structural model analysis, International Journal of Research in Marketing 5 (2) (1988) 91–106.

[18] J. Dyche, CRM Handbook: The Business Guide to Customer Relationship Management, Addison Wesley, Boston, 2002.

[19] K.M. File, R.A. Prince, Positive Word-of-Mouth: customer satisfaction and buyer behavior, International Journal of Bank Marketing 10 (1) (1993) 25–29.

[20] X. Gao, Z. Li, L. Li, A process model for concurrent design in manufacturing enterprise information systems, Enterprise Information Systems 2 (1) (2008) 33–46.

[21] N.C. Georgantzas, Reengineering business process reengineering with system dynamics, Proceedings of the 14th International Conference of the System Dynamics Society. Cambridge, Massachusetts, USA, 1996.

[22] J.A. Harding, K. Popplewell, R.Y.K. Fung, A.R. Omar, An intelligent information framework relating customer requirements and product characteristics, Computers in Industry 44 (2001) 51–65

[23] A. Herrmann, F. Huber, C. Braunstein, Market-driven product and service design: Bridging the gap between customer needs, quality management, and customer satisfaction, International Journal of Production Economics 66 (2000) 77–96.

[24] J.L. Heskett, W.E. Jr. Sasser, and L.A. Schlesinger, Putting the service-pro<sup>fi</sup>t chain to work. Harvard Business Review, Mar-Apr, (1994), 164–174.

[25] W.H. Ip, B.C. Chen, C.W. Lau, K.L. Choy, S.L. Chan, Modelling a CRM Markov chain process using system dynamics, International Journal of Value Chain Management 2 (3) (2008) 420–435.

[26] W.H. Ip, B.C. Chen, H.C.W. Lau, B. Liang, A functional framework for integrating eCRM with work<sup>fl</sup>ow management based on customer value, Tsinghua Science and Technology 11 (1) (2006) 65–73.

[27] C. Kahraman, T. Ertay, G. Buyukozkan, A fuzzy optimization model for QFD planning process using analytic network approach, European Journal of Operational Research 171 (2) (2006) 390–411.

[28] H.T. Keh, Y.H. Lee, Do reward programs build loyalty for services? The moderating effect of satisfaction on type and timing of rewards, Journal of Retailing 82 (2) (2006) 127–136.

[29] L.P. Khoo, C.H. Chen, W. Yan, An investigation on a prototype customer-oriented information system for product concept development, Computers in Industry 49 (2002) 157–174.

[30] D. Kumar, W. Chen, T.W. Simpson, A market-driven approach to product family design, International Journal of Production Research 47 (1) (2007) 71–104.

[31] V. Kumar, W. Reinartz, Customer Relationship Management: A Database Approach, John Wiley, New York, 2006.

[32] C.K. Kwong, H. Bai, Fuzzy regression approach to process modeling and optimization of epoxy dispensing, International Journal of Production Research 43 (12) (2005) 2359–2375.

[33] C.L. Lai, W.B. Lee, W.H. Ip, A study of system dynamics in just-in-time logistics, Journal of Materials Processing Technology 138 (2003) 265–269.

[34] C.Y. Lam, S.L. Chan, W.H. Ip, A Structural Reliability Business Process Modelling with System Dynamics Simulation, in: Cakaj Shkelzen (Ed.), INTECH, ISBN: 978- 953-307-055-1, 2010.

[35] C. Lin, T.S. Baines, J. O'Kane, D. Link, A Generic Methodology that Aids the Application of System Dynamics to Manufacturing System Modeling, In Proceedings of the International Conference on, Simulation, 1998 344–349.

[36] C.T. Lin, C.T. Chen, New product go/no-go evaluation at the front end: a fuzzy linguistic approach, IEEE Transactions on Engineering Management 51 (2) (2004) 197–207.

[37] X. Liu, W.J. Zhang, R. Jiang, An analytical approach to customer requirement satisfaction in design speci<sup>fi</sup>cation development, IEEE Transactions on Engineering Management 35 (1) (2008) 94–102.

[38] J.M. Lyneis, System dynamics or market forecasting and structural analysis, System Dynamics Review 16 (1) (2000) 3–25.

[39] E. Mans<sup>fi</sup>eld, S. Wagner, Organization and Strategic Factors Associated with Probabilities of Success in Industrial R&D, Journal of Business, April, 1975.

[40] A.S. Melissa, Strategic Management of Technological Innovation, International Edition McGraw-Hill, New York, 2005.

[41] W.L. Meyer, The effects of loyalty programs on customer lifetime duration and share of wallet, Journal of Retailing 83 (2) (2007) 223–236

[42] K. Mohan, R. Jain, B. Ramesh, Knowledge networking to support medical new product development, Decision Support Systems 43 (2007) 1255–1273.

[43] B.K. Mohanty, B. Bhasker, Product classi<sup>fi</sup>cation in the internet business — a fuzzy approach, Decision Support Systems 38 (2005) 611–619.

[44] H. Moskowitz, K.J. Kim, QFD optimizer: a novice friendly quality function deployment decision support system for optimizing product designs, Computers Industry Engineering 32 (3) (1997) 641–655.

[45] J.A. Murphy, J. Burton, R. Gleaves, J. Kithoff, Converting Customer Value: from Retention to Pro<sup>fi</sup>t, USA, Wiley, 2005.

[46] J.P. Peter, J.C. Olston, Consumer Behavior and Marketing Strategy, 8th ed, McGraw-Hill Irwin, New York, 2008.

[47] P.E. Pfeifer, R.L. Carraway, Modeling customer relationships as Markov chains, Journal of Interactive Marketing 14 (2) (2000) 43–45.

[48] C. Piao, X. Han, H. Wu, Research on E-commerce transaction networks using multi-agent modeling and open application programming interface, Enterprise Information Systems 4 (3) (2010) 329–353.

[49] J. Qi, L. Li, H. Ai, A systems dynamics approach to competitive strategy in mobile telecommunication industry, Systems Research and Behavioral Science 26 (2) (2009) 155–168.

[50] C. Ranaweera, J. Prabhu, On the relative importance of customer satisfaction and trust as determinants of customer retention and positive word of mouth, Journal of Targeting, Measurement and Analysis for Marketing 12 (1) (2003) 82–90.

[51] W.J. Reinartz, V. Kumar, The impact of customer relationship characteristics on profitable lifetime duration, Journal of Marketing 67 (1) (2003) 77–99.

[52] G.P. Richardson, System dynamics: simulation for policy analysis from a feedback perspective, Qualitative Simulation Modeling and Analysis (Advances in Simulation), Springer-Verlag, New York, 1991, pp. 144–169.

[53] A. Rodrigues, J. Bowers, The role of system dynamics in project management, International Journal of Project Management 14 (4) (1996) 213–220.

[54] A.K. Saysel, Y. Barlas, O. Yenigun, Environmental sustainability in an agricultural development project: a system dynamics approach, Journal of Environmental Management 64 (3) (2002) 247–260.

[55] Q. Shu, C. Wang, A conceptual framework for product lifecycle modeling, Enterprise Information Systems 1 (3) (2007) 353–363

[56] M.R. Solomon, G.W. Marshall, E.W. Stuart, Marketing: Real People Choices, 6 ed, Pearson Education, Inc., Upper Saddle River, NJ, 2010.

[57] S. Staley, J. War<sup>fi</sup>eld, Enterprise integration of product development data: systems science in action, Enterprise Information Systems 1 (3) (2007) 269–285

[58] M. Swink, S. Talluri, T. Pandejpong, Faster, better, cheaper: a study of NPD project ef<sup>fi</sup>ciency and performance tradeoffs, Journal of Operations Management 24 (5) (2006) 542–562.

[59] A.H. Tarek, M. Stuart, Software Project Dynamics: An Integrated Approach, Prentice-Hall, Englewood Cliffs, New Jersey, 1991.

[60] H.T. Thorsten, P.G. Kevin, D.G. Dwayne, Understanding relationship marketing outcomes: an integration of relational bene<sup>fi</sup>ts and relationship quality, Journal of Service Research 4 (3) (2002) 230–247.

[61] J. War<sup>fi</sup>eld, Systems science serves enterprise integration: a tutorial, Enterprise Information Systems 1 (2) (2007) 235–254.

[62] T. Wasserman, Word Games. Brandweek, October 24 (2005), 30

[63] L. Xu, The contribution of systems sciences to information systems research, Systems Research and Behavioral Science 17 (2000) 105–116.

[64] L. Xu, Information architecture for supply chain quality management, International Journal of Production Research 49 (1) (2011) 183–198.

[65] L. Xu, Z. Li, S. Li, F. Tang, A polychromatic sets approach to the conceptual design of machine tools, International Journal of Production Research 43 (12) (2005) 2397–2422.

[66] L. Xu, Z. Li, S. Li, F. Tang, A decision support system for product design in concurrent engineering, Decision Support Systems 47 (2007) 2029–2042

[67] X.F. Zha, R.D. Sriram, W.F. Lu, Evaluation and selection in product design for mass customization: a knowledge decision support approach, Arti<sup>fi</sup>cial Intelligence for Engineering Design, Analysis, and Manufacturing 18 (1) (2004) 87–109.

S.L. Chan is currently a PhD candidate in the Department of Industrial and Systems Engineering of the Hong Kong Polytechnic University. Her research interests include customer relationship management, customer satisfaction, product design and development, technology management, system dynamics modeling, quantitativ analysis, and manufacturing strategy.

Dr. W.H. Ip is an Associate Professor of the Department of Industrial and Systems Engineering of the Hong Kong Polytechnic University. Dr. Ip has more than 20 years of experience in industry, education and consulting. He received his PhD from Loughborough University in the UK. He also holds MBA, MSc, and LLB (Hons) degrees. Dr. Ip has published more than 100 international journals and conference articles. His research interests are operational research, logistics and supply chain management, ERP and MRP.
