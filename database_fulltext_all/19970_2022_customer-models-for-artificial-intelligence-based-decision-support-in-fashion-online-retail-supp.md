---
otero_id: 19970
otero_key: "M4G83T2R"
title: "Customer models for artificial intelligence-based decision support in fashion online retail supply chains"
authors: "Artur M. Pereira; J. Antão B. Moura; Evandro De B. Costa; Thales Vieira; André R.D.B. Landim; Eirini Bazaki; Vanissa Wanick"
year: "2022"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2022.113795"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Customer models for artificial intelligence-based decision support in fashion online retail supply chains

![](/api/attachments/M4G83T2R/fulltext/images/d15d086f8579823e39599c31a3ac10b839edc46e96aeb96b3fbb8f46e1b5ed9b.jpg)

Artur M. Pereira <sup>a,\*</sup>, J. Ant˜ao B. Moura <sup>a</sup>, Evandro De B. Costa <sup>b</sup>, Thales Vieira <sup>b</sup>, Andr´e R.D. B. Landim <sup>a</sup>, Eirini Bazaki <sup>c</sup>, Vanissa Wanick <sup>c</sup>

<sup>a</sup> Federal University of Campina Grande, Graduate Program on Computer Science (PPGCC), R. Aprígio Veloso, 882, Campina Grande 58428-830, PB, Brazil

<sup>b</sup> Federal University of Alagoas, Institute of Computing (IC), Av. Lourival Melo Mota, S/N, Maceio ´ 57072-900, AL, Brazil

<sup>c</sup> University of Southampton, Faculty of Arts and Humanities, Winchester School of Art, Park Ave, Winchester SO23 8DL, Hampshire, UK

## A R T I C L E I N F O

Keywords: Decision support systems Artificial intelligence Customer mode Retail supply chain Fashion User model

## A B S T R A C T

Fashion is a global, multi-trillion dollar industry devoted to producing and selling clothing, footwear, and ac cessories to individuals or groups of people. Its sheer numbers, together with social and environmental sus tainability concerns, and the move towards digitalization of customer-centric operations, make the fashion business a prime target for Decision Support Systems (DSSs). On the other hand, decision support in fashion retail is particularly problematic and embraces all major supply chain domains. Decisions in an online fashion retail supply chain (FRSC) are highly dependent on time-varying customers' preferences and product availability, often leading to a combinatorial explosion. To address such a problem, DSSs could greatly benefit from high-quality information stored in customer models (CMs), constructed by using Artificial Intelligence techniques, allowing informed decisions on how to personalize (adapt) to match the customer's needs and preferences. Combinations of CMs with recommender systems (RSs) have been increasingly utilized in fashion e-commerce to provide personalized product recommendations. Nevertheless, works on enhancing CMs for e-commerce or other decision-making chain domains are scanty. This paper offers a systematic review of the literature on fashion CMs with applications to decision-making in FRSCs mining topics for a research agenda Research on the theme is relevant and urgent for the fashion business, which is still in its infancy. Work on the agenda topics could benefit distinct fashion stakeholders, not just customers, and produce well-grounded decision-making in varied FRSC contexts and dynamics.

## 1. Introduction

The fashion industry is estimated to be worth more than 3 trillion US dollars worldwide.<sup>1</sup> It supplies the world population with clothing, footwear, makeup, and other accessories. The digitalization of the fashion retail chain and new trends in customer behavior have boosted fashion e-commerce. In the US alone, e-commerce accounted for 29.5% of fashion retail sales in 2020.²

Artificial Intelligence (AI) techniques have been used in fashion e commerce and retailing, enabling significant competitive advantages by supporting decision-making tasks, delegating them to software systems. For instance, due to the Covid-19 pandemic, the luxury fashion market had to deploy and rely on AI technologies to provide remote high-end customer service.<sup>3</sup> The high quality and variety of information gener ated by AI techniques, including machine learning algorithms, for customer modeling have helped in personalizing and enhancing cus tomers' shopping experiences, analyzing data, predicting trends, and managing fashion supply chains to some extent [1,2].

At the same time, the benefits of high quality and variety of infor mation are now being challenged by two complementary issues: on one hand, e-commerce customers are surrounded by rising floods of infor mation (cognitive overload [3]) that impair their judgment and decision-making, particularly when having too many options to choose from. On the other hand, the many different information sources with vast amounts of customers' data make them valuable feeders of personal information to recommender systems (RSs) or other kinds of decisionsupport systems (DSSs), such as those for enabling advertising tools/ campaigns [4]).

Recently, fashion RSs based on customer models (CMs) that include basic data on the customer $( \boldsymbol { \mathrm { e . } } \boldsymbol { \mathrm { g . } } ,$ its body measurements [5]) who is using a personalized RS together with complementary input, such as clothing features [6,7] or apparel usage context [8], have been proposed to alleviate the information overload problem, providing personalized services and assisting customers to make more satisfying decisions. Researchers also highlight the need to model the influence of personality and emotions in the fashion e-commerce domain [9]. Existing models for this domain are still in their early stages of development.

Considering that the fashion shopping decision is shaped by several aspects that reflect product catalog offerings and perhaps, more importantly, the customer's entire profile and possibly dynamic in terests, such as occasional needs, it is of interest to enhance CMs to cover these aspects and variations for adequately supporting the personaliza tion of the customer's experience in online fashion retail supply chains (FRSCs). Further, CMs could also be enhanced to support decisions by other FRSC stakeholders in scenarios beyond retail - e.g., design, manufacturing, and distribution.

The extant literature on fashion CMs/RSs-DSSs concentrates on ap plications to online retail. With the movement towards consumercentric business operations from a more traditional product-centric approach, CMs become linchpins for decision-making automated sup port in other parts of the FRSC as well. The authors of [[10], p. 4] quote Sanjay Choudpouri, former director of mass customization at Levi Strauss, as foreseeing that customization in the fashion industry “will become a competitive necessity rather than a nice fringe offering”.

Mr. Choudpouri's customer-centric vision has an implicit, complex business problem in terms of transforming fashion business processes to accurately and quickly understand customers' wants and effectively and timely respond to them throughout the online FRSC. The subservient technical problem involves finding models and tools for decision support in FRSCs. Personalized CMs will have an important role to play for the underpinning technical solution to the latter problem.

This paper seeks to study works on the theme of (fashion) customers models as drivers of DSSs that have been reported in the recent litera ture. The study is carried out by means of a systematic literature review from 2011 to mid February 2022 to answer the following Research Questions (RQs):

• RQ1: Which features are considered in the literature to build fashion customers' personalized models?

• RQ2: Which AI tools and methods have been proposed to automat ically acquire customer information and represent the resulting model?

• RQ3: Which AI algorithms use the aforementioned customer models to provide recommendations?

• RQ4: Where are the above models (meant to be) applied as decision support in an FRSC?

The main contributions of this study are: (i) an updated analysis of recent works on the theme that can serve as support for guiding man agers, IT professionals, and researchers interested in understanding, building, or applying such kind of DSSs to online FRSCs; (ii) the provi sion of a synthesized basis, forming a body of knowledge, for future reference and research on the theme.

The remainder of the paper is organized as follows. Section 2 sum marizes the conceptual foundations and terminology used. Section 3 describes the methodology employed to harvest studies. Section 4 presents and discusses findings to answer the RQs. Section 5 proposes a research agenda to further customer model-driven DSSs' enhancement and their applications to cover online FRSC's domains more compre hensively. Section 6 brings concluding remarks.

## 2. Theoretical background

This section introduces terminology and briefly discusses CMs and their use to support decision-making in FRSCs.

## 2.1. Customer modeling, recommender system and decision support

In a broad sense, RSs using Artificial Intelligence techniques are a particular class of DSS in a knowledge-based (or data-driven) approach. One distinctive feature of a personalized RS is the presence of a user model (or “profile” [4]). In a computational perspective, the user model contains a representation of knowledge about an individual user or group, thus providing essential information for a DSS to support the adaptation effect, i.e., to behave differently for different users. There fore, a user model is intended to provide information about the indi vidual user who is using a personalized RS. Hence, RSs represent a class of well-established software tools and techniques to help users (cus tomers) access online product catalogs, gather data about their interests and tastes, and give suggestions on product items that may interest them, based on customer and products features. These suggestions are related to decision-making processes, such as what items to buy or manufacture. According to [11,12], people rely on recommendations from different sources in the consumer decision-making process for products, services, and general content. Examples of contexts where RSs are currently employed include music services, news, restaurants, and fashion e-commerce. In an FRSC context, the “user” is the customer of a fashion product or service. The CM/RS combination assists customers by recommending feasible buying choices.

CMs are created by a customer modeling process. Tasks in this pro cess include representation and acquisition of knowledge about the customer. Acquisition of information for a CM is many times executed as a machine learning task to automatically acquire new information, e.g., predicting customers' behaviors and preferences by observing and interpreting their interactions with the RS, as well as new representa tions of existing information.

The RS uses the CM to provide appropriate recommendations for that customer. Note that a CM usually relies on products that the customer has interacted with somehow. Also, RS's outputs are generally related to products. Thus, a proper product model is also appropriate in this context.

To build a CM, information must be explicitly collected, through direct customer interactions which may include: rating items; ranking items; and choosing items from a gallery of items, or implicitly, through mechanisms that monitor customer activity, for instance, analyzing customer views (and viewing times) of items in the store; purchase history; and social network analysis, among others. Given the omni presence of raw data in this context, in the form of text and images, for instance, it is usually necessary to include information extraction algo rithms to extract high level structured data (see Section 4.2).

The customer profiles contained in a CM can be updated or augmented dynamically, in contrast to static profiles that maintain the same information over time. Dynamic profiles that consider time may differentiate between short-term and long-term interests. Short-term profiles represent the customer's current interests, whereas long-term profiles indicate interests that are not subject to frequent changes over time. Hence, CMs for RSs may be static, when only long-term prefer ences are considered; or dynamic, when both long-term and short-term preferences are represented. Thus identifying a customer's short-term and long-term preferences is a relevant concern. For instance, a trop ical country customer may frequently browse and purchase summer outfits (long-term preference); it may also visit a store to occasionally buy a winter coat for a vacation trip (short-term preference). For a comprehensive review on RSs, we refer the reader to [13].

The development of RSs surged with e-commerce and the wide availability of huge catalogs of items, which led to an information overload problem. To address this major problem, RSs use data filtering tools, such as content-based filtering, collaborative filtering, or even a combination of these approaches, leading to hybrid recommendation techniques [13].

Content-based filtering recommendation techniques try to match product or service characteristics to a specific customer through pre dictive algorithms, according to its profile, i.e., it tries try to guess the features or behavior of a customer given the item's features which they positively react to. For instance, they use characteristics about products to suggest items that relate to the ones the customer has liked or browsed in the past, based on information about comparisons of the chosen item with other items from the preference history of this consumer [13]. Such is the case of a RS suggesting ties after a customer finishes browsing some tuxedos.

Collaborative filtering is based on the fundamental assumption that if a group of customers rates items similarly, or if they share a similar consumer behavior, they will probably share the same preferences for other items [14]. For instance, a customer browsing a pair of running shoes may receive a recommendation to buy a pair of running socks because others who bought the shoes also bought the socks.

## 2.2. Decision-making in fashion retail supply chains

FRSC stakeholders make decisions to steer the chain's operations towards business objectives by fulfilling customers' needs. From the models in [15] and the stakeholder map in [16], we identify 5 main FRSC decision-making domains:

i) Planning - where activities such as creation, design, materials, and means procurement (e.g., textiles, financing) take place.

ii) Production - involves the actual manufacturing of fashion products.

iii) Distribution - includes logistics and warehousing.

iv) Retail - encompasses customer-facing activities, e.g., marketing and sales.

v) Post-sales - covers activities that deal with the follow-up, satis faction surveys, loyalty plans, and returns or exchanges of items bought by customers.

To the list of major FRSC stakeholders in [16] - namely, suppliers, manufacturers, retailers, and fashion designers; post-consumer actors (e. g. second-hand sellers); service providers (e.g., software, consultants) and independent experts (e.g. management scholars) - we add customers.

This paper focuses on modeling fashion customers to feed informa tion to RSs or DSSs which, in turn, may support decisions by the cus tomers themselves or by other FRSC stakeholders. Consumer decision support, as detailed in Section 4.1, is influenced by different factors that depend on attributes from the product/service and consumer values.

Technology influences consumer engagement with a product, brand, or service through points of interaction of the consumer journey. This technological (digital) transformation is not only limited to online spaces and can also be applied in the omnichannel environment [17].

In a digital transformation move, a company's processes are rear ranged with adequate IT support, changing its existing business logic or value creation. For instance, compiling and analyzing information on fashion online retail customers' needs, wants, preferences, and buying decisions may be used to build CMs and then combine these CMs with RSs to recommend buying options to e-commerce customers. CMs combined with adequate DSSs may support decisions by FRSC stake holders elsewhere in the chain, such as in design and materials sourcing. Hereinafter, we use the term “CM” to indistinctly refer to the CM itself or

CM/RS-DSS combinations unless stated otherwise. Using CMs over FRSC decision domains will transform the entire chain, not just sales.

## 3. Methodology

A theme-based, systematic literature review was designed according to recommendations in [18] and carried out to elicit papers from which to answer RQs 1 to 4. Its details are given in the following subsections and Table 2. Complementary references were also used to support the research agenda.

## 3.1. Database and search terms

Searches were performed on the following databases: ACM Digital Library; Emerald Insight; Google Scholar; IBM TechDocs; IEEEXplore; Microsoft Academic; Taylor & Francis Online; Scopus (Elsevier); and Wiley Online Library.

The following search string, comprised of four main operands con nected by AND operators, was used in the searches:

((fashion OR apparel OR textile OR garment OR cloth\* OR cosmetics OR shoes OR jewelry)

AND (user OR customer OR buyer OR client OR shopper OR purchaser).

AND (model\* OR profil\* OR preference OR decision OR behavi\*).

AND (digit\* OR supply chain OR design OR manufactur\* OR pro duction OR distribut\* OR logistics OR marketing OR catalog\* OR sales OR retail\* OR e-commerce OR return OR recycl\* OR business OR Per sonali\* OR Virtual Assistant OR Recommend\* System)).

To go around Google Scholar's limitation of up to 256 characters search strings, we hashed the part after the third “AND” operator and combined each of this part's in-between “OR” chunks to the string's top three parts. The string wildcards characters “\*” were also expanded as required by IEEEXplore. The searches over the selected databases “harvested” a total of 19,767 papers as being of potential interest here.

A Python script<sup>4</sup> was applied to filter the harvested papers whose publicly available content (title or abstract) satisfied the conditions of the second and third operands of the search string. The first and fourth operands were intentionally not used in this filtering to recover papers that addressed CM-based decision support approaches for contexts other than fashion, but that could be relevant to our study somehow. The script produced 5800 filtered papers. After removing 309 duplicates using Mendeley tools, we manually inspected the remaining papers to reach a final selection for detailed examination.

## 3.2. Selection criteria in the manual inspection

The 2011–2022 publication window was a criterion applied when the initial searches were carried out. In this last selection step, we manually inspected each filtered paper to check whether it met the se lection criteria. A paper was excluded if it failed to meet at least one of the following selection criteria: the paper contributes to answering at least one RQ; it is peer-reviewed; it is written in English. Checking whether a paper satisfies the first selection criterion is equivalent to verifying whether it proposes: i) a personalized customer modeling approach; or ii) it uses a CM to support decisions in any FRSC domain.

After applying the selection criteria, 54 papers were selected for further detailed analysis; out of these, 48 (89%) used AI- and $^ { 6 , }$ rulebased techniques. Table 1 brings the distribution of finally selected pa pers per searched database. Regarding the selected column, whenever a selected paper was duplicated on search sources, we count it in their correspondent publisher's digital library. Moreover, the papers were published along 47 journals and conferences where the top-1 was the IEEE Transactions on Multimedia with three published papers.

Table 1  
Results per database (Microsoft Academic retired Dec 31st, 2021).

<table><tr><td>Source</td><td>Harvested</td><td>Filtered</td><td>Selected</td></tr><tr><td>ACM Digital Library</td><td>3899</td><td>1292</td><td>11</td></tr><tr><td>Emerald Insight</td><td>957</td><td>322</td><td>3</td></tr><tr><td>Google Scholar</td><td>3711</td><td>998</td><td>1</td></tr><tr><td>IEEE Digital Library</td><td>1207</td><td>1011</td><td>33</td></tr><tr><td>Microsoft Academic</td><td>33</td><td>9</td><td>0</td></tr><tr><td>Scopus</td><td>2111</td><td>930</td><td>4</td></tr><tr><td>Taylor &amp; Francis</td><td>3831</td><td>770</td><td>0</td></tr><tr><td>Wiley Online Library</td><td>4018</td><td>468</td><td>1</td></tr><tr><td>Total</td><td>19,767</td><td>5800</td><td>54</td></tr></table>

The plausibility of the relatively low number of selected articles (54 out of 5800), derives mainly from the requirement that a CM be considered. On the other hand, the number seems plausible when compared to the 144 selected papers in the 2006–2017 literature survey on FRSC decision models [15]. These papers had “conventional” (as termed by the authors) operational research-based or closed-form or computational optimization solutions - only one paper was AI-based, but it did not consider CMs [15].

Each of the 54 papers was then examined to elicit the problem it addresses, its main contributions, the customer or product aspects it considered for personalization, recommendation approaches, validation experiments and metrics, data availability, its limitations, and sugges tions for future work.

## 4. Results and discussion

Results of our systematic literature review are summarized in Table 2. Entries correspond to findings from our reading of the 54 selected papers and serve as a basis to answer the proposed RQs. Given RQ2 and RQ3 relate to how AI-based fashion RSs function, their dis cussions (sections 4.2 and 4.3) are more technical and carried out using AI jargon. For brevity, only basic information are discussed. Indicated references bring clarifications and further details.

## 4.1. Answering RQ1 - Product's, Customer's and context features

Five categories of features were identified: i) products' features (PF); ii) apparel use context (AUC); iii) customer's browsing history (CBH); iv) customer's physical characteristics (CPC); and v) customer's personality traits (CPT). Category ii) represents customers' transient needs (shortterm features) that are valid for specific time-space situations - e.g., a wedding or a beach outing; category v) represent much slower varying features and have an extended life expectancy (long-term preferences); category iv) corresponds mainly to body measurements and colors (of skin, eyes, hair). Exceptionally, categories i) and iii) may be bonded and represent the customer needs through product characteristics (see Fig. 1).

As shown in Fig. 1, PF is omnipresent in CMs. That is not surprising since both customers, retailers, and algorithms need to consider the products themselves to make buying recommendations. On the other hand, we found CPT aspects to be present in one study only [19] - that is possible because it is more difficult to acquire and verify the customer personality traits than its physical characteristics (see also 4.1.4). CPT aspects, however, may be pivotal for personalized online recommen dations. Each of the remaining categories was considered by a third (15) of the investigated papers, and they are not exclusive (check the feature combinations on Table 2).

## 4.1.1. Products' features

Customer's needs related to PF are commonly modeled through a feature vector considering well-defined clothing categories such as skirt, shirt, dress, pants [20]; fine-grained visual attributes, such as colors [21], shapes (sleeves, necklace, length, silhouette) [22,23], fabric [24,25], or even combining category and attribute information [6]. While [26] uses a pre-labeled dataset (structured data) to build the customer feature vector, [8,27,28] require the customer to input an image or textual description of the desired product and apply intelligent algorithms to extract the feature vector from the input.

## 4.1.2. Apparel use context

Customer context may play a meaningful role in his decision-making process due to seasonal changes. Considering this, [29,30] have pro posed location-based approaches, asking the customer to describe through natural language, scenarios (e.g., city, beach, mountain), and the weather where the customer intends to wear the clothing.

Another relevant context-related aspect is the social occasion. [31] applied a binary approach, classifying outfits as casual or party look. Differently, [32] followed a multilabel approach, classifying clothing items into five occasions: office, wedding, sports, dating, or travel.

## 4.1.3. Customer's browsing history

CBH information can be collected through an implicit or explicit process [33]. Based on implicit information, [34,35] identified the customer's needs through its purchase history, and [27] analyzed cus tomer's viewed screens history. Other approaches work with the cus tomer's explicit opinion, such as rating [36], reviews [37], or likes (positive feedback) [2].

As for external sources, information from social networks can be collected, e.g., from fashion bloggers or liked posts to infer customers' needs [38].

## 4.1.4. Customer's personality traits

A single finding considered CPTs in CMs to support personalized decisions in the FRSC [19]. Through questionnaires, they proposed a segmentation of fashion customers based on the concept of E-lifestyles, which means activities, perceptions, attitudes, and values related to the internet as a shopping medium. Three segments were proposed based on the K-Means clustering algorithm: disengaged averse online shoppers, interactive convenience seekers, and adept online shopping optimists. Further, the authors discussed behavior insights that might support fashion marketing strategies, such as which group is likely to accept new technologies or requires a wide range of available products.

## 4.1.5. Customer's physical characteristics

Even though the customer's clothing preferences have a subjective and personal bias, fashion experts usually associate clothing models with two types of human physical characteristics: body measurements and body undertones

Regarding body measurements, [5,39] have modeled the customer according to body types, such as hourglass, inverted triangle, rectangle, round, and triangle. [40] gathered body measurements to propose a 3D virtual body that customers could virtually try on clothing.

As for body tones, the most common aspect is the skin tone, which might be enhanced with eye color and/or hair color [21,24,31].

## 4.2. Answering RQ2 - CM's information acquisition/updating/ representation

The previously described features may be directly provided from uncomplicated structured data or implicitly acquired from the customer as raw data such as RGB images or natural language text. Thus, pre processing techniques may be necessary to extract high-level structured data that compose a customer model. Such techniques may be catego rized according to the data modality. As shown in Fig. 2, image data holding relevant customer information is generally preprocessed by state-of-the-art deep neural networks (DNNs); and less frequently by classical Computer Vision algorithms. For textual data, however, there is still a higher prevalence of classical natural language processing (NLP) algorithms, although text-based DNNs are already being exploited for

Table 2 Literature results.

<table><tr><td>Authors</td><td>Features</td><td>FRSC Domain</td><td>Application</td><td>Output</td><td>IE Algorithm</td><td>Customer Model</td><td>Recomm. Algorithm</td></tr><tr><td>Zhan et al. [27]</td><td>PF, CBH</td><td>Retail (Sales)</td><td>Outfit recomm.</td><td>List of outfits</td><td>ResNet50, Word2vec</td><td>Browsing history</td><td>GraphNN, Similarity scr.</td></tr><tr><td>Koshy et al. [21]</td><td>PF, CPC</td><td>Retail (Sales)</td><td>Outfit recomm.</td><td>VFR</td><td>Color analysis, CNN</td><td>Skin color, Weather</td><td>KNN, Similarity scr.</td></tr><tr><td>Verma et al. [32]</td><td>PF, AUC</td><td>Retail (Sales)</td><td>Outfit recomm.</td><td>List of outfits</td><td>FasterRCNN</td><td>Customer&#x27;s feedback, Gender, Occasion</td><td>K-Modes</td></tr><tr><td>Li and Chen [52]</td><td>PF, CPC</td><td>Planning (Design)</td><td>Gen. custom item</td><td>Single item</td><td>-</td><td>Body measures</td><td>Inference engine</td></tr><tr><td>Stan and Mocanu [20]</td><td>PF, CBH</td><td>Retail (Sales)</td><td>Outfit recomm.</td><td>Pair matching</td><td>CNN</td><td>Customer&#x27;s query, Customer&#x27;s wardrobe</td><td>Pair compatibility scr.</td></tr><tr><td>Zeng et al. [56]</td><td>PF, CPC</td><td>Planning (Design)</td><td>Gen. custom item</td><td>3D clothing</td><td>-</td><td>Body measures, Style</td><td>Fuzzy tree</td></tr><tr><td>Dong et al. [40]</td><td>PF, CPC</td><td>Planning (Design)</td><td>Gen. custom item</td><td>3D clothing</td><td>-</td><td>Body measures, Style</td><td>Inference engine</td></tr><tr><td>Ajmani et al. [31]</td><td>PF, AUC</td><td>Retail (Sales)</td><td>Single recomm.</td><td>List of items</td><td>-</td><td>Color(skin, hair, eye), Body measures, Weather</td><td>Bayesian network</td></tr><tr><td>Banerjee et al. [2]</td><td>PF, AUC</td><td>Retail (Sales)</td><td>Outfit recomm.</td><td>List of outfits</td><td>CNN</td><td>Customer&#x27;s feedback, Occasion, Budget</td><td>Similarity scr.</td></tr><tr><td>Lin et al. [48]</td><td>PF, CPC</td><td>Retail (Sales)</td><td>Single recomm.</td><td>List of items</td><td>CNN, K-Means, Color analysis</td><td>Gender, Height, Customer body pic.</td><td>Similarity scr.</td></tr><tr><td>Gharaei et al. [34]</td><td>PF, CBH</td><td>Retail (Sales)</td><td>Outfit recomm.</td><td>List of outfits</td><td>CNN</td><td>Gender, Customer&#x27;s purchases</td><td>Similarity scr.</td></tr><tr><td>Hao and Hao [24]</td><td>PF, AUC, CPC</td><td>Retail (Sales)</td><td>Single recomm.</td><td>List of items</td><td>Fuzzy NN</td><td>Gender, Skin color, Weather, Occasion, Body measures</td><td>Self-organizing map</td></tr><tr><td>Jo et al. [8]</td><td>PF</td><td>Retail (Sales)</td><td>Outfit recomm.</td><td>Pair matching</td><td>CNN, GAN</td><td>Customer sketch</td><td>Similarity scr.</td></tr><tr><td>Yan et al. [35]</td><td>PF, CBH</td><td>Retail (Sales)</td><td>Single recomm.</td><td>List of items</td><td>CNN, Word2Vec</td><td>Customer&#x27;s purchases</td><td>Knowledge graph</td></tr><tr><td>Hidayati et al. [5]</td><td>PF, CPC</td><td>Retail (Sales)</td><td>Single recomm.</td><td>List of items</td><td>CNN, BiDNN, Color analysis</td><td>Body measures, Customer&#x27;s query</td><td>Knowledge graph</td></tr><tr><td>Pandey and Chawla [19]</td><td>CPT</td><td>Retail (Mktg)</td><td>-</td><td>Cust. segments</td><td>K-Means</td><td>E-lifestyles, Website quality</td><td>-</td></tr><tr><td>Hou et al. [22]</td><td>PF, CBH</td><td>Retail (Sales)</td><td>Single recomm.</td><td>List of items</td><td>CNN, Grad-AAM</td><td>Customer&#x27;s Purchases</td><td>BPR</td></tr><tr><td>Lin et al. [6]</td><td>PF</td><td>Retail (Sales)</td><td>Outfit recomm.</td><td>Pair matching</td><td>CNN</td><td>Customer&#x27;s Query</td><td>RNN, Mutual att. NN, Cross-modality att. NN</td></tr><tr><td>Gu et al. [67]</td><td>PF</td><td>Retail (Sales)</td><td>Outfit recomm.</td><td>Pair matching</td><td>CNN</td><td>Customer&#x27;s query</td><td>Extended-LFM</td></tr><tr><td>Hsieh and Li [9]</td><td>PF, CBH</td><td>Retail (Sales)</td><td>Single recomm.</td><td>List of items</td><td>WordNet, LDA</td><td>Customer&#x27;s feedback</td><td>Similarity scr.</td></tr><tr><td>Yang et al. [28]</td><td>PF</td><td>Retail (Sales)</td><td>Outfit recomm.</td><td>Pair matching</td><td>Siamese NN</td><td>Customer&#x27;s feedback, Budget</td><td>BPR, GAN</td></tr><tr><td>Li et al. [26]</td><td>CBH</td><td>Retail (Sales)</td><td>Outfit recomm.</td><td>Pair matching</td><td>-</td><td>Customer&#x27;s clicks</td><td>GraphNN, BPR</td></tr><tr><td>Lin et al. [68]</td><td>CBH</td><td>Retail (Sales) Planning (Design)</td><td>Outfit recomm.</td><td>Pair matching</td><td>CNN</td><td>Customer&#x27;s query</td><td>Pair compatibility scr.</td></tr><tr><td>Zhang and Caverlee [38]</td><td>PF, CBH</td><td>Retail (Sales)</td><td>Single recomm.</td><td>List of items</td><td>CNN, RNN</td><td>Customer&#x27;s purchases</td><td>Similarity scr.</td></tr><tr><td>Mao et al. [69]</td><td>PF, CPC</td><td>Retail (Sales)</td><td>Single recomm.</td><td>List of items</td><td>-</td><td>Body measures, Skin color</td><td>Inference engine</td></tr><tr><td>Unehara et al. [54]</td><td>PF, CBH, AUC</td><td>Retail (Sales)</td><td>Outfit recomm.</td><td>List of outfits</td><td>-</td><td>Customer&#x27;s feedback, Weather</td><td>Genetic algorithm (GA)</td></tr><tr><td>Vuruskan et al. [39]</td><td>CPC</td><td>Retail (Sales)</td><td>Single recomm.</td><td>Clothing models</td><td>-</td><td>Body measures</td><td>GA, PSO NN</td></tr><tr><td>Lu et al. [70]</td><td>PF</td><td>Retail (Sales)</td><td>Outfit recomm.</td><td>List of outfits</td><td>CNN</td><td>Customer&#x27;s feedback</td><td>BPR</td></tr><tr><td>Polania and Gupte [71]</td><td>PF</td><td>Retail (Sales)</td><td>Outfit recomm.</td><td>Pair matching</td><td>CNN, Color analysis</td><td>Customer&#x27;s query</td><td>Pair compatibility scr.</td></tr><tr><td>Han et al. [45]</td><td>PF</td><td>Retail (Sales)</td><td>Outfit recomm.</td><td>Pair matching</td><td>CNN</td><td>Customer&#x27;s query</td><td>RNN</td></tr><tr><td>Ding et al. [72]</td><td>PF, AUC</td><td>Retail (Sales)</td><td>Single recomm.</td><td>List of items</td><td>CNN</td><td>Customer&#x27;s purchases</td><td>K-Means, CF</td></tr><tr><td>Goel et al. [41]</td><td>PF, CPC</td><td>Retail (Sales)</td><td>Outfit recomm.</td><td>Pair matching</td><td>CED, Color analysis, Photomeasure app</td><td>Body measures, Skin color</td><td>Inference engine</td></tr><tr><td>Sekozawa et al. [73]</td><td>PF, CBH</td><td>Retail (Sales)</td><td>Single recomm.</td><td>Clothing models</td><td>-</td><td>Style, customer&#x27;s Purchases</td><td>Analytic hierarchy, K-Means</td></tr><tr><td>Lin et al. [36]</td><td>PF</td><td>Retail (Sales)</td><td>Outfit recomm.</td><td>Pair matching</td><td>Siamese NN</td><td>Customer&#x27;s feedback</td><td>Pair compatibility</td></tr><tr><td>Sagar et al. [7]</td><td>PF</td><td>Retail (Sales)</td><td>Outfit recomm.</td><td>Pair matching</td><td>CNN, Word2Vec</td><td>Customer&#x27;s outfits history</td><td>BPR</td></tr><tr><td>Wen et al. [53]</td><td>PF, CPC, AUC</td><td>Retail (Sales)</td><td>Single recomm.</td><td>List of items</td><td>-</td><td>Body measures, Gender, Face type, Skin color, Age</td><td>Knowledge graph, Inference engine</td></tr><tr><td>Kottage et al. [37]</td><td>PF, CBH</td><td>Retail (Sales)</td><td>Single recomm.</td><td>List of items</td><td>TF-IDF</td><td>Customer&#x27;s feedback, views, and purchases</td><td>Similarity scr.</td></tr><tr><td>Chen et al. [43]</td><td>CBH</td><td>Retail (Sales)</td><td>Outfit recomm.</td><td>List of outfits</td><td>CNN, TextCNN</td><td>Customer&#x27;s feedback</td><td>Graph embedding, Transformer NN</td></tr><tr><td>De Carolis et al. [65]</td><td>PF, CBH</td><td>Retail (Sales)</td><td>Single recomm.</td><td>List of items</td><td>-</td><td>Customer&#x27;s feedback</td><td>Dynamic belief network</td></tr><tr><td>Goel et al. [50]</td><td>PF, CPC, AUC</td><td>Retail (Sales)</td><td>Outfit recomm.</td><td>Pair matching</td><td>-</td><td>Color(hair, skin), Body measures, Customer&#x27;s query</td><td>Inference engine</td></tr><tr><td>Sapna et al. [46]</td><td>PF</td><td>Retail (Sales)</td><td>Outfit recomm.</td><td>List of items</td><td>CNN, RNN</td><td>Customer&#x27;s feedback</td><td>Constrained CF</td></tr></table>

Table 2 (continued )

<table><tr><td>Authors</td><td>Features</td><td>FRSC Domain</td><td>Application</td><td>Output</td><td>IE Algorithm</td><td>Customer Model</td><td>Recomm. Algorithm</td></tr><tr><td>Deng et al. [74]</td><td>PF</td><td>Retail (Sales)</td><td>Single recomm.</td><td>List of items</td><td>CNN</td><td>Customer&#x27;s feedback</td><td>Similarity scr.</td></tr><tr><td>Surya et al. [49]</td><td>PF</td><td>Planning (Design)</td><td>Gen. custom item</td><td>List of items</td><td>-</td><td>Customer&#x27;s query</td><td>GAN</td></tr><tr><td>Jo et al. [29]</td><td>PF, AUC</td><td>Planning (Design)</td><td>Gen. custom item</td><td>List of items</td><td>Keyword matching</td><td>Customer&#x27;s query</td><td>GAN</td></tr><tr><td>Han et al. [44]</td><td>PF, CBH</td><td>Retail (Sales)</td><td>Single recomm.</td><td>List of items</td><td>CNN, BERT</td><td>Customer&#x27;s purchases</td><td>Deep neural network</td></tr><tr><td>Poorni et al. [55]</td><td>PF, CPC</td><td>Planning (Design)</td><td>Gen. custom item</td><td>Single. item, VFR</td><td>CNN, Color analysis</td><td>Body measures, Skin color, Occasion, Customer&#x27;s feedback</td><td>-</td></tr><tr><td></td><td>AUC</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Zhang et al. [30]</td><td>PF, AUC</td><td>Retail (Sales)</td><td>Outfit recomm.</td><td>List of outfits</td><td>CNN</td><td>Occasion</td><td>SVM</td></tr><tr><td>Kang et al. [23]</td><td>PF, CBH</td><td>Planning (Design), Retail(Sales)</td><td>Single recomm., Gen. custom item</td><td>List of items</td><td>CNN</td><td>Customer&#x27;s Feedback</td><td>BPR, GAN</td></tr><tr><td>Hidayati et al. [42]</td><td>PF, CPC</td><td>Retail (Sales)</td><td>Single recomm.</td><td>List of items</td><td>Color analysis, Bag-of-Visual-Word</td><td>Body measures</td><td>Bayesian classifier</td></tr><tr><td>Lu et al. [75]</td><td>PF, CBH</td><td>Retail (Sales)</td><td>Outfit recomm.</td><td>List of outfits</td><td>CNN</td><td>Customer&#x27;s feedback</td><td>Similarity score</td></tr><tr><td>Ding et al. [51]</td><td>CBH</td><td>Retail (Sales)</td><td>Single recomm.</td><td>Single item</td><td>-</td><td>Browsing history</td><td>GraphNN</td></tr><tr><td>Sharma et al. [25]</td><td>PF, CPC</td><td>Planning (Design)</td><td>Single recomm.</td><td>S3D clothing</td><td>RBFNN</td><td>Body Measures, Style</td><td>Inference engine, Kd-tree</td></tr><tr><td>Yethindra and Deepak [76]</td><td>PF, CBH</td><td>Retail (Sales)</td><td>Single recomm.</td><td>List of items</td><td>Logistic regression</td><td>Customer&#x27;s query, Customer&#x27;s click</td><td>Similarity score</td></tr><tr><td>Zhan and Lin [77]</td><td>PF, CBH</td><td>Retail (Sales)</td><td>Outfit recomm.</td><td>Pair matching</td><td>CNN</td><td>Customer&#x27;s feedback</td><td>BPR</td></tr></table>

![](/api/attachments/M4G83T2R/fulltext/images/727ac884449521025a78fe34bfa8ee7b445ead765cd94999a07228ff6d2e2192.jpg)  
Fig. 1. Yearly distribution of Features in Fashion Customer's Models.

that purpose. It is also worth mentioning that multimodal approaches, which simultaneously combine visual and textual data to acquire customer information. are also found in recent work.

Several DNNs have been proposed for CM's information acquisition from images. Most are based on variants of Convolutional Neural Net works (CNN), including the ResNet architecture [21]: the Faster Region Based CNN (FasterRCNN) [32]; Radial Basis Function Network (RBFNN) [25]; Generative Adversarial Networks (GANs) [8]; and Siamese net works [28]. Alternatively, classical Computer Vision algorithms have been explored in a few methods. For instance, the Canny Edge Detector (CED) was proposed to recognize visual patterns of garments [41]. Color space analysis and Bag-of-Visual-Word (BoVW) histograms are investi gated in [42].

Textual data have been mostly preprocessed through a variety of classical NLP algorithms, ranging from straightforward keyword-based matching methods [29] to sophisticated unsupervised techniques like Latent Dirichlet Allocation(LDA) [9]. Vectorial representations have also been explored, including the classical Term Frequency-Inverse Document Frequency (TF-IDF) representation [37]. Deep Learning methods have also been applied to text. One may find variations of Recurrent Neural Networks (RNNs), including Bidirectional Long Short-Term Memory networks (BiLSTM) [38]; text-based CNN [43]; and stateof-the-art neural network transformers such as BERT [44]. Finally, several researches explored multimodal neural networks capable of simultaneously combining images, texts, and structured information in neural network architecture, as in [27,45,46]. In summary, state-of-theart DNN architectures for both text and images have drawn growing interest recently to develop customer models, and it is expected that they will be even more omnipresent in this scope, as they become easier to use and more widely available.

![](/api/attachments/M4G83T2R/fulltext/images/7e1c998815586cb1c128425c03eeff022873310388ed899f52efd1961cf52efa.jpg)  
Fig. 2. Yearly distribution of information extraction algorithms.

4.3. Answering RQ3 - AI algorithms to perform recommendations using CM's

Fashion recommendations have been typically performed in a customized manner over time by human sales assistants. In this context, three classes of methods have been successfully applied: statistical, computational, and rule-based (developed by specialists). In the last decade, recent developments have allowed AI algorithms to make CM based RSs more easily adaptable and responsive to the current avail ability of customer information, i.e. big data [47].

![](/api/attachments/M4G83T2R/fulltext/images/02c4c6177bbd9aa075719664fd60bc7e5caa2d675a9e9a660bcdd4ce57933867.jpg)  
Fig. 3. Yearly distribution of recommendation algorithms.

According to our literature review, fashion recommendation engines based on AI and customer models are mostly built using ML approaches - with classical ML techniques the most widely adopted category (Fig. 3). It includes supervised approaches, such as the K-Nearest Neighbor (KNN) classifier [21], Bayesian classifiers [42], and Support Vector Machines (SVM) [30]; and unsupervised approaches that try to identify occurring patterns in unsupervised data, like the K-means algorithm [48] and the Self-Organizing Maps (SOM) [24].

A variety of Deep Learning techniques have also been adopted for fashion recommendations. This category includes RNNs [45], attentionbased neural networks [44], which have Transformers [43], and Generative Adversarial Networks (GANs) [49] that are capable of directly synthesizing clothing recommendations in the form of images.

In several rule-based methods, subjective knowledge of clothing experts, in the form of ontologies, is exploited to perform recommen dations. For instance, [50] proposes an ontology to recommend com plementary garments. Differently, [40] presented an ontology-based recommender system for garment design.

Knowledge graphs are also appropriate to represent relevant data and provide recommendations in this context. These graphs may combine customer interactions and product relations, for instance. Several techniques exploit this data structure in the recommendation process, including factorization models [35], graph embeddings [43], and Graph Neural Networks [27,51]. It is worth noting that graphs may be built either to learn embeddings that are subsequently exploited; or to simultaneously learn representations, as in the Hierarchical Fashion Graph Network (HFGN) [26]. Also worth mentioning, straightforward collaborative filtering approaches aiming to provide recommendations based on matching similar user behaviors have also been proposed [46].

## 4.4. Answering RQ4 - application to FRSC decision domains

Only the planning (design) and the retail (sales and marketing) FRSC decision domains are considered in the collected studies.

The vast majority of the selected studies were associated with the retail domain, especially for sales activities (46 papers or roughly 85% of the total) through personalized shopping recommendations but also through marketing activities (1 paper or less than 2%) [19]. A bit less than 17% (9 papers) of the 54 collected studies tackle the planning domain aiming to offer customization in the design process [49,52] (the sum exceeds 100% for a paper may address multiple domains). A simi larly skewed concentration of studies was reported in [15] whose au thors argue it is as expected for the main focus of FRSC management is on downstream stakeholders (retailers and consumers) rather than on those upstream (manufacturers). See also [53] and Section 5.4.

The results show four ways of representing CM support in relation to consumer decision-making, such as single clothing recommendation, full outfit recommendation, complementary outfit, and image genera tion of a new clothing item that matches the customer's needs (Fig. 4a). Fig. 4b shows the output modalities considered in the reviewed litera ture. Most of the studies propose RSs that return lists of single clothing items [9] that fit the customer's needs. For outfit recommendation, two approaches were applied in the studies: the use of combinations ac cording to the initial clothing information provided by the customer [36,41] and the recommendation of a complete list of outfits [43,54].

[40,49] propose a decision support mechanism to generate custom ized fashion items based on the customer's needs, presenting them in the RS's output as a single image [52], or using augmented reality (AR) fa cilities such as virtual fitting rooms (VFR) [55], or item projection onto a 3D virtual body [25,56].

The combination of images or AR with other CM data (e.g., product design preference and body size) may serve other FRSC domains, not just retail, as Nike's Fit tool may exemplify. By using a combination of AI, AR and RSs, the tool scans the foot (with a smartphone camera) to read a customer's shoe size. Nike then stores the acquired data for sizing of future recommendations (retail domain); to project revenue streams from individual customers (planning); and, to establish inventories

Levi Strauss' Chief Strategy Officer, Dr. Katia Walsh, offers another example. In an October 2021 interview,<sup>6</sup> Dr. Walsh commented on strategies for clearing up Covid-19 pandemic's large inventories. While many competitors decided to discount en masse in May 2020, Levi's ran an ML model on (CMs') data to identify “which individual product would sell to which consumers at what price… and discounted only items that had to be discounted but not others. This led to better margins”.

A systematic exploration of how CM/RS may contribute to each FRSC decision domain may be carried out by having [15], and some of the references therein, as a backdrop. For instance, consider demand forecasting as needed to inform some decisions in all FRSC domains. As discussed in [15], such demand has been typically predicted by closedform or approximate (e.g., through numerical computation) models that relate future demand to the item's features and historic sales. Accumu lated data from CM/RSs - e.g., a customer's preferences - may now allow, through AI techniques such as ML, to first learn and then, directly infer not only which item's attributes or merchandising factors but also, customers' characteristics and behaviors steered the demand for that particular item. By having a more comprehensive set of input variables on which to forecast demand, one expects related decisions to become more realistic.

## 4.5. Limitations

This systematic literature review presents limitations. For instance, papers in other libraries and recent dissertations or theses were not collected. Also, oversight or mistakes in our manual inspection, the search string, and the automated script may have missed some relevant studies. Multiple readers double-checked papers to reduce oversight and mistakes. Future work with finer-grained strings and/or other ways of searching may complement the results. On the other hand, the quality of the sources accredits the selected body of knowledge as representative of the theme's state of the art.

## 5. A research agenda

We suggest future research to concentrate on five high-impact directions.

## 5.1. Enhancing customer experience through virtual fitting rooms

A main limitation of retail e-commerce is the difficulty of physically touching or trying on an item [57]. 3D body scan or 3D avatar [57] could feed customers' physical features to VFRs to support better fitting fashion item recommendations. Computer vision algorithms based on Deep Learning can be applied in this context since they have allowed the advent of novel vision-based tools [58].

## 5.2. Supporting sustainability-oriented decisions

Environmental sustainability in the fashion industry is a recent trending research topic [59]. Customers' environmental concerns have not been regularly considered in previous work on CMs, and we thus point out that they need to be rapidly integrated into them. The dis covery of such knowledge from customers has been acquired through laborious approaches, such as scientific investigation. For instance, [27] employed descriptive statistics and regression analysis to explore customer attitudes towards the sustainability of fast fashion products in the UK.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$^{5}$  https://emerj.com/ai-sector-overviews/artificial-intelligence-at-nike/
 $^{6}$  For the AI in Business podcast, (https://emerj.com/artificial-intelligence-podcast/).
</div>

![](/api/attachments/M4G83T2R/fulltext/images/ebac0fc23e4e2b8b441df34192d0eff103b93fdbecdb72ff0fb2aae173493c5d.jpg)  
(a) Papers' support representation for customer decision-making

![](/api/attachments/M4G83T2R/fulltext/images/739578250763017c209601628ff6cc8580444c3bd95bbae7b0e2d7cb978517bc.jpg)  
(b) CMs' output modalities.  
Fig. 4. CM application to FRSC decision domain.

The identification and monitoring of customers' attitudes towards an environmentalist agenda may inform fashion companies to adopt sus tainable fashion value chains. That includes major shifts in logistics, phasing out (over)production, and consumption that fulfills social re sponsibility [59]. In that sense, ML algorithms could be employed to provide not only quick and accurate information about the sustainability profile of companies and places but also customer-centric models for specific companies and fashion segments through the methodical pro cessing of big data.

## 5.3. Modeling Customer's cultural, social and ethical concerns

Customers are also becoming more sensitive about cultural and so cial impacts, along with industry ethics [60]. Also, the Covid-19 pandemic increased customers' awareness of “buying local” for the financial sustainability of local communities and enterprises aiming the preservation of jobs they offer [61]. Georeferences for suppliers, man ufacturers, and logistics could serve to estimate how the local economy benefits from choices an RS presents. And even assist customers to gauge environmental sustainability.

## 5.4. Integration of CMs into online FRSC domains

CMs have been predominantly used to improve sales. Identifying suitable decisions and quantifying the potential of CMs to generate high impact choices in all FRSC domains is still an open research question.

To our knowledge, CMs have not been sufficiently explored to mitigate return logistics costs or to reduce the number of returns from customers. In particular, the latter could be impacted by the research and development of high-quality VFRs (Section 5.1) as Nike's Fit tool (Section 4.4) for shoes suggests. [62] applied mathematical models to support management decisions of item returns based on apparel supply chains features. Complexity is now compounded, however, by the online and quickly varying demands that CM-based operations entail, and one may have to resort to simulation techniques or ML. Learning CMs from post-purchase investigations is also an open research question. As dis cussed by [63], post-purchase behavior plays an important role in

replacement purchases

Implications to other online FRSC domains may be appreciated by drawing feasible scenarios for planning (e.g., “instantaneous design”), for manufacturing and logistics - both in need of new arrangements fo local sustainability.

In the production domain, an appropriate database of CMs could be employed to comprehend a retailer's customers' profiles and identify novel products that could be manufactured to satisfy customers preferences.

Exploiting CMs to improve logistics and warehousing is also worthy of attention. By recognizing patterns of customer preferences and their spatial distribution, one could optimally plan logistics and distribution of products, considering costs and delivery speed, or even predict sales in terms of space and time to anticipate shipping [64].

## 5.5. Evaluating the impact of CMs/RSs to online FRSC processes

An important limitation of the extant literature is the lack of exper iments with CMs in real-life scenarios. [22] avoid experimenting with new customers because of the cold start problem (little or no informa tion on a new customer). [46,65] performed experiments in a laboratory where the customer had only a few options of actions and according to a predefined script. Furthermore, most of the findings focused on evalu ating the accuracy of the recommendation algorithms by simulating the customer [5,23,38]. Future work may experiment in real retail scenarios and consider metrics such as usefulness, novelty, diversity, and seren dipity [66] besides financial indicators.

## 6. Conclusion

This paper presented a systematic review of the 2011–2022 literature on AI-enabled customer model-recommendation system (CM/RS) com binations to support decisions in fashion retail supply chains (FRSCs). Searches on nine prominent digital databases/libraries followed by automatic filtering and manual inspection led to a final selection of 54 studies that answered four Research Questions (RQs) of interest. The answer to RQ1 identified features considered in the literature to build fashion customers' personalized models. RQ2 concerned AI tools and methods to automatically acquire customer information and represent the resulting CM. RQ3 regards AI algorithms that use CMs to provide fashion recommendations. And, the answer to RQ4 indicated where such

CM/RS combinations serve as decision support in FRSCs - as exemplified by Nike and Levi Strauss. Taken together, the answers provided an overview of the state of the art and supported a proposal of a research agenda. The main findings of the state of the art and opportunities fo CM/RS-DSS research were:

• Regarding RQ1, products' features (PF) are used in most modeling efforts, followed by the customer's browsing history (CBH), the customer's physical characteristics (CPC), and apparel usage context (AUC), with customer's personality traits (CPT) receiving the least attention so far. A clear research gap on modeling customers' sus tainability, cultural, social, and ethical concerns was identified.

• As for RQ2 and possibly because of the Covid-19 pandemic, 2019 saw the most publications on AI-based information extraction algo rithms. DNNs are already prevalent for image information extrac tion, while text is still mostly processed by classical algorithms. It is expected that state-of-the-art such as Transformers, will become highly investigated and adopted in the next few years. Other major opportunities for research here relate to methods for high quality and practical acquisition of physical CMs, mainly for virtual fitting room applications.

• The answer to RQ3 points to a preference for classical machine learning algorithms to make fashion recommendations, although Deep Learning methods may become prevalent in the following years.

• Lastly, RQ4 answer appears limited to decision support in the do mains of planning and mostly, retail. As FRSC operations continue to move towards customer-centric, investigating benefits of AI-enabled CM/RS-DSS to other FRSC decision domains should receive atten tion. One notices, however, a lack of methodologies to evaluate the impact of using such DSSs throughout an online FRSC.

Answers to RQ1–4 offered a synthesized body of knowledge, for future reference by theoretical and practical research on the theme. The main contribution of the research agenda is in proposing a compre hensive exploration of CM-driven DSSs and FRSC intersection: estab lishing a framework to research how fashion CMs combined to RS/DSSs could carry online FRSCs to the limit of personalized operation and its implications for creating, manufacturing, delivering, retailing, and post selling fashion products and services.

## Acknowledgements

The authors thank the editor and reviewers whose comments and suggestions much improved the contents of this paper.

## Appendix A. Supplementary data

Supplementary data to this article can be found online at https://doi. org/10.1016/j.dss.2022.113795.

## References

[1] A. Loureiro, V. Migu´eis, L.F. da Silva, Exploring the use of deep neural networks for sales forecasting in fashion retail. Decis, Support, Syst, 114 (2018) 81–93.

[2] D. Banerjee, K.S. Rao, S. Sural, N. Ganguly, Boxrec: recommending a box of preferred outfits in online shopping, ACM Trans. Intell, Syst, Technol. 11 (2020).

[3] V. Banken, Q. Ilmer, I. Seeber, S. Haeussler, A method for smart idea allocation in crowd-based idea selection, Decis, Support, Syst. 124 (2019). 113072.

[4] Y.C. Yang, Web user behavioral profiling for user identification, Decis. Support. Syst. 49 (2010) 261–271.

[5] S.C. Hidayati, T.W. Goh, J.S.G. Chan, C.C. Hsu, J. See, L.K. Wong, K.L. Hua, Y. Tsao. W.H. Cheng, Dress with style: learning style from joint deep embedding of clothing styles and body shapes, IEEE Transactions on Multimedia 23 (2021) 365–377.

[6] Y. Lin, P. Ren, Z. Chen, Z. Ren, J. Ma, M. de Riike, Explainable outfit recommendation with joint outfit matching and comment generation. IEEE Trans. Knowl. Data Eng, 32 (2020) 1502–1516.

[7] D. Sagar, J. Garg, P. Kansal, S. Bhalla, R.R. Shah, Y. Yu, Pai-bpr: personalized outfit recommendation scheme with attribute-wise interpretability, in: IEEE Conference on Multimedia Big Data, 2020, pp. 221–230

[8] J. Jo, S. Lee, C. Lee, D. Lee, H. Lim, Development of fashion product retrieval and recommendations model based on deep learning, Electronics (Switzerland) 9 (2020).

[9] C.Y. Hsieh, Y.M. Li, Fashion recommendation with social intelligence on personality and trends, in: International Conference on Advanced Applied Informatics, 2019, pp. 85–90.

[10] M.M. Tseng, F.T. Piller, The Customer Centric Enterprise: Advances in Mass Customization and Personalization, Springer, 2003

[11] M. Maity, M. Dass, Consumer decision-making across modern and traditional channels: E-commerce, m-commerce, in-store, Decis. Support. Syst. 61 (2014) 34–46.

[12] K.Z. Zhang, S.J. Zhao, C.M. Cheung, M.K. Lee, Examining the influence of online reviews on consumers’ decision-making: a heuristic–systematic model, Decis. Support. Syst, 67 (2014) 78–89.

[13] J. Bobadilla, F. Ortega, A. Hernando, J. Bernal, A collaborative filtering approach to mitigate the new user cold start problem, Knowl.-Based Syst. 26 (2012) 225-238.

[14] K. Goldberg, T. Roeder, D. Gupta, C. Perkins, Eigentaste: a constant time collaborative filtering algorithm, Information Retrieval Journal 4 (2001) 133–151.

[15] X. Wen, T.-M. Choi, S.-H. Chung, Fashion retail supply chain management: a review of operational models, Int. J. Prod. Econ. 207 (2019) 34–55.

[16] M.P. de Brito, V. Carbone, C.M. Blanquart, Towards a sustainable fashion retail supply chain in europe: organisation and performance, Int. J. Prod. Econ. 114 (2008) 534–553.

[17] C. Colombi, P. Kim, N. Wyatt, Fashion retailing “tech-gagement”: engagement fueled by new technology, Res. J. Text. Appar. 22 (2018) 390–406.

[18] H. Snyder, Literature review as a research methodology: an overview and

[19] S. Pandey, D.A. Chawla, Evolving segments of online clothing buyers: an emerging market study. Journal of Advances in Management Research 15 (2018) 536–557

[20] C. Stan, I. Mocanu, An intelligent personalized fashion recommendation system, in, International Conference on Communications, Circuits and Systems (2019) 210–215.

[21] R. Koshy, A. Gharat, T. Wagh, S. Sonawane, A complexion based outfit color recommender using neural networks, in: International Conference on Advances in Electrical, Computing, Communication and Sustainable Technologies, 2021, pp. 1–7.

[22] M. Hou, L. Wu, E. Chen, Z. Li, V.W. Zheng, Q. Liu, Explainable fashion recommendation: A semantic attribute region guided approach. in: International Joint Conference on Artificial Intelligence. 2019. pp. 4681–4688.

[23] W.C. Kang, C. Fang, Z. Wang, J. McAuley, Visually-aware fashion recommendation and design with generative image models. in: JEEE International Conference or Data Mining, 2017, pp. 207–216.

[24] L. Hao, M. Hao, Design of intelligent clothing selection system based on neural network, in: IEEE IT, Networking, Electronic and Automation Control C, 2019 (pp. 1789–1792).

[25] S. Sharma, L. Koehl, P. Bruniaux, X. Zeng, Z. Wang, Development of an intelligent data-driven system to recommend personalized fashion design solutions, Sensors 21 (2021).

[26] X. Li, X. Wang, X. He, L. Chen, J. Xiao, T.S. Chua, Hierarchical fashion graph network for personalized outfit recommendation, in: ACM Conference on Research & Development in Information Retrieval, 2020, pp. 159–168.

[27] H. Zhan, J. Lin, K.E. Ak, B. Shi, L.Y. Duan, A.C. Kot, A3-fkg: attentive attribute aware fashion knowledge graph for outfit preference prediction, IEEE Transactions on Multimedia 1. (2021)

[28] Z. Yang, Z. Su, Y. Yang, G. Lin, From recommendation to generation: A novel fashion clothing advising framework, in: 7th International Conference on Digital Home, 2018, pp. 180–186.

[29] S.Y. Jo, S.H. Jang, H.E. Cho, J.W. Jeong, Scenery-based fashion recommendation with cross-domain geneartive adverserial networks, in: IEEE Conference on Big Data and Smart Computing, 2019, pp. 1–4.

[30] X. Zhang, J. Jia, K. Gao, Y. Zhang, D. Zhang, J. Li, Q. Tian, Trip outfits advisor: location-oriented clothing recommendation. JEEE Transactions on Multimedia 19 (2017) 2533–2544.

[31] S. Ajmani, H. Ghosh, A. Mallik, S. Chaudhury, An ontology based personalized garment recommendation system, in: Conferences on Web Intelligence and Intelligent Agent Technologies, 2013, p. 3, 17–20).

[32] D. Verma, K. Gulati, R.R. Shah, Addressing the cold-start problem in outfit recommendation using visual preference modelling, in: IEEE Conference on Multimedia Big Data, 2020, pp. 251–256

[33] H. Ramampiaro, H. Langseth, T. Almenningen, H. Schistad, M. Havig, H.T. Nguyen, New Ideas in Ranking for Personalized Fashion Recommender Systems, Business and Consumer Analytics: New Ideas. 2019. pp. 933–961

[34] Y.N. Gharaei, C. Dadkhah, L. Daryoush, Content-based clothing recommender system using deep neural network, in: 26th International Computer Conference,

[35] C. Yan, Y. Chen, L. Zhou, Differentiated fashion recommendation using knowledge graph and data augmentation, IEEE Access 7 (2019) 102239–102248.

[36] Y. Lin, M. Moosaei, H. Yang, Outfitnet: fashion outfit recommendation with attention-based multiple instance learning in: The Web Conference. ACM, 2020 pp. 77–87.

[37] G.N. Kottage, D.K. Jayathilake, K.C. Chankuma, G.U. Ganegoda, T. Sandanayake

17th International Conference on Computer and Information Science, 2018, pp. 122–127.

[38] Y. Zhang, J. Caverlee, Instagrammers, fashionistas, and me: Recurrent fashion recommendation with implicit visual influence, in: Conference on Information and Knowledge Management, ACM, 2019, pp. 1583–1592.

[39] A. Vuruskan, T. Ince, E. Bulgun, C. Guzelis, Intelligent fashion styling using genetic search and neural classification. International Journal of Clothing Science and Technology 27 (2015) 283–301.

[40] M. Dong, X. Zeng, L. Koehl, J. Zhang, An interactive knowledge-based recommender system for fashion product design in the big data environment. Inf Sci, 540 (2020) 469–488.

[41] D. Goel, S. Chaudhury, H. Ghosh, Multimedia ontology based complementary garment recommendation, in: IEEE International Conference on Multimedia & Expo Workshops, 2017, pp. 208–213.

[42] S.C. Hidayati, K.L. Hua, C.C. Hsu, J. Fu, Y.T. Chang, W.H. Cheng, What dress fits me best? Fashion recommendation on the clothing style for personal body shape, in: Conference on Multimedia, 2018, pp. 438–446.

[43] W. Chen, P. Huang, J. Xu, X. Guo, C. Guo, F. Sun, C. Li, A. Pfadler, H. Zhao. B. Zhao. Pog: personalized outfit generation for fashion recommendation at alibaba ifashion, in: ACM International Conference on Knowledge Discovery & Data Mining, 2019, pp. 2662–2670.

[44] T. Han, Y. Tian, J. Zhang, S. Niu, Sequential recommendation with a pre-trained module learning multi-modal information, in: IEEE Congress on Cybermatics, 2020, pp. 611–616.

[45] X. Han, Z. Wu, Y.G. Jiang, L.S. Davis, Learning fashion compatibility with bidirectional lstms, in: ACM Internacional Conference on Multimedia, 2017, pp. 1078–1086.

[46] R. Sapna, M. Chakraborty, K. Anagha, K. Vats, T. Baradia, S. Khan, S. Roychowdhury Sarkar, Recommendence and fashionsence online fashion advisor for offline experience, in: International Conference on Data Science and Management of Data, 2019, pp. 256–259.

[47] Q. Andr´e, Z. Carmon, K. Wertenbroch, A. Crum, D. Frank, W. Goldstein, J. Huber, L. van Boven, B. Weber, H. Yang, Consumer choice and autonomy in the age of artificial intelligence and big data. Cust. Needs Solut. 5 (2017) 28–37

[48] Y.R. Lin, W.H. Su, C.H. Lin, B.F. Wu, C.H. Lin, H.Y. Yang, M.Y. Chen, Clothing recommendation system based on visual information analytics, in: International Automatic Control Conference, 2019, pp. 1–6.

[49] S. Surya, A. Setlur, A. Biswas, S. Negi, Restgan: A step towards visually guided shopper experience via text-to-image synthesis, in: IEEE Winter Conference on Applications of Computer Vision, 2020, pp. 1189–1197.

[50] D. Goel, S. Chaudhury, H. Ghosh, Recommendation of Complementary Garments Using Ontology. in: National Conference on Computer Vision. Pattern Recognition. Image Processing and Graphics. 2016. pp. 1–4.

[51] Y. Ding, Y. Ma, W.K. Wong, T. Chua, Leveraging two types of global graph for sequential fashion recommendation. in: International Conference on Multimedia Retrieval, 2021, pp. 73–81.

[52] P. Li, J.H. Chen, A model of an e-customized co-design system on garment design, journal of clothing, Sci, Technol. 30 (2018) 628–640.

[53] Y. Wen, X. Liu, B. Xu, Personalized clothing recommendation based on knowledge graph, in: Conference on Audio, Language and Image Processing, 2018, pp. 1–5.

[54] M. Unehara, Y. Hasegawa, K. Yamada, I. Suzuki, Interactive apparel coordination recommendation system reflecting situation and preference, in: 11th Conference on Soft Computing and Intelligent Systems and 21st Symposium on Advanced Intelligent Systems. 2020, pp. 1–4.

[55] W. Poorni, M. De Silva, C. Weerasinghe, H. Nanayakkara, P. Abeygunawardhana, S. Silva, Trenditex: An intelligent fashion designer, in: Seminar on Research of IT and Intelligent Systems, 2019, pp. 505–510.

[56] X. Zeng, L. Koehl, L. Wang, Y. Chen, An intelligent recommender system for personalized fashion design, in: Joint IFSA World Congress and NAFIPS Annual Meeting, 2013, pp. 760–765.

[57] H. Lee, Y. Xu, Classification of virtual fitting room technologies in the fashion industry: from the perspective of consumer experience, International Journal of Fashion Design, Technology and Education 13 (2020) 1–10.

[58] Y. LeCun, Y. Bengio, G. Hinton, Deep learning, Nature 521 (2015) 436–444.

[59] J. Str¨ahle, V. Müller, Key aspects of sustainability in fashion retail, Green Fashion

[60] H. Park, Y.-K. Kim, An empirical test of the triple bottom line of customer-centric sustainability:fast fashion case, Fashion and Textiles 3 (2016) 25.

[61] A. Butu, I.S. BrumA<sup>¨</sup>ƒ, L. TanasA<sup>¨</sup>ƒ, S. Rodino, C. Dinu Vasiliu, S. Dobo, M. Butu, The directly from local producers, Int. J. Environ. Res. Public Health 17 (2020) 5485–5509.

[62] Y. Li, F. Xu, X. Li, Intelligent systems for managing returns in apparel supply chains, in: Information Systems for the Fashion and Apparel Industry, Woodhead Publishing, 2016, pp. 199–219.

[63] R. Mugge, H.N. Schifferstein, J.P. Schoormans, Product attachment and satisfaction: understanding consumers' post-purchase behavior, J. Consum, Mark 27 (2010) 271–282.

[64] S. Erevelles, N. Fukawa, L. Swayne. Big data consumer analytics and the

[65] B. De Carolis, M. de Gemmis, P. Lops, G. Palestra, Recognizing users feedback from non-verbal communicative acts in conversational recommender systems, Pattern Recogn Lett, 99 (2017) 87–95

[66] S. Fazeli, H. Drachsler, M. Bitter-Rijpkema, F. Brouns, W.V.D. Vegt, P.B. Sloep, User-centric evaluation of recommender systems in social learning platforms:

Accuracy is just the tip of the iceberg, in: IEEE Transactions on Learning Technologies 3, 2018, pp. 294–306. V. 11.

[67] S. Gu, X. Liu, L. Cai, J. Shen, Fashion coordinates recommendation based on user behavior and visual clothing style, in: International Conference on Communication and Information Processing. 2017. pp. 185–189

[68] Y. Lin, P. Ren, Z. Chen, Z. Ren, J. Ma, M. de Rijke, Improving outfit recommendation with co-supervision of fashion generation, in: World Wide Web Conference, 2019, pp. 1095–1105.

[69] Q. Mao, A. Dong, Q. Miao, L. Pan, Intelligent costume recommendation system based on expert system, Journal of Shanghai Jiaotong University 23 (2018) 227–234.

[70] Z. Lu, Y. Hu, Y. Jiang, Y. Chen, B. Zeng, Learning binary code for personalized fashion recommendation, in: Conference on Computer Vision and Pattern Recognition, 2019, pp. 10554–10562.

[71] L.F. Polania, S. Gupte, Learning fashion compatibility across apparel categories for outfit recommendation, in: International Conference on Image Processing, volume 2019-September, 2019, pp. 4489–4493.

[72] H. Ding, X. Su, Z. Xie, Multi-models dynamic recommendation for offline clothing sales, in: Conference on Cloud Computing and Big Data Analysis, 2019, pp. 237-243.

[73] T. Sekozawa, H. Mitsuhashi, Y. Ozawa, One-to-one recommendation system in apparel online shopping, Electronics and Communications in Japan 94 (2011) 51–60.

[74] Q. Deng, R. Wang, Z. Gong, G. Zheng, Z. Su, Research and implementation of personalized clothing recommendation algorithm, in: International Conference on Digital Home, 2019, pp. 219–223.

[75] Z. Lu, Y. Hu, Y. Chen, B. Zeng, Personalized outfit recommendation with learnable anchors, in: IEEE Conference on Computer Vision and Pattern Recognition, 2021, pp. 12717–12726.

[76] D.N. Yethindra, G. Deepak, A semantic approach for fashion recommendation using logistic regression and ontologies, in: C. on Innovative Computing, Intelligent Communication & Smart Electrical Systems, 2021, pp. 1–6.

[77] H. Zhan, J. Lin, Pan: Personalized attention network for outfit recommendation, in: Conference on Image Processing, 2021, pp. 2663–2667.

Artur Pereira is a PhD student at the Federal University of Campina Grande (UFCG), Brazil. He holds a Master's degree in Computer Science from Federal University of Alagoa (UFAL), Brazil. Currently, he is an Application Developer at IBM Brazil. His research in terests are Machine Learning, Personalized Recommender Systems, Deep Learning, Nat ural Language Processing, and Knowledge Representation.

J. Antão B. Moura got his PhD in Electrical Engineering from the University of Waterloo Canada in 1982. Ant˜ao is currently a Professor of Computer Science at the Federal Uni versity of Campina Grande (UFCG), Brazil. Over the years, he has worked extensively on modeling and performance evaluation of computer networks. More recently, he has been researching IT economics and its applications to business-driven IT management partic ularly of (fashion) e/m-commerce scenarios.

Evandro de Barros Costa is Professor at Federal University of Alagoas, Brazil. He received a B.S. degree in Computer Science from Federal University of Paraiba (UFPB), Brazil in 1988, an M.Sc. and a Ph.D degree in Electrical Engineering from UFPB in 1989 and 1997. His research interests include knowledge representation and reasoning, personalized recommendation systems, machine learning and multiagent systems.

Thales Vieira is Professor at the Institute of Computing. Federal University of Alagoas (UFAL). Maceió. Brazil. He holds a PhD degree in Mathematics from Pontifical Catholic University of Rio de Janeiro (PUC-Rio) in 2010. His current research interests include Machine Learning, Computer Vision, Natural Language Processing and Pattern Recognition.

Andre ´ Landim is a MS student at Federal University of Campina Grande (UFCG), Brazil. He is a Software Engineer at UFCG. His research focuses on Artificial Intelligence.

Eirini Bazaki is Senior Teaching Fellow in Fashion Management Marketing and MA Coordinator of MA Luxury Brand Management, MA Fashion Management, MA Fashion Marketing and Branding at the University of Southampton, UK. Eirini is a graduate of Saïd Business School, University of Oxford, a Fellow of the UK Higher Education Academy, holds a PhD in Marketing from Adam Smith Business School, University of Glasgow, an MSc in Management Research from the University of Glasgow, an MSc Degree in Mar keting Management from Aston University and a BSc (Hons) in Sociology from the department of Social Sciences. Panteion University. Eirini research interests lie in fashion marketing, e-branding and e-retailing for fashion and luxury fashion brands. Her research work is published in leading academic books and international journals and has previously been presented at the 2021 Global Fashion Marketing Conference, 2019 Academy for Design Innovation Management Conference UK, the European Academy of Marketing Conference and Athens Institute for Education and Research. Eirini actively advises fashion and luxury fashion brands on how to build a strong brand identity, connect with customers and drive sales through digital channels.

Vanissa Wanick holds a PhD in design from the University of Southampton, UK, MBA in Marketing from Federal Fluminense University (UFF), Rio de Janeiro, Brazil and a BA in Design at PUC-Rio, Rio de Janeiro, Brazil. Currently, she is teaching fellow at the Uni versity of Southampton (Winchester School of Art). Her research interests are

multidisciplinary and include cross-cultural Human-Computer Interaction (HCI), games design, creativity and diversity, design innovation, games user research methods, gamification, immersive technologies like Virtual Reality (VR), games for behavior change and sustainable consumer behavior across cultures.
