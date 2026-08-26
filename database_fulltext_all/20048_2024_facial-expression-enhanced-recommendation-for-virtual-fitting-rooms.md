---
otero_id: 20048
otero_key: "5JZBS5GR"
title: "Facial expression-enhanced recommendation for virtual fitting rooms"
authors: "Ying Xue; Jianshan Sun; Yezheng Liu; Xin Li; Kun Yuan"
year: "2024"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2023.114082"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Facial expression-enhanced recommendation for virtual fitting rooms

Ying Xue <sup>a</sup>, Jianshan Sun <sup>a,b,c,\*</sup>, Yezheng Liu <sup>a,d</sup>, Xin Li <sup>e</sup>, Kun Yuan <sup>a,c</sup>

<sup>a</sup> School of Management, Hefei University of Technology, Hefei, Anhui 230009, China

<sup>b</sup> Key Laboratory of Process Optimization and Intelligent Decision-making, Ministry of Education, Hefei, Anhui 230009, China

<sup>c</sup> Anhui Provincial Laboratory of Philosophy and Social Sciences, Hefei, Anhui 230009, China

<sup>d</sup> National Engineering Laboratory for Big Data Distribution and Exchange Technologies, Shanghai 200436, China

<sup>e</sup> Department of Information Systems, City University of Hong Kong, Kowloon Tong, Hong Kong, China

## A R T I C L E I N F O

Keywords: Virtual fitting rooms Facial expression Recommender system User behaviors

## A B S T R A C T

With the development of Augmented Reality (AR) technology in the retail industry, virtual fitting room (VFR) are considered promising enhancement of e-commerce by providing users with an immersive environment to try on new products, especially fashion products. While allowing users having more vivid impression of products, virtual fitting rooms also offer sellers more channels to collect information on user preferences, which can be used to enhance recommender systems. This study proposes to leverage facial expression recognition technology together with fine-grained human-computer interactions in virtual fitting rooms to personalize product recom mendations. This paper proposes a recommendation algorithm based on confidence setting, negative feedback sampling, and matrix factorization to model user behaviors in virtual fitting rooms. We conduct an experiment on 81 subjects to evaluate the proposed method. Experimental results show the proposed method outperforms existing methods using traditional behavior information. Our study provides a strong support to the value of AR in enhancing e-commerce.

## 1. Introduction

Augmented reality (AR) is a technology that combines virtual in formation with the real world. AR has gained considerable attention and has already generated excellent applications in navigation, art, social networking, and marketing [1]. The Virtual Fitting Room(VFR) is an application of AR technology that combines the real physical environ ment with the virtual effects of the product to better understand the product [2]. It belongs to the concept of MR proposed in [3] which is a kind of AR.

Traditionally, users mainly obtain product information from the text descriptions and images provided by the merchant [4,5]. With VFR, it enables users to learn about items intuitively by three-dimensional im ages of items and users can see how the products look like in real world settings, such as how a sofa looks in their living room and how cosmetics look on their faces [6]. VFR breaks the boundaries of consumers, products, and application scenarios and helps consumers view products more easily and intuitively [7]. Such an in-depth interaction forms an immersive and highly interactive virtual shopping environment. Therefore, the application of VFR can also enhance the post-purchase consumption experience [8]. Recently, several companies and plat forms, such as IKEA, Nike, Amazon, and Alibaba have provided VFR services to help consumers experience products [9,10].

In addition to help users understand products, virtual fitting rooms also allow detailed behavioral traces of consumers, providing richer scene experience data for discovering consumers' real-time needs [11,12]. In the AR e-commerce shopping environment virtual fitting rooms, consumers click to try out products, adjust product position, color, etc. With the help of eye-tracking devices and facial expression technology, more information about consumers' attention and prefer ence can be revealed, which are fine-grained portrayals of consumers behaviors and emotions, and can be employed to enhance recommender systems. However, the existing recommendation methods do not adequately capture and utilize such AR-related information.

Although VFR has rapidly developed in e-commerce, existing ap plications are mainly to display product information [13]. The existing studies focus on the impact of VFR AR on the user experience [14] and decision-making process [15,16]. There are studies on using VFR AR to display trip recommendation information [17,18]. Few studies com bined VFR AR interactions into recommendation algorithms. Users' physical features can support better item recommendation in virtual fitting rooms [19], and this is considered a high-impact direction [20].

Then, whether the interaction between users and products in the virtual fitting room can help users' preference prediction and product recommendation, and how to use users' behavior for recommendation, are the questions that need to be studied. In this paper, we propose a personalized recommendation method in a virtual fitting room envi ronment that uses user interaction behavior to predict user preferences based on Matrix factorization methods. In this method, it is proposed that the user's expression information when interacting with products in the virtual fitting room can help predict user preferences and recom mend products. By designing and conducting laboratory experiments, the performance of the proposed method in this paper is verified.

The contribution of this article is summarized in the following three aspects: 1) We propose a personalized recommendation method through their multiple interaction behaviors in VFR scenarios. 2) We leverage user facial expressions in VFR as new explicit feedback to predict user preferences. 3) We collect data and validate the performance of the proposed recommendation method by organizing user experiments, and provide new insights into product marketing and user decision-making in virtual fitting room environments.

## 2. Related work

We divide the relevant research into two categories, namely the impact of virtual environment usage on user purchase decision behavior, and existing research on designing recommendation methods in the virtual environment.

## 2.1. Virtual environment in E-commerce

Virtual reality and augmented reality technologies such as virtual fitting rooms are increasingly being used in physical and online retail to provide virtual shopping environments [21], to improve the shopping environment and consumer experience [22]. The use of virtual envi ronment technology has had an impact on users' shopping experience and purchase decisions, and there has been a great deal of research in the literature on this.

Virtual environment provides users with more intuitive interaction by adding virtual images of products to the physical world, making it more immersive than traditional e-commerce sites. There are two main aspects to the generation of immersive experience. One is that the AR environment triggers the consumer's sense of presence [23], and the other is that when the virtual experience is very close to the real, con sumers will have a credible illusion of the scene [24]. Specifically, im mersion can lead to higher interactivity, vividness, and other experiences [25]. In addition, the use of AR positively impacts con sumers' perception of brand usefulness and brand attitudes [26], while increasing consumer engagement and satisfaction [27].

The impact of AR on consumers' experience and emotional percep tions affects their attitude and satisfaction with the shopping process, which in turn affects purchase intentions. Research by Helena et al. [28] showed that liveliness positively stimulated consumer purchase in tentions. Bone et al. [29] demonstrated that interactivity led to a better consumer experience and further enhanced user satisfaction and pur chase intention. Kim et al. [30] proposed that consumers' perceptions of usefulness, ease of use, and pleasure affected consumers' attitudes and willingness to use AR fitting equipment. Yim et al. [31] proposed a model to confirm that AR websites' liveliness, interactivity, and novelty affected consumers' immersion, which in turn affected consumers' per ceptions of usefulness, attitudes, and purchase intentions. The same conclusion was found in paper [32].

There are also individual differences in the user experience in the virtual shopping environment. Existing studies have found that con sumer purchase intentions in immersive interactive environments are also affected by consumer gender [30], degree of participation [33], and prior experience [31]. Therefore, personalization in the virtual shopping environment is also essential.

## 2.2. Recommendation in virtual environment

Recommender systems are commonly used in online shopping plat forms. Research has found that using augmented reality shopping as sistant with recommendation can help users improve their shopping experience [34]. With the application of virtual environment in ecommerce, there have been several studies proposing personalized recommendation methods in virtual environment. The literature has demonstrated that AR can be used in brick-and-mortar stores to stimu late purchase [35]. Ahn et al. [36] developed an application with an AR interface to tag the healthiness of products and recommended healthy products to users through their selection behaviors and the product's location. Another study used AR technology to help users find the areas to visit in large shopping malls. In addition to assisting the users in finding products [37]. Marquez ´ et al. [38] deployed AR devices in physical stores. When users use AR to browse products, it recommends products similar to the currently browsed products and lists the product attributes to help users make comparisons.

Besides the application in brick-and-mortar stores, some studies apply virtual environment recommendations to travel, navigation, and online APP. The user's real-time location is obtained through AR com bined with the museum's exhibitions, stay time, social media comments and other information to recommend suitable museum tour routes for users [17,39,40]. There is also research to design AR shopping recom mendation environment. Hiranandani et al. [41] designed an AR-based furniture retail APP to model user preferences and product compatibility during AR interactions as a way to recommend products to users. K. Andersen et al. [42] designed a variety of immersive scenarios to assess user preferences for food, drink, and dining environments by adjusting details in the scenes, including temperature, color, smell, ambience, etc.

Most existing studies use virtual environment as a tool for data acquisition and information display, without fully considering the interaction behavior and meaning of users in virtual environment, especially in shopping scenarios.

In this paper, we design recommendation methods using user inter action behaviors and facial expressions in virtual fitting room environ ments. Studies have shown that facial expressions can be used as implicit feedback to improve the results in the search system. Existing research uses collaborative filtering methods to make recommendations by calculating the similarity of facial expressions when different users watch videos. Liu et al. combined emotions, audio and video features to predict the user's intention to want to see the movie after seeing the trailer. Our proposed method uses facial expressions to identify user preferences and combine them with other interaction behaviors to make product recommendations.

## 3. Research context

Our proposed recommendation context is a VFR environment, where consumers can try on certain products, such as fashion products. Generally, in such an application, a user can choose a product, and “put” it in a specific scene to get product information through AR technology. As compared with traditional e-commerce environment, where users can only see the text description and pictures, the virtual fitting rooms allows the consumer to see the effect of the product in the real scene.

Our study is based the JD.com AR makeup function. JD.com is one of the most popular e-commerce platforms in China. Its mobile app deploys the AR make-up trying function, which allows users to try different beauty products in the VFR. The main interface of the AR make-up trying function contains two parts shown in Fig. 1 (a), the upper part is the product interaction area and the lower part is the product display area.

When users enter the VFR, they can choose a product to try on, as shown in Fig. 1 (b). Users can choose the type of product in Fig. 1 (b)-①, and the products belonging to this type will be shown in Fig. 1 (b)-②. When the user clicks and chooses a product to try on, the product title will be displayed in Fig. 1 (b)-③, and the experience effect of the product will be shown in the product interaction area on the user face in the corresponding position.

Decision Support Systems xxx (xxxx) xxx  
![](/api/attachments/5JZBS5GR/fulltext/images/892c1c91fa2bf18475c9a25efd42873ab02a872dd4357e2ea8298ef6dbcc1124.jpg)  
Fig. 1. The main page of JD.com AR make-up trying function.

In the product interaction area, they can adjust the effect of the cosmetics according to their preference, including turning on/off the beauty effect(Fig. 1 (c)-⑤), checking the comparison effect with and without the product(Fig. 1 (c)-⑥), and adjust the degree of product ef fect(Fig. 1 (a)-⑦). Fig. 1(c)-④ presents some notes about the AR func tion. In addition to selecting products by product type (Fig. 1(b)-①), users can also click Fig. 1(c)-\* to filter the products they want to try by other product attributes (Fig. 1(c)).

## 4. A recommendation framework in virtual fitting room

In this section, we present our recommendation model, named FEERS (Facial Expression-Enhanced Recommendation System), which assigns weights to personalized preferences and makes product recom mendations based on user interaction behaviors in the VFR.

## 4.1. Preliminaries

Firstly, we illustrate the basic concepts and symbols in Table 1. Suppose there are m users and n items, $\pmb { R } _ { m \times n }$ is the user-item interactions matrix, $r _ { u i }$ is an element of the matrix. $b _ { u i }$ is the number of user behav iors, including clicking to try, taking photos, going to the detail page, and adding to the shopping cart. When $b _ { u i } = 0 .$ , it means that the user u doesn't take any action on the product, i.e. doesn't click to try this product. When $b _ { u i } = 1$ , it means that user u clicks on product i to try it on AR. When $b _ { u i } > 1$ , it indicates that user u takes multiple interaction actions when interacting with product $i ,$ and the value of $b _ { u i }$ at this point indicates the number of actions taken. The time the user spends inter acting with the product is denoted by $t _ { u i } .$ . The user's facial emotion when interacting with the product is represented by $e _ { u i } ,$ , which is divided into three emotions: positive (P), negative (N), and medium (M).

Table 1  
The definitions of basic concepts and symbols.

<table><tr><td>Symbol</td><td>Meaning</td><td>Value/Unit</td></tr><tr><td> $R_{m \times n}$ </td><td>The user-item interactions matrix</td><td> $m \times n$ </td></tr><tr><td> $r_{ui}$ </td><td>One element of  $R_{m \times n}$ </td><td>0, 1</td></tr><tr><td> $b_{ui}$ </td><td>The number of behaviors of user u when interacting with the product i</td><td>0, 1, 2, 3, 4</td></tr><tr><td> $t_{ui}$ </td><td>The dwell time of user u&#x27;s interaction with the product i</td><td>s</td></tr><tr><td> $e_{ui}$ </td><td>The emotion of user u when interacting with the product i</td><td>P, M, N</td></tr><tr><td> $c_{ui}$ </td><td>The confidence for  $r_{ui}$ </td><td>[0,1]</td></tr><tr><td> $s_{fi}$ </td><td>The text similarity between product f&#x27;s and product i&#x27;s titles</td><td>[0,1]</td></tr></table>

## 4.2. Recommendation model

## 4.2.1. Framework

We design recommendation methods based on matrix factorization. Given a set of observed user-item interactions, the goal of our model is to obtain the interaction behavior $r _ { u i }$ and its confidence level $c _ { u i } ,$ , which is used to indicate the user's preference for the product. A user-item click interaction matrix can be obtained based on the click behavior, and weights are assigned to the values in the interaction matrix with the help of other interaction behaviors to indicate the user's preference level. Based on the final interaction matrix, by means of matrix factorization, we can recommend top K items with the highest scores for each user.

The most common measure of $r _ { u i }$ is whether the user u clicks to try the product i. Previous researches tend to consider it when the user likes this product, $r _ { u i } = 1 ,$ . Conversely, if the user u doesn't click to try the product $i ,$ it means the user dislikes this product, then $r _ { u i } = 0 .$ . This strategy treats all missing values as negative cases, namely AMAN (All Missing as Negative) [43]. Another strategy is AMAU (All Missing as

Unknown) [43], that means all missing values are left as missing data.

However, neither of these strategies is a good representation of the actual situation. In a real-world scenario, firstly, clicking is not equal to liking, users may click on a product to view detailed information but find they don't like it. Secondly, products that aren't clicked on by users don't necessarily have to be disliked by them either. The number of products available for online shopping is huge and there are many products that users do not see. Therefore, it is not accurate to set the values in the interaction matrix simply based on whether the user clicks or not. For the original positive feedback $( r _ { u i } = 1 )$ ), researchers proposed to assign confidence levels to the observations, such as the dwell time method [44]. Hu et al. [44] proposed to set the confidence proportional to video viewing duration to fill the missing data. For the original negative example $( r _ { u i } = 0 ) _ { i }$ , better methods are to conduct negative feedback sampling, such uniform sampling, user-oriented sampling, and itemoriented sampling [43]. Uniform sampling assumes each negative observation has the same probability of being positive or negative. The latter two sampling methods assign different negative feedback weights according to the number of positive feedbacks from users and items, respectively.

Existing studies have shown that different user behaviors have different effects on decision-making and prediction [45]. This study aims to analyze multiple interaction behaviors to complete interaction matrix and infer user preferences. Particularly, virtual fitting rooms can be used to collect facial expressions, which contain rich information directly indicating user preferences. As compared with implicit feed back, facial expression can better reflect use preferences and help addressing the missing data issue. Due to these reasons, this paper mainly studies how to use the implicit feedback information including facial expression to complete the interaction matrix and make recommendations.

The flow of the method proposed in this paper is shown in Fig. 2. First, distinguish between clicked and unclicked records. If product i is clicked by user $u ,$ then based on the user's facial emotion when inter acting with the product, it is further divided into positive, negative and neutral situations. Different emotions indicate different user prefer ences, and the confidence level is further determined by combining emotions and user interaction behaviors. For records that are not clicked, sampling of negative examples is performed, and sampling weights are determined based on the similarity between these product and the always-user negative example titles.

The core of our recommendation model is confidence setting and negative feedback sampling to weight user's multiple interactive behaviors in the virtual fitting room for recommendation. A detailed description of the confidence setting and the negative feedback sampling strategy follows.

## 4.2.2. Confidence setting strategy

## (1) Facial expression recognition and classification

As the most intuitive response, facial emotions can be a good expression of user preferences [46] on the product. This signal can be directly observed in the virtual fitting room.

In this paper, we apply Frame Attention Networks (FAN) [47], facial expression recognition method proposed in 2019 to identify users' emotions when trying the product. The model consists of two parts: the feature embedding module and the frame attention module. The input of the first module is a variable number of face images from the video and then using a deep CNN to generate a feature representation. The second module learns two levels of attention weights, self-attention and rela tional attention, and extracts attention weights from global and local features, respectively. Thus, the features of individual frames and the relationships between frames can be obtained. In the calculation pro cess, the emotion of each frame and the probability value can be ob tained, and the final emotion is calculated from each frame emotion and its probability.

The output of the model is one of the seven emotions of happy, angry, disgust, fear, sad, neutral, and surprise. We code output result to “positive” when the emotion is “happy” [48], when the emotion is “neutral”, it is coded as “neutral”, otherwise it is coded as “negative” [49]. Fig. 3. shows an example of the results of using an algorithm to identify user facial emotions.

![](/api/attachments/5JZBS5GR/fulltext/images/18e05ed4aa4a19383b9355d3b341174b8cf7c49359ede7a50878fa861c0784bf.jpg)  
Fig. 3. Examples of facial emotion recognition results.

![](/api/attachments/5JZBS5GR/fulltext/images/54f96ca200485ff54263b9c401d511917d0cb8b98c72ad7f3ded17ff1d55e932.jpg)  
Fig. 2. Overview of the proposed method for setting confidence.

## (2) Set confidence based on emotion and interaction behaviors

After completing the user emotion recognition by the above method, the confidence level is set separately according to the different emotion categories.

Firstly, user's facial emotions can directly indicate the user's prefer ences. Thus, when user u tries product i with positive facial emotion, it is assumed that the user really likes the product, at this point, $r _ { u i }$ is iden tified positive feedback, then $c _ { u i } = 1$ . When user u tries product i with negative facial emotion, the user tries the product, but finds that it is not what they really like, at this point, $r _ { u i }$ is identified negative feedback, then $c _ { u i } = 0 .$

Otherwise, if user u tries product i with a neutral facial emotion, we can't directly judge users' preferences. At this point, $r _ { u i }$ ’s confidence level needs further set.

When trying products, users also can go to the product detail page to see more information about product features and comments, and they can add the product to the cart. Furthermore, they can take photos of the product effect and save them or share them with others. The users take more interactions, and they are more likely to like the product. That is when the user u clicks to try product i, the bigger the b is, the more possibility the user like this product, then the bigger the confidence $c _ { u i }$ is. According to this, we assign the confidence as:

$$
c _ {u i} = 0. 5 + \alpha (b _ {u i} - 1), b _ {u i} \neq 0\tag{1}
$$

Constant $_ { 0 . 5 }$ is added to represent that, if the user u clicks to try product $i ,$ he/she has a 50% possibility of liking the product. The parameter $\alpha = 0 . 4$ is set according to the confidence level setting method in the literature [44].

Besides the number of behaviors, dwell time can also indicate the degree of preference of the user [50]. Wu et al. [51] argued that dwell time is an important indicator of user engagement and satisfaction. The more time user u spends on the product $i ( t _ { u i } ) _ { i }$ , the more he/she likes the product. Therefore, the confidence obtained from the number of be haviors and the dwell time is:

$$
c _ {u i} = t _ {u i} ^ {\prime} [ 0. 5 + \alpha (b _ {u i} - 1) ], b _ {u i} \neq 0\tag{2}
$$

$t _ { u i } ^ { ' }$ is the normalized dwell time $t _ { u i } ,$ the normalization method used is the one proposed in [50]:

① For each user $u ,$ collect the historical per-item dwell time and calculate the mean $\mu _ { u }$ and standard deviation $\sigma _ { u } .$

② For each product i clicked by each user $u ,$ the dwell time is $t _ { u i }$ calculate the z-value in log space: $z _ { u i } = \frac { l o g ( t _ { u i } ) - \mu _ { u } } { \sigma _ { u } }$

③ Calculate the normalized dwell time of the product i clicked by user u: $\dot { t _ { u i } } = e x p ( \mu _ { u } + \sigma _ { u } \times z _ { u i } )$

In summary, when $b _ { u i } \neq 0 ,$ , the confidence set for $r _ { u i } = 1$ is:

$$
c _ {u i} = \left\{ \begin{array}{c c} 1 & , e _ {u i} = P \\ t _ {u i} ^ {\prime} [ 0. 5 + \alpha (b _ {u i} - 1) ] & , e _ {u i} = M \\ 0 & , e _ {u i} = N \end{array} \right.\tag{3}
$$

## 4.2.3. Negative feedback sampling strategy

For the missing values, we employ sampling methods to fill such negative feedbacks. In this research context, we also have the title of the product, which contains much information about the product. The product title often has much information about product features in order to make search convenient. As shown in Fig. 4, the product title contains the product's brand (the red part in Fig. 4), type (the green part in Fig. 4), suitable people and other features (the purple part in Fig. 4). The text information can be on behalf of the product's basic features and can help users to make purchase decisions. Therefore, this paper samples nega tive feedback by calculating the title similarity.

In Section $4 . 2 . 2 ,$ we have found products that users really don't like by their facial expressions (identified negative feedback). The confi dence level of user u not clicking on the negative example is obtained by calculating its similarity to the title of the negative feedback product identified by user u. If user u has k identified negative feedback, the confidence for unidentified negative feedback $r _ { u i }$ is the average text similarity between the title of the product i and the titles of all identified negative feedbacks. That is:

$$
c _ {u i} = \frac {\sum_ {f = 1} ^ {k} S _ {f i}}{k}\tag{4}
$$

$s _ { f i }$ is the text similarity between the title of product f (identified negative feedback) and product i (unidentified negative feedback). Before calculating the similarity, first, remove the useless information at the end of the title text, then perform the word separation and vector transformation, use the TF-IDF algorithm to model the corpus, and finally calculate the cosine similarity.

In combination with the above analysis, the overall confidence is set as follows:

$$
c _ {u i} = \left\{ \begin{array}{c c} 1 & , b _ {u i} \neq 0 \text {   and   } e _ {u i} = P \\ 0 & , b _ {u i} \neq 0 \text {   and   } e _ {u i} = N \\ t _ {u i} ^ {\prime} [ 0. 5 + \alpha (b _ {u i} - 1) ] & , b _ {u i} \neq 0 \text {   and   } e _ {u i} = M \\ \frac {\sum_ {f = 1} ^ {k} s _ {\bar {f} i}}{k} & , b _ {u i} = 0 \end{array} \right.\tag{5}
$$

After assigning the confidence levels to the interaction matrix ac cording to the above strategy, the initial matrix is divided into one user matrix $X _ { m \times k }$ and one item matrix $Y _ { n \times k }$ our goal is to predict $r _ { u i } ,$ , which is done by an inner product, $r _ { u i } = x _ { u } y _ { i } ^ { T }$ . Our model's loss function is as follows:

$$
L = \min \sum_ {u, i} c _ {u i} \left(r _ {u i} - x _ {u} ^ {T} y _ {i}\right) ^ {2} + \lambda \left(\sum_ {u} \| x _ {u} \| ^ {2} + \sum_ {i} \| y _ {i} \| ^ {2}\right)\tag{6}
$$

## 4.3. Learning process of the proposed model

The model is trained by alternation least squares (ALS) for implicit feedback [52]. First, we update $x _ { u }$ by calculate $\begin{array} { r } { \frac { \partial L } { \partial x _ { u } } = 0 , } \end{array}$ , the function is obtained as function (7):

$$
x _ {u} = \left(Y ^ {T} C ^ {u} Y + \lambda I\right) ^ {- 1} Y ^ {T} C ^ {u} r (u)\tag{7}
$$

In function $( 7 ) , C ^ { u }$ is a diagonal n × n matrix where $C _ { i i } ^ { u } = c _ { u i }$ , and the vector r(u) contains all the preferences by user u.

Fig. 4. The example of the product title.

Then update $y _ { i } ,$ in a similar way to update $x _ { u } ,$ the function is obtained as function (8):

$$
y _ {i} = \left(X ^ {T} C ^ {i} X + \lambda I\right) ^ {- 1} X ^ {T} C ^ {i} r (i)\tag{8}
$$

And $c ^ { i }$ is a diagonal m × m matrix where $C _ { u u } ^ { i } = c _ { u i } ,$ , and the vector r(i) contains all the preferences for item i. The algorithm solution process is shown in Table 2.

After getting the best latent feature matrix $X _ { m \times k }$ and $Y _ { n \times k } , r _ { u i }$ can be calculated by inner product, $r _ { u i } = x _ { u } y _ { i } ^ { T }$ . That is the user u’s preference for product i predicted by the proposed model. Then, based on the predicted $r _ { u i } ,$ for each user, we can sort the items that he/she might like and recommend the top-k products to the user.

## 5. Experiment and evaluation

We designed experiments based on the Design of Experiments (DoE) method [53] to collect data and verify whether the user interaction behavior in the proposed method can help personalize recommenda tions. The experimental design [54] is shown in Fig. 5.

## 5.1. User experiment design

To verify the effectiveness of the user interactions utilized in Section 4 for personalized recommendations, a user experiment was conducted to collect data on user interactions.

## 5.1.1. Data collection

A total of 82 paid participants were recruited, all of whom were students at colleges and universities. Because the scenario of the experiment was to select cosmetics, the participants were all female and facial veiling was required during the experiment.

First, all participants were asked to fill out a questionnaire. The content included basic demographic information, as well as the partic ipants' familiarity with VFR and beauty products. Then, using their own cell phones, participants entered the VFR system on the JD.com platform and began to try and select products freely. This process does not limit time or products, participants only need to select in the VFR according to their own habits and preferences.

Objective: Verifying the role of user interaction behavior on personalized recommendation in VFR

![](/api/attachments/5JZBS5GR/fulltext/images/a68b99b46d4940dc588443a203e3c808ce3c8d5934e7d13b7638bdd36f1ece44.jpg)  
Fig. 5. The design of the experiment.

The experimental data was recorded by using cell phone screen recording. That is, to record the whole process and operation from the participants entering the virtual fitting room to the exit, including all behaviors such as clicking and adding on the cell phone screen, and the facial information of the participants when trying the products. After the experiment, each participant's recorded video is segmented by product and manually recorded and processed into “user-product-interaction” data, which will be used as input data for personalized recommendations.

The experiment was conducted from January 5 to January 18, 2022, in a fixed classroom at a university. To avoid the effect of light on the trial effect, the, we conduct experiments during 9:30–16:30 every day.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Pseudocode of ALS algorithm.

Algorithm 1.

Input: The user-item interactions matrix  $R_{ui}$ , k,  $\lambda$ , the confidence matrix  $C_{ui}$ 

Output: Latent feature matrix  $X_{m\times k}$  and  $Y_{n\times k}$ 

Initialize  $X_{m\times k}$  and  $Y_{n\times k}$  at random

Repeat:

Fix  $Y_{n\times k}$  and optimize all  $x_{u}$  using function (6)

Fix  $X_{m\times k}$  and optimize all  $y_{i}$  using function (7)

Until convergence

Return: The best latent feature matrix  $X_{m\times k}$  and  $Y_{n\times k}$ 

End
</div>

In addition, each user has a separate experiment space to ensure that they are not influenced by others.

## 5.1.2. Recommendation and result feedback

The processed data is used as the input of the recommendation al gorithm, and the recommendation list is generated using the FEERS method and other baseline algorithms proposed in this paper, respec tively. The top-2 products in the recommendation list of each algorithm are taken, and the duplicate products are removed to form the final recommendation list for this user. The final recommendation list was sent to each participant by email, asking them to select their preferred product from the list based on their preferences and return that result, which forms the gold standard for evaluation. The whole process of the user experiment is shown in Fig. 6.

## 5.1.3. Data statistics

JD.com virtual fitting room has 7 types of beauty products, including 3263 beauty products. Including 2279 lipsticks, 347 foundations, 215 eyebrow pencils, 129 eyeliners, 128 eyeshadows, 83 mascaras and 82 blush products. The processed user experiment data had 81 participants (one user's data is broken) interacting with 372 products with 2816. Each user interacts with an average of 35 products.

For interaction behaviors, including clicking to try, taking photos, going to the detail page, and adding to the cart. In addition, the user's expression was recognized by the facial expression recognition algo rithm introduced in 4.2.2, and the time spent by the participant inter acting with each product was recorded, with an average dwell time of 3.5 s.

## 5.2. Baselines

The baselines are shown as follows.

(1) Popularity Based Recommendation Method. Recommend the most popular products for users. The product popularity is calculated based on the user interactions with the product, and we use the method proposed in. First, count the number of times product i appears in the interaction record, $f _ { i \cdot }$ . Then calculate the product popularity $p _ { i } = \frac { f _ { i } } { \sum _ { i = 1 } ^ { m } f _ { i } } .$

(2) AMAN Sampling Strategy [43]. It means All Missing as Negative. For missing data, the most general method is to regard all of them as negative feedback, so early studies make the AMAN assump tion. That is when user u clicks to try product i, the user likes the product, $r _ { u i } = 1$ , otherwise, user u doesn't like the product, $r _ { u i } =$ 0. And the confidence of all $r _ { u i } \mathrm { i } s 1 , c _ { u i } = 1$

(3) Average Sample Strategy. This method is proposed in [43]. Its basic assumption is that missing data being negative feedback has an equal chance overall users or all items, so it uniformly assigns a confidence $\delta \in [ 0 , 1 ]$ for “negative” feedback. That is when user u clicks to try product i, the user likes the product, $r _ { u i } = 1 , c _ { u i } = 1$ Otherwise, $r _ { u i } = 0 ,$ , and $c _ { u i } = \delta , \delta \in [ 0 , 1 ]$ , and follows a uniform distribution.

(4) BERS (Behavior Enhanced Recommendation System). The methods above only set confidence for negative feedback, from this method, we consider the users' behaviors to set confidence for the positive feedback. As described in 3.3.1, we use users' interaction behaviors to set confidence for unidentified positive feedback. BERS only uses the user interaction behaviors.

(5) DTERS (Dwell Time Enhanced Recommendation System). DTERS uses the user interaction behaviors and dwell time to set confi dence for unidentified positive feedback.

## 5.3. Evaluation metrics

After sending the mixed recommendation list to users and receiving their feedback, the products in the mixed recommendation list are cor responded to the lists obtained by different recommendation methods according to the preferred products selected by users, and the different baselines are evaluated according to the preferred products selected by users.

![](/api/attachments/5JZBS5GR/fulltext/images/7d669a59f900c8b24d298fc2a914814caa7c311c7bd9dfd3a000d0fd438fa83f.jpg)  
Fig. 6. The whole process of the user experiment.

In this paper, two widely used metrics were employed to evaluate the performance of the recommendation approaches, Precision and MAP (Mean Average Precision). Precision is used to measure the extent to which the recommendation algorithm correctly predicts what users will like about a product. That is the percentage of products in the recom mendation list that the user selected.

$$
\text { Precision } = \sum_ {u = 1} ^ {m} \frac {\left| R _ {u} \cap T _ {u} \right|}{R _ {u}}\tag{9}
$$

In the above equation, $R _ { u }$ is the recommended products for user u, and $T _ { u }$ is the selected products for user u.

Additionally, to consider the order in the list when evaluating, MAP is also used. MAP is originally an evaluation metric used in the field of information retrieval to measure the ranking performance of search engines, and for recommendation Systems, the recommendation list can be considered as a ranked list. It can be divided into P, AP, and MAP, P i precision, and AP (Average Precision) takes into account the list location factor which calculates the average Precision for each position. And MAP is the average of all the users' AP. The equations are as follows, where $A P _ { u }$ represents the AP-value of user u, k represents the kth posi tion in user u<sup>’</sup>s recommendation list and K represents the length of user u<sup>’</sup>s recommendation list. Precision denotes the precision of the rec ommended result for user u at k.

$$
A P _ {u} = \sum_ {k = 1} ^ {K} P r e c i s i o n _ {u k} \times \frac {1}{k}\tag{10}
$$

$$
M A P = \sum_ {u = 1} ^ {m} A P _ {u}\tag{11}
$$

## 6. Result and analysis

## 6.1. Overall performance

We calculate the Precision and MAP value of the six methods, and the results are shown in Table 3. It is apparent that our proposed method achieves the best performance in both Precision and MAP metrics. Our method significantly outperforms the first three baselines, indicating that it is better than typical methods. Compared with the latter two baselines, it shows that the user behavior and confidence setting method we used are effective. DTERS and BERS ranked second and third, respectively, indicating that both the number of user interactions and dwell time have a positive impact on the recommendation. The popularity-based recommendation method is better than AMAN, and the possible reason is that the products with high popularity are the ones that users click to try more and meet the preference of most users. The AMAN and Average s

ample methods have the worst performance, indicating that only using the implicit feedback behavior of user clicks for recommendation is unreliable.

In addition, for our experimental data, the results of the two methods (AMAN and Average) are identical. The possible reason is that the sample size of our data is small, resulting in uniform sampling having less impact on sample selection, so the results of Average are the same as the AMAN method.

Table 3  
Overall performance of recommendation methods.

<table><tr><td>Methods</td><td>Precision</td><td>MAP</td></tr><tr><td>Popularity-based</td><td>0.698</td><td>0.648</td></tr><tr><td>AMAN</td><td>0.636</td><td>0.580</td></tr><tr><td>Average</td><td>0.636</td><td>0.580</td></tr><tr><td>BERS</td><td>0.698</td><td>0.664</td></tr><tr><td>DTERS</td><td>0.704</td><td>0.630</td></tr><tr><td>FEERS</td><td>0.803</td><td>0.756</td></tr></table>

## 6.2. Performance on different user types

To further verify the effectiveness of our proposed method, we analyze the performance of the recommendation results for different types of users.

First, according to the personality information obtained from the user questionnaire, users with different education, different experience in using virtual fitting rooms and different familiarity with beauty products are analyzed separately. The number of users in different cat egories is shown in Fig. 7.

The Precision and MAP results of different algorithms in different groups of users are shown in Fig. 8. Take Fig. 8-(a) as an example, the vertical coordinate is the precision value, the horizontal coordinate is different categories of users, different dashes indicate different recom mendation algorithms (example: the recommendation precision of different algorithms for users who have not used the VFR). Thus, com bined with the graphs, it can be obtained that the FEERS method ach ieves the best results for different types of users in both precision and MAP metrics. It shows that the user's familiarity with the experimental environment and the product does not affect the performance of the proposed method

Since data features can affect the performance of the recommenda tion algorithm, we also analyze the performance of the recommendation results based on user interaction data. Including the number of products users interacted with, the number of interaction behaviors, and the average interaction time per product, we analyze different levels of user recommendation results based on the number of the above behaviors, respectively. Fig. 9. shows the recommended Precision of several methods for different groups of users under different groupings. Taking Fig. 9-(a) as an example, users are divided into three groups according to the number of interactive products, different dashes indicate differen recommendation algorithms. From Fig. 9, it can be seen that the preci sion values of the FEERS method in all three classification cases basically reach the highest value for each group.

The results show that our method can achieve good precision regardless of whether the user interaction data is large or small. And the results show that for users with more interaction data, the recommen dation results are better, which is also in line with the general rules of the recommendation algorithm.

The analysis of the above results can prove that our proposed method is better than other algorithms in terms of precision and MAP. Further, we conduct the Mann-Whitney U test was employed to assess the dif ferences between the proposed method and other methods. The results are shown in Table 4. The test results further prove that the Precision of the proposed method is significantly higher than that of other methods. We therefore conclude that our proposed method statistically signifi cantly outperforms other methods in terms of recommendation accuracy.

![](/api/attachments/5JZBS5GR/fulltext/images/100897e2f914164820c9770dea4fb68f5fb8fea20c0f912399a311cec0cdc832.jpg)  
Fig. 7. User type and number.

![](/api/attachments/5JZBS5GR/fulltext/images/ff34e4d6a9fd829a2b55f1c8c44456d52f6243049de7e9a95360af5d7a6f8bff.jpg)  
(a)

![](/api/attachments/5JZBS5GR/fulltext/images/da16043ff3a93a6f9c8a55a2b2b427dbbb5c2cd0e20a6d914943b47b3c33508b.jpg)  
(b)  
Fig. 8. Precision and MAP values of users with different personal characteristics.

## 6.3. Performance on recommendation popularity and diversity

Pursuing only high accuracy may lead to problems such as reduced diversity and the information cocoon effect, which may reduce the satisfaction of users [55,56]. Therefore, we further calculated the product popularity and diversity of the recommendation lists generated by each recommendation algorithm, to evaluate the ability of the pro posed method in terms of beyond-accurate.

According to the method of calculating product popularity different in 5.1.3, we calculated the average popularity of the products in the recommendation lists generated by recommendation algorithms. The diversity can be evaluated by Hamming distance [57], the formula is as follows,

$$
\mathrm{H} _ {i j} = 1 - \frac {Q _ {i j}}{L}\tag{12}
$$

L is the length of the recommendation list $Q _ { i j }$ indicates the number of identical items in the recommendation list for user i and j. Hamming distance measures the variability of the recommendation results among different users, and the larger the value, the higher the diversity among different users. We use the mean value of Hamming distance,

$$
S = \frac {1}{m (m - 1)} \sum_ {i \neq j} H _ {i j}\tag{13}
$$

Table 5 reports the popularity and diversity performance the six recommendation methods. For popularity, the proposed method ach ieves the lowest recommended result of 0.072 for popularity. For di versity, our method is second only to the DTERS method at 0.628. This is reasonable because when the accuracy is increased, some diversity is sacrificed [58], but our method still achieves accuracy and higher di versity to some extent. In summary, the proposed method also performs well on the beyond-accuracy metric and is able to recommend some unpopular and diverse products.

## 6.4. Case study

In order to analyze the role of user expression in mining user pref erences, we analyze an example of user interactions, recommendations and feedback results.

Take the third participant for example, 50% of the products he interacted with were lipstick products, while the rest were eyebrow pencils, blushers and eye shadows. Among them, the top three brands in the lipstick category were Armani, YSL and Colorkey. The recommen dation results for user 3# obtained by FEERS and DTERS algorithms are shown in Table 6. As the table describes. the first two products in the recommendation list obtained by our proposed method are Armani's lipstick products, one is more popular and the other is less popular. The latter two lipstick categories are MAC and Chioture two brands, where MAC and Armani for the price, positioning similar brands, Chioture and Colorkey for similar brands. Compared with the FEERS method, the top two products of the recommendation list obtained by the DTERS method are products of other categories. It can be obtained that the method proposed in this paper can indeed capture the relevant information expressed by the user's emotion to predict the user's preference.

According to the experimental feedback results, user 3 selected a total of five favorite products (item\_id: 760, 878, 898, 2450, 2453) from the recommendation list, two of which were the first two products in the recommendation list obtained by the proposed method. This case study visually demonstrates the effectiveness of the proposed method in terms of accuracy and diversity of recommendations.

## 7. Conclusion

VFR has been widely used in e-commerce, but no personalized recommendation method adapted to this environment has been pro posed. In this paper, FEERS is proposed to perform personalized rec ommendations in VFR. The method uses the user's interaction behavior in the virtual environment, especially the facial expressions specific to that environment, to analyze and predict the user's preferences. The user's preference is first determined based on the user's facial expression, and then a new confidence calculation and negative example sampling method is designed to predict the user's preference and solve the implicit feedback problem in the recommendation process. The effectiveness of the proposed method was verified by conducting user experiments (N = 82). It is demonstrated that users' facial expressions and other interaction behaviors during virtual fitting room interactions can help predict user preferences and make product recommendations. This paper proposes a preference prediction and product recommendation method applicable to virtual fitting room environments, which provides support for personalized recommendation in new shopping environments.

![](/api/attachments/5JZBS5GR/fulltext/images/501e2ff0e973d887ad6bd73160666c2c735e22c85fe6bf3c4b417a7ea7a5886c.jpg)

![](/api/attachments/5JZBS5GR/fulltext/images/83551c707cb18893e78321a2e38e3d1bb94e0bcbd3337f00468b35d9ef687da0.jpg)  
Fig. 9. Precision values of users with different levels.

![](/api/attachments/5JZBS5GR/fulltext/images/53683fc49ee1a7479a762509c887bdf7ca73647faad6faa0968fe45c860f0d95.jpg)

Table 4  
Results of Mann-Whitney U test.

<table><tr><td rowspan="2"></td><td colspan="4">Score</td></tr><tr><td>FEERS vs. Popu</td><td>FEERS vs. AMAN</td><td>FEERS vs. BERS</td><td>FEERS vs. DTERS</td></tr><tr><td>Mann-Whitney U</td><td>10</td><td>8</td><td>20</td><td>7</td></tr><tr><td>Wilcoxon W</td><td>88</td><td>86</td><td>98</td><td>85</td></tr><tr><td>Z</td><td>-3.582</td><td>-3.696</td><td>-3.004</td><td>-3.757</td></tr><tr><td>Asymp.Sig.(2-tailed)</td><td>0.000***</td><td>0.000***</td><td>0.003**</td><td>0.000***</td></tr></table>

$P < 0 . 0 1 $ Represents significance a  
Represents significance at $P < 0 . 0 0 1 .$

Table 5  
Performance on recommendation popularity and diversity.

<table><tr><td>Baseline</td><td>Popularity</td><td>Diversity</td></tr><tr><td>Popularity based</td><td>0.144</td><td>0.000</td></tr><tr><td>AMAN</td><td>0.081</td><td>0.141</td></tr><tr><td>Average</td><td>0.081</td><td>0.141</td></tr><tr><td>BERS</td><td>0.089</td><td>0.576</td></tr><tr><td>DTERS</td><td>0.082</td><td>0.782</td></tr><tr><td>FEERS</td><td>0.072</td><td>0.628</td></tr></table>

This research also provides practical implications for decision sup port in immersive shopping environments such as virtual fitting rooms. Merchants can more directly understand users' real preferences based on their facial expressions and other interactive behaviors in virtual fitting room environments. Personalized marketing helps users reduce search costs and assists decision-making, while promoting purchases and increasing merchant revenue. In addition, it helps to improve the user profile, providing a basis for further data analysis and decision-making.

This research has some limitations. First, due to the lack of public dataset, we conduct experimental validation only through the method of user experimentation. Secondly, deep learning methods have been bet ter developed and applied in the field of personalized recommendation, while this paper is limited by the amount of data, and in order to more directly analyze the role of user interaction behavior on the recom mendation. the traditional matrix decomposition method is used. and it is planned to be further optimized in the follow-up work. Furthermore, the method proposed in this paper is only based on the user's behavior in VFR and does not take into account other external information, such as product information.

For future work, firstly, the experimental dataset can be expanded through cooperation and other means, and external information such as product information and user reviews can be added to assist personal ized recommendation. Second, deep learning tools will be employed to predict user preferences and provide a better basis for recommendation decisions.

## Declaration of Competing Interest

The authors declare the following financial interests/personal re lationships which may be considered as potential competing interests:

Jianshan Sun reports financial support was provided by National Natural Science Foundation of China.

Table 6  
The top-5 products in the recommendation list obtained by both FEERS and DTERS.

<table><tr><td colspan="4">FEERS</td><td colspan="4">DTERS</td></tr><tr><td>Item_id</td><td>Type</td><td>Brand</td><td>Popularity</td><td>Item_id</td><td>Type</td><td>Brand</td><td>Popularity</td></tr><tr><td>2453</td><td>lipstick</td><td>Armani</td><td>0.094</td><td>405</td><td>eyebrow pencil</td><td>Kiss me</td><td>0.091</td></tr><tr><td>2450</td><td>lipstick</td><td>Armani</td><td>0.046</td><td>682</td><td>eye shadow</td><td>Maridega</td><td>0.135</td></tr><tr><td>480</td><td>blush</td><td>NARS</td><td>0.015</td><td>2453</td><td>lipstick</td><td>Armani</td><td>0.094</td></tr><tr><td>1180</td><td>lipstick</td><td>Chioture</td><td>0</td><td>2234</td><td>lipstick</td><td>MAC</td><td>0.115</td></tr><tr><td>2194</td><td>lipstick</td><td>MAC</td><td>0</td><td>1386</td><td>lipstick</td><td>Colorkey</td><td>0.057</td></tr></table>

## Data availability

Data will be made available on request.

## Acknowledgement

This work is supported by the National Natural Science Foundation of China (72271083, 72071069, 72271084, 72101076, and 72101072), the Fundamental Research Funds for the Central Universities (JZ2023YQTD0075) and National Engineering Laboratory for Big Data Distribution and Exchange Technologies.

## References

[1] R. Skibba, Virtual reality comes of age, Nature. 553 (2018) 402–403, https://doi. org/10.1038/d41586-018-00894-w.

[2] R.T. Azuma, A survey of augmented reality, presence, Teleoperators Virtua Environ. 6 (1997) 335–385, https://doi.org/10.1162/pres.1997.6.4.355.

[3] A.R. Philipp, R. Felix, C. Hinsch, H. Shahab, F. Alt, What is XR? Towards a framework for augmented and virtual reality, Comput. Hum. Behav. 133 (2022), https://doi.org/10.1016/j.chb.2022.107289, 107289.

[4] G. McLean, A. Wilson, Shopping in the digital world: examining customer engagement through augmented reality mobile applications, Comput. Hum. Behav. 101 (2019) 210–224, https://doi.org/10.1016/j.chb.2019.07.002.

[5] J. Neve, R. McConville, ImRec: Learning reciprocal preferences using images, in: BecSvs ‘20. 2020 pp. 170–179, https://doi org/10.1145/3383313.3411476

[6] K.-S. Suh, Y.E. Lee, The effect of virtual reality on consumer learning: an empirical investigation, MIS Q. 29 (2005) 673–697, https://doi.org/10.2307/25148705.

[7] C. Vonkeman, T. Verhagen, W. van Dolen, Role of local presence in online impulse buying, Inf. Manag. 54 (2017) 1038–1048, https://doi.org/10.1016/j. im.2017.02.008.

[8] Y.-C. Tan, S.R. Chandukala, S.K. Reddy, Augmented reality in retail and its impact on sales, J. Mark. 86 (2022) 48–66, https://doi.org/10.1177/0022242921995449.

[9] J. Bin Whang, J.H. Song, B. Choi, J.-H. Lee, The effect of augmented reality on purchase intention of beauty products, J. Bus. Res. 133 (2021) 275–284, https:// doi.org/10.1016/j.jbusres.2021.04.057.

[10] B. Huynh. A. Ibrahim. Y.S. Chang, T. Höllerer, J. O'Donovan. A Study of Situated Product Recommendations in Augmented Reality. in: 2018 JEEE Int Conf Artif Intell Virtual Real. 2018. pp. 35–43. https://doi,org/10.1109/AIVR.2018.00013.

[11] E. Olshannikova, A. Ometov, Y. Koucheryavy, T. Olsson, Visualizing big data with augmented and virtual reality: challenges and research agenda, J. Big Data. 2 (2015)1–27, https://doi.org/10.1186/s40537-015-0031-2.

[12] B. Ejder, B. Mehdi, M. Muriell, D. Merouane, Towards interconnected virtual reality: opportunities, challenges and enablers, IEEE Commun. Mag. 55 (2017) 110–117, https://doi.org/10.1109/MCOM.2017.1601089.

[13] J. Scholz, K. Duffy, We ARe at home: how augmented reality reshapes mobile marketing and consumer-brand relationships, J. Retail. Consum. Sery. 44 (2018) 11–23. https://doi.org/10.1016/i.iretconser,2018.05.004.

[14] P. Vandith, K. Warut, A. Karthik, The impact of an augmented-reality game on local businesses: a study of Pokemon go on restaurants, Inf, Syst. Res, 32 (2021) 950–966, https://doi.org/10.1287/isre.2021.1004

[15] H. Oin, B. Osatuvi, L. Xu, How mobile augmented reality applications affect continuous use and purchase intentions: a cognition-affect-conation perspective. J. Retail. Consum. Sery, 63 (2021) 102680, https://doi.org/10.1016/j. jretconser.2021.102680.

[16] A. Butt, H. Ahmad, A. Muzaffar, F. Ali, N. Shafique, WOW, the make-up AR app is impressive: a comparative study between China and South Korea, J. Serv. Mark. 36 (2021).73–88, https://doi org/10.1108/JSM-12-2020-0508

[17] C.-S. Wang, An AR mobile navigation system integrating indoor positioning and content recommendation services, in: World Wide Web, 2019, pp. 1241–1262, https://doi.org/10.1007/s11280-018-0580-3.

[18] J. Zhou, K. Yamamoto, Development of the system to support tourists’ excursion behavior using augmented reality, Int. J. Adv. Comput. Sci. Appl. 7 (2016) 197–209, https://doi.org/10.14569/IJACSA.2016.070727.

[19] H. Lee, Y. Xu, Classification of virtual fitting room technologies in the fashion industry: from the perspective of consumer experience, Int. J .Fash. Des. Technol. Educ. 13 (2019) 1–10, https://doi.org/10.1080/17543266.2019.1657505.

[20] A.M. Pereira, J.A.B. Moura, E.D.B. Costa, T. Vieira, A.R.D.B. Landim, E. Bazaki V. Wanick, Customer models for artificial intelligence-based decision support in fashion online retail supply chains, Decis. Support. Syst. 158 (2022) 113795, https://doi.org/10.1016/j.dss.2022.113795.

[21] A. Javornik, Augmented reality: research agenda for studying the impact of its media characteristics on consumer behavior, J. Retail. Consum. Serv. 30 (2016) 252–261, https://doi.org/10.1016/j.jretconser.2016.02.004.

[22] E. Pantano, Successful Technological Integration for Competitive Advantage in Retail Settings, Business Science Reference, London, 2015.

[23] Y.C. Huang, K.F. Backman, S.J. Backman, L.L. Chang, Exploring the implications of virtual reality technology in tourism marketing: an integrated research framework, Int. J. Tour. Res. 18 (2016) 116–128, https://doi.org/10.1002/jtr.2038.

[24] I. Yu, J. Mortensen, P. Khanna, B. Spanlang, M. Slater, Visual realism enhances realistic response in an immersive virtual environment, IEEE Comput. Graph. Appl. 32 (2012) 36–45, https://doi.org/10.1109/MCG.2012.121.

[25] Y.K. Choi, C.R. Taylor, How do 3-dimensional images promote products on the internet? J. Bus. Res. 67 (2014) 2164–2170, https://doi.org/10.1016/j. jbusres.2014.04.026.

[26] V. Arghashi, C.A. Yuksel, Interactivity, inspiration, and perceived usefulness! How retailers’ AR-apps improve consumer engagement through flow, J. Retail. Consum. Serv. 64 (2022), https://doi.org/10.1016/j.jretconser.2021.102756, 102756.

[27] A. Jessena, T. Hilken, M. Chylinski, D. Mahr, J. Heller, D.I. Keeling, K. de Ruyter, The plavground effect: how augmented reality drives creative customer engagement, J. Bus. Res. 116 (2020) 85–98, https://doi.org/10.1016/j. jbusres.2020.05.002.

[28] H. Van Kerrebroeck, M. Brengman, K. Willems, When brands come to life: experimental research on the vividness effect of virtual reality in transformational marketing communications, Virtual Reality 21 (2017) 177–191, https://doi.org 10.1007/s10055-017-0306-3

[29] S.A. Bone, K.N. Lemon, C.M. Voorhees, K.A. Liljenquist, P.W. Fombelle, K. B. Detienne, R.B. Money, "Mere measurement plus": how solicitation of open ended positive feedback influences customer purchase behavior. J. Mark. Res. 54 (2017).156–170. https://doi.org/10.2307/44878496.

[30] B.K. Jiyeon, F. Sandra, Adoption of virtual try-on technology for online apparel shopping, J. Interact, Mark, 22 (2008) 45–59. https://doi,org/10.1002/dir,20113

[31] M.Y.-C. Yim, S.-C. Chu, P.L. Sauer, Is augmented reality technology an effective tool for E-commerce? An interactivity and vividness perspective, J. Interact. Mark. 39 (2017) 89–103, https://doi.org/10.1016/i.intmar.2017.04.001

[32] S. Francesca, V. R´egine, V. Milena, Does product involvement drive consumer flow state in the AR environment? A study on behavioural responses, J. Retail. Consum. Serv. 72 (2023), https://doi.org/10.1016/j.jretconser.2023.103279, 103279.

[33] B. Jin, S.-A. Annie, The roles of modality richness and involvement in shopping behavior in 3D virtual stores, J. Interact. Mark. 23 (2009) 234–246, https://doi. org/10.1016/j.intmar.2009.04.005.

[34] R. Zimmermann, D. Mora, D. Cirqueira, M. Helfert, M. Bezbradica, D. Werth, W J. Weitzl, R. Riedl, A. Auinger, Enhancing brick-and-mortar store shopping experience with an augmented reality shopping assistant application using personalized recommendations and explainable artificial intelligence, J. Res. Interact. Mark. 17 (2022) 273–298, https://doi.org/10.1108/JRIM-09-2021-0237.

[35] T. Joerß, S. Hoffmann, R. Mai, P. Akbar, Digitalization as solution to environmental problems? When users rely on augmented reality-recommendation agents, J. Bus. Res. 128 (2021) 510–523, https://doi.org/10.1016/j.jbusres.2021.02.019.

[36] J. Ahn, J. Williamson, M. Gartrell, R. Han, Q. Lv, S. Mishra, Supporting healthy grocery shopping via mobile augmented reality, ACM Trans. Multimed. Comput. Commun. Appl. 12 (2015) 1–24, https://doi.org/10.1145/2808207.

[37] E. Cruz, S. Orts-Escolano, F. Gomez-Donoso, C. Rizo, J.C. Rangel, H. Mora, M. Cazorla. An augmented reality application for improving shopping experience in large retail stores, Virtual Reality 23 (2019) 281–291, https://doi.org/10.1007 s10055-018-0338-3.

[38] J.O.A. <sup>´</sup> M´arquez, J. Ziegler, In-store augmented reality-enabled product comparison and recommendation, in: RecSys ‘20 Proc 14th ACM Conf Recomm Syst, 2020, pp. 180–189, https://doi.org/10.1145/3383313.3412266.

[39] M. Torres-Ruiz, F. Mata, R. Zagal, G. Guzman, ´ R. Quintero, M. Moreno-Ibarra, A recommender system to generate museum itineraries applying augmented reality and social-sensor mining techniques, Virtual Reality 24 (2020) 175–189, https:// doi.org/10.1007/s10055-018-0366-z

[40] S. Kalloori, R. Chalumattu, F. Yang, S. Klingler, M. Gross, Towards Recommender Systems in Augmented Reality for Tourism, in: J Retail Consum Sery. 2023. pp. 267–272. https://doi.org/10.1007/978-3-031-25752-0 29

[41] G. Hiranandani, K. Ayush, C. Varsha, A. Sinha, P. Maneriker, S.V.R. Maram, [POSTER] enhanced personalized targeting using augmented reality, in: 2017 IEEE

Int Symp Mix Augment Real, 2017, pp. 69–74, https://doi.org/10.1109/ISMAR-Adjunct.2017.34.

[42] I.N.S.K. Andersen, A.A. Kraus, C. Ritz, W.L.P. Bredie, Desires for beverages and liking of skin care product odors in imaginative and immersive virtual reality beach contexts, Food Res. Int. 117 (2019) 10–18, https://doi.org/10.1016/j. foodres.2018.01.027.

[43] R. Pan, Y. Zhou, B. Cao, N.N. Liu, R. Lukose, M. Scholz, Q. Yang, One-clas collaborative filtering, in: Proc 2008 Eighth IEEE Int Conf Data Min (ICDM ‘08) 2008, pp. 502–511, https://doi.org/10.1109/ICDM.2008.16.

[44] Y. Hu, Y. Koren, C. Volinsky, Collaborative filtering for implicit feedback datasets, in: 2008 Eighth IEEE Int Conf Data Min, 2008, pp. 263–272, https://doi.org/ 10.1109/ICDM.2008.22.

[45] N. Wang, Y. Liu, S. Xiao, Which feedback matters? The role of expressions and valence in continuous high-quality knowledge contribution in the online Q&A community, Decis. Support. Syst. 156 (2022) 113750, https://doi.org/10.1016/j. dss.2022.113750.

[46] X. Su, M. Gao, J. Ren, Y. Li, M. R¨atsch, Personalized clothing recommendation based on user emotional analysis, Discret. Dyn. Nat. Soc. 2020 (2020) 1–8, https: doi.org/10.1155/2020/7954393

[47] D. Meng, X. Peng, K. Wang, Y. Qiao, Frame attention networks for facial expression recognition in videos, in: 2019 IEEE Int Conf Image Process, 2019, pp. 3866–3870, https://doi.org/10.1109/ICIP.2019.8803603.

[48] S. Jaiswal, S. Virmani, V. Sethi, K. De, P.P. Roy, An intelligent recommendation system using gaze and emotion detection, Multimed. Tools Appl. 78 (2019) 14231–14250, https://doi.org/10.1007/s11042-018-6755-1.

[49] M.K. Noordewier, S.M. Breugelmans, On the valence of surprise, Cognit. Emot. 27 (2013) 1326–1334, https://doi.org/10.1080/02699931.2013.777660.

[50] X. Yi, L. Hong, E. Zhong, N.N. Liu, S. Rajan, Beyond clicks: dwell time for personalization, in: Proc 8th ACM Conf Recomm Syst, 2014, pp. 113–120, https:// doi.org/10.1145/2645710.2645724.

[51] C. Wu, F. Wu, Y. Huang, X. Xie, Neural news recommendation with negative feedback. CCF Trans. Pervasive Comput. Interact. 2 (2020) 178–188. https://doi org/10.1007/s42486-020-00044-0.

[52] X. He, H. Zhang, M.-Y. Kan, T.-S. Chua, Fast matrix factorization for online recommendation with implicit feedback, in: SIGIR ‘16, 2016, pp. 549–558, https:/ doi.org/10.1145/2911451.2911489.

[53] R.A. Fisher, Design of experiments, Br. Med. J. 1 (1936) 554, https://doi.org/ 10.1136/bmj.1.3923.554-a.

[54] G.-J. Park, Analytic Methods for Design Practice, Springer Science & Business Media, London, 2007.

[55] A. Tommasel, J.M. Rodriguez, D. Godoy, I want to break free! Recommending friends from outside the echo chamber. in: Proc 15th ACM Conf Recomm Syst. 2021, pp. 23–33, https://doi.org/10.1145/3460231.3474270.

[56] M. Ge, C. Delgado-Battenfeld, D. Jannach, Beyond accuracy: evaluating recommender systems by coverage and serendipity. in: Proc Fourth ACM Conf Recomm Syst, 2021, pp. 257–260, https://doi.org/10.1145/1864708.1864761.

[57] T. Zhou, R.Q. Su, R.R. Liu, L.L. Jiang, B.H. Wang, Y.C. Zhang, Accurate and diverse recommendations via eliminating redundant correlations, New J. Phys. 11 (2009) 123008, https://doi.org/10.1088/1367-2630/11/12/123008.

[58] G. Adomavicius, Y.O. Kwon, Improving aggregate recommendation diversity using ranking-based techniques, IEEE Trans. Knowl. Data Eng. 24 (2012) 896–911, https://doi.org/10.1109/TKDE.2011.15.

Ying Xue is currently pursuing her PhD degree at School of Management, Hefei University of Technology, China. Her research interests include recommender system, user modeling in VR/AR environments.

Jianshan Sun is an Associate Professor of Electronic Commerce in the School of Man agement at the Hefei University of Technology, China. He received his PhD in Information Systems from City University of Hong Kong in 2014. His research interests include big data analytics, recommender Systems and personalized services. His research has been pub lished in several journals including: Journal of Management Information Systems, Decision Support Systems, Tourism Management, Journal of the Association for Information Science and Technology, IEEE Transactions on Knowledge and Data Engineering, ACM Transactions on Information Systems, International Journal of Production Economics, Information Processing and Management, among others.

Yezheng Liu is a professor of Electronic Commerce at Hefei University of Technology, China. He received his Ph.D. in Management Science and Engineering from Hefei Uni versity of Technology in 2001. His main research interests include decision science, electronic commerce, intelligent decision support systems and data mining. His work has appeared in journals including Marketing Science, IEEE Transactions on Software Engineering, Information Sciences, and ACM Transactions on Information Systems.

Xin Li is a professor in the Department of Information Systems at the City University of Hong Kong. He received his Ph.D. in Management Information Systems from the Uni versity of Arizona. He received his Bachelor's and Master's degrees from the Department of Automation at Tsinghua University, China. His research interests include business intel ligence & knowledge discovery, social network analysis, social media, and scientometric analysis. His work has appeared in the MIS Quarterly, Information Systems Research, Journal of Management Information Systems, INFORMS Journal on Computing, Decision Support Sys tems, Information & Management, ACM Transactions on Management Information Systems, among others, and in various conference proceedings.

Kun Yuan is an assistant professor at School of Management, Hefei University of Tech nology, China. He received Ph.D. degree from Beihang University, China. His general area of research interests include data mining, recommender systems and social network analysis. His work has published in the journal of IEEE Transactions on Knowledge and Data Engineering. ACM Transactions on Knowledge Discovery from Data. ACM Transactions on Intelligent Systems and Technology, Information Processing & Management.
