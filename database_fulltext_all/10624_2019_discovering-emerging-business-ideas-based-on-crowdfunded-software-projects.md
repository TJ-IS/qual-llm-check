---
otero_id: 10624
otero_key: "TXQURDR6"
title: "Discovering emerging business ideas based on crowdfunded software projects"
authors: "Won Sang Lee; So Young Sohn"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2018.10.013"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Discovering emerging business ideas based on crowdfunded software projects

![](/api/attachments/TXQURDR6/fulltext/images/f79c301026be8cdf24e5f0f9cab3c824f27d7b702dd50026d9fe7726a22f4517.jpg)

Won Sang Lee, So Young Sohn

<table><tr><td>PII:</td><td>S0167-9236(18)30170-2</td></tr><tr><td>DOI:</td><td>https://doi.org/10.1016/j.dss.2018.10.013</td></tr><tr><td>Reference:</td><td>DECSUP 13005</td></tr><tr><td>To appear in:</td><td>Decision Support Systems</td></tr><tr><td>Received date:</td><td>1 April 2018</td></tr><tr><td>Revised date:</td><td>18 October 2018</td></tr><tr><td>Accepted date:</td><td>23 October 2018</td></tr></table>

Please cite this article as: Won Sang Lee, So Young Sohn , Discovering emerging business ideas based on crowdfunded software projects. Decsup (2018), https://doi.org/10.1016/ j.dss.2018.10.013

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Discovering Emerging Business Ideas based on Crowdfunded Software Projects Won Sang Lee\*, So Young Sohn\*

Dept. of Information and Industrial Engineering Yonsei University, 134 Shinchon-dong, Seoul, Republic of Korea \* Corresponding Author

## Highlights

 50 latent topics are identified from software-related projects on Kickstarter.

 New business ideas are proposed using conjoint analysis with a design thinking approach.

 Different combinations of software business ideas are recommended for different countries.

## Acknowledgement

This work was supported by the National Research Foundation of Korea (NRF) grant funded by the Korea government (MSIP) (2016R1A2A1A05005270).

# Discovering Emerging Business Ideas based on Crowdfunded Software Projects

## Abstract

User-centered innovation has attracted considerable interest for exploiting emerging business ideas. We suggest a novel framework for discovering emerging business ideas and their combination with user-centered innovation in the software industry based on design thinking processes. We apply topic modeling to projects on Kickstarter which is one of the largest crowdfunding platforms in the world. We adopt conjoint analysis to find which topics are most preferred upon the platform in terms of the amount of funding that they have received. From our findings, the convergence of smart assistant services with various domains, such as tutoring mathematics and seeking job opportunities, is recommended as an emerging idea for software businesses. We also find that the ideas preferred in the US are different from those preferred in other countries. Our findings can be exploited effectively for decision support in establishing a new business model. Finally, this study contributes to discovering emerging business ideas by connecting user-centered innovation with a design thinking perspective.

Keywords: Crowdfunding; User-centered Innovation; Design Thinking

## Highlights

 50 latent topics are identified from software-related projects on Kickstarter.

 New business ideas are proposed using conjoint analysis with a design thinking approach.

 Different combinations of software business ideas are recommended for different countries.

## 1. Introduction

Sourcing innovative ideas is one of the important factors in gaining a competitive advantage (Chesbrough, 2003). Unfortunately, many innovative ideas do not meet the needs of daily life.

Nevertheless, it is necessary to generate creative ideas properly based on market demand (Shah &

Tripsas, 2007). It follows that there is a need to focus on user-centered innovation, especially in the software industry where innovative ideas are continuously generated and commercialized. Usercentered innovation offers an alternative to existent innovation systems for sourcing emerging ideas. Indeed, user-centered innovation is growing rapidly and has attracted considerable interest from both academia and industry (Von Hippel, 2009). Furthermore, user-centered innovation can be fostered on a crowdfunding platform (Shah & Tripsas, 2007).

This study considers crowdfunding initiatives as an effective way to promote user-centered innovation. In the crowdfunding environment, individuals create and commercialize their own solutions to the needs and problems that exist within their daily lives (Shah & Tripsas, 2007). Crowdfunding offers interesting means for commercialization by enabling users to propose their ideas locally through requesting funds. If the projects receive more funds than requested, innovators can proceed toward commercialization. Innovative ideas affiliated with such commercialized projects may have a high degree of market demand. Accordingly, this study focuses on the possibility that these ideas and their combinations can contribute toward forming new business models which are critical for the success of innovative services (Li, 2018). For example, an emerging business idea, such as artificial intelligence needs. Such a system combines voice recognition, recommendations, an online music platform, and a chat bot application. Its usage and development could lead to convergence between diverse business areas and eventually contribute to the creation of new business models.

Our study provides a novel method for the discovery of new business ideas. In particular, we apply design thinking - which can be associated with the user-centered approach - to crowdfunded projects. The p method used consists of the joint use of topic modeling and conjoint analysis. Thereafter we empirically show the effective application of our framework in the software industry. The software industry is a suitable case study for our proposed methodology because technological innovation continuously occurs within it to reflect the daily needs of businesses. Such business ideas can play a critical role in creating new markets and accelerating the economic

ecosystem based on new business idea. As innovative ideas can be important with regard to regional knowledge capabilities (Bogers & West, 2012; Lau & Lo, 2015), it is necessary to associate the region with the discovered business ideas. We also attempt to distinguish between the leading country in the software industry and other countries by comparing the proposed business ideas derived in the US with those derived in other regions.

This is one of the few studies to propose using the design thinking approach with the joint use of the conjoint analysis and topic modeling for discovering new business ideas and measuring their effective combinations. The analysis proposes innovative business ideas by combining emerging topics based on crowdfunded ideas. The findings of this study contribute to the acceleration of usercentered innovation as a new business model which reflects our daily needs. The remainder of this paper is structured as follows. Section 2 presents a review of previous studies on design thinking for user-centered innovation. Section 3 introduces our research framework. Section 4 provides the findings of this study. Based on the analytical findings, Section 5 discusses and provides details on designing emerging innovations, and conclusion is provided.

## 2. Literature Review

## Innovation of Software Industry and Related Issues

Since 2000, innovative technologies have grown and have been shared in the open innovation system owing to the development of IT (Ahn et al., 2016). Innovative technologies can lead to the creation of new markets and firms (Calia et al., 2007). Such a process can efficiently utilize resources and provide goods or services to communities (Antolín-López et al., 2015). New markets and industries are eventually created based on the open innovation system. In addition, the open innovation system needs to adopt a corresponding business model (Zott et al., 2011).

Creative ideas can be derived from innovative technologies and within the software industry, innovative technologies and ideas are continuously generated and commercialized. The software industry is different from other areas since it has both zero marginal costs in generating copies and

# ACCEPTED MANUSCRIPT

opportunities for upgrades (Raghunathan, 2000). Software can converge with other areas in accelerating businesses since most industries exploit software. In addition, it does not require massive amounts of raw materials which lead to the industry possessing low entry barriers. The generation of creative ideas and the adoption of an innovative approach are key factors for the success of business models in the software industry (Hui & Tam, 2002). Currently, the software-related market and industry are experiencing high growth, and are thus attracting a crowd. These characteristics of the software industry correspond to the user-centered innovation system where users could pursue their innovations.

Many previous studies have explored the innovative attempts of the software industry to understand the rapid development of software. Munir et al. (2016) argued that the software industry has continuously experienced the emergence of innovation for decades. Their findings suggest that start-ups prefer the open innovation ecosystem compared to incumbents. Their findings also suggest that start-ups assimilate knowledge into their R&D activities in such an open environment.

Some studies indicate that software could eventually contribute to the further development of businesses and the pursuit of innovation. Boudreau (2012) found that a close relationship exists between the number of producers and the number of software varieties that exist on a given platform. This study also suggested that the link was closely associated with the diversity and distinct specializations of producers. Edison et al. (2013) mentioned that innovation needs to add value in terms of customer value, user experience, and internal value. The commercialization of innovation in this context was highlighted.

To further pursue innovation in software, it is necessary to attract people to participate in the innovation ecosystem for software and support commercialization (Bhatt et al., 2016). Some might consider the business models of major ICT companies, such as the Apple app market or the Android app market, as examples. However, issues related to the management and maintenance of such platforms also exist (Kim, 2016). Such concerns could lead to the strict management of providers on the given platform, which might hinder free and active participation on the platform. Kim (2016) suggested that the platform would collapse if participants did not continue to support it, even if it was already established. For generating more innovation in software, the user-centered approach can be useful because it can contribute to the development of software through which the needs of people can be satisfied.

Crowdfunding Initiatives for User-centered Innovation

Recently, user-centered innovation has attracted considerable attention worldwide as a consequence of it being an effective mechanism through which to source innovative ideas (Li et al., 2016). Crowdfunding initiatives are regarded as representing the implementation of such usercentered innovations in this paper. People experience the necessity of satisfying for their daily needs, and they are likely to come up with solutions to meet these needs (Shah & Tripsas, 2007). It is argued that user-centered innovation could grow quickly due to the development of ICT (Von Hippel, 2009). This kind innovation is different from extant innovation since the former considers the daily needs of individuals (Shah & Tripsas, 2007; Von Hippel, 2009). It could deal with various aspects of daily life, and it could even lead to new industries being established and unserved market niches being created (Agarwal & Shah, 2014). Recently, Hoornaert et al. (2017) identified the latent ideas for the development of new IT products from crowdsourcing communities. They applied text mining and classification to crowdsourced ideas for their selection based on Mendeley, which provides IT service for the research community.

Crowdfunding initiatives provide an opportunity for publicly and promptly commercializing user-centered innovation (Gamble et al., 2017). This approach can be of interest in the development of new products (Luchs et al., 2016). Crowdfunding initiatives are platforms that are accessible online, and are places in which people can propose their ideas and request funds from others (Siering et al., 2016). Various categories, including art, technology, and games, can exist on a crowdfunding platform. Mollick (2014) considered crowdfunding as a substitute source of finance for innovation that might find it difficult to raise funds through traditional financial institutions. Therefore, crowdfunding initiatives enable people to promote their ideas and commercialization by focusing on the needs of daily lives. Such ideas are likely to bring substantial changes to innovations in science

# ACCEPTED MANUSCRIPT

and technology as well as their commercialization (Calic & Mosakowski, 2016).

Since crowdfunded innovations are based on the interaction of diverse entities, diversity can be important (Bogers & West, 2012). This importance may stem from various users’ “local” daily needs (Haefliger et al., 2010). Diverse ideas are likely to be sourced through crowdfunding initiatives since there are various different perspectives on satisfying the daily needs. The complexity of innovation necessitates the need for the integration of ideas from diverse sources (Quintana-García & Benavides-Velasco, 2008; Subramaniam, & Youndt, 2005). Thus, diversity is considered as an important source of innovative activities (Frenken et al., 2007). It is necessary to discover and combine emerging business ideas for providing the solutions to daily needs of users. This study considers that an influential crowdfunded innovation could be discovered by the combination of diverse innovations at a conceptual level. Such innovative ideas based on customer needs might play an important role as components of an innovative business model (Chesbrough, 2003). In the following section, we review design thinking that has been focused toward combining diverse innovations for designing user-centered software.

## Design Thinking for Crowdfunded Innovations

There could be many ways to find what can be the effective way for pursuing the user-centered approach. This paper considers the design thinking approach as a good candidate. Bazjanac (1974) mentioned that a design process consists of well-defined activities and assumes that application of scientific method can contribute to problem solving. Design thinking, which has been widely discussed since 2000, can be considered as a problem-solving approach that can improve business outcomes (Brown, 2009). Due to its fast-growing nature, there exist various definitions and different understandings of design thinking. Among the various approaches, the systematic approach of design thinking is important and necessary (Cooper et al., 2009). Design thinking explains the process of transforming ideas into products based on design theories (Liedtka, 2015).

The design thinking approach is likely to correspond to the user-centered approach with regard to discovering emerging business ideas. Recently, the user-centered approach has been considered to be very important for design thinking in the business environment (Liedtka, 2015). There could be some reasons for the emergence of user-centered approach. First, there rises the issue of who will design the product (Moreau, 2011). The boundaries between designers and users are currently blurred and this can lead to the generative engagement of users and result in co-designing activities (Garud et al., 2008). The current study adopts the design thinking perspective for pursuing user-centered innovation. Secondly, the role of empathy is important in design thinking (Liedtka, 2015). This emphasizes that latent topics from the perspective of users. Thirdly, it is important to provide prototypes of the ideas that exist in design thinking. Liedtka (2015) mentioned that design needs to be concrete and visual in order to highlight the core concepts through visualization and prototyping. The current study considers this approach in designing the concepts of products or services that can be utilized in prototyping business models.

Since design thinking emphasizes the engagement and empathy of users in product innovation, we exploit conjoint analysis as part of our methodology. Conjoint analysis is a practical method by which to analyze and understand the demands of users. It measures how users evaluate the multitudinous attributes of individual products and services (Green & Rao, 1971). The analysis is used widely in marketing research to quantify the relative preference for particular attributes from customers – both individually and collectively (Caruso et al., 2009; Scholz et al., 2015). Discovering and combining existing knowledge can play an important role in achieving value-added innovation (Mukherjee et al., 2016). Indeed, conjoint analysis can discover user preferences based on user needs, and the diverse combinations of such preferences are considered. Such conjoint analysis could contribute to the further use and adoption of the design thinking approach. Conjoint analysis has been successfully applied to emerging areas and innovative services (Berger et al., 2015).

Previous studies provided evidence as to the wide application of conjoint analysis in terms of innovation. Jedidi and Zhang (2002) applied the analysis in examining the utility of consumers, and attempted to estimate how respondents’ willingness to pay varied in accordance with product attributes. Radford and Bloch (2011) argued that by measuring consumers preferences with regard to a

# ACCEPTED MANUSCRIPT

given product’s functions, conjoint analysis might provide useful information for managers who prototype products. Conjoint analysis could be also useful for researchers who attempt to understand the interaction between products and consumers. Zhang et al. (2011) utilized the choice-based conjoint analysis for their study on alternative fuel vehicles. They analyzed 7,000 respondents to infer consumer preferences. Jee and Sohn (2015) suggested that the individual preferences for adopting a wearable device. They segmented customers based on patent network analysis, and suggested that the analysis used in this study are explained in the next section.

## Research Issues

Innovative business ideas grounded in the daily needs of users might enhance the software industry. In addition, it can be important to source innovative ideas from users as well as from corporate and laboratory centered R&D. The efficient commercialization of innovative ideas in the software industry possesses a low entry barrier. For the pursuit of successful commercialization, it is important to discover user-centered business ideas. Adoption of a user-centered perspective could directly help in indicating the needs of users and related trends. Many user-centered innovations are likely to be developed and commercialized through crowdfunding because crowdfunding initiatives indicate unrevealed interests in new areas and markets,. In addition, each region might possess a different environment for discovering and implementing business ideas (Crescenzi et al., 2012). Mindful of this, this paper also examines whether crowd funded innovation vary between regions.

This study focuses on the design thinking approach in order to discover and combine innovative business ideas for the software industry. According to Liedtka (2015), design thinking can be applied to user-centered ideas and their prototyping. Design thinking involves three phases (Liedtka, 2015). The initial step involves an exploratory analysis of the data gathered to identify users’ needs. The second step involves problem definition and idea generation. The third step involves prototyping and testing. This study applies design thinking to the data gathered from crowdfunding platforms.

# ACCEPTED MANUSCRIPT

## 3. Methodology

This paper particularly uses topic modeling and conjoint analysis to empirically measure the implementation of design thinking in crowdfunded projects. While crowdfunded projects can indicate new business opportunities, it is difficult to explicitly discover where this has actually occurred with regard to crowdfunded projects. Therefore, we used topic modeling to discover latent topics from amongst crowdfunded projects. Whilst various topics can be identified using this ethod, not all of those topics are e emerging business ideas or preferred by the given market. Thus, we used conjoint analysis to examine he preference for each topic and propose a combination of emerging topics.

This study analyzes Kickstarter, one of the largest crowdfunding platforms in the world. Kickstarter has been analyzed in previous studies to understand the process and effects of crowdfunding (Deodhar et al., 2017; Kuppuswamy & Bayus, 2015; Mitra, & Gilbert, 2014; Siering et al., 2016). Based on data collected from the webrobots website comprising project descriptions on Kickstarter as of December 27, 2015, we specify software-related subcategories under the technology category among the 15 main categories that also include photography, video, and art. Further, we chose the projects that were successfully funded rather than those that were to sell in the software/web/app categories, and gathered a total of 595 projects. Using these projects, we propose the following research framework (Figure 1) to discover emerging software business ideas and their combinations.

![](/api/attachments/TXQURDR6/fulltext/images/0317b2ad46181ac9f9d741e1977826902610cdd47670b9e8453475b08f9dab19.jpg)  
Figure 1 Research Framework

First, the 595 descriptions of projects were analyzed using Latent Dirichlet Allocation (LDA), a widely used topic modeling technique (Antons et al., 2015; Pournarakis et al., 2017), to discover the innovative topics hidden in the project sets. Project descriptions were text-mined and converted into a document term matrix with term frequency weighting. LDA was then applied using Gibbs sampling with a tenfold cross validation. The number of topics was chosen by observing the changes in perplexity alongside the change in the number of topics. Perplexity is widely used in conducting cross validation on hold-out data to determine the proper number of topics (Hornik and Grün, 2011; Wang and Xu, 2018). As lower perplexity can indicate that the topic model has a better generalization performance (Huang et al., 2018), it follows that perplexity improves as the number of topics

increases. However, that improvement can marginally decrease, too (Blei et al., 2003). From our tenfold cross validation, we focused on the point where perplexity was located at the inflection of decrease to increase. This paper also considered the number of topics to be ‘correct’ where perplexity was at the inflection point of decrease to increase. .

Thereafter, and in order to build the conceptual design for a new user-centered innovation in software, we conducted conjoint analysis with the topics, which are regarded as attributes. The occurrence or non-occurrence status of those topics are utilized as levels of attributes. We categorized the topic probabilities as “Occurred” and “Non-Occurred” based on the 50% percentile. For each “Occurred.” If not, it was classified as “Non-Occurred.” Our study, therefore, modified the regular method of handling profiles in conjoint analysis. While the profiles are usually generated by designing experiments in conjoint analysis, we took a retrospective approach by utilizing the given data and estimating the part-worth of occurrence or non-occurrence for each topic. The profiles in this study consist of a combination of topic occurrences in each of the crowdfunded projects. In particular, the part-worth model was deployed, and we followed the mode of interpretation used in conjoint analysis.

Each project possessed a gap between its willingness to sell and the amount raised from the crowd. This study considered the gap between the willingness to sell and the amount of funding received as a measure of how people value a project. This gap can be regarded as the value of the project. During a designated period, a crowd freely invests in a project that is of interest. Once the funded amounts exceed the funding goal designated for the project, it progresses into the commercialization phase. It is assumed that a project that exceeds the funding goal can be considered as a valuable project based on crowd intelligence. There are many factors that can be associated with such investments. The description of ideas can an important element in crowdfunding. The ideas are explained in detail and may also be accompanied by a critical summary. This paper obtained business ideas from these descriptions.

Each project can be regarded as comprising a mixture of various topics. The value of each project is considered as a dependent variable. The log of each project’s value was then utilized as the

# ACCEPTED MANUSCRIPT

preference for conjoint analysis. In this study, there are no multiple responses for each profile. Therefore, each project is considered to be a profile, and whether each topic occurred or not is regarded as the level of attribute for the conjoint analysis. As the part-worth model requires categorical attributes, the probabilities of discovered topics need to be converted into categorical variables to be considered as attributes in the analysis.

Conjoint analysis in this paper corresponds to the perspective of design thinking. To analyze the preference from the perspective of a given user’s needs, the design of conjoint analysis is different from normal conjoint analysis. Each profile cannot, as would be expected in conjoint analysis normal settings, experimentally designed profiles and balanced responses. Instead, we adapted the method with text mining and topic modeling to pursue the design thinking approach.

Using the results of conjoint analysis, the discovered topic as significant attributes and their part-worths were derived. These results represent how the crowd values each topic. We experimentally suggested the conceptual design of user-centered innovation based on the results. The most probable terms assigned for discovered topics were combined to explain the conceptual design of user-centered innovation. The possible scenarios of user-centered innovation were suggested based upon a combination of terms. The approach of combining existing technologies can be utilized in innovation (Mukherjee et al., 2016). Finally, we conducted a region-wise analysis since software industries are deployed differently across various countries. It was expected that region-specific business ideas can be derived and that these ideas and their combinations can be user-centered in each region. From the perspective of decision support, the proposed method provided the results. We interpreted and exploited those results. Topic extraction and scenarios based on topic combinations for new business ideas were studied using LDA and conjoint analysis.

## 4. Analysis and Results

Discovering Topics from Kickstarter Projects

The technology category on Kickstarter comprises 15 subcategories, including Hardware, Gadgets, Software, and DIY Electronics. The ratio of projects is summarized by subcategories in Table 1.

Table 1 Ratio of Each Subcategory in Technology

<table><tr><td>Category</td><td>% of projects</td><td>Category</td><td>% of projects</td></tr><tr><td>Hardware</td><td>29.77%</td><td>Robots</td><td>4.48%</td></tr><tr><td>Gadgets</td><td>11.74%</td><td>Sound</td><td>3.94%</td></tr><tr><td>Software</td><td>9.23%</td><td>Camera Equipment</td><td>3.05%</td></tr><tr><td>DIY Electronics</td><td>7.81%</td><td>Space Exploration</td><td>2.61%</td></tr><tr><td>Apps</td><td>6.72%</td><td>Flight</td><td>1.80%</td></tr><tr><td>Wearables</td><td>5.70%</td><td>Makerspaces</td><td>1.73%</td></tr><tr><td>Web</td><td>5.50%</td><td>Fabrication Tools</td><td>1.12%</td></tr><tr><td>3D Printing</td><td>4.79%</td><td></td><td></td></tr></table>

In the first phase of analysis, 595 projects were chosen from the software/web/app subcategories under the technology category. These projects exceeded the goal amount in their crowdfunding efforts. Then, we performed text mining on these 595 projects with a weight of term frequency. We also carried out topic modeling with tenfold cross validation. The results are shown in Figure 2.

![](/api/attachments/TXQURDR6/fulltext/images/030ccb11a8c59c0dc5e4631a5da202c16b75b7b7a130cc50255e52d79d0a7e92.jpg)  
Figure 2 Tenfold Cross Validation on Perplexity of Topic Model

In Figure 2, the X-axis indicates the number of topics and the Y-axis indicates the perplexity. As seen in the figure, more than half the tenfold cross validation results indicate that lowest perplexity occurs around the topic number of 50. Thus, we set the number of topics as 50 in this study. Table 2 shows the most prevalent terms for each discovered topic.

Table 2 Prevalent Terms for Each Topic

<table><tr><td>#</td><td>Prevalent Top 10 Terms*</td><td>#</td><td>Prevalent Top 10 Terms*</td></tr><tr><td>1</td><td>communiti, donat, organ, contribut, volunt, resourc, peopl, develop, project, share</td><td>26</td><td>project, support, api, django, releas, implement, github, tool, document, code</td></tr><tr><td>2</td><td>network, local, busi, peopl, servic, system, provid, communiti, free, creat</td><td>27</td><td>map, world, layer, creat, transform, paint, art, region, artwork, releas</td></tr><tr><td>3</td><td>stori, photo, pictur, life, share, memori, camera, audio, voic, famili</td><td>28</td><td>softwar, open, sourc, project, support, system, engin, linux, mac, raspberry</td></tr><tr><td>4</td><td>associ, pour, financ, convers, profil, chat, direct, public, facebook, particip</td><td>29</td><td>video, anim, effect, creat, audio, screen, qualiti, download, youtub, flexibl</td></tr><tr><td>5</td><td>phone, messag, call, send, person, text, devic, support, alert, smartphon</td><td>30</td><td>social, media, share, facebook, post, follow, connect, platform, twitter, advertis</td></tr><tr><td>6</td><td>reward, support, shirt, love, friend, hope, improv, offer, special, gift</td><td>31</td><td>peopl, start, final, amaz, good, place, decid, money, talk, invest</td></tr><tr><td>7</td><td>compani, insur, servic, qualiti, auto, industri, price, recommend, compar, california</td><td>32</td><td>imag, filter, color, face, display, mockup, real, chart, pattern, detect</td></tr><tr><td>8</td><td>job, compani, assist, career, young, employ, experi, profession, talent, develop</td><td>33</td><td>comput, program, scienc, code, lab, research, problem, interest, complex, algorithm</td></tr><tr><td>9</td><td>featur, reach, manag, free, communiti, help, love, profession, tech, achiev</td><td>34</td><td>day, dream, peopl, world, live, idea, love, life, friend, inspir</td></tr><tr><td>10</td><td>train, track, fit, run, plan, weight, bodi, program, work, strength</td><td>35</td><td>web, develop, python, applic, tutori, project, code, rubi, php, jqueri</td></tr><tr><td>11</td><td>book, read, free, author, write, publish, amazon, question, review, premium</td><td>36</td><td>product, custom, shop, servic, store, purchas, market, onlin, subscript, mobil</td></tr><tr><td>12</td><td>secur, internet, server, comput, devic, encrypt, cloud, password, privaci, protect</td><td>37</td><td>app, iphon, learn, swift, teach, watch, complet, code, program, ipad</td></tr><tr><td>13</td><td>applic, creat, mobil, content, design, build, user, idea, game, scratch</td><td>38</td><td>student, school, educ, teacher, math, colleg, tutor, curriculum, platform, activ</td></tr><tr><td>14</td><td>sound, play, content, browser, replay, onlin, back, watch, video, platform</td><td>39</td><td>space, citi, histori, transit, nyc, technolog, visitor, explor, map, smartphon</td></tr><tr><td>15</td><td>develop, product, fund, feedback, softwar, design, prototyp, magic, perform, fast</td><td>40</td><td>beta, experi, version, support, button, virtual, keyboard, mit, access, develop</td></tr><tr><td>16</td><td>learn, skill, creat, teach, program, practic, cours, onlin, content, interact</td><td>41</td><td>data, inform, databas, process, manag, direct, access, health, medic, intellig</td></tr><tr><td>17</td><td>code, web, develop, editor, html, visual, javascript, open, server, framework</td><td>42</td><td>build, access, great, show, reward, awesom, deal, love, talk, discount</td></tr><tr><td>18</td><td>member, group, share, card, event, match, friend, profil, score, interest</td><td>43</td><td>money, free, cost, pay, spend, offer, googl, calendar, hire, benefit</td></tr><tr><td>19</td><td>system, model, program, develop, financi, bank, fund, futur, visual, graph</td><td>44</td><td>dog, challeng, life, real, social, friend, problem, connect, join, experi</td></tr><tr><td>20</td><td>kid, famili, friend, parent, engag, fun, hous, mom, enjoy, ipad</td><td>45</td><td>music, artist, art, listen, song, print, fan, stream, world, radio</td></tr><tr><td>21</td><td>market, technolog, manag, campaign, client, softwar, growth, idea, launch, startup</td><td>46</td><td>event, women, sponsor, innov, support, communiti, open, compani, workshop, particip</td></tr><tr><td>22</td><td>travel, find, food, item, inform, grow, search, guid, restaur, experi</td><td>47</td><td>app, develop, android, mobil, store, complet, iphon, market, tablet, bluetooth</td></tr><tr><td>23</td><td>build, blog, web, fund, wordpress, plan, theme, servic, design, ensur</td><td>48</td><td>game, play, creat, develop, experi, interact, world, virtual, realiti, mobil</td></tr><tr><td>24</td><td>word, languag, translat, english, learn, peopl, phrase, find, spanish, French</td><td>49</td><td>user, platform, interfac, devic, control, support, client, chat, speed, profil</td></tr><tr><td>25</td><td>design, work, team, creat, product, collabor, creativ, tv, robot, produc</td><td>50</td><td>project, write, idea, vote, plan, updat, success, progress, encourage, screenshot</td></tr></table>

\* Stemmed, general terms are eliminated

Table 2 shows that there is a wide range of software topics covered by crowdfunded software projects. We interpreted the meaning of each topic based on the representative top ten terms. For example, Topic 3 represents the software used to share family memories from camera and audio devices, whereas Topic 34 represents software for day-dreamers who love life, friends, and the world. Topics 8 and 46 represent social applications, wherein the goal is to support community activity for women and enable career management for young people, respectively. Topics 26 and 28 suggest software development-related issues, such as supporting a Django (Python) platform for the implementation of GitHub documentation tools and supporting an open-source project for raspberrypi. Topic 16 focuses on an interactive online learning program, and Topic 41 explains intelligent data management for healthcare.

Having undertaken this step we thereafter, for purposes of analytical clarity, summarized the crowdfunded projects by region. In the software industry, there are differences in the number, and support for, crowdfunded projects between countries. The US leads the industry, while other countries have made huge efforts to gain competitive advantage, and new business ideas are deployed in different areas. In order to examine how differently the business ideas occur based on regional characteristics, we first compared the number of crowdfunded projects in the US with those in other countries, (as

Table 3 Regional Distribution of Projects in Software

<table><tr><td colspan="4">States in the U.S. (473 projects)</td><td colspan="2">Other Countries (122 projects)</td></tr><tr><td>State</td><td>Counts*</td><td>State</td><td>Counts*</td><td>Country</td><td>Counts*</td></tr><tr><td>CA</td><td>101</td><td>WI</td><td>5</td><td>UK</td><td>48</td></tr><tr><td>NY</td><td>79</td><td>MO</td><td>4</td><td>Canada</td><td>19</td></tr><tr><td>TX</td><td>26</td><td>HI</td><td>3</td><td>France</td><td>12</td></tr><tr><td>IL</td><td>25</td><td>MI</td><td>3</td><td>Germany</td><td>10</td></tr><tr><td>MA</td><td>24</td><td>OK</td><td>3</td><td>Netherlands</td><td>9</td></tr><tr><td>FL</td><td>21</td><td>KY</td><td>2</td><td>Switzerland</td><td>4</td></tr><tr><td>OR</td><td>19</td><td>LA</td><td>2</td><td>Japan</td><td>2</td></tr><tr><td>MD</td><td>12</td><td>NH</td><td>2</td><td>Kenya</td><td>2</td></tr><tr><td>UT</td><td>12</td><td>NZ</td><td>2</td><td>Mexico</td><td>2</td></tr><tr><td>CO</td><td>11</td><td>RI</td><td>2</td><td>Argentina</td><td>1</td></tr><tr><td>AU</td><td>10</td><td>CT</td><td>1</td><td>Cambodia</td><td>1</td></tr><tr><td>AZ</td><td>10</td><td>DE</td><td>1</td><td>Indonesia</td><td>1</td></tr><tr><td>DC</td><td>10</td><td>IA</td><td>1</td><td>Ireland</td><td>1</td></tr><tr><td>MN</td><td>10</td><td>ID</td><td>1</td><td>Israel</td><td>1</td></tr><tr><td>OH</td><td>9</td><td>KS</td><td>1</td><td>Italy</td><td>1</td></tr><tr><td>VA</td><td>9</td><td>ME</td><td>1</td><td>Jordan</td><td>1</td></tr><tr><td>IN</td><td>8</td><td>NV</td><td>1</td><td>Nepal</td><td>1</td></tr><tr><td>NC</td><td>8</td><td>SC</td><td>1</td><td>Romania</td><td>1</td></tr><tr><td>NJ</td><td>7</td><td>SD</td><td>1</td><td>Russia</td><td>1</td></tr><tr><td>WA</td><td>7</td><td>-</td><td>-</td><td>Korea</td><td>1</td></tr><tr><td>GA</td><td>6</td><td>-</td><td>-</td><td>Spain</td><td>1</td></tr><tr><td>PA</td><td>6</td><td>-</td><td>-</td><td>Tanzania</td><td>1</td></tr><tr><td>TN</td><td>6</td><td>-</td><td>-</td><td>Trinidad and Tobago</td><td>1</td></tr><tr><td colspan="6">* Number of projects</td></tr></table>

Table 3 shows the regional distribution of projects in software. It may be observed that there were 473 projects in the US, and 122 projects in other countries. In the US, most of the innovative ideas were proposed in California and New York. Beyond these two states, projects were only moderately distributed across the other states. Amongst other countries, the United Kingdom has the largest number of projects in software-related areas. Asian countries do not rank highly with regard to crowdfunded software business ideas, despite their presence in the ICT industry. Such notable difference between different regions of the globe may imply that the generation of business ideas varies by regions. This semi-hypothesis is continuously, and vigorously, examined in the following section.

## Conjoint Analysis

Based on the findings of topic modeling, we applied conjoint analysis to the categorized topic probabilities of 595 projects. Table 4 presents the results.

Table 4. Results of Conjoint Analysis

<table><tr><td>Variable</td><td>Estimate</td><td>Std. error</td><td>t value</td><td>p-value</td><td>Variable</td><td>Estimate</td><td>Std. error</td><td>t value</td><td>p-value</td></tr><tr><td>Topic1</td><td>0.048</td><td>0.094</td><td>0.507</td><td>0.612</td><td>Topic26</td><td>-0.125</td><td>0.097</td><td>-1.284</td><td>0.2</td></tr><tr><td>Topic2</td><td>0.112</td><td>0.095</td><td>1.17</td><td>0.243</td><td>Topic27</td><td>0.025</td><td>0.097</td><td>0.26</td><td>0.795</td></tr><tr><td>Topic3</td><td>0.071</td><td>0.095</td><td>0.748</td><td>0.455</td><td>Topic28</td><td>-0.065</td><td>0.098</td><td>-0.656</td><td>0.512</td></tr><tr><td>Topic4</td><td>0.124</td><td>0.119</td><td>1.038</td><td>0.3</td><td>Topic29</td><td>-0.121</td><td>0.095</td><td>-1.268</td><td>0.205</td></tr><tr><td>Topic5</td><td>0.162</td><td>0.093</td><td>1.734</td><td>0.083 *</td><td>Topic30</td><td>0.027</td><td>0.096</td><td>0.284</td><td>0.777</td></tr><tr><td>Topic6</td><td>-0.157</td><td>0.094</td><td>-1.661</td><td>0.097 *</td><td>Topic31</td><td>-0.182</td><td>0.097</td><td>-1.876</td><td>0.061 *</td></tr><tr><td>Topic7</td><td>-0.116</td><td>0.098</td><td>-1.192</td><td>0.234</td><td>Topic32</td><td>-0.104</td><td>0.098</td><td>-1.061</td><td>0.289</td></tr><tr><td>Topic8</td><td>-0.131</td><td>0.097</td><td>-1.353</td><td>0.177</td><td>Topic33</td><td>-0.145</td><td>0.097</td><td>-1.499</td><td>0.134</td></tr><tr><td>Topic9</td><td>-0.315</td><td>0.093</td><td>-3.381</td><td>&lt;0.001 *</td><td>Topic34</td><td>0.1</td><td>0.097</td><td>1.034</td><td>0.302</td></tr><tr><td>Topic10</td><td>-0.031</td><td>0.097</td><td>-0.318</td><td>0.751</td><td>Topic35</td><td>-0.269</td><td>0.102</td><td>-2.63</td><td>0.009 *</td></tr><tr><td>Topic11</td><td>-0.106</td><td>0.097</td><td>-1.094</td><td>0.275</td><td>Topic36</td><td>-0.067</td><td>0.094</td><td>-0.713</td><td>0.476</td></tr><tr><td>Topic12</td><td>-0.032</td><td>0.097</td><td>-0.33</td><td>0.741</td><td>Topic37</td><td>-0.011</td><td>0.099</td><td>-0.115</td><td>0.909</td></tr><tr><td>Topic13</td><td>-0.022</td><td>0.094</td><td>-0.24</td><td>0.811</td><td>Topic38</td><td>0.265</td><td>0.102</td><td>2.588</td><td>0.01 *</td></tr><tr><td>Topic14</td><td>0.019</td><td>0.096</td><td>0.199</td><td>0.842</td><td>Topic39</td><td>-0.043</td><td>0.102</td><td>-0.417</td><td>0.676</td></tr><tr><td>Topic15</td><td>-0.09</td><td>0.095</td><td>-0.948</td><td>0.344</td><td>Topic40</td><td>-0.131</td><td>0.095</td><td>-1.384</td><td>0.167</td></tr><tr><td>Topic16</td><td>-0.107</td><td>0.099</td><td>-1.079</td><td>0.281</td><td>Topic41</td><td>-0.024</td><td>0.095</td><td>-0.257</td><td>0.797</td></tr><tr><td>Topic17</td><td>-0.314</td><td>0.1</td><td>-3.142</td><td>0.002 *</td><td>Topic42</td><td>-0.355</td><td>0.096</td><td>-3.687</td><td>&lt;0.001 *</td></tr><tr><td>Topic18</td><td>0.122</td><td>0.095</td><td>1.286</td><td>0.199</td><td>Topic43</td><td>0.174</td><td>0.094</td><td>1.84</td><td>0.066 *</td></tr><tr><td>Topic19</td><td>-0.048</td><td>0.096</td><td>-0.494</td><td>0.621</td><td>Topic44</td><td>-0.07</td><td>0.095</td><td>-0.74</td><td>0.46</td></tr><tr><td>Topic20</td><td>0.036</td><td>0.097</td><td>0.367</td><td>0.714</td><td>Topic45</td><td>0.135</td><td>0.101</td><td>1.337</td><td>0.182</td></tr><tr><td>Topic21</td><td>-0.009</td><td>0.096</td><td>-0.093</td><td>0.926</td><td>Topic46</td><td>-0.085</td><td>0.097</td><td>-0.878</td><td>0.381</td></tr><tr><td>Topic22</td><td>0.114</td><td>0.098</td><td>1.169</td><td>0.243</td><td>Topic47</td><td>-0.033</td><td>0.098</td><td>-0.342</td><td>0.732</td></tr><tr><td>Topic23</td><td>0.084</td><td>0.096</td><td>0.879</td><td>0.38</td><td>Topic48</td><td>-0.23</td><td>0.097</td><td>-2.362</td><td>0.019 *</td></tr><tr><td>Topic24</td><td>0.07</td><td>0.096</td><td>0.728</td><td>0.467</td><td>Topic49</td><td>-0.149</td><td>0.093</td><td>-1.591</td><td>0.112</td></tr><tr><td>Topic25</td><td>-0.195</td><td>0.096</td><td>-2.043</td><td>0.042 *</td><td>Topic50</td><td>-0.207</td><td>0.095</td><td>-2.182</td><td>0.03 *</td></tr></table>

\*significant at 10%

The findings suggest that there were 11 significant topics among 50 discovered topics, and that 3 possessed positive coefficients.

![](/api/attachments/TXQURDR6/fulltext/images/6c15bb62148e59babd9057982ef7bb854d117661578361f426127c152f797b78.jpg)  
Figure 3. Average Importance of Each Topic

Figure 3 presents a comparative analysis of all the topics based on their average importance. It demonstrates that Topics 42, 9, 17, 38, and 35 had the highest importance. We focused on the significant topics with positive coefficients to design the software conceptually. Table 4 shows that

![](/api/attachments/TXQURDR6/fulltext/images/2eef54e5199b060b555f0453cc835c74cc7ae70abc48e95234347a58717c2a59.jpg)

topics 5, 38, and 43 possessed significantly positive factors in developing crowdfunded software. Topic 5 was about a smartphone program which gives people alerts. Topic 38 represented a tutoring platform for mathematics, and Topic 43 pertained to job information using Google Calendar. The preferences for each attribute are represented in Figure 4 through visualizing the part-worth for each topic.

<table><tr><td>Topic 5</td><td>Topic 38</td></tr><tr><td></td><td><img src="/api/attachments/TXQURDR6/fulltext/images/db886fdcb7f6e26d3b9254efa2e3be3747213dd6513f29473636b996ba7b7d27.jpg"/></td></tr><tr><td>Topic 43</td><td></td></tr><tr><td></td><td></td></tr></table>

Figure 4. Part-worth of Levels of Significant Attributes

The left hand side of each figure indicates the part-worth for topic occurrence, and the right hand side shows the part-worth for topic non-occurrence. Figure 4 shows that Topic 38 has a larger part-worth than topics 5 and 43.

## Conjoint Analysis by Region

In spite of the online platform, the crowdfunded projects were varied by region. About 80% of the projects were associated with the US, and about 20% are from other countries. In the US, most innovations took place in California and New York. This implies that there are regional differences when it comes to user-centered innovation. To consider regional differences further, this study performed a conjoint analysis for the US and other regions. Interestingly, the results show that the different topics can also be discovered by region. This may indicate that business ideas on the crowdfunding platform are associated with regional characteristics. Table 5 shows the result of the conjoint analysis for projects in the US. The table and results demonstrate that topics 4, 5, 38, and 45 are significant and positive, and that topics 4 and 45 were newly discovered in the US.

Table 5. Results of Conjoint Analysis in the US.

<table><tr><td>Variable</td><td>Estimate</td><td>Std. error</td><td>t value</td><td>p-value</td><td>Variable</td><td>Estimate</td><td>Std. error</td><td>t value</td><td>p-value</td></tr><tr><td>Topic1</td><td>0.027</td><td>0.103</td><td>0.264</td><td>0.792</td><td>Topic26</td><td>-0.12</td><td>0.105</td><td>-1.139</td><td>0.255</td></tr><tr><td>Topic2</td><td>0.114</td><td>0.102</td><td>1.111</td><td>0.267</td><td>Topic27</td><td>0.096</td><td>0.106</td><td>0.904</td><td>0.367</td></tr><tr><td>Topic3</td><td>0.024</td><td>0.104</td><td>0.231</td><td>0.818</td><td>Topic28</td><td>-0.043</td><td>0.108</td><td>-0.396</td><td>0.692</td></tr><tr><td>Topic4</td><td>0.241</td><td>0.134</td><td>1.798</td><td>0.073 *</td><td>Topic29</td><td>-0.163</td><td>0.103</td><td>-1.572</td><td>0.117</td></tr><tr><td>Topic5</td><td>0.182</td><td>0.101</td><td>1.797</td><td>0.073 *</td><td>Topic30</td><td>0.071</td><td>0.104</td><td>0.686</td><td>0.493</td></tr><tr><td>Topic6</td><td>-0.279</td><td>0.102</td><td>-2.744</td><td>0.006</td><td>Topic31</td><td>-0.112</td><td>0.105</td><td>-1.068</td><td>0.286</td></tr><tr><td>Topic7</td><td>-0.014</td><td>0.108</td><td>-0.131</td><td>0.896</td><td>Topic32</td><td>-0.056</td><td>0.108</td><td>-0.52</td><td>0.603</td></tr><tr><td>Topic8</td><td>-0.086</td><td>0.105</td><td>-0.815</td><td>0.416</td><td>Topic33</td><td>-0.089</td><td>0.106</td><td>-0.84</td><td>0.401</td></tr><tr><td>Topic9</td><td>-0.4</td><td>0.103</td><td>-3.892</td><td>&lt; 0.001 *</td><td>Topic34</td><td>0.04</td><td>0.106</td><td>0.38</td><td>0.704</td></tr><tr><td>Topic10</td><td>0.012</td><td>0.106</td><td>0.116</td><td>0.907</td><td>Topic35</td><td>-0.254</td><td>0.112</td><td>-2.265</td><td>0.024 *</td></tr><tr><td>Topic11</td><td>-0.108</td><td>0.107</td><td>-1.007</td><td>0.315</td><td>Topic36</td><td>0.011</td><td>0.103</td><td>0.107</td><td>0.915</td></tr><tr><td>Topic12</td><td>-0.145</td><td>0.104</td><td>-1.393</td><td>0.164</td><td>Topic37</td><td>0.008</td><td>0.109</td><td>0.075</td><td>0.94</td></tr><tr><td>Topic13</td><td>-0.004</td><td>0.103</td><td>-0.035</td><td>0.972</td><td>Topic38</td><td>0.243</td><td>0.112</td><td>2.178</td><td>0.03 *</td></tr><tr><td>Topic14</td><td>0.09</td><td>0.106</td><td>0.851</td><td>0.395</td><td>Topic39</td><td>-0.083</td><td>0.113</td><td>-0.739</td><td>0.46</td></tr><tr><td>Topic15</td><td>-0.153</td><td>0.103</td><td>-1.488</td><td>0.137</td><td>Topic40</td><td>0.004</td><td>0.106</td><td>0.035</td><td>0.972</td></tr><tr><td>Topic16</td><td>-0.002</td><td>0.108</td><td>-0.015</td><td>0.988</td><td>Topic41</td><td>-0.043</td><td>0.103</td><td>-0.414</td><td>0.679</td></tr><tr><td>Topic17</td><td>-0.339</td><td>0.109</td><td>-3.101</td><td>0.002 *</td><td>Topic42</td><td>-0.429</td><td>0.105</td><td>-4.099</td><td>&lt; 0.001 *</td></tr><tr><td>Topic18</td><td>0.153</td><td>0.104</td><td>1.471</td><td>0.142</td><td>Topic43</td><td>0.162</td><td>0.103</td><td>1.571</td><td>0.117</td></tr><tr><td>Topic19</td><td>-0.113</td><td>0.105</td><td>-1.077</td><td>0.282</td><td>Topic44</td><td>-0.047</td><td>0.103</td><td>-0.459</td><td>0.646</td></tr><tr><td>Topic20</td><td>0.035</td><td>0.106</td><td>0.334</td><td>0.738</td><td>Topic45</td><td>0.204</td><td>0.111</td><td>1.83</td><td>0.068</td></tr><tr><td>Topic21</td><td>0.035</td><td>0.106</td><td>0.334</td><td>0.739</td><td>Topic46</td><td>-0.067</td><td>0.108</td><td>-0.624</td><td>0.533</td></tr><tr><td>Topic22</td><td>0.149</td><td>0.108</td><td>1.375</td><td>0.17</td><td>Topic47</td><td>0.034</td><td>0.108</td><td>0.315</td><td>0.753</td></tr><tr><td>Topic23</td><td>0.065</td><td>0.106</td><td>0.617</td><td>0.537</td><td>Topic48</td><td>-0.286</td><td>0.106</td><td>-2.697</td><td>0.007 *</td></tr><tr><td>Topic24</td><td>0.122</td><td>0.106</td><td>1.152</td><td>0.25</td><td>Topic49</td><td>-0.115</td><td>0.102</td><td>-1.124</td><td>0.262</td></tr><tr><td>Topic25</td><td>-0.139</td><td>0.105</td><td>-1.317</td><td>0.189</td><td>Topic50</td><td>-0.11</td><td>0.105</td><td>-1.052</td><td>0.293</td></tr></table>

To understand how this finding could be affected by region, conjoint analysis was also conducted on projects from other countries. The results are shown in Table 6, and it indicates that topics 12, 15, and 48 were significant and positive.

Table 6. Results of Conjoint Analysis in other Countries

<table><tr><td>Variable</td><td>Estimate</td><td>Std. error</td><td>t value</td><td>p-value</td><td>Variable</td><td>Estimate</td><td>Std. error</td><td>t value</td><td>p-value</td></tr><tr><td>Topic1</td><td>-0.37</td><td>0.224</td><td>-1.648</td><td>0.104</td><td>Topic26</td><td>-0.201</td><td>0.245</td><td>-0.822</td><td>0.414</td></tr><tr><td>Topic2</td><td>0.355</td><td>0.251</td><td>1.414</td><td>0.162</td><td>Topic27</td><td>-0.654</td><td>0.259</td><td>-2.524</td><td>0.014 *</td></tr><tr><td>Topic3</td><td>0.158</td><td>0.242</td><td>0.655</td><td>0.515</td><td>Topic28</td><td>0.16</td><td>0.228</td><td>0.703</td><td>0.485</td></tr><tr><td>Topic4</td><td>0.074</td><td>0.268</td><td>0.276</td><td>0.784</td><td>Topic29</td><td>-0.007</td><td>0.21</td><td>-0.034</td><td>0.973</td></tr><tr><td>Topic5</td><td>-0.026</td><td>0.23</td><td>-0.112</td><td>0.911</td><td>Topic30</td><td>0.152</td><td>0.249</td><td>0.612</td><td>0.543</td></tr><tr><td>Topic6</td><td>0.296</td><td>0.237</td><td>1.249</td><td>0.217</td><td>Topic31</td><td>-0.126</td><td>0.26</td><td>-0.484</td><td>0.63</td></tr><tr><td>Topic7</td><td>-0.711</td><td>0.256</td><td>-2.778</td><td>0.007 *</td><td>Topic32</td><td>-0.089</td><td>0.245</td><td>-0.364</td><td>0.717</td></tr><tr><td>Topic8</td><td>-0.038</td><td>0.252</td><td>-0.152</td><td>0.88</td><td>Topic33</td><td>-0.714</td><td>0.241</td><td>-2.967</td><td>0.004 *</td></tr><tr><td>Topic9</td><td>-0.251</td><td>0.234</td><td>-1.076</td><td>0.286</td><td>Topic34</td><td>0.252</td><td>0.218</td><td>1.154</td><td>0.253</td></tr><tr><td>Topic10</td><td>0.139</td><td>0.257</td><td>0.539</td><td>0.592</td><td>Topic35</td><td>-0.009</td><td>0.26</td><td>-0.036</td><td>0.972</td></tr><tr><td>Topic11</td><td>0.273</td><td>0.212</td><td>1.29</td><td>0.202</td><td>Topic36</td><td>-0.197</td><td>0.224</td><td>-0.878</td><td>0.384</td></tr><tr><td>Topic12</td><td>0.457</td><td>0.249</td><td>1.833</td><td>0.072 *</td><td>Topic37</td><td>-0.176</td><td>0.257</td><td>-0.685</td><td>0.496</td></tr><tr><td>Topic13</td><td>-0.471</td><td>0.215</td><td>-2.186</td><td>0.033 *</td><td>Topic38</td><td>0.256</td><td>0.247</td><td>1.035</td><td>0.305</td></tr><tr><td>Topic14</td><td>0.107</td><td>0.214</td><td>0.499</td><td>0.619</td><td>Topic39</td><td>0.193</td><td>0.252</td><td>0.767</td><td>0.446</td></tr><tr><td>Topic15</td><td>0.407</td><td>0.226</td><td>1.801</td><td>0.077 *</td><td>Topic40</td><td>-0.472</td><td>0.201</td><td>-2.345</td><td>0.022 *</td></tr><tr><td>Topic16</td><td>-0.257</td><td>0.246</td><td>-1.043</td><td>0.301</td><td>Topic41</td><td>-0.25</td><td>0.207</td><td>-1.209</td><td>0.231</td></tr><tr><td>Topic17</td><td>0.092</td><td>0.238</td><td>0.386</td><td>0.701</td><td>Topic42</td><td>-0.487</td><td>0.244</td><td>-1.998</td><td>&lt; 0.001 *</td></tr><tr><td>Topic18</td><td>-0.125</td><td>0.222</td><td>-0.561</td><td>0.577</td><td>Topic43</td><td>0.382</td><td>0.239</td><td>1.599</td><td>0.115</td></tr><tr><td>Topic19</td><td>0.044</td><td>0.219</td><td>0.201</td><td>0.842</td><td>Topic44</td><td>-0.754</td><td>0.252</td><td>-2.996</td><td>0.004 *</td></tr><tr><td>Topic20</td><td>-0.177</td><td>0.241</td><td>-0.735</td><td>0.465</td><td>Topic45</td><td>-0.321</td><td>0.23</td><td>-1.393</td><td>0.169</td></tr><tr><td>Topic21</td><td>-0.105</td><td>0.237</td><td>-0.444</td><td>0.658</td><td>Topic46</td><td>-0.279</td><td>0.227</td><td>-1.233</td><td>0.222</td></tr><tr><td>Topic22</td><td>-0.047</td><td>0.242</td><td>-0.196</td><td>0.845</td><td>Topic47</td><td>-0.3</td><td>0.228</td><td>-1.315</td><td>0.193</td></tr><tr><td>Topic23</td><td>-0.113</td><td>0.234</td><td>-0.484</td><td>0.63</td><td>Topic48</td><td>0.451</td><td>0.228</td><td>1.976</td><td>0.053 *</td></tr><tr><td>Topic24</td><td>-0.027</td><td>0.214</td><td>-0.125</td><td>0.901</td><td>Topic49</td><td>-0.34</td><td>0.222</td><td>-1.527</td><td>0.132</td></tr><tr><td>Topic25</td><td>-0.85</td><td>0.234</td><td>-3.625</td><td>0.001 *</td><td>Topic50</td><td>-0.71</td><td>0.225</td><td>-3.16</td><td>0.002 *</td></tr></table>

\*significant at 10%

These findings on the discovered topics in other countries are completely different from those that we unveiled with regard to the US and suggest, therefore, that there are significant regional variations.

In Table 7 we present, a summary of the newly discovered topics with their 10 most probable terms. The discovered business ideas and their combinations appeared different by country. Such findings could contribute to identifying region-wide user-centered needs. The difference by region may be a result of different regional innovation environments. Different regions generate different ideas. This can be explained by the existence of different regional characteristics. In the US, the software industry is expanding and influencing other industries, such as education, communication, and music. In other countries, the focus has remained on specific areas, for example, internet security, software development, and gaming with virtual reality.

Table 7. Discovered Topics in the U.S. and other Countries

<table><tr><td colspan="2">Hot Topics from Projects in the U.S.</td><td colspan="2">Hot Topics from Projects in other Countries</td></tr><tr><td>Topic</td><td>Prevalent Top 10 Terms*</td><td>Topic</td><td>Prevalent Top 10 Terms*</td></tr><tr><td>4</td><td>associ, pour, financ, convers, profil, chat, direct, public, facebook, particip</td><td>12</td><td>secur, internet, server, comput, devic, encrypt, cloud, password, privaci, protect</td></tr><tr><td>5</td><td>phone, messag, call, send, person, text, devic, support, alert, smartphone</td><td>15</td><td>develop, product, fund, feedback, softwar, design, prototyp, magic, perform, fast</td></tr><tr><td>38</td><td>student, school, educ, teacher, math, colleg, tutor, curriculum, platform, active</td><td>48</td><td>game, play, creat, develop, experi, interact, world, virtual, realiti, mobil</td></tr><tr><td>45</td><td>music, artist, art, listen, song, print, fan, stream, world, radar</td><td></td><td></td></tr></table>

# ACCEPTED MANUSCRIPT

In the US, topics 4 and 45 were newly discovered and considered important; topics 5 and 38, have already been examined. Topic 4 focuses on peer-to-peer finance, and may be significant because Fintech has grown rapidly and experienced active convergence with the software industry (Lee & Sohn, 2017). Topic 45 pertains to software that enables personal curation of music and artwork, which has been an important area, too (Yoo et al., 2017). The topic can also be applied to several other areas of relevance, such as content curation and personalized service curation.

On the other hand, topics 12, 15, and 48 are newly identified in other countries. Topic 12 is about securing cloud services, which can be significant as information piracy is considered a major issue in cloud computing (Choi et al., 2017). Topic 15 is about the easy and fast development of software with funding/designing/prototyping support. It can be associated with the rapid deployment of software to satisfy customer needs (Storey et al., 2017). Topic 48 centers around virtual reality games in the mobile environment. Virtual reality is among the more popular emerging trends in software (Van Kerrebroeck et al., 2017).

## Discovering New Business Ideas in Software

In order to elaborate on the conceptual design of software, this study utilized the representative terms belonging to the discovered topics. As displayed in Table 8, we obtained 20 additional terms for each topic to further clarify the meanings of these discovered topics.

Table 8. Additional Terms per Topic

<table><tr><td>Topic</td><td>Top 10 terms* (from Table 3)</td><td>Additional top 20 terms*</td><td>Remarks</td></tr><tr><td>5</td><td>phone, messag, call, send, person, text, devic, support, alert, smartphon</td><td>locat, inform, android, communic,human, receiv, appl, mobil,meet, friend, awar,emerg, monitor, speech,situat, connect,tablet, recognit, respond,patent, gps,assist, voic, robot, search,</td><td>Entire Projects, / U.S. Projects</td></tr><tr><td>38</td><td>student, school, educ, teacher, math, colleg, tutor, curriculum, platform, active</td><td>experi, opportun, classroom, graduat, program, afford, question, instrument, subscript, sponsor, youth, goal, parent, lesson, particip, dashboard, senior, difficult, privat, answer, grant, implement, skype, studio, academ</td><td>Entire Projects, / U.S. Projects</td></tr><tr><td>43</td><td>money, free, cost, pay, spend, offer, googl, calendar, hire, benefit</td><td>expens, cover, corpor, request, budget, chang, specif, estim, care, exchang, bill, law, establish, process, respect, expand, strong, worth, search, approxim, exclus, histori, secur, subscrib, valu</td><td>Entire Projects</td></tr><tr><td>4</td><td>associ, pour, financ, convers, profil, chat, direct, public, facebook, particip</td><td>applic, internet, contribut, access, plan, open, small, twitter, aid, programm, decid, exist, locat, crowdfund, rent, role, techniqu, transact, angel, companion</td><td>U.S. Projects</td></tr><tr><td>45</td><td>music, artist, art, listen, song, print, fan, stream, world, radio</td><td>indi, favorit, band, commerci, curat, galleri, angel, direct, receiv, archiv, festiv, photographi, studio, creativ, youtub, album, artwork, instrument, comprehens</td><td>U.S. Projects</td></tr><tr><td>12</td><td>secur, internet, server, comput, devic, encrypt, cloud, password, privaci, protect</td><td>connect, onlin, access, store, data, email, privat, upload, account, log, inform, retriev, desktop, safe, usb, transfer, ident, communic, attack, sync</td><td>Non-U.S. Projects</td></tr><tr><td>15</td><td>develop, product, fund, feedback, softwar, design, prototyp, magic, perform, fast</td><td>improv, compil, result, finish, goal, depend, popular, import, easier, plan, fix, major, call, support, execut, featur, parallel, visit, bug, consult</td><td>Non-U.S. Projects</td></tr><tr><td>48</td><td>game, play, creat, develop, experi, interact, world, virtual, realiti, mobil</td><td>creation, abil, model, fund, platform, engin, physic, test, upload, unlock, attent, futur, prototyp, charact, demo, sport, support, seamless, showcas, adventur</td><td>Non-U.S. Projects</td></tr></table>

\* Stemmed, general terms are eliminated

First, we interpreted the topics using their representative terms based on the results of the LDA. Topic 5 represents a smart assistant service or a “chat bot” service which is designed especially for community activities. It deals with location information using GPS, speech/voice recognition, and robot applications. Topic 38 pertains to a mathematics tutoring platform. It provides tutoring for students of graduate programs, sponsors youth and parent participation, and enables private question and answer sessions. It utilizes Skype, an internet-based video-conferencing service. Finally, Topic 43 pertains to job information using Google Calendar. It provides a subscription-based service with strong search functionality and also complies with corporate requests.

Since user-centered innovations can be based on the needs of local users and communities, we examined how the topics of user-centered innovations are derived differently across regions. First, the topics in the US were examined. Topic 5 focuses on smart assistant whilst Topic 38 represents a

# ACCEPTED MANUSCRIPT

mathematics tutoring program. Topic 4 focuses on peer-to-peer financing, and can utilize an individual user’s social networking sites such as Twitter or Facebook. It supports an internet service, and also covers crowdfunding. Topic 45 pertains to software that personally curates music and art. This concept also contributes to the enhancement of creativity.

On the other hand, topics 12, 15, and 48 are newly identified in other countries. Topic 12 focuses on securing cloud services, for example data storage. It specifically secures private access, protects from external attacks, and syncs between desktop and cloud environments. Topic 15 focuses on enabling the easy and speedy development of software with funding/designing/prototyping support. It also improves the development environment by including compiling and debugging facilities. Remote support and visits are also included. Topic 48 pertains to a virtual reality game platform in the mobile environment and deals with seamless adventure.

Thereafter, and based on the findings of the conjoint analysis, we combined emerging business ideas for software. Table 9 shows some example scenarios.

Table 9 Example Scenarios

<table><tr><td>Regions</td><td>Concept Design Example</td><td>Relevant Terms Example</td></tr><tr><td>Global/U.S.</td><td>Smart Assistant App (or Robot) for Math Tutoring using Skype</td><td>Support, smartphon, inform, communic, human, mobil, assist, robot, math, tutor, platform, curriculum, sponsor, Skype</td></tr><tr><td>Global</td><td>Location Information based Smart Personal Assistant for Recognizing and Searching Job Offers</td><td>Support, smartphon, locat, inform, communic, mobil, situate, gps, assist, speech, recognit, respond, offer, hire, benefit, corpor, process</td></tr><tr><td>Global</td><td>Smart Platform for Tutoring Mathematics to Youth in the local community</td><td>Support, smartphone, locat, inform, communic, friend, connect, assit, math, tutor, curriculum, platform, sponsor, youth, parent, dashboard</td></tr><tr><td>Global</td><td>Mathematics Tutoring with Communicating with responding to Job Information</td><td>Support, smartphone, communic, human, mobil, situate, connect, recognit, respond, assist, math, tutor, platform, offer, hire, benefit, corpor, request, process</td></tr><tr><td>U.S.</td><td>Smart Assistant App (or Robot) for peer-to-peer finance</td><td>Support, smartphon, inform, communic, human, mobil, assist, robot, finance, chat, direct, participat, internet, applic, crowdfunding</td></tr><tr><td>U.S.</td><td>Peer-to-Peer finance based on the software of personally curating music and artwork</td><td>finance, chat, directparticipat, internet, applic, crowdfunding, curate, artwork, creativity, design, consult,</td></tr><tr><td>non U.S.</td><td>Easy and fast development of software for virtual reality game in mobile environment</td><td>develop, softwar, design, prototyp, magic, perform, fast, game, play, creat, develop, experi, interact, world, virtual, realiti, mobil</td></tr></table>

The presented scenarios reflect a combination of discovered hot topics. For example, one of the possible scenarios is a smart assistant platform for tutoring mathematics via Skype. Currently, many universities and research institutes concentrate on industrial and applied mathematics, indicating that mathematics has become an important area for academics (Neunzert, 2016). With the growing importance of mathematics in industry, learning mathematics has become associated with accessing job opportunities.

The abovementioned scenarios also suggest that there is a need for a smart personal assistant that uses GPS. The importance of spatial data is rapidly increasing, and its use in various areas is also expanding (Jee & Sohn, 2015). The suggested scenario involved the design of a smart personal assistant software that uses location information and represents a business idea that recognizes how jobs offered are dependent on the location of users. The third scenario presents a smart platform for tutoring youth mathematics. It also considers parent participation in their given local communities. In the fourth scenario, all three topics are integrated into one idea. As a result a smart platform is recommended for tutoring mathematics and automatically responding to hiring information with text recognition.

When we considered the different regions, we realized that there could be different scenarios. In the case of the US, the results suggest a need for smart assistant software for peer-to-peer financing for leading the newly generated market. Another scenario suggested focuses on peer-to-peer financing based on individually curated artwork. For other countries, a different perspective is suggested. The findings imply that the most efficient environment for the development of software is provided by a scenario which would see the launch of a virtual reality-based mobile game.

In summary, the findings show that the use of smart assistant software can accelerate both mathematics tutoring and searching for related job opportunities. Indeed, the industrial application of mathematics has become an important subject in the last few decades (Neunzert, 2016). Since firms in many industries require employees who are specialized in math, it is necessary to associate mathematics tutoring with job information. Smart services based on location information are also critical in many areas. Furthermore, the use of smart assistant technology is emerging rapidly in major global firms. Indeed, it is expected to trigger various changes across several industries. For the US, peer-to-peer financing is emerging and merging with various other domains, such as smart assistants and the personal curation of artwork. In this context, our findings contribute to the development of the innovative business ideas in software.

## 5. Discussion and Conclusion

This study extended the design thinking approach to user-centered innovations by operationalizing the proposed methodological framework in terms of underlying design thinking and estimating preferences of users. In particular, this study makes several contributions to developing business ideas by exploiting the design thinking approach in the software industry.

First, it is one of the few studies on designing new business ideas for the software industry that has combined various emerging topics pertaining to daily needs. In the process, our proposed method played an important role. Second, this study extends the open and user-centered approaches to innovation management in the software industry. This study addresses recent calls for further research on designing user-centered innovation perspectives in software. By unpacking the latent needs of the crowd, this study regards and leverages them to facilitate open innovation. Third, our study provides a comparison of inter-regional differences while applying the proposed framework to new business ideas. Based on such findings, relevant policy implications can be proposed by considering the differences among countries.

The study connects two different areas for the pursuit of innovation. One is design thinking, which has been effectively utilized for product development, and the other is user-entrepreneurship, which is emerging as a key factor in sourcing and commercializing innovative ideas. They have a common factor: the user-centered perspective. In this study, the proposed method based on

crowdfunding platforms extended both approaches. It is important to consider the crowd as an important party in the open innovation system because the crowd actively participates in selling and commercializing innovative ideas. Through so doing it brings more diversity into the open innovation system, and sourcing external technologies can be accelerated as a result.

Lastly, the proposed method can provide a meta-level design for new business ideas in software. While functionality-centered approach in software already exists, our proposed framework pursued business ideas with emerging topic convergence at the meta-level. It follows that this paper can contribute to decision making for user-centered innovation in the software industry in two ways: first, this paper can contribute to decision making pertaining to the discovery of topics that are emerging from crowdfunded innovation; second, it can contribute by suggesting ways to converge emerging business ideas for grounding a new business model.

Overall, this study demonstrates how the needs of the crowd can be substantially transformed into innovative business mechanisms. This study utilized crowdfunded innovation to propose the concept of user-centered product development. The study measured the preferences on the discovered topics in crowdfunded innovations. This can help users top understand customer needs and userdriven topics in the software industry. In addition, the measured preferences can be exploited in future studies or business design on software. Our findings support the open innovation approach and pursue the development of the software industry by exploiting newly emerging crowdfunded innovations. Furthermore, our empirical findings imply that the proposed application can be applied in other areas. Finally, this paper can connect open innovation with user-entrepreneurship to broaden their perspectives. By doing so, it eventually contributes to the development of emerging industries and economic growth for sustainable development.

However, our proposed method cannot effectively be utilized when topics are not properly discovered or if noise data exists in the software project category. In order to find topics, we utilized the perplexity metric by LDA (Hornik and Grün, 2011). This method alleviated the difficulties encountered in finding proper topics. In addition, even though there may be some noise data in the software category, those noise data could be merely associated with the discovered topics since LDA provided the topic based on terms with high occurrence probability. From the findings of this this study, it is expected that such efforts could widen the scope of the software industry. The possibility, availability, business opportunity, and potential risks of such scenarios might be elaborated and examined for the development of the software industry. In addition, this study considers software categories on Kickstarter. Even though Kickstarter has been one of the largest crowdfunding platforms in the world, it might be necessary to extend the proposed method of this study to other crowdfunding ch as the hardware industry or financial industry. These are some interesting avenues for fu ure research.

## References

Ahn, M. J.; Ju, Y. H.; Moon, T. H.; Minshall, T.; Probert, D.; Sohn, S. Y.; and Mortara, L. Beyond absorptive capacity in open innovation process: the relationships between openness, capacities and firm performance Technology Analysis & Strategic Management 28, 9 (2016), 1009-1028.

Antons, D.; Kleer, R.; and Salge, T. O. Mapping the Topic landscape of JPIM, 1984–2013: In search of hidden structures and development trajectories. Journal of Product Innovation Management 33, 6 (2015), 726- 749.

Antolín-López, R.; Céspedes-Lorente, J.; García-de-Frutos, N.; Martínez-del-Río, J.; and Pérez-Valls, M. Fostering product innovation: Differences between new ventures and established firms. Technovation, 41 (2015), 25-37.

Arora, A.; Branstetter, L. G.; and Drev, M. Going Soft: How the Rise of Software-Based Innovation Led to the Decline of Japan's IT Industry and the Resurgence of Silicon Valley. Review of Economics and Statistics 95, 3 (2013),757-775.

Agarwal, R.; and Shah, S. K. Knowledge sources of entrepreneurship: Firm formation by academic, user and employee innovators. Research Policy 43, 7 (2014), 1109-1133.

Audretsch, D.; Dohse, D.; and Niebuhr, A. Cultural diversity and entrepreneurship: a regional analysis for Germany. The Annals of Regional Science 45, 1 (2010), 55-85.

Bazjanac, V. Architectural design theory: Models of the design process. Basic Questions of Design Theory (1974). New York, 3-20 Elsevier.

Berger, B.; Matt, C.; Steininger, D. M.; and Hess, T. It is not just about competition with “free”: differences between content formats in consumer preferences and willingness to pay. Journal of Management Information Systems, 32, 3 (2015), 105-128.

Bhatt, P.; Ahmad, A. J.; and Roomi, M. A. Social innovation with open source software: User engagement and development challenges in India. Technovation, 52 (2016), 28-39.

Bogers, M.; and West, J. Managing distributed innovation: Strategic utilization of open and user innovation. Creativity and Innovation Management 21, 1 (2012), 61-75.

Boudreau, K. J. Let a thousand flowers bloom? An early look at large numbers of software app developers and patterns of innovation. Organization Science 23, 5 (2012), 1409-1427.

Branstetter, L. G.; Drev, M.; and Kwon, N. Get With the Program: Software-Driven Innovation in Traditional Manufacturing. Available at National Bureau of Economic Research No. w21752 (2015).

Brown, T. Change by design: How design thinking transforms organizations and inspires innovation (2009). New York: Harper-Collins.

Caruso, E. M.; Rahnev, D. A.; and Banaji, M. R. Using conjoint analysis to detect discrimination: revealing covert preferences from overt choices. Social Cognition 27, 1 (2009), 128-137.

Calia, R. C., Guerrini, F. M.; and Moura, G. L. Innovation networks: From technological development to business model reconfiguration. Technovation, 27, 8 (2007), 426-432.

Calic, G.; and Mosakowski, E. Kicking off social entrepreneurship: how a sustainability orientation influences crowdfunding success. Journal of Management Studies 53, 5 (2016), 738-767.

Chesbrough H. Open Innovation (2003). Harvard University Press: Cambridge, MA.

Choi, H. S.; Lee, W. S.; and Sohn, S. Y. Analyzing research trends in personal information privacy using topic modeling. Computers & Security 67 (2017), 244-253.

Cooper, R.; Juninger, S.; and T. Lockwood. Design thinking and design management: A research and practice perspective. In Design thinking: Integrating innovation, customer experience, and brand value (2009) (3rd ed.), ed. T. Lockwood, 57–64. New York: Allworth Press.

Crescenzi, R.; Rodríguez-Pose, A.; and Storper, M. The territorial dynamics of innovation in China and India. Journal of Economic Geography, 12, 5 (2012), 1055-1085

Deodhar, S. J.; Subramani, M.; and Zaheer, A. Geography of online network ties: A predictive modelling approach. Decision Support Systems, 99 (2017), 9-17.

Edison, H.; Bin Ali, N.; and Torkar, R. Towards innovation measurement in the software industry. Journal of Systems and Software 86, 5 (2013), 1390-1407.

Frenken, K.; Van Oort, F.; and Verburg, T. Related variety, unrelated variety and regional economic growth. Regional Studies 41, 5 (2007), 685-697.

Gamble, J. R.; Brennan, M.; and McAdam, R. A rewarding experience? Exploring how crowdfunding is affecting music industry business models. Journal of business research, 70 (2017), 25-36.

Garud, R.; Jain, S.; and P. Tuertscher. Designing for incompleteness; incompleteness by design. Organization Studies 29, 3 (2008), 351–371.

Green, P. E.; and Rao, V. R. Conjoint measurement for quantifying judgmental data. Journal of Marketing Research (1971), 355-363.

Grillitsch, M.; Tödtling, F.; and Höglinger, C. Variety in knowledge sourcing, geography and innovation: Evidence from the ICT sector in Austria. Papers in Regional Science 94, 1 (2015), 25-43.

Haefliger, S.; Jäger, P.; and Von Krogh, G. Under the radar: Industry entry by user entrepreneurs. Research Policy 39, 9 (2010), 1198-1213.

Hoornaert, S.; Ballings, M.; Malthouse, E. C.; and Van den Poel, D. Identifying New Product Ideas: Waiting for the Wisdom of the Crowd or Screening Ideas in Real Time. Journal of Product Innovation Management 34, 5 (2017), 580-597.

Hornik, K.; and Grün, B. topicmodels: An R package for fitting topic models. Journal of Statistical Software, 40, 13 (2011), 1-30.

Huang, A. H.; Lehavy, R.; Zang, A. Y.; and Zheng, R. Analyst information discovery and interpretation roles: A topic modeling approach. Management Science 64, 6(2017), 2473-2972

Hui, K. L.; Tam, K. Y. Software functionality: a game theoretic analysis. Journal of Management Information Systems, 19, 1 (2002), 151-184.

Jedidi, K.; and Z. J. Zhang. Augmenting conjoint analysis to estimate consumer reservation price. Management Science 48, 10 (2002), 1350–1368.

Jee, S. J.; and Sohn, S. Y. Patent network based conjoint analysis for wearable device. Technological Forecasting and Social Change, 101 (2015), 338-346.

Kim, J. 2016. The platform business model and business ecosystem: quality management and revenue structures. European Planning Studies 24 (12): 2113-2132.

Kuppuswamy, V.; and Bayus, B. L. Crowdfunding creative ideas: The dynamics of project backers in

Kickstarter. UNC Kenan-Flagler Research Paper (2015) 2013-15.

Lau, A. K.; and Lo, W. Regional innovation system, absorptive capacity and innovation performance: An empirical study. Technological Forecasting and Social Change 92 (2015), 99-114.

Li, F. The digital transformation of business models in the creative industries: A holistic framework and emerging trends. Technovation (2017), https://doi.org/10.1016/j.

Liedtka, J. Perspective: Linking design thinking with innovation outcomes through cognitive bias reduction. Journal of Product Innovation Management 32, 6 (2015), 925-938.

Li, M.; Kankanhalli, A.; and Kim, S. H. Which ideas are more likely to be implemented in online user innovation communities? An empirical analysis. Decision Support Systems, 84(2016), 28-40.

Lee, W. S.; and Sohn, S. Y. Identifying Emerging Trends of Financial Business Method Patents. Sustainability 9, 9(2017), 1670.

Luchs, M. G.; Swan, K. S.; and Creusen, M. E. Perspective: a review of marketing research on product design with directions for future research. Journal of Product Innovation Management 33, 3 (2016), 320-341.

Mitra, T.; and Gilbert, E. The language that gets people to give: Phrases that predict success on kickstarter. In Proceedings of the 17th ACM conference on Computer supported cooperative work & social computing, Baltimore, USA, 2014.

Mollick, E. The dynamics of crowdfunding: An exploratory study. Journal of Business Venturing, 29, 1 (2014), 1-16.

Moreau, C. P. Inviting the amateurs into the studio: Understanding how consumer engagement in product design creates value. Journal of Product Innovation Management 28, 3(2011), 409-410.

Moser, D. J.; and Gassmann, O. Innovating Platform Business Models: Insights from Major Tech-Companies. In ISPIM Innovation Symposium. The International Society for Professional Innovation Management (ISPIM), Melbourne, Australia, 2016.

Mukherjee, S.; Uzzi, B.; Jones, B.; and Stringer, M. A New Method for Identifying Recombinations of Existing Knowledge Associated with High‐Impact Innovation. Journal of Product Innovation Management 33, 2 (2016), 224-236.

Mulder, P.; De Groot, H. L. F.; and Hofkes, M. W. Economic growth and technological change: A comparison of insights from a neo-classical and an evolutionary perspective. Technological Forecasting and Social Change 68, 2 (2001), 151-171.

Munir, H.; Wnuk, K.; and Runeson, P. Open innovation in software engineering: a systematic mapping study. Empirical Software Engineering, 21, 2 (2016), 684-723.

Neunzert, H. Mathematics in industry. Mathematics and Society (2016), 167-183.

Noel, M.; and Schankerman, M. Strategic patenting and software innovation. The Journal of Industrial Economics 61, 3(2013), 481-520.

Pournarakis, D. E.; Sotiropoulos, D. N.; and Giaglis, G. M. A computational model for mining consumer perceptions in social media. Decision Support Systems, 93 (2017), 98-110.

Quintana-García, C.; and Benavides-Velasco, C. A. Innovative competence, exploration and exploitation: The influence of technological diversification. Research Policy 37, 3(2008), 492-507.

Radford, S. K.; and Bloch, P. H. Linking innovation to design: Consumer responses to visual product

newness. Journal of Product Innovation Management 28, s1(2011), 208-220.

Raghunathan, S. Software editions: An application of segmentation theory to the packaged software market. Journal of Management Information Systems, 17, 1 (2000), 87-113.

Scholz, M.; Dorner, V.; Franz, M.; and Hinz, O. Measuring consumers' willingness to pay with utility-based recommendation systems. Decision Support Systems, 72 (2015), 60-71.

Shah, S. K.; and Tripsas, M. The accidental entrepreneur: The emergent and collective process of user entrepreneurship. Strategic Entrepreneurship Journal 1, 1‐2 (2007), 123-140.

Siering, M.; Koch, J. A.; and Deokar, A. V. Detecting Fraudulent Behavior on Crowdfunding Platforms: The Role of Linguistic and Content-Based Cues in Static and Dynamic Contexts. Journal of Management Information Systems, 33, 2 (2016), 421-455.

Storey, M. A.; Zagalsky, A.; Figueira Filho, F.; Singer, L.; and German, D. M. How social and communication channels shape and challenge a participatory culture in software development. IEEE Transactions on Software Engineering 43, 2 (2017), 185-204.

Subramaniam, M.; and Youndt, M. A. The influence of intellectual capital on the types of innovative capabilities. Academy of Management Journal 48, 3 (2005), 450-463.

Van Kerrebroeck, H.; Brengman, M.; and Willems, K. When brands come to life: experimental research on the vividness effect of Virtual Reality in transformational marketing communications. Virtual Reality 21, 4 (2017), 177-191.

Von Hippel, E. Democratizing innovation: the evolving phenomenon of user innovation. International Journal of Innovation Science 1, 1 (2009), 29-40.

Wang, Y.; and Xu, W. Leveraging deep learning with LDA-based text analytics to detect automobile insurance fraud. Decision Support Systems, 105 (2018), 87-95.

Yoo, Y.; Ju, Y.; and Sohn, S. Y. Quantitative analysis of a half‐century of K‐Pop songs: Association rule analysis of lyrics and social network analysis of singers and composers. Journal of Popular Music Studies 29,3 (2017)

Zhang, T.; Gensler, S.; and Garcia, R. A Study of the Diffusion of Alternative Fuel Vehicles: An Agent‐Based Modeling Approach. Journal of Product Innovation Management 28, 2 (2011), 152-168.

Zott, C., Amit, R.; and Massa, L. The business model: recent developments and future research. Journal of management, 37, 4 (2011), 1019-1042.

## Biographical Note

Won Sang Lee received Ph.D. from the Department of Information and Industrial Engineering, Yonsei University. His research area is data mining and text mining. Address: uraah@yonsei.ac.kr.

So Young Sohn is a Professor of Industrial Engineering at Yonsei University in Korea. Her research areas include technology management, marketing, quality, and reliability engineering. Detailed information about her teaching and research areas can be found at http://isl.yonsei.ac.kr.
