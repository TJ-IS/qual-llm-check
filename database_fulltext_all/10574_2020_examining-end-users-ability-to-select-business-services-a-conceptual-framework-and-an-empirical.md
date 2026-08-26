---
otero_id: 10574
otero_key: "9R6YDYPC"
title: "Examining end users’ ability to select business services: A conceptual framework and an empirical study"
authors: "Padmal Vitharana; Amiya Basu"
year: "2020"
journal: "Information & Management"
doi: "10.1016/j.im.2019.103241"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Examining end users’ ability to select business services: A conceptual framework and an empirical study

Padmal Vitharana\*, Amiya Basu

![](/api/attachments/9R6YDYPC/fulltext/images/fe28cd1e388536cbaee44118ea9ef447cb74accd363003144d7e42cf0bf2124f.jpg)

Martin J. Whitman School of Management, Syracuse University, Syracuse, NY 13244-2130, USA

## A R T I C L E I N F O

Keywords: Business services Service duplication Empirical study Requirements

## A B S T R A C T

Software made from autonomous business services is gaining popularity. Now end users can build large applications by assembling a suite of services. Because some end users might have limited knowledge of their requirements and the functionality of available services, the key challenge is to find the services needed to build an application. The task of finding the services matching requirements requires specialized knowledge—knowledge of requirements and the functionality of available services—not just mere general competence. Moreover, the complexity of the requirements could also hinder the ability of end users to select services. However, there is little research into how the end users sophistication and requirement complexity afect their ability to avoid duplication (i.e., select the most cost-efective set of services) and select a set of services that satisfy their requirements. We provide a conceptual framework for the choice problem faced by the decision maker and develop a set of hypotheses on end user's sophistication and requirement complexity, and the impact of these factors on outcome performance—the ability to avoid duplication and select the appropriate services. Then we conduct an empirical study to test the hypotheses. Empirical results ofer support for all hypotheses. Our work has several implications. We demonstrate both conceptually and empirically that end users’ naivety has a significant impact on service duplication. For a profit-maximizing service vendor, knowledge of the end user's sophistication/naivety allows there to be diferent pricing strategies: (1) a pure component strategy, (2) a pure bundling strategy, or (3) a mixed bundling strategy.

## 1. Introduction

Over the years, software systems built from components and web services have become commonplace [1,2]. The service-oriented architecture provides the architectural model for implementing applications using web services. Such applications rely on a set of services that communicate with each other and with other applications using a messaging protocol over the Internet [3]. More recently, microservice-based application development has started to gain traction in the industry. Unlike web services, a microservice represents a single function around a business capability, encompasses own data resources, and is quickly deployable [1]. Instead of the monolithic architecture prevalent in conventional development, the nascent architecture relies on building applications using independently deployable microservices. Software is no longer built from scratch, and the emerging trend to build applications using business services is likely to continue into the foreseeable future.

There are many vendors ofering components and web services, such as Amazon Web Services (https://aws.amazon.com) and ComponentSource (https://www.componentsource.com). For example, Amazon's pay-as-you-go model allows organizations to pay for services as needed, thereby afording greater responsiveness to change without overcommitting their budgets. Many services can be downloaded and incorporated into applications or can be invoked over a network, over the Internet, or in the cloud using a software-as-a-service (SaaS) subscription model [4,5]. Microservice-based development is in its infancy, but marketplaces for vendors ofering microservices could start to emerge as the paradigm gains further momentum [5]. Because these are digital products, generally the services purchased outright are not returnable, while subscription contracts can be terminated for a fee.

While the service-based paradigm has clear advantages, end users face several challenges in building applications using business services. The service selection process involves a search process where requirements are matched against the functionality of a suite of services. Some end users may lack full understanding of their requirements,<sup>1</sup> which constrains their ability to select the services needed [6]. The task of finding the services matching requirements requires specialized knowledge—end user's knowledge of re quirements and functionality of available services—not just mere general competence. Research has acknowledged this distinction between sophis ticated and naive analysts, including end users (e.g., Berry [7]), and as a result, their capacity to find the matching services (e.g., Vitharana [8]).

Furthermore, the complexity of the requirements is shown to inhibit the end users’ ability to efectively engage in the requirement analysis task [9,6]. It is easy to fathom why requirement complexity could further complicate the service selection process, although there is little research examining this cause-efect relationship in the context of service-based software development. Consumer research postulates that decision makers knowledge of the product or service characteristics impacts their ability to select those that meet their needs [10,11]. Likewise, some end users may also have limited knowledge of the functionality of the available services, which further hinders their ability to find the services that match their requirements. Naive end users with limited knowledge of both the requirements of the application and the functionality of available services may select services that do not have the capabilities needed for the application or may rely on a suboptimal solution with duplicate service functionality, thereby greatly increasing the cost of software development.

While challenges are acknowledged, research to date has not fully examined two key antecedents of the end user's performance in business service-based application development: (1) end user's knowledge of requirements and functionality of available services and (2) the complexity of the requirements. In this article, we address this gap in our understanding of service-based development. We provide a con ceptual framework for the choice problem faced by the decision maker and develop a set of hypotheses on the end user's sophistication and requirement complexity, and their impact on outcome performance—the ability to avoid duplication and select the appropriate services.

Our research design is twofold. First, we develop a mathematical mode to conceptualize the end users’ service selection process. In this model, we consider an end user selecting services one at a time until she is confident that the selected services fulfill the functionality needed for the application. This process proceeds in stages, where the end user selects a service, reviews it, and decides whether to stop or continue the search for additional ser vices. Second, we conduct an empirical study to test the hypotheses.

Our research makes several contributions. We contribute to theory by conceptualizing how the aforementioned antecedents impact end users’ ability to build service-based applications. Our conceptualizing ofers insights into the impacts of end users’ sophistication/naivety and requirement complexity on service selection. We also present a simple metric developed for assessing end users’ naivety/sophistication (termed NAISOP) based on both perceptual and objective measures. Overall, this work provides one of the first attempts to both theoretically and empirically examine end users’ performance with regard to service duplication. For the management focused on profit maximization, knowledge of the end user's sophistication/naivety allows there to be diferent pricing strategies: (1) a pure component strategy, (2) a pure bundling strategy, or (3) a mixed bundling strategy.

## 2. Literature review

End users’ lack of knowledge of requirements hinders their ability to develop systems that meet their needs [12]. Unlike conventional software development, the service-based paradigm relies on building applications by assembling a suite of existing business services that match requirements [8]. Hence, end users’ ability to select the required business services that are typically stored in a large repository depends on their understanding of their needs. End users’ inability to fully grasp the requirements could also lead to unnecessary duplication of service functionality and, as a result, increase software development costs.

Brucks [13] found that understanding of the product class char acteristics facilitates information search behavior. Hence, similarly to the scenario of a general consumer searching for a specific product, the end users’ ability to select the required business services also depends on their understanding of the characteristics or features of the business services considered to fulfill those needs [10]. Service repositories use various service characteristics and features to catalog services. For ex ample, Vitharana et al. [14,15] introduced a cataloging scheme using characteristics such as rules applicable to services to catalog them in the repository so that end users searching for services that match their requirements can find them on the basis of the rule facet. Therefore, understanding of product characteristics such as rules applicable to services being considered plays a pivotal role in this search exercise.

The two aforementioned knowledge aspects—understanding of both end users’ needs and the characteristics or features of the business services considered to fulfill those needs—manifest themselves in end users’ sophistication of the task at hand; that is, finding business services that match requirements. In decision-making scenarios such as service-based development, those who have diminished capacity with regard to these two knowledge aspects can be called naive consumers, a term used by scholars such as Dean [16]. Irrespective of the end users sophistication or naivety, the complexity of the requirements also im pacts the search for business services matching requirements [12,6].

In the build-by-assembly business services paradigm, the end users performance corresponds to their ability to select the services that fulfill their requirements [14]. In many cases involving large repositories, end users could find multiple sets of business services that might satisfy the given requirement [14,15]. Because these services have diferent prices, rational end users strive to identify the suite of business services that is most cost-efective. However, as their sophistication in terms of knowledge of requirements and characteristics or features of the business services considered is bound to difer, some end users are likely to consider duplicate solutions; that is, select a suite of services with characteristics and features over and beyond those required to satisfy their requirements. Selecting duplicate business services would increase the cost of developing service-based software systems.

The sophistication level of customers also impacts the vendor's pricing strategy. Services, and more generally any products, can be ofered individually or as a bundle, where two or more services are ofered as a package, typically at a discounted price. The vendor must choose from three “bundling” strategies: pure bundling, where services are ofered as a bundle only; pure components, where no bundle is ofered; and mixed bundling, where the customer can buy services either individually or as a bundle [17]. For a less sophisticated end user, a bundle of services makes it less likely that she would miss something important. Thus, the end user gains from bundling because of reduced search and transaction costs [18,19]. In contrast, a sophisticated end user can easily discern which services she needs and would prefer to buy services individually. Vendors could gain from bundling because it can potentially generate greater profits through price discrimination and demand expansion [20–24]. The choice of bundling strategy depends on the relative sizes of naive and sophisticated end users, and a pure bundling strategy is more attractive if end users largely lack sophistication [11].

## 3. Conceptual framework and hypotheses

In the present study, we wish to examine how an end user's ability to select appropriate business services for an application depends on the knowledge of her requirements and the characteristics and features of available services (i.e., level of sophistication), and the complexity of the requirements. To develop hypotheses, we draw from research in two distinct disciplines: consumer psychology and information systems. In consumer psychology, Brucks [13] examined how a consumer's knowledge of a product category and the complexity of the choice task afect the consumer's search behavior, and found that a more knowledgeable (i.e., sophisticated) consumer seeks less information about inappropriate alternatives, particularly when the task is complex. Sujan [25] found that a more knowledgeable (sophisticated) consumer has greater ability to match a given problem to an appropriate category, thus facilitating the search for a solution. Both findings suggest that a more sophisticated customer will be able to search over alternative products more eficiently and make fewer mistakes. Alba and Hutchinson [10] postulated that a consumer with greater experience is better able to isolate information relevant to a given task. Summarizing, we conclude that a more sophisticated end user should be less likely to select a business service not relevant to a given requirement and more likely to recognize a service that meets the requirements of a specific application.

From an information systems point of view, the challenge faced by the end user is to map the problem space as represented by the requirements to the solution space as represented by the suite of available business services [8]. The end users’ sophistication plays a significant role in their ability to map the problem space to the solution space [26,8]. A sophisticated end user can be expected to have greater understanding of her needs and therefore the problem space than a naive end user. Likewise, a sophisticated end user is more likely to be aware of the characteristics or features ofered by those business services that are being considered (i.e., solution space) visà-vis a naive end user. Ko et al. [27] reported that in a software maintenance exercise developers search for cues in the code to determine which specific code segment needs to be changed. We could easily draw an analogy between the scenario considered in this article and software maintenance, where requirements (i.e., problem space) are mapped against system code (i.e., solution space). It can be expected that sophisticated end users who are better versed in their own requirements as well as the characteristics and features of available business services will more readily identify the right cues, which would help them more precisely map the problem space to the solution space. Such cues could include a functional description of the business services, applicable rules, expected inputs and outputs, and exception conditions [26,6]. Therefore, the challenges faced by more naive end users in mapping the problem space to the solution space would lead to a larger number of duplications and incorrect picks when compared with more sophisticated end users.

The end user faces an added challenge when requirements are more complex. Mapping of requirements (i.e., problem space) to the business services (i.e., solution space) that match them is hindered by the complex nature of needs and wants. Requirement complexity could manifest itself in the form of complex decision rules, exceptions, and interrelationships between subrequirements [28,6]. Again, analyzability of software code during a maintenance exercise is germane to the scenario considered in this article. Shaft and Vessey [29] demonstrated that software maintainers’ performance has a positive relationship with the cognitive fit between their mental representation of the code and the new requirement. When requirements are relatively simple, we could expect end users to more readily realize a cognitive fit between requirements and the relevant business ser vices considered to fulfill them. In contrast, complex requirements could cloud end users’ ability to form more accurate mental models in mapping requirements with available business services. This is likely to result in a larger number of duplications and incorrect picks when compared with a scenario involving simpler requirements.

There is a clear convergence between consumer psychology and information systems research streams with respect to the conceptualization of the decision scenario under consideration. The decision makers, regardless of whether they are general consumers or software end users, difer in their sophistication in terms of knowledge of the need or requirement and knowledge of product or business services aforded to them. The two research streams converge to postulate that this variation in sophistication together with the complexity of their own need in the case of a consumer, or the complexity of the requirement in the case of an end user, impacts de cision makers’ outcome performance—the ability to avoid duplication and select the appropriate services. Hence, we summarize the above as the following four hypotheses regarding how an end user picks services to fulfill a given requirement:

Hypothesis 1. If the level of requirement complexity is the same, a more naive end user will have a larger number of duplications than a less naive end user.

Hypothesis 2. If the level of end user sophistication is the same, the number of duplications will increase with requirement complexity.

Hypothesis 3. If the level of requirement complexity is the same, a more naive end user will have a larger number of incorrect picks than a less naive end user.

Hypothesis 4. If the level of end user sophistication is the same, the number of incorrect picks will increase with requirement complexity.

In Appendix A, we present a mathematical model based on search behavior and stopping time that also leads to the same hypotheses. In this model, we consider an end user who is selecting services with corresponding functionality. We assume that there is a large number of services and the end user selects services one at a time until she has chosen all the services needed for the application. This process proceeds in stages, where the end user selects a service, reviews it, and decides whether to stop or continue the search for additional services (see Fig. 1 for an illustration).

## 4. Empirical study

## 4.1. Experimental task

The task was to select the “most cost-efective business service or services” needed to complete five sets of requirements. Appendix B provides details of the experimental task. The associated dataset contained information about universities in the United States and tasks related to various aspects of analyzing this dataset. The dataset and the corresponding tasks<sup>2</sup> were selected because of the participants’ general familiarity with the do main. Before the tasks were presented, descriptions of six business services were presented (see Appendix C). Following Brucks [13], we present the end user as the decision maker with hypothetical brands to avoid an internal search of known business services within the decision maker's memory. Thus, the decision maker must process the information presented about the business service alternatives to make an appropriate selection. At any time during the subsequent problem-solving task, the participants had the opportunity to review these business services. The dataset was presented in a browser window in a table format (with scrollable rows and columns) without any reference to Microsoft Excel.

## 4.2. Instrument development

We developed an instrument to measure the participants’ knowledge of data analysis (see Appendix D), which was subsequently used to develop an aggregated measure of their NAISOP (knowledge of requirements and functionality of available services).

## 4.3. Experimental design and protocol

We used a controlled experiment to test the hypotheses. An experiment website was built to conduct the study, including the administration of the survey questions. Every alternate participant was assigned the simple task or the complex task. Before the main study was conducted, a pilot study was performed with 16 students. The objectives were to test the website, the survey instrument, and the overall flow of the experiment. On the basis of the results of the pilot study, a few minor changes to the instrument and the website were made. For the main experiment, both students and profes sionals were included as participants to diversify the level of sophistication. Hence, students from a university in northeast United States and profes sionals (from a panel maintained by Qualtrics) were recruited. The data collection was performed over an 8-month period. For their participation, a student and a professional received \$5 and \$26, respectively.

Descriptive statistics.  
![](/api/attachments/9R6YDYPC/fulltext/images/ab6aaf0572bf3aedc2ca29de0e84915f36cca88d1bf832eed8da0eaa13d5b87e.jpg)  
Fig. 1. Business services search and stop process.

## 4.4. Data collection

At the start of the experiment, all participants answered online survey questions about their personal profiles (demographics) and knowledge of data analysis, number of statistics courses taken, and experience with Excel (number of months). A total of 379 participants completed the study.

## 4.5. Analysis

Participants’ nativity/sophistication (NAISOP) was assessed using both a perceptual measure and an objective measure. The perceptual aspect was assessed using their perceived knowledge of data analysis described earlier. The objective aspect was assessed using the number of statistics courses they had taken and the number of months of Microsoft Excel experience. While other metrics such as personal IQ or college GPA could be used to distinguish between naive and sophisticated participants, we chose this combination of perceived knowledge of data analysis and number of statistics courses and Excel experience because the tasks are statistics related and the business services ofer the statistics-related functionality of common spreadsheet software such as Microsoft Excel (e.g., charts, pivot tables, and regression analysis). Cronbach alpha for the aggregated NAISOP construct was 0.90, demonstrating suficient reliability. Appendix E provides details of the measurement model for NAISOP.

To further establish reliability and validity of the aggregated NAISOP construct, we examined its correlation with two related measures. There were strong correlations between NAISOP and the number of data analysis classes (correlation coeficient 0.514, $p < 0 . 0 0 1 )$ and between NAISOP and months of data analysis experience (correlation coeficient $0 . 6 1 1 , p < 0 . 0 0 1 \AA$ ). Hence, NAISOP is a suitable measure to distinguish between naive and sophisticated participants.

In coding dependent variables, we considered each task separately such that duplication for one task was scored as 0 (no duplication) or 1 (duplication). The same scoring scheme was used for the selection of correct business services for each task. Hence, given that there were five tasks, for duplication and correct dependent variables, the possible minimum and maximum values were 0 and $^ { 5 , }$ respectively. Scoring each task with 0/1 and then adding the scores for the five tasks aforded an efective way to deal with potential outliers. Table 1 presents relevant descriptive statistics.

The regression models used to test the hypotheses are as follows:

Duplicates = $: \beta _ { 0 } + \beta _ { 1 } \times \mathrm { N A I S O P } + \beta _ { 2 }$ ×  Complexity $+ \ \in _ { \mathrm { 1 : } }$

$$
\text { Correct } = \gamma_ {0} + \gamma_ {1} \text { NAISOP } + \gamma_ {2} \times \text { Complexity } + \epsilon_ {2}.
$$

Although data were collected from students in many disciplines and professionals across many firms, it is possible that the error terms are correlated because of a common efect. Seemingly unrelated regression estimation (SURE) corrects for correlated error terms [30,31]. In SURE, a linear regression model consisting of a set of regression equations is generated. Each regression equation has its own dependent variable and a set of exogenous variables. The equations appear to be unrelated although they are related through the correlation in the errors. It is argued that joint estimation of the set of equations using generalized least squares produces more eficient estimates than individual ordinary least squares [32,33]. Hence, we tested our hypotheses using SURE models [34]. The results obtained with Stata version 15 are shown in Table 2.

All hypotheses were supported.

• End users’ sophistication impacted their ability to avoid duplication in selecting only those business services required to accomplish the given task $( t = - 3 . 4 5 , p < 0 . 0 1 )$ , thereby supporting Hypothesis 1.

Task complexity impacted end users’ ability to avoid duplication in selecting only those business services required to accomplish the given task $( t = 1 0 . 4 0 , p < 0 . 0 0 1 )$ , thereby supporting Hypothesis 2.

<table><tr><td>Variable</td><td>Mean</td></tr><tr><td>Age</td><td>28 years</td></tr><tr><td>Female</td><td>40%</td></tr><tr><td>No. of statistics courses</td><td>4.15</td></tr><tr><td>Excel experience</td><td>33.9 months</td></tr><tr><td rowspan="3">Status</td><td>Undergraduate 43%</td></tr><tr><td>Graduate 32%</td></tr><tr><td>Professional 24%</td></tr><tr><td>Duplicates</td><td></td></tr><tr><td>0</td><td>6.60%</td></tr><tr><td>1</td><td>12.14%</td></tr><tr><td>2</td><td>15.57%</td></tr><tr><td>3</td><td>17.41%</td></tr><tr><td>4</td><td>17.15%</td></tr><tr><td>5</td><td>31.13%</td></tr><tr><td>Correct</td><td></td></tr><tr><td>0</td><td>14.78%</td></tr><tr><td>1</td><td>10.29%</td></tr><tr><td>2</td><td>11.61%</td></tr><tr><td>3</td><td>13.19%</td></tr><tr><td>4</td><td>22.16%</td></tr><tr><td>5</td><td>27.97%</td></tr></table>

Table 2  
Seemingly unrelated regression estimation analysis.

<table><tr><td>Variable</td><td>Coefficient</td><td>Standard error</td><td>t</td><td>p</td><td> $\chi^2$ </td><td> $R^2$ </td></tr><tr><td colspan="7">Dependent variable: duplicates</td></tr><tr><td>Intercept ( $\alpha_0$ )</td><td>3.157</td><td>0.227</td><td>13.88</td><td>&lt;0.001</td><td></td><td></td></tr><tr><td>NAISOP ( $\alpha_1$ )</td><td>-0.002</td><td>0.001</td><td>-3.45</td><td>&lt;0.01</td><td></td><td></td></tr><tr><td>Complexity ( $\alpha_2$ )</td><td>1.507</td><td>0.145</td><td>10.40</td><td>&lt;0.001</td><td></td><td></td></tr><tr><td>Model</td><td></td><td></td><td></td><td>&lt;0.001</td><td>118.54</td><td>0.24</td></tr><tr><td colspan="7">Dependent variable: correct</td></tr><tr><td>Intercept ( $\beta_0$ )</td><td>3.551</td><td>0.235</td><td>15.13</td><td>&lt;0.001</td><td></td><td></td></tr><tr><td>NAISOP ( $\beta_1$ )</td><td>0.002</td><td>0.001</td><td>2.29</td><td>&lt;0.05</td><td></td><td></td></tr><tr><td>Complexity ( $\beta_2$ )</td><td>-2.055</td><td>0.150</td><td>-13.73</td><td>&lt;0.001</td><td></td><td></td></tr><tr><td>Model</td><td></td><td></td><td></td><td>&lt;0.001</td><td>192.53</td><td>0.34</td></tr></table>

n = 379.

End users’ sophistication also impacted their ability to select the business services with the functionality needed to accomplish the given task $( t = 2 . 2 9 , p < 0 . 0 5 )$ , thereby establishing support for Hypothesis 3.

• Task complexity impacted end users’ ability to select the busines services with the functionality needed to accomplish the given task $( t = - 1 3 . 7 3 , p < 0 . 0 0 1 )$ , thereby establishing support for Hypothesi 4.

Furthermore, a simple t test revealed that the end users’ status (professional vs. student) had no impact on their ability to avoid duplication and to select the services needed although, as shown in Table 3, the groups difered significantly on demographics. This counterintuitive revelation is interesting because professionals who have greater sophistication were expected to perform better than students. The examination of R<sup>2</sup> values showed explanatory power for avoiding duplication and selecting correct business services at 24% and 34%, respectively.

## 5. Discussion

We theorized that the end users’ sophistication (or lack thereof) and task complexity impact their ability to avoid duplication and select the business services with the functionality needed. Our empirical results support this premise. Furthermore, we highlight the significance of perceptual and ob jective aspects of the decision makers’ knowledge in forming the aggregate measure for their sophistication. In the marketing literature, only consumers’ knowledge of available product choices is typically considered as a decision parameter impacting their purchase behavior [10,25]. This approach implicitly assumes that the customer knows about her needs, and it is not necessary to consider knowledge of the needs themselves explicitly. In contrast, the end user examined in this article requires knowledge of both her own needs and business services that can fulfill those needs. Thus. the end users’ knowledge of the requirement considered in this article (i.e., selection of business services needed to complete the requirement) is unique in that it needs to include both their knowledge of the requirements and their knowledge of the available choices. Therefore, in developing measures for the decision makers’ sophistication with respect to the task at hand, we need to include both dimensions of knowledge.

Table 3  
Demographics among undergraduates, graduate students, and professionals.

<table><tr><td></td><td>Age (years)</td><td>Data analysis (0–100 scale)</td><td>Statistics classes</td><td>Data analysis classes</td><td>Excel experience (months)</td></tr><tr><td>Undergraduate</td><td>22</td><td>58</td><td>2</td><td>1</td><td>10</td></tr><tr><td>Graduate</td><td>29</td><td>67</td><td>4</td><td>3</td><td>28</td></tr><tr><td>Professional</td><td>38</td><td>86</td><td>9</td><td>7</td><td>86</td></tr></table>

## 5.1. Theoretical contribution

This study makes several theoretical contributions. We provide a conceptual framework for the choice problem faced by an end user in the selection of business services needed to fulfill a given requirement. This conceptualization ofers the basis for the key premise in the article that end users’ sophistication impacts their performance—the ability avoid duplication and select the services needed. We conceptualized the need to consider both perceptual and objective aspects of end users knowledge in developing a measure for sophistication as they represent two distinct dimensions of the decision makers’ knowledge. The ag gregated NAISOP measure is pivotal in capturing end users’ sophistication in terms of both their knowledge of available business services and their knowledge of the requirements.

## 5.2. Managerial implications

Our work has several implications for managers. End users’ performance depends both on the knowledge of their requirements and their knowledge of the functionality of available business services, not on merely one alone. For a profit-maximizing vendor, the realization of disparate end user sophistication allows the vendor to have diferent pricing strategies, such as a pure component strategy, a pure bundling strategy, or a mixed bundling strategy. Sophisticated end users may be more inclined to purchase in dividual business services because of their superior knowledge of available choices and the task itself. On the other hand, naive end users may be enticed to purchase bundles to help them mitigate the risk of leaving out any crucial functionality needed for the task at hand.

In the present study, we found that professionals do not perform sig nificantly better than students in identifying the correct services for a given task. Also, both students and professionals tend to equally duplicate services. These findings suggest that most business customers would prefer bundles, which are more likely to include items that fulfill their needs. Unless there are high royalty costs involved, the marginal costs for the marketer are low. The combination of low marginal cost and the customer's uncertainty about the value of a given service suggests that a pure bundling strategy is optimal for a market such as this [11]. Clearly, this recommendation is based on our examination of a specific domain, and further research is needed to determine if the results are similar in other domains.

## 5.3. Limitations and directions for future research

We considered two key variables—end users’ sophistication and requirement complexity—that could impact end users’ ability to avoid duplication and select the business services needed. We tried to mitigate threats to internal validity by putting necessary controls in place during the experiment. For example, participants were randomly assigned to simple and complex tasks on an even/odd basis. The website ofered a control setting that included solicitation of demographic information, the instrument, the task, and the dataset. However, other variables, such as knowledge of the domain, in our case university admissions, could also impact their performance. Representational methods for conventional reusable assets are shown to impact developers’ understanding of those assets [35]. Likewise, the efectiveness of the business service descriptions (e.g., cataloging scheme implemented in the service repository) could also impact the end users’ ability to select the services and avoid duplication. Research has also shown that an improvement in media richness reduces the cost of information search [36], thereby enhancing the end user's ability to select the services needed. Future research needs to account for other possible variables that could explain the variation in outcome performance.

One threat to external validity and generalizability stems from the selection of the participant pool. We tried to mitigate this threat by selecting a participant pool with a diverse background (e.g., students in accounting, finance, etc., and professionals across multiple organizations). Moreover, we used a participant pool with a broad background in terms of the number of statistics courses taken (range 0–20, mean 4.1, standard deviation 5.0) and months of Excel experience (range 0–100 months, mean 33.9 months, and standard deviation 38.5 months).<sup>3</sup> Nonetheless, future research needs to include alternative domains and corresponding participant pools.

## Conflict of interest

This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

## Acknowledgments

The authors thank Information & Management editorial and review team for guidance through the review process. This research was funded by grants from the Robert H. Brethen Operations Management Institute and the Earl V. Snyder Innovation Management Center at the Whitman School of Management, Syracuse University.

## Appendix A. A model and an empirical test<sup>4</sup>

In this appendix, we provide a simple model based on search behavior and stopping time to derive the hypotheses examined in this article. We consider a decision maker who is selecting services that can fulfill a predetermined set of functions. To simplify the model, we assume that there is a large pool of services, and the decision maker selects services one at a time until she is confident she has picked all the services needed for the given application. This process may proceed in stages, where the decision maker selects some services, reviews them, and decides whether to stop o continue the search. Each time the decision maker picks a service, three cases are possible:

1. The decision maker picks a service that is not relevant to the given application. We call this event an incorrect pick, and denote the probability this happens by $q _ { 1 } ^ { \phantom { * } }$ . We assume that if an incorrect pick occurs, the decision maker eventually recognizes that fact and continues the search.

2. The decision maker picks a service that is relevant to the given application but, after picking, she is not confident it is relevant. As the decision maker stops her search only when she is confident she has picked all services she needs, the event where she picks a relevant service but is not confident it is relevant leads to her picking at least another item that performs the same function. Thus, the item originally picked becomes a duplicate pick. We denote the probability of this event by $q _ { 2 } .$

3. The decision maker picks a service that is relevant, and is also confident that it is relevant. The probability this happens is $p = 1 - q _ { 1 } - q _ { 2 }$ Clearly, the last item selected must meet this criterion.

If the decision maker always picks the correct services and is confident in her selection, we will have $p = 1$ and $q _ { 1 } = q _ { 2 } = 0$ . Otherwise, $q _ { 1 }$ or $q _ { 2 }$ should exceed zero. The related literature in consumer psychology [10,13,25] suggests that $q _ { 1 }$ should be higher for less knowledgeable decision makers. By the same logic, we posit that $q _ { 2 }$ should also be higher for less knowledgeable decision makers and that. for the same level of decision maker knowledge, $q _ { 1 }$ and $q _ { 2 }$ should be higher for more complex requirements.

Formally, we assume that the decision maker is not confident with any incorrect pick, and she stops the search after she has picked r services she is confident are useful for the given requirement. As even simple requirements may involve many functions, we assume that r is the same for all cases, simple or complex. Consider first the dichotomy where, after picking, the decision maker is either confident or not confident that the service is useful for the application. The probability that she stops her search after picking n services is the same as the probability that she picks exactly n services to have r services, including the last service picked, she is confident are useful. The probability of this event is given by the negative binomia probability distribution; that ${ \mathrm { i } } s ,$

$$
P (n) = \binom {n - 1} {r - 1} p ^ {r} (1 - p) ^ {n - r}.\tag{A.1}
$$

Kraft and Lee [37] used this distribution to model search lengths for an information retrieval system. The expected search length is given by

$$
E (n) = \frac {r}{p}\tag{A.2}
$$

(see, $\mathbf { e . g . , }$ , Ross [38], page 187).

Expected numbers of incorrect and duplicate picks. Suppose, after picking n services, the decision maker is confident she has picked r services that are useful and stops her search. Thus, she also picked ( )n r services that are either incorrect or duplicate picks. For each of these $( n - r )$ picks, the probability that it is incorrect is $\begin{array} { r } { \frac { q _ { 1 } } { q _ { 1 } + q _ { 2 } } = \frac { q _ { 1 } } { 1 - p } ; } \end{array}$ , and the probability that it is a duplicate is $\frac { q _ { 2 } } { 1 - p }$ . Hence, if the search stops after n steps, the expected numbers of incorrect and duplicate picks are $\frac { q _ { 1 } } { 1 - p } ( n - r )$ and $\frac { q _ { 2 } } { 1 - p } ( n - r )$ , respectively. Since the probability of stopping after n steps is $P ( n )$ , the expected number of incorrect picks is given by

$$
\sum_ {n = r} ^ {\infty} \frac {q _ {1}}{1 - p} (n - r) P (n) = \frac {q _ {1}}{1 - p} [ E (n) - r ] = \frac {q _ {1}}{1 - p} (\frac {r}{p} - r) = \frac {q _ {1} r}{p} = \frac {q _ {1} r}{1 - q _ {1} - q _ {2}}.\tag{A.3}
$$

Similarly, the expected number of duplicates is $\frac { q _ { 2 } r } { 1 - q _ { 1 } - q _ { 2 } }$

Since we posit that $q _ { 1 }$ increases if the requirement is more complex or the decision maker is more naive, the expected number of incorrect picks should also increase. We have a similar result for duplicate picks. Summarizing, we have the following hypotheses:

Hypothesis 1. If the level of requirement complexity is the same, a more naive end user will have a larger number of duplications than a less naive developer.

Hypothesis 2. If the level of end user sophistication is the same, the number of duplications will increase with requirement complexity.

Hypothesis 3. If the level of requirement complexity is the same, a more naive end user will have a larger number of incorrect picks than a less naive end user.

Hypothesis 4. If the level of end user sophistication is the same, the number of duplications is larger for greater requirement complexity.

Distributions of numbers of incorrect picks and duplications. We now show that under our assumptions, the numbers of incorrect and duplicate picks also follow negative binomial distributions. Let y and z denote the numbers of incorrect picks and duplications when a given search ends with r correct picks. Thus, for the first $( r - 1 + y + z )$ picks, there are $( r - 1 )$ correct picks, y incorrect picks, and z duplicate picks, and pick number $( r + y + z )$ (last pick) is a correct pick. As each pick is independent, the probability of this occurring is given by

$$
\left[ \frac {(r - 1 + y + z) !}{(r - 1) ! y ! z !} p ^ {r - 1} q _ {1} ^ {y} q _ {2} ^ {z} \right] \times p = \frac {(r - 1 + y + z) !}{(r - 1) ! y ! z !} p ^ {r} q _ {1} ^ {y} q _ {2} ^ {z}.\tag{A.4}
$$

The term in brackets in the above expression is the multinomial probability of observing $( r - 1 )$ correct picks, y incorrect picks, and z duplicate picks among the first $( r - 1 + y + z )$ picks ([38], page 267).

Hence, the probability that a given value y of incorrect picks occurs is

$$
\begin{array}{r l} \phi (y) & = \sum_ {z = 0} ^ {\infty} \frac {(r - 1 + y + z) !}{(r - 1) ! y ! z !} p ^ {r} q _ {1} ^ {y} q _ {2} ^ {z} \\ & = \frac {p ^ {r} q _ {1} ^ {y}}{(r - 1) ! y !} \sum_ {z = 0} ^ {\infty} \frac {(r - 1 + y + z) !}{z !} q _ {2} ^ {z} \\ & = \frac {(r - 1 + y) !}{(r - 1) ! y !} p ^ {r} q _ {1} ^ {y} (1 - q _ {2}) ^ {- (r - 1 + y)} \sum_ {z = 0} ^ {\infty} \frac {(r - 1 + y + z) !}{z ! (r - 1 + y) !} q _ {2} ^ {z} (1 - q _ {2}) ^ {r - 1 + y} \\ & = \frac {(r - 1 + y) !}{(r - 1) ! y !} p ^ {r} q _ {1} ^ {y} (1 - q _ {2}) ^ {- (r + y)} \sum_ {z = 0} ^ {\infty} [ \frac {(r - 1 + y + z) !}{z ! (r - 1 + y) !} q _ {2} ^ {z} (1 - q _ {2}) ^ {r - 1 + y} ] \times (1 - q _ {2}) \\ & = \frac {(r - 1 + y) !}{(r - 1) ! y !} p ^ {r} q _ {1} ^ {y} (1 - q _ {2}) ^ {- (r + y)} \times \sum_ {z = 0} ^ {\infty} \psi (z), \end{array}
$$

where $\psi ( z )$ is the probability, for a negative binomial process with probability of success $( 1 - q _ { 2 } )$ that stops after $( r + y )$ cases of success, that there are z cases of failure before the process stops. Thus,

$$
\sum_ {z = 0} ^ {\infty} \psi (z) = 1;
$$

that is,

$$
\phi (y) = \frac {(r - 1 + y) !}{(r - 1) ! y !} p ^ {r} q _ {1} ^ {y} (1 - q _ {2}) ^ {- (r + y)} = \frac {(r - 1 + y) !}{(r - 1) ! y !} p _ {1} ^ {r} p _ {2} ^ {y},\tag{A.5}
$$

where $\begin{array} { r } { p _ { 1 } = \frac { p } { 1 - q _ { 2 } } } \end{array}$ and $\begin{array} { r } { p _ { 2 } = \frac { q _ { 1 } } { 1 - q _ { 2 } } . } \end{array}$

Since $p _ { 1 } + p _ { 2 } = 1 ,$ it follows from (A5) that $( y + r )$ is the length of a negative binomial process that stops after r cases of success, where the probability of success in each trial is $p _ { 1 }$ . Hence, the number of incorrect picks y is generated by a negative binomial process. Similarly, the number of duplicate picks z is also generated by a negative binomial process.

Empirical test. We now present results obtained with negative binomial regression with dependent variables Duplicates and Correct. The results obtained with the procedure glm.nb with the MASS library in R version 3.3.1 are presented in Table 4.

Table 4  
Results of negative binomial regression.

<table><tr><td>Variable</td><td>Estimate</td><td>Standard error</td><td>z</td><td>p</td><td> $\chi^2$ </td></tr><tr><td colspan="6">Dependent variable: duplicates</td></tr><tr><td>Intercept ( $\alpha_0$ )</td><td>1.1145</td><td>0.09016</td><td>12.36</td><td>&lt;2 × 10-16</td><td></td></tr><tr><td>NAISOP ( $\alpha_1$ )</td><td>-0.00077</td><td>0.00028</td><td>-2.748</td><td>0.006</td><td></td></tr><tr><td>Complexity ( $\alpha_2$ )</td><td>0.4798</td><td>0.05900</td><td>8.13</td><td>4.2 × 10-16</td><td></td></tr><tr><td>Model</td><td></td><td></td><td></td><td>&lt;0.001</td><td>74.36 (df = 2)</td></tr><tr><td colspan="6">Dependent variable: correct</td></tr><tr><td>Intercept ( $\beta_0$ )</td><td>1.2353</td><td>0.09216</td><td>13.40</td><td>&lt;2 × 10-16</td><td></td></tr><tr><td>NAISOP ( $\beta_1$ )</td><td>0.00056</td><td>0.00029</td><td>1.892</td><td>0.0585</td><td></td></tr><tr><td>Complexity ( $\beta_2$ )</td><td>-0.7111</td><td>0.06309</td><td>-11.27</td><td>2 × 10-16</td><td></td></tr><tr><td>Model</td><td></td><td></td><td></td><td>&lt;0.001</td><td>138.20 (df = 2)</td></tr></table>

Comparison shows that these results are consistent with the results presented in Table 2 and support all four hypotheses.

## Appendix B. Description of task

You are given a dataset that has information about all the universities in the United States. Your supervisor has asked you to investigate various aspects of the data to gain greater insights. Once the analysis is complete, you are required to give a presentation to your supervisor by includin charts illustrating your findings.

Select the most cost-efective business service or services needed to complete each of the following tasks, and in one or two sentences briefly describe why each service is required

Important note: You are asked to select only the service or services needed to complete the given task and give the subsequent presentation to your supervisor. You are not asked to actually do the data analysis and give the presentation.

## Simple task

Task 1: Find the average and standard deviation of the number of applicants, admissions, and enrolled students for private schools. Find the average and standard deviation of the number of applicants, admissions, and enrolled students for public schools. How do these numbers compare? (Remember, after you complete the task, your supervisor wants you to present your findings.)

Which service or services do you need to complete this task? (Check all that apply.)

Task 2: Find the average and standard deviation of the number of applicants, admissions, and enrolled students in each geographical region. How do these numbers compare? (Remember, after you complete the task, your supervisor wants you to present your findings.)

Which service or services do you need to complete this task? (Check all that apply.)

Task 3: Find the average and standard deviation of the admissions-to-applicants ratio, and the enrolled students to admissions ratio for each private/public and geographical region subset. (For example, private schools in the northeast is a subset.) How do these numbers compare? (Remember, after you complete the task, your supervisor wants you to present your findings.)

Which service or services do you need to complete this task? (Check all that apply.)

Task 4: Find the average SAT Math 75th percentile score and divide the data into two groups: (1) at or above this average; (2) below this average. Compare these two groups in terms of the admissions-to-applicants ratio. (Remember, after you complete the task, your supervisor wants you to present your findings.)

Which service or services do you need to complete this task? (Check all that apply.)

Task 5: In New York State, identify schools with the ten highest tuition rates. For these ten schools, find the average, maximum, and minimum admission rates (Remember, after you complete the task, your supervisor wants you to present your findings.)

Which service or services do you need to complete this task? (Check all that apply.)

## Complex task

Task 1: How does the undergraduate graduation rate (within 4 years) depend on the following three features of a school: size of the school, tuition rate, and SAT Math 75th percentile score of entrants? Your model should include the three factors (size, tuition rate, SAT Math 75th percentile score) simultaneously. (Remember, after you complete the task, your supervisor wants you to present your findings).

Which service or services do you need to complete this task? (Check all that apply.)

Task 2: Beyond the three factors listed in task 1 above, other factors may also afect the graduation rate. Overall (considering all factors simultaneously), what are the three most important factors (features/characteristics of the school) that determine the undergraduate graduation rate? (Remember, after you complete the task, your supervisor wants you to present your findings).

Which service or services do you need to complete this task? (Check all that apply.)

Task 3: How does tuition depend on the following three factors considered at the same time: geographical area, the nature of the school (public or private), and selectivity (defined as total number of admissions divided by total number of applicants)? (Remember, after you complete the task, your supervisor wants you to present your findings).

Which service or services do you need to complete this task? (Check all that apply.)

Task 4: How does the percentage of freshmen receiving financial aid depend on the type of school (private vs. public), tuition rate, and per centage of students who graduate? (Remember, after you complete the task, your supervisor wants you to present your findings).

Which service or services do you need to complete this task? (Check all that apply.)

Task 5: How does the percentage of female students depend on geographical location? Statistically test if the percentage of female students is the same for all geographical locations. (Remember, after you complete the task, your supervisor wants you to present your findings).

Which service or services do you need to complete this task? (Check all that apply.)

## Appendix C. Business services

Core Studio (price \$200). This service can be used to enter data into a spreadsheet and save them in a file. This file can then be opened again. It ofers the ability to sort, filter, and conditionally format data. It ofers the ability to make logical comparisons between two values. The features include the following: (1) create a new (blank) spreadsheet file, (2) enter data, (3) save file, (4) open an existing file, (5) sort data, (6) filter data, (7) conditionally format data, and (8) make logical comparisons between two values

Chart Expert (price \$300). This service creates charts such as line, pie, column, bar, area, scatter, and clustered column charts in a variety of colors. In addition, it creates geographical maps. It ofers the ability to label axes and insert a title for the chart. The features include the following: (1) create a new line, pie, column, bar, area, scatter, or clustered column chart or geographical map, (2) open an existing chart or a geographical map, (3) format charts and maps using colors and number formatting, and (4) format axis labels and chart/map titles

Pivot Professional (price \$400). This service creates pivot tables for summarizing, aggregating, and cross-tabulating data. Subsets of data can be created and formatted to illustrate simple statistics such as means, medians, counts, maximums, and minimums. It has an easy-to-use drag-and-drop capability to visually create new tables for data subsets. It offers the ability to create charts such as line, pie, column, bar, area, scatter, and clustered column charts in a variety of colors. In addition, it creates geographical maps. It ofers the ability to label axes and insert a title for the chart. The features include the following: (1) create a new pivot table, (2) open an existing pivot table, (3) create subsets of larger datasets to summarize, aggregate, and cross-tabulate data, (4) format pivot tables with simple statistics such as means, medians, counts, maximums, and minimums, (5)

filter data in the pivot table, (6) easy-to-use drag-and-drop capability to visually create new tables for data subsets, (7) using data in the pivot table, create a new line, pie, column, bar, area, scatter, or clustered column chart or a geographical map, (8) open an existing chart or a geographical map (9) format charts and maps using colors and number formatting, and (10) format axis labels and chart/map titles.

Text Authority (price \$300). This is a comprehensive service for manipulating text. Text Authority ofers all the text functions users need to work with text in your data. The features include the following: (1) join several texts into a one long text string, (2) segment text strings that are separated by a delimiter (e.g., fruit/plumb), (3) determine the number of characters in a text string, (4) replace characters within a text string (replace “a” with “b”), (5) substitute new text for old text in a text string (changing “le” to “ility” changes “able” to “ability”), (6) remove spaces from text, and (7) convert lowercase to uppercase (and vice versa).

AlphaStatistics (price \$400). This has simple statistical functionality. AlphaStatistics allows users to report basic statistics and conduct simple statistical analysis of their data. This service is ideal for those who need only basic statistical features. The features include the following: (1) calculate minimum, maximum, average, median, mode, standard deviation, and variance and (2) calculate correlation, covariance, moving averages, and confidence intervals.

PinnacleStats (price \$600). This has a comprehensive set of functions to conduct a wide array of statistical analyses. PinnacleStats is your ultimate statistical suite for all your statistical needs. This service is ideal for those who need to conduct advance statistical analyses. The features include the following: (1) calculate minimum, maximum, average, median, mode, standard deviation, and variance, (2) calculate correlation covariance, moving averages, and confidence intervals, (3) ANOVA, (4) multivariate ANOVA, (5) F test, t test, and z test, (6) structural equation modeling, (7) regression, (8) time-series analysis, (9) $\chi ^ { 2 }$ test, (10) discriminant analysis, (11) binary logit, and (12) factor analysis.

## Appendix D. Measurement of knowledge of data analysis

Knowledge of data analysis construct items was measured on a semantic diferential continuous scale from 0 (very low) to 100 (very high). My knowledge of data analysis

Data analysis refers to the process of inspecting, cleaning, transforming, and modeling data with the goal of discovering useful information, suggesting conclusions, and supporting decision-making.

DA1: I characterize my understanding of the various aspects of data analysis as:

DA2: I characterize my understanding of what data analysis involves as:

DA3: I characterize my expertise in data analysis as:

DA4: I characterize my ability to answer questions on data analysis as:

DA5: In general, I characterize my overall knowledge of data analysis as:

## Appendix E. Development of NAISOP measure

This appendix details of the measurement model that uses perceptual data analysis (DA) and objective statistics classes and Excel experience in months (STATEXC) to derive the second-order NAISOP measure (Table E.1),

Table E.1  
Factor loadings for NAISOP.

<table><tr><td></td><td>Loading</td><td>t</td><td>p</td></tr><tr><td colspan="4">1st-order DA</td></tr><tr><td>DA1</td><td>0.954</td><td>159.467</td><td>0.000</td></tr><tr><td>DA2</td><td>0.950</td><td>138.227</td><td>0.000</td></tr><tr><td>DA3</td><td>0.957</td><td>153.884</td><td>0.000</td></tr><tr><td>DA4</td><td>0.968</td><td>215.751</td><td>0.000</td></tr><tr><td>DAGEN</td><td>0.983</td><td>281.129</td><td>0.000</td></tr><tr><td colspan="4">1st-order STATEXC</td></tr><tr><td>STATCLA</td><td>0.657</td><td>12.745</td><td>0.000</td></tr><tr><td>EXCMNTS</td><td>0.744</td><td>16.386</td><td>0.000</td></tr><tr><td colspan="4">2nd-order NAISOP</td></tr><tr><td>STATEXC</td><td>0.669</td><td>15.748</td><td>0.000</td></tr><tr><td>DA</td><td>0.816</td><td>22.688</td><td>0.000</td></tr></table>

## References

[1] S. Daya, N. van Duy, K. Eati, C.M. Ferreira, D. Glozic, V. Gucer, M. Gupta, S. Joshi, V. Lampkin, M. Martins, S. Narain, R. Vennam, Microservices from Theory to Practice: Creating Applications in IBM Bluemix Using the Microservices Approach, IBM Redbooks. 2016.

[2] E. Kessler, Assembling COTS software in a certifiable safety-critical domain, Inf. Syst. J. 18 (3) (2008) 299–324

[3] M.N. Haines, M.A. Rothenberger, How a service-oriented architecture may change the software development process, Commun. ACM 53 (8) (2010) 135–140.

[4] S. Newman, Building Microservices: Designing Fine-Grained Systems, O’Reilly Media, Inc., 2015.

[5] A. Singleton, The economics of microservices, IEEE Cloud Comput. 3 (5) (2016) 16-20.

[6] P. Vitharana. E.M. Zahedi. H.K. Jain. Enhancing analysts' mental models for im: proving requirements elicitation: a two-stage theoretical framework and empirical results, J. Assoc. Inf. Syst. 17 (12) (2016) 1.

[7] D.M. Berry, The importance of ignorance in requirements engineering, J. Syst Softw, 28 (1) (1995) 179–184

[8] P. Vitharana, Risks and challenges of component-based software development, Commun. ACM 46 (8) (2003) 67–72.

[9] G.J. Browne, V. Ramesh. Improving information requirements determination: a

[10] J.W. Alba, J.W. Hutchinson, Dimensions of consumer expertise, J. Consum. Res. 13

[11] A. Basu, P. Vitharana, Impact of customer knowledge heterogeneity on bundling strategy, Market, Sci, 28 (4) (2009) 792–801.

[12] J.W. Moody. J.E. Blanton. P.H. Cheney. A theoretically grounded approach to assist memory recall during information requirements determination, J. Manag. Inf. Syst.

15 (1) (1998) 79–98.

[13] M. Brucks, The efects of product class knowledge on information search behavior, J. Consum. Res. 13 (June) (1985) 1–16.

[14] P. Vitharana, F.M. Zahedi, H. Jain, Design, retrieval, and assembly in component based software development, Commun. ACM 46 (11) (2003) 97–102.

[15] P. Vitharana, F.M. Zahedi, H. Jain, Knowledge-based repository scheme for storing and retrieving business components: a theoretical design and an empirical analysis, IEEE Trans. Softw. Eng. 29 (7) (2003) 649–664.

[16] D.H. Dean, Brand endorsement, popularity, and event sponsorship as advertising cues afecting consumer pre-purchase attitudes, J. Advert. 28 (3) (1999) 1–12.

[17] B. Ghosh, S. Balachander, Competitive bundling and counterbundling with generalist and specialist firms, Manag. Sci. 53 (1) (2007) 159–168.

[18] J. Harris, E.A. Blair, Consumer preference for product bundles: the role of reduced search costs, J. Acad. Market. Sci. 34 (4) (2006) 506–513.

[19] M.S. Yadav, K.B. Monroe, How buyers perceive savings in a bundle price: an ex amination of a bundle's transaction value, J. Market. Res, 30 (3) (1993) 350–358

[20] W.J. Adams, J.L. Yellen, Commodity bundling and the burden of monopoly, Q. J. Econ, 90 (August) (1976) 475–498.

[21] G.D. Eppen, W.A. Hanson, R.K. Martin, Bundling – new products, new markets, low risk, Sloan Manag. Rev. 32 (4) (1991) 7–14.

[22] L.M. Hitt, P. Chen, Bundling with customer self-selection: a simple approach to bundling low-marginal-cost goods, Manag. Sci. 51 (10) (2005) 1481–1493.

[23] R. Schmalensee, Gaussian demand and commodity bundling, J. Bus. 57 (1) (1984) S211–S230.

[24] R. Venkatesh, V. Mahajan, A probabilistic approach to pricing a bundle of products or services, J. Market. Res. 30 (4) (1993) 494–508.

[25] M. Sujan, Consumer knowledge: efects on evaluation strategies mediating consumer judgments, J. Consum. Res. 12 (1) (1985) 31–46.

[26] T. Ravichandran, M.A. Rothenberger, Software reuse strategies and component markets, Commun. ACM 46 (8) (2003) 109–114.

[27] A.J. Ko, B.A. Myers, M.J. Coblenz, H.H. Aung, An exploratory study of how developers seek, relate, and collect relevant information during software maintenance tasks, IEEE Trans. Softw. Eng. 32 (12) (2006) 971–987.

[28] K. Crowston, E.E. Kammerer, Coordination and collective mind in software re quirements development, IBM Syst. J. 37 (2) (1998) 227–245.

[29] T.M. Shaft, I. Vessey, The role of cognitive fit in the relationship between software

comprehension and modification, MIS Q. 30 (1) (2006) 29–55

[30] R. Davidson, J.G. MacKinnon, Estimation and Inference in Econometrics, Oxford University Press, Oxford, 1993.

[31] W.H. Greene, Econometric Analysis, fifth ed., Prentice Hall, Upper Saddle River, 2002.

[32] H. Theil, Principles of Econometrics, Wiley, New York, 1971.

[33] A. Zellner, An eficient method of estimating seemingly unrelated regressions and tests for aggregation bias, J. Am. Stat. Assoc. 57 (1968) (1962) 348–368

[34] J. Johnston, Econometric Methods, third ed., McGraw-Hill, New York, 1984.

[35] W.B. Frakes, T.P. Pole, An empirical study of representation methods for reusabl software components, IEEE Trans. Softw. Eng. 20 (8) (1994) 617–630.

[36] M. Maity, M. Dass, P. Kumar, The impact of media richness on consumer in formation search and choice, J. Bus. Res. 87 (2018) 36–45

[37] D.H. Kraft, T. Lee, Stopping rules and their efect on expected search length, Inf. Process. Manag. 15 (1979) 47–58.

[38] S. Ross, A First Course in Probability, seventh ed., Prentice Hall, Upper Saddl River, 2006.

Padmal Vitharana is a professor of information systems in the Martin J. Whitman School of Management at Syracuse University. He received his PhD degree from the University of Wisconsin-Milwaukee. His research expertise lies in system analysis and design. His research has been published in leading journals, such as the IEEE Transactions on Software Engineering, IEEE Transactions on Systems, Man, and Cybernetics, Journal of Management Information Systems, Marketing Science, Journal of the Association for Information Systems, Communications of the ACM, Database for Advances in Information Systems, Communications of the Association for Information Systems, Information Resource Management Journal, Marketing Science, and Information & Management.

Amiya Basu is a professor of marketing in the Martin J. Whitman School of Management at Syracuse University. He received his PhD degree from the Stanford Graduate School of Business of Stanford University. His research interests include salesforce compensation, pricing, and stochastic models. His research has been published in Marketing Science, Journal of Marketing Research, Journal of Retailing and International Journal of Research in Marketing.
