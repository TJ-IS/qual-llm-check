---
otero_id: 14816
otero_key: "T8DSJMEQ"
title: "What's buzzing in the blizzard of buzz? Automotive component isolation in social media postings"
authors: "Alan S. Abrahams; Jian Jiao; Weiguo Fan; G. Alan Wang; Zhongju Zhang"
year: "2013"
journal: "Decision Support Systems"
doi: "10.1016/i.dss.2012.12.023"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# What's buzzing in the blizzard of buzz? Automotive component isolation in social media postings

Alan S. Abrahams <sup>a,</sup>⁎, Jian Jiao <sup>b</sup>, Weiguo Fan <sup>c,e</sup>, G. Alan Wang <sup>a</sup>, Zhongju Zhang d

<sup>a</sup> Department of Business Information Technology, Pamplin College of Business, Virginia Tech, 1007 Pamplin Hall, Blacksburg, VA 24061, United States

<sup>b</sup> Department of Computer Science, Virginia Tech, 114 McBryde Hall, Blacksburg, VA 24061, United States

<sup>c</sup> Department of Accounting and Information Systems, Pamplin College of Business, Virginia Tech, 3007 Pamplin Hall, Blacksburg, VA 24061, United States

<sup>d</sup> Operations and Information Management Department, School of Business, University of Connecticut, 2100 Hillside Road, Unit 1041, Storrs, CT 06269, United States

<sup>e</sup> School of Information, Zhejiang University of Finance and Economics, Hang Zhou, 310018, P.R. China

## a r t i c l e i n f o

Available online 30 December 2012

Keywords: Social media analytics Diagnostics Text mining User-generated content (UGC)

## a b s t r a c t

In the blizzard of social media postings, isolating what is important to a corporation is a huge challenge. In the consumer-related manufacturing industry, for instance, manufacturers and distributors are faced with an unrelenting, accumulating snow of millions of discussion forum postings. In this paper, we describe and evaluate text mining tools for categorizing this user-generated content and distilling valuable intelligence frozen in the mound of postings. Using the automotive industry as an example, we implement and tune the parameters of a text-mining model for component diagnostics from social media. Our model can automatically and accurately isolate the vehicle component that is the subject of a user discussion. The procedure described also rapidly identi<sup>fi</sup>es the most distinctive terms for each component category, which provides further marketing and competitive intelligence to manufacturers, distributors, service centers, and suppliers.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

Hundreds of millions of users are contributing social media content via blogs, product reviews, social networking sites, and content communities on the Internet [45]. Detecting “whispers of useful information in a howling hurricane of noise” is a huge challenge and <sup>fi</sup>lters are needed to extract meaning from the “blizzard of buzz”, prompting automotive companies like Chrysler to employ “Twitter teams” to <sup>fi</sup>nd and reply to complaint-laden tweets [94].

To gain a better understanding of the issues affecting their products, effective <sup>fi</sup>rms must gather product-relevant information both internally and externally [28,32,35]. It is widely accepted that consumer complaints are a valuable source of product intelligence [34,58,75,76]. The knowledge of outsiders or user communities is an important source for product-related business intelligence [5,23,25]. Historically, many companies have invested substantial effort in soliciting product usage stories from practitioners, for the purposes of diagnosing or understanding problems, or allocating issues to technicians that are able to solve them. Especially for <sup>fi</sup>rms selling a mechanical consumer product, these so-called ‘communities of practice’ are an important aspect of a <sup>fi</sup>rm's business intelligence repertoire, as they provide a repository of past usage experiences which can be drawn upon for operational issue resolution, product development, or other purposes [12,20,49,79,90,91].

Monitoring trending topics [11,52,99] and <sup>fi</sup>nding opinionated postings by outspoken customers [2,21,64,86,87] have been attempted in a variety of industries. However, it has recently been shown that, in the motor vehicle industry, customer anger (negative opinion) does not necessarily correlate with defect existence or severity, and specialpurpose tools are required for diagnosing and prioritizing vehicle defects [4]. Pin-pointing the speci<sup>fi</sup>c components referred to in these discussions, is a further issue of concern to automotive corporations, since diagnostic information must map to a sensible, industry-speci<sup>fi</sup>c ontology (or ‘decomposition’) for describing vehicle components, in order for a proper hazard analysis (HA) or failure modes and effects analysis (FMEA) to be performed [43,89].

In this paper, we employ text mining to map automotive enthusiast discussion forum postings to such an ontology: effectively isolating the component under discussion. In the process, we uncover distinctive terminology that relates to each component category, which provides additional marketing and competitive insight to both vehicle and parts manufacturers and distributors.

This paper tackles three major research questions. Firstly, can text mining be employed to automatically isolate the vehicle component category under discussion in an online social media posting? Secondly, if component isolation is feasible, what text mining parameters (algorithm, feature selection method, and number of features/terms) produce optimal classi<sup>fi</sup>cation performance? Finally, what are the distinctive features that discriminate discussion threads that come from different component categories?

The primary contribution of this paper is the development and assessment of a text mining model for vehicle component isolation from discussion forum postings. For nine major component categories, our model is able to accurately pinpoint the component category that is the subject of the postings, with greater than 95% accuracy. In comprehensive evaluations, we determine the parameters (algorithm, feature selection, and number of terms) that appear to provide optimal classi<sup>fi</sup>cation performance. A further contribution of this paper is a consequence of the pursuit of the primary goal: a signi<sup>fi</sup>cant number of the top terms discovered by the feature selection methods are component-speci<sup>fi</sup>c industry jargon terms, or brand names that are active in manufacturing or distributing replacement parts for the component. As we shall illustrate later, our approach can therefore be a helpful source of real-time marketing and competitive intelligence.

While we focus on a speci<sup>fi</sup>c example from the vehicle industry, the method we propose can be generalized to various other industries and problem contexts. For instance, it could be well-suited to component isolation for a multitude of complex manufactured products, such as power tools [32], computers and electronics, <sup>fi</sup>shing gear [33], and other items. Further, while our example speci<sup>fi</sup>cally analyzes discussion threads, these are just one form of social media posting [45] and the techniques are applicable to other forms of social media posting such as user reviews, blog posts, micro-blogs, social media status updates, and feeds (such as RSS feeds [72], Atom feeds [41,42], or Twitter feeds).

The rest of this paper is structured as follows. First, we discuss and contrast related work. We describe our contributions and the research questions we aim to address. We lay out a work<sup>fl</sup>ow for automotive component diagnostics from online discussions. We test our text mining approach in a pilot study and then on a large sample data set. Finally, we discuss limitations, implications, and conclusions.

## 2. Background and related work

In this section, we set out our research motivation. We explore related work on text categorization and on social media analytics. We review the coverage and limitations of prior work, and the research questions raised.

## 2.1. Text categorization

Automated document categorization involves the automated assignment of documents to pre-de<sup>fi</sup>ned categories, and has been well-studied over the past half-century [7,9,13,44,51,95]. Categorization may be guided by a training set of manually tagged documents [50,68,73,82], or may be entirely machine-directed [17,61] using classi<sup>fi</sup>cation-based techniques. In the information retrieval literature, search results (documents) can be partitioned by topic (class) to allow the user of the web search engine to rapidly locate a pertinent document in the user's intended subject area, thereby reducing information overload [18,38,96]. Text categorization problems characteristically have high dimensionality: hundreds of available input attributes, some of which may be highly correlated or violate the assumption of normality. Popular algorithmic approaches to text categorization include Bayesian approaches, decision trees, example-based classi<sup>fi</sup>ers, neural nets, and Support Vector Machines, with the latter (SVMs) showing particularly high performance for text characterization and discrimination tasks when used with a suitable selection of text features [1,82].

## 2.2. Social media analytics

The “social web” has recently received substantial attention [65]. 75% of Internet users have created or read some form of social media content: this user-generated content (UGC) includes blog postings, oduct reviews, social networking sites, and collaborative content [45]. We de<sup>fi</sup>ne social media as online services that provide for decentralized, user level content creation (including editing or tagging), social interaction, and open (public) membership. In our de<sup>fi</sup>nition, public discussion forums, public listservs, public wikis, open online communities (social networks), public usenet groups, customer product reviews, public visitor comments, user-contributed news articles, micro-blogs, and folksonomies would fall within the gamut of social media. Online discussions contain a signi<sup>fi</sup>cant amount of information relating to companies and their product categories [32,33]. Navigation of this content is a signi<sup>fi</sup>cant research challenge [31,39,65] that may require <sup>fi</sup>ltering, semantic content grouping, tagging, information mining, or other techniques.

Social media analytics involves “developing and evaluating informatics tools and frameworks to collect, monitor, analyze, summarize, and visualize social media data, usually driven by speci<sup>fi</sup>c requirements from a target application” [98]. Social media analytics revolves around technologies for web-based social listening, measuring, and monitoring [84]. It is sometimes viewed narrowly as “buzz monitoring”, “reputation monitoring”, or “topic monitoring”. Popular commercial software platforms include Google Trends, Nielsen BlogPulse/BuzzMetrics, TweetDeck, Collective Intellect, TwelveFold Analytics, Clarabridge, Visible Edge, and others. Users of social media analytics include marketing managers who view content trends in the top areas of interest for a target audience, product managers who chart brand or product mentions over time to measure the success of campaigns, or customer service managers (e.g. in hospitality) who monitor user review forums for disappointed or irate customers. Existing buzz monitoring services typically monitor and graph topic mentions and consumer sentiment, with the intention of uncovering trends.

Comparison of text analysis studies using traditional web and social media.

<table><tr><td>Study</td><td>Medium</td><td>Domain</td><td>Output variable</td></tr><tr><td>Coussement and vd. Poel [21]</td><td>Email</td><td>Customer complaints</td><td>Complaint classification</td></tr><tr><td>Spangler and Kreulen [83]</td><td>Email</td><td>Customer complaints</td><td>Issue categorization</td></tr><tr><td>Romano et al. [70]</td><td>Product reviews</td><td>Movie box office</td><td>Film popularity score</td></tr><tr><td>Cao, Duan, and Gan [14]</td><td>Product reviews</td><td>Software</td><td>Helpfulness votes</td></tr><tr><td>Wang, Liu, and Fan [88]</td><td>Online forums</td><td>Consumer electronics</td><td>Helpfulness classification</td></tr><tr><td>Duan, Gu, and Whinston [26]</td><td>Product reviews</td><td>Movie box office</td><td>Estimated revenues</td></tr><tr><td>Abbasi and Chen [1]</td><td>Email</td><td>Enron scandal communications</td><td>Topic, opinion, style, genre, interaction pattern</td></tr><tr><td>Schumaker and Chen [80]</td><td>News articles</td><td>Stock market</td><td>Stock price</td></tr><tr><td>Antweiler and Frank [6]</td><td>Online forums</td><td>Stock market</td><td>Market volatility and trading volume</td></tr><tr><td>Tetlock et al. [85]</td><td>News articles</td><td>Stock market</td><td>Company earnings and stock returns</td></tr><tr><td>Ma, Sheng, and Pant [56]</td><td>News articles</td><td>Stock market</td><td>Comparative revenue</td></tr><tr><td>Ma, Pant, and Sheng [57]</td><td>News articles</td><td>Stock market</td><td>Competitor relationships</td></tr><tr><td>Oh and Sheng [63]</td><td>Micro-blogs</td><td>Stock market</td><td>Directional movement</td></tr><tr><td>Loughran and McDonald [55]</td><td>10-K filings</td><td>Stock market</td><td>Tone (negativity); earnings; volatility; company internal control weakness</td></tr><tr><td>Vechtomova [87]</td><td>Blog postings</td><td>General</td><td>Topic, opinion</td></tr><tr><td>Kolari et al. [47]</td><td>Blog postings</td><td>General</td><td>Spam classification</td></tr><tr><td>Brooks and Montanez [11]</td><td>Blog postings</td><td>General</td><td>Topic</td></tr><tr><td>Santos et al. [77]</td><td>Blog postings</td><td>General</td><td>Relevance, trends</td></tr><tr><td>Li and Wu [52]</td><td>Online forums</td><td>Sports</td><td>Hot (i.e. trending) sports topics</td></tr><tr><td>Zhang et al. [99]</td><td>News articles</td><td>Health epidemics</td><td>Disease news classification</td></tr><tr><td>Wiebe et al. [69,92,93]</td><td>News articles</td><td>News/politics/business/travel/English literature</td><td>Subjectivity</td></tr><tr><td>Finch [32]</td><td>Newsgroup</td><td>Power tools</td><td>Message purpose, tone, product classa</td></tr><tr><td>Finch and Luebbe [33]</td><td>Public listserv</td><td>Fly fishing gear</td><td>Company name, product typea</td></tr><tr><td>Abbasi, Chen, and Salem [2]</td><td>Online forums</td><td>Movie reviews, political talk</td><td>Opinion classification</td></tr><tr><td>Decker and Trusov [24]</td><td>Online product reviews</td><td>Mobile phones</td><td>Sentiment towards each product attribute of each brand</td></tr><tr><td>Abrahams et al. [4]</td><td>Online forums</td><td>Vehicle defects</td><td>Defect existence and criticality</td></tr><tr><td>This study</td><td>Online forums</td><td>Vehicle defects</td><td>Component classification</td></tr></table>

<sup>a</sup> Manual analysis, rather than automated classi<sup>fi</sup>cation, was used in [32,33].

In the academic space, various methods have been proposed for navigating the content (topics) and sentiment of the blogosphere. For example, Kolari et al. [47] introduce tools for automatically identifying reputable blogs and Brooks and Montanez [11] propose a system for automatically tagging blogs by topic. Vechtomova [87] presents a method for retrieving blog posts containing opinions about an entity expressed in the query. Results are classi<sup>fi</sup>ed as either relevant/not-relevant to the target entity and, if relevant, positive or negative in sentiment about the target entity. See [62,77] for a detailed review of social media mining techniques.

Table 1 summarizes previous research on text classi<sup>fi</sup>cation of various types of social media content (product reviews, internet news articles, public regulatory <sup>fi</sup>lings, listservs, emails, newsgroups, blogs, and online discussion forums). To the best of our knowledge, no previous study has focused on product component analysis using social media. The only research stream close to ours studies aggregated quality features extracted from user-generated product reviews, and the users sentiment toward those features [24].

## 2.3. Research gap addressed

In this paper, we investigate the use of text mining for the classi<sup>fi</sup>cation of content (component isolation) from social media postings in the automotive industry. Rapid classi<sup>fi</sup>cation of the components discussed in individual postings, and the identi<sup>fi</sup>cation of signi<sup>fi</sup>cant terms (or more generally, features) for each component class, is helpful for a variety of tasks, such as defect management, and competitive intelligence.

## 3. A process model for text classi<sup>fi</sup>cation and component isolation

Fig. 1 shows the process model for component isolation from social media postings. Again, while our example case revolves around discussion threads in the vehicle industry, the method we propose can be generalized to social media postings in various other industries and problem contexts.

Starting at the top right of Fig. 1, users of an online automobile discussion forum manually choose a relevant sub-forum for their new postings. This is effectively manual component classi<sup>fi</sup>cation. Fig. 2 shows an example of this from a user posting at Honda-Tech.com. Here the user has added their posting to the sub-forum “Honda and Acura Technical Forums>Suspension & Brakes”. The user has provided a manual component classi<sup>fi</sup>cation, by assigning their posting to a component-related sub-forum: “Suspension & Brakes”.

Returning to Fig. 1, each component-related sub-forum is crawled (1.) and terms are extracted (2.). In our study, term extraction involves stemming [66] of the thread text, followed by uni-gram (single word) extraction. However, alternative approaches may involve word-sense-disambiguation [81] and/or part-of-speech tagging, coupled with noun-phrase (n-gram), named entity, verb, or other term extraction methods [16,29]. Term selection (3.) is employed, for each component category, to determine which terms are most signi<sup>fi</sup>cant (unusually prominent, or unusually absent) for that category relative to other categories [30]. Full threads, including component category, and terms, are stored in the discussion database (4.). Text mining (5.) is employed on new social media postings to determine which terms are indicative of which component categories. The results of text mining are two-fold: <sup>fi</sup>rstly, an automated component classi<sup>fi</sup>- cation (6.) for each posting; secondly, a list of signi<sup>fi</sup>cant terms, by component category (7.). In summary, a text mining model is trained on a large sample of discussion threads, organized by category; this process identi<sup>fi</sup>es signi<sup>fi</sup>cant terms for each component category. The text mining model can then be applied to new social media postings to classify each posting, and construct an organized database of postings.

![](/api/attachments/T8DSJMEQ/fulltext/images/964251cedc11479846758e0abd97ec7b9f1a8a3980ae7d25738babb1786de29e.jpg)  
Fig. 1. Process for vehicle component isolation from social media postings.

![](/api/attachments/T8DSJMEQ/fulltext/images/a2ea0a6d1c9bf2c6f1608b7f5f6d5f2e9f98cafab077ef12c77c332403718182.jpg)  
Fig. 2. Example of a user-classi<sup>fi</sup>ed discussion forum posting at Honda-Tech.com.

Automated component classi<sup>fi</sup>cation (6.) is helpful as it allows new social media postings to be rapidly and accurately classi<sup>fi</sup>ed. This facilitates defect prioritization [4], since analysts can segregate safety issues (e.g. relating to brakes) from performance issues (e.g. relating to air conditioning) by mapping the posting to a vehicle component decomposition (i.e. to component classes) [43,89].

The list of signi<sup>fi</sup>cant terms (7.) typically includes the brand names of competitors that market or distribute the component, as well as component-speci<sup>fi</sup>c jargon. Both these items provide additional competitive intelligence to the social media analyst: <sup>fi</sup>rstly, brand names allow the analyst to rapidly identify potential competitors, suppliers, or business partners. Component-speci<sup>fi</sup>c jargon is valuable as it can be used for search engine optimization (SEO) [22] and pay-per-click (PPC) campaign enhancement. For example, for PPC, the use of highlyrelevant jargon words in pay-per-click campaigns is known to increase impressions, decrease cost-per-click (CPC), increase click-through-rate (CTR) and in-bound traf<sup>fi</sup>c, and ultimately lead to higher return-oninvestment [3,36,54,74]. The use of brand names as bid keywords in PPC campaigns can have similar effects [71]. Auto manufacturers and parts suppliers could therefore use the list of signi<sup>fi</sup>cant terms to optimize their pay-per-click campaigns, and to optimize their web-page content to improve their search engine rankings (i.e. SEO).

Finally, descriptive analysis (8.) can be performed. This is useful to analysts working at auto manufacturers, parts suppliers, and car dealers. For example by observing, comparing, and investigating trends in discussions for certain components of certain models or brands, auto manufacturers can feed insights to their product managers, designers, and engineers, who can use this intelligence for benchmarking their vehicles against competitors, or conducting quality improvement. Parts suppliers could use the component isolation tool to compile focused information on speci<sup>fi</sup>c component types. Using the component isolation model as a rapid content discovery and organization tool, auto dealers, dealer networks, and service centers could build a componentspeci<sup>fi</sup>c knowledgebase to assist service technicians with diagnosing and remedying speci<sup>fi</sup>c component failures presented by customers at dealerships. Such categorized experience repositories, or “communities of practice”, have been shown to substantially increase the ef<sup>fi</sup>ciency of technical staff [12,20,49,79,91].

Table 2 Data sources.

<table><tr><td>Forum</td><td>Number of users</td><td>Number of sub-forums</td><td>Total threads</td><td>Sample size (threads)</td></tr><tr><td>Honda Tech</td><td>201,975</td><td>34</td><td>1,316,881</td><td>1500</td></tr><tr><td>Toyota Nation</td><td>78,203</td><td>100</td><td>216,599</td><td>1500</td></tr><tr><td>Chevrolet Forum</td><td>18,498</td><td>48</td><td>26,936</td><td>1500</td></tr></table>

## 4. Methodology

We used a case study approach to validate the process model proposed in the previous section. The case study method of theory building is widely accepted [8,27,37,59,78,97]. We followed a research design consistent with earlier studies on consumer postings [32] and textual content analysis [60].

We began with a small pilot study of 4500 discussion threads, which were tagged by three paid automotive experts. Our intention with the pilot study was to determine what major vehicle components existed, how discussions were dispersed among these components, and how these components related to vehicle defects, for a variety of vehicle brands. We observed that a random sampling of threads yielded a poorly balanced sample: roughly consistent with Koch's 80/20 principle [46], it was found that only 20% of component categories accounted for (more than) 80% of forum postings, leading to too few postings for the majority of component categories. To avoid this bias, which was exacerbated by the high cost of retrospective classi<sup>fi</sup>cation by automotive experts, we undertook strati<sup>fi</sup>ed sampling for the production study.

In the production study, we used 25,000 threads, pre-categorized into one of several component categories by the writer (creator) of the <sup>fi</sup>rst post in the thread, and we selected a roughly even number of threads from each known component category.

The following sections describe the pilot and production studies in more detail.

## 4.1. Pilot study

For the pilot study, we used 15 major component classi<sup>fi</sup>cation labels, abridged from the 339 unique component descriptions used by the National Highway Traf<sup>fi</sup>c Safety Administration, Of<sup>fi</sup>ce of Defect Investigation (NHTSA ODI<sup>1</sup>). For example, the NHTSA provides 45 categories of “Service Brake” complaints and 29 categories of “Power Train (Transmission)” related complaints — we simpli<sup>fi</sup>ed these to the categories “Braking” and “Transmission” respectively. The 15 major component classi<sup>fi</sup>cation labels we used were as follows: [Acoustics], [Air Conditioning], Airbag, Braking, Electrical system, Engine, Lights, Seat Belts, Steering, Structure and Body, Suspension, Transmission, Visibility (Windows), Wheels and Tires, and Other. The categories in square brackets were added as they cover a substantial set of performancerelated defects that are largely ignored by the NHTSA's safety-focused classi<sup>fi</sup>cation scheme.

We studied three different vehicle brands: Honda, Toyota, and Chevrolet. We obtained the permission of the forum owners and crawled all threads available at Honda-Tech.com, ToyotaNation.com, and ChevroletForum.com as of June 2010. We then found the top 1500 threads from each of these three forums, which contained the most occurrences of the top 200 defective components from NHTSA complaints. 1500 was chosen as the sample size that would produce an acceptable margin-of-error of ±2.5% at the 95% con<sup>fi</sup>dence level. We eliminated sub forums about news, racing and advertising because discussions in those forums generally do not relate to defects. To remove short and low quality discussions, we applied two additional criteria: (1) thread contained at least 50 words; and (2) thread comprised at least 2 posts. Table 2 presents summary information related to the three forums.

![](/api/attachments/T8DSJMEQ/fulltext/images/8c407879bcd05ea5d8f5d34a3cc37c4ed2b816ff295988cc4d9d48e1c7eae370.jpg)  
Fig. 3. Total number of threads discussing a defect, by component category.

We extracted the following information from each thread: title, text of each posting, date and time of each posting, user identi<sup>fi</sup>er of each posting, and number of times the thread had been viewed.

We employed three, paid automotive experts to tag the threads by defect existence, defect criticality, and component affected, following the protocol de<sup>fi</sup>ned in [4]. We computed the inter-rater agreement [19] for the component category<sup>2</sup> selected by the raters on the training set, and found $\kappa = 0 . 6 5 ^ { 3 }$ , indicating substantial agreement between raters [48]. Disagreements in component classi<sup>fi</sup>cation were resolved by taking the judgment of the most senior (experienced) rater.

Most of the defect discussions related to the engine, electrical system or transmission; few threads discussed defects with seat belts, suspension, or acoustics (Fig. 3). Overall, for all three brands together, discussions about air conditioning, visibility, or lights were usually concerning defects with these components, whereas discussions about the wheels and tires or transmission where usually not about defects (Fig. 4). As is to be expected, this varied substantially by brand, with some brands having a larger or smaller proportion of defect discussions for certain components.

Finally, for statistical rigor, we ran a contingency analysis between defect existence and each component category. Table 3 shows the results: for each component category, we show whether the proportion of defects in that category is lower than other threads, higher than other threads, or no different from other threads. Bold text and an asterisk (\*) alongside the p-value indicates statistical signi<sup>fi</sup>cance at the 95% con<sup>fi</sup>- dence level (support for the hypothesis; pb0.05); non-bold text (with no asterisk) indicates that the hypothesis is not supported. Table 3 shows strong associations between types of component discussed in the thread, and the existence, or absence, of defects.

## 4.2. Production study

Having ascertained that vehicle components were frequently discussed in connection with vehicle defects, but that the distribution of discussions by component was highly skewed, we moved to a production study, with a larger sample of threads, more evenly distributed between components, to attempt to rapidly and automatically classify threads by the component class under discussion.

## 4.2.1. Coding scheme for components

In the pilot study, tagging of the 4500-thread training set consumed 30 person days of effort expended over a period of 11 weeks. The average time to tag a thread was 1.8 min, with a standard deviation of 2.2 min [4]. Given the slow speed of manual thread classi<sup>fi</sup>cation, and the small number of threads found for certain component classes (as seen earlier in Fig. 3), we moved to an alternative component classi<sup>fi</sup>cation method for the production study. For the production study, we searched through all sub-forum titles on a single, large forum, Honda-Tech.com, to <sup>fi</sup>nd sub-forums that speci<sup>fi</sup>cally related to vehicle components. Honda-Tech was chosen for this case study as it was the

## Table 3

p-Values for contingency analyses: defect existence vs. component category.

<table><tr><td rowspan="2">Component category</td><td colspan="3">Defect proportion for component, compared to other threads? (p-value)</td></tr><tr><td>Is lower?</td><td>Is higher?</td><td>Is different?</td></tr><tr><td>Air conditioning</td><td>1.000</td><td>&lt;0.0001*</td><td>&lt;0.0001*</td></tr><tr><td>Airbag</td><td>0.1209</td><td>0.9129</td><td>0.2196</td></tr><tr><td>Braking</td><td>0.9995</td><td>0.0008*</td><td>0.0014*</td></tr><tr><td>Electrical</td><td>1.000</td><td>&lt;0.001*</td><td>&lt;0.0001*</td></tr><tr><td>Engine</td><td>0.0117*</td><td>0.9901</td><td>0.0220*</td></tr><tr><td>Lights</td><td>1.000</td><td>&lt;0.0001*</td><td>&lt;0.001*</td></tr><tr><td>Seat belts</td><td>0.9820</td><td>0.0336*</td><td>0.0530</td></tr><tr><td>Steering</td><td>0.9994</td><td>0.0011*</td><td>0.0020*</td></tr><tr><td>Structure and body</td><td>1.000</td><td>&lt;0.0001*</td><td>&lt;0.0001*</td></tr><tr><td>Transmission</td><td>&lt;0.0001*</td><td>1.000</td><td>&lt;0.0001*</td></tr><tr><td>Visibility</td><td>1.000</td><td>&lt;0.0001*</td><td>&lt;0.0001*</td></tr><tr><td>Wheel and tires</td><td>0.1378</td><td>0.9022</td><td>0.2591</td></tr><tr><td>Suspension</td><td>0.8466</td><td>0.2194</td><td>0.3922</td></tr><tr><td>Other</td><td>&lt;0.0001*</td><td>1.000</td><td>&lt;0.0001*</td></tr></table>

Table 4  
![](/api/attachments/T8DSJMEQ/fulltext/images/932a66289a437fe894edf434bdc211fc2013ca2ee62c75120767b3d299360ecd.jpg)  
Fig. 4. Percentage of threads, for each component category, discussing a defect.

largest forum, by number of users, by number of threads, and by number of component-speci<sup>fi</sup>c sub-forums. Component classi<sup>fi</sup>cation labels (sub-forum names) varied by brand so sub-forums across different brands were not directly mappable: Chevroletforum.com contained only 4 component-speci<sup>fi</sup>c sub-forums, each with fewer than 500 threads; ToyotaNation.com contained only 1 component-speci<sup>fi</sup>c sub-forum; the remaining Chevrolet and Toyota sub-forums were organized primarily by model name and model year.

We identi<sup>fi</sup>ed the following 9 component-related sub-forums from Honda-Tech.com: Audio/security/video, Welding/fabrication, Suspension, Wheel and tire, Paint and body, Lighting, Engine management and tuning, Transmission/drivetrain, and Brakes. We dissected the multi-class classi<sup>fi</sup>cation problem into multiple binary classi<sup>fi</sup>cation problems (one for each component category), and solved each binary classi<sup>fi</sup>cation separately. Our reason for undertaking separate binary classi<sup>fi</sup>cation problems is that it is well-known that the more classes a multiclass classi<sup>fi</sup>er handles, the more likely it is that the classi<sup>fi</sup>er's prediction accuracy will degrade [53].

## 4.2.2. Data sampling

In the production study, for each component we sampled up to 5000 threads from that component's sub-forum as positive examples and we used a random sample with the same number of threads from all the other sub forums as negative examples. To increase the variety of automobile-related threads, we included threads from one non-component-related sub-forum (“Road-racing/autocross” sub-forum; 30,863 available threads) among the available negative examples. Table 4 shows the number of threads that existed in each component-related sub-forum, and the sample size (number of positive examples) we used for training and testing the binary classi-<sup>fi</sup>ers for each component-related sub-forum.

Sub-forum names, threads per forum, and sample size used in the production study.

<table><tr><td>Sub-forum name</td><td>Threads available</td><td>Sample size used</td></tr><tr><td>Audio/security/video</td><td>24,124</td><td>5000</td></tr><tr><td>Welding/fabrication</td><td>9117</td><td>5000</td></tr><tr><td>Suspension</td><td>16,395</td><td>5,000</td></tr><tr><td>Wheel and tire</td><td>11,572</td><td>5000</td></tr><tr><td>Paint and body</td><td>4721</td><td>4721</td></tr><tr><td>Lighting</td><td>1872</td><td>1872</td></tr><tr><td>Engine management and tuning</td><td>2090</td><td>2090</td></tr><tr><td>Transmission/drivetrain</td><td>1917</td><td>1917</td></tr><tr><td>Brakes</td><td>620</td><td>620</td></tr></table>

## 4.3. Procedure

For all sub-forums that related directly to vehicle components, all discussion threads for the sub-forum were crawled, and mapped to their sub-forum name (component classi<sup>fi</sup>cation) in a database. The text of each thread was parsed and stemmed, using Porter's stemming algorithm [66], to obtain a term vector of canonical (stemmed) terms for each thread. The term vectors for each thread were stored and analyzed.

Text mining was then run on the component-labeled, term vectors. Three parameters were used for model tuning: algorithm, feature selection method, and number of terms.

## 4.3.1. Algorithms

We tried two alternative algorithms known to perform well for text classi<sup>fi</sup>cation tasks [82]. Support vector machines (SVM) were run using the LibSVM package [15] with a linear kernel while the Naïve Bayes classi<sup>fi</sup>er (NB) was executed using Weka [40].

## 4.3.2. Feature selection method

We used four feature ranking methods to select the most important term features. These were: information gain (IG), chi-square (CS), document and relevance correlation (DRC), and Robertson's selection value (RSV) [30].

## 4.3.3. Number of terms

We varied the number of terms from 200 to 2000, in 200 term increments.

We ran 5-fold cross validation for all experiments as illustrated in Fig. 5. To alleviate the problem of over-<sup>fi</sup>tting, feature selection and validation were run separately within each fold, following the general approach outlined in [67].<sup>4</sup> The average classi<sup>fi</sup>er performance across all folds was evaluated for each combination of algorithm×feature selection method×number of terms.

![](/api/attachments/T8DSJMEQ/fulltext/images/174f888da2e8aa4e259571938cc294a0d27e8900750fe4d0233bc68fbcd96a20.jpg)  
Fig. 5. Feature selection and validation for separate folds.

## 5. Results and evaluation

Table 5 shows the classi<sup>fi</sup>cation performance (F -measures, as de-<sup>fi</sup>ned in [95]) for each binary component classi<sup>fi</sup>cation task, as the classi<sup>fi</sup>cation algorithm, term selection method, and number of terms are adjusted. The algorithm and feature-selection method which produced the highest classi<sup>fi</sup>cation performance are shown in parentheses alongside the component class name in the heading for each chart. In all 9 cases, SVM was the top performing algorithm. The IG and RSV feature selection methods each produced the highest classi<sup>fi</sup>cation performance in 4 cases. Finally, 400–600 features produces the optimal (or very nearly the optimal) classi<sup>fi</sup>cation performance in all cases, though in many (6 of 9) cases the relatively <sup>fl</sup>at line (F -measure score) for the best method (i.e. algorithm+term selection combination) indicates that the best method is relatively insensitive to the number of features used.

Table 6 provides receiver operating characteristics (ROC) curves for the highest performance classi<sup>fi</sup>er, for the binary classi<sup>fi</sup>cation tasks for each component. The identity of the highest performance classi<sup>fi</sup>er (algorithm+feature selection method) and the total Area Under each ROC Curve (AUC score) are shown alongside each component heading. All AUC values are close to 1, which indicates high performance of the classi<sup>fi</sup>ers [10].

Table 7 shows the most signi<sup>fi</sup>cant features we found for each component classi<sup>fi</sup>cation. In the table, column headers describe the component. In parentheses, alongside the component class, is the feature selection method that produced the highest classi<sup>fi</sup>cation performance, as measured by F score. Below each component class is the list of the 20 most signi<sup>fi</sup>cant features we discovered for that component class. As a word stemmer was employed, word stems are used (e.g. “suspens” in place of “suspension”) [66]. For nonobvious terms (industry jargon for the component category), footnotes provide further details as to the origin of the term. Brand names are shown italicized in the table.

## 6. Conclusions

In this paper, we developed a model of text classi<sup>fi</sup>cation and component feature selection. We showcased our model for automatic product component categorization of online user postings using the automotive industry as an example. Various model con<sup>fi</sup>gurations (in terms of classi<sup>fi</sup>cation algorithm, term selection method, and number of selected features) were evaluated to identify the “optimal” classi<sup>fi</sup>er. Our results demonstrate that the performance of the classi-<sup>fi</sup>er is highly sensitive to classi<sup>fi</sup>cation algorithm, term selection method, and number of selected features. An SVM classi<sup>fi</sup>er with IG or RSV feature selection and 400–600 terms produced the highest classi<sup>fi</sup>cation performance. The limitations and implications of our work are as follows:

## 6.1. Limitations

The study reported in this paper was restricted to automotive enthusiast forums. While the results are likely to generalize to other social media postings, such as user reviews, comments, feeds, blogs, and micro-blogs (e.g. Twitter), this presumption needs to be further tested. Given that the classi<sup>fi</sup>ers were tuned using different vehicle sub-forums, and the most signi<sup>fi</sup>cant features appear highly plausible, it would seem that the classi<sup>fi</sup>er is able to distinguish even subtle differences between component-related postings. Further large-scale research needs to be undertaken on a wide range of social media postings, with manual veri<sup>fi</sup>cation by automotive experts, to validate this supposition.

## 6.2. Implications for practice and research

The <sup>fi</sup>ndings of this study have a number of implications for practitioners at vehicle and vehicle component manufacturing or distribution companies:

• An SVM classi<sup>fi</sup>er with IG or RSV feature selection and 400–600 terms produced the highest classi<sup>fi</sup>cation performance. This implies that product managers can use these parameters to rapidly isolate component-speci<sup>fi</sup>c threads on discussion forums, and categorize by component for detailed review (e.g. defect discovery and prioritization, or customer requirement elicitation).

• The most signi<sup>fi</sup>cant features (terms) for each component category were identi<sup>fi</sup>ed. This implies that marketing managers can increase product visibility by using these highly signi<sup>fi</sup>cant terms both in web-site content, for search engine optimization (SEO), and in pay-per-click or pay-per-action search engine marketing/search engine advertising (SEM/SEA) campaigns relating to the corresponding component categories.

For researchers, the implications of our <sup>fi</sup>ndings are as follows:

• Our study reinforces prior research showing that SVM approaches perform well for text-categorization tasks (e.g. [1,82]). We showed that, for vehicle discussion threads, the SVM's classi<sup>fi</sup>cation accuracy is sensitive to both feature selection approach and number of features. This implies that social media analytics researchers should continue to pursue SVM approaches for text categorization tasks, but must <sup>fi</sup>ne-tune both feature selection approaches and number of features.

Table 5 Variation in F<sub>1</sub> measures for binary classification tasks for each component category adj usting algorithm feature selection method and number of features ( i.e. selected terms )  
![](/api/attachments/T8DSJMEQ/fulltext/images/23617c2da8aa5af8f4b484328d67f0820a9d7dc409194d983aea9cbd4e3410fb.jpg)

Table 6 Receiver operating characteristics ( ROC ) curves for binary classification tasks for each vehicle component.  
![](/api/attachments/T8DSJMEQ/fulltext/images/159d7f878a6f5ca2dba905f883d045c1592e2d4bedd6d11518e4c56f021fc5df.jpg)

Table 7  
Most signi<sup>fi</sup>cant features for each component classi<sup>fi</sup>cation.

<table><tr><td>Audio/security/video (IG)</td><td>Welding/fabrication (CS)</td><td>Suspension(RSV)</td><td>Wheel and tire (RSV)</td><td>Paint and body (IG)</td><td>Lighting(IG)</td><td>Engine managementand tuning (IG)</td><td>Transmission/drivetrain (RSV)</td><td>Brakes(RSV)</td></tr><tr><td>amp</td><td>weld</td><td>spring</td><td>wheel</td><td>paint</td><td>light</td><td> $ecu^a$ </td><td>tranni</td><td>brake</td></tr><tr><td>speaker</td><td>welder</td><td> $coilov^b$ </td><td>rim</td><td>sprai</td><td>bulb</td><td>tune</td><td>gear</td><td>calip</td></tr><tr><td> $94^c$ </td><td>pipe</td><td>shock</td><td>tire</td><td>sand</td><td>headlight</td><td>wheel</td><td>tran</td><td>rotor</td></tr><tr><td>wire</td><td> $tig^d$ </td><td>suspens</td><td>wire</td><td>coat</td><td>hid</td><td>front</td><td>transmiss</td><td>pad</td></tr><tr><td>race</td><td>steel</td><td> $koni^e$ </td><td>rota</td><td>race</td><td>wheel</td><td>map</td><td>clutch</td><td>booster</td></tr><tr><td>sub</td><td>manifold</td><td>lower</td><td>har</td><td>color</td><td>race</td><td> $hondata^f$ </td><td> $lsd^g$ </td><td> $ab^h$ </td></tr><tr><td>alarm</td><td>tube</td><td>ride</td><td> $ecu^a$ </td><td>clear</td><td>projector</td><td>rear</td><td>synchro</td><td>master</td></tr><tr><td>audio</td><td>stainless</td><td>rear</td><td>offset</td><td>bodi</td><td>beam</td><td>chip</td><td>shift</td><td>slot</td></tr><tr><td>instal</td><td>machin</td><td> $gc^i$ </td><td>spt</td><td>primer</td><td>retrofit</td><td>tire</td><td>bear</td><td>disc</td></tr><tr><td>wheel</td><td>flang</td><td> $tein^j$ </td><td>amp</td><td>set</td><td>spring</td><td>paint</td><td>shaft</td><td>legend</td></tr><tr><td>power</td><td>aluminum</td><td>bush</td><td>size</td><td>setup</td><td>suspens</td><td> $crome$ </td><td>countershaft</td><td>prop</td></tr><tr><td>unit</td><td> $mig^k$ </td><td>strut</td><td> $nsxtasi^l$ </td><td>ecu</td><td>tire</td><td>tuner</td><td>paint</td><td>cylind</td></tr><tr><td>radio</td><td>fab</td><td> $lca^m$ </td><td>speaker</td><td>track</td><td>track</td><td>fuel</td><td>mainshaft</td><td>bleed</td></tr><tr><td>spring</td><td>exhaust</td><td>wire</td><td>motor</td><td>stock</td><td>fog</td><td> $s300^n$ </td><td> $mfactori$ </td><td>pedal</td></tr><tr><td>weld</td><td>materi</td><td>front</td><td>engin</td><td>job</td><td>ballast</td><td>suspens</td><td>amp</td><td> $mc^o$ </td></tr><tr><td>suspens</td><td>metal</td><td>adjust</td><td> $195/55-15^p$ </td><td>wire</td><td>tranni</td><td>sensor</td><td>wire</td><td>proport</td></tr><tr><td>deck</td><td>cut</td><td> $tokico^q$ </td><td>manifold</td><td>swap</td><td>weld</td><td>rim</td><td> $hydro^r$ </td><td>front</td></tr><tr><td>alpin</td><td>make</td><td> $kyb^s$ </td><td>instal</td><td>bumper</td><td>halogen</td><td> $obd1^t$ </td><td>5th</td><td>drum</td></tr><tr><td>system</td><td>fabric</td><td>swai</td><td> $obd1^t$ </td><td>spring</td><td> $coilov^b$ </td><td>injector</td><td>diff</td><td>rear</td></tr><tr><td>cd</td><td>piec</td><td> $ecu^a$ </td><td> $195/50-15^p$ </td><td>power</td><td>shock</td><td> $p28^u$ </td><td>fd</td><td> $ecu^a$ </td></tr></table>

<sup>a</sup> ECU=Engine Control Unit.  
<sup>b</sup> Coilov=Coilover (automobile suspension device).  
<sup>c</sup> 94=model year number (1994).  
<sup>d</sup> TIG=Tungsten Inert Gas (welding method).  
<sup>e</sup> Koni=popular brand of adjustable shock absorber.  
<sup>f</sup> Hondata=company that modi<sup>fi</sup>es and enhances standard Honda Engine Control Units.  
<sup>g</sup> LSD =Limited Slip Differential transmission.  
<sup>h</sup> Ab=stem of ABS=Anti-lock Braking System.  
<sup>i</sup> GC=Ground Control Suspensions (popular brand of suspension equipment).  
<sup>j</sup> Tein=popular brand of suspension products.  
<sup>k</sup> MIG=Metal Inert Gas (welding method).  
<sup>l</sup> Nsxtasi=username of active forum user.  
<sup>m</sup> LCA=Lower Control Arm (suspension part).  
<sup>n</sup> S300=plug in module to the OBD1 factory Honda Engine Computer (ECU).  
<sup>o</sup> MC=Motorcycle.  
<sup>p</sup> 195/5X-XX=popular tire size descriptors.

<sup>q</sup> Tokico=popular brand of shocks, springs, and suspension.

<sup>r</sup> Hydro=hydrostatic transmission.

<sup>s</sup> Kyb=popular brand of shocks and struts.

<sup>t</sup> OBD1=On Board Diagnostics protocol.

<sup>u</sup> P28=part number for commonly-used Engine Control Unit.

## Acknowledgements

The authors are grateful to Professor Mehdi Ahmadian, Director of the Center for Vehicle Systems and Safety, Virginia Tech, for his helpful feedback, guidance, and assistance. This research is partly supported by the Natural Science Foundation of China (Grant #70872089 and #71072129) and the National Science Foundation (Grant #DUE-0840719).

## References

[1] A. Abbasi, H. Chen, CyberGate: a system and design framework for text analysis of computer-mediated communication, MIS Quarterly 32 (4) (2008) 811–837.

[2] A. Abbasi, H. Chen, H.A. Salem, Sentiment analysis in multiple languages: feature selection for opinion classi<sup>fi</sup>cation in Web forums, ACM Transactions on Information Systems 26 (3) (2008).

[3] N. Abou Nabout, B. Skiera, Return on quality improvements in search engine marketing, Journal of Interactive Marketing 26 (3) (August 2012) 141–154.

[4] A.S. Abrahams, J. Jiao, G.A. Wang, W. Fan, Vehicle defect discovery from social media, Decision Support Systems 54 (1) (December 2012) 87–97.

[5] V. Anand, W.H. Glick, C.C. Manz, Thriving on the knowledge of outsiders: tapping organizational social capital, The Academy of Management Executive 16 (1) (2002) 87–101.

[6] W. Antweiler, M.Z. Frank, Is all that talk just noise? The information content of Internet stock message boards Journal of Finance 59 (3) (2004) 1259–1294

[7] C. Apte, F. Damerau, S. Weiss, Automated learning of decision rules for text categorization, ACM Transactions on Information Systems 12 (3) (1994) 233–240.

[8] I. Benbasat, D.K. Goldstein, M. Mead, The case research strategy in studies of information systems, MIS Ouarterly 11 (3) (1987) 369–386

[9] H. Borko, M. Bernick, Automatic document classi<sup>fi</sup>cation, Journal of the ACM 10 (2)(1963).151-162

[10] A.P. Bradley, The use of the area under the ROC curve in the evaluation of machine learning algorithms, Pattern Recognition 30 (1997) 1145–1159.

[11] C.H. Brooks, N. Montanez, Improved annotation of the blogosphere via autotagging and hierarchical clustering, Proceedings of the International World Wide Web Conference (WWW 2006), ACM Press, Edinburgh, Scotland, May 23–26 2006, pp. 625–632.

[12] J.S. Brown, P. Duguid, Organizational learning and communities-of-practice: toward a uni<sup>fi</sup>ed view of working, learning, and innovation, Organization Science 2 (1) (1991) 40–57.

[13] R.A. Calvo, J.M. Lee, X. Li, Managing content with automatic document classi<sup>fi</sup>cation, Journal of Digital Information 5 (2) (2004) 1–15.

[14] Q. Cao, W. Duan, Q. Gan, Exploring determinants of voting for the “helpfulness” of online user reviews: a text mining approach, Decision Support Systems 50 (2) (2011) 511–521.

[15] C.C. Chang, C.J. Lin, LIBSVM: a library for support vector machines, ACM Transactions on Intelligent Systems and Technology 2 (3) (2011) 27:1–27:27, (Software available at http://www.csie.ntu.edu.tw/\~cjlin/libsvm).

[16] K.H. Chen, H.H. Chen, Extracting noun phrases from large-scale texts: a hybrid approach and its automatic evaluation, Proceedings of the 32nd ACL Annual Meeting, 1994, pp. 234–241.

[17] H. Chen, C. Schuffels, R. Orwig, Internet categorization and search: a self-organizing approach, Journal of Visual Communication and Image Representation 7 (1) (1996) 88–102.

[18] W. Chung, H. Chen, J. Nunamaker, A visual framework for knowledge discovery on the Web: an empirical study of business intelligence exploration, Journal of Management Information Systems 21 (4) (2005) 57–84

[19] J. Cohen, A coef<sup>fi</sup>cient of agreement for nominal scales, Educational and Psychological Measurement 20 (1) (1960) 37–46

[20] D. Constant, L. Sproull, S. Kiesler, The kindness of strangers: the usefulness of electronic weak ties for technical advice, Organization Science 7 (2) (1996) 119–135.

[21] K. Coussement, D. Van den Poel, Improving customer complaint management by automatic email classi<sup>fi</sup>cation using linguistic style features as predictors, Decision Support Systems 44 (4) (2008) 870–882.

[22] H. Davis, Search Engine Optimization, O'Reilly Media, 2006.

[23] K. De Valcka, G.H. Van Bruggen, B. Wierenga, Virtual communities: a marketing perspective, Decision Support Systems 47 (3) (2009) 185–203.

[24] R. Decker, M. Trusov, Estimating aggregate consumer preferences from online product reviews, International Journal of Research in Marketing 27 (2010) 293–307.

[25] P.M. Di Gangi, M.M. Wasko, Steal my idea! Organizational adoption of user innovations from a user innovation community: a case study of Dell IdeaStorm, Decision Support Systems 48 (1) (2009) 303–312.

[26] W. Duan, B. Gu, A.B. Whinston, Do online reviews matter? An empirical investigation of panel data, Decision Support Systems 45 (4) (2008) 1007–1016.

[27] K.M. Eisenhardt, Building theories from case study research, Academy of Management Review 14 (4) (1989) 532–550.

[28] O.A. El Sawy, Personal information systems for strategic scanning in turbulent environments: can the CEO go online? MIS Quarterly 9 (1) (1985) 53–60.

[29] O. Etzioni, M. Banko, S. Soderland, D.S. Weld, Open information extraction from the web, Communications of the ACM 51 (12) (2008) 68–74.

[30] W. Fan, M.D. Gordon, P. Pathak, Effective pro<sup>fi</sup>ling of consumer information retrieval needs: a uni<sup>fi</sup>ed framework and empirical comparison, Decision Support Systems 40 (2) (2005) 213–233.

[31] W. Fan, L. Wallace, S. Rich, Z. Zhang, Tapping the power of text mining, Communications of the ACM 49 (9) (2006) 76–82.

[32] B.J. Finch, Internet discussions as a source for consumer product customer involvement and quality information: an exploratory study, Journal of Operations Management 17 (5) (1999) 535–556.

[33] B.J. Finch, R.L. Luebbe, Using Internet conversations to improve product quality: an exploratory study, International Journal of Quality and Reliability Management 14 (8) (1997) 849–865.

[34] C. Fornell, B. Wernerfelt, Defensive marketing strategy by customer complaint management: a theoretical analysis, Journal of Marketing Research 24 (4) (1987) 337–346.

[35] J. Gerdes, B.B. Stringham, R.G. Brookshire, An integrative approach to assess qualitative and quantitative consumer feedback, Electronic Commerce Research 8 (4) (2008) 217–234.

[36] A. Ghose, S. Yang, An empirical analysis of search engine advertising: sponsored search in electronic markets, Management Science 55 (10) (October 2009) 1605–1622.

[37] B. Glaser, A. Straus, The Discovery of Grounded Theory: Strategies of Qualitative Research, Wiedenfeld and Nicholson, London, 1967.

[38] K. Golub, Automated subject classi<sup>fi</sup>cation of Web documents, Journal of Documentation 62 (3) (2006) 350–371.

[39] R. Gopal, J.R. Marsden, J. Vanthienen, Information mining — re<sup>fl</sup>ections on recent advancements and the road ahead in data, text, and media mining, Decision Support Systems 51 (4) (2011) 727–731.

[40] M. Hall, E. Frank, G. Holmes, B. Pfahringer, P. Reutemann, I.H. Witten, The WEKA data mining software: an update, SIGKDD Explorations 11 (1) (2009) 10–18.

[41] Internet Engineering Task Force (IETF), The Atom syndication format, Request for Comments (RFC), 4287, December 2005.

[42] Internet Engineering Task Force (IETF), The Atom publishing protocol, Request for Comments (RFC), 5023, October 2007.

[43] P.H. Jesty, K.M. Hobley, R. Evans, I. Kendall, Safety analysis of vehicle-based systems, in: F. Redmill, T. Anderson (Eds.), Lessons in System Safety, Proceedings of the 8th Safety-Critical Systems Symposium (SCSS), Springer, London, 2000.

[44] In: T. Joachims, F. Sebastiani (Eds.), Automated text categorization (Special Issue), Journal of Intelligent Information Systems, 18, 2002.

[45] A.M. Kaplan, M. Haenlein, Users of the world, unite! The challenges and opportunities of social media, Business Horizons 53 (1) (January–February 2010) 59–68. R. Koch, The 80/20 Principle, Doubleday, New York, NY, 2008.

[47] P. Kolari, T. Finin, A. Joshi, SVMs for the blogosphere: blog identi<sup>fi</sup>cation and splog detection, AAAI Spring Symposium on Computational Approaches to Analyzing Weblogs, 2006.

[48] J.R. Landis, G.G. Koch, The measurement of observer agreement for categorical data, Biometrics 33 (1) (1977) 159–174.

[49] E.L. Lesser, J. Storck, Communities of practice and organizational performance, IBM Systems Journal 40 (4) (2001) 831–841.

[50] D.D. Lewis, Y. Yang, T.G. Rose, F. Li, RCV1: a new benchmark collection for text categorization research, Journal of Machine Learning Research 5 (2004) 361–397.

[51] Y.H. Li, A.K. Jain, Classi<sup>fi</sup>cation of text documents, The Computer Journal 41 (8) (1998) 537–546.

[52] N. Li, D.D. Wu, Using text mining and sentiment analysis for online forums hotspot detection and forecast, Decision Support Systems 48 (2) (2010) 354–368.

[53] T. Li, C. Zhang, M. Ogihara, A comparative study of feature selection and multiclass classi<sup>fi</sup>cation methods for tissue classi<sup>fi</sup>cation based on gene expression, Bioinformatics 20 (15) (2004) 2429–2437.

[54] J. Li, R. Pan, W. Wang, Selection of best keywords: a Poisson regression model, Journal of Interactive Advertising 11 (1) (Fall 2010) 27–35.

[55] T. Loughran, B. McDonald, When is a liability not a liability? Textual analysis, dictionaries, and 10-Ks, Journal of Finance 661 (1) (2011) 35–65.

[56]. Z. Ma O.R.L. Sheng G. Pant Discovering company revenue relations from news: a network approach, Decision Support Systems 47 (2009) 408–414.

[57] Z. Ma, G. Pant, O.R.L. Sheng, Mining competitor relationships from online news: a network-based approach, Electronic Commerce Research and Applications 10 (4) (2011) 418–427.

[58] J.C. McCune, Snooping the Net, Management Review (1997) 58–59.

[59] D.M. McCutcheon, J.R. Meredith, Conducting case study research in operations Management, Journal of Operations Management 11 (3) (1993) 239–256.

[60] K.A. Neuendorf, The Content Analysis Guidebook, Sage Publications Inc., 2001

[61] K. Nigam, A. McCallum, S. Thrun, T. Mitchell, Text classi<sup>fi</sup>cation from labeled and unlabeled documents using EM, Machine Learning 39 (2/3) (2000) 103–134

[62] D.E. O'Leary, Blog mining-review and extensions: from each according to his opinion, Decision Support Systems 51 (4) (2011) 821–830.

[63] C. Oh, O.R.L. Sheng, Investigating predictive power of stock micro blog sentiment in forecasting future stock price directional movement, Proceedings of the International Conference on Information Systems (ICIS), December 6, 2011(Paper 17).

[64] B. Pang, L. Lee, Opinion mining and sentiment analysis, Foundations and Trends in Information Retrieval 2 (1–2) (2008) 1–135.

[65] M. Parameswaran, A.B. Whinston, Research issues in social computing, Journal of the Association for Information Systems 8 (6) (2007) 336–350.

[66] M.F. Porter, An algorithm for suf<sup>fi</sup>x stripping, Program 14 (3) (1980) 130–137.

[67] P. Refaeilzadeh, L. Tang, H. Liu, On comparison of feature selection algorithms, AAAI 2007 Workshop on Evaluation Methods for Machine Learning II, Vancouver, British Columbia, Canada, July 22 2007.

[68] E. Riloff, W. Lehnert, Information extraction as a basis for high-precision text classi<sup>fi</sup>cation, ACM Transactions on Information Systems 12 (3) (1994) 296–333.

[69] E. Riloff, J. Wiebe, Learning extraction patterns for subjective expressions, Conference on Empirical Methods in Natural Language Processing (EMNLP-03), 2003, pp. 105–112.

[70] N.C. Romano, C. Donovan, H. Chen, J. Nunamaker, A methodology for analyzing Web-based qualitative data, Journal of Management Information Systems 19 (4) (2003) 213–246.

[71] M.A. Rosso, B.J. Jansen, Brand names as keywords in sponsored search advertising, Communications of the Association for Information Systems 27 (1) (2010) 6.

[72] RSS Advisory Board, RSS 2.0 Speci<sup>fi</sup>cation. Available at: http://www.rssboard.org/ rss-speci<sup>fi</sup>cation, (Accessed on: 18 Oct 2012).

[73] M. Ruiz, P. Srinivasan, Hierarchical text categorization using neural networks, Information Retrieval 5 (1) (2002) 87–118.

[74] O.J. Rutz, M. Trusov, R.E. Bucklin, Modeling indirect effects of paid search advertising: which keywords lead to more future visits? Marketing Science 30 (4) (July/August 2011) 646–665.

[75] S.E. Sampson, Rami<sup>fi</sup>cations of monitoring service quality through passively solicited customer feedback, Decision Sciences 27 (4) (1996) 601–622

[76] C. Sanes, Complaints are hidden treasure, Journal for Quality and Participation 16 (5) (1993) 78–82.

[77] R.L.T. Santos, C. Macdonald, R.M.C. McCreadie, I. Ounis, I. Soboroff, Information retrieval on the blogosphere, Foundations and Trends in Information Retrieval 6 (1) (2012) 1–125.

[78] D.E. Schendel, C.W. Hofer, Theory Building and Theory Testing: A Conceptual Overview, Strategic Management, Little, Brown and Company, Boston, 1979.

[79] A. Schenkel, R. Teigland, Improved organizational performance through communities of practice, Journal of Knowledge Management 12 (1) (2008) 106–118.

[80] R.P. Schumaker, H. Chen, Textual analysis of stock market prediction using breaking <sup>fi</sup>nancial news: the AZFin text system, ACM Transactions on Information Systems 27 (2) (2009).

[81] H. Schutze, Automatic word sense discrimination, Computational Linguistics 24 (1) (1998) 97–123.

[82] F. Sebastiani, Machine learning in automated text categorization, ACM Computing Surveys 34 (1) (2002) 1-47

[83] S. Spangler, I. Kreulen, Mining the Talk: Unlocking the Business Value in Unstructured Information, IBM Press, 2008.

[84] M. Sponder, Social Media Analytics: Effective Tools for Building, Interpreting, and Using Metrics, Mc-Graw Hill, 2011.

[85] P.C. Tetlock, M. Saar-Tsechansky, S. Macskassy, More than words: quantifying language to measure <sup>fi</sup>rms' fundamentals, Journal of Finance 63 (3) (2008) 1437–1467.

[86] P.D. Turney, M.L. Littman, Measuring praise and criticism: inference of semantic orientation from association, ACM Transactions on Information Systems 2 (4) (2003) 315–346.

[87] O. Vechtomova, Facet-based opinion retrieval from blogs, Journal Information Processing and Management: an International Journal 46 (1) (January 2010) 71–88.

[88] G. Wang, X. Liu, W. Fan, A knowledge adoption model based framework for <sup>fi</sup>nding helpful user-generated contents in online communities, International Conference on Information Systems (ICIS) 2011 Proceedings, December 6 2011, (Paper 15).

[89] D.D. Ward, P.H. Jesty, R.S. Rivett, Decomposition scheme in automotive hazard analysis, SAE International Journal of Passenger Cars — Mechanical Systems 2 (1) (2009) 803–813.

[90] M.M. Wasko, S. Faraj, Why should I share? Examining social capital and knowledge contribution in electronic networks of practice, MIS Quarterly 29 (1) (2005) 35–57.

[91] E.C. Wenger, W.M. Snyder, Communities of practice and organizational performance, Harvard Business Review (2000) 139–145.

[92] J. Wiebe, E. Riloff, Creating subjective and objective sentence classi<sup>fi</sup>ers from unannotated texts, Sixth International Conference on Intelligent Text Processing and Computational Linguistics, 2005, pp. 486–497.

[93] T. Wilson, J. Wiebe, P. Hoffmann, Recognizing contextual polarity in phrase-level sentiment analysis, Proceedings of Human Language Technologies Conference/ Conference on Empirical Methods in Natural Language Processing, Vancouver, 2005.

[94] A. Woolridge, Social media provides huge opportunities, but will bring huge problems, Economist (2011) 50.

[95] Y. Yang, An evaluation of statistical approaches to text categorization, Information Retrieval 1 (1) (1999) 69–90

[96] Y. Yang, S. Slattery, R. Ghani, A study of approaches to hypertext categorization, Journal of Intelligent Information Systems 18 (2–3) (2002) 219–241.

[97] R.K. Yin, Case Study Research, Sage Publications, London, 1989

[98] D. Zeng, H. Chen, R. Lusch, S.H. Li, Social media analytics and intelligence, IEEE Intelligent Systems (November/December 2010) 13–16.

[99] Y. Zhang, Y. Dang, H. Chen, M. Thurmond, C. Larson, Automatic online news monitoring and classi<sup>fi</sup>cation for syndromic surveillance, Decision Support Systems 47 (4) (2009) 508–517.

![](/api/attachments/T8DSJMEQ/fulltext/images/241d5dabcc564dbe733bfed1d73a76166ed0b342c86f0939400491c8174850ad.jpg)

Alan S. Abrahams is an Assistant Professor in the Department of Business Information Technology, Pamplin College of Business, at Virginia Tech. He received a Ph.D. in Computer Science from the University of Cambridge, and holds a Bachelor of Business Science degree from the University of Cape Town. Dr. Abrahams's primary research interest is in the application of decision support systems in entrepreneurship. He has published in a variety of journals including Decision Support Systems, Expert Systems with Applications, Journal of Computer Information Systems, Communications of the AIS, and Group Decision and Negotiation.

![](/api/attachments/T8DSJMEQ/fulltext/images/77bec827de492c0710db1e66b8887de0b55840680b0a4742496b0261aa43d5fd.jpg)

G. Alan Wang is an Assistant Professor in the Department of Business Information Technology, Pamplin College of Business, at Virginia Tech. He received a Ph.D. in Management Information Systems from the University of Arizona, an M.S. in Industrial Engineering from Louisiana State University, and a B.E. in Industrial Management and Engineering from Tianjin University. His research interests include heterogeneous data manage ment, data cleansing, data mining and knowledge discovery, and decision support systems. He has published in Decision Support Systems, Communications of the ACM, IEEE Transactions of Systems, Man and Cybernetics (Part A), IEEE Computer, Group Decision and Negotiation, Journal of the American Society for Information Science and Technology, and Journal of Intelligence Community Research and Development.

![](/api/attachments/T8DSJMEQ/fulltext/images/4387c19cd371130e69c0652d65971c0d11774a4720018bb0c6067cd8ad32d8a6.jpg)

Jian Jiao is a PhD candidate in Computer Science at Virginia Tech and a Software Design Engineer at Microsoft. He hold an M.S. in Computer Science from the Beijing Institute of Technology, and has previous work experience at Microsoft Research Asia and Motorola.

![](/api/attachments/T8DSJMEQ/fulltext/images/f980e711895d393ab03bacd1b0153e411e0f95c4921d0e4c06d004d2cc058a97.jpg)

![](/api/attachments/T8DSJMEQ/fulltext/images/e21f2231144e88d09e8e49387a4cf703b199baf7e7434100cf2ac3531cd01eba.jpg)

Weiguo (Patrick) Fan is a Full Professor of Accounting and Information Systems and Full Professor of Computer Science (courtesy) at the Virginia Polytechnic Institute and State University (Virginia Tech). He received his Ph.D. in Business Administration from the Ross School of Business, University of Michigan, Ann Arbor, in 2002, an M.S. in Computer Science from the National University of Singapore in 1997, and a B.E. in Information and Control Engineering from the Xi'an Jiaotong University, P.R. China, in 1995. His research interests focus on the design and development of novel information technologies – information retrieval, data mining, text/web mining, business intelligence techniques – to support better business information management and decision making. He has published more than 100 refereed journal and confer ence papers. His research has appeared in journals such as Information Systems Research, Journal of Management Information Systems, IEEE Transactions on Knowledge and Data Engineering, Information Systems, Communications of the ACM, Journal of the American Society on Information Science and Technology, Information Processing and Management, Decision Support Systems, ACM Transactions on Internet Technology, Pattern Recognition, IEEE Intelligent Systems, Pattern Recognition Letters, International Journal of e-Collaboration, and International Journal of Electronic Business.

Zhongju (John) Zhang is an Associate Professor in the School of Business, University of Connecticut. He received his Ph.D. in Management Science (with minors in Economics and Operations Management) from the University of Washington Business School. Zhang's research focuses on the problems at the interface of information systems/technologies, marketing, economics, and operations research. His research has been published in academic journals including Information Systems Research, INFORMS Journal on Computing, Journal of Management Information Systems, IEEE Transactions on Engineering Management, Decision Support Systems, European Journal of Operational Research, Communications of the ACM, Decision Sciences Journal, as well as in various international conference proceedings. Zhang was a co-recipient

of the Best IS Publications of the Year 2010 award. He has also won the Research Excellenc Award (2011), the MBA Teacher of the Year (2010), the Best Paper Award (2009), and the Ackerman Scholar Award (2007–2009) at the UConn School of Business. Zhang is a guest associate editor for MIS Quarterly and serves on the editorial board of Journal of Database Management, Journal of Electronic Commerce Research, and Electronic Commerce Research and Applications.
