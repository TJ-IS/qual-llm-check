---
otero_id: 2964
otero_key: "9MYFXG3W"
title: "User innovation evaluation: Empirical evidence from an online game community"
authors: "Jifeng Ma; Yaobin Lu; Sumeet Gupta"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.11.003"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

User innovation evaluation: Empirical evidence from an online game community

Jifeng Ma, Yaobin Lu, Sumeet Gupta

![](/api/attachments/9MYFXG3W/fulltext/images/a43836ed2289806214c5522ce9e4afd56403b2bb1a1fe4428cd06c811ed70b76.jpg)

PII: S0167-9236(18)30194-5

DOI: https://doi.org/10.1016/j.dss.2018.11.003

Reference: DECSUP 13011

To appear in: Decision Support Systems

Received date: 25 April 2018

Revised date: 17 November 2018

Accepted date: 18 November 2018

Please cite this article as: Jifeng Ma, Yaobin Lu, Sumeet Gupta , User innovation evaluation: Empirical evidence from an online game community. Decsup (2018), https://doi.org/10.1016/j.dss.2018.11.003

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# User Innovation Evaluation: Empirical Evidence from an Online Game Community

Jifeng Ma

School of Management

Huazhong University of Science and Technology

China

majifeng@hust.edu.com

Yaobin Lu

School of Management

Huazhong University of Science and Technology

China

luyb@mail.hust.edu.cn

Sumeet Gupta

Indian Institute of Management,

sumeetgupta@iimraipur.ac.in

Raipur 493661, India

# ACCEPTED MANUSCRIPT

## Abstract

User innovation community – as a ground for open innovation – has been widely deployed by firms to leverage external sources of innovation. Obtaining contributions from external users, however, poses screening challenges in front of a firm, particularly when such contributions are enormously large in number. Therefore, this study attempts to help firms reduce their workload by examining the differences between adopted and non-adopted user innovations. characteristics of a user innovation: innovation-related, innovator-related, presentation-related and rareness that may influence the evaluation process. The results of logistic regression on a publicly available dataset of 21,557 user innovations spanning five years collected from an online game UIC show that the popularity, integrity and maintenance of the innovation, as well as the prior adoption experience of the innovator, positively influence the adoption of a user innovation by the firm. Moreover, both the complexity of a user innovation and descriptive images have an inverted U-shaped relationship with the adopted innovation. Finally, adopted user innovations have high levels of rareness than non-adopted user innovations. We discuss our findings and implications of this study to research and practice.

Keywords: open innovation; user innovation community; user innovation evaluation; innovation rareness

## 1. Introduction

Innovation is an important strategy for a firm to gain a competitive advantage [1]. Traditionally, innovation has been carried within a firm’s boundary with little involvement of its customers [2]. However, development in information and communication technology (ICT) has made it easy for a firm to engage its customers into the innovation process [3,4]. This new innovation paradigm – termed as open innovation – allows firms to not only leverage external sources of innovation [1], but also substantially lower their R&D costs as well as improve the market acceptance of their innovations [5]. Firms normally practice open innovation by hosting a user innovation community (UIC), whereby they invite and motivate users to generate new ideas, make modifications to the existing products or even develop new products [2,4]. LEGO ideas, hosted by the LEGO group, for example, is a successful UIC where customers submit their innovative ideas for LEGO products. Some of these ideas are adopted and transformed into successful commercial products by the firm [1,3].

Although UICs carry tremendous potential in generating promising ideas, they also suffer from the problem of contribution overload when users contribute large number of ideas in the community [6,7]. Given the limited resources and abilities available with a firm, it is difficult to evaluate such large number of contributions and identify the promising ones [8]. For contributors, their motivations to continuously engage into innovative activities would be impaired if they cannot get quickly responses from companies [9]. Moreover, receiving feedback from firms can help users improve their abilities and therefore suggest high-quality ideas in the future [10]. Thus, screening potentially promising user contributions from the mass efficiently and effectively is a critical challenge for the firm. Previous studies on UICs have primarily focused on two issues: (i) why do users voluntarily engage in innovative behavior [11–13], and (ii) how do firms support such innovative behavior [14–16]. Only a few studies have examined the issue of identifying promising ideas among a large number of contributions. For example, Di Gangi and Wasko [17] examined this issue using diffusion of innovation theory, but did not found any significant influence of relative advantage and compatibility on the likelihood of adoption of an innovative idea. Jensen et al. [7], however, found that positive feedback from other users in a UIC is a good indicator of commercial attractiveness of a user-generated idea. Li et al. [18] found that contributors’ experience and presentation characteristics influence the likelihood of adoption of an idea. We observe a few gaps within this stream of work that need further examination. First, most of the studies in this area focus on the evaluation of contributions proposed by users as ideas [17,18] and not as actual innovations. These studies assume that users can only contribute ideas which should then be transformed into innovations by a firm using its internal resources. However, in a UIC, where actual contributions (and not just ideas) are made by the user, the factors influencing evaluation process may be different. Second, these studies analyze the adoption likelihood considering the inherent characteristics of an innovative idea [17–19]. However, adopting user innovations from the UIC is an approach for a firm to meet customer needs in the market [20]. Therefore, it is important to consider market-based factors, such as customer demand into the evaluation of a user innovation. Third, the data used in most of the previous studies is collected from a single community ‘Dell IdeaStorm’, which limits the generalizability of the findings.

Considering these gaps, this paper is to examine the differences between adopted and non-adopted user innovations. A better understanding of these differences will help firms reduce workload in evaluating user innovations and leverage external sources of innovation more efficiently and effectively. Based on the prior research, we identify three characteristics of a user innovation that influence the evaluation process, including innovation-related characteristics, innovator-related characteristics and presentation-related characteristics. Besides, we also consider a few market-based factors in the examination, as the primary goal of a firm in adopting user innovations is to satisfy their customers. The research model is tested on a publicly available dataset of 21,557 user innovations collected from an online game UIC.

The present study makes three important contributions. First, most research on UICs focused on examining users’ motivation and firms’ support strategies for innovative behavior

# ACCEPTED MANUSCRIPT

and few studies examined the issue of contribution overload experienced by firms attempting UICs [13,21,22]. This study proposes a holistic model to examine different characteristics of a user innovation and evaluate their relative predictive importance. Second, we consider market-based factors into our research model and examine how the rareness of a use innovation influence firms’ evaluation process. Our empirical results show that there is a positive relationship between rareness and adopted user innovations. Third, we extend the literature on UICs to the context of online game UICs. Previous studies assumed that users can only contribute ideas which are then adopted and transformed into actual innovations by a firm using its own internal resources [7,17,18]. However, user in online game UICs can develop an innovation with little help from the firm and therefore play a much more significant role in the innovation process. This new context not only increases the generalizability of our results but also sharpens our understanding of the role of users in the open innovation. This research also makes a few interesting practical contributions for both firms and users. For firms, this study provides some luable guidelines to reduce their efforts in evaluating a user innovation. For instance, firms can establish recognition systems to recognize those experienced innovators who are more likely to develop high-quality innovations. For suggests insights into increasing the adoption likelihood of their innovations. For example, using appropriate images to describe the innovation will make it easier for the firm to understand the innovation and thus increase the adoption likelihood.

## 2. Literature Review

Traditionally, business innovation has occurred exclusively within the boundaries of a firm. Advancement in ICT has broken this boundary and promoted user-generated innovation [23,24]. A number of firms have established UICs where users can contribute and discuss ideas, suggest possible solutions and develop new products [22,25]. Prior research on UICs can be divided into two streams. The first stream consists of studies that have explored the antecedents of user’s intention to innovate [26]. Franke et al. [12], for example, found that

# ACCEPTED MANUSCRIPT

expected benefits and leader-user characteristics of users have significant and positive effects on users’ intention to innovate. Similarly, Zhang et al. [27] demonstrated that community response plays an important role in motivating users’ continuance intention to innovate. Kankanhalli et al. [13] tested three dimensions of expected benefits, including expected enjoyment, expected extrinsic reward and expected recognition, and proved their different effects on potential and actual innovators’ intention to innovate. The second stream consists of studies that have examined the support strategies provided by firms to encourage users’ innovative behavior. For example, Jeppesen [16] demonstrated that innovation toolkit provided by firms plays an important role in facilitating the innovation process. Nambisan and Nambisan [28], similarly noted that virtual customer environment, such as rating systems, elite customer forums and customer recognition programs designed by companies, has a positive effect on engaging users into innovation behavior. Yang et al. [15] suggested that online innovation contest is a good strategy to encourage users with various backgrounds to participate into innovation activities.

Although these studies broaden our understanding of the user innovation behavior, they do not address the issue of contribution overload [29]. The limited resources, such as manpower, budget and time, constrain the firm’s ability to filter the best from a large number of innovations generated by users [30]. Prior studies have identified three characteristics of an idea that may influence the adoption likelihood, namely, idea-related characteristics, innovator-related characteristics and presentation-related characteristics. Regarding idea-related characteristics, Di Gangi and Wasko [17] investigated a firm’s adoption decision by examining 21 ideas contributed by users in Dell’s IdeaStorm. Based on the diffusion of innovation theory [31], they found that the age and complexity of ideas positively influence adoption likelihood, whereas relative advantage and compatibility of ideas do not. Other studies found that the popularity and novelty of an idea are also positively related to the adoption likelihood [18,32,33]. Regarding innovator-related characteristics, previous studies noted that innovators’ past experience and prior adoption rate have positive effects on the idea adoption likelihood because innovators with sufficient knowledge and abilities are more likely

# ACCEPTED MANUSCRIPT

to suggest high-quality ideas [7,9,19]. Presentation-related characteristics refer to the text, images and videos provided by contributors to describe their innovative ideas. As most of ideas in the UIC come from users’ unique experience, it is hard for firms to understand those ideas clearly without sufficient details. Thus, adding descriptive information for ideas can help firms assess the potential value of those ideas and thus enhance the adoption likelihood [32]. However, Li et al. [18] found that number of images provided by contributors has an inverted U-shaped relationship with adoption likelihood because too much descriptive information lead to the problem of information overload. Table 1 summarizes various studies on user innovation adoption.

## Table 1

Studies on User Innovation Adoption

<table><tr><td>Study</td><td>Theoretical lens</td><td>Research context &amp; data</td><td>Research variables</td><td>Key findings</td></tr><tr><td>Di Gangi and Wasko [17]</td><td>Diffusion of innovation theory</td><td>Dell IdeaStorm; Qualitative case data with 21 ideas</td><td>Dependent variable: idea implementation likelihoodIndependent variables: relative advantage; compatibility; idea popularity</td><td>1. Three independent variables have non-significant effects on idea implementation likelihood;2. Idea complexity has a negative effect on idea implementation likelihood</td></tr><tr><td>Bayus [9]</td><td>Cognitive fixation theory &amp; structured imagination theory</td><td>Dell IdeaStorm; Secondary data with 8,801 ideas</td><td>Dependent variable: idea implementation likelihoodIndependent variables: contributors' past experience</td><td>Contributors' past experience has a positive effect on idea implementation likelihood</td></tr><tr><td>Jensen et al. [7]</td><td>Creativity theory &amp; design theory</td><td>LEGO Ideas; Secondary data with designs</td><td>Dependent variable: perceived commercial attractivenessIndependent variables: complexity; positive feedback; contributors' past experience</td><td>1. Complexity has an inverted U-shaped effect on perceived commercial attractiveness;2. Positive feedback has a positive effect on perceived commercial attractiveness;3. Contributors' past experience has a U-shaped effect on perceived commercial attractiveness</td></tr><tr><td>Schemma nn et al. [33]</td><td>Creativity theory</td><td>Online idea crowdsourcing platform; Secondary with 1,456 ideas</td><td>Dependent variable: idea implementation likelihoodIndependent variables: contributors' past experience; idea popularity</td><td>Idea popularity has a positive effect on idea implementation likelihood</td></tr><tr><td>Li et al. [18]</td><td>Message persuasion theory</td><td>Dell IdeaStorm &amp; Idea Exchange; Secondary datawith 19,964</td><td>Dependent variable: idea implementation likelihoodIndependent variables: idea popularity; contributors' pastexperience; idea presentation</td><td>1. Idea popularity has a positive effect on idea implementation likelihood;2. Contributors' prior participation and prior implementation rate have positive effects on idea implementation likelihood;3. Number of images has an inverted U-shaped effect on idea implementation likelihood</td></tr><tr><td>Froehlich et al. [32]</td><td>Knowledge creation theory</td><td>Suggestion System of a manufacturer; Secondary data with 378 ideas</td><td>Dependent variable: idea evaluationIndependent variables: idea novelty; idea presentation</td><td>Idea novelty and idea presentation both have positive effects on idea evaluations</td></tr><tr><td>Hoornaert et al. [19]</td><td>Research of idea selection in UICs</td><td>Mendeley crowdsourcing Community; Secondary data with 7046 ideas</td><td>Dependent variable: idea implementation likelihoodIndependent variables: idea content and distinctiveness; contributors' past experience; crowd feedback</td><td>Three independent variables have positive effects on idea implementation likelihood</td></tr></table>

However, we noted a few critical gaps in these studies. First, previous studies mainly assumed that users in a UIC can suggest ideas, but cannot actually create an innovation [7,17]. They must rely on the firm to adopt their ideas and then use internal resources to turn the s give users an opportunity to make an actual innovation by exposing more core resources, such as by opening the code libraries, and providing more favorable supports, for example, by offering innovation support toolkits [13,34]. Therefore, user plays a much more important role in the innovation process than the case of simply recommending ideas. The process of evaluating an actual innovation in these different from those where only an idea is to be evaluated. For example, there may exist some other innovation-related characteristics that affect firms’ adoption decision. Moreover, it is difficult for firms to understand and analyze a user innovation, so innovator-related and presentation-related characteristics are still important for firms to predict the potential value of a user innovation. Second, previous studies have not considered the role of market-based factors in the adoption of a user innovation. Unlike the case of suggesting ideas, users need to rely on their own resources to design and create an innovation. Therefore, the quality of these innovations varies for innovators depending upon their levels of experience and knowledge. Since the adopted innovation will be sold back to customers in the market, those innovations with low market acceptance may endanger the firm’s reputation and performance [35]. Thus, a firm must consider market-related factors into the evaluation of an actual innovation. Third, it is important to extend the studies of user innovation evaluation to different research contexts.

We try to fill these gaps in this study by examining the differences between adopted and non-adopted user innovations based on the characteristics as identified in previous studies, namely, innovation-related characteristics, innovator-related characteristics and presentation-related characteristics in the context of an online game UIC. We also incorporate market-based factors that may influence the evaluation process of a user innovation.

First, innovation-related characteristics are factors that influence the value of a user innovation. Previous studies argue that the popularity and complexity of an innovative idea have significant effects on its attractiveness to customers [7,12,36]. As our research focuses on user innovations and not just ideas, we additionally examine two other product-related attributes of a user innovation, namely, integrity and maintenance. Integrity refers to the degree to which innovative components developed by users can be successfully integrated with the existing components [37]. Although, in a UIC, users can innovate any component of an existing product, their innovation should be dovetailed with the existing components. It is important that a firm should consider integration of innovations with other existing components so as to ensure a high-quality final product. Another important product-related characteristic is the maintenance. As users possess limited skills and knowledge, their innovations may have errors or bugs which would impede their normal use [38]. Prior research suggests that maintenance is a good approach to solve these errors and thus improve the quality of a user-generated software [39].

Second, innovator-related characteristics, in our study, refer to the prior experience and expertise possessed by an innovator. Previous studies note that prior adoption experience of the innovator is positively related to the adoption likelihood of an idea [12,40,41]. Since, developing an innovation is much more difficult as compared to suggesting an idea, an innovator who has generated successful innovations would be perceived as possessing enough skills and knowledge for undertaking the entire innovation process and develop a high-quality

innovation.

Third, presentation-related characteristics are also important because a firm may not be able to accurately evaluate the innovation generated by a user unless it is presented properly [6]. Providing sufficient descriptive information about the innovation makes the value embedded in it clear and thus facilitates the evaluation process [8]. However, too much descriptive information may lead to information overload which can hamper the adoption decision. Li et al. [18] found that there is an inverted U-shaped relationship between descriptive information and the likelihood of adoption of an idea.

Besides these three characteristics, we also consider market-based factors into our examination because satisfying customer needs is the primary goal of firms in adopting user innovations in the UIC [25]. We use rareness –the demand/supply ratio – to highlight the role of marketplace in evaluating a user innovation. Previous studies have mostly focused on the supply side of an innovative idea and reported mixed results. Poetz and Schreier [42], for innovative idea. On the other hand, Kornish and Ulrich [43] found that ideas that are different from existing ones in the UIC, do not increase the likelihood for further investment. One possible reason for these inconsistent results is that prior studies have neglected the effect of market demand. A unique and limited-in-supply user innovation may not be adopted, if there is no demand for such kind of innovation in the market. Therefore, we use rareness to measure both demand and supply side of a user innovation and examine its effect on the adoption of a user innovation.

## 3. Research model and hypotheses

Drawing on the above literature review, we present our research model in Figure 1 followed by a discussion on the hypotheses.

![](/api/attachments/9MYFXG3W/fulltext/images/b3402090806dc06d09b4acaa9b81bc31fe22bf212d5a565c783a7321ebba08f6.jpg)  
Fig. 1. Research Model

## 3.1 Innovation characteristics

## 3.1.1 Popularity

In a UIC, customers can freely browse the homepage of a user innovation and add it to their favorite list. This addition to the favorite list can be considered as a cue of a user innovation being preferred by other users and is thus a good indicator of its popularity in the community [44]. Previous studies argued that the popularity of a product is a signal of its value to the customers [45], and is therefore, positively related to the future investments from firms [18,33]. Bartl et al. [46] suggested that firms can use online community as a test market to verify the popularity of a user innovation and thus predict its potential commercial attractiveness. In summary, a user innovation’s popularity is a signal of its value and future market acceptance. Hence, we hypothesize:

H1: User innovations with higher levels of popularity are more likely to be adopted by the firm.

## 3.1.2 Complexity

When evaluating the potential value of a user innovation, firms consider its distinguishing characteristics (such as appearance and function) from the existing similar products in the market [47]. Inculcating differentiation makes an innovation complex as it possesses more unique features [7]. The potential value of a complex innovation is usually higher than a simple one because it can provide more functionalities to the customer [36]. However, after a certain point, higher level of complexity may have a negative effect on the commercial attractiveness because it is difficult for firms to understand such innovation and assess its potential value. Previous studies also reported that the market acceptance of overly complex products is low, as it is hard for customers to comprehend such products [48,49]. Hence, we hypothesize:

H2: There is an inverted U-shaped relationship between the level of complexity and adoption of user innovation.

## 3.1.3 Integrity

Integrity refers to the degree to which innovations created by users can be integrated with the existing product [50]. In a UIC, users are allowed to freely develop or modify any component of an existing product [25]. As a product consists of several different components, a firm has to evaluate the fit between the innovative components developed by users and the existing product components [7]. If the innovative component is not consistent (in terms of its appearance, function and structure) with the existing product components, a firm may not adopt it for two reasons. First, it would be time-consuming and costly for firms to integrate a various components of a product may decrease its attractiveness to a customer and thus lower its commercial value [50]. Therefore, if users develop components which can be properly integrated with the existing product components, the potential value of their innovations will be higher. Hence, we hypothesize:

H3: User innovations with higher levels of integrity are more likely to be adopted by the firm.

## 3.1.4 Maintenance

As users in a UIC generally lack professional knowledge and technical skills, their innovations are often fraught with errors. In an open source software development community (OSSD), developers usually solve bugs in the software through upgrading and these maintenance efforts improve the productivity and quality of the software [38,39]. In a UIC, innovators can continuously improve and upgrade their innovations based on the feedback from other members [25]. Therefore, maintenance from the innovator, in general, delivers a signal to the firm that the innovation is more valuable. Hence, we hypothesize:

H4: User innovations with higher levels of maintenance are more likely to be adopted by the firm.

## 3.2 Innovator characteristics

Since making an innovation requires high levels of expertise and experience, most users may not be able to develop an actual innovation by themselves [3]. An innovator whose innovations have been adopted previously is expected to have sufficient knowledge and experience in developing a high-quality and valuable innovation. Hoornaert et al. [19] noted good indicator of the likelihood of implementation of their ideas. Bayus [9] found that experienced contributors are more likely to suggest ideas that are valuable enough to be implemented by the firm. Therefore, innovators who have more prior adoption experience are more likely to develop a higher quality innovations. Hence, we hypothesize:

H5: User innovations developed by innovators with more prior adoption experience are more likely to be adopted by the firm.

## 3.3 Presentation characteristics

Lack of detail about the innovation is one of the biggest challenges faced by firms during the evaluation process [7]. As most of the user innovations are a result of innovators’ personal experience of problems with the existing products, firms may find it hard to understand the innovations clearly [25]. In a UIC, innovators can use text, image, and/or video to describe their innovations. Providing sufficient descriptive information about the innovation facilitates the evaluation process and increases the adoption likelihood [8]. However, excessive descriptive information about an innovation may result in information overload and thus has a negative effect on the evaluation process [18]. This is because the limited cognitive ability to process large amounts of information at a time may interfere with the evaluation of the innovation by the firm [18] and other members [49]. Hence, we hypothesize:

H6: There is an inverted U-shaped relationship between the presentation characteristics (including description length, number of images and number of videos) and adoption of user innovation.

## 3.4 Innovation rareness

In this study, we use rareness to examine the impact of marketplace on the evaluation of the user innovation. Specifically, we consider the rareness of a user innovation from both supply and demand perspective. Previous studies used novelty to measure the supply of an idea and examined the relationship between the novelty of an idea and firms’ future investment intention, while the results are inconsistent [42,43]. One possible reason for this inconsistency could be that the influence of market demand was ignored. Therefore, we incorporate demand by using demand/supply ratio as the measure of rareness. A lower magnitude of this ratio implies that the supply of this kind of innovations in the community is high, but the market demand is low, and therefore a firm should refrain from adopting this innovation. A higher magnitude, on the contrary, indicates a greater likelihood of adoption of an innovation by the firm because the demand in the market is relatively high. Hence, we hypothesize:

H7: User innovations with higher levels of rareness are more likely to be adopted by the firm.

## 4. Research method

## 4.1 Research subject and data collection

Following previous studies in innovation management [14,51], we selected the UIC of a globally leading online game as our research subject. This online game is one of the most popular multiplayer online battle arena game (MOBA) across the world, with over a million concurrent players during the peak period. In 2012, the game developer established a UIC that allows players to create and submit user-generated contents, such as cosmetic items and

# ACCEPTED MANUSCRIPT

custom game modes, for the game. In order to operationalize our variables and examine the hypotheses, we focused on the user-generated cosmetic items for heroes – the characters controlled by players in the game. Cosmetic items refer to visual elements for different heroes in the game. Each hero has several slots, such as head, arm, shoulder and weapon, which can be equipped with unique accessories and users can optionally create innovative contents for these slots to decorate a specific hero. It should be noted that if a user creates accessories for more than one slot of a specific hero, these items can be placed into a collection known as ‘item set’. After players submit their innovations to the UIC, the firm evaluates and decides whether to adopt these innovations. At the same time, other members in the UIC can comment on an innovation and add it to their favorite list. Once these innovations are adopted by the firm, they will be added into the real game and other users can buy them with real money from the game store. Innovators of these adopted innovations will receive a percentage share of the sales of their items. However, innovators cannot modify their innovations, once these tions that are not adopted by the firm cannot be downloaded or experienced by other users. The detailed information about user innovations can be obtained from their product homepages. Appendix A presents a screen shot of the homepage of a user innovation. Appendix B illustrates the activities of the innovator, the firm and other members in the UIC in different phases.

We collected this publicly available data from the user innovation homepage using a web crawler during January 2018. To test our research model, we used a dataset of user innovations submitted from April 17, 2012 (the day first innovation was submitted) to obtained the final dataset consisting of 21,557 user innovations. Among these, 4,203 user innovations were adopted by the firm.

## 4.2 Measurement of variables

The unit of analysis in this study is a user innovation and the dependent variable is the adoption status of a user innovation. Adoption status is mentioned in the homepage of a user

# ACCEPTED MANUSCRIPT

innovation. We code the dependent variable as 1, if a user innovation is adopted, and 0 otherwise. We measure popularity as the ratio of the number of favorites to the number of page visitors in a user innovation. Other members in the community can show their interests in a user innovation by adding it to their favorite list after visiting its homepage. Such behavior signals the popularity of a user innovation in the UIC [44]. We measure complexity as the log-transformed file size of an innovation because of its skewed distribution. Prior studies found that size is a good indicator of the complexity because products with more features are usually bigger than those with less features [39]. We measure integrity as a binary variable indicating whether an innovation is placed into a collection (1) or not (0). Collection implies a set of innovations for a specific hero. For example, an innovator may create a new weapon, shoulder and armor for a specific hero and then place these together as a set or collection. Therefore, the innovations in a collection can completely decorate a hero without any need for integration with other components. On the other hand, innovations that are not in a collection need to be matched with other existing components to decorate a hero and may result in a mismatch. Thus, innovations, which are included in the collection, have higher levels of integrity than those which are not. Maintenance is measured by the number of updates an innovator has made to the innovation. Update is an activity performed by an innovator to continuously modify and upgrade the innovation and can be considered as the maintenance of an innovation by the innovator.

To measure innovator-related characteristic, namely prior adoption experience, we consider the number of adopted innovations made by the innovator prior to the current innovation. We choose the number of prior adopted innovations rather than prior innovation as the measure of innovator experience, because successful adoption experience is more valuable for innovators to create high-quality innovations [18].

To measure presentation-related characteristics, namely, the description length, number of images and number of videos, we use log-transformed number of words, number of images (JPG and GIF format) and number of videos respectively as mentioned in the description of an innovation. Innovators can optionally describe their innovations using texts, images or

videos during submission.

To measure rareness, we use a log-transformed ratio of search volume from Google Trends for a specific hero in the current month to the number of prior innovations in this hero category. The monthly search volume across the world for each hero was extracted from game-related search category of the Google Trends during the period of data collection. Google Trends has been widely used as a tool for predicting customer demand in previous studies [52] and can therefore be used as a reflection of customer demand for a specific hero in our study. The high trends index of a specific hero signals the popularity of this hero in the market, and therefore the firm should adopt more user innovations from this hero category in the UIC to satisfy customer needs. The supply of an innovation is measured by the number of innovations in the same hero category prior to the current innovation. Each hero has a unique model, and therefore, guidelines, knowledge and skills required to create innovations for various heroes are different. Therefore, it is suitable to classify innovations by heroes. In our dataset, there are 116 hero categories. The measurement of the denominator can be considered as the supply of user innovations for one specific hero in the UIC because the goal of developing these innovations is to decorate the same hero. Greater supply means that a firm has more choices to select from a number of alternative innovations, and therefore, adoption likelihood of a particular innovation in this hero category will be lower [43]. In summary, a higher demand/supply ratio implies that that demand for a specific hero is higher as compared to the supply of user innovations in this hero category in the UIC, and hence the innovation can be considered as high on rareness. This ratio reflects the rareness of a certain user innovation from both demand and supply perspective.

We also add a few control variables in our empirical model. Age of community is measured as the number of months passed since the day first innovation was submitted to the community [18]. Given the limited resources available with the host-firm, the evaluating process may be constrained when there are too many innovations submitted in the same day. Thus, we use same day submission which is measured by the number of innovations submitted on a single day as a control variable [53]. We use game search trends which is measured as the monthly search volume data of the game from Google Trends during the time period of our data collection to control for exogenous demand shocks on the game which may influence the adoption decision [54,55]. The detailed description of variables in our research model is presented in Table 2.

The descriptive statistics for all variables in our research model are presented in Table 3. The correlations of the variables are reported in Table 4 and we can note that all values are below 0.35. In addition, we performed the variance inflation factor (VIF) test and found that all values are below 2, indicating the absence of multicollinearity in our study.

Table 2  
Description of variables

<table><tr><td>Construct</td><td colspan="2">Variable</td><td>Description</td><td>Reference</td></tr><tr><td rowspan="8">Innovation Value</td><td rowspan="4">Innovation Characteristics</td><td>Popularity</td><td>Ratio of favorites to page visitors in a user innovation</td><td>Susarla et al. [44]</td></tr><tr><td>Complexity</td><td>File size of a user innovation</td><td>Midha and Bhattacherjee [39]</td></tr><tr><td>Integrity</td><td>1 if a user innovation is placed into a collection; 0 otherwise</td><td>Clark and Fujimoto [50]</td></tr><tr><td>Maintenance</td><td>The number of update the innovator has made</td><td>Hienerth et al. [40]</td></tr><tr><td>Innovator Characteristics</td><td>Prior adoption experience</td><td>The number of prior adopted innovations of an innovator before the current innovation</td><td>Jessen et al. [7]</td></tr><tr><td rowspan="3">Presentation Characteristics</td><td>Description length</td><td>The number of words in the innovation description</td><td>Li et al. [18]</td></tr><tr><td>Number of images</td><td>The number of images (JPG and GIF format) in the innovation description</td><td>Li et al. [18]</td></tr><tr><td>Number of videos</td><td>The number of videos in the innovation description</td><td>Li et al. [18]</td></tr><tr><td>Innovation Rareness</td><td>Rareness</td><td></td><td>Ratio of search volume from google trends for a specific hero in the current month to the number of innovations in this hero category prior to the current innovation</td><td>Fang and Chen [52]; Kornish and Ulrich [43]</td></tr><tr><td rowspan="3">Controls</td><td>Age of community</td><td></td><td>The number of month passed since the day of first innovation submitted to the community</td><td>Li et al. [18]</td></tr><tr><td>Same day submission</td><td></td><td>The number of innovations submitted in the same day</td><td>Culnan et al. [53]</td></tr><tr><td>Game search trends</td><td></td><td>The monthly search volume data of the game from Google</td><td>Ghose [54]; Gu et al. [55]</td></tr></table>

Table 3 Descriptive Statistics of variables

<table><tr><td></td><td>Mean</td><td>SD</td><td>Minimum</td><td>Maximum</td><td>Median</td></tr><tr><td>Adoption status</td><td>0.19</td><td>0.40</td><td>0</td><td>1</td><td>0</td></tr><tr><td>Popularity</td><td>0.02</td><td>0.02</td><td>0</td><td>0.82</td><td>0.02</td></tr><tr><td>Integrity</td><td>0.73</td><td>0.44</td><td>0</td><td>1</td><td>1</td></tr><tr><td>Maintenance</td><td>0.36</td><td>0.85</td><td>0</td><td>16</td><td>0</td></tr><tr><td>Complexity</td><td>17.95</td><td>30.78</td><td>0</td><td>661.73</td><td>8.48</td></tr><tr><td>Prior adoption experience</td><td>30.17</td><td>50.60</td><td>0</td><td>446</td><td>4</td></tr><tr><td>Description length</td><td>144.62</td><td>242.87</td><td>0</td><td>5545</td><td>67</td></tr><tr><td>Number of images</td><td>1.03</td><td>2.57</td><td>0</td><td>29</td><td>0</td></tr><tr><td>Number of videos</td><td>0.02</td><td>0.20</td><td>0</td><td>7</td><td>0</td></tr><tr><td>Rareness (ln)</td><td>0.52</td><td>0.73</td><td>0</td><td>9.21</td><td>0.33</td></tr><tr><td>Game search trends</td><td>55.08</td><td>14.82</td><td>23</td><td>100</td><td>57</td></tr><tr><td>Age of community</td><td>29.33</td><td>16.38</td><td>0</td><td>66</td><td>27</td></tr><tr><td>Same day submission</td><td>7.52</td><td>13.06</td><td>0</td><td>82</td><td>4</td></tr></table>

## Table 4

Correlations of variables

<table><tr><td></td><td>VIF</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td></tr><tr><td>(1) Adoption status</td><td>—</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(2) Popularity</td><td>1.12</td><td>0.200***</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(3) Complexity (ln)</td><td>1.05</td><td>0.038***</td><td>-0.049***</td><td></td><td></td><td></td><td></td></tr><tr><td>(4) Integrity</td><td>1.20</td><td>0.155***</td><td>0.083***</td><td>0.144***</td><td></td><td></td><td></td></tr><tr><td>(5) Maintenance</td><td>1.03</td><td>0.191***</td><td>0.086***</td><td>-0.007</td><td>0.026***</td><td></td><td></td></tr><tr><td>(6) Prior adoption experience</td><td>1.20</td><td>0.236***</td><td>0.044***</td><td>0.088***</td><td>0.245***</td><td>0.029***</td><td></td></tr><tr><td>(7) Description length (ln)</td><td>1.05</td><td>0.069***</td><td>0.065***</td><td>0.005</td><td>-0.011</td><td>0.068***</td><td>-0.077</td></tr><tr><td>(8) Number of images</td><td>1.16</td><td>0.030***</td><td>0.030***</td><td>0.017**</td><td>0.209***</td><td>0.030***</td><td>0.184**</td></tr><tr><td>(9) Number of videos</td><td>1.03</td><td>0.018**</td><td>0.006</td><td>0.016**</td><td>0.031***</td><td>0.002</td><td>0.066***</td></tr><tr><td>(10) Rareness (ln)</td><td>1.23</td><td>0.088***</td><td>0.145***</td><td>-0.048***</td><td>-0.095***</td><td>0.066***</td><td>-0.094***</td></tr><tr><td>(11) Game search trends</td><td>1.12</td><td>0.001</td><td>-0.114***</td><td>-0.037***</td><td>-0.042***</td><td>-0.079***</td><td>-0.043***</td></tr><tr><td>(12) Age of community</td><td>1.74</td><td>-0.121***</td><td>-0.206***</td><td>0.190***</td><td>0.304***</td><td>-0.071***</td><td>0.338***</td></tr><tr><td>(13) Same day submission</td><td>1.04</td><td>0.207***</td><td>0.064***</td><td>-0.016**</td><td>0.126***</td><td>0.057***</td><td>0.121***</td></tr><tr><td></td><td></td><td>(7)</td><td>(8)</td><td>(9)</td><td>(10)</td><td>(11)</td><td>(12)</td></tr><tr><td>(8)</td><td></td><td>-0.030***</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(9)</td><td></td><td>0.019***</td><td>0.169***</td><td></td><td></td><td></td><td></td></tr><tr><td>(10)</td><td></td><td>0.073***</td><td>-0.096***</td><td>-0.017**</td><td></td><td></td><td></td></tr><tr><td>(11)</td><td></td><td>0.086***</td><td>0.005</td><td>0.026***</td><td>-0.162***</td><td></td><td></td></tr><tr><td>(12)</td><td></td><td>-0.193***</td><td>0.273***</td><td>0.018**</td><td>0.276***</td><td>-0.187***</td><td></td></tr><tr><td>(13)</td><td></td><td>0.032***</td><td>0.007</td><td>0.017**</td><td>-0.009</td><td>0.040***</td><td>-0.017**</td></tr></table>

Note: \*\*\* p<0.01; \*\* p<0.05; \* p<0.1

## 4.3 Empirical model

We use logistic regression to examine our research hypotheses because the dependent variable in our model is a binary variable. Logistic regression has been widely used in previous studies to analyze choice decisions of firms [9,18]. Considering the independent variables (popularity, complexity, integrity, maintenance, prior adoption experience, description length, number of images, number of videos, and rareness) and control variables (game search trends, age of community, and same day submission) as influencing the adoption status of a user innovation, we formulate the logistic regression model as follows:

$$
\begin{array}{l} \text {P(Adoption status_{i} = 1|X_{i})} \\ = \bigwedge \left( \begin{array}{c} \beta_ {0} + \beta_ {1} \cdot (\text {Game search trends_{i}}) + \beta_ {2} \cdot (\text {Age of community_{i}}) \\ + \beta_ {3} \cdot (\text {Same day submission_{i}}) + \beta_ {4} \cdot (\text {Popularity_{i}}) + \beta_ {5} \cdot (\ln \text {Complexity_{i}}) \\ + \beta_ {6} \cdot (\text {Integrity_{i}}) + \beta_ {7} \cdot (\text {Maintenance_{i}}) + \beta_ {8} \cdot (\text {Prior adoption experience_{i}}) \\ + \beta_ {9} \cdot (\ln \text {Description length_{i}}) + \beta_ {1 0} \cdot (\text {Number of images_{i}}) \\ + \beta_ {1 1} \cdot (\text {Number of videos_{i}}) + \beta_ {1 2} \cdot (\ln \text {Rareness_{i}}) + \beta_ {1 3} \cdot (\ln \text {Complexity_{i}}) ^ {2} \\ + \beta_ {1 4} \cdot (\ln \text {Description length_{i}}) ^ {2} + \beta_ {1 5} \cdot (\text {Number of images_{i}}) ^ {2} \\ \beta_ {1 6} \cdot (\text {Number of videos_{i}}) ^ {2} + \varepsilon_ {\mathrm{i}} \end{array} \right) \end{array}
$$

In this equation, $\beta _ { 0 }$ is the intercept; ε<sub>i</sub> is the error term; $\beta _ { \mathrm { j } }$ (from 1 to 16) is the regression coefficient of each predictor variable. We use maximum likelihood estimation method to examine this model.

## 5. Results

The detailed results of the logistic regression are presented in Table 5. Model 1 includes control variables only. The coefficients for game search trends and age of community are significant and negative, whereas the coefficient for same day submission is significant and positive. Model 2 represents the results with the main effects of our independent variables. Model 3 adds the quadratic effects of complexity, description length, number of images and number of videos. The value of pseudo R-squared among these models is increasing from 5.16% to 19.92%, indicating a good model fit for our research model. In addition, the log likelihood value is also increasing from Model 1 to Model 3. Thus, we use Model 3 for subsequent interpretations.

# ACCEPTED MANUSCRIPT

Table 5  
Logistic regression results

<table><tr><td>Variable</td><td>Model 1</td><td>Model 2</td><td>Model 3</td></tr><tr><td>Intercept</td><td>-0.975***(0.077)</td><td>-3.063***(0.12)</td><td>-3.141***(0.145)</td></tr><tr><td>Game search trends</td><td>-0.003*(0.001)</td><td>0.003*(0.001)</td><td>0.002 (0.001)</td></tr><tr><td>Age of community</td><td>-0.021***(0.001)</td><td>-0.045***(0.002)</td><td>-0.047***(0.002)</td></tr><tr><td>Same day submission</td><td>0.033***(0.001)</td><td>0.025***(0.001)</td><td>0.025***(0.002)</td></tr><tr><td>Popularity</td><td></td><td>0.182***(0.012)</td><td>0.178***(0.012)</td></tr><tr><td>Complexity (ln)</td><td></td><td>0.141***(0.017)</td><td>0.413***(0.069)</td></tr><tr><td>Integrity</td><td></td><td>1.070***(0.056)</td><td>1.039***(0.056)</td></tr><tr><td>Maintenance</td><td></td><td>0.414***(0.024)</td><td>0.409***(0.024)</td></tr><tr><td>Prior adoption experience</td><td></td><td>0.014***(0.0004)</td><td>0.013***(0.0004)</td></tr><tr><td>Description length (ln)</td><td></td><td>0.035**(0.012)</td><td>-0.024(0.037)</td></tr><tr><td>Number of images</td><td></td><td>0.025***(0.007)</td><td>0.115***(0.018)</td></tr><tr><td>Number of videos</td><td></td><td>-0.079(0.076)</td><td>0.348(0.222)</td></tr><tr><td>Rareness (ln)</td><td></td><td>0.068**(0.024)</td><td>0.065**(0.024)</td></tr><tr><td>Complexity $(ln)^2$ </td><td></td><td></td><td>-0.059***(0.014)</td></tr><tr><td>Description length $(ln)^2$ </td><td></td><td></td><td>0.009(0.005)</td></tr><tr><td>Number of image $^2$ </td><td></td><td></td><td>-0.007***(0.001)</td></tr><tr><td>Number of video $^2$ </td><td></td><td></td><td>-0.128(0.07)</td></tr><tr><td>Log pseudolikelihood</td><td>-10086.42</td><td>-8546.65</td><td>-8516.81</td></tr><tr><td>N</td><td>21557</td><td>21557</td><td>21557</td></tr><tr><td>Pseudo R-squared</td><td>5.16%</td><td>19.64%</td><td>19.92%</td></tr></table>

Robust standard errors in parentheses  
Note: \* p<0.05; \*\* p<0.01；\*\*\* p<0.001

Regarding innovation-related characteristics, three variables, namely popularity, integrity and maintenance, show significant positive effects on the adopted innovation (p<0.001). Specifically, for one unit increase in the popularity of an innovation, the odds of adoption increase by 19.48% (β=0.178). The odds ratio of integrity and maintenance are 1.83 (β=1.039) and 50.53% (β=0.409) respectively. Thus, H1, H3 and H4 are supported. Moreover, the coefficient value of squared complexity is significant and negative (p<0.001). This result indicates an inverted U-shaped relationship between the level of complexity and adopted user innovation, thus supporting H2. According to the results in Model 3, the innovation adoption likelihood increases until the complexity reaches 33.1 and decreases after that.

Regarding innovator-related characteristics, the results indicate that innovators with more prior adoption experience are more likely to develop adopted innovation (β=0.013, p<0.001). An increase in the prior adoption experience by one-unit results in a 1.34% increase in the odds ratio. Thus, H5 is supported.

Regarding presentation-related characteristics, the results show an inverted U-shaped relationship with adopted innovation only for number of images and not for description length and number of videos. Based on the results in Model 3, the innovation adoption likelihood increases until the number of images reach 8 and decreases after that. Thus, H6 is partially supported.

Finally, the rareness of user innovation has a significant and positive effect on the adoption of user innovation (β=0.065, p<0.001). An increase in rareness by one-unit results in the increase of odds of innovation adoption likelihood by 6.72%. Thus, H7 is supported.

As the evaluation process is quite time-consuming, recent innovations may less likely be assessed timely and hence the possibility of their adoption will be lower. This bias may make our results inaccurate. Therefore, we excluded all innovations that were made within last one year of data collection. This reduced our dataset to 19,364. We ran the same analysis on the new dataset but did not notice any significant differences from the earlier results. This indicates that our results are robust.

## 6. Discussion and implications

## 6.1 Discussion of findings

Through this study, we report a few interesting findings. First, innovation characteristics, innovation. Consistent with the results of previous studies [7,18,46], our study also reveals that popularity is an important predictor of the adoption likelihood of a user innovation. Moreover, our results reveal that the integrity of an adopted innovation is 1.83 times that of non-adopted innovation. Maintenance is also positively related to the adopted innovation. It means that upgrading is a good approach for innovators to improve the potential value of a user innovation. In addition, the inverted U-shaped relationship between complexity and adopted innovation is also confirmed in our study. This finding is also consistent with the results of previous studies in other types of UICs [7].

Second, prior adoption experience of innovators has a significant and positive effect on

# ACCEPTED MANUSCRIPT

the adopted innovation. This indicates that with the accumulation of adoption experience over time, innovators are more likely to develop a high-quality innovation. Third, the number of images has a significant inverted U-shaped effect on the adopted innovation. Specifically, if innovators provide more than 8 images, it may lead to information overload which interferes with the evaluation of a user innovation. However, description length and number of videos do not have such effect on the adopted innovation. Finally, rareness of a user innovation has a positive and significant effect with the adopted innovation. Using demand/supply ratio as the measure of rareness, we demonstrate that adopted innovations have a high level of rareness than non-adopted innovations.

## 6.2 Implications for research

Our study has a few interesting contributions to research. First, we draw attention towards investigating the differences between adopted and non-adopted user innovations in an online game UIC. Prior research mainly focused on users’ motivation to innovate [12,14,27,41] and explored the strategy to support user innovation behavior [13,15,16], and did not address the issue of contribution overload. In this study, we developed a holistic model to address this question and demonstrated that innovation-related characteristics, innovator-related characteristics and presentation-related characteristics can be used to distinguish adopted innovation from non-adopted innovation.

Second, we included market-based factors into our examination as adopting a user innovation from the UIC is a strategy for the firm to satisfy customer needs in the market [1,3],. Prior research only focused on the supply side effect and reported inconsistent results [42,43]. In our paper, we used the rareness of a user innovation, measured by the demand/supply ratio, to highlight the role of marketplace in the evaluation phase. The results show that adopted innovations have higher levels of rareness than non-adopted innovations.

Third, prior studies mostly focus on the UICs in the IT industry which limit the generalizability of the results. Moreover, these studies widely assume that users must rely on the firm to adopt their ideas and then use internal resources to make the real products. However, users in online game UIC can entirely develop an innovation by themselves. This new research subject not only increases the generalizability of our empirical results but also extends our understanding about the roles of users in the innovation process.

## 6.3 Implications for practice

The results of this study present several valuable practical implications. First, our research indicates that innovation characteristics, such as popularity, complexity, maintenance and integrity, can be utilized to evaluate user innovations. Firms can use these results to establish mechanisms that facilitate the evaluation process. For example, rating and voting systems may be helpful for firms to ascertain the popularity of a user innovation. Firms should encourage innovators to develop a complete set of innovations, not a stand-alone innovation, and periodically upgrade their innovations as these activities will improve the potential value of these innovations. In addition, firms should remind innovators not to develop overly complex innovations as this may increase the effort on the part of the firm to understand and evaluate the innovation and thereby reduce the adoption likelihood.

Second, it is important for firms to identify experienced users because they are more likely to develop high-quality innovations. There are several useful mechanisms to achieve this goal. For example, firms can establish a recognition system to award points and virtual badges to innovators depending on the number of innovations developed by them. Based on this practice, firms can easily observe innovations generated by experienced innovators. strong social identity for these experienced users, but also facilities communications among innovators and firms. Furthermore, the outcomes from this forum may be worthy of deeper analysis of their potential value.

Third, firms should motivate users to provide sufficient descriptive details about their innovations which will help firms understand their innovations easily. To achieve this, firms can make functions that allow users to upload texts, images or videos to describe their innovations. However, it should be noted that providing images is not always good. If the number of images is more than a threshold value (e.g. eight images in our study), it may result in information overload for reviewers and thus have a significant negative effect on the adoption likelihood. Therefore, users should control the number of images and select only those can describe their innovations clearly during the submission.

Finally, our results show that the rareness of a user innovation has a significant and positive effect on the adopted innovation. Thus, innovators should not only focus on improving the value of an innovation, but also consider the impact of the potential market. Even if the quality of an innovation is high, firms may still not adopt because it does not meet customer requirements in the market. Firms can develop an index to suggest the kind of innovations that are more likely to be accepted in the market to the innovator.

## 6.4 Limitations and future research

Although our study makes several valuable contributions, its results must be interpreted in the light of its limitations. First, given the limited scope of our data, we could not incorporate all variables that may affect the evaluation process. For example, future studies may examine whether the valence and extremity of comments on an innovation have significant effects on collect the data at a time immediately preceding the adoption decision. Future research can collect time series data in a certain period and accurately examine the factors that influence the adoption decision. Second, although we provide some guidelines for firms to evaluate user innovations, the actual commercial value of these adopted innovations is not clear. Further studies can collect sales data to measure the actual commercial value of an adopted innovation. This will help firms dynamically adjust their adoption strategy. Third, we conduct our research in an online game UIC. It may be interesting to examine firms’ evaluation process in other types of UICs. Moreover, there may exist other mechanisms to evaluate a user innovation. For example, user innovations in LEGO community must obtain more than 10,000 supports from other members in the community before being eligible for formal evaluation from designers in LEGO. Thus, other members play an important role in the evaluation process. It would be quite interesting for future research to figure out which kind of evaluation mechanism is more effective for firms.

# ACCEPTED MANUSCRIPT

## Acknowledgement

This work was partially supported by a grant from the National Nature Science Foundation of China (71810107003) and the National Social Science Fund of China (18ZDA109). This work was also partially supported by the Modern Information Management Research Centre at HUST.

Appendix A. User Innovation Homepage  
![](/api/attachments/9MYFXG3W/fulltext/images/398906c561500e574b2213336d006eb3fbee619a116b28a4e3d9ff10c9d942ad.jpg)  
Appendix B. Time Line of User Innovation in the UIC

![](/api/attachments/9MYFXG3W/fulltext/images/bc6dfd9082d4f9473553a8664c23ca3ceb36274b60da6a0ae7bc5d7592d4f05e.jpg)  
-Firm: evaluate user innovation -Other users in the UIC: browse user innovation homepage, make comments and add into favorite list if they like -Innovator: receive feedback from other users and upgrade the innovation  
-Firm: adopt user innovation and add into the game -Other users in the UIC: browse user innovation homepage, make comments, add into favorite list and buy the innovation in the game store if they like -Innovator: receive a percentage share of the sales of adopted innovation, but no more changes on

## References

[1] H.W. Chesbrough, Open Innovation: The New Imperative for Creating and Profiting From Technology, 2003.

[2] E. Von Hippel, S. Ogawa, J.P.J. de Jong, The Age of the Consumer—Innovator, MIT Sloan Management Review. 53 (2011) 27–35.

[3] E. Von Hippel, Innovation by user communities: Learning from open-source software, MIT Sloan Management Review. 42 (2001) 82–86.

[4] E. Von Hippel, Democratizing Innovation: The Evolving Phenomenon of User Innovation, International Journal of Innovation Science. 1 (2009) 29–40.

[5] S. Thomke, E. Von Hippel, Customers as innovators: A new way to create value, Harvard Business Review. 80 (2002) 74–81.

[6] P.M. Di Gangi, M.M. Wasko, R.E. Hooker, Getting Customers’ ideas To Work For You: Learning From Dell How To Succeed With Online User Innovation Communities, Mis Quarterly Executive. 9 (2010) 213–228.

[7] M.B. Jensen, C. Hienerth, C. Lettl, Forecasting the commercial attractiveness of user-generated designs using online data: An empirical study within the LEGO user community, Journal of Product Innovation Management. 31 (2014) 75–93.

[8] T. Schulze, M. Indulska, D. Geiger, A. Korthaus, Idea assessment in open innovation:

A state of practice, in: European Conference on Information Systems, ECIS, 2012: pp. 4965–4967.

[9] B.L. Bayus, Crowdsourcing New Product Ideas over Time: An Analysis of the Dell IdeaStorm Community, Management Science. 59 (2013) 226–244.

[10] Y. Huang, P. Vir Singh, K. Srinivasan, Crowdsourcing New Product Ideas Under Consumer Learning, Management Science. 60 (2014) 2138–2159.

[11] C. Lüthje, Characteristics of innovating users in a consumer goods field: An empirical study of sport-related product consumers, Technovation. 24 (2004) 683–695.

[12] N. Franke, E. Von Hippel, M. Schreier, Finding Commercially Attractive User Innovations:A Test of Lead-User Theory, Journal of Product Innovation Management. 23 (2006) 301–315.

[13] A. Kankanhalli, H. (Jonathan) Ye, H.H. Teo, Comparing Potential and Actual Innovators: An Empirical Study of Mobile Data Services Innovation, MIS Quarterly. 39 (2015) 667–682.

[14] R. Prügl, M. Schreier, Learning from leading-edge customers at the Sims: Opening up the innovation process using toolkits, R&D Management. 36 (2006) 237–250.

[15] Y. Yang, P. Chen, R. Banker, Winner Determination of Open Innovation Contests in Online Markets, in: Thirty Second International Conference on Information Systems,

[16] L.B. Jeppesen, User toolkits for innovation: Consumers support each other, Journal of Product Innovation Management. 22 (2005) 347–362.

[17] P.M. Di Gangi, M. Wasko, Steal my idea! Organizational adoption of user innovations from a user innovation community: A case study of Dell IdeaStorm, Decision Support Systems. 48 (2009) 303–312.

[18] M. Li, A. Kankanhalli, S.H. Kim, Which ideas are more likely to be implemented in online user innovation communities? An empirical analysis, Decision Support Systems. 84 (2016) 28–40.

[19] S. Hoornaert, M. Ballings, E.C. Malthouse, D. Van den Poel, Identifying New Product

Ideas: Waiting for the Wisdom of the Crowd or Screening Ideas in Real Time, Journal of Product Innovation Management. 34 (2017) 580–597.

[20] F. Damanpour, M. Schneider, Phases of the adoption of innovation in organizations: Effects of environment, organization and top managers, British Journal of Management. 17 (2006) 215–236.

[21] S. Vosen, T. Schmidt, Forecasting private consumption: survey-based indicators vs. Google trends, Journal of Forecasting. 30 (2011) 565–578.

[22] Y.S. Hau, Y.G. Kim, Why would online gamers share their innovation-conducive knowledge in the online game user community? Integrating individual motivations and social capital perspectives, Computers in Human Behavior. 27 (2011) 956–970.

[23] C. Fuchs, M. Schreier, Customer empowerment in new product development, Journal of Product Innovation Management. 28 (2011) 17–32.

[24] S. Nambisan, Designing Virtual Customer Environments for New Product 392–413.

[25] J. Füller, G. Jawecki, H. Mühlbacher, Innovation creation by online basketball communities, Journal of Business Research. 60 (2007) 60–71.

[26] K.M. Chu, H.C. Chan, Community based innovation: Its antecedents and its impact on innovation success, Internet Research. 19 (2009) 496–516.

[27] C. Zhang, J. Hahn, P. De, Research Note-Continued Participation in Online Innovation Communities : Does Community Response Matter Equally for Everyone ?, Information Systems Research. 24 (2013) 1112–1130.

[28] S. Nambisan, P. Nambisan, How to Profit From a BetterVirtual Customer Environment, MIT Sloan Management Review. 49 (2008) 53–61.

[29] J. West, M. Bogers, Leveraging external sources of innovation: A review of research on open innovation, Journal of Product Innovation Management. 31 (2014) 814–831.

[30] I. Blohm, C. Riedl, J.M. Leimeister, H. Krcmar, Idea Evaluation mechanisms for collective inteligence in open innovation communities: do traders outperformm raters ?,

in: Thirthy Second International Conference on Information Systems, 2011: pp. 1–24.

[31] E.M. Rogers, Diffusion of innovations, 2003.

[32] J.K. Froehlich, M. Hoegl, M. Gibbert, Idea selection in suggestion systems: a thematic similarity perspective, R&D Management. 46 (2016) 887–899.

[33] B. Schemmann, A.M. Herrmann, M.M.H. Chappin, G.J. Heimeriks, Crowdsourcing ideas: Involving ordinary users in the ideation phase of new product development, Research Policy. 45 (2016) 1145–1154.

[34] G. Parker, M. Van Alstyne, X. Jiang, Platform Ecosystems: How Developers Invert the Firm, MIS Quarterly. 41 (2017) 255–266.

[35] J. West, S. Gallagher, Challenges of open innovation: the paradox of firm investment in open‐ source software, R&D Management. 36 (2006) 319–331.

[36] C. Baldwin, C. Hienerth, E. von Hippel, How user innovations become commercial products: A theoretical investigation and case study, Research Policy. 35 (2006) 1291– 1313.

[37] R.W. Veryzer, B. Borja de Mozota, The Impact of User-Oriented Design on New Product Development: An Examination of Fundamental Relationships\*, Journal of Product Innovation Management. 22 (2005) 128–143.

[38] I. Stamelos, L. Angelis, A. Oikonomou, G.L. Bleris, Code quality analysis in open source software development, Information Systems Journal. 12 (2002) 43–60.

[39] V. Midha, A. Bhattacherjee, Governance practices and software maintenance: A study of open source projects, Decision Support Systems. 54 (2012) 23–32.

[40] C. Hienerth, C. Lettl, Exploring How Peer Communities Enable Lead User Innovations to Become Standard Equipment in the Industry: Community Pull Effects, Journal of Product Innovation Management. 28 (2011) 175–195.

[41] L.B. Jeppesen, L. Frederiksen, Why Do Users Contribute to Firm-Hosted User Communities? The Case of Computer-Controlled Music Instruments, Organization Science. 17 (2006) 45–63.

[42] M.K. Poetz, M. Schreier, The value of crowdsourcing: Can users really compete with

professionals in generating new product ideas?, Journal of Product Innovation Management. 29 (2012) 245–256.

[43] L.J. Kornish, K.T. Ulrich, Opportunity Spaces in Innovation: Empirical Analysis of Large Samples of Ideas, Management Science. 57 (2011) 107–128.

[44] A. Susarla, J. Oh, Y. Tan, Social Networks and the Diffusion of User-Generated Content : Evidence from YouTube Social Networks and the Diffusion of User-Generated Content : Evidence from YouTube, Information System Research. 23 (2012) 22–41.

[45] S. Dewan, Y.I. Ho, J. Ramaprasad, Popularity or Proximity: Characterizing the Nature of Social Influence in an Online Music Community, Information Systems Research. 28 (2017) 117–136.

[46] M. Bartl, J. Füller, H. Mühlbacher, H. Ernst, A managers perspective on virtual customer integration for new product development, Journal of Product Innovation Management. 29 (2012) 1031–1046.

[47] N. Franke, P. Keinz, C.J. Steger, Testing the Value of Customization: When Do Customers Really Prefer Products Tailored to Their Preferences?, Journal of Marketing. 73 (2009) 103–121.

[48] B.G.C. Dellaert, S. Stremersch, Marketing Mass-Customized Products: Striking a Balance Between Utility and Complexity, Journal of Marketing Research. 42 (2005) 219–227.

[49] M.A. Stanko, Toward a theory of remixing in online innovation communities, Information Systems Research. 27 (2016) 773–791.

[50] K.B. Clark, T. Fujimoto, The Power of Product Integrity, Harvard Business Review. 68 (1990) 107–118.

[51] L.B. Jeppesen, M.J. Molin, Consumers as Co-developers: Learning and Innovation Outside the Firm, Technology Analysis & Strategic Management. 15 (2003) 363–383.

[52] Z. Fang, C.C. Chen, A novel trend surveillance system using the information from web search engines, Decision Support Systems. 88 (2016) 85–97.

[53] M.J. Culnan, P.J. McHugh, J.I. Zubillaga, How Large U.S. Companies Can Use Twitter and Other Social Media to Gain Business Value, MIS Quarterly Executive. 9 (2010) 243–259.

[54] A. Ghose, Internet exchanges for used goods: an empirical analysis of trade patterns and adverse selection, MIS Quarterly. 33 (2009) 263–291.

[55] B. Gu, J. Park, P. Konana, The impact of external word-of-mouth sources on retailer sales of high-involvement products, Information Systems Research. 23 (2012) 182– 196.

Authors Biography

![](/api/attachments/9MYFXG3W/fulltext/images/0489700e4679c1fefce5768b2d5c551d7280caf0ead2004beeb84e632dbab85b.jpg)

Jifeng Ma is a PhD student in Management Science & Information Systems at School of Management, Huazhong University of Science & Technology in China. His research interests include mobile commerce, social commerce, and technology adoption of Information System. He has published in Pacific Asia Conference on Information Systems (PACIS).

![](/api/attachments/9MYFXG3W/fulltext/images/87192670ecbb0150fe0c6780eadd20ed346b37f9a8207f38493da63106ea20cc.jpg)

Yaobin Lu is a specially appointed Professor in Management Science & Information Systems at School of Management, Huazhong University of Science & Technology in China. His research interests include social commerce, mobile commerce, business mode, electronic commerce, and related topics. He is the author of more than 50 publications in leading international journals such as Journal of Management Information Systems, Decision Support Systems, Information Systems Journal, Information & Management, International Journal of Electronic Commerce, and Journal of Information Technology.

![](/api/attachments/9MYFXG3W/fulltext/images/fd7888424e824450046cca8ff312b0c92637d3c35b1a8a884c438add94ddd717.jpg)

Sumeet Gupta is chair of the Research Division at the Indian Institute of Management Raipur, India. He received his M.B.A. and Ph.D. from the National University of Singapore. He was associated with the Logistic Institute-Asia Pacific, Singapore as a research fellow and worked on several projects with the ASEAN Secretariat, DFS Gallerias, and SAP A.G., Walldorf, Germany. He is the author of more than fifty publications in leading international journals (Decision Support Systems, International Journal of Electronic Commerce, and others) and conference proceedings (ICIS, AMCIS, ECIS, PACIS, and others). He has also published many book chapters. His research interests include supply chain management and business analytics.

## Highlights

 We focus on the evaluation of user-generated innovations.

 We use a secondary data of 21,557 user innovations to examine our model.

 Innovation rareness is an important factor during the evaluation.
