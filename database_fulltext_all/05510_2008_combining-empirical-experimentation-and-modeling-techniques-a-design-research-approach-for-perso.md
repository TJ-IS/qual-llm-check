---
otero_id: 5510
otero_key: "Z9FNACMU"
title: "Combining empirical experimentation and modeling techniques: A design research approach for personalized mobile advertising applications"
authors: "David Jingjun Xu; Stephen Shaoyi Liao; Qiudan Li"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.10.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Combining empirical experimentation and modeling techniques: A design research approach for personalized mobile advertising applications

David Jingjun Xu <sup>a,⁎</sup>, Stephen Shaoyi Liao <sup>b,c</sup>, Qiudan Li <sup>d</sup>

Sauder School of Business, University of British Columbia, Canada

<sup>b</sup> Department of Information Systems, City University of Hong Kong, Hong Kong

<sup>c</sup> School of Economics and Management, South West JiaoTong University, PR China

<sup>d</sup> Laboratory of Complex Systems and Intelligence Science, Institute of Automation, Chinese Academy of Sciences, PR China

Received 31 July 2007; accepted 7 October 2007 Available online 13 October 2007

## Abstract

We propose a design research approach combining behaviour and engineering techniques to better support user modeling in personalized mobile advertising applications. User modeling is a practical means of enabling personalization; one important method to construct user models is that of Bayesian networks. To identify the Bayesian network structure variables and the prior probabilities, empirical experimentation is adopted and context, content, and user preferences are the salient variables. User data collected from the survey are used to set the prior probabilities for the Bayesian network. Experimental evaluation of the system shows it is effective in improving user attitude toward mobile advertising © 2007 Elsevier B.V. All rights reserved.

Keywords: Mobile commerce; Bayesian networks; User modeling; Mobile advertising; Personalization

## 1. Introduction

With the development of wireless and mobile networks, mobile commerce (m-commerce) is creating significant benefits and new business opportunities for both mobile devices and services. According to Research and Markets [63], the number of mobile users worldwide is expected to climb to 2 billion by 2007, and the annual handset sales are predicted to generate more than U.S. \$3 billion by 2009. The high penetration rate of mobile phones has resulted in the increasing use of handheld devices to deliver advertisements of products and services. Mobile advertising revenues, as indicated by many research firms, make up the largest share of m-commerce revenues. One may expect mobile advertising to be even more appealing to consumers who use location-sensitive and time-critical m-commerce applications.

However, constraints in using both mobile networks and devices impose significant negative influences on the operational performance of m-commerce applications. For example, the small screens of the devices allow the user to view only limited pages of information [39]. Many other inherent constraints exist in a mobile computing environment (e.g., minimal battery power on wireless devices [71], limited and error-prone wireless links [5,47], limited input and output capacity [51], the diversity of devices, and the myriad differences in user profiles), which should be taken into consideration in the design and development phases of m-commerce services and applications [4]. The success of m-commerce largely depends on whether personalization can be well utilized to deliver highly personalized and context-sensitive (timeand location-dependent) information to mobile users. Providing personalized information to mobile users will create better customer satisfaction and will in turn increase the demand for mobile services.

The practice of randomly sending promotion messages to all available users results in user dissatisfaction and a high advertising cost for the merchants. In an effort to tackle this problem, we have developed a Bayesian-network-based mobile application prototype, which is designed to provide personalized dining advertisements to mobile users. In order to support this objective, we propose a design research approach that combines empirical experimentation and modeling techniques to help construct the user models with more realistic data support. The Bayesian network is an efficient tool for building user models of domains with inherent uncertainty [41,59], and is therefore adopted as the key modeling technique for the construction of the user model.

The reasons for choosing empirical experimentation to support the construction of the Bayesian-based user model are threefold: First, this technique verifies whether personalization is indeed an important factor that contributes to consumers' perceptions of mobile advertising. The collected data are analyzed using the Partial Least Squares (PLS). Second, this method enables the determination of what variables should be considered to strengthen the personalization capability so that merchants can focus on these variables in order to more effectively deliver personalized mobile advertisements. Third, the empirical experiment provides the data for setting prior probabilities in the Bayesian-networkbased user models. After identifying the network structure variables and the prior probabilities, a Bayesian-network-based user model can be built accordingly.

To demonstrate the use of the proposed design research approach, we have constructed a prototype that is a personalized mobile advertising application consisting of two major parts: a model component and a mobile Internet connectivity system. The component is Bayesian network based and contains a user model that describes the user's profiles and preferences, a context model that describes contextual information, and a matching engine that integrates information from the two models and the content information to predict the most likely interested customers or matched restaurants. The mobile Internet connectivity system implements the model component to provide relevant advertising information to the right customers or matched restaurants.

This paper is organized as follows: Section 2 reviews the literature on mobile advertising, consumer behaviour, personalization, Bayesian networks, and user modeling. Section 3 focuses on a research framework of the factors affecting user attitude toward mobile advertising, and the particular dimensions of personalization. Section 4 describes the methods used to collect the data in order to verify the research frameworks. Section 5 describes the elements and structure of the Bayesian-network-based model component. Section 6 presents the mobile Internet system that implements the model component to deliver the right mobile advertising to the right users at the right time and place, and helps users to find matched restaurants. Section 7 evaluates the application, and the final section highlights the contributions of this research and concludes the paper.

## 2. Literature review

## 2.1. Mobile advertising

Short message services (SMS) have become a new technological buzzword in transmitting business-tocustomer messages to such wireless devices as cellular telephones, pagers, and personal data assistants. Many brands and media companies include text message numbers in their advertisements to enable interested consumers to obtain more information [60]. Mobile marketing uses interactive wireless media to deliver personalized time- and location-sensitive information promoting goods, services, and ideas, “thereby generating value for all stakeholders” [26]. Mobile advertising is predicted to be an important source of revenue for mobile operators in the future [25] and has been identified as one of the most promising potential business areas [46]. Compared to traditional and Internet-based advertising, mobile advertising has distinctive features such as personalization [1,43,52,68] that can greatly enhance advertising effectiveness. For instance, in comparison with much advertising in traditional media, mobile advertisements can be customized to better suit a consumer's needs and improve client relationship [32]. Examples of mobile advertising methods include mobile banners, alerts, and proximity-triggered advertisements [34].

A mobile advertising study with 1000 mobile phone users, initiated by Barwise and Strong [9], showed mobile advertising generated high levels of readership and advertising awareness, stronger brand attitudes, direct behavioural responses, and some unintended positive effects. In addition, 81% of those in the trial did not delete any of the text messages before reading them. Enpocket [30], the Intelligent Mobile Marketing Company, conducted an advertising study with more than 1200 mobile Internet users across the United States, Europe, and India, which revealed that consumers were far more accepting of mobile advertising when it was made relevant. The research showed that targeted mobile advertising was 50% more acceptable to mobile Internet users than were untargeted advertising. Moreover, 78% said they would be happy to receive mobile advertising that was tailored to their interests. Of those, 64% would be willing to provide personal details for analysis to improve relevance of targeted advertisings. These results indicated that many people were already familiar with mobile advertisements.

According to a study reported by eMarketer [28] in early 2003, approximately 40% of mobile phone subscribers in Asia had received mobile advertisements from marketers, 36% in Europe, and only 8% in the United States. SMS were not yet as popular in the United States as in Europe and Asia [9,29]. While some countries were still debating the merits of cellular telephone advertisements, they were much more accepted in China [12]. China had about 350 million mobile phone subscriptions, and an estimated 304 billion Short Message Service (SMS) messages were sent a year [57]. Within the month of June 2006, 1.5 billion SMS and 780 million Multimedia Message Service (MMS) advertisements were distributed via Korea Telecom Freetel, the second largest wireless service provider in that country [50]. The response rate in mobile advertising was usually higher than in other forms of direct response advertising, including direct mail and banner advertisings. If properly used, mobile advertising could be an effective way to interact with consumers [53]. An earlier pilot study conducted by Quios found that in mobile advertising the level of recognition was surprisingly high: 79% of participants recalled 60% of mobile advertising [8].

Mobile advertising provides a good platform for personalization since mobile devices usually carry the user's assigned identity [49]. If marketers employ mobile devices for their advertising activities, they can use consumer feedback to customize their messages and collect information about consumers' preferences to improve future offerings of products and services [3,69,70]. This provides an exceptional advantage to marketers because it enables them to reach their potential customers in an individual way and thus improves their relationship with customers.

## 2.2. Consumer behaviour and dimensions of personalization

Marketing researchers have been trying for decades to understand consumer behaviour [27] and have summarized their findings in a model. Turban et al. modified this model for the e-commerce environment [74], stating that the buyer's decision is influenced by several factors including the buyer's individual characteristics, the environment, and the merchant's marketing strategy components such as price and promotion. We believe that the consumer's profile, choice of merchants, and context will also influence the way the consumer reacts to mobile advertising.

The management of user profiles forms the core of personalization technology [31,52]. According to Zhang [83], this individualized profile includes user ID, background information, interest and preferences, and target device information. In a scenario described by Varshney and Vetter [78], a mobile advertising and shopping application might include databases containing demographics, location information, user preference, and store sales and specials. Thus, mobile advertising can be carried out in a precise way with a clear focus on the target group. Advertisements sent to a user can also be location-sensitive and can inform a user about various ongoing specials at establishments in the surrounding areas (e.g., shops, malls, and restaurants). Rao and Minakakis [62] argued for the necessity of marketing techniques based on knowledge of customer profiles, history, and needs. Beyond personalization based on consumers' feedback, the ability to locate consumers allows the specific situation of a user to be considered. Consequently, advertising activities can be adapted to take into account location, time, and timerelated items such as local events.

The users' demographic variables that affect their attitudes toward advertising (including gender, age, income, and education level [65,71]) are shown in a model developed by Brackett and Carr [10]. In mcommerce, context awareness is one of the key enabling factors for providing personalized services [54,71]. Context information covers aspects such as location [52,76,79], time [52,79], user activities [24,66], and weather [17]. The utilization of time- and locationawareness as personalization variables is beneficial in that mobile advertising as a marketing medium has features that other marketing channels lack [42].

To summarize, the components of personalization in the m-commerce environment include individual demographic information, user preference, merchant's information, and environment contexts. In our personalized mobile advertising application, sending advertising messages to mobile devices is based on customers user demographics (e.g., age), user preferences (e.g., preferred ambience), context (e.g., weather and location), and content (e.g., brand) information.

## 2.3. Bayesian networks and user modeling

Bayesian networks are probabilistic representations for uncertain relations, and have been successfully applied to real-world issues such as diagnosis of medical diseases [23,64], troubleshooting of printer problems [38], and telemarketing operation [2].

The definition of Bayesian networks by Jensen [41] includes a set of variables and a set of directed edges between variables, each variable having a finite set of mutually exclusive states, with the variables and the directed edges forming a directed acyclic graph (DAG). The potential table $P ( A | B 1 , . . . , \mathrm { B n } )$ is attached to each variable A with parents $B 1 , . . . ,$ Bn.

User modeling in m-commerce applications is an area into which Bayesian networks fit perfectly, as the relation between different variables is usually not deterministic; that is, there are many influential factors for a particular decision. Bayesian networks can learn from experiences (e.g., they can learn from a database with previous cases) and continuously adapt to changes in the domain. As a result, a Bayesian-network-based application does not require that all probabilities have a high accuracy rate from the beginning in a mobile environment.

A user model is an explicit representation of properties of a particular user, which allows the application to adapt diverse aspects of its performance to individual users' needs [6]. The Bayesian network is an efficient tool for building models of a domain with inherent uncertainties. Witting [80] outlined this for modeling contexts such as user model building. In such a context, we often have to deal with sparse data; on the other hand, in most cases we have additional domain knowledge available. When constructing the structure of a user model, background knowledge can be incorporated by specifying “starting” structures manually that reflect the basic assumptions that we make in the domain. Therefore, a Bayesian-networkbased user model with prior probabilities is particularly suitable to handle a situation with incomplete information such as mobile user modeling.

## 2.4. Related work and literature gap

Due to the importance of mobile advertising, much research has been done on mobile advertising. Barnes [7] introduced the concept of tempting nearby users into the stores and delivering location messaging related to security in a particular area of the city. Ranganathan and Campbell [61] discussed a list of challenges and some ideas for solutions for mobile advertising in pervasive environments. Mahmoud and Yu [56] discussed a novel mobile agent platform that can be used for comparison shopping in a mobile wireless environment, through which businesses can better understand and communicate with the mobile consumer. Their proposed agent-based approach helps the end user reduce information overload by filtering out unnecessary information and show only information that is relevant. Chehimi et al. [13] introduced a novel and highly interactive location- and permissionbased advertising system that allows 3D product advertisements to be displayed on users' mobile phones.

A number of researchers have presented similar systems that provide personalized services for mobile users. Among them, Jukic et al. [42] developed a prototype system that implements a range of personalization strategies and utilizes a set of technologies, such as mobile XML and application of mobile agents, which were used as a test bed for demonstrating and fine-tuning customer profiling and target-marketing techniques. Their consideration of user profile is similar to ours, but their prototype and architecture is not specific for mobile advertising and does not adopt Bayesian network to deal with the uncertainty situation. Yuan and Tsao [82] presented a personalized, contextualized mobile advertising infrastructure (MALCR) for the advertisement of commercial and non-commercial activities. Their recommendation mechanism is novel in its combination of twolevel Neural Network learning, Neural Network sensitivity analysis, and attribute-based filtering. However, it is not clear what variables are considered in their user profile and their system has not been empirically tested. Aalto et al. [1] introduced and implemented a new locationaware mobile advertising system, which is based on Bluetooth positioning and WAP Push. Their research focused on the user location and their system has gone through a thorough quantitative evaluation in a laboratory environment as well as a qualitative user evaluation in the form of a field trial in the real environment of use. However their approach did not consider user demographics, user preference and other personalization factors; therefore, the personalization of their system is limited. Figge and Schrott [32] provided a solution approach based on the Situation Concept and stated how successful mobile advertising could take place. The Situation Concept has identified some personalization factors that need to be considered to individualize mobile customer relationships. These factors can be incorporated to build personalized systems. However, their paper was conceptual and no actual system or prototype was built up. Varshney [76] conceptually proposed a location architecture that could be used to support future mobile advertising application. He believed that by keeping track of users' purchasing habits and current location, a highly targeted advertising campaign could be performed. The architecture is similar to ours. In addition, we have identified specific user preference variables, and implemented and evaluated the system. Choi [20] proposed a new, ubiquitous, GPS/Web-enabled mobile search mechanism based on the user's physical location and search intentions. By using fuzzy query, ubiquitous GPS/Webenabled mobile devices can receive more personalized and locally targeted search results. Lankhorst [48] proposed the Personal Service Environment (PSE), which included user-related information, characteristics of services, location-related information, the network characteristics and terminal capabilities, content-related preferences, and so forth. Zhang [83] implemented a prototype system for personalized mobile-content delivery using the Java 2 Micro Edition (J2ME) based on his framework. Later Zhang and his colleagues [15] proposed an m-service portal architecture and exemplified it with an e-procurement m-service prototype. Their portal architecture integrated m-services to provide adaptive and personalized services and to accommodate the constraints of mobile devices.

At least two key differences exist between our approach and these related research found in the literature. First, the above research does not provide solid literature support and empirical findings that indicate why certain variables should be included in the model constructions. Second, none of these papers adopts Bayesian networks, which is a powerful tool to construct user models with uncertainties.

According to Shuster [67], almost no direct comprehensive studies exist on consumer behaviour and preferences related to the wireless Internet in the public domain. Currently, only a few examples of locationbased services (not necessarily personalized or user specific) exist [75]. More work is also needed to identify new and useful mobile applications and services, including those dealing with personalization of mobile content, context, and location awareness [77].

In summary, the research on consumer behaviour in m-commerce is in its infancy. The research presented in this paper begins to fill the gap in the current literature and paves the way for further empirical research in this area. The empirical approach adopted in this paper examines the potential role of personalization in influencing consumer attitudes toward mobile advertising. In turn, attitudes are verified as influencing intentions to receive mobile advertisements. This paper also determines that context, content, and user preferences are the important components of the personalization factor in mobile advertising applications.

## 3. Research framework of personalization

Research by Tsang and others found entertainment, creditability, irritation, and[AU1] informativeness to be the significant factors affecting respondents' attitudes toward mobile advertising [35,73]. These researchers used attitude as a dependent variable and considered the antecedents of advertising value as factors of attitude in their framework.

Compared to its significance in other types of advertising, personalization is a more important factor in mobile advertising. This factor may help further distinguish the mobile environment from traditional media. Personalization can ensure that visitors to online stores see the most appropriate and appealing Internet advertising [44] and have positive responses ranging from improved attitude toward the website [16] to a decision to purchase [11]. Specifically, in our empirical study we found that respondents' attitudes toward mobile advertising are affected by personalization, in addition to factors proposed by Tsang and others.

For illustration purposes, we chose the dining industry around which to design the personalized mobile advertising application prototype using Bayesian networks. The identification of user preferences comes from the survey done by Londoneats.com [55]. The results show that cuisine, recommendation, price, ambience, and service are ranked in descending order as the most important factors for users in choosing a restaurant.

Based on the existing literature about the dimensions of personalization (as indicated in Section 2.2) and users' preferences when choosing a restaurant, a research framework (Fig. 1) is proposed to illustrate the constructs and items that make up personalization. The empirical study described in the next section will verify whether these components of personalization are important and how they should be grouped together.

## 4. Empirical methodology

## 4.1. Research design

We conducted a field survey in 2005, consisting of a questionnaire designed to collect data regarding personalization components and the effect of personalization on mobile advertising. Convenience samples were collected. We collected convenience samples, which are suitable for the requirements of exploratory research design [21,37,45]. We targeted as research subjects people in China who had experience in using mobile devices and who were above eighteen years of age. The questionnaire contained six parts. The first asked whether the respondents had experience in using mobile devices, SMS, MMS, and mobile Internet. The second part asked about respondents' attitude and intention toward mobile advertising, as well as the improvement of their attitude if mobile advertising was personalized. The third part measured users' general attitudes toward mobile advertising from five perspectives: personalization, entertainment, informativeness, irritation, and creditability. In the second and third parts, the respondents were asked to indicate how strongly they agreed or disagreed with the statements about their perception toward mobile advertising. The fourth part solicited their opinions on how important it was for restaurant merchants to consider user demographics, user preference, content, and context factors when sending mobile advertising messages to users. The fifth part asked about respondents' preferences regarding restaurants and food; this was followed by the collection of demographic data.

![](/api/attachments/Z9FNACMU/fulltext/images/974b6094a132d9d8c9cce6706716380c72c7537c0806ef23460f550315707bdb.jpg)  
Fig. 1. Proposed dimensions of personalization.

## 4.2. Measurement

The constructs and measured items used in this research regarding respondents' attitude and intention toward general mobile adverting, and their perceptions regarding attributes of mobile advertising, have already been validated by prior research. The Theory of Planned Behaviour (TPB) scales of attitude and intention were used, based on Taylor and Todd [72]. The scales of entertainment, informativeness, irritation, and creditability were adapted from Tsang et al. [73]. The factors of personalization were assessed using the measures from Mittal and Lassar [58], and Chellappa and Sin [14]. The wordings of the questionnaire were modified in order to better fit this particular context of mobile advertising. Apart from the demographic attributes and user experience, all other measures were assessed via a 7-point Likert-type scale ranging from “strongly agree” to “strongly disagree.” These scales were reverse-coded where appropriate.

## 4.3. Data description

The questionnaire was pre-tested on twenty individuals and was revised according to their feedback. It was sent to the target people in China in 2005. A total of 235 questionnaires were distributed, and 143 of them were returned within the specified time frame (response rate 60.8%), of which there were 135 usable responses. A total of 48.1% of the respondents were males and 51.9% were females. The respondents included 59.3% who were aged from eighteen to twenty-four, and 32.6% who were twenty-five to thirty-four years old. A total of 83.0% held a college degree. Thus the respondents were primarily young and well educated. A total of 26.7% earned an income of 2000–4000 RMB (U.S. \$250–500) per month, and 44.2% earned below 2000 RMB per month. Because all of the respondents (100%) carried mobile devices and reflected high experience in receiving and sending SMS (99.3%), receiving and sending MMS (58.5%), and accessing the mobile Internet (51.9%), they are relevant and appropriate subjects for this exploratory study.

## 4.4. Data analysis using PLS software

We used Partial Least Squares (PLS) to analyze the data. The PLS procedure [81] has been gaining in popularity and use for behaviour research in recent years because of its ability to model latent constructs under conditions of non-normality with small to medium sample sizes [18,19,22]. It allows the researcher to specify the relationships among both the conceptual factors of interest and the measures underlying each construct, which may result in a simultaneous analysis of (1) how well the measures relate to each construct and (2) whether the hypothesized relationships at the theoretical level are empirically true. This ability to include multiple measures for each construct also provides more accurate estimates of the paths among constructs, which are typically biased downward by measurement error when using techniques such as multiple regressions. Thus, PLS-Graph was used to perform the analysis.

Following a two-step analytical procedure [36], we examined the measurement model first, followed by the structural model. The rationale behind this two-step approach is that it ensures that the conclusion about the structural relationship is drawn from a set of measurement instruments with desirable psychometric properties.

The reliability and convergent validity were also checked using PLS software. All measure items had significant path loadings at the 0.01 level. All the values of composite reliability and average variance extracted were considered satisfactory, with composite reliability at 0.82 or above and average variance extracted at 0.62 or above, all of which exceeded the 0.5 recommended levels [45]. Discriminant validity was successfully verified with the squared root of the average variance extracted for each construct higher than the correlations between it and all other constructs [33]. The statistics checking demonstrated strong empirical support for the reliability, convergent validity, and discriminant validity of the scales of the research model.

Fig. 2 presents the results of the analysis with overall explanatory powers, estimated path coefficients (all significant paths are indicated with an asterisk), and associated t-value of the paths. Tests of significance of all paths were performed using the bootstrap resampling procedure. As shown in Fig. 2, all hypothesized paths (except the links between attitude and informativeness, and attitude and irritation) in the research model were found to be statistically significant at a 95% significance level.

As shown in Fig. 2, only three determinants of behavioural attitude (entertainment, creditability, and personalization) were found to have significant effects on behavioural attitude, with path coefficients of 0.38, 0.31, and 0.16, respectively. The three constructs explain a 51.2% variance in behavioural attitude. In addition, attitude was found to have a significant effect on intention with a path coefficient of 0.722, and explains a 52.2% variance in intention. In summary, personalization appears to indeed be one important variable that affects the user's attitude and intention toward mobile advertising.

![](/api/attachments/Z9FNACMU/fulltext/images/81ce92ae70a24c71dc0d6e04b994809e781dea480cea87f8a7bda44ef9ed6daf.jpg)  
Fig. 2. Results of PLS analysis.

Measures of items for personalization

<table><tr><td>Factor Items</td><td>Min</td><td>Max</td><td>Mean</td><td>Rank</td><td>SD</td></tr><tr><td>Price</td><td>3</td><td>7</td><td>6.12</td><td>1</td><td>1.091</td></tr><tr><td>Discount</td><td>3</td><td>7</td><td>6.00</td><td>2</td><td>1.164</td></tr><tr><td>Restaurant Service</td><td>1</td><td>7</td><td>5.63</td><td>3</td><td>1.320</td></tr><tr><td>Restaurant Ambience</td><td>1</td><td>7</td><td>5.57</td><td>4</td><td>1.306</td></tr><tr><td>Brand</td><td>2</td><td>7</td><td>5.56</td><td>5</td><td>1.226</td></tr><tr><td>Cuisine type</td><td>1</td><td>7</td><td>5.50</td><td>6</td><td>1.268</td></tr><tr><td>Food</td><td>1</td><td>7</td><td>5.48</td><td>7</td><td>1.248</td></tr><tr><td>User activities</td><td>1</td><td>7</td><td>5.31</td><td>8</td><td>1.388</td></tr><tr><td>Location</td><td>1</td><td>7</td><td>5.26</td><td>9</td><td>1.510</td></tr><tr><td>Time</td><td>1</td><td>7</td><td>5.16</td><td>10</td><td>1.496</td></tr><tr><td>Device type</td><td>1</td><td>7</td><td>4.69</td><td>11</td><td>1.522</td></tr><tr><td>Weather</td><td>1</td><td>7</td><td>4.65</td><td>12</td><td>1.720</td></tr></table>

## 4.5. Components of personalization

Descriptive statistics regarding the components of personalization are shown in Table 1, including the mean, standard deviation, and the ranking. The table shows that all of these components are important to personalized mobile advertising, as the means are all higher than the neutral score of 4.

The principal component analysis was conducted to determine personalization factors and to classify specific factors into fewer categories. In order to best identify the relationships between the specific factors and the latent variables, the variance-maximizing approach of orthogonal rotation was used to extract three principal components. The accumulated explained variance was found to be 69.80%. The results of the factor analysis, the Cronbach's coefficient of each principal component, and the overall Cronbach's coefficient of the factors are summarized in Table 2. It was also confirmed that personalization is composed of three main components—user preference, context and content—with user's profile as a moderating factor. In Table 2, component 1 represents the context, component 2 represents user preference, and component 3 represents content. Three to five items were measured for each of the three components. The highest Eigen value (3.07) and explained variance (25.61%) of the first component (labeled as the “context” factor) suggest the significant emphasis placed by mobile phone users on this feature for personalized mobile advertising. The second most important components are the “user preference” factor with a high Eigen value (2.84) and explained variance (23.74%), followed by the “content” factor with an Eigen value of 2.24 and explained variance of 18.70%. The factor analysis results in Table 2 suggest solid convergent and discriminant validity, which means the items measuring one particular component of personalization are strongly associated with it, and not other dimensions. Convergent validity is demonstrated by an item's high loadings on its own dimension, which are all close to 0.70 or higher. Based on the statements above as well as the loadings, it can be seen that these twelve factor items discriminate well into three factors, and they converge among each specific factor. The items low loadings with the other two dimensions (b0.301) suggest the items are distinguishably associated with only one component of personalization. The validity of the scales is reinforced by the high-reliability measures.

Table 2  
Result of analysis of personalization factors

<table><tr><td rowspan="2">Factor</td><td rowspan="2">Mean</td><td rowspan="2">Rank</td><td rowspan="2">Specific factor items</td><td colspan="3">Factor loading</td><td rowspan="2">Cronbach&#x27;s alpha</td></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td rowspan="4">User preference</td><td rowspan="4">5.92</td><td rowspan="4">1</td><td>Cuisines</td><td>0.035</td><td>0.862</td><td>0.122</td><td>0.860</td></tr><tr><td>Food type/style</td><td>0.083</td><td>0.817</td><td>0.203</td><td></td></tr><tr><td>Restaurant service</td><td>0.266</td><td>0.793</td><td>0.201</td><td></td></tr><tr><td>Restaurant ambience</td><td>0.281</td><td>0.720</td><td>0.205</td><td></td></tr><tr><td rowspan="5">Context</td><td rowspan="5">5.19</td><td rowspan="5">3</td><td>User activities</td><td>0.800</td><td>0.084</td><td>0.301</td><td>0.830</td></tr><tr><td>User location</td><td>0.808</td><td>0.055</td><td>0.222</td><td></td></tr><tr><td>Weather</td><td>0.737</td><td>0.224</td><td>-0.02</td><td></td></tr><tr><td>Time</td><td>0.832</td><td>0.114</td><td>0.001</td><td></td></tr><tr><td>Mobile device types</td><td>0.594</td><td>0.139</td><td>0.01</td><td></td></tr><tr><td rowspan="3">Content</td><td rowspan="3">5.55</td><td rowspan="3">2</td><td>Price</td><td>0.066</td><td>0.209</td><td>0.864</td><td>0.808</td></tr><tr><td>Discount</td><td>0.112</td><td>0.117</td><td>0.865</td><td></td></tr><tr><td>Restaurant brand</td><td>0.133</td><td>0.377</td><td>0.684</td><td></td></tr><tr><td>Eigen value</td><td></td><td></td><td></td><td>3.07</td><td>2.84</td><td>2.24</td><td>0.855</td></tr><tr><td>Explained variance (%)</td><td></td><td></td><td></td><td>25.61</td><td>23.74</td><td>18.70</td><td></td></tr><tr><td>Explained variance accumulated (%)</td><td></td><td></td><td></td><td>25.61</td><td>49.35</td><td>68.02</td><td></td></tr></table>

From the above data analysis, we have seen that the most important factor influencing personalization is the context factor, followed by user preference and content respectively. This result is expected because context is most unique to mobile advertising, which makes it different from the traditional advertising media such as television and newspaper advertising. The likelihood is low that these traditional media would incorporate timely personalized advertising based on user context information (e.g., location). Internet advertisers might consider some kinds of context factors, but they would be limited in comparison to mobile advertisers. The user preference factor is not unique to mobile media, as Internet providers can also collect user information and consider personal preference to recommend a piece of advertising, which explains the secondary importance of this factor. That content is the third most important factor is also reasonable because content is least unique to mobile media, and any medium can broadcast a merchant's information including price, discount, and brand name.

## 5. Model components

The components of personalization we extracted from the data analysis, along with several models and a matching engine we developed, were used to construct a Bayesian-network-based, personalized advertising mobile application prototype.

## 5.1. Bayesian-network-based model component

The proposed Bayesian-network-based model component is shown in Fig. 3. It consists of a user model (including user profiles and preferences), a context model, some content-related information (regarding products and services), and a matching engine. Age, gender, education, and income make up the individual characteristics for the user profiles (upper left). Price, product (cuisine type), and quality (service and ambience) are the stimuli listed under the user preferences (upper right). Promotion and brand are the vendor's content information (bottom left), and distance, weather, time, and activity form the elements of the context model (bottom right).

Users will be more satisfied if mobile dining messages are relevant and are sent to them at the right time and in the right situations. For example, a user who prefers Chinese food would find a Japanese restaurant promotion irrelevant; likewise, a lunch coupon would be of little interest to evening diners. Determining the relevance of messages is a complex decision-making process involving multiple factors that are often interrelated—the main motive for using Bayesian networks in the construction of the models.

## 5.2. Prior probabilities setting

After building the model structure, we needed to set up the prior probabilities. From the empirical study described in Section 4, we used a database filled with information from the questionnaire to calculate the prior probabilities of the model. For example, we might have assumed that the possibility for a random person to like American food was 25%; if the user was a male, the possibility that he liked American food became 33%. Further, if the user was also between the ages of twentyfive and thirty-four, the probability increased to 50%. Similarly, the database can indicate a prior possibility for a person with a certain education level and income to like seafood or good restaurant ambience.

![](/api/attachments/Z9FNACMU/fulltext/images/0c662fdfb6db17786e9acabb39025ab38c9cd821a5c31088f1fe9c73c70b1aa4.jpg)  
Fig. 3. Model component consisting of user model, context model, content information, and matching engine

For those prior probabilities that could not be obtained directly from the questionnaire, the knowledge of domain experts was involved. The knowledge was precisely transferred to the models in the format of a Bayesian network. Converting the expert knowledge into Bayesian-network-based models involved determining the states of the variables, the relations among the variables, and the associated prior probabilities—a complex and time-consuming task requiring support of a software package. Hugin Lite 6.3 was used in this research to collect and consolidate expert knowledge, and to perform network reasoning and adaptation for the models and the matching engine.

Experts were invited to specify the weights on the variables as well. Specifying probabilities for a given structure is difficult, and different experts may provide different values, which may lead to inaccurate results. Therefore, when we held equal confidence in each of the experts, we used the mean of the values advised by them; otherwise, a weighted average was generated [41]. Eventually, the experts' knowledge and the survey data were used by the model as a seed to automatically complete all the information needed to build the Bayesian network.

## 5.3. Matching engine

For the prototype to make a prediction, each instance of the Bayesian network of the user model propagates the information based on its structure and conditional or prior probabilities and returns the post-probabilities associated with each interest status (strong interest, medium, low) of acceptance for a particular restaurant. The same propagation process applies to the context model as well. Consequently, the Bayesian-networkbased matching engine takes the output probabilities from both the user model and the context model as its direct attributes, together with the brand and promotion information, to make a prediction. After the information propagation, the output of the Bayesian network of the engine is a decision status (sending a promotion message or not) with an associated probability. If the “send” probability is higher than a preset threshold, the promotion messages will be sent out to the user.

## 6. Architecture and interfaces of the personalized mobile application

A prototype has been developed in order to implement the proposed model components to provide personalized advertisements to mobile users. The construction of both the Web interface and mobile interface can be exemplified in the illustration below, with the decision-making process based on the following scenario: The time is noon, the user's location is near a restaurant “CFC” (e.g., the user is within 1 km of CFC), the user is not busy with work, and CFC is promoting a newly created Western-style lunch set.

In this illustration, CFC wants to identify the potential target users with the help of the prototype. The decision process will generate a list of users in descending order of probability, indicating the likelihood of the users being interested in CFC's products or services. Based on the list, CFC can use a “push” method to send promotion messages to the potential customers more selectively. Fig. 4 shows the top four users sorted by interest probabilities in a descending order. The match ratio is the interest probabilities of the “yes” state in the “send” node shown in Fig. 3. If the interest probability of a user exceeds CFC's threshold setting (e.g., 45%), the prototype will signal “send,” and the corresponding customer (e.g., Lucy Thor) together with other users with a higher probability (e.g., Anna Wu, Jacky Wang, and Alice Lau) will receive promotion information about CFC. If the recipient uses the coupon before the expiration date, the prototype will consider this case as a positive adaptation; if not, it will be considered a negative adaptation, and it will consequently learn from these experiences and update the probabilities for future calculations. Obviously, the more cases of positive adaptation, the more accurate the personalization model will be.

<table><tr><td colspan="7">Branch: 119</td></tr><tr><td></td><td>Customer</td><td>Gender</td><td>Age</td><td>Education</td><td>Month Income</td><td>Match Ratio</td></tr><tr><td>1</td><td>Lucy Thor</td><td>Male</td><td>16-30</td><td>Secondary</td><td>Below10000</td><td>99.99%</td></tr><tr><td>2</td><td>Anna Wu</td><td>Female</td><td>16-30</td><td>Secondary</td><td>Below10000</td><td>50.0%</td></tr><tr><td>3</td><td>Jack Wang</td><td>Male</td><td>&gt;30</td><td>Bachelor</td><td>10000-30000</td><td>50.0%</td></tr><tr><td>4</td><td>Alice Lau</td><td>Female</td><td>16-30</td><td>MasterAbove</td><td>Above30000</td><td>50.0%</td></tr></table>

Fig. 4. Web interface for merchants to search matched customers.

Similarly, mobile users can use their mobile devices to identify which coupons offered by the nearby merchants best fit their profile. For example, if Anna Wu is a registered user who has saved her personal demographics and preferences in the user database of the application and wants to find an appropriate restaurant coupon for lunch, she can push “start” and select her preferred food style (Fig. 5a). The application will search for the most suitable restaurant by matching Anna's personal profile with the merchant's content plus context information.

The application will send Anna Wu the restaurant list as shown in Fig. 5b, with the restaurants sorted in descending order. KFC, CFC, and McDonald's turn out to be the top three good choices for her. If she is most interested in CFC among the entire list of restaurants, she can further obtain information about it by selecting CFC. The information (Fig. 5c) includes the merchant coupon, address and telephone number, and even the merchant's location map if available on the map server. CFC has created a coupon, so if Anna chooses the “view m-coupon” option, the coupon content will be shown in Fig. 5d. Additionally, if she wants to download the coupon to her own mobile device for later use, she can do so by clicking “download” to save it to her mobile device. After the coupon is used by Anna, her profile with the merchant's content and the context information will be considered a completely new case to be put into

Bayesian networks, which can learn from and adapt automatically to the new case so that the accuracy of the model can be improved continuously. After the learning adaptation, when CFC next uses the web interface to search potential customers, the matching ratio for Anna will increase correspondingly.

## 7. Evaluations and discussion

To evaluate the proposed application, we conducted an experiment in a large public university in China. In this experiment, 90.16% of subjects (sample size: 183) had the prior experience of having received mobile advertisements. One group with 93 subjects was sent random mobile advertisements without any personalization. The other group with 90 subjects received a personalized mobile advertisement from the system. The results show a statistically significant difference at α = .05 between the two groups in terms of their views on the personalization of mobile advertisements sent to them in the experiment (t = 2.36, p = 0.019), their attitude toward these mobile advertisements (t = 2.46, p = 0.015), and the indication of willingness to utilize these mobile advertisements (t = 2.24, p = 0.027). The preliminary result indeed shows that the system of sending out personalized mobile advisements is effective and can influence users' consumption behaviour.

A number of limitations to this study should be noted. First, the data were collected in China and, therefore, generalizing to other countries should be done with caution due to different cultural issues, economies, and development stages of mobile advertising. However, since the study was conducted in one of the countries with relatively high penetration of mobile advertising, the personalization factors identified here might provide some reference for other countries that are just beginning to develop the market of mobile advertising. Second, due to the limitation of self-report measures, the factors that were identified are not exhaustive. Other uncertainties may influence consumer decision to accept the mobile advertisements, such as mood and whether someone is accompanying them at the time they receive the transmission. Therefore, the system may not satisfy all people in diverse situations. However, Tarasewich [71] also realized that, realistically, all context characteristics (e.g., mental state, noise) are not relevant (or important) to an m-commerce application or its user at a given time. In addition, we have reviewed the relevant literature to identify the important factors and have confirmed these factors by empirical study.

![](/api/attachments/Z9FNACMU/fulltext/images/3c07dcbcdbb1a848d751ebd86c5bdc7052949ad298364855a02a5d79909cf87f.jpg)  
Fig. 5. Mobile interface for customers.

This research has two goals. One is to illustrate how Bayesian networks can be built by combing both the empirical approach and the design method to construct a personalized mobile advertising system. The non-exhaustive factors may not harm this objective. As an ongoing project of ours, other methods such as interviews will be used to determine if there are other key factors and incorporate them into our system at the outset. The second goal is to design a system to send out personalized mobile advertising and improve user attitude toward mobile advertising. The system has preliminarily achieved this objective, which is confirmed by the statistically significant difference in user attitude toward the sent mobile advertisements between the treatment group and control group. Furthermore, with the inherent adaptability function, the Bayesian network can learn from real experiences and update the probabilities automatically when the function is applied in practice.

## 8. Contribution and conclusion

Design and behavioural science have complementary roles in the IS discipline. Lee [49] and Hevner et al. [40] observed that technology and behaviour are inseparable rather than dichotomous in an information system. The behavioural science concept aims at developing and verifying theories that explain or foresee individual or organizational behaviour. The design-science concept seeks to extend the boundaries of human and organizational capabilities by creating new and innovative objects.

This paper has proposed a design research method that combines an empirical approach and modeling techniques for the design of a personalized mobile application. First, we conducted a questionnaire survey to verify the users' purchasing decision theory in the traditional marketing research and confirm that e-commerce settings can be applied to the m-commerce context. Further, we identified the factors that influence users' purchasing decisions and extend marketing theories in the m-commerce context in order to predict users' purchasing behaviour in the m-commerce environment. Next, those empirical findings were combined with the Bayesian-network-modeling technique for the development of a personalized mobile advertising environment. More concretely, those personalization component variables were used to build the Bayesian network structure, and the data collected from the empirical study were used to set the prior probabilities. A prototype implementing the user model, content model, context model, and a matching engine to deliver more relevant advertisements to the right mobile customers has been developed as a result.

In order to verify the effectiveness of the proposed design research method, we chose the dining industry in our study to test the model components. User preferences regarding food and restaurants were collected as part of the user preference and content components. This prototype can be applied to other industries as well, such as movies, CDs, books, hotel booking, flight booking, and all manner of retail sectors. Taking the movie business as an example, user preferences regarding movies such as the preference for an actor, director, or movie type (e.g., action or romance) would be input into the user preference component. Information about movie theatre preference would be input into the content component. User demographic data and the context model would remain unchanged. We believe that our prototype will enable far more effective advertising in comparison with random message sending, because of the intrinsic capacity of Bayesian networks to deal with uncertainties and causal relationships.

There will be two directions for our future research. One is to consider more factors that will influence personalization, find ways to measure them, and incorporate them into our systems. The other is to collect more data points so that we can compare current Bayesian network systems with other techniques such as neural networks.

## Acknowledgements

We would like to thank the editor and four reviewers, whose suggestions were very helpful and guided us in improving the paper. We acknowledge S.J. Zhu and C.S. Wang for their help in conducting the experiment and collecting the experimental data. The research related to this paper is directly supported by the Strategic Research

Grant (SRG no. 7001897 and no. 7001738) of the City University of Hong Kong.

## Appendix A. Questionnaire

The following are the questions used to collect data in the study.

## Attitude

I like the idea of using mobile advertising.

It is wise to use mobile advertising.

My attitude toward using mobile advertising is positive.

## Intention

I think I will use mobile advertising to consume whenever I have a chance.

I intend to use mobile advertising message for shopping after I receive it.

It is likely that I am going to use mobile advertising to purchase.

## Personalization

I feel that mobile advertising would tailor to me.

I feel that personalization is one characteristic of mobile advertising.

The contents in mobile advertisements are personalized.

## Components of personalization

1. Please indicate the importance of the following items, which a restaurant should consider to compose a personalized mobile advertising message sent to you. User preference a. Cuisine b. Food style c. Restaurant service d. Restaurant ambience e. Others (please specify) Content information a. Price b. Discount c. Restaurant brand d. Others (please specify)

2. Please indicate the importance of the following items, which should be taken into consideration to compose a personalized mobile advertising message sent to you. a. User activities b. User location c. Weather d. Time e. Types of user mobile device f. Others (please specify)

## References

[1] L. Aalto, N. Göthlin, J. Korhonen, T. Ojala, Bluetooth and WAP push based location–aware mobile advertising system, Proceedings of the Second International Conference on Mobile Systems, Applications, and Services (MobiSys04), ACM Press, 2004.

[2] J.H. Ahn, K.J. Ezawa, Decision support for real-time telemarketing operations through Bayesian network learning, Decision Support Systems 21 (1) (1997).

[3] B. Anckar, D. D'Incau, Value-added services in mobile commerce: an analytical framework and empirical findings from a national consumer survey, HICSS (2002) 1444–1453.

[4] A.S. Andreou, C. Chrysostomou, C. Leonidou, S. Mavromoustakos, A. Pitsillides, G. Samaras, C. Schizas, Mobile commerce applications and services: a design and development approach, First International Conference on Mobile Business, M-Business, Athens, Greece, 2002.

[5] D. Barbara, Mobile computing and databases—a survey, IEEE Transactions on Knowledge and Data Engineering 11 (1) (1999).

[6] S.J. Barnes, The mobile commerce value chain: analysis and future development, International Journal of Information Management 22 (2) (2002).

[7] S.J. Barnes, Known by the network: the emergence of locationbased mobile commerce, Advances in Mobile Commerce Technologies, 2003.

[8] S.J. Barnes, Wireless digital advertising: nature and implications, International Journal of Advertising 21 (3) (2003).

[9] P. Barwise, C. Strong, Permission-based mobile advertising, Journal of Interactive Marketing 16 (1) (2002).

[10] L.K. Brackett, B.N. Carr, Cyberspace advertising vs. other media: consumer vs. mature student attitudes, Journal of Advertising Research 41 (5) (2001).

[11] G. Chakraborty, V. Lala, D. Warren, What do customers consider important in B2B websites? Journal of Advertising Research 43 (1) (2003).

[12] L. Chao, Cellphone ads are easier pitch in China, Wall Street Journal 249 (Jan. 4, 2007) B5 (1).

[13] F. Chehimi, P. Coulton, R. Edwards, Delivering 3D advertising to mobile phones, Consumer Electronics, ICCE 06 (2006).

[14] R.K. Chellappa, R.G. Sin, Personalization versus privacy: an empirical examination of the online consumer's dilemma, Information Technology and Management 6 (2005).

[15] M. Chen, D. Zhang, L. Zhou, Providing web services to mobile users: the architecture design of an m-service portal, International Journal of Mobile Communications 3 (1) (2005).

[16] Q. Chen, W.D. Wells, Attitude toward the site, Journal of Advertising Research 39 (5) (1999).

[17] K. Cheverst, K. Mitchell, N. Davies, Design of an object model for a context sensitive tourist guide, Proceedings of the International Workshop on Interactive Applications of Mobile Computing (IMC98), Rostock, Germany, 1998.

[18] W.W. Chin, Modern methods for business research, in: G.A. Marcoulides (Ed.), The Partial Least Squares Approach for Structural Equation Modeling, Lawrence Erlbaum Associates, 1998.

[19] W.W. Chin, A. Gopal, Adoption intention in GSS: relative importance of beliefs, Database for Advances in Information Systems 26 (2–3) (1995).

[20] D.Y. Choi, Personalized local Internet in the location-based mobile web search, Decision Support Systems 43 (1) (2007).

[21] S.J. Coakes, L.G. Steed, SPSS Analysis without Anguish, John Wiley & Sons Australia, Ltd., 1999.

[22] D.R. Compeau, C.A. Higgins, Application of social cognitive theory to training for computer skills, Information Systems Research 6 (1995).

[23] J.E. Desmedt, Computer-Aided Electromyography and Expert Systems, Elsevier Science Publishers, Amsterdam, 1990.

[24] A.K. Dey, D. Salber, G.D. Abowd, A conceptual framework and a toolkit for supporting the rapid prototyping of context-aware applications, Human–Computer Interaction Journal 16 (2–4) (2001).

[25] S. DeZoysa, Mobile advertising needs to get personal, Telecommunications International 36 (2) (2002).

[26] A.P. Dickinger, A. Haghirian, A. Scharl, J. Murphy, A conceptua model and investigation of SMS marketing, Thirty-Seventh Hawaii International Conference on System Sciences (HICSS-37), Hawaii, U.S.A., 2004.

[27] R. East, Consumer Behaviour, Prentice Hall, 1997.

[28] eMarketer, SMS marketing yields strong results, eMarketer Research Report, 2003.

[29] eMarketer, Mobile Messaging: Not Sexy, But Profitable, http:// www.emarketer.com/Article.aspx?id=1004216. October 18, 2006.

[30] Enpocket, http://www.enpocket.com/news/press-releases/researchshows-that-targeting-and-relevance-are-key-to-making-mobileadvertising-work (2006).

[31] W. Fan, M.D. Gordon, P. Pathak, Effective profiling of consumer information retrieval needs: a unified framework and empirical comparison, Decision Support Systems 40 (2005).

[32] S. Figge, G. Schrott, 3G “Ad” work-3G's breakthrough with mobile advertising, Proceedings of the Eighth International Workshop on Mobile Multimedia Communications, Munich, Germany, October 5–8, 2003.

[33] C. Fornell, D. Larcker, A second generation of multivariate analysis: classification of methods and implications for marketing research, in: M.J. Houston (Ed.), Review of Marketing, American Marketing Association, Chicago, 1987.

[34] G.M. Giaglis, P. Kourouthanassis, A. Tsamakos, Towards a classification framework for mobile location services, in: B.E. Mennecke, T.J. Strader (Eds.), Mobile Commerce: Technology, Theory, and Applications, Idea Group Publishing, 2003.

[35] P. Haghirian, A. Inoue, An advanced model of consumer attitudes toward advertising on the mobile internet, International Journal of Mobile Communications 5 (1) (2007).

[36] J.F. Hair, R.E. Anderson, R.L. Tatham, W.C. Black, Multivariate Data Analysis, Prentice Hall, Englewood Cliffs, NJ, 1998.

[37] J.F. Hair, R.P. Bush, D.J. Ortinau, Marketing Research: A Practical Approach for the New Millenium, Irwin McGraw–Hill, 2000.

[38] D. Heckerman, J. Breese, K. Rommelse, Decision-theoretic troubleshooting, Communication of the ACM 38 (3) (1995).

[39] H.V.D. Heijden, Mobile decision support for in-store purchase decisions, Decision Support Systems, 42 (2) (2006).

[40] A.R. Hevner, S.T. March, J. Park, S. Ram, Design science in information systems research, MIS Quarterly 28 (1) (2004).

[41] F.V. Jensen, Bayesian Networks and Decision Graphs, Springer, New York, 2001.

[42] N. Jukic, A. Sharma, B. Jukic, M. Parameswran, M-Commerce: Analysis of Impact on Marketing Orientation, 2003 http://www. ebusinessforum.gr/content/downloads/011020.pdf.

[43] P. Kavassalis, N. Spyropoulou, D. Drossos, E. Mitrokostas, G. Gikas, A. Hatzistamatiou, Mobile permission marketing: framing the market inquiry, International Journal of Electronic Commerce 8 (1) (2003).

[44] J.W. Kim, B.S. Lee, M.J. Shaw, H.L. Chang, M. Nelson, Application of decision-tree induction techniques to personalized

advertisements on Internet storefronts, International Journal of Electronic Commerce 5 (3) (2001).

[45] T.C. Kinnear, J.R. Taylor, Marketing Research: An Applied Approach, 5th edition, McGraw–Hill, 1996.

[46] H. Komulainen, T. Mainela, J. Sinisalo, J. Tahtinen, P. Ulkuniemi, Business model scenarios in mobile advertising, International Journal of Internet Marketing and Advertising 3 (3) (2006).

[47] N. Kumar, A. Gangopadhyay, G. Karabatis, Supporting mobile decision making with association rules and multi-layered caching, Decision Support Systems 43 (1) (2007).

[48] M.M. Lankhorst, H.V. Kranenburg, A. Salden, A.J.H. Peddemors, Enabling technology for personalizing mobile services, Proceedings of the Hawaii International Conference on System Sciences, Big Island, Hawaii, U.S.A., 2002.

[49] A. Lee, Systems thinking, design science, and paradigms: heeding three lessons from the past to resolve three dilemmas in the present to direct a trajectory for future research in the information systems field, keynote address, Eleventh International Conference on Information Management, Taiwan, 2000.

[50] H.S. Lee, C.H. Lee, G.H. Lee, Y.H. Kim, B.G. Lee, Analysis of the actual response rates in mobile advertising, Innovations in Information Technology (Nov, 2006) 1–5.

[51] Y.E. Lee, I. Benbasat, Interface design for mobile commerce, Communications of the ACM 46 (12) (2003).

[52] M. Leppaniemi, H. Karjaluoto, Factors influencing consumers' willingness to accept mobile advertising: a conceptual model, International Journal of Mobile Communications 3 (3) (2005).

[53] H.R. Li, K.Y. Lee, Mobile phones and mobile advertising: an Asian perspective, International Journal of Internet Marketing and Advertising 3 (2) (2006).

[54] S. Liao, J. He, T. Tang, A framework for context information management, Journal of Information Science 30 (6) (2004).

[55] Londoneats, http://www.londoneats.com/news/poll.asp?PollID=34 (2004).

[56] Q.H. Mahmoud, L. Yu, Havana agents for comparison shopping and location-aware advertising in wireless mobile environments, Electronic Commerce Research and Applications 5 (3) (2006).

[57] Ministry of Information Industry, http://www.mii.gov.cn (2005).

[58] B. Mittal, W.M. Lassar, The role of personalization in service encounters, Journal of Retailing 72 (1) (1996).

[59] S. Nadkarni, P.P. Shenoy, A causal mapping approach to constructing Bayesian networks, Decision Support Systems 38 (2) (2004).

[60] S. Okazaki, Mobile advertising adoption by multinationals, Internet Research 15 (2) (2005).

[61] A. Ranganathan, R.H. Campbell, Advertising in a pervasive computing environment, Proceedings of the Second International Workshop on Mobile Commerce, Georgia, U.S.A, 2002.

[62] B. Rao, L. Minakakis, Evolution of mobile location-based services, Communications of the ACM 46 (12) (2003).

[63] Research and Markets, http://www.researchandmarkets.com reports/296002 (2006).

[64] G.C. Sakellaropoulos, G.C. Nikiforidis, Prognostic performance of two expert systems based on Bayesian belief networks, Decision Support Systems 27 (2000).

[65] SBDC, http://www.isbdc.org/start\_up/market3.cfm (2002).

[66] A. Schmidt, M. Beigl, H.W. Gellersen, There is more to context than location, Computer & Graphics 23 (1999).

[67] T. Shuster, Pocket Internet and M-Commerce— (How) Will it fly, 2001 www.gwu.edu/\~emkt/ Ecommerce/file/Mcommerce. pdf.

[68] K. Siau, E.P. Lim, Z. Shen, Mobile commerce: promises, challenges and research agenda, Journal of Database Management 12 (3) (2001).

[69] T.F. Stafford, M.L. Gillenson, Mobile commerce: what it is and what it could be, Communications of the ACM 46 (12) (2003).

[70] D.W. Stewart, P.A. Pavlou, From consumer response to active consumer: measuring the effectiveness of interactive media, Journal of the Academy of Marketing Science 30 (4) (2002).

[71] P. Tarasewich, Designing mobile commerce applications, Com munications of the ACM 46 (12) (2003).

[72] S. Taylor, P.A. Todd, Understanding information technology usage: a test of competing models, Information Systems Research 6 (2) (June 1995).

[73] M.M. Tsang, S.C. Ho, T.P. Liang, Consumer attitudes toward mobile advertising: an empirical study, International Journal of Electronic Commerce 8 (3) (2004).

[74] E. Turban, N. Lee, D. King, H.M. Chung, Electronic Commerce— A Managerial Perspective, Prentice Hall, 2000.

[75] U. Varshney, M-Commerce Tutorial, ACM Mobicom, 2002 (slides available via e-mail: uvarshney@gsu.edu).

[76] U. Varshney, Location management for mobile commerce applications in wireless internet environment, ACM Transactions on Internet Technology 3 (3) (2003).

[77] U. Varshney, Wireless I: mobile and wireless information systems: applications, networks, and research problems, Communications of the AIS 12 (2003).

[78] U. Varshney, R. Vetter, Mobile commerce: framework, applications and networking support, Mobile Networks and Applications 7 (2002).

[79] V. Venkatesh, V. Ramesh, A.P. Massey, Understanding usability in mobile commerce, Communications of the ACM 46 (12) (2003).

[80] F. Wittig, ML4UM for Bayesian network user model acquisition, Proceedings of the second workshop on machine learning, information retrieval and user modeling, Johnstown, PA U.S.A., 2003.

[81] H. Wold, Introduction to the second generation of multivariate analysis, in: H. Wold (Ed.), Theoretical Empiricism, Paragon House, New York, 1989.

[82] S.T. Yuan, Y.W. Tsao, A recommendation mechanism for contextualized mobile advertising, Expert Systems with Applications 24 (4) (2003).

[83] D.S. Zhang, Delivery of personalized and adaptive content to mobile devices: a framework and enabling technology, Communication of the AIS 12 (13) (2003).

David Jingjun Xu is a Ph.D. student in Management Information Systems at the Sauder School of Business, University of British Columbia. He finished his M.Phil Degree of Information Systems at City University of Hong Kong. His research interests include recommendation agents, E-commerce service, human–computer interaction and mobile commerce application.

Stephen Shaoyi Liao is Associate Professor of Information Systems at City University of Hong Kong. He earned a Ph.D. from the University of Aix-Marseille III and Institute of France Telecom in 1993. He has been working at City University of Hong Kong since 1993 and his research has focused on use of IT in e-business systems. His articles have been published in Decision Support Systems, IEEE transactions, Communications of the ACM, Information Science, Computer Software and other SCI journals.

QiuDan Li is a researcher in the Laboratory of Complex Systems and Intelligence Science, Institute of Automation, Chinese Academy of Sciences, China. She received a Ph.D. in Computer Science from Da Lian University of Technology, China. Her current research interests include data mining and mobile commerce application.
