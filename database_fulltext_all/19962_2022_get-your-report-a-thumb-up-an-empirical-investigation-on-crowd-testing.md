---
otero_id: 19962
otero_key: "ZYZJ5QZH"
title: "Get your report a thumb-up: An empirical investigation on crowd testing"
authors: "Jingxuan Cai; Dan Ke; Jiang Wu; Xin (Robert) Luo"
year: "2022"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2022.113781"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Get your report a thumb-up: An empirical investigation on crowd testing

![](/api/attachments/ZYZJ5QZH/fulltext/images/9017badb773ef8162481b9a97bc41276c41814504a271f730b81f1bbdbb39e03.jpg)

Jingxuan Cai <sup>a,c</sup>, Dan Ke <sup>b,\*</sup>, Jiang Wu <sup>c,\*</sup>, Xin (Robert) Luo <sup>d</sup>

<sup>a</sup> Research Center for Smarter Supply Chain, Dongwu Business School, Soochow University, Suzhou, Jiangsu 215031, PR China

<sup>b</sup> Economics and Management School, Wuhan University, Wuhan, Hubei 430072, PR China

<sup>c</sup> School of Information Management, Wuhan University, Wuhan, Hubei 430072, PR China

<sup>d</sup> Anderson School of Management, The University of New Mexico, Albuquerque, NM 87106, USA

## A R T I C L E I N F O

Keywords: Crowd testing Testing reports Peer tester Information adopting model Text mining

## A B S T R A C T

Crowd testing has been increasingly adopted as a marketing strategy for e-Retailers. However, scant academic research empirically addresses the performance of crowd testing from either the platform's or crowd testers perspectives. This study aims to investigate the determinants of the usefulness of crowd testing reports in order to theoretically demonstrate the significance of crowd testing strategy, especially for new product promotion. We integrated text mining and regression to test the research model using the data extracted from a crowd testing website, Dealmoon.com. The analysis results show that the crowd testers' credibility and the testing report's information quality both play significant roles in the usefulness of crowd testing reports. Furthermore, the presence of peer testers' reports on the focal product moderates the effect of information quality on the report's usefulness. The research findings provide managerial implications for marketing practitioners to implement the crowd testing strategy effectively and for crowd testers to create useful testing reports.

## 1. Introduction

Crowd testing is a business strategy in which merchants provide free samples to selected customers in exchange for their testing reports [1], such as PINCHme.com and Dealmoon.com in the U.S. and Try.taobao. com in China. It has become an effective means of promoting products and facilitating product diffusion during the introduction phase of their marketing cycle. For merchants, launching such a marketing strategy can increase product ratings by 1.1% and consumers' purchase proba bility by approximately 300% [2,3]. For crowd testers, publishing testing reports in such a social commerce platform leads to growing social recognition and influence as they grow up and become opinion leaders [4].

Crowd testing stems from offline free trials and online reviews [1]. The free trial aims to provide potential customers with samples and provoke their purchase intention. It merely targets those who receive the product/services. With the prosperity of e-commerce, free trials have gradually embarked online. The virtual community enables the mer chant to recruit a crowd of participants to try out their products. This metric was initially used by software companies to collect feedback on new software versions, as well as product diffusion and word-of-mouth marketing [5]. Following that, the types of testing products expanded to various genres, including food, cosmetics, and houseware [3].

Due to the information asymmetry of online transactions, it is diffi cult to evaluate the true value of goods before they are delivered and consumed [6]. Consumers need firsthand experience of the product to reasonably support their assessment of its value [7]. As e-commerce flourishes with information technologies, crowd testing has been increasingly adopted as a marketing strategy for e-retailers. E-retailers send out free products to selected testers and collect their feedback via online social media, where it functions as a leverage to increase the likelihood of persuading potential consumers to accept the newly launched product. In addition, platforms shape up and recruit experi enced consumers to test free products on the condition that they share their real experience of the product or service – accompanied by all their comments related to the product (in terms of their emotions, prefer ences, cognitive impressions, behaviors, and achievements) before, during, and after using the trial sample [8].

The typical crowd testing in our research context entails the following steps. First, the online merchant posts a free sample offer on the crowd testing community, seeking volunteers to test a product for the cost of a post-consumption evaluation report within a specific period; anyone interested in the offer can apply for a free sample. Then, the merchant selects a few qualified applicants and sends them a product sample. After the testing period, the selected testers publish their per sonal testing reports on the crowd testing community for potential customers' references [3, 9].

Normally, merchants view crowd testing as a strategy for word-of mouth marketing in complement to online reviews. The crowd testing operator creates a community for testers to publish their testing reports for others to refer to. The scope of reach expands to include a broader range of potential customers [3]. The online review takes previous customers' comments about their product or service experience as a reference for potential customers [10]. As a result, online reviews are helpful only if the focal product is already on the market with a strong sales volume. For a newly launched product or an updated version of an existing product, the online review volume may not be insufficient for consumers to effectively identify its new features. The best way to demonstrate its superiority is to have the customer try it [11]. Moreover, online reviews are commonly attached to online shopping sites as a measure to persuade customers' purchasing decisions. Fake or biased reviews are an obstacle for consumers to evaluate products correctly [66]. In contrast, the platform itself, such as Dealmoon.com, does not sell products, putting it in an objective position when it comes to pub lishing testing reports. The crowd testing platform functions as a social community. An online social network is formed as patrons participate in these activities. The crowd testing report is delivered as one of the ways to encourage interaction and experience sharing. Thus, compared to anonymous online reviews, crowd testing reports are inextricably tied to the authors' social identities in the community.

This study is motivated by the conspicuity of the crowd testing strategy. Prior research has limitedly focused on the overall impact of the free product trial strategy on sales and new product diffusion [8,11,12]. However, scant research touches on the perspective of crowd testers or crowd testing reports. The crowd testing report, although in the shape of extensive online review as a complement of e-WOM, has its innovative form and originates from the crowd wisdom. To advance this line of research, this paper is an initial effort to shed light on crowd testing reports by conducting a theory-driven, robust empirical study to investigate the determinants of their usefulness. Utilizing data extracted from a leading crowd testing website, Dealmoon, this study aims to investigate the determinants of the perceived usefulness of crowd testing reports.

This paper applies theories in information systems and marketing disciplines to establish the research model. The information adoption model suggests that the perceived usefulness of information is evaluated from two perspectives: information source credibility and information quality [13]. Uncertainty reduction theory, from the perspective of report content, explains the behavior in which customers tend to collect more information to reduce uncertainty in online shopping [14]. Peer competition proposes that an individual's behavior is influenced by peer presence due to competition challenges [15]. Accordingly, we conjec ture that the usefulness of the crowd testing report is demonstrated through testers' attributes (the information source credibility) and the report text (information quality). Such an effect would be mitigated by the intensity of peer competition (peer testers' report). We extracted all information from crowd testing reports on Dealmoon to illustrate the writers' credibility and reports' quality. To achieve scientific research pluralism, sentiment extraction is conducted using machine learning algorithms to capture essential signals from report text, and negative binomial regression is adopted to analyze and validate the theoretical framework. Combining these methods allows us to explore the de terminants of the usefulness of crowd testing reports from the afore mentioned two theoretical perspectives. This research looks into the emerging business model of crowd testing, and the research finding carry managerial implications for marketing practitioners to implement the crowd testing strategy effectively and for crowd testers to create useful testing reports.

## 2. Related literature

Since there is scarce literature on crowd testing, this section reviews the related research from three literature streams: (1) Free product trial strategy, as an earlier form of marketing tool that incubates crowd testing; (2) Usefulness of online review, given that crowd testing reports develop as an extensive form of online review; (3) Crowdsourcing, and crowd testing alike, is engaged in crowd behavior and practice of obtaining opinions or content from the online community to demon strate the wisdom from the crowd.

## 2.1. Free product trial strategy

The free product trial is the predecessor of the crowd testing strategy for new products. The product trial is an essential promotional tool that has long been employed by merchants to reach out to consumers of experiential products before the actual purchase event to allow them to sample the product in hopes of motivating them to make a purchase [1]. However, the traditional product trial only targets the people who participate in the event, which offers the participant a free product and then generates their demand for repeated consumption [16]. With the rapid development of e-commerce, product trial is increasingly admin istered online [3].

The existing literature on online free product trials mostly focuses on its effect on promotion or new product marketing. Offering free samples can reduce consumers' uncertainties about new products by serving as a direct source of information [17]. Compared to traditional advertise ments that are always positive and still raise consumers' suspicions over their objectivity, the direct experience recounted by the product trial report can influence consumers' perception of the product more than the indirect advertising information [18]. Consumers are more intensely involved in product trials, thereby having a more significant effect on sales. The combination of product trial reports and regular reviews can promote sales of experiential products [5,19].

Table 1 is a summary of recent research related to free product trials. The existing literature mainly demonstrates the marketing effectiveness of this strategy to reduce the risks perceived by consumers, especially toward the development of new products and new markets [5,20]. The determinants of crowd testing reports have barely been studied. Thus, this study takes crowd testing reports as the research object from the testers' perspective.

## 2.2. Helpfulness of online reviews

Crowd testing reports are formed as an extensive product review. However, unlike online reviews generated in the full cycle of product lifetime, crowd testing reports usually apply to the preannouncement and introduction period of the product lifecycle to promote new prod ucts. In any case, it is necessary to review the literature on online re views to understand the usefulness of crowd testing reports.

Scholars have explored the usefulness and helpfulness of online re views to potential consumers. Rocklage and Fazio conducted a wellcontrolled experiment with 100,000 Amazon reviews across 500 prod ucts and found that reviews expressing emotion for hedonic products have a positive impact when read by others, but this emotion backfires for utilitarian products and leads others to be less positive [24]. Yin et al. found that reviews containing content indicating anxiety are more helpful than those indicative of anger [25]. Lare et al. investigated the narrativity of reviews and argued that the most persuasive reviews have better-developed characters and events and are emotionally charged, recounting dramatic events [26]. Hong et al. empirically confirmed through a meta-analysis that review depth, review age, reviewer infor mation disclosure, and reviewer expertise all have positive influences on review helpfulness [10]. Additional features such as specific review content and writing styles, readability, product rating, and review valence also positively impact review helpfulness [27,28].

Table 1 Related literature on free product trial.

<table><tr><td>Reference</td><td>Research question</td><td>Sampling distribution approach</td><td>Methodology/Description</td><td>Key findings</td></tr><tr><td>[1]</td><td>Costumers&#x27; attitude to product trial.</td><td>Offline</td><td>An online questionnaire with 484 respondents</td><td>Customers perceive samplings positively.</td></tr><tr><td>[2]</td><td>How a product&#x27;s engagement in free product sampling affects the product&#x27;s review rating.</td><td>Online</td><td>A rich data set from Taobao.com and multiple identification strategies and estimation methods</td><td>Consumers give higher ratings as a return to retailers&#x27; beneficial actions. Engaging in free product sampling increases product rating by 1.1%.</td></tr><tr><td>[12]</td><td>The effect of free sampling on product diffusion</td><td>Online and Offline</td><td>A Bass model</td><td>Enterprises should select different sampling levels according to different pricing strategies and product types.</td></tr><tr><td>[3]</td><td>The effects of product sample&#x27;s application outcomes on applicants&#x27; purchase behavior.</td><td>Online</td><td>A Probit binary choice model with data of online physical product sampling and consumers&#x27; purchase behavior</td><td>Receiving a product sample could increase the consumers&#x27; purchase probability by approximately 300%. These effects vary among different types of consumers.</td></tr><tr><td>[7]</td><td>How competing retailers&#x27; sampling and pricing strategies are affected by consumer switching behavior, the goodwill effect of sampling, and the intensity of product competition.</td><td>In general</td><td>Game theory</td><td>The goodwill effect of sampling, the probability of realizing good fits with products, consumer switching behavior, and the intensity of product competition play different roles in determining the retailers&#x27; sampling and pricing strategies.</td></tr><tr><td>[5]</td><td>The interplay between free sampling and word of mouth in the online software market</td><td>Online</td><td>A Bayesian analysis of software free sampling on CNETD and sales and WOM from Amazon over a 25-week data set.</td><td>Free sampling complements WOM in the online market by amplifying its sales effect and facilitating its implementation.</td></tr><tr><td>[9]</td><td>The effect of physical product sampling on sales.</td><td>Online</td><td>A DID model with a panel data of 122 online product sampling campaigns</td><td>Online sampling could increase the physical product sales, while popular brands enjoyed greater advantages in terms of an increase in both immediate and lagged sales.</td></tr><tr><td>[11]</td><td>The effect of product sampling for new product diffusion.</td><td>In general</td><td>Bass model</td><td>Product sampling can accelerate the diffusion process of a new product. The best time to send free samples is just before the product is launched.</td></tr><tr><td>[8]</td><td>The effect of sample type on sampling campaigns and the relative importance of the decisions of which consumers to target and how many to target.</td><td>Online</td><td>An agent-based model</td><td>The decision of which consumers to target is more important than that of how many consumers to target.</td></tr><tr><td>[21]</td><td>Examines the trade-off between the effects of reduced uncertainty and demand cannibalization.</td><td>Online</td><td>Quantitative model</td><td>A threshold of network effect exists. It will affect the effects of the free trial strategy.</td></tr><tr><td>[22]</td><td>Build the optimal model group of product sampling by considering dynamic pricing and promotion strategies.</td><td>In general</td><td>Genetic algorithms</td><td>It presents a future research framework for determining optimal product sampling for the market diffusion of new products at time zero or over time.</td></tr><tr><td>[23]</td><td>Should the firm keep customers informed.</td><td>In general</td><td>Operational research and game theory</td><td>Product sampling, acting as a way to solve information asymmetry, enables the firm to extract a higher surplus.</td></tr><tr><td>[16]</td><td>The effects of sampling experiential products on subsequent product choices</td><td>Offline</td><td>Experiment</td><td>When sampling two equally desirable experiential products, consumers prefer the product experienced second. When sampling two equally undesirable experiential products, they prefer the first product.</td></tr><tr><td>[18]</td><td>How a product trial influences product-attitude formation,</td><td>In general</td><td>Lab experiments</td><td>Affective response overrode cognitive structure in forming product-trial attitudes, whereas the roles of affective response and cognitive structure were similar in product trial-based product attitude formation.</td></tr><tr><td>[19]</td><td>To model both the immediate effects of sampling on sales as well as its longer-term effects on building goodwill.</td><td>Offline and online</td><td>A theoretical model</td><td>Although the sampling effort will decline over a product&#x27;s Life cycle, it may continue in mature products.</td></tr><tr><td>[17]</td><td>Examined the effectiveness of mail-drop product samples and coupons as means of promoting trial behavior among non-users of three products.</td><td>Mail-drop product samples</td><td>Interview among 356 household respondents</td><td>Samples and coupons encourage more trials when delivered in combination than when delivered separately, and coupons delivered alone are an ineffective means of generating trials.</td></tr></table>

Crowd testing reports are distinct from online reviews in the process, tested product, and content. Customers leave online reviews after they actually purchase the products. The new product marketers call crowd testers and request testing reports of the newly announced products. However, for newly arriving or even upcoming products, online reviews can hardly provide effective references due to limited sales volume. In contrast, crowd testing strategies apply to a wide range of product types, typically “experience products” such as food, cosmetics, electronics, automobiles, and virtual services. [5]. Most of them are newly launched products in the market introduction period [12]. The crowd testing report can provide potential customers with a real experience of a product even before it is officially released and widely spread among the general public. However, online reviews contain mostly paragraphs that describe customers' evaluations of products or services [29]. According to the data we collected from Dealmoon.com, the average word count of a crowd testing report is 1175 with 22.7 pictures. The average length of online review in the recent literature range from 72 to 149.9 [26,30,31]. Compared with the online review, the crowd testing report is generally longer in text length and has more pictures, and thus contains more information about the product, its features, and pros and cons. There fore, crowd testing works better in providing information about the tested product and reducing consumers' uncertainty. Table 2 makes a distinction between crowd testing reports and online reviews.

Despite the distinctions between online reviews and crowd test re ports, their usefulness shares some common determinants, including length, readability, writing style, and sentiment [10,30]. Thus, we extend them to the context of crowd testing reports in the subsequent study.

## 2.3. Crowdsourcing

Crowd testing takes full advantage of crowd behavior and practice and shares personal wisdom in an online community. Crowdsourcing is a technique that often takes the form of an idea competition or innovation contest that allows an organization to divide the responsibilities of a task among individuals to accomplish a pooled result. Brabham has argued that crowdsourcing is more than just an online business model but a profoundly influential problem-solving model that could be used for our world's most pressing social and environmental problems [32]. In a crowdsourcing application, the term “crowd” refers to the collective of web users who participate in the problem-solving process by positing solutions. Their strength lies in the composite or aggregate of ideas rather than in collaboration [33].

Similarly, the crowd testing platform invites a group of testers to test the same product. It inherits the idea of crowdsourcing, which hires a crowd of people working together to accomplish a task [34]. Thus, crowd testing can be regarded as a practice of crowdsourcing in the context of e-WOM marketing to provide comprehensive information on an upcoming product, possibly from different angles.

Competition is an inherent feature of crowdsourcing that influences how teams allocate their effort and achieve the desired performance [34]. There is competition among participants when they strive for the opportunity to participate in the crowdsourcing task [35]. Competitions among participants would lead to higher enjoyment and crowdsourcing participation and then lead to better performance [36]. However, the outcome of the competition is not always satisfying. Competitions can have demotivating effects on performance when competition intensity is overwhelming [37].

In the context of crowd testing, peer testers are competitors to each other to obtain more “likes” to become successful product endorsers. However, it remains unclear how the presence of peer testers would impact the usefulness of the testing report. In this paper, we take the number of peer testers as the competition intensity and explore its moderating effect.

## 3. Theoretical foundations and hypothesis development

The research model is established based on the theoretical un derpinnings of the Information Adoption Model, uncertainty reduction theory, and peer effect theory. The research framework is pre-shadowed in Fig. 1. Information source credibility includes the author's expertise and socialization on the platform. We estimate the information quality through the report text, including information amount, readability, processing burden, sentiment, and content of the text. Peer testers' re ports relating to the same product negatively moderate the effect of information quality on report usefulness. Additionally, we control the tested product attributes (e.g., product type, price, and whether the tested product is new to market) and report attributes (e.g., publishing time and number of pictures in the report) in the research.

## 3.1. Information adoption model

The Information Adoption Model proposes that information adop tion behavior (from information searchers) is affected by information quality and information source credibility. The former is the core path for information seekers to adopt information–making decisions by deeply evaluating the content. Information source credibility is the edge path adopted by information searchers. When they make decisions through the edge path, they attach more importance to the reliability of the information source rather than the content itself. This model has been widely used to study the information adoption behavior of online community users [13].

Table 2  
Characteristics of crowd testing reports and online reviews.

<table><tr><td></td><td>Crowd testing report</td><td>Online reviews</td></tr><tr><td>Who can participate</td><td>Selected qualified testers</td><td>Consumers who have purchased products</td></tr><tr><td>Cost of consuming the product</td><td>Free</td><td>Pay for the product</td></tr><tr><td>Whether it is mandatory</td><td>Yes</td><td>No</td></tr><tr><td>When to be released in the market cycle</td><td>Preannouncement or introduction period</td><td>After the product is on the market</td></tr><tr><td>Richness of content</td><td>Long text and plenty of pictures</td><td>Mostly short text and some pictures</td></tr><tr><td>Operator</td><td>Crowd testing platform or the merchants</td><td>Shopping sites</td></tr><tr><td>Purpose of participating in crowd testing</td><td>To become a successful tester to earn business value in the future</td><td>To share shopping experience</td></tr></table>

Applicants need to compete with each other to become a selected tester and receive the testing product.

Based on the literature on information adoption behavior, this paper argues that the factors that influence the adoption of crowd testing re ports are mainly divided into two categories: 1) the information source credibility related to the crowd tester, such as his/her history, the number of followers, etc. 2) the information quality of the report.

## 3.1.1. Crowd Testers' credibility

We regard the crowd testers as the information source of the crowd testing reports. We evaluate crowd testers' credibility in the research model by two variables: level of expertise and level of socialization.

According to Chaiken and Shelly, information source credibility is the trust of the receiver in the source of information [38]. Thus, a factor for the reader when assessing the usefulness is whether they trust the source of information [39]. As an information source, the author's at tributes (e.g., expertise, reputation, and fanbase) are significantly correlated with the perceived usefulness of the information. When people collect information in their decision-making process, they are inclined to follow experts' suggestions because they believe that infor mation provided by an expert is more useful and trustworthy. In the online environment, source expertise is a cue to evaluate trustworthi ness. Online readers are influenced by the degree of expertise. Thus, we propose:

Hypothesis 1a. Crowd testing reports published by authors with a higher level of expertise are more useful to readers.

Many product-focused online social platforms have included design features that can convey more information about product quality as well as the credibility of the members of the social community. To eliminate anonymity concerns between information providers and receivers, websites provide measures to establish social networks between them. The count of a key opinion leader's followers impacts product involve ment, buying intention, and intention to pass along e-WOM from the source credibility aspect [40]. The counts of followers and following users represent the author's level of socialization in an online commu nity and are regarded as a cue for information source credibility ac cording to information signaling theory [41]. The more followers a tester has, the greater the number of people who recognize him/her [39], and the more his/her reports would be “Liked”. Thus, we propose that.

Hypothesis 1b. Crowd testing reports published by authors with a higher level of socialization are more useful to readers.

![](/api/attachments/ZYZJ5QZH/fulltext/images/9d63640e30400151bbcbe147cff724dce17b19f8f67559a4201e6982ee39bb17.jpg)  
Fig. 1. Research framework.

## 3.1.2. Quality of crowd testing reports

We take the information amount, readability, perception process, and emotional expression to evaluate the information quality of the testing reports.

In the e-commerce environment, consumers cannot truly see and touch the product before it is delivered, which increases quality con cerns before the online purchase [42]. Consumers, trying to avoid risks, would like to wait until feedback from leading consumers is available. A large portion of rational consumers will then read the crowd testing reports to obtain more product detail information to reduce uncertainty and make better purchase decisions.

Information helps consumers reduce the risk and uncertainty in the decision-making process. Information is mostly composed and delivered in text forms, so text length is a natural way to gain insights. A long piece of text can attract attention and motivate reading [31]. Long texts with more information are more likely to contain a deep analysis of a product, its features, and the context in which it was used [30]. An individual's argument is more persuasive when it provides a larger amount of in formation [30]. Reports are perceived as more useful because readers treat higher word counts as representative of greater depth in infor mation, including its comprehensiveness and usefulness. Thus, we pro pose that.

Hypothesis 2a. Crowd testing reports with larger information amounts are more useful to readers.

Readability refers to the cognitive efforts required to read and comprehend reviews [43]. Text is the information resource that readers use to gain knowledge about products and services [44]. Thus, read ability is a central cue for its usefulness. Text that is not readable may cause difficulties for readers and is more likely to be disregarded or evaluated unfavorably [31]. A useful report should be understandable to readers so that they can extract information from the text. Thus, we propose that.

Hypothesis 2b. Crowd testing reports with higher readability are more useful to readers.

Most of the products in crowd testing are experience products. Browsers would perceive the suppositional experience of using the product according to the information in the testing reports. However, information processing requires some effort on the part of the reader. The prevalence of online information and the ever-growing difficulty of judging information quality result in the increasing need for users to reduce cognitive costs [45]. Users will not put too much effort into further information processing when complex text imposes a heavy processing burden. Thus, we propose that.

Hypothesis 2c. Crowd testing reports that require more processing effort are less useful to readers.

Sentiment that indicates the tester's attitude toward the tested product enhances the completeness of the information and ultimately reduces information asymmetry and potential risks [6]. However, the valence and volume of e-WOM are usually provided at an aggregated level. Fake reviews that purport to reflect actual user experience are used as a promoting strategy to mislead customers, which impedes consumers from collecting truthful information to make decisions [46]. Fake reviews are commonly assumed to be more exaggerated than authentic reviews [47]. Previous literature has suggested that when consumers encounter too many positive reviews about a product, they may doubt its credibility [46].

Hypothesis 2d. Crowd testing reports with more positive sentiment are less useful to readers.

Sentiments from online word-of-mouth are often controversial [46]. Emotional content reflects the subjective feelings that consumers expe rience during the consumption of products or services [48]. According to the negativity bias effect in psychology, people tend to place more weight on negative information than neutral or positive information [49]. Negative sentiment, although it tends to be much rarer than pos itive sentiment, is considered more diagnostic and thus can adversely affect attitudes and purchasing intentions [50]. The literature on online reviews echoes the argument that negative reviews have the potential to influence the attitude and behaviors of future customers to a greater extent than positive reviews [51,52].

Hypothesis 2e. Crowd testing reports with more negative sentiment are more useful to readers.

## 3.2. Uncertainty Reduction Theory (URT) and the effect of parallel tests

Compared to in-store shopping, customers are separated from re tailers and products in time and space in an online shopping environ ment. Merchants and retailers have more access to information about the product than online customers in the market. Information asym metry makes customers with missing information in disadvantaged po sitions suffer from uncertainty and risks of loss. Uncertainty reduction theory proposes that individuals tend to reduce uncertainty and increase predictability through active, passive, and interactive strategies [14]. A decrease in uncertainty results in a decrease in perceived risk, leading to an increase in trust. Accordingly, in the online shopping context, cus tomers tend to seek more information and focus on reducing uncertainty [53].

Inferenced by uncertainty reduction theory, the lack of information about a product on the market is a disincentive for potential customers to make purchasing decisions. Thus, the essence of the product diffusion process is the product information exchanged by which one individual communicates a new product to one or several others [11]. To fully present the characteristics of the tested product, some testers would test it and its congeneric products so as to compare their advantages as well as the disadvantages in manifold features. Through such a practice, the features of a relatively unfamiliar testing product can be analogized to its popular competitors that are familiar to customers. This work especially for newly launched products considering that it sharply re duces uncertainty about the new product. Thus, we propose that.

Hypothesis 3. Crowd testing reports with more parallel tests of competing products are more useful to readers.

## 3.3. The peer competition and its moderating effect

Crowd behavior is driven by human-to-human interactions. The value of implementing crowdsourcing practice in problem solving lies in the aggregation of wisdom from a crowd [33]. Competition is a key characteristic in any crowdsourcing practice that influences how the crowd allocates their effort and achieves the desired performance [54]. Peer effects might be viewed as the effects of competitive challenges [55]. The increasing number of peers increases the competition intensity and makes it more difficult for subsequent users to stand out from their peers [15]. An individual can be influenced by peers. However, the influencing mechanism of peer presence on individual performance re mains controversial. Some scholars demonstrate that performance im proves in response to the incentives of peer competition [56]. Others argue that the average performance of peers has a significant negative effect on an individual's performance [57].

In most crowd testing projects, the enterprises release free samples to more than one tester to motivate more individuals to participate in this crowd behavior. As a result, several testing reports are functioning as counterparts for a single product. On the one hand, this action effec tively increases the information available on the product. On the other hand. these peer testers' reports produce peer effects on each other. Competition intensifies among the testers since potential consumers are provided with extra information sources (e.g., there are several reports for the same products). Performance tends to increase in response to competitive challenges due to peer competition [55]. Better perfor mance is necessary to survive in a competitive environment [58]. Ad vantages would lose their preponderance and mistakes are costlier.

Potential customers prefer reports with large information amounts because they contain a thorough analysis of a product, its features, and the context in which it was used [30]. However, when multiple testers try out the same testing product, their reports may be interchangeable with each other. Missing information in one report can be accessed in the report of its peer testers. The advantage of providing more infor mation is offset by the accessibility of its alternatives.

Hypothesis 4a. The number of peer testers' reports on the focal product mitigates the positive effect of the text's information amount on the report's perceived usefulness.

A crowd testing report with high readability makes it easy to obtain information so that it is favored by readers [31]. Peer testers' reports provide readers with more information sources of the same product. Peer testers' reports increase the number of options available, thereby reducing the cost of information acquisition and promoting competition among peer testers' reports. When they are faced with various choices, readers adopt stricter criteria when evaluating these reports [58]. Thus, we assume that readability would suffer from a loss of competitivenes under the competition of peer testers' reports.

Hypothesis 4b. The number of peer tester s' reports on the focal product mitigates the positive effect of text readability on the report's perceived usefulness.

Crowd testing reports that require much information processing ef fect would impose an extra burden on readers. Information processing is discouraged when the additional effort anticipated exceeds the incre mental value expected from extra text [52]. The presence of peer testers reports lowers the expected cost for readers to obtain information from other sources. Thus, peer competition would increase the downside of information process effort as a disobliged characteristic.

Hypothesis 4c. The number of peer testers' reports on the focal product magnifies the negative effect of information process effort in the report text on the report's perceived usefulness.

Crowd testing reports with exaggerated positive sentiment may be regarded as fake [47], which is not preferred by readers. Peer testers' reports provide potential customers with more choices of information sources. They can easily turn to other reports about the same testing report if they regard a certain information source as unreliable. The reduction of switching costs leads readers to adopt stricter criteria when evaluating these reports [58]. Thus, the negative effect of sharing much positive sentiment would be magnified.

Hypothesis 4d. The number of peer testers' reports on the focal product magnifies the negative effect of positive sentiment in the report text on the report's perceived usefulness.

Peer testers' reports on the same focal product effectively increase the amount of information available on the testing product, making it easier for interested customers to evaluate it. Compared with positive sentiment, negative sentiment is considered more diagnostic and thus can be more useful in affecting attitudes and purchasing intentions [50]. With the competition of peer testers' reports, abundant information sources reduce the difficulty customers face when making purchase decisions. Thus, we assume that negative sentiment loses popularity as consumers' demand escalates for reports of higher quality.

Hypothesis 4e. The number of peer testers' reports on the focal product mitigates the positive effect of negative sentiment in the report text on the report's perceived usefulness.

Parallel tests introduce unfamiliar products through people's famil iarity with their popular competitors. Therefore, it can vividly reflect the characteristics of the testing product. It is useful to potential customers because it helps reduce uncertainty in online shopping [53]. However, when peer testers' reports are available to readers, they have various information sources to acquire details about the testing product. The parallel test no longer has an exclusive feature. To conclude, as the available information increases because of the peer testers' reports, the positive effect of parallel tests on the report's perceived usefulness decreases.

Hypothesis 4f. The number of peer testers' reports on the focal product mitigates the positive effect of parallel tests on the report's perceived usefulness.

## 4. Research method

We extracted secondary data from a popular crowd testing platform, Dealmoon, for empirical analysis. Text mining methods were adopted to extract text features from the reports. Negative binomial regression was applied to analyze the data and test the research framework.

## 4.1. Research context

Dealmoon.com, launched in the year 2009, operates the leading social shopping community as well as an e-commerce advisory platform for global consumer brands. In September 2016, Dealmoon launched its crowd testing channel. Originally, testers were mainly selected by the website operating crew. All reports are published by the site officials. In February 2017, Dealmoon opened the crowd testing channel to the public so that all patrons of the website could apply to become a crowd tester. Selected applicants would receive the testing product and publish testing reports after they try it out. Testing reports on Dealmoon become remarkably diversified thereafter due to the distinguished testers' per sonal styles.

## 4.2. Data collection and variable measures

We developed a web crawler to collect information on all crowd testing reports on Dealmoon. The crowd test products are classified into eight categories: beauty, food, at home, clothing/jewelry/bags, elec tronics, baby/kids, travel, and automotive. Crowd tests in travel and automotive are executed in a completely different pattern, and we excluded these two categories from the data set for analysis. Since crowd testing before February 2017 is closed to the public, the alpha test in siders cannot represent real customer behavior. We also excluded these reports from the analysis in the statistical model along with reports that contained missing values (product information, author information, publication date, etc.). Finally, we obtained 1546 crowd testing reports, including 468 tests in beauty, 140 tests in food, 391 tests in home ap pliances, 330 tests in clothing/jewelry/bags, 188 tests in electronics, and 29 tests in baby/kids. The attributes of each report include the author who published it, the product being tested, a product description, publication date, and statistical data on the report.

We use “Like”, a numerical variable representing the number of users who like certain testing reports, as the dependent variable. The inde pendent variables are categorized into three dimensions: author attri butes, text quality, and other control variables, which include the days after the reports are published and the type and price of the product being tested.

For the text attributes, we ran text mining algorithms to extract text features from the report [29]. First, word segmentation was conducted to separate sentences into words – usually the very first step for the natural language process. After that, the dictionary of C-LIWC was used for psychological analysis. We counted various structural composition elements, such as positive emotions, negative emotions, and cognitive/ perceptive processes. The ratio of each element was calculated as the text feature.

We then employed the Gunning Fog Index, considered as an accurate readability formula, 0.4\*(average sentence length + percentage of hard words) [59]. It assesses reading grade levels needed to understand the text. For example, a Gunning Fog Index of 6 is equivalent to the reading comprehension of a grade 6 student, and a Gunning Fog Index of 20 is equivalent to that of a college or university graduate [59].

Crowd testing reports can serve as a direct source of information about the tested product, especially for those that are new to the market without any word-of-mouth. Thus, the crowd testing report of newly launched products is expected to be particularly useful to potential customers. We take NewProduct as a control variable which is measured by whether the tested product is a brand-new product or a soon-to-bereleased product that is unfamiliar to the market. An updated or spe cial version of an on-market product is excluded considering it is not brand new to the market without any customer base.

The definitions and descriptive statistics of the numerical variables are listed in Table 3. The statistics show that the variables have varying scales. Thus, we normalized the dependent variables using the z-score to transform the data to comparable scales in the subsequent analysis.

Test is the number of crowd tests the author has attended before. Article and Sharing refer to the author's previous experience in publishing all kinds of articles, such as buying guides, reviews, and even life sharing articles. Level is an indicator of the author's general behavior on the website. All four variables represent the author's past experience. Adopting them simultaneously into the model might cause information redundancy and lead to a multi-collinearity problem. Thus, we con ducted a principal component analysis (PCA) to extract the principal component from these four variables. The KMO is 0.623, larger than the acceptable point of 0.5. The p-value is 0.000, which confirms that the PCA method is effective.

The results of PCA are shown in Table 4. We extracted one compo nent with eigenvalues larger than one and named it Expertise. Its cu mulative variance proportion is 72.219%, which confirms that the principal component can explain most of the information in the dataset. After that, we obtained coefficients related to the four standardized in dependent variables to create expressions of the components as: Exper tis $\begin{array} { r } { \mathrm { ~  ~ \xi ~ } _ { 2 } = 0 . 5 4 8 ^ { * } L e \nu e l + 0 . 5 0 1 ^ { * } A r t i c l e + 0 . 4 2 8 ^ { * } T e s t + 0 . 5 1 6 ^ { * } S h } \end{array}$ haring. Since it accounts for a high proportion of the total variance, we use Expertise as the indicator representing the report author's expertise in our subse quent analysis.

To further avoid the multi-collinearity issue, we estimated the cor relation coefficients among all numeric variables. All the correlation coefficients are less than 0.6 (See Table 5). The VIF values of all explanatory variables are less than 10, which disconfirms the multicollinearity among variables.

## 4.3. Model specification

For each online testing report, the usefulness of the testing report is measured by how many times it is “Liked”. In this study, we applied negative binomial regression to test the research framework since the dependable variable is a count variable and the variance of the dependable variable (950.659) is much larger than its mean (26.678). Thus, the baseline model of this study is Eq. (1).

$$
\text { Like } = \alpha + \beta_ {1} \text { AUTHOR } + \beta_ {2} \text { TEXT } + \beta_ {3} \text { CONTROLS } + \varepsilon\tag{1}
$$

AUTHOR is a set of variables relating to the author's attribute, including Expertise, Follower, and Followed. TEXT has five parts: text emotions (Posemo and Negemo), text expression (Process), information amount (Wordcount), text readability (Fogindex), and content (Paral leltest). CONTROLS is the control variable, namely Pictures, Days, Price, Newproduct, and the entity fixed effects of Type. The Eq. (2) is used to estimate the effect of the crowd testers' credibility and the quality of the crowd testing reports.

Table 3  
Definitions and descriptive statistics of numerical variables.

<table><tr><td>Dimension</td><td>Variable</td><td>Definition</td><td>Mean</td><td>S.D.</td><td>Min</td><td>Max</td></tr><tr><td>Dependent Variable</td><td>Like</td><td>The number of likes received by the report</td><td>26.678</td><td>30.833</td><td>0</td><td>233</td></tr><tr><td rowspan="4">Expertise</td><td>Level</td><td>Author&#x27;s level</td><td>9.543</td><td>3.725</td><td>1</td><td>26</td></tr><tr><td>Article</td><td>The number of articles the author has published</td><td>24.603</td><td>31.213</td><td>1</td><td>246</td></tr><tr><td>Sharing</td><td>The number of experiences sharing the author has published</td><td>255.093</td><td>279.832</td><td>0</td><td>1751</td></tr><tr><td>Test</td><td>The number of crowd tests the author has participated in</td><td>5.102</td><td>4.819</td><td>1</td><td>114</td></tr><tr><td rowspan="2">Socialization</td><td>Follower</td><td>The number of followers the author has</td><td>910.774</td><td>1486.832</td><td>0</td><td>10,620</td></tr><tr><td>Followed</td><td>The number of accounts the author follows</td><td>56.964</td><td>66.681</td><td>0</td><td>1225</td></tr><tr><td rowspan="2">Emotion</td><td>Posemo</td><td>The proportion of words expressing positive emotion</td><td>0.023</td><td>0.009</td><td>0.003</td><td>0.070</td></tr><tr><td>Negemo</td><td>The proportion of words expressing negative emotion</td><td>0.006</td><td>0.003</td><td>0</td><td>0.023</td></tr><tr><td>Expression</td><td>Process</td><td>The proportion of words that need cognitive/perceptive process to understand</td><td>0.037</td><td>0.014</td><td>0.004</td><td>0.118</td></tr><tr><td>Information Amount</td><td>Wordcount</td><td>The number of words in the reports</td><td>1175.513</td><td>640.868</td><td>44</td><td>5805</td></tr><tr><td>Readability</td><td>Fogindex</td><td>The readability of the report according to the Gunning Fog Index</td><td>8.214</td><td>4.076</td><td>0.558</td><td>69.74</td></tr><tr><td>Content</td><td>Paralleltest</td><td>Whether the report contains parallel tests with competing products</td><td>0.086</td><td>0.280</td><td>0</td><td>1</td></tr><tr><td>Moderator</td><td>Peer</td><td>The number of reports relating to the same product</td><td>7.986</td><td>7.353</td><td>1</td><td>32</td></tr><tr><td rowspan="4">Controls</td><td>Picture</td><td>The number of pictures in the report</td><td>22.716</td><td>17.269</td><td>0</td><td>210</td></tr><tr><td>Days</td><td>Elapsed days since the publishing date</td><td>346.441</td><td>228.851</td><td>4</td><td>941</td></tr><tr><td>Price</td><td>The price of the product being tested</td><td>177.174</td><td>215.306</td><td>11.99</td><td>1700</td></tr><tr><td>Newproduct</td><td>Whether the tested product is new to the market</td><td>0.105</td><td>0.306</td><td>0</td><td>1</td></tr></table>

To estimate the moderating role of peer testers, we come up with Eq. (3). PEER stands for the number of peer testers' reports relating to the same product.

$$
\begin{array}{r l} \text { Like } & = \alpha + \beta_ {1} \text { AUTHOR } + \beta_ {2} \text { TEXT } + \beta_ {3} \text { PEER } + \beta_ {4} \text { TEXT } ^ {*} \text { PEER } \\ & + \beta_ {5} \text { CONTROLS } + \varepsilon \end{array}\tag{3}
$$

Accordingly, Eq. (4) is used to investigate how peer testers' reports on the focal product moderate the effect of crowd testers' credibility and the quality of the crowd testing report on its usefulness.

about the report text are respectively added. Table 6 shows the esti mated results of the usefulness of the crowd testing reports. The pseudo $\mathrm { R } ^ { 2 }$ and Chi-square are also reported. The model performance was improved as more variables were added to the model.

Testing reports from authors with expertise are more likely to be Liked $( \beta = 0 . 0 9 2 8 , p = 0 . 0 0 2 )$ . Additionally, authors with more fol lowers $( \beta = 0 . 3 8 1 , p = 0 . 0 0 0 )$ and accounts followed $( \beta = 0 . 1 6 5 , \rho =$ 0.000) received more Likes for testing reports. Thus, H1a and H1b are supported.

Readers prefer long reports because they contain more valuable in

$L i k e = \alpha + \beta _ { I }$ Expertise ${ } _ { - \beta _ { 2 } }$ Follower $+ \beta _ { 3 }$ Followed $+ \beta _ { 4 }$ Posemo $+ \beta _ { 5 }$ Negemo $+ \beta _ { 6 }$ Process $+ \beta _ { 7 }$ Wordcount $+ \beta _ { g }$ Fogindex+ ${ } _ { - \beta _ { 9 } }$ Paralleltest ${ } - \beta _ { I O }$ Peer $+ \beta _ { I I }$ Posemo\*Peer $+ \beta _ { I 2 }$ Negemo\*Peer $+ \beta _ { I 3 }$ Process\*Peer $+ \beta _ { I 4 }$ Wordcount\*Peer $+ \beta _ { I 5 }$ Fogindex\*Peer $- \beta _ { I 6 }$ Paralleltest\*Peer $- \beta _ { I 7 }$ Pictures+ $- \beta _ { I 8 }$ Days $+ \beta _ { I 9 } P r i c e + \beta _ { 2 0 }$ Newproduct+θ Type +ε (4)

## 5. Empirical results

We present the results of the statistical model in this section. The focal results are used to test H1a, H1b, H2a. H2b, H2c, H2b, H2e, and H3. The results on the moderating effect of peer testers' reports on the focal product are used to test H4a, H4b, H4c, H4d, H4e, and H4f. Then, a robustness check was carried out.

To ensure that the final explanatory variables are the optimal set, this paper adopts stepwise regression [60]. In the first attempt, only vari ables relating to the report author are included. After that. variables

## 5.1. The focal results

formation $( \beta = 0 . 1 0 6 , p = 0 . 0 0 0 )$ . Thus, H2a is supported. The Gunning Fog Index gives the number of years of education that the reader hy pothetically needs to understand the paragraph or text. A large Fog index means that the text is hard to read. The negative coefficient of the Fog Index $( \beta = - 0 . 0 4 9 1 , p = 0 . 0 3 6 )$ means that readers prefer the report if it is easily understood. Thus, H2b is supported. Heavy information processing effort would cause a burden to the readers and thus nega tively influence the usefulness of the report $( \beta = - 0 . 1 1 9 , p = 0 . 0 0 0 )$ . Thus, H2c is supported. Positive reports may be regarded as fake reviews and are not preferred $( \beta = - 0 . 3 0 4 , \ p = 0 . 0 0 0 )$ . The use of positive sentiment, as an accepted social norm, does not improve a review's usefulness. Hypothesis H2d is supported. In contrast, negative online reviews are generally more attention-grabbing and receive greater scrutiny, thus being perceived as more useful [45]. Reports that contain negative sentiment are favored by viewers $( \beta = 0 . 0 7 0 2 , p = 0 . 0 0 2 )$ Thus, H2e is supported.

Table 4  
Eigenvalue and contribution rate.

<table><tr><td rowspan="2">Principal component</td><td colspan="3">Initial eigenvalues</td><td colspan="3">Extraction sum of squared loadings</td><td colspan="4">Coefficient</td></tr><tr><td>Total</td><td>% of Variable</td><td>Cumulative %</td><td>Total</td><td>% of Variable</td><td>Cumulative %</td><td>Level</td><td>Article</td><td>Test</td><td>Sharing</td></tr><tr><td>1</td><td>2.889</td><td>72.219</td><td>72.219</td><td>2.889</td><td>72.219</td><td>72.219</td><td>0.548</td><td>0.501</td><td>0.428</td><td>0.516</td></tr><tr><td>2</td><td>0.623</td><td>15.583</td><td>87.801</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>0.318</td><td>7.95</td><td>95.752</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>0.17</td><td>4.248</td><td>100</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Table 5 Correlation test.

<table><tr><td colspan="2"></td><td>VIF</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td></tr><tr><td>1</td><td>Like</td><td></td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>Expertise</td><td>1.62</td><td>0.286</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>Follower</td><td>1.41</td><td>0.475</td><td>0.367</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>Followed</td><td>1.19</td><td>0.230</td><td>0.533</td><td>0.229</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5</td><td>Posemo</td><td>1.08</td><td>-0.029</td><td>0.030</td><td>0.048</td><td>0.049</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6</td><td>Negemo</td><td>1.07</td><td>-0.022</td><td>-0.075</td><td>-0.053</td><td>-0.045</td><td>0.085</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7</td><td>Process</td><td>1.05</td><td>0.020</td><td>0.068</td><td>0.070</td><td>0.058</td><td>0.124</td><td>0.075</td><td>1.000</td><td></td><td></td><td></td><td></td></tr><tr><td>8</td><td>Wordcount</td><td>1.05</td><td>0.195</td><td>0.199</td><td>0.002</td><td>0.070</td><td>-0.068</td><td>0.008</td><td>0.031</td><td>1.000</td><td></td><td></td><td></td></tr><tr><td>9</td><td>Fogindex</td><td>1.04</td><td>0.014</td><td>-0.062</td><td>0.044</td><td>-0.037</td><td>0.022</td><td>0.011</td><td>0.029</td><td>0.019</td><td>1.000</td><td></td><td></td></tr><tr><td>10</td><td>Paralleltest</td><td>1.02</td><td>0.135</td><td>0.037</td><td>0.030</td><td>-0.020</td><td>-0.036</td><td>0.013</td><td>0.068</td><td>0.095</td><td>-0.016</td><td>1.000</td><td></td></tr><tr><td>11</td><td>Peer</td><td>1.01</td><td>-0.190</td><td>-0.060</td><td>-0.131</td><td>-0.030</td><td>0.064</td><td>-0.061</td><td>-0.126</td><td>-0.099</td><td>-0.021</td><td>-0.180</td><td>1.000</td></tr></table>

Paralleltest is positively related to the Like number received by a report $( \beta = 0 . 1 1 4 , \ p = 0 . 0 0 0 )$ . Crowd testing reports with parallel tests with competing products are favored by readers. Thus, H3 is supported.

## 5.2. The moderating effect of peer Testers' reports

We still adopt stepwise regression to ensure the optimal set of the final explanatory variables [60]. The first model is the baseline without moderators. The moderating effect of peer testers' reports on text quality has been added in the following model. Table 7 shows the results of the moderating effect of peer testers' reports on the focal product. The pseudo $\mathtt { R } ^ { 2 }$ and Chi-square are successively improved with the addition of independent variables, which confirms the model performance improvement.

Peer testers' reports mitigate the effect of report length on report usefulness $( \beta = - 0 . 0 1 7 8 , p = 0 . 0 2 6 )$ . Thus, H4a is supported. Peer tes ters' reports mitigated the effect of readability $( \beta = - 0 . 0 2 8 8 , p = 0 . 0 3 2 )$ Thus, H4b is supported. The moderating effect of peer testers' reports on the effect of Process is $( \beta = 0 . 1 0 4 , p = 0 . 0 0 0 )$ . Thus, H4c is supported.

The estimated results of like.

<table><tr><td></td><td>Model 1</td><td>Model 2</td><td>Model 3</td></tr><tr><td>Expertise</td><td>0.123***(0.0304)</td><td>0.0914**(0.0307)</td><td>0.0928**(0.0303)</td></tr><tr><td>Follower</td><td>0.374***(0.0292)</td><td>0.395***(0.0293)</td><td>0.381***(0.0289)</td></tr><tr><td>Followed</td><td>0.141***(0.0309)</td><td>0.158***(0.0310)</td><td>0.165***(0.0307)</td></tr><tr><td>Posemo</td><td></td><td>-0.320***(0.0233)</td><td>-0.304***(0.0231)</td></tr><tr><td>Negemo</td><td></td><td>0.0432*(0.0218)</td><td>0.0702**(0.0217)</td></tr><tr><td>Process</td><td></td><td>-0.136***(0.0239)</td><td>-0.119***(0.0237)</td></tr><tr><td>Wordcount</td><td></td><td>0.123***(0.0221)</td><td>0.106***(0.0224)</td></tr><tr><td>Fogindex</td><td></td><td>-0.0475*(0.0237)</td><td>-0.0491*(0.0235)</td></tr><tr><td>Paralleltest</td><td></td><td></td><td>0.114***(0.0217)</td></tr><tr><td>Pictures</td><td>0.246***(0.0271)</td><td>0.204***(0.0274)</td><td>0.206***(0.0272)</td></tr><tr><td>Days</td><td>0.275***(0.0220)</td><td>0.261***(0.0221)</td><td>0.249***(0.0222)</td></tr><tr><td>Price</td><td>0.109***(0.0250)</td><td>0.0902***(0.0250)</td><td>0.0913***(0.0246)</td></tr><tr><td>Newproduct</td><td>0.0457*(0.0225)</td><td>0.0462*(0.0223)</td><td>0.0462*(0.0222)</td></tr><tr><td>Product type dummies</td><td>Included</td><td>Included</td><td>Included</td></tr><tr><td>_cons</td><td>3.273***(0.0433)</td><td>3.259***(0.0449)</td><td>3.263***(0.0446)</td></tr><tr><td>N</td><td>1546</td><td>1546</td><td>1546</td></tr><tr><td>pseudo  $R^2$ </td><td>0.053</td><td>0.056</td><td>0.058</td></tr><tr><td>Chi-squared</td><td>706.1</td><td>745.5</td><td>775.3</td></tr></table>

Standard errors in parentheses: \* p < 0.05, \*\* p < 0.01, \*\*\* p < 0.001.

Peer testers' reports will enhance the negative effect of positive senti ment $( \beta = 0 . 0 9 2 5 , p = 0 . 0 0 0 )$ in the report on its usefulness while softening the positive effect of negative sentiment $( \beta = - 0 . 0 6 2 8 , p =$ 0.005). Crowd testing reports containing much positive emotional content may encourage the feeling that the report is an advertisement instead of sharing a real experience, which would be objectionable to potential customers and aggravate the negative effect of the report. At the same time, strong negative opinions would convey poor impressions to customers that the product or service is not favorable. Thus, peer testers' reports ameliorate the positive effect of negative emotions in testing reports. Thus, H4d and H4e are supported.

At the same time, peer testers' reports mitigate the effect of parallel tests on report usefulness $( \beta \ = \ - 0 . 2 2 8 , \ \ p \ = \ 0 . 0 0 0 )$ . Thus, H4f is supported.

## 5.3. Robustness checks

To avoid the contingency of the results, this paper conducts robust ness checks with alternative dependent variables. For the baseline model, the number of likes received by a report is regarded as the indi cator of its usefulness. On the crowd testing platform, there are book marks and other sharing functions for users to express their feelings about the report. However, a high-quality report consistently earns more attention from platform users and third-party viewers. Thus, for robustness checks, we take the number of bookmarks, the number of shares, the number of views, and the number of comments as dependent variables respectively, instead of the number of likes used in the original model. We applied the negative binomial regression model by replacing the number of Likes with these four variables. Table 8 shows that the results are consistent with our research model, which makes our findings robust.

## 6. Discussions and conclusions

Crowd testing has appeared in recent years on e-retailing platforms and has been regarded as a credible information source for new prod ucts. As an effective marketing tool, crowd testing reports become preferred sources for young consumers to seek for online products. By means of vivid presentation and detailed description of upcoming products, this new business model intrigues online consumers to expe rience products that are new to the market. Crowd testing expectedly aggregates the promotion effects when quite a few peer testers' reports are available for the readers to select an appropriate product and make purchase decisions.

In e-commerce markets, consumers are often uncertain of new product quality and function details and thus hesitate to make purchase decisions in the early introduction period of the product lifecycle. A crowd testing strategy that offers free samples of new products reduces consumers' uncertainty and often has a greater impact on sales than other traditional marketing tools such as advertising [19]. Furthermore, crowd testing enables testers to share their personal experiences and intrigue their readers' interests in new products. In terms of the exten siveness, profundity, and intensity of marketing, the effects of online crowd testing programs have greatly enhanced promotion effects compared to traditional in-store product trials.

Table 7  
The moderating effect of peer testers' report.

<table><tr><td></td><td>Model 1</td><td>Model 2</td><td>Model 3</td></tr><tr><td>Expertise</td><td>0.0979**(0.0299)</td><td>0.0970**(0.0298)</td><td>0.0960**(0.0296)</td></tr><tr><td>Follower</td><td>0.355***(0.0284)</td><td>0.371***(0.0286)</td><td>0.380***(0.0286)</td></tr><tr><td>Followed</td><td>0.166***(0.0305)</td><td>0.157***(0.0304)</td><td>0.157***(0.0302)</td></tr><tr><td>Wordcount</td><td>0.0994***(0.0221)</td><td>0.0915***(0.0231)</td><td>0.0873***(0.0232)</td></tr><tr><td>Fogindex</td><td>-0.0449(0.0232)</td><td>-0.0514*(0.0230)</td><td>-0.0509*(0.0228)</td></tr><tr><td>Process</td><td>-0.0806**(0.0236)</td><td>-0.0513**(0.0238)</td><td>-0.0177*(0.0237)</td></tr><tr><td>Posemo</td><td>-0.209***(0.0229)</td><td>-0.192***(0.0227)</td><td>-0.208***(0.0226)</td></tr><tr><td>Negemo</td><td>0.0537*(0.0215)</td><td>0.154***(0.0214)</td><td>0.167***(0.0214)</td></tr><tr><td>Paralleltest</td><td>0.0960***(0.0216)</td><td>0.0895***(0.0215)</td><td>0.0503*(0.0397)</td></tr><tr><td>Peer</td><td>-0.172***(0.0249)</td><td>-0.170***(0.0255)</td><td>-0.234***(0.0302)</td></tr><tr><td>Wordcount*Peer</td><td></td><td>-0.0218*(0.0237)</td><td>-0.0178*(0.0238)</td></tr><tr><td>Fogindex*Peer</td><td></td><td>-0.0493**(0.0231)</td><td>-0.0288*(0.0231)</td></tr><tr><td>Process*Peer</td><td></td><td>0.0875**(0.0252)</td><td>0.104***(0.0252)</td></tr><tr><td>Posemo*Peer</td><td></td><td>0.0957***(0.0217)</td><td>0.0925***(0.0217)</td></tr><tr><td>Negemo*Peer</td><td></td><td>-0.0610**(0.0224)</td><td>-0.0628**(0.0224)</td></tr><tr><td>Paralleltest*Peer</td><td></td><td></td><td>-0.228***(0.0582)</td></tr><tr><td>Pictures</td><td>0.199***(0.0270)</td><td>0.203***(0.0269)</td><td>0.199***(0.0268)</td></tr><tr><td>Days</td><td>0.220***(0.0223)</td><td>0.222***(0.0223)</td><td>0.215***(0.0223)</td></tr><tr><td>Price</td><td>0.0767**(0.0240)</td><td>0.0766**(0.0239)</td><td>0.0789***(0.0239)</td></tr><tr><td>Newproduct</td><td>0.0457*(0.0219)</td><td>0.0441*(0.0218)</td><td>0.0466*(0.0217)</td></tr><tr><td>Product type dummies</td><td>Included</td><td>Included</td><td>Included</td></tr><tr><td>_cons</td><td>3.251***(0.0442)</td><td>3.232***(0.0449)</td><td>3.188***(0.0461)</td></tr><tr><td>N</td><td>1546</td><td>1546</td><td>1546</td></tr><tr><td>pseudo  $R^2$ </td><td>0.062</td><td>0.064</td><td>0.065</td></tr><tr><td>Chi-squared</td><td>820.3</td><td>846.7</td><td>860.6</td></tr></table>

Standard errors in parentheses: $^ { * } p < 0 . 0 5 ,$ $p < 0 . 0 1 ,$ \*\*\* $p < 0 . 0 0 1$

This paper identifies the determinants of the perceived usefulness of crowd testing reports. The results show that high-level, experienced testers are more likely to be internet influencers on the crowd testing platform and gain more popularity from their test. In addition to positive emotions, the cognitive process and the perceptive process in the report texts decrease the perceived usefulness of the report. For example, a crowd testing report brimming with praise or rigorous logical expression may be regarded as an advertisement from a paid supporter instead of real experience from a random crowd tester. It is against the original intention of informing potential customers of the tested product's quality and functions. Thus, a comprehensive description with both the pros and cons of the product is what potential customers need instead. Mean while, report length and text readability have significant positive im pacts on perceived report usefulness. Readers prefer reports with parallel tests with competing products. The number of peer testers moderates the effect of the perceived quality of the testing report on its usefulness.

This paper integrates the theoretical foundations of the information adaption model, uncertainty reduction theory, and peer competition to propose a framework to understand the usefulness of crowd testing re ports. The findings contribute to the literature on e-WOM in online marketing strategy for the newly launched product and its product diffusion, exploring the content-related factors for a useful testing report, and extending peer competition to the new perspective of peer testers' reports. Practically, the findings of this paper are instructive to all stakeholders of crowd testing practice, including testers, merchants, and crowd testing platforms.

Table 8  
Robustness checks.

<table><tr><td></td><td>Bookmark</td><td>Comment</td><td>Share</td><td>View</td></tr><tr><td>Expertise</td><td>0.257***(0.0442)</td><td>0.255***(0.0403)</td><td>0.114***(0.0385)</td><td>0.265***(0.0358)</td></tr><tr><td>Follower</td><td>0.476***(0.0464)</td><td>0.253***(0.0380)</td><td>0.337***(0.0398)</td><td>0.221***(0.0357)</td></tr><tr><td>Followed</td><td>0.256*(0.0412)</td><td>0.210***(0.0428)</td><td>0.120***(0.0364)</td><td>0.103**(0.0331)</td></tr><tr><td>Wordcount</td><td>0.0957**(0.0359)</td><td>0.0915**(0.0313)</td><td>0.0844**(0.0321)</td><td>0.0573**(0.0275)</td></tr><tr><td>Fogindex</td><td>-0.0621*(0.0348)</td><td>-0.0449*(0.0300)</td><td>-0.0740**(0.0311)</td><td>-0.0849**(0.0277)</td></tr><tr><td>Process</td><td>-0.0655**(0.0362)</td><td>-0.0137(0.0334)</td><td>-0.0574*(0.0327)</td><td>-0.0225(0.0297)</td></tr><tr><td>Posemo</td><td>-0.0473*(0.0357)</td><td>-0.258***(0.0310)</td><td>-0.533***(0.0319)</td><td>-0.0425**(0.0270)</td></tr><tr><td>Negemo</td><td>0.0548**(0.0321)</td><td>0.0624***(0.0297)</td><td>0.0117(0.0299)</td><td>0.0261*(0.0246)</td></tr><tr><td>Paralleltest</td><td>-0.114*(0.0580)</td><td>-0.483***(0.0535)</td><td>-0.611***(0.0524)</td><td>0.0964**(0.0519)</td></tr><tr><td>Peer</td><td>-0.393***(0.0449)</td><td>-0.212***(0.0417)</td><td>-0.427***(0.0416)</td><td>-0.207***(0.0384)</td></tr><tr><td>Wordcount*Peer</td><td>-0.0281(0.0381)</td><td>-0.0239(0.0320)</td><td>-0.0608*(0.0337)</td><td>-0.0792**(0.0274)</td></tr><tr><td>Fogindex*Peer</td><td>-0.0311(0.0342)</td><td>-0.0614**(0.0314)</td><td>-0.0468*(0.0318)</td><td>-0.103***(0.0268)</td></tr><tr><td>Process*Peer</td><td>0.0265(0.0399)</td><td>0.0687*(0.0357)</td><td>0.0188(0.0360)</td><td>0.0401*(0.0336)</td></tr><tr><td>Posemo*Peer</td><td>0.0589(0.0371)</td><td>0.0891**(0.0286)</td><td>0.104**(0.0344)</td><td>0.0477**(0.0269)</td></tr><tr><td>Negemo*Peer</td><td>-0.0722*(0.0344)</td><td>-0.151**(0.0323)</td><td>-0.101**(0.0319)</td><td>-0.0265*(0.0257)</td></tr><tr><td>Picture</td><td>0.193***(0.0415)</td><td>0.305***(0.0396)</td><td>0.188***(0.0372)</td><td>0.0935**(0.0351)</td></tr><tr><td>Days</td><td>0.712***(0.0332)</td><td>0.220***(0.0310)</td><td>0.551***(0.0296)</td><td>0.654***(0.0301)</td></tr><tr><td>Price</td><td>0.0878**(0.0332)</td><td>0.149***(0.0331)</td><td>0.201***(0.0337)</td><td>0.448***(0.0318)</td></tr><tr><td>Newproduct</td><td>0.0539*(0.0326)</td><td>0.0682*(0.0295)</td><td>0.0669*(0.0302)</td><td>0.0398(0.0257)</td></tr><tr><td>Product type dummies</td><td>Included</td><td>Included</td><td>Included</td><td>Included</td></tr><tr><td>_cons</td><td>0.329***(0.0343)</td><td>0.116**(0.0413)</td><td>0.0865*(0.0387)</td><td>-0.110***(0.0320)</td></tr><tr><td>N</td><td>1546</td><td>1546</td><td>1546</td><td>1546</td></tr><tr><td>pseudo  $R^2$ </td><td>0.068</td><td>0.053</td><td>0.087</td><td>0.036</td></tr><tr><td>Chi-squared</td><td>976.8</td><td>590.1</td><td>999.4</td><td>1084.6</td></tr></table>

Standard errors in parentheses: $^ { * } p < 0 . 0 5 ,$ 2 $^ { \ast } p < 0 . 0 1 ,$ $^ { \ast \ast \ast } p < 0 . 0 0 1$

## 6.1. Theoretical implications

This study initiates the examination of crowd testing, which has become popular in recent years. Crowd testing reports are distinct from online reviews from several perspectives, such as the focal product's market status (upcoming product vs. on-the-market product), length of content (long text vs. short text), and testing objects (parallel tests on competing products on market vs. consumed product). However, crowd testing reports have not gained adequate attention in academic research.

Unlike related studies that verify the effects of conducting crowd testing on sales volume [3,5,8], our study focuses on crowd testing re ports and investigates the determinants of the usefulness of crowd testing reports. We find that a crowd testing strategy integrates the advantages of several marketing tactics and innovative business models, such as e-WOM, online crowdsourcing, free trial marketing, and online key opinion leaders' endorsements, to implement new product promo tion. This paper borrows information adoption theory to establish the theoretical framework in light of that readers evaluate crowd testing reports based on information source credibility and information quality. We extract text information based on text mining techniques and extend information quality with image sources. Our proposed research model is tested using secondary data extracted from a popular crowd testing website.

Moreover, this paper examines how crowd behavior impacts the perceived information quality provided by the focal information source. According to peer competition theory, an individual's behavior is influenced by competing peers [55]. However, the effect of peer competition on the behavior of information adoption has not been investigated in the context of e-WOM. Our study contributes to the peer competition literature in which the presence of peer testers of focal products moderates the relationship between information quality and perceived usefulness. The empirical results show the moderating role of peer testers' reports on the determining factors of information quality and available parallel tests. Notably, peer competition moderates the effects of various attributes of information quality in different directions.

## 6.2. Managerial implications

Crowd testing is becoming increasingly popular for online retailers to promote new products and services. This study not only provides novel insights for crowd testers to write a professional testing report but also provides implications for marketers to select successful testers to make their crowd testing program more effective and profitable.

Information quality is a critical predictor of the perceived usefulness of crowd testing reports. Our research also provides an objective crite rion for well-delivered crowd testing reports. Specifically, parallel tests with competing products provide more detailed information about the strengths and weaknesses of the focal product and are thus preferred by readers. Currently, less than 10% of all crowd testing reports contain parallel tests, whereas the perceived usefulness of a crowd testing report with parallel tests can be improved by 11% according to the research findings in this paper. Thus, we encourage the operator to conduct additional crowd testing with parallel tests. The characteristics of testing products can be vividly reflected through the analogy of their popular competitors.

The crowd testing platform functions as a social community in which patrons can develop relationships. All of their behavior on the website, including crowd testing and other sharing articles, conjunctly shapes the social identity in the community. Testers could publish more high quality testing reports as a way to gain influence in the community. Our empirical findings also show that product testing reports published by active, experienced authors with a large fan base easily gain more recognition and higher ratings. This ushers insights for new product marketers looking to select competitive crowd testers from a large pool of applicants to achieve their marketing goals at the lowest possible cost. At the same time, the platform may foster a friendly environment fo patrons to form social relationships.

To achieve the best results when launching crowd testing, merchants usually distribute free samples to a number of selected testers, ranging from 1 to 32. The extra cost of increasing sampling quantity does not guarantee the expected return [12]. This strategy places peer testers reports in an intensively competitive environment. This paper has demonstrated the moderating role of available peer testers' reports on their perceived usefulness of crowd testing reports. The effect of favored characteristics would be mitigated, while the effect of disobliged char acteristics would be magnified. Thus, the merchant should exercise caution when determining the number of free samples.

## 6.3. Limitations and future directions

This paper merely takes into consideration the information source credibility and text quality. Crowd testers also attach pictures to their reports, which convey information more vividly than plain text. We use the number of pictures in a testing report as a control variable in the current research framework. A potential direction for future study would be applying image mining to extract features from the picture with machine learning tools, such as the visual quality and angle coverage, and then estimate the influences of diverse visual content on the usefulness of crowd testing reports.

Another future direction lies in the perspective of the information receiver. A growing number of studies have shown that demographic characteristics (e.g., gender, age, educational background, etc.) of the information receiver are related to their information adoption behavior. We did not add these factors to our model due to the lack of such in formation accessible on the website. Future research can be conducted from the perspective of the information receiver to investigate the similarities and differences between report readers who possess different characteristics in their information adoption process and purchase behavior.

## Credit author statement

Jingxuan Cai: Software, Validation, Resources, Methodology, Formal analysis, Data curation, Writing- Original draft.

Dan Ke: Conceptualization, Investigation, Methodology, Writing Review and editing, Funding acquisition, Project administration.

Jiang Wu: Methodology, Funding acquisition, Visualization

Xin (Robert) Luo: Supervision, Project administration, Writing- Re view and editing.

## Acknowledgments

This research is supported by the Key Program of National Natural Science of China (Grant No. 71832010), National Natural Science Foundation of China (Grant No. 71874131), the Key Projects of Phi losophy and Social Sciences Research at Ministry of Education of China (Grant No. 20JZD024).

## References

[1] M. Sedliacikova, A. Kocianova, M. Dzian, J. Drabek, Product Sampling as a sale Promotion Tool. Marketing and Management of Innovations 1. 2020, pp. 136–148

[2] Z.J. Lin, Y. Zhang, Y. Tan, An empirical study of free product sampling and rating

[3] X.H. Lu, C.W. Phang, S.L. Ba, X.L. Yao, Know who to give: enhancing the effectiveness of online product sampling, Decis. Support. Syst. 105 (2018) 77–86.

[4] Z.S. Wang, H.Y. Liu, W. Liu, S.Y. Wang, Understanding the power of opinion leaders’ influence on the diffusion process of popular mobile games: travel frog on Sina Weibo, Comput. Hum. Behav. 109 (2020) 11.

[5] H. Chen, W.J. Duan, W.Q. Zhou, The interplay between free sampling and word of mouth in the online software market, Decis, Support. Syst. 95 (2017) 82–90.

[6] S. Park, J.L. Nicolau. Asymmetric effects of online consumer reviews, Ann. Tour Res. 50 (2015) 67–83.

[7] L.L. Wu, S.M. Deng, X. Jiang, Sampling and pricing strategy under competition omega-international journal of, Manag, Sci. 80 (2018) 192–208.

[8] C. Schlereth, C. Barrot, B. Skiera, C. Takac, Optimal product-sampling strategies in social networks: how many and whom to target? Int. J. Electron. Commer. 18 (1)

[9] X.L. Yao, X.H. Lu, C.W. Phang, S.L. Ba, Dynamic sales impacts of online physical product sampling, Inf. Manag. 54 (5) (2017) 599–612.

[10] H. Hong, D. Xu, G.A. Wang, W.G. Fan, Understanding the determinants of online review helpfulness: a meta-analytic investigation, Decis. Support. Syst. 102 (2017 1–11.

[11] Z.N. Hu, Y.R. Pei, R.K. Xie, Analysis of product sampling for new product diffusion incorporating multiple-unit ownership, Abstr. Appl. Anal. 2014 (2014) 1–10.

[12] Y.Q. Han, Z.M. Zhang, Impact of free sampling on product diffusion based on bass

[13], I. Erkan, C. Evans. The influence of Ewom in social media on consumers' purchase intentions: an extended approach to information adoption, Comput. Hum. Behav. 61.(2016).47–55

[14] C.R. Berger, R.J. Calabrese, Some explorations in initial interaction and beyond: toward a developmental theory of interpersonal, Communication 1 (2) (1975) 99–112.

[15] X.W. Liu, Z.L. Zhang, R. Law, Z.Q. Zhang, Posting reviews on OTAs: motives, rewards and effort, Tour. Manag. 70 (2019) 230–237.

[16] D. Biswas, D. Grewal, A. Roggeveen, How the order of sampled experientia products affects choice, J. Mark. Res. 47 (3) (2010) 508–519.

[17] D. McGuinness, M. Brennan, P. Gendall, An empirical-test of product sampling and couponing, J. Mark, Res, Soc, 37 (2) (1995) 159–170.

[18] J. Kim, J.D. Morris, The power of affective response and cognitive structure in product-trial attitude formation, J. Advert. 36 (1) (2007) 95–106.

[19] A. Heiman, B. McWilliams, Z.H. Shen, D. Zilberman, Learning and forgetting: modeling optimal product sampling over time, Manag. Sci. 47 (4) (2001) 532–546

[20] F. Li, Z. Yi, Trial or no trial: supplying costly signals to improve profits, Decis. Sci. 48 (4) (2017) 795–827.

[21] H.K. Cheng, Y.P. Liu, Optimal software free trial strategy: the impact of network externalities and consumer uncertainty, Inf. Syst. Res. 23 (2) (2012) 488–504.

[22] Z.N. Hu, W. Wei, J.P. Xu, Dynamic pricing policies and optimal product sampling for the diffusion model of new product, Inform.-an Int. Interdis. J. 15 (8) (2012) 3277-3300.

[23] H.K. Bhargava, R.R. Chen, The benefit of information asymmetry: when to sell to informed customers? Decis. Supp. Syst. 53 (2) (2012) 345–356.

[24] M.D. Rocklage, R.H. Fazio, The enhancing versus backfiring effects of positive emotion in consumer reviews, J. Mark. Res. 57 (2) (2020) 332–352.

[25] D. Yin, S.D. Bond, Z. Han, Anxious or Angry? Effects of Discrete Emotions on the Perceived Helpfulness of Online Reviews, Mis Quarterly 38, 2014, pp. 539–560.

[26] V.L. Tom, E.E. Jennifer, L. Stephan, V.D.H.E. A, What happens in Vegas stays on Tripadvisor? A theory and technique to understand Narrativity in consumer reviews, J. Consum. Res. 46 (2) (2019) 267–285.

[27] A. Agnihotri, S. Bhattacharya, Online review helpfulness: role of qualitative factors, Psychol, Mark, 33 (11) (2016) 1006–1017.

[28] D.Z. Yin, S. Mitra, H. Zhang, When do consumers value positive vs. negative reviews? An empirical investigation of confirmation Bias in online word of mouth, Inf, Syst, Res, 27 (1) (2016) 131–144

[29] M.S.I. Malik, A. Hussain, An analysis of review content and reviewer variables that contribute to review helpfulness, Inf. Process. Manag. 54 (1) (2018) 88–104.

[30] M. Salehan, D.J. Kim, Predicting the performance of online consumer reviews: a sentiment mining approach to big data analytics, Decis. Support. Syst. 81 (2016) 30–40.

[31] K.K.Y. Kuan, K.-L. Hui, P. Prasarnphanich, H.-Y. Lai, What makes a review voted? An empirical investigation of review voting in online review systems, J. Assoc. Inf. Syst, 16 (1) (2015) 48–71.

[32] D.C. Brabham. Crowdsourcing as a model for problem solving an introduction and cases, Converg, Int, J. Res, Into New Media Technol, 14 (1) (2008) 75–90.

[33] D.C. Brabham, Moving the crowd at Threadless motivations for participation in a crowdsourcing application, Inf. Commun. Soc. 13 (8) (2010) 1122–1145.

[34] I. Dissanayake, N. Mehta, P. Palvia, V. Taras, K. Amoako-Gyampah, Competition matters! Self-efficacy, effort, and performance in crowdsourcing teams, Inf. Manag. 56 (8) (2019).

[35] D.C. Liang, W. Cao, Z.S. Xu, M.W. Wang, A novel approach of two-stage three-way co-Opetition decision for crowdsourcing task allocation scheme, Inf. Sci. 559 (2021) 191–211.

[36] B. Morschheuser, J. Hamari, A. Maedche, Cooperation or competition - when do people contribute more? A field experiment on gamification of crowdsourcing, Int. J. Human-Comp. Stud. 127 (2019) 7–24.

[37] D. Liu, X. Li, R. Santhanam, Digital games and beyond: what happens when players compete? MIS Q. 37 (1) (2013) 111–+.

[38] Shelly Chaiken, Heuristic versus systematic information processing and the use of source versus message cues in persuasion, J. Pers. Soc. Psychol. 39 (5) (1980) 752–766.

[39] Y.-H. Cheng, H.-Y. Ho, Social Influence’s impact on reader perceptions of online reviews, J. Bus. Res. 68 (4) (2015) 883–887.

[40] S.A.A. Jin, J. Phua, Following Celebrities’ tweets about brands: the impact of twitter-based electronic word-of-mouth on Consumers’ source credibility perception, Buying Intention, and Social Identification with Celebrities, J. Advert. 43 (2) (2014) 181–195.

[41] A. Benlian, T. Hess, The signaling role of it features in influencing trust and

[42] T. Zhang, G. Li, K.K. Lai, J.W.K. Leung, Information disclosure strategies for the intermediary and competitive sellers, Eur. J. Oper. Res. 271 (3) (2018) 1156–1173.

[43] L. Zhu, G. Yin, W. He, Is this opinion Leader’s review useful? Peripheral Cues for Online Review Helpfulness, J. Electron, Commer, Res, 15 (2014) 267–280

[44] Z. Liu, S. Park, What makes a useful online review? Implication for travel product

[45] S. Liang, M. Schuckert, R. Law, How to improve the stated helpfulness of hotel 953–977.

[46] J.H. Lee, S.H. Jung, J. Park, The role of entropy of review text sentiments on online WoM and movie box office sales, Electron. Commer. Res. Appl. 22 (2017) 42–52.

[47] S. Banerjee, Exaggeration in fake Vs. authentic online reviews for luxury and budget hotels, Int. J. Inf. Manag. 62 (2022).

[48] H.Y. Li, H.B. Liu, Z.L. Zhang, Online persuasion of review emotional intensity: a text mining analysis of restaurant reviews, Int. J. Hosp. Manag. 89 (2020).

[49] P. Rozin, E.B. Royzman, Negativity bias, negativity dominance, and contagion, Personal. Soc. Psychol. Rev. 5 (4) (2001) 296–320.

[50] M.S. Balaji, K.W. Khong, A.Y.L. Chong, Determinants of negative word-of-mouth communication using social networking sites. Inf. Manag. 53 (4) (2016) 528–540

[51] D. Yin, S.D. Bond, H. Zhang, Anxious or angry? Effects of discrete emotions on the perceived helpfulness of online reviews, MIS Q. 38 (2) (2014) 539–560.

[52] H. Li, Z. Zhang, F. Meng, R. Janakiraman, Is peer evaluation of consumer online reviews socially embedded? An examination combining reviewer's social network and social identity, Int. J. Hosp. Manag. 67 (2017) 143–153.

[53] X. Cheng, L. Su, B. Yang, An investigation into sharing economy enabled ridesharing drivers’ trust: a qualitative study, Electron. Commer. Res. Appl. 40 (2020).

[54] I. Dissanayake, N. Mehta, P. Palvia, V. Taras, K. Amoako-Gyampah, Competition matters! Self-efficacy, effort, and performance in crowdsourcing teams, Inf. Manag. 56 (8) (2019) 12.

[55] M. Baldauf, J. Mollner, Pedaling peers: the effect of targets on performance, J. Econ. Behav. Organ. 167 (2019) 90–103.

[56] J. Berger, D. Pope, Can losing lead to winning? Manag. Sci. 57 (5) (2011) 817–827.

[57] C.C. Lee, Team characteristics, peer competition threats and individual performance within a working team: an analysis of realtor agents, South Afr. J. Econ. and Manag. Sci. 17 (2) (2014) 140–156.

[58] R. Hallak, G. Assaker, P. O’Connor, C. Lee, Firm performance in the upscale restaurant sector: the effects of resilience, creative self-efficacy, innovation an industry experience, J. Retail. Consum. Serv. 40 (2018) 229–240.

[59] J.S. Armstrong, Unintelligible management research and academic prestige, Interfaces 10 (2) (1980) 80–86.

[60] H. Song, R. Turson, A. Ganguly, K.K. Yu, Evaluating the effects of supply chain quality management on food Firms’ performance the mediating role of food certification and reputation, Int. J. Oper. Prod. Manag. 37 (10) (2017) 1541–1562.

Jingxuan Cai holds a Ph.D. in management science and engineering at Wuhan University and a master degree at the University of Washington. She is an assistant professor in Dongwu Business School at Soochow University. Her current research interests include machine learning, sharing economy, electronic commerce, etc. One of her research has been published at Decision Support Systems.

Dan Ke is an associate professor in the School of Economics and Management at Wuhan University. She holds a Ph.D. from the School of Business at the University of Connecticut. USA. Her current research interests include virtual worlds economy, digital marketing, business analytics, FinTech and blockchain innovations, etc. She was a recipient of the 2010 Best Information Systems Publications Award (Given by the Association for Infor mation Systems) and her publications has appeared in leading academic journals, including ACM Transactions on Management Information Systems, Decision Sciences, Journal of Business Research, etc.

Jiang Wu is a professor in the School of Information Management at Wuhan University. He holds a Ph.D. from Huazhong University of Science and Technology in Wuhan and a Master from Tsinghua University in Beijing, China. His current research interests include electronic commerce, business analytics, social networks, machine learning, informetrics, etc. His research has been published in journals such as the Journal of Informetrics, Sci entometrics, Journal of the Association for Information Science and Technology, Journal of Knowledge Management, and Decision Support Systems, etc.

Xin (Robert) Luo is an Endowed Regent's Professor and a Full Professor of Management Information Systems and Information Assurance in the Anderson School of Management at the University of New Mexico, Albuquerque, USA. He received his Ph.D. in Management Information Systems from Mississippi State University, USA. His research will or has appeared in leading IS/business journals, including the Information Systems Research Journal of Operations Management, Journal of Management Information Systems, Journal of the Association for Information Systems, European Journal of Information Systems, Information Systems Journal, Journal of Strategic Information Systems, Decision Sciences, Decision Support Systems, Information & Management, and IEEE Transactions on Engineering Management. He has served as an ad hoc Associate Editor for MIS Ougrterly and an Associate Editor for European Journal of Information Systems, and currently serves as an Associate Editor for the Journal of the Association for Information Systems, Decision Sciences, Information & Man agement, Electronic Commerce Research, and the Journal of Electronic Commerce Research. His research interests center around information assurance, innovative technologies for strategic decision-making, and global IT management. He is the Co-Editor-in-Chief for the International Journal of Accounting and Information Management.
