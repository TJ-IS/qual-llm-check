---
otero_id: 10424
otero_key: "G6KHHCQE"
title: "Recommendation of startups as technology cooperation candidates from the perspectives of similarity and potential: A deep learning approach"
authors: "Hyoung Jun Kim; Tae San Kim; So Young Sohn"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.113229"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Recommendation of startups as technology cooperation candidates from the perspectives of similarity and potential: A deep learning approach

Hyoung Jun Kim, Tae San Kim, So Young Sohn

Department of Industrial Engineering, Yonsei University, 134 Shinchon-dong, Seoul 120–749, Republic of Korea

## A R T I C L E I N F O

Keywords: Doc2vec Item-based collaborative filtering Factor analysis Startup M&A

## A B S T R A C T

Companies consistently strive to prepare for new technologies for survival. In a rapidly changing market, absorbing innovation through cooperation strategies can complement internal research and development for new technology development. Startups with state-of-the-art technologies are good candidates for successful cooperation; however, it is dificult to identify their technological positions. Our study suggests a framework to identify appropriate startup candidates using startup profile texts provided by the Crunchbase database. We utilize a doc2vec approach to extract feature vectors representing technological meanings from the startup profile texts and patent abstracts of acquiring companies. Based on these vectors, we apply item-based collaborative filtering to estimate scores for technological similarity between a company and a startup to be acquired. Furthermore, we screen for promising startups using factor analysis, with variables representing the startup's potential. We believe that our framework can save time and efort in the early stage of cooperation planning by supporting efective decision-making.

## 1. Introduction

Nowadays, companies and organizations consistently seek emerging trends and develop corresponding technologies to survive [1]. However, merely investing more in internal research and development (R& D) is not suficient to absorb the rapidly changing trends and meet the demand for novel technologies. Cooperation strategies such as mergers and acquisitions (M&A), co-application, co-creation, and co-production [2] provide advantageous external sources in a fluctuating technology market. These strategies reduce uncertainty in the innovation process and increase the synergetic efects through cooperation and competi tion with other firms.

Regarding external cooperation strategies related to a company's technology capabilities, startups are considered great candidates for cooperation, because they possess innovative technologies and are assumed to forge new frontiers in high-end industries. Furthermore, their relatively low costs and flexible decision-making systems can foster successful cooperation [3]. However, companies seeking proper target startups often sufer from information asymmetry with respect to technological capabilities, which are relatively unknown. Several studies have suggested using patents to identify technological positions, but most startups do not own patents so as to prevent technology leaks and save resources required to apply for a patent. Furthermore, as there are a considerably high number of new ventures, their evaluation becomes dificult. Therefore, successful cooperation begins by identifying and filtering for candidates that would be strategically fit for each other, which will yield remarkable savings of time and cost.

This study suggests a framework for screening startups as cooperation candidates by identifying their technological positions. Among the many external cooperation strategies, we explain our framework in terms of the M&A strategy. We collect startup profiles from Crunchbase, the biggest—and a reliable—data source for startups as well as patent abstracts from the United States Patent and Trademark Ofice (USPTO) [4]. We vectorize the collected text corpus using doc2vec and calculate the adjacency matrix between patents and startups. Based on this matrix, we estimate scores for technological similarity between the acquiring company and startup candidates by employing item-based collaborative filtering (IBCF). Moreover, potentially promising startups are evaluated using factor analysis (FA) with key variables, including total funding, number of events and articles for firms' promotion, competitive environment, and CEOs' business experience. Based on the individual factor and technological similarity scores, we recommend the best candidate startups considering both exploitative and exploratory cooperation approaches. We apply our framework to a case study in the virtual reality and augmented reality (VR/AR) field. Then, we sort several promising startups according to the acquiring company's interests and strategy. We believe that our framework, by recommending strategically suitable candidates, can save companies' valuable resources. The results provide grounds for developing major cooperation strategies and making other types of technology-based collaboration decisions.

We elaborate the aforementioned frameworks in the following sections. In Section 2, we review the literature on promising startups, technology M&A, and M&A strategies. In Section 3, we suggest a recommendation system based on IBCF using doc2vec and FA. In Section 4, we explore the Crunchbase startup database and patents from USPTO. In Section 5, we apply our framework in the VR/AR field and identify suitable startup M&A candidates for a global electronics company. Lastly, we discuss the contributions and limitations of this study in Section 6.

## 2. Literature review

## 2.1. Promising startups

Startups, also known as ventures and entrepreneurship companies, are normally companies that are young and small. Their biggest strength is that their fast decision-making process enables flexibility and responsiveness to market fluctuations and new business opportunities [3]. From the market's perspective, startups are vehicles of disruptive innovation as well as channels to commercialize novel business opportunities successfully [5]. Therefore, scholars, researchers, and entrepreneurs pay close attention to startups which can eventually lead to the development of new technologies, services, products, and busi ness models [6].

It is dificult to evaluate and identify high-potential cooperation candidates in the current unprecedented boom of startups. A company's potential can be evaluated by its technologies, patents, and products [7–9]. However, young startups are often insuficiently prepared or have limited exposure to the public. A startup's information can be obtained partially from its investor and venture capitalist network, or through an actual first-hand inspection of the company. It would be a waste of resources, and realistically impossible, to investigate all startups in the area of interest. Therefore, we focus on the literature evaluating startups in terms of their human resources, environment, social impact, and finances [10].

From a human resources point of view. the founder's capability must be considered with utmost priority [11]. First, the founder's level of competitiveness can be evaluated by the founder's personality [12]: this includes leadership traits, motivation, and vision, which can result in success [13]. The founder's personal and professional experiences should also be considered, including the level of education attained and prior experiences with starting other companies [14]. The founder's level of education is positively related to the company's survival and growth [15]. The experience of founding startups can directly influence the possibility of succeeding in future ventures [10,12,16]. These attributes naturally assist founders in building strong networks in related fields, which can be a great source of growth and development. In addition, the founder's age can afect the success of a startup.

The environment also influences startups' success. As characteristics and potential vary among markets [7], there needs to be a detailed investigation of the market to which a specific startup belongs. Startups are more likely to survive in markets with a large number of angel investors or aggressive and favorable funders [14,16]. However, if the surrounding environment fluctuates rapidly, startups may find it difi cult to adapt to drastic changes.

Social activities, including publicity and networking with other companies, have a lasting impact on the growth of startups. Moreover, the number of competitors and cooperators in a startup's network can significantly impact its early development. Many competitors exist in a growing market, making it dificult to settle in a secure position [16,17], but at the same time, startups can take advantage of strategic collaboration with other companies to make up for their insuficient resources. Furthermore, frequent press exposure has a positive impact on the image and growth of startups. The ability to market efectively is essential for increasing funding opportunities and attracting customers. Thus, a strong network and public exposure can be utilized to filter potential startups.

From the financial perspective, a startup's profit structure and stability are considered. Startups mostly depend on funding by other companies or investors, and this information can be an indication of the most essential survival factor [18]. Furthermore, investor information indirectly indicates a startup's potential. Venture capitalists provide not only financial aid but also business advice and network support, which can accelerate growth. Bertoni et al. [19] showed that startups in which venture capitalists have invested experience greater growth in both sales and employment rate.

## 2.2. Approaches for successful resource-based cooperation strategies

To develop a successful cooperation strategy, numerous factors should be considered, including the right price, suficient discussion between companies, speed of system integration, and cultural diferences between organizations [20]. Most importantly, companies must screen for appropriate candidates at the very first stage. The word “appropriate” indicates how well two companies fit with each other strategically. Finding potential targets that align with a company's corporate growth strategy is key to successful cooperation strategies, and this can be confirmed by identifying the company's resources. Several studies have been conducted on resource-based cooperation [21]. Resource-based cooperation strategies enhance the probability of success of actual cooperation and positively afect the company's outcomes [22]. There are two types of resource-based cooperation strategies: exploitative and exploratory. In other words, companies can target either other companies with similar technologies that can sharpen their core technology, or companies with very diferent technologies that can diversify their technology portfolio. Resource similarity indicates the distance between the core capabilities of the companies involved in the cooperation [23]. The degree of similarity in resource-based cooperation is a critical element for cooperation strategies and should have diferent efects.

An exploitative strategy seeks cooperation candidates with high technological relevance. This not only broadens the acquiring company's existing knowledge, but also takes advantage of economies of scale to develop more sophisticated technologies [24]. In addition, exploitative M&A can increase the company's market share and influence by absorbing the target company's customer base [25]. As a result, the combined company strengthens its superiority in its area of technological expertise and gains greater economic benefits than it would by cooperating with other firms [26].

However, an exploratory strategy requires the acquiring company to find cooperation candidates outside its own field. Complementary sources of technology can also help in re-deploying existing resources to enhance the acquiring company's innovative capabilities [27]. In addition, the exploratory strategy identifies novel market opportunities through cooperation with companies possessing unfamiliar technological resources. Although this strategy entails higher risk than other R& D activities, it may result in remarkable technological innovation and considerable economic benefit if successful [26].

## 2.3. Technology M&A

If a company can overcome its weaknesses by absorbing technolo gical assets, M&A can be a significant source of innovation and development [24]. Technology M&A can reduce the development risks of new technologies. Basu and Wadhwa [28] proved that M&A activities bring more disruptive innovation compared with collaboration and investment. Stettner and Lavie [29] showed that M&A is efective for exploring unique knowledge and novel technologies. Moreover, absorbing technological assets and resources such as patents can be critical [8,30]. Likewise, M&A is a great medium to maintain technolo gical competitiveness and gain advantage in the face of fierce competition.

![](/api/attachments/G6KHHCQE/fulltext/images/bb731179a1cbd855628b2c82b962b0874ed1daeec649a8098938fb508c8fab68.jpg)  
Fig. 1. Recommendation process for item-based collaborative filtering

Startups can be attractive M&A candidates as they possess in novative technologies [31]. Large companies collaborate with young ventures to extract novel ideas and explore innovations. Acquiring firms are inspired by startups with new knowledge [32], technology, market insight [33], and approaches [6]. Startups take advantage of coopera tion by gaining access to essential resources—including human resources and product knowledge—possessed by more mature acquirers [31]. Furthermore, they achieve accumulated market reputation, re liability, and know-how through their new partners [34].

For successful M&A, it is critical to filter out companies with inefective technology portfolios [21]. Nonetheless, only a few studies recommend proper target companies [35]. Resource-based M&A strategies are based on technological similarity, and only a few studies have identified such similarities between companies. They mostly use patent information to determine the technological position. Specifically, as the text of patents describes the overall meaning of the technology, evaluation of a massive volume of text information can prove very efective in assessing a company's technology. Saviotti et al. [36] constructed a similarity network based on the co-occurrence of words in patents to identify and recommend companies that demonstrate synergetic potential. Park et al. [37] employed subject-action-object text mining to recommend companies in accordance with M&A strategies and used a patent map to illustrate the results. Huang et al. [35] further enhanced the methodology by incorporating similarities based on International Patent Classification (IPC) for a more elaborate selection of potential M &A candidates.

## 3. Framework

In this study, we suggest a framework for acquiring firms to identify startups as potential M&A candidates using two M&A strategies: technological similarities and promising factor scores of the startups. For clarity, in this framework, we use the term “company” to refer to the acquiring player and “startup” to indicate the target candidate. Patent abstracts of companies and startup profile texts are collected from USPTO and Crunchbase, respectively. Dense vectors representing the semantic meaning of technology are extracted from these texts using doc2vec. We estimate the adjacency matrix using cosine similarity among the vectors of patents and startups. This matrix is used as the similarity matrix in IBCF to calculate the scores of technological similarity between companies and startups. Based on these scores, we can position the outcomes considering the two aforementioned types of M& A strategies: exploitative and exploratory. Using FA, we further exploit the variables related to evaluating the startups' potential, such as total amount of investment capital received, revenue generated, prior startup experience of the CEO, qualifications of team members, and presence in published articles and promotional events. We plot a recommendation map integrating the technological similarity and factor scores. Our study uses this map to ofer appropriate M&A targets to acquiring companies.

## 3.1. Technological similarity score

## 3.1.1. IBCF

Collaborative filtering is a methodology for predicting a customer's interest based on a large volume of customer preference data [38]. This is commonly used in recommendation systems and can be divided into user-based collaborative filtering and IBCF. User-based collaborative filtering (UBCF) exploits similar customers' interests to recommend new items to a specific customer [39]. Meanwhile, IBCF exploits similarities among items to recommend new items with traits similar to those receiving a favorable customer response [40]. It is based on the assumption that customers like new items that are similar to the ones they have already purchased or for which they have expressed a preference.

To obtain recommendation scores for IBCF, an item similarity matrix $A \in R ^ { N \times N }$ and the user's item ownership matrix $X \in R ^ { N \times D }$ are needed, where N and D denote the number of items and users, respectively. Recommendation matrix R can be measured by the matrix product of A and X. As shown in Fig. 1, the item similarity matrix indicates the similarity between items. For example, the column vector of item j includes similarity information about item j and other items. Meanwhile, the users' item matrix represents the users' item ownership information. The row vector of user i indicates whether the user owns (or has purchased) the item. The recommendation process is based on the assumption that the user will prefer items similar to the ones he/she already possesses. If the dot product of the column vector of item j and row vector of user i is obtained, the user's preference degree for item j can be measured based on his/her item ownership information. Therefore, recommendation matrix R shows the preference score of items according to the user. These items can be recommended to the user in accordance with their recommendation scores, with those scoring highest being the most highly recommended.

## 3.1.2. M&A recommendation process based on IBCF

In this study, we apply IBCF to companies and startups to develop a list of recommended M&A candidates for an acquiring company. IBCF is adopted to recommend similar startups based on patent information. Fig. 2 shows the overall IBCF process for estimating technological similarity between a company and a startup. The item matrix of user $\boldsymbol { X } \in \boldsymbol { R } ^ { \tilde { N } \times { D } }$ indicates patent ownership information for applicant firms, where N is the number of total patents and D is the number of total firms. This matrix is called the company applicant firm-patent matrix. If a company possesses a patent, the applicant firm-patent matrix records a value of 1, and 0 otherwise. A preference or importance matrix can be substituted for this binary matrix depending on the company's purposes; this may reflect the technological interests of a company more accurately.

![](/api/attachments/G6KHHCQE/fulltext/images/942d8069f429b0259f66c1e6cc38797210e1f04a57cbacf521d2a0ab3c792b20.jpg)  
Fig. 2. Process for calculating the similarity scores of startups

In contrast with traditional IBCF, the item similarity matrix $A \in R ^ { N \times M }$ shows the similarity information of startups and patents rather than the similarity of patents, where M is the number of total startups. This startup/patent adjacency matrix represents the technological similarity between startups and patents. However, there are various definitions of and approaches for ascertaining technological similarity. This study defines technological similarity as similarity in terms of bibliographic information, and it utilizes the doc2vec method to identify technological similarity based on the profiles of startups and patent abstracts. Multiplying the applicant firm-patent matrix with the startup/patent adjacency matrix results in an applicant firm-startup matrix containing technological similarity scores. High scores indicate vertical M&A candidates, and low scores indicate horizontal M&A candidates.

## 3.1.3. Doc2vec

This study aims to construct a startup/patent adjacency matrix or, in other words, to estimate the technological similarity between startups and companies. However, it is dificult to measure the quantitative technological distance between companies and startups. Previous studies exploited patent data (i.e., co-classification or textual information), which are generally not available for young ventures without patents. To overcome this drawback, we utilize the semantic meaning of the texts to identify the technological position of each company and startup. These texts provide detailed descriptions of the relevant tech nology.

To extract the semantic meaning of technology from these texts, we utilize the doc2vec method. Doc2vec is based on word2vec, which ex tracts word vectors based on the co-occurrence of words. Mikoloy et al. [41] designed a model to analyze a word by its surrounding words in a certain window size. The window size is the length of the surrounding words, and it is chosen by the user. Word2vec is based on the assumption that a higher possibility of two words' co-occurrence indicates higher similarity between the words. Word2vec maximizes the possibility of the central word's occurrence given the surrounding words.

Le and Mikolov [42] suggested doc2vec, which is a methodology used to extract the dense vector of a document. As shown in Fig. 3, an ID is added for each document, and the model learns the vectors according to the words in the corresponding document. Extracted vectors include the semantic meaning of the document based on the words and sentences, which can be used to estimate similarities among the documents [43].

In our doc2vec approach, each patent and startup was regarded as a document. The patent and startup documents utilized were the patent abstracts and startup profiles, respectively. A patent's abstract included a summary of technical specifications, and a startup's profile included general information with specific product explanations, which might provide indications of the startup's technology. The dense vector derived from each document represents the technical capacities of a patent or startup.

Given the specific area of interest, we vectorized the texts of the startup profiles and patent abstracts using doc2vec. Based on this result, the technological similarity between all patents and startups was assessed. The startup/patent adjacency matrix for IBCF was obtained by measuring the similarity between these vectors (Fig. 3). To calculate the adjacency matrix for startups and patents, we used cosine similarity. From the extracted startup/patent adjacency matrix, we measured the scores of similarity between the list of applicant firms and startups using the matrix product based on the applicant firm/patent matrix.

## 3.2. Evaluation of startup potential and the recommendation process

## 3.2.1. FA

Based on the results of the aforementioned process, we recommend startups with a high similarity score as exploitative M&A candidates, and those with a low score as exploratory M&A candidates. Our proposed framework, which aims to increase the likelihood of successful M &A, includes the evaluation of potential startups as part of its recommendation process and selects the most qualified M&A candidates from among many promising startups.

This study evaluates the potential of startups to recommend realistic candidates based on technological similarity. First, from a human resources perspective, we consider the presence of startup experience [10,12,16]. Experienced founders are expected to have the capability and know-how to overcome obstacles. Indirectly, a higher number of members in the founding team is likely to indicate a greater possibility of having more experience, a broader network, and better technological capability [14,16]. The number of employees is another variable of the asset base that represents the size of the startup and the number of people agreeing to the firm's philosophy. Almeida et al. [44] showed that the higher the number of employees, the more the external knowledge and innovation that the organization will be able to absorb.

Second, the success of a startup lies in its level of financial stability [45]. Young ventures are generally reliant on external funds and investments, which also indicates that their potential has been acknowledged and proven in the market. Revenue generation also represents the company's promising future. Third, we evaluate whether the company is well-exposed to the market. It is critical to be consistently visible to create customer appeal for the products and services ofered. Therefore, the number of articles referencing a certain startup and the number of events in which the startup participated, such as startup expositions and conferences, can be variables representing the degree of exposure. Fourth, we observed the corresponding market using the number of competitors [16,17]. The smaller the number of similar competitors, the higher the possibility of preempting the market. Hence, identifying competing startups can also be an important factor to assess potential. In this study, we use the average technological similarity based on the results of the doc2vec approach.

We employ FA to confirm the structure of the given variables and derive weights. FA is an unsupervised learning methodology used to excavate hidden linear patterns or structures among numerous vari ables [46]. Using FA, we can derive various factors related to the potential of startups. The meaning of each factor depends on which variables have material influence on the corresponding factors. Ou variables are described in Table 1.

![](/api/attachments/G6KHHCQE/fulltext/images/86c672ad2dcf95a154dc6edc01ca8e86c64207c86c9d7fd215092c08f04c5cba.jpg)  
Fig. 3. Framework for estimating the startup/patent adjacency matrix.

Table 1  
Description of our variables for evaluating startups' potential.

<table><tr><td>Variables</td><td>Description</td></tr><tr><td>Business experience</td><td>Prior experience in terms of the number of startups founded</td></tr><tr><td>Total investment</td><td>Total funding excluding debt</td></tr><tr><td>Revenue</td><td>Total revenue</td></tr><tr><td>Events</td><td>Number of events in which the startup participated</td></tr><tr><td>Articles</td><td>Number of news articles referencing the startup</td></tr><tr><td>Competitors</td><td>Similar startups in the same industry</td></tr><tr><td>Investors</td><td>Number of investors</td></tr><tr><td>Employees</td><td>Number of employees</td></tr><tr><td>Number of founders</td><td>Number of members on the founding team</td></tr></table>

## 3.2.2. Recommendation process

In our framework, the list of recommended M&A candidates is de rived based on technological similarity scores and evaluation of the startups' potential. Companies can have their own priorities among factors for evaluating a startup's potential. For instance, financially stable companies would place less importance on the startup's capitalization status; instead, they would assign more weight to their tech nological originality or the CEO's competency. On the other hand, conservative companies might seek financially stable startups. Therefore, we plotted a startup recommendation map according to each factor, as shown in Fig. 4.

The horizontal axis on the recommendation map represents the technological distance between an acquiring company and startups, while the vertical axis indicates the evaluated potential score of startups related to the corresponding factor. Since a company wants to find prospective candidates, startups with low potential in each factor are unlikely targets. Companies can extract target lists in line with their M& A strategy. If a company wants to use an exploratory M&A approach, startups with low similarity scores could still be suitable M&A candi dates. Startups with high similarity scores could be appropriate candi dates for an exploitative M&A approach.

## 4. Data and preprocessing

## 4.1. Data

Startups are generally founded based on their disruptive and in novative products, services, and technologies. In this study, we apply our framework to the patents and startups related to VR/AR. According to a report by Gartner, Inc. (2018), a global research and advisory firm,

VR/AR is one of the 10 core areas considered vehicles of the future information and communications technology market. VR involves interaction between a user and a 3D environment based on computer graphics or electronic simulations while wearing specific goggles and clothing. The concept of VR was introduced in the 1990s in the gaming industry and became popular after 2005, when it started being applied to various industries [47]. Meanwhile, AR is a 3D-vision complement added to the real environment in real time. Both VR and AR can be utilized in education, manufacturing, medicine, and design for various purposes. For realization of VR and AR, in addition to the technology itself, contents and wearable hardware are equally essential. Hence, the industry has potential to expand to markets for software, hardware, and content.

We collected 7005 USPTO patent applications from the WISDOM-AIN database using the keywords “augmented reality” and “virtual reality” [48]. Fig. 5 shows the number of patents applied for annually. Patents related to these fields first appeared in the early 1990s and reached a turning point in 2009 with an exponential increase. Patent applications from 2017 and 2018 are not all disclosed to the public.

Fig. 6 shows the number of patent applications by country. The United States applied for an overwhelming number of patents, followed by South Korea and Japan. Germany, England, France, and Finland are other countries that are ranked highly.

## 4.2. Preprocessing

For startup information, we used Crunchbase (www.crunchbase. com)—the largest startup company database, which includes company profiles and articles related to industry trends and investments [4]. The database has over 650,000 individuals and 400,000 companies from over 200 countries with well-sorted information pertaining to names, locations, founding dates, and management. This abundant data source can provide useful information for investors and researchers.

In this study, we mainly used startup profile texts. We collected the profiles of 2274 VR/AR-related startups (as of July 2018), but only 87 possessed patents [average 8.12, standard deviation (SD) 15.31]. Text data were preprocessed using a stopword process that excluded unnecessary words. Any meaningless repetitive terms such as “I,” “me,” “my,” and “is” were removed. Additionally, we eliminated the following general terms to focus on words relevant to a specific technology: “company,” “startup,” “patent,” “invention,” “application,” “method,” “drawing,” and “description.” Furthermore, stemming was applied to the text data to extract verb roots and delete special characters. Numeric information was also removed to prevent the inclusion of confusing information.

We also collected variables to evaluate the startups' potential. As shown in Table 2, a total of nine variables was extracted from 2274 startups with difering levels of potential. For example, Virtual Human

![](/api/attachments/G6KHHCQE/fulltext/images/f536abce919b00715e5f451fbfec66067d5c73ceb1668f7e875a104cd6c5df9a.jpg)  
Fig. 4. Recommendation map with technological similarity in terms of startup potential factors. M&A = merger and acquisition.

![](/api/attachments/G6KHHCQE/fulltext/images/d15ca3d2c1eb61f89451b2dabe7479646a071cba7f6f4dcfa5e2245613ba8d24.jpg)  
Fig. 5. Number of patent applications related to virtual reality and augmented reality (1990–2018).

Interaction Lab has the highest number of employees, as various university researchers participate in its projects. The number of articles also shows a large variance, because some startups that have already introduced their products have greater exposure to the public. For similar reasons, total revenue and total funding also have high variances. Therefore, the scale and magnitude of the potential variables vary. We standardized these variables by Z score before applying FA.

## 5. Experiment results

## 5.1. Experiment setting

This study utilized doc2vec to extract dense vectors that represent the technological concentrations of startups and patents. When a learning method for doc2vec is needed, a paragraph vector with distributed memory (PV-DM) and paragraph vector with distributed bag of words are often used [41]. We applied the PV-DM to extract technological vectors of the startups and patents and to obtain more precise vectors than would be obtained via the latter method, although the learning took longer.

![](/api/attachments/G6KHHCQE/fulltext/images/c2a3e67b620cec14fe1d14cb4f2771ece4dbe7d76fa6275cb0eb2f06c386501f.jpg)  
Fig. 6. Number of patents related to virtual reality and augmented reality by country and region.

Table 2  
Descriptive statistics of the variables for evaluation of startup potential.

<table><tr><td></td><td># of employees</td><td># of investors</td><td># of founders</td><td># of articles</td><td># of events</td></tr><tr><td>Average</td><td>30.88</td><td>1.19</td><td>1.63</td><td>9.9</td><td>0.66</td></tr><tr><td>Max</td><td>10,000</td><td>27</td><td>10</td><td>4164</td><td>21</td></tr><tr><td>Min</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr><tr><td>Std. dev</td><td>236.91</td><td>2.87</td><td>1.02</td><td>100.68</td><td>1.55</td></tr><tr><td></td><td>Total revenuea</td><td>Total fundinga</td><td># of competitors</td><td colspan="2"># of startup founding experience</td></tr><tr><td>Average</td><td>1,612,737</td><td>3,853,712</td><td>1274.8</td><td colspan="2">1.23</td></tr><tr><td>Max</td><td>8.04E+08</td><td>2.35E+09</td><td>1</td><td colspan="2">18</td></tr><tr><td>Min</td><td>0</td><td>0</td><td>1972</td><td colspan="2">1</td></tr><tr><td>Std. dev</td><td>22,651,679</td><td>52,361,266</td><td>660.36</td><td colspan="2">0.697</td></tr></table>

<sup>a</sup> In USD.

For the hyperparameters of the doc2vec, we needed to determine the window size representing the number of surrounding words from a central word as well as the dimension size of the document vector. In general. the selected window size was the average number of words in a sentence. With the window size set at 5, the average number of words in a sentence was 5.38 (SD = 2.83) for startup profiles and 5.05 (SD = 2.26) for patent abstracts. Normally, the quality of the vector dimension in doc2vec is assessed by visualizing the embedding space. The higher the quality of the vector, the closer the distance between similar types of startups in the visualization map (Pan et al., 2016). We highlight the top 10 startups based on their Crunchbase rank. These are divided into five categories (Table 3).

To create a two-dimensional visualization map, we conducted a principal component analysis with embedded vectors in a variety of dimensions. Fig. 7 shows the visualization map of the selected startups for the embedding spaces for the first two principal components. Startups in the vision and games categories (blue and green dots in the map) are located relatively close to each other on the maps of vector dimensions 200 and 400. However, startups in the games category are better clustered for vector dimension 400. To calculate the similarity between the patent vector of the company and the startup vector, we set the dimension size of the patent vector to 400.

## 5.2. Meaning of factors

Table 4 shows the result of the FA for the variables. We obtained four factors using the varimax method, which maximizes the sum of variances. The first factor is the level of public exposure, which includes the number of articles and instances of event participation. The second factor is network capability, which includes the number of investors, the founder's previous experience of founding startups, and members of the founding team. The third factor is the capitalization status based on total funding, revenue, and number of employees. The fourth factor is the originality of the startup's technology, which indicates the relative

## Table 3

Top 10 startups based on Crunchbase rank.

<table><tr><td>Startups</td><td>Category</td><td>Color</td></tr><tr><td>Immotion Group Plc.</td><td>Animation</td><td>Red</td></tr><tr><td>Niantic/Sphero/Improbable</td><td>Games</td><td>Green</td></tr><tr><td>vMocion, LLC</td><td>Motion</td><td>Magenta</td></tr><tr><td>Unity Technologies</td><td>Platform</td><td>Yellow</td></tr><tr><td>Magic Leap/Penrose Studios/High Fidelity/Mantis Vision</td><td>Vision</td><td>Blue</td></tr></table>

competition with other startups possessing similar technology. Each factor is then normalized using min–max normalization on a scale from 0 to 10. We extracted the top 100 companies for each of the four factors, respectively.

## 5.3. Startup recommendation map based on potential factors

For a brief visualization, we consider the top 20 startups for each factor. Since we derive four factors related to the potential of startups—public exposure, network capability, capitalization, and originality of technology—there are four recommendation maps in our visualization result from the perspective of each factor. As the recommendation map can difer according to the company (applicant), we choose the global information technology firm Samsung as an example.

Fig. 8 presents the recommendation map for technological similarity and public exposure of the top 20 companies. The cut-of level is 2.63. Startups such as MagicLeap and Oculus are already well known in the VR/AR field. MagicLeap has applied for the most patents, and Oculus has been developing its own product line of wearable goggles.

For exploitative M&A, Upload, Zappar, and HumanEyes emerge as recommended targets. These startups focus on the marketing opportunity that arises when users experience VR/AR services. As mentioned above, this type of M&A can strengthen the company's existing technology capacity and preempt the corresponding market by absorbing a potential competitor. Meanwhile, for exploratory M&A, Virtuix is a gaming company that sells interfaces for natural and free movement in the VR space. Therefore, Firm S can widen its technology portfolio and expect novel innovation by combining new ideas through such an M&A. Meanwhile, some companies wish to excavate diamonds in the rough. Hence, they seek startups with less exposure. This map can be used according to the company's needs.

Fig. 9 shows the top 20 startups with network capability and tech nological similarity. Companies' M&A directors and venture capitalists assign more credit to the information from networks, and startups with promising founders and acknowledgments from other market participants are considered more competitive. For the top 100 companies in terms of network capability, startups need to score over 2.26. #CNXTEch, which has the highest factor score, deals with product marketing in various technology fields, including VR/AR. They are strong in implementing viral marketing strategies using social media and internet platforms based on a global network to provide regionally customized services. As other exploitative M&A candidates, DenCity, ListingAR, and 500WONDERSLimited are recommended. Advanced Virtual, Qumranet, and NantMobile can be selected as exploratory M&A candidates, because they focus on AR/VR-related operating systems and VR interfaces.

Fig. 10 shows startups with capitalization scores over 1.14 as well as technological similarity. Large, global companies are relatively less concerned about the target's capital stability, whereas smaller compa nies are more inclined to choose more financially secure startups. TimeFireVR and Kogeto have similar technological capabilities. These startups are very safe from the technological and financial perspectives, enabling a more stable investment outcome. However, to widen the technological spectrum, Virtual Human Interaction Lab and ESIGroup could be appropriate options. Virtual Human Interaction Lab works on the comprehension of and efects of interactions in VR with researchers from diferent companies and countries. ESIGroup provides solutions for process simulation based on VR/AR. In conservative markets such as manufacturing, Firm S could achieve an eficient outcome from a merger with a startup such as ESIGroup.

![](/api/attachments/G6KHHCQE/fulltext/images/6ab596da08816f50cc744e707bdf22f6c7154f926a1ec2956e2a106ac8dc78a0.jpg)

![](/api/attachments/G6KHHCQE/fulltext/images/0554500bb592091ac51a556f9039d93f602492db05e16a9ccd781a6e51418b24.jpg)

![](/api/attachments/G6KHHCQE/fulltext/images/bef635f7bd426b24e51d9ac3aebc09e0aefbb0378b6f2174c651bf23532102a7.jpg)

![](/api/attachments/G6KHHCQE/fulltext/images/5656e5306cd7a50e3a5105464ffa6045357972192ecf3363835d6e221f15c5c6.jpg)

![](/api/attachments/G6KHHCQE/fulltext/images/b5ae2a1e0da1292e5a98f41ee16aee3418d96e6d45b911e73f3ebd35f81f906b.jpg)  
Fig. 7. Principal component analysis visualization of the embedded spaces on startups.

Fig. 11 plots technological similarity with technology originality. This factor considers the number of competitors with similar technological positions in the market. Therefore, we utilize the vectors from doc2vec and calculate the Euclidean distance among startups to see how many competitors exist within a certain bound. A higher score indicates that the startup has original technology. The scoring bench mark in terms of technology originality is 5.96, and Virtual Human Interaction Lab had the highest score. N-ix (R&D outsourcing startup)

![](/api/attachments/G6KHHCQE/fulltext/images/20b7aba508499befb612609618dd87d61db739dfd1bf5d1fb542e047d2a324ba.jpg)

and Oculus (VR/AR wearable devices) also ranked highly. Complementary startups include Virtual Human Interaction Lab, Getstigon (gesture recognition in VR), Advanced Virtual (AR/VR OS), and Vuzix (VR/AR wearables).

## 5.4. Combined startup recommendation map

We evaluated the potential startups from four diferent perspectives. Each company can select a perspective relevant to its interests and receive a list of M&A candidates. It is possible to create a master list of M& A candidates by evaluating potential startups through the combination of all four perspectives, which would indicate their overall potential. However, these perspectives would have to be weighted based on their relative importance prior to analysis—information that we are not privy to in advance. Therefore, we used the Crunchbase rank to comprehensively assess the potential of startups. The lower the Crunchbase rank, the more influential the startup is, in comparison with its peers. We selected the 20 most highly ranked startups in the VR/AR category.

Fig. 12 plots technological similarity based on the Crunchbase rank. The average and SD of the Crunchbase rank of 2305 startups is 168,697 and 143,265.8, respectively. A lower Crunchbase rank represents high potential for a startup in VR/AR. On the one hand, HiBloom.io, Sphero, VRtuoso, and Imporium Inc. have high degrees of technological similarity with Firm S, which is involved in VR/AR software development. However, MATSUKO (3D Telepresence) and Mantaray AR (AR education platform) could broaden the technology spectrum of Firm S.

Table 4  
Factor loadings by factor analysis.

<table><tr><td>Area</td><td>Variables</td><td>Factor1</td><td>Factor2</td><td>Factor3</td><td>Factor4</td></tr><tr><td>Public Exposure</td><td># of articles</td><td>0.43</td><td>-0.12</td><td>0.07</td><td>0.07</td></tr><tr><td>Public Exposure</td><td># of events</td><td>0.44</td><td>-0.05</td><td>-0.20</td><td>0.15</td></tr><tr><td>Network Capability</td><td># of investors</td><td>0.25</td><td>0.36</td><td>-0.07</td><td>-0.16</td></tr><tr><td>Network Capability</td><td># of startup founding experience</td><td>-0.27</td><td>0.65</td><td>0.26</td><td>0.16</td></tr><tr><td>Network Capability</td><td># of founders</td><td>0.06</td><td>0.53</td><td>-0.21</td><td>-0.08</td></tr><tr><td>Capitalization</td><td>Total funding*</td><td>0.29</td><td>-0.06</td><td>0.32</td><td>-0.16</td></tr><tr><td>Capitalization</td><td># of competitors</td><td>-0.02</td><td>-0.04</td><td>0.56</td><td>-0.20</td></tr><tr><td>Capitalization</td><td># of employees</td><td>-0.08</td><td>0.03</td><td>0.56</td><td>0.25</td></tr><tr><td>Technology Originality</td><td>Technology originality (1/# of competitors)</td><td>0.06</td><td>-0.02</td><td>-0.02</td><td>0.88</td></tr></table>

<sup>a</sup>In USD.

![](/api/attachments/G6KHHCQE/fulltext/images/f5710873a412ada0462e0b0a5f46b23febfcbf050da5eea67cbae996e0dfca29.jpg)  
Fig. 8. Recommendation map for technological similarity and public exposure.

## 6. Conclusion

In this study, we applied a PV-DM based doc2vec approach to the text of startup profiles to identify their technological position and recommend potential startups to acquiring companies based on technological similarity. Our framework exploits the logic of IBCF and FA to evaluate startups from four perspectives: public exposure, network capability, capitalization, and technological originality. Based on each factor and technological similarity, we recommended startups for exploitative and exploratory M&A. The proposed framework is applicable to real-world startups, and the technology of acquiring companies in the VR/AR field was examined as a case study. Companies can utilize this evaluative procedure in accordance with their own interests to identify high-potential targets for M&A.

We believe that our framework can reduce the efforts and resources needed to find strategically suitable startups, because the candidate lists are presented based on bibliographic information. Finding appropriate partners based on their technical positions in the market can help navigate the early stages of cooperation strategies for technological innovation. Furthermore, candidate lists generated according to the strategies and interests of the acquirer can support decision making regarding cooperation. In addition, reducing information asymmetry between startups seeking growth and companies looking to evolve through acquisition will not only benefit the direct participants but also bolster the entire industry.

Samsung Electronics - Competition  
![](/api/attachments/G6KHHCQE/fulltext/images/6cf8e5b640effece9b2a3456870653dec814c145cebd64293b92fcd886a2f1f6.jpg)  
Fig. 9. Recommendation map for network capability and technological similarity.

![](/api/attachments/G6KHHCQE/fulltext/images/eaeef300a3f9414c3036459b1205ec37ea27cdc42805ca54909be03c78f3feb9.jpg)  
Fig. 10. Recommendation map for capitalization and technological similarity.

![](/api/attachments/G6KHHCQE/fulltext/images/5472349a6ae68fe433bfb09715af0a2d9a8ca115fafa0041e49af2b89aa06d4c.jpg)  
Fig. 11. Recommendation map for technology originality and technological similarity.

![](/api/attachments/G6KHHCQE/fulltext/images/7dc9328068083abb3d54f7322ddee3feb348002de7e158203418185f3c5fac7c.jpg)  
Fig. 12. Recommendation map for combined potential factors and technological similarity.

Nevertheless, this study has some limitations. First, we identified the technology of companies through their own patents. However, most companies make a profit from their products, and thus, replacing patents with products could extend the scope of our framework. Second, this study can be expanded by considering external factors such as customer engagement and innovation spillover, as these are deemed to be critical factors for the success of startups. Such perspectives are qualitative and could improve the filtering process for potential can didates. Lastly, when integrating potential factors for startups, the Crunchbase rank was applied to recommend M&A candidates based on the combined potential factors. However, if a parent company assigns some prior weight to potential factors, such a prioritized list will help create a decision support system for M&As with startups. We expect future studies to address such limitations.

## Author contributions

Hyoung Jun Kim: Conceptualization; Methodology; Investigation; Writing – Original Draft; Writing – Review & Editing; Visualization.

Tae San Kim: Methodology; Software; Validation; Formal analysis; Data Curation; Writing – Review & Editing; Visualization.

So Young Sohn: Conceptualization; Writing – Review & Editing; Supervision; Project administration; Funding acquisition.

## Acknowledgement

The earlier Korean version of this paper, which was supervised by professor So Young Sohn, was awarded first place in the 14th KMAC Management Innovation Research Paper Competition in 2018.

## References

[1] N. Mukherji, B. Rajagopalan, M. Tanniru, A decision support model for optimal timing of investments in information technology upgrades. Decision Support Systems 42 (3) (2006) 1684–1696

[2] F. Hacklin, V. Raurich, C. Marxt, How incremental innovation becomes disruptive: the case of technology convergence, IEEE International Engineering Management Conference (IEEE Cat. No. 04CH37574), 1 2004, pp. 32–36.

[3] D.R. Crockett, J.E. McGee, G.T. Payne, Employing new business divisions to exploit disruptive innovations: the interplay between characteristics of the corporation and those of the venture management team. Journal of Product Innovation Management 30 (5) (2013) 856–879.

[4] Y.E. Liang, S.T.D. Yuan, Predicting investor funding behavior using crunchbase social network features, Internet Research 26 (1) (2016) 74–100.

[5] S.E. Reid, D. Roberts, K. Moore, Technology vision for radical innovation and its impact on early success, Journal of Product Innovation Management 32 (4) (2015) 593-609.

[6] G. Ahuja, C. Morris Lampert, Entrepreneurship in the large corporation: a long itudinal study of how established firms create breakthrough inventions, Strategic Management Journal 22 (6–7) (2001) 521–543.

[7] J. Carlos Nunes, E. Gomes Santana Félix, C. Pacheco Pires, Which criteria matter most in the evaluation of venture capital investments? Journal of Small Busines and Enterprise Development 21 (3) (2014) 505–527.

[8] B.K. Lee, S.Y. Sohn, Patent portfolio-based indicators to evaluate the commercial benefits of national plant genetic resources. Ecological Indicators 70 (2016) 43–52

[9] B.K. Lee, S.Y. Sohn, Exploring the efect of dual use on the value of military technology patents based on the renewal decision, Scientometrics 112 (3) (2017) 1203–1227.

[10] A. Omri, M.A. Frikha, M.A. Bouraoui, An empirical investigation of factors afecting small business success, Journal of Management Development 34 (9) (2015) 1073–1093.

[11] I.S. Heo, S.Y. Sohn, E.J. Ji, Efects of the matching fund program on IPO and bankruptcy of SMEs in Korea, Small Business Economics 42 (1) (2014) 117–129.

[12] A.L. Maxwell, S.A. Jefrey, M. Lévesque, Business angel early stage decision making, Journal of Business Venturing 26 (2) (2011) 212–225

[13] J.K. Schneider. M. Dowling, S. Raghuram. Empowerment as a success factor in startup companies, Review of Managerial Science 1 (2) (2007) 167–184.

[14] A.R.M. Toganel. M. Zhu. Success Factors of Accelerator Backed Ventures: Insights From the Case of TechStars Accelerator Program. (2017).

[15] W. Watson, W.H. Stewart Jr., A. BarNir, The efects of human capital, organiza tional demography, and interpersonal processes on venture partner perceptions of firm profit and growth, Journal of Business Venturing 18 (2) (2003) 145–164.

[16] M. Song, K. Podoynitsyna, H. Van Der Bij, J.I. Halman, Success factors in new ventures: a meta-analysis, Journal of Product Innovation Management 25 (1) (2008) 7–27.

[17] C. Arruda, V.S. Nogueira, V. Costa, The Brazilian entrepreneurial ecosystem of startups: an analysis of entrepreneurship determinants in Brazil as seen from the OECD pillars, Journal of Entrepreneurship and Innovation Management 2 (3) (2013) 17–57.

[18] À.C. Cooper, F.J. Gimeno-Gascon, C.Y. Woo, Initial human and financial capital as predictors of new venture performance, Journal of Business Venturing 9 (5) (1994) 371–395.

[19] F. Bertoni, M.G. Colombo, L. Grilli, Venture capital financing and the growth of high-tech start-ups: disentangling treatment from selection efects, Research Policy 40 (7) (2011) 1028–1043.

[20] E. Gomes, D.N. Angwin, Y. Weber, S. Yedidia Tarba, Critical success factors through the mergers and acquisitions process: revealing pre-and post-M&A connections for improved performance, Thunderbird International Business Review 55 (1) (2013) 13-35.

[21] C. Grimpe, K. Hussinger, Market and technology access through firm acquisitions: bevond one size fits all. New Perspectives in International Business Research. Emerald Group Publishing Limited. 2008, pp. 289–314

[22] S. Chatterjee, The keys to successful acquisition programmes, Long Range Planning 42 (2) (2009) 137–163.

[23] P. Datta, Y. Roumani, Knowledge-acquisitions and post-acquisition innovation performance: a comparative hazards model. European Journal of Information Systems 24 (2) (2015) 202–226.

[24] F. Bauer, K. Matzler, Antecedents of M&amp;A success: the role of strategic com plementarity, cultural fit, and degree and speed of integration, Strategic Management Journal 35 (2) (2014) 269–291.

[25] C. Grimpe. K. Hussinger, Pre-empting technology competition through firm acqui sitions, Economics Letters 100 (2) (2008) 189–191.

[26] M. Wagner, To explore or to exploit? An empirical investigation of acquisitions by large incumbents, Research Policy 40 (9) (2011) 1217–1225

[27] A.B. Sorescu, R.K. Chandy, J.C. Prahbu, Why some acquisitions do better than others: product capital as a driver of long-term stock returns, Journal of Marketing Research 44 (2007).57-72

[28] S. Basu, A. Wadhwa, External venturing and discontinuous strategic renewal: an options perspective, Journal of Product Innovation Management 30 (5) (2013) 956–975.

[29] U. Stettner, D. Lavie, Ambidexterity under scrutiny: exploration and exploitation via internal organization, alliances, and acquisitions, Strategic Management Journa 35 (13) (2014) 1903–1929.

[30] Y. Dang, Y. Zhang, P.J.H. Hu, S.A. Brown, H. Chen, Knowledge mapping for rapidly evolving domains: a design science approach, Decision Support Systems 50 (2) (2011) 415–427.

[31] T. Kohler, Corporate accelerators: building bridges between corporations and startups, Business Horizons 59 (3) (2016) 347–357.

[32] G. Dushnitsky, J.M. Shaver, Limitations to interorganizational knowledge acquisi tion: the paradox of corporate venture capital, Strategic Management Journal 30 (10) (2009) 1045–1064.

[33] R. Siegel, E. Siegel, I.C. MacMillan, Corporate venture capitalists: autonomy, ob stacles, and performance. Journal of Business Venturing 3 (3) (1988) 233–247.

[34] J.A. Baum, T. Calabrese, B.S. Silverman, Don’t go it alone: Alliance network com position and startups’ performance in Canadian biotechnology, Strategic Management Journal 21 (3) (2000) 267–294.

[35] L. Huang, L. Shang, K. Wang, A.L. Porter, Y. Zhang, Identifying target for technology mergers and acquisitions using patent information and semantic analysis, Management of Engineering and Technology (PICMET). 2015 Portland International Conference on, IEEE, 2015, August, pp. 2313–2321.

[36] P. Saviotti, M.A. De Looze, M.A. Maupertuis, Knowledge dynamics, firm strategy, mergers and acquisitions in the biotechnology based sectors, Economics of Innovation and New Technology 14 (1–2) (2005) 103–124.

[37] H. Park, J. Yoon, K. Kim, Identification and evaluation of corporations for merger and acquisition strategies using patent information and text mining, Scientometric 97 (3) (2013) 883–909

[38] C.P. Wei, C.S. Yang, H.W. Hsiao, A collaborative filtering-based approach to personalized document clustering, Decision Support Systems 45 (3) (2008) 413–428.

[39] M. Balabanović, Y. Shoham, Fab: content-based, collaborative recommendation, Communications of the ACM 40 (3) (1997) 66–72.

[40] G. Linden, B. Smith, J. York, Amazon.com recommendations: item-to-item collaborative filtering, IEEE Internet Computing 1 (2003) 76–80.

[41] T. Mikolov, K. Chen, G. Corrado, J. Dean, Efficient Estimation of Word

Representations in Vector Space, (2013) arXiv preprint arXiv:1301.3781.

[42] Q. Le, T. Mikolov, Distributed representations of sentences and documents, International Conference on Machine Learning, 2014, January, pp. 1188–1196.

[43] X. Wang, K. Zhao, S. Cha, M.S. Amato, A.M. Cohn, J.L. Pearson, ... A.L. Graham Mining user-generated content in an online smoking cessation community to identify smoking status: A machine learning approach, Decision Support Systems 116 (2019) 26–34.

[44] P. Almeida, G. Dokko, L. Rosenkopf, Startup size and the mechanisms of external learning: increasing opportunity and decreasing ability? Research Policy 32 (2) (2003) 301–315.

[45] J.W. Suh, S.Y. Sohn, Adaptive conjoint analysis for the vitalisation of angel investments by entrepreneurs, Technology Analysis & Strategic Management 28 (6) (2016) 677–690.

[46] S.Y. Sohn, Y. Kim, Searching customer patterns of mobile service using clustering and quantitative association rule, Expert Systems with Applications 34 (2) (2008) 1070–1077.

[47] M. Zyda, From visual simulation to virtual reality to games, Computer 38 (9) (2005) 25–32.

[48] Y. Ju, S.Y. Sohn, Patent-based QFD framework development for identification of emerging technologies and related business models: a case of robot technology in Korea, Technological Forecasting and Social Change 94 (2015) 44–64.

So Young Sohn received the Ph.D. degree from the Department of Industrial Engineering, University of Pittsburgh, USA in 1989. She is currently Professor of Department of Information & Industrial Engineering, Yonsei University, Seoul, Korea. Her current research interests include technology management, marketing, quality and reliability engineering. Detailed information about her teaching and research areas can be found at http://isl.yonsei.ac.kr.

Hyoung Jun Kim received master's degree in Industrial Engineering from Yonsei University. His research area includes technology management and spatial data mining. He is currently focusing on developing advanced credit scoring system at NICE Information Service. E-mail address: junkim1003@gmail.co.kr

Tae San Kim is a graduate student at the Department of Information and Industrial Engineering, Yonsei University. His research area includes technology Management and data mining.
