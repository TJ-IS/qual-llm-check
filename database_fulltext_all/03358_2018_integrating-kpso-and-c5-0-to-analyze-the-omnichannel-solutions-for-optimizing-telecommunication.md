---
otero_id: 3358
otero_key: "ACH7G4VA"
title: "Integrating KPSO and C5.0 to analyze the omnichannel solutions for optimizing telecommunication retail"
authors: "Shen-Tsu Wang"
year: "2018"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2017.12.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Integrating KPSO and C5.0 to analyze the omnichannel solutions for optimizing telecommunication retail

![](/api/attachments/ACH7G4VA/fulltext/images/a0d207ba2489381be14d357ac54fa66f4282c076f70372b3c71af78c5b7d2257.jpg)

Shen-Tsu Wang

<table><tr><td>PII:</td><td>S0167-9236(17)30238-5</td></tr><tr><td>DOI:</td><td>https://doi.org/10.1016/j.dss.2017.12.009</td></tr><tr><td>Reference:</td><td>DECSUP 12910</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>26 January 2017</td></tr><tr><td>Revised date:</td><td>14 September 2017</td></tr><tr><td>Accepted date:</td><td>21 December 2017</td></tr></table>

Please cite this article as: Shen-Tsu Wang , Integrating KPSO and C5.0 to analyze the omnichannel solutions for optimizing telecommunication retail. The address for the corresponding author was captured as affiliation for all authors. Please check if appropriate. Decsup(2017), https://doi.org/10.1016/j.dss.2017.12.009

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Integrating KPSO and C5.0 to Analyze the Omnichannel Solutions for Optimizing Telecommunication Retail

Shen-Tsu Wang

Department of Commerce Automation and Management, National Pingtung University,

Taiwan, R.O.C.

Full postal address: No. 51, Min Sheng E. Road, Pingtung 900, Taiwan, R.O.C.

Tel: 886-8-7663800

Fax:886-8-7210801

e-mail: d917812@oz.nthu.edu.tw

## ABSTRACT

Telecommunication system providers offer many special number commodities, and all marketing staff sell the commodities and special number combinations according to their marketing experience; consequently, telecommunication retailers find it difficult to consider both user demands and profits in their marketing strategies. This study proposes a classification model integrating K-means Particle Swarm Optimization (KPSO) and C5.0. The particles’ PSO only followed pbest and gbest when moving, resulting in the disadvantage that PSO may easily fall into a local optimal solution. First, clustering analysis is carried out using the KPSO clustering method. Second, classification rules for clustering results are formulated by the C5.0 classification method, and a classification model is established in order to achieve effective descriptions of the clustering rules. The methods proposed herein can help retailers find and utilize complementary tariff products for mobile numbers as the basis for future sales and procurement. This study also analyzes the best media for customers’ mobile phone purchase methods and utilizes different groups of buyers of the omnichannel. The proposed model is also able to categorize new future tariffs and can further conceptualize the clustering results in the analysis of telecom tariffs and product mix. Finally, the results effectively assist the telecommunications retail industry when considering procurement, product projects, sales, and marketing solutions.

Keywords: K-means Particle Swarm Optimization, C5.0, clustering analysis, classification method, omnichannel

## 1. Introduction

Since the Taiwan telecommunications industry began to accept applications for licenses by private telecommunications operators in January 1997, a total of six telecommunications operators have been granted telecommunications licenses, including Taiwan Mobile, Far EasTone, MOBITAI, TransAsia, KG Telecom and Tuntex Telecom. This move aimed to encourage innovation and investment in telecommunications and network infrastructure. The number of mobile phone users in Taiwan rose rapidly thanks to the positive expansion of different operators. Specifically, the number of mobile phone users grew to 800,000 in the first five months after the start of this new mobile phone industry. The present number of mobile phone numbers even exceeds the total population of Taiwan, according to the findings of the National Communications Commission (NCC)[9].

The penetration rate of mobile phone services in Taiwan has exceeded 100%, and the telecommunications industry has matured rapidly and become increasingly competitive. Promotional offers launched by telecommunications operators in order to meet various user requirements and make their products more competitive resulted in telecommunications system operators introducing a vast However, the dazzling array of telecom tariffs results in information overload among customers who cannot find appropriate tariff plans based on their needs. Telecommunication retailers facing the many special combinations of number charges offered by telecommunication system providers find it difficult to sell products according to user demand, while simultaneously pursuing profits. Telecommunication retailers focus on the marketing of user number charges and relevant products as their main operational projects. Retailers purchase number charge products and supporting products from upstream telecommunication system providers; meanwhile, they can recommend appropriate number charge products according to user demands through their daily marketing. Worse still, when

# ACCEPTED MANUSCRIPT

trying to reduce their inventory costs, retailers cannot engage in massive procurement of all commodities. Therefore, retailers must recognize the charge products that are mutually supplementary in procurement; however, due to the high number of miscellaneous special combinations of number charges, they find it difficult to make a choice. Normally, sellers only consider their demands and budgets in the selection of products, meaning they must only consider the products and prices of special combinations, the number of contract periods, and the amount of prepayments. Regarding telecommunication retailers, must consider the costs and profits of selling a product, in addition to user demands. Nevertheless, telecommunication system providers offer many special number commodities, and all marketing staff sell the commodities and special number combinations according to their marketing experience; consequently, telecommunication retailers find it difficult to consider both user demands and profits in their marketing solutions. No study has explored the topic in terms of omnichannel management for telecommunications retailers and consumers, offering the best mobile phone purchase plans[9,22,31].

From the above it can be seen that telecommunications retailers need to effectively identify tariff tariffs on mobile numbers launched by different telecommunications operators, and determine the best mobile phone purchase solutions. The model proposed in this paper can effectively help salespersons recommend better complementary products or products helping enterprises to profit in the event of short product supply or considering product profits. Alternatively, it can inform salespersons' recommendations to consumers to switch to complementary products of other telecommunications system operators in order to obtain better discounts and corporate revenues. Therefore, this study first conducted clustering analysis of data about mobile number tariffs offered by different telecommunications system operators by means of the KPSO clustering method. Then, classification rules for clustering results were formulated by C5.0 classification method and a classification model was established. This model also enables the categorization of new tariffs, and more effective omnichannel-related marketing[1,20,21,27,29].

## 2. Literature Review

# ACCEPTED MANUSCRIPT

## 2.1 Related studies of omnichannel

Due to the advent of the Omnichannel Era, enterprises need to use different information technologies to find out what customers are thinking in order to obtain relevant information. Thus, they need to analyze customers’ thoughts and information to conduct the best implementation schemes for both customers and their own businesses. Retailers pursuing a multi-channel strategy can enhance customer service delivery in order to cater to customers and to boost customer satisfaction, which are important factors of retailers' customer loyalty strategy [32]. While works on obtaining the optimal allocation by forming cross-channels has already been done in the literature, the cross-channel allocation of resources has not received enough attention. Channel assessment and channel coordination strategies have also received more attention than data integration and resource allocation, but such attention is less than that paid to consumer behavior [25]. Retailers should have the following seven winning strategies: 1) Provide attractive prices and carefully organize contents; 2) Use the power of data and analysis; 3) Avoid direct parity; 4) Learn to sell specific products; 5) Emphasize information about products; 6) Build high "switching costs" to reduce rival competition; 7) Embrace competition [29].

The existing concept of B2C (Business to Customer) needs to be expanded in a few ways. The results show that the dimensions of relative advantage are an interesting interaction between three suggestions and stages of the buying process. Consumers seem to be able to distinguish the sources of added value in the channels and the stages of the buying process. More studies are needed to further explore the series of complex basic structures and comparative advantages [13]. The possible factors of customer channel switching in the purchase process are as follows. First, when consumers feel that they are more able to use different channels for different purposes, their intention to switch between retailers turns higher. To be specific, when consumers have more practical experience, their perceived self-efficacy increases. Second, if consumers find it troublesome to search for information about products from online stores and buy them in a physical store, then they exhibit cross-channel free-riding behavior [12]. Brynjolfsson et al. [4] argued that in the past, physical stores were unique in that they allowed customers to touch and feel products and provided real-time satisfaction. As the retail industry evolved toward the seamless "omnichannel retail" experience, the boundaries between

## ACCEPTED MANUSCRIPT

physical and online stores would gradually disappear and the world would become a showroom without partition walls. Li et al. [22] offered a response to the urgent need of enterprise networks for tracking and receiving feedback on products in a dead life cycle in a perceived environment. This reference presents a practical example from the perspective of information service systems, realizing the tracking of production information in all stages of the product life cycle and managing omnichannel marketing. Verhoef et al. [30] noted that sometimes omnichannel management was also known as cross-channel management. After discussion below, this reference defines omnichannel management as the coordinated management of many available channels and customer contacts and optimizing cross-channel customer experience and cross-channel performance. Multi-channel retail is thus shifting to omnichannel management retail. Enterprises and customers should focus on the use of mobile devices, allowing enterprises to provide a stronger omnichannel experience so that customers can obtain more market information. Currently, many enterprises onsider customers’ views of omnichannel, as expressed on the Internet. Flory et al. [14] argu that most customers express their views on the Internet; therefore, it is imperative ises to analyze customer opinions on the Internet. This reference propo model consisting of structure, architecture, algorithm, and mode to meet cus ers’ needs to express their views online, and the result show that the new mode is effective and efficient. Therefore, this study examined the characteristics of different customer groups in the purchase of mobile phones from the perspective of Omnichannel.

## 2.2 K-means clustering method

The K-means clustering algorithm is a partitional clustering method. The number of k clusters must be first specified. The algorithm aims at finding the representative cluster centers in each cluster. Then, the square and the minimum of the distance between each data point and the corresponding cluster center is obtained through repeated iterative operations in an effort to find the approximate best clustering approach and the most representative cluster center [34]. Although K-means has been around for a while, it still remains the most widely used partitional clustering method, and is applied to many fields and research, such as distributed computing, data mining, pattern recognition and big data [24]. The particle swarm optimization (PSO) applied with K-means clustering to research image segmentation. PSO was used as the K-means clustering algorithm to adjust the initial parameters[23]. The K-means and K-medoids for big data analysis assess the performance differences between two calculations in dataset transaction of big data[2].

## 2.3 Particle Swarm Optimization

Regarding the PSO-based settlements of different problems, relevant academic studies have proposed various mechanisms according to the types of problems, in order to enhance the efficacy of PSO. Many references consider the problems of space and particle position to enhance the efficacy of PSO [10,33], thus, this study of the clustering method uses training generation, where K-means is adopted to group the particle population in the optimal solution space and divide the search solutions.

In their exploration into the role of PSO in the binary system, that track was a zero coordinate or had a changed probability value[18]. In the past, information regarding the best performance of PSO and the best performance approximating it have adjusted the track of the “particle” population through the problem space; more the particle population operated in a continual space, the track was defined as being hanged to a position on some other dimensions. The academic pap execution procedures and problem solving . [11] proposed two methods, the binary PSO with time-varying acceleration coefficients (BPSOTVAC) and the chaotic binary PSO with time-varying acceleration coefficients (CBPSOTVAC). The results of the comparison revealed that these two methods were better than others in solving low- and high-dimension backpacks. multidimensional knapsack problems (MKPs), Chin [10] proposed Integrating the self-adaptive check and repair operator (SACRO) with PSO increases the efficiency of PSO. The traditional PSO was likely to lead to a locally optimal solution in the settlement of economic dispatch (ED). The reference proposes solving such problems with an efficient self-adaptive chaos and Kalman filter-based particle swarm optimization algorithm (SCKF-PSO) and also considers the balance and minimization of the various costs. This algorithm adopts the learning process of PSO and the estimation strategies of the Kalman filter to renew particle positions and thus increases its convergence efficiency[33]. Therefore, this

## study combined K-means (section 2.2) with the PSO algorithm to improve the cluster analysis of the parameters for the purchase of mobile phones.

## 2.4 C5.0 decision tree classification method

The C5.0 classification method is an efficiency algorithm. The banks' personal credit rating models were compared with the original credit rating models. The computer-aided diagnosis method proposed by Abdar et al. [1], as an expert and intelligent system, exerted significant influence on liver disease detection. The result showed that the improved C5.0 algorithm considered the gender difference in liver diseases, which is a key factor that many other studies lacked. Concurrently, using the rule generated by the C5.0 algorithm, the paper obtained an important result that females are less susceptible to liver diseases than males, which was not found by other research studies on liver diseases. Chen et al. [7] tried to diagnose and detect profit management in the biotechnological industry by integrating the optimal algorithms. First, the principal component analysis (PCA) and Bayesian network (BN) were adopted to screen the profit management variable. Second, the back propagation neural network and the C5.0 decision tree were combined to detect whether or not corporate revenues were heavily manipulated. Earnings management by listed companies is a challenging problem. This reference uses stepwise regression and random forest techniques to select variables and adopts classification, regression trees, C5.0, and other integrated decision methods to establish an earnings management model for the electronics industry. The results show that the integrated method is highly effective in omnichannel classification [8]. Based on classification rules for clustering, the results are formulated by the C5.0 classification method in this study.

## 3. Research Design and Method

Each particle in PSO is independently searched, and the best adaptive value memory of the individuals is used to modify the next search direction, and this is called the cognition-only model of particles. For all particles, the best adaptive value of the population is applied to modify the search speed of the next particle, and this is called the social-only model of particles. After such iterations, PSO leads to the optimal solutions to problems according to the best

## ACCEPTED MANUSCRIPT

adaptive value in the particle population [20,33]. Being universal, the standard PSO is applicable to seeking solutions to various optimization problems, including solution-seeking for multi-target functions and the arrangement of the best parameters. Moreover, it is more efficient than other well-developed algorithms. At present, the standard PSO and the improved PSOs mainly focus on how to make use of a particle population to seek the optimal solution in a solution space; however, when searching the solution space, particles merely pursue the best adaptive value memory of the current population and the previous population of i ndividuals, thus, the search scope of particles is restricted, and particles may be trapped in the local optimal neration, K-means is adopted to group the particle population in the solution space and divide the search area, then, the optimal solution in the population is searched at a low the solution space, in order to broaden the search scope of particles. After that, the obtained optimal solutions are compared to determine the best optimal solution to enhance th y of the optimal solution [15, 31]. Therefore, this study u to group the es it with PSO, as shown in Table 3. According to the the comparis his study is better than PSO. After the test for the improvement of Interactive Dichotometer 3 (ID3) and C4.5, C5.0 turned out to be the most efficient and accurate algo m. According to the algorithm, each copy of data is regarde as group. The entropy en used to calculate the information gain of all attributes, so as to for the data classification. Omnichannel classification often applies C5.0 considered important parameters for data mining technology and the machine learning method [1,8].

This study constructs a classification model applicable to the telecommunications retailing industry, which finds group relations among many mixes of telecom tariffs for mobile numbers. Therefore, this study first conducts clustering analysis of the data about mobile number tariffs offered by different telecommunications system operators using the KPSO clustering method. Since the KPSO clustering method needs to divide data into k clusters first, it is not possible to know the best way to set the value of k for most unknown data. Consequently, this study uses the silhouette coefficient and $V _ { \mathrm { m a x } }$ to evaluate the cluster validity[17,23]. The coefficient is calculated based on the mean distance between the samples and each cluster as the basis for judging classification. Additionally, the KPSO clustering technique cannot effectively express and describe the clustering rules to speculate new data in the future. Therefore, this study established classification rules for the clustering results and constructed a classification model via the C5.0 classification method. The exploration process of the hybrid classification model combining KPSO with C5.0 proposed in this study is shown in Figure 1[1, 20,21,27,30].

Fig. 1 Data Mining Method Combining KPSO with $\mathrm { C } 5 . 0$

## 3.1 The steps of KPSO combined with C5.0 classification model

Lee et al. [20] suggested that standard PSO (standard particle swarm optimization) had the advantages of less parameter settings and fast convergence, but the particles only followed pbest and gbest when moving, resulting in the disadvantage that the standard PSO may easily fall into a local optimal solution. This paper puts forward a framework of K-means particle swarm optimization (KPSO). After the search space of the initially produced particles is clustered via the K-means algorithm, the smaller $V _ { \mathrm { m a x } }$ is obtained through experiments to enhance the space search ability of particles. Then, the optimal clustering solutions $g _ { k } b e s t$ found by each cluster are compared to obtain the optimal solution in the space, which is KPSO[21,27].

In this study, after the random particles were initialized, K points were randomly selected as the initial center. Then, other particles in the space were clustered by K-means algorithm. The particle search space was partitioned through clustering. The particles had given less $V _ { \mathrm { m a x } }$ so that they could have greater space search ability. Subsequently, the clustered particles respectively searched the best fitness value in the solution search. The movement of the particles in the clusters is only affected by their best fitness value pbest and the best fitness value $g _ { k } b e s t$ in the clusters, but not by other cluster particles. The clustered particles changed their position and velocity in the solution space based on Eqs. (1) and (2). Next, the best fitness values obtained by K clusters were compared and regarded as the best solution of that iteration. After this, the particles moved following pbest and $g _ { k } b e s t$ until the set maximum iterations were obtained [20].

$$
V _ {K i d} (t) = w \times V _ {k i d} (t - 1) + c _ {1} \times R a n d (\quad) \times \left(P _ {K i d} - X _ {K i d}\right) + c _ {2} \times R a n d (\quad) \times \left(P _ {K g d} - X _ {K i d}\right)\tag{1}
$$

$$
X _ {K i d} (t) = X _ {K i d} (t - 1) + V _ {K i d} (t)\tag{2}
$$

## K-means

K-means is clustering algorithm of target as shown in Eq.(3).

$$
\text {   Arg   } \quad M i n \sum_ {k = 1} ^ {d} \sum_ {y _ {i} \in S _ {i}} \left\| y _ {i} - u _ {k} \right\| ^ {2}\tag{3}
$$

d is cluster number； $u _ { k }$ is cluster $S _ { i }$ of center of cluster ; $Y = y _ { i } , i = 1 , 2 , . . . , n$ be the set of n.

Step 1: The data set was obtained and data pre-processing was carried out. The minimum and maximum numbers of clusters by K-means clustering method were set.

Step 2: K-means algorithm was carried out and clustering operation started from the smallest k value.

Step 3: The clustering results calculated in step 2 were used to evaluate the validity of the clustering through silhouette coefficients.

Step 4: If the k value satisfied the maximum number of clusters, then the termination conditions were met and step 5 was conducted. Otherwise, step 2 was taken.

Step 5: The best clustering results were determined based on the silhouette coefficient of each k cluster.

## 3.2 Classification method

Since the KPSO clustering technique cannot effectively express and describe the clustering rules to speculate new data in the future, this classification method established classification rules for the clustering results obtained in step 5 through the C5.0 classification method.

Step 1: The K-means clustering results and the complete data sets were summarized as the training data set of the C5.0 decision tree method.

Step 2: Data classification and analysis was carried out via C5.0 decision tree classification method and the corresponding sets of classification rules were generated.

Step 3: 10-fold cross-validation was conducted based on the classification model established in step 2. The data sets were divided into ten sets. 9 sets were used for training and 1 set for testing. The average of the 10 results was regarded as an estimate of the algorithm accuracy.

## 4. Experimental Results and Discussion

Previous related studies have not explored tariff items for telecommunications mobile numbers from the perspective of telecommunications retailers, only proposing suggestions or analysis models from the perspective of users or the planning of mobile number items by telecommunications operators. This study takes the problems faced by telecommunications retailers as the research topic, and a classification rule model is established using the KPSO and C5.0 classification method

## 4.1 Data sets

This study obtained information about mobile number tariff products sold by three major private telecommunications system operators, A, B and C, in Taiwan before June 1, 2016. To be specific, the primary operation items of communications retail company S were the retail of telecommunications products and sales service for telecommunication mobile numbers, and the company had more than 100 direct retail telecommunications outlets and diverse channel types. The outlets included general private brand retail stores, system franchised stores (franchised stores of telecommunications system operators), brand retail outlets (HTC, APPLE or SAMSUNG and other brand exclusive shops), counters in department stores, counters in stores (RT-MART and Carrefour) and other sales channels. A, B and C telecommunications system operators were the leading private telecommunications operators in Taiwan, and their main services were to provide mobile telecommunications services, mobile commerce and mobile value-added items. According to the overview of mobile telecommunications business operation of June 2016 set out in the announcement made by the National Communications Commission, the respective market share of these three companies stood at 32%. The data distribution ratio and the number of attributes of these two telecommunication system operators are detailed in Table 1. The attribute names for each data are shown in Table 1. The research method proposed in this study first clustered the data using KPSO. If the number of clusters is too small, there will be no difference in the clustering results or in practical application significance. If the number of clusters is too large, it does not meet practical operation requirements. Therefore, the predetermined k value is between 4 and 10, based on the above data sets. In addition, a collection of clustering rules for the clustering results will then be established using the C5.0 decision tree classification method.

## Table 1 Date distribution of tariff items for mobile numbers of

## 4.2 Experiment results

The data was divided into 4 to 10 clusters by the K-means clustering algorithm and evaluation was carried out through the silhouette coefficient. The silhouette coefficient results of each cluster are presented in Table 2\~3, and shows that when the number of clusters is 5, the silhouette coefficient is 0.736 and the best result is obtained.

Table 2 Evaluation results of K-means clustering via Silhouette coefficient

$$
V _ {\text { max }}
$$

Therefore, the C5.0 decision tree which divided KPSO into 5 clusters generates sets of classification rules. For objective C5.0 classification accuracy, this study verified data by 10-fold cross validation, dividing the data into ten sets. 9 sets were used for training and 1 set for testing. The average of the 10 results was regarded as an estimate of the algorithm accuracy. The 10-fold average accuracy calculated by the C5.0 classification algorithm is 98.08%.

## 4.3 Experimental results and discussion

This summary will explore various clustering rules based on the sets of classification rules obtained from the summary in 4.2 and on the practical experience of the telecommunications retail industry. The attributes of telecom tariff products have the definition of interval. The definition of mobile phone sales price interval is shown in Table 4. The mobile phones were divided into 5 types, namely low-priced, low- and medium-priced, medium-priced, medium- and high-priced and high-priced. The definition of sales commission is detailed in Table 4, and the sales commissions were divided into low commission on mobile number, low and medium commission on mobile number, medium commission on mobile number, medium and high commission on mobile number and high commission on mobile number. The definition of item prices is presented in Table 4, and the item prices were classified into low tariff, low and medium tariff, medium tariff, medium and high tariff and high tariff. Also, the definition of prepaid amount is detailed in Table 4, and the prepaid amount is divided into low prepaid amount, medium prepaid amount, medium and high prepaid amount and high prepaid amount.

Table 4 Intervals of different parameter

This study uses the related theory of Solomon [28], as shown below, to develop the best solutions and media for mobile phone purchases (more than one choice) include family and friends, colleagues, classmates, clerks, TV commercials, mobile commercials and newsletters, newspapers and magazines, newsletters and leaflets. Consumers live in diversified environment and will definitely be influenced by the reference populations when making purchasing decisions. This study developed different omnichannel solutions and for mobile phone purchases according to present-day technologies and customers’ use habits[28].

(1) Opinions of family members: The family members in this case refer to brothers, sisters, parents, grandparents, and other family members.

(2) Opinions of friends: the friends in this case refer to peers who are of a similar age, enjoy similar social status, and shared values, life experiences, and lifestyles with other consumers.

(3) Advertisement-based publicity: consumers are influenced by the advertisements of different media in making purchasing decisions.

4.3.1 Analysis of the first set of clustering rules

The analysis of the first set of clustering rules is demonstrated in Table 5 and Figure 2. It includes 7 rules and its classification accuracy rate is 97.56%, as shown in Table 5. The exploration of these 7 rules is as follows:

The following conclusions can be drawn from the first set: The products are medium-priced and medium- and high-priced mobile phones, but tend to have medium to high product prices. The commission on mobile numbers is medium to high, the special price is medium and the prepaid amount is low. The following analysis can be obtained by using the above conclusions with the industry situations. The categories of products are medium- and high-priced mobile phones by using product price, and higher product price may affect the price that consumers are willing to pay. Consumers may be unwilling to pay the high price and high prepaid amount to purchase this product, so the system operators promote the combination of a low tariff item price and low prepaid amount within the price range which the public can accept. For enterprises, the commission on mobile numbers is medium and high, signifying that enterprise sales outlets can incomes by promoting this item based on the promotion solutions developed by the system operators. This can benefit the overall profitability and operating revenues of enterprises.

Table 5 The first set of clustering rules

Fig. 2 The first set of clustering rules and omnichannel solutions

## 4.3.2 Analysis of the second set of clustering rules

The analysis of the second set of clustering rules is demonstrated in Table 6 and Figure 3. It includes 12 rules. Its classification accuracy rate is 98.53%, as shown in Table 6. The exploration of these 12 rules is as follows:

However, unlike the above first set, relatively low mobile phone price contributes to consumers operators is about NT\$7,000, a price which the public can accept. The contract periods in this cluster are 24 months and 30 months, and are the most popular ones in the market in which the system operators have promoted the item prices. The purchase behavior of consumers is thus the most popular as well.

## Table 6 The second set of clustering rules

Fig. 3 The second set of clustering rules and omnichannel solutions

## 4.3.3 Analysis of the third set of clustering rules

As shown in Table 7 and Figure 4, the third set includes 2 rules. Its classification accuracy rate is 97.06% The exploration of these 2 rules is as follows:

The product category is medium-priced mobile phones. The price of such products is similar to those in the first set. However, the item price of the third set is low, so such products are more competitive in outlet sales. However, unlike the above first set, consumers will have greater willingness and ability to purchase the products at a low item price, and outlet salespeople are more persuasive when promoting this solution. The only drawback is that the prepaid amount tends to be medium and high, ranging from NT\$18,001 to NT\$23,000, which is greater than the amount of less than about NT\$8,000 in the rules of the second set. Consumers' willingness to purchase may be affected as a result. Therefore, salespeople should promote these products in such a way as to emphasize the opportunity to buy a medium- and high-priced mobile phone at a low item price, in order to encourage consumers to accept these products and tariffs.

Table 7 The third set of clustering rules

## Fig. 4 The third set of clustering rules and omnichannel solutions

## 4.3.4 Analysis of the fourth set of clustering rules

As is shown in Table 8 and Figure 5, the fourth set includes 2 rules. Its classification accuracy rate is 98.64%. The exploration of this rule set is as follows:

The following conclusions can be drawn from the fourth set: The products are medium- and In this cluster, there is only two rule, but the number obtained from this rule reaches nearly 3,353.

Table 8 The fourth set of clustering rule

Fig. 5 The fourth set of clustering rules and omnichannel solutions

## 4.3.5 Analysis of the fifth set of clustering rules

As is shown in Table 9 and Figure 6, the fifth set includes 4 rules. Its classification accuracy rate is 98.24%. The exploration of these 4 rules is as follows:

The following conclusions can be drawn from the fifth set: The products are medium-priced and medium- and high-priced mobile phones. The commission on mobile numbers is high and the special price is medium and high and high, but tends to be high. Also, the prepaid amount is medium. The following analysis can be obtained by using the above conclusions with the industry situations. The categories of products are high-priced mobile phones. Unlike the second set, consumer willingness and ability to purchase will be low. Therefore, the item price promoted by the system operators is nearly NT\$13,000. Generally, the consumption ability of such consumers is high. Their possible purchase behavior is that before the launch of new mobile phones, as they have been the users of high-priced mobile phones or high-end users, or want to show their social status. Nonetheless, according to current consumption behavior, the consumption pattern of most consumers focuses on medium-priced mobile phones.

## Table 9 The fifth set of clustering rules

## Fig. 6 The fifth set of clustering rules and omnichannel solutions

## 4.3.6 Discussion about clustering rules

The first set of buyers included mainly working people with a monthly income of NT\$35000\~45000 or university students, taking up about 19.22%. This set obtained recommendations on optimal mobile phone purchase plans mainly from their colleagues, classmates, or newspapers and magazines, which took up about 80.21% is shown in Figure 2. They tended to assess the different optimal plans carefully. The second set of buyers encompassed relatively older people, approximately aged between 45 and 65, and 23.12% of them were retirees. They obtained recommendations on optimal mobile phone purchase 70.16% is shown in Figure 3. The third set of buyers had strong purchase intention and strong purchasing power (16.14%). They tended to analyze the optimal purchase plans based on public information and less easily trusted the information provided by their relatives and friends. They obtained optimal mobile phone purchase plans mainly from TV advertisements, mobile commerce advertisements and releases, newspapers, magazines, newsletters, and promotional leaflets, which took up about 76.16% is shown in Figure 4. The fourth set of buyers mainly comprised working people with a monthly income of NT\$30000\~40000 or university students, taking up about 28.2%. This set obtained optimal mobile phone purchase plans mainly from their colleagues or newspapers and magazines, which took up about 77.28% is shown in Figure 5. The fifth set of buyers mainly consisted of working people with a monthly income more than NT\$60000 or tech lovers who changed their mobile phones regularly, taking up about 13.32%. This set obtained optimal mobile phone purchase plans mainly from advertisements or newspapers and magazines, which took up about 79.18% is shown in Figure 6. They paid more attention to the functions of new mobile phones and cared less about purchase information provided by their relatives and friends. Under the environment of fierce competition, operators in the telecommunications retail industry nowadays have begun to develop solutions to attract consumers and to expand market share.

The characteristics of different buyer groups in this study are similar to those of the conclusions in the relevant important literature, including the first and fourt buyers purchase the mobile phone of media of solution are meet Rintamä [26] defined perceived value as “the bilateral emotional combination based on the added value of products after customers use the products or services of suppliers (newspapers and magazines); such combination would lead to customers’ repeated purchase behaviors and even their recommendation of the products or services (colleagues) [6]. The fifth set of buyers purchase the mobile phone of media of solution are nearly meet Kasi ] believed that different customers might obtain different perceived values from t e. Moreover, they argued that most consumers who purchased smart phones ferent purposes for the smart phone. Therefore, a low price is not the only factor considered by consumers. In addition to building innovation function, smart phone enterprises must conduct market investigations to launch products that meet the expectations of different consumer sets [3]. The second and third set of buyers purchase the mobile phone of media of solution are nearly meet Buil et al. [5] believed consumers may at a loss regarding how to make a choice in the face of a series of products and services, it will be difficult for enterprises to attract and retain customers. erefore, many enterprises would establish a relationship with customers through “advertising” and “promotion”[19].

From the analysis of these rules it is clear that product price is the most important factor affecting item price. If the price is high, then the item price will also be high. If the price is low, then the item price will be low. In addition, the commission on mobile numbers is positively correlated with the tariff amount. The higher the tariff, the higher the commission on mobile number, and vice versa! The prepaid amount and contract periods are only a kind of contract binding on consumers when they buy

# ACCEPTED MANUSCRIPT

products or apply for mobile numbers. From the perspective of industry practice and thinking, the prepaid amount should correspond to the tariff. However, it can be observed from the first set that the prepaid amount has nothing to do with the tariff. The prepaid amount is considered to be low in cases of less than NT\$6,000. The prepaid amount observed from the data is about NT\$0 to NT\$2,000, but the tariff result is medium and high tariff, not low tariff, which significantly rejects the original idea. Therefore, the prepaid amount and the contract periods are not associated with the tariff. In terms of the current telecommunications retail industry, the best solution for operators is to integrate contract periods, telecom tariffs, and mobile phones’ selling price. The classification model proposed in this study can produce results which traditional statistical models cannot explore. The analysis of the rules verifies the practical experience of the industry and points out the cognitive blind spots of the industry. commission is medium or high, so such products have the advantage of high sales commission. s resu can effectively help enterprises to make profit. Meanwhile, the product prices affe whether consumers are able to purchase the products, and also indirectly affect the overall turnover of enterprises. The item price will affect whether consumers are able to purchase the products. In the first, second and third sets of rules, high-priced mobile phones in terms of product prices. For such products, consumers can purchase medium- and high-priced or high-priced mobile phones as long as they do not need to pay too high or low an item price. In addition, the prepaid amount is low and medium. These factors substantially stimulate consumers' willingness to purchase. At the same time, the prepaid amount will affect consumer willingness to apply for these items. The prepaid amount in these three sets is low to medium, which is the range that the public can accept. The tariff amount is medium and high. In conclusion, if the item falls into the first, second and third sets, it can help enterprises increase profit. Furthermore, for average consumers, the items in the first three sets are also the mobile number products with more discounts and less prices, thereby considerably enhancing consumer willingness to purchase. However, attention should also be given to the mobile phone patterns preferred by consumers.

## ACCEPTED MANUSCRIPT

The mobile phone patterns preferred by consumers exhibit a significant effect in set 4 and set 5. It can be found by observing the rules of the fourth and fifth sets that the product prices of these two sets are high and that the corresponding item prices are high, so consumer willingness to purchase will be low. Although the commission in these two sets is high, the range of tariffs is too wide. Moreover, the products in the fourth set are not non-mainstream, and not favored by consumers at present. If such products are procured, enterprises may have inventory pressure or be unable to sell them. Additionally, salespeople are very likely not to procure such products because of their high commission. The retail price of items in these two sets is high, and the corresponding prepaid amount is medium. However, the mobile phones are not rare products or their sales price is high. This is not a good product mix for consumers. Unless there is a special call need, the telecom tariff products for mobile numbers in these two sets will reduce consumer willingness to purchase. However, the mobile phone patterns preferred by consumers in combination with special call demands are still the solutions that need attention.

## 5. Conclusion and Future Research Directions

## The practical implications of this study are as follows:

## (1) The telecommunications retailers provide precise customer demand

When procurement personnel choose products(Mobile phone manufacturer), they usually judge whether the products should be procured and the number of products to be ordered based on their experience in the industry and past sales volumes. They therefore lack objective basis for consideration and analysis tools when making procurement decisions, and the results obtained lack credibility and reasonable logic, and are probably mixed with personal emotion and thinking. However, if they use the rules obtained in this study to analyze results and take into account diverse mixes and reasons, they will be able to quickly identify the tariffs and items with which products can be equipped in case of short supply or the launch of new products.

(2) The telecommunications retailers are good at using the omnichannel solution

The best solutions and media for mobile phone purchases include family and friends, colleagues, classmates, clerks, TV commercials, mobile commercials and newsletters, newspapers and magazines, newsletters and leaflets. As shown above, the products in the first set are medium-priced and mediumand high-priced mobile phones, but tend to have medium to high product prices. The best solutions

# ACCEPTED MANUSCRIPT

and media for purchasing mobile phones in this category will therefore be family and friends, colleagues, clerks and TV commercials. The products in the second and third sets have low mobile phone prices, so consumer willingness and ability to purchase are high. The best solutions and media for purchasing mobile phones in this category will therefore be classmates, clerks, TV commercials, mobile commercials and newsletters, newspapers and magazines, newsletters and leaflets. The products in the fourth and fifth sets have high mobile phone price and high item price, so consumer TV com ercials. These results are analyzed according to the rules generated. When new products are introduced, system operators will provide item prices and prepaid amounts for the products. The data are then calculated by referring to the rules, and it can be found that the tariff of each set is fixed in a certain interval. The amount of commission influences a retail company's income and operating revenues, so the amount of commission on mobile numbers can be known and enterprises can primarily promote products and tariffs to create greater profits. Meanwhile, when new products are launched, the marketing staff can promote the products to target groups, and solutions like omnichannel management can be used to attract the target consumers with the help of promotion by marketing staff, and special tariff offers for management system.

This study bases its grouping on prepaid amount, sales commission, telecom tariffs, contract periods, project price, and product price, and found that different customer groups purchase mobile phones through different media. Since this study does not include it in this data analysis, future research will include the history of user of mobile phone payment on the every month, the services of number charges, the number of free communication minutes, network traffic, short message charges, and multi-media services included in the charges are important for users, thus, if retailers add such information into their marketing solutions, they will be able to provide more customized services. Hence, future studies can analyze the services of number charges and customers’ monthly expenses for communication to obtain more customized service solutions.

[1]Abdar, M., Zomorodi-Moghadam, M., Das, R. & Ting, I. H. (2017). Performance analysis of classification algorithms on early detection of liver disease. Expert Systems with Applications, 67, 239-251.

[2]Arora, P. & Varshney, S. (2016). Analysis of K-Means and K-Medoids algorithm for big data. Procedia Computer Science, 78, 507-512.

[3]Bolton, R. N. & Drew, J. H. (1991). A Multistage Model of Customers' Assessments of Service Quality and Value. Journal of Consumer Research, 17(4), 375-384.

[4]Brynjolfsson, E., Hu Y. J. & Rahman, M. S., (2013). Competing in the Age of Omnichannel Retailing. MIT Sloan Management Review, 54(4), 23-29.

[5]Buil, I., Chernatony, L. & Martínez, E. (2013), Examining the role of advertising and sales promotions in brand equity creation. Journal of Business Research, 66, 115-122.

[6]Butz, H. E. & Goodstein, L. D. (1996). Measuring Customer Value: Gaining the Strategic dvantage. Organizational Dynamics, 24(3), 63-77.

[7]Chen, F. H., Chi, D. J. & Wang, Y. C. (2015). Detecting biotechnology industry's earnings pal component analysis, back propagation neural network, and decision tree. Economic Modelling, Volume 46, 1-10.

[8]Chen, F. H. & Howard, H. (2016). An alternative model for the analysis of detecting electronic industries earnings management using stepwise regression, random forest, and decision tree. Soft Computing, 20(5), 1945-1960.

[9]Chiang, C.H. (2013). Observation of Mobile Internet Access in Taiwan in Q3 2013. National Communications Commission, 2014.

[10]Chih, M. (2015). Self-adaptive Check and Repair Operator-based Particle Swarm Optimization for the Multidimensional Knapsack Problem. Applied Soft Computing, 26, 378-389.

[11]Chih, M., Lin, C. J., Chern, M. S. & Ou, T. Y. (2014). Particle Swarm Optimization with Time-Varying Acceleration Coefficients for the Multidimensional Knapsack Problem. Applied Mathematical Modelling, 38(4), 1338-1350.

[12]Chiu, H. C., Hsieh, Y. C., Roan, J., Tseng, K. J. & Hsieh, J. K. (2011). The Challenge for Multichannel Services: Cross-Channel Free-Riding Behavior. Electronic Commerce Research and Applications, 10(2), 268–277.

[13]Choudhury, V., & Karahanna, E. (2008). The Relative Advantage of Electronic Channels: A Multidimensional View. MIS Quarterly, 32 (1), 179–200.

[14]Flory, L., Osei-Bryson, K. M. & Thomas, M. (2017). A new web personalization decisionsupport artifact for utility-sensitive customer review analysis. Decision Support Systems, 94, 85-96.

[15]Jiang, F., Xia, H., Tran, Q. A., Ha, Q. M. & Hu, J. (2017). A new binary hybrid particle swarm optimization with wavelet mutation. Knowledge-Based Systems, 130, 90-101.

[16]Kasiri, L. A., Cheng, K. T. G., Sambasivan, M. & Sidin, S. M. (2017). Integration of standardization and customization: Impact on service quality, customer satisfaction, and loyalty. Journal of Retailing and Consumer Services, 35, 91-97.

[17]Kaufman, L. & Rousseeuw, P.J. (2009). Finding groups in data: an introduction to cluster analysis (Vol. 344). John Wiley & Sons.

[18]Kennedy, J. & Eberhart, R. C. (1997). A Discrete Binary Version of the Particle Swarm Cybernetics. Computational Cybernetics and Simulation, 4104-4108.

[19]Kumar, P. (2002). Price and quality discrimination in durable goods monopoly with resale trading. International Journal of Industrial Organization, 20, 1313-1339.

[20]Lee, W. P., Wang, Y. X. & Chiang, C. W. (2008). Research on a Modified Particle Swarm Optimization Algorithm. Journal of Science and Engineering Technology, 4(2), 51-62.

[21]Lei, N. & Moon, S. K. (2015) A Decision Support System for market-driven product positioning and design. Decision Support Systems, 69, 82-91.

[22]Li, Q., Luo, H., Xie, P. X., Feng, X. Q. & Du, R. Y. (2015). Product whole life-cycle and omni-channels data convergence oriented enterprise networks integration in a sensing environment.

Computers in Industry, 70, 23-45.

[23]Li, H., He, H. & Wen, Y. (2015). Dynamic particle swarm optimization and K-means clustering algorithm for image segmentation. Optik - International Journal for Light and Electron Optics, 126(24), 4817-4822.

[24]Li, C., Sun, L., Jia, J., Cai, Y. & Wang, X. (2016). Risk assessment of water pollution sources based on an integrated k-means clustering and set pair analysis method in the region of Shiyan, China. Science of The Total Environment, 557, 307-316.

[25]Neslin, S. A., Grewal, D., Leghorn, R., Shankar, V., Teerling, M. L., Thomas, J. S. & Verhoef, P. C. (2006). Challenges and Opportunities in Multichannel Customer Management. Journal of Service Research, 9(2), 95 –112.

[26]Rintamäki, T. & Kirves, K. (2017). From perceptions to propositions: Profiling customer value across retail contexts. Journal of Retailing and Consumer Services, 37, 159-167.

[27]Shao, B. B. M., Yin, P. Y. & Chen, A. N. K. (2014) Organizing knowledge workforce for specified iterative software development tasks. Decision Support Systems, 59, 19-27.

[28]Solomon, M. R. (2016). Consumer Behavior: Buying, Having, and Being. (12th Ed.). England: Pearson Education Limited.

[29]Verhoef, P. C., Neslin, S. A. & Vroomen, B. (2007). Multichannel Customer Management: Understanding the Research-Shopper Phenomenon. International Journal of Research in Marketing, 24(2), 129–148.

[30]Verhoef, P. C., Kannan, P. K. & Inman, J. J. (2015). From Multi-Channel Retailing to Omni-Channel Retailing Introduction to the Special Issue on Multi-Channel Retailing. Journal of Retailing, 91, 174–181.

[31]Verma, A. & Kaushal, S. (2017). A hybrid multi-objective Particle Swarm Optimization for scientific workflow scheduling. Parallel Computing, 62, 1-19.

[32]Wallace, D. W., Giese, J. L. & Johnson, J. L. (2004). Customer Retailer Loyalty in the Context of

Multiple Channel Strategies. Journal of Retailing, 80(4), 249–263.

[33]Wu, B. L., Liu, G., Guo, X., Shi, Y. & Xie, L. (2016). A self-adaptive chaos and Kalman filter-based particle swarm optimization for economic dispatch problem. Soft Computing, First Online: 22 January 2016, 1-13.

[34]Ye, Z., Cao, H., Zhang, Y. & Jia, L. (2016). Outlier factor based partitional clustering analysis with constraints discovery and representative objects generation. Neurocomputing, 173, 1538-1553.

![](/api/attachments/ACH7G4VA/fulltext/images/17cc2f45aff46c308ef713ed733d01369a010fa38231c370fdd85e0e8d1fe55e.jpg)

Shen-Tsu Wang received his MS degree from the Department of Industrial Engineering and Management, National Yunlin University of Science and Technology, Taiwan in 2002. He received his PhD degree from the Department of Industrial Engineering and Engineering Management, National Tsing Hua University, Taiwan in 2008. He is currently a Professor at the Department of Commerce Automation and Management, National Pingtung University, Taiwan. His areas of interest include decision analysis and supply chain management.

Table 1 Date distribution of tariff items for mobile numbers of  
telecommunications system operators

<table><tr><td>Telecom System Operators</td><td>Number</td><td>Attribute</td><td>Proportion (%)</td></tr><tr><td>A</td><td>3687</td><td>Prepaid amount Sales commission</td><td>31.01</td></tr><tr><td>B</td><td>2983</td><td>Telecom tariffs Contract periods</td><td>25.09</td></tr><tr><td>C</td><td>5219</td><td>Project price Product price</td><td>43.9</td></tr><tr><td>Total</td><td>11889</td><td>Total</td><td>100</td></tr></table>

Table 2 Evaluation results of K-means clustering via Silhouette coefficient

<table><tr><td>Number of clusters</td><td>Silhouette coefficient</td></tr><tr><td>4</td><td>0.612</td></tr><tr><td>5</td><td>0.736</td></tr><tr><td>6</td><td>0.438</td></tr><tr><td>7</td><td>0.593</td></tr><tr><td>8</td><td>0.611</td></tr><tr><td>9</td><td>0.583</td></tr><tr><td>10</td><td>0.512</td></tr></table>

Table 3 KPSO and PSO of $V _ { \mathrm { m a x } }$ test results

<table><tr><td rowspan="9">Population size=22</td><td rowspan="2">d</td><td rowspan="2">Generations</td><td>MBF</td><td>MBF</td><td>MBF</td><td>Standard PSO; MBF</td></tr><tr><td> $V_{\text{max}} = 30$ </td><td> $V_{\text{max}} = 20$ </td><td> $V_{\text{max}} = 10$ </td><td> $V_{\text{max}} = 30$ </td></tr><tr><td>4</td><td>1000</td><td>89.98</td><td>81.06</td><td>78.39</td><td>198.26</td></tr><tr><td>5</td><td>1200</td><td>97.12</td><td>88.26</td><td>68.23</td><td>183.74</td></tr><tr><td>6</td><td>1400</td><td>198.73</td><td>188.36</td><td>173.28</td><td>203.46</td></tr><tr><td>7</td><td>1600</td><td>209.38</td><td>203.24</td><td>199.23</td><td>226.23</td></tr><tr><td>8</td><td>1800</td><td>259.23</td><td>246.18</td><td>239.11</td><td>269.18</td></tr><tr><td>9</td><td>2000</td><td>336.24</td><td>329.38</td><td>316.23</td><td>312.89</td></tr><tr><td>10</td><td>2200</td><td>526.72</td><td>498.23</td><td>472.38</td><td>449.38</td></tr></table>

Hint: Mean Best Fitness, MBF

Table 4 Intervals of different parameters

<table><tr><td>No.</td><td>Definition of Intervals</td><td>Mobile Phone Price Interval (NT$)</td><td>Interval of Sales Commission on Mobile Number (NT$)</td><td>Interval of Special Price (NT$)</td><td>Interval of Prepaid Amount (NT$)</td><td>Contract Periods (Months)</td><td>Telecom Tariff (NT$)</td></tr><tr><td>1</td><td>Low</td><td>0~4000</td><td>0~1200</td><td>0~3000</td><td>0~6000</td><td>12</td><td>0~580</td></tr><tr><td>2</td><td>Low and medium</td><td>4001~12000</td><td>1201~1800</td><td>3001~7000</td><td>6001~13000</td><td>12</td><td>581~660</td></tr><tr><td>3</td><td>Medium</td><td>12001~18000</td><td>1801~2600</td><td>7001~9000</td><td>13001~18000</td><td>24</td><td>661~770</td></tr><tr><td>4</td><td>Medium and high</td><td>18001~22000</td><td>2601~4000</td><td>9001~13000</td><td>18001~23000</td><td>24</td><td>771~1010</td></tr><tr><td>5</td><td>High</td><td>22001 or more</td><td>4000 or more</td><td>13,000 or more</td><td>2,3001 or more</td><td>30</td><td>1011~1558</td></tr></table>

Table 5 The first set of clustering rules

## ACCEPTED MANUSCRIPT

<table><tr><td>No.</td><td>Clustering Rules(Percentage of total investigations,19.22)</td><td>The Best Solutions and Media to Purchase Mobile Phones (Total number of people)</td><td>Accuracy(%)</td></tr><tr><td>1</td><td>Commission&gt; 2650 and item price &lt;=4600 and prepaid amount &lt;= 5000and telecom tariff &gt; 780</td><td>Family and friends(28),colleagues(129),classmates(110), clerks(12), TVcommercials(8), mobilecommercials and newsletters(8),newspapers and magazines(85),newsletters(3) and leaflets(4).</td><td>100</td></tr><tr><td>2</td><td>Mobile phone price&gt; 13000 and itemprice &lt;= 5000 and prepaid amount &lt;=3000 and telecom tariff&gt; 820 andcontract period 12</td><td>Family and friends(21),colleagues(98), classmates(76),clerks(8), TV commercials(3),mobile commercials andnewsletters(12), newspapers andmagazines(89), newsletters(2)and leaflets(3).</td><td>97.63</td></tr><tr><td>3</td><td>Commission 3100 and mobile phoneprice &gt; 14000 and special price &lt;=5100 and prepaid amount &lt;= 2700</td><td>Family and friends(18),colleagues(98), classmates(62),clerks(19), TV commercials(6),mobile commercials andnewsletters(11), newspapers andmagazines(86), newsletters(4)and leaflets(1).</td><td>100</td></tr><tr><td>4</td><td>Telecom tariff &gt; 1230 and mobilephone price&gt; 20000 and commission3600 and prepaid amount &lt;= 5500and special price &lt;= 6100</td><td>Family and friends(50),colleagues(99), classmates(119),clerks(6), TV commercials(5),mobile commercials andnewsletters(16), newspapers andmagazines(50), newsletters(5)and leaflets(6).</td><td>96.38</td></tr><tr><td>5</td><td>Contract period 24 and mobile phoneprice&gt; 9230 and commission&gt; 3600and item price &lt;= 6100 and prepaidamount &lt;= 5000 and telecom tariff&gt;890</td><td>Family and friends(29),colleagues(86), classmates(98),clerks(20), TV commercials(2),mobile commercials andnewsletters(5), newspapers andmagazines(52), newsletters(6)and leaflets(2).</td><td>90.29</td></tr><tr><td>6</td><td>Mobile phone price &gt; 12000 andspecial price &lt;= 4200 and prepaidamount &lt;= 6000 and contract period24 and commission&gt; 3700</td><td>Family and friends(12),colleagues(46), classmates(97),clerks(18), TV commercials(7),mobile commercials andnewsletters(3), newspapers andmagazines(66), newsletters(2)and leaflets(8).</td><td>100</td></tr><tr><td>7</td><td>Telecom tariff &gt; 890 and mobilephone price&gt; 16500 and commission&gt;3900 and special price = 7300</td><td>Family and friends(48),colleagues(102), classmates(69),clerks(7), TV commercials(5),mobile commercials andnewsletters(6), newspapers andmagazines(116), newsletters(7)and leaflets(6).</td><td>98.62</td></tr></table>

Table 6 The second set of clustering rules

<table><tr><td>No.</td><td>Clustering Rules</td><td>The Best Solutions and Media to</td><td>Accuracy</td></tr></table>

## ACCEPTED MANUSCRIPT

<table><tr><td></td><td>(Percentage of total investigations, 23.12)</td><td>Purchase Mobile Phones (Total number of people)</td><td>(%)</td></tr><tr><td>1</td><td>Contract period 24 and telecom tariff &gt;790 and mobile phone price&gt;8950 and special price &lt;= 6000 and prepaid amount &lt;= 8000</td><td>Family and friends(20), colleagues(15), classmates(5), clerks(4), TV commercials(22), mobile commercials and newsletters(12), newspapers and magazines(52), newsletters(28) and leaflets(42).</td><td>99.82</td></tr><tr><td>2</td><td>Mobile phone price&gt;8500 and mobile phone price &lt;= 11500 and special price&gt;6000 and special price &lt;= 8000 and prepaid amount &lt;= 8500</td><td>Family and friends(18), colleagues(16), classmates(3), clerks(2), TV commercials(20), mobile commercials and newsletters(8), newspapers and magazines(79), newsletters(62) and leaflets(43).</td><td>100</td></tr><tr><td>3</td><td>Mobile phone price&gt;9100 and mobile phone price &lt;= 11600 and special price&gt;6000 and prepaid amount &lt;= 9000</td><td>Family and friends(8), colleagues(7), classmates(2), clerks(5), TV commercials(30), mobile commercials and newsletters(10), newspapers and magazines(36), newsletters(89) and leaflets(98).</td><td>100</td></tr><tr><td>4</td><td>Mobile phone price&gt;9200 and mobile phone price &lt;= 12000 and special price&gt;6500 and special price &lt;= 8990 and prepaid amount &lt;= 7000 and contract period 30</td><td>Family and friends(10), colleagues(18), classmates(6), clerks(7), TV commercials(25), mobile commercials and newsletters(12), newspapers and magazines(68), newsletters(72) and leaflets(29).</td><td>96.27</td></tr><tr><td>5</td><td>Mobile phone price&gt;8500 and mobile phone price &lt;= 10650 and special price&gt;6990 and special price &lt;= 8950 and prepaid amount &lt;= 8600</td><td>Family and friends(8), colleagues(6), classmates(10), clerks(6), TV commercials(43), mobile commercials and newsletters(9), newspapers and magazines(38), newsletters(91) and leaflets(63).</td><td>91.39</td></tr><tr><td>6</td><td>Commission &lt;= 4500 and mobile phone price&gt;8200 and special price&gt;5990 and special price&lt;= 7990 and prepaid amount &lt;= 7500</td><td>Family and friends(2), colleagues(12), classmates(3), clerks(8), TV commercials(40), mobile commercials and newsletters(8), newspapers and magazines(82), newsletters(43) and leaflets(62).</td><td>100</td></tr><tr><td>7</td><td>Special price&gt;5850 and special price &lt;= 7250 and prepaid amount &gt;3800 and prepaid amount &lt;= 9000</td><td>Family and friends(6), colleagues(15), classmates(6), clerks(7), TV commercials(21), mobile commercials and newsletters(9), newspapers and magazines(89), newsletters(29) and leaflets(42).</td><td>98.97</td></tr><tr><td>8</td><td>Mobile phone price&gt;6200 and mobile phone price &lt;= 10900 and special price&gt;5460</td><td>Family and friends(5), colleagues(10), classmates(12), clerks(8), TV commercials(20), mobile commercials and</td><td>100</td></tr></table>

## ACCEPTED MANUSCRIPT

<table><tr><td></td><td></td><td>newsletters(8), newspapers and magazines(68), newsletters(21) and leaflets(36).</td><td></td></tr><tr><td>9</td><td>Mobile phone price &gt; 8100 and special price &gt; 5990 and special price &lt;= 6990 and prepaid amount &gt; 700 and prepaid amount &lt;= 7500</td><td>Family and friends(8), colleagues(12), classmates(7), clerks(8), TV commercials(21), mobile commercials and newsletters(6), newspapers and magazines(89), newsletters(36) and leaflets(40).</td><td>100</td></tr><tr><td>10</td><td>Mobile phone price &gt; 11200 and special price &gt; 4000 and special price &lt;= 6190 and prepaid amount &gt; 6000 and prepaid amount &lt;= 8800</td><td>Family and friends(8), colleagues(8), classmates(8), clerks(6), TV commercials(18), mobile commercials and newsletters(5), newspapers and magazines(38), newsletters(40) and leaflets(23).</td><td>98.23</td></tr><tr><td>11</td><td>Special price &gt; 6490 and special price &lt;= 9650 and prepaid amount &gt; 7500 and prepaid amount &lt;= 9900</td><td>Family and friends(6), colleagues(8), classmates(2), clerks(8), TV commercials(21), mobile commercials and newsletters(2), newspapers and magazines(66), newsletters(29) and leaflets(39).</td><td>97.63</td></tr><tr><td>12</td><td>Contract period = 24 and mobile phone price&gt; 5300 and mobile phone price &lt;= 8200 and special price &gt; 6210</td><td>Family and friends(8), colleagues(13), classmates(6), clerks(7), TV commercials(16), mobile commercials and newsletters(11), newspapers and magazines(82), newsletters(26) and leaflets(58).</td><td>100</td></tr></table>

Table 7 The third set of clustering rules

<table><tr><td>No.</td><td>Clustering Rules(Percentage of total investigations, 16.14)</td><td>The Best Solutions and Media to Purchase Mobile Phones (Total number of people)</td><td>Accuracy (%)</td></tr><tr><td>1</td><td>Commission &lt;= 6500 and mobile phone price &lt;= 12500 and special price &lt;= 2550 and prepaid amount &lt;= 18990</td><td>Family and friends(112), colleagues(98), classmates(87), clerks(100), TV commercials(248), mobile commercials and newsletters(116), newspapers and magazines(160), newsletters(120) and leaflets(115).</td><td>96.83</td></tr><tr><td>2</td><td>Mobile phone price &lt;= 11500 and prepaid amount &gt; 18500</td><td>Family and friends(108), colleagues(99), classmates(107), clerks(112), TV commercials(152), mobile commercials and newsletters(138), newspapers and magazines(129), newsletters(163) and leaflets(121).</td><td>97.28</td></tr></table>

Table 8 The fourth set of clustering rules

<table><tr><td>No.</td><td>Clustering Rules (Percentage of total investigations, 28.2)</td><td>The Best Solutions and Media to Purchase Mobile Phones (Total number of people)</td><td>Accuracy (%)</td></tr></table>

## ACCEPTED MANUSCRIPT

<table><tr><td>1</td><td>Mobile phone price &lt;= 13500 and special price &lt;= 3500 and prepaid amount &lt;= 18000 and tariff &gt;670</td><td>Family and friends(30), colleagues(683), classmates(20), clerks(168), TV commercials(50), mobile commercials and newsletters(24), newspapers and magazines(598), newsletters(26) and leaflets(21).</td><td>97.28</td></tr><tr><td>2</td><td>Mobile phone price &lt;= 21500 and prepaid amount &lt;= 16500 and tariff &lt;990</td><td>Family and friends(36), colleagues(528), classmates(9), clerks(209), TV commercials(70), mobile commercials and newsletters(39), newspapers and magazines(782), newsletters(30) and leaflets(30).</td><td>100</td></tr></table>

Table 9 The fifth set of clustering rules

<table><tr><td>No.</td><td>Clustering Rules(Percentage of totalinvestigations, 13.32)</td><td>The Best Solutions and Media to PurchaseMobile Phones (Total number of people)</td><td>Accuracy(%)</td></tr><tr><td>1</td><td>Mobile phone price &gt;19750 and prepaidamount &gt;16500</td><td>Family and friends(7), colleagues(10),classmates(12), clerks(12), TVcommercials(198), mobile commercials andnewsletters(14), newspapers andmagazines(162), newsletters(5) andleaflets(6).</td><td>97.16</td></tr><tr><td>2</td><td>Mobile phone price &gt;20000 and special price&lt;= 14500 and prepaidamount &gt;13500 andcommission &gt;4100</td><td>Family and friends(4), colleagues(20),classmates(12), clerks(10), TVcommercials(202), mobile commercials andnewsletters(5), newspapers andmagazines(83), newsletters(6) andleaflets(8).</td><td>100</td></tr><tr><td>3</td><td>Mobile phone price&gt;22500 and special price&lt;= 14000 and prepaidamount &gt;17000</td><td>Family and friends(8), colleagues(16),classmates(16), clerks(12), TVcommercials(181), mobile commercials andnewsletters(11), newspapers andmagazines(121), newsletters(7) andleaflets(10).</td><td>99.83</td></tr><tr><td>4</td><td>Mobile phone price&gt;19500 and mobile phoneprice &lt;= 23500 andspecial price&gt;13500 andcommission&gt;4200</td><td>Family and friends(9), colleagues(9),classmates(20), clerks(9), TVcommercials(172), mobile commercials andnewsletters(20), newspapers andmagazines(134), newsletters(11) andleaflets(8).</td><td>95.98</td></tr></table>

## Highlights

 This study analyzes different groups of buyers of the omnichannel.

 The telecommunications retailers provide precise customer demand.

 The telecommunications retailers are good at using the omnichannel solution.

![](/api/attachments/ACH7G4VA/fulltext/images/de8466bfbc425c4eb283ee78e0d6a9dad66fcaf91a6b39a0c5b0f165f0457dbf.jpg)

![](/api/attachments/ACH7G4VA/fulltext/images/12bf071ac296d16fc2e2a92445323823b176734d7bd0d7743da03e94b7ac029d.jpg)  
Figure 2

![](/api/attachments/ACH7G4VA/fulltext/images/5b148800dd09bccf9713b42181c5fdf0df8de2121025de067aaed16e45dad695.jpg)  
Figure 3

![](/api/attachments/ACH7G4VA/fulltext/images/b449cc0f82e5aef9c16227e3840bc649931cecfb19f2ef91858a273ea6c73213.jpg)  
Figure 4

![](/api/attachments/ACH7G4VA/fulltext/images/61551531b3a07bf11c112a80e0c2cd08ac93481cf12797777d88b7504ee82dc8.jpg)  
Figure 5

![](/api/attachments/ACH7G4VA/fulltext/images/186a7806bfce7a3b8060214183a6f629bb08a8490ef9271abdfcce2510defede.jpg)  
Figure 6
