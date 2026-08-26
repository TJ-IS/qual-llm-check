---
otero_id: 7428
otero_key: "5WTTSUGP"
title: "Determining importance degrees of website design parameters based on interactions and types of websites"
authors: "Selcuk Cebi"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.10.036"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Determining importance degrees of website design parameters based on interactions and types of websites

Selcuk Cebi ⁎

Department of Industrial Engineering, Karadeniz Technical University Trabzon, Turkey

a r t i c l e i n f o

Article history: Received 24 October 2011 Received in revised form 17 September 2012 Accepted 7 October 2012 Available online 31 October 2012

Keywords: Website design Design parameters DEMATEL Delphi TOPSIS

## a b s t r a c t

Nowadays, the internet is the most widely used and an effective tool for <sup>fi</sup>rms/organizations to reach their customers by their websites. Hence, effective design of websites helps firms/organizations to reach their aim. There are lots of design parameters that play an effective role on website design. These parameters are considered by researchers in some academic papers. However, none of the published articles takes into account both interactions among the design parameters and importance degrees of design parameters in terms of website types. Therefore, in the scope of this paper, in order to address these research gaps, an integrated multiple criteria decision making method including Delphi and DEMATEL (DEcision-MAking Trial and Evaluation Laboratory) techniques has been proposed for determining importance degrees of website design parameters. Furthermore, the website design parameters were determined based on detailed review of literature available. In addition, a new classi<sup>fi</sup>cation has been presented for websites. Finally, this paper indicates that the importance degrees of website design parameters are based on both website types and interaction among the design parameters. To illustrate the steps of the proposed algorithm, an application has been presented.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Internet, which has a wide application area, is accepted as an information data-base by websites. With the enlargement of the Internet and World Wide Web (WWW) applications, users are increasingly interfacing and interacting with web-based applications [2]. In particular, the rapid growth of the internet presents a new perspective to all aspects of business [19]. By using the internet, for instance, an organization can easily reach customers to provide them not only general information about its products or services but also the opportunity for performing interactive business transactions [2]. Therefore, an effective website design has an important role for organizations which want to maximize their pro<sup>fi</sup>ts by promoting their services or products in a competitive and limited market. To design an effective website, there are various design parameters that must be taken into consideration simultaneously. It is possible to de<sup>fi</sup>ne design parameters as qualitative and quantitative aspects of physical and functional characteristics of a website which play an important role on effectiveness of website design. However it is not easy to determine the design parameters of a good website-design because of its complex nature depending on expectations of humans [29]. Hence, website designers have to take an increasing number of design parameters such as usability, accessibility, cost, delay, quality, security, maintenance, etc. into account during design process to satisfy users' needs [9]. Therefore, the design parameters of a good website have been taken into consideration by researchers since last decade in order to increase the performance of the websites.

In the last decade, numerous papers have concentrated on the design parameters of websites. Some of them deal with the quality of the website ([6,19,31] etc.), usability of the website ([29,39,40] etc.), esthetics ([1,37,57] etc.), and website content [5,10]. These papers, published in the literature, depict that there are various design parameters to evaluate the effectiveness of websites. Furthermore, they prove that each design parameter has an impact role on website design. However, the common feature of these studies is that they consider simultaneously one or two design parameters, mentioned above during the evaluation of websites. Hence, taking all design parameters simultaneously while evaluating design aspects of a website may present an effective tool to reach perfect design. Moreover, some studies use a <sup>fi</sup>xed set of design parameters to evaluate all of the websites with different purposes or usage [6]. Furthermore, none of the proposed approaches for evaluation of websites considers the interactions among design parameters. Therefore, to cope with these shortcomings in the literature, this article addresses the concern for effective website design by means of multiple criteria decision making methods. In the scope of this paper, an integrated multiple criteria decision making model including the interactions among design parameters has been used. The main aim of this study is to present the importance of design parameters of websites based on types of websites and interactions among the design parameters. For this purpose, an integrated method has been proposed based on the method proposed by Shen et al. [41]. At the <sup>fi</sup>rst step, Delphi method is used to determine website design parameters with respect to website type. Then, decision-making trial and evaluation laboratory (DEMATEL) method is applied not only to obtain the importance of design parameters but also put to forward interactions among the determined design parameters [41,43].

The rest of this paper is organized as follows; Section 2 presents a wide literature review. In Section 3, the structure of the proposed method is given. An application of the proposed method is conducted in Section 4. Section 5 discusses the results obtained from the application. In Section 6, the degrees of interactions among design parameters are analyzed. Finally, concluding remarks are presented in Section 7.

## 2. Literature review

## 2.1. Classification of websites

On the internet, there have been various website applications which have been put out for various purposes and for wide user pro<sup>fi</sup>le. Therefore, different classi<sup>fi</sup>cations have been proposed for website categories in the literature. For instance Hoffman et al. [20] proposed a classi<sup>fi</sup>cation consisting of six categories for commercial websites. These are; i) online storefront websites which offer direct sales through an electronic channel via an electronic catalog or other, ii) internet presence sites which provide a virtual presence for a <sup>fi</sup>rm and its offerings, iii) content which is fee-based (where a provider supplies and/or pays for content while the consumer pays to access), sponsored sites (which sell advertising space), and a searchable database (where merchants or advertisers pay a provider for information placement), iv) mall sites which constitute a collection of online storefronts, v) incentive sites which represent a unique form of advertising that attract a potential customer to a site, and vi) search agent sites which identify other websites through keyword search of a database [20]. Zviran et al. [59] classi<sup>fi</sup>ed websites into <sup>fi</sup>ve categories with respect to volume of their traf<sup>fi</sup>cs. These are: i) publish/subscribe websites which provide users information such as search engines, media sites, and newspapers, ii) online shopping websites which let users browse and buy, iii) customer self-service websites which let users help themselves such as banking at home, tracking packages, and making travel arrangements, iv) trading websites which let visitors buy and sell, and v) business to business (B2B) websites which let businesses buy from and sell to each other [59]. Lee and Koubek [29] classi<sup>fi</sup>ed website into four categories due to usage purposes. These categories are: i) entertainment websites which provide diversion and relaxation to users who want to escape from the stressful reality, ii) information websites which make it possible for users to obtain useful information more quickly and more easily, iii) communication websites which facilitate communicating with others, and iv) commercial websites which provide an online market place for goods and services [29]. Hasan and Abuelrub [19] classi<sup>fi</sup>ed the websites into four categories. These are i) Business to Business (B2B), ii) Business to Consumer (B2C), iii) Consumer to Business (C2B), and iv) Consumer to Consumer (C2C).

In the literature, there are various classi<sup>fi</sup>cations for website types with respect to different purposes. However, the current classi<sup>fi</sup>cations do not include all types of websites. For instance, Hasan and Abuelrub [19] focused only commercial websites. Although, the most detail website classi<sup>fi</sup>cation has been presented by Lee and Koubek [29], it does not include mixed type of websites. For instance, some websites present a chance to gain money for their users beside they provide diversion and relaxation. Another example can be given for organization websites: their aim is to sell their product online while providing information for their product and company as well. Therefore, in the scope of this paper, we classi<sup>fi</sup>ed the websites based on both users' expectations and websites' purposes. Apart from governments' and some civil organizations' websites, the main objective of the most websites is to gain money. A website makes money in two ways; the <sup>fi</sup>rst one is the direct way to make money by selling products or services. The other is the indirect way to make money over commercial advertisements. The second option is nearly used among all types of websites. Therefore, by taking users' expectations and direct purpose of websites into account, a new classi<sup>fi</sup>cation of websites has been proposed in the scope of this paper.

In Fig. 1, websites are classi<sup>fi</sup>ed into three main groups and seven sub-groups. These are i) commercial websites including B2B, B2C, and C2C, ii) service websites including self-service websites, information websites, entertainment websites, and communication websites, and iii) mixed type websites. The main objective of the commercial websites is to make money by selling products or services. In other words, a user utilizes this type of website to purchase a product or to pay money for any service. The commercial website consists of B2B, B2C, and C2C. The main objective of B2B is to present a transaction between companies such as websites for the company and its vendors or its suppliers. The main objective of B2C is to present marketing between company and consumer such as shopping websites, transportation websites, travel agency websites, etc. The main objective of C2C is to present transaction between consumers such as bid websites. The purpose of the service websites is to present their users with various services without any cost such as information websites, entertainment websites, etc. The service websites consist of self-service websites, information websites, entertainment websites, and communication websites. The main objective of self-service websites is to present customers to access their information and perform certain operations such as internet banking websites, e-government websites etc. The main objective of information websites is to present information, advertisement or publicity such as personal websites, organization/company websites, news and magazine websites, search engines (Yahoo, Google), blogs and forms etc. The main objective of entertainment websites is to present amusement or fun such as game websites, video websites etc. The main objective of communication websites is to provide communication among people such as social network (face book, twitter) and <sup>fi</sup>le share websites. The mixed type websites present two or more purposes at the same time just in one page like a gambling website. A gambling website presents entertainment to their customers by gaining from it. Some game websites present entertainment to their customers with money. So, these websites are in mixed types.

![](/api/attachments/5WTTSUGP/fulltext/images/9f1d440aabe476a02a7a0b16cadbd77c5b1fad2cb5404910201ccdd9e1029fc6.jpg)  
Fig. 1. Classi<sup>fi</sup>cation of websites.

## 2.2. Design parameters of websites

Although the numbers of websites and internet users have been in creasing rapidly, the numbers of the academic researches which are tak ing aspects of website design into account are limited. Some of these studies are as follows; Bell and Tang [3] concentrated on following fac tors; access to the web, content, graphics, structure, user friendliness, navigation, usefulness, and unique features. Misic and Johnson [35] in vestigated speed, uniqueness of functionality, ease of navigation, coun ter, currency, wording, and color and style factors. [33] focused on accuracy, completeness, relevancy, security, reliability, customization, and interactivity, ease of use, speed, search functionality, and organization criteria. Huizingh [24] studied content and design criteria. Wan [49] divided web design attributes into four categories: information, friendliness, responsiveness, and reliability. Aladwani and Palvia [2] presented the key characteristics of a website based on users' percep tions. In their study, the website designs were evaluated with respect to three main criteria; adequacy, web content, and web appearance. Technical adequacy in their research consisted of security, ease of navi gation, broadcast services, limited use of special plug-ins, search facili ties, anonymity, availability, valid links, reliability, browser snif<sup>fi</sup>ng, personalization, speedy page loading, interactivity, ease of access, multi-language support, protected content, and bookmark facility. On the other hand, the web content criterion involved usefulness of content, completeness of content, clarity of content, uniqueness of content, broadness of content, originality of content, currency of content, conciseness of content, accuracy of content, <sup>fi</sup>nding contact information, <sup>fi</sup>nding people without delay, <sup>fi</sup>nding site maintainer, <sup>fi</sup>nding links to relevant sites, <sup>fi</sup>nding <sup>fi</sup>rm's general information, <sup>fi</sup>nding products/services de tails, <sup>fi</sup>nding customers' policies, <sup>fi</sup>nding customer support, <sup>fi</sup>nding free services, using limited registration forms, <sup>fi</sup>nding online help, diversity of content, and <sup>fi</sup>nding free information. Furthermore, web appearance criterion included attractiveness, distinctive hot buttons, changing look, organization, proper use of fonts, proper use of colors, proper use of graphics, graphics–text balance, proper use of multimedia, style con sistency, proper choice of page length, good labeling, text-only option, proper use of language/style, color consistency. González and Palacios [18] classi<sup>fi</sup>ed criteria into four categories: site content, speed, accessibil ity, and navigability. Muylle et al. [38] focused effective website design by means of the conceptualization and empirical validation of a website user satisfaction by taking into account layout, information quality, con nection quality, and language customization. Zviran et al. [59] investigat ed the performance of the user-based website design to put forward website usability on user expectations. In their study, four types of commercial website designs which are online shopping, customer self-service, trading, and publish/subscribe were analyzed in terms of content, accuracy format, ease of use, timeliness, structure, navigation, layout, performance, and searchability criteria. Akbulut and Akbulut [1] examined educational website designers' opinions about the visual elements (graph, picture, <sup>fi</sup>gure, simulation, video, etc.) on the websites. Lee and Koubek [29] considered content organization, visual organiza tion, navigation system, color, and typography as web design attributes. Djamasbi et al. [12] analyzed visual appeal of a website by using survey method and eye tracking methods. Bonnardel et al. [4] investigated preference of designers and users for home page colors of websites and analyzed the effect of the color of website on users' perceptions.

Although there are limited studies in the literature, there are a lot of criteria which have been taken into consideration. Chiou et al. [8] presented a literature review paper related to website design in order to present the trend of website evaluation approaches, to present the criteria used in the academic studies, and to propose a website evaluation model to literature. In their study, the papers published in the years between 1995 and 2006 were handled and the criteria used in the papers were classi<sup>fi</sup>ed into <sup>fi</sup>ve categories; i) Place including 25 sub-criteria, ii) Product including 6 sub-criteria, iii) Price including 4 sub-criteria, iv) Promotion including 5 sub-criteria, and v) Customer Relations including 13 sub-criteria [8]. In Table 1, the studies which are published after 2006 are taken into consideration in order to update the criteria pool proposed by Chiou et al. [8]. Then, criteria hierarchy for website design parameters obtained from literature review is given in Table 2.

In Table 1, the papers are classi<sup>fi</sup>ed into three categories; i) criteria used in the study, ii) methods which are used in the studies, iii) type of investigated websites. In particular, survey and experimental evaluation techniques are the most used methods. As well as survey and experimental evaluation techniques, a few studies have adopted multiple criteria decision making methods. In an experimental evaluation, participants are asked to accomplish a speci<sup>fi</sup>c task by following a detailed set of instructions [8]. In survey method, data are collected from participants via answering a questionnaire without any tasks. To obtain a decision for these methods, statistical analysis is applied on collected data. However, MCDM methods are based on expert evaluations and take multi-dimensional factors into consideration. Many studies evaluate websites within part of the criteria. To take the overall criteria into consideration, it is necessary to use MCDM methods [6]. Therefore, the applications of MCDM methods have been increasing recently and they differ from the studies published before 2006 as it is seen in Table 1.

In Table 2, a set of website design parameters compiled from the literature has been proposed for the evaluation of websites. In the literature, many studies use a <sup>fi</sup>xed set of criteria to evaluate all of the websites with different purposes or usage [6]. However, the importance degree of website design parameters varies according to the types of websites and thus, it is necessary to use different sets of criteria. Furthermore, there are some interactions among criteria e.g. esthetics affects usability [37,46]. None of the MCDM studies related to websites design takes interactions among criteria into consideration. Therefore, the main aim of this paper is to propose an integrated MCDM method that handles all design parameters related to website design and takes interactions among design parameters into account. Furthermore, considering both type of websites and interactions among design parameters, the importance degrees of the website design parameters are examined and obtained.

## 3. Website evaluation model

## 3.1. Delphi method

The Delphi method is a modi<sup>fi</sup>cation of brain writing and survey technique. The method was developed in the early of 1950s [26] in order to improve group decision making by seeking opinions without face-to-face interaction [41]. The technique has a wide application area such as technological forecasting, public-policy analysis, educational innovations, program planning etc. [26]. The method is de<sup>fi</sup>ned as a method of systematic solicitation and collection of group judgments on a particular topic through a set of carefully designed sequential questionnaires that are interspersed with summarized information and feedback of opinions derived from earlier responses [26,41].

## 3.2. DEMATEL method

It is the <sup>fi</sup>rst time Science and Human Affairs Program of the Battelle Memorial Institute of Geneva put forward decision-making trial and evaluation laboratory (DEMATEL) method to the literature between 1972 and 1976 in order to convert the relationship between the causes and effects of criteria into an intelligible structure [15–17].

The papers published between 2006 and 2011.

<table><tr><td rowspan="2">Author</td><td rowspan="2">Design parameters used in the study</td><td colspan="4">Method</td><td rowspan="2">Type of website</td></tr><tr><td>Empirical</td><td>Survey</td><td>MCDM</td><td>Other</td></tr><tr><td>Chiou et al. [8]</td><td>Information quality, Ease of use, Responsiveness</td><td></td><td></td><td>✓</td><td></td><td>Travel</td></tr><tr><td>Lee and Kozar [30]</td><td>Usability</td><td></td><td>✓</td><td></td><td></td><td></td></tr><tr><td>Bonnardel et al. [4]</td><td>Impact of color on users</td><td>✓</td><td></td><td></td><td></td><td></td></tr><tr><td>Tuch et al. [46]</td><td>Symmetry in terms of esthetics</td><td>✓</td><td></td><td></td><td></td><td></td></tr><tr><td>Cyretal et al. [11]</td><td>Impact of color on culturally diverse users</td><td>✓</td><td>✓</td><td></td><td></td><td></td></tr><tr><td>Yu et al. [56]</td><td>Product, design, technology, service quality, logistic companies</td><td></td><td></td><td>✓</td><td></td><td></td></tr><tr><td>Corman and Baloglu [10]</td><td>Content</td><td></td><td></td><td></td><td>✓</td><td>Medical travel</td></tr><tr><td>Liu et al. [34]</td><td>Learning materials, web usability, learners&#x27; preferences, technology integration, functionality of assisting language learning</td><td></td><td>✓</td><td></td><td></td><td>Education</td></tr><tr><td>Hasan and Abuelrub [19]</td><td>Quality of website</td><td></td><td>✓</td><td></td><td></td><td></td></tr><tr><td>Djamasbi et al. [12]</td><td>Visual appeal</td><td>✓</td><td>✓</td><td></td><td></td><td></td></tr><tr><td>Hu and Liao [21]</td><td>Electronic service quality</td><td></td><td></td><td>✓</td><td></td><td>Internet Banking</td></tr><tr><td>Yiu et al. [54]</td><td>Usefulness, ease of use,</td><td></td><td>✓</td><td></td><td></td><td>Internet Banking</td></tr><tr><td>Moshagen and Thielsch [37]</td><td>Visual esthetics of websites (simplicity, diversity, colorfulness, and craftsmanship)</td><td>✓</td><td>✓</td><td></td><td></td><td></td></tr><tr><td>Şengel and Öncü [40]</td><td>Usability of websites</td><td></td><td>✓</td><td></td><td></td><td>Education</td></tr><tr><td>Lin [31]</td><td>Quality of website</td><td></td><td></td><td>✓</td><td></td><td>Education</td></tr><tr><td>Zviran et al. [59]</td><td>Usability and user-based design</td><td>✓</td><td></td><td></td><td></td><td>Commercial</td></tr><tr><td>Huang and Huang [6]</td><td>Quality of websites</td><td></td><td></td><td>✓</td><td></td><td>Education</td></tr><tr><td>Akbulut and Akbulut [1]</td><td>Visual elements of websites</td><td>✓</td><td></td><td></td><td></td><td>Education</td></tr><tr><td>Lee and Koubek [29]</td><td>Usability</td><td>✓</td><td></td><td></td><td></td><td>Commercial</td></tr><tr><td>Caballero-Luque et al. [5]</td><td>Website content</td><td></td><td></td><td>✓</td><td></td><td>Internet Banking</td></tr><tr><td>Zeng et al. [57]</td><td>Esthetic appeal, interactivity, novelty and flexibility, affect, importance, commonality and simplicity, and personalization</td><td></td><td>✓</td><td></td><td></td><td></td></tr><tr><td>Ku and Fan [28]</td><td>Quality of websites</td><td></td><td></td><td>✓</td><td></td><td>Shopping</td></tr><tr><td>Robins and Holmes [60]</td><td>Effect of visual design and esthetics</td><td>✓</td><td></td><td></td><td></td><td></td></tr><tr><td>Pearson and Pearson [39]</td><td>Usability</td><td></td><td></td><td>✓</td><td></td><td></td></tr><tr><td>Morosan and Jeong [36]</td><td>Usability</td><td>✓</td><td></td><td></td><td></td><td>Truism</td></tr><tr><td>Éthier et al. [13]</td><td>Usability</td><td>✓</td><td></td><td></td><td></td><td>Shopping</td></tr><tr><td>Fang and Holsapple [14]</td><td>Usability</td><td>✓</td><td></td><td></td><td></td><td></td></tr><tr><td>Chevalier and Bonnardel [7]</td><td>Usability</td><td>✓</td><td></td><td></td><td></td><td></td></tr></table>

Table 2 Website design parameters.

Including indirect relations into a compromised cause and effect model is the main advantage of the DEMATEL method which is accepted as an effective procedure for analyzing structure and relationships between components of a system or a number of available alternatives [45]. The method ranks the criteria with respect to type and severity of interactions among the criteria. If any criterion is more effective than another, it is assumed as having higher priority and assigned as cause criterion. Otherwise, if the criterion receives more in<sup>fl</sup>uence from another criteria, it is assumed as having lower priority and assigned as effect criteria [45,47]. In the literature, many studies used the DEMATEL method to determine interactions among the criteria and their importance [22,23,25,32, 41,42,44,47,48,50,52,53,58].

<table><tr><td></td><td colspan="2">Main design parameters</td><td colspan="2">Sub-design parameters</td><td>Explanation</td></tr><tr><td rowspan="26">Website design parameters</td><td rowspan="4">C1</td><td rowspan="4">Usability</td><td></td><td></td><td></td></tr><tr><td> $C_{11}$ </td><td>Ease of use</td><td>The users should reach its aim in short time while using the site first time</td></tr><tr><td> $C_{12}$ </td><td>Ease of learning</td><td>The users should be adapted the site in short time</td></tr><tr><td> $C_{13}$ </td><td>Memorability</td><td>The users should remember the functions presented by the site</td></tr><tr><td rowspan="4"> $C_2$ </td><td rowspan="4">Visual aspects</td><td></td><td></td><td></td></tr><tr><td> $C_{21}$ </td><td>Layout</td><td>The site should present good visual organization</td></tr><tr><td> $C_{22}$ </td><td>Graphics</td><td>The site should present good tonality</td></tr><tr><td> $C_{23}$ </td><td>Text</td><td>The site should present readable font</td></tr><tr><td rowspan="5"> $C_3$ </td><td rowspan="5">Technical adequacy</td><td></td><td></td><td></td></tr><tr><td> $C_{31}$ </td><td>System availability</td><td>The site must be reached any time</td></tr><tr><td> $C_{32}$ </td><td>Speed</td><td>The site should provide quick loading, accessing, and using</td></tr><tr><td> $C_{33}$ </td><td>Accessibility</td><td>The site should provide easy access to materials</td></tr><tr><td> $C_{34}$ </td><td>Navigation</td><td>The site should provide easy navigation to reach services</td></tr><tr><td> $C_4$ </td><td>Content</td><td></td><td></td><td>The site should satisfy users&#x27; expectations</td></tr><tr><td rowspan="4"> $C_5$ </td><td rowspan="4">Security</td><td></td><td></td><td></td></tr><tr><td> $C_{51}$ </td><td>Reliability</td><td>The service protect users from hackers&#x27; attack while downloading a file or surfing</td></tr><tr><td> $C_{52}$ </td><td>Accuracy</td><td>The service provide correct information</td></tr><tr><td> $C_{53}$ </td><td>Privacy</td><td>The site protects users&#x27; information</td></tr><tr><td rowspan="4"> $C_6$ </td><td rowspan="4">Communication</td><td></td><td></td><td></td></tr><tr><td> $C_{61}$ </td><td>Contact info</td><td>The site should provide contact addresses and phone numbers</td></tr><tr><td> $C_{62}$ </td><td>Online help</td><td>The site should provide an assistance service through phone or internet</td></tr><tr><td> $C_{63}$ </td><td>Responsiveness</td><td>The site should handle user&#x27;s problems and return to users in a short time</td></tr><tr><td rowspan="4"> $C_7$ </td><td rowspan="4">Prestige</td><td></td><td></td><td></td></tr><tr><td> $C_{71}$ </td><td>Reputation</td><td>The site should be well known</td></tr><tr><td> $C_{72}$ </td><td>Sustainability</td><td>The site should guarantee to serve for a long time</td></tr><tr><td> $C_{73}$ </td><td>Currency</td><td>The site should provide continuous improvement</td></tr></table>

## 3.3. The framework of the integrated method

The main framework of the method used in this paper consists of the Delphi and DEMATEL methods (Fig. 2). The steps of the method can be described as follows

Step 1. Collect preferences on design parameters: The preferences of a design team consisting of experts are collected by a questionnaire on design parameters of a website. At <sup>fi</sup>rst, the requirements of the design parameters are discussed and then a binary scale $( \Upsilon \mathrm { e s } ^ { \mathrm { \ } \cdot \mathrm { \scriptscriptstyle i } } 1 ^ { \mathrm { \scriptscriptstyle i } } , \dot { \mathsf { N o } } ^ { \mathrm { \ } \cdot \mathrm { \scriptscriptstyle 4 } } 2 ^ { \mathrm { \scriptscriptstyle i } \cdot \mathrm { \scriptscriptstyle \gamma } } )$ which indicates the requirements of the design parameters with respect to related website design type is executed.

Step 2. Determine the requirements of each design parameter: Simple majority decision rule is used to determine whether a related website design parameter is required or not.

$$
\left\{ \begin{array}{l l} x P y: & \# (i: x P _ {i} y) > \# (i: y P _ {i} x), i \in Z ^ {+} \\ x R y: & \# (i: x P _ {i} y) \geq \# (i: y P _ {i} x), i \in Z ^ {+} \\ x I y: & \# (i: x P _ {i} y) = \# (i: y P _ {i} x), i \in Z ^ {+} \end{array} \right\}\tag{1}
$$

where # $( i ; x P _ { i } y )$ is the number of the individuals such that the ith individual prefers x to y. R, P, and I are the binary relation of weak simple majority, of strict simple majority, and of tie under simple majority [26].

Step 3. Obtain the importance degrees of each design parameters: In this step, the degrees of importance of design parameters with respect to website type are evaluated by website users using a questionnaire. Then, the aggregated decision matrix $( L = [ l _ { i } ] _ { n x m } )$ is obtained where n and m symbolize number of design parameters and number of website type, respectively.

Step 4. Create direct relation matrix: The design team makes a set of pairwise comparison in order to put forward interactions among criteria by using integer scale ranging [0; 4] (“No in<sup>fl</sup>uence (0),” Very Weak in<sup>fl</sup>uence (1), “Weak in<sup>fl</sup>uence $( 2 ) , "$ “Strong in<sup>fl</sup>uence (3)”, and “Extreme strong in<sup>fl</sup>uence $( 4 ) " )$ . Each member of the design team creates her direct relation matrix $M ^ { k } .$

![](/api/attachments/5WTTSUGP/fulltext/images/1028833fbc736930b8a311d3bbf777976d7f7450f808d2ec4af50bf63ea51916.jpg)  
Fig. 2. Framework of the proposed algorithm.

$$
M ^ {k} = \left[ m _ {i j} \right] _ {n \times n} \quad k = 1, 2, 3, \dots , K\tag{2}
$$

where $m _ { i j }$ is the preference of kth expert for ith criterion to jth criterion. The higher score indicates that the respondent has expressed that the insuf<sup>fi</sup>cient involvement in problem of design parameter i exerts stronger possible direct in<sup>fl</sup>uence on the inability of design parameter j. In other words, the higher score, in positive terms, indicates that greater improvement i is required to improve j. [61]. Direct relation matrix is obtained by using following equation;

$$
M = \frac {1}{K} \times \sum_ {k = 1} ^ {K} M ^ {k}\tag{3}
$$

where $K$ is the number of experts.

Step 5. Normalize the direct-relation matrix: The normalized directrelation matrix Z is obtained by [45,50,51]

$$
Z = \min _ {i, j} \left[ \frac {1}{\max _ {1 \leq i \leq n} \sum_ {j = 1} ^ {n} m _ {i j}}, \frac {1}{\max _ {1 \leq j \leq n} \sum_ {i = 1} ^ {n} m _ {i j}} \right] \times M.\tag{4}
$$

Step 6. Obtain the total relation matrix: The total relation matrix T is calculated by the following formula

$$
T = Z \times (I - Z) ^ {- 1}\tag{5}
$$

where I is identity matrix [45,50,51].

Step 7. Obtain R and C matrix: R and C are n×1 and 1×n vectors representing the sum of rows and sum of columns of the total relation matrix $T ,$ respectively. Assume that $r _ { i }$ is the sum of ith row and $c _ { j }$ denotes the sum of jth column in matrix T. While r presents both direct and indirect effects given by design parameter i to the other design parameters, $c _ { j }$ shows both direct and indirect effects resulted by design parameter j from the other design parameters. ${ \mathrm { I f ~ } } j = i ,$ the sum $( S { = } R + C )$ shows the total effects given and received by design parameter i. The sum indicates importance of the design parameter i in the entire system in terms of relation. On the contrary, the difference $\left( D = R - C \right)$ depicts the net effect that design parameter i contributes to the system. In particular, if the difference is positive, design parameter i is a net cause, while design parameter i is a net receiver or result if the difference is negative [50,51].

Step 8. Set up a threshold value to obtain the interaction diagram: In this step, it is necessary to set up a threshold value to <sup>fi</sup>lter out some negligible effects. Thus, only the effects, which are bigger than the determined threshold value are chosen and shown in diagram [50,51].

Step 9. Calculate the degrees of importance for website design parameters: In this step, a weight vector is obtained by using the sum $( R + C )$ which indicates degrees of interactions among design parameters and degrees of website design parameters' importance with respect to website type. In this step, normalization procedure is applied to $S = [ s _ { i } ] _ { n \times 1 }$ vector as follow [55]:

$$
\hat {s} _ {i} = \frac {s _ {i}}{\sum_ {i = 1} ^ {n} s _ {i}}, \quad i = 1,, 2,... n\tag{6}
$$

where $\hat { \boldsymbol { s } } _ { i }$ is the normalized value of sum vector for ith design parameter. The weight matrix presents the overall importance of each criterion by taking into consideration both interactions among criteria and importance degree of criteria with respect to website type and it is obtained as follows:

$$
w _ {i} = \hat {s} _ {i}, l _ {i} \quad i = 1,, 2,... n\tag{7}
$$

## 4. Application of the proposed model

In this study, the application of the proposed model is conducted in two phases. At <sup>fi</sup>rst, the importance degrees of the design parameters are obtained. Then, the design performance of three websites which are well-known in Turkey is evaluated by using importance degrees of the design parameters. A design team which consists of <sup>fi</sup>ve experts having experience on both interface design and usability is <sup>fi</sup>rstly created for the application phase of the proposed model.

## 4.1. Determining the importance degrees of design parameters

The main aim of this phase is to determine importance degrees of the design parameters which have an important role on website design

Step 1. Collect preferences on design parameters: Each member of the design team evaluated the requirements of the design parameters given in Table 2 individually.

Step 2. Determine the requirements of each design parameter: After expert evaluations, the only online help design parameters are eliminated with respect to information type of websites based on simple majority decision rule.

Step 3. Obtain the importance degrees of each design parameters: In this step, a questionnaire is executed to determine importance of design parameters in terms of website type. The <sup>fi</sup>ve-point Liker type scale ranging [1; 5] (“Very Low $( 1 ) " - " L o w$ (2)”–“Moderate (3)”–“High (4)”–“Very High (5)”) is utilized for the questionnaire by the design team. Simple descriptive statistics were used to identify the preferences. The experts' assessments are presented in Table 3.

Step 4. Create direct relation matrix: Each expert in the design team assess interactions among design parameters. Then, aggregated direct relation matrix is obtained for main and sub-design parameters by using Eq. (3). The relation matrices are as follows:

$$
\begin{array}{c c c c c c c c} & \text {C1} & \text {C2} & \text {C3} & \text {C4} & \text {C5} & \text {C6} & \text {C7} \\ \text {C1} & 0 & 1. 2 & 1 & 1. 6 & 1 & 1. 4 & 1. 8 \\ \text {C2} & 3. 4 & 0 & 1. 2 & 2. 2 & 0. 4 & 0. 6 & 2 \\ \text {C3} & 1. 4 & 1. 2 & 0 & 1. 8 & 1 & 0. 6 & 2 \\ \text {Mc} = & \text {C4} & 1. 8 & 1. 4 & 1. 2 & 0 & 2. 4 & 1. 4 \\ \text {C5} & 1. 2 & 1 & 1 & 2. 4 & 0 & 1. 2 & 3. 4 \\ \text {C6} & 2 & 0. 6 & 0. 4 & 1. 2 & 1. 2 & 0 & 1. 6 \\ \text {C7} & 0. 4 & 0. 6 & 0. 4 & 1. 6 & 1. 8 & 0. 4 & 0 \\ \hline \end{array} \quad \begin{array}{c c c c c c c c} & \text {C31} & \text {C32} & \text {C33} & \text {C34} \\ \text {C31} & 0 & 1. 4 & 2. 6 & 2 \\ \text {C32} & 1. 2 & 0 & 3. 6 & 3. 4 \\ \text {C33} & 1. 4 & 2. 4 & 0 & 1. 8 \\ \text {C34} & 0. 8 & 1. 4 & 1 & 0 \\ \hline \text {C11} & \text {C12} & \text {C13} \\ \text {C11} & 0 & 3. 2 & 3. 2 \\ \text {Mc1=} & \text {C12} & 2. 8 & 0 & 3. 4 \\ \text {C13} & 2. 8 & 3. 4 & 0 \\ \hline \end{array} \quad \begin{array}{c c c c c c c c} & \text {C71} & \text {C72} & \text {C73} \\ \text {C71} & 0 & 1. 8 & 1. 4 \\ \text {Mc7=} & \text {C72} & 3 & 0 \\ \text {C73} & 3. 2 & 2. 6 & 0 \\ \hline \end{array}
$$

$$
Z c = \begin{array}{c c c c c c c c} & C 1 & C 2 & C 3 & C 4 & C 5 & C 6 & C 7 \\ C 1 & 0 & 0. 1 & 0. 1 & 0. 1 & 0. 1 & 0. 1 & 0. 2 \\ C 2 & 0. 3 & 0 & 0. 1 & 0. 2 & 0 & 0. 1 & 0. 2 \\ C 3 & 0. 1 & 0. 1 & 0 & 0. 2 & 0. 1 & 0. 1 & 0. 2 \\ C 4 & 0. 2 & 0. 1 & 0. 1 & 0 & 0. 2 & 0. 1 & 0. 3 \\ C 5 & 0. 1 & 0. 1 & 0. 1 & 0. 2 & 0 & 0. 1 & 0. 3 \\ C 6 & 0. 2 & 0. 1 & 0 & 0. 1 & 0. 1 & 0 & 0. 1 \\ C 7 & 0 & 0. 1 & 0 & 0. 1 & 0. 2 & 0 & 0 \end{array} \quad Z c = \begin{array}{c c c c c c c c} & C 1 1 & C 1 2 & C 1 3 \\ C 1 1 & 0 & 0. 5 & 0. 5 \\ Z c = C 1 2 & C 4 & 0 & C 5 \\ C 1 3 & C 4 & C 5 & C \\ C 2 1 & C 2 2 & C 2 3 \\ Z c = C 2 1 & C 2 (C) = C _ {2} (C) = C _ {2} (C) = C _ {2} (C) = C _ {2} (C) = C _ {2} (C) = C _ {2} (C) = C _ {2} (C) = C _ {2} (C) = C _ {2} (C) = C _ {2} (C) = C _ {2} (C) = C _ {2} ^ {(C)} = C _ {2} ^ {(C)} = C _ {2} ^ {(C)} = C _ {2} ^ {(C)} = C _ {2} ^ {(C)} = C _ {2} ^ {(C)} = C _ {2} ^ {(C)} = C _ {2} ^ {(C)} = C _ {2} ^ {(C)} = C _ {2} ^ {(C)} = C _ {2} ^ {(C)},
$$

$$
Z c 3 = \begin{array}{c c c c c} C 3 1 & C 3 2 & C 3 3 & C 3 4 \\ C 3 1 & 0 & 0. 2 & 0. 4 & 0. 3 \\ C 3 2 & 0. 2 & 0 & 0. 5 & 0. 5 \\ C 3 3 & 0. 2 & 0. 3 & 0 & 0. 3 \\ C 3 4 & 0. 1 & 0. 2 & 0. 1 & 0 \end{array} \quad Z c s = \begin{array}{c c c c c} C 5 1 & C 5 2 & C 5 3 \\ C 5 1 & 0 & 0. 6 & 0. 4 \\ C 5 2 & 0. 7 & 0 & 0. 2 \\ C 5 3 & 0. 7 & 0. 3 & 0 \end{array} \quad Z c s = \begin{array}{c c c c c} C 6 1 & C 6 2 & C 6 3 \\ C 6 1 & 0 & 0. 3 & 0. 4 \\ C 6 2 & 0. 3 & 0 & 0. 7 \\ C 6 3 & 0. 2 & 0. 5 & 0 \end{array}
$$

Step 6. Obtain the total relation matrix: By using Eq. (5) the calculated total relation matrices for main and sub-design parameters are as follows:

Step 5. Normalize the direct-relation matrix: The normalized directrelation matrices are obtained by using Eq.(4):

<table><tr><td></td><td>C1</td><td>C2</td><td>C3</td><td>C4</td><td>C5</td><td>C6</td><td>C7</td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="8">Tc=</td><td>C1</td><td>0.2934</td><td>0.2902</td><td>0.2493</td><td>0.4555</td><td>0.3567</td><td>0.2956</td><td>0.5726</td><td>C11</td><td>C11</td><td>C12</td></tr><tr><td>C2</td><td>0.5984</td><td>0.2426</td><td>0.3033</td><td>0.5638</td><td>0.3707</td><td>0.2818</td><td>0.6722</td><td rowspan="5">Tc1</td><td>C11</td><td>14.0000</td></tr><tr><td>C3</td><td>0.4006</td><td>0.2943</td><td>0.1739</td><td>0.4745</td><td>0.3608</td><td>0.2393</td><td>0.5931</td><td>C12</td><td>14.0000</td></tr><tr><td>C4</td><td>0.5259</td><td>0.3753</td><td>0.3253</td><td>0.4637</td><td>0.5579</td><td>0.3632</td><td>0.8450</td><td>C13</td><td>14.0000</td></tr><tr><td>C5</td><td>0.4419</td><td>0.3200</td><td>0.2866</td><td>0.5872</td><td>0.3506</td><td>0.3224</td><td>0.7856</td><td>C21</td><td>C22</td></tr><tr><td>C6</td><td>0.4016</td><td>0.2231</td><td>0.1846</td><td>0.3869</td><td>0.3377</td><td>0.1686</td><td>0.5062</td><td>C21</td><td>3.9081</td></tr><tr><td>C7</td><td>0.2443</td><td>0.1935</td><td>0.1605</td><td>0.3676</td><td>0.3421</td><td>0.1734</td><td>0.3309</td><td rowspan="2">Tc2</td><td>C22</td><td>4.4865</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>C23</td><td>3.7639</td></tr><tr><td></td><td>C31</td><td>C32</td><td>C33</td><td>C34</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="4">Tc3</td><td>C31</td><td>0.4935</td><td>0.8873</td><td>1.1383</td><td>1.1185</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>C32</td><td>0.7624</td><td>0.9141</td><td>1.4372</td><td>1.4749</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>C33</td><td>0.6455</td><td>0.9617</td><td>0.8667</td><td>1.1001</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>C34</td><td>0.4038</td><td>0.6043</td><td>0.6652</td><td>0.5639</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>C61</td><td>C62</td><td>C63</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="3">Tc6</td><td>C61</td><td>0.7006</td><td>1.2203</td><td>1.5424</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>C62</td><td>1.1469</td><td>1.2881</td><td>2.0169</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>C63</td><td>0.8701</td><td>1.3220</td><td>1.2542</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Step 7. Obtain R and C matrix: The sum of in<sup>fl</sup>uences given and received among design parameters are presented in Table 4.

Step 8. Set up a threshold value to obtain the interaction diagram: In this study, threshold value is selected as the average of the elements in total relation matrix [50,51]. The threshold values for the total relation matrices $T _ { c } , T _ { c 1 } , T _ { c 2 } , T _ { c 3 } , T _ { c 4 } , T _ { c 5 } , T _ { c 6 } ,$ and $T _ { c 7 } ,$ are 0.38, 15.11, 3.47, 0.88, 5.93, 1.26, and 0.94, respectively. The effects which are bigger than the threshold values are shown in the diagrams. The diagrams which depict causal interactions among the main design parameters are presented in Fig. 3.

Step 9. Calculate the degrees of importance for website design parameters: By using Eq. (6) the normalized $\hat { \boldsymbol { S } } _ { i }$ vector is obtained. Then, weight matrix is calculated by Eq. (7). The obtained values are presented in Table 5.

To illustrate the numerical operations for Table 5, following numerical example has been presented;

Relative degrees of interactions for usability

$$
\begin{array}{r l} & = \frac {5 . 4 1 9 5}{5 . 4 1 9 5 + 4 . 9 7 1 9 + 6 . 7 5 5 7 + 4 . 2 2 + 5 . 7 7 0 7 + 4 . 0 5 3 2 + 6 . 1 1 7 9} = 0. 1 4 5 3 \\ & \text { Relative   degrees   of   interactions   for   ease   of   use } = \frac {8 8}{8 8 + 9 2 + 9 2} \\ & = 0. 3 2 3 5 \end{array}
$$

$$
\begin{array}{r l} \text { Overall   degrees   of   interactions   for   ease   of   use } & = 0. 1 4 5 3 \times 0. 3 2 3 5 \\ & = 0. 0 4 7 0 \end{array}
$$

Importance Degrees Including Interactions and website type for ease of use under commercial websites $= 0 . 3 2 3 5 \times 4 . 8 0 = 1 . 5 5 2 9$

## 4.2. Case study: evaluation of online shopping websites

An empirical study has been conducted to demonstrate the effectiveness of the proposed model. In the study, three online shopping websites which sell their customers clothes, shoes, cosmetics, accessories, and sporting goods have been assessed by the design team. Before the evaluation of the shopping websites, some tasks were asked to be carried out by the design team. These tasks are as follows; (i) to join the websites, (ii) to search for a product of a certain trade mark on the website, (iii) to obtain information about products, (iv) to request the

Table 4  
Table 3  
The importance degrees of design parameters with respect to types of websites.

<table><tr><td rowspan="2" colspan="2">Main design parameters</td><td rowspan="2" colspan="2">Sub-design parameters</td><td colspan="4">Types of Websites</td></tr><tr><td>Commercial</td><td>Information</td><td>Entertainment</td><td>Communications</td></tr><tr><td rowspan="4"> $C_1$ </td><td rowspan="4">Usability</td><td></td><td></td><td>5.00</td><td>3.00</td><td>3.67</td><td>5.00</td></tr><tr><td> $C_{11}$ </td><td>Ease of use</td><td>4.80</td><td>3.40</td><td>4.40</td><td>4.40</td></tr><tr><td> $C_{12}$ </td><td>Ease of learning</td><td>4.20</td><td>3.00</td><td>4.80</td><td>4.60</td></tr><tr><td> $C_{13}$ </td><td>Memorability</td><td>4.40</td><td>3.20</td><td>4.00</td><td>4.00</td></tr><tr><td rowspan="4"> $C_2$ </td><td rowspan="4">Visual Aspects</td><td></td><td></td><td>4.33</td><td>1.67</td><td>3.00</td><td>3.33</td></tr><tr><td> $C_{21}$ </td><td>Layout</td><td>4.40</td><td>3.40</td><td>4.20</td><td>3.20</td></tr><tr><td> $C_{22}$ </td><td>Graphics</td><td>3.60</td><td>3.20</td><td>3.60</td><td>2.60</td></tr><tr><td> $C_{23}$ </td><td>Text</td><td>4.20</td><td>4.40</td><td>3.60</td><td>3.60</td></tr><tr><td rowspan="5"> $C_3$ </td><td rowspan="5">Technical adequacy</td><td></td><td></td><td>5.00</td><td>2.67</td><td>4.00</td><td>4.67</td></tr><tr><td> $C_{41}$ </td><td>System availability</td><td>5.00</td><td>3.80</td><td>4.00</td><td>4.80</td></tr><tr><td> $C_{42}$ </td><td>Speed</td><td>4.40</td><td>2.80</td><td>4.80</td><td>4.00</td></tr><tr><td> $C_{43}$ </td><td>Accessibility</td><td>5.00</td><td>3.20</td><td>3.60</td><td>4.00</td></tr><tr><td> $C_{44}$ </td><td>Navigation</td><td>4.40</td><td>3.40</td><td>3.40</td><td>3.80</td></tr><tr><td> $C_4$ </td><td>Content</td><td></td><td></td><td>3.75</td><td>2.75</td><td>4.25</td><td>3.25</td></tr><tr><td rowspan="4"> $C_5$ </td><td rowspan="4">Security</td><td></td><td></td><td>5.00</td><td>3.00</td><td>4.33</td><td>4.67</td></tr><tr><td> $C_{51}$ </td><td>Reliability</td><td>5.00</td><td>4.40</td><td>3.80</td><td>4.60</td></tr><tr><td> $C_{52}$ </td><td>Accuracy</td><td>5.00</td><td>4.60</td><td>2.00</td><td>2.20</td></tr><tr><td> $C_{53}$ </td><td>Privacy</td><td>4.40</td><td>2.00</td><td>2.40</td><td>4.80</td></tr><tr><td rowspan="4"> $C_6$ </td><td rowspan="4">Communication</td><td></td><td></td><td>4.33</td><td>1.00</td><td>1.67</td><td>1.67</td></tr><tr><td> $C_{61}$ </td><td>Contact Info</td><td>4.40</td><td>2.20</td><td>1.40</td><td>1.60</td></tr><tr><td> $C_{62}$ </td><td>Online Help</td><td>4.60</td><td>0.00</td><td>2.00</td><td>2.00</td></tr><tr><td> $C_{63}$ </td><td>Responsiveness</td><td>5.00</td><td>1.00</td><td>2.50</td><td>2.75</td></tr><tr><td rowspan="4"> $C_7$ </td><td rowspan="4">Prestige</td><td></td><td></td><td>4.33</td><td>1.67</td><td>3.33</td><td>3.67</td></tr><tr><td> $C_{71}$ </td><td>Reputation</td><td>4.40</td><td>2.40</td><td>2.40</td><td>3.40</td></tr><tr><td> $C_{72}$ </td><td>Sustainability</td><td>4.20</td><td>1.60</td><td>1.80</td><td>3.00</td></tr><tr><td> $C_{73}$ </td><td>Currency</td><td>3.40</td><td>2.80</td><td>2.60</td><td>3.00</td></tr></table>

website assistance, and (v) to add any product to an online shopping cart. In this paper, the technique for order preference by similarity to the ideal solution (TOPSIS) methodology proposed by [27] has been used for the performance evaluation of the online shopping websites. The method has been based on the concept that the best alternative must have the shortest distance from positive ideal solution and the longest distance from the negative ideal solution [55]. The method consists of six main steps: (1) calculation of normalized ratings, (2) calculation of weighted normalized ratings, (3) identifying positive ideal and negative ideal solutions, (4) calculation of separation measures, (5) calculation of similarities to positive ideal solution, and (6) ranking preference order. In Table $^ { 6 , }$ co-decision matrix belongs to design team is given under the determined design parameters. For the evaluation of online shopping websites experts present their preferences on a scale with a range of [0–100].

The sum of in<sup>fl</sup>uences given and received between design parameters.

<table><tr><td colspan="2"></td><td>R</td><td>C</td><td>S=R+C</td><td>D=R-C</td></tr><tr><td> $C_1$ </td><td>Usability</td><td>2.5133</td><td>2.9061</td><td>5.4195</td><td>-0.3928</td></tr><tr><td> $C_2$ </td><td>Visual aspects</td><td>3.0328</td><td>1.9391</td><td>4.9719</td><td>1.0938</td></tr><tr><td> $C_3$ </td><td>Technical adequacy</td><td>3.4564</td><td>3.2993</td><td>6.7557</td><td>0.1571</td></tr><tr><td> $C_4$ </td><td>Content</td><td>2.5365</td><td>1.6835</td><td>4.2200</td><td>0.8530</td></tr><tr><td> $C_5$ </td><td>Security</td><td>3.0942</td><td>2.6765</td><td>5.7707</td><td>0.4178</td></tr><tr><td> $C_6$ </td><td>Communication</td><td>2.2087</td><td>1.8444</td><td>4.0532</td><td>0.3643</td></tr><tr><td> $C_7$ </td><td>Prestige</td><td>1.8123</td><td>4.3056</td><td>6.1179</td><td>-2.4933</td></tr><tr><td> $C_{11}$ </td><td>Ease of use</td><td>46.0000</td><td>42.0000</td><td>88.0000</td><td>4.0000</td></tr><tr><td> $C_{12}$ </td><td>Ease of learning</td><td>45.0000</td><td>47.0000</td><td>92.0000</td><td>-2.0000</td></tr><tr><td> $C_{13}$ </td><td>Memorability</td><td>45.0000</td><td>47.0000</td><td>92.0000</td><td>-2.0000</td></tr><tr><td> $C_{21}$ </td><td>Layout</td><td>10.6830</td><td>12.1585</td><td>22.8415</td><td>-1.4754</td></tr><tr><td> $C_{22}$ </td><td>Graphics</td><td>11.1949</td><td>9.1173</td><td>20.3122</td><td>2.0777</td></tr><tr><td> $C_{23}$ </td><td>Text</td><td>9.3582</td><td>9.9604</td><td>19.3185</td><td>-0.6022</td></tr><tr><td> $C_{31}$ </td><td>System availability</td><td>3.6376</td><td>2.3052</td><td>5.9427</td><td>1.3324</td></tr><tr><td> $C_{32}$ </td><td>Speed</td><td>4.5886</td><td>3.3674</td><td>7.9560</td><td>1.2212</td></tr><tr><td> $C_{33}$ </td><td>Accessibility</td><td>3.5739</td><td>4.1074</td><td>7.6813</td><td>-0.5335</td></tr><tr><td> $C_{34}$ </td><td>Navigation</td><td>2.2372</td><td>4.2573</td><td>6.4946</td><td>-2.0201</td></tr><tr><td> $C_{51}$ </td><td>Reliability</td><td>18.3951</td><td>22.7108</td><td>41.1060</td><td>-4.3157</td></tr><tr><td> $C_{52}$ </td><td>Accuracy</td><td>16.8212</td><td>17.1766</td><td>33.9978</td><td>-0.3554</td></tr><tr><td> $C_{53}$ </td><td>Privacy</td><td>18.1413</td><td>13.4702</td><td>31.6115</td><td>4.6711</td></tr><tr><td> $C_{61}$ </td><td>Contact info</td><td>3.4633</td><td>2.7175</td><td>6.1808</td><td>0.7458</td></tr><tr><td> $C_{62}$ </td><td>Online help</td><td>4.4520</td><td>3.8305</td><td>8.2825</td><td>0.6215</td></tr><tr><td> $C_{63}$ </td><td>Responsiveness</td><td>3.4463</td><td>4.8136</td><td>8.2599</td><td>-1.3672</td></tr><tr><td> $C_{71}$ </td><td>Reputation</td><td>2.2481</td><td>3.6442</td><td>5.8923</td><td>-1.3961</td></tr><tr><td> $C_{72}$ </td><td>Sustainability</td><td>2.7609</td><td>2.8037</td><td>5.5646</td><td>-0.0427</td></tr><tr><td> $C_{73}$ </td><td>Currency</td><td>3.4780</td><td>2.0391</td><td>5.5171</td><td>1.4388</td></tr></table>

In the application, obtaining two different ranks among the alternatives based on the interactions among design parameters is aimed. At <sup>fi</sup>rst, the rank is obtained without considering the interactions among design parameters. Then, the second rank is obtained by considering interactions among design parameters given in Table 5. For this purpose, the steps of the TOPSIS methodology are applied on the collected data given in Table 6. After we applied the steps of the TOPSIS method on the collected data without considering the interactions among the design parameters, the performance scores 0.761, 0.782, and 0.054 are obtained for A1, A2, and A3, respectively. If the method is applied to the collected data considering the interactions among design parameters, the performance scores 0.781, 0.780, and 0.044 are obtained for A1, A2, and A3, respectively. If we do not take into the interactions among the design parameters, the rank is A2, A1, and A3 from best to worst, respectively. However, if the interactions among the design parameters are taken into consideration, the rank is A1, A2, and A3 from best to worst.

![](/api/attachments/5WTTSUGP/fulltext/images/3f9df2976eaaf51a1833d5b9f14d01c7daecb4d3f1ce6c656178c6f272dc8e38.jpg)  
Fig. 3. The interactions among main design parameters.

Table 5 Im<sub>p</sub>ortance de<sub>g</sub>ree of website desi<sub>g</sub>n <sub>p</sub>arameters.

<table><tr><td rowspan="2" colspan="2"></td><td rowspan="2">R+C</td><td rowspan="2">Relative degrees of interactions</td><td rowspan="2">Overall degrees of interactions</td><td colspan="4">Importance degrees with respect to website type</td><td colspan="4">Importance Degrees Including Interactions and website type</td></tr><tr><td>Commercial</td><td>Information</td><td>Entertainment</td><td>Communications</td><td>Commercial</td><td>Information</td><td>Entertainment</td><td>Communications</td></tr><tr><td>C1</td><td>Usability</td><td>5.4195</td><td>0.1453</td><td></td><td>5.00</td><td>3.00</td><td>3.67</td><td>5.00</td><td>0.7263</td><td>0.4358</td><td>0.5326</td><td>0.7263</td></tr><tr><td>C2</td><td>Visual aspects</td><td>4.9719</td><td>0.1333</td><td></td><td>4.33</td><td>1.67</td><td>3.00</td><td>3.33</td><td>0.5775</td><td>0.2221</td><td>0.3998</td><td>0.4442</td></tr><tr><td>C3</td><td>Technical adequacy</td><td>6.7557</td><td>0.1811</td><td></td><td>5.00</td><td>2.67</td><td>4.00</td><td>4.67</td><td>0.9054</td><td>0.4829</td><td>0.7243</td><td>0.8450</td></tr><tr><td>C4</td><td>Content</td><td>4.2200</td><td>0.1131</td><td></td><td>3.75</td><td>2.75</td><td>4.25</td><td>3.25</td><td>0.4242</td><td>0.3111</td><td>0.4807</td><td>0.3676</td></tr><tr><td>C5</td><td>Security</td><td>5.7707</td><td>0.1547</td><td></td><td>5.00</td><td>3.00</td><td>4.33</td><td>4.67</td><td>0.7734</td><td>0.4640</td><td>0.6703</td><td>0.7218</td></tr><tr><td>C6</td><td>Communication</td><td>4.0532</td><td>0.1086</td><td></td><td>4.33</td><td>1.00</td><td>1.67</td><td>1.67</td><td>0.4708</td><td>0.1086</td><td>0.1811</td><td>0.1811</td></tr><tr><td>C7</td><td>Prestige</td><td>6.1179</td><td>0.1640</td><td></td><td>4.33</td><td>1.67</td><td>3.33</td><td>3.67</td><td>0.7106</td><td>0.2733</td><td>0.5466</td><td>0.6013</td></tr><tr><td>C11</td><td>Ease of use</td><td>88.0000</td><td>0.3235</td><td>0.0470</td><td>4.80</td><td>3.40</td><td>4.40</td><td>4.40</td><td>1.5529</td><td>1.1000</td><td>1.4235</td><td>1.4235</td></tr><tr><td>C12</td><td>Ease of learning</td><td>92.0000</td><td>0.3382</td><td>0.0491</td><td>4.20</td><td>3.00</td><td>4.80</td><td>4.60</td><td>1.4206</td><td>1.0147</td><td>1.6235</td><td>1.5559</td></tr><tr><td>C13</td><td>Memorability</td><td>92.0000</td><td>0.3382</td><td>0.0491</td><td>4.40</td><td>3.20</td><td>4.00</td><td>4.00</td><td>1.4882</td><td>1.0824</td><td>1.3529</td><td>1.3529</td></tr><tr><td>C21</td><td>Layout</td><td>22.8415</td><td>0.3656</td><td>0.0487</td><td>4.40</td><td>3.40</td><td>4.20</td><td>3.20</td><td>1.6088</td><td>1.2431</td><td>1.5356</td><td>1.1700</td></tr><tr><td>C22</td><td>Graphics</td><td>20.3122</td><td>0.3251</td><td>0.0433</td><td>3.60</td><td>3.20</td><td>3.60</td><td>2.60</td><td>1.1705</td><td>1.0404</td><td>1.1705</td><td>0.8454</td></tr><tr><td>C23</td><td>Text</td><td>19.3185</td><td>0.3092</td><td>0.0412</td><td>4.20</td><td>4.40</td><td>3.60</td><td>3.60</td><td>1.2988</td><td>1.3606</td><td>1.1132</td><td>1.1132</td></tr><tr><td>C31</td><td>System availability</td><td>5.9427</td><td>0.2117</td><td>0.0239</td><td>5.00</td><td>3.80</td><td>4.00</td><td>4.80</td><td>1.0584</td><td>0.8044</td><td>0.8467</td><td>1.0160</td></tr><tr><td>C32</td><td>Speed</td><td>7.9560</td><td>0.2834</td><td>0.0321</td><td>4.40</td><td>2.80</td><td>4.80</td><td>4.00</td><td>1.2469</td><td>0.7935</td><td>1.3603</td><td>1.1335</td></tr><tr><td>C33</td><td>Accessibility</td><td>7.6813</td><td>0.2736</td><td>0.0309</td><td>5.00</td><td>3.20</td><td>3.60</td><td>4.00</td><td>1.3680</td><td>0.8755</td><td>0.9850</td><td>1.0944</td></tr><tr><td>C34</td><td>Navigation</td><td>6.4946</td><td>0.2313</td><td>0.0262</td><td>4.40</td><td>3.40</td><td>3.40</td><td>3.80</td><td>1.0179</td><td>0.7865</td><td>0.7865</td><td>0.8791</td></tr><tr><td>C51</td><td>Reliability</td><td>41.1060</td><td>0.3852</td><td>0.0596</td><td>5.00</td><td>4.40</td><td>3.80</td><td>4.60</td><td>1.9260</td><td>1.6948</td><td>1.4637</td><td>1.7719</td></tr><tr><td>C52</td><td>Accuracy</td><td>33.9978</td><td>0.3186</td><td>0.0493</td><td>5.00</td><td>4.60</td><td>2.00</td><td>2.20</td><td>1.5929</td><td>1.4655</td><td>0.6372</td><td>0.7009</td></tr><tr><td>C53</td><td>Privacy</td><td>31.6115</td><td>0.2962</td><td>0.0458</td><td>4.40</td><td>2.00</td><td>2.40</td><td>4.80</td><td>1.3034</td><td>0.5924</td><td>0.7109</td><td>1.4219</td></tr><tr><td>C61</td><td>Contact Info</td><td>6.1808</td><td>0.2720</td><td>0.0295</td><td>4.40</td><td>2.20</td><td>1.40</td><td>1.60</td><td>1.1968</td><td>0.5984</td><td>0.3808</td><td>0.4352</td></tr><tr><td>C62</td><td>Online Help</td><td>8.2825</td><td>0.3645</td><td>0.0396</td><td>4.60</td><td>0.00</td><td>2.00</td><td>2.00</td><td>1.6767</td><td>0.0000</td><td>0.7290</td><td>0.7290</td></tr><tr><td>C63</td><td>Responsiveness</td><td>8.2599</td><td>0.3635</td><td>0.0395</td><td>5.00</td><td>1.00</td><td>2.50</td><td>2.75</td><td>1.8175</td><td>0.3635</td><td>0.9088</td><td>0.9996</td></tr><tr><td>C71</td><td>Reputation</td><td>5.8923</td><td>0.3471</td><td>0.0569</td><td>4.40</td><td>2.40</td><td>2.40</td><td>3.40</td><td>1.5274</td><td>0.8331</td><td>0.8331</td><td>1.1803</td></tr><tr><td>C72</td><td>Sustainability</td><td>5.5646</td><td>0.3278</td><td>0.0538</td><td>4.20</td><td>1.60</td><td>1.80</td><td>3.00</td><td>1.3769</td><td>0.5245</td><td>0.5901</td><td>0.9835</td></tr><tr><td>C73</td><td>Currency</td><td>5.5171</td><td>0.3250</td><td>0.0533</td><td>3.40</td><td>2.80</td><td>2.60</td><td>3.00</td><td>1.1051</td><td>0.9101</td><td>0.8451</td><td>0.9751</td></tr></table>

<table><tr><td rowspan="2"></td><td colspan="3">C1</td><td colspan="3">C2</td><td colspan="4">C3</td><td rowspan="2">C4</td><td colspan="3">C5</td><td colspan="3">C6</td><td colspan="3">C7</td></tr><tr><td>C11</td><td>C12</td><td>C13</td><td>C21</td><td>C22</td><td>C23</td><td>C31</td><td>C32</td><td>C33</td><td>C34</td><td>C51</td><td>C52</td><td>C53</td><td>C61</td><td>C62</td><td>C63</td><td>C71</td><td>C72</td><td>C73</td></tr><tr><td>A1</td><td>79.40</td><td>78.89</td><td>82.75</td><td>81.11</td><td>75.88</td><td>80.00</td><td>85.56</td><td>83.89</td><td>85.40</td><td>77.78</td><td>75.95</td><td>85.56</td><td>81.11</td><td>81.11</td><td>73.33</td><td>62.00</td><td>66.67</td><td>85.56</td><td>84.44</td><td>88.89</td></tr><tr><td>A2</td><td>80.00</td><td>78.89</td><td>85.56</td><td>81.11</td><td>76.67</td><td>75.56</td><td>82.22</td><td>83.33</td><td>83.33</td><td>75.56</td><td>74.45</td><td>85.25</td><td>83.33</td><td>85.56</td><td>76.67</td><td>57.78</td><td>72.22</td><td>90.00</td><td>87.78</td><td>82.22</td></tr><tr><td>A3</td><td>75.00</td><td>76.55</td><td>71.11</td><td>72.22</td><td>71.11</td><td>77.78</td><td>82.22</td><td>78.89</td><td>80.00</td><td>73.33</td><td>74.20</td><td>68.89</td><td>71.11</td><td>74.44</td><td>72.22</td><td>57.78</td><td>61.11</td><td>76.67</td><td>78.89</td><td>77.78</td></tr><tr><td> $w^*$ </td><td>0.047</td><td>0.049</td><td>0.049</td><td>0.049</td><td>0.043</td><td>0.041</td><td>0.024</td><td>0.032</td><td>0.031</td><td>0.026</td><td>0.181</td><td>0.060</td><td>0.049</td><td>0.046</td><td>0.030</td><td>0.040</td><td>0.039</td><td>0.057</td><td>0.054</td><td>0.053</td></tr></table>

Performance evaluation of online shopping websites. Table 6

## 5. Results

The technical adequacy is the most important design parameter with the largest S value whereas the communication criterion is the least important design parameter in terms of interactions among the main design parameters as given in Table 4. After technical adequacy, prestige and security design parameters come second and third, respectively. Furthermore, usability and prestige design parameters are net receivers because of negative D value whereas the others are net causes based on positive D value. From Fig. 3, all of the design parameters directly affect prestige. Moreover, except prestige, the others directly affect technological adequacy and usability of the design parameters. However, none of the design parameters directly affect visual aspects, content, and security design parameters.

From Table 4, ease of learning and memorability under usability, which are the main design parameters have the same interaction degree and they are more important than ease of use. However, ease of learning and memorability design parameters are net receivers because of the negative D value while the ease of use is the net cause based on the positive D value. In Fig. 4, it is seen that ease of use affects both ease of learning and memorability design parameters without being in<sup>fl</sup>uenced. Moreover, ease of learning and memorability affect each other. Hence, ease of use is the most critical design parameter among sub-criteria of usability.

Layout is the most important design parameter among sub-criteria under visual aspects whereas text is the least important design parameter (Table 4). Furthermore, graphic parameter is the net cause whereas layout and text are net receivers. The graphic design parameter is the most essential criterion based on Fig. 5 since it has direct impacts on both layout and text design parameters without being in<sup>fl</sup>uenced by them. Layout and text design parameters also affect each other.

The priority of sub-criteria of technical adequacy is based on S values as follows: speed >accessibility >navigation >system availability. System availability and speed design parameters are net causes while accessibility and navigation design parameters are net receivers. According to Fig. 6, system availability has a direct impact on the other design parameters without being in<sup>fl</sup>uenced by them. Moreover, speed has a direct impact on accessibility and navigation while it is also in<sup>fl</sup>uenced by accessibility.

R-C  
![](/api/attachments/5WTTSUGP/fulltext/images/b7e4fb00d582f29f29abff6ad8fe7077e44ebfdfe461da0804ec81487a020088.jpg)  
Fig. 4. The interaction diagram for sub-design parameter of usability.

![](/api/attachments/5WTTSUGP/fulltext/images/18e7b15d06c339fbbe95f05fdd9647caa14ad41eb3adfa274c8adf393b560d91.jpg)  
Fig. 5. The interaction diagram for sub-design parameter of visual aspects.

Reliability, accuracy, and privacy, the sub-design parameters of security, are the <sup>fi</sup>rst, second, and third with regard to S value, respectively. However, reliability is a net receiver and it is in<sup>fl</sup>uenced by other design parameters as well. Accuracy is also a net receiver and in<sup>fl</sup>uenced by reliability while privacy is a net cause without being in<sup>fl</sup>uenced (Fig. 7).

The priority of the sub-criteria of communication design parameters with respect to S value is as follows: responsiveness>online help>contact information. However, responsiveness is a net receiver whereas online help and contact information are net causes based on the D values. In addition, responsiveness is in<sup>fl</sup>uenced by the other sub-design parameter. Furthermore, online help and responsiveness affect each other while none of them in<sup>fl</sup>uences contact information (Fig. 8).

Among the sub-criteria of prestige design parameter, the rank from the <sup>fi</sup>rst to last is reputation, sustainability, and currency, respectively based on S values. In terms of D values, reputation and sustainability is a net receiver whereas currency is a net cause. From Fig. 9, reputation is in<sup>fl</sup>uenced by the other criteria without affecting them. In addition, currency is the only design parameter affecting both design parameters without being in<sup>fl</sup>uenced.

These results mentioned above are based on the interactions among design parameters. However, website types have a direct impact on the importance degrees of design parameters. Fig. 10 presents importance degrees of design parameters in terms of website types. The rank of the design parameters is usability=technical adequacy= security>visual aspects=prestige>content in terms of commercial website whereas the rank is security=content> technical adequacy> usability>prestige>visual aspects>communication in terms of entertainment websites. In addition, usability=security>content>technical adequacy>visual aspects>communication in terms of information websites while usability>security=technical adequacy>visual aspect>content>communication in terms of communication websites. Moreover, the rank among the sub criterion with respect to subcriteria is given in Fig. 10b. It can be concluded that the importance degrees of website types vary according to website type.

![](/api/attachments/5WTTSUGP/fulltext/images/183e5f1b2bf1ac8c4c7c3431020973dd5e3a1d2b85495c37e04edf68011cf651.jpg)  
Fig. 6. The interaction diagram for sub-design parameter of technical adequacy.

![](/api/attachments/5WTTSUGP/fulltext/images/eaf745b2a8adb01d7079442a9d2446eb0475571778ffba9f848a069364646b7b.jpg)  
Fig. 7. The interaction diagram for sub-design parameters of security.

Now, the relative importance of design parameters will be discussed based on the interactions degrees among design parameters and the

![](/api/attachments/5WTTSUGP/fulltext/images/be383f943ce5c87092d0edc4999cd59ac5b758033468cb77c6978791f6786028.jpg)  
Fig. 8. The interaction diagram for sub-design parameters of communication

![](/api/attachments/5WTTSUGP/fulltext/images/d3a7f813e434ac7d38aef24cf9fc239043831e684cf546f2af88e54d1d7fa43f.jpg)  
Fig. 9. The interaction diagram for sub-design parameter of prestige.

![](/api/attachments/5WTTSUGP/fulltext/images/3fa44d6547678e55ef03ff4755198bd03d04ca125a6da654ce0f043b9d092c21.jpg)

![](/api/attachments/5WTTSUGP/fulltext/images/2c4bd79dd0a974349edea077cead8a8e995ec50cb6bc26b0631c1fa5bb128669.jpg)  
Fig. 10. The rank of importance degrees: the ranks are presented with respect to a) main design parameters; b) sub-design parameters.

importance degrees of design parameters with respect to types of websites. Fig. 11 presents the rank of the design parameters including interactions among design parameters with respect to types of websites. When the interactions among the design parameters are taken into consideration, the importance degrees of design parameters in terms of website types are as follows: {technical adequacy > security>usability>prestige>visual aspects>communication>content}, {technical adequacy >security>usability>content>prestige>visual aspects>communication}, {technical adequacy>security>prestige> usability>content>visual Aspects>communication}, and {technical adequacy>usability>security>prestige>visual aspects>content> communication} according to commercial, information, entertainment, and communication websites, respectively. Table 7 presents the rank of importance degrees for website design parameters including interactions among design parameters and without using interactions.

From Table 7, it is clearly seen that the effect of interactions among design parameters varies with the rank of importance degrees according to website type. In the <sup>fi</sup>rst case, the rank of the importance degrees are the same for some design parameters without taking into account interactions among the criteria while the rank of importance degrees of design parameters signi<sup>fi</sup>cantly change with taking into account the interaction among the design parameters. Fig. 12 presents effects of interactions among the sub-design parameters on rank of importance degrees.

![](/api/attachments/5WTTSUGP/fulltext/images/53535d550a3fe61c30ce7cb69eed08514c595b77475898533b9d02b81b1d212e.jpg)  
Fig. 11. The rank of the design parameters including interactions among design parameters with respect to types of websites.

The rank of importance degrees belonging to website design parameters.

<table><tr><td>Rank</td><td colspan="2">Commercial</td><td colspan="2">Commercial $^{a}$ </td><td colspan="2">Information</td><td colspan="2">Information $^{a}$ </td></tr><tr><td rowspan="3">1</td><td>C3</td><td>Technical adequacy</td><td>C3</td><td>Technical adequacy</td><td>C1</td><td>Usability</td><td>C3</td><td>Technical adequacy</td></tr><tr><td>C1</td><td>Security</td><td></td><td></td><td>C5</td><td>Security</td><td></td><td></td></tr><tr><td>C5</td><td>Usability</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="3">2</td><td>C2</td><td>Visual Aspects</td><td>C5</td><td>Security</td><td>C4</td><td>Content</td><td>C5</td><td>Security</td></tr><tr><td>C6</td><td>Communication</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>C7</td><td>Prestige</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>C6</td><td>Content</td><td>C1</td><td>Usability</td><td>C3</td><td>Technical adequacy</td><td>C1</td><td>Usability</td></tr><tr><td rowspan="2">4</td><td></td><td></td><td>C7</td><td>Prestige</td><td>C2</td><td>Visual Aspects</td><td>C4</td><td>Content</td></tr><tr><td></td><td></td><td></td><td></td><td>C7</td><td>Prestige</td><td></td><td></td></tr><tr><td>5</td><td></td><td></td><td>C2</td><td>Visual Aspects</td><td>C6</td><td>Communication</td><td>C7</td><td>Prestige</td></tr><tr><td>6</td><td></td><td></td><td>C6</td><td>Communication</td><td></td><td></td><td>C2</td><td>Visual Aspects</td></tr><tr><td>7</td><td></td><td></td><td>C4</td><td>Content</td><td></td><td></td><td>C6</td><td>Communication</td></tr><tr><td>Rank</td><td colspan="2">Entertainment</td><td colspan="2">Entertainment $^{a}$ </td><td colspan="2">Communications</td><td colspan="2">Communications $^{a}$ </td></tr><tr><td rowspan="2">1</td><td>C4</td><td>Content</td><td>C3</td><td>Technical adequacy</td><td>C1</td><td>Usability</td><td>C3</td><td>Technical adequacy</td></tr><tr><td>C5</td><td>Security</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan="2">2</td><td>C3</td><td>Technical adequacy</td><td>C5</td><td>Security</td><td>C3</td><td>Technical adequacy</td><td>C1</td><td>Usability</td></tr><tr><td></td><td></td><td></td><td></td><td>C5</td><td>Security</td><td></td><td></td></tr><tr><td>3</td><td>C1</td><td>Usability</td><td>C7</td><td>Prestige</td><td>C7</td><td>Prestige</td><td>C5</td><td>Security</td></tr><tr><td>4</td><td>C7</td><td>Prestige</td><td>C1</td><td>Usability</td><td>C2</td><td>Visual Aspects</td><td>C7</td><td>Prestige</td></tr><tr><td>5</td><td>C2</td><td>Visual Aspects</td><td>C4</td><td>Content</td><td>C4</td><td>Content</td><td>C2</td><td>Visual Aspects</td></tr><tr><td>6</td><td>C6</td><td>Communication</td><td>C2</td><td>Visual Aspects</td><td>C6</td><td>Communication</td><td>C4</td><td>Content</td></tr><tr><td>7</td><td></td><td></td><td>C6</td><td>Communication</td><td></td><td></td><td>C6</td><td>Communication</td></tr></table>

<sup>a</sup> Includes interactions among design parameters

![](/api/attachments/5WTTSUGP/fulltext/images/5a45d1e4f1124230ca6db38842297f1fc355a52590bdcc298b8152d7d99dc2ff.jpg)  
Fig. 12. The effects of interactions among the sub-design parameters on rank of importance degrees.

## 6. The degrees of interactions among design parameters

In Tables 8–14, the degrees of interactions among the design parameters are given. There are four types of interactions; no interaction (○), interaction (◑), strong interaction (◕), very strong interaction (●). The mathematical foundation for the interactions is given by

$$
\tau = \left\{ \begin{array}{l} v <   \bar {t} \Rightarrow \text { no   interaction } \\ \bar {t} \leq v <   1. 5 \bar {t} \Rightarrow \text { interaction } \\ 1. 5 \bar {t} <   v \leq 2 \bar {t} \Rightarrow \text { strong   interaction } \\ 2 \bar {t} \leq v \Rightarrow \text { very   strong   interaction } \end{array} \right.\tag{8}
$$

The degrees of interactions among main criteria.

<table><tr><td></td><td>C1</td><td>C2</td><td>C3</td><td>C4</td><td>C5</td><td>C6</td><td>C7</td></tr><tr><td>C1</td><td>○</td><td>○</td><td>○</td><td>➊</td><td>○</td><td>○</td><td>➊</td></tr><tr><td>C2</td><td>➊</td><td>○</td><td>○</td><td>➊</td><td>○</td><td>○</td><td>➊</td></tr><tr><td>C3</td><td>➊</td><td>○</td><td>○</td><td>➊</td><td>○</td><td>○</td><td>➊</td></tr><tr><td>C4</td><td>➊</td><td>○</td><td>○</td><td>➊</td><td>➊</td><td>○</td><td>➊</td></tr><tr><td>C5</td><td>➊</td><td>○</td><td>○</td><td>➊</td><td>○</td><td>○</td><td>➊</td></tr><tr><td>C6</td><td>➊</td><td>○</td><td>○</td><td>➊</td><td>○</td><td>○</td><td>➊</td></tr><tr><td>C7</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td><td>○</td></tr></table>

where $\tau , { \bar { t } } ,$ and υ symbolize degree of interaction, average of the related total relation matrix, and element of the total relation matrix, respectively.

According to Table 8, there is a very strong interaction between security and prestige. Furthermore, there are strong interactions between usability and prestige, visual aspects and prestige, technical adequacy and prestige, security and content, visual aspects and usability.

According to Tables 9 and 10, there are strong interactions between speed and navigation, speed and accessibility, and online help and responsiveness.

The degrees of interactions among sub-design parameter of technical adequacy.

<table><tr><td></td><td>C31</td><td>C32</td><td>C33</td><td>C34</td></tr><tr><td>C31</td><td>○</td><td>➊</td><td>➊</td><td>➊</td></tr><tr><td>C32</td><td>○</td><td>➊</td><td>➊</td><td>➊</td></tr><tr><td>C33</td><td>○</td><td>➊</td><td>○</td><td>➊</td></tr><tr><td>C34</td><td>○</td><td>○</td><td>○</td><td>○</td></tr></table>

Table 10  
The degrees of interactions among sub-design parameters of communication.

<table><tr><td></td><td>C61</td><td>C62</td><td>C63</td></tr><tr><td>C61</td><td>○</td><td>○</td><td>➊</td></tr><tr><td>C62</td><td>○</td><td>➊</td><td>➊</td></tr><tr><td>C63</td><td>○</td><td>➊</td><td>○</td></tr></table>

Table 11  
The degrees of interactions among sub-design parameter of usability.

<table><tr><td></td><td>C11</td><td>C12</td><td>C13</td></tr><tr><td>C11</td><td>○</td><td>➀</td><td>➁</td></tr><tr><td>C12</td><td>○</td><td>➁</td><td>➁</td></tr><tr><td>C13</td><td>○</td><td>➁</td><td>➁</td></tr></table>

According to Tables 11–14, it is observed that there are not any strong or very strong interactions among design characteristics.

## 7. Conclusion

In the scope of this paper, unlike the published literature until now, importance degrees of website design parameters are determined by taking into consideration not only the importance degrees of the design parameters with respect to website types but also interactions among design parameters. For this purpose, an integrated multiple criteria decision making method including Delphi and DEMATEL techniques has been proposed. The website design parameters are determined based on a detailed review of literature available. In addition, a new classi<sup>fi</sup>cation has been presented for website types. Furthermore, a two phase application has been presented by using the proposed algorithm. The <sup>fi</sup>rst one is to determine the importance degrees of the design parameters. It is concluded from the <sup>fi</sup>rst phase that the importance degrees of the design parameters are affected from interactions among design parameters and website types. The second phase of the application is to evaluate design performance of three websites based on importance degrees of the design parameters. It shows that the rank among the online shopping websites is changed based on the interactions among the design parameters.

Finally, this paper indicates that importance degrees of website design parameters are based on both website types and interaction among the design parameters. It is shown that the obtained rank with respect to the website types is changed by considering interactions among the design parameters. Hence, the interactions among design parameters and importance of design parameters according to website type must be taken into consideration by designers in order to improve quality of a website design.

Table 12  
The degrees of interactions among sub-design parameter of visual aspects.

<table><tr><td></td><td>C21</td><td>C22</td><td>C23</td></tr><tr><td>C21</td><td>➊</td><td>○</td><td>➊</td></tr><tr><td>C22</td><td>➊</td><td>○</td><td>➊</td></tr><tr><td>C23</td><td>➊</td><td>○</td><td>○</td></tr></table>

Table 13  
The degrees of interactions among sub-design parameters of security.

<table><tr><td></td><td>C51</td><td>C52</td><td>C53</td></tr><tr><td>C51</td><td> $\textcircled{1}$ </td><td> $\textcircled{1}$ </td><td>○</td></tr><tr><td>C52</td><td> $\textcircled{1}$ </td><td>○</td><td>○</td></tr><tr><td>C53</td><td> $\textcircled{1}$ </td><td>○</td><td>○</td></tr></table>

Table 14  
The degrees of interactions among sub-design parameter of prestige.

<table><tr><td></td><td>C71</td><td>C72</td><td>C73</td></tr><tr><td>C71</td><td>○</td><td>○</td><td>○</td></tr><tr><td>C72</td><td>➊</td><td>○</td><td>○</td></tr><tr><td>C73</td><td>➊</td><td>➊</td><td>○</td></tr></table>

The main contribution of this paper to the website design literature, unlike the published literature is that this paper takes into consideration both interactions among website design parameters and importance degrees of design parameters according to website types. The second is that this paper extends the classi<sup>fi</sup>cations of websites. For further study, a fuzzy multiple criteria decision making method can be used to evaluate linguistic data and besides, the number of expert teams can be increased in order to investigate the change in the results.

## References

[1] Ö.E. Akbulut, K. Akbulut, Web site designers' opinions about the visual elements, Procedia — Social and Behavioral Sciences 2 (2) (2010) 1549–1553.

[2] A.M. Aladwani, P.C. Palvia, Developing and validating an instrument for measuring user-perceived web quality, Information Management 39 (6) (2002) 467–476.

[3] H. Bell, N. Tang, The effectiveness of commercial Internet web sites: a user's perspective, Internet Research 8 (3) (1998) 219–228.

[4] N. Bonnardel, A. Piolat, L.L. Bigot, The impact of colour on Website appeal and users' cognitive processes, Displays 32 (2011) 69–80

[5] A. Caballero-Luque, P. Aragones-Beltran, M. Garcia-Melon, C. Dema-Perez, Analysis of the alignment of company goals to web content using ANP, International Journal of Information Technology and Decision Making 9 (3) (2010) 419–436.

[6] T. Cheng-Kui Huang, C.C. Huang, An integrated decision model for evaluating educational web sites from the fuzzy subjective and objective perspectives, Computers in Education 55 (2010) 616–629.

[7] A. Chevalier, N. Bonnardel, Articulation of web site design constraints: effects of the task and designers' expertise, Computers in Human Behavior 23 (5) (2007) 2455–2472.

[8] W.C. Chiou, L.C. Lin, C. Perng, A strategic framework for website evaluation based on a review of the literature from 1995–2006, Information Management 47 (2010) 282–290.

[9] E. Cocquebert, D. Trentesaux, C. Tahon, WISDOM: a website design method based on reusing design and software solutions, Information and Software Technology 52 (2010) 1272–1285.

[10] D. Cormany, S. Baloglu, Medical travel facilitator websites: an exploratory study of web page contents and services offered to the prospective medical tourist, Tourism Management 32 (2011) 709–716.

[11] D. Cyretal, M. Head, H. Larios, Colour appeal in website design within and across cultures: a multi-method evaluation, International Journal of Human Computer Studies 68 (2010) 1–21.

[12] S. Djamasbi, M. Siegelb, T. Tullis, Generation Y, web design, and eye tracking, International Journal of Human Computer Studies 68 (2010) 307-323.

[13] J. Éthier, P. Hadaya, J. Talbot, J. Cadieux, Interface design and emotions experienced on B2C Web sites: empirical testing of a research model, Computers in Human Behavior 24 (2008) 2771–2791.

[14] X. Fang, C.W. Holsapple, An empirical study of web site navigation structures' impacts on web site usability, Decision Support Systems 43 (2) (2007) 476–491.

[15] E. Fontela, A. Gabus, Dematel — progress achieved, Futures 6 (4) (1974) 361–363.

[16] E. Fontela, A. Gabus, The DEMATEL Observer, Battelle Geneva Research Centre, Geneva, 1976.

[17] A. Gabus, E. Fontela, World problems, an invitation to further thought within the framework of DEMATEI Battelle Geneva Research Centre Geneva 1972

[18] F.J.M. Gonzalez, T.M.B. Palacios, Quantitative evaluation of commercial web sites: an empirical study of Spanish <sup>fi</sup>rms, International Journal of Information Management 24 (2004) 313–328.

[19] L. Hasan, E. Abuelrub, Assessing the quality of web sites, Applied Computing and Informatics.9 (2011).11-29

[20] D.L. Hoffman, T.P. Novak, P. Chatterjee, Commercial scenarios for the web: opportunities and challenges, Journal of Computer-Mediated Communication, Electronic Commerce 1 (3) (1995) 1–21

[21] Y.-C. Hu, P.-C. Liao, Finding critical criteria of evaluating electronic service quality of Internet banking using fuzzy multiple-criteria decision making, Applied Soft Computing 11 (2011).3764-3770.

[22] C.Y. Huang, J.Z. Shyu, G.H. Tzeng, Recon<sup>fi</sup>guring the innovation policy portfolios for Taiwan's SIP Mall industry, Technovation 27 (12) (2007) 744–765.

[23] A.Y. Huang, W.S. Lee, Y.Y. Chang, C.M. Cheng, Analysis of decision making factors for equity investment by DEMATEL and Analytic Network Process, Expert System with Applications 38 (7) (2011) 8375–8383.

[24] E.K. Huizingh, The content and design of web sites: an empirical study, Information Management 37 (3) (2000) 123–134.

[25] Y.-H. Hung, S.-C.T. Chou, G.-H. Tzeng, Knowledge management adoption and assessment for SMEs by a novel MCDM approach, Decision Support Systems 51 (2) (2011) 270–291.

[26] C.L. Hwang, M.J. Lin, Group Decision Making under Multiple Criteria, Springer-Verlag Berlin, 1987.

[27] C.L. Hwang, K. Yoon, Multiple Attribute Decision Making: Methods and Applications, Springer-Verlag, Berlin/Heidelberg/Newyork, 1981.

[28] E.C.S. Ku, Y.W. Fan, The decision making in selecting online travel agencies: an application of analytic hierarchy process, Journal of Travel & Tourism Marketing 26 (5–6) (2009) 482–493.

[29] S. Lee, R.J. Koubek, The effects of usability and web design attributes on user preference for e-commerce web sites, Computers in Industry 61 (4) (2010) 329–341.

[30] Y. Lee, K.A. Kozar, Understanding of Website Usability: Specifying and Measuring Constructs and Their Relationships, Decision Support Systems 52 (2) (2012) 450–463.

[31] H.-F. Lin, An application of fuzzy AHP for evaluating course website quality, Computers in Education 54 (2010) 877–888.

[32] Y.T. Lin, Y.H. Yang, J.S. Kang, H.C. Yu, Using DEMATEL method to explore the core competences and causal effect of the IC design service company: An empirical case study, Expert System with Applications 38 (5) (2011) 6262–6268.

[33] C. Liu, K.P. Arnett, Exploring the factors associated with web site success in the context of electronic commerce, Information Management 38 (1) (2000) 23–33.

[34] G.Z. Liu, Z.H. Liu, G.J. Hwang, Developing multi-dimensional evaluation criteria for English learning websites with university students and professors, Computers in Education 56 (2011) 65–79.

[35] M.M. Misic, K. Johnson, Benchmarking: a tool for web site evaluation and improvement, Internet Research 9 (5) (1999) 383–392.

[36] C. Morosan, M. Jeong, Users' perceptions of two types of hotel reservation web sites, International Journal of Hospitality Management 27 (2) (2008) 284–292.

[37] M. Moshagen, M.T. Thielsch, Facets of visual aesthetics, International Journal of Human Computer Studies 68 (2010) 689–709.

[38] S. Muylle, R. Moenaert, M. Despontin, The conceptualization and empirical validation of web site user satisfaction, Information Management 41 (5) (2004) 543–560.

[39] J.M. Pearson, A.M. Pearson, An exploratory study into determining the relative importance of key criteria in Web usability: a multi-criteria approach, The Journal of Computer Information Systems 48 (4) (2008) 115–127.

[40] E. Şengel, S. Öncü, Conducting preliminary steps to usability testing: investigating the website of Uludağ University, Procedia Social and Behavioral Sciences 2 (2010) 890–894.

[41] Y.C. Shen, G.T.R. Lin, G.H. Tzeng, Combined DEMATEL techniques with novel MCDM for the organic light emitting diode technology selection, Expert System with Applications 38 (3) (2011) 1468–1481.

[42] J.I. Shieh, H.H. Wu, K.K. Huang, A DEMATEL method in identifying key success factors of hospital service quality, Knowledge-Based Systems 23 (3) (2010) 277–282.

[43] C. Tsai, Y.T. Cheng, Analyzing key performance indicators (KPIs) for E-commerce and Internet marketing of elderly products: a review, Archives of Gerontology and Geriatrics 55 (2012) 126–132

[44] W.H. Tsai, W. Hsu, A novel hybrid model based on DEMATEL and ANP for selecting cost of quality model development, Total Quality Management and Business Excellence 21 (4) (2010) 439–456.

[45] M.L. Tseng, Y.H. Lin, Application of fuzzy DEMATEL to develop a cause and effect model of municipal solid waste management in Metro Manila, Environmental Monitoring and Assessment 158 (1–4) (2009) 519–533.

[46] A.N. Tuch, J.A. Bargas-Avila, K. Owis, Symmetry and aesthetics in website design: it's a man's business, Computers in Human Behavior 26 (2010) 1831–1837.

[47] G.H. Tzeng, F.H. Chen, T.S. Hsu, A balanced scorecard approach to establish a performance evaluation and relationship model for hot spring hotels based on a hybrid MCDM model combining DEMATEL and ANP, International Journal of Hospitality Management 30 (4) (2011) 908–932.

[48] G.H. Tzeng, W.R.J. Ho, C.L. Tsai, S.K. Fang, Combined DEMATEL technique with a novel MCDM model for exploring portfolio selection based on CAPM, Expert System with Applications 38 (1) (2011) 16–25.

[49] H.A. Wan, Opportunities to enhance a commercial web site, Information Management 38 (1) (2000) 15–21.

[50] H.H. Wu, Y.N. Tsai, A DEMATEL method to evaluate the causal relations among the criteria in auto spare parts industry, Applied Mathematics and Computation 218 (5) (2011) 2334–2342.

[51] H.H. Wu, H.K. Chen, J.I. Shieh, Evaluating performance criteria of Employment Service Outreach Program personnel by DEMATEL method, Expert Systems with Applications 37 (7) (2010) 5219–5223.

[52] C.H. Wu, B. Chang, C.W. Chang, Fuzzy DEMATEL method for developing supplier selection criteria, Expert Systems with Applications 38 (3) (2011) 1850–1858.

[53] J.L. Yang, G.H. Tzeng, An integrated MCDM technique combined with DEMATEL for a novel cluster-weighted with ANP method, Expert Systems with Applications 38 (3) (2011) 1417–1424.

[54] C.S. Yiu, K. Grant, D. Edgar, Factors affecting the adoption of Internet Banking in Hong Kong — implications for the banking sector, International Journal of Information Management 27 (2007) 336–351.

[55] K.P. Yoon, C.L. Hwang, Multiple Attribute Decision Making: An Introduction, Sage Publications, London, 1995.

[56] X. Yu, S. Guo, J. Guo, X. Huang, Rank B2C e-commerce websites in e-alliance based on AHP and fuzzy TOPSIS, Expert Systems with Applications 38 (2011) 3550–3557.

[57] L. Zeng, G. Salvendy, M. Zhang, Factor structure of web site creativity, Computers in Human Behavior 25 (2009) 568–577.

[58] Q. Zhou, W.L. Huang, Y. Zhang, Identifying critical success factors in emergency management using a fuzzy DEMATEL method, Safety Sci 49 (2) (2011) 243–252.

[59] M. Zviran, C. Glezer, I. Avni, User satisfaction from commercial web sites: the effect of design and use, Information Management 43 (2) (2006) 157–178.

[60] D. Robins, J. Holmes, Aesthetics and credibility in web site design, Information Processing and Management 44 (2008) 386–399.

[61] G.H. Tzeng, W.H. Chen, R. Yu, M.L. Shih, Fuzzy decision maps: a generalization of the DEMATEL methods, Soft Computing 14 (2010) 1141–1150.

Selcuk Cebi is an Assistant Professor in Department of Industrial Engineering at Karadeniz Technical University. He received his PhD from Istanbul Technical University in 2010. His current research interests are Decision support systems, Multiple Criteria Decision Making, Human-Computer Interactions, and Interface Design.
