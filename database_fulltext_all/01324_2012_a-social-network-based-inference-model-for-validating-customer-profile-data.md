---
otero_id: 1324
otero_key: "6AYU9XPY"
title: "A Social Network-Based Inference Model for Validating Customer Profile Data"
authors: "Sung-Hyuk Park; Soon-Young Huh; Wonseok Oh; Sang Pil Han"
year: "2012"
journal: "MIS Quarterly"
doi: "10.2307/41703505"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
A Social Network-Based Inference Model for Validating Customer Profile Data

Author(s): Sung-Hyuk Park, Soon-Young Huh, Wonseok Oh and Sang Pil Han

Source: MIS Quarterly, December 2012, Vol. 36, No. 4 (December 2012), pp. 1217-1237

Published by: Management Information Systems Research Center, University of Minnesota

Stable URL: https://www.jstor.org/stable/41703505

## REFERENCES

Linked references are available on JSTOR for this article: https://www.jstor.org/stable/41703505?seq=1&cid=pdf-reference#references\_tab\_contents
You may need to log in to JSTOR to access the linked references.

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at https://about.jstor.org/terms

# A SOCIAL NETWORK-BASED INFERENCE MODEL FOR VALIDATING CUSTOMER PROFILE DATA $^{1}$

Sung-Hyuk Park and Soon-Young Huh

College of Business, Korea Advanced Institute of Science and Technology, 207-43 Chongryangri-dong, Dongdaemoon-gu, Seoul 130-722 KOREA {sunghuk.dave.park@gmail.com} {syhuh@business.kaist.ac.kr}

Wonseok Oh
School of Business, Yonsei University, 50 Yonsei-ro, Seodaemun-gu,
Seoul 120-749 KOREA {wonseok.oh@yonsei.ac.kr}

Sang Pil Han
College of Business, City University of Hong Kong, Suite P7913, Information Systems,
83 Tat Chee Avenue, Kowloon Tong, HONG KONG {sangphan@cityu.edu.hk}

Drawing from the social and relational perspectives, this study offers an innovative conceptualization and operational approach regarding the validation of self-reported customer demographic data, which has become an essential corporate asset for harnessing business intelligence. Specifically, based on social network and homophily paradigms in which individuals have a natural tendency to associate and interact frequently with others with similar characteristics, we constructed a relational inference model to determine the accuracy of self-administered consumer profiles. In addition, to further enhance the reliability of our model's prediction capability, we employed the entropy mechanism that minimizes potential biases that may arise from a simple probabilistic approach. To empirically validate the accuracy of our inference framework, we obtained and analyzed over 20 million actual call transactions supplied by one of the largest global telecommunication service providers. The results suggest that our social network-based inference model consistently outperforms other competing mechanisms (e.g., weighted average and simple relational classifier) regardless of the criteria choice (e.g., number of call receivers, call duration, and call frequency), with an accuracy rate of approximately 93 percent. Finally, to confirm the generalizability of our findings, we conducted simulation experiments to validate the robustness of the results in response to variations in parameter values and increases in potential noise in the data. We discuss several implications related to business intelligence for both research and practice, and offer new directions for future studies.

Keywords: Customer profile, data quality, business intelligence, inference model, social network, query processing system, simulation experiment

## Introduction

Due to increasing environmental uncertainty and fast-paced organizational changes, contemporary businesses are striving to remain ahead of the learning curve, making every effort to escalate their profitability and market growth. Recently, large-scale data warehouses and business intelligence (BI) initiatives have become an integral aspect of firms' profits and yield management operations. By effectively gathering, storing, accessing, and analyzing business data, firms can reduce unnecessary marketing expenses, have a more holistic understanding of consumer preferences and behaviors, successfully implement market segmentation, and ensure that their consumers make well-informed decisions (Kotler and Armstrong 1999; Lin 2002; Wixom and Watson 2010). However, BI initiatives are only capable of optimal performance when the data utilized are of high quality (Redman 2004; Wang and Strong 1996). Although well-designed and highly functional, BI systems that include inaccurate and unreliable data will have only limited value, and can even adversely impact business performance. From a strategic point of view, poor quality data can prevent firms from establishing effective business strategies (Redman 1995, 1998), resulting in substantial financial losses (Eckerson 2002; Fisher and Kingma 2001).

Despite their importance, academics have paid scant attention to the issues surrounding data quality validation. Traditionally, BI research in the field of information systems (IS) has focused primarily on exploiting two types of business data. The first category includes transactional data, such as items purchased, time stamps of transactions, and purchase frequencies (Palmisano et al. 2007), all of which can easily be obtained from electronic transactional systems (e.g., point-of-sales terminals). The second category deals with individual demographic data (e.g., name, age, race, and gender) that are often solely available from consumers' self-reports. Over the past several decades, as reflected in substantial scientific advancements in the areas of data mining, segmentation, and clustering studies, research on transactional data has proliferated with a plethora of conceptual frameworks and mechanical algorithms (Anderson-Lehman et al. 2004; Cui et al. 2006; Watson and Volonino 2003). In contrast, very little research has been conducted to validate the quality of self-reported demographic data, although some work has been done by government agencies (e.g., the U.S. Census Bureau). These public institutions engage in data quality management using either direct surveys or interviews. However, use of such direct verification mechanisms may not be feasible for the majority of commercial enterprises due to privacy concerns and regulations.

Several issues (e.g., privacy concerns and the complexity involved in the self-reporting process) prompt many consumers to refrain from revealing their identities, even to the point of deliberately providing inaccurate profile information (Bernard et al. 1984; Gupta and Beehr 1982; Podsakoff and Organ 1986). Furthermore, in the context of online services, registered owners are often not the real users due to registration regulations (Park et al. 2009). For example, several mobile service providers prohibit adolescent users from legally owning cellular phones and subscribing to their services, as most of them are economically dependent on their parents, and thus unable to make payments by themselves. Consequently, parents register telecommunication services for their dependents, resulting in multiple service accounts for the same person who may or may not be the actual user.

As an example, a 41-year-old, affluent, mid-career, male professional parent may register a cell phone for his 15-year-old high school daughter who will have the “real ownership” of the service. For marketing purposes, a company (e.g., a mobile phone service provider) that obtains such registration information may send personalized services and offers that are, in fact, irrelevant to the student’s primary interests (e.g., stock market news and men’s suit promotions). From the company’s perspective, this type of mis-targeting not only wastes financial resources, but also preempts business opportunities that may have otherwise translated into profits if the promotion had targeted its intended customers. Moreover, misguided marketing campaigns may also introduce ethical issues. In the example above, the adolescent user may be sent age-restricted adult content that was targeted based on the registrant’s demographic information. For consumers, unwanted promotional offers are irritating and often annoying (Eckerson 2002). Consequently, the use of inaccurate data may lead to economically inefficient resource distribution and create a lose–lose situation in which both consumers and companies are penalized.

Surprisingly, Bernard et al. (1984) stated that about 50 percent of self-administered reports contain at least some inaccurate information, lamenting that “informant inaccuracy remains both a fugitive problem and a well-kept open secret” (p. 504). $^{2}$ BI tools and applications that utilize erroneous self-reported data may therefore end up generating businesses impotence rather than business intelligence.

There are two fundamental questions that must be answered when dealing with self-reported data. First, to what extent are such data accurate and reliable? Second, if the self-reported data turn out to be untrustworthy, how can we determine the truth from such erroneous data? To address these issues, we developed a conceptual and operational framework for truth validation mechanisms by drawing on the underpinnings of the social network and homophily paradigms (e.g., Byrne 1971; Fischer 1977; Marsden 1988; McPherson et al. 2001; Turner et al. 1987). These theoretical frameworks suggest that individuals with similar demographic characteristics (e.g., age and gender) form stronger social ties and interact and communicate more frequently with one another than individuals with disparate characteristics. Using social ties as a reference to ascertain the likelihood that self-reported customer data are accurate and reliable, we constructed a relational inference model (Macskassy and Provost 2007) in order to correctly predict customers' profiles.

With the supervision and support of one of the largest mobile service providers in Korea, we analyzed over 20 million actual call detail records (CDRs), providing information about users' actual phone usage patterns (e.g., the number of unique call receivers, the frequency and duration of calls between parties) to empirically validate our conceptual framework and mechanism. In terms of research methodology, this study employs a combination of diverse techniques, including query processing, statistical inference, social network analysis, and user profiling. Utilizing egocentric network data provided by the mobile telecommunications company, our query processing system implemented a statistical inference method based on a relational learning algorithm.

Results indicated that the proposed query processing system effectively detects situations in which there is a significant discrepancy between self-reported age and actual age. Furthermore, when the results were compared to verified samples, the prediction accuracy of our method was substantially higher than that of competing methods. Even with larger samples, the results suggest that our inference model has the ability to enhance the overall performance of BI systems—for example, customer relationship management (CRM)—by eliminating over 30 percent of untrustworthy user profiles.

To further enhance the accuracy of the inference mechanisms, we also adopted an entropy approach that minimizes potential biases that may arise from the utilization of a simple probabilistic approach. Finally, to investigate the generalizability of our findings, we conducted simulation experiments and tested the sensitivity of our results depending on variations in parameter values. The simulations also validated the robustness of the proposed mechanisms in response to an increase in the amount of potential “noise” (e.g., falsified data) in the sample. The entropy approach and the simulation experiments indicated the accuracy, reliability, and efficiency of our framework.

The remainder of this paper is organized as follows. In the theoretical background section, we survey prior research relevant to our study. The subsequent section illustrates other social network approaches that have been employed to validate users' age profile data. The empirical validation section describes the data samples and presents the results of our experiments to demonstrate the model's reliability. In the implications section, we extend the discussion regarding our findings to the context of BI communities. The paper concludes with its limitations and several directions for potential future studies.

## Theoretical Background

## Literature on Data Quality Validation

Although several institutional agencies (most notably, the U.S. Census Bureau) have been actively involved in the validation of self-administered data, academic researchers, including those in the field of information systems, have paid relatively scant attention to the problems associated with erroneous data. $^{3}$ Our literature survey revealed that medicine and mathematics/statistics are the two major disciplines that have conducted in-depth investigations of the issues surrounding the quality of self-reported data. Researchers in the mathematics and statistics domains primarily employ probabilistic approaches to detect fabricated or error-prone data. For example, many studies utilize Benford's first significant digit (FSD) distribution to determine the accuracy of self-reported documents, such as tax and other financial and accounting statements (e.g., Carslow 1988; Nigrini 1996), as well as survey interviews (Schräpler and Wagner 2005; Swanson et al. 2003). Benford (1938) argued that, contrary to common belief, the numerical digits 1 through 9 are unlikely to appear equally as leading digits in multi-digit numbers. This so-called “monotonic decreasing” FSD law states that for “real world” numbers, digit distribution is skewed toward the lower digits. The chances that a multi-digit number will start with the digits 1 and 2 are 30.1 percent and 17.6 percent, respectively, while the probabilities for the digits 8 and 9 are only 5.2 percent and 4.6 percent, respectively (for further detail, see Benford 1938). Benford obtained this pattern by collecting and analyzing a diverse set of naturally occurring data, such as lengths of rivers, baseball statistics, and population numbers in U.S. counties. Nigrini (1996) scrutinized IRS tax return data and discovered that several tax-filing categories (e.g., interest paid, interest received) closely followed Benford's law. These studies disclosed that accounting and tax data manipulators tended to use each of the digits 1 through 9 about 10 percent of the time as the FSD in a number.

Similarly, by applying Benford's distribution pattern, Swanson et al. (2003) analyzed Consumer Expenditure Survey (CES) data from the Bureau of Labor Statistics, which are important in establishing the Consumer Price Index. Based on 734,684 expenditure reports, these researchers found that the CES data are in accord with Benford's FSD distribution, although a slight excess of 2s and 5s was observed. Recently, Diekmann (2007) claimed that the digits far right of a number, rather than the first digit, provide more accurate clues for detecting the erroneous data associated with statistical estimates (e.g., regression coefficients).

Although probabilistic approaches have been successfully implemented in several fields to detect falsified data, they are based purely on stochastic likelihood, and may not work precisely for numbers that fall within a limited range. For example, Benford's law may not be fully utilized to detect the falsified age information of mobile users as most teenagers (whose ages start with the digit 1) are not allowed to register themselves. Recently, Deckert et al. (2010) demonstrated that the Benford law is ineffective as a data fraud detection mechanism in certain contexts (e.g., presidential elections). Moreover, this nondeterministic approach only provides insight into whether the data in question are accurate, but does not offer a comprehensive prediction about the authentic information in cases of falsification.

Another approach to validate data quality involves collecting a small subset of samples and empirically testing their accuracy. Government agencies (e.g., the U.S. Census Bureau) and medical researchers often utilize this type of “manual inspection” to estimate the accuracy of self-reported personal data. Several studies in medical fields have empirically validated the accuracy of diverse self-administered demographic data, related to age (Kumar et al. 2004), income (Gupta and Beehr 1982), weight, and height (Roberts 1995). Their findings have suggested the presence of sizable discrepancies between self-reported data and officially verified records. Mikkelsen and Aasly (2005) reported that inaccurate electronic patient records stored in hospital information systems hinder healthcare professionals from retrieving specific patient records, impeding and delaying processes in a work setting where timely treatment and care are paramount.

Although useful and instructive, studies based on empirical validation of data quality have typically only employed a small set of matched samples (i.e., entries that are both self-reported and officially validated) primarily due to the difficulty and high cost involved in obtaining such data. Consequently, the reported discrepancy itself may threaten external validity. Furthermore, evaluation of data quality through this mechanism can be costly and time-consuming.

Finally, management scholars have recently begun to devote greater attention to data-related problems. Building on the literature in accounting and auditing, Krishnan et al. (2005) established a conceptual ontology-based framework through which data reliability can be assessed for accounting IS. These authors initially developed a graph-theoretic, ontological meta-model in an attempt to delineate the key concepts required to assess data reliability. Then, they proposed specific algorithms designed to process instances of the ontological model in order to permit auditors to make informed decisions. One key aspect of this study lies in the formulation of the algorithm; whereas previous studies (e.g., Bailey et al. 1985) employed a pure mathematical approach, this study encompassed the human-judgment factors and heuristics used by practitioners (e.g., auditors) in its model to complement the formalized mathematical approach. In another study, Jiang et al. (2007) introduced a data integration framework to solve the attribute-value conflict, which occurs when data from heterogeneous sources are merged without systematic guidelines. In the absence of data integration, an attribute value for an entity is often recorded differently in multiple databases due to data management and processing errors. Based on a deterministic data integration approach, these authors offer an innovative solution that aims to provide the “best” value from the set of possible values in a variety of data sources. Furthermore, they discuss the implications of their systematic approaches for direct marketing campaigns and promotions. Although these two studies also deal with data quality issues, their main focus is on the “mechanical” issues (e.g., heterogeneous data sources) surrounding transactional data. Only limited implications are provided for the validation of self-reported data (e.g., census and consumer profile data).

## Homophilious Ties in Social Networks

The present study offers a new approach for detecting fraudulent and error-prone self-reported data based on the conceptual underpinnings of the homophily and social network frameworks. Specifically, by investigating consumers' social interaction patterns and homophilous ties, we propose new conceptual and operational mechanisms for validating the accuracy and credibility of self-reported data. According to Lin et al. (2007), processes, people, and technologies constitute the primary sources of flawed data, with people being the most common. In the case of self-reported data, many individuals opt to deliberately falsify their demographic information (e.g., age, sex, income) for a variety of reasons (Podsakoff and Organ 1986), including privacy-related concerns, dishonesty, and avoidance of time commitment. These fraudulent and inattentive responses prevent marketers from successfully implementing data-driven marketing campaigns (e.g., targeting, personalization, and segmentation), while severely impairing the integrity of BI (Lee and Strong 2003; Redman 2004).

Our theorizing is based on the homophily phenomenon in social networks, which suggests that people have a natural tendency to interact and socialize more frequently with individuals who are similar to themselves. The homophily effect denotes that

people's personal networks are homogeneous with regard to many socio-demographic, behavioral, and intrapersonal characteristics....Homophily is the principle that a contact between similar people occurs at a higher rate than among dissimilar people (McPherson et al. 2001, pp. 415-416).

The homophily principle has long been perceived as a powerful organizing standard that governs social structures and weaves interpersonal webs of connection (Lazarsfeld and Merton 1954). This “love of the same” social phenomenon suggests that communication relationships are not randomly determined. Extensive empirical support has been found for the presence of age–homophily effects in social affiliations and interactions (see Louch 2000; Marsden 1988). For example, if a user’s network is primarily composed of teenagers, there is a high probability that the user him or herself is, in fact, a teenager. The theory behind the homophily principle has served as the foundation for the development of major theories in sociology, such as social identity theory (Tajfel and Turner 1979), self-categorization theory (Turner et al. 1987), and group dynamics (Shaw 1976).

Recently, several studies have acknowledged the importance of social networks as business conduits. For example, Das-gupta et al. (2008) developed a customer churn prediction model utilizing social ties in mobile telecommunication networks. These authors found that customers whose friends or colleagues switched to another mobile service carrier were more likely to churn than those without such churners in their social networks. Similarly, Hill et al. (2006) proposed a network-based marketing method designed to predict likely adopters of a new service. These authors demonstrated that customers who were linked to a previous (or former/existing) customer adopted a new service at a rate three to five times greater than the “prospect” groups that were randomly chosen by the best practices of a company’s marketing team. Finally, Aral and Walker (2011) designed a randomized field experiment on a popular social networking website to demonstrate that firms can create word-of-mouth peer influence and social contagion by incorporating viral features into their products and marketing campaigns. These authors found that viral product design features can indeed generate econometrically identifiable peer influence and social contagion effects.

Drawing upon these theoretical foundations and insights, we investigate social interaction patterns among mobile phone users, developing a framework by which to evaluate the accuracy of self-reported user profile data. We also infer reliable demographic information for instances when potential inaccuracies are detected in such data. Further, we employ the entropy mechanism to enhance our model's predictive capability and design a large-scale simulation to validate the generalizability of our findings.

## Social Network-Based Inference Mechanisms

Recommendation systems have emerged as essential elements of CRM practice and BI initiatives (Kamakura et al. 2003). However, inaccurate and untrustworthy data may prevent these systems from achieving their full potential. To formally describe the business implications of this predicament, we rely upon the framework suggested by Adomavicius and Tuzhilin (2005):

$$
\forall c \in C, s _ {c} ^ {\prime} = \operatorname{argmax} _ {s \in S} u (c, s)\tag{1}
$$

where C denotes customer space, S refers to goods and services space, and u: $C \times S \rightarrow R$ represents a utility function that determines the usefulness of item $s \in S$ to customer $c \in C$ .

According to Adomavicius and Tuzhilin, recommendation can be thought of as a catalyst to identify an item $s' \in S$ that maximizes a user c's utility. However, the BI system is of no use at the outset if a user's input, C, such as age and gender, is falsified (Figure 1). Both firms and consumers that rely on erroneous recommendation will be penalized, and resources will be dissipated as a consequence of misdirected marketing efforts. To mitigate this problem, we extend Adomavicius and Tuzhilin's model by including an additional condition for the extent to which demographic profiles (C) correlate with a user's actual status. This integrated framework utilizing both existing recommendation systems and the social network-driven query processing system (see below) can generate recommendation outputs that accurately meet consumers' need and preferences.

## Architecture of Social Network-Driven Query Processing Systems

To improve the accuracy of consumers' demographic information, we developed a social network-based inference framework that includes a four-stage validation process. This framework was established using the conceptual insights obtained from studies based on social networks and homophily theories. For example, Marsden (1988, p. 71) states that, in confiding relations, “the patterning of citations by age reflects both homophily and social distance effects.” This suggests both a strong tendency to confide in same-age peers and a social distance effect; the greater the age gap, the less likely people are to discuss important matters with each other. In a large-scale empirical study analyzing Microsoft instant-messaging system data, Leskovec and Horvitz (2008) discovered that people of similar ages tend to communicate more with one another, and as the age difference between two participants decreases, the number of conversations increases exponentially.

![](/api/attachments/6AYU9XPY/fulltext/images/f53c4a1312c8385719cc6233680692d08f5768bbbfc3da558454749fe4c514a1.jpg)  
Figure 1. User Profile Data Quality Problems in Recommendation Systems

With input from social networks and homophily theory and empirical evidence from related studies as the framework's operational building blocks, we initially established users' communication patterns and computed probability mass functions in our data set. We then developed an inference mechanism and entropy-based validation system. More specific procedures and techniques regarding the construction of the inference mechanism are as follows: First, based on the actual mobile call records, the system identifies comprehensive social networks among numerous users, which depict the frequency of communications and closeness of interpersonal connections (step 1 in Figure 2). Second, a statistical analysis regarding the call receiver's (CR) age distribution in comparison to the call originator's (CO) age group is performed (step 2). Third, since each CO's age distribution contains his or her unique interaction pattern, this pattern is employed to assess the extent to which a CO's self-reported age profile is reliable and trustworthy. The reliability validation is conducted by comparing the age distribution of this particular CO's CRs with a typical CR age distribution pattern of the COs within the same age group, obtained from an analysis of the entire call detail record (CDR) data (step 3). Our system employed a likelihood-based inference mechanism to assess the accuracy of each user's profile. Finally, the system calculates entropy values for all users whose actual ages are inferred during step 3 (step 4). Figure 2 shows the system architecture of the query processing system, including the four-stage data validation process. Through utilizing the validated user profiles generated by the query processing system, "legacy" systems, such as recommendation and CRM systems, can provide managers with trustworthy and valuable information.

![](/api/attachments/6AYU9XPY/fulltext/images/48018406a7a62d9c496798fac5b76da4cc79f0c002d3e416beefd77cc2157e33.jpg)  
Figure 2. Architecture of the Query Processing System

## Network Construction (Step 1)

During this process (step 1), we create a validation model by applying a relational approach in a node-centric network learning framework (Macskassy and Provost 2007). In contrast to the nonrelational model, the relational mechanism utilizes the network's linked, bilateral relations as well as the attribute values of locally related entities. A particular node's probability of class membership is determined by the membership of the local network's neighbors (e.g., CRs). We follow Macskassy and Provost's notation, such that user $i$ 's attribute $x_{i}$ represents class membership. In addition, we adopt a first-order Markov assumption:

$$
\mathrm{P} (\mathbf {x} _ {\mathrm{i}} | \mathbf {G}) = \mathrm{P} (\mathbf {x} _ {\mathrm{i}} | \mathcal {N} _ {\mathrm{i}})\tag{2}
$$

where G is a set of neighbors in an entire network, and $N_{i}$ is a set of local network neighbors of user i such that $P(x_{i}|N_{i})$ is independent of $G - N_{i}$ . Throughout the paper, we assume that $N_{i}$ comprises only the immediate, local network neighbors of user i, and is time invariant during the sampling period. A simple relational classifier can estimate class membership probabilities by assuming the existence of demographic resemblance as follows:

$$
\mathbf {P} (\mathbf {x} _ {\mathrm{i}} = c | \boldsymbol {\mathcal {N}} _ {\mathrm{i}}) = \frac {1}{z} \sum_ {\left\{x _ {j} \in \boldsymbol {\mathcal {N}} _ {i}, x _ {j} = c \right\}} \mathbf {W} _ {\mathrm{i}, \mathrm{j}}\tag{3}
$$

where $Z = \sum_{\{s, e, x\}} w_{i,j}$ and $w_{i,j}$ are weights on the basis of the relational strength between user i and user j. The notation “c” refers to the age class.

## Profile Distribution Summarization (Step 2)

To provide stylized information regarding the operation of our age profile validation model, we offer the following mathematical explanations. Let O denote a set of COs, then $O = \{o_{1}, o_{2}, \ldots, o_{total number of COs}\}$ where $o_{i}$ is the i-th CO, and let $N_{i} = \{r_{i1}, r_{i2}, \ldots, r_{total number of CRs of i-th CO}\}$ be a set of $o_{i}$ 's network neighbors where $r_{ij}$ is the j-th network neighbor of $o_{i}$ . To summarize CR's age distribution for a given CO's k, we define a conditional probability mass function (pmf, $\Phi_{k}$ ) such that P(CR's age = v | CO's age = k) = N( $\{x \mid x \in \cup_{oi \in Oage=k} N_{i}$ and age of x = v }) / N( $\{x \mid x \in \cup_{oi \in Oage=k} N_{i}\}$ ). Three types of call information are utilized to calculate the conditional pmf. These include the number of unique CRs, call duration, and the number of calls. For example, consider the conditional pmf based on the number of unique CRs. The numerator can be written as N( $\{x \mid x \in \cup_{oi \in Oage=k} N_{i}$ and age of x = v ), and the denominator can be expressed as N( $\{x \mid x \in \cup_{oi \in Oage=k} N_{i}\}$ ), where N() is a function returning the number of elements in a given set, and $O_{age=k}$ is a subset of O that contains $o_{i}s$ of age k. The denominator represents a set of CRs who have received calls from a particular CO whose age is k. Similarly, we derive two additional collections of conditional pmfs: one based on call durations and the other on the number of calls.

## User Profile Inference (Step 3)

To identify users who may have provided incorrect age information and to predict their true ages on the basis of the social network analysis illustrated in step 1, we created and employed a likelihood-based, statistical, relational inference model. Of the several popular demographic attributes (e.g., age, gender, and address), we chose to focus on age, as it is a key criterion in both consumer survey and marketing campaigns (Peterson 1984). Our methodological approach is similar in flavor to the network-based inference method recently introduced in mobile telecom industries for churning analysis (Dasgupta et al. 2008). However, our system is unique and comprehensive. We capitalize on the entire age distribution of CR, rather than the single, derived, variable approach that has been adopted in previous studies (e.g., Dasgupta et al. 2008). We summarize our relational learning method as follows:

$$
\operatorname{Argmax} _ {k} L \left(\Phi_ {k} | x\right)\tag{4}
$$

where $\Phi_{k}$ is a pmf representing the distribution of CR age for the k-year-old CO, L denotes the likelihood function, and x is the user whose actual age we wish to infer.

By relying on the three summarized forms of statistical information, our relational inference model can accurately infer an individual user's age. Specifically, equation (4) can be rewritten to equation (5) as follows:

$$
\operatorname{Argmax} _ {k} \Pi_ {i \in \mathcal {N} _ {1}} P (r _ {i j} ^ {\prime} s a g e = v _ {j} | o _ {i} ^ {\prime} s a g e = k)\tag{5}
$$

where $r_{ij}$ is the j-th CR of the i-th CO, $o_{i}$ , and $v_{j}$ is the age of $r_{ij}$ . To diminish computing time in a database of this size, we employ logarithmic transformation to derive a revised equation (6).

$$
\operatorname{Argmax} _ {k} \sum_ {j \in \mathcal {N} _ {i}} \log_ {1 0} \left[ P \left(r _ {i j} ^ {\prime} s a g e = v _ {j} \mid o _ {j} ^ {\prime} s a g e = k\right) \right] \tag {6}
$$

Equation (6) is a crucial component of the user profile assessment model. For a CO, this equation provides the most relevant age (k). Identifying k maximizes the likelihood of observing a particular CO's network neighbors' ages using the formula above.

Figure 3 illustrates how our model identifies those users who have falsified their age profiles. In this particular example, A represents a user whose reported age in the firm's database is 38. As shown in A's social network, user A interacted with five CRs aged 10, 10, 11, 14, and 19 years. Based on A's CDR, we construct A's social network, which consists of five CR nodes and edges designating communication weight between any two. The three bar charts in the middle represent A's three different pmfs by the number of CRs, the number of calls, and the call durations. To compute the pmfs, we combined individual transactions for each of the three factors. For example, for A's pmf on 10-year-old CRs, the total number of CRs is 2 as there are two CRs in his network that are 10 years old (Figure 3, dotted circle). In this example, total call duration was 225 minutes (= 191 + 34) and 36 calls were made (= 27 + 9). These data are obtained from A's actual mobile communication records. On the right-hand side of Figure 3, the results of age prediction are presented. When inferring the age of this user based on the number of CRs, A's log-likelihood value is at maximum, 1.0, normalized value, when A is predicted to be 13 years old. Therefore, A's age is not presumed to be 38 years old, but 13 years old instead. Similar results were found when the two alternative pieces of information (i.e., call duration and number of calls) were employed. Thus, our query processing system has determined that A's self-reported age is likely to be inaccurate in the database. In fact, according to the manual validation, A was, indeed, not a 38-year-old adult, but rather a teenager whose mother had registered his mobile service on his behalf.

## Entropy Calculation (Step 4)

To further improve the accuracy of the inference model from step 3, we use an entropy measure to select the top-k users from a candidate pool of users whose actual ages were inferred in step 3. In academic circles, entropy is frequently implemented as a proxy to represent the level of complexity. However, in studies related to the issue of handling uncertain data, entropy is often used as a measure of uncertainty (Wang et al. 2009): if the level of uncertainty is low, the entropy is low as well. Moreover, the top-k selection queries are often used to select a small number of objects that best match the given condition. In the present study, the entropy measure is utilized to select top-k user profiles with a higher degree of certainty (Ayanso et al. 2009; Bruno et al. 2002). According to Shannon's (1948) well-known entropy theory. the definition of entropy can be expressed as shown in equation (7).

$$
\mathbf {E n t r o p y} = - \sum_ {\mathrm{j} = 1} ^ {\mathrm{n}} \mathrm{P} (\mathrm{X} = \mathrm{x} _ {\mathrm{i}}) \log_ {1 0} \mathrm{P} (\mathrm{X} = \mathrm{x} _ {\mathrm{i}})\tag{7}
$$

where X is a random variable, $x_{i}$ is X's value, and n is the number of possible outcomes. We can revise equation (7) to ensure a match with our setting as shown in equation (8).

$$
\begin{array}{l} \mathbf {o} _ {\mathrm{j}} ^ {\prime} \text {s entropy} = \\ \sum_ {\mathrm{j} \in \mathcal {N} _ {\mathrm{i}}} \mathrm{P} (\mathrm{r} _ {\mathrm{ij}} ^ {\prime} \text {s age} = \mathrm{v} _ {\mathrm{j}} | \mathrm{o} _ {\mathrm{i}}) \log_ {1 0} \mathrm{P} (\mathrm{r} _ {\mathrm{ij}} ^ {\prime} \text {s age} = \mathrm{v} _ {\mathrm{j}} | \mathrm{o} _ {\mathrm{i}}) \end{array} (8\tag{8}
$$

To reiterate, we use the two-phase approach based on two different techniques, as described in equations (6) and (8),

![](/api/attachments/6AYU9XPY/fulltext/images/f5b28f2672d863ae39545aaa9cbbee2a4b1c28c09c1bf9c1d53ce3ba697fc3a4.jpg)

Figure 3. An Example of Age Inference Process

respectively. Initially, our query processing system employs a statistical inference model to predict the true age of users, and then selects top-K user profiles on the basis of their entropy values to increase the accuracy of the inference system. For example, when a recommendation system requests 200 women ranging from 25 to 30 years of age, our system selects the top 200 answers with the lowest degree of uncertainty among the entire population of existing peers belonging to that particular age group. Then, the top-k retrieval results are selected in order to provide the number of k requested users.

Figure 4 provides a summary of all of the procedural mechanisms illustrated thus far. To ascertain the reliability of the data, we develop a user's social networks based on three distinctive parameters (number of unique CRs, call durations, and number of calls). Subsequently, we predict his or her true age through the implementation of the statistical inference mechanism in equations (5) and (6). During this process, the self-reported data that deviate substantially from predicted outcomes are eliminated (see area C in Figure 4). Finally, we measure the CO's entropy with equation (8) and choose the data with the lowest degree of uncertainty (area A in

Figure 4). The next section evaluates how well our reliability assessment measure and inference model perform based on data from millions of real-world call records.

## Empirical Validation

## Demographic Similarity Between Call Originators and Call Receivers

## Call Detail Records

Data were collected from one of the largest mobile telecommunications service companies in Korea. The sample consists of 20.4 million call transaction records made by more than 160,000 COs who were randomly drawn from a pool of 3G mobile telecommunication service users between March 2008 and May 2008. Call receivers (CRs) calls were traced and their profile information collected. The number of CRs with known profiles was 923,804. CDRs used in our study were not encrypted, with the exception of identification attributes (i.e., users' phone numbers). During the data collection process, the company's database administrator coded all phone numbers to prevent participating researchers from viewing users' identities. This robust procedure was employed to protect consumer privacy and data security.

![](/api/attachments/6AYU9XPY/fulltext/images/28b2ce99d8fe23f5edccd2d652fa72318d0c708634a4435b63f269cf4eb43993.jpg)  
Figure 4. Inference Process of the Query Processing System

## Age Distributions

We investigated how the distribution of CR age varied depending on CO age. Distributions of CR age were drawn using the CDR. Figure 5 depicts a complete distribution of the percentage of CRs based on the age differences between COs and CRs. The highest peak (approximately 13.7 percent) was observed when no age difference was present. Interestingly, CRs decrease sharply with a small age difference between COs and CRs (i.e., -2 or +2). Overall, the distribution is symmetric regardless of the direction of age differences.

Figure 6 illustrates the actual distributions of CR ages for four different age groups. Consistent with Figure 5, the distribution's peak occurs at the same CO age for all age groups, although the highest peak occurs at 15 (Figure 6b) and the lowest at 9 (Figure 6a). This seems to be a realistic communication pattern, as teenagers tend to interact most frequently with peers of the same age. Interestingly, this age group also tends to communicate frequently with individuals in their 40s, suggesting the presence of strong intergenerational (i.e., childparent) communication activities. As expected, this between-generation call pattern has the highest prevalence for the 9-year-old group (Figure 6a). The call distribution patterns of 21-year-olds (Figure 6c) are analogous to those exhibited in the 15-year-old group.

Finally, Figure 6d represents the call distribution pattern of 38-year-old COs. Similar to the pattern exhibited across the other age groups, this middle-aged group communicated most frequently with CRs of the same age, albeit not as intensively as their teenage counterparts. As expected, the call pattern of a CO within this age group demonstrates a more normal distribution compared to that of the 15-year-old teenagers. However, the 38-year-old COs also communicated with CRs who were 24 years younger. Thus, we estimate that the distribution of the CR's age peaks once at the CO's own age, and again at roughly the CO's age ± 24. This finding is consistent with the well-known theory of age homophily in the field of Sociology, which states that age homophily is a powerful baseline component for understanding social behaviors (Fischer 1977; Louch 2000; Marsden 1988; Mcpherson et al. 2001), and the extent of age homophily diminishes as children grow older (Shrum et al. 1988).

![](/api/attachments/6AYU9XPY/fulltext/images/e8bd565280c6d1e42d2ea1585f5eac25c12ac384ba4ef3141f58f840681768c3.jpg)  
Figure 5. The Distribution of Age Differences Between COs and CRs

(a) Age = 9  
![](/api/attachments/6AYU9XPY/fulltext/images/57ca2365f42b271efb8ddcf58402abc0018cc472f369dbddfdd47c8a8b8769af.jpg)

(b) $\mathrm{{Age}} = {15}$  
![](/api/attachments/6AYU9XPY/fulltext/images/9ad511bd8565e6fb43b6e9f55744fd6cace00617097fbdad21ae2d087b69c581.jpg)

(c) $\mathrm{{Age}} = {21}$  
![](/api/attachments/6AYU9XPY/fulltext/images/c7a5340d3b1e2628dcad9b5b43a561052e720c0a3170565696daf8361bc9860e.jpg)

(d) Age 38  
![](/api/attachments/6AYU9XPY/fulltext/images/c6737512d95e393144336dc6fa6265b6bf5454401ce040d2c681e517ed3638a9.jpg)

<table><tr><td colspan="3">Table 1. Three Mechanisms to Predict Accurate Age</td></tr><tr><td>Models</td><td>Methodological Approach</td><td>Example</td></tr><tr><td>Weighted Average Method</td><td>Use a frequency-weighted mean to predict age from a set of data ( $\mathcal{N}_{i}$ )</td><td>This method predicts that the CO is 19 years of age ( $14 \times 5 + 16 \times 3 + 38 \times 2$ ) / ( $5 + 3 + 2$ ) = 19.4)</td></tr><tr><td>Simple Relational Classifier</td><td>Use a probabilistic approach to predict age from a set of data ( $\mathcal{N}_{i}$ )</td><td>This method predicts that the CO is 14 years of age ( $P(CO = 14 yrs) = 0.5$ ,  $P(CO = 16 yrs) = 0.3$  and  $P(CO = 38 yrs) = 0.2$ )</td></tr><tr><td>Proposed Model</td><td>Use a maximum likelihood approach, which selects the value that maximizes the likelihood function from the known distribution of data ( $\mathcal{N}_{i}$ )</td><td>This method predicts that the CO is 15 years of age because the likelihood value is maximized at Age = 15 with a distribution of 9–38 years old</td></tr></table>

## Accuracy of Model with Known Profiles

Evaluating the performance of the proposed inference model requires user profiles with known, accurate age information. For a test sample, we used a set of COs between 13 and 18 years of age and their corresponding CRs. We chose this age group because in our data the only accurate age profile information was available in this adolescent group. We evaluated our proposed inference model by comparing it with alternative methods: the weighted average method and the simple relational classifier (Macskassy and Provost 2007). Table 1 compares these three alternative mechanisms that can be employed to predict age, including our proposed approach. To illustrate with an example (Table 1, second column), we assumed that this CO communicated with CRs who were 14, 16, and 38 years of age, and interacted 5, 3, and 2 times, respectively. All three methods produce divergent prediction outcomes.

The weighted average approach can be problematic, in particular when the weights are somewhat equally distributed. For example, consider a situation in which a 15-year-old CO communicates with his or her peer (a 15-year-old CR) with the same frequency as his or her parents (a 41-year-old CR). The weighted average method will produce misleading results, which suggest that the CO is 28 years of age (= (15 + 41)/2). The computed “average value” fails to preserve the unique characteristics of the inputs on two opposite ends of the age spectrum (15 and 41), while generating a value (28) that does not represent either one. The simple relational classification method, on the other hand, can perform effectively, as it does not involve the “artificial manipulation” required in the weighted average approach. However, this probabilistic approach can also result in biased predictions, as its focus is the event with the highest probability of occurrence; other possibilities are not taken into account. Our proposed mechanism improves the prediction capability by compensating for the deficiencies inherent in these approaches.

As noted earlier, three different types of information—the number of CRs, call duration, and the number of calls—were used as parameters in this study. Consequently, nine different combinations were made from the three prediction methods and three information types (Table 2). Each information type was evaluated using the three prediction methods. The performances of the three divergent methods are also listed (Table 2). In the weighted average method, the number of CRs and their weights (w1, w $_{i,j}$ , respectively in equation 2) are equal across j for a given i. Alternatively, for call duration (w2) and the number of calls (w3), the weights are determined between o $_{i}$ and r $_{ij}$ . Similarly, the simple relational classifier utilized three types of summary information to predict CO age (c in equation 2). The method proposed here used the same three parameters to predict the most appropriate CO age (k in equation 6).

Results from Table 2 indicate that our proposed method consistently outperforms the others, regardless of the information type. In Table 2, the deviation (Dev) is defined as the difference between the predicted age and the actual age in absolute value, and the prediction accuracy is equal to the correctly predicted number of users among the total number of users. For example, when the number of CRs was utilized as the information type, our proposed model accurately predicted the ages of 133 users (out of 155) with a margin of deviation being either 0 or 1 year (i.e., Dev ≤ 1). This represents 85.8 percent (= 133/155) prediction accuracy. When we expanded the margin of error to three years (i.e., Dev ≤ 3), our model's prediction accuracy increased to 92.9 percent. When call duration was chosen as the information type, our model's prediction accuracy was nearly 90 percent, while the competing models exhibited less than 70 percent accuracy. Overall, our methods (a1, a2, and a3) clearly outperform the alternative mechanisms, regardless of the choice of information type. This finding suggests that our method can be effectively employed to infer the actual ages of individuals, particularly when the quality of self-reported age profiles is

<table><tr><td colspan="8">Table 2. Result Comparison: Age Inference</td></tr><tr><td>Information Type (wi,j)</td><td>Method</td><td>Dev ≤1 (freq.)</td><td>Prediction Accuracy (%)</td><td>Dev ≤2 (freq.)</td><td>Prediction Accuracy (%)</td><td>Dev ≤3 (freq.)</td><td>Prediction Accuracy (%)</td></tr><tr><td rowspan="3">Number of CRs</td><td>Weighted Average (w1)</td><td>20</td><td>12.90</td><td>35</td><td>22.58</td><td>48</td><td>30.97</td></tr><tr><td>Simple Relational Classifier (s1)</td><td>128</td><td>82.58</td><td>136</td><td>87.74</td><td>138</td><td>89.03</td></tr><tr><td>Proposed Model (a1)</td><td>133</td><td>85.81</td><td>140</td><td>90.32</td><td>144</td><td>92.90</td></tr><tr><td rowspan="3">Call Duration</td><td>Weighted Average (w2)</td><td>36</td><td>23.23</td><td>51</td><td>32.90</td><td>66</td><td>42.58</td></tr><tr><td>Simple Relational Classifier (s2)</td><td>92</td><td>59.35</td><td>100</td><td>64.52</td><td>107</td><td>69.03</td></tr><tr><td>Proposed Model (a2)</td><td>120</td><td>77.42</td><td>131</td><td>84.52</td><td>137</td><td>88.39</td></tr><tr><td rowspan="3">Number of Calls</td><td>Weighted Average (w3)</td><td>34</td><td>21.94</td><td>55</td><td>35.48</td><td>71</td><td>45.81</td></tr><tr><td>Simple Relational Classifier (s3)</td><td>98</td><td>63.23</td><td>105</td><td>67.74</td><td>110</td><td>70.97</td></tr><tr><td>Proposed Model (a3)</td><td>117</td><td>75.48</td><td>131</td><td>84.52</td><td>139</td><td>89.68</td></tr></table>

Notes: Dev is defined as the absolute value of the age difference between observed and predicted ages. For example, Dev $\leq$ 1 indicates that the age difference in absolute value is less than or equal to 1 year.

Prediction Accuracy is defined as the percentage of users whose age was predicted accurately with a small margin of error (i.e., Dev $\leq k$ ( $k = 1, 2, 3$ )). Note that the total number of users whose age was known with certainty was 155.

unknown. Moreover, regardless of the variation in information type and the criterion value, high prediction accuracy authenticates the robustness of our new method.

Figure 7 demonstrates that entropy is a key factor in the system's performance. As depicted, the accuracy ratio decreases as the number of top-k users increases. More specifically, when only a few query answers are requested, our system can provide trustworthy user profiles among users who “passed” the data reliability test in the previous step. For example, the experimental results reported accuracy rates of 100 percent for the top 40 users, 98 percent for the top 100, and an accuracy rate higher than 92 percent for the top 150.

## System Implementation on Large-Scale Live Data

To perform a large-scale test with actual, “live” business data, we selected 96,078 COs with greater than five CRs (with known profiles) from the initial data set of 166,507 COs. Under the decision criterion “if |age deviation|≤3, then trustworthy age profile” where age deviation is defined as the predicted age minus the self-reported age, our system reported 66,424 COs as true age profile users. This implies that 69.13 percent of users (|age deviation|=0: 29.48%, 1: 20.49%, 2: 11.34%, and 3: 7.84%) offered accurate age profiles. In other words, our system estimated that 30.87 percent of users in a mobile company’s database submitted questionable, uncertain age profiles. Interestingly, these results are consistent with the qualitative estimation of the company’s marketing practitioners’ as well as the call center service employees' experiences. These findings support the idea that untrustworthy users withhold accurate demographic information when registering cell phones.

## Robustness Tests Through Simulation Experiments

To what extent can our results be generalized? How robust are our inference models in response to an increase in the proportion of “noise” (i.e., fabricated data) in the dataset? $^{4}$ Although the empirical verification with 155 validated customer profiles resulted in an accuracy rate of 93 percent, verification is necessary of the robustness and accuracy of our inference framework with known labels in a large-scale setting. Thus, we developed and conducted simulation experiments designed to reflect the real-world as closely as possible.

According to the data analysis results reported in the previous section (see Figure 6), the CR age (X) distribution for a given CO can be approximated as a bimodal distribution, which consists of two normal distributions: $N(\mu_{1\mathrm{st peak}}, \sigma_{1\mathrm{st peak}})$ and $N(\mu_{2\mathrm{nd peak}}, \sigma_{2\mathrm{nd peak}})$ . Since the mean parameters of the first and second normal distributions represent the CO's age and the CO's age ± alpha (i.e., 24), respectively, the distribution of CR age for a given CO (as a random variable) can be thought to be dependent on the CO's age. In addition, the noise (falsified data) can be assumed to be uniformly distributed, which implies that the age profile-independent CR age data, including error-prone self-reported CR ages, are randomly distributed.

![](/api/attachments/6AYU9XPY/fulltext/images/9bfa9339490c30400d74b220011dae4b29cc0ff992c95f288d843abbc3ced938.jpg)  
Figure 7. Entropy Effect

To design the simulation processes, we elected to use inverse transformation sampling, which has been widely adopted in similar experiments for the purpose of generating random numbers from continuous probability distributions (Ramberg and Schmeiser 1972). Utilizing this approach, we obtained a series of numbers with a normal distribution, N(μ, σ), where μ is the mean and σ is the standard deviation parameters. In the age inference context, it is assumed that the CR age distribution for a given CO follows a combination of two normal distributions and one uniform distribution: (1-p)w₁N(μ₁st peak, σ₁st peak) + (1-p)w₂N(μ₂nd peak, σ₂nd peak) + pU(Min\_CR\_age, Max\_CR\_age). The parameters are described in Table 3.

Given that each of the three distributions is continuous, the integrated distribution, which was constructed as a linear combination of the three continuous functions, should also be presumed to be continuous. In addition, the cumulative distribution function of the integrated function can also be extracted from these distributions. Therefore, we used the inverse transformation sampling to generate values for CR ages for a given CO distributed according to the observed communication patterns (within- and between-generation communications). Once a sufficiently large number of CR ages had been accumulated as samples, we predicted the CO's age using the proposed age inference model described in equation (6). The specific simulation processes, including the age inference steps, are as follow:

\- Step 1: Generate a uniform random number, $\mathbf{r} \sim \mathbf{U}(0,1)$ .

\- Step 2: For a cumulative density function, $\mathrm{F}( )$ of CR age, return $\mathrm{F}^{-1}(\mathrm{r})$ to generate a CR age, where $\mathrm{F}( )$ is a cumulative probability density function of the CR age for a given CO (random variable).

\- Step 3: For a given CO, generate N CR ages by iterating steps 1 and 2 N times (N > 0).

\- Step 4: Predict the CO's age using the proposed age inference model (i.e., equation 6).

• Step 5: Calculate entropy using equation (8).

Sensitivity analyses were performed for the following two key variables, which are the important elements in the robustness experiments: the number of CRs and the proportion of false CR ages (Table 3). Figure 8 illustrates the model's accuracy (y-axis) contingent on the number of CR ages (x-axis) used for the CO's age inference. Each combination was run 1,000 times to increase the experiment's validity. The results suggest that regardless of the magnitude of the false CR age proportion (10%, 30%, and 50%) in the dataset, prediction accuracy of the age inference model improves sharply as the number of CR age samples increases. For example, despite the high proportion of false CR age samples in the data (30%), the model's predictive accuracy still exceeds 90 percent when the number of CR age samples surpasses a certain threshold (5). $^{5}$ Despite variations in specific quantitative values with regard to prediction performance as the proportion of false data increased, the pattern and the trend did not, and the results were consistent across all parametric values. Therefore, the simulation experiments reveal that our model is robust and stable in the presence of inaccurate data. However, a large number of CRs must be utilized, particularly when the proportion of falsified data is expected to be high (e.g., 50%) in the self-reported data.

<table><tr><td colspan="3">Table 3. Simulation Parameters</td></tr><tr><td>Parameter</td><td>Description</td><td>Value</td></tr><tr><td>Num_CR</td><td>Number of CRs used to infer a CO&#x27;s age</td><td>values from 1 to 10</td></tr><tr><td>P</td><td>Proportion of false CR ages (&quot;noise&quot;)</td><td>values from 0% to 50%</td></tr><tr><td> $w_1$ </td><td>Within-generation communication weight ( $0 < w_1 \leq 1$ )</td><td>80%</td></tr><tr><td> $w_2$ </td><td>Between-generation communication weight ( $1 - w_1$ )</td><td>20%</td></tr><tr><td> $μ_{1st\ peak}$ </td><td>Mean of first normal distribution (i.e., the representative age value of the within generation group)</td><td>CO&#x27;s age</td></tr><tr><td> $σ_{1st\ peak}$ </td><td>Standard deviation of first normal distribution</td><td>2.0</td></tr><tr><td> $μ_{2nd\ peak}$ </td><td>Mean of second normal distribution (i.e., the representative age value of the between-generation group)</td><td>CO&#x27;s age ± 24</td></tr><tr><td> $σ_{2nd\ peak}$ </td><td>Standard deviation of second normal distribution</td><td>3.5</td></tr><tr><td>Min_CR_age</td><td>Minimum CR age among the observable CR ages</td><td>7</td></tr><tr><td>Max_CR_age</td><td>Maximum CR age among the observable CR ages</td><td>80</td></tr></table>

![](/api/attachments/6AYU9XPY/fulltext/images/5e61cb53e09bd268da3ac27a4ce19c3e8e700b9b18f2a2bdbb8ca87a6a06e449.jpg)  
Figure 8. Prediction Accuracy in Response to Inaccurate Data (CO age = 15)

An additional experiment was conducted to investigate the relationship between entropy values and prediction performance. Figure 9 indicates that the prediction accuracy (y-axis) is generally high regardless of the proportion of “noise” in the data. For example, when the falsified data comprise less than 20 percent of the entire data sample, the accuracy exceeds 90 percent regardless of the entropy values (x-axis). Even when the data include 40 percent noise, prediction accuracy still exceeds 85 percent, independent of the entropy value. Further, prediction performance shows only a marginal decrease in response to an increase in entropy value. Nevertheless, when the amount of falsified data is expected to be high (i.e., greater than 50% of the samples), it is recommended that managers use conservative (i.e., low) entropy values in order to preserve high prediction performance.

## Implications

Our conceptual framework and large-scale empirical analysis offer several scholarly and managerial insights. From a research perspective, our relational inference model, which is based on patterns of social ties, provides a unique lens through which to assess the validity of self-reported customer profiles. That the framework is based on patterns of social relationships makes sense, given that individuals' social circles and communication patterns within those circles reflect their identities. Patterns in the CDR data used in this study, which included the communication patterns of 166,507 real-world users, strongly support the notion of age-homophily. The accuracy of our relational inference framework was firmly validated in its ability to assess the quality of self-reported user profile data.

![](/api/attachments/6AYU9XPY/fulltext/images/e26ece09654c90ad84dc25155d7ea71bbc3c6398420c11c8229c48f29f48c951.jpg)  
Figure 9. Prediction Accuracy for Top-K% Low Entropy Users at Different Noise Rates

As demonstrated by these findings, our proposed mechanism consistently outperforms the alternative models in terms of computational and procedural efficiency, regardless of information types (number of CRs, call frequency, and call duration). Two factors contribute to the superior performance of our model relative to the alternatives. By utilizing the maximum likelihood mechanism, our social network-based inference model minimizes potential biases that may arise with the deterministic or simple probabilistic approaches, which have been prominent in research on BI and data quality. The dynamics embedded and nurtured in the fabric of social ties may enhance understanding of inference and validation trajectories. In addition, the entropy mechanism further improves the precision of our model by guaranteeing the quality of the inference mechanisms. In fact, combining the influence model with the entropy measure allows us to avoid potential caveats that can diminish accuracy when only one is utilized. In this respect, these two components are complementary mechanisms. Moreover, to develop comprehensive and rigorous inference models, we have combined several design-related frameworks and implementation techniques. For example, we integrated the query processing method, data mining techniques, social network analysis, and user profiling frameworks, all of which were used as building blocks to lay the foundation for our inference model.

The findings of this study provide managers with several practical insights into the strategic and tactical use of relational inference systems. While some managers focus on the functional and systematic aspects of BI systems, many are relatively inattentive to the quality of data that are processed through such systems. Profile-driven BI can be beneficial only when the systems' content truly reflects the identity and behavior of consumers in the first place. Therefore, data quality assessment and validation processes should be viewed as an integral part of any BI initiative.

Furthermore, the empirical regularities observed from the millions of actual call records offer corporate executives useful predictive guidelines for successfully planning and implementing a variety of marketing campaigns (e.g., promotion, market segmentation). For example, companies that rely heavily on social networks as their primary sources of profit (e.g., telecommunication service providers, online messenger companies, and social networking sites) can benefit from our social network-based approach, particularly to capitalize on relationship-based marketing (Crosby and Stephens 1987).

These companies can maximize their profits by bolstering their “friends and family” promotion programs. Additional discounts may stimulate users to communicate more frequently with their close friends, as well as to expand their circle of friends, while simultaneously increasing their call durations.

We also demonstrated that our system can improve a firm's operational efficiencies by reducing the proportion of users with uncertain age profiles. Results from the performance experiment reveal that our inference system can identify approximately 69.1 percent of users with accurate age profiles. This suggests that telecommunication service providers can significantly lower their opportunity costs by minimizing mis-targeting efforts and ineffective market segmentation. Accurate inference systems such as the one proposed here may enable marketers to fully utilize word-of-mouth referral strategies (Brown and Reingen 1987). When information about attractive promotional events is correctly delivered to targeted users, it may be rapidly dispersed within and across their network of peers (Aral and Walker 2011). Adolescent users, in particular, who may be more information and price sensitive than other users, tend to be actively involved in transmission of promotional events to their peers. In contrast, when promotion information is sent to inappropriate users, word-of-mouth will likely cease and further dissemination and propagation of the information will no longer occur. Consequently, inaccurate user profiles may hinder firms' ability to fully leverage word-of-mouth tactics and diminish associated potential profit opportunities.

## Limitations and Future Research

This study has several limitations. Due to internal policies and regulations of the data source, we obtained the data regarding the COs ranging from 9 to 38 years of age. Consequently, despite the large sample size, call patterns for other age groups are not represented. Mobile phone users over 40 years of age may exhibit dissimilar communication patterns from those included in our sample. Therefore, future studies should replicate and extend our work using samples that include a large sample of middle-aged and senior users. Another caveat involves the small amount of true profile data by which we manually validated the results of our inference model. It was a challenging task to find data that were both self-reported and physically verifiable; as a result, only 155 inspected profiles were available to test the model. Although our validation based on these verified profiles is statistically significant, future studies should consider increasing the number of available verified samples to enhance accuracy.

We also acknowledge that although age profile data alone provided fairly robust prediction outcomes, the model could be refined with additional demographic attributes, such as gender. This modification would facilitate the creation of more comprehensive social networks, which would improve prediction capability. For example, equation (5) can be expanded as follows:

$$
\begin{array}{l} \text {   Argmax   } _ {\mathrm{k}, \mathrm{g}} \Pi_ {i \in \mathcal {N} _ {i}} \mathrm{P} (\mathrm{r} _ {\mathrm{ij}} ^ {\prime} \text {   s   age   } = \mathrm{v} _ {\mathrm{j}} \& \mathrm{r} _ {\mathrm{ij}} ^ {\prime} \text {   s   gender   } = \mathrm{w} _ {\mathrm{j}} | \\ \mathrm{o} _ {\mathrm{i}} ^ {\prime} \text {   s   age   } = \mathrm{k} \& \mathrm{o} _ {\mathrm{i}} ^ {\prime} \text {   s   gender   } = \mathrm{g}) \end{array}
$$

where $w_{j}$ and $g \in \{male, female\}$ . Note that our method operates effectively regardless of the data format; continuous (e.g., age) or discrete (e.g., gender). This extension allows accurate prediction of the gender of a given CO when his or her age is known. Furthermore, we can infer a particular CO's age and gender simultaneously when neither is known with certainty. In the present study, the model's parsimony has been a priority, possibly at the expense of functional diversity. Therefore, we encourage future BI research to incorporate more diverse demographic characteristics to extend and augment the current study's approach.

Regarding its practical relevance and generalizability, our inference paradigm can be applied conceptually and mechanically to a wide range of social contexts. For example, our approach can be useful when members of online social networks or political groups do not share identifying information with other users. Recently, Thelwall (2009) demonstrated the presence of strong homophily for ethnicity, religion, age, country, marital status, attitude toward children, and sexual orientation in major social network sites (SNS). By applying our inference model and entropy mechanism, marketers are empowered to precisely ascertain SNS users' demographic characteristics and effectively facilitate strategic campaigns for targeting, branding, and promotions on social media platforms. Furthermore, online social financing platforms (e.g., Prosper.com), in which members lend and borrow small amounts of money from other members in the community, can also potentially benefit from our inference system. Peer-to-peer financing carries several inherent risks, such as anonymity-based transactions, high credit defaults, and limited legal protection. Recent research (e.g., Lin et al. 2009) has attempted to predict the credit rating of social financing borrowers on the basis of the credit scores of the friends in their social circles. However, no comprehensive mechanism has been suggested to determine the quality of friends' networks or the credit risk associated with borrowers. To address this need, our approach provides an initial vantage point from which lenders can systematically evaluate the credibility of borrowers with greater certainty. Future studies utilizing our inference model and entropy measure can elaborate further on these marketing- and finance-related issues that have become increasingly prevalent in a variety of online social platforms.

Finally, our mechanism can also be used to predict consumers' demographics based on their product purchases. Several product categories (e.g., clothes, music, baby products, and health and personal care items) are demographic-sensitive. The purchase of these products may provide information about the purchasers' demographic identities, such as age and gender. In addition, the proposed approach can offer illuminating insights regarding the identification of potential customers in the context of social commerce (e.g., Groupon), in which social media may stimulate a pattern of collective buying among multiple consumers. For example, if information is available about both purchase history and social network activities for individual customers, a particular user's purchase interest can be inferred from those of his or her neighbors in the SNS. Although further refinement and verification are necessary, our inference mechanism can offer participating retailers functional guidelines and prescriptions for attracting and retaining consumers, enabling them to analyze the network of consumers who purchase the same products. This is a relevant and timely area of research, as social commerce is rapidly emerging as a popular commercial platform.

Despite its wide range of applications, however, our model's results and insights are legitimate only when the presence of a particular homophily is verified both theoretically and empirically. More specifically, prior to implementation, a given social attribute of interest must be fully identified theoretically and substantiated empirically by the data. Otherwise, any predictions or inferences manifested through the proposed method have no foundation on which to base their accuracy and usefulness. An extensive body of literature in sociology has demonstrated various homophily propensities driven by individual demographics, such as age, gender, race/ethnicity, and education (e.g., Bott 1928; Loomis 1946), and also by psychological attributes like intelligence, attitudes, and aspirations (e.g., Almack 1922; Richardson 1940). Lazarsfeld and Merton (1954) classified these as status homophily and value homophily, respectively. Consequently, scholars who seek to build on our approach should be familiar with the status and value homophily attributes that are completely supported by both theory and data. Finally, regarding the precision of our inference mechanism, the simulation experiment conducted here suggests that increasing the number of neighbors and decreasing data noise can substantially enhance the model's accuracy. Future research in this domain should provide a finer level of empirical evidence as to the individual effects of these factors and their interactions.

## Conclusion

Self-reported profile data are prone to various forms of falsification, which often severely threatens the integrity of BI within and across firm boundaries. To alleviate this recurring dilemma, business managers and analysts need systematic approaches that enable them to accurately evaluate the quality of self-administered data. The present study addressed this need by presenting a novel inference model that utilizes social network insights. Empirical analysis of over 20 million actual communication calls revealed that our relational inference model outperformed the traditional systems, such as the weighted average and simple relational classifier methods. Our findings also suggest that entropy assessment plays an important role in further enhancing both the capacity and capability of our inference model.

In order to maximize the benefits from BI systems, organizations must be proactively involved in improving data quality. To elicit trustworthy self-reported responses from users, firms should enact effective reward systems. However, the institution of such incentive systems can not be the perfect solution, as many consumers will continue supplying inaccurate profile information due to increased security threats and privacy concerns. Therefore, it is no longer an option for organizations to institute data quality assurance systems as a critical component of their BI initiatives. Managers should be also mindful that BI systems with limited assurance capabilities will result in business impotence, rather than business intelligence.

## Acknowledgments

The authors are grateful to the special issue editors, the associate editor, and the anonymous reviewers for their valuable suggestions. All errors are the authors' own. Soon-Young Huh was the corresponding author.

This research was supported by the Business Start-Ups Growth Support Program (Social Mining Based Multi-Purpose Recommendation System) funded by the Small and Medium Business Administration, Korea. The work described in this paper was partially supported by a grant from City University of Hong Kong (Project No. 7200265).

## References

Adomavicius, G., and Tuzhilin, A. 2005. "Toward the Next Generation of Recommender Systems: A Survey of the State-of-the-Art and Possible Extensions," IEEE Transactions on Knowledge and Data Engineering (17), pp. 734-749.

Almack, J. C. 1922. “The Influence of Intelligence on the Selection of Associates,” School and Society (16), pp. 529-530

Anderson-Lehman, R., Watson, H. J., Wixom, B. H., and Hoffer, J. A. 2004. “Continental Airlines Flies High with Real-Time Business Intelligence,” MIS Quarterly Executive (3:4), pp. 163-176.

Aral, S., and Walker, D. 2011. “Creating Social Contagion Through Viral Product Design: A Randomized Trial of Peer Influence in Networks,” Management Science (57:9), pp. 1623-1639.

Ayanso, A., Goes, P. B., and Mehta, K. 2009. “A Cost-Based Range Estimation for Mapping Top-K Selection Queries Over Relational Databases,” Journal of Database Management (20:4), pp. 1-25.

Bailey, A. D., Jr., Duke, G. L., Gerlach, J., Ko, G., Meservy, R. D., and Whinston, A. B. 1985. "TICOM and the Analysis of Internal Controls," Accounting Review (60:2), pp. 186-211.

Benford, F. 1938. “The Law of Anomalous Numbers,” Proceedings of American Philosophical Society (78:4), pp. 551-572.

Bernard, H. R., Killworth, P., Kronenfeld, D., and Sailor, L. 1984. "The Problem of Informant Accuracy: The Validity of Retrospective Data," Annual Review of Anthropology (13), pp. 495-517.

Bott H. 1928. “Observation of Play Activities in a Nursery School,” Genetic Psychology Monographs (4), pp. 44-88

Brown, J. J., and Reingen, P. H. 1987. “Social Ties and Word-of-Mouth Referral Behavior,” Journal of Consumer Research (14:3), pp. 350-362.

Bruno, N., Chaudhuri, S., and Gravano, L. 2002. “Top-K Selection Queries Over Relational Databases: Mapping Strategies and Performance Evaluation,” ACM Transactions on Database Systems (27:2), pp. 153-187.

Byrne, D. 1971. “The Ubiquitous Relationship: Attitude Similarity and Attraction,” Human Relations (24:3), pp. 201-207.

Carslow, C. 1988. “Anomalies in Income Numbers: Evidence of Goal Oriented Behavior,” The Accounting Review (63), pp. 321-327.

Crosby, L. A., and Stephens, N. 1987. “Effects of Relationship Marketing on Satisfaction, Retention, and Prices in the Life Insurance Industry,” Journal of Marketing Research (24), pp. 404-411

Cui, G., Wong, M. L., and Lui, H. 2006. “Machine Learning for Direct Marketing Response Models: Bayesian Networks with Evolutionary Programming,” Management Science (52:4), pp. 597-612.

Dasgupta, K., Singh, R., Viswanathan, B., Chakraborty, D., Mukherjea, S., Nanavati, A. A., and Joshi, A. 2008. “Social Ties and Their Relevance to Churn in Mobile Telecom Networks,” in Proceedings of the 11 $^{th}$ International Conference on Extending Database Technology: Advances in Database Technology, Nantes, France, March 25-30, pp. 668-677.

Deckert, J., Myagkov, M., and Ordeshook, P. 2010. “The Irrelevance of Benford’s Law for Detecting Fraud in Elections,” Caltech/MIT Voting Technology Project Working Paper No. 9 (http://www.vote.caltech.edu/drupal/node/327).

Diekmann, A. 2007. “Not the First Digit! Using Benford’s Law to Detect Fraudulent Scientific Data,” Journal of Applied Statistics (34), pp. 321-329.

Eckerson, W. W. 2002. “Achieving Business Success Through a Commitment to High Quality Data,” TDWI Data Quality Report Series, The Data Warehousing Institute, Renton, WA.

English, L. 1999. Improving Data Warehouse and Business Information Quality, New York: John Wiley & Sons.

Fischer, C. S. 1977. Networks and Places: Social Relations in the Urban Setting, New York: Free Press, 1977.

Fisher, C. W., and Kingma, D. R. 2001. “Criticality of Data Quality as Exemplified in Two Disasters,” Information & Management (39:2), pp. 109-116.

Gupta, N., and Beehr, T. A. 1982. “A Test of the Correspondence Between Self-reports and Alternative Data Sources about Work Organizations,” Journal of Vocational Behavior (20), pp. 1-13.

Hill, S., Provost, F., and Volinsky, C. 2006. “Network-Based Marketing: Identifying Likely Adopters via Consumer Networks,” Statistical Science (21:2), pp. 256-276.

Jiang, Z., Sarkar, S., De, P., and Dey, D. 2007. “A Framework for Reconciling Attribute Values from Multiple Data Sources,” Management Science (53:12), pp. 1946-1963.

Kamakura, W. A., Wedel, M., Rosa, R. D., and Mazzon, J. A. 2003. “Cross-Selling Through Database Marketing: A Mixed Data Factor Analyzer for Data Augmentation and Prediction,” International Journal of Research in Marketing (20:1), pp. 45-65.

Kotler, P., and Armstrong, G. 1999. Principles of Marketing (8 $^{th}$ ed.), Englewood Cliffs, NJ: Prentice-Hall International.

Krishnan, R., Peters, J., Padman, R., and Kaplan, D. 2005. “On Data Reliability Assessment in Accounting Information Systems,” Information Systems Research. (16:3), pp. 307-326.

Kumar, R., Novak, J., Raghavan, P., and Tomkins, A. 2004. "Structure and Evolution of Blogspace" Communications of the ACM (47:12), pp. 35-39.

Lazarsfeld, P. F., and Merton, R. K. 1954. “Friendship as Social Process: A Substantive and Methodological Analysis,” in Freedom and Control in Modern Society, M. Berger, T. Able, and C. Page (eds.), New York: Van Nostrand.

Lee, Y. W. and Strong, D. M. 2003. “Knowing-Why About Data Processes and Data Quality,” Journal of Management Information Systems (20:3), pp. 13-39.

Leskovec, J., and Horvitz, E. 2008. “Planetary-Scale View on a Large Instant-Messaging Network,” in Proceedings of the 17 $^{th}$ International Conference on World Wide Web, New York: ACM, pp. 915-924.

Lin, C. 2002. “Segmenting Customer Brand Preference: Demographic or Psycho-Graphic,” Journal of Product & Brand Management (11:4), pp. 249-268.

Lin, M., Prabhala, N. R., and Viswanathan, S. 2009. “Can Social Networks Help Mitigate Information Asymmetry in Online Markets?” in Proceedings of the 30 $^{th}$ International Conference on Information Systems, Phoenix, AZ.

Lin, S., Gao, J., Koronios, A., and Chanana, V. 2007. “Developing a Data Quality Framework for Asset Management in Engineering

Organisations," International Journal of Information Quality (1), pp. 100-126.

Loomis, C. P. 1946. “Political and Occupational Cleavages in a Hanoverian Village,” Sociometry (9), pp. 316-333.

Louch, H. 2000. “Personal Network Integration: Transitivity and Homophily in Strong-Tie Relations,” Social Network (22), pp. 45-64.

Macskassy, S. A., and Provost, F. 2007. “Classification in Networked Data: A Toolkit and a Univariate Case Study,” Journal of Machine Learning Research (8), pp. 935-983.

Marsden P.V. 1988. “Homogeneity in Confiding Relations,” Social Networks (10), pp. 57-76.

McPherson, M., Smith-Lovin, L., and Cook, J. M. 2001. “Birds of a feather: Homophily in social networks,” Annual Review of Sociology (27), pp. 415-444.

Mikkelsen, G., and Aasly, J. 2005. “Consequences of Impaired Data Quality on Information Retrieval in Electronic Patient Records,” International Journal of Medical Informatics (74:5), pp. 387-394.

Nigrini, M. J. 1996. “A Taxpayer Compliance Application of Benford’s Law,” The Journal of the American Taxpayer Association (18), pp. 72-91.

Palmisano, C., Tuzhilin, A., and Gorgoglione, M. 2007. “User Profiling with Hierarchical Context: An E-Retailer Case Study,” in Proceedings of the 6 $^{th}$ International and Interdisciplinary Conference on Modeling and Using Context, Berlin: Springer-Verlag, pp. 369-383

Park, S., Han, S., Huh, S., and Lee, H. 2009. “Preprocessing Uncertain User Profile Data: Inferring User’s Actual Age from Ages of the User’s Neighbors,” in Proceedings of the 25 $^{th}$ IEEE International Conference on Data Engineering, Shanghai, China, March 29-April 2, pp. 1619-1624.

Peterson, R. 1984. “Asking the Age Question: A Research Note,” The Public Opinion Quarterly (48:1), pp. 379-383

Podsakoff, P. M., and Organ, D. W. 1986. “Self-Reports in Organizational Research Problems and Prospects,” Journal of Management (12:4), pp. 531-544.

Ramberg, J., and Schmeiser, B. 1972. “An Approximate Method for Generating Symmetric Random Variables,” Communications of the ACM (15:11), pp. 987-990.

Redman, T. C. 1995. “Improve Data Quality for Competitive Advantage,” Sloan Management Review (36:2), pp. 99-107.

Redman, T. C. 1998. “The Impact of Poor Data Quality on the Typical Enterprise,” Communicatinos of ACM(41:2), pp. 79-82.

Redman, T. C. 2004. “Data: An Unfolding Quality Disaster,” Information Management and SourceMedia, Inc. (http://www.information-management.com/issues/20040801/1007211-1.html).

Richardson, H. M. 1940. “Community of Values as a Factor in Friendships of College and Adult Women,” Journal of Social Psychology (11), pp. 303-312.

Roberts, R. 1995. “Can Self-Reported Data Accurately Describe the Prevalence of Overweight?” Public Health (109), pp. 275-284

Schräpler, J.-P., and Wagner, G. G. 2005. “Characteristics and Impact of Faked Interviews in Surveys: An Analysis of Genuine

Fakes in the Raw Data of SOEP," Allgemeines Statistisches Archive (89:1), pp. 7-20.

Shannon, C. 1948. “A Mathematical Theory of Communication” The Bell System Technical Journal (27:July/October), pp. 379-423, 623-656 (corrected reprint available at http://cm.bell-labs.com/cm/ms/what/shannonday/shannon1948.pdf).

Shaw, M. E. 1976. Group Dynamics: The Psychology of Small Group Behavior ( $2^{nd}$ ed.), New York: McGraw-Hill.

Shrum, W., Cheek, N. H., Jr., and Hunter, S. M. 1988. “Friendship in School: Gender and Racial Homophily,” Sociology of Education (61:4), pp. 227-239.

Swanson, D., Cho, M., and Eltinge, J. 2003. “Detecting Possibly Fraudulent or Error-Prone Survey Data Using Benford’s Law,” in Proceedings of the Section on Survey Research Methods, American Statistical Association, pp. 937-941.

Tajfel, H., and Turner, J. 1979. “An Integrative Theory of Intergroup Conflict,” in The Social Psychology of Intergroup Relations, W. G. Austin, S. Worchel (eds.), Monterey, CA: Brooks-Cole, pp. 94-109.

Thelwall, M. 2009. “Homophily in MySpace,” Journal of the American Society for Information Science and Technology (60:2), pp. 219-231

Turner, J. C., Hogg, M. A., Oakes, P. J., Reicher, S. D., and Wetherell, M. 1987. Rediscovering the Social Group: A Self-Categorization Theory, Oxford, England: Basil Blackwell.

Wang, B., Jia, Y., and Han, W. 2009. “Effective Feature Selection on Data with Uncertain Labels,” Proceedings of the 25 $^{th}$ IEEE International Conference on Data Engineering, Shanghai, China, March 29-April 2, pp. 1657-1662.

Wang, R. Y., and Strong, D. 1996. “Beyond Accuracy: What Data Quality Means to Data Consumers,” Journal of Management Information Systems (12:4), pp. 5-34.

Watson, H. J., and Volonino, L. 2003. “Customer Relationship Management at Harrah’s Entertainment,” in Decision Making Support Systems: Achievements, Trends and Challenges for the New Decade, M. Mora, G. A. Forgionne, and J. N. Gupta (eds.), Hershey, PA: IGI Publishing, pp.157-172.

Wixom, B., and Watson, H. 2010. “The BI-Based Organization,” International Journal of Business Intelligence Research (1:1), pp. 13-28.

## About the Authors

Sung-Hyuk Park is a visiting researcher at New York University's Stern School of Business. He received a B.S. degree in Applied Mathematics from Korea Advanced Institute of Science and Technology (KAIST), and a Ph.D. in Management Engineering from the KAIST Business School. He has presented his research at international conferences such as IEEE's International Conference on Data Engineering and the Hawaii International Conference on System Sciences. His research interests include business intelligence, large data analysis, social network service, and customer relationship management (CRM) systems.

Soon-Young Huh is a professor of Management Information Systems in the School of Business at KAIST. He received a B.S. degree in electronics engineering from Seoul National University, an M.S. degree from KAIST, and a Ph.D. from the Anderson Graduate School of Management at University of California, Los Angeles. He has published articles in such journals as Decision Sciences, Decision Support Systems, Omega, Journal of Database Management, and Journal of Systems and Software. His research deals with CRM systems, business intelligence, social network, web-based recommendation systems, and intelligent query answering system using XML and knowledge abstraction hierarchy.

Wonseok Oh is a professor of Information Systems in the School of Business at Yonsei University. He received his Ph.D. in Information Systems from the Stern School of Business at New York University. His research interests include network theory, social media, IT outsourcing, business value of information systems, and economic aspects of e-commerce. His research has been published in Information Systems Research, International Journal of Electronic Commerce, Journal of Management Information Systems, Journal of Strategic Information Systems, MIS Quarterly, and Management Science, and is forthcoming in Production and Operations Management.

Sang Pil Han is an assistant professor in the Information Systems Department at the City University of Hong Kong. He was a postdoctoral researcher at Stern School of Business, New York University. He received his doctoral degree from Korea Advanced Institute of Science and Technology Business School. His research interests include economics of mobile technology, economic value from content in spaces mediated by social media, consumer behavior in social networks, and economic aspects of e-commerce. His papers have been published or accepted in Management Science, MIS Quarterly, and Telecommunications Policy, among others.
