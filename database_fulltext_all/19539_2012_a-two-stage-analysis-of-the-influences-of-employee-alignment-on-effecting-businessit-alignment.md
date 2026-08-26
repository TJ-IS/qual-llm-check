---
otero_id: 19539
otero_key: "WVAAZPUY"
title: "A two-stage analysis of the influences of employee alignment on effecting business–IT alignment"
authors: "T.C. Wong; Shing-Chung Ngan; Felix T.S. Chan; Alain Yee-Loong Chong"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.03.008"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A two-stage analysis of the in<sup>fl</sup>uences of employee alignment on effecting business–IT alignment

T.C. Wong <sup>a,1</sup>, Shing-Chung Ngan <sup>a,</sup>⁎, Felix T.S. Chan <sup>b,2</sup>, Alain Yee-Loong Chong <sup>b,3</sup>

<sup>a</sup> Dept. of Systems Engineering and Engineering Management, City University of Hong Kong, 83 Tat Chee Avenue, Kowloon Tong, Hong Kong <sup>b</sup> Department of Industrial and Systems Engineering, The Hong Kong Polytechnic University, Hung Hom, Hong Kong

## a r t i c l e i n f o

Article history: Received 19 May 2011 Received in revised form 28 November 2011 Accepted 27 March 2012 Available online 4 April 2012

Keywords: Employee alignment Business–IT alignment PC-algorithm Neural network

## a b s t r a c t

The in<sup>fl</sup>uence of employee alignment orientations on successful implementation of business–IT alignment is investigated. Based on survey data collected from employees of Indonesian manufacturing companies, a twostage approach is applied (i) to discover the connectivity relations among business–IT alignment and four aspects of employee alignment orientations, and then (ii) to measure the relative in<sup>fl</sup>uence of each aspect onto one another. Employee communication is deemed to have the most direct contribution to business–IT alignment. Meanwhile, the connectivity relations show exactly how employee alignment orientations in<sup>fl</sup>uence business–IT alignment.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

The importance of utilizing information technologies (IT) as part of a strategic business toolset is well recognized in organizations nowadays, as higher customer expectations, escalating competitions, and larger supply-to-demand ratios all create severe challenges for enterprises which strive to survive and prosper in the increasingly globalized business eco-systems. Used effectively, IT can provide competitive advantages in supporting business needs and objectives [13]. However, the successful implementation of IT in organizations is highly non-trivial. In fact, most companies have dif<sup>fi</sup>culties in achieving and sustaining the long term bene<sup>fi</sup>ts from IT implementations, and for these companies, a main issue is how IT and their businesses can be ef<sup>fi</sup>ciently and effectively aligned [33–35]. Broadly de<sup>fi</sup>ned, the business–IT alignment is the application of IT in an appropriate and timely way, in harmony with the strategies, goals and needs of the business [33]. While the signi<sup>fi</sup>cance of business–IT alignment in improving business performance and marketplace competitiveness has been well recognized since three decades ago [37,39,48], it remains persistently dif<sup>fi</sup>cult in realizing this alignment in practice. A chief reason for the dif<sup>fi</sup>culties is (i) the dynamic nature of both the business strategies of a company and the continuously evolving available technologies and (ii) the interdependencies between IT and various business operations. Changes in IT technologies will require adjustments in business operations and vice versa. In other words, attaining and maintaining of business–IT alignment is a co-evolutionary process, requiring substantial and coordinated efforts from both the business and the IT professionals of a company in constantly adapting to changes [3].

In search of methods to improve the business–IT alignment, many practitioners and academics have focused on organization factors, such as business and IT managers’ relationships and their knowledge about each other's domain, top management commitment to the strategic use of IT, an organization's enterprise architecture, and the IT governance structures [15,23,34,54,55]. On the other hand, employees of a company should be among the most important stakeholders in developing IT and/or business strategy [11], even though paradoxically, in most organizational strategies, there is little understanding on the mechanisms by which individuals come to aligned with strategies [19]. Moreover, previous studies on business–IT alignment have been conducted exclusively in developed nations where less employees’ resistance against adopting IT strategies is expected, when compared to developing nations where the employees are comparatively new to IT implementation and might resist the idea of strategic IT implementations.

Thus, in bridging the gap in existing literatures, Chong et al. [11] investigated the relationships between employee alignment and business–IT alignment of organizations based on survey data obtained from 30 Indonesian manufacturing companies. Speci<sup>fi</sup>cally, Chong et al. [11] studied the relationships between employee alignment (composed of the following four factors: 1. employee trust, 2. communications on business–IT strategies to employees, 3. employee commitment to business–IT strategies, and 4. employee knowledge) and business–IT alignment. The regression model they assumed consisted of having business–IT alignment as the dependent variable, and the four employee alignment factors as the independent variables. By perform ing hypothesis testing based on this model, factors 1, 2 and 4 were found to have signi<sup>fi</sup>cant and positive relationship with business–IT alignment, while factor 3 was not.

In the present article, we carry out a further investigation into the relationships among the employee alignment factors in in<sup>fl</sup>uencing business–IT alignment, based on the survey data set described in [11]. As mentioned above, Chong et al. [11] conjectured a research model, and then used a con<sup>fi</sup>rmatory approach in testing their model. On the other hand, a recent paper [58] has demonstrated that the application of a two-stage exploratory approach, based on the PC-algorithm and neural network, can reveal non-trivial information about the connectivity relations among the constructs of a research domain of interest, directly from the data. This is consistent with the recommendation by Shmueli and Koppius [50], that one way to move information systems research forward is to employ predictive analytics methods such as neural network in order to examine and analyze observations in research models. Thus, the aim of this article is to contribute to the further understanding of how the various employee alignment factors in<sup>fl</sup>uence business–IT alignment, by applying the method described in [58] to acquire a map showing the web of relations among these factors. In other words, instead of conjecturing a path model as was done in [11], we apply the two-stage analysis method of [58] to the same data set described in [11] in order to algorithmically obtain a connectivity model that captures the phenomena underlying business–IT alignment. Our approach allows us to capture complex underlying patterns and relationships, and enable us to improve existing explanatory statistical models such as the one by Chong et al. [11]. A highlight of this research is that employee communication takes on a central role in enabling business–IT alignment, while the other factors can have signi<sup>fi</sup>cant but indirect contributions to the alignment. Arguably, this information is not easily obtainable from con<sup>fi</sup>rmatory analyses.

In the rest of this article, we will describe the main constructs of the present business–IT alignment study in Section 2. Section 3 will describe both the survey and the data analysis methodologies. In Sections 4 and 5, we will present and discuss the analysis results. A conclusion and suggestions for future research will be provided in Section 6.

## 2. Theoretical background

## 2.1. The alignment of business and IT strategies

As discussed in the Introduction, business–IT alignment is the appropriate application of information technologies in supporting a company's strategies, goals and needs. More speci<sup>fi</sup>cally, the appropriateness of IT application to a business can be determined by whether (i) the IT strategy is aligned to a company's broader goals and objectives, (ii) the IT services are delivered ef<sup>fi</sup>ciently and effectively in meeting a company's needs, and (iii) the IT offerings and services are aligned to the business goals [53]. In the case of misalignment, with the lack of harmony in objectives and culture and possibly with a mutual ignorance of each other's body of knowledge, business and IT professionals in an organization will <sup>fi</sup>nd it dif<sup>fi</sup>cult to cooperate effectively. On the other hand, the full harmonization of the IT and business components may lead to improvement in the <sup>fi</sup>nancial return from IT capital investment, lessening of con<sup>fl</sup>icts between business and IT strategies, and ultimately achieving competitive advantage [46].

Given the consequential bene<sup>fi</sup>ts of a successful business–IT alignment, there are tremendous interests in identifying the interdependencies between a successful alignment and its key driving factors. Indeed, as discussed in Section 1, many organizational factors have been investigated, but most of the studies tend to focus on the hardware side, such as the company size, IT capital investment, and resource allocation from top management. However, in aligning business and IT components, the software side of the organization, i.e. the employees involved in the processes, is just as crucial, if not more so. In fact, Drucker [18] has long pointed out that individuals within the company must behave in a contributory manner to support the strategic goals of the company, in order for strategic alignment of organizations to occur. One expects that business–IT alignment is no exception. In this connection, the role of employee alignment in relation to successful business–IT alignment much deserves to be studied and illuminated.

## 2.2. Employee alignment

In this study and also in [11], the aspects of employee alignment considered in connection to business–IT alignment are perceived employee trust, perceived communications on business–IT strategies to employees, perceived employee commitment to business–IT strategy, and perceived employee knowledge. In this article, by employee alignment, we refer to the alignment orientation of non-management level employees. We describe the four aspects of employee alignment in the following sub-sections.

## 2.2.1. Perceived employee trust

Generally speaking, trust in an organizational context consists of trust between the employees and their supervisors, trust of the employees with their organizations, as well as trust among the peers. Trust is present when an employee voluntarily becomes vulnerable to another in pursuing a mutually bene<sup>fi</sup>cial outcome [17,19]. As past studies have pointed out, the presence of trust is important for the effective operation and performance of an organization [21,56], as well as for enhancing employees’ organizational commitment and work attitudes [17]. Given the general positive in<sup>fl</sup>uences of employee trust on a company, Reich and Benbasat [49] have suggested that the role of trust in business–IT alignment should be examined in future research. Indeed, trust between the business and the IT departments would be one of the fundamental factors to alignment.

In the business–IT alignment study of [11], the trust that the authors focused on is employee trust, which involves employees’ trusts on each other, on their managers, and on the business–IT strategies proposed by their top management.

## 2.2.2. Perceived employee communication

Communication in the business–IT alignment context is the process of exchanging information, knowledge and ideas among the IT and business professionals, in ensuring that the business and IT sides have mutual understanding of the business and IT environments, and of the organization's strategies. A successful communication occurs when the receiver completely understands the information he or she received from the sender [1]. Previous studies have con<sup>fi</sup>rmed the importance of complete, accurate and direct communications in securing employees’ action in favor of company goals [44], and the importance of communication between business and IS executives in effecting business–IT alignment [49]. Several researchers [1,51] have pointed out that by understanding an organization's strategies through communications with the management, employees will feel involved thus increasing the probability of successful strategy implementation. Thus, the role of employee communication as a component of employee alignment has been examined in [11], and will be further investigated in the present study.

## 2.2.3. Perceived employee commitment

Broadly de<sup>fi</sup>ned, commitment is one's attachment and willingness to support his or her organization [41]. The speci<sup>fi</sup>c term goal commitment refers to an individual's determination and attachment to reach a goal [32]. Obviously, goal commitment can be extended to include commitment to a strategic goal, as a strategy is predominantly goal oriented. In their studies focusing on managers, [42,59] highlighted the importance of the commitment of the managers to the strategies of an organization. [11] argued that with our current business environment involving more team work, employees’ commitment to the strategy of their company is increasingly important, as a committed manager who <sup>fi</sup>nds that his team members are not committed to the company or strategy will have dif<sup>fi</sup>culties in securing the successful implementation of the strategies.

Researchers have found that when introducing new technologies, a hurdle to the successful implementation of the technologies is the lack of employee commitment [7,38]. The decline in employee commitment in turn is often driven by their resistance to technological change [5,8]. In fact, [9] pointed out that when implementing business–IT strategies, the risk is that employees might resist the adoption of technology and is not committed to the business–IT strategy. Thus, employee commitment is one of the employee alignment factors considered in [11] as well as in the present article.

## 2.2.4. Perceived employee knowledge

An employee is said to possess the organization's strategic knowledge when his or her thorough understanding of the strategies is consistent with those who created the strategies [11]. Employees’ possession of strategic knowledge is important because it facilitates the employees to commit to an organization's strategic goals [19]. In the context of business–IT alignment, Teo and Ang [54] noted that a major factor contributing to a successful alignment is the business strategies knowledge of the IT executives. On the other hand, [11] pointed out that the relation between employee knowledge and business–IT alignment has been rarely investigated, although there were studies [19,47] on the relation between employee knowledge and business strategies or strategic change. Thus, [11] examined the effect of how employee knowledge in<sup>fl</sup>uences business–IT alignment, with the de<sup>fi</sup>nition of employee knowledge adapted from [19] as an employee's global understanding of the organization's business–IT strategies.

## 3. The proposed methodology

## 3.1. Survey methodology

The survey data set we focus on in the present article is obtained from a study described in [11] — the detail methods used for creating the survey instrument can be found in that paper. Concisely, non-executive level employees in the various departments of 30 manufacturing companies in Bandung, Indonesia, were the target population. Of the 500 hardcopy surveys distributed, 121 fully completed surveys were received. With respect to the research model of [11] as presented in Fig. 1, items measuring the constructs Employee Trust, Communications to Employees, Employee Commitment, Employee Knowledge and Business–IT Alignment (for brevity, these constructs herein denoted as Trust, Communications, Commitment, Knowledge and Business–IT Alignment respectively) were all adapted from the existing literatures – for Trust: [17]; for Communications: [44]; for Commitment: [6,12] and [42]; for Knowledge: [6,14] and [59]; <sup>fi</sup>nally, for Business–IT Alignment: [30]. The 5-point Likert Scale covering the range of opinions from “strongly disagree” to “strongly agree” was used for all items measuring the abovementioned constructs in the survey instrument. Tables 1 and 2 show the key statements of the questionnaire used and the demographic details of respondents respectively.

## 3.2. Exploratory analysis of the survey data

As discussed in Section 1, we utilize an analysis methodology that has been previously developed in [58] to analyze the business–IT alignment survey data set. Step 1 of the method consists of using the PC-algorithm to discover the connectivity relations among the constructs discussed in Section 3.1, while Step 2 employs the neural network to determine the connectivity strength across the connected constructs. For completeness, we summarize the qualitative features of the two-stage method below, whereas the computational details of the method can be found in [58] and the references therein.

![](/api/attachments/WVAAZPUY/fulltext/images/996b2e8dd8c804569f552f4b963afbf3274f28c4237fad6b312e60989082164d.jpg)  
Fig. 1. The research model.

3.2.1. Using the PC-algorithm to discover connectivity relations among the constructs

The PC-algorithm [29] is a computationally ef<sup>fi</sup>cient procedure for calculating conditional correlation, which enables the identi<sup>fi</sup>cation of connectivity relations among the constructs $\{ C _ { 1 } , C _ { 2 } , . . , C _ { \mathrm { N } } \}$ of a given research domain. The key ideas of the algorithm are as follows: (i) Given the observed values of these constructs from the data set, an initial graph G is built, such that any pair of constructs, being treated as nodes, are directly connected with an edge if their standard correlation is signi<sup>fi</sup>cantly non-zero; (ii) The algorithm then selects an ordered pair of constructs $C _ { i }$ and $C _ { j }$ that are directly connected in G. With adj (C )denoting the set of constructs that are directly connected to $C _ { i } ,$ if there is a subset of the constructs $V _ { s } \subseteq a d j ( C _ { i } ) \backslash \{ C _ { j } \}$ such that $C _ { \mathrm { i } }$ and $C _ { \mathrm { j } }$ become uncorrelated when conditioned on $V _ { s }$ (i.e. if $\rho _ { C _ { i } , \ C j | V s }$ is not signi<sup>fi</sup>cantly non-zero), then the edge between $C _ { i }$ and $C _ { j }$ is deleted from the graph G. Precisely, this computation is done by using the following formula recursively

$$
\rho_ {C _ {i}, C _ {j} \mid V _ {s}} = \frac {\rho_ {C _ {i} , C _ {j} \mid V _ {s} \backslash C _ {k}} - \rho_ {C _ {i} , C _ {k} \mid V _ {s} \backslash C _ {k}} \times \rho_ {C _ {j} , C _ {k} \mid V _ {s} \backslash C _ {k}}}{\sqrt {\left(1 - \rho_ {C _ {i} , C _ {k} \mid V _ {s} \backslash C _ {k}} ^ {2}\right) \left(1 - \rho_ {C _ {j} , C _ {k} \mid V _ {s} \backslash C _ {j}} ^ {2}\right)}}\tag{1}
$$

where $C _ { k }$ is any member of $V _ { s } ,$ , and the null hypothesis that $\rho _ { C _ { i } , C j | V s } 2 0$ is rejected if the corresponding z-value

$$
Z \left(C _ {i}, C _ {j} \mid V _ {s}\right) \equiv \frac {1}{2} \log \left(\frac {1 + \rho_ {C _ {i} , C _ {j}} \mid V _ {s}}{1 - \rho_ {C _ {i} , C _ {j}} \mid V _ {s}}\right)\tag{2}
$$

passes a predetermined threshold [2], i.e.

$$
\left| Z \left(C _ {i}, C _ {j} \mid V _ {s}\right) \right| > \Phi^ {- 1} \left(1 - \frac {\alpha}{2}\right) / \sqrt {n - | V _ {s} | - 3}\tag{3}
$$

where n is the number of samples, $| V _ { s } |$ is the number of constructs in the $V _ { s } , \phi ^ { - 1 }$ is the inverse of the cumulative Gaussian distribution, and α is a preselected signi<sup>fi</sup>cance level; (iii) After iterating the edge testing/ deletion process of (ii) on all ordered pairs of constructs, a <sup>fi</sup>nal connectivity graph, termed the skeleton graph, is obtained. The skeleton graph has the interpretation rule that two constructs are connected in such a graph if and only if these two constructs remain correlated when conditioned on any subset of the remaining constructs. As a consequence, direct connectivity relation (existence of an edge between the two constructs) and indirect connectivity relation (existence of a chain of edges linking the two constructs) can be readily distinguished from a skeleton graph. An example skeleton graph is shown in Fig. 2. From this <sup>fi</sup>gure, D is directly connected to E, F and G. C and D are indirectly connected, via E. Another example of indirect connection is B and D, via C and E.

Table 1 Key statements of questionniare.

<table><tr><td>Perceived Organizational TrustWe believe in the strategies lay out by our senior management.When employees express their point of view, they will be truly heard.We trust each other to complete a job.We are encouraged to share our ideas and feelings with others.Conflicts in our views in company strategic directions will be dealt with in an appropriate and professional mannerIT strategies are an important part of business strategies.Business strategies can only be successful through a good support from IT strategies.We believe that our ideas will be heard.It is not a problem for us to provide ideas on feedbacks on companies&#x27; strategies.All employees are responsible and will perform their job regardless of their department.Perceived communications on business–IT strategies to employeesI am kept informed about major changes occurring within the companyInformation is shared in a timely manner from the companyI am kept informed about reasons behind company decisionsThe information I receive from the company is completeI am kept informed about major changes occurring within my business/ functionInformation is shared in a timely manner from my business/functionI am kept informed about reasons behind business/function decisionsI have the information needed to perform my job effectivelyThe information I receive from my business/function is completeMy business/function does a good job of communicating information to all employeesPerceived employee commitment to business–IT strategiesI am willing to put in a great deal of effort beyond that which is normally expected in order to help the business be successfulI am committed to the long term strategies set by my organization.I feel loyal to the businessI find my values and goals are compatible with the business&#x27; values and goalsI am proud to tell others that I am part of the businessThere is much to be gained by participating with the business on a long-term basisI agree with the business&#x27; goals, plans and policiesI really do care about the fate of the businessDeciding to be involved with the business has had a positive influence on my life.I understand and support decisions regarding the future of the businessPerceived knowledge on business–IT strategiesPeople in our organization frequently spend time discussing customers future needs, visions and companies&#x27; strategies.When people in our organization need information, they know who exactly to askThere are regular meetings between departments to discuss trends and developmentsWe keep a database of customer information, business and IT strategies that is easy to accessInformation about customer satisfaction is disseminated to all levels of our organizationWe encourage people with similar interest to work togetherWe manage to keep up to date with technological developments that could affect our businessInformation on new technological developments that affect our business is circulatedWe periodically review the likely effect of changes in technology on our customersWe are quick to decide on how to respond to changes in technologyBusiness–IT alignmentBusiness planners understand the value of IT to businessOur business plan specifies the contribution of IT to the businessBusiness plans revised whenever IT evolvesBusiness managers participate in IT planning processesIT personnel participate in business planningIT opportunities prioritized on basis of business objectivesWe revise IT plans whenever business evolvesIT personnel understand our business needsIT and business plans are prepared simultaneously</td></tr></table>

## 3.2.2. Neural computation of relative importance

In Fig. 2, a construct D is shown to be directly connected with constructs E, F and G. Depending on the business needs, D could be a critical factor of interest (say Business–IT Alignment) and one would like to determine the relative importance of the its directly connected factors (say Communication, Knowledge and trust) in in<sup>fl</sup>uencing the level of the critical factor. In the language of linear regression modeling, D can be treated as the output, and E, F and G as the inputs, with the resulting regression coef<sup>fi</sup>cients corresponding to the relative importance. A generalized approach is to employ the neural network as a nonlinear regression model for the three inputs (E, F and G) and the single output (D) as illustrated in Fig. 3. In the present study, we employ a neural network consisting of a base layer of input units, a middle layer of hidden units, and a layer of a single output unit. The numeric value of each hidden unit $H _ { k }$ is determined from the numeric values of the input units:

Demographic details of respondents.

<table><tr><td></td><td>Percentage (%)</td></tr><tr><td colspan="2">Number of Employees</td></tr><tr><td>Small: 5–19</td><td>34.7</td></tr><tr><td>Medium: 20–99</td><td>62.8</td></tr><tr><td>Large: 100 or more</td><td>2.5</td></tr><tr><td colspan="2">Annual Sales</td></tr><tr><td>Less than MYR 50,000</td><td>7.4</td></tr><tr><td>MYR 51,000 to 100,000</td><td>41.3</td></tr><tr><td>MYR 110,000 or more</td><td>51.2</td></tr><tr><td colspan="2">Education Level</td></tr><tr><td>Secondary</td><td>0</td></tr><tr><td>College</td><td>5</td></tr><tr><td>University</td><td>54.5</td></tr><tr><td>PhD/Master/Professional</td><td>40.5</td></tr><tr><td colspan="2">Job Post</td></tr><tr><td>Senior management</td><td>12.4</td></tr><tr><td>Administrative staff</td><td>22.3</td></tr><tr><td>Clerical staff</td><td>15.7</td></tr><tr><td>Factory workers</td><td>49.6</td></tr></table>

$$
H _ {k} = \sigma \left(a _ {0} ^ {k} + \sum_ {j = 1} ^ {M} a _ {j} ^ {k} I _ {j}\right)\tag{4}
$$

with

$$
\sigma (w) = \frac {1}{1 + e ^ {- w}}\tag{5}
$$

whereas the numeric value of the output unit is determined from the numeric values of the hidden units:

$$
\Theta = b _ {0} + \sum_ {k = 1} ^ {P} b _ {k} H _ {k}\tag{6}
$$

where σ(w) is the sigmoid function, I stands for the jth input unit, $H _ { k }$ stands for the kth hidden unit, Θ stands for the output unit, M is the number of the input units, and P is the number of the hidden units in the neural network. The standard feed-forward back-propagation algorithm is used to train the neural network, thus enabling the determination of appropriate values for the network parameters $\{ a _ { 0 } ^ { k } . . . , a _ { M } ^ { k } , b _ { 0 } . . . , b _ { P } \}$ with $k = 1 , . . , N$ [25]. Cross-validation is used to guard against over-<sup>fi</sup>tting the network to noise [24]. Meanwhile, the Change of Mean Square Error (CMSE) method [52], which has been found to be a robust approach for quantifying relative importance, is employed to compute the relative importance of E, F and G in in<sup>fl</sup>uencing D in the resulting nonlinear regression model. Qualitatively speaking, in the CMSE method, we compute the increase in the mean square prediction error (i.e. the socalled CMSE index) of the neural network after an input factor has been deleted from the input layer of that neural network. Hence, for the present example, the CMSE computation is done three times (one time with E and F kept and G deleted, another time with F and G kept and E deleted, and so on). The relative importance of each input factors is represented by the corresponding normalized CMSE index, illustrated in Section 4.2.

![](/api/attachments/WVAAZPUY/fulltext/images/84dbaa366b6b3830bc013b22b02812fb8b85ed8c96329c25f62412dea439a6ea.jpg)  
Fig. 2. An example skeleton graph.

![](/api/attachments/WVAAZPUY/fulltext/images/cb6fdc690447c21040a35faabcbabfae6041af582658fe4555ddec9a164ad2a5.jpg)  
Fig. 3. A neural network with three input units, four hidden units and a single output unit.

## 4. Results

## 4.1. The skeleton graph for the business–IT alignment survey data

Fig. 4 presents the revised model, obtained by carrying out the PCalgorithm on the survey data set (with a p-value threshold set at 0.05 for declaring a conditional correlation between two constructs signi<sup>fi</sup>cant) and then aggregating the results. Without the bene<sup>fi</sup>t of the data exploratory approach, the research model in [11] treated the construct business–IT alignment as the output variable, and the rest of the constructs as the input variables which might contribute to the alignment. In contrast, the revised model enables us to effectively disentangle the direct from the indirect connectivity relations. Specifically, among the <sup>fi</sup>ve constructs, Communication has the most direct connections with the other constructs (namely Trust, Knowledge and Business–IT Alignment) and can be regarded the hub of the skeleton graph. Comparing with the research model in [11], the PC-algorithm computation shows that Business–IT Alignment is directly connected with Communication and only indirectly connected with Knowledge, Trust and Commitment. The implications will be discussed in detail in Section 5.

In what follows, we will perform the relative importance calculations for the following relative importance (RI) models: (i) Communication treated as the output, with Trust, Knowledge and Business–IT Alignment as

![](/api/attachments/WVAAZPUY/fulltext/images/1cacc195e84cb7035bd6b59944f38e9133d38757c69de5e71458fd43a9556099.jpg)  
Fig. 4. The revised model.  
the inputs (Fig. 5a); (ii) Business–IT Alignment treated as the output, with Communication as the input (Fig. 5b); and (iii) Trust treated as the output, with Communication and Commitment as inputs (Fig. 5c), where $\Chi _ { 1 }$ is used to denote Trust, $X _ { 2 }$ for Communication, ${ \mathrm { X } } _ { 3 }$ for Commitment, ${ \mathrm { X } } _ { 4 }$ for Knowledge, and Y for Business–IT Alignment.

4.2. Relative importance calculations based on the neural network and CMSE analyses

As discussed in Section 3, the standard feed-forward backpropagation algorithm is employed to train the neural network, while cross-validation is employed to guard against over-<sup>fi</sup>tting of the neural network to noise. A neural network model is developed to each of the three RI models as shown in Fig. 6, with the size of hidden layer of each network model determined by the method described in [28], i.e. the number of units P in the hidden layer is taken as the average of the number of input units and the number of output units. Then, ten-fold cross-validation is performed (i.e. nine-tenth of the data was used in training the neural network, and the remaining onetenth was used in measuring the prediction accuracy of the trained network; since each tenth of the data set took turn to be the validation set, this training–validation process was repeated ten times) for each of our three network models. Speci<sup>fi</sup>cally, the Mean Absolute Percentage Error (MAPE) is used to measure the deviation of the neural network predicted outputs from the actual values in a validation set:

![](/api/attachments/WVAAZPUY/fulltext/images/5e3681e3abf3d0b14a9101c651b6c05d002692a01547a295c77623e0a880597d.jpg)  
Fig. 5. Three RI models.

![](/api/attachments/WVAAZPUY/fulltext/images/c8d6bfa2df5f2c04553454e67a2aaa9977ea5f023b33bc1d8ad3a08a796aef02.jpg)

![](/api/attachments/WVAAZPUY/fulltext/images/8b8ce5972dfcfb6f2bdc0a19d478a83638102f24a287bc460d16ac2c6f2d33f6.jpg)

![](/api/attachments/WVAAZPUY/fulltext/images/c725e7fd19d4319ec9ccae253b051ffd43b55b9342605b5d97b1215891be337a.jpg)  
Fig. 6. Three neural network models.

$$
M A P E _ {j} = \frac {1}{D _ {j}} \sum_ {i = 1} ^ {D _ {j}} \frac {\left| A _ {i , j} - E _ {i , j} \right|}{A _ {i , j}} \times 1 0 0\tag{7}
$$

where $D _ { j }$ is the number of samples in the jth validation set, $A _ { i , j }$ is the actual output value for the ith sample of the jth validation set, and $E _ { i , j }$ is the neural network predicted output value for that ith sample. The average cross-validated prediction error (ACVPE) is de<sup>fi</sup>ned as ∑ <sup>10</sup> MAPE /10. For the three network models, their ACVPEs are

6.54%, 7.09% and 7.4% respectively. Hence, all these neural networkbased nonlinear regression models (with error≤10%) can reliably capture the numeric relations between the respective inputs and outputs. The full cross-validation results for all three network models are reported in Tables 3–5.

To additionally verify that the method of choosing P as described in [28] indeed leads to good prediction performance, the above crossvalidation calculation is repeated for different P values. For example, Table 6 reports the average cross-validated prediction error of the <sup>fi</sup>rst network model with various P values. (The Pearson coef<sup>fi</sup>cients between the actual output values and the neural network predicted output values of the validation sets for the various P values are also computed and displayed in Table 6.) In general, the P value chosen according to the method described in [28] gives the best prediction performance, i.e. yielding a low ACVPE and a high Pearson coef<sup>fi</sup>cient.

As discussed in Section 3, in applying the CMSE method, we delete one input unit off an N-input-unit neural network models. We then train the resultant (N − 1)-input-unit network with ten-fold crossvalidation, and compute the increase in the mean square prediction error of the reduced network relative to the full network, obtaining the CMSE index for that input. We then rank the input with the largest CMSE index as the most important input, since its exclusion from the full neural network triggers the largest increase in the mean square prediction error and thus most deteriorates the prediction accuracy. Furthermore, the relative importance of each input is quanti<sup>fi</sup>ed by dividing the CMSE index of the input of interest by the sum of the CMSE indices of all the inputs in the underlying RI model, yielding a so-called normalized CMSE index. The results of the relative importance calculation are reported in Table 7. For ease of presentation, an overall RI model (Fig. 7) is presented to indicate all the connections between constructs and their associated relative importance onto others.

## 5. Discussions

## 5.1. Communication as a central construct of interest

From Fig. 7, Communication is the hub of the connectivity relations among the constructs, with direct connection with Trust, Knowledge and Business–IT Alignment. That trust is a basis for strong communications con<sup>fi</sup>rm <sup>fi</sup>ndings in the literature — certain level of mutual trust is important in enabling effective and free exchange of ideas, information and knowledge among various parties [10,27,36,45]. Regarding Knowledge, lack of common knowledge (i.e. those elements of knowledge common to all organizational members) can hinder communications among parties within a company. On the contrary, the availability of shared knowledge and shared meaning can enhance the level of sophistication and effectiveness in communications among employees, especially in the context of organizational learning [22,43,57]. Widely acknowledged, information technologies nowadays have become important tools in customer relationship management (CRM), supply chain management (SCM) and communications systems, among numerous other uses, enhancing the communication level of a company with its customers and suppliers and among the employees of a company. A direct bene<sup>fi</sup>t from implementing IT in an organization is that employees within and across functional units can be easily linked up, thus increasing the overall amount of communication [16].

Table 3  
The cross-validation results of the <sup>fi</sup>rst network model.

<table><tr><td rowspan="2">Test No.</td><td colspan="12">The first network model (P=2)</td><td rowspan="2">Average</td></tr><tr><td>E1</td><td>E2</td><td>E3</td><td>E4</td><td>E5</td><td>E6</td><td>E7</td><td>E8</td><td>E9</td><td>E10</td><td>E11</td><td>E12</td></tr><tr><td>1</td><td>1.02</td><td>9.10</td><td>4.74</td><td>5.44</td><td>7.04</td><td>1.80</td><td>2.44</td><td>1.77</td><td>12.35</td><td>3.05</td><td>4.67</td><td>1.56</td><td>4.58</td></tr><tr><td>2</td><td>4.97</td><td>15.36</td><td>8.47</td><td>10.24</td><td>10.87</td><td>10.41</td><td>0.79</td><td>9.45</td><td>12.79</td><td>6.46</td><td>0.40</td><td>2.63</td><td>7.74</td></tr><tr><td>3</td><td>5.18</td><td>12.80</td><td>33.17</td><td>22.59</td><td>9.24</td><td>22.60</td><td>4.69</td><td>1.14</td><td>3.97</td><td>4.12</td><td>3.87</td><td>4.28</td><td>10.64</td></tr><tr><td>4</td><td>4.18</td><td>18.08</td><td>2.02</td><td>2.17</td><td>0.00</td><td>7.18</td><td>0.41</td><td>21.92</td><td>12.89</td><td>4.20</td><td>0.23</td><td>1.10</td><td>6.20</td></tr><tr><td>5</td><td>8.53</td><td>4.57</td><td>1.93</td><td>0.55</td><td>2.06</td><td>9.58</td><td>1.80</td><td>2.11</td><td>4.53</td><td>2.69</td><td>6.96</td><td>6.49</td><td>4.32</td></tr><tr><td>6</td><td>1.37</td><td>3.02</td><td>0.75</td><td>16.05</td><td>2.21</td><td>0.00</td><td>7.62</td><td>3.68</td><td>1.62</td><td>15.65</td><td>5.25</td><td>7.79</td><td>5.42</td></tr><tr><td>7</td><td>4.43</td><td>4.64</td><td>3.75</td><td>6.23</td><td>8.64</td><td>2.29</td><td>36.42</td><td>1.69</td><td>26.74</td><td>10.03</td><td>2.40</td><td>2.24</td><td>9.12</td></tr><tr><td>8</td><td>7.79</td><td>11.94</td><td>4.88</td><td>9.35</td><td>0.48</td><td>2.69</td><td>5.54</td><td>2.54</td><td>4.92</td><td>0.89</td><td>0.27</td><td>10.46</td><td>5.15</td></tr><tr><td>9</td><td>6.93</td><td>17.66</td><td>40.94</td><td>2.81</td><td>7.05</td><td>10.79</td><td>0.82</td><td>5.51</td><td>0.60</td><td>3.28</td><td>1.59</td><td>7.24</td><td>8.77</td></tr><tr><td>10</td><td>5.18</td><td>4.51</td><td>2.86</td><td>0.12</td><td>4.58</td><td>4.47</td><td>6.40</td><td>1.17</td><td>2.82</td><td>4.99</td><td>2.27</td><td>2.60</td><td>3.50</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Mean</td><td>6.54</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>SD</td><td>2.39</td></tr></table>

Table 4  
The cross-validation results of the second network model

<table><tr><td rowspan="2">Test No.</td><td colspan="12">The second network model (P=2)</td><td rowspan="2">Average</td></tr><tr><td>E1</td><td>E2</td><td>E3</td><td>E4</td><td>E5</td><td>E6</td><td>E7</td><td>E8</td><td>E9</td><td>E10</td><td>E11</td><td>E12</td></tr><tr><td>1</td><td>4.01</td><td>12.29</td><td>2.91</td><td>0.83</td><td>0.60</td><td>0.75</td><td>3.24</td><td>0.69</td><td>9.29</td><td>1.69</td><td>3.47</td><td>0.68</td><td>3.37</td></tr><tr><td>2</td><td>2.81</td><td>20.70</td><td>17.39</td><td>15.03</td><td>11.15</td><td>1.98</td><td>6.02</td><td>14.03</td><td>1.61</td><td>2.93</td><td>6.02</td><td>3.72</td><td>8.62</td></tr><tr><td>3</td><td>6.79</td><td>5.14</td><td>28.04</td><td>19.44</td><td>6.44</td><td>19.44</td><td>9.61</td><td>2.01</td><td>21.04</td><td>5.58</td><td>4.47</td><td>8.43</td><td>11.37</td></tr><tr><td>4</td><td>10.46</td><td>1.32</td><td>33.01</td><td>24.95</td><td>19.57</td><td>10.28</td><td>8.46</td><td>56.21</td><td>1.86</td><td>6.25</td><td>10.80</td><td>7.12</td><td>15.86</td></tr><tr><td>5</td><td>8.11</td><td>2.12</td><td>3.10</td><td>0.56</td><td>0.09</td><td>11.17</td><td>2.52</td><td>2.70</td><td>6.05</td><td>0.92</td><td>1.48</td><td>7.00</td><td>3.82</td></tr><tr><td>6</td><td>8.50</td><td>4.57</td><td>0.96</td><td>6.17</td><td>5.05</td><td>8.51</td><td>5.95</td><td>8.50</td><td>8.51</td><td>0.89</td><td>1.66</td><td>1.08</td><td>5.03</td></tr><tr><td>7</td><td>0.65</td><td>6.76</td><td>34.36</td><td>11.03</td><td>4.44</td><td>15.06</td><td>1.96</td><td>13.67</td><td>23.35</td><td>0.57</td><td>9.27</td><td>13.10</td><td>11.18</td></tr><tr><td>8</td><td>3.34</td><td>0.82</td><td>4.44</td><td>3.20</td><td>4.63</td><td>10.06</td><td>7.47</td><td>4.49</td><td>0.89</td><td>1.84</td><td>5.13</td><td>12.57</td><td>4.91</td></tr><tr><td>9</td><td>2.44</td><td>3.23</td><td>6.16</td><td>2.68</td><td>15.85</td><td>2.46</td><td>2.78</td><td>4.02</td><td>2.68</td><td>2.08</td><td>1.45</td><td>0.57</td><td>3.87</td></tr><tr><td>10</td><td>2.45</td><td>4.58</td><td>3.11</td><td>1.18</td><td>1.43</td><td>1.43</td><td>0.62</td><td>0.68</td><td>6.57</td><td>1.43</td><td>4.22</td><td>7.44</td><td>2.93</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Mean</td><td>7.09</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>SD</td><td>4.42</td></tr></table>

According to Fig. 7, the relative importance calculations show that in affecting the level of Communication, Knowledge has the largest normalized CMSE index (0.41), followed by Trust (0.33) and <sup>fi</sup>nally Business–IT Alignment (0.26). An implication is that to ensure a strong communication level, a reasonable amount of resources needs to be devoted to maintaining and improving employees’ knowledge (e.g. knowledge about the company's business operations and knowledge about the particular business domain). Another implication is that since any two of the three factors contribute more than 50% in affecting Communication, none of three factors should be neglected by a company.

## 5.2. Business–IT Alignment as a central construct of interest

Also, Fig. 7 shows that Business–IT Alignment is directly connected with Communication and indirectly connected with Knowledge (via Communication) and Trust (via Communication) and Commitment (via Communication and then Trust). Incidentally, the hypothesis testing results of [11] support that employee trust and knowledge both signi<sup>fi</sup>cantly and positively affect business–IT alignment (their hypotheses H1 and H2) and do not support that employee commitment signi<sup>fi</sup>cantly affect business–IT alignment (their hypothesis H3). That H3 is not supported can be intuitively understood in the following way: the standard correlation between two constructs will be expected to be weak if they are “far apart” in the skeleton graph – e.g. the constructs Business–IT Alignment and Commitment has two intermediate constructs (Communication and Trust) separating them, whereas Knowledge and Trust are both one intermediate construct from Business–IT Alignment.

Perhaps a most interesting result garnered from the present study is that while the survey was initially designed to focus on business–IT alignment and how other factors may affect it, communication not only emerges as having the most direct role in in<sup>fl</sup>uencing the business–IT alignment, but also carries a central role in the entire skeleton graph. A <sup>fi</sup>rst implication is that in shaping the role of employees in executing successful strategic business–IT alignment, the employee communication aspect must be highlighted. A second implication is that instead of merely knowing whether or not business–IT alignment is affected by the other four factors, we can now see how these latter factors in<sup>fl</sup>uence the former: namely, Communications has direct association with Business–IT Alignment; Knowledge, Trust and Commitment in<sup>fl</sup>uence Business–IT Alignment via Communications. A third implication is that with Communications emerged as a pivotal construct in the present study, it may be worthwhile to further examine whether this “centrality of communication” phenomenon may take place in other aspects of business operations in relation to employee alignment.

## 5.3. Trust as a central construct of interest

That Trust is directly connected with Communication and Commitment (Fig. 7) con<sup>fi</sup>rm <sup>fi</sup>ndings in social and management sciences: effective communication is an essential ingredient in building trust between parties [20,40]. Also, as discussed in Section 2 and in [17,19], trust can occur when in the pursuit of a mutually bene<sup>fi</sup>cial outcome or a common goal, an employee voluntarily becomes vulnerable to another. This implies that a shared strong commitment towards a strategic goal among the employees can facilitate trust building among them.

Table 5  
The cross-validation results of the third network model

<table><tr><td rowspan="2">Test No.</td><td colspan="12">The third network (P=1)</td><td rowspan="2">Average</td></tr><tr><td>E1</td><td>E2</td><td>E3</td><td>E4</td><td>E5</td><td>E6</td><td>E7</td><td>E8</td><td>E9</td><td>E10</td><td>E11</td><td>E12</td></tr><tr><td>1</td><td>5.35</td><td>1.49</td><td>14.04</td><td>2.66</td><td>6.10</td><td>7.40</td><td>1.87</td><td>9.24</td><td>3.92</td><td>5.57</td><td>2.66</td><td>12.61</td><td>6.08</td></tr><tr><td>2</td><td>3.86</td><td>25.00</td><td>18.85</td><td>5.29</td><td>15.69</td><td>4.60</td><td>0.82</td><td>25.25</td><td>10.28</td><td>2.52</td><td>6.86</td><td>0.82</td><td>9.99</td></tr><tr><td>3</td><td>1.34</td><td>6.80</td><td>14.90</td><td>11.41</td><td>4.25</td><td>11.41</td><td>1.34</td><td>1.51</td><td>6.85</td><td>13.07</td><td>6.85</td><td>13.93</td><td>7.81</td></tr><tr><td>4</td><td>2.58</td><td>0.06</td><td>8.29</td><td>9.21</td><td>12.51</td><td>9.12</td><td>14.91</td><td>7.00</td><td>13.85</td><td>6.07</td><td>3.76</td><td>0.56</td><td>7.33</td></tr><tr><td>5</td><td>5.44</td><td>6.12</td><td>10.45</td><td>3.12</td><td>6.40</td><td>1.39</td><td>0.28</td><td>13.85</td><td>5.75</td><td>9.85</td><td>15.01</td><td>7.37</td><td>7.09</td></tr><tr><td>6</td><td>9.64</td><td>12.80</td><td>1.70</td><td>2.83</td><td>12.95</td><td>2.10</td><td>8.14</td><td>20.47</td><td>3.44</td><td>6.41</td><td>1.70</td><td>1.70</td><td>6.99</td></tr><tr><td>7</td><td>1.57</td><td>5.50</td><td>9.38</td><td>7.48</td><td>11.93</td><td>2.29</td><td>4.31</td><td>11.74</td><td>2.94</td><td>14.26</td><td>1.20</td><td>13.28</td><td>7.16</td></tr><tr><td>8</td><td>5.04</td><td>17.39</td><td>5.19</td><td>3.09</td><td>18.02</td><td>5.04</td><td>13.12</td><td>2.97</td><td>3.79</td><td>2.97</td><td>3.79</td><td>14.29</td><td>7.89</td></tr><tr><td>9</td><td>0.01</td><td>6.19</td><td>15.08</td><td>0.01</td><td>7.87</td><td>1.03</td><td>8.58</td><td>8.58</td><td>14.34</td><td>1.03</td><td>5.20</td><td>1.03</td><td>5.75</td></tr><tr><td>10</td><td>0.97</td><td>0.97</td><td>2.23</td><td>6.85</td><td>0.15</td><td>5.57</td><td>16.94</td><td>16.10</td><td>10.33</td><td>14.86</td><td>11.42</td><td>8.92</td><td>7.94</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>Mean</td><td>7.4</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>SD</td><td>1.17</td></tr></table>

Table 7  
Table 6  
Performance of the <sup>fi</sup>rst network model with varying P.

<table><tr><td>P</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>MAPE</td><td>6.54</td><td>7.65</td><td>7.87</td><td>8.04</td><td>7.66</td><td>8.16</td></tr><tr><td>Standard deviation of MAPE</td><td>2.39</td><td>2.92</td><td>2.69</td><td>2.64</td><td>2.83</td><td>3.22</td></tr><tr><td>Pearson coefficient</td><td>0.6</td><td>0.55</td><td>0.54</td><td>0.51</td><td>0.54</td><td>0.39</td></tr></table>

Fig. 7 also shows that in affecting the level of Trust, Communication has a larger normalized CMSE index (0.62) than Commitment (0.38). Communication, as we have discussed in Section 5.1, can be affected by knowledge and availability of IT infrastructure, as well as other factors outside the scope of the present project but should be addressed in the future studies. Commitment, on the other hand, can be nurtured by promoting the sense of belonging and ownership among employees such that they will be more encouraged to identify with their company goals.

## 6. Conclusion

In this study, an exploratory analysis was performed to examine the connectivity relations among employee alignment orientations and business–IT alignment. Based on survey data gathered from employees in Indonesian manufacturing companies, a two-stage approach was applied to discover the connectivity relations among several aspects of employee alignment orientation and the strategic implementation of business–IT alignment, and then to measure the relative in<sup>fl</sup>uence of one aspect onto another. Our <sup>fi</sup>ndings indicated that employee communication has the most direct and positive relationship with business–IT alignment, and yet employee trust and employee knowledge also have signi<sup>fi</sup>cant but indirect contribution to business–IT alignment. Our results suggested that in facilitating the development of IT to support the strategic implementation of business strategies, the securing of employee trust and employee knowledge can enhance communication effectiveness within organizational context. With it being supported and enhanced by trust and knowledge, employee communication can be used to foster and drive the implementation of business–IT alignment to a desired state. In other words, it would be appropriate to assure that enhanced employee trust and knowledge may in<sup>fl</sup>uence the business–IT alignment, only via organizational communication. One implication is that the development of IT not only can improve the effectiveness and ef<sup>fi</sup>ciency of business operations, but also enhance the communication aspect of employee alignment. In return, good communication would facilitate employees to both psychologically and technically align themselves with the implementation of business strategies.

At a more fundamental level, in this study, we demonstrated that instead of needing to conjecture a path model as in [11] to study business–IT alignment, the two-stage analysis approach of [58] can be fruitfully applied to the same data set of [11] to uncover the rich connectivity relations that capture the phenomena underlying business–IT alignment. The two-stage approach can be generally applied to other technology management studies involving the analysis of survey data, such as the recent articles [4,26,31,60]. A limitation of the present study is that we exclusively focused on how employees’ perceptions of their alignment orientation in<sup>fl</sup>uence business–IT alignment. In our future work, we plan to include objective measures such as employees quali<sup>fi</sup>cations, IT capital investment and organizational factors concerning team structures.

The averaged relative importance of factors.

<table><tr><td colspan="2">The first model</td><td colspan="2">The second model</td></tr><tr><td>Factors</td><td>R</td><td>Factors</td><td>R</td></tr><tr><td> $X_1$ </td><td>0.33</td><td> $X_2$ </td><td>0.38</td></tr><tr><td> $X_4$ </td><td>0.41</td><td> $X_3$ </td><td>0.62</td></tr><tr><td>Y</td><td>0.26</td><td></td><td></td></tr></table>

![](/api/attachments/WVAAZPUY/fulltext/images/faa4c9d1d9f7e0f690a20806048029142ee04db849ce564fdab5394da9236cdb.jpg)  
Fig. 7. Overall RI model.

## Acknowledgments

We thank the editor and the anonymous reviewers for their helpful suggestions and comments for improving the content of this article. SCN was supported by the City University of Hong Kong Strategic Research Grants (7002493, 7002566). FC and AC were supported by a grant from the Hong Kong Polytechnic University (Project No. G-YX4D). The authors would like to thank the City University of Hong Kong and the Hong Kong Polytechnic University Research Committees for the <sup>fi</sup>nancial and technical supports.

## References

[1] S.M. Al-Ghamdi, M.H. Roy, Z.U. Ahmad, How employees learn about corporate strategy: An Empirical analysis of Saudi manufacturing company, Cross Cultural Management: An International Journal 14 (2007) 273-295.

[2] K. Baba, R. Shibata, M. Sibuya, Partial correlation and conditional correlation as measures of conditional independence Australian & New Zealand Journal of Statistics 46 (2004).657-664

[3] H. Benbya, B. McKelvey, Using Co-Evolutionary and Complexity Theories to Improve IS Alignment: a multi-level Approach, Journal of Information Technology (Palgrave MacMillan) 21 (2006) 284–298.

[4] A. Benlian, T. Hess, Opportunities and risks of software-as-a-service: Findings from a survey of IT executives, Decision Support Systems 52 (2011) 232–246.

[5] H. Boer, M. Hill, K. Krabbendam, FMS implementation management: promise and performance, International Journal of Operations & Production Management 10 (1990) 5–20.

[6] W.R. Boswell, J.W. Boudreau, How leading companies create, measure and achieve strategic results through “line of sight”, Management Decision 39 (2001) 851-860.

[7] I.J. Chen, A. Gupta, Understanding the human aspects of <sup>fl</sup>exible manufacturing system through management development, The Journal of Management Development 10 (1993) 32–43.

[8] I. Chen, A. Gupta, C.H. Chung, Employee commitment to the implementation of <sup>fl</sup>exible manufacturing systems, International Journal of Operations & Production Management 16 (1996) 4–13.

[9] A.Y.L. Chong, K.B. Ooi, Adoption of Interorganizational System Standards in Supply Chains: An Empirical Analysis of RosettaNet Standards, Industrial Management and Data Systems 108 (2008) 529–547

[10] A.Y.L. Chong, K.B. Ooi, A. Sohal, The relationship between supply china factors and adoption of e-collaboration tools: an empirical examination, International Journal of Production Economics 122 (2009).150–160

[11] A.Y.L. Chong, F.T.S. Chan, K.-B. Ooi, N. Darmawan, Does employee alignment affect business-IT alignment: an empirical analysis, Journal of Computer Information Systems 51 (2011) 10–20.

[12] J.E. Cliff, P.D. Jennings, Commentary on the multidimensional degree of family in<sup>fl</sup>uence construct and the F-PEC measurement instrument, Entrepreneurship Theory and Practice 29 (2005) 341–347.

[13] B. Cumps, D. Martens, M. De Backer, R. Haesen, S. Viaene, G. Dedene, B. Baesens, M. Snoeck, Inferring comprehensive business/ICT alignment rules, Information Management 46 (2009) 116–124 Information & Management, 46, 116–124.

[14] J. Darroch, Developing a measure of knowledge management behaviors and practices Journal of Knowledge Management 7 (2003) 41–54.

[15] S. De Haes W. Van Grembergen Exploring the relationship between IT governance practices and business/IT alignment through extreme case analysis

in Belgian mid-to-large size <sup>fi</sup>nancial enterprises, Journal of Enterprise Information Management 22 (2009) 615–637.

[16] T. Dewett, G.R. Jones, The role of information technology in the organization: a review, model and assessment, Journal of Management 27 (2001) 313–346.

[17] K.T. Dirks, D.L. Ferrin, The Role of Trust in Organizational Settings, Organization Science 12 (2002) 450–467

[18] P. Drucker, The Practice of Management, Harper, New York, 1954.

[19] M. Gagnon, K. Jansen, J.H. Michael, Employee Alignment with Strategic Change: A study of Strategy-Supportive Behaviour among blue collar employees, Journal of Managerial Issues 20 (2008) 425–443.

[20] J.A. Gilbert, T.L.P. Tang, An examination of organizational trust antecedents, Public Personnel Management 27 (1998) 321–338.

[21] J. Gould-Williams, The importance of HR practices and workplace trust in achieving superior performance: a study of public-sector organizations, International Journal of Human Resource Management 14 (2003) 28–54.

[22] R.M. Grant, Toward a knowledge-based theory of the frim, Strategic Management Journal 17 (1996) 109–122.

[23] S. Gregor, D. Hart, N. Martin, Enterprise architectures: enablers of business strategy and IS/IT alignment in government, Information Technology & People 20 (2007) 96–120.

[24] T. Hastie, R. Tibshirani, J. Friedman, The elements of statistical learning, Springer-Verlag, New York, 2001.

[25] T. Hastie, R. Tibshirani, J. Friedman, The elements of statistical learning, 2nd ed. Springer-Verlag, New York, 2009.

[26] C.W. Holsapple, J. Wu, An elusive antecedent of superior <sup>fi</sup>rm performance: The knowledge management factor, Decision Support Systems 52 (2011) 271–283.

[27] M.H. Hsu, T.L. Ju, C.H. Yen, C.M. Chang, Knowledge sharing behavior in virtual communities: the relationship between trust, self-ef<sup>fi</sup>cacy, and outcome expectations, International Journal of Human Computer Studies 65 (2007) 153–169.

[28] Z. Huang, H. Chen, C.-J. Hsu, H.-W. Chen, S. Wu, Credit rating analysis with support vector machine and neural networks: a market comparative study, Decision Support Systems 37 (2004) 543–558.

[29] M. Kalisch, P. Buhlmann, Estimating high-dimensional directed acyclic graphs with the PC-Algorithm, Journal of Machine Learning Research 8 (2007) 613–636.

[30] M. Kyobe, The in<sup>fl</sup>uence of strategy-making types on IT alignment in SMEs, Journal of Systems and Information Technology 10 (2008) 22–38.

[31] H. Li, R. Sarathy, H. Xu, The role of affect and cognition on online consumers decision to disclose personal information to unfamiliar online vendors Decision Support Systems 51 (2011) 434–445.

[32] E.A. Locke, G.P. Latham, M. Erez, The determinants of goal commitment, Academy of Management Review 13 (1988) 23–29.

[33] J. Luftman, Assessing Business-IT alignment maturity, Communications of the Association for Information Systems 4 (2000) 1–51.

[34] J. Luftman, T. Brier, Achieving and sustaining business-IT alignment, California Management Review 42 (1) (1999) 109–122.

[35] J. Luftman, R. Kempaiah, E. Nash, Key issues for IT executives 2005, MIS Quarterly Executive 5 (2006) 80–99.

[36] B. McEvily, V. Perrone, A. Zaheer, Trust as an organization principle, Organization Science 14 (1) (2003) 91–103.

[37] E. McLean, J. Soden, Strategic planning for MIS, John Wiley & Sons, New York 1977.

[38] J.R. Meredith, Managerial Lessons in Factory Automation: Three Case Studies in Flexible Manufacturing Systems, Monograph No. 4, Operations Management Association, TX, 1989.

[39] P. Mills, Managing service industries, Ballinger, New York, 1986.

[40] J. Mishra, M.A. Morrissey, Trust in employee/employer relationships: a survey of West Michigan managers, Public Personnel Management 19 (1990) 443–485.

[41] R.T. Mowday, L.W. Porter, R.M. Steers, Employee Organization Linkages: The Psychology of Commitment, Absenteeism and Turnover, Academic Press, New York, 1982.

[42] C.H. Noble, P. Mokwa, Implementing Marketing Strategies: Developing and Testing a Managerial Theory, Journal of Marketing 63 (1999) 57–73.

[43] I. Nonaka, H. Takeuchi, The Knowledge Creating Company, Oxford University Press, New York, 1995.

[44] J. O'Neil, Measuring the Impact of Employee Communication on Employee Comprehension and Action: A Case Study of a Major International Firm, The Public Relations Journal 2 (2009) 1–17.

[45] N. Panteli, S. Sockalingam, Trust and con<sup>fl</sup>ict within virtual inter-organizational alliances: a framework for facilitating knowledge sharing, Decision Support Systems 39 (4) (2005) 599–617.

[46] R. Papp, Business-IT alignment: Productivity paradox payoff? Industrial Management & Data Systems 99 (1999) 367–373.

[47] J.M. Pappas, K.E. Flaherty, B. Wooldridge, Tapping into Hospital Champions: Strategic Middle Managers, Health Care Management Review 29 (2004) 8–16.

[48] M. Parker, R. Benson, Information economics, Prentice-Hall, Englewood Cliff, N.J, 1988.

[49] B.H. Reich, I. Benbasat, Factors that in<sup>fl</sup>uence the social dimension of alignment between business and information technology objectives, MIS Quarterly 24 (2000) 81–113.

[50] G. Shmueli, O.R. Koppius, Predictive analytics in information systems research, MIS Quarterly 35 (3) (2011) 553–572.

[51] G. Starzmann, C. Baca, Total rewards: creating freshness that lasts, Workspan 47 (2004) 55–61.

[52] A.H. Sung, Ranking importance of input parameters of neural networks, Expert Systems with Applications 15 (1998) 405–411.

[53] Technet, Business-IT alignment Overview http://technet.microsoft.com/en-us library/cc543301.aspx, , 2008.

[54] T.S.H. Teo, J.S.K. Ang, Critical Success Factors in the Alignment of IS plans with business plans, International Journal of Information Management 19 (1999) 173–185.

[55] T.S.H. Teo, W.R. King, Integration between business planning and information systems planning: An evolutionary-contingency perspective, Journal of Management Information Systems 14 (1997) 185–214.

[56] S.S. Tzafrir, G.H. Harel, Y. Baruch, S.L. Dolan, The consequences of emerging HRM practices for employees' trust in their managers, Personnel Review 33 (2004) 628–647.

[57] K.E. Weick, Cognitive processes in organizations, in: B.M. Staw (Ed.), Research in Organizational Behavior, JAI Press, Greenwich, CT, 1979, pp. 41–74.

[58] T.C. Wong, K.M.Y. Law, H.K. Yau, S.C. Ngan, Analyzing supply chain operation models with the PC-algorithm and the neural network, Expert Systems with Applications 38 (2011) 7526–7534.

[59] B. Wooldridge, S.W. Floyd, Research Notes and Communications Strategic Process Effects on Consensus, Strategic Management Journal 10 (1989) 295–302.

[60] I.-L. Wu, J.-Y. Li, C.-Y. Fu, The adoption of mobile healthcare by hospital's professionals: An integrative perspective, Decision Support Systems 51 (2011) 587–596.

Dr. T. C. Wong received the B.Eng. degree in Industrial Engineering and the M. Phil. and Ph.D. degrees in Operations Research from the University of Hong Kong, Pokfulam, Hong Kong, in 2002, 2005, and 2008, respectively. He is currently with the Department of Systems Engineering and Engineering Management, City University of Hong Kong. His current research interests include operations research, computation optimization and modeling, supply chain management, and evolutionary algorithms.

Dr. Shing-Chung Ngan is currently a Lecturer in the Department of Systems Engineering and Engineering Management at the City University of Hong Kong. He received his B.Sc. degree from UC Berkeley, USA, and his M.Sc. and Ph.D. degrees from the University of Minnesota, USA. His research interests include business and management data analysis, neuro-informatics and bioinformatics.

Dr. Felix Chan received his BSc Degree in Mechanical Engineering from Brighton Polytechnic (now University), UK, and obtained his MSc and PhD in Manufacturing Engineering from the Imperial College of Science and Technology, University of London, UK. Dr. Chan is an Associate Professor at the Department of Industrial and Systems Engineering The Hong Kong Polytechnic University. His current research interests are Logistics and Supply Chain Management, Operations Management, Distribution Coordination, Systems Modelling and Simulation. Supplier Selection. To date, he has published 10 book chapters, over 200 refereed international journal papers and 200 peer reviewed international conference papers. He is a chartered member of the Chartered Institute of Logistics and Transport in Hong Kong.

Dr. Alain Yee-Loong Chong is currently an assistant professor in information systems in Nottingham University Business School China, University of Nottingham (China campus). Prior to that, he was a postdoctoral research fellow in the Department of Industrial and Systems Engineering, The Hong Kong Polytechnic University. Dr. Chong received his BSc and MSc from Coventry University, UK, and PhD from the Multimedia University, Malaysia. His research interests include supply chain management, e-business adoption and service science. To date, his papers have been accepted/published in more than 70 refereed international journals and conference proceedings. His paper has been accepted/published in Decision Support Systems, International Journal of Production Research, International Journal of Production Economics, Production Planning and Control, Expert Systems with Applications, Journal of Computer Information Systems and Industrial Management & Data Systems.
