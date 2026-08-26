---
otero_id: 11786
otero_key: "4A7GXVNG"
title: "Emphasizing the entrepreneur or the idea? The impact of text content emphasis on investment decisions in crowdfunding"
authors: "Wei Wang; Wei Chen; Kevin Zhu; Hongwei Wang"
year: "2020"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2020.113341"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Journal Pre-proof

Emphasizing the entrepreneur or the idea? The impact of text content emphasis on investment decisions in crowdfunding

Wei Wang, Wei Chen, Kevin Zhu, Hongwei Wang

Decision Support Systems

![](/api/attachments/4A7GXVNG/fulltext/images/6acce808e2bd8bd1329563f68cc4660a9d69b0de612e4af8bc8ab2e21b0fa595.jpg)

PII: S0167-9236(20)30096-8

DOI: https://doi.org/10.1016/j.dss.2020.113341

Reference: DECSUP 113341

To appear in: Decision Support Systems

Received date: 7 September 2019

Revised date: 4 June 2020

Accepted date: 8 June 2020

Please cite this article as: W. Wang, W. Chen, K. Zhu, et al., Emphasizing the entrepreneur or the idea? The impact of text content emphasis on investment decisions in crowdfunding, Decision Support Systems (2020), https://doi.org/10.1016/j.dss.2020.113341

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

© 2020 Published by Elsevier.

# Emphasizing the Entrepreneur or the Idea? The Impact of Text Content Emphasis on Investment Decisions in Crowdfunding

Wei Wang<sup>a</sup> wwang@hqu.edu.cn, Wei Chen<sup>b</sup> weichen@email.arizona.edu, Kevin Zhu<sup>c</sup> kxzhu@ucsd.edu,

Hongwei Wang<sup>d,\*</sup> hwwang@tongji.edu.cn

<sup>a</sup>College of Business Administration, Huaqiao University, Quanzhou, 362021, China

<sup>b</sup>Eller College of Management, University of Arizona, Tucson, USA

<sup>c</sup>Rady School of Management, University of California, San Diego, USA

<sup>d</sup>School of Economics and Management, Tongji University, Shanghai 200092, China Corresponding author.

## Abstract

The criteria for evaluating a crowdfunding project vary from person to person. Some investors are concerned with the entrepreneurs’ profiles, while others are more interested in the creativity behind the project. Most investors evaluate a project by referring to founder-generated content. Entrepreneurs face project creativity within the limited narrative. Our study is thus motivated mine emphasis of the text narratives affect the fundraising outcomes. We propose an prove p lear ng model for text content emphasis (TCE) detection from various textual sources, including titles, blurbs, and detailed descriptions, and then estimate the impact of TCE on the fundraising success of Kickstarter campaigns. Our empirical analyses demonstrate that TCE matters differently for various textual sources. The title and blurb should emphasize the entrepreneur profile, while the detailed description should highlight the idea creativity. Furthermore , for the detailed description, the entrepreneur profile has a more positive effect when it is placed at the beginning of the narrative. And the effects of entrepreneur-oriented narratives are more pronounced in these projects with more social connections. This study contributes to the understanding of TCE, entrepreneur profile disclosure, and social connection in economic exchanges in online crowdfunding.

Keywords: crowdfunding; investment willingness; text content emphasis; text analytics

## 1. Introduction

Crowdfunding campaigns catch investors’ attention in one of two ways: (1) by advertising the creativity behind the project, or (2) by highlighting the fundraiser’s qualifications, such as education background, skills, awards, credit, reputation, and so on. In some situations, where the text length is limited (such as in project titles and blurbs), entrepreneurs cannot highlight one aspect without relinquishing the other. Therefore, entrepreneurs face a trade-off between two types of strategies for text content emphasis (TCE): highlighting either the entrepreneur profile or the idea creativity. Even in the both aspects, they still need to weigh the priority of the two types of TCE.

Creativity is one of the determinants in attracting investors to support startups [1]. Despite the lack of a universal definition of creativity, there is a consensus that a creative solution is characterized as being new and useful [2]. But there are far fewer discussions on the entrepreneur profile. In this paper, we study the impact of TCE, emphasizing either the entrepreneur profile or the idea creativity, on investment decisions in crowdfunding. Specifically, we propose the llowing two research questions as shown in Figure 1: (1) how TCE affects fundraising results when entrepreneurs highlight either the entrepreneur profile or the idea creativity, and (2) which aspect of TCE should be placed at the beginning of the narrative if entrepreneurs describe both aspects. Question 1 tries to estimate the influence of TCE when only one aspect is highlighted. While Question 2 attempts to explore how to choose a reasonable strategy when the entrepreneur intends to emphasize both aspects.

![](/api/attachments/4A7GXVNG/fulltext/images/3fa90ea933c6e8f2824f09c862d54f39d670002d68c4b261a674de4f0e2b7e2a.jpg)  
Figure 1. Research question definition

To address the questions above, we define TCE as how much the text emphasizes one specific aspect (either the entrepreneur profile or the idea creativity), while the other aspect is downplayed. TCE is not a binary classification. Instead, it is similar to a probability estimation, which estimates the degree of emphasis on one aspect or the other. One side is likely to be weakened if the emphasis is on the other side [3]. Consider the following examples from two real cases:

(1) We are the iGem team! Last year, we successfully tested a plasmid that identifies fluoride bioswitches. We won an award at iGem, the largest synthetic biology competition.

(2) This project proposes an experimental and multi-physics simulation of a novel Acoustic Emission delayed monitoring and use many actuators, AE monitoring gives the real-time damage information without any actuator.

The first narrative focuses on the promotion of the entrepreneur profile, while the second narrative concentrates on the idea creativity. If the TCE strategy is not appropriate in the project narrative, its attractiveness will decrease. Sometimes both e entrepreneur profile and the idea creativity can be introduced simultaneously. In such cases, however, the presentation order will matter to readers perception of the project, thus swayin willingness of investment. Therefore, in addition to highlighting certain aspects, entrepreneurs need to determine the TCE prioritization.

Using real data from Kickstarter campaigns, we aim to explore the impact of TCE on successful fundraising pitches to enrich our understanding of how narrative factors influence online financing. Practically, this study can improve our understanding of TCE's value and guide entrepreneurs to create more engaging crowdfunding narratives.

## 2. Literature Review and Hypotheses Development

## 2.1 Literature Review

In the areas of titles or blurbs where the text is subject to length limits, entrepreneurs can hardly detail both aspects. However, strengthening one aspect will inevitably result in weakening the other [4]. Hence, entrepreneurs face challenges similar to those from more than 50 years ago: they must persuade readers to take the expected actions [5]. Hovland’s persuasion model suggests that the content of a message is an antecedent of the audiences’ attitudes [6].

On the one hand, crowdfunding allows a large group of people to pool their money to help fund an idea. In 2009, Kickstarter launched as an innovative way to support creativity and brought a new term “crowdfunding” to the forefront. A crowdfunding campaign introduces an idea to help creative minds get funded by their peers. Therefore, in the evaluation of a campaign, the idea creativity often plays a major role [7].

On the other hand, information from credible and reliable sources is much more persuasive [8]. This is why the public is more likely to trust an expert than an amateur [9]. Regarding startups, even if they have good ideas, business success is not yet assured without a $\mathrm { \ s t { n } \mathrm { \Sigma . . } \mathrm { \Sigma } _ { \mathrm { { \ s } } } }$ team. From such a perspective, the entrepreneur profile is vital in investment decisions in crowdfunding [10].

However, existing studies lack a careful investigation regarding the effects of highlighting the studies have distinguished the impacts of TCE from different text areas. We conduct a careful literature

Table 1. Summary of the research related to our study

<table><tr><td colspan="7">1. Factors analysis related to entrepreneur aspect or idea aspect</td></tr><tr><td>Title [citation]</td><td>Meris</td><td>Comments</td><td>Entrepreneur aspect</td><td>Idea aspect</td><td>Text mining</td><td>Online funding</td></tr><tr><td>The Dynamics of Crowdfunding: An Exploratory Study [11]</td><td>Successful campaigns are positively correlated with the number of followers.</td><td>● The importance of the entrepreneur aspect is shown but lack of comparison with the ideas.</td><td>√</td><td></td><td></td><td>√</td></tr><tr><td>Assessing the Impact of Public Venture Capital Programmes in the United Kingdom: Do Regional Characteristics Matter? [1]</td><td>The factor, regional characteristics, is the key to evaluate whether to invest in venture capital firms.</td><td>● Regional characteristics are related to creativity, but they are not the same.● The characteristics of crowdfunding campaigns are not considered.</td><td></td><td>√</td><td></td><td>√</td></tr><tr><td>Small business online loan crowdfunding: who gets funded and what determines the rate of interest? [12]</td><td>Crowdfunding projects are affected by social relationships and entrepreneurs' credit.</td><td>● Social relationships are different from the entrepreneur aspect.● The entrepreneur aspect is not compared with the idea aspect.</td><td>√</td><td></td><td></td><td>√</td></tr><tr><td>Funders' positive affective reactions to entrepreneurs' crowdfunding pitches: The influence of perceived product creativity and entrepreneurial passion[13]</td><td>Product creativity perception shows a positive correlation with crowdfunding performance.</td><td>● The perceived entrepreneurial passion is attributed to the entrepreneur aspect.● The entrepreneur aspect is not compared with the idea aspect.</td><td>√</td><td></td><td></td><td>√</td></tr><tr><td>The role of entrepreneurial creativity in entrepreneurial processes, International Journalof Innovation[10]</td><td>The entrepreneur aspect plays an important role in attracting investors.</td><td>● It demonstrates the value of the entrepreneur aspect.● The entrepreneur aspect is not comparedwith the idea aspect.</td><td>√</td><td></td><td></td><td>√</td></tr><tr><td>Start-up Absorptive Capacity: Does the Owner's Human and Social Capital Matter? [14]</td><td>The entrepreneur aspect is more important than the idea aspect.</td><td>● The crowdfunding context is not considered.</td><td>√</td><td>√</td><td></td><td></td></tr><tr><td>Gender and Venture Capital Decision-making: The Effects of Technical Background and Social Capital on Entrepreneurial Evaluations[15]</td><td>The most significant influence on company valuation is the gender of the entrepreneur, followed by the type of business.</td><td>● The crowdfunding context is not considered.</td><td>√</td><td>√</td><td></td><td>√</td></tr><tr><td>Why We Plan: The Impact of Nascent Entrepreneurs' Cognitive Characteristics and Human Capital on Business Planning[16]</td><td>Highly educated entrepreneurs tend to have more pragmatic and formal business plans than less-educated counterparts.</td><td>● It highlights the importance of the entrepreneur aspect. ● The crowdfunding context is not considered.</td><td>√</td><td></td><td></td><td>√</td></tr><tr><td>Success in the management of crowdfunding projects in the creative industries[17]</td><td>Human resource is the key predictor of crowdfunding success.</td><td>● The authors imply the entrepreneur aspect is important. ● The entrepreneur aspect is not compared with the idea aspect.</td><td>√</td><td></td><td></td><td>√</td></tr><tr><td colspan="7">2. Research on the influencing factors of online investment intention</td></tr><tr><td>A principal-agent perspective on consumer co-production: Crowdfunding and the redefinition of consumer power [18]</td><td>Projects that do not meet the pledge goals due to the market's disapproval of their potentials.</td><td>● It shows the value of a funding goal to a funding outcome. ● The entrepreneur aspect is not compared with the idea aspect.</td><td>√</td><td></td><td></td><td>√</td></tr><tr><td>Having a creative day: Understanding entrepreneurs' daily idea generation through a recovery lens[19]</td><td>Ideas are important for a successful business.</td><td>● It emphasizes the importance of ideas, but the impact of ideas is not compared with the idea of entrepreneurs.</td><td></td><td>√</td><td></td><td>√</td></tr><tr><td>Crowdfunding revisited: a neo-institutional field-perspective[20]</td><td>Investment decisions are more influenced by a firm's value proposition than purely financial factors.</td><td>● It demonstrates the influence of the idea aspect. ● The idea aspect is not compared with the entrepreneur aspect.</td><td></td><td>√</td><td></td><td>√</td></tr><tr><td>Comparison of human versus technological support to reduce domestic electricity consumption in France [21]</td><td>It shows the importance of the entrepreneur aspect and the reduction of power consumption.</td><td>● It compares the differences between the entrepreneur aspect and the idea aspect, but the research field is not in crowdfunding.</td><td>√</td><td>√</td><td></td><td></td></tr><tr><td>Detecting fraudulent behavior on crowdfunding platforms: The role of linguistic and content-based cues in static and dynamic contexts[22]</td><td>Content-based clues in crowdfunding terms descriptions are valuable for fraud detection.</td><td>● It demonstrates the importance of textual description for crowdfunding projects. ● The idea aspect is not compared with the entrepreneur aspect.</td><td></td><td></td><td>√</td><td>√</td></tr><tr><td>Strategic learning for digital market pioneering: Examining the transformation of Wishberry's crowdfunding model [23]</td><td>Business plan are critical to the success of crowdfunding projects.</td><td>● It emphasizes the idea aspect of the crowdfunding project. ● It does not address the role of the entrepreneur aspect.</td><td></td><td>√</td><td></td><td>√</td></tr><tr><td>Why funders invest in crowdfunding projects: Role of trust from the dual-process perspective[24]</td><td>Project types and funding levels moderate the relationships between key antecedents and investment decisions.</td><td>● It demonstrates the power of project attributes. ● The idea aspect is not compared with the entrepreneur aspect.</td><td></td><td></td><td></td><td>√</td></tr><tr><td>Examining how the personality, self-efficacy, and anticipatory cognitions of potential entrepreneurs shape their entrepreneurial intentions[25]</td><td>Learning and creative forms of self-efficacy shape the entrepreneurial self-efficacy.</td><td>● The entrepreneur aspect is important. ● The entrepreneur aspect is not compared with the idea aspect. ● There is no discussion on crowdfunding.</td><td>√</td><td></td><td></td><td></td></tr><tr><td colspan="7">3. Text emphasis extraction</td></tr><tr><td>Leveraging deep learning with LDA-based text analytics to detect automobile insurance fraud [26]</td><td>The text description has power in predicting project financing results.</td><td>● It does not compare the idea aspect with the entrepreneur aspect.</td><td></td><td></td><td>√</td><td>√</td></tr><tr><td>The determinants of crowdfunding success: A</td><td>The topics extracted from the crowdfunding description will</td><td>● LDA is an unsupervised algorithm, while the TCE analysis is a supervised</td><td></td><td></td><td>√</td><td>√</td></tr><tr><td>semantic text analytics approach [27]</td><td>affect the fundraising results.</td><td>algorithm.</td><td></td><td></td><td></td><td></td></tr><tr><td>Exploring the multi-sided nature of crowdfunding campaign success [28]</td><td>Longer descriptions positively influence the achievement of campaign goals.</td><td>It demonstrates the power of the text description.The entrepreneur aspect is not compared with the idea aspect.</td><td></td><td></td><td>√</td><td>√</td></tr><tr><td>Being seen to care: the relationship between self-presentation and contributions to online pro-social crowdfunding campaigns [29]</td><td>Self-presenting founders will increase levels of visible activity, but will not vary levels of non-visible activity.</td><td>It shows the role of personal information presentation.It does not compare the idea aspect with the entrepreneur aspect.</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>Understanding the crowdfunding phenomenon and its implications for sustainability [30]</td><td>Both the entrepreneur aspect and the idea aspect are important.</td><td>The idea aspect is not compared with the entrepreneur aspect.</td><td>√</td><td>√</td><td></td><td>√</td></tr><tr><td>My words for your pizza: An analysis of persuasive narratives in online crowdfunding [31]</td><td>Demonstrate the role of text description.</td><td>The entrepreneur aspect is not compared with the idea aspect.</td><td></td><td></td><td>√</td><td>√</td></tr><tr><td>Project description and crowdfunding success: an exploratory study [32]</td><td>Three exemplary antecedents (length, readability, and tone) influence fundraising outcomes.</td><td>It demonstrates the power of the text description.The idea aspect is not compared with the entrepreneur aspect.</td><td></td><td></td><td>√</td><td>√</td></tr><tr><td>The relationship between soft information in loan titles and online peer-to-peer lending: evidence from RenRenDai platform[33]</td><td>A textual description with a clear purpose is conducive to improving the financing success ratio of P2P projects.</td><td>The idea aspect is not compared with the entrepreneur aspect.</td><td></td><td></td><td>√</td><td>√</td></tr><tr><td>How entrepreneurs seduce business angels: An impression management approach[34]</td><td>The investor's investment intention is influenced by the idea.</td><td>The idea aspect is not compared with the entrepreneur aspect.</td><td></td><td></td><td>√</td><td>√</td></tr><tr><td>Determinants of success of restaurant crowdfunding[35]</td><td>A comprehensive description of the idea will increase the probability of successful funding.</td><td>It focusses on restaurant crowdfunding.The idea aspect is not compared with the entrepreneur aspect.</td><td></td><td></td><td>√</td><td>√</td></tr><tr><td>Are the life and death of an early-stage venture indeed in the power of the tongue? Lessons from online crowdfunding pitches[36]</td><td>Projects that frequently mentioned entrepreneurs' names experienced higher rates of success.</td><td>It demonstrates the value of the entrepreneur aspect.The idea aspect is not compared with the entrepreneur aspect.</td><td>√</td><td></td><td>√</td><td>√</td></tr><tr><td>Start-up inertia versus flexibility: The role of founder identity in a nascent industry [37]</td><td>The entrepreneur aspect is the most important factor followed by the idea aspect.</td><td>The research field is the nascent air taxi market, not online crowdfunding.</td><td>√</td><td>√</td><td></td><td></td></tr></table>

Table 1 reveals the research gaps as follows: (1) Few studies are concerned about entrepreneur-oriented and idea-oriented strategies, especially for crowdfunding pitches (e.g., [14, 15, 21, 37]). Related works of narrative styles only considered the impact of name frequency (e.g.,[36]), but did not distinguish TCE and the differences among text areas. Emerging deep learning provides a technical tool to analyze TCE in narratives (e.g., [26, 28, 31] ). (2) Regarding the context, crowdfunding has not been mentioned among the existing studies of the two aspects of startups (e.g., [14, 15, 19, 20]). That is, few efforts are devoted to examining the different effects of entrepreneur-oriented and idea-oriented strategies on investors’ willingness to fund an entrepreneurial project. (3) We do not yet understand how the prioritization of TCE affects fundraising success. In a long text, entrepreneurs still wonder how to introduce the idea creativity and their profiles in the right sequence.

## 2.2 Hypotheses Development

On crowdfunding platforms, textual information can appear in several types of separated sections (also known as text levels), such as the title, blurb, and detailed description. As different sections differ in their persuasion effects, entrepreneurs need to select the right sections to describe a campaign [38, 39]. In a situation where the text is subject to length limitation, entrepreneurs should balance TCE's focus. While in a situation without text length limitations, entrepreneurs need to consider TCE prioritization.

In the first situation, such as in the title a nd blurb of crowdfunding projects , the text length is limite d. The entrepreneur can only describe the most important aspect of the project. The venture capital literature has long shown that the team experience may serve as a signal of the unobserved quality of a venture, and may affect a startup’s ability to attract funding [40]. Therefore, emphasizing the entrepreneur profile in limited text spaces might help attract the attention of potential backers and increase the funding amount. Studies have also pointed out that the entrepreneurial market never lacks good ideas, but is short of capable entrepreneurs to turn good ideas into reality [41]. Thus, the team factor is often the main reason why some good ideas are poorly executed. From this perspective, the entrepreneur aspect is vital in crowdfunding pitches. Thus, some studies indicate that highlighting the entrepreneur aspect is more beneficial in short texts [14, 29].

The title and blurb of a crowdfunding project are crucial for investors to comprehend a project [33]. Their role is similar to the title and abstract of academic publications. In the literature, they are shown to be more important than other sections because they enable readers to ascertain the key research findings quickly [42]. In the crowdfunding context, blurbs are short promotional pieces that mimic the function of abstracts and aim to attract investors' attention quickly. Given the importance of titles and blurbs, entrepreneurs must highlight the most attractive aspect in such short texts. Because the entrepreneur aspect is the key factor determining whether the project idea can be effectively implemented [41], it needs to be highlighted in the title and blurb. Furthermore, the idea creativity, as a complex and abstract concept, is diffic ult to clearly describe in short texts. Therefore , the description of creativity is often expressed in the form of images, rather than in the form of short texts [43]. Compared to creativity, the entrepreneur aspect of the campaigns is more likely to be described in a short text, such as identity, education, awards, etc. Thus, we propose the following hypothesis to test the importance of different aspects of TCE in titles and blurbs:

Hypothesis 1: Entrepreneur-oriented narratives are more attractive for investment than those that are idea-oriented in titles and blurbs.

In the second situation ( i.e., in a deta ile d description) where the text length is not limite d, entrepreneurs could elaborate on multiple aspects. Creativity is regarded as the key to value propositions for venture projects, so a venture investment decision is made based more on the idea aspect [20]. A survey of 50 venture companies finds tha t the core business of startups does not change over the long variety of reasons to fund a campaign, among which, supporting an innovative idea is dominant [1].

Additionally, reward-based crowdfunding is regarded as a creativity support tool, so the focus should be idea-oriented rather than entrepreneur-oriented in the detailed description [44]. Furthermore, in the length of the text, it is more like ly to communicate the creativity of the project estors, which is ore effective than in short texts. Therefore, it is reasonable to believe that idea-oriented narratives are more attractive than entrepreneur-oriented narratives. Thus, we speculate that crowdfunding campaigns that emphasize their idea creativity in the detailed description may attract more investment. This speculation leads to the following hypothesis:

Hypothesis 2: Idea-oriented narratives are more attractive for investment than those that are entrepreneur-oriented in the detailed description.

As the entrepreneur can incorporate both aspects in the detailed description, they need to determine the prioritization of TCE [49]. TCE prioritization determines the reading sequence and thus affects the reader’s cognitive process. A study of video presentation sequences shows that users will develop their judgment based on the video first presented, and such judgment is hardly changed by subsequent videos [50]. Therefore, merchants tend to present the most attractive features at the beginning during product displaying [51]. TCE prioritization may yield different fundraising outcomes. As an idea-oriented business model, entrepreneurial projects in crowdfunding aim to respond to market opportunities. Since crowdfunding projects attempt to turn a creative idea into a real product, investors may pay more attention to its idea creativity [1]. Thus, it seems reasonable to present the idea at the beginning of the detailed description. Therefore, we propose the following hypothesis:

Hypothesis 3: In the detailed description, introducing the idea aspect at the beginning is more attractive for investment than presenting it at the end of narratives .

We next examine the role of social connection and its moderating role in the impact of TCE on fundraising outcomes. The social network maintains, bonds, and bridges personal power through connections [53]. Studies have shown that social connections have a great positive effect on fundraising outcomes [54]. Social connections are the effective functioning of social groups through interpersonal relationships, a shared sense of identity, a shared understanding, shared norms, shared values, trust, to support the campaign, thus positively affecting users’ willingness to invest [56]. The bonds formed by nd highlight the project's attractiveness from the entrepreneur rather than the idea aspect. It suggests that social connections play an important role in enhancing the personal influence, which can be manifested through the entrepreneur aspect in the TCE. Therefore, we propose the following hypothesis:

Hypothesis 4: The positive effect of entrepreneur-oriented TCE on fundraising outcomes is more pronounced in these projects with more social connections.

In most cases, the funding goals moderate the influence of various factors on investment decisions. This is mainly because individuals adjust their behaviors, either consciously or subconsciously, by referencing intended goals in the decision process [59]. Goal setting is a challenge faced by each entrepreneur. Prior studies reveal the importance of considering how goal setting moderates the connection between management measures and enterprise performance [60, 61]. Because crowdfunding aims to meet the predetermined funding target, funding goals may play a moderating role in fundraising

outcomes in crowdfunding.

The pledged amount may reflect the quality of entrepreneurial projects. Namely, if the pledged amount reaches the funding goal, the entrepreneur receives a positive response to the commercial potential of the ir creative idea. In contrast, if a campaign fails to raise the fund, the entrepreneurs themselves will question the original idea, and even terminate the project [18]. When entrepreneurs set a higher funding goal, they will attempt to persuade investors to participate in their project through their profile rather than their idea [62], which may make entrepreneur-oriented TCE more effective in

## Hypothesis 5: The positive effect of entrepreneur-oriented TCE on fundraising outcomes is

Figure 2 depicts our research model. This study begins with the extraction of the TCE from different sections using an improved deep learning method. We then estimate the impact of the TCE in titles and blurbs (H1) and in detailed descriptions (H2) the pledged ratio, the number of backers, and the pledged amount of the crowdfunding campaign. Next, we formulate models to estimate the inf of TC prioritization in the detailed description on the funding outcomes (H3). , we examine oderating effects of social connections and funding goals of the crowdfunding campaign on the impact of TCE (H4 and H5).

![](/api/attachments/4A7GXVNG/fulltext/images/19cf12ee6eb42af5d26746f40f00856eed31926caf7113dcd602e16d3794c2aa.jpg)  
Figure 2. Research model

## 3. Data and Methods

## 3.1 Research Data

Figure 3 illustrates the research framework, which includes four major steps: (1) collect raw data, (2) preprocess the corpus, (3) build the TCE detection model, and (4) estimate the impact of the TCE on the funding outcomes.

![](/api/attachments/4A7GXVNG/fulltext/images/9c7e9c56cffa7366eaf8897d54e95fce09cb482ca85b95212f4f8ef6d59133f3.jpg)  
Figure 3. Processing flow on the data

Kickstarter is one of the most famous reward-based crowdfunding platforms in the world. We collected the information of the crowdfunding campaigns during an observation period from April 21<sup>th</sup>, ${ 8 } ^ { \mathrm { t h } }$ success rate of 52.18% (reaching their funding goals). We use this data set to facilitate our following analyses.

## 3.2 Text Content Emphasis Detection

TCE detection aims at exploring which aspect a narrative is intended to emphasize. It is a type of supervised algorithm that estimates the extent to which the text highlights the entrepreneur aspect or the idea aspect. Usually, entrepreneurs introduce both aspects simultaneously when describing a campaign. Therefore, TCE is more similar to a continuous variable between zero and one, measuring how much a text is highlighted toward the idea or the entrepreneur. We develop a deep learning method to detect the TCE for the crowdfunding texts.

The machine learning model needs to be trained by well-labeled data. A total of 6347 sentences are labeled manually. We use a dummy variable to label the text, 0 for the idea aspect, and 1 for the entrepreneur aspect. Annotation results show that sentences with label “1” share several commonalities: (1) quoting personal, team, and company names, as well as other words, related to the entrepreneur aspect, and (2) using vocabulary with strong person-related content, such as education, reward, credit, skill, experience, qualification, role, and social network [67]. Terms that describe the idea aspect are often scattered. We find no unified vocabulary to identify the TCE on the idea aspect. Therefore, we detect the TCE of a text by estimating the extent to which the entrepreneur aspect is highlighted. The converse is the extent that the idea aspect is emphasized. For example, if a narrative emphasizes the entrepreneur

In natural language processing, neural networks (NNs) usually use a softmax function for text classification and output the classification results. Our improved algorithm, instead of binary classification, estimates the probability that each text document belongs to a particular category. We utilize the long short-term memory (LSTM) recurrent neural network for our deep learning method. LSTM makes structural improvements to the hidden layer of the recurrent neural network (RNN), where a forget gate is introduced to solve the long-term dependencies problem. Therefore, LSTM can retain the characteristics of the sequence select ively by retaining important information while forgetting unimportant information [64].

As one of the most popular penalty functions, the quadratic loss function applies to many cases. Many statistics are based on the quadratic loss function, including t-tests, regression models, and linear-quadratic optimal control problems [65]. Deep learning algorithms often use the quadratic loss function as a penalty function in the learning process (see, e.g., [66]). We also employ a quadratic loss function to estimate the performance of the TCE detection models, as shown in Equation (1), where Y is the real value and f (X) is the predictive value.

$$
\operatorname{Loss} = L (Y, f (X)) = (Y - f (X)) ^ {2}\tag{1}
$$

Cross-validation (CV) is commonly used in machine learning to compare models for a given predictive problem and select one because it outperforms other methods. Cross-validation aims to ensure that every example from the original dataset has the same chance of appearing in training or testing sets.

Given a set of m examples, the widely used K-fold cross-validation partitions them equally into K sets. Each of the K-1 sets is used for training the classifier, while the last one set is used for testing [68]. Most extant studies have employed 10-fold cross-validations [69]. We also employ 10-fold cross-validation to divide the data into ten sets randomly, to train the model on nine sets, and finally to test the model on the remaining set. The experiment is repeated ten times with different combinations. The average loss value for the ten experiments is adopted as the final result. We compare the results of several machine learning algorithms on TCE detection in Table 2, where TF is term frequency, IDF indicates inverse document frequency, and SVD is singular value decomposition [70]. From the comparison, LSTM achieves the best results. We then use the LSTM model to estimate the TCE of the titles, blurbs, and detailed descriptions of crowdfunding projects.

Table 2. Comparison of loss values of machine learning algorithms

<table><tr><td>Algorithm</td><td>Text processing</td><td>Loss value</td></tr><tr><td>Logistic regression</td><td>TF-IDF</td><td>0.258</td></tr><tr><td>Logistic regression</td><td>TF-IDF</td><td>0.276</td></tr><tr><td>Naive Bayes</td><td>TF-IDF</td><td>0.292</td></tr><tr><td>Naive Bayes</td><td>TF-IDF</td><td>0.648</td></tr><tr><td>SVM</td><td>TF-IDF + SVD</td><td>0.314</td></tr><tr><td>Xgboost</td><td>TF-IDF</td><td>0.266</td></tr><tr><td>Xgboost</td><td>TF</td><td>0.264</td></tr><tr><td>Xgboost</td><td>TF-IDF + SVD</td><td>0.278</td></tr><tr><td>Xgboost</td><td>TF-IDF + Scaled SVD</td><td>0.282</td></tr><tr><td>Grid Search Model</td><td>TF-IDF</td><td>0.284</td></tr><tr><td>Sequential Neural Net (3 layers)</td><td>TF-IDF + SVD</td><td>0.3088</td></tr><tr><td>LSTM (3 layers)</td><td>Word2vec</td><td>0.2252</td></tr></table>

## 3.3 Empirical Models

The purpose of crowdfunding narratives is to convince investors to provide funding to the project. After obtaining the TCE of the texts, we then estimate the effects of TCE from different sections on the funding outcomes. Based on Kickstarter’s characteristics, we formulate the following empirical model to evaluate the impacts of TCE comprehensively:

$$
Y _ {i} = \alpha + T C E _ {i} ^ {\prime} \cdot \beta + Z _ {i} ^ {\prime} \cdot \gamma + \varepsilon_ {i},\tag{2}
$$

where $Y _ { i }$ is the funding outcome variables. We use four variables to measure the funding outcomes: (1) the pledge status, which is a dummy variable that indicates whether the campaign is a success (with value 1) or failure (value 0); (2) the pledged ratio, which measures the ratio of the actually raised funds compared to the original funding goal; (3) the number of backers who contributed to the crowdfunding campaign; (4) the pledged amount. $T C E _ { i }$ is a vector of the estimated TCE from different sections of project i, which is generated from our LSTM model. $Z _ { i } ^ { \prime }$ is the control variable vector, which includes the number of updates from the project, the number of comments on the introduction video is presented (1=true, 0=otherwise), and the lengths of the title, blurb, and detailed description [71].

## 4. Results

## 4.1 Summary Statistics

Table 3 reports the descriptive statistics of the sample. In terms of funding outcomes, which means that an age achieve more than two times its funding goal. The resulting in a substantial standard deviation (161.618). Meanwhile, the median project achieves 100.1% of its funding goal, just past what was set at the beginning of the crowdfunding campaign. Note that because the number of backers and the pledged amount are large numbers, we log-transform them in our regressions to avoid the bias brought by extreme values.

The TCE-related variables reveal that the general focus of project descriptions falls more on the idea aspect than the entrepreneur aspect. As the mean value 0.179 of EntrepreneurInTitle shows, projects tend to emphasize the idea aspect much more in titles (82.1% vs. 17.9%), and the ratio gap widens in blurbs (89.2% vs. 10.8%) and detailed descriptions (91.6% vs. 8.4%).

To estimate the impact of TCE prioritization on fundraising outcomes, we divide the detailed description into multiple sections according to the following two criteria: (1) extract the first 100 words and the following content, and (2) split the deta ile d description into three parts, na me ly, the first third, second third, and final third. The reason for such division is that entrepreneurs tend to describe both idea and entrepreneur aspects within the detailed description. Is it more attractive to describe the entrepreneur aspect first or to prioritize the idea? This issue can be examined by TCE prioritization. The descriptive statistics indicate that entrepreneurs more often introduce the entrepreneur aspect at the beginning of the 0.076 for EntrepreneurInFirstThirdDetail, and correlation among most of the independent variables.

Table 3. Descriptive statistics (N = 126,593)

<table><tr><td>Category</td><td>Variable</td><td>Description</td><td>AVG</td><td>S.D.</td><td>Median</td><td>Min.</td><td>Max.</td></tr><tr><td rowspan="4">Pledge results-related</td><td>PledgeStatus (1=success)</td><td>Pledge status</td><td>.522</td><td>.500</td><td>1</td><td>0</td><td>1</td></tr><tr><td>NumBackers</td><td>Backers count</td><td>67.814</td><td>117.499</td><td>28</td><td>0</td><td>999</td></tr><tr><td>PledgedRatio</td><td>Pledged ratio</td><td>2.457</td><td>161.618</td><td>1.001</td><td>0</td><td>41535.01</td></tr><tr><td>PledgedAmount</td><td>Pledged amount in U.S. dollars</td><td>9343.27</td><td>76976.77</td><td>1786</td><td>0</td><td>1.03e+07</td></tr><tr><td rowspan="8">Project-related</td><td>NumUpdates</td><td>Number of updates</td><td>5.880</td><td>9.397</td><td>3</td><td>0</td><td>301</td></tr><tr><td>NumComments</td><td>Number of comments</td><td>41.922</td><td>1319.638</td><td>1</td><td>0</td><td>313876</td></tr><tr><td>NumGoal</td><td>Funding goal ($)</td><td>18866.9</td><td>374394.9</td><td>5000</td><td>0.01</td><td>1.00e+08</td></tr><tr><td>NumDays</td><td>Pledge duration days</td><td>35.020</td><td>13.971</td><td>30</td><td>1</td><td>91</td></tr><tr><td>NumPledgeLevels</td><td>Number of pledge levels</td><td>9.004</td><td>5.527</td><td>8</td><td>0</td><td>227</td></tr><tr><td>Video (1=true, 0=otherwise)</td><td>Is an introduction video presented?</td><td>.831</td><td>.374</td><td>1</td><td>0</td><td>1</td></tr><tr><td>Social (1=true)</td><td>Is a social network connected?</td><td>.581</td><td>.493</td><td>1</td><td>0</td><td>1</td></tr><tr><td>NumFollowers</td><td>Number of followers</td><td>492.928</td><td>814.719</td><td>168</td><td>0</td><td>5981</td></tr><tr><td rowspan="3">Description-related</td><td>LengthTitle</td><td>Length of title</td><td>37.246</td><td>16.982</td><td>37</td><td>1</td><td>109</td></tr><tr><td>LengthBlurb</td><td>Length of blurb</td><td>117.248</td><td>25.643</td><td>126</td><td>1</td><td>196</td></tr><tr><td>LengthDetail</td><td>Length of detail description</td><td>5453.567</td><td>5982.085</td><td>3411</td><td>13</td><td>201535</td></tr><tr><td rowspan="4">TCE-related</td><td>EntrepreneurInTitle</td><td>Entrepreneur aspect in the title</td><td>.179</td><td>.617</td><td>0</td><td>0</td><td>1</td></tr><tr><td>EntrepreneurInBlurb</td><td>Entrepreneur aspect in the blurb</td><td>.108</td><td>.343</td><td>0</td><td>0</td><td>1</td></tr><tr><td>EntrepreneurInDetail</td><td>Entrepreneur aspect in the detailed description</td><td>.084</td><td>.635</td><td>0</td><td>0</td><td>1</td></tr><tr><td>EntrepreneurIn100Words</td><td>Entrepreneur aspect in the first 100 words of the detailed</td><td>.161</td><td>.677</td><td>0</td><td>0</td><td>1</td></tr><tr><td rowspan="4"></td><td colspan="7">description</td></tr><tr><td>EntrepreneurInFirstThirdDetail</td><td>Entrepreneur aspect in the first third detailed description</td><td>.123</td><td>.639</td><td>0</td><td colspan="2">0</td></tr><tr><td>EntrepreneurInSecondThirdDetail</td><td>Entrepreneur aspect in the second third detailed description</td><td>.090</td><td>.680</td><td>0</td><td colspan="2">0</td></tr><tr><td>EntrepreneurInLastThirdDetail</td><td>Entrepreneur aspect in the last third detailed description</td><td>.076</td><td>.583</td><td>0</td><td colspan="2">0</td></tr></table>

Table 4. Correlation matrix (Pearson)  
```txt
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22
PledgeStatus 1
(1 = success)
2 NumBackers 0.36 1
Δ*
3 PledgedRatio 0.01 0.00 1
Δ* 6
4 PledgedAmount 0.09 0.09 0.01 1
2* 3* 0*
5 NumUpdates 0.40 0.43 0.01 0.23 1
0* Δ* 3* 2*
6 NumComments 0.02 0.01 0.00 0.45 0.16 1
8* 3* 3 5* 0*
7 NumGoal -0.02 0.00 -0.0 0.03 0.00 0.02 1
9* 7 01 8* 4 3*
8 NumDays -0.12 -0.02 -0.0 0.00 0.01 -0.00 0.01 1
9* 3* 04 2 4* 3 9*
9 NumPledgeLevels 0.13 0.30 0.00 0.12 0.32 0.05 0.01 0.00 1
6* 2* 6 7* 8* 4* 4* 4
10 Video (l=true) 0.11 0.14 0.00 0.04 0.13 0.01 0.00 -0.03 0.20 1
5* 4* 2 1* 9* 1* 3 0* 6*
11 LengthTitle 0.03 0.03 -0.0 0.00 0.03 -0.01 -0.0 0.03 0.05 0.01
5* 1* 03 6
5* 1* 6
5* 1* 6
5* 1* 6
5* 1* 6
5* 1* 6
5* 1* 6
5* 1* 6
5* 1* 6
5* 1* 6
5* 1* 6
5* 1* 6
5* 1* 6
5* 1* 6
4 * A
4 * A
4 * A
4 * A
4 * A
4 * A
4 * A
4 * A
4 * A
4 * A
4 * A
4 * A
4 * A
4 * A
4 * A
4 * A
4 * A
4 * A
4 * A
4 * A
4 * A
4 * A
4 * A
4 * A
4 * A
4 * B
4 * B
4 * B
4 * B
4 * B
4 * B
4 * B
4 * B
4 * B
4 * B
4 * B
4 * B
4 * B
4 * B
4 * B
4 * B
4 * B
4 * B
4 * B
4 * B
4 * B
4 * B
4 * B
4 * B
4 * B
4 * C
4 * C
4 * C
4 * C
4 * C
4 * C
4 * C
4 * C
4 * C
4 * C
4 * C
4 * C
4 * C
4 * C
4 * C
4 * C
4 * C
4 * C
4 * C
4 * C
4 * C
```  
\* means significant at 0.001

## 4.2 Impact of TCE on investment decisions

Table 5 presents our results regarding the impact of TCE on funding outcomes. Using the four measures of funding outcomes, we find consistent results across all four models. Specifically, the coefficients for EntrepreneurInTitle and EntrepreneurInBlurb are both positive and significant, which suggests that the more emphasis the title and blurb put on the entrepreneur aspect, the more likely that the project attracts more funding and backers. That is, the title and blurb should emphasize the entrepreneur’s identity, education, experience, credit, skill, role, qualification, and personal titles, which are conducive to attracting investment. Therefore, Hypothesis 1 is supported.

Furthermore, we also notice that the magnitude for the coefficient of EntrepreneurInTitle is larger than that of the EntrepreneurInBlurb, which suggests that emphasizing the entrepreneur aspect in the title will have an even more substantial positive effect on funding success. In contrast, highlighting the project’s creativity in the title and blurb might not have such effects. In other words, our results suggest that in title and blurb, highlighting the entrepreneur aspect is better than highlighting the idea aspect.

Regarding the detailed description, however, the coefficients of EntrepreneurInDetail are all negative and significant in the four models. Therefore, highlighting the entrepreneur aspect too much in the detailed description seems to demote successful fundraising. In other words, entrepreneurs should focus on describing the creative ideas. Thus, Hypothesis 2 is supported.

We next examine the TCE prioritization in the detailed description. Generally, highlighting entrepreneur profiles still positively affect the funding outcomes if the entrepreneur aspect is placed at the front end of the detailed descriptions (see, e.g., the positive and statistically significant coefficients of EntrepreneurInFirst100Words and EntrepreneurInFirstThirdDetail). However, if the emphasis on description, the effect will turn negative, and sometimes statistically significant. Thus, Hypothesis 3 is rejected. For TCE prioritization, the factors of the idea aspect should follow the entrepreneur aspect.

Table 5. Impact of TCE on investment intention

<table><tr><td>D.V.</td><td colspan="2">PledgeStatus</td><td colspan="2">PledgedRatio</td><td colspan="2">NumBackers (logged)</td><td colspan="2">PledgedAmount (logged)</td></tr><tr><td>EntrepreneurInTitle</td><td>.524***(.0278)</td><td>.52***(.0274)</td><td>.198***(.0105)</td><td>.206***(.0104)</td><td>.215***(.0105)</td><td>.0425***(.003)</td><td>.3***(.0153)</td><td>.311***(.0151)</td></tr><tr><td>EntrepreneurInBlurb</td><td>.245***(.0292)</td><td>.253***(.0285)</td><td>.0952***(.011)</td><td>.107***(.0106)</td><td>.105***(.0109)</td><td>.0258***(.0031)</td><td>.141***(.016)</td><td>.159***(.0155)</td></tr><tr><td>EntrepreneurInDetail</td><td>-.0033**(.0014)</td><td></td><td>-.003***(4.3e-04)</td><td></td><td>-.0044***(4.2e-04)</td><td></td><td>-.0016**(6.2e-04)</td><td></td></tr><tr><td>EntrepreneurInFirst100Words</td><td>.0473***(.014)</td><td></td><td>.0196***(.0048)</td><td></td><td>.0205***(.0048)</td><td></td><td>.0331***(.007)</td><td></td></tr><tr><td>EntrepreneurInFirstThirdDetail</td><td></td><td>.0196**(.0082)</td><td></td><td>-.0026(.0028)</td><td></td><td>.0015*(8.3e-04)</td><td></td><td>.0071*(.0041)</td></tr><tr><td>EntrepreneurInSecondThirdDetail</td><td></td><td>-.0131(.0089)</td><td></td><td>-.0058*(.0031)</td><td></td><td>-8.4e-04(9.0e-04)</td><td></td><td>-.0026(.0045)</td></tr><tr><td>EntrepreneurInLastThirdDetail</td><td></td><td>-.0031(.0078)</td><td></td><td>.0019(.0027)</td><td></td><td>8.4e-05(7.8e-04)</td><td></td><td>-.0047(.0039)</td></tr><tr><td>NumUpdates</td><td>1.52***(.0116)</td><td>1.53***(.0115)</td><td>.659***(.0038)</td><td>.659***(.0038)</td><td>.64***(.0038)</td><td>.147***(.0011)</td><td>.927***(.0056)</td><td>.927***(.0056)</td></tr><tr><td>NumComments</td><td>.913***(.0105)</td><td>.927***(.0105)</td><td>.188***(.0032)</td><td>.188***(.0032)</td><td>.178***(.0031)</td><td>.161***(9.3e-04)</td><td>.475***(.0047)</td><td>.474***(.0047)</td></tr><tr><td>NumGoal</td><td>-1.03***(.0091)</td><td>-1.01***(.0091)</td><td>.0368***(.0026)</td><td>.0368***(.0026)</td><td>.0195***(.0026)</td><td>-.153***(7.6e-04)</td><td>.208***(.0038)</td><td>.208***(.0038)</td></tr><tr><td>NumDays</td><td>-.708***(.0228)</td><td>-.727***(.0228)</td><td>-.207***(.0086)</td><td>-.208***(.0086)</td><td>-.186***(.0085)</td><td>-.0694***(.0025)</td><td>-.307***(.0125)</td><td>-.307***(.0125)</td></tr><tr><td>NumPledgeLevels</td><td>.263***(.0218)</td><td>.323***(.0214)</td><td>.385***(.0077)</td><td>.385***(.0077)</td><td>.297***(.0079)</td><td>.048***(.0022)</td><td>.583***(.0112)</td><td>.584***(.0112)</td></tr><tr><td>Video (1=true)</td><td>.405***(.0241)</td><td>.41***(.024)</td><td>.34***(.009)</td><td>.341***(.009)</td><td>.32***(.009)</td><td>.039***(.0026)</td><td>.564***(.0131)</td><td>.565***(.0131)</td></tr><tr><td>LengthTitle</td><td>-.131***(.0166)</td><td>-.0036***(5.2e-04)</td><td>-.0005***(2.0e-04)</td><td>-.0006***(2.0e-04)</td><td>-.0317***(.0062)</td><td>-.0003***(5.7e-05)</td><td>-.0007**(2.8e-04)</td><td>-.0007**(2.8e-04)</td></tr><tr><td>LengthBlurb</td><td>.11***(.0295)</td><td>.0011***(3.4e-04)</td><td>.0003**(1.3e-04)</td><td>.0003**(1.3e-04)</td><td>.0254**(.0109)</td><td>-4.3e-05(3.7e-05)</td><td>.0013***(1.8e-04)</td><td>.0013***(1.8e-04)</td></tr><tr><td>LengthDetail</td><td>.0094(.0118)</td><td>-.0001***(2.0e-06)</td><td>-.0001***(6.9e-07)</td><td>-.0001***(6.9e-07)</td><td>.12***(.0043)</td><td>.0001***(2.0e-07)</td><td>.0001***(1.0e-06)</td><td>.0001***(1.0e-06)</td></tr><tr><td>Project type dummies</td><td colspan="8">Project type dummies: controlled</td></tr><tr><td>Constant</td><td>9.04***(.111)</td><td>9.05***(.111)</td><td>1.42***(.0535)</td><td>1.42***(.0535)</td><td>.731***(.0756)</td><td>1.57***(.0156)</td><td>2.69***(.078)</td><td>2.69***(.078)</td></tr><tr><td>Adjusted R-squared</td><td>0.491</td><td>0.491</td><td>0.458</td><td>0.458</td><td>0.575</td><td>0.575</td><td>0.548</td><td>0.548</td></tr></table>

大 $\mathsf { \Pi } _ { p \mathsf { \Pi } } \mathtt { \Pi } _ { 0 . 1 0 , \mathsf { \Pi } }$ \*\* $\scriptstyle { p < 0 . 0 5 , }$ \*\*\* ${ \rho } { < } 0 . 0 1$ , Standard errors in parentheses

The coefficients of the control variables also reveal some interesting insights. For example, the number of updates and comments are positively associated with the funding outcomes, which suggests the critical role of community engagement for a successful crowdfunding campaign. Also, while longer video may boost the probability of funding success. Lastly, a title that is too long may hurt the project,

Entrepreneurs' social connections promote the propagation of project information among potential investors. Figure 4 presents the statistical results of social connections and followers grouped by fundraising outcomes. Among the projects that are successfully funded (reaching their funding goals), 53.27% are linked to their social media accoun while the ratio fa lls to 50.67% for fa ile d campa igns. It shows a significant difference in successful fundraising $( p < 0 . 0 0 1 )$ ). Therefore, the link established via social media may improve funding outcomes. Similarly, successful campaigns on average have 575 followers, while those failed have only 403 followers. In other words, more followers may increase the probability of successful fundraising.

![](/api/attachments/4A7GXVNG/fulltext/images/8156e0fd9a7efe203eb2e1b31ccf0609ea41ec989dcab1986250b72d16358e34.jpg)

![](/api/attachments/4A7GXVNG/fulltext/images/a654eb7ba1a973b84c8fe6bac126173a7c0bd0415c8e0a0ad17b2b22978c2b7f.jpg)  
Figure 4. Statistical results of social connections and followers

To investigate the moderating role of social connections on TCE's impact, we formulate the models with interaction terms, as shown in Equations (3):

$$
Y _ {i} = \alpha + T C E _ {i} ^ {\prime} \cdot \beta + S o c i a l _ {i} \cdot E n t r e p r e n e u r I n T i t l e \cdot \delta + Z _ {i} ^ {\prime} \cdot \gamma + \varepsilon_ {i},\tag{3}
$$

where $\mathbf { \chi } _ { : } l _ { i }$ is a dummy variable indicating whether the i-th project has more social connections. We classify $S o c i a l _ { i }$ as one if the social connections (number of followers) of the project is larger than the average of the sample (493 followers). Note that we only examine the moderating effect of social connections on the impact of emphasizing the entrepreneur aspect in the title because it is the most effective place to highlight the entrepreneur profiles.

As social connections would highlight the advantages of the entrepreneur aspect [12], we hypothesized that the impact of TCE might be stronger among projects with more social connections. Figure 5 illustrates the comparison between entrepreneurs with more or less social connections. The results show a significant difference in the impact of TCE on fundraising outcomes if social connections are considered. Specifically, an entrepreneur-oriented strategy is more effective for all entrepreneurs, as shown by the higher values of funding outcomes when EntrepreneurInTitle changes from low to high.

Meanwhile, the entrepreneur-oriented strategy is more effective for entrepreneurs with more social connections, as the slopes are steeper for entrepreneurs with more social connections. Thus, Hypothesis 4 is supported.

![](/api/attachments/4A7GXVNG/fulltext/images/d34fcfbc44f4d8dd9f2dfbeec340fbefa1c456f858430c3cecc960200e7fd981.jpg)  
Figure 5. Moderating effect of social connections on fundraising outcomes

We further examine the moderation effects of funding goals. The specification is as shown in Equations (4):

$$
Y _ {i} = \alpha + T C E _ {i} ^ {\prime} \cdot \beta + H i g h G o a l _ {i} \cdot E n t r e p r e n e u r I n T i t l e \cdot \delta + Z _ {i} ^ {\prime} \cdot \gamma + \varepsilon_ {i},\tag{4}
$$

where $H i g h G o a l _ { i }$ is a dummy variable indicating whether the crowdfunding campaign has a high funding goal, which has the value of one if the project has a higher funding goal (NumGoal) than the sample mean (\$18,867). Figure 6 plots the moderating effects of funding goals. The moderating effect is not significant for pledge status, pledged ratio, and pledged amount, which is evident from the parallel slopes for both groups. However, the number of backers may respond differently to TCE on the entrepreneur aspect. While emphasizing the entrepreneur aspect increases the number of backers in the low funding goal group, it may decrease the number of backers in the high funding goal group. This may be because, for the projects with smaller financing targets, the credentials of the entrepreneurs might be more important. In contrast, for projects that attempt to raise more money, emphasizing the entrepreneur profiles too much may backfire. Therefore, to attract more investors, entrepreneurial projects of higher pledge targets should highlight the idea creativity, while low-target projects need to emphasize the rather than the entrepreneur aspect. Thus, Hypothesis 5 is not supported.

![](/api/attachments/4A7GXVNG/fulltext/images/7c7be7814056acc4c854b55e0667964e73575854e557459743a1cc5004842583.jpg)  
Figure 6. Moderating effect of funding goals on fundraising outcomes

Table 6 summarizes the results of the hypotheses testing.

Table 6. Results of the hypothesis tests

<table><tr><td>Hypothesis</td><td>Results</td></tr><tr><td>H1: Entrepreneur-oriented narratives are more attractive for investment than those that are idea-oriented in titles and blurbs.</td><td>Supported</td></tr><tr><td>H2: Idea-oriented narratives are more attractive for investment than those that are Entrepreneur-oriented in the detailed description.</td><td>Supported</td></tr><tr><td>H3: In the detailed description, introducing the idea aspect at the beginning is more attractive for investment than presenting it at the end of narratives.</td><td>Not Supported</td></tr><tr><td>H4: The positive effect of entrepreneur-oriented TCE on fundraising outcomes is more pronounced in these projects with more social connections.</td><td>Supported</td></tr><tr><td>H5: The positive effect of entrepreneur-oriented TCE on fundraising outcomes is strengthened in these campaigns with higher funding goals.</td><td>Not Supported</td></tr></table>

## 5. Discussion and Conclusion

## 5.1 Practical Implications for Entrepreneurs and Decision Support

In this paper, we intend to answer two questions: (1) whether and how TCE affects fundraising outcomes when entrepreneurs highlight a particular TCE aspect, and (2) how and where the TCE aspect empirical analysis of 126,593 crowdfunding campaigns indicates that the TCE strategy matters to investment decisions.

We find that entrepreneur profiles should be highlighted in the title, blurb, and the beginning of the detailed description, while the idea aspect can be described in the detailed narratives. Furthermore, socia connections amplify the entrepreneur aspect and thus should be fully used to promote the entrepreneur aspect and facilitate successful campaigns. The findings would contribute to the enhancement of managerial practices for crowdfunding stakeholders, including fundraisers and backers.

In venture financing, a long-standing issue is whether investors fund the team or the idea itself. These two arguments have not been tested in the crowdfunding context. Thus, entrepreneurs are lost in whether or how to introduce themselves or their ideas in narratives. The TCE analysis in this paper addresses this issue. Descriptive statistics show that most entrepreneurs tend to present their ideas in detail for successful fundraising. Our study empirically verifies the rationality of this TCE strategy. That is, in the detailed description, highlighting the idea aspect has a positive impact on fundraising outcomes.

However, the distinction between different text levels (title, blurb, and detailed description) has been underexplored in existing research. Our study demonstrates that entrepreneurs should describe the entrepreneur aspect in the title and blurb while highlighting the idea aspect in the detailed description. That is, highlighting the entrepreneur aspect in the title and blurb could lead to an increase in project attractiveness. Meanwhile, idea-oriented detailed descriptions are more attractive. The results would help protection concerns, past studies suggest that entrepreneurs should not describe their ideas in detail but should disclose more person-related information [73]. Due to the legislation lag of intellectual property protection, reducing the risk of idea plagiarism has a positive effect on crowdfunding. However, from a fundraising perspective , our findings indicate that the narrative of project creativity still plays an important role, especially in the detailed descriptions. It seems that creativity should be detailed in the detailed description, despite the risk of leaking business ideas.

Extant studies attribute the attractiveness of startups to a certain aspect, especially in the field of venture capital. However, there is a lack of discussion on the TCE prioritization in the scenario where the introduced. We address how to determine the TCE prioritization when entrepreneurs describ two aspects simultaneously. If the detailed description falls into several parts, entrepreneurs would wonder which part is most effective in introduc ing their creativity or personal profile. Exploring this issue will help entrepreneurs who consider both aspects to create attractive text descriptions. Because the TCE prioritization affects investors' perceptions of project quality, the presentation order of TCE will affect fundraising success. Our empirical results show that in the detailed description, the entrepreneur aspect should only be placed at the beginning of the narrative.

Regarding the narrative generation strategy, introducing entrepreneur factors is recommended, but only applicable to the title, blurb, and the beginning of the detailed narrative. In the detailed description, however, it might backfire. The detailed narrative should focus on campaign creativity. Therefore, if the fundraisers are famous figures, they should exert their advantage by presenting more personal information in the title, blurb, or beginning of the detailed narrative. However, this advantage does not apply to the latter part of the detailed description.

This study can help crowdfunding platforms guide entrepreneurs to generate attractive text descriptions. The main guidelines are as follows. (1) An emphasis on entrepreneur profiles is recommended in the title, blurb, and the beginning of the detailed narrative. (2) In the detailed description, the entrepreneur should focus on the idea aspect of the campaign. (3) Social connections related to the entrepreneur aspect promotes successful campaigns, and entrepreneurs should make full use of social connections in fundraising. Crowdfunding platforms could modification if the text description deviates from the guidelines.

## 5.2 Limitations and future directions

Though the research provides useful insights about how the TCE affects the fundraising outcomes, we also acknowledge some limitations and potentia l directions for future research. First, there are several types of funding models widely used by other platforms. For instance, Rockethub adopts the All-and-More funding model, where the entrepreneur receives all the raised mone less of whether the amount of funding exceeds the funding goal. In such a scenario, a dummy dependent variable is not applicable. Second, natural language processing is a rapidly evolving discipline, comprising a wide range of specialist areas. We adopt deep learning to identify the TCE without considering other potential approaches, such as keyword extraction, text format recognition, and depth grammar recognition. These approaches may enhance the performance of detecting the TCE in future studies [31]. Third, we reveal how TCE influences fundraising outcomes but the paper does not explain why it does so. Future studies could explore the mechanisms referring to psychology and marketing theories. Lastly, only two types of TEC strategies are defined. We first measure the entrepreneur aspect by placing the idea aspect on the opposing side since we believe either the entrepreneur aspect or the idea aspect is mentioned. However, in addition to the two aspects, there may be other content mentioned, such as online communication. We hope the initial insights from our study could inspire more research in this emerging research area.

## Acknowledgments

This work is partially supported by the NSFC Grant (71601082, 71771177), Natural Science Foundation of Fujian Province (2017J01132), Innovation Fund for University Production, Education and Research from China’s Ministry of Education (2019J01012).

## References

[1] F. Munari, L. Toschi, Assessing the impact of public venture capital programmes in the United Kingdom: Do regional characteristics matter?, Journal of Business Venturing, 30(2) (2015) 205-226.

[2] T.M. Amabile, A model of creativity and innovation in organizations, Research in organizational behavior, 10(1) (1988) 123-167.

[3] J.E. Perry-Smith, C.E. Shalley, The social side of creativity: A static and dynamic social network perspective, Academy of management review, 28(1) (2003) 89-106.

[4] M.A. McCollough, B. Devezer, G. Tanner, An alternative format for the elevator pitch, The International Journal of Entrepreneurship and Innovation, 17(1) (2016) 55-64.

and organizations, Handbook of organizations, 7(1965) 142-193.

[6] V. Kuppuswamy, B.L. Bayus, Crowdfunding creative ideas: The dynamics of project backers, in: The Economics of Crowdfunding, (Springer, 2018), pp. 151-182.

[7] A. Schwienbacher, Entrepreneurial risk-taking in crowdfunding campaigns, Small Business Economics, (2015) 1-17.

[8] I.L. Janis, C.I. Hovland, P.B. Field, H. Linton, E. Graham, A.R. Cohen, D. Rife, R.P. Abelson, G.S. Lesser, B.T. King, Personality and persuasibility, (Yale University Press, 1962).

[9] S. Bochner, C.A. Insko, Communicator discrepancy, source credibility, and opinion change, Journal of Personality and Social Psychology, 4(6) (1966) 614.

[10] C. Tu, S. Yang, The role of entrepreneurial creativity in entrepreneurial processes, International Journal of Innovation, Management and Technology, 4(2) (2013) 286-289.

[11] E. Mollick, The dynamics of crowdfunding: An exploratory study, Journal of Business Venturing, 29(1) (2014) 1-16.

[12] R. Kgoroeadira, A. Burke, A. van Stel, Small business online loan crowdfunding: who gets funded and what determines the rate of interest?, Small Business Economics, 52(1) (2019) 67-87.

[13] B.C. Davis, K.M. Hmieleski, J.W. Webb, J.E. Coombs, Funders' positive affective reactions to entrepreneurs' crowdfunding pitches: The influence of perceived product creativity and entrepreneurial passion, Journal of Business Venturing, 32(1) (2017) 90-106.

[14] J. Debrulle, Start-up absorptive capacity: does the owner's human and social capital matter?, International Small Business Journal, 32(7) (2013) 777-801.

[15] J.E. Tinkler, K.B. Whittington, M.C. Ku, A.R. Davies, Gender and venture capital decision-making: the effects of technical background and social capital on entrepreneurial evaluations, Social Science Research, 51(2015) 1-16.

[16] J. Brinckmann, S.M. Kim, Why we plan: the impact of nascent entrepreneurs' cognitive characteristics and human capital on business planning, Strategic Entrepreneurship Journal, 9(2) (2015) 153-166.

[17] J. Hobbs, G. Grigore, M. Molesworth, Success in the management of crowdfunding projects in the creative industries, Internet Research, 26(1) (2016) 146-166.

[18] D. Chaney, A principal–agent perspective on consumer co-production: Crowdfunding and the redefinition of consumer power, Technological Forecasting and Social Change, 141(2019) 74-84.

[19] E. Weinberger, D. Wach, U. Stephan, J. Wegge, Having a creative day: Understanding entrepreneurs daily idea generation through a recovery lens, Journal of Business Venturing, 33(1) (2018) 1-19.

[20] O.M. Lehner, T. Harrer, Crowdfunding revisited: a neo-institutional field-perspective, Venture Capital, 21(1) (2019) 75-96.

[21] M. Innocent, A. Francoislecompte, N. Roudaut, Comparison of human versus technological support to reduce domestic electricity consumption in France, Technological Forecasting and Social Change, 150(2020) 119780.

[22] M. Siering, J.-A. Koch, A.V. Deokar, Detecting fraudulent behavior on crowdfunding platforms: The role of linguistic and content-based cues in static and dynamic contexts, Journal of Management Information Systems, 33(2) (2016) 421-455.

[23] G. Gupta, I. Bose, Strategic learning for digital market pioneering: Examining the transformation of Wishberry's crowdfunding model, Technological Forecasting and Social Change, 146(2019) 865-876.

[24] T.-P. Liang, S.P.-J. Wu, C.-c. Huang, Why funders invest in crowdfunding projects: Role of trust from the dual-process perspective, Inf. Manage., 56(1) (2019) 70-84.

[25] B. Fuller, Y. Liu, S. Bajaba, L.E. Marler, J. Pratt, Examining how the personality, se lf -efficacy, and anticipatory cognitions of potential entrepreneurs shape their entrepreneurial intentions, Personality and Individual Differences, 125(2018) 120-125.

[26] Y. Wang, W. Xu, Leveraging deep learning with LDA-based text analytics to detect automobile insurance fraud, Decision Support Systems, 105(2018) 87-95.

[27] H. Yuan, R.Y. Lau, W. Xu, The determinants of crowdfunding success: A semantic text analytics approach, Decision Support Systems, 91(2016) 67-76.

[28] C. Lagazio, F. Querci, Exploring the multi-sided nature of crowdfunding campaign success, Journal of<sub>Business</sub> <sub>Research,</sub> <sub>90(2018)</sub> <sub>318-324.</sub> Business Research, 90(2018) 318-324

[29] J. Cox, T. Nguyen, A. Thorpe, A. Ishizaka, S. Chakhar, L. Meech, Being seen to care: the relationship Human Behavior, 83(2018) 45-55.

[30] A.M. Petruzzelli, A. Natalicchio, U. Panniello, P. Roma, Understanding the crowdfunding phenomenon and its implications for sustainability, Technological Forecasting and Social Change, 141(2019) 138-148.

[31] A. Majumdar, I. Bose, My words for your pizza: An analysis of persuasive narratives in online crowdfunding, Information & Management, 55(6) (2018) 781-794.

[32] M.J. Zhou, B. Lu, W.P. Fan, G.A. Wang, Project description and crowdfunding success: an exploratory study, Information Systems Frontiers, (2018) 1-16.

[33] J. Yao, J. Chen, J. Wei, Y. Chen, S. Yang, The relationship between soft information in loan titles and online peer-to-peer lending: evidence from RenRenDai platform, Electronic Commerce Research, 19(1) (2019) 111-129.

[34] A. Parhankangas, M. Ehrlich, How entrepreneurs seduce business angels: An impression management approach, Journal of Business Venturing, 29(4) (2014) 543-564.

[35] G.L. de Larrea, M. Altin, D. Singh, Determinants of success of restaurant crowdfunding, International Journal of Hospitality Management, 78(2019) 150-158.

[36] H. Gafni, D. Marom, O. Sade, Are the life and death of an early‐stage venture indeed in the power of the tongue? Lessons from online crowdfunding pitches, Strategic Entrepreneurship Journal, 13(1) (2019) 3-23.

[37] T. Zuzul, M. Tripsas, Start-up inertia versus flexibility: The role of founder identity in a nascent industry, Administrative Science Quarterly, (2019) 0001839219843486.

[38] W. Wang, K. Zhu, H. Wang, Y.-C.J. Wu, The impact of sentiment orientations on successful crowdfunding campaigns through text analytics, IET Software, 11(5) (2017) 229-238.

[39] C.F. Camerer, T.-H. Ho, J.-K. Chong, A cognitive hierarchy model of games, The Quarterly Journal of Economics, 119(3) (2004) 861-898.

[40] D. Hoenig, J. Henkel, Quality signals? The role of patents, alliances, and team experience in venture capital financing, Research Policy, 44(5) (2015) 1049-1064.

[41] R.J. Herring, CoCos: A promising idea poorly executed, Achieving Financial Stability, 61(2017) 103-120.

[42] B. Ohtani, Preparing Articles on Photocatalysis : Beyond the Illusions, Misconceptions, and Speculation, Chemistry Letters, 37(3) (2008) 216-229.

[43] J. Daley, Design creativity and the understanding of objects, Design Studies, 3(3) (1982) 133-137.

[44] A. Simons, L.F. Kaiser, J. vom Brocke, Enterprise crowdfunding: foundations, applications, and research findings, Business & Information Systems Engineering, 61(1) (2019) 113-121.

[45] S.N. Kaplan, B.A. Sensoy, P. Stromberg, Should investors bet on the jockey or the horse? Evidence from the evolution of firms from early business plans to public companies, Journal of Finance, 64(1) (2009) 75-115.

[46] F. Hu, R.H. Trivedi, Mapping hotel brand positioning and competitive landscapes by text-mining user-generated content, International Journal of Hospitality Management, 84(2020) 102317.

[47] G. Ercan, I. Cicekli, Lexical cohesion based topic modeling for summarization, in: International Conference on Intelligent Text Processing and Computational Linguistics, (Springer, 2008), pp. 582-592.

[48] J. Cayla, K. Bhatnagar, A.G. Woodside, Language and power in India's “new services”, Journal of Business Research, 72(2017) 189-198.

[49] Y. Wang, H. Chen, The influence of dialogic engagement and prominence on visual product placement in virtual reality videos, Journal of Business Research, 100(2019) 493-502.

[50] G. Antonini, S.V. Martinez, M. Bierla ire, J.P. Thiran, Behavioral priors for detection and tracking of pedestrians in video sequences, International Journal of Computer Vision, 69(2) (2006) 159-180.

[51] A. Pennisi, D.D. Bloisi, L. Iocchi, Online real-time crowd behavior detection in video sequences, Computer Vision and Image Understanding, 144(2016) 166-176.

[52] S. Wasiuzzaman, What motivates and deters the 'crowd' in crowdfunding in Malaysia?, Journal of Accounting and Finance in Emerging Economies, 6(1) (2020) 323-330.

1143-1168.

[54] L. Deng, P. Jiang, S. Li, M. Liao, Social capital and access to informal finance–evidence from Chinese private firms, Accounting & Finance, 59(5) (2019) 2767-2815.

[55] P.S. Adler, S.-W. Kwon, Social capital: Prospects for a new concept, Academy of management review, 27(1) (2002) 17-40.

[56] R. Andrews, A.M.S. Mostafa, Organizational goal ambiguity and senior public managers’ engagement: does organizational social capital make a difference?, International Review of Administrative Sciences, 85(2) (2019) 377-395.

[57] J. Weiss, T. Anisimova, G. Shirokova, The translation of entrepreneurial intention into startup behaviour: The moderating role of regional social capital, International Small Business Journal, 37(5) (2019) 473-501.

[58] T. Tuan Luu, Ambidextrous leadership, entrepreneurial orientation, and operational performance: Organizational social capital as a moderator, Leadership & Organization Development Journal, 38(2) (2017) 229-253.

[59] R.E. Wood, A.J. Mento, E.A. Locke, Task complexity as a moderator of goal effects: A meta-analysis, Journal of applied psychology, 72(3) (1987) 416.

[60] E. Fang, K.R. Evans, S. Zou, The moderating effect of goal-setting characteristics on the sales control systems–job performance relationship, Journal of Business Research, 58(9) (2005) 1214-1222.

[61] J.-C. Huang, The relationship between conflict and team performance in Taiwan: the moderating effect of goal orientation, The international journal of human resource management, 23(10) (2012) 2126-2143.

[62] D. Paravisini, V. Rappoport, E. Ravina, Risk aversion and wealth: Evidence from person-to-person lending portfolios, Management Science, 63(2) (2016) 279-297.

[63] C. Courtney, S. Dutta, Y. Li, Resolving information asymmetry: Signaling, endorsement, and crowdfunding success, Entrepreneurship Theory and Practice, 41(2) (2017) 265-290.

[64] K. Greff, R.K. Srivastava, J. Koutník, B.R. Steunebrink, J. Schmidhuber, LSTM: A search space odyssey, IEEE transactions on neural networks and learning systems, 28(10) (2016) 2222-2232.

[65] W. James, C. Stein, Estimation with quadratic loss, in: Breakthroughs in statistics, (Springer, 1992), pp. 443-460.

[66] P.L. Bartlett, D.P. Helmbold, P.M. Long, Gradient descent with identity initia lization effic iently learns positive-definite linear transformations by deep residual networks, Neural computation, 31(3) (2019) 477-502.

[67] A. Onan, S. Korukoglu, H. Bulut, Ensemble of keyword extraction methods and classif iers in text classification, Expert Systems With Applications, 57(2016) 232-247.

[68] T.-T. Wong, N.-Y. Yang, Dependency analysis of accuracy estimates in k-fold cross validation, IEEE Transactions on Knowledge and Data Engineering, 29(11) (2017) 2417-2427.

[69] L. Parisi, N. RaviChandran, M.L. Manaog, Decision support system to improve postoperative discharge: A novel multi-class classification approach, Knowledge-Based Systems, 152(2018) 1-10.

[70] W. Zhang, S.-x. Kong, Y.-c. Zhu, Sentiment classification and computing for online reviews by a hybrid SVM and LSA based approach, Cluster Computing, 22(5) (2019) 12619-12632.

[71] E. Kromidha, P. Robson, Social identity and signalling success factors in online crowdfunding, Entrepreneurship & Regional Development, 28(9-10) (2016) 605-629.

[72] T. Wang, X. Liu, M. Kang, H. Zheng, Exploring the determinants of fundraisers’ voluntary information disclosure on crowdfunding platforms: A risk-perception perspective, Online Information Review, 42(3) (2018) 324-342.

[73] N. Richter, P. Jackson, T. Schildhauer, Outsourcing creativity: An abductive study of open innovation using corporate accelerators, Creativity and Innovation Management, 27(1) (2018) 69-78.

Wei Wang, Ph.D., is an Associate Professor at the Department of Information Management, College of Business Administration, at Huaqiao University. His research interests include crowd funding, sentiment analysis, text analysis, and electronic commerce. His work has appeared in academic journals including Computers in Human Behavior, Behaviour & Information Technology, Industria Management & Data Systems, Journal of Experimental & Theoretical Artificial Intelligence, New Review of Hypermedia and Multimedia, Management World (China), Journal of Management Sciences in China, Systems Engineering—Theory & Practice, among others. He holds a Ph.D. from Tongji University in Shanghai, a master’s and a bachelor degree from Huaqiao University in Quanzhou, China.

Wei Chen, Ph.D., is an Assistant Professor at Management Information Systems, Eller College of Management, The University of Arizona. He received his Ph.D.in Innovation, Technology and Operations from the University of California, San Diego. His research interests include crowdsourcing, peer production, fintech and His work has appeared in academic journals including Information Systems Research, MIS Quarterly, and so on.

Kevin Zhu, Ph.D., is a Professor of Innovation, Technology and Operations (ITO), Rady School of Management, University of California, San Diego. He received his Ph.D. from Stanford University. His work focuses on technology-enabled innovation, next generation of information technologies (big data, AI, FinTech) and their adoption in the business world, economic impacts of information technology, integration of online and offli annels, competition and innovation in technology- intensive industries (softwar media, telecomm) as well as digital transformation of traditional industries (manufacturing, retail, and financial service). Dr. Zhu's research has been published in the top academic journals such as Management Science, Information Systems Research, IEEE, MIS Quarterly, and Marketing Science.

Hongwei Wang, Ph.D., is a School of Economics and Management, Tongji University. He received his Ph.D. from Shanghai Jiao Tong University. His research interests include crowd funding, sentiment analysis, text analysis, and electronic commerce. His work has appeared in academic journals including International Journal of Hospitality Management, Industrial Management & Data Systems, Journal of Experimental & Theoretical Artificial Intelligence, New Review of Hypermedia and Multimedia, Management World (China), Journal of Management Sciences in China, Systems Engineering—Theory & Practice, among others.

## Highlights

 Define and detect text content emphasis (TCE) by long short-term (LSTM)

 Estimate the TCE’s impact on fundraising results with the data from Kickstarter

 Title and blurb should focus on the entrepreneur aspect of the campaigns

 The entrepreneur aspect should be placed at the beginning of the detailed narrative

 The idea aspect should be emphasized in the detailed description
