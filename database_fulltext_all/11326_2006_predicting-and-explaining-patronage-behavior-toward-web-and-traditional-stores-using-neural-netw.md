---
otero_id: 11326
otero_key: "3AT7UXAU"
title: "Predicting and explaining patronage behavior toward web and traditional stores using neural networks: a comparative analysis with logistic regression"
authors: "Wei-yu Kevin Chiang; Dongsong Zhang; Lina Zhou"
year: "2006"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.08.016"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Predicting and explaining patronage behavior toward web and traditional stores using neural networks: a comparative analysis with logistic regression

Wei-yu Kevin Chiang<sup>\*</sup>, Dongsong Zhang, Lina Zhou

Department of Information Systems, University of Maryland, Baltimore County, 1000 Hilltop Circle, Baltimore, MD 21250, USA

Received 16 February 2004; received in revised form 25 August 2004; accepted 27 August 2004 Available online 3 October 2004

## Abstract

Web stores, where buyers place orders over the Internet, have emerged to become a prevalent sales channel. In this research, we developed neural network models, which are known for their capability of modeling noncompensatory decision processes, to predict and explain consumer choice between web and traditional stores. We conducted an empirical survey for the study. Specifically, in the survey, the purchases of six distinct products from web stores were contrasted with the corresponding purchases from traditional stores. The respondents’ perceived attribute performance was then used to predict the customers’ channel choice between web and traditional stores. We have provided statistical evidence that neural networks significantly outperform logistic regression models for most of the surveyed products in terms of the predicting power. To gain more insights from the models, we have identified the factors that have significant impact on customers’ channel attitude through sensitivity analyses on the neural networks. The results indicate that the influential factors are different across product categories. The findings of the study offer a number of implications for channel management. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Neural networks; Logit modeling; E-commerce; Choice process; Consumer behavior

## 1. Introduction

The Internet is changing the way firms market and distribute their products to customers. Despite the fact that Internet bubble in 2002 was accompanied by the shutdown of many Internet companies, sales over the Internet have continued to increase. According to Forrester Research [5], online sales in the United States grew 51% to approximately US\$26 billion just in the third quarter of 2003. Seemingly, web stores, where buyers place orders over the Internet, have emerged to become a prevalent sales channel. While more and more companies are engaging in online sales, there are speculations of an uncertain future of e-commerce due to the fact that the total amount of online sales is still a small portion of total retail sales. According to the U.S. Census Bureau [32], online sales accounted for only 1.6% of all retail sales in 2003. Will web stores prevail in future?

Apparently, the success of a web store as a viable sales channel is dependent upon whether it helps to attain a significant amount of potential customers who are willing to make purchases online. Therefore, understanding consumers’ attitude toward web stores appears crucial in the business-toconsumer (B2C) e-business context. The questions are: What are the predictors of consumers’ online buying behavior? Are we able to accurately predict and explain consumers’ channel choice between web and traditional stores? As indicated by Chiang et al. [6], the answers to the questions provide significant implications for firms who want to expand their market potential by tapping into customer segments that otherwise would not buy, or for suppliers who are strategically contemplating multi-channel distributions.

Although there are some recent papers (e.g., Refs. [2,14]) that provide insights into customers’ channel choice through analytical models and game theories, most studies seeking to address the above questions are based on empirical surveys and statistical analyses. For example, Liang and Huang [23] tried to explain the acceptance of online buying using consumer perceptions of transaction-costs associated with shopping, uncertainty and asset. The authors provided evidence that, in general, customers prefer traditional markets to the web stores and different products have different customer acceptance levels on the electronic market. Szymanski and Hise [30] measured <sup>b</sup>satisfaction<sup>Q</sup> with the Internet-shopping experience in a study of antecedents of e-satisfaction. They found that greater satisfaction with online shopping is positively correlated with consumer perceptions of the convenience, product offerings, product information, site design and financial security of web stores relative to traditional stores. Degeratu et al. [7] studied the decisions of individuals to use Peapod online grocery shopping. They gathered a sample of Peapod online buyers and a matching sample of individuals who did their grocery shopping in traditional supermarkets. As part of their broader study of brand preferences, their random utility model specified an indirect utility function for online versus offline shopping that depended only on the income of individuals. Bellman et al. [4] analyzed the responses of over 8000 participants in the Wharton Virtual Test Market who completed an initial survey about online buying and attitudes. Their logistic regression model indicated that online experience (i.e., web browsing) was the dominant predictor of whether or not a respondent had ever bought anything online. Kwak et al. [22] surveyed chatroom participants via email to discover whether these consumers had bought any of nine products online. They showed that four broad independent constructs (attitudes toward the Internet, experience with the Internet, demographics, and personality type) could explain Internet purchases of those products with logistic regressions.

All of the above empirical studies are forms of what Urban and Hauser [33] called <sup>b</sup>preference regressions<sup>Q</sup> and they all share the same a priori assumption that the process of consumers’ channel evaluation is linear compensatory. Specifically, those models assume that any shortfall in one channel attribute (e.g., immediate possession of a product) can be compensated by enhancements of other channel attributes (e.g., price). Although linear compensatory models, which can be easily estimated by statistical methods (such as analysis of variance procedures, logistic regression, and discriminant analysis), are widely used to predict consumer behavior for their ability to imitate consumer choice processes, challenges regarding their reliability have been levied by many research studies. It has been demonstrated that consumers might judge alternatives based on only one or a few attributes, and therefore the process of evaluation might not always be compensatory [18,24]. For instance, in the case of channel choice, the consumers’ concern may just be immediate possession of a product. This concern may not be compensated by the enhancement of other channel attributes, such as price (consumers do not mind paying more to possess a product immediately from another channel). Johnson et al. [18] suggested that compensatory statistical models may not be able to capture noncompensatory decision rules and, consequently, may be unreliable.

To the best of our knowledge, there are no research studies that have used noncompensatory models to explain consumers’ channel choice between traditional and web stores. Against this backdrop, this paper is motivated by the intention of making a contribution to this important line of inquiry. Specifically, we develop neural network models, which are known for their capability of modeling noncompensatory decision processes, to address the following research questions: Do noncompensatory choice models using neural networks perform better than logit choice models in predicting consumers’ channel choice between web and traditional stores? If so, based on the noncompensatory choice models, what are the main predictors of customers’ online buying behavior?

## Overview of neural networks for noncompensatory decision processes

Artificial neural networks are computer models used to emulate the human pattern recognition function through a similar parallel processing structure of multiple inputs. They learn the intrinsic nature of a pattern or process from sample data. A neural network consists of a set of fundamental processing elements (called nodes or neurons) that are distributed in a few hierarchic layers. Most neural networks contain at least three normal types of layers–input, hidden and output. The layer of input normally receives the data either from input files or directly from electronic sensors in real-time applications. The output layer generates information or conclusions. Between these two layers can be a number of hidden layers. In most networks, after each neuron in a hidden layer receives inputs from all of the neurons in a layer above it, typically an input layer, the values are added through applied weights and converted to an output value by a node activation function. Then, the result is passed to all of the neurons in the layer below it, providing a feed-forward path to the output layer. The weights of connections between two neurons in two adjacent layers are adjusted through an iterative training process where training samples are presented to the network. They are used to store knowledge and make it available for future use. Characterized by the pattern of connections between neurons, the method of determining weights on connections, and a node activation function, a neural network is designed to capture causal relationships among dependent and independent variables in a given sample data set. Unlike parametric models used in statistical techniques, neural networks do not require any restrictive a priori assumptions about the relationship among independent and dependent variables. In addition, they are adaptive and can respond to structural changes in the data generation process in ways that parametric models cannot.

Neural networks have been heavily used to model business problems in support of finance and marketing decision-making [25,34]. In most of those applications, neural networks outperformed traditional compensatory models such as discriminant and regression analysis [10,16,36]. In this study, we derived similar results in a different context. Based on the data that we collected through an empirical survey, we found that, in general, the noncompensatory neural network models outperform the compensatory logit choice models in terms of accuracy in predicting consumers’ channel choice between web and traditional stores.

The remainder of this paper is organized as follows. In the next section, we outline the empirical survey procedures and present the demographic data of the survey respondents. Then, we explain channel attributes and product categories used in the survey and report preliminary survey outcome. The logit choice models that are used to establish a performance benchmark are then introduced in the section that goes after, and it is followed by the section that presents the neural network models of consumer channel choice. Later, we report the results of our investigation and discuss some managerial implications. The paper is concluded with a summary of the findings in this study.

## 2. Survey procedures and demography of respondents

In order to collect data for our study, we conducted an empirical survey. The survey procedures are illustrated in Fig. 1. We first recruited 38 MBA students and 30 undergraduate students at 2 midwestern universities to participate in the pretest. The MBA students were asked to answer the preliminary survey questions created based on the questionnaire designed by Liang and Huang [23], while the undergraduate students were asked to provide qualitative open-ended suggestions and comments regarding the preliminary survey questionnaire and the research topic.

![](/api/attachments/3AT7UXAU/fulltext/images/b441517895e01e52068e9d5d3e31af5ae6f07151373e2ced23ba61e3be3964b0.jpg)  
Fig. 1. Survey procedures.

Based on the quantitative and qualitative feedback from the pretest, we modified and revised the questionnaire for the formal survey (see Appendix A for the formal survey questions). We then constructed a website and made the survey questions available online. We recruited MBA and undergraduate students from a large midwestern university to participate in the survey. Those students were motivated to participate in the survey by the incentive of earning extra credits for a course that they were taking. Moreover, additional extra credits were available if they invited their non-student adult family members or friends to participate in the web-based survey. Note that, in order to increase the data credibility, those non-student adults who participated in the survey were asked to provide their contact information for reference.

Table 1  
Demographic comparisons of the survey respondents

<table><tr><td rowspan="2"></td><td rowspan="2">Students(78%)N=175</td><td rowspan="2">Non-students(22%)N=49</td><td rowspan="2">Total(100%)N=224</td><td colspan="2">Age range(N=224)</td></tr><tr><td>20–29</td><td>64%</td></tr><tr><td>Female</td><td>58%</td><td>49%</td><td>56%</td><td>30–39</td><td>17%</td></tr><tr><td>Experienced</td><td>85%</td><td>88%</td><td>86%</td><td>40–49</td><td>6%</td></tr><tr><td>Mean age</td><td>27(S.D.=7)</td><td>43(S.D.=13)</td><td>30(S.D.=11)</td><td>50 and above</td><td>13%</td></tr></table>

The respondents to the research survey consisted of 224 college students (78%) and non-student adults (22%). Table 1 displays the demographic comparisons of the respondents. Fifty-six percent of the subjects were female, while 44% were male. Eighty-six percent of the subjects indicated that they had actual experience of buying some products or services from web stores. It is interesting to see that the proportion of non-student adults who had web-shopping experience is higher than that of students. The mean age of the subjects was 30 years old. Sixty-four percent were 20–29 of age, 17% were 30–39, 6% were 40–49 and 13% were over 49 years old.

## 3. Channel attributes and product categories in the survey

## 3.1. Channel attributes

A number of factors can be important in delineating whether consumers will have a positive attitude toward a shopping channel. For example, one might like to shop in a particular store because of wider brand selection and product variety. Some customers may expect rich product information available in shopping stores. The following qualitative feedback from our survey respondents is illustrative:

<sup>b</sup>I like to shop on the web because I have a bigger selection at my desk. I do not have to go anywhere to find what I want. Sometimes I can even find something I could never find in a regular store.<sup>Q</sup>

<sup>b</sup>I like to be able to go online to find out how the products have been reviewed. You can’t do that in a regular store.<sup>Q</sup>

b<sub>The</sub> <sub>convenience</sub> <sub>factor</sub> <sub>is</sub> <sub>a</sub> <sub>plus,</sub> <sub>you</sub> <sub>can</sub> <sub>shop</sub> <sub>anytime,</sub> day or night.<sup>Q</sup>

Some customers might avoid buying from a particular channel because of some concerns such as the security of transactions, post-purchase service and the uncertainty about getting the right products, as indicated by the respondents:

<sup>b</sup>I don’t like return charges associated with web merchandise returns and sometimes shipping charges are expensive.<sup>Q</sup>

<sup>b</sup>I’m a little leery of paying with my credit card on the web, because I don’t feel confident enough that it is safe to do so. I would probably order more things from the web if more locations would let you either pay by money order, cashiers check or by regular check.<sup>Q</sup>

<sup>b</sup>Returning items can be a hassle. Also the added cost of shipping and handling makes me think twice about buying online unless I can absolutely not find that item anywhere else.<sup>Q</sup>

Past studies have combined existing theoretical frameworks to investigate the factors that lead to customers’ channel preference (e.g., Refs. [8,20,23]). There are many theoretical frameworks in the IS literature, such as the technology acceptance model, flow theory and transaction cost analysis (TCA), that can be used for explaining of online consumer behavior. In this study, we focus on the economic factors to assess customers’ attitude toward web stores shopping. In particular, with TCA [37] as our theoretical foundation, we obtained a list of 18 attributes that may affect a customer’s decision to purchase from web stores for the survey (see Fig. 2).

TCA assumes that participants in a transaction relationship may seek their self-interest. Based on this assumption, we argue that shoppers will purchase products through a channel whose characteristics tend to minimize the transaction costs incurred due to product features and shoppers’ endowments [27,29]. The transaction costs perceived by customers may involve multiple factors related to the transaction process, which, according to the Consumer Mercantile Model [19], can be summarized into three phases—pre-purchase interaction, purchase consummation and post-purchase interaction. Specifically, the transaction costs considered in our survey to assess customers’ attitude toward web stores shopping include:

<sup>!</sup> Search cost (attributes 3, 15): cost perceived in relation to finding relevant products or service information in a transaction process.

<sup>!</sup> Comparison cost (attribute 14): cost perceived in relation to comparing alternatives based on the attributes of products in a transaction process.

<sup>!</sup> Examination cost (attribute 4): cost perceived in relation to examining products to be purchased in a transaction process, such as fitting shoes on.

<sup>!</sup> Opportunity cost (attributes 1, 2): cost perceived in relation to buying a product with a higher price.

<sup>!</sup> Payment cost (attribute 7): cost perceived in relation to ordering and paying for a product in a transaction process.

<sup>!</sup> Delivery cost (attributes 5, 17): product shipping cost incurred by a customer and/or the cost perceived when waiting for the product delivery.

<sup>!</sup> Post-service cost (attributes 10, 11): cost perceived after receiving a product, such as maintenance and exchange-refund policy for returns.

According to TCA, transaction cost may be affected by some factors such as <sup>b</sup>uncertainty<sup>Q</sup> and <sup>b</sup>asset specificity<sup>Q</sup>. The former refers to the risk of receiving unexpected outcomes in a transaction process (attribute 6), while the latter refers to the investments made to support transactions (attributes 8, 9, 12, 13, 16, 18).

![](/api/attachments/3AT7UXAU/fulltext/images/a61024f9831ce52d24c9b214144f3ce02131b56af88e1c15f8ce90e1f951bb4d.jpg)  
Fig. 2. List of channel attributes affecting patronage behavior.

## 3.2. Product categories

A web sales channel is capable of accommodating many different kinds of products. However, due to the nature of web stores, not all products are equal on the web. One dimension on which products are different is the ability of consumers to ascertain the quality of a product in cyberspace [11]. In addition, some products such as shoes have special needs of physical trial before being purchased. This kind of physical examination of products normally cannot be done online, as echoed from one of our survey respondents:

<sup>b</sup>I probably will never buy shoes online. They are very personal and I have a problem with shoes comfort. Sometimes I have to go to about thirty stores before I find shoes that fit right and are complimentary to my sort of style.<sup>Q</sup>

Apparently, not all products are suitable for sale at web stores. The following statements from our respondents also provide initial evidence that different products have different customer acceptance levels at web stores:

<sup>b</sup>I would never buy any consumable products, such as toothpaste or food online. I would say of anything I buy books online the most because it is easy to find what you want.<sup>Q</sup>

<sup>b</sup>The only thing I have purchased on the web is owers. That was because the person I was buying them for lived in another state. If she had not, I would have purchased them in person.<sup>Q</sup>

<sup>b</sup>Whether the good is perishable or not will affect my judgment.<sup>Q</sup>

Recognizing that different products may have different customers’ acceptance levels at web stores, we selected six products as representatives in our survey questionnaire. These six products were selected via a replication/extension of the survey used by Liang and Huang [23], where they used the following five products: <sup>d</sup>book<sup>T</sup>, <sup>d</sup>shoes<sup>T</sup>, <sup>d</sup>toothpaste<sup>T</sup>, <sup>d</sup>microwave<sup>T</sup>

Attribute performance

Table 2  
Six products used in the survey and their characteristics

<table><tr><td>Product</td><td>Characteristics of the selected product</td></tr><tr><td>Book</td><td>Information product</td></tr><tr><td>Shoes</td><td>The product with special needs of physical trial</td></tr><tr><td>Toothpaste</td><td>Consumptive and convenient product bought without much thinking</td></tr><tr><td>DVD player</td><td>Durable product with relatively higher cost and requiring maintenance</td></tr><tr><td>Flowers</td><td>The product that may be bought with temporal consideration</td></tr><tr><td>Food items</td><td>Perishable product</td></tr></table>

and <sup>d</sup>flowers<sup>T</sup>. Since microwave is not a very popular online product, we changed it to <sup>d</sup>DVD player<sup>T</sup>. In addition, we added <sup>d</sup>food items<sup>T</sup> as a representative of perishable products. These six products and their characteristics are listed in Table 2.

## 3.3. The preliminary survey outcome

In our study, the perceived performance of web stores on each attribute was measured in a relative sense with simple scales using the perceived performance of the traditional retail on each attribute as the benchmark. Specifically, to measure consumers’ perception of each channel attribute for each product, we used questions like <sup>b</sup>Compared with traditional stores, how much of a problem is the lack of physical examination of products when buying the following items from web stores?<sup>Q</sup> (See the survey questions in Appendix A for details.) Respondents were asked to indicate their perception of each attribute for web stores on a seven-point ordinal scale. The mid-level score of 4 indicates that the perception is indifferent between web stores and traditional stores. Table 3 shows the average performance of each attribute and each product obtained from our survey subjects. For product $j ,$ if web stores were perceived to have a higher level of attribute i than traditional stores, then $X _ { i j } ^ { \mathrm { { \scriptsize { W e b } } > 4 } }$ . On the other hand, if web stores were perceived to deliver a lower level of attribute i than traditional stores, then $X _ { i j } ^ { \mathrm { { W e b } } } { < } 4$

Table 3

<table><tr><td rowspan="2" colspan="2">Channel attribute (i)</td><td colspan="7">Performance of web stores on attribute i for product j ( $X_{ij}^{\text{Web}}$ )</td></tr><tr><td>Book</td><td>Shoes</td><td>Toothpaste</td><td>DVD</td><td>Flowers</td><td>Food</td><td>Overall</td></tr><tr><td rowspan="2">1. Prices</td><td>Mean</td><td>4.665</td><td>4.248</td><td>3.945</td><td>4.414</td><td>3.788</td><td>3.832</td><td>4.149</td></tr><tr><td>S.D.</td><td>1.074</td><td>0.949</td><td>0.738</td><td>1.036</td><td>1.173</td><td>0.958</td><td>0.713</td></tr><tr><td rowspan="2">2. Special sales, rebates, coupons</td><td>Mean</td><td>4.489</td><td>4.105</td><td>3.446</td><td>4.731</td><td>4.204</td><td>3.758</td><td>4.122</td></tr><tr><td>S.D.</td><td>1.199</td><td>1.291</td><td>1.260</td><td>1.257</td><td>1.177</td><td>1.202</td><td>0.889</td></tr><tr><td rowspan="2">3. Easy to find product information</td><td>Mean</td><td>4.336</td><td>3.855</td><td>4.842</td><td>3.457</td><td>4.112</td><td>4.239</td><td>4.140</td></tr><tr><td>S.D.</td><td>1.433</td><td>1.532</td><td>1.550</td><td>1.611</td><td>1.430</td><td>1.424</td><td>1.018</td></tr><tr><td rowspan="2">4. Physical examination of products</td><td>Mean</td><td>4.955</td><td>2.504</td><td>4.986</td><td>3.222</td><td>3.550</td><td>3.296</td><td>3.752</td></tr><tr><td>S.D.</td><td>1.648</td><td>1.502</td><td>1.693</td><td>1.585</td><td>1.597</td><td>1.686</td><td>1.044</td></tr><tr><td rowspan="2">5. Immediate possession of products</td><td>Mean</td><td>4.154</td><td>3.723</td><td>3.664</td><td>3.882</td><td>3.288</td><td>2.977</td><td>3.615</td></tr><tr><td>S.D.</td><td>1.510</td><td>1.479</td><td>1.735</td><td>1.428</td><td>1.532</td><td>1.403</td><td>1.152</td></tr><tr><td rowspan="2">6. Uncertainty about getting the right item</td><td>Mean</td><td>4.390</td><td>2.689</td><td>4.464</td><td>3.108</td><td>3.013</td><td>3.122</td><td>3.464</td></tr><tr><td>S.D.</td><td>1.552</td><td>1.238</td><td>1.598</td><td>1.273</td><td>1.351</td><td>1.448</td><td>0.951</td></tr><tr><td rowspan="2">7. Accepts all forms of payment</td><td>Mean</td><td>4.399</td><td>4.288</td><td>4.311</td><td>4.195</td><td>4.305</td><td>4.199</td><td>4.283</td></tr><tr><td>S.D.</td><td>1.606</td><td>1.653</td><td>1.637</td><td>1.657</td><td>1.564</td><td>1.603</td><td>1.531</td></tr><tr><td rowspan="2">8. Helpfulness of salespeople</td><td>Mean</td><td>3.186</td><td>3.014</td><td>2.959</td><td>3.264</td><td>3.153</td><td>3.050</td><td>3.104</td></tr><tr><td>S.D.</td><td>1.549</td><td>1.693</td><td>1.528</td><td>1.713</td><td>1.614</td><td>1.534</td><td>1.476</td></tr><tr><td rowspan="2">9. Brand selection and variety</td><td>Mean</td><td>5.331</td><td>4.591</td><td>4.117</td><td>4.913</td><td>4.590</td><td>4.184</td><td>4.621</td></tr><tr><td>S.D.</td><td>1.214</td><td>1.360</td><td>1.146</td><td>1.180</td><td>1.209</td><td>1.217</td><td>0.956</td></tr><tr><td rowspan="2">10. Post-purchase service</td><td>Mean</td><td>3.623</td><td>3.171</td><td>3.715</td><td>2.855</td><td>3.216</td><td>3.225</td><td>3.301</td></tr><tr><td>S.D.</td><td>1.396</td><td>1.287</td><td>1.406</td><td>1.248</td><td>1.401</td><td>1.351</td><td>1.101</td></tr><tr><td rowspan="2">11. Exchange-refund policy for returns</td><td>Mean</td><td>2.992</td><td>2.697</td><td>3.029</td><td>2.420</td><td>2.322</td><td>2.569</td><td>2.672</td></tr><tr><td>S.D.</td><td>0.954</td><td>0.840</td><td>1.002</td><td>0.946</td><td>0.943</td><td>0.952</td><td>0.761</td></tr><tr><td rowspan="2">12. Quality of the merchandise</td><td>Mean</td><td>4.453</td><td>4.207</td><td>4.131</td><td>4.302</td><td>4.004</td><td>3.887</td><td>4.164</td></tr><tr><td>S.D.</td><td>1.014</td><td>0.900</td><td>0.779</td><td>0.875</td><td>0.959</td><td>0.848</td><td>0.708</td></tr><tr><td rowspan="2">13. Product found is in stock</td><td>Mean</td><td>4.466</td><td>4.251</td><td>4.565</td><td>4.170</td><td>4.277</td><td>4.265</td><td>4.332</td></tr><tr><td>S.D.</td><td>1.254</td><td>1.196</td><td>1.139</td><td>1.232</td><td>1.249</td><td>1.232</td><td>1.052</td></tr><tr><td rowspan="2">14. Ability to compare products</td><td>Mean</td><td>4.299</td><td>3.443</td><td>3.747</td><td>4.122</td><td>3.725</td><td>3.554</td><td>3.815</td></tr><tr><td>S.D.</td><td>1.313</td><td>1.347</td><td>1.159</td><td>1.494</td><td>1.440</td><td>1.324</td><td>0.979</td></tr><tr><td rowspan="2">15. Speed of selection and purchase</td><td>Mean</td><td>3.798</td><td>3.865</td><td>4.199</td><td>3.614</td><td>3.803</td><td>4.023</td><td>3.884</td></tr><tr><td>S.D.</td><td>1.610</td><td>1.385</td><td>1.419</td><td>1.447</td><td>1.493</td><td>1.334</td><td>1.087</td></tr><tr><td rowspan="2">16. Interesting social or family experience</td><td>Mean</td><td>2.629</td><td>2.347</td><td>2.502</td><td>2.622</td><td>2.669</td><td>2.510</td><td>2.547</td></tr><tr><td>S.D.</td><td>1.118</td><td>0.902</td><td>1.080</td><td>1.093</td><td>1.090</td><td>1.026</td><td>0.934</td></tr><tr><td rowspan="2">17. Charges for shipping and handling</td><td>Mean</td><td>2.551</td><td>2.326</td><td>2.666</td><td>2.184</td><td>2.295</td><td>2.470</td><td>2.416</td></tr><tr><td>S.D.</td><td>1.126</td><td>1.065</td><td>1.346</td><td>1.291</td><td>1.185</td><td>1.197</td><td>0.908</td></tr><tr><td rowspan="2">18. Easy browsing for products</td><td>Mean</td><td>5.142</td><td>4.142</td><td>4.181</td><td>4.538</td><td>4.381</td><td>4.038</td><td>4.403</td></tr><tr><td>S.D.</td><td>1.111</td><td>1.222</td><td>1.109</td><td>1.141</td><td>1.181</td><td>1.073</td><td>0.893</td></tr></table>

All missing values in the survey are replaced by the corresponding series mean.

In addition to measuring consumers’ perceptions of attribute performance on web stores, we also assessed a behavioral response regarding consumer patronage. Our survey asked <sup>b</sup>Compared with buying in traditional stores, how likely are you to buy the following items from a web store?<sup>Q</sup> Response options ranged from 1=absolutely yes to 6=absolutely no. Based on a median split of the data, the behavioral response variable was then converted to a binary variable with 1 representing a <sup>b</sup>web store shopper<sup>Q</sup> and 0 representing a <sup>b</sup>traditional store shopper.<sup>Q</sup> Note that, in reality, customers may buy the same products from different channels at different times. Therefore, a web (traditional) store shopper can be interpreted as a shopper with a higher propensity to shop from a web (traditional) store.

## 4. The logit model of consumer channel choice

Using the concept of the Fishbein multiattribute attitude model [12,13], the consumer’s intention of purchasing a product from web stores is viewed as a linear compensatory function of beliefs about the attributes possessed by the channel weighted by the importance of each attribute. The relative utility of a consumer purchasing product j from a web store is

defined as:

$$
U _ {j} = U _ {j} ^ {\mathrm{Web}} - U _ {j} ^ {\mathrm{TR}}\tag{1}
$$

$$
= \sum_ {i} \beta_ {i} x _ {i j} ^ {\mathrm{Web}} - \sum_ {i} \beta_ {i} 4\tag{2}
$$

$$
= \sum_ {i} \beta_ {i} X _ {i j},\tag{3}
$$

where $U _ { j } ^ { \mathrm { { W e b } } } { = } \mathrm { u t i l i t y }$ of a consumer purchasing product j from web stores; $U _ { j } ^ { \mathrm { { T R } } } { = } \mathrm { u t i l i t y }$ of a consumer purchasing product $j$ from traditional stores; $x _ { i j } ^ { \mathrm { { W e b } } } =$ =perceived performance of web stores on attribute i for product $j ; ~ X _ { i j } { = } x _ { i j } ^ { \mathrm { { W e b } } }$ -4=relative performance of web stores on attribute i for product j; b =importance weight the customer attaches to attribute i.

Note that the value 4 in the model is the midpoint of the scale corresponding to traditional stores. The logit model given below allows the estimation of the importance weights for the linear compensatory function of channel attributes,

$$
Y _ {j} = \frac {\mathrm{e} ^ {U _ {j} ^ {\mathrm{Web}}}}{\mathrm{e} ^ {U _ {j} ^ {\mathrm{Web}}} + \mathrm{e} ^ {U _ {j} ^ {\mathrm{TR}}}} = \frac {1}{1 + \mathrm{e} ^ {- U _ {j}}},\tag{4}
$$

where $Y _ { j } ,$ , whose value falls between 0 and 1, is interpreted as the probability that web stores will be chosen by a consumer when buying product $j .$ This likelihood function can be used to estimate coefficients comprising $U _ { j } \ ( { \mathrm { i . e . , } \ \beta _ { i } } ,$ , the importance weight of each channel attribute).

## 5. The neural network model of consumer channel choice

As mentioned before, one primary objective of this research is to compare the predictive power of neural networks with that of logistic regression models. While there exist a variety of neural networks such as back-propagation (BP) networks and self-organizing networks, based on the nature of the problem and characteristics of the data, we chose BP networks for predicting consumers’ channel choice in this study.

5.1. Fundamentals of back-propagation (BP) neural networks

The BP network is the most commonly used artificial neural network in a variety of applications [3]. A BP network is a supervised learning network, aiming to learn to map an input vector to a desired output vector (see Fig. 3). The network learns from a training data collection, which includes a set of inputs and corresponding desired outputs. Training is an iterative process of minimizing the difference between actual output of the network and the desired output.

The training inputs are applied to the input layer of the network. The difference between the actual output at the final layer and the desired output is calculated and back-propagated to the previous layer(s). Then, the connection weights are adjusted using the Delta rule (also called the least mean square rule) in such a way as to reduce the observed output error. This process proceeds to the previous layer(s) until the input layer is reached [28]. Fig. 3(a) illustrates a three-layer BP network, wherein each input pattern is a vector that consists of m attributes (labeled as $x _ { 1 } , x _ { 2 } , . . . , x _ { m } )$ and each output vector consists of n classes (labeled as $o _ { 1 } { } _ { \cdot }$ $o _ { 2 } , . . . , o _ { n } )$ . There are l nodes in the hidden layer. $W _ { j i }$ denotes the weight value of the connection between the ith node in the input layer and jth node in the hidden layer, while $W _ { k j }$ denotes the weight value of the connection between the jth node in the hidden layer and the kth node in the output layer.

(a) A Three-Layer Back-Propagation Neural Network  
![](/api/attachments/3AT7UXAU/fulltext/images/1d4fae0db81d5d5cc92af535e46a28f6b7d9c6589f499a9a0915c80ea51ab393.jpg)  
(b) A Single Neuron j in the Hidden Layer

![](/api/attachments/3AT7UXAU/fulltext/images/9e1120d7e936a6fe06d7b779bffc49327bbba94007aef13d59d81d7d9c16bff1.jpg)  
Fig. 3. The back-propagation (BP) network.

## 5.2. Network topology and variable selection

During the construction of a neural network, the number of layers and the number of processing elements per layer are important decisions. There is no quantifiable, standard solution to the layout of networks for any particular application except some general rules picked up over time and followed by most researchers and engineers. Based on the data characteristics and objective of this research, we have created six separate BP networks, one for each individual product. Originally, in each BP network, the input layer consisted of 18 nodes, each corresponding to 1 of the channel attributes. The output layer had a single node with two values representing the consumer’s choice (either Web (1) or traditional (0) stores). The survey responses regarding consumer patronage behavior were encoded as the desired outputs for network training. Another initial task was to select the number of hidden layers. Many studies have reported no improvement of neural network performance with more than one hidden layer [17]. It was confirmed in several trial sessions during our evaluation that compared the performance of each BP network with one and two hidden layers, the additional hidden layer did not increase the classification accuracy for any product. As a result, each BP network in our study had only one hidden layer.

Once the number of hidden layer was identified, we must determine the number of nodes in the hidden layer. A larger number of hidden nodes may increase training performance, but at the expense of generalization and computation cost. Once again, there are no theoretical guidelines for such selection [17]. Therefore, we experimented with different numbers of hidden-layer nodes (within the range between 1 and 12) in each product network. The performance comparison revealed that the networks of toothpaste, ower, food and shoes performed the best (in terms of achieving the highest predictive accuracy with the minimum number of hidden-layer nodes) when there were four nodes in the hidden layer, while the networks of DVD players and books performed the best when there were three nodes in the hidden layer. In each network, we adopted one of the most commonly used activation functions–the Sigmoid activation function [39]:

$$
F (s u m _ {j}) = \frac {1}{1 + \exp (- s u m _ {j})},\tag{5}
$$

where sum<sub>j</sub> is a scalar product of an input vector and weights to the node j in either the hidden or output layer (see an example in Fig. 3(b)).

## 5.3. The procedure of network training

We used an iterative approach to training the BP network for each of the six products. The networks were initialized with all the channel attributes under investigation as input nodes and the optimal number of nodes in the hidden layer (as discussed earlier) of each network. After these networks were trained (during which separate validation data sets were applied), we conducted sensitivity analyses, aiming to identify the input variables that have significant impact on consumers’ choice. The input variables found to be insignificant were removed from the original networks, and then the training process was repeated on the pruned networks. Finally, the trained network models were tested on separate testing data sets to assess their predictive accuracy. The entire procedure is illustrated in Fig. 4.

A sensitivity analysis is used to measure the response of the network to the perturbation of network parameters [9]. Inputs and weights are two critical parameters that usually introduce perturbations to the network [38]. A sensitivity analysis provides a gross indicator of key factors via measuring the effect of altering the value of an input variable (e.g., channel attribute) on the output value (e.g., patronage behavior) [31]. In our study, the channel attributes that have little or no impact on the prediction of patronage behavior will produce low sensitivity values. Such attributes are considered insignificant and should be removed from a network. A reduction in the number of input variables directly decreases the total number of feedforward and backward propagation calculations. Such optimization offers advantages in terms of simpler networks, faster training and better generalization ability to avoid overfitting due to the oversized network [26]. Furthermore, pruning a network by removing insignificant input nodes may increase the predictive accuracy [15].

![](/api/attachments/3AT7UXAU/fulltext/images/f037e4e3b0de2686579720395e2ce6fd4a2c75203622680484457e75d44e2d79.jpg)  
Fig. 4. The procedure of network pruning.

In this study, the first order derivatives of the output units with respect to input units [9] were employed for sensitivity analysis. Thus, the sensitivity of an output $o _ { k } ( k { = } 1 , 2 , . . . , n )$ with respect to an input variable $x _ { i } ( i { = } 1 , . . . , m )$ was measured by

$$
\frac {\partial o _ {k}}{\partial x _ {i}} = \sum_ {j = 1} ^ {l} \frac {\partial o _ {k}}{\partial y _ {j}} \frac {\partial y _ {j}}{\partial x _ {i}}\tag{6}
$$

$$
\frac {\partial o _ {k}}{\partial x _ {i}} = \sum_ {j = 1} ^ {l} \left(W _ {k j} F ^ {\prime} (s u m _ {k})\right) \left(W _ {j i} F ^ {\prime} (s u m _ {j})\right)\tag{7}
$$

where y<sub>j</sub>=output of hidden node $j ~ ( j { = } 1 , ~ 2 , ~ . . . , ~ l ) ;$ $W _ { j i } { = } \mathrm { w e i g h t }$ of the connection between the hidden node j and the input node i; $W _ { k j } { = } \mathrm { w e i g h t }$ of the connection between the output node k and the hidden node $j .$

Since both hidden and output layers applied the sigmoidal activation function, we proceeded with the following transformation (subscripts k and j were ignored for simplification):

$$
F ^ {\prime} (s u m) = F (s u m) [ 1 - F (s u m) ].\tag{8}
$$

Consequently, a change in $\partial o _ { k } / \partial { x } _ { i }$ due to a perturbation $\Delta x _ { i }$ implies a change in F(sum). Given the same perturbation to $x _ { i } ,$ higher sensitivity is achieved when the change in FV(sum) is larger.

## 6. Results and implications

6.1. Comparison of predictive performance: ANN vs. logistic regression

The performance of neural networks was evaluated based on the predictive accuracy, namely the percentage of testing data whose actual outputs of networks were the same as desired ones. The results revealed that the pruned networks, which included fewer input variables than the original ones, performed just as well as or even better than the original networks across all product types.

To compare the performance of the neural network approach with that of the logistic regression approach, we applied a standard five-fold cross-validation method to each neural network and logistic regression model, and averaged the predictive accuracy of 15 cross-validation runs. This kind of cross-validation method is commonly used to ensure full and thorough training of classification models [35]. It worked as follows: the data were divided into five randomly selected, disjoint subsets of (approximately) equal size. Each subset was in turn used as the testing set while a classification model was trained using the other four subsets. Therefore, in each cross validation run, a model was trained and tested five times using different training and testing sets and a mean value of predictive accuracy of five tests was obtained. The process was repeated 15 times for each model by randomly reshuffling the data.

The means and standard deviations of predictive accuracies in 15 five-fold cross-validation runs for neural network and logistic regression models are shown in Table 4. Clearly, the neural network method demonstrates a superior ability to predict the consumer’s channel choice between traditional and web stores. To provide statistical evidence, we performed a series of paired t tests. As shown in Table 4, we can conclude that, at the 0.01 significance level, the neural network method produced a better performance across all types of products except for shoes.

There are different pros and cons of linear logistic regression and neural network models. Logistic regression yields a linear regression equation with coefficients for each significantly associated covariate. This equation allows one to make inferences regarding variable contribution to the model. In addition to predicting the outcome, the models can help explain the prediction. However, linear logistic regression is inappropriate for 0–1 dependent variables (like the classification problem in this research). For neural networks, their optimization process resembles the minimizing of the error term in that of standard regression. The difference lies in that neural networks consider linear, non-linear and pattern recognition relationships in the input data and conduct the optimization process automatically. Although there are some limitations with neural networks, such as over-fitting problem and difficulty of interpreting neural network results (<sup>b</sup>black-box<sup>Q</sup>), neural networks use a unique algorithm in such a way that the technology does not have a problem with multicollinearity, which can cause major errors in standard regression analysis [21].

## 6.2. The drivers of consumers’ channel attitude

What are the drivers of consumers’ channel attitude? In this section, we apply neural network models to investigate the factors that affect consumers’ channel choice. We chose to further examine the problem using neural network models instead of linear logistic regression models for the following two reasons. First, the result of our study indicated that noncompensatory choice models using neural networks outperform compensatory logit choice models in predicting consumers’ channel choice. This argument points to a potential flow of using compensatory models to explain predictors of customers’ online buying behavior due to their weaker predictive power. Second, the data in our study revealed a multicollinearity problem among the predictor variables. Therefore, as mentioned in the previous section, using linear logistic regression models to explain predictors will cause major errors.

Table 4  
Predictive accuracy of neural networks and logistic regression

<table><tr><td rowspan="2"></td><td colspan="2">Book</td><td colspan="2">Shoes</td><td colspan="2">Toothpaste</td><td colspan="2">DVD</td><td colspan="2">Flowers</td><td colspan="2">Food</td></tr><tr><td>Neural network</td><td>Logistic regression</td><td>Neural network</td><td>Logistic regression</td><td>Neural network</td><td>Logistic regression</td><td>Neural network</td><td>Logistic regression</td><td>Neural network</td><td>Logistic regression</td><td>Neural network</td><td>Logistic regression</td></tr><tr><td>Mean</td><td>77.2%</td><td>75.0%</td><td>75.1%</td><td>74.9%</td><td>82.7%</td><td>80.1%</td><td>72.3%</td><td>69.7%</td><td>76.5%</td><td>73.3%</td><td>80.6%</td><td>76.2%</td></tr><tr><td>S.D.</td><td>1.3%</td><td>1.3%</td><td>1.8%</td><td>1.2%</td><td>1.8%</td><td>1.2%</td><td>2.0%</td><td>1.4%</td><td>1.7%</td><td>1.4%</td><td>0.7%</td><td>1.5%</td></tr><tr><td>p-value</td><td>0.00006</td><td></td><td>0.37847</td><td></td><td>0.00004</td><td></td><td>0.00015</td><td></td><td>0.00000</td><td></td><td>0.00000</td><td></td></tr></table>

In contrast with a single constant importance weight of each channel attribute in traditional linear compensatory choice models, the importance weight of each channel attribute in neural network models can be further decomposed into multiple weights corresponding to a range of input levels. Moreover, such weights may differ from one level to another in magnitude. In other words, due to the non-compensatory nature of network models, the change in the output as a result of a change in an input may not be a constant. In our survey, for example, a response to each question was encoded into an integer value ranging from 1 to 7. Therefore, sensitivity of the output to an input can be assessed at each of the seven response levels in network models, which usually results in different weights for the same input variable at different input levels. Take books as an example: the sensitivity values of consumers’ patronage behavior to a store attribute i (i=1, 2, . . ., 18) at a response level s (s=1, 2, . . ., 7) are displayed in Table 5.

It is evident from Table 5 that sensitivity of each channel attribute varies across seven input levels. The differential explanatory power of neural network models in terms of relative weights is absent in traditional logit models. For example, the different weights on attribute 1, <sup>b</sup>prices<sup>Q</sup>, indicate that lowering book prices is most effective to attract consumers who perceive that the prices of books in web stores are at least 30% higher than those in traditional stores (level 7; see questionnaire item 1 in Appendix A). In other words, price cut may not always be attractive to every consumer since s/he may have different perception of book prices in web stores.

In order to examine the overall importance of a particular store attribute to consumers’ patronage behavior and help us prune neural networks and reduce prediction errors (as mentioned earlier), we obtained mean values of the sensitivities across all input levels for each input variable using the present knowledge about consumers’ perceptions of each channel attribute given in Table 3. Based on the derived sensitivity values, we removed those input attributes with sensitivity values smaller than 0.2. The process was repeated for each initially trained neural network separately. The results are cross-tabulated in

Table 5  
Sensitivity of output with respect to channel attributes for books

<table><tr><td rowspan="2">Channel attribute (i)</td><td colspan="7">Input level (s)</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>1. Prices</td><td>0.000</td><td>0.246</td><td>0.457</td><td>0.337</td><td>0.033</td><td>0.041</td><td>0.543</td></tr><tr><td>2. Special sales, rebates, coupons</td><td>0.000</td><td>0.000</td><td>0.010</td><td>0.753</td><td>0.508</td><td>0.040</td><td>0.000</td></tr><tr><td>3. Easy to find product information</td><td>0.379</td><td>0.020</td><td>0.379</td><td>0.000</td><td>0.163</td><td>0.000</td><td>0.000</td></tr><tr><td>4. Physical examination of products</td><td>0.230</td><td>0.010</td><td>0.032</td><td>0.320</td><td>0.000</td><td>0.307</td><td>0.000</td></tr><tr><td>5. Immediate possession of products</td><td>0.000</td><td>0.000</td><td>0.010</td><td>0.119</td><td>0.024</td><td>0.463</td><td>0.000</td></tr><tr><td>6. Uncertainty about getting the right item</td><td>0.028</td><td>0.331</td><td>0.229</td><td>0.092</td><td>0.032</td><td>0.267</td><td>0.000</td></tr><tr><td>7. Accepts all forms of payment</td><td>0.000</td><td>0.195</td><td>0.902</td><td>0.472</td><td>0.035</td><td>0.738</td><td>0.000</td></tr><tr><td>8. Helpfulness of salespeople</td><td>0.332</td><td>0.624</td><td>0.010</td><td>0.160</td><td>0.000</td><td>0.000</td><td>0.071</td></tr><tr><td>9. Brand selection and variety</td><td>0.000</td><td>0.000</td><td>0.041</td><td>0.119</td><td>0.092</td><td>0.207</td><td>0.166</td></tr><tr><td>10. Post-purchase service</td><td>0.000</td><td>0.000</td><td>0.429</td><td>0.141</td><td>0.000</td><td>0.056</td><td>0.000</td></tr><tr><td>11. Exchange-refund policy for returns</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.856</td><td>0.385</td><td>0.000</td></tr><tr><td>12. Quality of the merchandise</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.456</td><td>0.268</td><td>0.047</td><td>0.022</td></tr><tr><td>13. Product found is in stock</td><td>0.010</td><td>0.619</td><td>0.701</td><td>0.000</td><td>0.227</td><td>0.000</td><td>0.000</td></tr><tr><td>14. Ability to compare products</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.122</td><td>0.144</td><td>0.491</td><td>0.000</td></tr><tr><td>15. Speed of selection and purchase</td><td>0.000</td><td>0.050</td><td>0.024</td><td>0.151</td><td>0.122</td><td>0.321</td><td>0.198</td></tr><tr><td>16. Interesting social or family experience</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.017</td><td>0.538</td><td>0.503</td><td>0.014</td></tr><tr><td>17. Charges for shipping and handling</td><td>0.000</td><td>0.000</td><td>0.014</td><td>0.435</td><td>0.369</td><td>0.022</td><td>0.000</td></tr><tr><td>18. Easy browsing for products</td><td>0.000</td><td>0.191</td><td>0.567</td><td>0.022</td><td>0.000</td><td>0.033</td><td>0.000</td></tr></table>

(1) 0.000 indicates that the value is too small to be displayed.  
(2) All the values are normalized to the range between 0 and 1.

Table 6. Consumers’ patronage frequency is more sensitive to the channel attributes with higher sensitivity. When buying flowers, for example, Table 6 shows that consumers’ channel choice is more significantly affected by channel attributes 4, 7, 9, 10, 13 and 14.

We made a couple of insightful observations from Table 6. First, the channel attributes that strongly influence consumers’ attitude toward channel choice vary across product types. For example, patronage frequency is relatively sensitive to attribute 3, <sup>b</sup>easy to find product information<sup>Q</sup>, for majority of the six products, whereas attribute 17, <sup>b</sup>charges for shipping and handling<sup>Q</sup>, does not appear to be a major factor influencing consumers’ choice of any of the products. Second, among the selected attributes, there exists a great variability in terms of the degree of sensitivity. This offers significant managerial impli cations. Compared with improving store attributes with smaller sensitivity values, the same amount of improvement in attributes with relatively larger values is expected to produce a greater impact on consumers’ patronage behavior. The success of consumer product retailers is determined by the degree to which their strengths and weaknesses match the capabilities required to build competitive advantage [1]. Therefore, in view of cost-effectiveness, stores selling different types of products should focus on appropriate attributes when promoting their business. For example, food stores should provide mechanisms to allow consumers to easily compare different food items, and book stores should make it easier for consumers to find relevant book information. Many online retailers that sell books (e.g., Amazon) have built-in mechanisms to help consumers get right items, including providing editorial reviews and previous customers’ book ratings from previous customers, recommending other books on related topics based on other customers’ online purchasing behavior and displaying a hierarchical directory of relevant subjects.

## 7. Concluding remarks

In this paper, we developed neural networks and logistic regression models to predict and explain consumers’ choice between web and traditional stores. In order to identify new predictors of customers’ online buying behavior, we conducted an empirical survey for the study. Specifically, in the survey, purchases from web stores were contrasted with purchases from traditional stores for six distinct product categories. The respondents’ perceived attribute performance was then used to predict customers channel choice between web and traditional stores. We have provided statistical evidence that neural networks significantly outperform logistic regression models for most of the selected products in terms of the predictive power.

Attributes affecting consumers’ channel choice based on sensitivity analyses

<table><tr><td rowspan="2">Channel attribute (i)</td><td colspan="6">Product category (j)</td></tr><tr><td>Books</td><td>Shoes</td><td>Toothpaste</td><td>DVD player</td><td>Flowers</td><td>Food items</td></tr><tr><td>1. Prices</td><td>0.277</td><td>0.648</td><td>0.414</td><td></td><td></td><td></td></tr><tr><td>2. Special sales, rebates, coupons</td><td>0.254</td><td></td><td>0.671</td><td>0.223</td><td></td><td>0.691</td></tr><tr><td>3. Easy to find product information</td><td>0.466</td><td>0.532</td><td>0.304</td><td>0.248</td><td></td><td></td></tr><tr><td>4. Physical examination of products</td><td>0.331</td><td></td><td></td><td></td><td>0.278</td><td></td></tr><tr><td>5. Immediate possession of products</td><td></td><td>0.287</td><td>0.220</td><td></td><td></td><td>0.363</td></tr><tr><td>6. Uncertainty about getting the right item</td><td>0.302</td><td>0.357</td><td></td><td></td><td></td><td>0.406</td></tr><tr><td>7. Accepts all forms of payment</td><td></td><td></td><td>0.287</td><td></td><td>0.243</td><td>0.369</td></tr><tr><td>8. Helpfulness of salespeople</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>9. Brand selection and variety</td><td></td><td></td><td></td><td>0.223</td><td>0.303</td><td></td></tr><tr><td>10. Post-purchase service</td><td>0.310</td><td>0.201</td><td></td><td>0.267</td><td>0.305</td><td></td></tr><tr><td>11. Exchange-refund policy for returns</td><td>0.489</td><td>0.312</td><td></td><td></td><td></td><td></td></tr><tr><td>12. Quality of the merchandise</td><td></td><td></td><td></td><td>0.210</td><td></td><td>0.253</td></tr><tr><td>13. Product found is in stock</td><td></td><td>0.378</td><td></td><td></td><td>0.275</td><td></td></tr><tr><td>14. Ability to compare products</td><td>0.449</td><td>0.209</td><td></td><td></td><td>0.235</td><td>0.829</td></tr><tr><td>15. Speed of selection and purchase</td><td>0.268</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>16. Interesting social or family experience</td><td></td><td>0.332</td><td></td><td>0.342</td><td></td><td>0.434</td></tr><tr><td>17. Charges for shipping and handling</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>18. Easy browsing for products</td><td></td><td></td><td></td><td>0.275</td><td></td><td>0.546</td></tr></table>

All the values are normalized to the range between 0 and 1.

To gain more insights and implications from the models, we have identified the factors that have significant impact on customers’ channel choice through sensitivity analyses in the neural networks for each of the surveyed products. The results indicate that the influential factors are different across product categories. The findings of the study help us understand the decision support needs in online marketing and customer relationship management. For example, the improvement on some store characteristics may have little effect on consumer patronage for some products, and therefore, should not be high priorities for managerial actions. On the other hand, some shopping behaviors are strongly influenced by other variables that deserve more managerial attention and improvement. As indicated by [20], important decision support issues need to be tackled once a marketing channel decision has been made. Understanding what factors have the most significant impact on customers channel choice appears to be very critical in providing a decision support framework for shopping store management.

Web stores empower consumers with the ability to make informed decisions. However, the advantages of web stores may be dampened by their inherent limitations and consumers’ fear of the web. In addition to improving web stores’ service quality, educating the public on basic skills of using the web is also important. Traditional stores survived and will continue to survive. Findings in this study suggest that some types of products are more favorable for shopping online than others, and online consumers may value channel attributes differently from traditional store consumers for the same product categories. Therefore, in order to gain more competitive advantages, stores should focus on improving store attributes that are perceived important by consumers of the corresponding products in the corresponding channel. On the other hand, being aware of the strength of the opposite channel may also help managers better position themselves and make strategic decisions for their own stores.

We are not aware of any extant research studies using non-compensatory models to predict and explain consumers’ channel choice between traditional and web stores. While we believe that the neural network models developed in this paper and the implications of our results are important contributions to the related literature, there is still scope for further work in this area. For example, users personal traits, such as Internet experience, computer skill, and cognitive style, may be used for prediction of user online behavior. In this paper, we did not perform further demographical analysis due to the limitation on the data applicability. Clearly, studies seeking to analyze channel choice based on demographic categories would be valuable to extend this research.

## Appendix A. Questionnaire items

<table><tr><td>Scale repeated for items 2–16, 18</td><td>Absolutely low</td><td>Very low</td><td>Low</td><td>About the same</td><td>High</td><td>Very high</td><td>Absolutely high</td></tr><tr><td>Books</td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td></tr><tr><td>Shoes</td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td></tr><tr><td>Toothpaste</td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td></tr><tr><td>DVD player</td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td></tr><tr><td>Flowers</td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td></tr><tr><td>Food items</td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td><td> $\square$ </td></tr></table>

All responses are reverse coded (except for questions 2, 8, 9, 12, 14).

1. Compared with buying in traditional stores, how would you describe the list prices (not including charges for shipping and handling) for the following items when buying from a web store?

<table><tr><td>30% lower</td><td>20% lower</td><td>10% lower</td><td>About the same</td><td>10% higher</td><td>20% higher</td><td>30% higher</td></tr></table>

2. Compared with buying in traditional stores, how attractive are special sales, promotional rebates and coupons for the following items when buying from a web store?

3. The first step for buying merchandise is often to collect information such as where to buy, prices and others’ comments. Compared with buying in traditional stores, how much time and effort is spent in searching relevant information when buying the following items from web stores?

4. Sometimes people want to examine the product. Web stores usually don’t allow potential buyers to physically examine the product. Compared with traditional stores, how much of a problem is the lack of physical examination of products when buying the following items from web stores?

5. Web stores usually deliver the merchandise you ordered by mail or other means, which is different from traditional stores where you pick up what you buy immediately after payment. Compared with traditional stores, how much of a problem is delayed possession of products when buying the following items from web stores?

6. Compared to traditional stores, how much uncertainty is involved when purchasing the following items from web stores (e.g., the product you receive may not be exactly what you want)?

7. Web shopping requires that the order be placed on the web and the item(s) be paid by credit card or money orders. Compared with traditional stores, how much of a problem is placing orders and paying on the web when buying the following items from web stores?

8. Sometimes we want to ask a salesperson a question about a product or the store before making our purchase. Compared with buying in traditional stores, how easy is it to obtain the help of a salesperson or customer service representative before buying the following items from a web store?

9. Compared with buying in traditional stores, how would you describe the brand selection and variety available for the following items when buying from a web store?

10. After receiving the merchandise, it may need some post-purchase service. Compared with traditional stores, how much of a problem is post-purchase service after buying the following items from web stores?

11. After receiving the merchandise, it may need to be returned because it is not what you wanted. Compared with traditional stores, how much of a problem is returning a product when buying the following items from web stores?

12. Compared with buying in traditional stores, how would you describe the quality of the following items when buying from a web store?

13. Sometimes a store runs out of a product we want to purchase. Compared with buying in traditional stores, how big of a problem are stock-outs when buying the following items from a web store?

14. After collecting information, we often want to evaluate products based on various attributes such as size, color, or features. Compared with buying in traditional stores, how convenient are product evaluations when buying each of the following items from web stores?

15. Compared with buying in traditional stores, how much time does it take to get online, locate, evaluate, select and purchase a product for the following items from a web store?

16. Compared with shopping in traditional stores, how easy is it to have an interesting family or social experience shopping for the following items from a web store?

17. Traditional stores do not charge for shipping and handling because you bring the product home with you after purchase, but web stores sometimes charge for shipping and handling. What percent of the listed purchase price is typically charged for the following items from a web store?

<table><tr><td>No charge</td><td>2% of price</td><td>4% of price</td><td>6% of price</td><td>8% of price</td><td>10% of price</td><td>12% of price</td></tr></table>

(Attribute performance is rescaled as: $x _ { ( 1 7 ) j } ^ { \mathrm { { W e b } } } { = } ( 9 { - } x ) / 2$ , where x is the respondent’s response to the attribute $( x { = } 1 , . . . , 7 ) .$ If customers perceive no shipping and handling charges at a web store (x=1), then $x _ { ( 1 7 ) j } ^ { \mathrm { { W e b } } } { = } 4 .$ . In this case, the perception is indifferent between a web store and a traditional store since we assume that there are no shipping and handling charges at a retail store).

18. Compared with browsing in traditional stores, how easy is it to browse for the following items from a web store?

## References

[1] D. Aaker, Managing assets and skills: the key to a sustainable advantage, California Management Review 31 (1989 Winter) 91– 106.

[2] S. Ba, J. Stallaert, A.B. Whinston, H. Zhang, Choice of transaction channels: the effects of product characteristics on market evolution, Journal of Management Information Systems (2004) (in press).

[3] E. Barnard, L. Wessels, Extrapolation and interpolation in neural network classifiers, IEEE Control Systems 12 (5) (1992) 50– 53.

[4] S. Bellman, G.L. Lohse, E.J. Johnson, Predictors of online buying behavior, Communications of the ACM 42 (12) (1999) 32 – 38.

[5] J. Carrie, J. Walker, Q3 2003 Online Sales: Surprisingly Strong Growth, Forrester Research, 2003 (October 22).

[6] W.K. Chiang, D. Chhajed, J.D. Hess, Direct marketing, indirect profits: a strategic analysis of dual-channel supply chain design, Management Science 49 (1) (2003) 1 – 20.

[7] A.M. Degeratu, A. Rangaswamy, J. Wu, Consumer choice behavior in online and traditional supermarkets: the effects of brand name, price, and other search attributes, International Journal of Research in Marketing 17 (1) (2000) 55 – 78.

[8] S. Devaraj, M. Fan, R. Kohli, Antecedents of B2C channel satisfaction and preference, Information Systems Research 13 (3) (2002) 316–333.

[9] A.E. Engelbrecht, I. Cloete, A Sensitivity Analysis Algorithm for Pruning Feedforward Neural Networks, IEEE ICNN, Washington, DC, 1996, pp. 1274 – 1277.

[10] A. Fadlalla, C.-H. Lin, An analysis of the applications of neural networks in finance, Interfaces 31 (4) (2001) 112 – 122.

[11] J.M. de Figueiredo, Using strategic tools to generate profits in E-commerce, Working Paper, Sloan School of Management, MIT (2000).

[12] M. Fishbein, An investigation of the relationships between beliefs about an object and the attitude toward the object, Human Relations 16 (1963) 233– 240.

[13] M. Fishbein, A behavioral theory approach to the relations between beliefs about an object and the attitude toward the object, in: Martin Fishbein (Ed.), Readings in Attitude Theory and Measurement, Wiley, New York, 1967, pp. 389–400.

[14] A. Gupta, B. Sub, Z. Walterc, Risk profile and consumer chopping behavior in electronic and traditional channels, Decision Support Systems (2004) (in press).

[15] S. Hashem, Sensitivity analysis for feedforward artificial neural networks with differentiable activation functions, Proceedings of the 1992 International Joint Conference on Neural Networks, Baltimore, IEEE, vol. 1, 1992, pp. 419 – 429.

[16] S. Hung, T. Liang, V.W. Liu, Integrating arbitrage pricing theory and artificial neural networks to support portfolio management, Decision Support Systems (18) (1996) 301–316.

[17] B.A. Jain, B.N. Nag, Performance evaluation of neural network decision models, Journal of Management Information Systems 14 (2) (1997) 201– 216.

[18] F.I. Johnson, R.J. Meyer, S. Ghose, When choice models fail: compensatory models in negatively correlated environments, Journal of Marketing Research 26 (3) (1989) 255– 270.

[19] R. Kalakota, A.B. Whinston, Electronic Commerce: A Manager’s Guide, Addison-Wesley, Reading, MA, 1997.

[20] M.Y. Kiang, T.S. Raghu, K.H. Shang, Marketing on the Internet—who can benefit from an online marketing approach, Decision Support Systems (27) (2000) 383 – 393.

[21] S. Kudyba, Are neural networks a better forecaster? Futures (1998 October) 52– 57.

[22] H. Kwak, R.J. Fox, G.M. Zinkhan, What products can be successfully promoted and sold via the Internet? Journal of Advertising Research 42 (1) (2002) 23 – 38.

[23] T. Liang, J. Huang, An empirical study on consumer acceptance of products in electronic markets: a transaction cost model, Decision Support Systems (24) (1998) 29–43.

[24] J.W. Payne, J.R. Bettman, E.J. Johnson, The Adaptive Decision Maker, Cambridge University Press, New York, 1993.

[25] H.L. Poh, T. Jasic, Forecasting and analysis of marketing data using neural networks: a case of advertising and promotion impact, Paper Presented at the 11th Conference on Artificial Intelligence for Applications, Los Angeles, CA, USA, 1995, pp. 20 – 23.

[26] P.V.S. Ponnapalli, K.C. Ho, M. Thomson, A formal selection and pruning algorithm for feedforward artificial neural network optimization, IEEE Transactions on Neural Networks 10 (4) (1995) 964– 968.

[27] A. Rindfleisch, J.B. Heide, Transaction cost analysis: past, present, and future applications, Journal of Marketing 61 (4) (1997) 30 – 54.

[28] D.E. Rumelhart, J.L. McClelland (Eds.), Parallel and Distributed Processing: Explorations in the Microstructure of Cognition, MIT Press, Cambridge, MA, 1986.

[29] H.A. Shelanski, P.G. Klein, Empirical research in transaction cost economics: a review and assessment, Journal of Law, Economics, and Organization 11 (2) (1995) 335 – 361.

[30] D.M. Szymanski, R.T. Hise, e-satisfaction: an initial examination, Journal of Retailing 76 (3) (2000) 309–322.

[31] R. Tsaih, Sensitivity analysis, neural networks, and the finance, IEEE International Joint Conference on Neural Networks, Washington, DC, July 10–16, 1999, pp. 3830– 3835.

[32] United States Census Bureau, Retail E-Commerce Sales, 2004, http://www.census.gov/econ.

[33] G.L. Urban, J.R. Hauser, Design and Marketing of New Products, first edition, Prentice-Hall, Englewood Cliffs, NJ, 1980.

[34] S. Walczak, An empirical analysis of data requirements for financial forecasting with neural networks, Journal of Management Information Systems 17 (4) (2001) 203–222.

[35] S.M. Weiss, C.A. Kulikowski, Computer Systems That Learn, Kaufmann Publishers, San Mateo, CA, 1991.

[36] P. West, P.L. Brockett, L.L. Golden, A comparative analysis of neural networks and statistical methods for predicting consumer choice, Marketing Science 16 (4) (1997) 370– 391.

[37] O.E. Williamson, Transaction-cost economics, Journal of Economic Behavior and Organization 8 (4) (1987) 617–625.

[38] D.S. Yeung, X. Sun, Using function approximation to analyze the sensitivity of MLP with anti-symmetric squashing activation function, IEEE Transactions on Neural Networks 13 (1) (2002) 34 – 44.

[39] J.M. Zurada, Introduction to Artificial Neural Networks, West Publishing Company, 1992.

Wei-yu Kevin Chiang is an Assistant Professor in the Department of Information Systems, University of Maryland, Baltimore County. He received his PhD and MS degrees in Business Administration from the University of Illinois at Urbana-Champaign. His primary research is focused on applications of economic/game-theoretical models in the areas including supply chain coordination, e-commerce/e-business strategy, and distribution channel design. His research has been published in Management Science and European Journal of Operational Research, among others.

Dongsong Zhang is an Assistant Professor in the Department of Information Systems, University of Maryland, Baltimore County. He received his PhD in Management Information Systems from the University of Arizona. His research interests include Web-based learning, mobile computing, computer-mediated communication, and data mining. His work has been published in Communications of the ACM, IEEE Transactions on Multimedia, IEEE Transactions on Systems, Man, and Cybernetics, Communications of the AIS, Journal of the American Society for Information Science and Technology, among others.

Lina Zhong is an Assistant professor in the Department of Information Systems, University of Maryland, Baltimore County. She received her PhD in Computer Science from Peking University. Her research interests center around text mining, deception detection, ontology learning, and semantic Web. Her work has appeared in the Journal of Management Information Systems, Communications of the ACM, IEEE Transactions on Professional Communication, IEEE Transactions on Systems, Man, and Cybernetics, among others.
