---
otero_id: 8794
otero_key: "C5T8MDTR"
title: "Building a targeted mobile advertising system for location-based services"
authors: "Kai Li; Timon C. Du"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.02.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Building a targeted mobile advertising system for location-based services

Kai Li <sup>a</sup>, Timon C. Du <sup>b,</sup>⁎

<sup>a</sup> Department of Industrial Engineering, Teda College, Nankai University, China

<sup>b</sup> Department of Decision Sciences and Managerial Economics, The Chinese University of Hong Kong, Hong Kong

## a r t i c l e i n f o

Article history: Received 21 October 2010 Received in revised form 1 November 2011 Accepted 9 February 2012 Available online 21 February 2012

Keywords: Mobile advertising Pull strategy Targeted advertising Intelligent searching

## a b s t r a c t

Over the years, mobile advertising has grown to become a technology that allows an advertiser to promote products or services to targeted users ef<sup>fi</sup>ciently and effectively. This is because the ubiquitous nature of mobile devices can provide contextual information and allow users to demonstrate preferences. This study proposes a targeted mobile advertising system (TMAS) that works as a platform to provide both merchants and consumers with context-aware advertisements. The approach integrates the advantages of both mobile and targeted advertising to allow merchants to disseminate location-based targeted advertisements while providing pull-type and personalized advertisements for consumers. To demonstrate the TMAS, we build a platform to provide highly relevant advertising to consumers and to guarantee that advertisements have an equal opportunity of being presented to consumers.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Location-based services aim to offer personalized mobile transactions for targeted individuals in speci<sup>fi</sup>c locations at speci<sup>fi</sup>c times [45], using the knowledge of the location of an object and/or individuals [38]. The growth of mobile phones has provided an opportunity for such services. Mobile phones are by far the most popular personal communications device, and, as new multi-function mobile phones such as smart phones are widely adopted, they have emerged as a coveted media platform for marketers because they are personal, accessible anytime and anywhere, and location-aware [28,40,44].

Global mobile marketing spending is expected to be worth around \$19 billion by 2011 [8]. However, the most vital problem for merchants is how to reach their valuable targeted audience. That is, how best to deliver an advertisement to the right mobile user in the right context effectively and ef<sup>fi</sup>ciently remains an issue to be solved [13,49,52].

Currently, the most common mobile advertisement formats are Short Message Service (SMS) and Multimedia Message Service (MMS) [31]. These are push-type technologies that send messages proactively to mobile users [9]. Typically, push marketing is better for companies who have an established relationship with users, who have granted permission to receive such messages. This is referred to as permission-based marketing [6]. However, the mobile phone can be used as a user-driven media device to enhance the dynamics of business-to-consumer relationships [43,33]. It can be used for pull-type marketing that sends information based on consumer requests [6]. This mode is most suitable for merchants with simple, time-limited, and location-related advertisements. Advertisements can even be restricted by quota, such as the promotion of a regional company, coupons in a local mall, a community yard sale, and so on. Moreover, future customers with smart phones can actively demand promotional information. Compared with push-based advertising, this pull-type approach, which allows customers to have greater involvement, has gained in popularity.

This paper proposes a targeted mobile advertising system (TMAS) for mobile advertisements based on pull-type marketing strategies. It integrates the strengths of targeted advertising techniques, pull-type marketing, and mobile advertisement technology. The framework not only allows consumers to identify and access personalized advertisements, but also enables the advertisers to design and present contextaware targeted advertisements. The remainder of the paper is organized as follows. Section 2 reviews the related literature on targeted mobile advertising and pull-type advertising. Section 3 outlines the system framework, and the demonstration is presented in Section 4. The <sup>fi</sup>nal section highlights the contributions of the research and concludes the paper.

## 2. Targeted mobile advertising

Moving into the Internet age, the ability of Internet advertising to provide customization and personalization for web-based stores has been well recognized. Tools such as data mining, statistics, arti<sup>fi</sup>cial intelligence, and rule-based matching are popular for building recommendation systems [22]. However, similar to the <sup>fi</sup>ndings in [36], it was found that direct exposure to Internet advertising might not enhance web purchasing. Rather, the decision to purchase is determined by consumers' interests before sur<sup>fi</sup>ng Internet stores [23]. Thus, a pull strategy is more effective than a push strategy on the Internet. Similarly, the contextual appeal to consumers is more important to advertisers on the Internet. With the development of mobile devices, the collection of consumer information, such as location, has become more convenient. Thus, mobile commerce provides a venue for context-aware, targeted advertisements to advertisers and personalized pull-type advertisements for consumers.

The purpose of providing targeted advertisements is to increase the effectiveness of advertising by ensuring the right person receives the right message at the right time [1]. Scharl et al. [35] suggested that targeted advertisements using mobile devices could provide consumers with personalized information, including information such as time, location, and interests. Thus, providing a targeted mobile advertisement involves both scheduling and personalization issues. Here, scheduling refers to which advertiser should send out promotions to whom at what time, given a limited broadcasting capacity, to maximize positive customer response and revenues for the merchant who pays for the advertisement. De Reyck and Degraeve [14] used integer programming to solve the problem and then developed a decision support system for automatically scheduling and optimizing the broadcasting of advertisements to mobile phones [15]. Similarly, Tripathi and Nair [42] applied the same technology with contact history information to better schedule the delivery of advertisements.

Personalized advertising is also important and challenging to advertisers. Unlike primary targeted advertisements that simply deliver a speci<sup>fi</sup>c advertisement to segmented customers in a market, personalized advertising is more individualized [21]. Personalization aims to deliver suitable advertisements to a designated user rather than to a group of users. Generally speaking, an advertiser can personalize advertisements based on users' pro<sup>fi</sup>les and contextual information [5]. User pro<sup>fi</sup>les include their preferences and demographics [17], while contextual information includes location, time, user activities, and weather [49]. That is, users' long-term preferences are normally stored in pro<sup>fi</sup>les while their short-term interests are available from the contextual information [25]. Data mining techniques have been widely used in targeted advertising, especially on the Internet [27]. Techniques such as segmentation and clustering can be used to discover web access patterns and to solve other advertisement problems [10]. For example, through demographic analysis it was found that the unmarried working youth segment has a higher propensity to access pull-type mobile advertisements [32]. Similarly, the classi<sup>fi</sup>cation model can be used to match Web sessions with advertisements [27]. Other than data mining techniques, fuzzy logic can also be used to target advertising based on user pro<sup>fi</sup>les [50]. The assignment of appropriate advertisements to each active user can be accomplished according to the fuzzy rules stored in the system.

The delivery method of targeted mobile advertisements can be differentiated into push and pull marketing strategies [9]. Both strategies need to select targeted mobile users carefully. In push advertising, messages are proactively sent out to mobile users [9]. That is, information and marketing activities <sup>fl</sup>ow from the producer to the consumer [39], which is cheap and ef<sup>fi</sup>cient [34]. SMS mobile advertising is one of the typical applications adopting a push strategy in the mobile environment [6]. However, acquiring permission from mobile users to deliver messages is always a problem [6]. In contrast, using a pull strategy, a mobile user pulls mobile advertising for his her own use [6]. It is arguable that pull advertising might blur the line between advertising and service [20]. There are some successful applications using this approach. For example, Okazaki [31] proposed a mobile advertising platform, called “Tokusuru Menu”, that allows subscribers to access promotional information delivered by various companies. Mahmoud and Yu [29] developed a mobile agent platform to compare shopping items in a mobile environment. Choi [11] proposed a GPS/Web-enabled mobile search mechanism based on a user's physical location and search intentions so that they receive more personalized and locally targeted search results. A similar approach was taken by Yuan and Tsao [52], who developed a mobile advertising system integrating both push and pull modes, called MALCR.

Table 1 presents a comparison between this study and a number of other systems described in the literature. The targeted mobile advertising system (TMAS) proposed in this study is based on pulltype marketing strategies and anticipates the active involvement of consumers. Moreover, advertisers can use the framework to design context-aware targeted advertisements.

## 3. The targeted mobile advertising system

Merchants may prefer a platform that can promote a product to consumers in a timely, effective, and low cost way. Similarly, consumers would prefer to receive relevant and useful promotions. For example, a scenario in which a well-known pizza restaurant in a shopping mall wishes to promote its popular but high pro<sup>fi</sup>t margin triple sausage pizzas to draw the attention from nearby customers before the peak lunchtime hour. The promotion may be limited to ten pizzas selling between 11:30 and 12:00. The advertisement should be easily prepared by the owner and distributed via a platform to the mobile phones of targeted customers who are nearby or whose favorite place to eat is in this shopping mall.

In this study, we develop a targeted mobile advertising system (TMAS) for mobile advertising. TMAS works as a platform linking merchants and consumers (mobile phone users). It uses personalization and pull techniques to deliver targeted advertisements that can better match consumers' needs. Speci<sup>fi</sup>cally, it allows consumers to actively specify their demands, and a list of personalized advertisements will be delivered to them based on their contextual information and preferences. Similarly, a merchant can prepare an advertisement and access those consumers who are interested in it, and then further acquire consumer feedback from the platform to adjust their advertisement content and strategy.

The framework of TMAS, presented in Fig. 1, has three modules, Advertisement Management, User Pro<sup>fi</sup>le Management, and Advertisement Intelligent Searching, which interact with databases and users. The Advertisement Management module manages the content of advertisements and the properties of targeted customers. The advertiser is allowed to revise both the content and properties. Commercial software, such as x10advertisements and csBanner (http:// www.cgiscript.net), can be used for this purpose. The User Pro<sup>fi</sup>le Management module is used for creating pro<sup>fi</sup>les for new consumers and updating existing ones. The Advertisement Intelligent Searching module, the key to TMAS, provides personalized search results according to contextual information, including the location, demographics, and preferences of consumers.

Comparison between TMAS and other systems.

<table><tr><td></td><td>Okazaki [31]</td><td>Mahmoud and Yu [29]</td><td>Choi [11]</td><td>Yuan and Tsao [52]</td><td>This study (TMAS)</td></tr><tr><td>Location-based service</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Context-aware information</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Mobile agent</td><td>No</td><td>Yes</td><td>No</td><td>No</td><td>No</td></tr><tr><td>Advertising platform</td><td>Yes</td><td>Yes</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>Personalized advertisements</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Pull-type mobile advertisements</td><td>Yes</td><td>No</td><td>No</td><td>Yes</td><td>Yes</td></tr><tr><td>Consumers&#x27; active involvement</td><td>No</td><td>No</td><td>No</td><td>No</td><td>Yes</td></tr><tr><td>Targeted advertisements</td><td>No</td><td>No</td><td>Yes</td><td>No</td><td>Yes</td></tr></table>

![](/api/attachments/C5T8MDTR/fulltext/images/59504f29ac2c5dae95e47a6af9002b9dbf2e55f667fd3687de3776d135e7ae5d.jpg)  
Fig. 1. Framework of TMAS

Four kinds of information are collected from consumers. The <sup>fi</sup>rst is the keywords a consumer uses to locate a speci<sup>fi</sup>c promotion. This is considered to be the most direct and ef<sup>fi</sup>cient source of information retrieval [3], which helps the system to identify the needs of users and quickly reduce the range of the search. The second source of information is the wide-range of contextual data that can be collected from consumers in real-time, including location [26,46], time [2,47], weather [24], and others. Third, in location-based services, the context-aware nature of a mobile device represents an important advantage for providing useful and relevant content, products, or services [19,41]. Similarly, consumers' demographic data are also useful in location-based services. Finally, the action and feedback from consumers can be used not only to update user pro<sup>fi</sup>les but also to help advertisers to understand the real needs of customers and to improve advertisement strategies.

![](/api/attachments/C5T8MDTR/fulltext/images/8b4aed8eceb81580a96385782d87a5c8174b96d42f76e33c4397acb4b00c76f9.jpg)  
Fig. 2. Detailed representation of TMAS process in DFD.

Fig. 2 illustrates the procedure of TMAS in IDEF0 format. All mobile advertisements are provided by advertisers through the Advertisement Manager (A1) and are stored in the Database. When a user issues a query, the Advertisement Search Manager (A3) is activated and their contextual and demographic data are collected. The modi-<sup>fi</sup>ed query will be sent to the Advertisement Manager to retrieve advertisements in the Database after referring to their user pro<sup>fi</sup>les. The user pro<sup>fi</sup>le is managed in the Pro<sup>fi</sup>le Manager (A2) and is stored in the Database. In the Advertisement Search Manager, Query Manager (A3.1) analyzes the query based on speci<sup>fi</sup>ed keywords from the consumer and prepares the search. The Search Engine (A3.2) then provides the initial <sup>fi</sup>lter according to the keywords. Finally, the Rank Manager (A3.3) is the kernel process that matches advertisements with consumer's needs (this process will be explained in more detail later). Advertisements of greater interest to the consumer should be ranked at the top. When the search results are presented to the consumer, TMAS will monitor his/her action and collect feedback and then use this information to update the consumer's pro<sup>fi</sup>le. The information will also be stored in the Database to form the advertisements' effectiveness and feedback report that will be used to pull customers' needs to advertisers for later use.

The matching between consumers and advertisements involves a number of factors. First, each consumer has his/her own priority for criteria selection. This is a multi-criteria decision-making (MCDM) process that can take into account a number of attributes for ranking advertisements, such as distance, discount, service level, quota, expiration date, and many others. To solve the problem, attributes such as service level and price level can be represented by fuzzy functions because they do not have clear quantitative boundaries. In this way, we can allow descriptive attributes, such as economy, standard, or deluxe for price range; and bad, medium, or good for service level. Then, membership functions can be used to represent the degree of truth as an extension of valuation. Thus, fuzzy MCDM methods can be adopted for matching purposes. As mentioned, the Advertisement Search Manager is an intelligent searching process that provides personalized mobile advertisements for consumers based on their demographic, preference, and contextual information. Demographic and preference data are two different types of user pro<sup>fi</sup>le data that are often used for pro<sup>fi</sup>le modeling in electronic commerce [4,12]. A user pro<sup>fi</sup>le is an explicit representation of a person's identity and preferences. It is a computer representation of a user model [37].

In TMAS, the Pro<sup>fi</sup>le Manager (A2) manages and updates user pro-<sup>fi</sup>les that are modeled as a vector of weights to represent the interests of the consumer according to different criteria. Speci<sup>fi</sup>cally, the preference vector can be de<sup>fi</sup>ned as $P = ( p _ { 1 } , p _ { 2 } , . . . , p _ { i } , . . . , p _ { m } ) , 0 { \leq } p _ { i } { \leq } 1$ and 1≤i≤m, where $p _ { i }$ denotes the preference of attribute i in a user pro<sup>fi</sup>le. TMAS relies on consumers' preferences to provide personalized mobile advertisements. Thus, maintaining an updated user pro-<sup>fi</sup>le is crucial. Here, we use consumers' historical behavioral data to update their preferences. Speci<sup>fi</sup>cally, when a posted advertisement is chosen by a consumer, the consumer preference will be updated. The self-learning process allows preference vectors to evolve based on empirical data [51]. Suppose a decision space A contains n advertisements that are the result of initial searching $A = \{ a _ { 1 } , a _ { 2 } , . . . , a _ { n } \}$ All advertisements in A have m attributes. If we use $f ( . )$ to represent the mapping between advertisements and their attribute values, we can use $\bar { f ( a _ { j } ) } = ( f _ { 1 } ( a _ { j } ) , f _ { 2 } ( a _ { j } ) , . . . , f _ { i } ( a _ { j } ) , . . . , f _ { m } ( a _ { j } ) ) ^ { T }$ to represent all the attribute values of advertisement $a _ { j } ,$ and $f _ { i } ( a _ { j } )$ to denote the value of attribute i of advertisement $a _ { j } ,$ the MCDM problem can also be described as:

$$
\max _ {a _ {j} \in A} \left\{f (a _ {j}) \right\}.\tag{1}
$$

The domain of each attribute $f _ { i } ( a )$ can be different. It may be [0, 1], or a real number set, or even an evaluation set such as {very good, good, medium, bad, very bad}. It depends on the practical meaning of the attribute, but the domain of the membership function is between 0 and 1. Mostly, the attributes are cardinal. For a categorical attribute with n categories, we can simply treat it as n categorical variables, so we choose to create n binary variables (instead of $n - 1 )$ ). For each categorical variable, value 1 means that the advertisement belongs to this category whereas 0 means it does not. For example, an advertisement has three attributes: $f ( a ) = ( f _ { 1 } ( a ) , f _ { 2 } ( a ) , f _ { 3 } ( a ) ) ^ { T }$ , where $f _ { 3 } ( a )$ is a categorical attri bute with three categories. We create three categorical binary variables $f _ { 3 1 } ( a ) , f _ { 3 2 } ( a ) , f _ { 3 3 } ( a )$ to represent $f _ { 3 } ( a )$ . Then the advertisement's attributes can be represented as:

$$
f (a) = \left(f _ {1} (a), f _ {2} (a), f _ {3 1} (a), f _ {3 2} (a), f _ {3 3} (a)\right) ^ {T}.
$$

Accordingly, consumers' preference vector will be: $P = ( p _ { 1 } , p _ { 2 } , p _ { 3 1 }$ p ,p ). If the membership function of $f _ { i } ( a )$ is represented as $\mu _ { \tilde { f } _ { i } } ( a )$ the MCDM problem can be described as:

$$
\begin{array}{l} \max _ {a _ {j} \in A} \left\{\mu \tilde {f} (a _ {j}) \right\}, \\ \text { where } \mu \tilde {f} (a _ {j}) = (\mu \tilde {f} _ {1} (a _ {j}), \mu \tilde {f} _ {2} (a _ {j}), \dots , \mu \tilde {f} _ {m} (a _ {j})) ^ {T} \in [ 0, 1 ]. \end{array}\tag{2}
$$

Membership function represents the degree of truth as an extension of valuation in fuzzy logic. $f ( a _ { j } ) = ( f _ { 1 } ( a _ { j } ) , f _ { 2 } ( a _ { j } ) , . . . , f _ { i } ( a _ { j } )$ $f _ { m } ( a _ { j } ) ) ^ { T }$ represents all the attribute values of advertisement $a _ { j }$ and $f _ { i } ( a _ { j } )$ denotes the attribute i of advertisement $a _ { j } .$

Generally, most of the commonly used advertising attributes can be divided into two kinds: cost attributes (e.g. distance) and bene<sup>fi</sup>t attributes $( \mathbf { e . g . }$ discount). Cost attributes have a negative relationship with consumers' preference, while bene<sup>fi</sup>t attributes have a positive relationship. However, there may indeed be some non-monotonic attributes, which we did not take into account. In the fuzzy MCDM method, we can treat them as <sup>fi</sup>xed attributes. Fixed attributes have a non-monotonic relationship with preference. Consumers prefer a certain value in these attributes, which is called objective value. The membership of <sup>fi</sup>xed attributes can be calculated by:

$$
\mu_ {\tilde {f} _ {i}} (a) = \frac {f _ {i} ^ {*} (a)}{f _ {i} ^ {*} (a) + | f _ {i} (a) - f _ {i} ^ {*} (a) |},
$$

where $f _ { i } ^ { * } ( a )$ is the objective value of the consumer. Therefore, the non-monotonic attributes can also be incorporated into the “consumer-advertisements matching process”.

The membership degree of all attributes can be calculated by formulas (3), (4) and (5):

$$
\mu_ {\tilde {f} _ {i}} (a) = \frac {\sup \{f _ {i} (a) \} - f _ {i} (a)}{\sup \{f _ {i} (a) \} - \inf \{f _ {i} (a) \}}\tag{3}
$$

$$
\mu_ {\tilde {f} _ {i}} (a) = \frac {f _ {i} (a) - \inf \{f _ {i} (a) \}}{\sup \{f _ {i} (a) \} - \inf \{f _ {i} (a) \}}\tag{4}
$$

$$
\mu_ {\tilde {f} _ {i}} (a) = \frac {f _ {i} ^ {*} (a)}{f _ {i} ^ {*} (a) + | f _ {i} (a) - f _ {i} ^ {*} (a) |},\tag{5}
$$

where inf{f (a)} is the lower bound of $f _ { i } ( a )$ in $\mathsf { A } ,$ and $\operatorname { s u p } \{ f _ { i } ( a ) \}$ is the upper bound o $\mathrm { { \dot { \it ~ f } } } _ { i } ( a ) \mathrm { i n } \mathrm { A } . f _ { i } ^ { * } ( a )$ is the objective value of the consumer.

The least deviation method (LDM) is one of the algorithms for solving multi-criteria decision-making problems [48]. The LDM is based on positive/negative ideal solutions. The positive ideal solution is denoted as $a ^ { + }$ , which means the positive ideal advertisement. However, $a ^ { + }$ is not a feasible solution in $\mathsf { A } ;$ it is just an ideal solution which is formed by integrating the maximum value of each attribute's membership degree $\mu _ { \tilde { f } _ { i } } ( a )$ . Let

$$
\mu_ {\tilde {f} _ {i}} \left(a ^ {+}\right) = \operatorname{Max} \left\{\mu_ {\tilde {f} _ {i}} (a) \right\},
$$

the membership vector of the positive ideal solution can be denoted as: $\left( \mu _ { \tilde { f } _ { 1 } } ( a ^ { + } ) , \mu _ { \tilde { f } _ { 2 } } ( a ^ { + } ) , . . . , \mu _ { \tilde { f } _ { i } } ( a ^ { + } ) , . . . \mu _ { \tilde { f } _ { m } } ( a ^ { + } ) \right)$ .Similarly, let

$$
\mu_ {\tilde {f} _ {i}} (a ^ {-}) = \operatorname{Min} \left\{\mu_ {\tilde {f} _ {i}} (a) \right\},
$$

the membership vector of the negative ideal solution can be denoted as: $\left( \mu _ { \tilde { f } _ { 1 } } ( a ^ { - } ) , \mu _ { \tilde { f } _ { 2 } } ( a ^ { - } ) , . . . , \mu _ { \tilde { f } _ { i } } ( a ^ { - } ) , . . . \mu _ { \tilde { f } _ { m } } ( a ^ { - } ) \right) ^ { I }$

<sup>ð Þ ð</sup>Here, for each $a \in A ,$ , we use the Minkowski distance to calculate the distance between a and $a ^ { + / - }$ . The advertisement that has a shorter distance to $a ^ { + }$ should be ranked higher, whereas the advertisement that has a longer distance to $a ^ { - }$ should be ranked higher. We use $D ( . )$ to represent the mapping between the advertisements and their Minkowski distance. Let

$$
\left\{ \begin{array}{l} D (a ^ {-}) = \max _ {1 \leq j \leq n} \left\{D \Big (a _ {j}, a ^ {-} \Big) \right\} \\ D (a ^ {+}) = \min _ {1 \leq j \leq n} \left\{D \Big (a _ {j}, a ^ {+} \Big) \right\} \end{array} \right..\tag{7}
$$

We can use $\xi ( a _ { j } )$ to denote the relative ratio of membership, where

$$
\xi \left(a _ {j}\right) = D \left(a _ {j}, a ^ {-}\right) / D \left(a ^ {-}\right) - D \left(a _ {j}, a ^ {+}\right) / D \left(a ^ {+}\right).\tag{8}
$$

This represents the degree to which advertisement $a _ { j }$ approaches the ideal positive advertisement $a ^ { + }$ and how far away a is from the most negative advertisement a<sup>−</sup>. By comparing $\xi ( a _ { j } )$ , the initial search results are ranked before being posted to the consumer. The Advertisement Search Manager guarantees that the most personalized advertisements appear in the top positions.

In addition, the user pro<sup>fi</sup>le can be updated after an advertisement $a _ { j }$ is selected by the consumer. The updating procedure can be described as follows.

Input:

Consumer $C _ { k } " s$ pro<sup>fi</sup>le: $P ^ { C _ { k } } = ( p _ { 1 } ^ { C _ { k } } , p _ { 2 } ^ { C _ { k } } , . . . , p _ { i } ^ { C _ { k } } , . . . , p _ { m } ^ { C _ { k } } ) , 1 \leq i \leq m ,$

The attributes of clicked ad $j \colon f ( a _ { j } ) = ( f _ { 1 } ( a _ { j } ) , f _ { 2 } ( a _ { j } ) , . . . , f _ { m } ( a _ { j } ) ) ^ { T } ,$ $1 \leq i \leq m .$

Output:

Updated user pro<sup>fi</sup>le: $\tilde { P } ^ { C _ { k } }$

Updating pro<sup>fi</sup>les:

Let ε be the update parameter, which indicates the sensitivity of the user pro<sup>fi</sup>le update.

Compute $\tilde { P } _ { i } ^ { C _ { k } } = { \bar { p _ { i } ^ { C _ { k } } } } + \varepsilon \Big [ \mu _ { \tilde { f } _ { i } } ( a ) - p _ { i } ^ { C _ { k } } \Big ] \ ( \mathrm { f o r } i = 1 \ \mathrm { t o } \ m ) .$

The updated pro<sup>fi</sup>le: $\tilde { P } _ { i } ^ { \dot { \mathbb { C } } _ { k } ^ { \mu } } = \Big ( p _ { 1 } ^ { C _ { k } } , \dot { p } _ { 2 } ^ { \dot { \mathrm { Q } } _ { k } } , . . . , p _ { i } ^ { C _ { k } } , . . . , p _ { m } ^ { C _ { k } } \Big ) , 1 \le i \le m .$

## 4. Demonstration

This section demonstrates the validity and reliability of the TMAS system from the perspective of both consumers and advertisers. On the consumer side, two functions are provided: (1) consumers can receive targeted advertisements that match their preferences; and (2) consumers' preferences are updated based on their past actions. Similarly, for an advertiser: (1) an advertiser can deliver advertisements to potential customers via the platform, which will create a good impression and a better chance of their advertisements being selected; and (2) an advertiser can improve their advertisements by using feedback from TMAS.

As shown in Fig. 1, TMAS works as a platform for matching mobile users and advertisers. A demon system that runs behind the scene, called the TMAS demon, is developed for demonstration purposes (see Fig. 3). The demon system is developed by C# with a SQL2005 database to simulate the key processes of the Advertisement Search Manager. For illustration, we use a pizza restaurant (as the advertiser) located in a shopping mall that wishes to distribute lunch promotion coupons to customers. There are <sup>fi</sup>ve stages involved.

## 4.1. Shop owner posts advertisements on TMAS

For demonstration, we generated 20 promotional advertisements for pizzas, with four different attributes selected randomly: <sup>fl</sup>avor $\left( f _ { 1 } \right)$ discount (f<sub>2</sub>), price level $( f _ { 3 } )$ , and service level $( f _ { 4 } )$ , as shown in Table 2.

## 4.2. Consumer requests advertisements from TMAS

At this stage, the system receives a query (pizza) from consumers. We generated 100 mobile user pro<sup>fi</sup>les randomly. Table 3 shows 10 examples, in which p1 stands for the preference for <sup>fl</sup>avors, p2 for discount, $p 3$ for price level, and p4 for service level.

## 4.3. TMAS lists targeted advertisements for consumer

After receiving the request, advertisements are sorted by using Eq. (8) and presented to the consumer. To measure the relevance of searched results to the consumer we use three metrics, “Precision” $( P _ { j } )$ , “Average Cumulative Precision” (ACP), and “Precision at position n” (P@n) [18,53]:

$$
P _ {j} = \frac {\xi (a _ {j}) + 1}{2}, P _ {j} \in [ 0, 1 ].\tag{9}
$$

$P _ { j }$ represents the degree to which an advertisement j matches the user's preference. $P _ { j } = 0$ means advertisement j is irrelevant to the user while $P _ { j } = 1$ means advertisement j is perfectly matched to the user's needs. $\xi ( a _ { j } )$ is the relative ratio of af<sup>fi</sup>liation membership which denotes the precision of each advertisement in respect to a given query. The ACP is computed for a single query and is de<sup>fi</sup>ned as the average of the P values for all searched results:

$$
A C P = \frac {\sum_ {i = 1} ^ {N} P _ {i}}{N}.\tag{10}
$$

Precision at n (P@n) measures the relevance of the top n results with respect to a given query, obtained by:

$$
P @ n = \frac {\sum_ {i = 1} ^ {n} P _ {i}}{n}.\tag{11}
$$

![](/api/attachments/C5T8MDTR/fulltext/images/139e6251faad9265a2632a7a4f269a4a9013b002a0312f614fecaf41c6716bc7.jpg)  
Fig. 3. The TMAS Demon interface.

Table 2  
Twenty randomly generated advertisements and their attributes.

<table><tr><td>Ad ID</td><td> $f_1$ </td><td> $f_2$ </td><td> $f_3$ </td><td> $f_4$ </td><td>Ad ID</td><td> $f_1$ </td><td> $f_2$ </td><td> $f_3$ </td><td> $f_4$ </td></tr><tr><td>AD01</td><td>19.57</td><td>0.96</td><td>4.00</td><td>4.00</td><td>AD 11</td><td>40.79</td><td>0.57</td><td>3.00</td><td>2.00</td></tr><tr><td>AD 02</td><td>15.96</td><td>0.95</td><td>4.00</td><td>4.00</td><td>AD 12</td><td>16.99</td><td>0.52</td><td>3.00</td><td>1.00</td></tr><tr><td>AD 03</td><td>18.41</td><td>0.82</td><td>1.00</td><td>5.00</td><td>AD 13</td><td>32.09</td><td>0.51</td><td>1.00</td><td>3.00</td></tr><tr><td>AD 04</td><td>47.52</td><td>0.74</td><td>3.00</td><td>4.00</td><td>AD 14</td><td>5.38</td><td>0.74</td><td>5.00</td><td>1.00</td></tr><tr><td>AD 05</td><td>22.07</td><td>0.83</td><td>4.00</td><td>4.00</td><td>AD 15</td><td>30.02</td><td>0.92</td><td>5.00</td><td>3.00</td></tr><tr><td>AD 06</td><td>23.12</td><td>0.79</td><td>4.00</td><td>2.00</td><td>AD 16</td><td>48.53</td><td>0.82</td><td>2.00</td><td>3.00</td></tr><tr><td>AD 07</td><td>32.29</td><td>0.59</td><td>2.00</td><td>3.00</td><td>AD 17</td><td>5.89</td><td>0.62</td><td>3.00</td><td>3.00</td></tr><tr><td>AD 08</td><td>45.37</td><td>0.97</td><td>5.00</td><td>3.00</td><td>AD 18</td><td>44.95</td><td>0.96</td><td>3.00</td><td>5.00</td></tr><tr><td>AD 09</td><td>37.10</td><td>0.61</td><td>4.00</td><td>1.00</td><td>AD 19</td><td>49.83</td><td>0.69</td><td>5.00</td><td>1.00</td></tr><tr><td>AD 10</td><td>37.77</td><td>0.71</td><td>4.00</td><td>4.00</td><td>AD 20</td><td>16.64</td><td>0.98</td><td>3.00</td><td>5.00</td></tr></table>

ACP and P@n are similar to each other, but they are two different indexes. ACP and P@n have previously been used together in the literature to measure the precision of ranking algorithms. ACP measures the total precision of the ranking list (N represents the number of results that are involved in the ranking). After all the results are ranked by P and posted to consumers as a list, P@n represents the precision level of the top n results on the list (nbN). This index tells us the deviation of precision among different positions in the ranking list. If we can only display n results to consumers, P@n is a good index to show the precision level. In mobile advertising, the size of smart phone screens is limited and we can only list a few result on one page. Also, users are inherently more likely to click on higher-ranked items and do not like page turning [16].

The results obtained for 10 consumers are listed in Table 4. $P _ { m a x } = M a x ( P _ { i } )$ . It is the highest precision among all matched adver-$\mathrm { t i s e m e n t s . } A D _ { 1 4 }$ means the forth advertisement presented to User01. P@5 indicates the precision of the match between the users with the <sup>fi</sup>rst <sup>fi</sup>ve advertisements (e.g. $A D _ { 1 4 } , A D _ { 1 0 } , A D _ { 1 3 } , A D _ { 1 1 } ,$ and $A D _ { 1 9 }$ for User01). As shown in the table, the maximum precision values of all consumers are between 0.736 and 0.895, and the P@5 values are between 0.674 and 0.812. These numbers suggest that every advertisement in the top position is relevant and personalized to the consumer.

Fig. 4 presents the average P@n values for the top n (n=1 to 10 here) to 100 consumers. The average P@n value ranges between 0.82 and 0.65. Since the P@n value represents the relevance of all of the top n advertisements in the searched results, the high P@n value of the top 10 positions demonstrates that the intelligent searching process can help consumers to <sup>fi</sup>nd highly relevant advertisements.

Fig. 5 shows the ACP value over 100 consumers. In the experiment, every consumer has a relatively high value of ACP, ranging from 0.64 to 0.87. This means that every consumer receives precise advertisements as a result of the platform's intelligent search method. The above three indexes (P, P@n, and ACP) show that advertisements posted by the platform are highly relevant to consumers with different preferences.

However, as TMAS is a platform, matching the demand from both sides means that it should not only ensure that consumers can locate highly relevant advertisements, it also needs to make sure that each advertisement has a relatively equal opportunity of being viewed by potential consumers. To provide good advertising services, both revenue and uniformity (the fairness of service to a wide range of advertisers' advertisements) are important in ranking mechanism [10,27]. An advertisement-ranking mechanism does not need to guarantee equal opportunity of exposure, although it should at least make sure the Matthew effect is not too strong among advertisers. An advertisement-ranking mechanism does not need to guarantee equal opportunity of exposure, although it should at least make sure that the Matthew effect is not too strong among advertisers. ‘The Matthew effect’ refers to the sociological phenomenon of ‘the rich get[ting] richer and the poor get[ting] poorer’ [30]. If this effect is too strong, then the platform will lose many small advertisers, and new advertisers will not choose it. Thus, we use “number of times that an advertisement is ranked in top 10 (N)” and “expected clickthrough (EC)” to measure the chance that an advertisement will be retrieved from the platform. To compute the expected number of click-through for an advertisement j at position $k ,$ an exponentially decaying attention model with factor δ>1 is employed in our experiment. As suggested by Breese, Heckerman and Kadie [7], the average click-through can be computed as $p / \delta ^ { k - 1 }$ . Exponential decay of attention is a standard assumption, adopted by Feng et al. [16], using actual click-through data from Overture in 2003, with the top af<sup>fi</sup>liated websites (such as Yahoo, MSN, and AltaVista), where $\delta = 1 . 4 2 8 ( \mathrm { R } ^ { 2 } = 0 . 9 9 7 )$

Table 3  
Ten user preference examples

<table><tr><td>Ad ID</td><td> $p_1$ </td><td> $p_2$ </td><td> $p_3$ </td><td> $p_4$ </td></tr><tr><td>User 01</td><td>0.455</td><td>0.251</td><td>0.250</td><td>0.042</td></tr><tr><td>User 02</td><td>0.214</td><td>0.438</td><td>0.230</td><td>0.116</td></tr><tr><td>User 03</td><td>0.345</td><td>0.339</td><td>0.311</td><td>0.003</td></tr><tr><td>User 04</td><td>0.098</td><td>0.568</td><td>0.172</td><td>0.160</td></tr><tr><td>User 05</td><td>0.080</td><td>0.457</td><td>0.082</td><td>0.379</td></tr><tr><td>User 06</td><td>0.284</td><td>0.263</td><td>0.182</td><td>0.270</td></tr><tr><td>User 07</td><td>0.066</td><td>0.639</td><td>0.144</td><td>0.150</td></tr><tr><td>User 08</td><td>0.261</td><td>0.221</td><td>0.243</td><td>0.273</td></tr><tr><td>User 09</td><td>0.334</td><td>0.451</td><td>0.151</td><td>0.062</td></tr><tr><td>User 10</td><td>0.292</td><td>0.165</td><td>0.129</td><td>0.412</td></tr></table>

Table 4  
Results for 10 consumers.

<table><tr><td>User ID</td><td> $P_{\text{max}}$ </td><td>P@5</td><td>Ranking (top 5)</td></tr><tr><td>User 01</td><td>0.895</td><td>0.739</td><td> $AD_{14} \succ AD_{10} \succ AD_{13} \succ AD_{11} \succ AD_{19}$ </td></tr><tr><td>User 02</td><td>0.829</td><td>0.689</td><td> $AD_{12} \succ AD_{19} \succ AD_{11} \succ AD_{13} \succ AD_{6}$ </td></tr><tr><td>User 03</td><td>0.891</td><td>0.812</td><td> $AD_{14} \succ AD_{19} \succ AD_{12} \succ AD_{17} \succ AD_{15}$ </td></tr><tr><td>User 04</td><td>0.905</td><td>0.758</td><td> $AD_{19} \succ AD_{14} \succ AD_{17} \succ AD_{9} \succ AD_{5}$ </td></tr><tr><td>User 05</td><td>0.798</td><td>0.690</td><td> $AD_{13} \succ AD_{10} \succ AD_{17} \succ AD_{3} \succ AD_{7}$ </td></tr><tr><td>User 06</td><td>0.736</td><td>0.674</td><td> $AD_{18} \succ AD_{3} \succ AD_{4} \succ AD_{2} \succ AD_{12}$ </td></tr><tr><td>User 07</td><td>0.832</td><td>0.785</td><td> $AD_{13} \succ AD_{11} \succ AD_{12} \succ AD_{7} \succ AD_{17}$ </td></tr><tr><td>User 08</td><td>0.753</td><td>0.722</td><td> $AD_{4} \succ AD_{5} \succ AD_{17} \succ AD_{15} \succ AD_{10}$ </td></tr><tr><td>User 09</td><td>0.794</td><td>0.682</td><td> $AD_{17} \succ AD_{12} \succ AD_{11} \succ AD_{9} \succ AD_{7}$ </td></tr><tr><td>User 10</td><td>0.838</td><td>0.763</td><td> $AD_{18} \succ AD_{4} \succ AD_{10} \succ AD_{1} \succ AD_{3}$ </td></tr></table>

Fig. 6 shows the number of times that each advertisement is ranked in the top 10 and the expected click-through in the experiment over 100 consumers. We can see that the variation in the EC value is quite similar to the N value. When an advertisement has a higher chance of being ranked on top, it should get more clicks from consumers. Moreover, the variance and variance/mean ratio (VMR) of the N value are 192.74 and 4.28, while the variance and VMR of the EC value are 44.99 and 3.65. These results show that the degree of dispersion in N and EC is relatively small.

## 4.4. TMAS updates consumer preferences

In this stage, we update user pro<sup>fi</sup>les based on consumers' selection preferences and feedback. We assume that each consumer only clicks on one advertisement from the searched results. The 100 user pro<sup>fi</sup>les generated above are then updated following the procedure outlined in the previous section. For example, the input of consumer $C _ { 1 } " s$ pro<sup>fi</sup>le is U<sup>C1</sup>=(0.455, 0.251, 0.250, 0.042) and the attributes of clicked AD14 are $f ( a _ { 1 4 } ) = ( 5 . 3 8 , 0 . 7 4 , 5 , 1 )$ . The updated user pro<sup>fi</sup>le is $\tilde { u } ^ { C _ { 1 } }$ and the system updates the pro<sup>fi</sup>le, where ε= 0.1 is the update parameter that indicates the sensitivity of the user pro<sup>fi</sup>le update. We compute $\tilde { u } _ { 1 } ^ { C _ { 1 } } = u _ { i } ^ { C _ { 1 } } + 0 . 1 * [ \mu _ { \tilde { A } _ { 1 } } f _ { i } ( a _ { 1 4 } ) - u _ { i } ^ { C _ { 1 } } ] \ ( \mathrm { f o r } i = 1 \ \mathrm { t o } m )$ , and the updated pro-<sup>fi</sup>le becomes $\tilde { u } ^ { C _ { 1 } } = ( 0 . 4 5 6 , 0 . 2 5 0 , 0 . 2 3 0 , 0 . 0 6 1 )$ . A sample of 10 user preferences and updated user preferences is shown in Table 5.

![](/api/attachments/C5T8MDTR/fulltext/images/a54ed342d28a019fbf3b9f6c772a798854aabafad99739f3e6811a315b40e12e.jpg)  
Fig. 4. The average P@n of top n ranks.

![](/api/attachments/C5T8MDTR/fulltext/images/1f2395cf509b7b5178aebb4f6980140864fb1d61fe9f245f6535295c86b8ea2e.jpg)  
Fig. 5. The average cumulative precision of each user over 100 consumers.

![](/api/attachments/C5T8MDTR/fulltext/images/dc1f6012b9584789ded7c3b9fd37f85b3fa6485f893683bd1fdb6e935ba3e98e.jpg)  
Fig. 6. The N and EC values of all advertisements in the experiment.

4.5. TMAS feedback is provided to the pizza shop owner to improve the effectiveness of advertisements

$$
\bar {P} = (\bar {p} _ {1}, \bar {p} _ {2}, \dots , \bar {p} _ {i}, \dots , \bar {p} _ {m})
$$

$$
f _ {i} ^ {\prime} (a _ {j}) = \frac {n \bar {p} _ {i} f _ {i} (a _ {j})}{\sum_ {i = 1} ^ {m} \bar {p} _ {i}}
$$

<sup>i¼1</sup>the advertisement's attributes to simulate the improvement in advertisers' advertising strategies, such as discount and price. For example, if most of the consumers who clicked on an advertisement were interested in discounts, the advertiser could choose to offer more discounts in their advertisements.

We use the 100 updated user pro<sup>fi</sup>les to repeat the simulation for the same consumers (stage 1). The advertisements are also improved based on the feedback (stage 2). Fig. 7 shows the ACP values of each consumer at each of the two stages. Most consumers' ACP value for stage 2 is higher than for stage 1. The average ACP of all consumers in stage 2 is 0.775 with an increase of 4.7% over stage 1. Thus, by updating consumers' user pro<sup>fi</sup>les based on their past click-through behavior, the platform can provide more precisely targeted advertisements.

Ten updated user preferences.

<table><tr><td>User ID</td><td>P</td><td> $\tilde{P}$ </td></tr><tr><td>User 01</td><td>0.455, 0.251, 0.250, 0.042</td><td>0.456, 0.250, 0.230, 0.061</td></tr><tr><td>User 02</td><td>0.214, 0.438, 0.230, 0.116</td><td>0.222, 0.431, 0.226, 0.119</td></tr><tr><td>User 03</td><td>0.345, 0.339, 0.311, 0.003</td><td>0.338, 0.323, 0.320, 0.017</td></tr><tr><td>User 04</td><td>0.098, 0.568, 0.172, 0.160</td><td>0.087, 0.578, 0.184, 0.149</td></tr><tr><td>User 05</td><td>0.080, 0.457, 0.082, 0.379</td><td>0.074, 0.454, 0.092, 0.377</td></tr><tr><td>User 06</td><td>0.284, 0.263, 0.182, 0.270</td><td>0.294, 0.268, 0.176, 0.261</td></tr><tr><td>User 07</td><td>0.066, 0.639, 0.144, 0.150</td><td>0.074, 0.619, 0.155, 0.151</td></tr><tr><td>User 08</td><td>0.261, 0.221, 0.243, 0.273</td><td>0.274, 0.235, 0.232, 0.256</td></tr><tr><td>User 09</td><td>0.334, 0.451, 0.151, 0.062</td><td>0.318, 0.466, 0.143, 0.070</td></tr><tr><td>User 10</td><td>0.292, 0.165, 0.129, 0.412</td><td>0.304, 0.149, 0.139, 0.406</td></tr></table>

![](/api/attachments/C5T8MDTR/fulltext/images/1a115688f6c7be1e2727fd1b53d972c2f5eb6f236a64eb5386a9e90e5c9c3494.jpg)  
Fig. 7. The ACP value of all consumers for the two stages.

Fig. 8 shows the EC values for each advertisement over the two stages. Advertisers are looking for a higher number of clicks. The EC value of all 20 advertisements increases by an average of 4.3% in stage 2. The number of expected clicks increases after advertisements are improved based on their effectiveness and feedback information from the platform. Thus, by acquiring valuable information from the platform to improve their advertising strategies, advertisements can be made more effective.

## 5. Conclusions

Location-based services provide unique, ubiquitous, and timely services to customers. With the maturing of smart phone technology, it becomes feasible to deliver location-based advertising services to targeted customers. Thus, providing a service platform for mobile devices can link advertisers and consumers in an effective and economical way. The platform should be effective, timely, and simple to operate so that an advertiser can manage the promotion effortlessly. In this study, we proposed a targeted mobile advertising platform (TMAS) for matching the demands of both consumers and merchants. The platform provides consumers with relevant advertisements and merchants with an effective channel for accessing customers. Speci<sup>fi</sup>cally, the TMAS allows consumers to locate advertisements actively via their mobile phones with reference to their own demographic, contextual, and preference data. For merchants, promotions can be improved through better understanding of customers' needs using feedback from the platform, so that they can design effective targeted advertisements. The demonstration shows that mobile users will receive advertisements that match their preferences and merchants will make a better impression with their advertisements.

However, improving the ef<sup>fi</sup>ciency of delivering promotions also increases the possibility of invading privacy, as do most new technologies. There is always a trade-off between embracing new technologies and protection of privacy because to deliver more personalized promotions requires more detailed individual information on consumers. Future research can look at how to <sup>fi</sup>nd a balance between providing highly effective personalized mobile advertisements and satisfactory protection of privacy.

![](/api/attachments/C5T8MDTR/fulltext/images/79d153e306fdb3e46aa3da133650ec33729e4f4228bf5479af3244f8fe48bffb.jpg)  
Fig. 8. The EC value of all advertisements for the two stages.

## Acknowledgment

This study was partially supported by Humanity and Social Science Youth Foundation of Ministry of Education of China (11YJC630099).

## References

[1] S.A. Adam, Model of web use in direct and online marketing strategy, Electronic Markets 12 (4) (2002) 262–269

[2] G.D. Abowd, E.D. Mynatt, Charting past, present, and future research in ubiquitous computing, ACM Transactions on Computer–Human Interaction 7 (1) (2000) 29–58

[3] A.V. Aho, M.J. Corasick, Ef<sup>fi</sup>cient string matching: an aid to bibliographic search, Communications of the ACM 18 (6) (June 1975) 333–340.

[4] G. Amato, U. Straccia, User pro<sup>fi</sup>le modeling and applications to digital libraries, ECDL '99, Lecture Notes in Computer Science 1696 (1999) 184–197.

[5] S. Balasubramanian, R.A. Peterson, S.L. Jarvenpaa, Exploring the implications of M-commerce for markets and marketing, Journal of the Academy of Marketing Science 30 (4) (2002) 348–361.

[6] P. Barwise, C. Strong, Permission-based mobile advertising, Journal of Interactive Marketing 16 (1) (2002) 14–24.

[7] J.S. Breese, D. Heckerman, C. Kadie, Empirical analysis of predictive algorithms for collaborative <sup>fi</sup>ltering, in: S.M. Gregory, F. Cooper (Eds.), Proceedings of the Fourteenth Conference on Uncertainty in Arti<sup>fi</sup>cial Intelligence, University of Wiscon sin Business School, Madison, Wisconsin, 1998, pp. 43–52.

[8] Businessweek, Mobile ad biz comes of age, May 14, 2007, Available at: http:// www.businessweek.com.

[9] Carat Interactive, The future of wireless marketing, White Paper, Boston, MA, available at: http://www.bjoconsulting.com/download/Wireless\_WhitePaper.pdf, 2002.

[10] D. Chickering, D. Heckerman, Targeted advertising on the web with inventory management, INFORMS Journal of Interfaces 33 (5) (2003) 71–77.

[11] D.Y. Choi, Personalized local Internet in the location-based mobile web search, Decision Support Systems 43 (1) (2007) 31–45.

[12] M. Dastani, N. Jacobs, C.M. Jonkerc, J. Treur, Modeling user preferences and mediating agents in electronic commerce, Knowledge-Based Systems 18 (2005) 335–352.

[13] T. De Pessemier, T. Deryckere, K. Vanhecke, L. Martens, Proposed architecture and algorithm for personalized advertising on iDTV and mobile devices, IEEE Transactions on Consumer Electronics 54 (2) (May 2008) 709–713.

[14] B. De Reyck, Z. Degraeve, Broadcast scheduling for mobile advertising, Operations Research 51 (4) (Jul/Aug 2003) 509–517.

[15] B. De Reyck, Z. Degraeve, MABS: spreadvertisementsheet-based decision support for precision marketing, European Journal of Operational Research 171 (3) (June 2006) 935–950.

[16] J. Feng, K. Hemant, D.M. Bhargava, D. Pennock, Implementing sponsored search in web search engines: computational evaluation of alternative mechanisms, INFORMS Journal on Computing 19 (1) (2007) 137–148.

[17] P. Germanakos, N. Tsianos, Z. Lekkas, C. Mourlas, G. Samaras, Improving m-commerce services effectiveness with the use of user-centric content delivery, Journal of Electronic Commerce in Organizations 6 (1) (2008) 1–19.

[18] K. Jarvelin, J. Kekalainen, IR evaluation methods for retrieving highly relevant documents, Proceedings of the ACM Conference on Research and Development on Information Retrieval (SIGIR), 2000.

[19] J.J. Jung, Contextualized mobile recommendation service based on interactive social network discovered from mobile users, Expert Systems with Applications 36 (2009) 11950–11956.

[20] A. Katz-Stone, Wireless revenue: advertisements can work, Australia. internet.com, Available from: http://www.wirelessauthority.com.au/r/article/jsp/sid/445080, 2001.

[21] P. Kazienko, M. Adamski, AdROSA — adaptive personalization of web advertising, Information Sciences 177 (11) (June 2007) 2269–2295.

[22] J.W. Kim, B.H. Lee, M.J. Shaw, H. Chang, M. Nelson, Application of decision-tree induction techniques to personalized advertisements on Internet storefronts, International Journal of Electronic Commerce 5 (3) (2001) 45–62.

[23] H. Kwak, R.J. Fox, G.M. Zinkhan, What products can be successfully promoted and sold via the Internet? Journal of Advertising Research (Jan/Feb 2002) 23–38.

[24] O. Kwon, J. Kim, Concept lattices for visualizing and generating user pro<sup>fi</sup>les for context-aware service recommendations, Expert Systems with Applications 36 (2009) 1893–1902.

[25] M. Langheinrich, A. Nakamura, N. Abe, T. Kamba, Y. Koseki, Unintrusive customization techniques for web advertising, Computer Networks 31 (11–16) (1999) 1259–1272.

[26] M. Leppaniemi, H. Karjaluoto, Factors in<sup>fl</sup>uencing consumers' willingness to accept mobile advertising: a conceptual model, International Journal of Mobile Communications 3 (3) (2005) 197–213.

[27] K. Li, E.C. Idemudia, Z. Lin, Y. Yu, A framework for intermediated online targeted advertising with banner ranking mechanism, Information Systems and E-Business Management, doi:10.1007/s10257-010-0134-4, 26 June 2010.

[28] Y. Li, B. Steinberg, Sales call: more advertisements hit cell phone screens, Wall Street Journal, Eastern Edition 247 (27) (2006) B3.

[29] Q.H. Mahmoud, L. Yu, Havana agents for comparison shopping and location-aware advertising in wireless mobile environments, Electronic Com merce Research and Applications 5 (3) (2006) 220–228.

[30] R.K. Merton, The Matthew effect in science, Science 159 (3810) (1968) 56–63.

[31] S. Okazaki, How do Japanese consumers perceive wireless advertisements? A multivariate analysis, International Journal of Advertising 23 (4) (2004) 429–454.

[32] S. Okazaki, C.R. Taylor, What is SMS advertising and why do multinationals adopt it? Answers from an empirical study in European markets, Journal of Business Research 61 (1) (January 2008) 4–12.

[33] C. Peters, C.H. Amato, C.R. Hollenbeck, An exploratory investigation of consumers' perceptions of wireless advertising, Journal of Advertising 36 (4) (Winter 2007) 129–146.

[34] J.T.S. Quah, G.L. Lim, Push selling–multicast messages to wireless devices based on the publish/subscribe model, Electronic Commerce Research and Applications 1 (3–4) (2002) 235–246.

[35] A. Scharl, J. Dickinger, Murphy, Diffusion and success factors of mobile marketing, Electronic Commerce Research and Applications 4 (2) (Summer 2005) 159–173

[36] A.E. Schlosser, S. Shavitt, A. Kanfer, Survey of internet users' attitudes toward internet advertising, Journal Of Interactive Marketing 13 (3) (1999) 34–54.

[37] F.A. Schreiber, F. Barbic, S. Madeddu, Dynamic user pro<sup>fi</sup>les and <sup>fl</sup>exible queries in of-<sup>fi</sup>ce document retrieval systems, Decision Support Systems 5 (1) (March 1989) 13–28.

[38] E. Snekkenes, Concepts for personal location privacy policies, Proceedings of the 3rd ACM Conference on Electronic Commerce, Tampa, Florida, USA, 2001, pp. 48–57.

[39] L. Spiller, M. Baier, Contemporary Direct Marketing, Prentice-Hall, Upper Saddle River, NJ, 2005.

[40] F. Sultan, A.J. Rohm, How to market to generation m(obile), MIT Sloan Management Review 49 (4) (Summer 2008) 35–45.

[41] P. Tarasewich, Designing mobile commerce applications, Communications of the ACM 46 (12) (2003) 57–60.

[42] A.K. Tripathi, S.K. Nair, Narrowcasting of wireless advertising in malls, European Journal of Operational Research 182 (3) (November 2007) 1023–1038.

[43] A.K. Tripathi, S.K. Nair, Mobile advertising in capacitated wireless networks, IEEE Transactions on Knowledge & Data Engineering 18 (9) (September 2006) 1284–1296

[45] E. Turban, D. King, J. Lang, Introduction to Electronic Commerce, Second edition Prentice Hall, 2009.

[46] U. Varshney, Location management for mobile commerce applications in wireless internet environment, ACM Transactions on Internet Technology 3 (3) (2003) 236–255.

[47] V. Venkatesh, V. Ramesh, A.P. Massey, Understanding usability in mobile commerce, Communications of the ACM 46 (12) (2003) 53–56.

[48] Z. Xu, Q. Da, A least deviation method to obtain a priority vector of a fuzzy preference relation, European Journal of Operational Research 164 (1) (2005) 206–216.

[49] D.J. Xu, S.S. Liao, Q. Li, Combining empirical experimentation and modeling techniques: a design research approach for personalized mobile advertising applica tions, Decision Support Systems 44 (2008) 710–724.

[50] R.R. Yager, Targeted E-commerce marketing using fuzzy intelligent agents, IEEE Intelligent Systems 15 (6) (2000) 42–45.

[51] Y. Yang, Web user behavioral pro<sup>fi</sup>ling for user identi<sup>fi</sup>cation, Decision Support Systems 49 (3) (2010) 261–271.

[52] S. Yuan, Y.W. Tsao, A recommendation mechanism for contextualized mobile advertising, Expert Systems with Applications 24 (4) (May 2003) 399–414.

[53] A.M. Zareh Bidoki, P. Ghodsnia, N. Yazdani, F. Oroumchian, A3CRank: an adaptive ranking method based on connectivity, content and click-through data, Information Processing and Management 46 (2) (2010) 159–169.

![](/api/attachments/C5T8MDTR/fulltext/images/144f7d0da81454fc726dad3e9b7a0dd0c8008b02600f7a37b850f93abf3c6038.jpg)  
Kai Li received his BS degree in Information Systems and Information Management from Nankai University, China. He obtained his MS and PhD degrees in Management Science and Engineering also from Nankai University, China. Dr. Li is currently a lecturer at Nankai University. His research interests include electronic commerce, mobile commerce, and business intelligence.

![](/api/attachments/C5T8MDTR/fulltext/images/c6c79c43f130c2c671c48088bbb87299014d5ecd77c9ed590c89bf33862e3154.jpg)

Timon C. Du received his BS degree in Mechanical Engineering from the National Chung-Hsing University, Taiwan. He obtained his MS and PhD degrees in Industrial Engineering from the Arizona State University, USA. Dr. Du is a Professor at the Chinese University of Hong Kong. His research interests include e-business, data mining, collaborative commerce, and the semantic web. He has published papers in many leading international journals, including Decision Support Systems, IEEE Transactions on Knowledge and Data Engineering, Communications of the ACM, IIE Transactions, and Information and Management.
