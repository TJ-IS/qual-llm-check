---
otero_id: 7508
otero_key: "F27VJZ6K"
title: "Diffusing mobile coupons with social endorsing mechanism"
authors: "Yung-Ming Li; Jyh-Hwa Liou; Ching-Yuan Ni"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.11.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Difusing mobile coupons with social endorsing mechanism

Yung-Ming Li<sup>⁎</sup>, Jyh-Hwa Liou, Ching-Yuan Ni

Institute of Information Management, National Chiao Tung University, Hsinchu 300, Taiwan

A R T I C L E I N F O

Keywords: Mobile coupon Location-based commerce Social network Social endorser Social difusion

## A B S T R A C T

With the popularity of social media and mobile device, vendors have more distribution channels for digital coupons than ever before. However, coupon redemption rates are unacceptable to venders. The important factor driving coupon receivers to redeem mobile coupons is an understanding of them. The purpose of this study is to propose a new social coupon endorsing mechanism, which aims to identify those endorsers who have coupon proneness and a high sharing willingness for coupon difusion, with a recommended list of coupon receivers. Our experimental results show that our proposed mechanism efectively propagates mobile coupon or discount information by helping consumers to more eficiently gather coupons which fit their preferences and location, and to save money. It also helps vendors propagate mobile coupons to the target consumers in an eficient way.

## 1. Introduction

With the popularity of social media and mobile devices, social networking has become the most indispensable activity in modern society. Assorted applications are integrated into a contemporary mobile device, which has both portability and simplicity of operation. People, regardless of their age or sex, cannot go anywhere without a smart phone in real life. In America, around 87% of mobile users browse the internet or use e-mail with their mobile phone, and about 25% of users say they use their mobile phone more often than a computer [49]. For this reason, various businesses engage in social media advertising to promote their products, looking for additional marketing opportunities and a more extensive marketplace.

Price is the primary element influencing purchase decisions [33]. For businesses, coupon marketing is an efective method of price promotion marketing. Coupons can be used to attract coupon-prone consumers, increase product awareness, and encourage repeat purchasing. Coupon usage is a form of price discrimination, though which busi nesses ofer the same product but charge a diferent price to diferent consumers. Initially, coupons were issued by retailers and were widely distributed in newspapers, magazines, and leaflets; clipping paper coupons to save on living expenses became a daily routine for stay-athome moms. However, in recent years, collecting coupons has not been limited to housewives. As social networking sites and mobile devices have played a more significant role, businesses have more coupon distribution channels than ever before. 49% of US smartphone owners have used mobile coupons on their devices [34]. Mobile coupon ap plications such as Cellfire, Grocery IQ, Coupon.com and Saving Star are flourishing; these provide a wide variety of coupons for consumers [12].

Mobile coupons ofer huge business opportunities for marketers. Because of the increasing number of coupon distribution channels, lo cation-based coupons ofer another chance to reach prospective consumers instantly. Research shows that 47% of mobile consumers want retailers to send coupons to their devices when they are in or near the store [51]. Nowadays, in order to increase the visibility of advertisements, small and medium-sized companies encourage people to propagate advertisements through their social networks to get additional rewards. About 78% of mothers use social media to follow brands with the intent of getting coupons and promotions [52]. More and more businesses are taking advantage of the strength of propagation on social networking sites. They provide a price discount or special deal as a reward to encourage consumers to “check-in” to the business on Facebook, to tell friends they were there or to “like” the fan page of the business and thereby gain brand awareness.

RetailMeNot is the largest coupon site in the US, which aggregates over 500,000 coupons and ofers them to consumers. They provide a functionality of “coupon codes for referral” in which users are given a coupon code from RetailMeNot to share this code with a friend. When their friend buys something via this referral link, the user can get an additional discount from the store. However, coupon providers currently lack an eficient way to disseminate coupons. Even though users want to share the coupon codes with their friends through e-mail or social networking sites to get a referral reward, they encounter the main challenge of social referral; that is, they do not know who will need or like this product or coupon, and who will actually buy something. One low-cost approach is to broadcast coupons to all of their friends; nevertheless, excessive sharing of coupons or advertisements to all their friends will eventually harm their social capital and generate a negative impression, with irrelevant ofers being abandoned [22]. In order to avoid social spam, some users will only share coupons with specific close friends or family to decry antipathy, but for business. This conflicts with the purposes of social referral marketing, as the business hopes that their customers can be targeted by extensive coupon difu sion through users' social networks.

One study [36] points out that the important factor that can drive coupon receivers to redeem mobile coupons is a better understanding of the receivers' behavior. In essence, coupon distribution operation should be more eficient and smarter, in order to identify who is likely to receive coupons and to actually redeem them [5]. Since social media and mobile devices have become indispensable message propagation media for both marketers and consumers, finding better ways to disseminate coupons to the right consumers (the ones who need coupons) and continuously keep coupon propagation activities alive is an important issue.

The objective of this study is to design a new social coupon en dorsing mechanism. The major research problems to be resolved are as follows:

(1) How to help marketers eficiently disseminate relevant mobile coupons to the target consumer with preference fitness.

We aim to identify target consumers through social networking sites by analyzing the fit between the coupon category and the target consumer's preferences, and then examining whether the distance to the store is within an efective range for service. Finally, mobile coupons will be delivered by the coupon endorser to the target consumers.

(2) How to help marketers to disseminate mobile coupons through the right endorsers having sharing willingness without evoking irritation from the senders.

We attempt to find and rely on those mobile coupon endorsers with coupon proneness to influence our targeting consumers' response to the coupon. In this way, customers can also avoid evoking the feelings of disapproval and negative impression to coupons. In addition, we ana lyze the sharing willingness of endorsers to ensure the ability of coupon propagation. In order to get rewards, endorsers with coupon proneness have a high level of willingness to disseminate coupons through their social networks.

The proposed social coupon diffusion mechanism aims to identify those endorsers who have coupon proneness and sharing willingness for coupon difusion by analyzing factors such as preference, location, coupon proneness, sharing willingness, social similarity and social in teraction. Specifically, the proposed mechanism will recognize those people who are easily motivated by rewards, sensitive to discount information and highly willing to share coupon messages. Moreover, from a given list of coupon receivers recommended by our mechanism, the endorsers are able to determine to whom they should difuse a coupon. This not only assists endorsers encountering the coupon difusion pro blem (which friends would like the coupon), but also helps marketers increase difusion eficiency. The proposed coupon endorsing mechanism creates a new, available and active information propagation channel based on endorsers, and allows continuous and wide coupon dissemination. This mechanism will not only be acceptable to custo mers but also allows businesses to better understand customers and increase their satisfaction and customer retention rates.

The rest of the paper is organized as follows. In Section 2, we will describe the literature related to this research. Section 3 illustrates the system framework of the social coupon endorsing mechanism. Experi ments conducted on the proposed system are detailed in Section 4. Section 5 demonstrates and evaluates the experimental results. Lastly,

Section 6 summarizes the contributions of this research and discusses limitations and future studies.

## 2. Related literatures

## 2.1. Coupon redeeming

Coupons have many forms including paper coupon, electronic coupon, mobile coupon, and social coupon. A mobile coupon is a type of digital coupon that is commonly used for sales promotion; it is issued by retailers and marketers, who aim to retain old customers while attracting new price-sensitive customers [10]. Mobile coupons can be found on online websites, email, SMS, and mobile applications. Consumers can easily receive incentives at the time of redemption, without requiring the time to clip a paper coupon [20]. Previous works point out face value is one of the successes in terms of redemption [9,45] and it is suggested that the redemption rate of mobile coupons is better than traditional coupons [2].

Mobile devices have played a role in bridging the instant service gap between consumers and local retailers [39,58,61]. With location char acteristics, the retailers can utilize the promotions on the mobile platform to enhance customer loyalty [39]. For instance, the GPS functionality of mobile phones and check-in data allows businesses to target potential customers near to a store which is ofering a promotion deal [53]. A coupon is a form of advertisement. Mobile phones enhance the capabilities of advertisement reachability at the right time and right place. The study in Ref. [4] shows that the characteristics of locationbased mobile advertisements are significant factors influencing the effectiveness of an ad. For instance, it is more efective to receive a promotional advertisement when shopping at stores than to receive the same advertisement at home. Mobile devices are considered to be another form of the user self, and contain private information about users [55]. Based on the personal data of a user, a business can design targeted advertising and disseminate location-based services [29]. Furthermore, local retailers should consider the factors of electronic-word of–mouth and local competition to ofer daily deals [3].

Recently, the concept of social couponing is proposed [27]. Social coupons are labeled as daily deals that target consumers in a given city through website, e-mail and social media to ofer discount and refer their friends [7,37]. The study in [57] integrates social capital theory and motivation theory to study the success factors driving mobile coupons, including the factors of social tie, trust and perceived similarity. However, most of current research does not investigate how to difuse the social coupons or mobile coupons. In this paper, we aim to find certain characteristics of consumers, such as coupon proneness in social networking sites, and rely on these mobile coupon endorsers to influence our target consumers' response to the location-based coupon.

## 2.2. Information difusion

Social networks are important media which allow people to communicate and exchange information. People get news and real-life information from social media sites [11]. Users are more likely to be persuaded if the information or recommendation was sent by their peers; this may influence them to form or alter their preferences unconsciously and eventually afect their decision making [40]. There are several well-known information difusion models, including the linear threshold model [18], the independent cascade model [22], and the general cascade model [25].The basic concept of these difusion models is that nodes can be influenced by other nodes, and can also influence other nodes with similar characteristics. These information difusion models are efectively used in social networks [47].

Various other information difusion methods with diferent appli cations have also been proposed. The work in Ref. [23] uses high performance computing (HPC) architectures to optimize information propagation simulations which allow us to compute large-scale social networks with diferent network structures. The authors of Ref. [40] study the importance of the actor in the bridge position. A node with many contacts (i.e. a hub) has a higher degree of opinion leadership and influence on a group, while bridge nodes connect otherwise unconnected clusters. People commonly select and share interesting information with friends over social media. However, the issue of how to attract people to trigger information propagation is still an essential one. In this research, we aim to disseminate coupon or information by rewarding those people who are sensitive to the discount and those people who will spread this information to their close friends spontaneously.

## 2.3. Social influence

Social network structure consists of individuals and interpersonal relationships. Our interpersonal relationships can be visible to the public, and can be used to simplify the path of information spreading between individuals and to study the impact of social influence [23,44]. Social influence refers to how person's perception, attitudes, or behavior are changed by others; this has been an important topic in social psychology, which studies how individuals are influenced and become unfiled into a group [28,47,59]. With the power of electronic word of mouth (eWOM), discount information can be easily disseminated to friends or family [26]. Nowadays, information distribution does not need to be face to face, present or even oral communication. Customers can freely share their personal evaluations of products they have bought over social networks, and many studies have explored the as sociation between online comments and shopping decisions [21,28,41]. The Nielsen online survey across 58 countries indicates that word of mouth advertising from friends and family is the most influential and persuasive for consumers [35]. Businesses do not need to advertise themselves if ad information can be passed on using consumers' social networks in a low-cost but eficient way [56,57].

Many local retailers utilize social networks to advertise their shops. For example, they encourage consumers to “like” their brand or “checkin” to the business by providing reward incentives or promotion [51]. These actions are equivalent to give good recommendation on the business, which likely stimulates their purchasing desire. Target coupon and social coupon endorsing are two complementary ways to improve marketing of a certain product. Target coupon is implemented based on customer past historic economic activity [16,38]. For example, Ref. [38] studies optimal marketing strategies for a customer data intermediary that collects customer data and ofers to target services to the competitive manufacturers or retailers. Ref. [16] uses target coupon to ofer competitive price in diferent firms based on geo data and past consumer activity. In our study, we use the factors of personal preference and location of the targeted consumer discovery mechanism. Social endorsing is an efective way to difuse online advertisement [32,54]. Ref. [32] proposes social advertising in marketing and use social factors, such as popularity, centrality, social activity, and interaction to select seed endorsers. In this paper, we will develop a social endorsing mechanism to identify influential users as coupon endorsers from the target consumers' social networks to strengthen the efect of mobile coupon propagation.

## 3. The system framework

The purpose of this mechanism is to discover coupon-prone endorsers who also have strong persuasion capabilities and can actively distribute coupon information to the target consumers. The target consumers can then forward the coupon to their friends to acquire re wards. The proposed mechanism could help marketers reduce negative perceptions of commercial advertisements while increasing the rate of coupon redemption. The system architecture is shown in Fig. 1.

First of all, the target consumer discovery mechanism discovers the target consumers from all users. Then, the social endorser identifies mechanism identifies the influential coupon endorsers from the target consumers. Finally, the coupon receiver identification mechanism identifies the suitable receivers with respect to the corresponding endorser. The main modules of the proposed architecture are described below.

(1) Target consumer discovery mechanism: This mechanism aims to understand consumers' preferences and location, which are essential to provide the right coupons to the right consumers. We analyze the consumer's brand and product preferences to evaluate whether consumers are interested in the coupon. We then use a pre-classified coupon product tree to compute the similarity score between the coupon and the user's preference, in order to measure the relevance of the coupon to the target consumer. According to their location data, we can then determine the appropriate coupons to send.

(2) Seed endorser identification mechanism: This mechanism is focused on identifying endorsers who are coupon-prone and who have a high sharing willingness from the group of target consumers, which can help marketers to find the right coupon endorsers.

(3) Coupon receiver identification mechanism: This mechanism is used to discover the appropriate coupon receivers. The candidate receivers are evaluated based on their intensity of social similarity and the social interaction between coupon endorser and receivers.

## 3.1. Target consumer discovery mechanism

A coupon which fits a consumer's preferences can increase the rate of redemption. The target consumer discovery mechanism considers the user's preferences and location in order to locate suitable coupons for the target consumer.

## 3.1.1. Preference analysis module

We can infer a user's preference from their social network posts, profile and liked pages. We will convert individual preferences to keywords by taxonomy [1], estimate their semantic similarity using this taxonomy [30] and then categorize it for the next module.

3.1.1.1. Brand preference identification. Brand is an important factor driving coupon receivers to redeem coupons. A consumer who has brand loyalty is a good target for the coupon. A Facebook user's “likes” reveal the brands that they are interested in; we therefore extract a user's brand preferences from their “liked” pages, and then store the brand keywords in the dataset.

3.1.1.2. Product preference identification. In practice, consumers' preferences are not always constant and explicit; however, we can observe their social activities, such as posts, to infer their preferences. For example, if a user often posts images of cuisine, we can infer that s/ he might like to receive a restaurant coupon. Recent posts indicate a new focus and attention to specific products. Based on historical posts, Facebook “like” categories and online questionnaires, we can identify a consumer's focus and attention, and use these keywords to infer a user's product preferences.

## 3.1.2. Coupon attribute analysis module

This module is used to measure the similarity degree of the coupon and the consumer's preference. We construct a tree-like structure to classify a given coupon and the target consumer's preference and use a hierarchical distance to compute the similarity score in order to determine the most appropriate coupon for a consumer.

3.1.2.1. Category tree construction. In order to identify whether the coupon recommendation fits the target consumer's preference, we need to evaluate the similarity between them. We therefore use a product category tree to represent the types of user's preferences and products. The product category tree is built by referring to well-known online shopping sites and coupon providers such as “Yahoo Shopping Mall”, “Groupon” and “Savings.com”. A node close to a leaf indicates that the classification is more specific; conversely, a node closer to root indicates that the product type is more generic. The tree-structure of type representation has been widely applied in the fields of product taxonomy [60] and semantic similarity in taxonomy [30].

![](/api/attachments/F27VJZ6K/fulltext/images/e90249bb36ae4df78041c30dd44c4e3bf7b58e257e3ea35f85448ac35ab32b42.jpg)  
Fig. 1. The system architecture of the social coupon difusion mechanism.

3.1.2.2. Similarity computing. We will compute the similarity score by comparing user brand favorability and user preference on coupons attributes. The brand favorability score can be formulated as:

$$
F a v (u _ {i}, c) = \left\{ \begin{array}{l} 1, i f L i k e P a g e (b _ {i}) = C o u p o n s (b _ {j}); \\ 0, i f L i k e P a g e (b _ {i}) \neq C o u p o n s (b _ {j}). \end{array} \right.\tag{1}
$$

If a promotional coupon c is also a focused brand of user $u _ { i } ,$ the value is set to one; otherwise, it is zero. Secondly, we adopt a superior distance-based method [30] in the category tree to measure the similarity between the keywords of a consumers' preferences and the coupon attributes. As illustrated in Fig. 2, let $C _ { 1 }$ and C stand for the category of user preference and category of coupon, respectively. l is the shortest path length between $C _ { 1 }$ and $C _ { 2 } \left( \mathrm { i . e . } l _ { 1 } + l _ { 2 } \right)$ , and $C _ { m }$ in the upper layer hierarchy than $C _ { 1 }$ and $C _ { 2 }$ represents the general semantics between them. We denote the first mutual node as $C _ { m } ,$ where h is the depth of the hierarchy from root to $C _ { m }$

Note that α ≥ 0 is a constant and $\beta > 0$ is a smoothing factor; we set α = 0.2 and β = 0.6 [30]. The $e ^ { - \alpha l }$ exponential form constrains the path length l to between zero and one. Since the similarity increases with $h ,$ an exponential growth function is employed. The similarity score is formulated as:

![](/api/attachments/F27VJZ6K/fulltext/images/c0ff70da16b8739cb70077c206a2a0bb524eecc944905d03b1909addf3d1689e.jpg)  
Fig. 2. Category tree.

$$
S i m (C _ {1}, C _ {2}) = e ^ {- \alpha l} \times \frac {e ^ {\beta h} - e ^ {- \beta h}}{e ^ {\beta h} + e ^ {- \beta h}}.\tag{2}
$$

Cate(u ) denotes the set of user u preference categories and Cate(c) is the category of coupon c. We can derive the preference-similarity score for a consumer u and a coupon c as:

$$
\operatorname{Sim} _ {p} \left(u _ {i}, c\right) = \operatorname{Fav} \left(u _ {i}, c\right) + \left( \right.\frac {1}{| C a t e \left(u _ {i}\right) |} \cdot \sum_ {C _ {u _ {i}} \in C a t e \left(u _ {i}\right)} \left(\operatorname{Sim} \left(C _ {u _ {i}}, C a t e (c))\right)\right).\tag{3}
$$

## 3.1.3. Location fitness analysis module

The location is a significant factor to consider when a consumer considers redeeming a coupon. If the redemption service location is located too far from the user, the coupon is impractical to use. This module measures the similarity degree between a user's location and coupon redemption location to provide a relevant coupon service.

3.1.3.1. Feasible location identification. Location is one of the important factors driving consumers to redeem coupons. We consider three types of location-based factors which can afect consumers' willingness to redeem coupons: their current location, residence location and active location.

3.1.3.1.1. Current location. Geographical proximity plays a decisive role in triggering the intention to purchasing. A coupon from a nearby store will be more attractive to the user. Each user $u _ { i } \in U$ and coupon venue c are associated with a geo-location. u 's current location (i.e. longitude and latitude) can be revealed by GPS or mobile location technology such as Google Directions API. We use $C _ { u _ { i } , }$ to represent the current location value:

$$
C _ {u _ {i}, c} = 1 + \frac {1}{\text {distance} (u _ {i} , c)},\tag{4}
$$

where distance $( u _ { i } , c )$ represents the Euclidean distance between user u and coupon venue c. If distance $\begin{array} { r } { ( u _ { i } , c ) = 0 , } \end{array}$ , we set value as one. Impulse buying intention is inversely proportional to distance.

3.1.3.1.2. Residence location. When the retailer's location is in the city where the user lives, the chance of coupon redemption is greater, as it will require lower transportation costs to visit the shop. We can obtain a user's residence information from their social network profile. Notice that $R _ { u _ { i } } ,$ takes a value between zero and one. If user $u _ { i }$ and coupon venue c are in the same city, $R _ { u _ { i } , c } = 1$ , which means that user u has a high probability of redeeming the coupon. On the other hand, $R _ { u _ { i } } ,$ $_ c = 0$ means the coupon's attractiveness to the user is relatively low.

$$
R _ {u _ {i}, c} = \left\{ \begin{array}{l l} 1, & \text {   user   residence   =   coupon   location   } \\ 0, & \text {   user   residence   \neq   coupon   location.   } \end{array} \right.\tag{5}
$$

3.1.3.1.3. Active location. A user's check-in data reveals his/her mobility. When user frequently checks in within the same city or at the spot, this means that they often go to and are active in these places. Hence, the chance of redeeming the coupon is higher. $C I _ { u _ { i } } ,$ denotes the set of u ’s check ins at venue v and $L _ { c }$ denotes the redemption locations of coupon c. The check-in times of user $u _ { i }$ at given coupon venue c can be obtained as:

$$
C I T _ {u _ {i}, c} = \Sigma_ {v \in L _ {c}} | C I _ {u _ {i}, v} |.\tag{6}
$$

A higher value of $C I T _ { u _ { i } , ~ c }$ means that user $u _ { i }$ is more active in coupon venue c. The active location score of user $u _ { i }$ at a given coupon venue c is formulated as:

$$
A _ {u _ {i}, c} = \left\{ \begin{array}{l l} 1, & \text {if} C I T _ {u _ {i}, c} \geq \varepsilon \\ \gamma , & \text {if} 0 <   C I T _ {u _ {i}, c} <   \varepsilon , \\ 0, & \text {if} C I T _ {u _ {i}, c} = 0 \end{array} \right.\tag{7}
$$

where $0 \textless \gamma \textless 1$ , and ε represents a threshold for the active location score. Finally, the feasible location score can be calculated as:

$$
L (u _ {i}, c) = C _ {u _ {i}, c} + R _ {u _ {i}, c} + A _ {u _ {i}, c}.\tag{8}
$$

3.1.3.2. Fitness computing. By considering user's preference and available locations, we can further compute the fitness score using the following formula:

$$
F i t n e s s (u _ {i}, c) = S i m _ {p} (u _ {i}, c) + L (u _ {i}, c).\tag{9}
$$

By utilizing the fitness score, we can determine the set of target consumers that have an interest in the coupon and who have a high probability of redeeming it. We denote the set of target consumers as $\delta _ { T } .$ $\delta _ { T } = \left\{ u _ { i } | F i t n e s s ( u _ { i } , c ) > \lambda _ { t } \right\}$ , where $\lambda _ { t }$ is a threshold for the fitness acceptance level.

## 3.2. Seed endorser identification mechanism

After determining appropriate mobile coupons for the target consumers, we still have to attract them to visit the store. If the coupon advertisement is sent by the business or marketer, this may annoy the receivers; as an alternative, we can solicit endorsers who have coupon proneness and who are influential to the target consumers in order to difuse the mobile coupons. These endorsers are likely to be willing to help the business by forwarding attractive coupons to their friends.

## 3.2.1. Coupon proneness analysis module

Frugal behavior is entrenched for part of the consumer group; these customers focus on collecting price discount information and useful coupons before purchasing. A coupon is a market segmentation strategy for recognizing those customers who are price sensitive. This module aims to identify target endorsers who have high coupon proneness and higher motivation to difuse coupons.

3.2.1.1. Static coupon-prone identification. Females are more likely to recommend products, brands and sales information to their friends, and coupon redemption has a positive correlation with a high level of education. People with university degrees are more responsive to mobile coupon services [15]. Households also gain greater enjoyment from hunting available coupons than other users [50]. People aged between 25 and 44 are the major users of mobile coupons [8], and the study in [34] also indicates that students are the biggest group of coupon users. We therefore use these characteristics as our proneness characteristics set P = {college-educated, household, age: 25 to 44, student}. These data can be obtained from the target consumer's profile. Furthermore, since these data are not updated frequently, they can be considered “static”. The static proneness of a target consumer $t _ { i } \in \delta _ { T }$ can be calculated by following formula:

$$
S P (t _ {i}) = \text { gender } _ {t _ {i}} \times (\text {   } p _ {j} \in P \text { count } (t _ {i}, p _ {j})),\tag{10}
$$

where $p _ { j }$ ∈ proneness charecteristics set Pand $c o u n t ( t _ { i } , p _ { j } )$ indicates whether t has proneness characteristics $p _ { j } .$ The study in [19] indicates that women are more price-sensitive than men and are more likely to recommend products, brand or sales information to their friends. Thus, we set the value of gende $r _ { t _ { i } }$ to 0.6 for females and 0.4 for males.

3.2.1.2. Dynamic coupon-prone identification. A coupon-prone consumer usually has some channels (e.g. social groups) for collecting coupons. We analyze the keywords of a target consumer's posts and shared information, and then judge whether this information is related to coupon information. The keywords derived from a target consumer t are split into $K _ { t } = \{ x _ { 1 } , x _ { 2 } , . . . , x _ { n } \}$ and the discount-related keywords form the set $K _ { d } = \{ y _ { 1 } , y _ { 2 } , . . . , y _ { n } \}$ . We use the normalized Google distance (NGD) in semantic similarity computing to measure the correlation between a coupon and a target consumer's data (keywords from posts and the name of the social group joined). The terms x ∈ K and y ∈ $K _ { d }$ are used to compute the NGD based on the following formula:

$$
N G D (x, y) = \frac {\max \{\log f (x) , \log f (y) \} - \log f (x , y)}{\log N - \min \{\log f (x) , \log f (y) \}},\tag{11}
$$

where $f ( x )$ represents the number of target consumer's keywords x web page search results; $f ( y )$ represents the number of discount keyword y web pages search results, and $f ( x , y )$ is the number of web pages with both x and y. N represents the total number of web pages resulting from a search by Google. The value of $N G D ( x , y )$ is between zero and one; the smaller the value, the greater the association. Hence, the coupon proneness of target consumer $t _ { i }$ can be evaluated by the following formula:

$$
\text { Coupon\_Prone } (t _ {i}) = S P (t _ {i}) + \frac {1}{\sum_ {x \in k _ {t} (t _ {i})} N G D (x , K _ {d} (y))}.\tag{12}
$$

A higher value of Coupon\_Prone(t )ndicates a higher coupon proneness of target consumer $t _ { i } ,$ that is, the target customer has more probability of being driven by rewards to propagate coupon information.

## 3.2.2. Sharing willingness analysis module

One of key factors in successful difusion depends on the endorser's willingness in terms of spontaneous sharing behavior. Some endorsers are altruistic; even though there is no sharing reward, they are still willing to share information which will be helpful to their friends. Thus, we consider the frequency of sharing information by the endorser and subsequent reaction to his/her sharing to evaluate sharing willingness.

3.2.2.1. Sharing activeness. We evaluate a target consumer's sharing frequency on social networks based on his/her historical posts and replies which contain URLs or shared information via other channels. If a target consumer constantly shares information on a social network, this indicates that the target consumer has a higher probability of disseminating a coupon to his/her friends. Sharing activeness is measured as:

$$
S _ {a} (t _ {i}) = \frac {| \Phi h t t p (t _ {i}) |}{| \Phi p o s t (t _ {i}) | + | \Phi r e p l y (t _ {i}) |},\tag{13}
$$

where Φpost(t ) denotes the set of messages posted by target consumer $t _ { i } ,$ and Φreply(t ) denotes the set of messages replied to by the target consumer $t _ { i \cdot }$ Φhttp(t ) denotes the set of messages containing URLs in Φpost(t ) and Φreply(t ).

3.2.2.2. Sharing popularity. The subsequent feedback and reactions from other target consumers are significant considerations for evaluating the sharing willingness of a target consumer. These reactions from their friends can be viewed as implicit incentives for a person to share information. The sharing of information may be via liking, forwarding or responses from friends on a social network. Observing the popularity degree of a target consumer's posts allows us to predict the consequences of information difusion. We denote the sets of t 's shared information that were liked, forwarded and responded to by other target consumers as Φlike(t ), Φforw(t ) and Φresp(t ), respectively. The sharing feedback of target consumer t can be measured as:

$$
S _ {p} (t _ {i}) = \frac {| \Phi l i k e (t _ {i}) \cup \Phi f o r w (t _ {i}) \cup \Phi r e s p (t _ {i}) |}{| \Phi h t t p (t _ {i}) |}.\tag{14}
$$

We can derive a target consumer's sharing willingness score as:

$$
S W (t _ {i}) = S _ {a} (t _ {i}) \times S _ {p} (t _ {i}).\tag{15}
$$

Finally, the coupon endorser value can be derived from the following formula:

$$
e n d o r s e r _ {v a l u e} = C o u p o n _ {P r o n e (t _ {i})} \times S W (t _ {i}).\tag{16}
$$

The set of qualified coupon endorsers can be obtained as $\delta _ { E } = \left\{ t _ { i } | \mathrm { e n d o r s e r } _ { \mathrm { v a l u e } } > \lambda _ { e } \right\}$ , where $\lambda _ { e }$ is a threshold value for the fitness acceptance level.

## 3.3. Coupon receiver identification mechanism

A coupon receiver should be a target consumer for the coupon and should also have a close relationship with the coupon endorser. A coupon propagated by an influential endorser can create a more positive impression of the target consumer, improving the chances of both redeeming the coupon and further sharing the coupon. We analyze the social similarity and social interaction between the receiver and the endorser, in order to evaluate and identify suitable coupon receivers.

## 3.3.1. Social similarity

People are more likely to trust those who are like them [14,43]. When information difusion costs are high, information is more likely to be passed to friends with strong ties [40]. Previous researchers measure social similarity based on the number of common communities and local activities [31]. Ref. [46] points out a person who has more mutual friendships is more influential due to the relationships and interests in common. If two persons have more mutual friendships, they have higher influence and similar interest. In our research, social similarity is measured as the degree of the mutual friends between the endorser and the target consumer. The stronger tie between endorser and target consumer, the more possible they would be friends and get quite familiar with each other. The social tie between two users can be reflected on their social similarity, which could be measured by the common characteristics two users have from social network. In this research, we use Jaccard similarity coeficient to measure the friend similarity by analyzing the degree of the mutual friends to represent the social similarity between the coupon endorser and the target consumer. Suppose F(e ) indicates the friend set of coupon endorser $e _ { i }$ in a social network, and $F ( t _ { i } )$ indicates the friend set of target consumer $t _ { i \cdot }$ The social similarity between the coupon endorser $e _ { i }$ and target consumer t is computed by the following equation:

$$
S S (e _ {i}, t _ {j}) = \frac {| F (e _ {i}) \cap F (t _ {j}) |}{| F (e _ {i}) \cup F (t _ {j}) |}.\tag{17}
$$

When the social similarity is high, the coupon redemption intention of the target consumer is more likely to be stimulated by the endorser, since the recommendation is highly influential and persuasive to the receiver.

## 3.3.2. Social interaction

Interaction frequency can be an indicator for measuring the social relationship between endorser and target consumer. Social interactions include responses, likes, tags, and, sharing of messages posted by other users. Given a coupon endorser e and target consumer $t _ { i } ,$ the social interaction score is formulated as:

$$
S I (e _ {i}, t _ {j}) = \frac {| \Phi i n t e r a c t i o n (e _ {i} , t _ {j}) |}{| \Phi i n t e r a c t i o n (e _ {i}) |},\tag{18}
$$

where Φinteraction(e ) indicates the set of social activities that endorser $e _ { i }$ exhibits on social media, and Φinteraction(e , t ) indicates the set of social activities which includes both endorser $e _ { i }$ and consumer $t _ { j } .$ The greater the social interaction score, the greater is the closeness between two users.

Finally, the coupon endorser and the suitable coupon receiver can be matched using the equations above:

$$
M a t c h (e _ {i}, t _ {j}) = F (e _ {i}, t _ {j}) \times S S (e _ {i}, t _ {j}) \times S I (e _ {i}, t _ {j}),\tag{19}
$$

where $F ( e _ { i } , t _ { j } ) = 1$ if e and t are friends on the social network, and is zero otherwise. We use this match score to rank and identify appropriate coupon receivers. The coupon receivers with the top K ranked matching degrees are selected as targets for social coupon dissemination.

## 4. Experiments

We describe experiments here which verify the eficiency and ef fectiveness of the proposed mechanism. In this research, we validate our proposed mechanism using a well-known and popular social networking site, Facebook, which allows users to present themselves on a public platform, interact with other users, and to maintain and establish connections with other users. According to a survey conducted by Pew Research Center in 2014 [17], Facebook has a higher number of users than other social network sites like Twitter, Instagram and LinkedIn. With the increasing numbers of digital coupons available to consumers, a mobile device is an indispensable storage device for digital coupons. We obtain a user's location information using Google Location API, and utilize Facebook Graph API to mine the user's friends list, check ins, likes, fan pages liked, location data and product preferences to discover target users and endorsers for a coupon. In view of privacy concerns, these data are collected with the users' permission, using OAuth 2.0 protocol to get access to the tokens.

In the experiments, a brief coupon message is given, with a hyperlink. A receiver can click on the hyperlink for more detailed in formation, such as a picture of the coupon, information about the redemption shop, and the reward for difusion. An endorser can download the coupon and decide whether to share this coupon with their friends. In the following sections, we describe the details of our data collection strategy for coupon difusion and experimental processes.

## 4.1. Data description

## 4.1.1. Profile of participants

In our experiments, we collected social network data from a total of 219 participants. The average number of friends for each participant was 324. In records from the past 12 months, there were 21,024 check in data points, 63,092 posts, 10,731 fan page likes, 2,207,520 likes of friends' posts and 946,080 comments responding to friends. The participant's ages were between 15 and 50, and students and ofice staf were in the majority. The gender distribution was 95 males and 124 females, and the distribution of marital status was 177 unmarried and 42 married.

To recognize the product preferences of these users, we used the Chinese Knowledge and Information Process (CKIP) to separate and identify the most frequent words. The CKIP is a tool formed by the Institute of Information Science and the Institute of Linguistics of Academia Sinica in 1986 [13]. Firstly, we input participants' historical Chinese posts sentences to the CKIP. Then, the system will efective and automatically tag, parse and assign roles to the sentence. We identify the most frequent words. Next, the keywords quarried using CKIP were matched with the coupon category tree nodes. The matched categories can also be viewed as the users' product preferences. For example, if the term “pet” is a frequent word in a user's posts, “pet” can be matched with the “Pet supplies” category and added to a user's preferences, to aid in subsequent coupon recommendations.

## 4.1.2. Profiles of mobile coupons

In the experiment, we constructed a coupon category tree to compute the similarity degree between participant's preferences and the coupon provided, and used it to determine the target consumer. The category tree for the coupons used in our experiment was built by referencing the product categories of Yahoo shopping, Savings.com and Groupon. There are four layers with a total of 50 leaf categories, that is, 10 parent categories and five grandparent categories. The structure of the tree is shown in Fig. 3. If a category position is closer to the root, this represents that the concept of the category is more general. Our experiments collected 396 digital coupon samples from multiple Taiwan online coupon provider platforms, such as MyCoupon.com, iPeen, 17Life, and TraNews, to create a diversity of mobile coupon propagation scenarios. These coupon samples were then classified into the relevant leaf categories and were used to compare the performance of four coupon dissemination strategies. In the experiments, top-5 of the ranked candidate endorsers were selected as the recommended endorsers. In order to intensify an endorser's motivation toward coupon propagation, we ofered an incentive whereby the endorser could obtain an additional 10% discount as a default reward by difusing the coupon to their friends.

## 4.2. Coupon dissemination strategy

To evaluate the performance of the proposed coupon difusion mechanism, we compare it with three other diferent coupon difusion strategies. The four strategies are described below:

(1) Social difusion (our approach): This coupon difusion approach is based on our proposed mechanism. We firstly analyze users' preferences and location fitness to find target consumers (candidate endorsers); we then identify their coupon proneness and sharing willingness to determine suitable social coupon endorsers. Lastly, social similarity and social interaction measures are used to identify the remaining target consumers, who are the corresponding coupon receivers.

(2) Topic-aware influence: This is a commonly used approach in social network marketing. Users have diferent interests and characteristics, and are likely to be attracted to and influenced by something they are interested in. Therefore, we use preferences to rank the top K coupon endorsers, and then use this and social similarity measures to identify corresponding coupon receivers.

(3) Opinion leader difusion: This involves discovering nodes with a high distance centrality and high sociality. An opinion leader has more probability of influencing others to adopt a particular product or innovation. In this approach, we used the number of friend/ follower connections to rank the coupon endorsers, and then used the same connection ranking and social interaction measures to identify the corresponding coupon receivers.

(4) Bridge difusion: This approach selects endorsers, based on their position in a social network, who play a connector role, bridging two sub-networks. If the bridge endorser does not pass on the information, users in another network cannot acquire this information. A bridge endorser is an important node for delivering coupon information in order to achieve a higher target coverage rate. Therefore, we took the position in social network to identify influential coupon endorsers and corresponding coupon receivers.

Notice the selected benchmark models reflect diferent levels of personal information and social tie between the endorser and receivers. Among the benchmarks, the bridge approach doesn't consider any personal information nor social tie information. The opinion leader approach doesn't consider any personal information but considers partial social tie information (e.g. social interaction). The topic-aware influence approach considers partial social tie information (e.g. social similarity) and partial personal information (preference). Our approach considers more comprehensive factors of personal and social tie information.

## 4.3. Experiment procedures

The experimental procedures used are described as follows.

1. Target consumers are identified from the data collected from par ticipants' social networks.

2. Coupon endorsers are selected to disseminate mobile coupons using various planned endorser discovery strategies.

3. All the selected endorsers will receive a short URL; this will redirect endorsers to a webpage which contains digital coupon information and a recommended list of top-K coupon receivers. Endorsers can choose whether or not to distribute the coupon to those targets. The difusion reaction is recorded in a database. Note that when endorsers receive a coupon, they do not know which coupon dissemination approach is being tested.

![](/api/attachments/F27VJZ6K/fulltext/images/1b2e3830f2cd460d556d6ab5bd1dd20cb01df3ce926394ff0d86c839d0ccdc0d.jpg)  
Fig. 3. Coupon category tree.

4. After endorsers have visited the given webpage and made a decision on whether to pass on the coupon, the endorsers are asked to give their reactions to this coupon via an online questionnaire. Consequently, we can evaluate the efectiveness indicators for each experiment.

5. If the coupon endorsers pass on the coupon to the recommended target consumers, the target consumers will receive a URL from the endorsers; this will direct them to a webpage containing digital coupon information. In addition, the target consumer is asked to feed back their thoughts via a questionnaire.

6. Based on these questionnaires and difusion records, we evaluate the coupon receiver's impression, satisfaction, efectiveness, and willingness to disseminate the coupon.

## 5. Results and evaluation

In this section, we verify the efectiveness of our proposed social coupon difusion mechanism by comparing it with three diferent benchmark approaches, according to measures such as the average number of times a coupon is shared, the targeted coverage of a coupon recommendation and the use of an online questionnaire for coupon receivers' feedback to analyze the coupon receivers' satisfaction and the endorser appropriateness of a coupon recommendation. We also compare the sharing rates for the diferent categories of digital coupons and provide a reference for marketers to plan exceptional coupon difusion strategies in the future.

## 5.1. Average sharing times

The average sharing time is a significant factor quantifying the effectiveness of the coupon difusion process. Once the coupon from the endorser is delivered to the target consumer, we can measure the number of times a coupon was shared with the target consumers. The formula for coupon average sharing times (AST) is defined as:

$$
A S T = \frac {\Phi s h a r e d}{\Phi c o u p o n},\tag{20}
$$

where Φshared is the total times coupons were shared by coupon receivers, and Φ coupon is the total number of coupons. The descriptive statistics for AST is as follows (Table 1). # of coupon shared is the total number of the coupons shared by all receivers. Fig. 4 shows the average sharing times of the coupon for the diferent difusion strategies.

A paired sample t-test was used to show that our mechanism has significantly better performance in terms of coupon sharing than other approaches (as shown in Table 2). The confidence interval was set at

Table 1  
Descriptive statistics of average sharing times.

<table><tr><td></td><td>Bridge</td><td>Opinion leader</td><td>Topic-aware influence</td><td>Social diffusion</td></tr><tr><td># of coupon shared</td><td>1674</td><td>2021</td><td>2683</td><td>3206</td></tr><tr><td># of coupons</td><td>396</td><td>396</td><td>396</td><td>396</td></tr><tr><td>AST</td><td>4.2273</td><td>5.1035</td><td>6.7753</td><td>8.0960</td></tr></table>

![](/api/attachments/F27VJZ6K/fulltext/images/12419e2b3e1960c3f0b1f31da8a804b1b1c3fcc020d80c7f12e1eb79589572d1.jpg)  
Fig. 4. The average number of times a coupon was shared in the four difusion strategies.

95%. The targeted social difusion approach achieved significantly better results (α = 0.05) than the other benchmark approaches; the statistics t-test therefore indicates that our proposed approach showed the best results in terms of coupon sharing times.

## 5.2. Target coverage rate

For businesses, the purpose of issuing a coupon is to attract the attention of target consumers. We therefore evaluate the target coverage rate (TCR) for the diferent coupon dissemination strategies. The target coverage rate is defined as:

$$
T C R = \frac {\Phi \mathrm{target} \cap \Phi \mathrm{received}}{\Phi \mathrm{target}},\tag{21}
$$

where Φtarget represents the total number of coupon target consumers, and Φtarget ∩ Φreceived represents the users who are coupon target consumers and who have received the coupon. The descriptive statistics for TCR is as follows (Table 3). # of targeted customers is the total number of the customers targeted for all 396 coupons. # of targeted customers who received coupons is the total number of the targeted customers who actually received the coupons. Fig. 5 shows the target coverage rates of the coupon for the diferent difusion strategies.

As shown in Fig. 5, our proposed social difusion approach achieved the highest coverage rate. We can infer that endorsers with coupon proneness who share a coupon are encouraged by the rewards. A paired sample t-test was used to determine whether our mechanism performed statistically better in terms of target coverage rate than the other approaches (as shown in Table 4). When the confidence interval was set to 95%, the targeted social difusion approach achieved a significantly better efect than the other benchmark approaches. Therefore, the targeted social difusion approach has a higher dissemination strength and the best target coverage rate (TCR) for the coupon.

Table 2  
Statistical verification results based on AST measurement.

<table><tr><td>Paired group</td><td></td><td>Mean</td><td>Std. deviation</td><td>Std. error mean</td><td>T</td><td>Sig. (two-tailed)</td></tr><tr><td rowspan="3">Social diffusion VS.</td><td>Topic-aware influence</td><td>1.32071</td><td>2.55782</td><td>0.12854</td><td>10.275</td><td>0.000</td></tr><tr><td>Opinion leader</td><td>2.99242</td><td>2.46955</td><td>0.12410</td><td>24.113</td><td>0.000</td></tr><tr><td>Bridge</td><td>4.11111</td><td>2.58090</td><td>0.12970</td><td>31.698</td><td>0.000</td></tr></table>

## 5.3. Download rate

The download rate can be viewed as the number of coupon receivers who want to redeem this coupon; the number of downloads was obtained from our database record, and is expressed as:

$$
\mathrm{DR} = \frac {\Phi d o w n l o a d}{\Phi r e c e i v e d},\tag{22}
$$

where Φdownload is the total number of coupons downloaded and Φreceived indicates the total number of coupon receivers The descriptive statistics for DR is as follows (Table 5). # of coupon received is the total number of the coupons received by all receivers and # of coupon downloaded is the total number of the received coupons which are finally downloaded. Fig. 6 shows the download rates of the coupon for the diferent difusion strategies.

t-Tests were used to evaluate the significance of the diference between our approach and the other approaches. The results are shown in Table 6, and these show that social difusion has a significant confidence interval of 95% compared to the other approaches. That is to say, our social difusion approach has the best performance during the coupon difusion and has the highest coupon redemption willingness among four difusion approach.

## 5.4. Coupon efectiveness

We consider two indicators when evaluating the coupon efective ness in the proposed mechanism: recommended coupon likeness and sender appropriateness. The data were obtained from the coupon receiver feedback questionnaire completed after visiting the coupon webpage. The scoring rate ranges between 1 and 5; a higher score represents more agreement with the question. From Fig. 7, we can see that the targeted social difusion approach had the highest coupon likeness with a score of 4.11. The second highest was the topic-aware influence approach with 3.95; the opinion leader approach achieved 3.26; and the bridge approach got the lowest score with 3.21. Fig. 8 shows the endorser appropriateness measurement for the coupon dif fusion. We can see that the social difusion approach achieved an appropriateness score of 4.13; the topic-aware influence approach achieved 3.63; the opinion leader approach achieved 3.42; and the bridge approach achieved 2.63. The results show that the choice of coupon endorsers has a significant impact on the coupon receivers.

![](/api/attachments/F27VJZ6K/fulltext/images/98a2701bc27776ec7132fa0d3b17b486119041a3aeacf38d3259f5ab97304b6a.jpg)  
Fig. 5. Target coverage rate for the four coupon dissemination strategies.

## 5.5. Extended comparisons

## 5.5.1. Average sharing times for the coupon categories

In this section, we examine which type of coupon had the highest sharing rate using the proposed social coupon difusion approach. This can provide marketers with a reference when planning coupon propagation strategies. In the coupon category tree, there are five grand parent categories: “Computers, Telecommunications & Consumer Electronics” (3C), “Consumer Products”, “Home & Living”, “Health & Beauty” and “Entertainment”. We evaluate the average number of shares (ANS) for each category. The results are shown in Fig. 9.

The average number of shares indicates that the “Home & Living” coupon had the worst performance in terms of coupon difusion, with 3.68 average shares, while the “Entertainment” coupon showed the best performance. These results can provide a reference for marketers when creating social coupon difusion strategies. Though the “home & living” category generally has a higher face value discount, this category has the features of lower frequency of purchase and penetration [42], which outbalance the face value efect and result in the lowest sharing ratio. Coupons were more efective for entertainment, health and beauty and 3C products; people had much a greater willingness to share these types of coupons (travel, books/music/movies, beauty/health and electronics/computers) with their friends. This phenomenon also reveals that providing coupons (or discount) for entertainment, health and beauty and 3C products will attract more attention and increase purchase intentions as the target customers of these categories of products are younger generation people who are more familiar with and get used to information sharing on social media. Besides, a few studies also show that the youth is more toward to receptive mobile coupons [15,48]. The younger consumers prefer using the convenient digital medium and services than traditional coupons. Most traditional coupons are focused on daily necessities while digital coupons are focused on services such as restaurants, tour or travel agencies, and beauty parlors [24].

Table 3  
Descriptive statistics of target coverage rate.

<table><tr><td></td><td>Bridge</td><td>Opinion leader</td><td>Topic-aware influence</td><td>Social diffusion</td></tr><tr><td># of targeted customers who received coupons</td><td>381</td><td>711</td><td>1091</td><td>1647</td></tr><tr><td># of targeted customers</td><td>982</td><td>1652</td><td>2021</td><td>2426</td></tr><tr><td>TCR</td><td>0.3880</td><td>0.4304</td><td>0.5398</td><td>0.6789</td></tr></table>

Table 4  
Statistical verification results based on TCR measurement.

<table><tr><td>Paired group</td><td></td><td>Mean</td><td>Std. deviation</td><td>Std. error mean</td><td>T</td><td>Sig. (two-tailed)</td></tr><tr><td rowspan="3">Social diffusion vs.</td><td>Topic-aware influence</td><td>0.139100</td><td>0.41909</td><td>0.03422</td><td>4.065</td><td>0.000</td></tr><tr><td>Opinion leader</td><td>0.1391</td><td>0.49120</td><td>0.49120</td><td>6.196</td><td>0.000</td></tr><tr><td>Bridge</td><td>0.2909</td><td>0.33098</td><td>0.02702</td><td>10.764</td><td>0.000</td></tr></table>

## 5.5.2. Coupon receiver support comparison

In this section, we compare the diference between the aspects of coupon receiver support versus non-support. Coupon receiver support indicates that we give endorsers a recommended list telling them which coupon should be delivered to which friend (the target consumers for the coupon), while non-support indicates that after identifying the coupon endorsers, no coupon receiver suggestions were made. This comparison reveals the importance and efectiveness of our mechanism in providing selected endorsers with a recommended list.

From the results as shown in Fig. 10, we can see the significant efectiveness of coupon receiver support; it can reduce the burden on the endorser in terms of choosing suitable coupon receivers, decrease negative impressions and mitigate damage to social capital from spam difusion. In addition, the recommended list of recipients can help marketers achieve higher sharing, target coverage, coupon efectiveness and download rates.

## 6. Discussion and conclusion

Today, it is dificult to separate our lives from social media, which ofer people convenient and plentiful services in daily life. With multiple online coupon distribution channels, there are now more choices than ever before when planning shopping lists for consumers. However, there is still a lack of an eficient way for marketers to distribute coupons. Consumers need to expend time and efort in collecting coupons that they like or need. In addition, consumers encounter a problem when sharing excessive discount information with all of their friends, since this will incur a negative reaction. To solve this problem, we propose a social coupon difusion mechanism; this uses a process of social referral by identifying endorsers with high coupon proneness and sharing willingness to difuse coupons to their friends. The characteristic of coupon proneness is proved in our experiments to increase willingness to share coupons and to achieve a higher target coverage rate than other approaches. We also consider the coupon receivers' preferences and location data when planning the endorser difusion match list, which helps the endorsers to select the most suitable friends to receive this coupon.

Our proposed mechanism utilizes theories of social influence and consumer psychology to improve sharing intention. The mechanism was empirically verified by experiments conducted on the popular social networking site Facebook. The experimental results indicate that our social coupon difusion mechanism performs better than three other commonly used coupon difusion approaches in terms of average sharing rate, target coverage rate, coupon efectiveness and coupon download rate. This mechanism can help marketers propagate coupons to the right endorsers and the right customers, widely and continuously.

![](/api/attachments/F27VJZ6K/fulltext/images/9431d8b104ef94b97e394d566b93f93572e7a01021109cd539c503db777c8b7d.jpg)  
Fig. 6. Download rates for the coupon for the four difusion strategies.

## 6.1. Research contributions

The contributions and implications of this study in terms of innovation are as follows. First, from the viewpoint of system innovation, social networks have become the most popular advertising media for businesses, while little research has examined coupon difusion mechanisms using social couponing with social networks. Our paper is one of the first to identify the coupon proneness of a user of a social network in order to create an efective social couponing dissemination mechanism. Second, from the viewpoint of methodology, we consider the factors of individual preference and location to recommend personalized coupon for target consumers; we also take coupon proneness and sharing willingness into consideration when finding an appropriate coupon endorser for social couponing. Further, we take advantage of social influence (a measure of social similarity and social interaction between the endorser and the target consumer) to reduce the negative impressions of coupon advertisements and to increase the willingness of coupon redemption, achieving the marketer's objective of retaining customers. Fourth, from the viewpoint of mechanism performance, we achieve a better coupon sharing rate, showing that our mechanism has a higher coupon exposure rate and a higher target coverage rate than other difusion approaches. Seed endorsers are interested in the received coupon and are willing to share it with their friends via word of mouth. The better download rate reveals that the coupon receivers felt that the received coupon was practical and resonated with them. Fifth, from the viewpoint of factor efect, we examine the impact of diferent social factors (social information and tie strength) on social coupon difusion. We show a social endorsing approach considering more social information and stronger social tie will perform better. Lastly, from the viewpoint of practice, our mechanism shows that providing a recommended coupon receiver list can increase the efectiveness of coupon difusion and can reduce the burden on the endorser in terms of choosing appropriate receivers, avoiding negative impressions from spam dissemination. Furthermore, the experiments show that the social coupon diffusion mechanism is most effective for entertainment. health and beauty and 3C products. This mechanism can be easily applied by marketers with a limited advertising budget to create a large and positive response from consumers on social networking sites.

Table 5  
Descriptive statistics of download rate.

<table><tr><td></td><td>Bridge</td><td>Opinion leader</td><td>Topic-aware influence</td><td>Social diffusion</td></tr><tr><td># of coupon downloaded</td><td>132</td><td>289</td><td>512</td><td>987</td></tr><tr><td># of coupon received</td><td>381</td><td>711</td><td>1091</td><td>1647</td></tr><tr><td>DR</td><td>0.3465</td><td>0.4065</td><td>0.4693</td><td>0.5993</td></tr></table>

Table 6  
The statistical verification results of coupon download measurement.

<table><tr><td>Paired group</td><td></td><td>Mean</td><td>Std. deviation</td><td>Std. error mean</td><td>T</td><td>Sig. (two-tailed)</td></tr><tr><td rowspan="3">Social diffusion vs.</td><td>Topic-aware influence</td><td>0.12226</td><td>0.29523</td><td>0.02952</td><td>4.141</td><td>0.000</td></tr><tr><td>Opinion leader</td><td>0.18506</td><td>0.19838</td><td>0.01984</td><td>9.328</td><td>0.000</td></tr><tr><td>Bridge</td><td>0.24506</td><td>0.04893</td><td>0.04895</td><td>5.006</td><td>0.000</td></tr></table>

![](/api/attachments/F27VJZ6K/fulltext/images/6089e7b0e9643ebe67da45394f8ad11964bece8f927f6b7d9b9d57ed1a04dae0.jpg)  
Fig. 7. Coupon receiver's likeness for the four coupon difusion strategies.

## 6.2. Research limitations

The limitations of this research are as follows. Firstly, due to constraints in terms of time and experimental platform, the number of participants in the experiment was lower than realistic for the users of a social networking site. We cannot retrieve data from all Facebook users; the experiments can only reflect the behavior of a percentage of the users. Secondly, due to Facebook's privacy policy, it was necessary to gain the user's agreement to collect their social data, including friend list, posts, check ins. fan pages liked. location. likes and joint social groups. We also cannot access a user's friends or social data without permission; this was the major limitation on our experiment, since the interactions between users are significant factors determining the ap propriate coupon receiver. Thirdly, due to time constraints and the scope of the experiment, our coupon category tree had only 66 nodes for user preferences and coupon type matching. The accuracy of pre ference matching may be afected by the number of categories and classifications. Fourthly, the purpose of our mechanism is to find endorsers who have a high level of willingness to share coupons with their friends, and who can influence coupon receivers to increase the desire to purchase. This method avoids coupon spamming and negative impressions, but if the coupon difusion mechanism is changed to spread coupons to all of a user's friends on a social network site, the framework may produce diferent results, and may achieve a higher target coverage rate. Fifthly, in order to achieve consistency in the sharing intention of endorsers, the sharing reward in our experiments was an additional 10% discount for the endorsers. However, this may be diferent for diferent types of business. Lastly, this mechanism cannot trace the propagation path for those coupon receivers who are not participants recorded in our database. If coupon receivers did not provide feedback after receiving a coupon, we could not identify who sent them the coupon.

![](/api/attachments/F27VJZ6K/fulltext/images/99d4b5fc1344590c08ca209f7f3a0dd3b55fa059bf80874fdb11f9e2b3f13df7.jpg)  
Fig. 8. Endorser appropriateness for the four difusion strategies.

![](/api/attachments/F27VJZ6K/fulltext/images/4226d26d7dabdc825db9d6f1f9aa8e39aa3220e600a4c1ff36575887b2f18960.jpg)  
Fig. 9. Average number of shares for coupon categories.

## 6.3. Future studies

There are several research directions which could be further ex panded. First, if we could predict the difusion path and exposure range, this would help a business to control the budget for coupon advertising and plan customized coupon rewards or promotion strategies for the coupon receivers. Second, if we can use equilibrium theory to simulate the level of price discount that can trigger a specific consumer's purchasing intention, this would provide a more accurate result when identifying the coupon proneness of a user and increase the coupon diffusion effectiveness. Third, we can enhance the preference analysis module using a coupon taxonomy and concept expansion [6] to infer the types of coupon a consumer might need, to improve the accuracy of coupon recommendation. Fourth, we can establish a dynamic coupon difusion mechanism which can adjust the accuracy coupon recommendation based on the user's feedback. For instance, if the coupon receiver was not interested in beauty products, the next coupon recommendation for this customer would not include coupons related to beauty. Fifth, besides coupon endorser, coupon content and face value also have impact on the coupon redemption. The convolutional efect of face value and social endorsing behavior on the coupon redemption is a more complicated issue and could be deeper investigated. Sixth, the customer behavior in price competition with targeted coupons is a desirable issue to study [16,38]. We can further examine the competition efect between firms adopting social coupon service. Finally, if the social coupon difusion could be carried out simultaneously using diferent social media, this could provide a wider advertising exposure for the coupon. This may help businesses to target consumers on diferent platforms and to increase the speed of dissemination of the coupons.

![](/api/attachments/F27VJZ6K/fulltext/images/949c61ce8978188d946455d465a8582f470c4be10b8ffa80ca93fed4acd7e6a5.jpg)  
Fig. 10. Average number of shares for supported and non-supported strategies.

## Acknowledgments

This research was supported by the National Science Council of Taiwan (Republic of China) under grant NSC 104-2410-H-028-MY3.

## References

[1] A. Albadvi, M. Shahbazi, A hybrid recommendation technique based on produc category attributes, Expert Systems with Applications 36 (9) (2009) 11480–11488.

[2] D. Astrid, M. Kleijnen, Coupons going wireless: determinants of adoption of consumer intentions to redeem mobile coupons, Journal of Interactive Marketing 22 (3) (2008) 23–39.

[3] X. Bai, J.R. Marsden, W.T. Ross Jr., G. Wang, How e-WOM and local competition drive local retailers' decisions about daily deal oferings, Decision Support Systems 101 (2017) 82–94.

[4] S. Banerjee, R.R. Dholakia, Mobile advertising: Does location-based advertising work? International Journal of Mobile Marketing 3 (2) (2008) 68–74.

[5] S. Barat, C. Amos, A. Paswan, G. Holmes, An exploratory investigation into how socioeconomic attributes influence coupons redeeming intentions Journal of Retailing and Consumer Services 20 (2) (2013) 240–247.

[6] R. Blanco, M. Matthews, P. Mika, Ranking of daily deals with concept expansion, Information Processing & Management 51 (4) (2015) 359–372.

[7] J.W. Byers, M. Mitzenmacher, G. Zervas, Daily deals: prediction, social difusion, and reputational ramifications, The Fifth ACM WSDM Conference, Seattle, WA, 2012.

[8] B. Californian, Market intelligence: Online coupon use doubles among metro adults, Retrieved from http://www.bakersfieldcalifornian.com/business/x2098053484/ Market-intelligence-Online-coupon-use-doubles-among-metro-adults.

[9] G. Chakraborty, C. Cole, Coupon characteristic and brand choice, Psychology and Marketing 8 (1991) 145–159.

[10] P. Chandon, B. Wansink, G. Laurent, A benefit congruency framework of sales promotion efectiveness, Journal of Marketing 64 (4) (2000) 65–81.

[11] S. Chen, G. Wang, W. Jia, κ-FuzzyTrust: eficient trust computation for large-scale mobile social networks using a fuzzy implicit social graph, Information Sciences 318 (2015) 13–143

[12] Consumer Reports, Best coupon apps for grocery shopping: you don't have to be a coupon-clipping maven to save big, Retrieved from http://www.consumerreports. org/cro/2013/08/best-coupon-apps/index.htm.

[13] CKIP, Chinese knowledge and information processing, Retrieved from, 2018. http://ckip.iis.sinica.edu.tw/CKIP/engversion/index.htm

[14] D. Crandall, D. Cosley, D. Huttenlocher, J. Kleinberg, S. Suri, Feedback efects between similarity and social influence in online communities, Proceedings of the 14th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, ACM. 2008.

[15] A. Dickinger, M. Kleijnen, Coupons going wireless: determinants of consumer intentions to redeem mobile coupons. Journal of Interactive Marketing 22 (3) (2008 23–39.

[16] J.P. Dubé, Z. Fang, N. Fong, X. Luo, Competitive price targeting with smartphone coupons, Marketing Science 36 (6) (2017) 944–975.

[17] M. Duggan, N.B. Ellison, N.B. Lampe, A. Lenhart, M. Madden, Social media update 2014, Retrieved from http://www.pewinternet.org/2015/01/09/social-mediaupdate-2014/.

[18] M. Granovetter, Threshold models of collective behavior, American Journal of Sociology 83 (1978) 1420–1443.

[19] GSMA, Bridging the Gender Gap: Mobile Access and Usage in Lowland Middle Income Countries, (2015)

[20] C.M. Heilman, K. Nakamoto, A.G. Rao, Pleasant surprises: consumer response to unexpected in-store coupons Journal of Marketing Research 39 (2) (2002) 242-252.

[21] Q. Huang, R.M. Davison, H. Liu, An exploratory study of buyers' participation intentions in reputation systems: the relationship quality perspective, Information & Management 51 (8) (2014) 952–963.

[22] J. Goldenberg, B. Libai, E. Muller, Talk of the network: a complex systems look at the underlying process of word-of-mouth, Marketing Letters 12 (3) (2001) 211–223.

[23] J. Jin, S.J. Turner, B.S. Lee, J. Zhong, B. He, HPC simulations of information pro pagation over social networks, Procedia Computer Science 9 (2012) 292–301.

[24] H. Kang, M. Hahn, D.R. Fortin, Y.J. Hyun, Y. Eom, Efects of perceived behavioral control on the consumer usage intention of E-coupons. Psychology and Marketins 23 (10) (2006) 841–864.

[25] D. Kempe, J. Kleinberg, E. Tardos, Maximizing the spread of influence in a social network, ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD), 2003.

[26] R.V. Kozinets. K. de Valck. A.C. Woinicki. S.LS. Wilner. Networked narratives understanding word-of-mouth marketing in online communities, Journal of

Marketing 74 (2010) 71–89.

[27] V. Kumar, B. Rajan, Social coupons as a marketing strategy: a multifaceted perspective, Journal of the Academy of Marketing Science 40 (1) (2012) 120–136.

[28] M.K.O. Lee, N. Shi, C.M.K. Cheung, K.H. Lim, C.L. Sia, Consumer's decision to shop online: the moderating role of positive informational social influence, Information & Management 48 (2011) 185–191.

[29] K. Li, T.C. Du, Building a targeted mobile advertising system for location-based services, Decision Support Systems 54 (1) (2012) 1–8.

[30] Y. Li, Z.A. Bandar, D. McLean, An approach for measuring semantic similarity between words using multiple information sources, IEEE Transactions on Knowledg and Data Engineering 15 (4) (2003) 871–882.

[31] Z. Li, C. Wang, S. Yang, C. Jiang, X. Li, Lass: local-activity and social-similarity based data forwarding in mobile social networks, IEEE Transactions on Parallel and Distributed Systems 26 (1) (2015) 174–184

[32] L.F. Lin, Y.M. Li, W.H. Wu, A social endorsing mechanism for target advertisement diffusion. Information & Management 42 (2015) 982–997.

[33] T.T. Nagle, R.K. Holden, Strategy and Tactics of Pricing, Pearson Education Limited, 2013.

[34] Nielsen, SHOPPING lists: how mobile helps consumers tick all the boxes, Retrieved from, 2014. http://www.nielsen.com/us/en/insights/news/2014/shopping-lists how-mobile-helps-consumers-tick-all-the-boxes.html.

[35] Nielsen, Under the influence: consumer trust in advertising, Retrieved from, 2013. http://www.nielsen.com/us/en/insights/news/2013/under-the-influence consumer-trust-in-advertising.html

[36] A. Nikander, Determinants of Consumer Intentions to Redeem Mobile Coupons, (2011).

[37] B.S. Ong, Attitudes, perceptions, and responses of purchasers versus subscribersonly for daily deals on hospitality products, Journal of Hospitality Marketing and Management 24 (2) (2015) 180–201.

[38] J. Pancras, K. Sudhir, Optimal marketing strategies for a customer data inter mediary,Journal of Marketing Research XLJV (2007) 560–578

[39] J. Pancras, R. Venkatesan, B. Li, Investigating the value of competitive mobile loyalty program platforms for intermediaries and retailers, Marketing Science Institute Working Paper Series, 2015, pp. 15–107.

[40] C. Pescher, M. Spann, Relevance of actors in bridging positions for product-related information difusion, Journal of Business Research 67 (8) (2014) 1630–1637.

[41] C.W. Phang, C. Zhang, J. Sutanto, The influence of user interaction and participation in social media on the consumption intention of niche products, Information & Management 50 (8) (2013) 661–672.

[42] N. Ponder, Consumer Attitudes and Buying Behavior for Home Furniture, Franklin Furniture Institute, 2013.

[43] R. Reagans, Close encounters: analyzing how social similarity and propinquity contribute to strong network connections, Organization Science 22 (4) (2011) 835–849.

[44] I. Roelens, P. Baecke, D.F. Benoit, Identifying influencers in a social network: the value of real referral data, Decision Support Systems 91 (2016) 25–36.

[45] P. Rossi, R.E. McCulloch, G.M. Allenby, The value of purchase history data in target marketing, Marketing Science 15 (4) (1996) 321–340.

[46] M.A. Russell, Mining the Social Web: Data Mining Facebook, Twitter, LinkedIn, Google +, GitHub, and More, O'Reilly Media. Inc, Sebastopol, 2013

[47] K. Saito, M. Kimura, K. Ohara, H. Motoda, Super mediator – a new centrality measure of node importance for information diffusion over social network. Information Sciences 329 (2016) 985–1000.

[48] A. Scharl. A. Dickinger, J. Murphy, Diffusion and success factors of mobile marketing. Electronic Commerce Research and Applications 4 (2) (2005) 159–173

[49] A. Smith, 35% of American Adults Own a Smartphone, July 11 Pew Research Center, 2011.

[50] S. Swaminathan, K. Bawa, Category-specific coupon proneness: the impact of individual characteristics and category-specific variables, Journal of Retailing 81 (3) (2005) 205–214.

[51] J. Tierney, Customers want online shopping options, Retrieved from, 2013. http:/ loyalty360.org/resources/article/customers-want-online-shopping-options.

[52] LA. Villella, Digital coupons drive sales, trial, and brand lovalty, Retrieved from http://www.bardadvertising.com/blog/digital-coupons-drive-sales-trial-brandloyalty/.

[53] L. Wang, R. Gopal, R. Shankar, J. Pancras, On the brink: predicting business failure with mobile location-based checkins, Decision Support Systems 76 (2015) 3–13.

[54] C. Wen, B.C.Y. Tan, K.T.T. Chang, Advertising efectiveness on social network sites: an investigation of tie strength, endorser expertise and product type on consumer purchase intention, Proceedings of the International Conference on Information Systems (ICIS), Phoenix, Arizona, United States, 2009, pp. 15–18.

[55] H. Xu, H.H. Teo, Alleviating consumers' privacy concerns in location-based services: a psychological control perspective, ICIS 2004 Proceedings, 2004, p. 64.

[56] C.W. Yoo, G.L. Sanders, J. Moon, Exploring the efect of e-WOM participation on eloyalty in e-commerce, Decision Support Systems 55 (3) (2013) 669–678.

[57] X. Zhao, Q. Tang, S. Liu, F. Liu, Social capital, motivations, and mobile coupon sharing, Industrial Management & Data Systems 116 (2016) 188–206.

[58] D.H. Zhu, Y.P. Chang, J.J. Luo, X. Li, Understanding the adoption of location-based recommendation agents among active users of social networking sites, Information Processing & Management 50 (5) (2014) 675–682.

[59] T. Zhu, B. Wang, B. Wu, C. Zhu, Maximizing the spread of influence ranking in social networks, Information Sciences 278 (0) (2014) 535–544.

[60] C.N. Ziegler, G. Lausen, L. Schmidt-Thieme, Taxonomy-driven computation of product recommendations, Proceedings of the Thirteenth ACM International Conference on Information and Knowledge Management, ACM, 2004.

[61] X. Zou, K.W. Huang, Leveraging location-based services for couponing and

## infomediation, Decision Support Systems 78 (2015) 93–103.

Yung-Ming Li is a Professor at the Institute of Information Management, National Chiao Tung University in Taiwan. He received his Ph.D. in Information Systems from the University of Washington. His research interests include network science, Internet economics, and business intelligence. His research has appeared in IEEE/ACM Transactions on Networking, INFORMS Journal on Computing, Decision Sciences, International Journal of Electronic Commerce, Information and Management, Decision Support Systems, European Journal of Operational Research, International Conference on Information Systems (ICIS), Workshop on Information Technology and Systems (WITS),

## among others.

Jyh-Hwa Liou is a Ph.D. student at the Institute of Information Management, National Chiao Tung University in Taiwan. Her research interests include electronic commerce and business intelligence. Her research has appeared in Decision Support Systems.

Ching-Yuan Ni received her M.S. degree from the Institute of Information Management, National Chiao Tung University in Taiwan and B.S. degree in Information Management from the National Yunlin University of Science and Technology, Taiwan. Her research interests focus on social commerce and mobile computing.
