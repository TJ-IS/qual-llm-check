---
otero_id: 19776
otero_key: "TAXRGC7P"
title: "Prediction of initial coin offering success based on team knowledge and expert evaluation"
authors: "Wei Xu; Ting Wang; Runyu Chen; J. Leon Zhao"
year: "2021"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2021.113574"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Prediction of initial coin offering success based on team knowledge and expert evaluation

![](/api/attachments/TAXRGC7P/fulltext/images/d3bdfe9ae4b336be931387dbcab04171ad4b3132d50dca60dd2b3c751177c789.jpg)

Wei Xu <sup>a</sup>, Ting Wang <sup>a</sup>, Runyu Chen <sup>b,\*</sup>, J. Leon Zhao <sup>c</sup>

<sup>a</sup> School of Information, Renmin University of China, Beijing, 100872, PR China

<sup>b</sup> School of Information Technology and Management, University of International Business and Economics, Beijing, 100029, PR China

<sup>c</sup> School of Management and Economics, Chinese University of Hong Kong, Shenzhen, PR China

## A R T I C L E I N F O

Keywords: Initial coin offerings Cryptocurrency Heterogeneous knowledge Text analytics

## A B S T R A C T

Initial coin offering (ICO) is a new financing method that has been widely used in cryptocurrency projects. However, it has been reported that nearly 30% of cryptocurrency projects fail during ICO, indicating an important gap in research and an opportunity for more advanced research on ICO project assessment. This study reveals that previous studies primarily used project-related factors to predict ICO success while neglecting social factors such as team information and expert evaluation. Inspired by the knowledge-based theory (KBT) of the firm, we set out to examine the impact of heterogeneous team knowledge and expert evaluation on ICO success. One primary contribution of this study is the design of novel knowledge measures based on KBT. In addition, we propose a deep-learning model – an attention-based bidirectional recurrent neural network (A-BiRNN) – to automatically extract features from online comments. We validate the proposed model on a real-world dataset, and experiments show that the accuracy of the proposed prediction model outperforms those of existing models by more than 6%, highlighting the effectiveness of the proposed approach in predicting ICO success. This study’s results provide useful ideas for both investors and ICO platforms to assess the quality of cryptocurrency projects, thus improving information symmetry in ICO markets. Also, this study demonstrates the value of applying KBT in assessing firm performance in ICO markets. The generalized value of the proposed approach should be tested in more business contexts, such as crowdfunding and peer-to-peer (P2P) lending.

## 1. Introduction

Due to the rising price of Bitcoin and the development of blockchain technology, cryptocurrencies have attracted much attention in recent years [1,2]. Most cryptocurrencies (e.g., Ethereum) undergo a financing stage to increase money prior to public trading. Based on smart contract technology [3], a new financing method called initial coin offering (ICO) has been widely applied to cryptocurrency projects. ICOs are a special form of crowdfunding that raises funds from the public by issuing tokens [4]. The primary innovation of ICOs is that they allow entrepreneurs to raise large amounts of money in a short time with little effort while avoiding transaction costs [5]. ICO investors can obtain significant financial returns by selling or transferring their rewards to someone else in the secondary market, which cannot be achieved via traditional crowdfunding platforms [6]. The development and novel characteristics of ICOs have attracted the interest of many entrepreneurs and investors.

According to ICObench,<sup>1</sup> as of January 2021, more than 5000 projects had been launched by ICOs, raising more than \$27 billion USD.

For investors, ICOs provide a good opportunity to invest in crypto currencies but can also present marked risk. Lack of regulation and in formation asymmetry are the primary causes of the high investment risk inherent to ICOs [7]. In such a high-risk investment environment, how to use limited information to judge the probability of ICO success is a key task. An ICO project is considered a failure if the raised money does not meet the predetermined goal within a specified time. Failed projects make it difficult for project members to implement their ideas and also hurt investors. Therefore, it is critical to evaluate ICO performance prior to investing. We aim to design an accurate prediction model that can identify the determinants of ICO success, which can alleviate investment risks and provide effective assistance to investors for decision making.

Previous research in this area has examined the impact of many factors on ICO success, including project-related information and social media information [5,7,8]. However, unlike traditional crowdfunding projects, ICO projects usually have several team members, such as startups. Although previous studies have examined the impact of team information on ICO success, they considered only the number of team members. From the perspective of knowledge-based theory (KBT) [9], heterogeneous team knowledge is the most important strategic resource of a company and plays a positive role in the improvement of firm performance. Therefore, we aim to explore the impact of the heteroge neous team knowledge of ICOs on ICO success. In this study, we collected detailed personal information about team members from LinkedIn<sup>2</sup> and then constructed three dimensions (work experience, innovation ability and social connection) to evaluate the heterogeneous knowledge of team members. These features allow investors to have a comprehensive understanding of project team members. A better team has a greater probability of developing a successful project; thus, more investors decide to invest in such a project during the ICO process.

In addition to project-related information, ICObench also allows blockchain experts to evaluate ICO projects. Previous studies have demonstrated that online evaluations can influence customer purchase decisions [10,11]. Therefore, expert evaluations have a high probability of influencing potential investors in token purchase decisions. In addi tion to ratings [12], this study innovatively considers evaluation com ments in the proposed model. Because we are not sure which textual features are more important for ICO investors, an attention-based bidi rectional recurrent neural network (A-BiRNN) is proposed to automat ically extract features from comments [13]. The A-BiRNN model introduces an attention mechanism that can automatically capture important textual features. To improve result interpretability, we visu alize the weight of comment words with a heat map. The experimental results demonstrate that the proposed A-BiRNN model extracts more valuable textual features than baselines.

In summary, the primary contributions of this study are fourfold. First, we design an ICO success prediction model that combines het erogeneous team knowledge, expert evaluation information and other project-related features. Second, based on KBT, we design a new mea sure to estimate individual knowledge for ICO project team members. Third, to better understand investors’ attention in expert evaluation, we propose an A-BiRNN model to extract textual features from expert comments. Finally, we conduct an empirical analysis with a real-world dataset. The experimental results demonstrate the effectiveness of both team knowledge and expert evaluation in predicting ICO success. To our knowledge, this is the first study to consider either team knowledge or expert evaluations in the prediction of ICO success. The managerial implications of this study are as follows. Based on the pro posed prediction model, potential investors can prejudge failure risk and then invest in reliable cryptocurrency projects in ICOs. Therefore, in formation symmetry can be improved, which aids the healthy devel opment of ICO markets. From the perspective of KBT, this study demonstrates that heterogeneous team knowledge can affect ICO per formance. Because ICO is a special financing method, this study also provides insights that could help a team with heterogeneous knowledge increase funding.

The rest of this paper is organized as follows. Section 2 reviews the concepts and theories involved in this study and summarizes related studies. Section 3 describes the proposed ICO success prediction framework. Then, the proposed computational methods are explained in detail in Section 4. Sections 5 and 6 describe the experimental setup and results, respectively. The last section presents a summary and directions for future research.

## 2. Related work

## 2.1. Determinants of ICO success

ICO is a method for blockchain companies to increase funds by issuing tokens, which we also call cryptocurrencies (e.g., Ethereum) [7]. As a low threshold and fast financing method, ICOs provide a new development opportunity for small startups. As an open-source business model, all investors can participate in a project’s financing process by purchasing tokens, which is seen as a new form of crowdfunding but is completely decentralized. However, compared with other crowdfunding projects, the products of ICOs are relatively obscure and exhibit more information asymmetry and higher investment risks [5].

When launching an ICO project, a team typically publishes a whitepaper that describes the project in detail. The content of the whitepaper includes the project background, technical characteristics, team, quantity, price of the issued tokens, and the use plan after raising funds [8]. An ICO project usually lasts for a specific period, ranging from a few days to several months, as determined in advance by the project team. If the goal of an ICO is achieved or if the specified time runs out, then the ICO ends [7]. Some ICO projects have a presale before the official public offering, which is a private placement, primarily to attract some early investors to join the team. The price in the presale stage is lower than that of the official issue, and generally, more bonuses can be obtained after project completion [8]. An ICO project is considered successful if the money raised after the end of the project reaches the fundraising goal (soft cap or hard cap) set by the team; otherwise, the project is considered a failure.

If investors invest in a failed ICO project, then the purchased token may not be traded online, which will lead to great losses for investors. In addition, the entire ICO market lacks strict regulation, thus leading to a higher investment risk [7]. Many scholars have begun to study what determines the success of ICO projects. Fisch et al. [5] found that technical whitepapers and high-quality source codes increased the final funding for such projects, but patents had no significant impact. Chen [7] conducted further research on ICOs’ source codes and found that the availability of source codes has a certain impact on token sales, but the content of source codes was not an effective indicator, which may be because the source code is difficult to interpret and has a high threshold for most nonprofessionals. In addition, Chen also found that investors comments on social media affect the credibility of enterprises [7]. Fenu et al. conducted a multivariate regression analysis to evaluate the key factors that affect ICO success. Experimental results showed that expert ratings were highly correlated with success, but team size was not important [12].

Although team information and expert evaluation have been studied in previous studies [12], previous researchers only considered team size and expert ratings. In this study, we extract many more valuable features from heterogeneous team knowledge and expert comments, contrib uting to existing research.

## 2.2. Knowledge-based theory in competitive advantages

Knowledge-based theory (KBT) considers knowledge to be the most important strategic resource of a company [9], which is the outgrowth of the resource-based view (RBV) [14]. The RBV holds that heterogeneous resources owned by firms can enable firms to obtain stable competitive advantages over time [15]. However, the existing resources of firms and the knowledge, particularly heterogeneous knowledge, of firms is considered in the KBT. Supporters of this theory believe that resources are easy to imitate, transfer and replace, but that knowledge is difficult to imitate and transfer due to its particularity and complexity, which is the key factor in determining firm competitiveness [16,17]. Heteroge neous knowledge is an important driver of a firm’s innovation and performance, and is defined as a variety of technological knowledge, know-how, and expertise [18]. Firms with heterogeneous knowledge can offset weak individual knowledge, thereby improving creativity and competitive advantages [19]. Although firms are supposed to have learning capabilities, the generation and innovation of firm knowledge depend on the individual knowledge of employees [20,21]. Therefore, the heterogeneous knowledge of a company also markedly depends on that of individuals.

Many scholars have made contributions to the study of individual knowledge. Practical knowledge can be defined as the ability to put into practice previously acquired in specific circumstances [22], which is a primary factor in determining individual knowledge. Employees with rich practical knowledge know how to act at work and are more likely to create value for the firm [22]. Practical knowledge comes from the accumulation of previous experience, whether it is educational experi ence or work experience [23]. In addition, innovation ability is another key outcome of mastering knowledge. Innovation ability refers to the ability to create new ideas and value for a business by identifying and using opportunities in a specific environment [24]. Lawson et al. [25] consider it the ability to continuously transform knowledge into new products that ultimately benefit the firm. Employees with innovative abilities make full use of existing resources to create value and also bring new intangible assets to their firms, which can help firms improve their competitiveness and achieve better performance [26,27]. The compet itive advantage brought by innovation is due to asymmetries in knowledge across organizations [24]. However, much knowledge is implicit and difficult to transfer. Only the exchange and sharing of knowledge can bring different knowledge sources together and manip ulate it into new knowledge, promote the transformation of individual knowledge to organizational knowledge, and ultimately improve the competitive advantage of the organization [28]. Also, research on organizational social networks reveals that people are more likely to generate good ideas and create new knowledge by interacting with people they know in the same setting or in other companies [29]. Social connections are a prerequisite for having opportunities to communicate with people in different organizations and are thus also significant in the promotion of individual knowledge [30].

Therefore, based on previous studies, we measure individual knowledge in three dimensions: work experience, innovation ability and social connection. Because heterogeneous knowledge represents stable competitive advantages, we innovatively consider the impact of het erogeneous knowledge on financial performance based on real-world ICO project data.

## 2.3. Online evaluation analysis

In online commercial activities, information asymmetry is an important issue. To address this problem, many platforms use evalua tions developed by previous users or authoritative experts to provide a reference for new users.

In e-commerce, many scholars have studied the impact of online evaluations on purchasing behavior and found that evaluations signifi cantly influence customers’ purchase decisions and product sales per formance [31–33]. To analyze these evaluation comments, scholars typically adopt SA methods. Hu et al. [10] used the term frequency approach to categorize the sentiments of the title and content into four classes: strong positive, strong negative, modal positive, and modal negative. Li et al. [34] proposed a joint sentient topic (JST) model. Traditional SA can only obtain the valence of comments but cannot reveal which aspect the reviewer truly prefers.

In addition, some researchers have also studied the influence of on line evaluations on crowdfunding platforms. ICO is a special form of crowdfunding that raises money by issuing tokens. Deyet al. [35] explained that endorsement can help backers gain trust. Considering experts’ evaluation of researchers’ competence and project feasibility, the authors developed a topic taxonomy model to determine which characteristics are significant to final project success. Courtney et al. [36] studied the influence of backers’ sentiment on crowdfunding success, and experimental results show that the stronger the positive emotion of backers is, the greater the possibility of crowdfunding success.

Project teams increase funds by selling tokens during the ICO pro cess. Thus, the role of tokens is similar to that of products in e-com merce. Because online evaluation analysis is valuable in both ecommerce and crowdfunding, this study contributes to evaluating its effectiveness in ICOs. Because deep-learning technology has developed in recent years, it has also shown great advantages in natural language processing (NLP) and automatic feature learning [13]. In this study, we use deep learning methods to extract features from comments auto matically to complete this task.

## 2.4. Main differences between our work and previous studies

Our work differs from previous studies in the following four ways. First, while previous studies primarily consider project-related features, we construct the proposed ICO success prediction model based on project team members and expert evaluations. Second, to our knowl edge, no study has examined whether heterogeneous knowledge of the project team can achieve better performance in ICO success predictions. Based on the KBT, we measure heterogeneous team knowledge and verify its effectiveness in the proposed model. Third, previous studies only considered the impact of ratings on ICO performance. In this study, we consider comments when predicting ICO success. In particular, we propose an A-BiRNN to perform textual feature extraction on comments to capture important textual features automatically. Finally, previous studies primarily focus on ICO performance, while we aim to predict ICO success. Experimental results can be used to help investors make a purchase decision and also contribute to the reasonable design of funding goals in cryptocurrency projects during ICO.

## 3. Proposed framework for ICO success prediction

Most previous studies have focused on the impact of project-related information on ICO performance, and few have considered the impact of expert evaluation and the heterogeneous knowledge of project team members on ICO success. In this study, project-related information, expert evaluation, and heterogeneous team knowledge are innovatively combined. The proposed ICO success prediction framework is shown in Fig. 1 and consists of three primary processes: data collection, feature extraction and success prediction.

## 3.1. Data collection

We collect data from ICObench using a Python web crawler. ICO bench is a free ICO information platform and a blockchain community that is supported by a wide range of experts to provide analytical, legal, and technical insights. Compared to other platforms, ICObench provide rich and comprehensive project information, and contains project evaluations from more than 300 active experts, including more than 17,000 ratings and comments. In addition, ICObench also provides an intelligent bot called ICO Analyzer<sup>3</sup> that analyzes projects automatically to help investors make decisions. As of January 2021, there were more than 5700 published ICO projects on this platform with a total of \$27 billion raised.

A Python-based web crawler is developed to crawl ICO projects and their related attribute information from this website. A project is described by name, brief introduction, team, financial data, ratings, and whitepaper. In addition, we also captured the report of ICO Analyzer for each project, including LinkedIn profiles, informativeness of white paper, etc. Also, because we want to study the impact of the heteroge neous team knowledge of ICOs’ teams on project success, we also crawl the personal information of the project team members’ webpages on LinkedIn, the world’s largest professional social networking site.

![](/api/attachments/TAXRGC7P/fulltext/images/e6a2f0486688ba32c01cef99aad73eea2978d5fa5c961cbee102bb7046a533fd.jpg)  
Fig. 1. ICO success prediction framework.

## 3.2. Feature extraction

Because not all features can be directly fed into the prediction model, we perform more feature engineering. We calculate the duration of an ICO project as a new feature using the ICO start time and end time. In addition, most ICO project teams are new organizations or are created by drawing people from different departments within the original company, leading to many challenges in terms of internalizing and creating new knowledge [20]. Therefore, at the individual level, we measure heterogeneous knowledge in three dimensions: work experi ence, innovation ability and social connection. The heterogeneous knowledge of a team is the fusion of all individuals, and the specific assessment method we propose will be described in Section 4.1. To extract features from comments, we propose a model called A-BiRNN to learn textual features automatically. The implementation of the model is described in Section 4.2.

All obtained features and their descriptions are shown in Table 1. These features, except for team knowledge and expert comments, are input to the model as numerical features.

## 3.3. Prediction of ICO success

Because the number of existing ICO projects is limited and relatively small, we propose a simple multilayer perceptron (MLP) to predict the ICO project success. We add a softmax layer to the MLP output layer to implement the classification problem. For the proposed ICOs, successful projects are marked as ‘1’, and failed projects are marked as ‘0’. We divide all data into training, validation and testing sets, and use the training set to train the MLP classifier in advance. Next, the trained classifier is used to predict the results of the testing set. Finally, we compare the prediction results with the real results and select some evaluation criteria to evaluate model performance.

Table 1  
Feature descriptions.

<table><tr><td>Feature</td><td>Type</td><td>Descriptions</td></tr><tr><td>Sale Price</td><td>Numerical</td><td>Price of the coin issued by an ICO project</td></tr><tr><td>Duration</td><td>Numerical</td><td>Duration of an ICO project</td></tr><tr><td>Bonuses</td><td>Binary</td><td>Whether there are bonuses</td></tr><tr><td>Number of members</td><td>Numerical</td><td>Number of team members of an ICO</td></tr><tr><td>ICO success score &gt; 5</td><td>Numerical</td><td>Number of members with ICO success Score greater than 5</td></tr><tr><td>LinkedIn profiles</td><td>Numerical</td><td>Number of members with links to their LinkedIn profiles</td></tr><tr><td>Team knowledge</td><td>Numerical</td><td>Personal information of team members</td></tr><tr><td>Benchy</td><td>Numerical</td><td>Rating of an ICO&#x27;s analyzer on a project</td></tr><tr><td>Team</td><td>Numerical</td><td>Rating of an ICO project&#x27;s team</td></tr><tr><td>Vision</td><td>Numerical</td><td>Rating of an ICO project&#x27;s vision</td></tr><tr><td>Product</td><td>Numerical</td><td>Rating of an ICO project&#x27;s product</td></tr><tr><td>Number of experts ratings</td><td>Numerical</td><td>Number of experts involved in rating</td></tr><tr><td>Expert reviews</td><td>Textual</td><td>Reviews of experts on ICO projects</td></tr><tr><td>Whitepaper</td><td>Binary</td><td>Whether there is a whitepaper</td></tr><tr><td>Informativeness of whitepaper</td><td>Numerical</td><td>Informativeness of whitepaper</td></tr><tr><td>GitHub</td><td>Binary</td><td>Whether there is source code on GitHub</td></tr><tr><td>Reddit</td><td>Binary</td><td>Whether there are activities on Reddit</td></tr><tr><td>Bitcointalk</td><td>Binary</td><td>Whether there are activities in Bitcointalk</td></tr></table>

## 4. Computational methods

## 4.1. Heterogeneous knowledge assessment

The first step of individual knowledge assessment is to determine its underlying influencing factors. Based on the review of the relevant literature in Section 2.2 and the data obtained from LinkedIn and ICO bench, we measure individual heterogeneous knowledge in three di mensions: work experience, innovation ability and social connection. Table 2 lists the evaluation criteria of the measures, and the details are discussed in the following subsections.

## 4.1.1. Work experience

Practical knowledge comes from the accumulation of previous experience [23]. Employees with rich practical knowledge are more likely to create value for the firm [22]. For this dimension, we construct three indicators to measure individual previous work experience, which include knowledge breadth (KB), knowledge depth (KD) and business process (BP).

Table 2  
Evaluation criteria of individual heterogeneous knowledge.

<table><tr><td>Dimension</td><td>Subdimension</td><td>Description</td></tr><tr><td rowspan="3">Work experience</td><td>Knowledge breadth (KB)</td><td>Breadth of knowledge learned from work</td></tr><tr><td>Knowledge depth (KD)</td><td>Depth of knowledge learned from work</td></tr><tr><td>Business process (BP) (Know-How)</td><td>Knowledge of the ICO business process</td></tr><tr><td rowspan="2">Innovation ability</td><td>Qualification certificate (QC)</td><td>Innovation ability reflected in work</td></tr><tr><td>External evaluation (EE)</td><td>Competence certification from other people</td></tr><tr><td rowspan="3">Social connection</td><td>Social ties (ST)</td><td>Social friends</td></tr><tr><td>Business communication (BC)</td><td>Business partners</td></tr><tr><td>Willingness to share (WS)</td><td>Willingness to share knowledge</td></tr></table>

KB: If a person is engaged in more industry categories, then the person’s KB will be greater. In this study, we only consider up to 5 recent jobs per person.

First, we consider the set of industries $I = \{ I _ { 1 } , I _ { 2 } , I _ { 3 } , \cdots , I _ { n } \}$ and the set of companies $C _ { i } = \{ C _ { i 1 } , C _ { i 2 } , C _ { i 3 } , \cdots , C _ { i m } \}$ of industry $I _ { i } , d _ { i j }$ is the number of fields covered by company $C _ { i j } .$ Then, the largest number of fields covered by industry I is $D _ { i } = \operatorname* { m a x } { ( d _ { i 1 } , d _ { i 2 } , d _ { i 3 } , \cdots , d _ { i m } ) } . r _ { i j }$ is the percentage of the fields that company $C _ { i j }$ focuses on as follows:

$$
r _ {i j} = \frac {d _ {i j}}{D _ {i}}\tag{1}
$$

Second, at the individual level, $C = \{ C _ { 1 } , C _ { 2 } , \cdots C _ { p } \}$ is the set of com: panies with which a person has recently engaged, and $I = \{ I _ { 1 } , I _ { 2 } , \cdots , I _ { q } \}$ is the set of industries corresponding to these companies $( 1 \leq p \leq q \leq 5 )$ . KB describes the personal KB, which is defined as follows:

$$
K B = \frac {6}{5} \left(1 - \frac {1}{q + 1}\right) \frac {\sum_ {k = 1} ^ {q} r _ {k}}{q}\tag{2}
$$

If more than one company in an individual’s work experience be longs to the same industry, then $r _ { k }$ is the maximum of the proportion of these companies’ fields. The maximum value of KB is 1, and the mini mum value approaches 0. If a person has worked for five companies in different industries, and if these 5 companies have the largest number of fields in their industry $( r _ { k } = 1 )$ , then KB equals the maximum value of 1.

KD: If a person works longer in an industry, then the person’s KD will be greater.

Considering a person’s recent industry set $I = \{ \ I _ { 1 } , I _ { 2 } , \cdots , I _ { q } \}$ , the corresponding working time set in each industry is $T = \{ \mathit { T } _ { 1 } , \mathit { T } _ { 2 } , \cdots , \mathit { T } _ { q } \}$ KD describes the personal KD, and $T _ { s t d }$ is the standard deviation of the working time set T:

$$
\mathrm{KD} = \frac {\sum_ {\mathrm{k} = 1} ^ {\mathrm{q}} \mathrm{T} _ {\mathrm{k}}}{\mathrm{q}} * (l n (\mathrm{T} _ {\mathrm{std}} + 1) + 1)\tag{3}
$$

BP: In this study, we use the number of ICO projects in which an individual is involved to value this item: the more ICOs an individual was previously involved in, the more knowledge they have likely gained about how to perform an ICO project.

## 4.1.2. Innovation ability

Employees with innovative abilities can make full use of existing resources to create value and also bring new intangible assets to their firms $[ 2 6 , 2 7 ]$ . Due to the interaction of various factors. the innovation process is complex and multidimensional [37]. Therefore, innovation ability is also defined as a broad concept, which is a combination of various abilities that an individual performs in his work. In this study, we use qualification certification (QC) and external evaluation (EE) to evaluate individual innovation ability from internal and external as pects, respectively.

QC: Qualification certification is the certification of required knowledge and ability to engage in a certain job. Qualification certifi cation demonstrates the knowledge and ability of the practitioner, and the ability level he has achieved. In this study, we use the number of qualifications that an individual has been certified on LinkedIn to measure this item.

EE: External evaluation refers to others’ comprehensive evaluation of an employee’s performance at work. In this study, we measure this item by the number of recommendation letters a person has received on LinkedIn. The number of recommendation letters can reflect a person’s recognition in their work.

## 4.1.3. Social connection

Social connections are a prerequisite for having the opportunity to communicate with people in different organizations, and individual knowledge can be promoted through knowledge sharing and creation [30]. In this study, we design three indicators called social ties (ST), business communication (BC) and willingness to share (WS) to measure an individual’s social connection scores.

ST: ST refers to the social network structure and tie strength, which is one of the basic conditions for knowledge sharing and creation. In this study, we measure this item by counting the number of friends that each individual has on LinkedIn.

BC: Compared to ordinary friends, business partners may have an influence on people’s professional knowledge that they use in their work more directly. The significant role of business communication in enhancing business knowledge and thus affecting firm performance was also demonstrated in a previous study [38]. In this study, we use the number of partners that an individual has on all relevant business teams to measure the BC score.

WS: Knowledge sharing is a voluntary process, and individuals are not likely to share their knowledge. People who like to share tend to be active and share with others on social media. Therefore, we measure this item by the number of articles shared on LinkedIn.

After calculating these items, we construct heterogeneous team knowledge based on the fusion of all individuals. The proposed method aims to equally fuse all individuals through average pooling.

## 4.2. Expert comments feature extraction (A-BiRNN)

We propose a bidirectional recursive neural network based on an attention mechanism (A-BiRNN) to extract the features of expert com ments automatically. As shown in Fig. 2, the sketch of the proposed A-BiRNN architecture contains three components: Word embedding, BiRNN and attentional mechanisms.

## 4.2.1. Word embedding

In the experiments, we use the pretrained BERT [39] to obtain the embedding of each word and use it as input word embeddings throughout the experiments. The BERT model architecture is based on a multiple-layer transformer encoder and can learn powerful representa tions from unlabeled text.

For a paragraph (comment) P consisting of n words, $P = \{ x _ { 1 } , x _ { 2 } , x _ { 3 } .$ $x _ { n } \} ,$ and each word $x _ { i }$ is converted into a 768-dimensional vector through the pretrained BERT. Then, the representation of the paragraph is $E _ { p } = \{ e _ { 1 } , e _ { 2 } , e _ { 3 } . . . e _ { n } \}$

## 4.2.2. BiRNN with GRU cells

The RNN model is known to exhibit gradient explosion or vanishing in certain cases. To avoid these problems, we introduce gated recurrent unit (GRU) cells in the proposed model. GRU cells are a variant of long short-term memory (LSTM) cells that contain two gates (an update gate and a reset gate) to decide which information to discard and which new information to add.

![](/api/attachments/TAXRGC7P/fulltext/images/0de1765881e5836f370114bd4fd0a257591d0bcef797036dfded44534ac3a134.jpg)  
Fig. 2. A-BiRNN Architecture.

We obtain the state of the two gates of the GRU cells through the output of the last node $h _ { t - 1 }$ and the input of the current nodee . The reset gate is represented by $r ,$ and the update gate is represented by z. σ is a sigmoid function; $\widetilde { h _ { t } }$ records the status of the current time, and $h _ { t }$ is the output of the current node:

$$
z _ {t} = \sigma (W _ {e z} \cdot [ e _ {t}, h _ {t - 1} ])\tag{4}
$$

$$
r _ {t} = \sigma (W _ {e r} \cdot [ e _ {t}, h _ {t - 1} ])\tag{5}
$$

$$
\widetilde {h} _ {t} = \tanh (W \cdot [ r _ {t} ^ {*} h _ {t - 1}, e _ {t} ])\tag{6}
$$

$$
h _ {t} = (1 - z _ {t}) ^ {*} h _ {t - 1} + z _ {t} ^ {*} \widetilde {h} _ {t}\tag{7}
$$

The results include the outputs of the forward and backward se quences. The result of each word $h _ { i }$ is the concatenation of two outputs:

$$
h _ {i} = \left[ \overrightarrow {h _ {i}} \bigoplus \overleftarrow {h _ {i}} \right]\tag{8}
$$

## 4.2.3. Attention layer

The attention layer is proposed to capture the attention of the neural network on each token. The attention layer can focus on the most important parts of a sentence, which can improve a model’s perfor mance and interpretations via visualization [40].

Given the output of a paragraph through BiR $\mathsf { N N } H _ { P } = \{ h _ { 1 } , h _ { 2 } , h _ { 3 } . . . h _ { n } \}$ the weight α of each word i in the paragraph is calculated by the following equation. The representation R of the paragraph is formed by a weighted sum of these output vectors:

$$
\alpha_ {i} = \text { softmax } \left(W _ {A} * H _ {p} + b _ {A}\right)\tag{9}
$$

$$
R _ {P} = \alpha^ {T *} H _ {P}\tag{10}
$$

## 4.3. Feature fusion and ICO success prediction

With all features available, we propose a fusion module to capture features. Let $\varphi ( X _ { C } ) , \varphi ( X _ { K } )$ and $\varphi ( X _ { N } )$ represent the features of comments $X _ { C } ,$ heterogeneous knowledge $X _ { K } ,$ and numerical features $X _ { N } ,$ , respec tively. The merged featureX is formulated as $\operatorname { E q . }$ (11), where the symbol ⨁ indicates the concatenation:

$$
X = \varphi (X _ {C}) \bigoplus \varphi (X _ {K}) \bigoplus \varphi (X _ {N})\tag{11}
$$

Our goal is to learn the nonlinear mapping relation F(X) from the merged feature X to the Y by training a deep neural network. F(X) is defined as follows:

$$
F (X) = \operatorname{sigmoid} \left(W _ {f c} \cdot X + b _ {f c}\right)\tag{12}
$$

where $W _ { f c }$ and $b _ { f c }$ represent the weight and bias of the fully connected layer in the deep neural network. They are given random values in advance and must be learned during the training process, and sigmoid(⋅) is the activation function:

$$
L = - \left[ y l o g \widehat {y} w + (1 - y) l o g (1 - \widehat {y}) \right]\tag{13}
$$

To mitigate the data imbalance, we use the weighted cross entropy loss function and update the parameters via stochastic gradient descent (SGD), as shown in Eq. (13), where y is the true value, $\widehat { \boldsymbol { y } }$ is the predicted value and w is the weight of the positive sample.

## 5. Experiment setup

## 5.1. Data

We collect a total of 5717 proiect from ICObench. Because we aim to predict the success of ICO projects, we only include projects that have ended. Finally, we end up with 4286 projects for the experimental analysis. The success of an ICO project is determined by comparing the amount raised and the soft cap of the project. If the money raised by the project is less than the soft cap, then it fails. Conversely, if the money raised exceeds the soft cap, then it is considered successful. In this study, we regard those projects that raise more money than the hard cap as successful projects but do not group them into one category. The dataset contains 3119 failed projects and 1167 successful projects, accounting for approximately 72.8% and 27.2%, respectively. Finally, we took 80% of the data as the training set, 10% as the validation $s \mathrm { e t , }$ and the remaining 10% as the testing set.

## 5.2. Evaluation criteria

To evaluate the results of the proposed model, we chose four commonly used evaluation criteria: accuracy, precision, recall and F1 score. The definitions of the four measures include true positive (TP), true negative (TN), false positive (FP) and false negative (FN) charac terizations, which correspond to the values of the confusion matrix in Table 3:

$$
A c c u r a c y (\%) = \frac {T P + T N}{T P + F P + F N + T N} \times 100 \%\tag{14}
$$

$$
P r e c i s i o n(\%) = \frac{TP}{TP + FP}\times 100\%\tag{15}
$$

$$
\text{Recall} (\%) = \frac {T P}{T P + F N} \times 100 \%\tag{16}
$$

$$
F 1 (\%) = \frac {2 \cdot \text { Precision } \cdot \text { Recall }}{\text { Precision } + \text { Recall}} \times 100 \%\tag{17}
$$

## 6. Experiment results

## 6.1. Comparison to baselines

A-BiRNN and baseline models are evaluated in this section. In the first three models, due to the high dimensionality of text features, particularly TF-IDF, we designed a three-layer fully connected model for prediction, including an input layer, one hidden layer and one output layer.

All results are shown in Table 4. Compared to the baseline models, the A-BiRNN achieved the best performance for all metrics, particularly precision and accuracy. TF-IDF + FC performs the worst because its features are sparse and high-dimensional. In addition, compared with doc2vec, BERT achieves better performance in feature extraction. We also found that the attention mechanism is helpful in improving model precision.

Because the A-BiRNN uses an attentional mechanism, it can auto matically learn the weights of different words in comments. To improve the interpretability of the model, we visualize the weights to reflect the focus of the network via text highlighting.

In Fig. 3, there is a visual representation of three real review data points. The first fragment shows that the proposed model has allocated more attention to “solid team” and “product with right label”. In the second comment, “team experience” and “global partnership” are highlighted. The words on which the model focuses indicate investors interests.

## 6.2. Feature ablation study

To demonstrate the influence of heterogeneous team knowledge and expert evaluation in the prediction of ICO project success, we test the performance of different feature combinations. We construct four feature sets, the first of which refers to the pure numerical features (FS1) $( \boldsymbol { \mathrm { e . } } \boldsymbol { \mathrm { g . } }$ , duration, price, and rating) involved in previous studies. The second feature set (FS2) considers the heterogeneous knowledge of the project team based on FS1, while the third feature set (FS3) adds the expert evaluation to FS1. The final feature set is the combination of all three features (FS4).

Table 3 Confusion matrix.

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Predicted Class</td></tr><tr><td>Success</td><td>Failure</td></tr><tr><td rowspan="2">Actual Class</td><td>Success</td><td>TP</td><td>FN</td></tr><tr><td>Failure</td><td>FP</td><td>TN</td></tr></table>

Table 4  
Prediction performance comparison of the proposed model and baselines.

<table><tr><td>Methods</td><td>Accuracy</td><td>Precision</td><td>Recall</td><td>F1 score</td></tr><tr><td>TF-IDF [41] + FC</td><td>0.6414</td><td>0.6989</td><td>0.5895</td><td>0.6395</td></tr><tr><td>Doc2vec [42] + FC</td><td>0.6305</td><td>0.6540</td><td>0.5614</td><td>0.6042</td></tr><tr><td>Word Embedding + FC</td><td>0.7117</td><td>0.7240</td><td>0.6505</td><td>0.6933</td></tr><tr><td>Word Embedding + BiRNN</td><td>0.7266</td><td>0.7372</td><td>0.7002</td><td>0.7182</td></tr><tr><td>Word Embedding + BiRNN + Attention (A-BiRNN)</td><td>0.7367</td><td>0.7610</td><td>0.7051</td><td>0.7320</td></tr></table>

Bold indicates performance of our proposed model.

The results of feature ablation are shown in Fig. 4. According to the experimental results, feature set FS4 leads to the best performance. In FS2, heterogeneous team knowledge improves accuracy by 1.1% and the F1 score by 0.7%. In addition, by adding text features extracted from expert evaluation (FS3), the accuracy and F1 score increase by 2.9% and 3.0%, respectively, compared to using the numeric features only (FS1). These experimental results confirm the necessity of combining text features extracted from expert evaluation, heterogeneous team knowl edge and numerical features in this task. The prediction performance based on FS3 is also shown to be better than that based on FS2, which indicates that the textual features of online expert evaluations contain more valuable information. This result may occur because investors can easily read expert evaluations but take more effort to obtain team knowledge information.

## 6.3. Comparison to previous work

We compare the proposed model with two previous studies on ICO by C. Fisch [5] and K. Chen [7] to show the effectiveness of the proposed features. To maintain comparability, we transform their research prob lems into the prediction of ICO success. Specifically, we extract the variables mentioned in their studies from the proposed dataset, predict ICO success using a gradient boosting decision tree (GBDT), and eval uate the models’ performances with the four evaluation criteria described in Section 5.2.

Table 5 provides an overview of the performance of all models. The features used in the proposed model are highly competitive, particularly in terms of precision and accuracy. Therefore, the proposed model achieves notable improvements in the prediction accuracy of ICO success.

## 6.4. Parameter tuning

To examine the robustness of A-BiRNN, we also conducted experi ments that vary certain key parameters. We change the dimension of word embedding in the A-BiRNN model in the set {32, 64. 128}. In addition, for the size of the attention layer in the A-BiRNN model, we set the range of the tuning parameters to be {32,64,128}. Another impor tant parameter is the weight of the positive sample, which ranges from {2.0, 2.5, 3.0, 3.5}. Finally, we select the size of the hidden layer of BiRNN from the set {32, 64, 128}, and the results are shown in Fig. 5.

Model accuracy is shown to be relatively stable for different parameter settings. In addition, the precision and recall are sensitive to the weight. When the weight of the positive sample increases, the recall increases, but the precision decreases. According to these results, the best model performance occurs when the dimension of word embedding is set to 128, the hidden layer size to 32, the attention size to 32 and the weight equals 3.0.

Team : Theteamis solidwith experienced people involved . Icounted a21 person core team and 13 advisors . Linkedln profiles are updated and created a long time ago . Good Follower rates on Social Media . Vision : The vision is solid another example of how the blockchain can be used to cut out the more middle men and connect users directly to producers . Product : With theright Labelon board this can behuge . Prototyp and Visionis good

Great project with already an MVP and 70 thousands downloads makes it must watch project. Teams experience and global partnershipis somethingvery exciting. Looking forward for this project expanding into job and business referrals in future.

![](/api/attachments/TAXRGC7P/fulltext/images/d4e2bf3d08ee1eaf03f12d111bb374b9b7f57d8ac9999c12c39dd93dd15250c0.jpg)

Fig. 3. A-BiRNN result visualization.  
![](/api/attachments/TAXRGC7P/fulltext/images/fb092591f7f8378ace13f785a962208bd2eb8a372732f50c3027b53bebc0fc7f.jpg)

![](/api/attachments/TAXRGC7P/fulltext/images/6cd3b3aca8f563b5b4e9cc8a335bc7f185a6f262630dc02cad5729fab93d5976.jpg)

![](/api/attachments/TAXRGC7P/fulltext/images/1caa2a91d872d191865a80b79169f20655ae94e729d4f5938560937a6b72430b.jpg)  
Fig. 4. Prediction performance of various feature combinations.

Performance of the proposed model compared to previous studies.

<table><tr><td>Model</td><td>Precision</td><td>Recall</td><td>F1</td><td>Accuracy</td></tr><tr><td>K. Chen [7]</td><td>0.6841</td><td>0.6562</td><td>0.6699</td><td>0.6766</td></tr><tr><td>C. Fisch [5]</td><td>0.6594</td><td>0.6625</td><td>0.6609</td><td>0.6601</td></tr><tr><td>Proposed model</td><td>0.7610</td><td>0.7051</td><td>0.7320</td><td>0.7367</td></tr></table>

## 6.5. Discussions

In this study, we propose an ICO success prediction model that innovatively combines heterogeneous team knowledge, expert evalua tion information and other project-related features. The experimental results shown in Fig. 4 indicate that the features extracted from both team knowledge and expert evaluation can effectively improve predic tion performance. Based on KBT, we measure heterogeneous team knowledge by constructing team members’ knowledge from three di mensions: work experience, innovation ability and social connection. The experimental results demonstrate that a team with heterogeneou team knowledge can have a higher probability of ICO success. Moreover, because ICO is a new form of crowdfunding and a special financing method, the results also provide some evidence that a team with het erogeneous knowledge may achieve better financial performance than a team with less heterogeneous knowledge.

To extract textual features from expert evaluation, we propose a model called A-BiRNN that can automatically extract the most impor tant words in the prediction of ICO success. To improve model inter pretability, we also visualize the weights to show the focus of the model via text highlighting. In the comparative experiments, we also use tf-idf and doc2vec to extract textual features. The results in Table 4 show that the prediction accuracy of the proposed A-BiRNN is significantly higher than those of the other models.

## 7. Conclusions and direction for future work

This paper proposes a model to predict ICO success that combines heterogeneous team knowledge, expert evaluation information and other project-related features. Based on a real-world dataset crawled from ICObench, the accuracy of the proposed prediction model can reach 73.67%. Previous researchers have studied the impact of some project-related features on ICO performance. However, little research has focused on heterogeneous team knowledge and expert evaluations. Therefore, this study fills this gap in research with the following primary contributions. First, we innovatively consider team knowledge and expert evaluation in the prediction of ICO success. Empirical analysis identifies that both factors are highly effective in the prediction task. Second, based on KBT, we construct a measure for heterogeneous ICO team knowledge from three dimensions: work experience, innovation ability and social connection. Third, to extract textual features from expert evaluation, we propose an A-BiRNN model with an attention mechanism, which outperforms baselines.

![](/api/attachments/TAXRGC7P/fulltext/images/60a9570e56f5f4261f24c31d32dc0781406eb21eb620cc87cce16a5ad21a4fd7.jpg)

![](/api/attachments/TAXRGC7P/fulltext/images/1814712cebf15df8e43b64098bf9c9adb7f7192b4d731b91c75adf28ea44fc73.jpg)

![](/api/attachments/TAXRGC7P/fulltext/images/b49b734a658055eca3100222bd65521300ec34a2b613e549e50a496a882b6149.jpg)

![](/api/attachments/TAXRGC7P/fulltext/images/6147baa0cb38ffac33f86bdfa5dda3149458a7978b5bd1414b6e1ae4ab647304.jpg)  
Fig. 5. Prediction performance of various setting parameters.

Because ICO markets are still in the preliminary stage of develop ment with high information asymmetry, this study has important managerial implications. Potential investors can prejudge the success probability of ICO projects to protect themselves from investment fail ures. ICO platforms such as ICObench can use the proposed model to select more quality cryptocurrency projects to be shown on their plat forms. This study can also help cryptocurrency projects set a reasonable target amount before the ICO begins. Moreover, because ICO is a special financing tool, this study also provides critical insights: a team with heterogeneous knowledge may raise more money, which is valuable insight for startup companies to build an effective team.

There are some limitations to this study. First, to measure the entire team’s knowledge, we took a simple average across all individuals. However, because different roles in the project team may have different impacts on the project, people’s importance differs from person to per son. Therefore, potential investors may pay more attention to the knowledge of chief executive officers than to that of other partners. Second, for project-related features, we considered only fundamental numerical features in the prediction model. For example, the textual features in the project’s whitepaper and social networks were neglected. Therefore, in future studies, we will primarily focus on extracting more valuable features of ICO projects and then attempt to study their impact on ICO performance. Moreover, since blockchain and cryptocurrency projects are undergoing dynamic development and change, we will also pay more attention to the differences in ICO performance at different times.

## Acknowledgments

This work was supported by the National Natural Science Foundation of China (Grant No. 71771212) and Fundamental Research Funds for the Central Universities in UIBE (CXTD12-04).

## Appendix A. Supplementary data

Supplementary data to this article can be found online at https://doi. org/10.1016/j.dss.2021.113574.

## References

[1] X. Li, C.A. Wang, The technology and economic determinants of cryptocurrency exchange rates: the case of Bitcoin, Decis. Support. Syst. 95 (2017) 49–60.

[2] H.H.Y. Sun, K. Langenheldt, M. Harlev, R.R. Mukkamala, R. Vatrapu, Regulating cryptocurrencies: a supervised machine learning approach to de-anonymizing the bitcoin blockchain, J. Manag. Inf. Syst. 36 (1) (2019) 37–73.

[3] L.W. Cong, Z. He, Blockchain disruption and smart contracts, Rev. Financ. Stud. 32 (5) (2019) 1754–1797.

[4] G. Fridgen, F. Regner, A. Schweizer, N. Urbach, Don't slip on the initial coin offering (ICO): A taxonomy for a blockchain-enabled form of crowdfunding, in: Proceedings of the 26th European Conference on Information Systems, 2018,

[5] C. Fisch. Initial coin offerings (ICOs) to finance new ventures, J. Bus. Ventur, 34 (1 (2019) 1–22.

[6] L. Arnold, M. Brennecke, P. Camus, G. Fridgen, T. Guggenberger, S. Radszuwill, A. Rieger, A. Schweizer, N. Urbach, Blockchain and initial coin offerings: blockchain’s implications for crowdfunding, Bus. Transf. Blockchain (2019) 233–272.

[7] K. Chen, Information asymmetry in initial coin offerings (ICOs): investigating the effects of multiple channel signals, Electron. Commer. Res. Appl. 36 (2019) 100858.

[8] S. Adhami, G. Giudici, S. Martinazzi, Why do businesses go crypto? An empirical analysis of initial coin offerings, J. Econ. Bus. 100 (2018) 64–75.

[9] E. Penrose, E.T. Penrose, The Theory of the Growth of the Firm, Oxford University

[10] N. Hu, N.S. Koh, S.K. Reddy, Ratings lead you to the product, reviews help you clinch it? The mediating role of online review sentiments on product sales. Decision Supp. Syst. 57 (2014) 42–53.

[11] S. Banerjee, S. Bhattacharyya, I. Bose, Whose online reviews to trust? Understanding reviewer trustworthiness and its impact on business, Decis. Support. Syst. 96 (2017) 17–26.

[12] G. Fenu, L. Marchesi, M. Marchesi, R. Tonelli, The ICO phenomenon and its relationships with ethereum smart contract environment, in: Proceedings of the International Workshop on Blockchain Oriented Software Engineering (IWBOSE) 2018, pp. 23–28.

[13] P. Zhou, W. Shi, J. Tian, Z. Qi, B. Li, H. Hao, B. Xu, Attention-based bidirectional long short-term memory networks for relation classification, in: Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics, 2016, pp. 207–212.

[14] R.M. Grant, Toward a knowledge-based theory of the firm, Strateg. Manag. J. 17 (S2) (1996) 109–122

[15] J. Barney, Firm resources and sustained competitive advantage, J. Manag. 17 (1) (1991) 99–120.

[16] S. Carayannopoulos, E.R. Auster, External knowledge sourcing in biotechnology through acquisition versus alliance: a KBV approach, Res. Policy 39 (2) (2010) 254–267.

[17] M. Alavi, D.E. Leidner, Knowledge management and knowledge management systems: conceptual foundations and research issues, MIS O. (2001) 107–136.

[18] J.F. Ye, B. Hao. P.C. Patel, Orchestrating heterogeneous knowledge: the effects of internal and external knowledge heterogeneity on innovation performance, IEEE Trans. Eng. Manag. 63 (2) (2016) 165–176.

[19] T. Caner, S.K. Cohen, F. Pil, Firm heterogeneity in complex problem solving: a knowledge-based look at invention, Strateg. Manag. J. 38 (9) (2017) 1791–1811.

[20] G.D. Bhatt, Management strategies for individual knowledge and organizationa knowledge, J. Knowl. Manag. 6 (1) (2002) 31–39.

[21] T. Felin, W.S. Hesterly, The knowledge-based view, nested heterogeneity, and new value creation: philosophical considerations on the locus of knowledge, Acad. Manag. Rev. 32 (1) (2007) 195–218.

[22] G. Guzman, What is practical knowledge? J. Knowl. Manag. 13 (4) (2009) 86–98.

[23] A. Papa, L. Dezi, G.L. Gregori, J. Mueller, N. Miglietta, Improving innovation performance through knowledge acquisition: the moderating role of employee retention and human resource management practices, J. Knowl. Manag. (2018), https://doiorg/10.1108/JKM-09-2017-0391.

[24] M. Subramaniam, M.A. Youndt, The influence of intellectual capital on the types of innovative capabilities, Acad. Manag. J. 48 (3) (2005) 450–463.

[25] B. Lawson, D. Samson, Developing innovation capability in organisations: a dynamic capabilities approach, Int. J. Innov. Manag. 5 (03) (2001) 377–400.

[26] J. Darroch, Knowledge management, innovation and firm performance, J. Knowl. Manag. 9 (3) (2005) 101–115.

[27] Z. Wang, N. Wang, Knowledge sharing, innovation and firm performance, Expert Syst. Appl. 39 (10) (2012) 8899–8908.

[28] J. Rhodes, R. Hung, P. Lok, B.Y.H. Lien, C.M. Wu, Factors influencing organizational knowledge transfer: implication for corporate performance. J. Knowl, Manag, 12 (2008) 84.

[29] L. Rhee. P.M. Leonardi, Which pathway to good ideas? An attention-based view of innovation in social networks. Strateg, Manag. J. 39 (4) (2018) 1188–1215.

[30] J.C. Spender, Making knowledge the basis of a dynamic theory of the firm, Strateg. Manag. J. 17 (S2) (1996) 45–62.

[31] D. Godes, D. Mayzlin, Using online conversations to study word-of-mouth communication, Mark, Sci. 23 (4) (2004) 545–560.

[32] S.M. Mudambi. D. Schuff, What Makes a Helpful Online Review? A study of customer reviews on Amazon.com, MIS Ouarterly, 2010, pp. 185–200

[33] N. Archak, A. Ghose, P.G. Ipeirotis, Deriving the pricing power of product features by mining consumer reviews, Manag. Sci. 57 (8) (2011) 1485–1509.

[34] X. Li, C. Wu, F. Mai, The effect of online reviews on product sales: a joint sentiment-topic analysis, Inf. Manag. 56 (2) (2019) 172–184

[35] S. Dey, K. Karahalios, W.T. Fu, Understanding the effects of endorsements in scientific crowdfunding, in: Proceedings of the 2017 CHI Conference on Human Factors in Computing Systems, 2017, pp. 2376–2381.

[36] C. Courtney, S. Dutta, Y. Li, Practice, resolving information asymmetry: signaling, endorsement, and crowdfunding success, Entrepreneurship Theory 41 (2) (2017) 265–290.

[37] S.G. Scott, R.A. Bruce, Determinants of innovative behavior: a path model of individual innovation in the workplace, Acad. Manag. J. 37 (3) (1994) 580–607.

[38] C. Vorakulpipat, Y. Rezgui, An evolutionary and interpretive perspective to knowledge management, J. Knowl. Manag. 12 (3) (2008) 17–34.

[39] J. Devlin, M.-W. Chang, K. Lee, K. Toutanova, BERT: Pre-training of deep bidirectional transformers for language understanding, arXiv (2018), 1810.04805 [cs.CL].

[40] C.K. Theil, S. Broscheit, H. Stuckenschmidt, PRoFET: Predicting the risk of firms from event transcripts. in: Proceedings of the 28th International Joint Conference on Artificial Intelligence, 2019, pp. 5211–5217.

[41] W. Zhang, T. Yoshida, X. Tang, A comparative study of TF\* IDF, LSI and multi words for text classification, Expert Syst. Appl. 38 (3) (2011) 2758–2765.

[42] J.H. Lau, T. Baldwin, An empirical evaluation of doc2vec with practical insights into document embedding generation, in: Proceedings of the 1st Workshop on Representation Learning for NLP, 2016, pp. 78–86.

Wei Xu is a professor at School of Information, Renmin University of China. He is a research fellow at Department of Information Systems. City University of Hong Kong, He got his bachelor and master degree in Mathematics at Xi'an Jiaotong University and doctor degree in Management Science at Chinese Academy of Sciences. His research interests include big data analytics, business intelligence and decision support systems. He has published over 90 research papers in international journals and conferences, such as Annals of Operations Research, Decision Support Systems, Electronic Commerce Research. European Journal of Operational Research, IEEE Trans. Systems, Man and Cybernetics,

International Journal of Production Economics, and Production and Operations Management.

Ting Wang is a master student at School of Information, Renmin University of China. He interests include big data analytics, business intelligence and decision support systems.

Runyu Chen is an assistant professor at School of Information Technology and Manage ment, University of International Business and Economics. He got his doctor degree in computer application technology at Renmin University of China, and B.E. degree from Beijing University of Posts and Telecommunications. His research interests include dat mining, business analysis, and financial technology. He has published several papers in international journals and conferences, such as Decision Support Systems, Electronic Commerce Research, Electronic Commerce Research and Applications, and Information Processing and Management.

J. Leon Zhao is Professor and Director, Center on Blockchain and Intelligent Technology, School of Management and Economics, Chinese University of Hong Kong, Shenzhen, China. Previously, he was Chair Professor (2009-2020) and Head (2009-2015) at the Department of Information Systems, City University of Hong Kong. He served as Interim Head and Eller Professor of MIS with the University of Arizona. He also taught at the Hong Kong University of Science and Technology, and the College of William and Mary. His current research interests include blockchain, FinTech, business intelligence, and other topics in information technology and management. He has published over 300 journal and conference articles including many in top-tier journals such as Management Science, MIS Quarterly, Information Systems Research, INFORMS Journal on Computing, Journal of MIS, and IEEE and ACM Transactions. He holds Ph.D. degree from Haas School of Business, University of California at Berkeley, Master degree from University of California at Davis， and B.S. degree from Beijing Institute of Agricultural Mechanization.
